# Checkpoint Review — 95–99

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

# Chapters 95–99

## Plot

Hong Woojin uses a kitten Familiar to infiltrate and surveil Jin Taekyung’s household, but Hayeon’s affection traps him in her room until he engineers a filthy escape. Taekyung recognizes Woojin when he returns home and later uses the two kitten Familiars and a staged phone call about a USB to bait the surveillance teams.

Sangdong Guild’s six-person Security Team, operating under Guild Master Im Chunsoo’s special order, identifies the three recently traded apartments near Taekyung’s home as possible surveillance bases. Convinced that Taekyung possesses valuable intelligence, Security Team Leader Choi Byungil authorizes an illegal attempt to seize the USB. Taekyung leads the team to a deserted mountain clearing, exposes their identities and affiliation, and reveals that the USB contains only his porn collection. After Choi orders the attack, Taekyung shatters an attacker’s dagger and begins the fight.

Hong Woojin observes the Sangdong team preparing to use violence and quits his assignment, reporting the decision to the Team 1 Leader.

## Continuity

- Sangdong Guild’s Security Team is conducting surveillance under a special order from Guild Master Im Chunsoo.
- Choi Byungil is the B-rank Security Team leader, with a Level in the mid-sixties. The other five field watchers are C-rank Hunters around Levels 30–40: Kim Gwondong, Park Hyungjin, Oh Gyuhyeon, Lee Mincheol, and Kim Junsu.
- Kim Junsu is Sangdong’s sole Familiar mage, a Level 41 C-rank mental mage suffering exhaustion and anxiety about his hair loss.
- The team uses black and white kitten Familiars and eavesdropping-magic Equipment installed in nearby real-estate offices.
- Taekyung identified three possible surveillance bases within five hundred meters of his home: Building 5, Unit 901; Building 4, Unit 302; and Building 3, Unit 202. Which one is occupied remains unknown.
- Taekyung scanned the apartment complex and parking lot with Qi Sense and found no suspicious vehicles.
- Taekyung deliberately baited the team with a phone call and a USB stored in his Inventory. The USB contains his porn collection, not intelligence.
- Taekyung has identified all six Sangdong watchers and confirmed their affiliation. The confrontation is underway in a deserted mountain clearing.
- Hong Woojin was recognized by Taekyung while infiltrating the home as a kitten Familiar. He maintains a rooftop supply-closet hideout at Taekyung’s apartment building and has quit the assignment after witnessing the planned violence.
- Hayeon is at the library; the two kitten Familiars were left with Taekyung before the bait operation.
- Unresolved: why Im Chunsoo issued the special warning about Taekyung; who Taekyung called; which apartment is the surveillance base; whether the black Familiar and Kim Gwondong share immediate instructions; and whether Woojin’s investigation and Sangdong’s operation have the same commissioning chain.

## Translation Decisions

- Retain **Familiar**, **Link**, **Qi Sense**, **Inventory**, **Lock**, and **third-awakening Hunter**.
- Use **mental mage** for 정신계 마법사 and **Security Team** for 보안팀.
- Use **Yeoreum** for 여름이 and **Midsummer** for the rejected naming pun.
- Render **도청 마법** as **wiretapping magic** and **도청 마법 Equipment** as **eavesdropping-magic Equipment**, according to context.
- Render **개냥이** as **dog-cat** with an explanatory footnote.
- Render **역마살** as **yeokmasal**, with a footnote explaining its wandering-fate meaning and age-related pun.
- Render **공(公)만 뺏기다** as **merely taking the credit** and **쇠뿔도 단김에 빼라** with the idiom about pulling the ox’s horn while it is hot.
- Preserve Hong Woojin’s profane, self-deprecating, deadpan comic voice; render **현자 타임** as **post-nut clarity**.

## Durable state

{
  "active_continuity": [
    "Sangdong Guild's Security Team is monitoring Jin Taekyung with its sole Familiar mage, Kim Junsu, and multiple C-rank stealth and tracking Hunters.",
    "Kim Junsu is a Level 41 C-rank mental mage who uses Familiars and is suffering from exhaustion and anxiety about his hair loss.",
    "Kim Gwondong is a Level 42 C-rank Security Team Hunter assigned to surveillance and disguises himself as a friendly neighbor.",
    "The Security Team has watched Taekyung for days and installed eavesdropping-magic Equipment in nearby real-estate offices.",
    "The Security Team uses a black Level 2 Cat Familiar to track Taekyung after he leaves home.",
    "Taekyung detects the black kitten as a Familiar and recognizes Kim Gwondong's disguise while concealing his suspicions.",
    "Taekyung learned of three properties traded within five days and five hundred meters of his home: Building 5, Unit 901; Building 4, Unit 302; and Building 3, Unit 202.",
    "Taekyung scanned the apartment complex and parking lot with Qi Sense and found no suspicious vehicles.",
    "The watchers are using one of the three recently traded apartments as a surveillance base, but the exact property remains unknown.",
    "Hong Woojin infiltrated Taekyung's home as a kitten Familiar and was recognized by Taekyung after Hayeon confined him.",
    "Hayeon left for the library, leaving Taekyung alone with the black and white Familiars.",
    "Taekyung searched his home with mana-detection Equipment and made a suspicious phone call as bait; the Security Team interpreted it as evidence of a secret plan and a USB.",
    "The Security Team's surveillance operation is being conducted under a special order from Guild Master Im Chunsoo.",
    "The Security Team Leader, Choi Byungil, orders an illegal attempt to subdue Taekyung and take the USB.",
    "Choi Byungil is a B-rank Hunter with a Level in the mid-sixties; the other five field watchers are C-rank Hunters around Levels 30 to 40.",
    "The two kitten Familiars are released after Taekyung's bait works, and Taekyung leads the watchers to a deserted mountain clearing.",
    "The USB is bait containing Taekyung's porn collection, stored in his Inventory.",
    "Hong Woojin maintains a hideout in a rooftop supply closet at Taekyung's apartment building and quits his assignment after observing the planned violence.",
    "Taekyung identifies the six watchers, confirms their Sangdong Guild affiliation, and begins fighting them after shattering an attacker's dagger."
  ],
  "continuity_sources": [
    98,
    99
  ],
  "open_questions": [
    "Why did Im Chunsoo issue a special warning about Taekyung?",
    "Which of the three recently traded properties is being used by the surveillance personnel?",
    "Whether the black Familiar and Kim Gwondong are operating under the same immediate instructions remains unresolved.",
    "Whether the Security Team's operation and Hong Woojin's investigation share the same commissioning chain remains unresolved.",
    "Who Taekyung called remains unknown."
  ],
  "safe_through": 99,
  "temporary_decisions": [
    "Render 정신계 마법사 as mental mage and 보안팀 as Security Team.",
    "Use Kim Junsu, Kim Gwondong, Nabi, and Goyang for 김준수, 김권동, 나비, and 고양시.",
    "Render 개냥이 as dog-cat with an explanatory footnote.",
    "Use target, Familiar, Link, and eavesdropping-magic Equipment for 표적, 패밀리어, 링크, and 도청 마법 장비.",
    "Render 도청 마법 as wiretapping magic when referring to the magic itself.",
    "Render 월세 as monthly rent and 전세 as jeonse lease.",
    "Render 홀아비 냄새 as old-bachelor smell.",
    "Render 현자 타임 as post-nut clarity in Hong Woojin's comic internal narration."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 95

# Chapter 95

*Heh heh heh. Success.*

Hong Woojin smiled smugly. He was a veteran at monitoring his targets’ every move and extracting every bit of information from them.

The information that Jin Taekyung’s younger sister was crazy about animals—cats in particular—had been especially useful.

“Meow-meow, answer me. You like being inside the house, don’t you?”

The infiltration had been natural and successful. Inside the kitten’s body, Hong Woojin let out a roar of joy.

“Miaowww.”

“Ahh, so cute! Oppa, did you hear that just now? You heard it, right?”

“Yeah. I heard it.”

“How can you be so indifferent to such a cute little creature? Are you even human?”

“Then what am I, a beast?”

The problem was Jin Taekyung.

Even the most emotionally dried-up person tended to soften in front of a cute animal, especially a tiny one, but…

“Move over a little. You’re blocking the TV.”

This guy had none of that. His sensitivity was drier than the Sahara Desert, and his younger sister, Jin Hayeon, grumbled.

“Good grief, there’s a limit to how bleak a person can be. Right, Yeoreum?”

“Yeoreum?”

“Yeah. Born in summer, so Midsummer. Pretty, right?”

“What do you mean, Midsummer? Judging by the size, the kitten looks about three months old. That would mean it was born in late spring, so call it Late Spring or something.”

“…Is that supposed to be a joke or what? Anyway, this kitten’s name is Yeoreum from today onward. Right, Yeoreum?”

“Mrowww.”

From Hong Woojin’s perspective, Jin Hayeon was his greatest asset. Thanks to her, everything was going smoothly.

“Ahh! Yeoreum answered! You just answered your big sister, didn’t you? Didn’t you?”

“Miaow.”

“Eek, my heart!”

*Heh. What an easy one to handle.* All it took was a few meows, and she practically melted.

*This is why high-school girls are… No, wait. It’s because my choice of Familiar was excellent.*

Hong Woojin was grinning contentedly when—

Jin Taekyung, who had been staring blankly at the TV, casually tossed out a remark.

“Isn’t that one male?”

“Huh? Well, that…”

“We don’t know yet, do we?”

“Come to think of it, I haven’t checked.”

“Let’s take a look. We can find out.”

Huh?

Things were taking a strange turn. His body might have been a cat’s, but Hong Woojin was a vigorous young man. When Jin Taekyung’s large hand approached, a sense of shame suddenly washed over him.

*That filthy bastard is going to look at my junk?*

Strictly speaking, it wasn’t Hong Woojin’s body. Since the species were different, the physical structures were different, too.

However, Familiar magic made the caster and the Familiar share everything. There was no helping the disgust he felt.

*Absolutely not!*

Hong Woojin hurriedly burrowed into Jin Hayeon’s arms.

“Mrowww.”

“Oh my, I don’t think the kitten likes that.”

“That’s how the world works. Who gets to live doing only what they want?”

“But Yeoreum’s a cat.”

“Cats are the same. If you want warm feed and even a can of treats, you have to put up with this much.”

What a lunatic. He was spouting ridiculous nonsense just because he wanted to check a cat’s sex. Grinding his teeth, Hong Woojin clung to his only hope, Jin Hayeon.

He rubbed his entire body against her arm and gave her a pitiful look. Her eyes slowly softened.

“What am I going to do? Yeoreum’s so cute I could die.”

“Yeah, very cute. So let’s take a look.”

“Do it next time. You’re scaring the kitten.”

“That’s just your imagination.”

“I told you, Yeoreum doesn’t like you, Oppa.”

The key was to let out a groan at exactly the right moment.

“Mnyaa. Mngh.”

“See? I’m right, aren’t I?”

“…Then I can’t help it.”

“Don’t you dare force the kitten to let you handle it. Kittens are sensitive, so you have to be careful with them.”

Good. He had gotten past the immediate crisis. Jin Taekyung seemed like a lunatic who lived in his own world, but he was weak when it came to his family.

Having fully absorbed all the background information Sangdong Guild had given him, Hong Woojin thought he was one step ahead.

*This is why information matters. You’ve already fallen right into my trap.*

But there was one fact Hong Woojin had never imagined.

“Hey, Sis.”

“Yeah?”

“Do you need more spending money?”

“…Are you trying to bribe me so you can mess with our Yeoreum?”

“Yeah. A hundred thousand won.”

“Deal. But you have to be gentle so she doesn’t hate you too much, okay?”

“My wallet’s on the desk in my room. Go get it.”

“Eek!”

“Miaow?”

Jin Hayeon disappeared like a bullet. Hong Woojin let out a cry filled with disbelief.

*You said she was so cute you could die. You called her our Yeoreum!*

*What a shameless little brat.*

One minute she had acted ready to give Yeoreum anything, and now she was abandoning “our Yeoreum” for a mere hundred thousand won?

But he was given no time to lament the realities of a capitalist society.

“Come on. Let’s play.”

He grabbed him.

Jin Taekyung restrained all four of his limbs with lightning speed and smiled horribly.

Hong Woojin screamed desperately.

*Let go! Let go, you son of a bitch!*

“Hiss! Hissss!”

The kitten’s fur stood on end as Hong Woojin hissed, catching the attention of his only hope as she rummaged through Jin Taekyung’s wallet.

“Oppa!”

“Yeah, take another hundred thousand won.”

“Thanks!”

*Hey! Hey!*

His only hope had become a slave to capitalism!

Before the shock had even worn off, Jin Taekyung’s hot breath swept over him.

“Our Yeoreum, shall we take a look at your little peepee?”

At that desperate, life-or-death moment—

*Sever Link!*

“Miaowww!”

With a sorrowful cry, all the strength drained out of the kitten’s body.

Then Hong Woojin opened his eyes somewhere dark and let out a breath.

“Puhack!”

Since starting work as a Hunter, he had handled more than a hundred large and small assignments, but this was the first time he had ever felt his life was in danger.

He looked down at his forearms, which were covered in goose bumps, and began to gag.

“Urgh.”

His stomach churned, and his head throbbed.

It was a side effect of the sudden Link severance. Only after he gulped down the potion he had prepared in advance like cold water could Hong Woojin finally catch his breath.

“Jin Taekyung, you fucking bastard…”

It was the moment he first regretted ever accepting the assignment.

* * *

> **System**
>
> **Lv. 2 Cat**

“There he goes.”

Clicking my tongue, I let the kitten go. Was it three months old? The little thing, smaller than my two joined palms, backed away with a bewildered expression.

“Miaow.”

Hayeon was leaving my room when she spotted what had happened.

“You didn’t do anything mean to our Yeoreum, did you?”

“And you’re the one who sold Yeoreum for 200,000 won?”

“…Ahem. Ahem.”

“Whatever. Good grief. Whenever you pick something up, it has to be something like that.”

“What are you talking about? Look how cute Yeoreum is.”

“That’s not what I meant… Never mind. Forget it.”

It was a long and complicated story to explain one detail at a time. Besides, I had no intention of explaining it.

If I told her that some sinister bastard had entered the body of a cat and was watching us, it was obvious how anxious she would become. My family couldn’t find out about what was happening.

*Besides, I was the one who had allowed it.*

The reason I had let a Familiar into the house wasn’t because Hayeon had asked or because Mom had given her permission.

*It was because I wanted it.*

I didn’t know who had hired them, but even if I drove them off now, they would keep trying.

It didn’t matter whether the Familiar took the form of an insect like last time or a cat like today.

What mattered was that I already knew what the Familiar was and could swat it away whenever I wanted.

*They’re definitely somewhere around here.*

Within 500 meters of the house. Somewhere inside that radius was a mage controlling the Familiar. If I roughed him up, I was sure I’d find the connection.

*First, I’ll punch him in the mouth, then ask some questions.*

He had illegally surveilled a civilian, so there was no way he could report me even if I beat him. Just thinking about teaching him a proper lesson made my fists itch.

*How dare they snoop around someone’s house?*

They had interrupted my first vacation in a long time, and thanks to these bastards, I had already spent well over 300 million won. In every respect, this was a losing proposition.

I was watching TV with my face twisted into a scowl when Hayeon cautiously watched my reaction and spoke.

“Oppa, are you mad?”

“No. What is there to be mad about?”

“I’m sorry.”

“…What’s gotten into you? You’re starting to scare me.”

I wasn’t joking. I was more startled than when I had first discovered the Familiar. Since when could she say something like that?

I asked seriously.

“Are you sick?”

“No, it’s just…”

“Then are you hungry?”

“That’s not it…”

Just as Hayeon hesitated, apparently about to say something, a stomach growled from somewhere.

It wasn’t mine. Mom had stepped out to run an errand.

“You’re hungry.”

“Mm, a little?”

“Right. You’re so hungry you’re starting to spout nonsense. You know where my wallet is, right? Order anything you want to eat.”

“Really?”

“Yeah. Up to 100,000 won.”

“Wow, now that you’re making money, you’ve gotten generous, Oppa.”

In all my life, I never thought I’d hear her call me “our Oppa.” It was the first time I’d heard it since Hayeon had been in middle school, and it gave me goose bumps.

“You’re the Familiar, you little bastard!”

“What are you talking about? Anyway, can I order whatever I want as long as it’s under 100,000 won?”

“Yeah. No, wait. Fine. Order everything you want.”

“What about the money left over?”

“…Did you leave your money with me?”

“More is better.”

I was dumbfounded by Hayeon’s shamelessness, but at the same time, I was happy.

She had never once asked me for spending money. Even judging by the clothes she wore and her usual appearance, she was far more modest than the kids her age I occasionally saw on the street.

*What an old soul.*

Come to think of it, Hayeon had been like that since she was little. She rarely cried, and she didn’t often express her feelings honestly. Her current personality had only developed after she entered high school.

*She ought to be allowed to act spoiled once in a while… She grew up too soon.*

*Maybe even much sooner than I did.*

Maybe that was why. None of her actions or words annoyed me in the slightest. If anything, I found her admirable, and I was happy.

“Fine. Take it all. Take everything.”

“Really?”

“Yeah.”

Hayeon beamed at my words.

“That’s a relief. I almost felt bad for nothing.”

“What’s there to feel bad about?”

“I took 300,000 won from your wallet earlier.”

“…Huh?”

“But when you said I could have whatever was left after eating within the 100,000-won limit, I felt better.”

“Hold on. Didn’t I tell you to take 200,000 won?”

“It was an accident.”

“…Don’t you mean a crime of opportunity?”

I take back what I said earlier.

The sight of her back as she hummed her way into her room couldn’t have been more irritating.

* * *

The head of Sangdong Guild’s Security Team frowned.

“A Cat Familiar?”

“Yes, I’m certain.”

The person who answered in a firm voice was a member of the Security Team and the Guild’s only Familiar mage. He was only a C-rank Hunter, but he was also a core member of the Security Team because mental mages were rare.

“The target’s younger sister is a cat fanatic. Hong Woojin took advantage of that opening perfectly.”

“Can’t you read the room? You’re praising that bastard in front of me?”

“I-I’m sorry.”

“Team 1 Leader said Hong Woojin called and went ballistic, saying he nearly got exposed because of us.”

“…”

“Come to think of it, that bastard is technically on our side, too. But can we afford to be outdone by a freelancer? Don’t you know the Guild Master is taking a special interest in this?”

Six people had been assigned to this operation, including the Security Team Leader. One was the Familiar mage, four were close-combat Hunters specializing in tracking and stealth, and the Team Leader himself was a B-rank Hunter.

“I think you’re under a misconception… We didn’t come here just to dig up dirt on one C-rank Hunter.”

The Security Team Leader glared at his team with a menacing expression.

The Guild Master had personally ordered this operation. They had to produce results that went beyond the direct order, no matter what.

“Let’s do this properly. This came straight from the Guild Master. Are you going to let your careers end here? You want bonuses and promotions, don’t you?”

The team members silently lowered their heads.

The person most desperate for a bonus and promotion was the Security Team Leader himself. The hysteria of a middle-aged family man whose retirement was slowly approaching was nothing new by this point.

“And you.”

The Security Team Leader pointed at the Familiar mage.

“You do the cat, too.”

“The cat? They already did that over there.”

“What, then? Are you going to put on another pathetic performance with a tiny Familiar you can’t even control and die like last time?”

“…”

“Do as you’re told. The girl’s a cat fanatic, isn’t she?”

If they wanted a cat, he had to use a cat. What else could he do?

After the Security Team Leader stormed out, the Familiar mage immediately turned on his smartphone and began searching.

Tap. Tap. Tap.

> **Ilsan Cat Adoption**

“…Do you think this will count as a business expense?”
## Chapter artifact 96

# Chapter 96

Kim Junsu was a C-rank Hunter belonging to Sangdong Guild’s Security Team.

He had not an ounce of talent for elemental magic, but fortunately, he had awakened as a rare type of mage—a mental mage—and was living a fairly successful life.

*Except for the fact that I can’t go home.*

What good was owning a house larger than 330 square meters? As the only Familiar mage in Sangdong Guild, he never ran out of work.

Raid teams at least got to go home after running a Gate, but the Security Team had no such luxury. They had to spend every night in a different hideout.

“Junsu, did you pull an all-nighter?”

“Yes.”

A colleague on the Security Team clicked his tongue when he saw Kim Junsu’s hollowed-out face. He was the one person who had stayed behind to protect their valuable Familiar mage.

“You’re working hard. How does that bastard manage not to step outside even once?”

“I know. We’ve been watching him for days, and he’s only gone out twice. Twice. Once to a real-estate office in Goyang and once to the Ilsan Store.”

“This is why it’s better when the target smokes. At least smokers come outside to have a cigarette.”

They had obtained a new cat to use as a Familiar and waited all night at the entrance of the apartment building, but the target had not budged.

The only incident was when the cat, exhausted from waiting, started meowing and was nearly chased away by a security guard.

“Peace Guild? It looked pretty small. Do they even go on raids?”

“They’re on vacation right now.”

“Vacation?”

“Yeah. A guy from Team 2 is watching the other members of Peace Guild, and apparently they’re all taking time off.”

“Ah… How’s that situation going?”

“They pulled out yesterday. There was one woman and one middle-aged man, but it ended quickly. Judging by the Team Leader’s reaction, it seems like they turned up something over there, but I don’t know the details.”

“Phew. We should just do enough to get by and pull out, too.”

His colleague looked at Kim Junsu with pity as he let out a deep sigh.

“There has to be a reason they specially assigned the Guild’s only Familiar mage, right?”

“He’s still only a C-rank Hunter. Don’t you think this is going a little overboard?”

“What can we do? When we’re told to do something, we have to do it. Even if the Team Leader hounds us like he did yesterday, we just have to put up with it.”

“He should hound us in moderation. This would’ve been over ages ago if he had just talked to that Hong Woojin guy and cooperated properly.”

“He wants to show the Guild Master. ‘Our Security Team is much better than Hong Woojin. My leadership is this outstanding.’ Besides, it’s almost time for the second-half personnel reshuffle. No wonder the Team Leader is sweating bullets.”

“…This is driving me insane.”

“It is.”

Kim Junsu wanted to tear his hair out, but he held himself back. If he did, the hair that had only just begun sprouting like fresh spring shoots might come right out.

*Ah, the doctor said stress makes hair loss worse.*

The doctor was a civilian who couldn’t even use the simple Light magic, but if he could give Kim Junsu a full head of hair, Junsu would worship him as Jesus.

*Come to think of it, maybe I haven’t lost much hair today.*

That was when Kim Junsu cautiously reached up to feel the crown of his head.

—Target confirmed. Target confirmed. Moving!

A low but urgent voice came through the radio.

The two men in the room—and even the Security Team Leader, who had been snoring in the next room—bolted upright.

Slurp. After wiping the drool from his mouth, the Team Leader shouted.

“Hey! Kim Junsu!”

*Damn it. I haven’t even eaten breakfast yet.*

*Using Familiar magic makes my hair fall out again!*

*Fuck this. I’m quitting the Guild the moment my contract ends.*

Swallowing back his tears, Kim Junsu drew up his mana. His head grew hot, and his consciousness was pulled inward.

*Faithful servant, answer my call. Link!*

Whoosh!

The next moment, a kitten lying beneath a car opened its eyes wide.

“Myaowww.”

* * *

I stopped walking.

A black ball of fur had suddenly popped out with a cry.

> **System**
>
> **Lv. 2 Cat—Familiar**

“…”

Another cat. Did these bastards have no creativity at all?

Well, one thing was different. This one’s fur was pitch-black.

“Miaow. Miaowww.”

The kitten approached with surprisingly confident steps for such a young creature, then rubbed its entire body against my slipper. Whoever had cast the spell clearly knew its way around a club.

*Man. I don’t like getting attention this way.*

But the appearance of this new Familiar allowed me to make a new guess.

*Could they be working together?*

Two conspicuous Familiars, both in the form of cats, appearing a day apart? It was hardly a good approach. If anything, it felt like someone had hurriedly copied the first attempt.

“Meow!”

The cat cried as if demanding my attention, and I let out a quiet laugh.

“You little thing. You’re cute.”

Should I take it with me or not…?

My mind was racing when—

“That cat’s pretty affectionate. Is it yours, sir?”

A man approached, dragging his slippers. He looked to be in his early forties, with an utterly ordinary face. His stretched-out T-shirt and soccer shorts stained with ramen broth gave him a friendly, familiar air.

“No. I think it’s a stray, but it suddenly started acting affectionate.”

“Wow, this is totally one of those. A dog-cat.”[^1]

“Exactly. Just like yesterday. I guess the cats in this neighborhood are pretty affectionate.”

“Yesterday?”

“Yeah, I picked up another one yesterday. It was a dog-cat, too.”

“That’s strange.”

The man took a drag from a half-burned cigarette.

“When you look at things like this, even animals seem to have connections with people. The cat’s acting affectionate because you look like you’d make a good owner.”

“Come on, what do you mean, a good owner? I think it just has this kind of personality.”

“Is that so? Hey, hey, come here.”

The cat did not move at the man’s beckoning.

No, it burrowed between my legs instead.

“Well, look at this one. Young as it is, it already knows how to pick its people.”

I only smiled without saying anything, so the man asked,

“So, are you planning to raise it?”

“I’m not sure. I have somewhere urgent to be right now. If it’s still here when I get back, I’ll keep it for a few days.”

“Who knows if it’ll still be here by then. Right, Nabi?”

“Mrow.”

“It won’t take long. I’m just going to the real-estate office right over there.”

“Really? Oh, come to think of it, I’ve never seen you before, young man. I’ve lived here a long time, so I know just about everyone. Since you’re going to a real-estate office, are you moving into the neighborhood?”

“I live somewhere else, so I only come by to see my family once in a while. I just have something to take care of at the real-estate office.”

“Ah…”

Phew. His final breath of smoke scattered in the wind. The man flicked his cigarette butt onto the ground and spoke.

“Well, look at me, holding up a busy man. You’re not offended, are you?”

“Not at all.”

“Then that’s good. If we meet again, let’s say hello. We’re neighbors, after all.”

I answered,

“Yes. We’re neighbors.”

“Then I’ll be off. The weather’s nice, so I should take a lap around the neighborhood.”

The man gave me a good-natured smile and started walking. I watched his retreating back for a moment as he moved away with a loose, swinging gait.

*He’s good at acting.*

“Meow.”

Right. You’re here, too.

The moment I left the house, I met two actors. Actors wearing the guises of a stray cat and a neighbor.

“I’ll be back soon, so wait here quietly, okay?”

The cat tilted its head as if it had no idea what I was talking about.

But I knew. I knew that it understood me—and that it would still be sitting here even after several hours had passed.

And there was one more thing.

> **System**
>
> **Lv. 42 Kim Gwondong**

There wasn’t a Hunter living in the building next to ours.

*So they aren’t working together.*

The appearance of the two actors was enough to turn my suspicion into certainty.

My steps grew lighter as I headed toward the real-estate office in front of the house.

* * *

Late in the morning, a middle-aged man in shabby clothes dragged his slippers along while humming. He was such an ordinary sight that he could be found anywhere. The moment he turned the corner, he pulled out a cigarette and placed it between his lips.

“Let’s see. Where’s my lighter…”

His hand moved slowly as it rummaged through his pocket, but his eyes were moving busily.

After confirming that no one was nearby, he pulled out something else instead of a lighter: a miniature radio.

“Was the acting okay? Maybe I should’ve become an actor instead of a Hunter. I’m better at acting than fighting.”

—It’s me, the Team Leader.

Plop.

The cigarette fell from his mouth. His now-free lips moved soundlessly.

*Shit. I’m screwed.*

The C-rank Hunter Kim Gwondong, a member of the Security Team, hurriedly pulled himself together and answered.

“Ah, yes, Team Leader.”

—Kim Gwondong’s pretty good at acting, huh? You could quit the Guild and go to Hollywood.

“I-I’m sorry.”

—Don’t get scared. It’s a compliment. Anyway, how’s the target? He didn’t smell anything, right?

“I don’t think so.”

The reason the Team Leader asked again, despite having already heard the conversation through Kim Junsu, was simple.

A cat’s eyes could not capture everything about the target clearly.

—Are you sure? One hundred percent?

“Ninety percent.”

—You little shit, is ninety percent certain? At times like this, you’re supposed to say it confidently and go for it.

“Jumping to conclusions is dangerous.”

Kim Gwondong cursed the Team Leader inwardly.

*What good does it do me to say it confidently? If something goes wrong later, you’ll be the first one to chew me out.*

He had to leave himself an escape route like this. Kim Gwondong’s ninety percent would only be complete once the Team Leader added his ten percent.

—That attitude of yours is exactly what I like to see. You know what to do next, right?

The Team Leader’s pleasant voice was a sign that he had finally reached one hundred percent.

Kim Gwondong subtly changed direction to avoid a resident approaching from far away.

“Yes. I’ll naturally circle around the area and keep watch.”

—Right. Report immediately if anything unusual happens.

“Yes.”

—Then keep up the good work.

The conversation between the two men lasted a little over a minute, and no one heard it.

This time, Kim Gwondong took out a real lighter and lit his cigarette. He inhaled deeply.

“Fuck. Looks like lung cancer’s going to kill me faster than a monster.”

* * *

The Security Team Leader got busy. There were three external surveillance personnel in total. He had to give instructions to the other two and make sure everything was in place.

“Number One.”

—Number One here.

“You were listening on the all-team channel, right? What about the real-estate office the target is heading to?”

—There are two in the nearby shopping district, and we’ve installed eavesdropping-magic Equipment in both.

“Good. Where’s the target?”

—We haven’t seen him yet… Ah, there he is. He’s approaching from about 300 meters away.

“Leave your position. We already installed the Equipment, so there’s no need to make contact for no reason.”

—Yes. I’ll report immediately if anything unusual happens.

“Okay. Number Two?”

—Waiting at my current position.

A deep voice came through the radio.

The Security Team Leader nodded at the reply from another team member hiding in a nearby shop.

“That bastard might take another route, so keep a close eye on him.”

—Yes.

Four C-rank Hunters specializing in stealth and tracking, along with a Familiar mage.

Their combat power was low, but every one of them was a veteran with extensive experience in this field.

*It’s overkill for one C-rank Hunter.*

At first, he had been somewhat wary. The Guild Master had given them a special warning about the target.

*They said he cleared a B-rank Gate alone, I think.*

But the more information he gathered about the man, the more he watched him, the more he felt that was not the case at all. The fact that the information had come from Im Changsoo finally put an end to his doubts.

*That good-for-nothing bastard made it all up because he didn’t want to get beaten to death.*

An ordinary C-rank Hunter whom one could find anywhere.

That was all Jin Taekyung was in his eyes.

Beep.

—Target entering the real-estate office.

A report came over the radio from the team member keeping watch.

Sangdong Guild’s Security Team went on full alert.

[^1]: A Korean term for a cat that acts like a dog—friendly and affectionate.
## Chapter artifact 97

# Chapter 97

“Oh my, welcome!”

An ajumma who looked to be in her forties greeted me with a nasal sing-song.

Maybe it was because this real-estate office was close to home. Her face looked vaguely familiar, as though I had passed her by on my way home once or twice.

“Young man, what would you like to drink? Coffee? Yulmu tea?[^1] Cola?”

“Coffee, please.”

“Black, creamer, or…”

“Black.”

“Well, look at you. A young bachelor who knows how to drink coffee.”

I let her rapid-fire chatter go in one ear and out the other as I took a seat. There was another place I needed to pay more attention to than the talkative real-estate ajumma.

*This is…*

The familiar energy flowing through the real-estate office.

It was mana.

*Wiretapping magic?*

There was almost no chance it was security magic installed by the owner. Who would put an expensive magic product in a real-estate office instead of their home?

The people watching me had clearly made preparations in advance.

*Well, it was something I expected.*

They were using Familiars, after all. Wiretapping magic was the least of it.

The question was how many of them there were and where they were hiding…

“Here you go. One coffee.”

I accepted the cup with a polite smile.

“Ah, thank you.”

I meant that sincerely.

She was about to tell me where their base was.

* * *

—So, what brings our handsome boss here?

—I’m looking for a house.

The voice transmitted by the eavesdropping magic was perfectly clear. Kim Junsu, who had briefly deactivated his Familiar magic, exchanged a look with another team member and the Security Team Leader.

“Didn’t that bastard go to a real-estate office recently, too?”

“Yes. He went to Goyang. At the time, we hadn’t been assigned to him yet, so the Team 1 Leader got the information from Hong Woojin and passed it along.”

“Junsu’s right. We went to the real-estate office afterward and dug around a little. Apparently, he even put down a deposit.”

“How much money does he have in his account right now?”

The Security Team already knew Jin Taekyung’s account balance inside and out.

At the Security Team Leader’s question, a team member quickly pulled out a tablet and brought up the report.

“About 3.7 billion won. Three billion of that will go toward buying the new house.”

“Are you sure he’s going to buy it?”

“We even heard that he’s planning to set a date with the owner and sign the contract soon, so he definitely intends to purchase it. We looked into it, and apparently it’s the neighborhood where the target lived as a child. It seems to have some special meaning to him.”

“I see…”

The Security Team Leader frowned.

The man was about to pour most of his fortune into a new house. So why was he looking into another house in this neighborhood now?

*Even though his Guild is in Bucheon.*

Whatever he was thinking, the whole thing left an unpleasant feeling in the Security Team Leader’s gut.

“Hey, turn up the volume a little.”

“Yes, sir.”

The conversation continued to flow into the three men’s ears.

—What kind of conditions are you looking for?

—Either monthly rent or a jeonse lease.

—I do have a few, but… as you know, this neighborhood straddles a safety zone, so it’s a little expensive.

—That’s fine. I’m a Hunter.

—Oh my, you’re a Hunter? I knew you looked fit. What rank are you? Ah, is it rude of me to ask something like that?

—Somewhere around there. It’s not very high. C-rank.

—Oh my, oh my. You must make good money. Can I feel that arm? Oh-ho-ho!

—Ha-ha. Show me some good listings and I’ll think about it. No, show me everything. Jeonse, purchases, whatever. If I find something I like, I’ll just buy it.

The three men listening were dumbfounded.

“That bastard’s really enjoying himself.”

“Can you blame him? He lived as an F-rank Hunter, then after his reawakening, big chunks of money started rolling in. Of course his ego would swell.”

“Hmm, true. That’s the age for it.”

They all knew from experience. The feeling of stepping into a new world.

Luxury goods they had once been unable to look at because they were too expensive suddenly seemed laughable, and other people started looking at them differently.

“That bastard’s exactly like that right now.”

“‘If I find something I like, I’ll buy it,’ my ass. Once you pay the balance on the house you already contracted for, your account will barely cover a jeonse deposit, you idiot.”

“Still, I’m jealous. What does he eat to have such thick hair?”

Watching Jin Taekyung’s childish, cocky behavior was pathetic, but a quiet laugh escaped them anyway.

Before they knew it, the three men had relaxed. Their ears were still open, but they felt as if they were listening to a radio broadcast.

—How about this place? Around five hundred million won for a jeonse lease? Considering that it’s in a safety zone, it’s much cheaper than market price.

—Not bad. Are there any others?

—Of course there are. There’s another listing in the building two over from the one I just showed you… Oh, this one already went off the market. It was monthly rent, but the terms were exceptionally good.

—Oh, really?

—Yeah. If you’d come a few days earlier, young man, you could’ve snagged it. The place wasn’t well maintained, but the rent was cheap. Of course, if you have money, remodeling can solve that problem.

—That’s a shame.

—Tell me about it. Some scary-looking man came by and spoke to me in this commanding tone. Did he think I’d been entrusted with his house or something? I’d much rather hand it over to a young, handsome bachelor, you know. Right?

—Ugh, I guess he was a total old-fashioned jerk.

—I thought he might be a gangster, so I couldn’t so much as squeak. The smell of an old bachelor was practically pouring off him. I thought I was going to die. Ho-ho-ho.

Grrrind.

The sound of teeth grinding came from beside them. Kim Junsu and the other team member suppressed the laughter threatening to burst out.

*It’s the Team Leader.*

*It really is the Team Leader.*

A gangster-like impression and the smell of an old bachelor. Just hearing that much was enough to identify the Security Team Leader.

His expression was so frightening that there was even a rumor that when he first joined Sangdong Guild, the interviewer had been too scared to look any further and hired him on the spot.

“Has that ajumma lost her mind…?”

The Team Leader ground his teeth and whipped his head around. The two men, whose faces had flushed red from holding back their laughter, hurriedly lowered their heads.

“You two look like you’re having a hard time holding it in.”

“Oh, no, sir.”

“There’s no such thing.”

They tried desperately to deny it, but the Team Leader was already thoroughly offended. He stood up.

For a single man in his mid-forties, the words *old bachelor* touched on a subject that absolutely should not be touched.

“I’m going to the sauna to wash off this old-bachelor smell, so have the transcript ready for me to read as soon as I get back.”

“What?”

Kim Junsu and the other team member were dumbfounded.

A C-rank Hunter showing off at a real-estate office and a scatterbrained ajumma. Why would anyone write up a transcript of their completely unremarkable conversation?

“Team Leader, it’s all being saved automatically…”

“Prepare a full-page A4 statement of your individual opinions, too. He’s an important target, so we should gather the team’s input.”

“…”

“…”

Since when had he ever asked for their opinions? And how could it make sense for the Team Leader to go to a sauna while they were dealing with such an important target?

Their expressions twisted at the narrow-minded superior’s petty retaliation.

“Didn’t you hear me? Repeat the order back. Execute!”

“…Yes.”

“…Execute.”

“You bastards have gotten way too lax. You treat your Team Leader like dog shit.”

The Security Team Leader glared at his subordinates, snorted angrily, and left the room.

Bang!

The apartment’s front door slammed shut. The two men left behind immediately let out everything they had been holding in.

“Man, fuck this.”

“Isn’t this taking things way too far?”

“Why is he taking out the fact that he has an ugly face and can’t get married on us?”

“Is his face the only problem? That ajumma said he spoke in a commanding tone. His personality’s rotten, too.”

“This is so damn unpleasant. I can’t keep doing this.”

“Ah, I really can’t afford to get stressed out. It’ll make even more of my hair fall out.”

Kim Junsu muttered in a voice thick with tears and felt the top of his head.

He couldn’t be sure, but it seemed like at least ten hairs had fallen out in the last few moments.

“Then what do we do about the transcript and the statements?”

“What do you think? If you don’t want to watch the Team Leader throw a fit, you have to write them. Want to go to the hospital and get a medical statement?”

“…”

“Just write something rough. I’ll cover for you and say you couldn’t write because you were using Familiar magic.”

After letting out a deep sigh, the two men began cursing the Team Leader in earnest.

Even then, the conversation continued through the transmitter.

—It’s nice. Since it faces south, it gets plenty of sunlight. What about the building next to it? Don’t tell me that one’s gone, too?

—Huh? No, it’s still available. Business has been slow lately, so the places that went recently were… Wait, young man.

—Yes?

—That arm of yours is really solid. Goodness, look at those muscles and veins.

—…

* * *

“Young man, come again. Come twice!”

I left the real-estate office with the ajumma’s regretful farewell behind me.

Goose bumps had risen all over the arm her hand had just brushed.

*Whether it’s an ajumma or an ajusshi, people who grow old without growing up are all alike when it comes to hitting on younger people.*

I had escaped as if fleeing from her sticky gaze, but I had already accomplished my purpose in visiting the real-estate office, so I had no reason to linger.

*Confirm the listings that were recently sold or leased.*

Today was exactly five days after the raid with Im Changsoo.

That meant the surveillance team had been assigned to me no more than five days ago.

*I tried to act and ask about it indirectly without making it obvious, but…*

Knowing that eavesdropping magic was in place, I had deliberately behaved that way. I wanted to come across as an unremarkable C-rank Hunter packed full of arrogance and extravagance.

*Whether they fell for it or not was another matter.*

My conversation with the real-estate ajumma had given me an important clue. I repeated the addresses I had memorized in advance in my head.

*Building 5, Unit 901. Building 4, Unit 302. Building 3, Unit 202.*

These were the listings that had changed hands in the past five days.

I had used our house as the center point and set the range at a maximum of five hundred meters—the distance Familiar magic could reach.

The watchers were definitely somewhere within that range.

*The problem is how to find them.*

My goal wasn’t to drive them away. I wanted to catch them, beat the hell out of them, and find out who was behind them.

If I jumped at the wrong lead, they might realize what was happening and run.

*They could be hiding in a car, too, so I should check the parking lot.*

If I started searching the nearby houses, they would notice something was wrong. But I could search the parking lot naturally.

All I had to do was scan the area with Qi Sense while pretending to take a walk.

Game over.

> **System**
>
> **Lv. 42 Kim Gwondong**

“Oh, we meet again.”

Just like this man.

I returned Kim Gwondong’s familiar greeting.

“Indeed. We meet again.”

“You said you were going to the real-estate office. Are you done already?”

“I just asked a few questions. But when I actually went there and looked into it, the house prices weren’t exactly cheap. I ran right back out.”

“That’s how this neighborhood is. Still, you’re doing well for yourself, young man. At your age, I was just sitting at home eating my parents’ food.”

“Doing well? Ha-ha.”

If he knew what real ability looked like, he’d faint.

Kim Gwondong laughed along, unaware of my thoughts, then spoke.

“Well, I should be going. I need to walk as far as the park over there.”

“You must like taking walks.”

“Huh? It’s not that I do it because I like it. I do it because I need to. You’ll have a hard time too once you reach my age.”

He deliberately waved his thin arms and legs.

From the outside, he looked exactly like an ordinary middle-aged man who was skinny everywhere except for his protruding belly.

*He certainly looks like a civilian.*

Anyone else would have been fooled.

But there was no way a civilian could be Level 42.

*Probably a C-rank Hunter. Judging by his build, he’s probably specialized in stealth and pursuit.*

Once you knew someone was a Hunter, there was a lot you could infer.

I said goodbye to Kim Gwondong.

“Then I’ll see you next time.”

“That depends. We might run into each other, or we might not. Ha-ha.”

Well, I definitely wanted to see him.

Of course, when that happened, I wouldn’t be parting from him with a smile and a laugh like I was now. I wanted to knock him flat right then and there, but it wasn’t time yet.

I gave him a slight bow and turned to leave.

“Oh, right. That cat seemed awfully smart. I saw it on my way over, and it was still there.”

He had even given me a friendly reminder not to forget to pick up my Familiar.

And just as he said, the cat was waiting for me in the same spot as before.

“Meow.”

Right. Hyung’s here, you punk.

[^1]: Yulmu tea is a sweet Korean grain beverage made from roasted Job’s tears.
## Chapter artifact 98

# Chapter 98

Hong Woojin regretted it.

*I didn't think this through.*

The intrusion itself had gone perfectly. He had approached the target’s cat-loving younger sister and won her heart with a pair of pitiful yet sparkling eyes.

The problem was…

“What does our Yeoreum eat to be this cute? Hmm? Hmm-hmm?”

*Meow.*

“Yeoreum, why do you keep trying to get out the door? Stay here and play with your big sis.”

*Meow.*

“Eek, you’re so cute!”

*Hiss! Hissssss!*

“Oh no, is Yeoreum mad? I’m sorry. Did Sis touch you too much? Okay, I’ll stay still, so play on the bed, all right?”

This damn younger sister had absolutely no intention of letting him outside. Thanks to her, he had spent more than a day and a half trapped in Jin Hayeon’s room.

*I should’ve gone with a dog.*

If he had been a dog, getting inside wouldn’t have been this easy. But once he was in, he wouldn’t have been practically held captive, either. At the very least, they would have taken him out for walks.

*This gets me nowhere.*

Swept up by a sense of crisis, Hong Woojin attempted to escape.

*Let’s see who wins—you or me!*

He had begun with that fierce resolve, but then…

Scritch, scritch-scritch-scritch.

“…”

*Meow. Myaaaaaow.*

“…”

His first attempt was a failure. He scratched desperately at the door and even tried crying as loudly as he could, but Jin Hayeon didn’t react even once.

Without even putting on earphones, she simply continued solving problems with a fierce look in her eyes and swift movements of her hands.

*So this is what it means to be in the top 0.01 percent nationwide.*

He had seen it in the initial investigation report. Ever since middle school, she had routinely ranked first or second in her entire school and had earned countless awards in various academic competitions. It was hard to forget a record like that.

Only today did Hong Woojin understand why.

Sitting in front of her desk, she possessed truly terrifying powers of concentration.

*Someone like this would make the perfect mage… No, that’s not the point.*

He continued trying to disrupt her studies somehow. He pawed at her feet without pause and kept acting cute.

But Jin Hayeon’s response was simple.

“Big sis is studying right now. Don’t bother me.”

She pulled her feet up onto the chair and sat cross-legged, putting them completely out of reach of his tiny body.

That was the limit of being a kitten.

*This operation has failed.*

Since his plan to disrupt her studies had gone up in smoke, he had no choice but to bring out his final card. It would deal a serious blow to his human dignity, but this was no time to be picky.

*Let’s see if you ignore this, too.*

Sssssssss.

The pristine white duvet turned yellow.

When nature called, it was best to take care of both kinds of business at once. Having finished both simultaneously, Hong Woojin made a solemn decision.

*Fine. Since things have come to this, I might as well take care of it properly. Like a professional.*

He rolled over and over.

It had been five years since he started using Familiar magic. This was the first time he had ever fallen this far.

He kept hypnotizing himself.

*I’m a professional. I’m a professional. I’m a professional…*

A little while later, Jin Hayeon noticed a strange smell and turned around.

By then, everything was over.

*Meow.*

A duvet stained with urine and feces, and a kitten covered in filth.

“Eek, Yeoreum!”

Jin Hayeon was startled and moved quickly. She pulled off the dirty duvet, then carefully grabbed the kitten by the scruff of its neck and lifted it up.

“What are you doing going to the bathroom here when your litter box is right there? We need to wash our Yeoreum.”

*Yes, go to the door! The door!*

This was the moment he had been waiting for.

Even though he was covered in filth and dangling from the hand of a girl who wasn’t even twenty, Hong Woojin was filled with joy.

Click.

The door was opening!

The living room he hadn’t seen since yesterday came into view!

*Meow! Myaaaow!*

“That’s strange. Why does it look so happy?”

Jin Hayeon tilted her head.

That was when the front door opened with the familiar electronic tones of someone entering the passcode.

“I’m ho—… What is that?”

“Where have you been—… What’s that?”

The siblings stared at each other in bewilderment.

More precisely, they stared at the creatures in each other’s hands.

*Meow.*

*Myaow.*

The two cats exchanged equally bewildered looks.

*That’s Hong Woojin?*

*That guy is the Sangdong Guild’s amateur?*

And then came the next thought.

*Why is he covered in shit from head to toe?*

*Ah, fuck.*

It was the moment the last shred of Hong Woojin’s human dignity collapsed.

* * *

“You smeared poop all over the duvet?”

“Yeah. I guess he had an accident while I was studying for a bit.”

*An accident, my ass.*

Since Hayeon had kept him in her room, petting and cuddling him nonstop, he had wracked his brain for a way to get out.

*Myaow…*

A cat.

No, there were two of them now, so I supposed I should call them by their names.

Whatever the case, Hayeon asked worriedly at the sound of Yeoreum’s feeble cry.

“He’s been looking weak for a while.”

“Hmm. That can happen.”

I couldn’t say for sure, but his self-loathing had to be something else.

He had run into both a fellow professional and his surveillance target while covered in shit.

“Don’t worry too much. Cats normally hate getting water on their bodies.”

“Is that why? No, he didn’t even resist when I washed him earlier. He was completely docile.”

“Oh, really?”

“I don’t know if it’s just my imagination, but he seems kind of out of it. Maybe he knows he made a mess and feels sorry?”

*Our Yeoreum had a serious case of post-nut clarity.*

I swallowed my laughter and said, “Who knows? Anyway, what are you going to do about the duvet? You’ll have to change the sheets, too.”

“It’s fine. It was an animal, not a person. What’s the big deal?”

They say a frog can die from a stone thrown without a second thought.

That was exactly what had happened here. Hayeon’s offhand remark turned into a blade and lodged itself in someone’s chest.

The kitten trembled violently in silence, unable to even cry out.

Meanwhile, the other one was having a wonderful time.

*Purr. Prrrr.*

Hayeon gazed at the black cat with a face full of adoration as it repeatedly rubbed its face against my leg, making happy noises.

“Where did you bring him from?”

“The entrance to the apartment complex.”

“Is he a stray?”

“I guess so. He was alone.”

“What? Then he might have a mother. You’re supposed to watch a kitten for about a day before bringing it home.”

“Some man told me he’d been crying alone since yesterday.”

“Oh, then he doesn’t have a mother.”

The black cat flinched.

Its purring and attempts to act cute stopped dead. Without realizing it, Hayeon had scored two kills, and she smiled brightly.

“There, there. You don’t have a mother, either. It’s okay. From today onward, Sis will be your mommy.”

“…”

For my little sister, she certainly had a talent for screwing people over with a smile.

The black cat seemed torn between professional duty and the cheap shot at his mom, but soon accepted reality.

*Meow.*

The sight of it acting cute for its mother’s enemy was downright pitiful.

*That’s the hardship of being a working stiff.*

Watching them, I suddenly thought of Mom.

“Where’s Mom?”

“I don’t know. She went out because she had an important appointment.”

“An appointment?”

“Yeah. She’s been going out a lot lately.”

*What’s going on?*

Mom had been leaving the house frequently these days. Now that she had some free time after quitting her job, was she finally looking for a life of her own?

*Come to think of it, she had been acting strange.*

Sometimes she would sit there with an expression that looked as though she had something to say. Other times, she would jump whenever I suddenly spoke to her.

Something had definitely changed around Mom.

*She’ll tell me when the time is right.*

The person I loved and trusted most in this world was my mother. Just as always, all I could do was trust her and wait.

Of course, listening to her and talking things over at the right time was also a child’s duty.

“What are you thinking about so hard?”

“It’s nothing. By the way, aren’t you going out?”

“What, you sound like you want me to leave.”

“Not exactly.”

“Hmm. Suspicious. You’re not planning to bring a girlfriend over, are you?”

“…”

*I wish I had a girlfriend to bring over.*

My expression must have revealed my thoughts, because Hayeon hesitated.

“Ah, I’m sorry.”

“Don’t apologize. It makes me twice as pathetic.”

“I’m really sorry.”

“You’re doing this on purpose, aren’t you?”

“Come to think of it, I have some books to return to the library.”

She sprinted into her room, threw on her backpack, and came back out at the speed of light.

The front door slammed shut, and the house fell silent.

*She really went and gouged out a single man’s heart.*

A corner of my chest felt hollow, but the stage I had been waiting for had finally been set.

This was a problem I needed to deal with while my family was out of the house, if possible.

*Myaow.*

*Meow.*

Two cats, one black and one white, began creeping toward me and circling around.

Bright eyes. Perked-up ears.

I left the Familiars, who were dying to learn more about me, behind and stepped onto the balcony.

The first thing I saw was the parking lot, where hundreds of cars were lined up.

*The parking lot is clear.*

Before returning home, I had carried the Familiar in my arms and taken a lap around the apartment complex. To everyone else, I probably looked like an idler out for a walk on a pleasant day.

My real purpose had been to check the vehicles.

The result was nothing suspicious.

*Then it has to be one of those houses.*

That confirmed the watchers had made one of the recently traded apartments their base. I recalled the information I had obtained from the real-estate office once more.

*Building 5, Unit 901. Building 4, Unit 302. Building 3, Unit 202.*

Coincidentally, all three were positioned around our apartment, forming a sort of ring. They were ideal for surveillance, since their windows offered a view of the entrances to the buildings.

It wouldn’t be strange for the watchers to be in any one of them.

*The question is which one they’re hiding in…*

They were cautious enough to use a Familiar instead of magical Equipment to avoid being discovered.

If I approached recklessly, I would lose them. To make a definite capture, I had no choice but to throw out equally substantial bait.

*I think it’s time to begin.*

Swish. Rustle.

First, I drew all the curtains in the house. Even though it was the middle of the day, the living room had grown dim. I reached into my pocket.

*Inventory open. Mana-detection Equipment.*

At the same time, my hand closed around a lump of metal about half the size of my palm.

As its name suggested, it was Equipment that could detect mana. I had paid twenty million won for it at the Store.

*Next step: search.*

I carefully swept through the house with the detection Equipment. After confirming that no mana was being detected inside, I took out my smartphone and called someone.

Beep. Beep. Click.

The other person answered as the call connected.

—Hello?

I replied.

“It’s me, Jin Taekyung.”

The two Familiars watched me without even seeming to breathe.

* * *

The moment Kim Junsu opened his eyes, he shouted.

“He’s here! He’s here!”

The Security Team members, who had been sitting close together and writing their assessments, jumped in surprise.

“What?”

“Who’s here? Our Team Leader?”

“Or could it be…”

Kim Junsu nodded at the team member who had let his voice trail off.

“The target. This guy reeks to high heaven.”

“Seriously?”

“Yes. I got a bad feeling when he drew all the curtains as soon as the house was empty, and then he even used detection Equipment to inspect the inside.”

That wasn’t something an ordinary C-rank Hunter, especially one on vacation, would do.

Everyone in the room swallowed hard.

“Th-then?”

“He pulled out his phone and made a call.”

“A call? To whom?”

“I don’t know.”

Kim Junsu furrowed his brow.

“The call was so short that it didn’t even last three minutes. But more than that, I could tell he was being extremely careful about how he addressed the other person.”

“That’s enough. We’ll report it up the chain and pull that bastard’s call records.”

“Right. And there was nothing else?”

“How could there be nothing else? Do you know what he said?”

He cleared his throat once. Then a low voice came from his mouth.

“‘The plan is proceeding without a hitch. Yes, yes. The Sangdong Guild hasn’t noticed anything yet. I have the item with me.’”

The team members listening slapped their knees.

“This is it!”

“We finally got something!”

“Wow, I just got chills. What is he, some kind of secret agent?”

At that moment, Kim Gwondong, who had been listening quietly, suddenly spoke.

“Junsu, didn’t that bastard say he had an item?”

“Good observation.”

Kim Junsu smiled meaningfully.

“That guy has a USB.”
## Chapter artifact 99

# Chapter 99

The Security Team Leader received a phone call just after finishing up at the sauna.

“Team Leader. It’s me, Kim Gwondong.”

“Oh, did you finish writing the transcript and assessment?”

“No, sir. That’s not it…”

“You little shit. I went easy on you because you’re the most senior one here, and now you’re getting careless? Write up your assessment and send it to me within ten minutes.”

“Come on, that’s not it. I’m calling to report something unusual.”

A moment later, the Security Team Leader dropped the roasted egg he was holding.

“He had a USB?”

“Yes. We don’t know who he was talking to, but he said he was keeping the item safe, and he even slipped it out to check it himself. Junsu saw it directly, so it’s certain.”

“Th-then?”

“The target is keeping it on him, apparently… Junsu has no way to do anything about it for now, so I’m reporting it.”

“Junsu? Put Junsu on right now.”

“He’s watching the target with his Familiar, so that might be difficult.”

The Security Team Leader bit down hard on his lip. His head was a complete mess after hearing the report.

*Who was the person on the phone? What was the target’s true identity? And what on earth is inside that USB?*

The Security Team Leader’s instincts began to stir.

“Gwondong. This was a special order from the Guild Master. You know that, right? I’ve told you so many times.”

“Everyone knows that.”

“If we manage to get even one thing out of this, we all hit the jackpot. I’ll move up, and you’ve been around long enough that you ought to become a Team Leader, too.”

“…It’s not as simple as wishing for it. You know perfectly well they won’t make someone a Team Leader unless they’re at least B-rank.”

“I think this is more than enough to make a real score. I don’t know where that Jin Taekyung bastard came from, but the picture is obvious. You can tell just by listening to him talk about our Sangdong Guild. Right?”

“I did think it looked that way.”

The plan was proceeding without a hitch. Sangdong Guild still hadn’t noticed anything. And he was keeping the item safe.

The conversation between Jin Taekyung and the unknown person on the other end of the line was suspicious enough to sound meaningful even to a third party.

For Sangdong Guild’s Security Team, there was no question.

“That USB is the key. To put it bluntly, whether it’s the Peace Guild Jin Taekyung belongs to or some rival Guild, if they’re making a move to bring down our Guild…”

“Then that’s seriously high-value intel.”

The bonus was a given, and promotion was an option. If he caught the Guild Master’s eye, he might even be able to aim for a position among the Guild executives.

At that very moment, the Security Team Leader imagined himself as the Guild Master’s right-hand man, while Kim Gwondong became lost in a dream of becoming Sangdong Guild’s first C-rank Team Leader.

“Keep watching him. I’ll report this up the chain and start by checking Jin Taekyung’s call records.”

“Yes, sir!”

“I’ll change clothes and head over immediately. No matter how late it is, we’ll know who the target spoke with before dinner. Let’s come up with a plan before then.”

Just as the Security Team Leader was about to hurry to the changing room, Kim Gwondong spoke again.

“Ah, Team Leader. There’s one thing I’m worried about…”

“What is it?”

Anxiety could be heard in Kim Gwondong’s voice. And his ominous premonition proved accurate.

“You know Hong Woojin, right?”

“Ah, damn it.”

It was a mistake. He had been so excited that he had briefly forgotten about Hong Woojin’s existence. The Security Team Leader grew impatient.

*It’ll be a problem if that bastard makes the first move.*

The Guild Master he knew, Im Chunsoo, was a man who made rewards and punishments absolutely clear.

If a newcomer proved their ability, he would pave the road to advancement for them. But if he decided someone was no good, he would cut them loose without hesitation—even if they had been a Guild member for ten years.

*I’ve seen it more than once or twice.*

This wouldn’t simply end with Hong Woojin taking the credit. The Security Team Leader’s own livelihood was on the line.

Money? That wasn’t the issue. He had devoted half his life to this Guild and wanted to climb as high as he possibly could.

“Gwondong.”

“Yes.”

“That bastard is alone at home right now, isn’t he?”

“Team Leader, surely not? You can’t!”

“I’m not finished talking.”

Unlike Kim Gwondong, whose voice had grown loud, the Security Team Leader remained calm.

“If we subdue the target, take the item, and leave, this ends cleanly. He’s only C-rank, after all. There’s nothing to be afraid of.”

“He’s a C-rank who reeks to high heaven. If we make the wrong move, we could be the ones getting taken down.”

“Taken down? By a rookie who only just awakened as a C-rank? Me, a B-rank veteran? That’s insulting.”

“…”

“You don’t actually believe what Im Changsoo said, do you? If that were true, it would mean Jin Taekyung was really an A-rank Hunter… If that’s the case, you might as well say the Guild Master is a spy. Huh?”

“Come on, why are you taking it that far?”

“Enough. Are you doing it or not?”

“Fuck, this is driving me crazy.”

Kim Gwondong let out several deep sighs before finally making up his mind.

“If we get caught, we become criminals. You know that, right?”

“I know. I also know that if we don’t get caught, we’re innocent.”

“Team Leader, you really have some nerve.”

“That’s why I’m the Team Leader. What about the others?”

“They’re all gathered right now. We finished checking the CCTV on the first day we were deployed, and we have some simple disguise Equipment, too.”

“Good.”

“When do we start?”

The Security Team Leader licked his dry lips.

“The moment I arrive.”

As the old saying went, you had to pull the ox’s horn while it was hot. To him, a C-rank Hunter was a soft horn he could yank out one-handed.

* * *

It didn’t take long for me to realize that the bait had worked.

*Meow.*

*Myaow.*

The two Familiars showered me with affection, trying to win my favor. But this time, something was different.

They had struggled up onto the sofa with their short legs, then settled down—not just anywhere, but on my thighs.

*They took the bait.*

The USB in my pocket was the bait. By now, the watchers must have been going crazy with curiosity.

What plan I had mentioned during the call, who I had been speaking to, and what on earth was inside the USB.

*I hope they’re more daring than I expect.*

Neither they nor I had anything to gain by dragging this out. It was a weekday afternoon, the apartment complex was quiet, and the TV was showing a boring documentary about returning to farming.

“Ah, should I go to the hill behind the apartment for the first time in a while…?”

I muttered to myself and was about to leave through the front door when the change I had been waiting for occurred.

> **System**
>
> Level 2 Cat
>
> Level 2 Cat

The Familiar magic had been dispelled. The meaning of this phenomenon was obvious.

*They’re finally making their move.*

In the body of a kitten, they couldn’t steal the USB from me. But if I, the target, moved somewhere sparsely populated on my own, that would change things.

*Anyone looking at me would see an ordinary C-rank Hunter. They’d think they could take it from me without worry.*

Of course, it wasn’t hard to predict that a suitable amount of violence and threats would be part of the process.

But the watchers had made one crucial mistake.

What they had misjudged was me. They had always been the perpetrators, and had never imagined that they could become the victims.

*I’m looking forward to this. What kind of bastards are they?*

I intended to show them exactly what happened when someone illegally stalked another person without permission.

* * *

The information Jin Taekyung had obtained from the real-estate office was only half right. Unlike Sangdong Guild’s Security Team, Hong Woojin’s hideout was in a place Taekyung had never expected.

The rooftop of the apartment building where Jin Taekyung lived.

“Whew.”

After severing his Link with the Familiar, Hong Woojin opened his eyes inside the tiny supply closet attached to the rooftop.

By slipping the security guard a little money, he had secured this optimal space of roughly five pyeong[^1] for several days.

“This job got horribly tangled up.”

Jin Taekyung’s suspicious phone call. A USB whose contents were unknown.

He had finally discovered something that could be called information, but Sangdong Guild had discovered the same thing.

Hong Woojin stepped out of the supply closet and looked down over the edge of the roof. Far below, he could see Jin Taekyung just leaving the apartment entrance.

*Should I follow him or not?*

If he thought about the job, following him was the right choice. But something about it felt wrong. Hong Woojin was watching Jin Taekyung grow smaller in the distance with a conflicted look in his eyes when—

“Huh. What do we have here?”

One person, then another. The way they slowly crawled out was no different from snakes stalking their prey.

There were six of them in total.

Their clothes were all different, and their behavior was no different from ordinary people’s. But to Hong Woojin, a fellow professional in the industry, it was obvious.

“They’re from Sangdong Guild.”

Not one or two of them—six had emerged.

What was more, the target’s destination was a deserted hillside. Realizing what was about to happen, Hong Woojin furrowed his brow.

“They really pull every dirty trick in the book.”

Using force crossed Hong Woojin’s line. He should have quit when they deployed the Security Team, despite his repeated warnings when he first accepted the job. But this had gone too far.

*I wanted to uncover Jin Taekyung’s secrets myself.*

He was a man whose identity had made Hong Woojin curious, but this was where it ended. He had a feeling that he shouldn’t get involved any further.

*Sangdong Guild, you goddamn thugs.*

Clicking his tongue, Hong Woojin took out his smartphone and sent a text.

The recipient was the Team 1 Leader. The message was short and simple.

> **Team 1 Leader**
>
> I’m dropping the job.

Before leaving the rooftop, he also remembered to wish the already-vanished Jin Taekyung a peaceful rest.

*Well, that was filthy. Let’s never see each other again.*

In every respect, it had been a cursed job.

* * *

I climbed the mountain path in silence. It had been a long time since I’d left the hiking trail behind.

But I didn’t stop. I kept walking deeper and deeper into the mountain.

At some point, a broad clearing came into view. Weeds had grown thick there, reaching up to my knees. I slowly turned around.

“Looks like you’re still out for a walk?”

Kim Gwondong, the middle-aged man I had run into twice before, said nothing. His face hardened.

“No answer? Who’s the person with you?”

“My friend.”

If Kim Gwondong had an ordinary, forgettable face, the man who answered me was the complete opposite.

He was huge, with a vicious expression fierce enough to make gangsters cry. A rough voice rumbled from between his lips.

“You already know everything, so why did you come all the way here?”

“You kept trailing me from behind, so I wanted to see how far you’d follow. Think of it as training a mutt.”

The man let out a hearty laugh.

“Young punk’s got nerve. How old are you?”

“*Yeokmasal*.”[^2]

“You’ve got a real talent for earning a beating.”

“Thanks for the compliment, Mr. Choi Byungil.”

The man, Choi Byungil, closed his mouth. His eyes shook.

“…How did you know?”

“That’s a trade secret. But are you and Mr. Kim Gwondong really friends? Judging by appearances, you two don’t exactly look like a matching pair.”

This time, it was Kim Gwondong’s turn to panic. But I wasn’t finished.

“Is it difficult to answer because you’re not friends? Then I’ll ask the other four. Mr. Park Hyungjin, Mr. Oh Gyuhyeon, Mr. Lee Mincheol, and Mr. Kim Junsu, I’d appreciate an honest answer.”

Bzzzzzz.

The air rippled, and four people dropped straight down.

Each of them had a Level window floating over their head, and their faces looked as if they had seen a ghost.

“Why is everyone so surprised? I was just being considerate so you could breathe comfortably.”

Choi Byungil gritted his teeth. All traces of his earlier composure had vanished, leaving his face colored by anxiety and bewilderment.

“What the fuck… What kind of bastard are you?”

Since he had started with profanity, my respect for my elders ended there. I let out a quiet laugh as I looked at Choi Byungil.

“You still don’t know? You must have dug up every scrap of information about me. If you went so far as to attach Familiars, that says everything.”

“…”

“I could’ve let it go if I’d been alone at home. But the thought of my family being watched pissed me off. So I threw out some bait, and you snapped it up.”

The six watchers trembled.

“Th-then what about the USB?”

“Oh, that? It’s my collection of porn I’ve spent my whole life putting together.”

It was a treasure of humanity that I had carefully stored in my Inventory.

“No way! I definitely had a feeling!”

“Well, there are plenty of works in there that defy belief. And any man would get a gut feeling about it.”

I looked at them, standing there with faces full of despair.

“You answered honestly, so let me ask you one thing, too.”

One by one, they flinched whenever their eyes met mine.

At last, my gaze stopped on a painfully thin man in his twenties. He was probably the Familiar mage.

> **System**
>
> Level 41 Kim Junsu

“Junsu. You were sent here by Sangdong Guild, weren’t you?”

“Shut your mouth!”

Choi Byungil shouted, but Kim Junsu had already answered.

His face had gone completely pale. That was answer enough.

“Okay, Sangdong Guild. I figured as much.”

Choi Byungil’s face stiffened at my words.

“You shouldn’t have said that name out loud.”

“What, you’re going to kill me?”

“…I’ll capture you first and think about it.”

“That’ll be pretty hard.”

Choi Byungil’s Level was in the mid-sixties. His aura was comparable to Im Changsoo’s, while the others were ordinary C-ranks around Levels 30 or 40.

The odds of a group that wasn’t even a professional raid team managing to capture me were extremely low.

“Come at me prepared to die. That’s the only way you’ll manage to tie even a butterfly knot around my wrist.”

“Get him!”

At Choi Byungil’s shout, the Sangdong Guild watchers began charging at me from all directions.

Whoosh!

A dagger dropping toward my shoulder was the opening move.

I reached toward the trajectory that looked slow to me.

At the same time…

*Inventory open. Equip.*

Crunch!

A blade brimming with internal energy shattered the enemy’s dagger. Broken metal and someone’s blood spilled across the nameless weeds.

“Come on, you stalker bastards!”

Ssshhhhh!

[^1]: *Pyeong* is a traditional Korean unit of floor area; five pyeong is roughly 16.5 square meters.

[^2]: *Yeokmasal* is a traditional Korean notion of a fate that compels someone to wander. Here it also puns on *sal*, the Korean word used when asking someone’s age.

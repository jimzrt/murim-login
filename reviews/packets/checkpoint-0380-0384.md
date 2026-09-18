# Checkpoint Review — 380–384

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

# Chapters 380–384

## Plot

Jin Taekyung and Team Leader Choi crash their aircraft into the monster army attacking Chengdu International Airport. Choi protects the passengers with Barrier magic while Jin joins Shao Shen and the Chinese Hunters. Jin discovers that more than half of the nearly two-thousand-monster army are undead and uses the Skeleton Warlord to override their control, turn them against the living monsters, and resurrect fallen creatures. The undead army collapses after Jin destroys the three incomplete Liches serving the Arch Lich. Their testimony confirms that the Arch Lich began the attack a week earlier, but Jin rejects their attempted allegiance and destroys them. The Skeleton Warlord absorbs their death energy and grows stronger. Jin completes the Unexpected Attack Quest, gains the Undead Hunter Title, EXP, Fame, and a level, reaching Level 121.

Wei Fenghu, China's Minister of National Defense, takes Jin and Choi to a temporary operations headquarters on Mount Qingcheng. He explains that Sichuan's crisis began in Gaoping District of Nanchong City, where magical communications interference and flying-monster attacks have isolated the province. Lei Fei, a concealed Chinese S-rank Hunter and head of the Sichuan Public Security Armed Forces Department, disappeared with his Hunters when the first Monster Wave began. Wei, Lei's maternal uncle and adoptive father, asks Jin to bring him back if he is found; Jin agrees but gives no guarantee of survival.

At the underground headquarters, Jin meets Shao Yang, Chairman of the People's Republic of China, the Communist Party's Central Military Commission, and General Secretary. Shao asks the assembled Hunters to save as many people as possible while retaining full authority and responsibility for the response. Jin also encounters international S-rank Hunters, including the Archmage and the combat-focused War Mage Magic Johnson, before trading insults with a young Chinese Hunter over the Lord Fuck nickname and Jin's supposed A-rank status.

## Continuity

- Jin Taekyung is Level 121, at the Supreme Peak realm, has manifested Force, and is publicly known as the Blazing Flame Divine Dragon and, internationally, Lord Fuck.
- Jin's bound Items remain White Flame, the Myriad-Poison Ring, and the self-repairing Fire Dragon Armor.
- The Skeleton Warlord, mockingly called Bones, remains in Jin's Inventory. It can control nearby undead, resurrect fallen monsters, and has absorbed the three incomplete Liches' death energy, greatly increasing its strength.
- The Chengdu International Airport monster army was defeated. The three incomplete Liches serving the Arch Lich were destroyed, and their testimony established that the Arch Lich initiated the attack one week earlier.
- Jin completed the Unexpected Attack Quest and gained the Undead Hunter Title, EXP, Fame, and one level.
- Wei Fenghu is China's Minister of National Defense under the Central Military Commission, a four-star general, and Lei Fei's maternal uncle and adoptive father.
- Lei Fei is a concealed Chinese S-rank Hunter who led the Public Security Armed Forces Department in Sichuan. He disappeared with his Hunters when the first Monster Wave began; his survival remains unconfirmed.
- Jin agreed to bring Lei Fei back if he encounters him, without promising that Lei will survive.
- The temporary operations headquarters is an underground bunker on Mount Qingcheng.
- Shao Yang retains full authority and responsibility for China's response to the Sichuan crisis. International S-rank Hunters have gathered at the bunker, including the Archmage and War Mage Magic Johnson.
- The Arch Lich's identity and next move remain unknown. The Second Fiend assigned to the Qingcheng attack has not been accounted for.
- Aehyang's unidentified superior, the Lord of Heaven's nature, and the fate of the Western Heaven Demon Lord remain unresolved.

## Translation Decisions

- Use **Undead Hunter**, **Arch Lich**, **Lich**, **Death Knight**, **death energy**, **River of Death**, and **Bones** for the established undead terminology.
- Render **웨이펑후** as **Wei Fenghu**, **샤오 양** as **Shao Yang**, and **레이페이** as **Lei Fei**.
- Use **Public Security Armed Forces Department**, **Minister of National Defense**, **Chairman**, **General Secretary**, **Senior Colonel**, and **Comrade** for the established Chinese and military titles.
- Distinguish **Archmage** from **War Mage**, and use **Magic Johnson** for the latter.
- Preserve **Lord Fuck**, **peninsula bangzi**, and the **gukbap** wordplay, including Jin's deliberately awkward welcome to Shao Yang.
- Keep **Blazing Flame Divine Dragon** distinct from **Huashan Divine Dragon**; retain **Mimi**, **Mimi-chan**, **Cheongpung**, **Fire Dragon Armor**, **Myriad-Poison Ring**, and **Moving Formation** as established terms.

## Durable state

{
  "active_continuity": [
    "Jin Taekyung is Level 121, has the Undead Hunter Title, and keeps the strengthened Skeleton Warlord in his Inventory under the mocking name Bones.",
    "The Arch Lich's three incomplete Liches were destroyed at Chengdu International Airport, and their testimony identified the Arch Lich as responsible for the undead army's actions.",
    "Wei Fenghu is China's Minister of National Defense under the Central Military Commission, a four-star general, and the current Chairman's right-hand man.",
    "Sichuan Province is in a wartime emergency involving magical communications interference, flying-monster attacks, and a Monster Wave that began in Gaoping District of Nanchong City.",
    "China has deliberately concealed at least one of its S-rank Hunters, Lei Fei, who led the Public Security Armed Forces Department stationed in Sichuan Province.",
    "Lei Fei disappeared with his department's Hunters when the first Monster Wave began, and neither his death nor his survival has been confirmed.",
    "Wei Fenghu is Lei Fei's maternal uncle, raised him as his own son, believes he is alive, and asked Jin Taekyung to bring him back if found.",
    "Jin Taekyung agreed to Wei Fenghu's request but did not guarantee that Lei Fei would be found alive.",
    "The temporary operations headquarters is at Mount Qingcheng.",
    "Shao Yang is the Chairman of the People's Republic of China, Chairman of the Chinese Communist Party's Central Military Commission, and General Secretary.",
    "Shao Yang has retained full authority and responsibility for directing China's response to the crisis while asking the Hunters to prioritize human lives.",
    "International S-rank Hunters are gathered at the underground headquarters, including Magic Johnson, one of the world's three Archmages and its most combat-oriented War Mage."
  ],
  "continuity_sources": [
    384
  ],
  "open_questions": [
    "Who is the Arch Lich, and what will happen after Jin Taekyung destroys its three servants?",
    "What happened to Lei Fei and the Hunters who disappeared with him?",
    "What happened to the Second Fiend assigned to the Qingcheng attack?",
    "Who is the unidentified person directing Aehyang, and what are they planning?",
    "What is the true nature and purpose of the Lord of Heaven, and what became of the Western Heaven Demon Lord?"
  ],
  "safe_through": 384,
  "temporary_decisions": [
    "Render 열화신룡 as Blazing Flame Divine Dragon, distinct from Huashan Divine Dragon; use Mimi and Mimi-chan for 미미 and 미미쨩, and Third Fiend and Three Fiends for 삼괴.",
    "Render 진인 as Perfected One, 도우 as Fellow Daoist, 신니 as Venerable Nun, 환영진 as illusion formation, and 이동진 as Moving Formation; use Archmage and War Mage for 대마법사 and 워 메이지.",
    "Render 독룡각 as Poison Dragon Pavilion, 가주 대행 as Acting Family Head, 화룡갑 as Fire Dragon Armor, and 공안무력부 as Public Security Armed Forces Department.",
    "Render 사기 as death energy, 의념 as conveyed thoughts, 데스나이트 as Death Knight, 골골 as Bones, and 아크 리치 as Arch Lich.",
    "Render 대교 as Senior Colonel, 동지 as Comrade, 견마지로 as utmost loyalty, 옥체 as august self, and preserve the gukbap wordplay; retain Lord Fuck and peninsula bangzi for the chapter's insults."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 380

# Chapter 380

Shao Shen realized it for the first time.

Roooooar!

If you witnessed an airplane diving toward the ground with both wings engulfed in flames, you would be seized by a terror that transcended species.

—Graaaar!

The supposedly fearsome ogres screamed, and the Trolls shrieked.

—Gweeeaaah!

Even the notoriously sluggish Ghouls ran so fast that sweat broke out on the soles of their feet.

—Squeeeeee!

“Uh, uh, uhhh…”

The monsters that could scream were the lucky ones.

Shao Shen and most of the others could do nothing but stare at the airplane hurtling toward the ground, frozen like stone statues.

*I have to run…*

His feet and hands would not move.

More importantly, Shao Shen and the Hunters of the Public Security Armed Forces Department were surrounded in the middle of the battlefield. They were not even given the chance to escape.

*Is this really the end?*

The same thought crossed everyone’s mind at that moment.

Rumble, rumble, rumble!

With a deafening roar, the airplane’s enormous fuselage swept across the battlefield.

And that earth-shaking collision began at the rear of the monster army, which had been scattering like a swarm of ants.

Crunch! Crack!

The massive steel hulk, weighing dozens of tons, crushed and burst apart everything in its path.

Green monster blood sprayed like fountains, while limbs of every size flew in all directions.

*W-What is this…?*

No matter how powerful the monsters’ physical defenses were, there were limits. Nothing could stop the airplane after it had transformed into a monster blender.

—Graaaar…!

—Kiiiiek!

Krrrunch!

The monsters’ screams were buried beneath the grisly sounds of flesh being torn apart. It was a scene of carnage beyond anything they had ever seen or heard.

As Shao Shen and the Hunters stared blankly at the unimaginable sight, someone’s frenzied shout pierced their ears.

“Monsters! Ram them! Kill them!”

“……!”

The unmistakable language of their homeland reached them even in the midst of all this chaos. The Hunters of the Public Security Armed Forces Department had one word flash through their minds: *reinforcements.*

Shao Shen was stunned.

*An incredible powerhouse!*

The powerful mana carried in that voice. The person was unquestionably an S-rank Hunter.

“Go for it! Airplane!”

“……”

And definitely a slightly insane S-rank Hunter.

*To think he’d resort to a tactic those island bastards used back in World War II. Did he not consider that his own allies might die?*

*He seems to have been sent by the Central Military Commission… But did our country have an S-rank Hunter like that?*

The question suddenly occurred to Shao Shen. But it was about to become irrelevant to him.

The gigantic steel hulk that had ground its way across half the battlefield was now charging straight toward him and the Hunters.

—K-Kiiit!

“Run!”

There was no distinction between friend and foe in the struggle to survive.

Shao Shen forgot the humans right in front of him and drove his dagger into a monster barreling toward him.

Schunk!

—Grrrk.

The monster’s lifeless body collapsed toward Shao Shen.

Unable to move even one step because monsters were surging in from every direction, Shao Shen felt the crushing weight descending upon him and shouted.

“The battle isn’t over! Fight until the very end!”

He was right. The battle was not over yet. A Hunter was someone who had to kill monsters until the final moment, until their own breath ran out.

The Hunters who heard Shao Shen’s shout gritted their teeth and swung their weapons.

*This will do.*

With lightning-fast skill, Shao Shen drove his dagger into the back of a fleeing ogre’s head, then drew a deep breath.

The airplane’s massive body had already reached a point less than twenty meters away.

Its speed had decreased considerably from before, but with everyone trapped in place, avoiding it seemed impossible.

*I have no regrets.*

If he died fighting for the people as a proud Hunter of Zhonghua, that was enough.

Shao Shen closed his eyes as screams rained down from every direction.

“Heave-ho.”

Krrrunch! Splat!

Drenched in a sticky liquid that he assumed was blood, Shao Shen thought:

*…“Whew”?*

Wasn’t it usually more of an “Aaaah”?

The strange sound was an odd choice for a dying cry, so Shao Shen slowly raised his eyelids.

And at last, he saw it.

A few steps away, the airplane had come to a complete stop. Two men were standing beside it, chatting casually.

“All right, we’ve arrived. It might explode, so get everyone off quickly.”

“……Mr. Jin Taekyung. They’re all unconscious.”

“Really? How weak.”

“……They would have died if not for the Barrier magic.”

“Then carry them out, Team Leader Choi. Oh, right. Is that bastard who called us chinks earlier alive, too?”

“Yes. He’s… alive, at least.”

“Then keep a close eye on that bastard. I’m going to give him hell for it when we head back.”

“……I’ll do my best.”

Shao Shen could not make sense of the situation at all.

Who, when, where, what, how, and why. It was such a bizarre sight that even the six fundamental questions could not organize it.

*How did the airplane suddenly stop, and who are those people? Were they not Hunters sent by the Central Military Commission?*

The two men were even speaking in a different language.

Shao Shen could not understand the words of the clean-cut man who looked like a young master, but he knew what country the language belonged to.

Korea, their longtime neighbor.

*Wait. If he’s Korean…!*

Shao Shen hurriedly wiped the blood from around his eyes. Only then did he recognize one of the men.

A muscular young man who stood a full head taller than everyone else.

The man Shao Shen had only ever seen on television—his idol—was standing right in front of him.

“C-Could you possibly be Mr. Jin from Korea?”

“Huh?”

The young man, Jin Taekyung, tilted his head as he looked at Shao Shen.

“I’m not a teacher.”

“Then… Lord Fuck…”

“…Fuck. What?”

*It really is him!*

Relief and hope coursed through Shao Shen’s entire body, making him tremble.

* * *

*How on earth does a Chinese person know about Lord Fuck?*

Articles about me had caused a brief stir in the foreign media, but I never expected my nickname to spread this far.

*Lord Fuck, making the five oceans and six continents tremble.*

If I ever went to the United States, some huge Yankee bros might approach me with beer bottles and act like they knew me.

*Hey, you. Lord Fuck?*

*I’m fine, thanks. Fuck. What kind of deranged bastards came up with a nickname like this?*

Anyway…

“What a mess.”

That was my brief assessment as I looked around.

Team Leader Choi, who had tied up the unconscious flight attendants like a string of dried fish, and the Skeleton Warlord, who I had shoved into my Inventory, answered me.

“It is a horrifying sight.”

—You wicked human. This commander finds this place quite pleasing. It feels familiar and even nostalgic.

“……”

The fact that a named undead monster—something that could be called death itself—was pleased by the sight said it all.

“We get thrown into actual combat the moment we arrive.”

As if responding to my complaint, the System notification rang.

Ding.

> **System**
>
> —An unexpected Quest, **Unexpected Attack**, has been generated.

*Was this why they said they were paying so much?*

I clicked my tongue and spoke.

“Team Leader Choi, protect the civilians first. After that, fight as you see fit. Don’t push yourself too hard.”

“Yes. That was already my intention.”

Team Leader Choi was a clever man. Learning the Jin Family’s Cultivation Technique had made him incomparably stronger than before, but he would never try to show off.

“And you there, young man.”

“Yes, y-yes, Mr. Jin.”

*Mr. Jin? What am I, a schoolteacher?*

I looked the young man who had answered so quickly up and down.

His face was young, but he was obviously a Hunter. A powerful one, too—probably around A-rank. Unlike the surrounding Hunters, who all wore identical armor as if they had been stamped out in a factory, he also had a red insignia on his shoulder.

“You look like you hold a pretty significant rank, so take good care of your men. Let’s save even one more person.”

“Y-Yes?”

“This is only the beginning.”

As I answered, I thrust out my fist.

Boom!

Streams of Scorching Yang Qi shot toward the monsters standing blankly in place.

When the searing heat swept through the area, only dozens of monster corpses remained.

“Why are you all staring? Did someone hit the pause button?”

“……!”

—……!

At my single remark, the silence pressing down on the battlefield shattered.

—Graaaar!

“K-Kill them! Stop the monsters!”

Humans and monsters. Monsters and humans.

A battle of killing and being killed began. I pulled White Flame from where it was deeply embedded in the ground and swung it.

Shing!

This wasn’t half water and half fish. Monsters filled every direction.

A crescent of Force extending from the spearhead brushed against a tightly packed cluster of monsters.

Ding.

> **System**
>
> —Defeated **Lv. 15 Undead Goblin**!
>
> —Defeated **Lv. 78 Undead Lycanthrope**!
>
> —Defeated **Lv. 93 Dullahan**!
>
> —Defeated **Lv. 30 Skeleton**!
>
> —…
>
> —…
>
> —There is a large Level gap. You gained negligible EXP!

System notifications announcing monster kills and EXP gains rang out without pause.

Under normal circumstances, I would have let such notifications go in one ear and out the other, or simply ignored them.

But this time, they provided an important clue.

“These things couldn’t possibly be…”

—Ah, that’s right. Wicked human! Such a powerful undead army!

The Skeleton Warlord’s delighted shout was enough to turn my suspicion into certainty.

*No wonder something felt strange.*

I had already been puzzled by the fact that I could not sense any life force from them.

There were still quite a few living monsters, but more than half of them were undead. Altogether, they formed a massive army numbering nearly two thousand.

“And undead monsters are…”

The Skeleton Warlord shouted, brimming with excitement.

—Beautiful! Magnificent! Heroic!

Thwack!

I cut down five monsters and muttered.

“Do you want to be annihilated like that thing just now? Beautiful, magnificent, and heroic?”

—……I misspoke. I apologize, wicked human.

The Skeleton Warlord, who had briefly forgotten its current situation, hurriedly added:

—Wait. If that is the case, then they must be under someone’s control!

I thought so, too.

There was only one thing I was not certain about.

“The Lich. Did that bastard personally come here?”

—Hmm. If you mean the Lich in that holographic video you showed me last time, then probably not.

As I listened to the Skeleton Warlord’s answer, I took half a step forward.

Boom!

A massive iron club passed dangerously close to my shoulder and smashed into the ground. It was an ordinary ogre, still carrying the vitality of a living creature.

—Graaaar!

“Sure. I’ll grill you.”

Boom!

The ogre struck in the chest by the Flame Divine Palm spurted dark green blood from all seven orifices.

I passed the collapsing bulk and brought White Flame down at an angle.

Shiiiiing! Slice!

Space itself was cut apart, and the bodies of the monsters caught within it were chopped to pieces.

Leaving behind the Chinese Hunter who stared blankly at me while covered in blood and bodily fluids, I clenched my fist.

Whoooom.

Extreme heat raced into my fist, then shot forward.

Boom!

Flame-Extinguishing Divine Fist.

A massive pillar of fire swallowed the monsters.

Alongside the foul stench of burning flesh, the few monsters that had somehow survived shrieked in pain.

The destructive power was enough to make both monsters and Hunters forget to fight for a moment.

The Skeleton Warlord spoke in a faltering voice.

—W-Wicked human. You have become even more of a monster.

“It feels strange hearing that from a monster. Anyway, if it wasn’t the Lich, then what kind of bastard is causing all this?”

—How should this commander know? But I can guarantee you one thing.

“Guarantee what?”

—His control over the undead is a notch below mine. Wahaha! Legion! This commander has missed you!

“……”

*Should I kill this bastard or let him live?*

As I pondered the question, a thought suddenly flashed through my mind, and I stopped dead.

“Hey. What did you just say?”

—Wahahaha! Have you finally felt the majesty of this commander, wicked human?

“Disappear or talk.”

—……I will talk. But what are you asking about?

“That bit about controlling the undead.”

—Isn’t that obvious? This commander is a Skeleton Warlord. Compared to them, of course I’m… Huh?

A brief silence followed.

The Skeleton Warlord must have reached the same conclusion I had. I swallowed dryly before bringing it up casually.

“Try it. Do that.”

—…….

“Do it, or disappear.”

The Skeleton Warlord opened its mouth.

—Grow, grow, skeletons, skeletons…

At that moment, the undead monsters in the middle of their fierce battle suddenly froze in place.

*…It works.*
## Chapter artifact 381

# Chapter 381

Whoooosh.

I couldn’t see it. But I could feel it.

Centered around me—or rather, flowing out from the Skeleton Warlord in the subspace known as my Inventory—a sticky energy spread in every direction.

The change happened in an instant.

—Kirik?

—Gwoo?

The movements of the monsters, who had been nothing short of ferocious, abruptly stopped.

Orcs, Trolls, goblins, Lycanthropes, every kind of monster I had only ever seen in monster encyclopedias, and even the fallen Hunters.

They had only one thing in common: they had already died once and been resurrected as undead.

Gulp.

I swallowed dryly and muttered.

“It works.”

—Wow. It really works.

“……?”

—……?

*Wait. What did he just say?*

My brain froze for a moment before I whispered,

“What kind of dog-bone bullshit is that? Didn’t you try it because you knew it would work?”

The Skeleton Warlord answered hesitantly.

—The truth is… This commander did not know it would work so easily.

“You said your control was much stronger.”

—Ah, that? I just said it in the heat of the moment.

“What?”

—I was too proud to just sit around doing nothing…

“…….”

*Isn’t this guy completely insane?*

I was dumbfounded, but regardless of that, the result was undeniable.

The undead monsters within a radius of several dozen meters had all stopped moving at once, and the fierce battle raging around us had temporarily fallen into a lull.

「T-The monsters have stopped moving!」

「What in the world is going on?」

「Don’t let your guard down! Some of them are still moving!」

Just as someone shouted, it was still too early to relax.

Only some of the nearby undead monsters had come under the Skeleton Warlord’s control. The ones farther away, along with the ordinary monsters that were not undead, were exceptions.

—Gwoooooar!

—Chiiik!

“Haaah!”

Clang! Stab!

The uncontrolled monsters were only briefly bewildered by the sudden change in their own kind before they began rampaging again, and the battle resumed.

It was a fight where the two sides could not even be compared in terms of numbers.

But from this moment onward, that would change.

I shouted in a hushed voice.

“Go, Warlordmon!”

The Warlordmon—no, the Skeleton Warlord—shouted back in outrage.

—Wicked human! Do not call this commander that!

“Then how about Warlordmon who’s desperate to be annihilated?”

—……Damn it.

Despite being a skeleton that couldn’t even breathe, he let out a deep sigh before chanting a spell.

—Fight, Skeleton Skeleton.

That guy had definitely started enjoying the whole Skeleton Skeleton thing. It was hardly an impressive incantation, but its effect was undeniable.

—Gwoo?

At the Skeleton Warlord’s command, ferocity filled the eyes of the undead monsters that had been standing blankly. Then, in the next moment—

Crunch!

An undead ogre’s iron club crushed a Troll’s skull.

That was the beginning.

The undead monsters who had gained a new master charged at their own kind.

—Gwoooooar!

—Ch, chirik?

Crack! Slice! Stab-stab-stab!

An unexpected ambush from behind.

One flank of the monster army surrounding the Chinese Hunters collapsed helplessly.

—Chiiiiiik!

「W-What the hell!」

「Why are those monsters suddenly…?」

The monsters betrayed by their own kind were not the only ones thrown into confusion.

The Chinese Hunters were also bewildered by the sudden turn of events.

I shouted toward the young Hunter who had been cutting through the battlefield with his spear from the front of the formation.

“Shao Shen!”

「M-Mr. Jin?」

His round eyes looked toward me.

「H-How do you know my name?」

I had just checked his Level with Qi Sense, but that was not important right now.

“What are you doing? Why aren’t you switching to an all-out offensive?”

「But what is going on here…?」

“Are you really curious about that right now? Do you want to grab an undead monster and make it explain why it’s helping us using the five Ws and one H?”

「N-No, sir!」

“Then what should you do now?”

Shao Shen’s eyes cleared, and he raised his spear high.

「Attack formation! Everyone in the Public Security Armed Forces Department, from this moment on, attack everything except the undead monsters!」

「Yes, sir!」

*That was an excellent decision.*

Along with their unified shout, the momentum of the roughly five hundred Hunters who had been driven into a corner changed.

「Kill them!」

「Avenge our fallen comrades!」

Shish-shish-shishik! Slice!

—Awooooo!

A Lycanthrope charged toward a Hunter who had just cut down an Orc.

The creature opened its jaws, yellow fangs aimed at the Hunter’s throat, but a massive fist slammed into its mouth.

Crunch!

—Gwoooooar!

The ogre that had crushed the Lycanthrope’s skull let out a savage roar.

Above the ogre’s head, a Griffon dove sharply. Its razor-sharp claws flashed.

—Kiiiieeeek!

Just as the A-rank monster’s mana-infused claws were about to rake across the ogre’s eyes—

「Ice Ball!」

「Lightning Bolt!」

The waiting ranged Hunters unleashed their magic, and the electrocuted Griffon shuddered in midair.

At that very moment, a figure sprang upward after stepping on a Troll’s shoulder and swung a weapon at the Griffon.

“Specially made by J Company, widely considered one of Germany’s finest weapon workshops—!”

Slice!

The clean, effortless strike split the Griffon’s head in two.

Team Leader Choi landed gracefully and smiled with satisfaction as he looked at the transparent sword blade, which did not have a single drop of blood on it.

“A longsword I won at auction for 5.2 billion won. It certainly earns its price.”

“…….”

*It looks stupid, but it’s cool.*

*It’s cool, but it looks stupid.*

The Skeleton Warlord, who had been watching the scene, asked in a dubious voice,

—Wicked human, you said that man was your superior?

“No, well. Technically speaking, in terms of Guild positions, he is, but…”

—He looked rather clever for a human, but I have never seen such a strange human. He truly is a fitting superior for you.

“Who wants to be annihilated because he couldn’t keep his mouth shut?”

After a brief silence, the Skeleton Warlord answered by chanting another spell.

—Grow, Skeleton Skeleton!

They say even a dog at a village school can recite poetry after three years. Now he could do it without being told.

Crack. Crack-crack-crack.

The Griffon killed by Team Leader Choi, along with the monsters brought down by the combined attacks of the Hunters and undead, gained new life and rose from their dead bodies.

There were two hundred of them.

It seemed the range was also wider than during the first attempt. Even the undead monsters in the distance had come under the Skeleton Warlord’s control and begun attacking their former allies.

“Wow. You were capable of this?”

—Wow. Was this commander capable of this?

“…….”

—……Actually, this commander was not capable of quite this much. But for some reason, an enormous amount of mana is surging through me now that I am here!

“Sure. Great.”

I gave up on trying to understand this bizarre named monster.

As long as the result was good, that was all that mattered. Trying to figure it out right now would only give me a headache.

—Give me more. More legions!

I couldn’t see him because he was inside my Inventory, but I was certain his bony skull was trembling with excitement.

I sighed and tightened my grip on the spear.

“I was planning to.”

—Do you have a way?

“I do.”

The method for increasing the number of undead was simple.

“Kill them all.”

—Kahaha! You truly are a wicked and ignorant human!

The bastard was being cheeky, but this time, I had no choice but to agree with part of what he said.

Listening to the Skeleton Warlord’s laughter echo through my mind, I stepped forward.

*Flamefire Path.*

Whoooosh!

A path of flame opened with every step.

* * *

Black robes. A staff with skulls dangling from it.

The places where their pupils should have been were empty, and patches of flesh that had yet to rot still clung to their bodies.

The three beings, who looked as though they had stepped out of a nightmare, conveyed their thoughts to one another.

—There is a problem.

—The undead monsters are slipping out of our control. They are helping the humans and attacking the legion.

—Why?

They were not asking how their control had been broken. The three beings already knew the answer to that question.

—A higher undead. One more powerful than us.

All monsters had a hierarchy, but undead were ruled by power more absolutely than any other species.

If control had been stolen from them like this, it was undoubtedly the work of a higher existence.

—But…

—How is that possible?

None of the three beings could answer.

How could an existence more powerful than them be here, seize control of the undead, and help the humans?

—Could it be that person?

—That is absurd. Have you forgotten the command that person gave us when sending us here?

—Kill the humans. Create more undead and an army, and kill more, more humans.

The three beings recalled the command and fell into a state of confusion.

If that person—the Arch Lich—was not responsible, then who could possibly surpass their control?

—Was there a necromancer among the humans?

—I sensed nothing.

—Humans reject and despise death. That is impossible. Even if there were one, they would be nothing compared to us.

The reason unmistakable hostility could be felt in their thoughts was that they, too, had once been necromancers who had suffered human rejection and contempt.

But that had happened in the distant past, in another dimension.

Drifting across the boundless ocean of death, they had met a boatman named the Arch Lich. After gaining new power, they were finally on the verge of becoming the Liches they had longed to be.

But…

—What a shame.

—If only our transformation had been completed. If only there had been more death in this land.

—Then we would not have lost control, either.

The three beings could not hide their regret.

They had been great necromancers while alive, but they had not yet fully transformed into Liches.

They had been reborn using the bodies of dead mages, but one week was far too short to absorb enough death energy to complete their transformation into Liches.

—That is why that person sent the three of us.

—If this mission fails, that person will be disappointed.

—That person might even take back the power they gave us.

That was what the three beings feared most.

They had to overcome this crisis somehow if they wanted to earn the Arch Lich’s favor.

Even if it meant exhausting a tremendous amount of power.

—There is no other choice.

—Are you suggesting that we combine our strength?

—Yes. If the three of us combine our strength, even an unidentified higher undead will no longer be able to steal control from us.

—Hmm. Fine.

—Do you agree?

—I agree.

The three beings, who had been competing to earn the Arch Lich’s favor, finally reached an agreement.

Without hesitation, they began chanting a spell of necromancy.

—Valencia. Madrid.

—Bayern. Munich.

—Stoke. City.

The energy of death flowing from the three beings spread through the air.

The green grass turned black, and the soldiers of the People’s Liberation Army within its range clutched their throats and collapsed.

“Ghk!”

“Guhhh!”

Whoooosh.

The death energy flowing from the bodies of the humans whose lives had been cut short seeped into the monsters’ entire bodies.

—Kyaaaaaaah!

—Gwoooooar!

The air trembled from the powerful mana carried in their savage cries. Their strength was beyond comparison with that of ordinary monsters.

Only after sensing their strengthened control and the power of the monsters under their command did the three beings stop chanting.

—Kikikikik.

—Success.

—We did consume an enormous amount of power… but this is more than enough.

Just as the three beings were smiling in satisfaction at their now more powerful army—

Boom!

Far away, a monster’s limbs flew through the air with a thunderous explosion.

The three beings looked toward the rising flames and exchanged thoughts.

—There appears to be a flame mage. Not bad.

—He is still only human. Deploy a large number of Skeleton Mages.

—Good idea.

A short while later, more flames rose into the distance, and the three beings looked at one another.

—What was that just now?

—Our control was severed. It was not stolen.

—Did he annihilate them? Impressive.

—But is he really a mage? His movements seem far too fast…

—Let us deploy the ogre unit.

—I’ll see your ogres and raise you Dullahans.

—Dullahans, too? Then who will protect us?

—He is right. Dullahans would be excessive. Strengthened ogres will be enough.

—That is true.

Three minutes later, a grim atmosphere hung over the three beings’ skulls.

—It broke.

—Again?

—I told you we should send Dullahans.

—What is that thing? It does not seem to be a mage.

—J-Just send the Dullahans first!

—Th-Then we shall do so.

The three beings watched as more than twenty Dullahans, chosen as their escort force, rushed away. Then they quietly began searching for another point of agreement.

—Hmm. It is unlikely that such a thing will happen, but just in case…

—I had a similar thought.

—Should we create a Death Knight?

—We have already consumed too much power. A Death Knight, too? We do not have suitable materials, and it would take a long time.

—In an emergency, we can choose the most useful one and make it. If the three of us combine our strength, it will be possible.

—Th-Then should we try?

But the three beings’ plan to create a Death Knight was smashed to pieces less than ten minutes later.

Whoosh! Boom!

Even with nothing but bones left on their bodies, they could feel the heat of the searing flames.

“Fucking bastards. There’s a shitload of them.”

Crunch!

The three beings witnessed an existence tearing through the monster army with a spear engulfed in hellfire and hurriedly began chanting spells.

Their slow, dragging voices had become as fast as rap.

—Omnehasoyu!

—Yenwigajike!

But before the chant was complete, the young human who could not be identified as either a flame mage or a warrior had already arrived right in front of them.

“Oh, nice to meet you.”

—O-Omnehasoyu!

—Y-Yes, Yenwigajike!

The young man, Jin Taekyung, tilted his head to one side.

“Hello. *Entertainment Weekly*? Are you idiots?”[^1]

[^1]: The garbled incantations sound like the Korean phrase *annyeonghaseyo, Yeonye-ga Junggye* (“Hello, *Entertainment Weekly*”), using the title of a long-running Korean entertainment-news program.
## Chapter artifact 382

# Chapter 382

Strike the head, and the body falls.

The moment I seized the three who looked like the leaders, the undead they had been controlling stopped moving like wind-up dolls, and the monster army, having lost its command structure, scattered and collapsed. Some died, while others fled.

“Arch Lich?”

At my question, the three kneeling figures nodded.

I wasn’t sure whether I could call things that were already dead and reduced to bones “guys,” but whatever.

I stroked each of the three skulls in turn and continued.

“When someone talks to you, you’re supposed to answer. Are you putting on airs just because you’re dead?”

The answer came almost before I had finished speaking.

—Yes. Yes. It is an Arch Lich.

—What you heard is accurate, human sir.

—Indeed.

“Hmm. An Arch Lich. That’s a monster I’ve never heard of before… But which one of you answered informally at the end?”

—That one!

—How dare he speak so casually to our great human master!

Whip! Whip!

The bony fingers pointed at one of them.

Betrayed by his comrades with lightning speed, the accused skull began to tremble.

—No! This is a despicable false accusation!

“…I don’t think it’s a false accusation.”

If he was going to lie, he could at least have changed the way he talked.

After glancing around, I took *that* out of my Inventory.

“Bones. Time for a snack.”

A skull with a strange black sheen. Flames flickered in its empty eye sockets.

—…Bones? If you insist on calling me something, call me Warlordmon like before.

“Why? You’re a skeleton, so Bones. It fits perfectly.”

—How dare you insult this commander like this!

“If you don’t like it, fine.”

Just as I was about to put it back in my Inventory, the Skeleton Warlord shouted in an enraged voice.

—Thank you for the meal!

“What an honest little guy.”

Honest children deserved rewards. Liars deserved punishment.

“All right. Have a taste.”

—Thank you. You are a slightly less wicked human. But how much should I eat…?

“Just a little, like before.”

—Hmm. I want to eat more. But I understand.

Even snacks were too much if you gave them out too often. After expressing its slight disappointment, the Skeleton Warlord opened its jaws wide toward the trembling figure.

—Come here.

—Eek! No!

—Yes!

The change began with the Skeleton Warlord’s decisive shout.

Whoooosh!

That was still amazing, even after seeing it again.

Like being sucked up by a vacuum cleaner, black mist began flowing from the kneeling figure’s body and being absorbed into the Skeleton Warlord.

—Gaaah!

But the change did not end there.

The more black mist flowed out—the substance the Skeleton Warlord called death energy—the whiter the figure’s complexion became.

Or, rather, its bones became whiter and whiter.

The Skeleton Warlord’s black sheen, meanwhile, grew deeper and richer.

—S-Stop!

—Heh heh heh. Such delicious death energy.

—Nooo!

—This commander shall take it all. Deeeath energy!

Crack!

—Hrk!

“Don’t go around saying ‘deeeath energy.’ Where did you even learn something like that?”

—…Are you really in a position to say that?

“Anyway, stop eating now.”

—Why?!

“You’ll get fat.”

The Skeleton Warlord fell silent for a moment. I tucked it inside my clothes and looked at the figure.

When I had first seen it, its bones had been dark and dirty. Now, it was half-white, as though it had been bleached. Perhaps because it had lost so much death energy, the green light in its eye sockets swayed dangerously.

—Hic… Sob…

At the sight of their comrade, who had been sucked dry down to his bones, the other two anxiously clicked their teeth together.

—Command us in anything, great ruler of flame.

—Please, I beg you. Accept the loyalty of this insignificant being, Orpheus von Maximus Valencia Bayern.

“…You’re undead, not a bidet.”

They really didn’t want to lose their strength. Well, I was grateful that they were being so cooperative.

“All right. If there’s anything you haven’t told me, scrape the bottom of the barrel and confess everything. If you start feeding me any lies…”

—We will tell you everything!

—Please, I beg you. Grant this false and insignificant being permission to speak the truth!

—I-I will tell you.

Apparently unwilling to become bone broth, the three skeletons enthusiastically participated in the interrogation.

After hearing every single thing that had happened from the Arch Lich’s first appearance a week ago until now, I deliberately furrowed my brow.

“Are you sure?”

—Yes, great human!

—I swear upon the River of Death!

—T-There is not a single lie.

At the sight of the three vigorously nodding skulls, the Skeleton Warlord suddenly interrupted.

—It is true.

“Did they pay you off? How can you guarantee that?”

—Because they swore upon the River of Death. For beings like us, that is an absolute promise. It cannot be broken.

“Hmm.”

The guy was usually as frivolous as they came, so hearing it speak with such gravity made me think this probably wasn’t a lie.

Besides, the three of them had no reason to scheme in a situation like this.

“All right. I believe you.”

—Thank you! Thank you so much!

—Sob, sob! I shall devote my entire loyalty to you, my king!

—I-I mean, I will also swear loyalty to you, human sir. I swear upon the River of Death that I will never commit an act like today’s again—

Crack!

The last one could not finish speaking.

His trembling green eye light shifted back and forth between the fist embedded in his chest and me.

—W-Why?

“Why do you think?”

—I-I, loyalty, swear, River of Death…

“You’re too late.”

A voice as cold as though it belonged to someone else slipped through my lips.

“It’s too late to undo what you’ve done.”

A great many people had died here today.

Even regular troops armed with firearms and Hunters had been unable to stop them, so there was no telling how many civilians the monster army had killed over the past week.

“I don’t need your loyalty. Especially not when it’s offered by bastards like you.”

The moment I released the Scorching Yang Qi I had drawn up from my dantian—

Whoosh!

Extreme Yang energy surged from the fist embedded in the figure’s shattered ribs. Blue-white Force, radiating a heat beyond anything ordinary, coiled around its entire body.

Boom!

I saw it.

The green light in its eye sockets flickered like a candle in the wind, then went out.

I also saw the other two figures spring to their feet and begin chanting spells.

—Jazuchawa Umbado…!

—Vargan Mahra…!

Whoooom.

A wind of mana swirled around them. Just as their sinister spell was about to be completed, I casually said,

“Devour them. All of them.”

As though it had been waiting only for those words, the Skeleton Warlord leaped from between the folds of my clothes and opened its jaws wide.

—As you command.

—Varsaba… Eek!

—N-No!

The final screams of monsters that wanted to live—or, rather, wanted to remain undead.

But contrary to their wishes, the Skeleton Warlord’s suction was stronger and faster than ever.

Whoooosh! Gulp!

After swallowing an enormous amount of death energy in a single bite, the Skeleton Warlord’s skull trembled.

In the next moment, the two skeletons whose energy had been completely drained collapsed in a heap.

Ding. Ding. Ding.

> **System**
>
> —You have successfully completed the unexpected Quest, **Unexpected Attack**!
>
> —You have caused the monster army to collapse! This is truly an outstanding achievement!
>
> —As a Quest Reward, you have acquired the Title **Undead Hunter**!
>
> —You have acquired a considerable amount of EXP and Fame!
>
> —Level Up!

*Only once?*

In the past, I would have leveled up several times without difficulty. But now that I had reached Level 120, it seemed the amount of EXP I needed had increased.

*It’s not like I did this for the EXP.*

I had merely done what needed to be done, but I couldn’t help feeling a little disappointed.

The stronger I became, the more useful I would be in the battles ahead.

*That guy is the same.*

I looked at the Skeleton Warlord while thinking to myself.

Perhaps because it had absorbed such an enormous amount of death energy, the power I felt from it was incomparable to what I had sensed when we first met.

—Hmm. Hoooo…

Black mist billowed through the holes in its skull where its nose, ears, and eyes should have been.

Its violet eye light burned like torches, while its surface gleamed with a smooth, deep-black sheen. Soon, its mad laughter reverberated through my head.

—Kahaha! Kahahahaha!

“Turn down the volume. You’re loud.”

—You wicked human. This time, this commander shall offer you his profound gratitude.

“You should. Who gave you your food?”

—Food?! Are you saying this body has become some kind of pet?!

“Something like that. Isn’t it?”

—Don’t talk nonsense!

“Oh? Bones, come here.”

When I held out my hand, the skull sprang up and landed in my palm.

As a reward, I gently scratched the spot between its eyes.

“Good job, Bones. Oh, aren’t you adorable?”

—…!

The skull began to tremble.

—H-How could this happen?! How could this commander be treated like this by a mere human?!

“You say no with your mouth, but your body is honest.”

—I am the master of the Black Forest and the commander of the great undead army. Do not humiliate this body!

“A commander with nothing but a head left?”

—What?! This insignificant body can be restored as many times as necessary as long as I expend death energy!

“Really? Then why haven’t you restored it yet?”

—…Because even if I restored it, some crazy human would just smash it again.

“Oh, correct.”

Grind.

The Skeleton Warlord had no teeth, so it ground its bones together instead. Its eye light narrowed.

—Why, wicked human?

“What?”

—You must have some ulterior motive for feeding me—or rather, for giving me such enormous power. You obviously have some dark scheme in mind. Speak the truth!

I thought for a moment before answering.

“Hmm. Because you’re a fucking scrub.”

—Huh?

“You can’t beat me anyway. If that’s the case, it’s easier to make use of a stronger, more useful scrub. Don’t you think?”

—…!

“All right. Stay inside now. People are coming.”

I put the Skeleton Warlord, frozen from the shock, back into my Inventory and stood up.

The airport duty-free corridor should normally have been crowded with employees and passengers. Now, in the empty, darkened passageway, three people were walking toward me.

Two of them had familiar faces.

“Mr. Jin Taekyung.”

“Mr. Jin.”

It was Team Leader Choi, who was in relatively decent shape, and Shao Shen, an A-rank Hunter from the Public Security Armed Forces Department of China.

Even though a considerable amount of time had passed since the battle ended, Shao Shen’s face was still covered in blood and dust, and exhaustion had settled heavily over his features.

“There you are.”

I exchanged a look of greeting with Team Leader Choi before making an excuse.

“Yes. I had something to take care of.”

“Please speak casually with me. Fuc—no, Mr. Jin, you are the hero who saved me, my comrades, and even the people of Zhonghua.”

“…”

*Was that my imagination, or had he almost called me Lord Fuck just now?*

Whether he knew what I was thinking or not, Shao Shen continued in an extremely respectful tone.

“Fortunately, with the help of the two gentlemen from the Peace Guild, we were able to defeat the monsters. I would like to take this opportunity to express my gratitude once again.”

“Ah, yes. It was nothing. It was simply what had to be done.”

I waved my hands modestly and stole a glance at Team Leader Choi.

I had worried that the *Integrated Language Pack* might malfunction and he might notice something strange, but since Shao Shen was the one I was speaking with, it seemed that Team Leader Choi was hearing my words as Chinese as well.

“But who is the person beside you…?”

The only unfamiliar person among them was a middle-aged man with graying hair. He had silently listened to our conversation before extending his hand for a handshake.

“I am Wei Fenghu, the Minister of National Defense under the Central Military Commission. It is a pleasure to meet you, Mr. Jin.”

“If you’re the Minister of National Defense, then…”

“My rank is general.”

“Ahh.”

I knew that meant he was important, but I had no idea what rank that actually was.

Perhaps he had read my thoughts, because Team Leader Choi whispered from beside me in a voice barely louder than an ant.

“Four-star. Four-star.”

“Ahh, ahhh! So you’re a general! It’s a pleasure to meet you!”

I had been a four-star once, too. That game I played when I was young had been a lot of fun. The sequel had bombed so badly, though.

At my reaction, Wei Fenghu clasped my hand with a faint smile.

“You are full of youthful vigor. I have many things I would like to ask you, but shall we talk while we walk?”

“Sure.”

I started to follow Wei Fenghu, then stopped.

“Where are we going?”

“To the operations headquarters. I have a jet waiting.”

“What? Headquarters? A jet?”

“That is correct. Everyone is waiting for you there, Mr. Jin.”

*Everyone? Who?*
## Chapter artifact 383

# Chapter 383

The jet Wei Fenghu had prepared looked quite different from what I had imagined.

*It’s spacious. And fancy.*

Through the slightly open cabin door, I could see a luxurious table and what people usually called a chairman’s chair.

Team Leader Choi, who was standing beside me, informed us that the business jet we were looking at cost nearly one hundred billion won per plane, then added,

“Never thought I’d see an aircraft used for state guests here.”

“It is only natural. The two of you are state guests of our country.”

“Ah.”

“Thanks to you, we were able to save countless soldiers and Hunters. None of us—not even me—will ever forget the help you gave us today.”

“…Ah, yes.”

I would have preferred it if they dealt with the fine dust and historical distortions first.

Still, I boarded the aircraft while secretly hoping China was a more conscientious country than I knew.

The waiting pilot saluted us—or, more precisely, Wei Fenghu—with crisp, disciplined movements.

“You have arrived, Comrade Minister of National Defense.”

“How are the preparations?”

“All escort aircraft, including this one, have completed their preparations. We await only your order.”

I had wondered what he meant by “escort,” but then I saw five fighter jets on the runway outside the window. Their sleek, curved bodies flashed their lights as though signaling us.

*What the hell are those?*

I had only ever seen things like that in war movies. Were we about to go off and fight a battle right now?

When Wei Fenghu saw my eyes widen, he spoke.

“It has not yet been properly announced to the outside world…but as you know, Sichuan Province is currently in a state of war. Magical interference with communications and attacks by flying monsters are occurring frequently, so an escort is essential for safety.”

“Is that really true?”

The situation was more serious than I had expected.

The Wyverns had only attacked us in passing while they were raiding Chengdu International Airport, but if this was happening throughout Sichuan Province, that changed things completely.

“If only I were lying.”

Perhaps merely thinking about the current situation exhausted him. Wei Fenghu, who seemed to have aged considerably in a short time, leaned back into the soft seat.

“It seems we must part ways here. We will meet again soon, Senior Colonel Shao Shen.”

Unlike us, one person had not boarded the aircraft. Shao Shen stood at attention and saluted.

“Yes. I will join you after completing my mission as quickly as possible, Comrade Minister of National Defense. And you two gentlemen.”

“Good. I have high expectations.”

Perhaps because he had achieved such impressive accomplishments, a pleased smile passed across Wei Fenghu’s lips as he looked at the promising young Hunter.

Team Leader Choi substituted a respectful bow for a farewell, while I waved.

“See you next time. You fought really well today.”

It had only been one sentence.

But the moment Shao Shen heard my words, his eyes grew as wide as serving trays. His body trembled as though he had been electrocuted, and then he shouted at the top of his lungs.

“Th-Thank you! I will devote myself to every task with the utmost loyalty,[^1] so that you never have cause to be disappointed in me, Mr. Jin!”

“…No need to go that far.”

“May your august self remain safe! Loooyalty!”

“‘August self’? What are you—”

Whack!

“Ugh!”

“…”

That seemed like a textbook example of poor judgment.

He had saluted with such force that the edge of his hand had struck his own eyebrow.

I was staring at Shao Shen as he clenched his teeth and endured the pain when the entrance closed, and the business jet carrying us began to take off.

“That guy is, well, how should I put it… His character is pretty unique.”

At my dissatisfied comment, Wei Fenghu let out a quiet laugh.

“You can hardly blame him. He received praise from his idol.”

“Excuse me?”

“There are many young Hunters in our country who admire you, Mr. Jin. That young man is no exception.”

*What the hell? Was I a Korean Wave star?*

Come to think of it, for a four-star general reputed to be able to knock birds out of the sky with a single finger, this man seemed unusually interested in his subordinates.

Or maybe Shao Shen was simply that promising.

Ah, but…

—Team Leader. How important is the Minister of National Defense under the Central Military Commission, exactly? I’m not very familiar with the structure over here.

Team Leader Choi flinched at my Sound Transmission and answered through Message Magic.

—If you compare it to our country, he is the Minister of National Defense. Of course, this is China, and Wei Fenghu is the current Chairman’s right-hand man, so his power is considerably greater.

—Ah.

*He’s not that different from me. I’m the Minister of gukbap.[^2]*

One special serving of sundae-guk was enough to handle three bowls of rice.

Of course, Wei Fenghu could probably erase three cities with a single pointed finger.

And now, that powerful figure of the People’s Republic of China was leaning his upper body toward us and asking,

“It seems we have many things to discuss during the journey. Would you not agree?”

Team Leader Choi and I nodded solemnly and opened our mouths.

“Of course. First, I would like to ask exactly what is happening in Sichuan—”

“But do you happen to have any boiled eggs and soda? I’m hungry after fighting so hard.”

“…”

“…”

Apparently, they did not.

“We do.”

“…”

“…”

They did.

* * *

The People’s Republic of China.

As one could tell from the country’s formal name, these imposing people of the continent still held socialism as their national ideology.

About twenty years ago, the Chairman of that time died during the Great Cataclysm after laying a firm foundation for dictatorship through lifelong rule. Power was transferred to a much more moderate government, but the core remained unchanged.

—What was the dead Chairman’s name again? Pingping? Paengpaeng?

Team Leader Choi, who had been chiming in as Wei Fenghu spoke, silently moved his lips. His poker face was astonishing.

—Just in case you were wondering, saying something like that here would get you into serious trouble.

—That’s why I’m using Sound Transmission—no, Message Magic.

—I’m telling you to be careful. Some outstanding mages of A rank or higher can eavesdrop on Message Magic.

—Anyway, what was his name? Pingping or Paengpaeng? If I don’t find out, I won’t be able to sleep tonight.

—…Pingping.

*You were going to answer me in the end anyway.*

Now that I was finally satisfied, I listened closely to Wei Fenghu’s words.

“No one could have predicted what happened.”

Sichuan Province was an enormous region with a vast area and a population of tens of millions.

And all of this had begun in Gaoping District of Nanchong City, one of the roughly twenty administrative divisions in Sichuan Province.

“As you know, our country has more than ten times as many Gates as other countries. Because of that, we were one of the nations hit hardest during the Great Cataclysm, and we have managed them with corresponding rigor ever since.”

But human power could not control even natural disasters, and the Monster Wave was a calamity far worse than any natural disaster.

“We received word that the mana levels in Gaoping District had suddenly spiked exactly thirteen minutes after the first signs appeared. And by the time Lei Fei, head of the Public Security Armed Forces Department stationed in Sichuan Province, arrived at the scene with the Hunters under his command…everything was already too late.”

“Lei Fei?”

The name was unfamiliar. And yet, for some reason, a memory suddenly came to me.

*That video Team Leader Choi showed me at the Guild house before we left.*

I still remembered it clearly. A city thrown into chaos beneath the light of a hologram, and a man cutting down monsters at the head of the Hunters.

An aura bright enough to blind me had gathered around his weapon.

“I think I’ve seen him before. Is he the one who appeared in the video you sent us…?”

“That is correct.”

Wei Fenghu hesitated for a moment before speaking with a faint sigh.

“He was one of our country’s S-rank Hunters. Of course, the two of you would not have known about him.”

*We wouldn’t know?*

There were only twenty S-rank Hunters in the entire world. They were absolute powerhouses.

The fame and status they enjoyed were far greater than those of even a Supreme Peak master in the Murim.

The internet, news, and social media were their platforms, while microphones and cameras followed them like shadows.

If the common people of the Murim looked at martial artists with half wariness and half curiosity, modern people simply admired Hunters. They were celebrities known throughout the world.

*But we’re supposed to not know an S-rank Hunter like that?*

Wei Fenghu had spoken indirectly, but it was enough for me to understand what he meant.

Team Leader Choi’s gaze met mine in midair. At that moment, we were thinking the same thing.

*An undisclosed S-rank Hunter.*

No, to be precise, an S-rank Hunter deliberately concealed by the Chinese government.

*I’d only heard rumors about things like this. So they were true?*

An S-rank Hunter was practically the face of a nation.

But unlike the weak, who struggled desperately to avoid being underestimated, the strong concealed their claws.

China was already known to possess two S-rank Hunters. It was obvious that they had not wanted to reveal all their strength.

*Maybe the other great powers of the world were the same.*

*Good grief. Even after surviving the Great Cataclysm, they’re still playing this kind of game of nerves.*

It was pathetic, but at the same time, I thought I could understand it. Diplomacy. Politics. I felt as though I had caught a glimpse of the truths of a world I had never known, and the feeling was strange.

Unlike me, however, Team Leader Choi was sharper.

“When you say he ‘was’ one of the S-rank Hunters your country possesses, I take it you are speaking in the past tense.”

Wei Fenghu answered with a devastated expression.

“…A week ago, when the first Monster Wave began, Lei Fei disappeared. Along with the Hunters of the Public Security Armed Forces Department under his command.”

“Are you certain he is missing? Perhaps…”

“We could not confirm his death. After that video was recorded, the monster known as the Lich—no, the Arch Lich—blocked all communications and surveillance with mana.”

Team Leader Choi and I both groaned.

At our reaction, Wei Fenghu asked in a hoarse voice,

“Do you two also believe that Lei Fei is dead?”

“Hmm.”

“Uh…”

If someone had disappeared in that chaos a week ago, the outcome was practically decided already.

At Team Leader Choi’s glance, I cautiously opened my mouth.

“Well, you never know what can happen to someone, but…”

“The other experts said he was one hundred percent dead. Useless windbags, the lot of them.”

*Why are you saying that? They seem like genuine experts.*

If anyone claimed he was alive in that situation, they should be fired immediately. That was simply a fact.

“But I disagree. Lei Fei—my boy—is certainly alive.”

“I hope so too, but realistically speaking…”

“He is my only nephew. My sister had been sickly since childhood. She died in childbirth, unable to survive the ordeal, and I raised that tiny baby, who had not even been weaned, as if he were my own son.”

“Excuse me?”

*Your nephew? You raised him as your own son? What is this supposed to mean?*

As I sat frozen like a statue, Wei Fenghu asked me with damp eyes,

“What were you about to say? After ‘realistically speaking.’”

*Crap. This is an all-time crisis.*

My words caught in my throat. I barely managed to squeeze out a voice.

“I was going to say that, realistically speaking, there is still a chance he could be alive.”

“Is that so? Is that really true?”

“Yes, but that chance is extremely slim—”

“Thank you, Mr. Jin!”

“No, General. Commander. Supreme Leader. Please hold on for a moment and let me finish…”

Grab!

It was too late. Wei Fenghu was no longer listening to me. Instead, he clasped my hand in both of his, his eyes brimming with tears.

“May I ask you for one favor?”

*I really wish you wouldn’t.*

Contrary to my desperate hopes, a few seconds later, the one sentence I had expected pierced my heart.

“If you happen to meet that boy someday, could you bring him back to me?”

“…”

“I beg you.”

Over Wei Fenghu’s shoulder, I saw Team Leader Choi shaking his head.

What if I had answered firmly from the very beginning? I regretted it, but it was already too late.

In the end, there was only one answer I could give.

“I will. But…”

“Mr. Jin.”

“Yes?”

“You do not need to say it. I am already prepared for what may happen.”

“…”

Wei Fenghu wiped the corner of his eye with his sleeve. He had returned from a middle-aged man worried about the safety of his blood relative to the Minister of National Defense under the Central Military Commission.

“This is enough. No one was willing to step forward, but you have given me your word, Mr. Jin. I am relieved.”

“I cannot guarantee anything.”

“I did not need someone’s boastful guarantee. What I needed was a thread of hope.”

Just as Wei Fenghu murmured those words, the aircraft began to descend, accompanied by a sudden sensation of floating.

Outside the window, beneath a blanket of deep darkness, I could see rugged mountain ridges, lights moving without pause, and military vehicles.

“It seems we have arrived.”

I had been staring fixedly out the window as though possessed by something. Then I asked,

“Where are we?”

“A temporary operations headquarters.”

“No. That is not what I meant.”

“Hmm?”

“For some reason, that mountain feels strangely familiar.”

“That cannot be. As far as I know, you have never entered our country… Ah, could you have seen it in a photograph?”

“A photograph?”

“It is a UNESCO-designated World Cultural Heritage Site, so that would certainly be possible.”

With a faint smile, Wei Fenghu continued,

“Temporary operations headquarters. Welcome to Mount Qingcheng.”[^3]

[^1]: A self-deprecating Korean idiom meaning to offer one’s utmost loyal service, literally “the labor of a dog or horse.”

[^2]: *Gukbap* is rice served in hot soup; here, Taekyung is riffing on the similar sound of *gukbangbu*, the Ministry of National Defense.

[^3]: Mount Qingcheng is a UNESCO World Heritage site associated with the Qingcheng Taoist tradition.
## Chapter artifact 384

# Chapter 384

Mount Qingcheng.

A sacred Taoist site bearing the imprint of ages.

Anyone who stood before its stern, overwhelming mountain ridges would lose their words for a moment and stare.

But I was amazed for an entirely different reason.

*It’s definitely different…but it’s similar.*

Mount Qingcheng in the Murim. Mount Qingcheng in the modern twenty-first century.

The two worlds I had experienced so far resembled each other in many ways. Their terrain, languages, people’s features, and lifestyles were all similar.

At one point, I had even wondered if the Murim might be the distant past of the modern world.

*But it wasn’t.*

The butterfly effect? It wasn’t like something I had only seen in movies could really happen.

The two worlds were certainly similar, but they had subtle differences, and their histories were different as well.

The Murim world was also smaller than the modern one, and it wasn’t divided into five oceans and six continents.

There were people with colored eyes living in far-off foreign lands, but that was all. The continent ruled by a vast Great Nation was the center of that world.

Perhaps the Zhonghua that Chinese people insisted on so tiresomely was the Murim itself.

*But why did even this have to be similar?*

I had just returned from the Three-Gate Bloodbath, which had mercilessly dyed Sichuan Province in blood, only to come to Mount Qingcheng in Sichuan Province.

I couldn’t tell whether it was a simple coincidence or a terrible connection.

I really hoped it wouldn’t be similar in that way, too…

“Mr. Jin?”

“Mr. Jin Taekyung.”

“Ah.”

I raised my head like someone waking from sleep.

Wei Fenghu and Team Leader Choi had already gotten off the business jet and were looking at me strangely.

“Sorry. I got distracted by the scenery for a moment.”

“It is so dark, yet you can see the beauty of Mount Qingcheng. You truly possess extraordinary mana, Mr. Jin.”

That wasn’t wrong, but now that I had reached the Supreme Peak realm, I could generally see clearly with my eyesight alone, without relying on internal energy.

When I nodded with a complicated expression, Wei Fenghu admired me.

“Now I understand why Korea has hidden you away so carefully, Mr. Jin. You are worthy of being called an S-rank Hunter—the face of your nation.”

“Excuse me? I’m still officially A-rank.”

“There is no need to hide it. Our country has already grasped the situation to some extent.”

Before I could say anything, Wei Fenghu continued smoothly.

“To become an S-rank Hunter, one must attain enlightenment through relentless mental cultivation and arduous training. Our country also had to endure countless trials and errors to foster its current Hunters…but to reach such a realm at an age as young as yours means that the Korean government must have given you its full support.”

“…?”

“…?”

“Of course, Mr. Choi beside you is also an excellent Hunter. With people like the two of you working together, I feel reassured.”

*What kind of reassuring gukbap nonsense is that?*[^1]

Team Leader Choi and I exchanged a brief glance and reached a silent agreement.

*Keep your mouths shut.*

*Let’s just go.*

It seemed to be a misunderstanding brought about by the fact that I had reached this position in such an unrealistic way. But there was no reason for us to remove the label they had already stuck on us.

Besides, it would be annoying to convince Wei Fenghu right here.

“Hmm. I think there’s been a slight misunderstanding, but I’ll explain everything bit by bit when the time comes.”

“What is there to misunderstand? We both know each other’s circumstances.”

“…”

“…”

“Even the Chairman already knows about the matter. When you meet him, do not bother denying it. Just accept it as it is.”

*Knows what?* I let out a quiet laugh.

*Speaking of the Chairman…*

He was a kinglike figure who held more than a billion people, the economy, and the military of the People’s Republic of China in one hand.

Even now that I had reached the Supreme Peak realm, he was a being who felt close yet infinitely distant to me, a man with modern common sense rooted in his bones.

*I wonder if I’ll get to see his face after this is over.*

Well, what did it matter? That was a problem to think about much later.

Even without my raid pay, my weekly salary was ten billion won. To me, he was simply a generous employer.

I got to save people and make money—two birds with one stone.

“I’ll do that. When I meet him.”

“Good. Then let us go meet him.”

“Excuse me?”

“Did I not tell you? He is waiting in the underground bunker right now.”

*What the hell was going on?*

I stared blankly at Wei Fenghu’s back as he walked ahead, then approached Team Leader Choi and whispered quickly.

“D-Did you hear that?”

“Yes, I did. But it is unexpected for me as well. For the Chairman of China to leave the safety of Beijing and come all the way here… It seems the public perception of him is at least partly accurate.”

“To hell with public perception. China’s Jongseok—Jongseok!”

“Not Jongseok, General Secretary! The Chairman!”

“Hmm? What did you just say?”

“Nothing, Minister.”

Team Leader Choi politely covered for us when Wei Fenghu suddenly turned around. Then, with an earnest and serious expression I had never seen on him before, he said,

“Mr. Jin Taekyung. You must not make the same kind of verbal mistake in front of the Chairman. Understood? Especially do not even mention Jongseok. It sounds like the name of some high school classmate.”

“Huh? How did you know?”

“…”

*I think Team Leader Choi just said fuck.*

*Must be my imagination.*

*It’s not Jongseok. It’s General Secretary. China’s Chairman.*

Unlike Team Leader Choi, who had been born into the aristocratic elite, I was an ordinary citizen to my core.

No matter what feelings I had normally held toward China, my heart pounded at the thought of meeting the leader of one of the ten most powerful nations in the world.

*Let’s just not make any mistakes. Especially not Jongseok.*

Ten minutes later, beneath the ground in a deep underground bunker, I shook hands with the leader of the People’s Republic of China while receiving the gazes of all the important people gathered there.

“Nice to meet you, Mr. Jin. This old man is Shao Yang, the Chairman of the People’s Republic of China.”

*Good. There was no reason to bring up even a syllable of Jongseok.*

Having cleared that hurdle, I opened my mouth with a relaxed expression.

“Welcome.”

“……?”

“……?”

*Ah, fuck.*

* * *

Chairman of the Chinese Communist Party’s Central Military Commission and General Secretary.

The Chairman who stood at the apex of more than a billion people.

Shao Yang.

His voice directed at the people was gentle, while strength filled his eyes.

“As you all know, unfortunately, I am neither a military expert nor an outstanding general. I am merely a political schemer who entered politics early and managed to achieve one small ambition only after reaching the age of seventy.”

The fact that the leader of the country with the fourth-largest territory on Earth and the largest population called himself a schemer was so unconventional that it was hard to believe the words had come from his mouth.

*So this is what Team Leader Choi meant by the public perception of him?*

I felt as though I had a rough idea of what kind of person he was.

Perhaps it was merely a mask or hypocrisy he had put on before the people.

But at least from the old man speaking before all of us now, including me—Shao Yang, the Chairman of China—I sensed a kind of qi utterly unlike either of those things.

“Please do your best. I ask you to save as many more people as possible and stop this terrible disaster as quickly as you can. If you do so, I will show you and your countries my proper gratitude and remember the help you have given us for a long time.”

The truth was, I didn’t know what kind of life that old man had lived or what policies he had pursued.

But I wanted to give him considerable credit for reaching out to countries around the world for help in order to save his own people.

“That is all this old man has to say. Please do not concern yourselves with complicated matters such as politics. I earnestly ask you to find the best way to stop this situation with the fewest possible sacrifices.”

The old political veteran who had devoted his entire life to politics turned his head and looked at one man.

“Minister of National Defense Wei Fenghu. My old friend.”

“Yes, my respected Chairman Comrade.”

“Do you want the Central Military Commission’s full authority?”

Wei Fenghu hesitated for a moment before heavily nodding.

“That is correct.”

“You could use that power well. But I must refuse.”

“…Chairman Comrade?”

“When this meeting is over, bring me the orders. I will take both full authority over everything and responsibility for everything.”

For a moment, I wondered why China’s Jongseok was acting like that.

But now I understood. He was declaring that he would shoulder everything himself.

Team Leader Choi, who had been watching the scene beside me, murmured,

“He’s a good leader.”

I quietly shook my head.

“No. To me, you’re the best, Team Leader Choi.”

“Mr. Jin Taekyung…”

“So please raise my Guild settlement percentage.”

“Mr. Jin Taekyung…”

Same words. A completely different feeling.

Team Leader Choi was looking at me with an expression that said, *Of course you’d say that, you bastard*, when he shook his head.

“The Chairman is departing.”

At the secretary’s words, everyone who had been seated stood up. It was the minimum courtesy owed to the head of state.

“I wish you all good fortune.”

The Chairman spoke to everyone present, meeting each person’s eyes in turn. Of course, I was no exception.

Unfortunately, I was the very last one.

“Mr. Jin.”

“…Yes.”

A faint smile touched the corners of the Chairman’s mouth as he looked at me.

“I have very high expectations of you, Mr. Jin. Although this is a contract in which we exchange what we each need, I hope you will prioritize human lives in any situation.”

Was it my imagination, or was his farewell unusually long compared to those he had given everyone else?

Feeling the eyes of the others on me, I nodded.

“Understood.”

“Please be a great source of strength to us.”

The Chairman turned to leave, then suddenly stopped. He tossed out one last remark.

“Welcome.”

“…”

“Then I’ll take my leave.”

After the senior Chinese officials who had been present to see the Chairman off disappeared, I sank into a chair.

*Fuck.*

If I died, the cause of death would be death by humiliation.

Even if a monster killed me, I would have the cause of death recorded as death by humiliation.

*Aagh, aaaaaagh!*

As I screamed in every direction inside my mind, something firmly stepped on my foot.

It was obviously Team Leader Choi, who was sitting beside me.

“Why?”

Team Leader Choi gave a small cough.

“Ahem.”

“What?”

“Ahem. People. People.”

“Oh.”

I looked around and finally realized that a dozen or so men and women of various races were staring at me inside the underground bunker.

Four of them stood out in particular.

*Those people are…*

A Chinese man and woman.

And two Western men, one tinged green and the other blue.

I could feel it simply from meeting their gazes—the enormous mana coiled inside their bodies.

Rather than being surprised, I felt that it was only natural. Anyone who knew the identities of those four people would have thought the same way I did.

*S-rank Hunters.*

People who were news simply by existing. The individuals at the very top among the countless Hunters in the world.

The faces I had grown sick of seeing on television and in commercials were right before my eyes.

And now, one of them stood up and extended a hand to me.

“Nice to meet you. I’m… Ah, do you happen not to know English? I can use translation magic for you.”

I had never expected him to speak to me first.

I shook his offered hand with a dazed expression and answered,

“No, it’s fine.”

“Oh, listen to that pronunciation. I’d believe you were American.”

He was a middle-aged Black man, a giant well over two meters tall. His blue eyes glinted as he asked,

“You seem to know who I am. Don’t you?”

How could I not?

I felt even more nervous than I had when I met Chairman Shao Yang.

“Of course, Magic Johnson.”

The title of Archmage, bestowed on only three people in the entire world.

Magic Johnson, the Black man standing before me, was a War Mage—the most combat-focused of those Archmages.

*I’m actually talking to Magic Johnson. I never thought I’d live to see the day.*

As I thought that coming here had been the right choice in more ways than one, the world’s greatest War Mage smiled broadly and spoke to me.

“Haha. Thank you for recognizing me. Actually, I’ve known about you for a while.”

“Y-You know me?”

“Of course. Even my youngest daughter, who started elementary school this year, knows Lord Fuck.”

“…”

*Just how far has that damn nickname spread?*

I wondered what Lord Fuck would be called in the English-speaking world.

*Fuck Guy? Fuck Man?*

The thought of Magic Johnson’s young youngest daughter knowing me by that name did not make me happy in the slightest.

Apparently, I wasn’t the only one who was displeased.

“What a vulgar nickname. Though I suppose it does suit a little A-rank Hunter like you.”

The Chinese man who had just turned thirty, or perhaps was about to, watched me with his arms folded.

“Isn’t that right, you peninsula bangzi?”[^2]

Team Leader Choi had no time to stop me.

My voice had already spilled out like a prerecorded response.

“What the hell are you talking about, you mainland chink bastard?”

[^1]: *Gukbap* is rice served in hot soup. Here, Taekyung twists Wei Fenghu’s confident reassurance into a joke about “hearty” gukbap.

[^2]: *Bangzi* is a derogatory Chinese term for Koreans; “peninsula” refers to Korea.

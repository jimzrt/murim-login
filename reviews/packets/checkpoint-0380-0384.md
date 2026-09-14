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

## Chapter 374 Expedition

- This branch backfills Chapters 370–373 against the Chapter 65 anchor. Chapters 66–369 have no accepted local English translation here.
- Treat `docs/EXPEDITION_SEED.md` as bounded orientation, not as a substitute for missing translations. Do not read parked Chapters 374–375 while drafting 370–373.
- When the current Korean source conflicts with bridge context, the current source wins. Preserve uncertainty instead of inventing skipped-range backstory.
- After Chapter 373 is committed, run `python tools/expedition.py resume-parked` so the existing 374–375 translations remain the accepted line.

## Checkpoint summary

# Chapters 380–384

## Plot

At Chengdu International Airport, Jin Taekyung and Team Leader Choi survive their burning jet’s crash into the monster army and join Shao Shen’s defense. Taekyung discovers that nearly half the army consists of undead controlled by an unidentified force. The Skeleton Warlord seizes control of roughly two hundred nearby undead, turning them against the living monsters while the Chinese Hunters counterattack.

Three incomplete Liches, former human necromancers serving an Arch Lich, command the assault. They strengthen their army by harvesting death energy from soldiers and attempt to create increasingly powerful undead, but Taekyung reaches them before they can complete a Death Knight. He destroys all three, using Scorching Yang Qi against one and ordering the Skeleton Warlord to consume the other two. The Unexpected Assault Quest is completed, granting Taekyung the **Undead Hunter** Title, EXP, Fame, and a level up; the Skeleton Warlord becomes substantially stronger.

Taekyung is taken to Mount Qingcheng, where Senior General Wei Penghu explains that the monster wave began in Gaoping District, Nanchong City, after a sudden mana surge. Lei Fei, China’s previously undisclosed S-rank Hunter and commander of the Sichuan Public Security Armed Forces, disappeared with his Hunters while investigating the incident. Wei, who raised Lei Fei as his own son, asks Taekyung to bring him back if he is found. Taekyung agrees without promising that Lei Fei is alive.

At the underground operations headquarters, state chairman Xiao Yang personally asks Taekyung and the assembled international Hunters to save as many people as possible. He retains overall authority rather than granting Wei Penghu unrestricted control. The bunker contains several S-rank Hunters, including the Archmage and War Mage Magic Johnson, who recognizes Taekyung’s Sibeol-jwa nickname. A young Chinese Hunter insults Taekyung as a peninsula bangzi; Taekyung answers with an equally offensive insult.

## Continuity

- Taekyung and Team Leader Choi are cooperating with China to stop the Sichuan disaster and locate Lei Fei and the missing Sichuan Hunters.
- Chengdu International Airport’s monster army was controlled by three incomplete Arch Liches, all destroyed by Taekyung and the Skeleton Warlord.
- The three Arch Liches served an Arch Lich and swore upon the River of Death that their account of their origins and orders was truthful; the relationship between them and the earlier Lich remains unresolved.
- The Skeleton Warlord absorbed substantial death energy and is much stronger, but the full extent and persistence of the increase remain unknown.
- The monster wave began in Gaoping District, Nanchong City, following a sudden mana surge. Magical interference disrupts communications throughout wartime Sichuan.
- Lei Fei is Wei Penghu’s only nephew and was raised by Wei as his son. Lei Fei’s fate and the fate of his missing unit remain unresolved.
- Wei Penghu is a Senior General and Minister of Defense at the Central Military Commission. Xiao Yang is its Chairman, the Communist Party’s General Secretary, and the state chairman of the People’s Republic of China.
- Xiao Yang has personally tasked the Hunters with minimizing casualties while retaining full responsibility and authority.
- Magic Johnson is an S-rank Hunter, one of the world’s three Archmages, and a combat-specialized War Mage. At least four other unnamed international S-rank Hunters are present.
- Taekyung’s exact post-level-up Level, Fame, Titles, martial-art stages, and unassigned points remain unstated.
- Dark Heaven, the hidden transport formation, the Sichuan Tang Clan’s relocation, Mungyeong’s response to the coming war, the port boy’s identity, and Ae-hyang’s superior remain unresolved.
- The monster wave’s larger plan, the Arch Lich’s identity, and the reason for the mana surge remain unresolved.
- The insult exchange between Taekyung and the young Chinese Hunter remains an immediate interpersonal tension.

## Translation Decisions

- Preserve **Undead Hunter**, **Sibeol-jwa**, **Teacher Jin**, **Lei Fei**, **Wei Penghu**, **Gaoping District**, **Nanchong City**, **Mount Qingcheng**, **Magic Johnson**, **Archmage**, and **War Mage**.
- Render **중앙군사위원회** as **Central Military Commission**, **국가 주석** as **state chairman**, and **총서기** as **General Secretary**.
- Preserve the **Jongseok** mishearing joke for General Secretary and the official forms **Comrade Minister of Defense** and **Comrade Chairman**.
- Render **반도의 빵즈** as **peninsula bangzi**, retaining a footnote identifying *bangzi* as a derogatory Chinese slur for Koreans.
- Preserve Taekyung’s Sibeol-jwa nickname, self-mocking voice, death-by-humiliation joke, and the deliberately offensive insult exchange.

## Durable state

{
  "active_continuity": [
    "Jin Taekyung is a Supreme Peak martial artist; his exact current level, Fame, complete Titles, martial-art stages, and unassigned points remain unstated.",
    "Taekyung has returned to the modern world and is working with Chinese authorities to stop the monster disaster while seeking Lei Fei and the missing Sichuan Hunters.",
    "Sichuan Province remains in a wartime state, and the current monster wave began in Gaoping District, Nanchong City, after a sudden mana surge.",
    "Wei Penghu is a Senior General and Minister of Defense at the Central Military Commission, and he raised his missing nephew Lei Fei as his own son.",
    "Wei Penghu's jet has reached the temporary operations headquarters in a deep bunker beneath Mount Qingcheng.",
    "Xiao Yang is Chairman of the Central Military Commission of the Chinese Communist Party, General Secretary, and state chairman of the People's Republic of China.",
    "Xiao Yang has asked the assembled Hunters to prioritize human lives and stop the disaster, while taking personal responsibility and retaining full authority.",
    "Team Leader Choi accompanies Taekyung and continues to trust him during the Chinese crisis.",
    "Magic Johnson is an S-rank Hunter, one of three Archmages worldwide, and a combat-specialized War Mage.",
    "Magic Johnson recognizes Taekyung's Sibeol-jwa nickname, which is known even to his youngest daughter.",
    "At least four additional S-rank Hunters are gathered in the bunker: one Chinese man, one Chinese woman, and two Western men.",
    "An unnamed young Chinese Hunter has insulted Taekyung with the slur peninsula bangzi, and Taekyung has answered with an offensive insult toward mainland Chinese people.",
    "The Chengdu International Airport attack involved an undead army controlled by three incomplete Arch Liches, all of whom Taekyung destroyed.",
    "The Skeleton Warlord absorbed the death energy of the remaining two Arch Liches and became much stronger, but the persistence and full extent of that increase remain unknown.",
    "Dark Heaven's agents, purpose, and connection to the hidden transport formation remain unresolved.",
    "The Sichuan Tang Clan was devastated by Dark Heaven, owes Taekyung's group a debt, and is considering relocation.",
    "Mungyeong remains torn between Dongbong's warning about an approaching war and his stated wish to leave Murim affairs behind.",
    "Ae-hyang appears to serve an unidentified superior after a sinister red light entered her eyes, and the Sichuan Governor's false memorial remains unresolved.",
    "Lei Fei's fate and the fate of the Public Security Armed Forces Hunters who disappeared with him remain unresolved."
  ],
  "continuity_sources": [
    384
  ],
  "open_questions": [
    "The outcome of Taekyung's spar with Jin Mukyung remains unresolved.",
    "Dark Heaven's larger purpose, its reason for sparing Taekyung, and the origin and function of the hidden transport formation remain unresolved.",
    "The Sichuan Tang Clan's relocation decision and destination, along with the timing and outcome of the Samgoe escort to Henan, remain unresolved.",
    "The request Dongbong wants to make of Taekyung, Mungyeong's eventual response to the coming war, and the identity and fate of the boy from the Chengdu port remain unresolved.",
    "Ae-hyang's superior and the consequences of the Sichuan Governor's false memorial remain unresolved.",
    "The relationship between the Lich and the Arch Lich, the full extent of the Skeleton Warlord's increased power, and the monster wave's larger plan remain unresolved.",
    "Lei Fei's fate and the fate of the missing Sichuan Hunters remain unresolved.",
    "The identities and roles of the other international S-rank Hunters gathered at Mount Qingcheng remain unresolved."
  ],
  "safe_through": 384,
  "temporary_decisions": [
    "Use the current Korean source as authoritative; the skipped range is not accepted English continuity.",
    "Render Zhonghua as Zhonghua and preserve the Jongseok mishearing joke for 총서기.",
    "Render Xiao Yang's offices as Chairman of the Central Military Commission, General Secretary, and state chairman.",
    "Render 대마법사 as Archmage and 워 메이지 as War Mage.",
    "Retain Teacher Jin for 진 선생 and Comrade Chairman for 주석 동지.",
    "Render 반도의 빵즈 as peninsula bangzi and retain the derogatory-slur footnote.",
    "Preserve Taekyung's conversational, self-mocking first-person voice and the source's offensive insult exchange.",
    "Render 수치사 as death by humiliation in Taekyung's internal joke."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 380

# Chapter 380

Shao Shen realized something for the first time.

Krrrrrrrummble!

If you ever witnessed an airplane with both wings engulfed in flames hurtling toward the ground, you would be seized by a terror that transcended species.

- Gaaaaaaaah!

The ogres reputed to be so fearsome screamed. The trolls screamed, too.

- Roooooar!

Even ghouls, reputed to be the slowest of all undead monsters, ran until the soles of their feet sweated.

- Sssssss!

“U-Urgh, uhhh, uhhhhh…”

The monsters that could scream were the lucky ones.

Most of them—including Shao Shen—could only stare at the airplane charging toward the ground, frozen like statues.

*I need to run…*

Neither his hands nor his feet would move.

More importantly, Shao Shen and the Hunters of the Public Security Armed Forces had been surrounded in the middle of the battlefield. They had not even been given a chance to escape.

*Is this really the end?*

The same thought flashed through everyone’s mind at that very moment.

Rrrrrrrumble!

With an earsplitting roar, the airplane’s enormous fuselage swept across the battlefield.

That earth-shaking collision began at the very rear of the monster army, which was scattering like a swarm of ants.

Krrrrrunch! Crack!

The massive hunk of steel, weighing dozens of tons, smashed and burst through everything in its path.

Green blood spurted from the monsters like fountains, and limbs of every size flew in all directions.

*W-What the hell is this…?*

No matter how formidable a monster’s physical defenses were, they had their limits. Nothing could stop the airplane now that it had become a monster blender.

- Roooo…

- Kiiiiiiik!

Krrrrrunch!

The eerie sounds of flesh being torn apart swallowed the monsters’ screams. It was a hellish scene unlike anything Shao Shen had ever seen or heard.

As Shao Shen and the other Hunters stared blankly at the unimaginable sight, someone’s crazed shout pierced their ears.

“Monsters! Ram! Kill!”

“……!”

Despite the chaos, the Hunters of the Public Security Armed Forces heard their native language loud and clear. The word *reinforcements* flashed through their minds, and Shao Shen was stunned.

*An incredible powerhouse!*

The voice carried immense mana. It had to belong to an S-rank Hunter.

“Go! Go, airplane!”

“……”

And definitely a slightly insane S-rank Hunter.

*To think he’d use a method those island bastards employed back in World War II. Had he not considered that his own allies might die too?*

*He seemed to have been dispatched by the Central Military Commission… But did our country even have an S-rank Hunter like that?*

The question suddenly occurred to Shao Shen. But it would soon have nothing to do with him.

The massive hunk of steel that had ground its way through half the battlefield was charging straight toward him and the Hunters.

- S-Sssss!

“Run!”

When it came to the struggle for survival, there was no distinction between friend and foe.

Shao Shen thrust his dagger at a monster hurling itself toward him, heedless of the human right in front of it.

Shunk!

- Grrrk.

The dead monster’s body collapsed toward Shao Shen.

Monsters surged in from every direction, leaving him unable to move even a single step. Feeling the immense weight bearing down on him, Shao Shen shouted.

“The battle isn’t over! Fight until the very end!”

He was right. The battle was not over yet. A Hunter had to keep killing monsters until the final moment, when his own breath ran out.

The Hunters who heard Shao Shen’s shout gritted their teeth and swung their weapons.

*This is enough.*

With lightning-fast skill, Shao Shen drove his dagger into the back of a fleeing ogre’s head, then drew a deep breath.

The airplane’s enormous fuselage was already only about twenty meters away.

Its speed had decreased considerably since the beginning, but with everyone trapped in place, evading it seemed impossible.

*I have no regrets.*

If he died fighting for the people as a proud Hunter of Zhonghua, that was enough.

Shao Shen closed his eyes as screams rained down from every direction.

“Hup.”

Krrrrrunch! Splaash!

Drenched in a sticky liquid that he assumed was blood, Shao Shen thought:

*…Hup?*

*Shouldn’t it normally be “Aagh”?*

The strange sound was hardly an appropriate death cry. Shao Shen cautiously lifted his eyelids.

At last, he saw it.

The airplane had stopped a few steps away, and two men stood beside it, chatting casually.

“All right, we’ve arrived. It might explode, so get everyone off quickly.”

“…Mr. Jin Taekyung. Everyone has passed out.”

“Really? How pathetic.”

“…They would have died if not for the barrier magic.”

“Then carry them out, Team Leader Choi. Oh, right. Is that bastard who called us *bangzi*[^1] earlier alive, too?”

“Yes. He’s, uh… alive, at least.”

“Then keep a close eye on him. I’m going to give him hell for a long time when we get back.”

“…I’ll do my best.”

Shao Shen could not make sense of the situation at all.

Who, when, where, what, how. Why. Even the five Ws and one H could not organize a scene this bizarre.

*How did the airplane stop so suddenly, and who are those people? So they weren’t Hunters sent by the Central Military Commission?*

The two men were even speaking to each other in a different language.

Shao Shen could not understand the words of the refined-looking man who resembled a young master, but he knew what country the language belonged to.

Their longtime neighbor.

Korea.

*Wait. If he’s Korean…!*

Shao Shen hurriedly wiped the sticky blood from around his eyes. Only then did he recognize one of the men.

A muscular young man who stood a full head taller than everyone else.

The man he had only ever seen on television—his idol—was standing right in front of him.

“E-Excuse me. Are you Teacher Jin from Korea?”

“Huh?”

The young man, Jin Taekyung, tilted his head as he looked at Shao Shen.

“I’m not a teacher.”

“Then… Sibeol-jwa…”[^2]

“…Sibeol. What?”

That was him!

Relief and hope swept through Shao Shen, making his entire body tremble.

[^1]: *Bangzi* (棒子) is a derogatory Chinese slur for Koreans.

[^2]: *Sibeol* is a Korean profanity, while *-jwa* is a playful suffix used in a nickname.

* * *

*How does a Chinese guy even know about Sibeol-jwa?*

Articles about me had briefly made a splash in the foreign press, but I had never expected my nickname to spread along with them.

*Sibeol-jwa, whose name makes the five oceans and six continents tremble.*

If I ever went to the United States, maybe some huge Yankee bros would come up to me with beer bottles in hand and greet me like an old friend.

*Hey, you. Sibeol-jwa?*

*I’m fine, thank you. Sibeol.*

What kind of deranged bastards came up with a nickname like this?

Anyway…

“It’s a complete mess.”

That was my brief assessment as I looked around.

Team Leader Choi, who had strung the unconscious flight attendants together like dried fish, and the Skeleton Warlord I had shoved into my inventory both answered.

“It’s a horrifying sight.”

- Vile human, I like this place. It feels familiar and strangely comforting.

“……”

There was no need to say more. A named undead monster who could be called death itself found the scene satisfying.

“We just got here, and we’re already being thrown into actual combat.”

As if responding to my complaint, a System notification rang out.

Ding.

> **System**
>
> - An unexpected Quest, **Unexpected Assault**, has been generated.

*So this is why they said they were paying me so much.*

I clicked my tongue to myself and spoke.

“Team Leader Choi, protect the civilians first. After that, fight as you see fit. Don’t overdo it.”

“Yes. I was already planning to.”

Team Leader Choi was a smart man. Learning the Jin Family’s Cultivation Technique had made him incomparably stronger than before, but he was not the sort to show off.

“And you, young man over there.”

“Y-Yes, Teacher Jin.”

*Teacher, my ass.*

I looked the young man up and down as he answered so promptly.

His face was young, but he was obviously a Hunter. And a powerful one, at that—around A-rank, judging by appearances. Unlike the Hunters around him, who wore identical armor as if they had been stamped out in a factory, he also had a red insignia on his shoulder.

“You look like you hold a decent rank, so take care of your men. Let’s save as many people as we can.”

“Y-Yes?”

“This is only the beginning.”

As I answered, I thrust out my fist.

KABOOM!

Streams of Scorching Yang Qi shot toward the monsters standing there in a daze.

Once the wave of searing heat had swept past, only dozens of monster corpses remained.

“What are you all staring at? Did someone press the pause button?”

“……!”

- ……!

My words served as the signal.

The silence pressing down on the battlefield shattered.

- Grrrrrrrr!

“K-Kill them! Hold back those monsters!”

Humans and monsters. Monsters and humans.

A battle of killing and being killed began. I pulled White Flame from where it was embedded deep in the ground and swung it.

Swish!

Forget waters so crowded they were half water and half fish—monsters were swarming everywhere.

A crescent of sword qi extended from the spearhead and grazed a tightly packed mob of monsters.

Ding.

> **System**
>
> - Defeated **Lv. 15 Undead Goblin**!
>
> - Defeated **Lv. 78 Undead Lycanthrope**!
>
> - Defeated **Lv. 93 Dullahan**!
>
> - Defeated **Lv. 30 Skeleton**!
>
> - …
>
> - The Level gap is significant. Gained negligible EXP!

System notifications announcing monster kills and EXP gains rang out without end.

Normally, I would have let them go in one ear and out the other, or simply ignored them.

But this time, they gave me an important clue.

“Don’t tell me these guys are…”

- Ah, that’s right, vile human! What a powerful undead army!

The Skeleton Warlord’s delighted shout was enough to turn my suspicion into certainty.

*No wonder something felt off.*

I had already been wondering why I could not sense any life force from them.

A sizeable number of monsters were still alive, but roughly half or more of them were undead. All told, it was an army of close to two thousand monsters.

“And undead monsters are…”

The Skeleton Warlord shouted excitedly.

- Beautiful! Magnificent! Valiant!

Crash!

I cut down five monsters and muttered.

“Do you want to disappear like that guy just did? Beautifully, magnificently, and valiantly?”

- ……I misspoke. My apologies, vile human.

The Skeleton Warlord had briefly forgotten his own situation. He hurriedly added:

- Wait. Then they must be under someone’s control!

I thought so, too.

But there was one thing I still could not be certain about…

“The Lich. Did that bastard come out personally?”

- Hmm. If you mean the Lich from that holographic video you showed me last time, then probably not.

As I listened to the Skeleton Warlord’s answer, I took half a step forward.

Boom!

A massive iron club passed dangerously close to my shoulder and smashed into the ground. This was an ordinary ogre, and I could still sense its life force.

- Guwooooo![^3]

“Yeah, I’ll roast you.”

[^3]: The ogre’s roar, *guwo*, is also Korean for “roast it.”

Boom!

The Flame Divine Palm struck the ogre in the chest, and black-green blood erupted from all seven of its orifices.

As I passed its collapsing bulk, I slashed White Flame diagonally downward.

Whoooosh! Slash!

Space split apart, and the bodies of the monsters caught between the two halves were sliced to pieces.

Leaving behind a Chinese Hunter who stared blankly at me, drenched in blood and bodily fluids, I clenched my fist.

Whoooooom.

A surge of extreme heat raced toward my fist, then shot forward.

KABOOM!

Flame-Annihilating Divine Fist.

A massive pillar of fire swallowed the monsters.

Along with the foul smell of burning flesh, the few monsters that had somehow survived shrieked in agony.

The attack had enough destructive power to make both monsters and Hunters forget to fight for a moment.

The Skeleton Warlord stammered.

- V-Vile human. You have become even more of a monster.

“It feels weird being called a monster by a monster. But if it’s not the Lich, then what bastard is causing all this chaos?”

- This commander does not know, either. But I can guarantee one thing.

“Guarantee? What?”

- That bastard’s control of the undead is a notch below this commander’s. Hahaha! My army! This commander misses you!

“……”

*Should I kill this bastard or let him live?*

As I was wondering, a thought suddenly flashed through my mind, and I stopped dead.

“Hey. What did you just say?”

- Hahahaha! Did you feel this commander’s majesty, vile human?

“Disappear or talk.”

- ……I will talk. But what are you asking?

“That thing you said about controlling the undead.”

- Isn’t it obvious? This commander is a Skeleton Warlord. Compared to them, naturally… Huh?

A brief silence followed.

He must have had the same thought I did. I swallowed hard, then casually broached the subject.

“Try it. That thing.”

- ……

“Are you going to do it, or do you want to disappear?”

The Skeleton Warlord opened his mouth.

- Grow, grow, skeletons, skeletons…

At that moment, the undead monsters locked in fierce combat abruptly stopped moving.

*…So it works.*
## Chapter artifact 381

# Chapter 381

Swoooosh.

I couldn’t see it. But I could feel it. Centered on me—or rather, flowing from the Skeleton Warlord inside the subspace called my inventory—a sticky energy spread in every direction.

The change was instantaneous.

- Krrik?

- Guwo?

The movements of the utterly savage monsters abruptly stopped.

Orcs, trolls, goblins, lycanthropes, every kind of monster I had only ever seen in monster encyclopedias, and even the fallen Hunters.

They had just one thing in common: they had already died once and been resurrected as undead.

Gulp.

I swallowed dryly and muttered, “It actually worked.”

- Wow. It really worked.

“……?”

- ……?

*Wait, what did you just say?*

My brain froze for a moment. Then I whispered, “What kind of boneheaded nonsense was that? Didn’t you do it because you knew it would work?”

The Skeleton Warlord answered sheepishly.

- The truth is… even this commander did not expect it to work so easily.

“You said your control was much stronger.”

- Ah, that? I only said it in a fit of anger.

“What?”

- My pride would not let me sit there doing nothing…

“……”

*Is this guy completely insane?*

It was absurd, but the result was undeniable.

When all the undead monsters within a radius of several dozen meters stopped moving at once, the fierce battle raging around us briefly fell into a lull.

“Th-The monsters have stopped moving!”

“What the hell is going on?”

“Don’t let your guard down! Some of them are still moving!”

As someone shouted, it was still too soon to relax.

The Skeleton Warlord had only taken control of some of the nearby undead monsters. Those farther away, as well as the ordinary monsters that were not undead, were the exception.

- Roooooar!

- Kreeeek!

“Haaaaah!”

Clang-clang-clang! Stab-stab!

The uncontrolled monsters were bewildered by the sudden change in their own kind, but only for a moment. Once they began rampaging again, the battle resumed.

The two sides’ numbers had been incomparable. From this moment on, though, that was about to change.

I shouted in a hushed voice.

“Go, Warlordmon!”

Warlordmon—no, the Skeleton Warlord—flared up and shouted.

- You vile human! Do not call this commander that!

“Then how about Warlordmon Who’s Dying to Be Annihilated?”

- ……Damn it.

Despite being a skeleton that couldn’t even breathe, he let out a deep sigh before chanting a spell.

- Fight, skeleton skeleton.

That bastard had clearly gotten hooked on “skeleton skeleton.” The incantation wasn’t even funny, but its effect was undeniable.

- Guwo?

At the Skeleton Warlord’s command, the eyes of the undead monsters that had been staring blankly into space filled with savagery.

Then, in the next moment—

Crunch!

An undead ogre’s iron club crushed a troll’s skull.

That was the beginning.

The undead monsters who now served a new master charged at their former allies.

- Guwoooooo!

- K-Kreeek?

Crack! Slash! Stab-stab-stab!

It was an unexpected ambush from behind by their own allies.

One flank of the monster army surrounding the Chinese Hunters collapsed helplessly.

- Kreeeeeeek!

“What the hell?!”

“Why are they suddenly…?”

The monsters betrayed by their own kind weren’t the only ones thrown into confusion.

The Chinese Hunters were just as bewildered by the sudden turn of events. I shouted at the young Hunter who had been darting across the front line, swinging his spear all over the battlefield.

“Shao Shen!”

“T-Teacher Jin?”

His widened eyes turned toward me.

“How do you know my name?”

I had just checked his Level window using Qi Sense, but that wasn’t important right now.

“What are you doing? Why haven’t you switched to an all-out attack?”

“But what exactly is happening…?”

“Are you really that curious right now? Do you want to grab an undead monster and make it explain why it’s helping us according to the five Ws and one H?”

“Ah, no, sir!”

“Then what should we do now?”

Shao Shen snapped back to his senses and raised his spear high.

“Attack formation! All Public Security Armed Forces personnel, attack everything except the undead monsters from this moment on!”

“Yes, sir!”

*An excellent example of sound judgment.*

With one unified shout, the momentum of the five hundred or so Hunters who had been cornered changed.

“Kill them!”

“Avenge our fallen comrades!”

Swish-swish-swish! Slash!

A lycanthrope charged at a Hunter who had just severed an orc’s neck.

Its jaws opened, yellow fangs poised to tear out the Hunter’s throat—but a massive fist slammed into its maw.

Crunch!

- Grrrrrrr!

The ogre that had crushed the lycanthrope’s skull let out a savage roar.

At that moment, the sharp claws of a griffin diving toward the ogre flashed above its head.

- Screeeeeech!

The griffin shrieked. Its claws, charged with the mana of an A-rank monster, were about to rake across the ogre’s eyes when—

“Ice Ball!”

“Lightning Bolt!”

The griffin convulsed from the electric shock in midair after being struck by the spells of the ranged Hunters waiting nearby.

Right then, a figure launched himself upward after stepping on a troll’s shoulder and swung his weapon at the griffin.

“Specially made by J Company, widely regarded as one of Germany’s finest weapon workshops…!”

Slash!

A clean, no-frills strike split the griffin’s head in two.

Team Leader Choi landed gracefully and gazed at the transparent blade, not a single drop of blood staining it. He smiled with satisfaction.

“The longsword I won at auction for 5.2 billion won. It really was worth the price.”

“……”

*He looks like an idiot, but he’s cool.*

*He’s cool, but he looks like an idiot.*

The Skeleton Warlord watched the scene, then asked dubiously:

- Vile human, did you say that man was your superior?

“Technically, yes, in terms of internal Guild positions, but…”

- He looked fairly intelligent for a human, yet what a bizarre human he is. He truly suits you as a superior.

“Raise your hand if you’re a Skeleton Warlord who wants to be annihilated for running his mouth.”

After a brief silence, the Skeleton Warlord answered by chanting another spell.

- Grow, skeleton skeleton!

After three years at a village school, even a dog could recite poetry. By now, he did it well without being told.

Tuk. Tuk-tuk-tuk.

The griffin killed by Team Leader Choi, along with the monsters brought down by the combined attacks of the Hunters and the undead, gained new life and hauled their dead bodies back to their feet.

There were two hundred of them.

The range also seemed to have grown even wider compared to his first attempt. Even the undead monsters far away had come under the Skeleton Warlord’s control and begun attacking their former allies.

“Wow. You were this strong?”

- Wow. Was this commander really this strong?

“……”

- ……Actually, this commander was not this strong before. But for some reason, an incredible amount of mana is surging through me now that I am here!

“Uh-huh. Good for you.”

I gave up trying to understand this bizarre named monster.

The result was all that mattered. Trying to figure it out right now would only give me a headache.

- Give me a larger legion! More! More!

I couldn’t see him because he was inside my inventory, but I was certain his skull—which had nothing left but bones—was trembling with excitement.

I sighed and tightened my grip on my spear.

“I was already planning to.”

- Is there a way?

“There is.”

The method for increasing the number of undead was simple.

“You just have to kill every last one of them.”

- Krahahaha! You truly are a vile and brainless human!

*Arrogant bastard.*

Still, this time, I couldn’t help agreeing with part of what he said.

As the Skeleton Warlord’s mad laughter echoed through my head, I took a step forward.

*Flamefire Path.*

Whoooooosh!

A path of flame opened along my footsteps.

* * *

Black robes. Staffs hung with dangling skulls.

The places where their pupils should have been were empty, and pieces of flesh that had not yet rotted still clung to their bodies.

The three beings looked as though they had stepped out of a nightmare. They exchanged thoughts with one another.

- We have a problem.

- The undead monsters are breaking free of our control. They are helping the humans and attacking the legion.

- Why?

They were not asking how the undead had escaped their control.

The three beings already knew the answer to that question.

- A higher undead. One more powerful than us.

All monsters had a hierarchy, but the undead in particular were ruled absolutely by strength.

If control had been taken away as it had now, it was undoubtedly the work of a superior being.

- But…

- How is that possible?

None of the three beings could answer.

How could an existence more powerful than them be here? How could it steal control of the undead and use them to help the humans?

- Could it be *Him*?

- Don’t be ridiculous. Have you forgotten the order He gave us when He sent us here?

- Kill the humans. Create more undead and a larger legion, then kill more and more humans.

The three beings fell into momentary confusion as they recalled the order.

If it was not Him—the Arch Lich—then who could possibly surpass their control?

- Was there a necromancer among the humans?

- I sensed nothing.

- Humans reject and despise death. It cannot be. Even if there were one, they would be no match for us.

The reason unmistakable hostility could be felt in their thoughts was that they, too, had once been necromancers who had borne the full weight of human rejection and contempt.

But that had been in the distant past, in another dimension.

They had drifted across the boundless sea of death until they encountered a ferryman named the Arch Lich. They gained new power and were now trying to become the Liches they had long yearned to be.

However…

- What a shame.

- If only the transformation had been completed. If only there had been more death in this land.

- Then we would not have lost control, either.

The three beings could not hide their regret.

They had been great necromancers in life, but they had not yet fully transformed into Liches.

They had been reborn by borrowing the bodies of dead mages, but one week was far too short to absorb the death energy needed to transform into Liches.

- That is why He sent the three of us.

- He will be disappointed if this fails.

- He may even take back the power He gave us.

That was what the three beings feared most.

They had to overcome this crisis somehow if they wanted to earn the Arch Lich’s trust—even if it meant expending a tremendous amount of power.

- It cannot be helped.

- Are you suggesting we join forces?

- Yes. If the three of us combine our power, even this unidentified higher undead will no longer be able to wrest control from us.

- Hmm. Very well.

- Do you agree?

- I agree.

The three beings, who had been competing for the Arch Lich’s favor, finally found common ground.

Without hesitation, they began chanting a necromantic spell.

- Barensia. Madrit.[^1]

- Baielrn. Munich.

- Stoh. Siri.

[^1]: The pseudo-incantation mangles the names Valencia, Madrid, Bayern Munich, and Stoke City.

The energy of death flowed from the three beings and spread through the air.

Green grass turned black. Soldiers of the People’s Liberation Army caught within its range clutched their throats and collapsed.

“Urk!”

“Ghhurk!”

Ssshhhhhh.

The death energy flowing from the bodies of the humans who had died with those final cries seeped into every inch of the monsters.

- Kyaaaaaaa!

- Grrrrrrr!

The air shook beneath the powerful mana carried in their savage cries. Their strength was beyond comparison with that of ordinary monsters.

Only after sensing their strengthened control and the increased power of the monsters under their command did the three beings stop chanting.

- Kikikikikik.

- It worked.

- We expended an enormous amount of power, but… this is more than enough.

The three beings were smiling with satisfaction at their strengthened legion when—

BOOM!

In the distance, a monster’s limbs went flying with a thunderous explosion.

The three beings looked toward the flames surging into the sky.

- There appears to be a fire mage. Not bad.

- It is still only a human. Deploy a large number of Skeleton Mages.

- A good idea.

A short while later, flames surged into the sky once again.

The three beings looked at one another.

- Just now. What was that?

- Our control was severed. It was not stolen.

- It annihilated them? Impressive.

- But is that really a mage? Its movements seem too fast…

- Let’s deploy the ogre unit.

- I’ll see your ogres and raise you Dullahans.

- Dullahans as well? Then who will guard us?

- He has a point. Dullahans are excessive. Strengthened ogres will be enough.

- That is true.

Three minutes later, a grim atmosphere hung over the three beings’ skulls.

- It was severed.

- Again?

- I told you we should send the Dullahans.

- What the hell is that thing? It does not seem to be a mage.

- I said we should send the Dullahans first!

- Th-Then let us do that.

Watching the twenty or so Dullahans they had selected as an escort troop rush off as a group, the three beings furtively began searching for another point of agreement.

- Hmm. It will not happen, but just in case…

- I had a similar thought.

- A Death Knight… should we make one?

- We have already expended too much power. A Death Knight, too? We do not have suitable materials, and it would take a long time.

- For now, we can pick the most useful one and make a Death Knight out of it. If the three of us combine our power, it is possible.

- Th-Then should we at least try?

But the three beings’ plan to create a Death Knight was shattered into pieces before even ten minutes had passed.

Fwoosh! Kaaaa-boom!

Even their bodies made of nothing but bones could feel the scorching heat.

“Fucking bastards. There are a shitload of them.”

Crack-crack-crack!

The three beings saw the figure tearing through the monster legion with a spear engulfed in hellfire and hurriedly began chanting.

Their slow voices had become as fast as rap.

- Omnehasoyu!

- Yenwigajike!

But before the spell could be completed, the young human—whose identity as either a fire mage or a warrior was impossible to determine—had already arrived right in front of them.

“Uh, nice to meet you.”

- O-Omnehasoyu!

- Ye-Yenwigajike!

The young man, Jin Taekyung, cocked his head to one side.

“Hello. *Entertainment Weekly*?[^2] Are you idiots?”

[^2]: The incantations sound like mangled versions of *annyeonghaseyo* (“hello”) and *Yeonye-ga Junggye*, the Korean title of the TV program *Entertainment Weekly*.
## Chapter artifact 382

# Chapter 382

Strike the head, and the body falls.

Once I captured the three who looked like leaders, the undead they had been controlling stopped moving like clockwork dolls. Deprived of its command, the monster army scattered and collapsed, with some dying and others fleeing.

“Arch Lich?”

At my question, the three kneeling creatures nodded.

I wasn’t sure whether I could call things that were already dead and reduced to bones “creatures,” but whatever.

I stroked each of the three skulls in turn and continued.

“When someone speaks to you, you’re supposed to answer. Are you throwing your weight around just because you’re dead?”

The answer came flying out before I had even finished speaking.

- Yes. Yes. It is indeed the Arch Lich.

- What the great human heard is correct.

- That is so.

“Hmm. An Arch Lich. Never heard of that monster before… But which one of you just answered me informally?”

- That one!

- How dare he address the great human that way!

Swish! Swish!

The skeletal fingers pointed at one of them.

His comrades’ lightning-fast betrayal made the accused skull tremble.

- No! This is vile slander!

“…Doesn’t sound like slander to me.”

If you’re going to lie, at least put on a respectful tone.

I casually checked my surroundings, then pulled *it* out of my inventory.

“Boney. Snack time.”

A skull with a strange black sheen. Flames flickered inside its empty eye sockets.

- …Boney? You might as well go back to calling me Warlordmon.

“Why? You’re a skeleton, so Boney. Perfect fit.”

- To think you would insult this commander like this!

“What? If you don’t like it, forget it.”

I was about to put him back in my inventory when the Skeleton Warlord shouted furiously.

- I will gladly eat it!

“What an honest little thing.”

An honest little thing deserved a reward. A bad liar deserved punishment.

“Here. Have a taste.”

- Thank you, slightly less wicked human. But how much should I eat…?

“Just a little, like before.”

- Hmm. I want to eat more. But I understand.

Too many snacks would be overdoing it. With a hint of disappointment, the Skeleton Warlord opened his mouth wide toward the trembling creature.

- Come here.

- E-Eek! No!

- Yes!

The change began with the Skeleton Warlord’s firm declaration.

Whoooooosh!

It was fascinating no matter how many times I saw it.

Like it was being sucked up by a vacuum cleaner, black mist began flowing out of the kneeling creature’s body and being absorbed by the Skeleton Warlord.

- Gaaaaaah!

The change didn’t end there.

As more of the black mist—the substance the Skeleton Warlord called death energy—flowed out, the creature’s complexion, or rather its bones, gradually turned whiter and whiter.

Meanwhile, the Skeleton Warlord’s black sheen grew deeper and darker.

- S-Stop!

- Hehehe. Such delicious death energy.

- Noooo!

- This commander shall take it all. Death energyyyy!

Crack!

- Hk!

“Enough with the ‘death energyyyy.’ Where did you learn that weird crap?”

- …Are you really one to talk?

“Anyway, stop eating now.”

- Why?!

“You’ll get fat.”

The Skeleton Warlord was struck speechless. I tucked him against my chest and looked at the creature.

Its bones had been dark and grimy when I first saw it. Now they were halfway bleached white. Perhaps because so much death energy had been drained from it, the green light in its eye sockets wavered dangerously.

- Sob… sob…

The other two creatures anxiously clacked their teeth at the sight of their weakened comrade, sucked dry to the bone.

- Ask us anything, great ruler of flame.

- I humbly beseech you. Please accept the loyalty of this lowly being, Orpheus von Maximus Valencia Bayern.

“…Are you undead, or are you bidets?”

They really didn’t want to lose their strength. I appreciated their cooperation, though.

“All right. If there’s anything you haven’t told me, scrape the bottom clean and spill every last detail. But if you start spewing lies…”

- We will tell you everything!

- I humbly beseech you! Please permit this false and lowly being to speak the truth!

- I-I will tell you.

Apparently, none of the three wanted to end up as bone broth. They threw themselves into the interrogation with enthusiasm.

After hearing every detail of what had happened over the past week, from the Arch Lich’s first appearance until now, I deliberately furrowed my brow.

“You’re sure?”

- Yes, we are!

- We swear upon the River of Death!

- Th-There is not a single lie.

As the three creatures vigorously nodded their skulls, the Skeleton Warlord suddenly interrupted.

- It is true.

“Did they pay you off? How can you guarantee that?”

- Because they swore upon the River of Death. It is an absolute promise to beings like us. One that can never be broken.

“Hmm.”

The Skeleton Warlord normally treated everything with all the gravity of a speck of dust. If even he was being this solemn, they probably weren’t lying.

Besides, there was no reason for them to scheme in a situation like this.

“Okay. I’ll believe you.”

- Thank you! Thank you so much!

- Sob, sob! I shall serve you with all my heart, my king!

- I-I will serve the human, too. I swear upon the River of Death that I will never again commit an act like today’s—

Crack!

The last creature faltered before he could finish.

The trembling green light in its eyes shifted between the fist buried in its chest and me.

- Wh-Why?

“Why do you think?”

- I-I swear my loyalty. Upon the River of Death, I swear—

“Too late.”

A voice so cold it seemed to belong to someone else slipped through my lips.

“Too late to undo what you’ve done.”

A great many people had died here today.

Even regular troops armed with firearms and Hunters had been unable to stop them. There was no telling how many civilians had died at the monster army’s hands over the past week.

“I don’t need your loyalty. Especially not from pieces of shit like you.”

The moment I released the Scorching Yang Qi I had drawn up from my dantian—

Fwoosh!

Extreme Yang qi surged from the fist embedded in the creature’s shattered ribs. Blue-white aura, carrying ultra-high heat, coiled around its entire body.

Roooooar!

I saw it.

The green light in its eyes, wavering like a candle in the wind, went out.

I also saw the other two creatures spring to their feet and begin chanting spells.

- Jajeuchawa Eumbado…!

- Bareugan Mahra…!

Whoooong.

A wind of mana swirled around them. Just as the evil spell was about to be completed, I casually tossed out a command.

“Devour them. All of them.”

As though he had been waiting for those exact words, the Skeleton Warlord leaped from inside my clothes and opened his mouth wide.

- Gladly.

- Barsaba… Eeeek!

- N-No!

The monsters’ final cries were filled with the desire to live—or rather, the desire to remain undead.

But contrary to their wishes, the Skeleton Warlord’s suction was stronger and faster than ever.

Whoooooosh! Gulp!

After swallowing an enormous amount of death energy in one bite, the Skeleton Warlord’s skull trembled.

The next moment, the two skeletons, drained of every last trace of energy, collapsed into piles of bone.

Ding. Ding. Ding.

> **System**
>
> - The unexpected Quest, **Unexpected Assault**, has been successfully completed!
>
> - You have routed the monster army! This is truly an outstanding achievement!
>
> - As a Quest Reward, you have acquired the Title **Undead Hunter**!
>
> - You have acquired a considerable amount of EXP and Fame!
>
> - Level Up!

Only once?

In the past, I would easily have leveled up several times. But now that I had reached Level 120, it seemed the EXP requirement had increased.

*It’s not like I did this for the EXP.*

I had only done what needed to be done, but I couldn’t help feeling a little disappointed.

The stronger I became, the more useful I would be in the battles ahead.

*The same goes for him.*

I looked at the Skeleton Warlord.

Perhaps because he had absorbed such a massive amount of death energy, the power I felt from him was incomparable to what I had sensed when we first met.

- Hmm. Hoooooo…

Black mist billowed from the holes in his skull—his nose, ears, eyes, and more.

Purple light blazed in his eyes like torches, and the surface of his skull gleamed with a smooth, inky luster. Then his booming, maniacal laughter rang through my head.

- Krah, hahahahaha!

“Turn down the volume. You’re loud.”

- You vile human. This time, this commander shall express his great gratitude to you.

“You should. Who fed you?”

At my indifferent reply, the Skeleton Warlord flared up.

- Food?! Are you saying this body has become a pet?!

“Something like that. Isn’t it?”

- Do not spout nonsense!

“Really? Boney, come back.”

I held out my hand.

The skull leaped up as though spring-loaded and landed neatly on my palm.

As a reward, I gently scratched the spot between his eyes.

“Good job, Boney. Who’s a pretty boy?”

- …!

The skull trembled violently.

- H-How can this be?! How can this commander possibly… to a mere human?!

“Your mouth says no, but your body is honest.”

- I am the master of the Black Forest and commander of the great undead legion. Do not humiliate this body!

“A commander who’s only a head?”

- What?! This paltry body is nothing! If I expend death energy, I can restore it as many times as I wish!

“Really? Then why haven’t you restored it yet?”

- …Because some crazy human would just smash it again anyway.

“Oh, correct.”

Grind.

The Skeleton Warlord had no teeth, so he ground his bone joints instead. The light in his eye sockets narrowed.

- Why, vile human?

“What?”

- You must have an ulterior motive for giving me food—or rather, granting me such great power. You clearly have some sinister intention. Tell me the truth!

I thought for a moment before answering.

“Hmm. Because you’re a fucking weakling.”

- Huh?

“You can’t beat me anyway. If I’m going to drag you around, it’s easier to make use of a stronger, more useful fucking weakling, isn’t it?”

- …!

“Now get back inside. People are coming.”

I put the creature, frozen with shock, back into my inventory and stood up.

The airport duty-free corridor would normally have been packed with employees and passengers. Now it was empty and dark, and three people were walking toward me through the gloom.

Two of them were familiar faces.

“Mr. Jin Taekyung.”

“Teacher Jin.”

They were Team Leader Choi, who looked relatively presentable, and Shao Shen, the A-rank Hunter from China’s Public Security Armed Forces.

A considerable amount of time had passed since the battle ended, but Shao Shen’s face was still covered in blood and dust, and exhaustion had sunk deep into his features.

“So you were here.”

I greeted Team Leader Choi with a glance and made an excuse.

“Yes. I had something to take care of.”

“Please, speak casually to me. Sibeol—no, Teacher Jin, you are a hero who saved me and my comrades. More than that, you saved the people of Zhonghua.”

“……”

Was it my imagination, or had he just been about to call me Sibeol-jwa?

Whether he knew what I was thinking or not, Shao Shen continued in an extremely polite tone.

“Fortunately, with the help of the two gentlemen from Peace Guild, we were able to repel the monsters. I would like to take this opportunity to thank you once again.”

“Ah, yes. It was nothing. It was simply what needed to be done.”

I waved my hands modestly, then glanced at Team Leader Choi.

I had been worried that the Integrated Language Pack might malfunction and he would notice something strange. But since Shao Shen was the person I was speaking with, it seemed that even my words sounded like Chinese to Team Leader Choi.

“But who is the gentleman beside you…?”

The only unfamiliar person among them was a middle-aged man with half-gray hair.

He had been listening silently to our conversation. Now he extended a hand for a handshake.

“I am Wei Penghu, Minister of Defense at the Central Military Commission. It is a pleasure to meet you, Teacher Jin.”

“The Minister of Defense…?”

“My rank is Senior General.”

“Oh.”

I could tell he was an important man, but I had no idea what a Senior General was.

Perhaps he read my thoughts, because Team Leader Choi whispered from beside me in a voice as tiny as an ant.

“Four-star. Four-star.”

“Oh, ohhh! So you’re a four-star general! Nice to meet you!”

I had been a four-star once, too. The game I played as a kid had been a lot of fun. The sequel had flopped so hard it was practically in a league of its own.

Wei Penghu smiled faintly at my reaction and clasped my hand.

“Perhaps because you are young, you are full of vigor. I have much to ask Teacher Jin, but… shall we talk on the way?”

“Sure, why not?”

I started following Wei Penghu, then stopped.

“But where are we going?”

“To the operations headquarters. I have a jet standing by.”

“What? Headquarters? A jet?”

“That is correct. Everyone is waiting for Teacher Jin there.”

Everyone?

Who?
## Chapter artifact 383

# Chapter 383

The jet Wei Penghu had prepared looked nothing like what I’d expected.

*It’s spacious. And fancy.*

Through the slightly open door, I could see a luxurious table and the kind of chair people called a chairman’s chair.

Team Leader Choi, who was standing beside me, informed me that this was a business jet costing close to one hundred billion won per aircraft, then added,

“I never thought I’d see an aircraft normally reserved for state guests here.”

Wei Penghu replied calmly.

“Of course. The two of you are state guests of our country.”

“Oh.”

“Thanks to you, we were able to save countless soldiers and Hunters. No one—including me—will ever forget the help you gave us today.”

“…Ah, yes.”

*I’d appreciate it if you dealt with the fine dust and historical distortions first.*

Hoping China was a more conscientious country than I knew it to be, I boarded the aircraft.

The waiting pilot gave us a crisp salute—or, more precisely, gave Wei Penghu a crisp salute.

“Welcome, Comrade Minister of Defense.”

“Are we ready?”

“All escort aircraft, including this one, have completed their preparations. We await only your command.”

I wondered what he meant by “escort,” then looked out the window and saw five fighter jets with sleek, elegant curves blinking their lights as if signaling us.

*What the hell?*

I’d only ever seen things like that in war movies. Were we heading straight into a fight?

Seeing my eyes widen, Wei Penghu spoke.

“The exact situation has not yet been made public, but as you know, Sichuan Province is currently in a state of war. Magical interference with communications and attacks by flying monsters are both frequent. Escorts are essential for our safety.”

“Are you serious?”

The situation was worse than I’d imagined.

The wyverns had come to attack Chengdu International Airport and only attacked us while they were at it. But if the same thing was happening throughout Sichuan Province, that was an entirely different story.

“If only I were lying. How wonderful that would be.”

Perhaps merely recalling the current situation was exhausting him. Wei Penghu, who had aged considerably, leaned back into the plush seat.

“It seems we must part ways here. I hope we meet again soon, Senior Colonel Shao Shen.”

Unlike us, one man had not boarded the aircraft. Shao Shen stood rigidly at attention and saluted.

“Yes. I will complete my mission as quickly as possible and rejoin you, Comrade Minister of Defense. And you as well, Teachers.”

“Yes. I have high hopes for you.”

Perhaps because Shao Shen had distinguished himself in battle, a pleased smile briefly touched Wei Penghu’s lips as he regarded the promising young Hunter.

Team Leader Choi offered a polite bow in place of a farewell, while I waved.

“See you next time. You fought really well today.”

It was only one sentence.

But Shao Shen’s eyes grew as large as serving trays when he heard me. His entire body trembled as though he’d been electrocuted, and he shouted in a booming voice,

“Th-Thank you! I will devote every ounce of my humble strength to every task so that Teacher Jin is never disappointed!”

“…No need to go that far.”

“I pray that your august person remains safe! Loya-alty!”

“Your august person? What does that even—”

Smack!

“Ngh!”

“…”

*That looked like a textbook example of poor judgment.*

He’d saluted so forcefully that the edge of his hand had struck his own eyebrow.

As I stared dumbfounded at Shao Shen clenching his teeth against the pain, the door closed and our business jet slowly began to take off.

“That guy is, how should I put it… quite a character.”

Wei Penghu let out a quiet laugh at my dubious comment.

“He heard praise from his idol. Can you blame him?”

“Pardon?”

“There are many young Hunters in our country who admire Teacher Jin. He is no exception.”

*What? Was I a Korean Wave star now?*

Come to think of it, this man seemed unusually interested in those beneath him for a four-star general who was powerful enough to make birds fall from the sky.

Or perhaps Shao Shen was simply a young man who inspired that much expectation.

*Ah, but…*

- Team Leader, how high up is the Minister of Defense at the Central Military Commission, exactly? I’m not familiar with how things are structured here.

Team Leader Choi flinched at my Sound Transmission, then answered through message magic.

- In our country, he would be the Minister of Defense. Of course, this is China, and Wei Penghu is the current chairman’s right-hand man, so his power is far greater.

- Ah.

*We’re similar. I’m the Minister of Soup and Rice, myself.*

*One extra-large bowl of sundae-guk[^1] is enough for me to polish off three bowls of rice.*

*Of course, Wei Penghu could probably erase three cities with a single point of his finger.*

And now, that immensely powerful official of the People’s Republic of China leaned his upper body toward us and asked,

“It seems we have much to discuss on the way. Wouldn’t you agree?”

Team Leader Choi and I solemnly nodded and began to speak.

“Of course. First, we would like to ask exactly what is happening in Sichuan Province—”

“By the way, do you happen to have any boiled eggs and soda? I’m hungry after fighting so hard.”

“…”

“…”

Apparently, they didn’t.

“We do.”

“…?”

“…?”

They did.

* * *

The People’s Republic of China.

As its official name suggested, the majestic people of this vast continent still embraced socialism as their national ideology.

About twenty years ago, the chairman at the time—who had cemented the foundations of his dictatorship by securing lifelong rule—died during the Great Cataclysm, and power passed to a much more moderate regime.

But the core of the system remained unchanged.

- What was the dead chairman’s name again? Pingping? Pengpeng?

Team Leader Choi, who had been responding to Wei Penghu, silently moved his lips. His poker face was astonishing.

- …I’m only saying this in case you didn’t know, but you’ll be in serious trouble if you bring up something like that here.

- That’s why I’m using Sound Transmission—or rather, message magic.

- I’m telling you to be careful. Some outstanding mages of A-rank or above can eavesdrop on message magic.

- Anyway, what was his name? Pingping or Pengpeng? I won’t be able to sleep tonight if I don’t find out.

- …Pingping.

*He was going to answer in the end anyway. Why make such a fuss?*

Finally relieved, I listened to Wei Penghu’s words.

“No one could have anticipated it.”

Sichuan Province was a massive province with a vast area and a population of tens of millions.

And all of this had begun in Gaoping District, Nanchong City—one of the more than twenty administrative districts in Sichuan Province.

“As you know, our country has more than ten times as many Gates as other nations. Because of that, we were one of the countries hit hardest during the Great Cataclysm, and we have managed them with corresponding rigor ever since.”

But humans could not control even natural disasters, and the monster wave was a calamity worse than any natural disaster.

“Exactly thirteen minutes after the first sign appeared, we received word that the mana levels in Gaoping District had skyrocketed. And by the time Lei Fei, commander of the Public Security Armed Forces stationed in Sichuan Province, arrived at the scene with the Hunters under his command… everything was already too late.”

“Lei Fei?”

An unfamiliar name. And yet, for some reason, a memory suddenly surfaced.

*The video Team Leader Choi showed me at the Guild house before we left.*

It was still vivid: the city plunged into pandemonium beneath the hologram’s light, and a man at the head of the Hunters cutting down monsters one after another.

His weapon had been wreathed in aura brilliant enough to dazzle the eyes.

“I think I’ve seen him before. Is he the man who appeared in the video you sent us…?”

“That’s right.”

Wei Penghu hesitated briefly, then continued with a faint sigh.

“He was one of our country’s S-rank Hunters. Of course, the two of you would not have known that.”

*We wouldn’t have known?*

There were only twenty S-rank Hunters in the entire world. They were absolute powerhouses.

The fame and status they enjoyed were far greater and more formidable than those of even a Supreme Peak master in the Murim.

The internet, the news, and social media were their platforms, while microphones and cameras followed them like shadows.

If ordinary people regarded martial artists with equal parts wariness and curiosity, modern people saw Hunters as objects of pure admiration.

They were celebrities known throughout the world.

*But we didn’t know about an S-rank Hunter like that?*

Wei Penghu had spoken indirectly, but the meaning behind his words was clear enough.

Team Leader Choi and I locked eyes in midair. At that moment, we were thinking the same thing.

*An undisclosed S-rank Hunter.*

No. More precisely, an S-rank Hunter deliberately concealed by the Chinese government.

*I’d only heard rumors about things like this. So it was true?*

An S-rank Hunter was practically the face of a nation.

But unlike the weak, who struggled desperately not to be looked down on, the strong hid their claws.

China was already known to possess two S-rank Hunters. Clearly, it had not wanted to reveal all its strength.

Perhaps the same was true of the world’s other great powers.

*Seriously. Even after going through the Great Cataclysm, they’re still jockeying for advantage like this.*

It was pathetic. At the same time, I could almost understand it.

Diplomacy. Politics.

I felt as though I’d caught a glimpse of the truth of a world I’d never understood, and it left me with a strange feeling.

Unlike me, however, Team Leader Choi was much sharper.

“When you say Lei Fei ‘was’ one of your country’s S-rank Hunters, that sounds like the past tense.”

Wei Penghu answered with a grim expression.

“…A week ago, when the first monster wave occurred, Lei Fei disappeared. Along with the Hunters from the Public Security Armed Forces under his command.”

“Are you certain he’s missing? Could he perhaps…”

“We have not confirmed his death. After that video, the monster called the Lich—no, the Arch Lich—used mana to cut off all communications and surveillance.”

Team Leader Choi and I groaned at the same time.

Hearing our reaction, Wei Penghu asked in a hoarse voice,

“Do you two also think Lei Fei is dead?”

“Hmm.”

“Uh…”

*Missing. And if someone had gone missing in that hell a week ago, the ending was practically a foregone conclusion.*

At Team Leader Choi’s signal, I cautiously opened my mouth.

“Well, you never know how things will turn out, but…”

“Other experts said he was one hundred percent dead. Useless blowhards, every last one of them.”

*What’s wrong with you? They sound like real experts.*

If anyone guaranteed he was alive under those circumstances, they should be fired immediately.

That was simply a fact.

“But I disagree. Lei Fei—that boy must still be alive.”

“I hope so too, but realistically speaking…”

“He is my only nephew. My sister was sickly from childhood and died in childbirth. I raised that tiny, unweaned infant as if he were my own son.”

“What?”

*A nephew? You raised him as your own son? What the hell is this?*

I froze like a statue. Wei Penghu looked at me with tear-filled eyes.

“But what were you going to say? After ‘realistically speaking,’ I mean.”

*Fuck. This is the biggest crisis I’ve ever faced.*

The words caught in my throat. I barely managed to squeeze out a reply.

“Well, realistically speaking, I was going to say that there’s still some chance he might be alive.”

“Is that so? Is that true?”

“Yes. But that chance is extremely slim…”

“Thank you, Teacher Jin!”

“No, General. Commander. Great Leader. Just hold on a second and let me finish—”

Grab!

It was too late. Wei Penghu was no longer listening.

Instead, he clasped my hand in both of his, his eyes brimming with tears.

“May I ask you for one favor?”

*I wish you wouldn’t.*

Despite my desperate hopes, the words I’d been dreading pierced my heart a few seconds later.

“If you happen to meet that boy someday, would you bring him back to me?”

“…”

“I beg you.”

Over his desperately pleading shoulder, I saw Team Leader Choi shaking his head.

*What if I’d just given him a firm answer from the beginning?*

I regretted it, but it was already too late.

In the end, there was only one answer I could give.

“I will. But…”

“Teacher Jin.”

“Yes?”

“You don’t have to say it. I’m already prepared for that.”

“…!”

Wei Penghu wiped the corners of his eyes with his sleeve.

He was no longer a middle-aged man worrying about the safety of his blood relative. He had returned to being the Minister of Defense at the Central Military Commission.

“This is enough. No one was willing to step forward, but you promised me. I can rest easy now.”

“I can’t guarantee anything.”

“What I needed was not someone’s bombastic guarantee. It was a thread of hope.”

Just as Wei Penghu murmured those words, the aircraft glided toward the ground with a weightless sensation.

Outside the window, amid the deep darkness, I could see rugged mountain terrain, lights moving ceaselessly, and military vehicles.

“It looks like we’ve arrived.”

I had been staring fixedly out the window as though possessed by something. Now I asked,

“Where are we?”

“The temporary operations headquarters.”

“No. That’s not what I asked.”

“Hmm?”

“The mountain. That mountain feels strangely familiar.”

“That’s impossible. As far as I know, you have never entered our country before… Ah, perhaps you saw it in a photograph?”

“A photograph?”

“It is a UNESCO-designated World Cultural Heritage Site, so that is entirely possible.”

With a faint smile, Wei Penghu continued,

“The temporary operations headquarters. Welcome to Mount Qingcheng.”

[^1]: *Sundae-guk* is a Korean soup made with sundae, a type of Korean blood sausage, and is commonly served with rice.
## Chapter artifact 384

# Chapter 384

Mount Qingcheng.

A sacred Taoist site that had preserved the passage of countless ages.

Anyone who faced its stern, overwhelming mountain terrain would find themselves momentarily speechless, staring in awe.

But I was feeling a completely different kind of surprise.

*They’re definitely different… but they look alike.*

Mount Qingcheng in the Murim. And Mount Qingcheng in the modern world of the twenty-first century.

The two worlds I had experienced so far were similar in many ways—the terrain, the language, and even the appearance and lifestyles of their people.

At one point, I had even wondered whether the Murim might be the modern world’s distant past.

*But it wasn’t.*

The butterfly effect? There was no way something I’d only seen in movies had actually happened.

The two worlds were certainly similar, but they had subtle differences, and their histories were different as well.

The world of the Murim was also smaller than the modern world. It wasn’t divided into five oceans and six continents.

People with colored eyes did live in foreign lands thousands of miles away, but that was all. The center of that world was a continent ruled by a vast and powerful nation.

Perhaps the Zhonghua that the Chinese people insisted on so tirelessly was the Murim itself.

*But why did even this have to look alike?*

I had just returned from the Three-Sect Bloodbath, which had mercilessly dyed Sichuan Province in blood, only to come to Mount Qingcheng in Sichuan Province.

I didn’t know whether it was a simple coincidence or a cursed connection.

I just hoped even that wasn’t similar…

“Teacher Jin?”

“Mr. Jin Taekyung.”

“Huh?”

I lifted my head like someone waking from sleep.

Wei Penghu and Team Leader Choi had already gotten off the business jet and were looking at me with strange expressions.

“Sorry. I got distracted by the scenery for a moment.”

“You can see Mount Qingcheng’s beauty in this darkness. You must possess tremendous mana, Teacher Jin.”

That wasn’t entirely wrong, but now that I had reached the Supreme Peak realm, I could see through most things with my eyesight alone, without even using internal energy.

When I nodded with a subtle expression, Wei Penghu exclaimed in admiration.

“Now I understand why Korea has hidden you away so carefully. You truly are worthy of being called an S-rank Hunter—the face of your nation.”

“What? I’m still A-rank according to my license.”

“There’s no need to hide it. Our country has figured it out to some extent as well.”

Before I could say anything, Wei Penghu continued as smoothly as flowing water.

“To become an S-rank Hunter, one must gain enlightenment through constant mental cultivation and arduous training. Our country has also raised its current Hunters through countless trials and errors… Reaching such a realm at your young age means you must have received the full support of the Korean government.”

“…”

“…”

“Ah, of course, Teacher Choi beside you is also an excellent Hunter. Having people like the two of you with us is reassuring.”

*What was this nonsense about feeling reassured? Was he talking about a hearty bowl of gukbap or something?*

Team Leader Choi and I exchanged glances for a brief moment and reached a silent agreement.

*Keep your mouths shut.*

*Let’s just go.*

This seemed to have happened because I had reached this position in such an utterly unrealistic way. But there was no reason to remove the label they had already stuck on us.

Besides, convincing Wei Penghu right here and now sounded exhausting.

“Well, I think there’s been a slight misunderstanding. I’ll explain everything little by little when the time comes.”

“What misunderstanding? We’re both in a position to know the circumstances.”

“…”

“…”

“The Chairman already knows about the matter, so when you meet him, don’t bother denying it. Just accept it.”

*What does he know?*

I let out a quiet laugh.

*Speaking of the Chairman…*

A kinglike figure who held the population, economy, and military of the People’s Republic of China’s billion-plus people in one hand.

Even now that I had reached the Supreme Peak realm, to me—with modern common sense still rooted deep in my bones—he felt both close and infinitely distant.

*I wonder if I’ll get to see his face once this is over.*

Well, what did it matter? That was a problem for much later.

Even without my raid pay, my weekly salary was a whopping ten billion won. To me, he was merely a generous employer.

I could save people and make money at the same time. Two birds with one stone.

“That’s what I’ll do. If I meet him.”

“Good. Then let’s go meet him.”

“What?”

“Didn’t I tell you? He’s waiting in the underground bunker right now.”

*What the hell was going on?*

I stared blankly at Wei Penghu’s back as he walked ahead, then approached Team Leader Choi and whispered quickly.

“D-Did you hear that?”

“Yes, I did. But it’s somewhat unexpected to me as well. For the Chairman of China to leave the safety of Beijing and come all the way here… The public perception of him must be at least somewhat accurate.”

“To hell with public perception. China’s Jongseok—Jongseok!”

“Not Jongseok! The General Secretary! The state chairman!”

“Hmm? What did you just say?”

“Nothing, Comrade Minister of Defense.”

Team Leader Choi politely covered for us when Wei Penghu suddenly glanced back. Then, wearing an extremely serious and earnest expression I had never seen before, he spoke to me.

“Mr. Jin Taekyung. You must not make a slip like that in front of the Chairman. You understand? Especially the Jongseok thing. Don’t even bring it up. It’s not as though you’re talking about the name of some high school classmate.”

“Huh? How did you know?”

“…”

I could have sworn Team Leader Choi had just said *fuck*.

It was probably just my imagination.

I took a deep breath and muttered inwardly.

*Not Jongseok. The General Secretary. China’s Chairman.*

Unlike Team Leader Choi, who had been born into aristocracy, I was a commoner down to my bones.

Whatever feelings I usually had toward China, the thought of meeting the leader of one of the world’s ten greatest powers made my heart pound.

*Let’s just not make any mistakes. Especially not about Jongseok.*

Ten minutes later, I stood amid the gazes of the important figures gathered in a deep underground bunker and shook hands with the leader of the People’s Republic of China.

“Nice to meet you, Teacher Jin. This old man is Xiao Yang, the state chairman of the People’s Republic of China.”

*Good. I won’t even have to utter the first syllable of Jongseok.*

Having cleared the first hurdle, I opened my mouth with a relaxed mind.

“Welcome.”

“…”

“…”

*Oh, fuck.*

* * *

Chairman of the Central Military Commission of the Chinese Communist Party and General Secretary.

And the state chairman standing at the pinnacle of more than a billion people.

Xiao Yang.

His voice was gentle as he spoke to the people gathered there, but his eyes held power.

“As you all know, unfortunately, I am neither a military expert nor an outstanding general. I am merely a political schemer who entered politics early and achieved one small ambition only after reaching the age of seventy.”

The fact that he referred to himself as a schemer was so audacious that it was difficult to believe the words had come from the leader of a nation with the fourth-largest territory and the largest population on Earth.

*Was this what Team Leader Choi meant by the public perception of him?*

I felt as though I had a rough idea of what kind of person he was.

Perhaps it was merely a mask or hypocrisy he had put on before the people.

But at least from the old man continuing to speak before all of us—including me—Chairman Xiao Yang of China, I sensed a kind of qi entirely different from either of those things.

“Please do your utmost. Save as many of our people as possible, and stop this terrible disaster as soon as you can. If you do so, I will express my gratitude to you and your country in a manner befitting your efforts, and I will remember the help you have given us for a long time.”

I knew nothing about the life that old man had lived or the policies he had pursued.

But I wanted to give him considerable credit for reaching out to countries around the world for help in order to save his own people.

“That is all this old man has to say. I earnestly ask you not to concern yourselves with complicated matters like politics. Please find the best way to stop this situation with the fewest possible sacrifices.”

The old politician, who had devoted his entire life to politics, turned his head and looked at one man.

“Minister of Defense Wei Penghu. My old friend.”

“Yes, Comrade Chairman.”

“Do you want full authority over the Central Military Commission?”

Wei Penghu hesitated for a moment, then gave a heavy nod.

“Yes.”

“You would use that power well. But I will refuse.”

“…Comrade Chairman?”

“When this meeting is over, bring me the written order. I will take full authority over every matter and bear all the responsibility myself.”

For a moment, I wondered why China’s Jongseok was acting that way.

But now I understood. It was his declaration that he would shoulder everything himself.

Team Leader Choi muttered beside me as he watched the scene.

“He’s a good leader.”

I shook my head slightly.

“No. To me, Team Leader Choi, you’re the best.”

“Mr. Jin Taekyung…”

“So please raise my Guild settlement percentage.”

“Mr. Jin Taekyung…”

Same words. Different feeling.

Team Leader Choi looked at me as if to say, *Of course you’d say that, you bastard,* and shook his head.

That was when it happened.

“The Chairman is leaving.”

At the secretary’s words, everyone who had been seated rose from their places.

It was the minimum courtesy owed to a head of state.

“I wish you all good fortune.”

The Chairman looked each person in the eyes as he spoke to them.

Of course, I was no exception.

As luck would have it, I was the last one.

“Teacher Jin.”

“…Yes.”

A faint smile touched the corners of the Chairman’s mouth as he looked at me.

“I have very high hopes for you, Teacher Jin. Though this is a contract in which we exchange what we each need, I hope that you will put human lives first in every situation.”

Was it my imagination, or was his farewell unusually long compared to everyone else’s?

Feeling everyone’s eyes on me, I nodded.

“I understand.”

“Please be a great source of strength to us.”

The Chairman finished speaking and was about to turn away when he abruptly stopped.

Then he tossed out one more word.

“Welcome.”

“…”

“Well, that will be all.”

After the high-ranking Chinese officials who had been present to see the Chairman off disappeared, I dropped heavily into a chair.

*Fuck.*

If I died, the cause of death would be humiliation.

Even if a monster killed me, I would insist that the cause of death be recorded as humiliation.

*No! Nooooooo!*

As I screamed inwardly in every direction, something pressed down firmly on my foot.

It was obviously Team Leader Choi, who was sitting beside me.

“What?”

Team Leader Choi gave a small cough.

“Ahem.”

“What?”

“Ahem. People. People.”

“Oh.”

I looked around and finally realized that more than a dozen men and women of different races were watching me inside the underground bunker.

Four of them stood out in particular.

*Those people are…*

A Chinese man and woman.

And two Western men, one tinged with green and the other with blue.

I could feel it just from meeting their eyes—the immense power coiled inside their bodies.

My first thought wasn’t that it was surprising, but that it was only natural. Anyone who knew the identities of those four would have thought the same thing.

*S-rank Hunters.*

People whose very existence was news. Those who stood at the pinnacle of the countless Hunters in the world.

The faces I had seen to death on television and in advertisements were right in front of me.

And now, one of them stood up and extended a hand toward me.

“Nice to meet you. I’m… Ah, do you perhaps not speak English? I can use translation magic if you’d like.”

I hadn’t expected him to speak to me first. Looking flustered, I took his hand and answered.

“No, it’s fine.”

“Oh, listen to this fellow’s pronunciation. I’d believe you if you told me you were American.”

The middle-aged Black man was a giant well over two meters tall. His blue eyes gleamed as he asked,

“You seem to know who I am. Don’t you?”

As if I wouldn’t.

I felt even more nervous than I had when facing Chairman Shao Yang.

“Of course, Magic Johnson.”

The title of Archmage had been bestowed upon only three people in the entire world.

The Black man standing before me, Magic Johnson, was a War Mage—the most combat-oriented of those three Archmages.

*I’m talking to Magic Johnson. I guess days like this really do come along.*

As I thought that I had made the right choice in coming here, the world’s greatest War Mage smiled broadly and spoke to me.

“Haha. I’m glad you recognized me. Actually, I’ve known about you for a while too.”

“M-Me?”

“Of course. Even my youngest daughter, who started elementary school this year, knows Sibeol-jwa.”

“…”

*How far has that damn nickname spread?*

What would they call the nickname Sibeol-jwa in the English-speaking world?

*Fuck Guy? Fuck Man?*

The thought of Magic Johnson’s little youngest daughter knowing me by that name was not flattering in the slightest.

And apparently, I wasn’t the only one who disliked it.

“That is an obscenely vulgar nickname. Though I suppose it suits a mere A-rank Hunter like you.”

A Chinese man who looked to be around thirty, relatively young, stared at me with his arms folded at an angle.

“Isn’t that right, you peninsula bangzi?”[^1]

Team Leader Choi didn’t even have time to stop him.

My voice had already come out like an automatic response.

“What are you saying, you mainland chink bastard?”

[^1]: *Bangzi* is a derogatory Chinese slur for Koreans.

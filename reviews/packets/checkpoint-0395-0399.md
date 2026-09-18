# Checkpoint Review — 395–399

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

# Chapters 395–399

## Plot

Magic Johnson teleports Jin Taekyung to an emergency conference as the Arch Lich’s interference appears to weaken. The conference confirms that the Arch Lich can intercept missiles with teleportation magic, making aerial support unreliable. Jin challenges Prince Felix’s formalities and Lee Jungryong’s account of Ares Guild’s northern-front defeat, suspecting the loss was intentional. Before he can investigate further, coordinated monster assaults erupt across every front.

The Arch Lich had concealed the restoration of its power, withdrawn its armies to create false confidence, disrupted communications, and then launched simultaneous attacks. The black knight leads a massive undead legion against a city, displaying disciplined tactics, human-language comprehension, and flashes of memories involving a child and a place from its unknown past.

Magic Johnson sends Jin alone to the battlefield using a teleportation method with only a ten-percent survival chance. Jin arrives after Choi Minwoo and Shao Shen lead a final stand to protect the People’s Liberation Army. He restores Choi and Shao with Wu Heixing’s top-grade potion, kills a Death Knight, and leaves the Skeleton Warlord to guard them. Jin then cuts through the undead army and battles the Level 135 Death Knight Lord. After a devastating clash destroys the hospital and surrounding ground, Jin breaks the Lord’s armor, wrist, sword, and helmet, revealing a face resembling the missing Lei Fei.

## Continuity

- Jin survived the dangerous teleportation and remains combat-capable despite a deep chest wound.
- The Fire Dragon Armor is approximately fifty percent restored and mitigated part of the Death Knight Lord’s attack.
- Jin killed one Death Knight with the Flame-Extinguishing Divine Fist and overwhelmed the surrounding monster army.
- The Level 135 Death Knight Lord’s armor, wrist, sword, and helmet are broken; his exposed face resembles Lei Fei, but their identity is not confirmed.
- The Skeleton Warlord is guarding the recovering Choi Minwoo and Shao Shen at Jin’s command.
- Choi survived catastrophic injuries after receiving half of Wu Heixing’s top-grade potion; Shao received the remainder and is recovering.
- The Arch Lich’s strengthened interference has severed or delayed communications across the fronts and enabled a coordinated surprise attack.
- The black knight commands one of five undead legions, serves an unidentified lord, and remains bound to that lord’s orders.
- The black knight understands human speech, remembers a child and a shoe, experiences unexplained chest pain, and has begun questioning its obedience and identity.
- Lei Fei and his unit remain unresolved; the Second Fiend assigned to the Qingcheng attack is also unaccounted for.
- The identity of the lord served by the black knight and the Arch Lich’s larger objective remain unknown.

## Translation Decisions

- Use **Jin Taekyung**, **Magic Johnson**, **Team Leader Choi**, **Choi Minwoo**, **Shao Shen**, **Lee Jungryong**, **Wu Heixing**, **Prince Felix**, and **Lei Fei**.
- Render **Death Knight Lord** and **Skeleton Warlord** as capitalized titles; keep **black knight** lowercase and distinct from both.
- Render **Lord** for 로드 when the Death Knights address the black knight, and **my lord** for 군주시여.
- Retain **Nightmare**, **Fire Dragon Armor**, **Flame-Extinguishing Divine Fist**, **top-grade potion**, and **White Flame**.
- Preserve Jin’s blunt, profane combat voice, his irreverent banter, Choi Minwoo’s profanity, and Magic Johnson’s casual flirtatious tone.

## Durable state

{
  "active_continuity": [
    "Jin Taekyung is fighting the Level 135 Death Knight Lord after overwhelming the surrounding monster army.",
    "Jin killed an attacking Death Knight and heavily damaged the Death Knight Lord, breaking his armor, wrist, sword, and helmet.",
    "The Death Knight Lord's sword cut Jin's chest, but Jin remains able to fight.",
    "The Fire Dragon Armor is approximately fifty percent restored and mitigated part of the Death Knight Lord's attack.",
    "Jin recognizes the Death Knight Lord's exposed face as resembling the missing Lei Fei, without confirming that they are the same person.",
    "The Skeleton Warlord is guarding Choi and Shao at Jin's command.",
    "Lei Fei remains missing with his unit after the first Monster Wave."
  ],
  "continuity_sources": [
    399
  ],
  "open_questions": [
    "Is the Death Knight Lord actually Lei Fei, and what is the black knight's identity and origin?",
    "What is the significance of the black knight's memories and the child and shoe he recalls?",
    "Who is the lord served by the black knight, and what is the Arch Lich's larger objective?",
    "What will happen in Jin Taekyung's confrontation with the Death Knight Lord?",
    "What happened to the Second Fiend assigned to the Qingcheng attack?"
  ],
  "safe_through": 399,
  "temporary_decisions": [
    "Render 나이트메어 as Nightmare.",
    "Use black knight for 검은 기사 and keep it distinct from Death Knight and Death Knight Lord.",
    "Preserve Jin's blunt, profane combat voice."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 395

# Chapter 395

“Follow me.”

Magic Johnson led us to none other than the hospital rooftop.

After sweeping my eyes across the empty landing pad, where there wasn’t a helicopter or jet in sight, I asked,

“There’s nothing here.”

“Nope. I’m here.”

Magic Johnson’s answer was short and simple, but the meaning behind it was anything but.

Team Leader Choi’s eyes widened slightly, as if he had arrived at the same conclusion I had.

“Mr. Johnson. Don’t tell me…”

“That’s right. We’re going to travel by teleportation magic.”

Teleportation. In simple terms, instant travel.

Magic Johnson spoke as casually as if he were suggesting we take a ride on a tricycle, but everyone knew that teleportation magic was infamous for its extreme difficulty.

The finicky conditions that had to be met to cast the spell were one thing. If your coordinates were even slightly off, you could easily end up dead.

Apparently, being one step off could leave you fused with an apple tree or a boulder. Horrifying.

“Can’t we just take a jet?”

“Nope.”

Magic Johnson answered firmly and narrowed his eyes.

“Hey, Jin. You don’t actually distrust me, do you? I’m Magic Johnson. Do I have to show you before you’ll believe me?”

“……”

*You saying that somehow makes it sound even stranger.*

Whether what he intended to show us was teleportation magic or Johnson himself, I didn’t care. I simply wanted to travel peacefully by jet.

Team Leader Choi noticed my desperate expression and spoke up.

“Mr. Johnson. As you know, this area is within the Arch Lich’s sphere of influence. Not only is magic disrupted, but communications are unreliable as well.”

“Ah, so that’s what this is about. I thought it was something else.”

Magic Johnson let out a quiet laugh.

“How do you think I got here?”

“Huh?”

“Don’t tell me…”

“That’s right. I came by teleportation. It was a little irritating, but nothing can keep Magic Johnson down.”

Snap!

Magic Johnson snapped his fingers, and a pillar of flame shot up from the empty air. It was the effortless manifestation of magic, as natural as breathing. The contrast between him and the mages of the Public Security Armed Forces Department, who had been unable to use magic properly because of the magical interference, was striking.

“You could do that from the beginning?”

“Of course not. Until now, I could use most ordinary spells well enough even with the magical interference, but teleportation is too dangerous. I didn’t even dare try it.”

“Then…”

“The Arch Lich. Its power had been gradually weakening. In particular, a considerable portion of the interference disappeared after last night. Though communications still seem to be a complete mess.”

It was something he could say—and accomplish—because he was one of only three archmages in the entire world.

Magic Johnson showed us his white teeth as he held out a hand.

“That should be enough for you to trust me, don’t you think?”

“Well, if you put it that way.”

Unlike me, who took his hand without much hesitation, Team Leader Choi quietly stepped backward.

“Team Leader Choi?”

“I’ll stay here.”

“Why, Choi?”

“There are still things I need to take care of. Besides, with my limited voice in the matter, listening in person or hearing about it afterward will make little difference.”

Team Leader Choi always looked at the situation coldly. If he couldn’t change the course of events himself, he pulled forward matters of secondary importance and resolved them instead.

I wanted to tell him that he was mistaken, but I quietly nodded.

*He wasn’t wrong.*

Even the S-rank Hunters with powerful voices were, in the end, mostly mercenaries from other countries—borrowed blades.

That was why Chairman Shao Yang and Minister Wei Fenghu had made it clear that overall command belonged to them.

“Choi’s dropping out? This can’t be happening! Jin has no Charm!”

“……”

*I really want to put a nail through him. On second thought, maybe this is a good thing.*

After whining for quite some time, Magic Johnson said goodbye to Team Leader Choi with a deeply disappointed expression.

“Can’t be helped. See you next time, Choi.”

“Take care.”

“Take care of what? It’ll only be an instant anyway.”

Magic Johnson shrugged and looked at me.

“Hey, Jin. Ready?”

“Yes.”

“Hold my hand tight. Don’t let go.”

“……Why are we interlocking fingers? Can’t I just hold your palm?”

*Isn’t this something lovers do?*

As a guy in his late twenties who had been single his entire life, I couldn’t help feeling uncomfortable about interlocking fingers with a huge Black man.

Magic Johnson spoke to me in a gentle voice as I grimaced.

“You can let go if you want. But if you lose your grip during the journey, you might die.”

I thought of my first love from childhood and gripped Magic Johnson’s hand firmly.

“Let’s go, darling.”

Magic Johnson answered with a stern expression.

“Sorry, but Jin isn’t my type. You don’t have to squeeze that hard, so could you ease up?”

“……Oh. Right.”

“Then, shall we go?”

Just as I opened my mouth to answer—

Whoooooosh!

*Gasp!*

My breath caught in my throat, and taut air squeezed my entire body.

Through my blurring vision, Team Leader Choi’s figure wavered like a mirage before disappearing.

The earth and sky turned upside down, and then an incredible sense of release finally washed over me.

“Bwah!”

I let out the breath I had been holding and drew in a deep breath. Cool air seeped deep into my lungs. I blinked, and my briefly blurred vision cleared.

It felt as if barely a second had passed, yet an entirely different landscape and different people stood around me.

“Our last guest has arrived.”

Wei Fenghu, Minister of National Defense under China’s Central Military Commission, approached and patted me on the shoulder. He looked as if he had aged ten years in the past week.

“Everyone is waiting. Let us go inside together.”

“W-wait a second.”

“Yes?”

“Don’t come any closer…”

“Uweeeeeegh!”

Splash!

For the record, I’m fairly tall. About two heads taller than Wei Fenghu.

As I vomited all over the thinning-haired old general’s crown, Magic Johnson’s voice reached me.

“Ah, I forgot to mention that the motion sickness gets worse. I’m sorry, Jin. I’m sorry, Wei Fenghu.”

“You should’ve told me that earlier, uweeegh!”

“……Hah.”

It took a little longer before I was able to attend the meeting.

* * *

The large conference room was dim, and a holographic video was playing in the darkness.

The footage captured everything from a single person’s perspective: a complicated control panel, clouds scattering beyond reinforced glass, and the tiny, distant specks that began to appear as the aircraft descended.

The things covering the ground surged forward like waves, without ranks or formation.

*Monsters.*

It wasn’t difficult to tell that the owner of this viewpoint was a fighter pilot. Wearing a head-mounted camera, the pilot transmitted a radio message to someone.

—This is YANU-4885. I repeat, YANU-4885. Target confirmed. Locked on.

—You are cleared to fire.

Crackle. Crackle.

The radio was filled with static, but the words were still clear enough to understand. The pilot took a deep breath and carried out the mission without hesitation.

Rumble.

With a slight tremor, a missile mounted on the fighter jet launched. It became a single dot as it streaked away, about to strike the center of the advancing monster army—

Whoosh!

A black vortex suddenly appeared in the empty air above their heads and swallowed the missile.

—Hngh!

With an urgent gasp, the pilot pressed a red button on the control panel. But then—

Boom! Crackle.

The footage cut out amid a thunderous roar that suddenly crashed through the room.

The hologram disappeared, and Minister Wei Fenghu spoke with a grave expression.

“What do the rest of you think?”

Magic Johnson lit a cigar before answering.

“It was teleportation magic. The missile was teleported above the aircraft.”

“Mr. Johnson. Would that be possible for you?”

Magic Johnson, who had been deep in thought, finally spoke.

“It wouldn’t be difficult. But I can’t say I’d be able to do it that quickly and accurately.”

“Even for an archmage such as yourself?”

“……Hmm.”

Magic Johnson nodded slightly and exhaled cigar smoke.

He, too, was an S-rank Hunter who had accomplished feats that would go down in history. He must have been proud of his abilities, so he couldn’t have been pleased to learn that he had been outdone by a monster called the Arch Lich.

But this meeting had not been arranged to protect anyone’s pride. We had to face reality.

“Then it looks like fire support will be difficult. If one of the big shots goes wrong, it could cause a catastrophe.”

Faye Chen continued, lightly touching her wineglass with one slender finger.

“I expected something like this to a certain extent, but now that it’s come to this, we have no choice but to settle things on the ground.”

“The situation will gradually improve if things continue as they are. The royal guard of the British Empire, led by this prince, crushed the monster army. More importantly, that wine you’re drinking—is it perhaps a 1945 Romanée-Conti?”

“No.”

“Hm. You don’t know how to drink.”

Faye Chen glared at Prince Felix.

“Oh, my. What is this child talking about? Get a grip. The British Empire was dissolved long ago, and the monsters didn’t retreat because you won a few battles. They retreated because of that fellow sitting across from you.”

Prince Felix glanced at me.

“I heard that you distinguished yourself greatly on the western front…but are all those stories truly accurate?”

*What, does he think I’m lying?*

I stared at Prince Felix with an incredulous expression.

“Then they’re true, aren’t they? What, you think I made it all up? If you don’t want to believe me, don’t.”

“You may deserve praise for accomplishing such a great feat, but your words and conduct are remarkably insolent. Address me as His Highness and always speak respectfully.”

I readily agreed to his demand.

“His Highness, did you eat your fish and chips wrong?”

“Hmm. A man of unmatched courage, but utterly lacking in manners.”

“……”

*Utterly lacking in manners, my ass. I might just take one of his balls off.*

For the record, the guy I had beaten up about a week ago kept his mouth shut and refused even to meet my eyes.

*It’s nice that he’s quiet, but something about it feels unsettling.*

With Wu Heixing’s level of stupidity, I had expected him to come at me at least a few more times. Maybe he was more cowardly than I’d thought—or maybe I’d misjudged him.

More than anyone else, though, there was someone I found more irritating than Wu Heixing at that moment.

“You’ve been quiet for a while. Don’t you have anything to say?”

Lee Jungryong, a snake coiled in wait, smiled gently.

“Thank you for your concern, but I’m fine. A mercenary’s virtue is following the employer’s wishes without comment.”

“Oh, is that so?”

“It’s a simple principle.”

I smiled along with him and spoke.

“But for someone who says that, your performance seemed a little lacking. The situation on the northern front doesn’t look very good. Was that the employer’s wish, too?”

“……!”

At my single remark, the entire room fell silent as if someone had dumped cold water over everyone’s heads. As the gazes of those around him gathered, Lee Jungryong stroked his chin.

“That remark is unpleasant. Ares Guild and I did our best.”

“Your best? Really?”

“We fought ten times over the past week and won nine. Though we unfortunately suffered one defeat, I would consider that an impressive military record.”

Ten battles, nine wins, one loss. By the numbers, it was certainly an impressive record.

But two days ago, when Team Leader Choi and I heard the news of the northern front’s defeat, we had both let out hollow laughs.

*What a sly old man.*

Lee Jungryong was one of the strongest men in the world—or, by Murim standards, an incredibly powerful martial artist. Given his personality, there was no way he had revealed all his abilities. He was probably even stronger than the public believed.

And someone like that had the nerve to say—

*“Unfortunately suffered a defeat,” my ass.*

I couldn’t say this about anyone else, but I was certain.

The fact that Lee Jungryong had joined the battle and still lost meant the defeat had been intentional from beginning to end.

The Ares Guild members, who had withdrawn intact even amid the enormous casualties, were proof of that.

*Since I can’t prove it, I suppose it’s only a suspicion.*

That was also why Lee Jungryong could remain so relaxed. He loosely folded his arms and spoke.

“I regret that day’s defeat, but I would appreciate it if you refrained from making hasty accusations. There was an obvious reason for our loss.”

“An obvious reason?”

“Who could have expected a Death Knight to appear in that situation? Once the commander died, the confusion became impossible to control.”

“If you mean the Death Knights…”

“I heard they appeared on the western front last night as well. Is that not so?”

His words suddenly brought something to mind: the testimony of the civilian couple rescued from the small city.

Ten Death Knights had slaughtered nearly a thousand troops, and their leader, the black knight, had left without killing the couple for some unknown reason.

The black knight had bothered me ever since I heard that story.

“Then among the ones that appeared on the northern front, could one of them perhaps—”

My question to Lee Jungryong never reached its end.

Someone who looked like a Chinese officer came bursting through the door, accompanied by the urgent sound of footsteps racing down the corridor.

Bang!

“Huff, huff. Emergency! Emergency!”

He continued while gasping for breath.

“We have received word that the monster army has advanced! Fighting has broken out on every front!”

“……What?”
## Chapter artifact 396

# Chapter 396

The black knight raised his head and looked up at the sky.

A clear blue expanse without a single cloud. But to the black knight’s eyes, which had already lost their light, it appeared only as a dark, murky gray.

*How dark.*

The thought that suddenly occurred to him left the black knight feeling strange. Dark? What did darkness even mean?

He had been a black knight from the beginning. A being born from darkness does not know what darkness means.

*But this… What is it?*

Light and sunlight. A child laughing brightly. Someone’s hand stroking his head…

Several words and inexplicable scenes flashed through his mind in succession, leaving him confused.

If not for the call from one of his subordinates a moment later, the black knight would have stood there for a long time.

—Lord.

—Please.

Black armor as dark as night covered his entire body. Green lights flickered between the slits of the helmet covering his head.

Two Death Knights dismounted from their skeletal warhorses and knelt on one knee. Their voices were flat as they continued.

—Give us—

—your orders.

Ah.

The black knight recalled something he had briefly forgotten. It was the command given by the lord he served.

—Go. Advance in all directions, trample everything, and kill them all. Offer me mountains of corpses and seas of blood.

His lord’s commands were absolute. With even his soul bound to that lord, the black knight faithfully obeyed.

He had appointed the ten Death Knights under his command to lead five legions, then personally taken command of one legion’s vanguard and come here.

*But why this place, of all places?*

The black knight gazed at the small city in the distance.

It was a place he remembered. A place where the unfamiliar word *child* had suddenly come to mind, and where he had sensed an enormous power whose nature he could not identify.

But the black knight did not know why he had come here.

—Lord?

—Lord?

After silently looking down at his subordinates, the black knight finally gave his command.

—Advance.

—Your command.

—We obey.

Hearing the answer they had been waiting for, the Death Knights mounted their skeletal warhorses and raised their enormous spears high.

Demonic qi surged from the spearheads, and the monsters packed across the broad plain let out shrill howls.

—Kik. Kikikikik.

—Graaaargh!

From Skeletons that had died only recently and still had flesh clinging to their bones, to small monsters like goblins and Orcs, and large monsters such as Trolls and ogres…

Their numbers reached tens of thousands by a rough estimate. In the sky, groups of Gargoyles and Wyverns cast enormous shadows over the land.

—Rally.

—Do it.

At the next command, roughly two hundred Dullahans formed ranks. Holding their severed heads in one hand and weapons in the other, they rode atop beasts made of white bones, their eyes gleaming with ferocity.

—Prepare.

—for the charge.

The two Death Knights formed the tip of the legion. Their spearheads rose high enough to pierce the sky, then slowly descended until they pointed toward the city.

A city of humans. But soon, it would become a city of the undead—a land of death.

—Public Security Armed Forces Department, assemble!

—F-fuck! Monsters! They’ve appeared!

—Sound the alarm immediately and report to command!

Wheeeeeeng!

The cries of the humans and the sound announcing the emergency carried on the wind.

But the order had already been given. Nothing could stop the undead legion now that it had begun its advance.

Boom. Boom. Boom.

Ranks and files arranged with military precision.

Death Knights and Dullahans led the way, with fast-moving Lycanthropes and other monsters at the very front. Large monsters such as ogres, Trolls, and Golems advanced like a gigantic wall.

Monsters capable of using bows and magic had long since moved to the rear.

The black knight was also the one who had conceived of the discipline and formations that ordinary monsters lacked.

*Where did I learn something like this?*

Setting the question aside once more, the black knight opened his mouth.

—Follow.

In accordance with their master’s will, the skeletal warhorse he rode began to move.

Clip-clop. Clip-clop.

Hooves made of white bone trampled the new shoots beneath them. The undead legion blanketing the vast breadbasket advanced slowly behind its commander.

The earth shook beneath the enormous vibration. The legion, moving forward like a slow wave, soon became a wave of bones that swept across the plain.

Thudthudthudthudthud!

—Graaaargh!

The enormous roar of tens of thousands of monsters.

At the head of the monsters surging toward the city, the black knight shot forward like a streak of light.

—That one’s the leader!

—Ranged units! Prepare!

—Tanks, stay calm! The armored units will intercept him alongside the Hunters!

Tanks, armored units, Hunters.

The black knight could hear the humans shouting, and astonishingly, he understood them perfectly.

He even understood the command that would come next.

—Begin concentrated fire!

Rat-a-tat-tat-tat!

Boom-boom-boom!

Whoosh-whoosh-whoosh!

It was dazzling. Flames, ice, and flashes of light erupted throughout the city.

Some attacks came crashing down in graceful arcs. Others followed trajectories close to straight lines as they targeted the black knight and the undead knights behind him.

—Ah.

Even in a world dyed gray, the light those attacks emitted was enchanting and familiar. The black knight felt an inexplicable upheaval in his chest as he reached out a hand.

Shrring.

The greatsword strapped to his back slid free.

Before the fired shells, magic, and arrows could even reach him, the pitch-black blade slashed through the air in every direction.

Kraaaash!

A magical wind stormed through the battlefield. Space split apart. The magic containing dazzling mana went out like candle flames, and the arrows shattered into pieces.

Everyone in the city watched clearly as the light was devoured by darkness.

A single thought passed through Choi Minwoo’s and Shao Shen’s minds.

*This is…*

*Impossible to stop.*

An insight approaching certainty.

Then, in the next moment, a pitch-black flash leaped across space and struck the Hunters.

KABOOM!

A thunderous roar rang out, as if the sky itself had been split apart.

Dozens of tower shields shattered, and sprays of blood burst into the air. The black knight, who had cut down three A-rank Hunters and twenty B-rank Hunters with a single sword stroke, stared at the frozen humans through red glowing eyes.

Beneath his deeply lowered helmet, the cold voice of the dead drifted out.

—Aksar. Garosh.

Kill them all.

They were the words of the Demon Realm—the final words heard by those who had died here the previous day.

And…

They were also the order the black knight gave to the legion following behind him.

—Your command.

—We obey.

Two Death Knights appeared to the black knight’s left and right. Then one hundred Dullahans charged in behind them, becoming sharp awls that pierced the human wall.

Kra-d-d-d-d-d!

* * *

*An ambush?*

Emergency reports poured in from every front. Wei Fenghu shouted, demanding to know what had happened, but the answer he received was that communications with every front had been completely severed.

—Completely severed? Even if communications were unstable, weren’t we still connected since last night?

The communications officer answered while sweating coldly.

—W-we don’t know why, but the communications interference has grown even stronger. The emergency report that just arrived was confirmed to be from approximately thirty minutes ago.

“……!”

What? Thirty minutes?

If that was true, it meant the attacks had begun while the meeting was in progress.

And since the report had only barely arrived after struggling through the communications interference, it might not have been thirty minutes. It could have been an hour.

Magic Johnson muttered with his face gone rigid.

—That can’t be. It wasn’t that bad before I left…

Suddenly, the words Magic Johnson had spoken before leaving the city flashed through my mind.

*“Arch Lich. Its power is gradually weakening. In particular, a considerable portion of the interference disappeared after last night.”*

Wrong.

The Arch Lich’s power affecting the surrounding area hadn’t weakened. It had merely made it look that way.

Little by little, without giving anything away. Then, by withdrawing the legion, it had made it seem as if the range of its influence had shrunk dramatically—so that we could let our guard down even a little more.

*This is…*

A thoroughly prepared trap.

I didn’t know how the Arch Lich had realized that the S-rank Hunters were absent. What mattered was that it had seized that brief opening and sent the monster legions forward.

The thought of the horrific slaughter we had witnessed the day before happening across every front made my stomach churn even more violently than it had during my first teleportation.

But this time, instead of throwing up, I grabbed Magic Johnson and said,

“Teleport.”

—What?

“Teleport. Hurry!”

I expected Magic Johnson to use magic immediately. But the answer I heard next was not what I had expected.

—Jin. Take a jet.

“What? A jet? Why are you suddenly talking about that…? We’ll be too late.”

—It’d be too risky right now.

“Why not? You know the coordinates of the hospital rooftop where we were earlier.”

Magic Johnson shook his head.

—The coordinates aren’t the problem. If we try to teleport like this…we could both die.

“……!”

I had momentarily forgotten about the Arch Lich’s magical interference in my desperation. There was no way the one who had laid such a trap would kindly allow us to attempt teleportation.

Magic Johnson continued in a subdued voice.

—Ten minutes. Twenty at most. Take the jet, Jin.

“……A lot of people will die in that time.”

—Yes. But if you get yourself killed for nothing during the teleportation, there’ll be even more casualties.

An S-rank Hunter was a strategic weapon capable of turning the tide of a war.

Even if I arrived late, I might still be able to save some people. But if an accident occurred during teleportation, the countless people who lost me and the reinforcements would cross a river from which there was no return.

Magic Johnson was worried about me, but he was also pointing that out.

—It’s brave, but it’s foolish.

“……”

—The jet will finish preparing for takeoff soon. We don’t have time for this.

Through the bulletproof glass occupying one side of the conference room, I could see the pilots crossing the runway and boarding the aircraft.

I could also see the backs of the other S-rank Hunters, who had already left the conference room.

I watched the scene in silence, then suddenly spoke.

“You said it was possible, right?”

—What?

“Teleporting missiles, like in the hologram footage we saw earlier.”

Magic Johnson’s eyes widened.

—Jin, don’t tell me…

“There’s no need for you to risk yourself too, Johnson. I’m enough on my own.”

—Good God. Are you crazy? I explained it to you, and you still don’t understand!

“I understand perfectly. And I’m prepared to go that far.”

—You…

His lips moved as if he were about to say something, but then he suddenly slammed his fist down on the table.

Bang!

The expensive hardwood shattered beneath the force of his blow.

—Damn it! What the fuck is this!

I let out a quiet laugh as I watched Magic Johnson mutter one curse after another.

I already knew what his reaction meant.

“I can take that as your permission, right?”

—Yes, you insolent little brat.

His bloodshot eyes fixed on me.

He looked as if he might start hurling abuse at me.

Magic Johnson was genuinely furious—and at the same time, he was grieving.

—Listen, Jin. I…

“I know. You have people you need to protect, too. I’m sorry to ask you this.”

—……Damn it. Is sending you to the hospital rooftop enough?

“Yes. That’s enough.”

Swoosh.

Magic Johnson clenched his teeth and placed his thick palm against my chest.

As though taking every possible precaution, his mana began to slowly wrap around my body, unlike the first time he had teleported me.

—Ten percent. That’s your chance of survival. There’s a ninety percent chance you could die.

Ten percent…

I raised my head and looked up at the sky beyond the window.

A clear blue expanse without a single cloud. Was Murim somewhere in the distant universe above that sky? Were they waiting for me?

At that moment, a thought suddenly occurred to me, and the corners of my mouth lifted.

“That’s not bad. Ten percent is enough.”

—What?

A dazzling mass of light burst forth. Feeling warmth envelop my entire body, I continued,

“It’s probably a thousand times higher than the odds of crossing dimensions.”

—……!

I wondered what expression Magic Johnson was wearing by then.

I wanted to know, but unfortunately, I could no longer see his face. Along with the blinding flash blocking my vision came a rough, powerful force that sucked me beyond the distorting space.

Whoooosh!
## Chapter artifact 397

# Chapter 397

Team Leader Choi—or rather, Choi Minwoo—thought,

*What should I do?*

Unlike his violently pounding heart, his mind was ice-cold.

Only thirty minutes had passed since the battle began. The hastily constructed defensive line had collapsed the moment the fighting started, and when the highest-grade monsters slipped through the gaps and began rampaging as if no one stood in their way, it had been torn apart completely.

Just like now.

Crunch!

Sharp fangs savagely bit into a human throat.

The Lycanthrope threw aside the Hunter it had killed with a wheezing exhalation and let out a roar.

—Awooooooooo!

And those became the Lycanthrope’s final words.

Whoosh. Slash!

Gray fur was dyed red, and its body tilted. Choi Minwoo decapitated it with a clean, waste-free strike, then bent backward without even a moment to catch his breath.

Whoooooom! Crack!

It had passed within a handspan.

An ax blade rippling with ominous magic grazed Choi Minwoo and smashed the heads of two Orcs nearby.

The headless knight, a Dullahan, attacked the human in front of it without the slightest hesitation, despite having killed one of its own kind.

Swoooooosh! Slash!

—Krrk!

“Guh!”

As the enormous halberd swept back and forth, the bodies of humans and monsters caught within its range were torn apart.

A Dullahan was an A-rank monster that required three Hunters of the same level to deal with safely.

But Choi Minwoo slipped past its attack like water and thrust out his sword without hesitation.

*Now!*

A short exhalation.

Then a strike as swift as a flash of light.

Thud!

The blade, enchanted with three different spells and forged by a Master Artisan, pierced through the Dullahan’s shoulder.

It had already died once and become undead, so it might not have felt pain. But its body was still human.

When the muscles and tendons of its right arm were severed, the halberd lost its strength and slammed into the ground. Choi Minwoo did not miss the opening.

Shhhhhk!

A blade of white aura cleaved the Dullahan in half at the waist. It must have died only recently, because rotten blood burst from its collapsing body and splattered across Choi Minwoo’s face.

But even in the face of the terrible stench stabbing at his nose, he did not so much as twitch an eyebrow.

Choi Minwoo was consumed by the tension of the battlefield, his cold reason, and a faint exhilaration.

*That makes ten.*

The number of A-rank monsters Choi Minwoo had defeated alone today. Including the monsters of lower grades, the number must have easily exceeded fifty.

*Was I always this strong?*

If he answered that question honestly, the answer was no.

Perhaps because of the Arch Lich’s influence, the monsters he had encountered in China were slightly stronger and far more ferocious.

Even so, Choi Minwoo had been able to perform so well in this chaotic battle because he had been blessed with two strokes of luck.

The first was—

*The Jin Family’s Cultivation Technique.*

The mana cultivation method he had learned directly from Jin Taekyung.

Choi Minwoo had been suspicious of Jin Taekyung’s claim that it was a family heirloom passed down through the generations. But he had no disagreement whatsoever that it was an outstanding secret technique.

The Jin Family’s Cultivation Technique he had learned allowed him to control his energy steadily while greatly improving his distribution of strength. The immense mana he had gained during his training had also given him stamina that let him fight without tiring easily.

And his second stroke of luck was—

—Gwoooooar!

Boom!

A rebar swung with berserk force smashed through the concrete road.

Choi Minwoo sprang upward, stepping on the ogre’s thick arm, and brought his sword down with all his strength.

Thrust!

The aura-infused blade split through the ogre’s crown as easily as tofu.

Thud.

The four-meter-tall giant dropped to its knees with a heavy crash. Choi Minwoo stood atop the shoulder of the dead creature and swept his gaze rapidly across his surroundings.

*He’s not here.*

A hellish scene overflowed with screams and death on every side.

But the monster was nowhere to be seen. The monster who had displayed unbelievable power the moment the battle began—the commander of the monster army and leader of the Death Knights.

*Where the hell is he?*

Choi Minwoo remembered the black knight clearly. With a single strike, it had swept aside dozens of Hunters.

If the creature had truly decided to join the battle, the humans might have been annihilated without lasting even thirty minutes.

But for some reason, the black knight had not appeared since then.

Was it the monster’s arrogance—the belief that this was not a battle worthy of its intervention?

Choi Minwoo could not understand it at all. But that was both the second stroke of luck he had been granted and his last chance to make a decision.

*We have to retreat.*

The urban battle had already lost all meaning. The monster army, numbering around ten thousand, had already covered the city like a swarm of ants. Among them were more than a hundred A-rank monsters.

They were outmatched in both numbers and strength.

Nearly half of the thousand Hunters from the Public Security Armed Forces Department who had been holding the front line were already dead or wounded. And more than half of the damned People’s Liberation Army had thrown down their weapons and fled before the monsters even approached.

The armored units, reduced to heaps of scrap metal, and the air force, becoming prey for the flying monsters, were simply more of the same.

Rat-a-tat-tat-tat-tat! Boom!

A state-of-the-art combat helicopter lost its balance and plunged from the sky, exploding in flames. Around a dozen soldiers caught in the flying debris died without even having time to scream.

It was a horrifying sight. But in terms of dying without pain, they were the lucky ones.

The monster horde began tearing everyone apart indiscriminately.

—Kraaaaaaang!

Whoom! Crack!

The foreleg of a Saber Tiger, carrying several tons of force, crushed a soldier’s limbs and burst his head.

The soldiers of the People’s Liberation Army were not as fast as Hunters, and the rifles they carried were no different from slingshots to the monsters.

Choi Minwoo clenched his teeth at the merciless slaughter unfolding before him.

*Pull yourself together. You can’t save all of them.*

He did not speak hypocritically of sacrificing the few for the sake of the many. He simply faced the situation with a cold eye and finished preparing himself to become the villain of this stage.

*Could we have stopped them if he had come?*

He suddenly thought of Jin Taekyung, but it was nothing more than useless regret.

Even after hounding the communications officer into sending emergency signals frantically, there had been no response.

A carefully planned ambush, combined with thorough communications interference.

For now, all he could do was hope that one of the countless glass bottles cast into the sea would somehow reach him.

Thud!

Choi Minwoo drove his sword into the chest of a charging Minotaur and shouted,

“Shao Shen!”

His mana-infused voice pierced through the screams and thunderous crashes and reached one person’s ears.

Shao Shen, covered in wounds and blood as he fought back the endless stream of monsters, shouted in response like a battle cry.

「Speak!」

“Withdraw the Public Security Armed Forces Department. We have to retreat now!”

「What? But if we retreat now…」

Choi Minwoo already knew what the young Hunter was about to say.

The greatest number of casualties occurred during the pursuit after a retreat.

Especially in a situation like this, if the Hunters who had been serving as the last barrier withdrew, the People’s Liberation Army would fall into the monster army’s grasp.

“If we get surrounded, it’s all over. Do you understand? Even now, you need to lead the surviving Hunters and the rear units out of the city!”

「……Mr. Choi.」

“I know what you’re thinking. But we have no other choice.”

「……!」

Shao Shen squeezed his eyes shut without realizing it.

He knew the situation. No—he was one of the people who understood it better than anyone.

The battle had turned sharply against them from the very beginning, and the humans had been driven all the way back to the hospital they were using as a temporary command center. If the monsters completed their encirclement—

*Annihilation.*

He had thought for a long time, but the moment itself was brief.

Shao Shen opened his eyes and shouted with all his strength while deflecting the attacks raining down on him.

「Retreat! All Public Security Armed Forces Department personnel, withdraw immediately! The North Gate is open!」

During wartime, the command of a commander like Shao Shen was absolute.

All the more so when the military leadership, including Senior General Liao, had not even shown their faces.

*Good.*

The soldiers might not have much hope, but the Hunters’ odds of survival would rise dramatically. If Shao Shen made the right calls, a considerable number of them might be able to break through the encirclement and survive.

*Yes. This is enough.*

Feeling his heart grow lighter, Choi Minwoo threw himself forward.

Not toward the North Gate, which the monsters had yet to block, but toward the People’s Liberation Army being slaughtered by the monsters.

*It feels like I’m going to kill myself.*

Why had he made this choice? Even he could not understand it.

Still…

For something that amounted to going to his death, he felt surprisingly good.

Perhaps because dark clouds had gathered overhead, the wind was cool. And behind him, he had companions who would die alongside him, so he would not have to die alone.

Choi Minwoo suddenly parted his lips.

“Why didn’t you retreat?”

Shao Shen, who should have been heading toward the North Gate, gave him a faint smile.

「What about you, Mr. Choi?」

“……I asked first.”

「Then I suppose I should answer first. Public Security Armed Forces Department!」

At the regimental commander’s call, the roughly three hundred Hunters following behind him released a thunderous shout.

「To eliminate monsters and protect the people from every threat!」

「This is why we do not retreat. The 325 members of the Sichuan Province Public Security Armed Forces Department’s 1st Regiment, led by Regimental Commander Shao Shen, have come to protect the people!」

Shao Shen’s quiet voice followed.

「Now it is your turn to answer, Mr. Choi.」

Choi Minwoo silently gazed at the thousands of monsters drawing closer, then suddenly muttered,

“Fuck. Quite a crowd.”

「……!」

“That man probably would have said something like that. And he would have fought harder than anyone else, then won in the end.”

It was true. He had always been that way.

He had never retreated from any situation and had never given up. Choi Minwoo, who had watched him from closer and for longer than anyone else, knew that.

That man, Jin Taekyung, was a hero of the new age, while Choi Minwoo could never create miracles the way he did.

But still—

“It’s embarrassing.”

「What?」

“Jin Taekyung is technically my subordinate, you see. This is when a superior should lead by example.”

Choi Minwoo burst into laughter, loudly enough to leave Shao Shen bewildered.

His heart felt as light as a dandelion seed, and an indescribable power surged through his body as he launched himself toward the enemies.

*Mr. Jin. I’ll see you later.*

If I survive today, as soon as possible.

If I die, as late as possible.

Let’s meet then.

Hissssss.

The blade of his sword, filled with aura brighter and more radiant than ever, pointed toward the enemies.

The roughly three hundred-strong death squad, roaring loud enough to deafen the ears and overflowing with fighting spirit, shot forward behind him like arrows.

“Waaaaaaaah!”

Two Death Knights who had been leading thousands of monsters and slaughtering the People’s Liberation Army looked down from their skeletal warhorses at the pitiful human force.

—Aksar. Garosh.

A moment later, the black wave swallowed the white pebbles.

The battle’s conclusion had already been decided. Yet at the end of the fiercest battle of all, there was a sword belonging to someone whose light had never faded from beginning to end.

* * *

The two Death Knights dropped to one knee before the black knight watching them.

—In the battle—

—we achieved victory.

—Today, this glory—

—we offer to our Lord.

Their voices were clipped and devoid of intonation. Even at the news of victory, the black knight merely nodded without interest.

It had gone as expected. The humans had been unable to stop his mighty army and had collapsed all at once.

But if someone asked whether everything had unfolded according to the black knight’s wishes, the answer would have been no.

*Those humans from back then.*

After breaking through the city and forcing the humans to retreat at the start of the battle, the black knight had casually turned his warhorse around.

And at the previous day’s location—a place that felt strangely familiar—he had found something small.

*Human? No. Not human. A child. And this is a shoe.*

Memories and words surfaced one after another.

As the black knight had thought, it was a child’s shoe. A tiny infant’s shoe left behind during the chaos, without anyone realizing it had been dropped.

Looking at the unbelievably small, dirt-covered shoe, he felt that it was strangely familiar. His chest hurt.

*Hm? My chest hurts?*

What an unfamiliar expression.

The black knight’s body had been incapable of feeling pain from the beginning. His master had created him personally and given him a powerful blessing. Naturally, he did not tire, nor did he feel pain.

More importantly, this was no time to be swayed by something so trivial.

—Lord.

—Is something wrong?

He did not know why he had done it.

The black knight tucked the shoe he held into a gap between the plates of his armor and changed the subject.

—No. Rather, quite a few humans managed to escape alive.

—We apologize.

—It was our failure.

—There must be a reason.

The Death Knights bowed their heads deeply.

—The humans’ resistance—

—was fiercer than expected.

—In exchange—

—we gained a small prize.

As if they had been waiting for those words, the densely packed monsters parted left and right, opening a path.

A Troll cautiously approached, lowered what it had been carrying across its shoulders, and stepped back.

The black knight’s eyes shimmered as he looked at the “small prize.”

—They are humans.

—Yes.

The two loyal retainers answered at the same time, then continued.

—Personally reap their souls—

—and make them servants of our Lord.

—If you do so, Lord—

—you will grow even mightier.

They were right. Those two humans possessed rich and desirable souls.

If he personally reaped them and made them his subordinates, they would be reborn as even more outstanding warriors. They might even be entrusted with command over an entire force.

But—

*Why?*

The black knight realized that he was hesitating.

This was something he obviously had to do. Gaining powerful subordinates would strengthen the legion, which in turn meant loyalty and devotion to the King of Death whom he served.

So why was he hesitating?

*What is making me hesitate?*

Under normal circumstances, he would have withdrawn, feeling that something was wrong. But recently, the black knight had experienced this kind of confusion far too many times.

The fact that he had forced himself to reach out might have been an act of defiance against himself.

—I will accept your suggestion.

And the moment the black knight’s hand reached out to reap the souls of the two humans—

“I’ve been thinking about it carefully.”

A voice rang out through the air, and the black knight raised his head.

On the roof of the half-burned, half-collapsed hospital, someone stood with the sunlight shining through the dark clouds behind him.

“Ten percent is surprisingly high when you think about it. Hmm. It’s definitely higher than my chances of getting a girlfriend.”

The black knight’s eyes narrowed. It was the same energy he had sensed from afar the day before.

At last, he had come face-to-face with the owner of that immense heat.

—Who are you?

“Me?”

Swish. Tap.

It happened in an instant. A young human dropped rapidly from a dizzying height, yet landed as lightly as a leaf. Pointing at himself with one finger, he grinned.

“I’m a son of a bitch who’s disgustingly lucky.”

The next moment, the black knight saw it clearly.

The human’s finger moving toward him.

And the expression on the human’s face, from which every emotion had vanished.

“You’re, what…”

A voice cold enough to make even the dead shudder continued.

“You’re a son of a bitch who’s disgustingly unlucky.”
## Chapter artifact 398

# Chapter 398

Before attempting teleportation, a thought suddenly occurred to me.

*If I calculated the past two years as a percentage, what would it be?*

What were the odds that an F-rank Hunter, trudging up a hill after getting fired from his Guild, would find an old capsule discarded at a recycling station?

What were the odds that the old capsule would be a passage connecting to another world?

What were the odds that I would begin a second life as the Third Young Master of a frontier martial family, rather than as a member of the Nangong Family or the direct Disciple of Huashan?

And after crossing one war, two massacres, and more death lines than I could count, what were the odds that I would still be alive now…?

After considering all of that, only one conclusion emerged.

“Ten percent is enough after all.”

With that quiet mutter, I reached out.

Seizing an Object Through Empty Space.

Three jiazi of internal energy pulled Team Leader Choi and Shao Shen toward me. The Death Knights and monsters tried to move, but stopped when their leader raised a hand.

Ignoring them, I checked the two men’s condition. Their breaths were faint, and their qi was so precarious it seemed ready to vanish at any moment.

If I had taken a jet instead of teleporting, I might have been too late forever.

“I would have tried even with a one-percent chance. I’m not someone who’s going to die this pointlessly.”

Of course, I had insurance prepared in case something like this happened. I never expected to use that insurance so soon, or in a situation like this.

*Open Inventory. Summon.*

I paid no attention to the monsters watching me.

The leader watched me immediately take the necessary item from my Inventory, then asked in a flat voice,

—An extradimensional space. Have you learned magic?

*Shut your fucking trap.*

I swallowed the words hovering at the tip of my tongue. Normally, that would have been quite difficult, but it was not so hard for me now.

I did not want anyone to interfere with me. At least not right now.

Pop.

When I removed the magically sealed stopper, a faint fragrance escaped. A milky liquid sloshed inside the transparent glass bottle.

A top-grade potion.

A miraculous medicine said to heal any injury as long as the patient was still breathing.

At least right now, I had no interest in the rarity or value of this small amount of liquid—barely a hundred milliliters.

I simply felt grateful for Wu Heixing’s immense wealth and stupidity as I let the top-grade potion trickle between the lips of the patient lying there as if dead.

*Bear with it a little, Shen.*

Team Leader Choi came first. Not only because of the time we had spent together, but even if we had shared no bond until now, I would still have chosen him first.

That was how serious Team Leader Choi’s injuries were.

*This is…*

His left arm had been torn away from the shoulder. His right ankle was mangled as if something had chewed and swallowed it, while his left leg had been cleanly amputated. Seven ribs were broken, and his spine was fractured.

And…

His right hand was still twisted at an unnatural angle, yet it continued to grip the hilt of his sword.

The leather strap he had fastened tightly so he would never lose hold of it was soaked through with blood.

“……”

I silently undid the strap. I pulled the sword from his right hand, whose bones had been crushed, and set it beside him.

I did not forget to offer him a reproach in my heart.

*Why did you do this? It’s a miracle you’re still alive.*

And then a genuine miracle began.

When I carefully tilted the bottle and administered exactly half of it, a sound like something burning filled the air, and the wounds covering Team Leader Choi’s entire body began to heal.

Hissssss, hissssss—

His bones grew back, severed muscles reconnected, and his organs and flesh closed together.

His recovery was even faster than a Troll’s, the very embodiment of regeneration. As Team Leader Choi’s body recovered as if time were being reversed, color finally returned to his face.

*His qi is stable, too. This is enough.*

The result was more than satisfactory to me.

It was not satisfactory to someone else watching the scene.

—Fearless human.

—Stop immediately.

—They have been given the destiny—

—of becoming subservient to our mighty Lord.

I silently looked at the two Death Knights who stepped forward in place of their leader.

Their bodies were covered in pitch-black armor, and at a glance they looked like twins. They were similar in height, and their voices were difficult to distinguish.

There was only one obvious difference between them: the weapons hanging at their waists were different.

*One has a mace. The other has a sword.*

That was already enough to provide an answer. I had solved the question, so I could write down the answer later. Right now, it was time to solve the remaining problem.

“You’ve had a rough time too, Shen.”

Shao Shen was not as severely injured as Team Leader Choi, but he had still suffered serious wounds. I was just about to pour the remaining half of the potion into his mouth when—

—Wretched human.

—This is your final warning.

—Put down those two humans, withdraw, and beg for mercy.

—Then our Lord will take you in as a servant.

“A servant?”

—That is correct.

Along with the emotionless, flat voice, one of the Death Knights stepped toward me. The scabbard fixed to his waist swayed with every step.

Clank. Clank. Clank.

One step. Two steps. Three steps.

There was not even a hint of hesitation in the creature approaching me.

Thousands of monsters and their leader were watching.

The Death Knight spoke in a confident tone so strong that it was hard to believe he was an undead monster without emotions.

—You possess a truly great and radiant soul. Become one of us.

A great and radiant soul…

Without even raising my head, I continued pouring in the potion.

After emptying the last few drops into Shao Shen’s mouth, I closed the bottle and put it back in my Inventory.

Hissssss, hissssss.

A signal that recovery had begun.

I straightened up at the welcome sound I had been waiting for. Looking at the Death Knight, I said what I had wanted to say for some time.

“His left leg.”

—Hm?

“Team Leader Choi’s left leg. It was empty from a handspan below the knee. Completely clean. Shao Shen—the young one’s was his right arm.”

—Human. What are you trying to say?

“What am I trying to say?”

I gave him a faint smile.

“If you cut off limbs that were perfectly attached, you should be prepared for the consequences.”

And then, in the next moment—

Time was split in half, then split again within that divided instant, and before I knew it, the creature had arrived right in front of my nose.

No.

It was the opposite.

It had not come to me.

I had gone to it.

“Let’s see that vaunted skill of yours.”

—……!

Everything happened in an instant. The Death Knight tried to draw his sword, and I reached out with my left hand and pressed down firmly on the back of his hand.

That was both the beginning and the end.

Shing. Click!

The dark-gray blade had barely begun to emerge before it slid back into its scabbard—but by then, my fist had already punched through the creature’s chest.

Crunch!

The Flame-Extinguishing Divine Fist, charged with the Scorching Yang Qi of three jiazi, vaporized even the fistful of blood remaining inside the undead monster and blazed up using its long-dead body as kindling.

Whoosh! KRAAAASH!

Engulfed in inextinguishable flames, the Death Knight waved its hands and turned toward its kin.

It staggered along the path it had walked so confidently, then collapsed into ash.

—……!

—……!

Even with thousands of monsters gathered together, the silence was absolute, as if someone had pressed a mute button.

I took White Flame from my Inventory and began walking slowly.

Splash. Splash.

Everywhere my gaze fell, and everywhere my feet stepped, there were corpses and blood.

Countless rifles kept catching against my feet, while a soldier wearing a crooked helmet stared up at the sky with eyes from which life had already departed.

At least that soldier’s corpse was still intact.

In what appeared to have been the fiercest battlefield, people who seemed to be Hunters from the Public Security Armed Forces Department lay dead in mangled conditions.

I had spent a full week with the 1st Regiment led by Shao Shen. Among the corpses were many familiar faces.

*So many people died. So many.*

At least three thousand humans had died here today alone.

If all five fronts were combined, and the civilians killed in this monster wave were included, how many victims would there be?

Thud!

I borrowed the spear of an unknown Hunter and drove it deep into the ground. The leather strap belonging to Team Leader Choi, tied securely to the end of the shaft, fluttered in the wind.

Beyond it stood an army of thousands of monsters—and *him.*

> **System**
>
> Lv. 135 Death Knight Lord

Death Knight Lord. What an imposing name.

It was also a monster with enough power to match that grand name.

*The circumstances are different, but there is another one like him.*

I called out to the one who had maintained the longest silence in history.

“Let me ask you for one favor.”

I thought he might pretend not to hear me, but after a brief hesitation, the Skeleton Warlord answered.

—……A favor? You’re not asking me to fight alongside you, are you?

“Of course not.”

I had never expected that, nor did I expect it now. The favor I wanted to ask had nothing to do with fighting.

It was about protecting someone.

“Protect the two people behind me. No matter what it takes.”

With my permission, the Skeleton Warlord had been absorbing death qi whenever there was an opportunity, and had consequently grown stronger.

As a Named Monster, it should have been able to handle several ordinary A-rank monsters by itself.

“When the battle is over, I’ll grant you any wish.”

—In that case, there’s nothing I can’t do. But how long am I supposed to protect them?

“That should be obvious…”

I raised White Flame and aimed it at the Death Knight Lord.

“Until every last one of those bastards is dead.”

—You insane—

“You’re too late.”

I pulled the Skeleton Warlord’s skull from my Inventory and threw it behind me.

Crack. Pop.

While it hurriedly regenerated its body, I stroked the leather strap fluttering from the spear shaft.

How had he—how had they—felt?

What had they been thinking as they charged toward death? I could not even begin to guess.

There was only one thing I could be certain of now.

“Any bastard who comes past this spear is going to fucking die.”

The fire dragon coiled within my dantian raised its head.

* * *

CRUNCH!

Flesh and bone shattered and flew in every direction.

An ogre’s limbs were sent flying, while a Troll was engulfed in inextinguishable flames before it had a chance to regenerate.

Boom! Slash!

The head of a Lycanthrope that had bared its fangs exploded.

A Dullahan came charging at me, covered in foul-smelling brain matter, only to be cleaved in two with a single blow. The halberd, having found a new master, flew away with tremendous force and tore through a Wyvern’s wing.

CRACKLE!

—Kyaaaaaaa!

Thud-thud-thud!

A rain of blood scattered through the air.

At the same time, a streak of blue flame came flying through the rain.

Whoooooosh! Slash!

A storm of blood erupted. Whenever the flames embroidered the air, dozens of monsters fell and hundreds of monsters stepped backward.

And the thousands of monsters…

At some point, they began to be overwhelmed.

They were afraid of the death line carved by a single human with a single spear.

—L-Lord.

The flat voice of the Death Knight, which had never wavered, now contained tremors and inflection.

The black knight knew perfectly well what his subordinate’s desperate call meant.

—Make way.

Between the slits of the deeply lowered helmet, red eyes flickered.

As he advanced, leaking immense magical power, he tried to ignore the strange words and scenes that kept surfacing in his mind.

Nothing could take precedence over his creator, his eternal lord.

—Are you listening, my servant?

At the voice of his lord echoing like a hallucination, the black knight quietly replied,

—Yes, my lord.

He failed to realize it until the very end.

That his hand was groping somewhere between the plates of his armor.
## Chapter artifact 399

# Chapter 399

Whoosh!

Nothing could stop the spearhead wrapped in Force—not leather that could deflect bullets, nor flesh and bone harder than steel.

Puff, puff, puff!

The target was wide, so there was a bonus. The spearhead pierced through the Lycanthrope’s chest and skewered the ones right behind it like meat on a skewer.

—Kreuk, k-kek.

The emotion in its wide-open eyes was a mixture of confusion and indignation.

Its gaze seemed to protest: *Why me, out of all these monsters? I never crossed the death line you drew.*

“No, you did.”

With a quiet mutter, I pulled on the shaft.

Scrape, scrape. The Lycanthrope’s claws raked the ground as I dragged it over to my side of the spear.

“You crossed it. Just now.”

—……!

That was far enough. I yanked the embedded spear free at lightning speed, then swept it horizontally in front of me.

Whoosh, KRAAAASH!

Blue flames whipped through the air, scorching it as they swept forward and devoured the monsters.

The monsters that were still alive burned to death with screams, while those that had already become undead were reduced to ashes.

Ding. Ding. Ding……

System notifications announcing my kills rang out without pause.

How many had fallen from that single strike? Dozens? Or a hundred?

Rather than count every one of them, I chose to keep moving. My goal had never been to kill a certain number of monsters.

*Annihilation.*

The battle between humans and monsters—a fate of killing and being killed—had continued for decades.

Only one species would be able to survive here today, and I would not be the one to fall.

Thud.

I stepped over the spear embedded deep in the cement floor. At the same time, countless monsters retreated as if they had made a pact.

One step. Two steps. Three steps.

No matter how far I continued walking, the distance between me and the monsters did not shrink. They retreated as far as I advanced.

—This is insane……

Behind me, the Skeleton Warlord muttered as if groaning.

A single human was overwhelming an army of thousands of monsters.

Even if it was not enough to fill a page in human history, surely this was worth at least a paragraph.

—W-Where are you going?

“Keep a good eye on those two. I’m not going far anyway.”

More precisely, I no longer had any need to go far.

The guest had already arrived. There was no reason to go out and greet him.

*He’s finally here.*

My guess had been correct. The monster army split apart to the left and right like the tide going out, and ‘he’ appeared among them, riding a skeletal horse made entirely of black bones.

From far away.

Clip-clop, clip-clop.

His full plate armor was pitch-black, and a vivid red glow shone beneath his low-set helmet.

He was far smaller than a large monster like an ogre, but the mana emanating from him was immense and powerful.

> **System**
>
> Lv. 135 Death Knight Lord

Level 135. It was a number I had never seen on any monster I had faced before.

As the Death Knight Lord slowly picked up speed and approached, a thought suddenly occurred to me.

*Can I defeat him?*

My battle with the Western Heaven Demon Lord in Murim had been a desperate struggle in which I had wagered my life.

If the Western Heaven Demon Lord had intended to eliminate me from the very beginning, if the Heavenly Power Demon had not passed his internal energy to me, if I had not experienced that miraculous recovery from leveling up, if Jeok Cheongang had not awakened and saved me at the critical moment, I would have died three or four times over.

But in the end, I had survived—and grown stronger.

That was when one question began circling endlessly in my mind.

*How strong am I now?*

The System said that my martial arts realm and stats had risen.

I had distributed my stats and fought battles just as I always had, but aside from the existence of Force, I wasn’t sure.

I had no real sense of how much stronger I had become.

At some point, it had all become easy and natural.

And now—

Tap-tap, thud-thud-thud!

As I watched the Death Knight Lord shoot toward me like a gust of wind, I realized it.

I remained unshaken by the immense mana pouring from his entire body like a waterfall. That alone told me.

*I am……*

Whoooooosh!

The wind vanished, and a flash of light filled its place. The sword held in the Death Knight Lord’s hand moved as he charged in together with his skeletal horse.

The sight of thick darkness gathering and crashing down seemed to unfold in slow motion. A single certainty surfaced in my mind.

*I am stronger than anyone else on this battlefield.*

In the slowed-down world, I thrust out White Flame.

Blue-white flames surged up along the spearhead and devoured the darkness.

* * *

A roar like the sky splitting apart rang out.

KRAAAASH!

The ground within a radius of several hundred meters caved in, and the hospital that had stood firm for decades collapsed.

Compressed air exploded layer after layer like a sonic boom, striking and hurling away everything around us.

And at the center of it all stood two beings whom no one else could approach.

Whoosh, whoosh-whoosh-whoosh! KABOOM!

Several times, or perhaps dozens of times, in the blink of an eye.

Every time the blue-white flames and pitch-black darkness collided and mingled, deafening roars and terrible destruction followed.

No human or monster could see the movements of the two beings.

They existed on a higher plane, clashing within a world and time of their own.

Swish!

The silver-white spear in Jin Taekyung’s hand slashed downward through empty space.

Blue-white flames poured down, tearing through space. But the black knight did not retreat. He swung his sword.

KABOOM!

The moment the surging mana collided with the flames, the resulting pressure shattered the black knight’s skeletal horse into pieces.

But the disappearance of Nightmare—a loyal warhorse and an A-rank monster—was nothing compared to what was about to happen.

Whoooooosh!

A thrown spear without any preparatory stance. A flash of light itself.

The black knight twisted his body with an instinctive movement. Tremendous heat grazed his chest and burrowed into the monsters behind him.

KRAKAKAK! KABOOM!

When the spearhead that had pierced through dozens of monsters slammed into the ground, a massive crater formed with a thunderous roar.

Before the monsters caught in the aftermath could even let out terrified screams, Jin Taekyung was already moving toward the black knight.

Sshk.

A single step without sound or presence.

By the time the black knight noticed, Jin Taekyung had erased dozens of meters and reached his target. His fist shot toward the black knight’s chest.

“Get lost.”

—……!

Boom!

Flame-Extinguishing Divine Fist. Heat hotter than lava slammed into the armor.

The black knight was flung away at tremendous speed, but he flipped his body in midair and regained his balance. At the same time, his hand seized the hilt of his sword and swept it out with force.

Whoooooosh! Shh-shh-shhk!

Black mana became dozens of lightning bolts and shot toward Jin Taekyung. Every one of the attacks possessed earth-shaking power.

But Jin Taekyung was no longer there.

KRAKABOOM!

Jin Taekyung charged through the cloud of pale dust and extended both hands.

The sword blade, which had changed direction and was now slashing down toward the crown of his head, was caught between his hands as if he were pressing his palms together.

Empty-Hand Seizes the Blade.

His blue-flame-wreathed hands and the blade laden with immense mana trembled between the two beings.

The one who blocked, and the one who advanced.

The fierce confrontation that had briefly halted their relentless exchange was broken by the arrival of an unexpected intruder.

—You, human!

It was the moment a Death Knight appeared with a shout and brought a mace down toward Jin Taekyung’s back.

Boom!

The Death Knight did not even know when or how he had died.

Jin Taekyung’s heel had sliced through the air like a blade and blown apart his head, helmet and all.

Thud.

But even if it had been a futile death, the attack had not been entirely meaningless.

The black knight’s red eye-light flashed, and the sword in his grasp unleashed more mana than ever before.

A gap no wider than a hair.

The instant Jin Taekyung had diverted his internal energy to kill the Death Knight was enough to break the balance.

Crunch! Slash!

Blood gushed out.

It was a shockingly red spray of human blood—the proof that the black knight’s sword had cut across Jin Taekyung’s chest.

A single certainty flashed through the black knight’s mind.

*It’s over.*

And in the next moment, Jin Taekyung’s fist, engulfed in flames, slammed into the black knight’s side.

* * *

Crack!

—……!

The Death Knight Lord’s body jerked.

As befitted an undead monster incapable of feeling pain, he made no sound, but I read the question in the red glow visible between the slits of his helmet.

*How?*

Yes. That was exactly the look in his eyes.

I answered in a flat voice.

“You think you’re the only one with armor?”

Boom!

This time, it was the Flame Divine Palm.

The Death Knight Lord’s armor, already cracked from the repeated blows, broke apart into fragments before my eyes.

“That hurt, you son of a bitch.”

Crack!

I twisted the wrist of the bastard wearing the gauntlet and broke it just like that.

I had no idea how meaningful attacks like these were against an undead monster, but they were enough to make him drop his sword.

Clank.

As the sword fell with a metallic sound, the Death Knight Lord was met with a merciless assault.

Boom! Crack! Bam!

I stepped on his instep and threw punches without pause.

Shoulder. Arm. Side. Chest.

The Death Knight Lord took dozens of attacks in an instant. He attempted a counterattack, but it did not matter.

Thud!

—……?

“Don’t be surprised. My armor’s pretty useful too.”

I had the Fire Dragon Armor.

*I’m using this here.*

The Fire Dragon Armor was a divine weapon I had obtained after defeating the Western Heaven Demon Lord.

It had been damaged so severely during the battle in Murim that it was still repairing itself, but even at a restoration rate of around fifty percent, it had more than done its job.

*Though I almost died because it couldn’t block everything completely.*

When the sword cut me, my vision had swum too.

But I had suffered this much pain more times than I could count.

Besides, it was nothing compared to the pain endured by those who had died before me.

“This is…for the people you killed today.”

I put all my strength into punching him in the face.

A Flame-Extinguishing Divine Fist at the eighth level smashed apart the helmet that had withstood everything, revealing his face.

The balance had tipped. One blow. One final strike would be enough to take his life.

“And this is……”

At that moment, my raised fist stopped dead.

I blinked through eyelids clotted with blood. For just an instant, time seemed to stop when my gaze landed on someone’s face.

A face that was unfamiliar, yet familiar.

With dead-white skin and red eyes, he looked exactly like a certain hero I had seen in a hologram video.

“……Lei Fei?”

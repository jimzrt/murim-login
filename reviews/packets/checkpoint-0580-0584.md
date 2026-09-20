# Checkpoint Review — 580–584

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

# Chapters 580–584

## Plot

Go Se-won discovers that Go Jun used an S-grade Magic Gem to trigger the Busan Monster Wave and sent Kim Ho-jung to Busan separately. Go Jun forced Song Cheonwoo to attack Choi Minwoo by holding Song’s family hostage. Song falls into an abyss and is killed by an unidentified monster, while the unused object in his pocket releases darkness that becomes light.

The Yeti’s Winter Range Gate in Pyeongchang tears open into the modern world. A gigantic Behemoth emerges, destroys the control station, devours hundreds of yetis, and paralyzes witnesses with Fear. Choi’s Hero’s Soul breaks the effect, and he, Kim Hwajong, and Peace Guild Hunters confront the monster to protect more than a thousand civilians. Behemoth kills more than half the force. Choi severs two of its four forelegs before collapsing, while Hwajong loses his left arm rescuing him and orders the survivors to evacuate with Choi.

Hwajong remains behind and uses Hell Fire and Flame Cannon to destroy Behemoth’s wounded forelegs, forcing it to kneel. The monster then hurls him into solid rock and gravely injures him. His memories reveal his recruitment by Cheon Taemin, his service as Butler Kim and Peace Guild Guild Master, and his role in raising Minwoo after his parents’ deaths. As Behemoth prepares to consume him, an unexplained flash erupts from midair.

Meanwhile, in Busan, the narrator exterminates the remaining Mermen and finds a murdered family, deepening his rage. A broadcast reports Choi’s involvement in the Pyeongchang Monster Wave as the narrator continues toward the surviving civilians.

## Continuity

- Go Jun artificially caused the Busan Monster Wave with an S-grade Magic Gem and sent Kim Ho-jung to Busan.
- Song Cheonwoo was forced to attack Choi Minwoo because Go Jun held Song’s family hostage. Song died after falling into an abyss and being crushed and drained by an unidentified monster.
- The unused object Song carried released darkness that became light; its identity and effect remain unknown.
- Behemoth emerged from the Pyeongchang Yeti’s Winter Range Gate, can speak Demon Realm language, emits Fear, and remains hungry.
- Behemoth killed more than half of the twenty-two Peace Guild Hunters. Choi Minwoo is unconscious after injuring it, and the surviving Hunters evacuated with him.
- Kim Hwajong lost his left arm while rescuing Choi, then stayed behind. He disabled Behemoth’s two wounded forelegs but was gravely injured; his survival after the final flash is unresolved.
- Cheon Taemin recruited Hwajong alongside Jungryong and Cheonwoo. Hwajong later became Butler Kim, raised Minwoo, and served as Peace Guild Guild Master.
- The narrator has cleared Busan of the Mermen and continues searching for survivors.
- Cheon Taemin’s collapse, his more than twenty years of unconsciousness, and the suspected Area A connection remain unresolved.

## Translation Decisions

- Use **Monster Wave**, **Yeti’s Winter Range**, **Behemoth**, **Behemos**, **Hero’s Soul**, **White Flame**, **Fire Dragon’s Single Tail**, **Flame Divine Palm**, **Hell Fire**, and **Hellfire Mage**.
- Use **S-grade Magic Gem**, **Named Monster**, **Guild Master**, **Young Master**, and **Butler Kim**.
- Preserve the distinction between **Hell Fire** as a spell and **Hellfire Mage** as a title.
- Render **형님** as **hyung** and retain the **COVID/Merona** wordplay with its explanatory footnote.
- Keep the narrator’s brutal, grief-stricken first-person register during the Busan massacre and discovery of the dead family.

## Durable state

{
  "active_continuity": [
    "Song Cheonwoo says Cheon Taemin suddenly collapsed more than twenty years ago and has remained unconscious, but no one knows why.",
    "Song Cheonwoo and Lee Jungryong concealed Taemin's condition, waited two years, conducted experiments, and purged aides who knew the truth.",
    "Hwa-jong was not told about Taemin's condition and remains loyal to Choi Minwoo.",
    "Song claims Taemin is still alive, but his location is unknown and Area A is only suspected.",
    "Choi Minwoo has confirmed Song's account enough to treat Taemin's status as genuine while continuing to investigate.",
    "Busan's Kraken has been eliminated, but more than one thousand Mermen remain across Haeundae and Gwangalli while the Peace Guild and other forces contain the disaster.",
    "Go Jun seized Song Cheonwoo's children as leverage and used the threat to force Song to attack Choi Minwoo.",
    "Go Jun used an S-grade Magic Gem to artificially cause the Busan Monster Wave and sent Kim Ho-jung to Busan.",
    "Go Jun intends to kill Choi Minwoo through Song Cheonwoo and may be relying on another unidentified being.",
    "Song Cheonwoo was killed after falling into an abyss and being attacked by an unidentified monster; the unused object in his pocket released darkness that became light after his death.",
    "Kim Hwajong forced Behemoth to kneel by disabling its two forelegs, but Behemoth gravely injured him while Choi Minwoo escaped; a flash from midair interrupted the monster's final attack."
  ],
  "continuity_sources": [
    584,
    583
  ],
  "open_questions": [
    "What caused Cheon Taemin's collapse, and what happened during his more than twenty years of unconsciousness?",
    "Is Cheon Taemin actually being kept in Area A of Ares Guild headquarters?",
    "What is the unidentified being involved in Go Jun's plan, and is it connected to the monster that killed Song Cheonwoo?",
    "What was the object Song Cheonwoo kept unused in his pocket, and what did its release of darkness and light accomplish?",
    "Did Choi Minwoo and Kim Hwajong survive the Pyeongchang confrontation, and what caused the final flash?"
  ],
  "safe_through": 584,
  "temporary_decisions": [
    "Use Yeti's Winter Range for 예티의 겨울 산맥, Behemoth for 베히모스, and Behemos for 베헤모스.",
    "Use Stone King for 스톤 킹 and Skeleton King for 스켈레톤 킹.",
    "Use Area A for A구역.",
    "Use Hwa-jong for 화종.",
    "Use Hero's Soul for 영웅의 혼, Hyung for 형님, S-grade Magic Gem for S급 마정석, Hell Fire for 헬 파이어, and Hellfire Mage for 겁화의 마법사."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 580

# Chapter 580

The shocking news that a Named Monster called the Kraken had landed in Busan, leading thousands of Mermen, spread quickly.

And Go Se-won was one of the few people who had received the information before the breaking news even appeared.

*A Monster Wave…*

He was human, too. Busan was a major city with a population approaching five million. He did not even know those people, but the thought of countless civilians being sacrificed still left a bitter taste in his mouth.

*At least Jin Taekyung is there.*

*Step. Step.*

Guild members moving through the headquarters hurriedly cleared a path when they saw Go Se-won.

He passed them at a brisk pace and muttered in a low voice,

“Security Team. Respond.”

*Beep.*

A faint mechanical sound came from his earpiece, followed by immediate replies.

—Team Three. Transmission complete.

—Team Two. Transmission complete.

—Team One. Transmission complete.

“I’m going to see a VIP. Open Area A and report your current locations and personnel.”

Go Se-won intended to obtain his superior’s permission to deploy the security teams to Busan.

It was partly to rescue people, but it would also help repair Ares Guild’s recently shattered image.

However, his brow gradually furrowed as the team leaders reported in one after another.

—All of Team Three are monitoring the target’s family in London.

—Team Two has returned from London and is waiting in Area A of headquarters.

—Team One currently has nine members. We returned from London and are waiting on the hundredth floor of headquarters.

“Team Leader of Team One. Say that again. What did you say?”

—Team One currently has nine members. We are waiting on the hundredth floor of headquar—

“Forget the rest.”

Go Se-won stepped onto a magic circle as he spoke in a quiet voice.

*Whoosh.*

A flash of pure white light signaled the activation of the Teleport spell, and he moved to Area A.

“Why are there nine instead of ten?”

—Because an urgent matter came up.

“An urgent matter. Who is missing?”

—Kim Ho-jung.

“Kim Ho-jung?”

—Yes.

Listening to the Team Leader’s dry voice, Go Se-won crossed the hallway in Area A. His mood soured with each sharp click of his dress shoes.

“That’s strange. I don’t remember receiving any report.”

—My apologies.

“I’m not asking for an apology. I’m asking for the reason. Did he leave without permission?”

—Of course not.

*Of course not.*

Go Se-won muttered inwardly.

The security team was a pack of hunting dogs raised by the dead Lee Jungryong.

For a long time, Lee Jungryong had secretly operated enormous orphanages and children’s homes, instilling loyalty in orphans who had nowhere else to go.

He had been the same way. So were they.

And Team One consisted of only the most loyal and capable members. The odds of a member of Team One going AWOL were even lower than the odds of a Monster Wave.

Especially someone like the missing Kim Ho-jung.

*Which meant…*

Ares Guild had many senior executives and elders, but the security team obeyed the orders of only two people.

The fact that Kim Ho-jung had disappeared without reporting to Go Se-won, one of those two people, could mean only one thing.

*Step.*

His unimpeded stride came to an abrupt halt.

Go Se-won silently stared at a door with no nameplate or decoration when a bright voice rang out from beyond it.

“Come in. Don’t loiter outside.”

“...!”

Swallowing hard, Go Se-won opened the door and entered. In the neatly arranged room, his sole direct superior was waiting for him.

“Nice weather today. Don’t you think so, Team Leader Go?”

“Yes.”

Go Se-won gave a brief bow, then quickly swept his gaze around the room.

The pleasant smile at Go Jun’s lips. The whiskey glass in his hand. And the object he was rolling around in his other hand.

*What is that?*

This was not the Go Jun he usually knew. Everything in the room felt strange and unsettling to Go Se-won.

Perhaps it was because of the noise drilling into his ears.

*Grind. Grate.*

Go Jun’s voice blended with the irritating sound of friction.

“You don’t need to worry about that Kim Ho-jung fellow, Team Leader Go. I gave him a separate assignment.”

“I see.”

“Aren’t you curious what kind of assignment it was?”

Their gazes collided in midair. Looking into Go Jun’s unusually red eyes, Go Se-won politely lowered his head.

“No. If it was the Vice Guild Master’s order, I’m sure there was a good reason.”

“That’s a nice answer to hear. I thought you’d been feeling a little hurt by me lately. I’m younger than you, after all, and you were always especially devoted to Master.”

“How could that be? It’s true that I owed a debt to the former Vice Guild Master, but that does not lessen my loyalty.”

“Is that so? Then that’s a relief.”

*Grind.*

Go Jun rubbed the object in his grasp once more, then smiled pleasantly and swirled his glass.

“The weather is nice. How about a drink?”

Go Se-won answered calmly.

“I’m sorry, but…”

“You mean you won’t drink? What a shame. It’s good liquor.”

Go Jun leisurely emptied his glass. Go Se-won watched him in silence before suddenly speaking.

“There is an urgent matter I need to report.”

“Go ahead.”

“In Busan…”

Go Se-won trailed off the moment he saw the holographic PC sitting on the table where Go Jun had set down his glass.

The paused screen showed an enormous octopus and the devastated remains of Gwangan Bridge.

“In Busan, what?”

“…”

After a brief silence, Go Se-won murmured,

“You already knew.”

Go Jun let out a low laugh.

“I did. Before anyone else.”

The bright voice had not changed, but Go Se-won felt his heart sink.

As the unease he had tried to dismiss revealed its true shape, he forced himself to speak calmly.

“Then Kim Ho-jung… Is he in Busan right now?”

“I seem to remember you saying you weren’t curious a moment ago.”

“I’m sorry. It slipped out.”

“Forget it. You need to know, anyway.”

Go Jun answered pleasantly as he filled his empty glass with whiskey.

“That’s right. Kim Ho-jung is in Busan on my orders.”

After thinking for a moment, Go Jun added,

“He might be gone by now.”

“...!”

“Don’t just stand there. Sit down and have a drink. My neck hurts from looking up at you.”

This time, Go Se-won could not refuse. No—there was no reason to refuse.

He needed to drink, if only to calm the turmoil raging inside him.

*Gulp, gulp.*

He downed the strong whiskey in one swallow, and only then did he feel as if he could breathe again.

Clutching the empty crystal glass, Go Se-won hesitated before barely squeezing out his voice.

“Vice Guild Master. I don’t know how you managed to make something like this happen, but this method cannot inflict much damage on them.”

“Why do you think that?”

“He… No, Jin Taekyung is there. He’s the man who even took down an Arch Lich. He’s already suppressing this Monster Wave quickly. All this will do is add to the Peace Guild’s reputation.”

“Yes. That’s right. Jin Taekyung. He really is something.”

Go Se-won had brought up the name despite knowing he might provoke his superior’s anger. Yet contrary to his expectations, the smile remained on Go Jun’s lips.

And that gentle smile made Go Se-won feel even more uneasy.

“Vice Guild Master. Don’t tell me…”

“If you want to capture the commander, you have to lure out the general. It’ll cause an uproar if this becomes known, but there won’t be any consequences afterward.”

“...!”

“Jin Taekyung is untouchable for now. But Choi Minwoo is a different story. Don’t you agree?”

*Grind. Grate.*

Along with the irritating sound of friction, one name flashed through Go Se-won’s mind like a bolt of lightning.

“Song Cheonwoo. It’s Song Cheonwoo.”

“Correct. I’ll give you another drink as your reward.”

Go Se-won accepted the drink, hiding the trembling of his fingertips. He could not begin to estimate where things had gone wrong.

Even so, he was certain that his superior’s plan would fail.

“…Choi Minwoo is a cautious man. On the surface, he is the master of the Peace Guild, and he also has Kim Hwajong, who has served him loyally at his side for a long time.”

“I know. Master mentioned Kim Hwajong several times. And if we include the other security personnel, Song Cheonwoo couldn’t handle it alone.”

“Vice Guild Master. Then why in the world—”

*Graaaate!*

The loud sound of friction drowned out Go Se-won’s voice.

Instead of answering, Go Jun let out a short laugh and opened his palm. The object he had been clutching all along finally revealed itself.

It was about the size of an egg, filled with darkness that looked as though it had gathered an abyss and sealed it inside. Its name slipped from Go Se-won’s lips.

“A Magic Gem…”

He would not have been surprised if it had been an ordinary Magic Gem.

But the object resting on Go Jun’s palm could only come from a Named Monster. It was what people called an S-grade Magic Gem.

Pure, unrefined mana churned inside it.

“V-Vice Guild Master.”

Only now did Go Se-won understand how Go Jun had been able to cause the Monster Wave artificially.

At Go Se-won’s voice, filled with both dread and lament, Go Jun muttered quietly,

“Choi Minwoo. That man will die today. Without fail.”

And the one who killed Choi Minwoo would be one of two things.

An old man whose family had been taken hostage.

Or another being whose identity even Go Jun himself could not clearly determine.

“One thing is certain. Song Cheonwoo has no choice.”

Go Jun murmured softly and smiled with satisfaction.

As he habitually stroked the old necklace around his neck, darkness flickered in his eyes.

* * *

If someone asked how Song Cheonwoo had managed to move in such a serious physical condition, he would answer with one word.

Will.

That was exactly what it was. The last strength he had dragged up through sheer willpower. The nearly seventy-year-old man threw himself toward death with every ounce of strength he had left.

*Flash! Whoosh!*

The world slowed.

The cold sensation of snow disappeared, replaced by a buoyant feeling that seized his entire body.

In that brief moment, split and split again into fragments, Song Cheonwoo met the wide-open eyes of two people staring at him.

Choi Minwoo and Kim Hwajong. Their eyes seemed to ask the same question.

*Why?*

Song Cheonwoo muttered an answer to the question in their hearts.

*Because this is the only way.*

If it had been a few days ago, he probably would have taken Choi Minwoo’s hand.

But Go Jun, whom he had faced for the last time, had become… a monster.

Song Cheonwoo had sensed madness in his eyes. If Song Cheonwoo left this place alive, Go Jun would eliminate his family without the slightest hesitation.

Neither the Peace Guild, nor even Jin Taekyung or *that person*, could resolve that problem.

*So this is how it ends, in the end.*

Along with that fleeting thought, Song Cheonwoo fell toward the pitch-black darkness.

The darkness had no end in sight. It resembled the mouth of a monster.

It also resembled his life.

*Was it Nietzsche?*

Someone had said that if you stared into the abyss, you became the abyss as well.

Song Cheonwoo realized that too late.

By then, everything was already too late.

*SHWAAA!*

A cold, savage wind battered his entire body.

Amid the howl of the vicious wind, a conversation he had shared with someone a few days ago seemed to press into his ears.

*“This.”*

*“Put it away. As you know, Director, it’s an extremely dangerous object. It’s expensive, too.”*

*“…You bastard. You’re insane.”*

*“You need to be insane, too. If you want to save your family.”*

The man had been insane, and it had been an insane conversation.

And after agonizing over it for what felt like ten years in a single day, Song Cheonwoo had not used *it* until the very end.

*Was that the last thing I did right?*

As the wind grew more violent, Song Cheonwoo sensed something approaching through the darkness and closed his eyes.

*Crack! Crunch, crunch, crunch!*

The end of his long fall.

First, his neck broke. Then every bone in his body was crushed.

And in the next moment, Song Cheonwoo heard the cry of something through his fading consciousness.

—Grrrr.

It was the eerie cry of a monster unlike anything he had ever heard before.

He wanted to say something, but the being that had crouched in the abyss for countless years did not allow its prey any last words.

*Crack!*

Darkness came.

Enormous teeth crushed the body from which life had already fled and drank its blood.

Even the object Song Cheonwoo had kept deep in his pocket—something he had never used until the end because he wanted to die as a human being, not as a monster.

*Whoosh.*

The darkness itself became light and burst forth.
## Chapter artifact 581

# Chapter 581

*Whump! BOOM!*

A whip of fire lashed the ground. The snow that had piled up melted, and the yeti blood began to boil. A voice that sounded as if it were chewing out the words spilled through Kim Hwajong’s clenched teeth.

“Song Cheonwoo, you fucking bastard…”

The old butler’s widened eyes were fixed on the place where someone had been lying only a few seconds ago.

If this was how it was going to end—if that bastard was going to meet a death like this—Hwajong should have killed him with his own hands. But Song Cheonwoo had summoned the last of some unknown strength, thrown himself into the deep crevasse, and met the death he had chosen for himself.

A traitor had received a far too generous end.

And what was even more regrettable was…

“We’ve lost an important witness. I’m sorry, Young Master.”

“No.”

Choi Minwoo shook his head at Kim Hwajong’s sigh-like murmur. His gaze remained fixed on the crevasse whose depth could not be estimated.

“You have nothing to apologize for, Butler Kim. It was my fault for failing to be more careful.”

Victory dulled one’s vigilance. Perhaps it was even more understandable after such a difficult battle. Choi Minwoo poured the potion—less than a quarter of which had been used—over his body.

*Hiss.*

The sound of flesh burning filled the air as his wounds began to close little by little. Feeling a faint pain, he continued.

“Song Cheonwoo must have thought this was the only way to save his family.”

“…”

“I understand his situation, but… he must have been more desperate than we realized.”

Kim Hwajong muttered in a rough voice.

“What a damn fool. There wasn’t even any guarantee his family would survive just because he did this. Why the hell would he…”

“He must have been that afraid. Isn’t clinging to hope even in the middle of despair what makes us human?”

Choi Minwoo answered in a low voice, then took his eyes off the crevasse. He did not know its exact depth, but the drop had to be hundreds of meters at the very least. Song Cheonwoo had already been on the verge of death. The odds that he had survived the fall were close to zero.

“We should call the Guild members. No—it would be faster to order the Guild House to dispatch personnel.”

The two men had been together for more than twenty years. Kim Hwajong immediately understood what Choi Minwoo intended.

“You mean to recover the body?”

“I don’t know if it will be possible, but we should at least try. Song Cheonwoo is still Ares Guild’s European regional branch director.”

Even if he had stopped breathing, his status remained. If they could prove even half of what had happened here, the repercussions would extend beyond Ares Guild’s iron fortress and shake Go Jun to his core.

“Attempted murder, murder-for-hire—whatever it is, it will be a disgrace that even Ares Guild’s Vice Guild Master cannot escape. Especially in a situation like this.”

A fortress built through decades of effort did not crumble easily. But Go Jun was different. Choi Minwoo intended to use every bit of power at his disposal to unseat him as lord of that fortress.

“From now on, we’ll be busier than ever. Both you and me, Butler Kim.”

Kim Hwajong smiled proudly.

“I’ve been waiting for this day.”

“I’m glad. That you’re always at my side.”

“You should put me to work before I get any older, Young Master. We have to make that bastard Go Jun regret starting this whole fucking mess.”

“That’s exactly what I intend to do.”

Choi Minwoo nodded and began walking away from the crevasse. Whether it was because of the fierce battle with Song Cheonwoo or the considerable amount of blood he had lost, fatigue swept through his entire body and weighed down his steps.

Then, as his consciousness gradually grew hazy and he retraced the path he had taken, Choi Minwoo came to an abrupt stop.

*Splash.*

Muddy water mixed with snow and blood sprayed around him. Kim Hwajong, who had been following behind him, asked in confusion,

“Young Master?”

Choi Minwoo did not answer. He silently stared down at his foot, half-submerged in a puddle of murky water, then suddenly muttered,

“Regret.”

“Pardon?”

“You said that earlier, Butler Kim. That we needed to make Go Jun regret starting this whole mess.”

“I did, but is something wrong…?”

“You left out the ‘why.’ The question of why Go Jun started this whole mess.”

Choi Minwoo looked down at the puddle and thought.

One step was enough to make the muddy water splash and send ripples across its surface. So why had Go Jun sent Song Cheonwoo—a member of Ares Guild—to assassinate him?

Because Song Cheonwoo was exceptionally skilled?

Or because he was a traitor?

Both were wrong.

This was…

*A trap.*

The word flashed through his mind like a bolt of lightning. Choi Minwoo’s body began to tremble.

It was not from the shock of his realization. It was even less due to the fatigue that had seized his entire body.

No. His body was not the only thing that had been trembling from the beginning.

*Rumble…*

Another ripple spread across the puddle that had slowly fallen still, and a mass of half-melted snow collapsed. The earth was shaking.

As the entire snow-covered mountain trembled, terrified yetis cried out from all around. And at the center of it all was an enormous rumble.

*Crack—RUMBLE, RUMBLE!*

Choi Minwoo and Kim Hwajong turned around at the same time, as if they had planned it.

The ground split apart like a spiderweb amid a tremendous vibration. The cracks in the earth, connected like threads, reached the darkness behind them.

*Crack! Crack-crack-crack!*

A crevasse.

An enormous darkness whose end could not be seen opened its jaws. Darkness poured from the widening gap.

No—the force flowing from it was powerful mana.

It shook the snow-covered mountain and tore through space-time.

*SHWAAAA!*

And the two men saw it.

Beyond the split in space lay an endless blue sky and buildings.

The world they had lived in—and the world they were supposed to continue living in.

“…Monster Wave.”

Two worlds that touched but should never have been connected had become linked. A roar announcing the beginning of the disaster reverberated in every direction.

—GRAAAAAAAH!

Facing the abyss as it finally revealed itself, Kim Hwajong stepped in front of his young master, his gaze darker than ever.

*Step.*

A snowstorm swept around them. Stained black by mana, it was no longer white.

Nor was it beautiful.

* * *

“Team Leader, how about a drink?”

The team member approached with a soju bottle in hand and an easygoing grin. The Team Leader answered brusquely,

“No, asshole.”

Despite his words, his glass was already being raised ever so slightly. The team member grinned as if he knew everything and filled the empty glass.

*Glug, glug, glug.*

The Team Leader tossed back the soju in one gulp, then dipped a piece of flounder sashimi deep into the spicy-sweet dipping sauce and swallowed it. The chewy texture lifted his mood, if only a little.

“…Shit. At least it tastes good.”

“Right? This place is famous in the Hunter community.”

“Really?”

“Yeah. There are tons of reviews if you search for it. They say it’s the best place to have a drink after finishing a raid.”

“Of course it tastes good to those people. They probably picked up Magic Gems by the handful after their raids. It’s not like any of them came up empty-handed like me.”

“…Oh, boy. Here he goes again.”

The Team Leader smacked his lips.

If he had belonged to a Guild, it would not have mattered whether he struck out on a raid or spent the day swinging a bat. But as the leader of a freelance Hunter team, it was different. Even if he had to dig into his own pocket, he had to pay the daily wages of the people laughing and chatting around him.

Including this shameless bastard who had come over to him.

“Team Leader. You’re not angry, are you?”

“Forget it, punk. Pour me another.”

“Yes, sir.”

The team member gave a sharp salute and began pouring. The Team Leader let out a quiet laugh, then turned his gaze beyond the railing.

The raid had fallen through, but drinking while looking out over the snow-white landscape after the recent snowfall was not so bad.

*Pyeongchang really does have beautiful scenery. The scenery, anyway.*

Well, that was probably why they had built so many ski resorts around here.

The Team Leader murmured inwardly, emptied his glass again and again, and took in the view around him. The countless people who had come to the ski resort today and the gondolas constantly traveling up and down the mountain showed just how little common sense those people had.

“Hey. Isn’t this funny?”

The team member, who had been devouring sashimi with great enthusiasm, looked up.

“What is?”

“There’s a Gate sitting right on top of the mountain, and mana has increased by seven percent, but those people are still doing this shit.”

And when he had come down and checked, he had heard that a Monster Wave had broken out in Busan below. The Team Leader shook his head.

“Come to think of it, there were idiots who went skiing even when COVID broke out when I was young.”

“Merona?”[^1]

“…Never mind. Just keep stuffing your face.”

The Team Leader let out a deep sigh and emptied his glass again. His chest was beginning to feel tight as he thought about what must be happening in Busan.

“Uh—uh-oh! Oh, whoa! Whoa, whoa, whoa!”

“What now?”

“…Why is she doing that again?”

At the sudden outburst, every gaze around them—including the Team Leader’s—turned in the same direction. A female Hunter in her twenties, who had been thinking hard about something for a while, was shaking her smartphone like a madwoman.

“Wow! No way! This is insane!”

The Team Leader answered with a worried expression.

“Yeah. It certainly seems that way.”

“No, not that! I told you earlier, didn’t I? I thought I recognized that masked, incredibly handsome guy up there!”

The Team Leader recalled the group of Hunters he had encountered earlier, especially the young man walking at the very back.

“Yeah, you did. Thanks to those people, we came up empty-handed on today’s raid.”

“But it’s him! Wow, this is incredible. Kim Sohye, is your eye for faces really this good? How did you recognize him?”

“I’m going to lose my mind if I keep listening without knowing what you’re talking about, so could you please explain?”

“Look at this! Look at this!”

The Team Leader frowned when she thrust the smartphone right in front of his face. Then he saw the face on the screen and his eyes widened.

“What the hell? Is this for real? They do look alike, I guess…”

“I told you! Don’t you trust me, Team Leader?”

“No.”

“Ah, damn it! This time I’m certain, so believe me! I’ve got an eye for this that I honed through thirty years of idol fandom!”

“You’re twenty-five. Did your father do the idol fandom for you?”

“Anyway, I’m right! If I’m wrong, you don’t have to pay me today!”

A slave to capitalism was betting her daily wages.

Only then did the Team Leader begin to believe her. And he grew curious, too.

*If this is true… why would someone of this stature come all the way here?*

A brief article was displayed on the smartphone alongside a face handsome enough to pass for a celebrity.

> **Peace Guild Team Leader Choi Minwoo:** “Emergency Rescue Teams Are for Everyone”

A big shot.

An extremely big shot.

The Team Leader had not gotten a proper look at his face, but even in the photograph, the calmness in his eyes and his distinctive air seemed similar.

*If this is true, then the other Hunters must all belong to the Peace Guild, too.*

Choi Minwoo had become famous enough recently that the Team Leader had heard about him several times. But even if only half of those stories were true, the man should have been too busy to breathe. Why would he lead his Guild members to a B-grade Gate in Pyeongchang?

*Wait. Then what about that older man I saw coming down earlier?*

The thought had barely reached that point when—

*RUMBLE, RUMBLE, RUMBLE!*

A tremendous vibration began to sweep through the area. For an instant, every sound fell silent, and everyone turned their heads in the same direction as if they had planned it.

The first person to notice the anomaly was the Team Leader.

His gaze had already been fixed on that spot before the vibration began.

*…That place…*

The location he had climbed toward full of expectations, only to descend from in vain.

The B-grade Gate known as Yeti’s Winter Range.

The next moment, what appeared in the Team Leader’s widened eyes was part of the mountain slowly collapsing, with pitch-black darkness settling over it.

Amid the gondolas and buildings crumbling to pieces, a horrifying roar that shook the mind rang out.

—GRAAAAAAAH!

A Monster Wave.

And the people still inside the Gate.

Overcome by suffocating terror, the Team Leader forced out a voice he had barely managed to squeeze together.

“Report it! Right now!”

A frightened question came back.

“W-where?”

“The Hunter Association, the Peace Guild, Jin Taekyung—anywhere! Right now!”

[^1]: Merona is a Korean melon-flavored ice cream bar; its name echoes “Corona” in the original wordplay.
## Chapter artifact 582

# Chapter 582

What should this be called?

Choi Minwoo, Kim Hwajong, and the twenty elite Hunters from the Peace Guild guarding the Gate from outside.

They all shared the same question, but no one could answer it. No—they couldn’t answer it.

All they could do was stare at *it*, which had arrived in the modern world, with bewildered expressions.

—GRAAAAAAAH!

A thunderous roar shook the sky.

It was a hippopotamus, an elephant, an ox, and a rhinoceros all at once. And yet it was none of those things.

It was simply too enormous and powerful to be called a beast.

*Whoooosh. CRUNCH!*

One step.

But the impact was tremendous.

A huge foreleg crushed the Gate control station beneath a shadow that covered more than ten meters around it.

The ground shook as if an earthquake had struck. The cable lines running down toward the foot of the mountain snapped, and a gondola came crashing down.

And in the next moment, Kim Hwajong recalled the name of a monster from a distant memory.

“…Behemoth.”

Behemoth. Or Behemos.

The name of a monster derived from the Hebrew word for “beast.”

Traces of the mythical monster that had risen from a deep, dark abyss could even be found in the Bible.

> Look at Behemoth. Just as I made you, I made it too.
>
> It grazes grass like an ox.

But the record written in the Bible was wrong.

Kim Hwajong did not know what kind of being had created that monster, but Behemoth was far removed from a peaceful creature that grazed on grass and drank water from ponds.

*CRUNCH! CRRRUNCH!*

—Kwooh! Kwoooooh!

Behemoth was not the only thing to emerge from the Gate and enter the world.

More than two hundred yetis fled, their cries sounding like screams.

Behemoth’s first target was them.

The enormous creature mercilessly trampled and devoured the creatures that were both its kind and its subordinates.

*SHAAK! Thud-thud-thud!*

Blue blood fell like rain.

Four legs like the pillars of a temple stamped across the earth. Every time tusks resembling an elephant’s ivory scraped across the ground, severed limbs and blood burst from the monsters beneath them.

A trembling voice escaped between someone’s lips.

“T-This is…”

The sight alone was enough to inspire despair.

Everyone stood frozen, watching the yeti horde meet a gruesome death with vacant eyes.

Then—

*FWOOOOSH!*

Beyond the black mist that had settled around them, dazzling radiance surged upward.

The light, infused with warm energy, pushed back the mist and gradually expanded its range.

Only then did the people who had been holding their breath finally exhale and search for the source of the radiance.

Twenty-odd pairs of eyes.

Where their gazes fell, a young man stood holding a sword that spewed forth brilliant light.

His eyes shone brighter than ever as he opened his mouth.

“Everyone, behind me.”

“...!”

The moment his calm voice reached their ears, the Peace Guild Hunters finally realized that they had escaped the influence of the Fear emanating from Behemoth.

And one person watching the scene trembled with emotion.

*This is…*

A feeling both deeply familiar and achingly distant.

Kim Hwajong recalled the face of someone whose features had faded in his memories of the past and murmured,

“So you were here.”

The past and present overlapped.

What Kim Hwajong saw reflected in his eyes was Cheon Taemin and Choi Minwoo at the same time—and Choi Minwoo and Cheon Taemin at the same time.

Song Cheonwoo, who saw the same thing, felt despair.

But the old butler felt joy welling up from deep within his chest, even in this precarious situation.

He stepped to the side of the young man shining alone.

*FWOOSH!*

Long, fierce whips of flame appeared in both his hands.

Choi Minwoo met Kim Hwajong’s gaze and spoke with a composed expression.

“We have to stop it. No matter what it takes.”

His voice carried an unshakable determination not to retreat.

Down below the mountain, the screams of people who had noticed the anomaly were already echoing through the air.

“Aaaah!”

“A-Aaaah!”

—GRAAAAAAAH!

Behemoth’s roar as it slaughtered the two hundred yetis sent the snow piled up on the mountain sliding down like a wave.

More than a thousand people scattered in every direction, screaming in shrill voices.

If the Hunters escaped the monster before them through sheer luck, those people would become Behemoth’s next targets.

Choi Minwoo, Kim Hwajong, and the Peace Guild Hunters gathered there all knew that.

They also knew that they could not face that monster on their own.

“L-Team Leader.”

They all possessed the strength of high-level Hunters, but their opponent was a monster that appeared only in mythology.

At the sound of the fear-stricken voice, Choi Minwoo answered.

“I won’t force you. If you want to run, run.”

Before the murmuring could even begin, he continued in a quiet voice.

“But don’t forget what choice you made here today. Whether you can still call yourself a Hunter.”

“...!”

The trembling in their wavering eyes stopped.

The sword in Choi Minwoo’s hand was radiating a brighter light than ever.

[Hero’s Soul].

An ego sword that granted the strength befitting a hero only to those who possessed the necessary qualifications.

*Hummm. Fwoooosh.*

The blade trembled violently.

Light burst forth like a flash, pushing back the darkness. The warmth contained within it wrapped around everyone.

By then, Choi Minwoo’s eyes had turned golden, and Behemoth’s form was reflected in them as it finished devouring every last one of its kind.

“Wasn’t the power we received given to us for a day like this?”

There was not a single exception.

Everyone gathered here had been chosen one day by someone unknown and had gained power beyond the ordinary.

And that power came with duty and a sense of responsibility.

Hunters.

The sword that protected humanity, the shield that defended it from threats, and the guardians who had to stand at the forefront of every battle against monsters.

Their wealth and fame might have dulled that ideal, but its pure essence remained.

“Attack formation. Take your positions.”

*Step.*

Choi Minwoo moved forward.

The light moved with his footsteps, followed by Kim Hwajong and the twenty Hunters.

They advanced in an arrowhead formation, and their figures were reflected in the enormous eyes of the monster that had just finished its first meal in this new world.

—G. R. A. A. A. A. H.

The monster, Behemoth, let out a cry that sounded almost like a sneer.

Even after devouring hundreds of yetis, it was still hungry.

It was ready to trample, chew, and swallow the humans approaching it while radiating that irritating light.

—Come. Hu. Mans.

No one there could understand Behemoth’s Demon Realm language.

But everyone understood its meaning perfectly.

*Shing. Fwoosh.*

Weapons were drawn.

Manifested magic surged through staffs and hands.

Twenty-two Hunters shone brightly in the deep darkness, bathed in the radiance.

And the shout of Choi Minwoo at the front launched them forward, taut as bowstrings.

“Charge!”

With a roar enormous enough to leave their ears ringing, they shot forward as one arrow.

*SHWAAAAAAK!*

A single ray of light cut through the darkness.

At its tip, the monster raised a roar that seemed to have been dragged up from the depths of an abyss.

—KWOAAAAAAH!

The next moment—

*BOOOOM! CRRRUNCH!*

Shouts and roars, light and darkness, all blended together.

* * *

—Kik!

“Shut your mouth, you fucking bastard.”

*Wham!*

With a heavy impact, the Merman’s head disappeared.

But I didn’t bother confirming its death.

Before the corpse had even fallen, I launched myself forward and blocked the Mermen trying to flee.

“You shit everywhere you go, then run away when it’s time to pay up. What kind of business ethics is that? Huh?”

—K-Kiiik.

Their cries were filled with a desperate desire to live.

But it was too late.

They were monsters, and I was human.

Besides, if they had crawled all the way to Busan and shit everywhere, they had to pay compensation for it.

An eye for an eye.

A life for a life.

Without hesitation, I swung White Flame in my hand.

*Whoosh!*

Flames surged along the spearhead and swept horizontally.

Fire Dragon’s Single Tail.

The fire dragon’s tail, packed with immense heat, lashed fifty Mermen in a single strike.

Their screams rang out alongside the horrific stench of flesh burning away.

—KIEEEEEEK!

A pitiful death cry.

I swiftly passed the nearest Merman.

*Slice.*

I felt its head rise into the air through my heightened senses, accompanied by the faint sound of something being cut.

But it wasn’t over yet.

There had been more than five hundred of them gathered together while searching for an escape route.

That meant there were just as many monsters I had to kill here.

*Slice. Slice. Shhhhhk!*

Monster limbs flew through the air with sprays of blood.

Everything caught in the path of my spear was sliced apart, while the force of Flame Divine Palm bursting from my outstretched palm burned more than twenty Mermen.

*Fwoosh! KRAAAASH!*

It was hot.

The asphalt melting beneath the ultra-high heat was hot.

So were the tires of the car spinning uselessly after slamming into the side of a bus.

And so was my heart as I looked at the driver who had died with his foot still on the accelerator.

*Drip. Drip.*

Blood ran over the hood after soaking the shattered windshield.

Apparently, even the most advanced airbag couldn’t stop the trident that had pierced through the windshield and embedded itself in the driver’s chest.

The eyes of the middle-aged man had already lost their light and were hollow.

The family photograph hanging from the rearview mirror like a talisman was soaked in blood.

Middle-aged parents.

A boy who looked like he was in elementary school, and a girl who looked even younger.

The worst fucking part was that the entire family in the photograph was inside the car.

Every one of them had lost their smiles.

Every one of them was covered in blood from head to toe.

“You fucking bastards!”

*Fwoosh! KRAAAASH!*

The flames grew even more ferocious and swallowed the monsters.

I cut across the path created by the fire, swinging my spear.

I kept cutting, slicing, tearing, and smashing without pause.

Between the scorching heat and the evaporating blood, a thought suddenly crossed my mind.

*Maybe.*

Maybe they had been traveling too.

Maybe they had gone on a family trip to Busan for the first time in years, laughing and chatting happily before they encountered the monsters.

Looking at Gwangan Bridge not far away, maybe this father and son had made a promise they could never keep.

*Crack!*

My fist punched through hard scales and crushed bone and flesh.

I silently looked at the Merman that let out a short groan.

Then I grabbed the warm, pulpy thing my hand had touched and tore it out.

*SPURT! Thud!*

The moment I pulled my hand free, green blood splashed across my face.

The stench was horrific, but I didn’t care. I was already covered in blood from head to toe.

With my eyes wide open, I dropped the heart I had just ripped out onto the corpse of the fallen Merman.

*Plop.*

Then I stomped on it because I disliked the disbelief in its eyes and the expression that seemed to accuse the world of wronging it.

*CRUNCH. Pop.*

Only then did I realize it.

There were no more monsters attacking me from all around.

There were no monsters fleeing.

There were no monsters still alive.

I was breathing heavily in the pool of green blood when—

“…Wicked human. You.”

“Why?”

The Skeleton King met my gaze as I turned my head and asked, then let out a sigh.

“No. Never mind.”

I briefly wondered what kind of figure I appeared to be in its eyes, but I didn’t ask.

I could probably guess from the expressions of the hundred or so Hunters standing behind the Skeleton King.

“We’re done here.”

At the dry voice that sounded strangely unfamiliar even to me, a Hunter who appeared to be a superior jolted and answered,

“Pardon? Ah, yes. Yes.”

“How are things in the other areas?”

“T-Those were the last ones. We were gathering our forces to strike them all at once, but…”

*Gulp.*

After swallowing nervously, he continued,

“It looks like everything has been taken care of.”

“Then that’s good. You worked hard too.”

I patted the Skeleton King on the shoulder and began walking again.

When someone asked where I was going, I answered briefly.

“We have to save people. The people still dying right now. The people who have survived this long.”

I was tired.

The mental fatigue was greater than the physical exhaustion.

But I couldn’t rest yet.

There had to be people somewhere still facing the terror of death and waiting for rescue.

I had to save even one person.

And then—

*Splash.*

The moment a footprint made of green blood stepped onto the asphalt in the middle of the city—

*Bzzzt. Bzzzt.*

Alongside an irritating electronic buzz, the electronic billboard on a high-rise building flickered.

A familiar face appeared on the screen through the static.

A face so handsome it was almost irritating.

It was Team Leader Choi.

At the same time, a small inset image appeared alongside a caption.

> **Peace Guild Hunter Choi Minwoo. Caught up in the Monster Wave that occurred in Pyeongchang…**

God fucking damn it.
## Chapter artifact 583

# Chapter 583

Team Leader Choi. Pyeongchang. Monster Wave.

The three keywords that had suddenly come crashing in left my mind in turmoil.

But the footage filling the electronic billboard left me no time to think.

—Kwooooom!

—Aaaahhh!

“An avalanche!”

People fled, screaming.

They stumbled along awkwardly without even thinking to take off their ski equipment, then fell as an enormous amount of snow and shattered rock came pouring down behind them.

—BOOOM!

Dozens of people were swept away by the snowdrift that surged over them like a wave, and red blood sprayed through the thunderous roar.

Buildings crushed beneath the rocks were engulfed in flames. And beyond those rolling flames lay the source of it all.

—Ruuuumble!

Although the sun had not yet set, the sky above that place was dark.

Black clouds had settled over an unfamiliar mountain peak.

Every time dazzling light flashed through them, tremendous vibrations and thunderous booms erupted.

*A Monster Wave.*

I understood instinctively.

In that place where light and darkness coexisted, a clash was taking place that would decide the fate of thousands.

And… Team Leader Choi, Butler Kim, and the Peace Guild Hunters were risking their lives against a named monster.

The voice of an announcer whose face was not visible came through the static.

—The government has declared the Pyeongchang area of Gyeonggi Province a disaster zone and dispatched emergency support forces. Meanwhile, the Monster Wave that occurred in Busan…

I had neither the reason nor the time to listen any further.

I spun around and shouted at the Hunters staring blankly at the electronic billboard on the high-rise building.

“Mages!”

“Y-Yes?”

“Mages, step forward! We have to get to Pyeongchang with Teleport! Right now!”

A few of the startled Hunters, jolted awake as if from a nightmare by the shout infused with internal energy, timidly raised their hands.

One A-grade mage and six B-grade mages. But despite stepping forward, their expressions were grim.

“I-I’m sorry, but it would be difficult for us to cast Teleport on our own.”

“What did you say?”

“We’ve all just fought monsters, so our mana fatigue is severe. On top of that, we need to draw a Teleport magic circle, and under the current circumstances…”

The mages let their voices trail off and looked around.

The corpses of victims and monsters lay scattered everywhere. The roads had been turned upside down.

Even among high-ranking mages, Teleport was famous for being difficult to cast. This was the worst possible environment in which to attempt it.

Skeleton King, who had been watching the situation, opened his mouth with a twisted expression.

“You stupid hu—bastards. Do you really think this is the time to worry about conditions? Do it. Please? Fuck. This is ridiculously hard.”

Despite barely holding back his anger, the murderous aura leaking from him made the mages swallow hard.

“B-But there’s nothing we can do right now. It’s too dangerous.”

“It’s impossible. Even if we succeeded against all odds, Busan to Pyeongchang is more than 250 kilometers. We can’t cross that kind of distance in a single jump.”

“Try it! Somehow, just try!”

Skeleton King’s shout was exactly what I wanted to say.

But I also knew the mages weren’t complaining for no reason. They weren’t Magic Johnson.

The dark-skinned Grand Mage who had sent me from Sichuan in China to a chaotic battlefield without even a magic circle was probably somewhere beyond the continent by now.

*Damn it.*

Sticky blood dripped from my clenched fist. I couldn’t tell whether it was mine or the monsters’. Maybe it was both.

“Isn’t there any other way?”

A middle-aged Hunter who appeared to be the highest-ranking person there answered in an anxious voice.

“We already contacted headquarters. We’re currently trying to locate a high-ranking mage among the Hunters in Busan who can cast Teleport, but…”

His voice trailed off. His expression was dark.

That was enough to tell me everything I needed to know about the situation.

After repeatedly urging the superior to hurry, I clenched my teeth.

*Damn it.*

Their opponent was a named monster. Something equal to—or even stronger than—the Kraken.

How much longer could they hold out against a monster whose might was conveyed even through the footage? How many of them would survive?

*Just a little longer. Please, hold out just a little longer.*

Muttering an unspoken plea that would never reach them, I sat down cross-legged.

For now, I had to replenish even a little of my depleted strength while we searched for a mage.

“Whoo.”

I closed my eyes, calming the anxiety and rage boiling inside me. Darkness covered my vision.

At the same time, the faces of those fighting in an even deeper darkness flashed before my eyes.

*Please… survive.*

Until I get there.

Whoooosh.

A profound internal energy carrying my desperate wish spread through my entire body, every limb and bone.

* * *

The trunk that swung through space was long and enormous.

It resembled an elephant’s trunk. It deflected the incoming magic and arrows, then rushed toward the ground.

Whoooosh!

A dense shadow fell over the people’s heads.

Choi Minwoo gritted his teeth, threw himself forward, and shouted.

“Scatter!”

Fwap-fwap-fwap!

The figures that had shot upward like the wind scattered in every direction.

It was movement befitting high-level Hunters at the very top of the Hunter hierarchy.

But if the people gathered here were A-grade Hunters, the enemy they faced was a named monster from ancient mythology.

—GRAAAAAAAH!

Behemoth.

The monster that had descended into the mortal world from the depths of the abyss let out a roar.

The powerful Fear that seized the soul and movement shook the Hunters as they scattered.

“Gasp!”

“Hk…!”

Two Peace Guild Hunters who had stepped outside the range of the light radiating from **Hero’s Soul** swallowed sharp breaths.

Without their wealth of real-combat experience and iron wills, they might have fainted or gone insane on the spot.

But even the momentary chaos brought on by Fear was enough for the cunning monster to achieve the result it wanted.

“No!”

Behemoth was half a beat faster than Choi Minwoo’s shout of warning.

And that determined the fate of the two men.

Whoom—CRUNCH!

A gust of wind erupted from empty air and slammed into the earth.

Superior defensive magic enchanted their armor. Their muscles had been trained to the extreme. Their vitality was tenacious.

But nothing could stop that force. It shattered and crushed everything in its path.

“Ghk. Cough!”

Dark red blood burst out with their dying cries.

Their bones, flesh, and even internal organs had been crushed. Not even the highest-grade potion could help them now.

For an instant, Choi Minwoo’s eyes met the two pairs of eyes in which the light was fading. He gritted his teeth.

*Again…!*

They had died. Died, and died again.

They had been trampled beneath enormous forelegs, pierced by tusks, and crushed from head to toe by the swinging trunk.

Of the twenty-two Hunters—including himself and Kim Hwajong—more than half had met gruesome deaths.

If they had not been carrying potions, he would have had to watch even more people die with his own eyes.

But now, even those potions were almost gone.

*Damn it.*

Choi Minwoo gritted his teeth.

The pain rising from his broken molar had faded before he knew it, and he could no longer feel the blood flowing from his split lips.

Only rage and determination remained.

Those two emotions kept Choi Minwoo from collapsing in despair. They helped him overcome his fear and charge toward Behemoth.

“Young Master!”

Whoosh!

Leaving Kim Hwajong’s anguished shout behind, Choi Minwoo’s mana-infused foot kicked off the earth.

A powerful sound of splitting air rang above his head as he rushed forward like a ray of light.

Choi Minwoo twisted his body with every ounce of strength he possessed.

Whoom—BOOOM!

The ground shook.

Snow that had covered the earth scattered, and shards of shattered rock scraped across his forehead.

The blood blocking his vision was red, and the sword Choi Minwoo held in both hands radiated a pure white brilliance.

Fwoooosh—slash!

The dense darkness split apart.

When the ray of light that cut through space sliced through the two forelegs standing like pillars, an enormous amount of blood burst from the deep, split wounds.

Fwoooosh!

Choi Minwoo, drenched from head to toe in green blood, exhaled the breath he had been holding.

He had wanted to avoid it, but he couldn’t.

Like Behemoth’s staggering legs, his own body was shaking after releasing so much strength in such a short moment.

“Two of its four legs…”

Choi Minwoo muttered faintly through his completely green-tinted vision.

Fifteen Hunters.

And compared to the price of his own life, it was an absurdly expensive exchange.

Still, Behemoth’s scream of pain was not unpleasant to hear.

—GRAAAAAAAH! Hu. Man!

“…I’m listening. I just don’t know what you’re saying.”

Choi Minwoo answered weakly.

The fatigue and pain he had forgotten came rushing over him all at once.

The brilliance radiating from **Hero’s Soul** in his hand was fading as though it might go out at any moment.

*Hold out a little longer. Just a little longer.*

But that was too much to ask.

The fatigue that had begun with his bloody battle against Song Cheonwoo had steadily accumulated until now.

The healer’s death and the depletion of their potions had left the bleeding and injuries unchecked, and they were bringing him down.

Ssssh.

The world tilted.

No—the world was not tilting.

Choi Minwoo was.

Through his slowly overturning field of vision, he saw something enormous flying toward him.

Whoooosh!

Feeling the wind that would crush his entire body, Choi Minwoo closed his eyes.

* * *

BOOOM!

With a thunderous crash, the only light disappeared.

A cloud of snow and dirt rose through the dense black mist surrounding them.

Ruuumble!

Under Behemoth’s most powerful strike yet, the entire mountain trembled.

The surviving Peace Guild Hunters watched the sight with eyes filled with despair.

The hope they had held in their hearts, however faintly, had vanished along with the light.

Along with the young man who had led them from the front.

*It’s over. Everything is over.*

They all realized it instinctively.

The world might not end, but at least the world they knew would end here, today.

And yet, strangely enough, their hearts were calm as they faced the end.

At least they had fulfilled their duty—their duty as human beings and as Hunters.

They had poured out all their sense of mission, which wealth and fame had briefly made them forget.

They had no regrets.

“Fuck. I just signed a house contract the day before yesterday.”

A snort of laughter escaped the Hunters at someone’s mutter.

“That crazy bastard.”

“If you’re scared, leave. Nobody’s stopping you.”

But no one moved.

Not even the Hunter who had spoken first.

He stared blankly at his trembling legs, then tossed out,

“How are we supposed to leave? I’d rather die fighting.”

Everyone felt the same way.

Thousands of people were still evacuating behind them.

The comrades who had died before them, and Choi Minwoo, who had charged toward Behemoth until the very end, had died to protect those people.

“We’ve got plenty of money, and we’ve got our pride.”

“Still, what a lousy day to die. I can’t even see the sky because of this shitty fog.”

“By the way, why is that elephant bastard suddenly standing still?”

It was just as the few remaining Hunters steeled themselves and prepared to charge Behemoth.

“You don’t need to die.”

With that quiet voice, the dense fog scattered.

What drove away the abyss-like darkness was not light, but flame.

Fwoooosh!

A man appeared through the fog amid fierce flames and continued,

“At least you don’t.”

The trembling eyes of the Hunters reflected a middle-aged man with half-gray hair.

Kim Hwajong, who had disappeared into the fog after chasing Choi Minwoo, looked very different from when he had first entered.

“…Guild Master, your arm.”

“I’m fine.”

Kim Hwajong’s left arm had been torn away, but he smiled faintly through his exhaustion.

It was the smile of someone who had lost one arm but managed to save something far more precious.

He handed the person he had been carrying in his right arm over to the Hunters and continued,

“You must leave this place immediately. With the Young Master.”

“But…”

“That is an order from the Guild Master.”

Grrrrr.

The monster let out a low laugh after finding the prey it had missed by a hair.

The smile faded from Kim Hwajong’s lips.

“Go!”

“...!”

At the fierce shout that erupted in an instant, the Hunters realized they had no choice and clenched their teeth.

They took Choi Minwoo’s limp body and launched themselves away with a brief bow.

Shhhh-shhhh-shhk!

Their figures slid down the steep slope.

Kim Hwajong watched them silently, then another faint smile appeared at the corners of his mouth.

*You must be safe. You have to be.*

When he turned away after murmuring the small plea that would never reach them, hellfire flickered in his one remaining hand.

“Come at me, you fucking bastard.”

—GRAAAAAAAH!

Behemoth’s enormous eyes and Kim Hwajong’s flame-filled gaze collided in midair.

The old butler, who had sent everyone away and placed himself at the edge of the cliff, began to recite a spell that might be his last.

“Hellfire of hell. Descend upon this place.”

**Hell Fire.**

Ruuuuumble!
## Chapter artifact 584

# Chapter 584

Kwooooom!

A pillar of fire shot into the sky. The mountain shook. An area spanning hundreds of meters boiled with ultrahigh heat as snow, dirt, and rock melted away.

A land of death, overflowing with lava. Standing like towers above the ground where everything had evaporated were two beings.

—Hu. Man. How. Dare. You!

The mythical monster raged, its body charred black, while the gray-haired old butler calmly gazed at it.

**Hell Fire.**

Even the hellfire summoned from the depths of hell had failed to bring Behemoth down. One of its enormous tusks had melted away without a trace, and its entire body was charred black, but the monster remained standing.

And yet…

“What a bastardly tough one you are.”

Kim Hwajong did not retreat. He could not retreat.

With his only remaining hand, he gripped his Magic Staff tightly.

Fwoosh.

The short, slender staff was engulfed in flames. Once the fire passed over it, a new staff emerged—thicker and longer than before.

It was the cherished weapon that had turned countless monsters into ash during the chaotic era of the Great Cataclysm and earned its master the title of Hellfire Mage.

Kim Hwajong pointed the reddish staff at Behemoth and muttered,

“Stop. You’re not going anywhere.”

—You. Wretch!

Behemoth roared. At the same time, the thick black mist that had settled over the area moved like a living creature and shot toward Kim Hwajong.

Sssshhhh!

It was both a rope meant to bind his entire body and a blade meant to tear through flesh and bone.

But Kim Hwajong calmly watched the mist closing in from every direction.

In that instant, the staff in his blood-covered hand struck the ground.

BOOM!

A wave spread outward with a deep rumble. The flames rising around Kim Hwajong formed a single ring that enclosed him.

Fwoosh—FWOOSH!

Before fire was a symbol of destruction, it was a force of purification.

The moment the black mist shooting toward him touched the flames, it withered away like ash.

The enormous eyes of the monster looking down upon the earth reflected the figure of a lone human standing tall.

—What. Is. This?

Even Behemoth had not expected this.

Its opponent was nothing more than a human. And yet this small, insignificant creature had not only wounded it, but nullified its attack.

—You. Hu. Man!

A roar filled with powerful Fear shook the entire area. But unlike the flames flickering in his eyes, Kim Hwajong’s heart was utterly calm.

The monster before him had made one mistake.

It did not realize that the old human standing before it possessed none of the fear that everyone carried deep in their hearts.

*I’m glad, Young Master.*

Along with a murmur that would never reach him, Kim Hwajong smiled faintly. His one and only fear was moving farther away from the disaster even now.

As long as that child, Choi Minwoo, could survive… it did not matter what happened to him.

*Even if I die here.*

It would be fine if he were crushed beneath the monster’s feet, pierced by its tusks and killed without being able to leave even a final word, or reduced to ash after squeezing his mana and body past their limits.

*If the Young Master is safe, that is enough for me.*

And so Kim Hwajong gripped the staff with joy in his heart.

An immense amount of mana, already beyond its limits, surged into the tip of his cherished weapon, which glowed with a reddish light. The heated mana erupted as flame.

“Be swept away.”

**Fire Wave.**

With the short incantation, a wave of fire rolled forward.

At its end, Behemoth swung the trunk it had raised with an enraged cry. It was long like an elephant’s trunk—and dozens of times larger.

FWOOSH!

The wind that arose with a mighty crack of splitting air slammed into the wave of fire. The ultrahigh heat died away in an instant, and invisible blades of wind flew in and raked the area from every direction.

Ssshhh-shhk! Slash!

The ground split and tore apart like sheets of paper. But Kim Hwajong had already slipped out of the area by the narrowest margin.

A low voice escaped between the old butler’s lips as he charged toward Behemoth’s flank.

“Shoot forth.”

**Blaze.**

BOOM!

Flames burst from the tip of the foot he planted.

With the instantaneous explosion, Kim Hwajong shot forward as a streak of flame. Then a dense shadow fell over his head.

Whoooosh!

“……!”

His instincts moved half a beat faster than his reason. **Fire Shield.** Alongside a silent, wordless spell, layers of fiery shields formed above Kim Hwajong’s head.

And in an instant so brief it could barely be called a moment, tremendous pressure crushed down upon the more than twenty overlapping shields.

CRRRRUNCH!

Everything shattered and scattered.

Overwhelming force and weight. On top of that, the immense magic power whose end could not be fathomed shattered the layered fiery shields and shook the caster’s mana.

Ptooey!

Dark red blood sprayed from between Kim Hwajong’s lips.

His vision went hazy for a moment in the aftermath of the dispersing magic. But instead of collapsing where he stood, he clenched his teeth and threw himself aside as though falling.

CRACK! THUD!

The defensive magic had bought him a brief moment.

Behemoth’s trunk swept past him by the narrowest margin and smashed into the ground. At the same time, hundreds of fragments flew in every direction, scraping across Kim Hwajong’s calf.

The pain felt like a burn. But instead of groaning, the old butler exposed his bloodstained teeth and smiled.

“Didn’t I tell you? You’re not going anywhere.”

In that instant, the staff in his hand emitted ultrahigh heat. A sphere of flame formed in midair and swelled in size.

Kim Hwajong coughed up a mouthful of blood and muttered,

“Explode. Artillery of flame.”

**Flame Cannon.**

With the completed spell, dazzling light-flames burst forth.

The ultimate fire spell, carrying power faster and more formidable than any cannon, shot toward the monster’s two forelegs—the same forelegs that Choi Minwoo had already cut halfway through.

—You…!

FWOOSH—BOOOOOOM!

The next moment, Behemoth’s cry was swallowed by a thunderous boom that shook the entire area.

The fire that tore through space burst open the wounds that had not yet healed and swept through the inside of the legs.

Sizzle.

Terrible pain spread from the forelegs, blackened like charcoal. Behemoth let out a roar filled with agony.

—GRAAAAAAAAAAH!

Ruuuuumble!

At last, the two forelegs bent.

The mythical monster that had risen into the mortal world from the depths of the abyss dropped both forelegs to its knees as if a temple were collapsing.

Its tremendous weight shook the earth, and an enormous cloud of dust rose into the air.

And the human who had forced Behemoth to its knees was laughing as he spat blood.

“Ha! Hahahaha!”

It was the laughter of the Hunter once called the greatest fire mage—and the relief of a butler who had fulfilled his duty.

*This is enough. This is enough.*

Half of Behemoth’s four legs had been rendered useless.

Unless someone gave it wings, Behemoth would not be able to chase Choi Minwoo now.

And because of that, no small number of lives would survive.

Kim Hwajong smiled as he watched the dense shadow flying toward him.

*Still, just a little… I wish…*

CRACK! Sssshhhh!

His vision turned white. Kim Hwajong felt tremendous impact and pain engulf his body as he shot through the air like a cannonball.

BOOM!

With a thunderous crash, his back smashed into solid rock and broke. Something unstoppable surged up from deep inside him.

“Gueeeeeegh!”

The old butler looked down at the blood he had vomited, his eyes dimming. Small pieces of his organs floated in the pool of dark red blood.

His ears felt blocked, as though his eardrums had burst. Through his blurred vision, a memory from long ago rose like a haze.

*“Your fire magic is incredible. Were you a former arsonist?”*

*“……What kind of crazy shit are you talking about? If you’re not going to help, then get lost.”*

*“Fortunately, I won’t have to ‘go out,’ then. I’m going to help you and everyone here.”*[^1]

[^1]: The same verb means both “get lost” and for a flame to “go out.”

*“Hmm. In that case, the story changes a little. What’s your name?”*

*“Cheon Taemin.”*

When they first met, Kim Hwajong had not known.

He had not known that this man, who looked absurdly young for his age, would become the idol to whom Kim Hwajong would devote his entire life.

But that became reality soon enough.

One year, two years, five years… When the long and terrible Great War finally ended, Kim Hwajong had become Cheon Taemin’s shadow.

*“What am I supposed to do now?”*

Like it had for everyone else, the Great Cataclysm had completely changed Kim Hwajong’s life.

In those days, despite having waited so long, he was confused by the peace that had finally arrived. His idol calmly asked him in return,

*“What do you want to do?”*

*“I don’t know. But I’ll do anything you tell me to do.”*

*“Then join the Guild. I need you. I’ve brought Jungryong and Cheonwoo in too.”*

*“The Peace Guild, or whatever it’s called?”*

*“Yes.”*

*“The name sounds pretty damn lame. How about Ares instead? The god of war from Greek mythology. Ares.”*

*“Ares, huh? Not bad. Then I’ll go with your suggestion. Join the Guild. I’ll make sure you don’t have to worry about your old age.”*

*“……I’m not really suited for office work. All right, Guild Master.”*

*“I think I’ve told you about five thousand times over the past five years to call me hyung. You really never change.”*

Just as he had said then, Kim Hwajong did not change.

Not even after his relationship with his two trusted comrades and closest sworn brothers grew distant, and after it became difficult to see Cheon Taemin’s face.

Even after peace arrived, his fiery temperament remained, and he continued to swear constantly.

The moment he decided to change came just after a child born amid everyone’s blessings lost his parents in an unfortunate accident.

*“Hello.”*

*“……Hello.”*

At the funeral, attended by only a few people, the little boy—no more than four or five years old—looked lonely.

The sight of him clinging to the leg of his maternal grandfather, now his only family, and offering a greeting with a dark expression pained Kim Hwajong’s aging heart.

Perhaps that was why he readily accepted Cheon Taemin’s proposal when he came to visit a few days later.

*“Can you take care of Minwoo? That child?”*

The immortal hero who had become a symbol of humanity was always busy.

Instead of Cheon Taemin, who continued living as though he were being chased by something even after the Great Cataclysm ended, Kim Hwajong became the family of a child who had been left alone.

*“Good day, Young Master.”*

His hair and clothes had to be neat. His voice had to be gentle. A smile had to rest at the corners of his mouth.

And so the Hellfire Mage who had burned through a page of the Great Cataclysm became Butler Kim.

*“Young Master. You mustn’t run! You might get hurt. Oh, dear.”*

*“Young Master. Being a picky eater is bad for your health. Please eat.”*

*“Young Master. Please don’t cry.”*

Young Master. Young Master. Young Master…

Time flowed like a river.

The child grew into a young man, and white frost settled over Kim Hwajong’s hair.

Even after Cheon Taemin vanished without a trace, Kim Hwajong remained steadfast in his place.

His Young Master no longer ran about recklessly, ate every kind of food without complaint, or cried while thinking of the parents who had left him too soon.

And then came the day when Kim Hwajong discovered traces of someone he had not seen in a long time on the face of the grown young man.

*“You said you were going to create a Guild.”*

*“Yes. I’m sorry, but I’ll need you to serve as the Guild Master, Butler Kim.”*

*“If that is what you wish, Young Master, I will do anything. But what do you intend to name the Guild?”*

*“The Peace Guild. I’ll call it the Peace Guild.”*

*“……!”*

*“Why does your expression look so… unhappy, Butler Kim?”*

What should he say? Hesitating over the many thoughts that flashed through his mind, the old butler soon burst into loud laughter.

*“Not at all. The Peace Guild. That’s a wonderful name.”*

And so the past met the present.

After the Peace Guild was founded, Kim Hwajong faced each day immersed in joy and memories.

The Young Master, who had worn a cold, rigid mask, softened after meeting “comrades” for the first time in his life, and the Peace Guild continued to grow with every passing day.

Kim Hwajong thought that nothing but good things lay ahead. From then on. Forever.

He thought he would be able to watch his Young Master grow from his side.

*Today really was… the best day of my life.*

Cough.

Kim Hwajong laughed as he vomited blood mixed with pieces of his organs.

The only reason he could still laugh while dying was because of one thing his Young Master had said today.

*“Thank you. For becoming my only family.”*

And then… what else had his Young Master said?

*“I’ve always wanted to say this to you.”*

Yes. That was what he had said.

Kim Hwajong raised his head through a fit of coughing. Dense black mist filled the direction of his fading gaze.

Somewhere beyond that invisible mist, his only hope—and his only fear—was probably still alive and leaving this place.

“I want to… see you.”

A trembling voice slipped between his bloodstained lips.

Pleased by the sight of the old butler facing death, the mythical monster opened its jaws with a satisfied smile.

FWOOSH.

A tremendous gust swept through the entire area.

The flames that had not yet gone out, someone’s limbs and blood scattered across the ground, and even the rocks were sucked in together.

Everything drawn in like a tornado spun inside Behemoth’s mouth.

“Young… Master.”

No. That was not it. Though his words would never reach him, this was his final greeting.

A faint smile spread across his wrinkled lips.

“Minwoo.”

At the very moment his fading voice escaped—

Sssshhhh—FLASH!

A burst of radiance erupted from midair and bathed the entire world in white.

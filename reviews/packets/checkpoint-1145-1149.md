# Checkpoint Review — 1145–1149

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

# Chapters 1145–1149

## Plot

While Jin Taekyung’s body sleeps in Murim, his consciousness investigates a suspected crisis in the realm of immortals. Jeok Cheongang stays beside him as the coalition army crosses the Taklamakan Desert toward Tianshan. Elsewhere, the Grand Mage awakens after being reborn through the Lord of Heaven’s grace; the Lord connects a wave she felt to the heavens opening again.

In a buried desert shelter, Choi Minwoo leads the Hunters out to fight thousands of approaching enemies. Taekyung awakens in the Skeleton King’s backpack and joins the battle. He and the Skeleton King fight exceptionally durable, rapidly regenerating monsters, while the Grand Mage—now identified as Magic Johnson—attacks from above. The Hunters defeat the monsters.

Johnson says his last contact with the group was twenty-four hours earlier. Team Leader Choi tells Taekyung he has been unconscious for ten days. The System reports that the Main Quest Cataclysm failed despite the Doppelganger’s defeat: the Demon Realm’s boundaries have partially opened, and a rift is in progress. Black Dragon Duke Morgoth has answered a summoning. Taekyung recognizes his wings and roar from his last night in Murim. In Russia, Morgoth destroys Red Square and enters Vladimir Furin’s office.

## Continuity

- Taekyung has awakened and reunited with Choi Minwoo, the Skeleton King, the Hunters, and Magic Johnson. He and the Skeleton King are friends and allies.
- Taekyung was unconscious for ten days, while Johnson’s last contact with the group was twenty-four hours earlier. The difference remains unexplained.
- The Main Quest Cataclysm failed despite the Doppelganger’s defeat. The Demon Realm’s boundaries have partially opened, and a rift is in progress.
- Black Dragon Duke Morgoth answered a summoning. He destroyed Red Square and entered Vladimir Furin’s office in Russia; his intentions are unknown.
- The Grand Mage was reborn through the Lord of Heaven’s grace and felt a wave the Lord associated with the heavens opening again. The wave’s cause and significance remain unexplained.
- The coalition army of more than two hundred thousand is crossing the Taklamakan Desert toward Tianshan. Jeok Cheongang is keeping watch over Taekyung’s sleeping body.

## Translation Decisions

- Render 스켈레톤 킹 as “Skeleton King,” 스톤 킹 as “Stone King,” 리자드맨 as “Lizardman,” and 리자드 as “Charmeleon.”
- Render 오러 as “Auror” and 검기 as “Sword Energy.”
- Render 흑룡공 as “Black Dragon Duke,” 모르고스 as “Morgoth,” and 균열과 붕괴 as “Rift and Collapse.”

## Durable state

{
  "active_continuity": [
    "Taekyung has been unconscious for ten days; Magic Johnson's last contact with the group was twenty-four hours ago.",
    "The Main Quest Cataclysm failed despite the Doppelganger's defeat; the Demon Realm's boundaries have partially opened and a rift is in progress.",
    "Black Dragon Duke Morgoth has answered a summoning; Taekyung recognizes his wings and roar from his last night in Murim.",
    "Morgoth destroyed Red Square and entered Vladimir Furin's office in Russia.",
    "Taekyung and the Skeleton King are allies and friends."
  ],
  "continuity_sources": [
    1149
  ],
  "open_questions": [
    "Why has Taekyung's ten days of unconsciousness corresponded to only twenty-four hours since the last contact?",
    "What conditions change the rift's progress?",
    "What does Morgoth intend in Russia?"
  ],
  "safe_through": 1149,
  "temporary_decisions": [
    "Render 흑룡공 as “Black Dragon Duke” and 모르고스 as “Morgoth.”",
    "Render 균열과 붕괴 as “Rift and Collapse.”"
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 1145

# Chapter 1145

The Fire King, Jeok Cheongang, silently looked down at his Disciple, who lay in a comfortable position.

His eyelids were firmly shut. His chest rose and fell with each quiet breath.

Anyone could see that Jin Taekyung was in a deep sleep, oblivious to the world. But Jeok Cheongang knew the truth no one else did.

His Disciple had gone somewhere beyond his dreams—to another world.

*The realm of immortals.*

Jeok Cheongang remembered clearly the shock he’d felt that day, when he first heard the truth from his Disciple’s own lips.

No—he could never forget it.

A world where skyscrapers hundreds of *jang* tall stood together like a forest; where the footsteps of humanity reached beyond the sky and into the universe; where supernatural powers that defied all reason ruled the land.

An unknown world Jeok Cheongang could scarcely imagine.

But the place where his Disciple had been born and raised was clearly not as peaceful and beautiful as he’d first thought.

“I have to go.”

The previous night, Jin Taekyung’s face had been more solemn than ever as he said he intended to return to his homeland.

Even Jeok Cheongang had never seen him like that.

“Has something happened in the realm of immortals?”

“I don’t know. Not yet.”

“Not yet, you say. From the way you put it, something bad must be happening.”

“It’s only a hunch, but yes.”

Jin Taekyung had dismissed it with the words *only a hunch*, but Jeok Cheongang, who understood him better than anyone, already knew.

His Disciple never spoke idly.

Behind his usual lighthearted manner, which sometimes bordered on frivolous, lurked a beast alert to even the smallest changes around him.

That was why Jeok Cheongang could feel it all the more clearly.

The immense anxiety and burden pressing down on Jin Taekyung’s shoulders—and the way Jeok Cheongang’s heart had sunk when he saw his Disciple like that.

Perhaps that was why the image of his Disciple’s limp body, hanging helplessly in his arms ten days ago, had suddenly come to mind.

“Then say it properly this time.”

“What?”

“You just said you were leaving. As if you might never return.”

Maybe he’d been worried about his Master’s needless concern.

Jeok Cheongang hadn’t heard everything about the place called the realm of immortals, but he knew one thing for certain.

Even if the two worlds were different in every way, when the soul was erased, the body died too.

More than anything, a Master feared the day he might find his Disciple in a deep sleep from which he would never awaken.

And after a moment of silence that seemed to last forever, Jin Taekyung smiled and answered.

“Then… I’ll be back. I promise.”

And yet, why was it?

Even after hearing the answer he’d wanted, Jeok Cheongang’s heart had sunk heavily.

He’d stayed awake all night, and even now, as he remained beside his Disciple on the long journey, his heart was still weighed down.

*As little as a month.*

That was how long it would take an army of more than two hundred thousand to cross the vast Taklamakan Desert in Xinjiang.

It was only an estimate, of course. But the coalition army, having completed every preparation and calculation with meticulous care, would cross the desert at breakneck speed and reach its destination.

That very place which had been regarded as cursed for the past thousand years: Tianshan.

*No matter what danger lies ahead, it makes no difference. This old man will protect you.*

Those who know what they must do have no fear.

A Master belonged beside his Disciple, and Jeok Cheongang would not leave this spot until Jin Taekyung woke.

Nor would the others, who had arrived and taken up their positions without a word.

“What are you staring at?”

Jeok Cheongang answered the Slaughter Saint, who sat in one corner of the carriage with his eyes half-closed.

“There’s an uninvited guest planted right there. I was wondering who the hell he was.”

“Uninvited? Why would I be uninvited?”

“Because the owner of the carriage didn’t invite you.”

The Slaughter Saint snorted and nodded toward Jin Taekyung.

“You’re mistaken. The owner of the carriage isn’t you. It’s that fellow lying over there. And this carriage was a gift from the Emperor and the Zhuge Clan, not you.”

“But I’m his Master.”

“By that logic, I’m his Master too. I gave him some valuable instruction once.”

“You mean that Ghost-whatever footwork technique? It wasn’t very good.”

“What? Not very good? Your Fire Gate Clan—”

“Your? You snot-nosed brat. How dare you talk to an elder like that—”

It was a bewildering conversation for two old masters, whose combined ages exceeded two hundred, to be having inside a carriage drawn by the eight finest imperial sweat-blood horses. And yet Jeok Cheongang felt warmth spreading in one corner of his heart.

*Do you see? Your efforts and pain weren’t in vain.*

Not even one shichen had passed since the army began its full-scale march, yet the eight-horse carriage at the very back of the long, seemingly endless column had already received plenty of visitors.

The Embroidered Uniform Guard protecting the Emperor’s closest confidants, masters from the Nine Sects and One Gang, and others from Murim.

Every one of them was among the most skilled in this vast army, and each had come asking to join them.

To repay a debt.

To show even a little respect for the great devotion and effort the owner of the carriage had shown until now.

If Jeok Cheongang hadn’t sent them away with threats, there might have been more than a thousand of the finest guards surrounding the carriage by now.

Of course, a handful had stood their ground without so much as a twitch of the eyebrow, even in the face of Jeok Cheongang’s threats.

“Good grief, there they go again.”

“They’ve got plenty of energy.”

“Shh. They’ll hear you.”

At the familiar voices drifting in through the carriage door, Jeok Cheongang felt a sudden swell of emotion, then let out a small laugh before he knew it.

“Why are you laughing all of a sudden? You sound like a crazy old man.”

“Who knows.”

Perhaps Jeok Cheongang couldn’t stop smiling even after the Slaughter Saint’s sour jab because he was happy.

It was a small but profound joy, knowing that he wasn’t the only one in this harsh world who treasured his Disciple as much as himself and looked out for him.

Though Jeok Cheongang had turned his back on the world long ago and kept his distance from people, he didn’t want his one and only Disciple to walk the same path.

No. This boy had to be different.

He had to pursue righteousness, practice chivalry, and win people’s hearts.

Now, and from here on.

Always. Forever.

And to make that wish come true, his Master could do anything.

Even if hell waited beyond those scorching sands.

*I swear it.*

By now, Jeok Cheongang’s eyes had sunk deep as he watched the vast desert outside the window.

Then—

Rumble.

A huge bank of dark clouds began to spread above the intense heat shimmer.

* * *

Everything that happens in the world has two sides, like a coin.

As there is darkness where there is light, and the moon rises when the sun sets.

Not long after someone closed their eyes in comforting warmth, the same was true of someone who awoke in a sealed chamber tens of thousands of *ri* away.

No—perhaps *awoke* was the wrong word.

The one who had just opened their eyes had become someone who could never sleep again.

“What happened?”

At the low voice that seemed to ring inside his head, a subordinate shuddered and answered.

“You collapsed for a moment.”

“I collapsed?”

“Yes. It seemed you lost consciousness, but this subordinate dared not touch you…”

Crack.

Before he could finish, an invisible hand squeezed his throat, and the subordinate’s face went pale.

“You dare lie to me.”

“C-cough. I-I’m not.”

Instead of an answer, formless energy crawled over him, binding his whole body and constricting his breath.

The subordinate gasped and struggled to plead his case. When his body finally went limp, the energy pressing down on the entire chamber faded as though it had been washed away.

Leaving behind the realization that the dead man had told the truth—and one question that remained unanswered.

*Lost consciousness? Why?*

The shadow left the sealed chamber, its subordinate’s corpse behind it, and fell into thought amid the deep darkness.

An inexplicable shock had struck in an instant, followed by a break in consciousness.

Even the shadow, with its vast knowledge, could not explain what had happened.

The shadow rose as if floating, climbing thousands of steps. It stopped only when it reached the one being who could answer its question.

Rumble.

The enormous iron doors opened before the shadow could even ask to enter.

In the perfectly complete darkness, where not a single glimmer of light could be seen, *he* was there.

“Your humble servant comes before the great Lord of Heaven.”

The shadow cried out in reverence and immediately prostrated itself.

The shadow already possessed power and stature far beyond the limits of a human being. Yet that pitch-black darkness held a power that could crush the shadow like a bug at any moment.

No—in having grown another level, the shadow could feel that omnipotence all the more clearly.

“I knew you would come.”

Even the sound of that voice, so devoid of highs or lows that it froze the soul just to hear it, carried the faintest hint of delight.

“You must have felt the wave.”

“……!”

“What surprises you so, Grand Mage?”

A shadow stirred, then gently wrapped around the Grand Mage’s shoulder.

“Root and branch are parts of the same whole. Reborn through my grace, you must have felt it.”

The Grand Mage’s eyes trembled. For a moment, they turned toward their own hand.

It was rotted and decayed, white bone showing through—a chilling reminder that the body had already died. But the Grand Mage shuddered with joy and awe.

That was right.

They had been born again.

Under the blessing of the great and omnipotent Lord of Heaven, they had risen from death and returned to their master’s side.

And at last, they understood.

The true purpose behind the Lord of Heaven’s grand design.

“Then, the wave you spoke of just now…”

“Yes.”

At that very moment—

Ssssh.

A faint green light rose in the pitch-black darkness.

For more than fifty years, no one in Dark Heaven had seen the Lord of Heaven’s snow-white fingers. Now those fingers, bathed in green light, gently caressed a piece of jade.

Softly, and coolly.

“Once again, the heavens have opened.”
## Chapter artifact 1146

# Chapter 1146

In a dark, narrow room, a man stood before a full-length mirror, silently staring at its smooth surface.

Tall and slender, with sharply defined features.

He had seen his own reflection countless times over the past thirty-odd years. But the feelings gripping him now weren’t familiarity, but bitterness and anger.

“Why did it have to be you?”

The faint words slipped suddenly from his lips.

Normally, he would never have muttered to himself. But the man didn’t care, and continued.

“You’re not the one who should be here.”

Each word felt like it was spitting fire.

A sharp, invisible awl seemed to probe deep inside his chest. Sweat had gathered on his face, then rolled down his cheek.

Like his heart. Endlessly.

“You don’t deserve it.”

That was right.

Unlike the handful of people who possessed the necessary “qualifications,” the man had neither overwhelming power nor the experience of a battle-hardened veteran.

But even apart from whether he could accept that truth, he knew better than anyone the weight of the immense responsibility pressing down on his shoulders—and how important this mission was.

That was when his trembling eyes suddenly flashed.

Crack.

With a gruesome sound of flesh tearing, the taste of blood spread through his mouth.

The man spat out a mouthful of blood, then faced the mirror again.

There stood a man with a deep, unwavering gaze, unlike the one from moments ago.

He bore an uncanny resemblance to someone bound to him by the longest and closest of ties—and yet, someone who had never felt farther away.

But even this brief reflection was a luxury for the man—no, for Choi Minwoo.

Crack.

A faint tremor traveled down from the ceiling, and hairline fractures spread across the full-length mirror like a spiderweb.

Sensing that the time had finally come, Choi Minwoo turned away, leaving behind his distorted reflection, and flung open the rusted iron door that had briefly shielded him from the harsh reality outside.

Creeeak.

In the middle of a corridor barely wide enough for two adult men to stand shoulder to shoulder, a hulking figure wrapped from head to toe in a military poncho raincoat gave Choi Minwoo a nod.

“Right on time.”

“Sorry to keep you waiting. I needed a moment to get ready.”

“No need to apologize. You’re in charge here. Though…”

The figure glanced at the dust drifting slowly down from the ceiling, stirred by a tremor that had grown slightly stronger.

“Any later and we’d have been in trouble. Let’s move.”

As if they’d planned it, they quickly set off, trading words as they made their way through the winding, ant-nest-like corridors.

“What happened?”

At Choi Minwoo’s question, the hulking figure answered in a low voice.

“Hopefully it’s just a sandstorm…”

“It’s them.”

“Damn it. Yeah.”

Why were ominous hunches never wrong?

But he’d left all his self-reproach and complaints behind him in front of the broken mirror. Choi Minwoo steeled himself and spoke again.

“How many?”

“From what we’ve figured out so far, at least several thousand.”

Several thousand.

At first glance, it was a recklessly broad estimate. But communications and every radar network had been down for some time.

So Choi Minwoo accepted the figure without question or hesitation.

The hulking figure’s abilities were unlike anyone else’s in this old, worn-out underground bomb shelter. He was also someone Choi Minwoo trusted enough to entrust with his own life.

“…Several thousand?”

If there were already several thousand as far as they could tell, the number could exceed ten thousand, depending on the situation.

At Choi Minwoo’s darkening gaze, the hulking figure made an effort to shake his head.

“They might just be a scouting party. Those guys always move around in swarms like ants.”

It was a reasonable guess.

The enemy had already swallowed up a vast stretch of desert, their numbers horrifyingly large—and they were growing by the day.

*Even if they aren’t here to attack, they could simply be passing through on their way to another city. Our routes might have crossed by chance.*

Choi Minwoo walked in silence, lost in thought.

The place they were staying was an underground bomb shelter secretly built by the US military during the Gulf War.

It had been abandoned for over fifty years since the war ended. Then the Great Cataclysm reshaped the landscape, and the shelter was forgotten altogether.

Until one day, a group of people rushing across the desert discovered its entrance, hidden beneath a sand dune.

*And what are the odds the enemy knows about this place too, when we only found it by luck?*

Virtually none.

The only thing that bothered him was the communication Magic they’d barely managed to establish not long ago. But given who had sent it, the chance the enemy had picked up on it was close to zero.

*Which means, in the end…*

Choi Minwoo finally arrived at a conclusion.

That all of this was just a coincidence.

It was highly likely they were a scouting party, as the hulking figure had said, or that their routes had simply crossed.

So all they had to do was wait.

If they held their breath in this old, musty place, took the sand and dust raining down on them from overhead, and prepared for a possible fight, peace would return before long.

The uninvited guests wouldn’t even find the doorbell to their hidden home. They’d pass right over their heads, and Choi Minwoo could lead the survivors out of the shelter without a single casualty.

In just a few hours.

Yeah.

That was the best option.

*…Then why?*

The hulking figure’s eyes widened when Choi Minwoo suddenly stopped walking.

“What’s wrong? Something happen?”

After a brief silence, Choi Minwoo answered.

“No. Nothing.”

“Damn, you scared me. We’re almost there, so let’s join the others. They’ll be chirping away like nervous little chicks.”

The hulking figure shook his head and started down the last corridor leading to the central chamber.

That was when Choi Minwoo noticed his back, bulging beneath the military poncho like a hunchback.

And at the same moment, his tightly shut lips parted.

“What do you think the best choice is?”

“What?”

The hulking figure turned at the unexpected question.

Beneath his raincoat hood, pulled so low it nearly touched his nose, golden hair spilled out as if made of molten gold.

“What’s gotten into you all of a sudden…?”

“I can’t tell what’s right or wrong. What’s the difference between the best choice and the worst?”

Choi Minwoo continued in a hoarse voice. His eyes had begun to tremble, just like the ones he’d seen in the mirror.

“Even now, an enemy ten times our size is heading this way. But if we wait quietly, there won’t be any unnecessary casualties. They don’t know about this place.”

Rumble.

The growing tremors shook the ceiling. The rumbling had grown stronger with every step they’d taken down the corridor.

“If we wait just ten more minutes, it’ll all be over. At least for us.”

The last words fell from his lips, weak and abrupt. The hulking figure’s eyes grew more serious.

“Say what you want to say.”

“Whatever the enemy’s goal, blood is sure to be spilled somewhere nearby. No matter how many of them there are, they wouldn’t move thousands of troops without a reason.”

“Now that you mention it, you’re right. So?”

“Once we’re through this corridor, I’ll give the order as their commander. If you want to make it home alive, hold your breath and wait. Don’t get involved, whether the enemy’s chasing helpless civilians or Hunters.”

Choi Minwoo let it all out at once, like a dam giving way, then took a deep breath.

In the faint light from a bulb nearing the end of its life, he saw the hulking figure’s mouth.

“Yeah, I get what you’re saying. So…”

He was smiling.

“If you’re done with the bullshit, tell me what you really want to say.”

“...!”

“Come on, say it and get it off your chest. Like that guy we know so well.”

Amid the now-uncontrollable rumbling, the hulking figure dropped onto the shaking floor.

As if he wouldn’t take another step until Choi Minwoo answered.

“What, can’t do it like him?”

Instead of answering, Choi Minwoo clenched his trembling fist.

He knew who the hulking figure meant by “that guy,” even without hearing his name.

He’d been watching him from close by for a long time now—Jin Taekyung.

And he knew that no matter what crisis he faced, Jin Taekyung always took responsibility for his actions.

That was a gap Choi Minwoo simply couldn’t close.

“Hunter Jin Taekyung… is different from me.”

“How?”

“I’m weak. I can’t compare to him. And I have a mission I absolutely have to succeed at, as the commander here.”

“Responsibility matters. But that has nothing to do with it.”

Before Choi Minwoo could respond to the cryptic remark, the hulking figure added quietly:

“The others still here are already planning to rush out and fight. Every last one of them.”

“...!”

“I stopped by on the way and told them how many enemies there were. First thing they did was grab their gear. They figure there must be a reason for that many of the bastards to be swarming around. Want to hear the funniest part?”

The hulking figure gave a short laugh.

“I told them to wait for the commander’s orders. They said they figured you’d think the same way anyway.”

He rose and approached Choi Minwoo, who stood frozen like a statue.

And he wasn’t the only one who moved.

“Uh, hey…”

“When are we heading out?”

At some point, Hunters had poked their heads out from the far end of the corridor. The hulking figure shrugged and looked at Choi Minwoo.

“Sounds like they’re ready.”

Choi Minwoo silently looked from the hulking figure to the Hunters, already fully prepared.

Then, slowly.

Very slowly, amid the enormous rumbling that now shook the surroundings like thunder, he drew the sword at his waist.

“This is my answer.”

At that moment—

Shhhhhk! Slash!

The aura surging fiercely along the blade split the shelter’s concrete wall like tofu.

KABOOM!

Debris flew everywhere in the explosion.

Beyond it came the blazing sunlight—and the blood of cursed monsters.

“Not bad for a human.”

The hulking figure, the Skeleton King, laughed aloud and patted the large backpack hidden beneath his poncho.

“Don’t worry. I’ll protect you. You uselessly sleepy human.”

And he shot toward the enemies.

Or he would have.

If not for the answer no one had expected.

“Dad’s not sleeping.”

“…Huh?”
## Chapter artifact 1147

# Chapter 1147

In that brief moment, split into a thousand smaller moments, the Skeleton King thought:

*Have I been feeling a little weak lately?*

Yes. He must have heard wrong.

They said that humans—strictly speaking, he wasn’t human, and certainly not an animal—sometimes heard things that weren’t there when their bodies and minds were weak.

Besides, he was about to fight enemies who outnumbered them by more than ten to one.

With the odds so bad he’d take help from a cat if he could get it, hearing things wasn’t strange at all.

That guy—

No, Jin Taekyung was the most reliable person in the world to him.

But…

*There’s no way he’s woken up.*

It was all wishful thinking.

They’d faced countless dangers on the way to this old, musty underground bomb shelter, but every time, Jin Taekyung’s eyelids had stayed firmly shut without so much as a twitch.

The Skeleton King had even begun to worry that he might never wake up at all.

*That damn human.*

As the Skeleton King thought bitterly to himself, it happened.

Whoosh!

With a sharp whistle, the flow of time—which had briefly stopped—came rushing back like a flood.

KABOOM!

A powerful impact shook the space around them.

The Skeleton King’s eyes grew heavy as he canceled out a dozen or so streaks of light flying through the air.

*This is…*

There was no mistaking it.

Speed and strength on a level entirely different from ordinary monsters.

The Bone Sword trembling in his grasp told him that *those guys* were among the thousands of monsters.

It also told him this battle, now past the point of no return, would be even harder than expected.

“Shit, it’s them!”

“Everyone, switch to a defensive formation!”

They were quick to judge, and quick to act.

Every Hunter here was a skilled veteran with plenty of combat experience.

At the almost simultaneous shouts from the Skeleton King and Choi Minwoo, the Hunters charging behind their commander moved at once, without the slightest hesitation or sign of panic.

Or they did—right up until a low voice stopped them in their tracks.

“Maintain the attack formation.”

“……?”

“……?”

The Hunters, midway through switching to a defensive formation, looked at one another in confusion.

First, because the order had suddenly changed.

Second, because Choi Minwoo—the only one there with the authority to give orders—looked just as strange as they did. Stranger, even.

And third—

*I’ve heard that voice somewhere before.*

He definitely had.

It sounded unfamiliar, yet somehow it stuck with him the moment he heard it.

Though low and hoarse, it carried a feeling that wouldn’t fade.

Perhaps that was why the veteran Hunters, all of them battle-hardened, couldn’t hide their dismay.

And why they left a fatal opening for the enemies right in front of them.

—Grrrrrrrr!

Thousands of monsters surged toward them like a wave, roaring.

Ghouls, Orcs, Lizardmen, and Manticores swung claws and weapons that could tear through steel like paper.

And then—

Whoosh.

A dazzling streak of light shot toward the fearsome monsters.

BOOM!

Flesh and bone exploded into hundreds, then thousands of pieces.

At the same time, countless dying screams burst out alongside sprays of blue-green blood.

In the thick mist of blood that wrapped around them in an instant, those who witnessed the unbelievable scene suddenly understood.

Who had given the order they’d just heard.

Why that low, hoarse voice had felt so familiar.

“Hey.”

Over the Skeleton King’s shoulder, rigid as a statue, a young man suddenly poked his head out of the backpack he’d been carrying.

“You were pretending not to hear me on purpose, weren’t you?”

“……!”

“……!”

* * *

Honestly, at first I thought I was dreaming.

Dreaming of a time before I was even born, when I was busy kicking around in Mom’s belly.

I mean, what kind of person would neatly fold up someone who was asleep and shove them into a huge backpack?

And they’d used those famously tough ogre tendons to tie me up in a turtle-shell pattern like something out of a certain kind of Japanese video. Whoever did this wasn’t just crazy.

Of course, I knew exactly who that lunatic was.

“This guy’s tastes are seriously… No, let’s talk about that later.”

“You, you…!”

Leaving the Skeleton King behind as he stammered, his face like he’d seen a ghost, I put strength back into my stiff body.

Crack, crack.

I snapped the ogre tendons binding me from head to toe like strands of thread, tore through the backpack made of equally tough hide, and stood on my own two feet. Only then could I finally breathe freely.

*How long was I like that?*

Questions lined up at the tip of my tongue, each one demanding an answer.

But I knew it wasn’t the time to ask.

From the moment I regained consciousness until now, the stench boiling all around me and the thick magical power had been enough to make me nauseous.

“Team Leader.”

I gave a slight nod in greeting. Team Leader Choi, looking like he was overwhelmed by a dozen different emotions, finally let out the breath he’d been holding.

“Everyone, form up for an attack.”

At once, the air around us began to boil.

The Skeleton King and Team Leader Choi, whom I hadn’t seen in ages. Along with them, more than two hundred Hunters of various races raised their weapons, eyes alight, and took their places.

Like a single arrow.

And the direction it would fly was already decided.

CRUNCH, clack!

Just as when it first charged out, White Flame returned after piercing through dozens of monsters, trembling in my grasp.

As if it sensed what was about to come.

“Let’s go.”

That was all I said.

Nothing more, nothing less.

The thought became a sound, the sound slipped past my lips—and in that instant, I was already charging at the enemies.

Whoosh.

One step.

I closed the twenty-meter gap in an instant and brought White Flame down without hesitation.

Fwoosh!

Space warped before the deep-blue flames now burning along the spearhead.

Heat so intense it was horrifying swallowed the monsters, and pillars of fire erupted from cracks in the ground, heated like a field of lava.

KABOOM!

Explosions and thunderous noise. Screams burst out from all around.

But I paid no attention to the massive shock wave or the chaos.

No—more accurately, none of my allies did.

Whoosh, whoosh, whoosh!

Flying sparks and pieces of flesh too mangled to make out.

Leaving them behind, more than two hundred Hunters charged like the wind and tore through the enemy ranks.

With a level of force even I hadn’t expected.

Whoooooosh!

In a split second, countless streaks of light dazzled my eyes.

And at the same time, ogre hide—said to be impenetrable even to an anti-materiel sniper rifle—and Manticore tails split apart like tofu, scattering in every direction.

Slash, splatter!

The monsters’ encirclement crumbled amid fountains of dark blood.

The Hunters’ weapons shone fiercely at its center, charged with a power I knew well.

*Auror?*

My eyes widened despite myself.

There was no mistaking it.

Auror, also known as Sword Energy.

A hallmark of A-rank Hunters in the modern world, and the exclusive domain of Peak masters in Murim, it flowed through their weapons.

Not just ten or twenty of them. Every one of the two hundred or so Hunters.

*Why are there this many A-rank Hunters gathered here? The last place I remember being was more than a thousand kilometers from even the nearest ally.*

What on earth had happened while I was gone?

I tried to recall what I knew of the modern world, but it was hard to make sense of the situation.

No.

Before I could even begin to understand the reality in front of me, another unexpected factor got in the way.

Ssssh.

A chillingly low whistle suddenly reached my ears.

My body reacted before my brain. White Flame, which had paused for only an instant, swung down.

Slash, KABOOM!

Everything happened in a flash.

I cut through a crescent-shaped mass of magical power as it flew toward me.

The sticky, cold force at its core swallowed the monsters to either side.

And then—

Splash.

A group appeared in my sight, stepping through a puddle of blue-green blood.

“……What are they?”

Team Leader Choi and the Skeleton King, who had moved up beside me, answered the question that had slipped out on instinct.

“It’s them.”

“Be careful, human. They’re nothing like the monsters you know.”

I looked at the uninvited guests instead of answering.

There were seven of them.

Their appearance was… similar to humans.

More so than even Lizardmen, who at least walked on two legs and could be called humanoid monsters.

But they weren’t human. Not even close.

It wasn’t just their height, well over two meters, or their bulging muscles.

It wasn’t even that they were all exactly alike, with identical height and builds, as though they’d come off the same production line.

*What is that energy?*

Magical power too dense to be human, yet far too pure to be a monster’s.

The Skeleton King had been right.

Each of them was as strong as a named monster, and their magical power was purer than that of any monster I’d ever encountered.

Like beings born with genes entirely free of flaws.

But…

“Yeah. They’re definitely different.”

What the Skeleton King had said a moment ago wasn’t entirely right.

Step.

They weren’t the only ones on a different level.

And they’d picked the wrong person to warn.

Slash.

I moved in that instant—when not a single person there could see or sense me—and felt the touch of the spearhead as it passed through.

*Six left.*
## Chapter artifact 1148

# Chapter 1148

For a martial artist, an increase in martial prowess meant more than heightened senses. It was directly tied to concentration, too.

No matter what happened around him, he could pour out everything he had in a single instant, with a terrifying focus that allowed only one thought.

That was Jin Taekyung now.

Ding.

A familiar chime pierced his ears.

But his senses had been sharpened to the edge of a blade forged by a renowned master. They hadn’t dulled in the slightest.

If anything, they’d grown even sharper.

*What was that?*

The sudden appearance of the mysterious named monsters.

He’d already killed one of them, but before any satisfaction came the heavy sensation transmitted through his spear and an inexplicable wariness. That wariness soon turned into even faster movement.

Flash.

A perfect Shifting Form and Position, leaving not even an afterimage.

Six bolts of magical power shot after him a beat too late and passed harmlessly through empty air. At the same time, White Flame in Jin Taekyung’s hands once again spewed fire.

Fwoosh—KABOOM!

Space warped along the spearhead’s slanting downward arc. Deep-blue flames, carrying a tremendous amount of Scorching Yang Qi, sliced through another named monster.

Or, rather, it looked that way.

At least, until Jin Taekyung felt the powerful recoil through the spearhead.

CRUNCH!

“……!”

Jin Taekyung stared wide-eyed at the named monster hurled far into the distance.

And at the same time, he understood the source of the inexplicable wariness he’d felt when he killed the first one.

*They’re tough.*

He wasn’t talking about their movements or their aura. Quite literally, their bodies were damn tough.

So tough that even he, who had brought down countless enemies, could hardly make sense of it.

*They’re so tough White Flame can’t cut all the way through?*

What kind of weapon was White Flame?

A ridiculously overpowered item of the kind he’d never have even seen if the System hadn’t showered him with all sorts of rewards early on—and a priceless treasure that no amount of money in Murim could buy.

Even the modern world’s artifacts, decked out with cutting-edge technology and all kinds of Magic, couldn’t match White Flame’s natural sharpness and durability.

And yet the monsters’ bodies—especially their bones, which were far denser than he could have imagined—couldn’t be cut like tofu, even by White Flame’s spearhead, wreathed in Force.

Sure, the monster had suffered a horrific wound in exchange. But the fact that it still stood, when it should have been split cleanly in two from collarbone to pelvis, was a shock to Jin Taekyung.

Its incredible regenerative ability, already restoring the wound in an instant, was just a bonus.

“How is this even possible?”

A question slipped from his lips before he knew it. The Skeleton King, who had joined him by now, answered.

“I thought the same thing at first. But when I thought about it, it wasn’t impossible to understand.”

“Why not?”

“If a human as monstrous as you can exist, why can’t monsters like them?”

“Are you kidding? I’m an exception.”

“Do you have to say things that put me off my food like it’s nothing?”

“Food? You’ve really become Korean. Weren’t you supposed to be playing a foreigner?”

The question had been based on reasonable evidence, but Mr. Stone King, from Atlanta, Georgia, had just learned a lot from a marvel of civilization called a smartphone.

“I’m Korean American.”

“……Your way with words has gotten pretty good since I last saw you.”

“Who knows? It’s not the only thing that’s improved.”

WHOOOOSH.

The moment he finished speaking, a tremendous mass of magical power swelled around him.

Jin Taekyung blinked silently at the stark difference in power from before. The Skeleton King shrugged.

“What, are you trembling at my might?”

“……What the hell happened while I was gone?”

“A lot. But there’s no time to tell you about it now.”

The Skeleton King had a clear-eyed grasp of reality.

Not far away, Choi Minwoo was leading the Hunters in a fierce battle against the monsters. The six named monsters had formed a semicircle around them.

Ssshhh.

Materialized magical power rippled like fog.

Behind the skull masks covering their entire faces, their gazes—devoid of even a hint of emotion—stabbed at the two of them like blades.

“Go for the neck. It’s the easiest part to cut.”

At the Skeleton King’s advice, his back now pressed against Jin Taekyung’s, Jin adjusted his grip on the spear and replied.

“I know.”

“We’ll take half each. Three for me, three for you.”

“Can you handle that? You’re weak as hell.”

“Arrogant human. Have you got a knife embedded in your tongue?”

Just then, the Skeleton King stopped grumbling. Then, in a voice so quiet it was almost inaudible, he added:

“Still… it’s good to see you.”

“What was that?”

“I said I’m damn glad to see you again, even if it had to be like this.”

Jin Taekyung wondered what he should say, then simply let out a soft laugh.

Before an awkward silence could settle between them, he pushed off the ground and charged at the enemies.

Just as his monster friend had done, he answered in a very quiet voice.

“Yeah. Me too.”

It all happened almost at once.

The wind rushing over his whole body swallowed his voice.

Jin Taekyung’s form, launched faster than sound, reached the monsters a step ahead of the Skeleton King.

KABOOM!

Three swords clashed with one spearhead, and a deafening roar erupted.

But this wasn’t an even match. The monsters, unable to withstand his power, were driven back, while Jin Taekyung kept advancing.

KABOOM! KABOOM! CRUNCH!

Amid the successive crashes, one named monster couldn’t keep up with Jin Taekyung’s strength and speed and dropped to its knees. He didn’t hesitate.

Slash!

The heavy sensation traveled through the spearhead.

With a strike even stronger than usual, the head wearing a pure-white skull mask floated into the air.

Two swords were already swinging at him from either side, but the attacks came half a beat too late to reach Jin Taekyung.

No—instead, the punch he threw after them struck empty air first.

WHUMP!

Compressed air exploded.

Like striking a mountain to hit the cow behind it, the shock wave burst out in an instant, driving the monsters back and opening a gap.

A tiny opening, but one that could decide the difference between life and death.

Whoosh!

The sequence of movements didn’t need so much as a preparatory motion.

Drawing on physical abilities that made even the word *superhuman* woefully inadequate, Jin Taekyung threw his spear.

THUNK!

The spearhead shot through the air as if plunging down from above, piercing another named monster’s body.

Just as its owner intended, it slipped precisely between its bones.

CRUNCH!

Its skin and flesh, tougher than those of a giant monster like an ogre, were useless this time.

White Flame’s spearhead, forged from Ten-Thousand-Year Cold Iron, did more than pierce its target. It drove deep into the ground. Jin Taekyung left the monster writhing like a fish caught on a harpoon and pushed off the ground.

He unleashed the ability granted to him alone.

*Inventory open. Summon. Summon. Summon.*

Whoosh, whoosh, whoosh!

A dozen or so daggers streaked through the air like beams of light.

By the time the only named monster still standing on two feet swung its sword, brimming with tremendous magical power, and knocked away every dagger, it was already too late.

Slip.

With a movement infused with the subtle principles of Ghost Illusory Slaughter Step, Jin Taekyung plunged deep into the enemy’s reach and swung the last dagger still in his hand.

He spoke in a low voice.

“You’re damn tough, but…”

Slash!

“That doesn’t mean you’re strong.”

THUD.

And just as the towering figure, well over two meters tall, crumpled limply to the ground—

Rumble.

A vast tremor suddenly shook space, and a dazzling flash fell over everyone’s heads.

* * *

Maybe it was thanks to the enlightenment I’d gained over the past few months away in Murim.

I felt a sense of déjà vu before anyone else, and at the same time became aware of a tremendous presence suddenly looming high overhead.

*Shit, again?*

Perhaps it was only natural, but the first thing that came to mind in this situation was the arrival of yet another unexpected enemy.

Another powerful being like the mysterious named monsters I’d taken down—and the ones the Skeleton King was still fighting.

Maybe that was why everyone on the ground froze as the powerful rumbling shook the sky.

But why?

A foreboding prediction flashed through my mind like lightning, yet the red warning light that always blared with my instincts stayed quiet, even as the flash swallowed the sky.

No. The larger the flash grew, the calmer I felt.

The Skeleton King, who had just taken down a second named monster and was fighting desperately against the last enemy, didn’t feel the same way.

“Uh? Uh, hey!”

His pupils were shaking like an earthquake measuring 8.0, complete with a tsunami.

He glanced up at the sky with a look that said, *What the hell is that?* Then he shouted at me, standing stock-still.

“What are you doing? Quit gawking and do something!”

“Okay.”

I obediently raised both hands and waved.

At the sky.

“What are you doing, you bastard?!”

“Waving hello.”

“……What?”

He clearly couldn’t understand, despite my helpful explanation. I gave him a grin.

“Someone came a long way to get here. The least we can do is say hello.”

“What the hell are you—”

The Skeleton King could hold it in no longer. He burst out in anger—

And at that very moment—

FLASH!

The light gathering in the sky exploded.

And amid the distant flash that covered everything around us, a different, destructive energy suddenly surged.

WHOOOOOSH!

I spread my arms even wider.

Toward the countless streaks of light raining down like lightning, like arrows, accompanied by a fierce whistle—and aimed only at the monsters.

Toward the one who had set all of this in motion: my friend, a great Grand Mage.
## Chapter artifact 1149

# Chapter 1149

The battle didn’t take long to wrap up.

By the time most of the seven named monsters—the ones who’d been acting as leaders—were dead or incapacitated, the tide had already turned sharply in our favor.

On top of that, humanity’s greatest War Mage had appeared and immediately pulled the plug on the monster army’s life support.

KWA-BOOOOM!

Spells rained down without pause from dozens of meters above us, turning over the earth and sending blood spraying everywhere.

His accuracy was almost perfect, as if he were sniping his targets.

And so the battle ended.

What followed was nothing more than a one-sided massacre.

“Charge! Wipe them all out!”

CRUNCH!

With me, the Skeleton King, and Team Leader Choi at the center, some three hundred Hunters advanced like a wave, swallowing up enemies more than ten times their number.

Slash, splatter!

I cut and stabbed at every enemy that came into view.

The medium and large monsters that trusted their strength and fought to the end—and even the ones who had only just gotten scared and turned their backs to run.

No exceptions. No mercy.

After about thirty minutes of pursuit and slaughter, there wasn’t a single monster still standing on two feet in this blood-soaked desert.

Well.

Actually, there was one.

“Thankfully, we didn’t suffer any casualties… What’s that insolent look for, human?”

The Skeleton King had started toward me, then hesitated and stopped. I glanced over at him.

“Hmm. It’s nothing.”

“Looks like something to me.”

“There are exceptions to every rule. Right?”

“Where’d that come from?”

“It’s a thing. It has nothing to do with you, so don’t ask.”

He narrowed his eyes, apparently picking up on something suspicious, but thankfully I wasn’t subjected to any further interrogation.

A massive shadow, cast by someone standing with the sun at their back, fell over my head like a lifeline from heaven.

“Good gentlemen. I have a question for you.”

Dark-brown skin like dark chocolate. Muscles that strained the imagination. And on top of that, a staff that looked more vicious than most close-combat weapons.

The huge Grand Mage slowly descended from the air and continued in a trembling voice.

“What I’m looking at right now isn’t some damn mirage or illusion spell, is it?”

He stared at me with disbelieving eyes. I slowly held out a fist and answered.

“Why don’t you check?”

“Oh, damn it. Jin?”

Magic Johnson, the Grand Mage of the United States, pulled me into a tight hug instead of bumping fists.

Squeeze.

“……”

The firm, heavy thing poking me in the stomach right now was probably his staff.

It had to be.

* * *

It took Magic Johnson quite a while to calm down. Fortunately, all that excitement had come from the joy of seeing me again.

Yeah. No matter how black he was, no one could be that big and that hard.

“Dear God. I can’t believe it, even with my own eyes. When did you wake up?”

Magic Johnson had only just begun to regain his composure. I’d barely managed to escape the massive embrace of the Grand Mage, a man of the physical school, before answering.

I instinctively glanced at the staff tucked into his belt.

“Not long ago. I can barely believe it myself.”

“Ah, I see. The last time I managed to get in touch, I still hadn’t heard you’d woken up.”

“What?”

At that peculiar choice of words, I felt the foreboding I’d been struggling to suppress begin to stir inside me.

What kind of world was this modern one, anyway?

Humanity had flourished so brilliantly that even the word *global community* no longer seemed big enough to describe it.

They’d added Magic, a supernatural power, to the most advanced technology they already possessed. It was only natural that civilization, reborn from the ashes of the Great Cataclysm, would shine more brightly than at any other time in human history.

And yet…

*The last time he managed to get in touch?*

For a moment, I couldn’t make sense of what those words meant.

Magic Johnson was a Grand Mage.

One of only three masters of Magic among billions of people—or, now, one of only two.

As a War Mage, most of his Magic was related to combat, but a Grand Mage was someone who could turn imagination into reality.

With a single teleportation spell, he could cross hundreds—or even thousands—of kilometers. And if the conditions were right, he could contact someone just as far away whenever he wanted.

So what he’d said was more than strange. It was downright ominous.

He sounded like a signalman barely managing to contact his allies with a busted communications device.

And all of this was whispering the same thing in my ear.

That it was finally time to face reality.

“Johnson.”

“Yeah?”

“When was that last contact?”

“Well…”

Magic Johnson trailed off. Only then, as if he’d realized something, did he turn toward the Skeleton King beside him.

“Could it be…?”

The Skeleton King muttered like he was trying to defend himself.

“Damn it. I didn’t have time to tell you.”

“……Shit.”

“I couldn’t have told you, either.”

More precisely, I hadn’t been able to bring myself to ask.

I’d been that afraid. That scared.

*How long?*

What had happened while I was gone? How much time had passed?

I let out a quiet, trembling breath. At the sight of me, Magic Johnson heaved a deep sigh.

“Fuck.”

It was a painful situation for the one who had to speak and the one who had to listen.

But the longer we put it off, the more it would hurt.

“Tell me. Right now.”

And the very next moment, the answer I’d been waiting for came from over Magic Johnson’s shoulder.

“The last contact was one day ago—exactly twenty-one hours ago.”

It was Team Leader Choi.

His armor and sword were caked in dried monster blood and flesh, and his eyes were as dry as sand. They drove into my vision like awls.

“The first contact was three hours before that.”

Twenty-four hours. One day.

The number slipping through Team Leader Choi’s lips swelled to a weight thousands of times heavier, crushing my chest.

It washed my vision white, brighter than all the flashes Magic Johnson had unleashed at the monsters combined.

*No way.*

A time difference that dwarfed every ratio we’d seen so far.

But that wasn’t all.

Even before Team Leader Choi spoke, I’d already sensed it instinctively.

A far crueler truth was waiting.

“And…”

In the vast silence pressing down on us from every direction, Team Leader Choi took a deep breath. Then, his voice trembling, he continued.

“Today is the tenth day since you lost consciousness.”

“……!”

At that moment—

BOOM.

Along with the ominous, low rumble of a war drum, a new kind of System window—one I’d never seen in Murim—appeared before my eyes.

> **System**
> The trigger has been activated due to the failure of Main Quest Cataclysm.
>
> **Mission:** Prevent the Summoning (Failed)
>
> You defeated the “The Final Abyss” Doppelganger, but failed to complete the mission.
>
> As a consequence of the Main Quest failure, the boundaries of the Demon Realm have partially opened. Unknown beings, never before known to exist, are invading this world.
>
> A rift is in progress. Its progress will change when certain conditions are met and can be checked through the System.

The words were the same ones that had been etched clearly in my last memory of the modern world.

But over them, on a new holographic window, was a name for a being I’d never seen or heard of before.

> **System**
> An unknown being willingly answers the summoning.
>
> The immense shadow of Black Dragon Duke Morgoth[^1] has fallen over this world.
>
> Would you like to view the new Main Quest, Rift and Collapse?

I stood frozen like a statue, then suddenly remembered.

The enormous wings I’d seen in that meaningless nightmare on my last night in Murim.

The dragon’s roar, shaking the sky swallowed by darkness.

* * *

He was, in truth, a man of utter darkness.

His hair fell all the way to his calves, and his eyes looked as if they’d been set with obsidian.

The only part of him that wasn’t black was the irises around his pupils. They shone silver—brighter than white—and were so captivating they seemed to draw the viewer in.

At least, that was how they might have affected someone other than the old man looking back at the man who had just entered his office, his gaze calm.

Step. Step.

Footsteps rang out through the silence.

Only after the man had crossed the long carpet and come right up to him did the old man abruptly speak.

“You have no manners.”

In response to the man’s gaze, the old man continued.

“If you’re a guest, you should wipe your shoes before coming in. You’ve dirtied the carpet.”

“Ah.”

At the quiet exclamation that slipped from the man’s lips, the old man felt something stir deep in his chest.

If it weren’t for the bits of human flesh and blood scattered here and there along the man’s path, he might have felt boundless affection for him.

“My apologies. I’m still a little clumsy with things like this.”

The man smiled gently and held out his hand.

His movement was perfectly natural, despite what he’d just said.

“Ah, did I get it wrong again? I was told this is how you do things.”

The old man paused for a moment at the man’s puzzled tilt of the head, then answered.

“No. I was only surprised by how skilled you were. Your appearance—and that handshake just now.”

The gesture had been more than natural. It was graceful, even elegant.

And his appearance was so beautiful he could be called the most beautiful human in the world.

But the old man knew the truth.

He had seen it with his own eyes.

A little over ten minutes earlier, the man before him had erased the Red Square he loved with a single gesture.

“So, Morgoth. What brings you here?”

Vladimir Furin, the Russian autocrat, gritted his teeth as he clasped the hand of the monster wearing a human face.

[^1]: “Duke” renders the noble title 公 in the name 黑龍公.

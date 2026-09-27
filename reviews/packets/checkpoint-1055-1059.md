# Checkpoint Review — 1055–1059

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

# Chapters 1055–1059

## Plot

Sama Pyo returns to his dying father, Sima Gong, who admits betraying the Gansu sects and the Kongtong Sect. Pyo accepts responsibility for concealing the truth and proposes sacrificing the Black Dragon Demon Gate’s leaders and compensating those seeking revenge. Sima Gong approves of his resolve, but dies before finishing his final words.

Jin Taekyung, near collapse while fighting the remaining Dark Heaven cultists, is rescued by Taishan and the others, including Sama Pyo. After Dark Heaven’s army is annihilated, Pyo says he will leave the Fire Dragon Pavilion and face his burdens alone. Taekyung insists he still trusts Pyo as a friend.

Pyo approaches Perfected Being Hyeoncheon, the Kongtong Sect Leader, who came with roughly a hundred surviving Disciples to confront the Gansu leaders over the betrayal at Dunhuang. Learning that Sima Gong, Song Il, and Hwangbo Eom are dead, Hyeoncheon wounds Pyo but spares him, rejecting collective vengeance and telling his Disciples to grieve. Taekyung stops Taishan from charging the Kongtong Disciples, knocking him unconscious.

Jeok Cheongang and the Bow Saint return with a foul-smelling, weeping man. Jeok calls him a madman; some mounted bandits address him as Great Sir.

## Continuity

- Sima Gong is dead. Sama Pyo accepts responsibility for concealing his father’s betrayal and says he will leave the Fire Dragon Pavilion to face his burdens alone; Taekyung still trusts him as a friend.
- The allied forces annihilated Dark Heaven’s army. Hyeoncheon spared Pyo after wounding him shallowly and says the Kongtong Sect will pursue revenge without punishing people for their kinship.
- Taishan charged toward the Kongtong Disciples; Taekyung stopped him by knocking him unconscious.
- Some Kongtong Sect survivors vanished to an unknown location.
- Jeok Cheongang and the Bow Saint returned with an unidentified, foul-smelling man whom Jeok called a madman; some mounted bandits call him Great Sir.
- The Lord of Heaven’s identity and connection to Asmodeus remain unknown. The Grand Mage departed for Qinghai on a new mission; the other servant’s identity is unknown. The mysterious green light remains unexplained.

## Translation Decisions

- Render 풍운아 as “bold hero of changing fortunes” in Sama Pyo’s ironic self-description.
- Preserve the wordplay in 최선(最先) and 최선(最善) as the contrast between “what comes first” and “what is best.”
- Render 전멸 as “annihilation” in the military-definition passage, preserving the narrator’s distinction between that term and the literal slaughter he sees.
- Render 혈의인 as “Blood-Clad Men”; they are identified as Kongtong Sect Disciples.
- Render 대인 as “Great Sir” when the mounted bandits address the unidentified man.

## Durable state

{
  "active_continuity": [
    "Hyeoncheon spared Sama Pyo after wounding him shallowly; he declares that the Kongtong Sect will pursue revenge without punishing relatives for their kinship.",
    "Taishan charged toward Sama Pyo, and Taekyung stopped him by knocking him unconscious.",
    "Hyeoncheon tells the surviving Kongtong Disciples to grieve for their dead.",
    "Some Kongtong Sect survivors vanished to an unknown location.",
    "The Lord of Heaven’s identity and connection to Asmodeus remain unknown.",
    "The Grand Mage departed for Qinghai on a new mission; the identity of the other servant remains unknown.",
    "A mysterious green light remains in the dispersing darkness.",
    "Jeok Cheongang and the Bow Saint returned with an unidentified, foul-smelling man whom Jeok called a madman; some mounted bandits call him Great Sir."
  ],
  "continuity_sources": [
    1058,
    1059
  ],
  "open_questions": [
    "What are the identity and purpose of the Lord of Heaven, and is he connected to Asmodeus?",
    "Where did the missing Kongtong Sect survivors go?",
    "What is the new mission in Qinghai, and who is the other servant there?",
    "What is the mysterious green light?",
    "Who is the foul-smelling man, and why do some mounted bandits call him Great Sir?"
  ],
  "safe_through": 1059,
  "temporary_decisions": [
    "Render 대인 as “Great Sir” for the mounted bandits’ address to the unidentified man."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 1055

# Chapter 1055

Time kept flowing, just as it always had.

Even around the time the conversation between two master and servant figures ended in a dark space with no way to tell how far away it was—or where it was.

Even now, as a young man suddenly stopped in the middle of a snowfield whose original, pure-white color had long since been lost to red.

*Squish.*

Cold. Sticky.

The pool of blood sloshing around his ankles held the deaths of dozens of people.

At the same time, it was the future of someone waiting in that blood, waiting for death to slowly draw near.

“So this is where you were.”

*Kh—cough.*

At the young man’s words, which slipped unexpectedly past his lips, the Black Night King Sima Gong blinked. He had been coughing with difficulty.

A face almost exactly like his own appeared in Sima Gong’s bleary eyes—a face he’d thought he would never see again in this life.

“How…”

His words trailed off.

But his surprise lasted only a moment. His son had returned before he knew it. The father studied him, then spoke in the same calm voice as always.

“I thought you’d gone far away. Why have you come back here?”

“It was too far for me. As I am now.”

The young man, Sama Pyo, answered, then abruptly turned his head to look somewhere.

Amid the relentless, fierce roar of battle, powerful fighters swept through the remaining enemies, scattering destructive flashes of light.

And at their center stood Jin Taekyung, the Blazing Flame Divine Dragon.

“Maybe… it wasn’t time yet.”

He had wanted to reach him, but couldn’t. He had wanted to help, but in the end had no choice but to turn back.

Sama Pyo already knew.

The reason Jin Taekyung’s distance from him—only a few hundred *jang*—had felt like tens of thousands of *ri* was his own inadequacy.

And yet, in another part of himself, he stubbornly denied it.

Denied that there was another, true reason he had come back.

“So you passed up all those roads just to come back here?”

“I only happened to see you.”

*You.*

It was a thoroughly dry way to address his father, but Sima Gong merely nodded in silence.

“An accident. Yes, I see.”

“Yes. An accident. All of it.”

Despite the words they exchanged, the father and son both knew.

None of this had been an accident. It had been a choice.

And though they knew that, neither of them saw any need to say it aloud. The two of them resembled each other more than anyone else.

“How is the battle going?”

“Is that really important to you? When you don’t even know how long you have left to breathe?”

“My death is the future. The battle is the present. Nothing matters more than the present before us.”

He was as good as standing at death’s door.

Yet his father’s reply was utterly firm. Without realizing it, his son gave a hollow laugh and answered.

“It’s practically over. The enemy leaders are all dead or have fled. The rest will be wiped out before long.”

Sama Pyo’s words were the plain truth, no more and no less.

The scales that had once tilted toward a victory for Dark Heaven had long since been shattered.

The Blood-Sword Demon Lord and the mages were all dead, and the Grand Mage had vanished like a phantom.

Now even the powerful Black Ghosts were gone. With the mysterious reinforcements who’d arrived on the battlefield, led by the Kongtong Sect, the allied forces were running wild.

Before long, the battle that had stained this vast snowfield with blood would be over.

No—it was already over.

All that remained was the slaughter and butchery that would continue under the name of battle.

Sima Gong, whose fading consciousness had kept him from knowing any of this, gave a small nod only after hearing the whole story.

“A great victory.”

“A great victory. Ours.”

“Ours. Yes, I suppose you can think of it that way now. The Kongtong Sect might see things differently, of course.”

“The Kongtong Sect…?”

“You don’t need to pretend you don’t know. You’ve already guessed, haven’t you? That the great defeat at Dunhuang wasn’t an accident.”

Despite the unforgivable crime of betrayal, Sima Gong confessed with pride and composure.

To the child who resembled him more than anyone else.

“Yes. It’s just as you suspect. I goaded the Gansu sects that opposed me into banding together with the Kongtong Sect to defend Dunhuang, then passed information to the Blood-Sword Demon Lord. I knew what was happening beyond the desert, but I didn’t tell them. If it weren’t for those mounted bandits who came from Ningxia, things wouldn’t have gone the way they did.”

“……!”

“Are you surprised? Or angry? But whatever you think of me, I have no regrets. It was a choice made for practical gain and survival. Nothing more.”

After pouring out those words, Sima Gong looked his son straight in the eye.

Practical gain and survival.

Yes. That was all.

It had always been that way.

He had lived his whole life as a member of the unorthodox faction, and had always been forced to gamble dangerously to build up his power—a force weaker than even the Demonic Path and the orthodox faction, not to mention the dark-path figures.

Just as, after careful calculation amid the great upheaval of the Great Faction War, he had chosen the orthodox faction and claimed the rights of the victors.

The son who had been looking down at his father in silence suddenly spoke.

“Why did you do it?”

“I’ve already told you everything.”

“I’m not asking why you betrayed them. I know what kind of person you are.”

“Then what are you asking…?”

“Why? Why did you make that choice? You, who chased survival and practical gain so ruthlessly—why?”

At the depth in his son’s eyes, the father finally understood what his flesh and blood was asking. What answer he wanted.

But after a short silence that felt like an eternity, Sima Gong’s voice finally slipped through his lips, low and cold.

“You still have a long way to go.”

“What… What does that mean?”

“The past is past. The reason for it doesn’t matter in the least. As my heir, you should have asked what lies ahead. That is what it takes to be a Sect Leader.”

“……!”

“Everything now falls into your hands. Your household and sect, vast lands and untold wealth… and, most importantly, the grudges you’ll have to deal with. And yet you’re so curious about what’s already past?”

Sima Gong let out a mocking laugh at his heir.

“My judgment was wrong. You’ll soon gain half of Gansu, but before long, you’ll lose all of it. Wolves and vultures that have caught the scent of blood will come from every direction to tear the Black Dragon Demon Gate apart.”

Thousands had already died in Dunhuang alone because of the betrayal.

The Kongtong Sect had suffered damage on a scale comparable to—or greater than—what it had suffered during the Great Faction War. The same was true of the many sects that were little more than the roots of the Gansu martial world.

Sima Gong could guess what would happen if the truth came out.

If Dark Heaven, betrayed for the second time, let even a little information slip, the name of the Black Dragon Demon Gate would disappear from the world.

Even the Zhongnan Sect, one of the Nine Sects and One Gang, would hardly be an exception.

Because of the crimes committed by the Roaring Fury Swordsman and the Taeeul Merciless Sword—whether they were alive or dead—the Zhongnan Sect might have to close its gates, too.

But…

*Even if the sky falls, there’s always a hole to crawl out of. There’s always a way.*

Just as Sima Gong murmured to himself, Sama Pyo, who had been watching him with an indescribable expression, finally opened his firmly closed lips.

“There’s another way.”

“What?”

“There’s a way to save the Black Dragon Demon Gate. A way to escape the wolves and vultures closing in from every direction.”

For an instant, a strange glint flashed in Sima Gong’s eyes.

“Blood must be repaid with blood. That is the law of the martial world. They will never forget what the Black Dragon Demon Gate has done.”

“Half right, half wrong.”

Sama Pyo answered quietly, then continued.

“Blood should be repaid with blood. But not everyone in the Black Dragon Demon Gate needs to bleed.”

“……!”

“Am I wrong?”

A heavy silence fell between them.

Screams and shouts continued without pause, yet in that moment it seemed as if every sound around them had vanished.

At last, a low voice slipped through one of their lips.

“Yes, you’re right. The body itself is innocent. It only did what the head told it to. Isn’t that so?”

At Sima Gong’s question, Sama Pyo answered in a calm voice.

“If the heads alone don’t satisfy them, I’ll have to be prepared to cut off the limbs one by one.”

“So you intend to cut down your father, along with the senior members who followed my orders. Every last one of us.”

“There are too many guests coming to us with grudges. Even if each one takes only a sip to wet their throat, they’ll need a lot of blood.”

“Guests, is it? If you’re welcoming guests rather than facing enemies, then you, as their soon-to-be host, will have to make the arrangements yourself.”

“If I cut off the Gate’s head and arms myself and offer them up, then propose reasonable compensation, their grounds for revenge will crumble.”

“Yes. It can’t be helped. Even if someone calls the son who killed his own father a disgraceful wretch…”

“More people will call me a bold hero of changing fortunes. A Great Hero of Benevolence and Righteousness, willing to go so far as to violate filial piety for the world and for the greater good.”

At that reply, delivered without hesitation, Sima Gong stared at Sama Pyo, his face stiff.

At the son who dared to say he would kill his own father with his own hands.

Then, in the next instant, his face broke into a smile as if it had never been stern.

“Truly… excellent.”

Forgetting for a moment even the terrible agony that wracked his whole body, the giant who had ruled the unorthodox faction for decades burst into a hearty laugh.

“Yes. This is exactly the kind of person I wanted you to become. That’s why I chose you as my heir.”

At that moment, the Black Night King Sima Gong was genuinely glad.

Glad that his choice hadn’t been wrong.

Certain that everything he had built over the course of his life could be passed on to a worthy heir.

Eight sons and nine daughters.

Sama Pyo was the eighth son and the seventeenth—and last—child.

The youngest and most talented of them all, he was the true heir. And now, at last, he had grown into a proper member of the unorthodox faction.

A true member of the unorthodox faction—someone who could kill even his own father, and pursue practical gain and survival with a cool head in any situation.

*That settles it.*

At the end of a long, hard-fought life, Sima Gong was ready to accept death with a relieved smile.

At the same time, he parted his bloodied lips to speak to Sama Pyo, who was lifting his treasured weapon, the Black Dragon Saber, out of the pool of blood.

To the unorthodox faction’s new ruler, who had grown from an immature son into the Sect Leader of his own sect.

“Go ahead and strike, Sect Leader.”

At the instant his voice rang out, polite in the extreme—

*Shwaa!*

A brilliant streak of light flashed before his eyes.
## Chapter artifact 1056

# Chapter 1056

*Shwaa!*

The flash that tore through the wind was razor-sharp and perfectly aimed.

The Black Dragon Saber.

The treasured blade had been a gift from his father—the first and last he had ever received from him. Its owner had been only a boy in his teens, yet he had distinguished himself so early that his youth hardly mattered. Now the blade followed its master’s hand and cut cleanly through the target before him.

*Shhk!*

Blood sprayed with a cold, slicing sound. A pair of eyes that had watched the whole thing sank deeply.

“What have you done?”

The question held a great many things, but the answer was simple.

“Because this isn’t the path I want.”

Sama Pyo let go of the hilt, already cold beneath his hand.

The keen blade, a weapon permitted only to the heir of the Black Dragon Demon Gate, had passed just beside Sima Gong’s nose and cut through the pool of blood.

As if mocking the father who had been glad to see his son become a true man of the unorthodox faction—and had willingly accepted death.

“This is my choice. The path I, Sama Pyo, have chosen—the man who will succeed you as Sect Leader of the Black Dragon Demon Gate.”

“Why…!”

Sama Pyo calmly met Sima Gong’s gaze as he shouted, his voice boiling with blood.

“Because it isn’t right.”

“What?”

“Because it isn’t what comes first, or what is best.”

For Sama Pyo, this wasn’t a question of what came first.

It was a question of what was right—and what was better.

“I’d forgotten for my whole life. No—I’d grown so used to it that I kept pretending not to know. But not anymore.”

His life in Gansu had been one long struggle.

Like the siblings born before him, the youngest of the Sama family had fought desperately to avoid being cast aside.

They were family, bound by the same blood, and rivals competing for the one and only position of heir. They were little more than soldiers, obeying the one man who had given them that blood.

The kind of people who sometimes had to face even death without hesitation.

*“Father, Second Brother…”*

*“I’ve already heard from the messenger. We’ll hold the funeral after we’ve wiped them all out. Understand?”*

Sima Gong had been a cold conqueror. Unifying the unorthodox faction demanded blood and sacrifice.

It was an open secret that more than five of Sama Pyo’s brothers and sisters had died as the Black Dragon Demon Gate brought every unorthodox faction in the land under its banner and rose to stand alongside the Kongtong Sect.

No one knew that the Black Dragon Demon Gate’s youngest young lord, chosen as heir while still in his teens, wasn’t as cold as he seemed.

*“Why are you crying so bitterly?”*

*“Father helped Black Dragon Demon Gate. But he died. Taishan sad.”*

*“……!”*

*“Need to find body. Taishan needs to bury father. But, but those people said they don’t know. Taishan sad.”*

*“……You said your name was Taishan. Come with me.”*

Sama Pyo had found the father of the huge boy who was crying, then carefully buried him. He had been wearing the Black Dragon Demon Gate’s uniform, surrounded by a flock of crows.

And Sama Pyo had made his first friend.

A friend more precious than family—the only one who cared for him more than his own father did.

But he hadn’t imagined that he would make other friends more than a decade later.

“Living with them taught me that in the end, everything changes according to the choices I make.”

The Fire Dragon Pavilion.

Despite its grand name, it had fewer than ten members. Among them, Sama Pyo had found a new path he’d never known existed.

There were no shackles or labels there.

They always trusted one another and fought together, and that was how they overcame each crisis.

Perhaps that was why.

Why Sama Pyo had looked back on his past again and again.

Why, at some point, he had begun to feel something unfamiliar toward his father, a man of ice and stone.

“Then, out of nowhere, I thought: when you look at it closely, you’re a rather pitiable man.”

“……!”

“You probably weren’t like this from the start. Little by little, ambition took hold of you. And one day, you began using any means necessary.”

The son who once couldn’t bear to meet his father’s cold gaze was gone.

Now, in this moment, Sama Pyo looked at his father, who stood on the brink of death, his eyes calm but full of sorrow.

“It wasn’t an accident.”

“What… do you mean?”

“I didn’t happen to come back. I came to see you through your final moments. Not as the heir of the Black Night King, but as the son who carries Sima Gong’s blood.”

*Splash.*

“Do you know?”

Sama Pyo sat in the pool of blood and met his father’s eyes. Watching his trembling pupils, he continued slowly.

“No son in this world can kill his father.”

“……!”

“I’ll tell them everything myself. I’ll also confess what a pathetic son I’ve been—turning a blind eye to your betrayal even though I knew the truth.”

“You…”

“I’m not asking to be forgiven. I’m choosing to bear it.”

At that peaceful answer, as if he had accepted everything, Sima Gong could say nothing.

He could only struggle to hold back a feeling he’d forgotten for so long, one that had suddenly come back to him here, today.

As his vision slowly dimmed, his breath grew short, hinting at the end.

“You asked why I did it. Why I, who’d spent my whole life chasing survival and practical gain, made such a foolish choice…”

To save the heir who would inherit everything he had?

No. That wasn’t it.

At least in that moment, Sima Gong knew there had been another reason.

He was simply too late to confess it.

“I, your father…”

Facing the son who had returned to see his father’s last moments, Sima Gong squeezed out his remaining strength to speak.

He didn’t even realize that this was his final breath.

*Slump.*

His head suddenly drooped.

The son looked toward his father, who had met death in a wretched state, as if paying for the sins of his life. Then he whispered quietly.

“I heard you. Clearly.”

The pool of blood soaking father and son trembled faintly as Sama Pyo’s shoulders began to shake.



* * *



Highly trained hunting dogs always obeyed their master’s commands.

They fixed their eyes on the prey their master pointed out, bared their teeth and growled, then, the moment their leash was released, charged forward with all their strength and tore into it.

Until their prey stopped breathing.

Or until their master ordered them to stop hunting and return.

Just like now.

*Shwaa!*

A fierce, piercing whistle and a flash of light came from the side.

But speed was always relative.

The Sword Energy that surged along the white blade and fell toward my crown moved with the lightning-fast speed of a Peak master. But to me, it didn’t.

*Shhk!*

Space split in an instant.

A fraction of a beat later, the slicing sound rang out. Everything within the path of the silver-white spearhead had been cut apart.

The Sword Energy went out like a candle before the wind.

The sword that held that mighty energy.

And finally, the body of the person who had launched this futile attack.

*Fwoosh!*

A tremendous fountain of blood burst from the body, split cleanly without a single ragged edge. But I didn’t even blink at the gruesome sight.

Neither did the other hunting dogs charging from every direction, even now.

*Thud, crunch! Whump!*

I drove my spearhead into the chest of the first enemy charging straight at me, then crushed the face of another who came at me from the blind spot with one punch. At the same time, I yanked out the embedded spearhead and swung it.

“Ghk—kgh.”

*Thump.*

Three Peak masters fell as their dying cries served as their last words.

No—not three masters.

Three corpses.

But the battle frenzy sweeping across the blood-soaked snowfield showed no sign of easing.

*Shh-shh-shh-shhk!*

The Dark Heaven cultists charged in without allowing even the briefest gap, rushing to fill the space left behind.

Looking at their blank expressions and emotionless eyes, I felt the crushing exhaustion weighing down my whole body.

*How many is that now?*

I had no idea.

I had neither the time nor the reason to count every enemy who had died by my hand.

I just had to fight. Keep knocking them down.

Those soulless wooden puppets.

Those hunting dogs, those moths to the flame, blindly carrying out their final orders even though the master who held their leash was gone.

Of course, I knew what this was.

A one-sided massacre. Slaughter.

But I had to do it.

It was the only way to end this blood-soaked battle, and the only way to save as many allies as possible.

So I had no choice but to cling with all my strength to the thread of consciousness that felt ready to snap at any moment.

*Come on.*

I muttered the words to myself and charged toward the enemy.

Or tried to.

That was when my vision began to fade.

“……!”

A red alarm bell rang in my head.

My mental strength had reached its limit long ago. Now, unable to endure any longer, it was sending me a warning.

But by the time I gritted my teeth and forced my eyes open, it was already too late.

*Shwaa!*

From my slanted, blurry view, a dozen blades came raining down on my body as it staggered without my realizing it.

Faintly. Slowly.

The problem was that, as keen as my eyes were, the brain that needed to send quick commands to move my body had frozen like stone.

*Damn it.*

In the slowed-down world, I cursed under my breath.

These men weren’t the Blood-Sword Demon Lord, the Grand Mage, or even close to the Black Ghosts.

No—they were far weaker.

The gap was so wide that under normal circumstances, I would’ve scoffed at them.

Even so, I had a gut feeling I wouldn’t be able to dodge all their attacks.

And, even as my body refused to move, one ridiculous thought crossed my mind.

*If I level up, does that maybe heal me even if my limbs get cut off?*

Fortunately, nothing happened that forced me to worry about the unpleasant first-time experience only someone like Cheongpung might look forward to.

The next moment, an enormous whistle rang out from somewhere and swept all my worries away.

*Whoooosh!*

It happened in the blink of an eye.

Over the shoulders of the enemies charging toward me, a huge shadow suddenly surged upward. Along with it, the two-section staff—big and beautiful, just like its name—sliced through the air like a bolt of lightning.

*Craaaack!*

If someone asked whether I’d ever seen five heads blown away with a single whack of a bat, I’d nod without hesitation.

I could even tell them the name of the top prospect who’d be bombing today’s modern Major League, now turned into a playground for Awakened Ones.

Of course, that lunatic hulk would introduce himself before anyone else could tell you.

Just like now.

“Taishan! Came! Saw! Hit!”

“Well done! Now, Body Slam!”

Starting with Namho, perched on the shoulder of Taishan—who had just delivered a line to rival even Julius Caesar—familiar faces burst out like streaks of light.

“Young Master! No, Benefactor! No, Captain!”

*Shhk!*

Ju Hwaran split an enemy’s skull while blurting out a three-step change of address that even Transformers would’ve had trouble keeping up with.

“Fools! How dare you try to harm the Captain! Your courage is admirable, but to do that, you’ll have to get through me—the Captain’s right arm and heart! I, Hyuk Mu—whoa, shit!”

*Clang!*

Hyuk Mujin had charged in with a grand entrance, only to stumble back in a panic when an unexpectedly stronger enemy counterattacked.

“Uh, does that guy know how to fight without running his mouth?”

“You should start by keeping yours shut.”

*Thrust!*

Song Ilseom and… wait, who was that black, shaggy old guy? Together, they saved Hyuk Mujin and cut down the remaining enemies in a flash.

“The Seven Masters of the Black Horse?”

The four syllables suddenly slipped out of my mouth. The middle-aged man, a former mounted bandit, twisted his already fearsome face.

“Not Black Horse—White Horse! I’m Ma Junggeol, eldest of the Seven Masters of Baekma Bang! Who do you think I went through all this shit for? And you forgot me…!”

“Lower your voice. While I’m asking nicely.”

At Ju Hwaran’s chilling warning, Ma Junggeol clamped his mouth shut. A laugh escaped me before I knew it.

Just because it was nice to see.

Because I knew we hadn’t lost anyone.

And…

Because I could see the one last person I’d thought I’d never meet again.

“You made it?”

At my abrupt question, Sama Pyo, who I hadn’t even seen arrive, shrugged.

“Am I late?”

No.

Not at all.
## Chapter artifact 1057

# Chapter 1057

No further surprises occurred in the great battle that day across the vast snowfield.

Just a few hours earlier, the forces of Dark Heaven had flaunted their overwhelming might. Now they were no more than candles before the wind, while the allied forces—led by Supreme Peak masters and wave after wave of reinforcements—were like a tremendous storm.

A storm made of steel and killing intent, tearing through everything in its path.

*Crraack!*

*Thud! Shhk!*

Fountains of blood erupted all around them.

With thick blood mist draped over them like cloaks, the allied soldiers charged, stabbing and cutting down every enemy in their path without the slightest hesitation.

An eye for an eye.

A tooth for a tooth.

And death repaid with death. That was the law of this world—the Murim—and the very essence of war.

“Heaven above and earth below, all demons—”

*Thwack!*

A guard’s spear pierced his arm. Arrows and swords flying from somewhere slashed through his face and chest.

Before they could finish their eight-character doctrine, the enemies fell, spraying blood. The allied forces trampled over their bodies and closed in around the enormous slaughterhouse.

Quickly. Ferociously.

Against Dark Heaven’s cultists, who had lost their reason, words like *persuasion* and *capture alive* were luxuries. The immense sacrifices the allied forces had made here today had left them with no mercy to spare.

Least of all the band of fighters who had joined last, yet were now sweeping through the enemy ranks at the very front.

*Shh-shh-shhk!*

Blood-soaked robes fluttered in the wind.

They plunged straight into the heart of the enemy lines as if they didn’t care whether they lived or died. Their movements were as elusive as the wind, and the sword light that surged along the blade of the old man at their head was cruelly dazzling.

*Boom!*

A thunderous blast shook the earth.

Chunks of flesh, no longer recognizable as such, and blood flew in every direction.

Where the Force had passed, nothing remained.

Nothing but blood and death.

And the tremendous roar of the allied forces as they crashed into the enemies’ broken formation and crushed it completely.

“Waaah!”

“Charge! Keep charging!”

“Don’t leave a single one alive!”

In that moment, the allied forces were one wave, though each part had a different color.

The Embroidered Uniform Guard charged in ranks, keeping their composure amid the chaos.

The soldiers and martial artists of Gansu followed behind them, squeezing out their last strength.

Then there were the Zhongnan Sect Disciples, whose numbers had dwindled drastically since the start—and even the mysterious mounted fighters who had suddenly appeared and joined the allied forces.

*Thud-thud-thud-thud!*

The ground trembled as if an earthquake had struck.

Their deafening shouts echoed without end. The forest of steel packed across the land engulfed the invaders, blooming with countless flowers and branches.

Red flowers made of blood and bone, white branches made of bone.

That was the end of the long, brutal battle.

Another half day passed. Of the fully thirty thousand Dark Heaven cultists, not one still stood on the battlefield of his own will.

Not one.



* * *



In modern military terminology, annihilation means the loss of combat effectiveness.

Troops, equipment, supplies, morale, and so on.

Generally, when at least thirty percent of a fighting force has been killed or wounded and the surviving troops’ will falters, they’re judged incapable of continuing to fight—and are considered annihilated.

But here in the Murim, what lay before Jin Taekyung at this very moment was different.

*Annihilation.*

The word meant exactly what it said.

No, perhaps those two characters still couldn’t express the whole thing.

Killing. Massacre.

Or…

*…Slaughter.*

The word I couldn’t bring myself to say lingered on the tip of my tongue. I looked around, my gaze heavy.

Red. Everything in sight was stained red.

The once-white snowfield. The faces of the corpses submerged in pools of blood, eyes wide open.

And the bloodshot eyes searching for enemies who might have survived, probing through rivers of blood and mountains of corpses.

*Shhk!*

The sword that came down hard pierced the chest of an enemy writhing among the countless corpses.

A miracle wouldn’t happen twice. If you survived once, it was practically a misfortune.

Had his life ended sooner, he could have met a much quicker, more peaceful death.

*Craack.*

The blade buried deep inside him slowly twisted.

At the dreadful sound of bone and flesh being crushed—and the killing intent, even more vivid than the sound—the faces of the Fire Dragon Pavilion members beside me stiffened.

“Captain.”

“Even so, this is…”

I raised a hand to stop them before they could finish.

I knew what they wanted to say.

This wasn’t murder. It was slaughter, like butchering livestock.

At the same time, Taekyung understood the feelings of those giving such a cruel end to enemies who no longer had the strength to resist.

“Wait here.”

I tossed the words to the Fire Dragon Pavilion members and slowly started walking.

One step. Then another. With each step, unbearable fatigue washed over me. But someone’s hand reached out from somewhere and steadied my swaying body.

“I believe I told you to wait.”

At my mutter, which came out almost as if I were talking to myself, Sama Pyo shrugged.

“Did you? I don’t remember hearing that.”

“You’ve heard it now. Step back.”

“I can’t do that.”

“That’s an order.”

“An order? So that’s how you’re going to play it?”

“Yeah.”

My voice was firmer than ever. Sama Pyo’s reply, which rang out a moment later, was just as firm.

“Fine. Then as of this moment, I’m leaving the Fire Dragon Pavilion.”

“……!”

I stared at him, eyes widening. Sama Pyo gave me a faint smile.

“What? Didn’t see that coming?”

“You…”

“I’ve enjoyed our time together, Pavilion Master. But this is where we part ways.”

He met my gaze calmly and added, “I can’t keep dragging you or anyone else into this. Whatever comes, I have to face it alone.”

He knew.

He knew why I was still clinging to consciousness when I’d been on the verge of collapse for a long time.

And he knew how great the danger waiting at the end of the road he now had to walk alone might be.

Even so, he could remain so calm because he had already made up his mind.

“Whatever happens, don’t get involved. And if something should happen to me…”

His voice trailed off as his gaze shifted to Taishan.

Taekyung, who had been watching him, cut in.

“Nope.”

“What?”

“I said no, asshole. Look after your own man. Don’t dump him on someone who’s already got enough on his plate.”

Sama Pyo fell silent for a moment. Then he understood what Taekyung meant and gave a short laugh.

“You’re right. I have to look after him to the very end. No matter what.”

*If I can. If I can survive, like you said.*

Swallowing the words he could not bring himself to say, Sama Pyo set off alone.

Taekyung watched him go, then suddenly spoke.

“Something just occurred to me… Do you remember the day we left the Jin Family of Taiyuan?”

Of course he did.

It had been recent—not years or months ago, but barely more than a month.

And he could guess well enough why I’d brought it up.

“Of course. Right before we left for the west, Elder Namho and Taishan came looking for me themselves.”

That night, Sama Pyo had been reading a secret letter from Gansu.

He had already read it, then read it again—over and over.

Even as the two men’s footsteps approached his door.

“You’re usually punctual to the second, but that day you dragged your feet. Like someone waiting for a visitor.”

At my mutter, Sama Pyo abruptly stopped walking.

“I had a lot on my mind that day.”

“Elder Namho’s old, but he’s a fine agent. His nose is pretty sharp for his age, too.”

“True. Though his hearing’s bad, so he talks loudly.”

A giant nearly nine feet tall who made the ground shake just by walking, and an old man who talked a lot and had a booming voice.

They stood out wherever they went, and you couldn’t help hearing them.

That had been true for Sama Pyo, too, alone in his quarters that night, reading the secret letter.

“You planned it, didn’t you? From the start.”

“No. Not at all.”

A blatant lie.

Sama Pyo had been waiting there.

Waiting for the oldest friend who would come looking for him before anyone else.

No—or for the old Hidden Shadow Pavilion agent who was always stuck to Taishan’s side.

And, deep down, he had hoped Namho would figure out at least a little of the secret he couldn’t bring himself to say aloud.

He had hoped Namho would be on his guard because of it.

“Why? Why go that far?”

At my quiet question from behind him, Sama Pyo resumed his halted steps.

“Even so… he’s my father.”

He’d wanted to believe in him until the very end, no matter what.

But when that trust was betrayed, he didn’t want the people beside him put in danger.

So he had deliberately left a clue as a warning, so they would naturally grow suspicious before Sama Pyo himself could report his father’s suspicious actions.

Even if that meant they might suspect him, too, he didn’t care, as long as everyone else would be safe.

He was used to being suspected and hated.

That was what it meant to live as the blood relative of Sima Gong, the Black Night King, and the Young Sect Leader of the Black Dragon Demon Gate.

And yet it was strange.

Even after Namho’s gaze toward him had grown sharper and more searching, I hadn’t said a word.

Not once.

Not even now.

“Then why didn’t you ask me anything? Not once, all this time?”

The moment he voiced the question that had been circling in his mind, a short answer came from behind him without a hint of hesitation.

“Even so, we’re friends.”

“……!”

“Shit, I don’t know. You look dark and gloomy on the outside, but… I kept wanting to trust you. Even as everything kept turning into a shitshow, I still wanted to.”

Sama Pyo couldn’t say anything.

He just clenched his teeth to hold back the heat in his eyes, then continued forward with unsteady steps.

Somewhere behind him, my voice had already grown faint with distance.

“Don’t die. That’s an order.”

At my gentler-than-ever command, Sama Pyo didn’t answer.

He kept walking, through the ruined battlefield where the band of fighters were still hunting down and slaughtering the surviving enemies.

Or, to be exact, toward the old man standing at their center.

*Splash.*

He came to a stop at last. A pool of blood rippled beneath his feet.

Sama Pyo took a deep breath. The stench and reek of blood were foul enough to make him gag, but his heart was strangely calm and still.

His heart was as calm and still as the expression of the old man before him, who gazed at his enemy’s son with eyes too deep to read.

“Your junior, Sama Pyo, pays his respects to the Sect Leader of the great Kongtong Sect.”

At that moment—

*Shwaaah.*

Killing intent, so immense it was terrifying, surged up all around him and pressed down on Sama Pyo’s entire body.
## Chapter artifact 1058

# Chapter 1058

It happened in an instant.

The Blood-Clad Men, drenched head to toe in blood as they slaughtered their enemies, surrounded Sama Pyo and unleashed a terrifying wave of killing intent.

*Shhhhhh.*

There were about a hundred of them.

Their qi was so fierce that the lingering heat of the battlefield froze in a flash. The flow of the air changed all at once, and I could feel it clearly.

Even from some thirty-odd yards away, where I’d stopped to watch.

And even farther off, where the Fire Dragon Pavilion members stood waiting as ordered, with no idea what was happening.

“My Lord! It’s dangerous!”

The killing intent was so dense it seemed to erase the distance between them.

Taishan instinctively sensed Sama Pyo was in danger. With an urgent shout, he launched himself forward—only to be stopped immediately.

By no one other than me.

“What do you think you’re doing, Pavilion Master!”

He roared the words, his fighting spirit pouring out fiercely.

I’d never seen him like this before.

But I couldn’t back down either.

This wasn’t some damn fate or bad luck. This was Sama Pyo’s own choice.

“Don’t go. Not yet.”

“Taishan will not obey such an unreasonable order!”

“I’m not ordering you. I’m asking. Just like Sama Pyo asked me not to interfere.”

“……!”

Taishan’s enormous eyes wavered.

The Fire Dragon Pavilion members caught up, but before any of them could say a word, Namho suddenly spoke in an unusually subdued voice.

Though riding on someone’s shoulders didn’t exactly make him look authoritative.

“I understand how you feel right now, but this isn’t the right time.”

“Namho, but—”

“Honestly, look at this angry bull of a man!”

*Smack!*

Namho struck Taishan’s forehead with a sharp, emphatic slap, then rebuked him sternly.

“You weren’t satisfied with letting sentiment cloud your eyes, so now you’ve gone deaf too? You didn’t even hear what the Pavilion Master just said?”

He was right.

As Namho said, I’d told Taishan clearly.

*Not yet… Don’t go yet.*

*That’s right. Not yet.*

I murmured to myself, then patted Taishan on the shoulder as he lowered his two-section staff, his strength seeming to leave him after his inner struggle.

At the same time, I turned to look toward the hundred figures radiating such vivid killing intent.

The Blood-Clad Men—or rather, the Kongtong Sect Disciples.

And at their center, an old man stared at Sama Pyo with deeply sunken eyes.

*Perfected Being Hyeoncheon.*

That was who he was.

The Sect Leader of the Kongtong Sect, one of the Nine Sects and One Gang, and the greatest martial artist in Gansu.

And…

Another avenger, betrayed by those he had trusted as allies and forced to lose countless Disciples.

*Whoooosh.*

His sleeves swelled with the force of his formidable internal energy.

At that moment, the emotionless, ink-black eyes—so deep their depths were impossible to discern—didn’t reflect Sama Pyo.

They reflected the bloodline of his enemy: a man Hyeoncheon would gladly tear to pieces.

* * *

*Rumble.*

The air trembled within a radius of several yards. It was hard to breathe.

In the moment the overwhelming qi began slowly tightening around him from every direction, like the hand of an invisible giant, Sama Pyo froze. Then Perfected Being Hyeoncheon suddenly spoke.

“Lately, I keep remembering when I first met your esteemed father, my friend, in the middle of the Great Faction War.”

From infancy to old age, the elderly Daoist had devoted his entire life to the Dao. His character was gentle, and he had earned the respect of many.

Though he had never joined the ranks of the Ten Kings, he had always been humble, even as Sect Leader of the great Kongtong Sect.

But even the largest vessel has its limits.

“At the same time, I regretted it. I wondered if I should have killed him then and there.”

Sama Pyo said nothing in response to the deep sigh in Hyeoncheon’s voice.

No—he couldn’t answer.

The old Daoist before him had already glimpsed part of the truth, even though Sama Pyo hadn’t told him yet.

And the first time Hyeoncheon learned anything of the sort had been through a woman.

“At first, I didn’t want to believe it. I tried to convince myself it was a ploy to stir up internal strife among the survivors from Dunhuang—that we were being used as stepping-stones for an even greater scheme.”

Hyeoncheon had tried to shake the information he’d heard while holding his breath in the undergrowth from his mind. But with every passing day, his suspicions had deepened.

His distrust of one man: Sima Gong, the Black Night King.

Everything—including the ominous signs he had sensed before setting out for Dunhuang—had fitted together like the precise teeth of a single gear.

“The more I thought about it, the stranger it seemed. Every scrap of information we received from the Black Dragon Demon Gate was wrong, and we were the only ones who bled.”

Kongtong Mountain, the Kongtong Sect’s home since ancient times, stood at the southeastern edge of Gansu. The Black Dragon Demon Gate’s territory, by contrast, covered the Dunhuang region in the northwest.

So the Kongtong Sect and the many sects that followed it had acted on information provided by the Black Dragon Demon Gate—and suffered a crushing defeat.

“Thousands died. In that single day.”

At the slight tremor in Hyeoncheon’s voice, the hundred Disciples surrounding them clenched their teeth.

How could they forget that horrific battle, which had begun like a bolt of lightning?

No—it had been a one-sided slaughter.

“Defending the city meant nothing. When that enormous army appeared out of nowhere, we couldn’t do a thing.”

The Three Elders of Tianshan.

The three old fiends from Tianshan, returned after decades away, had led the charge. Behind them came tens of thousands of cultists who knew no fear.

Neither the arrows they fired without pause nor the city walls—built of sturdy stone coated in yellow earth—could stop them.

That immense human tide, black as night, had brought down the high walls in an instant and swept away everything in its path.

The lives of brothers, friends, and family members who had stood by them through so many years.

“I would rather have fought there with them and died. Heroically, with my last breath.”

Hyeoncheon wasn’t the only one who felt that way. A hundred pairs of eyes, reddened and now glistening with tears, bore witness to it.

But they had survived in the end.

They had to survive.

If only to avenge those who had died screaming.

“So we ran away like cowards. We received unexpected help on the way and easily shook off their pursuit, but the others weren’t so lucky.”

Luck didn’t come equally to everyone.

Thousands had died in Dunhuang alone, and even those who had fled in tears had remained prey.

They scattered to survive, and thousands more were killed or wounded as they were hunted down one by one.

But even after escaping Dark Heaven’s encirclement, Hyeoncheon and the Kongtong Sect Disciples hadn’t returned to the rear.

More precisely, they couldn’t return yet. Every one of them had suffered some injury, large or small.

But the suspicion the Grand Mage had planted deep in their hearts had already taken root. And while Hyeoncheon was groaning in pain from the severe injuries he’d sustained in the battle against Dark Heaven, he suddenly realized whose familiar faces had flashed through his memories.

Back then, as he hovered between life and death and swore revenge.

They weren’t the mysterious woman whose face had been hidden behind a silver-white veil. They weren’t the Three Elders of Tianshan or the Blood-Sword Demon Lord, who had captured and killed two Elders and hundreds of Disciples.

They were the allies he had believed would protect their rear.

“It’s strange, isn’t it, my friend?”

His voice was low.

After three days at death’s door, Hyeoncheon had barely recovered from his injuries. He’d thought then:

*Why?*

Why had their faces come to mind as he vowed revenge, as if chewing bear gall?

The Black Night King, Sima Gong. The Roaring Fury Swordsman, Song Il. The Taeeul Merciless Sword, Hwangbo Eom.

And the many leaders of Gansu, no different from the Black Dragon Demon Gate’s servants.

Why did fire surge from deep in his chest whenever he recalled each face and name the woman had spoken of from behind her silver-white veil?

In the end, Hyeoncheon had found the answer.

To see it with his own eyes, he had come here with the Disciples who had survived.

And at this very moment, before beginning his revenge, he faced a young man who had come to him of his own accord.

“Boy of the Sama family.”

His way of speaking had changed.

His voice was steady, edged with iron, but cold flames burned in the old Daoist’s eyes.

“Bring me your father. There’s something I must confirm before I draw my sword.”

*Rumble.*

The ground trembled faintly.

Sama Pyo silently watched the ripples spreading across the pools of blood. Then, at last, he raised his head, which had been bowed all this time, and spoke.

“He’s already gone. To a distant place from which he can never return.”

“……!”

Perfected Being Hyeoncheon’s eyes flew open.

So did those of every Kongtong Sect Disciple around Sama Pyo, still radiating suffocating killing intent.

By instinct, they understood what his words meant.

*He was dead.*

*The Black Night King, Sima Gong.*

The enemy they ought to have put to death with their own hands—the heinous traitor who deserved no less.

And Sima Gong wasn’t the only traitor who had met this fate.

“Sect Leader!”

A heartrending cry came from somewhere.

A Kongtong Sect Disciple closed a distance of well over a hundred yards in an instant, moving like an arrow. His face was streaked with grief and fury as he threw himself down before Hyeoncheon.

“They—they…!”

Before his sobbing shout could even end, Hyeoncheon suddenly turned his head.

He saw it clearly in the distance: the flag of the Zhongnan Sect, rising at an angle.

Or rather, he saw the two white cloths tied to its pole, fluttering weakly.

“A mourning flag…!”

At the anguished whisper that slipped through someone’s clenched teeth, the qi surrounding them surged violently.

The white cloth signaled someone’s death. Then there was the reaction of the Disciple who had just returned.

The meaning was clear.

The Roaring Fury Swordsman, Song Il, and the Taeeul Merciless Sword, Hwangbo Eom.

The two Zhongnan Sect traitors, whom they’d meant to punish after Sima Gong, were gone too.

To the far-off place no movement technique could reach: the afterlife.

“Dead? You mean they’re dead? Just like that? Is that all they get?”

*Grrk.*

Hyeoncheon bit his lip.

The flesh split and blood flew, but that pain was nothing beside the agony in his chest, which felt ready to burst.

“How—how dare they…!”

Hyeoncheon was enraged.

Despite his still-healing body, his immense qi pressed down all around him. Even the Kongtong Sect Disciples nearby had to hold their breath.

Only one person was an exception: Sama Pyo.

“I’ll take his place.”

His voice was barely squeezed out as he endured the Supreme Peak master’s qi with his whole body. Hyeoncheon’s eyes sank deeply.

“What did you just say?”

“I said I’ll take his place. I’ll accept the just punishment for my sinful father’s wrongs.”

In the silence that fell, Sama Pyo bowed his head to everyone, Hyeoncheon included, and continued.

“I know how presumptuous that sounds. I know my insignificant life can’t make up for the grudge of those who are gone.”

He was right.

A person’s heart wasn’t something that could simply be filled again whenever it was empty.

Nothing could fill a hole once it had been torn open.

All you could do was keep filling it with things in an attempt to forget, or remember as you stared at the hole that remained no matter how much you put inside.

Remember the things lost in a single moment of carelessness. Regret what you’d lost.

That was why Sama Pyo was here now.

Why he wanted to take a different path from his father.

“An eye for an eye. A tooth for a tooth. Death for death.”

In the Murim, a blood debt between martial artists could only be repaid with blood.

“Strike me down. I won’t hold it against you.”

And at that moment—

*Shing.*

A dazzling flash burst from the sword at Perfected Being Hyeoncheon’s waist.
## Chapter artifact 1059

# Chapter 1059

For me and everyone else, it was only the briefest instant.

Though for someone, it might have felt unbearably slow and suffocating—a moment from a life flashing before their eyes.

*Shing.*

The sound of sharp steel slipping from the scabbard that held it was so faint it raised goose bumps. It meant the sword had been drawn almost perfectly.

Not a hair’s breadth off. The right amount of force, at the right speed.

And…

A clear trajectory, following its master’s will as it cut diagonally across its target.

*Shhk!*

The distance was too short to dodge. The gap in their martial prowess was too great.

And Sama Pyo had quietly closed his eyes without even trying to evade, as if accepting his fate.

Of course, nothing out of the ordinary happened. The sword light that flashed in a split second scattered red flowers through the air.

*Shwaaa!*

Time started moving again.

Beyond Sama Pyo’s staggering back, a fountain of blood shot high into the air, staining everyone’s vision.

The Kongtong Disciples nearby. The Fire Dragon Pavilion members and me.

And someone else, too, who had been doing everything in their power to hold back the urge to rush over.

“No!”

Taishan’s patience, stretched taut as he anxiously watched everything unfolding around Sama Pyo, had finally snapped.

With a thunderous shout that rang in every direction, the giant—over nine feet tall—set down the poor old man riding on his shoulders as if he were tossing him aside and shot forward at a speed I’d never seen from him before.

*Whoosh!*

The wind roared around him, but his path was as straight as could be.

Before anyone had a chance to stop him, Taishan shot forward like a cannonball, heading straight for Sama Pyo as he staggered backward.

He didn’t seem to care one bit about the Kongtong Disciples who had surrounded Sama Pyo, as if to box him in.

“You bastard!”

“Stop right there!”

*Papat!*

Shouts erupted all around them, and blurry figures appeared in every direction.

Dozens of Kongtong Disciples moved with elusive speed to block Taishan’s path. Each raised their weapon and aimed it at him.

Their blades were slick with blood. And, as if to prove how they had survived the brutal, desperate battle at Dunhuang, every one of them bore the gleam of Sword Energy—the level at which it could injure others.

But Taishan’s two-section staff, clutched in his hands as he shot forward even faster despite dozens of Peak masters blocking his way, shone with the same light.

“Raaaargh!”

Tiger Giant Child.

True to the meaning of his epithet, Taishan was usually as innocent as a child, but his inborn strength and martial prowess were those of a beast.

Roaring like a furious tiger, Taishan swung his two-section staff with all his might. A tremendous gale swept along with it.

*Whoooosh!*

Even a hardened veteran of the Murim would have felt a chill run down their spine at that terrifying whistle through the air.

But the Kongtong Disciples didn’t take a single step back.

No—they unleashed dazzling sword light at Taishan as he charged them with a menacing look.

*Shwiiing!*

In an instant, the space was filled with murderous intent.

The two-section staff barreling through the wind, and blades shooting through the air.

And, slipping into that life-or-death moment, I took a forceful step forward.

*Shhk.*

One step.

Just one was enough.

Several yards of space vanished in an instant, and the scene around me changed.

I had already slipped between Taishan and the Kongtong Disciples. Without hesitation, I thrust out both palms.

*Bang!*

Compressed air exploded. The heat of the Flame Divine Palm, held back as much as I could, burst from my palms and shoved everything away.

Not only the weapons being swung fiercely at one another, but the bodies of the people holding them, too.

*Clatter!*

Weapons shot up into the air without reaching their targets. The figures that wielded them stumbled backward, swaying like reeds in the wind.

“……!”

“……!”

Through the dust that rose hazily from the ground amid all the blood, I looked at their bewildered faces as they were forced back. My voice came out tired and flat.

“Do you all have energy to burn? Take it down a notch.”

Before anyone could answer, I spoke again, this time to Perfected Being Hyeoncheon, who had silently watched the sudden scene unfold before him.

“Apologies for the late greeting. We met once before in Henan.”

Perfected Being Hyeoncheon had briefly met me at the Mount Song Resolution, where the new Murim Alliance was first formed. He gave a slight nod.

“It’s been a while, my friend Jin.”

A corner of my heart ached.

Even though our connection had lasted no more than fifteen minutes, it still did.

The old Daoist who had once praised my martial arts with a kind voice and laugh, like my own grandfather, was nowhere to be found now.

Perfected Being Hyeoncheon’s voice, reaching my ears, was as dry and brittle as grains of desert sand. The traces of grief and anger remained at the corners of his mouth.

Just like the sword trembling in his wrinkled hand.

The blood slowly dripping from the tip of the treasured sword he had likely carried with him his entire life must have come from the emotions he still hadn’t managed to shake off.

“Pavilion Master! What are you doing? Move aside, now!”

Right. That guy was here, too.

Taishan’s shout brought me back to my senses. I pulled myself out of the emotional swamp I’d been sinking into.

At the same time, I called out to the guy as he adjusted his grip on the two-section staff and stepped forward.

In my own rough way.

*Thump!*

My fist drove straight into his abdomen. The giant, nearly nine feet tall, bent over like a shrimp and went rigid.

Taishan drew in a startled breath. He stared at me wide-eyed, then squeezed out a few words.

“P-Pavilion Master…”

“Cool your head.”

With that quiet word, I brought the edge of my hand down on the back of his neck without hesitation.

*Thud.*

Even a tough guy with skin and bones so thick that a Pressure-Point Strike probably wouldn’t work was no match for overwhelming strength.

The sound of him falling was like a bear hitting the ground. Silence followed.

The Fire Dragon Pavilion members, who arrived a moment later, and the Kongtong Disciples, who had been about to charge at Taishan again, stared at me in bewilderment.

Everyone except Perfected Being Hyeoncheon, who watched in silence with a sunken gaze.

“I heard there was a giant tiger beside the young Black Dragon… You’re every bit as strong as they say. And fiercely loyal, too.”

Perfected Being Hyeoncheon muttered as he looked at Sama Pyo, still lying motionless.

“He’s a better subordinate than he looks. Don’t you think?”

“He’s as dumb as he is big, but he’s a good guy. And…”

I added with a bitter expression, “That friend you showed mercy to is a much better person than you think, Sect Leader.”

“……!”

“……!”

The air around us gave a sharp, electric shiver.

Those who understood what I meant opened their eyes wide at the same time, as if on cue. Perfected Being Hyeoncheon closed his eyes without a word.

As if trying to wipe away the killing intent still lingering in his heart.

“Do you… regret it?”

I broke the silence and looked at Perfected Being Hyeoncheon.

From the moment he had drawn his sword at his waist and swung it, I’d known instinctively.

That perfect draw held conflict, but not the slightest trace of killing intent.

That the old Daoist’s sword would never take someone’s life.

That was why I hadn’t stepped in.

I could feel that though his unsteady sword tip had cut shallowly into Sama Pyo’s skin, it was because of the last bit of conflict he had left.

“Regret it? Of course I do.”

“Then why?”

“His eyes. I saw those eyes.”

Perfected Being Hyeoncheon suddenly opened his eyes. He looked up at the Kongtong Sect flag fluttering above his head and continued.

“They were like the eyes of my Disciples, the last time I saw them in Dunhuang. Deep, upright, and unbowed even in the face of death. Those were their eyes.”

Some say a person’s eyes are the windows and mirrors of the heart.

Perhaps that was why the old Daoist, who had come here carrying his desire for revenge, couldn’t bring himself to kill the son of his enemy—the man who had come here seeking death himself.

“I’m just a wretched old Daoist. I devoted my life to the sword instead of the Daoist scriptures, and I couldn’t save my Disciples as they bled and died. But…”

A hot breath slipped between his trembling lips.

“Someone I met recently said this to me. If you take someone’s life simply because they share the blood of your enemy, what else could that be but the Demonic Path?”

I understood.

Even though Perfected Being Hyeoncheon’s voice was directed at me, what he meant to say was for every Kongtong Disciple to hear.

*Splat.*

A sword slipped from someone’s grasp and plunged into a pool of blood.

Only moments earlier, they had been giving off suffocating killing intent. Now, they stared at one another with vacant eyes.

As if they were remembering themselves through the sight of their fellow Disciples, drenched in blood from head to toe—remembering how they had searched for their surviving enemies and slaughtered them like livestock.

And they swallowed their tears.

In silence. Struggling to hold back the emotions and beloved faces that passed before their eyes.

“Revenge will be carried out, but it will not extend to the relatives of the guilty. The Kongtong Sect we build anew from this day forward must be that way.”

Perfected Being Hyeoncheon declared this to all his surviving Disciples.

Though the tower they had painstakingly built had fallen, he would build it again upon bedrock.

And no innocent blood would stain the bedrock on which they built an even stronger tower.

Then, looking at his Disciples with tear-filled eyes, he said, “Cry to your hearts’ content. These tears may be your last today.”

The next moment, I quietly closed my eyes and shut out the sound.

So did every member of the Fire Dragon Pavilion. So did the others who had come over after belatedly realizing what was happening.

The desperate, sorrowful wails and sobs filled the air. They couldn’t help hearing them, even if they didn’t want to.

But it didn’t matter.

No one on this battlefield, covered in countless corpses and pools of blood, would hear or remember their crying.

Or…

Maybe everyone was already crying together.

*Tap.*

At the familiar touch of someone patting my shoulder, I wiped the hazy moisture from my eyes with my sleeve.

“Old Master.”

“I was worried I might be late, but it seems that worry was misplaced.”

I turned around. Jeok Cheongang and the Bow Saint were there. They had disappeared somewhere around the time the shouts of victory began to ring out.

No—strictly speaking, they weren’t the only ones there.

“Ugh, sob… sob!”

A man wept openly as if his heart were breaking.

Even after spending years being worked like a dog in Gates so disgusting that just standing in one made me gag, I’d never smelled anything like this. A certain foul-smelling oddball thrust his hand toward me.

*What the hell is this?*

I blinked, my tears already gone, when the oddball grabbed my hand, yanked me close, and wrapped me in a tight embrace. Then he began to sob miserably.

“Waaah! Uuughhh!”

No, seriously, what was going on?

After my brain stalled for a moment, and whatever tears had been about to come out disappeared completely, I asked, “……Um, who exactly are you?”

Jeok Cheongang answered without hesitation.

“A madman.”

“What?”

“Some vicious-looking mounted bandits call him ‘Great Sir,’ too.”

“……!”

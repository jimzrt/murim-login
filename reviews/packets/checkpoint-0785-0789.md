# Checkpoint Review — 785–789

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

# Chapters 785–789

## Plot

Magic Johnson’s Absolute Shield protects the National Assembly and nearby city from the final clash between Jin Taekyung and Michael Silbert. Michael loses his transformation, magical power, and regeneration; Jin defeats and executes him after the assembled Hunters approve the World Hunter Federation’s first resolution. The Skeleton King reconciles with Jin, accepts Stone King as another name for himself, and shares his private first name only with Jin.

Exhausted, Jin collapses after the battle. The Hunters honor him and acclaim him as the Federation’s Alliance Leader. Meanwhile, the Federation dismantles Michael’s network: Chuck Hagel captures President Emmanuel, and major political and business figures are arrested. When Jin wakes beside Hayeon and his mother, he accepts his appointment and asks Team Leader Choi where The Prophet is.

## Continuity

- Michael Silbert is dead. His forces were killed or captured; Huginn survived and was captured.
- Jin has awakened and accepted his appointment as the World Hunter Federation’s Alliance Leader.
- President Emmanuel was taken alive by Chuck Hagel; Ares Guild members are keeping him alive. The Federation’s operation against Michael’s associates has led to further arrests.
- The Skeleton King accepts both Skeleton King and Stone King as names. His first name in this world remains private, shared only with Jin.
- Jin’s nightmare showed the world consumed by fire and a rift splitting the sky and space. Whether it foretells a real catastrophe is unknown.
- The Prophet’s whereabouts remain unknown; Jin has asked Team Leader Choi about them.

## Translation Decisions

- Keep **magical power** distinct from **mana**.
- Render **맹주** as **Alliance Leader**.
- Render **균열** as **Rift**; treat Jin’s vision as ominous imagery, not a confirmed future event.

## Durable state

{
  "active_continuity": [
    "Michael Silbert is dead; Huginn was captured alive, and Michael’s forces were killed or captured.",
    "Jin Taekyung has awakened and accepted the World Hunter Federation’s appointment as Alliance Leader.",
    "The Federation’s operation against Michael Silbert’s associates has led to arrests of major political and business figures.",
    "Jin’s nightmare showed a world-ending fire and a rift in the sky and space; their significance is unresolved.",
    "Jin’s sister Hayeon and mother were with him when he woke.",
    "The Prophet’s whereabouts are unknown; Jin has asked Team Leader Choi about them."
  ],
  "continuity_sources": [
    788,
    789
  ],
  "open_questions": [
    "Where is The Prophet?",
    "Was Jin’s nightmare of fire and a rift a warning of an actual catastrophe?"
  ],
  "safe_through": 789,
  "temporary_decisions": [
    "Keep magical power distinct from mana.",
    "Treat the fire and rift in Jin’s nightmare as ominous imagery, not established future events."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 785

# Chapter 785

It was a resonance.

More than a simple roar—a resonance that made their ears ring.

*Gooooong.*

Darkness and flames collided. At the same time, they swirled together.

As everyone watched the two incomparably powerful forces suck in wind, air, and debris, slowly swelling, a single word flashed through their minds beneath a red warning light.

Annihilation.

In the face of that immense power, unlike anything they had ever felt, everything seemed meaningless.

If it burst as it was, everything within a few hundred meters would be reduced to ash.

No—not just the National Assembly. The fallout might reach the entire city.

*At this rate…… even the civilians will get hurt.*

But not everyone thought that way.

Even if they all felt the same crisis, their circumstances were different.

Some here were fighting to protect the world where everyone outside lived. Others had turned their weapons against them for the sole purpose of protecting their own world.

And that one fundamental difference soon showed itself in the actions each side took.

“Get them!”

*Shhk-shhk-shhk!*

With their backs against the cliff, there was nowhere left to retreat.

The traitors who had chosen Michael Silbert seized the chance presented by this sudden turn of events, even as they were already outnumbered, and made one last desperate stand.

Their numbers had already been cut in half, but the malice in their auras gleamed more viciously than ever.

*Krrrraack!*

A massive tower shield split apart, and the ground cracked like a block of tofu.

Strikes came rushing in from every direction, each one lethal if they let their guard down for even a moment. Yet no one stepped back.

Because they were Hunters.

Even if the word meant nothing more to those traitors than a faded slogan, they had upheld what it meant to be a Hunter—and they would continue to do so.

It was their duty. The responsibility that came with their strength.

“Mr. Johnson!”

Choi Minwoo shouted like a battle cry and swung his sword with all his might.

Unlike its owner, who was now little more than a man drenched in blood, the dazzling crescent of aura shot across the air, passing close to the towering Black man standing there and cleaving through the dozens of arrows flying toward him.

*Shhk!*

The arrows fell apart in an instant, their severed remains scattering before him.

But even amid the urgent crisis unfolding all around him, Magic Johnson drew a deep breath and gathered his mana, muttering to himself.

*Just call me Johnson, already.*

When this battle was over, when the endless flow of blood had finally stopped, he would tell Choi Minwoo again.

He really could speak casually with him now.

He wanted to clap Pai Chen on the shoulder, still drawing his bowstring until his fingers were raw with blood; Prince Felix, fighting drenched in blood despite his noble status; and Chuck Hagel, who had just brutally ripped off the Kronos Guild Master’s arm.

No—he wanted to drink and laugh and talk with every Hunter who survived.

And there was no doubt that…….

*Yeah, Jin. You’ll be there.*

His voice, unable to reach anyone, was swallowed by the resonance and faded away.

Beyond the dazzling light that now filled the National Assembly, a young man’s figure flickered faintly across Magic Johnson’s vision.

And there was someone else running without hesitation toward him, toward the heart of the disaster.

*Chrrrrrrk!*

Something white as snow swept in like a wave.

The moment it finished forming, sealing off every gap around the two beings standing at an impassable crossroads—Jin Taekyung and Michael Silbert—Magic Johnson gave a faint smile and awakened the mana throughout his body.

Then he spread it across the entire National Assembly, as if to envelop the whole world, and spoke.

“Absolute Shield.”

The spell, completed by devouring the Grand Mage’s vast reserves of mana, covered a radius of several hundred meters.

*Whooosh.*

At last, a blinding flash burst forth, filling everyone’s vision.


* * *


In the sliver of time between moments, split thinner and thinner—

*Bam! Rumble-rumble-rumble!*

The world shook with a roar so immense it hurt. Pitch-black darkness and flashes of light flickered before my eyes over and over, while countless sensations coursed through my body.

It hurt. It was hot. It was cold. It was wet.

And…… it was heavy.

So heavy that I could barely bear the weight crushing down on me even now.

*Huff. Huff.*

My breathing was ragged. I struggled to clear my blurred vision, then drove the shaft of my spear into the ground to support myself.

*Thump.*

In moments like this, I was glad I’d chosen a spear as my weapon.

It reminded me of what the Instructor in the red cap had said when I first entered the Hunter Training Center, handing out weapons from the armory.

*“Just use a spear. Spears are the best.”*

*“Yes. Sorry, but may I ask why?”*

*“What’s your Awakening Grade?”*

*“F-rank.”*

*“Right. There’s your answer. In a fight between weaklings like you, reach is everything. I know because I’ve used one myself. Another important thing is……”*

*“What’s important?”*

*“It looks cool.”*

*“Sorry, I didn’t quite catch that……?”*

*“I said it looks cool. Now, listen. Say you run into an enemy. You fight like hell, one-on-one. You both pour out all your strength until you can’t even move a finger. In that situation, who’s going to fall over—the guy with the sword or the guy with the spear?”*

*“I’d guess the one with weak legs.”*

*“Wrong. The guy with the sword falls over first. Guaranteed.”*

*“Could you perhaps explain why……?”*


I still couldn’t forget what the Instructor had said then, with a solemn expression.

*“The guy with the spear can use it as a cane.”*

*“Excuse me?”*

*“You jam it into the ground or a wall, and it’ll hold you up. But the guy with the sword is bound to fall over. Why? It’s short. That’s where the fight’s decided. One guy’s down, the other’s still standing. What do you think? Sounds like a scene from a movie, doesn’t it?”*

*“Oh.”*

*“Good. So, have you decided what weapon you’re going to use?”*

*“Yes, I have.”*

*“What is it?”*

*“A bow.”*

*“Get down.”*


It was a stupid, dusty old memory.

I’d gotten about twenty whacks on the ass with a spear shaft from the armory, then been practically forced to accept that spear as my first weapon.

And when I saw that Instructor show up to our first training session the next day with a sword at his side, I learned one of the truths of the world.

This line of work was crawling with some truly incredible assholes.

But even that Instructor, who must’ve stuck around the training center for the fun of messing with recruits like me, couldn’t have guessed back then.

That because of his stupid little joke, I’d be standing here now.

That the F-rank Hunter he’d seen back then would make Michael Silbert kneel just a little over ten years later.

*Thump.*

I raised my head at the heavy sound that pierced my ears.

Through my blurry vision, I saw a man trembling on one knee.

Michael Silbert, whose magical-power wings and gleaming black scales had both disappeared, stared at me, panting.

“Y-you bastard…….”

*Cough.*

With a cough, a torrent of bloody fluid mixed with bits of his organs poured out.

His body had spent all its magical power, and, despite his hopes, it showed none of the miraculous recovery it had displayed before.

No. It would never do that again.

He—Michael Silbert—was going to……

*Die today. By my hand.*

I didn’t have the strength to say it out loud. I muttered the words where no one could hear them, gritted my teeth, and used White Flame to straighten up.

Then I walked toward him.

*Thud.*

Every step sent pain crashing through my body, as if I were about to break apart.

Or perhaps I already had.

*Beep. Beep. Beep-beep!*

It was strange.

My eardrums had burst, and my ears had been ringing for a while, but the System’s warning beeps were still loud and annoying.

*Looks like my body’s pretty thoroughly wrecked.*

I let out a hollow laugh, but it didn’t matter.

Since when had I worried about my condition before a fight?

I was happier that I’d finally brought Michael Silbert down—and that, despite the immense aftermath, all those familiar faces had made it through alive.

Of course, not everyone felt the same joy I did.

“Jin Taekyung!”

That middle-aged giant charging at me now, the Kronos Guild Master, was one of them.

As proof of how fierce the fighting had been, he’d lost an arm to some powerful fighter I couldn’t identify. Unable to accept that his life was over, he charged at me.

But the fierce whoosh that came from behind me forced him to accept it after all.

*Boom!*

An absurdly huge War Hammer swept past, and the Kronos Guild Master’s face disappeared.

Behind his corpse, which crumpled like a rotten log, Chuck Hagel stood posed like a shot-putter.

After staring intently at me for a brief moment, he let out a short laugh and turned away. Then he charged the remaining traitors.

With a warm little line to thaw their frozen hearts.

“Let’s see you keep playing to the very end, you sons of bitches.”

Cheers and screams mingled in my ringing ears. Some fell, spraying blood; others stepped over their bodies and pressed on.

The tide had already turned.

Even if the goddess of fate showed up to tip the scales back, all we had to do was take her down, too.

Like the monster struggling to rise as I came within a few steps of him.

*Thud.*

When had I gotten this close?

I suddenly stopped. And, like an old man leaning on his cane after a long journey to visit a lifelong friend, I greeted him, weary but glad to see him.

“Hey. I’m here.”

*Clang!*

In reply, all I got was the still-brilliant blue gleam of his sword.

But even the sharp edge forged from Dragon Bone—a material without peer—couldn’t cut through Ten-Thousand-Year Cold Iron. And the strength and speed behind the sword were nowhere near enough.

Not enough to get past even me, a man who was practically a hospital patient.

Not enough to stop me from returning that rude answer.

*Thud. Crunch.*

Michael Silbert’s eyes flew wide open. His arms crumpled, the pain so intense that a scream, mixed with blood, bubbled up from his gaping mouth before he could even let it out.

*Grrk. Grrrk.*

Blood spurted intermittently, splattering my face.

But why?

If I thought about what he’d done up until now, the scent of blood seeping into my nose should have been sweet. But all I could smell was something revolting.

Maybe that was why I suddenly stopped.

Why my own face, reflected in those eyes darkened by blood and tears, looked twisted like a monster’s.

“……So this is the world you wanted so badly?”

I knew.

No matter what I asked, he wouldn’t give me the answer I wanted.

No answer could calm this heart and these emotions threatening to burst out of me.

But…… I still wanted to hear it. I had to hear it.

For the countless people who had died because of the pathetic ambition he’d held on to.

“Answer me.”

*Grab.*

I seized Michael Silbert by his one remaining horn and hauled him upright. Enduring the pain flooding over me, I whispered to him as he died by the second.

“Say something. Anything. Come on.”

And in the next moment—

I realized where his other horn had gone. Why it was nowhere to be seen.

*Thump.*

With a dull, wet sound, the horn shot up from somewhere and pierced someone’s palm.

But there was no blood, though blood should have poured out. No groan of pain held back.

All that filled the empty space was Michael Silbert’s trembling eyes, fixed over my shoulder, and his voice.

“How dare you… How dare a monster like you…….”

“Wrong. I’ll tell you this once, and only once, so you’d better remember it.”

At that familiar voice reaching my ears, I realized who was standing behind me and laughed out loud.

“My name is Stone King, you hideous monster.”
## Chapter artifact 786

# Chapter 786

“My name is Stone King, you hideous monster.”

The moment he spat out those words as if biting them off, the Skeleton King finally understood.

He had found the answer to the question that had tormented him for so long.

The days when he couldn’t sleep even as everyone else slept, when he was alone in death while everyone else lived their own lives.

And the one question that bound his body and mind like chains.

*Who am I?*

No matter how hard he’d thought about it, he’d never found an answer. But the answer had been there all along, within the Skeleton King himself.

*So that’s how it was.*

The Skeleton King muttered to himself.

In the black eyes he saw over a man’s shoulder, the radiance cast by his golden crown was reflected.

“What, exactly, did you want to become?”

At that offhand question, Michael Silbert’s eyes trembled.

The Skeleton King continued in a calm voice.

“There was a time when I was desperate to know. I tried to find a past I can no longer remember, and I didn’t know what to call who I am now.”

That was why.

One day, he had followed a human he met out of a forest filled with nothing but death and darkness, and set foot in an unfamiliar world.

“I wanted to find the answer in the world you live in. I believed I could.”

But he couldn’t. Even there, amid enormous metal boxes on wheels and buildings that towered higher than trees, the answer he sought was nowhere to be found.

To the Skeleton King, who had left the forest to find an answer, the world inhabited by humans was simply another forest.

“I can’t breathe or sleep. I can’t feel what other humans call the cool breeze or the taste of food. I can’t even feel the faintest, smallest pain.”

He learned for the first time.

That the inability to feel pain could itself be painful. And that some kinds of pain lay in the truth itself.

*Monster.*

That was the first word the Skeleton King had searched online the day he got a smartphone. It was one of the words he’d heard most often in the human world, and the word used to describe a being like him.

And so, his questions gave way to a new emotion, one he’d never experienced before.

It was anguish.

Anguish over having awakened as a monster against his own will.

Fear that to the people with whom he’d first begun to share conversations and feelings, and grow close, he might be nothing more than a monster.

“I wanted to deny that I was like them. So I fought alongside you, and for you, with everything I had. Because I believed it was the right thing to do.”

That belief hadn’t changed, even now.

If it had, he wouldn’t have considered sacrificing himself here today.

The Skeleton King didn’t want the humans he cared about to fall before the world did.

Humans were more complicated creatures than he’d ever imagined. Some harbored hideous rage and killing intent, just like monsters—or worse than monsters.

But humans also knew restraint and love. They thought and acted according to their own will.

When countless lives were lost or injured over petty disputes, when children no bigger than infants were abandoned in the street, humans were also the ones who took them in and embraced them.

That was why.

The Skeleton King had wanted to become a human like them.

Not a monster, but a neighbor. A friend accepted into the same community.

And it was why he’d despaired when he realized that was impossible.

But…

“Not anymore.”

The Skeleton King murmured calmly and gripped the horn piercing the back of his hand.

*Crack.*

He caught the hand gripping the horn as well—a hand that had been horribly bent and broken earlier but was slowly healing.

A voice that sounded as if it were boiling over slipped between Michael Silbert’s clenched teeth.

“You think, you think a mere monster like you can become human just by doing this…?”

“It doesn’t matter.”

“What?”

“I know. I’m a monster, so I can’t be called human. And because I live among humans, I can’t be called a monster.”

The Skeleton King smiled faintly.

“So what’s the problem? That’s enough for me.”

“……!”

“You wretched, pitiful monster. Let me introduce myself once more.”

Looking into Michael Silbert’s wide eyes, the Skeleton King spoke slowly.

“I am the master of the Black Forest, the ruler of all the undead, and a hero of this world who fought for you humans. You can call me the Skeleton King or the Stone King. Whatever name you use for me, it’s part of who I am. But…”

*Tap.*

The Skeleton King’s hand rose and came to rest on a man’s shoulder.

“I won’t tell you the first name I ever received in this world.”

Because…

It was a name only a friend could use.

“Isn’t that right, Jin Taekyung? You conniving human.”


* * *


I didn’t know what to say.

Should I laugh at the bastard, now that he’d finally come to his senses? Get angry? Or smack him upside the head as hard as I could, like I usually did?

Like someone who’d forgotten how to speak, I sank into a brief but deep debate before suddenly opening my mouth.

“Golgoli, you stupid son of a bitch.”

Bones.

The first name I’d given the undead of the Black Forest when we met.

Usually, he’d have thrown a fit and told me not to call him that. But today, he answered meekly.

“I admit it. I was a stupid son of a bitch.”

“……”

“I won’t doubt you again.”

Damn it.

I was speechless. I had nothing to say. But for some reason, I didn’t feel the least bit frustrated.

I just… felt relieved.

Like a stone weighing on my chest had disappeared. Like the distance between me and the guy—the distance that had never quite closed until now—had finally vanished.

Yeah. That was enough.

Feeling lighter, I threw a punch.

*Thwack!*

Michael Silbert’s face, slack with shock as I held him by the hair, snapped back.

But I wouldn’t even let him fall.

*Thwack, thwack. Crack.*

His proud nose caved in. Teeth poured out through his mangled lips.

Blood or tears streamed down his cheeks from eyes veined with burst capillaries.

His limbs, twitching in spasms, went limp.

*Crack. Crunch.*

I kept hitting him, breaking him, crushing him.

Every time I moved, every time my fists and feet slammed into him, the lingering aftermath of One Annihilation sent excruciating pain through my whole body. But I didn’t care.

If someone hadn’t grabbed my wrist, I might have beaten Michael Silbert to death right there.

*Grab.*

“Please stop, Mr. Jin. Not yet.”

A familiar voice, worn with exhaustion.

I turned my head without thinking and blinked. Team Leader Choi stood there, drenched from head to toe in blood.

No—all of them did.

“Jin, it’s over. It’s finally… finally over.”

Magic Johnson walked over with Chuck Hagel supporting him. He smiled weakly, but there was no joy in his expression at having won the battle that had decided their fate.

The hero’s smile, after having to kill people who’d once been his comrades, was dark and bitter.

Just like the silence that had settled over us, and everyone surrounding me.

“Oh.”

A sound escaped my lips, neither quite a gasp nor a groan.

Only then did I lift my head and look around. I realized that everything I’d been told was true.

*Whoooosh.*

A wind heavy with the smell of blood swept past.

Everywhere I looked, weapons without owners and bodies lay scattered.

Pools of blood on the floor soaked our shoes. The enormous Round Table, once a symbol of the heroes who had saved the world, had been shattered, leaving only ruins behind.

Yeah. It was over.

The first battle for humanity’s fate.

The battle between duty and self-interest. The battle between humans and monsters had finally come to an end.

In here.

And out there, where blood had been spilled beyond our sight.

*Eeeeeek. Boom.*

The entrance, already half broken, fell with a heavy crash. Tired footsteps followed, stepping over the fallen door.

*Clank. Clank.*

Armor and weapons soaked in blood.

At the sight of those figures filing in, looking no different from people drenched in gore, quite a few of the surviving Hunters reached for their weapons. But they stopped at Team Leader Choi’s timely question.

“How did it go?”

One of the two people at the front—a young man who still had peach fuzz on his face—answered in a military tone.

“We killed or captured them all. We took more casualties than expected because of a man named Huginn, but we joined forces with the Peace and Ares Guilds and subdued him. Then we dispelled the illusion magic surrounding the area and informed the Korean government a little while ago. Oh, and Mr. Shu here played a major role, too.”

“You’ve both worked hard. It would have been a difficult fight if you hadn’t trusted us and helped.”

At Team Leader Choi’s heartfelt words, the man in his thirties whom the young man had called “Mr. Shu” shook his head.

“I simply trusted the Übermensch’s judgment and choices. The man I saw in Munich that day was… a superhuman in every sense of the word.”

When the man looked my way, I gave him a slight nod in greeting.

And I did the same for the young man beside him, who watched me with an expectant look.

*Joel Schumacher. Xiao Shen.*

They owed me, and today they’d paid me back with interest.

The others probably had no idea that Joel Schumacher, who’d politely declined the invitation to the inaugural ceremony on the grounds of his injuries in Munich, had secretly entered Korea.

Or that Xiao Shen had brought the Hunters from the Public Security Ministry’s armed forces with him, and joined up with the elite forces of the Peace and Ares Guilds, who had finished making all the preparations.

I suddenly remembered a question Team Leader Choi had asked me a few days ago.

*“There’s a very thorough person. When do you think his greatest weakness is exposed, Mr. Jin?”*

The answer wasn’t hard. I’d seen it happen several times, and I’d made the same mistake myself.

*“When he thinks everything has gone according to plan.”*

The answer was right.

Perhaps Michael Silbert had been on guard against the possibility of something going wrong, but at the same time, he’d been certain of his victory.

If he’d been acting like himself, he would have chosen France—his stronghold—or somewhere else with a firm support base, instead of Seoul, for the inaugural ceremony.

But that little lapse, that petty desire to put his name on this historic place, had brought down his grand ambition.

And now, at this very moment—

I could hear it clearly.

“We’ve won.”

Along with Team Leader Choi’s words, echoing through the silent air, someone’s hideous ambition crumbled to pieces.

And I realized what I still had to do.

*…Yeah.*

To end everything, I had to erase the starting line where it all began.

Just as we had executed the traitors here today, the people who would have stood in the way of the great war to come.

I had to pull out the root. Otherwise, new weeds—and offshoots of this thorn tree—would keep growing.

*Michael Silbert.*

*Crack.*

I stomped on the chest of the man collapsed at my feet. The sound of bone shifting rang out.

Michael Silbert came to with a rush of blood spilling from his mouth and looked around with bleary eyes.

“So… it ended like this.”

His voice was fading, but his tone was composed.

He had probably realized it instinctively the moment he looked around.

That Huginn, his right-hand man, and the private army he had spent so many years training would never make it here.

“Did you kill them all?”

I answered evenly.

“The ones who were going to die died. The ones who were going to live lived.”

“Huginn must be one of the latter. He’s a useful man to question.”

“You know it.”

“Then I have a favor to ask.”

A favor.

At that unremarkable word, I suddenly felt disgusted and kicked him in the face.

*Thwack.*

His head snapped to the side, blood spraying through the air.

But maybe he couldn’t feel pain anymore. Without so much as a groan, Michael Silbert spat the blood filling his mouth and stubbornly continued.

“Tell Huginn this for me. I’m grateful for everything he’s done, and he doesn’t have to serve me anymore. If you do me this favor, we’ll both be better off. At least you can skip the unpleasant, tedious torture and interrogation.”

“Is that a kindness for a retainer who’s been loyal his whole life, or your last words?”

“Both, I suppose. Judging by your eyes, this is about to become my grave.”

I silently looked down at Michael Silbert, smiling without a sound.

And I was certain once more.

I couldn’t leave so much as the slightest opening when it came to executing him.

The law? A trial?

Those institutions were made for humans, not monsters.

Monsters should die like monsters.

So they could never struggle again. So that even the tiniest chance of the tumors he’d planted in this land over the past several decades saving that monster would disappear.

And yet, this was a lawful judgment.

Everyone here had witnessed the truth and fought through the bloodshed. They were witnesses and jurors, prosecutors and judges.

And from this moment on, they and I would finally become *us*.

Race. Sex. Age and borders.

We would stand together beneath one flag, even surpassing species.

In the name of the World Hunter Federation.

“Michael Silbert.”

My voice slipped between my lips, breaking the silence. I wasn’t channeling any internal energy, yet it filled the space and spread.

Loudly and clearly. On and on.

“From this moment forward, the World Hunter Federation revokes all your qualifications and summarily executes you as a traitor. Anyone who objects, step forward.”

Team Leader Choi answered at once.

“No objections.”

Magic Johnson followed.

“Everything according to the rules.”

Prince Felix bowed with dignity instead of answering, while Pai Chen and Chuck Hagel struck their weapons together.

*Clang!*

A deep resonance rang out beyond the devastated ruins.

As time passed, the weapons grew from one to dozens, then from dozens to hundreds, sending blue sparks flying.

One person pounded his armor with the only hand he had left. A white-haired elder struck the ground with his bloodied cane.

*Boom. Boom. Boom-boom-boom.*

The world shook. Pooled blood splashed in every direction.

No one objected. Everyone agreed.

To the World Hunter Federation’s first resolution.

To the death of a traitor born human and turned into a monster.

Amid the deep resonance that rang on and on, I stared at Michael Silbert and asked,

“Any objections?”

After a brief silence, he answered.

“None. At first, I fought with all my strength to survive. After that, I fought to get what I wanted.”

“Any last words?”

“It’s your turn now. Go on, struggle with everything you have. I’ll be watching from up there.”

As I listened to his mocking words, I lifted my spear. It felt heavier than ever before.

Then, in front of hundreds of pairs of eyes, I drove the spearhead down with all my strength.

*Thrust!*

The spearhead pierced straight through his throat.

With a choking sound that never made it out of his mouth, Michael Silbert’s body stiffened.

I looked into the monster’s eyes as life quickly drained away, then delivered the last words I’d put off until now.

“Just like you said, watch closely. Not from up above—from the very bottom, beneath my feet.”

“……!”

Did his eyes widen in anger at the last moment? Or because he could no longer stave off death?

Perhaps it was both.

*Ding. Ding. Ding.*

Countless chimes and radiance welled up inside me.
## Chapter artifact 787

# Chapter 787

“Ah.”

Jin Taekyung let out a single exclamation.

At that very moment, he could feel the full blessing of the supernatural power that had come to him.

Clear chimes, audible to him alone, rang incessantly in his ears, while countless holographic windows rose above the ruins and filled his vision.

*Ding. Ding. Ding.*

> **System**
> You have defeated Lv. 175 Michael Silbert!
> You have gained a tremendous amount of EXP and Fame!
> You have achieved the rare feat Cut the Weeds and Pull Up the Roots!
> We offer our unreserved praise for your bold decision to cut down the diseased grass and pull out its roots, for the sake of the forest where everyone lives together.
> But remember: the great fire that could consume the forest is more dangerous than any disease.
> You have gained a tremendous amount of EXP and Fame as a reward for your achievement!
> You have gained 20 points as a special bonus reward!
> Level Up!
> Level Up!
> Most of your injuries and Stamina have been restored by the stacked effects of leveling up!
> The special debuff Broken Body rejects the power of healing!

…

…

…

Countless notifications filled his eyes and ears.

At the same time, a warm radiance no one else could see or feel welled up from deep inside Jin Taekyung.

*Whoosh.*

An energy that could only be called purification, not merely healing, washed over his entire body like a downpour.

It embraced the waste that had naturally built up inside him, his damaged blood vessels and organs, and his broken and slashed bones and skin.

*Shhhhh.*

The excruciating pain that had been coming from every part of his body quickly faded.

Beneath the sticky blood covering him from head to toe, the injuries no one had noticed healed as if they’d never been there.

But none of that mattered to Jin Taekyung.

Not compared to the relief he felt at that moment.

*It’s over.*

Jin Taekyung let out the breath he’d been holding.

No trace of life remained in Michael Silbert, whose eyes were wide open even as he lay dead.

There was no doubt.

The bastard was dead for sure.

The scheming mastermind, more cunning than any enemy Jin had ever faced, the man who had shaken him to his core, had been born human and left this world in the form of a monster.

No—or perhaps, by now, his soul had fallen into the abyss held in those wide-open eyes.

Just like Jin’s final farewell to him, in the moment the cold spearhead pierced his throat.

“……Go to hell.”

With that one line, spat out between clenched teeth, Jin Taekyung gripped the spear shaft. Then he twisted it with all his strength, slicing through the monster’s neck.

*Slash. Splash.*

Along with a jet of green blood, Michael Silbert’s head came completely free of his body and rolled across the pool of blood.

At the same moment, as if on cue, a tremendous roar erupted. No—it was both a roar and a cheer.

*Boom! Boom-boom-boom!*

*Rumble!*

The hundreds of surviving Hunters roared as one.

Their mana-charged shouts burst through the compressed air, while the feet and weapons pounding the ground without pause shook the National Assembly building.

Some were simply overjoyed. Others trembled with anger that had yet to fade. And still others, staring blankly at them, began to cry.

Jin Taekyung let the spear that had ended it all hang limply at his side.

“……Fuck.”

Why was this such a big deal? Why did this little thing matter so damn much?

Even Jin Taekyung didn’t know.

Why had the curse suddenly slipped out? Why was he crying like an idiot while everyone else was celebrating?

But the voice that reached his ears a moment later supplied the answer for him.

“I don’t know what kind of stupid thought you’re having right now, but I’ll tell you one thing.”

The Skeleton King rested a hand on Jin Taekyung’s shoulder and continued.

“It isn’t your fault that people died. Just as this body became a monster against its own will.”

“……!”

“So stop bawling like an idiot. No one is blaming you or holding you responsible.”

At those prickly but warm words, Jin Taekyung fell silent.

Then, amid the endless cheering and rumbling, he suddenly let out a wry chuckle.

“Hey.”

“Hmm? Did you call?”

“Why are you suddenly acting all serious, you monster bastard?”

“……!”

“What are you looking at? Keep your eyes nice and polite.”

The Skeleton King had been quietly hoping for a response, though he’d tried not to show it. Now, he muttered with a stunned look on his face.

“Is this what human nature is really like……?”

“I can hear you.”

“I meant you to.”

“A monster……talking back?”

“Ah, enough already!”

Teasing the Skeleton King. No, teasing his friend was always fun.

At the Skeleton King’s fit of outrage, Jin Taekyung chuckled and laughed, even wiping away his tears with his blood-soaked sleeve.

“And don’t try to sneakily wipe your tears. It’s too late for that.”

“……You’re spreading false rumors, you bastard. When did I do that? Got proof?”

“No proof, but I’ve got witnesses. Plenty of people saw it besides me—huh?”

*Grab.*

The Skeleton King’s eyes widened as Jin Taekyung suddenly staggered and he caught him by the arm.

“You……”

“Ah. The floor’s slippery with blood.”

Jin Taekyung answered with a grin. But he couldn’t hide his quivering lips or the exhaustion in his half-closed eyes.

It was only natural.

The effects of leveling up twice had healed most of his injuries. But all the events that had led to this moment, along with the mental strain, were more than a young man barely in his twenties could bear on his own.

The sleepless nights and countless battles had begun the day he learned the truth about Michael Silbert’s hideous nature and ambitions.

For the past few weeks, Jin Taekyung had fought day and night.

And Michael Silbert and the countless monster hordes weren’t the only enemies he’d had to bring down.

There was the world’s harsh, ever-growing condemnation. There were the disasters he’d heard about from every corner of the world on the news, and his own self-loathing at being powerless in the face of all those deaths.

Jin Taekyung had fought himself, and he had fought the world.

Now that he’d finally defeated Michael Silbert, even standing still demanded superhuman patience.

But……

*I can’t.*

Jin Taekyung struggled to lift his eyelids as they kept drooping shut.

Not yet. He had to hold on a little longer. Just a little longer.

Until he finished what he’d started.

The sirens, now mingling with the people’s cheers, were getting closer. He couldn’t collapse before he told the world the whole truth about what had happened here today.

*No matter what.*

*Thump.*

Using the spear he’d driven into the ground as a cane, Jin Taekyung leaned against it and murmured in a voice that seemed about to fade away.

“Thanks so fucking much, Assistant Hwang, you son of a bitch……”

“Are you really okay……? Wait, what did you just say?”

“Hey, Golgoli.”

“Huh?”

“You should use a spear too. Not a sword.”

What? Out of nowhere?

The Skeleton King blinked, utterly unable to process the situation.

“Why?”

“Compared to a sword……”

“Compared to a sword.”

“A spear……”

“A spear.”

“Looks cooler.”

“Looks coo……Fuck.”

The Skeleton King sighed.

Why had he ever listened to that human bastard who wasn’t even human?

Half the time he spouted nonsense, and the other half he chewed him out with profanity.

*I’m the idiot.*

But the Skeleton King said nothing. He only sighed.

He didn’t want to wake his friend, who had fallen into a deep sleep as if he’d passed out, leaning against the spear driven deep into the ground.

*You’ve worked hard. Rest.*

Perhaps everyone felt the same way.

As if they’d never cheered at all, the hundreds of Hunters pressed their lips together in silence and simply looked on.

At the young man who had been braver and brighter than anyone else here today.

At the superhuman who had faced the whole world and steadily walked the path he had to follow, in the darkness of a truth where he couldn’t see even an inch ahead.

*If it were me, could I have done what he did?*

Everyone asked themselves, then arrived at the same answer.

No one here could have done it.

They would have fallen, scraped themselves raw, shattered and broken, then finally gone down and never risen again.

But that young man, barely in his twenties—that Jin Taekyung—had done it.

No matter how many times he fell, he got back up. No matter how badly he was battered and broken, he refused to go down.

He alone had become a signpost and a beacon, lighting the way for those who had been lost in the darkness.

The one who led everyone from the front.

The one who felt the pain of the wounded alongside them, but was never weak—and pressed bravely onward with an unbreakable will.

And that was what people called such a person, with all the reverence and love in the world:

*Hero.*

The moment that short word filled their minds, everyone there was seized by an indescribable emotion.

Hero. It was a word they knew all too well.

At some point, the whole world had begun calling them heroes. One ordinary day, they’d gained unexpected powers, fought monsters, and become humanity’s sword and shield.

But why?

Why did that word, heard so often it had nearly worn grooves in their ears, make their hearts swell like this?

Why did every moment of the past feel both shameful and achingly poignant?

All they could see, over and over, was the look in his eyes as he shouted the truth without fear, surrounded by hundreds of weapons.

And the sight of a young man weeping alone, while everyone cheered at the end of the fierce battle.

That was probably why the many reinforcements entering the National Assembly, now a ruin, stopped in their tracks without realizing it and held their breath.

And why, in a silence so deep it seemed you could hear a needle drop, someone let out the breath they’d been holding.

“Fuck.”

People turned their heads at the sudden break in the silence and were surprised three times.

First, that anyone could curse in such a refined manner.

Second, that a curse could sound so awkward.

And finally, that the person who’d managed both at once was someone they’d never expected.

But Prince Felix himself paid no attention to the eyes gathering on him.

No—he didn’t care anymore.

“Fuck. Fuck. Fuck.”

It was a relief.

His pronunciation was still far from perfect, but after spitting out one curse after another, it felt as though something knotted in his chest had loosened.

Prince Felix found himself chuckling.

*Damn it. What was so important about all that?*

Bloodline. Dignity. Appearances. Etiquette.

Every value he’d proudly held onto for more than thirty years felt empty and burdensome.

So much so that he wanted to cast them all off right then and there.

So that was what he did.

For the first time in his life, he let loose a filthy curse like a dockworker and threw off the armor engraved with the royal crest.

For a moment, he wondered what expression His Majesty the King—his father—would have worn if he’d seen him like this. But, well.

*Was that really so important?*

*Clop. Clop.*

Under the gaze of the people, Prince Felix slowly crossed the ruined space and stopped.

Then he spoke without preamble.

“It looks as though you could use another pair of hands. If you don’t mind, may I help?”

At Prince Felix’s most courteous offer yet, the Skeleton King nodded. He was supporting Jin Taekyung, who had collapsed into sleep against the spear shaft.

“If you wish, then do so, human prince.”

And Prince Felix’s response was enough to astonish everyone watching them from nearby.

“Please call me Felix, Mr. King. My friend.”

“……!”

Prince Felix smiled faintly at the people staring blankly at him. Just as he took one side of Jin Taekyung’s shoulder, another hand reached out to help.

“You……”

“Watching from the side, it seemed you could use another pair of hands.”

Choi Minwoo answered calmly, and more hands joined in.

One trembling hand belonged to Chuck Hagel, who was already acting as if he were going through withdrawal. The unusually small, heavily callused hand belonged to Faye Chen.

As for Magic Johnson, he stared at the staff in his hand for a moment, then suddenly grinned.

“Sometimes I feel like everything I’ve learned is useless. Like right now.”

Magic Johnson tucked the staff away and strode over to lend a hand.

At first glance, it was hard to understand.

A Grand Mage who had mastered hundreds of spells, and the finest Hunters, capable of slicing through tons of concrete in an instant, had all gathered to lift one young man.

But that was how they truly showed their respect.

*Rustle. Rustle.*

The only sounds were the quiet brushing of clothes. The helping hands had multiplied until there were hundreds, sending ripples across a lake as they slowly lifted the sleeping young hero above their heads.

As carefully as if he were made of glass.

So that the peace that had come to him, if only for a little while, wouldn’t be disturbed.

And when at last they laid Jin Taekyung down against the ground, everyone suddenly realized:

The inaugural ceremony of the New World Hunter Federation, which would be recorded in the history of humanity, was not over yet.

That the young man before them would be both the beginning and the end of the Great War to come.

*Shing.*

A cold scrape cut through the silence.

At the same time, a sword slowly slid free and pointed toward the sky.

Soon, countless weapons—dozens, then hundreds—glinted in the sunset streaming through the shattered stained glass.

In the ruins, steeped in the reddish warmth of flames, they were turned toward the young man immersed in an unbreakable peace.

No.

Toward their new Alliance Leader.

*Ding. Ding. Ding.*

> **System**
> You have achieved the unbelievable feat A Coronation for One Person Alone!
> The World Hunter Federation appoints you as its Alliance Leader!
> You have gained a tremendous amount of EXP and Fame!
>
> …

…

…

The chimes, audible to just one person, rang clearer and louder than ever.

Loud enough for a smile to brush the lips of someone deep in sleep.

Loud enough to melt the guilt still lingering in a corner of his heart.

And so, at the end of a long and fierce day, a new page of history was turning.
## Chapter artifact 788

# Chapter 788

Paris, France. The Élysée Palace.

Unlike most French people, who counted fine food among life’s virtues, President Emmanuel had finished a short, simple breakfast. Now he gazed wistfully at a box of cigars he’d kept safely stored away.

*At last, the day has come to take these out.*

President Emmanuel had been a nonsmoker for twenty years.

In his youth, he’d been known to those around him as a cigar aficionado. But everything changed after he met one man.

“I hear you like cigars.”

“Ah, I enjoy one now and then as a hobby.”

“Then that’s quite an expensive hobby. Most people can’t spend over ten thousand euros a month just to sit in their garden and burn weeds.”

“……!”

“You said you wanted to go into politics, didn’t you? Then you’d be wise to cut back on the cigars. They’re a monster that devours both your time and your health. And there’s no easier target to tear apart than a wasteful politician from a family of businesspeople. All right, you may go.”

His first meeting with the powerful man, arranged through his family’s connections and enormous lobbying efforts, ended just like that—with an absurdly simple piece of advice to cut back on cigars.

But Emmanuel, a promising young lawyer, didn’t forget that advice.

As soon as he returned to his mansion, he threw every last one of his cigars—worth hundreds of thousands of euros—into the fireplace and began living a far more modest life.

Then, a few years later, at Easter, he received a card bearing the image of two ravens.

> Congratulations on your rebirth.
>
> M. S.

That was how Emmanuel was chosen by Michael Silbert. The following year, he made his dazzling debut in French politics, basking in the spotlight.

And after that?

What more was there to say?

Emmanuel rose faster than anyone.

It took barely a decade for him to establish himself as a force no political heavyweight—not even a prime minister or president—could treat lightly. Michael Silbert’s shadow was more than enough to cover everything.

“Run in the next presidential election. You won’t be the youngest, but I’ll help you make history as the longest-serving president.”

*I’ll help you.*

At those words from Michael Silbert, Emmanuel—now a senator who embodied Paris and the leader of the largest party in parliament—had a sudden certainty.

The election was over before it even began.

He would be the next master of the Élysée Palace.

And at last, on the day that prediction came true, President Emmanuel mustered the courage to ask the benefactor who had come to see him:

“Why did you choose me, of all those people?”

The answer was brief.

“You listened well.”

“Pardon?”

“I want only one thing: give me your absolute loyalty, just as you have until now. If I tell you to bark, bark. If I tell you to bite, bite. As long as you don’t repeat your predecessor’s mistake, I’ll place not only enormous wealth and honor in your hands, but this entire country.”

“……!”

“Will you be loyal to me?”

“No. I’ll obey you.”

At that flawless answer, Michael Silbert laughed aloud and handed his new watchdog a box of cigars decorated with gold leaf.

“These are……”

“A gift. When my goal is realized, you’ll be as good as a king. Save these cigars for that moment.”

The memory of that day was still vivid.

As President Emmanuel gazed at the box and sank into thought, he felt his heart pound.

*A king. A king.*

A king in the modern twenty-first century—in a country obsessed with revolution, no less.

It was insane.

But when Michael Silbert said it, that was different. He was a man who had made countless impossibilities and wild imaginings come true.

President Emmanuel suddenly recalled the last words of his father, who’d used the chaos of the Great Cataclysm as a springboard to amass an astronomical fortune in no time.

> Everything that happens in this world is an investment and a deal. If someone wants something, give it to them freely. But you must always get back more than you gave.

People had despised his father, calling him the “Merchant of Death.” But even if he had gone to hell, he probably had few regrets.

He must have watched his son make the most successful deal of anyone.

Young lawyer Emmanuel had given one man a loyalty bordering on obedience, and in return he became President Emmanuel.

Soon, he’d possess power beyond the presidency—such overwhelming might that he could rightly be called Emmanuel the First.

“Emmanuel the First……”

President Emmanuel murmured dreamily, lost in his fantasy, when the grandfather clock against the office wall chimed.

*Dong. Dooong.*

With the chimes, a bird and a dwarf popped out of the clock and spun around.

President Emmanuel blinked as he checked the hour hand.

“Noon? Already?”

He must have lost track of time while reminiscing. President Emmanuel slowly tapped the desk in his office and thought:

*It’s taking longer than I expected.*

Taking the time difference between France and Korea into account, it was now eight in the evening in Seoul, where the World Hunter Federation’s inaugural ceremony was likely underway.

He checked his smartphone just in case, but the message he’d been waiting for hadn’t arrived.

*Well, it would be strange if it ended early.*

This wasn’t just any gathering. It was the first inaugural ceremony of the World Hunter Federation.

Given the importance of the event, which would shape the future of security around the world, it was hardly surprising that the meeting was dragging on like a full-course marathon.

Of course, even with his unwavering faith in Michael Silbert, he couldn’t help feeling a little anxious.

*Knock, knock.*

President Emmanuel frowned at the sudden knock.

“What is it?”

An attendant’s voice came through the crack in the closed door.

“It’s time for your meal, Mr. President.”

“I don’t need it. And don’t let anyone near my office until I call for them myself. Understood?”

“Yes, I’ll pass that along.”

How could he have an appetite with the most important moment of his life just ahead?

President Emmanuel cursed inwardly at his dim-witted attendant, then stared down at the smartphone in his hand.

After hesitating, he tapped one person’s number.

*Brr. Brr. Brr.*

The call rang on and on.

President Emmanuel was doing his best to suppress his anxiety as he ran his hand over the cigar box when, at last, there was a click and someone answered.

“How did the ceremony go? The inaugural ceremony?”

After a brief silence, the other person replied.

“It ended successfully.”

The words he’d been waiting so long to hear.

President Emmanuel felt joy surge through his whole body and burst out laughing.

He swung the fist he’d clenched without even realizing it and thanked the man who’d given him the answer he’d wanted so badly.

“Thank you! Thank you so much! Huginn, you’ve been through so much, too—!”

“Thank me? I’m the one who should be thanking you.”

“What?”

At that moment, President Emmanuel suddenly realized.

The voice on the other end was deeper and rougher than usual.

And the owner of that voice wasn’t in Seoul.

He was standing outside the door.

The price for realizing it too late was about to be paid.

*Crash!*

With a thunderous boom, the door to the office, which had stood for hundreds of years, burst into dust.

A broad-shouldered man, his hair half gray, strode through the wreckage and gave the frozen President Emmanuel a friendly smile.

“Long time no see, Emmanuel. You little rat—I could tear you apart and kill you, and it still wouldn’t be enough.”

“You—you’re……”

“Funny, isn’t it? A moment ago, I thought I could fall asleep in three seconds. But looking at your face has driven the tiredness right out of me. Johnson, who should be in Switzerland right now, probably feels the same way. Don’t you think?”

Chuck Hagel laughed heartily.

He shoved Huginn’s smartphone into his back pocket, then continued speaking to President Emmanuel, who stood frozen like a statue.

This time, his voice was as deep and dark as an abyss.

“Michael Silbert is dead. In the name of the World Hunter Federation. By the hand of the new Alliance Leader we chose ourselves.”

“……!”

“Now, you can choose. Do you want to be carried out with every limb broken, or do you want to walk out on those swizzle-stick legs of yours?”

It was over. All of it was over.

Everything he’d built, along with every future he could have had, had collapsed.

Facing this unbelievable reality, President Emmanuel trembled, unable even to remember how to breathe.

After countless thoughts and doubts, he managed to force out a single word.

“C-cigar.”

“What?”

“Would you mind if I smoked one cigar before I go?”

Chuck Hagel blinked, then burst into a hearty laugh.

“A cigar, huh? That sounds good.”

Then he drove a fist like a lump of iron straight into President Emmanuel’s face.

*Wham! Crash!*

Teeth and blood sprayed into the air. President Emmanuel shot away like a cannonball, smashed through the window, and disappeared from sight.

“Asshole. What kind of question was that?”

Chuck Hagel muttered, then looked down through the window.

Dozens of Ares Guild members waiting below were pouring potions over President Emmanuel’s body, which had dropped out of the sky.

“Is he alive?”

“Yes, sir. He’s alive, all right.”

“Good. Just keep him breathing.”

“Understood. But, Mr. Hagel, where are we headed next?”

“Don’t worry about it. Our mission is over.”

“So we’re heading straight back?”

“No. Wait a little. There’s still something to do.”

Chuck Hagel opened the cigar box, set neatly on the table, and smiled with satisfaction.

“Something very important, yes.”

A little while later, people drawn by the unexpected commotion saw their president being carried away, his entire body crushed, and pale smoke drifting out through the broken window of the Élysée Palace.

But that wasn’t the last shock they would face.

When they picked up their smartphones to report this unprecedented crime, an enormous bomb no one could have foreseen rocked the world.

> **Breaking News:** World Hunter Federation’s first official announcement: “Two hours ago, we summarily executed Michael Silbert and his followers, who betrayed humanity. The operation is still ongoing.”
>
> **Unprecedented bloodshed.** Choi, descendant of the Savior and interim spokesperson for the World Hunter Federation: “We will reveal the truth, along with all the evidence.”
>
> **[Live] World Hunter Federation Official Press Conference**

The press conference began amid such confusion and shock that “unprecedented” hardly did it justice.

And even as Choi Minwoo calmly continued speaking before everyone, captured by hundreds of camera lenses, the key figures of the New World Hunter Federation spread across the globe like dandelion seeds on the wind, uprooting the weeds Michael Silbert had left behind.

One day. Two days. Three……

Even on the day a young man finally woke from his deep sleep, they were still at it.
## Chapter artifact 789

# Chapter 789

It must have started a few years ago.

That was when I, who used to fall asleep as if I’d passed out whenever I closed my eyes, no matter where or when, began having nightmares.

In a way, it was only natural.

Even someone with nerves of steel could only take so much. Cross the line between life and death several times a week, watch people close to you die or get hurt, and sooner or later, you start to fall apart.

The nightmare that came this time was much the same.

But it was far calmer, sadder, and, in a way, even more welcome than the ones I usually had. Because I met people I missed inside it.

“Son. While Dad’s at work, be a good boy and play with Hayeon, okay?”

I heard my father’s voice.

“Just call me hyung. Hyung.”

“Whoa, we hit the jackpot with these Magic Gems today. Since we’re on a roll, let’s keep going till the end of the day, yeah?”

I saw the smiling faces of Cheonsu hyung and the other team members who’d died in the mutation Gate.

“It wasn’t your fault. You did everything you could.”

I got to stand by Kim Butler’s side once more as he panted for breath and tried to comfort me.

Of course, if it had ended there, I wouldn’t have called it a nightmare.

Even in my dream, I fought without stopping.

I cut down people who all looked the same and drove my spearhead into monsters’ chests.

Then, amid blood that reached my thighs and corpses piled like mountains, I heard the screams of those I hadn’t managed to save.

“Help me! There are people here! Please, at least save my child…”

When I looked around, I found myself surrounded by a hellscape.

No—maybe it was hell itself.

A familiar face, one more at home in this place than anyone else, came into view.

“This is a pleasant place, wouldn’t you say?”

“Go fuck yourself.”

I swung my spear as I answered.

*Slash.*

Michael Silbert’s head sprang into the air as he approached at a leisurely pace.

But the smile on his lips and the gleam in his dark eyes didn’t disappear.

“Take a good look. At this landscape we made together.”

His headless body moved of its own accord.

*Clap. Clap. Clap.* The slow applause rang out, and I clenched my teeth. Flames erupted from my slashing spear and swallowed him.

*Whoosh!*

Michael Silbert’s body, moving as though controlled by invisible strings, turned to ash and crumbled away.

But the flames weren’t satisfied. They raced over the blood pooled everywhere.

Farther. On and on.

*Fwoosh.*

A monstrous blaze fed on the blood and countless corpses like firewood, completing the hellscape.

The screams of the living rose higher than ever—then faded without a trace.

Everything was dead. Everything was burning.

The terrible scene before me was something beyond a dream.

I let my spear droop limply and stared blankly as the whole world went up in flames.

Then I heard the voice of a monster who had stubbornly survived even this calamity.

“Do your best to survive to the end. Struggle with everything you have, every moment, until the very last day of this world. That way, you’ll be able to witness this sight with your own eyes, right until—”

*Pop! Thud-thud.*

I stomped down with all my strength, and his head burst like a watermelon.

But the silence that finally came wasn’t an ending. It was the beginning of something new.

*Crack. Crack.*

The world shook with a deafening roar.

The sky split apart, and space warped in every direction.

At the same time, a single word flashed through my mind like a bolt of lightning.

*Rift.*

*Rrrumble!*

That was when it happened.

As my senses slowly slipped away, someone’s distant shout reached me and pulled my mind up from the depths of the nightmare.

“...ppa!”

Ppa?

“Oppa!”

“……!”

At that moment, a radiant light filled my vision, and I woke from the nightmare.

At last, I saw Hayeon’s face, drenched in tears for some reason.

After a brief but difficult deliberation, I greeted her with all sincerity.

“Don’t cry. You’re ugly enough as it is. If your makeup runs, it’ll only get worse…”

*Smack!*

Ow.

I hurt, therefore I am.

* * *

I couldn’t tell how the rest of the day passed.

The instant I woke up, Hayeon—the recipient of my unfiltered honesty—smacked my arm with a hand just as sharp as Mom’s.

Then she hugged me for the first time since kindergarten and burst into tears.

Mom stepped away for a moment, then came hurrying back… There’s no point going on. It’ll only make my mouth tired.

She sobbed so bitterly that I thought I’d woken up in a morgue instead of a hospital room.

If the medical staff who’d been waiting nearby hadn’t insisted she stop, I might have drowned in their tears. I’m only exaggerating a little.

“Um, family members. We need to run some tests first, so please calm down a little…”

Mom wouldn’t have budged even if Demon King Asmodeus had come knocking—but a few words from a renowned doctor and healer were enough to make her step back without a fuss.

Of course, she didn’t forget to clutch their hands and beg them to take good care of me.

“Please look after my son. Make sure nothing’s wrong with him. And there won’t be any lasting effects, right? I heard from my younger one that Taekyung was talking nonsense as soon as he woke up…”

“Nonsense?”

“Yes. I’m not sure exactly what he said. I was away for a moment when it happened.”

“Understood. Patient, do you remember what you said?”

I answered.

“I told her not to cry because she’d look uglier if her makeup ran.”

“……”

“And it wasn’t nonsense. I almost closed my eyes again as soon as I opened them.”

“……”

“You may not know this, but once she takes off that makeup, it’s a disaster. You don’t have to go looking far for a monster wave.”

Hayeon glared at me as if she wanted to kill me, while the medical staff listened with their mouths hanging open. Then they gathered in a corner of the room and started whispering.

“Is he all right?”

“Does he look all right to you?”

“Hard to say. His younger sister looks pretty, at least. Her makeup’s waterproof, so I don’t think it ran…”

“I can’t believe this. Is that what you’re worried about right now? Are you in your right mind? Who recommended you for this job?”

“I did. Sorry.”

“I’m sorry, Professor. What should we do?”

“Hmm. There doesn’t seem to be anything obviously wrong with his body, but… His brain could have been affected. Let’s run a full set of tests.”

“Yes. We’ll include a psychiatric evaluation.”

“……”

I’d told the truth and they were treating me like a lunatic.

It was unfair, but there was nothing I could do. The fastest way to stop Mom from crying was to show her I was healthy.

*Like I’d be sick.*

But I swallowed that thought and cooperated with the healers and doctors.

And even after completing every test known to this world, I was forced to rest until the next day.

Two days.

It wasn’t a bad stretch.

Actually, if I’m being honest, it was peaceful for once.

I was stuck in bed for two whole days, without a smartphone or TV, all in the name of resting. But the people I cared about most were right there with me.

I ate, slept, laughed, and chatted with my family. It felt like a dream.

If not for the nightmare I’d had just before waking up, those days would have been so happy I wouldn’t have felt a hint of anxiety.

But I already knew.

I couldn’t make that time last any longer.

If I wanted to stop the unease growing inside me, it was time to step back out into the world.

Mom and Hayeon. The medical staff. And all the friends who didn’t come to visit because they wanted me to rest.

Even if the others were considerate enough not to tell me what was happening outside, the System wasn’t.

*Alliance Leader, huh?*

I saw the System notifications I hadn’t had a chance to check and found out: right after Michael Silbert was finished off for good, the World Hunter Federation had appointed me as its new leader while I was unconscious.

*Never thought I’d end up as Alliance Leader, of all things.*

I was surprised at first, but after thinking it over, I decided to accept.

It was their decision, but it was mine too.

I’d seen more than once what someone’s ambition, their hunger for power, could bring about.

Team Leader Choi or Magic Johnson would make several times the leader I could—but if I was the one they chose, then even if I wasn’t ready, I was willing to live up to their expectations.

*I’ll do the best I can.*

But before that, there was one thing I had to take care of.

“Hayeon.”

“Yeah?”

“You know Team Leader Choi’s number, right?”

“No. You need to rest.”

Her answer was immediate and firm.

Hayeon continued, her face set.

“Mom would be thrilled to hear that. Right?”

“Call him for me.”

“……”

“There’s something I need to take care of. Please.”

At my sincere request, Hayeon bit her lip.

“Ugh, this is driving me crazy.”

“Thanks.”

“Are you crazy? Who said I’d call him for you?”

“You always bite your lip before agreeing to do me a favor.”

“……”

Hayeon stared at me without a word, then let out a deep sigh. That meant yes.

* * *

“The wind’s cold.”

That was the first thing Team Leader Choi said when I saw him after several days.

I was sitting on an empty bench. I smiled broadly, glad to see him.

“How long has it been?”

“Today makes exactly one week since that day.”

“Must’ve been a busy week. In more ways than one.”

Team Leader Choi smiled along with me and joked.

“Yes. While you were lying comfortably in bed, we were running around like mad.”

“You make me feel bad. Should I apologize?”

“No need. It’s one of the perks of being the boss. Though the press is desperate to find out about your condition.”

“Fair enough. They made a fuss last time, too. Now I’ve even got the title of Alliance Leader.”

Team Leader Choi paused at my calm response.

“You knew?”

“Yes.”

“That’s not quite the reaction I expected. Did your family tell you?”

“No. They wouldn’t even let me lift a finger.”

“Hmm. I wonder where the news leaked from. I made sure to keep everyone quiet for the sake of your recovery.”

“Who knows? I’ve got sources you don’t know about, too.”

Team Leader Choi studied me for a moment, then nodded without saying anything.

The gesture said he wouldn’t ask any more.

He had a hunch I was keeping some secrets from the others. What mattered more to him was why I’d contacted him just two days after waking up.

“Things outside are going smoothly, despite what you may think. You could rest a little longer.”

“Is that so?”

“Yes. A week ago, we arrested a number of key figures who had close ties to Michael Silbert. Among them…”

He rattled off names: French President Emmanuel, Swiss Interior Minister Werner, who was almost certain to become the next president, and the head of a massive corporation.

Every one of them was a heavyweight who held sway over politics and business around the world.

There were so few Hunters among them because the ones you could call the brains behind it all had either died alongside Michael Silbert that day or been captured.

“It was a bold and brilliant decision. If you’d let them live, a much larger civil war would have broken out.”

Yes. That was exactly why we couldn’t let the bastards live.

The battle at the National Assembly had been a bloody bargain: their lives to prevent tens, perhaps hundreds, of thousands of others from dying.

But even so, Team Leader Choi never brought up the one thing I wanted to know.

What had happened to the one person I was worried about. The source of this unease.

“Team Leader Choi.”

I looked up at the night sky, thick with stars. No—or rather, I looked at the Main Quest, *Cataclysm*, still hanging there, and continued.

“Where is The Prophet?”

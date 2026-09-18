# Checkpoint Review — 400–404

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

# Chapters 400–404

## Plot

Jin Taekyung discovers that the black knight is Lei Fei, the missing Chinese S-rank Hunter and Wei Fenghu’s nephew. Although Lei’s memories return, the unidentified lord’s word-spell forces him back into his undead role as supreme commander of the dead. Jin’s command to rest breaks the control, allowing Lei to lead the fallen Public Security Armed Forces Department Hunters in one final battle. After the monsters are destroyed, Lei entrusts Jin with his love and apology to his family, urges him to go west and end the war, and disintegrates.

Wei Fenghu and thousands of Hunters arrive at the devastated Western Front. Jin delivers Lei’s final message, receives Lei’s sword, Hero’s Soul, and asks that Lei be listed among the dead despite the absence of a body. Hero’s Soul briefly grants Jin Hero’s Power before rejecting him when he imagines using it for an unworthy purpose. The Skeleton Warlord confirms that only a faint trace of Lei’s soul remains in the sword and admits it has no memories of its own past. Jin is then summoned to a meeting with Wei and five S-rank Hunters, where he declares that they must end the war by killing the force responsible for the catastrophe.

## Continuity

- Lei Fei is confirmed to be the black knight, a level-120 undead whose body collapses after the Arch Lich’s control is broken.
- Lei Fei leads the undead remnants of the Public Security Armed Forces Department in a final battle, then dies after asking Jin to convey his love and apology to his family.
- Lei Fei’s wife and daughter were moved to safety while he was missing.
- Wei Fenghu and more than four thousand Hunters have reached the Western Front. Jin survived the dangerous teleportation and the battle.
- The Western Front city has no recoverable survivors among those who remained to fight; the known survivors include the Public Security Armed Forces Department regimental commander, Jin, and one other person identified by the searchers.
- Jin publicly minimizes his role, insisting that the other Hunters fought desperately and that the battle was nearly over when he arrived.
- Hero’s Soul is a Supreme Peak sword that can grant Hero’s Power to someone it recognizes as upright. It rejected Jin and removed the power after he formed an evil intention, even in jest.
- The Skeleton Warlord absorbed some of the mana released when Lei disappeared and confirms that only a faint trace of Lei’s soul remains in Hero’s Soul.
- The Skeleton Warlord has no memories of its own past and is beginning to question what it once was.
- Wei Fenghu and five S-rank Hunters are assembled with Jin for an operation intended to end the war.
- The unidentified lord who controls the undead, the Second Fiend assigned to Qingcheng, and the Arch Lich’s larger objective remain unresolved.

## Translation Decisions

- Use **Jin Taekyung**, **Wei Fenghu**, **Lei Fei**, **Hero’s Soul**, and **Hero’s Power**.
- Render **검은 기사** as **black knight**, distinct from **Death Knight** and **Death Knight Lord**.
- Render **언령** as **word-spell**.
- Keep **Nightmare** unchanged.
- Render **진 선생** and **진 선생님** as **Mr. Jin**.
- Preserve Jin’s blunt, profane, self-deprecating voice; Lei Fei’s formal, wistful military voice; and the Skeleton Warlord’s formal self-reference.

## Durable state

{
  "active_continuity": [
    "Wei Fenghu and more than four thousand Hunters have reached the Western Front, where the battle left the small city with no recoverable survivors among those who remained to fight.",
    "The known survivors of the Western Front catastrophe are the Public Security Armed Forces Department regimental commander, Jin Taekyung, and one other person recognized by the searchers as the final survivor.",
    "Lei Fei died after completing his final mission, and Jin has asked that Lei Fei be recorded among the dead even though his body cannot be found.",
    "Jin publicly insists that he did not win the battle alone and that the other Hunters fought desperately before his arrival.",
    "Wei Fenghu and five S-rank Hunters are assembled with Jin to pursue the culprit behind the catastrophe and end the war.",
    "Hero's Soul is a Supreme Peak sword that can grant Hero's Power to someone it recognizes as having an upright character.",
    "Hero's Soul rejected Jin and removed Hero's Power when he formed an evil intention.",
    "The Skeleton Warlord absorbed some of the mana released when Lei Fei disappeared and confirms that only a faint trace of Lei Fei's soul remains in Hero's Soul.",
    "The Skeleton Warlord has no memories of its own past and has begun questioning what kind of being it once was.",
    "The wider war against the Arch Lich remains unresolved, and Jin has now committed to the operation intended to end it."
  ],
  "continuity_sources": [
    404,
    403
  ],
  "open_questions": [
    "Who is Lei Fei's unidentified lord, what is the lord's origin, and how does the lord relate to the Arch Lich's objective?",
    "What happened to the Second Fiend assigned to the Qingcheng attack?",
    "Will Jin and the five assembled S-rank Hunters defeat the Arch Lich and end the war?",
    "What kind of being was the Skeleton Warlord before it became an undead commander?",
    "What specific situation will allow Jin to draw out Hero's Power more strongly?"
  ],
  "safe_through": 404,
  "temporary_decisions": [
    "Render 나이트메어 as Nightmare.",
    "Use black knight for 검은 기사 and keep it distinct from Death Knight and Death Knight Lord.",
    "Render 언령 as word-spell.",
    "Render 영웅의 혼 as Hero's Soul and 영웅의 힘 as Hero's Power.",
    "Render 진 선생 and 진 선생님 as Mr. Jin while preserving Jin's blunt, profane voice."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 400

# Chapter 400

At the very first moment he clashed with Jin Taekyung, the black knight instinctively realized it.

*Strong.*

The young human before him was an unbelievably powerful opponent. Someone whose strength was so great that even if the black knight gave it everything he had, he could not guarantee victory—or perhaps someone even stronger than that.

As they traded attack and defense again and again, the thought only grew firmer.

*This will be a difficult fight.*

But the black knight was neither frightened nor willing to retreat.

He was his lord’s most loyal servant, a being entrusted with the mission of carrying out his orders.

This was a battle between powerful beings who had transcended their limits. Even the slightest difference could turn victory into defeat.

*If I do not give up, an opportunity will come.*

The black knight knew that well.

It was something he had repeated to himself ever since he was a child in training, and surviving countless battles had allowed him to grow into a powerful warrior.

*…Me?*

Confusion came over him again. As his mind grew disordered, his hands and feet grew clumsy.

And his opponent was neither weak nor careless enough to miss such an opening.

Whoosh, scrape!

The spearhead tore through dead flesh.

Boom!

Blue flames slammed into his chest.

Amid that heat, so intense it seemed close enough to grasp, the black knight suddenly felt something.

The name of that sensation was pain.

*What is this…?*

What disconcerted the black knight was not the fact that he could feel pain, but that a sensation which should have been completely unfamiliar felt so terribly familiar.

*What are these memories…?*

His chest throbbed, and his head pounded.

As the black knight staggered under the relentless barrage of attacks, memories belonging to someone whose identity he could not possibly determine flashed rapidly before his eyes.

*This, this can’t be!*

“His mana adaptability is incredible. It’s the highest figure we’ve ever recorded!”

“He needs to be placed in the Zhonghua Development Training program immediately!”

Humans in dazzling white clothes chattered in excited voices. Standing among them was a middle-aged man dressed in a dark, angular uniform.

“Zhonghua Development Training? Are you saying you intend to raise that child as a Hunter?”

“Of course. He’s only thirteen years old, yet his mana adaptability is comparable to Faye Chen’s. He has more than enough potential to become an S-rank Hunter—the best Hunter in the country!”

“I refuse.”

“Pardon me?”

“No, Comrade Lieutenant General. What do you mean? This child…”

“Enough.”

The middle-aged man continued in a subdued voice.

“He is my only nephew. I promised my sister that I would make the boy happy, not turn him into a Hunter and put him in danger.”

“Being a Hunter is a noble profession. If that child becomes an S-rank Hunter, he will be a blessing to the entire people!”

“I know how noble the work they do is. But that is how my brother-in-law also…”

The middle-aged man suddenly stopped and shook his head.

“No matter what you say, I will not change my mind. If there had been no directive from above, I would not even have had him tested. We will be leaving now, so handle the rest yourselves.”

“Comrade Lieutenant General! Comrade Lieutenant General!”

Leaving the shouts echoing behind him, the middle-aged man strode over with a forced smile and held out his hand.

“You’ve been waiting long, haven’t you? Come on, let’s go.”

The black knight—or rather, the man who seemed to be the owner of these memories—grasped the middle-aged man’s hand.

A small, pale hand.

Then a clear child’s voice rang out.

“Uncle.”

“Yes?”

“I… I want to become a Hunter.”

A complicated array of emotions crossed the middle-aged man’s face.

After staring at the child while biting his lip for a long time, he let out a worried sigh. Then the humans whose expressions had brightened considerably approached him.

“Zhonghua Development Training is a project we developed with painstaking care. Its safety measures are thorough, and its effectiveness is proven. Wu Heixing, who is the same age, is doing well too.”

“If the child changes his mind, we will stop the training at any time.”

The oldest-looking man placed a hand on the middle-aged man’s shoulder.

“Please trust us and leave him in our care, Comrade Lieutenant General Wei Fenghu.”

Wei Fenghu. Wei Fenghu…

The name echoed endlessly through the black knight’s mind. A name that felt so familiar, and so dearly missed.

Boom!

Was the throbbing in his chest caused by the attack he had taken, or was there another reason?

As the staggering black knight stared ahead, more memories appeared before his eyes.

“You think you’re the best just because the adults praise you?”

A boy in a bow tie and black suit glared at him with sharp eyes. His polished shoes gleamed.

“Don’t get confused. I’m the best. You’re second!”

The black knight’s vision tilted to one side, and then an innocent voice rang out.

“Okay. Let’s do that, then.”

“What?”

“I like being second, too. Third is fine, and I don’t care if I come in last.”

The sharp-featured boy’s mouth fell open.

“Are you stupid? Do you want to become worse than Zhang Wei, the last-place trainee at the training camp?”

“But Zhang Wei is kind and helps other people, too. He’ll become a great Hunter.”

“Y-You’re making fun of me right now, aren’t you?”

“Huh? No. I just… whatever you want is fine with me—ah!”

Crash!

Subduing the boy who suddenly lunged at him took only an instant. The boy pinned beneath him struggled and shouted.

“I’m the best! Wu Heixing is the best at everything!”

When one memory disappeared, another appeared in its place, as though someone were tossing stones one after another into a still pond.

The memories of that unknown person continued to throw the black knight’s mind into confusion.

“Top trainee, ■■■■, step forward.”

A small number of people filled a vast space.

For some reason, he could not hear the name being called clearly, but his body moved on its own.

Step. Step.

His disciplined stride was long, and his field of view was high.

By then, he had grown into a young man. An older man in uniform approached and pinned a medal to his chest.

It was a familiar face. The same man he had seen in the first memory whispered quietly.

“Will you not regret this?”

“I have no regrets. I did not regret it before, and I never will.”

“Most people will not know that you exist. You may have to live your entire life like a shadow.”

“I was taught that another name for a Hunter is a guardian. My honor does not disappear simply because I remain unseen.”

“There is something I have not been able to tell you until now.”

The older man’s hand tightened around his shoulder.

“I’m proud of you. Thank you for growing up so well.”

“Thank you, Uncle. No… Father.”

The older man’s eyes grew damp beneath his bright smile.

At the moment a single tear slid down his wrinkled cheek and fell onto the platform, another memory surfaced.

“Hello? Is anyone there?”

On a warm spring day, the place he visited was a small flower shop. As he looked around at the bright flowers and peered inside, she approached him.

“Welcome!”

She walked with a buoyant step, and her eyes had the prim, coy look of a cat.

Her voice was so lively and bright. And so beautiful…

The black knight—or rather, a man who had passed through his youthful years and grown more mature—felt his heart pound.

“Are you a customer?”

“No, I, um… I came to buy some fl-flowers.”

“For your parents? Or your girlfriend?”

“My parents. Strictly speaking, they aren’t my parents. It’s my uncle who raised me…”

“I see. But you speak very stiffly. Are you a soldier?”

“S-Something like that, ma’am.”

It was a strange memory. His words kept breaking off, and everything before his eyes repeatedly turned white.

When he came to his senses, he was walking dazedly into a hospital room with a bright bouquet of flowers in his arms.

“You fool. I told you there was no need to come when it was only mild pneumonia… What’s that?”

At Wei Fenghu’s question, he answered in a dazed voice.

“Flowers.”

“Is that a get-well gift?”

“Yes.”

“So you bought chrysanthemums as a get-well gift for me?”

“Yes… Huh?”

“You ungrateful brat! Hey, you!”

Smack! Smack!

The man laughed even as he was beaten with the bouquet. A quiet laugh escaped him at his own stupidity, and he could not help laughing because she reminded him of chrysanthemums.

After that, the memories began to flow rapidly. He visited the flower shop every day.

“Ah, h-hello!”

“Welcome—oh my, you’re back again?”

“Haha.”

“Chrysanthemums, right? The pure white ones.”

Spring, summer, autumn, winter.

By the time four seasons had passed, the relationship between the two was no longer that of a flower-shop owner and her customer.

“I have something to say.”

“What is it?”

“Will you marry me?”

“…Ah.”

“I’ll make you happy.”

That was the longest of all the memories so far.

After a silence so long that a single second felt like ten years, or even a hundred, she finally opened her mouth.

“I have something to say, too.”

“No, before that, let me hear your answer…”

“I’m pregnant.”

“What?”

Thump. Thump-thump. Thump-thump-thump!

The man’s heart pounded violently, and the black knight writhed in pain.

“Ahhh! Aaaah!”

His head hurt as if it were splitting apart, and it felt as though someone were wringing out his insides with their hands.

Along with pain he had never even imagined, another memory forced its way into the empty space.

“Waaah! Waaah!”

“T-This child…”

“Congratulations on becoming a father, honey.”

The birth of a new life.

And its growth.

“Dada. Dada-da!”

“Honey, honey! Did you hear that? Our baby’s already saying ‘Dada.’ Could our baby be a genius?”

“Could you change the diaper?”

“Wait a moment. Let me hear it one more time.”

“Dada, Momma!”

“Hahaha! That’s right! We’re your daddy and mommy!”

The day the baby, bundled in a swaddling cloth and squirming helplessly, succeeded in rolling over.

The day he first crawled on all fours, and the day he first walked…

The man was happy as if he had gained the entire world.

But it did not take long for those dreamlike days to turn into a nightmare.

“The mana level in Gaoping District has spiked!”

“Gaoping District? Keep trying to contact them, and mobilize and deploy the Second Regiment as a precaution.”

“D-Director, we’ve lost communications.”

“What?”

A disaster that struck without warning.

The man hurriedly assembled the forces under his command and headed for the source of the problem. There, he encountered a sight he could not believe.

“Kyawwwww!”

“E-Everyone, run… Ghk!”

Slash! KABOOM!

Flames rose into the sky above the peaceful city, while countless monsters slaughtered the humans on the ground.

In that land overflowing with screams and death, the man drew his sword before the unbelievable scene of carnage.

“Public Security Armed Forces Department!”

Zzt!

An aura blade rose around the blade, shining brilliantly.

More than a thousand Hunters answered the man’s cry with a resonant roar.

They were humanity’s shield and guardians. They could not retreat even a single step.

“Wipe them all out!”

“Long live the People’s Republic of China!”

With the Five-Starred Red Flag engraved on their armor, they advanced like a wave. Soon, instead of white foam, they broke apart in a spray of blood.

“Perish in the flames of hellfire, Fire Rain.”

Kiiiiing.

The ash-gray sky opened its maw.

Beneath the rain of falling flames, the man thought of his beloved wife and his five-year-old daughter.

And then he came face-to-face with *that being*.

“If you had run, you could have lived.”

“I’ll kill you.”

“How noble. What is your name, human?”

“I am…”

* * *

“…Lei Fei?”

At the sound of Jin Taekyung’s voice in his ear, the black knight’s body abruptly went rigid.

As a dam finally gave way, everything began to reassemble.

Thirty-six years of memories from his life as a human poured out like a tidal wave, obscuring his vision.

—I am, I am…

What in the world was he?

As the black knight trembled in confusion and pain, a thunderous voice rang out in his mind.

—You are my most loyal servant and the supreme commander of my legion. Your lord commands you: fulfill your duty until you crumble and wither into ash!

—……!

It was an irresistible word-spell.[^1]

The red eye-light that had been wavering like a candle before the wind flared fiercely.

The black knight—or rather, Lei Fei—who had fallen with one strike still remaining, now erupted with tremendous mana from his entire body.

KRAAAAAASH!

[^1]: A command imbued with supernatural power.
## Chapter artifact 401

# Chapter 401

A single word, almost a groan, slipped between my lips.

“……Lei Fei?”

Wei Fenghu’s only nephew through his sister, and an S-rank Hunter secretly raised by China.

And on the day the Monster Wave erupted, a hero who had vanished along with a thousand Hunters from the Public Security Armed Forces Department.

*If you happen to meet that child, Mr. Jin…would you be able to bring him back?*

The desperate request from the old general echoed in my ears.

That was probably why my body suddenly locked up.

—You treacherous human! Get a grip! He is no longer human. He is a fallen monster!

The Skeleton Warlord’s cry stated an obvious fact.

Among the monsters I had defeated so far, there had been Hunters and civilians resurrected as undead. Lei Fei was merely one of them.

The being before me was no longer an S-rank Hunter who had died while carrying out his mission.

He was a Death Knight Lord leading a monster army.

But……

*Something’s different.*

Crack, crack, crack!

—Kgh, k-khgh. Kraaah!

His body trembled in small spasms, and groans escaped him at irregular intervals.

Each time the red glow in his eyes blinked like a traffic light, stark-white eyes and pupils appeared beneath it—unmistakably human.

I had never heard of or seen an undead that moved solely on the instinct to slaughter, having lost its senses and reason, react this way.

*What if—just maybe—his transformation into an undead hasn’t been completed?*

If that was true……what was I supposed to do?

Right now, a single blow would end the battle and allow me to console the souls of the victims.

But what would I be killing? A hero who had given his life to protect people, or a Death Knight Lord who had led a monster army and carried out countless massacres and acts of destruction?

“Fuck……”

My hesitation was brief.

There was no helping it. The die had been cast, and he and I had already crossed a river from which there was no return. If my opponent could not be subdued halfheartedly, I had to end it now.

*Rest easy.*

Lei Fei, Death Knight Lord—whoever he was, he would be able to find peace now.

My Flame-Extinguishing Divine Fist, mastered to eight-tenths and unleashed at full power, would finish him without pain.

Fwoosh! Whoooooosh!

And just as my fist, engulfed in blue flames, advanced to bring everything to an end—

—My. Lord!

A chilling voice slipped between lips stained dark red. At the same time, the red glow in his eyes sharpened, and solidified mana surged upward.

Crack! KRAAAANG!

Flames and darkness collided.

The two tremendous forces crashed into each other and exploded with an enormous shock wave.

Rumble, rumble, rumble!

The deafening boom left my ears ringing. Flung backward by the tremendous recoil, I twisted my body in midair and regained my balance.

The ground and monster remains caught in the explosion had been blown to pieces.

Through the pale smoke that had overturned everything within a radius of several hundred meters, a being wrapped in darkness approached.

—I am that person’s most loyal servant.

Sssssss.

Darkness rose from the devastated earth.

It was the death energy held by the dead monsters.

—I am the supreme commander who leads the legion of the dead.

Whoooooosh!

The swirling darkness was sucked toward the being. At the same time, his half-destroyed armor was restored, his broken bones joined together, and the red glow in his eyes flared fiercely.

Recovery followed by an increase in strength.

The being, now holding even greater mana within him, slowly raised his sword.

—By my lord’s command, I shall fulfill my duty.

He was wrong.

His duty had been to serve as humanity’s shield and guardian, but the hero who had given his life for others had lost his memories and been corrupted by the Arch Lich.

> **System**
>
> Lv. 140 Death Knight Lord

Lei Fei no longer existed.

The being approaching me was nothing but a monster.

If so……

“I have a duty to fulfill as well.”

The moment I murmured those words, a sword scattering mana fell from above my head.

* * *

Slash!

A single handspan.

That was how far death had missed me.

Mana sharpened more keenly than ever grazed my arm and cut into the ground. Without any deafening boom or flying fragments, more than ten meters of earth split apart like a cheesecake.

Slice!

Hearing the chilling sound of something being cut, I thrust out my hand.

The ultra-high heat contained in the Flame Divine Palm collided with the sword blade, which had already changed direction.

KRAANG!

A tremendous shock wave exploded around us with a deafening boom.

Through the drifting dust, I saw the burning red glow of his eyes.

“Eat this.”

—……!

The Flame-Extinguishing Divine Fist shot forward like a cannon shell.

The bastard’s eyes flew wide as he drove his knee upward. My fist engulfed in flame and his knee wrapped in darkness collided.

KRAAANG!

The world shook.

The tremendous recoil flung me backward, and the outer wall of a building rushed closer into my field of vision.

I twisted my body in midair. The tips of my feet touched solid concrete.

*Flamefire Path.*

I sent internal energy flowing into both legs.

Concentration of energy.

Then an explosion.

Crack. Boom!

The outer wall received all the force and speed loaded into my toes and burst apart.

I shot forward like a streak of flame, appearing in the air above the head of the Death Knight Lord, who was only just recovering his stance.

*Inventory open. Summon.*

A sturdy spear shaft appeared in my hand. The energy filling my entire body surged through my fingertips and into the spearhead.

Blue hellfire bloomed in midair, became the claw of a fire dragon, and slashed downward.

The second form of the Fire Dragon Divine Spear.

*Heavenly Strike.*

Whoooooooom—

Ultra-high heat burned the air.

The Death Knight Lord, swelling his mana as if detonating it, raised his sword toward the spear that plunged down like a bolt of lightning.

KRAANG!

The spearhead shattered, and a blue-black flash filled my vision.

Cracks spread like a spiderweb around the bastard, who had taken the full force carried by the spearhead. The next moment, the ground within a radius of more than a hundred meters sank inward.

Rumble, rumble, rumble!

A gigantic sinkhole finally revealed itself amid the collapse.

Monsters swept up in the aftermath of the battle let out shrieks as they fell hundreds of meters below.

The Death Knight Lord stepped on a falling ogre and shot back up to the surface. Then he raised his head and looked at me.

At me, standing tall in the sky.

*Stepping on Empty Air.*

Another supernatural ability permitted only to those who had reached the Supreme Peak realm.

I felt the immense drain on my internal energy as I stepped on empty air and leaped upward. Before my feet could even touch the ground, mana lashed out like a whip toward my side.

*Inventory open. Summon.*

Clang!

I succeeded in blocking the attack, but the price was the spearhead, which shattered into countless pieces.

White Flame had already been hurled away as a javelin. Even if the weapons stored in my inventory were of usable quality, in a battle like this they were nothing more than disposable weapons.

But if I had dozens or hundreds of disposable weapons, that changed things.

*Inventory open. Summon.*

Whoooooosh! Clang!

*Summon.*

Crack!

With every exchange of blows, a spear shaft bent and a spearhead broke.

But I paid no attention.

The senses throughout my body, quieter and sharper than ever, told me what was happening now and what movement would come next.

*Summon. Summon.*

I crossed and swung the spears in both hands like rays of light.

Crack!

One was destroyed when it collided with his sword, but the other slammed into his side.

Boom!

I stepped toward the body driven backward by the earth-shaking boom.

A single step.

I stood before the Death Knight Lord. I moved faster than he could retreat.

The first form of the Blazing Flame Divine Spear.

*Fire Dragon’s Single Tail.*

Whoooooosh! Thrust!

A new spear, already drawn from my inventory, pierced the pitch-black armor and drove into the area around his knee.

His armor had been restored even more solidly than before, but the mana it had absorbed still could not stop the Force contained in the spearhead.

*He can’t feel pain, but he should still feel the impact.*

Contrary to my expectations, however, the Death Knight Lord did not waver.

Slice!

The bastard severed the spear with his mana-coated sword. Instead of retreating, he charged toward me.

Slash!

Space split open, and every hair on my body stood on end.

I thought I had turned my head in time, but a thread-thin stream of mana grazed the underside of my earlobe, slicing into it.

Ssshhh!

Blood gushed from the earlobe, nearly severed in half, accompanied by a sharp, stinging pain.

Feeling the blood run down and wet my neck, I thrust a palm toward his face.

Just as the Flame Divine Palm was about to erupt with a burst of rising flames—

KRAANG!

Amid the ringing boom, my eyes widened.

The palm that should have blown his head away was blocked by a pitch-black gauntlet.

*What the hell?*

I was not surprised because the attack had been blocked.

The movement the Death Knight Lord had just shown was still clumsy, but it was a type of palm technique I recognized.

And it had taken the form of the Flame Divine Palm.

*This bastard……he’s copying my martial arts.*

As I faced the unwavering red glow of his burning eyes, a thought suddenly flashed through my mind.

*An S-rank Hunter secretly raised by China.*

I had forgotten for a moment.

The being before me, who had now been reduced to a monster, was a genius chosen from among 1.2 billion people—and a secret weapon China had wanted to conceal until the very end.

*Impressive. Truly impressive.*

I admired him inwardly.

At the same time, I became certain of one thing.

*You can’t beat me.*

If he was the man chosen from among 1.2 billion people, then I was the sole existence among nearly seven billion human beings.

The blood I had spilled while moving between the modern world and Murim, and the countless times I had crossed the line of death, had made me who I was now.

“Let’s……end this.”

I took a step with a quiet murmur.

My mind was calmer than ever, and my five senses were razor-sharp.

Pfft!

I twisted my head, and the mana the Death Knight Lord had unleashed in an explosive burst narrowly passed by.

Feeling the Scorching Yang Qi filling my entire body, I thrust out a fist.

KRAANG!

His body shook with an earth-shattering boom.

He hurriedly imitated a grappling technique to block the attack, but the Flame-Extinguishing Divine Fist broke through his clumsy defense and slammed into his chest.

*More.*

Whoosh, boom!

*More. More. More.*

I muttered the words inwardly as I thrust out my hands and feet without pause.

Every blow loaded with Force collided with his sword, slipped into openings, and battered him without end.

It was not only the spears summoned from my inventory.

My fists, legs, elbows—everything that made up my body was both a weapon and a shield.

Crack! Slice!

When his wrist was severed together with the gauntlet, the powerful mana flickered like a candle flame.

The Death Knight Lord’s armor was slowly coming apart, unable to withstand physical abilities that far surpassed the limits of humanity and internal energy as vast as the sea.

KRAANG!

We exchanged a blow without bothering to defend ourselves.

A System notification informed me that the Fire Dragon Armor’s durability had fallen, while the armor covering his entire body shattered like glass.

Thud, thud, thud.

His bare body was finally revealed.

His pale skin was dotted with patches of lividity.

The red glow in the eyes set within the dead man’s body flared more fiercely than ever, as if announcing the end.

—I am, I am……!

But his cry did not continue.

Thrust!

A transparent spearhead pierced through his pale skin and burst out from his chest.

I used Seizing an Object Through Empty Space to pull White Flame back, then looked at him and answered.

“That’s enough……rest now.”
## Chapter artifact 402

# Chapter 402

Thrust!

*What is this?*

It was hot, yet cool.

Sensing those two contradictory sensations, the black knight looked down at the transparent spearhead protruding through his chest.

He slowly raised his head. His gaze met that of a young human wearing an unreadable expression.

“Enough now…… rest.”

The emotion in the voice was neither mockery toward a defeated opponent nor the joy of a victor. It was bitter—and, in a way, wistful.

That one sentence filled the black knight’s mind.

*Rest.*

And then, in the next moment—

Crack!

The black knight heard the sound of everything binding him shattering apart.

The jet-black armor that had barely maintained its shape broke into hundreds, thousands of fragments, and the mighty mana within him staggered.

But the greatest change was taking place inside his mind.

*That’s……*

In a world that had slowed to a crawl, he saw a small, worn child’s shoe through the fragments of armor scattering around him.

At the same time, countless memories flashed through his mind.

*“I want to become a Hunter.”*

A young boy speaking of his dream.

*“I’m proud of you. Thank you for growing up so well.”*

*“Thank you, Uncle. No…… Father.”*

A young man who had become both a proud nephew and a son.

*“Is anyone there?”*

*“Welcome!”*

*……Ah.*

On a day when everything had been perfect—the scent, the temperature, the weather—a man met a woman and fell in love.

*“Will you marry me?”*

The young boy who had wanted to become a Hunter became someone’s husband.

*“Waaah, waaah!”*

*“T-This child……”*

*“Congratulations on becoming a father, honey.”*

At last, he became the father of a child.

*“Dada, Momma!”*

*“Hahaha! That’s right! We’re your daddy and mommy!”*

How could he ever forget those moments, when he had been happier than anyone else in the world?

A single tear rolled down his bloodless, pale cheek.

It was a tear that wiped away the dark clouds filling his mind. The tear of a dead man who had finally remembered himself.

*Ah…… ahhh……*

Only now did he know. Only now did he understand.

He reached out and grabbed the small shoe.

The unknown child crying in its parents’ arms overlapped with the image of his daughter, smiling brightly as she saw him off on the morning he died.

*“Daddy! Come back soon!”*

*“Have a safe trip. Be careful.”*

He thought he had kissed his wife on the forehead and rubbed his face against his daughter’s cheek. He had hugged his daughter as she laughed and complained that his beard was scratchy, then left through the front door.

Leaving behind the same words he always did.

*“I’ll be back.”*

But that promise was never kept.

A few hours later, a disaster unlike any seen since the Great Cataclysm began, and he fought with every ounce of strength he possessed. At last, he encountered a certain being.

*“How noble. Human, what is your name?”*

*“I am……”*

The red glow burning in his eyes faded as if it had been washed away.

The man with cloudy, gray-white eyes was no longer the black knight, nor the Death Knight Lord.

*“Lei Fei. That is my name.”*

Freed from his long darkness, he raised his head.

The glow of the setting sun shining through the clouds cast a reddish hue over his pale skin.

* * *

The System notification rang out at the exact moment I reached out to deliver the final blow.

Ding.

> **System**
>
> - Information about the target has changed.
> - The changed information is displayed through **Qi Sense**.
>
> **Lv. 120 Lei Fei**

“……!”

My movement abruptly stopped at the unexpected development.

The gray-white eyes of the Death Knight Lord—or rather, Lei Fei—who had been staring up at the sky slowly turned toward me. The voice escaping between his lips was hollow and lonely.

“It feels like I’ve just had a terrible nightmare. No, I almost wish it had been a nightmare.”

I had never heard of or seen anything like this before. I stared at him in silence for a moment, then opened my mouth.

“Have you come back to your senses?”

“Yes. Only now, at last.”

Lei Fei looked down at his own hands. They were pale and rotten. Some of his flesh and bone had fallen away during his fierce exchange with me.

And they were soaked in red blood. Human blood.

“What have I done?”

The man who had once thrown away his life for humanity had become the commander of a monster army and slaughtered humans.

I could not even begin to imagine how he felt after realizing that terrible truth.

“Lei Fei.”

I wanted to tell him. *It wasn’t your will. It happened because the Arch Lich’s magic had seized control of your mind.*

But Lei Fei shook his head.

“You don’t have to say it. I already know what you’re trying to tell me. But……”

Lei Fei gestured toward his own body and continued.

“I don’t think I have much time left.”

Everything he said was true. The sturdy body of the undead, which neither steel nor bullets could pierce, was slowly—very slowly—falling apart.

And, paradoxically, what was sustaining Lei Fei now was the mana that still remained within his body.

“It’s ridiculous. I became an undead and killed humans, yet I’m clinging to existence with that very power.”

After muttering hollowly, he spoke to me.

“May I ask one favor?”

“……Please, go ahead.”

I thought Lei Fei wanted to disappear. I assumed he wished to find rest and escape from everything that had caused him pain.

But the words that slipped from his lips in the next moment were completely different from what I expected.

“Help me fulfill my mission.”

“……!”

“I swore an oath on the day I became a Hunter. I swore that I would fight monsters until the moment my life ended. That oath is still valid.”

Lei Fei had already fulfilled his mission. He had charged forward bravely and shattered magnificently.

The one who had fought humanity after becoming a Death Knight Lord had been acting on the Arch Lich’s will, not his own.

And yet, even now, he wanted to fight again. Though his life had already ended, he stood tall once more, reaffirming his mission.

That was why I could not help asking.

“Why? Why go this far?”

At my question, Lei Fei smiled faintly.

“What a foolish question.”

“What?”

“Why did you come running here alone, even though countless monsters and dangers were waiting for you? And why am I trying to fight until the very end? What’s the difference?”

“……!”

“You already know the answer. That is all.”

I knew the answer.

The moment I heard those words, a shiver ran down my spine.

Lei Fei looked at me, unable to speak, then raised his hand and gestured around us.

The countless monster troops that still remained were reflected in his eyes, which had already lost the light of life.

“This…… will be my final battle.”

Schlk!

Lei Fei pulled White Flame from his own chest and handed it to me, then raised his sword.

Instead of the dazzling aura blade symbolizing an S-rank Hunter, ominous dark mana coiled around the blade and surged upward.

But the one wielding that power was not the Death Knight Lord.

It was a Hunter burning through his final mission.

“I’d like to fight together. But will they allow me?”

Anyone who heard those words without knowing the circumstances would have dismissed them as random nonsense.

But I understood Lei Fei. Angling the spearhead of White Flame downward, I answered.

“They’ll be happy. If they’re the people I know.”

“……You think the same way I do.”

A red light flickered in Lei Fei’s gray-white eyes.

The mana he had dragged forth with all his strength seeped across the battlefield. Then a thunderous cry burst from his lips.

“Public Security Armed Forces Department—!”

And in the next moment—

Rustle. Rattle, rattle.

At the call of the Death Knight Lord—or rather, the head of the Public Security Armed Forces Department—the hundreds of Hunters who had fallen across the battlefield rose to their feet. They had returned from death as undead, and now they gripped their weapons and gathered in one place.

At their apex stood Lei Fei and me.

“You take the lead. The living must finish this fight.”

As if bewitched, I stepped forward.

The monster army, which had been thrown into confusion by the unexpected turn of events, finally gathered together, spewing hostile cries.

Toward the commander who had now become their enemy.

And toward me, standing at the front.

Step. Step.

I walked slowly but firmly.

Tap. Tap-tap.

Then I gradually picked up speed.

Lei Fei and the hundreds of Public Security Armed Forces Department Hunters resurrected as undead followed behind me.

It did not take long for the ripples spreading across the water to become waves and crash over them.

And at the entrance to what would be our final battle, Lei Fei shouted at the top of his lungs.

“Wipe them all out!”

That was the cry that had echoed through the footage.

On their battered, filthy armor, the Five-Starred Red Flag—their symbol and pride—shone in the glow of the setting sun.

Clutching my throbbing chest, I shot toward the monsters like a ray of light.

Whoooooosh! KRA-DOOM!

* * *

Crunch!

How many had I brought down by now?

Hundreds? A thousand?

Slash! Boom!

I had no idea. Like someone possessed, I kept moving forward. I smashed, cut, stabbed, and blew apart everything that stood in my way.

Whoooooosh!

—Kuaaaargh!

—Kraaah!

Blue hellfire surged upward like pillars, and monsters engulfed in flames that would not go out screamed.

Then, when nothing could be heard anymore, I suddenly stopped where I stood.

“Hah, huff.”

I was out of breath. My mouth felt rough and dry, as if I had chewed and swallowed a handful of sand.

Feeling the fatigue I had momentarily forgotten come crashing back over me, I looked around.

Across the wide expanse of land, there were no monsters left standing.

Not the ogres and Trolls that had spewed their hostile cries, nor the Wyverns and Gargoyles that had circled through the air.

And……

Thud. Collapse!

Not even the Public Security Armed Forces Department Hunters who had been resurrected as undead.

Having fulfilled their final mission, they fell one after another like puppets whose strings had been cut.

As I stared at them with indescribable emotions, I realized what their collapse meant.

“……Lei Fei!”

He was sitting in the middle of the silent battlefield. One arm had been severed, and his side had been torn open, yet he waited for me with a peaceful expression.

“You came at just the right time.”

I did not know why, but that insignificant sentence made something surge up inside my chest.

I had not known him for ten years, yet a curse slipped from my lips before I could stop it.

“Damn it……”

“Don’t swear so much. I saw you on television, and it seems to be a habit. Women won’t like that, and it’s not good for children’s education.”

Lei Fei gave a quiet laugh as he spoke. He already knew who I was.

“Is that really the problem right now? There has to be some way……”

—There is no such way, you treacherous human.

The owner of the voice, much deeper and more subdued than usual, was the Skeleton Warlord.

Lei Fei looked at him with wide eyes.

“A monster?”

—I am the commander. You are a foolish but somewhat remarkable human.

“You are a monster, then. I have no idea what’s going on, but…… yes, if you’re Jin Taekyung, I’m sure you’ll handle it somehow.”

Lei Fei nodded, then raised his head toward the sky. His slowly blinking gray-white eyes reflected a sky stained entirely red.

“Could you pass along one message?”

I did not ask the foolish question of *to whom?* I already knew who he meant.

“Tell them I love them. And tell them I’m sorry I couldn’t return.”

It was the final message a dead man left for his family.

Feeling my chest churn, I answered.

“……I will.”

“Thank you. You’re a good person.”

Lei Fei smiled faintly and tapped my shoulder with his one remaining hand.

With a dry, crumbling sound, his fingers broke apart into dust. Soon, his arm, his leg, his chest……

At the very end, a single sentence slipped between his lips.

“Go west. End this war.”

Whoooooosh.

The wind blew. The hero who had turned into a handful of dust scattered through the air.

I stared blankly at the sight. Then I saw dozens of aircraft flying toward us in formation.
## Chapter artifact 403

# Chapter 403

The twenty-some military transport aircraft and their fighter escorts had trouble landing from the moment they arrived.

“W-What the……”

“We can’t find a place to land!”

Below them lay a small city that had been reduced entirely to ruins.

The buildings packed tightly together had collapsed like dominoes, and flames rose from here and there.

But what frightened the pilots more than anything was the horrific sight visible even from high above.

Schoolyards, convenience stores, government offices……

In that place, where peaceful daily life had vanished, mountains of corpses and rivers of red blood filled every empty space.

A hellscape painted by the monster army.

As the pilots trembled with indescribable terror while looking down at the lifeless ground, a voice rang out.

“Land.”

“C-Commander-in-Chief, but……”

“Not ‘but.’ You must land. That is an order.”

When the pilot met the hardened face of the middle-aged man who had spoken in a heavy voice, he realized he had no choice.

He was a soldier, and the man before him was the de facto commander-in-chief directing this war.

Disobeying the order of General Wei Fenghu, the Minister of National Defense under the Central Military Commission and Chairman Xiao’s most trusted subordinate, would have been insane.

Then Wei Fenghu spoke again, and the pilot thought that disobeying the order might actually be less insane.

“Go to the general hospital the Western Front has been using as its temporary headquarters.”

“What? But that place……”

“According to the last communication we received, that is where the fiercest battle took place. Perhaps it is still going on.”

“……”

“I know that as well as you do. We may already be too late. But we have to go. If even one person is still alive, we must help them and fight alongside them.”

Wei Fenghu continued, his gaze sunk deep.

“Take the controls. And land first.”

It was extraordinary enough that the commander-in-chief had come all the way here himself. But ordering them to attempt the first landing was something else entirely. Considering that monsters might still remain, it was a decision accompanied by tremendous danger.

*Damn it.*

The pilot squeezed his eyes shut and turned on the radio. Soon, his trembling voice began to spread through the communications network to every aircraft.

“VIP-777 issuing orders to all aircraft. I repeat, orders to all aircraft……”

As he listened to his orders being relayed, Wei Fenghu slowly drew a deep breath.

The parachute equipment he had put on in case of an emergency felt as heavy as a thousand-pound boulder.

*Is this because it’s been more than thirty years since I last saw real combat? I’m trembling.*

And Wei Fenghu was not the only one feeling that way.

All four thousand Hunters aboard the twenty-some military transports carried fears large and small.

Some probably wanted to run away right then and there. Others were suppressing their fear and desperately trying to fan their fighting spirit.

No one knew who would die in the battle that was about to begin. Wei Fenghu was no exception, and the reason the commander-in-chief had come to the battlefield despite the danger was the morale of his soldiers.

*A commander has no right to drive only his subordinates into a place of death.*

That had been Wei Fenghu’s lifelong principle, and his nephew through his sister—who was like a biological son to him—Lei Fei had respected him for it.

At the sudden memory of a beloved face passing before his eyes, a corner of the old general’s heart ached.

“I miss you.”

Wei Fenghu murmured quietly.

It had already been fifteen days since Lei Fei had gone missing. But he had not let go of hope. Neither had Lei Fei’s wife and daughter, who had been moved to a safe place.

*Today, I saw someone who reminded me of you.*

A young man who was still only in his twenties. He had achieved an incredible military feat in a distant foreign land, and when he heard that the Western Front was in danger, he had left without hesitation.

He had even laughed while attempting a teleport with a survival rate of only ten percent.

*“Ten percent sounds pretty good.”*

*“It’s probably a thousand times more likely than crossing dimensions.”*

When Magic Johnson relayed that news to him, Wei Fenghu had immediately mobilized the headquarters’ forces and organized the squadron.

He had been struck by the courage shown by a young foreigner named Jin Taekyung, and seeing him had reminded Wei Fenghu of his missing nephew.

*You would have done the same, wouldn’t you?*

Just as Wei Fenghu’s lips curved into a faint smile after asking the silent question, a cry rang out.

“H-How can this be……”

“C-Commander-in-Chief!”

Wei Fenghu raised his head at the pilots’ urgent shouts and looked out the window.

The ground was gradually drawing closer. Across it lay a sea of corpses and blood more horrific than any battlefield he had ever witnessed.

Corpses and blood, blood and corpses……

The general hospital serving as the Western Front’s temporary headquarters had collapsed miserably, exposing its ugly steel framework. A gigantic sinkhole, gaping open like the entrance to hell, and dozens of craters carved into the ground were filled with red and green blood.

There were more monster and human corpses than anyone could count, sprawled together in tangled heaps.

Thousands?

No, well over ten thousand.

“My God……”

“W-Who did this?”

A land of death, raked by disaster.

The pilots, speechless as they stared at the devastated ground, abruptly came to their senses when Wei Fenghu shouted.

“Lower our altitude! Quickly!”

“Yes, sir!”

The threat from the monsters had vanished, but they could not afford to let their guard down.

The pilot maneuvered the aircraft more carefully than ever and attempted to land with his entire body drenched in cold sweat.

Krrrrrrk, boom!

The aircraft shuddered violently several times. At last, when the transport successfully landed, the first person to step out was none other than Wei Fenghu.

Rapid footsteps followed.

The two hundred Hunters aboard the transport quickly set foot on the ground behind him.

Their reactions split into two kinds.

“This is fucking insane……”

Shock at a sight beyond anything they could have imagined.

“Urk, urrrrgh!”

Nausea at the stench of blood filling the surroundings and the dismembered corpses.

At the same time, one question filled every mind.

*Who did this?*

They had even forgotten that they needed to search for survivors. Wei Fenghu and everyone else stood frozen like stone statues.

Then—

Splash. Splash.

Footsteps echoed across the silent battlefield.

Two hundred pairs of eyes turned toward a single person crossing the battlefield, stepping through the pools of blood covering the ground.

The man was drenched in green blood from head to toe. Wei Fenghu stared at him and muttered as if groaning.

“Mr. Jin……?”

It was definitely him.

Even though he looked no different from a man made entirely of blood, Wei Fenghu recognized him.

Jin Taekyung had survived a teleportation spell with a ten-percent survival rate, overturned the hopeless course of the battle, and lived.

The footsteps that seemed as though they would never stop came to a halt in front of Wei Fenghu.

Splash.

Jin Taekyung brushed back the hair clotted together with the monsters’ sticky blood. After a long silence, he spoke his first words.

“The battle is over. There are… no monsters left alive.”

“……!”

“……!”

His unbelievable statement sent a shudder through everyone present.

According to the last communication sent from the Western Front, the monster army had numbered no fewer than ten thousand.

And that was not all. A Death Knight Lord believed to be one of the Arch Lich’s trusted servants had personally entered the battle, making it the most overwhelming offensive of the five fronts.

By contrast, barely a thousand Hunters had fought against them. The rest of the People’s Liberation Army had been no more useful than scraps of paper.

*Not only did he win that battle—he annihilated a monster army of ten thousand.*

It was a battle that would have been impossible without one person. And at the same time, a victory that had been possible because one person was there.

An S-rank Hunter was said to be a strategic weapon capable of overturning a battlefield in an instant. But since the Great Cataclysm, who had ever accomplished something like this?

The two hundred Hunters looked at the young man before them with reverence.

But Wei Fenghu was different.

The old general stared at Jin Taekyung with grief and fear in his eyes.

No—not at Jin Taekyung himself.

At the sword in his hand.

It was a sword Wei Fenghu knew far too well, and that was why his heart hurt even more.

He knew what the situation meant.

“Did you…… meet him?”

After a brief silence, Jin Taekyung answered.

“He asked me to pass along his love.”

“……!”

“He also said he was sorry.”

Wei Fenghu clenched his teeth to hold back the sob rising from his throat. Through his vision clouding with tears, he heard one final sentence.

“He was the best Hunter I’ve ever seen.”

That was all.

Tears trickled down Wei Fenghu’s wrinkled face.

A breeze blew from somewhere and gently wrapped around him.

* * *

Rank, achievements, whether someone was a Hunter or not—it did not matter.

The fact that he had sacrificed himself for someone else was enough to make him worthy of being called a hero.

That was why Lei Fei would remain in my memories for a long time.

A man who had been resurrected as an undead but died as a human.

A true Hunter and hero who fulfilled his mission to the very end.

The countless others who had died here today were the same.

And so were the two people who had not yet regained consciousness.

*The healer said they wouldn’t wake until they had recovered from all their fatigue.*

I looked at Team Leader Choi and Shao Shen, both lost in a deep sleep, remembering what the healer who had visited earlier had said.

Thanks to the top-grade potion, both of their injuries had healed as if they had never existed. But the fatigue accumulated in their bodies and minds was another matter.

*Even I occasionally pass out, and I level up.*

The two of them had fought bravely to the very end.

They had held on to their weapons even while enduring the pain of having their limbs severed.

“Heroes…… heroes, huh.”

I muttered the word under my breath and looked at the sword lying beside me.

The sword left behind by that very hero. His keepsake.

Wei Fenghu had wept endlessly as he returned the sword to me despite my repeated refusal.

*“He would have wanted you to keep it too, Mr. Jin.”*

*Really, Lei Fei?*

I ran my fingers over the blade as I asked a question that would never receive an answer.

It was an exceptional sword whose chilling edge could be felt simply by looking at it.

*Item appraisal.*

Ding.

> **System**
>
> **Item Window**
>
> **Hero’s Soul**
>
> **Type:** Sword  
> **Grade:** Supreme Peak  
> **Restriction:** Those worthy of being called heroes  
> **Description:** Extremely hard and sharp. The final soul of a noble hero dwells within it, and those who meet its qualifications can draw out even greater power.

*Hero’s Soul?*

It was a fitting name for Lei Fei, but the sword was certainly strange.

The Supreme Peak Grade made sense, considering that it had not suffered even a hairline crack amid such fierce exchanges. But the restriction was unusual from the start.

*Only someone with an upright character can use it?*

Hmm. Why not put it to the test?

Without hesitation, I gripped the hilt and slashed downward through the air.

Whoosh!

Better than I expected.

The weight and balance were just right, and I liked the sharpness that could even cut through the wind. The System notification that came immediately afterward was the icing on the cake.

Ding.

> **System**
>
> - **Hero’s Soul** has recognized you as someone of upright character.
> - **Hero’s Power** has manifested. All stats have increased slightly, and fatigue has been reduced. You may draw out even greater power depending on the situation.

I had no idea what that specific situation was, but apparently this was not it. The increase in my stats was so tiny that I could not feel it at all.

It was like pouring one more bucket of water into a lake.

*Still, it would be perfect for evaluating someone’s character.*

A sword for judging character.

From now on, I planned to test anyone who approached me with Hero’s Soul. If the sword accepted them, I would stay close to them. If not, I’d cut the weeds out by the roots and—snip…

Crackle!

A powerful electric current suddenly ran through my hand, and I dropped the sword.

“What the hell?”

As bewilderment washed over me, a sharp alarm rang out and a System message appeared in the air.

Beep!

> **System**
>
> - You have harbored an evil intention!
> - **Hero’s Soul** has rejected you!
> - The effect of **Hero’s Power** has disappeared!

“……”

Come on. It was just a passing thought.

I looked down at the fallen sword and let out a quiet laugh. For some reason, it suddenly occurred to me that perhaps a little of Lei Fei’s soul had entered it.

Wait. If that was true……

“Are you listening?”

After a brief silence, the Skeleton Warlord, who had been placed inside my inventory, answered.

—……I am.

“I wanted to ask you something.”

—……If that question concerns the ego sword, I will answer no. Only the faintest trace of a soul remains within that sword. The human you have in mind has already ceased to exist.

He usually had a screw loose, but he was still a named monster and commander of the army of the dead.

He had absorbed some of the mana scattered when Lei Fei disappeared and grown even stronger, so there was a good chance his words were true.

That aside……

“Is something wrong?”

—Hmm?

“You’ve seemed gloomy for a while.”

Even after saying it, I wondered whether that made any sense. Why was I asking an undead monster why he seemed gloomy? Weren’t they gloomy by nature?

*That’s the problem—he wasn’t acting like this before.*

But then the Skeleton Warlord suddenly spoke.

—A thought occurred to me.

“What thought?”

—What kind of being was I in the past?

“……!”

—I have no memories at all. Although the human named Lei Fei has ceased to exist, this commander was secretly envious of him. At least he learned who he was.

I had not expected him to be thinking about something like that.

After considering it for a moment, I spoke in a warm voice.

“Then should I make you cease to exist too?”

—……!

“What? You said you were envious.”

—N-No, that’s not what I meant……

The Skeleton Warlord’s frantic excuse did not reach its end.

A knock sounded, followed by a polite voice from beyond the door.

“Mr. Jin. Comrade Minister of State would like to see you.”

It seemed the time had already come.

“Yes. I’ll be right there.”

I took one last look at the two people sleeping soundly, then rose from my seat. As I did, I muttered the words I had not managed to say earlier.

“Well, in my opinion, you were probably a pretty decent guy.”

—……Huh? Were you talking to this commander?

“No. I was just talking to myself.”

—Ahem. Right?

The Skeleton’s voice had been utterly dejected until then, but it brightened.

That was definitely not my imagination.

I let out a quiet laugh and left the room.
## Chapter artifact 404

# Chapter 404

“Phew.”

It was pitch-black outside.

The moment he returned, the young man threw off his equipment and dropped heavily into a seat. As he struggled to catch his breath, a middle-aged man approached and handed him a drink.

“You look exhausted. Drink this.”

The two men had bonded somewhat on the way here over their shared status as Hunters drafted from Shanxi Province.

The young man recognized the familiar face and eyed the can in the middle-aged man’s hand, then muttered dubiously.

“Did this come from the supplies? I don’t think I’ve seen this drink before.”

“It came in as foreign relief supplies. It’s not from our country.”

“Hmm. Do you have anything carbonated?”

“If you don’t want it, never mind.”

The middle-aged man began to withdraw his hand, but the young man quickly grabbed it and spoke with a solemn expression.

“Sir. Have I ever told you that canned ration drinks are my favorite thing in the world?”

“No.”

“Then you’re about to learn.”

“Good. That’s the spirit.”

“I’ll enjoy it.”

Click.

The young man opened the can and took a sip. His expression changed subtly.

But before he could say anything, the middle-aged man asked a question.

“You’re coming back from searching Sector Three, aren’t you?”

“……Urk, yes.”

“It must have been rough.”

The young man answered with a shrug. His bare upper body was drenched in cold sweat that had not yet dried, and green blood had splattered across his cheek.

“Monster blood. Did you get into a fight?”

“No. I was passing by a building when a damn gargoyle corpse fell on me. I guess it had been caught on the roof.”

“That must have caused quite a commotion.”

“Do you really have to ask? The rookies with only a year or two under their belts started vomiting and pissing themselves the moment they were covered in blood.”

“And you?”

“I may not look it, but I’m a seven-year Hunter. I didn’t even blink.”

The middle-aged man’s gaze slowly lowered toward a certain part of the young man’s body. He stared at the slightly stained area of the navy-blue pants, then nodded.

“Hmm. I see.”

“……It’s sweat.”

“I didn’t say anything. But looking at you is making my eyes feel sweaty.”

“……Actually, I did piss a little. Is it obvious?”

“Yes.”

“Damn it.”

The young man swore and tilted back the canned drink. The middle-aged man watched him in silence before abruptly asking a question.

“Did you find any survivors?”

“……!”

“So it was the same on your side.”

The young man’s expression stiffened the instant the words left the man’s mouth. The middle-aged man let out a sigh.

He had already taken part in one search himself.

It had been a truly nightmarish experience.

Everywhere he looked, corpses torn apart by monsters had been piled up, and the horrific stench had made him feel as if his head were splitting open.

The two of them would probably never forget what they had seen that day.

“……I can’t even imagine how fierce the battle must have been.”

“You don’t need to imagine it. Whatever you think it was, it was worse.”

The four thousand Hunters who had come here with Minister of National Defense Wei Fenghu had been divided according to their units and sent to search the small city. Every piece of search equipment they used kept producing the same result.

No survivors.

Everyone except the three thousand members of the People’s Liberation Army who had fled in terror at the beginning of the battle lay cold and dead. No one yet knew how many of the cowardly deserters who had scattered had survived.

“At this rate, we can’t even call it a casualty count. A death toll would be more accurate……”

“Watch what you say. We don’t know that yet.”

“Mm. I’m sorry. I spoke carelessly.”

“If you know that, it’s fine. And……”

The middle-aged man cut off the young man’s thoughtless comment and continued.

“A casualty count is the correct term. There are survivors.”

“……Oh.”

The young man remembered the three people he had momentarily forgotten—the three who had survived this gruesome hell.

“You mean the regimental commander of the Public Security Armed Forces Department? That young fellow?”

“That’s right. The young man from Korea survived too.”

“And then there’s……”

The two people mentioned earlier had certainly shown heroic courage, but compared to the last person, they were no more than fireflies before the sun.

The middle-aged man continued in place of the young man, who swallowed hard.

“Yes, that man. No—that person survived too.”

Unmistakable awe colored his voice. He felt no discomfort calling a young man far younger than himself “that person,” because he knew how great the man’s achievements had been.

“Can you believe it? That one Hunter could be so strong?”

He was a veteran Hunter with years of experience. Because of that, he could at least vaguely imagine what monsters S-rank Hunters truly were.

But Jin Taekyung’s performance had been so incredible that it was difficult to believe it had been the work of a Hunter—or even a human being.

“It was a monster army numbering nearly ten thousand. There were two Death Knights, and even a Death Knight Lord said to be as strong as or stronger than an S-rank Hunter.”

The middle-aged man continued rapidly, his voice filled with excitement.

“And how many allied Hunters were there? Only a thousand. The People’s Liberation Army was there too, but even they……”

“Nearly half of them ran away when the front line collapsed. The rest fought bravely, but the monsters slaughtered them. I heard about it myself.”

“How many Hunters do you think were still alive when Jin Taekyung arrived? A thousand? No, I’d stake my life that fewer than half of them were left!”

If he had witnessed the situation when Jin Taekyung arrived with his own eyes, he might have suffered cardiac arrest from the shock.

Even the middle-aged man, who revered Jin so deeply, had not imagined that Jin Taekyung had faced the monster army alone.

“He led hundreds of exhausted, wounded Hunters and annihilated a monster army more than ten times their size! Do you think that makes any sense?”

The young man looked at him with a thoroughly dubious expression.

“I don’t think it does.”

“Exactly. But that person did it!”

“Uh, sir. Sorry to pour cold water on you, but nothing’s actually been confirmed yet, has it?”

“What?”

“I think Jin Taekyung……”

“Not Jin Taekyung. Mr. Jin!”

The middle-aged man opened his eyes wide and shouted. The young man flinched and cleared his throat.

“Ahem. I mean, I admit that Mr. Jin is an incredible powerhouse, but I can’t help thinking that the story may have been exaggerated a little.”

“Exaggerated? You saw the traces left on the battlefield and you still say that? If it wasn’t Mr. Jin, then who……”

“For goodness’ sake, don’t get so worked up. Look at it a little more calmly. If everything you’re saying is true, then that means Mr. Jin is stronger than Faye Chen or Wu Heixing.”

“I don’t want to rank them, but based on the achievements shown during this monster wave, Mr. Jin is clearly the best. So?”

“Faye Chen may be from Hong Kong, but she’s a hero who accomplished countless great feats during the Great Cataclysm. And even if Wu Heixing causes plenty of trouble, he’s a true genius born from Zhonghua. Jin Taekyung surpassing those two? That’s crossing a line.”

The middle-aged man stared at the young man with a gaze full of disbelief and contempt.

“You’re the one who crossed the line.”

“What?”

“Is that all you have to say? You shout about Zhonghua being number one, then belittle the hero who achieved a great victory and saved the people?”

The young man’s face twisted.

“Since we’re talking about it, Jin Taekyung only saved two people today. No, the other one was Korean, so he only saved one of our people. And that person was perfectly healthy, without a single injury. He fought just to protect the people of his own country. Do you really think he used a top-grade potion?”

“There’s no point talking to you. You can’t even offer praise, and this is how you repay him……”

The middle-aged man shook his head and stood up.

The middle-aged man shook his head and rose from his seat. At that moment, a voice spoke up.

“Maybe he would’ve said you were a fucking asshole who wasn’t worth helping.”

“……!”

“……!”

The two men spun around in shock at the voice that had approached without making a sound.

Standing before them was a face they had grown familiar with through television and the mass media.

“Hic.”

The young man, looking up at a man a full head taller than himself, began to hiccup.

“J-J-J-J-Jin!”

The middle-aged man stuttered like he’d started buffering.

Jin Taekyung looked at the two of them and spoke with a friendly smile.

“You there, young man—stop hiccupping if you don’t want to become a good Chinese person. And you, sir, stop the earthquake—unless you’re planning to use a great one to bring down the Arch Lich.”

“Hic—”

“A-Are you really him?”

Jin Taekyung gave a slight nod.

“I was just passing by, but I heard a particularly irritating sound.”

“……Th-That……”

Jin Taekyung turned toward the young man—the source of the irritating sound, who had stopped hiccupping and begun trembling like a leaf.

“How old are you?”

“I-I’m twenty-nine.”

“You’re older than me. I’ll speak casually.”

“……What?”

“What?”

“N-No, sir.”

Even if Jin Taekyung swore at him instead of merely speaking casually, the young man would have had no grounds to complain.

He had only ever seen Jin Taekyung from a distance or in passing. Now that he realized Jin had heard everything he had said, his hands and feet began to tingle, and his vision went white.

“I-I’m sorry.”

“You don’t have to apologize. That’s how backbiting works. I understand.”

“Th-Thank you.”

Just as Jin Taekyung’s gentle smile began to melt the young man’s heart, he continued.

“There’s nothing to thank me for. Backbiting is fun when you’re tearing someone down, but once you get caught, you’re fucked.”

“……!”

“There should be someone behind me right now. Do you see him?”

The young man slowly—very slowly—shifted his eyes.

Sure enough, more than ten meters away, a middle-aged man with the face of a demon was glaring at him, radiating a terrifying aura.

“They say he’s an A-rank Hunter with the Central Military Commission. He must have found your story very interesting, because he keeps bowing to me. Run over and put a pain-relief patch on him.”

“Y-Yes, sir!”

The young man answered with a shriek and darted over, only to let out a real scream when a mana-infused kick struck his shin.

Jin Taekyung chuckled at the sight and began to leave, but then he suddenly stopped.

“Ah, there’s one thing you’ve got wrong.”

“M-Me?”

The middle-aged man, who had been standing there half-dazed, suddenly came to his senses.

“I’m sorry, but what is it?”

“I didn’t do it alone.”

“What?”

“Everyone fought like hell. By the time I arrived, the battle was almost over. Make sure you tell the others that too.”

“Is that really true?”

“Of course. Oh, do you have a family?”

“Yes. Three daughters and five sons……”

“You’re quite the patriot. In a few years, you could put together a soccer team.”

Jin Taekyung seemed to think about something, then abruptly asked another question.

“You’re not part of a combat unit, are you?”

“……You knew right away.”

The middle-aged man lowered his head in embarrassment.

“As you can see, I’m an E-rank Hunter, so I was excluded from combat. I’ll probably be assigned to tally the casualties.”

“Then can I ask you for one favor?”

“It would be my honor, Mr. Jin.”

“Then please include one person on the list of the dead. We won’t be able to find his body, so I’m asking you to make a special exception.”

“What is his name?”

“Lei Fei. Lei Fei.”

That was the last thing Jin Taekyung said.

The middle-aged man remained rooted in place, staring at Jin’s back as he walked away. At last, he released the breath he had been holding.

He felt certain that Jin Taekyung’s expression the last time he saw him would remain etched in his memory for a long time.

*What was that look in his eyes……?*

The resolve to see something through no matter what.

The middle-aged man, who had repeatedly expressed his awe at Jin Taekyung, picked up the canned drink the young man had left behind and took a swallow to wet his throat.

Then he frowned at its indescribable flavor.

“Ptooey!”

Burdian?

It looked like a Korean drink, but it tasted fucking awful.

* * *

“You’ve come, Mr. Jin.”

Wei Fenghu was not the only one waiting for me.

Five monitors stood inside the conference room. Sitting on the screens were five S-rank Hunters.

I opened my mouth in a calm voice.

“Let’s go end the war.”

At long last, it was time to eliminate the culprit behind all of this.

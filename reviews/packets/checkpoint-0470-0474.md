# Checkpoint Review — 470–474

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

# Chapters 470–474

## Plot

Jin Taekyung and Cheongpung battle the Mutated Water God Dragon after the System forcibly assigns Taekyung the Supreme Peak–Grade Corrupted Spirit Beast Quest and disables Logout. The dragon destroys the ferryboat, attacks with boulders, whiskers, water, and its tail, and overwhelms the party with Fear. Cheongpung resists the Fear, while Gung Gibang and Hyuk Mujin recover only after Taekyung rouses them.

Jeok Cheongang, Mungyeong, and Zhuge Feng arrive. Jeok breaks through the dragon’s Fear with rage and Scorching Yang Qi; Mungyeong does so through reason and enlightenment. Together with Taekyung and Cheongpung, they injure the dragon, but its enormous body, speed, scales, and anomalous accumulated qi make it comparable to multiple Supreme Peak masters. Mungyeong concludes that the dragon’s body and whiskers likely caused the destruction at Donghu Stronghold and the death of Yangtze One Saber.

Taekyung drives White Flame into the dragon’s eye, triggering its Berserk Status. While the dragon rampages through the cliffs and river, Taekyung tears out its whiskers by their roots, then strips away scales and attacks its head with the Flame-Extinguishing Divine Fist. Jeok identifies Taekyung’s superhuman strength as the result of his Heavenly Martial Physique.

The enraged dragon summons storms, lightning, floods, and whirlpools before forming a massive sphere of water in its mouth. It fires the attack as Taekyung, Jeok, Mungyeong, and Cheongpung rush to respond. The narration identifies Breath as the exclusive power of dragonkin and ends by questioning how this corrupted Water God Dragon can use it.

## Continuity

- The forced System Quest **Corrupted Spirit Beast** remains active; Logout is disabled, and Taekyung must defeat the Mutated Water God Dragon or suffer death or an equivalent penalty.
- The Water God Dragon was once a noble spirit beast awaiting ascension before an unknown power corrupted it into an evil beast.
- The dragon has lost one eye, every whisker, and many scales, but remains alive and berserk. Its Berserk Status increases its abilities while impairing its judgment.
- Taekyung possesses the Heavenly Martial Physique, granting superhuman physical strength independent of his accumulated internal energy and martial enlightenment.
- The dragon’s scales resist early Peak Sword Energy; Force is normally required to penetrate them. Its accumulated qi is distinct from both Force and Sword Energy.
- The dragon can manipulate surrounding water and weather and has begun using Breath, forming and firing a gigantic sphere of water.
- Cheongpung remains highly resistant to Fear and fights with the Zaha Divine Technique. Mungyeong remains partly affected but continues fighting as the former Slaughter Saint.
- Jeok Cheongang can withstand the dragon’s direct tail strike and remains engaged in battle. Zhuge Feng stays under cover to protect the others.
- The unidentified figure remains attached to the dragon’s head and can tear out its whiskers barehanded.
- The Dongting Fisherman remains severely injured, sealed, and alive for interrogation about Dark Heaven. Honglan is recovering, and Ju Wongong remains unconscious under guard.
- Unresolved: the fisherman’s role in Dark Heaven and the damage to his refuge; the shared Arch Lich/Dark Heaven symbols; the dragon’s possible responsibility for the Yangtze River Channel League massacres and the missing Moving Formation traces; the power that corrupted the dragon; the dragon’s origin and purpose; the unidentified figure’s identity and strength.

## Translation Decisions

- Render 타락한 영물 as **Corrupted Spirit Beast**, 악물 as **evil beast**, 광폭화 as **Berserk**, 천무지체 as **Heavenly Martial Physique**, 용족 as **Dragonkin**, and 브레스 as **Breath**.
- Preserve the distinction between accumulated qi, Force, Sword Energy, and Breath.
- Continue rendering 수염 as **whiskers**, 강기 as **Force**, 검기 as **Sword Energy**, 유령환살보 as **Ghost Illusory Slaughter Step**, and 멸염신권 as **Flame-Extinguishing Divine Fist**.
- Preserve Taekyung’s blunt profanity, dry contemporary humor, and vicious combat jokes, including the Baldy and hairless-head taunts.
- Preserve Cheongpung’s innocent literalism and emerging profanity, Mungyeong’s impassive Slaughter Saint voice, and Jeok Cheongang’s gruff insults.
- Retain **live-fish sashimi**, **bone-in sashimi**, the explanatory footnote, and jang and geun measurements.

## Durable state

{
  "active_continuity": [
    "Taekyung's forced System Quest, Corrupted Spirit Beast, remains active with Logout disabled and the Mutated Water God Dragon as its target.",
    "The Water God Dragon was once a noble spirit beast awaiting ascension before an unknown power corrupted it into an evil beast.",
    "The battle remains active: Taekyung destroyed one eye, tore out every whisker, and ripped away many scales from the dragon with his bare hands while using his spear as an anchor.",
    "The dragon's Berserk Status increases all abilities but clouds combat judgment, and its rampage continues.",
    "Taekyung possesses the Heavenly Martial Physique, giving him superhuman physical strength independent of his accumulated internal energy and martial enlightenment.",
    "The dragon's scales are so durable that early Peak Sword Energy cannot properly cut them; Force is normally required to split them and damage what lies beneath.",
    "Cheongpung remains resistant to Fear and fights with the Zaha Divine Technique; Mungyeong remains partially affected by Fear but continues fighting as the former Slaughter Saint.",
    "The dragon possesses extreme speed, immense durability, black scales, and centuries of accumulated qi.",
    "The dragon's anger manifests as violent storms, lightning, swollen river whirlpools, and other responses from the surrounding water and weather.",
    "The dragon has begun using Breath: its pupils turn black, it forms a massive sphere of water in its mouth, and it fires the sphere toward the ground.",
    "Zhuge Feng remains under cover protecting the others, and the severely injured Dongting Fisherman remains alive for interrogation about Dark Heaven.",
    "An unidentified figure remains on the dragon's head and can tear out its whiskers barehanded."
  ],
  "continuity_sources": [
    474,
    473
  ],
  "open_questions": [
    "What is the Dongting Fisherman's exact role within Dark Heaven, and how was he connected to the earlier destruction inside the secret refuge?",
    "What are the origin and purpose of the symbols shared by the Arch Lich's magic circle and Dark Heaven's formations?",
    "Did the Mutated Water God Dragon destroy Donghu Stronghold and the related Yangtze River Channel League strongholds, and why was no Moving Formation trace left?",
    "What unknown power corrupted the Water God Dragon, and what are its true origin and purpose?",
    "Who is the unidentified figure hanging from the dragon's head, and why can that figure tear out its whiskers barehanded?"
  ],
  "safe_through": 474,
  "temporary_decisions": [
    "Render 광폭화 as Berserk and preserve the System Status distinction.",
    "Render 활어회 as live-fish sashimi and 세꼬시 as bone-in sashimi with an explanatory footnote.",
    "Preserve Taekyung's profane, improvisational combat humor and Jin-ho's deliberately absurd USB-related saying.",
    "Continue rendering 수염 as whiskers and distinguish the dragon's anomalous qi from Force and Sword Energy.",
    "Retain jang and geun measurements."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 470

# Chapter 470

No, what the hell was going on?

Even with every second counting, I blanked out for a moment before finally managing to open my mouth.

“W-Wait a second. Young Hero Cheongpung.”

“I’ve never seen anything like that in my life! Just as Grandfather said, the world really is vast! I’m so glad I left Huashan!”

“Yes, the world is vast, but that has absolutely nothing to do with—”

“Whoa! It moved again!”

“……”

He wasn’t listening to a word I said.

I had known for a long time that Cheongpung was a little unhinged, but I had never imagined he was this far gone.

*What kind of person is this?*

Even a veteran Hunter who encountered monsters more often than his own parents would naturally feel fear upon facing a supermassive monster of that size.

But Cheongpung wasn’t merely unaffected by Fear. He was running around excitedly.

I had underestimated him without realizing it. He wasn’t a little crazy. He was thoroughly insane.

*Still, it’s much better than having him tremble like the others.*

He was different from ordinary people from the very beginning. The fear of the unknown—of an existence no one had ever seen or heard of before—did not apply to Cheongpung.

Because everything was new and interesting to that bastard.

*If you pointed a gun at a baby who didn’t even know what a gun was, it would just smile because it found the gun fascinating.*

I’d stake Hyuk Mujin’s balls on this: even if you turned the entire world upside down and shook it out, Cheongpung would be the only martial artist in all of Murim capable of reacting this way to such an enormous monster.

*……Yeah. This is much better.*

Gung Gibang and Hyuk Mujin were still half out of their minds.

With the situation desperate enough to borrow even a cat’s paw, Cheongpung’s resistance to Fear was a tremendous help.

I grabbed Cheongpung by the shoulders as he stared back and forth between the thoroughly cowed Mimi-chan and the Mutated Water God Dragon with glittering eyes.

“Staring at it like that won’t make it evolve, so snap out of it. Protect the boatman and the Dongting Fisherman first.”

“What about you, Benefactor?”

“I need to get those two back to their senses first.”

Before I had even finished speaking, I raced forward and slapped Gung Gibang and Hyuk Mujin across the face.

*Smack! Smack!*

Two bodies went tumbling away to the accompaniment of sharp, satisfying sounds.

The two men flailed like people waking from nightmares, then looked up at me with unsteady eyes.

“Gasp—cough.”

“C-Captain.”

I had put a fair amount of strength into those slaps.

Their mouths must have split open from that single blow, because blood poured through their parted lips. But Gung Gibang and Hyuk Mujin didn’t even have enough room left in their minds to feel pain.

“I thought it was a dream. Why am I still seeing things?”

“W-What is that?”

Even if my help had pulled them out of Fear’s influence, it was impossible to erase the primitive fear inherent to being human.

As the two men stared blankly over my shoulder, a low, deep roar rang out in every direction.

—Kraaaaaaah!

Damn it. I didn’t need to turn around to know that the enormous monster was thoroughly enraged.

I also knew what that terrifying sound splitting the air and rapidly approaching from behind was.

“Cheongpung!”

I shouted as I grabbed Gung Gibang and Hyuk Mujin by the backs of their necks and threw myself aside.

At the same time, something enormous viciously struck the place where we had been standing.

*Whoooooosh—crash!*

Sand and mud erupted into the air with a deafening boom.

The thing that had missed us by only a few steps was a bizarre boulder that looked to be nearly one *jang* tall.

*……It threw that all the way here?*

The boulder must have weighed several thousand *geun* at least, yet it had been hurled from far away.

Its strength was terrifying, but its aim was accurate, too. If I hadn’t moved quickly, I would have been crushed to death on the spot.

*Look at that accuracy. Was it from the Major Leagues?*

Just as I stared at the monster with a horrified expression, a familiar notification pierced my ears alongside its enraged roar.

*Ding.*

> **System**
>
> - A sudden Quest, **Corrupted Spirit Beast**, has been generated.
>
> - You cannot refuse the Quest. The Quest has been forcibly accepted!
>
> - **Logout** is unavailable while the Quest is in progress!
>
> **Quest**
>
> **Corrupted Spirit Beast**
>
> For many years, this noble existence waited to ascend within the depths of a great river. But an unknown power corrupted it.
>
> The spirit beast, which once possessed dazzling intelligence and a beautiful form, has become an ugly evil beast. Because of the countless deaths it has caused, it will never be able to return to its former appearance.
>
> And now, you must stop this unfortunate yet powerful evil beast.
>
> Dispel the dark clouds hanging over Hubei Province!
>
> **Grade:** Supreme Peak
>
> **Restriction:** Jin Taekyung
>
> **Objective:** Defeat the **Mutated Water God Dragon** (Incomplete)
>
> **Reward:** Linked Quest
>
> &nbsp;&nbsp;Vast EXP and Fame
>
> &nbsp;&nbsp;???
>
> **Failure:** Death or an equivalent penalty

I checked the Quest window at lightning speed. My assessment was short and concise.

“……What a load of crap.”

It was the worst Quest imaginable for the worst possible situation.

First, the Quest had been forcibly accepted. Then Logout had been prohibited. On top of that, it had driven the final nail into the coffin so I couldn’t even run away if things went badly.

Either I killed that enormous monster or I died here.

The System was demanding that I choose one of those two options.

*And it says death or an equivalent penalty. What the hell kind of penalty is that supposed to be?*

I didn’t even want to think about it. No—to be precise, I wasn’t given so much as a moment to think any further.

*Boom! Whoooooosh!*

The next moment, I saw it.

Beyond the semitransparent holographic window, a cliff collapsing in the distance and dozens of black dots filling the vast sky overhead as they plunged downward like meteors.

Faced with that spectacular sight, Hyuk Mujin and Gung Gibang muttered blankly.

“Are those stars? Yeah. They must be stars.”

“They’re too dark to be stars. And they’re getting closer.”

“Stars have all been like that lately.”

“Come to think of it, that’s true. Captain, you always tell me to throw away my preconceptions, but……”

“You two crazy bastards!”

*Grab—whoooooosh!*

I seized the two men, who still hadn’t come to their senses and were spouting nonsense, and threw myself aside.

Cheongpung was no exception. He had the Dongting Fisherman, who had passed out again after giving his warning, tucked under one arm and the old boatman under the other.

“Benefactor! They’re big! And there are lots of them!”

His language skills were on an elementary-school level, but that was more than enough to understand what he meant. Even I could see that there were far too many of those bizarre boulders falling toward us.

There was no doubt they would cover every inch of the narrow patch of ground where we stood—and then some.

*Whoooooosh!*

Damn it. There was nowhere to dodge.

As I threw the two men I was holding behind me, I recited the activation command in my mind.

*Open Inventory. Summon.*

White Flame appeared in my hand, just as the shadow of an enormous bizarre boulder spread over my head.

Without hesitation, I pulled up all the internal energy in my body and swept the spearhead forward.

*Shh-shh-shh-shing!*

Blue-white Force erupted from the spearhead and tore through the air.

It shot toward the bizarre boulders, which must have spent countless ages as part of the cliff, undergoing layer after layer of deposition and weathering.

*Split apart.*

*Schk!*

Force was a concentrated manifestation of energy capable of cutting steel like soft tofu. The bizarre boulders caught in the arc traced by my spearhead broke into pieces and began to fall.

*Boom!*

Sand and river water surged upward with a boom that shook the ground.

Amid the shrill screams of Hyuk Mujin and Gung Gibang, I saw Cheongpung escaping the crisis by the same method I had used.

However……

*Crack!*

*Damn it. I forgot about that.*

My stomach twisted when I saw the shattered remains of the ferryboat, so thoroughly destroyed that not a trace of its original shape remained.

If the boat’s owner, the old boatman, had been awake, he might have fainted.

*If we stay here, we’ll be nothing more than targets. I need to use even the wreckage to move our position, at least for now—*

Before I could finish the thought, my body suddenly locked up.

I had only glanced across the surface of the water, but something that should have been there was missing.

The enormous being that had stood tall amid the raging river and flashing lightning had vanished without a trace.

*This is—*

A red alert rang out inside my head.

I widened my eyes and shouted at the top of my lungs.

“It’s coming!”

And in the next moment—

*Kwaaaaaaah!*

A wall of water more than ten *jang* high surged into the air, and a body far darker and larger than the bizarre boulders blocked out the blackened sky.

My familiar face was reflected in its long, vertical, blood-red pupils.

—Grrrrrrrr.

The breath spilling from the maw of that corrupted evil beast was chillingly cold. Its enormous body, larger than any monster I had ever seen, radiated killing intent and pressure that crushed down on everything around it.

*What kind of monster is this……!*

That was when it happened, as I stared up at it in shock.

*Shra-ra-ra-ra-ra!*

Countless streaks of light came raining down from every direction.

The whiskers surrounding the bridge of its nose, which was covered in hard scales, split into hundreds of strands and plunged toward me.

Each one was several *jang* long. Some shot straight forward, while others curved like living creatures and attacked from blind spots.

“……!”

I wasn’t even given time to shout.

Every hair on my body stood on end, and all my senses opened wide. I twisted my body in the slowed-down world.

*Thud-thud-thud-thud! Slash!*

A scorching pain spread from around my shoulder. It was obvious who the drops of blood spattering across the muddy water belonged to.

Still, if I had avoided an unexpected strike with no more than an injury like this, I had gotten off cheap.

Now it was time to make the monster pay a much higher price.

“Hah!”

*Schk!*

The spearhead I swung with a battle cry cut through dozens of whiskers.

The long, flaming tail of the **Fire Dragon’s Single Tail**, befitting the form’s name, did not stop there. It cut through the air and swept toward the monster’s jaw.

*Whoooooosh!*

Alongside a deafening sound of something splitting the air, everything around me turned black.

Time slowed until it felt as though everything had stopped. Only then did I see it clearly.

Something flying toward me from the side, tracing a massive arc.

*Ah, fuck. The tail.*

The instant I realized what it was, an enormous impact swept through my entire body.

*Boom!*

My clear vision blurred.

In less than a second, the sky and ground flipped over countless times, and everything around me shook as if an earthquake had struck.

No. That wasn’t right.

The only thing flipping and shaking was me.

When I finally escaped the enormous impact that had tangled even my thoughts, I was flying across more than ten *jang* of space in a flash, headed straight for the cliff.

*Damn it. I need to dodge, even now…….*

But I couldn’t move my body easily after taking a blow carrying such tremendous force.

I gritted my teeth and braced myself for the secondary impact that was about to come.

No.

I tried to brace myself.

*Thud. Krrrraaaack!*

A light impact reached me through my back. Then my speed began to decrease as the ground was churned up beneath me.

As I blinked, someone’s voice reached my ears.

“Are you all right, Benefactor?”

It was Cheongpung.

I exhaled the breath I had been holding and stood on both feet. Then I realized why the Quest’s Grade was Supreme Peak instead of a question mark.

“Hey, you goddamn eel bastard!”

At the sound of that familiar voice, I let out a quiet laugh.
## Chapter artifact 471

# Chapter 471

Fire King Jeok Cheongang had lived for well over a hundred years.

The boy who had wandered from place to place, begging for food, met a master one day and became the eighteenth successor of the Fire Gate Clan. When time passed and his master returned to the earth, he became both the clan’s sole Disciple and its Sect Leader.

It had taken a truly long time for the boy to become a young man, the young man to become middle-aged, and finally the middle-aged man to become old.

During that time, a great war erupted—one that would determine the fate of the world—and a new nation was founded under a new imperial surname.

Five floods and earthquakes struck. Plagues spread, and bands of bandits wearing red turbans rose everywhere, pillaging as they pleased.

In every event Jeok Cheongang had witnessed, there had been disasters brought about by humans and divine punishments sent down by the heavens.

But one event had left the deepest and greatest mark on his life.

The Great Faction War.

An age when corpses formed mountains and blood flowed like rivers.

Amid that war’s vortex, Jeok Cheongang glimpsed a vast world of demonic, heterodox arts unlike anything he had ever experienced.

The martial arts of the Heavenly Demon Divine Cult, which could be compared to those of Shaolin Temple, the Mount Tai and Northern Dipper of the Murim’s orthodox faction, were deep and broad—devious, yet bizarre.

But now, Jeok Cheongang understood.

Even if he combined everything he had seen and experienced throughout his life, it would amount to nothing more than a drop in the bucket compared to the scene unfolding before his eyes.

*Rumble-rumble-rumble!*

*What in the world…?*

And when he finally saw the enormous being reveal itself, Jeok Cheongang felt as though every drop of blood in his body had frozen.

*What on earth is that thing?*

He was a master from two generations past, well beyond his ninety-ninth year.

Given the years he had lived and the position he held, he had seen no small number of beings that ordinary martial artists might never encounter even once in their entire lives—beings known as spirit beasts or evil beasts.

But that being…

It was different. It surpassed every bit of Fire King Jeok Cheongang’s experience and knowledge.

The thing being destroyed by the monster was not merely the cliff.

The laws and rules of the world he had firmly believed in were collapsing along with the bizarre boulders. They were being destroyed and scattered completely.

And Jeok Cheongang was not the only one feeling that shock.

“Ha.”

“Ah, ahhh!”

The greatest assassin of all time, known as the Slaughter Saint, could not suppress his groan of disbelief. Crouching Dragon Guest Zhuge Feng, whose knowledge and genius alone were said to rival those of Zhuge Wuhou of the past, was left speechless.

But the shock they felt did not end there.

—Kraaaaaaaaaah!

The enormous monster’s roar drove back the rain and burst the wind apart.

At the same time, a chilling aura spreading outward from the monster engulfed the entire bodies of the three people standing more than a hundred *jang* away.

*Whooooooosh!*

“……”

“……”

“……”

The three figures stiffened at once, as if they had made an agreement to do so. In their three pairs of eyes, widened without their consent, unmistakable shock appeared.

*This can’t be!*

Their bodies had grown heavy as wet cotton, and their clenched hands were tightening on their own.

Zhuge Feng, who still remained at the Peak realm, let out a faint groan amid an overpowering chill. Jeok Cheongang and Mungyeong, whose realms were unimaginably higher, swallowed a startled breath in spite of themselves.

*Th-This is…!*

*Impossible.*

The two extraordinary martial artists known as the Fire King and the Slaughter Saint immediately realized the identity of the unfamiliar sensation that had come over them.

It was an emotion they had forgotten long ago. A stale, ancient emotion they had been unable to feel since becoming beings so powerful that no one dared approach them.

Fear.

The sheer strength of the Fear radiating from the Mutated Water God Dragon was certainly partly responsible. But the greater cause was the ignorance of Jeok Cheongang and Mungyeong.

Their martial arts were unquestionably several levels above those of modern S-rank Hunters. Even so, the appearance of a gigantic monster they had never encountered before was more than enough to shake the firm minds of two people who had spent decades building their own domains and common sense.

—Kraaaaaaow!

The monster did not miss the opening and began rampaging with all its might.

Each time its body, covered in black scales, lashed against the cliff, enormous bizarre boulders filled the sky before crashing down.

*Kwagwagwagwang!*

A rain of bizarre boulders shot without pause toward somewhere hidden from view by the terrain.

Flames poured from Jeok Cheongang’s eyes as he watched the sight.

*You bastard!*

Jeok Cheongang already knew what the unknown monster was attacking so relentlessly.

His sole successor to the Fire Gate Clan and his Disciple. No—his temporary Disciple, Jin Taekyung.

As he recalled that fact, lava-like energy burst from his entire body, which had been momentarily frozen by Fear.

*Whoom!*

Several jiazi’s worth of Scorching Yang Qi surged along his Twelve Regular Meridians and Eight Extraordinary Meridians, pushing away the power radiating from the unknown being.

Though only for an instant, superheated energy filled his body, which had been briefly immobilized. Then he released a battle cry like a thunderclap.

“Ha!”

*Bang!*

The internal energy contained in that shout was so powerful that the raindrops and air filling the area around the three men burst apart.

Jeok Cheongang had not yet completely escaped Fear’s influence. But even though he had been exposed to Fear for the first time in his life, he had broken free of it on his own, without anyone’s help.

If modern Hunters had witnessed the scene, they would have doubted their own eyes.

But Jeok Cheongang was not the only one to accomplish something so astonishing.

If Jeok Cheongang dispelled part of Fear through his rage, Mungyeong overcame its oppression through cool reason and enlightenment half a step above Jeok Cheongang’s.

*An evil beast unheard of throughout history. It must be brought down here and now.*

The young medical apprentice who had always cared warmly for the sick was no longer present.

As the greatest assassin of all time—the one feared by everyone in the world—took a step forward with calm eyes, his slender figure scattered like an illusion.

*Tap. Whoooooosh!*

The Slaughter Saint’s signature martial art, the Ghost Illusory Slaughter Step, shot forward after pressing down on the current and stepping across the raindrops.

His figure advanced like a streak of light, leaving behind only a pale afterimage. Beneath him, a single trail of flame raced forward, evaporating every trace of moisture around it.

*Whoom!*

A furious roar erupted from between Jeok Cheongang’s lips.

“You unholy eel bastard! Get away from that boy this instant!”

* * *

*Rumble, crash!*

A clear, ringing shout pierced through the ceaseless thunder. At the same time, two figures charged toward the gigantic Water God Dragon at the speed of lightning.

Only now did I finally understand why the Quest’s Grade was Supreme Peak.

*It might have been difficult alone, but things are different now.*

There was Cheongpung—a proud Supreme Peak master and a genius whose application and acquisition of martial arts even I, despite using the System, couldn’t keep up with.

And then there were two existences who needed no embellishment whatsoever.

The Fire King and the Slaughter Saint. The Slaughter Saint and the Fire King.

Even by the standards of the modern world, where average life expectancy had risen dramatically, those two were old enough to be playing gateball in a retirement community.

Yet they were both monsters capable of knocking a Peak master’s head clean off with a single finger.

*Their movements do look a little heavier than before…*

Had those two also been affected by Fear, even if only slightly?

In any case, two more human-shaped monsters had joined the fight against the supermassive monster.

I had taken a little damage in the initial clash, but aside from the minor Internal Injury I had suffered while fighting the Dongting Fisherman and the cut on my shoulder, I was perfectly fine.

*If I hadn’t had those insane Muscles and Bones and the Fire Dragon Armor, I might have broken all four limbs.*

The monster moved far faster than its massive body suggested, and it used its whiskers to attack.

Just as I was thinking that it resembled the Sea Serpent I had read about in the *Monster Encyclopedia* while still being different in certain ways—

—Grrrrrrr…!

In that split second, the Water God Dragon’s eyes flashed as it finally realized the situation was taking an unusual turn.

And I did not miss that brief opening.

“Cheongpung!”

“Yes, Benefactor!”

Sometimes, a single short word or the exchange of a glance was enough for two people to understand each other.

Cheongpung and I were exactly like that as we rushed toward the Water God Dragon at the same time as my shout.

*Whoooooosh!*

*Shh-shh-shh-shing!*

We were moving twice as fast as when the dragon’s tail had sent us flying.

As blue and red Force surged along the spearhead and sword blade and rose toward it, the Water God Dragon’s whiskers thrashed violently.

*Shri-ri-ri-rik!*

Those whiskers were the absolute worst.

The energy contained in each one was not quite as powerful as the Force of a Supreme Peak master, but their destructive power and sharpness surpassed ordinary Sword Energy. They could not be ignored.

On top of that, each strand was roughly three *jang* long. Their trajectories were bizarre and impossible to predict, much like the Dongting Fisherman’s martial arts when he used his black-wood fishing rod.

The only reason I had allowed the first attack to land was that I hadn’t known the bastard could use hundreds of whiskers like that.

But…

*Come at me again, you son of a bitch.*

Streaks of light carrying the Water God Dragon’s power poured down from every direction. I slashed the spearhead diagonally downward in front of me.

*Whoooooom! Schk!*

The streaks of light caught in the path drawn by the blue-white flames lost their strength and were sliced apart.

But the Water God Dragon was no pushover, either. Just as many streaks of light as I had cut through a moment ago were already targeting my back.

*Whoosh!*

I had sensed it from the beginning, but the bastard was definitely intelligent. Perhaps it had instinctively recognized the strength of the Fire Dragon Armor and was targeting the bare flesh not protected by the armor.

My back grew cold as I felt the killing intent flying toward me.

But an instant ahead of it, a powerful force came rushing in.

*Shik. Schk!*

Brilliant violet Force drove away the darkness and illuminated the world.

The Zaha Divine Technique, a secret ultimate art taught only to the direct Disciples of Huashan.

*Cheongpung.*

I felt the killing intent shooting toward my back vanish.

I knew without turning around to check. Cheongpung had carried out his role perfectly.

Now it was my turn to use all my strength.

No. Correction.

It was our turn.

—Grrrrrrrrk!

The Mutated Water God Dragon hurriedly raised its head, but it was already too late.

Its failure to stop Cheongpung and me in time was its greatest mistake. Two human-shaped monsters were already closing in behind its enormous body.

*Shik!*

Quietly and stealthily. At the same time, with a swiftness greater than anything else, a streak of lightning plunged down from the air.

Then, a moment later, the sound of something being sliced apart rang out.

*Schk!*

One of the Water God Dragon’s black horns was cut in half when it met the silver Force. A cry that might have been pain or rage burst from the monster’s maw.

—Graaaargh!

“Gasp!”

Mungyeong’s figure shook as he tried to thrust a small sword between the Water God Dragon’s scales.

*My guess was right.*

Unlike me, who was accustomed to the Fear of monsters, and Cheongpung, who was simply insane to begin with, the others had not yet completely escaped Fear’s influence, though the degree varied from person to person.

But that did not mean the fist Jeok Cheongang had already launched stopped.

“You godforsaken son of a bitch—!”

Jeok Cheongang spewed the curse like a magic incantation, and his fist slammed into the Water God Dragon’s waist.

*Fwoosh! Boom!*

—Kra-ra-ra-ra-ra!

An enormous amount of flame and steam exploded outward, and the Water God Dragon’s gigantic body tilted toward the ground.

At the end of the direction in which its maw was falling, I was already charging forward with all my strength.

*Whoooooosh!*

—Krrk!

My figure, thrusting White Flame wreathed in blue fire, was reflected in the enormous blood-red pupil split vertically down the middle.

“I told you not to open those eyes like that, you sibu-leol bastard.”

*Shnk!*
## Chapter artifact 472

# Chapter 472

*Puhuk!*

The heat boring through the pupil was scorching, while the pain that followed was cold enough to numb the senses.

The Mutated Water God Dragon let out a roar filled with agony as the pain spread through its body like flames.

—Kraaaaaaaaaah!

Its torso was as thick as a dozen or so full-grown trees bundled together, and its length easily exceeded thirty *jang*.

When the enormous body, reminiscent of a small mountain, thrashed about madly, a tremendous shock wave swept through the surrounding area.

*Kwang! Kwagwagwagwang!*

The bizarre boulders it had hurled earlier exploded into hundreds and thousands of fragments, while barriers of dirt and water surged into the air.

As every direction was reduced to a wasteland as though it had been subjected to concentrated bombardment, several figures raced swiftly through the chaos.

*Shh-shh-shik!*

Some charged toward the monster, while others retreated a considerable distance to avoid its thrashing. Zhuge Feng, the current Family Head of the Zhuge Clan and the Crouching Dragon Guest, belonged to the latter group.

At last, his reason returned, and he stared at the scene before him in bewilderment.

*It isn’t enough that the heavenly patterns are becoming distorted. Now beings of supernatural powers are appearing too?*

Zhuge Feng possessed an abundance of knowledge about the creatures called spirit beasts or evil beasts, but this dragon-like monster shattered every bit of common sense.

If word of what had happened here today reached the outside world, there was no doubt that not only the Murim but the entire world would be thrown into an uproar.

*How could something like this happen…?*

Zhuge Feng’s body trembled from fear that still had not completely faded when someone spoke to him.

“Stay here with the others. Hide behind cover and keep yourselves as safe as possible.”

Any martial artist would have felt his pride wounded upon hearing those words. Martial artists were people who staked their lives on their martial arts and a single sword as they roamed mountains of blades and forests of swords.

Zhuge Feng looked at the other person with a stiff expression and opened his mouth.

“Who am I?”

“Pardon?”

“I asked if you know who I am.”

Cheongpung answered.

“Yes. Great Hero Zhuge Pong.”

“It’s Zhuge Feng, not Zhuge Pong. In any case, you do know that I’m the Family Head of the Zhuge Clan.”

“Uh, yes, I do know that…”

“And yet you’re telling the Family Head of the Zhuge Clan to hide like a coward?”

Cheongpung thought about it, then nodded.

“That would be much safer.”

“Good. Then I should stay right here without moving.”

“Pardon?”

“Didn’t you say this place was safe? Better to be a coward than die a pointless death.”

“…?”

“Don’t look at me like that. It’s simply that this isn’t a battle I need to fight today. It’s the same reason Zhuge Wuhou, our family’s ancestor, did not stand at the vanguard and cut down the enemy.”

Zhuge Feng knew exactly where he stood and what he needed to do.

He was too clearheaded to wager his life on a martial artist’s pride, and as a Family Head, he was responsible for countless members of his household.

“This vast war has only just begun. The day will come when I can prove my worth in the battles ahead. So go on. I’ll protect these people.”

Cheongpung regarded Zhuge Feng with a strange look, then turned away with a small bow.

As the young man disappeared into the distance like a gust of wind, Zhuge Feng’s gaze grew somber.

*Yes. The beginning of another age of chaos.*

The peace that had lasted for more than fifty years had come to an end. The sky had turned black with clouds, and new winds were blowing in from every direction.

Cheongpung, shooting toward the distant battlefield, was one of those winds.

*Wuhou. At least today, it seems there is no place for this unworthy descendant to step forward.*

Just as Zhuge Feng muttered those words quietly to himself, a conversation in dazed voices behind him pierced his ears.

“I can see a monster over there. Is this a dream?”

“I don’t think it’s a dream. No. Maybe it is a dream.”

“But Hyuk, why are your pants so wet?”

“It’s raining. They must have gotten wet.”

“That’s a very bright yellow for rainwater.”

“That can happen.”

“Can it? How strange. Anyway, isn’t this really a dream?”

“I don’t think it’s a dream. No. Maybe it is a dream.”

“But Hyuk, why are your pants so wet—”

“…”

Zhuge Feng listened to the utterly incoherent conversation, then quietly moved away to escape the smell of urine.

On a hill formed by dirt and sand that had piled up into a small mound, he looked toward a battlefield that resembled a scene taken straight from mythology.

* * *

*Shhk, schk!*

When a silver line cleaved through space, everything rushing toward him was cut apart.

*Papat!*

The instant Mungyeong’s figure vanished like an illusion and then sprang upward after stepping on a fragment of stone suspended in the air—

*Whoooooosh!*

Something enormous came hurtling through the spray and clouds of dust.

It did not take long for him to realize that it was a tail covered in black scales.

*It’s fast. Faster than I expected.*

Its movements were impossibly swift for a body of such tremendous size. Mungyeong gripped his short sword tightly as he drew a breath.

*Tsstsstssts!*

Quietly, yet at a speed as sudden as lightning, internal energy surged upward and wrapped around the short sword.

A power more destructive and sharper than anything in the world. Force rose along the blade.

A technique containing the principles of extreme swiftness flowed from the fingertips of the greatest assassin of all time.

*I’ll cut it in one stroke.*

The next moment, Mungyeong brought his sword down diagonally toward the incoming tail—and realized that he had miscalculated.

*Schk.*

Although he had clearly cut it, the resistance transmitted through the blade was absurdly strong.

The Force imbued in his short sword had to cut through more than black scales.

Hidden beneath scales as hard as steel were flesh and muscles like wrought iron, along with bones boasting tremendous strength.

*Damn.*

Mungyeong clicked his tongue inwardly.

Force. And not just any Force, but Force infused with the enlightenment of the greatest assassin of all time.

No matter how hard the monster’s body was, his Force should have been able to cut through it in a single stroke.

The problem was its thickness.

The tail was a monstrous two *jang* in diameter.

Add to that the toughness of its flesh, which far exceeded his expectations…

*Cutting through it in one strike is impossible.*

Under normal circumstances, it might have been different. But he had not yet completely escaped the remnants of Fear, and he knew better than anyone that his martial prowess would not be at its full strength.

*In that case…*

At the same time as he made his decision, Mungyeong twisted the wrist gripping the sword hilt.

The blade, which had cut through the scales and was splitting the flesh and muscles beneath them, rotated smoothly. Its side diverted the force carried by the tail.

*Ka-ga-gak! Whoom!*

His small, slender figure was flung backward through the air.

*Kwaang!*

Mungyeong twisted his body in midair and landed with a rough movement that did not suit the name of the Ghost Illusory Slaughter Step. Beside him, Jeok Cheongang melted an incoming bizarre boulder with a single palm strike and muttered mockingly.

“Did your martial arts become childish too after you Returned to Youth?”

“Its strength and speed both far exceeded my expectations. Even with the principles of Four Ounces Deflecting a Thousand Catties, I couldn’t completely redirect it.”

“Your tongue got longer, too.”

Mungyeong gave Jeok Cheongang a dry sidelong glance.

“If you’re trying to taunt me, stop here. The timing seems rather poor.”

“It isn’t a taunt. It’s an undeniable fact. Didn’t you see that thing crumple when this old man hit it once?”

“That was after I had already cut its horn…”

*Chiririririk! Kwang!*

A thunderous explosion swallowed Mungyeong’s continuing words.

The two men launched themselves away at the same time, as though they had made an agreement, and clicked their tongues while staring at the streak of light writhing like a living creature.

Only moments ago, the place where they had been standing had been completely devastated.

“The more I see, the more bizarre that thing becomes. An evil beast that can use Force?”

“It isn’t strong enough to be called Force, yet it’s too powerful to be called Sword Energy. It’s clearly not a cultivation technique, but the fact that it can use an art like this with energy accumulated over countless years is difficult to believe.”

Possessing energy and utilizing or releasing it were fundamentally different matters.

In that respect, the monster before them had far surpassed the common sense of both men.

*Was that thing also responsible for wiping out Yangtze One Saber and Donghu Stronghold?*

Mungyeong avoided the attack flying toward him once again and stared at the monster with profound eyes.

He had assumed that at least two Supreme Peak masters had attacked Donghu Stronghold. But after encountering that unimaginable monster, he finally felt that he understood what had happened.

*Those bizarre whiskers and that enormous body… There’s no mistake. They resemble the traces left on the corpses.*

He could picture the scene clearly: the monster crushing and cutting everything in its path with its tail and whiskers.

At the same time, the mystery surrounding the corpse of Yangtze One Saber, which everyone had thought had been damaged by schools of fish, was solved.

*He wasn’t torn apart and eaten after he died. He died because he was torn apart and eaten.*

Who could ever have imagined it?

That an enormous dragon-like monster had committed such a slaughter through a deep tributary blocked even to boats, a waterway that only fish could enter and leave.

Since it had never revealed itself, it was only natural that there had been no witnesses.

“It’s a monster, all right.”

He had no choice but to admit it. That monster possessed enough power to rival hundreds of Peak masters—or two or three Supreme Peak masters. It was a being of supernatural powers.

Jeok Cheongang nodded in agreement with Mungyeong’s lament.

“That’s right. It’s a monster.”

“I never thought such an inexplicable being truly existed.”

“That one never ceases to amaze me. That’s why I can’t help wondering what it would have been like if this old man had had more time. Just a little more time.”

“What are you—”

Mungyeong suddenly remembered something and looked at Jeok Cheongang. The old man’s wrinkled face, marked by the passage of countless years, was filled with a smile.

“Hey, Slaughter Saint. Do you know something?”

*Whoooooosh!*

A gigantic shadow descended with enough momentum to split the world apart.

Jeok Cheongang looked up at the black tail falling toward his small body and slowly continued.

“That one is the strangest and most terrifying monster this old man has ever seen.”

“Look out!”

Mungyeong’s eyes widened.

*Kwa-gwa-gwa-gwang! Fwoooosh!*

A tremendous roar and vibration spread across a radius of several dozen *jang*.

And at the center of it all, Jeok Cheongang stood tall without a single hair on his body harmed.

Unlike him, who had not moved even one step from where he had originally been standing, the black-scaled tail had struck the ground far away.

“Yes, that’s right. A monster should be fought by a monster.”

“……!”

*Thud-thud-thud.*

Above Jeok Cheongang’s head, where he laughed aloud, the monster’s dark-blue blood poured down mixed with the rain and wind.

Mungyeong turned toward the monster’s enormous body, and Cheongpung, who had just returned to the battlefield, looked in the same direction.

At last, they saw it.

The thrashing monster—and someone hanging from its head at a dizzying height, tearing out its whiskers with his bare hands.

“Baldy! Bald! Smooth, shiny, shaved head!”

*Ppok! Ppok! Ppobobobok!*

—Kroooooooooah!

The Water God Dragon’s mournful cry rang out through the rain and wind.
## Chapter artifact 473

# Chapter 473

*Puhuk!*

The Mutated Water God Dragon.

The instant I drove the tip of White Flame into its enormous eye, I realized something.

*Hard. And deep.*

It felt like plunging my hand into a cave with no visible end.

If it had been an ordinary human or beast, this single strike would have melted not only its eye but its entire head without a trace.

But this thing was different.

*What the…!*

Its head was so enormous that even after I drove White Flame in as far as it would go, the Force wrapped around the spearhead could not reach deep enough inside.

On top of that, the bones and flesh within were absurdly tough.

I was still reeling from the resistance that far exceeded my expectations when the Mutated Water God Dragon let out a scream of agony.

—Kraaaaaaaaaah!

I had failed to finish it with my decisive strike, but that did not mean I had failed to inflict any damage.

The Scorching Yang Qi carried by the spearhead had melted one of its eyes.

Its enormous body writhed in horrible pain. At the same time, a familiar System notification pierced my ears.

*Ding.*

> **System**
>
> - **Lv. ??? Mutated Water God Dragon** is overwhelmed by pain and rage it has never experienced before!
>
> - Enters **Berserk** Status!
>
> - Due to **Berserk**, all of the target’s stats increase! However, because it has momentarily lost its reason, its judgment in combat is clouded!

“... Huh?”

The moment I heard the System notification, I nearly lost my own reason.

*Damn it. What the hell is this Berserk bullshit?*

Do your damn job properly, System. It was already a monster. If it got even stronger, how was I supposed to make a living?

But the System had already activated, and the water was already spilled.

The Water God Dragon’s only remaining eye turned completely bloodred, and its Berserk Status began in earnest.

—Kyaaaaaaaaaow!

Along with a roar that shook heaven and earth, an enormous gust of wind slammed into my entire body.

Before I could even blink, I saw a cliff rush right up to my face.

*Oh. I’m fucked.*

*Kwaang!*

A tremendous shock wave crashed over my entire body with a roar that seemed to split the sky apart. My vision blurred, and my eyes lost focus.

The Water God Dragon slammed its head into the cliff with tens of thousands—perhaps hundreds of thousands—of *geun* of force, but it did not stop there.

*Whoooooosh!*

The length of its torso exposed above the surface of the water alone was more than thirty *jang*. If I counted the part hidden beneath the water, it was comparable in size to a modern aircraft carrier.

Once a monster that enormous began rampaging like a mad thing, nothing could stop it.

*Kwaang! Kwang! Kwagwagwagwang!*

It repeatedly smashed its head into the cliff and the river, lashed out with its tail, and sometimes flapped its entire body like a fish caught on a hook.

Every movement reduced the surrounding area to a wasteland, and countless fragments of rock and blasts of wind came crashing down on me.

Just like now.

*Ppeok!*

“... Hng!”

Damn it. Of all places, my back had slammed into a sharply jutting rock.

A searing pain raced up my spine. But I gritted my teeth and held back my groan.

This was the Water God Dragon’s desperate struggle to throw me off.

If I fell now, it might counterattack instead.

I tightened my grip on White Flame, driven deep into the bastard’s eye, and steadied the center of my body as it bucked wildly with the enormous body’s movements.

“You… you fucking bastard!”

If it thought I would be thrown off by something this pathetic, it was gravely mistaken.

I wrapped one hand tightly around the spear shaft and grasped at something invisible with the other.

At the moment, my hand was clutching nothing but empty air.

But that was about to change.

I had a magical command that only I could use.

*Inventory Open. Summon.*

*Shhk. Tak.*

The instant I gave the command, the hilt of a sharp short sword appeared in my hand.

The only sword technique I had learned was the basic swordsmanship taught at the Hunter training center.

But in a situation like this, who cared about sword technique?

Faster than anyone else, different from everyone else. This was the moment to become a sashimi master riding a different rhythm on the cutting board.

“From now on, your name is live-fish sashimi. Or maybe bone-in sashimi.”[^1]

I made the solemn declaration and drove the blade of the short sword, wrapped in blue-white Scorching Yang Qi, straight into it.

*Puk!*

The sword was too short to stab very deeply, but I definitely felt the signal of pain.

Its firm, pale flesh split open as though it were burning, and dark-blue blood burst out.

“You’ve got pink flesh, of all things, you bastard.”

—Krrrk!

A groan burst from the creature’s maw, and its body stopped for a moment.

I did not miss the opening and swung the short sword again.

*Schk! Puhuk!*

—Krrrrrk!

*Puh-puh-puh-puh-puhuk!*

—Kraaaaaaaaaah!

Sword technique? There was no such thing.

I simply cut and stabbed wherever my hands moved and wherever my eyes saw.

The speed at which the blade emerged after crushing and splitting through bone and flesh, then shot forward again, was faster than a flash of light.

Each time it did, the creature’s screams and thrashing grew more violent.

*Huh. This is actually useful at a time like this.*

My physical abilities, which could be called superhuman, certainly played a part. But the wrist snap I had trained through the USB—a treasure of humanity—was enough to make even a Peak sword master yield a move.

*Ah. So this is All Streams Returning to the Source…*

When had it been?

Just after I became a Sage, Jin-ho hyung had tried to stop me when I decided to destroy the USB.

His words flashed through my mind.

*Taekyung, remember the words left behind by our ancient ancestors. A ghost that dies after getting one in has a beautiful complexion. It’s getting one in that counts.*

*…Which ancestor said that?*

*Does that matter? The problem is that you’re about to destroy a national-treasure-grade cultural artifact. If you erase that thing, I’ll report you directly to the Cultural Heritage Administration. You’re looking at a minimum of twenty-five years in prison with no chance of parole.*

*Is he insane?*

What did he mean, getting one in? And what did he mean, a beautiful complexion?

Back then, I had nearly hit him.

But looking back now, those words were without question the greatest saying since the founding of Korea.

I felt profound gratitude toward Jin-ho hyung and thought of the women who had now become memories.

*Thank you, Uehara. I love you, filial daughter of the mapo tofu restaurant.*

*Schk! Puh-puh-puh-puh-puhuk!*

—Graaaargh!

Ah, what a *sugoi* scream.

The pro-Japanese sword technique filled with my gratitude gouged into the gaping pupil and drove deeper and deeper inside.

The Mutated Water God Dragon had no choice but to stop attacking the other enemies far below on the ground.

*Whoooooosh—Kwaang!*

I could not see what had happened, but I could tell from the sound.

As the enormous body shook in pain, the tail that had been coming down toward the ground had struck somewhere completely different.

Then, amid the rising dirt and spray, a streak of silver light flew toward me after changing targets.

*Chiririririk!*

From the outside, it must have been a bizarre sight.

A monster was using its own whiskers to gouge at its melted eye.

But from my position, there was nothing funny about it.

*Damn it.*

No matter how enormous the Mutated Water God Dragon’s eye was, the space was far too narrow for me to avoid dozens of whiskers.

Even though I twisted my body as much as possible, the streaks of light moved with the same cunning subtlety as the black-wood fishing rod, slipping past my Fire Dragon Armor and slicing into my bare flesh.

*Puhwak!*

“Ghk!”

Red blood sprayed out, and searing pain spread through every part of my body.

I had managed to protect myself by circulating my internal energy at the same time as I dodged, so this was all that happened.

If I had been even slightly slower, one of my limbs might have been severed.

*Chiriririk!*

Dozens of streaks of light flew toward me again.

I endured the rapidly spreading pain and twisted my body.

When the silver whiskers, which possessed terrifying cutting power, missed by less than the width of a hair, a chill ran down my spine.

*The space is too narrow. I’ll be cut to pieces if this continues.*

Perhaps it was because of that sense of crisis.

While I hesitated, a spear of light, twisted together like a rope into the shape of a spearhead, flew toward my face.

*Shwing!*

“...!”

It was unbelievably fast.

In the slowed-down world, I stared wide-eyed at the streak of light flying toward me with a sharp sound as it tore through the air.

Countless possibilities and thoughts flashed through my mind.

*If I pull out White Flame right now and swing it… No. It’s already too late. And I might lose my balance before then.*

Even now, the bastard’s head was shaking like mad.

If I pulled out White Flame, which was practically acting as a support, I would lose my balance for just an instant.

That would be the end.

*There has to be a better way. There has to be some better way…*

But the time I had been given amounted to no more than a fleeting instant, and the short sword I swung in haste was helplessly knocked away the moment it collided with the streak of light.

No—it shattered into hundreds of fragments.

*Kwa-chang!*

Perhaps it was only natural.

The power contained in each individual whisker did not reach the level of Force, but it surpassed the Sword Energy of a Peak master.

With that much energy gathered together, there was no way the traitorous sword technique I had learned through the USB could stand against it.

*Whoom!*

*Am I going to get hit like this?*

I stared blankly at the destructive force erasing the space between us and rushing toward my face.

What moved me was something close to instinct itself.

*Fwoosh—Kwaddeudeuk!*

Just as the streak of light was about to pierce through my chest, I found myself gripping it with a hand wreathed in blue-white flames.

It was neither Flame Divine Palm nor Flame-Extinguishing Divine Fist.

It was nothing more than a crude contest of strength, in which I dragged up every ounce of energy in my entire body and forced it against the attack.

The result of that clash did not take long to reveal itself.

*Pajik—Puhwak!*

Two powerful energies collided, filling my vision with a blinding flash.

And beyond that dazzling radiance, I could see my hand hanging in tatters like a rag and the streak of light, its thickness reduced ever so slightly.

There was no question who held the advantage.

*Damn it. The amount of energy we possess is on completely different levels.*

I had accumulated a tremendous amount of internal energy through the System’s accelerated growth.

But I could not compare with the bastard, which had accumulated qi for hundreds of years as a spirit beast.

*Kwa-deu-deuk!*

Even this grueling contest of strength was slowly reaching its limit.

I gritted my teeth as pain traveled through my hand.

“You live-fish-sashimi bastard!”

I could not end things here.

I summoned every last ounce of strength I possessed, twisted my body, and yanked hard on the creature’s whiskers as though executing a shoulder throw.

It was impossible.

But even if it was, I had to try—

*Kwadeudeudeudeuk—Ppok!*

“... Huh?”

—Krrk?

I was stunned.

The Mutated Water God Dragon was stunned too.

In the slowed-down world, dozens of whiskers had been torn out by the roots and were fluttering helplessly toward the ground.

*What the fuck? Why did those pull out?*

Countless thoughts flashed through my mind.

Was it really okay for them to come out this easily? Were its roots weaker than its hair? No, but even so, could this really happen…?

At last, I reached one conclusion.

*My strength is really fucking insane.*

When I thought about it, this was entirely possible.

I had enough muscle to knead steel like dough. What was pulling out a few whiskers compared to that?

No matter how enormous a monster the size of an aircraft carrier was, everything had its limits.

Unlike its scales and bones, which boasted tremendous durability, its hair roots were apparently weak enough for my Strength to pull out.

*So this is how it works.*

This was something only I could do, with my strength worthy of being called superhuman.

Until now, I had only thought about dodging and cutting.

It had never occurred to me to tear the whiskers out.

With that great enlightenment, I retrieved White Flame and stepped forward.

*Shwaaaaaaaaaak!*

When I emerged from the pupil, I saw the creature’s enormous body frozen stiff in confusion and its eye blinking rapidly.

“You bastard…”

I smiled brightly and tore out its whiskers.

*Kwadeudeuk!*

[^1]: *Hwal-eo-hoe* is sashimi prepared from live fish, while *sekkosi* is thinly sliced raw fish served with the bones left in.
## Chapter artifact 474

# Chapter 474

*Kwadeudeuk!*

The instant dozens of whiskers were torn out all at once by Jin Taekyung, the Mutated Water God Dragon opened wide the one eye it had left.

—Krrrrrk…!

It could not believe it.

That some tiny, insignificant human had torn out its whiskers—and with his bare hands, without even a weapon.

It was something that could not happen and should never have happened. Even for the Water God Dragon, which had lived for hundreds of years, it was a shocking first.

And then, in the next moment, the Water God Dragon realized something.

The human who had ripped out its whiskers using nothing but pure physical strength was completely fucking insane.

“Baldy!”

*Ppok!*

“Bald!”

*Ppobok!*

“Smooth, shiny, shaved head!”

*Ppobobobobok!*

—Gwooooooooooar!

A scream rising from the depths of its soul.

The Mutated Water God Dragon thrashed about, howling in agony. For some reason, it did not know why, but the pain and sorrow welling up inside it were dozens of times greater than when it had first lost its eye.

It had to get this mad human off it as soon as possible.

No—before every last whisker was torn out, it had to save at least one!

—Kroaaaaaah!

But unlike the Water God Dragon’s desperate wish, Jin Taekyung had no intention of stopping.

*Puhuk!*

After driving the spearhead between the scales covering the bridge of its nose and pinning himself in place, Jin Taekyung spoke in a sinister voice.

“Hey, know why you can’t walk?”

—Krrk…?

“Because you don’t have two feet. Hell, you don’t even have two hairs.”

*Ppobobobobobok!*

—Gwooooooar!

“Even if you multiplied together all the fur belonging to every spirit beast in the world, the result would still be zero. Because you don’t have any fur. You just don’t. You don’t have a goddamn single hair!”

*Kwadeudeudeuk!*

Jin Taekyung’s hands were more ruthless than ever.

Whenever the whiskers flew toward him in a tangled mass to attack, he caught them with one hand and yanked them out like weeds. Iron-hard skin split open, and whiskers tougher and sharper than Heavenly Silkworm Thread were ripped out in their entirety.

Every last one of them. Without leaving even a single strand behind.

—Uooh, uwooooooar!

Even through the reason clouded like a sky hidden behind storm clouds, the Mutated Water God Dragon was consumed by furious rage and sorrow.

What kind of whiskers were these?

They had grown alongside it for hundreds of years. They were practically companions of its soul.

They were excellent weapons with which to destroy intruders who harbored impudent thoughts, as well as symbols of its power and majesty.

And now those whiskers were gone. They had been pulled out helplessly, like weak and useless seaweed.

And by the hands of a human much smaller and more insignificant than itself!

—Kyaaaaaaaaaow!

A savage roar that shook heaven and earth.

When the master who had ruled Dongting Lake and the Yangtze for hundreds of years began to radiate a baleful aura, everything around it held its breath.

No. Everything changed according to its anger.

*Krrrrrung! Kwa-gwang!*

It was a truly frightening and bizarre sight. Lightning struck without pause from the sky, which was covered in unusually thick black clouds, while rain poured down in a deluge unlike anything seen in the past fifty years.

The river, swollen several times over by the abnormal weather that had continued for several shichen, formed whirlpools of every size that circled around the Water God Dragon.

*Kwaaaaaaaaa!*

And in the middle of that landscape, which resembled a minor catastrophe, stood an enormous body towering like an iron monument.

At the sight of the monster, its eye glowing with an entirely blood-red light, the people on the ground let out quiet groans.

“Good heavens.”

“Damn it. This old man really has lived a long time. I never thought I’d see something this absurd.”

Jeok Cheongang and Mungyeong stared at the unbelievable scene with stunned expressions.

They had long known that beings called spirit beasts and evil beasts possessed astonishing power, but the sight unfolding before them was far beyond anything they had imagined.

A monster as large as a small mountain.

When it swung its tail, cliffs collapsed. When it roared, the world shook in every direction.

And that was not all. Plants, trees, mountains, and rivers held their breath beneath the baleful aura pouring from it, while lightning and water responded to its fury.

Something that belonged in an old, faded legend was happening in reality.

At that moment, a single thought arose in the minds of the two old masters.

*Supernatural powers.*

Things of the strange, prodigious force, rebellion, and ghosts.

It was exactly what those four characters meant.

Uncanny beings and phenomena beyond the understanding of even two men who had spent most of their lives in the Murim were unfolding before them.

But the words *supernatural powers* did not belong to only one being.

*Kwadeuk!*

The sound of flesh being torn was clearly audible even amid the thunder and lightning.

The next moment, scales drenched in dark-blue blood poured down over Jeok Cheongang and Mungyeong’s heads.

One, two, three…

Soon, dozens of scales began to patter down like a sudden shower.

With eyesight like birds of prey, the two men saw what was happening high above them and were rendered speechless.

“Let’s see the flesh underneath! Let’s see what’s inside!”

“……!”

“……!”

*Kwadeudeudeuk!*

Along with a crazed shout, a young man moved his hands like a madman.

One hand gripped the shaft of his spear with all his strength. The other held no weapon at all as his bare hand seized a scale.

Then he yanked hard.

The scale tore free helplessly, trailing dark-blue blood.

—Kwoooooooooar!

The Mutated Water God Dragon thrashed its enormous body and let out a savage cry, but it was useless.

Whenever it sensed something was wrong, Jin Taekyung darted like a ghost into the empty socket where its eye had melted away. Once the monster’s rampage ended, he popped his head back out and resumed his work.

He even threw in a few furious punches for good measure.

“You fucking bastard!”

*Kwaang! Kwang! Kwajijik!*

The Flame-Extinguishing Divine Fist, one of the five most destructive techniques among the Fire Gate Clan’s various secret arts, combined with strength tremendous enough to call him superhuman.

The monster’s head, nearly the size of an average ship, shook violently, and shattered scales rained down.

—Kyaaaaaaaaaow!

The Mutated Water God Dragon was at its wits’ end.

When it still had its whiskers, it had at least been able to attack.

But now that every last one had been pulled out, it had no idea what to do.

Whenever it thrashed to throw him off, he held on with the spear driven into its flesh. Whenever it seemed to calm down, he emerged and tore off more scales.

What the hell was it supposed to do?

Perhaps because it had smashed its head against the cliff so many times, it was beginning to feel dizzy.

*Kwaang! Kwaaaaaang!*

Mungyeong and Jeok Cheongang could only open and close their mouths as they watched.

*This fucking lunatic…*

*What is he doing? It’s not like he’s pulling a radish out of the ground…*

The two men knew how incredibly strong those scales were, which only made them more shocked.

A sloppy Sword Energy wielded by someone who had just entered the Peak realm could not even cut them properly. Only Force could reliably split the scales and damage what lay beneath them.

The scales were that absurdly hard.

And yet that young whelp had simply smashed them apart and ripped them off.

With nothing but his empty bare hands.

*Did he draw up all of his internal energy? Even so, a human’s physical strength should be nowhere near enough.*

*What the… No, wait. If it’s that bastard, then maybe he can.*

Mungyeong felt as though he were dreaming.

Jeok Cheongang, who had watched Jin Taekyung from Shanxi Province until now, found the whole thing both absurd and astonishing.

“What a goddamn lunatic! Hahahaha!”

It was not enough that Jin Taekyung had torn out every single whisker, one of the monster’s weapons. Now he had begun stripping away its scales too.

For a martial artist, it was like breaking all their weapons and stripping away the armor worn over their martial uniform.

From Jeok Cheongang’s perspective, Jin Taekyung’s current insight into martial arts was clearly inferior to that of both old masters—and even below Cheongpung’s.

But his foundation was entirely different.

*He’s simply strong.*

As a martial artist, Jin Taekyung was a powerful fighter who had reached the Supreme Peak realm.

Yet even without the internal energy and martial enlightenment accumulated over several jiazi, he was strong in his own right.

It was as though the power of the heavens had taken residence inside a human body made of nothing but flesh.

“Is that truly possible?”

There was faint astonishment in Mungyeong’s voice.

Jeok Cheongang laughed with delight.

It was a question he had asked himself countless times while training in the Fire Gate Cavern. And every time, Jin Taekyung had responded with an infuriatingly shameless answer.

Now it was time to give that answer to someone else.

“Yes. The Heavenly Martial Physique.”

“……!”

“You find it absurd and ridiculous, don’t you? Good. Don’t try to understand it too quickly. That bastard has always been like that.”

Just as Jeok Cheongang shrugged, Cheongpung spoke with a determined expression.

“Come on, let’s go too. Mimi! Strike with lightning! Whip up a whirlwind!”

……*Chirik, chiriririk?*

“Oh. You can’t.”

“……Neither can that idiot.”

Just as Jeok Cheongang threatened Cheongpung that if he spouted one more load of bullshit, he would make him drink liquor made from a Thousand-Year Poison Horned Snake, an eerie silence and pressure descended over an area several dozen *jang* wide.

*Gugugugugung!*

Jeok Cheongang, Mungyeong, and Cheongpung felt a chill run down their spines and raised their heads.

*Goooooooong.*

A ripple passed through the air.

By then, the wind and rain that had been pouring down without pause had stopped.

So had the lightning.

Everything held its breath.

Everyone on the ground saw the monster’s blood-red pupils, which had been scattering red energy, slowly turn pitch-black.

At the same time, its enormous maw slowly opened, revealing cavernous darkness, while a sphere of water churned as though being sucked into its depths.

*What is that?*

A single question flashed through everyone’s minds.

And then, from high above, came a shout.

No—a scream.

“Get out of the way—!”

Before they could even realize that the voice belonged to Jin Taekyung, the three figures shot forward like the wind.

There might have been differences, great and small, between them, but each one was a Supreme Peak master and an experienced martial artist with exceptional instincts in actual combat.

They could not see through the nature of that thing, but they could tell how terrifying the unknown power was.

Their prediction proved exactly right.

*Kwaaaaaaaaa—!*

Along with a deafening roar, the enormous sphere of water shot toward the ground.

* * *

There are many different kinds of monsters.

Some are bipedal, with bodies resembling human beings. Others are beast-type monsters that move and run on four legs like animals, yet are hundreds of times stronger.

Their Intelligence varies just as widely according to their species.

Some are simple-minded and crude but possess such insane physical abilities that they have earned a place among the high-level monsters.

Others, like goblins, hunt in packs and employ tactics such as poison and ambushes, but are classified as the lowest rank because their physical abilities are so poor.

With monsters possessing such diverse traits, arguments are inevitable whenever the topic comes up—both among actual experts and among every fucking know-it-all on the internet.

Even so, when people talk about the strongest monsters, there is one type that everyone names first.

*Dragonkin.*

Beings blessed with both Intelligence and extraordinary physiques.

And the mighty power granted exclusively to them.

*Breath.*

But seriously.

How?

Why?

*Kwaaaaaaaaaah!*

…Why the hell was this bastard using Breath?

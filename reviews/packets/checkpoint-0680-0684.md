# Checkpoint Review — 680–684

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

# Chapters 680–684

## Plot

Jin Taekyung battles the Great Snow Fiend and Black Hand Fist Demon in the Poisonblood Grounds despite severe internal injuries. The Great Snow Fiend reveals that the Southern Heaven Demon Empress ordered Jin captured alive if possible, but Jin rejects surrender and provokes him over his past retreat during the Great Faction War.

Jin exploits Black Hand’s anger to create an opening, but the Great Snow Fiend’s killing attack pierces Black Hand from behind as Jin’s hand strikes through his chest. Black Hand dies, granting Jin enough experience to level up and recover internal energy. Jin’s Fire Dragon Armor then lets him survive the Great Snow Fiend’s continued assault, though his injuries remain severe.

As the duel escalates between Jin’s blue-white flames and the Great Snow Fiend’s ice sword and Yin-Cold Qi, Muyaho unexpectedly ambushes the Great Snow Fiend and disappears into the distance. The Great Snow Fiend loses his right arm, but turns the apparent opening into a counterattack, driving White Flame through Jin’s Fire Dragon Armor and into his chest. With the armor partially destroyed, massive internal injuries worsening, and qi deviation imminent, Jin forces the spear deeper into himself to advance and unleashes his remaining blue-white light-flames against the Great Snow Fiend.

## Continuity

- Black Hand Fist Demon is dead.
- The Great Snow Fiend is the former ruler of Great Snow Mountain and a former Great Faction War participant. He killed the former Zhongnan Sect Leader before fleeing and hiding.
- The Southern Heaven Demon Empress ordered the Great Snow Fiend to capture Jin alive if possible because Jin may become a major future threat.
- Jin leveled up after killing Black Hand, restoring some internal energy but not healing his existing injuries.
- Jin’s Fire Dragon Armor blocked much of the Great Snow Fiend’s ice-sword attack but is now partially destroyed; its automatic repair requires three days.
- White Flame pierced the armor and lodged in Jin’s chest. Jin is bleeding and suffering massive internal and external injuries, with qi deviation imminent.
- Jin drove White Flame deeper into his own chest to force himself forward and struck the Great Snow Fiend with his final blue-white light-flame attack.
- Muyaho ambushed the Great Snow Fiend despite Jin’s order to stay out of the battle, helped sever his right arm, and then disappeared into the distance.
- The Great Snow Fiend lost his right arm but remained capable of fighting when Jin launched his final attack.
- Yohi and Heugung remain captive and alive in the unknown prison; the Southern Heaven Demon Empress has not yet returned.
- Namho’s group remains at the northeastern Nanman border with the detained Han Chinese reconnaissance members and the Yangtze River Channel League’s unidentified arrival. Namho intends to take them to the Central Plains for Murim Alliance and Sichuan sect assistance.
- Jin’s survival, the Great Snow Fiend’s fate, and the consequences of the damaged Fire Dragon Armor remain unresolved.

## Translation Decisions

- Use **Great Snow Fiend** for the newly identified twin-wheel master.
- Retain **Fire Dragon Armor**, **White Flame**, **Fire Dragon Divine Spear**, **Flame Divine Palm**, and **Flamefire Path** as established technique and item names.
- Render 대마불사 as **“a large group doesn’t die easily.”**
- Render 육참골단 as **“Sacrifice flesh to break bone.”**
- Render 막대한 내상 as **“Massive Internal Injury”** in system status text.
- Keep 광염 as **“light-flames”** and 화염 as **“flame”** according to context.
- Preserve the hunter-and-wounded-beast imagery in the Great Snow Fiend’s internal narration.
- Keep Jin’s EXP and level-up references in their game-like register.
- Keep the white-furred attacker unidentified until the source identifies it.

## Durable state

{
  "active_continuity": [
    "Black Hand Fist Demon is dead.",
    "Muyaho unexpectedly ambushed the Great Snow Fiend and then disappeared into the distance.",
    "The Great Snow Fiend lost his right arm but remained capable of fighting.",
    "White Flame pierced Jin's Fire Dragon Armor and lodged in his chest.",
    "The Fire Dragon Armor is partially destroyed and will take three days to repair.",
    "Jin is bleeding and suffering massive internal and external injuries with a risk of qi deviation.",
    "Jin drove White Flame deeper into his own chest to force himself forward.",
    "Jin's final blue-white light-flame attack struck the Great Snow Fiend."
  ],
  "continuity_sources": [
    684
  ],
  "open_questions": [
    "Will Jin survive the White Flame wound, massive internal injury, and risk of qi deviation?",
    "Will the Great Snow Fiend survive Jin's final blue-white light-flame attack?",
    "What will happen to the Fire Dragon Armor while its automatic repair is unavailable for three days?"
  ],
  "safe_through": 684,
  "temporary_decisions": [
    "Render 막대한 내상 as \"Massive Internal Injury.\"",
    "Render 광염 as \"light-flames.\""
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 680

# Chapter 680

In a world flowing sluggishly by.

Blue-white flames surge around my fist, burning every scene that flashes past in an instant as kindling.

The punch I thrust like a cannonball toward the Black Hand Fist Demon’s heart.

The sight of him hurriedly reaching out with his eyes bulging as though they might pop from their sockets at any moment.

The black Force being pushed away helplessly despite that, and the Body-Protecting Qi shattering the instant it touched the flames.

And…

Even the dazzling flash that came slicing through the space beyond them.

KWA-AAANG!

A tremendous roar and vibration.

Everything happened in an instant, and ended just as quickly. Then a blast of hot air swept across the place.

No—the same was true for everything within a radius of several dozen jang.[^1]

Mist born from the heat and steam of Scorching Yang Qi spread everywhere, blocking my view.

Whoosh…

I stood perfectly still and stared into the hazy mist.

At least, I did until a voice drifted out from beyond it.

“What an astonishing display. It is even more impressive than I expected.”

There was a faint note of genuine admiration in his voice. I used Seizing an Object Through Empty Space to pull White Flame back and answered calmly.

“I’m pretty good for my age. I doubt even the Heavenly Demon or Martial God was this good.”

“How arrogant. Still, I will acknowledge it. You possess every right to speak that way.”

“Listen to you going on about rights. You got scared and interfered, so what the hell are you talking about?”

My voice sounded composed, but inside, I was bitter.

*Damn it.*

That flash that had entered my field of vision at the last moment.

If it had not been for the twin wheels thrown by the slender old man, the Black Hand Fist Demon might have suffered severe internal injuries—or died on the spot.

*I knew it was possible…but the timing was too perfect.*

In that brief moment, I had been left with only two choices.

Either finish off the Black Hand Fist Demon at the cost of letting the twin wheels take my head and turn me into a Dullahan candidate, or let him go and save my own life.

Naturally, I had chosen the latter.

I changed the direction of my punch in midair and struck the twin wheels aside. The Black Hand Fist Demon did not even dare try to take advantage of the opening. He hurriedly pulled back.

It had been a brief clash that began and ended in the blink of an eye.

At a glance, it might have looked like we had fought to an even draw. But this was a tremendous loss for me.

After getting a taste of how harshly I could hit him, the Black Hand Fist Demon would face me far more cautiously and thoroughly than before.

An opponent’s carelessness was the greatest weakness of all, but you only got one chance to exploit it.

*At this rate…*

This would not be easy.

No. It had become an incredibly difficult fight.

I felt around for the figure hiding beyond the mist and opened my mouth.

“Our Black Hand. Black Hand, who is fifty years older than me yet learned martial arts through his asshole. Where are you hiding?”

I wondered if he might simply ignore me, but the Black Hand Fist Demon possessed an admirable character and answered my words with complete sincerity.

“…Shut your damn mouth.”

“Is it just me, or is your voice much quieter than before? Did tasting a little fire shrink your balls too?”

“…You bastard. You’re awfully full of yourself just because you caught me off guard once. Do you really think you’ll get another chance like that?”

I let out a quiet laugh.

Considering the Black Hand Fist Demon’s martial prowess, it was not entirely wrong to say I had taken advantage of his carelessness. But that was something a young prodigy might say.

Not an old monster who had lived long enough to rot with age.

“You sound like a fucking idiot even while saying that. Don’t you?”

“You—tearing you limb from limb wouldn’t be enough…!”

“Enough.”

The Black Hand Fist Demon’s shout was cut off by a cold voice.

A slender figure emerged from beyond the mist that still blanketed the area.

Step.

The mud, baked hard by the terrible heat, crumbled like sand beneath the old man’s toes.

He held a wheel in each hand, blades jutting from them like the teeth of gears, and lightly shook his sleeves.

Whoosh…

A cold wind settled over the scorching heat and pushed away the mist blocking my vision.

The scene around us was revealed. The poisonous marshland had been transformed into a desert.

“So this is the Fire Gate Divine Technique I have heard so much about. Impressive. At what stage has it reached?”

The old man’s question was filled with genuine admiration.

I lowered the spearhead and answered.

“Three thousand twenty-five stages.”

“Is it my imagination, or does that seem like a ridiculous number?”

“The realm of martial arts has no end.”

“A foolish question met with a wise answer. The Fire King raised his Disciple well.”

“He did raise me well, didn’t he? But why did your parents raise their child like this?”

A killer parent insult, right on the inside corner.

But the old man did not so much as waver.

“I suppose I shall ask them if I ever have occasion to visit the realm of the dead.”

Step.

He advanced as though he were taking a leisurely stroll.

I measured the distance between us and answered.

“Since we’re on the subject, why not go visit them today?”

“Unfortunately, I doubt I will be going anywhere near there for some time.”

“You shouldn’t put things like that off. How angry must your parents be in the Nine Springs? They worked themselves half to death raising you, and now you won’t even visit.”

“This time, you have guessed wrong. I am an orphan with no family in this world. I received no one’s care, so I have no reason to be called an unfilial son.”

Step.

That was his third step.

Muyaho, who had gone from a majestic White Tiger to Poppy after a botched pet-grooming job because the twin wheels had shaved off his fur, let out a low growl.

I watched the twin wheels slowly begin to spin in the old man’s hands and muttered.

“Then you won’t be able to ask them why they raised you like this even after you get to the Nine Springs. You don’t know what they look like, after all.”

“Now that you mention it, that is true. Thank you for the advice.”

“Then what about that idiot sneaking along behind you?”

The Black Hand Fist Demon spat out a brief curse, and the old man answered calmly.

“Black Hand. That friend is in a similar situation.”

“I’m asking because I’m genuinely curious. Is that a requirement for joining Dark Heaven? Or is it some kind of trend?”

The old man did not answer. Instead, he took another step.

Step.

At that moment, the unusually clear sound pierced my ears.

I saw it.

The blue radiance pouring from the twin wheels in the old man’s hands.

Hiss! Whoosh!

Two streaks of light flew toward me with faint sounds of splitting air.

The twin wheels flew in grotesque, unnatural movements like living snakes.

And beneath them, the Black Hand Fist Demon came charging forward, his eyes gleaming with madness.

SHWAAAAAAK!

The attack began from two directions.

No—from three directions at once.

“GRAAAH!”

Along with the roar of the White Tiger exploding behind me, I swung White Flame’s spearhead down with all my strength.

KWAANG!

A violent rebound traveled through me with the deafening impact.

I knocked one of the twin wheels away, then felt wind blowing in from my blind spot and turned my head.

Whoosh—shhk!

It had missed by no more than a hair.

As hair sliced apart by Force scattered through the air, the Black Hand Fist Demon, who had already rushed to within three jang of me, shook his tattered sleeves.

“Youuu!”

Rumble-rumble-rumble!

Palm Force erupted from his wide-open hands and shook the space around us.

I gently thrust the spearhead toward the black Force rolling over me like a wave.

Fire Dragon Divine Spear. First form.

Fire Dragon’s Single Tail.

Fwoosh—shaaaa!

Blue-white flames surged.

The tail of the fire dragon tore through the black Palm Force and shot forward without hesitation. The Black Hand Fist Demon, astonished, twisted his body with a startled cry.

Shhk!

A sharp cutting sound.

But unlike me, the Black Hand Fist Demon did not get away with losing only a few strands of hair.

Blood dripped from the blunt tip of his nose, sliced away without him realizing it.

“You—you dare…”

I knew it for certain now.

Even if we fought ten more times, the Black Hand Fist Demon could never defeat me.

The pride of that ancient monster, along with the anger buried in his heart, had numbed his reason.

That tiny crack was an opportunity for me.

*Now.*

Flash!

One step.

The distance of several jang between the Black Hand Fist Demon and me vanished in an instant, and more than ten possible movements flashed through my mind.

Choosing one of them was easy.

Whoosh!

From the heavens to the earth.

Blue-white flames rose along the spearhead as it slashed downward with a faint sound of splitting air.

Fire Dragon Divine Spear. Second form.

*Heavenly Strike.*

Fwoosh—KWA-AAANG!

A snowball grew larger the farther it rolled, and a current became a wave when more water joined it.

The Black Hand Fist Demon looked up at the streak of flame cutting across the air, and his eyes flew wide.

“Guh…!”

With a startled cry, he raised both palms.

The Palm Force he desperately dragged upward collided with the flames and faded away.

In that brief moment, blue flashes flew in from the left and right.

SHWIIIIING!

His neck.

And his chest.

This was an attack that could not be avoided through movement alone.

With a split-second decision, I twisted the spearhead aimed at the Black Hand Fist Demon and swung it.

KWAANG!

Even someone like me couldn’t overcome the verdict contained in those four characters: *force majeure*.

SHRAAAK!

The tremendous rebound made me lose my balance and sent me helplessly sliding backward.

At that moment, someone’s pale figure rushed in like a ghost.

Shrik!

There was no word.

Not even a breath.

Until now, the old man had done nothing but throw twin wheels from the rear. But now, with a cold and composed demeanor—and with precise speed and flow—he began his own battle.

Just as he did now.

SHWAAK! THUD!

It was hot.

And cold.

Even though I twisted my body at the last moment, the result did not change much.

Finger Qi erupted from the tips of fingers long and withered as tree branches and pierced my shoulder.

The White Flame spearhead moving toward the old man lost its direction and wavered.

And avoiding the weakened spearhead was far too easy for the old man.

Whoosh!

The spearhead passed pointlessly through empty air.

I clenched my teeth, straightened my body, and opened my remaining hand.

At the same time, flames roiling with heat surged from it as I thrust my palm toward the old man’s chest.

Fwoosh—whoooom!

The Flame Divine Palm advanced while burning everything in its path.

The old man’s eyes reflected the flames.

An indescribably intense heat that continued to burn without pause.

But when I saw that the old man’s eyes remained cold, I felt an inexplicable chill.

*This is…*

An unease whose source I could not identify.

And the ominous instinct that seized my entire body soon revealed itself as reality.

Sss…

Within that brief moment, split into even smaller fractions of time, the old man slowly extended his hand.

No.

He was not the only thing moving slowly.

My palm advancing toward his chest was moving slowly as well.

So were the Black Hand Fist Demon and the White Tiger, each charging in from behind one of us.

And…

Along with the cold energy flowing from the old man’s wrinkled hand, the time that had stopped began to move again.

KRAK! SHHHHTZZZ!

At last, our two palms met.

Blue-white flames collided and mingled with pure-white cold.

KRRRUMBLE!

Everything was burning hot.

And freezing cold.

Two lights of different colors flashed relentlessly before my eyes, while unprecedented internal energy shattered and shook everything around us.

Rumble-rumble-rumble!

A roar like heaven and earth splitting apart.

And then I saw it.

At the same time, I heard it.

“My introduction came rather late.”

The powerful Yin-Cold Qi pressed down on the flames as they slowly died away.

“I am called the Great Snow Fiend.”

The cold voice drifted through a cloud of pure-white breath.

KRAAASH!

[^1]: A *jang* is a traditional Korean unit of length, roughly three meters.
## Chapter artifact 681

# Chapter 681

For an instant, a thought crossed my mind.

*What if the Black Hand Fist Demon hadn’t been there? What if I had avoided the Finger Qi?*

*What if the pain hadn’t risen from the shoulder pierced by the Finger Qi at the exact moment our palms met?*

*What if I had known that my opponent’s martial arts were based on Yin-Cold Qi?*

*If—if things had gone that way…*

*Who would be standing here by now?*

But I was given no time to find the answer to those questions.

KRAK!

The frozen flames died away, and the Yin-Cold Qi that had swallowed even the flames swelled as though it might burst.

Beyond the unprecedented internal energy that shook the surrounding space, someone’s hand, engulfed in pure-white light, pressed against my chest.

Tap.

At that moment, only one thought filled my mind.

*Cold.*

KRAAANG!

A storm of cold energy swept in every direction.

What struck me at its center was a fierce wind battering my entire body, the scenery flashing past at incredible speed, and an immense force of recoil transmitted through my back.

KRRRUNCH!

Trees. Rocks. Grass.

And even some unknown creatures unfortunate enough to be caught up in it.

It did not matter whether they had been alive or dead.

Everything my body collided with as it was flung backward like a misfired shell was bent, shattered, and blown apart.

However, the fact that a thick stone wall stood across the middle of that path—one over which I had not possessed the slightest control—was both unfortunate and fortunate.

KWAANG! RRRUMBLE!

Even through the haze, I could feel the excruciating pain.

The scenery that had whipped past my vision every moment finally stopped. But so had I, after being flung several dozen jang[^1] and embedded deep inside the stone wall.

*Goddamn it.*

The voice I squeezed out with all my strength never made it past my lips.

The world was red and blurry, while a constant ringing filled my ears.

BEEP! BEEP! BEEP!

Even for tinnitus, that was a little unusual.

“…Fuck.”

I raised my head with a hollow mutter.

More than a dozen holographic windows floated in the air, accompanied not by the clear bell tones I was accustomed to, but by warning sounds signaling danger.

*I really got the shit kicked out of me.*

A bitter laugh escaped me.

Pain kept surging from every injury.

My hands and feet trembled from the Yin-Cold Qi that had invaded my body, making a mockery of my realm of Unaffected by Cold and Heat.

*I have to get up. I have to fight again…*

But unlike my wishes, my body—as if all its screws had come loose—refused to listen.

I was cold.

And tired.

If I closed my eyes right now, I felt as though I could sleep soundly for the first time in a long while.

Yes. If I slept until my back hurt, with no dreams and no one to wake me, everything would have gotten better.

By the time I woke up, the pain assaulting my entire body would be gone, and this goddamn body that refused to listen would be fine again. Then, as I wriggled beneath a warm microfiber blanket and looked at my smartphone, I would hear Mom’s voice through the crack in the door.

—Jin Taekyung, Jin Hayeon. I’ve set the table, so come out already.

Then I would stagger to the kitchen and prepare the meal, setting out spoons and side dishes on the empty table despite what I had just heard her say.

All while breathing in the savory scent of soybean-paste stew wafting from beyond Mom’s shoulder as she stood with her back to me.

*Ah. This is nice.*

Just thinking about it brought peace to my heart.

The corners of my mouth rose without my realizing it, while my eyelids kept sinking lower.

Sss…

Something rough and damp brushed across my face.

When I slowly opened my eyes, the first things I saw were sharp teeth and clear blue-white eyes.

—Whine.

At the sight of the White Tiger whining like a puppy the moment our eyes met, a quiet laugh escaped me.

“…Was it you?”

—Whine. Whiiine.

Although I could not understand him, I could feel it clearly enough—the meaning contained in those cries, and what he wanted to tell me.

“Phew.”

Pain came with my breath.

It felt as though I had awakened from a long dream. The thoughts that had flashed through my mind had been long, but the moments I had passed through had been brief.

Broken stone dust rained down over my body, buried deep inside the stone wall whose thickness I could not even estimate.

Only a few seconds had passed since I took the blow.

There was still time.

Thud.

With a hand trembling from the cold, I pressed it against the ground and muttered,

“Stop crying. I’m not dead yet.”

It was an answer for him, but it was also something I said to myself.

That was right. I was not dead yet, and even if my flame had briefly gone cold, it could flare up again and again.

Just as it was doing now.

Fwoooosh.

The internal energy drawn up from my lower dantian heated hundreds of acupoints before spreading throughout my limbs and bones.

As I temporarily sealed my insides, thrown into disarray by my internal injuries, a searing pain swept over me, and something surged up in my throat.

Cough!

Dark red blood spilled from between my lips, but I paid it no attention.

That was dead blood.

In other words, blood that had already been rendered useless.

And the substance that had been gnawing away at my body and interfering with the flow of my internal energy was covered in pure-white frost the instant it touched the ground.

Fsssh.

Yin-Cold Qi.

And not merely Yin-Cold Qi, but an extreme form of it unlike anything I had ever seen.

During the Shaolin Bloodshed, the Yin Freak—one of the Yin-Yang Twin Freaks who had led Dark Heaven’s martial artists in a surprise attack on Shaolin Temple—had not possessed anything like this.

“…Yeah. So that’s how it is.”

After muttering under my breath, I rose without hesitation.

Tududuk.

At my sudden movement, leaves and stone dust that had clung to various parts of my body fell away, and a dull pain rose through me.

But in contrast, a new warmth filled my insides.

The hand that had been trembling from the cold and my blurry vision had both improved enough for me to recognize the two figures slowly drawing near.

Step.

Footsteps slowly crossed the Poisonblood Grounds, which had changed from a swamp into a desert, and from a desert into frost-covered land.

The Black Hand Fist Demon followed several paces behind, wearing a triumphant expression, but my gaze was fixed on only one person.

*That damn old man.*

And just as I held White Flame at a slant and stared at the old man walking leisurely as if admiring a landscape painting he had created himself, he suddenly spoke.

“Unexpected. I was certain that would leave you unable to move.”

The old man had spoken without warning.

No, I knew his sobriquet now, too. Though perhaps it would be more accurate to say I had remembered it.

“That might be true for old men like you, Great Snow Fiend.”

“Youth is a fine thing. But why do you not understand? In a situation like this, it will only make things more painful.”

As he had until now, the Great Snow Fiend answered without the slightest wavering and continued.

“The fight is already over. If you surrender obediently now, I will spare your life. This is the first and last offer.”

“Senior! What are you talking about?”

Naturally, that was not me.

At the Black Hand Fist Demon’s protest, his face twisting violently, the Great Snow Fiend shook his head.

“The Demon Empress gave me that order herself. If I let the bastard live, he will become a great source of trouble in the future, but she told me to capture him alive if possible. And the upper hand is already ours.”

“Even so…”

“Shut your mouth.”

“…”

“I know how you feel, but this is Heaven’s business. If you question me again, I will not forgive you.”

His aura and tone were as cold as a blade of frost.

No matter how half-mad the Black Hand Fist Demon was, continuing to resist would be insanity.

“This fucking…”

The Great Snow Fiend casually ignored the mutter that slipped between the Black Hand Fist Demon’s clenched teeth and held out a hand toward me.

“It is foolish to continue a fight whose outcome is obvious. Surrender instead and live to fight another day. If you do, the Fire Gate Clan and the Jin Family of Taiyuan will be allowed to preserve their lineages.”

I stared at the Great Snow Fiend and answered.

Not with words, but with action.

Whoosh!

A sharp sound of air splitting rang through the air.

The Great Snow Fiend moved exactly half a step and avoided my spear strike before speaking calmly.

“I believe I made myself clear. This is the first and last offer.”

“So?”

“I thought you were fairly clever, but you have chosen the foolish path in the end. Can you not feel that the upper hand has already shifted?”

“The upper hand.”

I muttered the words and continued.

“Honestly, I do want to live. But I’m not the kind of bastard who surrenders or runs away just because things have tilted a little. Unlike some people.”

The Great Snow Fiend paused for a moment, then gave a small nod as though he had realized something.

“You know me.”

“I’ve heard of a sobriquet or two. White Rice Cake, Great Snow Fiend, something like that.”[^2]

“A sobriquet like mine is not something a child like you could easily have heard… Fire King Jeok Cheongang. Did your master tell you?”

“Then do you think the fucking Heavenly Demon told me?”

I shrugged and continued.

“He told me that if I ever met some bastard using twin wheels and Yin-Cold Qi, that bastard would either be the Great Snow Fiend or his successor. He also said it was unfortunate that he never got to kill you with his own hands, because you killed the former Sect Leader of the Zhongnan Sect and disappeared without a trace.”

“I feel the same regret. If this old man had met your master during the Great Faction War, I could have killed the Fire King and made my name resound throughout the world.”

“At best, you’d have been the Ice God instead of the Great Snow Fiend, you fucking idiot.[^3]”

[^3]: “Ice God” (*bingsin*) puns on *byeongsin*, a harsh Korean insult roughly meaning “fucking idiot.”

“…”

For the first time, he reacted.

It was faint, but the Great Snow Fiend’s brow definitely furrowed.

A quiet laugh escaped me.

“So you do have some pride after all. Then again, seeing as you ran away back then, maybe you don’t have any at all.”

“I merely lived to fight another day. This old man is not foolish enough to risk his life when outnumbered.”

In fact, based on what I had heard, the Great Snow Fiend’s judgment at the time had been cold but appropriate.

He had killed the former Sect Leader of the Zhongnan Sect, thrown the chain of command into chaos, then used the confusion to escape from Great Snow Mountain and vanish without a trace.

But…

“So what?”

“What?”

“In the end, you just ran away because you were scared. Because you didn’t want to die. Because you were afraid of death. That’s why you stayed hidden for so long.”

“You bastard.”

“It’s not like I’m criticizing you. I don’t want to die either. But once you’ve lived that many years, you should be honest every now and then—even about the things you don’t want to admit. Don’t you think?”

Deep furrows appeared on the Great Snow Fiend’s brow.

At the same time, powerful Yin-Cold Qi rose and pressed down on the surroundings.

“I heard you well. If I meet your master in the future, I shall deliver your last words to him.”

*Last words.*

*Maybe that’s how it will be.*

I took a deep breath.

My opponent was no ordinary nobody.

Moreover, facing two Supreme Peak masters while suffering from internal injuries was little different from committing suicide.

Death?

Naturally, I was afraid.

Ever since becoming a Hunter, I had always feared death. The same was true even after coming to the Murim.

But…

Now that I had taken one step toward accepting the word *death* in my heart, I was different from before.

*I can do anything. Anything.*

This was not a fight to survive.

It was a fight to kill.

And because of that, at this moment, I could throw myself forward without sparing my life.

SHWAAAAAK!

[^1]: A *jang* is a traditional Korean unit of length, roughly three meters.

[^2]: The insult riffs on *baekseolgi*, a white Korean steamed rice cake, and the Great Snow Fiend’s sobriquet.
## Chapter artifact 682

# Chapter 682

SHWAAAAK!

As he watched Jin Taekyung charge straight toward him, the Great Snow Fiend muttered inwardly.

*Yes. Come.*

The boy’s three-inch tongue had stirred him for the first time in a long while, but nothing had changed.

He had erased from his mind long ago the fact that his opponent was a green youngster barely twenty, so young he was practically a newborn.

How could he dare to do otherwise? The Jin Taekyung the Great Snow Fiend had assessed was a monster without equal throughout all of history.

The Three Saints and Ten Kings—giants who had already left enormous footprints across the distant history of the Murim—had not reached the Supreme Peak realm until after they were at least thirty.

That made Jin Taekyung all the more astonishing.

Terrifying talent. And an absurdly young age.

Alongside another genius who had inherited Sword Saint Mae Jonghak’s legacy, Cheongpung of Huashan, he was certain to become one of the most dangerous obstacles.

*At the very least, within the next fifty years, he will grow into a monster capable of matching the Martial God and Heavenly Demon. He must be dealt with now.*

The Great Snow Fiend did not know the full reason why his direct superior, the Southern Heaven Demon Empress, had ordered Jin Taekyung captured alive.

But at this moment, he was certain of his own judgment.

*Demon Empress, you are wrong this time. He… is not someone who can ever be allowed to live.*

Along with words that would never reach their intended listener, the twin wheels let out a harsh howl from within the Great Snow Fiend’s sleeves.

WOOOOONG!

Now that his martial arts and identity had been exposed, there was nothing to gain from holding back his strength.

The Great Snow Fiend focused every sense throughout his body and watched Jin Taekyung’s rapidly approaching figure. His eyes flashed.

*Now!*

It happened at that very moment.

SHWING!

The rapidly spinning twin wheels left his wrinkled hand.

SHWAAAAK!

The twin wheels, filled to the brim with extreme Yin-Cold Qi, shot forward, freezing the space around them.

The two blades traced grotesque paths according to the Great Snow Fiend’s will. At the point where they descended, Jin Taekyung had already closed to within three jang.[^1]

KWAANG!

A tremendous roar erupted as blue and white flashes collided.

Fire and ice clashed.

With a single swing, Jin Taekyung knocked the twin wheels away, then burst through the mistlike steam that had settled over the ground.

SHWAAK!

His movement was swift, appearing no different from before.

But the Great Snow Fiend’s sharp eyes had grasped every detail.

*He is only suppressing it for the moment. The aftereffects of his internal injuries are certainly still with him.*

The difference was minuscule, but it was clear.

His movements were subtly disordered compared to before, and his momentum had grown rougher.

In the Great Snow Fiend’s eyes, Jin Taekyung was a wounded beast.

His claws were still sharp, but he was rapidly growing tired.

And the Great Snow Fiend was a seasoned hunter who knew better than anyone how to hunt such a beast.

*At this rate, bringing him down is only a matter of time.*

He even had a hunting dog beside him in the form of the Black Hand Fist Demon.

The dog was not strong enough to sink its teeth into the beast’s neck, but it was savage enough to charge at the beast in place of the hunter.

PAT-PAT!

“Black Hand!”

The hunter moved back. The hunting dog moved forward.

The Great Snow Fiend retreated a great distance, matching exactly the distance Jin Taekyung had advanced, and shouted. In response, the Black Hand Fist Demon charged toward Jin Taekyung.

“Youuu!”

Along with a roar filled with rage, dozens of palm strikes packed with powerful internal energy shot forward.

KRAAAAA!

A wave of black Force surged toward him.

At the same time, the spear in Jin Taekyung’s hand blurred.

SHWAAAAK!

The realm of Supreme Peak, where only the chosen could set foot.

The young monster who had reached that realm at barely twenty thrust out his spear without a moment’s hesitation. Blue-white flames coiling around the spearhead bored into the center of the black wave.

BOOM!

A strike that pierced a single point exactly.

As Jin Taekyung split the wave of Force in half and blasted through it, the Great Snow Fiend swept both hands downward through the air.

At the same time, the twin wheels that had been knocked away by the spearhead and were circling somewhere in the air plunged downward.

SHWIIIIING!

Their movements were like those of living creatures.

Some might have called it Seizing an Object Through Empty Space, or Snake Sword, a technique performed with cords or threads.

Both would have been wrong.

What moved the twin wheels was the Great Snow Fiend’s own will. And the twin wheels, moved solely by the power of his Middle Dantian, contained only one purpose.

*Die.*

A killing intent as cold as ice, directed at one person alone.

The two wheels bent in different directions and descended like flashes of light. At the same time, the Black Hand Fist Demon’s figure shot forward, trailing a savage momentum.

SHWING! SHWAAAAK!

Three flashes arrived at once from three directions.

The Great Snow Fiend looked at Jin Taekyung, standing at the intersection of death, and felt certain.

*If he clashes with the Black Hand Fist Demon like this, he will not come away unharmed. He will retreat. I will use that opening to…*

But at that moment, Jin Taekyung’s movement rendered the Great Snow Fiend’s entire line of thought useless.

PAT!

Jin Taekyung advanced.

He did not retreat even an inch. He did not hesitate.

He swung his spear like lightning toward the twin wheels flying overhead, then dropped one fist like the forepaw of a tiger charging after being driven to the edge of a cliff.

KWAANG! KRRRUNCH!

The Great Snow Fiend saw it all clearly.

THOOM!

Within the tremendous roar that sounded as if the sky were splitting apart and the flash of light that followed, a spear rose over Jin Taekyung’s shoulder.

SHWIIIIK! SHRAK!

And then the twin wheel that slashed across Jin Taekyung’s shoulder like a bolt of lightning, while he clashed with the Black Hand Fist Demon and left the beloved spear that had slipped from his hand behind.

SHRAK! FWOOSH!

Bright-red blood burst out like a fountain, and Jin Taekyung’s figure staggered.

At this wholly unexpected development that had unfolded in an instant, even the normally cold Great Snow Fiend faltered. He could not retrieve the twin wheels buried deep in the stone wall.

*Why would he choose that?*

The Great Snow Fiend could not understand.

If he had been in the same position, he would have chosen to evade without the slightest hesitation.

But his thoughts could go no further.

RRRRUMBLE!

A shock wave burst from Jin Taekyung and the Black Hand Fist Demon, shaking the space around them.

Their fists had met in midair.

Neither could retreat. Neither could advance. Both fists trembled violently.

An even match.

Along with the three words that flashed through his mind, the Great Snow Fiend’s figure blurred.

SHWIK!

Jin Taekyung was exhausted from his successive injuries.

The fact that the Black Hand Fist Demon—despite being a Supreme Peak master like him, clearly a level below—had managed to match him for even a brief moment was proof.

And the Great Snow Fiend was not an inept hunter who would miss an opportunity that had arrived earlier than expected.

*Now is the perfect time.*

Even if it was wounded and bleeding, a beast was still a beast. The hunting dog called the Black Hand Fist Demon could never handle that young beast on its own.

Unless the hunter—the only one capable of tearing out the beast’s throat—stepped forward.

*He must die. Right now.*

The decision made in that split second was cold, and his advancing figure was like a flash of lightning.

FSSSH. With every step he took, the Yin-Cold Qi leaking from the Great Snow Fiend’s entire body froze the air.

He crossed more than twenty jang in only three steps and shot forward. Over the Black Hand Fist Demon’s shoulder, he saw one person.

*Jin Taekyung.*

He could see him. He could sense him.

Haa. Hah.

Ragged breathing and a pale face.

The upper half of his body, where the twin wheel had skimmed him before moving on, was drenched in bright-red blood. The eyes of the beast that had discovered the hunter rushing right up to him trembled faintly.

*My judgment was correct.*

Certainty filled the Great Snow Fiend’s cold, composed gaze.

Blazing Flame Divine Dragon Jin Taekyung.

The heir to the Fire Gate Clan. The successor of the Fire King Jeok Cheongang.

The Divine Dragon of the Central Plains, who would one day become a new Martial God and look down upon the world, would die before he ever rose above the clouds.

Right here.

Today.

The time for the hunt had finally arrived.

Ssssss.

The wind blew.

It carried cold into the air and earth that had briefly heated to a fever, and it would cover the mountains, rivers, plants, and trees with frost.

It was a snow wind that planted despair in one person and hope in another.

*He’s here. He came!*

The Black Hand Fist Demon barely managed to suppress the cheer trying to escape between his lips.

He had never liked the Great Snow Fiend.

No. Considering the attitude the Great Snow Fiend usually showed him, even that description was generous.

The condescending way he spoke, as though addressing a slave. The way he looked at him as if he were far beneath him.

If his martial arts had been strong enough, he might have killed the man long ago without alerting the Southern Heaven Demon Empress.

But in a situation like this, the Great Snow Fiend’s presence was worth a thousand troops.

The Black Hand Fist Demon watched Jin Taekyung hurriedly try to pull away and smiled with madness.

*You bastard disciple of the Fire Gate Clan. Even tearing you apart limb by limb wouldn’t be enough. You will never escape.*

KRRUNCH!

In that instant, a hand spread like a hook wrapped around Jin Taekyung’s fist just as it was about to fall.

It was a grappling technique the Black Hand Fist Demon had practiced for as many years as his fist technique.

ZZZT. The heat was like lava, hot enough to make both his hands seem ready to burn, but the Black Hand Fist Demon did not care.

A single moment would be enough.

Then both this pain and Jin Taekyung’s life would come to an end.

The Black Hand Fist Demon looked into Jin Taekyung’s wide-open eyes and shouted as though cheering.

“Senior!”

Before the Black Hand Fist Demon’s shout had even ended, the Great Snow Fiend answered his call.

He drove an ice sword created solely from extreme Yin-Cold Qi into the Black Hand Fist Demon’s back.

SQUELCH!

“……!”

In the slowed world, a single sound of tearing flesh rang out, and the Black Hand Fist Demon’s body stiffened with a jolt.

But to the Great Snow Fiend, the hunting dog’s reaction after completing its mission was irrelevant.

His cold gaze was fixed on only one place: Jin Taekyung’s eyes, wide with pain and shock.

Or at least, it should have been.

Just as the former Sect Leader of the Zhongnan Sect had been, when the Great Snow Fiend encountered him long ago on Great Snow Mountain.

Just as the Black Hand Fist Demon, who had already met his death, had been.

Jin Taekyung should have been pierced and killed by the ice sword filled with powerful Yin-Cold Qi.

But…

*What is this?*

The Great Snow Fiend’s gaze, frozen as though it could not move, trembled.

His eyes slowly lowered.

There, he saw someone’s hand pressed against his chest.

At the same moment the Great Snow Fiend thrust out his ice sword—no, a fraction of a moment before it—the hand that had pierced through the Black Hand Fist Demon’s chest was red, yet blue, and blue, yet dazzling.

FWOOSH.

It was hot.

Hot enough to burn flesh and bone, even the soul inside the body.

As he gazed at the blue-white hellfire burning while drenched in blood, the Great Snow Fiend muttered in a voice that seemed to boil.

“How? How did you…?”

The next moment, Jin Taekyung’s calm voice pierced his ears.

“You should’ve stabbed a little higher. Unless you were trying to give me EXP.”

What?

The Great Snow Fiend wanted to ask again, but Jin Taekyung did not allow him to.

BOOM!

Beyond the terrible heat that seemed to burn through his entire body, the Great Snow Fiend saw it.

*That…*

The Black Hand Fist Demon’s collapsing body.

And an unidentified red armor draped across Jin Taekyung’s upper body.

KRRRUNCH!

[^1]: A *jang* is a traditional Korean unit of length, roughly three meters.
## Chapter artifact 683

# Chapter 683

BOOM!

The heat coming through his chest was scorching.

KRRRUNCH!

An immense impact swept through his entire body like a wave.

“Cough.”

It was an agony he had not felt in a very long time.

His once-clear vision grew hazy, and dark-red blood burst between his parted lips.

But what tormented the Great Snow Fiend, who had been hurled through a massive ten-thousand-geun boulder, was neither the pain nor his internal injuries.

*He read my move? That little blood-soaked brat?*

The unbelievable reality that the strategies he had used to reach this point—after defeating countless powerful enemies—had been outmaneuvered by a young man barely twenty made the Great Snow Fiend's head spin.

*My judgment was certainly correct.*

He muttered the words blankly inside his mind, then shook his head.

No. That was wrong.

It was not that his judgment *should have* been correct.

It had unquestionably been correct.

The reason he had survived this insane Murim, at the intersection of countless lines of death, was not merely his formidable martial arts.

Hide yourself. Know your opponent.

If the Supreme Peak martial arts dwelling within the Great Snow Fiend were a sharp sword, then his unwavering composure and cold judgment were both a shield and a hidden weapon.

But this…

This was the first time.

The first time he had encountered an opponent who did not fall when cut by a sword, was not stopped by a shield, and could not be brought down even by a hidden weapon.

An existence so far beyond every one of his judgments and certainties.

*How?*

With that one unanswered question, the Great Snow Fiend lifted his trembling eyelids and looked straight ahead.

FWOOSH.

The fiercely whirling snow wind subsided. The frost-covered ground began to melt, and the white breath spilling into the air grew tinged with bitter heat.

At the center of it all stood a single person.

Step.

Footsteps rang through the silent space, and a figure emerged through the hazy steam, appearing in the Great Snow Fiend's eyes.

A man drenched in blood from head to toe.

And yet, in stark contrast, his pair of eyes was clear and bright.

As the young man slowly approached, the Great Snow Fiend pushed himself upright.

PATTER. PATTER.

Stone fragments fell from his body, bringing fresh pain with them. He clenched his teeth and suppressed his internal injuries before spitting out a name.

“…Jin Taekyung.”

His voice was as cold as his muddled mind.

But Jin Taekyung's answer was utterly calm.

“I'm surprised. I thought you wouldn't be able to move after that.”

“What?”

“Old man, you've still got plenty of energy. But that isn't a good thing in a situation like this. It only makes things more painful.”

The Great Snow Fiend's eyebrow twitched as he realized something.

“…You.”

“Oh. It doesn't mean anything. I think someone said something similar to me earlier, so I just repeated it. Looking at things, it can't have been more than… fifteen minutes ago. I can't remember what idiot was running his mouth, though.”

Jin Taekyung muttered under his breath, “Young-onset dementia, maybe,” then glanced over his shoulder and sighed.

“Ah. If I don't figure this out, I might not be able to sleep tonight. That old man lying over there might know, so would it be okay if I went and asked him?”

“……!”

“I'll be right back, okay?”

It was utter nonsense.

Asking a corpse whose heart had already been crushed a question was impossible. So was receiving an answer from it.

It was blatant mockery. Not worth listening to.

And yet, the Great Snow Fiend bit his lip without realizing it. Under normal circumstances, he would not have reacted at all to such nonsense.

But not now.

“Just what… are you?”

It was a single question filled with genuine confusion.

The Great Snow Fiend truly wanted to know.

How could Jin Taekyung still be standing on his own two feet at this moment? Why had he not fallen together with the Black Hand Fist Demon?

“I saw it clearly with these two eyes. It was neither an illusion nor some clumsy act. How… how could you have done that?”

There was not a trace of falsehood in the Great Snow Fiend's words.

There was no mistake.

Jin Taekyung's qi and blood had been thrown into chaos by the powerful Yin-Cold Qi, and he had even been cut by the Force-wreathed twin wheels.

That was why the Great Snow Fiend had been certain until the very last moment.

With the ice sword in his hand, he could kill both the wounded beast and the hunting dog.

Even the Great Snow Fiend's decision to kill the Black Hand Fist Demon had been born from the single thread of caution held by an experienced hunter.

A beast driven to the edge of a cliff could do anything.

But…

He had been wrong.

No. Everything had been turned upside down.

The hunter had failed to kill the beast, and the beast that had sunk its teeth into the hunting dog's neck had clawed the hunter's chest.

Something that could never have happened—and should never have happened—had occurred.

Jin Taekyung gazed silently at the Great Snow Fiend's incomprehending expression and muttered as though speaking to himself.

“Yeah. Maybe it was.”

The meaning behind those words reached a place the Great Snow Fiend could not understand.

Because it was a gamble only one person in this world could have attempted.

*Level Up.*

A single move capable of reversing an overwhelmingly disadvantageous battle.

Jin Taekyung had wagered everything on that one thing. He had willingly offered up his flesh to draw out the enemies' complacency, and at last, he had taken their bones.

*If I hadn't leveled up with the EXP I got from the Black Hand Fist Demon… I'd be the one lying here right now.*

But the gamble that had put his life on the line had succeeded.

On his way to Ailao Mountain, Jin Taekyung had fought more than ten battles and dealt with hundreds of venomous beasts while breaking through the Poisonblood Grounds.

Then he had added the name Black Hand Fist Demon on top of all the EXP he had accumulated little by little.

*And on top of that, the ten points I'd obtained while escaping the underground prison and never used… along with the Fire Dragon Armor.*

He had been forced to suffer an internal injury first because of the Great Snow Fiend's unexpected move.

But that was precisely why he had been able to draw them out at the most important moment.

It had been incredibly close.

But the result was a success.

The punch Jin Taekyung had thrown with every ounce of his strength had taken the Black Hand Fist Demon's life faster than the ice sword could, while the Great Snow Fiend's ice sword had failed to pierce the Fire Dragon Armor completely.

Jin Taekyung suddenly remembered words he had heard from someone long ago.

A man who had truly loved Go. Whenever he lost a game, that man had shouted, “Japs out! Chinks out!”

“Son, Go has a saying: a large group doesn't die.”

“Dad. Is that Buddhist?”

“No, no. A large group—a big formation of stones—doesn't die easily.”

“Oh, I see. But Dad, why did you lose this game?”

“Because the large group died… Honey! Please take Taekyung away! Honey!”

A small laugh escaped him.

His father had been right. A large group did not die easily.

A large group that found a brilliant move at the end of a bad sequence became larger than any other stone and came to dominate the board.

Just like now.

“Black Hand already went ahead, and our Santa Claus needs to go see his parents soon, too. Just so you know, I don't ask people to surrender.”

SHING.

The blade of White Flame, gripped in his blood-soaked hand, pointed at a single person.

The Great Snow Fiend stared at Jin Taekyung with blood vessels burst across his eyes and spoke.

“Do not spout such nonsense. You have gained only a slight advantage. It is not over yet.”

Jin Taekyung did not bother denying it.

At least, the damned old man's claim that it was not over yet was true.

*Sacrifice flesh to break bone.*

The flesh he had given up to take the bone had served its purpose, but the internal injuries he had already suffered, along with the wound from the twin wheels, were too severe to heal with a single level-up.

And just as he had risen again after taking the first attack, the Great Snow Fiend still had plenty of strength left.

“You will die, and this old man will live. That is the natural order—and the mandate granted by Heaven.”

FSSSSSH.

Cold seeped into the surroundings along with his icy voice.

The sight of the old monster remaining upright even after being struck by the Flame-Extinguishing Divine Fist with all of Jin Taekyung's strength made him awaken the fire dragon filling his lower dantian once more.

“Well, I can understand an old man becoming senile…”

FWOOSH.

Blue-white flames rose over the transparent spearhead and drove back the cold. Fire blossomed in Jin Taekyung's eyes, which held a faint warmth.

“But if some bastard from Dark Heaven starts talking about Heaven's mandate, you won't even get to see your parents after you die.”

At that moment—

POP!

Space vanished, and flame and cold collided.

* * *

KWAANG!

The world shook.

The fire spear and ice sword met head-on and released a tremendous roar.

A shock wave powerful enough to shake the earth and sky swept in every direction, but the two figures blown back by the explosion immediately stepped toward each other without giving up even an inch.

SHWIK!

One step.

A single step was enough.

The Great Snow Fiend split the instant apart and whipped his blood-soaked sleeve.

BOOM!

Cold capable of freezing the air itself swept over the thousand-geun boulder buried deep beneath the ground.

*Rock?*

The Great Snow Fiend raised his head at the same time as his realization.

As if there were invisible stairs in the air, Jin Taekyung had stepped on empty space half a beat ahead and leaped upward.

He was falling with his spear, his body and weapon moving as one.

Fire Dragon Divine Spear.

Second Form.

Heavenly Strike.

KRAAAAA!

There was not even time to think.

The Great Snow Fiend instinctively swung the ice sword in his hand upward.

A streak of flame descended like a meteor and collided with the ice sword.

KWAANG!

If it had been fifteen minutes earlier, he would have blocked it without difficulty.

But now, things were different.

Jin Taekyung's attack, backed by fully restored internal energy, was heavier and sharper than before.

No.

The Great Snow Fiend's internal injuries were simply that severe.

*Hngh.*

Blood surged up, and the Great Snow Fiend swallowed it with a groan before changing the direction of his ice sword.

The flames slid across the ground and exploded.

A deafening roar shook his ears as his body was flung backward.

Through his spinning vision, the Great Snow Fiend launched the ice sword toward the approaching figure as though throwing it.

SHWAAK! KWAANG!

Jin Taekyung knocked aside the ice sword that came hurtling at him faster than sound and did not hesitate.

He put strength into the toes planted on the rock frozen by Yin-Cold Qi.

FSSSH. KRRRUNCH.

The ice melted, and web-like cracks spread across the solid surface of the rock.

Then a single streak of flame rose.

KRAAAAA!

“Flamefire Path.”

Jin Taekyung charged forward, blue-white flames wrapped around him.

Toward the Great Snow Fiend.

Toward the old monster who dared to defy the natural order and invoke Heaven's mandate.

*I can do this.*

It was not certainty or complacency.

He was simply trusting himself.

Without even breathing, Jin Taekyung cut through space, wrapped both hands around the spear shaft in a reverse grip, and thrust it straight forward.

SHWAAAAAAK!

The flame-wreathed spearhead grazed past in an instant.

It split the wind.

It set the air ablaze.

And at the end of it…

There was a single person.

“Hah!”

The speed was simply too great.

The Great Snow Fiend released a roar and gathered Yin-Cold Qi in both hands.

A white Force that seemed capable of freezing even the world shot toward the spearhead.

No.

It should have.

It absolutely had to.

Pain came from his back.

Along with a burning sensation, something trailing white fur flashed across the Great Snow Fiend's vision.

The thing that flashed through the old monster's vision as his judgment clouded raced straight onward without slowing.

*Damn it. Baek…*

The Great Snow Fiend swallowed the curse rising in his throat and thrust both palms with all his strength toward the blue-white hellfire filling his vision.

KWA A A A A AANG!

RRRRUMBLE!

A tremendous roar, as though the sky itself were splitting apart, shook the world.
## Chapter artifact 684

# Chapter 684

RUMBLE!

The earth shook with a thunderous roar.

Ancient trees that had taken root so long ago that no one could guess their age. Boulders weighing ten thousand geun.

Even the strange creatures of the Poisonblood Grounds that had been hiding somewhere nearby, silently watching this battle.

Everything was swallowed by the earth as it heaved and overturned like a wave.

KRRRUNCH!

It was hot.

At the center of the shock wave, I felt the scorching wind whipping around me.

There was not a trace of coolness in the muggy air, and the thick cloud of dust covering a radius of dozens of yards allowed me no visibility whatsoever.

Yet I remembered one thing clearly: the old man who had unleashed both palms packed with immense Yin-Cold Qi at the spearhead that had lunged right up to his face.

I also remembered the red blood gushing from his body, and the figure of the White Tiger disappearing into the distance in a flurry of white fur.

*That bastard…*

At the last moment, Muyaho’s sudden ambush against the Great Snow Fiend had not been planned beforehand.

In fact, I had told him to avoid the battle and search for Yohi, who was probably being held captive somewhere in this place.

Even if I died here today, I wanted that clever beast, at least, to escape the Poisonblood Grounds alive.

If he went to the Nanman Beast Palace alongside the two Great Chieftains, there would still be hope of preventing the disasters that would follow.

But Muyaho had ignored my advice, and his reckless, dangerously risky ambush had ultimately succeeded.

*The difference was tiny, but it was clear. The unexpected attack delayed the Great Snow Fiend’s reaction.*

It had been worth sending White Flame—practically an extension of myself—flying.

A hunter who had lost his composure and been wounded was no longer a hunter.

He was nothing more than prey.

*Where are you?*

POP!

With a quiet mutter, I shot forward.

The thick dust cloud winding around me, the soil and stones pouring down from every direction—those things blocked my vision and masked every sign of movement.

I thrust a fist at them.

BOOM!

I did not even need to imbue it with internal energy. The air compressed by the speed that broke the sound barrier and the force that shattered the wind burst outward.

The enormous dust cloud split in two, revealing what had been hidden beyond it.

FWOOSH!

A hot wind swept through the surroundings. The instant I caught a glimpse of someone’s blood-soaked clothes beyond the dust cloud, I reached out without hesitation.

This was the opening I had won after an agonizing struggle.

Now that the scales of the battle had begun to tilt little by little, I could not let it slip away.

Not even if it meant revealing some of the abilities I had yet to show the Great Snow Fiend.

*Inventory Open. Summon.*

Along with the command that rose in my mind, I flung the spear in my hand with every ounce of my strength.

SHWAAAAK! BOOM!

A fierce sound of splitting air was followed by a thunderous roar. But before either sound had faded, another spear was already clutched in my hand.

SHWIK!

Again.

KWAANG!

Again.

*More. More. More, more.*

My body moved at the same instant as my thoughts. I twisted my waist, drew back my shoulder, and sent each spear flying with the weight of my entire body.

They devastated the surroundings like a bombardment.

RUMBLE!

I ignored the dust cloud as it began to rise again after briefly scattering.

I was pouring out attacks even more powerful than that.

Each spear was a cheap iron weapon that could not compare to White Flame, but if even one of those weapons, shot from my hand like a flash of light, struck its target, no one could escape unharmed.

*Even if he’s a Supreme Peak master. No…*

Even if he was the Great Snow Fiend.

BOOM! KWAANG! KRAAA-BOOM!

Explosions and thunderous roars continued without pause. After driving more than ten spears into the ground like bolts of lightning in the span of a moment, I finally saw it.

KRRK! SPLAAASH!

Beyond the thick dust cloud, bright-red blood scattered into the air with a grisly sound of flesh being torn.

There you are.

The instant I was certain, I thrust out my foot.

The tip of my foot, bearing the weight of a thousand geun, dug deeply into the overturned earth.

KRRRUNCH. BOOM!

An explosion occurred at the same time as I compressed my internal energy. I surged forward, erasing dozens of yards of space in an instant, and plunged into the dust cloud.

The noise coming from every direction and the falling debris had already made it impossible to tell front from back.

But my movements as I cut through the space held not the slightest hesitation.

*Because I’ve already seen him.*

My sharp senses detected the metallic scent of blood, and my keen eyesight once again found someone’s back through the dust cloud.

The Great Snow Fiend could not be faster than me after being injured while blocking White Flame.

I summoned a spear from my Inventory and slashed it down diagonally.

SHIIING.

With a low sound of splitting air, blue-white flames rose around the spearhead and slowly cut through the wind.

No. It was not only the spearhead that had slowed.

Extreme concentration paralyzed my brain and brought the world to a standstill.

Within that frozen time, the flame slowly slicing through the dust cloud finally touched the hem of the clothes.

At that instant, a single certainty flashed through my mind.

*It’s over—!*

But why?

Why was I feeling this inexplicable cold and strange sense of déjà vu?

Why was my body trying to retreat, ignoring the command descending from my brain, when moving even one inch farther would end everything?

At the same time, I realized.

It was reason and instinct at once.

And it was instinct that came before reason.

*The Great Snow Fiend.*

An old monster who had crawled up from the abyss of a distant past.

But the reason he was dangerous was not because he was a Supreme Peak master who had opened his Middle Dantian.

What he possessed that the Blood Lord and the Western Heaven Demon Lord did not—

No, what they had not even felt the need to possess because their strength was so overwhelming—

was caution and thoroughness.

Those were the old monster’s sharpest weapons.

*The Great Snow Fiend, this easy?*

No.

At least, the Great Snow Fiend I had faced until now could never have fallen this easily.

In the brief instant that was split into even briefer instants, I twisted my body with all my strength.

My body came to a sudden stop, and the internal energy surging through me like a raging sea reversed course.

A mouthful of hot blood surged up my throat, and the spearhead that had veered away in midair sliced through the clothes.

Then, in the next instant, I saw it clearly.

SHNK.

Within the slowly flowing time, I saw flesh and bone being sliced away like tofu.

Beyond the blood drifting through the air as if it were weightless, I saw disheveled hair fluttering in the breeze.

And beyond the shoulder of the corpse that had already stopped breathing, a pair of cold eyes gleamed.

*I’ll return it to you. Exactly the way you did.*

The instant I felt an inaudible voice speak those words, a painfully cold flash of light burst from the gaping chest of the Black Hand Fist Demon.

SHWAAASH!

I knew instinctively.

I could not avoid this attack.

But I could avoid a fatal wound.

Because covering my upper body right now was the peerless divine weapon I had obtained by killing the Western Heaven Demon Lord.

Fire Dragon Armor.

But…

KRRUNCH! THUD!

It was cold.

And at the same time, it was hot.

The Yin-Cold Qi seeping into my body.

And the spearhead of another divine weapon, White Flame, which broke through the Fire Dragon Armor and lodged itself in my chest.

BEEP. BEEP. BEEEEP!

> **System**
>
> - Part of **Fire Dragon Armor** has been destroyed by powerful energy!
>
> - Time remaining until **Fire Dragon Armor** is automatically repaired: **3 days**
>
> - **Yin-Cold Qi** is violently shaking your insides!
>
> - Status abnormality: **Bleeding**
>
> - Status abnormality: **Massive Internal Injury**
>
> - There is a risk of **qi deviation**! Calm your energy as soon as possible!
>
> - The internal and external parts of your body have suffered severe damage!

…

…

…

My vision grew hazy from the horrible pain. As warning sounds continued to pierce my ears without pause, I thought:

This was truly turning out to be one hell of a day.

* * *

In that brief instant when everything flashed by in the blink of an eye, Jin Taekyung was not the only one who felt that the world had stopped.

The Great Snow Fiend felt the same.

He had been hiding among the dust cloud, waiting for his final opportunity. After enduring the longest and most difficult wait of his nearly century-long life, he could finally exhale the breath he had been holding.

KRRUNCH. THUD!

A spearhead buried in a man’s chest.

A body trembling violently.

Eyes filled with pain and despair.

“Gueeek!”

SPLASH!

Dark-red blood mixed with pieces of internal organs splattered across the Great Snow Fiend’s face.

But the foul metallic smell and rank stench filling his nose did not bother him.

No, what stunned him was the sight of that young bastard still alive.

*What a lunatic.*

The Great Snow Fiend’s plan had been perfect.

It would have been, if Jin Taekyung had not twisted his body at the last moment.

The spearhead had been meant to pierce his heart cleanly. That was why it had become embedded in the vicinity of his chest instead.

*If this old man had not changed the direction of the spearhead along with him… it would have ended at his side.*

The Great Snow Fiend felt a chill run down his spine.

The assessment he had made of Jin Taekyung at the beginning of the battle had long since been corrected.

*Not in fifty years, but thirty. No… perhaps within twenty years, he’ll be able to rival the Martial God and the Heavenly Demon.*

A talent that could only be called monstrous.

A determination more ferocious than fire.

This was not a question of martial arts. It was a powerful strength that came from the man himself—a momentum that went beyond danger and inspired fear.

In the Great Snow Fiend’s eyes, Jin Taekyung was already a powerhouse.

He was in no way inferior to the masters of the Nine Sects and One Gang or the Five Great Families.

No, even when compared to the Ten Kings, he did not fall short in the slightest.

But—

*Even you end here.*

GRIND.

The Great Snow Fiend gritted his teeth and tightened his grip on the spear shaft.

His right sleeve hung empty, as though something had torn away the arm inside it. The arm had been sacrificed to the White Tiger’s ambush and the spear that came crashing down immediately afterward.

But he had no regrets.

He had lost an arm as precious as his life, but the uncanny sorcerers of Dark Heaven would surely find some solution without much difficulty.

What mattered to him now was the fact that he could finish Jin Taekyung—that terrifyingly tenacious monster.

*Did I not tell you? You will die, and this old man will survive. That is the natural order, and the mandate granted by Heaven.*

With fear and rapture mingling across his face, the Great Snow Fiend gathered what little strength remained to him.

At the same time, the cold spear shaft made of Ten-Thousand-Year Cold Iron drove deeper into Jin Taekyung’s chest.

KRRUNCH!

The spearhead, steeped in cold rather than flame, bored into its owner’s chest.

Along with the dreadful sound of flesh being split and bone being crushed, Jin Taekyung’s body jerked violently.

PFFT. SPLAAASH!

Blood spurted upward like a fountain, and his eyes slowly grew dim.

The Great Snow Fiend had watched countless deaths. He had never been more certain.

*Now no one can save him. Not even if the Great Firmament Immortal himself comes—not merely the Divine Physician.*

But the Great Snow Fiend had momentarily forgotten.

The young man dying right before his eyes was an existence akin to supernatural powers—something that could not be predicted by his judgment.

GRAB. THRUST!

The Great Snow Fiend was given neither the time nor the strength to respond.

Reflected in his astonished eyes was the sight of one man.

Jin Taekyung had seized the spear shaft with all his strength and driven it even deeper into his own chest.

Then he forced himself forward.

And in his blood-soaked hand, the final flame was burning.

“……!”

Blue-white light-flames spread across the Great Snow Fiend’s widened eyes.

FWOOSH—KWAANG!

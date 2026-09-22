# Checkpoint Review — 675–679

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

# Chapters 675–679

## Plot

Jin Taekyung follows Yohi’s tracking scent back to Ailao Mountain, rescues information from a captured Nanman chieftain, and learns that Baeksang has become temporary Palace Lord while mobilizing Nanman against the suspected traitors. Jin and Muyaho enter the Poisonblood Grounds, where they discover that Yohi and Heugung are imprisoned by Dark Heaven agents.

Black Hand tortures the captives and admits that Dark Heaven manipulated the Yao succession and orchestrated the Western Yao Estate killings. He and an unnamed slender Supreme Peak master, wielding twin wheels, confront Jin while awaiting the Southern Heaven Demon Empress’s return. Jin awakens the fire dragon in his dantian and begins fighting both masters, protecting Muyaho as the battle escalates.

Meanwhile, Namho and the surviving reconnaissance squad reach Nanman’s northeastern border with Yayul Mok and the detained Han Chinese members. They infer that Baeksang and Dark Heaven may have used the Blood Monk to eliminate the Beast Miao King’s loyalists. Namho plans to escort the Han Chinese to the Central Plains for Murim Alliance aid, but the Yangtze River Channel League’s swift ship arrives unexpectedly, carrying an unidentified person. Jin counters the twin wheels and Black Hand Fist Demon with the Flame-Extinguishing Divine Fist.

## Continuity

- Baeksang is Nanman’s temporary Palace Lord and has ordered a general mobilization; nearly ten thousand troops occupy the Inner Palace, while the Miao people remain under surveillance.
- The Beast Miao King sent Yayul Mok and the others to the underground prison after choosing to stake Nanman’s fate on keeping faith with Jin and Baeksang. His survival and the fate of his loyalists remain unresolved.
- Jin and Muyaho are inside the Poisonblood Grounds, fighting Black Hand Fist Demon and an unidentified slender Supreme Peak master who uses twin wheels.
- Black Hand Fist Demon admits responsibility for the Western Yao Estate killings and confirms that Yohi and Heugung are alive but captive.
- The Southern Heaven Demon Empress is absent from the battlefield and is expected to return for Yohi and Heugung; her agents consider Jin a major future obstacle.
- Heugung is severely injured and unconscious; Yohi’s internal energy remains sealed. Both are chained in the unknown prison.
- Muyaho’s fur has been cut by a twin wheel, though he remains beside Jin. Jin has temporarily discarded White Flame and is using blue-white flames with the Flame-Extinguishing Divine Fist.
- Namho’s group has reached the northeastern border. The Han Chinese prisoners are unharmed, with their Sleep Acupoints struck.
- Namho intends to take the Han Chinese to the Central Plains so the Murim Alliance and Sichuan’s major sects can aid Nanman; the journey is expected to take seven to ten days.
- The Yangtze River Channel League’s swift ship has arrived directly at the group’s position, and an unidentified person has stepped ashore.
- It remains unknown who the slender Supreme Peak master is, whether Jin and Muyaho can survive the two-master battle, and whether reinforcements can arrive before Nanman is overwhelmed.

## Translation Decisions

- Use **temporary Palace Lord** for 임시 궁주 and **Inner Palace** for 내궁.
- Retain **Black Hand** for 흑수 and use **Black Hand Fist Demon** for 흑수권마.
- Render 쌍륜 as **twin wheels**.
- Use **Chief Jang** and **Chief Go** for 장 족장 and 고 족장.
- Retain **swift ship** for 쾌조선.
- Use **Flame-Extinguishing Divine Fist** for 멸염신권.
- Preserve Jin Taekyung’s abrupt register shifts, profanity, and deliberate psychological provocation.
- Preserve Black Hand’s archaic, sadistic voice and the slender master’s cold, formal command.

## Durable state

{
  "active_continuity": [
    "The Beast Miao King sent Yayul Mok and others to the underground prison after choosing to stake his fate on keeping faith with Jin Taekyung and Baeksang.",
    "Namho believes Baeksang and Dark Heaven have likely seized the Inner Palace and may have intended the Blood Monk to eliminate the Beast Miao King's loyalists.",
    "The Han Chinese members of the reconnaissance squad are detained without harm, with their Sleep Acupoints struck.",
    "Namho plans to escort the Han Chinese to the Central Plains so the Murim Alliance and Sichuan's major sects can aid Nanman, a journey expected to take seven to ten days.",
    "The Yangtze River Channel League's swift ship has arrived unexpectedly at the reconnaissance squad's position, and an unidentified person has stepped ashore.",
    "Jin Taekyung is fighting the Black Hand Fist Demon and an unidentified twin-wheel Supreme Peak master in the Poisonblood Grounds.",
    "Muyaho's fur was cut by a twin wheel while Jin protected him.",
    "Jin has discarded White Flame temporarily and is launching the Flame-Extinguishing Divine Fist with blue-white flames.",
    "Yohi and Heugung remain captive and alive, awaiting the Southern Heaven Demon Empress's return.",
    "The Southern Heaven Demon Empress remains absent from the battlefield while her agents threaten Jin's allies."
  ],
  "continuity_sources": [
    679,
    678
  ],
  "open_questions": [
    "Who has arrived on the Yangtze River Channel League's swift ship, and why did it come directly to the reconnaissance squad's position?",
    "What is the identity and full strength of the Supreme Peak master wielding the twin wheels?",
    "Can Jin and Muyaho survive the battle against the two Supreme Peak masters?",
    "Can Namho's group reach the Central Plains and bring reinforcements before Nanman is overwhelmed?",
    "Will the Blood Monk act with Baeksang and Dark Heaven, and what will happen to the Beast Miao King's loyalists in the Inner Palace?"
  ],
  "safe_through": 679,
  "temporary_decisions": [
    "Use Black Hand Fist Demon for 흑수권마 while retaining Black Hand for 흑수.",
    "Preserve Jin's abrupt register changes and profanity as deliberate psychological provocation.",
    "Render 쌍륜 as twin wheels.",
    "Render 장 족장 and 고 족장 as Chief Jang and Chief Go.",
    "Use Flame-Extinguishing Divine Fist for 멸염신권."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 675

# Chapter 675

It was true that I had thought of this place from the beginning, but even so, I had hoped I was wrong. Nanman was vast, after all, and I was still a Korean who didn’t even properly know the geography of the Central Plains.

In fact, even among all the martial artists in the world, there probably wasn’t another hybrid as strange as me.

*An outsider in the Central Plains, for all intents and purposes. An outsider in Nanman too, with no way to deny it.*

As someone in that position, there was no way I could have known exactly where we were headed or where we would stop.

Besides, Muyaho was a spiritual creature that understood human speech, not one that could speak it.

That was why, when the White Tiger’s pace finally slowed, I realized it.

*Looks like “no way” really is going to get someone killed. Fuck.*

The mountain’s shape alone gave off an ominous feeling.

Ailao Mountain, which we had returned to after only a few days, was unchanged. It was dark and chilly, and beyond the thick fog, it seemed as though the smell of blood was drifting toward us.

In short, it was the kind of place that felt fucking awful no matter when you came.

As far as Ailao Mountain was concerned, it felt like it deserved a separate name written with the character for “dick” instead of the character for “mountain.”

“…Is it really here?”

- *Grrr.*

“You know your leg’s getting chopped off if you lie, right?”

- *Grrrr!*

“Ah. Okay.”

Damn, I guess it really was.

I gently scratched the White Tiger between the brows, soothing its slight irritation as I surveyed the surroundings.

The occasional howl of a wolf. Mountain birds taking flight with a flutter whenever it sounded. Those were the only noises coming from around us.

*Yeah. At least as far as sound goes.*

Muttering inwardly, I checked the Quest window.

The linked Quest that had begun automatically when Muyaho and I split off from the group was short and simple for something with such a high grade as Supreme Peak.

> **System**
>
> **Quest**
>
> **I Can See Your Tracking Scent**
>
> You chose to track the tracking scent.
>
> At the end of the road you are traveling now, may you find what you seek.
>
> **Grade:** Supreme Peak
>
> **Restriction:** Jin Taekyung
>
> **Mission:** Find Yohi (Incomplete)
>
> **Reward:** ???
>
> **Failure:** ???

Find Yohi, huh? Of course I had to succeed.

But honestly, from my perspective, it didn’t matter whether it was Yohi or Heugung.

This was a mission I had to accomplish even if it wasn’t a Quest. Those two were among the surest cards I had for thwarting the Southern Heaven Demon Empress and Baeksang’s plans.

*According to the information I gathered, the Beast Miao King’s whereabouts are unknown, and the friendly forces inside the Nanman Beast Palace have effectively lost their power. With time running out, the best option is to rescue the two Great Chieftains and head to the Inner Palace.*

Did you think I’d made Muyaho run like hell while I sat comfortably on the tiger’s back doing nothing but sightseeing? I had already finished thinking things through on the way here.

Now that I had become the greatest fucking bastard under heaven in the eyes of the Nanman Beast Palace because of what happened at the Western Yao Estate, charging in alone would only leave me facing spears and blades.

But what if Heugung and Yohi—the people who had actually been abducted—returned alive with me?

*The whole board would turn over. Completely.*

“Words” carried different weight depending on who spoke them.

If each of the Great Chieftains leading the four tribes came forward to prove my innocence and reveal the truth behind this tragedy, then everything currently happening in Nanman would enter a new phase.

That was why I had to succeed at this Quest somehow. It was a brilliant move that might overturn the entire situation in a single stroke.

Of course…

“You need a Go stone before you can make a brilliant move. Not easy, starting from here.”

I muttered like a sigh, then continued as I sensed presences approaching from every direction, surrounding me.

“So I’m thinking I’ll grab a few of you first instead of Go stones and get started… Who wants to die first?”

“……!”

As expected, there was no answer. Without hesitation, I launched myself forward.

Whoosh. Fwoooosh!

Flamefire Path.

Flames surged up with each step, cleaving through the darkness like the tail of a meteor.

* * *

There were more enemies than at any point since I had begun tracking the tracking scent.

Just the ones visible at a glance numbered roughly three hundred.

There were probably as many, or more, lying in wait behind the dense grass.

But…

*Only this much?*

To me, who stood at the top of the food chain known as the Murim, the enemies surrounding me at this very moment were nothing more than a powerless flock of sheep.

I could subdue them without even sinking my teeth into their necks.

Whoosh, fwoooosh!

My body shot forward amid flames that devoured the darkness. Screams erupted from among the enemies who realized what was happening half a beat too late.

“He’s spotted us!”

“Stop him! He’s com—!”

Kwaaaang!

Someone’s shout was swallowed by the thunderous explosion that followed.

The ground overturned. Massive trees were ripped out by their roots. Dozens of enemies were flung in every direction at the same time, as if they had planned it together.

“Cough!”

“Aaargh!”

The tightly packed formation had already collapsed, leaving nothing in the gaps but screams.

As I walked out, brushing dirt from my shoulder, someone shouted.

“Put the beasts in front! Attack him from the rear!”

“Oh, that animal-abusing bastard.”

That aside, it was a decent choice.

Nanman’s method of fighting with beasts was well respected in its own right. It was also one reason Nanman warriors, whose individual abilities were inferior to those of martial artists from the Central Plains, had been able to distinguish themselves during the Great Faction War.

Of course, that only applied when the situation allowed for it.

Grrrrrrr!

The moment a creature far larger than an ordinary brown bear charged at me with a roar—

Shh-shh-shhik!

A pale blur accompanied by a sharp whistle of displaced air flashed past my side and struck the alpha brown bear in the mouth.

Crack! Crunch!

Blood droplets scattered through the air, and the massive body collapsed forward.

Muyaho had subdued the alpha brown bear—perhaps one of the three strongest beasts present here—with a single kitty-paw punch. Its eyes gleamed.

Whooosh!

I couldn’t see it, but I could feel it. A chilly aura spreading in every direction.

*This is…*

Fear.

The pressure of the White Tiger, which had transcended the vessel of a beast from the moment it was born, weighed down on the surroundings.

The growls of the beasts vanished as though washed away, and their tails, which had been standing straight up, lowered toward the ground.

At that moment, another strange gleam passed through the moonlit blue-white eyes.

- *GRAAAAAAWR!*

The explosive roar made the air tremble.

The wind rippled. Grass and flowers bent at the waist. The beasts’ pupils dilated as they crouched low and backed away.

And this strange phenomenon did not affect only the beasts.

“Gasp.”

“My, my body…”

Muyaho’s aura did not reach the level of the Water God Dragon or some of the monsters I had encountered so far. But it was more than enough to freeze several enemies who did not possess particularly outstanding martial arts.

Of course, that meant there were exceptions.

“You idiots! What are you doing?!”

The shout was stained with panic and fury.

I spotted a middle-aged man wearing a leopard hide relatively far behind the others and shot toward him like a spear.

Shaaak! Crack!

“Argh!”

“M-Monster!”

That was right. At least at this moment, in this place, I was the only monster.

An existence no one could stop. The kind of powerhouse they had only ever imagined, never once thinking they would have to face one as an enemy.

Even if everyone here stood in my way, I had the strength to move forward.

“Protect the Chieftain!”

“Stop him by any means necessary—cough!”

A palm gently tapped the opponent’s chest.

The Scorching Yang Qi that seeped into his body disrupted the flow of his qi. His body crumpled as blood burst from his mouth like a fountain.

“You bastard! How dare—!”

Whoosh! Thud.

Was the guy I’d just taken down a comrade of his?

He had plenty of momentum, but not enough skill.

I caught the blade between two fingers with ease, displaying the essence of Empty-Hand Seizes the Blade. Then I shrugged at the face visible beyond the trembling sword.

“He’s not dead. He’ll just be bedridden for about a month, shitting blood.”

“……!”

“Since you’re at it, you can shit beside him.”

Boom!

More than a dozen people were swept up by the body that shot backward with tremendous force.

I walked along the path that had opened before me and spread both hands.

The fire dragon coiled in my lower dantian surged upward along the acupoints in my body, lodging itself in my palms.

Whoosh. Ssssss.

Terrible heat spread in every direction.

The moisture evaporated before my feet even touched the mud, and blue-white flames reflected in the eyes of the elite warriors who were trying to charge me.

“W-Wait…”

I answered with both palms.

Like the former Sect Leader of the Fire Gate Clan who had once annihilated the Five Poisons Sect, I unleashed Flame Divine Palm in every direction.

Kwaaaang!

Rumble!

Flames fired through the air swept across the undergrowth and set the densely packed trees ablaze.

Beneath the enormous blaze that swallowed the darkness, hundreds of enemies fled screaming.

Including, most thankfully, a middle-aged man wearing a leopard hide so striking that I could recognize him at a glance.

“Move! Get out of my way!”

Judging by the way he was running for his life, he clearly wanted to live.

But no matter how hard he and his guards tried to escape, there was a reason the word “impossible” existed in this world.

“Yeah. I’m afraid I can’t get out of your way.”

“J-Jin Taekyung!”

“They said you were a tribal chieftain, so I wasn’t sure at first. But I definitely saw that face once at the Tribal Grand Council. So, have you been well?”

Shaaak!

This was why people said sword-carrying bastards had no manners. I greeted him warmly, and he started by swinging a weapon.

Whoosh, crack!

“Aaargh!”

I easily dodged the sword and broke the man’s wrist, drawing a scream of pain.

Then I fired Finger Qi at the five guards charging straight at me. Muyaho appeared like the wind right afterward, and the beasts fled with their tails between their legs.

Whoosh. Rumble!

Flames and ash drifted overhead. Massive trees toppled one after another like dominoes.

The tribal chieftain’s face turned deathly pale.

“P-Please, spare me…”

“You’re a tribal chieftain, so of course I’ll spare you. Assuming you answer my questions properly.”

“I-I’ll tell you anything you want to know!”

The chieftain I had captured was the kind of enemy I most wanted to encounter.

People like him knew the value of their own lives, so they willingly confessed even things I had not thought to ask.

And some of the information included in his confession was quite useful.

“…A general mobilization order?”

The chieftain nodded frantically.

“G-Great Chieftain Baeksang has become the temporary Palace Lord, and an army of nearly ten thousand is already stationed in the Inner Palace.”

“Continue.”

“The Miao people are under such strict surveillance that they couldn’t respond, but all of Nanman is moving, centered around the three tribes led by Baeksang.”

Damn it.

I swallowed the curse.

With the Beast Miao King having fled, it had been inevitable that Baeksang would become the temporary Palace Lord.

But this was not a net over heaven and earth meant to capture me. It was a general mobilization order.

*No way.*

An ominous feeling seized my entire body.

Perhaps the picture Dark Heaven had drawn was far larger than any of us—including me—had imagined, and perhaps it was nearing completion.

*If I delay here for even a moment…*

I watched the flames rapidly spreading through Ailao Mountain, then hurriedly launched myself forward.

Into the darkness crouched over Ailao Mountain.

Into the flames.
## Chapter artifact 676

# Chapter 676

The flames born from Flame Divine Palm began at the entrance of Ailao Mountain and spread in every direction in the blink of an eye.

*Fwoosh. Roooar!*

If the Scorching Hell described in Buddhism existed, I imagined it would look something like this.

Ash drifted endlessly through the air, mixing with acrid smoke. A fire demon rolled like a wave, devouring everything in its path.

*Crack. Rumble!*

The earth shook as massive trees toppled one after another, and every mountain bird took flight at once.

It was the sort of sight that would have made Jeok Cheongang, honorary chairman of the Forest Protection Association, roll his eyes back in horror. Fortunately, there didn’t seem to be any noticeable beasts nearby, so it looked like the Animal Protection Association wouldn’t be getting involved too.

*They’re wild animals, so I guess they’re quick on the uptake. Did they all run away already?*

Honestly, I didn’t care what happened now.

I had no desire to take away the home and lives of some poor family of muntjacs, but stopping Dark Heaven’s sinister scheme and saving everyone else’s lives mattered more.

*If the ominous feeling I sensed is real…*

I no longer had the luxury of hesitating.

As I ran forward at full speed, I spotted a wall of flame blocking the path roughly forty yards ahead and reached toward the air.

*Open Inventory. Summon.*

It had been the right choice not to take White Flame out when I surrendered at the Western Yao Estate.

If it had been confiscated, I wouldn’t have been able to use it at the most important moment like this.

*Shing.*

A cool sensation filled my hand. Flames flickering in every direction were reflected across the spearhead, which was white enough to appear transparent.

*Now.*

With the entire area already turning into a sea of fire, I didn’t do something stupid like infuse the spear with Scorching Yang Qi and fire it away.

What I needed now was power and speed. Along with simple yet perfect movements and flow.

*Whoosh!*

With a sharp whistle, a violent gust burst from the tip of my diagonally slashed spear and tore the flames apart.

*Fwoosh! Boom!*

A path opened amid the explosion.

I lay flat against the white fur and whispered beside Muyaho’s ear, who had briefly hesitated in front of the flames.

“Let’s go.”

- *Grrr.*

The White Tiger answered with a low growl and shot forward like a beam of light.

The flames rolling like waves pursued us close behind, but even amid the chaos, Muyaho knew exactly where it was going.

*Papat!*

The scenery flashed past at incredible speed. The moon hanging high in the sky was hidden behind clouds, and as I continued forward without pause with the fire at my back, I muttered at the strange familiarity I felt.

“Don’t tell me…”

The next moment, a thought flashed through my mind, and I abruptly closed my mouth.

No. Maybe it wasn’t a matter of *don’t tell me* at all.

The fact that this path and the surrounding scenery, which should have been unfamiliar, felt so familiar could mean only one thing.

*The Poisonblood Grounds.*

Ailao Mountain had become known as one of Nanman’s forbidden lands after the destruction of the Five Poisons Sect, which had once plunged all of Nanman into terror.

And the Poisonblood Grounds lay in the deepest, most secluded part of Ailao Mountain.

If my guess was right, we were heading straight there. To a place that might be the most dangerous in all of Nanman.

*But by now, a considerable number of troops should be guarding it.*

The Nanman Beast Palace wasn’t some backwater sect filled with assorted riffraff.

When as many as five extremely rare Thousand-Year Spiders appeared and the Poisonblood Grounds, which no one had discovered for so long, revealed itself, the Nanman Beast Palace dispatched a sizable force.

They had intended to root out any remnants of the Five Poisons Sect and any dangers that might still remain.

*Even if they were counting on hiding right under their noses, did they really crawl into a place like that?*

It didn’t take long for the question in my mind to be answered.

- *Grrrr…*

At some point, Muyaho’s steps gradually slowed.

The White Tiger bared its teeth, having sensed something, and I immediately realized that something had happened. Soon after, I realized that the metallic smell seeping through the acrid smoke was the scent of human blood.

*I see. So that’s how it is.*

Muttering inwardly, I looked toward the entrance to the Poisonblood Grounds.

It yawned open like the mouth of a gigantic monster, seemingly filled with unknown dangers just as it had been when I first came here.

No. Maybe it was even worse than before.

*Well, if it were easy, it wouldn’t be a Supreme Peak-grade Quest.*

I had started to think things were going more smoothly than expected. But unlike Baeksang, I had come too far to turn back, though for a different reason.

If I avoided the danger directly in front of me, an even greater danger would come rushing in behind me.

Just like the flames sweeping through the forest and closing in behind me at this very moment.

*Rustle.*

I climbed down from Muyaho’s back and gently scratched beneath its chin, the spot it usually liked, as I spoke.

“It looks like this is where we part ways. The difference from last time is that this time, you don’t have to come back.”

- *Grrr?*

“Go back before it gets any later. You can break through the flames and escape. I know you can.”

- *Grrrr…*

Muyaho gazed at me silently with a small whimper.

I could sense the conflict and fear reflected in the blue-white eyes of the intelligent White Tiger.

As befitted a creature with extraordinary instincts, it seemed to have already guessed.

That entering would be easy, but getting out would be difficult.

That it might never see Yayul Mok again.

Even so, it couldn’t turn away as easily as it had last time, probably because a certain bond had formed between us in the time since.

“I’m not going there to die. So don’t worry and leave first. Your master will be waiting for you.”

As I reassured it and gently stroked the back of its neck, Muyaho finally nodded slowly and launched itself forward after a brief pause.

- *GRAAAWR!*

*Whoosh!*

Not toward the hill the flames had yet to reach, but toward the entrance to the Poisonblood Grounds.

“Hey! Hey, you idiot!”

I shouted in surprise, but it was already too late to catch it.

For a moment, my body stiffened at the unexpected turn of events. Then, with a mighty roar, the White Tiger that had charged headlong into the pale Poison Mist came staggering back out.

- *Krrk. Cough.*

“…Want a poison-warding pearl?”

The White Tiger hesitated, avoided my gaze, and gave a small nod.

* * *

Muyaho adapted to the Poisonblood Grounds much faster than I had expected.

As if biting down on the poison-warding pearl weren’t enough, it gulped the thing down whole. With nimble reflexes, it dealt with the venomous beasts surging in from every direction and cleared a swamp so wide that even Peak masters who had learned a movement technique would have hesitated to cross it in a single leap.

However, the deeper we went, the more cautious its movements and breathing became.

*Whooosh…*

The Poison Mist that had swallowed the inside of the Poisonblood Grounds made it impossible to see clearly. Only the occasional sound of something unknown brushing against the grass or water dripping reached our ears. Everywhere around us was silent enough to make my skin crawl.

*It wasn’t this bad even when I came here with the Beast Miao King last time.*

I had sensed it from the moment I smelled blood at the entrance, but this was definitely not a good sign.

A thought suddenly crossed my mind.

Perhaps… No, with a fairly high probability, the people the Nanman Beast Palace had dispatched to the Poisonblood Grounds a few days ago were no longer of this world.

*If that’s true, it must be that bastard’s work.*

A Supreme Peak master whose name, sobriquet, and face had never been revealed.

Someone who had dyed the Western Yao Estate in blood and kidnapped Heugung and Yohi in less than a moment could certainly have done this.

It was also highly possible that it wasn’t just one bastard, but *them*.

Dark Heaven.

The strength of those who had appeared after the Demonic Cult was terrifying, even judging only by what they had revealed so far.

In particular, the martial prowess of the Blood Lord and the Western Heaven Demon Lord, whom I had personally faced…

Even I, who had used the System as a foundation to grow rapidly through relentless training and countless life-or-death battles, couldn’t dare guarantee victory against them.

*Though I’ve never faced her myself, the Southern Heaven Demon Empress must be a master whose skill is no less than theirs.*

That was why, as I headed alone into enemy territory, I couldn’t help but be even more tense.

When I had encountered the Blood Lord, Sword Saint Mae Jonghak had been there.

And during my decisive battle with the Western Heaven Demon Lord—the battle that had brought me closer to death than any other—Jeok Cheongang had helped me.

*But if the Southern Heaven Demon Empress is here…*

Would I be able to survive and see my comrades and family again?

*Drip.*

It was at that exact moment, when a bead of cold sweat formed without me even realizing it and slid down the back of my neck.

*Lick.*

The sensation was rough enough to sting.

When the White Tiger licked the back of my neck and pretended nothing had happened, a quiet laugh escaped me.

“Are you telling me not to be nervous?”

- *Grrrr.*

It was a trivial thing, but it strangely put me at ease.

Come to think of it, I had gone through countless brushes with death until now. And yet here I was, breaking into a cold sweat now that I had come this far.

If I stayed this tense, my body would stiffen and I wouldn’t even be able to fight properly.

*Yeah, fuck it. It’s not like this is my first time.*

I reaffirmed in body and mind the no-brakes mentality that was an essential virtue for the successor of the Fire Gate Clan and the heir of the Fire King, then thrust one palm toward the Poison Mist.

*Boom!*

The sharp sound of displaced air shattered the silence.

The heat of Flame Divine Palm, which possessed the Scorching Yang Qi that was the natural enemy of poison—an unimaginably fierce heat—surged forward.

The thick Poison Mist broke apart and scattered, and the dark Poisonblood Grounds turned red.

*Hssssss!*

Strange-shaped venomous beasts hurriedly moved away from the light and heat.

As I glared at the maze of tangled paths that had finally been revealed, I infused my voice with internal energy and roared.

“Come out, you fucking bastards!”

- *GRAAAAAAWR!*

* * *

How had this happened?

At some point, Yohi suddenly came to her senses and blinked in the darkness, unable to see even an inch ahead.

“Ah.”

Her usually alluring voice was half-hoarse, and her entire body ached from having remained motionless for so long.

Only then did fragments of memory gradually begin to rise to the surface.

“……!”

Her heart dropped without her realizing it, and her body, which had relaxed for a moment, stiffened again like a stone statue.

In Yohi’s trembling eyes, memories she couldn’t believe were flashing past.

Screams. Corpses. Blood.

And the face of the one person who had created all of it.

Just as Yohi instinctively tried to scream, a tightly hushed voice came from the darkness.

“Calm yourself, Yohi.”

“Gasp…!”

“There’s nothing to be surprised about. It’s me.”

Yohi barely managed to swallow her scream and calm her pounding heart.

As her eyes slowly adjusted to the darkness, a familiar silhouette came into view.

“Heugung? Is it really you, big brother Heugung?”

“That’s right. Don’t you remember?”

It took a little time for her memories to return in sequence.

Remembering Heugung resisting *him* until the very end, Yohi murmured,

“I must have forgotten for a moment without realizing it. But why are you speaking so differently from usual…?”

In the darkness not far away, Heugung had been waiting for her to wake up. He gave a bitter smile.

“There were various circumstances. Circumstances I couldn’t easily tell even you.”

His tone and manner of speaking were respectful.

Yohi found this side of Heugung—who usually wore a goofy grin and called her “my dear”—strange, but that wasn’t what mattered right now.

“Where are we? Wh-where is that man?”

“I don’t know either. I opened my eyes and found myself here.”

Her body was bound in iron chains, and her internal energy would not move at all.

Just as Yohi searched her surroundings with despairing eyes, a dull noise sounded and faint light poured in.
## Chapter artifact 677

# Chapter 677

*Click. Rumble.*

Light spilled out through the stone gate as it suddenly opened.

Heugung and Yohi, whose eyes had grown accustomed to the darkness, instinctively shrank back and groaned. Then a voice bored into their ears.

“Oh-ho. Now this is a sight worth seeing.”

“……!”

“……!”

“Of course. This is how the barbarians of Nanman ought to look.”

The voice swayed as if its owner were drunk, and both their bodies trembled.

Was it because they felt humiliated by the mockery and ridicule in his words?

No. It was because of fear. Because of terror.

*That voice…*

Yohi recognized the speaker and felt as though the blood throughout her body had turned cold.

How could she forget it? The voice of the Fiend who had appeared like a ghost, slaughtered the warriors under her command, and turned Heugung into a one-armed man with a single move.

Just as Yohi’s mind went blank, she heard Heugung whispering with bated breath.

“Remember this. You must never open your eyes—”

*Boom!*

A sharp blast of displaced air rang out alongside a scream.

Yohi had squeezed her eyes shut as he advised, so she could not see what had happened. But it was not difficult to imagine Heugung coughing up dark-red blood from his internal injuries.

“Stop! Please, stop!”

“Cough, cough. Yohi, stay still—”

*Boom! Thud.*

Another blast of displaced air rang out, and Yohi could no longer endure it. She opened her eyes.

Heugung lay on the floor with his entire body bound. Standing before him was the Fiend, who had forced him to vomit what looked like a full doe measure[^1] of blood.

“You…”

“I heard you were a fairly clever woman, but I see that was nothing more than a false rumor.”

The Fiend revealed yellow teeth in a grin as Yohi’s voice slipped between her trembling lips.

His white hair was nearly as disheveled as a bird’s nest, and his eyes were narrow slits. He had hidden his face behind a mask in the Western Yao Estate, but there was no doubt that the old man before her was the same Fiend.

“Why didn’t you listen to that fellow? If you hadn’t seen this old man’s face, you might have lived for another fifteen minutes.”

“……!”

“Well, what’s done is done. I suppose we’ll just have to send both of you on your way to the afterlife together.”

The old man shrugged and extended an arm that was unnaturally long compared to his pitifully small frame.

The closer his palm came, the stronger the smell of death grew. His hand was covered in spots whose origins Yohi could not identify.

Just as Yohi realized this was the end and tried to struggle—

“That’s enough, Black Hand.”

The words came through the gap in the half-open stone gate. The old man called Black Hand withdrew his hand with a sigh.

“Come on. Now I can’t even have a little fun without having to watch myself.”

Someone Yohi could not see answered him.

“Are you saying that to me?”

The voice was as cold and remote as eternal snow. Black Hand clicked his tongue.

“Of course not. I was talking to myself. Just talking to myself.”

“Stop acting like a reckless brat. You haven’t forgotten the order given by Her Majesty the Demon Empress, have you?”

Black Hand’s face twisted.

“A reckless brat? I never thought I’d be called that at my age.”

“Then act your age. If you behave rashly with the great undertaking so close at hand, I will not forgive you.”

“……”

“I’ll take your silence as an answer.”

Yohi felt no presence at all, but she realized that the person outside the stone gate had disappeared when she heard Black Hand muttering a moment later.

“Damn old monster.”

Perhaps it had been nothing more than a minor complaint to Black Hand, but Yohi had to struggle with all her might not to reveal her shock and fear.

*It wasn’t just him.*

She did not know who owned the cold voice that had suddenly cut into their conversation. But she could tell from the brief exchange between the two of them.

*That person possesses enough seniority and martial prowess to make even the Fiend before me obey him.*

And on top of that…

*The Demon Empress. He definitely said the Demon Empress.*

Two words that had appeared in the middle of their short conversation.

The Demon Empress.

Yohi already knew whom that word referred to.

*The Southern Heaven Demon Empress.*

A core figure of Dark Heaven, known for being unnaturally beautiful—and even more dangerous than she was beautiful.

Everything concerning the Southern Heaven Demon Empress was treated as top-secret information. But Yohi was one of Nanman’s four Great Chieftains, so she was an exception.

More importantly, she had a great tree named Baeksang whom she could trust and rely on.

> “If you stand by my side, I will give you what you want.”

That was what Baeksang had said when they first met, shortly after Yohi had risen to the position of Great Chieftain.

Yohi had asked him in return:

> “What do you intend to give me?”

> “Vast wealth and influence. And the restoration of the Yao people.”

> “Interesting. But I’ll refuse.”

> “Why?”

> “Even if I accept Great Chieftain Baeksang’s offer, I won’t receive the reward I want. I have greater ambitions than I appear to. Nor am I naive enough to make Palace Lord Yayul my enemy over a promise that may never be kept.”

> “You inherited the Western Yao Estate when you took the position of Great Chieftain. Do you have any trustworthy subordinates there?”

> “Of course. But why are you suddenly asking about that…?”

> “I was thinking of sending a gift, albeit late, as a congratulatory gesture. Five carts of gold should be enough to start with.”

> “……!”

> “Go home for today. If you intend to accept my proposal, come meet me again at this time tomorrow.”

Five carts of gold.

At first, Yohi had been half-convinced and half-doubtful at the enormous sum, which she had never even dared imagine. But after seeing the piles of gold waiting for her with her own eyes, she had no choice but to believe.

Baeksang always kept his promises.

If she stood by his side, she could obtain even more than the reward she wanted.

The following day, after spending the entire night awake, Yohi had gone straight to Baeksang and realized that her judgment had been correct.

No. She had believed it was correct.

At least until the Fiend before her came looking for her.

“Oh-ho. Look at this little bitch.”

As if he had never been offended, Black Hand smiled hazily like a drunk.

“Judging by those round, wide-open eyes, I suppose you’ve figured out what this is about. Hmm?”

“I, I…”

“Well, this old man has heard the general story. They said our preparations went smoothly thanks to you. At least in that regard, Baeksang did a decent job for a barbarian.”

Yohi’s pupils shook violently.

She could not believe the situation she was in: not only had she served as a pawn of Dark Heaven, she was now in danger of dying.

“That can’t be. It can’t be. I didn’t know…”

“Did you not know? Or did you pretend not to know?”

“……!”

“I don’t even need to ask. After all, you followed that bastard Baeksang for more than ten years. A woman who had risen to become a Great Chieftain would naturally have had her doubts.”

Yohi could only stare blankly at Black Hand as he chuckled.

Everything the Fiend before her said was true.

It had begun with something insignificant. Once a year, at the Tribal Grand Council, she had raised her hand in support of Baeksang’s opinions. She had followed a few minor orders he gave her, and gold and influence had rolled toward her in abundance.

But as the years passed, her suspicions had deepened. Then, several months ago, she began hearing the name Dark Heaven with increasing frequency, and unease had taken root in her heart.

But that was all.

Yohi had deliberately ignored and suppressed the doubts and anxiety that had taken hold inside her.

She had gained too much to reveal everything and try to clean up the mess.

The people of the Yao tribe looked up to Yohi, who had revived their slowly weakening tribe. The tribal leaders who had treated her like a little girl were the first to lower their heads.

Even the mighty Beast Miao King and Baeksang would eventually return to the earth as a handful of soil. When that time came, she might even be able to reach for the vacant throne.

She would rise to the position of Palace Lord as a woman and rewrite the history of the Nanman Beast Palace.

Yet the grand ambition Yohi had revisited every night was collapsing completely at this very moment.

“Even so, you should be grateful to this old man. If the previous Great Chieftain of the Yao people hadn’t died suddenly, how could a stupid woman like you have lived in luxury until now?”

“Th-that can’t mean…”

“He was a troublesome old man in many ways. His martial arts were pathetic, but he was quick to notice things. Fortunately, a plague broke out among the Yao people at just the right time, so he was easy to deal with.”

Black Hand continued with a grin.

“Isn’t it strange? The Great Chieftain was already old enough to die, so perhaps that part was understandable. But then his three sons, who were supposed to succeed him, died as well, and the position passed all the way to the old man’s illegitimate daughter, born in his later years.”

“……!”

“Baeksang’s expression back then was truly something to see. He dragged things out to the bitter end, insisting he would somehow persuade the old man… Still, perhaps the bastard had a strong survival instinct, because he never came charging in. What a shame.”

Yohi stared at Black Hand with hollow eyes. She thought she had no more strength left to be shocked by anything.

But that, too, was only a delusion of her own.

“You did fairly well for a woman, though. Even with your life in danger, you prepared a tracking scent. Did you inherit that caution from your old father?”

Tracking scent.

At the three words that slipped from Black Hand’s dark lips, Yohi’s delicate body suddenly went rigid.

Black Hand had shattered even Yohi’s last hope, and he could not contain his amusement.

“Why? Did you think this old man wouldn’t know?”

Black Hand chuckled as he read the despair trembling in her eyes.

He had faced this emotion countless times before, but the exhilaration that surged through him in moments like this had never dulled in the slightest.

“Oh, you poor thing. You inexperienced little girl. What a foolish child.”

Just as his name suggested, Black Hand’s palm was covered in black spots as it stroked her snow-white cheek.

“You’re truly beautiful. Beautiful enough for Her Majesty the Demon Empress to covet.”

The old man opened his mouth like a predator facing its prey. A terrible stench wafted from his teeth, all of them either rotten or twisted grotesquely out of shape.

“I’d like nothing more than to kill you both with a single palm strike, but… I’ll restrain myself this time. There’s something I have to do first.”

Leaving Yohi frozen like an insect caught in a spider’s web, Black Hand rose from his seat.

He glanced at Heugung, who had already collapsed unconscious, and approached the stone gate.

That was when—

*Rumble-rumble-rumble!*

Black Hand heard it.

Along with a thunderous roar that shook the entire area, someone’s distant shout reached his ears.

—Come out, you fucking bastards!

*GRAAAAAWR!*

It was time to go welcome the guest who had come such a long way.

* * *

My method of calling out enemies was simple.

I broke things, wrecked things, and smashed them to pieces.

Poison Mist? Venomous beasts? Enemies hiding somewhere and watching for a chance to strike?

I didn’t care.

I rampaged like an eight-ton truck with a broken steering wheel, smashing everything in the Poisonblood Grounds.

I had to make sure the enemies had no choice but to come out.

And my efforts bore fruit before long.

“What a vigorous young man.”

“I expected the Beast Miao King if someone came looking for us… So you’re Jin Taekyung?”

Following the voices, I slowly turned around and saw them.

A short, squat old man swaying as though he were drugged, and a tall old man radiating such cold that I wondered if his hometown was King Sejong Station in Antarctica.

The two old men could not have been more different, but they had things in common.

First, they were both Supreme Peak masters.

Second, they were emitting killing intent that made it clear they had no intention of letting me leave alive.

After studying the two old men for a moment, I spoke sternly.

“One of you step aside. I’ll face you one at a time, according to the customs of the martial world.”

The answer came immediately.

*Whoosh—KWA-BOOM!*

Yeah, fuck. I knew that wouldn’t work.

[^1]: A *doe* is a traditional Korean unit of volume, roughly 1.8 liters.
## Chapter artifact 678

# Chapter 678

It was fortunate that the Southern Heaven Demon Empress was nowhere to be seen for the moment, but there were two Supreme Peak masters here.

*Damn it. I don’t know.*

Should I call this situation fortunate? Or unfortunate?

*Whoosh—KWA-BOOM!*

I narrowly dodged a black Fist Force that came rushing at me like a beam of light, straightened my body, and let out a sigh.

“Ah, the ways of the martial world have fallen to the ground. Where has the martial virtue of yielding three forms for the sake of a junior disappeared to?”

“What?”

The squat old man with disheveled hair blinked at me.

Apparently, what I had just said was so absurd that the fist he had been about to send out after his opening attack slowly lowered.

“The ways of the martial world? Yielding three forms for a junior?”

I lowered my voice and answered.

“That is correct.”

“Why are you suddenly talking like some old-fashioned gentleman and spouting nonsense? A moment ago, you said you’d face us one at a time and told one bastard to stay out of it.”

“‘Bastard’? Did I say that?”

“Now you’re being polite again. Either speak casually like you did at first, or stick to the formal register. You’re giving me whiplash.”

“Forgive me. This distant junior failed to recognize his Seniors and committed a grave discourtesy.”

I adopted a posture as straight as a sword and even performed a clasped-fist salute. Confusion filled the disheveled old man’s eyes.

“This is getting confusing. You’re not Blazing Flame Divine Dragon Jin Taekyung, the Fire King’s heir, are you?”

“I am.”

“Then that means you’re one of those orthodox-faction types. Hearing you go on about juniors is enough to make me sick.”

“What a hurtful thing to say. Aren’t all those who dwell in the martial world fellow martial artists and members of one family? Besides, the Fire Gate Clan has always been a faction between the orthodox and unorthodox sides. We don’t discriminate between the orthodox, demonic, or anything else. We all get along.”

“And yet you’re serving as a pavilion master in the Murim Alliance?”

His eyes had already gone completely off the rails, but at least his brain still seemed to possess a minimum level of function.

However, a true master maintained his composure in any situation.

So I answered his sharp question without changing my expression.

“I’m actually a double agent.”

“A double agent?”

“Yes.”

“Bullshit.”

“Woof.”

“This is driving me insane.”

“I understand how you feel. But I swear to heaven, there isn’t a shred of falsehood in what I’ve said.”

“You little…”

“Did you call for me, Senior?”

The disheveled old man stared blankly at my polite demeanor before opening his mouth with a look of admiration.

“You put your whole heart into spouting nonsense, one stitch at a time. In all my years, I’ve never seen an orthodox-faction brat like you.”

I scratched the back of my head sheepishly.

“You fucking bastard. Then at least pretend to fall for it out of respect for the effort.”

“You deranged child. Shouldn’t the lie be believable before anyone can be fooled?”

“I’m already embarrassed, so shut up, you idiot.”

“……That tongue of yours got awfully rude, awfully fast. I could’ve sworn I was ‘Senior’ just a moment ago.”

“Did senility finally get you, old man? You’re a piece of demonic, heterodox trash who should’ve died back during the Great Faction War. Who the hell do you think you are, demanding to be called Senior?”

At the stream of abuse, the disheveled old man stared blankly for a moment before bursting into laughter.

“You really are a completely insane bastard. You’re truly worthy of being the Fire King’s Disciple.”

“Funny how everyone I meet says that when none of them have ever even seen the Fire King’s face.”

The disheveled old man hesitated for a moment before letting out a quiet laugh.

“How amusing. Truly amusing. You’re nothing but a bloody whelp who has barely passed the age of twenty, yet you dare speak of those days.”

“Well, I feel like I can figure it out without having lived through them.”

I shrugged and continued.

“If a bastard like you had met him, you’d already be dead. In short, you’re a lucky bastard who survived by avoiding the Fire King.”

“……!”

“But I have a feeling that luck will run out today.”

*Swish.*

I raised White Flame and pointed it at him—or rather, at them. A haze rose from the pure-white spearhead filled with Scorching Yang Qi.

“The Western Yao Estate. Was that your doing?”

*Crack.*

The smile vanished from the disheveled old man’s face as he clenched his fist and stepped forward.

“Yes. This old man did it.”

“I thought so. Only someone out of his mind would kill people that way. What about Heugung and Yohi?”

“For now, we have those two tucked away nice and comfortably. But once Her Majesty the Demon Empress returns, those bastards’ stubborn hold on life will end.”

I felt relieved by the two facts the enemy had confirmed himself.

“Thanks for the fucking useful intel. So the Southern Heaven Demon Empress—that fucking bitch—isn’t here. And those two are still in one piece.”

Only then did the disheveled old man realize that he had said more than he needed to. His face hardened.

“……That changes nothing. Even if Her Majesty the Demon Empress is absent, you will die by this old man’s hand.”

“Then why did you two come together? Were you scared a kid would kick your ass, so you brought your hyung?”

“You fucking brat…”

*Step.*

The disheveled old man took a step forward, unable to contain his anger. It was nothing special to an observer, but that single step was exactly what I needed.

*Now.*

But in the next moment, I had no choice but to stop the spear I had been about to swing with all my strength.

*Thud.*

A long, withered hand as thin as a tree branch had seized the shoulder of the disheveled old man just as he stepped forward.

“It’s a provocation tactic. Don’t let that bastard’s three-inch tongue fool you.”

*So he finally stepped in.*

A cold voice. A cold expression.

Baeksang was second to none when it came to being chilly, but the slender old man, who had not said a word from beginning to end, was on another level. No—their temperaments might have been similar, but there was a difference in depth.

The ice-hard, glacier-cold composure.

And the martial prowess contained within his body.

*There’s no opening.*

The meaning of that instinct was clear.

He was at least my equal—or perhaps even stronger.

That was why, although the disheveled old man had been the one speaking with me directly, my nerves had been focused on the slender old man from the very beginning.

And it seemed my opponent felt the same way.

“You’re quite something. No, ‘quite something’ doesn’t come close.”

With an exclamation that betrayed little emotion, the slender old man stepped forward.

“You unsettled your opponent with a few words and exploited the opening you created… Now I understand why Her Majesty the Demon Empress warned us to be wary of you. You possess martial prowess that belies your age, as well as a calculating mind. You will become a major obstacle in the future.”

“Am I being too negative about a simple compliment? It sounds like you’re saying you intend to kill me somehow.”

“Then you understood correctly. Both the compliment and the intention to kill you.”

“Since you went to the trouble of complimenting me, why don’t you just let me pass quietly? Is there really any need to pull out a stone?”

“If you remove the stone embedded in the middle of the road, the path ahead will become smooth.”

“And are the two of you really skilled enough to do that?”

“You bastard! Shut your mouth!”

Unlike the disheveled old man, whose face twisted at my casually tossed taunt, the slender old man answered in his cold voice.

“We will have to do our best.”

*Damn it.*

I suddenly had a feeling—no, the certainty—that this would be an extremely difficult fight.

If a mad dog runs wild, all you have to do is beat it down with a club.

But an enemy who maintained his composure in every situation and never underestimated his opponent was bound to be troublesome.

Even more so if that enemy possessed martial prowess that was in no way inferior to my own.

*If I fought that man one-on-one in a life-and-death duel, my odds would be fifty-fifty. But that situation won’t happen.*

In a bloody struggle where life and death could be decided by the slightest difference, even a cat’s paw was useful. And the disheveled old man’s skill, as far as I could tell, was even greater than Baeksang’s.

*Can I do this? Can I?*

Just as a single doubt summoned by instinct flashed through my mind—

“Grrrr…”

Muyaho bared his fangs and let out a wary growl.

Yet in his crouched posture, ready to spring at any moment, there was not the slightest sign of retreat.

*Yeah, fuck. Even an animal that can’t speak is willing to fight. How can I, a human being, back down?*

There was only one thing that bothered me.

I had a feeling I might not be able to protect him this time.

*I’m sorry.*

“Grrr.”

I didn’t know.

Perhaps the clever White Tiger had read the meaning in my eyes. Perhaps he understood that I wished, if nothing else, for him to run far away.

But one thing was certain.

Either I would die here, or I would kill them.

Regardless of the outcome, I would not retreat.

*Step.*

“Since I’ve never even heard your names anyway, go peel and eat those limp cocks of yours, then spit out your sobriquets.”

The disheveled old man smiled with killing intent as he spoke to me, White Flame hanging loosely in my hand.

“Black Hand Fist Demon.”

“Yeah, there you are, Black Hand. I’ve never heard that sobriquet before, so I guess you really are some nobody.”

“There were reasons for that. But now the whole world will know it. It will be the sobriquet of the one who killed the Blazing Flame Divine Dragon.”

“Maybe. But everyone will learn who I am even without that. Everyone who dies by my hand becomes famous.”

I answered calmly, ignoring the Black Hand Fist Demon as he began to flare up, and turned my gaze away.

But contrary to my wishes, the slender old man met my eyes and gave a small shake of his head.

“There is no enemy easier to assess than one whose sobriquet is known. Isn’t that right, Blazing Flame Divine Dragon Jin Taekyung?”

“……!”

“This old man knows you, while you do not know me. But one of us will fall here. If you have finished preparing yourself, come.”

*Damn it. This really won’t be easy.*

But the die had already been cast. Now it was time to see how it landed.

I awakened the fire dragon curled within my lower dantian.

*Rumble-rumble-rumble—!*

An aura erupted from my entire body like a volcano exploding, shaking the area in every direction. Blue-white flames layered themselves over the transparent spearhead made of Ten-Thousand-Year Cold Iron, completely enveloping the spear.

*Fwoosh. Sizzle-sizzle-sizzle!*

The terrible heat burned poison and evaporated moisture.

The Black Hand Fist Demon’s focus, which had been hazy like that of a drunken man, sharpened at the aura I released. A strange light flashed through the old man’s eyes, frozen like eternal snow.

“Indeed…!”

*Swish.*

At that moment, with a brief exclamation, an edged weapon emerged from beneath his loose sleeve and gleamed with a cold blue light.

*SHWAAAAAAK!*

The twin wheels flew from the old man’s hand, tearing through the air.

* * *

*Whoosh-whoosh-whoosh!*

They ran without stopping.

Even when three tigers became two and five people became four, that fact did not change.

No—in that situation, they had to move even faster.

They had come too far to turn back. If they returned now, *his* choice and sacrifice would become meaningless.

And perhaps thanks to his—no, Jin Taekyung’s—efforts, nothing blocked their path.

The tigers carrying four people on their backs ran north, then farther north, before the messenger pigeon sent from the Nanman Beast Palace could even arrive. The warriors of each tribe were too busy chasing Jin Taekyung to interfere.

*Whoosh-whoosh-whoosh!*

They crossed the plains, climbed over mountains, and passed through swamps and rivers.

And at last, the first goal of this short yet urgent journey began to appear.

“There!”

Namho’s shout was directed below the hill.

In the distance, several hundred Nanman warriors advanced toward the northern border in a long, snaking line.

At last, having caught up with the reconnaissance squad, they felt the tension leave their bodies as a single person’s face came to mind.

*Jin Taekyung.*

Their Pavilion Master, though they had no idea where he was or what he might be doing now.
## Chapter artifact 679

# Chapter 679

The reconnaissance squad, made up of swift-footed elites, moved at a rapid pace.

Despite numbering more than two hundred people, they reached the northeastern border in barely three days, taking breaks whenever they could along the way.

However, none of them—not even the two tribal chieftains leading the reconnaissance squad—had expected another group of unwelcome visitors to arrive before they encountered the mysterious monster known as the Blood Monk.

And this unexpected situation was nothing compared to the news those visitors had brought.

“What… did you just say?”

“What are you talking about?”

Chief Jang and Chief Go stared wide-eyed in disbelief.

It was shocking information that no one could have anticipated.

If the one who had delivered it had not been the Young Palace Lord of the Nanman Beast Palace, they would have dismissed it as nothing more than absurd nonsense.

No. They had actually hoped it was nonsense.

But despite their desperate wish, Yayul Mok’s answer did not change.

“It is all true.”

The truth shone in his quivering eyes. At last realizing that all of this was reality, the two chieftains could do nothing but sigh.

“What in the world…”

“Why did the Palace Lord make such a choice? Why?”

Yayul Mok clenched his fists so tightly that blood ran from his palms before opening his mouth.

“My father had already guessed that he would be unable to resist the tide of events once so many chieftains had joined hands with Uncle Baek—no, with Baeksang.”

“Even so, did he really bring this danger upon himself just to save a few Han Chinese?”

“He did not bring danger upon himself.”

“What?”

“My father said this when he sent me and the others to the underground prison. He said that repaying a righteous act with righteousness was keeping faith, and that turning away from someone who had helped us was injustice. So today, I intend to stake my fate on keeping faith. On those two people—Jin Taekyung and Baeksang.”

“……!”

“……!”

The two chieftains closed their eyes with quiet groans.

Having served at the Beast Miao King’s side for a long time, they had vaguely guessed what kind of person he was and what choices he would make.

But…

“This time, the Palace Lord was wrong. He should have gathered all the strength of the tribes that followed him and the Miao people, then executed the traitors in the Inner Palace.”

“Even if we give Jin Taekyung every benefit of the doubt, trusting him may have been the right choice. If the Young Palace Lord’s story is true, Jin Taekyung ultimately left alone in order to keep faith. But Baeksang is different.”

As the two chieftains spoke with such certainty, Yayul Mok, who had been looking at them with a trace of hope, opened his mouth.

“It is too early to judge. If Baeksang honored my father’s request…”

“Young Palace Lord.”

Chief Jang cut him off and continued in a hollow voice.

“Subdue the Han Chinese within the reconnaissance squad and escort them to the Inner Palace. This is the first and last missive we received. Do you understand what it means?”

Yayul Mok stopped short.

Behind him, Namho had been quietly watching the situation. Then he suddenly realized something and muttered as if groaning.

“He deliberately didn’t tell us.”

“Elder Namho, what do you mean?”

“There is no need to say more. The two chieftains here and the warriors in the reconnaissance squad are all people who follow the Palace Lord. If they were told about the trouble in the Inner Palace, they would surely interfere somehow. He probably intended to call them back after everything was finished. Or…”

Namho continued with a grave look in his eyes.

““Or… the Blood Monk. He may have planned to let that old monster deal with them.””

“……!”

“A borrowed knife to kill others. Baeksang and Dark Heaven chose a useful blade. No, in this situation, it isn’t even someone else’s blade. There is a strong possibility that the Blood Monk is in league with them as well.”

A frigid silence descended over the group. Seeing their unsteady gazes, Namho felt his heart grow heavy.

*This is bad. The worst.*

Behind them was the Nanman Beast Palace, which was likely under Baeksang and Dark Heaven’s control by now. Ahead of them was a mysterious Supreme Peak master they could not oppose on their own.

And in this situation, even Jin Taekyung—the person they trusted more than anyone—was absent.

*What in the world are we supposed to do?*

Even after a lifetime in the Hidden Shadow Pavilion, Namho could not easily find an answer. But they had to make a decision before it was too late.

Amid the suffocating feeling that invisible chains were wrapped around his entire body, Namho finally forced his lips apart.

“Where are the others?”

Chief Jang understood what he meant and answered.

“If you mean the Han Chinese, we detained them as a precaution. We did not harm them in any way. We merely struck their Sleep Acupoints.”

“……”

“Do you intend to send them back to the Central Plains?”

The question caught Namho squarely off guard. After a brief silence, Namho nodded heavily.

“I’m sorry. But for now, this is the best option. If they cross the Yangtze and report what is happening in Nanman, the Murim Alliance will never stand by and do nothing.”

“……The Murim Alliance.”

“I was born in Nanman and spent half my life in the Central Plains. Though I am nothing more than a powerless old man, I am someone who understands the circumstances of both Nanman and the Central Plains better than anyone. If it is the Murim Alliance I know, they will find a way to help Nanman.”

His voice was calm, but it carried a powerful resolve.

Beyond the dense grass where they were lying in ambush, the two chieftains gazed at the broad, endless waters of the Yangtze before opening their mouths with sighs.

“Damn it.”

“What should we do?”

Namho had already finished thinking. His answer came without hesitation.

“There are two ways. First, release the Han Chinese, leave this place at once, avoid Baeksang’s eyes, and wait for the right moment. Second, head to the Central Plains together with the Han Chinese.”

“Head to the Central Plains together? There is no ship of sufficient size anywhere around here. How are we supposed to—”

“There is one. A ship large enough to carry everyone.”

The voice came from somewhere nearby.

Everyone turned at once to see Sama Pyo staggering to his feet with Taishan’s support.

“Is that true?”

At Chief Jang’s question, Sama Pyo answered with a pale face.

“How do you think we managed to come all the way to Nanman?”

“Could that mean…”

“The swift ship of the Yangtze River Channel League is not far from here. It’s half a day to the west. If we travel for even half that time, we might be able to rendezvous with it.”

Unexpected good news brought hope to the two chieftains’ faces.

Even reaching Sichuan by following one of the Yangtze’s tributaries would bring them within the domain of the Central Plains Murim.

Even if Baeksang and Dark Heaven had seized control of the Nanman Beast Palace, the arrival of reinforcements from the Murim Alliance—with the Nine Sects and One Gang and the Five Great Families at the forefront—would be more than enough to turn the situation around.

*There are already three prestigious great sects in Sichuan alone. Even if the Murim Alliance’s official reinforcements are delayed, those three will be different.*

Namho calmly sorted through the situation.

The Emei Sect, the Qingcheng Sect, and the Sichuan Tang Clan.

Even though they had shed much blood and weakened during the Sichuan Bloodbath, their roots ran deep and firm enough that even Dark Heaven could not tear them out in a single stroke.

Moreover, all three sects considered Jin Taekyung their Benefactor. If they answered the call, gathered the strength of Sichuan Murim, and headed for Nanman…

*It would take seven days and nights at the fastest to return. Ten days at the latest.*

Namho was neither a hot-blooded youth nor a martial artist who trusted in his own martial arts. That was why his judgment was colder and more accurate than anyone else’s in this place.

*If I lead these people back the way we came, we will certainly die. But if we bring in the strength of the Central Plains, we have more than enough of a chance. Until then, Jin Taekyung and the Beast Miao King will…*

They had no choice but to trust them.

To hope they would hold out. To hope they would remain alive until Namho and the others returned.

And just as Namho was muttering that hope—one he could not even fully convince himself of—in his heart…

Boom. Boom. Booooom!

Namho heard it.

No—everyone lying in ambush within the forest overlooking the endless river could both see and hear it.

A drumbeat that rumbled low, and a sleek hull riding the currents of the Yangtze as it approached.

“What is that…?”

“The Yangtze River Channel League. That’s the Yangtze River Channel League’s swift ship!”

But the next moment, the two chieftains, who had been celebrating with brightened faces, sensed something strange and fell silent.

The swift ship should have been at least half a day away to the west.

Why had it appeared here?

The question flashed through their minds. Then, when they saw Namho and Sama Pyo’s rigid expressions, it transformed into unease.

Namho’s words, which escaped like a groan, revealed the truth.

“Prepare for battle.”

“……!”

As the group was swept up in a chill of fear, Namho thought of the one person who was not beside him.

The one whose presence he needed more desperately than ever.

*Damn it. I’m sorry.*

Along with the thought that they might die before they could save him.

*Crash. Boom.*

The hull cut fiercely through the water and ran hard aground on the sandy shore.

And then…

*Step.*

In the place where a wave had swept through, one person’s footsteps were etched into the ground.

* * *

Whoosh!

Two streaks of light flew through the air, cleaving space.

Despite their strange movements, the twin wheels came at me like flashes of light. I swung White Flame diagonally downward to meet them.

KWA-BOOM! Rumble-rumble!

A tremendous roar erupted as a shockwave tore through the area and shook the air. But it was not over yet.

My five senses, sharp as blades, tracked every movement of the twin wheels behind me.

*They’re coming again.*

As Muyaho slid backward, I caught him by the nape and twisted my body.

Whoosh—shhk!

A blue flash barely grazed my body. Along with the sharp sound of something being sliced, I saw the White Tiger’s snow-white fur scatter through the air.

In my tilted field of vision, another sight came into view: a wild-haired freak charging at me like a mad bison.

“You bastard—!”

The Black Hand Fist Demon.

Black Force layered itself over his dark fist, and then he shot it straight toward my chest.

Whoom!

I could feel it—the wave of air, and the terrifying power contained in his punch. But…

*That won’t be enough.*

With a brief mutter, I straightened the body I had twisted as far as it would go. By then, the black Force had already reached point-blank range and was giving off an ominous light.

Beyond it, the Black Hand Fist Demon’s eyes gleamed with madness, as if whispering to me.

*You’re dead now.*

It was a gaze filled with certainty. I had seen that same look in the eyes of many enemies before.

From Third Rate swordsmen to Supreme Peak masters. Regardless of their level of martial arts, they had always worn that expression.

And when everything was over, I was always the one still standing on two feet.

*Swish.*

In the slowed-down world, the cool feel of the spear shaft slipped away from my hand.

The Black Hand Fist Demon had entered with such exquisite timing that the spear’s advantage had disappeared.

Without a moment’s hesitation, I let go of the spear and thrust out a palm.

KWA-BOOM!

Two Forces of different colors collided with a deafening roar.

Everything within a radius of ten-odd jang[^1] melted beneath the horrific heat, and the Black Hand Fist Demon’s eyes flew wide open.

“You…”

A single clash. But it was enough to measure each other’s strength.

Even though the twin wheels had made me react half a beat late, I had easily blocked the Black Hand Fist Demon’s punch. Looking into his wavering eyes, I spoke calmly.

“A nobody. Right?”

“……!”

He had realized that something had gone wrong, but it was already too late.

I clenched my empty hand.

Fwoosh.

Blue-white flames surged up around my fist.

Flame-Extinguishing Divine Fist.

KWA-AAANG!

[^1]: A *jang* is a traditional Korean unit of length, roughly three meters.

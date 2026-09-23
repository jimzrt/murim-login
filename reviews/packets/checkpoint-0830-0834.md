# Checkpoint Review — 830–834

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

# Chapters 830–834

## Plot

The Doppelganger claims Asmodeus overcame the gods’ curse and will return. Jin is pulled into a vision of a monster-ravaged future, but escapes when the System firewall blocks the illusion. He destroys the Doppelganger, only for Main Quest [Cataclysm] to fail: the summoning was not stopped, and the Rift begins at 10%. After warning the Skeleton King to alert the World Hunter Federation, Jin collapses and is transferred to Murim.

Elsewhere, Ahomed Jemal Pasha and the Prophet’s remaining mage disciples complete their ritual, summoning a red-eyed being. Jin dreams—or sees a vision—of that being killing Ahomed and attacking the gathered crowd, but cannot tell whether it is real or prophetic. He wakes in Nanman, where the System’s Status Window is inaccessible, his [Broken Body] injury still hurts, and Jeok Cheongang has gone to fetch the Divine Physician. Taishan returns with a giant beehive as a supposed cure, sending the party retreating to their carriage.

## Continuity

- Jin is the World Hunter Federation’s Alliance Leader. He erased the Doppelganger, but Main Quest [Cataclysm] and its “Stop the Summoning” mission failed.
- The Rift has begun at 10%. Its progress increases magical power, and unidentified beings are invading.
- The Prophet’s remaining mage disciples completed their prepared ritual under Ahomed Jemal Pasha. A black-haired, red-eyed man appeared; his identity is unknown. Jin doubts he is Asmodeus.
- Jin’s vision of the summoned man killing Ahomed and attacking the crowd may be a dream, a System-delivered vision, or prophecy; its nature is unresolved.
- The System called Jin “the Chosen One” and “the Master of the Ark,” activated a firewall against the Doppelganger, and transferred Jin to Murim while he was unconscious. The meanings of the titles and the Ark remain unknown.
- Jin has awakened in Nanman after being unconscious for several days. The Status Window is inaccessible, possibly due to a System update.
- Jin’s [Broken Body] injury remains unresolved and causes pain around his lower dantian. Jeok Cheongang has gone to Sichuan to bring the Divine Physician, his former Disciple, to treat him.
- Taishan returned with a giant beehive, prompting the party to retreat to the carriage.

## Translation Decisions

- Keep magical power distinct from mana. Keep Blink distinct from Teleport and Warp; extended-range Blink causes severe strain.
- Keep Fire Storm and Aqua Storm distinct named spells. Render [영웅의 검] as “Hero’s Sword,” 에어 슬래시 as “Air Slash,” and 실드 마법 as “Shield magic.”
- Render 선택받은 자 as “the Chosen One,” 방주의 주인 as “the Master of the Ark,” [격변] as [Cataclysm], [어데 도씹니꺼] as “Where’s Your Do Clan From?,” and [종족 학살자] as “Species Slayer.”
- Render 일섬 as “One Annihilation” and 벌집 as “beehive”; the mistaken “honey” and “pot of honey” identifications are part of the joke.

## Durable state

{
  "active_continuity": [
    "Jin Taekyung is the World Hunter Federation’s Alliance Leader.",
    "Jin erased the Doppelganger, but Main Quest [Cataclysm] and its “Stop the Summoning” mission failed.",
    "The Rift began at 10%; its progress increases the distribution and concentration of magical power.",
    "The System transferred Jin to Murim while he was unconscious; he has awakened in Nanman after being unconscious for several days.",
    "The System’s Status Window is currently inaccessible; Jin suspects an update may be responsible.",
    "Jin saw a vision in which Ahomed’s ritual summoned a black-haired man who killed Ahomed and unleashed a destructive storm of magical power; whether the vision was real remains unknown.",
    "Jin believes the summoned man is not Asmodeus, but does not know his identity.",
    "The Prophet’s remaining mage disciples completed their prepared ritual, and Ahomed was the mage who led it.",
    "Jin’s [Broken Body] injury remains unresolved, causing pain around his lower dantian; leveling up did not heal it.",
    "Jeok Cheongang has gone to Sichuan to bring the Divine Physician, his former Disciple, to treat Jin.",
    "Taishan returned with a giant beehive as a supposed cure for Jin."
  ],
  "continuity_sources": [
    833,
    834
  ],
  "open_questions": [
    "Why did the Main Quest fail despite the Doppelganger’s erasure, and who or what was summoned?",
    "Was Jin’s vision of the summoned being real, System-delivered, or prophetic?",
    "What will happen as the Rift progresses and more beings enter the world?",
    "Who or what chose Jin, and what is the Ark?",
    "What changed in the System update, and when will its functions return?"
  ],
  "safe_through": 834,
  "temporary_decisions": [
    "Keep magical power distinct from mana.",
    "Keep Blink distinct from Teleport and Warp; extended-range Blink causes severe strain.",
    "Keep Fire Storm and Aqua Storm as distinct named spells.",
    "Render [영웅의 검] as “Hero’s Sword,” 에어 슬래시 as “Air Slash,” and 실드 마법 as “Shield magic.”",
    "Render 선택받은 자 as “the Chosen One,” 방주의 주인 as “the Master of the Ark,” [격변] as [Cataclysm], [어데 도씹니꺼] as “Where’s Your Do Clan From?,” and [종족 학살자] as “Species Slayer.”"
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 830

# Chapter 830

Master of the Demon Realm. Lord of the monsters.

Demon King Asmodeus.

How could I ever forget that name? The demonic being who was the starting point of every catastrophe, its very source.

“I-I didn’t do it because I wanted to! Have you forgotten that it was all on the king’s orders?”

I silently looked down at the Doppelganger, shouting in desperation. After a brief moment of hesitation, I drew back the internal energy I’d been channeling through my foot.

“Cough, hack.”

The pressure on its chest lifted, and it immediately broke into a fit of coughing.

The Doppelganger let out the breath it had been holding, then glared at me with eyes full of pain and fury. But deep inside them, fear lurked—fear it hadn’t quite managed to hide.

It looked so helpless that it was hard to believe it had once been a named monster at Level 170.

But the small shadow before me now was the Doppelganger’s true nature. Its one and only truth.

*It must have stolen countless lives to become so powerful.*

It had taken whatever it could, absorbed it, and digested it.

It had climbed to the heights of power on the backs of those lives, using them as food and stepping-stones.

But today, the feast it had so happily gorged itself on would come to an end.

Its fanatical followers, who’d worshiped it like a god, were gone. So was its army of monsters. With no one beside it, only one path remained.

“Spit it all out.”

*Crick.*

The crushing pressure I’d lifted a moment ago bore down through the tip of my foot once more. I watched the Doppelganger let out a muffled groan, then continued in a low voice.

“What you know. And what’s about to happen.”

Demon King Asmodeus.

Evil itself, and its source.

What I wanted from the Doppelganger was information about that accursed being—and the future of this world.

“What you said just now.”

The hoarse voice that slipped from my lips sounded like someone else’s.

My mouth felt as rough as if I’d swallowed a handful of sand. It wasn’t just exhaustion and thirst.

“He—the Demon King…”

Each syllable was a struggle. I didn’t dare say it aloud, or even imagine it.

But I knew.

I knew what became of those who turned away from reality, and what waited beyond the reality they’d tried so hard to ignore.

To escape a forest fire, you have to recognize that the fire is there.

You have to see the smoke billowing up and the red flames raging, and feel the heat that threatens to burn you alive.

Just as I was doing now.

“Is he still alive?”

In the suffocating silence, the sound of little bits of stone falling from overhead rang out with unusual clarity.

Neither I, nor the Skeleton King, nor the Doppelganger spoke.

Not for a brief moment.

Until I heard the whisper of a shadow, something not of this world.

“Is he still alive?”

*Stir.*

The darkness rippled. A pitch-black abyss, where its features were barely distinguishable, split into a long grin.

“You do not know, Chosen One. And yet you are also a foolish mortal, destined one day to be broken by time and crumble into dust.”

The Doppelganger was laughing.

It had forgotten its anger, pain, and fear of me.

Or perhaps it had covered them all with the presence of its absent master.

“Our Great King overcame the curse of the gods. He may waver, but he will not break. Even if he perishes, he will rise again. And at last, he will make all the earth and water in this world his own.”

“……!”

“That is the only truth. A truth you cannot stop, even knowing it—a truth that will become reality in the not-too-distant future.”

I stared blankly at the Doppelganger, laughing aloud.

And the moment I met its eyes, darkness swirling within them, I felt my vision grow hazy.

*This is…*

No sound came from my throat. The sand and rubble that had filled the area, the Skeleton King, the Doppelganger—they all vanished.

No. It felt as though my entire consciousness was being pulled somewhere.

At the same time, a vision unlike anything I’d ever seen came pouring into view like a meteor shower.

*SHWAAAAA…*

A brilliant sun rose in the east, bathing the world in light. Clouds raced across the blue sky. Before long, the moon rose with the glow of sunset, and darkness fell.

One day, then another.

It rushed by like a scene from a nature documentary I’d once watched, but there was nothing beautiful about it.

*BOOOOM!*

A tremendous blaze erupted with a thunderous roar.

The wild animals living in the vast wilderness bolted all at once, as if on cue. With flames like a setting sun at their backs, monsters marched across the horizon.

*Rumble…*

Hundreds of thousands. Millions.

Perhaps even more.

A horde of monsters beyond counting poured in from every direction. They shook the earth and blotted out the sky.

*Kyaaaaargh!*

A terrible roar rang out from above the clouds.

Huge wings swept across the clouds and blotted out the sunlight. Then, all at once, the shadow they cast fell over my eyes.

*Whoosh.*

My vision flipped. The sky and earth turned upside down.

And in the transformed landscape, I saw a city burning.

*BOOOOM!*

Hundreds of cannons fired at once. As giants standing shoulder to shoulder with skyscrapers staggered, engulfed in flames, figures shot forward like streaks of light and charged through the ruined streets.

They wielded weapons blazing with radiance and shouted their resolve as if spitting blood.

“Never retreat! Stand and fight!”

“For humanity!”

They were Hunters.

The sword and shield protecting humanity from the accursed beings.

Warriors given a sacred mission by someone unseen.

I couldn’t even twitch a finger. From high above, I watched their magnificent charge.

They fought monsters dozens of times their number. As if to prove their cries true, they never retreated. They fell, spraying their blood for humanity.

Until the sun went down and the moon rose.

Until the very last one.

All I could do was watch.

As if someone were controlling me, I saw Niagara Falls turn red with blood. I saw hundreds crushed to death beneath the shattered Leaning Tower of Pisa.

I was a consciousness that did not exist, nothing more than a spectator.

There was nothing I could do.

In a landscape changing without pause, the one right—and curse—granted to me was to see the civilization burning to ash and hear the screams of the dying.

Countless deaths. And destruction.

The streets were carpeted with corpses. A broken church cross lay plunged into a pool of blood.

A child, unaware of what had happened to their parents, could no longer bear the hunger and crawled out of a small box. When the child saw a pack of goblins in the alley, the doll in their hand fell to the ground.

Catastrophe.

A word for an unexpected, unfortunate disaster.

But even that word, a symbol of the Great Cataclysm, could not begin to describe the horrors I had seen.

In place of the voice that wouldn’t come, one word suddenly occurred to me.

*The end.*

Yes. It was the end.

The civilization humanity had built over countless years was destroyed, and not a glimmer of hope remained in people’s hearts.

To be exact, their hope was already dead.

One person at a time. Slowly.

Torn into hundreds or thousands of pieces, they disappeared into the bellies of hungry monsters.

“For Magic Johnson.”

A quiet voice rang out across a vast plaza flickering with countless candles.

A face both familiar and unfamiliar.

Team Leader Choi, his face covered in scars and one arm gone, drained his glass.

Xiao Shen lifted a bottle with tearful eyes and filled the empty glass.

“To ‘Uncle Chuck’ Hagel and our friend Stone King, who became eternal stars one year ago today.”

As I heard the names called out with every glass filled and drained, I understood.

This was a memorial for the fallen.

A send-off ceremony, a final remembrance of the heroes who had gone before us—the people who had been humanity’s hope.

And…

“To the bravest man of all.”

“To the light of humanity, who always illuminated the way for everyone as he stood against the darkness.”

My figure was nowhere to be seen.

“To Jin Taekyung…”

The trembling voice came to an end. Team Leader Choi drained yet another glass and clenched his fist.

*Crack.*

Blood ran from his hand, mingling with the shards of the shattered glass and dripping onto the ground. The candles went out all at once, and silence fell over the entire plaza.

At the same time, light swelled at Team Leader Choi’s waist.

*Fwoosh.*

The Hero’s Sword.

Though cracked and broken, its blade still held a keen edge. Brilliant radiance welled up from it.

The light embraced the entire plaza, where the candles had gone out, and faintly lit the deep darkness.

*Flap.*

A powerful wind, which had come from far away while no one was watching, whipped dozens of large and small flags.

A crossed sword and shield. Roughly depicted, but unmistakable: the emblem on the World Hunter Federation’s flag.

“There’s nowhere left to retreat.”

*Thud. Thud-thud.*

Thousands—perhaps tens of thousands—of feet stamped against the ground. The radiance gathered on the Hero’s Sword picked out their faces one by one.

“And we must not retreat.”

*Clang! Clang-clang!*

Blades clashed in the air, spitting sparks. The tanks slammed and pounded their massive tower shields like mad.

As if a giant heart were beating, they moved with a single purpose.

For those who had gone before them, and for the battle ahead, they looked to their new Alliance Leader.

They waited for his final words.

“Today, we fight until the very last person.”

*Chachachachang!*

“WAAAAH!”

Countless auras surged up at once, as if on cue. Their distant roar, raised as one voice, drove back the darkness.

The candles that had lit the plaza had long since gone out, but humanity’s flame still burned.

At least until they fell here today.

Until the darkness that would extinguish their final flame drew near.

*SHWAAAA…*

At that moment.

The wind stopped. The air trembled.

The plaza, heated to a fever pitch, turned cold. Countless eyes shifted in the same direction.

And there, stood a being cloaked in darkness.

“Ah…”

A moan slipped through someone’s lips and pierced my ears.

My senses, floating as if submerged in water, came back to me. The hairs all over my body stood on end.

*The Demon King.*

An instinctive fear and wariness stirred. Unlike before, I moved my head of my own free will. Following everyone’s gaze, I looked at him.

Demon King Asmodeus.

The accursed king who had once—and would again, in a future that had yet to begin—cast humanity into the flames.

And the moment I stared into the writhing darkness in the distance—

*Crack…*

The world around me collapsed. Every illusion shattered.
## Chapter artifact 831

# Chapter 831

I could’ve sworn I heard something like that.

*CRASH.*

The sound of a window shattering.

It was a signal that it was time to shed the illusion surrounding me and return to reality. An alarm waking my mind from its deep slumber.

*Fwoosh.*

The scenery around me melted away like ice cream. The cheers that had sounded so clear now seemed distant, like echoes.

“Chaaaarge!”

The final battle of this Great War. Perhaps the final battle on which humanity’s fate would rest.

Team Leader Choi strode forward, Hero’s Sword held high, and countless Hunters followed behind him like a surging wave.

Toward somewhere the moonlight couldn’t reach.

Toward a being standing alone, cloaked in darkness.

*No.*

Not yet. Not yet.

I reached out with all my strength. Through my blurring vision, I moved the body that had become entirely my own and took a step toward him.

Demon King Asmodeus.

I could see the back of the calamity. It wasn’t enormous or grotesque.

Even if all of this was an illusion that would never come to pass, I wanted to see his true form with my own eyes—the form no one had ever told me about.

I wanted to catch even a glimpse of him buried in the deep darkness, to feel the power coiled within him, if only for a moment.

*More. Just a little more!*

I didn’t know.

Maybe my desperate cry had echoed in my heart and reached him. Or maybe everything I was seeing and feeling wasn’t an illusion after all, but something else.

There was only one thing I could be sure of: something had reacted to my silent cry.

*Rustle.*

A figure slowly turning around. Darkness rippling.

“……!”

My heart lurched. An icy chill ran down my spine.

It made no sense. It was impossible.

But the Demon King was definitely turning toward me—and that was the last thing I saw.

*Flash.*

Everything around me disappeared. Team Leader Choi and Xiao Shen, the countless Hunters. And even Demon King Asmodeus.

But the darkness did not disappear.

No—an abyss-like presence was closing in, pressing in on me from every direction.

*What the hell is this…*

I was confused. I couldn’t make sense of anything.

Was what I was seeing another illusion? Or had I finally reached my limit, lost consciousness, and started dreaming?

And just as I was gripped by those questions—

*Ding.*

> **System**
> You are the Chosen One. The Master of the Ark.
>
> The System automatically activates its firewall.
>
> The System blocks a newly detected virus.
>
> Abyssal Swamp has been dispelled.
>
> Power of the Abyss dissipates.
>
> Level 10 “Final Abyss” Doppelganger has been blocked.

*Ding. Ding. Ding.*

Clear chimes reached my ears. Their sound rang out in every direction.

At the same time, the darkness that had writhed toward me like a living snake scattered rapidly.

It thrashed violently, as if confronted by something it feared.

And then I realized what this abyss was.

The being that had conjured all those countless illusions that came crashing down on me, too.

*Doppelganger.*

A line I’d read somewhere suddenly came to mind.

When you look into the abyss, the abyss looks back at you.

The short sentence meant something else, but what had happened to me was the same.

I looked at the Doppelganger, and the Doppelganger looked at me. And so I was dragged into the abyss it had created.

No. I had been.

But now I knew.

This was another illusion within reality. The Doppelganger’s power itself.

And I knew what I had to do.

*Fwoosh.*

Heat surged from my empty hands. Darkness writhed against the dazzling blue-white flames.

As if I’d made up my mind to do this long ago, I reached out with hands blazing with Scorching Yang Qi and seized the darkness.

*CRUNCH.*

And the instant I gathered my strength and tore it apart—

*SHRAAAK!*

I saw it.

The darkness, reduced to ash by the flames, crumbled away without a fight. Beyond it, the world I remembered came into view.

*Huff.*

Air mixed with dust flowed through my nose and mouth.

The chunks of stone that had hung in midair began to fall again. The Skeleton King came into view, staring at me with wide eyes.

*It all happened in an instant.*

Had even a second passed in reality?

But I’d experienced at least several hours—years’ worth of illusions—and returned.

There probably wasn’t a single survivor among those who’d gone through what I had. They must all have been absorbed by the Doppelganger.

“What the…”

It was impossible to explain in a few words, and there was no time to explain.

Instead of answering the confused Skeleton King, I shook my head.

Then I turned away from him and faced the Doppelganger, who was staring up at me, dazed.

“You—you… What are you…?”

*Rustle.*

Its body, wavering like a shadow, was slowly scattering—bit by bit, without pause.

What I’d torn apart with my flame-filled hands wasn’t just an illusion. It was the Doppelganger’s body, its very life.

“I got a good look at your last-ditch effort.”

“……!”

“Yeah. I figured there had to be some reason that dog barking its head off this whole time was cooperating so easily.”

At my offhand remark, the Doppelganger shuddered.

Whenever darkness welled up from it in bursts, like spurting blood, and scattered like ash, the shadow that was its body shrank.

“Honestly, it wasn’t a bad attempt. If I’d been in my usual shape, you wouldn’t have stood a chance, but… I didn’t expect some bastard to come flying in without even signaling.”

“This can’t… This can’t be happening.”

“If a bastard like you can exist, why can’t a bastard like me?”

The Doppelganger muttered as if groaning.

“The Chosen One…”

The Chosen One. The Master of the Ark.

I didn’t know why the Doppelganger and the System called me that.

I didn’t know who had chosen me, or what the Ark was. I couldn’t know that right now.

But if those two words referring to me weren’t just nonsense, then I knew at least this much: stopping that fucked-up scene the Doppelganger had shown me must be the mission I’d been given.

“Be prepared. Everything you saw will soon become the future—and reality.”

“Are you sure? I may be a genius, but I’m not exactly planning to die young.”

The Doppelganger laughed out loud at my reply. Its helplessness and madness were impossible to hide now that it had accepted its complete Erasure.

“If the King returns, will you still be able to say the same thing?”

I thought of the deep darkness I’d seen in the illusion.

I thought of that last glimpse of Demon King Asmodeus, whose appearance I’d never managed to make out clearly. I thought of the overwhelming strength I’d felt from him, even from a distance.

*If I fought him, could I really win?*

An empty question.

I already knew the answer.

Demon King Asmodeus was strong. No—there was no point even talking about how strong he was.

If that had been reality, and the power I’d felt was real, just meeting his gaze would’ve frozen my hands and feet.

But sometimes, a question can have more than one answer.

Especially when I’m the one solving it.

“If it were me right now, I’d definitely die. Miserably, without even managing to hurt him properly.”

At my answer, the Doppelganger’s laughter grew louder. It didn’t seem to care that more than half of its body had already disappeared.

“Yes. That is the truth. Accepting the death our King has decreed is all you can do…”

“You’re leaving out a premise.”

“What?”

I looked at the Doppelganger as it fell silent and continued slowly.

“If it were me right now. That’s the most important premise.”

At some point, I’d changed. I’d had no choice but to change in order to survive, in order to protect what mattered.

I’d thrown away the caution I’d held on to as an F-rank Hunter. Sometimes I’d faced my enemies with courage—and with even more recklessness.

And every time I risked my life in a fight, I’d reaped the rewards of that risk.

*That’s how it’s been so far, and that’s how it’ll keep being.*

The me of now and the me of the future are different.

So the future has to change, too. Whatever risks I have to take—even if it costs me my life—I’ll change it with my own power.

That’s all I can do. And it must be why some unknown someone chose me.

“An illusion is just an illusion. We’ll have to wait and see how the future changes… but some bastard who’s about to drop dead won’t be around to find out, so it’s none of his business.”

The Middle Dantian is moved by mental strength, and mental strength comes from the firmness of one’s heart.

I won’t be shaken by a horrible illusion, or by a few words from the Doppelganger.

“And you seem to have forgotten something important.”

I was tired. I felt like I could collapse at any moment.

But as I looked down at the Doppelganger, which had stiffened, I wanted to make sure I said this.

“The future’s already changed.”

I tugged at the corner of my mouth, stiff with dried blood. Then I forced the words out, fighting the sleepiness washing over me.

“I put an end to the plan you came up with. With my own hands.”

I didn’t know exactly how the Doppelganger had planned to get the results it wanted.

I’d wanted to hear it directly from the thing itself, but it would be completely gone in a few seconds. There was no point asking now.

I could find everything out.

Even if I had to scour the whole world, I’d track down every trace of the Doppelganger and pull up every root it had left behind somewhere. Then the illusion would remain an illusion.

The future, once filled with horrible calamities, would be filled with peace.

*I can do it.*

This wasn’t just a wish. I was certain.

At long last, the world had come together as one. I’d sounded the alarm for those who’d been complacent in their peace, and doused the powerful—who’d been turning their backs on reality—with a bucket of cold water.

And I’d brought those known as humanity’s sword and shield, the countless Hunters, together under one flag.

The World Hunter Federation.

A group that transcended gender, race, age, and national borders.

I was the Alliance Leader at the head of that vast federation.

Everyone had chosen me. Everyone trusted and followed me. So there was no room in my heart for the word *impossible*.

“So…”

My voice trailed off, growing weak.

My vision slowly tilted against my will. Without a word, the Skeleton King suddenly came up beside me and reached out to support me.

He helped me finish what I hadn’t yet managed to say.

“Quit your bullshit and go link arms with your friend who went ahead of you. You can watch from there.”

*Whoosh.*

My toe came down hard, with a heavy rush of air.

And in that moment, an inexplicable sight flickered into my hazy vision.

*Was it… smiling?*

I couldn’t possibly know.

Was it a phantom brought on by exhaustion, or an incomprehensible reality?

Before I could even think back over that fleeting question, the toe, still wreathed in a faint flame, had already stamped down on the shadow. It led a monster that had lived through ages beyond imagining to Erasure.

*BOOM!*

The shadow shattered and scattered with a deafening crash. Through it rang the clear chime announcing the Doppelganger’s Erasure.

*Ding.*

It was over. At last.

At least in that moment, I was sure it was.

Until an unpleasant noise pierced my ears.

*Beep.*

> **System**
> Main Quest Cataclysm has failed!

…What did it say?
## Chapter artifact 832

# Chapter 832

Sometimes, life throws you a curveball.

A moment when something you’d always taken for granted—one is followed by two, and two by three—suddenly takes an unexpected turn.

But I’d never once imagined this outcome.

*Beep.*

> **System**
> Main Quest Cataclysm has failed!

…What?

I froze like a statue and stared blankly at the holographic window floating in the air.

Inside its translucent frame, the words on the screen said exactly what I’d just heard.

Main Quest. Failed.

The two words drilled into my retinas, tearing through the emptiness in my mind and leaving me reeling.

*Why? How could this happen?*

My lips moved on instinct, but no sound came out.

With endless questions swirling in my mind, I shook my head. The world spun around me. No matter how I looked at it, I couldn’t make sense of what was happening.

Was I dreaming?

Or was I still trapped in an illusion the Doppelganger had created?

I wanted that to be the case.

But, unfortunately, the truth was different.

“……Human, snap out of it!”

A voice reached me through my blurred vision. If the Skeleton King’s hand shaking me was proof that this was all real—

*Ding. Ding. Ding.*

The chimes still rang out without stopping. And the darkness, scattering into the air like ash, was proof that one being had been erased.

> **System**
> You have defeated Level 10 “Final Abyss” Doppelganger.
> 
> Due to the extreme level difference, you receive no Reward.
> 
> With the death of this target, the Doppelganger species has been completely wiped out.
> 
> You have completely eradicated a species. The name Doppelganger will now slowly be forgotten as time passes.
> 
> You have achieved the very rare achievement, Where’s Your Do Clan From?[^1]
> 
> As a Reward for achieving a very rare achievement, you have gained a massive amount of EXP and Fame!
> 
> You have acquired the Title Species Slayer!
> 
> Level Up!

Another Level Up. And then, recovery.

*Fwoosh.*

Focus returned to my sight, which had been clouded by thick fog. Energy surged through my revitalized body, stronger than before.

But none of that mattered to me now.

Something else was far more important.

I’d failed the most important Quest—the one I’d been certain I would complete.

*The Doppelganger was definitely erased. It was.*

My body was brimming with strength, but my mental reserves had run dry long ago.

The shock hit me hard, and I staggered.

Michael Silbert was dead. The Doppelganger was dead. I’d personally eliminated every being that threatened this world.

I’d thought it was over. It should have been over.

Even if a new threat came someday, one that would plunge the entire world into a sea of fire, I’d believed we’d at least bought ourselves time for now.

But we hadn’t.

*That smile.*

I couldn’t breathe. A terrible headache stabbed at my brain like an awl, and I remembered the Doppelganger’s final moments. That faint smile I’d thought I’d only imagined.

*I didn’t see it wrong…*

I’d been wrong.

What I’d seen at the end hadn’t been some passing illusion. It was the smile of someone who had finished everything they needed to do.

Where had things gone wrong? Had I lacked the effort, or the strength?

Or had the enormous calamity I’d tried to stop been in preparation for so long that no mere human could have prevented it?

I didn’t know. There was nothing I could figure out.

I was only sure of one thing: something that should never have happened had begun.

*Boom. Ba-boom.*

A drumbeat suddenly reached my ears.

It wasn’t a clear chime or a mechanical warning. It was more ominous than anything I’d ever heard—a war drum heralding the dawn of a great war, and a warning from the System.

*Ba-boom.*

> **System**
> Main Quest Cataclysm has failed.
> 
> Some details in the Quest window have been updated.
> 
> Mission: Stop the Summoning (Failed)
> 
> You have failed to complete the mission.
> 
> The boundary of the Demon Realm has temporarily opened. Unidentified beings are invading this world.
> 
> A page of history is turning, and a new age is right around the corner.
> 
> The Rift has begun.
> 
> Current Rift progress: 10%
> 
> As the Rift progresses, the distribution and concentration of magical power will rise sharply. This may vary depending on location and the passage of time, and may have greater or lesser effects on the laws and living beings of this world.

“……!”

I stared wide-eyed at the new holographic windows.

The Demon Realm.

A cursed world no one had ever glimpsed, crawling with nothing but darkness and monsters.

A land of death ruled by Demon King Asmodeus.

It was only temporary, but the Demon Realm had opened.

Cursed beings, summoned from another dimension by someone else, had set foot in this world.

A rift. And magical power surging.

*So this was it. The plan the Doppelganger had been preparing.*

I’d underestimated it far too much.

It had been clever enough to manipulate the whole world from behind Michael Silbert, to establish itself as a divine being in a vast religion.

And I’d thought a creature like that wouldn’t have prepared a failsafe for a plan it had spent over thirty years working on?

Bombs don’t care who owns them. Whoever holds the switch, the slightest jolt is enough to set one off.

Just like now.

*Dammit.*

My mind went white.

The bomb had already gone off, and the rift had begun. This was a calamity that would spread like wildfire, one that couldn’t even be compared to mutation Gates or monster waves.

“We have to stop it. Right now.”

*Grab.*

I seized the Skeleton King’s wrist, my voice urgent.

He’d been watching me behave incomprehensibly since the Doppelganger died. His face twisted in confusion as he shouted.

“Get a grip, human! It’s already dead.”

“No.”

“What?”

“This is just the beginning. It’s not over.”

“What are you talking about—”

“Tell the main force. The World Hunter Federation. Right now.”

My breathing was ragged. The hand gripping the Skeleton King trembled.

I was tired. I wanted to rest.

The mental exhaustion that had been eating away at me, combined with the shock I hadn’t seen coming, kept dragging me toward the darkness.

The sleep demon pressed down on my eyelids with the weight of a mountain.

But—

*Crack.*

I bit my tongue and fought off the sleep washing over me. Forcing my fading consciousness back, I continued.

“We failed, and the Doppelganger’s plan has come to fruition.”

“……!”

“They’re coming.”

That was all I managed to say.

*Slump.*

“Human! Human!”

The Skeleton King tried to haul me up with his powerful hands, but my body went limp against my will.

After a long fight, as my consciousness sank from exhaustion, I thought of the best thing I could do right now.

*Murim.*

The Main Quest had failed, but regardless of the outcome, the System’s restrictions were gone. The wall separating the two worlds had crumbled.

Now I had to return there.

To the other world that had given me a second life.

To the place where time flowed so slowly that it could delay the flames of calamity.

But…

But why was I so sleepy? Why couldn’t I think of anything?

*Log…*

The three syllables I’d always shouted with all my strength scattered into emptiness in my mind.

My thoughts sank beneath the water before I could finish that one short word.

And just as I was about to plunge into complete darkness—

*Ding.*

Along with a clear chime, a voice like a hallucination reached my ears.

> **System**
> The System is automatically executing a new update.
> 
> The System wishes to move the Player under its authority. Do you accept this offer?
> 
> The Player has not responded. Proceeding automatically.
> 
> Connecting to Murim.
> 
> Countdown begins.
> 
> 10, 9, 8……

.

.

.

> **System**
> Login successful.
> 
> May fortune favor you in battle.

*Fwoosh.*

As a burst of light announced the opening of a new world, I let go of the last thread of consciousness I’d held on to.

* * *

Ahomed Jemal Pasha.

By ordinary standards, his name was long. For a man from the Middle East, it was short. And he was trembling with joy, along with the dozens of companions gathered around him.

“Ah… Ahhh…”

“Inshallah!”

It had been an unbearably long time. It was true for Ahomed, whose family had followed God’s will for generations, as it was for the others.

Despite being blessed with a talent for magic that others would have envied, they’d had to live like criminals, hiding from the world. They’d also had to conceal their great plan to change the world’s fate.

But…

*We did it. At last.*

Ahomed felt hot tears running down his face before he even realized it. He had devoted his entire life to following only the Prophet’s words.

In the old mage’s eyes lay the relief of someone finally free of all his hardship, the joy of fulfilling God’s mission, and worry and sorrow for someone who wasn’t there.

*O Prophet. Our guiding light. Where are you now?*

He had an inkling of what it meant that the Prophet, who had set out to face the infidels’ army, hadn’t returned.

But Ahomed didn’t let those feelings show.

If the Prophet had died, then it was a holy sacrifice to fulfill God’s mission—a martyrdom. He must not grieve.

*Perhaps he foresaw a day like this long ago.*

No. A great prophet like him would surely have foreseen all of this.

That was why, before he left, he had summoned Ahomed, the one in charge, and urged him to do this.

> “Ahomed. If I haven’t returned by dawn three days from now, you and the others who remain must complete the mission.”
>
> “P-Prophet, how could you say such a thing?”
>
> “It’s only a precaution. If you all don’t stay here to protect everyone and carry on the mission, how can we fight the infidels’ army without worry?”
>
> “B-but…”
>
> “I trust you, Ahomed. You are my brother and Disciple, bound to me in the name of God.”

Neither the Prophet—no, the Doppelganger—nor Ahomed knew.

They didn’t know that he would never return. That he would be erased forever by the hand of a single human.

But, impossibly, all of it had come to pass. Sensing that something had gone wrong, Ahomed led the mages who had learned from the Prophet alongside him, and they stood before the magic circle they’d been preparing for so long.

And now, in this very moment—

They watched the darkness rise, devouring more Magic Gems than they could count.

“O Messenger of God! O God’s hammer, come to set this defiled world right! At last, descend upon us!”

In that moment, a cry rang out, filled with a lifetime of resentment and a faith that could only be called fanatical.

*Fwoooooosh.*

Amid the deep darkness, red eyes flashed.

[^1]: The Korean title is a dialect-flavored pun that sounds like “Where are you from, Mr. Do?” while also evoking a question about one’s ancestral clan.
## Chapter artifact 833

# Chapter 833

Dazed.

A sensation of floating, as though gravity didn’t exist, took over my entire body.

Jin Taekyung opened his eyes amid that alien sensation and stared blankly at the unfamiliar sight spread out before him, beyond a field of vision full of static like a broken television screen.

*Where am I?*

He looked around, and the answer came quickly.

Stalactites hanging from the ceiling. A damp floor and humid air.

He hadn’t recognized it right away only because it was so vast that it defied common sense, but this was a cave.

And in that place, where the hand of man had clearly been at work, a crowd of tens of thousands had gathered, by his rough estimate.

“Ooh. Ooooooh…”

“Inshallah!”

Shouts reached him from far away, like echoes.

At the cry of someone wearing a long robe, countless people sank to their knees, rippling through the crowd like dominoes.

The hunched old men, the men and women clasping both hands together, even the children whose innocent eyes had been sparkling—all of them did the same.

No. They were the only ones there.

Ordinary people, the kind you could see anywhere in the Middle East.

The only ones who stood out among them were a group wearing robes covered in mysterious patterns.

*Swish.*

The hem of a long robe brushed the floor. An old man with snowy white hair showing through his loosely wrapped turban spread both arms wide.

“O Messenger of God! O God’s hammer, come to set this defiled world right!”

At the sound of that shout, Jin Taekyung spotted something in the unfamiliar scene before him that was stranger than anything else.

*That’s…*

It was darkness. And fire.

The flames blazed using countless Magic Gems as kindling, filling half the vast cavern and piling so high they nearly touched the ceiling.

The darkness rippled like flames, so dense that it seemed strange he hadn’t noticed it until now.

An unprecedented energy seethed within, as if it might burst out at any moment.

*Fwoooooosh.*

The old mage’s eyes shone with rapture as he gazed at the bizarre sight.

His body trembled with awe, but he still managed to cry out one last time. The staff in his hands blazed with light.

“At last, descend upon us!”

At that moment—

*Crack.*

Like a child in the womb forcing its way into the world, the space beyond the tightly closed darkness opened its jaws.

At the same time, the black flames writhed violently like a twisting dragon and devoured countless Magic Gems. Unrefined, pure magical power raced along the magic circle carved into the ground and flowed into the flames.

On and on. Until the Magic Gems had poured out all their energy and crumbled to ash.

*Crackle.*

The mountain of Magic Gems crumbled. It collapsed in on itself.

Jin Taekyung watched, stunned, as the mass of magical power that had served its purpose lost all its strength and scattered.

He watched the enormous bomb he’d been searching for with such desperation ignite—the seed of calamity that had slipped away somewhere, hidden from the world’s eyes for decades.

And at last, the calamity in full bloom stepped through a crack in space.

*Step.*

A snow-white bare foot touched the ground. Two legs and two arms, no different from a human’s. And yet, his glinting red eyes proved that he was unlike anyone else.

*Haaah.*

The black-haired man, wearing not a single thread of clothing, breathed slowly.

Like a sailor returning home after a long voyage. Or a predator facing a mouthwatering meal.

Then, with the red glint from moments ago all but forgotten, he took in the new world through eyes that had turned pitch-black. He looked around and sensed everything.

The faint sunlight filtering through the ceiling.

The damp air, and tens of thousands of people pressed flat against the wet floor as if worshiping God.

And lastly, the old mage staggering toward him.

“Ah… Ahhh…”

The mage, Ahomed, stared at the man with tears streaming down his face.

Skin so translucent his veins showed through. A face so beautiful it was hard to believe. And a distant power surging within him.

There was no doubt.

The man before him was the messenger sent by God—a being who could truly be called a divine man.

“O Prophet, are you watching? At last, your prophecy has come true—!”

The instant Ahomed opened his arms toward the man—

*Slice.*

His voice, trembling with emotion, cut off abruptly. At the same time, the old mage’s body collapsed like a rotten log.

*Thump. Thud.*

His arms and legs, torn apart. His upper and lower body, severed.

And last of all, his head slid diagonally off his torso and hit the ground.

The man stared down at the dead face that rolled like a ball of thread until it reached his feet.

“You did well.”

That was all.

The darkness writhing around the man pulled in the old mage’s corpse, now split into dozens of pieces, and swallowed it. It broke it down, melted it, and digested it.

*Crunch.*

The horrible sound of bones and flesh being crushed echoed through the silent cavern.

“……!”

Tens of thousands of people froze as they witnessed the unbelievable sight with their own eyes.

So did the mages who, until just moments ago, had been filled with the joy of success—and the one man who had watched it all through a dreamy, half-real haze.

*That’s him.*

Jin Taekyung knew it instinctively.

That strange man standing alone was something that had no place in this world.

A demon who had crossed over from a world of death, cursed by God, through that slowly closing crack in space.

*Rustle.*

The darkness, which had greedily swallowed the corpse without a single drop of blood, coiled around the man from head to toe. It adorned him like luxurious black silk, then settled across his shoulders as a cloak.

No—at the same time, it surged upward like a pair of enormous wings.

*Flash!*

Jin Taekyung saw it.

The darkness stretching out without end, blotting out the sunlight seeping through cracks in the ceiling and casting death over the heads of the people frozen like statues.

The living and the dead.

A storm of magical power that swallowed everything.

As the cavern shattered and terrible screams filled the air, the nightmare surrounding Jin Taekyung broke apart, and he woke.

*CRUUUUNCH!*

* * *

*Hah.*

I opened my eyes and let out the breath I’d been holding.

At the same time, I saw an unfamiliar ceiling. My body swayed gently in time with the sound of hooves coming from somewhere.

“Ah.”

I let out a short groan and blinked. I steadied myself with a deep breath, and air thick with damp heat filled my lungs.

*This is…*

I didn’t need to look around carefully to know.

I was lying in a carriage, and the hot, humid air unique to Nanman—something I hadn’t felt in a couple of months—was familiar.

Of course, given the time difference with the modern world, it had probably been a few shichen, not two months.

*That last System notification wasn’t a dream.*

The sudden rush of relief drained the tension right out of me.

In my final moments in the modern world, my mental strength had been so completely depleted that I hadn’t even been able to attempt Login.

If the System hadn’t helped, even by force, I would’ve stayed collapsed for days without knowing what was happening… No, wait.

*System update?*

Those words had stuck out sharply amid my jumbled memories.

If all the System notifications I’d heard were true, then something had changed—something that had never happened before.

I hurriedly sat up and murmured to myself.

*Open Status Window.*

But, just as I’d half expected, nothing happened.

No matter how hard I stared into the air, no translucent holographic window appeared. I didn’t hear the clear chime that should’ve sounded along with the command, either.

“……Shit.”

The curse slipped out before I could stop it. I was taken aback, but I had a pretty good idea why the System had suddenly gone dead.

System update.

*Maybe I can’t use it until the update is complete? Something like that?*

I’d loved physical activity ever since I was a kid, so I’d lived far removed from computers. But any modern person with a smartphone had experienced an update.

Still, I was this flustered because I’d never expected anything like this.

*Come to think of it, this is a program too, so I guess it could update.*

I couldn’t help wondering what kind of lunatic made something like this and then updated it, but it had happened.

No, maybe it was only natural.

A System this insane existed—one that connected two worlds and let me level up like a game. An update was nothing by comparison.

And besides…

*After everything that happened.*

I remembered the unbelievable information the System had given me right after I erased the Doppelganger.

And in that moment, I realized once again that the enormous, horrible calamity I’d failed to stop had begun.

*Clench.*

My hand tightened without me realizing it. My fist had gone white and trembled. At the same time, the scene from the nightmare flashed before my eyes.

Honestly, I still didn’t know.

Was what I’d seen reality, secretly delivered to me by the System through a dream? Or was it a nightmare conjured by my confused subconscious?

Or was it something you might call a prophetic dream?

But despite my wanting it to have been nothing but a nightmare, I already had an instinctive suspicion.

*That wasn’t… just a nightmare.*

I’d seen it clearly, even through the static in my vision. I remembered it vividly.

The crack in space that had opened, if only for a moment, through the countless Magic Gems and magic circles—and the man wrapped in power so monstrously vast that he slaughtered tens of thousands of fanatics who couldn’t offer the slightest resistance.

No—the demon who, for some reason, looked human.

*No way.*

I forced myself to push the name that surfaced in my mind away.

I still didn’t know who he was.

But judging by the Doppelganger’s attitude when we talked and how things had played out, that man wasn’t Asmodeus.

Even if—if he really was a Demon King…

*I have plenty of time.*

Just as I’d shut myself away to train on Mount Jiuhua, I could spend a little over a year in Murim while only a few days passed in the modern world.

As long as the System existed, time was on my side.

*Dark Heaven might not be, though.*

I muttered to myself and got to my feet, looking around inside the carriage.

Had sleeping in a carriage become popular at the Nanman Beast Palace lately? The place was so spacious, even by my exaggeration, it was about the size of a large inn’s private wing—and I was alone.

*Well, it’s quiet, at least. But where is everyone?*

The familiar faces who should’ve been by my side were nowhere to be seen.

The people from the Fire Dragon Pavilion. Hyuk Mujin, who should’ve been sitting beside me as my guard and nodding off. And Jeok Cheongang, whose jaw had dropped when I told him about the modern world and he mistook it for the realm of immortals.

*Where the hell… Hm?*

Just then, as I wandered around the carriage to stretch my legs, a familiar voice reached my ears.

“The Central Plains have already been scrapped by the Earth Mother Goddess. Now, who does the Central Plains martial world revolve around? Our Captain. The Blazing Flame Divine Dragon of the great Jin Family of Taiyuan—that’s who.”

“Ooh. Ooooooh.”

What the hell was he talking about?

I listened to the voice ringing out louder than the surrounding hubbub.

“And who is it that believes in and follows that Blazing Flame Divine Dragon? It’s me. Want to know why? Because I’ve got my place at the Captain’s side locked down! I’m his most trusted subordinate—that’s why my place is secure.”

“A firm grip? How so?”

“Captain, don’t move! Blazing Flame Divine Dragon, mess with me and you’re dead! That’s how close I am to our Captain. We’re very close.”

“Ohhh.”

“Who is the Earth Mother Goddess’s son? The Blazing Flame Divine Dragon! And who’s the one holding on tight to that Blazing Flame Divine Dragon?!”

As the speech reached its climax, I stuck my head out through the window.

“Listening to all that has me curious. Who is it?”

Hyuk Mujin laughed heartily and turned his head.

Then his eyes met mine, and he went completely stiff.

“Me! Hyuk Mu—uh, fuck.”

“Fuck?”

“Ah.”

“Ah?”

“Come here, you bastard.”
## Chapter artifact 834

# Chapter 834

Everyone has their own way of forgetting their troubles.

Some people soothe their grief with books and music. Others shake off their anger with good food and a drink.

Getting physical is another good option. Run until you’re gasping for breath, work out hard enough, and all those half-baked thoughts get wiped clean from your mind.

In that sense, having been born a chubby baby weighing over eleven pounds and made history at the local maternity clinic, I’d always preferred the last method.

“Nothing beats a good workout. Don’t you think so too, Mujin?”

At my voice, soft as a cat’s paw, Hyuk Mujin—who’d been listening to my lecture on “overcoming your troubles”—finally opened his tightly shut mouth.

“No.”

“No?”

“Yes.”

“Why not?”

“Because you’re going to hit me.”

“Who says? I haven’t even said anything yet.”

“Your fist, Captain. It’s practically howling.”

Hyuk Mujin’s eyes trembled as he looked at me—or, more precisely, at the fist I had clenched tight. I nodded readily.

“Yeah. You’re right.”

“……You’re admitting it that easily?”

“I have to. That’s reality.”

“Could you spare me just this once?”

“People could misunderstand that question. Anyone listening might think I’m trying to kill you.”

“You may not kill me, but you hit me like you’re trying to.”

“When did I do that?”

At that, Hyuk Mujin stared at me in disbelief and shouted as if his life depended on it.

“Yesterday! The day before! Since last year! All the time! Rain or snow—”

Wham!

“Urgh!”

There’s always a reason someone gets beaten up.

And while I was getting warmed up and happily beating Hyuk Mujin for a while, forgetting my troubles in the process, familiar voices came through the slats of the tightly shut carriage window, accompanied by footsteps drawing closer.

“Why did the carriage stop—wait, why are there only guides here? Where’s Hyuk Mujin?”

“I don’t see Young Hero Taishan either!”

After the urgent voices of a young man and woman came the shout of an old man.

“What! That Taishan brat has disappeared?”

“Yes. He should definitely be with Hyuk Mujin and the other guides, protecting the Pavilion Master.”

“Oh, thank you, gods of heaven and earth. Ever since I met that bastard, the back of my head’s been throbbing, and I thought I’d kick the bucket any day now. Looks like I’ve got another twenty years in me.”

“Now that’s going too far!”

“Going too far, my ass. What’s going too far is the appetite of that underling of yours—Taishan, Scenic Mountain, whatever his name is. I’ve spent decades in Nanman and seen every kind of strange beast there is, but I never imagined there’d be a man who eats more than an elephant.”

“Now, listen here, Elder Nam!”

“Hey, hang on. This little shit’s been mouthing off at me for a while now… You think you can act like this in front of Senior Jeok? You’re still wet behind the ears—how dare you raise your voice at an elder!”

As that dizzying conversation went on, Hyuk Mujin, who’d been sprawled on the floor and twitching, called out.

“I-I’m right here! Help me!”

A short silence followed. Then everyone shouted at once.

“Dark Heaven! It’s an attack by Dark Heaven!”

“Young Hero Hyuk will be fine—save the Pavilion Master first!”

“Damn it, were the guides in on it too? Then Taishan must’ve—!”

“By this old man’s keen eye, that Taishan brat’s in on it too! If he shows up, kill him! Please, kill him!”

Clang, clang, clang!

As swords were drawn and the Nanman guides screamed in terror, I found myself thinking:

*Ah. I miss Mom.*

Murim really wasn’t easy.

* * *

The people who saw me step out of the carriage in perfect health reacted in all sorts of ways.

“We’re saved!”

“O Apostle of the Earth Mother Goddess!”

“Mother Goddess Heaven! Unbeliever Hell!”

The guides from the Nanman Beast Palace, who’d been branded Dark Heaven’s lackeys and nearly killed without a chance to explain themselves, sank to the ground.

“Huh?”

“Huh?”

Soul-Chasing Guest Song Ilseom and Black Dragon Saber Sama Pyo had been ready to cut someone down first and ask questions later. They both froze at the same time, like mirror images.

“Blazing Flame Divine Dragon Jin Taekyung… was Dark Heaven’s lackey all along?”

Namho, a Hidden Shadow Pavilion agent who’d lived in Nanman for decades since the Great Faction War, finally started showing signs of dementia.

“Benefactor!”

Last of all, Ju Hwaran—the Escort King’s granddaughter and the Young Bureau Head of the Yongbong Escort Bureau—ran over to me with a shriek.

She threw her arms around me.

Well, coming to Murim really had been the right call.

But I was a man who kept business and pleasure strictly separate, no matter the circumstances. I fought to keep the corners of my mouth from rising and spoke in a solemn voice.

“What shampoo do you use?”

“I was so worried something had really happened to you, I was terrified—what?”

“N-Nothing.”

I must have been a little out of it.

As I took a deep breath to get a hold of myself, Ju Hwaran asked in a voice full of concern, “Are you really all right?”

“I’m fine in every season—whether it’s snowing, raining, thundering, or hailing. But seriously, what shampoo do you use?”

“Oh no. You must have hit your head.”

“……I’m sorry. I didn’t hit my head. I’m just a little confused.”

The stream of consciousness is no joke.

I’d only just returned from the modern world, and maybe I was still half asleep. It took a little time and effort to prove I was in my right mind, thanks to my tongue doing whatever it wanted.

Which meant I had to go through a test administered by a certain old, eccentric Hidden Shadow Pavilion agent.

“What is this old man’s name?”

“Why do I have to do something like this?”

“Answer the question. I’ll ask again. What’s the name?”

“This is driving me nuts.”

“This old man’s not named Mi.”

“Wow, I’m going to lose my mind.”

“This old man’s not named Wa, either.”

I was about to say I was going crazy, but gave up and answered.

“Namho.”

“Then what’s your affiliation?”

“Hidden Shadow Pavilion.”

“Wrong.”

“What?”

“This old man isn’t just a Hidden Shadow Pavilion agent. He’s the Pavilion’s finest agent.”

“Wouldn’t you be its oldest agent?”

“……”

Namho glared at me without a word. Hyuk Mujin, who’d finally escaped the Truthful Carriage and was getting back on his feet, muttered,

“His memory and judgment seem fine to me.”

“Bah! What do you know, you fool!”

“Whoa. Why are you getting so mad?”

“This old man has a plan, too. What would you do if the fellow in front of you were a Dark Heaven lackey wearing Blazing Flame Divine Dragon Jin Taekyung’s face?”

“I suspect infirmities of old age, but no, he isn’t. I’ll stake my neck on it.”

“What’s your evidence?”

“I got hit before everyone came over. That punch felt exactly like the Captain’s.”

“……”

“His fist sticks to my skin like glue. My body remembers it. My soul remembers it. I only get that feeling when the Captain hits me.”

Hyuk Mujin looked at me with a sad smile.

“I’m glad you woke up, Captain. I was really worried these past three days.”

I’d been wondering if I ought to hit him a little less from now on. But at that, my brow furrowed.

“What did you just say?”

“Huh? What about?”

“Did you say three days?”

“Oh. You didn’t know? You woke up briefly three days ago, then slept the whole time after that, groaning and sweating.”

“……Of course I didn’t know. How would someone who was asleep know?”

Hyuk Mujin rubbed the bump on his head, looking sheepish.

“Sorry. Anyway, everyone was in an uproar over it. Elder Nam searched everywhere nearby with the others, saying they had to find some medicinal herbs. Great Hero Jeok left right away, saying he was heading to Sichuan.”

“Old Master—no, my Master went to Sichuan?”

“Yes. I’ve never seen him so hurried.”

“But why Sichuan… Oh.”

Before I could finish the question, a thought suddenly crossed my mind.

*The Sichuan Tang Clan.*

Although the Sichuan Tang Clan had suffered a devastating blow at the hands of the Western Heaven Demon Lord a few months ago, the strength of a great family didn’t disappear overnight.

Besides, the Sichuan Tang Clan, which mainly dealt in hidden weapons and poison, was also one of the most renowned medical families in the world.

And on top of that…

*The Divine Physician is in Sichuan.*

Strictly speaking, the Divine Physician known to the world was actually the Slaughter Saint. But unlike his master, the Disciple had stayed in Sichuan, and he was a physician every bit as worthy of the title.

Jeok Cheongang had left ahead of us to bring that new Divine Physician back.

*He didn’t have to go that far.*

I felt a pang of regret that I wouldn’t get to see him right away, and a warmth stirred in one corner of my heart. Then a stabbing pain rose from deep inside my body.

*This is…*

There was no doubt.

Separate from the System update, the effects of [Broken Body] remained.

That damage, which even leveling up hadn’t healed, was needling me around the lower dantian.

*Mm.*

I swallowed the groan, but I couldn’t stop my brow from furrowing just a little. The people who’d already been focused on me noticed.

“C-Captain. Is something wrong?”

“No. I’ve just got something on my mind.”

That wasn’t a lie.

I was thinking about my injuries—and about Jeok Cheongang, who’d noticed them three days ago.

*Master must have gone to find the Divine Physician because he realized there was nothing he could do to treat me.*

I could say this without a doubt: Fire King Jeok Cheongang was a great martial artist and a good Master.

But my injury, which the System couldn’t heal, must have seemed like a problem even Jeok Cheongang couldn’t solve.

*Fuck. At first I thought I’d gotten a loan from a regular bank, but now I find out it was a Sunshine Loan.*

I felt like a gambler who’d borrowed from loan sharks to keep playing, only to ruin his life.

But there was no point dwelling on it now.

Even if I could go back to that moment, I knew I’d make the same choice. All I could do was give a bitter smile.

It couldn’t be helped.

The stakes in those few gambles hadn’t been gold bars or checks. They’d been my life—and someone else’s.

If I hadn’t used One Annihilation at each of those moments of crisis, I wouldn’t still be alive.

*I’ve finally got some breathing room. I guess it’s time to pay my debt.*

I couldn’t sit down face-to-face and talk with the System, and I had no intention of whining at it. I’d already received more than enough of a gift, and it had warned me plenty of times.

Every path I’d walked until now had been my own choice.

*That’s enough. It is what it is.*

With those words, I cleared the jumble of thoughts from my mind.

Thinking about it on my own wouldn’t make anything better right now. I had to think about how the people around me felt, too.

I’m really a considerate person, aren’t I? No, wait a second.

“Then where’d that Taishan bastard go?”

“Huh?”

“Huh?”

Everyone blinked at my sudden question. One of the guides from the Nanman Beast Palace shuffled over and spoke.

“Um… the big fellow went to get something.”

Namho asked in bewilderment, “Went to get something?”

“Yes.”

“What on earth?”

“Well, um…”

The guide was about to say something when—

*Rustle, rustle, rustle!*

The bushes some fifty jang away shook, and a huge figure burst out. He was so massive you had to wonder if he was human.

“Taishan! Brought it!”

He raised the dark, murky thing in his hand.

“Taishan’s favorite thing in the world—no, a miracle cure for the sick Pavilion Master!”

The people watching stared blankly and murmured.

“That’s honey.”

“Right. A pot of honey.”

“Sorry to interrupt, but isn’t that a beehive, not a pot of honey?”

“That’s true, too.”

*Bzzzzzzzz!*

It was the first time I’d ever seen it.

Bees that big—and thousands of them all swarming together.

“……Primordial Heavenly Venerable. Gods of heaven and earth.”

Leaving Namho’s sorrowful voice behind, the rest of us quietly climbed back into the carriage.

Murim really wasn’t easy.

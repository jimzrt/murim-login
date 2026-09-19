# Checkpoint Review — 425–429

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

# Chapters 425–429

## Plot

Jin Taekyung is tortured by the Arch Lich until Hero’s Soul pierces its chest, reconstructs the destroyed Skeleton Warlord as a Lv.160 Skeleton King, and fully heals Jin. Reunited with White Flame, Jin uses One Annihilation to destroy the Arch Lich, its unfinished Gate, and the surrounding city. The Arch Lich’s escaping soul fragment is erased by the remnant of Lei Fei’s soul within Hero’s Soul. Jin collapses, while the Skeleton King retrieves him and Hero’s Soul.

The Arch Lich’s destruction ends the thirty-four-day Winter War, though worldwide speculation accuses Jin of involvement in Wu Heixing’s and Lee Jungryong’s deaths. After four days of staged unconsciousness and a week of recovery and examinations, Jin publicly accepts responsibility for his hostility toward Wu but claims the Arch Lich killed him and that Wu’s potion saved Jin. He mourns Lee and the other dead at a press conference watched by roughly three billion people, ending the criticism against him.

Jin then meets Magic Johnson, who has given the Skeleton King a nearly perfect human body through magic circles carved into its bones. The Skeleton King adopts the name Stone-King and begins learning to live as a human, immediately clashing with Jin. Their fight scatters Johnson’s papers, and Jin recognizes a pattern from Sichuan among them.

## Continuity

- Hero’s Soul reconstructed the Skeleton Warlord as a stronger Lv.160 Skeleton King and restored Jin’s health and attributes. The Skeleton King remains Jin’s friend and ally.
- The Arch Lich, its soul fragment, the unfinished Gate, and the surrounding ruined city were destroyed. The fragment was erased by the remnant of Lei Fei’s soul within Hero’s Soul.
- The Winter War ended after thirty-four days. Jin is internationally celebrated as the hero who prevented a wider catastrophe.
- Lee Jungryong is publicly presumed dead without a surviving body. Wu Heixing’s broken corpse was recovered, and Jin’s public explanation attributes his death to the Arch Lich.
- Chairman Shao Yang is preparing prosecutions against the corrupt Crown Prince Party leadership, including Wu Heixing’s father, after its persecution and forced-labor campaign.
- Jin’s mother and Hayeon remain in China under Chairman Shao’s protection.
- Opening his Middle Dantian lets Jin perceive the texture of qi and sever layered magic with Force; he can also manipulate Magic Gem-powered equipment.
- Magic Johnson created the Skeleton King’s near-human body with magic circles carved into its bones. The Skeleton King can appear human outside his Inventory and is establishing the identity Stone-King.
- Jin recognized the Sichuan pattern on Magic Johnson’s papers. What the pattern represents and why Johnson possesses it remain unresolved.
- The Quest **One Who Returned from Death** remains active, keeping Login unavailable until the Quest ends.

## Translation Decisions

- Render **영웅의 혼** as **Hero’s Soul**, **스켈레톤 킹** as **Skeleton King**, and **스톤-킹** as **Stone-King**.
- Render **라이프 포스 베슬** as **Life Force Vessel**, **중단전** as **Middle Dantian**, and **소멸** as **Erasure**.
- Render **샤오 쉔** as **Xiao Shen**, **매직 존슨** as **Magic Johnson**, and preserve **hyung** in Xiao Shen’s address to Jin.
- Preserve Jin’s dry, profane voice; the Skeleton King’s grandiose, Internet-influenced insults; and the Arch Lich’s archaic, contemptuous register.

## Durable state

{
  "active_continuity": [
    "Jin Taekyung can perceive the texture of qi and sever layered magic with Force after opening his Middle Dantian.",
    "Magic Johnson has created a near-perfect human appearance for the Skeleton King using magic circles carved into the Skeleton King's bones.",
    "The Skeleton King can now appear human outside his Inventory and is attempting to establish a human-world identity as Stone-King.",
    "Jin recognized a pattern on Magic Johnson's scattered papers as the same pattern he previously saw in Sichuan.",
    "Chairman Shao is preparing a political reckoning against the Crown Prince Party after its persecution and forced labor campaign.",
    "Jin's mother and Hayeon remain in China under Chairman Shao's protection.",
    "Lee Jungryong is publicly presumed dead without a surviving body, while Wu Heixing's corpse was recovered after the battle."
  ],
  "continuity_sources": [
    429,
    428
  ],
  "open_questions": [
    "What do the papers bearing the Sichuan pattern represent, and why did Magic Johnson possess them?",
    "What final punishment will be imposed on Wu Heixing's father and the Crown Prince Party leadership?",
    "How will the Skeleton King's human identity and Stone-King name be formalized in the human world?"
  ],
  "safe_through": 429,
  "temporary_decisions": [
    "Render 샤오 쉔 as “Xiao Shen” and preserve “hyung” for his address to Jin.",
    "Render 매직 존슨 as “Magic Johnson,” 스켈레톤 킹 as “Skeleton King,” and 스톤-킹 as “Stone-King.”",
    "Preserve Jin's dry, profane voice and the Skeleton King's grandiose, Internet-influenced insults."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 425

# Chapter 425

*Thud!*

White Flame, having lost its target, rolled across the ground.

“Ah.”

The Arch Lich snapped its fingers at me, frozen stiff as a statue. A pair of black hands materialized in midair and squeezed my entire body.

A spell that no longer even needed an incantation to manifest.

*Step. Step.*

With every step the Arch Lich took, something seeped into various parts of its body, which was as hazy as mist.

The left arm that had vanished in One Annihilation slowly regenerated, while its shattered and cracked bones were restored even more solidly than before, taking on an even darker hue.

The closer the Gate came to completion, the stronger it became as well.

—So there was a reason I thought I smelled death on you. Human and monster, friends… How touching.

*Crack.*

I heard bones shifting out of place throughout my body, but I stared blankly over the Arch Lich’s shoulder.

More precisely, at the sword buried in the ground—and the hand of someone who had not let go of its hilt until the very end.

*The Skeleton Warlord.*

Monsters and humans were sworn enemies, as ordained by God.

The same had been true of me and it. It certainly had been at first.

But… I finally understood now. At some point, the Skeleton Warlord had stopped being a monster to me.

*If I had thought of it as a monster, I would have erased it with my own hands.*

If I had killed the Skeleton Warlord myself, I could have gained one last hope through a level-up.

But I had hesitated, and in the end, I had given up.

Not because it had saved my life. Because I had already accepted it as a friend in my heart.

A hollow laugh escaped me.

*Damn it. I never should have grown attached.*

At the sight of me, the Arch Lich’s eye-lights narrowed.

—Are you laughing? In a situation like this?

“My mother used to say that fortune comes to those who smile.”

—You have lost your mind.

“Why the fuck do you care if I laugh? What are you, my immediate senior in the army?”

I spat toward the Arch Lich’s face. A thick liquid, impossible to distinguish as blood or phlegm, trickled down between its brows.

At the same time, the red eye-lights in the places where its eyes should have been flared violently.

—I heard your answer clearly.

“Go eat a dick.”

It would be a lie to say I had no regrets about the life I had lived, but there was no point in any of it now. Regret always came too late, and I had struggled until the very end. I had done enough.

Once I let go of everything, it all felt like one long dream. My face, smiling peacefully at the Arch Lich’s eye-lights, was reflected in them.

—I told you, did I not? Your flesh would be torn to pieces, and your soul would wander the River of Death forever.

I readily nodded in agreement.

“I suppose so. Just like that Demon King bastard you serve.”

—……!

“If we meet, I’ll pass on your regards. Give me the address.”

—……Let us see how long you can continue spouting such nonsense.

At the Arch Lich’s gesture, the enormous hands of mana squeezing me seized all four of my limbs. Then they began pulling my body apart with tremendous force.

Slowly, little by little.

*Crack. Craaack.*

Small ruptures sounded inside me, and the sensation of pain I had momentarily forgotten awakened.

I thought I no longer had enough strength even to scream, but a cry escaped between my lips before I realized it.

“Gnh, graaaaagh!”

—That sounds much better.

My vision was bleached white by the pain. I finally let out the screams I had been holding back and waited for death to approach.

But when even the pain began to fade, what came to me was not death, but a System notification.

*Beep.*

> **System**
>
> - **High-grade Potion** has been used!
>
> - The amount of potion used is too small. Your injuries have been healed slightly!
>
> - Your injuries are extremely severe. You require a greater amount of higher-quality healing than this!

…What?

As I felt a refreshing sensation and the pain awaken once more, I opened my eyes wide.

The Arch Lich was staring at me with mocking eye-lights.

And in its hand was a glass bottle.

*That’s…*

It was one of the potions that had been in Lee Jungryong’s subspace pocket—the one the Arch Lich had stolen long ago.

And now, it was using a potion made for healing as a tool to inflict pain.

Healing enough to stop me right at the threshold of death.

Healing enough to make me feel the greatest possible pain.

—Foolish human. Did you truly think this body would grant you such an easy and comfortable death?

“……!”

—Continue to howl. Weep tears like a coward and writhe in agony. Only after you realize your foolishness will you be permitted to travel to the River of Death.

The Arch Lich shook the glass bottle filled with potion, its voice thick with mockery.

The potion was not even one-tenth empty yet. That was equal to the amount of pain I still had to endure.

And that time would pass infinitely slowly, stretching on like countless eons.

Weak healing spread through my body, but so did pain that came crashing down over every inch of me. My breathing grew ragged. I forced a smile and asked the Arch Lich,

“If I give three cheers for the Demon King, will you end this sooner?”

—Perhaps, if you devote yourself to it with all your heart.

“I’m not doing that, you son of a bitch.”

—Very well. Time is plentiful, after all. There is no harm in taking your time to think about—

*Thwack!*

The Arch Lich’s eye-lights trembled.

I was just as shaken.

Neither of us—not a single person—had expected what happened next.

—……What is this?

With a doubtful voice, the Arch Lich looked down at its chest.

Light.

It was light. A dazzling radiance, bright enough to illuminate the entire world, had burst through its chest.

*No. It’s not light.*

I stared at it with vacant eyes.

It was a sword, emitting a radiance more brilliant than ever before.

I knew the name of that sword, which was so familiar to me.

*Hero’s Soul.*

And I knew the owner of the hand gripping its hilt tightly, visible beyond the Arch Lich’s skeletal chest.

“……!”

It was as if the entire world had stopped moving.

Within that world, slowed to an immeasurable crawl, I watched hundreds—thousands—of fragments of bone gather.

They were nothing more than the last traces someone had left behind, but they pulled toward one another and formed their own shapes.

*Pop. Pop!*

The fusion of bones.

Two arms and two legs formed first, followed by a chest and abdomen.

The bones that had gleamed black were washed clean by the radiance scattered from **Hero’s Soul**. Before long, they had taken on a soft golden hue and become longer and sturdier.

*Ah.*

It was a wondrous sight.

The countless fragments of bone gathering to form a body seemed to reverse the flow of time, while the light flowing from the sword drove the darkness engraved in each joint away, as if heralding the birth of a new being.

And finally, when a skull settled onto the completed body—

*Fwoosh!*

Golden eye-lights burst from its empty sockets.

The feeling was both utterly familiar and completely strange.

The next moment, a voice rang out, and the time that had stopped began to flow again.

—You asked me why, did you not?

“……!”

My body trembled as if lightning had pierced through me. A memory from less than an hour ago flashed through my mind.

*Then why? Why, exactly?*

Yes. That was what I had asked back then.

Why had it saved me? Why had it chosen to become my shield even though it had been prepared to face Erasure?

In answer to my question, it had said it did not know. It had said it did not know why it had done such a thing. Perhaps it had been bewitched by the sword.

And now, the answer I had not heard then pierced my ears.

—You are a crafty human, but a pretty decent one. That was all.

*A pretty decent guy.*

Words I had once said to someone.

I stared at it in disbelief.

Its entire body was larger and sturdier than before, with a faint golden glow. An unknown silver pattern was engraved across the forehead of its skull, resembling a crown.

No. It was unmistakably a crown.

> **System**
>
> - **Lv. 160 Skeleton King**

The moment I saw the System window hovering above its head, a hollow laugh escaped me.

“Look how much you’ve grown, Bones.”

—No wonder I had felt itchy all over my body for so long.

The small black caterpillar had finally shed its skin and spread its wings.

The Skeleton Warlord—or rather, the Skeleton King’s eye-lights curved like crescent moons.

It was smiling.

So was I.

And there was one being who was unable to smile.

—Graaaagh! Graaaaaaaaaagh!

The Arch Lich.

The unprecedented named monster, which commanded hundreds of thousands of undead and possessed inexhaustible, tremendous mana, writhed in agony.

A single sword had pierced straight through the center of its chest.

The golden radiance flowing from **Hero’s Soul** devoured its mana and melted its body.

Perhaps even its soul.

—Human.

At the Skeleton King’s quiet call, I realized what I had to do.

*Now… let’s finish this.*

*Beep.*

> **System**
>
> - **Hero’s Soul** grants you the light of healing!
>
> - All status effects have been removed!
>
> - All injuries have been healed, and all attributes restored!
>
> - Someone who is not here smiles at you.

*Fwoooooosh!*

A pillar of light burst from **Hero’s Soul** and enveloped my body.

Along with a gentle warmth, my shattered bones joined together and my flesh healed. My injured organs and damaged meridians recovered, while a heat hot enough to burst boiled through me like lava.

*I can do this.*

It was a certainty so firm that even I was surprised by it.

And in reality, it was true.

If I had strength, there was nothing I could not do.

*Come.*

*Fwoooooosh! Clack!*

At the same time that I pulled White Flame, rolling across the ground, into my hand—

*Fwoosh!*

I thrust out my foot, feeling myself rise into the air.

At the end of that step stood the Arch Lich, streaming powerful mana as it writhed in agony.

—What in the world! What magic did you use?!

The Arch Lich spotted me and shouted as if in a fit.

Its red eye-lights shook without pause and swelled larger.

That alone told me how much pain it was suffering.

—Damn you, damn you, human! Graaaaagh!

Instead of answering, I slowly raised White Flame.

I aimed its transparent spearhead at the Arch Lich, trembling violently from the pain, and the enormous Gate standing behind it.

*Whoosh.*

The fire dragon spread its wings and soared from my dantian, transforming into a ball of flame as it surged through every limb and bone in my body. It flowed along my fingertips, kindling blue flames atop White Flame’s spearhead and layering them over and over.

—You cur! How dare you—

The Arch Lich flailed its arms and legs in a frenzy, but the magic it fired collided with the heat surrounding me like a barrier and vanished before it could even reach me.

Unlike the weakened Arch Lich, however, the darkness surrounding the Gate roiled even more violently.

And at last, I realized.

*Now!*

White Flame trembled as rotational force traveled up through my leg, waist, shoulder, and wrist.

The unprecedented surge of qi drawn from my entire body kindled flames larger than ever before.

Yes.

This was the moment.

*Fwoosh.*

One step.

All the space separating the Arch Lich and me disappeared, and time slowed.

Before the Arch Lich’s slowly moving lips could finish the incantation, I launched a single strike filled with every ounce of my will and strength.

—Blink…!

*One Annihilation.*

There would be no second mistake.

The blue fire dragon that sprang from White Flame’s spearhead swallowed both the Arch Lich and the Gate.

*Kwooooooooooong!*
## Chapter artifact 426

# Chapter 426

*Fwoooooosh!*

The instant the Arch Lich faced the enormous fire dragon that burst from the spearhead, it realized the truth.

*Too late.*

An unavoidable attack.

The Spell it had not yet managed to unleash and the mana that had been on the verge of completion scattered beneath the flames rushing straight toward it.

The fire dragon, blazing with hellfire, opened its jaws at the Arch Lich, which had frozen in place, oblivious even to the pain.

*Kwooooooong!*

Along with a thunderous roar like that of a dragon, blue flames swept in every direction. A terrible heat distorted space and vaporized everything.

The Arch Lich felt the mana and barriers surrounding it melt away. It even felt a sensation it had truly forgotten for a very long time.

*It’s hot.*

*Fwoosh!*

Blue hellfire filled the Arch Lich’s vision. The fire dragon swept over its entire body and continued onward without stopping.

The fire dragon was headed toward the enormous black door standing tall in the center of the ruined city.

The Gate.

*No!*

The Arch Lich opened its red eye-lights wide and reached out, but no voice came from it, and the fire dragon swallowed the Gate—as large as itself—whole.

At the moment that the unprecedented mana gathered from the life force of hundreds of thousands of humans collided with the flames, a blinding flash erupted.

*Fwoosh!*

It was a pillar of light that could probably be seen from hundreds, even thousands, of kilometers away.

Darkness and blue flames collided with one another, then soon blended together. The forest of buildings that had been struggling to remain standing bent at the waist, and a ring of wind burst outward.

*Krrrrooooom—*

A thunderous roar and vibration beyond anything words could express shook the world.

The gray sky split apart, and the gray fog that had densely shrouded the entire city scattered like heat haze.

And then, as if all of it had been a dream from some distant day, a quiet stillness descended.

*Ah.*

The Arch Lich gazed at the world with hollow eyes.

The scenery looked no different from before, but it knew. Everything, including itself, had changed. Everything had collapsed like a sandcastle.

The Arch Lich slowly turned its head. Its trembling red eye-lights reached the person standing tall like an iron tower.

—“I should have killed you.”

The single sentence broke the silence.

Jin Taekyung opened his mouth, his complexion utterly bloodless. The accumulated damage and mental exhaustion from his endless battles made him look as though he might collapse at any moment, but his voice alone had not lost its strength.

“Yeah. You should’ve killed me sooner.”

The Arch Lich closed its mouth. It was certainly its own fault for missing the chance to cut off Jin Taekyung’s breath.

A momentary lapse in vigilance had turned everything to nothing.

*My king. Please forgive this disloyal servant.*

The Arch Lich begged forgiveness from its king, wherever he might be.

If it had killed Jin Taekyung without delay, if the monster that had taken the human’s side had not been reborn as a new being and driven that damned sword into its chest… everything would have proceeded according to plan.

It would have survived and completed the Gate. Leading an innumerable monster army beyond imagination, it would have hunted down and killed those verminous humans and burned the city to the ground.

While waiting for the great king to return someday.

But the plan it had believed to be perfect had been thoroughly ruined.

By the arrival of a single human.

Jin Taekyung.

The Arch Lich’s red eye-lights, which had been gradually fading, flared with their last remaining strength.

A vow to itself and an oath of vengeance spilled toward Jin Taekyung.

—“Remember me. Remember this body, which will one day trample your souls beneath its bare feet.”

Jin Taekyung spat out a wad of phlegm.

“Big talk from a bastard who’s about to croak. Try saying, ‘Asmodeus is a fucking son of a bitch.’”

The Skeleton King hesitantly opened its mouth.

—“Asmodeus is a fucking asshole…”

“Not you.”

—“Ah, I know. I just wanted to try it once. But I cannot say that I feel good after uttering something so blasphemous.”

“What’s the problem? You’re a king now, too.”

—“Oh. That’s true.”

*I swear on the River of Death, I will tear those two apart.*

The Arch Lich stretched both hands toward Jin Taekyung and the Skeleton King.

Its skeletal hands clenched as if they would crush the two figures standing far away, but nothing happened.

Instead, a wind that had blown in from somewhere brushed against its entire body.

*Whoooooosh.*

It was collapse.

Beginning with the Arch Lich’s hands turning to ash and scattering, everything that made up its body began to crumble.

Its arms, legs, and chest, and finally even the skull containing its red eye-lights.

—“Please survive. Until the day we meet again…”

Its final voice, filled with resentment, vanished into the wind.

The wind grew stronger, carrying the ash that had once been called the Arch Lich as it continued onward.

Whenever the wind passed, everything caught within the range of One Annihilation sank and crumbled. Collapsed high-rise buildings, heaps of concrete, overturned cars, and corpses from which life had already departed…

And even the enormous, unfinished Gate that would have become the starting point of an even greater war.

*Fssshhh.*

As Jin Taekyung stared silently at the scene, a clear chime rang in his ears—the sound that only he could hear in this place.

*Ding. Ding. Ding.*

Countless System messages obscured his vision. They were a celebratory salute announcing that everything had finally ended.

But Jin Taekyung’s body, which had exhausted every last bit of its strength, was already tilting toward the ground.

*I did it.*

With that as his only remaining thought, a deep, peaceful sleep came to him.

And as the Skeleton King carefully caught Jin Taekyung’s falling body, it saw the faint smile spreading across his lips.

—“…You worked hard.”

*He is a cunning human, but he really is a pretty decent one.*

The Skeleton King murmured inwardly. Then, as it began to move Jin Taekyung to a safe and comfortable place, it remembered something it had forgotten.

—“Ah, that’s right. The sword.”

*Was it called Hero’s Soul?* It did not know who had given it that name, but it was certain that a mysterious power dwelled within it.

It was thanks to that sword that it had awakened on the verge of Erasure when it had been the Skeleton Warlord, and that it had been able to inflict serious damage on that terrifying Arch Lich.

—“I almost forgot. I need to make sure to keep it safe.”

It did not take the Skeleton King long to find it. The sword that had remained buried in the target’s chest until the very end was lying quietly in the place where the Arch Lich had stood only moments ago.

But after picking up **Hero’s Soul**, the Skeleton King tilted its head.

—“Huh? Something feels strange.”

It was a peculiar feeling, difficult to explain.

It could not put its finger on it, but how should it say this? The sword was certainly a fine blade, yet it did not have the same sense of mystery as before.

—“Did I pick up the wrong sword?”

But no matter how thoroughly the Skeleton King searched its surroundings or examined the sword, nothing changed.

After scratching its golden skull and pondering for a while, the Skeleton King finally reached a conclusion.

—“Hmm. I guess this is it.”

It decided that it was nothing more than a momentary feeling. The sword looked the same as the one it remembered, and it had even seen it fall from the Arch Lich’s chest with its own eyes.

*But why does this feel so unsettling?*

It was something it could not understand at all. The Skeleton King shook its head, then slid the sword between its pelvic bones to store it.

As it immediately headed toward Jin Taekyung, who lay collapsed on the ground, it did not know that the moment Jin Taekyung lost consciousness after exhausting all his strength, mist-like black energy had mingled with the wind scattering in the distance.

Nor did it know that the golden light clinging to **Hero’s Soul** had vanished as it pursued the black energy.

But one being was different.

The black energy that had flowed somewhere within the wind.

The Arch Lich, which had lost most of its power because of Jin Taekyung and had been reduced to a tiny, powerless fragment of a soul, opened its eyes wide as it saw the dazzling golden light blocking its path.

*This is impossible.*

The words the Arch Lich had spoken to Jin Taekyung and the Skeleton King before losing its form had been entirely true.

It would return in the near future. It intended to stain this land with blood using even greater power than before and an even larger monster army.

Life Force Vessel.

The highest-level black magic usable only by the undead, and a vessel capable of storing a fragment of the soul.

If it had that, it could avoid eternal Erasure.

No—it had believed it could, until that brilliant golden light blocked its path.

—“You… What are you?”

The Arch Lich was now nothing more than a pitiful fragment of a soul, incomparable to the power transmitted by the light.

The black energy writhed violently with rage, confusion, and fear.

But even though the Arch Lich’s thoughts reached it, the golden light showed no reaction. It merely shone more brightly and swelled larger.

And in the next moment, the Arch Lich realized the identity of the light.

*That is not magic. It is a soul.*

Someone’s soul—the one it had once shattered and trampled beneath its feet. A fragment of a soul that had already lost its form, yet remained within the sword through nothing but its will.

Suddenly, the Arch Lich recalled one of the memories it had pushed deep into the back of its mind.



*“You are a noble one, human. What is your name?”*



That day, when blood had formed rivers and corpses had formed mountains. A single human who had remained standing until the very end in a city filled with nothing but destruction and death.

—“Lei Fei.”

The movement of the Arch Lich—or rather, the black energy—stopped abruptly.

The dazzling golden light that burst through the air swept over it like a wave.

*Fwoooooosh!*

*…Damn it.*

And that was the Arch Lich’s final thought.



* * *



The situation on the battlefield where the main forces had gathered was fierce.

While the S-rank Hunters moved toward the rear with some of the troops to open a path for the suicide squad, the monster army numbering in the tens of thousands did not miss the opportunity and charged forward.

「Fire Rain!」

*Kwaaang!*

When the mage units positioned in the rear unleashed an area-wide spell, a rain of fire poured down.

The mages clenched their fists at the sight of hundreds of monsters burning to death as charred lumps of coal.

That was when—

*Whoooooosh! Thwack!*

「…Huh?」

One of the mages wiped the blood from their face with a bewildered expression.

The face of a comrade who had been smiling back at them only moments ago had disappeared.

No, it had burst apart.

Pierced by a black spear that had cut through the distance like a beam of light.

*Whooooooosh! Boom!*

Only after another spear flew in and skewered six or seven mages like meat on a spit did belated screams ring out.

「Aaaaargh!」

「Death Knights! It’s Death Knights!」

「Fuck, what the hell are you talking about? Didn’t we take care of all of them?」

「I-I don’t think so! It looks like they hid their elites separately among the others!」

Someone’s words soon became reality.

The elite monsters, having clearly noticed the absence of the S-rank Hunters, revealed themselves on the battlefield, and an unstoppable slaughter began.

*Slash!*

*Kwaaang!*

Death Knights, Liches, and dozens of Wyverns that had remained unseen appeared and launched a fierce assault.

People died without end, and monsters continued to surge forward.

With even the S-rank Hunters away from their positions, deep despair spread across the faces of those staking their lives to hold the line.

*It’s all over.*

And at the exact moment everyone thought of death—

*Shiiiiing!*

The Death Knight’s sword, which had been cutting through someone’s body, suddenly stopped.

No.

It crumbled into ash.

“W-What the hell…?”

The Hunter who had barely survived checked his surroundings and gaped.

It was an unbelievable sight.

First, hundreds fell.

Then thousands crumbled.

Before long, monsters numbering in the tens of thousands were turning to ash and scattering.

*Whoooooosh.*

At long last, it was the end of the war.
## Chapter artifact 427

# Chapter 427

It was a winter night in December, and snow was pouring down in thick flurries.

People who had hurried through the streets trusting the weather forecast—which had confidently predicted clearer weather than usual—were bewildered, and the Meteorological Agency was thrown into confusion.

“What the hell? What’s going on?”

“We’re analyzing it now. This definitely shouldn’t be happening.”

“With snow the size of hailstones pouring down, don’t tell me this shouldn’t be happening. Stop spouting nonsense and bring me the data. There should be real-time observations!”

“We’re looking into it right now, but… Ah, it looks like an abnormal phenomenon caused by a sudden surge in mana in China’s Sichuan region. The expected snowfall is no joke.”

“Sichuan? Damn it. Is that Arch Lich bastard controlling the weather now, too?”

After the Great Cataclysm, the Meteorological Agency had introduced various types of magic and begun issuing weather forecasts that bordered on prophecy.

One hour after hastily beginning a second round of observations, the agency issued a heavy-snow advisory across the country. Their conclusion was that record-breaking snowfall, the heaviest in roughly thirty years, was on its way.

But before long, the people hurrying home had no choice but to stop in their tracks.

It was because of a single sentence that rang out from a massive screen installed in the center of one of the countless busy commercial districts.

—On a day like today, it is both my pleasure and my honor to bring you this news.

An elderly East Asian man appeared on the screen.

Behind him sat the leaders of the nations belonging to the United Nations Security Council. The Chairman of the People’s Republic of China began speaking into the countless microphones, his eyes red and his voice thick with emotion.

—The Arch Lich has been erased. We… have won.

Victory.

That single word was enough.

For roughly a month—thirty-four days, to be exact—an unprecedented monster wave had continued without pause.

The news that the great war, which had spread unease throughout the world beyond Sichuan Province, had finally come to an end left people standing there with their mouths hanging open.

Then they erupted into thunderous cheers.

“Waaaaaaah!”

“Wait! Hold on! I couldn’t hear that. What did he just say?”

“...It’s over!”

“What?”

“Look at the subtitles! Look at the subtitles!”

“‘The Arch Lich has been erased’… Oh, shit, it’s true! Waaaaaaah! I thought I was going to get called up for reserve duty!”

They heard neither Chairman Xiao Yang’s thirty-minute announcement nor the additional explanation given afterward by the spokesperson for the United Nations Security Council.

With the Arch Lich erased, countless undead legions had lost their power and been annihilated as well. At last, the peace everyone had prayed for had arrived.

“Mom, it’s me. Yeah. Did you see the news? You didn’t? Turn it on right now. Yeah, yeah!”

“We have to celebrate. Assistant Manager Kim, let’s go for a third round!”

“A third round? The server update is tomorrow. Manager Noh is going to lose his shit.”

“Manager Noh is coming, too. He has the corporate card.”

“Ugh, I don’t want to see that bastard’s face. Fine. Let’s go.”

“Unity! Yes, Battalion Commander. This is Captain Lee Junbeom. Could I extend my leave by just one more day—? No, sir. I’m sorry, sir.”

People who had been going back and forth outside while desperately ignoring their unease ran to the bars amid the cheers. Even those who had stayed home, anticipating a second Great Cataclysm, poured into the streets and joined the festive atmosphere.

The cheers did not die down even after midnight.

Nor the next day, or the day after that…

The entire world boiled like a cauldron over a charcoal brazier at this monumental victory, pouring out new articles day after day in every language.

There were even jokes that more news and articles had been published about the victory than about the heavy snow that had fallen over Korea for three straight days.

And… there was one name that appeared without fail in every one of those articles.

[The New York Times, United States: “A Great Victory, a New Hero.”]

[The Times, United Kingdom: “A New Star Rising in the East. Is He Close to Prince Felix?”]

[Asahi Shimbun, Japan: “Jin Taekyung Is Asia’s Pride. But Japan’s First-String Hunters Could Surpass Him!”]

[People’s Daily, China: “The Young Korean Knight-Errant Who Saved Countless People. And the Tragic Death of Zhonghua’s Genius, Wu Heixing.”]

[China Youth News: “Jin Taekyung Is a Descendant of Chen Lin, a Ming Dynasty General. The Blood of Zhonghua Unmistakably Flows Through Him, and He Will Surely Become a Chinese Citizen Before Long.”]

[Goryeo Daily, Korea: “Ares Guild Vice Guild Master, Hunter Lee Jungryong, Age 68. Presumed Dead…”]

[Das Patch Korea official: “We have devoted every effort to investigating Jin Taekyung for several months, but we could not uncover a single thing. His romantic history is astonishingly clean.” When a reporter asked whether that meant he had dated many women but parted with each of them amicably, the official cut him off: “No. I mean he’s never dated anyone in his life.”]

To the various media outlets, Jin Taekyung’s existence was nothing short of a Christmas present.

Every spotlight turned toward him, and all kinds of stories about him came pouring out.

The material was endless. Needless to say, there was plenty to cover about the monster wave now known as the “Winter War,” but his past actions on the way to his current position and even the most trivial details of his private life were considered newsworthy.

Even the trashy articles that would normally have been cursed out as gutter journalism attracted interest.

That was how much the attention of the entire world had turned toward the new hero who had led them to this great victory.

But not all that attention was positive.

Information had begun leaking out bit by bit from behind the ironclad internal security, and people began raising questions.

[Four Days After the War. What Was Hidden Behind the Great Victory That Day? The Questions Surrounding Jin Taekyung.]

[Lee Jungryong Presumed Dead. Wu Heixing’s Suspicious Death. The Deaths of Two S-Rank Hunters and the Rise of a New Hero.]

[Secret Testimony from Coalition Commanders Who Were at the Scene: “Despite the battle’s ferocity, no significant injuries were visible on Jin Taekyung’s body when he was discovered. We are investigating whether he used potions. If he regains consciousness, the entire situation will become clear.”]

Although they were few in number, conspiracy theories began to appear, and the internet erupted into fierce arguments.

Articles like these, unable to withstand waves of malicious comments and reports, vanished almost immediately. But they planted doubts in the minds of some members of the public, and eventually everyone’s attention focused on one thing.

Jin Taekyung.

When, exactly, would he show himself?

* * *

Beep. Beep.

State-of-the-art medical equipment emitted mechanical sounds.

The people gathered in one part of the hospital room, which only a select few were permitted to enter, gazed worriedly at Jin Taekyung as he lay there wearing an oxygen mask.

“How is Mr. Jin’s condition?”

Choi Minwoo answered Chairman Shao Yang’s question.

“It’s always the same. Everything is perfectly normal, but for some reason, he still hasn’t regained consciousness.”

“Did both of them say that?”

“Yes. They said they don’t know the cause.”

“Hmm. If both of them said so, there can be no doubt… Then why on earth hasn’t he regained consciousness?”

Chairman Shao Yang sighed.

The two people he had mentioned were both at the very top of their fields.

One was a civilian physician known as the reincarnation of Hua Tuo, while the other was a top-class healer renowned throughout the world.

If the two people invited as Jin Taekyung’s temporary attending physicians had said so, there could be no doubt about it.

“I heard his family is here.”

“The Peace Guild is taking good care of them. Fortunately, they’ve regained their composure.”

“I see. Would it be possible for me to see them, even briefly?”

“I can ask, but their wishes are the most important thing, so…”

“I understand. Who could feel differently when a blood relative has yet to regain consciousness? I would appreciate it if you simply considered this the foolishness of an old man.”

“No, Chairman. We’re grateful that you even thought of it.”

“Don’t say that you’re grateful. If not for Mr. Jin, an even greater catastrophe would have occurred. Though I am an old man with little time left to live, I will carry this gratitude with me to the grave.”

Chairman Shao Yang was sincere.

Four days had passed since that day. During that time, an investigation team made up of countless experts from around the world had combed through the city that had served as the Arch Lich’s base and discovered traces of the Gate.

And the projected scale of the Gate, inferred from the enormous residue of mana, was nothing short of catastrophic.

“If Mr. Jin had failed to stop the Arch Lich that day, not only our country but all of Asia would have become a battlefield. No… Perhaps the entire world could have become one.”

“It was certainly possible.”

There might have been some exaggeration, but most of it was true.

That was why Choi Minwoo did not bother to deny it. He simply nodded in acknowledgment.

There was no need to feel embarrassed, since the praise was not directed at him in the first place. Nor did he feel the need to diminish the gratitude of the leader of a nation with a population of more than a billion.

A debt of gratitude in someone’s heart had a way of returning as an even greater gift.

“But Chairman. I’ve been hearing some unfavorable rumors about Jin Taekyung lately… Were you aware of them?”

“Do you mean something inside the country or outside it?”

“Inside. The leadership of the Communist Party—or, more precisely, the Crown Prince Party.”

Chairman Shao Yang nodded.

“I am fully aware of the matter.”

It concerned Wu Heixing’s death.

The investigation team had found his body in a severely mutilated state, and conspiracy theories about it were slowly spreading both inside and outside the country.

“There are people who suspect Mr. Jin. They point to the fact that he had a minor argument with Wu Heixing during their first meeting, as well as the fact that Mr. Jin had no notable injuries when he was first discovered.”

There were two negative theories about what had happened.

The first was that Jin Taekyung, who had harbored ill feelings toward Wu Heixing for some time, had killed him and disguised it as the work of the Arch Lich.

The second was that, together with Lee Jungryong, who was presumed missing or dead, he had used Wu Heixing as a shield and taken advantage of the opportunity to kill the Arch Lich.

Chairman Shao Yang knew about these theories as well, and he had already reached his own conclusion.

The old statesman spoke to Choi Minwoo in a firm tone.

“They are nothing more than absurd slander and conspiracy theories.”

“Thank you for believing him, but…”

It was a good response, but it was not enough.

Choi Minwoo continued slowly.

“The leader of the Crown Prince Party doesn’t seem to share your view, Chairman.”

It was a conspiracy theory that even people inside China condemned as an embarrassment to the country. But to a father who had lost his son, it sounded like a credible hypothesis.

Wu Heixing’s father was the head of the Crown Prince Party, which made up half of the Chinese Communist Party.

A political giant comparable to the Chairman, he had begun spreading the rumors in earnest. He had gone even further and formed an independent investigation team to dig into the matter.

“If Mr. Jin regains consciousness, the truth will come to light anyway. But for a high-ranking politician to take the lead in spreading such an absurd conspiracy theory…”

Choi Minwoo let his voice trail off, and Chairman Shao Yang smiled faintly.

*He has no qualms at all.*

No matter how great a feat he had accomplished, the young man before him had lived a very different life and stood in a very different position from his own.

And yet, the young man was actively making his position known, even carefully modulating his pace and tone.

*Was that information true?*

As Chairman Shao Yang suddenly recalled Choi Minwoo’s personal information, he tapped the armrest of his chair.

“Very well. It seems my explanation was insufficient, so let me say it again.”

“I’m listening.”

“My comrades and I already know everything about the matter, and we have made all the necessary preparations.”

“All the necessary preparations…?”

“Before he can appeal to anyone about his son’s death, he will be standing trial.”

The Arch Lich was not the only one to fall in this war.

Corruption and embezzlement involving astronomical sums had been uncovered, and to contain the fallout, the Crown Prince Party would have to sacrifice its very pillars.

Only then did Choi Minwoo allow a gentle smile to spread across his lips.

“Does that answer your question?”

“It’s more than enough.”

That was sufficient for today’s conversation.

A short while later, after exchanging a few more words, Chairman Shao Yang left the room. Choi Minwoo, now alone, suddenly opened his mouth.

“That’s what he says.”

And then one person’s eyes snapped open.

“Oh, fuck. I thought I was going to die from how stifling this was.”
## Chapter artifact 428

# Chapter 428

I raised my upper body and let out the breath I had been holding.

“God, I’m dying.”

Pretending to be an unconscious patient for four days required a considerable amount of patience.

Even more so when I was covered in state-of-the-art medical equipment like this.

*Going back to Murim was awkward under the circumstances.*

Even if I went back, I’d just be stuck aboard the express ship, staring stupidly at the Yangtze.

I was better off finishing things in the modern world properly. As long as I had the System, time was on my side.

Crack. Crack.

As I twisted my stiff neck from side to side, Team Leader Choi gave a short laugh.

“If people had seen this on CCTV, it would have caused quite a commotion.”

“That’s a terrible thing to say. If that had happened, I would’ve bitten my tongue and killed myself.”

Fortunately, there were no CCTV cameras, and my tongue remained safe.

In fact, I was wearing a brain-wave detection device that immediately notified the medical staff whenever a patient regained consciousness, so CCTV was practically unnecessary.

“I’m asking because I’m curious, but how on earth did you fool that machine?”

I shrugged.

“Oh, the brain-wave detector? This isn’t a machine.”

“Excuse me?”

“It is a machine, but I found out that its core power source is a Magic Gem.”

“Then did you use mana…? No, internal energy?”

“Yeah. I caused a kind of malfunction. Adjusting it that much wasn’t difficult.”

After opening my Middle Dantian this time, my control over my internal energy had improved tremendously.

If I couldn’t even fool a few medical devices, I would’ve been so frustrated that I’d have gone to check the temperature of the Han River.

“That aside, what do you think will happen with the Wu Heixing situation? From what Grandpa Jongseok said, it sounds like he made some preparations.”

“This must be the fiftieth time I’ve told you, but he’s not Grandpa Jongseok. He’s Chairman Shao.”

“What’s wrong with it? It’s friendly.”

“……Sigh.”

Team Leader Choi shook his head and picked up an apple from the fruit basket beside him.

Then he pulled out a dagger that looked expensive at a glance, smoothly peeled the apple, and held it out to me.

“I don’t think you need to worry about the Wu Heixing situation. Public opinion is on our side, and Chairman Shao seems to have sharpened his blade.”

“Chairman Shao? To be honest, he seemed a little soft to me.”

Crunch.

I bit into the firm apple. Sweet juice filled my mouth.

If Chairman Shao Yang had been as hard as this apple, the Crown Prince Party would never have occupied the center of power all this time.

As if he had read my thoughts, Team Leader Choi spoke.

“Did you know that Chairman Shao was once branded a reactionary and forced to perform five years of hard labor at a pig slaughterhouse?”

“He was?”

“I heard he became a target of the Crown Prince Party while trying to push for political reform after the Great Cataclysm. But look at the position he occupies now.”

That was enough for me to understand what he meant.

Chairman Shao had a personal grudge against the Crown Prince Party, and after enduring years of hardship, he had risen to the highest position in the country. In other words, he had an iron will.

“A blade that’s been sharpened for a long time has to be swung when the time comes. To the Crown Prince Party, Chairman Shao will become the most frightening swordsman of all.”

“Then Wu Heixing’s father…”

“Considering his political position and the public sympathy for Wu Heixing, execution would be too much. He’ll probably be sent to a political prison camp or a pig slaughterhouse. But he’s already old, so he’ll spend the rest of his life there.”

Wu Heixing, followed by his father.

So this was how father and son ended up.

It wasn’t my imagination that the apple tasted especially sweet today.

I grinned and wiped the juice from the corner of my mouth.

“Lying here for four days was worth it.”

Team Leader Choi peeled a second apple and handed it to me.

“Mr. Jin’s judgment was correct. If the media had found out that you woke up after only half a day, you wouldn’t have been able to avoid suspicion.”

According to the news Team Leader Choi had given me, Lee Jungryong had not even left behind a body, and his death was considered certain by the public. Wu Heixing, who had died with his neck broken, had been caught in the aftermath of the battle and discovered as a gruesome corpse.

If I had woken up perfectly fine after half a day under those circumstances, it would have been a feast for the media, who loved tearing people apart.

“When Mr. Jin first woke up, I couldn’t easily regain my composure either… Had you already thought this far before taking care of those two?”

I answered while biting into the apple.

“I didn’t think that far.”

“What?”

“No, my body was tired and my head hurt, so I just told them not to announce it yet. If people found out I was awake, there’d be hell to pay inside and out.”

“……”

“What?”

Team Leader Choi looked at me with an expression of betrayal, then quietly averted his eyes.

“……It’s nothing.”

“Relax your face. The result is what matters.”

Just as I said, the result had gone incomparably well for us.

Putting the Wu Heixing and Crown Prince Party problems aside, we had not only legally removed the biggest obstacle, Lee Jungryong, but also prevented an even greater catastrophe by defeating the Arch Lich.

Of course, the praise and adoration of people around the world had come free of charge.

I had received the notification that my Fame had risen so many times that I was on the verge of developing a nervous disorder.

Just like now.

> **System**
>
> The attention of the entire world is focused on you!
>
> Your **Fame** has risen dramatically!
>
> There is too much information to process. From now on, Fame-related notifications will be combined and delivered once a month.

“……You should’ve done that from the start, you bastard.”

The sigh slipped out before I could stop it, and Team Leader Choi tilted his head.

“Pardon?”

“Oh, it’s nothing. More importantly, how’s my family?”

My mother and Hayeon had arrived in China only a few hours earlier on a chartered plane, under Chairman Shao Yang’s special orders. They had received treatment surpassing that given to a state guest, complete with an escort of dozens of fighter jets.

“You don’t need to worry. Your mother is resting, and your younger sister…”

“You don’t have to tell me about her. She’ll be fine on her own.”

“……Ah. Yes.”

I couldn’t bring myself to hide it even from my family, so I’d secretly had Team Leader Choi tell them that I hadn’t been hurt in the slightest and was already awake. Still, I was worried about their first visit, which was coming up soon.

*One or two back smacks won’t be enough to settle this.*

I’d rather fight several thousand monsters.

I had left with nothing more than a single message in the family group chat saying that I was going to China. Just imagining the aftermath sent a chill down my spine.

“Team Leader Choi.”

“Yes?”

“When my family comes to visit, you absolutely cannot go anywhere. Understand?”

“……?”

“Promise me. Promise that you’ll stay right beside me and watch over me.”

“Ah, yes. I promise.”

And two hours later—

“You little brat! You little braaaat!”

“Mom!”

“M-Ma’am!”

Team Leader Choi stepped in front of my mother as she charged forward with a tearful roar unlike anything I had ever heard before.

He became the first victim of the back-smacking assault.

“M-Ma’am, please calm down…”

“Get out of my way! Aren’t you going to move?”

Smack! Smack!

“Urgh! Gah!”

“Jin Taekyuuung!”

Then the kick from a fearless soon-to-be college freshman whose entrance exam was finally over struck him squarely between the legs.

It was simply an accident of misfortune.

Wham!

“……Oh.”

“……Ah.”

Team Leader Choi, his eyes wide, muttered in a hollow voice.

“M-My special underwear, which can’t be burned or soaked and even has a semi-permanent cleaning spell on it…”

Goodbye, Team Leader Choi.

You should’ve put a reinforcement spell on it instead.

Thud. Collapse.

I paid my respects to the knight errant of this era, who had been forced to his knees by pain, then calmly prepared for the storm that was about to arrive.

*Open Inventory. Equip Fire Dragon Armor.*

I closed my eyes as I felt the armor of this divine weapon smoothly enveloping my chest, stomach, and back beneath my patient’s gown.

At that exact moment, someone’s palm struck my cheek.

Smack!

Wait a second. A slap across the face wasn’t part of my calculations…

* * *

I regained consciousness after a week.

No, it was announced that I had regained consciousness.

Then, after another week of complicated comprehensive examinations and various other matters being dealt with, I held a brief press conference in front of countless cheers and microphones.

“Mr. Jin. We’ve filtered out any reporters who might cause trouble, so you can simply call on the reporters we selected in advance and take their questions.”

But contrary to what Chairman Shao had said before the press conference, several reporters hunting for a scoop as sweet as honey charged forward like a swarm of bees.

“Mr. Jin! We’ve heard that you and Wu Heixing, one of the casualties of this battle, didn’t get along. Is that true?”

I stopped the security personnel who were trying to drag away the foreign reporter with a gesture and answered.

“I already told the investigators everything, but I’ll say it again. It’s all true.”

Flash! Flash!

Flashes several times brighter erupted, along with a burst of murmuring. A Chinese reporter’s lips twitched with a malicious smile as he asked another question.

“Why? Why was that?”

“That little bastard was rude from the moment we met.”

“Exactly what did he…?”

“He called me a peninsula bangzi and cursed me out. So I called him a chink bastard, and he tried to attack me after the meeting ended.”

The smile vanished from the Chinese reporter’s face.

“A chink? That’s an insulting remark against Chinese people!”

“Oh. Is it?”

I gave a vague nod and gestured to the security personnel.

“Get that chink bastard out of here.”

“Let go! This is suppression of the press!”

“Suppress that bastard’s mouth, too. I’ll talk to Chinese people, but I don’t speak with chinks. He was exactly like that Wu Heixing bastard.”

Right then, someone among the mass of reporters raised a hand and asked a question. This one was Chinese as well.

“Then did you clash with Wu Heixing after that?”

“It wasn’t exactly a clash. I beat him to a jajinmori rhythm[^1] with the spirit of Korea behind it, and he quieted down. After that, we got along well enough.”

“Then…”

“Yes.”

I continued in a solemn voice.

“Wu Heixing was killed by the Arch Lich. There was nothing I could do, and I survived thanks to the top-grade potion he left behind. Once again, I offer my condolences for his death.”

There. My condolences.

You had to say what needed saying and patch up what needed patching. No matter what crimes Wu Heixing had committed while alive or how completely rotten he was as a person, admitting that I had killed him would only hurt my future plans.

*Almost no one would believe me if I said Lee Jungryong had incited Wu Heixing and conspired with him.*

People tended to turn away from inconvenient truths.

I imagined the 100-terabyte USB containing all of humanity’s treasures disappearing, and my eyes welled with tears.

“And… above all, I feel profound sorrow over the death of Hunter Lee Jungryong, a hero of the Great Cataclysm and the great Senior I respected more than anyone. He was truly a good man.”

“Ah…”

The press-conference hall instantly grew solemn. I wiped away the tears rolling down my cheeks and delivered the line I had prepared.

“Although the time we spent together was brief, I will never forget him for the rest of my life. I offer my condolences to everyone who died in this war. I’m sorry I couldn’t save even one more person.”

One sentence that brought the wave of criticism to an end.

Compared with the seriousness of the matter, the press conference was absurdly short, lasting only about thirty minutes. It was broadcast around the world on terrestrial and cable networks in various countries, as well as through an iTube livestream, and recorded a combined total of three billion live viewers.

Before I could even feel the impact, I went to find one person.

[^1]: Jajinmori is a traditional Korean rhythmic pattern.
## Chapter artifact 429

# Chapter 429

“Should we head there right away?”

The acting Head of Security—no, Xiao Shen—approached me as soon as the press conference ended and asked the question. I nodded.

“Let’s do that. You know where he is, right?”

“Yes, I do. Then let’s go.”

Dozens of security personnel led by Xiao Shen formed a circle around me and began moving slowly.

At the same time, chaos erupted all around us. Reporters from various networks, cameras and microphones in hand, came rushing over in a swarm.

“Mr. Jin! Is it true that you’re close to His Highness Prince Felix?”

“Jin-san! Jin-san!”[^1]

*You’re the real jinsang here, asshole.*

[^1]: The Japanese address “Jin-san” sounds like the Korean word *jinsang*, meaning an obnoxious nuisance.

The reporters from various countries hadn’t been satisfied with the press conference and latched onto me, but they couldn’t break through the Hunter security detail.

Of course, there was always someone who managed to push his way closer and stubbornly shove a microphone in my face.

“Mr. Jin Taekyung! We’re both Korean, so just one interview…”

There were people like this wherever you went.

“Oh, sure. We’re both Korean, so please move aside.”

I gave him a halfhearted answer and was about to walk past when I suddenly stopped. His face looked familiar.

I stopped Xiao Shen as he moved to block the reporter and asked,

“Wait a second. Are you with Daspatch?”

“……!”

“I thought so. You published an article about me, didn’t you?”

“Oh, no, I didn’t.”

*That confirms it. You son of a bitch.*

I’d been wondering where I had seen him before. He was the reporter who had posted an article about me having been single my entire life and called it an exclusive.

After that, whenever I typed my name into a search portal, “Jin Taekyung single since birth” showed up as a related search term.

“Shen.”

Xiao Shen, who hadn’t understood our Korean conversation and was looking bewildered, lowered his head.

“Yes, hyung.”

“Crack down on him.”

“Yes, sir.”

Xiao Shen answered energetically and grabbed the Daspatch reporter by the wrist.

“Sir, I will enforce balance.”

“W-Wait a second!”

It was already too late. The reporter was lifted into the air by tremendous force and dropped into the crowd.

Several cameras broke, and curses in languages from around the world poured down like hail.

I let out an exclamation of admiration at the feast of profanity spanning five oceans and six continents.

“So this is the global village.”

“Huh?”

“Never mind. Let’s keep going.”

The public-security officers who had been waiting nearby arrived and joined us, clearing a path.

Under the eyes of the crowd and the protection of an impenetrable escort, I headed toward my destination.

A short while later, I met him in the suite of the five-star hotel where the VVIPs were staying.

“Johnson.”

“Oh, Jin. You got here earlier than I expected.”

Magic Johnson, who had been staring at something with a serious expression, smiled brightly and rose from his seat.

He patted my shoulder with his thick hand, guided me to a seat, and asked,

“So, did the press conference go well?”

Judging by the question, he probably hadn’t watched the press conference himself.

I accepted the canned beer Johnson handed me and answered,

“It was all right. I gave reasonable answers to their questions and wrapped it up in thirty minutes.”

“Ha-ha. I doubt the reporters were very happy.”

“They’ll like me much more than they like you. At least I held a press conference.”

As soon as the war ended, Magic Johnson had shut himself away in his accommodations and refused to show himself.

Unlike Faye Chen or Prince Felix, the other S-rank Hunters, he hadn’t appeared anywhere. Some people had even begun spreading rumors that he was dead.

Only after things had reached that point did he leave a brief comment on his official social-media account. That was the full extent of his public activity.

> I am researching something new.
>
> It is as mysterious and magnificent as the victory we achieved this time.

Most people had probably nodded and moved on without knowing what that meant.

But I was one of the few people who knew the identity of the “new thing” he was talking about.

“So? How did it turn out?”

Magic Johnson answered, the corners of his mouth twitching.

“Who knows?”

“Oh, then I guess it ended successfully.”

“I didn’t say anything.”

“You’re doing a terrible job of hiding that you’re holding back a laugh.”

“I’m not. Not at all.”

*Of course you are.*

At the sight of his eyes shining with anticipation, I let out a quiet laugh.

“I heard you didn’t like it at first.”

“You didn’t come to see me then. Did Choi tell you that?”

“Who else could have told me? At the moment, this secret is known by only three people: me, Johnson, and Team Leader Choi.”

“Ah. But there was one mistake in what Choi told you.”

“A mistake?”

“Yes. I didn’t refuse from the beginning.”

Magic Johnson downed the contents of his five-hundred-milliliter can of beer in one gulp, then continued in a grave tone.

“I was about to fire off a spell.”

“Oh.”

“I’m not joking. Imagine that you were in my position. You probably would have smashed the entire suite to pieces.”

“If I’d been you, I would’ve destroyed the hotel.”

The suite and the hotel had survived only because Magic Johnson was a Grand Mage.

Humans were sometimes called animals of curiosity, but mages were curiosity itself. A Grand Mage at the very pinnacle of magic was no exception.

And when he received an offer involving a “new thing” he had never seen before, he accepted it readily.

“After hearing Choi’s explanation and seeing it with my own eyes, I still couldn’t believe it. This is truly…”

Magic Johnson mumbled with hazy eyes, then suddenly shook his head.

“No. This won’t do. Come and see for yourself.”

“Good. I nearly grew old and died waiting.”

I set down the half-empty can of beer and stood. Without hesitation, I walked across the spacious suite and stopped somewhere inside it.

“This is the place, right?”

Magic Johnson nodded. It wasn’t particularly surprising that an S-rank Hunter sensitive to the flow of energy would notice something strange.

“That’s right. You’re very perceptive.”

“Even someone fairly observant would have a hard time noticing this.”

At a glance, it was nothing more than a section of the room.

But I had known from the moment I stepped into the suite.

*This is magic that blocks out every sound and sight.*

“Wait a moment. I’ll dispel the magic right aw—”

Whoosh. Slash!

Magic Johnson couldn’t finish his sentence. His eyes widened.

The edge of my hand, wrapped in Force, swept down through empty air, and the various spells he had laid out split apart cleanly.

“Jin. What on earth…?”

During my battle with the Arch Lich, I had opened my Middle Dantian and gained the ability to see the texture of qi.

From then on, I had become capable of doing things like this. But I didn’t bother offering an explanation and simply stared straight ahead.

As the magic was dispelled, a single layer peeled away from the space before me.

Beyond it stood a single person.

“Ah, eh, ee, oh, oo. Hellow. Nishe to meet you. I like rice-soup freaks. I wuv kimchi.”

A blond foreigner had been practicing Korean in front of a full-length mirror while holding something in his hands. When he noticed my reflection in the mirror, he turned around.

A hint of laughter crossed his pretty-boy face.

“At last, you have arrived, vile human.”

*Look at this bastard pronouncing only that perfectly.*

I briefly considered hitting him, but soon let out a quiet laugh and opened my mouth.

“You’ve gotten better-looking since the last time I saw you.”

The blond foreigner, the Skeleton King, answered in a smug voice.

“You have become even uglier since the last time I saw you.”

“…….”

“Ugly as hell.”

“……No, you son of a bitch.”

Where on earth had this bastard learned Korean?

* * *

“Hmm. It really is beautiful. There’s no sense of incongruity at all.”

Magic Johnson kept smiling with satisfaction, like a plastic surgeon in Gangnam.

“Even after seeing it again, it’s an unprecedented masterpiece. I might be the first mage in human history to carve a magic circle into the bones of a Skeleton—and not just any Skeleton, but the bones of a completely new Named Monster.”

This wasn’t a surgeon bragging about his own work. It was simply the truth.

Shiny blond hair. Mysteriously glowing golden eyes. A body nearly 190 centimeters tall, with well-balanced proportions and long limbs covered in just the right amount of body hair.

And that wasn’t all.

The clearly defined muscles and veins. The reactions of his body whenever he breathed or swallowed.

Even I had to pay close attention to notice anything strange. The Skeleton King had taken on the complete appearance of a human being.

“……Wow. This actually works.”

I had asked him to do it thinking that, at worst, I had nothing to lose.

I hadn’t expected it to be this perfect.

I swallowed hard in amazement and reached out to touch his blond hair.

That was when it happened.

Swish.

The Skeleton King took one step back and looked at me arrogantly.

“Take your filthy hand away. You will damage my hair.”

“…….”

“If I go bald, will you take responsibility?”

*This bastard is practically human now…*

I was so dumbfounded that I couldn’t even speak.

Ignoring me as I stood there speechless, the Skeleton King looked at his reflection in the full-length mirror and smiled with satisfaction.

“Hmm. Insanely handsome.”

“I’ve been wondering this for a while, but where did you learn expressions like that?”

“On the Internet.”

“The Internet?”

“Indeed. I spent a whole week browsing the shit out of it.”

“Wait. Do you have a phone, too?”

“That kind human over there bought one for me. Thank you, Johnson.”

Magic Johnson was using a translation spell. He nodded with a pleased smile.

“I wish you a successful new beginning, Mr. King.”

“Thank you, Johnson.”

*“Thank you, Johnson,” my ass. When did he learn basic English, too?*

I immediately turned to Magic Johnson.

“Wait. You bought him a phone, too?”

“Hey, Jin. What’s the problem? My youngest daughter is five years old, and even she uses a smartphone.”

“That’s your youngest daughter. He’s the Skeleton King.”

“Hold on. Vile human, I apologize for interrupting your conversation, but I must say this.”

The Skeleton King cut in with a serious expression and continued,

“From now on, call me Stone-King.”

“What fresh hell is this supposed to be?”

“That is my new name. Stone King. Born in Atlanta, Georgia, United States…”

I muttered as I felt a headache coming on.

“Should I just kill him? I’m seriously about to.”

“Would you kill a citizen of the United States?”

“Who’s an American citizen, you lunatic?”

“Perhaps not right now, but I can soon obtain United States citizenship.”

“You should write a web novel for KakaoPage instead. What kind of idiot comes up with that bullshit?”

Magic Johnson shyly raised his hand.

“Jin, with my connections, it should be entirely poss—”

“Ah! Aah! Aaaaah!”

This was driving me insane.

I clutched my throbbing forehead and spoke to Magic Johnson.

“Johnson.”

“Hmm?”

“What I asked Team Leader Choi to do was simply make him look like a human being.”

“Ah, of course. That was what you asked. But I heard this friend desperately wanted it.”

All of this had begun shortly after I first regained consciousness.

The Skeleton King had loudly complained about how long he was supposed to remain trapped inside that cramped Inventory.

His argument was that, in consideration of the great contribution he had made during the battle, he deserved an appropriate reward. From my perspective and Team Leader Choi’s, it was a perfectly reasonable demand.

*He protected Team Leader Choi and Xiao Shen during the battle with Lei Fei, and we managed to defeat the Arch Lich thanks to him.*

I had already been thinking that I needed to reward the Skeleton King.

And if he could take human form, it would be convenient in many ways.

He wouldn’t need to hide anymore, and he could sign a contract with the Peace Guild so that they could help each other.

But…

“For one thing, he doesn’t look like the East Asian appearance I asked for. No matter how many foreigners there are in Korea these days, he’s going to stand out. Especially with a face like that.”

Before Magic Johnson could answer, the Skeleton King cut in with a stiff voice.

“I asked him to change it.”

“What? Why?”

“I saw it on the Internet. Handsome white men do well everywhere in the world.”

“……And what are you going to do with that?”

“I wish to date.”

“Oh, God.”

As I let out a deep sigh, Magic Johnson patted my shoulder.

“It’s all right, Jin.”

“What do you mean, it’s all right? Do you have any idea how terrifying social media is these days? What if netizens dig up his identity and discover that he wasn’t born in Atlanta, Georgia, United States, but is actually a native of the Demon Realm? Does that make any sense? Why did you agree to a request like that?”

“I wanted to try making a face that suited my tastes.”

“What?”

“That face is my ideal type.”

*Oh, for fuck’s sake…*

I had just lost my words when the final blow to my patience arrived.

“Do you feel wronged? Ugly as hell.”

“You son of a bitch!”

Crack!

I launched myself forward and buried my fist in the crown of his head.

The Skeleton King let out a strangled groan. He must have bitten his tongue, because bright red blood spurted from the corner of his mouth.

*Red blood? Was this an illusion spell? He really did a great job of implementing—*

No, that wasn’t the point.

“Die! Die!”

“Ghk! Guhk!”

As two heavily built men began rolling around, the suite was transformed into a disaster zone in an instant.

The desk was caught in the aftermath and collapsed with a splintering crack. The stack of papers Magic Johnson had been examining came cascading down onto my face.

“W-Wait! Vile human! I cannot see!”

“I’m going to teach you some manners today…!”

And then, in the next moment, I stopped moving.

There were strange yet familiar symbols visible among the sheets of paper blocking my view.

*This is…*

I left the Skeleton King where he was and rose from my seat, dazedly picking up a sheet of paper printed with the symbols.

*Sichuan.*

There was no mistake.

It was the exact same pattern I had seen in Sichuan—not the province in China, but Sichuan in Murim.

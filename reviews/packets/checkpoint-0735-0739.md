# Checkpoint Review — 735–739

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

# Chapters 735–739

## Plot

Odin Guild Master Michael Silbert reveals that Jin Taekyung is a serious threat but assumes Cheon Taemin is no longer relevant. After Huginn delivers weapons to foreign collaborators, a Monster Wave destroys Ares Guild’s Paris branch. Michael and roughly one hundred Odin Hunters eliminate the monsters, then present Odin as Paris’s savior.

Michael privately admits that he arranged the attack with Middle Eastern fanatics seeking revenge, supplying them with bombs and unrefined Magic Gems. He prepared the casualties, evidence, media narrative, and press conference to make Odin appear heroic while isolating Ares Guild. Jin nearly attacks him, but Team Leader Choi and the Skeleton King prevent it because Michael has engineered the situation so that Jin would appear responsible.

The forced Quest Chain of Terror Attacks begins with a second strike in London. Within twenty-four hours, ten coordinated Monster Waves hit major cities, landmarks, corporations, and Guild branches worldwide. Odin suppresses five of them, while Michael publicly declares the attacks deliberate terrorism and releases footage that reinforces his narrative. Governments and civilians descend into chaos, with thousands dead.

A hidden Prophet confirms that ten fanatical warriors carried out the attacks and died. The Prophet broadcasts a threat beside the severed heads of former IS and Al Qaeda leaders, declares that judgment has begun, and says everything started with the audience. A later transmission shows a masked figure whose face allegedly matches another identity of a young hero by 99.99 percent, leading public suspicion toward Jin Taekyung.

The Skeleton King sees the growing condemnation of Jin and decides that revealing the truth immediately would cause an even greater backlash. He carries a silver tray into a large room, where an unidentified person sits cross-legged beyond the doorway.

## Continuity

- Michael Silbert orchestrated the destruction of Ares Guild’s Paris branch and the wider chain of terrorist Monster Waves with Huginn and ten Middle Eastern fanatics.
- The attackers used bombs and unrefined A-rank Magic Gems near high-mana Gates; the coordinated attacks killed thousands.
- Michael prepared Odin Guild’s rescue operation, casualty reports, CCTV evidence, and public messaging in advance.
- Odin Guild suppressed five of the ten Monster Waves and now claims the role of the world’s protector.
- The attacks targeted crowded landmarks, major corporations, and overseas branches of major Guilds, with isolating Ares Guild as Michael’s objective.
- The forced Quest Chain of Terror Attacks remains active and cannot be refused; London was the second attack, with eight additional attacks originally planned.
- The Prophet’s organization has completed the first ten missions, and the Prophet promises further judgment and punishment.
- Public opinion is turning against Jin Taekyung because of the masked figure and alleged 99.99-percent identity match.
- The Skeleton King believes the public narrative is false or incomplete but cannot safely reveal the truth yet.
- An unidentified person is sitting cross-legged in the room the Skeleton King enters; the reason for the silver tray and the person’s identity remain unknown.
- Cheon Taemin remains unconscious, and Ares Guild remains vulnerable while Jin is being publicly targeted.
- Jin’s abilities remain reduced by ten percent while the thirty-day Idle Bystander Title is active.

## Translation Decisions

- Render **몬스터 웨이브** as **Monster Wave**.
- Render **선지자** as **The Prophet**.
- Render **인샬라** as **Inshallah**.
- Render **신의 품** as **the embrace of God** and **핏값** as **blood price**.
- Render **시벌좌** as **Lord Fuck**.
- Render **스켈레톤 킹** as **Skeleton King**.
- Render **조국일보** as **Joguk Ilbo**.
- Preserve Michael’s polished public heroism and concealed manipulation, Jin’s restrained fury, Choi’s pragmatic caution, the Skeleton King’s archaic voice, and the Prophet’s religiously charged threats.
- Preserve uncertainty around the masked figure, the Prophet’s identity and motive, the true purpose of the attacks, and the unidentified person in the final room.

## Durable state

{
  "active_continuity": [
    "The ten Monster Waves are publicly established as planned terrorist attacks using bombs and unrefined A-rank Magic Gems near high-mana Gates, with thousands dead.",
    "Michael Silbert has released Odin Guild footage and publicly shaped the narrative that the attacks were deliberate terrorism.",
    "The Prophet has threatened continued attacks, judgment, and punishment after displaying the severed heads of the former IS and Al Qaeda leaders.",
    "A masked figure is being linked by alleged 99.99%-matching video analysis to another identity of a young hero, and public discussion is targeting Jin Taekyung.",
    "The Skeleton King knows the public narrative is false or incomplete and cannot safely reveal the truth yet.",
    "An unidentified person is sitting cross-legged inside the room the Skeleton King enters."
  ],
  "continuity_sources": [
    739
  ],
  "open_questions": [
    "Who is the masked figure shown in the Prophet's transmission?",
    "What does the Prophet mean by saying that all of this began with the audience?",
    "How will the Prophet's promised further judgment and punishment proceed?",
    "Why is the Skeleton King bringing a silver tray to the unidentified person?",
    "What is the identity and condition of the person sitting cross-legged inside the room?"
  ],
  "safe_through": 739,
  "temporary_decisions": [
    "Render 선지자 as The Prophet.",
    "Render 인샬라 as Inshallah.",
    "Render 시벌좌 as Lord Fuck.",
    "Render 스켈레톤 킹 as Skeleton King.",
    "Render 조국일보 as Joguk Ilbo."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 735

# Chapter 735

A middle-aged man wearing a thin silk gown gazed out the window.

Clouds carrying January’s chill swept past before his eyes, so close he could almost reach out and touch them. Far below, buildings and plazas divided into neat districts spread across the ground.

The view of a great city steeped in history. Countless people moved below, reduced to tiny dots within the city.

The gloomy gray sky and streets submerged in mist were hardly a sight befitting Paris, the City of Light. But the middle-aged man did not care.

He loved everything about this city—about Paris.

The world viewed from a skyscraper too high for even the mist to reach was always beautiful.

Especially on a day like this.

*Ding. Deeeeng—*

The bells ringing out across the plaza announced seven in the morning. The middle-aged man tore his gaze from the windows covering one wall and slowly turned around.

It was a massive study.

At the round table in its center, over ten figures waited for him, appearing amid the green glow unique to holograms.

“It’s been a long time since we gathered in one place like this. The last meeting was probably… three years ago?”

The corners of the people’s mouths, visible beneath their masks, curled slightly at the joke the middle-aged man made as soon as he took the seat of honor.

Three years?

They had held a secret meeting only two nights ago.

—If I remember correctly, the last one was ten years ago.

—Ten years? Has it really been that long?

—Wasn’t it more like thirty years ago?

—Damn it. Thirty years ago was the Great Cataclysm. I don’t even want to remember the hell we went through, so drop it.

Quiet laughter mingled with the conversation passing back and forth.

Watching them, the middle-aged man smiled gently.

“You all seem remarkably relaxed. Still, it is nice to exchange this sort of idle chatter once in a while.”

—…!

—…!

Silence descended with that quiet remark.

The people who had all fallen silent at the same time, as if they had made an agreement beforehand, looked toward him. The middle-aged man continued speaking with a smile on his face.

“I did not call this meeting to listen to pointless nonsense or trashy small talk like this… What does everyone think?”

The people’s eyes wavered at the slightest sound of his breathing or the smallest movement of his fingertips.

His overwhelming presence came through despite the hologram. So did his aura.

Every person attending the meeting was a major figure, yet none of them could hope to rival the middle-aged man.

The reason was simple.

The man before them was the master of Odin Guild, known as the greatest Guild in the world, and one of the absolute beings capable of controlling the world.

—I-I apologize, Michael. I was simply pleased that everything was proceeding without a hitch…

“I did not say that to hear excuses.”

Michael cut the person off and continued.

“It only seemed absurd to see you all acting as though everything were already over.”

—……

“Our opponent is more daring than expected. Otherwise, could they have carried out such a lunatic act?”

There was not a single person in the room who did not know what that “lunatic act” referred to. No—the entire world knew by now.

Making the Mana Cultivation Method public.

To a tiny number of people, it was madness capable of destroying the established order. But their opponent had turned that madness into reality.

“I sent Huginn, but they still refused to listen. Unbelievably reckless… though I suppose that means they’re just that confident.”

One person cautiously opened their mouth.

—If—just hypothetically—the one they’re counting on is Sky…

“I believe I already said that you need not concern yourselves with that matter.”

—…Understood.

The answer was not entirely convincing.

Until now, Michael’s word had been law to all of them.

Once he had spoken with such certainty, they had no choice but to dig a hole for any lingering doubts deep in their hearts and bury them there.

But this time, every one of them could not help turning the question over in their minds.

Because the person in question was none other than Cheon Taemin.

*Even so, how can he tell us not to worry about a matter this serious?*

*If Sky gets involved, what will happen then?*

*What kind of information does he have to be so certain…?*

The thoughts continued to circle endlessly through their minds.

Michael’s information had always been reliable. No one knew who provided it or what methods he used to obtain it, but as long as they trusted and acted on the information he brought them, they profited.

Immense wealth and fame. Lofty social status.

But no matter how strong and high a fortress was, it could collapse in an instant.

And the name Cheon Taemin was not something they could simply bury through faith. The sense of crisis they felt was conveyed in its entirety to one person.

*Tap. Tap.*

Fingers slowly tapped against the round table. At the same time, those who felt the waves of powerful mana shook off their thoughts and returned to reality.

“You seem uneasy.”

At the gentle voice, the people hurried to answer.

—Not at all.

—How could we be?

—Our alliance is powerful. There is no way we could lose to brats like them.

They swallowed the needless addition: *if only Cheon Taemin were not involved.*

For now, they could only trust Michael. Judging by the power and ability he had shown them all this time, those mere fledglings would not be opponents at all, just as one of them had said.

—Choi’s resourcefulness is impressive, but his limitations are equally clear.

—The same goes for Jin Taekyung. No matter how strong he is, he cannot break through the walls we have built.

There had certainly been a time when such a thing was possible.

A time so cruel and chaotic that it could only be called the Great Cataclysm.

Humans slaughtered monsters. Monsters slaughtered humans. And humans slaughtered other humans like livestock.

It was a turbulent period when nothing seemed strange, no matter what happened.

But the Great Cataclysm had ended.

On a sea lashed by storms, nothing that happened would seem strange. But in a peaceful world like this one, even a ripple could not cause meaningful change.

The Mana Cultivation Method revealed this time was no different.

—By making the Mana Cultivation Method public, they have caused us enormous losses as well… But the immediate crisis has been dealt with, so there is no reason for concern.

—Exactly. In the end, even the media did not dare criticize us. Above all, it was thanks to your swift action, Guild Master.

Michael silently nodded.

The news about the Mana Cultivation Method, released in Odin Guild’s name at sunrise, was spreading across the world through all kinds of media even now.

The public criticism aimed at the established major Guilds would gradually die down, and the fledglings who had ignored his generous offer would soon regret it.

This time, he would not settle for words. He would show them directly through his actions.

*How foolish.*

Michael muttered inwardly.

In this world, the Mana Cultivation Method was a treasure beyond calculation.

At a time when a Guild’s standing and a nation’s influence depended on how many powerful Hunters they possessed, those fools had revealed it to the entire world.

*They should have thought it through first. Why do they think there has never been a precedent for something like this?*

There had been fools in the past who stepped forward armed only with morality and a sense of justice.

They had been powerful figures recognized throughout the world. They had wanted to share the special abilities they possessed with everyone—and that was why they had died.

*And the result will be the same this time.*

History repeated itself.

Although the Mana Cultivation Method had been made public because of their opponent’s unexpected and impulsive act, they would have to pay the price for their foolishness.

That was the law of this world.

There was only one thing that continued to bother him: the young man who had caused the greatest change in recent times.

*Jin Taekyung.*

Unlike Choi Minwoo, whom Michael still considered a fledgling, that bastard was a powerful figure no one could deny.

In less than a year, he had piled up countless achievements and a fearsome reputation. Not long ago, he had even brought down the Ares Guild headquarters single-handedly, despite hundreds of Hunters—including Go Jun—waiting there.

That was not all.

The world did not know it yet, but Michael knew that Jin Taekyung was the one who had recently swept away terrorist organizations and rebel groups.

*Power that ranks among the best even among S-rank Hunters. And daring.*

It was a realm that not one of the people chattering endlessly before him could ever reach.

An S-rank Hunter leading a world-class major Guild. A politician who could control a powerful nation. A tycoon who owned hundreds of Gates and oil fields…

Every one of them was more than worthy of being called a major figure. Yet in Michael’s eyes, they were all nothing more than greedy idiots.

*Of course, thanks to that, I was able to raise Odin Guild to the top of the world.*

Michael muttered inwardly and clicked his tongue softly.

*Tsks.*

The endless voices vanished, and everyone’s eyes turned toward him.

Michael studied them one by one. Then, all at once, he sensed someone approaching from far away and opened his mouth.

“It seems we have a guest.”

—Ah, then…

“I will notify you separately about the next meeting.”

*Bzzzt.*

That was all.

The instant Michael spoke, the holograms melted away and disappeared. At the same time, the study’s tightly closed doors swung wide open at a gesture from him.

“So, did you enjoy your trip?”

A man in old-fashioned clothing answered the question Michael had been waiting to ask.

“I was merely following orders.”

“You are always so stiff. Huginn, come inside.”

“Thank you.”

*Thud.*

Huginn removed his hat and dusted it with a few sharp taps before stepping into the study.

Michael saw grains of sand scattered near the door and smiled calmly.

“You seem to have been moving around quite a bit.”

“It was a very tight schedule.”

“You went a long way. It must have been difficult. Did you encounter any problems?”

“There were some, but I resolved them.”

Despite his curt answer, Huginn’s eyes still burned with the afterglow of battle.

Michael nodded without showing any particular reaction.

Huginn was a talent Michael had personally selected and trained. As a fixer, he had always been the best, and he carried out every mission perfectly.

Just like this one.

“Did you bring your friends?”

“Yes. When they heard why I had come, they volunteered to cooperate. Unlike the reception I received in Korea, they were all very kind to me.”

“What considerate friends, coming all that way. Where are they now?”

“They should all be heading toward their destinations by now.”

“And the gifts?”

“I handed them over without fail.”

Huginn took a pocket watch from inside his coat and checked the time before adding:

“There is about an hour left until the first gift is delivered.”

“One hour, hm? Good. Would you like to have a cup of coffee while we wait?”

“If possible, I would prefer black tea.”

Michael smiled pleasantly and prepared one cup of coffee and one cup of black tea.

Exactly one hour later, he confirmed with his own eyes that his orders had been carried out without fail.

*BOOOOM!*

Beneath the pale clouds, red flames surged upward with a deafening roar. And then…

*Whooosh!*

As he watched the air slowly distort, Michael murmured lightly:

“As expected, it is a beautiful city.”

A building was engulfed in flames.

Centered on the Paris branch of Ares Guild, space began to tear apart.
## Chapter artifact 736

# Chapter 736

It had certainly started out insignificant. Just a slight tremor. Nothing more, nothing less.

But that had only been a small omen.

*Rumble…*

The ground shook.

The visitors standing in line outside the Louvre instinctively ducked, while the lower-class residents of Paris’s 10th arrondissement, who had been fighting as they clutched one another by the collars, scattered in all directions with curses.

And the citizens of the 6th arrondissement…

“Ah…”

They forgot even to scream. With vacant eyes, they stared at the scene unfolding before them.

*Gooooom.*

A crimson-black darkness coiled around a skyscraper that soared to dizzying heights before surging upward.

At the moment everyone held their breath before that ominous, overwhelming energy unlike anything they had ever experienced—

*BOOOOOM!*

The skyscraper that had once housed Ares Guild’s Paris branch exploded as though it were bursting apart.

The defensive Magic layered over the building’s exterior. The sturdy frame designed to withstand missile bombardments. Every last bit of it shattered and blew outward.

Large and small fragments that had once been part of a building roughly fifty stories tall came pouring down, engulfed in flames.

*Fwoosh. Whoooooosh!*

“……!”

It was an unbelievable reality, yet one that could not be denied.

As countless fragments rained down and blocked out the sky, people suddenly thought:

*Maybe today really is the day of the apocalypse described in the Bible.*

Then they saw the air twisting strangely, and that suspicion hardened into despairing certainty.

*Fwoooooosh!*

They had never witnessed it with their own eyes, but people who had lived through the brightest civilization in history knew the name of the phenomenon.

“Monster Wave…”

Someone’s voice slipped out like a groan.

Yet even as countless fragments fell over their heads and monsters stepped out from beyond the warped space, no one could run.

The Sorbonne University students riding their bicycles to class. The young couple strolling through the Luxembourg Gardens with a stroller. The police rushing around to calm the citizens.

Everyone who had been moving busily in their respective places—and the entire 6th arrondissement with them—froze where they stood, submerged in a fear and chill that seeped into their bones.

And then.

*BOOM! BOOM! BOOM!*

Amid a rain of fire covering a radius of more than a hundred meters, the doorway to hell opened.

*Thud. Thud.*

Monsters with arms and legs as thick as the pillars of a temple, each bearing two heads on a single massive body, pounded their chests and roared.

—Gwooooooar!

*Crash!*

Glass shattered in every direction, unable to withstand the waves contained in their roar.

Fear, something only High-Rank monsters could release, flew out like invisible ropes and bound thousands of humans.

—Grrrr.

A cry filled with deep satisfaction.

It was time to hunt.

No—it should have been.

*Whoooooosh! Boom!*

At that moment, accompanied by a flash of light, the monster at the front staggered. Everything that had been atop its shoulders had vanished.

*Thud!*

The ground shook. By then, the hundred or so monsters had raised their heads as though they had made a silent pact.

Among the thousands of humans standing frozen in place, predators hiding among the flock were revealing themselves.

Alongside dazzling flashes too fast for the eye to follow.

*Whoooooosh! Crack!*

*Rattle, rattle.*

Flesh and bone were crushed, and blue blood sprayed in every direction.

The Twin Head Ogre that had survived by sacrificing one of its two heads unknowingly took a step backward.

It did not know what threat awaited it there.

*Crunch!*

A gigantic fist burst the only head it had left like a watermelon.

A giant whose terrifying strength and physique were on an entirely different level from the other ogres.

The giant licked the brain matter of its subordinate from its fist. Reflected in its enormous pupils was the figure of a human with golden eyes.

—Karsh. Marto.

It was Demon Realm language, and it sounded almost like a curse.

But Huginn, the golden-eyed human, paid it no attention. He turned around and bowed politely to someone behind him.

“It is a Named Monster—a Giant Ogre. What shall we do?”

A calm voice answered:

“Not bad. This is about right for putting on a show.”

“What do you mean?”

“I’ll take that one. Clear out the rest.”

That was all.

The moment the order was given, Huginn and a hundred Hunters crossed the space as one body, like the storm and lightning painted across their armor.

Just like Odin, the name of the ancient god who symbolized them.

*Whooooooosh! Slash!*

Clash.

Then slaughter.

Limbs as thick as logs flew into the air, while dazzling aura cut through the magical energy surging around them.

It was like a scene from a myth.

Even myths filled with countless figures had a protagonist who shone alone.

—Gwooooooar!

*Crack!*

One Strike.

The roar that had seemed capable of swallowing the entire city vanished.

*Ruuuuumble!*

The Giant Ogre, dozens of meters tall, dropped to its knees.

Before a single human who looked insignificant compared to the monster’s mountain-sized body.

But to the people who had watched the entire scene without missing a moment, that human did not look insignificant at all.

A hero who had protected them from danger.

A true giant stood there.

The people who had returned alive from the brink of death shouted the hero’s—or heroes’—name with one voice.

“Michael! Michael!”

“Odin Guild!”

Amid the enormous roar spreading like wildfire, Michael declared in a powerful voice:

“Please rest assured. As long as Odin Guild and I are here to protect you, no danger will befall you.”

Then, as he looked toward the ruins buried beneath heaps of concrete, he added in a voice too quiet for anyone to hear:

“At least today.”

With a faint smile, he stepped toward the remaining group of monsters.

Toward the name Ares, which had fallen from the building alongside countless fragments, stripped of its former shine.

And he trampled it beneath his feet.

* * *

**Odin Guild Declares Support for Ares**

**Odin Guild Master Michael Silbert: “We Offer Our Heartfelt Applause for Ares Guild’s Actions in the Public Interest and Will Walk Forward Alongside Them”**

**Odin Guild Makes a Surprise Release of a New Mana Cultivation Method!**

**Senior Odin Guild Official: “A Large-Scale Project We Have Been Preparing for Years. If You Think We Released It with Public Opinion in Mind, That Is Regrettable, but We Will Endure It…”—Dismisses Controversy Before Release**

The breaking news I learned from the Skeleton King early that morning was certainly astonishing.

The problem was that before the shock had even faded, another wave came crashing in.

A much larger and more terrifying wave.

*Bzzzt. Bzzzt.*

Team Leader Choi’s smartphone, which had been lying on the table, began to vibrate.

A few seconds later, another breaking-news report flowed from the holographic television. It was almost impossible to believe.

—A Monster Wave has occurred in Paris, France. The incident took place at a skyscraper in the 6th arrondissement of Paris, which has been identified as the Paris branch of Ares Guild, causing tremendous shock…

—The French government has begun an operation to seal off the 6th arrondissement under international emergency law. The exact number of casualties and the details of the suppression operation remain unknown…

—Local residents have testified that Odin Guild, which was located nearby, was the first to head toward the scene…

News reports flowed from the several televisions installed throughout the restaurant.

But among the countless words spilling from the lips of people with different skin colors and speaking different languages, only three terms pierced my ears.

Monster Wave.

Ares Guild’s Paris branch.

And…

Odin.

*Ding.*

> **System**
>
> A sudden Quest, **The Darkness Over Paris**, has been generated!
>
> You cannot choose whether to accept this Quest. By the authority of the System, the Quest will proceed by force!
>
> **Quest**
>
> **The Darkness Over Paris**
>
> Every choice is always followed by consequences.
>
> Your enemies have brought down Ares Guild’s Paris branch, and the city that once overflowed with life is now shrouded in the roars of monsters and darkness.
>
> Rescue them as quickly as possible and repel the monster army to prevent innocent casualties!
>
> **Grade:** Supreme Peak
>
> **Restriction:** Jin Taekyung
>
> **Mission:**
>
> Rescue the survivors of the Paris branch (Incomplete)
>
> Suppress the Monster Wave (Incomplete)
>
> **Reward:** Determined by the outcome
>
> **Failure:** Determined by the outcome

“……!”

Everything happened so suddenly.

The System notification ringing in my ears. The holographic windows floating in the air before me.

But the instant I saw and heard all of it, I was already moving on instinct.

No—all of us were.

“Gather around me. Quickly!”

The moment Team Leader Choi shouted urgently and tore a Magic Scroll from inside his coat—

*Fwoosh!*

A blinding flash suddenly burst forth and wrapped around us.

* * *

*If I can’t come to help and you need to move somewhere as quickly as possible, make sure you use this. If you know the exact coordinates, you’ll be able to reach your destination safely.*

That was what Magic Johnson had told me several weeks earlier, around the time the Middle East cleanup operation was coming to an end, when he handed me the Magic Scrolls.

And the several dozen Teleport scrolls I had received back then were now being consumed at intervals of only a few seconds.

*Rip!*

The specially treated, durable parchment tore apart. At the same time, the mana sleeping inside it awakened, and the brilliant flash that poured out once again embraced us before leaping toward the predetermined coordinates.

*Flash!*

Flashes erupted without pause.

As we continued leaping through space—sometimes tens of kilometers away, sometimes hundreds—the body began to creak, and my mind started to cry out from exhaustion.

*Hup.*

The spatial-transit Magic cast in rapid succession had brought on an overload.

But no one stopped. Not even Team Leader Choi, who was probably bearing the greatest burden among us.

*Grind.*

Clenching his teeth, he pulled out another scroll.

Ignoring the foreign airport Hunters thrown into confusion by our unauthorized spatial movement, he tore one scroll, then another before the aftereffects of the first had even faded.

He continued tearing scroll after scroll without pause.

Every time the light flashed, the scenery around us changed, along with the skin and languages of the people nearby.

And when a flash whose number I had long since lost count of finally faded—

we could see it at last.

The ruins that had once been called Ares Guild’s Paris branch.

The enormous corpses of monsters scattered everywhere. The graveyard of concrete and rebar, from which not even a handful of life could be felt.

At the same time, a sound only I could hear pierced my ears.

*Beep.*

> **System**
>
> You have not completed a single mission.
>
> The sudden Quest, **The Darkness Over Paris**, has failed.
>
> Every event is always accompanied by a reward and a price. You will receive penalties for failing the Quest.
>
> EXP decreases drastically.
>
> Fame decreases drastically.
>
> The special Title **Idle Bystander** will apply for the next 30 days.
>
> Due to the penalty effect of the special Title **Idle Bystander**, all stats decrease by 10%.

“……Ah.”

I let out a short groan.

Quest failure?

A massive penalty?

None of that mattered.

The atmosphere around us, which had begun to murmur after belatedly noticing our arrival, did not matter either. Neither did the group making its way across the ruins.

Of the several holographic windows floating in the air, all five of my senses were drawn toward only one.

> **System**
>
> You have not completed a single mission.

That was all.

That cold, rigid sentence pierced through my eyes and tore through my mind. I already knew what it meant.

*They’re dead. All of them.*

That was reality.

Ares Guild’s Paris branch no longer existed.

Neither did the people who had been peacefully beginning their day nearby.

The skyscraper that had once reached the clouds had become a ruin blanketed in death, and the people who had been laughing and talking here only a few dozen minutes ago had crossed a river from which they could never return.

Just like the unidentified corpse buried beneath the wreckage of the building before me.

*What was I thinking?*

As I stared blankly down at the unidentified corpse, I suddenly reached out and grabbed his arm. Only after pulling on it did I realize that it was the arm of another corpse.

And that was not the end.

When I dragged one corpse out, three more appeared. When I pulled those away, severed limbs emerged from beneath them.

“H-how…”

“Wicked human. This… this is truly…”

Hearing Team Leader Choi and the Skeleton King’s voices, which felt impossibly distant, I silently looked around.

The streets around the former branch had been reduced to a wasteland. Smoke laced with the smell of burning flesh rose acridly into the air, and the bodies of people who had not yet been recovered lay scattered everywhere.

Then how many people were sleeping beneath the ruins where I stood?

And why had they—

*Why did they have to die?*

My stomach burned as if I had swallowed a ball of fire.

I clenched my teeth so hard they felt ready to break. Swallowing the blood flowing from my split lips, I forced down the three jiazi of Scorching Yang Qi struggling in my dantian.

I could not get any more agitated. I had to remain calm and composed—more than ever.

Because if I failed to do so, I would not be able to face the master of that enormous energy approaching from behind me with a clear mind.

*Michael Silbert.*

As I recalled one man’s name, I slowly turned around.
## Chapter artifact 737

# Chapter 737

Michael Silbert.

It was a name no modern person living in this world could fail to know.

He was the Guild Master of Odin Guild, called the greatest in the world, and an extraordinary figure even among the countless heroes born from the Great Cataclysm.

People loved Michael Silbert, who had risked his life to save them.

I had admired him too.

No—I *had* admired him.

*Step.*

Footsteps stopped behind me.

At the same time, I slowly turned around and saw him.

A man standing atop the heat-soaked ash and ruins, gazing steadily in my direction.

“So, it’s you.”

A single sentence broke the brief silence.

But that was enough. He and I both recognized each other’s existence.

Even without all the photographs of his face circulating through the media, that fact would not have changed.

*This is…*

I could feel it.

The immense power compressed inside that neither-large-nor-small body.

It was a force more powerful than Lee Jungryong’s—or rather, more powerful than any S-rank Hunter I had ever faced.

And that was not the only thing I realized.

“……So it was you?”

Michael Silbert.

The moment I met his gray eyes, I became certain.

I knew whose work the ruins beneath my feet were.

I knew who had started this terrible disaster.

And when I asked my question—similar to, yet different from, the first words he had spoken—Michael Silbert answered in a calm voice.

“What a pointless question. If it wasn’t me, who else could it be?”

“What?”

“It’s an obvious and trite story anyway. There’s no point in asking or answering anything more.”

What the hell?

What the hell was this bastard talking about?

I stood frozen, having forgotten my anger for a moment. Michael blinked at me with a bewildered expression.

“I don’t understand why you look so surprised. We already understand each other’s intentions, and now that negotiations have broken down, this is merely the inevitable next step.”

“You son of a—”

“Didn’t I warn you through Huginn? I told you that refusing my proposal would come at a price.”

Michael Silbert cut me off as though it were nothing important.

Then the Great Cataclysm’s hero, loved by people all over the world, reached out and gathered the ash drifting through the air in his hand.

“From what I hear, you’ve been rather busy these past few weeks. Were you wandering around that vast desert searching for an oasis?”

“……!”

“Let me give you one piece of advice. There are no perfect secrets in this world—not even in the Pentagon.”

He opened the fist he had clenched.

The ash mixed with a monster’s blood brought back a scene I had witnessed countless times a few weeks ago.

Fanatics dying in droves all around me. Their screams. Grains of desert sand made sticky with blood flowing like a river…

And beyond those memories flashing before my eyes, a low voice pierced my ears.

“If you wanted to make the world peaceful and good, you should have uprooted them completely from the beginning.”

“……You’re saying…”

“Considering that the other party was a bunch of insane fanatics, it was a perfectly reasonable deal. I wanted them to pay for ignoring my warning, and they wanted a weapon for revenge.”

I understood.

Only now did I understand.

The true cause of this sudden Monster Wave.

The reason the madman before me could stand there with such confidence.

*The stratagem of borrowing another’s knife to kill.*[^1]

And at the very moment I understood everything—

*Fwoosh.*

My vision burned hot.

Three jiazi of Scorching Yang Qi surged from my dantian, transformed into lava, and flowed through my limbs and bones.

I was already prepared.

From the moment I first met him, my mind had been spinning without pause, searching for the optimal movement.

*One step.*

A single step would be enough.

The instant my foot touched the ground, the space between him and me would vanish. Then I could shut that mouth spouting bullshit with my Flame-Extinguishing Divine Fist.

No.

I had to shut it.

For the sake of the innocent people who had died at the hands of another human rather than a monster.

And to eliminate the source of an even greater disaster that would soon arise.

But—

*Grab.*

Two hands seized my shoulders, and a familiar voice struck my ears.

“Mr. Jin Taekyung!”

“There are eyes on us. Not now.”

Team Leader Choi and the Skeleton King.

When I thought of the men gripping my shoulders—men who must have been holding back their own anger as well—the fury boiling inside me slowly began to subside.

I knew it too.

They were right.

Rushing at the bastard standing before me was easy. But dealing with the aftermath would be extremely difficult, even for me.

*I have neither evidence nor justification enough to convince people.*

To the world, Michael Silbert was the hero of the Great Cataclysm who had defeated a terrorist consumed by revenge.

Whether I could kill him or not, attacking him here would be enough to get me branded a public enemy—even if this were Murim rather than the modern world.

And that was probably…

*Exactly the situation he wanted most.*

Cheon Taemin, the beginning and the end of Ares Guild, had already been unconscious for a long time.

What if something happened to me at a time like this?

*Even if I killed him here, I couldn’t take responsibility for everything that came afterward.*

The greatest enemy stood right before my eyes, but there were unseen enemies as well.

When my thoughts reached that point, both my head and my heart cooled.

*Hssss.*

As the aura that had swelled as though it might explode at any moment subsided, Michael Silbert let out a small sigh.

“What a shame. You looked much better when you were full of youthful fire.”

“Shut up. I’ll tear your mouth apart.”

“If my mouth were that easy to tear apart, someone else would have done it hundreds of times already. But do you know something?”

He continued with a faint smile.

“One day, I suddenly realized that the people who had said things similar to you had vanished without a trace. You see, I knew a method more certain than tearing their mouths apart.”

“……!”

“So be grateful today that you have good friends. The fact that those friends are highly capable is also a great stroke of luck for you. Isn’t it?”

His voice was directed at me, but his gaze was not.

The way he stared past my shoulder with that strange look woke my dulled sense of danger.

*The Skeleton King.*

He had already undergone a clean change of identity through Magic Johnson and was working as a Hunter affiliated with Peace Guild.

But if he attracted unnecessary attention, it would cause problems.

Michael Silbert was that difficult an opponent. The moment a weakness appeared, he would pounce without mercy and tear into it.

*Should I have left him behind?*

But the thought had barely crossed my mind when Michael’s attention quickly shifted elsewhere.

“So you’re the young Vice Guild Master of Ares Guild I’ve heard about. How is your maternal grandfather?”

Team Leader Choi replied in a voice cold as ice.

“He is doing well. Though I cannot say how he will react when he hears the news about the Paris branch.”

“I regret that things turned out this way too. I personally respect your grandfather as well. So please put in a good word for me.”

“That is exactly what I intend to do. I will tell him precisely what I saw and heard.”

There was not a trace of hesitation in his answer.

And as Michael Silbert gazed at Team Leader Choi—

*Whoosh! Whoosh!*

A group came rushing across the ruins with the sound of air being split apart.

At the head of them was Huginn, the messenger who had visited Ares Guild only a short while ago.

He glanced at us, then ran straight to his master and bowed his head.

“Guild Master, everything is ready.”

“Start with the casualty count.”

“There are approximately three hundred casualties. Forty-five survivors have been rescued.”

“That is enough to know for now. Have many people gathered?”

“Not only the nearby citizens. Every reporter in Paris is waiting for you.”

“Faster than I expected.”

“We were fortunate. The international press was already watching closely because of the release of the new Mana Cultivation Method.”

“What about the CCTV?”

“We secured it immediately. It recorded everything from beginning to end. The terrorist carrying out a suicide attack with unrefined Magic Gems and bombs, all the way to our Odin Guild suppressing the Monster Wave.”

At first, I did not understand.

I did not know what Huginn meant by “ready.”

But as I listened to the two men exchange words, my mind began to freeze over.

*This is…*

Meticulous.

The release of a new Mana Cultivation Method.

The assault on the Paris branch and the Monster Wave, carried out by a Middle Eastern terrorist consumed by revenge.

And a press conference with every eye focused on it.

It was as though dozens of large and small gears had meshed together without the slightest error. They were moving according to an intricately designed plan.

That was also why they could continue speaking so openly in front of me and my companions.

They knew there was no way to stop gears that had already begun turning.

Even if we shouted the truth for three days and three nights in front of the countless cameras camped out in the distance, no one would believe us anyway.

But the bigger problem was that those madmen’s assessment was undeniably true.

A reality that could never be solved through force alone.

“I’m sorry, but I should be going now. There are a lot of people waiting for me.”

Michael Silbert acknowledged me, Team Leader Choi, and finally the Skeleton King with a glance before slowly turning away.

Then he suddenly stopped and added one more thing.

“You’ll be very busy from now on. Much busier than you think.”

*Grind.*

I watched his back recede and clenched my fists with all my strength.

But in the end, I could not swing.

Not long afterward, I understood the meaning of his final words.

*Ding.*

> **System**
>
> A sudden Quest, **Chain of Terror Attacks**, has been generated!
>
> You cannot choose whether to accept this Quest. The System will force the Quest to proceed!

It was January, before the joy of the New Year had even faded.

Winter was dyed red.

* * *

“It has begun.”

At Huginn’s low voice beside his ear, Michael Silbert calmly asked:

“Where this time?”

“London.”

“The old king will be furious.”

“Buckingham Palace should be fine. London Bridge will collapse instead.”

Michael let out a quiet laugh at his subordinate’s dry joke.

“Once London is dealt with… eight will remain.”

“Yes.”

There were ten people in total whom Huginn had brought back from the desert.

Each one was both an insane fanatic and a seasoned Hunter. They would carry out their missions without a single problem.

The bombs they detonated would bring buildings crashing down, and the unrefined Magic Gems would be enough to shatter the people’s hope.

*And our Odin Guild will piece that shattered hope back together.*

Everything was already prepared.

This was a position he had reached after countless sacrifices and efforts.

He could tolerate neither a single mistake nor failure.

As Michael heard the cheers of the citizens and saw the reporters drawing closer, he hid his smile behind a grief-stricken expression.

[^1]: A classical expression meaning to use someone else as the weapon for killing one’s enemy.
## Chapter artifact 738

# Chapter 738

There was a strange magic in the words *New Year*.

The excitement of beginning another year. The vague hope that everything would be better than it had been the year before.

But one day in January, before people had even turned the first page of their new calendars, that excitement and hope collapsed in an instant.

—This is an emergency news bulletin. Following the news from Paris that we reported only an hour ago, a second Monster Wave has occurred in London, United Kingdom. Central London is currently engulfed in extreme chaos, and King Philip II of the United Kingdom is…

—Another emergency bulletin! A Monster Wave has occurred once again in Mumbai, India! This is the third Monster Wave to occur in a single day, an unprecedented event since the Great Cataclysm…

—Oh my God. Are you all seeing this? The symbol of Rio de Janeiro, the Christ the Redeemer statue—Cristo Redentor—is collapsing!

It was the beginning of a catastrophe.

First, France’s Luxembourg Gardens were stained with blood. Then London Bridge, which had stood through a long and storied history, collapsed. And Brazil’s colossal statue of Jesus, weighing over six hundred tons, toppled over, crushing buildings and people beneath it.

*Rumble, rumble, rumble!*

The ground shook with a deafening roar.

Those barely managing to keep their balance were met by the sound of something crying out beyond the flames that erupted with the explosion.

—Grrr…

Monster Waves.

True to the name that had become synonymous with disaster, legions of monsters tore through space and appeared, sweeping in every direction like a wave.

—Kraaaargh!

“M-Monsters!”

“Run!”

“Aaaah!”

The forest of skyscrapers built by dazzling civilization filled with screams.

Some people fled. Some were seized by monsters, torn apart, and killed. Others raised shining weapons and fought against creatures that did not belong to this world.

“Formation! Don’t retreat!”

“Ranged units, fire!”

*Boom! Boom! KABOOM!*

Humans and monsters. Monsters and humans.

The two species, incapable of coexisting from the very beginning, charged at one another. And the flames that had begun in Paris, France, spread to every corner of the world.



[Red Square in Moscow stained with blood by monsters]

[Disaster strikes China once again—the Forbidden City engulfed in flames]

[Five Monster Waves in a single day. Upon hearing the news, Pope Urban VIII says, “O God.”]

[The sixth Monster Wave occurs in New York. Wall Street plunged into shock.]

[Tokyo Tower seized by flying monsters. Crashed Air Self-Defense Force aircraft cause secondary damage.]

[Odin Guild Master Michael Silbert rapidly suppresses the first Monster Wave. Releases CCTV footage obtained in Paris: “This is not a simple disaster. It is undoubtedly a terrorist attack with a purpose.”]



Metropolises inhabited by at least several million—or even more than ten million—people were thrown into chaos.

People watching the shocking news reports one after another on their televisions and smartphones were left speechless.

*Disaster.*

It was the only word that could explain everything happening now.

At the same time, the fear spreading like a plague paralyzed people’s reason.

“Hello? You saw the news, right? I’m going to pick you up at school right now, so…”

“Hey, what are you doing?”

“What does it look like? I’m packing.”

“You idiot, there’s still a long time before you get off work. What are you talking about?”

“Fuck, is that what matters right now? I need to take care of my family first.”

“Hey, hey! Section Chief Kim!”

Monster Waves were like natural disasters that no one could predict, and people abandoned whatever they were doing and moved about like they had lost their souls.

Toward the homes where their families were waiting. Or toward emergency shelters where their chances of survival might be even slightly higher.

As if to attest to the empty offices, most work and road traffic had ground to a halt, and the people crowding into the subways could not bring themselves to put down their smartphones.

What weighed them down now was an extreme fear and anxiety they could not see.

The fear that a Monster Wave might occur right there at any moment. The anxiety that they—or someone precious to them—might lose their life because of it.

*Wheeeeeeeen.*

—Temporary state of emergency. This is a temporary state of emergency. Residents living nearby are advised to prepare for any eventuality and proceed to an emergency shelter…

States of emergency were declared simultaneously in countries around the world.

Warning sirens rang through the streets without pause, while soldiers armed with all kinds of heavy weapons and Hunters summoned in an emergency waited for instructions from their governments, tense-faced.

Until the sun—or moon—hanging overhead disappeared according to each country’s time zone.

Until, after a long wait, the governments issued new announcements.

—The temporary state of emergency is hereby lifted.

It had been only twenty-four hours since the first Monster Wave occurred in Paris, France. The disaster of that day, which had seemed as though it might continue until the world ended, finally came to a close with Cairo, Egypt.

Leaving behind the unprecedented and horrifying record of ten Monster Waves in a single day.

And the hero who had successfully stopped five of those Monster Waves stepped before countless cameras.

“From this day forward, Odin Guild will continue to fulfill its duty by becoming your sword and shield.”

Michael Silbert.

As people watched him shed hot tears while mourning the souls of the fallen, they cried along with him.

Everyone cheered for the hero who had saved countless people, and for Odin Guild.

No—not everyone.



* * *



*Bang!*

With a deafening roar, more than a dozen holographic televisions crumbled into dust.

I stared at the empty air where a man’s face had appeared only moments ago. Then I suddenly opened my mouth.

“Should I apologize?”

Team Leader Choi, sitting on the nearest sofa, shook his head.

“It’s fine. If you hadn’t stepped in, I would have smashed them myself.”

That was no exaggeration or empty courtesy.

I looked at Team Leader Choi’s tightly clenched fist. Blood was slowly dripping from his whitened knuckles.

Along with the green monster blood he had not yet managed to wipe away.

*Drip. Drip.*

The white wool carpet was gradually becoming stained red and green, but no one in the room cared.

Everything around us simply felt cold and empty.

*We got played. And perfectly.*

Ten.

Out of ten Monster Waves—ten of them—we had failed to stop even one. No, perhaps it would be more accurate to say that we had been unable to stop them.

*Because they had been planned from the start.*

It was impossible to stop Monster Waves occurring in major cities thousands, or even tens of thousands, of kilometers apart.

The situation would not have changed even if Magic Johnson had been with us.

The Monster Waves that occurred today had been planned terrorist attacks from beginning to end—bombs detonating without regard for either time or place.

And when we finally heard the news and arrived, what awaited us were more ruins and corpses.

There was only one slight difference between the Monster Wave in Paris and the ones that followed: the locations where the later Monster Waves occurred.

*Their targets weren’t Ares Guild’s overseas branches.*

The terrorists who had joined hands with Michael Silbert had headed for all kinds of places. Tourist attractions crowded with people. The headquarters of major corporations recognizable by name alone.

But the most frequently targeted sites of all had been the branches of major Guilds like Ares.

“Why?”

At my abrupt question, Team Leader Choi raised his head. I added one word.

“Targets.”

That was explanation enough.

Team Leader Choi stared into empty space with hollow eyes, then suddenly opened his mouth.

“Isolation.”

“Isolation?”

“Yes. Isolating Ares Guild. That must be Michael Silbert’s objective.”

“But why do it like the Paris branch…?”

I stopped before I could finish.

Various thoughts raced through my tangled mind like threads being unwound. Somewhere among them was an answer I had failed to see.

*A Middle Eastern terrorist organization.*

The mission of the men who had joined hands with Michael Silbert was not over yet.

The final strike that would bring this horrific day to a close—the keen, ice-cold blade that would isolate Ares Guild from the entire world—was rushing toward us.

Perhaps even now.



* * *



*Step. Step.*

The sound of footsteps echoing through the darkness was unusually loud.

I could not tell whether it was because there were several dozen people, or because the space they were crossing was a dark cave. But one thing was certain.

This was a place no one knew about and no one could reach.

*Step.*

The footsteps that had seemed destined to continue forever came to a simultaneous halt.

Something rippled in the pitch-black darkness.

“Inshallah.”

At the single word that sounded as though it had been whispered directly into their ears, several dozen people dropped to their knees and prostrated themselves.

Then they opened their mouths and answered in unison.

“Inshallah.”

God willing.

It was an incantation that bound them together and a prayer that reminded them of God’s greatness. And the silhouette wavering beyond the darkness finally revealed itself.

*Swish.*

A long robe brushed against the ground.

The people bowed their heads even lower and murmured with one voice.

“This lowly servant of Allah humbly greets the great Prophet.”

*The Prophet.*

That title, used for a being whose face they did not even dare properly meet, occupied a sacred and inviolable place among them.

“Raise your heads.”

At the mysterious voice whose gender and age could not be discerned, the people trembled.

Then, pressing their faces into the ground, they answered.

“How could these lowly servants dare to face the great Prophet?”

“Please withdraw your command.”

*Whoosh.*

A single gust of wind blew in from somewhere and enveloped them.

Then the Prophet’s voice, mingled with the wind, reached their ears.

“What became of them?”

No one had any doubt whom the Prophet meant by *them*.

The old man prostrated at the very front opened his mouth.

“They completed the missions entrusted to them and returned to the embrace of God.”

The Prophet gave a slight nod.

“Inshallah. It was only right that they should.”

“Inshallah.”

Ten warriors had crossed the desert and scattered across the five oceans and six continents. As warriors of God, they had completed their missions and returned to the embrace of God.

And now it was time to collect the blood price.

The Prophet spoke in a mysterious voice.

“Let the whole world know what brought about all this disaster.”
## Chapter artifact 739

# Chapter 739

Ten Monster Waves in a single day were more than enough to plunge the entire world into shock and terror.

What made it worse was that the attacks had occurred in capitals or major cities whose names were known around the world.

Several major Guilds, led by Odin Guild, had swiftly suppressed the Monster Waves, but the resulting damage was immense.

It was a horrific catastrophe. The confirmed death toll alone had already reached several thousand.

People kept their senses on high alert in their homes or emergency shelters, and Michael Silbert did not miss the opportunity to seize the attention of the entire world.

“This is footage Odin Guild obtained when the first Monster Wave occurred in Paris.”

And when people finally saw the CCTV footage that had been released, they were once again thrown into shock.

> **Odin Guild Master Michael Silbert: “Before this was a Monster Wave, it was a meticulously planned terrorist attack.”**

> **Not a natural disaster, but a man-made one**

> **A calamity born of malice**

> **Ten killers armed with bombs and Magic Gems. Who are the suicide terrorists shown in the released CCTV footage?**

> **Following expert analysis of the CCTV footage: “Each of them possessed several unrefined A-rank Magic Gems, and they carried out the attacks by targeting areas near Gates with high mana concentrations.”**

> **The world shudders at a horrifying déjà vu: “Remember what happened in South Korea.”**

> **Bringing in bombs and unrefined A-rank Magic Gems was an obvious violation of international law**

> **The bombs and Magic Gems came from Africa and the Middle East**

Countless news reports poured in from every direction.

Once it became clear that the Monster Waves had not been unstoppable natural disasters but tragedies caused by terrorism, people were consumed by anger and emptiness, and the internet reached saturation point.

> Nothing to say. These guys are seriously insane.

>> Are they really crazy fuckers?

> The truth must be revealed to the whole world. Every last one of them must be hanged.

> I was reading a foreign article, and it kept mentioning South Korea. Is it talking about the Go Jun incident from a little while ago?

>> Yeah, that’s right. And because of that, the people who hate Korea are foaming at the mouth and shouting that Korea is the root of all evil.

>> What the fuck? This is ridiculous. They wouldn’t even be alive if it weren’t for Cheon Taemin in the first place.

>> But which country’s people are going around saying such bullshit?

>> Jjajang. Wasabi.[^1]

>> Oh.

>> I can understand Japan, since they’ve always been like that, but why are those Chinese bastards doing it? Have they already forgotten that Lord Fuck helped them?

>> “China.”

>> That one word says everything.

>> Still, maybe because China received help from him before, it’s definitely much less extreme than Japan. There are even people tracking the IQs of those who curse Lord Fuck in the comments and teaching them a lesson.

>> I’m IQ 110. Can you track my location with that?

>> I don’t know about anything else, but I have seen people bashing Korea on foreign forums too. Cheon Taemin and Jin Taekyung worked hard to raise Korea’s standing, but that dead bastard Go Jun ruined it all.

>> Jin Taekyung raised Korea’s standing? Are you sure? You wouldn’t know it from the fact that he hasn’t shown his face at all today, lololololol.

>> Your Air Self-Defense Force hasn’t shown its face since getting beaten up by a Wyvern, either. Though I did get a good look at Tokyo Tower collapsing.

>> Welcome, wasabi.

>> Does Lord Fuck have ten bodies, you Japanese bastard? Watch some TV. Taekyung ran himself ragged today. He was a step late, but seeing him try to save even one person somehow really moved me.

>> So criticizing Korea automatically makes someone Japanese now, lol? Unfortunately, I’m Korean.

>> Take the W key off your keyboard if you want to keep pretending to be Korean;;

[^1]: Food-based shorthand used here as derogatory references to Chinese and Japanese people.

There was no point paying attention to trolls. The most important thing now was finding out who the terrorists belonged to and why they had committed such acts.

> The terrorists are all from the Arab world, so it’s obvious. It has to be either Al Qaeda or IS.

>> If it’s so obvious, why are the affected countries still delaying a joint statement or official announcement? This absolutely needs to be verified. Al Qaeda and IS have both suffered serious losses recently.

>> I agree with the comment above. A few weeks ago, their main bases were completely wrecked and their leader was killed and replaced.

No one was unaware of the bloodbath that had swept through the Middle East and Africa.

A mysterious group of vigilantes whose faces, names, and even genders were unknown.

They had beheaded the leaders of the terrorist and rebel groups, and the two factions, suddenly deprived of their leadership, suffered enormous losses in the fierce internal struggles that followed and were forced to raise the white flag.

> Doesn’t that make it even more obvious? They may have been weakened, but if they lost their leader, they could easily have carried out terrorist attacks around the world in the name of revenge.

>> There are probably a lot of elementary school kids here who don’t know this, but when the United States got seriously pissed off during the 9/11 attacks, Hussein got scared and denied that it was them. A little while ago, they practically surrendered and begged people to stop, saying they wouldn’t commit any more terrorist attacks. But this terrorist attack involved ten countries, including the United States. Do you really think that makes sense?

>> No matter how crazy they are, that’s impossible. Besides, I heard the current leaders of the Middle Eastern terrorist groups belong to the moderate faction.

>> What the hell is going on?

This was not a question held only by Korean netizens. News sites and online communities around the world were heated by fierce arguments for and against.

And before long, the answer to that question was broadcast across the world in a single video.

—I declare in the name of the Prophet.

Beneath dim lighting stood an unidentified figure with a robe pulled deeply over their head.

In the grainy footage, the figure called themself the Prophet and pointed to the two heads placed in front of them before continuing.

—I will erase the apostates who abandoned their convictions for the sake of their own safety from this sacred land, and establish rightful vengeance and justice throughout the world.

It was not difficult for people to recognize the owners of the heads.

They were the leaders of the most dangerous terrorist organizations in the world, and only a short while ago, they had announced a humiliating surrender.

IS.

And Al Qaeda.

Before the horribly beheaded former leaders, the Prophet slowly parted their lips.

—As long as God is with us, we will not stop. Beginning today, we will judge and punish you.

“……!”

“……!”

The people watching the video caught their breath without realizing it.

Judgment.

Today’s horrific tragedy was only the beginning.

Those who widened their eyes as if they could not believe it nevertheless realized instinctively.

The unidentified figure who called themself the Prophet was not making empty threats.

Even now, they could detonate a bomb somewhere in the world and bring about another disaster.

And then.

The Prophet’s final words pierced the ears of the frozen audience.

—Inshallah. Know that all of this began with you.

*Crackle.*

The short video ended amid a burst of harsh static.

No—just when everyone thought it had ended, another screen began transmitting.

It was a dark night in which even the moonlight was hazy.

A lone figure standing in a desert filled with blood and corpses suddenly raised their head. The face glimpsed through the mask resembled someone everyone knew.

* * *

The Skeleton King crossed an empty corridor.

Holding a silver tray in one hand, he kept his gaze fixed on the smartphone in the other.

> **Seven Days Stained with Blood**

> **Monster Wave in Madrid, Spain. Terrorism Again?**

> **The Notorious Terrorist Who Vanished Like a Ghost: “The Prophet”**

> **Video Analysis Shows a 99.99% Match. Another Identity of a Young Hero**

> **Joguk Ilbo Chief Editorial Writer Lee Kanghee: “A Tragedy Born of Pointless Heroism”**

> **Public Opinion on a Knife-Edge: A Criminal Intoxicated by Heroism, or a Vigilante of Darkness?**

“……Damn humans.”

The Skeleton King muttered a curse without realizing it.

Even from the brief glance he had taken, the state of the online news pages was a complete mess.

The front page was filled with nothing but openly condemnatory articles and sensational headlines, while fierce battles between netizens raged beneath them.

> Lol, look at the level of these garbage reporters’ headlines.

>> For real. They’re desperate to increase their views. The articles say nothing and are all stitched together from scraps.

>> But if you only look at the headline, it isn’t entirely wrong, is it?

>> Honestly, I like Lord Fuck too, but I think he really did act rashly this time.

> This deserves criticism. There’s nothing he can say for himself.

>> What do you mean, there’s nothing he can say? A few weeks ago, when he completely wrecked Al Qaeda and the others, you were all cheering. Whoever he was, you said it felt great to see him wipe those bastards out.

>> That doesn’t mean what he did was right.

>> So it was fine then but not now? You’re fucking crazy, lol.

>> The situation has changed. Seriously, how many people are dead now? Nationalist hype and personal fandom are all well and good, but look at how serious the situation has become because of what Jin Taekyung did.

> I knew that bastard Jin Taekyung would cause trouble. I hated watching him get full of himself from the moment people started hyping him up as a young hero and the next Cheon Taemin.

>> That’s complete bullshit. When was he ever full of himself? Even when the media was hyping him nonstop, hyung still walked around in a tracksuit.

> Putting it neutrally, I personally just think it’s unfortunate. Do you really think Jin Taekyung did that because he was some bloodthirsty killer?

>> Then why did he do it?

>> Look at the timing. It was right before the Mana Cultivation Method was released. Seriously, do you think there are only one or two Awakened among the Middle Eastern terrorists and African rebel groups? Who was supposed to deal with them if they learned the Mana Cultivation Method and started committing every kind of crime, including terrorism?

>> That still doesn’t justify murder.

>> Fine, you’re right. But let’s be precise. Everyone justified it back then. Now that one unbelievably insane bastard has appeared, you’re all switching sides at the speed of light.

>> At the time, people both at home and abroad were universally praising the vigilantes. “Whoever you are, great job. Let’s not bother finding out who they are.” That was the atmosphere, and now it has completely reversed.

> There are a lot of Jin Taekyung fanboys here, lol. That doesn’t change the fact that he’s being condemned around the world.

>> The fact is, polls show that more people support Lord Fuck. It only looks otherwise because sensational headlines are being mass-produced.

> What I don’t understand is Cheon Taemin. Even now, he hasn’t shown his face once. Jin Taekyung has been missing for several days too.

>> He caused trouble and is pretending it has nothing to do with him. Seriously disgusting, lol. Just look at Odin Guild. King-God Michael is the past and the future.

As he read through the comments beneath the online articles, the Skeleton King suddenly wondered:

*If they learned the truth, what kind of expressions would the humans who posted those comments make?*

But the Skeleton King knew that it was all a pointless thought.

At least for now, there was no way to reveal the truth. On the contrary, they might be completely sunk by the backlash.

The society of humans he had experienced so far was far more complicated and frustrating than he had expected.

*Stupid humans.*

The Skeleton King shook his head and stopped in front of a massive door.

When he discovered that the silver tray he had brought yesterday was still sitting there, he let out a deep sigh and carefully pulled on the doorknob.

*Click.*

Beyond the slowly opening door, he saw the back of someone sitting cross-legged.

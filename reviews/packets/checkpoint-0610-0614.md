# Checkpoint Review — 610–614

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

# Chapters 610–614

## Plot

Jin Taekyung and his allies dismantle Al-Qaeda and other terrorist networks across the Middle East and Africa. He defeats Al-Qaeda leader Al Diab Jawahiri and leaves him in the Skeleton King’s custody, while Choi and Magic Johnson investigate Al-Qaeda’s long-running Magic Gem laboratory. The discovery of advanced weapons, artifacts, medical equipment, and American military cigars suggests that the terrorists have an undisclosed supplier or smuggling connection. Their campaign creates enough fear to force Middle Eastern terrorist groups and Afghan rebels to promise restraint, though Taekyung expects this to be temporary.

Taekyung briefly returns to the modern world, reunites with his old friend Jin-ho, and realizes that he came home partly for emotional support rather than merely to retrieve the game capsule. He returns to the Murim after completing a stable cultivation technique designed for even low-rank Hunters. He entrusts the technique and a letter for Choi Minwoo to the Skeleton King, who encounters Minwoo grieving at Kim Hwajong’s grave but delays delivering them.

After more than a month away, Taekyung returns to Mount Daebyeol and takes charge of the Fire Dragon Pavilion’s Nanman expedition. Meanwhile, the Lord of Heaven awakens after 136 days, empowers Blood Lord and Dark Heaven’s other servants, orders messages sent to South Heaven and North Heaven, and declares that the Great War has begun.

## Continuity

- Jin Taekyung has returned to the Murim and is leading the Fire Dragon Pavilion’s Nanman expedition from Mount Daebyeol.
- The expedition party includes Hyuk Mujin, Ju Hwaran, Song Ilseom, and Taishan.
- The Lord of Heaven has awakened, empowered Dark Heaven’s servants, and announced the beginning of the Great War.
- South Heaven and North Heaven are powers Dark Heaven intends to notify about the Great War.
- Blood Lord still seeks revenge against Jin Taekyung and the Sword Saint after the Shaolin Bloodshed.
- Al Diab Jawahiri remains in the Skeleton King’s custody; the ultimate fate of Al Diab and the other terrorists is unresolved.
- Al-Qaeda operated a large Magic Gem research laboratory for at least ten years. Its advanced supplies and American military goods imply support from an unidentified military, political, or smuggling network.
- The results of Al-Qaeda’s Magic Gem experiments remain unknown.
- The masked campaign has weakened terrorist leadership and prompted public promises of restraint from Middle Eastern terrorist groups and Afghan rebels, but their submission may not last.
- Jin-ho knows or strongly suspects Taekyung’s connection to the five masked figures and has agreed to keep it secret.
- Taekyung has completed an unnamed cultivation technique intended to be broadly teachable without making it easy for evildoers to abuse.
- The Skeleton King holds Taekyung’s completed martial art and letter for Choi Minwoo but has not yet delivered them.
- Choi Minwoo is Guild Master of the Peace Guild and Vice Guild Master of Ares Guild. He is grieving Kim Hwajong, his grandfather and former butler, and has not yet received Taekyung’s package.

## Translation Decisions

- Use **Al Diab Jawahiri**, **Al-Qaeda**, **Magic Gem**, **Magic Gem laboratory**, **Grand War**, **Lord of Heaven**, **Dark Heaven**, **South Heaven**, and **North Heaven** consistently.
- Render **심마** as **heart demon**, **심법** as **cultivation technique**, and **무공** as **martial arts**.
- Use **Fire Dragon Pavilion**, **Nanman expedition**, **Mount Daebyeol**, **Skeleton King**, **Blood Lord**, and **Sword Saint**.
- Render **천마군림보** as **Heavenly Demon Reign Step**.
- Render **천상천하** as **Heaven above, earth below** and **만마앙복** as **All demons bow in submission**.
- Preserve **Jin-ho hyung**, **Crazy Korean**, and the Skeleton King’s address **devious human** where applicable.

## Durable state

{
  "active_continuity": [
    "Jin Taekyung has returned to the Murim and is leading the Fire Dragon Pavilion's Nanman expedition from Mount Daebyeol.",
    "The Fire Dragon Pavilion's current expedition party includes Hyuk Mujin, Ju Hwaran, Song Ilseom, and Taishan.",
    "Jin Taekyung has completed an unnamed cultivation technique intended for even the lowest-rank Hunter to learn without making it easily abusable.",
    "Jin Taekyung has entrusted the Skeleton King with the completed martial art and a letter for Choi Minwoo.",
    "Choi Minwoo is serving as Guild Master of the Peace Guild and Vice Guild Master of Ares Guild while grieving his grandfather Kim Hwajong.",
    "Al Diab Jawahiri, the leader of Al-Qaeda, remains in the Skeleton King's custody.",
    "The Skeleton King is an undead named monster who has fought alongside Jin Taekyung and is accepted by Chuck Hagel as an ally.",
    "Al-Qaeda possesses a large Magic Gem research laboratory that appears to have operated for at least ten years.",
    "Restricted supplies found among the terrorists indicate support from established military, political, or smuggling networks.",
    "Jin-ho has inferred Jin Taekyung's involvement in the masked group's campaign and agreed to keep it secret.",
    "The masked group's campaign has destroyed terrorist leadership and headquarters, prompting Middle Eastern terrorist groups and Afghan rebels to promise restraint.",
    "The Lord of Heaven has awakened, empowered Dark Heaven's servants, and declared that the Great War is beginning."
  ],
  "continuity_sources": [
    614,
    613
  ],
  "open_questions": [
    "Who supplied Al-Qaeda with the restricted equipment, weapons, artifacts, and military goods?",
    "What results, if any, did Al-Qaeda obtain from its long-running Magic Gem experiments?",
    "What fate will the Skeleton King ultimately assign to Al Diab and the remaining terrorists?",
    "Will the terrorist groups' apparent surrender and restraint last beyond the immediate pressure of the masked group's campaign?",
    "How will Choi Minwoo respond after receiving Jin Taekyung's martial art and letter?"
  ],
  "safe_through": 614,
  "temporary_decisions": [
    "Use Al Diab Jawahiri as the full English rendering of 알 디아브 자와히리.",
    "Retain Crazy Korean as Chuck Hagel's address for the masked protagonist.",
    "Preserve Jin-ho hyung as Jin-ho's familiar address.",
    "Render 심마 as heart demon, 심법 as cultivation technique, and 무공 as martial arts.",
    "Keep Magic Gem laboratory for 마정석 관련 비밀 실험실."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 610

# Chapter 610

While dealing with armed terrorist groups and rebel forces in the Middle East, I came to realize two things.

First, there was no end to human malice.

Second, this horrendous treadmill kept turning without pause.

There were just too many bad people in this world.

They were weeds, plain and simple—viruses found everywhere on Earth.

No matter how many you pulled out, more would grow somewhere else and make the world sick.

In the end, there was no way to stop this damn treadmill forever.

*Still, one thing is certain.*

Even if I couldn’t stop the treadmill forever, I could at least break it for a while and bring it to a halt.

In that sense, the old man sitting in front of me was one of the biggest components keeping that massive treadmill turning.

“Hey there. Young man in the bizarre mask.”

After casually tossing out a single sentence in a composed voice, the old man stroked the teacup in his wrinkled hand. A strange scent drifted from it.

“Finding me was impressive, but… the world doesn’t change that easily.”

The old man, whose name—Al Diab Jawahiri—was as long as any other Arab’s, remained calm even as thunderous noises echoed outside and an unwelcome guest suddenly barged in.

*He’s clearly nothing more than a powerless old man.*

I didn’t know whether that remarkable composure came from more than a century of experience, or from the fact that he was the leader of Al-Qaeda, a colossal terrorist organization that divided control of the Middle East with ISIS.

What mattered was that he was wrong.

“It changes. Just like people change, the world will change someday, too.”

“Do you know how many Muslims bow before mighty Allah?”

“No. Other than the fact that one of them is sitting in front of me.”

“They say it’s twenty-five percent. Twenty-five percent of the entire world. That’s over a billion people when you count heads.”

Al Diab smiled faintly and continued.

“You’re fighting more than a billion Muslims. You’ve made mighty Allah and His servants your enemies.”

I wasn’t the kind of person who would be shaken by the ramblings of a crazy old man. I smiled back at Al Diab and answered.

“Not Muslims. Terrorists like you.”

“I won’t deny that some of them still do not sympathize with us. It is a truly regrettable thing. But in the end, we are brothers. Bound together in the name of Allah, we will eventually gather beneath a single flag.”

“So the people you call brothers have spent centuries beating the hell out of each other after splitting into Shiites and Sunnis?”

Al Diab answered my rebuttal without the slightest change in expression.

“There is nothing strange about that. Husbands and wives. Brothers and sisters. Even within a single household, endless conflicts take place.”

“That’s because your family’s a complete mess. Mine isn’t.”

“What can one do? It is a conflict passed down from our ancestors. It, too, is merely a small dispute born from trivial misunderstandings and differences of opinion—a process by which we will ultimately become one.”

Al Diab didn’t understand.

No, he didn’t even want to understand—not by the tiniest amount.

He didn’t understand how much suffering innocent people had endured because of those trivial misunderstandings and conflicts, and that hollow word *unity*.

Or how many countless people would suffer in the future.

*Monster.*

The ancient old man before me was a monster, too. A monster trapped by twisted beliefs and stubborn conviction.

The next moment, I felt a chill when I saw the bright smile spreading across his face.

“How about it, misguided young man? Why not stop these foolish acts and join me?”

“……!”

“Your eyes are wavering. Your heart is shaken. Do not suffer while trapped by countless afflictions. Enter the warm embrace of Allah.”

Along with his utterly peaceful voice, the old man’s deeply wrinkled hand slowly reached toward me.

I watched him with a faint tremor in my eyes, then let out a small sigh.

“Has living too long driven you senile, old man…? Where the hell do you get off trying that shit on me?”

“……!”

Shock appeared in the old man’s eyes.

“If you get caught playing around, you pay in blood. Pick one. Your neck or your wrist.”

At that moment, our gazes collided with a hard jolt.

*Shk! Bang!*

Everything happened in an instant.

The slender old man’s wrist shot into the air, severed by the short sword I swung at the speed of a ray of light. At the same time, a bullet fired from a special firearm hidden deep inside his dark, voluminous sleeve pierced somewhere beyond my shoulder.

In short, I dodged, and he didn’t.

“Aaaaaaargh!”

That old man had quite a set of lungs.

It was a booming scream, impossible to believe had come from a man well over a hundred years old.

Clutching his cleanly severed wrist, Al Diab collapsed onto the carpet.

And then… a group that moved even faster than he did appeared.

*Shishshishshishk!*

From the ceiling, the walls, and beneath the carpet-covered floor.

Like ghosts, they emerged, beams of light and gusts of wind swirling from their hands.

Front, back, left, right. They tightly surrounded me from all thirty-six directions and unleashed a terrifying assault.

But instead of dodging, I chose to attack.

*Inventory open. Equip Fire Dragon Armor.*

At the same time—

*Kakak! Ting-ting!*

The aura that tore through space struck the reddish armor and vanished, while blackened arrowheads bounced off helplessly.

Of course they did. Unless it was a concentration of energy called Force—or an aura blade—nothing could pierce the Fire Dragon Armor.

The men, who gave off the scent of Murim assassins regardless of who had trained them or how intensely, realized that fact immediately.

*Whoosh!*

There were no commands or exchanged glances.

The men wearing black turbans moved like machines with commands already programmed into them.

They gave up on targeting my upper body, which was protected by the Fire Dragon Armor, and aimed for the exposed areas, including my lower body.

But the Fire Dragon Armor was a divine weapon capable of changing the flow of battle.

If I encountered an opponent a level above me, it could let me match them for a while. If our skills were equal, it could give me an overwhelming advantage.

And if the opponent was far weaker than me?

What difference did it make?

Thirty men? Even if ten times that number came rushing at me, the ones who would fall would not be me.

It would be them.

“Come on in, you crow bastards.”

With that short taunt, I brought down the short sword in my hand.

*Whoosh!*

A single horizontal strike.

But that alone was enough.

*Kabooooom!*

Superheated air erupted along the blade, melting Magic and weapons alike. The space around me warped.

As the mighty power crouched within the sword stretched and woke, the underground hideout shook from top to bottom.

*Rumble-rumble-rumble!*

It wasn’t only the ground and ceiling that trembled.

Several pairs of eyes visible between the black turbans quivered faintly.

I didn’t know whether it was because their comrades had been caught in the short sword’s path and died without even managing to cry out, or because they had felt the unbelievable gap in power.

*Maybe it was both.*

But one thing was certain.

It was already too late for them to retreat.

“Not coming? Then I’ll go to you.”

The phrase *outnumbered and outmatched* had lost its meaning to me a long time ago.

I had occasionally fought dozens of people, sometimes hundreds, and rarely even thousands—and I had survived every time.

The battle about to unfold here was nothing more than an extension of all the battles that had come before.

*Shing!*

A blade suddenly shot up from the ground and grazed my chin.

The patient one had never revealed himself, even while his comrades appeared one after another. But his attack had failed, and the price was death.

*Crack!*

I unleashed a grappling technique at lightning speed.

Before the man who had performed the bizarre feat of rotating his neck several times could collapse, I thrust out one hand.

*Shishshik! Puk!*

Five streams of Finger Qi tore through the air. Some of the crows who had launched themselves forward by stepping off the ceiling and walls fell from above.

The others who rushed in while leaving behind their comrade, whose neck had been pierced clean through, met much the same fate.

*Fwoooooosh! Slash!*

Their One Strike carried desperate resolve.

But the gap between will and ability was vast and deep.

The corpse, split in two along with its sword by my short sword, fell like a kite with its string cut.

*Fwoosh! Boom!*

I struck a palm toward the blood spraying through the air.

The blood evaporated in the terrible heat. Beyond it, another attacker flying toward me was knocked away even faster and slammed into the wall.

*Boom!*

The impact shook the space around us.

But even if it wasn’t merely the space that flipped upside down, but the whole world, their attacks would not stop.

*Whoosh!*

Neck. Calf. Hand.

Three sharp whistles rang out at once as they aimed for separate targets.

Instead of dodging, I took a step forward and swung the short sword in my hand.

No.

I sent it flying.

*Fwoooooosh! Crunch!*

No one could survive with a Force-infused sword embedded in their heart.

The hilt slipped from the hand of its owner, who had met death in an instant.

I reached toward the two blades that had already come within arm’s length.

*Grab!*

Aura was an extremely sharp and destructive concentration of energy, but cutting through bare hands covered in Force was another matter entirely.

I applied strength with both hands gripping the blades.

*Grnk. Crack!*

“……!”

“……!”

Two broken swords.

Two pairs of eyes with exclamation marks practically floating in them.

I bade them farewell in an emotionless voice.

“Go.”

“W-Wait…!”

“Oh, take this with you, too.”

Had these men ever given the people they killed enough time to say even a single last word?

They might have.

But I didn’t.

*Puk!*

“Guh!”

A bubbling death cry escaped them.

The light faded from the eyes of the men who had driven what had once been their own swords into their chests.

*Thud.*

The two bodies fell like rotten logs, and I looked around.

No enemies were rushing at me anymore. No sounds of attacks tearing through the air remained, and no more deaths followed.

Only one man was left, staring at me with eyes full of fear.

“Satan. You… you’re Satan.”

“Maybe I am. At least to people like you.”

Satan.

It was a word I had first heard from the deacon at my childhood church, but by now it felt almost as familiar as my own name.

I pulled the short sword from a corpse and approached Al Diab, muttering,

“What a joke. The people most like demons in the world are calling me Satan.”

“Y-You devilish bastard! Don’t come near me! Evil Satan! Demon! In God’s name, begone!”

“……I’ve heard that a lot on Line 1.[^1] I’m suddenly getting homesick for a place I’ve never even missed.”

I was briefly wondering whether Al Diab had studied in Korea when the iron door leading outside opened.

Beyond it, everything had gone quiet.

A Skeleton King covered in dust appeared.

“Vile human. Are you finished?”

“Yeah, I’m done. What about you?”

“I finished a little while ago and am preparing to start work. There are so many useful materials, and it is not exactly a bad deal for me, but… are you really certain this is all right?”

“What is?”

“They are human, just like you. Since they are your own kind, it might bother you to use them as my Skeleton army…”

“They’re not my kind. And this way, I can return to Korea with a clear conscience.”

I answered without hesitation, then introduced the Skeleton King to Al Diab, who had frozen with his eyes wide open.

“Oh. This one’s an actual demon.”

“……!”

*Fight barbarians with barbarians.*

Barbarians should be dealt with by barbarians. Terrorists should be dealt with by what used to be terrorists.

I jabbed the Skeleton King in the side and spoke to him.

“Hey. Do it.”

“……I don’t want to.”

“Come on, don’t be like that. Do it already.”

The Skeleton King, who had been wearing an unenthusiastic expression, gave Al Diab a thumbs-up and said,

“Don’t worry! The undead army will take care of those piece-of-shit terrorists!”

Oh, I couldn’t resist that. 

[^1]: Seoul Subway Line 1 is stereotypically associated with eccentric older passengers and their loud outbursts.
## Chapter artifact 611

# Chapter 611

“Allah! O great Allah!”

“Deal with him, Satan.”

“Farewell, vile human.”

I left Al Diab, who was screaming loud enough to split the heavens, in the Skeleton King’s hands and turned away. Whatever happened after that was no longer my concern.

If he had been the leader of some run-of-the-mill terrorist organization, there would have been nothing left to discuss—I would have executed him on the spot. But the leader of Al-Qaeda was another matter entirely. Magic Johnson or the Skeleton King would probably find a way to put him to good use. Whether through Magic or some kind of divine power.

*I should have learned the Soul-Seizing Technique.*

I felt a little regret.

The Soul-Seizing Technique, which bewitched and controlled people, was a martial art classified among the demonic, heterodox arts. But it wasn’t as if no one from the orthodox faction had ever learned it. The same went for the disguise technique, of course.

Of course, I hadn’t learned either one.

Not because I didn’t need them. I’d simply been too busy putting on one tearful shitshow after another just to survive.

*Now that I think about it, there is a practitioner of demonic, heterodox arts nearby…*

I wasn’t sure whether that guy had learned the Soul-Seizing Technique. If I got the chance, maybe I could learn a few techniques from him that might prove useful in the future.

While I was thinking about matters in the Murim, the enormous underground hideout, which resembled a giant anthill, finally came to an end. An endless sandy desert filled my field of vision.

Beneath the glittering stars, a man puffing thick clouds of cigar smoke opened his mouth in a rough voice.

“Already? That ended faster than I expected. You caught Al Diab, too?”

I looked over the bodies of the terrorists scattered around him and answered.

“Yes. I left him with the Skeleton King.”

“Allah’s faithful servant has fallen into the hands of a monster. Good. That damn old man. I would have liked to see his face.”

“He didn’t seem to like it very much. He’s probably still screaming and calling him Satan.”

Chuck Hagel gave a satisfied laugh at my answer.

Three days earlier, he had learned the Skeleton King’s true identity for the first time. In the short conversation that followed, he had proven that his way of thinking existed on an entirely different plane from that of ordinary people.

*Undead?*

*Yes.*

*Is that fellow’s surname Undead? If I didn’t hear wrong, I could have sworn you said Stone King earlier.*

*No. His gender is undead. No, not gender—species.*

*You said he was from Georgia.*

*Surprise. He was actually a Skeleton King from the Demon Realm.*

*Then he’s a monster.*

*Yes.*

*Hey, motherfucker. Are you kidding me? Why is a monster here…*

*To be precise, he’s an undead monster. More precisely, a named undead monster.*

*…Is everyone out of their minds? What the hell are you people doing?*

*He is a monster, but he saved my life from an Arch Lich during the Small Cataclysm.*

*What?*

*Oh. And he helped suppress more than ten Mutated Gates and three Gate Waves in Korea.*

*Holy shit. Then he’s a war veteran. Welcome, undead warrior.*

*Black cat or white cat.*

People said it didn’t matter whether a cat was black or white as long as it caught mice. Even so, Chuck Hagel’s way of thinking was truly extraordinary.

*My grandfather was a goddamn Indian-killer who even received medals. But I don’t give a fuck about that. If someone can deal with fucking terrorists and Gates and has the heart to devote themselves to helping people, what does skin color matter?*

*Chuck. He doesn’t have any skin.*

*Bone color doesn’t matter, either.*

My chest swelled at Chuck Hagel’s declaration of equality that transcended race and extended even across species.

He even showed an ambition I could hardly believe coming from the Secretary of Defense of the United States.

*I won’t tell the President.*

*Of course, I was hoping you’d do that, Chuck, but… are you really allowed to?*

*He didn’t ask.*

*Oh.*

*And that’s how the military works. If you don’t get caught, it’s fine. You write “military” and read it as “make-believe.”*

Of course, that was complete nonsense.

How could the Secretary of Defense of a country know about something like this and keep his mouth shut just because the President hadn’t asked?

And yet it was also the kind of insane thing only Chuck Hagel could do.

Uncle Chuck was, along with Magic Johnson, a symbol of the United States. The legendary war heroes born from the Great Cataclysm had been granted tremendous love and affection—along with an unspoken free pass.

*Even taking that into account, this is still crazy. Hm.*

Still, the fortunate thing was that Chuck Hagel had been a lunatic who committed that kind of insanity on a fairly regular basis.

With those thoughts in mind, I looked at Chuck Hagel warmly.

“What’s with that look?”

“I just really like you, Chuck.”

“Was that why you were so close to Johnson?”

“…That’s how you took it? Come to think of it, where are the other two?”

Team Leader Choi and Magic Johnson had been nowhere to be seen for some time.

Chuck Hagel gnawed on his cigar as he answered.

“They’re investigating the Gate. These bastards even had a secret laboratory for Magic Gem research.”

A secret laboratory.

I had expected as much to some degree.

A middling-sized terrorist organization might not have been able to manage it, but Al-Qaeda was a massive terrorist organization that carried out attacks throughout the world. They possessed enormous human and material resources.

It wasn’t particularly surprising that they had a Magic Gem laboratory, even though running one required astronomical amounts of money.

“How large is it?”

“Much larger than expected. According to Choi and Johnson, it looks like it was built at least ten years ago.”

“Ten years?”

“Yes. I don’t know whether they conducted other experiments here before this, or whether they were planning terrorist attacks using Magic Gems, as we feared… But it’s clear that they’ve been plotting something for quite a long time.”

“Hmm.”

It seemed that Go Jun had not been the first to come up with the idea of using Magic Gems to cause mass casualties.

That was only natural, considering that these people were a terrorist organization at their core.

“Did they achieve anything? Have they already discovered something?”

“Who knows? We’ll have to squeeze the terrorist researchers for answers. But if they’d achieved anything, I imagine an even bigger incident would already have happened.”

“That makes sense.”

“At the very least, the terrorist attacks that took place in Texas and elsewhere this time have little to do with Al-Qaeda. If it had been them, they would have already obtained data through human experimentation. They would have had no reason to put on such a stupid show of suicide.”

He was right.

It might have been a different story if the terrorist attacks had succeeded, but Al-Qaeda had no reason to waste valuable Hunters and Magic Gems on a suicide show that only proved how stupid they were.

It wasn’t as if they were making a banzai charge or carrying out a kamikaze attack.

*They would just attract a whole lot of attention and get beaten to a pulp.*

As I muttered to myself, Chuck Hagel suddenly opened his mouth.

“Lately, I’ve found myself thinking about something. Maybe it’s impossible to completely eradicate these bastards. Maybe that’s something we’ll never be able to do.”

He looked unusually drained today. The cigar he had been holding in his mouth was extended toward me.

“I don’t smoke.”

“I know that. What matters is that this goddamn American military cigar was in their possession.”

I muttered quietly.

“They have an insider helping them?”

“If it had only been the cigar, I wouldn’t have said anything. But… there was enough to fill a mountain. Food, experimental equipment, medical equipment, advanced missiles, even artifacts. Most of it was the kind of material that couldn’t be taken overseas without approval from the Ministry of National Defense.”

I firmly patted his shoulder as he muttered bitterly.

“Cheer up, Chuck. It’s not the first time, is it? And it’s not as if you didn’t know.”

“Hah. That’s certainly comforting.”

But it was an undeniable fact.

As we had destroyed more than a few dozen terrorist organizations, the only things we had seen weren’t corpses and pools of blood. What we had seen most nakedly was the shameful face of the world.

*How, and from whom, did they get all those things?*

Military officials? High-ranking politicians? Or black-market dealers who would do anything for money?

Maybe all of them.

I didn’t know.

But one thing was certain.

Someone was watering the weeds that absolutely had to be pulled out by the roots.

“Bastards.”

Chuck Hagel muttered bitterly and threw his cigar far away.

The faint flame, which had been slowly burning down, disappeared completely in the middle of the dark desert, where a bitter cold had settled.

He watched it until the very end before speaking with a sigh.

“Crazy Korean. What are you planning to do now?”

The sudden question pulled me from my thoughts, but I answered calmly. I had already made up my mind several days ago.

“I’m going back.”

“To South Korea? Well, it couldn’t be North Korea, so I suppose that’s right.”

“Hard to say.”

Half right, half wrong.

But instead of confirming or denying it, I merely shrugged.

Chuck Hagel gave me a bitter smile.

“Right. You can’t keep working as a vigilante for justice while wearing that ridiculous mask forever.”

“Hmm. I wouldn’t call it particularly ridiculous.”

“Are you serious? Is this some kind of South Korean fashion sense?”

I gave a small laugh and answered.

“Not to us.”

“Hm?”

“Rebel forces and terrorists. What do you think it looks like from their perspective?”

“……!”

Chuck Hagel’s mouth closed tightly.

I looked up at the night sky, filled with countless constellations whose names I didn’t know, and continued.

“The Mujahideen. Al-Qaeda. ISIS’s Syrian branch…”

One by one, I recited the names of the massive terrorist organizations whose leaders and headquarters we had annihilated over the past week.

Then I listed the small and medium-sized terrorist organizations whose roots we had torn out entirely.

“We may not have cleaned up everything, but we’ve certainly sent them a warning.”

They didn’t know our names or ages. They didn’t even know our nationalities or what we looked like.

We wore masks, avoided surveillance with Magic Johnson’s Magic, and fought while changing our weapons and combat methods.

And…

“There’s no opponent more frightening than an enemy whose identity you don’t know.”

In the short span of only one week, we had become objects of fear to terrorist organizations.

They couldn’t catch us even with enormous bounties on our heads. And because they didn’t know who we were, their specialty—the retaliatory terrorist attacks they were so good at—was useless against us.

On top of that, several leaders of some of the world’s most notorious international terrorist organizations had already died at our hands or been controlled into starting internal conflicts.

“If they don’t want to suffer the same fate, they’ll flatten themselves and hunker down.”

A weak deterrent invited resistance, but overwhelming power inspired fear and terror.

The prisoners we had freed had already spoken before microphones and cameras about what they had seen and experienced, as well as the atrocities they had endured.

The international community was once again burning like a furnace.

Over the horrific situations unfolding throughout the world.

And over us.

“Things will get a little better, then.”

The weed called malice first sprouts in the human heart, and those who harbor malice commit evil deeds.

But what could I do?

Even if it was impossible to pull out every weed growing in people’s hearts, it was still possible to pull out the weeds that were visible.

“It’s not how many weeds you pull out. What matters is how many people pull them out together. Chuck and me. Just like we did.”

One person pulls one.

Another pulls two.

Or three.

If everyone paid attention and did their part, wouldn’t the weeds eventually disappear?

I had only recently gained that small but great insight.

“Well, that’s how I see it, at least.”

Had I talked too much by myself?

I quietly closed my mouth.

Chuck Hagel had been looking at me with a strange expression when he suddenly spoke.

“Hey. Can I ask you one thing?”

“Anything.”

“I didn’t get an answer earlier… Where exactly are you going back to? Judging by what you just said, it sounds like you should at least be going to the Vatican.”

I answered with a small laugh.

“It’s hard to explain, but somewhere similar to this.”

“Where? Afghanistan?”

“Somewhere farther away. Much farther.”

“…Much farther?”

Chuck Hagel looked bewildered, and my smile deepened despite myself.

That was right.

It was time to go back now.

After taking care of the one thing I had put off until the very end.
## Chapter artifact 612

# Chapter 612

“Come out.”

His voice was low and steady. His eyes gleamed sharply in the darkness.

Instead of answering, I calmly watched him. After a brief silence, the living room suddenly brightened with a click.

The man cautiously stepped forward and spoke again, his voice firm.

“Come out. I know you’re hiding there. Do you know who I am?”

Of course I did. I knew his name and face, even his age and hometown. I just hadn’t expected him to pull something like this the moment I came home.

“All right, this is the last warning. If you don’t come out by the time I count to three, I’m calling my close younger friend. He’s an incredibly strong and successful Hunter. One. Two…”

I was curious about what would happen after he counted to three, but after seeing everything there was to see, continuing to watch felt embarrassing.

I spoke with a sigh.

“Don’t tell me that close younger friend is me?”

“……!”

“Well, would you look at that. Guess I was right.”

The man who had frozen like a statue in shock stared at me with wide eyes.

“What the hell? Why are you coming out of there?”

“I knew you were going to call me anyway, so I came before you could. Happy now?”

After a brief silence, Jin-ho hyung spoke with a heavy expression.

“How much did you see?”

“From when you said, ‘Come out.’”

“Ah, fuck…”

“You looked pretty cool. Your presence was so intense I almost came out on my own.”

“Are you making fun of me right now?”

“Yes.”

At my shameless answer, Jin-ho hyung stared at me for a moment before suddenly letting out a quiet laugh.

“You bastard. You haven’t changed at all.”

Why did such a simple remark make me feel so happy and grateful to see him?

I smiled along with him and answered.

“I’m hungry. Make me some ramyeon.”

* * *

Sitting across from each other with a steaming pot between us made me feel as though I had gone back about a year.

Of course, both Jin-ho hyung and I had changed considerably since then.

“This is the first time I’ve seen you in a suit. You used to wear nothing but ragged-looking tracksuits.”

“Hey, don’t call it ragged. It’s a pretty expensive brand.”

“When did you buy it?”

“Hmm. High school?”

How old had Jin-ho hyung been then? After thinking for a moment, I nodded.

“So it wasn’t ragged-looking. It was actually ragged. Get me some water. No, wait. Do you have any soju?”

“You might as well go to a barbecue restaurant and ask if they have any meat.”

“……Judging by that, you’re probably going to die young.”

“I would’ve quit ages ago if it weren’t for that asshole Section Chief Kim. That fucking bastard isn’t even that far from me in age, but he picks fights over every little thing and acts like a complete jackass.”

Jin-ho hyung roughly loosened his tie and downed three shots of soju in a row.

At the end of last year, he had finally passed the civil service exam he had been preparing for so long.

“So you really did become a civil servant. The world really is coming to an end.”

“Listen to this bastard’s attitude. Did you think I wouldn’t?”

“No. Becoming one is beside the point. I thought you’d drop dead in the act while watching porn before you ever got there.”

“……Hmm. That does make a fair amount of sense.”

Since he didn’t deny it, at least one thread of his conscience must still have remained.

If there had been a Pornography Department among the government’s official ministries, this man would have climbed all the way to minister.

With Sora Aoi as deputy minister and Asuka Kirara as spokesperson, he would have ruled Pornhub from the top.

Unfortunately, no such deranged ministry existed. After passing through a special recruitment exam, Jin-ho hyung had been assigned to the Hunter and Gate Management Department, a division known for being a plum assignment.

Of course, I had a vague suspicion that our personal relationship had earned him a few invisible bonus points.

Glug, glug, glug.

After filling his soju glass to the brim, Jin-ho hyung suddenly spoke.

“What brings you here?”

“You seem to have forgotten, but this is my house. Though at this point, I’m starting to confuse it with a garbage dump or an officetel.”

“Isn’t that because the owner hasn’t shown his face in two or three months?”

“If that’s what you mean, I came partly to see your face. I also had something to pick up.”

“Something to pick up? If you mean clothes, why not just buy some? You’ve got money coming out of your ears.”

“I can’t buy it even if I have the money. There’s nowhere that sells it.”

“What kind of thing is that?”

Jin-ho hyung looked puzzled, then suddenly let out a short exclamation.

“Ah. You mean that old capsule?”

“Yeah, that one. Luckily, you didn’t throw it away.”

“You said you’d kill me if I did.”

“That’s why it’s lucky. If you’d thrown it away, I really would have killed you. Phew.”

“……You’re joking, right? Please tell me you’re joking.”

The game capsule that had first led me to the Murim had been left here, abandoned without any real purpose.

Thanks to the System’s permission, I could now freely use Login and Logout without the capsule.

But that didn’t mean I could treat it like an unwanted piece of junk.

That old capsule was the greatest contributor to making me who I was. It was a priceless treasure.

“I don’t wipe the dining table, but I clean that capsule once a week. It still doesn’t work, though. Why are you taking it?”

“Just because. It’s decoration or something.”

“Isn’t it haunted? You know, back when you lived at Hope Goshiwon, you slept in that capsule and had a weird nightmare…”

Come to think of it, that had happened.

As Jin-ho hyung began bringing up what happened after my first Logout, I hurriedly changed the subject.

“Did you see the news? Things got pretty crazy in the Middle East and Afghanistan this time.”

“Huh? Why are you bringing that up all of a sudden?”

“No, I’m asking if you saw it.”

“Of course I saw it. Yesterday, the terrorist groups in the Middle East and the rebel forces in Afghanistan even issued a joint statement. They said they’d refrain from terrorism in the future and keep their subordinates under control. It was basically a declaration of surrender because they were scared shitless.”

“You shouldn’t let your guard down. It’ll only last for a little while.”

“Even so, aren’t those five masked weirdos incredible?”

Fortunately, it seemed my attempt to change the subject had worked. I breathed an inward sigh of relief and nodded.

“They are.”

“Well, anyway.”

After slurping up a mouthful of noodles, Jin-ho hyung rinsed his mouth with soju and continued.

“You’ve had it rough. A monster wave right after the new year, humans worse than monsters, and now trips to the desert and Africa.”

“What do you mean, rough? It was just something I had to do…”

I suddenly faltered and let the end of the sentence trail off.

Wait a minute. What the hell was this guy saying?

“Sorry, what?”

“What do you think? Exactly what you heard. I took a guess, and I was more or less right.”

“……!”

“Come on. How many people in the entire world could have done something like that? Everyone says they wish all the terrorists would just die, and that they can’t stand the rebel bastards. But who would actually put on a mask and act on it? No, more importantly, who would even have the ability to make it happen?”

At the sight of my round eyes, Jin-ho hyung snorted softly.

“Some people have probably guessed, too, but they’re keeping quiet. There’s no evidence, and it’s not as if they have any reason to blame you. But one low-ranking civil servant happens to know what kind of person the masked man is—and even shares ramyeon with him—so he can casually sound him out like this.”

I rubbed the back of my head, which had somehow gone numb.

I had suspected I would be named as a prime suspect, but I hadn’t expected to get caught this absurdly easily.

“I’m… I’m really not him.”

“Sure. Let’s say that’s true. So when did you get back?”

“……”

Damn it. I was already done for.

I let out a deep sigh, filled my soju glass, and answered.

“Three days ago. No, four.”

“Good. You’re finally being a little more cooperative.”

“Don’t say a word about this anywhere. Forget the fact that it’s classified—you’ll be in danger if you do.”

Team Leader Choi, my family, and I were always surrounded by invisible protection.

Jin-ho hyung wasn’t.

He understood exactly what I meant and smacked his lips.

“Hmm. I feel like some kind of big shot.”

“Before you become a big shot, a bomb might get delivered to you.”

“Maybe. But even if they all know, they won’t be able to touch me, will they? They won’t know what Jin Taekyung might do if he completely loses it. Hah, isn’t this what you call Untouchable?”

Jin-ho hyung laughed without a care and continued.

“By the way, how busy have you been lately that you can’t even keep track of when you came back?”

“Hmm.”

How busy had I been?

I scratched at my thick, overgrown beard and answered.

“I just train day and night. I eat with my family, then go right back to training.”

“Training? Why does someone at your level still need to train?”

“You graduated from a prestigious university, but you spent almost another ten years studying. It’s basically the same thing.”

“You really know how to hit a sore spot. And how are you and I the same? This isn’t just a difference in fields. We’re playing on entirely different levels.”

He had a point. The prestigious university Jin-ho hyung had attended admitted hundreds of students a year, and roughly the same number graduated.

But I still needed training.

There was no end to learning, and *gongbu*—the work of mastering something—didn’t apply only to academics.

*To be more precise, I’m not learning something new so much as slowly going over what I already know.*

In that sense, the training I was doing was more like a review.

It was study for my own sake, and study for the sake of this world.

Unfortunately, I still hadn’t managed to create a complete result.

“Ugh, look at that serious expression. It makes me want to slap you in the cheek.”

“……I’m in the middle of being serious, so could you shut that mouth of yours?”

“Put yourself in my shoes. What would you do if you were me?”

“Hmm. I suppose you’re right. Have a drink.”

We clinked our glasses amicably.

After tossing back his soju and stirring the noodles that had gone completely cold, Jin-ho hyung asked,

“So, is the training going well?”

“More or less. I started preparing about a month ago, so I’m slowly reaching the final stage, but… it isn’t easy.”

This was no exaggeration.

Right now, I was like a child trying to put together a ten-thousand-piece puzzle.

As I checked each piece and fit them together, I felt my own shortcomings and regretted what I lacked. Now, unable to find the final piece, I was groping around in the dark.

And I already knew the name of the darkness covering my eyes.

*The heart demon.*

The dark cloud hanging over my heart did not scatter easily.

My worries about the Murim and the modern world. And… yes, more than anything, the final sight of Kim Hwajong kept coming back to me.

His voice, which seemed as though it could fade away at any moment.

His eyes slowly closing in the red snowfield covered with blood.

Maybe the reason I had come here wasn’t to take the capsule after all.

Maybe I had come because I wanted to feel at ease.

I wanted to meet a friend who lived his own life in a completely different world—not a beloved family member or a companion at my side—and clink glasses with him like we used to.

*Yes. That was it.*

I suddenly felt my heart grow lighter.

I hadn’t completely shaken off the heart demon, but simply acknowledging and accepting every situation and worry had lifted some of the weight from my heart.

At the same time, I realized that the place where I needed to be wasn’t here.

“I’m leaving.”

“The ramyeon’s gone cold. I was going to make some tofu kimchi as a side dish… What? All of a sudden?”

“Yeah. I just thought of something I have to do. Drink by yourself.”

“Are you crazy?”

“No. I’m the landlord. Are you going to start paying rent this month?”

Jin-ho hyung, who had been glaring at me fiercely, immediately bent deeply at the waist.

“Please get home safely, Boss.”

“Yeah, yeah.”

I snorted softly and headed for the front door. Behind me, Jin-ho hyung’s urgent voice rang out.

“Hey, hey! What about the capsule?”

“Next time. I’ll take it next time.”

Even as I answered, I knew.

Maybe next time, I would give the exact same answer and still not take the capsule.

Maybe, just like today, I would only clink glasses with him.

“All right. Hang in there, you bastard.”

With someone’s quiet mutter reaching my ears, I walked on.
## Chapter artifact 613

# Chapter 613

The Training Room was silent again today.

Countless kinds of weapons lay strewn across the floor, and the walls—enchanted with automatic restoration magic—had been reduced to a miserable ruin.

And at the center of it all… there I was, sitting cross-legged and lost in thought.

*More. Just a little more.*

I was almost there.

The final piece of this enormous puzzle.

Immediately after parting ways with Jin-ho hyung, I had holed myself up in the Training Room and begun the final work required to find that last piece.

Even if stress made every hair on my head fall out, even if things reached the worst possible point and I faced the danger of qi deviation, I had to overcome it.

No matter what it took, I had to complete this puzzle before I left.

*For the future ahead.*

I had only begun looking for the puzzle’s final piece recently, but I had been thinking about putting the puzzle together for several months.

Yes. It had probably been after the battle with the Arch Lich—the incident dubbed the Small Cataclysm.

*If things continue like this, everyone will be in danger.*

It was a thought that had suddenly occurred to me one day.

And as time passed, my unease had turned into certainty.

Mana levels had risen abnormally, monsters had grown stronger accordingly, and human casualties—which had fallen dramatically after the Great Cataclysm—were once again mounting everywhere.

Modern humanity needed another kind of power, and after much thought, I made a decision.

To create martial arts.

To hand them a new sword and shield with which to face the dangers and disasters that grew every day.

Of course, it was anything but easy. The martial art had to be stable enough for even the lowest-rank Hunter to learn, while still possessing a moderate level of power that evil people could not easily abuse.

But… at last, I had found the final piece of this enormous puzzle.

*Yes. This is it.*

A single path completed after hundreds of attempts.

The moment I completed the cultivation technique I had not yet given a name.

Ding. Ding. Ding.

As if to congratulate me on my success, a series of vigorous alerts rang out.

* * *

Team Leader Choi—or rather, Choi Minwoo, who had now taken office as Guild Master of the Peace Guild and Vice Guild Master of Ares Guild—was so busy that he barely had time to breathe.

The matters requiring his attention had multiplied into the hundreds during the week he had been away, and his temporarily assigned personal secretary was sweating bullets as calls from bigwigs poured in from every direction.

“G-Guild Master. The Blue House has proposed a luncheon.”

“The political world and the Federation of Korean Industries would like you to attend a social gathering…”

“The Guild Alliance has proposed a partnership concerning Gate-related business…”

“Regarding the establishment of overseas branches…”

Some of the proposals could not be refused, while others could easily have been rejected. But Choi Minwoo’s answer was always the same.

“All right. Schedule them.”

Choi Minwoo moved according to a schedule planned down to the minute. He spent each day like a machine, barely sleeping at all.

The people around him watched his dangerously busy routine with concern.

“Now, choose one. Team Leader Choi, Guild Master Choi, or Vice Guild Master Choi. Which title should we use to address you?”

“Please call me Team Leader Choi. That was my title when we met.”

“All right, then. Team Leader Choi, I’ll be direct… Get some rest. Cut down your schedule and leave the minor tasks to your secretary.”

“She’s right, Team Leader Choi. You may be young, but if you keep going like this, you’ll wear yourself out.”

“I’m fine. Please don’t worry, either of you.”

“Team Leader Choi.”

“No, really…”

“As for me, I’m fine.”

Faced with Choi Minwoo calmly repeating the same answer, Song Song and Im Kkeokjeong, who had tried to dissuade him, could do nothing but fall silent.

And yet, why was it?

The answer that reached their ears was the same as before, but the answer that reached their hearts was different.

*As for me, I’m fine.*

Choi Minwoo left them with that one phrase, the same and yet different, and continued burying himself in work.

He even sent away the personal secretary who had been giving him a little help, then spent his days in a frenzy as his already hectic life grew even busier.

It was only natural that a conversation about him would come up one day during a private meeting with President Baek Hanseong.

“You seem very busy these days.”

“That’s why I like it.”

“I heard you no longer even keep a secretary… Is there some special reason?”

“Coffee.”

“Pardon?”

“She couldn’t make coffee. That’s all.”

President Baek Hanseong assumed it was a joke and laughed it off, but every answer Choi Minwoo had given him was sincere.

Choi Minwoo liked being buried in work so completely, and the coffee made by his young secretary had been strangely awful.

And… he was grateful that, at least for a little while, this allowed him to forget the longing and sadness he kept feeling for someone who repeatedly came to mind.

“I’ve wasted enough time on idle conversation. Let’s move on to the next item.”

One day. Then another.

While Jin Taekyung continued training in an isolated space, Choi Minwoo isolated himself even while meeting countless people.

Perhaps that was why, one day, he suddenly remembered someone’s name.

On that day, when he had been pushing himself with almost cruel intensity as usual, the longing he had been suppressing deep in his heart raised its head.

“Driver Jung, turn the car around.”

“Pardon? I’m sorry, but as far as I know, our next scheduled location is…”

“Cancel everything on today’s schedule. There’s somewhere I need to go.”

Leaving behind the driver’s startled gaze in the rearview mirror, Choi Minwoo sank deep into the limousine seat.

With the warm spring breeze and sunlight flowing through the half-open window, he headed toward a place where he could meet someone.

Step. Step.

The hill he climbed alone was high and steep, and Choi Minwoo’s footsteps were heavy.

No—perhaps it was his heart that was heavy.

Sorrow and guilt over the one person he could never reach, even if he climbed this high, steep path a hundred or a thousand times, weighed on Choi Minwoo’s heart.

Rustle. Pluck.

Along the way, he gathered an armful of spring flowers that had bloomed early. The pure white violets did not seem like enough, so he added the scarlet moss phlox growing in clusters along the path.

The man who was no longer by his side had always said he liked red.

*And yet he always wore black suits.*

It was only recently that Choi Minwoo had learned what color he liked most, and why he had sold all those motorcycles.

Why he had quit drinking despite once keeping alcohol so close, and why he had trimmed the shaggy beard and long hair he had grown out before neatly parting it.

*Why did you do that? You were enough for me.*

He had learned everything, but he had learned it all too late.

Feeling the dull ache in his chest, Choi Minwoo continued walking.

On the warm, breezy hilltop, a large burial mound awaited him, and the three characters carved into the granite gravestone stood out with unusual clarity.

**The late Kim Hwajong.**

What was he supposed to say?

Staring blankly at the old butler sleeping beneath the warm hill rather than a cold, snow-covered mountain, Choi Minwoo opened his mouth.

“I’m here.”

The eyes that had always remained calm trembled faintly. Choi Minwoo bit down hard on his trembling lips, then slowly continued.

“…Grandfather.”

The one word he had held in his heart but never once managed to say while the old man was alive finally slipped out.

Whoosh—

A wind that had come from somewhere swept over Choi Minwoo’s entire body. The grass covering the hill bowed at the waist, and the branches waved their hands.

Then, the next moment, Choi Minwoo set the bouquet beside the burial mound—and froze.

*What’s that?*

His eyes widened with puzzlement. His gaze had stopped on the back of the gravestone.

There, in a place he had failed to notice until now, other words had been carved.

> You came.
>
> Thank you, and I love you.
>
> Be happy.

“……!”

Who had carved those words?

It was an obvious question, but for the moment, it did not matter.

Choi Minwoo stood frozen like a stone statue, staring endlessly at the short message.

His heart trembled like flowers swaying in the wind. Something that had suddenly surged up from somewhere deep inside his chest blocked his throat and heated his eyes.

“Ah.”

Overwhelmed by it all, he let out a choked sigh.

“You came quickly. I thought I’d have to wait at least a few more days.”

Someone’s voice suddenly rang out.

Choi Minwoo turned around. In his field of vision stood someone holding a small box.

It was the Skeleton King.

Why was he here?

What did he mean by saying he had been waiting?

But those questions disappeared as soon as they arose.

What Choi Minwoo needed now was not a reason, but warmth.

He needed an answer to a question he could not answer on his own.

“May I ask just one thing? Just one question.”

Under normal circumstances, the Skeleton King would have bluntly said no.

But not this time.

He readily nodded.

“Anything.”

“If it had been Mr. Jin Taekyung… what would he have done at a time like this?”

It was a sudden question, but the Skeleton King immediately understood what it meant.

“Why do you ask?”

“Because he’s the strongest person I know. Stronger than anyone else.”

The Skeleton King stared at Choi Minwoo in silence before answering in a low voice.

“He would have cried. Without a doubt.”

“……!”

“And then he would overcome it and go on living, forever remembering the person who left.”

That was enough.

Choi Minwoo shed the tears he had been holding back. He let his sorrow and regret, his longing and guilt, flow away with them.

The Skeleton King quietly stepped back and thought that it would be better to hand over the things in the box a little later.

At the same time, he recalled what Jin Taekyung had said about half a day earlier when entrusting the box to him.

*“I’m sorry, but let me ask you one favor.”*

*“I don’t want to. No. Go back.”*

*“Give this to Team Leader Choi. No one else.”*

*“You damnable human. Now you’re not even pretending to listen. Do I look like an errand boy to you?”*

*“It’s not because you’re an errand boy. I can entrust it to you because I trust you.”*

*“…What exactly am I supposed to deliver?”*

*“Martial arts.”*

*“What?”*

*“He’ll understand if you put it that way. Tell him there’s a letter inside the box and make sure he reads it.”*

*“No. As if I could find a human I haven’t even seen lately…”*

*“Wait at Butler Kim’s grave. Even if you run into him before then, don’t say a word. He’ll probably need time to overcome it.”*

The Skeleton King thought that Jin Taekyung was an exceedingly strange human, no matter how much he considered it.

For one thing, he had run into Choi Minwoo at the cemetery exactly as Taekyung had predicted.

And he was even stranger for the fact that once he fell asleep, he would not so much as blink even if someone grabbed him by the collar and shook him awake.

*Damn him. How dare he make me run such a pathetic errand while he sleeps peacefully by himself?*

Jin Taekyung had repeatedly begged him not to wake him under any circumstances, so he was probably dead asleep by now.

The more the Skeleton King thought about Jin Taekyung, the more infuriating he found him. But honestly, for some strange reason, he did not feel all that bad.

*“I can entrust it to you because I trust you.” Trust, huh? Hmm. Hmmm.*

The Skeleton King nodded as he remembered the box in his hands and Jin Taekyung’s words, then muttered quietly.

“…Have a good dream, you devious human.”

Whoosh—

The wind blew once more.

One man’s sobs and the voice of a monster who had grown closer to humanity were swallowed by the wind.
## Chapter artifact 614

# Chapter 614

> **System**
>
> **Synchronization** begins. 10, 9, 8, 7…… 1, 0.
>
> **Synchronization** completed successfully. The updated stats have been applied to the body, and the use of certain **Titles** is restricted.
>
> **Login** complete.

Before the familiar System notifications had even finished, the rough texture of straw and the smell of wet grass reached me through my skin and nose.

I spat out the piece of rice straw stuck to my lips and muttered inwardly.

*I’m back.*

My return to the Murim.

I had spent barely over a month in the modern world, yet it felt like something that had happened in the distant past. That was no illusion.

*I’ve had way too much going on.*

The Murim. And the modern world.

Everything surrounding me and the two worlds was changing at a frightening pace. There had been so many incidents one after another that even two bodies would hardly have been enough.

“……”

Come to think of it, I really did have two. It was having to control them by turns that made it so damn exhausting.

Anyway…

*Ah. I don’t want to get up.*

The rice straw wrapped around my entire body was warmer and softer than I had expected.

I desperately wanted to stay sprawled out like this and sleep for a while. I had barely slept for nearly a week while developing a martial art for widespread use.

If I hadn’t heard the low murmur of conversation nearby the next moment, I might really have fallen asleep.

“Hmm. You’re asking what kind of person Captain is?”

“Yes. I’ve been curious for a while. The other two haven’t arrived yet, so I’m bored, too. Escort Song, you’re curious as well, right?”

It was a familiar voice. After Hyuk Mujin and Ju Hwaran’s conversation, Song Ilseom, the Soul-Chasing Guest, answered gruffly.

“I’m not particularly curious.”

“Did you hear that? Escort Song is curious, too.”

“I said I’m not curious.”

“I’ll give you two more silver nyang.”

“……I’m becoming slightly curious.”

That bastard was obsessed with money.

Once Song Ilseom had joined in after kneeling before the big spender’s silver donation, Hyuk Mujin’s hesitant voice reached me.

“Hmm. This is difficult to answer. Captain is definitely still asleep, right?”

“Yes. Yes.”

“He is certainly asleep. His breathing is steady.”

“Well, I suppose that makes sense. Once he falls asleep, he wouldn’t know if a ghost carried him away.”

What do you mean, steady?

That was because I was controlling my breathing. Personally, I was rather curious about what kind of answer I would hear, too.

And my loyal right pinky toe did not betray my expectations.

“Our captain is that very famous, uh, that extremely famous… What should I call it…?”

“A handsome and heroic rising martial artist?”

At Ju Hwaran’s question, delivered in a voice as clear and lovely as a Young Chang piano, Hyuk Mujin answered in the most decisive tone imaginable.

“He was a fucking bastard.”

“……Ah.”

“……Uh.”

“These days, people call him the Blazing Flame Divine Dragon and all that. But just a year or two ago, you’d have been hard-pressed to find a bigger fucking bastard. Every day, he’d hit a pleasure house, get shit-faced, steal public funds, and blow the money at gambling dens. He was so bad that his sobriquet back then was…”

“Hey.”

“That’s right. He was the Night King. In that field, even if all Ten Kings came at him together, they wouldn’t have been a match. Whenever he strapped a money pouch to his side and headed proudly toward a pleasure house every night, my fellow gate guards and I would say, ‘That fucking bastard is using the Heavenly Demon Reign Step again today.’ Come to think of it, Great Hero Song, you’ve heard of him because you’re so well traveled. As expected.”

At Hyuk Mujin’s rambling, Song Ilseom answered in a displeased voice.

“What are you talking about? I didn’t say anything.”

“What?”

“I didn’t say anything.”

“Come on. What are you talking about? You said ‘hey’ a moment ago.”

“I didn’t.”

“It was definitely a man’s voice. Don’t joke around. Then who on earth was it…?”

His drawn-out sentence abruptly broke off.

A short but heavy silence passed. Then someone carefully brushed away the rice straw covering my face.

Rustle. Ssshh.

The straw blocking my vision was removed, and beneath the faint moonlight, two gazes collided.

With a warm, friendly smile, I greeted Hyuk Mujin, whom I had not seen in a long time.

“Hey.”

“……”

Hyuk Mujin stared down at me in silence, his gaze sinking deeply. Then he covered my face with the straw in his hand again.

Very carefully, as if nothing had happened.

“Move it.”

“Perhaps the moon is bright. I seem to be hearing things….”

“If you don’t move it, your life is going to get dark. Move it.”

“Yes, sir.”

The pleasant warmth I had felt from the straw had long since vanished.

Like a vampire sealed away by an exorcist and awakened after several hundred years, I slowly rose from the wagon’s cargo bed.

Whoooosh.

A chilly wind blew away the pieces of straw clinging to my clothes.

Ju Hwaran met my gaze, then hurriedly turned her head away. Song Ilseom, who had been warming himself by the campfire—when had he even lit it?—suddenly stood up with a mutter about needing to feed the horses hay.

And my shadow, enlarged by the dancing firelight, fell over one person.

“What are your last words?”

At my quiet question, Hyuk Mujin answered calmly.

“Captain, please don’t do this. Hear me out.”

“That’s why I asked.”

“You said they were my last words. It sounds like a will.”

“It probably is.”

“……Ah.”

“You were having a great time. As your squad leader, I feel an indescribable joy at seeing my subordinate like that.”

That was half true. I really couldn’t contain myself.

After busting my ass in the Murim, busting my ass in the modern world, and returning without getting any sleep, I found my direct subordinate badmouthing me behind my back.

And the name of the emotion that followed this situation straight out of a light novel was rage.

“Face, arms, legs, abdomen, or back. Pick one.”

“Is that perhaps my cause of death?”

“I’m not going to kill you. I’m just going to beat you within an inch of your life.”

After a brief moment of thought, Hyuk Mujin answered.

“I’ll choose my abdomen.”

“Why?”

“Wounds on the back are… a martial artist’s shame.”

I let out an exclamation at his spirit.

“What a load of bullshit.”

“I did do wrong, so I’ll gladly accept my punishment. Come at me.”

“Since you chose your abdomen, I’ll choose the rest.”

“What?”

“What do you mean, ‘what?’ It would be unfair if only you got to choose. I have to choose, too, for it to be fair.”

“No, wait a minute. How is that fair at all…?”

Wham!

A violent impact rang out.

Above the slowly burning campfire, the dark shadow of a man who had leaped into the air while spraying blood from his nose loomed large.

*I’m already using my fists the moment I get back.*

This was Mount Daebyeol, the border region connecting Anhui and Hubei to Henan.

And the two shadows approaching from the distance to the accompaniment of Hyuk Mujin’s quiet screams were the Fire Dragon Pavilion’s final members, a bunch of rootless unorthodox faction trash.

“……Why is that person being beaten?”

“Taishan! Is here!”

At last, the Fire Dragon Pavilion’s Nanman expedition party had gathered in one place. I left them with a short but powerful lecture, then turned away.

“All right, let’s finish beating this bastard and get going.”

There was no objection.

Right now, I wasn’t the S-rank Hunter Jin Taekyung. I was the Blazing Flame Divine Dragon, the greatest young prodigy of the orthodox Murim, and the Fire Dragon Pavilion Master—their direct superior.

Crack!

“Urgh! Aaaagh!”

I really did love the Murim.

Of course, that excluded the damned Dark Heaven.

* * *

It was a pitch-black space where not a single ray of light entered.

In the darkness, where no sound or sign of life could be felt, figures lying facedown trembled faintly.

Then, the next moment—

“Heaven above, earth below!”

“All demons bow in submission!”

With those thunderous cries bursting forth in a single voice, crimson-black flames rose from the darkness.

Fwoosh!

A ring of fire blazed fiercely.

Though it was unmistakably a flame, the fire beyond it radiated a chill deep enough to seep into the bones. Beyond that flame, someone’s shadow wavered.

—It has been a long time.

It was impossible to tell whether the voice belonged to a man or woman, a young person or an old one. It was impossible even to distinguish whether the voice was low or high.

It was a truly strange voice. It reverberated loudly, echoing from every direction and constricting the figures prostrate on the floor.

—My servants.

Everyone trembled before the unprecedented power contained in those few words.

Perhaps from fear of the absolute being. Or perhaps from the joy and rapture of standing before the one they served.

That was why they cried out in unison.

“These foolish and lowly servants humbly pay their respects to the great Lord of Heaven!”

Lord of Heaven. The master of the heavens.

That was the only phrase capable of describing the being.

A supreme entity more dignified and magnificent than anyone else. The heavens above the clouds were his palace, and every lowly thing living on the earth beneath the sky was the Lord of Heaven’s servant and subject.

No. They had to make it so.

—How much time has passed?

No one failed to understand the question of the living god.

Those prostrate in this place were the Lord of Heaven’s devoted and loyal servants, devoted beyond anything that could be put into words.

The young man bowed low against the floor was no different.

“Exactly one hundred and thirty-six days have passed since the day the great Lord of Heaven last awoke!”

At the young man’s vigorous answer, the fiercely burning flames wavered.

—Yes. I remember now. Western Heaven. That was the day the child left.

“We are deeply ashamed!”

Led by the young man, another enormous cry burst forth.

Unlike the first, this cry was filled with shame and self-reproach.

When the Western Heaven Demon Lord and the forces of Dark Heaven under his command had been annihilated at the Sichuan Tang Clan, they had been thrown into confusion by the unexpected result and had been forced to awaken their master, who had been sleeping deeply.

“Great Lord of Heaven. Never again… will such a thing happen.”

The flames shook once more at the voice that slipped through the young man’s clenched teeth.

—No. It was my mistake for trusting you, who were inadequate.

“……!”

—Blood Lord. You are no different, are you?

At the most painful reprimand of all, the pupils of the young man—Blood Lord—trembled.

He knew better than anyone what the master he worshiped so fervently was saying.

*Henan.*

The day the orthodox Murim had named the Shaolin Bloodshed was one of the most painful memories of Blood Lord’s life.

Not only had the results fallen far short of what had been planned, but he had also suffered the humiliation of leaving one of his arms behind.

If he had failed to bring back Shaolin’s sacred treasure, the Green Jade Buddha Staff, as well… He did not even want to think about it.

*The Sword Saint. And Jin Taekyung.*

The thought of those two bastards—whom even tearing apart alive would not satisfy him—made murderous intent rise within him.

But a loyal servant must never display wicked emotions before his master. Blood Lord barely suppressed the murderous intent surging within him and opened his mouth.

“P-Please forgive me.”

Whoooong.

Instead of an answer, a chilly wind swept through the darkness.

Just as Blood Lord and everyone else shrank back even further, a quiet voice pierced their ears.

—What is lacking can simply be filled.

The air sank heavily. The wind stopped, and every living thing held its breath.

In that space where everything had come to a halt, the Lord of Heaven’s voice continued.

—I shall fill what you lack.

It was a command, backed by an irresistible force.

Fwoooooosh.

The darkness and shadows wavered.

Blood Lord’s eyes widened with rapture as he realized that an immense surge of qi from somewhere unseen was settling into his body.

“L-Lord of Heaven!”

Blood Lord—and everyone else—understood once more.

Their master was a living god, an absolute being who encompassed the entirety of heaven and earth.

And they understood what this power, personally bestowed upon them by their master, meant.

—Deliver this message to South Heaven and North Heaven.

Rumble, rumble, rumble!

The earth trembled. The world shook.

Beyond that unprecedented power that warped everything, a thunderous resonance burst forth.

—Now… we begin the Great War.

Heaven above, earth below. All demons bow in submission.

Amid the cries of the loyal servants, filled with rapture and madness, the invisible shadow waved a hand.

The crimson-black flames that had colored the pitch-black space disappeared, and darkness descended once more.

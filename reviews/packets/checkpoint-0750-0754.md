# Checkpoint Review — 750–754

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

# Chapters 750–754

## Plot

Leviathan survives Jin Taekyung’s second attack and escapes into the deep sea. Back in Japan, Jin and Team Leader Choi confront the Defense Minister for withholding forces during the disaster, while the Skeleton King’s invocation of Pearl Harbor’s vengeful spirits causes a supernatural disturbance. Prime Minister Koizumi grants the Korean forces independent authority and promises Japanese support.

The Skeleton King determines that Leviathan, badly wounded and hungry, must be lured back toward land with S-rank Magic Gems. Japan provides two refined gems, and Jin uses the Skeleton King as bait aboard a small motorboat near an uninhabited island. Leviathan attacks, but Jin—concealing his presence with the Turtle Breath Technique—impales its mouth, rescues the Skeleton King, and begins an aerial battle.

Despite the Broken Body debuff, Jin destroys Leviathan’s water attacks and pierces its brow with Heavenly Strike. The Skeleton King draws a lightning strike and survives because his skeletal body acts as a lightning rod. Leviathan, terrified that Jin may be the human who defeated its former master Asmodeus, flees toward the deep sea with Jin clinging to its body. A vast, unidentified mass of bones gathers in the abyss and blocks its path as Jin and the Skeleton King prepare to fight together.

## Continuity

- Leviathan remains alive but severely wounded, with injuries to its mouth, teeth, eye, and brow. It is fleeing toward the deep sea while Jin attacks from its body.
- Jin’s Broken Body debuff remains active, reducing his physical attributes, slowing him, and increasing his internal-energy consumption.
- Jin can suppress his breathing, heartbeat, body temperature, and vital energy with the Turtle Breath Technique.
- The Skeleton King’s skeletal body can draw and survive Leviathan’s lightning. His identity as a monster remains concealed from the public.
- Japan has granted Jin and the Korean forces independent operational authority and promised military support.
- The two Japanese-provided refined S-rank Magic Gems were used as bait; five additional refined gems remain hidden in Ares Guild’s Area A.
- The source and identity of the enormous mass of bones blocking Leviathan remain unknown.
- Jin and the Skeleton King intend to fight Leviathan together, but whether they can stop it or whether Leviathan will survive remains unresolved.
- The Prophet’s second terrorist campaign, Michael Silbert and Huginn’s undisclosed operation, the media campaign against Jin, Siegfried Wassmann’s death, and Jin’s **Unknown Death** quest remain unresolved.

## Translation Decisions

- Render **진상** as **Jinsang** and **경상** as **Gyeongsang**, preserving Koizumi’s wordplay; render **진주만의 원혼** as **the vengeful spirits of Pearl Harbor**.
- Use **Defense Minister**, **Team Leader Choi**, **Prime Minister Koizumi**, and **Skeleton King**.
- Retain **Broken Body**, **Turtle Breath Technique**, **Heavenly Strike**, **Leviathan**, **Asmodeus**, **Magic Gem**, and **Philippine Sea**.
- Render **마력** as **magical power**, distinct from **mana**.
- Render **유골사태** as **boneshed** and preserve the Skeleton King’s modern-food wordplay with **samgyeopsal**, **ssamjang**, and **scallion salad**.

## Durable state

{
  "active_continuity": [
    "Jin Taekyung is fighting Leviathan while weakened by the Broken Body debuff.",
    "Jin Taekyung has pierced Leviathan's brow with his flaming spear and is attacking from its body.",
    "The Skeleton King's skeletal body can draw and survive Leviathan's lightning.",
    "Leviathan believes Jin may be the human who defeated Asmodeus and is fleeing in fear toward the deep sea.",
    "Jin intends to fight Leviathan together with the Skeleton King.",
    "An unknown mass of bones blocks Leviathan's path in the deep sea."
  ],
  "continuity_sources": [
    754
  ],
  "open_questions": [
    "What is the source or identity of the bones blocking Leviathan?",
    "Can Jin Taekyung and the Skeleton King stop Leviathan in the deep sea?",
    "Will Leviathan survive the injuries to its brow and body?"
  ],
  "safe_through": 754,
  "temporary_decisions": [
    "Render 망가진 신체 as Broken Body.",
    "Retain Skeleton King as the English title for 스켈레톤 킹."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 750

# Chapter 750

Deep beneath the sea.

It was so dark, with countless wrecks and corpses filling the water, that it was impossible to see even an inch ahead. Then, without warning, blue-white flames erupted.

*Fwoosh! KRAAAAAASH!*

The current split apart, and the water vaporized.

The flames carried a force that defied the laws of nature. No—a spear shot forward like a ray of light.

Toward the enormous shadow moving at an unbelievable speed.

Toward a calamity that could never be allowed to live.

But just as the force within the spear defied the laws of nature, so too did the mythical monster.

*KRRRRRUMBLE!*

The sea shook.

At the same time, large and small whirlpools of water surged up from the depths and blocked the spearhead as it raced forward.

*KOOOOONG!*

Waves spread outward in layers with the violent collision.

By the time the shock and thunderous roar that had shaken the world had subsided, the flames that had pulverized every obstacle in their path were also fading away, having exhausted their strength.

They had ultimately failed to reach the monster’s body, which was disappearing into the thick darkness in the distance.

*Swish. Clack.*

The sea had already grown quiet.

The spear, drifting helplessly with the current, was caught in someone’s hand.

The back of the man silently staring in the direction the monster had vanished seemed to radiate emotion ready to erupt like an active volcano.

No, let me correct that.

It was not merely that he seemed to radiate emotion ready to erupt.

It looked as though he would explode if anyone so much as touched him.

Even in that moment, when he had lost the monster that could never be allowed to live.

…Even now.

“Enough.”

The instant the sharp voice slipped from my lips without my realizing it—

*Flash.*

Everything that had filled the surroundings melted away in a vivid green light.

The sea, dark as night.

The enormous wreckage left behind by the skyscrapers.

Even the nameless corpses that had met their deaths with their eyes wide open.

The empty space where the hologram had disappeared was filled by several dozen unfamiliar faces.

Men dressed in custom-tailored suits and military uniforms that looked expensive at a glance.

Among them, the old man sitting in the seat of honor across from me opened his mouth with a grim expression.

“Good heavens. To think Leviathan got away.”

It was the first time I had seen his face, but according to Team Leader Choi, that old man was one of the three most powerful people in Japan.

No—if you counted only the authority he actually possessed, he might even have been number one.

The position of Defense Minister was an immensely powerful one even in peacetime. In a situation like this, with the country at war, he possessed more power than anyone.

But I was not in a good mood as I looked at the old Defense Minister.

To be a little more honest, I wanted to deal with that damned old man in front of me before Leviathan, who was not even there right now.

Why?

Simple.

Because that man had eliminated the last chance of catching Leviathan only an hour ago.

Now that I understood the whole situation, there was no way my words could be pleasant.

“Exactly. It was a shame we missed it. If someone had helped us at the end, we might have caught it.”

“……!”

The air in the conference room froze in an instant. While the Japanese men glanced around nervously, the Defense Minister glared at me with displeasure.

“What you said sounds as though you are implying that Japan is responsible. Did these old ears hear you incorrectly?”

“I heard you were over eighty, but you still seem remarkably healthy. Your ears work pretty well for an old man.”

“What did you say?”

“Have your ears actually gotten worse? You already heard me, so why do you keep asking?”

“What kind of—!”

*Bang!*

The Defense Minister slammed his hand on the table and turned toward Team Leader Choi.

“Are you simply going to stand by and watch this insolence?”

Normally, Team Leader Choi would have given me a warning look around this point.

That is, normally.

“When you speak of insolence, Defense Minister, are you perhaps referring to striking the table in a place like this?”

“What?”

“Japan formally requested assistance through the Ministry of Foreign Affairs, and we risked our lives to come all the way here in response. And yet…”

Team Leader Choi’s words cut off, and his gaze turned cold.

“Why did your side not deploy additional forces?”

“……”

“As I understand it, at the exact moment Jin Taekyung attacked Leviathan, at least two thousand Hunters had been mobilized. The Ground and Air Self-Defense Forces were also standing by.”

“That was…”

“I know. I know that most of them would not have been much help in battle. But if you had deployed Japan’s Hunters, even at the last moment, they could have delayed the fleeing Leviathan for a little while.”

Team Leader Choi’s words were clear and precise. They were also entirely true.

That little bit of time was exactly what I had needed.

A small amount of support and sacrifice to distract the wounded monster dragging its battered body away and make it lose precious time.

But in that deep sea, where I had risked my life to enter, all I could do was watch the monster’s back grow more distant.

The same problem applied to Team Leader Choi and the more than two hundred Hunters who had gotten off the aircraft and were preparing to enter.

“I was about to lead the Hunters in myself because I could not stand by and watch, but your side stopped us. You even invoked your authority over field operations.”

“……!”

“If you wanted to minimize your own sacrifices and take all the credit, you should have done it properly. Then things would never have reached this point.”

The Defense Minister clenched his lips tightly before speaking.

“The encirclement—the encirclement was perfect.”

The Skeleton King, who had been listening, asked me with genuine confusion.

“If it was perfect, shouldn’t it not have been breached?”

“Yeah, exactly.”

“But I heard it was breached?”

“That’s right. It was.”

“And you even lost its location because of the magical power it released?”

“Yep.”

After listening to all my helpful answers, the Skeleton King muttered,

“What the hell? Are they idiots…?”

“……!”

“……!”

With that single statement striking the truth with perfect accuracy, the temperature inside the conference room dropped below freezing.

But even as I watched everyone clamp their mouths shut and glance nervously at one another, I felt not the slightest bit satisfied.

*What a bunch of fucking lunatics.*

Seeing these bugs, worse than monsters, sitting there pretending to be an operations command center was not even enough to make me laugh bitterly.

*It’s not like I can call this fucking bullshit and quit, either.*

The number of casualties confirmed so far was roughly one hundred thousand.

It was only this low because, fortunately, the tsunami Leviathan had created had stopped around the outskirts of Tokyo.

If it returned after I left, Tokyo would be renamed Atlantis.

*And if it gives up on Japan and targets somewhere else…*

That would be a problem in its own way.

Of course, the idiots—including that old monkey chief standing before me—would probably celebrate and dance with joy just because they had survived.

“……”

They were exactly the kind of people who would do that.

The thought only made me feel worse.

After letting out a hundred-percent pure, deep sigh, I spoke to the Defense Minister, who had become completely silent.

“Enough with the pointless arguing. Call someone else in charge.”

“S-Someone else in charge?”

“The Prime Minister. Or the King of Japan. Anyone has to be better than you.”

“The King of Japan?! How dare you refer to His Majesty the Emperor of the Great Japanese Empire that way—”

“This is driving me crazy. How long are you going to keep using that empire crap? If you collapsed after taking two atomic bombs, you should have surrendered the title of Emperor too. Don’t you think?”

“That was a savage and barbaric act of destruction by those American Yankees!”

I covered my ears as the Defense Minister screamed.

“I think I’m going to get radiation poisoning. I think I’m going to get radiation poisoning. I think I’m going to get radiation poisoning. I think I’m going to get radiation poisoning.”

“Chikshō!”

Was it because he had already lived a full life? Or had radiation contamination robbed him of his fear?

Just as the Defense Minister was rampaging and charging at me with his old body, the Skeleton King reached out and seized him by the back of the neck.

“Stop, you old and insignificant per—no, Yellow Monkey.”

“You insolent dog! Release me at once! How dare a Yankee bastard covered in fur lay his hands on the Defense Minister of the Great Japanese Empire!”

“Do you dare insult the mighty United States in front of me?”

“I have not forgotten! I have not forgotten the terrible things you bastards did to this land and its innocent subjects of the Imperial State!”

“Vengeful spirits of Pearl Harbor, descend upon me!”

*What the hell are these lunatics…*

A heated argument between a Japanese imperialist from the ’70s–’80s generation and an American monster from the Demon Realm.

Watching those horrifying hybrids with my own two eyes made my chest swell with emotion despite itself, but it was not over yet.

*Fwoooooosh.*

“……?”

What the hell was this?

My entire body suddenly grew cold, and the fluorescent lights began to dim.

Even the people struggling desperately to pull the Defense Minister and the Skeleton King apart felt the chill and shuddered.

*What the hell is happening all of a sudden?*

I turned my head in confusion.

In midair, my eyes met Team Leader Choi’s.

And in that moment, I realized something and stood there with my mouth hanging open.

In my ears, someone’s shout from a moment earlier was repeating itself with vivid clarity.

*Vengeful spirits of Pearl Harbor, descend upon me!*

*No, fuck. Don’t tell me…*

*Whoooooosh! KRAAASH!*

The eerie energy transformed into a gale and shattered the fluorescent lights on the ceiling.

I was already running through the sudden darkness toward someone.

“Look closely, and feel the resentment of the—”

“Hey, you crazy bastard!”

*Crack!*

* * *

Thank goodness.

Thanks to a traditional promotion system that still prioritized family and connections over ability even in the twenty-first century, most of the high-ranking officials and generals inside the conference room were ordinary people. They were so frightened that they had not even heard the Skeleton King’s shout.

And apparently my demand to call someone in charge had gotten through, because not long afterward, the manager—no, the Prime Minister—arrived.

“Thank you so much for coming all the way here to help our homeland, Jinsang!”

“Ah, yes. It’s nice to meet you, Prime Minister Koizumi.”

I had never imagined I would live to see the day I met this man in person.

I had always seen collections of his famous quotes on the internet, so meeting him like this briefly made me feel as if I had run into a celebrity.

Of course, given the situation, I could not show it. The important matter right now was Leviathan.

At the very least, that was what I wanted.

I wanted to.

“I’ll get straight to the point. In order to track Leviathan—”

“I heard the Defense Minister was rude to you, Jinsang. Once this matter is settled, I will severely reprimand him, if only to soothe your feelings!”

“Uh, wow. I really appreciate that.”

“Why do you look like that, Jinsang?”

“No, it’s just… We also need to discuss Leviathan. And the way you keep addressing me is a little…”

“What is wrong with the way I address you, Jinsang?”

“……”

“Ah, I see. It must sound different in Korea. Then shall I call you Gyeongsang, using the last syllable of your name?”

There was no way that would work.

I felt as though I had dodged a pile of shit only to get pissed on.

*Is he wishing me a minor injury the next time I fight Leviathan…?*

I seriously considered Jinsang versus Gyeongsang, then sighed.

*Well, at least it isn’t Severe Injury.*[^1]

[^1]: Japanese *Jin-san* (“Mr. Jin”) sounds like the Korean *jinsang*, meaning an obnoxious or troublesome person. Koizumi’s proposed *Gyeong-san* sounds like Korean *gyeongsang*, meaning a minor injury.
## Chapter artifact 751

# Chapter 751

Unlike the Defense Minister, a lunatic imperialist, Japan’s newly seated prime minister was surprisingly reasonable.

“It is impossible to remove the Defense Minister right this moment, but I will grant the Korean people—including Jinsang—independent operational authority.”

“Please also guarantee various supplies and military support through the Defense Ministry. We accepted your country’s request because we wanted to cooperate, not because we wanted to be sacrificed.”

In response to Team Leader Choi’s polite but firm words, the Japanese prime minister nodded.

“I will gladly agree. I shall do everything within the limits of my authority.”

Given how I felt, even throwing the idiots in the Defense Ministry into a radioactive hot spring wouldn’t have been enough.

But what could we do? The damage had already been done. All we could do was our best with what we had.

“But how do you intend to deal with the monster that has already escaped?”

“I have a method.”

The answer suddenly came from somewhere.

When I made a throat-cutting gesture toward the Skeleton King, who was glaring arrogantly at the Japanese prime minister, he flinched and hastily corrected himself.

“I have a method, yo.”

It was a form of honorific speech that had no place in any family tree, but the Japanese prime minister—already famous for his priceless quotes—was not the sort of man to care about details like that.

Instead, he gazed at the Skeleton King with a friendly expression.

“Oh, Stomu-King. I have heard quite a bit about you.”

“Me? I mean… me, sir?”

“Of course. I knew of you not only because of this incident, but also from when you suppressed several mutation Gates in Korea.”

The Skeleton King had already become known among the public here and there, even before the vigilante incident came to light.

For a brief while, public attention focused on the appearance of a top-tier Hunter whose existence had never been revealed. But that attention quickly faded.

Magic Johnson’s identity laundering had been that perfect, and since the whole thing was so absurd, nobody had suspected from the beginning that he was a monster.

*…Actually, it’s because I was the one getting cursed at so much.*

“It is a pleasure to meet you at last, Stomu-King.”

The Skeleton King had been looking proud that the prime minister of an entire country knew who he was. Now, he slightly narrowed his brow.

“It is a pleasure to meet you as well. But I am—no, my name is Stone King.”

“That is why I am calling you that now. Stomu-King.”

“I said Stone King. Here. Repeat after me slowly. S. Tone. King.”

“S. Tone. King.”

“This time, join the first two. Stone. King.”

“Stone. King.”

“Very excellent! Now put it all together.”

“Stomu-King.”

“Good heavens. I really am going to lose my mind. I can’t believe this! What on earth is your tongue made of?”

A cursed archipelago’s pronunciation system in a bizarre collaboration with Demon Realm-style mangled speech.

Unable to watch the tragedy any longer, I stepped in to mediate on Team Leader Choi’s behalf, since he had squeezed his eyes shut.

“Let’s stop. Stone King, Stomu King, stalking—what difference does it make?”

“It makes a tremendous difference! You Jinsang bastard!”

“More than the crack that’s about to appear in your skull?”

“Hmm. Now that I think about it, perhaps it doesn’t matter that much.”

“See?”

“Of course. Just call me whatever is convenient. That becomes my name.”

“Good attitude, Fucking. Now tell us how to track Leviathan.”

Perhaps he disliked his newly bestowed name, because the Skeleton King muttered a quiet curse before opening his mouth.

“First of all, your premise is wrong. We should not be tracking Leviathan. We need to lure the bastard as close to land as possible.”

“Lure it?”

“Yes. That sea is entirely its territory. If we try to track it with some half-baked method, we may lose it forever instead.”

“That means…”

“It was too severely injured to flee very far. Leviathan will not have gone far yet.”

Team Leader Choi raised a question.

“Although Leviathan suffered a heavy blow thanks to Mr. Jin Taekyung, I understand that it obtained an unrefined S-rank Magic Gem. Wouldn’t that be enough for it to recover from its wounds and then some?”

“Recover?”

The Skeleton King gave a small snort and continued.

“If it is Leviathan, it can absorb all the magical power no matter how much there is. But even if it makes that magical power entirely its own, completely healing its injuries is a separate matter.”

“Hmm.”

“It needs far more magical power to recover from wounds of that magnitude. By now, the bastard must have realized that as well.”

The opinion of an actual monster was fairly persuasive.

On top of that, One Annihilation was a killing blow powerful enough to wreck even its caster’s body.

True to its name, Leviathan had twisted its body at the last moment, but those were not wounds that could heal in a short time.

*Lure it. Lure it, huh.*

As I turned the word over in my mind, I suddenly spoke.

“Do you really think a monster cunning enough to assess the situation quickly, take only what it wants, and run away would fall for a trap?”

The answer that came back was simple.

“It will. If the conditions are right.”

“A trap it can’t help but enter, even though it knows it’s a trap?”

“We must think of Leviathan as a hungry, wounded beast. That is also why it came all the way here.”

Team Leader Choi muttered like he was groaning.

“We’ll need to prepare an enormous bait.”

“Yes. We need bait so delicious that Leviathan will risk its life to charge at it.”

And at this point, there was only one thing that could lure Leviathan in.

“Excuse me, Prime Minister?”

At my deliberately mild voice, Prime Minister Koizumi—who had been watching our conversation with dazed eyes—answered.

“Ah, yes. Go ahead.”

“I was wondering… does Japan happen to have a few of those?”

“Those? What are you talking about?”

“Don’t play dumb. S-rank Magic Gems.”

“…What?”

“Let us borrow them for a bit.”

“…What?”

“Now, now. Why are you so surprised? We’ll catch Leviathan and return them. There, it’s a promise.”

I held out my little finger toward the prime minister, whose eyes had gone perfectly round.

*We’ll win one and pay it back. Win it.*

* * *

In the modern world, S-rank Magic Gems were treasures of tremendous value.

Before even considering that they were the finest energy source capable of powering an entire metropolis, there were only around a hundred of them in the entire world. Their rarity alone was astonishing.

Perhaps that was why the Japanese prime minister, despite promising his full cooperation, had initially been horrified. Of course, in the end, he had no choice but to hand them over, even if it was against his will.

“Here they are.”

*Click.*

As the security Magic was deactivated, a box made of soft velvet opened. Inside sat two Magic Gems scattering a brilliant light.

“Hm. Only two?”

The Japanese prime minister hurriedly answered after seeing my expression.

“These are all the S-rank Magic Gems owned by the Japanese government.”

“Really?”

“It is the absolute truth! Do you know how much trouble I went through persuading the cabinet members and His Imperial Majesty?”

“If I dig around and find more, then for every S-rank Magic Gem…”

“…Mr. Jin Taekyung?”

“Oh, sorry. I’ve gotten so used to doing this.”

*This is why habits are scary.*

At Team Leader Choi’s intervention, I scratched the back of my head. The Japanese prime minister, who had been edging backward for a while now, hurriedly slipped out of the room, repeatedly begging us to return the Magic Gems safely.

But once he was gone, the mood in the room was rather lukewarm.

“Hmm. Two…”

“That’s not enough.”

“This body agrees. They still contain a considerable amount of magical power, but not enough to lure Leviathan.”

The number of Magic Gems did not matter. What mattered was the quantity and quality of the magical power remaining inside them.

*Normally, they should obviously have been refined… but this time, we have a different use for them.*

There were two S-rank Magic Gems right in front of us, but what we wanted was bait.

Bait so delicious that Leviathan would have no choice but to charge at it even while knowing it was a trap.

A massive mass of pure magical power, like the one it had taken.

*Even if we use both of these together as bait, they still won’t come close to an unrefined Magic Gem.*

And I was not the only one who had reached that conclusion.

Just as we looked at one another with similar expressions, the Skeleton King suddenly spoke.

“No matter how I think about it, these will not be enough. What about bringing more?”

“What do you mean, bring more… Oh.”

A fact I had briefly forgotten flashed through my mind.

Area A, hidden within the Ares Guild headquarters.

That mysterious place had been filled with astronomical amounts of cash, works of art, and Magic Gems. Among them had been no fewer than five S-rank Magic Gems.

“But those have already been refined.”

“That… is true.”

The Skeleton King smacked his lips and added regretfully,

“Still, they should be better than nothing. Can’t we make it work somehow?”

Of course, having something was better than having nothing.

But even adding five more would not make much difference under the current circumstances.

The more perfectly refined a Magic Gem was, the greater its value. The S-rank Magic Gems that Lee Jungryong and Go Jun had stashed away in Area A were literally top of the line.

And there was one more thing.

The final decision belonged to the owner.

“They must have been obtained through illegal channels in the first place. If the truth gets out, the media will have a field day.”

*Yeah. Especially in a situation like this, it would turn into a complete fucking shitshow. Hyenas with cameras were everywhere, waiting to pounce at the slightest opening.*

After Team Leader Choi’s firm statement, the Skeleton King thought for a moment before offering another idea.

“What if we gather completely unrefined Magic Gems? We could collect every one that emerges from the nearby Gates and bring them all here…”

I smiled broadly and patted him on the shoulder.

“Congratulations. You have been sentenced to life in prison for violating international law.”

“What the goddamn hell!”

“Welcome to the bright and cheerful twenty-first century. It’s surprisingly fucking hard to live here.”

*Crack.*

The Skeleton King clenched his teeth and continued.

“Since it has come to this, we have no choice. We either use those Magic Gems as bait, or we select only the very best and track down and kill the bastard ourselves with a raid team.”

“Wow. The world has really improved. I never thought I’d live to see the day a monster suggested raiding another monster.”

“There is no other way!”

*No other way, huh?*

I exchanged a covert glance with Team Leader Choi.

Then, carefully gauging the angry Skeleton King’s reaction, I slowly began.

“I never said there wasn’t.”

“What?”

“There is one method.”

The Skeleton King brightened and asked,

“What method is that?”

“Before I tell you, there’s one thing you should know. If a raid team is organized… you’re sitting this one out.”

“You’re leaving me out? What do you mean?”

It must have been more unexpected than he could have imagined. I continued as he stared at me with perfectly round eyes.

“We have no choice. There are too many eyes on us right now.”

He was not stupid enough to miss the meaning behind my words. The Skeleton King asked with a stiff expression,

“You mean that because my power might be exposed, you intend to leave me out of the battle with Leviathan?”

“You know it.”

“This is insane! Is that really something you can say right now?”

*Bang! Crunch!*

The fist he brought down with a shout shattered the table. The pair of eyes that had come right up in front of me held clear disappointment and fury.

“Wicked human. I must have judged you wrongly. How can you say such a thing in a situation like this?”

“It doesn’t matter. You’re a monster.”

“…What?”

“Even if we catch Leviathan, once your identity is revealed, you’re finished. I’m only trying to avoid that.”

*Wood crackle.*

The bones in the Skeleton King’s fist shifted with a grinding sound. He stared at me with an expression of disbelief before crying out as though spitting blood.

“It doesn’t matter! If I can save them, I can do anything! Leviathan, the one that caused this disaster—”

“Anything?”

“Huh?”

*Got you. Hooked.*

I looked at the Skeleton King with a satisfied smile.

“You said you would do anything. Right?”
## Chapter artifact 752

# Chapter 752

Leviathan.

The news that the nightmare of the sea, slowly fading from memory with the passage of time, had been resurrected drew more attention from around the world than any of the other Monster Waves that occurred that day.

[Breaking News) Leviathan Appears—Disaster Descends on Japan]

[The Star of Asia, Jin Taekyung, Saves Japan Despite Countless Suspicions; Leviathan Disappears After Suffering Injuries]

[Anonymous Senior Japanese Official: “There Was More Than Enough Chance to Kill Leviathan. If Only the Defense Minister Hadn’t Suddenly Shit Himself.” Complacency at Japan’s Defense Ministry?]

[At Least 100,000 Casualties Confirmed So Far. The Archipelago in Crisis.]

[Japanese Defense Minister Fujiwara: “I Will Risk My Life to Protect the Imperial Subjects—No, the Citizens.” The True Feelings of an Imperialist Who Can’t Keep Up with the Times?]

[Japanese Defense Minister Fujiwara Leaves the Press Conference as Though Fleeing (Photo)]

[Japanese Prime Minister’s Resolute Declaration: “We Will Kill That Monster Within Three Days and Show the Archipelago’s Strength.” When Asked by a Foreign Reporter How, He Smiled Faintly and Said, “We will do it, no matter what. That is my promise.”]

[Japanese Netizens: “Please, Someone Shut the Prime Minister’s Mouth.” Unanimous…]

[The Young Hero from the Peninsula Who Saved the Archipelago. Yet Light and Shadow Surround the Hero.]

[Chinese Chairman Xiao Yang: “Mr. Jin is a True Hero. Only Cowardly, Narrow-Minded Petty Men Would Insult Him.”]

[Operator of China’s Biggest Anti–Jin Taekyung Website Arrested by Public Security. The Charge? Being a Petty Man.]

[Leviathan Disappears Once Again. Yet the Terrorist Attacks and Monster Waves Continue.]

[Michael Silbert and Odin Guild Suppress a Third Monster Wave in a Single Day. Praise Pours in from Around the World, Along with Questions About Sky: “Why Hasn’t He Appeared?”]

.

.

.

*Tap.*

After setting down the tablet, Huginn thought,

*As I expected. This isn’t good.*

The tide of public opinion was slowly changing. Japan’s Defense Ministry was being blamed for losing Leviathan, and even the media outlets that had competed to insult Jin Taekyung were beginning to quietly change their stance.

*What if Jin Taekyung actually kills Leviathan in a situation like this?*

The image they had damaged through their media campaign could be restored in an instant.

If that happened, it was only natural that the plan they had already prepared down to the last detail would suffer a setback.

Once his thoughts reached that point, Huginn turned toward his superior. Michael Silbert, who had his back turned while making coffee, spoke abruptly.

“The back of my head suddenly feels prickly. Is that just my imagination?”

“……It probably isn’t just your imagination.”

“If you have something to say, say it. But if it concerns Jin Taekyung, keep it to yourself.”

Under normal circumstances, Huginn would have silently obeyed his superior.

But Huginn still carried the heat of the battle that had ended only thirty minutes earlier, and he could not ignore his sense that the situation in Japan was taking a dangerous turn.

“Have you perhaps not heard the news yet?”

At the frustration in Huginn’s question, Michael gave a quiet laugh and lifted his coffee cup.

“Huginn, my friend. Do you really think I don’t know what you know?”

“Then why—”

“The aroma is especially good today. Shall I make you a cup as well?”

“……Guild Master, if Jin Taekyung ends up killing Leviathan, dealing with the aftermath will become difficult.”

*Click.*

Michael set down his coffee cup and leaned back against the leather sofa.

The inside of the tent, enchanted with spatial expansion, was as luxurious as a suite in a seven-star hotel. Michael seemed so relaxed that it was hard to believe he had defeated an S-rank monster only moments earlier.

“Huginn, I will say this only once, so listen carefully.”

“Yes.”

“There is nothing to worry about. Every condition has already been met, and Leviathan is not something that can be defeated so easily.”

“But……”

“I want Jin Taekyung and Leviathan to do their best. To struggle with everything they have in order to kill each other and survive. That is all I want.”

“……!”

“Ah, of course, if Jin Taekyung dies in the process, that would be the best possible outcome.”

Michael winked at the confused Huginn and reached for the coffee cup he had set down a moment earlier.

*Click. Splash.*

Steam rose from the coffee that spilled across the table.

Huginn, lost in thought, looked at his superior in surprise.

“Are you all right?”

“……”

“Guild Master?”

“Ah.”

Michael’s face, which had been as rigid as stone, relaxed smoothly. He instantly regained his characteristic impassive expression and answered,

“It is nothing. I suppose I am slightly tired after several intense battles.”

But the loyal retainer who had remained by Michael’s side for many years did not take his words at face value.

After stealing a glance at Michael’s trembling fingers, Huginn spoke with genuine concern.

“It seems your training has been too intense over the past few months.”

“Did it seem that way?”

“Yes. Especially after you learned about Jin Taekyung, you have been noticeably……”

Huginn let his sentence trail off. Realizing Michael was staring at him, he lowered his head.

“I spoke out of turn.”

Heavy silence settled between the two men.

Michael was the first to break it.

“Is the press conference ready?”

“Yes. They have been waiting for an hour already.”

“We will begin in thirty minutes. We will leave as soon as the conference ends, so finish preparing to depart in the meantime.”

“Understood, Guild Master.”

Huginn answered without a moment’s hesitation. He did not ask why they were preparing to leave already, or where they were going.

He would find out naturally by the time preparations for their withdrawal were complete.

Another terrorist attack. Another Monster Wave. And somewhere out there, another measure of glory and fame would be waiting for them.

Within this cruelly well-written script, Odin Guild was always moving one step ahead and building an immortal reputation.

“I will come to escort you shortly.”

After bowing politely, Huginn left the room.

Left alone, Michael Silbert muttered softly,

“You’re right, Huginn. Maybe that really is the case.”

Jin Taekyung.

From the moment he first learned of that man’s existence, an inexplicable emotion had filled Michael’s chest.

The name of that emotion, hazy as fog, was impatience.

And anxiety.

Then, an old memory suddenly surfaced.

The pathetic version of himself who had possessed nothing but ambition. The humiliation of those days when he had no choice but to keep his head down and stay out of Cheon Taemin’s sight.

But……

“In the end, I will be the only one who wins.”

The low murmur slipped between his lips.

Feeling the mighty energy filling his entire body, Michael Silbert became certain of the victory that would soon arrive.



* * *



*Whoooooosh.*

The wind blowing from far away was thick with the smell of salt.

Near the Philippine Sea, close to the Japanese archipelago, a whale surfaced above the rolling water and blinked its enormous eyes.

The sea seemed strangely quiet today—even to this gigantic creature.

Although it had been traveling through the ocean for several hours, it had not seen a single ordinary fishing boat, much less a whaling ship.

*Pfooout.*

The whale spouted a stream of water into the air before diving back into the deep. Hundreds of fish that had been swimming together in a school followed behind it.

*Splash.*

The creatures that had naturally joined together swam without rest.

Not farther away, but deeper.

They followed a resonance calling to them from somewhere in the depths swallowed by thick darkness.

*Gooooong.*

The hundreds became thousands, and the variety of species increased as well.

Yet the marine creatures swimming after the resonance sensed nothing strange.

Not even when a vast darkness they had never seen before surrounded them like a net.

*GRAAAAAH. CRUNCH!*

And that was the end.

Teeth harder than steel tore the whale and sharks apart, and the monster sucked in thousands of fish.

The monster opened its enormous jaws and chewed and swallowed everything. For a moment, it savored the taste.

No—it absorbed all the energy and memories they contained.

*Whoooooosh.*

In the place known as the deep sea, a dim light rose.

But even after absorbing new energy, hunger still filled the monster’s eyes.

*This is all there is?*

It had not been like this when it roamed the five oceans at its master’s command.

From the moment the Demon King Asmodeus descended, the entire world—from land to sea—had been filled with delectable magical power. Even the smallest fish had carried a small amount of magical power.

But now, everything had changed.

Its once-great master had vanished, and the monster that had ruled every sea in the world had been forced to hide in the deep sea once more to avoid human eyes.

And it had done so while suffering severe injuries.

*Hisssss.*

Green blood flowed from wounds that had not yet healed and mixed with the seawater.

Consumed by unbearable rage, Leviathan shuddered its enormous body.

*How dare… How dare a mere human…*

But anger was not the only thing Leviathan felt.

Fear.

That loathsome emotion it had felt because of one impossibly tiny human had bound the mighty monster tightly to the deep sea.

*What are you? How can a lowly human possess such power?*

Leviathan could not understand it.

Over the course of roughly a day, Leviathan had completely absorbed the masses of magical power that humans called S-rank Magic Gems.

It had been certain that, if the healing power of water were combined with the new magical power, even wounds of this severity would heal completely.

Yet everything was unfolding in the worst possible way.

*The moment I leave the deep sea, the humans will target me. It would be better to build up as much strength as possible here before leaving…*

Then.

The enormous eye that had been rolling aimlessly in every direction stopped moving.

It was because unfamiliar memories that were not its own had suddenly flashed through its mind.

*What is this?*

The question lasted only an instant.

The memories of the countless marine creatures Leviathan had swallowed moments ago were surging into its mind like waves.

A blue sky.

A calm sea without a single fishing boat.

And……

*What is that?*

A small boat bobbed in the middle of a sea that had been filled with human warships and submarines only a few hours earlier. The image was embedded in one of the memories.

The distance was only a few hundred kilometers.

The boat was circling near an unidentified uninhabited island. A school of fish had discovered it an hour earlier.

*It’s too close. And the sea has grown too quiet.*

Leviathan immediately realized that it was a trap prepared by humans and scoffed.

*Idiots. Do you really think you can deceive me—*

The thought abruptly broke off before reaching its end.

Leviathan had already turned its head toward the surface above, and all five senses sharpened toward the alluring scent that had traveled down the waves into the deep sea.

*Magical power. An enormous amount of magical power.*

At the same time as the realization came, an intense craving seized Leviathan’s entire body.

*If only I had that.*

*If I could make that power—greater even than what I absorbed before—my own, these wounds would be nothing.*

*I could even kill the human who inflicted this humiliation on me in an instant.*

Muttering as though hypnotized, Leviathan ground its teeth.

*I must not be swayed. It is obviously a trap prepared by humans.*

But that resolve did not last long before collapsing.

According to the memories it had received, there was no sign of a human anywhere. The information carried by the waves at that very moment was the same.

*I cannot sense the vital energy unique to humans. Then…?*

Leviathan made its decision.

It would willingly advance toward the trap they had prepared.

*Splash!*

Its enormous body surged upward, cutting through the currents of the deep sea.
## Chapter artifact 753

# Chapter 753

The man looked around and thought,

*What wonderful weather.*

Only a little over twenty hours ago, the sea had been bucking like mad. Now it was calm, and gulls flew in flocks across the clear sky.

*Beautiful. Is this nature?*

The place where the man had lived was nothing like this. That distant, distant place was always dim and dark as night, with a terrible stench hanging in the air. Of course, for personal reasons, he had never smelled a stench in his life, but there was no doubt the place had reeked.

In any case, the man liked this world.

He liked it even more because he could see beautiful scenery he had never witnessed before, and because he was surrounded by some pretty decent people.

“……”

Thinking it over again, though, he supposed he had to exclude one of them.

No, two.

The man—the Skeleton King—suddenly remembered a conversation he had shared with someone a few hours earlier.



“Anything?”

“Huh?”

“You said you’d do anything, right?”

“Huh?”

“My goodness, such a noble spirit of sacrifice. As battalion commander, I am genuinely moved.”

“A spirit of sacrifice? What are you talking about?”

“Shh. Enough. I know. I know all about your heart, so stop pretending.”

*Holy shit…?*



Something felt off.

Things were taking a strange turn.

He looked toward another human with an expression that desperately pleaded for help, but even the man he had thought was at least somewhat sane turned out to be in on it.



“Hey, handsome and intelligent human…”

“Please don’t speak to me. My heart is too full right now to answer.”

“You son of a bitch…”

“I see you in a new light, Mr. King. To sacrifice yourself for the greater good…”

“I never said anything about sacrificing myself, so why do you keep saying that…?”

“We will never forget this sacrifice. You are a true hero.”

“Stop! Why are you coming closer?”



By the time he sensed that this was more than just strange—that he was in danger—it was already too late.

Jin Taekyung was blocking the door and creeping toward him with a bundle of rope in his hands.



“I’ll talk to you carefully. I’ll try to find my courage.”

“Don’t sing some weird song! Put down the rope!”

“From today on, I want to use you as bait.”

“What song has lyrics like that? Don’t rewrite it!”

“Team Leader Choi, what are you doing just standing there? Am I the only bad guy?”

“Ah, my apologies. I was wiping away my tears.”

“Get the hell out of here!”



*Whooosh! Rattle!*

A wave that had rolled in from far away crashed against the stern of the little motorboat.

The seawater splashed refreshingly across his face, jolting the Skeleton King out of his thoughts. He muttered,

“……Damn it.”

Naturally, resisting had been pointless.

The humans he had trusted had boxed him in from the front and rear, while Jin Taekyung—the root of all evil—solemnly declared, like a judge delivering a verdict:



“Don’t make a needless fuss. If you willingly become bait, there won’t be a boneshed.”

“Isn’t it supposed to be bloodshed?”

“He doesn’t have any blood.”

“Oh.”

“So, what’ll it be?”



What else could he do?

The die had already been cast—and it was a loaded die controlled by hustlers.

Realizing that he had fallen into the trap before Leviathan, the Skeleton King chose to avoid a boneshed and obediently boarded the little boat.

Along with the two S-rank Magic Gems provided in advance by the Japanese government.



“Get rid of these cumbersome things. The monster will drool over me even if I’m alone.”

“No, no. Do you eat samgyeopsal without ssamjang and scallion salad?”[^1]

“……Has it already been decided that this body will be eaten by Leviathan?”

“Don’t worry. We’ll save you when it’s time to dip you in the ssamjang.”

“What if it swallows me in one bite?”

“Wow, that sounds delicious.”

“……You are going to save me, right?”

“I suddenly feel like having some soju. Don’t you think so, Team Leader Choi?”

“I do prefer wine, but soju definitely goes with samgyeopsal.”

“You’re definitely going to save me… right?”



That was the last thing he heard.

The little boat, carrying one S-rank monster and two S-rank Magic Gems, set off before he even received an answer. Following the GPS coordinates entered beforehand, it began circling near an uninhabited island several hundred kilometers away.

It had been doing so for the past hour.

Waiting for the big one hiding somewhere in the deep sea to take the bait.

“You damn humans.”

The Skeleton King looked up at the blue sky and lamented. He could feel a nonexistent heart pounding in his chest.

*What if the monster really shows up?*

The Skeleton King was fully aware of the difference in strength between himself and Leviathan.

Unlike his former self, who had not even possessed reason, Leviathan was a predator endowed with immense magical power from the moment of its birth. In other words, they were fundamentally different.

Leviathan had ranked among the top ten even among the S-rank monsters known in the Demon Realm as the “Seventy-Two Legion Commanders.”

Even if its strength had declined compared to its former reputation, fear that had once settled in his heart did not disappear easily.

*Don’t come. Don’t come. Please don’t come…*

The Skeleton King liked this world.

Unlike himself, who was already dead, nature was filled with vital energy. The cities were packed with dazzling, wondrous things, and there were human women of blinding beauty.

Sometimes, the sight of certain humans disgusted him, but most of them were decent enough. He was even gradually getting used to the word *friend*, which had felt so unfamiliar at first.

But even for him, becoming nourishment for Leviathan was out of the question.

The Skeleton King felt as though he might cry when he imagined himself turned into a hearty samgyeopsal set meal.

*You damn humans, please let me live too!*

He was even more miserable because he could not shout aloud for fear of attracting Leviathan’s attention, but it was already far too late to turn back.

The Skeleton King touched the ssamjang and scallion salad hanging around his neck.

No—the two S-rank Magic Gems.

He glared at the sea.

*Right. You only die once, not twice.*

As he repeated a phrase humans often used, courage he did not know he possessed welled up inside him.

Besides, unlike humans, he had actually died before. There was nothing left but bones, so maybe he could somehow survive being chewed a few times.

It would be even better if he got stuck between the monster’s teeth.

“Come on, you monster! I’ll take you on!”

And at the very moment the Skeleton King released that brave shout—

*ZZZT. Splat.*

Something fell from the sky and covered the crown of his head and one shoulder.

The Skeleton King rubbed the sticky, glaringly white substance with a bewildered expression, then scowled.

Shit.

Fresh bird shit, too.

“I ought to pluck every last feather off those bastards.”

Growling under his breath, the Skeleton King lifted his head.

As expected, a flock of gulls had been circling above him for some time. They had apparently decided that humans were free cafeterias and had been following the little boat.

More precisely, they were flying somewhere far away while scattering their droppings and urine.

“They’ve got one hell of a sense of—”

The Skeleton King suddenly let his voice trail off, and his pupils began to tremble.

His eyes widened.

Across the opposite sky, a mass of flying creatures was approaching, blackening the heavens.

*Birds? All of those?*

As the Skeleton King stared blankly with his mouth hanging open, tens of thousands of birds of countless different species—so mixed together that even an ornithologist would have struggled to distinguish them—flew over his head and chased after the gulls already disappearing into the distance.

No.

That wasn’t it.

That was…

*They were fleeing.*

Together with those two words filling the Skeleton King’s mind, the calm sea began to heave.

*Rumble, rumble, rumble!*

A vibration rising from deep beneath the seafloor.

And then—

*Whooosh!*

A triangular wave surged upward as though it intended to swallow the world, a massive shadow undulating within it.

“GRAAAAAAAH!”

A savage roar shook the Philippine Sea.

The moment the three-hundred-meter-long monster of myth opened its jaws toward the feast laid out on the tiny boat—

“It’s been twenty-three hours. You piece of shit.”

Along with the unexpected voice of one man, a fierce flame shot forward, evaporating the moisture in its path.

*Thud!*



* * *



There is a martial art in the Murim called the Turtle Breath Technique.

To be precise, it is closer to a method than a martial art.

But what matters is that the Turtle Breath Technique can suppress breathing and heartbeat as much as possible, even lowering the body’s temperature.

In short, it is a strange method that erases a person’s vital energy for a certain amount of time. Since it also requires excellent internal energy and martial prowess, few people in the Murim learned it.

In fact, that was only natural if you knew anything at all about the strange species known as martial artists.

Even with their lives hanging in the balance, the Murim was crawling with show-offs who shouted the names of their forms as they fought. And you expected them to play dead?

In that world, where even rolling around on the ground could earn you a humiliating performance as people claimed you had achieved Great Completion in Narye tagon, the people who learned the Turtle Breath Technique were bound to be extremely limited.

The unorthodox faction.

Wandering martial artists.

And…

*Assassins.*

Unlike the two occupations listed above, assassins were such rare creatures that it was difficult to see one even once in your lifetime.

Even if an assassin brushed past your sleeve, you would not realize what they were.

And if you did recognize that the person standing before you was an assassin, you were already pretty damn screwed.

Still, meeting an assassin could sometimes be helpful.

Especially if that assassin’s epithet was the Slaughter Saint.



“I’m not sure what I should teach you. But I can’t exactly teach something like the Turtle Breath Technique to the Fire King’s successor…”

“Wow, the Turtle Breath Technique!”

“……?”

“Teach me! I want to live!”

“……Aren’t you from the orthodox faction?”

“Do orthodox martial artists not die even when they get stabbed?”

“No, but it would be better to further develop your martial arts…”

“Turtle Breath Technique! Turtle Breath Technique! Survival! Taekyung Grylls!”

“I understand, so please calm down. Stop spouting weird nonsense.”



In short, I had been lucky.

The living legend of the assassin world had teaching skills that could put even Daechi-dong’s top cram-school instructor[^2] to shame, and I was good at anything that involved using my body, so I absorbed his teachings like a sponge.

[^2]: Daechi-dong is a Seoul neighborhood famous for its intensely competitive private academies.

Of course, I had never dreamed that I would use the Turtle Breath Technique in the modern world before using it in the Murim.

But at least its effectiveness was unquestionable.

*Thud!*

A spear wreathed in blue-white flames was sucked into the dark monster’s maw.

No—it shattered the teeth that had already grown back and embedded itself in the roof of its mouth.

“GRAAAAAAAH!”

*Crack-crack-crack!*

As the enormous body thrashed with a roar, the little motorboat crumpled like a stalk of dried grass.

I grabbed the Skeleton King by the back of his neck as he stared at me with wide eyes, then kicked off from the sinking boat and shot upward.

*Boom!*

Fragments exploding behind me grazed my shoulder. Strong wind whipped across my entire body.

I stepped on an invisible staircase and came to a stop in midair.

*Grrrrr.*

Ragged breathing.

The pupils of Leviathan’s enormous crocodilian eyes narrowed into long vertical slits.

“You. How could you…”

“Ah, that? It’s a long story.”

I continued with a grin.

“And I have no intention of telling you.”

Inventory open. Summon.

Along with the thought that accompanied the words, I hurled the spear in my hand.

*Whoooooom!*

[^1]: Samgyeopsal is grilled pork belly, traditionally eaten with ssamjang, a savory dipping paste, and pa-chae, a shredded scallion salad.
## Chapter artifact 754

# Chapter 754

*Whoooooom!*

Ultra-high heat scorched the air and evaporated the moisture as it advanced.

A single streak of flame fell like a meteor. Leviathan’s eyes widened as it twisted its body, forgetting even the pain that had come before.

*Shhk!*

Hot.

The spearhead sliced clean through scales that could shrug off missiles. A mere graze sheared dozens of kilograms of flesh from Leviathan.

No.

It burned them away.

*Hissssss!*

Overcome by searing pain, Leviathan let out a silent scream.

From the day it first opened its eyes until now, the mythical monster that had reigned as the calamity of the sea had always found pain caused by fire unfamiliar.

Just like the human attacking it at a speed as swift as light.

*Shh-shh-shh-shhk!*

Leviathan did not know when or how the attack had been launched.

All it knew was that five streaks of flame shot forward with a sharp ripping sound, and a red warning light came on in its mind.

*Danger!*

The massive body that had frozen from pain twisted frantically.

After narrowly avoiding the flame-wreathed spears, Leviathan summoned its magical power.

*Ruuumble!*

A tremendous force pressed down from every direction.

Its wounds had not yet healed, but both the quality and quantity of its magical power far surpassed what they had been a day earlier.

A wave surged upward, filled to the brim with magical power, then advanced without any wind, responding to Leviathan’s will.

Toward the human who had dared to challenge the ruler of the sea.

And toward the traitor who attacked its own kind while wearing the skin of a worthless human.

*Whooooooosh!*

A massive shadow covered a radius of several hundred meters. Magical power churned within the pitch-black wave, where not even the faintest light could seep through.

“Damn it, I told you I don’t taste good…”

The Skeleton King muttered blankly.

At that very moment—

“Get lost.”

A low voice slipped through clenched teeth.

At the same time, the human—Jin Taekyung—thrust out a fist wreathed in flame.

*Boom!*

Flame-Extinguishing Divine Fist.

Blue-white flames erupted through the air and tore apart the center of the wave.

A small human figure shot through the collapsing spray. Leviathan let out an enraged roar.

—You bastard!

*Whoooooosh!*

Streams of water surged up from every direction and shot toward Jin Taekyung’s entire body.

Each one possessed enough power to pierce an aircraft carrier. Against an ordinary human, there was no point even discussing the result.

That was true if the opponent was really an ordinary human.

*Shhk.*

The air vanished. The wind split apart.

Flames bloomed at the end of a silver spearhead, distinctly different from the ones Jin had sent flying at Leviathan earlier.

*Fwoosh. Shhk!*

A blue line was drawn across the black sea.

Blue-white flames advanced smoothly like a dragon’s tail, burning away the streams of water that thrust toward Jin like spears.

Jin Taekyung stepped on empty air once more and accelerated. Within the slowed passage of time, he steadied his breathing.

*My body…*

It was different from usual.

His hands and feet felt heavy today, his speed was slower than before, and his internal energy was being consumed much faster than he had expected.

*That damn debuff.*

The effect of **Broken Body** on the battle was enormous.

It might have been different if he had never possessed those capabilities in the first place. But with every attribute except Intelligence drastically reduced, the resulting void left his body unable to properly carry out the commands from his mind.

Just like now.

*Thud!*

His body shook from a dull impact.

Jin swallowed his groan and evaded the attack that came immediately after.

*Boom! Boom! Boom!*

Hundreds of spheres of water came rushing toward him, covering his field of vision.

They resembled the attack spell mages called Water Ball, but Jin Taekyung knew better than anyone that the power contained within them was incomparable to any ordinary Water Ball.

He also knew that the moment he retreated here, he might lose sight of the monster in front of him once again.

*Whoooom.*

The nearly translucent white shaft of the spear trembled.

The flame that had seemed ready to die out surged violently, announcing its presence.

Jin Taekyung swung the divine weapon, drawn far back, down at an angle.

Fire Dragon Divine Spear, second form.

Heavenly Strike.

*Fwoooooosh!*

A dazzling flash illuminated the darkness that had already swallowed the surrounding area.

The hellfire falling through the air evaporated the countless spheres of water filling every direction, and the monster’s enormous eye was stained reddish.

—How dare you! How dare a mere human…!

Along with the scream, Leviathan drew up all of its magical power.

*Ruuuuumble.*

The sea heaved, and the dark clouds hanging overhead let out a groan.

At the moment the spearhead met the barrier of magical power wrapped around Leviathan like a shield, a dazzling flash spread across the blackened sky.

Toward the human who had dared to stand against a myth.

*Fwoosh!*

Within the slowed world, dozens of bolts of lightning plunged down from the distant sky.

They emerged as dozens, but by the time they reached their destination, they had merged into one. That destructive force of nature was sucked toward a single point as though drawn there by something.

*Crackle, crackle, crackle!*

“Gyaaaaaaaah!”

The sea was dyed with countless flashes, accompanied by a scream filled with horrific pain.

Leviathan had been using all its magical power to hold back the spearhead, and joy filled its mind.

*As expected!*

The voltage reached billions of volts.

No matter how strong the human was, he could not possibly remain unharmed after taking a direct hit from that pillar of lightning—

*What?*

Leviathan’s enormous eye blinked.

Beyond the slowly fading flash, the human who should have been standing there with his flesh burned and his bones shattered by the lightning was staring back at Leviathan completely unharmed.

He even spoke, his expression slightly embarrassed.

“Uh, he’s always been a scaredy-cat.”

—…?

“Hey, cut it out. You’re not going to die from that.”

What?

Leviathan tilted its head without realizing it.

Over Jin Taekyung’s shoulder, a being screaming horribly appeared in the monster’s pupil.

“Gyaaaaaaaah…”

The scream gradually grew quieter.

The Skeleton King glanced over his body, which was giving off wisps of smoke, then awkwardly lowered the sword he was holding.

“Ah, right. I am a skeleton.”

“That was some great timing. The lightning-rod strategy was good.”

“I only drew this to help you… No, as expected, you saw through my strategy perfectly. Not bad.”

—…!

What the hell were these bastards?

Unable to process the situation, Leviathan’s mind grew hazy for a moment.

That instant of distraction was enough to disrupt the flow of magical power that had been as solid as a wall with no gaps.

*Crack!*

A tiny fissure compared to the whole.

But it was exactly the opening Jin Taekyung had been desperately waiting for, and the flame dwelling in the spearhead smashed through the wavering magical power and plunged toward its target.

*Thrust!*

The spearhead shattered the scales. Amid the horrific pain of flesh and bone catching fire, Leviathan thrashed instinctively.

—GRAAAAAAAH!

*Rumble! Whoooooosh!*

The enormous body writhed madly.

But Jin Taekyung was not satisfied.

Grabbing the small horns scattered across the monster’s skin, he poured even more strength into the spear clutched tightly in his hand.

*Shhhhuuuk!*

The spear shaft, nearly two meters long, dug into the center of Leviathan’s brow.

Its enormous head saved it from death, but the mythical monster, dominated by pain unlike anything it had ever experienced or even imagined, let out a terrible roar.

—You bastard!

*Whoooooosh!*

A terrifyingly powerful Fear spread outward from Leviathan.

Marine creatures crouching in the deep sea rolled their eyes back and floated upward, while countless birds fleeing far away after sensing the danger that was about to arrive suddenly fell from the sky.

At this moment, Leviathan was angrier than it had ever been.

*I’ll kill them. I must!*

It had to tear them apart so completely that no one would be able to recognize them.

The human bastard who had inflicted this pain upon it and the traitor who had betrayed its own kind both deserved the most horrible deaths.

But within the emotions of pain and anger dominating Leviathan, fear suddenly raised its head.

*But how?*

The enemies had not only inflicted such a massive wound upon it the day before—they had deceived its senses and lured it into a trap.

And that human in particular…

That tiny creature that had dared to drive a weapon into its head possessed a power Leviathan could not understand at all.

*Strong. Stronger than any human I have ever seen.*

This would have been unimaginable during the Great Cataclysm.

Leviathan had roamed the five oceans, sending countless lives to watery graves. Even the humans considered the strongest had failed every time they tried to hunt it.

No.

Leviathan had always been the one doing the hunting.

It had been born a ruler and lived as a predator.

In this vast ocean, it had always been the predator, while humans were nothing more than prey that could be swallowed in a single bite.

Even after looking back across its distant lifetime, Leviathan could remember only one being who had ever made it submit.

The master to whom it had sworn loyalty.

The Demon King, Asmodeus.

—…!

In that instant, Leviathan’s eyes, stained with pain and anger, opened wide.

*Could this bastard be…?*

It had definitely heard of him before.

Of a human who had opposed its once-mighty master.

Though Leviathan had never once encountered that human, he had proven his strength by defeating countless monsters, ending with the great name of the Demon King Asmodeus.

*Then could this human really be…?*

There was no mistaking it.

There could not be two humans this strong.

Leviathan’s misunderstanding swelled into fear.

Before it knew it, the anger had disappeared, replaced by a single thought.

*I have to run. As far away as possible. I have to get away from him!*

Anger? Fighting spirit?

None of that mattered. If this human had defeated the Demon King Asmodeus, whom Leviathan had served as its master, then its own fate was practically decided.

—GROOOOOOAR!

Leviathan let out a massive roar and shook its body.

Its movements, no longer driven by pain but by the struggle to survive, were more violent than ever. But they had no effect on the figure who had already made a nest on its enormous body.

“Shut up. Shut up. Aren’t you going to shut up?”

*Bam! Bam! Bam!*

Blood splattered and flesh was crushed.

Under his tremendous grip, the incredibly tough scales were yanked out like cabbages, while the flames riding his punches crushed flesh and bone.

*Thud. Crack!*

—Kuhk. Khk.

The successive waves of pain nearly drove Leviathan unconscious.

The strength was so immense that it was impossible to imagine its wielder as human.

In the end, only one path remained.

The deep sea.

The place where Leviathan had first opened its eyes. An unknown domain deep beneath the ocean that no enemy had ever been able to invade.

If it reached that place, even this tenacious and terrifying human would be shaken off.

*Whoosh!*

Spray surged upward.

Leaving the shallow waters and advancing into the open sea, Leviathan swam deeper.

Then, the next moment, it saw the smiling face of the human and realized that its guess had been wrong.

“Now we can finally fight together.”

What?

A single question flashed through Leviathan’s mind.

At that moment—

*Whoooooosh!*

Deep within the abyssal darkness of the seawater, countless things gathered into one and blocked Leviathan’s path.

Bones.

They were bones.

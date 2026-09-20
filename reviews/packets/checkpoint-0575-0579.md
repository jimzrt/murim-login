# Checkpoint Review — 575–579

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

# Chapters 575–579

## Plot

Jin Taekyung kills the Lv. 140 King of the Black Sea Kraken, saving Busan survivors but failing to identify the humans who empowered it. As rescue efforts continue, President Baek Hanseong seeks to bring Taekyung and Choi Minwoo into his political camp. Choi instead leaves to meet Song Cheonwoo, who warns that Go Jun has prepared a trap involving Choi’s maternal grandfather, Cheon Taemin.

Inside the Peace Guild’s Yeti’s Winter Range Gate, Song reveals that Taemin suddenly collapsed more than twenty years ago and was secretly kept alive while Lee Jungryong and Song concealed his condition, conducted experiments, and purged informed aides. Song claims Taemin is still alive and may be in Ares Guild’s restricted Area A, though he cannot confirm the location. Before Choi can verify the story, Song’s Yeti’s Necklace draws hundreds of yetis into an ambush. Kim Hwajong diverts the monsters while Choi fights Song.

Choi defeats Song with Hero’s Soul and keeps him alive as a witness. Song explains that Go Jun seized his children, forcing him to attack Choi, and confirms that Taemin remains alive but unconscious. After receiving treatment, Song uses a potion-enhanced burst of strength to escape into a crevasse, leaving his whereabouts unknown.

## Continuity

- The Kraken is dead, but the humans who empowered and released it—and whether they deliberately caused the Monster Wave—remain unidentified.
- More than one thousand Mermen remain around Haeundae and Gwangalli while the Peace Guild and other forces contain Busan’s disaster.
- Cheon Taemin collapsed more than twenty years ago and has remained unconscious; the cause and the events surrounding his condition are unknown.
- Song Cheonwoo and Lee Jungryong concealed Taemin’s condition, experimented on him, and purged aides who knew the truth. Song survived by accepting the European regional director position.
- Song claims Taemin is alive and may be held in Ares Guild headquarters’ Area A, but Area A remains an unconfirmed location.
- Go Jun has seized Song’s children and is preparing a separate trap involving Choi’s maternal grandfather.
- Choi defeated Song and preserved him as a witness, but Song escaped into a crevasse after being treated.
- Kim Hwajong remains Choi’s loyal butler and considers himself Choi’s only family.

## Translation Decisions

- Retain **King of the Black Sea Kraken**, **Monster Wave**, **Area A**, **Hero’s Soul**, **Yeti’s Necklace**, **Yeti’s Winter Range**, **Stone King**, and **Skeleton King**.
- Use **Hwa-jong** for 화종 and **Hyung** for Song’s address to Cheon Taemin.
- Use **crevasse** for 크레바스 and **mid-grade potion** for 중급 포션.
- Preserve the distinction between **dragonkin** attracted by the Yeti’s Necklace and **yetis**, who recognize its wearer as one of their own.

## Durable state

{
  "active_continuity": [
    "Song Cheonwoo says Cheon Taemin suddenly collapsed more than twenty years ago and has remained unconscious, but no one knows why.",
    "Song Cheonwoo and Lee Jungryong concealed Taemin's condition, waited two years, conducted experiments, and purged aides who knew the truth.",
    "Song survived by negotiating the European regional director position and saving his family.",
    "Hwa-jong was not told about Taemin's condition and remains loyal to Choi Minwoo.",
    "Song claims Taemin is still alive, but his location is unknown and Area A is only suspected.",
    "Choi Minwoo has confirmed Song's account enough to treat Taemin's status as genuine while continuing to investigate.",
    "Busan's Kraken has been eliminated, but more than one thousand Mermen remain across Haeundae and Gwangalli while the Peace Guild and other forces contain the disaster.",
    "Song Cheonwoo warned Choi Minwoo that Go Jun is preparing a trap related to Choi's maternal grandfather.",
    "Go Jun seized Song Cheonwoo's children as leverage, forcing Song to attack Choi despite their temporary alignment against Go Jun.",
    "Song Cheonwoo used the Yeti's Necklace to bring hundreds of yetis into the confrontation; Kim Hwajong diverted them while Choi fought Song.",
    "Choi Minwoo defeated Song Cheonwoo with Hero's Soul and kept him alive as a witness.",
    "Song survived treatment and escaped into a crevasse, leaving his location unresolved."
  ],
  "continuity_sources": [
    579
  ],
  "open_questions": [
    "What caused Cheon Taemin's collapse, and what happened during his more than twenty years of unconsciousness?",
    "Is Cheon Taemin actually being kept in Area A of Ares Guild headquarters?",
    "What trap is Go Jun preparing, and can Song Cheonwoo's warning be trusted?",
    "Who empowered and released the Kraken, and did that person engineer the Monster Wave?",
    "Where did Song Cheonwoo go after escaping into the crevasse, and can he be recovered as a witness?"
  ],
  "safe_through": 579,
  "temporary_decisions": [
    "Use Yeti's Winter Range for 예티의 겨울 산맥.",
    "Use Stone King for 스톤 킹 and Skeleton King for 스켈레톤 킹.",
    "Use Area A for A구역.",
    "Use Hwa-jong for 화종.",
    "Use Hero's Soul for 영웅의 혼, Yeti's Necklace for 예티의 목걸이, and Hyung for 형님 when Song addresses Cheon Taemin."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 575

# Chapter 575

There was no need to confirm it with my own eyes or run over and check for a pulse.

The moment the blue-flame-wreathed spearhead pierced the Kraken’s body, I realized it.

*It’s over.*

*Slash! Boom!*

A severing strike. At the same time, fire qi exploded from within.

The head of the monster, which measured more than ten meters from top to bottom, burst like a balloon. Blue blood that had not yet evaporated poured down over the surface of the sea like a sudden shower.

And then—

*Whoooooosh—*

Along with the Kraken’s enormous body finally collapsing, a clear chime rang in my ears.

*Ding.*

> **System**
>
> You have defeated Lv. 140 ‘King of the Black Sea’ Kraken!
>
> You have gained a large amount of EXP!
>
> **Myriad-Poison Ring** has detoxified all poison within your body!
>
> Status Abnormality: **Poisoned** disappears!
>
> Status Abnormality: **Paralyzed** disappears!

Even after the System notified me that I had defeated the Kraken, my mouth felt gritty, as though I were chewing sand.

*Damn it.*

I should have kept it alive. Somehow, I should have kept it alive and learned the true identity of whoever was behind it.

But a moment of carelessness had brought about irreversible consequences, and the Kraken had died while leaving behind an unsolved mystery.

If it had attacked me directly, there would have been a good chance of keeping it alive, but…

*It’s too late.*

The Kraken had been more intelligent than I expected.

It knew that even while poisoned, I was stronger than it was. It also understood that it could never escape.

That was why it had targeted the survivors instead of me. It had chosen death over capture.

And when faced with the Kraken’s final desperate struggle, I had only one choice left.

“……Phew.”

I sighed as I looked at the Kraken’s corpse, half-submerged in the sea.

It had been an unavoidable choice. If I had not killed it in a single strike, someone would have died right in front of me.

People talked about sacrificing the small for the sake of the greater good, but that was just a pretty phrase. In the end, it was still a sacrifice—doing nothing while someone died pointlessly, despite having the power to prevent it.

*I should never have let my guard down until the very end…*

But the water had already been spilled.

I was anxious and regretful that I had ultimately failed to uncover the truth behind the disaster. But I did not regret killing the Kraken.

People had survived because of my choice.

“Th-there! Please, someone save us!”

“Cough! Please, my child…”

“Mom! Mooooom!”

Perhaps it was because we had fought as far away from them as possible.

Hundreds of casualties had already occurred before I could even arrive, but the survivors still waiting to be rescued outnumbered them.

The desperate cries of the people carried across the rolling sea and the collapsed Gwangan Bridge. I forced myself to shake off my exhaustion and launched myself forward.

*Fwoooooosh!*

The salty yet refreshing scent of the sea seeped deep into my nose.

I became a gust of wind and raced across the surface of the water.

After leaping over the Kraken’s floating corpse and reaching the people, I quickly pulled them to safety and spoke to them.

“It’s dangerous, so everyone needs to stay here. Those of you who still have the strength, help me rescue the others first.”

A young man who looked relatively unharmed spat out seawater before speaking.

“Cough. B-but we should still run somewhere else…”

“Run?”

“Y-yes.”

I raised a hand and pointed toward the distance.

Black smoke billowed up between the dense forest of buildings surrounding us.

These ordinary civilians could not hear it, but my senses had developed far beyond human limits. I already knew.

—Hssssss!

—Tank! Three steps forward!

—The building! The building is collapsing! The civilians are in danger!

—Aaaaaagh!

*Rumble! Boom!*

Faint screams and thunderous crashes reached my ears. They were proof that a city battle between humans and monsters was taking place not far away.

And not just in one place. Fighting was breaking out simultaneously throughout the surrounding area.

“There are monsters waiting in every direction. Do you still want to go?”

“……No. I’ll stay here.”

At least he understood quickly.

Even though the Kraken was dead, it was not over.

To completely bring this chaos under control, I was going to have to spend the rest of the day extremely busy.

*Fwoooooosh! Boom!*

The survivors watched, dazed, as I kicked off the surface of the water and shot into the sky.

* * *

Everyone ate.

But it was impossible to deny that the level of formality changed depending on who one ate with and where the meal took place.

In that sense, today’s meal, shared by only two people sitting across from each other, had been highly formal.

The late-starting breakfast had continued for a full two hours amid quiet conversation. By then, a beautifully decorated dish of sujeonggwa[^1] had been placed on the spotless white tablecloth.

“Since Seollal is just around the corner, I had tteokguk prepared… I’m not sure whether the meal suited your taste, Team Leader Choi.”

At the polite yet gentle voice, Choi Minwoo wiped his mouth with a napkin before replying.

“Perhaps because you took such care, Mr. President, but it was excellent.”

“Ha-ha. I’m glad to hear it.”

The middle-aged man seated across from him, President Baek Hanseong, continued with a genial smile.

“You’ve been so busy lately that I was worried you weren’t eating properly. So I repeatedly impressed upon the head chef here at the Blue House that you were an important guest and that he needed to take special care with your meal.”

Calling him an important guest was not mere flattery.

Being invited to a Blue House breakfast already meant that someone was an influential figure with considerable power. But a meal shared by only two people carried an entirely different meaning.

It showed just how important Baek Hanseong considered Choi Minwoo.

“You eat well. It’s nice to see. Makes me proud, too.”

Choi Minwoo lowered his head slightly.

“Thank you. Still, I don’t go hungry as often as you seem to think, Mr. President. I feel I may have caused you unnecessary concern.”

“Oh, is that so? Well, I suppose you have a personal chef as well.”

“No. There’s someone who takes care of my meals separately these days.”

“Someone who prepares your meals separately… Ah, could it be?”

Choi Minwoo gave a small nod.

“Mr. Jin Taekyung’s mother prepares my meals.”

“Oh. His mother does it herself?”

“Yes. I tried to refuse because it didn’t seem right, but she’s remarkably stubborn.”

President Baek Hanseong let out a quiet exclamation.

He already knew that Jin Taekyung’s family was temporarily staying at Choi Minwoo’s estate, but hearing it directly from the person involved gave the matter a different significance.

*If she goes as far as preparing his meals… They’re even closer than I thought.*

Jin Taekyung and Choi Minwoo. Choi Minwoo and Jin Taekyung.

From President Baek Hanseong’s perspective, the two men were not only enormous fish he could never afford to let go, but also the only means of restraining the Ares Guild, which wielded tremendous influence.

Jin Taekyung, a man of extraordinary stature.

Choi Minwoo, Cheon Taemin’s maternal grandson and only living blood relative.

If he joined forces with those two, he could rise to an even higher position.

After becoming the youngest president in Korea’s history, he had a very real chance of becoming the first president to win reelection under the amended law.

*No matter what it takes, I have to make those two my people.*

While President Baek Hanseong entertained thoroughly political thoughts, Choi Minwoo was thinking about something completely different as he drank his coffee.

*The dinner she said she’d make tonight was… kimchi stew, wasn’t it?*

It was strange. He had just finished eating, yet he felt as though his stomach were completely empty.

The kimchi stew made by Jin Taekyung’s mother sounded more appealing than the tteokguk prepared with painstaking care by the head chef of the Blue House, one of the finest Korean-cuisine masters in the country.

Fluffy white rice cooked in an old-fashioned pressure cooker, something rarely seen these days, alongside pork and fully fermented kimchi.

And the people huddled around the same table, frantically moving their spoons.

*Hmm.*

As Choi Minwoo realized he was unconsciously smacking his lips, he let out a faint, bemused laugh.

*I see. So that’s what it was.*

He did not particularly like either tteokguk or kimchi stew.

The reason he looked forward to dinner was not because her cooking was better than the Blue House chef’s.

It was simply that he liked that place. The warm food. The place where he could eat with warm-hearted people.

*Home.*

And family.

For Choi Minwoo, those two words referred to something he had lost when he was shorter than the chair he now sat in. Something he had believed he would never be able to reclaim.

*No. If we’re talking about family, there is still one person left.*

A hero who had saved humanity. A living savior.

And yet, a man who had failed to protect his own family.

As he thought of his maternal grandfather—the last time they had met was too distant for Choi Minwoo to remember—he spoke inwardly.

*Soon… I’ll be able to see you again.*

At the thought of his maternal grandfather, who had shut himself away from the world for decades, an emotion he could not identify suddenly rose within him.

Noticing that Choi Minwoo’s mood had changed, President Baek Hanseong asked with concern, “Is something troubling you?”

“Ah. No. It’s nothing.”

“Ha-ha. I see. Well, now that we’ve finished eating, there’s something important I wanted to discuss with you, Team Leader—”

*Bang!*

But President Baek Hanseong could not finish his sentence.

When he saw the aide entering without knocking, his brow furrowed.

“I told everyone not to come in.”

“I’m sorry. I tried not to, but I couldn’t reach you…”

“Reach me? Of course you couldn’t. I put my phone on silent.”

This was a place where important matters were being discussed. Considering their respective positions, taking out a smartphone would have been extremely discourteous.

“Huuf. I’m sorry. But this was an emergency.”

The aide was breathing heavily, sweat beading on his forehead.

Sensing that something serious had happened, Choi Minwoo pulled out the smartphone tucked inside his suit jacket.

There were more than ten missed calls from Butler Kim, along with a pile of text messages.

A sense of foreboding surged up from the depths of his heart.

*Don’t tell me…*

The moment he checked the messages, his perfectly groomed eyebrow twitched.

> **Butler Kim**
>
> **Butler Kim**
>
> Emergency Monster Wave in Busan
>
> Extra-large named monster sighted
>
> Young Master, where are you?
>
> Young Maㄴter

The sender was Butler Kim.

The messages were short, but their contents were anything but trivial.

*A Monster Wave. In Busan, of all places?*

Busan was Korea’s second-largest city, home to millions of people. If an extra-large named monster merely did a forward roll, it would cause an enormous loss of life.

And the situation was even worse than that, as the aide’s next words revealed.

“The emergency alert was delayed for about ten minutes. The Monster Wave happened so suddenly, and the Gate management office and all the surrounding facilities were destroyed…”

“You idiot! Do you hear yourself?”

“I-I’m sorry.”

The aide, sweating profusely, continued.

“But according to the report that came in one minute ago, the extra-large named monster has been subdued. Hunter Jin Taekyung happened to arrive at the scene just in time…”

“What? Are you certain?”

“Yes. Absolutely. The remaining monster groups are being cleared, and survivors are being rescued.”

“……Phew. At least that’s a relief.”

President Baek Hanseong exhaled in relief, while Choi Minwoo rose from his seat without hesitation.

Even if the immediate crisis had been contained, this was not a situation where he could leisurely sit around and chat.

“I’ll be going now, Mr. President.”

“All right. We’ll continue our conversation another time.”

After exchanging a brief farewell, Choi Minwoo had just left the Blue House when—

*Bzzzzzt.*

The smartphone he had turned back on began vibrating forcefully again.

Having already guessed who was calling, Team Leader Choi answered immediately.

“Yes, Butler Kim. I’m on my way ri—”

—It’s me.

“……!”

Choi Minwoo’s footsteps stopped dead.

Song Cheonwoo’s aged voice rang out from the other end of the phone.

—Let’s talk for a moment. It’s urgent.

[^1]: Sujeonggwa is a traditional Korean cinnamon punch, commonly served chilled with dried persimmons and pine nuts.
## Chapter artifact 576

# Chapter 576

*Click.*

The short call ended. The signal ringing from the smartphone stopped, but the hand Choi Minwoo had raised to his ear did not come down easily.

With a conflicted look in his eyes, Choi Minwoo crossed the Green Garden spread out before the Blue House residence.

Unlike before, his steps had slowed because of a certain thought filling his mind.

*Song Cheonwoo wants to meet me. And he wants to meet right now.*

Song Cheonwoo.

The Trojan horse who would let him enter the impregnable fortress known as the Ares Guild.

It was true that he had been waiting for Song's contact, but he had not expected it to come today—or for Song to demand a meeting immediately.

Choi Minwoo recalled the brief conversation and muttered inwardly.

*What should I do?*

Then Choi Minwoo's footsteps stopped dead.

Two paths had opened before him. It was as though another fork had appeared in his heart.

*Busan. And Song Cheonwoo.*

There was no time. He had to choose.

Choi Minwoo stared at the two paths with deeply sunken eyes. At last, he began walking.

*Crunch.*

The frozen grass crumbled beneath the heels of his dress shoes. Though the path had split in two, every road ultimately led to the exit.

Outside the main gate, beside the Blue House security office, a familiar face was already waiting for him.

“Young Master.”

Choi Minwoo greeted Butler Kim with a nod before stepping through the gate.

A sleek limousine, five black SUVs, and around twenty Hunters were waiting by the roadside.

They were all skilled enough to be called the elite of the Peace Guild, which now boasted considerable strength.

The various pieces of Equipment they already wore were proof that they were fully prepared for battle.

Butler Kim's next words turned Choi Minwoo's suspicion into certainty.

“We were waiting to escort you.”

“I’m sorry. Given where I was, I failed to check in time. More importantly, I heard that Mr. Jin Taekyung defeated a named monster. What is the current situation?”

“As you said, the named monster that appeared during this wave, the Kraken, has been eliminated. However, over a thousand Mermen have spread throughout Haeundae and Gwangalli.”

Choi Minwoo muttered in a low voice after hearing Butler Kim's answer.

“The damage must be severe.”

Busan might not have been as large as Seoul, but it was still a major city with a population approaching five million, worthy of being called Korea's second-largest city.

The appearance of a thousand monsters—monsters made even stronger by the recent rise in magic power—in such a place was nothing short of a disaster.

But Butler Kim calmly shook his head.

“It is not something we should celebrate, but fortunately, the number of casualties is far lower than expected.”

“Even if Mr. Jin Taekyung defeated the Kraken, he could not have stopped all one thousand Mermen.”

“There was Skel—no. The Stone King was there.”

“Ah.”

The face of the blond foreigner who always wore an arrogant, self-assured expression flashed before Choi Minwoo's eyes. He gave a small exclamation and nodded.

*If he was there, it was possible.*

The existence of the undead monster suffering an identity crisis between monster and American was a secret known only to a very small number of people.

Choi Minwoo also knew that the Stone King was a powerful being who was in no way inferior to an S-rank Hunter.

“Yes. Fortunately, thanks to the efforts of those two, the damage is not particularly severe.”

It could only be called good fortune.

Jin Taekyung and the Skeleton King were both powerful enough to be called one-man armies.

And unlike the Skeleton King, who was subject to various restrictions despite his abilities, Jin Taekyung was one of the strongest people in Korea.

No—in the entire world.

*Except for one person…*

Choi Minwoo muttered inwardly before speaking.

“What about our Peace Guild?”

“Approximately five minutes ago, we dispatched an emergency rescue team and three prepared teams to Busan. The Guilds and Hunters based in Busan, as well as outside reinforcements, are doing everything they can to prevent the damage from spreading.”

Choi Minwoo knew the number of Gates in Korea, along with the number of Guilds and Hunters in every region, by heart.

He finished his calculations after blinking several times and asked abruptly,

“Containment will be complete within two hours at the latest. Correct?”

“That is correct. Of course, rescuing the victims after containment will also take considerable time, but…”

“Then, given the current situation, calling in Mr. Jin Taekyung or the Stone King would be difficult.”

“Forgive me, Young Master, but what do you mean by calling them?”

“It is nothing. Let us depart.”

Despite his quiet, decisive reply, Choi Minwoo's lips moved as he walked toward the limousine.

What now deserved to be called Sound Transmission rather than message magic pierced Butler Kim's ear.

—He has requested a meeting.

“……!”

Butler Kim's eyes trembled slightly. Even without a name, there was no mistaking whom *he* referred to.

—Song Cheonwoo?

—Yes.

—Young Master. It may be dangerous. The Busan Monster Wave is already nearing its end. It would be safer to go to the Guild House instead—

—He spoke about my maternal grandfather's safety. He also said that Go Jun was laying a trap.

Choi Minwoo looked at Butler Kim's rigid face and continued the Sound Transmission quietly.

—I have to meet him. Right now.

* * *

The B-rank Gate in Pyeongchang, Gangwon Province, known as *Yeti's Winter Range* was not a particularly appealing raid site for Hunters.

No matter how outstanding their physical abilities were or how much Magic Equipment they possessed, fighting furry giants on a snow-covered mountain where their feet sank deep with every step was hardly pleasant.

That did not mean everyone avoided *Yeti's Winter Range*, however.

Even amid the recent, successive rises in magic power, some Hunters still visited the Gate. The group that had just ridden the lift down belonged to that category.

“Damn it. Why did they suddenly prohibit entry?”

“I know. But, Team Leader, are we getting paid today?”

“……You’re worse than a yeti. We couldn’t even enter the Gate because of the rise in magic power, and you’re asking about pay? Don’t you have any conscience?”

“Aw, I got my hopes up for nothing. By the way, who were those people up there? The handsome guy wearing the mask looked kind of familiar.”

“I don’t know. How would I know—huh?”

The thirty-odd Hunters were coming down while grumbling. The Team Leader walking at the front suddenly opened his eyes wide.

At the end of his gaze, a man was walking up the path at neither a fast nor slow pace.

“Tsk, tsk. Looks like he’s going to strike out too.”

It was obvious at a glance that the man had come for a raid. The Team Leader spoke to the middle-aged man who looked to be in his forties.

“Yeti raid?”

The middle-aged man stopped for a moment at the two words thrown abruptly at him, then nodded without a word.

The Team Leader clicked his tongue and continued.

“Looks like you’re striking out too, Boss. Don’t go up. It’s blocked.”

“……”

“They say the magic power reading suddenly went up or something. Anyway, entry’s prohibited. That’s why we got turned back too.”

“……”

“……Sir? Did you hear me?”

The Team Leader frowned when he sensed something strange. Without answering a single word, the middle-aged man who had merely listened to him walked past the group.

*Step. Step.*

As the middle-aged man's figure receded, the Team Leader muttered,

“What the hell was that guy?”

To the middle-aged man, however, the Team Leader's goodwill was nothing more than needless meddling.

*Clatter.*

The man rode the lift up with a slight jolt and found dozens of pairs of eyes waiting for him.

A Hunter who appeared to be quite powerful stepped forward to block the unwelcome visitor.

“Sorry, but due to the rise in the magic power reading, you cannot enter the Gate—”

“He’s my guest.”

At the quiet voice that interrupted him, the twenty-odd Hunters standing like a wall split apart to make way.

At the end of the path they created stood two people.

“You’re late.”

At Choi Minwoo's flat voice, the middle-aged man whose appearance had been changed by an illusion spell—Song Cheonwoo—finally parted his tightly closed lips.

“I had to be careful. And wasn’t this place chosen by you, Minwoo?”

“I was not the one who asked to meet at a Gate first. In that case, I see no problem with choosing the location myself.”

“We had no choice if we wanted to avoid wiretapping and possible surveillance. Once we enter the Gate, all of that becomes useless.”

“Then there should be no problem. This Gate belongs to the Peace Guild. It is an ideal place for both of us to be cautious.”

“……Both of us? Are you saying you suspect me?”

Butler Kim, who had been standing quietly behind Choi Minwoo, answered instead.

“Then why should the Young Master trust you?”

“Come now, Hwa-jong.”

“Do not presume to call me by my name. Our relationship ended long ago.”

“……!”

At Butler Kim's eyes, cold as a glacier, Song Cheonwoo's eyelids trembled.

There had been a time when the two men had treated each other like brothers. But they had parted ways at the fork between loyalty and ambition.

As an icy chill settled between them, a quiet voice rang out.

“More importantly, I believe there is something we need to discuss first.”

With that gentle but incisive remark, Choi Minwoo looked back and forth between the two men, who had both taken a step away from each other.

The Gate entrance, shimmering with a field of magic power, stood behind him.

“You two will enter the Gate with me. The other Guild members will prevent any possible intrusion from outside.”

Choi Minwoo took the first step. Butler Kim and Song Cheonwoo followed him.

*Whoooooosh.*

Cold, sticky magic power wrapped around their entire bodies. When they opened their eyes again, a world drenched in white stretched out before them.

*Yeti's Winter Range.*

Snowdrifts filled every direction. Somewhere amid the steep slopes, a monster's roar rang out.

—Kraaaaaaaar!

Yet the three men remained unmoved by the bitter cold and chilling roar.

They were far too powerful to be frightened by a mere yeti. More importantly, they had come here not for a raid, but to have a private conversation.

“Speak now. About my maternal grandfather's safety. And about the trap Go Jun is preparing.”

At Choi Minwoo's direct demand, Song Cheonwoo gave a bitter smile.

“Although I have not watched you for long… your personality has not changed.”

“Get to the point. I do not think that is a difficult request.”

Song Cheonwoo let out a shallow breath. His white breath rose through the wind, mingling with his suddenly aged voice.

“Would you walk with me for a while? I want to speak with you alone.”

Butler Kim furrowed his brow, while Choi Minwoo answered calmly.

“Is that really necessary?”

“You seem to suspect me.”

“I have no reason to trust you, either.”

“This Gate belongs neither to me nor to Ares, but to the Peace Guild. You chose it yourself. How could there be a trap?”

“……”

“I am not foolish enough to scheme against my only collaborator.”

Choi Minwoo had been staring at some distant point in the snowy mountains when he suddenly turned his head.

He gazed silently into Song Cheonwoo's eyes, which showed not the slightest hint of wavering, then spoke in a low voice.

“Very well.”

“Young Master.”

“Do not worry. I will not go far.”

“……Then I will follow at a distance from behind.”

Song Cheonwoo nodded and slowly drew the weapon at his waist.

“I suppose you cannot stop even that. Do as you please.”

“You……!”

“Do not misunderstand.”

*Thud.*

What Butler Kim had feared did not happen.

Song Cheonwoo deliberately drove his weapon deep into the snow. Choi Minwoo took the first step.

*Crunch. Crunch.*

The snow crumbled beneath the footsteps of the two men walking side by side.

How many steps had they taken?

Song Cheonwoo's tightly closed lips finally moved.

“There is a secret area inside the Ares Guild headquarters that only a very small number of people can enter.”

“Are you referring to Area A?”

“……!”

Song Cheonwoo's eyes widened at the unexpected question.

Choi Minwoo continued in a calm voice.

“I knew about the existence and name of the secret area. Anything beyond that was impossible, however.”

“……Your abilities are impressive. How did you find out?”

“I put in more effort than you can imagine. And what I need from you now is not praise, but more detailed information. What connection does it have to my maternal grandfather's safety?”

“Because that person is there.”

*Crunch.*

At the two words referring to someone, the footsteps that had been moving forward without hesitation stopped dead.

After a brief silence, Choi Minwoo began walking again.

“That information is not certain.”

“Why do you think that?”

“You were pushed out of the Ares Guild's inner circle long ago, Director Song.”

“……That hurts. But what you say is true. It is not certain information.”

“I have also been unable to find any reason for my maternal grandfather to be there. No—I cannot understand it.”

“A reason……”

Song Cheonwoo let out a small sigh before continuing.

“You would not be able to understand. No one, including you, knows what happened to him.”

“What does that—”

Choi Minwoo turned to him with a questioning expression. Then, at the next words, he froze.

“It happened more than twenty years ago. That person lost consciousness.” 

“……!”
## Chapter artifact 577

# Chapter 577

Choi Minwoo’s face had gone rigid. His eyes, fixed on Song Cheonwoo, trembled faintly.

“What… do you mean?”

“You may not believe me, but it is an undeniable fact.”

Song Cheonwoo continued with a sigh.

“It happened suddenly one day. No one saw it coming.”

“……!”

Without realizing it, Choi Minwoo clenched his fists.

He had never trusted Song Cheonwoo in the slightest, but he could not sense even a trace of falsehood from the old man standing before him.

*Then is it really true?*

For an instant, Choi Minwoo’s heart sank with a thud. A bead of cold sweat had formed before he knew it, rolling down the back of his neck.

A voice barely escaped between his tightly pressed lips.

“But I’ve never heard anything like that from anyone. Not even Butler Kim, who was my maternal grandfather’s closest aide…”

Before Choi Minwoo could finish, Song Cheonwoo shook his head.

“He did not choose not to tell you. He could not.”

“Then…”

“I am sorry.”

There was a difference between choosing not to do something and being unable to do it.

Only one character separated the two phrases, but the difference was enormous. Realizing what Song Cheonwoo’s words meant, Choi Minwoo glared at him.

“You hid it from Butler Kim too? Something this important?”

The septuagenarian quietly nodded. His voice, suddenly much older, forced its way between his lips.

“Hwa-jong. That man was always loyal. And he gave that same loyalty, whole and undiminished, to a life born after the war ended. A young child who lost his parents in an unfortunate accident and was left all alone.”

“……!”

“Even on the day everything changed, your grandfather’s most loyal aide was at your side.”

Choi Minwoo turned his head without realizing it.

A figure standing far away in the snow came into view, staring directly at them.

Had Song Cheonwoo’s voice not been swallowed by the howling blizzard, that loyal servant would have flown over and tried to kill the traitor.

“Was this why you asked me to walk with you alone?”

“It was unavoidable. If he had been listening, we would not have been able to continue this conversation.”

“If Butler Kim had heard about my maternal grandfather back then, you two would already have…”

The calm, cool composure he always maintained was nowhere to be found.

Blue flames seemed to flicker in Choi Minwoo’s eyes. Song Cheonwoo did not dare meet his gaze and turned his head away.

“At first, we were merely confused. We thought he would regain consciousness soon, so we kept it strictly confidential.”

*Crunch.*

His weary footsteps continued, followed by his aged voice.

“But then a month passed. Then half a year. Then a year. And a strange thought suddenly occurred to me. What if… he never woke up?”

Song Cheonwoo and Lee Jungryong.

At first, neither man had dared believe it. But as time passed, their suspicions gradually hardened into certainty—and that certainty changed into another emotion.

“Another year passed, and we discovered the greed we each carried.”

The greed to take the empty place left behind by Cheon Taemin, the absolute ruler no one had ever dared approach. The desire to become the master of the enormous fortress called Ares Guild.

“The purge began in secret one day. Unlike Kim Hwajong, who had already grown distant from Ares Guild, several of the closest aides who knew about his condition met their deaths in Gates.”

Choi Minwoo bit down hard on his lip.

From ancient times to the modern day, the surest way to bury the truth was death.

Lee Jungryong and Song Cheonwoo had chosen the same path. They intended to usurp the throne while its king was still alive.

*Crack.*

His smooth, flawless lips split open, and bright red blood trickled down his chin.

Choi Minwoo’s furious steps trampled the drops of blood falling onto the pure white snow.

“You managed to survive all that, Regional Director. You really are tenacious.”

Song Cheonwoo answered Choi Minwoo’s cutting sarcasm in a feeble voice.

“It was not easy for Lee Jungryong to eliminate me, either. Besides, while we fought over Ares Guild, we had both gotten equally covered in filth. He must have judged that I was unlikely to reveal anything. And he was right.”

Knowing the truth could be a reason to die. But if you had wallowed together in the mud, it could also be a reason to survive.

And in Choi Minwoo’s eyes, Song Cheonwoo was not the kind of man who could have continued resisting Lee Jungryong to the very end.

“Was the price of that negotiation the position of European regional branch director?”

“Yes. Thanks to it, I was able to save my life and the lives of my family.”

Choi Minwoo took a deep breath. At last, the puzzle that had refused to fit together in his mind seemed to be falling perfectly into place.

Why Lee Jungryong, so cold and thorough, had gone out of his way to keep Song Cheonwoo alive.

And why his only blood relative, the man who had become a symbol of the world, had not appeared for more than twenty years.

—Kraaaaaaar!

A yeti’s roar echoed from somewhere, as though voicing Choi Minwoo’s feelings.

*Damn it.*

*Crack.*

The bones in his tightly clenched fist shifted with a harsh sound.

He wanted to scream. He wanted to ask why they had done it. What in the world had driven them to such a thing?

He wanted to shout with all his strength, seize Song Cheonwoo by the collar, draw the sword hanging at his waist, and stab the old man in the back as he walked ahead.

But…

*Swish. Thud.*

The hand moving toward his sword hilt failed to reach its destination and dropped limply.

*It is not time yet.*

He could demand payment for Song Cheonwoo’s sins only after confirming every fact.

Forcing down the pounding in his chest, Choi Minwoo spoke in a trembling voice.

“Why did my maternal grandfather collapse?”

*Crunch.*

Along with the sound of footsteps pressing into the snow, Song Cheonwoo’s stride came to an abrupt halt.

An empty void now stretched out before him.

A crevasse.

The enormous crack said to appear in snow-covered mountains and glacial regions was dark inside, like an abyss whose depth could not be gauged.

“Why. Why, you ask…”

Song Cheonwoo stared down at the darkness spread before his feet and muttered in a low voice.

“I do not know.”

“Be precise. Do you not know? Or do you merely want to pretend you do not know?”

“Do you think Lee Jungryong or I pulled some kind of trick? On him, of all people?”

“That…”

Choi Minwoo suddenly fell silent. He had remembered once more what kind of person his maternal grandfather was.

Cheon Taemin.

An immortal hero born from humanity. The first and last Hunter to defeat the countless monsters and their lord, the Demon King Asmodeus, who descended upon Earth.

The surviving human race gave the hero who had saved them the title Slayer, a name that also expressed the reverence Hunters offered to a powerhouse no one could approach.

“I respected him, and I feared him. Lee Jungryong was the same. If he had not, we would not have waited for him to awaken for so many years.”

It was true. Even after Cheon Taemin, the object of their respect and fear, collapsed, Song Cheonwoo and Lee Jungryong had been unable to act easily.

It took two years, countless experiments to confirm Cheon Taemin’s condition, and a certainty laced with a measure of anxiety before those men finally revealed their greed.

“Then what in the world…?”

At the confused voice coming from behind him, Song Cheonwoo shook his head.

“No one can guess the reason. But one thing is certain. He is still alive.”

The answer to the question Choi Minwoo had been about to ask slipped from Song Cheonwoo’s lips. Gathering his confused thoughts, Choi Minwoo asked,

“What is your basis for thinking that?”

“If he had died, Lee Jungryong would never have kept me alive until now.”

“……!”

“But I do not know exactly where he is being kept. For now, I merely suspect Area A.”

“Area A…”

Choi Minwoo muttered the words under his breath and suddenly raised his head.

His gaze settled on Song Cheonwoo’s back as the old man stood before the crevasse, gazing down endlessly into the enormous crack.

“There are a few more things I want to ask.”

“Ask whatever you wish.”

Choi Minwoo silently studied his back before abruptly speaking.

“I want to know why.”

“……Why?”

“Yes. Why are you telling me everything now? We are cooperating for the moment, but in the not-too-distant future, I will become another rival of yours. Why tell me something this important?”

The enemy of my enemy is my ally.

That was the relationship between Choi Minwoo and Song Cheonwoo.

They had joined hands temporarily to bring down Go Jun and make Ares Guild their own. Nothing more and nothing less.

That was why Choi Minwoo understood Song Cheonwoo’s attitude even less.

*He has suddenly changed.*

They had met in secret only a week ago.

Back then, Song Cheonwoo had been cautious, and a faint wariness had shown through his words and actions.

As someone who had once stood as Lee Jungryong’s political rival, he knew that this temporary alliance would fall apart as soon as it successfully achieved its purpose.

*Then why?*

Information about Cheon Taemin’s whereabouts was a secret within a secret. Considering the confrontation that would come later, it was also a powerful weapon that could force Choi Minwoo to withdraw.

It was not something he could reveal openly on a whim, swept away by a momentary emotion.

*Swish.*

Just as Choi Minwoo’s fingertips touched his sword hilt, Song Cheonwoo, who had been silently staring down into the distant void, slowly turned around.

“The reason…”

The old man’s voice was calm and composed.

The hesitation and faint tremor that had colored his voice when they first met outside the Gate were gone.

The moment Choi Minwoo felt Song Cheonwoo’s gaze settle on his hand, the old man continued in a quiet voice.

“Let us call it atonement.”

Choi Minwoo tightened his grip on the sword and asked,

“Atonement for what?”

“I wanted to tell you someday, even if it was late. About the wrongs I committed against him—and against you.”

“You are more than twenty years too late.”

“Yes, I am late. But it could not be helped.”

“An excuse.”

Choi Minwoo answered firmly.

That was when—

*Rumble, rumble, rumble!*

The snow-covered mountain trembled beneath its blanket of white. An avalanche was taking place beyond the crevasse, which stretched dozens of meters across.

Even now, fur-covered giants stood atop the violently surging waves of snow.

—Kraaaaaaaaaar!

—Kauu!

Feral roars reverberated through the mountain.

At the sight of hundreds of yetis charging toward them, Choi Minwoo suddenly muttered,

“That is strange.”

“What is?”

“Yetis usually live in groups of around a dozen.”

“Yes. They used to.”

*Crunch. Shing.*

Song Cheonwoo, his back to the crevasse, stepped forward. The sword hanging from Choi Minwoo’s waist slid free of its sheath.

It was a sword left behind by a hero who had fulfilled his duty even in death.

“That is a fine sword.”

Song Cheonwoo muttered the words under his breath and took another step.

Over Choi Minwoo’s shoulder, someone was already launching himself forward.

“Young Master!”

As he heard the old loyal servant’s shout, Song Cheonwoo muttered,

“Understand. It could not be helped.”

And then—

*BOOM!*

A thunderous explosion erupted, and a blizzard came whirling toward them.
## Chapter artifact 578

# Chapter 578

*BOOOOM!*

The ground heaved beneath a massive wave of energy called mana, and the snow that burst into the air rose into a colossal wall.

Then, at the instant everything turned white—

*Zzt.*

A dazzling streak of light tore through Song Cheonwoo’s sleeve and shot outward.

The slender, razor-sharp blade was a weapon modified for the sole purpose of delivering this strike at this exact moment.

*I’m sorry.*

Along with that brief apology no one could hear, Song Cheonwoo moved like a flash of light.

*Swish.*

His lower body stayed low. His rear foot remained straight. His front foot bent at an angle. He drove strength into the hand gripping his weapon and thrust it forward.

The motion, perfected through more attempts than anyone could count, flowed together as smoothly as water. Wrapped in blinding aura, the blade pierced through space.

*SHWAAA!*

A sharp crack split the air, cutting through everything.

Song Cheonwoo had retired from active duty and was now an old man nearing seventy, but he remained a powerhouse no one could deny.

The instincts engraved throughout his body after surviving the vortex of the Great Cataclysm—and the tremendous mana coiled within him—refused to acknowledge the years that had passed.

There was no way some youngster who was not even thirty could block that strike.

*It’s over.*

Song Cheonwoo was certain of it.

At least, he was—until the next instant, when the blade piercing through the wall of wind and snow was stopped by something.

*SKRAAAK!*

“……!”

A powerful resistance traveled up the blade. Song Cheonwoo’s eyes flew open, and a thunderous roar rang out.

*BOOOOM!*

Mana collided with mana. The gale created by the impact clawed at everything around them.

The wall of snow collapsed, and the snowdrifts scattered.

Between them, a pair of eyes sat deep and still.

“So this is it. The trap Go Jun prepared.”

Song Cheonwoo let out a low groan at the sight of Choi Minwoo, who had caught the strike with the flat of his blade.

“How did you……?”

It was impossible. Song Cheonwoo remembered clearly when Choi Minwoo, still in his early twenties, had stayed at the European regional branch several years ago.

The youngster had possessed outstanding natural talent, but his actual ability had fallen far short of it.

But now…

*Rrrrrumble.*

He could tell from the force traveling along their crossed blades.

The young man locking swords with him was no longer someone who could be called a youngster. He had grown into a formidable warrior.

And Song Cheonwoo’s plan had suffered a major setback.

*So blood really does tell.*

Cheon Taemin.

The three syllables weighed heavily on his heart, and suddenly his sword felt heavier. But he had come too far to turn back now.

Long ago, he had crossed the river and sunk his own boat. He could not retreat if he wanted to protect the blood relatives Go Jun had taken hostage.

*I have to kill him here. No matter what.*

Song Cheonwoo clenched his teeth. Mana surged through his solid body, which had seemingly forgotten how to age.

As his wrist traced an arc, the sharp tip of his sword slid across the flat of Choi Minwoo’s blade.

*Clack. Swish!*

It had been a hair’s breadth. The sword tip narrowly grazed past Choi Minwoo’s neck and pierced empty air.

A stream of blood spurted from his neck, split open by the sword pressure.

Someone watching the scene cried out like a scream.

“Young Master!”

The shout carried sorrow, urgency, and fury.

The newcomer crossed hundreds of meters in an instant. When he flung his sleeve, the air around them heated rapidly.

*Fwoooosh!*

Flames made of mana erupted and rose between Song Cheonwoo and the others. The snow on the mountain melted and evaporated.

Amid the scorching heat, Song Cheonwoo could see the old butler drawing closer over Choi Minwoo’s shoulder as the young man retreated and steadied his breathing.

“You’ve come.”

Song Cheonwoo calmly stared at Butler Kim.

The man with whom he had once shared the bond of older and younger brothers. One of the few comrades he had trusted enough to leave his back to on the battlefield.

But that had become a thing of the past for both of them.

“I resented you, but I never hated you. However……”

*Fwoosh.*

A fierce heat burst forth. Flames formed in midair, coiled around Butler Kim’s hands, and took on a new shape.

Song Cheonwoo gazed wistfully at the man now holding a whip of fire in each hand.

“You finally look like yourself. You really are the Kim Hwajong I knew.”

Butler Kim—no, Kim Hwajong—tightened his grip on the whips of fire and took a step forward.

*Thud.*

Lava seemed to boil in the eyes that had always remained calm.

The old butler, who had preserved his loyalty without wavering through all the years that had passed, had returned to the vigorous figure he had been in the past.

“Shut your fucking mouth, you piece of shit.”

“……!”

At the sight of Kim Hwajong as he had never seen him before, Choi Minwoo opened his mouth.

Then—

*Swish! FWOOSH!*

Following the arc of the sword as it swung, the wall of fire separating the three of them split apart.

And Choi Minwoo saw it.

Song Cheonwoo’s calm face as he stared at them—and the brilliantly white necklace that had somehow appeared around his neck.

*That’s…*

The name of the necklace, so painfully familiar, slipped from Song Cheonwoo’s lips.

“It’s a Yeti’s Necklace. When you told me to come here, I knew it was bound to come in handy.”

Song Cheonwoo suddenly turned his head. Beyond the crevasse, hundreds of yetis came surging down with the avalanche.

“And this time, it seems I was right. Don’t you agree?”

—Kyaaaaaaar!

As he watched the hundreds of yetis charging toward them, Choi Minwoo felt his grip tighten instinctively around his sword hilt.

*A Yeti’s Necklace.*

Choi Minwoo—and even Kim Hwajong—knew what function the small necklace possessed.

Only a few months earlier, Won Myunghoon had prepared it as a magic item to trap Jin Taekyung in the Black Wyvern’s nest.

*A slave’s mark that draws in dragonkin monsters.*

There were hierarchies even among monsters.

Yetis, giants who lived in the snow-covered mountains, were the slaves and prey of dragonkin. But the Yeti’s Necklace did more than simply attract dragonkin monsters.

It marked its wearer as a slave of the dragonkin—and, to yetis, as one of their own kind.

“You……!”

Choi Minwoo’s shout toward Song Cheonwoo never finished.

*RUMBLE! Rat-a-tat!*

An enormous avalanche surged forward. Hundreds of yetis raced across it as though riding a wave, then leaped over the crevasse.

Song Cheonwoo was the closest to them, but as long as he wore the necklace carrying the scent of a yeti, he was no different from one of their kind.

—Kraaaaaar!

The savage roar shook the snowfield.

Song Cheonwoo glanced at the hundreds of shadows leaping over his head and charging toward the other two before speaking.

“Hwa-jong. You should stay out of this.”

“You dog-shit bastard! I’ll tear you apart!”

Kim Hwajong let out a furious cry and swung his whips of fire.

*Whoooosh! BOOM!*

Flames carrying tremendous heat swept across everything around them and set it ablaze. But the hundreds of yetis, strengthened by magic power, paid no attention even as their own kind fell.

If anything, they raised even more ferocious magic power.

—Kraaaaaar!

“……!”

There were simply too many of them.

Kim Hwajong clenched his lips tightly. At that moment, Choi Minwoo’s quiet voice reached his ears.

“It’s all right, Butler Kim.”

“Young Master!”

“If the yetis are here, my fight will only become more difficult.”

“But……”

“Go. I’ll handle things here.”

Kim Hwajong, who had been about to argue, stopped short.

For a brief moment, the old butler stared into Choi Minwoo’s unwavering eyes. Then he silently kicked off the ground.

The whips of fire swinging from both hands drew the hundreds of yetis away.

*RUMBLE!*

—Kyaaaa!

Hundreds of yetis retreated alongside the heat. At the same time, Song Cheonwoo stepped forward.

*Crunch.*

Song Cheonwoo took one step through the snow. His hand blurred.

The sword wrapped in dazzling aura tore through everything around it.

*SHWAAAAK! Slice!*

Aura was the essence containing the true power of mana.

An extremely sharp and destructive force surged forward, cleaving through space. Neither wind, snow, nor rock could stop it.

If there was only one way to stop it, that way was with another aura.

*Swish! Slice!*

The sword strikes slashed ceaselessly in every direction. Skin split, and drops of blood flew.

Choi Minwoo narrowly evaded the streaks of light cutting across him. His eyes sank deeply, and strength filled the hand gripping his sword hilt.

*Whoooosh.*

*Hero’s Soul.* The sword left behind by a noble hero trembled.

Pure white aura, resembling the snowy mountain, coiled around the blade and surged upward. Choi Minwoo gripped the sword tightly with both hands and smoothly rotated his upper body.

*Shiiiiing.*

Aura against aura. Light against light.

The instant two flashes of different colors met—

*RUMBLE-RUMBLE-RUMBLE!*

A massive shock wave shook the snowy mountain. Snowdrifts within a radius of dozens of meters turned to powder and scattered, breaking apart in the air.

Then pale figures streaked across the space turned completely white.

*Swish, swish, swish!*

*BOOM! CRASH!*

Two figures. Two swords. Auras belonging to different masters crossed space and collided.

Every time they did, tremendous shock waves erupted, pushing away snowdrifts and ripping up the ground.

Red liquid dropped onto the dark green ground, revealed for the first time in ages beneath the snow.

*Trickle.*

Choi Minwoo felt hot blood running along his wrist. His shoulder throbbed, and cold sweat had already formed on his forehead, brushing against his eyebrows.

But he was given no time to staunch the bleeding or wipe away the sweat.

The opponent facing him was still raining down sword strikes filled with killing intent.

*SHIIING! Slice!*

It was truly a matter of a single hair. The ground, made of solid rock, was sliced apart like tofu.

Choi Minwoo narrowly avoided the attack and let out a short breath. The enemy’s face entered his field of vision, radiating killing intent so intense that his entire body prickled.

*Song Cheonwoo.*

A hero born from the Great Cataclysm and once one of the most renowned Hunters alongside Lee Jungryong, Song Cheonwoo possessed truly terrifying skill.

His skill was one of the reasons Song Cheonwoo had survived despite knowing a truth that could never be allowed into the open.

*Shing!*

Choi Minwoo twisted his head, and his hair scattered in the fierce wind. If he had been even a moment slower, it would not have been his hair that was cut off, but his neck.

But why?

Why did he not feel the terror of death he had experienced in Sichuan?

*Heh.*

Instead, a quiet laugh escaped him. He had suddenly remembered a conversation he had once shared with someone who was not here.

*“This might sound a little crazy, but sometimes I start laughing when I’m in a situation where I feel like I’m going to die.”*

*“You really are quite insane.”*

*“But… whenever I start laughing, I always end up winning somehow.”*

He did not know why that conversation, exchanged so casually that day, had come to mind in a situation like this.

But Choi Minwoo finally felt as though he understood, at least a little, what that person had meant.

*I won’t die.*

It was faith in oneself, and a will possessed only by those who never gave up until the very end.

It was an enlightenment Choi Minwoo had made his own when he walked toward thousands of monsters in a body exhausted and wounded.

*Shing. Slice!*

A burning pain flared from his thigh.

At the sight of Choi Minwoo staggering as he twisted his body, Song Cheonwoo’s movements grew even more violent.

*Swish, swish, swish! Slice!*

This time, his arm.

*Thunk!*

Then his flank.

But Choi Minwoo continued forward, enduring the pain.

He met the rain of sword strikes head-on and kept taking one step after another. In the hand advancing without pause, a single sword was trembling.

*Whoooom.*

*Hero’s Soul.* A sword passed down to him from a hero who had fulfilled his mission even after becoming a vengeful spirit.

A legendary sword that bestowed even greater power upon those who possessed the qualifications.

*Fwoooooom!*

The blade trembled. A brilliant radiance caused the aura to swell.

Song Cheonwoo’s eyes widened at the enormous light.

“You……!”

“One last question.”

Unlike his cold gaze, his voice was hot.

Along with those quiet words, Choi Minwoo drove forward a strike carrying all his strength.

“Have you forgotten whose blood flows through my body?”

“……!”

*Shiiing!*

A massive streak of light cleaved through space.

And within the blinding flash that filled his vision, Song Cheonwoo felt a bolt of lightning slash across his chest.

*Slice!*
## Chapter artifact 579

# Chapter 579

*Slice!*

The instant a streak of light cut across his chest, Song Cheonwoo felt his vision go dim.

*It’s hot.*

It was lightning.

The kind of lightning even a hero of old—one who had left his mark on the chaotic, perilous Great Cataclysm—had been unable to stop.

With trembling eyes, Song Cheonwoo stared at the sword in his hand.

Only a few seconds ago, it had been radiating a brilliant aura. Now it had been cut in half by something even more destructive and razor-sharp.

*Clang.*

The sword slipped from his grip and rolled across the ground. A beat later, pain swept through his entire body.

“Cough.”

*Drip, drip.*

Dark red blood spilled from the corner of his mouth and stained the snow. His clothes and armor split diagonally, exposing his bronze-colored upper body.

Then, the instant a fine line across his firm muscles and skin glowed red—

*SHWAAA!*

An enormous amount of blood burst forth like a waterfall.

From his left chest to his right hip. The scar left behind by the lightning that had swept across him was horrific, and it would never heal.

Feeling the strength leave his body, Song Cheonwoo staggered backward.

*Crunch.*

His powerless foot stepped onto snow soaked in blood.

One step. Two steps. Three steps. And then…

*Fsssh.*

At the sound of the piled-up snow sliding away, Song Cheonwoo barely managed to steady himself.

By then, a massive fissure known as a crevasse had opened its jaws behind him, waiting.

There was nowhere left to retreat—and nowhere left to advance.

*What a fucking mess.*

Song Cheonwoo felt his chest grow hollow.

Perhaps it was because the vitality was still draining from his body at that very moment.

He suddenly raised his head, and a figure slowly walking toward him entered his view.

*Choi Minwoo.*

The only blood relative of *that person*, who had always been an object of respect and fear.

Song Cheonwoo recalled the quiet voice he had heard just before facing the lightning.

*“Have you forgotten whose blood flows through my body?”*

At this moment, what was reflected in the old man’s eyes was someone else who was not here.

A person who had now become nothing more than a memory of the past.

A being who inspired respect and fear in anyone who merely watched him from nearby.

Song Cheonwoo realized something he had forgotten for a long time.

Cheon Taemin’s blood flowed through that young man’s body.

“...Hyung?”

Song Cheonwoo muttered the word between ragged breaths.

Through his vision dyed entirely red, the young man holding a sword that radiated brilliant light resembled his maternal grandfather.

The deep, solemn look in his eyes seemed to ask why Song Cheonwoo had changed sides.

“Don’t come any closer. Don’t!”

With a shout he barely managed to force out, Song Cheonwoo swung his sword. Or rather, he thought he had swung it.

But the hand that had dropped the sword moments earlier was empty. The hand flailing through empty air was finally stopped by the firm grip of someone who had reached him.

*Whooom. Crack.*

Choi Minwoo seized Song Cheonwoo’s wrist and tightened his grip.

With a sickening sound as the bones shifted out of place, a scream burst forth.

“GRAAAAAH!”

*Thud.*

Song Cheonwoo dropped to his knees, unable to withstand the pain. Choi Minwoo stared down at him with sunken eyes.

What he saw now was not Song Cheonwoo, but an old man.

*Zzt, zzt, zzt.*

The radiance contained within *Hero’s Soul* gradually faded.

The winner of this fight had already been decided.

Facing the fallen loser, the victor stood tall and quietly announced the result of their fierce battle.

“Stop. It’s over.”

“...!”

Song Cheonwoo’s body, writhing in pain, suddenly went rigid.

He had lost.

It was impossible. It could not happen, and it should not have happened.

But the reality he had finally come to understand was different.

His trembling gaze rose. He looked at Choi Minwoo, whose expression was calm enough to make the bloody battle from moments ago seem unreal, and muttered,

“How? How did you...?”

“I wonder.”

Choi Minwoo felt the immense energy flowing through his body.

Only a few months ago, he had been unable to sense it. It was the only gift his maternal grandfather had left him—and Jin Taekyung had torn open the wrapping and returned it to its rightful owner.

Along with how to make good use of the gift.

“Perhaps... it’s because I was stronger than you.”

That was not all. Choi Minwoo had believed in himself and acted with an upright heart.

And to a qualified owner, a sword containing the soul of a hero had granted even greater strength.

Choi Minwoo looked down at Song Cheonwoo with powerful eyes.

“I won, and you lost. That is all that remains between us.”

“...!”

The old man’s trembling gaze gradually settled. A cracked voice escaped between his bloodstained lips.

“Yes. You’re right. I didn’t expect this result, though.”

“We agree on that much. I never thought a situation like this would come either.”

Anger. Hostility. A faint trace of pity for a man who had fallen to the very bottom.

Choi Minwoo felt many things toward Song Cheonwoo, but the strongest of them all was a question.

Why? For what reason had Song Cheonwoo done this?

And he still distrusted the story Song Cheonwoo had told him earlier.

“Why did you do this? If we had joined forces, driving Go Jun out and taking control of Ares Guild would not have been difficult.”

Song Cheonwoo answered Choi Minwoo’s question in an empty voice.

“I know. I thought the same.”

“Then why?”

“I had no choice. It was an offer I couldn’t refuse.”

Choi Minwoo already knew the name of the person who had made Song Cheonwoo that offer.

“Go Jun. Was everything his order? From forming an alliance with me to what happened just now?”

“Cough. An order?”

Song Cheonwoo spat out blood once more and let out a weak laugh.

It was unmistakable mockery directed at Go Jun.

“If it were Lee Jungryong, perhaps. But that bastard is nothing more than a powerful, immature brat. I may be a despicable and pathetic old man, but I haven’t fallen so low that I would submit to the orders of some young punk. My alliance with you was entirely my own decision.”

“Then—”

“Didn’t I tell you? It was an offer I couldn’t refuse.”

As he looked into Song Cheonwoo’s eyes, which seemed ready to go out at any moment, Choi Minwoo suddenly understood.

What the old man still had left.

What that impossible-to-refuse offer contained.

“Your family.”

Song Cheonwoo gave a small nod before speaking.

“I only realized it after losing to Lee Jungryong. I had forgotten what mattered most.”

It had been a fierce life.

Before the Great Cataclysm, he had been forced to support his household day and night. During the Great Cataclysm, he had been unable to leave the battlefield. After the Great Cataclysm, he had begun another battle to approach the center of power.

And after losing his political struggle against Lee Jungryong, he had remembered the value of his family once more—only to forget it again when ambition awoke alongside Lee Jungryong’s death.

“My absence was the root of all this. I suppose this is the price an old man paid for reaching too greedily after ambition too late in life.”

“You’re probably right.”

Choi Minwoo’s voice as he answered Song Cheonwoo’s lament was cold. Listening to him made even the last remnants of pity disappear.

“Because of you and Lee Jungryong, I had to lose the only family I had.”

His cold voice held a flame.

Because of the ambitions of two adults, a child who did not even understand the meaning of ambition had been left in the position of an orphan.

Before he could properly comprehend his parents’ deaths, he had been forced to live on while resenting the maternal grandfather who had disappeared.

“...I’m sorry. It was my fault.”

“Then I suppose you wouldn’t have any objections if I burned you to death right now. Would you?”

The voice that suddenly rang out through the empty air did not belong to Choi Minwoo.

*Crunch.*

Kim Hwajong stepped onto the ground, covered from head to toe in blue yeti blood.

Flames like the fire whip in his hand burned in the old butler’s eyes.

“Hwa-jong. It was you.”

“Shut your fucking mouth, you piece of shit. Because of you, how much the Young Master—”

Choi Minwoo was the one who stopped Kim Hwajong from swinging his whip immediately.

At a slight glance from Choi Minwoo, the old servant clamped his mouth shut and stepped back. Choi Minwoo turned his gaze toward Song Cheonwoo.

“Then is everything you told me about my maternal grandfather a lie as well?”

“I wish it were a lie. But it is all true. I’ve already come too far.”

Unlike Kim Hwajong, who furrowed his brow because he could not understand the meaning of the answer, Choi Minwoo let out a sigh filled with both relief and disappointment.

The fact that his maternal grandfather was alive was good news, but the thought that he had been unconscious for more than twenty years troubled him.

But that was for later.

For now, Song Cheonwoo’s fate came first.

*—Young Master.*

At the message spell from Kim Hwajong, carrying pride in Choi Minwoo, fury toward Song Cheonwoo, and a trace of hope, Choi Minwoo shook his head.

He already knew what the old butler was going to say.

*—Butler Kim. That isn’t possible.*

*—What do you mean, it isn’t possible?*

*—Give me a potion. We need to treat him enough to keep him alive, at least for now.*

*—But...!*

Kim Hwajong had been about to shout something, but he forcibly restrained himself beneath Choi Minwoo’s calm gaze.

He knew too.

Song Cheonwoo was a decisive witness and a crucial piece of evidence simply by remaining alive.

He merely wanted to deny it.

“Butler Kim.”

“Damn it. All right.”

Choi Minwoo’s eyes widened when Kim Hwajong cursed as he handed over a mid-grade potion.

“Did you just swear in front of me?”

“Yes, I did. Why?”

“I heard bits and pieces about it, but this is completely different from how I remember you.”

“This is who I am. When you were young, I watched my behavior and my language in case you learned from me.”

“Why not keep doing that...?”

“You’re almost thirty now. Since things have come to this, learn from me if you want to learn. Otherwise, drink this.”

*Is he really the same person who stayed by my side since I was young?*

At the old butler’s gruff tone, Choi Minwoo let out a quiet laugh and said,

“Butler Kim.”

“What? And don’t laugh. You shouldn’t laugh at an adult like that.”

“Thank you. For becoming my only family.”

“...!”

“I’ve always wanted to say that.”

Unable to meet the old butler’s eyes after speaking those sincere words, Choi Minwoo turned away without another word.

At the end of the path before him, an old man lay buried in the snow, waiting for death.

*Click.*

When he opened the stopper, a clear yet subtle fragrance drove away the sharp smell of blood.

Song Cheonwoo looked at Choi Minwoo approaching him with eyes that seemed ready to go out at any moment.

“Are you... planning to save me?”

“Do you want to live?”

“I... I...”

As Song Cheonwoo hesitated, Choi Minwoo felt an intense disgust.

“If I had my way, I would kill you a hundred times, a thousand times over.”

“B-but my family...”

“There must be a way. But we’ll have to deal with that after we get out of here.”

“...”

“Choose.”

Song Cheonwoo hesitated, then nodded with an expression of resignation.

Choi Minwoo looked down at him coldly and slowly tilted the potion.

*Hiss.*

The wounds began to close little by little the instant the milky liquid touched them.

It was an extremely weak recovery, but to someone, it was a lifeline that could give them enough strength for one final effort.

*Crack!*

Where had he found such strength?

Amid the snow exploding in every direction, Song Cheonwoo launched himself with superhuman force and slipped into the enormous crevasse.

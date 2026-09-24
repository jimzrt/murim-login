# Checkpoint Review — 1015–1019

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

# Chapters 1015–1019

## Plot

Taekyung’s force of roughly three thousand marches west from Tianshui, through Lanzhou and the Hexi Corridor, reaching the Qilian Mountains. Along the way, Taekyung is flustered by Wolhwa’s unusually affectionate missive and Ju Hwaran’s questions about their relationship. At the Qilian Mountains, Gansu’s leaders defend their strategy of leaving the rear exposed to lure Dark Heaven into a trap if it uses the Moving Formation. Taekyung lets their decision stand for now, though he suspects Sima Gong is hiding something.

Namho reports that Sama Pyo burned a secret letter shortly before the group left the Jin Family of Taiyuan. The scent of camel-oil paper suggests it came from Gansu or Qinghai, and Sima Gong is suspected as its sender, but the letter’s contents and purpose remain unknown. Jeok Cheongang asks whether Taekyung would kill Pyo and Taishan if they were acting on orders tied to Dark Heaven; Taekyung cannot answer.

Sima Gong reinforces the westbound force with three thousand troops from the Qilian Mountains. As the army moves west through falling snow, Hyuk Mujin tells Taekyung that trust in him keeps him from fearing danger. Pyo questions Sima Gong’s decision-making and reflects on the ruthless calculations that shaped his rise as heir. A red flare bursts above a distant hill.

## Continuity

- The westbound force has reached the Qilian Mountains and now includes three thousand troops from the forces stationed there. It is moving west through the mountains; Dark Heaven’s location and objective remain unknown.
- Gansu’s leaders chose to leave forces on the rear front to delay Dark Heaven if it uses the Moving Formation. Taekyung allowed the decision to stand for now.
- Sama Pyo burned a secret letter shortly before the group left the Jin Family of Taiyuan. Camel-oil paper suggests it came from Gansu or Qinghai; Sima Gong is only a suspected sender. Its contents, sender, and purpose are unconfirmed.
- Taishan appeared unusually gloomy and ate less as the group approached Gansu; whether he knows about the letter remains unknown.
- Taekyung remains unsure whether he would kill Sama Pyo and Taishan if they were acting on orders connected to Dark Heaven.
- Sama Pyo recognizes that Sima Gong’s ruthless calculations, including sacrificing family, shaped the Black Dragon Demon Gate and Pyo’s rise as heir. Sima interprets Pyo’s recent deference as a return to his former self.
- A red flare burst above a distant hill as the force moved west; what it signaled is unknown.
- Wolhwa’s latest missive includes affectionate personal language and a wish that she and Taekyung meet again. Ju Hwaran’s response to it remains unresolved.
- Namho’s important disclosure to Taekyung was the report about Pyo burning the letter.
- Six Baekma Bang men left to fetch the Lord; Ma Junggeol remains with Taekyung’s group. The Lord’s identity and motives remain unknown.
- Sama Pyo previously disobeyed Sima Gong’s order to return to Gansu. Sima Gong also ordered two martial artists dealt with for a taboo remark about Pyo’s succession; their fates remain unknown.

## Translation Decisions

- Render 하서주랑 as “Hexi Corridor.”
- Retain “Moving Formation” for 이동진.
- Render 밀서 as “secret letter,” distinct from 전서, “missive.”
- Render 군자도 as “Junzi Saber,” preserving 군자 as “junzi” and 刀 as “Saber.”
- Retain “iron ball” as the image for the weight of Sama Pyo’s inherited constraints; it is not a literal restraint.

## Durable state

{
  "active_continuity": [
    "A secret letter Sama Pyo received was suspected to have come from Gansu or Qinghai; its sender, contents, and purpose remain unknown.",
    "Taishan appeared unusually gloomy and ate less as the group approached Gansu; whether he knows about the letter is unknown.",
    "Taekyung remains unsure whether he would kill Sama Pyo and Taishan if they were acting on Sima Gong's orders connected to Dark Heaven.",
    "Sima Gong has reinforced the westbound force with three thousand troops from those stationed in the Qilian Mountains.",
    "Sama Pyo knows his father's ruthless calculations included sacrificing family and enabled his own rise as heir; Sima reads Pyo's recent deference as a return to his former self.",
    "A red flare burst above a distant hill as the force moved west through the Qilian Mountains."
  ],
  "continuity_sources": [
    1019
  ],
  "open_questions": [
    "Who sent Sama Pyo the secret letter, what did it say, and what was its purpose?",
    "Are Sama Pyo and Taishan acting on Sima Gong's orders, and are those orders connected to Dark Heaven?",
    "What did the red flare signal?"
  ],
  "safe_through": 1019,
  "temporary_decisions": [],
  "version": 1
}

## Reading copies

## Chapter artifact 1015

# Chapter 1015

Our force numbered a staggering three thousand, but every last one of them was a martial artist, so we moved far faster than common sense would suggest.

We’d been on the road for only two days since leaving Tianshui, on the eastern edge of Gansu, and we’d already passed Lanzhou, the provincial capital, and were pressing ahead without slowing down.

It must have been around then.

At some point, the bone-chilling plateau and endless wilderness vanished, replaced by a narrow road lined on both sides with rocky hills of every size.

*This place…*

Sometimes, after leaving the modern world behind and roaming the Murim, I’d find myself overwhelmed, even if only for a moment, by the majesty of nature untouched by human hands, preserving the passage of countless ages.

And just as I let go of my reins and silently gazed at the endless view below the plateau, a soft voice reached my ear.

“This is the Hexi Corridor. It’s called that because it stretches west of the Yellow River like a corridor. I don’t know who first gave it that name, but doesn’t it suit the place?”

I agreed with her, but that aside, it was easy to recognize the voice’s owner.

Even if Sama Pyo and Taishan hadn’t been away, it would have been the same.

There was only one person around me with such a fresh, clear voice.

“You certainly know your stuff, Young Lady Ju.”

Ju Hwaran gave a shy smile at my reply.

“It’s only natural. I once led the Escort Bureau temporarily, even if it wasn’t for very long. And I am the Escort King’s granddaughter, after all.”

At first glance, she was right. But there was modesty in her words, too.

Just as being born into a martial family didn’t mean you had to learn martial arts, Ju Hwaran hadn’t been obligated to take over the family business.

The reason she knew so much about the Central Plains’ geography and related matters was entirely her own effort.

*Now that I think about it, the Yongbong Escort Bureau was in a situation not all that different from the Jin Family of Taiyuan at first.*

A family that had left its former glory behind and begun to fall into ruin.

One small difference was that, unlike the Jin Family of Taiyuan, which had three sons and a whole lot of testosterone, Ju Hwaran was an only child—and had to bear that much heavier burden alone.

*Though her father, the Head of the Escort Bureau, was still there, unlike mine, even if he was bedridden.*

That was all in the past.

The Head of the Yongbong Escort Bureau had recovered his vitality and returned to the front lines. And the huge sum of gold I’d beaten out of the Taeeul Merciless Sword in return had been more than enough to pull the crumbling family back onto its feet.

And the Jin Family of Taiyuan had risen to join the Five Great Families, filling the void left by the Murong great family—or rather, what remained of the Murong household.

*If Dark Heaven didn’t exist, we could’ve wrapped things up here with a happy ending where everyone lived happily ever after.*

But reality wasn’t something you could ignore. You had to face it head-on, and opportunities always came in the midst of crises.

That was how Ju Hwaran and the Yongbong Escort Bureau, and I and the Jin Family of Taiyuan, had overcome their crises and grown stronger.

It was only the many sacrifices we’d made along the way—and the fact that more would inevitably come—that weighed heavily on my heart.

And besides…

*No, never mind. I’ll leave it at that for now.*

I pushed from my mind the sight of Namho approaching me just yesterday, his face unusually stiff. His low voice still seemed to ring in my ears.

When I realized Ju Hwaran was watching me with concern, I forced a casual smile.

“Ah, sorry. I was just… just thinking about something.”

“It’s all right. I understand. You must be troubled with the battle coming up.”

How should I put it?

I couldn’t exactly tell her something I wasn’t even sure of myself.

I silently watched Ju Hwaran’s profile as she rode alongside me, then spoke almost on impulse.

“That’s part of it, of course. But I’ve also been thinking about relationships.”

“Relationships?”

“Between people. Trust, expectations. Things like that.”

I lifted my head and looked toward the narrow pass between the distant rocky hills, where thousands of our allies were pouring through like a flood.

“Nothing’s easy, I suppose, but I find this especially hard. The connections and feelings between people.”

“Connections and feelings…”

Ju Hwaran murmured the words as if to herself, then added quietly,

“I think I understand how you feel.”

“I thought you might, Young Lady Ju.”

She’d been through it herself. How could she not?

I still remembered it clearly: during the conflict with the Zhongnan Sect, Ju Hwaran had personally cut down Chief Escort Heo Jun, who had betrayed her from the shadows.

*She once followed him like a real uncle. The wound from that must still be with her.*

That was why relationships between people were so difficult.

You could readily give someone something, but no one knew whether they’d give as much in return—or more, or nothing at all.

*That’s why I’m hesitating so much, too.*

But the next thing Ju Hwaran blurted out was enough to sweep away the doubts that had been creeping back into my mind.

“It’s Wolhwa, isn’t it?”

“Y-yes?”

I’d almost agreed without thinking. I blinked at Ju Hwaran.

What? Had I just heard her wrong?

“Um, sorry, what did you just say?”

Without turning her head, Ju Hwaran answered,

“The woman named Wolhwa. The Branch Leader of the Lower District Sect in Shaanxi. Isn’t she?”

“Yes. That’s right.”

“Exactly.”

“No, I meant that she is the Branch Leader of the Shaanxi branch.”

“Oh, really?”

“Yes.”

“And?”

“Pardon?”

“Never mind.”

What on earth was this conversation?

I stared blankly at Ju Hwaran, speechless, when a violent fit of coughing rang out loud enough to cut through the pounding hooves of our galloping horses.

“Cough! Cough! Cough-aaargh!”

What’s that idiot doing now?

I turned to look behind me, ready to say something to Hyuk Mujin, who was practically convulsing in his saddle. And that was when I saw it clearly.

Hyuk Mujin desperately shaking his head, while Namho and Song Ilseom, on either side of him, looked at me with pity.

At the same time, a certain suspicion suddenly crossed my mind.

Hmm.

Hmmmm.

Could it be… what I thought it was?

*This isn’t exactly the best time for something like this.*

Still, I had to clear up any needless misunderstanding.

Feeling a little strange, I parted my lips.

“Um, Young Lady Ju?”

“Yes. Go ahead.”

Her eyes were still fixed straight ahead, as if she’d spotted her family’s sworn enemy up the road.

And, quite apart from that, her ears had somehow perked up.

Watching her, I rubbed my chin even though it didn’t itch.

“Well, this isn’t something you’re particularly curious about, but I thought I’d mention it.”

“That’s right. I’m not particularly curious, but I’ll hear you out.”

“I’m not very close with Wolhwa.”

“……”

“We did have some dealings, sure. Just a year or two ago, she was the Branch Leader in Shanxi, not Shaanxi. The Lower District Sect and I had various mutual dealings, so we got to know each other a little.”

After a brief silence, Ju Hwaran spoke.

“You speak casually for someone you’re not close to. And you just call her by her name.”

“You’re badly mistaken. I call her that when she isn’t here. If we were face-to-face, I’d use proper honorifics.”

“I see. So you sometimes exchange heartfelt missives like this one, too?”

“Missives?”

I blinked silently. Only then did I begin to understand why she’d suddenly brought up Wolhwa.

The missive.

The one delivered by the Lower District Sect member who’d guided us to Gansu, written under Wolhwa’s name.

“Was that why?”

“Why what?”

“That’s, well…”

How should I put it?

Was it really a good idea to say the first thing that came to mind?

I faltered, unable to find the words. At last, Ju Hwaran turned her head and looked me straight in the eye.

“Can I ask what was written in that missive?”

It was strange.

Even as our saddles jolted with every pounding hoof and the fierce wind rushed past us, Ju Hwaran’s voice reached my ears more clearly than anything else.

Though it was barely half as loud as usual.

Maybe that was why.

I stared at her blankly, then blurted out an answer without meaning to.

“No.”

“Ah.”

Ju Hwaran closed her mouth, her expression dimming slightly. I continued, slowly.

“I can’t tell you about the missive. I haven’t checked what it says yet.”

“……!”

“Hmm. With everything going on, I’d forgotten about it for a while. Want to read it together now?”

I didn’t need an answer. Ju Hwaran’s bright smile said enough.

*Inventory open. Summon.*

As I slipped my hand inside my robe and spoke the command, I felt something solid between my fingers.

I naturally pulled out the bamboo tube I’d received from the Lower District Sect member a few days ago, then took out the missive rolled up inside and unfolded it in front of Ju Hwaran.

Hesitation? The slightest worry?

Not a trace of either. Not even a pinch.

*Why would I have anything like that? Wolhwa only teases me with wordplay when we meet in person. When it comes to business, she’s meticulous.*

There was a reason I was so sure. This wasn’t the first time I’d heard from Wolhwa.

Maybe because of the agreement with the Jin Family of Taiyuan, she’d sent me a couple of missives while I was away, and they’d contained some fairly useful information.

The location of Lower District Sect branches. How to make contact in an emergency.

Or the latest news from Shanxi or Shaanxi.

That was all it was: “information.”

It wasn’t Wolhwa writing to me personally. It was the Branch Leader of the Lower District Sect’s Shaanxi branch looking after a valued client.

So I unfolded the missive without a moment’s hesitation—and immediately realized something was wrong.

Young Master Jin, have you been well?

Maybe it’s because we haven’t seen each other in so long. I miss you so much. I missed you so much that you even appeared in my dream last night!

*Rustle.*

The paper rolled back up as I instinctively let go.

Ju Hwaran, who’d brought her horse right alongside mine so we could read the missive together, spoke.

Her voice was so gentle it felt out of place.

“Could you open it again?”

“……”

“I was reading it.”

“…Um, Young Lady Ju?”

“Yes. Go ahead. I’m listening.”

I hurriedly opened my mouth, feeling like I had to say something. But her soft reply—and the steady gaze she fixed on me—sent a chill down my spine.

As if my body had completely forgotten the power I’d gained long ago: Unaffected by Cold and Heat.

*How am I supposed to explain this?*

It felt like I’d stepped into a deep swamp with no way out.

As I struggled to find something to say, Ju Hwaran gave a faint smile.

“Never mind. It’s fine. You don’t have to say anything.”

“Y-yes?”

“Don’t mind me. Go ahead and finish reading. It sounds like a very deep and important conversation. Well, I’ll leave you to it.”

“Wait, Young Lady Ju—!”

*Thud-thud-thud!*

Before my desperate shout was even finished, Ju Hwaran urged her horse forward and sped ahead.

I stared blankly at her retreating back, then silently unfolded the missive in my hand.

Unlike usual, it was full of trivial personal chatter. And at the very end, it had one line that put the finishing touch on the whole thing.

*Hoping for the day the Yellow River runs clear and we can meet again,[^1] Wolhwa.*

“……”

She really was trying to get me killed.

I stared at the words, which anyone would mistake for a message between people on very intimate terms. Then Hyuk Mujin carefully approached and spoke.

“Um, Captain.”

“What.”

“I can see the Qilian Mountains.”

“Get lost.”

“Yes, sir.”

*God, I want to die.*

[^1]: The Korean expression evokes the Yellow River running clear—a rare, auspicious event—and uses it to express the hope of meeting again.
## Chapter artifact 1016

# Chapter 1016

I’d vaguely sensed it from the moment we first met, but Wolhwa was impossible to figure out.

*What on earth possessed her to send me a letter like this out of nowhere?*

A Meeting When the Yellow River Runs Clear.[^1]

I didn’t know much about classical idioms, but even a rough, literal translation left plenty of room for misunderstanding.

A meeting like the moment the river runs clear.

Wasn’t that the sort of thing you’d say only to someone you were at least flirting with?

*This is going to give the gossip mill a real boost.*

Of course, I wasn’t delusional enough to get the wrong idea over a single letter like this.

I’d known for a long time that Wolhwa’s interest in me was limited to her being a member of the Lower District Sect. It had absolutely nothing to do with romantic feelings.

But…

*The problem is that Young Lady Ju might misunderstand—not me.*

I muttered to myself and put the crumpled missive back in my Inventory.

It bothered me a little, but there was nothing I could do about it for now.

Time would sort it out eventually. Besides, far more important problems stood in my way.

And at this very moment—

*Whoosh.*

A vast mountain range finally appeared before us, accompanied by the cold wind sweeping across the plateau. It was like a marker telling us we’d taken one more step toward those problems.

*That’s…*

My eyes widened before I knew it.

Vast. Dazzling.

That was what came to mind the first time I saw the Qilian Mountains.

“I’d only heard about them. This is the real thing. Wow…”

Hyuk Mujin murmured, sounding dazed.

But he wasn’t the only one. Everyone was staring in wonder, myself included.

Sheer cliffs and a mountain range that stretched on without end, like the body of a dragon. Between them, peaks rose so high they pierced the clouds, as if holding up the sky.

And that wasn’t all.

The perpetual snow that painted great swaths of the mountains white gave the place an otherworldly air, as though we’d stepped into a completely different world.

Yet the narrow gorges between the cliffs were so long and constricted they looked like the entrance to hell. This was nothing less than a natural fortress, built by nature itself.

*This is even more than I’d heard.*

The Eight Spring Gorge, which had changed Shanxi’s fortunes time and time again, would have looked like a hill behind the village compared to the Qilian Mountains before us.

But the drawbacks were just as obvious.

“It’s too vast.”

At Song Ilseom’s brief remark, I nodded quietly.

He was right.

The Qilian Mountains weren’t merely wide. They were immense.

The range stretched for thousands of *li*, beginning in southwestern Gansu and reaching all the way to Qinghai. If we spread out a hastily assembled net over such a wide area, it would be torn apart in an instant.

Especially if our target was a big fish like Dark Heaven.

So, as soon as we entered the Qilian Mountains—which were already surrounded by the Gansu martial artists’ tight defenses—the leaders gathered in one place to discuss this problem first.

Or, more precisely, Jeok Cheongang and I did.

“There are too many troops stationed in the rear for what they’re meant to do. So, what I’m saying is—”

“Pull them out. All of them.”

Jeok Cheongang cut in before I could finish. He picked at his ear, then added,

“I had a bad feeling when I heard about it, but seeing it in person confirms it. Even if we threw every last man at the Great Snow Mountain and Dunhuang into this, we couldn’t completely seal off this place. Our best move would be to pull everyone together and throw them at another front.”

Jeok Cheongang swept his gaze over the gathering like a landlord telling a troublesome tenant to get out. Then his eyes came to rest on one man.

“I thought you’d know this much already. Was I mistaken?”

The Black Night King, Sima Gong, answered with a gentle smile.

“Thank you for your generous opinion of me. But I, and the many Sect Leaders and Family Heads gathered here, know the Gansu region better than anyone. The Qilian Mountains included, of course.”

“Know it better than anyone…”

Jeok Cheongang quietly repeated Sima Gong’s words, as if turning them over in his mouth, then spoke evenly.

“That sounds like you’re telling me to shut up if I don’t know enough.”

“How could we dare show such disrespect to you, Senior Jeok—not you, of all people? Please, take back your words.”

“Please calm yourself, Great Hero Jeok.”

“It’s simply a matter we decided after thorough discussion.”

After Sima Gong’s smooth apology, the Sect Leaders and Family Heads of Gansu Murim, who’d been watching for a cue, took turns clasping their hands in salute.

Like lackeys following their boss.

And that was when, as I silently watched the scene before me, I noticed the only one among them sitting with his back straight.

*Sama Pyo.*

For a moment, his unreadable expression met my gaze. Then Sama Pyo quietly lowered his head, following his father’s lead.

*Swish.*

Perhaps it was the sudden silence that made the sound of clothing brushing together ring unusually loud.

The Wind-and-Cloud Sword Lord spoke.

“It’s difficult for this poor Daoist to make a judgment so easily. Everyone here is a leader of Gansu Murim, and I would like to believe you’ve reached the right decision. But… what Senior Jeok has said also seems entirely possible.”

“Not just possible. I’d say it’s more than likely.”

At my sudden remark, everyone turned to look at me. I continued without the slightest embarrassment.

“Even if we have thirty thousand allied troops and several thousand more, splitting them up to maintain three separate fronts means we won’t be worth a damn anywhere. There’s a reason people say you survive by sticking together and die when you scatter.”

“Thank you. For reminding us all of the most basic principle, which everyone here had somehow completely forgotten.”

The Roaring Fury Swordsman spoke with a derisive chuckle. I shrugged at him.

“You really don’t have to thank me that much. People forget things from time to time when they get old. Though this is a pretty basic principle.”

“……!”

“Oh, sorry. Was that too cheeky?”

I hadn’t said it to get under his skin. I meant it.

Seeing the Roaring Fury Swordsman’s face turn red, I realized I might’ve gone too far—but what could I do when the words just came out on their own?

Well, we were all on the same boat now. He’d understand.

Or not.

“You—no, you…”

Maybe the cheek of a young punk talking back had made his blood boil. The Roaring Fury Swordsman glanced at Jeok Cheongang, and seemed to be starting to hyperventilate. Someone else stepped in for him.

“Stick together to live and scatter to die. That’s true enough. But not in a situation like this.”

I guess that’s what having fellow disciples was good for.

I looked straight at the Taeeul Merciless Sword, who’d stepped in at just the right moment.

“What kind of situation do you mean?”

“Are you asking because you don’t know, or because you know and are pretending you don’t?”

The Taeeul Merciless Sword frowned and continued.

“You seem to have forgotten already what kind of monstrous dark arts they wield.”

Nobody here failed to understand what the Taeeul Merciless Sword meant. I certainly hadn’t.

“The Moving Formation. Right. They have that.”

I nodded, then spoke again in a perfectly calm voice, as if nothing were wrong.

“So?”

“What!”

“What did you say?”

Questions burst out from all sides at once.

But if I hadn’t expected this kind of reaction, I wouldn’t have brought it up in the first place.

“On the way here, I thought of something I wanted to ask…”

I let the words trail off and slowly looked around the gathering.

“If you’re so wary of the Moving Formation, why did you station an army of over thirty thousand in the front in the first place?”

“……!”

For an instant, a quiet silence pressed down on the air around us.

It didn’t lift until someone, who’d been watching the situation with calm eyes, suddenly spoke.

“For the greater good.”

The Black Night King, Sima Gong. Him again.

Speaking on everyone’s behalf, Sima Gong continued in a low, steady voice.

“What you said earlier was right. If we spread ourselves out carelessly, we’ll accomplish nothing. So we put our heads together and considered it carefully, and this is the conclusion we reached: divide our forces among three fronts, so they can return to the rear at any time.”

At first glance, it sounded reasonable.

It was the same proposal that had come up when the leaders first gathered.

But…

That was only true, as I’d just said, *at first glance*.

“It seems like a long way to go back. If Dark Heaven appears in the rear through the Moving Formation, how are we supposed to catch up with them?”

If a swarm of tens of thousands of locusts descended on a field, it wouldn’t take even half a day for everything to disappear.

Dark Heaven was that swarm of locusts.

And their fangs and wings were too savage and fast for us to make up a delay of several days and catch them.

*By the time our allies arrived, Gansu would already be laid waste, and Dark Heaven would be heading for the Central Plains.*

But did those men really not know this? Men whose families had been fixtures in Gansu for decades, even more than a century?

*Of course they knew.*

They had to.

And the next words that came from Sima Gong’s lips were enough to turn my suspicion into certainty.

“They would. Certainly.”

“……!”

“……!”

At that brief reply, Jeok Cheongang and I understood what he meant, and our gazes grew intent. But not everyone understood. The Wind-and-Cloud Sword Lord, for one, was looking at Sima Gong with a puzzled expression.

“Lord Sima. What exactly do you mean by that…?”

His words trailed off unfinished.

But the Wind-and-Cloud Sword Lord was the leader of the Zhongnan Sect, a great sect in his own right. Before Sima Gong’s words had even faded, a suspicion occurred to him, and his face stiffened.

“Are you saying we’ll just let it happen? Even if they use the Moving Formation to bypass our lines and ravage the rear?”

Sima Gong answered with an even expression.

“Let it happen? That’s an absurd accusation. We’ve simply chosen the option with the best odds of victory.”

“Wait. Then what happens to the rear? The common people and martial artists who remain there?”

“That’s why I said it. For the greater good.”

“Lord Sima!”

*Crash!*

The chair shattered in an instant.

But even as the Wind-and-Cloud Sword Lord shouted and sprang to his feet, Sima Gong’s voice didn’t waver in the slightest.

“If Dark Heaven crosses the desert and attacks us head-on, we’ll immediately concentrate every force there. They could use the Moving Formation to take the rear… but that would be the worst move they could make.”

A fish that tore through a net from the outside could come and go as it pleased. But if it passed through the net as if by teleportation, it would only end up trapped inside.

*A two-front war.*

That was Sima Gong’s plan.

Effective, but one that would demand enormous sacrifice.

A truly unorthodox scheme.

But…

Could that be all there was to it?

“Whether we defend this place or burn it to the ground is our choice. Zhongnan Sect doesn’t own this land. Neither does the Jin Family of Taiyuan.”

Sima Gong’s icy gaze silenced the Wind-and-Cloud Sword Lord. I watched him, my own gaze sinking deep.

[^1]: The Yellow River running clear is an exceptionally rare, auspicious event; here, the phrase conveys the hope of meeting again.
## Chapter artifact 1017

# Chapter 1017

Sima Gong and the leaders of Gansu Murim had made their position perfectly clear:

- Don’t go demanding this and that in someone else’s territory.

Honestly, there wasn’t much room to argue with that.

Every one of them was an old fixture who’d ruled Gansu Murim for decades at the very least, and some for more than a century. Besides, ever since the Great Faction War, interfering too much in another sect’s affairs had been taboo.

And then there was the Black Dragon Demon Gate, standing at the center of it all. What kind of place was it?

Despite its relatively short history of only a few decades, it wielded tremendous influence throughout Gansu. It was, without question, a pillar of the unorthodox faction.

At least in Gansu, it stood shoulder to shoulder with the Kongtong Sect, one of the Nine Sects and One Gang. In fact, it might have built an even stronger power base by now—a true regional overlord.

With Sima Gong, the beginning and end of the Black Dragon Demon Gate, speaking so frankly, even the Wind-and-Cloud Sword Lord had no choice but to back down after briefly letting his anger show.

But not the one who had watched it all without so much as twitching an eyebrow.

“Why are you growling so much? You sound like a yellow dog whose food bowl’s been taken away.”

There was only one person here who could compare the Black Night King himself to a yellow dog.

The Fire King, Jeok Cheongang.

At last, the giant who’d left his mark on the distant history of Murim parted his lips. The icy gleam in Sima Gong’s eyes settled.

“I suppose I should. If I can protect my food bowl, I’ll do whatever it takes.”

“And it never crossed your mind that someone else’s life might depend on that food bowl?”

“It’s for the greater good.”

“You mean your own good. The good of a select few who follow you and the Black Dragon Demon Gate.”

Jeok Cheongang slowly looked around the room.

There were around twenty people here, not counting the Zhongnan Sect and the Black Dragon Demon Gate.

As Jeok Cheongang looked from one leader of Gansu Murim to the next, an unmistakable sneer curled his lips.

“Come to think of it, isn’t it strange? As I understand it, Gansu has at least fifty sects and martial families, yet not even half of them are here. Ah… were the others already sent to the other fronts?”

“They’re already carrying out other assignments,” Sima Gong answered in a dry voice.

“So they were left behind. To delay Dark Heaven for even half a day if it uses the Moving Formation to appear in the rear.”

“Everyone agreed to it.”

“And before you got that agreement, did you lay out all the facts? Or did you go straight to drawing your sword?”

“With all due respect, there’s something I’d like to say while we’re at it.”

“‘With all due respect’ already puts me in a shitty mood, but I suppose that’s what you’ve got a mouth for. Go on, then. Spit it out.”

At Jeok Cheongang’s continued string of barbs, Sima Gong let out a short breath. Then, with a calm expression, he began.

“We of Gansu Murim will not accept interference from outsiders in this decision, in any form. Even if that interference comes from one of the Nine Sects and One Gang or the Five Great Families. Or…”

Sima Gong’s gaze swept past the Wind-and-Cloud Sword Lord and me, then finally came to a dead stop on Jeok Cheongang.

“Even if it comes from you, Senior.”

“……!”

“……!”

The air around us lurched.

Stiffened hands and feet came standard. The slight bobbing of people’s throats was an added bonus.

Even if it was Sima Gong, who was he speaking to?

Jeok Cheongang, the Fire King himself.

A terrifying old monster who ranked among the top five in the Central Plains in martial arts—and was said to be number one when it came to having a foul temper.

He’d answered Jeok Cheongang in a tone that was downright challenging. No wonder everyone reacted as if they’d been burned.

Everyone except me.

*This is far enough for today.*

I’d been watching events unfold the whole time, and I made up my mind.

Then, at a moment nobody could have expected, I suddenly clapped my hands together with all my strength.

*Clap!*

The sharp sound broke the silence, short and yet seemingly endless. Everyone turned toward me, startled as if they’d just woken from a dream. I blinked at them with perfect composure.

“Oh, sorry. A damn mosquito was buzzing around.”

Of course, I was lying.

With perennial snow on the ground, what damn mosquito?

But the point was that my sudden outburst had instantly relieved the tension, which had been plunging toward the abyss.

And the two men at the center of it understood the meaning behind my clap at once.

“You’ve grown some brains, I see. You’ve come a long way.”

At last, Jeok Cheongang’s low voice slipped from between his lips. Sima Gong, as if nothing had happened, respectfully clasped his hands in salute.

“I still have a long way to go. I hope you’ll look kindly on this inadequate junior.”

Jeok Cheongang looked at me, put on a frown, and spoke.

“You certainly do have a long way to go. The road ahead is full of trouble, after all. Isn’t it?”

“With you here beside us, who needs an army?”

Sima Gong put particular emphasis on the word *beside*, then suddenly lifted his head and looked at me.

“You truly have an exceptionally perceptive Disciple.”

“I don’t know about perceptive. He’s got a good sense for reading a room.”

“Remarkable martial prowess, and a mind that sees several moves ahead. He’s a blessing to all Murim. My son ought to have spent more time watching and learning from you while he had the chance… What do you think of him?”

At Sima Gong’s sudden question, I answered without hesitation.

“He’s useful.”

“What?”

“Now that I’ve spent some time with him, he’s a pretty decent kid. A little gloomy, though.”

By Murim’s reckoning, Sama Pyo was much older than me.

But even though I’d just thrown the whole idea of respecting my elders to the dogs, Sima Gong only smiled in a way I couldn’t quite read.

“Thank you for saying so. It makes all the effort I put into raising him worthwhile.”

Over his shoulder, I saw Sama Pyo standing there without a trace of expression. It made me wonder if Sima Gong meant he’d raised his son as a father—or if he sounded more like a craftsman talking about a piece he’d made.

But the thought vanished as quickly as it had come, and I spoke again.

“So, you don’t plan to change your current judgment?”

“Decision. A choice made by firmly settling on a course of action or attitude.”

“So that’s a no. Then can I assume the Kongtong Sect’s position is the same?”

“The Kongtong Sect opposed it, but that changes nothing. All of Gansu Murim reached this decision after extensive discussion.”

Maybe. Was this really what Gansu Murim wanted?

Or…

*Was it only what the Black Dragon Demon Gate wanted?*

I swallowed the words hovering on the tip of my tongue and thought for a moment.

*Inventory.*

I mentally felt for an item stowed somewhere in that bottomless, pitch-black subspace.

But then I shook my head.

No matter how I looked at it, the timing wasn’t right yet.

Not now, at least.

“Then let’s do that.”

“What?”

The surprised question came from neither Jeok Cheongang, who was frowning, nor Sima Gong.

It was the Wind-and-Cloud Sword Lord. He stared at me with wide eyes.

“You’re willing to accept this as it stands? Are you serious?”

Right then, before I could answer, two other voices cut the Wind-and-Cloud Sword Lord off.

“Every group has its own rules, wherever you go. Just as our Zhongnan does.”

“Senior Brother is right. Junior Brother, as the Sect Leader of our sect, remember once more how you should conduct yourself.”

The Roaring Fury Swordsman and the Taeeul Merciless Sword.

Those were the two.

After his Senior Brothers spoke in turn, the Wind-and-Cloud Sword Lord muttered as though groaning.

“Senior Brothers. But how can we let this happen?”

“We can well imagine how you feel, Sect Leader. But we must tell you that further discord may jeopardize the greater cause.”

Sima Gong calmly but firmly cut off the Wind-and-Cloud Sword Lord before he could continue. Then he surveyed the room and went on.

“I hope everyone will remember this. We are allies united beneath the Murim Alliance’s banner, and we must not create discord over a decision that has already been made. Much less…”

Sima Gong’s deeply lowered gaze suddenly came to rest on me.

“Should anyone act unilaterally without seeking everyone’s agreement. Wouldn’t you say?”

I already knew what Sima Gong meant, so I nodded.

“I’ll keep that in mind.”

“I hope sending those horse caravans away wasn’t a grievous mistake for our allies.”

“There won’t be any problem. At least, if my expectations are right.”

“His name was Ma Junggeol, wasn’t it? If you’d let that man go as well… we would’ve been disappointed in you. Very disappointed.”

At the sudden drop in his voice, Jeok Cheongang’s eyebrow twitched. But I discreetly tugged at his sleeve from where Sima Gong couldn’t see, then shrugged.

“I’ll remember.”

After that, the meeting wrapped up in less than another fifteen minutes.

As the leaders of Gansu Murim filed out, they kept stealing anxious glances at Jeok Cheongang. He stayed silent, his face like someone suffering from a particularly nasty case of constipation.

Only after we’d escaped the eyes of everyone around us, leaving just the two of us, did he finally speak.

“What are you plotting?”

“What do you mean?”

“Don’t change the subject. You had something in mind, or you wouldn’t have tried so hard to hold this old man back.”

“I didn’t try to hold you back. I just gave you a look to calm you down.”

“What?”

“Were you planning to grab him by the collar and beat the crap out of him right there? The Sect Leader of the Black Dragon Demon Gate, no less?”

“Why? You think this old man couldn’t do it?”

“……”

Fair point.

My words caught in my throat for a moment. I let out a deep sigh, then resumed walking.

“There was something bothering me.”

“That would be Sima Gong. You can tell just by looking at that bastard’s face.”

“That’s not it. He’s hiding something.”

At my quiet words, Jeok Cheongang’s expression hardened too.

“What do you mean… Wait. Don’t tell me—”

His voice grew louder as he reached the end of the sentence. I gave a small shake of my head.

“Don’t jump to conclusions. I’m not sure yet.”

“Tell me everything. Don’t leave anything out.”

“Do you remember how Elder Nam suddenly came to see me a day ago and said he had something to discuss?”

“Of course. I suddenly had to relieve myself, so I didn’t hear him out.”

Jeok Cheongang furrowed his brow and continued.

“If it was that important, you’d have told me later. Why haven’t you said a word about it for more than a day?”

He was right.

I’d always discussed most important matters with Jeok Cheongang, and sometimes we’d even found the answer together.

But…

*There are exceptions.*

That day, that moment, was one of them.

*“It’s important. Something I can only tell you now.”*

Namho had approached me suddenly and, speaking in a hushed voice, told me something I hadn’t expected.

*“Just before we left the Jin Family of Taiyuan, I went looking for Sama Pyo because he was missing. Taishan was with him.”*

And there, the old agent of the Hidden Shadow Pavilion had caught a smell that was both familiar and strange.

*“There wasn’t a trace of anything, but I’m certain Sama Pyo was burning a missive.”*

No—by the time Sama Pyo had tried to hide it, it had already been more than an ordinary missive.

It was a secret letter.
## Chapter artifact 1018

# Chapter 1018

“He was burning a secret letter alone, without anyone knowing.”

The words slipped from my lips in a low murmur.

Jeok Cheongang’s gaze, fixed on me, had grown dark and still.

“Could Namho have been mistaken?”

“That…”

I closed my mouth instead of finishing the sentence. Jeok Cheongang let out a quiet sigh.

“Damn it. So it’s true.”

At first, I’d thought the whole thing was just a simple misunderstanding.

A minor incident we could clear up by calling Sama Pyo over and talking to him directly.

But…

“Elder Nam was already certain.”

“I thought so. If he’s only just brought it up with you, he must have given it a great deal of thought until now.”

“Yes. At first, even he wasn’t sure. There wasn’t any solid evidence to back it up, either.”

Growing old meant the senses grew dull.

Namho had said he’d agonized over it again and again.

Whether the familiar smell he’d encountered over and over as an agent of the Hidden Shadow Pavilion was the same kind as the one that had lingered in Sama Pyo’s room.

Whether his dulled senses were leading him to make a baseless accusation.

And after more than seven days and nights of worry, this old Hidden Shadow Pavilion agent had reached only one conclusion.

*“It was definitely the smell of oiled paper burning. I’m certain now.”*

Oiled paper—paper treated with oil.

It was customary to soak missives in oil to keep them from getting wet or torn, and naturally, they smelled different when burned from dry paper.

*“Another reason to oil paper is that it burns easily. The more a letter must not be discovered, the more important it is to destroy the evidence quickly.”*

Namho had spent decades as an intelligence agent.

Though he’d found no trace of anything beyond the faint smell of something burning in the room, from that moment on he never let go of his suspicions about Sama Pyo and Taishan.

*“I watched them closely from the day we left Shanxi Province, but until just a few days ago, I still couldn’t be sure. Whether it really was oiled paper burning—and, if so, who had sent it, and from where.”*

But there was another, more important reason Namho had hesitated to reach a conclusion.

“He said the scent was unusual.”

“The scent? You mean the smell of the paper burning?”

“Yes. He said it was quite different from the various kinds of burning smells he knew.”

“Burning paper smells like burning paper. What does that—”

“I’ve heard each region has its own particular traits. Its customs, its food, and even the animals whose fat is used to make oil.”

At my quiet addition, Jeok Cheongang suddenly furrowed his brow.

“Wait. Could it be?”

“Elder Nam said there are animals found only in Gansu and Qinghai. Is that right?”

“Camels…!”

Jeok Cheongang gave a muffled gasp and nodded.

“So that’s what it was. The source of that unusual scent.”

“Since he’d spent his whole life in the Central Plains and Nanman, it wouldn’t have been easy for Elder Nam to tell the difference.”

“That’s right. Those oddly shaped beasts are hard to come across, since they live only in Qinghai and western Gansu.”

Besides, in Murim these days, it was common to use animal fats from cows, horses, sheep, and pigs.

But the day we first entered Gansu Province, Namho had been resting for a while with the other members of the Fire Dragon Pavilion when he stumbled upon an unexpected clue.

*“It was an incredible coincidence. I’d lost my appetite and was sitting by myself, lost in thought, when a familiar smell started wafting over. I asked what it was, and they told me it was camel meat.”*

That was how the clues came together. Once Namho had finally become certain, he told me what he’d found.

Sama Pyo had received a secret letter from someone, and it had almost certainly been sent from Gansu or Qinghai.

As for the exact identity of the person who had sent it, everyone who knew about the letter had already formed a vague guess.

Namho had mentioned Qinghai as well as Gansu only as a possibility. There was only one person who might send a secret letter all the way to Shanxi Province, thousands of *li* away.

“The Black Night King, Sima Gong…”

At my murmur, which sounded almost like I was talking to myself, Jeok Cheongang spat roughly.

“You’ve gotten bold. You really have.”

“What do you think the letter said?”

“Do you have a guess?”

“I do.”

“Then tell me.”

“At the very least, I’m pretty sure it wasn’t something like, ‘Is my son eating well?’”

In an instant, a vein bulged at Jeok Cheongang’s temple.

“You call that an answer? Even that Taishan—or Gangsan, whatever his name is—could tell you that.”

“Taishan might not.”

“……Honestly, I can’t argue with you on that one. Speaking of that oversized fool, how was he on the way here?”

“Elder Nam said he was definitely acting strange, based on what he’d observed over the last few days. The closer we got to Gansu, the less he ate, and he stayed gloomy all day.”

Of course, there was a slight—no, a considerable—problem with saying he ate less.

He was still stuffing his face five times a day. How was that eating less? That was eating plenty.

But considering how much Taishan usually ate, five meals a day was basically intermittent fasting.

And the closer we got to Gansu, the more miserable he looked. There was no shortage of things that seemed strange.

*Knowing Sama Pyo, he might’ve kept it from Taishan, too.*

Whatever the case, only one thing mattered most right now.

While they were still in Shanxi Province, a secret letter containing some hidden message had passed between father and son. And whatever it said, it certainly wasn’t a hopeful or positive development for us.

I didn’t want to think this way, but if the absolute worst happened…

“Hmm.”

I shook my head, trying to force the thought from my mind.

Jeok Cheongang had been watching me closely. Then he abruptly spoke.

“Are you worried?”

“About what?”

“About having to cut down Sama Pyo and Taishan with your own hands.”

“……!”

*Step.*

Without realizing it, I stopped walking.

I’d been walking almost mechanically, but now I stood stock-still, staring silently at Jeok Cheongang.

“You look like you have a lot to say.”

“……”

“Since you’ve clammed up, let this old man tell you an interesting story.”

I didn’t answer, and Jeok Cheongang didn’t wait for one.

“During the Great Faction War, when the world was going up in flames, I came to know a man called the Junzi Saber.”

We started walking again, and I replied, my voice troubled.

“That’s quite a title.”

“Like hell it is. At first, I didn’t care for it much. The title was so embarrassingly grand it made my fingers curl up—and nearly break. But after spending some time with him, cutting down Demonic Cult bastards, I found he was a pretty useful fellow.”

“What do you mean, useful?”

“Both as a person and as a martial artist.”

“That’s quite a compliment. Especially coming from you, Old Master.”

“People thought even more highly of him. He came from a once-prominent martial family, though it had fallen into decline. His personal skill and sense of justice were exceptional, and he always led the way in even the most dangerous situations. He never backed down.”

In other words, he’d been the very model of a chivalrous hero.

The first to charge in, the last to retreat, living out the spirit of self-sacrifice with his whole body.

But I already had a feeling how this story, which had come out of nowhere, would end.

“Why are you talking about him entirely in the past tense? You sound like you regret what happened.”

A bitter smile passed over Jeok Cheongang’s lips.

“You’re a sharp one.”

“Was he a traitor?”

“Yes. He was a Demonic Cult lackey. But he hadn’t been one from the beginning.”

“You mean…”

“Do you remember what I told you about the Junzi Saber’s origins?”

“Yes. He was from a prominent martial family in Qinghai.”

“In truth, his family had been completely destroyed in a war with another sect. ‘Scattered to the winds’ would be more accurate. The only family he knew was an old retainer who’d raised the infant Junzi Saber by begging for breast milk.”

The only family he *knew*.

It suddenly made sense.

Why that chivalrous hero from the past had ended up under the Demonic Cult’s shadow.

“There was a surviving relative.”

“His eldest brother, apparently. He was the Lesser Family Head, yet survived the family’s destruction. You’d have to call him blessed by fate. He crossed the desert and sought refuge with the Demonic Cult, armed with that luck—and a thirst for revenge even greater than it. …You’re sharp enough to guess what happened next.”

Why did it feel like I could see the Korean flag waving before my eyes?[^1]

A classic movie I’d seen long ago came to mind—but only for a moment.

[^1]: *Taegukgi* (“Korean flag”) is the Korean title of a film about brothers caught up in the Korean War.

Unlike that movie, which had made me cry my eyes out, this story’s ending would be different.

And that ending was why Jeok Cheongang had dredged up an unpleasant memory from his past.

“The Junzi Saber must’ve died.”

Jeok Cheongang answered in a low voice.

“Yes. I killed him myself.”

“Do you regret that choice?”

“Regret it? What would you have done?”

“……!”

“If Sama Pyo and Taishan are plotting something on Sima Gong’s secret orders—and those orders are connected to Dark Heaven… what would you do?”

I fell silent.

A mere year.

It wasn’t long enough to form a deep bond. We’d lived in different circumstances, and we had different personalities.

But why?

No answer came easily through my tightly pressed lips.

Though it was a question I should have answered without hesitation.

*What would you do?*

Jeok Cheongang’s question echoed in my ears, colliding again and again without end.

* * *

Around the time the three thousand troops, after several days of nonstop marching, reached the Qilian Mountains and were taking a brief but sweet rest—

In a pitch-black secret chamber where not a single ray of light could enter, three people faced one another.

“Things have gone wrong. Very wrong.”

“The Fire King—that damned old monster—what’s he doing here?”

Two voices came flying at once as soon as the others had taken their seats. The person occupying the seat of honor answered.

“What’s done is done. The situation has changed, so I’ve summoned the two of you to come up with a new plan.”

“Things have gone badly from the start, yet you’re brimming with confidence without offering a single excuse.”

“This time, Sect Leader Sima, you’ll have to give us a reason to accept this.”

“……Accept it.”

The eyes of the person in the seat of honor—no, the Black Night King, Sima Gong—suddenly gleamed.

He stared into the darkness at the two old Daoists facing him.
## Chapter artifact 1019

# Chapter 1019

Boom, boom, boom.

As the rough beat of drums began to echo across the rugged ridges of the Qilian Mountains, one by one, the people who’d realized their sweet rest was over got to their feet and began to assemble.

Naturally, Jeok Cheongang and I—and the members of the Fire Dragon Pavilion—were no exception.

The only difference was that, thanks to our small numbers, we had a little more breathing room.

“Whew. Still, even a quick nap helped a lot. Don’t you think?”

Hyuk Mujin had just woken up and stretched until he was practically dangling when he asked me. I answered in a calm voice.

“Yeah.”

“Huh? You say that, but you look awfully gloomy.”

“Your imagination.”

“Doesn’t look like my imagination. You don’t seem to have slept at all.”

“No. I’m just not fully awake yet.”

“Man, you should’ve slept, even if it was only for a little while. Sleep is the best medicine at a time like this.”

“……Are you not hearing me?”

Did this bastard have himself on mute or something?

At my incredulous stare, Hyuk Mujin shrugged.

“Oh, come on. I could tell the moment I saw your face, Captain. You’ve got something on your mind, right?”

Sharp as a tack, isn’t he.

But no matter how he asked, my current position meant I couldn’t just come out and tell him the truth.

Think about it.

What would the Fire Dragon Pavilion members do if they learned the truth about Sama Pyo right now?

*The more people who know, the harder it is to keep a secret.*

Just as Hyuk Mujin had picked up on something the moment he saw my face, someone watching us might do the same.

Worries in your heart tended to show through, one way or another.

In the end, my answer to Hyuk Mujin in a situation like this had been decided from the start.

“When anything could happen at any moment, is it even human to have nothing to worry about? Huh?”

“Well, I guess you’ve got a point. It’s just that you seem a little different from usual, Captain.”

Hyuk Mujin scratched the back of his head at my unassailable logic, then hesitantly opened his mouth.

“But, Captain.”

“What? You have something important to say?”

“No, it’s not that important. I just wanted to tell you that I’m not worried about anything.”

“What?”

“You said it just now, didn’t you? If you have nothing to worry about in a situation like this, are you even human?”

“So?”

“I don’t know what you’ll think of this, but ever since I started following you, for some reason I haven’t really felt that way. Maybe it’s because I’ve been through so much that my guts have swollen up like a waterlogged balloon, but, well…”

Even as he spoke, Hyuk Mujin kept glancing at me, fidgeting. Then he looked toward a distant mountain and murmured as if to himself.

“Since you’re always by my side, and I trust that you’ll fight alongside me every time, I’m not afraid no matter how dangerous things get.”

“……”

“Ah, of course, don’t let what I just said put any extra pressure on you. What I mean is… Well, I mean…”

Maybe the awkwardness had gotten to him. Maybe his thoughts had gotten tangled up.

I watched Hyuk Mujin struggle to find the words, then spoke for him.

In my usual, deliberately curt voice.

“Don’t get caught up in pointless worries. I’ve always trusted you. That’s basically what you’re trying to say, right?”

“That’s… right.”

“What’s so hard about saying that? You’re old enough to know better.”

Hyuk Mujin looked indignant at my sudden attack on his age.

“Hey, show me some respect as your senior before you say that. What, has your conscience sprouted hair?”

“Mujin.”

“What?”

“Get in formation before I pluck every last hair from down below. Can’t you hear the drums telling everyone to assemble?”

“……Honestly, if someone who didn’t know us heard that, they’d think I was the only one who talked the whole time. You said plenty yourself.”

“What was that?”

“Ah, I’m going! I said I’m going!”

Watching Hyuk Mujin dash off with his lips stuck out, I couldn’t hide my quiet laugh. I muttered under my breath,

“You can speak casually when you say you’re going, huh?”

But my words reached no one. They scattered into the air, and the pale breath that escaped with them briefly obscured something falling from overhead.

Plop.

A moment later, I felt a cold touch.

I looked up. Between the clouds of every size scattered across the sky, countless snowflakes were falling.

Boom, boom, boom.

Following the drums as they sounded again right on cue, I resumed the steps I’d paused.

Repeating in my heart Hyuk Mujin’s words: that he trusted me, no matter the situation.

And at the same time, thinking of the two people who weren’t here.

*Was it because I hadn’t shown them enough that they couldn’t trust me? Or…*

Had I been the only fool to think that we’d become dependable comrades and friends?

Crunch.

I stamped down hard on the ground, which was already turning white beneath the falling snow.

* * *

When the nonstop drumbeats finally stopped, the number of people and horses heading west over the Qilian Mountains had swelled so noticeably that anyone could see the difference.

Grind. Grrind.

The mountain ridges groaned under the movement of a massive force numbering thousands.

Sama Pyo had been counting the flags visible between the bare branches. He spoke abruptly just after they crossed yet another hill and emerged onto the wilderness once more.

“That’s unexpected.”

He offered no preamble.

But neither Sama Pyo nor the person he was speaking to thought anything of it.

It was normal between father and son.

“What is?”

His father answered without even turning his head. His son quietly watched his profile.

“That you agreed to their demands.”

“Their demands?”

“At the meeting, you even argued with them to get your way. Yet in the end, you reinforced our troops with part of the force stationed in the Qilian Mountains. Three thousand of them, no less.”

Sama Pyo was right.

When the drums announcing the end of the brief rest stopped, nearly half the Black Dragon Demon Gate’s martial artists stationed in the Qilian Mountains had already assembled ahead of them.

“Is that a problem?”

“I only find it surprising. It’s not like you.”

“Not like me?”

Only then did his father turn his head and look straight at him. Sama Pyo lowered his head slightly.

“It was only a small question that occurred to me.”

“Go on. Tell me what’s on your mind.”

“I thought you would never withdraw a decision you’d already made. Especially when dealing with outsiders.”

“Why did you think that?”

“Because that’s what I’ve seen you do all this time.”

“Raise your head.”

Sama Pyo obediently did as his father’s dry voice commanded. His father’s eyes, black as obsidian, were already gleaming at him.

“Have you forgotten already? I told you never to be certain about any situation—or any person.”

“……!”

“Sometimes the situation around you changes drastically. To survive and grow stronger in this harsh world, you must question everything and keep recalculating to account for new developments. This time is no different.”

A few years ago—or even just one year ago—Sama Pyo would have remained silent and listened to his father.

But why?

Today, Sima Gong’s voice, coming from right in front of him, seemed distant as an echo. Sama Pyo muttered inwardly,

*Keep questioning everything and calculating… You haven’t changed at all.*

Sama Pyo was reminded, painfully, of what kind of person his father was—and the kind of life he’d lived.

By questioning and guarding against everything, the Black Dragon Demon Gate had survived even the Great Faction War. Through calculations so precise there wasn’t a hair’s breadth of error, it had prospered immensely.

But anyone well-informed about the martial world knew.

The blood of one’s own family was included in the calculations and suspicions that had made Sima Gong who he was.

Seven older brothers and nine older sisters.

Thinking of the present circumstances of the children born to different mothers under the same father, Sama Pyo murmured inwardly,

*That’s right. It was thanks to that thorough calculation that I, too, became the Young Sect Leader.*

Sima Gong, the Black Night King, was that kind of man.

A man who stopped at nothing to survive and rule.

A man who would put even his blood relatives on the scales to weigh their worth, and unhesitatingly cast aside his other children to appoint the most capable, his seventeenth child, as Young Sect Leader.

That was what made him a man of the unorthodox factions in the truest sense. And beneath Sama Pyo’s skin ran the blood he’d inherited from him.

Like shackles that wouldn’t suffer even a scratch, no matter how desperately he struggled.

And beneath the immense weight of the iron ball chained to those shackles, Sama Pyo’s body and mind bent naturally under the pressure.

“I will keep those words, precious as gold and jade, deeply in my heart.”

It wasn’t a mere empty platitude or a ruse. The words came from deep within his heart, and his father sensed his son’s feelings just as clearly.

*Pyo, it seems that boy is finally coming to his senses.*

Sima Gong murmured inwardly and felt his spirits lift.

Who was Sama Pyo, after all?

The heir he’d finally managed to have in his old age, the one who would someday inherit everything from him.

His innate martial talent was no less than that of the Ten Dragons and Phoenixes, the greatest young prodigies in the Central Plains—no, it wouldn’t be an exaggeration to say it surpassed theirs. And his strategic mind was deep as well. He was a born leader.

*But something started to change in him after he joined the Fire Dragon Pavilion.*

His first act of defiance.

Without any command or permission from Sima Gong, the Sect Leader, his son had joined the Fire Dragon Pavilion on his own. By the time Sima Gong found out, the deed was done.

The Fire Dragon Pavilion and the Azure Dragon Pavilion were newly established strike forces under the Alliance Leader’s direct command.

A great many eyes were watching the actions of the two pavilions, as they were called. And the Fire Dragon Pavilion Sama Pyo had joined had *him*.

*Jin Taekyung.*

The Hidden Dragon of Shanxi, who’d risen to become the Divine Dragon of the world—a young giant of Murim.

Every step he took left a deep and massive imprint.

Wherever he went, the path behind him filled with the corpses and blood of countless enemies, followed by the praise and cheers of people throughout the land.

Sima Gong could only watch.

He’d hoped that his son’s sudden act of defiance might give the Black Dragon Demon Gate another chance to rise.

But the secret correspondence he should have received never came, and Sama Pyo’s attitude, when they met for the first time in a year, had seemed somehow different.

At least, until just now.

*Of course, I’ll have to keep watching him. But for the time being, I can breathe a little easier.*

And it was just as Sima Gong let out a quiet laugh to himself at the sight of his son gradually returning to his old self that it happened.

Shhhwick—BOOM!

A burst of red flame shot up over a barren hill several hundred *jang* away, then exploded, brilliantly coloring his eyes.

No—everyone’s.

# Checkpoint Review — 900–904

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

# Chapters 900–904

## Plot

At the imperial birthday banquet, the Emperor appears in public for the first time in years and names Prince Shangshan his heir. Jin Taekyung privately speaks with Cang Gong, who says the Fire King is needed to deal with So Gyo and confirms that Murim Alliance reinforcements have arrived.

Taekyung realizes the Emperor’s leniency toward him is meant to keep Shangshan safe. Cang Gong reveals that the Lord of Heaven is interested in Taekyung and displays an unfamiliar, chilling power. Taekyung attacks to signal the Fire King, but Cang Gong repels him. Jeok Cheongang arrives as the banquet hall erupts into battle: attackers disguised among the Embroidered Uniform Guard fire arrows at the hall and the Emperor. Taekyung burns the arrows away and fights through the attackers. Ma Sanbao kills several guards and confronts Taekyung, who strikes at him.

Meanwhile, Hyuk Mujin and the Fire Dragon Pavilion party travel toward the Jiangsu–Zhejiang border on Taekyung’s mission. Jeok Cheongang had warned them that Taekyung sent Mujin away for his safety. The group spots countless silent figures in a nearby forest.

## Continuity

- The Emperor publicly designated Prince Shangshan as his heir. Aehyang arrived under Embroidered Uniform Guard protection, visibly uneasy and touching her belly; the Emperor had said she was pregnant.
- Taekyung believes the Emperor forgave his disrespect to prevent Shangshan from being endangered. Shangshan still has the Myriad-Poison Ring.
- Cang Gong says So Gyo must be dealt with and that the Fire King is essential. So Gyo’s identity and allegiance remain unknown; she is with the Emperor and Baek Yeon.
- Cang Gong’s chilling power is unfamiliar and is not simply Yin-Cold Qi. He intends to take Taekyung to the Lord of Heaven, believing he can be recruited; the Lord of Heaven has shown interest in Taekyung.
- The banquet-hall battle is underway. Attackers infiltrated the Embroidered Uniform Guard and targeted the Emperor with arrows. Jeok Cheongang has joined the fight.
- Ma Sanbao killed several Embroidered Uniform Guards and confronted Taekyung. Taekyung attacked him; Ma’s allegiance and motives remain unclear.
- Hyuk Mujin and the Fire Dragon Pavilion party are headed to the Jiangsu–Zhejiang border on Taekyung’s mission. Countless silent figures have appeared near them in the forest.

## Translation Decisions

- Render 東廠掌印太監 as “Seal-Holding Eunuch of the East Depot”; retain “Cang Gong” for 창공.
- Keep Cang Gong’s confidential dialogue distinct from the public banquet through the sound-blocking internal-energy barrier.
- Render 鴻門宴 as “Hongmen Banquet.”
- Render 天上天下，萬魔仰伏 as “Heaven above, earth below. All demons bow in reverence.”
- Keep the incantation 아씨오 as “Accio.”

## Durable state

{
  "active_continuity": [
    "Cang Gong's unfamiliar chilling power is not simply Yin-Cold Qi; he intends to take Taekyung to the Lord of Heaven and believes Taekyung can be recruited.",
    "Attackers have infiltrated the Embroidered Uniform Guard, and the banquet-hall battle and assault on the Emperor are underway.",
    "Jeok Cheongang has joined Taekyung in the battle.",
    "Ma Sanbao killed several Embroidered Uniform Guards and confronted Taekyung, who attacked him; Ma's allegiance and motives are unclear.",
    "So Gyo's identity and allegiance remain unknown; she is beside the Emperor with Baek Yeon.",
    "The Emperor does not want Prince Shangshan endangered.",
    "Hyuk Mujin and the Fire Dragon Pavilion party are traveling to the Jiangsu–Zhejiang border on Taekyung's mission; silent figures have appeared in the nearby forest."
  ],
  "continuity_sources": [
    904
  ],
  "open_questions": [
    "Who is So Gyo, and is she an ally or enemy?",
    "What is the nature of Cang Gong's unfamiliar power, and what is his relationship to the Lord of Heaven?",
    "Why did Ma Sanbao kill the guards and confront Taekyung, and where does his allegiance lie?",
    "Who are the silent figures surrounding Mujin's group?"
  ],
  "safe_through": 904,
  "temporary_decisions": [],
  "version": 1
}

## Reading copies

## Chapter artifact 900

# Chapter 900

Thud. Thud-thud.

The earth trembled. Blazing torches roused the night.

A thousand Embroidered Uniform Guards marched in ranks, imperial flags flying overhead. Behind them came countless eunuchs and palace maids.

And at the center of it all was a magnificent, enormous imperial carriage, built for one person alone.

*Boom!*

At last, the thousand Embroidered Uniform Guards entered the Grand Banquet Hall and stamped their feet in unison.

The powerful waves of qi they unleashed at the same time shook the air and washed over everyone’s skin.

“At last…”

Those who heard the voice slip between someone’s lips suddenly wondered:

Who could that voice belong to?

Which side were they on, and what outcome were they waiting for?

But there was no time to think of an answer.

From the enormous procession that had stopped at the Grand Banquet Hall, someone slowly rode forward on a fine steed and let out a thunderous cry.

“The sovereign of the Great Nation, master of Heaven and Earth and all things beneath them, has deigned to appear in person! All civil and military officials, great and small, kneel and pay your respects to His Majesty the Emperor!”

*Whoosh!*

Not even the golden armor encasing his body or the helmet pulled low over his head could hide his truly overwhelming presence.

At the shout, infused with internal energy, from Baek Yeon—the Emperor’s right hand in name and deed, and Commander of the Embroidered Uniform Guard—everyone in the Grand Banquet Hall rose and knelt.

*Clatter.*

There were hundreds of civil and military officials, and thousands of soldiers already standing guard all around them.

They moved as if they were one body, bowing their heads to the ruler of this vast continent.

Even if, for some of them, it was nothing more than an empty show of respect, the fuse that would bring this banquet to an end had not yet burned all the way down.

“Long live His Majesty the Emperor.”

At Ma Sanbao’s quiet murmur, everyone soon joined in.

“Long live His Majesty the Emperor! Long live! Long, long live!”

It was then.

At the very end of that resounding cheer, the Emperor stepped down from his sedan chair and walked slowly through the human curtain of guards.

*Step. Step.*

His footsteps rang out with unusual clarity.

But those who bowed their heads couldn’t see the Emperor as he passed them. Only after the empty seat on the throne atop the lofty stairs had finally been filled could they straighten up and face him.

The ruler of all under Heaven, who had shut himself away in Qianqing Palace for years on end while attending to the affairs of state.

The Great Nation’s fourth prince turned rebel, then rebel turned Emperor: a notorious unfilial wretch and butcher who had finally seized the throne.

And a man of tempestuous fortune, standing at the highest place beneath Heaven.

They were stunned.

“……!”

“……!”

In an instant, an unseen shock and disturbance swept across the Grand Banquet Hall like a wave.

There was no trace of the Emperor’s once-youthful, handsome appearance in the man who had emerged after his long seclusion.

But the Emperor paid it no mind.

He looked down haughtily at the countless gazes fixed on him.

Though he had aged beyond recognition, his eyes shone brighter than anyone else’s in the hall as he surveyed the gathered officials, great and small, one by one.

The pillars that held up this vast empire. The very heart of the realm.

Among them were generals who commanded armies, and old scholars with stooped backs but unbending eyes.

Ma Sanbao, the East Depot’s de facto leader and the Emperor’s greatest adversary, was there as well.

But the last place the Emperor’s gaze fell was far off at the end of the hall, where a young man watched him in silence.

*Jin Taekyung.*

Their eyes met in midair.

The Emperor looked at Jin Taekyung. Jin Taekyung looked at the Emperor.

They stared at each other for a while without saying a word. At last, the Emperor’s firmly closed lips parted.

“Begin.”

Perhaps it wasn’t just a few people who imagined it.

*Boom. Boom. Bwoom!*

The drums heralding the start of the grand banquet sounded like war drums announcing the opening of a battle.

* * *

The atmosphere, frozen like a glacier, began to thaw little by little when musicians and dancers entered with an astonishing spread of delicacies and began to perform.

A melody that stirred the heart just to hear it, and sleeves fluttering in time with the music.

On top of that, the imperial chefs had displayed all their skill, and the finest wines were served without limit.

It was only natural that those who’d nervously downed a cup of wine would feel at least a little more at ease.

“Whew. I can finally breathe.”

“Indeed. I really thought something was about to happen…”

“Shut your mouth. You want to say something wrong and invite needless suspicion?”

“M-My apologies, sir.”

“If I hear you say something that disrespectful again, I won’t let it pass.”

The middle-aged man reprimanded the young official beside him in a carefully lowered voice, then swept a sharp gaze around them.

He seemed worried someone might have overheard.

I casually picked up a bite of food from the appetizer in front of me.

The next moment, I felt the middle-aged man across from me fixing me with an unusually persistent stare.

At the same time, the young official’s voice reached my ears.

“S-Sir. I did misspeak, but no one could’ve heard me. The Embroidered Uniform Guards are far away, too.”

He wasn’t wrong.

The hall being used for today’s grand banquet was large enough to hold training for thousands of soldiers at once. For that reason, the officials seated at regular intervals were also quite far apart.

And the Embroidered Uniform Guards were all exceptional masters. Only a few, including their commander, Baek Yeon, remained by the Emperor’s side.

The rest were far away, holding to their assigned positions.

But even after hearing the young official, the middle-aged man kept watching me closely for a while before asking,

“Do you know anything about that man?”

“Pardon? W-Well, I’ve heard in passing that he’s a ruffian from the martial world.”

“Is that all?”

“I’m not sure what you mean…”

“Tsk. Honestly, you never think. Be grateful that your father and I have a connection. Otherwise, you wouldn’t have made it this far.”

The middle-aged man clicked his tongue and continued, as he had all along, in a low whisper.

“How could some ruffian attend a banquet like this? He’s Prince Shangshan’s bodyguard and guest, brought here by His Highness. He’s also the third son of the Jin Family of Taiyuan, whose influence has recently spread all the way south of the Yangtze.”

“The Jin Family of Taiyuan. The Jin Family of Taiyuan… Do you mean the family that runs the Jin Family Trading Company and the Jin Family Escort Bureau?”

“That’s right. And that Jin Family of Taiyuan is based in Shanxi, Prince Shangshan’s fief.”

“Ah.”

The young official breathed out softly.

“A family of that standing must have considerable influence in Shanxi Province.”

“With Prince Shangshan’s protection, how could it be otherwise? Martial artists who defy the Great Nation’s solemn laws have no business wielding that kind of power… but apparently they rule as de facto overlords across Shanxi Province.”

“Is that why you’re paying attention to him, sir? Because he’s the son of a martial arts family?”

“It’s more than that.”

“Then…”

“Blazing Flame Divine Dragon. That’s his sobriquet. A tremendous master, barely in his twenties, who’s already accomplished countless feats of arms. There’s no one in the martial world who hasn’t heard of him.”

“You’ve done a fair amount of digging.”

“There was no need to look into it in detail. Even among the people of the imperial capital, there are countless who know of Blazing Flame Divine Dragon Jin Taekyung…”

The middle-aged man, who hadn’t taken his eyes off me as he spoke, suddenly frowned.

“Did you just speak casually to me?”

But the young official didn’t answer.

Normally, he would’ve scrambled to make excuses. Now, though, his face had gone white as he stared at the person standing behind him and the middle-aged man.

One second.

Two seconds.

Three.

After a silence in which the world seemed to stop, the middle-aged man slowly turned his head to follow the young official’s gaze.

Then he froze like a statue.

“Y-Your Majesty…!”

It was no illusion of mine that the words, forced from deep in his lungs, sounded like a scream.

The Emperor.

Like the title Son of Heaven, the absolute being called a descendant of Heaven looked down at the two men without a word.

As if considering how to kill them.

Perhaps he seemed all the more like it because Baek Yeon stood tall behind him—the very man who had led the purge of tens of thousands of “traitors” more than a decade ago.

“Y-Your Majesty. Please…”

*Flap.*

The voice cut off with the Emperor’s small gesture.

That was right. This arrogant and cruel absolute ruler still hadn’t spoken.

And he would allow no one to speak before him.

By now, the Grand Banquet Hall had fallen into deathly silence. The Emperor abruptly turned his head and looked at me.

“Jin Taekyung of the Jin Family of Taiyuan.”

“……!”

“……!”

I could feel it.

The air quivering.

Countless gazes piercing my entire body without mercy.

The Emperor had spoken first to me, the only outsider among the high officials who supported the empire and the gathered civil and military officials.

And he’d done it after walking all the way to the far end of the hall, where I sat in the lowliest seat, far from his throne.

“I ask you: what should I do with these people?”

If this had happened a few days ago, I would’ve been shocked.

Why the fuck is this crazy bastard pulling this shit out of nowhere? I probably would’ve thought something like that—and started to feel like I needed to piss.

But not today.

*Yeah. No.*

I’d already stepped into a gamble where each side had staked their lives.

The moment I entered the tiger’s den that was the imperial palace, perhaps all of this had been inevitable.

The time had come.

The die had been cast. Now it was time to see how it landed.

“Well, before I answer, would it be all right if I had a drink?”

*Haaaa.*

The air quivered again.

No, saying it quivered might not be quite right.

If the wave just now had been a small ripple from a stone dropped into a lake, this one was a disaster like a towering wave.

Everyone in the Grand Banquet Hall gaped as that wave swept over them in an instant. I looked at the Emperor, who gave a small nod, and spoke.

“Then I’ll take that as permission.”

*Gulp.*

The moment I tossed back the wine already poured into my cup instead of answering, cries of shock and angry shouts erupted from every direction.

That wave, which hadn’t felt real even when they’d seen and heard it themselves, had finally swept them up.

“What a lunatic!”

“H-How dare that man…!”

“How can there be such a lawless man in this world?”

“Commander of the Embroidered Uniform Guard, what are you doing? Why haven’t you cut down that high traitor yet?”

“Your Majesty! Punish that outrageous ruffian at once for insulting Your Majesty and the imperial household!”

“Please punish him!”

Listen to that decibel level.

They say the more people curse you, the longer you live. If this raucous enthusiasm had lasted even fifteen minutes longer, my sobriquet might’ve become Three Thousand Jiazi instead of Blazing Flame Divine Dragon.

Beheading was the basic option, and they kept piling on extras: cut off my balls, torture me slowly, then tear me limb from limb by quartering.

*…No, I mean, the balls are a bit much.*

Was that guy from the Sichuan Tang Clan or something?

I took a good look at the face of the man who’d proposed castrating me, then put down my cup.

Then I looked at the Emperor and spoke.

“Kill them if you want, or spare them if you want. Isn’t that what Your Majesty does best?”

Well.

I was starting to feel like I needed to piss.
## Chapter artifact 901

# Chapter 901

Silence.

A perfect silence settled over the grand banquet hall—not even the smallest breath could be heard.

Along with it came countless eyes, wide with shock, all fixed on one person.

*What… did he just say?*

*What on earth did I just hear?*

Everyone wondered the same thing at once. Looking toward the young man at the end of their gazes, they recalled the remark they’d just heard.

> “Kill them if you want, or spare them if you want. Isn’t that what Your Majesty does best?”

The words had rung out clearly enough for everyone in the hall to hear.

They doubted their memories once, twice, ten times, but reality refused to change. Forgetting all about decorum, people gaped at him, barely managing to swallow the curses on the tips of their tongues.

*That crazy bastard.*

Even calling him crazy fell far short of describing what that young man, Jin Taekyung, had just done.

He’d provoked the Emperor to his face.

Mocked him.

The Emperor, of all people.

The usurper who had cut down tens of thousands of political enemies like a farmer harvesting crops, then built the strongest centralized regime since Taizu, founder of the Great Nation.

*He’s insane. Completely, utterly insane.*

The officials in the lowest seats, their ranks too low to sit anywhere else, and even the high-ranking ministers at the heart of the political world all turned deathly pale and pressed their lips together.

Something had happened that could never be allowed to happen.

It wouldn’t be strange to call this treason. What came next was as plain as day.

They would die. Die, and die again.

Jin Taekyung and his entire family, along with everyone connected to them, would vanish like dew on the execution ground.

And there was a very good chance the names of several people with no connection to any of it would end up on the Embroidered Uniform Guard’s death list, too.

The late Emperor’s loyal subjects.

It wasn’t hard to predict that some of those who considered Prince Shangshan the rightful heir would become targets.

Evidence? Justification?

None of that mattered.

Evidence and justification could always be manufactured.

Once the pain of flesh and muscle tearing against the instruments of torture had them writhing, even the most loyal subject would beg for death.

The imperial torturers had the skill to turn lies into truth and truth into lies. The East Depot had once been responsible for that work, but that duty had long since passed to the Embroidered Uniform Guard.

In other words, the sword was in one man’s hands alone.

The Emperor’s.

With a single order from him, it would all be over.

Now that Jin Taekyung had given the Emperor grounds to punish him, it wouldn’t be strange if the blade he swung cut down anyone at all.

Even if the final target were Prince Shangshan.

*How could he do something this absurd? What on earth is he thinking…?*

*Grit.*

Some of the assembled officials, who had watched the whole unbelievable scene unfold, clenched their teeth to hold back groans.

Each of them either supported Prince Shangshan in secret or had signed the pledge and dreamed of a restoration. To them, the whole situation felt like a terrible calamity.

Jin Taekyung had entered the imperial court as Prince Shangshan’s guest. The prince wouldn’t be able to escape responsibility, either.

*Heh… So Heaven’s Mandate is leaving the Great Nation.*

Those who knew nothing about the restoration lamented the heavens, bitter with resentment.

*The plan’s gone off course, but there’s no choice now. At this point, we may have to act this very moment…*

Those who had signed the pledge steeled themselves. Their faces rigid, they watched Ma Sanbao, ready to move the instant he gave the order.

But then—

“Indeed. You are right.”

The Emperor’s words broke the long silence, and were enough to plunge everyone into shock once more.

“And one who wishes to become a sage king does not punish those who speak the truth.”

“……!”

“……!”

“Jin Taekyung of the Jin Family of Taiyuan.”

At the center of the quiet, the Emperor continued in an even voice.

“In the name of the Son of Heaven, I forgive you for the disrespect you have shown me.”

Forgive.

He’d said he forgave him.

The very man who had ruthlessly slaughtered tens of thousands.

The cruel Emperor who had launched a rebellion and a great purge.

Everyone who had been at a loss for words stared blankly at the back of the absolute ruler—everyone except one person.

Reading the sliver of emotion the Emperor hadn’t quite managed to hide from his face, Jin Taekyung muttered to himself.

*So this is how he’s playing it.*

Taekyung’s earlier provocation had been a gamble with his life.

If it failed, it could throw the restoration army’s entire plan into disarray.

*That’s why it had to be now.*

And the result of that dangerous gamble was a success.

He’d gained a crucial key, as important as the risk had been. The Emperor’s response was enough to answer the question Taekyung had hardly dared to ask himself.

*Forgiveness in a situation like this… That makes no sense.*

Except in one case.

Jin Taekyung quietly swallowed the rest of his thought.

The scattered pieces of the puzzle were coming together, one by one.

His head, which had felt ready to burst moments ago, was gradually clearing. His mind settled, calm, and a new path came into view.

Even so, not every question had been answered.

*But why on earth…?*

Jin Taekyung sent Sound Transmission toward the Emperor.

Or, more precisely, he tried to.

If someone hadn’t arrived just then, he might have managed it.

“It’s heartening to hear Your Majesty wishes to become such a merciful sage king.”

“……!”

Jin Taekyung reacted a little faster than the Emperor, and Baek Yeon faster still.

Somewhere only five *jang* away, an old man with pale skin appeared without a sound. In a hoarse, aged voice, he continued, cupping his hands toward the Emperor.

“The late Emperor would be pleased as well. Would he not?”

*Rustle.*

The old man slowly lifted his head, his long white hair swaying.

The Emperor’s stiff expression was reflected in eyes the color of ash, bearing the marks of many years. A dry voice slipped between cracked lips.

“Your servant, Wei Zhong, Seal-Holding Eunuch of the East Depot, pays his respects to Your Majesty.”

* * *

The moment I saw Wei Zhong, I reflexively thought of an old fantasy movie I’d watched as a kid.

A motley party of heroes from different races setting off on a journey to destroy a certain necklace, the source of the Demon King’s power, in a vast fantasy world.

And one of the central characters: an old mage.

“…Gandalf?”

The white hair that looked like it reached his knees, those gray eyes…

Strictly speaking, he was closer to “Gandalf who’s very sick,” but there was no denying the resemblance.

The slight problem was that the thought slipped out of my mouth before I could stop it.

*Ah.*

I realized what I’d done and shut my mouth, but it was too late.

Everyone’s eyes had shifted back to me—including the Emperor’s, and Wei Zhong’s, too.

“You must be the very man I’ve heard so much about.”

What was I supposed to say?

I thought it over for a moment, then gave a small nod instead. Wei Zhong let out a snort and turned back toward the Emperor.

“He truly is a rude man. Is he not, Your Majesty?”

But the Emperor didn’t answer.

He gazed at Wei Zhong with eyes sunk deep in thought, and only spoke once the air around them had grown so cold it seemed frozen.

“I was about to send someone to find you, since you were nowhere to be seen… It’s been a long time, Cang Gong. Have you been well?”

“After a rather long period of recuperation, I’ve finally recovered enough to move about. I owe it all to Your Majesty’s grace.”

“My grace, is it? Are you sure?”

“Even the finest physicians couldn’t guarantee your servant’s life. Seeing how much I’ve recovered, surely Heaven must have willed it. So I believe it is all thanks to Your Majesty, the Son of Heaven.”

“That’s unfortunate. If you’d had the decoction made as the imperial physician I sent advised, you might have overcome your illness sooner.”

“I beg your forgiveness. However, I feared my old body couldn’t withstand the medicine prepared by the imperial physicians, so I had no choice but to recuperate instead. But…”

Wei Zhong looked the Emperor over, his face suddenly clouded with concern.

“Perhaps it is only because it has been so long since I last saw you, but Your Majesty’s countenance seems rather poor. Has illness taken hold of your precious body, which ought to be so strong?”

“……!”

A chill passed through the Emperor’s eyes, already hard with displeasure.

“There’s no need to worry. It isn’t as bad as you fear.”

“Then I’m greatly relieved. Now that you’ve become a sage king who shows such mercy, you must rule over the land for ten thousand years—ten thousand times ten thousand years.”

I could feel it.

The invisible blades the Emperor and Cang Gong were endlessly exchanging.

And the immense energy now emanating from the Emperor.

*Rrrrmmm.*

The air around us began to churn. A few officials nearby went pale and trembled as if struck by a chill.

His status as Emperor overshadowed it, but he too had entered the realm of the superhuman. He was a Supreme Peak master.

But…

*Cang Gong is different. That man is something else.*

I’d realized it the moment he appeared.

That pale old man who looked like Gandalf was a greater master than anyone else here.

*Even Baek Yeon.*

A battle between Supreme Peak masters could decide life and death in the blink of an eye.

The fact that Cang Gong had come within five *jang* of us without me sensing him meant he’d all but seized the initiative.

*Now I see why Ma Sanbao was so confident.*

From what I could sense, Cang Gong and So Gyo were evenly matched.

If Jeok Cheongang and the other fighters who hadn’t yet arrived at the Grand Banquet Hall joined the restoration army, they could take down So Gyo with ease.

Of course, So Gyo hadn’t shown herself yet.

*She’s probably somewhere else, guarding Prince Shangshan.*

The prince was a crucial key.

Neither the restoration army nor the Emperor could let him fall into the enemy’s hands.

It seemed I wasn’t the only one thinking along those lines.

“Your Majesty. Perhaps the recent storms have made the weather unusually chilly today. Might Your Majesty show some mercy for the sake of those poor officials, who are trembling over there?”

Cang Gong indicated the shivering officials, his words respectful and relaxed, but carrying a barb. Then, as if a thought had just occurred to him, he spoke again.

“By the way, why are Prince Shangshan and the pregnant Consort not here? The two of them are indisputably members of the imperial family, and ought to be here to lend their presence to this occasion alongside Your Majesty—”

“Silence, Wei Zhong.”

Baek Yeon cut Cang Gong off in a hard voice and was about to step forward when—

“That’s enough.”

The Emperor raised a hand to stop him and stared at Wei Zhong with cold eyes.

“Cang Gong, you needn’t concern yourself. The two of them are already on their way here.”

“I’m deeply grateful for Your Majesty’s grace. At last, I’ll get to meet the heir who will one day rule this vast Great Nation.”

“Yes. You will.”

Neither of them said anything more.

Nor did either bother to ask the other which heir he truly had in mind, or whom the other considered the heir.

They would simply wait.

For the banquet to reach its height. For the fuse to burn all the way down.

And so would I.

“Excuse me. It looks like you two are about done talking. Could I say something, if you don’t mind?”

The Emperor answered.

“What is it?”

“It’s nothing special. You’re probably going to move over to that raised seat over there now. I was wondering if I could move, too. Preferably to the seat next to Cang Gong.”

“…You want to change seats?”

While the officials who’d been frozen in place all glared at me as if they wanted to tear me apart, Cang Gong spoke in the Emperor’s stead, who’d been momentarily lost for words.

“Is, um… there a particular reason?”

I gave him my most confident, dashing look.

“The seats up there seem to come with more side dishes.”

Of course, it didn’t look particularly dashing.
## Chapter artifact 902

# Chapter 902

This might have been a first in the history of the Great Nation.

A ruffian from the martial world who didn’t even hold an official post—or carry an identity token—sitting at the same table as the court’s high-ranking officials at a grand banquet presided over by the Emperor himself.

*The first, and probably the last.*

Even considering the short history of the Great Nation, which had only lasted three generations so far, it was a feat unlikely ever to be repeated.

Yet almost no one spoke up to object to this measure, which trampled on the imperial family’s dignity.

Not unless they were among the handful of ministers with unwavering convictions and courage.

“Your Majesty! Forgive my boldness, but this measure of seating that man so close to you—”

“It is the imperial decree.”

“……It is indeed a wise decision!”

As a rule, even conviction and courage crumbled like a sandcastle hit by a wave when faced with the Emperor.

Especially when that Emperor’s hobby—and specialty—was purging people.

Thanks to that, I was able to sit down without much fuss in front of an even more lavish spread.

*Smack. Smack-smack. Slurp.*

At the vivid sound of me inhaling one dish after another, the pupils of the people around me trembled.

When I showed off the godlike noodle-slurping technique I’d honed on ramen, groans broke out from all over.

“Good heavens.”

“Have you ever seen such a low-class bastard…?”

“What a sight. It’s enough to kill what little appetite I had. Look over there—even Cang Gong hasn’t touched a single thing.”

At someone’s last remark, I casually turned my head. Cang Gong was gazing steadily at me with his gray eyes.

*Hmm. Was that too much?*

“Pay no mind to what the others say. Keep eating. By the way, is it that good?”

At Cang Gong’s calm question, I answered.

“Definithely delishious.”

“I see. But you should probably finish what’s in your mouth first.”

“Oh.”

I swallowed the mouthful crammed into my cheeks, then spoke again.

“It’s definitely good. There’s a great variety of side dishes, too.”

Cang Gong nodded.

“I understood you the first time. My hearing isn’t that bad. Besides, the imperial chefs have long been renowned for their skill.”

“Then why aren’t you eating?”

“I don’t particularly have an appetite. It’s been that way for some time.”

“Hmm. That’s lucky, at least. I thought it was because of me.”

“Don’t worry about that. I’ve been this way since I was young. Still, it is a little disappointing that even the finest and rarest delicacies taste like grains of sand now.”

Cang Gong took his eyes off me and looked at the table in front of him, his face expressionless.

It was laden with enough food to make the table legs bow under the weight, yet his hands remained neatly on his knees the whole time.

They were so white they had no color in them—or rather, so pale they looked like a corpse’s hands.

I studied Cang Gong, sitting right beside me yet barely giving off any sense of presence. Then I quietly moved my lips.

“When are we going to start?”

At that moment—

*Vrrrm.*

A subtle, chilling qi sealed off the area so tightly that it would have gone unnoticed without careful attention.

A remarkable feat.

Cang Gong had raised a flawless barrier of internal energy to block out sound. He spoke.

“I’ll give the signal.”

“I think now would be the perfect time.”

“As long as that woman called So Gyo remains by Prince Shangshan’s side, we can’t act rashly. Even if we take the Emperor’s head, everything will be for nothing if we can’t secure His Highness.”

“That’s true.”

“Besides, your master is still waiting outside the banquet hall. The Fire King is essential if we’re to defeat So Gyo.”

“Maybe. But I think you’re every bit the master my teacher is.”

“This old man was able to overcome a grave Internal Injury and attend today thanks to the good fortune of gaining insight during my recovery. The more important the matter, the more carefully it must be handled, don’t you think?”

Yeah, that made sense.

I nodded naturally and resumed moving the chopsticks I’d set down for a moment.

Cang Gong, who was watching me as if I were some strange creature, suddenly spoke.

“You look like you haven’t eaten in days.”

“You’ve got that right. I barely ate anything for two days.”

“A master of your caliber should be able to endure a little hunger.”

“Why should I have to endure it? My principle is to eat a hearty meal before a fight.”

“Are you nervous?”

“I am. My stomach is.”

“You really do take after your master. You’ve got quite a nerve, just as I’d heard.”

“Did you hear anything else about me?”

“I heard that, at your age, your martial arts are without precedent—and that your quick wits and survival skills are good enough to see you through any crisis.”

“Sounds about right.”

“That was the abbreviated version. The East Depot has eyes and ears all across the land, and the reports they bring me always exceed my expectations. One of the most recent reports was particularly surprising.”

“May I ask what it was? What could have surprised even Cang Gong?”

“The Murim Alliance reinforcements.”

“Ah.”

“I truly didn’t expect that. I thought the Murim Alliance had already deployed most of its forces throughout the land to deal with sudden attacks by Dark Heaven, which could appear anywhere at any time.”

Instead of answering, I lifted my cup and wet my throat. A fragrant aroma filled my mouth, befitting the finest liquor in the land, followed by a smooth swallow.

Of course, the drunkenness that should have come with it vanished without a trace when it met my Scorching Yang Qi.

“I hear they use the strangest supernatural powers. Did the Alliance really have enough strength left to form a reserve force?”

“They wouldn’t have come if they didn’t.”

“They came because they had enough… Yes, I suppose so.”

Cang Gong was gazing steadily at me with his gray eyes when—

“Enough.”

The Emperor’s resonant voice rang out, and in the same instant, the beautiful music that had filled the grand banquet hall vanished as if it had been washed away.

Those who’d been whispering to one another, those who’d been drinking with solemn expressions, even the musicians and dancers who’d forced themselves to continue performing in that atmosphere—all fell silent.

Everyone stopped moving and turned toward the Emperor, following his voice and gaze.

“The heir who will inherit this continent, the Great Nation that shall endure for the next thousand years, is on his way. Receive him with the proper ceremony.”

“……!”

“……!”

It was an unmistakable declaration of the heir.

Everyone had expected it, and yet had thought it couldn’t possibly happen. Now that they were facing the moment, a great shock swept through the people in the hall.

But while their minds raced, their bodies had already begun to bow according to protocol toward the newly arrived eight-horse carriage.

*Boom. Boom-boom. Boom-boom-boom!*

The vigorous drumbeats of the drum master made the air shudder. In the quietly building tension, the carriage door opened, and someone stepped out.

*Swish.*

The hem of a splendid red palace gown brushed the ground. The woman alighted from the carriage, stepping lightly on the back of a palace attendant who had prostrated himself before her. Her bewitching beauty drew a low gasp from somewhere in the hall.

“Good heavens.”

“This can’t be…”

It was an unwise thing to say, but understandable all the same.

The woman’s beauty was so extraordinary that “beauty capable of toppling a kingdom” hardly seemed an exaggeration.

*No wonder the City Lord of Sichuan Province fell for her.*

I thought to myself as I looked at the woman—or rather, Aehyang.

Until only a few months ago, she had been the City Lord of Sichuan Province’s favored concubine. Now she walked under the unyielding protection of the Embroidered Uniform Guard, uneasily caressing her belly.

And just as everyone’s eyes followed her, I saw another person step out through the still-open carriage door.

A face that still belonged to a child.

Yet his expression and stride were bolder than those of any young man.

Prince Shangshan, Zhu Bao.

* * *

As I watched Prince Shangshan stride up the tall staircase, I wondered what I should say.

What kind of greeting should I offer the young prince, whom I was seeing again after several days?

I didn’t have to think for long.

“Have you been well?”

My Sound Transmission crossed the space between us, and Prince Shangshan’s steps came to an abrupt halt. Seeing him stop, I let out a quiet laugh to myself and moved my lips again.

“Are you still keeping the item I entrusted to you safe?”

After a brief pause, his steps resumed. Prince Shangshan didn’t look my way, but he answered by flicking the sleeve over the back of his hand.

For a moment, I caught sight of a dark, dull ring.

I nodded after spotting the Myriad-Poison Ring, and Cang Gong suddenly spoke up.

“Good. It seems His Highness is still keeping it safe.”

“Sure is. I was worried he might lose it, but I’m glad he hasn’t.”

I answered calmly without even turning my head. I felt Cang Gong’s gaze lingering on me, but it soon shifted to someone else.

*So Gyo.*

I saw her.

She followed quietly behind Prince Shangshan.

Instead of her flexible sword, she wore two weapons at her waist, each curved at an angle like a saber. So Gyo looked straight at me and smiled faintly.

“Did you see that?”

At Cang Gong’s question, I answered calmly.

“I did.”

“She was smiling at you.”

“Really? I thought she was smiling at you, Cang Gong.”

“You’re mistaken. That gaze just now… she was looking straight at you.”

“I’ve met her before, as Eunuch Ma probably told you.”

“Is that the only reason?”

“What other reason could there be?”

“A thousand years! A thousand years! A thousand thousand years!”

The civil and military officials of the court, along with two thousand Embroidered Uniform Guards, roared their cheers toward the heir of the Great Nation, shaking the whole place.

Whether they were merely going along with the occasion or were genuinely celebrating it, they all chanted with one voice. At the center of that immense cheer stood the Emperor, Aehyang, and finally, Prince Shangshan.

And beside me sat the only person who wasn’t crying out “Long live.”

“I find myself wondering what you think.”

Cang Gong continued without waiting for my answer.

“Why did the Emperor forgive you, despite your unforgivable disrespect? It was the perfect chance to remove Prince Shangshan while gaining both a pretext and a practical advantage.”

“I don’t know. I’m a pretty simple guy.”

“Simple, you say? Then was that stunt you pulled all of a sudden, without any plan, simply a result of your personality?”

“If that’s what it was, then it was. If it wasn’t, maybe it wasn’t.”

“Explain.”

“To hell with the grand plan. A lot of people’s lives were at stake, so there was one thing I had to make sure of.”

Cang Gong no longer looked toward the throne where the Emperor stood, nor did he bow toward it. He held himself straight and looked at me with gray eyes.

“So, have you finished checking?”

“Yes.”

“And your conclusion?”

“No matter how I look at it, there could only be one.”

I met Cang Gong’s gaze with eyes that were quiet, yet burning hot, and spoke.

“The Emperor doesn’t want Prince Shangshan to be put in danger.”

“……!”
## Chapter artifact 903

# Chapter 903

There are some mysteries that no amount of thought can solve. When that happens, there’s only one way to get to the answer.

Turn everything upside down.

Forget all the circumstances and clues you’ve gathered so far, and start over from the beginning. That’s the last resort.

Like retracing your steps to find some precious thing you don’t remember dropping, I went back to the starting point and reviewed every little detail, big and small.

And at last, I arrived at a hypothesis.

“The Emperor doesn’t want Prince Shangshan to be put in danger.”

“……!”

A faint ripple passed through Cang Gong’s gray eyes.

It appeared and vanished in less time than it took to blink, but I’d been watching his every tiny movement too closely to miss it.

*So it was true.*

The realization struck me, and a jolt of electricity ran down my spine.

Amid the people’s enormous, still-undiminished roar, Cang Gong, who’d been gazing steadily at me, suddenly spoke.

“When did you figure it out?”

It was a question without context, one anyone else would have struggled to understand.

But I immediately realized what he meant.

He was asking when I’d started suspecting them.

“So Gyo.”

Yes. It had started right then.

The day she let me go, even though everything was going so well that there was no way she could fail.

No matter what circumstances or clues I considered, I couldn’t make sense of So Gyo’s strange behavior.

It was like a fishbone stuck in my throat.

“So Gyo…”

At my brief answer, Cang Gong gave a small nod.

“Yes, I suppose it would be. She was the only flaw in this grand scheme. If I’d known this would happen, I should have eliminated that mysterious woman long ago. Even if it meant an all-out war with the Emperor.”

What?

I managed to swallow the words that almost burst from my mouth, but I couldn’t hide my momentary shock.

*Even Cang Gong doesn’t know who So Gyo is?*

Cang Gong caught the confusion that had appeared on my face and gave a low laugh.

“From the looks of it, you don’t know who she is either. Not even whether she’s an ally or an enemy.”

“……!”

“Strange. Very strange. Until just now, I suspected she might be a Murim Alliance spy, but… now I have no idea. If she were a master secretly trained by the imperial family, she still couldn’t have escaped my notice.”

This time, setting aside the situation I was in, I couldn’t help sharing Cang Gong’s bewilderment.

*Then who is So Gyo? Who is that woman?*

If she’d belonged to the Murim Alliance, she would have told me the whole truth before things got to this point. And if she were a master of Dark Heaven or the imperial family, Cang Gong would have known.

But So Gyo was different.

As far as I could tell, she was a third party.

Unaffiliated with anyone.

*Who the hell…*

Who was So Gyo? What expression was she wearing as she watched us right now? What was she thinking?

And…

*Is she an enemy or an ally?*

I fought the urge to turn and look toward So Gyo, who should have been standing atop the tall stairs in the distance.

Cang Gong and I were only a few steps apart. Taking my eyes off him, even for a moment, would be no different from suicide.

Of course, I was only acting this bold because I was sure Cang Gong couldn’t kill me right away.

“You have good eyes. Full of fighting spirit. But why would that person take an interest in you?”

*That person.*

There was no mistaking the fear and reverence in Cang Gong’s voice as he spoke of someone who wasn’t here.

The Blood Lord, the Western Heaven Demon Lord, and the Southern Heaven Demon Empress had all felt the same way.

Those people of Dark Heaven existed because they had a heaven of their own—the Lord of Heaven.

“Tell me. As the person concerned, you might know why that person is searching for you so relentlessly. Is it because you’ve achieved something unprecedented at such a young age? Or is it because of some other worth only that person can recognize?”

His gray eyes, like those of a dead man, glimmered dimly.

A secret, terrifying chill came with them, unlike anything I’d ever felt before.

*Fwoosh.*

I’d stake my life on it: even the Yin-Cold Qi of the Great Snow Fiend, who’d cornered me in Nanman, hadn’t been this intense.

*No. This isn’t Yin-Cold Qi.*

It was something more primal and pure.

Another kind of power, one I’d never heard of or experienced.

But I overcame my instinctive fear. Enduring the chill that seeped into my bones, I answered.

“Why the hell are you asking me? You’re the one without any balls.”

“……!”

Cang Gong stared at me with eyes wide, then smiled faintly.

“Yes, of course you wouldn’t know. How could someone like you possibly fathom that person’s intentions—”

“Yeah. I can look all I want, but I still can’t find your balls.”

“Be careful with your choice of words. No matter how much grace that person has shown me…”

“Yeah. I could search the whole ocean and still not find your testicles.”

“…….”

“I chose my words carefully. What’s the problem?”

His faint smile had vanished long ago.

Amid the people’s continued cheering, Cang Gong’s tightly shut, pale lips parted.

“What do you think? Surely that person would understand if I merely pulled out your tongue.”

“Sure. The Lord of Heaven might. You’re the one among his followers he worries about most. His sore ball—no, his sore finger. Especially since you haven’t got any balls.”

I nodded in agreement and kept talking.

Pointing over Cang Gong’s shoulder.

“But that guy won’t understand.”

At that moment—

In the slowed-down flow of time, everything happened at once.

Cang Gong reflexively turned to look behind him. I thrust a fist wreathed in flame at him. And a solid palm shot forward like a flash of light, as if reversing time all by itself, intercepting my fist before it could reach anyone.

*BOOM!*

A roar like the sky splitting apart brought time back to normal. At the same instant, a mighty shock wave shook the grand banquet hall.

*Crack! Rrrrmm!*

The ground shook as if there’d been an earthquake.

Screams and shouts erupted in every direction.

In the space that had plunged into chaos in an instant, a pair of pure white eyes stared at me.

“Was that all you had?”

*Crack.*

His voice was calm, but the immense force squeezing my fist was anything but.

An unknown, ice-cold energy within his hand suppressed the flames in mine and snuffed them out.

“I’m disappointed you’d resort to such a shallow trick.”

*Crunch. Crunch.*

Agonizing pain shot through my captured fist.

If my muscles and bones hadn’t long since surpassed the limits of an ordinary human, they would have been crushed to dust already.

But I’d suffered this much pain more times than I cared to count, and I’d never expected that surprise attack to take him down.

I’d only needed a signal flare to let everyone know what was happening.

“If you thought it was just a shallow trick, I’m a little hurt.”

“What?”

“I don’t know if you’ve heard of magic, but I’m going to show you some now. Make sure you watch.”

“What are you—”

The moment Cang Gong frowned—

*BOOOOM!*

With a blinding blaze that swallowed even the darkness, the rock walls surrounding the grand banquet hall like a towering fortress exploded.

And from the place Cang Gong had glanced at just moments earlier, a figure strode out.

“I’ll give you my first and last warning.”

The flames dancing in that damn monk’s eyes looked anything but Buddhist. He swept his gaze across the hall and went on.

“Only step forward if you want your flesh and bones to melt.”

“……!”

Cang Gong’s eyes sank when he recognized the uninvited guest. I smiled and spoke.

“Accio, Fire King.”

At the same time, I thrust out my one free hand.

Toward the bastard’s chest, which had stiffened for an instant.

With the Flame Divine Palm, now at nine-tenths mastery.

*BOOOOM!*

* * *

“Huh?”

The young man abruptly stopped walking and turned around.

A burly man walking ahead of him asked when he saw the young man staring back down the road with a furrowed brow.

“Mujin. What’s wrong?”

“No, it’s just…”

Hyuk Mujin trailed off and clicked his tongue.

“I thought I heard something.”

At that, the burly man, Taishan, raised an eyebrow.

“A sound? Enemy?”

“I don’t know. Maybe I imagined it.”

“Then no. That sound Mujin heard. Taishan didn’t hear it.”

“But I’m telling you, I definitely heard something.”

“Mujin. Weak martial arts. Taishan can make you into well-prepared five-spice pork if he wants.”

“……Hey, what the hell? Are you looking down on me?”

“Mm. Honestly, a little.”

“…….”

“Mujin. We can’t stop. We have to go now. Everyone is waiting.”

Hyuk Mujin swallowed the flare of anger and let out a long sigh.

“Yeah, I’m going. I’m going.”

But despite his answer, his steps didn’t come as easily as before.

The road he’d already traveled and the walls of the Imperial Capital, growing a little more distant with every passing moment, kept appearing before his eyes.

*Damn it. Am I hearing things now, too?*

He was a little annoyed, but Taishan was probably right that there hadn’t been a sound.

If Taishan, a Peak master a step above him, said there was no sound, then there was no sound.

Even if Mujin had heard something, it must have been a faint rustle from an insect or an animal moving.

*So why do I feel like this?*

Hyuk Mujin frowned even harder and thumped his chest.

His heart, which had never behaved this way before, kept pounding. It was as if an invisible hand were squeezing it hard.

*I have a bad feeling.*

Along with the inexplicable unease, the face of someone he’d parted with a few shichen ago suddenly flashed through his mind.

*Just one mission.*

The last words he’d heard before leaving still echoed in his ears.

*Oh, one more thing.*

*Yes?*

*Be careful. You, and everyone else.*

Blazing Flame Divine Dragon Jin Taekyung.

Hyuk Mujin had answered his warning with a grin, then left the Imperial Capital with everyone from the Fire Dragon Pavilion, heading for the border between Jiangsu and Zhejiang Provinces.

For the very place written on the note Jin Taekyung had given him.

*I’m carrying out the mission just fine… so why do I feel like this?*

The mission was going smoothly, but his chest felt unbearably tight.

The way the Captain—Jin Taekyung—had acted so unlike himself had been like a fishbone caught in Mujin’s throat.

He’d laughed and joked about nothing, hit him for being cheeky, and cursed him without holding back. But he hadn’t seen any of that from Taekyung today.

“Mujin!”

“……Ah.”

Snapping out of his thoughts, Hyuk Mujin realized he’d stopped walking again.

Then he saw his companions waiting for him not far away, and his heart sank.

Their eyes were grave.

Their expressions troubled.

Everyone except Taishan was looking at him with the same face.

“Everyone…”

Hyuk Mujin barely swallowed a groan. At last, he thought he understood what the unaccountable unease that had been squeezing his chest all this time meant.

“Did… did you all know?”

At his question, forced out through stiff lips, Namho answered in a heavy voice.

“Yes. More or less.”

“On the Captain’s orders?”

“No. Senior Jeok warned us in advance. He knew what choice his Disciple would make.”

“Then why was I the only one—”

“If he’d told you to leave because you’d be a burden, would you have obeyed without a fuss?”

“……!”

“I don’t like this situation either. No—none of us do.”

Hyuk Mujin was momentarily at a loss for words.

He understood perfectly well how they felt, knowing they could only be burdens rather than help, and why Jin Taekyung had lied to send him away.

And it was the truth.

But, but…

*Still, it shouldn’t be like this.*

*Grit.*

Hyuk Mujin bit down on his lip until it bled and turned his head. Then, for an instant, he forgot the entire situation and muttered in a dazed voice.

“Huh…?”

At the end of his gaze, countless figures moved in the darkness, shaking the distant forest.

Too many to count, yet not a trace of their presence could be felt.

*What is that?*

The same question rose in everyone’s mind. So did an inexplicable fear.

This time, instinct—not reason—moved Hyuk Mujin.

No, it moved all of them.

*Whoosh!*
## Chapter artifact 904

# Chapter 904

The situation in the Grand Banquet Hall had already spiraled beyond anyone’s control.

The festive music had long since fallen silent, and the endless cries of “Ten thousand years!” celebrating the heir’s birth had turned into screams and shouts.

At last, the fuse had been lit.

The banquet was over.

But at the same time, another banquet remained—one that had not yet ended.

A Hongmen Banquet,[^1] where they would turn weapons on one another instead of smiling, and spill blood instead of wine.

Then a tremendous roar announced the start of that horrific feast, shaking everything around it.

*BOOOOM!*

The ground shuddered, and a dreadful wave of heat erupted. At that very moment, a figure shot out from beyond the blazing flames and clouds of dust at the speed of a flash.

*Whooosh!*

*Crunch!*

The ground crumbled like tofu beneath the tip of the foot that barely touched down.

Jin Taekyung, the young man who’d just managed to steady himself after being hurled through the air with a sharp blast, spat the blood pooling in his mouth and muttered,

“So, you’re a cut above me…”

Even after making full use of speed, strength, and the art of a perfect surprise attack, the gap between them had been unmistakable.

Along with the tingling pain in his hand, Jin Taekyung remembered the moment he’d thrust out his palm.

The instant his full-power Flame Divine Palm was about to strike the man’s chest, an icy energy had lightly suppressed his Scorching Yang Qi and shaken his entire body.

*What the hell was that?*

It was a kind of energy Jin Taekyung had never felt before, despite having enough experience to rival most veteran masters.

Something more primal. Something that couldn’t be defined as mere Yin-Cold Qi.

But there was far too little of everything he needed to solve the mystery.

Information. Experience.

And time.

*Clop. Clop.*

Even amid the chaos consuming the Grand Banquet Hall, footsteps rang out clearly.

Cang Gong strolled across the ground, which had melted horribly in the wake of that powerful Scorching Yang Qi. Then he suddenly stopped.

Right where he’d been standing moments earlier.

“Five steps. He made me retreat five steps.”

His low mutter carried a note of admiration.

It was admiration for a martial artist who’d reached astonishing heights at an absurdly young age.

*To make this old man retreat five steps, in that battered condition.*

Now that he’d experienced it firsthand, he thought he finally understood why *that person* had taken such an interest in Jin Taekyung.

Why *that person* had ordered them to keep that young brat alive, even after losing two loyal servants—the Western Heaven Demon Lord and the Southern Heaven Demon Empress—in the process.

*As an enemy, he’d be the greatest obstacle. But as an ally, he’d soon become a monster who could surpass even the Three Saints.*

He never once considered that Jin Taekyung might refuse to join them, even if they captured him.

If he ever met the Lord of Heaven—if he felt even once the power of that irresistible absolute—he’d have no choice but to kneel before him.

Just as Cang Gong himself had once done.

“I’ll have to take him to the Lord of Heaven. No matter what.”

It was at that very moment that Cang Gong muttered those words.

“Take who to whom?”

*Fwoosh.*

With that dry voice, the air within a radius of dozens of yards grew scorching hot.

Cang Gong’s pale lips parted when he saw the bald, middle-aged man approaching through the shimmering haze rising from the ground.

“Fire King Jeok Cheongang.”

“How dare you toss my honored name around, you ball-less bastard?”

“You two really are alike in speech and behavior. You’d think one learned it from the other—though I couldn’t say whether the disciple learned it from the master or the master from the disciple.”

Jeok Cheongang gave him an indifferent reply.

“Usually the disciple learns from the master. Though a rootless bastard like you wouldn’t know that.”

“Roots, huh? I had those once. A master and fellow disciples who were like family.”

“I see. So did you learn to cut off your own balls from your master?”

“No.”

A murderous smile spread across Cang Gong’s lips.

“He taught me never to forget my roots, no matter the circumstances. I have never forgotten his words for even a moment.”

“I don’t know what long-winded sob story you’ve got, but… teaching or whatever, you won’t need to remember it anymore.”

Jeok Cheongang raised his fist and grinned.

“Everyone who’s taken a hit from this old man ended up like that.”

He glanced around and added,

“Well, even without me, looks like there are plenty of people who’d love to tear you apart.”

Jeok Cheongang wasn’t exaggerating.

Nearly two thousand members of the Embroidered Uniform Guard surrounded them in a circle. Every one of them was among the Great Nation’s finest troops, martial artists ranging from Supreme First Rate to Peak.

And that wasn’t all.

The Imperial Guards, considered a cut below the Embroidered Uniform Guard who protected the Emperor and the imperial family, were no less deserving of being called an elite force. They’d arrived late, seized the outer walls of the Grand Banquet Hall, and drawn their bows.

Five thousand men in all.

There wasn’t the slightest doubt they could be called an army. In terms of quality, their forces could rival even an army of a hundred thousand.

And yet Cang Gong calmly looked at the countless spears, swords, and arrowheads surrounding him.

Or, to be precise, he looked past their shoulders, toward the one man watching from atop the high platform.

“The hunting dogs have slipped their leashes and are running wild without even knowing where they’ll die, while their cunning master sits back and watches.”

Just as he always had.

After adding that under his breath, Cang Gong laughed aloud.

Then, abruptly—

His laughter cut off, and a tremendous shout burst from between his pale lips.

“Attack!”

*BOOOOM!*

The unprecedented internal energy carried by his voice shook the Grand Banquet Hall. At that instant—

*Thrust! Slash!*

A dazzling blade burst out of one member of the Embroidered Uniform Guard’s chest. He stared blankly at it, the sword piercing his golden armor, too stunned even to feel the pain. Then he stammered,

“W-Why…?”

His wide eyes held both shock and disbelief.

Even as death rushed toward him, he desperately wanted to know.

Why? Why was he dying so pointlessly?

Why had the comrade he’d called hyung for more than ten years stabbed him in the back?

“Ghk. D-Dong hyung?”

Why?

How could this be?

They weren’t related by blood, but they’d promised to treat each other as sworn brothers.

They’d raised their cups together dozens, hundreds of times, encouraging each other, strengthening their bond, and swearing their loyalty to this country and His Majesty the Emperor.

But when he gasped out that one desperate call, trying to hold back the blood rising in his throat, the answer that came back was a dry voice he’d never heard in ten years.

“Heaven above, earth below. All demons bow in reverence.”

“……!”

That was the last thing he heard.

*Crunch.*

The sword twisted and pulled free. The soulless body toppled to the ground.

Everywhere.

*Thrust!*

All around.

*Slash!*

Countless times.

*Shhhk!*

Necks neatly severed rolled across the ground. Chopped limbs and streams of blood shot through the air.

In the blink of an eye, hundreds of lives vanished from the two thousand members of the Embroidered Uniform Guard.

At the hands of their own comrades—superiors, subordinates, even men they’d cherished like brothers.

“……!”

“……!”

Muffled shouts burst out from every direction. The traitors and the betrayed, those who fought to protect and those who fought to take, clashed with one another.

*Clang-clang-clang!*

*Slash! Thrust!*

“Aaagh!”

Amid echoes of screams, flashes of swordlight flickered ceaselessly through the darkness.

Someone’s hand, still holding a torch, twitched in a pool of blood.

And over the horrific melee that had erupted in an instant beneath the cover of night, another darkness descended.

*Fwoooooosh.*

Some who heard it thought it was raining. Another man, panting as he waited for death, remembered the wide plains of his hometown.

When a strong wind blew in from far away and swept across the fields, it made a sound just like this.

The ripe grain and grasses would bend at the waist. The great tree where the village festival had been held would shake its lush branches and leaves.

But the nameless man realized he’d never return to the hometown he missed.

*Ah.*

The darkness covering the sky wasn’t darkness at all. It was an uncountable rain of arrows pouring down.

They spread across the sky as they rushed toward the people below—or toward the Emperor they’d sworn their loyalty to.

*Cough.*

Spitting blood mixed with bits of his innards, he muttered to himself.

This wasn’t how it was supposed to be.

He hadn’t left his hometown and family just to die this pointlessly.

*Damn it.*

He stared blankly at the darkness rushing toward him, waiting for death to end this terrible pain and despair.

And then he saw it.

*Fwoosh—BOOOOM!*

A tremendous blaze devoured the darkness.

In that overwhelming heat, which burned the countless arrows to nothing, a young man plunged toward the ground like a hawk snatching up its prey.

*BOOM!*

Why did a roar that should have sounded like thunder seem faint, as if it were hundreds of yards away?

As his vision dimmed, he wondered what the young man’s name was.

Why couldn’t the words “Please, save me”—that short plea to send him home—come out as a voice?

He could only watch through the darkness gathering before his eyes: the flames burning the endless rain of arrows, and the traitors falling like bundles of straw whenever the young man moved.

He watched the two beings begin a battle that shook heaven and earth, beings he couldn’t believe were made of the same flesh and blood as him.

*Bang! Bang! BOOOOM!*

Scorching heat. Shuddering cold.

Flames and white flashes dyed every corner of the night, setting it ablaze and freezing it over.

Even now, countless corpses piled up as blood splattered in every direction, used as firewood.

And the life of one unfortunate man, made to suffer a little longer than the others, as its sacrifice.

But at the end of that horrific wait, the nameless member of the Embroidered Uniform Guard managed to remember the young man’s name—the one he’d almost forgotten.

*Jin Taekyung. Right. It was Jin Taekyung.*

It was strange.

Though he lay in a pool of blood, dying amid a sea of corpses and blood, he didn’t feel even the slightest bit cold.

*It’s warm.*

Watching the flames surge between the flashing spears and swords, he couldn’t fight off the sleep pouring over him. He closed his eyes.

Thinking of the hometown he’d never return to.

* * *

People who love to talk say that the only things capable of killing a Supreme Peak master are the passage of time and their own carelessness.

And right now, I wanted to tell those people:

*Then why don’t you try fighting them?*

A Supreme Peak master is still a person made of flesh and blood.

To people who don’t know any better, he might look like a superhuman who can take down hundreds or thousands of enemies. But there are limits.

Especially when at least half of those hundreds or thousands are Peak masters.

*Swish! Thwack!*

The tip of a spear someone thrust out skimmed past my cheek by a hair. Getting my skin sliced open by the internal energy packed into its blade was just the standard package. My fist returning the favor was a bonus.

*Wham!*

The member of the Embroidered Uniform Guard—no, the traitor planted by Dark Heaven—went flying like a puppet with its strings cut after my Flame Divine Palm struck him in the chest.

A clear-cut instant death.

But someone else filled the gap, and their movements grew more cautious and agile.

*Damn it.*

If they’d been ordinary martial artists, they’d have been much easier to deal with. But they were martial artists and soldiers at the same time. A group with the power of martial arts and the discipline of an army.

*Slash! Thrust!*

I snatched a spear from someone’s hands and swung it wildly, glaring past the shoulders of the enemies surrounding me.

*Why the hell?!*

I wanted to shout it right then and there.

Why weren’t they helping?

Why were they just standing by, even when things had gotten this bad?

At the end of the direction I was looking, the Emperor stood there. Baek Yeon and So Gyo were beside him, guarding him like stone statues.

And now someone else had joined them.

An unwelcome guest who’d suddenly stepped into my line of sight.

*Whoosh!*

At the same time as a sharp blast of air, a dozen or so members of the Embroidered Uniform Guard fighting nearby stopped moving.

Their eyes were wide with disbelief.

Then, as if to reveal the cold truth, faint lines of blood appeared on their necks, growing darker by the second.

*Gurgle—SHHHK!*

The blood, gathering in thick beads, sprayed out like fountains. The man who’d swept past the falling bodies, which crumpled like rotten trees, looked at me and sighed.

“Why did you do that? If you’d simply trusted me and followed along, everything could have gone smoothly.”

Instead of answering Ma Sanbao’s bullshit—the kind even the mutt next door could understand—I brought my spearhead down.

*Whoosh!*

[^1]: A Hongmen Banquet is a treacherous feast, named after a famous historical ambush during a banquet.

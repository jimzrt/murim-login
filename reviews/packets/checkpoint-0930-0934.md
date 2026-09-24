# Checkpoint Review — 930–934

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

# Chapters 930–934

## Plot

After three days unconscious, Jin Taekyung wakes in the Fire Dragon Pavilion. A strange dream leaves him wondering about the System and the endlessly spinning Myriad-Poison Ring. He sends away a stream of officials and learns from Hong Jin—now Eunuch Hong and head of the East Depot—that Ma Sanbao evaded the search. Taekyung then receives a seemingly useless but remarkably durable broken pocket watch as his System Update reward. When Mujin asks for it, Taekyung decides to keep it for half a month before reconsidering.

Summoned to Qianqing Palace, Taekyung learns that the Emperor has been suffering from the Blood Soul Gu for more than ten years. The Emperor was poisoned by a trusted loyalist after the coup, and the Gu has reached his marrow. The Divine Physician examined him three days earlier but judged the condition too advanced to treat at present. Though the Emperor had accepted his approaching death, he admits he wants to live, chiefly to protect Zhu Bao and prepare him for the war he expects. Taekyung refuses to offer false reassurance and promises to save him.

## Continuity

- Hong Jin is Eunuch Hong and is responsible for the East Depot; the Cang Gong post remains vacant.
- Ma Sanbao escaped and evaded the Imperial Army’s three-day search.
- The Eastern Heaven Demon Lord’s final instruction was to find an unspecified object at a particular place; Taekyung does not yet know what or where.
- The System Update reward is a durable pocket watch that appears broken and bears the faint inscription, “A broken clock is right twice a day.” Its significance is unknown. Taekyung intends to keep it for half a month before deciding whether to give it to Mujin.
- The Emperor was poisoned with the Blood Soul Gu after the coup. It has reached his marrow, and he has endured its effects for more than ten years. The Divine Physician recently judged his condition too advanced to treat at present.
- The Emperor wants to live, chiefly to protect Zhu Bao and serve the country and its people. He expects a devastating war and fears Zhu Bao is too young to bear the burden of ruling through it.
- Taekyung promises to save the Emperor.

## Translation Decisions

- Keep “pocket watch” for 회중시계 and “A broken clock is right twice a day” for the inscription.
- Retain established System terminology and capitalization: System, Update, Reward, Inventory, Item, and Item Window.
- Keep 血魂蠱 as “Blood Soul Gu” and 罌粟 as “poppy”; do not imply that poppy caused the Emperor’s poisoning.
- Render 주체 as “Zhu Di,” the name the Emperor gives.
- Keep Taekyung’s speech to the Emperor blunt and teasing, while the Emperor’s speech shifts from formal royal diction to personal candor.

## Durable state

{
  "active_continuity": [
    "The System update reward is a very durable pocket watch that appears broken and bears the faint inscription, “A broken clock is right twice a day”; its significance is unknown.",
    "Taekyung intends to keep the pocket watch for half a month before deciding whether to give it to Mujin.",
    "Hong Jin is Eunuch Hong, responsible for the East Depot; the Cang Gong post remains vacant.",
    "Ma Sanbao escaped and evaded the Imperial Army’s three-day search.",
    "The Eastern Heaven Demon Lord’s final instruction was to find an unspecified object at a particular place.",
    "The Emperor was poisoned with the Blood Soul Gu after the coup; it has reached his marrow, and he has endured its effects for more than ten years.",
    "The Divine Physician examined the Emperor three days before chapter 934 and said the condition was too advanced for him to treat at present.",
    "The Emperor wants to live, chiefly to protect Zhu Bao and serve the country and its people.",
    "The Emperor expects a devastating war and fears Zhu Bao is too young to bear the burden of ruling through it.",
    "Taekyung promises to save the Emperor."
  ],
  "continuity_sources": [
    934
  ],
  "open_questions": [
    "What is the Martial God’s identity, and how did he know a chosen one would appear?",
    "How far has Dark Heaven infiltrated the Great Nation, and which officials or commanders are involved?",
    "Where is Ma Sanbao, and what is his current status?",
    "What object and place did the Eastern Heaven Demon Lord refer to, and what significance does the object have?",
    "What is the significance, if any, of the broken pocket watch given as the System update reward?"
  ],
  "safe_through": 934,
  "temporary_decisions": [
    "Taekyung will keep the pocket watch for half a month before deciding whether to give it to Mujin."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 930

# Chapter 930

Strange.

The unfamiliar ceiling that should have been waiting for me, just like always, somehow felt familiar.

*What is this?*

As my vision slowly sharpened, I turned my eyes and looked around.

The space was far too large to call a mere bedroom.

Thick pillars stood between the curtains surrounding the room, and light spilled from braziers placed here and there and night-shining pearls embedded in the ceiling like stars, softly bathing the entire room.

*Wait. Night-shining pearls?*

The next moment, I finally realized what had been causing this sense of déjà vu.

And why the place felt so familiar.

*This is…*

That’s right.

This was a vast pavilion built to serve as both living quarters and a place to handle state affairs—and a fortress filled with an ironclad guard.

It was Qianqing Palace.

*No wonder it felt familiar.*

Actually, if not for the night-shining pearls, it might have taken me longer to figure out what was going on.

Only an emperor could plaster the place with night-shining pearls big enough to fetch hundreds of silver nyang each on Bok Choy Market, as if they were glitter stickers.

*But…why am I here?*

The question rose in my mind, which felt as if it had been emptied out.

*Whoosh.*

At that moment, a faint breeze blew in from somewhere, stirring the curtains around the bedroom.

At the same time, a man in black appeared out of nowhere like a ghost and bowed his head slightly.

“Have you awakened?”

His voice was muffled, almost a mumble.

I stared blankly at the unexpected intruder, then calmly assessed the situation.

The Emperor’s quarters. The Emperor’s blanket. The Emperor’s bed. The Emperor’s pillow.

The clothes I was wearing were all golden, and when I lifted the edge of my pants to sneak a peek, even my underwear was gleaming golden silk.

The full King-God-Emperor package.

And on top of that, No Shadow—the Emperor’s hidden guard, an assassin and Supreme Peak master—was speaking to me with such courtesy.

*Then could this be…*

I drew a conclusion through clear-headed reasoning, then shuddered.

“Possession…!”

It had to be. There was no other explanation.

I’d gotten a good night’s sleep, woken up, and my life had changed genres from fusion Murim to a possession story. Just as I was reeling from the shock, No Shadow spoke in his usual muffled voice.

“Are you all right?”

*Would you be all right?* rose to the tip of my tongue, but figuring out exactly what was going on came first.

“What time is it? No, how many days have passed since the grand banquet?”

“……?”

Apparently, it was a strange question for an emperor who’d just woken up. No Shadow stared at me blankly before answering.

“Three days.”

“Three days?”

“Yes.”

“……Then how long was I asleep?”

“Three days as well.”

I squeezed my eyes shut.

Three days. In just three days, everything had gone to shit.

Forget being an emperor—I’d gone from a handsome young man in his early twenties with a bright future to a middle-aged man with the face of an old-timer, and everything I’d achieved had gone up in smoke.

*System window…open.*

I silently tried the command, just in case.

But it scattered into the void.

There was no clear chime, no translucent holographic window.

*What the hell is going on? How did things get like this?*

I couldn’t breathe.

The levels I’d busted my ass to gain, my stats—and now I couldn’t even access the System window. I might never return to the real world.

*Wait. Then what happened to the original me?*

The thought suddenly struck me, and my eyes flew open. I shouted at No Shadow in a panicked voice.

“Then what happened to me…? No, what happened to Jin Taekyung!”

Above his pitch-black mask, No Shadow blinked.

“You mean Jin Taekyung of the Jin Family of Taiyuan?”

“Yes, the Blazing Flame Divine Dragon, Jin Taekyung! The guy who’s handsome, tall, and perfectly muscled, and I have no idea why women aren’t all over him!”

The answer No Shadow gave me next was enough to make my mind go blank.

“He has yet to awaken.”

“What?”

“For reasons unknown, he has not regained consciousness. I regret to report that, according to the examination of the one called the Divine Physician, he is as good as dead.”

“……!”

“As a result, His Highness the Crown Prince has not eaten or drunk anything for three days. He said there was something he must return to a friend with whom he shared a bond…”

No Shadow trailed off, then carefully held something out to me. I accepted it in a daze.

The feel of rough, cold metal.

It gleamed like obsidian. It was the divine artifact of the Sichuan Tang Clan—the one I’d given Zhu Bao in case the worst happened.

*The Myriad-Poison Ring.*

The boy who’d promised to survive and return it to me before long appeared before my eyes.

But…

*Damn it.*

I didn’t know how things had turned out this way, but that shitty fate had twisted my life into knots once again.

Jin Taekyung of the Jin Family of Taiyuan was gone.

And perhaps the life of Jin Taekyung, the Hunter from Korea, had ended here too.

*Crack.*

At some point, my fist had clenched so hard my knuckles had gone white. But when I saw the wrinkles covering the back of my hand, the strength left me.

*Slide.*

My fingers loosened helplessly.

At the same time, the Myriad-Poison Ring rolled over my rough skin and fell, striking the bluestone floor of the bedroom.

*Clang. Clang.*

A cold metallic sound rang through the vast space, all alone.

With hope drained from my eyes, I watched the Myriad-Poison Ring spin rapidly.

Each time the black gem caught the light of the night-shining pearls and flashed, faces I would never see again crossed my mind.

My family, more precious to me than my own life, and all the countless comrades who stood with me, starting with Team Leader Choi.

They all came to mind—every one of them, the people I trusted and who trusted me.

And now, at last, I understood there was another being born to the same fate as me.

*The Martial God.*

Another System user, known as a Player.

Someone who had been chosen by this cruel fate long before I was.

Where was he now?

Had he gone through the same thing I had?

Or had the System chosen me as a new Player because he really was dead?

I didn’t know.

Not right now, and perhaps never.

I was no longer the chosen one. I was no longer a Player.

And so the System, which knew the whole truth, wouldn’t answer these questions.

No—it was me who wouldn’t hear the answers.

That was the power of the System.

A power meant for one person alone.

*So…another Player will appear.*

The empty thought never made it past the tip of my tongue.

With my eyes sunk deep, I kept watching the Myriad-Poison Ring spinning.

It was still turning and turning on the blue bluestone floor, without end.

“……?”

Wait a second.

Something about this is weird.

“H-how long is that thing going to keep spinning?”

At my cautious question, No Shadow answered.

“That’s why I hate people who catch on too fast.”

What?

* * *

Quietly. Very quietly, I opened my eyes to slits, like a flounder.

An unfamiliar ceiling came into view. Unlike the one from a moment ago, this one was moderately luxurious and moderately Murim-like.

*Good. First check passed.*

I raised a hand so slightly it made no sound.

Seeing the glittering golden sleeve weighed on my heart.

*Second check, pending.*

Ignoring the cold sweat beading on my forehead, I carefully lifted my pants.

I had no idea which son of a bitch had put this on me and called it underwear, but sure enough, it was dazzlingly golden.

*Third check. This is getting shitty.*

Afraid to confirm reality, I closed my barely open eyes again.

A bad sign.

But it wasn’t over yet.

In the awful silence, I quietly reached inside my pants and felt over my underwear.

The familiar, tearfully welcome, and utterly unique weight of it made my whole body shudder.

“Ah, ah…”

An indescribably thrilling jolt spread through my entire body.

I was alive.

I was still alive.

This wasn’t that shitty dream from a moment ago. This was vivid reality, the present in which I was alive and breathing.

I was Jin Taekyung the Hunter and Jin Taekyung the Blazing Flame Divine Dragon.

*Damn it. What a thing to be grateful for.*

How moving it was to be alive as myself.

I wiped away a few tears with my sleeve.

And just as I opened my eyes to face the world with more gratitude than ever—

“Ah.”

My gaze met a group of familiar faces who’d been watching me without making so much as a sound.

“……”

“……”

“……”

“……”

In the suffocating silence that felt like it would last forever, the Divine Physician spoke first, his voice grave.

“That is perfectly understandable.”

Jeok Cheongang, standing beside the Divine Physician, avoided my gaze as he chimed in.

“Yes, it’s the Scorching Yang Qi. He’s done nothing wrong.”

The Bow Saint nodded and murmured,

“Truly the chosen one…”

I took a quiet, deep breath.

It was as if the world had stopped.

No—more accurately, I wished it would stop.

But even after I shut my eyes tight, made a fervent wish, and opened them again, the dreadful reality was still waiting for me right there.

The Divine Physician. Jeok Cheongang. The Bow Saint.

Yes, I could understand them.

They were all old enough to have been through thick and thin, to have witnessed every sight the world could offer.

But they weren’t the only ones gathered in the room.

The Fire Dragon Pavilion.

Fuck. The Fire Dragon Pavilion.

I was looking at them. They were looking at me.

More precisely, they were staring at me with their eyes wide, as though they couldn’t believe what they were seeing—at the sight of my hand inside the front of my pants.

*Ah.*

I barely swallowed the sigh that was about to burst out.

Then, as calmly as I could, I spoke.

“I know. It looks like there’s plenty of room for misunderstanding.”

“I don’t think it’s really a misunderstanding, mm.”

Song Ilseom muttered under his breath, then shut his mouth when he saw my eyes.

Beside him, Sama Pyo raised his thumb quietly, looking rather impressed.

……You bastard.

Feeling a little pleased and utterly humiliated at the same time, I parted my lips again.

“But I had…something to take care of.”

“Taishan knows! Taishan knows about taking care of that! Taishan knows what it is!”

“Shut your mouth, you bastard!”

“Ah.”

Taishan had been bouncing with excitement, but shrank back at my thunderous shout. For some reason, Namho was still perched on his shoulders, riding him like a human throne. He spoke with a serious expression.

“But when are you planning to take that hand out?”

He’d hit the nail on the head.

I kept my cool and answered without panicking.

“I was just waiting for the right moment.”

“Mm. In a situation like this, it can’t be easy to pull it out.”

“Thank you for understanding.”

“Still, there are a lot of eyes on you. You should pull it out now. Don’t do it slowly—do it quickly.”

“May I ask why?”

“If you move slowly, people will stare longer. Here, I’ll count to three. Pull it out exactly when I get to three.”

“That sounds like a good idea, but I think saying that has drawn even more attention.”

Namho looked around, then nodded with an impressed expression.

“That’s true.”

“Please just stop talking. For a little while—even just a little while.”

“Understood.”

Leaving Namho behind as he quietly shut his mouth, I took a small breath.

Then I carefully spoke to the one person standing beside Hyuk Mujin and staring off in the other direction.

“Young Lady Ju.”

The next moment—

*Whoosh. Bam!*

As Ju Hwaran bolted out of the room at a speed I’d never seen from her before, Hyuk Mujin came over and patted my shoulder.

“I understand exactly how you feel, Captain.”

“……Shut it.”

“Yes, sir.”

I wished it had just been a dream.
## Chapter artifact 931

# Chapter 931

Everyone needs some time alone.

Say, when you need to check the System messages piled up until they’re ready to burst, like emails in a portal account you haven’t opened in years.

Especially if you’ve just groped your own private parts in front of a dozen people, then shuddered all over.

But even after I’d endured an incomprehensible nightmare—and a situation more horrifying than the nightmare itself—people seemed determined not to leave me alone.

“Now, please raise your arm and follow my movements.”

“Very good. This time, turn it at a slightly different angle…”

“Can you see how many fingers I’m holding up?”

My first visitors were the imperial physicians, who came charging in as soon as word spread that I’d regained consciousness.

They’d apparently been waiting on the Emperor’s strict orders since three days ago. Reeking of herbal decoctions, they had me do this and that, then huddled together with grave expressions and whispered to one another.

Of course, I could hear every word perfectly.

“His condition is normal—no, perfect.”

“I heard there was an enormous battle, but he’s bizarrely unharmed. Not a single wound.”

“That’s not all. If you look more closely, the front of his robe is suspiciously bulging.”

“What? You mean that could be…? No, that can’t be. It’s impossible.”

“To be honest, I’m not certain either. I’ll give you a signal when the opportunity arises. You can press it once, pretending it was an accident.”

“Hmm. Understood.”

The physicians finished their brief discussion, turned around with gentle smiles, and suggested they examine me one more time, just in case.

I answered without hesitation.

“Get out. Now.”

But even after the physicians left, there was no end to the people coming to the pavilion where I was staying.

“Um, Captain. Someone’s here to see you.”

“Who?”

“Just a moment. They say they were appointed Guanglu Dafu the day before yesterday.”

“What exactly does a Guanglu Dafu do?”

“If I knew that, I wouldn’t have become a martial artist.”

“Even just hearing the title, he sounds like a scammer. Tell him I’m not taking out a loan.”

“Yes, I’ll pass that along.”

I only learned that the Guanglu Dafu was an official whose rank came just below the Three Excellencies after turning away dozens of officials. Then, at last, I welcomed a new visitor.

“I hope I’m not too late. Looking at the crowds already gathered outside your door, you’re quite the popular man.”

His voice was warm and familiar.

Hong Jin came in with a joking air, and a smile spread across my face too.

“Comrade Hong.”

“Comrade? Have I ever told you? Even though it was an official title, whenever Young Master Jin called me Comrade, it always made me feel I could count on you.”

His expression was full of mischief. But Hong Jin’s eyes and voice held a feeling beyond words.

“Thank you. Truly. His Highness, the Emperor’s younger brother and heir, couldn’t come with me today, but I hope you know he feels the same way.”

*Swish.*

Hong Jin straightened his navy-blue robe, embroidered with ornate patterns, and bowed with the utmost respect. Then he raised his head and smiled as though nothing had happened.

“Oh, and I got promoted. From now on, don’t call me Comrade Hong. Call me Eunuch Hong.”

“Eunuch? Don’t tell me…”

“You’re thinking of exactly the right thing, Young Master Jin. I felt guilty and ashamed that I’d spent all those years suspecting His Majesty without knowing the truth. I turned down the position several times and even tried to retire to the countryside, but…”

Now wearing the uniform of the East Depot, a sight I’d grown fairly used to, Hong Jin continued with a faint smile.

“His Majesty said, ‘There’s so much left to take care of. How can you try to run off on your own? I’m not letting you go, if only because you’ve got the nerve to try.’”

“That’s good. Truly.”

It was good news—and the right outcome, too.

In truth, Hong Jin’s hostility toward the Emperor over the past decade or so wasn’t something he could be blamed for.

It had happened because the Emperor had deliberately hidden the truth. And, putting everything else aside, the fact that he’d kept Hong Jin by Zhu Bao’s side was proof of how much he trusted his loyalty.

“So, Comrade Hong—no, Eunuch Hong—have you become the East Depot’s new Cang Gong?”

“I’m responsible for the East Depot, yes. But the position of Cang Gong—the Seal-Holding Eunuch—may remain vacant forever. It’s the Great Nation’s way to leave no trace of a traitor behind. Besides…”

For a moment, Hong Jin’s eyes turned cold.

“There are still roots we haven’t pulled up.”

I thought I knew what he meant by “roots.”

In the broadest sense, it could mean the entire East Depot, where the Eastern Heaven Demon Lord’s shadow had fallen most heavily. More narrowly, it could mean one man whose death had not been confirmed by the time I lost consciousness.

“Ma Sanbao.”

At the name that slipped between my lips, Hong Jin gave a small nod.

“We searched the capital and hundreds of miles around it for the past three days, but there’s no trace of him. It’s as if he vanished into the sky.”

Honestly, I couldn’t help admiring Ma Sanbao, at least a little.

He’d managed to escape in the middle of that desperate situation—and then evade the Imperial Army’s pursuit for three straight days.

*He must have been badly wounded already. How did he disappear?*

Of course, it was entirely possible.

Even if he fell far short of his master, the Eastern Heaven Demon Lord, Ma Sanbao had still reached the Supreme Peak realm and was a monster with incredible powers of recovery. And his disguise technique, which could change his face and build, was good enough to make even me whistle in admiration.

*Lastly, he could’ve used a Moving Formation Dark Heaven had hidden somewhere nearby.*

Ma Sanbao was someone who had to be killed to eliminate future trouble. But if he’d already fled somewhere beyond our reach, there wasn’t much we could do.

For now, the best course was to prepare for the prey that hadn’t escaped the net yet—and the predators approaching from far away with their presence concealed.

“Comrade Hong… no, Eunuch Hong.”

Hong Jin smiled at me.

“Call me whatever you like. You’re allowed, Young Master Jin.”

“Hey, Hong.”

“…You really do make yourself at home. What is it?”

“Can I ask you a favor?”

“Why even ask? I’d do anything for you, Young Master Jin—anything but treason. So, name it.”

“Then…”

Hong Jin had answered so readily, but at my request he blinked in surprise.

“Hm?”

“Can’t you do it?”

“No, it’s not a difficult favor. I’m just wondering what it means.”

“It’s very important. I’ll tell you more precisely after I check it myself.”

“Of course you will. You can’t just expect me to do it for nothing. You’re making use of an East Depot eunuch, after all.”

Hong Jin joked as he stood and left. Hyuk Mujin, who’d been watching for an opening, sidled over and spoke.

“Um, Captain.”

“You’re wondering what that favor was?”

“Wow. You really are a mind reader.”

Even now, Hyuk Mujin raised his thumb and tried to butter me up. I chuckled and shook my head.

“There is something.”

“Wait, you’re keeping it secret from me too?”

“It’s not exactly that…”

“Not exactly?”

“I don’t know either.”

“……?”

Hyuk Mujin stared at me with a deeply unimpressed look.

“If you just don’t want to tell me, then say so. Don’t make me feel even more pathetic.”

“I’m serious, you idiot.”

“Forget it. Don’t talk to me for a while. I won’t talk to you either.”

As he headed for the door, making a big show of how offended he was, I called after him apologetically.

“Get back here before I count to three. One.”

*Whoosh.*

Hyuk Mujin returned to his spot before I could count to two, then asked while pretending to look elsewhere,

“So, what was it?”

“I told you. I don’t know exactly what it is either.”

“…For real?”

“Yeah. Someone just told me about it. Not in detail—just the gist.”

“Who?”

“Someone you know, too.”

Hyuk Mujin tilted his head, then thumped his chest with a confident look.

“Tell me who it is, and I’ll bring them here right away. Then you can hear all about it in greater detail…”

“That won’t work.”

I cut him off and added,

“That person’s already dead.”

“What?”

“They’re dead. And I killed them myself.”

That was when Hyuk Mujin, who’d been staring at me with his mouth hanging open, suddenly widened his eyes.

“Y-you don’t mean…? No, right?”

“I told you, so go. Leave me alone.”

“Wait, why would that bastard tell you…?”

“Get out before I count to three. And deal with whatever comes after on your own. One.”

*Whoosh.*

That sure works.

I let out a hollow laugh at the empty spot where Hyuk Mujin had been. He’d vanished before I could count to two.

Then I sank into the soft silk bedding and stared out the window, bright enough to make it hard to believe it was night.

*It’s bright. And loud.*

Even from this pavilion deep inside the Inner Palace, I could hear the distant cheers and songs carried on the wind.

Fireworks shot up here and there, painting the night sky in brilliant colors. The people, welcoming a new era, would have forgotten sleep and poured into the streets, laughing, talking, and drinking all night.

Leaving tomorrow’s worries behind to enjoy today’s happiness to the fullest.

*You wanted a world like this once, too.*

I thought of someone who no longer existed in this world.

The man who had laid down all the anger left in his heart at the very end and died as a human being. The Eastern Heaven Demon Lord.

And the Sound Transmission that had been all but his last words.

*“Remember every word I say from this moment on.”*

What he said next was short and simple.

Find one thing in one particular place.

That was all.

*And I’d find out what that thing was soon enough.*

I didn’t know either. I had no idea what that thing was, the one the Eastern Heaven Demon Lord had mentioned at the very end, or what it contained or meant.

But I decided not to think about it anymore until I could see it with my own eyes.

There were things I needed to deal with right now.

“Open System window.”

The instant the quiet words slipped from my lips—

*Ding. Ding. D-d-ding!*

A mad chorus of chimes rang out, and countless holographic windows filled my vision.

For a very long time.

As if they’d been waiting for this moment alone.
## Chapter artifact 932

# Chapter 932

“Open System window.”

At that brief command, the dam blocking the floodgates came crashing down.

*Ding. Ding. D-d-ding!*

A chorus of chimes rang out, overlapping again and again.

At the same time, countless holographic windows surged toward me like a giant wave. My mouth fell open before I could stop it.

*Holy shit. Why are there so many?*

It felt like staring at all the homework I’d put off over the entire summer vacation in elementary school. No—worse than that.

Even at a glance, well over a hundred holographic windows packed the air around me.

*It’d be nice if they were all Level-up notifications.*

Of course, that was nothing but wishful thinking. And there was no way all those holographic windows had piled up in just the past three days.

I started with the first System message to appear and read them in order.

> **System**
> Congratulations! Update is complete!
>
> We sincerely regret any minor inconvenience caused by the Update.

“……”

Minor inconvenience. Sincere regret.

Well, I’m already pissed off.

The memories of coming close to death because of that very “minor inconvenience” came flooding back. But the next message quickly cooled my anger.

> **System**
> Therefore, as an apology, we would like to provide you with an appropriate Reward.

“Oh.”

Right. That’s more like it.

This System was fundamentally different from those garbage games that wielded the Four Great Swords—scheduled maintenance, unscheduled maintenance, extended maintenance, and emergency maintenance—like an heirloom blade.

Giving you a fitting reward for all your hard work and doing everything it could to make the user’s experience more enjoyable—that was the true purpose of a kingly, god-tier System.

> **System**
> Update Reward has been delivered to your Inventory.
>
> Would you like to check your new Item?
>
> **Y / N**

Reward. New Item.

Those two unremarkable words awakened the childlike wonder I’d long forgotten.

This was even more thrilling than opening the Christmas present I’d gotten when I was seven.

With excitement and joy mingling inside me, I answered.

“Open.”

*Ding.*

> **System**
> **Item Window**
>
> Pocket Watch of Unknown Make
>
> **Type:** Item  
> **Grade:** None  
> **Restriction:** None  
> **Description:** A pocket watch made by someone unknown. Very sturdy. At a glance, it looks like an old, broken watch. Even on closer inspection, it still looks like an old, broken watch.

“……?”

What the hell is this?

My brain stalled. I stared blankly at the pocket watch in my hand.

It was exactly as the Item description said.

At a glance, it looked broken. On closer inspection, it still looked broken. I could’ve written an entire poem about it on the spot.

*Title: Pocket Watch.*

*It looks old up close.*

*It stays broken no matter how long I look.*

*Fucking sucks.*

“……”

I felt like I was going insane.

It was on par with the betrayal I’d felt when Santa Claus—the old man who’d brought my Christmas present when I was seven—had punched in the front door’s passcode and strolled in like he owned the place, then kissed my mom right in front of me.

*This is my… Update Reward?*

My head still buzzing, I tried to pull myself out of the shock.

*No, no. This can’t be right.*

There were only two possibilities.

Either the System had prepared a surprise hidden-camera prank for me, exhausted as I was from everything I’d been through, or there was something special about the watch that I hadn’t figured out yet.

*There was only one notification, so it’s not a prank. Which means…*

I gathered my scattered wits and carefully examined the watch in my hand.

It didn’t take long to notice something I’d missed on the back, polished smooth by someone’s touch.

*Wait.*

The mark was so faint it had nearly vanished—probably too faint for an ordinary person to see.

I stirred up my internal energy and sent it toward my eyes. With my enhanced vision, I made out the dim inscription.

“N-no way…”

> A broken clock is right twice a day.

“It doesn't mean a damn thing, you bastards!”

*BANG!*

I hurled the pocket watch with all my strength. It flew like a cannonball and struck the wall.

Or, to be precise, it smashed through the wall.

*Rumble!*

The wall crumbled apart. Beyond it, Hyuk Mujin stood staring at me with his mouth hanging open.

“What the—Gasp! Was that an assassination attempt?!”

In a way, it was.

I’d taken a hit to the back of the head like that with absolutely no warning, and now my insides ached as if I’d been stabbed.

“Mujin. I’m dizzy. Mujin.”

“Captain! Stay still! I’ll protect you!”

“You? Protect me?”

Hyuk Mujin hesitated, then cautiously offered, “Should I bring Great Hero Jeok over?”

“……If you call him, we’re the ones who’ll get put through the wringer. Don’t.”

“Oh, come on. You scared me. It wasn’t an assassination attempt, right?”

“Yeah, idiot. So quit making a scene and go pick that thing up.”

Hyuk Mujin coughed in the cloud of dust rising around him, then cautiously picked up the pocket watch.

“C-Captain. The thing you mentioned isn’t this piece of iron junk, is it?”

“……”

“Sorry. I guess it is. And, just in case, I take back the ‘junk’ part.”

As befitting an unlucky eunuch, Hyuk Mujin had sensed my foul mood and hurried over to hand me the watch.

“But what exactly is it?”

“A broken watch.”

“A watch? This little thing?”

I answered in a mournful voice as Hyuk Mujin eyed the unfamiliar shape of the pocket watch.

“It’s still junk. Very sturdy and completely useless.”

“Why would you keep something like this? It’s even broken.”

“……I got it somehow, okay? Watch your mouth.”

Every word was a blade, digging into my heart.

I’d confirmed the watch’s durability by accident, and now I swallowed back the tears welling up inside me.

*The Item description was telling the truth after all.*

Some truths could be unbearably cruel. This pocket watch was one of them.

*But why would the System give me something like this?*

This wasn’t some ordinary Quest. It was the Reward I’d received for completing an entire Update, and it was garbage like this.

I clung to one last sliver of hope and examined the watch again. But what awaited me was an even greater humiliation.

*This thing really is broken.*

For starters, the time was completely wrong.

It was already nearing midnight, but the hour hand pointed somewhere around five.

And the numbers that should’ve been there were missing, so I had to estimate its position by eye.

*And where the hell did the minute hand go?*

At this point, I wasn’t sure I could even call it a pocket watch.

A pocket watch. Maybe a pocket dial. Even that seemed generous.

*I can’t adjust the time, either. And it doesn’t look like it’s moving. What the hell is this thing?*

I shook it this way and that, then pressed it right up to my ear. There wasn’t so much as a ticking sound—not even the faintest noise of its inner parts turning.

It had only one advantage: it was so sturdy I couldn’t crush it no matter how hard I squeezed, and couldn’t even scratch it.

*Did they give it to me as a weapon? Or a shield for emergencies?*

A familiar scene from a war movie suddenly flashed through my mind.

A sharp gunshot rang out. Private Johnson collapsed.

But when his squadmates rushed over, sure their comrade was dead, they found a bullet lodged in the little Bible he always carried over his heart—he’d been a devout believer, after all…

“Wow. This is already driving me insane.”

Hyuk Mujin, who’d been watching me warily for a while, cautiously spoke up.

“Um, Captain?”

“Don’t call me in that sly, eunuch-like voice. I’ll kill you. Seriously.”

“Yes, sir. May I ask you something?”

“Spit it out.”

“Um… are you going to throw that away?”

Hyuk Mujin pointed discreetly at the pocket watch in my palm, then kept talking as though he were making casual conversation.

“If you are, I’d like to humbly suggest giving it to someone who’s your right arm, your heart, and unwaveringly loyal to you.”

“Was that supposed to be humble? You sound pretty confident.”

“Well, I’m just saying. If you’re not going to use it, there’s no reason to keep it.”

“Why the hell do you want this thing?”

“It’s a watch, isn’t it? And judging by the look of it, it’s a rare item from the Western Regions. Even if it’s broken, wouldn’t it look cool to carry around?”

Hyuk Mujin made a surprisingly coherent argument. I quietly smacked my lips.

*I guess it wouldn’t really matter if I gave it to him…*

But something about it bothered me. Like a fish bone stuck in my throat.

If I handed this godforsaken pocket watch to Hyuk Mujin right now, I’d feel worse than if I went to a Chinese restaurant and ate fried rice without a bowl of spicy jjambbong broth.

*There might be something I don’t know about it yet. I can wait a little longer and see. If I decide it really is junk, I can give it to him then.*

It wasn’t as if the System always gave out incredible Rewards.

I didn’t know exactly how it decided what to hand out, but after completing countless Quests, I’d received plenty of useless junk Items.

They said many a little made a mickle. My Inventory was now packed with enough junk to fill a truck.

The one thing that bothered me was that this broken pocket watch in my hand was the Reward for completing an Update.

“Hmm.”

I only nodded, without saying a word. Then Hyuk Mujin’s sly voice reached my ear.

“Um, Captain?”

“What?”

“Could you give me an answer?”

“Not yet. Just wait a little. A month—or, no, half a month.”

Half a month. Half of one month.

That was the final trial period I’d decided on, and Hyuk Mujin’s face lit up.

“So you’ll give it to me in half a month?”

“Yeah. Assuming I’ve confirmed it’s useless to me, of course.”

“Come on. It came from the Western Regions. There probably isn’t a craftsman who can fix it around here. At most, you can carry it around because it looks pretty.”

Hyuk Mujin grinned unpleasantly as he went on.

“But what do you call it?”

“Pocket-watch, shi—pocket watch.”

“Wow. That’s a lovely name. You could thread a leather cord through that ring and wear it around your neck. It’d draw eyes wherever you went.”

“Yeah?”

“Yes. A shiny silk cord would look even better than leather.”

“Oh, yeah?”

It was a suggestion worthy of the eldest grandson of a wealthy textile-merchant family. And quite a good one, too. Without hesitation, I tore a strip from the gold silk robe I was wearing, threaded it through the ring, and hung the watch around my neck.

“How do I look? Pretty?”

“Whew. Is your name Mr. Golden Sun? You’re practically glowing.”

“They’d like it if I gave it to them like this, wouldn’t they?”

“Captain, you’d go that far for me…”

Hyuk Mujin’s eyes trembled with emotion. I gazed fondly at the pocket watch hanging around my neck and continued.

“Not you. Young Lady Ju.”

“……”

“Maybe Young Lady Ju would be less upset if she got a gift like this. Don’t you think?”

“……”

“Answer me.”

“……I’m sure she’d love it. Yes.”

His eyes had gone cold in an instant.

As Hyuk Mujin silently berated me with his gaze, I sensed dozens of people approaching the pavilion. I leaned out the window.

“Stop! Stop! Stop! Move and I’ll cut you down. Pocket watch!”

At the head of the Embroidered Uniform Guard, their torches flickering, Jeong Hogun fell silent for a moment before replying.

“What nonsense are you talking about?”

“You stupid, useless Embroidered Uniform Guard bastard! You showed up without even learning the password!”

“No, I mean, what is this all of a sudden…?”

“Shut up! Say ‘watch’! Hurry!”

“……Watch.”

“I said shut up!”

“……”

With that angry, venomous look in his eyes, like an enraged pufferfish, it seemed I’d better stop messing with him.

I generously decided to let him off the hook and asked Jeong Hogun, who’d clamped his mouth shut.

“So, why are you here?”

“You need to come with me for a moment.”

“Am I someone who comes and goes just because you tell me to? Besides, I’m really busy right now. I’ve got a lot to do.”

“His Majesty has summoned you.”

“Oh.”

Then I’d better go.
## Chapter artifact 933

# Chapter 933

I followed Jeong Hogun, taking a careful look around as we went.

Contrary to what I’d expected, the Imperial Palace hadn’t changed much since my first visit. No dramatic transformation or anything.

Palace attendants in neat uniforms hurried back and forth, while the heavily armed Embroidered Uniform Guards stood watch at their posts like iron towers.

But if there was one big change, it was me.

*Swish.*

When a group of palace attendants coming from the other direction bowed deeply as they passed, I thought it was just a coincidence.

*Clank.*

Even when the Embroidered Uniform Guards, standing watch with a formidable air, struck their armor and saluted, I didn’t think much of it.

I just assumed it was because Jeong Hogun—a man with considerable pull even among the Embroidered Uniform Guards—was accompanying me.

“Guess being a Thousand Captain means you can throw your weight around, huh?”

But Jeong Hogun’s reply to my joking remark was utterly calm.

“You’re less observant than you look.”

“Hm?”

“They aren’t paying their respects because I’m here.”

Only then did it hit me.

Only then did I see it.

The gazes of the people passing around us—their eyes filled with gratitude and respect—were fixed solely on me.

“Uh…”

What was I supposed to say?

I hesitated, at a loss for words, when Jeong Hogun’s steady stride came to an abrupt halt.

No—not just his. Everyone who’d come with him stopped at the same time.

*Clop.*

With a movement as sharp as a blade, they rang with the heavy sound of metal.

A dozen or so jang away, Jeong Hogun glanced at the plaque that read *Qianqing Palace*, then turned to look at me.

“We may not get another chance to see each other, so I should say this now.”

The sharp eyes visible beneath his low-pulled helmet softened in an instant, curving like a crescent moon.

“It was an honor to fight alongside you, Blazing Flame Divine Dragon Jin Taekyung.”

“……!”

I stared at Jeong Hogun, eyes wide.

The back that had never bowed to anyone but the Emperor, the stiff neck—both were inclining toward me.

Along with a most respectful fist-and-palm salute.

“Until we meet again, I wish you good fortune in battle.”

“We wish you good fortune!”

*Ching, ching, ching!*

Dozens of Embroidered Uniform Guards shouted in unison and drew their swords, gripping them in reverse.

They stood in two neat rows on either side of the path leading to Qianqing Palace. I couldn’t help but burst out laughing.

“Come on, you’re making me blush.”

But I stopped laughing almost at once and returned their salute, bringing my hands together.

“See you again sometime. We will.”

A few words, spoken from the heart.

That was enough.

No one knew when we’d meet again, but I decided to leave the rest of the conversation for that day.

Every meeting, every bond, eventually came with a parting.

*Clop. Clop.*

I walked slowly along the path Jeong Hogun and the Embroidered Uniform Guards had made for me.

Beneath the high eaves of Qianqing Palace, the twin armored guards were waiting. A new scar finally let me tell their faces apart.

And as if no formalities were needed, they silently stepped aside instead of blocking my way as I came up the stairs.

The enormous iron gate they guarded stood wide open, unlike the last time I’d visited.



* * *



Qianqing Palace stood in the deepest part of the Imperial Palace.

And in the deepest part of Qianqing Palace, the Emperor was waiting for me.

“Oh, you’re here.”

His tone was gentler than before, his voice warm with welcome.

And his eyes were smiling.

But even with the welcome of an Emperor known as Iron Blood for his countless purges and ruthless decisions, even before his accession to the throne, I didn’t smile.

No—to be precise, I couldn’t.

*Why?*

I hadn’t said it out loud, but apparently I hadn’t managed to hide my bewilderment. It showed in my expression and my eyes.

The Emperor watched me searching for something to say, then gave a quiet laugh and spoke first.

“You seem rather taken aback. I suppose it’s understandable, given that the Son of Heaven looks like this.”

He tapped the bandages wrapped around his upper body.

His cheeks were sunken, made all the more prominent by the faint smile at the corner of his mouth.

“If I may offer you one piece of advice, it’s best to lower your head first at times like this.”

The Emperor looked absurdly gaunt compared to just three days ago. My shock hadn’t eased, but I forced myself to reply calmly.

“Is there a reason for that?”

“Two. First, you can hide your expression. Second, you buy yourself a little time to think.”

“I see. Since we’re here, I’ll give it a try too.”

I lowered my head for a moment, then lifted it again before even ten seconds had passed.

“I’ve already been found out, so there’s no point trying to hide my expression. But I have to admit, it does give me time to think.”

“May I ask what you thought about?”

“I wondered why Your Majesty looks like this. And what the reason might be.”

“You’ve been thinking about something pointless. I simply overexerted myself in that battle.”

The Emperor smiled and waved a hand, but the smile vanished without a trace when he heard my next words.

“So you’ve taken poppy again?”

“……!”

“I was a little slow to notice. Your Majesty’s appearance caught me by surprise, and I didn’t pay attention to the smell around me.”

I took a slow breath as I looked at the Emperor’s face, gone rigid. The heavy, peculiar scent drifting into my nose was unmistakably familiar.

“How long… have you known?”

The Emperor’s voice had sunk low. I thought back to the first time I’d stepped into Qianqing Palace.

I remembered the strangely familiar scent I’d sensed from the Emperor I finally met—and the moment I learned the truth through someone who occasionally smoked poppy.

“I didn’t know at first.”

“I can’t imagine how you figured it out. It’s not something you can easily get on the street, and I’d heard Murim practitioners avoid anything that harms the mind and spirit.”

“You’re right. They generally do.”

I added calmly,

“But I hear eunuchs sometimes use it.”

“……Hong Jin, then.”

A wound, once inflicted, has a long shelf life.

Whether the cause is psychological or physical, the human mind and body remember it clearly.

Even decades later, after the scars have faded, old wounds still ache. How much worse must it be for eunuchs, who’ve had their most private parts cut off?

Hong Jin was no exception.

Whenever the pain struck without warning and he couldn’t bear it, he turned to poppy. That was how I’d accidentally learned one of the Emperor’s secrets.

“How long have you been using it, and why?”

“Well. I don’t see why you need to know.”

Before I could say anything, the Emperor gave a bitter smile and gestured toward his own head.

“And even if I told you, it wouldn’t change much.”

“……No way.”

He seemed to have already given up. And that gesture had meaning, too.

The Emperor moved his dry lips as I stared at him, eyes wide.

“That’s right. What you’re thinking.”

“……!”

“The Blood Soul Gu. That cursed poison has already reached my very marrow.”

The moment my suspicion became certainty, a curse escaped me with a groan.

“Damn it.”

“Impertinent. To say something so vulgar in front of me, the father of all the people. If Commander Baek were here, he’d have you dragged to the prison at once.”

Someone else might have trembled and begged forgiveness, but I only sighed at the Emperor, who was making a show of frowning.

“Is this really the time for jokes?”

“Have I ever told you I’m good at jokes?”

“This is the first I’ve heard of it. And you’re so bad it gives me goose bumps.”

“That’s because you’re a dull fellow. Back when I was campaigning on the battlefield, I’d drink and laugh with my men every night. Those were good times.”

“I hate to say this to a critically ill man, but you were probably the only one having fun.”

“That can’t be. Every time I said something, they’d laugh until they doubled over.”

“……I see.”

I didn’t know who his men had been back then, but they must’ve worked hard to laugh along.

Not that any of that mattered right now.

I shook my head at the tactless commander—or rather, Emperor—and asked what I was most curious about.

“When did it start?”

“More than ten years ago. Just after the coup, to be exact.”

The Emperor continued calmly, as though there was nothing left to hide.

“A trusted loyalist did it. By the time I realized, it was already too late.”

“Who among Your Majesty’s inner circle knows?”

“Only two people. Baek Yeon and So Gyo. Though perhaps I should call her the Bow Saint now.”

The Emperor looked at me and added,

“And here, today, one more person has learned a truth that must never be known.”

I understood what he meant at once and clicked my tongue.

“Are you going to kill me to keep me quiet?”

“If I tried, would you let me?”

“Not a chance. I’m going to live until I’m so old I’m smearing shit on the walls.”

“In that respect, I’m much better off. I can’t disgrace myself like that as Emperor.”

That was when it happened.

The Emperor, who’d been chuckling softly, suddenly gave a small cough.

*Cough.*

His golden sleeve stained red. I looked around, my face hardening at the sudden spitting of blood, but the Emperor shook his head before I could move.

“Don’t bother.”

“Bother with what?”

“If you’re thinking of calling an imperial physician, don’t.”

“……”

“If their medicine could’ve treated this, I would’ve sought their help long ago. Why do you think I hid this even from the imperial physicians?”

The Emperor gazed at his blood-soaked sleeve and murmured as though to himself.

“My father and mother. My three elder brothers. And the senior members of the imperial family who worked so faithfully to protect the ancestral shrines and the state… Not one person was spared. They all died.”

That was right. No one had escaped the Blood Soul Gu’s grasp.

That was why his attempt to set everything right after the coup had come to nothing.

The late Emperor, the Empress, and several direct members of the imperial family, including the Crown Prince, had died one after another. The Fourth Prince who’d started the coup was branded an unfilial son and an unforgivable usurper.

“I have no regrets left. I took every elixir I could to stay alive, and trained in martial arts until my bones ached, trying to overcome the Blood Soul Gu’s poison. I endured like that for ten years.”

At last, I understood.

Why he—the man who held the greatest territory in the world and commanded countless troops—had reached the realm he stood in now.

“After enduring a winter that lasted more than ten years, spring has finally come. That’s enough for me.”

Right now,

a clear smile rested on the Emperor’s lips.
## Chapter artifact 934

# Chapter 934

Winter comes for everyone.

But the winter one man—an emperor, or rather a man named Zhu Di—had to endure was exceptionally harsh.

More than ten long years.

For all that time, long enough for the world to change beyond recognition, he fought against illness. He had to learn martial arts just to stay alive, and not a single day passed when he could sleep easy, with the blades of rebellion lurking on every side.

*Spring, regained after such a long wait.*

The Emperor smiled bitterly.

At last, the long winter had ended, and warm spring had come. Yet he still shivered with cold.

“I was prepared for this. Have been for a long time. So…”

The Emperor murmured calmly, then fixed his gaze on the young man before him.

“You don’t need to look at me like that.”

Someone had once said that the back of a person who had given their all was beautiful.

But there was nothing beautiful about someone wasting away after giving everything they had.

It only stirred up a bitter, indistinct sadness.

That was exactly the look in the eyes of the young man staring at the Emperor now: Jin Taekyung.

“How much time do you have left?”

“That’s a question for the heavens.”

“This isn’t the time for jokes.”

“Did it sound like a joke?”

“……”

“Even making it this far is a miracle. If I hadn’t learned martial arts, and if I hadn’t had the help of Baek Yeon and the Bow Saint, I’d already be dead.”

The vitality and physical strength of a Supreme Peak master were beyond comparison with those of ordinary people.

That was why the Emperor had learned martial arts—not to become stronger, but solely to survive.

He had to grow stronger to resist the Blood Soul Gu’s poison.

But even that precious time he had bought himself was now drawing to a close.

“Not long ago, I found myself wondering something. If I’d been born with martial talent like yours, perhaps I could’ve completely suppressed the Blood Soul Gu.”

“Don’t talk like you’re helpless. Making it this far is already incredible. If you don’t give up and keep working at it…”

“Do you really believe that? Sincerely, without a trace of pity or deceit?”

Jin Taekyung was at a loss for words. The Emperor continued, his voice calm.

“I don’t need half-hearted comfort. I know reality better than anyone.”

Despite having been taught by two peerless masters—the Bow Saint and Baek Yeon—and having absorbed all manner of elixirs, he had only reached the early stages of Supreme Peak.

Of course, the Blood Soul Gu’s poison had made learning martial arts no easy task. But the fact that even bone-deep effort and the finest possible conditions hadn’t brought him any further meant one thing.

A limit.

This was as far as he could go.

The Emperor had neither the talent to break through the enormous wall in front of him nor the time to do it.

*Ka-koff. Koff.*

The Emperor’s complexion was pale as he let out a series of small coughs. That was when Jin Taekyung’s quiet voice reached him.

“What if there’s still… a chance?”

“A chance.”

It was a word he hadn’t heard in a long time.

And at the same time, the Emperor already knew what Taekyung meant by it.

“It’s too soon to give up.”

“Yes, I suppose you could think that. You trust the Divine Physician that much.”

“……!”

“Now that I think about it, there were three of you, not two. Three people who knew about my condition.”

At the sight of Jin Taekyung frozen with wide eyes, the Emperor gave a quiet laugh.

“He came to see me three days ago.”

Taekyung fell silent.

There was no need to ask how the examination had gone. Everything the Emperor had said and done until now was proof enough.

“He said it was too late. He shook his head and said there was nothing he could do about it for now.”

It was the judgment of the Divine Physician, whose medical skill was the greatest under heaven.

Unless the Great Firmament Immortal got involved, it was as good as confirmation that this was an illness no human being could overcome.

“And yet, all of a sudden, I felt ridiculous.”

The Emperor continued with a bitter smile.

“I thought I’d already prepared myself for everything and accepted it long ago. But when the Divine Physician confirmed it, I felt as if something inside my chest had gone hollow.”

At last, spring had come.

No—he had reclaimed spring.

He had lived fiercely, and wanted to keep doing so.

But he didn’t have much time left.

“Earlier, I told you I had no regrets left. That I was content.”

Taekyung, who had been silent, parted his lips.

“I know. I knew you didn’t mean it.”

“Yes. You’re right. It was all a complete lie.”

The Emperor breathed heavily.

The crushing pressure on his chest at that moment, as if an enormous boulder were weighing it down, wasn’t caused only by the Blood Soul Gu that had eaten away at his body and mind over the years.

“There’s… so much I have to take care of before I die.”

The Emperor knew.

The spring he’d fought so hard to reclaim, its warmth, was only a passing breeze—a brief respite.

Before long, a cold frost would fall over the land and blanket it all.

“There will be a war. One more brutal and devastating than any before it.”

The calm before the storm.

Four characters that described the current situation more accurately than anything else.

And at the same time, it was the weight someone would have to bear when he stood as ruler of the continent after the Emperor.

“Bao’er.”

One person’s name slipped from the Emperor’s dry lips.

Prince Shangshan. No—the Crown Prince, Zhu Bao.

His last lingering attachment, the one who made him look back again and again at the end of his life. His flesh and blood, so precious he could never bear to see him hurt.

The little boy who wasn’t here had become a great boulder, pressing down on the Emperor’s chest.

“He’ll surely become a sage king. He’ll be loved and praised by all the people, and bring peace and prosperity to this land.”

But peace had already been broken.

To survive the flames of war that would sweep across the continent, the boy would have to become a ruthless ruler, not a sage king.

“That burden will be too much for him.”

The Emperor knew better than anyone how heavy and overwhelming the two words *Son of Heaven* could be.

Perhaps by the heavens’ grace, his youngest brother had been born with the qualities of a sage king. But he was still far too young.

Too young to rule a nation.

And too young to weather a war.

*I want to live. I still have things to do for that boy, for this country and its people.*

The Emperor murmured to himself.

He knew reality wouldn’t change no matter how desperately he wished it would, so he had to swallow his words. And because he was the ruler, who must never waver, he couldn’t say them aloud.

*What’s the point of lamenting? It’s all futile anyway.*

The Emperor gave a bitter laugh. That was when—

“Did you know?”

Jin Taekyung spoke up without warning, fixing his gaze on the Emperor as he continued.

“There are two main ways to piss someone off. The first is to start saying something and then stop, and the second is…”

His voice trailed off, and silence followed.

The Emperor waited patiently for the rest. Then he couldn’t hold back any longer.

“The second is what?”

“Hm?”

“I asked what the second one is.”

“Oh, that.”

Taekyung blinked, as though he’d just remembered something he’d forgotten long ago, and scratched his chin.

“I just won’t tell you. Let’s move on.”

“……What?”

“What does it matter? You didn’t finish what you were saying, either.”

“What are you talking about—”

The Emperor was so dumbfounded he was about to continue, but Taekyung spoke first.

“Just be honest. Tell me you want to live.”

“……!”

“Is that so hard?”

The Emperor’s pupils trembled.

It wasn’t because of Taekyung’s wildly disrespectful behavior.

It was the embarrassment of having his tightly concealed truth laid bare, as if he’d been stripped naked.

“I am… the Son of Heaven.”

“So what? The Son of Heaven isn’t a person?”

“That’s enough!”

The Emperor’s low shout didn’t faze Taekyung. He fired off his words like a machine gun.

“When someone says something hurtful, it hurts. When you get cut by a blade, you bleed. When you’re facing a hard reality, you lose heart. It’s the same for everyone. What’s different about wearing golden silk embroidered with dragons and looking down on all the civil and military officials?”

“……”

“You said you didn’t need half-hearted comfort. Fine. I won’t give you any. But you need to be more honest, too. Forget being the Emperor or anything else—just act like a person for a little while.”

The Emperor, his face clouded with confusion, wondered to himself:

Why had he summoned Jin Taekyung here today? Why had he let out thoughts he’d never shared with anyone?

And why, despite being subjected to such insolent behavior, did he feel no anger?

Then, at last, he let out a quiet laugh.

“Do you know something?”

“I don’t. Except that you’re feeling better than I expected.”

“But I haven’t even said anything yet.”

“That’s why I said I don’t know. I’d have to hear it to know. How could I know if I haven’t heard it?”

“Ha! Ha-ha-ha!”

The Emperor suddenly burst into loud laughter. Before long, he coughed up blood and muttered,

“Damn it.”

“I didn’t know you knew how to swear.”

“You said the Son of Heaven was a person, didn’t you?”

“Oh. Yeah, I did.”

“……Still, don’t drop the formalities.”

“I was talking to myself.”

“What do you think would happen if I muttered to myself that you’d just tried to assassinate me?”

“That wouldn’t work. That’d be spreading false information.”

“You made me cough up blood, so it wouldn’t be entirely false.”

“You’ve got a real talent for twisting things.”

“This is getting more and more absurd. Is that any way to speak to the father of all the people and the Emperor of the Great Nation?”

“Dad.”

“What?”

“You said you were a father. If you don’t like me calling you Dad, I’ll call you Mom.”

“Have I ever seen a lunatic like this?”

The Emperor had been laughing so hard he was nearly out of breath. With a broad grin still on his face, he spoke.

“Do you know what I was about to say just now?”

“You mean the thing I said I didn’t know?”

“That’s right.”

“Not really.”

“We—no, I…”

The Emperor stared at Taekyung, who was still playing coy, then slowly parted his lips.

“I want to live. More desperately than anyone.”

Jin Taekyung grinned.

“You sound like a person now.”

“But reality hasn’t changed. I didn’t want to make a pitiful spectacle of myself.”

“So, are you crying now?”

“Where did that come from all of a sudden—”

“I cried. Three days ago.”

Despite what he was saying, Taekyung continued in a voice edged with laughter.

“I’m not exaggerating one bit. I bawled my eyes out, with snot running everywhere. I writhed around like a grub and begged the heavens to save me. I told them I still had so much left to do. That there were precious people I absolutely had to see one more time.”

“……!”

“I must’ve looked too pathetic to bear watching. But I wasn’t ashamed of myself.”

He’d fought to stay alive, and survived.

That was how he’d been given a second chance. How he’d ended up here.

“You don’t need to be ashamed, and you don’t need to despair.”

Jin Taekyung held out his hand to the Emperor.

“I’ll save you, one way or another.”

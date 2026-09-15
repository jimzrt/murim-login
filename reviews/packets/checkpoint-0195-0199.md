# Checkpoint Review — 195–199

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

# Chapters 195–199

## Plot

Rumors spread that Jin Taekyung is the Fire King’s Disciple and heir to the Fire Gate Clan. Jeok Cheongang reveals that the Unnamed Sword is actually the Fire Heaven Sword and that his public claim about it being the clan’s sacred treasure was a calculated lie to deter the Zhongnan Sect. He also tells Taekyung that he found no remains at Jeongyang and has finally accepted his grief over Jangcheon.

After Taekyung insults him over the partly burned Flame Divine Palm manual, Jeok beats him severely. While treating Taekyung, Jeok performs an abbreviated cleansing of the sinews and washing of the marrow, discovers Taekyung’s extraordinarily balanced physique, and suspects he may possess the legendary Heavenly Martial Physique. Jin Wikyung confirms that Taekyung advanced from Third Rate to the beginning of the Peak realm in only three months.

At the extended Jin Family banquet, Ak Bulgun of the Shandong Yue Family offers Taekyung special admission to Heaven’s Gate Temple. Jeok interrupts, publicly declares himself the eighteenth Sect Leader of the Fire Gate Clan, accepts Taekyung as his Disciple, and names him heir to the clan’s orthodox lineage. The declaration protects Taekyung but ends his opportunity to attend Heaven’s Gate Temple or take another master. Later, Taekyung confronts Jeok over the decision, and Jeok asks whether he objects to having him as a master.

## Continuity

- The former Unnamed Sword is the Fire Heaven Sword, the beloved weapon of the Fire Gate Clan’s tenth Sect Leader, forged from Ten-Thousand-Year Cold Iron.
- Jeok Cheongang’s claim that the sword was the Fire Gate Clan’s sacred treasure was a deliberate public deception intended to deter the Zhongnan Sect and protect Taekyung and the Jin Family.
- Jeok Cheongang publicly declared himself the eighteenth Sect Leader of the Fire Gate Clan, accepted Jin Taekyung as his Disciple, and named him heir to the clan’s orthodox lineage.
- Jeok said the declaration was meant to ensure that no one would dare approach or harm Taekyung. Whether he will genuinely teach Taekyung remains unresolved.
- Taekyung’s public status as Jeok’s Disciple prevents him from entering Heaven’s Gate Temple or becoming another master’s Disciple.
- Ak Bulgun is a spear Instructor at Heaven’s Gate Temple and a member of the Shandong Yue Family; he had offered Taekyung special admission before Jeok’s declaration.
- Jeok’s abbreviated treatment increased Taekyung’s Muscles and Bones and Sinews and Meridians by 5 each, and Strength, Stamina, and Agility by 1 each.
- Jeok suspects Taekyung possesses the Heavenly Martial Physique, but this is unconfirmed. Only someone who inherits the Fire Gate Clan’s legacy can draw out Fire Heaven Sword’s full power, and Taekyung’s ability to do so is unknown.
- Taekyung remains a Level 73 Peak Master with seventy allocated stat points and only three months of martial-arts training.
- Jang Taebo’s commissioned Ten-Thousand-Year Cold Iron spear is unfinished, and the Treasured Jade remains missing.
- Dark Heaven’s objective, the reason for targeting Shanxi, and the information held by the three surviving remnants remain unresolved. Jin Wikyung suspects the attack was only the beginning.
- The consequences of Woo Hwangtae’s conflict with Chulwoo and the Jin Family, and whether Song Il will honor his pledge after returning to Zhongnan, remain unresolved.
- Lee Seowol and the Mount Heng Sword Sect remain vassals of the Jin Family; Chulwoo remains in love with Seowol.

## Translation Decisions

- Render 화천검 as “Fire Heaven Sword,” replacing the earlier provisional “Unnamed Sword” once its true name is revealed.
- Render 열화문 as “Fire Gate Clan,” 적통 as “orthodox lineage,” 천무지체 as “Heavenly Martial Physique,” and 천무학관 as “Heaven’s Gate Temple.”
- Preserve the distinction between Jeok’s deliberate public lie about the “Fire Gate Clan’s sacred treasure” and the sword’s actual identity.
- Treat Jeok’s public acceptance of Taekyung as binding from Chapter 199 onward, while preserving the unresolved question of whether he will genuinely train him.
- Retain “cleansing the sinews and washing the marrow” for the constitution-improving treatment.

## Durable state

{
  "active_continuity": [
    "Jeok Cheongang publicly declared himself the eighteenth Sect Leader of the Fire Gate Clan, accepted Jin Taekyung as his Disciple, and declared that Taekyung would inherit the clan's orthodox lineage.",
    "Jeok's declaration ended Taekyung's opportunity to enter Heaven's Gate Temple or become another master's Disciple.",
    "Jeok said he made the declaration because no one would dare approach his Disciple, extending his protection of Taekyung and the Jin Family.",
    "In private, Jeok asked whether Taekyung objected to him being his master; whether he genuinely intends to teach Taekyung remains unresolved.",
    "The Unnamed Sword's true name is Fire Heaven Sword, the beloved sword of the Fire Gate Clan's tenth Sect Leader and a weapon forged from Ten-Thousand-Year Cold Iron.",
    "Only someone who inherits the Fire Gate Clan's legacy can draw out Fire Heaven Sword's true power; whether Taekyung can do so remains unknown.",
    "Three Dark Heaven remnants survived interrogation under powerful restrictions and are being kept alive as the Jin Family's physical evidence.",
    "Jin Wikyung suspects Dark Heaven's attack on Shanxi Province was only the beginning and considers the Jin Family's victory suspiciously easy.",
    "Lee Seowol and the Mount Heng Sword Sect swore loyalty to the Jin Family of Taiyuan on New Year's Day, and the Jin Family accepted the sect as its vassal.",
    "Chulwoo is twenty-five, intensely in love with Lee Seowol, and lost his challenge to Taekyung after seeing him interact with Seowol.",
    "Taekyung is a Level 73 Peak Master with seventy allocated stat points and completed the duel Quest and Jin Family tournament event.",
    "Taekyung has three months of martial-arts training, having advanced from Third Rate to the beginning of the Peak realm during that period.",
    "Jang Taebo agreed to forge Taekyung's Ten-Thousand-Year Cold Iron into a spear, but the work is not complete.",
    "The Treasured Jade remains missing, and Woo Hwangtae's conflict with Chulwoo and the Jin Family remains unresolved.",
    "Jeok Cheongang severely beat Taekyung over the partly burned Flame Divine Palm manual, then performed abbreviated cleansing treatment that increased Taekyung's Muscles and Bones and Sinews and Meridians by 5 each and Strength, Stamina, and Agility by 1 each.",
    "Jeok Cheongang suspects Taekyung may possess the Heavenly Martial Physique, but this has not been confirmed.",
    "Ak Bulgun of the Shandong Yue Family is a spear Instructor at Heaven's Gate Temple and personally taught Jin Mukyung there.",
    "Jeok Cheongang and Taekyung publicly presented themselves as an affectionate master and Disciple at the banquet despite Taekyung's private distress."
  ],
  "continuity_sources": [
    199,
    198
  ],
  "open_questions": [
    "What is Dark Heaven ultimately seeking, why was Shanxi Province targeted, and what can be learned from the three surviving remnants?",
    "Will Jeok Cheongang genuinely teach Taekyung and maintain the master-and-Disciple relationship he publicly declared?",
    "When will Jang Taebo complete Taekyung's commissioned weapon?",
    "Who has the Treasured Jade, or was it lost by Jopil?",
    "What consequences will follow Woo Hwangtae's conflict with Chulwoo and the Jin Family?",
    "Will Song Il honor his pledge after returning to Zhongnan, and what consequences will follow his confrontation with the Jin Family?",
    "Can Taekyung inherit the Fire Gate Clan's legacy and draw out Fire Heaven Sword's true power?"
  ],
  "safe_through": 199,
  "temporary_decisions": [
    "Render 화왕 as “Fire King” and 화염신장 as “Flame Divine Palm.”",
    "Render 만년한철 as “Ten-Thousand-Year Cold Iron,” 이름 없는 검 as “Unnamed Sword,” and 화천검 as “Fire Heaven Sword.”",
    "Render 열화문의 신물 as “Fire Gate Clan’s sacred treasure”; preserve Jeok Cheongang’s deliberate public lie in Chapter 195.",
    "Render 암천 as “Dark Heaven,” 전음 as “Sound Transmission,” 육합전성 as “Six-Harmonies Voice Transmission,” and 천하삼십육검 as “Heavenly River Thirty-Six Swords.”",
    "Render 대연무장 as “Grand Training Ground” and 종남산 as “Mount Zhongnan.”",
    "Render 주모 as “Lady of the House,” 권기 as “Fist Qi,” and 화산제일의 기재 as “Huashan’s greatest prodigy.”",
    "Render 사자후 as “lion’s roar,” 봉문 as “seal its gates,” 피독지환 as “Poison-Averting Ring,” 철혈도 as “Iron Blood Saber,” 양천상회 as “Yangcheon Merchant Association,” and 마이클 천강 as “Michael Cheongang.”",
    "Render 적통 as “orthodox lineage,” and treat Taekyung’s status as Jeok Cheongang’s Disciple as publicly confirmed from Chapter 199 onward."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 195

# Chapter 195

The banquet held on New Year’s Day had been such a resounding success that calling it merely a success felt insufficient.

By embracing the Mount Heng Sword Sect, Jin Wikyung had made a bold move that won the loyalty of dozens of mid- and small-sized sects. The Zhongnan Sect’s intervention and the appearance of Fire King Jeok Cheongang, whom everyone had believed dead, had left them all stunned.

And…

*I was one of the people left stunned, too.*

I ate, drank, and moved from place to place. Wherever I went, people’s eyes followed my every movement.

Half a day ago, those gazes had meant interest in the Sleeping Dragon of Shanxi.

But not anymore.

*The Fire King’s Disciple. The Fire Gate Clan’s heir.*

Those words were drifting through the crowd everywhere I went. People were endlessly discussing what it meant that Jeok Cheongang, the current Sect Leader of the Fire Gate Clan, had entrusted me with the sect’s sacred treasure—and why he had protected the Jin Family of Taiyuan even while making an enemy of the Zhongnan Sect.

*It feels like this has already become half-confirmed as fact.*

To be honest, I didn’t understand Jeok Cheongang’s intentions either.

That was why I was here.

And now, while everyone was distracted, I had slipped away. This was my chance.

“Phew.”

I took a deep breath.

I was standing in front of the pavilion where Jeok Cheongang had been given lodging. No one—not even a mouse—was anywhere near the large pavilion. Someone must have issued orders to keep the area clear.

“Great Hero Jeok. Are you there?”

A reply came from beyond the door.

“I’m sleeping.”

“I came because there’s something I wanted to ask you.”

“I said I’m sleeping.”

“…How are you answering me if you’re asleep?”

“I’m sleepwalking.”

Was that an answer or a whinny?

It made no sense, but if the Fire King said that was how it was, then that was how it was. I pulled myself together and spoke again.

“Um, there’s something I’ve been wondering about no matter how much I think it over.”

“Am I someone who solves your problems for you?”

“No, but…”

“If you know that, go wash your feet and get some sleep.”

Talk about an impenetrable wall.

But I couldn’t back down now.

I was cautiously creeping toward the firmly closed door when—

“Take one more step, and you won’t live to see tomorrow’s sunrise.”

“…How did you know?”

“To this old man, your presence is no different from the sound of thunder.”

“Please don’t be like that. Couldn’t you let me in now? It’s still winter, so it’s rather chilly outside.”

“Should this old man warm you up with the Flame Divine Palm?”

“…”

Just hearing that made my insides feel hot.

When I fell silent, silence descended once more. After a while, Jeok Cheongang broke it with a single sentence.

“I went to Jeongyang.”

“Ah.”

Even an insignificant bead could hold special meaning for someone. Jeongyang was like that.

Of the dozens of counties and towns in Shanxi Province, Jeongyang was nothing special. But Jeok Cheongang had had a reason to visit a mountain path somewhere there.

*Jopil.*

On that day, when the sky had poured down snow, a man who had lived as Jangcheon died under the name Jopil.

“I stayed for a long time at the place you told me about. Some passersby saw an old man wandering around the foot of the mountain and asked why I was there.”

His subdued voice continued.

“I told them that a blood relative had died right there. That I had come because I wanted to recover whatever remained of his body.”

“…”

“That was when I realized something. Even if I had met that boy before you did, I could never have killed him. I would have let him go again—and regretted it.”

It was difficult to imagine what expression Jeok Cheongang wore on the other side of the door.

After hesitating, I asked:

“Did you find the body?”

“Nothing was left.”

Several months had already passed.

He had spent his entire life walking a path of blood. The subordinates who might have recovered his body had died with him, too. He had either been buried by the capricious weather or become food for hungry beasts.

“It’s an old man’s greed. Ugly and pointless.”

Glug.

The sound of liquor filling a cup rang unusually loudly.

“I thought you said you were drunk earlier.”

“You crafty brat. Why ask when you already know?”

The candlelight filling the pavilion cast his silhouette across the walls.

Jeok Cheongang let out a quiet laugh, then tipped back his cup.

“Ahh. Good.”

His voice sounded refreshed, as though a single drink had washed away his troubles.

It occurred to me that Jeok Cheongang had gone to the place where Jopil died to shake off the regret and lingering attachment that still held him there.

I spoke in a deliberately brighter voice.

“I was taught that good things should be shared.”

“I was taught from a young age that anyone who coveted other people’s things should be burned with the Flame Divine Palm.”

“What terrifying person taught you that?”

“My Master.”

That’s the Volcano Gate Clan for you. Ruthless.

They burned everyone with the Flame Divine Palm.

I didn’t know the history of the Fire Gate Clan or the names of its past Sect Leaders, but looking at Jeok Cheongang, I could make a rough guess.

*An old sect of thugs.*

They say beans grow where beans are planted, and red beans where red beans are planted.

The disciple takes after the master. Jopil was the exception, of course.

*Anyway, that isn’t why I came here.*

I was watching the silhouette inside the pavilion while trying to read the situation when Jeok Cheongang suddenly spoke.

“From now on, the Fire Heaven Sword is yours.”

“Fire… what?”

“The Fire Heaven Sword. The sword I entrusted to you.”

I had learned the true name of the Unnamed Sword, but that wasn’t the issue right now. I was so shocked that I even stammered.

“B-but this is the Fire Gate Clan’s sacred treasure.”

“Ah. The sacred treasure.”

Jeok Cheongang tilted back yet another cup of liquor and continued.

“That was a lie.”

“What?”

“It isn’t a sacred treasure. About a hundred years ago, one of our sect’s Sect Leaders used it. Later generations inherited it from him. It’s old, but it was already famous as a divine weapon back then, so it should still be useful.”

“…”

What the hell was he talking about?

I stood there with my mouth hanging open at this shocking truth I had never expected.

“That was all a lie? You’re messing with me, right?”

“Messing with you? Why would I bother with a little pup like you?”

“You said it in front of everyone! ‘I entrusted this boy with the Fire Gate Clan’s sacred treasure!’”

“I did. Because we were in front of everyone.”

Jeok Cheongang continued in a bored voice.

“I had to go that far for people to start talking. ‘That boy must have a deep connection to the Fire King. Since he was entrusted with the sacred treasure, perhaps he is the Fire King’s Disciple. If we provoke the Jin Family of Taiyuan, that terrifying Fire King will step in.’ Rumors like that will spread far and wide.”

“…”

“Do you really think this old man would entrust our sect’s sacred treasure to a young brat like you? Our arts are passed down to only one successor per generation, so there’s no one else who would know. If I say it’s a sacred treasure, then it’s a sacred treasure.”

“…”

“So keep the sword. That way, those Zhongnan bastards won’t dare make a move.”

*Is this a dream?*

As I stood there in shock, a System notification rang in my ears, delivering the final blow.

Ding.

> **System**
>
> Information regarding the Unnamed Sword has been updated.
>
> **Item Window**
>
> **Fire Heaven Sword**
>
> **Type:** Sword  
> **Grade:** Peak  
> **Restriction:** One who has inherited the Fire Gate Clan’s legacy  
> **Description:** The beloved sword once used by the Fire Gate Clan’s tenth Sect Leader. Forged from Ten-Thousand-Year Cold Iron, it is exceptionally sharp and durable. After passing through the hands of countless owners over the course of many years, it changed of its own accord. Only one who has inherited the Fire Gate Clan’s legacy can draw out its true power.
>
> **Effect:** Unknown

The updated information was exactly as Jeok Cheongang had said.

It was the beloved sword of the tenth Sect Leader. No mention of the Fire Gate Clan’s sacred treasure anywhere, no matter how hard I looked.

Even the so-called “true power” hidden within the sword could only be drawn out by someone who had inherited the Fire Gate Clan’s legacy.

In other words, take away the fact that it was made of Ten-Thousand-Year Cold Iron, and the sword was a corpse.

*I really thought it was a sacred treasure. I spent so much time worrying about what I’d do if he said he was going to make me a Disciple…*

As I stared blankly at the holographic window, Jeok Cheongang added as though he were doing me a great favor:

“Think of it as a long-term loan. If this old man forgets about it and dies, you may keep it. Ah, and hand over the Flame Divine Palm manual right now.”

“Damn old man…”

“Gasp.”

I had only meant to think that, but it slipped out of my mouth.

The moment I clapped my mouth shut in alarm, the firmly closed pavilion door exploded outward.

Crack!

A pair of eyes burning with flames glared at me.

“You little pup. What did you just say?”

“I-I-I misspoke.”

“Misspoke? Then this old man will make a little mistake with his hand, too.”

Whoosh!

A palm glowing red-hot. An overwhelming wave of heat.

I turned around without even looking back. In the same instant, I pulled the Flame Divine Palm manual from my Inventory and threw it.

“Gasp! The manual—the Flame Divine Palm manual!”

If he reached out now, the manual would turn to ash.

Jeok Cheongang, startled, hastily pulled back his fist. I took advantage of the opening and ran with all my might.

“I’m sorry! I’m really sorry! Please spare me!”

“You damned bastard! Stop right there!”

His roar rang out thunderously behind me.

* * *

Jeok Cheongang watched Jin Taekyung’s back as he fled as though his tail were on fire and let out a quiet laugh.

The anger that had filled his face only moments ago had vanished without a trace.

“You little fool. No matter how far you run, you’re still in the palm of this old man’s hand.”

If he wanted to catch him, he could do so at any time.

But Jeok Cheongang merely clasped his hands behind his back and turned around.

Jin Taekyung was the man who had killed Jangcheon, the Disciple Jeok Cheongang had cherished like a son.

Yet Jeok Cheongang did not hate him.

If anything, Taekyung was one of the people to whom Jeok Cheongang truly owed an apology.

Everything had begun with a wrong choice he had made ten years ago.

“He called me a damn old man.”

Despite being cursed out by a young pup, Jeok Cheongang did not feel bad.

No—in fact, he felt refreshed.

“That’s right. I am a damn old man. A senile old man, too. Heh heh. Heh heh heh.”

After his Master died, no one had dared criticize or curse Jeok Cheongang to his face.

He was the Fire King. A great martial artist who had written his own legend.

And yet, hearing that one remark from Jin Taekyung made him feel as though something that had been blocked for a long time had suddenly burst open.

“It feels good. So good.”

As people grow older, they become lonelier day by day. Not because they have no one with whom to share their warmth, but because they have no one to lean on.

A person might serve as someone else’s support, but Jeok Cheongang had grown too old to lean on anyone himself.

“To be someone’s support…”

Jeok Cheongang was a rough, sharp thorn tree. He had lived a long life and crossed paths with countless people, but he had never allowed any of them to lean on him.

There had been only one exception.

Jangcheon.

“What about you? Did you ever feel, even for a moment, that this Master was a dependable support?”

As Jeok Cheongang thought of him, his eyes grew clouded. But his chest did not hurt as much as it once had, nor did his eyes grow hot.

The dead had already returned to a handful of earth.

Jeok Cheongang had drunk a bottle of liquor at the place where his Disciple had fallen after spilling his blood, then poured out an entire crockful.

He had wept freely, shedding the tears he had been unable to shed for the past ten years and letting the grief in his heart flow out with them.

“I’m sorry. Today will be the last time I think of you.”

If there was a next time, that belonged to the next life.

He might still think of his dead Disciple from time to time. But those thoughts would no longer be regrets about the past.

They would be memories.

“This is enough. This is how it should be.”

After wandering around the courtyard for a long while, Jeok Cheongang suddenly stopped.

The image of Jangcheon that had been flickering before his eyes vanished, replaced by someone he had never expected to think of.

*Why him?*

Clear-cut features. A confident smile that was somehow irritating.

And the way he cautiously gauged Jeok Cheongang’s mood while still taking all of his sharp remarks in stride.

*Did I get angry without realizing it because he called me a damn old man?*

Jeok Cheongang was frowning when—

Sizzle.

The sound of something burning filled the air, followed by a thin trail of smoke.

Realizing where the sound had come from, he opened his eyes wide.

“The manual!”

The cover of the Flame Divine Palm manual was already half-burned.

Jeok Cheongang let out a furious roar.

“Jin Taekyung! You damned bastard!”
## Chapter artifact 196

# Chapter 196

“W-What happened here?”

A middle-aged merchant—the third generation of his family to run a textile shop in the center of Taiyuan, Shanxi Province—stood with his mouth hanging open.

“T-The silk…”

The bolts of silk that should have filled the shop had vanished without a trace. Various items had been damaged, and the shopkeeper, who should have been busy welcoming customers, lay sprawled on the floor, drenched in sweat.

“Thieves! We’ve been robbed!”

The merchant’s vision went dark, and the strength drained from his legs.

He already operated several textile shops, but Taiyuan was his largest main branch—and the symbolic shop passed down to him from his grandfather.

And someone had robbed that shop. All that silk had been cleaned out!

*I knew things had been going too well.*

For the past four months, the merchant had traveled from province to province, inspecting his stores and closing major contracts.

Yet the main branch he had finally returned to after so long was in complete ruin. He collapsed to the floor, unable to withstand the shock.

That was when—

“Tsk, tsk. This place is a mess, too. Honestly, martial artists…”

The middle-aged man who had been clicking his tongue and looking around the shop widened his eyes when he saw the merchant sitting on the floor.

“Oh? When did you get back? I heard you had a big deal to close this time. You’re back earlier than I expected.”

But the merchant was already half out of his mind and didn’t hear him. Only one word from the middle-aged man’s sentence kept echoing in his ears.

“H-Here, too?”

“Huh?”

The merchant grabbed the middle-aged man by the collar and shook him violently.

“You said it was like this here, too!”

“Y-Yeah, I did. But couldn’t you let go of my collar while we talk?”

“What happened? Mounted bandits? Thieves? Did a war break out and the authorities requisition everything? And what do you mean, martial artists?”

“Ah, let go while we’re talking!”

The middle-aged man finally tore himself free and grumbled as he inspected his clothes.

“Damn it, these are new.”

“If you don’t tell me right now, you’ll die and I’ll die with you.”

“All right. All right.”

“So what happened?”

The middle-aged man’s answer was simple.

“Everything sold.”

“…What?”

“It isn’t gone because thieves broke in. It’s gone because everything sold, my friend. So get a grip.”

The merchant stared blankly at him before finally managing to speak.

“Have you lost your mind? Does that make any sense? Who would buy more than a thousand bolts of silk?”

“Officials from the local government, merchants, martial artists. They all came rushing in and swept everything away.”

“…Why?”

“Why do you think? They all want to make an impression on the Jin Family of Taiyuan.”

“The Jin Family of Taiyuan? The one I know?”

“Of course the Jin Family of Taiyuan. What, did you think I meant the Mount Heng Sword Sect?”

“Why the Mount Heng Sword Sect? Did something happen?”

“…You really haven’t heard?”

“I just got back after four months. I came straight here without even seeing my wife!”

“W-Wait! Calm down, please. I’ll tell you everything.”

Not wanting his new clothes to be ruined, the middle-aged man quickly and concisely explained everything that had happened over the past few months.

Fifteen minutes later, the merchant had heard the entire story, from the war between the Jin Family of Taiyuan and the Mount Heng Sword Sect to the present day. He muttered with a dazed expression:

“That happened?”

“I told you. Shanxi is in an uproar over the Fire King’s appearance. And it isn’t just Shanxi Province. The place is crawling with outsiders who came to meet him.”

The middle-aged man continued with an excited look on his face.

“I’ve been doing business in Taiyuan for over twenty years, but I’ve never seen a boom like this.”

“For all that, the number of people out in the streets doesn’t look any different from usual…”

“Do you think people would still be loitering in the streets when the sun has been high in the sky for hours? They packed up their things ages ago and ran to the Jin Family of Taiyuan.”

“Good heavens. It’s hard to believe.”

“I even sold off all my stock.”

“Already?”

“What are you so surprised about? Compared to you, I’ve done nothing. And I heard this from someone reliable…”

The middle-aged man lowered his voice and whispered:

“The gathering that was originally scheduled to last three days may be extended. The rumors are spreading quickly, and the real big shots are starting to move.”

“The real big shots?”

“I mean the prestigious major sects of the Murim have begun to move. Seok Family Manor, said to be the foremost in the merchant world, and His Highness Prince Shangshan, the City Lord, both went to the Jin Family of Taiyuan early this morning.”

“His Highness Prince Shangshan did, too?”

“That’s why even those sluggish officials have started scrambling. A member of the imperial family is coming, after all. They have to show their faces and demonstrate their sincerity, don’t they?”

“Of course. And they’d better arrive before everyone else.”

“What kind of place is Taiyuan? It may not rival the Central Plains, but it’s unquestionably the greatest commercial city in Shanxi Province. You can buy almost anything here.”

“Local procurement. I see.”

“The more people come looking for something, the faster it’ll disappear. Prices will rise, too.”

The merchant’s eyes flashed. He realized this would not end in a day or two.

The confusion and despair he had felt at first disappeared, replaced by visions of mountains of silver nyang dancing before his eyes.

*This is an opportunity.*

He could become familiar with the faces of people from the Murim, the merchant world, and the authorities. If he played his cards right, he might close a deal of enormous size.

After finishing all his calculations, the merchant spoke to the middle-aged man.

“I stocked several warehouses just in case. I’ll let you have some at a reasonable price, so tell me straight. Who should I go to?”

The middle-aged man, who had just found a chance to make a killing, grinned broadly.

“First, remember three people. The Fire King, Jin Wikyung, the Lesser Family Head of the Jin Family of Taiyuan, and the Sleeping Dragon of Shanxi, Jin Taekyung.”

“…The Fire King and the Lesser Family Head, sure. But why that good-for-nothing Jin Taekyung?”

“Hey now. He’s the Sleeping Dragon of Shanxi now. And he’s destined to become an incredible master who will one day influence the entire world.”

“What are you talking about?”

“Tsk, tsk. How can a merchant be this completely out of touch?”

The middle-aged man enjoyed the merchant’s bewildered expression. Finally, he revealed the fact he had kept from him for this very moment.

“The Fire King took the Sleeping Dragon of Shanxi as his Disciple.”

“What? Is that true?”

“I told you it was. Two days ago, an Elder of the Zhongnan Sect who didn’t know about it caused a scene, then went back after getting thoroughly beaten. The Fire King has already entrusted the Sleeping Dragon with the sect’s sacred treasure.”

“Th-Then…”

“It wouldn’t be wrong to say that half the people going to the Jin Family of Taiyuan right now are trying to make an impression on the Sleeping Dragon of Shanxi rather than the Fire King.”

The Fire King was unquestionably one of the greatest Supreme Peak masters in the world, but he was old—very old—and had no real power base to speak of.

Jin Taekyung was different.

He was only twenty-one, possessed outstanding martial talent, and had the solid backing of the Jin Family of Taiyuan.

*No, wait.*

It was the other way around now. The Jin Family of Taiyuan had gained incredible backing:

The famous Fire King, and Jin Taekyung, who might one day grow into a Supreme Peak master comparable to his teacher.

The merchant’s face flushed with excitement.

“It’s like putting wings on a tiger.”

“So we have to climb on before it flies away.”

It would be an opportunity worth pouring in his entire fortune.

Having finally made up his mind, the merchant opened his mouth.

“I should meet the Sleeping Dragon of Shanxi immediately.”

“Of course you should. But right now, you wouldn’t be able to meet him even if you carried a fortune with you.”

“Why?”

“I don’t know. According to the Jin Family of Taiyuan, he suddenly went into seclusion.”

“Closed-door cultivation? That thing martial artists do? Why would he do that now, of all times?”

The middle-aged man let out a deep sigh.

“Exactly. I hear the Heaven Shaking Sword also locked himself away, talking about enlightenment or something.”

“Good heavens. Isn’t there any way around this?”

“I don’t know. Things have grown too big in too short a time. The Jin Family of Taiyuan is practically bursting at the seams, so it seems they’re being selective about whom they allow in.”

“Didn’t you say you were fairly close with one of the Jin Family’s Squad Leaders? I heard you slipped him a few bribes, too.”

“He’s dead. He died in the last war.”

“Oh dear.”

With big shots from every sphere moving around, it would not be easy for ordinary merchants like them to get involved.

The two of them were putting their heads together and racking their brains when the merchant suddenly spoke.

“I do know someone over there.”

“Oh! Someone you know well?”

“I know him very well. He’s a boy my wife gave birth to.”

The middle-aged man frowned at the merchant’s answer.

They had known each other for a long time, so they knew each other’s family histories inside and out.

“You mean your eldest son?”

“That’s right. That unfilial bastard hasn’t shown his face even once in several years. Judging by the fact that my wife hasn’t said anything, he must still be alive somehow…”

The middle-aged man nodded, his face falling.

“Well, try contacting him while you’re at it. Who knows? He might be doing well for himself as a proper martial artist.”

The merchant let out a derisive laugh.

“The son of a textile merchant, a martial artist? As if. He’s probably waiting hand and foot on someone.”

“If that someone is the Sleeping Dragon of Shanxi, wouldn’t that be a good thing?”

“Regardless, that’s impossible. If it is, then from today onward my family name won’t be Hyuk—it’ll be Gyeon. Gyeon as in dog!”

* * *

“Achoo!”

With the sound of a sneeze, my back suddenly felt cool.

I was lying face-down on the bed with my upper body bare when I quietly opened my mouth.

“Mujin, do you want to die?”

Hyuk Mujin, who had been wiping my back with a cloth soaked in cold water, answered:

“Oh, I’m sorry. My nose suddenly started itching.”

“Do that one more time. It’ll be the last sneeze of your life.”

“…Yes, sir.”

“Good. Keep wiping.”

Swish. Swish.

Every time the cold cloth brushed against my back, a throbbing pain rose up.

That was only natural, considering my entire upper body was covered in dark blue bruises.

*Damn it. I’ve been like this for two days already?*

This had never happened before. Until now, I had recovered from most injuries in no time with sleep mode and by circulating my qi.

I had dumped points into [Muscles and Bones] and [Sinews and Meridians] every time I leveled up. Ordinary blows shouldn’t have been enough to damage them.

But…

*As expected of a Supreme Peak master.*

None of that mattered in front of the Fire King.

He had been quiet for a long time, then suddenly chased after me and beat me senseless. His bare fists—not even the Flame Divine Palm—had made me feel as though my bones were separating from my flesh.

When I came to amid the incredible pain, I was in the Jin Family of Taiyuan’s infirmary. After being moved to my pavilion, I had spent two full days confined to bed.

“That damn old man.”

“Gasp!”

Hyuk Mujin sucked in a breath at my words.

“Captain, are you insane? He’ll really kill you.”

“Let him kill me. What are people outside saying?”

“Officially, we’ve settled on calling it closed-door cultivation. It would be rather bad if rumors spread that the Fire King beat up the Sleeping Dragon of Shanxi.”

“What about my eldest brother?”

“Would the Lesser Family Head have any other choice? After hearing the initial report, he got extremely angry for a moment and went to see Great Hero Jeok, but…”

“He went to see him?”

“He saw that the Flame Divine Palm manual had been burned and apologized several times before leaving.”

“What does he have to apologize for? Did I set the fire? Jeok Cheongang did. Did he really have to beat me this badly over a little singeing?”

“I took a quick look, and it wasn’t just a little singeing. Almost half of the cover bearing the title burned away, so the Flame Divine Palm became just the Flame.”

“…”

“Anyway, I think we should stop talking about this. You may not be afraid, Captain, but my blood runs cold just thinking about it. If Great Hero Jeok suddenly walks in, we’ll both be dead, won’t we?”

“That’s true.”

Hyuk Mujin’s foresight was remarkable. Not long after he finished speaking, the door burst open.

“Gasp!”

“Guh!”

“…You bastards. What was that reaction?”

“N-Nothing.”

The small, elderly man narrowed his eyes and looked at us. Then he snorted.

“Fine. Since it didn’t reach this old man’s ears, I’ll let it go this time.”

Showing an unexpectedly cool side, he jerked his chin toward Hyuk Mujin.

“You, get out. You’re in the way.”

I didn’t know what he intended to do, but I felt like I would be better off if Hyuk Mujin stayed.

Hyuk Mujin responded to my desperate gaze—the gaze of a man who wanted to live a long life.

“Yes, sir. I’ll take my leave. Good luck!”

“Very well.”

*…Son of a bitch.*

As Hyuk Mujin scampered out, anxiety washed over me.

There was something strange about the way Jeok Cheongang was looking at my bare upper body.

“Wh-What is it?”

*Surely not.*

But Jeok Cheongang’s eyes gleamed with an inexplicable heat.

“Take off your pants.”

“Gasp. Wh-What do you mean?”

“Take everything off. Don’t leave behind a single scrap of cloth.”

I desperately covered my chest. My voice trembled with shame and fear.

“B-But there’s someone I like.”

“…What does that have to do with anything?”

*What a Western mindset!*

I was screwed. There was no way out.

As I stood there frozen, Jeok Cheongang shouted:

“Ah, I’m going to cleanse your sinews and wash your marrow, so take off your clothes and lie down already!”

“….”

*You should’ve said so from the start.*
## Chapter artifact 197

# Chapter 197

Cleansing the sinews and washing the marrow.

The term meant shedding one’s hair and cleansing one’s bones and muscles. It was a treatment performed only by prestigious, long-established major sects.

Using internal energy to artificially reshape the bones and muscles and remove the waste accumulated inside the body, it transformed one’s constitution into one suited for learning martial arts.

Cleansing the sinews and washing the marrow had to be performed steadily over multiple sessions. The problem was that its conditions and process were extremely complicated.

After hearing Jeok Cheongang’s explanation, I asked:

“Is it really that complicated?”

Jeok Cheongang nodded.

“You’re artificially changing the body you were born with. Did you really think that would be easy and convenient? If it were, there wouldn’t be anyone in this world who wasn’t a master.”

Fair enough.

An ordinary person had to exercise for months, gritting their teeth, just to carve a six-pack onto their abs.

If you were changing your bones, muscles, and constitution entirely, it went without saying that it would be even more difficult.

“There are three conditions necessary for cleansing the sinews and washing the marrow.”

*He said it was incredibly difficult, but there are only three conditions?*

That thought vanished the instant Jeok Cheongang continued.

“First. An internal-energy master with at least two jiazi of internal energy.”

“…Yikes.”

The difficulty level was brutal right from the start.

Two jiazi amounted to a full one hundred and twenty years. How many people in the world could possibly possess that much internal energy?

There had to be very few—and Jeok Cheongang standing before me was one of them.

He raised two wrinkled fingers.

“Second. Financial resources.”

“Why do you need money?”

“Because you need to obtain elixirs for the recipient to absorb. The practitioner has to guide and circulate the qi filling the recipient’s body. Every sect has a different method, but it would not be an exaggeration to say that it costs a thousand gold.”

“It would be difficult for anyone outside the Nine Sects and One Gang or the Five Great Families.”

“Not merely difficult. Extremely difficult. Was it Baek Museong? That Huashan-something fellow seems to have undergone it.”

This was an investment in the literal sense. The sects selected promising young talents whose futures looked bright and performed the treatment on them.

If Baek Museong was the equivalent of a blue-chip stock, then Huashan would have considered him worth investing in.

“Then what about Cheongpung?”

“Do you think the Sword Saint would have simply watched? He must have gradually refined him from a very young age.”

*Damn it. I’m the only one who didn’t get it.*

I had thought the Jin Family of Taiyuan was at least something like a silver spoon in the Murim. But compared to the diamond-spoon babies who underwent cleansing as casually as double-eyelid surgery, we were nothing.

“What is the third and final condition?”

“Patience.”

“Pardon?”

“Cleansing the sinews and washing the marrow is a technique that changes the bones, muscles, and constitution one was born with. The bones and muscles twist and settle into place again, and that process inevitably comes with tremendous pain.”

“How painful are we talking?”

Jeok Cheongang answered without hesitation:

“Painful enough to kill you.”

“...Painful enough to kill me?”

“People really do die.”

“Gasp.”

“In the Sichuan Tang Clan, they fill a jar with more than a thousand different poisons and then...”

The more Jeok Cheongang continued, the more it felt as though my stomach was shrinking. I swallowed hard and asked:

“T-That’s just how the Sichuan Tang Clan does it, right?”

“Of course. Our sect has a separate secret method.”

“Do you perhaps stack up more than a thousand logs, climb on top, and set them on fire...?”

“...”

“Apparently not. Sorry.”

“What the hell do you think our sect is?”

Jeok Cheongang glared at me with round, bulging eyes before shaking his head.

“Cleansing the sinews and washing the marrow cannot be prepared overnight. Today, this old man will only straighten your bones and muscles with internal energy. Whether you stuff yourself with elixirs afterward is your business.”

“Ah. Okay.”

Come to think of it, Jeok Cheongang had come empty-handed. If he had intended to perform the procedure properly, he would have brought elixirs and all sorts of other necessities.

“Then should I take off my clothes?”

“If you ask me that one more time, I’ll skin you alive.”

I stripped off every piece of clothing I was wearing at the speed of light.

Jeok Cheongang’s gaze traveled over my completely naked body, and his expression grew strange.

“This is...”

“Yes?”

“Ah, never mind. It’s nothing.”

*What was that? Why did the atmosphere suddenly become so ominous?*

As I wondered what was wrong with the old man, I realized something and grinned.

“Come on, now. We’re all friends here. Why are you acting like that?”

“...?”

“Honestly, this size is absolutely not normal. I was shocked myself when I first saw it. Do you know the Amazon? There’s something called a black anaconda there. It’s just—whoosh. Really enormous. Whew.”

“...!”

“I understand that you’re surprised, but you still can’t touch it. Got it?”

Whoosh—whack!

With a short rush of wind, a tightly clenched fist slammed into my temple.

* * *

Ding.

> **System**
>
> Status effect: **Unconsciousness** has been removed.

I came to with the System notification and stared up at a familiar ceiling before muttering:

“Damn, you could’ve just said you wouldn’t touch it. Why hit me?”

*Did he really want to touch it that badly? Was he offended because I rejected him so firmly?*

I rubbed my throbbing temple and sat up. Several System messages I had not yet read were floating before my eyes.

“Huh? It’s over? The cleansing?”

I looked around, but Jeok Cheongang was nowhere to be seen.

It seemed he had finished the treatment in a flash and left while I was unconscious. The messages confirmed it.

> **System**
>
> **Cleansing the Sinews and Washing the Marrow** has been successfully completed.
>
> **Muscles and Bones** and **Sinews and Meridians** have increased by 5 each.
>
> **Strength**, **Stamina**, and **Agility** have increased by 1 each.

“Oh...”

A weak exclamation of admiration escaped me.

It was definitely good. I was certainly better off than before. This was the sort of improvement that normally took one level-up plus steady training to achieve.

But...

“Is that really all?”

*Form is temporary, but class is forever.*

Even if it had been performed as a makeshift procedure without proper preparation, this was still cleansing the sinews and washing the marrow.

I had expected some incredible effect. Instead, I was so disappointed that I was practically bewildered.

“What the hell?”

In Murim novels, these things were practically cheat codes.

Bone Transformation and cleansing the sinews and washing the marrow were practically basic requirements for any protagonist.

Even a sickly weakling could undergo both of those procedures, suddenly turn into a thug, and run rampant through the Murim.

So why was I like this?

“Did he do too cursory a job?”

Just then, the door opened, and Hyuk Mujin cautiously poked his head inside.

“May I come in—gasp.”

As I pulled on the clothes scattered across the floor, I said:

“Just so we’re clear, if you get any strange ideas, I’ll smash your skull. And by skull, I mean your head.”

“Then why are you naked?”

“The old man checked my body.”

“Your body? While you were completely naked?”

“...You’re making that sound strange.”

Hyuk Mujin flinched and hurriedly waved his hands.

“No, that’s not what I meant. Great Hero Jeok’s expression when I ran into him earlier was so strange that I came to see if something had happened.”

“His expression was strange?”

“His face was completely rigid. He looked like someone who had been startled by something, or perhaps someone who was angry.”

“Really?”

“Yes. He looked so frightening that I couldn’t even bring myself to speak to him.”

“Why?”

“How would I know?”

I tilted my head. Had something happened all of a sudden?

* * *

Jeok Cheongang walked along, lost in thought.

The people who recognized him bowed from every direction, but his mind was filled with only one person.

*Jin Taekyung.*

His assessment of the young man had changed several times over the past few days.

From an interesting fellow to an infuriating bastard who had burned his sect’s martial arts manual. And today, when he saw Jin Taekyung’s naked body for the first time, Jeok Cheongang thought:

*What a strange fellow.*

Even at a glance, Jin Taekyung’s bones and muscles were exceptional. It seemed a shame for such a body to waste away in a backwater like this.

But after seeing the body hidden beneath his clothes with his own eyes, Jeok Cheongang realized it was beyond anything he had expected.

*How can a body be this perfectly balanced?*

The human body grew over time, but balance was another matter.

One’s usual posture and even the smallest habits related to clothing, food, and shelter could throw that balance off.

A swordsman who used a sword in his right hand would naturally have more muscle and greater strength in his right arm.

It was as natural as water flowing downhill.

But Jin Taekyung was different.

*...What is this fellow?*

The length and angles of his bones. The shape and form of his muscles.

Every part of him was in perfect balance.

It was as though some omnipotent, unknown being had drawn half of Jin Taekyung on an empty sheet of white paper, folded it in half, and unfolded it again.

*Could he have undergone the treatment steadily since childhood? No. Even cleansing the sinews and washing the marrow couldn’t achieve this.*

In the past, Jeok Cheongang had agonized and conducted extensive research for Jangcheon, whose bones and muscles were lacking. He had eventually found the best possible method and performed the treatment on him.

The result had been successful, but that experience had taught him one thing.

*Even cleansing the sinews and washing the marrow has its limits.*

The words *perfect balance* did not suit the human body.

Even if one spent ten thousand gold instead of a thousand, minute flaws would remain. But Jin Taekyung was different.

Jeok Cheongang had kneaded and touched his unconscious body from head to toe.

He had felt the tough, elastic skin and the strength filling both the surface and the depths of his body. He had circulated his internal energy through Taekyung’s body and confirmed the broad, sturdy Sinews and Meridians within.

And then he had been stunned.

*How can a body like this exist?*

It was perfect. He almost wondered if this was what the legendary Bone Transformation he had only heard about would look like.

Jeok Cheongang had met several Supreme Peak masters in his life, including the peerless master Mae Jonghak, the Sword Saint.

But he could say this without hesitation: Of all the bones and muscles he had seen, Jin Taekyung’s were the finest beneath heaven.

*Could it be...*

Jeok Cheongang, who had been staring blankly for quite some time, trembled at the thought that suddenly flashed through his mind.

The Murim held sayings passed down like legends from the distant past.

The Heavenly Martial Physique, said to be born once every several hundred years—or perhaps once every thousand—through a caprice of Heaven, was one such legend.

*The Heavenly Martial Physique? I must be out of my mind.*

But the more Jeok Cheongang examined Jin Taekyung’s body, the deeper his doubts grew and the more tangled his thoughts became.

It would not be an exaggeration to say that there was nothing about that body that needed correcting.

After completing a formality barely worthy of being called cleansing the sinews and washing the marrow, his worries only deepened.

*If that boy really possesses the Heavenly Martial Physique, what would happen if he learned even greater martial arts than he knows now and absorbed elixirs?*

The thoughts continued, chasing one another, even after he left the pavilion.

And at last, the desire coiled deep in Jeok Cheongang’s heart raised its head.

“What if... I taught that boy?”

The mutter escaped him before he realized it, and Jeok Cheongang was startled.

*A Disciple?*

His only Disciple had betrayed their sect and was no longer of this world.

The wound from that betrayal had not even healed, and he was already thinking of taking another Disciple.

Furthermore, he was over a hundred years old, and his mind had already grown hazy from old age.

*Even if I don’t do it, Mae Jonghak could find a worthy talent and carry on our sect’s legacy.*

He had told no one, but Jeok Cheongang had planned to seek out the Sword Saint Mae Jonghak as soon as he left the Jin Family of Taiyuan.

Mae Jonghak possessed martial arts counted among the strongest in the world and had no selfish ambitions. Jeok Cheongang wanted to entrust the succession of the Fire Gate Clan to him.

*And yet I’m having this absurd thought now? Jeok Cheongang, you stupid bastard. You fool.*

Jeok Cheongang was repeatedly sighing and looking up at the sky when a voice reached him.

“Great Hero Jeok. Are you troubled by something?”

The polite voice belonged to Jin Wikyung, a giant of a man.

Jeok Cheongang, who had been thinking of Jin Taekyung at that very moment, flinched.

“Uh, yes?”

It was already the third day since Jeok Cheongang had begun staying at the Jin Family of Taiyuan. Seeing him behave differently from usual, Jin Wikyung asked cautiously:

“Is there perhaps something making you uncomfortable...?”

“No, no. It’s nothing.”

“Then that is a relief.”

Jeok Cheongang waved a hand while gazing at a distant mountain.

“There’s nothing wrong with this old man. I’m perfectly fine, so go about your business.”

“Um, did you perhaps have something specific to say to me?”

“I said I don’t.”

“Are you certain?”

“I said I am! Don’t worry about it and be on your way.”

“...Great Hero Jeok?”

“Ah, what is it?”

After Jeok Cheongang finally exploded, Jin Wikyung hesitated before speaking.

“Great Hero Jeok, the place where you’re standing is directly in front of my office.”

“...”

“Would you care to have a cup of tea and chat?”

After a brief silence, Jeok Cheongang cleared his throat.

“Ahem. Give me liquor instead of tea.”

Whatever he might have been thinking, Jeok Cheongang’s feet had been telling the truth.
## Chapter artifact 198

# Chapter 198

An awkward atmosphere hung inside the office.

Jin Wikyung and Jeok Cheongang each stole glances at the other while sipping tea and liquor.

*Great Hero Jeok came here in person. What could this be about?*

*Has he been possessed by a ghost? Of all places, why did he have to come here?*

But even silence had its limits.

After emptying several more cups, Jeok Cheongang finally spoke. Since things had turned out this way, he intended to clear up some questions about Jin Taekyung before he left.

“I was on my way back from seeing that fellow.”

“Ah, you mean Taekyung.”

Jin Wikyung understood immediately and carefully gauged his mood.

He had already heard the whole story. Jeok Cheongang had helped the Jin Family of Taiyuan because of the emotional debt he carried toward his dead Disciple.

But he was worried that the anger caused by the martial arts manual incident two days ago might not have faded yet.

“Is this perhaps about the martial arts manual?”

“This old man has already erased that from his memory. No matter how precious a manual is, people are more important, aren’t they?”

“…”

“What is it? What’s with that expression?”

“Oh, it’s nothing.”

*After beating him into a pulp, he’s talking about how people are more important now?*

Jin Wikyung swallowed the words hovering at the tip of his tongue.

“In any event, I thought I might have hit him a little too hard, so I went to treat his body by cleansing the sinews and washing the marrow.”

“C-Cleansing the sinews and washing the marrow? You mean the cleansing I know about?”

Jeok Cheongang nodded at Jin Wikyung’s wide-eyed stare.

“Is there another kind?”

“No, of course not. I was just so surprised.”

“Surprised?”

“How could I not be surprised to hear that someone as extraordinary as Great Hero Jeok performed cleansing the sinews and washing the marrow on my younger brother? This is a great blessing for our family.”

Jeok Cheongang gazed at Jin Wikyung’s delighted face and realized something.

“I see. You might not have known.”

“Pardon?”

You can only see as much as you know. Even Jeok Cheongang, one of the most renowned Supreme Peak masters in the world, had never imagined that Jin Taekyung’s bones and muscles could be that exceptional.

So how could Jin Wikyung have known?

*Perhaps it was fortunate that I found out now.*

Jeok Cheongang clicked his tongue softly before speaking.

“The effect of cleansing the sinews and washing the marrow was minimal.”

“What are you saying? How could cleansing the sinews and washing the marrow have no effect?”

“That isn’t what I mean. It would be more accurate to say that Jin Taekyung doesn’t need it. It’s too early to make a definite judgment, but…”

Jeok Cheongang added in a low voice:

“I think he might possess the Heavenly Martial Physique.”

“!”

For a brief moment, shock flashed across Jin Wikyung’s face.

But then he calmly nodded, prompting Jeok Cheongang to ask:

“You already knew?”

“I didn’t. I only understand it now.”

“Understand what?”

“Taekyung’s astonishingly rapid progress in martial arts. But if he possesses the Heavenly Martial Physique, it can be explained. If it really is that Heavenly Martial Physique.”

“Astonishingly rapid?”

Jeok Cheongang narrowed his brow and continued.

“That fellow has certainly achieved remarkable results for someone his age, but not to that extent. No, when you consider the legends surrounding the Heavenly Martial Physique, his progress actually feels insufficient.”

His voice held absolute certainty.

And for good reason. When Jeok Cheongang had been young, he had been no less talented than Jin Taekyung. If anything, he had been more so.

The Supreme Peak masters who currently dominated the Murim had shown flashes of genius from childhood. Compared to them, Jin Taekyung’s current realm was merely ordinary.

“The Heavenly Martial Physique is exactly what its name says: bones and muscles granted by Heaven. Once every several hundred years—or perhaps once every thousand years—a whim of Heaven causes a god to dwell within the body of a mere human. But the boy now…”

“He’s only at the beginning of the Peak realm.”

“Exactly. But the world is vast, and there are many talented people. Cheongpung alone proves that.”

Everything Jeok Cheongang said was true.

The people sheltered by the Nine Sects and One Gang and the Five Great Families were not the only ones who existed.

There were undoubtedly young talents whose names had not yet reached the Central Plains, as well as people who had buried themselves in the countryside while training in martial arts.

If one scoured the entire world from the very bottom, several Supreme Peak masters approaching the level of the One God, the Three Saints, and the Ten Kings would surely emerge.

“That is why this old man cannot be certain. The boy is certainly exceptional, but… it isn’t enough. Is a legend merely a legend? Perhaps his martial talent is inferior to his physique.”

“How interesting.”

“What is?”

“I thought the opposite.”

Jin Wikyung smiled faintly at Jeok Cheongang’s questioning expression.

“My younger brother’s martial talent is the greatest beneath Heaven. No, you could call it the greatest in all history.”

“W-What did you say?”

Jeok Cheongang barely managed to suppress the curse that nearly escaped his mouth.

Even he, a living legend in all but name, did not dare claim to be the greatest beneath Heaven. And this man was calling his younger brother the greatest in all history?

Yet the confidence and conviction radiating from Jin Wikyung made Jeok Cheongang ask another question.

“What grounds do you have for thinking that?”

Jin Wikyung quietly extended three fingers.

“Three months.”

“…”

“That’s how long Taekyung has been learning martial arts.”

“!”

“It’s also how long it took a Third Rate wastrel who frequented pleasure houses to become a Peak master.”

For an instant, Jeok Cheongang’s vision turned white. Lightning crackled inside his head, and his heart pounded violently.

Three months from Third Rate to Peak. It was absurd. Categorically impossible.

But…

*It’s possible. If he possesses the Heavenly Martial Physique.*

Jeok Cheongang was a Supreme Peak master.

Yet even he—powerful enough to kill a thousand people alone—was merely an old man whose body was withering beneath the force of time.

The Heavenly Martial Physique, on the other hand, was an existence born from Heaven’s choice and whim.

*How could a mere human presume to guess Heaven’s intentions?*

*Is this what lies beyond Heaven?*

Jeok Cheongang slowly rose from his seat and approached the window. When he opened the tightly closed window, he saw an endless blue sky.

As the cold wind rushed inside, he suddenly wondered:

Why had Heaven chosen Jin Taekyung? And why had it caused Taekyung and him to meet?

*Who are you? Is there really someone there?*

No answer came.

Jeok Cheongang stared silently at the drifting scraps of cloud in the clear, tranquil sky for a long while before speaking.

“I think we need more liquor. What do you say?”

Jin Taekyung answered with a smile.

“Great. I was getting sick of tea anyway.”

* * *

The next day, Hyuk Mujin came to deliver some unexpected news.

“They want you to attend the banquet.”

“Me?”

“Who else would they mean?”

I answered without a moment’s hesitation.

“I don’t want to.”

Even if I sat there occupying a seat, I would only grow restless.

People would gawk at me like I was a monkey in a zoo, and my biggest fan, Prince Shangshan, would probably ask me for another autograph.

I’d much rather hole myself up in a pavilion and circulate my qi or ponder martial arts. It would be a hundred times better.

“Just tell them I can’t go.”

“It was the Lesser Family Head’s order.”

“Then that makes things even better. My brother won’t say anything, will he? Besides, people would find it strange if my closed-door training ended after only three days.”

“Just say you gained a little insight. If you say that’s what happened, who’s going to argue?”

“…”

He had a point.

I narrowed my eyes as I watched Hyuk Mujin become more and more logical.

“I’m still a patient.”

“You’ve already recovered. When I saw you this morning, almost all your bruises were gone.”

Just as Hyuk Mujin said, most of the bruises that had covered my upper body had already disappeared.

Seeing that, I supposed cleansing the sinews and washing the marrow really did have some effect.

Of course, from my perspective, gaining more stats would have been far more helpful.

Hyuk Mujin scratched the back of his head as though he had a headache.

“Why don’t you just go?”

“Tell them I’m still in pain. Who’s going to complain if I say I am?”

“Great Hero Jeok.”

“Huh?”

“He says that you should stop trying any tricks because you’ll have recovered by now. Otherwise, he’ll come here himself and drag you away.”

“Damn it. That old man is still at the banquet hall?”

“He drank through the night with the Lesser Family Head and appeared just a moment ago, completely drunk.”

I let out a deep sigh.

Jeok Cheongang had said he would remain at the Jin Family of Taiyuan only until this gathering ended.

According to the original schedule, he should have left yesterday. But the gathering had been extended as more people arrived and heavyweights began appearing, so his stay had naturally been extended as well.

“Shit. Fine, let’s go. Let’s go.”

“Good thinking. If you hadn’t, I would’ve been a dead man.”

I followed Hyuk Mujin, who was grinning foolishly, toward the banquet hall.

It was still packed tighter than a marketplace, but perhaps because they had finally begun controlling the crowds, there were far fewer people than on the first day.

“We had no choice. More and more people kept arriving every day. So many people were eating and drinking all day that, leaving aside the expense, we ran out of room.”

“You should’ve turned more of them away. It still looks like there are a lot of people.”

“If we turn away any more, people will curse us. The ones who remain are, at the very least, heads of small martial arts academies.”

“So you’re making sure their pride stays intact?”

“Something like that. We even gave each person a gift when we sent away the people who had been here on the first day.”

*They’re managing even the grassroots sentiment?*

Whether it was the result of careful calculations that had taken all this into account or simple human kindness, Jin Wikyung was undeniably capable.

He was different from the other martial artists who put their pride and martial arts first. Could he be what you would call a bureaucrat-style martial artist?

If the excellent CEO Jin Wikyung did not exist, the Jin Family of Taiyuan probably would not have risen to its current position.

“Hey, our youngest! My beloved little brother, you’ve come!”

“…”

Yes, he would have been perfect if not for things like this.

His face was bright red from all the liquor he had consumed. Jin Wikyung bellowed from the seat of honor, and laughter erupted from every corner of the hall.

*He really went all out. He really did.*

Jin Wikyung was a Peak master, after all. He could have driven away the drunkenness with internal energy, so the fact that he was this drunk meant he had never intended to do so.

Jeok Cheongang, seated beside him, was in a similar state.

“I called you ages ago. Why are you only coming now?”

“…I came right away.”

“I’d hardly call this coming right away. You dragged your feet after saying you wouldn’t come, then came running as soon as you heard this old man was here.”

“…”

“No matter how far you run, you’re still in the palm of my hand. Stop spouting nonsense and sit down.”

As expected of that terrifyingly perceptive old man.

I exchanged nods with several familiar faces, including Baek Museong and Lee Seowol, then cautiously made my way forward.

The instant I sat beside Jeok Cheongang, a bowl-sized liquor cup suddenly appeared in front of me.

“Drink.”

“Oh. Yes.”

I filled the cup to the brim and downed it in one gulp. As I wiped my mouth with my sleeve, Jeok Cheongang thrust the liquor bottle toward me again.

“One more.”

“Yes.”

Another one-shot.

“More.”

“…Again?”

“What did you say?”

“No. The liquor just tastes so good, that’s all.”

*Something about this feels off.*

In the end, I emptied an entire liquor jar by myself before even a quarter of an hour had passed. Only then did Jeok Cheongang pull up the corners of his mouth in satisfaction.

“That’s more like it. You need to drink at least this much.”

“…”

Why was I suddenly thinking of a story I had once seen online about a university freshman welcome party?

The difference was that the person forcing me to drink wasn’t some senior from a fossilized class year.

It was the Fire King.

*This is brutal right from the start.*

Still, I had made it past one hurdle.

I was catching my breath while Jeok Cheongang, thoroughly drunk, went to relieve himself when someone suddenly spoke to me.

“May I pour you a drink?”

The person who had addressed me was a solidly built, middle-aged man.

He had stern eyes and tightly pressed lips. He looked at me with an unreadable expression before continuing:

“I’m Ak Bulgun of the Shandong Yue Family.”

The Shandong Yue Family? I had heard that name several times, both in novels and after coming to the Murim.

I gave him an awkward bow.

“Ah, I’m—”

“I already know. Jin Taekyung, the Sleeping Dragon of Shanxi. Though when I heard about you from the cadets last year, you didn’t have that nickname yet.”

“…Cadets?”

What was this man talking about?

Seeing my bewilderment, Ak Bulgun smiled faintly.

“Have you heard of Heaven’s Gate Temple? I serve as a spear Instructor there.”

“Oh.”

“I don’t know if you’re aware, but your second brother is fairly famous within the academy. Naturally, stories about you have made their way to us as well.”

I let out a quiet laugh.

Until three months ago, I had been called the disgrace of my family. I didn’t need to hear the stories to know exactly what they had been.

“They probably weren’t very flattering.”

“Rumors in the martial world aren’t worth believing. You yourself are proof of that.”

“Who knows?”

I answered vaguely and drank the liquor he poured for me.

“But what brings you here?”

“I came to take care of some business, but then I received a message from the academy. A cadet who said he was going to visit his family for a short while has stopped responding, so they told me to bring him back.”

“Jin Mukyung—I mean, my second brother.”

“That’s right. I hear he’s in closed-door training?”

When I nodded, Ak Bulgun stroked his beard.

“That’s troublesome. He’ll have to leave within seven days at the latest, no matter what. Did he give you any indication before entering seclusion?”

“No. He’s the sort of person who won’t stop until he’s satisfied with his progress.”

“I know. I’ve taught him myself.”

He let out a small sigh before suddenly speaking again.

“What about you?”

“Me?”

“Why not become a cadet at Heaven’s Gate Temple while you’re at it? Ah, if the rumor that you’re studying under the Fire King is true, pretend you never heard me.”

Heaven’s Gate Temple, out of nowhere. I hadn’t expected this.

Heaven’s Gate Temple was practically a gateway to advancement—a place filled with the finest talents in the world whose abilities had been recognized, excellent Instructors, and countless opportunities.

I had heard that, if you met certain conditions, you could even learn advanced martial arts like Jin Mukyung.

*If I stay at the Jin Family of Taiyuan as I am now, my growth will eventually hit a ceiling.*

The Roaring Fury Swordsman’s incident had taught me that much. Even if you obtained something, you would have no choice but to suffer if you lacked the strength to protect it.

I needed a turning point if I wanted to become stronger than I was now, and Heaven’s Gate Temple was a place where both safety and opportunity were guaranteed.

*Unless I’m really the Fire King’s Disciple, this is definitely the best option available to me right now.*

When I failed to answer immediately, Ak Bulgun spoke.

“The admission period has already passed, but I can grant you special permission.”

“Special permission?”

“You’re an exceptional talent.”

Ak Bulgun’s rough palm came to rest on my shoulder.

“What do you say? Become a cadet at Heaven’s Gate Temple. If it’s you, the higher-ups will welcome you with open arms.”

“I…”

Just as I opened my mouth, a voice cut through the air.

“Take your hand off.”

“!”

Along with a burst of scorching heat came alcohol fumes so overpowering that my vision swam.

And there was not a trace of drunkenness in Jeok Cheongang’s voice.

“I said take your hand off what’s mine.”
## Chapter artifact 199

# Chapter 199

“Take your hand off what’s mine.”

At Jeok Cheongang’s single sentence, the air grew heavy. The next moment, Ak Bulgun’s hand slowly dropped from my shoulder.

“Great Hero Jeok. I merely…”

A sharp voice cut off whatever he was about to say.

“Who taught you the habit of touching what belongs to someone else?”

What did he mean, *belongs to someone else*?

Treating a person like an object was one thing, but why was I the object in question? It wasn’t as though I was Jeok Cheongang’s Disciple or grandson.

I had been standing there considering Heaven’s Gate Temple as an excellent option, and I hadn’t expected him to throw chili powder all over it like this.

*Why is this old man suddenly acting like this?*

Unlike me, who was completely flustered, Ak Bulgun remained calm.

“I apologize for disturbing your mood, but I merely wished to give Young Hero Jin an opportunity.”

“An opportunity? Give me a break. It sounds good on the surface, but aren’t you ultimately trying to spirit this fellow away behind my back? Did you think this old man wouldn’t see through your filthy intentions?”

“Spirit him away? Certainly not.”

“Then?”

Even beneath Jeok Cheongang’s round, bulging eyes, Ak Bulgun continued without wavering.

“I came here not as a member of the Shandong Yue Family, but as an Instructor of Heaven’s Gate Temple. How could I allow personal feelings to influence the delivery of an order from the higher-ups?”

“Then those so-called higher-ups gave such an order without even knowing what kind of relationship this fellow and I have?”

“If I may be so bold, could I ask exactly what kind of relationship you have?”

“What?”

Jeok Cheongang glared at Ak Bulgun with a stiff expression.

“This old man entrusted that boy with our sect’s sacred treasure.”

“I’m well aware. I’ve heard enough about it.”

“You must know what that means. Are you mocking this old man?”

“How could I ever dare harbor such an intention? However…”

Ak Bulgun looked back and forth between Jeok Cheongang and me.

“You do not appear to be in a master-and-Disciple relationship at all, so I merely conveyed their intentions with caution.”

“…”

“…”

We both flinched at the same time.

Well, I didn’t know how warm and affectionate a normal master-and-Disciple relationship was supposed to be, but at the very least, someone like me probably wouldn’t address his master as “Great Hero.”

Besides, Jeok Cheongang’s attitude toward me had been no different.

*Look at how sharp he is.*

We had been far too careless. When I glanced to the side, Jeok Cheongang was biting his lips as well. Seeing our reaction, Ak Bulgun’s gaze deepened.

“You hesitated after hearing the offer, Young Hero Jin. If you were truly Great Hero Jeok’s Disciple, you would have rejected it without a second thought.”

Everything he said was true from beginning to end, leaving me unable to refute him.

Who in their right mind would enter Heaven’s Gate Temple after becoming the Disciple of the Fire King, one of the greatest Supreme Peak masters beneath Heaven?

That would be like picking up a pretty pebble when there was gold right in front of you.

*It looks like everything’s going to come out anyway.*

The three of us were not the only people seated at the table of honor. Everyone was looking elsewhere, but their ears were perked up.

If today’s conversation spread, it was obvious that my sturdy shield of being known as the Fire King’s Disciple would disappear. And after that?

*Every bastard under the sun will come crawling out.*

Until recently, the Jin Family of Taiyuan had been little more than a skeleton with no flesh on its bones.

But things were different now. We had put on a fair amount of flesh, and wolves would soon begin prowling around us.

They would watch one another carefully, then pounce the moment the time was right.

The Fire King was already over a hundred years old. His death would be the starting signal for those bastards to sink their teeth into us.

*The first to come running will obviously be the Zhongnan Sect.*

I had to grow stronger before that happened. To do so, Heaven’s Gate Temple was a hundred times better than a title like the Fire King’s Disciple—a mere illusion that would disappear before long.

*All right. I’m going to Heaven’s Gate Temple.*

Once I had made up my mind, I opened my mouth toward Ak Bulgun.

“Actually, I…”

I have no relationship with Great Hero Jeok here. We just happen to share a slight connection. I really want to enter Heaven’s Gate Temple, so would someone like me qualify for a scholarship? Or maybe the Shanxi Province rural-area special-admissions track? And so on.

But the words that had been about to pour out like a waterfall were blocked by a single sentence from Jeok Cheongang.

“He is my Disciple.”

“Great Hero Jeok and I have no relationship at all… Pardon?”

What the hell was he talking about?

I whipped my head around and stared at Jeok Cheongang.

*What did he just say?*

Ignoring my bewildered gaze, Jeok Cheongang continued in an unconcerned voice.

“I intended to keep him hidden away until he was ready, but it seems that will no longer be possible. Everyone appears to have plenty to say on the subject, so I might as well drive the point home once and for all.”

“No, wait a moment.”

The voice I had barely managed to dredge up was swallowed by Jeok Cheongang’s shout, charged with internal energy.

“I proclaim this to the Murim beneath Heaven!”

A terrifying wave of energy shook the ground and pressed down over the Jin Family of Taiyuan’s grounds. Every other sound vanished, and hundreds of pairs of eyes turned toward us.

It had happened before I even had a chance to stop it.

Veins bulged on Jeok Cheongang’s liver-spotted neck.

“Jeok Cheongang, the eighteenth Sect Leader of the Fire Gate Clan, hereby accepts Jin Taekyung of the Jin Family of Taiyuan as his Disciple and shall have him inherit our sect’s orthodox lineage!”

A brief silence followed. Then those who understood his words let out tremendous exclamations and cheers.

It was the moment when everyone’s half-believed suspicions became fact—and an old man’s perfect bullshit became reality.

And I…

“I have committed a grave discourtesy. I apologize to you as well, Young Hero Jin. I’ll convey everything properly to Heaven’s Gate Temple. No one will dare lay a hand on Great Hero Jeok’s Disciple, so the Temple Master will surely give up on the matter.”

Every path that would let me enter Heaven’s Gate Temple—or become someone else’s Disciple—had been slammed shut.

Ak Bulgun looked at my devastated expression and let out a hearty laugh.

“Look at you, my friend. Why such a face on a day this wonderful?”

“…”

Because I knew perfectly well there wasn’t even a one-percent chance that Jeok Cheongang would truly take me as his Disciple.

Having gained nothing while only seeing my future blocked off, I trembled with my fists clenched.

*Damn this old man.*

A bleak future was already playing out before my eyes. He wouldn’t teach me a single martial art, would torment me endlessly, beat me up, and make me run all sorts of errands.

At best, I would become an Inventory for storing his belongings.

*I’m screwed.*

Congratulations poured in from every corner of the table of honor, but I couldn’t hear a single word.

Jeok Cheongang spread his arms wide toward me with a fake smile.

“Come here and let this master give you a hug. Dis. ci. ple.”

“…”

“Oh, look at this rascal. Getting shy in front of everyone. Ho ho ho.”

Jeok Cheongang laughed heartily, then secretly crooked one finger.

At that moment, an unprecedented force I couldn’t resist seized my ankle.

One step. Two steps.

Regardless of my will, my feet began moving toward him.

*…Is this Seizing an Object Through Empty Space?*

Was this for real?

In the end, the small old man pulled me into a tight embrace and moved his lips.

“C’mon, smile.”

“…Yes.”

“Put your arm around my shoulders. Pull the corners of your mouth up to your ears.”

*Fuck it. I don’t know anymore. Let the chips fall where they may.*

We put our arms around each other’s shoulders and smiled brightly like an affectionate master and Disciple.

Instead of camera flashes, tremendous cheers rained down around us, and that day, Prince Shangshan Zhu Bao received a hyper-rare, limited-edition autograph reading:

**Fire King & Sleeping Dragon of Shanxi.**

* * *

Deep in the night, beneath a heavy blanket of darkness.

Behind a wall on the Jin Family of Taiyuan’s grounds where no one seemed to be around, I opened my mouth.

“Why are you doing this to me?”

The small silhouette did not answer.

“Protecting the Jin Family of Taiyuan? Fine, I’ll grant you that. I’m grateful that you drove those Zhongnan bastards away, too. But!”

“…”

“You’re blocking my future! Things have gotten so out of hand that I can’t even enter Heaven’s Gate Temple anymore, and I can’t take anyone else as my master either! Do you know why?”

The small figure, Jeok Cheongang, answered while drinking straight from a liquor bottle.

“Because no matter how foolhardy someone is, they won’t approach this old man’s Disciple.”

“Yes! Exactly! Great Hero Jeok, you’ve completely blocked off every path ahead of me!”

“I see.”

“That’s not the point! You’re more than smart enough to know better, so why are you doing this? I have to make a living, too!”

*Glug. Glug. Buuuurp.*

After draining the bottle to the last drop, Jeok Cheongang let out a tremendous belch and looked at me intently.

“You’re a fellow who knows better, so why are you acting this way?”

“Pardon?”

The liquor bottle in his hand suddenly slammed into the wall.

*Whoosh—BOOM!*

Ordinarily, the bottle should have shattered into pieces with a sharp crash.

But the thing that broke apart with a deafening roar was the wall.

The round liquor bottle was already rippling with tangible internal energy.

“Have you forgotten who this old man is? Why, you little—are you trying to die?”

“Gasp!”

“Even a full prostration wouldn’t be enough, and you dare raise your voice? You wet-behind-the-ears little bastard, I ought to…”

“W-Wait! F-Fix yourself! Fix yourself!”

“Fix myself? Do you want to be fixed in a grave until your bones turn to dust?”

“…”

I had briefly forgotten.

The old man before me looked like the big boss of a nursing home, but he was actually a notorious thug in the Murim.

And when I remembered that his shakedowns took lives rather than money, the blood in my entire body seemed to turn cold.

*I really shouldn’t have touched a nerve.*

It was already dark because it was night, but now even my vision had gone black.

Just then, Jeok Cheongang, who had been staring at me intently, suddenly spoke.

“Do you hate it that much?”

“Pardon?”

“Is taking this old man as your master really that unbearable?”

“…”

What the hell was he talking about when he had no intention of making me his Disciple?

I had a lot I wanted to say, but keeping quiet was clearly the better way to extend my lifespan.

However, Jeok Cheongang wasn’t going to leave me alone while I kept my mouth shut and avoided his gaze.

“Tell me.”

“W-What?”

“You look like you have a great deal on your mind. Tell this old man what you’re thinking.”

“I don’t have anything like that.”

“You don’t?”

*BOOM!*

The last remaining section of the wall crumbled into dust and scattered.

I stared blankly at the sight, then hurriedly opened my mouth.

“On second thought, I do.”

“You just said you didn’t.”

“I didn’t, but now I do.”

“Fine. Tell me.”

I had blurted it out in a panic, but now that I actually had to speak, my heart shrank. I fidgeted with my fingers and cleared my throat.

“But it’s a little…”

“Speak frankly. I want an honest answer without a single lie.”

“Really?”

“No matter what you say, I won’t touch a hair on your head. I swear it by the gods of Heaven and Earth.”

“You don’t believe in things like the gods of Heaven and Earth.”

“…”

“…”

I must have hit the nail on the head.

Jeok Cheongang glared at me with a terrifying expression before finally forcing the words out.

“I do as of today. I don’t know what damned bastard is up there in the heavens, but I’ve seen something with my own eyes, so I have no choice but to believe.”

“…?”

I didn’t know what he claimed to have seen, but he sounded sincere.

Only after making him stake the honor of his sect and even his own name did I cautiously open my mouth.

“First of all, your personality is kind of…”

“Kind of?”

“Isn’t it pretty nasty?”

“…”

“And it’s very nasty, actually.”

His expression was incredulous, but the liquor bottle in his hand remained still. Taking courage from that, I continued.

“And your hands aren’t much better.”

“…”

“You remember what happened a few days ago, right? I know I was partly at fault, but is it really reasonable to throw a Flame Divine Palm at me without warning?”

“…Continue.”

“I’m not opposed to a certain amount of discipline, but that means a flick on the forehead or a few strokes with a switch. What kind of Disciple wants to train by getting hit with a Flame Divine Palm? That isn’t a loving beating. It’s a deadly beating. A deadly beating. If you take it wrong, it kills you, I’m telling you.”

Once I started, everything came pouring out like a burst floodgate.

Starting with my first meeting with Jeok Cheongang and continuing through everything that had happened since, one complaint after another spilled from my mouth.

The more I spoke, the stiffer Jeok Cheongang’s face became.

*Still, this is pretty cathartic.*

A quarter of an hour later, after I had finished my storm of a confession, Jeok Cheongang asked in a subdued voice:

“Are you finished?”

“There’s one important thing left.”

“That… phew.”

Contrary to my expectation that the liquor bottle would come flying, Jeok Cheongang merely let out several deep sighs.

“Tell me.”

“My biggest complaint is what I mentioned earlier. Why on earth did you make it official that I’m your Disciple when you aren’t even going to teach me martial arts?”

“Is that the problem?”

“Of course it is! If I’m going to teach myself, entering Heaven’s Gate Temple would be a hundred times better.”

“Learning from this old man is a thousand times better than Heaven’s Gate Temple.”

“…”

As if I didn’t know that.

I stared at him in disbelief when a thought suddenly crossed my mind.

“Great Hero Jeok, could it be…”

Jeok Cheongang replied bluntly.

“What?”

“Never mind. I just had a ridiculous thought.”

“Tell me.”

“No, it’s pointless. Let’s just move on.”

“Tell me, unless you want to die.”

Oh. Then I had to tell him. If I didn’t want to die, I absolutely had to tell him.

I let out a dry laugh and opened my mouth.

“I wondered if perhaps you were thinking of taking me as a real Disciple, or something like that. It was nonsense, so you don’t need to answer. Hahaha.”

“…”

“Hahaha.”

“…”

“Great Hero Jeok?”

Jeok Cheongang remained silent for a long while despite my calling him, then tossed out a single sentence.

“Would that be a problem?”

“What would?”

“I asked if there was something wrong with this old man being your master.”

“…Pardon?”

*What the hell was this atmosphere?*

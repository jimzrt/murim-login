# Checkpoint Review — 985–989

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

# Chapters 985–989

## Plot

Back in Taiyuan after the memorial at Eight Spring Gorge, the Jin Family is recognized as one of the Five Great Families following the Murong Family’s fall. Jin Taekyung receives System rewards and is hailed as a possible new young king, but remains uneasy about Dark Heaven’s unshown strength and the purpose behind its failed schemes. Jeok Cheongang summons him to meet someone: the dying Thunderbolt Saber King, who asks Taekyung to inherit his remaining internal energy.

Taekyung accepts the dangerous transfer. He absorbs the Heavenly Power Demon’s energy and the Thunderbolt Saber King’s lightning, uniting his three currents of energy. As he advances through Five Qi Returning to Origin and Supreme Peak into Bone Transformation, Peng Cheolhu dies after spending his remaining strength to steady Taekyung. Before losing consciousness, Taekyung hears an unidentified voice say, “A wise choice. Just like back then.”

News of Peng’s death reaches Mae Jonghak. Seeing the age’s unusual concentration of Bone Transformation, Dark Heaven’s rise, and worldwide shifts in weather and heavenly patterns, Mae warns Song Ho to remain vigilant. Song orders the Inner Hall summoned, the Outer Hall put on alert, and messenger eagles sent to the provinces. Mae expects Taekyung and Cheongpung to become central figures in the upheaval.

## Continuity

- The Jin Family of Taiyuan has joined the Five Great Families; the Murong Family has fallen.
- The Thunderbolt Saber King and Peng Cheolhu are dead. Taekyung successfully inherited their remaining power through Transmitting Internal Energy Across the Body.
- Taekyung reached Five Qi Returning to Origin and Supreme Peak and underwent Bone Transformation. He lost consciousness afterward; his condition is not yet known.
- An unidentified voice addressed Taekyung during the transfer and alluded to a previous occasion.
- Dark Heaven’s full strength and the purpose of its repeated failed schemes remain unexplained.
- Unprecedented early-autumn snowfall and rapidly changing heavenly patterns are occurring worldwide. Mae suspects an unknown power may be behind the upheaval.
- Mae sees supernatural forces and grotesque monsters gathering around the Lord of Heaven. Song Ho has ordered the Inner Hall summoned, the Outer Hall placed on alert, and messenger eagles dispatched.
- Mae expects Jin Taekyung and Cheongpung to become key figures in the strange age.

## Translation Decisions

- Use “Transmitting Internal Energy Across the Body” for 격체전공 and “Upper Dantian” for 상단전.
- Render 뇌반업 as “Prison of Karma.”
- Keep “Jeok hyung” and “younger brother” as Jeok Cheongang and Peng Cheolhu’s affectionate forms of address, not literal kinship.
- Render 적서 as “red missive” and 적서에 적힌 이름 as “the name written in that red letter.”

## Durable state

{
  "active_continuity": [
    "Peng Cheolhu died after successfully passing everything he had to Jin Taekyung through Transmitting Internal Energy Across the Body.",
    "Jin Taekyung underwent Bone Transformation after the transfer.",
    "Mae Jonghak regards the age as anomalous, with Dark Heaven, supernatural forces, grotesque monsters, and the Lord of Heaven at the center of growing danger.",
    "Unprecedented snowfall and rapidly changing heavenly patterns are occurring across the world.",
    "Song Ho ordered the Inner Hall officers summoned, the Outer Hall placed on alert, and messenger eagles dispatched."
  ],
  "continuity_sources": [
    989
  ],
  "open_questions": [
    "What is behind the worldwide weather and heavenly-pattern changes?",
    "Is the upheaval a scheme laid by some unknown power, as Mae Jonghak suspects?",
    "What are Dark Heaven and the Lord of Heaven planning?"
  ],
  "safe_through": 989,
  "temporary_decisions": [],
  "version": 1
}

## Reading copies

## Chapter artifact 985

# Chapter 985

Leaving behind the tears of countless people and the ceaseless shower of falling petals, tens of thousands of people—martial artists and ordinary folk mixed together—departed Eight Spring Gorge and returned to their respective places.

The memorial for the departed, and the belated Double Ninth Festival, had come to an end. But those who remained had to keep moving forward, toward tomorrow and the day after.

And waiting for us when we returned to the Jin Family of Taiyuan were more than just the few family members who had stayed behind in case of an emergency.

“My name is Hwang. I serve, though inadequately, as a Hall Master of the Murim Alliance. I’ve come to deliver a message from the Alliance Leader.”

When the Murim Alliance’s envoy introduced himself with impeccable courtesy and added those words, everyone’s gaze turned toward the three of us brothers.

More precisely, they focused on Jin Wikyung.

“I see.”

His voice was calm, though the corners of his eyes were still red.

As if welcoming a guest he had been waiting for a long time, Jin Wikyung led the Murim Alliance’s envoy with a composed air.

“Before we talk, please come inside and rest from your journey.”

“I’m deeply grateful for the consideration you’ve shown me, Great Hero Jin.”

In that moment, an unmistakable emotion passed over the faces of the Jin Family of Taiyuan’s senior members and the Sect Leaders under its protection.

And it wasn’t only because the envoy bowed so deeply, with genuine respect and reverence.

*Great Hero.*

Just two words, but they meant something special.

This wasn’t some nobody, one of those self-important fools forever puffing each other up. A renowned master of the martial world, entrusted with the important position of Hall Master in the Murim Alliance, had come as an envoy and addressed him that way.

*Everything is changing.*

I, too, felt the weight of it all over again.

Jin Wikyung was no longer the Young Hero or Lesser Family Head who had led a fading family in place of a father whose whereabouts were unknown.

He was the ruler of Shanxi Province, and another Alliance Leader recognized by everyone in this land.

No, now he was…

“What are you thinking about so hard?”

At Hyuk Mujin’s sudden question in my ear, I shook my head.

“Nothing.”

“Doesn’t look like nothing.”

“Mujin.”

“Yes?”

“Want me to make your life a living hell?”

“…No. I was just going to tell you to hurry up and follow them. You were standing there by yourself.”

Hyuk Mujin was right.

Behind Jin Wikyung, who strode forward with confidence, came the Murim Alliance’s envoy, the family’s senior members, and the Sect Leaders under the Jin Family of Taiyuan, including Lee Seowol.

Their faces held a mixture of grief that had not yet faded and joy over something soon to become reality.

But after silently watching them from behind, I turned and headed in another direction.

“Huh? Where are you going?”

“No idea. Wherever I feel like.”

“What do you mean? Maybe someone else could miss it, but you of all people shouldn’t, Captain.”

“Doesn’t matter. I more or less know what they’re going to say anyway.”

“What?”

I heard Hyuk Mujin’s bewildered pause, then the sound of him hurrying after me. I let out a quiet laugh.

At the same time, a memory came to me.

Eight Spring Gorge.

The narrow gorge that had swallowed so many lives, and the clear chime that rang out amid the shower of falling petals.

The holographic window that had announced yet another change.

*Ding. Ding-ding.*

> **System**
>
> Since the world first began, nothing beneath the heavens has been eternal. The vast land and sea, the countless lives that dwell within them, and even the mighty power held by the rarest few are no exception.
>
> No flower stays red for ten days (*花無十日紅*), and no matter how great one’s power, it does not last ten years (*權不十年*).
>
> But when a tree’s roots run deep, its branches grow thick (*根深枝茂*). When a spring runs deep, its waters flow far (*源遠流長*). At last, it will become another world where many can dwell and find rest.

As the System had told me, the Jin Family of Taiyuan, once rotting like an ancient tree, had now become a forest.

It bore fruit at the ends of countless branches and created a lake as vast as the sea.

Though they might lack strength, everyone I had seen and known among them had always been just and righteous.

Unlike those who had chosen the wrong path, seized by anger and greed.

> **System**
>
> The Murong Family has fallen. They are no longer one of the Five Great Families.
>
> At long last, the fame of the Jin Family of Taiyuan resounds throughout the world!
>
> The fame and power of the Jin Family of Taiyuan have risen to that of a member of the Five Great Families!

The Nine Sects and One Gang. The Five Great Families.

Fifteen pillars that had upheld the martial world for hundreds of years.

And now, the Jin Family of Taiyuan had become one of those mighty pillars.

It wasn’t simply because the Murim Alliance had appointed them, or because renowned masters from across the martial world had strongly urged it.

The whole world had accepted it. They had recognized the Jin Family’s courage in standing against an army of tens of thousands.

They had recognized its sense of justice in seeking to protect not just Murim, but this land and its people.

And so, the provincial martial family that had once been slowly fading, its glory behind it, had become stronger than ever by uniting as one.

> **System**
>
> The Title Scion of a Great Family has been removed!
>
> You have acquired a new Title: Direct Descendant of a Prestigious Family!
>
> As your family’s standing has risen, you have gained a tremendous amount of Fame!
>
> Hidden Quest Might As Well Go All the Way to the Five Great Families successfully completed!
>
> You have earned the very rare Achievement Dad, Where Are You? Glory and blessings to the three Jin Family brothers, who overcame countless hardships and trials through their own efforts!
>
> Jin Wikyung and Jin Mukyung have been granted the effects of Amazing Natural Healing and various bonus buffs. It goes without saying that these effects will not be displayed to the individuals in question.
>
> You have acquired 10 bonus stat points as an Achievement reward!
>
> You have gained a tremendous amount of EXP!
>
> Level Up!
>
> You have gained a tremendous amount of Fame!
>
> Your name and reputation have now reached beyond Murim and across the world. You are a feudal lord appointed by the Son of Heaven, a successor of the Fire King Jeok Cheongang, and a great martial artist in your own right.
>
> Your footsteps have been inscribed in history.
>
> Martial artists have begun to speak cautiously of the glorious Title granted to only ten martial artists beneath the vast sky and its three stars. They speak of the birth of a new young king.
>
> Nothing has been decided yet. Just as the small flap of a butterfly’s wings can bring a typhoon from afar, each of your choices, big or small, will gradually change this world.
>
> But remember: time keeps moving.
>
> May you have good fortune in Murim.

The System window, far longer than usual and full of more changes than ever, ended as always with a wish for good fortune in Murim.

For the first time in a long while, there was no follow-up Quest.

And yet that was the only thing that left me uneasy, even in the peace that had finally arrived.

*What is this? I was sure something else was going to happen.*

It had been a long time since I’d cared about getting stronger just for the sake of it.

In the Quests that came one after another, someone’s death had been so inevitable that it might as well have been written into the bargain. And the burden I carried had grown just as heavy.

On top of that, the greatest crisis Murim had ever faced was hanging over the entire martial world.

*They’re not the type to back off just because this plan failed.*

It had always been like that.

Dark Heaven had carried out numerous schemes across Murim. Since murdering the Dharma King Hong Dao and stealing Shaolin Temple’s divine artifact, the Green Jade Buddha Staff, they hadn’t made a move anyone could call a success.

And yet, in Sichuan. In Hubei.

Then Nanman, the Imperial Palace, and now even here in Shanxi Province, they had brought one blood-soaked disaster after another.

*The Murong Family’s betrayal and the nomads’ invasion were certainly huge events. But the forces Dark Heaven has revealed in the process are still far below what I expected.*

Other than the four Demon Lords and the Demon Empress, who were certainly key figures within Dark Heaven, more than half the enemies we had fought so far had been traitors and underlings.

In other words, it was as if they had recruited their forces locally.

*And they still haven’t shown themselves. Why? And why keep up this string of costly battles that lead only to failure?*

My steps had carried me onward without my noticing, but I stopped and frowned.

Then another memory came to me: part of a conversation with Murong Baek, Family Head of the Murong Family, who had met his end as the North Heaven Demon Lord.



*“If that’s what you believe, fine. There’s nothing wrong with continuing to hope.”*

*“What?”*

*“Now that I’m in this situation, I find myself wondering why the Western Heaven Demon Lord, the Southern Heaven Demon Empress, and the Eastern Heaven Demon Lord failed. How did a plan prepared so carefully for so long fall apart in an instant?”*



We never found out what those incomprehensible words meant.

The North Heaven Demon Lord died without ever explaining them.

But even after I drove the spearhead into his heart, and even now, days after all the fighting had finally ended, I remembered every detail of that moment clearly.

His voice and expression had been utterly calm.

The North Heaven Demon Lord had been ready to die. He had proved it moments later by drawing on even his innate qi.

*He wasn’t just saying it to shake my composure.*

I know how honest a person can become when standing before an inevitable death.

When someone stands at the end of their life by their own choice, they don’t speak lies.

*Then why? Why say that at all?*

Of course, there were hints in the North Heaven Demon Lord’s words and demeanor.

I just hadn’t thought much about them, because the idea seemed so utterly unrealistic.

*It was as if he thought this situation had been fated from the beginning—or as if he, too, had been used…*

No matter how I looked at it, it made no sense.

After the fierce battle ended, I’d shared my thoughts with Jeok Cheongang. He answered more firmly than ever.



*“Fate, my ass. And as much as those bastards deserve to die, you think masters that powerful grow on trees?”*

*“Yeah. Something does seem off, doesn’t it?”*

*“Lord of Heaven. No matter how powerful that bastard is, he can’t use men like them as disposable pawns. Not unless they’ve had their heads cracked open a couple of times by my Flame-Extinguishing Divine Fist.”*



He was right.

There wasn’t a madman anywhere in the world who would use Supreme Peak masters as pawns.

The Bow Saint hadn’t agreed or disagreed. She’d only made an inscrutable face, but whatever she might have said probably wouldn’t have differed much from Jeok Cheongang’s answer.

*No. Then why say it at all? What’s with this suspiciously quiet stretch of time?*

I screwed up my face and thought it over.

Had he just been spouting nonsense before he died? Or had his words carried some other meaning none of us, myself included, could guess?

As I clung to that endless chain of thoughts, a familiar voice suddenly broke in.

“No wonder you never came, even after I waited all that time. So this is where you were.”

Jeok Cheongang.

His expression was heavier than ever. His voice was low and subdued as he continued.

“Come with me. There’s someone who wants to see you.”
## Chapter artifact 986

# Chapter 986

Truth be told, I’d had a pretty good idea from the start.

The heaviness in Jeok Cheongang’s expression and voice, so unlike his usual self.

And the grief carried in his low, subdued voice was something the giant known as the Fire King rarely let show.

But…

As always, a bad feeling never misses.

“You’ve arrived.”

The first person to greet us was the Medicine King Hall Master, who had been standing guard at the door.

As the man gathered his bundle and left the moment we arrived, Jeok Cheongang spoke to him in a quiet voice.

“As I asked, please don’t tell anyone.”

“…”

“Thank you. You’re an excellent physician.”

The Medicine King Hall Master bowed his head slightly without a word and left. Only then could we face the man waiting inside.

“Oh, you brought him back sooner than I expected. That old man’s legs are so short, I figured it’d take another seven days and nights.”

Another giant had come to his senses after several days.

I silently watched the Thunderbolt Saber King laugh heartily at his own lighthearted joke. Only when Jeok Cheongang gave my shoulder a nudge did I belatedly clasp my hands in a salute.

I gave him the utmost respect I could.

“I am Jin Taekyung, an insignificant martial artist of Murim. It’s an honor to meet you, Great Hero Peng.”

“Don’t bother. Excessive humility can be a poison in its own right. If you’re an insignificant martial artist, does that mean every other one beneath Heaven is dead?”

The Thunderbolt Saber King smiled at me with satisfaction, then turned his gaze to Jeok Cheongang.

“Now that I see him, you were whining for nothing. You kept complaining that he ran wild like a reckless brat, with no respect for his elders, more and more as the days went by.”

“Friend, my ass. You’ve got a lot of nerve talking to someone so much older than you like that.”

Jeok Cheongang managed to answer in his usual gruff tone, but the weight in his eyes was impossible to hide.

Whether he noticed Jeok Cheongang’s state or not, the Thunderbolt Saber King laughed even louder.

“Wahaha! What are you so sore about? We’re both getting old.”

“Don’t you know the Three Bonds and Five Relationships? Never heard of respect for elders?”

“If knowing that meant someone else would feed me, maybe. Or would it make my martial arts stronger?”

“Forget it. I’m the fool for having this conversation with an ignorant Peng.”

“Admitting your own shortcomings. I like it. I was just getting tired of talking to a stinky old man, so this works out nicely. Don’t you agree?”

At the Thunderbolt Saber King’s tossed-off question, I nodded.

“Well, my Master is a little old.”

“What did you say? Hahaha!”

His laugh burst out, loud enough to shake the room.

It didn’t suit the Thunderbolt Saber King’s pallid complexion at all. It sounded so loud, it was almost as if he’d forced it out.

*No. That’s probably exactly what he did.*

I murmured silently to myself.

What you could see with your eyes wasn’t everything. I could feel it.

Even now, the energy within the Thunderbolt Saber King was wavering precariously, like a glass vessel cracked all over.

Like a flame that could go out at any moment.

“I heard you wanted to see me.”

At my heavy-voiced remark, the Thunderbolt Saber King seemed to realize I’d noticed his condition. He spoke, still smiling.

“You’re a perceptive one. You’re worlds apart from the last time I saw you. The Fire King may not be good at much else, but he’s certainly raised his Disciple well.”

“…”

“There’s no need to look so miserable. For martial artists like us, life and death are just part of the deal.”

He was right.

That was the life of a martial artist.

And the Thunderbolt Saber King had spent his life making his way through a mountain of sabers and a forest of swords, beset by countless threats and schemes. He accepted the reality of his situation with calm composure.

“I had a very long dream. I was able to look back on my whole life in it. I even got to see my friend Murong Baek as a young man again, for the first time in ages.”

“Friend, my ass. That bastard deserved to die.”

At Jeok Cheongang’s casual remark, the Thunderbolt Saber King let out a quiet laugh and continued.

“That’s all in the past. It couldn’t be helped. You can’t put spilled water back where it was. But in the end, we stopped Dark Heaven’s plot and saved more people. That’s enough for me.”

He was famous for having a temper as fiery as Jeok Cheongang’s. But he looked at me with eyes as still as a pond.

“When I first saw you at the Star-Array Grand Banquet, I had a feeling you’d accomplish great things before long. Everyone could tell you’d become a pillar capable of protecting the world, together with the Sword Saint’s Disciple.”

Of course, I’d been inexperienced back then.

I hadn’t stood shoulder to shoulder with all those powerful masters like I did now, and I’d been brutally defeated by a monster called the Blood Lord.

“But nobody could have guessed you’d grow this much, this quickly.”

The threats to my life had come one after another, each one growing more dangerous, and I’d grown at a staggering pace as a result.

Enough to make even those who’d watched me from the closest distance question their own eyes.

“That’s why I asked for you right away. It’s also my last chance to make the best use of the time and energy I have left.”

“…You mean…”

“They say an ordinary tiger leaves its hide behind when it dies. But the great tiger of Hebei will leave something else.”

At the Thunderbolt Saber King’s faint smile, I finally understood why he’d sought me out first, rather than his own flesh and blood, after barely regaining consciousness—and with death right before him.

“Take it. Everything I have left.”

At the very moment the Thunderbolt Saber King’s calm voice rang through the room—

*Ding.*

> **System**
>
> An emergency Quest, **Transmitting Internal Energy Across the Body**, has been created.
>
> **!!Warning, warning!!**
>
> The process of completing this Quest carries an extreme risk.
>
> Do you accept the emergency Quest?
>
> Y / N

I stared silently at the Thunderbolt Saber King’s smiling face through the holographic window that had appeared with a clear chime.

Then, all at once, I spoke.

“Why… Why did you choose me?”

The answer came without the slightest hesitation.

“Because I believe in you.”

“…!”

“That belief isn’t mine alone. The Dharma King believes in you. Your Master believes in you. Now, the whole world believes in you.”

I could hardly breathe.

My chest tightened, and it felt as if my blood were surging through my veins.

Amid it all, the Thunderbolt Saber King’s voice rang clearly in my ears.

“This is all for the world, not for you. Do you need any other reason?”

“No.”

I took a small, steadying breath and continued.

“That’s reason enough.”

A smile crossed the Thunderbolt Saber King’s pallid face.

“Sit in the lotus position.”

*Ding.*

> **System**
>
> You have accepted the emergency Quest, **Transmitting Internal Energy Across the Body**!

* * *

Internal energy was an intangible force that existed everywhere in the world.

Those who practiced martial arts accumulated it within their bodies, strengthening their bodies and minds. They repeated grueling training in hopes of stepping beyond human limits and into the realm of the superhuman.

But not everyone wanted that kind of power.

The greater the energy accumulated within the body, the greater the backlash it could unleash.

If someone tried to circulate their internal energy recklessly by following an incorrect formula, they were likely to end up crippled. And without enlightenment, many fell into a heart demon and became half-mad.

Even so, the desire of martial artists to reach ever greater realms rarely faded.

A world ruled by the law of the jungle.

They came up with all kinds of ideas to grow stronger, faster and more safely. In the process, they discovered one astonishing method.

*What if, instead of spending years accumulating internal energy, you inherited it all from someone else?*

*Inherit the power of an old master on the verge of death? Huh? Isn’t that basically rock honey?*

In the distant past, Transmitting Internal Energy Across the Body was born that way.

And from the moment it was born, it became a taboo that must never be put into practice.

The reason was simple.

It only looked sweet on the surface. In truth, it was a double-edged sword.

No—it was so much worse that calling it a double-edged sword was laughable. The failures far outnumbered the successes.

“Master!”

“No!”

They died, and died, and died again.

Even those who survived through sheer luck would end up crippled, their qi and blood snarled together, or lose their original martial prowess forever. In the process, they lost Supreme Peak masters who had dominated their era and gifted young prodigies.

So when the Thunderbolt Saber King told Jin Taekyung he intended to transmit his internal energy to him, Jeok Cheongang could only ask in disbelief:

*“Have you gone mad?”*

*“Not at all.”*

*“No, you’re definitely mad. Normally, you’d be flying into a rage by now.”*

*“I may have been awake for only half a shichen, but my mind has never been clearer. I can’t remember ever being this sharp in my life.”*

*“Well, that’s a hell of a thing to celebrate. So does that mean you can finally finish the Thousand Character Classic?”*

*“Cut the nonsense. You know this isn’t just a mad idea.”*

In truth, the Thunderbolt Saber King was right.

Jeok Cheongang had only answered that way on reflex at first. In his heart, he was already weighing the chances of this insane undertaking.

*“I hate to admit it, but your precious Disciple could withstand Transmitting Internal Energy Across the Body. Isn’t he blessed with the Heavenly Martial Physique, along with that child Cheongpung?”*

*“…The Heavenly Martial Physique.”*

*“If that were all, I wouldn’t be having this conversation with you. He has the Muscles and Bones Heaven granted him, as well as enough potential and insight as a martial artist.”*

If this had happened a few months ago, Jeok Cheongang would never have accepted a proposal that put his Disciple’s life at risk, no matter how strongly anyone urged him.

Not even if it came from the Thunderbolt Saber King, a man he’d spent decades trading barbs with and grown fond of despite himself—and who was now on the verge of death.

But Jeok Cheongang was different after Jin Taekyung had told him the truth himself.

*There’s a chance. No—it’s more than enough.*

A transfer of internal energy between two Supreme Peak masters who had reached their realms—a feat with no precedent in the long history of Murim.

And Jin Taekyung, with a superhuman body that could only be called the Heavenly Martial Physique, possessed yet another strange power.

The Prison of Karma.

A divine strength that could purify the body and even heal injuries.

As long as he remained alive, that power gave him a chance.

And besides…

*He’s already succeeded at Transmitting Internal Energy Across the Body once.*

Jeok Cheongang had only heard the story much later.

Jin Taekyung had received the internal energy of the Heavenly Power Demon, a great fiend of the Demonic Cult imprisoned in the Sichuan Tang Clan’s underground prison, then defeated the Western Heaven Demon Lord.

When he first heard it, the shock of learning his Disciple had nearly died had made his heart feel ready to burst. But the difference between that time and now was clear.

The circumstances were different. So was the martial prowess Jin Taekyung had achieved since then.

*He can do it. No…*

He *will* do it.

He had to.

Jeok Cheongang steadied his wavering heart with firm resolve, then watched the two men, joined at the Great Palace acupoint, with a deeply troubled gaze.

*Whoosh.*

Unprecedented internal energy surged out in every direction.
## Chapter artifact 987

# Chapter 987

I still remember every moment of the day I first circulated my qi.

The Qi-Sea Acupoint.

The energy I first encountered inside my body, in the place also known as the lower dantian, was pitiful.

Its name meant “sea of qi,” which felt almost laughable. In that cramped vessel, more like a little stream than a sea, only a handful of murky energy rippled.

That was right.

It had definitely been that way.

But…

Now it was different.

*Ding.*

> **System**
>
> An emergency Quest, **Transmitting Internal Energy Across the Body**, has begun.
>
> **Transmitting Internal Energy Across the Body** carries extreme risks. If anything goes wrong while the internal energy is being transferred and absorbed, it may lead to qi deviation or death.

As the System’s notification gradually faded into the distance, my consciousness sank deep into my body.

The world that spread before my eyes as they opened anew within it was an endless ocean.

*Rooooar.*

It was immeasurable. And hot.

Instead of clear blue waves, waves of fire surged without end.

An ocean of flame, vast beyond measure.

And at its center, a gigantic fire dragon lay coiled atop a reef as black as pitch.

*That’s…*

I knew instinctively the moment I saw it.

In this place, filled with nothing but flames and heat, the reef where the fire dragon had made its home stood out as something especially alien.

*The energy I received from the Heavenly Power Demon.*

How could I forget?

The Heavenly Power Demon, once a great fiend of the Demonic Cult who had shaken the whole world, had passed his internal energy to me and asked me to defeat the Western Heaven Demon Lord.

Though decades of imprisonment and torture had worn him down, leaving him with far less internal energy than his old reputation suggested, perhaps that was why Transmitting Internal Energy Across the Body had succeeded without killing me.

*Put too much power into a vessel, and you break it.*

And the Heavenly Power Demon’s energy, which I’d inherited back then, had remained inside me ever since.

That energy served as the nest of the fire dragon, the very embodiment of Scorching Yang Qi born of the Fire Gate Clan’s martial arts.

It was a fairly harmonious coexistence, even a symbiosis. But in that moment, I instinctively understood.

If I wanted to climb higher, I had to bring this strange relationship between two energies with different roots to an end.

*Wake up.*

The world around me responded to my focused will.

An unseen vibration swept across the ocean of flames. It reached the fire dragon, sleeping peacefully atop the reef at its center.

*Rumble.*

The fire dragon’s massive body trembled. Between its finally lifted eyelids, pale blue eyes appeared—and fixed directly on me.

Slitted vertically, the eyes of a vicious beast.

But the emotion within them wasn’t anger at being woken. It was obedience to its master.

Of course.

The fire dragon and the reef were both, in the end, part of this ocean.

And the master of this vast world deep inside my body was none other than me.

So, the instant our eyes met, that tremendous concentration of Scorching Yang Qi joined with my consciousness.

*Whoosh!*

Warmth and consciousness mingled.

My vision had turned pale blue. One with the fire dragon, I flung out both arms without hesitation.

No—I spread wings as vast as my body and took flight.

*Boom!*

The reef shook as though an earthquake had struck. With a shockwave, I shot into the air and drew a great breath high above.

*Hummm.*

The energy, compressed layer upon layer, screamed.

If it hadn’t been mine, that appalling heat rising from deep inside my body and racing up to my throat would have turned my whole body to ash long ago.

*Now.*

There was no hesitation. With the breath I finally released, pale blue flames burst forth and wrapped around the reef.

Before that hellfire, powerful enough to destroy the world, the pitch-black reef began to lose its shape and melt.

Then it was swept up by the waves of fire surging all around, rising high into the air. Having just breathed out a torrent of hellfire, I opened my mouth toward it.

*Whooosh.*

The moment I swallowed the liquid, its color a dark crimson from the melted reef—

*Gasp…!*

Suddenly, I couldn’t breathe. It was as if invisible blades were savagely carving through my insides.

Before I could feel any satisfaction at the thirst that had finally been quenched, a sharp pain assailed my mind.

But I clenched my teeth.

I steadied my wavering mind and used all my strength to swallow back the energy surging up my throat.

So it could never return to its original form.

So it could melt into me anew.

And for that, my endurance and choice were soon rewarded.

*Rumble.*

I could feel it.

The power swelling inside me.

The reef—or rather, the Heavenly Power Demon’s energy—hadn’t disappeared.

It had been absorbed, and yet in another sense, it was a new kind of coexistence.

Unlike before, when it had been imperfect, now it had melted together into one. A perfect coexistence.

And at the end of this astonishing change, something else was beginning.

*Rrrrrumble!*

The world, all red with flames, flashed.

A massive bolt of lightning split open the closed sky and pierced through the ocean of flames.

*Ah.*

Before I could fully feel the change in my power, a genuine exclamation escaped me.

Yes.

It was lightning, in the truest sense of the word.

The end of a long and fierce life.

The symbol of a giant standing at death’s door, and the final legacy he’d hoped to leave in this world through me.

As that massive bolt of lightning finally entered deep into my body through the Great Palace Acupoint, I moved toward it as if entranced.

I followed it upward and upward, the current joining sea to sky.

*Whooosh!*

I couldn’t hear it. And yet I seemed to hear it.

The sound of the fierce wind.

Everything I felt through the fire dragon’s massive body, which had long since come to feel like my own.

My consciousness raced into the depths, perceiving everything as reality. I had risen so high that the ocean was no longer visible, and at last I saw it.

A gigantic mountain rising like it would pierce the sky.

And I already knew what that mountain was.

*The Middle Dantian.*

The mountain known as the Jade Hall Acupoint glittered like a jewel, just as its name suggested.

There was only one place that didn’t. The very highest peak.

*Why? How come?*

The question surfaced in my mind, but it disappeared as I found the answer myself.

*It means I’m still not ready.*

It had already been quite some time since I opened my Middle Dantian, but even my incredible pace of growth had its limits.

That mountain peak was the realm of enlightenment.

A realm only those with heaven-given talent, blood-soaked effort, and long years behind them could enter.

A lofty height I, too, could hardly aspire to, even after improving at a dazzling pace.

But…

*If not now, when will I ever get another chance to try?*

I’d experienced countless strokes of good fortune, but heavenly fortune never came easily.

And a stroke of heavenly fortune someone had created while prepared to die was an opportunity I’d never see again.

*Let’s go.*

Maybe my hesitation had vanished the moment this all began. The System’s warning no longer mattered.

I’d already swallowed the Heavenly Power Demon’s energy. I already knew what I had to do.

*Crackle. Crackle-crackle!*

A bolt of lightning continued to shine without fading.

I leaped toward its massive pillar of light.

*Rooooar!*

Everything before me turned white. The agony was incomparable to when I absorbed the Heavenly Power Demon’s energy. It squeezed every muscle in my body and vaporized my consciousness.

*Gyaaaah!*

I didn’t know. I didn’t know where I was.

I couldn’t tell whether the desperate scream ringing in my mind was mine or the fire dragon’s.

All I could do, as my consciousness grew hazy, was hear someone’s thunderous shout.

—Hah!

The instant that unmistakably Jeok Cheongang-like shout rang out—

“……!”

My consciousness, sinking fast, awakened.

Strength flowed into my limp, powerless body. Memories of reality, long forgotten, returned.

Who I was. Where I was.

And…

What I had to do for everyone who’d believed in me, a callow, inadequate brat.

*Endure. And keep enduring.*

I bore the unceasing pain tearing through my body with all my strength.

I mustered the Scorching Yang Qi at the fire dragon’s core and the Heavenly Power Demon’s energy I’d just absorbed, down to the last ounce of strength I could summon, and bit into the pillar of lightning.

*Crunch. Crunch.*

Lightning flashed before my eyes. Everything belonging to a giant was contained in that energy. That lightning, holding everything the giant had been, was numbing my mind past the point of pain.

Luckily for me.

*Fuck, it’s not like I’ve never shit blood before.*

At some point, I was laughing like a madman.

I bit into the lightning, swallowed it, and kept going without pause, even as I nearly blacked out from the pain I’d known was coming.

Until the distant flash that had filled my vision slowly dimmed.

And at last, until it vanished completely, as if it had never existed.

*Rumble.*

Suddenly, through my hazy consciousness, I realized:

The massive bolt of lightning that had connected my Middle and Lower Dantians was no longer there.

The thunder I could hear from somewhere was ringing out inside me.

*I did it…*

The moment I faced the truth of Transmitting Internal Energy Across the Body’s success—

*Ding. Ding. Ding-ding-ding!*

From far off in my consciousness, clear chimes began ringing without pause.

But the sound hadn’t come from the ocean of the Lower Dantian, now far in the distance, or from the peak of the Middle Dantian, finally glowing like a brilliant jewel.

I raised my head and saw it.

Clouds the mountain peak couldn’t reach.

Another world, hidden behind those clouds.

*The Upper Dantian.*

I was thirsty. As soon as I achieved my goal, the threadbare strands of my consciousness began to grow clearer.

It was thirst, and it was longing.

*More, more, more…!*

I wanted to grow stronger. I wanted to go farther.

I wanted to pierce through those white clouds, soar above them, and look down on everything.

But I had to force down that burning thirst and longing.

I’d reached my limit.

Any more would be greed.

I already knew what consequences this fleeting impulse would bring.

*Next time. I swear.*

With that vow, I looked down over the mountain and ocean that had become wholly mine.

And for the first time, I faced the essence contained within the three currents of energy, now united, and the vast power they formed together.

No—I became one with it.

*Ah. Ahhh.*

I shuddered and groaned.

I floundered in my distant consciousness.

Enveloped in a dazzling radiance where three lights mingled, I forgot everything around me.

No-self.

As I sank into that endless swamp of consciousness, I heard a voice like a hallucination.

—A wise choice. Just like back then.

A voice that felt unfamiliar, yet strangely familiar, as though I’d heard it somewhere before.

Then the thread of my consciousness snapped.
## Chapter artifact 988

# Chapter 988

At some point, the Thunderbolt Saber King, Peng Cheolhu, began to laugh without a sound.

Even as the several sixty-year cycles’ worth of internal energy he’d accumulated, along with every ounce of strength in his body, melted away and vanished, the clear smile at the corners of his wrinkled mouth remained.

Just like the brilliant halo of light still brightening his view in this very moment.

*Whoooosh.*

The wind howled.

The unprecedented energy seeping into it swelled. Three lights, each with its own color, endlessly drew together and mingled.

And at last, they changed.

*Whoosh!*

In the air that rapidly grew hot enough to boil, the Thunderbolt Saber King saw it clearly.

Three flower buds blossoming in radiant splendor.

No—more precisely, a young man seated cross-legged, slowly rising into the air.

*Yes. I suppose so.*

Though he was watching the realm of the Three Flowers Gather at the Crown, the dream of everyone in Murim, the Thunderbolt Saber King wasn’t surprised in the least.

He’d walked this path himself once. And it was someone else’s present.

The Blazing Flame Divine Dragon, Jin Taekyung.

The heir to the Fire Gate Clan, and the successor to the Fire King, Jeok Cheongang.

The Thunderbolt Saber King knew. And he believed it, too.

For that callow brat, who’d only passed twenty two years ago, the realm of the Three Flowers Gather at the Crown was nothing more than a step on the way to a greater height.

Even now, Jin Taekyung was moving toward the next step.

And the Thunderbolt Saber King’s belief soon became reality.

*Fwoosh.*

The three flower buds suddenly began to burn.

After an intense struggle, the Extreme Yang flames swallowed the pitch-black energy. The moment they completed five rings, the Thunderbolt Saber King let out a quiet laugh.

*Beyond the Three Flowers Gather at the Crown, he’s reached Five Qi Returning to Origin.*

Jin Taekyung probably didn’t know the exact meaning of those five rings.

But the Thunderbolt Saber King did.

No—all the martial artists beneath Heaven knew.

To set foot in the realm of Five Qi Returning to Origin meant one had attained the bare minimum qualifications to be called a king in the vast world of the Nine Provinces.

But the transformation didn’t end there.

*Crackle!*

Flame and lightning intertwined.

The fight between the hellfire that had swallowed the darkness and the lightning was fierce—and desperate.

The force of their struggle made Jin Taekyung’s body, floating in the air, tremble with pain.

A massive shockwave burst from his body and spread in every direction beyond the pavilion.

“*Hah!*”

In that instant, Jeok Cheongang’s sudden shout rang out. The body trembling like a quaking aspen slowly began to settle.

As if to prove the terrible pain he must be feeling, a new emotion appeared on his face, still twisted like a fiend’s.

Will.

It was Will.

A fierce determination to reach beyond this wall, even if it broke him—never to be bent.

When the Thunderbolt Saber King felt Jin Taekyung’s Will, he was finally certain.

*My choice was right.*

A brighter smile than ever bloomed across his face.

Watching the internal energy he’d built up over his whole life, those long years, and the last spark of life he had left melt into the flames, the Thunderbolt Saber King opened his mouth.

His tone was deliberately gruff, completely at odds with how he felt.

“Damn it. I’ve done nothing but good things for the Fire Gate Clan before I go.”

The old master, gazing at his Disciple wrapped in the energy that had finally united within the distant halo of light, answered.

“If you’re so sore about it, you should’ve had more kids. If you’d tried a little harder, maybe the Peng Family would’ve had a brat like him.”

“Would you listen to this senile old man? You took a monster for a Disciple by pure luck, and now you’re saying whatever you please.”

“That’s right. I was lucky.”

“Damn it. Don’t admit it!”

“Why not?”

“If you admit it that easily, I’ve got nothing to say.”

The Fire King, Jeok Cheongang, and the Thunderbolt Saber King, Peng Cheolhu, looked at each other and chuckled.

“Do you remember that?”

“Remember what?”

“Wasn’t it right after the Great Faction War ended? We all got together for a drink to celebrate.”

“Oh, the day you mouthed off to this old man and got a bloody nose?”

The Thunderbolt Saber King frowned.

“Get it straight. We were evenly matched until then.”

“We were. For about thirty exchanges. But you got beaten in the end, didn’t you? This old man was clearly a cut above.”

“...You’re childish to the very end. There’s a reason they say people never change.”

“If a person changes, it means they’re about to die. Anyway, it was my complete victory.”

“You insufferable old bastard. Did you eat all those years through your asshole?”

If this had happened fifty years ago, they’d surely be throwing punches at each other by now.

But the two old men continued to look at each other with smiles on their faces.

One was desperately hiding the bitterness welling up from deep inside.

The other had accepted the years that had long since passed and the death drawing near.

Then Jeok Cheongang gazed at Peng Cheolhu, whose hair had turned completely white, and deliberately scowled.

“You ill-mannered brat. I’ve told you: if you’re going to treat me like an old man, you’d better mind your manners and give me the respect my age deserves.”

“Damn it. There you go talking about age again.”

“I’ve told you hundreds of times by now. Is your skull made of Ten-Thousand-Year Cold Iron? Is that why you can’t remember?”

“Cut the talk I don’t want to hear. Fine, fine, I get it. I’ll show you some respect, all right?”

“Peng Family bastards, honestly… What did you just say?”

Jeok Cheongang stopped mid-sentence, suddenly startled. The Thunderbolt Saber King let out a hearty laugh at his reaction.

“What’s the matter? Have you gotten so old you’ve gone deaf, Jeok hyung?”

“...!”

“Tsk, tsk. What good is it to look young again? You’ve got plenty of years, but nothing to show for them.”

Jeok Cheongang stared silently at him as he clicked his tongue for all to hear. Then he suddenly laughed out loud.

“What are you laughing at?”

“Nothing. I was just thinking that after living so long, a day like this would come. Got a problem with that?”

“I always have a problem with something, but can a younger brother talk back to his hyung?”

Younger brother.

Why did those simple words make something stir in Jeok Cheongang’s chest? He forced the fading smile back onto his lips and spoke.

“You’ve finally come to your senses. I was always wondering how long you’d keep digging in your heels.”

“Now, now. Calling your younger brother ‘you’ and ‘brat’? It seems Jeok hyung still hasn’t come to his senses.”

“Then should I start calling you little brother Peng?”

This time, the Thunderbolt Saber King laughed out loud.

After emptying himself of everything he had, deep creases appeared all over his face, now covered in fine wrinkles and age spots.

“No, it’d be best if you didn’t use that title. Hearing those words from Jeok hyung makes me feel itchy down to my guts.”

“You damnable bastard. What do I have to do to satisfy you?”

“That’s much better. You’ve finally turned back into the Fire King Jeok Cheongang I know.”

Only then did the Thunderbolt Saber King smile with satisfaction. In a gentler tone, he spoke.

“Jeok hyung.”

Jeok Cheongang didn’t answer.

No—he couldn’t.

The sudden change in the Thunderbolt Saber King’s tone and expression, that aged voice now unmistakably an old man’s, became something unseen that lodged in Jeok Cheongang’s throat.

The Thunderbolt Saber King looked at him as if he understood everything and continued.

“You, at least… don’t change, Jeok hyung.”

“...!”

“From now on, just as you have until now, stay in Murim as you are.”

Long years had passed.

The sun and moon kept changing places. The mountains and rivers changed their clothes in turn, and those born into this world with vigorous cries returned to the soil.

But there were also those who didn’t change.

Though their bodies grew old with the passage of time, their hearts remained unshaken and firm.

“Looking back, I’ve been very lucky.”

In the Thunderbolt Saber King’s fading eyes, the years gone by flashed past like meteors.

Born into the Hebei Peng Family, which commanded the region, he’d spent a childhood wanting for nothing.

In his youth, his name had spread beyond the northern lands and across the world.

And then—

“Even in that terrible war, I had friends I could fight back to back with.”

“...Yes. We did. And we still do.”

Jeok Cheongang answered in a dry voice. He quietly bit his lip and was no longer smiling.

“Jeok hyung.”

“Go on. I’m listening.”

“Do you remember what I used to say out of habit?”

Jeok Cheongang nodded without hesitation and answered.

“You used to say that a man should meet death with his head held high on the battlefield.”

“You remembered.”

“How could I forget? You said it several times a day.”

“True. Every time, Jeok hyung threatened to rip my mouth open.”

The Thunderbolt Saber King laughed happily at the old memory. But instead of the thunderous laughter that had once boomed from him, only a faint breath came out.

“I take it back. Now that I’ve come this far… this kind of death isn’t so bad after all.”

The Thunderbolt Saber King forced his head upright when it kept drooping to one side.

He straightened his bent back and fixed his gaze ahead.

Over Jeok Cheongang’s shoulder, at someone floating in the air, engulfed in a deep halo of light.

*Crack. Creak.*

With the sound of flesh tearing, fine tremors spread throughout Jin Taekyung’s body.

In the Thunderbolt Saber King’s eyes, alight with joy, was Jin Taekyung, entering the process of Bone Transformation—a process even he had never experienced.

*Supreme Peak.*

At last, he’d climbed the summit and attained the ultimate. The highest place on earth, and the path closest to Heaven.

“Jeok hyung. Do you see him?”

At the Thunderbolt Saber King’s voice, trembling with emotion, Jeok Cheongang turned to look at his Disciple.

“Yes. I see him. My one and only Disciple—and the successor who has inherited everything you had.”

“Is that so?”

The Thunderbolt Saber King’s eyes, steeped in death, had already lost focus.

Now, he could no longer see Jeok Cheongang’s face or Jin Taekyung’s form.

And yet, in the darkness slowly approaching, he saw a radiant halo of light that would not go out.

“Th-that child…”

The Thunderbolt Saber King gasped for breath.

Clinging to his fading consciousness, he reached toward the thing shining clearly beyond the darkness.

Toward the future he’d left behind, toward hope.

Then he cast off everything pressing down on his body and lunged toward the light.

Toward a new mountain peak that didn’t exist in this world, waiting for him.

Toward another Supreme Peak: death.

*Thud.*

His fingertips fell limply, touching nothing.

Jeok Cheongang quietly closed his eyes. A low voice slipped between his lips.

“Farewell, you Peng bastard.”

He decided to save the words “younger brother” for the day they met again.

That had been his last promise to the Thunderbolt Saber King—or rather, to Peng Cheolhu.

And as the Fire King Jeok Cheongang, rather than Jeok hyung, he still had far too much left to do.

*Whoosh.*

Feeling the halo of light finally begin to fade, Jeok Cheongang opened his eyes.
## Chapter artifact 989

# Chapter 989

The Thousand-Faced Fox, Song Ho, was having another day so busy he couldn’t catch his breath.

Or, more accurately, he was supposed to be.

When he got up after less than two hours of sleep, his day’s schedule had already been neatly laid out in fifteen-minute increments.

But the moment he read the message in the red missive brought by a Hidden Shadow Pavilion agent who had sought him out before sunrise, the Thousand-Faced Fox realized:

Today was not going to go according to plan.

“Cancel the meeting already on the schedule. Instead, summon the Inner Hall’s officers within fifteen minutes.”

“I’ll make sure every one of them is notified.”

“What’s the Outer Hall doing?”

“They’re already on alert. The messenger eagles to be sent to each province are fully prepared and waiting for your orders, Pavilion Master—”

“Send them out at once. In the meantime, I’ll go see the Alliance Leader.”

After giving several more orders, the Thousand-Faced Fox set off briskly toward his destination.

And, as always, Sword Saint Mae Jonghak was waiting for him, seated cross-legged.

“It’s early for bad news. You could’ve waited until sunrise, at least.”

His voice and gaze were as clear as water by a lake.

Faced with the Number One Sword Under Heaven’s calm, which usually made him seem utterly at ease with the world, the Thousand-Faced Fox cautiously spoke.

“Had you already… heard?”

“I can’t say I know. I just found it hard to sleep last night.”

Mae Jonghak slowly opened his eyes and looked at the Thousand-Faced Fox.

Or, more precisely, at the red missive in his hand.

“So. Who is it this time?”

Mae Jonghak’s voice had sunk low.

Though many years had passed and much had changed, some things remained just as they were.

Red letters bearing bad news were one of them.

Whenever an important figure died or there were heavy casualties during the Great Faction War, they would write a red missive with heavy hearts.

Just like the one in the Thousand-Faced Fox’s hand now.

“Alliance Leader.”

“It’s all right. Tell me the name written in that red letter.”

After hesitating for a moment, the Thousand-Faced Fox spoke in a heavy voice.

“The Thunderbolt Saber King, who was staying with the Jin Family of Taiyuan, has finally…”

“Enough. That will do.”

Mae Jonghak waved a hand and muttered with a bitter expression.

“So it came to this, after all.”

“I can only apologize for bringing you such news.”

“You? No. If someone has to be blamed, it should be me—the Alliance Leader.”

The Thousand-Faced Fox bowed his head without a word.

They had spent decades building a bond: as promising young martial artists of the Nine Sects and One Gang and the Five Great Families, and as comrades who joined forces to weather the war.

For now, he had to give Mae Jonghak time to take in the news as the deceased man’s friend, not as the Alliance Leader. Fortunately, the silence didn’t last long.

“How did Senior Peng pass?”

“They say he left smiling to the very end. He knew for himself that he didn’t have much time left, so he passed on everything he had through Transmitting Internal Energy Across the Body.”

The astonishing news left out one crucial detail: to whom.

But Mae Jonghak didn’t bother to ask.

Before the Thousand-Faced Fox could finish answering, one name had already come to mind.

“Jin Taekyung. It must’ve been that boy.”

“Yes. It was an extremely dangerous attempt, but I’m told the technique was completed successfully.”

Mae Jonghak quietly nodded.

Though he’d spent only a short time with Jin Taekyung, he’d had a vague sense that the transfer would succeed.

“That boy could certainly pull it off. You can’t fathom how deep he goes.”

But the Thousand-Faced Fox’s next report drew a hollow laugh from even Mae Jonghak.

“Bone Transformation, you say?”

If the Heavenly Martial Physique was something one was born with, Bone Transformation was the process of completely rebuilding the body after birth, through immense internal energy and enlightenment.

Even a white-haired old man on the verge of death could regain his youth and see a remarkable increase in his martial arts—that was the power of Bone Transformation.

And yet the good fortune everyone dreamed of had been granted to a young man barely past twenty.

Even the Thousand-Faced Fox, who had read the report with his own eyes, looked like he could hardly believe it.

“Is this truly… possible?”

“You don’t seem convinced.”

“I doubt most people would be.”

“Why do you think it’s impossible?”

“In the entire thousand-year history of Murim, how many have experienced Bone Transformation? As far as I know, fewer than twenty.”

“You have a point. But there’s something you’re overlooking.”

“What is it?”

Mae Jonghak spread one hand instead of answering.

“Five.”

“What does that—”

“I mean that of those fewer than twenty, five have already appeared in this age alone.”

“……!”

“No—now there’ll be six.”

The Martial God and the Three Saints.

The Fire King, Jeok Cheongang, and his Disciple, the Blazing Flame Divine Dragon, Jin Taekyung.

As he spoke, Mae Jonghak raised one more finger and continued calmly.

“Isn’t it strange? In the last thousand years, only around twenty people have undergone Bone Transformation, yet six have appeared in the orthodox Murim alone.”

“That’s…”

“You’ve felt it yourself, I’m sure. You just can’t easily accept it out loud.”

Mae Jonghak unfolded his legs and stood.

His appearance and presence were so ordinary he looked like someone you might run into anywhere. But as he gazed at the Thousand-Faced Fox, his eyes were clear as glass.

“We’re living in a truly strange age. The boundaries of common sense collapsed long ago, and a vast, unimaginable shadow has fallen over the world.”

More than fifty years ago, two supreme figures had appeared in the same age: the Martial God and the Heavenly Demon.

And that wasn’t all.

Dozens of Supreme Peak masters from the orthodox, unorthodox, and Demonic factions had gathered around them, and a battle had begun between superhumans wielding unprecedented power.

The Three Saints and the Ten Kings. The great fiends of the Demonic Cult and the unorthodox factions, wielding earth-shaking power.

And…

“Now Dark Heaven has appeared, surpassing even the Demonic Cult of that era by far.”

Does the age make the people, or do the people make the age?

No one had ever found a clear answer to that question, which had prompted countless debates. Sword Saint Mae Jonghak was no exception.

But deep down, he understood that the age he lived in was more than a simple time of chaos.

He sensed something hidden behind the conflict between superhumans—born of a chaotic age, or perhaps bringing one into being.

“The supernatural powers we can’t understand, the grotesque monsters. And the man at their center—the Lord of Heaven.”

With a deepening gaze, Mae Jonghak muttered as if to himself.

“Sometimes I find myself wondering if all this is some sort of scheme, laid out by someone beyond anything we could imagine.”

Mae Jonghak suddenly turned to look out the window.

Snowflakes drifted slowly down, thickly covering the sunlight spreading from the distant east.

Snow in early autumn. A tremendous snowfall, at that.

It was a phenomenon rarely seen in Henan’s warm climate—or rather, one never seen before—that had begun several months ago.

And it wasn’t just Henan. It was happening throughout the world.

The changes weren’t limited to the ground, either.

The sky that had always stretched above them—the heavenly patterns Dharma King Hong Dao had once predicted—was changing at an alarming rate.

“Can you make sense of any of this?”

At Mae Jonghak’s question, the Thousand-Faced Fox, Song Ho, bit his lip without a word.

By now, cold sweat had dampened his back.

“I—I can’t understand it at all. I can’t even begin to guess what’s about to happen.”

His voice trembled.

Even he, who had served the Martial God at close quarters and fought against the hundred thousand under the Heavenly Demon’s command, couldn’t stay calm when he thought of the future ahead.

This was like…

*Something beyond the bounds of the human world.*

The words hovered on the tip of his tongue, but the Thousand-Faced Fox couldn’t bring himself to let them out. He swallowed them instead.

He couldn’t believe it.

No—he didn’t want to believe it.

Mae Jonghak watched the Thousand-Faced Fox’s agitation with clear eyes.

“Chief Song. May I say something to you as your superior and as the Alliance Leader?”

“Please.”

“Admit your fear and accept it.”

“……!”

“Be more afraid than anyone else. Always be on guard against our enemies and distrust them. You and I have no choice. We’re in positions where we have to.”

The Thousand-Faced Fox understood the meaning behind Mae Jonghak’s words at once.

“I’ll take your words to heart, Alliance Leader.”

“Thank you. You’re a coolheaded, intelligent man. One of the most… well, not the best, but certainly among the top ten I’ve known.”

The Thousand-Faced Fox gave a dry chuckle.

“So there are quite a few above me, then.”

“Wouldn’t the ranking have to be accurate? Don’t take it personally.”

“I’ll try not to take that part to heart.”

“That’s good news. Your mind is already busy enough with the work you need to handle right away.”

“Of course. Then I’ll take my leave.”

Mae Jonghak smiled faintly but didn’t stop the Thousand-Faced Fox as he hurried away, just as briskly as he’d arrived.

After reading the red missive he had left behind, Mae Jonghak murmured in a low voice.

“So, in the end, I’m losing someone again.”

Apart from his friendship with the Thunderbolt Saber King, Peng’s death was a tremendous loss to the orthodox Murim as a whole.

Over the long years, half of the Ten Kings had fallen. And now another had been lost from the five who remained.

But perhaps the sorrow of the Thunderbolt Saber King’s death could be eased, if only a little, by the mark left behind by that giant’s final step.

“The Blazing Flame Divine Dragon, Jin Taekyung.”

Mae Jonghak quietly spoke the name that had lingered in his mind.

Though a great star named the Thunderbolt Saber King had fallen, a new star had risen to fill his place.

No—he had already been shining brightly long before this.

Just as his title, Divine Dragon, promised.

*Before long, two dragons will finally ascend to the heavens.*

Mae Jonghak had not the slightest doubt.

Jin Taekyung, who had become a giant of Murim, and the last successor he had raised like his own grandson would become the center of this strange age.

Thinking of Cheongpung, who must by now have finally heard the news from Shanxi Province even where he was so far away, Mae Jonghak poured internal energy into the missive in his hand.

*Fwoosh. Crackle.*

The flames of Samadhi True Fire tinted Mae Jonghak’s clear eyes red.

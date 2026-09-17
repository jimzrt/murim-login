# Checkpoint Review — 305–309

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

# Chapters 305–309

## Plot

Lee Jungryong visits the injured Go Jun and promises to grant him greater strength so he can defeat Jin Taekyung. China offers Ares Guild and the Peace Guild a mercenary contract for the Sichuan Catastrophe at Xiao Yang’s personal insistence. Taekyung accepts fifty trillion won for killing the Lich and travels to China with Team Leader Choi aboard a private Boeing 747-8 VIP jet.

During the flight, Choi explains that rising mana density may be causing the recent increase in Gate accidents and may have caused the Lich’s extraordinary evolution, just as the Skeleton Warlord evolved. Taekyung logs into the Murim after a month away and returns to find Jeok Cheongang unconscious. The Luoyang Strange Physician, accidentally struck by Taekyung’s vase, diagnoses a progressive blockage of Jeok’s qi acupoints and gives Taekyung a porcelain clue pointing to the Divine Physician in Sichuan. The System creates the Supreme Peak Quest **Find Mr. Shin in Sichuan**, which will fail if Jeok dies.

Taekyung decides to carry Jeok to Sichuan and search for the Divine Physician. Mae Jonghak arranges letters to the Sichuan Tang Clan, Emei, and Qingcheng, while Hyuk Mujin, Cheongpung, and Gung Gibang join the search party. Taekyung forces rapid travel with a Ten-Thousand-Year Cold Iron chain and ninety years of internal energy. Meanwhile, the exhausted Yongbong Escort Bureau caravan, led by twenty-one-year-old Ju Hwaran, reaches Black Stone Mountain, where Heavenly Axe and hundreds of Green Forest bandits from Black Stone Stronghold demand to inspect its goods and collect a toll.

## Continuity

- China has requested Ares Guild and Peace Guild participation in the Sichuan Catastrophe; Xiao Yang personally required Lee Jungryong, Ares Guild, and Jin Taekyung to participate.
- China’s contract requests thirty A-rank Hunters and two hundred B-rank Hunters, offers ten billion won for one week with additional weekly payment, and offers fifty trillion won for killing the Lich.
- Jin Taekyung and Team Leader Choi have departed for China aboard a Chinese private jet.
- Increasing mana density is associated with a recent rise in Gate accidents. The Lich may have undergone an unexplained evolution similar to the Skeleton Warlord.
- Lee Jungryong intends to strengthen Go Jun so that Go Jun can defeat Jin Taekyung.
- Jeok Cheongang remains unconscious after the battle at Mount Song. His qi acupoints are slowly becoming blocked; he has roughly six months left, with continued qi treatment potentially buying one or two additional months.
- The Luoyang Strange Physician does not know how to cure Jeok and directs Taekyung to the Divine Physician, who is believed to be in Sichuan.
- The System created the Supreme Peak Quest **Find Mr. Shin in Sichuan**. Its objective is to find the Divine Physician and receive treatment; its failure condition is Jeok Cheongang’s death.
- Taekyung is carrying Jeok Cheongang to Sichuan with Hyuk Mujin, Cheongpung, and Gung Gibang. Mae Jonghak will seek assistance from the Sichuan Tang Clan, Emei, and Qingcheng.
- Taekyung connected Hyuk Mujin and Gung Gibang to himself with a Ten-Thousand-Year Cold Iron chain and used ninety years of internal energy to force their journey toward Sichuan. Cheongpung travels alongside them.
- Ju Hwaran is twenty-one and has led the Yongbong Escort Bureau for two years while her father, Ju Hogun, remains near death from qi deviation.
- Chief Escort Seok is the caravan’s thirty-third casualty; Hwaran blames herself for his death and the preceding losses. Heo Jun, her uncle and Chief Escort, supports her.
- Black Stone Stronghold is one of the Green Forest Alliance’s Eighteen Strongholds, led by the Peak master Heavenly Axe. Heavenly Axe and hundreds of bandits are confronting the Yongbong caravan near Black Stone Mountain.

## Translation Decisions

- Use **Warlordmon**, **Quick Attack**, and **Body Slam** for established terms.
- Use **Chairman Xiao Yang**, **People’s Liberation Army**, **Central Military Commission**, and **Focke-Wulf**.
- Retain **Tokyo Hot** with an explanatory adult-video-studio footnote.
- Retain **hwabyeong** for the anger-and-vase pun, with an explanatory footnote.
- Use **Divine Physician** for 신의 and **Medicine Immortal** for 의선.
- Use **Find Mr. Shin in Sichuan** for 사천에서 신 서방 찾기.
- Use **Sichuan Tang Clan**, **Emei/Emei Sect**, and **Qingcheng/Qingcheng Sect**.
- Use **Chinese gallnut**, **Guozijian**, **Zhuge Gonghu**, and **Myriad-Li Chasing Wind Movement Technique**.
- Use **Ten-Thousand-Year Cold Iron**, **Black Stone Mountain**, **Black Stone Stronghold**, **Eighteen Strongholds**, **Chief Escort Seok**, and **flexible sword**.

## Durable state

{
  "active_continuity": [
    "Jeok Cheongang remains unconscious after the battle at Mount Song.",
    "Jeok Cheongang is not suffering from demonic qi or poisoning, but his qi acupoints will slowly become blocked.",
    "Jeok Cheongang has roughly six months left, with continued qi treatment potentially buying one or two additional months.",
    "The Divine Physician is a legendary anonymous physician who has practiced for more than forty years, refuses payment, and is protected by common people.",
    "A porcelain shard left for the Luoyang Strange Physician indicates that the Divine Physician is in Sichuan.",
    "The System created Trace of the Divine Physician and the Quest Find Mr. Shin in Sichuan.",
    "Jin Taekyung is taking Jeok Cheongang to Sichuan while searching for the Divine Physician.",
    "Mae Jonghak will seek assistance from the Sichuan Tang Clan, Emei, and Qingcheng and provide several helpers requested by Taekyung.",
    "Hyuk Mujin, Cheongpung, and Gung Gibang are accompanying Taekyung as the small search party.",
    "Ju Hwaran is twenty-one and has led the Yongbong Escort Bureau for two years while her father Ju Hogun remains near death from qi deviation.",
    "Chief Escort Seok is the thirty-third casualty of the Yongbong Escort Bureau's current escort journey, and Hwaran blames herself for the deaths.",
    "Heo Jun is Hwaran's uncle and the Yongbong Escort Bureau's Chief Escort.",
    "Black Stone Stronghold is one of the Green Forest Alliance's Eighteen Strongholds, led by the Peak master Heavenly Axe.",
    "Heavenly Axe and hundreds of Green Forest bandits have confronted the Yongbong Escort Bureau near Black Stone Mountain."
  ],
  "continuity_sources": [
    309
  ],
  "open_questions": [
    "Can Jin Taekyung find the Divine Physician in Sichuan before Jeok Cheongang's condition becomes irreversible?",
    "What is Jeok Cheongang's unidentified illness, and can the Divine Physician cure it?",
    "Will the Sichuan Tang Clan, Emei, Qingcheng, and the requested helpers assist the search?",
    "Can Ju Hwaran's exhausted Yongbong Escort Bureau cross Black Stone Mountain and complete its escort journey?",
    "How will the confrontation with Heavenly Axe and Black Stone Stronghold affect the caravan?",
    "Will Ju Hogun recover from his qi deviation?"
  ],
  "safe_through": 309,
  "temporary_decisions": [
    "Use Divine Physician for 신의 and Medicine Immortal for 의선.",
    "Use Chinese gallnut for 오배자.",
    "Use Find Mr. Shin in Sichuan for 사천에서 신 서방 찾기.",
    "Use Sichuan Tang Clan for 사천당문 and 당문, Emei/Emei Sect for 아미 and 아미파, and Qingcheng/Qingcheng Sect for 청성 and 청성파.",
    "Use Guozijian for 국자감.",
    "Use Zhuge Gonghu for 제갈공후, distinct from Zhuge Wuhou.",
    "Use Myriad-Li Chasing Wind Movement Technique for 만리추풍신법.",
    "Use Black Stone Mountain, Black Stone Stronghold, Eighteen Strongholds, Chief Escort Seok, and flexible sword for the newly established source terms."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 305

# Chapter 305

“Are you feeling any better? You haven’t fully recovered yet.”

“…I’m fine.”

“If you’re struggling, rest. Even if Team Leader Seok is still young, keep pushing yourself and you’ll wear your bones down.”

“I have no excuse.”

Lee Jungryong shot a glance at Go Jun, who answered with a pale face, and clicked his tongue inwardly.

*I never expected him to be beaten so easily.*

Go Jun was the most useful blade Lee Jungryong possessed.

Although his abilities were not known outside their circle, Lee believed that fewer than five people in all of Korea could stand against him.

Of course, two of those people were Cheon Taemin and himself.

*To take him down in a single move… He exceeded my expectations.*

Lee could no longer deny it. He had underestimated Jin Taekyung and the Peace Guild.

The gap in strength was laughable, yet he was the one who kept getting humiliated.

Lee Jungryong’s gaze shifted to Go Jun’s bowed head.

“Go Jun.”

Go Jun lifted his head. Lee calling him by name meant that this was a conversation between Master and Disciple, not between a Vice Guild Master and his Head of Security.

“Yes, Master.”

“You are the Disciple I taught with all my heart and soul. Never forget that.”

“I have never forgotten it for a moment. You are more than a parent to me, Master.”

At the unwaveringly loyal answer, Lee Jungryong nodded.

In many respects, Go Jun was a lacking Disciple. But when it came to loyalty, he surpassed anyone.

Lee had put it off because of a faint hope that Go Jun might be enough as he was…but now he needed to sharpen him further.

“You weren’t defeated. You merely fell. I will give you the strength to rise again.”

“Strength, you say?”

“For now, understand it that way. I will make it possible for you to defeat Jin Taekyung with your own hands.”

“…”

Go Jun’s body trembled as he bent deeply at the waist.

“Thank you, Master.”

“Always remember that this Master believes in you.”

Despite his warm voice, Lee Jungryong’s eyes had sunk to unfathomable depths.

Go Jun, unaware of that fact, raised his flushed face. By then, faint sounds from outside the door were drawing closer.

“He’s finally here.”

At Lee Jungryong’s mutter, Go Jun frowned.

“He missed the agreed-upon time.”

“Leave it. It’s only the first year of his term. He wants to enjoy himself as much as possible before the lame-duck period begins.”

“Even so, making you wait…”

“Team Leader Seok. Remember your position.”

“Understood.”

Go Jun returned from Lee Jungryong’s Disciple to the Head of Security for the Ares Guild and closed his mouth.

Not long afterward, five or six people opened the door and appeared.

The middle-aged man at the front strode toward Lee Jungryong and extended his hand.

“I apologize for keeping you waiting. Traffic was especially bad today. It reminded me once again how valuable a security vehicle can be. Ha ha.”

He was someone who could extend his hand first to Lee Jungryong, the practical leader of the Ares Guild, while carrying himself with both courtesy and confidence.

The middle-aged man wearing a Korean flag pin on his chest was entitled to do so.

Lee Jungryong shook his hand with a faint smile.

“Think nothing of it. Thank you for coming, Mr. President.”

Baek Hanseong, the twenty-seventh President of Korea and the youngest person ever elected to the office at the age of forty, nodded.

“It’s been a while, Vice Guild Master Lee. Is this the first time we’ve met since I took the oath of office at the beginning of the year?”

“That’s right. We seem to be meeting more often than expected.”

“Pardon me? Ha ha.”

Baek Hanseong let out a dry laugh at Lee Jungryong’s answer.

He knew very well how much power the man before him wielded.

There was even a saying that Korea had two presidents, and that the Ares Guild House was another Blue House.

*Lee Jungryong never once visited the Blue House during the previous president’s term.*

The major Guilds were fortresses built from power and wealth.

And Lee Jungryong’s standing, as the man who held the Ares Guild in the palm of his hand, surpassed that once held by the heads of the chaebol conglomerates.

There were two reasons Baek Hanseong could meet him like this, unofficially though it was.

First, Baek was still early in his term and enjoyed the full support of the people. Second, they had a matter in which they could help each other.

“They say people become more relaxed as they grow older. I suppose that doesn’t apply to me.”

“You really are refreshingly direct.”

Baek Hanseong understood the meaning behind Lee Jungryong’s subtle remark and held out a pristine white document envelope.

“An unofficial diplomatic letter from Chairman Xiao Yang.”

“Unofficial, as expected.”

“Yes. As you know, that’s how it is.”

The People’s Republic of China. As its formal name suggested, China remained a deeply rooted communist nation.

And the Communist Party leadership did not want the people to become agitated or their trust in the Party to waver.

“You’ve managed to conceal damage on that scale. I’m not sure whether to call that impressive.”

“If this becomes known, all of China will fall into chaos. By then, it will be too late to undo.”

Even so, among the tiny number of people who already knew the truth, it was being called the Sichuan Catastrophe.

The Chinese Communist Party leadership had announced that the destruction was the result of a major earthquake and deployed the People’s Liberation Army to seal off the surrounding area.

“A Lich, was it? That Named Monster ended up helping China’s Central Committee, albeit unintentionally. I hear even satellites from the United States can’t see what’s happening inside.”

“It’s spatial distortion magic. Extremely powerful spatial distortion magic.”

“I see. I’m still completely ignorant when it comes to magic.”

“It may have helped the Central Committee, but it will have a negative effect on the war situation. We have no idea what is actually happening in there.”

Unlike his unhurried voice, Lee Jungryong’s eyes were rapidly scanning the words written on the documents.

A short while later, after confirming everything, a quiet mutter escaped between his lips.

“Thirty A-rank Hunters and two hundred B-rank Hunters…”

The documents from China were contracts.

Contracts stating that China intended to hire them as mercenaries to resolve the current crisis.

There was also one clause that Lee Jungryong could not simply overlook.

“They singled me out.”

President Baek Hanseong nodded.

“They say the Central Military Commission strongly insisted on it. They believe the Ares Guild and your role, Vice Guild Master Lee, will be decisive in this matter.”

“I imagine so. The situation is becoming urgent enough to spiral out of control.”

“As you know, China has a great many Hunters, but relatively few of them are truly elite.”

“That’s China’s chronic problem.”

Tap. Tap. Tap.

Lee Jungryong’s fingers tapped slowly against the documents. A calculator was spinning busily inside his head.

The strength China was requesting amounted to twenty percent of the Ares Guild’s total forces.

No. If Lee Jungryong joined them, it would rise to fifty percent. There were fewer than twenty S-rank Hunters in the entire world, making them absolute powers.

*They must be desperate.*

This was not the first time China had made such a request.

Three days earlier, Lee Jungryong had held a secret meeting with the Chinese ambassador to Korea. The video he had watched along with the proposal had far surpassed his expectations.

*That was tremendous magic.*

The ability to command more than several thousand monsters. Magic with overwhelming destructive power.

It was on an entirely different level from the Liches he had encountered during the Great Cataclysm. It had been only a single spell, but it was more than enough to understand the danger this incident posed.

However…

*Danger always comes with a commensurate reward.*

Establishing a foothold in a dictatorship was never easy.

The Sichuan Catastrophe was a disaster to some, but an opportunity to others. And the terms China had offered were sweet—so sweet that Lee was worried his competitors might seize them first.

*Either way, as long as I’m there, this won’t fail.*

Lee Jungryong finally finished thinking and parted his lips.

“I accept China’s proposal.”

“That is a wise decision.”

A smile appeared at the corners of President Baek Hanseong’s mouth.

If the Ares Guild made a major contribution to this incident, it would have considerable diplomatic value as well. As someone who wanted to achieve a major accomplishment during his term, Baek could not have been more pleased.

“I’m the one who should be grateful that I can help my country and Your Excellency. However…”

Baek Hanseong’s smile faded at Lee Jungryong’s next words.

“I heard a rumor that similar proposals were made not only to the Ares Guild, but also to several of the other ten largest Guilds in Korea.”

“…”

“I know it’s an unfounded rumor. But I thought I’d ask you, just in case.”

After a brief silence, Baek Hanseong answered.

“An unfounded rumor has leaked out. That will never happen.”

At that moment, the chief secretary standing behind Baek Hanseong thought to himself:

*I’ll have to remove tomorrow’s unofficial meeting with the heads of Korea’s ten largest Guilds from the schedule.*

Only after trimming away those irritating stray branches did Lee Jungryong smile brightly.

“Just as I thought. I understand. I’ll select the necessary personnel immediately.”

But Baek Hanseong was not finished.

“The rumor about the ten largest Guilds is false, but it isn’t entirely baseless.”

Lee Jungryong, who had been organizing the documents, paused.

“What do you mean?”

“Among the Guilds that received China’s proposal, there is one that does not belong to the ten largest Guilds.”

“Don’t tell me…”

A sudden thought flashed through Lee Jungryong’s mind.

At the same time, Baek Hanseong opened his lips.

“The Peace Guild, to which Hunter Jin Taekyung belongs.”

“…”

Lee Jungryong’s face hardened.

Again. Once more, that bastard was getting in his way.

The three syllables of Jin Taekyung’s name were beginning to irritate him more than the name Choi Minwoo ever had.

“That is rather inconvenient.”

Lee Jungryong’s voice rasped like sandpaper.

The young, inexperienced president, whose five-year shelf life had only just begun, had allowed it to happen despite knowing exactly what he was doing.

Lee knew that the new president’s political leanings were anti-Ares, but wasn’t this tantamount to declaring open hostility?

Suppressing the shout that was trying to burst from him, Lee Jungryong spoke.

“When there are too many boatmen, the ship ends up on a mountain.”

“I’m aware.”

“Your Excellency, this is not something that can be handled so simply…”

Lee Jungryong’s words were cut off by Baek Hanseong’s calm reply.

“The boat’s owner personally called for those boatmen, so there was nothing I could do.”

“If you mean the boat’s owner… Surely not?”

“Yes. Chairman Xiao Yang personally named them. He specifically requested that Vice Guild Master Lee, the Ares Guild, and Hunter Jin Taekyung all participate.”

“…”

Lee Jungryong’s eyelids trembled.

At the sight, President Baek Hanseong felt the same thrilling sensation he had experienced when he had defied everyone’s expectations and won the presidential election. He suppressed the smile trying to escape and glanced down at his watch.

“The Peace Guild is a very small operation, so perhaps that’s why they prepared so quickly. They should already be aboard their flight by now.”

* * *

—You, wicked human.

“Wow. So this is first class.”

—My judgment that you were a wicked and foolish human was mistaken. I humbly apologize.

“Damn, these cushions are incredible. What kind of alcohol do they have?”

—You are a madman. A madman. A lunatic. A fucking lunatic!

“Look at how spacious the seats are. I could live here.”

—You insane human! Don’t go!

*Ah, he’s so damn loud.*

Pretending not to hear the Skeleton Warlord screaming inside my Inventory, I asked Team Leader Choi:

“How much does one of these cost?”

Team Leader Choi opened his mouth as though he had been waiting for the question.

“The new model from the German aircraft manufacturer Focke-Wulf, famous for its outstanding technological prowess, costs—”

*Here we go again.*

Before I had to listen to an explanation about Focke-Wulf’s founder, I hurriedly cut him off.

“I don’t know if it’s Focke-Wulf or Pokémon Black Friday, but I’m asking how much a plane like this usually costs.”

“For an aircraft like the one we’re currently riding, it should be a little over one hundred billion won.”

“Hmm. I should buy one.”

Anyone who overheard me would have stared at me as if I were insane.

But it wasn’t impossible.

I recalled the conversation Team Leader Choi and I had shared only a few hours earlier.

*It’s a shame, but please tell Chairman Jongseok[^1] I can’t go.*

[^1]: Taekyung twists the Korean title *juseok* (“chairman”) into the similar-sounding name Jongseok.

*It isn’t Chairman Jongseok. It’s Chairman Xiao Yang. In any case, that is unfortunate.*

*I’m sorry too. Promoting my name and raising the Guild’s standing both sound good, but that place is a bit much.*

*They offered ten billion won.*

*How much?*

*Ten billion won. If you go beyond the promised period of one week, they’ll calculate an additional ten billion won per week.*

*Weekly pay? T-ten billion won a week?*

*It can’t be helped.*

*B-but I’m still not going. With thousands of monsters and a crazy skeleton mage, even I have to draw the line. It’s not like I’m some money-crazed bastard.*

*They say they’ll pay fifty trillion won to whoever kills the Lich.*

*Ah, now I suddenly feel like eating something spicy. I hear Sichuan cuisine is incredibly hot and savory…*

*…*

*Fuck it. Let’s go.*

All the preparations had been completed in the blink of an eye. Only Team Leader Choi and I were leaving for China.

In any case, Chairman Xiao Yang had originally wanted only me.

*This isn’t about the money.*

I was going only to help the people of China who were suffering and raise the Guild’s standing.

With an expression full of resolve, I turned to Team Leader Choi.

“But, Team Leader.”

“Yes?”

“If I make fifty trillion won… Do I split that with the Guild too?”

“…”

“Let’s settle this before we go. Money matters need to be clean.”

Team Leader Choi stared at me with an expression of disbelief before answering.

“We’ll split it nine to one.”

*This guy was something else, too.*

Just as we were looking at each other like a pair of human garbage heaps, the private jet sent by China began taking off with an in-flight announcement.
## Chapter artifact 306

# Chapter 306

As the enormous fuselage of the Boeing 747-8 VIP lifted into the sky, Jin Taekyung, who had been bouncing excitedly in his seat, sprang up and began roaming around the interior.

“Wow, this isn’t a plane. It’s practically a hotel suite! Team Leader, look over here. There’s even a bed!”

At his repeated exclamations, Choi Minwoo pressed a hand to his forehead. Anyone watching him would think they were going on an overseas vacation instead of heading to a battlefield.

“Um… Mr. Jin Taekyung?”

“Hang on. I’m going to ask what kind of liquor they have here.”

The private jet sent by China’s Central Committee had three Chinese flight attendants. Jin Taekyung called one of them over and began speaking to her in fluent Chinese.

*No way. He’s practically a native speaker.*

His vocabulary and fluency were good enough to belong to someone born and raised in China.

Choi Minwoo was also talented with languages and could speak several fluently, but he was nowhere near Jin Taekyung’s level.

He had heard that Taekyung hadn’t even been good at studying. When on earth had he learned to converse in Chinese that well?

A thought suddenly flashed through Choi Minwoo’s astonished mind.

*Come to think of it, he’s the sort of person who talks to monsters, too.*

Jin Taekyung was the very person who used the Demon Realm language—which even renowned linguists struggled to decipher—while mixing in every kind of profanity.

When Choi Minwoo had asked how that was even possible, the only answer he had received was that it was a trade secret.

*…Let’s just stop thinking about it. That’ll be easier on my mind.*

Giving up on things did make life more peaceful. Besides, it wasn’t as if this was the first time something like this had happened. He figured he would find out when the time came.

Having given up, Choi Minwoo accepted the glass of liquor poured by the flight attendant.

“What kind of liquor is this? It’s clear, so it looks like some kind of vodka.”

“First Dew Fresh.”

“…”

“Heh. I didn’t expect it, but they actually had soju. First Dew tastes best on the rocks.”

Jin Taekyung sat down on one of the sofas provided inside the plane and downed glass after glass. Choi Minwoo was appalled by the nonstop drinking and asked:

“Are you haunted by the ghost of someone who died unable to drink?”

“I’m getting my drinking done in advance. Going back and forth is a hassle.”

“Excuse me?”

“Never mind. It’s nothing.”

After muttering something incomprehensible, Jin Taekyung asked:

“You said it would take five or six hours, right?”

“That’s how long it will take to reach Chengdu International Airport in Sichuan Province. It could take longer in an emergency.”

“What do you mean by an emergency?”

“What else could it be?”

The emergency Choi Minwoo referred to meant that the army of monsters led by the Lich had conquered Chengdu.

“Of course, that possibility is remote. By now, an enormous number of members of the People’s Liberation Army and Hunters should be guarding the city.”

A population of one hundred million and an area twice the size of the Korean Peninsula.

Chengdu was the administrative capital of Sichuan Province. If Chengdu fell, it would be the same as Sichuan Province being occupied.

Jin Taekyung waved a hand after listening to Choi Minwoo.

“Come on, you can’t rule things out just because they seem unlikely. If we could do that, Monster Waves wouldn’t happen in the first place.”

“Of course, that’s true, but…”

“Always assume the worst. Don’t try to guess the best.”

It was a casual remark, tossed out without a second thought. Anyone could say such a thing, but hearing it from Jin Taekyung made it feel different.

How should he put it? It carried a meticulousness concealed beneath apparent carelessness, along with the seasoned skill of a veteran who had survived countless battles.

*He’s a strange man.*

Choi Minwoo sometimes found Jin Taekyung uncanny.

It wasn’t a question of skill or combat experience.

Whenever he spoke with Taekyung, he would occasionally get the feeling that this was not someone who had weathered only one or two crises.

*Even though he’s younger than me.*

At Choi Minwoo’s newly contemplative gaze, Jin Taekyung paused while raising his glass.

“What? Want vodka instead?”

“No. First Dew is fine, too.”

“Right? It has such a clean taste…”

Jin Taekyung stopped speaking and scowled.

“This bastard’s acting up again. Seriously.”

“…”

“I wasn’t talking to you, Team Leader. Some asshole keeps squawking so loudly.”

Choi Minwoo glanced nervously at the flight attendants and whispered:

“The Skeleton Warlord?”

“Yeah. He’s been making a huge fuss about not wanting to go to China.”

“Because of the Lich.”

“Even if they’re both Named Monsters, they’re in completely different classes. And the Lich is a high-ranking undead monster, too.”

If the Lich was a big shot, the Skeleton Warlord was a complete nobody. No matter that he had become a Named Monster, he was different from the roots up.

Besides, the Lich that had appeared this time was powerful enough to be on an entirely different level from the Liches that had existed during the Great Cataclysm.

Choi Minwoo spoke with a serious expression.

“Mr. Jin.”

“Ah, shut up already! Sorry, what?”

“I think something has been going wrong lately.”

“Did you throw out your back?”

“No. I mean the way the world is changing.”

“Oh, the atmosphere. Same here. I want to live peacefully, but all these pieces of shit keep raising hell from every direction… Ah, I wasn’t talking about you, so shut up.”

A sudden headache began pounding through Choi Minwoo’s skull, and he rubbed the space between his brows.

“I’m talking about Gates and monsters.”

“Oh.”

Jin Taekyung, who had been arguing with the invisible Skeleton Warlord, raised his head.

“It is strange. Two Named Monsters have appeared within a few months, even though normally you might see one every few years.”

“Gate accidents have also increased sharply this year. The media, which love to tear people apart, are blaming the carelessness of Guilds and individuals. But I’m not so sure. The International Gate Research Institute’s position is the exact opposite.”

On the tablet PC Choi Minwoo handed him, the words **Investigation Results: Sudden Increase in Gate Mana** were displayed in a large, heavy font.

“It hasn’t been officially announced, but it’s already a foregone conclusion. Mana density is rapidly increasing in a considerable number of Gates.”

“That’s the real cause of the recent spate of Gate accidents?”

“Yes.”

Mana was the source of a monster’s power. If the mana density inside a Gate increased, it was only natural for the monsters inside to grow stronger as well.

And above all…

“I have proof in my hands.”

At Jin Taekyung’s words, Choi Minwoo nodded.

The Skeleton Warlord. According to what Taekyung had told him a few days ago, this Named Monster had *evolved*.

It had happened so suddenly that even the Warlord himself did not know why.

“The Lich that appeared this time may have experienced the same growth in power.”

“I expected something like that to some extent. But…”

Jin Taekyung swept back his long hair.

“This is going to be fucking brutal.”

“That’s why we need sufficient countermeasures. According to some of the material I obtained regarding this incident…”

“I’ll look at the material later.”

“Excuse me?”

“I’ve got a lot of things to catch up on right now.”

“Things to catch up on? Right now?”

The Boeing 747-8 VIP they were riding was flying at an altitude of twenty-five thousand feet.

What kind of overdue work could he possibly deal with up here?

Jin Taekyung’s answer only made Choi Minwoo more bewildered.

“I’m going to sleep.”

“Sleep? In times like these?”

“I haven’t been able to sleep at all lately.”

“W-wait a second.”

“Don’t wake me under any circumstances. This is the answer for now.”

What kind of person was this?

Before Choi Minwoo could stop him, Jin Taekyung began crawling into the bed prepared inside the aircraft. Choi Minwoo could only gape at him.

“Oh, right. Team Leader Choi.”

Jin Taekyung poked his head out and added with a serious expression:

“Please turn off the lights.”

“…”

The moment his head touched the pillow, Jin Taekyung fell peacefully asleep.

Watching him, Choi Minwoo thought:

*The profit split is nine to one. No exceptions.*

* * *

Ding.

> **System**  
> **Login** complete.

I opened my eyes to the hardness of a wooden pillow and bed instead of a soft pillow and mattress.

Above me was the ceiling of a pavilion in the Murim Alliance, entirely unfamiliar to me.

*I’m back.*

A full month had passed since I left. In the Murim, not even two shichen would have passed.

I turned my head to the right and saw a small-framed old man fast asleep.

Even with sunlight streaming through the window and shining directly on his face, he—the Fire King, Jeok Cheongang—did not move an inch.

“I’m back, Old Master.”

It was the moment I quietly muttered those words and began to rise.

“Oh, mm. Ah.”

“…”

I stared down at Hyuk Mujin, who was writhing like a worm in the corner of the room, and thought:

*I’m pretty sure I put him on guard duty before logging in.*

This lunatic was having a wet dream when I told him to stand guard.

It was a lifelong regret that I couldn’t record this on video and share it in the Jin Family of Taiyuan group chat.

Still, I could kick him in the ass.

Bam!

“Ugh!”

“Wake up, you Tokyo Hot[^1] bastard.”

[^1]: Tokyo Hot is a Japanese adult-video studio.

Hyuk Mujin sprang to his feet, jolted awake from his blissful dream by the pain.

“Captain, you’re awake!”

“Yeah. Looks like you just woke up too.”

Hyuk Mujin’s eyes darted around as he gave an awkward smile.

“Ah, well. Something came up.”

“…”

*Did something come up, or were you about to come?*

I glared at Hyuk Mujin with disgust and let out a deep sigh.

Fine. This was all my fault for trusting him.

“Whew. How long have you been asleep?”

“Not long. I swear.”

“Then nothing unusual happened while you were awake?”

“Yes. Until two shichen ago, I kept watch so thoroughly that I wouldn’t have let even a single ant get inside.”

I thought about that for a moment before asking:

“If it was two shichen ago, wasn’t that when I had just fallen asleep?”

“Well, yes, I suppose it was. But I really didn’t sleep long.”

“Right. Two shichen isn’t very long.”

“Yes, yes.”

“Our Mujin followed me into my dreams to protect me, huh?”

Hyuk Mujin nodded furiously.

“That’s right! Hyuk Mujin, Vice Squad Leader of the Jin Dragon Squad of the great Jin Family of Taiyuan! I swear that I will remain eternally loyal to you, Captain!”

“My, aren’t you a good boy.”

I chuckled and picked up the flower vase beside the bed.

“Then why did you make such strange moaning sounds while guarding me in my dream?”

“Gasp.”

“Who on earth did you meet? Mimi of Honghwaru? Kirara of Tokyo-ru? Or the filial daughter from the soft tofu restaurant?”

I’d had it. Just looking at that bastard made my pent-up rage flare and my chest feel so tight I couldn’t stand it—*hwabyeong*[^2] in the making.

I raised the flower vase high, and Hyuk Mujin cautiously backed away.

[^2]: *Hwabyeong* literally means “anger illness”; *byeong* can also mean “bottle” or “vase,” creating a pun with the flower vase.

“P-please let me off just this once.”

“I’ve let you off five hundred times already.”

“Then since you’ve let me off five hundred times, just one more time…”

“Hold still.”

Whoosh!

At that moment, three things happened simultaneously.

First, the flower vase in my hand shot forward with tremendous force.

Second, after barely grazing the crown of Hyuk Mujin’s bowed head, it flew toward the door.

Third, the door opened at exactly that impossible moment, and someone entered.

“How is Great Hero Jeok’s condition—”

Bam!

The squat old man holding a small cloth-wrapped bundle in one hand could not finish his sentence.

His eyes losing focus, he stared at Hyuk Mujin and me. His lips opened and closed several times before he slowly crumpled to the floor.

Thud. Crash!

The flower vase rolled away after striking the old man squarely in the forehead, while acupuncture needles and various medical instruments spilled from the bundle he had been carrying.

“…”

“…”

At first light, the Luoyang Strange Physician had come to check on Jeok Cheongang’s condition.

And that was how he collapsed with a concussion.
## Chapter artifact 307

# Chapter 307

“The world looks new.”

Those were the first words spoken by the Luoyang Strange Physician after he came to his senses one shichen later.

His tone and voice were so gentle that I could hardly believe he was the same old man who had been flying into a rage before I returned to the modern world.

“A-are you all right?”

“Of course I’m all right. My head hurts a little, but these things happen.”

I was starting to get scared.

How eccentric did someone have to be for people to call him the Strange Physician to his face?

And yet, after taking that flower vase to the head, he had completely transformed into another person.

Even Sword Saint Mae Jonghak, who had rushed over after mistaking the commotion for an attack by Dark Heaven, asked him anxiously:

“Hey, Strange Physician. Are you really all right?”

The Luoyang Strange Physician smiled faintly and nodded.

“Ha-ha, Great Hero Mae. You need not worry about this old man. Just take special care to ensure that this promising young man does not get injured in the war that will break out in the future.”

“You…!”

“Elder…!”

This was the greatest physician in Henan. A true doctor!

And I had grumbled to Mae Jonghak that such a good man was a quack.

With my head bowed from overwhelming emotion and shame, I heard the Luoyang Strange Physician’s voice beside my ear.

“If that young man were to suffer a serious injury and I had to treat him, I might just drive a large acupuncture needle into his stagnant blood with this hand. Ha-ha.”

“…”

“…”

“A physician cannot commit murder, can he?”

So that was what he meant by taking care not to get injured.

Feeling a chill run down my spine, I raised my head. The Luoyang Strange Physician met my gaze and smiled like the kindly old man next door.

“Disciple of Great Hero Jeok or not, I’ll gouge those eyes right out. Ha-ha.”

“…”

He wasn’t an old man next door anymore. He was practically the murderer next door.

Still wearing a bandage wound tightly around his head and laughing like a lunatic, the Luoyang Strange Physician began the examination of Jeok Cheongang that he had put off for a while.

Whatever his personality, he was the greatest physician in Henan and a medical master counted among the top ten in the world.

However, the conclusion he reached after an examination lasting a little over half an hour was much the same as before.

“I don’t know. It’s truly strange.”

“There’s… no way to treat him?”

“You’re asking whether there’s no way to treat him?”

The Luoyang Strange Physician looked at me with displeasure before continuing.

“There is no incurable illness under heaven. But how can you find a treatment when you do not even know the name of the disease?”

This was desperate.

If we at least knew the name of the illness, we could somehow search for a treatment. But this meant it was an unknown disease.

I took Jeok Cheongang’s wrinkled hand in mine.

*Why can’t someone as strong as you wake up?*

Was it because he couldn’t bear the shock caused by the death of his closest friend after losing his Disciple?

No. The Jeok Cheongang I knew was far more steadfast than that.

Then…

*The aftereffects of the Dance of the Fire God and Demon? Or did that bastard Blood Lord use some kind of trick?*

The Dance of the Fire God and Demon was a double-edged sword that even ate away at its user’s life. For an already aged Jeok Cheongang, its power must have been more than he could bear.

And the Blood Lord, one of Dark Heaven’s core figures, was exactly the kind of bastard who would have used some dirty trick.

The Luoyang Strange Physician muttered as if groaning.

“It isn’t demonic qi seeping into him, and he hasn’t been poisoned. But if this continues, his qi acupoints will slowly become blocked. That much is certain.”

Mae Jonghak and I both snapped our eyes wide open.

“What? What does that…?”

“Strange Physician, didn’t you say his life wasn’t in danger?”

“You weren’t listening properly. I clearly said his life was not in danger *for now*.”

The Luoyang Strange Physician continued slowly.

“I could tell from his pulse today that he is different from yesterday. If Great Hero Jeok remains in this state and does not wake up, all his qi acupoints will become blocked, and he will be reduced to an ordinary countryman.”

“You mean he’ll only regain consciousness after losing his martial arts?”

The Luoyang Strange Physician shook his head at my question.

“I cannot even guarantee that. Even if Heaven helps Great Hero Jeok wake up, his body has already outlived its natural span. How much longer do you think it can hold out?”

“…”

It felt as if I had been struck in the back of the head with a hammer.

As the Luoyang Strange Physician said, Jeok Cheongang had already lived for more than a hundred years.

The Fire King could probably endure another ten or twenty years, but only while he still possessed powerful internal energy and martial arts.

How much time did the old man named Jeok Cheongang have left—not the Fire King?

“Six months. If we keep guiding his qi through his acupoints, we might buy him another couple of months, but that’s all.”

“Six months… Is there really no way?”

“You insolent brat. Do you need to make this old man repeat himself twice before you’ll be satisfied?”

He was saying that because he didn’t know the disease, he didn’t know how to cure it.

The Luoyang Strange Physician’s answer was so firm that it doused the tiny spark of hope.

But he was also the one who rekindled that spark.

“So you must find a Divine Physician.”

“A Divine Physician?”

My mind snapped fully awake, as if someone had dumped a bucket of ice water over my head. I opened my eyes wide and asked:

“Who is the Divine Physician?”

The Luoyang Strange Physician stared at me in surprise.

“…You don’t know the Divine Physician?”

“He sounds like a physician. A really skilled one.”

“His sobriquet is Divine Physician, of course! Even a stray dog in a back alley would know that. Great Hero Mae, is this fellow really a martial artist?”

Mae Jonghak, who had been standing a step away, stopped the enraged Luoyang Strange Physician.

“Calm down, Strange Physician.”

“Even if he’s a complete outsider, there are limits. Does it make any sense for him not to know the Divine Physician?”

“Hm. He must be famous.”

“…What?”

“…Huh?”

The Luoyang Strange Physician and I both whipped our heads around. Mae Jonghak was smiling with an innocent expression.

*Where have I seen that smile before?*

Oh, right. I remembered.

With a smile exactly like Cheongpung’s, Mae Jonghak opened his mouth.

“I was secluded deep in the mountains for nearly thirty years, you see. Ha-ha.”

“What are you talking about? It has already been more than forty years since the Divine Physician made his name known throughout the martial world.”

Mae Jonghak was silent for a moment after the Luoyang Strange Physician’s blunt correction. Then he answered:

“Come to think of it, it has been more than forty years for this old man as well. It had been so long that I got confused.”

“…”

“…”

*That was dark, Chuseong.*

* * *

The Divine Physician.

Just as his sobriquet suggested, he possessed medical skills that had reached the realm of the divine.

It was said that he had appeared at the edge of the continent more than forty years ago, displayed medical skills approaching a miracle, treated thousands of patients by himself, and subdued an epidemic. That was how he earned the sobriquet Divine Physician.

“After that, the Divine Physician continued to generously share his medical skills. He never turned away a patient who came to him, and he never accepted any form of payment. He was a true physician with a character as lofty as his medical ability.”

“Ooh, a god-tier doctor.”

“The powerful figures of the world tried to invite him as a guest, but he vanished without a trace every time. He would say that he intended to care for patients in the lowest places.”

“Ooh, the Medicine Immortal Hong Gil-dong.[^1]”

“The Divine Physician always covered his face with a white veil, so no one could see what he looked like, but…”

“Ooh, the masked physician.”

The Luoyang Strange Physician, who had been about to continue, picked up a large acupuncture needle a handspan long.

“I’ll shut that mouth of yours for you.”

“I’m sorry. It slipped out before I knew it.”

“Even with Great Hero Mae here, this young brat’s mouth never stops. Isn’t that right?”

Mae Jonghak’s eyes lit up as he answered:

“Ooh, the Divine Physician.”

“…”

After that, the Luoyang Strange Physician, who had become half a sage, gave us a brief but thorough explanation of the Divine Physician.

He was universally recognized as the greatest physician under heaven and possessed a noble character.

And…

“No one knows his identity?”

“Did I not tell you that he always wears a veil when practicing medicine?”

“Even so, he’s been active for over forty years. How can no one know what he looks like?”

To put it bluntly, one gust of wind should have been enough to expose his face.

But the Luoyang Strange Physician shook his head.

“Someone may know. But no one in the world has ever properly identified him.”

“Why? Because he always ran away before anyone could find him?”

“The witnesses contradicted one another every time. Some among the common people said the Medicine Immortal was an old man with white hair, while others claimed he was a shaven-headed Buddhist nun. Even when people who had seen the Medicine Immortal were tracked down and coaxed in every way imaginable, their accounts never matched. How could anyone possibly find him?”

“Huh.”

“His reputation among the common people is absolute. So many of them volunteered to become his eyes and ears and hide his identity that even the imperial palace gave up trying to find him.”

“I understand that this Divine Physician is impressive, but…”

I looked at the Luoyang Strange Physician, who was smiling proudly, with disbelief.

“How am I supposed to find someone even the imperial palace gave up on?”

“Oh. That’s true.”

“…”

Was he joking right now?

When I glowered at him, the Luoyang Strange Physician suddenly began to laugh heartily.

“Don’t worry. Would I have brought this up without a plan?”

“Just as I thought. I knew I could trust you, Elder.”

“Ten years ago, I heard about the Divine Physician and was so deeply impressed that I set out on a medical tour.”

“Oh, a medical tour.”

I had heard of such a thing in passing when I was holed up at the Jin Family of Taiyuan. If martial artists went on dueling tours, physicians went on medical tours.

The Luoyang Strange Physician said that he had followed the trail of the Divine Physician’s deeds, crossing the continent from its most remote regions and spending five years on the journey.

“It was a rewarding and joyful journey. However, it was difficult for someone like me who was already over sixty.”

But he had found something at the end of it.

“Something I had only imagined actually happened.”

The unexpected gift he received came from a slash-and-burn farming village in the southern part of the continent.[^2]

The slash-and-burn settlers, who had barely been able to eat or receive an education, told him about a benefactor who had treated their illnesses and left several months earlier.

“You folks have nothing I can treat. I’ll leave a few silver coins behind, so use them to restore your strength.”

“Um…”

“Why? I’m sorry, but this is all the money I have left…”

“It’s not that. Are you perhaps a physician from Luoyang?”

“Why do you ask?”

“The benefactor who treated us not long ago told us that if a physician from Luoyang with the surname Oh came, we should give this to him.”

They had given him a shard of a porcelain bottle with a jade-like hue. That object was now held in the Luoyang Strange Physician’s hand.

“What is this…?”

“Read what’s written on it.”

Faint writing remained on the shard resting in his wrinkled palm.

*Chinese gallnuts from Sichuan are the finest.*

What the hell did that mean? As I stared at it in bewilderment, the Luoyang Strange Physician explained:

“Chinese gallnut is a widely used medicinal ingredient. With this one line, the Divine Physician was subtly telling me that he was in Sichuan.”

“…That’s how you got that from it?”

“I’m telling you, that’s what it means.”

“Then if I say Japanese adult videos are the best, does that mean I’m in Japan?”

“What the hell are you talking about? Great Hero Mae, isn’t this fellow completely insane?”

Mae Jonghak, who looked ready to die of curiosity, asked:

“Just what are these ‘adult videos’?”

“That’s not important right now!”

The Luoyang Strange Physician, who had been hopping mad, placed the shard of the bottle in my palm.

“Look properly! Can’t you feel it? The Divine Physician’s desperate desire to exchange medical knowledge with me?”

“I can feel no such desperate desire…”

It was the exact moment I picked up the shard to inspect it more closely.

Ding.

> **System**
>
> - Quest Item, **Trace of the Divine Physician**, acquired!
> - You can infer his whereabouts from **Trace of the Divine Physician**!
> - Quest, **Find Mr. Shin in Sichuan**, generated!

I muttered as I looked at the Luoyang Strange Physician.

“I can feel it. His feelings.”

And I could see it, too.

A way to treat Jeok Cheongang.  

[^1]: Hong Gil-dong is a legendary Korean outlaw known for helping the oppressed and vanishing from those who pursued him.

[^2]: A slash-and-burn farming village was a remote settlement established by people who cleared and cultivated forested land by burning vegetation.
## Chapter artifact 308

# Chapter 308

“Go to Sichuan. If it’s the Divine Physician, there must surely be some way.”

The Luoyang Strange Physician was one of the ten greatest physicians under Heaven.

A physician of that caliber spoke with absolute certainty. Find the Divine Physician. His medical skills were the best under Heaven.

*There’s hope.*

If I found the Divine Physician, I could save Jeok Cheongang.

I looked down at Jeok Cheongang, lying there like a man sleeping peacefully, then bowed to the Luoyang Strange Physician.

“Thank you. Truly.”

The Divine Physician was an enigmatic figure whose identity no one knew.

Without the token of the Divine Physician that the Luoyang Strange Physician had given me, I would have felt as if I had been dropped into the middle of a vast ocean.

“Ahem. Just with words?”

“Would you like me to bring you a souvenir?”

The Luoyang Strange Physician gave a quiet laugh at my joking reply.

“You insolent brat. Instead of wasting time spouting nonsense, start packing your bags right now.”

“Oh, right.”

The journey from Henan to Sichuan was several thousand li even by a rough estimate. Even if I used my movement technique, it would surely take close to a month.

*And there’s no guarantee I’ll find the Divine Physician quickly.*

I looked at the Quest window, which I had not yet closed, and muttered inwardly.



> **System**
>
> **Quest**
>
> **Find Mr. Shin in Sichuan**
>
> You have acquired the only trace left behind by the Divine Physician.
>
> The Divine Physician is the greatest physician under Heaven. At present, he is the only hope capable of waking Jeok Cheongang.
>
> You must search every corner of the vast land of Sichuan and find him!
>
> **Grade:** Supreme Peak
>
> **Restriction:** Possession of **Trace of the Divine Physician**
>
> **Mission:** Find the Divine Physician and receive treatment (Incomplete)
>
> **Reward:** ???
>
> **Failure:** Jeok Cheongang’s death



What the hell was with that Quest Grade?

I was looking for one person, and its Grade was Supreme Peak.

Fortunately, the trace he had left long ago allowed me to determine that he was in Sichuan. But the land was so vast that the search would still be damn hard.

*Modern Sichuan Province was about twice the size of the Korean Peninsula, wasn’t it?*

Murim and the modern world were completely separate worlds. But based on what I had experienced so far, the scale of the land and the way people lived were similar.

The thought of searching Sichuan for someone whose name and face I did not even know left me at a loss.

*Damn it. It would be easier to find Mr. Kim in Seoul.*

But what choice did I have? This was not a matter of choice. I had to find the Divine Physician by any means necessary if I wanted Jeok Cheongang to live.

Jeok Cheongang had six months left.

If I continued guiding qi through his acupoints, I might be able to buy another month or two. But that was all the time Jeok Cheongang had been given.

*I’ll find him before the deadline.*

To do that, I had to shorten the time required. I quickly turned the matter over in my head, then spoke.

“May I ask you for a favor?”

It might consume a huge amount of manpower and money.

But Sword Saint Mae Jonghak offered a solution without hesitation.

“I will write letters to the Sichuan Tang Clan, Emei, and Qingcheng.”

“Thank you.”

If I could obtain the cooperation of the Sichuan Tang Clan, one of the Five Great Families, as well as the Emei Sect and Qingcheng Sect, each one of the pillars of the Nine Sects and One Gang, the search would become much easier.

But that was not the end of my request.

“Since you’re helping me anyway, could you add a few more things?”

“Hm. The atmosphere is unsettled after the bloodbath at Shaolin. Everyone suspects that Dark Heaven and the Demonic Cult are stirring again, so I may not be able to offer you much help. For martial artists affiliated with a sect, their own sect comes first.”

“I don’t need that much help.”

“Tell me anything I—or Huashan—can help with.”

“Please assign me a few people. That will be enough.”

“Do you have anyone in mind?”

“Yes.”

I nodded and named several people.



* * *



A short while later, Mae Jonghak and the Luoyang Strange Physician left the pavilion and walked along slowly as they spoke.

“Will that be all right? I understand that meeting the Divine Physician has been your lifelong wish.”

“My lifelong wish…”

At Mae Jonghak’s words, the Luoyang Strange Physician gazed into the distance as he recalled the past.

“It was. I abandoned my official post and picked up acupuncture needles because of him.”

The Luoyang Strange Physician had once been a promising young scholar.

His grandfather had been the head of the Guozijian, the empire’s highest educational institution, and had served as the late Emperor’s tutor when he was still Crown Prince.

What else could one expect from a scholar’s bloodline? His father and two older brothers had also entered government service and made names for themselves at court.

If a plague had not broken out in the year the Luoyang Strange Physician placed first in the imperial examination, he likely would have followed the same path.

“Countless people died. Following my assigned duty, I classified the dead, the survivors, and those who were bound to die.”

In his youth, when he had only just entered government service, the Luoyang Strange Physician had believed without a doubt that the august Emperor would issue an order, release relief grain, and send imperial physicians to suppress the plague.

He had believed that every civil and military official would do their utmost to save the suffering people.

“I had been mistaken. While the people were dying from the plague, the Emperor expanded a detached palace for his new consort, and the powerful divided among themselves everything that should have gone to the people.”

“What did you do?”

“I wrote lies as facts. Under my brush, a hundred thousand seok of grain, wealth, and medicinal supplies became aid distributed to the sick. The imperial physicians who had been attending the scholar-officials became true physicians laboring to suppress the plague.”

“That must have been painful.”

“It was. When I returned to my family after leaving the palace, the imperial physicians sent by the Emperor were there. They had been sent for my grandfather, who had caught a mild cold.”

That was when he first learned that the world put a price even on human life.

The hand of the Luoyang Strange Physician, gripping the cloth bundle containing his acupuncture needles, turned white.

“Then I heard about the Divine Physician. A doctor who risked his life to treat patients at the source of the plague. One person who subdued the plague alone and saved thousands of lives.”

He immediately returned to the palace, destroyed every record he had written, and left the government.

He had to sever his ties with his family, but he did not care.

He took up acupuncture needles instead of a brush and studied medical texts instead of the Four Books and Three Classics.

“I was called a quack many times. There were patients sitting at death’s door whom I managed to save, but there were also many whom I ultimately failed to treat and had to send off.”

After becoming a physician, he witnessed countless cycles of life, aging, illness, and death.

Then, twenty years later, the promising young official began to be known as the Luoyang Strange Physician.

“None of it would have been possible without the Divine Physician. Without him, I would have become a puppet of the rotten court.”

Mae Jonghak smiled faintly at his words.

“So the Divine Physician gave rise to another Divine Physician.”

“What an absurd thing to say. I’m content to remain the Strange Physician. There is only one Divine Physician under Heaven.”

The eyes of the Luoyang Strange Physician, who was famous for his eccentricity, shone like a boy’s.

Mae Jonghak could not hold back his laughter at the sight.

“Good grief. Should I take back the Divine Physician’s token even now?”

“Since Heaven cannot be reached, it is Heaven. If I had wanted to find him, I would have left for Sichuan ten years ago, when I received the token. My place is here. And…”

The Luoyang Strange Physician added with a bitter smile:

“What face could a quack who cannot cure even one patient at this age possibly show the Divine Physician? This is enough for me.”

“Thank you. With hostile forces stirring everywhere, if Great Hero Jeok recovers, the entire Murim will owe you a great debt.”

“Come now, why are you acting like this? That doesn’t suit you.”

The Luoyang Strange Physician waved his hand as he spoke lightly, then suddenly wore a mischievous expression.

“Are you practicing in advance?”

“Practicing what?”

“The gravitas of an Alliance Leader, ha-ha.”

“Ah. That?”

Mae Jonghak scratched the back of his head with an awkward expression.

“I have no idea who keeps spreading such rumors. I have already turned it down several times…”

“At present, Great Hero Mae is the most qualified.”

“Don’t say that. Everyone is simply anxious and making the wrong choice.”

The bloodbath at Shaolin Temple had been a warning bell.

A hidden force known as Dark Heaven had appeared.

When an enemy whose existence had never previously come to light revealed itself, the leaders of orthodox Murim cautiously began bringing up one topic.

The re-formation of the Murim Alliance.

“There is someone else suited to that position. At the very least, it is not this old man.”

“Do you truly think so?”

The Luoyang Strange Physician raised a hand and pointed toward the sky.

It was still early dawn. The moon and stars remained in the sky, which had only just begun to brighten.

“One God has vanished, and the Ten Kings have grown old. From what I have seen with my own eyes, Great Hero Mae possesses formidable martial arts and an upright heart. You are the most suitable person to lead the Murim Alliance, the symbol of the orthodox faction.”

“Come now. I’ve already said that this old man absolutely cannot do it. With so many people in the world, why would they make me the Alliance Leader?”

“Then who do you believe is suitable?”

“Hm…”

Mae Jonghak thought for a moment before speaking.

“Right. Senior Peng, the Thunderbolt Saber King, is nearby.”

“He is far too…”

“What’s wrong with Senior Peng? I like his fiery personality. He’s a real man.”

“He would wreck the Murim Alliance with the same fire—with all the manliness in the world.”

“Then Senior Zhuge Gonghu is the obvious choice. He once served as the Murim Alliance’s Chief Strategist, and he rose to become one of the Ten Kings through his Supreme Peak immortal arts and outstanding formation techniques…”

“He died.”

“What? When?”

“More than ten years ago.”

“Good heavens…”

Mae Jonghak had been away for so long that he did not even know who was alive and who was dead.

After groaning for a while, he asked:

“Do you happen to know what became of the other two members of the Three Saints?”

“The Bow Saint’s whereabouts have been unknown for more than twenty years, and the other one… honestly, he should not even be considered.”

“Hm? Why not?”

The Luoyang Strange Physician looked at Mae Jonghak with an incredulous expression.

“Who in their right mind would try to elevate the Slaughter Saint to Alliance Leader?”

“What’s wrong with him? His martial arts go without saying, and he is thorough by nature. He would be perfect as Alliance Leader.”

“That is precisely the problem. He uses those martial arts and that thorough personality to work as an assassin. The greatest assassin under Heaven as the Alliance Leader? Is that even remotely possible?”

“Is that so? Now that you mention it, you may be right.”

As Mae Jonghak scratched the back of his head, the Luoyang Strange Physician thought:

*Is orthodox Murim really going to be all right like this?*

Meanwhile, preparations for Jin Taekyung’s departure were proceeding swiftly.



* * *



The first person to rush over after hearing that I was leaving was Jin Wikyung.

“Youngest.”

I was stuffing everything I needed into my traveling bag when I answered:

“Yes?”

“This eldest brother just heard some unbelievable news.”

“Believe it. It’s true.”

“W-where did you say you were going?”

“Sichuan.”

“H-how long will you be gone?”

“Six months. Maybe another month or two if it takes longer.”

“No!”

Jin Wikyung shouted as if he were crying out in grief.

“Where are you going at a dangerous time like this?”

“Sichuan.”

“I know! That is why I cannot send you!”

“I’m going.”

Jin Wikyung declared it with a grim expression I had never seen before.

“I forbid it.”

“Oh. Then I’ll veto your veto.”

“With Father away, you cannot defy my order as the Lesser Family Head and acting Family Head!”

“What happens if I defy it?”

“I will have no choice but to punish you according to the family law.”

“Then strike me from the family register.”

“How can you say such a thing!”

Judging by his expression, the world was going to end in ten minutes.

I left Jin Wikyung, who was reeling from the shock, and rose to my feet.

Jeok Cheongang, still unconscious, was strapped to a wooden back carrier on my back with silk.

*It might be too late by the time I bring the Divine Physician back with me.*

That was why I had chosen this method.

I would take Jeok Cheongang to Sichuan with me.

“Heave-ho.”

With this much, I would have no problem using my movement technique to some extent.

I let out a deep sigh as I looked at Jin Wikyung, who was staring at me with pleading eyes.

“Don’t worry so much. Nothing like what you’re imagining will happen.”

“Take the Jin Dragon Squad. At least take the Jin Dragon Squad.”

No matter how elite the Jin Dragon Squad was within the Jin Family of Taiyuan, under the circumstances, they would only be deadweight that slowed me down.

I threw a fully packed traveling bag toward one of the men and said:

“That’s why the Vice Squad Leader is coming with me.”

Hyuk Mujin caught the bag and thumped his chest confidently.

“Leave it to me, Lesser Family Head!”

“…”

“…Lesser Family Head?”

“Oh, no. Please take good care of the youngest.”

Jin Wikyung patted Hyuk Mujin on the shoulder with an expression that clearly said he did not trust him at all.

That was when—

“Benefactor! When are we leaving? Huh? Benefactor?”

“…”

“We’re leaving now, so please shut your mouth.”

Was taking that guy with us really the right choice?

I briefly regretted it, but Cheongpung was the perfect person for this trip, which required us to move as a small elite group.

*His strength is undeniable.*

If anything went wrong during the journey, Cheongpung was practically an entire army by himself.

“Sichuan! The Divine Physician! This is so exciting!”

“…”

It still wasn’t too late. Should I just leave him behind?

I left the pavilion while locked in an intense internal struggle.

The final member of our party was waiting at the entrance.

“Long time no see, you.”

At my words, he spoke with a gloomy expression.

“Requesting me was a poor choice.”

“No. You have to come with us.”

“My Myriad-Li Chasing Wind Movement Technique…”

“You only learned it up to the fifth stage.”

“H-how do you know that?”

“…Have you learned anything past the fifth stage?”

*The Oseong-and-Haneum villain.*[^1]

No, the final member was Gung Gibang, the Successor Beggar of the Beggars’ Sect.

Hyuk Mujin, Cheongpung, and Gung Gibang. Looking at the three of them together, this lineup was no joke.

I sighed and said:

“Come on, let’s go, you three Bermuda Triangle bastards.”

[^1]: O Seong and Han Eum were famous friends from the Joseon era; Taekyung is punning on O Seong’s name and oseong, “five stages.”
## Chapter artifact 309

# Chapter 309

It had already been three days since I left Luoyang with the Bermuda Triangle.

I suddenly opened my mouth.

“Mujin.”

“Huff, huff. Yes?”

Hyuk Mujin was sprawled face-down over a rock near a stream, looking as if he was about to breathe his last.

He had made great strides over the past year, but his personal reserves of internal energy and martial arts had quickly revealed their limits.

*Gung Gibang is keeping up fairly well too, but he’s not enough.*

As befitting the Successor Beggar of the Beggars’ Sect, Gung Gibang possessed one of the best movement techniques among the young prodigies. But he still fell short of Cheongpung and me.

What good was learning the Myriad-Li Chasing Wind Movement Technique, said to be the Beggars’ Sect’s finest movement technique for speed? He had only mastered it to five-tenths.

“Gung Gibang.”

“Huff… Why’d you call me?”

His breathing was ragged.

He was in better shape than Hyuk Mujin, but he was still having a hard time.

And then there was the last one…

“Benefactor, would you like some dumplings?”

“You eat plenty yourself.”

“I ate a lot on the way here. I’m full.”

“Then take a shit and eat.”

“Wow! What a method!”

“…”

As expected of Cheongpung.

The fact that he had enough leisure to stuff himself with dumplings while using his movement technique proved that he really was a monster.

Though I had no right to say that when I was in almost the same condition as Cheongpung even with Jeok Cheongang strapped to the pack frame on my back.

I scratched the side of my head as I looked at the three of them.

*Hmm. This is a problem.*

From Henan through Shaanxi and all the way to Sichuan.

It was a journey spanning several thousand li, and even on horseback, it would take at least a month.

But we did not have that much time.

We needed drastic measures to shorten the journey.

“Huff… Captain. Why did you call me?”

“Oh, it’s nothing.”

I turned to Hyuk Mujin.

“The thing I asked you to hold onto last time. Do you still have it?”

“The thing you asked me to hold? What was that?”

“The chain.”

“What are you talking about…? Ah, you mean that thing you used to wear with all those things dangling from it?”

“Yeah.”

It was a chain made of Ten-Thousand-Year Cold Iron, specially crafted by the Fire Gate Clan.

Just before the Star-Array Grand Banquet began, I had removed the chain along with the iron ball. When Hyuk Mujin heard that it was made of Ten-Thousand-Year Cold Iron, his eyes had lit up, and he had quickly taken it.

“You brought it, right?”

He was exceptionally quick on the uptake.

Sensing that something was wrong, Hyuk Mujin’s eyes darted around as he answered.

“No. I left it somewhere else for safekeeping.”

“Really?”

“Yes.”

“Then let’s do this. If I turn you over and it turns up, you turn up dead.”

“Ah, silly me. Now that I think about it, I did bring it.”

Clink.

Only then did Hyuk Mujin begin unwinding the chain he had wrapped around himself beneath his shirt.

Ten-Thousand-Year Cold Iron was impossibly hard yet light. It seemed he had tied it around his body like armor.

The chain could be used as temporary armor or as a weapon, and the material itself was an incredibly valuable treasure.

Perhaps for that reason, regret dripped from Hyuk Mujin’s eyes as he handed it to me.

“Didn’t you give this to me to use? I was saving it so I could make a weapon later…”

“I told you to hold on to it. Did I say it was yours?”

“Where’s the sense in taking back something you gave me?”

“I only borrowed it. It belongs to the Fire Gate Clan. What do you think Old Master will do if he wakes up later and finds you carrying this?”

“Please take it. Please hide it somewhere I’ll never see again.”

“Good. You’ve made the right choice. Gibang!”

I picked up the chain and called over the bewildered Gung Gibang before getting to work.

The two of them stared blankly at me, wearing expressions that clearly asked what I was doing. Then they spoke at the same time.

“What are you doing?”

“What kind of pointless crap are you pulling?”

Rattle, rattle.

I answered calmly.

“Can’t you see? I’m tying a knot with the chain.”

“No, I mean, why are you wrapping it around my waist…?”

“Hold on. Untie this.”

“There. Done.”

I looked proudly at the result of my labor.

Hyuk Mujin, Gung Gibang, and finally me—we were all tied together with the chain like a string of dried fish.

“Everyone had a good rest, right?”

“What do you mean, a good rest? It hasn’t even been fifteen minutes!”

“Untie us right now!”

I smiled brightly and shook my head.

At the same time, my dantian churned, and ninety years’ worth of internal energy surged toward my legs.

“All right. Let’s run.”

Fwoooosh!

“Waaaaagh! You lunatic!”

“The Captain’s gone mad! He’s trying to kill me!”

Connected to me, Gung Gibang and Hyuk Mujin sprinted wildly like wild boars with their tails on fire.

At the sound, Cheongpung, who had been relieving himself in the nearby brush with his ass bared, hurriedly burst out and followed us.

“Benefactor! I’m coming too!”

“…”

*I don’t think that bastard wiped.*

*No, he must have.*

I forced down the thought that had just occurred to me and activated my movement technique.

Time passed as quickly as the scenery rushing by, and we accomplished the astonishing feat of reaching the border between Henan and Shaanxi in just two days.

* * *

Disordered ranks and files. Exhausted faces.

Dozens of people trudging forward with difficulty all belonged to an Escort Bureau.

The escorts wearing weapons at their sides were exhausted, as were the caravan porters wearing thick clothes while leading the horses and carts.

It was not simply because of the four-month trade journey.

“Hwaran.”

At the voice that pierced her ear, the girl’s dark eyes, gleaming faintly, turned to the side. A clear voice soon rang out.

“Yes, Uncle Heo?”

“It’s about that…”

The person who quietly approached the front of the procession was a middle-aged man with a graying beard.

After hesitating, he let out a sigh and spoke.

“Chief Escort Seok has passed away.”

“…!”

The delicate figure swaying quietly atop the saddle abruptly went rigid. Only a moment later did her trembling voice emerge.

“In the end… it came to that.”

“The poison spread all the way to his marrow. There was nothing more we could do. I’m sorry.”

“It isn’t something you need to apologize for, Uncle. The death of Brother Seok—no, Chief Escort Seok—was my fault.”

Ju Hwaran bit down hard on her lip beneath her veil.

*It’s true. Everything happened because I lacked virtue.*

The death of Chief Escort Seok, who had grown up alongside her like a blood brother, and the deaths of the thirty-two people who had passed away before him had all been caused by her misguided judgment.

*Father. What should I do?*

Ju Hwaran raised her head and looked at the sky.

The sky was the color of ink. Above the countless stars, a man’s face appeared in her mind.

Her father, Ju Hogun, had fallen into qi deviation while cultivating two years earlier and was still hovering between life and death.

‘To have a beautiful and exceptionally talented daughter like you… This father could ask for nothing more. Ha-ha!’

That was something Ju Hogun had always said.

Another father might have adopted a son to continue the family line. But he loved his beautiful and extraordinarily talented only daughter, and always took pride in her.

‘You are the only one who will carry on my legacy. The past fifty years of the Yongbong Escort Bureau are nothing compared to what you will accomplish in the future.’

There was no one in Shaanxi who did not know how much Ju Hogun doted on his daughter.

But as Ju Hwaran grew older, people came to understand that he was not merely a foolishly doting father.

She possessed an exceptionally sharp mind—sharp enough to understand the Escort Bureau’s ledgers before she had even turned twenty—and looks so remarkable that she was known as one of the Three Flowers of Jiangbei.

On top of that, she was a master of martial arts skilled enough to be counted among the Ten Dragons and Phoenixes, the greatest young prodigies of the orthodox Murim.

That was who Ju Hwaran was.

But…

*Where did everything start going wrong?*

Ju Hwaran swallowed the sigh rising from deep within her chest.

Everything around her was collapsing, only two years after she had begun leading the Yongbong Escort Bureau in place of her incapacitated father.

“Hwaran, are you all right?”

The only thing she still had left was her people.

The fifty years her grandfather and father had built through kindness and virtue were the one support keeping her upright.

Ju Hwaran forced a smile at Heo Jun, the Chief Escort, who spoke to her with concern.

“Please don’t worry about me, Uncle Heo.”

“Then that’s a relief.”

Heo Jun nodded with a dark expression.

Ju Hwaran was only twenty-one years old.

She already possessed so much, but she was still far too young for her heart to have grown equally strong.

And now that she was suffering such intense guilt, the only thing he could do was watch over her.

Ju Hwaran knew that better than anyone. She cleared her throat and spoke.

“It’s getting dark, so we’ll camp here for the night. Please make the preparations.”

“That’s a good idea.”

“And… prepare for the funeral too.”

The thirty-third victim of this escort journey.

It was time to send off Chief Escort Seok, who had been with Ju Hwaran since her childhood.

If they could obtain salt, it would slow the corpse’s decay. But by the time the escort journey was complete, the poison remaining in his body would undoubtedly turn his flesh and bones into a handful of bloody water.

“I understand. Rest for a while.”

“Everyone is working hard. How could I rest? Don’t worry and go.”

Heo Jun gave a small nod and signaled with his hand. Soon, the people’s footsteps came to a halt.

There was still a chill in the air, but the broad stretch of land was perfect for camping. Ju Hwaran planned to replenish her strength here and cross the mountain early the next morning.

*We’re almost there.*

Ju Hwaran’s gaze fixed on the mountain shrouded in darkness.

The stones on that mountain were black, which was why it was called Black Stone Mountain. Once they crossed it, this escort journey would enter its final stretch.

They had suffered countless losses, but if the escort journey succeeded, the Yongbong Escort Bureau would have a chance to catch its breath.

*It’s seven days and nights to Mount Zhongnan. That isn’t generous, but if we cross Black Stone Mountain safely, we’ll have enough time.*

The problem was…

What attitude would the master of Black Stone Mountain take?

Black Stone Stronghold was one of the many mountain strongholds belonging to the Green Forest Alliance. It was powerful enough to be called one of the Eighteen Strongholds, and its leader was a Peak master famous for wielding a single battle axe with uncanny skill.

If the exhausted Yongbong Escort Bureau clashed with Black Stone Stronghold, they might have to endure even greater losses than the ones they had already suffered.

*Please, let nothing happen.*

Ju Hwaran was just turning around with that thought in mind when—

Rustle.

A faint noise pierced her ears.

The sound of someone stepping on dry leaves did not belong to a wild animal.

A red alarm bell instantly rang in Ju Hwaran’s mind.

*An enemy!*

Shing!

Ju Hwaran drew the flexible sword at her waist and shouted like a bolt of lightning.

“Who’s there?”

Her sharp cry echoed through the darkness.

Heo Jun, the Chief Escort, noticed the situation almost simultaneously. He led the escorts and surrounded her.

“Protect the Young Bureau Head!”

“Yes, sir!”

Clang, clang, clang!

Sharp weapons flashed in the faint moonlight.

That was when the brush more than fifty jang away began to sway.

“So this is who it is. The brave escorts of the Yongbong Escort Bureau.”

The sight of the towering, eight-cheok-tall giant with a huge axe strapped to his back drew a low groan from Heo Jun.

“Heavenly Axe…”

“Oh, Brother Heo. I’ve heard you’ve been running yourself ragged wiping the ass of some little girl lately.”

“How dare this bastard!”

A graceful figure suddenly stepped forward beside the stiffly standing Heo Jun.

“Perfect timing. We were just about to give you the toll.”

“Well…”

Heavenly Axe grinned and gave his axe a shake.

“Let’s see the goods first. Then we’ll talk.”

Rustle, rustle, rustle!

Behind his axe, hundreds of Green Forest bandits emerged.

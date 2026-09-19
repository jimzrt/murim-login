# Checkpoint Review — 450–454

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

# Chapters 450–454

## Plot

Taekyung’s group finds Donghu Stronghold completely destroyed, with Hwang Chung, Hwang Cheol, and Do Ripgun dead and no survivors. Mungyeong’s examination suggests that two or three Supreme Peak masters attacked, possibly including the missing Dongting Fisherman, whose connection to Dark Heaven remains unproven. No trace of the suspected Moving Formation is found, so Taekyung’s party travels through Tianling Falls to Zaoyang and continues overland toward the Zhuge Clan for expert help. Meanwhile, Wudang is investigating an unidentified killer demon responsible for more than thirty deaths.

At Zaoyang, the group encounters Qingxia Hall, a lavish procession of powerful families’ children. Taekyung defeats their guards and forces their leader, Ju Wongong, from his sedan chair. Ju claims imperial kinship and threatens punishment, but immediately submits when Taekyung displays Prince Shangshan Zhu Bao’s token. Ju explains that he is an exiled distant imperial relative who abused his authority and is now traveling to Dongting Lake for a luxurious boat excursion disguised as a welfare inspection.

Ju offers Taekyung Honglan, a beautiful singing courtesan and covert Lower District Sect member, as an inducement to join him. Taekyung recognizes her martial ability through Sound Transmission, refuses the offer, and receives an autograph request from Ju after Ju learns that Prince Shangshan has one.

## Continuity

- Taekyung accepted *Another Chaos* and is investigating the destruction of the Yangtze River Channel League’s Hubei strongholds with Jin Wikyung.
- Hwang Chung, Hwang Cheol, Do Ripgun, and Wang Pil are dead; the Dongting Fisherman is missing and is the leading suspect, but his guilt and Dark Heaven affiliation remain unresolved.
- The massacre involved at least two, possibly three, Supreme Peak attackers using different methods. No Moving Formation trace was found.
- Taekyung’s party escaped Tianling Falls, reached Zaoyang, and is traveling toward the Zhuge Clan on Mount Longzhong.
- Wudang is dealing with an unidentified killer demon that has murdered more than thirty people, including twenty pilgrims.
- Ju Wongong is an exiled distant imperial relative and Qingxia Hall leader. Prince Shangshan’s token can command his immediate submission.
- Honglan is Ju Wongong’s stage-name singing courtesan and a Lower District Sect member concealing her real name.
- The shared symbols between the Arch Lich’s magic circle and Dark Heaven’s formations, the Wudang killer demon’s identity, the other attackers, and the evidence in Lee Jungryong’s holographic recorder remain open questions.

## Translation Decisions

- Use “Donghu Stronghold,” “Dongting Fisherman,” “Tianling Falls,” “Zaoyang,” “Zhuge Clan,” “Qingxia Hall,” “Dongting Lake,” and “Lower District Sect.”
- Render 광수도귀 as “Mad Water Saber Demon,” 파랑호 as “Wave Fox,” and 사천혈사 as “Sichuan Blood Tragedy.”
- Render 살귀 as “killer demon,” 일급 낭인 as “First Rate wandering martial artist,” 주원공 as “Ju Wongong,” 홍란 as “Honglan,” 가기 as “singing courtesan,” 구족 as “the nine branches of kin,” and 사인교 as “four-person sedan chair.”
- Preserve Taekyung’s dry, profane humor, including his Johnson, Buster Call, Celestial Dragon, and hair-loss wordplay.

## Durable state

{
  "active_continuity": [
    "Taekyung accepted Quest Another Chaos to uncover the truth behind the Hubei incidents and find the culprit.",
    "Jin Wikyung is acting as an inspector for the new Murim Alliance and is cooperating with Taekyung's investigation.",
    "The shared symbols between the Arch Lich's magic circle and Dark Heaven's formations remain unexplained.",
    "The Sea Serpent Society and the Yangtze River Channel League's Hubei strongholds were destroyed, while the Dongting Fisherman disappeared.",
    "Wudang is responding to an unidentified killer demon responsible for more than thirty deaths, including twenty pilgrims on Mount Wudang.",
    "The Skeleton King's undead identity remains concealed, and Taekyung has ordered him to join Peace Guild under a prepared contract.",
    "Go Jun is expected to succeed Lee Jungryong as Ares Guild's captain and is searching China for Lee's holographic recorder.",
    "Taekyung's party has escaped Tianling Falls, reached Zaoyang, and is traveling by land toward the Zhuge Clan.",
    "Qingxia Hall is an influential Hubei social club formed by powerful families' children.",
    "Ju Wongong is an exiled Qingxia Hall young master and distant imperial relative who has been forced to defer to Prince Shangshan's authority.",
    "Honglan is Ju Wongong's Lower District Sect singing courtesan and is concealing her real name."
  ],
  "continuity_sources": [
    454,
    453
  ],
  "open_questions": [
    "What are the origin and purpose of the symbols shared by the Arch Lich's magic circle and Dark Heaven's formations?",
    "Who destroyed Donghu Stronghold and the related Yangtze River Channel League strongholds, and why was no Moving Formation trace left behind?",
    "Is the Dongting Fisherman a member of Dark Heaven, and who are the other Supreme Peak attackers?",
    "Is the killer demon attacking Wudang connected to Dark Heaven?",
    "What evidence is contained in Lee Jungryong's holographic recorder, and what are the terms of the Peace Guild–Wizard Guild agreement?"
  ],
  "safe_through": 454,
  "temporary_decisions": [
    "Render 황철 as Hwang Cheol, 도립군 as Do Ripgun, 광수도귀 as Mad Water Saber Demon, 파랑호 as Wave Fox, 동정호 as Dongting Lake, and 사천혈사 as Sichuan Blood Tragedy.",
    "Render 살귀 as killer demon and 일급 낭인 as First Rate wandering martial artist.",
    "Render 시부럴 as “sibu-leol,” 시벌좌 as “Lord Fuck,” and 시부럴좌 as “Lord Sibu-leol.”",
    "Preserve the Skeleton King's grandiose, mock-offended voice and Taekyung's dry, profane humor.",
    "Render 주원공 as Ju Wongong, 대죽산표국 as Daejuksan Escort Bureau, 형문검가 as Hyungmun Sword Family, 응성상회 as Eungseong Merchant Association, 천룡인 as Celestial Dragon, 사인교 as four-person sedan chair, 홍란 as Honglan, 가기 as singing courtesan, and 구족 as the nine branches of kin."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 450

# Chapter 450

At the edge of the island, near the sandy shore, several dozen people had gathered.

When the martial artists surrounding us opened a path, I finally spotted some familiar faces.

“Uncle Hwang! How could you leave without your nephew? How could you!”

Mu Song wailed in a hoarse voice. Perfected Being Hyeongong of Wudang watched him with a sorrowful expression, while Crouching Dragon Guest Zhuge Feng watched with a profound, unreadable gaze.

And then…

*Mungyeong.*

Usually, Mungyeong had a presence that was there and yet not there, never drawing attention to himself among the others. But from the instant he realized something had happened at Donghu Stronghold, he had moved more quickly than anyone.

As a medical apprentice rather than a Slaughter Saint, he had rushed from place to place in an effort to save even a single person.

But as though mocking all his efforts, not a single survivor remained.

The corpse Mu Song clutched as he wept endlessly belonged to one of the countless victims claimed by the tragedy.

“You’ve arrived.”

Jeok Cheongang gave Zhuge Feng a displeased glance before speaking.

“Is that Yangtze One Saber Hwang Chung?”

“It may be difficult to recognize him, but according to what we have determined, there is no doubt.”

*That.*

It might sound inappropriate to use such a word when referring to the dead.

But anyone who had seen the corpse of Yangtze One Saber Hwang Chung in person would have been unable to object. I was no different.

*What kind of lunatic did this?*

The corpse had been so badly mutilated that it was difficult to believe it had once been a living person.

The face had been crushed as if it had been smashed with a rock, and below the chest, there was simply no body left.

The stench of rotting flesh and viscera stabbed at my nose.

“Urgh—ugh!”

I could not blame Hyuk Mujin for staggering backward with a retch.

Even I, who had witnessed more gruesome scenes and corpses than I could count, felt my stomach churn.

The sworn brother of the Seafaring King, a Supreme Peak master who had ruled the vast Yangtze with his formidable martial arts…

Yangtze One Saber Hwang Chung looked more like a lump of meat than a corpse.

“Benefactor, this is…”

“It’s horrifying. What kind of fiend would commit such an atrocity?”

Cheongpung and Gung Gibang murmured, their faces pale.

I stared at the corpse with my face stiff as stone, then suddenly felt something strange and opened my mouth.

“What are those corpses?”

There were corpses covering the island, so it was not surprising that there were a few more.

But the two corpses I had noticed had been laid out side by side next to Yangtze One Saber Hwang Chung.

*That must mean they were important figures as well.*

Zhuge Feng followed my gaze and answered.

“Mad Water Saber Demon Hwang Cheol. And Wave Fox Do Ripgun.”

“Mad Water Saber Demon, Wave Fox…”

I had heard those names a few times before. Fairly recently, too.

After a brief moment of thought, I suddenly lifted my head.

“Could they be…?”

“That’s right. They were the Stronghold Lords of Dangyang Stronghold and Honghu Stronghold, which were under Dongting Lake.”

“Weren’t they said to have vanished without a trace after taking control of the Sea Serpent Society’s territory?”

“Yes. That was certainly the case.”

Zhuge Feng continued, his deep eyes fixed on the corpses of the two Stronghold Lords.

“The Mad Water Saber Demon was hot-tempered, while the Wave Fox was cunning. That was why, when the Sea Serpent Society incident occurred a month ago, everyone had no choice but to suspect them.”

Gung Gibang suddenly spoke up.

“My Master once said that only two people in the Yangtze River Channel League were capable of controlling the Mad Water Saber Demon and the Wave Fox.”

“That is correct. Regardless of their personalities, both possessed formidable martial arts. Without a leash to control them, they would have run wild like vicious hounds.”

In that sense, Yangtze One Saber Hwang Chung would have been the perfect leash for those vicious hounds.

He was the second most powerful master in the Yangtze River Channel League after the Seafaring King, and he must also have been exceptionally skilled at handling people.

But the sturdy leash had snapped, and the two vicious hounds had also been found dead.

Even the Yangtze River Channel League in Hubei Province, which had been locked in a fierce struggle over interests with the Sea Serpent Society for a long time, had been laid to waste.

And there was only one group capable of doing something like this without reason or justification.

“Dark Heaven. Is it them again?”

Perfected Being Hyeongong’s sigh carried unmistakable anger and sorrow.

After Henan and Sichuan, Dark Heaven’s shadow had finally fallen over Hubei Province.

No—perhaps Dark Heaven had been standing atop the world for a very long time.

Perhaps we simply had not felt its shadow because it had been night, with not a single ray of light.

*Just as the Head Elder joined hands with Dark Heaven long ago.*

This was not some scheme that had begun yesterday or today. It was a sinister plot that had been taking shape since the time of the Great Faction War.

“An age of chaos. This is truly an age of chaos.”

Crouching Dragon Guest Zhuge Feng muttered the words under his breath, then raised his head and looked around.

A pair of eyes gleaming with an unknowable light stared into the thick fog surrounding us.

It was as though he could see through it, straight to something crouching beyond.

* * *

Everyone, myself and my companions included, moved busily.

But even after searching every corner of the island and the surrounding cliffs in the hope of finding a single survivor or witness, we gained nothing.

If anything, our questions and frustration only grew.

*I can accept that there isn’t a single survivor. But how can there be no trace of a formation, either?*

If Dark Heaven had entered this place through a Moving Formation without passing through Tianling Falls, there had to be traces somewhere resembling those we had found in Sichuan.

Yet even after the retainers of the Zhuge Clan, famed for their knowledge of formations and mechanisms, joined the search, we had nothing to show for it.

The situation was so strange that Zhuge Feng eventually came to ask me about it.

“Are you certain such a formation really exists?”

“I told you, it does. We left Henan immediately after everything was over, so we couldn’t search for it there. But during the Sichuan Blood Tragedy, I saw it clearly with my own two eyes.”

“I knew about it through the letters I received, but even our family’s records contain no trace of such a strange formation.”

“Then add it to the records this time.”

“…”

“If we keep looking, we’ll find it. We have to.”

“I agree. But the people gathered here are insufficient.”

The island Donghu Stronghold had made its headquarters was large enough, but the surrounding environment was an even greater problem.

Cliffs hundreds of zhang long surrounded it on every side, making entry by land impossible, and an even wider expanse of river stretched beyond them.

Four fast ships and roughly three hundred people could only accomplish so much.

“It was a mistake to select people skilled in martial arts. We should have brought retainers with a deep understanding of formations.”

There was no point regretting it now.

Not only Zhuge Feng but everyone present, myself included, had been worried about a bloody conflict with the Yangtze River Channel League. None of us had dreamed that a situation like this would be waiting for us.

“Then we’ll go to the Zhuge Clan and bring back the people we need.”

“It would be best for me, as Family Head, to go myself, but under the circumstances, that seems to be our best option. I’ll have several retainers from our family accompany you. Take them with you.”

Jeok Cheongang, who had been listening quietly, suddenly spoke to me.

“Does that ‘we’ you mentioned include this old man?”

“Of course. Don’t you know the saying? Wherever a needle goes, the thread follows.”

“I see. Then have you heard this saying?”

“…?”

“Talk bullshit and you die.”

“...!”

When I flinched, Jeok Cheongang clenched his fist and threatened me.

“This old man isn’t going. If you want to go, go by yourself.”

“What, are you planning to stay here for the rest of your life? Never leave?”

“Who said this old man was staying forever? There’s no need for everyone to swarm off. If even one extra person stays behind to help find the formation, we can uncover the culprit and restore peace to Hubei, can’t we?”

Ever since his friend, the Dharma King Hong Dao, had been killed by Dark Heaven, Jeok Cheongang had ground his teeth at so much as the first syllable of its name. But there was something suspicious about his reaction this time.

After thinking for a moment, I clapped my hands.

“Ah. Now I understand. This is because of Tianling Falls.”

“...!”

“You should have just said so instead of beating around the bush. I forgot to take that into account, too.”

“W-who says I care about a little water? Have you forgotten who this old man is?”

“Hmm. A Coward?”

“You little—!”

Bam! Bam! Baaam!

After taking about seven blows to the back of the head, I ran away and headed toward our next destination.

The familiar faces gathered in one place turned toward me.

“Captain. What do we do now?”

I answered while giving Hyuk Mujin a light kick to the butt.

“I just talked it over with them. We have to leave immediately, so get ready.”

“Leave? Where are we going?”

“The Zhuge Clan. It seems we need to bring back people skilled in formations and mechanisms. If necessary, we’ll also bring in reinforcements from Wudang. I heard they have several Daoists who are well versed in formations.”

“I’m afraid Wudang may be difficult.”

I frowned at Gung Gibang’s sudden interruption.

“What kind of bullshit is that?”

“I’m not the one who said it. Perfected Being Hyeongong did.”

“Hmm. Now that I think about it, there must be a good reason for him to say that.”

“…”

“Whatever. Explain it properly. What do you mean?”

“It seems there’s been trouble on Wudang’s side as well. Even before the Sea Serpent Society incident, some mad killer demon had been murdering people throughout Hubei Province… It appears the situation has grown serious. More than thirty people have already been killed by his hand, so I suppose it would.”

“A killer demon? Is he a martial artist?”

“He certainly seems to be a martial artist of considerable skill. Most of the victims were commoners, but an accomplished First Rate wandering martial artist with a respectable name was reportedly found dead after accepting a government assignment to hunt him down.”

A first-class wandering martial artist would be considered a First Rate master wherever he went.

If the killer demon from the rumors had really disposed of a First Rate wandering martial artist with ease and escaped, there was a good chance he was a Peak master.

*But Wudang wouldn’t mobilize the entire sect just to catch one man.*

The question that had arisen in my mind vanished at Gung Gibang’s next words.

“Was it three days ago? Twenty pilgrims climbing Mount Wudang were slaughtered to a person. Among them were the sons and daughters of high officials and nobles who were seeking admission as lay disciples of Wudang.”

“Ah.”

It was not merely a massacre that had taken place somewhere else. It had happened on Mount Wudang itself.

As if pilgrims being massacred right in Wudang’s own front yard weren’t enough, the victims included children of high officials and nobles. Wudang’s fury was only natural.

*He’s completely insane. And bold, too.*

For a moment, the two words *Dark Heaven* crossed my mind, but I soon shook my head.

This was Murim. There were lunatics everywhere who made modern serial killers look like amateurs.

Even if someone were murdered in broad daylight on a main road, it would not be all that surprising.

*If Dark Heaven had done this, an incident incomparably larger would have erupted.*

In any case, that was the situation in Wudang. For now, we would have to think about it again after reaching the Zhuge Clan.

“Well, now that I know, everyone pack your things. They’re already preparing outside to take us back.”

Jin Wikyung had already decided to remain behind even before we went to meet Zhuge Feng, so I only needed to take the people here with me.

But one person—or rather, one gentleman—seemed to have a different idea.

“I’ll stay.”

“Which bastard— Oh. It’s Mungyeong.”

“Is there any reason I should go with you?”

“Nope. Stay. Stay.”

*Please stay.*
## Chapter artifact 451

# Chapter 451

“Benefactor, where are you going?”

“Huh?”

I flinched as I quietly headed for the door. Cheongpung, who had gathered his belongings, tilted his head and looked at me.

“What? Why?”

“Are you going somewhere?”

“I, uh… something urgent came up.”

“You said we had to leave quickly.”

“Listen, Young Hero Cheong. I wasn’t going to say this, but…”

I deliberately hardened my expression.

“I’m going to relieve myself. Happy?”

“But the privy isn’t in that direction.”

“…”

He was annoyingly sharp.

Martial arts were his minor, while eating and shitting were his major. He had to know the location of every privy on the island.

After hesitating for a moment, I answered.

“…I’m going to piss outside.”

Even I had to admit it was a desperate excuse.

Only then did Gung Gibang and Hyuk Mujin realize something was off. They stopped packing their bags and turned to look at me.

“Young Hero Gung, doesn’t the Captain seem unusually long-tongued today?”

“Yeah. Why does he look so restless?”

“That’s because I’m trying to decide which of you two to hit first.”

Normally, they would have backed down the moment I said something like that. But after being thoroughly conditioned by my violence, the two of them had grown considerably.

“Hmm. If this were our usual Captain, his hands would have moved before his words. But he’s trying to talk his way out of it? There’s definitely something going on.”

“Right?”

“Absolutely. Do you think I’ve only been beaten once or twice? There’s a reason and a flow to all this.”

Just as Hyuk Mujin was staring at me with narrowed eyes, Gung Gibang’s eyes suddenly widened, and he looked around.

“Wait. Where did Mungyeong go?”

“Oh, yeah. He was with us a moment ago. Where the hell did he go?”

Where did he go? He had already gone outside to wait for me.

*Let’s talk.*

I sighed as I remembered the Sound Transmission Mungyeong had sent me earlier.

If I denied it any further, I would only attract more suspicion.

“He’s outside. We have something to discuss privately.”

“In the privy? Just the two of you?”

“…What the hell are you talking about, you lunatic? You’re making it sound suggestive.”

Hyuk Mujin looked at me with a suspicious expression.

“Captain. I’ve already been conditioned to insults and violence, so I’ll be fine. But please don’t expose Mungyeong to anything strange.”

“…”

What the hell was this lunatic talking about? I was the one who looked ready to be stained with blood.

I was so dumbfounded that I could barely speak when Gung Gibang added his own remark.

“Hyuk’s right. The more I see that kid, the more thoughtful and kind he seems. Don’t harass him for no reason.”

“Wow. You bastards, seriously…”

I stopped myself.

“Forget it. What would you two know?”

Cheongpung had at least finally noticed what was going on and kept his mouth shut like a mute with honey in it…

No, now that I looked closely, he really was stuffing candy into his mouth.

*Where does that candy of his keep coming from?*

If I stayed here any longer, I was going to lose my mind.

I shook my head and ignored the voices coming from behind me as I left the house.

Outside, Mungyeong was waiting for me in the courtyard, dressed in spotless white robes.

“You’re late.”

“It didn’t take that long…”

“You’re late.”

“Sorry…”

“You’re late.”

“…”

*Please save me.*

The pressure of that endless repetition was no joke. His aura was being directed at me so subtly that no one else could notice it, and I swallowed hard.

“S-sorry I’m late. But what’s going on?”

“Pardon?”

“Huh?”

“What do you mean? You called me out earlier because you had something to say.”

Was he this year’s actor selected by the Cannes Film Festival?

He blinked as if he truly knew nothing. For an instant, even I almost fell for it.

The monster wearing the shell of a young medical apprentice smiled brightly and continued.

“Oh, you want us to move somewhere else for a moment? Understood.”

“No. If possible, I think it would be better to talk right here…”

“Oh, you want us to move somewhere else for a moment? Understood.”

“…Fine. Let’s go.”

I miss my mother.

Holding back tears, I began walking after Mungyeong.

We avoided the occasional disciples of the Zhuge Clan and Wudang, along with the river bandits of Water Dragon Stronghold, and entered a deserted area. Only then did Mungyeong finally speak.

“Dark Heaven. Did they do this?”

“Yeah. It seems that way.”

“There’s no one here.”

I corrected myself at the speed of light.

“It seems that way, sir.”

“So it is not certain yet.”

“There is always a possibility. But even though no formation was found, I believe this was definitely Dark Heaven’s doing.”

“Dark Heaven. Dark Heaven…”

Mungyeong muttered the words under his breath, then suddenly raised his head.

He silently stared at the dark night sky, where even the full moon had hidden itself. After a moment, he spoke without warning.

“Did you notice anything strange when looking at the corpses?”

“Something strange?”

“The marks left on them.”

Every death left traces. This was especially true of deaths caused by fighting between martial artists.

I had heard that a master with broad experience and a deep understanding of various martial arts could identify an opponent’s weapon and even determine which form had killed the deceased simply by examining the wounds left on the corpse.

And the young medical apprentice before me possessed the insight and martial arts to make him one of the finest forensic examiners in Murim.

“I’ve never seen wounds like these before. They seem to follow the principles of the very basic Three Calamities Sword Technique, yet they ripple like waves. They’re extremely strange and unusual.”

Mungyeong slowly raised one hand and waved it through the air. Strands of internal energy flowed from his fingertips, giving off a faint light in the darkness.

“If I had to guess, the culprit was not using an ordinary weapon. It was an unusual weapon with a crooked blade, something resembling a Snake Sword.”

“I thought they were cut with Force.”

“Your guess is correct. It was Force—or something equally sharp.”

The only thing as sharp as Force was Ten-Thousand-Year Cold Iron.

And no matter how thoroughly Dark Heaven had prepared, there was no way all those soldiers could have been equipped with weapons made of Ten-Thousand-Year Cold Iron.

*No matter how much gold you have, Ten-Thousand-Year Cold Iron is difficult to obtain.*

This was not a matter of capital. It was a matter of resource scarcity.

As I stood lost in thought, Mungyeong asked me a question.

“Did you examine all the corpses?”

“Not all of them. I looked at the ones that stood out. I’m not especially knowledgeable, so even after seeing them firsthand, I couldn’t tell what martial arts or forms had been used.”

“Among the corpses you examined was that of Hwang Chung, the Yangtze One Saber. What did you think?”

“His waist was severed in a single blow by Force. But the decay was so severe that I couldn’t determine anything beyond that…”

“What about the Mad Water Saber Demon and the Wave Fox?”

“Those two…”

I suddenly frowned.

A common feature shared by three corpses had just come to mind.

*…Only their upper bodies remained.*

The lower halves of all three corpses were nowhere to be found.

I had seen several corpses like that earlier, so I had not found it strange at the time. But now that I thought about it, it was certainly suspicious.

“Wasn’t it because the fish ate them?”

“That would not be entirely incorrect. According to my examination, the massacre at Donghu Stronghold took place ten days ago. The cold weather ended long ago, so severe decay is only natural. The corpses that were submerged in water would be even worse.”

Warm sunlight and damp air had erased many of the traces left behind by death.

But they had not erased everything.

“Compared to them, the limbs of the commoners’ corpses were relatively intact. Did you notice that?”

“Yes. Those who had not learned martial arts were not cut apart. They had been crushed.”

Unlike the corpses of the river bandits, the bodies of the children, women, and elderly had not been severed. Their entire bodies had simply been crushed and pulverized.

And there was one more thing.

“The houses and the ground around them had all collapsed. That would have been impossible without a force of ten thousand geun, and it is not a method an internal-arts master with powerful internal energy would choose.”

“So, an external-arts master?”

“There’s no one here, remember?”

“…I was just talking to myself.”

He was being awfully sensitive.

After making that hasty excuse, I fell silent for a moment.

Martial arts in Murim could broadly be divided into two categories.

Internal arts emphasized the efficient use and application of internal energy. External arts also used internal energy, but focused on tempering the body to its limits.

Most people were faced with those two choices as soon as they entered the world of martial arts, and most chose the former.

External-arts training was extremely painful. More importantly, it required a long period of endurance to achieve any meaningful results.

*That means there are only a handful of Supreme Peak external-arts masters capable of producing this level of destructive power.*

There were hardly any Supreme Peak masters in the world to begin with, even if you turned the entire world upside down and shook it out.

I glanced at Mungyeong, silently asking for an answer. A small wrinkle appeared on the smooth forehead of the young medical apprentice.

“Looking at me won’t help. I don’t know his identity either. No—I should say their identities, not his.”

“There are two of them?”

“At least two. Three at most.”

“Three Supreme Peak masters…”

“Based on my guess, they are even more formidable than the Qilian Three Fiends we faced in Sichuan. At least one of them uses an unusual weapon.”

*For fuck’s sake. This isn’t some five-star establishment. Why are there three Supreme Peak masters?*

It was only because Mungyeong and Jeok Cheongang were holding the line that I could afford to leave the stronghold at all. If they had not been here, I would have been too worried to go anywhere.

“With this much information, the Third Fiend might know something. He must have heard who his fellow conspirators were.”

The Third Fiend captured in Sichuan was one of the reasons I was going to the Zhuge Clan.

I had heard that he had become like a bipolar patient after his balls were crushed, but if I worked him over with care and dedication, he would not last long.

*Perhaps we can even use him to find the formation.*

That hopeful thought had barely crossed my mind when Mungyeong spoke.

“Perhaps it is someone everyone already knows.”

“What?”

“I mean the one who uses that unusual weapon.”

It took me a long time to understand what he meant.

The shock felt as if someone had struck me in the back of the head with a hammer.

I stared blankly at Mungyeong.

“Are you serious?”

“An experienced Supreme Peak master. Forms and wounds so unusual that it is difficult to read them. There are not many people who have reached that realm and use a weapon like this.”

“Then it really is…”

A dry voice slipped between Mungyeong’s lips.

“The Dongting Fisherman. At present, he is the most likely suspect.”

“…”

The eccentric master who had never left the area around Dongting Lake his entire life.

Unusually, he used a fishing rod made of black wood as his signature weapon. He was a Supreme Peak master who had crossed Tianling Falls and disappeared after becoming enraged by the tragic news concerning his friend, the head of the Sea Serpent Society.

*Everything fits perfectly.*

I had forgotten for a moment.

I had forgotten about his existence.

This was not a baseless suspicion.

Unlike the others, the Dongting Fisherman’s corpse had never been found. The only trace he had left behind was his broken black-wood fishing rod.

It was only a guess, but what if the Dongting Fisherman really was a member of Dark Heaven?

“But the Dongting Fisherman Zhuge Feng told me about had absolutely no reason to do something like this…”

“Everything has a reason. The Dongting Fisherman is a person, too. He must have had a shadow no one else could see. Zhuge Feng is probably suspicious of him by now as well.”

Mungyeong turned away, his voice cold.

“Always be suspicious, and stay alert. May martial fortune be with you.”
## Chapter artifact 452

# Chapter 452

Unlike when we first entered, the trip out was not as difficult as I had expected.

Part of that was because the whirlpools of Tianling Falls mostly spiraled outward. But it was also thanks to the veteran river bandits inside Water Dragon Stronghold, who had spent years working on boats and were making full use of their skills.

“Turn to port!”

“Starboard! Don’t row until the signal!”

“More, more, more… Now!”

“Yaaah!”

Whoooosh! Splash!

“The boat—the boat’s tilting!”

“Great Hero Jin!”

“Help us!”

“…Damn it, you bastards.”

Come to think of it, maybe it had been a little difficult after all.

But it was nothing we couldn’t handle. Even without powerful allies like Jeok Cheongang and Mungyeong, Cheongpung and I could get through most crises if we put our minds to it.

*The first time is hard. Why would the second be?*

The river bandits weren’t the only ones who had grown accustomed to Tianling Falls’ violent whirlpools. I had prepared in advance as well, and thrust both palms forward with all my strength.

Boom!

The tilting fast ship regained its balance. Now was the time to increase our speed and escape this damned whirlpool.

I called out the name of the person I had stationed at the stern specifically for situations like this.

“Young Hero Cheong, now!”

“Yee-haw!”

“You crazy bastard! Stop hanging there and playing around!”

“Oh, sorry, Benefactor. I didn’t mean to, but before I knew it…”

“Just hurry up and do it!”

“Yes!”

Boom, boom, boom!

Cheongpung was about as far from normal as a person could get, but his skills were undeniable.

Dozens of palm shadows infused with powerful internal energy struck through the air and lashed the surface of the water. The resulting thrust sent the fast ship vaulting over the whirlpool of Tianling Falls before landing on the other side.

Boom! Splash!

A towering spray of water fell over the ship’s hull. Gung Gibang and Hyuk Mujin, drenched from head to toe, muttered under their breath.

“Damn it. Last time we got dunked, and now we’re getting drenched. We really get everything.”

“I swear on my life, once this is over, I’m never coming back to the Yangtze. Not ever. Every day feels like living as a goddamn beggar.”

“…Are you picking a fight with me?”

“No. Honestly, doesn’t it feel like we’re living as beggars?”

“That’s true. It feels shitty to hear it, but you’re right. You’re right, but it still feels shitty.”

“Damn, I really do feel like a beggar.”

“…I get it, so shut up.”

Those two acted like this every chance they got.

Leaving behind the bickering of the two sweet-and-sour pork pieces who had now experienced both dipping and pouring sauce, the ship safely passed through Tianling Falls and sped across the Yangtze.

About three shichen later, when the fast ship that had departed at dawn reached the ferry landing at Zaoyang, it was already close to noon.

“The waters of the Yangtze do not reach Mount Longzhong, where the Zhuge Clan is located. From here, you will have to travel by land.”

The deputy Stronghold Lord of Water Dragon Stronghold had come in Mu Song’s place. I nodded at his words.

Hubei Province had highly developed water and land transportation, but that did not mean all the Yangtze’s tributaries were connected. A boat could not travel where there was no water.

*It’s not like these people are Vikings.*

Fortunately, the broad, level highways were well maintained. We could reach our destination quickly by carriage or by using movement techniques.

Zaoyang and Mount Longzhong were relatively close to each other, so it would not take very long.

The Zhuge Clan retainer who had been ordered by Zhuge Feng to accompany us was not standing around idle, either.

“I will immediately send word to the Zaoyang branch and have carriages prepared. Relay stations have been established all along the main roads, so if you change carriages along the way, you will reach our family home in no time.”

“Oh, right.”

The Zhuge Clan was a prestigious major faction that divided control of Hubei Province with Wudang.

The Jin Family of Taiyuan had also established branches and sub-branches throughout Shanxi Province to solidify its control over the region. The Zhuge Clan’s network was probably even more extensive.

*It’s like a major brand opening chain stores.*

*Then we should arrive in half a day at the latest.*

I had just gotten off the boat after roughly calculating the travel time in my head when—

Clack, clack, clack.

A group of people appeared with the sound of perfectly synchronized footsteps and surrounded the ferry landing.

I frowned as I stared at the unwelcome guests.

*What is this now?*

There were nearly thirty martial artists.

Every one of them wore a blue silk martial uniform that gleamed with luster, and each had a fine-steel long sword hanging at his waist. Hyuk Mujin’s eyes widened.

“That’s…”

“What? Do you know them?”

“No. I was just surprised by those silk uniforms.”

“What?”

“That’s Shu brocade, produced in Sichuan. It’s considered one of the finest kinds of silk in the world. My father dreamed of filling an entire warehouse with it. That’s how expensive and precious it is… And they made martial uniforms out of it. I don’t know who their employer is, but they must have a lot of money.”

“…”

I had told the bastard to identify them, and he was evaluating the quality of their silk instead.

When I stared at him in disbelief, Gung Gibang clicked his tongue and cut in.

“I can’t tell whether that bastard is a martial artist or a cloth merchant. Don’t waste your expectations on that Hyuk Family brat. Ask this old man instead.”

“I don’t know about the old man part, but I can make you a cripple. Tell us before my fist gets there.”

“…”

“They’re martial artists from Qingxia Hall. I told you, so please relax your fist a little.”

“Qingxia Hall? What do those bastards do?”

Gung Gibang glanced at my fist, which was still tightly clenched, and answered.

“They aren’t an official sect, but they wield considerable influence in Hubei Province in various ways.”

“They look pretty pathetic for people with that kind of influence.”

I cast a brief glance at the martial artists standing in formation in the distance.

They had made martial uniforms from expensive Shu brocade and carried quality swords, but that was all.

Most were Second or Third Rate swordsmen who fell short of First Rate. Perhaps they cared more about their appearance than their martial arts, because every one of them was well built and handsome.

*They’re even wearing makeup.*

At this point, weren’t they idols rather than martial artists?

The K-pop craze that had begun in Korea must have spread beyond the world and reached the Murim as well.

Qingxia Bulletproof Martial Artist Corps. Maybe they had come to perform at some event under a name like that.

“Those guys’ group name—or, no, their organization name—was Qingxia Hall, right? They’re that popular in Hubei?”

“I heard they’re fairly influential.”

“They look like they’d piss themselves the moment a real fight started…”

Did sect rankings in Hubei get decided by a popularity vote?

I was seriously pondering the question when the Zhuge Clan retainer spoke.

“Qingxia Hall is a sort of social club.”

“A social club?”

“Yes. It was formed by the sons and daughters of influential people with varying degrees of power throughout Hubei Province. They are always running around together and causing all kinds of trouble, but they have such powerful backing that matters usually fizzle out without consequence.”

“Oh. A rich-kid club.”

“I’m sorry, what did you say?”

“Nothing important. In that case, we can just continue on our way.”

So that was what they were. An empty cart making a great deal of noise, dressed up in gaudy finery wherever they went.

Pathetic people like that could be found anywhere. Having lost interest in Qingxia Hall, I took the lead and started walking.

“Which way do we go to reach the Zaoyang branch?”

“It will take less than fifteen minutes from here. First, we should head to the main road over there…”

The Zhuge Clan retainer trailed off.

From the main road he had just mentioned, an extravagantly luxurious procession was approaching—more lavish than anything I had ever seen.

“The heroes of Qingxia Hall are making their procession!”

At the shout of a middle-aged man with weasel whiskers and a thin voice, musicians walking along both sides of the procession began playing their instruments. Beautiful women scattered flower petals through the air.

In an instant, the main road was swept up in a festive atmosphere.

Commoners traveling along the road watched the procession with expressions that mingled expectation and discontent.

At the end of the countless gazes stood ten men and women riding in sedan chairs engraved with dragons and phoenixes.

They carried themselves with the ease and smiles possessed only by those who had money, looking down at the poorly dressed commoners as they tossed something from their hands.

Clatter, clatter, clatter!

Not hidden weapons… money. Shining silver nyang, each worth a hundred iron coins.

Only then did I understand why there had been anticipation in the commoners’ expressions.

“Waaah!”

“Silver nyang! It’s silver!”

“Jang-pal, you filthy bastard! How dare you try to snatch someone else’s silver nyang? Take your hand off it right now!”

“Bullshit. Didn’t you see that my hand got there first?”

“You fucking son of a—!”

The cheers and curses of the people covered the falling flower petals and silver nyang.

Women bit the silver nyang to test it after their unexpected windfall. Men loudly claimed that they were the rightful owners, then soon began fighting over it.

And the young men and women sitting in the sedan chairs laughed as they watched the spectacle.

“What a complete mess.”

It was a sight that made my head shake on its own.

The rich kids scattering money and enjoying the people’s reactions as if they were watching a circus looked pathetic. The sight of the commoners fighting tooth and nail for a single silver nyang left a bitter taste in my mouth and made me feel sorry for them.

But it had nothing to do with me.

“Let’s stop worrying about that and get going…”

I blinked, unable to finish my sentence.

What the hell?

The people who had been beside me moments ago were nowhere to be seen. Only the Zhuge Clan retainer remained, standing awkwardly in place.

“Wait, where did all those bastards go?”

The retainer hesitated, then raised a hand and pointed in one direction.

“They’re over there.”

“…?”

I turned my head and was rendered speechless.

Whoosh, whoosh-whoosh!

“No! You can’t!”

“My silver!”

One person was darting through the crowd with ghostlike movements, snatching silver nyang out of the air.

No. Not one person.

One fucking beggar.

*The Myriad-Li Chasing Wind Movement Technique?*

That lunatic was actually using a Beggars’ Sect secret technique for this?

He was even faster and more agile than he had ever been before. He had complained endlessly that he had only mastered the technique to the fifth stage, yet the movements he was displaying now were at least seventh-stage.

*That bastard is singlehandedly disgracing the Beggars’ Sect.*

Even if he was a beggar, how could he be this devoted to his calling?

But as little as I cared about another sect’s reputation, the Jin Family of Taiyuan’s own dark horse was no less impressive.

“Hah!”

Whoosh! Rat-a-tat-tat!

Hyuk Mujin kicked off the ground and soared into the air before swinging his sword. The silver nyang caught in the powerful, fluid arc flew upward, then came raining down onto the flat of his blade.

Hyuk Mujin’s face lit up when he checked the silver.

“Wow! Ten silver nyang!”

“…”

That bastard had ten hits coming, guaranteed.

I swallowed the curses rising to my throat and searched for the last remaining person.

*Where is that Cheongpung bastard?*

Unlike Gung Gibang and Hyuk Mujin, who were scooping up silver nyang with all their might, Cheongpung was nowhere to be seen.

But I knew Cheongpung’s habits inside and out, so it did not take long to find him.

“First, ten sweets, please. Oh, and some jeonbyeong too. Not the ones you just picked up—the big ones over there, and make it a generous serving. Wow, thank you! By any chance, where’s the dumpling shop?”

Snap.

As something inside my head broke, I rolled my eyes back and shouted.

“You fucking bastards!”
## Chapter artifact 453

# Chapter 453

“You fucking baaaastards!”

For a moment, I thought a cold wind had blown through.

Or maybe my shout had simply been loud enough to feel like one.

The latter was probably more likely.

Whoooosh.

Dozens of people who had been scrambling to pick up silver nyang froze in place, and silence descended over the noisy main road.

Then, the next moment, a single sentence slipping between my lips shattered the brief quiet.

“I’m counting to three.”

“……?”

“Fall in.”

“……!”

Give a dog three years in a village school and it can recite poetry. Keep beating it for long enough and it can memorize the Four Books and Three Classics.

That was why the village-school dog—or rather, Hyuk Mujin—who had been conditioned by a year of my violence and profanity, moved faster than anyone else.

“Faaall iiiin!”

With his reply echoing like a scream, Hyuk Mujin came running and stopped right in front of me.

A beat later, Gung Gibang finally grasped what was happening and used his movement technique to arrive almost simultaneously with Hyuk Mujin. As for Cheongpung…

“Pancakes! Please give me the pancakes, quick! Benefactor is angry!”

That sibu-leol bastard. Look at him making sure to get his pancakes even now.

Once the snacks were wrapped, I spoke gently to Cheongpung as he came rushing toward me like a streak of light.

“Take your time. I’m not angry.”

“Wow! Really?”

“Yeah. I’m not angry. I’m fucking pissed.”

“Ah, ah…”

I looked at the fidgeting Cheongpung and the two others who were subtly avoiding my gaze.

*When the hell are these bastards going to become human?*

They could not even drag up the last ounce of their strength and run to the Zhuge Clan, yet look at them using martial arts to pick up a few silver nyang.

Gung Gibang had even sneakily snatched silver nyang out of someone else’s hand. At this point, he was not a beggar. He was a bandit.

*Life, for fuck’s sake…*

I had worked so hard lately for the sake of the staff’s welfare, and this was how it ended up.

I looked up at the clear sky and spat into my palm.

“Hyuk Mujin. Put your forehead here.”

“Pardon?”

Hyuk Mujin raised his head sharply and asked with an incredulous expression.

“Just me?”

“Yeah. You for now.”

“What about Young Hero Gung?”

“He’s a beggar down to his bones. Honestly, if a beggar says he’s picking up silver nyang, it’s hard to criticize him.”

“An accurate and wise judgment.”

Gung Gibang, who had been watching my mood, cut in with a solemn voice. Hyuk Mujin opened his round eyes.

“No, what do you mean, ‘hard to criticize’? You get angry every time I call you a beggar.”

“Me? What nonsense. I’m a beggar from head to toe. I was a beggar when I was born, and I’ll live as a beggar until I die.”

“……You really are a beggar.”

“Thank you for the compliment.”

“Gung Gibang, you beggar bastard.”

“Ah, how sweet.”

Hyuk Mujin glared at Gung Gibang as if he wanted to kill him, then spoke again.

“What about Young Hero Cheong?”

“Cheongpung is Cheongpung.”

Huashan Sect or not, Cheongpung was simply like that by nature.

At that one sentence, which contained everything, Hyuk Mujin muttered,

“That makes no sense, but somehow I understand…”

“There are too many people watching. Let’s finish this quickly.”

“How many?”

“Tell me. How many blows would it take for you to reflect on your actions?”

“Then… one?”

“Three.”

“Damn it. Understood.”

“You cursed, so five.”

“……Just hit me ten times. Beat me until I die.”

“I award bonus points for that determined attitude worthy of a martial artist. So one blow. How many?”

“One!”

Hyuk Mujin shouted his reply with all his might and thrust his forehead forward.

That was when it happened.

“You there. Stop.”

“……?”

I lowered my hand and turned around.

In the middle of the road, which had fallen silent enough to hear a mouse breathe, ten men and women riding in four-person sedan chairs were looking in our direction with gazes that mixed displeasure and interest.

Among them, all dressed lavishly as if to flaunt their immense wealth, one young man stood out in particular.

He was the owner of the voice I had heard moments earlier.

“I stopped. Why?”

The young man’s eyes went round at my question. He blinked for a while, as if unable to believe what he had just heard, then let out a quiet laugh.

“It seems you do not know who this Young Master is.”

“Do I have to know?”

“Have you ever seen such an arrogant bastard?”

The young man had not said that.

I looked at the man who had kicked off from the sedan chair and shot into the air.

*What is this now?*

Whoosh, clang!

After performing three somersaults in midair, the sparrow-eyed man landed and drew his sword, his eyes burning with fury.

The spectators gasped at the dazzling movement.

“You appear to be a wandering martial artist, but as if causing a disturbance in broad daylight were not enough, you dare to utter such insolent words to a person of—”

“You’ve put a lot of jewels on that. Are they meant to distract people?”

I stared at the jewels decorating his sword. Dozens of gems in a variety of colors were shining in the sunlight.

“What?”

“It’s dazzling. Put it away.”

Clang!

The sparrow-eyed man’s eyes widened.

The sword flew from his grasp when he failed to withstand the force of the finger flick I sent at him. It spun through the air and plunged deep into the ground.

“You fucking bastard. How dare you point a sword at someone so carelessly? And in broad daylight, no less.”

*Oh, look at this bastard running his mouth.*

He was probably somewhere around First Rate.

He seemed to have polished his skills to a decent level, but he was an extreme poseur obsessed with appearances.

“T-this bastard…!”

“And you were the ones making all the noise. I just made things quiet. Don’t make this more complicated than it needs to be. Just leave, all right?”

I was serious.

It was not as though this was the first time one or two flies had buzzed around me. If I was merely passing through rather than standing in front of my own home, there was no reason to spray bug killer at every mosquito that came at me.

It would be better to wave them away and continue on my way.

But no matter how sincerely you tried to explain something, there were always people who could not understand it the first time.

Shing, shing-shing!

Dozens of sword blades flashed from every direction. As martial artists from Qingxia Hall wearing blue silk martial uniforms surrounded us in layer after layer, a smug expression appeared over the sparrow-eyed man’s earlier panic.

“You appear to be a fairly well-known wandering martial artist, but even now, kneel and beg for forgiveness. Who knows? Perhaps the Young Master will show you mercy.”

I glanced over the sparrow-eyed man’s shoulder. The other men and women were watching us with bright, excited eyes, led by the young man who appeared to be their leader.

They looked exactly like spectators watching monkeys at a zoo.

“I don’t think the people over there have any intention of showing mercy.”

“What?”

“Of course, neither do I. And based on my experience so far, this is the most effective medicine. Isn’t that right?”

I slowly raised my fist, and the Bermuda Triangle, which had been watching only my expression, responded enthusiastically.

“Exactly. They won’t come to their senses until they’ve been beaten like dogs on the hottest day of summer.”

“I was the first one to take that medicine. I was cured immediately.”

“Benefactor, can I go buy some dumplings while you’re doing that?”

“No. Just stay there. It’ll be over soon anyway.”

Step.

“W-wait!”

As I took a step forward, panic filled the sparrow-eyed man’s eyes.

A Third Rate thug would charge in out of sheer stubbornness because he would not know his opponent’s level. But that man was a martial artist who had learned martial arts to a certain degree.

That was why he—and even the Qingxia Hall martial artists acting as decorative guards—had clearly realized that none of them were my match.

“W-we’re Qingxia Hall!”

“Oh. So?”

“D-did you say you’ve never heard of Qingxia Hall’s reputation?”

“Yeah. My hearing hasn’t been very good lately.”

Step.

“Stop! I said stop!”

“Ahem.”

Now the sparrow-eyed man was not the only one growing desperate.

A retainer of the Zhuge Clan, who had been watching the situation while clicking his tongue, cleared his throat and spoke.

“I will explain the situation, so perhaps it would be best if you stopped…”

Whack! Thud!

“Pardon me? What did you just say?”

“……”

The Zhuge Clan retainer looked back and forth between me, standing there with my fist clenched, and the sparrow-eyed man, who had passed out with his nose crushed.

He muttered awkwardly,

“I said it would be best if you stopped…”

“Pardon?”

“There may be various issues…”

“Pardon?”

“It would be better to avoid any unnecessary conflict…”

“What was that?”

“……Never mind.”

“Ah. Right.”

I wiped the blood from my fist on my trouser leg and looked around.

Gung Gibang was muttering that he had known that bastard would end up like this, while Hyuk Mujin’s expression was bright thanks to the extra years of life he had gained.

And Cheongpung…

“Hey! Where do you think you’re going?”

“Gasp, Benefactor!”

No way. Was that bastard actually going to buy dumplings right now…?

Seeing Cheongpung’s back as he slowly slipped away without making a sound, I began to wonder whether he was really human.

*I’m definitely catching that bastard.*

With that firm resolve, I took a step forward. The decorative guards surrounding us swallowed their breaths and moved aside.

But they were not the only Qingxia Hall martial artists present.

“Ha-ha-ha! This is amusing. Very amusing. Don’t you agree?”

At the young man’s laughing question, the four huge men carrying his four-person sedan chair answered in unison.

“Yes, my lord.”

“We cannot send off the benefactor who gave this Young Master such a good laugh. I am fine, so go and bring him here.”

“Loyalty!”

With a shout filled with internal energy, the huge men set down the sedan chair and charged toward me at a speed like the wind.

They had transformed from mere sedan bearers into outstanding Peak masters, attacking while covering all four directions.

Whoooooosh!

The moment each of their punches, infused with powerful energy, interlocked with exquisite precision and swung toward me—

Boom-boom-boom-boom!

With exactly four sounds of impact, four bodies sprawled face-first onto the ground at the same speed with which they had charged.

And they stayed down.

“What the sibu-leol?”

“……!”

“……!”

“……!”

Complete silence descended over the main road.

After lightly kicking the unconscious giants, I shrugged at the young man. The corners of his mouth, which had risen so high, were now trembling.

“Interesting. Very interesting. Don’t you all think so too?”

The Zhuge Clan retainer put a hand to his forehead, while Gung Gibang and Hyuk Mujin nodded mechanically.

“This is the most fun I’ve had in my entire thirty-year life as a beggar.”

“Captain, my belly button popped off from laughing. I can’t see where it rolled off to, so I’m still looking for it.”

“Yes, in these dry times, how could we simply send away the man who gave us such great entertainment? So…”

He pointed at the young man.

“Grab that bastard by the collar and bring him here.”

“Loyalty, loyalty!”

“I don’t know anymore. Whatever happens, you’ll handle it all yourself.”

Hyuk Mujin, who did not want to take even a single hit, burned with more enthusiasm than anyone else, while Gung Gibang stepped forward despite grumbling.

The situation had completely reversed from how it had begun.

When even the guards they had trusted were defeated, the men and women of Qingxia Hall began screaming at the tops of their lungs.

“You bastard! Do you know who I am?”

“You wretched scoundrel! Do you dare defy the laws of the Great Nation?”

“If you lay a hand on me, do you think my family will stand by and do nothing?”

I had only meant to grab one person, but these people were apparently set items that came attached in a chain.

I asked the first one who had shouted.

“Who are you?”

“I am the Young Bureau Head of the Daejuksan Escort Bureau…”

“Oh, Juksan Escort Bureau?”

“So you do know us!”

“I don’t, you sibu-leol bastard. Get down before I beat you until you’re a bowl of porridge.”

They might have thrown their weight around in Hubei Province, but if I had never heard of them, they were nobodies.

I continued quietly.

“If you get down now, I’ll only destroy the sedan chair. If you refuse, I’ll destroy your legs along with it. What’ll it be?”

The Young Bureau Head of the Daejuksan Escort Bureau widened his eyes and answered,

“I’ll get down.”

“You should have done that from the beginning. Why are your eyes so wide?”

“I’m sorry. If I don’t, I think I might cry…”

Ah. In that case, I accepted it.

After dealing with one of them easily, I turned to the sharp-voiced woman.

“What family did you say you were from?”

“Hmph! No matter how much of a scoundrel you are, surely you’ve heard of the name of the Hyungmun Sword Family!”

“Never heard of it. Stop talking nonsense and get down.”

“……!”

“Next. Where are you from?”

“I-I’m from the Eungseong Merchant Association…”

“Eungseong, Eung-poop, whatever. If you don’t want to be beaten until you shit yourself, get down too.”

“Yes, sir.”

After two or three of them climbed down from their sedan chairs, the rest began touching their feet to the ground one by one without even speaking.

All except one.

“So who are you?”

Every trace of laughter had vanished from the young man’s face. His eyes gleamed coldly.

“You have crossed a line you should never have crossed.”

“Looks like you crossed your own lifeline, too. So who are you?”

“Heh. What a ridiculous situation.”

The young man gave a hollow laugh, then shouted in a dignified voice,

“I, Ju Wongong, am a noble scion of the dragon’s blood and a third cousin of His Majesty the Emperor! If you know your crime, kneel even now!”

“Okay, Celestial Dragon.[^1] Get down.”

[^1]: The privileged world nobles in *One Piece*, infamous for treating ordinary people as beneath them.

“……!”
## Chapter artifact 454

# Chapter 454

The young man who had been frozen with his eyes wide open—or rather, Ju Wongong—asked in a trembling voice,

“W-what did you say?”

Had this bastard’s ears been plugged since earlier? He kept making me repeat myself.

Ignoring the people staring back and forth between Ju Wongong and me with their mouths hanging open, I spoke again.

“Get down.”

“I-I am Ju Wongong!”

“Whether you’re the main character or Ju Wongong, get down.”

“Though you are ultimately a subject of the Great Nation, how dare you show such disrespect to me, a member of His Majesty the Emperor’s bloodline?”

“I have a friend named Johnson. If he were here, he would have violated something else.”

“……!”

“I’ll say it one last time. Get down.”

Though he had no idea what I meant, anyone could sense danger.

Ju Wongong’s butt twitched instinctively, and he slowly rose to his feet.

Yet even as his eyes darted about anxiously at a situation he had never experienced before, he did not forget to issue threats until the very end. Perhaps he trusted in his imperial background.

“D-do you think you’ll get away with this?”

“Yeah. I think I will.”

“To insult an imperial relative? This is treason!”

“As long as it’s not hair loss.”

“What kind of bastard says things like that…!”

Although I answered casually, I was not entirely wrong.

The imperial family possessed the same Zhu surname as the Son of Heaven and carried the blood of dragons. That alone made them noble.

Even though the Murim and the government maintained a relationship of mutual noninterference, disrespecting or threatening an imperial relative was treated as a serious crime.

That was why the Zhuge Clan retainer had been groaning like a dog that needed to relieve itself.

“P-perhaps it would be best if you stopped now.”

I frowned at the retainer’s whisper.

“Why?”

“Pardon?”

“What did I do? I didn’t swear at him, and I didn’t threaten to kill him. He even attacked first. All I did was tell him to get down from the four-person sedan chair.”

“……Well, that is true when you look at it that way. But he is an imperial relative.”

“Imperial relatives come in all grades. If he’s an eighth-degree relative, doesn’t that mean he isn’t really related by blood, but merely has a few drops of blood somewhere in common? If I spit into the Yangtze right now, the Yangtze and I would probably be about eighth-degree relatives.”

“Gasp. Great Hero Jin, please.”

“It’s all right. I spoke quietly, so no one could have heard us anyway.”

At that moment, Ju Wongong, who had misunderstood our whispering, shouted in a triumphant voice,

“It seems you have finally grasped the gravity of the situation. But it is already too late. The imperial court’s hundred thousand troops will soon be dispatched to exterminate the nine branches of your kin, along with all other traitors!”

“Oh. A Buster Call.”

“What have you been saying this whole time, you traitorous bastard?”

“Gasp!”

“Eek!”

When unmistakable fury appeared in Ju Wongong’s eyes, the commoners swallowed their breaths and prostrated themselves on the ground. Some had already begun fleeing in every direction.

They seemed intent on avoiding involvement in a needless incident. That meant fewer eyes watching us, so I had no complaints.

*They keep threatening people with the nine branches of their kin whenever they get bored.*

Did they not bother with anything less?

As I let out a deep sigh, the Zhuge Clan retainer whispered,

“Do not be too frightened. His talk of a hundred thousand troops is only a bluff.”

“……Do you think I’m an idiot? Why would I believe that?”

“Master Ju was exiled for embezzling a fortune while throwing around his imperial authority. He has no intention of escalating the matter. So please apologize and withdraw at an appropriate point.”

“Wait. Exiled?”

“Yes.”

“Him?”

“He is an imperial relative. No matter how distant his branch may be, his blood cannot be ignored. Besides, he is a distant branch with no chance of inheriting the throne, so even when he commits a crime, they allow him to enjoy a certain amount of special treatment.”

“In short, he’s such a fucking nobody that no one around him even bothers with him?”

“……Great Hero Jin, please choose your words more carefully.”

I let the retainer’s complaint go in one ear and out the other, then gave a quiet laugh.

I had wondered why someone who was supposedly an imperial relative was socializing with a gang of thugs on a main road in Hubei rather than staying in the imperial palace. He was even more insignificant than I had imagined.

Though I had already guessed as much when he started talking about being an eighth-degree relative.

“First, I shall gouge out those arrogant eyeballs of yours for failing to recognize this noble self, then tear you limb from limb, and afterward—”

“Yeah, yeah, I get it. Let’s talk about the rest after you look at this.”

I threw an object from inside my robe at Ju Wongong as he delivered his long speech.

At the same time, the man who had been puffing out his chest flailed both arms and sat down hard.

“It’s a hidden weapon! A hidden weapon! This bastard is attempting to assassinate an imperial relative!”

“……Your level is truly something else.”

And then.

The “hidden weapon” landed with a soft clack in front of Ju Wongong’s feet, scattering a brilliant light beneath everyone’s gaze.

“Huh?”

Ju Wongong stared at the object before his feet with a puzzled look, then opened his mouth blankly.

“Huh? Huh? Huhhhhhh?”

It did not take long for his question marks to become exclamation marks, or for his anger to turn into shock.

He looked back and forth between me and the token of Prince Shangshan Zhu Bao, engraved with clouds and a dragon. Then he spoke heavily.

“I shall show you mercy and forgive you.”

“……”

What a load of crap.

* * *

“So you were on your way to Dongting Lake?”

“That is correct! No, I mean, yes, that is so!”

Ju Wongong nodded energetically at my gentle voice.

The decorative showpieces from Qingxia Hall whom he had hired were keeping people quiet alongside the government troops, who had arrived late. Meanwhile, Cheongpung, who had somehow succeeded in buying dumplings in bulk, opened his eyes wide at the mention of Dongting Lake.

“Wow! Dongting Lake!”

Ju Wongong had finally learned the identity of this dumpling ghost. His uneasy gaze flicked toward the sword hanging at Cheongpung’s waist.

“W-well, I could invite you along if you wished…”

I muttered,

“You don’t mean that at all.”

“That is a misunderstanding! No, I mean, you misunderstand.”

“Do you often misunderstand things in your daily life? You attacked people who were trying to pass peacefully, so it would seem that way.”

“That was… I shall apologize once again. I never dreamed that you possessed His Highness Prince Shangshan’s token.”

“Oh, I see. If I hadn’t had the token, you would have brought a hundred thousand troops to exterminate my nine branches of kin, gouged out my eyes, and dismembered me?”

“W-why would you say such a thing? Ha, ha-ha-ha.”

His forced laughter was almost pitiful.

*I didn’t know the token would have this much power, either.*

There was a reason Ju Wongong was being so humble.

Even animals distinguished between purebred and mixed-breed. How much more would the imperial family—the most noble bloodline in the world—care about such distinctions?

Even though the same imperial blood ran in their veins, Prince Shangshan Zhu Bao was the Son of Heaven’s only younger full brother and the sole prince he had personally appointed.

After the late Emperor’s death, the ruthless Emperor eliminated countless blood relatives in the struggle for the throne. Prince Shangshan Zhu Bao was that ruthless Emperor’s one soft spot.

Ju Wongong, on the other hand, was an imperial relative from a branch eight degrees removed.

The direct imperial line possessed legitimacy and authority. Even by counting degrees of kinship, Prince Shangshan Zhu Bao was a distant and exalted elder of the household to Ju Wongong.

*This is what they call using barbarians to defeat barbarians.*

Defeat barbarians with barbarians, and defeat a weak Celestial Dragon with a strong Celestial Dragon.

The chairman of my fan club was this formidable. The more I thought about it, the more my chest swelled with pride.

“Well, putting that aside, what are you planning to do at Dongting Lake?”

“W-well, the weather is nice, so I thought I would take a boat ride…”

At the unimpressed expression on my face, Ju Wongong hurriedly corrected himself.

“I intended to take a boat ride while also checking on the people’s welfare, since I heard the mood in Hubei Province has been rather grim lately.”

“……Shouldn’t you inspect your own life first? I heard you were exiled for siphoning off a fortune through back channels.”

“Ahem! Ahem!”

“And you brought all these people along for a boat ride? In times like these?”

Everyone with eyes and ears in Hubei Province was trembling with anxiety because of the ominous rumors that had continued without pause. Meanwhile, an exiled imperial relative was planning a luxurious boat ride on Dongting Lake.

If Mr. Current Situation heard about this and smashed Ju Wongong’s skull with a sledgehammer, Ju Wongong would have no grounds to complain.

*That’s rich people for you.*

I shook my head and rose from my seat.

The matter had been settled without too much noise, so I intended to leave without giving it any more thought. But Ju Wongong seemed to see things differently.

“W-wait a moment. Where are you going?”

“I’m a busy man. Why would I go boating on Dongting Lake? What is it?”

“If I have offended you, I shall apologize once again. In that spirit…”

Ju Wongong trailed off and gave a meaningful glance.

The Qingxia Hall martial artists who had been waiting in advance came forward carrying several ornate sedan chairs positioned among the procession.

The cloth curtains had not even been lifted, yet a faint fragrance slipped into my nostrils.

*Don’t tell me…*

There is an old saying: the thing you say “surely not” about is the thing that gets you. This time was no different.

“Show yourself.”

The moment Ju Wongong finished speaking, the sedan chair’s door slowly opened.

And then, when a woman carefully stepped down from the sedan chair, a quiet exclamation escaped my lips before I could stop it.

“……Huh.”

People often describe celebrities as pretty or handsome.

But the woman before me possessed something beyond those ordinary standards.

*Beautiful.*

Yes. That was probably the most appropriate word.

The woman was beautiful enough to make even me gasp in admiration, despite having already guessed Ju Wongong’s intentions.

Beautiful enough for Gung Gibang to hurriedly wash his face with spit, for Hyuk Mujin to lose himself in a daze, and for Cheongpung—who had been holding a meat dumpling in one hand and a vegetable dumpling in the other while trying to decide between them—to drop every single dumpling.

Amid the quiet shock flowing through the crowd, Ju Wongong’s voice reached me.

“She is the singing courtesan I keep at my side. As you can see, her beauty is worthy of being called the most beautiful in the world. She is also skilled in music, and anyone who hears her play loses himself completely.”

I was not so sure. It seemed as though she could steal a person’s soul without playing a single note.

Ju Wongong gave a quiet laugh at the admiration that could not be hidden from my face, then spoke to the woman.

“What are you waiting for? Hurry and greet him.”

Her red lips slowly opened.

“This humble girl is Honglan. It is my greatest pleasure to meet such an honored guest.”

“……Oh.”

“……Wow.”

“……Amazing.”

Before the shock of her appearance had even faded, exclamations arose from every direction.

Her voice was clear and pure, yet alluring.

Honglan. A woman whose name, meaning red orchid, suited her better than anyone.

*Of course, it wasn’t her real name, and she wasn’t an ordinary singing courtesan, either.*

Like most courtesans, including Wolhwa, Honglan was hiding her real name.

And unlike Ju Wongong, who did not know even a single martial move or half a stance, she had learned a small amount of martial arts.

—Lower District Sect?

Her slender shoulder twitched at my Sound Transmission, and Honglan gave a slight nod.

*The Lower District Sect. I had a feeling that was the case.*

After the Beggars’ Sect, the Lower District Sect possessed more disciples than any other sect.

Ju Wongong beside me did not seem to know that, but like the other Lower District Sect courtesans, Honglan had learned enough martial arts to protect herself.

“So? What do you think, Great Hero Jin? If you give me the opportunity, this Young Master will treat you properly. Of course, Honglan will sit beside you…”

*Let’s see you refuse to come along after this.*

That was written plainly across Ju Wongong’s smug face.

I stared at Honglan for a moment, then smiled and spoke.

“Forget it. Let’s each continue on our way.”

“Then we can all move somewhere else together, hm? W-wait. What did you just say?”

“Why are you so flustered? I’m pretty sure I said I had something urgent to do. Is my memory failing me?”

“N-no. But Honglan is here…”

I raised a hand and cut Ju Wongong off.

I had already wasted time by getting dragged into something pointless. If I were the kind of man who would lose his head over a beautiful woman and follow her somewhere, I would not have survived this long.

“Don’t overdo the partying, either. You’d be better off going home and staying quiet. See you.”

I was about to turn away after that final remark when Ju Wongong held something out to me.

“Wait! Then at least take this.”

“……?”

“I heard that His Highness Prince Shangshan received your autograph, Great Hero Jin. Please give me one as well…”

“……!”

At this rate, my fan café would be reaching Leaf Level 2 soon.[^1]

[^1]: Korean online fan communities often use graded membership tiers named after stages of a leaf’s growth.

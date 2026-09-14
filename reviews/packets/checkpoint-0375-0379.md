# Checkpoint Review — 375–379

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

## Chapter 374 Expedition

- This branch backfills Chapters 370–373 against the Chapter 65 anchor. Chapters 66–369 have no accepted local English translation here.
- Treat `docs/EXPEDITION_SEED.md` as bounded orientation, not as a substitute for missing translations. Do not read parked Chapters 374–375 while drafting 370–373.
- When the current Korean source conflicts with bridge context, the current source wins. Preserve uncertainty instead of inventing skipped-range backstory.
- After Chapter 373 is committed, run `python tools/expedition.py resume-parked` so the existing 374–375 translations remain the accepted line.

## Checkpoint summary

# Chapters 375–379

## Plot

Tang Sadok awakens and confesses that he revealed the Myriad Poison Ring’s location to the Western Heaven Demon Lord to protect the Sichuan Tang Clan. Taekyung forgives him, completing the Hidden Quest **Atonement and Forgiveness** and earning the **Benefactor of the Tang Clan** Title, EXP, Fame, and a level up. Tang Sadok transfers the Myriad Poison Ring to Taekyung, making it bound. The Divine Physician asks Taekyung for time before his departure, while Cheongpung becomes Mimi’s temporary guardian.

Taekyung and his companions leave the Sichuan Tang Clan amid a massive farewell. Mungyeong’s disciple Dongbong recalls how Mungyeong cured him after an epidemic killed his wife and children. Dongbong asks Mungyeong to prevent the great war he expects to come, but Mungyeong insists that his place is outside the Murim. At Chengdu’s western port, Taekyung accepts an unidentified boy as a last-minute passenger aboard the Water Dragon Stronghold’s ship.

The Sichuan Governor’s concubine Ae-hyang manipulates him into concealing the government’s involvement in the recent conflict and submitting an inflated report. A sinister red light appears in her eyes, implying an unidentified superior’s influence. During the voyage, Taekyung identifies the surviving Black Dragon Armor fragment, renames it **Flame Dragon Armor** after infusing it with Scorching Yang Qi, and learns that it repairs itself by consuming his internal energy. He then completes Logout.

Taekyung awakens aboard a private jet returning to the modern world, with Chengdu International Airport under monster attack. Around a dozen A-rank wyverns pursue the aircraft. With Team Leader Choi maintaining a pressure-sealing barrier, Taekyung cuts open the hull using an Aura Blade and kills Black Star and several wyverns with a spear. The survivors retreat, promising revenge.

At the airport, twenty-year-old Hunter Shao Shen leads Chinese Hunters and soldiers against a monster army. A green wyvern’s Poison Breath kills the command staff, after which dark magic spreads through blood and corpses, resurrecting the dead as bound undead. Shao Shen kills his friend Yao Wei after Yao is transformed into a headless Dullahan. As the defenders near defeat, Taekyung’s burning airplane sweeps toward the battlefield.

## Continuity

- Taekyung forgave Tang Sadok, completed **Atonement and Forgiveness**, gained the **Benefactor of the Tang Clan** Title, and received EXP, Fame, and a level up.
- The Myriad Poison Ring is now bound to Taekyung. His bound items include White Flame, Myriad Poison Ring, and Flame Dragon Armor.
- Tang Sadok is awake and again serving as Family Head of the Sichuan Tang Clan; the clan owes Taekyung’s group a significant debt.
- Cheongpung is temporarily responsible for Mimi while the Tang Clan’s future remains uncertain.
- The Divine Physician has asked Taekyung for time, but the matter remains undisclosed.
- Mungyeong is both the Divine Physician and the Slaughter Saint; Dongbong is his longtime disciple. Mungyeong verbally refuses to intervene in the coming war, though his ultimate choice remains unresolved.
- An unidentified boy boarded Taekyung’s departing ship at Chengdu’s western port.
- Ae-hyang is secretly influenced by an unidentified superior; the Governor’s false memorial and its consequences remain unresolved.
- Logout succeeded. Taekyung has returned to the modern world aboard a Central Committee of China jet bound for Chengdu International Airport.
- Team Leader Choi can maintain a pressure-blocking barrier. Taekyung’s sword qi is called an Aura Blade in the modern world.
- The Lich is suspected of extending its reach to Chengdu, but its exact role in the attack is unconfirmed.
- Black Star and several pursuing wyverns were killed; surviving wyverns escaped and seek revenge.
- Shao Shen is a twenty-year-old spear-wielding Hunter of the Public Security Armed Forces. Yao Wei was his A-rank friend and comrade before becoming a Dullahan.
- The airport’s undead army is created and controlled through dark magic, but the controlling beings’ identities remain unknown.
- The burning aircraft’s passengers, its impact on the monster army, and Taekyung’s immediate fate remain unresolved.

## Translation Decisions

- Preserve **Atonement and Forgiveness**, **Benefactor of the Tang Clan**, **Myriad Poison Ring**, **Flame Dragon Armor**, **Divine Physician**, **Slaughter Saint**, **Dongbong**, **Water Dragon Stronghold**, **Aura Blade**, **Black Star**, **Shao Shen**, **Yao Wei**, **Dullahan**, **Public Security Armed Forces**, and **Chengdu International Airport**.
- Render **술시** as **the Hour of the Dog**, with a footnote identifying it as approximately 7–9 p.m.
- Render **식경** as **sikgyeong**, approximately thirty minutes, with a footnote.
- Render **강기** as **sword qi**, **오라 블레이드** as **Aura Blade**, **흑룡갑** as **Black Dragon Armor**, and **화룡갑** as **Flame Dragon Armor**.
- Render **수룡채** as **Water Dragon Stronghold**, **열화신공** as **Blazing Flame Divine Art**, **선화아** as **boatman**, and **무송** as **Mu Song**.
- Retain Mungyeong’s distinction between his physician identity and his slaughter-demon past; preserve the chapter’s casual banter and Taekyung’s self-mocking narration.

## Durable state

{
  "active_continuity": [
    "By the end of the source-only bridge, Jin Taekyung had reached the Supreme Peak realm and Level 120; this chapter grants him another level up, but the resulting level, exact current Fame, Titles, martial-art stages, and unassigned points are not stated.",
    "Jin Mukyung is Taekyung's second older brother, twenty-three, the Heaven Shaking Sword, a Peak-level martial genius, and substantially stronger than Taekyung.",
    "Dark Heaven rescued the former conspirators from the Demonic Cult, implanted gu in them, and its larger purpose and reason for sparing Taekyung remain unresolved.",
    "The Sichuan Tang Clan, Qingcheng Sect, and Emei Sect were devastated by the recent Dark Heaven attacks; Tang Sadok has awakened and is again serving as Family Head of the Sichuan Tang Clan.",
    "Tang Sadok confessed that he revealed the Myriad Poison Ring's location to the Western Heaven Demon Lord to preserve the Tang Clan; Taekyung forgave him, and the Tang Clan owes Taekyung's group a great debt.",
    "Taekyung completed the Hidden Quest Atonement and Forgiveness and acquired the Benefactor of the Tang Clan Title, along with EXP, Fame, and a level up.",
    "The Myriad Poison Ring was transferred to Taekyung by Tang Sadok and is now bound to him; White Flame, Myriad Poison Ring, and Flame Dragon Armor are currently bound.",
    "Mungyeong is the Divine Physician and the Slaughter Saint. He has left the Murim's affairs behind, intends to live as a physician, and is the master of Dongbong.",
    "Dongbong is Mungyeong's longtime disciple and a physician who lost his wife and two children to an epidemic before Mungyeong cured him and accepted him as a disciple.",
    "A hidden, currently inactive transport formation associated with Dark Heaven was found near Sichuan; its origin and function remain unresolved.",
    "Jin Wikyung has proposed relocating the Sichuan Tang Clan and has been assigned to escort Samgoe toward Henan.",
    "Taekyung has successfully completed Logout and returned to the modern world aboard a private jet sent by China's Central Committee toward Chengdu International Airport.",
    "Cheongpung is Mimi's temporary guardian while the Tang Clan's future is uncertain.",
    "The Divine Physician, referred to in Taekyung's joke as Dongbong, has asked Taekyung for time before his departure; the request remains undisclosed.",
    "Dongbong predicts that a great war will soon occur and asks Mungyeong to prevent it as the Divine Physician; Mungyeong verbally refuses and says the Murim is not where he belongs, while the announced departure from Chengdu's western port remains unresolved.",
    "Taekyung and Cheongpung were preparing to leave Sichuan by fast ship from Chengdu's western port after the Hour of the Dog.",
    "Mu Song is the boatman associated with the water bandits preparing the ship.",
    "An unidentified boy reaches the port immediately before departure and is accepted as one more passenger.",
    "The Sichuan Governor's favorite concubine Ae-hyang manipulated him into concealing the government uniforms and weapons involved in the recent martial-artist conflict and preparing a false memorial that exaggerates his role in restoring order. A sinister red light entered her eyes, and she appears to serve an unidentified superior.",
    "Chengdu International Airport is under attack by monsters, with humans and monsters fighting on the ground while around a dozen A-rank wyverns pursue Taekyung's private jet.",
    "Taekyung concludes that the Lich, the supreme undead monster associated with the recent monster wave, has extended its reach to Chengdu.",
    "Team Leader Choi accompanies Taekyung, trusts him to resolve the attack, and can create a pressure-blocking barrier with a ring.",
    "Taekyung cuts an opening in the aircraft with sword qi, called an Aura Blade in the modern world, and kills the lead wyvern and multiple others with a spear.",
    "Shao Shen is a twenty-year-old spear-wielding Hunter of the Public Security Armed Forces who rallies Chinese forces at Chengdu International Airport.",
    "Yao Wei was an A-rank Hunter, Shao Shen's friend and comrade, and a playful sparring partner before being killed and reanimated as a Dullahan.",
    "A monster army unexpectedly attacks Chengdu International Airport, including low- and high-level monsters, A-rank flying monsters, and a green wyvern capable of using Poison Breath.",
    "Dark magic spreads through battlefield blood and corpses, restores the dead with strength and souls, and binds the resulting undead to invisible chains.",
    "The identity of the beings controlling the undead army is not established.",
    "A burning airplane enters the battlefield and begins sweeping through the monster army; its passengers, identity, and final outcome remain unresolved."
  ],
  "continuity_sources": [
    379
  ],
  "open_questions": [
    "The outcome of Taekyung's spar with Jin Mukyung remains unresolved in the accepted local anchor.",
    "Dark Heaven's agents, purpose, and connection to the transport formation remain unresolved.",
    "The Sichuan Tang Clan's relocation decision and destination remain unresolved.",
    "The outcome and timing of the planned Samgoe escort to Henan remain unresolved.",
    "The matter the Divine Physician wants to discuss with Taekyung before his departure remains unresolved.",
    "The identity of the boy who arrives at the port and whether he will accompany Taekyung's group remain unresolved.",
    "Whether Mungyeong will ultimately intervene in the coming war or leave the Murim remains unresolved.",
    "The identity of Ae-hyang's superior and the nature of her sinister red-eyed influence remain unresolved.",
    "Whether the Sichuan Governor submits the false memorial and what consequences follow remain unresolved.",
    "The Lich's exact role in the Chengdu attack and the extent of its reach remain unresolved.",
    "Whether Taekyung's private jet survives the ongoing wyvern attack remains unresolved.",
    "The identity of the beings controlling the undead army is unresolved.",
    "The identity of the burning airplane's passengers and the outcome of its attack on the monster army are unresolved."
  ],
  "safe_through": 379,
  "temporary_decisions": [
    "This expedition deliberately skips accepted translation of Chapters 65–370.",
    "Chapters 371–373 are source-only bridge summaries and must not be treated as complete English continuity.",
    "When bridge context conflicts with the current Korean source, preserve the current source and record the uncertainty.",
    "Use Reformation Fist for 갱생권, grappling technique for 금나수, and retain hyung for 형 where the accepted anchor requires them.",
    "Render 반 시진 and 한 시진 as half a shichen and one shichen, with a footnote explaining that a shichen is a traditional two-hour period.",
    "Render 종형 as older cousin in this chapter's family context.",
    "Render 사죄와 용서 as Atonement and Forgiveness, 당문의 은인 as Benefactor of the Tang Clan, 백염 as White Flame, 동봉 as Dongbong, and 신의 as Divine Physician.",
    "Render 인산인해 as “a sea of people.”",
    "Render 홍무 as Hongwu and 성도 as Chengdu.",
    "Render 술시 as the Hour of the Dog, with a footnote identifying it as a traditional period roughly corresponding to 7–9 p.m.",
    "Render 선화아 as boatman and 무송 as Mu Song.",
    "Retain Master for 스승님 and render 살귀 as slaughter demon in Mungyeong's self-description.",
    "Render 식경 as sikgyeong, approximately thirty minutes, with a footnote.",
    "Render 흑룡갑 as Black Dragon Armor, 화룡갑 as Flame Dragon Armor, 수룡채 as Water Dragon Stronghold, 열화신공 as Blazing Flame Divine Art, 상산왕 as King of Shangshan, and 삼공 as Grand Councilor.",
    "Render 최 팀장 as Team Leader Choi, 리치 as Lich, 스켈레톤 워로드 as Skeleton Warlord, 샤오 양 as Xiao Yang, 중국 중앙위원회 as Central Committee of China, 쓰촨성 as Sichuan Province, 청두 국제공항 as Chengdu International Airport, 헌터 마켓 as Hunter Market, and 검은 별 as Black Star.",
    "Render 와이번 as wyvern, 드레이크 as drake, 용족 as dragonkin, 브레스 as Breath, 강기 as sword qi, and 오라 블레이드 as Aura Blade.",
    "Retain a footnote explaining 빵즈 as a derogatory Chinese slur for Koreans.",
    "Render 샤오 쉔 as Shao Shen, 야오위 as Yao Wei, and 류인친 as Ryu Inchin.",
    "Render 공안 무력부 as Public Security Armed Forces, 인민 해방군 as People's Liberation Army, 중화인민공화국 as People's Republic of China, 중화 as Zhonghua, 오성홍기 as Five-Star Red Flag, and 듀라한 as Dullahan."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 375

# Chapter 375

Even visiting the sick had a proper order.

When word spread that Tang Sadok—the Family Head and elder of the clan—had awakened, the members of the Tang household dropped everything and came running.

But not all hundred-plus people could see him.

“Benefactor, when can we see Grandpa Tang?”

“I don’t know. The people ahead of us have been in there for a while, so they should be coming out soon.”

“Oh, I see.”

Cheongpung nodded at my answer.

Wait. Cheongpung?

“What are you doing here? When did you get here?”

“Just now.”

He had slipped into the conversation so naturally that I hadn’t even noticed him. But why had this guy come here?

As though he had read my thoughts, Cheongpung pointed to his chest.

“Mimi said she wanted to see him.”

“……?”

*What the hell did I just hear?*

Now they could even communicate. Was this bastard from Slytherin instead of Huashan?

At my suspicious gaze, Cheongpung tilted his head.

“Why are you suddenly staring at my forehead? Is there something on it?”

“I was just checking whether you had a lightning-shaped scar.”

“What?”

“It’s a thing.”

The moment the words left my mouth—

Clunk.

The tightly shut door of the medical ward opened, and more than ten people emerged.

They were among the few remaining direct descendants of the Sichuan Tang Clan. Tang Horyong, whom I had met before, was among them.

“Hoo……”

He looked up at the sky with bloodshot eyes, then walked toward us.

“The Family Head wishes to see you.”

“We’ve been waiting.”

Jin Wikyung nodded and led the way. Cheongpung and I followed him into the medical ward.

Who knew how long we walked through the pervasive smell of medicinal decoctions? At last, a physician with his nose and mouth covered by white cloth led us into a treatment room, where we came face-to-face with several familiar faces.

“Cough. You’ve come.”

One glance was enough to tell that Tang Sadok, laboring through a faint cough, was in serious condition.

His limbs were broken, and his internal injuries had left his qi unstable.

He tried to sit up, but the Divine Physician, who had exchanged nods with us, stopped him.

“Family Head, didn’t I tell you not to move?”

“This old man is a sinner. I committed a crime deserving of death, so it is only right that I ask for punishment.”

Pale-faced, Tang Sadok shook his head, stared straight at me, and continued.

“I will make no pathetic excuses. The Western Heaven Demon Lord went to the underground prison because I told him about it.”

I crossed my arms at a slant.

“Ah. That explains it.”

“……?”

“Why?”

Tang Sadok asked, looking bewildered.

“Ah, you knew?”

“Of course I didn’t know at first. There was too much going on at the time. But later, when I thought about it carefully, I started wondering how that bastard, the Western Heaven Demon Lord, had known the location of the Myriad Poison Ring.”

Only a handful of people knew its location in the first place.

Cheongpung might look as light as a flower petal, but he was as solid as a tree root. That left Tang Sadok as the only person who could have revealed it.

“Why did you do it?”

“He said he would preserve our family line if I told him where the Myriad Poison Ring was.”

“And you believed him?”

“This old man was foolish. My judgment was clouded for a moment, and I did something I never should have done.”

“At least you know that.”

Tang Sadok’s eyes trembled as he looked at me.

“Surely heaven spared this old man so that I might apologize to all of you and receive my punishment.”

“What punishment do you want, then?”

The cold voice that suddenly rang out belonged to Jin Wikyung, who had been listening in silence.

“Are you the Lesser Family Head of the Jin Family of Taiyuan?”

“Yes. I am also the older brother who raised my two younger brothers as though they were my own children.”

Unconcealed anger clung heavily to Jin Wikyung’s deeply sunken eyes.

“It was something no one who walks the righteous path should ever have done.”

“I know. No—I understand. That is why I ask to be punished.”

“What would you do if I told you to take your own life?”

“……!”

Everyone, myself included, looked at Jin Wikyung in surprise.

Everyone except Tang Sadok.

With an utterly calm expression, he spoke.

“I abandoned righteousness, but because all of you risked your lives to fight for us, my family line will endure. If this worthless old man’s life can serve as an apology, I will gladly give it.”

After a brief silence, Jin Wikyung sighed.

“Hoo……”

He regarded Tang Sadok with a complicated look, then turned to me.

“What will you do?”

“……About what? His suicide?”

“Whatever you wish.”

Having the hilt of a knife suddenly thrust into my hand made my heart feel strangely taut.

Especially when the life hanging from the other end belonged to the Family Head of the Sichuan Tang Clan.

*Would you look at how suddenly the mood turned cold.*

Of course, this wasn’t something I could laugh off. I wasn’t some fair-minded, magnanimous Great Hero of benevolence and righteousness. To be honest, when I realized the full truth of what had happened, anger had quietly welled up inside me.

After all, everyone’s lives had been on the line at the time—not just mine.

But……

“That’s enough. I don’t want to take it that far.”

That was right. On the other hand, I could understand Tang Sadok’s position.

If, as the head of a family, I had to weigh outsiders I’d met only a few times against blood relatives I was duty-bound to protect with my life, I probably would’ve made the same choice.

*Besides, I owed him.*

Tang Sadok’s help had played a major role in allowing Jeok Cheongang to wake up.

There may have been some sort of deal involved, but Tang Sadok had still lent us a sacred artifact whose existence he hadn’t revealed even to his own blood relatives.

“So let’s call it even. We’ll let it slide. No, that’s going too far—let’s say the Sichuan Tang Clan owes us a huge debt over this.”

When I finished, Cheongpung and the Divine Physician spoke up.

“It was definitely Grandpa Tang’s fault that Benefactor was put in danger, but… I’ll follow Benefactor’s wishes too.”

“I have already forgotten the matter. But if I have one wish as a physician, it is that the Family Head recover as soon as possible. After all, there are still surviving members of his household.”

Jin Wikyung spoke last. Unlike before, there was no anger left in him.

No—perhaps he had known what my answer would be from the very beginning.

“So that is their decision. What do you think, Family Head?”

“……!”

Tang Sadok’s eyes trembled with emotion as he looked at us.

After a short silence, a hoarse voice slipped between his lips.

“This old man—and the Sichuan Tang Clan—owe all of you a great debt of gratitude.”

The instant Tang Sadok bowed his head with genuine sincerity—

> **System**
>
> Confessing one’s sins is difficult, but there is something that requires even greater courage. That is forgiveness.
>
> **Hidden Quest:** **Apology and Forgiveness** successfully completed!
>
> **Level 115 Tang Sadok** expresses his deep gratitude for your kindness. He and the **Sichuan Tang Clan** will never forget the kindness and assistance you showed them today, and the people of the **Sichuan Tang Clan** will remember you as their **Benefactor**!
>
> **Title Acquired:** **Benefactor of the Tang Clan**
>
> You have gained a tremendous amount of EXP and Fame as a reward for completing the Hidden Quest!
>
> **Level Up!**

*What was this? A Hidden Quest, all of a sudden?*

As I stood there dumbfounded by the System notification that had suddenly rung out, something cold brushed between my legs.

Sssrik. Sssriririk.

“Mimi, you little……”

At the sight of Mimi and Tang Sadok reunited after so long, I remembered something I had momentarily forgotten.

“Ah, now that I think about it, the Myriad Poison Ring. Thankfully, I’ve been keeping it safe all this time……”

“Is that so?”

Tang Sadok cut in before I could finish.

“Then continue to keep it.”

“Yes, then I’ll keep—what?”

“I am entrusting our family’s sacred artifact to you. It is a token of gratitude for our Benefactor, so please do not refuse.”

> **System**
>
> According to the owner’s wishes, **Myriad Poison Ring** has been transferred to you!
>
> A new item is now bound to you!
>
> **Currently bound items:** **White Flame**, **Myriad Poison Ring**, **???**
>
> You have a bound item that has not yet been named. Please give it a new name.

*What kind of day was today?*

I was getting downright nervous, wondering what kind of shitty things were about to happen for them to be giving so much away like this.

At the sight of me opening and closing my mouth like a goldfish, Tang Sadok smiled faintly.

“If any of you desire something, speak. I will grant anything within our family’s power.”

The Divine Physician smiled along with him.

“If there is something I desire, it is simply for the patients to recover as soon as possible.”

“Good heavens.”

That was certainly an answer worthy of the Divine Physician. No, should I be calling him Dongbong now?

But one thing was certain: he, too, was another Divine Physician.

“What do you want?”

Cheongpung jumped at the sudden question.

“M-Me?”

Tang Sadok nodded, and Cheongpung answered while fidgeting with his hands and feet.

“Well, I… Let me think. Um. Nothing.”

“Are you sure?”

“Yeees. I don’t think there’s anything.”

“……”

“……”

*Hey, you idiot. Take your eyes off Mimi-chan and talk.*

I wanted to bring him a mirror and show him his own face. His eyes brimmed with aching longing and desire for Mimi-chan.

*At this rate, he’s going to stare a hole through the snake’s hide.*

Just then, Tang Sadok spoke.

“This creature is an old friend of mine. For the past several decades, she has been the only one with whom this old man could share the joy, anger, sorrow, and pleasure he could reveal to no one else.”

Cheongpung looked at Tang Sadok with pity.

“So you don’t have any other friends, Grandpa Tang.”

“I never made any. Being the Family Head of the Tang Clan was that kind of position.”

“So you have no friends.”

“It wasn’t that I had none. I could have made them, but……”

“You didn’t have a single friend. How pitiful.”

“……”

The Divine Physician hurriedly grabbed Tang Sadok by the shoulders.

“Family Head, calm down. You’re breathing too quickly!”

“Huuk, hoo-oo.”

“Take deep, slow breaths. Come on, follow me. One, two……”

“Huooooo……”

A little while later, after narrowly escaping a hypertensive crisis, Tang Sadok looked at Cheongpung and spoke again.

“But as for Mimi, perhaps you……”

Cheongpung covered his mouth with both hands.

“No, Grandpa Tang. I can’t take away your only friend.”

“……I haven’t said I’m entrusting her to you yet.”

“Oh. Oh!”

Tang Sadok let out a deep sigh. It had only been for a moment, but he had undoubtedly wondered whether he could entrust Mimi-chan to someone like that.

“Yes, just as you guessed. Since we do not know what path our family will take from here on, I wish to entrust Mimi to you. Temporarily, of course.”

“Yaaay!”

“Did you hear the last part? Temporarily.”

“Yaaay!”

*I’ll bet Hyuk Mujin’s right wrist that he didn’t.*

Now Mimi’s temporary guardian, Cheongpung was beside himself with joy.

“Don’t worry. I’ll take good care of her!”

“From what I saw last time, Mimi does seem fond of you, but she is temperamental by nature and extremely wary of strangers, so……”

“Mimi. Do Whirlwind, then spin round and round and say hello!”

Sssriririk!

“Holy shit.”

*He busted out a new trick right here.*

Jin Wikyung, half stunned by the sight he was seeing for the first time in his life, muttered in a dazed voice.

“It seems you have nothing to worry about, Family Head.”

An earthquake shook Tang Sadok’s eyes.

Tang Sadok asked Jin Wikyung to stay behind for a private conversation, while Cheongpung and I left the room first.

No, one person had just been added.

“Young Hero Jin. Could you spare this old man a little of your time?”

“Me?”

The Divine Physician nodded with a gentle smile.

“There is something I very much wish to ask of you before you leave.”
## Chapter artifact 376

# Chapter 376

A sea of people.

There was no other way to describe the scene.

Word had spread that the Sleeping Dragon of Shanxi—or rather, the Blazing Fire Divine Dragon, Jin Taekyung—and the Huashan Divine Dragon, Cheongpung, were leaving, drawing people in like clouds.

Not only martial artists, but fearless commoners as well, had come out to see them off. The crowd stretched farther and farther, an endless tail that could not be counted.

“Safe travels, Blazing Fire Divine Dragon!”

“The martial world of Sichuan will never forget you!”

“It’s a snake with horns! The Huashan Divine Dragon has a snake with horns!”

“Whoa! The snake just did a somersault in midair!”

“The Fire King! The Fire King is holding the snake and trying to set it on fire!”

The murmuring noise gradually faded as the procession moved farther away.

On a deserted hilltop, a boy sat on a tree stump watching it all. He suddenly spoke.

“We’ve come a long way.”

“We certainly have. It’s tiring.”

At the sight of the old disciple plopping down on the grass with ragged breaths, the boy, Mungyeong, muttered,

“…We really have come a long way.”

He was not talking about distance. Mungyeong was talking about the years they had traveled through.

“Do you remember when we first met?”

“How could I forget?”

The old disciple wiped the sweat from his brow as though the scorching sun of that day were beating down on him once more.

“The first year of Hongwu. That exceptionally hot summer.”

It was the year the civil war over the imperial throne ended and a new emperor ascended.

The young, ambitious emperor changed the era name and sought to enact reforms, but the people were too exhausted by the long civil war to heed his will and take part.

“Rebellions broke out across the land, and bandits ran rampant.”

“Drought struck, and swarms of locusts swept across the plains. The corpses of government soldiers and rebels lay everywhere, and epidemics raged.”

“Yes. It was truly an age of turmoil.”

Death bred more death, and soon it devoured the entire continent.

A young carpenter surnamed Dong could not escape the dark shadow that hung over the land, either.

“I still think about those days from time to time.”

The decades had changed more than just the landscape. The young carpenter who had lost his beloved wife and two children to the epidemic had since become an old physician.

“I wonder whether I could have saved my family if I’d been just a little faster. If I’d found you sooner.”

“Do you regret it?”

“Yes.”

Sitting on a hill close to the heavens and gazing at the drifting wisps of cloud, the old physician’s eyes became those of the young carpenter once more.

“I will for as long as there is breath in my body.”

It had been only a single day.

By the time the carpenter, dragging along his plague-stricken body, brought back the nameless old physician who had been staying in the slash-and-burn settlers’ village, everything was already too late.

He wept for an entire day, then dug a pit in which to bury his family. Afterward, he made one request of the physician he had brought.

“Bury me with them. That was what I asked.”

Mungyeong answered in his blunt voice.

“And so I slapped you across the face.”

“It hurt. Enough to make me want to die.”

It had hurt. Not because of pain that threatened his life, but because he could no longer see his beloved wife and children.

“You were the one who helped me to my feet, Master.”

Mungyeong shook his head.

“I merely held out my hand. You were the one who chose to take it and stand.”

“I had to live. I had something to do.”

The carpenter should have died from the epidemic as well.

But the physician cured him with medical arts unlike anything he had ever seen. For the first time, the carpenter realized that even a mere human could alter the birth, aging, sickness, and death ordained by heaven.

“I can still see it clearly. You kneeling before me and asking me to accept you as my disciple.”

“I remember it differently. I remember you beckoning me to follow you, Master.”

Thus, the young carpenter who had lost his family found a new goal, while the old physician who traveled the world caring for helpless, impoverished patients gained a new disciple.

It was only much later that Dongbong—the carpenter, by then a physician himself—learned his master’s true identity.

“Slaughter Saint… It is a truly terrifying sobriquet. That was the first time you felt like a stranger to me, Master.”

Mungyeong gazed into the distance, his gaze emotionless.

What he was about to ask was something he had never once asked his disciple.

“Why didn’t you leave?”

“Did you think I would leave you?”

“I have taken countless lives over the years. I was nothing more than an ugly slaughter demon hiding my past. I would have understood if you had left.”

“Perhaps I really might have. But I knew all too well what kind of person you were, Master.”

A moment later, the old disciple continued quietly.

“The Divine Physician. My master is known as the Divine Physician. You are not someone who would kill without reason.”

“…!”

Mungyeong’s eyes trembled.

It was a truth he had never told anyone—and one no one had ever been willing to acknowledge.

He had lived as an assassin, taking countless lives with his own hands, whether they belonged to the orthodox faction, the unorthodox faction, or the Demonic Cult. And every one of those people had had a reason they deserved to die.

A Great Hero of the orthodox faction, renowned for his fairness and integrity, had made a hobby of raping and murdering women. A master of an unorthodox faction had slaughtered an entire village for fun.

If the army of the Demonic Cult invading the Central Plains had not killed and destroyed indiscriminately, and if the greatest assassin under heaven had not stepped forward to kill those infamous demon heads because he could no longer stand by and watch, he could never have been called the Slaughter Saint.

“If I had not fought the Demonic Cult, the entire world would have pointed fingers at me. Just as it had always done.”

The sobriquet Slaughter Saint was merely absolution granted by the orthodox faction that now ruled Murim—and praise for a man of great strength.

Mungyeong had always been Mungyeong, yet people neither knew nor cared to know the truth hidden beneath the surface.

“Why didn’t you tell them?”

“It is all in the past. I wished to leave Murim, so I became a physician as I had intended. And I will remain one.”

Mungyeong slowly rose to his feet. By then, the long procession that had left the Sichuan Tang Clan had disappeared into the distance.

“Let’s head down. There are patients waiting for us.”

He had just started walking, his voice dry, when—

“A great war will break out soon.”

Mungyeong stopped dead. Behind him, the old disciple continued.

“The same thing that happened back then will happen again. Countless people will die or be injured. People who have lost their parents or children will be everywhere, and the screams and deaths will never end.”

“…I suppose I’ll be very busy. I should make preparations.”

“You know what I am trying to say, Master.”

“I do not want to know.”

“Master.”

“I am a physician. Though I broke the promise I made to myself and took lives when I had no other choice, I will never make that mistake again.”

Mungyeong continued slowly.

“Fighting is their duty, and treating the sick is ours. In my heart, I left Murim long ago.”

“Then why have you never abandoned your martial arts?”

“…!”

Mungyeong was at a loss for words.

It was a question he himself had carried for a long time. If he had wanted to leave the Murim because he hated killing, then it should have been right for him to abandon martial arts as well—the means by which he killed.

Yet his martial arts had advanced even further. It was proof that he had been unable to let go of his attachment to them.

*Why was that?*

The old disciple’s voice broke through his brief reverie.

“You can treat hundreds, even thousands, of patients, Master. At the same time, you are capable of saving tens of thousands of lives.”

“…”

“Please prevent the coming war—not as the Slaughter Saint, but as the Divine Physician. This disciple will care for the patients here.”

Mungyeong suddenly lifted his head and looked at the sky.

It was clear and blue. Seven days and nights earlier, when the Sichuan Tang Clan had been dyed in blood, the sky had been filled with dark clouds.

“The sky is clear.”

In his blunt voice, he resumed his halted steps.

“I should go check on the patients. Take your time coming down.”

As he descended the hill, Dongbong’s voice scattered behind him.

“The Hour of the Dog. They said they would depart from Chengdu’s western port then.[^1]”

“Pointless. The Murim is not where I belong.”

Yet as the old disciple watched his master’s back recede into the distance, a faint smile formed on his lips.

“Please… be well.”

Whoooosh.

A wind blew from somewhere, sweeping between the two men.

* * *

“What are you looking at so intently?”

At Hyuk Mujin’s question, I turned away from the crowd surrounding the port.

“Nothing. Just in case.”

“Then what are you looking at?”

“You little pest. Why are you interrogating me like this? If I say it’s nothing, take it as nothing.”

Hyuk Mujin gave me a knowing smile.

“I actually know why you’re acting that way, Squad Leader.”

“…?”

I froze for a moment. How the hell did he know? Even Cheongpung hadn’t heard the conversation between the Divine Physician and me.

*Since when was this guy so perceptive?*

As I wondered about it, he whispered,

“Weren’t you looking at the young lady standing fourth from the right in the front row?”

“…”

“She is pretty, that’s for sure. She looks like the daughter of a fairly wealthy family. If you give me permission, Squad Leader, I could quietly go over there as your right-hand man and arrange a separate—”

“Mujin.”

“Yes? Ah, do you prefer meeting women naturally? If so…”

“Do you want to sink to the bottom of the Yangtze?”

“…!”

“Stop talking nonsense and keep lying there. And don’t puke later because you get seasick.”

“…Yes, sir.”

As Hyuk Mujin quietly shrank in on himself, Gung Gibang snickered.

“What a fool. It’s not the fourth woman on the right, but the third on the left. Anyone can see she’s much prettier. Your eyes must be crooked.”

“Want me to make them crooked for real?”

“…Sorry.”

“Let’s live like human beings. Like human beings.”

With a sigh, I shook my head and gave the crowd gathered like clouds one last sweeping look.

They were both definitely pretty, but the third woman from the left was more my type—

*No. That’s not what this is about.*

*Damn it. Those idiots wouldn’t shut up about them, and now I can’t stop looking.*

Just then, a towering, bronze-skinned man approached me.

“Hey there, junior. No, not junior. Young Hero Jin. No, Great Hero.”

*What is this, buffering?*

I offered a solution to the boatman Mu Song, who was switching forms of address at lightning speed.

“Just call me junior.”

“Ahem. Th-That would be all right?”

“Why wouldn’t it be? You used to do it just fine.”

“Even so, you’ve accomplished such a great thing.”

He had a point. I had gone from a local rising martial artist known as the Sleeping Dragon of Shanxi to a nationwide celebrity.

“And Great Hero Jeok doesn’t seem to like me very much, either…”

“It’s fine. He never liked water much in the first place.”

Where Mu Song kept glancing, Jeok Cheongang stood with a face twisted in fury.

Right beside him, Jin Wikyung was examining some bamboo slips whose contents I could not identify, while Cheongpung was teaching Mimi a new trick.

“Mimi, ride the waves!”

Sssrik—splaash!

…Was that thing a water snake?

Mu Song, whose attention had been stolen for a moment by the rare spectacle, finally spoke with a sour expression.

“In any case, preparations for departure are complete. When should we set sail?”

“What time is it now?”

“The Hour of the Dog you mentioned has passed. It would be best to leave before it gets any darker.”

“…Hmm.”

“Is someone else coming?”

I considered Mu Song’s question for a moment, then shook my head.

“No. No one.”

“Then we can depart.”

“Let’s do that.”

“Very well.”

Mu Song raised one hand high, and the water bandits, who had already finished all their preparations, moved in perfect unison.

The people gathered to see us off were waving in our direction when—

“Wait! Just a moment!”

“Stop! Stop!”

The bow of the fast ship rocked as it was about to pull away from the port.

Far in the distance, I spotted a boy pushing his way through the crowd and let out a quiet laugh.

“Let’s take one more passenger.”

[^1]: The Hour of the Dog was a traditional two-hour period, roughly corresponding to 7–9 p.m.
## Chapter artifact 377

# Chapter 377

“They’ve left?”

The guard captain answered the plump, middle-aged Sichuan Governor’s anxious question.

“Yes. The Yangtze River Channel League fast ship carrying them departed one sikgyeong ago.[^1]”

“Pheeeeew.”

The Sichuan Governor let out such a deep sigh of relief that his belly wobbled, then waved a hand.

“All right, you may go. If you hear any news concerning the martial artists, report it to me immediately.”

“Understood. But what about the troops stationed near Chengdu…?”

The Sichuan Governor frowned.

“Listen, Guard Captain.”

“Yes?”

“Must I concern myself with every little detail? Handle that sort of cleanup among yourselves. Consult the Provincial Military Commissioner—that stubborn bastard—or whatever it takes. Hmm?”

“…”

The Guard Captain was inwardly dumbfounded.

*Was that supposed to be an order or a fart?*

The governor’s incompetence and habit of dumping work on his subordinates were nothing new, but this was too much even for him.

*Even so, I don’t remember him being this bad.*

Several years ago, he had taken a favorite concubine, and ever since then, he had been so consumed by women that official duties had become an afterthought.

The Guard Captain sighed inwardly and weakly performed a military salute.

“…I will carry out Your Excellency’s order.”

“Of course you will. Then get to work. I have urgent business to attend to, so I’ll be going.”

Only then did the Sichuan Governor nod with satisfaction and rise from his seat.

The Guard Captain watched his back recede as he walked away, panting from his excessive weight. Then he muttered in a voice as tiny as an ant.

“Urgent business, my ass. He’s off to embrace his favorite concubine again.”

His prediction proved correct. After leaving the main hall, the Sichuan Governor went straight to an extravagantly decorated bedchamber.

“Ae-hyang! Ae-hyang!”

A beautiful woman lying half-naked on a silk bed larger than most rooms sat up.

“My dear. Why did you take so long? Ae-hyang has been waiting for you.”

“Y-You have?”

The Sichuan Governor was dazed once by her coy eyes and twice by the dazzling white skin that peeked out from between the blankets. His mouth fell open in a foolish grin.

“I’m sorry. The Guard Captain was bothering me.”

“That man again? You’re already so busy, my dear. Why does he keep giving you such a hard time?”

“Exactly.”

“That’s the problem with incompetent underlings. They can’t do anything without you, can they?”

“As expected, you’re the only one who truly cares about me, Ae-hyang!”

The Guard Captain would have rolled his eyes if he had heard them.

The favorite concubine opened her arms to the Sichuan Governor, whose cheeks quivered with emotion.

“Come here, my dear. You’ve worked so hard. Let Ae-hyang hold you.”

“Ae-hyang…”

At his beloved concubine’s sultry, alluring smile, the Sichuan Governor’s eyes grew hazy.

“Could there truly be another woman in all the world as beautiful as you?”

The Sichuan Governor had been born into a powerful family that had produced Grand Councilors, and his path through life had always been smooth.

Backed by inexhaustible wealth, he had frequented pleasure houses and held countless beautiful women in his arms.

Whenever one caught his fancy, he took her as a concubine. He had done so several times, but after meeting so many women, he invariably lost interest before a year had passed.

*But this girl is different!*

He swore he had never seen a woman like her. Her voice, her eyes, even the smallest movement of her fingertips—everything about Ae-hyang was captivating and lovable in his eyes.

He had been seeing her for years, yet he had never grown tired of her. No—if anything, he was falling for her more deeply, to a frightening degree.

“I love you. I love you, Ae-hyang!”

The Sichuan Governor had just entered his fifties, but his cry was as heartfelt as that of a young man who had fallen in love.

He approached as if bewitched and nestled into his concubine’s arms. As always, he began telling her everything that had happened that day. To the Sichuan Governor, she was the only person with whom he could share even his most closely guarded secrets.

“…And so, those troublesome rogues finally left.”

“By rogues, you mean them, right? The martial artists who came here last time.”

“That’s right. The ones carrying His Highness the King of Shangshan’s token.”

“Hmm.”

“What is it?”

“Nothing. Anyway, you must have had a hard time because of this. I heard that the martial artists got into a dispute and many people were killed or injured.”

The Sichuan Governor shook his head in disgust.

“Don’t remind me. Who knows where they got them? They even dared to steal government uniforms and wear them, throwing the empire’s order into chaos.”

“Oh my, really?”

“It may be hard to believe, but it’s true. Whatever else I may overlook, I will certainly submit a memorial to the court about that…”

“How gallant of you. But, my dear…”

The concubine smiled sweetly and stroked the Sichuan Governor’s head where it rested on her lap.

“Wouldn’t matters grow serious if the imperial court found out?”

“Huh?”

“Think about it. One day, you will rise to the position of Grand Councilor, command all the civil and military officials, and assist His Majesty… I’m worried that those jealous of you might use this incident against you.”

“Ha ha. As expected, you’re the only one who cares about me this much.”

The Sichuan Governor gazed at his concubine with overflowing affection.

But he was not a complete fool.

Though the government and the Murim treated each other as they would a cow and a chicken, maintaining mutually inviolable spheres, well over a thousand people had died throughout Sichuan over the past seven days and nights.

He could dump the minor cleanup on his subordinates, but he needed to handle at least this much himself.

“Your concern is touching, but with a matter this serious, trying to hide it would only create a greater problem.”

“Oh, my dear. Do you think I don’t know that?”

“Hmm? Then what do you suggest?”

“Hide what must be hidden and exaggerate your achievements.”

Her coquettish voice tickled the Sichuan Governor’s ear.

“There was a major conflict among the martial artists, and you mobilized the government troops under your command to bring the situation under control.”

“Hmm…”

“You’ll become a wise governor who restored the empire’s order after it was thrown into chaos by a group of rogues and cared for the common people. Of course, it would be best to leave out anything about the government weapons and uniforms, don’t you think? They might cause a misunderstanding.”

“It would be nice if everything went as you said, Ae-hyang. But even so, submitting a false memorial feels a little…”

“My dear, look at me.”

The hesitating Sichuan Governor let out a short exclamation when he saw her eyes glittering beautifully like obsidian.

“Ah.”

“Don’t you understand Ae-hyang’s feelings? Don’t you know how deeply I adore you?”

“I… That is…”

The Sichuan Governor could not continue.

The moment their eyes met, his mind had already gone blank.

His heart trembled at her bewitching figure, and the floral scent of her body made him dizzy.

Boundless trust and affection that had surged up from somewhere, along with unbearable desire, seized control of him.

“Ae-hyang, Ae-hyang!”

His voice was desperate, but his concubine caught the hand roaming over her body.

“My dear, what is your answer?”

“O-Of course I’ll do as you wish. I would do anything for you!”

The smile at the corner of her mouth deepened.

“Good. Just keep doing that, as you have until now. Understood?”

“Yes, yes!”

The Sichuan Governor, consumed by fierce desire, failed to notice.

A bewitching red light seeped into the eyes of the concubine he loved so dearly, an ominous sight.

“Oh, what a good boy. Our governor listens so well.”

The concubine burst into peals of laughter.

Everything was unfolding exactly as she—or rather, the one above her—desired.

* * *

“Hmm?”

“What’s wrong?”

“I thought I just heard some crazy bitch laughing.”

“A crazy bitch? Here?”

“Yeah. It gave me the creeps.”

Hyuk Mujin and I looked around. Three fast ships flying the flag of the Water Dragon Stronghold were gliding unimpeded along a broad tributary of the Yangtze, and naturally, there wasn’t a woman aboard any of them.

“Did I hear wrong? That’s strange.”

*After everything I’ve been through lately, am I hearing things now?*

As I pondered the matter, Hyuk Mujin spoke with a serious expression.

“Could it be that…”

“That what?”

“Perhaps you still cannot forget the young lady standing fourth from the right in the front row?”

Gung Gibang shook his head.

“Nonsense. It was the third from the left. Anyone would have trouble forgetting a beauty like that.”

“Oh, that’s what this was about?”

I smiled benevolently at the two of them.

“I think today is going to be an unforgettable day for you two.”

I beckoned with a bright smile, and several burly river bandits came running over, bowing repeatedly.

“Did you call for us, Great Hero Jin?”

“Is there something you want us humble men to do?”

“Grab those bastards and give them the dipping treatment in the Yangtze.”

The river bandits looked bewildered.

“Uh, did you say ‘dipping’?”

“We’re ignorant men, you see. What exactly is this dipping treatment?”

“Dipping is the proper cultural practice—no, forget that. Just keep dunking their heads in and pulling them out until I tell you to stop.”

“Oh, yes.”

“Easy enough.”

“W-Wait!”

“Squad Leader!”

Gung Gibang and Hyuk Mujin tried to resist, but they didn’t stand a chance.

One had only one good leg, and the other was wrapped in bandages from head to toe.

As the hulking martial artists swarmed them, seized their limbs, and began the dunking show, I looked at the System window I had already left floating in the air.

> **System**
>
> You have an unnamed bound item. Would you like to inspect it?

*Obviously, yes.*

A cheerful chime rang out.

> **System**
>
> **Item Window**
>
> **???**
>
> **Type:** Armor  
> **Grade:** Divine Weapon  
> **Restriction:** Jin Taekyung  
> **Description:** Armor imbued with the spirit of an unknown ancient blacksmith. It possesses truly formidable defensive power. Upon the death of its previous owner, its ownership became bound to a new owner. Once given a name, it can be used freely anywhere.

*Its ownership became bound because the previous owner died?*

I had suspected as much, but it seemed this really was what I thought it was.

After turning my inventory upside down, I finally found the new bound item. A flat, deflated sound escaped my lips.

“…Eh?”

The object resting on my palm was nothing more than a tiny fragment. It had originally been called Black Dragon Armor.

*I definitely blew it away along with that bastard, the Western Heaven Demon Lord, in the final slash. Did it automatically enter my inventory because it was a bound item?*

The sight of the Black Dragon Armor shattering into pieces was still vivid before my eyes.

But what was I supposed to do with a fragment this small?

*I guess I’d feel incredibly secure if I tucked it into the front of my underwear.*

Ah. Maybe that was why it was classified as armor.

I was tugging at the front of my pants and inspecting a suitable position when—

“What are you doing th—”

“…Ah.”

A chilly silence descended in an instant.

The boy’s face stiffened at the sight of my loosened waistband and the hand thrust inside it.

After making sure no one else was nearby, the Slaughter Saint—no, Mungyeong—spoke.

“Why here, of all places?”

“Wait a second. I think there’s been a misunderstanding.”

Just as I hurriedly began to make excuses, Mungyeong’s gaze turned cold.

“I told you when we departed. In front of anyone other than the Fire King and Cheongpung, you are to treat me as Mungyeong.”

I answered with an aggrieved expression.

“You’re speaking casually to me right now too, you bastard.”

“…!”

“Oh. Sorry.”

A multitude of emotions crossed Mungyeong’s face. He glanced sideways at the approaching river bandits and clicked his tongue.

The terrifying Slaughter Saint transformed into the Divine Physician’s Disciple—a cheerful young physician-in-training—in an instant.

“What were you doing, sir?”

“What business is it of yours?”

“…!”

*This is surprisingly fun. But I can’t do it a third time.*

I quickly held out my hand toward the speechless Mungyeong.

“This got into the front of my pants.”

That was slightly at odds with the truth, of course, but Mungyeong did not care about such details. More precisely, his eyes were fixed on the fragment of the Black Dragon Armor.

“This is…”

“Do you happen to know this? No—do you know it?”

“Where did you get it?”

“From that bastard.”

Mungyeong understood that I meant the Western Heaven Demon Lord and nodded.

“You obtained a divine weapon. Though I do not know how only a fragment remained.”

“He called it Black Dragon Armor.”

“Black Dragon Armor?”

“Why? Is that different from the name you knew?”

“I once read about it in an old secret history. A mysterious suit of armor with no fixed name, said to change its form and properties according to its owner.”

“It changes its form and properties? How?”

Mungyeong answered with a look that said I was hopeless. Only then did I realize what I needed to do next.

*Internal energy.*

Internal energy was the very form and nature possessed by its owner.

Sssaaaaah.

Following the formula of the Blazing Flame Divine Art, which had reached its eighth stage, I poured magma-like qi into the fragment of Black Dragon Armor.

The ink-dark energy swirling over its surface vanished, and bluish-white Scorching Yang Qi filled the void.

Engraved with patterns that seemed to blaze like flames, it was no longer something that could be called Black Dragon Armor.

*Flame Dragon Armor.*

The name was simple, but nothing could have suited it better.

The instant I smiled in satisfaction, a bright chime rang out.

> **System**
>
> You have given the bound item ??? a new name!
>
> From now on, you can freely use Flame Dragon Armor anywhere!
>
> Flame Dragon Armor is resonating with your qi! It requires its owner’s power to repair its damaged sections by itself!

Whoooosh.

I could feel it—a massive amount of internal energy rushing out of my body and into the Flame Dragon Armor.

The fragment absorbed it like a sponge. Pretending to tuck it into my robes, I stored it in my inventory instead.

*Automatic repairs? That’s incredible.*

I had certainly obtained something useful.

Thank goodness the final gift of this journey was the Flame Dragon Armor.

As I turned away, Mungyeong stared at me with wide eyes.

“Where are you go—going, sir?”

“What business is it of yours?”

“…!”

This was strangely addictive.

I waved to Mungyeong, who was probably repeating the character for *patience* to himself.

“I’m going to get some sleep. Don’t wake me.”

“…?”

Yes. It was time to wake from a long sleep.

But…

*Why do I feel so uneasy? Did I forget something?*

Tilting my head, I found a place in the fast ship’s cabin and lay down. I closed my eyes, took a deep breath, and called out the command.

*Logout.*

A chime rang out.

> **System**
>
> Logging out in 10 seconds. Ten, nine, eight, seven…

With the final count, the sound of splashing and someone’s cries faintly pierced my ears from somewhere.

Splash! Gasp! Squad Leader, save me—gasp!

[^1]: A sikgyeong was the time required to eat a meal, conventionally treated as roughly thirty minutes.
## Chapter artifact 378

# Chapter 378

Ding.

> **System**
>
> You have successfully completed **Logout**.

With the cheerful System notification, the senses that had briefly left me began to return.

The softness of the bed beneath my back. The warm air inside the private jet.

And the hands gripping and shaking both my shoulders, along with the shouts that came with them.

“Mr. Jin Taekyung! Wake up! Mr. Jin Taekyung!”

- Wake up, you vile human!

I blinked at the urgent voices drilling into my ears—two voices, no, one monster’s and one human’s.

As my vision cleared, a familiar face came into view.

“Uh, Team Lea—”

Smack!

“Wake up!”

- Well done, slightly less vile human!

“…”

What the hell was this?

After taking an unexpected slap across the face, I answered in a dazed voice.

“I’m awake…”

“What is wrong with you? I tried so hard to wake you up, so why are you only getting up now?”

- Just die! Go ahead and die!

“S-Sorry…”

Damn, he was intense. This was the first time I’d ever seen Team Leader Choi this furious.

No matter what happened, Team Leader Choi always kept his composure and bragged about his designer goods. Now, lightning was practically shooting from his eyes.

*What’s gotten into him? We’re still on the plane, aren’t we?*

I had apologized on instinct, but I was still bewildered. Was this really worth slapping me over?

That was when—

“This is no time for this! Hurry and—”

“Aaaah!”

Team Leader Choi’s voice was drowned out by the flight attendants’ screams. The shouts of men I assumed were the pilots followed.

“Mayday! Mayday! Mayday!”

“Control tower! Control towerrrr!”

“…What the fuck?”

What the hell was going on?

As I frantically looked around, Team Leader Choi hit me with an unbelievable statement.

“We’re under attack by monsters!”

“Monsters? An attack?”

What kind of bullshit was that? We were flying at twenty-five thousand feet in a private jet sent by the Chinese Central Committee.

By now, it wouldn’t have been strange for our destination, Chengdu International Airport in Sichuan Province, to have come into view…

“Huh?”

I unconsciously turned toward the window—and stared with my mouth hanging open.

Far below, a massive airport stretched across the ground. Flames surged into the sky, while large and small dots moved through the chaos.

It was a battle. Humans and monsters were locked in a fight to the death.

And that wasn’t all.

- Kyaaaauuu!

The enormous body of a monster was rapidly closing in on the private jet I was riding in.

“That’s…”

There was no mistaking it. Even after rubbing my eyes and looking again, it was still a wyvern.

An A-rank monster classified as dragonkin alongside drakes.

They were a pain in the ass even on the ground, but at twenty-five thousand feet, they were the last things I wanted to encounter.

And there were around a dozen of them!

*…What kind of fucked-up situation is this?*

A fierce battle was raging around Chengdu International Airport below, while a flock of wyverns chased the private jet carrying me through the sky.

It didn’t take long for my briefly frozen brain to reach a conclusion.

“Lich!”

The shout burst from me like a thunderbolt.

There was no doubt about it. The top-tier undead monster that had appeared with an unprecedented monster wave one week ago in modern-world time had already extended its reach this far.

“The control tower isn’t responding!”

“The wyverns! The wyverns are—!”

“Kyaaaah!”

- I knew this would happen! We’re all dead!

Even in the middle of my panic, I corrected the Skeleton Warlord.

“That’s true, but weren’t you already dead?”

- Shut up, you vile human! This is all your fault! Ahhh, my legion! Forgive your commander!

Screams and shouts rained down from every direction as humans and monsters alike fell into a panic.

Only one person among them managed to retain his sanity.

“Everyone, calm down! What you’re afraid of won’t happen!”

As expected of Team Leader Choi. He was reliable.

He had obviously thought of a way to overcome this crisis.

After calming the chaos with his composed voice, Team Leader Choi pointed at me.

“Mr. Jin Taekyung here will take care of it!”

“…?”

“Mr. Jin Taekyung. What should we do?”

“Why are you asking me?”

“I trust you, Mr. Jin Taekyung!”

“…”

Why did he trust me?

In a situation like this, putting his faith in God, Buddha, or Allah would probably help more.

I was momentarily speechless as people’s gazes came flying toward me from all sides.

“Come to think of it, I’ve heard about that Hunter. They say he’s so formidable that even Comrade Chairman Xiao Yang made a special request for him.”

“I’ve heard the rumors too. They say he might be a new S-rank Hunter. Apparently, he defeated two named monsters all by himself.”

“Ooh! Ooooooh!”

“We’re saved! We’re going to live!”

- You vile human! I knew you were strong, but you’re beyond my wildest imagination! Rejoice, my legion! Your commander has survived!

“…You’re already dead.”

This was driving me insane. None of them were in their right minds anymore.

I stared at Team Leader Choi in disbelief.

“What exactly are you basing this on?”

He answered without hesitation.

“I told you. I trust you.”

“That’s what I’m asking. Where does that baseless trust come from—”

“It isn’t baseless.”

“What?”

“Your attitude, tone of voice, and expression in a situation like this. All of them are grounds for my trust.”

“…!”

Only then did I finally realize it.

I was flustered by the unexpected situation, but I felt no fear or terror whatsoever.

The answer was closer than I had thought.

*Because I’m strong.*

I was strong. Stronger than ever. Strong enough to avoid any danger.

That was why neither the monsters sweeping across the ground like a wave nor the flock of wyverns right behind us frightened me.

“So that’s it…”

I muttered under my breath, then spoke up.

“Who’s the captain?”

A hand shot up from the cockpit ahead.

It was trembling violently. His other hand must have been gripping the controls for dear life as he desperately tried to evade the wyverns lunging at us.

“I-I am.”

“Can I open the door for a second?”

“What?”

“I said, can I open the plane door?”

The captain was so shocked that he poked his head out and stared at me as if I were insane.

“Of course not! The pressure-sealing system won’t even let you open it, and the aircraft will be damaged because it can’t withstand the pressure difference! We won’t be able to breathe properly, either!”

Team Leader Choi, fiddling with the ring on his finger, cut in.

“I think I can block the pressure. I don’t know what you have in mind, but go ahead and try.”

“Okay.”

“Don’t! You *bangzi* bastards![^1] Are you trying to kill us all?”

“…What did you just call us?”

The nerve of him, insulting Koreans right in front of a proud Korean kimchi man like me!

The captain realized what had slipped out, and his face turned white.

“No, that’s not what I meant.”

“You fucking Chink bastard. Damn it.”

“…!”

“Hey, Captain!”

“Y-Yes?”

“I’m opening it.”

“Ah! Ahhh!”

Before the captain could stop me, I opened the door.

No—I cut it open.

Shhk!

Sword qi—the force called an Aura Blade in the modern world—sliced through the sturdy alloy and created a small door.

It was the tremendous power wielded by Supreme Peak masters in Murim and, in this world, only by S-rank Hunters.

Team Leader Choi’s eyes widened in shock.

“Mr. Jin Taekyung, this is—”

“Team Leader!”

Whoooosh!

This was no time to be surprised. The tremendous wind and pressure were making the aircraft lurch, turning the cabin into a complete mess.

The screams and my shout snapped Team Leader Choi back to his senses. He rubbed his ring.

“An airtight barrier surrounds us. Barrier!”

“Oh.”

With the incantation, a transparent membrane of energy sealed the new opening without leaving the slightest gap.

So there was a way to do this.

With a brief exclamation of admiration, I stuck my upper body out of the cabin.

Team Leader Choi’s barrier recognized me as an ally and let me pass through without resistance.

Rrrrrumble!

The wind pressure slammed into my upper body as if trying to crush me to death. I grinned.

*This is no joke.*

But it wasn’t unbearable.

Actually, it would have been strange if I couldn’t withstand it. Compared to the waves of qi the Western Heaven Demon Lord had emitted, this was no more than a gentle spring breeze.

- Kyaaaauuu!

The monster’s sharp cry mixed into that spring breeze.

The flock of wyverns had already drawn close enough for me to judge the distance.

*About a hundred meters. I’ve never tried this before, but… at this distance, it should be enough.*

*Open Inventory. Equip.*

Ssswish.

A spear I had bought at a discount from the Hunter Market appeared in my hand.

Like a javelin thrower, I drew my shoulder all the way back. From my waist to my wrist, every muscle and tendon I needed pulled taut like a bowstring.

- Kyaau!

The lead wyvern—their chief—sensed something was wrong and threw back its head with a shriek.

I could see a pure-white current of air being sucked toward its snout.

*That’s…*

- Breath! It’s Breath! Dodge it, you vile human!

The Skeleton Warlord was right.

Of all the countless monsters, Breath was a power granted only to the dragonkin. I could clearly see it taking shape inside the wyvern’s gaping maw.

Whooooom.

A massive sphere of wind. The Air Breath, powerful enough to shred metal like paper, finished taking shape.

“Hey, wyvern!”

- Kya?

“I’m putting it in!”

I shouted like a thunderbolt and whipped my drawn-back shoulder forward.

Fwoom—whooosh!

Fiery concentrated qi sheathed the spearhead, burning through the air and cleaving the wind.

The wyvern’s bright yellow eyes widened at the blue-white streak of light shooting straight toward it.

- Kiiiiiik!

Whoooom!

Compressed air burst from the tip of the spear. A cloud of white.

And then—

Thwack! Boom-boom!

A massive body plummeted toward the ground like a kite with its string cut.

* * *

- Kyaau?

- Kiiit?

Around a dozen pairs of bright yellow eyes stared at one another.

Wyverns were ferocious creatures from the moment they were born, but at this moment, they were utterly bewildered and had no idea what to do.

- Kikikit?

- Kiiik…

*What? Is the boss dead?*

*Looks that way…*

After exchanging words in their own language, the wyverns were dumbfounded.

Their leader was exceptionally powerful even among their own kind—so powerful that he was known as the “Black Star.”

And now, the Black Star had become a black speck falling toward the impossibly distant ground.

- Kiririk?

- Grrrrr.

None of them had even properly seen how he died.

They could only guess that the tiny human had thrown a spear and hit him.

But that was impossible.

How could a mere human dare lay a hand on a descendant of the great dragons…

“Hey, green wyvern over there!”

- Kiiik?

“I’m putting it in!”

Thwack!

This time, they saw it clearly: their companion’s head bursting apart in the beam of light.

- Kiiik!

- Kyaaaauuu!

*Another of our bloodline has died after the boss!*

Furious beyond measure, the wyverns vowed revenge against that damned human.

- Kiiit!

Of course, not today.

They would get their revenge later. A little later.

“Hey, blue wyvern over there!”

Thwack!

*…Would they ever get their revenge?*

Around a dozen pairs of wings began flapping desperately.

[^1]: *Bangzi* (棒子) is a derogatory Chinese slur for Koreans.
## Chapter artifact 379

# Chapter 379

Rrrrrumble!

A tremendous roar, followed by vibrations traveling through the ground.

Shao Shen, a twenty-year-old young man staring toward the horizon, simply could not believe what he was seeing.

*How can monsters that should be thousands of kilometers away be here…?*

He was not the only one asking that question.

More than a thousand Hunters from the Public Security Armed Forces, along with five thousand soldiers of the Chinese People’s Liberation Army dispatched to maintain public order—all of them stationed at Chengdu International Airport—were asking themselves the same thing as they stared in horror at the reality bearing down on them.

- Ssssss!

- Grrrrr!

From low-level monsters like goblins and orcs to higher monsters like trolls, ogres, and lycanthropes—

A monster army filling the horizon was charging forward with hideous roars.

The distance of one kilometer was shrinking by the second. Shouts like screams erupted across the airport.

“Form ranks by unit! Assemble! Assembllllle—!”

“Fire! Fire! I said fire!”

Rat-a-tat-tat! Boom!

The People’s Liberation Army hurriedly formed ranks and poured out firepower at their commanders’ orders, but the effect was pitifully small.

They had been ambushed by an unexpected monster army.

The soldiers, who were merely ordinary people without any abilities, froze in fear. Their firearms were barely effective against the low-level monsters at best.

“There are too many monsters! There are too many!”

“Pilots!”

“Get the fighter jets into the air! Bomb them from above—!”

The desperate shouts of the commanders were drowned out the next moment by a savage roar that rang across the sky.

- Kyaaaauuu!

“W-What is that?”

“Wyverns! They’re wyverns!”

A massive body came flying with the setting sun behind it.

Leading the charge were wyverns, known as the terror of the skies, followed by dozens of griffons and gargoyles.

The A-rank monsters descended with their wings angled sharply, swooping down upon the fighter jets that had not yet managed to take off.

Krrrunch! Boom!

The powerful beat of their wings made several-ton blocks of metal jolt, while claws infused with magic tore through the fighter jets like sheets of paper.

The metal fragments hurled away by the explosions crashed into the pilots running frantically across the tarmac.

Bang-bang! Crunch!

Instant death. They did not even have time to scream.

The guns began spitting fire at the commanders’ orders once they regained their senses, but the flesh and hide saturated with powerful magic could do little more than suffer scratches from hundreds or even thousands of bullets.

- Kikikikit.

The monsters laughed at the helpless humans.

Everyone felt a shock and terror that made the hair all over their bodies stand on end.

“H-How can this be?”

A monster army filled the ground and the sky. The creatures that could barely be harmed by firearms were monsters in the truest sense.

“M-Monsters…”

“I-I have to live. I don’t want to die like a dog in a place like this!”

Fear of death spread faster than any epidemic.

And just as the soldiers of the People’s Liberation Army began taking a step backward one by one, one person instead moved forward.

“Don’t retreat!”

Shao Shen, a young man whose boyishness had not yet faded, shouted with blazing eyes.

The five-star red flag of the People’s Republic of China was embroidered across the chest of his armor.

“Who are we?”

At the young man’s question, those who had been about to flee stopped in their tracks.

Shao Shen glared at the monster army charging from several hundred meters away. His thunderous voice erupted again from beneath his tightly pulled helmet.

“Who are we?”

His shout made their blood seem to boil.

With everyone watching him, Shao Shen raised his spear point straight into the air.

“We are the descendants of Zhonghua, and we are brothers of the People’s Liberation Army and the Public Security Armed Forces!”

An aura resembling the colors of the setting sun surged from the spear point, which rose high enough to pierce the sky.

Ssssss!

“Let’s go! Let’s sweep away every last one of those monsters!”

“Waaaaah!”

A colossal roar that made their ears ring shook the earth.

Led by Shao Shen, the Hunters of the Public Security Armed Forces gripped their weapons and charged into the monster army like fierce tigers.

“Don’t retreat! Show them the power of Zhonghua!”

“Uraaaaaah!”

- Grrrrr!

- Awooooo!

Human cries filled with the resolve to face death mingled with the monsters’ roars.

The two groups became one mass as they crashed into each other.

Kra-kra-kra-boom!

A clash that shook the heavens and earth.

And death raining down from every direction.

“Gaaaaah!”

- Kweeeek!

Thud! Crunch!

Screams and thunderous impacts rang out across the battlefield.

The aura-coated blade of an A-rank Hunter cleaved through a lycanthrope’s neck, while an ogre’s iron club sent three or four Hunters flying as bloody pulp.

Two Hunters worked together to bring down a monster, then raised their weapons toward the next enemy.

A massive shadow fell over their heads.

- Kiiiiit!

Slash!

The claws of a griffon diving from the sky shredded the Hunters’ bodies along with their armor.

A large ball of fire flew toward the griffon as it searched for its next prey.

“Fireball!”

Bang!

The griffon’s body, gliding through the sky, staggered amid a cloud of acrid smoke.

The ranged units waiting on the ground for their chance did not miss the opening.

“Now!”

Boom! Bang-bang-bang!

Spells of every kind and arrows saturated with mana tore into the griffon.

The flying monsters let out savage cries at the sight of the griffon plummeting with a final scream.

- Kyaaaauuu!

The modern weapons made of lead and iron blocked the flying monsters diving toward the ranged units.

“Commence mass fire!”

Rat-a-tat-tat-tat! Boom!

Countless rifles and heavy weapons fired at once. Dozens of tanks spewed fire simultaneously.

Though modern weapons were no match for mana—the natural counter to monsters’ magic—concentrating all that firepower at once still forced even the flying monsters to falter.

- Kiiit!

“It works!”

“It’s useless anywhere else! Aim for their eyes!”

Monsters were born with magic running through their bodies, and their flesh could casually ignore most physical force.

But their eyes were the one exception.

Their eyeballs, covered only by a thin membrane, could be damaged if heavy weapons were brought to bear.

At the sight of the monsters hesitating, the division commander watching everything unfold excitedly waved his baton.

“More! Pour more fire into them! Don’t let those monsters move an inch—”

Whoooooom!

His voice never finished.

Poison Breath fired by a green wyvern covered a radius of more than a hundred meters. The division commander and the command staff were drenched in potent acidic poison and melted away.

“D-Division Commander!”

“The command staff…!”

The People’s Liberation Army fell into a state of panic after losing hundreds of soldiers and senior commanders in the blink of an eye.

Officers, noncommissioned officers, and soldiers alike stared at the horrific scene unfolding before them, crying out in shock.

“This can’t be happening…”

“N-No. This isn’t right. This can’t be happening! This isn’t what I signed up for!”

Someone’s scream spoke for everyone.

They had brought their forces as a precaution, but their primary mission was to join up with and escort the foreign Hunters who would soon arrive at Chengdu International Airport, then follow orders from above.

They had never heard anything about a monster army that should have been thousands of kilometers away invading the airport.

“What the hell is going on…?”

“We’re going to die. We’re all going to die.”

The fear they had briefly forgotten settled over the heads of the People’s Liberation Army once more.

Unlike the Hunters of the Public Security Armed Forces fighting on the front lines, they were merely ordinary people carrying modern firearms.

And their ominous premonition soon became reality.

A nightmare far worse than they had imagined.

- Om. Ne. Ha. So. Yu.

A voice broken into disconnected syllables.

An eerie noise resembling the static of a radio with an unstable signal echoed across the battlefield.

Black fog that had come from somewhere spread over the heads of the people.

- Yen. Wi. Ga. Ji. Ke!

That was when the horrifying change occurred.

Swoooooosh!

Dark magic as black as storm clouds spread like a web through the blood and corpses.

It breathed new strength and souls into bodies that were growing cold, then bound them in chains and enslaved them.

Snap. Snap-snap.

Given new life, an army of skeletons slowly rose from the pools of death.

*Those beings* had woven countless dead together with invisible chains and made them their slaves.

They laughed in satisfaction.

- Kik, kikikik.

- Grrk. Kihihihi.

* * *

- Grrrrr.

With a bubbling sound, a man rose to his feet.

He wore armor bearing the five-star red flag and carried a massive ax. He looked exactly like the A-rank Hunter Shao Shen remembered.

*…Mr. Yao Wei.*

But Shao Shen could not call the man’s name aloud.

No—he could not bring himself to call it.

He knew that the person standing before him was no longer the man he had known.

*Ah… ahhh.*

If Shao Shen had not witnessed the man’s decapitation ten minutes earlier, if he had not seen him rise with his severed head tucked beneath his arm, Shao Shen would have thought of him as a comrade and friend.

But Yao Wei no longer existed.

A new name slipped between Shao Shen’s lips.

“Dullahan…”

A headless knight.

A dullahan.

Shao Shen bit his lip at the sight of his comrade transformed into a higher undead monster.

Something hot ran down his cheek.

“I’m sorry. I really am.”

- Grrrrraaaah!

As the dullahan charged at him with a roar, Shao Shen shot forward like the wind.

In the past, the two of them had often sparred like this.

Their bouts had begun with nothing more than competitive pride and continued day after day. Once each spar ended, Shao Shen had to put up with Yao Wei’s complaints.



*You little brat have no manners, I tell you. Would it kill you to let me win once?*

*Ha-ha. Let’s go get something to eat. The loser was supposed to pay, so I guess you’re buying again today, Mr. Yao Wei.*

*You’ve got plenty of money at home, and you’re still so cheap. One day, I’ll make you buy me a meal.*



But that had never happened before, and now it never would. Shao Shen had always been the winner.

*Goodbye. Thank you for everything.*

Whoosh! Slash!

The ax swept through empty air, while the aura surging from Shao Shen’s spear point cleaved through the dullahan’s upper body.

A cut line appeared, starting at his waist. The headless knight’s body slowly crumpled.

Thud. Collapse.

Shao Shen stared blankly down at the face of the fallen dullahan—no, Yao Wei.

His eyes burned.

“How dare you… How dare you do this…”

His friends and comrades, who had been laughing and joking with him only half a day earlier, had become undead monsters.

The Hunters of the Public Security Armed Forces were famous for their strict discipline, but they were not cold-blooded people without a drop of human feeling.

The Hunters who had entered the battle prepared to die now faced something frightening for the first time—the fear of human attachment.

“Wake up! It’s me, Ryu Inchin! Ryu Inchin!”

“H-Hyung…!”

- Grrrrr!

Crunch! Boom!

Screams and death rained down from every direction.

Unlike the Public Security Armed Forces, which had suffered casualties approaching half its strength, the monster army had increased its numbers and continued to surge forward without end.

*Am I going to die here, like this?*

For the first time in his life, Shao Shen thought about death.

The situation was so desperate that even someone as bright and cheerful as him had begun to think that way.

*We didn’t receive any warning signal, so communications must be down. There won’t be any reinforcements either… This really is the end.*

Slash!

After cutting down one undead monster after another, Shao Shen laughed hollowly and looked up at the sky.

The sunset was surprisingly beautiful.

When the sun went down and darkness arrived, he would never see a sight like this again.

*It’s not so bad for the last sky I’ll ever see…*

Huh?

Shao Shen blinked, unable to finish the thought.

Something unimaginably enormous was rapidly approaching the battlefield from high above.

*An airplane?*

Whoooooom!

A massive aircraft engulfed in flames.

And someone’s shout rang across the vast sky.

“Hey! Monsters!”

“…?”

- …?

*Am I hearing things?*

Shao Shen was not the only one to look up.

Everyone on the battlefield raised their eyes toward the sky.

A voice that seemed to hold even a hint of madness thundered across the battlefield.

“I’m going to ram it!”

*Ram what?*

Shao Shen soon understood what the voice meant.

Rrrrrumble!

The massive fuselage of the airplane swept across the battlefield.

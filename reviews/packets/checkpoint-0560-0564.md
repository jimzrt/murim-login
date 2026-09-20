# Checkpoint Review — 560–564

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

# Chapters 560–564

## Plot

The accelerating Mutated Gate crisis prompts Team Leader Choi to build political, business, and Guild alliances around the Peace Guild while weakening Ares. He reveals his descent from Cheon Taemin to Magic Johnson, who pledges the Wizard Guild’s support and introduces him to influential contacts, including Joseph Biden. Magic also reports that worldwide mana levels have risen seven percent over the previous year.

A C-rank Gate in Yeokgok, Bucheon, leased by Ares Guild, mutates after its rescue team fails to respond. Jin Taekyung and the Skeleton King enter, kill the Orc Lord, and rescue the trapped Ares Hunters. The incident becomes the third Mutated Gate of the new year.

During a New Year press conference with President Baek Hanseong, Taekyung exposes the major Guild’s negligent fifteen-minute delay and argues that timely intervention could have prevented the mutation. The government launches an investigation, while the public recasts Taekyung as a heroic successor to Cheon Taemin. Go Jun’s legitimacy as Lee Jungryong’s successor collapses further; roughly ten Ares members transfer to Peace, and he vows to kill Taekyung.

The Peace Guild expands beyond its original Guild House, buying surrounding properties and constructing a larger facility. Magic Johnson discusses the Guild’s growing influence, gives Taekyung a chip for Team Leader Choi, and confirms that a secured training room is reserved for Taekyung and selected founding members learning the Jin Family’s Cultivation Technique.

## Continuity

- Team Leader Choi is gathering political, business, and Guild allies to strengthen Peace and undermine Ares. Magic Johnson and the Wizard Guild support him.
- Choi’s blood descends from Cheon Taemin, giving him significant political and social leverage.
- The first six-member Fire Dragon Pavilion mission remains underway through the Journey to Nanman Quest. Its failure penalty is the Title Can’t Go to Nanman; the party secretly departed Henan.
- Taekyung is in the modern world in early 2047. He has entered the Yeokgok Mutated Gate and killed its Orc Lord.
- Three Mutated Gates have appeared within the first ten days of the new year. The cause of the accelerating Mutated Gates, Monster Waves, and seven-percent worldwide mana increase remains unknown.
- Go Jun is Ares Guild’s Vice Guild Master and Lee Jungryong’s disciple. Public exposure of Ares’s Gate negligence, the Blue House press conference, and defections to Peace have damaged his authority, but he remains determined to kill Taekyung.
- The Peace Guild’s secured training room is restricted to Jin Taekyung, Team Leader Choi, Butler Kim, Song Song, and Im Kkeokjeong.
- Mungyeong suspects Nanman may contain Dark Heaven’s second rift. The Lord of Heaven’s identity, Dark Heaven’s Gate-opening method, the origin of its mutants, and the connection between those mutants and Mutated Gates remain unresolved.
- The Southern Heaven Demon Empress may be heading toward Nanman. Song Ho’s dispatch there remains unanswered.
- The outcomes of Jeok Cheongang’s duel with Nangong Cheon and the reason Ju Hwaran and Sama Pyo’s engagement ended remain unresolved.
- The information on Magic Johnson’s chip remains unknown.

## Translation Decisions

- Render 변이 게이트 as **Mutated Gate**, 몬스터 웨이브 as **Monster Wave**, 오크의 황무지 as **Orc Wasteland**, and 오크 로드 as **Orc Lord**.
- Render 남만행 as **Journey to Nanman**, 남만을 못 가 as **Can’t Go to Nanman**, and retain **Nanman**, **Nanman Beast Palace**, **Fire Dragon Pavilion**, and **Young Lady Ju**.
- Render 건량 as **dry rations**, 반 시진 as **half a shichen**, 국회의사당 as **National Assembly**, 영구 임대 as **permanent lease**, and 길드 하우스 as **Guild House**.
- Render 고세원 as **Go Se-won**, 경호팀장 as **Head of Security**, A구역 as **Section A**, 매직 존슨 as **Magic Johnson**, and 썩코춘 as **Sseokkochoon**.
- Retain established renderings including **Peace Guild**, **Ares Guild**, **Grand Mage**, **Wizard Guild**, **Skeleton King**, **Teleport**, **Teleportation**, **One Against a Thousand**, **Giant’s Roar**, **Corrupted Ent**, **Red Eye**, **Chikorita**, **Dark Heaven**, **Murim Alliance**, and **Five Kings Hall**.

## Durable state

{
  "active_continuity": [
    "Magic Johnson's information records at least thirty-two Mutated Gates in the United States during one week, and the true number is likely higher.",
    "The Peace Guild has risen as the only apparent counterweight to Ares Guild; Team Leader Choi is gathering political, business, and Guild allies to strengthen Peace and weaken Ares, with Magic Johnson and the Wizard Guild supporting him.",
    "Team Leader Choi has confirmed that his blood descends from Cheon Taemin, whose legacy gives him exceptional political and social leverage.",
    "The Fire Dragon Pavilion's six-member first mission is entering Nanman through the Journey to Nanman Quest, whose reward is a linked quest and whose failure penalty is the Title Can't Go to Nanman; the party secretly departed Henan.",
    "Taekyung is a Supreme Peak master with Three Flowers Gather at the Crown, advanced Qi Sense, exceptional resistance to monster Fear, public S-rank-level recognition while retaining an A-rank license, leadership of the Fire Dragon Pavilion's first mission to Nanman, and the Peace Guild's modern-world patronage.",
    "Mungyeong ended Taekyung's direct training and assigned him the final task of incorporating martial principles into his learned martial arts; Cheongpung accompanies Mungyeong and learns through observation.",
    "Mungyeong considers Nanman a plausible site for Dark Heaven's second rift, while Dark Heaven remains a monster-like threat capable of causing rifts and creating mutants; the mechanism behind Jang Sam's transformation remains unresolved.",
    "The Mount Song Resolution restored the Murim Alliance with Mae Jonghak as Alliance Leader and Jeok Cheongang heading the Five Kings Hall; Zhuge Feng's Demon-Sealing Formation still blocks mana from the exposed Gate while Jang Taebo processes the Water God Dragon's remains.",
    "Taekyung is in the modern world in early 2047, has entered the Yeokgok Mutated Gate, and has just killed its Orc Lord to rescue an Ares raid team.",
    "Go Jun is Ares Guild's Vice Guild Master and Lee Jungryong's disciple; Jin Taekyung's public exposure of a major Guild's Gate negligence and the Blue House press conference have intensified the threat to Ares, while Go Jun remains determined to kill Jin.",
    "Ares Guild's authority is visibly cracking: about ten members have transferred to Peace Guild, and Go Jun's legitimacy as Lee Jungryong's successor has been publicly undermined.",
    "The secured Peace Guild training room is restricted to Jin Taekyung and selected founding members training in the Jin Family's Cultivation Technique; Magic Johnson has delivered a chip for Team Leader Choi and reported a seven-percent year-over-year rise in worldwide mana levels."
  ],
  "continuity_sources": [
    564,
    563
  ],
  "open_questions": [
    "What is the Lord of Heaven's identity, how is he connected to the dangerous force Taekyung associates with his original world, and how can Dark Heaven open Gates?",
    "What will Taekyung's party find in Nanman, and what does the Southern Heaven Demon Empress intend there?",
    "What process created Jang Sam's mutant form, whether Dark Heaven's mutants can absorb human energy, and whether it relates to the Mutated Gate?",
    "What will result from the duel between Jeok Cheongang and Nangong Cheon, and why did Ju Hwaran and Sama Pyo's political engagement end?",
    "What information is stored on Magic Johnson's chip, and what is causing worldwide mana levels to rise?"
  ],
  "safe_through": 564,
  "temporary_decisions": [
    "Render 건량 as dry rations, 광서 as Guangxi, 대별산 as Mount Daebyeol, 만리행 as Ten-Thousand-Li Journey, and 고잉메리호 as Going Merry.",
    "Render 반 시진 as half a shichen and retain Nanman, Nanman Beast Palace, Fire Dragon Pavilion, Great Hero, and Young Lady Ju.",
    "Render 남만행 as Journey to Nanman, 남만을 못 가 as Can't Go to Nanman, 면구 as disguise mask, 역용술 as disguise technique, 각주님 as Pavilion Master, 로그아웃 as Logout, and 동기화 as Synchronization.",
    "Render 일기당천 as One Against a Thousand, 거인의 포효 as Giant's Roar, 타락한 엔트 as Corrupted Ent, 붉은 눈 as Red Eye, 치코리타 as Chikorita, 대마도사 as Grand Mage, 순간이동 as Teleportation, 텔레포트 as Teleport, 변이 게이트 as Mutated Gate, and 몬스터 웨이브 as Monster Wave.",
    "Render 모하비 사막 as Mojave Desert, 애리조나주 as Arizona, 대의 as greater cause, 순수혈통 as pureblood, 국부 as Founding Father, 위저드(Wizard) 길드 as Wizard Guild, 조셉 바이든 as Joseph Biden, 펠릭스 왕자 as Prince Felix, 곽한구 as Gwak Hangu, 역곡 as Yeokgok, 오크의 황무지 as Orc Wasteland, 오크 로드 as Orc Lord, 국회의사당 as National Assembly, 고세원 as Go Se-won, 경호팀장 as Head of Security, A구역 as Section A, 신성불가침 as sacrosanct, 바티칸 as Vatican, 영구 임대 as permanent lease, 혈안 as bloodshot, 매직 존슨 as Magic Johnson, 썩코춘 as Sseokkochoon, and 길드 하우스 as Guild House."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 560

# Chapter 560

Holy shit. What the fuck.

Even if I brought out every English-language curse I knew, I still couldn’t express how utterly fucked things were.

*Thirty-two times in a single week.*

It was an outrageous number. And even that only covered the information Magic Johnson had managed to obtain.

I had no idea what the exact statistics were, but it was obvious there had been more than thirty-two incidents.

*Yeah. Maybe this was inevitable.*

The United States was ninety-eight times the size of Korea, and it had nearly twenty times as many Gates.

The United States had also been Demon King Asmodeus’s top-priority target in the past, suffering tremendous damage throughout the Great Cataclysm.

But ironically, the thing that had once again elevated the United States to the position of the world’s greatest power was the very existence of the Gates left behind by the war.

*Oil fields.*

Modern Gates were literally new, far more abundant oil fields.

More than thirty years had passed since the disaster that swallowed the entire world. Monster byproducts had long since become expensive commodities, and Magic Gems had become an environmentally friendly energy source.

The surviving human race had built an even more dazzling and enormous civilization atop the ruins left behind by the war.

But…

“The party seems to be over.”

Like Magic Johnson’s offhand remark, the lavish party of the winners was finally coming to an end.

The oil fields called Gates had caught fire. Soon, explosions would erupt all over the world.

No—they were already happening.

For now, an invisible hand was merely covering everything up.

“Ah, fuck…”

I muttered like a groan, then asked Team Leader Choi,

“Domestic conditions aren’t similar, are they?”

My question meant more than what I had said aloud. I was asking whether there were other incidents I didn’t know about, like the ones happening in the United States.

Team Leader Choi, who had been lost in thought for a moment, opened his mouth.

“I always keep unexpected possibilities in mind, but as far as I know, there aren’t any.”

“Team Leader Choi, this is something we need to be certain about.”

“I know. That’s why I’m thinking of arranging another meeting while I have the chance.”

Magic Johnson, who had been listening to us, asked,

“A meeting? With whom?”

“People whose paths happened to cross with mine. I can’t imagine they would have lied to me, but you never know what people are thinking.”

“True. Especially politicians.”

At Magic Johnson’s offhand remark, Team Leader Choi quietly nodded.

“So you knew.”

“Choi looked awfully busy at Mr. Lee’s national funeral. A lot of people were looking for him.”

Team Leader Choi and I had also attended Lee Jungryong’s national funeral to pay our respects.

Our true feelings had been different, but it wasn’t only because of the public image we had to maintain.

“They’re looking for a new shadow to shelter under. I was hoping for the same thing.”

People from the political and business worlds, along with key figures from the mid-sized and large Guilds that had been crushed beneath Ares Guild, had shown tremendous interest in us.

Of course, more than half of them had come looking for me first. But I had known from the beginning what my answer would be.

*Don’t talk to some Hunter nobody like me. Go talk to our Team Leader Choi.*

Earning a place at Lee Jungryong’s national funeral, where every kind of heavyweight had gathered, meant they were people who had claimed their own victories in society after fighting tooth and nail.

They understood exactly what I meant and immediately began scrambling to arrange meetings with Team Leader Choi.

“The powerless are ignored, but people extend their hands in every direction to those with power. No matter how much the world changes, that fact never does.”

Magic Johnson’s words were a sharp truth.

No one had ever sought out me or Team Leader Choi before.

No—the Peace Guild had risen to become the only force capable of standing against Ares Guild.

The public might not know it, but the people sitting at the top of society knew it better than anyone.

By now, political and business leaders were probably racking their brains over how much they could profit from a clash between the two forces, and whose shadow would offer them the most room to breathe.

The owners of the mid-sized and large Guilds probably wanted to use this opportunity to escape Ares Guild’s excessive monopoly as well.

And so Team Leader Choi had gained new allies and the power they possessed.

He had taken his first step toward digesting the entire feast called Ares.

Perhaps that was why, when Team Leader Choi’s voice flowed between his perfectly smooth lips a moment later, it carried more strength than ever.

“I won’t reject the hands they’ve extended.”

Magic Johnson gazed at Team Leader Choi, then suddenly spoke.

“So… it seems the rumor was true.”

“What are you talking about?”

“That rumor. The one saying that Choi is connected to *him*.”

“There’s no reason to hide it anymore. It’s true.”

Magic Johnson’s eyes widened.

“I didn’t expect Choi to admit it so easily. Or have you already told everyone else you’ve newly crossed paths with?”

“No. But they know, and so do I, even though none of us has said it aloud. We know whose blood flows through my veins.”

A quiet laugh escaped between the Grand Mage’s thick lips.

“Right. No one can deny that fact. He’s the only pureblood in existence in the twenty-first century.”

No living noble or royal could compare to Team Leader Choi.

Not even if the arrogant Prince Felix of the United Kingdom became king.

If his ancestor had built a vast empire upon which the sun never set, then Cheon Taemin was the savior who had allowed billions of people to see the sun rise on another day.

“And I’ll say that not mentioning him directly was wise. Quiet people who don’t reveal themselves easily inspire trust.”

“Thank you for the compliment.”

“Don’t thank me. It’s simply a fact.”

The cheerful, playful Magic Johnson of usual was nowhere to be seen. He continued in a calm voice.

“But Choi, keep this in mind. Your grandfather, wherever he may be now, and I have always known what came first. We risked our lives and fought for a better future. Is that what people in the East call a greater cause?”

“...!”

Magic Johnson was indirectly telling him that stopping the crisis looming directly ahead had to take priority over Ares Guild.

After a brief silence, Team Leader Choi answered,

“I’ll keep that in mind, Mr. Johnson. But my reason for targeting Ares Guild isn’t purely personal.”

“I know what kind of person Choi is. You intend to weaken Ares in preparation for the worst while strengthening the Peace Guild itself. You can’t swallow a tiger with teeth like that.”

Team Leader Choi gave a bitter smile.

“A hyena… I can’t deny it.”

Even though the central figure named Lee Jungryong was gone, Ares was still Ares.

The Peace Guild had grown explosively, etching its name into the minds of people around the world because of my existence. But it couldn’t tear down in one blow the impregnable fortress Ares Guild had built over decades.

“Keep increasing your strength without pursuing personal glory. The Wizard Guild and I will help you. If necessary, I can even introduce you to a few friends I know personally.”

“Yes. That’s what I intend to do. The bad blood from the past hasn’t run its course yet.”

“You mean that young fellow. Mr. Seok.”

Magic Johnson suddenly drew his brows together.

“Although I haven’t watched him closely for very long, I know he isn’t a particularly kind person. Isn’t that right, Jin?”

I nodded immediately.

“He’s a fucking asshole.”

“I could tell from his surname. Even the pronunciation sounds like ‘suck.’ I already had a bad feeling about him when he attacked Jin at the Arch Lich’s stronghold, while we were still investigating…”

Magic Johnson continued with a serious expression.

“But that fellow gives off an even more dangerous smell now than he did before. Jin, you were standing right in front of me. Didn’t you notice?”

“…”

“Jin?”

After hesitating for a moment, I answered,

“Well, I did fart in front of you.”

“What the fuck…”

“Even so, there’s no need to swear. And Go Jun was already a dangerous bastard to begin with.”

“Whew. That’s true. But from now on, please refrain from farting when I’m standing behind you.”

“...Yes.”

I had been uneasy about having Magic Johnson at my back too, but I had been the one to fart in the end, so I had nothing to say.

Magic Johnson’s nose twitched as I answered while subtly avoiding his gaze. Then he opened his mouth.

“All right. I think that’s enough for today. I want you two to know that, whatever anyone else may think, I trust you both completely.”

He looked warmly at Team Leader Choi and me before turning to the two people—no, the one person and one monster—standing there blankly and adding,

“Well, of course, you two as well.”

The Skeleton King and Im Kkeokjeong answered at the same time.

“Don’t take us to a gay bar.”

“I-I don’t speak English.”

“...Very reassuring.”

Magic Johnson muttered that with an expression utterly at odds with his words, then pulled a small glass bottle from inside his clothes and drained it in one go.

I realized that the bottle contained a potion for replenishing spent mana and asked,

“Are you leaving?”

“I should head back. I’m going to be quite busy from now on, too. I need to get in touch with some friends I haven’t seen in a while.”

“Your friends?”

“The ones I mentioned earlier. Half of them have retired, but they should still be able to help quite a bit. Oh. If Choi wants, I can take him to meet them right now. What do you say?”

Team Leader Choi hesitated under Magic Johnson’s eager gaze, then quickly shook his head.

“N-No, that’s all right.”

“What a shame. My friend Joseph was interested in meeting Choi.”

“I’m disappointed too, but maybe next time… Wait. Did you say Joseph?”

“Unless your ears have gone bad, you heard me correctly.”

“Then don’t tell me. Could you mean former United States President Joseph Biden?”

“That’s right. He retired a long time ago, but we meet about once a month and have a drink together. Though he’s so old he can barely drink anymore.”

“...!”

Team Leader Choi wasn’t the only one shocked. I gaped as well, and even Im Kkeokjeong’s jaw dropped.

“That Joseph Biden?”

“Ah, I know! I know Joseph Biden!”

I didn’t care whether the name of the American president was Chakumba Okumbo or Kim Cheol Soo, but I had heard the name Joseph Biden many times since my days at the Hunter training camp.

The Great Cataclysm had struck during his time in office, so he had suffered even more than the mayor of New York in a superhero movie.

*Look at the level of his connections.*

In the United States, he was practically the second Founding Father after George Washington.

I had known Magic Johnson was impressive, but I had never realized he could boast connections this extravagant.

“Don’t look at me like that. Joseph and I have been intimate friends for nearly fifty years, but most people don’t know about our personal relationship.”

“...!”

Team Leader Choi froze, and Magic Johnson hurriedly added,

“Forget I said ‘intimate.’ We’re just friends. Best friends.”

“Whew.”

“Shit. Do I really have to make excuses like this?”

“Mr. Johnson, we have a saying in Korea: you reap what you sow.”

“Damn it. I really got what I deserved. So, what are you going to do, Choi?”

Team Leader Choi answered without hesitation.

“Let’s go. I’ll impose on you.”

“Good idea. You might get a little motion sick traveling between continents, though.”

“What’s a little motion sickness compared to this?”

Team Leader Choi answered calmly and took the hand Magic Johnson held out to him.

With a light nod, an enormous amount of mana wrapped tightly around their entire bodies.

*Whoooosh!*

At that exact moment, a blinding flash erupted and sent their figures flying somewhere else.

*Brrrrrrr.*

The smartphones belonging to the three people left behind—Im Kkeokjeong, the Skeleton King, and me—began vibrating violently.
## Chapter artifact 561

# Chapter 561

*Brrrrrrr.*

A smartphone suddenly began vibrating. I, Im Kkeokjeong, and finally the Skeleton King checked the screen in rapid succession before opening our mouths one after another.

“What’s this?”

“T-Taekyung!”

“Oh. Ohoho. Look at this, you uncivilized humans. A girl-group member has sent this body a DM.”

“…”

“…”

*That fucking bastard, seriously. I told him to stop screwing around on social media.*

*No wonder the phone of some bastard who isn’t even in the group chat was ringing.*

I felt like stomping him until his illusion magic shattered, but that wasn’t important right now.

*Which girl-group member… No. That’s not it. Another incident like this?*

I barely swallowed my thoughts and stared at the smartphone screen.

It was the group chat for the early members of the Peace Guild, including Team Leader Choi and me. Song Song had urgently posted some information there.



> **Peace Guild**
>
> **Song Song**
>
> Hey hey heyyy
>
> C-rank Gate anomaly.
>
> Just got contacted through the government hotline.
>
> They say the mana levels are skyrocketing.
>
> Shit; why aren’t you reading this?
>
> If you read it, answer me, you crazy bastard.
>
> **Butler Kim**
>
> Sorry. I am at the Blue House right now.
>
> **Song Song**
>
> S-sorry;; I didn’t know it was you, Butler Kim;;; Go take care of your business……
>
> **Butler Kim**
>
> Yes. You have a happy day too, Song-i. ^^
>
> **Song Song**
>
> Huh. Everyone but one person has read it?
>
> Whoever has read this, get over there and check it out as quickly as possible.
>
> It’s far away, and I have things to deal with, so I probably can’t go right away.
>
> **[Map attached]**
>
> ?
>
> Ah, but now that I look at it, that Gate is kind of…
>
> Just go check it out.
>
> Especially you, Jin Taekyung. Reply as soon as you read this.

*Where is it?*

What kind of Gate could make her react like that?

I put my questions aside, left a reply saying I had seen the message, and checked the attached map. The moment I did, I understood why Song Song had reacted that way.

“Ah. Hmm.”

The location was definitely a little… awkward.

Im Kkeokjeong checked the map a beat later, and his expression hardened as well.

“Taekyung. Is this place, by any chance…”

“It’s probably exactly where you think it is.”

The C-rank Gate marked on the map was in a prime location near a subway station in Bucheon. It was also one of those places that benefited from the so-called “luck” Hunters talked about.

The monsters that appeared there were relatively easy to deal with compared to those in other C-rank Gates, and Magic Gems dropped frequently.

There was no way either Im Kkeokjeong, who had worked as a Hunter in Bucheon for over ten years, or I could fail to know this Gate.

The same went for the Guild that owned it.

“This isn’t exactly welcome news…”

At Im Kkeokjeong’s low mutter, the Skeleton King looked up from the smartphone he had been busily fiddling with.

“Humans. Where is this place that you are making such a fuss over?”

I answered quietly.

“The location isn’t the problem. The owner is.”

“Hm? The owner?”

“That’s right.”

Gates could not be privately owned, but starting with the mid-sized Guilds, Guilds acted as their de facto owners under the name of long-term leases.

And there wasn’t a person in Korea—or anywhere else in the world—who didn’t know the Guild that owned the C-rank Gate indicated by this address.

“Then who is the owner?”

At the Skeleton King’s question, Im Kkeokjeong tossed out a short answer.

“Ares Guild.”

For a moment, my gaze shifted involuntarily to his arms.

The arms that had been severed at someone’s command were attached cleanly, as though nothing had ever happened. But they were trembling faintly, as if he had recalled the pain of that day.

“Kkeokjeong Uncle. No—hyung.”

“…I’m fine.”

It was an empty answer.

The tremors running through his body were growing stronger, and his dark expression was proof enough.

As if he had noticed my deeply lowered gaze, he forced his expression to relax.

“I said I’m really fine. More importantly, hurry up and go. If the mana levels have skyrocketed, another Mutated Gate could appear.”

“…No. They’ll handle it themselves.”

*How can I go in this situation? And not to help anyone else, but those bastards.*

I stood rooted to the spot, unable to move. Im Kkeokjeong gave me a faint smile.

“Taekyung.”

“Yes?”

“When I said I was fine, I wasn’t just saying it. The people who cut off my arms, including Lee Jungryong, all paid for their crimes. My rehabilitation training is practically finished, too. These days, I’m happy just spending time with my wife and watching the kids grow up.”

“Hyung…”

“I’m really fine, so hurry up and go. There must be plenty of good people in Ares Guild, too. If you let a petty personal reason stop you from helping, you’ll regret it for a long time. At least, the Taekyung I know would.”

“…!”

“I’d like to help, too, but I can’t. My rehabilitation isn’t finished, for one thing, and more importantly, I’m just not strong enough.”

I quietly watched Im Kkeokjeong laugh heartily alongside that forced joke. Then I nodded.

He was right. The people facing danger inside the Gate were not enemies of me or the Peace Guild.

If I sensed danger and possessed the strength to save someone from it, then stepping forward was the right thing to do.

*That’s what we created the rescue team for.*

Maybe the moment I obtained the System, what I had to do had already been decided.

I gave Im Kkeokjeong a brief look of acknowledgment.

“I’ll be back soon.”

“All right. Don’t get hurt.”

“Deal with it quickly and return. As a reward, I shall show you a selfie of this girl-group member.”

I smiled warmly and spoke to the Skeleton King.

“Quit screwing around and follow me. Otherwise, I’ll smash your smartphone as punishment.”

“…Understood.”

*I should’ve done this from the start. You trying to get yourself killed?*



* * *



When we arrived at the C-rank Gate *Orc Wasteland*, indicated by the map Song Song had sent, the area was already filled with panicked voices and shouting.

“The mana levels have risen to more than twice their normal level!”

“I know that. What about the support request?”

“They say it hasn’t come through yet!”

“Goddammit, there have to be people left at the Bucheon branch! Tell them to send at least one A-rank Hunter and request it again!”

“We already passed that along, but most of the A-rank Hunters stationed in Bucheon are deployed overseas, and some of the others are on vacation, so they’re refusing…”

“What? Vacation? They’re refusing because they’re on vacation? You fucking—!”

It happened in an instant.

A fist filled with rage slammed into a parked car.

*Bam!*

With a thunderous crash, the foreign car worth more than a hundred million won crumpled, sending large and small fragments flying in every direction.

That was when the red-faced, wheezing B-rank Hunter spotted the Skeleton King and me.

“Hell, this is driving me crazy. No matter how urgent things are, they should still be controlling access properly—”

His voice trailed off, followed by a pair of bulging eyes.

“Huh? Uh? Huh? Huhhhhh?”

Question after question spilled from his lips, his gaze fixed on my face. The Skeleton King snorted and opened his mouth with a meaningful expression.

“Heh heh. Yes, this human is that very human.”

“…?”

*Why is this bastard stepping in and making a scene when I’m just standing here?*

I looked at the Skeleton King suspiciously and cleared my throat.

By then, everyone who had been rushing around busily had frozen and was staring in our direction.

“Ahem. I’d like to say a few words in case anyone here doesn’t know who I am…”

“Jin Taekyung!”

“Lord Fuck!”

“Lord Sibu-leol!”

“…but I suppose that won’t be necessary.”

Well, as strange as it was to say it myself, by now, if there was a Hunter who didn’t recognize my face, I had to wonder whether they were actually a monster.

“Is, is that really Jin Taekyung?”

“I doubt there’s a fake Jin Taekyung.”

“Ah, that’s not what I meant…”

“It’s fine. That isn’t important right now, either.”

I turned toward the B-rank Hunter who had destroyed the car.

“From what I’ve seen, you appear to be the person in charge here. Is that right?”

“Y-Yes, that’s right. My name is Gwak Hangu, the Branch Leader of Ares Guild’s Yeokgok Branch.”

Not even the Bucheon Branch Leader, but one of the dozens of lower Branch Leaders beneath him was a B-rank Hunter.

It was a fresh reminder of Ares Guild’s talent pool and sheer size. Along with another fact I had briefly overlooked.

*Maybe because of their public image, but the atmosphere here is better than I expected.*

Ares Guild, I, and the Peace Guild were bound together by a terrible history.

But in the end, that battle had taken place beneath the surface. To people who knew nothing about it, the surface was peaceful and calm.

No. If anything, the eyes of the Ares Guild members here held expectation and even goodwill.

*Maybe we can build up our strength faster than Team Leader Choi expected.*

But something more important was waiting right now.

I pushed the thought that had suddenly crossed my mind aside and spoke to the Branch Leader.

“Let’s cut out all the side issues and get straight to the point.”

“Y-Yes?”

“Guild support is difficult right now, isn’t it? Ares Guild isn’t responsible for just one or two Gates, after all. You’re also sending personnel overseas.”

“Pardon?”

“Even if you send people now, they’ll arrive too late. That A-rank Hunter who’s on vacation has probably switched off his phone and pager and is having a good time. And if the people here rush in, there’s a high chance they’ll all die without even being able to perform a rescue. Am I right?”

“That, that’s not something we know…”

“Don’t give me that. What we don’t know is how long the people inside can hold out.”

The Branch Leader gasped.

“It’s been fifteen minutes since the mana levels first began rising. The team members inside might already be dying.”

“W-Wait a moment.”

The B-rank Hunter barely managed to stop me before continuing in a trembling voice.

“I know. I know that, too. But… outside intervention is a serious violation of Guild policy.”

“So?”

“Everyone here, including me, desperately wants to ask you for help. But we can’t. You already know that. You’ve heard about it.”

I did know.

Anyone who worked as a Hunter had to know how strict and difficult Ares Guild’s rules were.

Lee Jungryong had selected only the most capable Hunters from each rank and locked them inside a tall, enormous cage. The fact that no Guild would accept a Hunter expelled from Ares Guild wasn’t some vague urban legend.

“Ha…”

“Goddammit…”

Sighs and curses rose from various places. I stared at the Ares Guild members, then suddenly opened my mouth.

“One person? Or two?”

“Huh? What are you—”

“I have a feeling two people have died while you were hesitating.”

“Mr. Jin Taekyung!”

“Hey, you measuring over there. What are the mana levels now?”

Despite my arrival, one C-rank Hunter had been anxiously biting his nails in front of the measuring device. He now shouted as though screaming.

“Three times! It’s broken through three times the average mana level!”

“…!”

No one present failed to understand what that meant.

*Mutated Gate.*

The third Mutated Gate to erupt in the week since the new year began.

I clicked my tongue softly and looked straight at the Branch Leader.

“What are you waiting for? Open it.”

“…!”

“I wasn’t going to enter without the person in charge’s consent because it would be illegal. But people need to be saved, don’t they? So just say that I barged in while making a huge fucking scene and open it right now.”

His eyes squeezed shut. His tightly clenched fists trembled.

As I turned away from the silent Branch Leader, a trembling voice came from behind me.

“Let’s say… that I gave my consent.”

I thought he was a complete moron, but this put him at least in the category of a fool.

I let out a short laugh and left him with one final remark before striding toward the Gate.

“Call me if you get fired. The Peace Guild will take you in.”
## Chapter artifact 562

# Chapter 562

It was a wasteland stretching endlessly in every direction.

There was no sun, but dark light formed from mana hung in the air. Hundreds of orcs roamed in packs, only to be hunted down by Hunters.

Or rather, that was what had happened here once.

*Boom. Boom. Boom.*

The ground trembled. The mana consuming the area swelled as though it might burst at any moment, squeezing the breath from their lungs.

The Hunters panted raggedly, their breath carrying a sickly sweet smell.

More than a hundred orcs already lay sprawled around the Hunters, who stood back-to-back in a circle. But beyond them, a monstrous army ten times their number was advancing.

“T-Team Leader.”

“Don’t worry. We’ll get out of here somehow.”

The Team Leader’s reply to the frightened Hunter was hollow.

The person asking and the person answering both already had a vague idea of the truth.

None of them would make it out of this place alive today.

Even if they miraculously broke through the monster army’s encirclement, there was one opponent they would never be able to bring down.

*—Kraaaargh!*

The Orc Lord.

At the roar of the powerful mutated individual said to be born only once in a million chances, more than a thousand orcs let out shrieks and struck their weapons together.

*—Chweeek!*

*Clang! Crash-crash-crash!*

Despair flickered in the Hunters’ eyes as they watched.

*It’s over.*

They were facing an army of monsters made even more powerful under the Orc Lord’s command.

With a powerful commander at their head, the orcs were no longer a rabble that merely wandered around in groups of a few dozen. And the Hunters numbered fewer than twenty.

*This is… a fight we can’t win.*

The thought flashed through everyone’s mind at once.

Even if they were elites capable of overwhelming Hunters of the same rank, that fact would not change.

Their pride in belonging to Ares Guild crumbled helplessly before the death approaching them.

“……Damn Mutated Gate.”

As someone muttered those words, the monsters filling the area began charging all at once.

At the very front was the Orc Lord, a monster so hateful that killing it would never be satisfying enough.

*—Karchwi! Kalipto!*

*Rumble-rumble-rumble!*

The massive body shot forward alongside unintelligible words in the Demon Realm language.

The raid Team Leader gritted his teeth, raised his shield, and charged to meet it.

His team members shouted for him from behind, but he drew every ounce of his strength and concentration toward the enemy in front of him.

“Come on!”

It was a great shout, forced out to drive away his fear.

The moment red light flashed in the Orc Lord’s eyes, the enormous ax in its hands came crashing down toward the Team Leader’s crown.

*Whooosh—crash!*

One strike.

That was all it took.

The blow was unbelievably fast and powerful. With a thunderous roar, it shattered the **Tower Shield** reinforced with high-grade enhancement magic.

The Team Leader’s eyes widened. He forgot even the pain of both arms breaking.

*Whoooosh.*

The ax had not even reached him, yet it already felt as though his side had been sliced open.

The world slowed around him as his life flashed before his eyes. A second attack was hurtling toward him, one that would cleave him in half at the waist.

*No. Not a second attack. The last attack.*

The Team Leader closed his eyes.

He had no desire to spend the last moment of his life looking at this ugly, fucking monster.

And then, in the next instant—

Along with the pitch-black darkness blocking his vision, a sharp sound of something cutting through the air pierced his ears.

*Fwoooooosh—crack!*

The pain he had been waiting for never came.

It was so strange that even he doubted whether this was really death.

“……?”

The Team Leader opened his eyes to narrow slits and stared blankly with his mouth hanging open.

Less than five paces away, the three-meter-tall body of the Orc Lord stood frozen in place.

Its head was gone.

“……!”

“……!”

It was as if the world had stopped.

Humans and monsters alike had ceased moving as they stared at the sight.

At that moment, only one thing moved across the endless wasteland.

*Rrrrrr.*

A single spear that had blown apart the Orc Lord’s head, pierced through the ground, and now trembled violently.

The Hunters there knew who owned that spear, which gave off a soft, almost mystical light.

*Jin Taekyung!*

Along with the name that flashed through their minds like lightning, the spear lodged deep in the ground shot upward and flew into someone’s grasp.

*Fwoooooosh—tap.*

As though they had agreed beforehand, the people slowly turned their heads.

Only then did they realize.

“Lambs wandering through the Mutated Gate. Run your asses off and get behind me.”

The shadow of death that had been looming right before them had vanished without a trace.



* * *



*Tap. Tap.*

The middle-aged man’s stride was confident and unhindered.

Even after entering the interior of the skyscraper overlooking the Blue House and the National Assembly at a glance, nothing changed.

“If you’re a Guild member, please present your access pass first—”

“I haven’t seen your face before. Are you new?”

“Pardon? Yes. Yes, I am.”

“Thought so. You must be new if you’re acting like this. Looks like your Team Leader didn’t tell you.”

The Security Team Hunter, who had been staring blankly at the middle-aged man, sucked in a startled breath.

“I’m sorry. I didn’t recognize you—”

“It’s fine. I’m busy, so move.”

“Y-Yes, sir.”

Not even the security checkpoint that everyone, outsider or insider, had to pass through could stop the middle-aged man.

He gave the Security Team Hunter, who was hurriedly bowing, a sidelong glance before continuing toward his destination.

A voice was already coming through the tiny communication device implanted below his ear through a simple operation.

—He’s waiting for you.

The middle-aged man’s lips moved slightly.

“Where?”

—Section A.

The 150-story skyscraper had no section called A anywhere on its design plans or interior signs.

It was a space granted only to a very small number of people among the countless Guild members.

Naturally, the middle-aged man was one of them.

“Open the Teleport.”

—It’s ready. By the way, about that new Security Team recruit, Deputy Team—ah, sorry. Team Leader.

“It’s fine. Don’t worry about it.”

*Even I’m not used to it yet, so what can you expect?*

As the middle-aged man silently muttered the rest to himself, the person on the other end continued.

—In any case, I’ll notify the Security Team Leader and have the individual disciplined.

It was not a report or a suggestion. It was a notification.

The word had become ordinary at some point, but it still felt unfamiliar. The middle-aged man frowned faintly.

“Is that really necessary?”

—Team Leader?

“……Never mind. Handle it however you see fit.”

—Yes. I’ll take care of it appropriately.

“Appropriately” meant a pay cut at minimum, or possibly demotion.

The middle-aged man thought briefly of the young man who had stopped him and felt a twinge of discomfort in one corner of his heart.

But there was nothing he could do.

That was the policy of the Guild he belonged to.

No—their policy.

*It’s been getting worse ever since that incident.*

He had long known that the Guild was ruled with an iron fist, but its grip had tightened even further since the recent unfortunate incident.

Perhaps it was the impatience of a new king whose legitimacy had not yet been fully acknowledged by his subjects.

The middle-aged man let out a small sigh and spoke as he walked.

“Give me a report on the VIP’s current condition.”

—He is in a bad mood.

“Am I imagining things? I feel like I heard something similar yesterday.”

—……Well, after reading this morning’s newspaper, he—

“That’s enough. Send me everything the VIP is reading. Scrape it all and send it to me. Right now.”

The moment the middle-aged man finished speaking, the smartphone protected by security magic began vibrating as though it had been waiting for his order.

He tapped the screen lightly. The headlines of more than twenty morning newspapers that had left the presses only two or three hours earlier filled the display.



> An Unprecedented Crisis… What Do the Successive Mutated Gates Signify?

> Ominous Signs. Will the Nightmare of China’s Sichuan Province Reach Korea?

> Emergency Blue House Announcement: “To Prevent Any Unforeseen Incidents, We Have Signed an Agreement with the Peace Guild. The Results So Far Are Encouraging.”

> The Third Mutated Gate. Yet Zero Fatalities? Worldwide Praise for the Peace Guild’s Emergency Rescue Team.

> American Grand Mage Magic Johnson: “The Peace Guild Is the Light of a New Age. Jin and Choi Are Good, Upright Young Men.”

> Former U.S. President Joseph Biden: “South Korea Is an Unquestionable Hunter Powerhouse and Home to Wonderful Young People Who Will Lead This Era. The Choi I Met This Time Is One of Them.”

> Chinese Chairman Xiao Yang: “Mr. Choi Is Another Unsung Hero. We Remember How He Risked His Life Fighting in Sichuan.”

> Japanese Prime Minister Shinjirō Koizumi Also Mentions Choi on Social Media: “As Far as I Know, Choi Is Korean. Therefore, He Is Not Japanese.” Domestic Netizens React: “Thank God He Isn’t One of Our Idiots.”

> Unprecedented Interest Following Statements from One Powerful Figure After Another: “Who on Earth Is the Choi They’re Talking About?” Sources Confirm That He Is Choi Minwoo, Team Leader of the Peace Guild……

> S-Rank Hunter Jin Taekyung Attends New Year’s “Communicating with the People” Press Conference with the President!

> .

> .

> .

“……Whew.”

After reading every article, the middle-aged man rubbed his dry, aching eyes.

The fatigue he had forgotten about seemed to come rushing back.

“Damn it.”

—Have you finished reading?

“Yes. It would probably have been better if I hadn’t read them.”

—……I’m sorry to interrupt, but you should hurry.

“I was about to. I’m almost there.”

*Tap.*

As he answered, the middle-aged man stepped onto a magic circle radiating a faint light.

He authenticated his fingerprint and infused it with mana. The Teleportation magic circle recognized its user and released a powerful flash.

*Flash!*

A sensation like his entire body floating into the air seized him amid a dazzling halo of light.

And in the next moment, the middle-aged man opened his eyes and realized that the Teleport to Section A had succeeded.

The interior was decorated with pure white marble and Magic Gems. Around a dozen men and women in tailored suits bowed toward him.

“Welcome, Team Leader.”

There were many people, but only one voice.

The middle-aged man glanced at his subordinates, who moved like machines, and slowly stepped off the magic circle.

“Where’s the VIP?”

“He is alone in his private office.”

“Without any security? I clearly told you to keep at least three people stationed in the hallway—”

*Boom!*

A faint roar echoed from somewhere, abruptly cutting off the rest of his sentence.

The middle-aged man roughly guessed what had happened and clicked his tongue.

“I’ll go. Leave one person behind and clear Section A.”

“Yes.”

His subordinates began moving in perfect order as soon as the command was given. Leaving them behind, the middle-aged man started down the wide corridor.

At least fifty Magic Traps had been installed throughout the hallway to guard against intruders. But the access card hanging around his neck concealed a device that allowed him to pass safely through the minefield.

*Bzzzt.*



> **Head of Security Go Se-won**



As a red radiance swept over the area, the mana boiling all around him settled in an instant.

The middle-aged man, Go Se-won, crossed the seemingly endless corridor with practiced ease and stopped in front of a tightly closed door.

*Knock, knock.*

“This is Go Se-won.”

A sharp voice came from beyond the door.

“Come in.”

Go Se-won slowly grasped the doorknob and pushed it open.

At the center of the office, which had been wrecked as though a bomb had exploded inside, a man sitting on the sofa stared at him with red light glowing in his eyes.

“You’re later than usual.”

Go Se-won silently bowed his head.

Amid the scattered wreckage, a nameplate flashed.



> **Ares Guild Vice Guild Master Go Jun**
## Chapter artifact 563

# Chapter 563

“You’re later than usual.”

Go Jun was wrong. Go Se-won’s watch was always accurate, and there was still plenty of time before the designated start of the workday.

So it wasn’t Go Se-won who was different from usual. It was simply that his superior was in an unusually foul mood today.

Still, Go Se-won kept his words to a minimum and quietly bowed his head.

“I’m sorry.”

“Enough. Sit down.”

Being allowed to sit on the same sofa as Go Jun was one of the privileges reserved for his closest aides.

But before Go Se-won could even sit down on the Italian leather sofa, he realized that his superior’s anger had not yet run its course.

> “This is reporter Go Hyeon-woo of Rough News.”

The reporter in his early thirties who had been given the floor in the holographic television broadcast continued speaking smoothly.

> “It has only been ten days since the new year began, yet three Mutated Gates have already appeared. What are your thoughts on this, Mr. President?”

Go Se-won’s gaze naturally shifted to the side.

Go Jun’s face was stiff, and his eyes were bloodshot. He was glaring at one person in the holographic footage.

*Ah.*

One of the articles he had seen on the way there suddenly came back to him. It had announced that Jin Taekyung and the President would be holding an official New Year’s press conference.

He had more or less guessed what was happening, but watching the broadcast in his current state was no different from forcing Go Jun to swallow deadly poison.

*Like showing a snuff film to a child.*

Go Se-won had made up his mind and was bending down to pick up the remote from the floor when—

“Head of Security.”

The curt voice stabbed into his ear. Without taking his eyes off the television, Go Jun tossed out a single word.

“Leave it.”

“…I’ll only put it back.”

Go Se-won paused for a moment, then brushed the shards of glass off the remote and placed it on the table in front of the sofa. By then, a middle-aged man in his early forties had begun speaking on the holographic television.

> “That’s an excellent question.”

His voice was pleasant to listen to. His expression was kind, but not the least bit weak.

Baek Hanseong, the twenty-seventh President of Korea and the youngest person ever elected to the office at the age of forty, continued in a gentle tone.

> “As anyone who saw the Blue House’s official announcement yesterday afternoon will know, the series of Mutated Gates that have appeared this time—”

A calm, unruffled attitude naturally inspired trust.

One of President Baek Hanseong’s specialties was delivering stirring speeches in a compelling voice, with bits of humor slipped in here and there so subtly that people weren’t sure whether he had meant them as jokes.

No wonder everyone was paying attention.

When the speech finally ended after what sounded almost exactly like his declaration of candidacy for president, vigorous applause erupted among the reporters.

“It’s practically a campaign rally.”

Go Jun spat out the words, anger and mockery mingling in his voice. Then he muttered,

“How many of those bastards in there haven’t taken the fucking money we gave them, huh?”

“……”

“They couldn’t even breathe properly when Master was around. The youngest president in history? Anti-Ares Guild? That bastard Baek Hanseong was still beneath Master’s feet in the end.”

Humiliation and rage poured from his voice—emotions that had never been visible in him before.

Go Se-won lowered his eyes in silence and felt his thoughts grow cold.

*It’s true. Even if it has become a story from the past now.*

Lee Jungryong’s influence had been overwhelming.

Before Cheon Taemin disappeared, he had shown little interest in worldly affairs and seemed like an immortal living above the clouds. Lee Jungryong, on the other hand, had remained on the ground and enjoyed a status on par with—or even above—that of a president or king.

*Yes. That was how it was back then…*

Politicians. Business leaders. Even the masters of the enormous Guilds that had risen rapidly as a new power class had bowed before Lee Jungryong.

He had been a hero who accomplished incredible deeds at Cheon Taemin’s side, and, as the sworn brother of the vanished savior, he had been no different from a pope entrusted with absolute authority.

*Another Vatican.*

The people of Korea called the 150-story skyscraper a second Blue House, but in reality, it was closer to the Vatican where the pope lived.

Even those who cursed the incompetent government and lawmakers found it difficult to speak freely in the presence of the name Ares Guild.

It had been practically sacrosanct.

But—

> “This world! The entire world! Is changing even now! We have entered a new phase!”

Everything was changing, just as the President shouted while receiving endless applause from the crowd on television.

With the fall of the giant known as Lee Jungryong, the shadow he had cast over the world was beginning to recede.

And at the center of all these events, one person’s presence was exerting a powerful influence.

> “However, my fellow citizens! The government, myself included, will do everything in our power to protect your safety! Together with the young man sitting beside me! Together, we will protect Korea from every threat, both within and without!”

President Baek Hanseong did not call the young man by name, but everyone knew who he was.

Over the past few months, the young man in his late twenties had become one of the most famous people in human history.

> “Waaaaah!”

> “Jin Taekyung! Jin Taekyung!”

> “Fuck! Fucking fuck!”

The cheers that shook the press conference hall were louder than ever.

The young man who had been sleeping with his chin propped at an angle suddenly opened his eyes. Then he began clapping at a frantic speed while staring at the President.

> “That was truly an incredible speech, Mr. President. Especially your final words. They moved me so deeply that I feel—”

> “Um, that last part was about you, Hunter Jin Taekyung.”

> “Ah, wait a moment. My stomach really is churning. I think I’m suddenly getting motion sickness.”

> “All of this is being filmed. Please wipe the drool off your face first—”

> “Please edit that out. Please. All right?”

> “I told you several times before we started. This is live.”

> “Right. Wow, fucking hell. I’m screwed.”

> “It’s live. I said it’s live, please. Hunter Jin Taekyung. Hello?”

The sight of the sweating President in his forties and the young hero in his twenties was broadcast in its entirety.

It was a broadcasting accident that would go down in the history of Korean television, but no one would scold or curse Jin Taekyung for it.

Even now, the people caught on camera were not frowning. Instead, they were shouting his name with faces full of laughter.

*Jin Taekyung.*

Watching the scene, Go Se-won suddenly realized something.

The young man on the holographic television and the reactions of the people surrounding him resembled a word that had come to mind only a moment earlier.

*…Sacrosanct?*

Compared to the sun that was Cheon Taemin, Jin Taekyung was still nothing more than a torch.

But one thing could not be denied.

Jin Taekyung was walking the same path as the man who would be remembered as an immortal hero.

And perhaps, regardless of Jin Taekyung’s wishes, the circumstances around him were trying to turn him into a second Cheon Taemin.

> “Mr. Jin Taekyung! I heard you suppressed all three Mutated Gates that appeared this time by yourself! Would you say a few words about that?”

> “I wasn’t alone. There were two of us, though—”

> “Mr. Jin Taekyung! This is Kim Jin-mu of the Mudang Daily!”

> “I have a question about the Mutated Gates!”

The reporters holding microphones rushed toward him like a swarm of bees, and camera flashes erupted without pause.

As Go Se-won listened to the questions from every direction, he suddenly felt a sense of déjà vu.

*This is…*

Something about the flow was strange. At first glance, it seemed natural, but everyone was racing in a direction someone had deliberately chosen.

Then, when he heard a shout from some unknown reporter, a chill ran down Go Se-won’s spine.

> “I have a question about the third Mutated Gate you suppressed two days ago! According to information obtained by our newspaper, that Gate was being handled by a famous Guild—”

“……!”

*This is it. So this was it.*

The moment enlightenment flashed through him, Go Se-won hurriedly reached for the remote.

But someone else’s hand moved faster.

*Crunch!*

Go Jun crushed the table along with the remote. A red glare flashed in his eyes.

“I believe I told you to leave it alone.”

“But, Vice Guild Master—”

“I won’t say it twice.”

The blood vessels in his superior’s eyes had burst. The voice that followed was so chilling that it raised goose bumps.

“Stay still if you don’t want to die.”

“Ghk—!”

Go Se-won swallowed a breath without meaning to and leaned back against the sofa as though his half-raised body had collapsed.

Meanwhile, the situation he had feared was unfolding on the holographic television.

> “That’s right. It was a Gate handled by Ares Guild. Well, technically, it was under a permanent lease. But as everyone knows, that’s practically the same as owning it.”

The giant Guilds’ monopoly over Gates was an open secret. Everyone knew about it, but no one spoke openly.

Yet Jin Taekyung had not only exposed that ugly truth without hesitation during a live official press conference at the Blue House—he had gone one step further.

> “The exact circumstances? The mana levels kept rising, but the rescue team never came.”

The reporters who had spotted their prey rushed forward one after another.

Quite a few of them had once taken Ares Guild’s black money, but money always gave way to more money.

> “Wait, wait a moment. Are you saying the rescue team never arrived?”

Jin Taekyung nodded.

> “Yes. They still hadn’t come fifteen minutes after the initial situation began. In the meantime, the mana levels kept rising until the Gate became a Mutated Gate.”

> “Does that mean the Gate could have been dealt with before it fully mutated if the rescue team had arrived in time?”

> “Well, I can’t be a hundred percent certain, but if they had sent in even one A-rank Hunter early on, there probably would have been a high chance of resolving it without outside assistance.”

> “Unlike the other Mutated Gates, the Guild responsible for this Gate is known to possess an enormous number of Hunters and vast financial resources. Why do you think it failed to send a rescue team in time?”

> “The reason… Well, I’m not sure.”

Jin Taekyung thought for a moment before casually tossing out his next words.

> “That family seems to be having a lot of trouble these days. Or should I say, the boss? Their management has changed, too, so I imagine there was probably some confusion here and there.”

*Crack!*

Hearing something beside him being crushed, Go Se-won slowly closed his eyes.

*It’s over.*

A certain giant Guild with enormous manpower and capital. A change in management.

Those two key phrases alone were enough. Anyone who knew anything would understand, even without looking it up online.

Although the exact name had not yet been revealed—

> “It was a serious mistake, but what could I do? Fortunately, I happened to be there, so no one died. Personally, I’m just glad about that. Oh, and while I have this opportunity, I’d like to once again offer my deepest condolences to the deceased.”

> “That was an excellent answer, Hunter Jin Taekyung. I have no doubt that the deceased would also be grateful and proud.”

*Damn it.*

Go Se-won muttered a quiet curse inwardly and opened his eyes.

On the television, Korea’s youngest President had taken the microphone again and was delivering the final blow.

> “Fortunately, we were able to bring this incident to an end without any fatalities, but our government intends to take the initiative and begin a thorough investigation. As President of Korea—and as a citizen—I find this Guild’s negligent response deeply regrettable. However, the wishes and legacy of the deceased, who was a great hero, have been passed on in their entirety to Hunter Jin Taekyung—”

The President’s words did not reach the end.

No—in precise terms, Go Se-won could no longer hear them.

“……!”

The instant he instinctively took a defensive stance, powerful mana shot out at the speed of a beam and shattered the holographic television, tearing the surroundings apart.

*Kwa-gwa-gwa-gwang!*

The overlapping protective magic circles installed by ten high-ranking mages shattered. Bulletproof glass and everything else burst into pieces, then scattered as dust.

At the center of the collapse stood Go Jun, his eyes bloodshot.

“How dare you! How dare you! How dare you—!”

*Bang! Bang! Kraaang!*

Everything had its limits.

And that one sentence had just set fire to all the rage Go Jun had forced down and endured over the past several days since becoming Vice Guild Master.

“I’ll kill him! I’ll kill him no matter what!”

*Kwaaaang!*

Go Jun was Lee Jungryong’s de facto successor.

But the people who watched today’s press conference would think differently.

They would believe that Jin Taekyung was the new hero—and the only person who had inherited the will of Cheon Taemin, who had still not revealed himself, and Lee Jungryong, who had died only recently.

“Jin Taekyung! Jin Taekyuuung!”

Go Se-won stared at Go Jun as he screamed until he seemed to be spitting blood, having completely lost his reason.

His gaze grew dark and unfathomable.
## Chapter artifact 564

# Chapter 564

When a company grows, what is the first thing it should do?

Everyone would have a different answer, but every CEO has a dream tucked away somewhere in their heart.

Building their own headquarters.

*Or should I call it an expansion in this case?*

I was walking through the Guild House when I suddenly stopped and looked down at the scene unfolding below in the hallway.

“Hey, could you use gravity magic to lift some of these materials?”

“All right, listen up. Any former tanks here?”

“Me.”

“I’m one, too. Why?”

“Why do you think? To put you to work. If you understand, five F-ranks get over here. Add one or two E-ranks, too.”

*Grrrind. Boom!*

Smooth marble rose and fell through the air, while every swing of the muscle-bound giants’ sledgehammers smashed apart the solid concrete walls.

More than a hundred workers moved busily about. Maybe it was because they were all Awakened, but they worked at an incredible pace.

Of course, their wages were just as expensive. But to a young tycoon with deep pockets, it was little more than pocket change.



*Now that there are more people, the Guild House has gotten cramped.*

Team Leader Choi had casually tossed out that one remark a few days ago, then immediately taken action.

I heard he had bought up all the nearby plots of land, even paying above market value, and begun a massive expansion. As for me, I could only shrug.

*It’s not like any of my money is going into it.*

And there were other places where my money would be going.

My fifty trillion in assets, not a penny of which had been taken in taxes, was slowly shrinking depending on how I used it. But compared to what remained, the amount spent was barely a drop in the ocean.

*Fifty trillion…*

Even thinking about it again, it was an absurd amount of money. Like the figure of a man gradually approaching from beyond the corridor.

*Swoosh.*

A huge man glided through the air like a ghost before suddenly speaking.

“Hey, I watched the press conference.”

“……”

*Wait. What are you doing here, hyung?*

I stared at Magic Johnson in disbelief, then finally managed to open my mouth.

“What is it?”

“Why?”

“Why? That’s what I want to ask you. Why are you here again today?”

“I had something to take care of.”

“You didn’t come because you needed to use the bathroom, did you?”

“Of course not. I came to give Choi something. I figured I’d check on the progress while I was here.”

“Do you put emails in cereal and eat them?”

“Surely you’re not uncomfortable because I’m here?”

“Surely you didn’t think I was comfortable?”

Magic Johnson sighed deeply at my immediate retort.

“Hey, Jin. Sensitive people like me get hurt when they hear such harsh words.”

“…Hurt?”

I looked at his thick neck and iron-hard, bronze-colored arms.

*He looks like a knife couldn’t even get through him.*

*Damn, that Black dude is jacked.*

With a physique like that, he could quit being a mage and switch to being a melee Hunter right now.

And I wasn’t just saying that. Even if you searched for “Magic Johnson’s staff” on the internet right now, page after page of related videos would come up.

Practically everyone had heard the story about how he had smashed an ogre’s skull with a single blow using a staff designed for casting magic. Even the fitness community was divided over exactly how heavy that staff was.

*That man is calling himself sensitive? Give me a break.*

Magic Johnson realized what my deep stare meant and shook his head.

“It’s not the body. It’s the heart. The heart is what matters, Jin.”

“A sensitive person couldn’t survive the Great Cataclysm. You survived this long and became a hero because you’re strong.”

“Hmm. I can’t tell whether that was a compliment or an insult.”

“Take it as a compliment.”

Magic Johnson gave me a suspicious look before continuing.

“Anyway, I watched the press conference. It was quite meaningful.”

The press conference…

I scratched the back of my head, embarrassed.

The official Blue House press conference I had attended at the President’s request had caused an enormous stir.

I heard domestic viewership had broken seventy percent, while it had also become a major topic in the foreign press.

Even two days later, the related search terms were still firmly near the top of the real-time rankings. They probably would be a week from now, too.

“The broadcasting accident probably helped, and the ratings did turn out pretty well. I didn’t know you had watched it, Johnson.”

“Jin’s every move is always a topic of conversation in the United States. For some people in particular, President Baek’s final words must have sounded quite meaningful. I was one of them, of course.”

“Oh, that.”

“I was wondering why he was praising Mr. Lee so much. Then he landed one hell of a blow, didn’t he?”

“Well, I wasn’t the one who landed it exactly… But I’m sure it really got under Go Jun’s skin.”

The world was no longer in the Warring States period, but legitimacy was still necessary for anyone who wanted to inherit a massive organization.

And in that respect, Go Jun, who had taken office as Ares Guild’s new Vice Guild Master, had very little legitimacy.

“Ares Guild is a vast empire. Even if he inherited the shares according to the will, he didn’t inherit all of Mr. Lee’s influence. If they had shared blood, he would at least have met certain expectations in Asian society. But he doesn’t, does he?”

“Lee Jungryong did have a son, but I heard he died young. Even if he had still been alive, he wouldn’t have inherited Lee Jungryong’s position, since he was an ordinary person who never Awakened.”

Modern Guilds were like Murim sects. Just as a bookish scholar could not become the Sect Leader of Huashan, only those with the power and authority of a Hunter could become a Guild Master.

Magic Johnson knew that as well as anyone and nodded.

“That’s right. On the other hand, that Sseokkochoon fellow has plenty of skill despite his character flaws. I heard he passed the S-rank Hunter qualification assessment with an incredible score this time. Of course, all the other issues erupting in succession these days quickly buried the news.”

“His name is Go Jun, not Sseokkochoon. And anyway, that bastard was Lee Jungryong’s Head of Security.”

“That’s nowhere near enough. He needs the support of the other founding heroes who made Ares Guild what it is today. But…”

“He didn’t have enough time.”

“Exactly. Time. Even while preparing a will in case of the worst, Mr. Lee probably never imagined that he would die so easily.”

But he had died in the end, and Go Jun had inherited the crown before he could firmly establish himself as the successor.

Being Head of Security was proof that he had been one of Lee Jungryong’s closest aides, but there were many difficulties involved in inheriting an enormous organization like Ares Guild.

Even with Lee Jungryong’s will, it would not be easy for elderly veterans to respectfully serve a fresh-faced man in his thirties as their superior.

And on top of that, Go Jun himself had visibly begun to crumble after Lee Jungryong’s death.

*And in the middle of all that, his legitimacy was openly denied during an official Blue House press conference with seventy percent viewership…*

President Baek Hanseong’s single remark had been subtle and sharp.

He had indirectly criticized Ares Guild over the Mutated Gate while praising Lee Jungryong’s achievements and presenting me as the man who would carry on his legacy.

*The whole thing was rigged from start to finish.*

The press conference had been a joint production by President Baek Hanseong, who had shown an anti-Ares stance since his days as a lawmaker, and Team Leader Choi.

They had won over the reporters, handed them questions, and led the conversation in the direction they wanted.

A script and cast prepared with absolute thoroughness from beginning to end.

If Lee Jungryong had still been alive, the scenario would have been scrapped. But Go Jun did not have the power to suppress the rebellion of a new underdog, so we had managed to finish the shoot without incident.

With the excellent domestic rating of seventy percent and the full glare of the foreign press upon us.

“Either way, it’s another small victory. This would be the time to celebrate with a glass of champagne. Where’s Choi?”

“He was busy before, but these days he’s especially swamped. If we’re lucky, he might be in his office right now.”

“He’s not.”

Magic Johnson shrugged and added,

“I just stopped by there on my way here.”

“Ah. So something else must have come up.”

It was hardly surprising. Team Leader Choi might have been called a team leader, but he had effectively been the Guild Master from the beginning, and by now, that was how the public saw him, too.

He was probably one of the busiest people in all of Korea.

“Hey, Jin. Want to walk together?”

“Sure. As long as we avoid secluded places.”

“You’ve gotten funnier.”

“……”

“Tell me that was a joke.”

I silently increased my walking speed. Magic Johnson followed behind, stepping through the air as though he were floating, and grumbled.

“Jin, why do you keep making me seem like a strange person?”

“Because you keep saying strange things.”

“Obviously, I’m joking. And I have preferences, too, you know. You’re not my type. That guy over there might be, though.”

Following Magic Johnson’s gaze, I saw a tall, handsome man walking past.

“I haven’t seen that face before. Is he a new Guild member?”

“Who would hear you and not think you were a Guild member? How many people here do you even know?”

“That’s ridiculous! There’s no way I could fail to remember a handsome man like that!”

“……”

*Why was he so needlessly adamant about that?*

When it came to this sort of thing, his instincts were downright uncanny.

I let out a small sigh before answering.

“I don’t know his name very well either, but he’s definitely new. I think he’s C-rank.”

“I don’t know who the former Guild Master was, but he must be crying tears of blood. Someone that handsome would have plenty of publicity value. He could make a name for himself as a star Hunter, too.”

“The former Guild Master you mentioned is probably crying blood over something else. He was humiliated pretty badly during the press conference.”

“Oh. Then, could it be…?”

“Yes. That guy used to belong to Ares Guild.”

Leaving Ares Guild and transferring to Peace Guild did not simply mean changing jobs.

Magic Johnson seemed to guess the general situation and muttered,

“He’s living proof that an iron fortress is beginning to shake. How many people have transferred from Ares so far?”

“Not many. Around ten.”

“The number isn’t important. It’s proof that a crack has opened.”

I nodded faintly. If the fracture was visible to outsiders, then an even larger crack must have formed on the inside.

*Of course, we can’t rule out the possibility that Go Jun sent him deliberately as a spy.*

That was why he had been accepted only after a thorough verification process, and I heard they planned to deploy him in actual operations little by little.

Even with the System, I couldn’t see straight through people’s hearts. In that regard, Team Leader Choi’s intelligence network would be a tremendous asset.

“But what’s that place? The security looks pretty serious.”

I had been walking in silence, lost in thought, when I suddenly looked up.

In the direction Magic Johnson pointed stood a door made of titanium alloy.

“Oh, that? It’s the training room.”

“The training room? A training room?”

“Yes.”

“My goodness. What kind of training room needs security that intense?”

Magic Johnson gave a short, incredulous laugh.

“Five overlapping spells? I can understand not wanting other people to see your training, but isn’t that excessive considering it’s inside the Guild House?”

“Who knows?”

I kept my answer brief. That training room had been prepared for only a handful of people.

More specifically…

*For those training the Jin Family’s Cultivation Technique.*

It was a secret I had not even told Magic Johnson yet. It was an area permitted only to Team Leader Choi, Butler Kim, Song Song, and Im Kkeokjeong.

“Judging by the security, it doesn’t seem like a space open to every Guild member.”

His sharp observation made me nod.

“That’s exactly right. It’s for the Guild’s founding members, including me.”

“Hmm. So it’s a secret. Hearing you say that makes my spirit of inquiry as a mage awaken.”

“Put it back to sleep.”

“You’re really too much. I can’t even take a quick look?”

I hesitated for a moment, then waved my hand.

“No. There’s someone inside.”

“Who? Is it Choi?”

“No.”

A sudden bitterness welled up inside me as I continued.

“Someone more desperate to train than anyone else.”

“……”

“There is such a person.”

I couldn’t see him with my own eyes at the moment, but a vivid image rose in my mind.

A middle-aged Hunter training again and again, sweat pouring from him like rain.

A man who tried harder than anyone to pretend he was fine, yet willed himself to stand again after his spirit had been brutally crushed.

*Should I start that soon…?*

A thought flashed through my mind. Then, as I listened to Magic Johnson’s next words, it slowly began to take shape.

“Well, it can’t be helped. Give this to Choi when you see him.”

“Give him what?”

“This.”

*Swoosh.*

A small object slipped into my clothes on a faint current of energy.

I confirmed the presence of the chip and looked up.

The Grand Mage’s face had hardened into grim seriousness.

“It’s not only Korea and the United States. Mana levels are skyrocketing all over the world. They’re up seven percent compared to last year. This is the first time a lucky number has felt so ominous.”

# Checkpoint Review — 550–554

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

# Chapters 550–554

## Plot

The Fire Dragon Pavilion begins its first mission: entering Nanman to investigate Dark Heaven’s suspected second rift. The six members secretly depart Henan, planning to reunite at Mount Daebyeol. Mungyeong warns that a successful attack could spread chaos through Yunnan, Guizhou, Guangxi, and Sichuan; Cheongpung remains with him to learn martial arts through observation. Taekyung begins Logout during the journey.

Taekyung returns to the modern world on January 1, 2047—his twenty-eighth birthday—where he reunites with Team Leader Choi, Hayeon, the human-disguised Skeleton King, and Kim Jeonghee at Choi’s mansion. Family quarrels escalate into a fight before Kim Jeonghee subdues everyone and prepares breakfast. Taekyung learns that Lee Jungryong’s national funeral will take place the next day and that public attention has turned to Go Jun after Ares Guild members return from Sichuan.

The Small Cataclysm in Sichuan killed more than four million people. The public credits the Lich with killing Lee Jungryong and Wu Heixing, while Taekyung knows he killed them himself. Go Jun, Lee’s disciple and former Head of Security, is viewed as the likely successor to Ares Guild leadership. Team Leader Choi reveals that he deliberately exposed his identity as Cheon Taemin’s only living blood relative and plans to inherit Ares’s influence before dismantling Lee’s corruption.

## Continuity

- The six-member Fire Dragon Pavilion—Jin Taekyung, Ju Hwaran, Song Ilseom, Sama Pyo, Taishan, and Hyuk Mujin—has secretly departed Henan for Nanman.
- The Journey to Nanman Quest requires Taekyung and the pavilion to enter Nanman. Its reward is a linked quest; failure imposes the Title **Can’t Go to Nanman**.
- Mungyeong believes Nanman is a plausible site for Dark Heaven’s second rift. Dark Heaven can create rifts and grotesque mutants, but the transformation process and the mutants’ ability to absorb human energy remain unresolved.
- Cheongpung accompanies Mungyeong and is learning through observation after Mungyeong ended his direct training. Taekyung’s final task is to incorporate martial principles into his learned techniques.
- Mae Jonghak leads the restored Murim Alliance; Jeok Cheongang heads the Five Kings Hall; Murong Yeonghwi oversees Murong defenses in Liaoning.
- Zhuge Feng’s Demon-Sealing Formation still blocks mana from the exposed Gate, and Jang Taebo is processing the Water God Dragon’s remains.
- The Southern Heaven Demon Empress may be moving toward Nanman, while Song Ho’s dispatch there has received no reply for more than seven days.
- Taekyung is in the modern world on January 1, 2047, staying with Kim Jeonghee and Hayeon at Team Leader Choi’s mansion. Cheon Taemin once lived there, but his current whereabouts and life status are unknown.
- The public regards Lee Jungryong as a Great Cataclysm hero and believes the Lich killed him and Wu Heixing. Taekyung knows the truth.
- Go Jun has returned from Sichuan with Ares Guild members and is publicly considered Ares’s likely successor.
- Team Leader Choi intends to secure Ares Guild’s reputation, influence, and power before removing its corruption. Choi knows Taekyung is concealing his identity, while Taekyung recognizes that Choi has been waiting for Lee’s death to act.
- The Lord of Heaven’s identity, his connection to Taekyung’s original-world force, Dark Heaven’s method for opening Gates, the Jeok Cheongang–Nangong Cheon duel, and Ju Hwaran and Sama Pyo’s broken engagement remain unresolved.

## Translation Decisions

- Render **남만행** as **Journey to Nanman** and **남만을 못 가** as **Can’t Go to Nanman**.
- Preserve **Nanman**, **Nanman Beast Palace**, **Fire Dragon Pavilion**, **Fire Dragon Pavilion Master**, **Murim Alliance**, **Dark Heaven**, **Five Kings Hall**, **Hidden Shadow Pavilion**, **Ares Guild**, **Great Hero**, and **Young Lady Ju**.
- Render **반 시진** as **half a shichen**, **건량** as **dry rations**, **광서** as **Guangxi**, **대별산** as **Mount Daebyeol**, **만리행** as **Ten-Thousand-Li Journey**, and **고잉메리호** as **Going Merry**.
- Render **면구** as **disguise mask**, **역용술** as **disguise technique**, **각주님** as **Pavilion Master**, **로그아웃** as **Logout**, and **동기화** as **Synchronization**.
- Render **소격변** as **Small Cataclysm**, **낭중지추** as **needle in a bag**, and **국장** as **national funeral**.
- Preserve Taekyung’s profanity and dry self-mockery, Hayeon’s chaotic sibling banter, Cheongpung’s innocence, Mungyeong’s dry menace, Choi’s controlled candor, and the Skeleton King’s archaic diction.

## Durable state

{
  "active_continuity": [
    "The Fire Dragon Pavilion's six-member first mission is to enter Nanman through the Journey to Nanman Quest, whose reward is a linked quest and whose failure penalty is the Title Can't Go to Nanman; the party secretly departed Henan.",
    "Taekyung is a Supreme Peak master with Three Flowers Gather at the Crown, advanced Qi Sense, exceptional resistance to monster Fear, public S-rank-level recognition while retaining an A-rank license, and leadership of the Fire Dragon Pavilion's first mission to Nanman.",
    "Mungyeong ended Taekyung's direct training and assigned him the final task of incorporating martial principles into his learned martial arts; Cheongpung accompanies Mungyeong and learns through observation.",
    "Mungyeong considers Nanman a plausible site for Dark Heaven's second rift, while Dark Heaven remains a monster-like threat capable of causing rifts and creating mutants; the mechanism behind Jang Sam's transformation remains unresolved.",
    "The Mount Song Resolution restored the Murim Alliance; Mae Jonghak is Alliance Leader, Jeok Cheongang heads the Five Kings Hall, and Murong Yeonghwi oversees Murong Family defenses in Liaoning.",
    "Zhuge Feng's Demon-Sealing Formation still blocks mana from the exposed Gate, while Jang Taebo processes the Water God Dragon's remains.",
    "The Southern Heaven Demon Empress is believed to be moving toward the suspected next target, while Song Ho's dispatch there has received no reply for more than seven days.",
    "Taekyung is in the modern world on January 1, 2047, staying with Kim Jeonghee and Hayeon at Team Leader Choi's mansion, where Cheon Taemin once lived.",
    "The public believes the Lich killed Lee Jungryong and Wu Heixing; Lee is being honored as a Great Cataclysm hero and is scheduled to receive a national funeral, while Taekyung knows the actual deaths were caused by him.",
    "Go Jun, Lee Jungryong's disciple and former Head of Security, has returned from Sichuan with Ares Guild members and is publicly regarded as a likely successor to Ares leadership.",
    "Team Leader Choi deliberately revealed his connection to Cheon Taemin as the old hero's only living blood relative and intends to acquire the Ares Guild with its influence intact before removing Lee's corruption.",
    "Choi knows that Taekyung keeps secrets about his identity, while Taekyung recognizes that Choi has been waiting for the opportunity created by Lee's death."
  ],
  "continuity_sources": [
    554,
    553
  ],
  "open_questions": [
    "What is the Lord of Heaven's identity, how is he connected to the dangerous force Taekyung associates with his original world, and how can Dark Heaven open Gates?",
    "What will Taekyung's party find in Nanman, and what does the Southern Heaven Demon Empress intend there?",
    "What is the outcome of the duel between Jeok Cheongang and Nangong Cheon, and why did Ju Hwaran and Sama Pyo's political engagement end?",
    "What process created Jang Sam's mutant form, and can Dark Heaven's mutants absorb human energy?",
    "What are Cheon Taemin's current whereabouts and life status, and can Team Leader Choi secure control of Ares Guild?"
  ],
  "safe_through": 554,
  "temporary_decisions": [
    "Render 건량 as dry rations, 광서 as Guangxi, 대별산 as Mount Daebyeol, 만리행 as Ten-Thousand-Li Journey, and 고잉메리호 as Going Merry.",
    "Render 반 시진 as half a shichen and retain Nanman, Nanman Beast Palace, Fire Dragon Pavilion, Great Hero, and Young Lady Ju.",
    "Render 남만행 as Journey to Nanman and 남만을 못 가 as Can't Go to Nanman.",
    "Render 면구 as disguise mask, 역용술 as disguise technique, 각주님 as Pavilion Master, 로그아웃 as Logout, and 동기화 as Synchronization.",
    "Render 소격변 as Small Cataclysm, 낭중지추 as needle in a bag, and 국장 as national funeral."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 550

# Chapter 550

After everyone left, Hyuk Mujin busily disappeared to gather what we needed, leaving me alone. I quietly opened my mouth.

“Quest Window Open.”

*Ding.*

> **System**
>
> **Quest**
>
> **Journey to Nanman**
>
> Murim Alliance Leader Mae Jonghak has given the Fire Dragon Pavilion its first mission.
>
> You must now head to Nanman and proactively respond to any unforeseen circumstances.
>
> It is impossible to know what lies ahead for you and the Fire Dragon Pavilion.
>
> Always remain alert and act with a flexible mindset.
>
> **Grade:** Peak
>
> **Restriction:** Jin Taekyung and Fire Dragon Pavilion members
>
> **Mission:** Enter Nanman (Incomplete)
>
> **Reward:** Linked Quest
>
> ???
>
> **Failure:** Gain the Title **Can't Go to Nanman**
>
> **Fame** and **Trust** drop significantly.

The Journey to Nanman had been created when Mae Jonghak gave me the mission.

As I could tell from the description and mission fields, the System had not offered any particularly useful hints this time.

*There’s no time limit, either.*

That did not mean we had plenty of time. It meant we were entering a situation where we had no idea what might happen even a moment from now.

I let out a quiet sigh and closed the Quest Window.

*If nothing happens, that would be fortunate in its own way…*

But if something did happen, it could quickly spiral out of control. I would have to lead the Fire Dragon Pavilion, bring the situation under control as quickly as possible, and return safely.

I could barely make a living on my own, and now I had become responsible for other people. Just then, the two words *Pavilion Master* suddenly felt much heavier.

“Um…”

A voice abruptly slipped into my ear.

I turned around and saw Cheongpung standing in front of the half-destroyed door, staring blankly at me with a bundle in his arms.

“Benefactor, may I come in?”

“Anyone listening would think you always ask permission before coming in.”

When the door had been intact, he had barged in without even knocking. Seeing him stand there like that in front of the wreckage was almost too ridiculous.

I let out a quiet laugh and waved him inside.

“Just come in. I was planning to go see you anyway, so this works out.”

“I was going to come in whether you gave permission or not.”

The answer, of course, had not come from Cheongpung.

I looked at Mungyeong, who had appeared like a ghost, and muttered awkwardly,

“I was talking to Young Hero Cheongpung.”

“Like I said, I don’t need your permission.”

Mungyeong entered the annex without a care, then glanced at the cups on the table and the disordered chairs.

“Someone has been here. Six people in total, including you and Hyuk. One of them was a woman.”

“How did you know that?”

“You can tell if you look.”

At Mungyeong’s dry answer, Cheongpung added in his innocent tone,

“I saw the others leaving. I thought I should come when no one else was here.”

“…”

“…”

*What the fuck?*

At my deeply suspicious stare, Mungyeong opened his mouth again with an expression that seemed to ask what I intended to do about it.

“If you look, you know.”

“When you said ‘if you look,’ did you actually mean looking with your eyes?”

“You could tell without looking at something like this.”

“Don’t stare off at distant mountains. There are buildings everywhere, so you can’t see any mountains anyway.”

“Instead, I can see your future. If you say one more word, I have a feeling this room will be filled with the smell of blood.”

“…”

*Damn old man. And he still pretends to be a medical apprentice.*

I shuddered at the evil fake physician’s behavior and turned toward Cheongpung.

“So what brings you here?”

“I came to say goodbye.”

“What?”

Cheongpung scratched the back of his head and smiled.

“When you told me to go on ahead outside the Alliance Leader’s Hall earlier, I had a feeling you were about to leave soon. Hehe.”

Even though I had never told him directly, it seemed Cheongpung had guessed to some extent.

After hesitating briefly, I nodded readily.

“That’s right. It’s a mission.”

“Ah! Then where are you going?”

“Nanman.”

“Nan…man?”

Cheongpung’s eyes went wide at my answer. Mungyeong, who seemed to have been thinking about something, muttered quietly,

“If it’s Nanman, then the Nanman Beast Palace?”

“Yes.”

“That strange phenomenon. It must be because of the rift.”

“That’s right. If a second rift occurs, Dark Heaven would have a hard time finding a more suitable place than that.”

“It is certainly possible. Moreover, the distance from the Central Plains is great and the terrain is difficult. If the Nanman Beast Palace were to fall, the chaos would begin in Yunnan and spread like wildfire.”

I agreed with Mungyeong’s assessment.

If Dark Heaven really was plotting something in Nanman and its plan succeeded, the flames of war would not stop in Yunnan Province alone.

*It would spread to neighboring Guizhou and Guangxi—and even Sichuan, which suffered considerable damage in the last battle.*

Guizhou and Guangxi were particularly vulnerable.

The number of sects and martial artists in each province was smaller than in other regions, and their overall strength was weaker as well. The flames would unquestionably spread faster there.

“Going to Nanman in a situation like this. It will be a difficult journey.”

“It would be fortunate if nothing happens. If it does, though… we’ll have to stop it by any means necessary.”

“With only six people?”

“A whole six.”

“…”

“I heard a rumor that among them is a young, handsome Supreme Peak master who was taught by the Fire King and the Slaughter Saint. Have you ever heard of him?”

“I haven’t. Especially not the part about him being handsome.”

“Ah. Right.”

He cut that down with such precision.

Mungyeong had effortlessly blocked my nonsense, then continued while looking at Cheongpung.

“But I have heard another rumor. About a certain man obsessed with dumplings who has latched onto a young medical apprentice and is learning martial arts by watching him.”

“Huh?”

*What did I just hear?*

My thoughts must have shown clearly on my face. Mungyeong nodded when he saw my expression.

“That is probably exactly what you are thinking.”

“Really?”

“It is true.”

“Why would he pass up the almighty Sword Saint and go out of his way to learn from someone with such a foul temper—sorry. That came out wrong.”

At some point, Mungyeong had drawn a small sword from his sleeve. I deliberately avoided his chilling gaze and looked toward Cheongpung instead.

“If you’re being blackmailed, blink twice.”

“You little bastard…”

“Hehe. It’s all true, Benefactor.”

I stared at Cheongpung for a moment, then shrugged.

“I know. I was just making a joke.”

I did not need to hear the answer to know why he had sought out Mungyeong, or what he wanted to gain from him.

*To become stronger. To change himself to fit this world.*

It had been more than a year since we first met.

I had been heading toward an inn when a ragged young man suddenly approached me and asked for a single piece of sweetmeat.

Despite Hyuk Mujin’s protests, I gave him all my sweetmeats. That was how my connection with Cheongpung began.

*We’ve both changed a lot. Me and him.*

The Third Young Master of the Jin Family of Taiyuan, once called the family’s disgrace, had become a Supreme Peak master who shook the Murim.

And the young genius who loved martial arts and delighted in every large and small experience the world offered had, at some point, developed a firm core within himself.

The change could not be seen, but it could be felt.

Only a very small number of people close to Cheongpung, myself included, knew about the transformation that others could not perceive.

*Tap.*

I suddenly reached out and patted Cheongpung on the shoulder. His eyes went round.

“Benefactor?”

“Nothing. Just telling you to hang in there.”

Cheongpung stared at me, then his eyes curved into crescents.

“Yes. You too, Benefactor.”

“Of course I need to try harder. At least Young Hero Cheongpung has something reliable to lean on. I don’t even have a hill to lean against over here.”

Mungyeong had been silently watching our exchange when he suddenly spoke.

“Come to think of it, I don’t see that hill.”

“That hill is staying in Henan. Only the rest of us are leaving.”

“Well, now I’ve seen everything. To think the Fire King would make such a decision.”

“It’s embarrassing to say it, but let’s call it the greater good. We need more hands in the current situation.”

Even as I answered, a hollow feeling remained in one corner of my heart.

Perhaps it was because this was the first time since meeting Jeok Cheongang that I would be moving separately from him.

Even when Jeok Cheongang had been unconscious for a long time, we had always been together.

*But now it’s time for me to stand on my own.*

Jeok Cheongang’s protection had been vast and generous, but I had grown too quickly to remain there forever.

And the turbulent situation would not allow the two of us to keep traveling together.

*Could it be…?*

At one thought that suddenly crossed my mind, I turned slightly and looked out the window.

But every face passing along the main road was unfamiliar and indistinct.

The person I was waiting for never appeared.

*Come on. That’s a little harsh.*

Still, this was the last chance before I left. Couldn’t he at least come see me?

The words lingered at the tip of my tongue before vanishing.

I had said goodbye in advance before leaving the office after receiving the mission, but I could not help feeling disappointed.

Before I was a Hunter or a martial artist, I was still a person.

“…I’ll see them again soon, anyway.”

“What does that mean?”

“It’s nothing. I was just talking to myself.”

Just as I was about to turn my eyes away from the window and leave my disappointment behind, a small baggage cart began rattling toward us in the distance.

It was a sight one could see anywhere, not just in Henan. But the situation changed when a Peak master with his identity concealed beneath a disguise was sitting on the driver’s bench.

*Song Ilseom.*

He had finally arrived.

Ju Hwaran must have finished all the preparations within half a shichen, just as she had boasted, and sent a carriage that could leave Henan discreetly.

I could already sense Hyuk Mujin coming up the stairs from downstairs.

*Is it about time to leave?*

I had grown fairly familiar with this annex. But I seemed to have been saddled with a wandering fate in this life.

I looked around once, then spoke to the two of them.

“I should get going before it gets any later. Thank you for coming all the way here. You too, Young Hero Cheongpung.”

Cheongpung hesitated, then suddenly held out the bundle he had been carrying the entire time.

“This, Benefactor.”

“What is it?”

“Dumplings. I bought them from the best shop in Henan. I wanted to eat them, but I held back while thinking of you, Benefactor.”

Mungyeong quietly added,

“He stuffed down a good five on the way here. That’s what ‘holding back’ amounted to.”

“Ah, aah…”

I had already known from the smell, but I was still touched. Even if he had eaten five of them, that feeling did not change.

“Thanks. I’ll enjoy them. Then I’ll be going.”

I let out a quiet laugh, accepted the bundle, and turned around.

That was when a single strand of Sound Transmission slipped into my ear.

—Do you know? Everyone who has received my teachings up to now has died.

“…!”

—So don’t die a pointless death. If you die in Nanman, all that I’ve put up with until now will have been for nothing.

It was a terrifying way to worry about someone. But the important thing was that, just like the dumplings in my hands, his feelings had come through unmistakably.

I stood there and gave a small nod before immediately setting off.

*Step.*

It was a powerful stride that echoed unusually loudly.
## Chapter artifact 551

# Chapter 551

On the night six young men and women secretly slipped out of Henan, two men clinked their wine cups together in a moonlit pavilion.

*Clink.*

The cups tipped with a clear, spotless chime. After draining his drink in one go, Fire King Jeok Cheongang muttered,

“This wine tastes worse than usual.”

Mae Jonghak, seated across from him, smiled faintly.

“It seems Yeoahong[^1] is not to your taste.”

“I don’t know. My throat’s been scratchy and my tongue bitter for a while now. You haven’t poisoned the wine, have you?”

It was something no one else could have said, even as a joke.

It was only possible because he was Jeok Cheongang—and because the person sitting across from him was Mae Jonghak, who could laugh it off.

“Me, poison Great Hero Jeok? Surely not. Though I may give it a try sometime.”

“Do your research before you use it. I’m confident I can withstand even Formless Ultimate Poison now.”

“Oh. Then I’ll make sure to investigate it thoroughly, even if I have to devote the full strength of the Murim Alliance.”

Jeok Cheongang answered gruffly.

“How frightening. Anyone listening might think you were serious.”

“Oh, that was a joke? And here I thought…”

“...?”

*Surely not.*

Mae Jonghak nodded as though he had only just realized the truth, and a chill ran down Jeok Cheongang’s spine.

*What a lunatic old man.*

His appearance had become younger, but in terms of sanity, he was exactly the same as he had been forty years ago.

Then again, he did not have to look far for proof. Cheongpung alone made it obvious.

*Like father, like son. The master and his Disciple are both...*

At that moment, Jeok Cheongang’s hand shook as he filled his cup.

*Disciple.*

Splash.

The face of a middle-aged man wearing a bitter expression appeared in the wine that had spilled over the brim.

Jeok Cheongang gazed at his own face, familiar yet still strange, then abruptly opened his mouth.

“Nothing will happen, right?”

Mae Jonghak filled his own cup and asked in return,

“Are you worried?”

“Worried about what? Once a man is past twenty, he should follow his own path. He’s old enough to start a family.”

He put on a bold front, but the bitterness remained on Jeok Cheongang’s tongue. He had thought of the face of someone who must be heading south by now.

Mae Jonghak did not miss the emotion that briefly crossed his face.

“He can’t have gone far.”

At those casually spoken words, Jeok Cheongang answered bitterly,

“Even though we already said our goodbyes, what would be the point of seeing him again? It would only make it harder to leave.”

“Now that you mention it, I suppose you’re right.”

“So? What’s your answer?”

“Hm? To what?”

“This old man became Alliance Leader and lost his hearing. You know... what I asked earlier.”

Jeok Cheongang toyed with his cup before continuing carefully.

“Nothing will happen. Right?”

Mae Jonghak thought for a moment before answering.

“It might. Or it might not.”

“…And you call that something to say?”

“Well, it was something I said. It just came out of my mouth.”

“Damn it. This is driving me insane. Anyone could give an answer like that!”

“Oh. I suppose that’s true as well.”

“Then find an appropriate answer as the Murim Alliance Leader. An appropriate answer!”

As Jeok Cheongang flew into a rage, Mae Jonghak smiled faintly.

“He’ll do fine. Just as he always has.”

“Do you mean that?”

“Of course. If I didn’t have faith in him, why would I have entrusted such an important mission to the Fire Dragon Pavilion?”

Jeok Cheongang spoke again, his voice somewhat calmer.

“Did you also prepare a contingency plan, in case something happens?”

“The Hidden Shadow Pavilion has eyes and ears throughout the realm. Nanman is no exception.”

“...!”

“Sending the Fire Dragon Pavilion to Nanman is the fastest and most reliable option. We don’t have enough time to raise an army right now.”

The Murim Alliance was not small by any measure, even compared with its size during the Great Faction War. In fact, it would not be an exaggeration to say it was larger now.

Although Shaolin Temple, the Sichuan Sect, and several other sects had suffered heavy losses, none of the provinces within the Nine Provinces—the territory still held by the orthodox faction—had fallen.

The problem was the time and supplies required to gather troops and send them to Nanman.

And the Fire Dragon Pavilion, led by Jin Taekyung, was one of the few cards the Murim Alliance could confidently play.

“Hmm.”

But no matter what Mae Jonghak said, Jeok Cheongang’s worry did not fade.

As Jeok Cheongang silently glared at his wine cup, Mae Jonghak muttered in a voice as tiny as an ant’s.

“There is one especially reliable source of support.”

“Hm? What did you say?”

“It was nothing. I was just talking to myself.”

“You think you can fool me? I heard you say something clearly with these ears!”

“Calm down and finish your drink. Then I’ll give it some thought.”

Jeok Cheongang stared at Mae Jonghak and grumbled,

“Why do you keep trying to make me drink this tasteless wine?”

“Great Hero Jeok.”

“What?”

As Jeok Cheongang answered curtly, Mae Jonghak fixed him with a deep gaze.

“You’ve already drunk five jars of that tasteless wine.”

“...”

“You’re drinking your sixth now.”

“...”

“Let’s drink for now.”

Jeok Cheongang quietly closed his mouth and raised his cup.

The wine slid down his throat with a fragrant aroma. It was not nearly as bitter as he had claimed. Moonlight softly touched his face as he tilted his head back with the cup.

*I wonder where he is right now.*

*Heartless brat. Couldn’t you have shown your face at least once before leaving?*

The mutter that rose from his heart soon scattered with a breeze that came from somewhere.

* * *

Clip-clop. Clip-clop.

The old horse’s steps were slow, and the straw packed tightly around my entire body was cold and prickly.

Outside the carriage, the voices of hawkers and passersby gradually faded into the distance.

*Did we get out?*

The moment that thought crossed my mind, a whisper slipped into my ear.

“Captain. I need to take a shit.”

“...”

*Hyuk Mujin, you insane bastard. You’re really doing this here?*

We needed to move as little as possible, which meant I could not even subdue him by force. I lowered my voice as much as I could and barked,

“You lunatic. I told you to go before we left.”

“I’m nervous. That’s why. I’m nervous.”

“Then hold it, you son of a bitch.”

“Why are you swearing at me? I can’t even say anything around you.”

“Do I look like I won’t swear right now? What are we going to do about the smell if you shit in here?”

Even a fart under the same blanket would be enough to make me swear. I absolutely refused to let such a catastrophe happen while we were buried together in straw.

“Actually, I thought about it. Wouldn’t it be better if I just went? The smell might make it easier to get through the inspection.”

“Die. Please, just die.”

“I’m sorry. I’ve held it as long as I can, but I don’t think I can anymore. This might be the end for me.”

“Hey, Mujin. Wait. Just wait a second.”

“I’ll accept my punishment later.”

*No! You bastard!*

Terrified, I was about to spring up, camouflage be damned, when—

“We’ve passed through Luoyang’s central avenue. We’re on an empty mountain road now, so you may come out for a moment.”

“Gasp!”

“Phew!”

*Rustle!*

Hyuk Mujin burst through the straw and sprinted toward the bushes. Having escaped death at the edge of a cliff, I repeatedly bowed toward my savior.

“Thank you. I’ll live a good life. Thank you so much.”

“The inspection must have taken a while if Young Hero Hyuk was that desperate. I’m glad we weren’t too late.”

The voice was familiar, but the woman’s smiling face was not.

Under the moonlight pouring through the tall branches overhead, the freckles covering both her cheeks and her dry, rough skin stood out especially clearly.

*No matter how many times I see it, it’s amazing.*

Changing only her features and a few minor details had completely altered her impression.

The woman, Ju Hwaran, noticed me staring and touched her face.

“Ah, I did change a little, didn’t I?”

“Yes. But your eyes are still the same.”

A smile flickered in her beautiful dark-blue eyes.

“That isn’t something a disguise mask can alter. If Captain Song hadn’t helped, it would have been difficult to obtain a mask this good on such short notice.”

Song Ilseom, seated on the driver’s bench, added flatly,

“It was nothing. Just a miscellaneous skill I learned to survive.”

“That’s impressive for a mere trick.”

“It’s probably empty praise, but I’ll accept it for now.”

*That bastard is crooked as hell. I meant it.*

Ju Hwaran’s face had become that of an entirely different person thanks to Song Ilseom’s skill.

I had known that he had lived through all kinds of hardship from the very bottom, but I had not expected him to know how to make disguise masks as well.

*He’s more useful than I thought.*

The various things he had learned while living as a wandering martial artist would undoubtedly help us on the road ahead.

I was privately impressed by Song Ilseom when a sudden thought made my eyes widen.

“Wait. Why don’t I have one?”

If I had a disguise mask, there would be no reason to be transported like luggage with an explosive shit bomb beside me, one that might go off at any moment.

As I protested my unfair treatment, Song Ilseom clicked his tongue.

“Everyone’s features are different, so making the mold for a disguise mask takes several days by itself. How was I supposed to make one for you in such a short time? Wearing an awkward mask would only have the opposite effect. If you feel so wronged, you should have learned a disguise technique.”

Hyuk Mujin emerged from the bushes with an indescribably refreshed expression and joined the conversation.

“What about Young Lady Ju? You said it takes several days.”

“The Young Bureau Head’s mask was...”

Song Ilseom let his voice trail off, then suddenly furrowed his brow.

“What a pointless question. Shut up and bury yourself in the straw again. And don’t stink up my face with your shit.”

“You shit too. Why are you giving me such a hard time…”

Song Ilseom glared at Hyuk Mujin as he grumbled his way back into the straw, then asked me,

“Can I cut him?”

“No.”

I answered firmly, then turned toward Ju Hwaran.

“The others must have gotten out by now, right?”

Ju Hwaran knew perfectly well whom I meant. She gave a small nod.

“Probably. They headed for the West Gate, where inspections are the weakest, so they should have left Luoyang before us.”

I was worried because Taishan was enormous, but Ju Hwaran’s arrangements were not so careless, and we had the Alliance Leader’s Hall and the Hidden Shadow Pavilion behind us. I could afford to relax.

*Rustle.*

Hyuk Mujin poked his head out through the straw.

“Are we going straight to Mount Daebyeol, then?”

“Of course. We’ll change horses once along the way, but nothing will happen before then.”

Ju Hwaran continued without pause.

“If we keep moving without stopping, it will take two shichen. Assuming we undergo a thorough inspection, it could take as long as three. After we meet the other two at Mount Daebyeol...”

“We leave Henan immediately. Correct?”

Ju Hwaran smiled and nodded.

“Just as the Pavilion Master said.”

“...The Pavilion Master?”

“Why? Isn’t that the correct title?”

Technically, it was correct, but it felt awkward, like wearing clothes that did not fit.

I smacked my lips and nodded.

“Well, let’s say that’s fine. Then there won’t be any problems before we reach Mount Daebyeol?”

“Of course. You should be able to sleep soundly and wake up before then.”

Since Henan was the Murim Alliance’s base, it would not be an exaggeration to say there was no chance of an enemy attack.

But I gave a faint laugh with an expression that was neither positive nor negative, only vague.

“What is it?”

“It’s nothing. Nothing at all.”

What was I supposed to call this? After a brief moment of thought, I continued.

“It just feels strange thinking that I’m going to dream for the first time in a long while.”

“A dream?”

“Yes. I dream sometimes. I sleep so deeply that I wouldn’t even know if someone carried me away.”

Ju Hwaran looked puzzled by my cryptic answer, while Song Ilseom furrowed his brow as though wondering what kind of nonsense I was spouting.

Ignoring their reactions, I buried myself deep in the straw piled in the carriage’s storage compartment.

*Two shichen at the earliest to Mount Daebyeol. I have plenty of time.*

From now on, it was time to dream the dream I had put off for a very long time.

*Logout.*

*Ding.*

Along with the clear sound of a bell, my alert consciousness slowly began to sink.

[^1]: Yeoahong is a traditional Chinese rice wine; the name literally means “Daughter’s Red.”
## Chapter artifact 552

# Chapter 552

> **System**
>
> **Synchronization** begins. 10, 9, 8, 7… 1, 0.
>
> **Synchronization** completed successfully. Increased stats have been applied to the body, and use is restricted for certain **Titles**.
>
> **Logout** complete.

Before my vision, which had been dyed black, had even cleared, a cool breeze swept across my entire body.

No—it washed over me, purifying me.

*Synchronization.*

It was one of the processes I had gone through without fail ever since I first began traveling between Murim and reality.

Changes to my stats were reflected immediately, while scars and injuries did not carry over.

Perhaps because sudden changes to one’s physique and appearance would make other people suspicious, there was also a considerate function that allowed those changes to happen gradually and naturally.

*Fwoosh.*

This time was no different.

Strength flowed once more into a body that had already surpassed human limits, and I could feel my muscles becoming more supple.

Even the internal energy refined through my battle with the Water God Dragon and Mungyeong’s teachings was no exception.

“Phew.”

The first thing that caught my eye was a ceiling without a speck of dust on it.

The ceiling, several meters above me, was decorated with an old-fashioned painting.

*Is it because I haven’t seen it in a while? Or am I still not used to it?*

The last time I had seen it was when I had been traveling along a tributary of the Yangtze toward Hubei Province. In other words, I had returned after roughly two months.

Perhaps that was why everything around me felt unfamiliar.

I lay there for a long while, feeling the softness of the blankets and staring only at the ceiling. Then I suddenly opened my mouth.

“What was the title of that painting again?”

A quiet answer came from nearby.

“The official title is the Sistine Chapel ceiling frescoes, but in Korea, it’s better known as *The Creation*—*The Genesis*. It’s a masterpiece created by Michelangelo Buonarroti, a sculptor and painter of the Renaissance.”

“Ah, Michelangelo. Right.”

“Have you heard of him?”

“He’s incredibly famous. Are you looking down on me because I got a Level 7 in my school grades?”

“What do your school grades have to do with it? These days, Mr. Jin Taekyung is far more famous than that painting.”

*Tap.*

Soft leather slippers stepped onto the marble floor.

I tilted my face, half-buried in the pillow, and saw a man crossing the vast—no, almost boundless—space.

*How does that man get more handsome every time I see him?*

He would have to be merely good-looking for me to feel jealous, but once someone passed a certain level, all I could feel was admiration.

Especially when he also possessed an aura that made such an appearance seem completely natural.

I grinned at the man I was seeing for the first time in two months.

“It’s been a while, Team Leader Choi.”

At my greeting, Team Leader Choi—a handsome man dressed in a silk robe—came to an abrupt stop.

“You speak as though you’ve just returned from a distant journey.”

“I had a dream about a pretty distant place. It was a very long dream, too.”

I had spent more than two months in Murim, so what I said was by no means a lie.

In fact, considering everything that had happened during that time, even two months felt short.

“It must not have been a bad dream.”

“No. I had to fight a dragon right from the start, so not really.”

“A Western dragon?”

“Something a little different, but close.”

“A nightmare, then. When that happens, it’s better to wake up quickly.”

*Clink.*

Team Leader Choi set the coffee cup in his hand on the table beside the bed.

“Drink.”

“Is it some incredibly expensive coffee made from rare beans?”

If it was coffee made from cat shit or Hyuk Mujin’s shit like last time, I would have to refuse with all my might.

I glared suspiciously at the cup, but then my eyes widened as a familiar scent reached deep into my nose.

“Huh?”

When I looked at him with an expression that said *surely not*, Team Leader Choi gave a quiet laugh.

“It’s instant coffee. Gold blend. Strong.”

“Damn, our Team Leader Choi knows what’s what.”

“At the very least, I know that Jin Taekyung and bean coffee are a poor combination.”

“Good. Ten points to Gryffindor.”

I gave him a thumbs-up and downed the coffee in one gulp.

*Mm. This is more like it.*

Cheap, but sweet.

After finally experiencing one of the great wonders of modern civilization again, I felt somewhat alive.

“Ah, that’s good. I’m starting to wake up.”

“Are you? You did seem to sleep longer than usual today.”

Like Awakened and Murim martial artists, I possessed a body that had already surpassed human limits. As a result, I slept particularly little.

Even when I slept properly, it never lasted more than two hours a day. And even that could be called nothing more than self-indulgent sleep to satisfy my need for rest.

*Unless I’ve pushed my body too far or my mind is exhausted, there’s no problem.*

When someone like that slept like the dead for several hours, it was only natural for people to become suspicious.

I yawned widely and stretched.

“Are you all right?”

“I get days like this sometimes. Maybe all the fatigue caught up with me at once.”

Groggily, I raised my upper body and reached out.

The smartphone sitting on the table beside the bed flew toward me through *Seizing an Object Through Empty Space* and snapped into my hand like a magnet.

*Maybe it’s because I haven’t seen this in a while, but it feels really strange.*

It was one of the forms of disorientation I experienced every time I returned to reality.

I awkwardly tapped the screen, and the current time appeared.

**7:05 a.m.**

Seven in the morning. I had clearly gone to bed not long after midnight, so I must have slept for roughly seven hours…

“Hm?”

What was this? The date looked strange.

I stared at the smartphone screen. Then a thought flashed through my mind, and my eyes widened.

“Ah.”

I had forgotten because so many things had happened.

What day it was. Why I had returned to my room only after midnight.

And just as that realization struck me like a flash of light, Team Leader Choi’s voice reached my ears.

“I mentioned this last night, but I suppose I should say it once more.”

*Swish.*

He held out his hand, his quiet voice following close behind.

“I look forward to working with you this year as well, Mr. Jin Taekyung.”

January 1, 2047.

That was right. Today was the first day of a new year in the modern world. And…

“Happy birthday.”

“...!”

It was also my twenty-eighth birthday.

*Damn it. Already?*

Just as the number thirty came rushing toward me and my vision went dark, two people burst in from the distance amid a great commotion.

“Hey! Twenty-eight! Mom says you have to eat seaweed soup!”[^1]

“I hereby congratulate you on the day of your birth!”

I take it back. Those weren’t people. They were two monsters.

Jin Hayeon, my old enemy on the family register, whom I was seeing for the first time in a while—and the blond foreigner beside her, the Skeleton King.

I let out a deep sigh at the sight of them both.

* * *

The time difference between Murim and the modern world was enormous.

According to everything I had learned so far, whenever someone crossed into one world, time in the other flowed extremely slowly. Ten days in Murim amounted to roughly one hour in the modern world, so it was only natural to feel disoriented sometimes.

*Especially this time. So much happened.*

Rapid changes had taken place in both Murim and the modern world.

And among those changes was the enormous mansion where I now lived.

*Step. Step.*

White marble gleamed wherever we walked, while old-fashioned paintings and statues filled the halls.

And more than anything else…

“Wow. This place is ridiculously huge.”

It was huge. Big enough to leave me speechless.

Even if I combined every place I had used as lodging while traveling between the two worlds, they would still amount to nothing compared to the scale of this mansion.

But the mansion’s owner did not seem to think so.

“As you said, Mr. Jin Taekyung, it is somewhat large. It also requires quite a bit of upkeep.”

“For a place that takes so much work, I don’t see any other people around. Right, old man?”

Hayeon had been trailing along behind us when she suddenly spoke up.

The title was not directed at Team Leader Choi.

A foreigner with hair the color of melted pure gold and golden eyes that gleamed mysteriously frowned.

“Surely you aren’t addressing me.”

“I am.”

“Hah.”

The foreigner, Magic Johnson’s illusion magic having given the Skeleton King a new life in human form, let out a quiet laugh.

“You seem to have misunderstood something. As far as I know, in this country, the term you just used refers to a male relative of an older generation—or a middle-aged man.”

“Yes.”

“...”

The Skeleton King was silent for a moment before squeezing out his voice.

“What I mean is…”

“You said you’re over thirty. Then you’re an old man to me.”

“I am over thirty, but…”

“Ah, I see. You’re an old man, but you don’t want to be called one, right?”

“...!”

His golden eyes trembled.

The Skeleton King stopped walking and glared at Hayeon before muttering,

“They say relatives resemble one another. You really are siblings.”

Hayeon and I answered at the same time.

“I’m an only child.”

“I’m an only child, old man.”

*Good heavens. There were two wicked humans now.*

The Skeleton King looked back and forth between us with eyes that seemed to say exactly that, then shook his head in resignation.

“All right. All right, so stop it, both of you. And you, insolent human girl. If you ever call me an old man again…”

*Step.*

The Skeleton King could not finish his sentence.

Hayeon had stopped walking and was staring at him with a blank expression.

“What did you say?”

“No, that’s not what I meant. I misspoke.”

The Skeleton King hurriedly tried to recover while watching my reaction, and Team Leader Choi sighed with an expression that said this had finally happened.

“You really did it this time. I’ll take him with me, so please calm your sister down, Mr. Jin Taekyung. Be careful she doesn’t get the wrong idea.”

“...?”

What was he talking about?

I blinked at Team Leader Choi.

“Why?”

“Pardon?”

“No, why? Why do I have to calm her down?”

“Why? Because Miss Hayeon was just subjected to an insulting remark…”

At that moment, before Team Leader Choi could continue, Hayeon suddenly opened her mouth.

“‘Insolent human girl’? Is that something you say to a person, you long-nosed bastard?”

“...Huh?”

“...What?”

Here we go.

I smiled warmly.

*She hasn’t changed a bit.*

Yes. This was Jin Hayeon.

As my capillaries swelled magnificently, I finally felt that I had truly returned to the modern world.

Hayeon abruptly turned toward me.

“Did you hear that? That Yankee bastard just said that.”

I nodded silently.

“I heard.”

“Does he have dirt on you? Did you get caught doing some private webcam show or something? Why else would you be hanging around with a bastard like that? With someone who isn’t even human…”

She was surprisingly accurate.

Impressed, I answered,

“Oh, right. He really isn’t human.”

“He called me an insolent human girl. Is that psycho seriously saying things like that?”

“Well, they are words. Just bad ones.”

“Honestly, if he’d just called me a crazy bitch or some other normal insult, I wouldn’t even complain. What the hell is ‘human girl’ supposed to mean? It feels fucking gross.”

I pulled out my smartphone and whispered,

“Siri, tell me today’s weather.”

—Today’s weather is clear.

“You asshole. Are you in the mood for wordplay right now? My one and only little sister just got called something like that by another person!”

I hastily straightened my clothes and bowed politely.

“Hello. My name is Jin Taekyung, and I’m the only child in my family.”

“You really are a lunatic.”

“That’s a remarkably harsh thing to say upon our first meeting. I’ll sue you for defamation by stating facts.”

Hayeon’s eyes instantly turned cold.

“I’m telling Mom everything.”

“What?”

“I said I’m telling Mom. Everything, from beginning to end.”

“Are you threatening me?”

“Yep.”

“You little…”

*Wham!*

Eyes bulging, I grabbed someone by the collar with all my strength.

Of course, not Hayeon.

I had grabbed the Skeleton King.

“Apologize to my sister right now! You subhuman bastard! You monster!”

“I-I’m sorry! I was wrong! I’ll apologize a hundred times, so please…!”

“Of course she’s insolent! She’s human! She’s a girl! But you can’t put those three facts together like that!”

“Ugh! Grrrgh!”

“Say it properly! Put the right words together!”

“I-Insolent! Person! Girl!”

*Boom.*

I think I heard something explode.

It was the sound of Hayeon’s anger gauge hitting its limit. She grabbed the plaster statue closest to her.

“Die. Just die, both of you!”

*Whoosh! Clang!*

The hallway descended into chaos, beginning with the daily clang.

Hayeon charged at us like a brave Viking warrior, while Team Leader Choi stared at the scene unfolding before him in stunned disbelief.

That was when—

“I told you to come eat, so what is all this commotion…!”

At the end of the hallway, the elevator installed inside the mansion opened, and a familiar face emerged before freezing rigidly.

Dear Lady Kim Jeonghee.

My mother.

“...What are you doing, all of you?”

From the tiny body of a woman who stood no more than 160 centimeters tall, I sensed an aura at least on par with one of the Ten Kings.

[^1]: Seaweed soup is traditionally eaten in Korea on birthdays.
## Chapter artifact 553

# Chapter 553

No matter how much I leveled up or increased my stats, there was one fact that never changed.

To one person, I was still nothing more than an immature little son.

And… my mother, dear Lady Kim Jeonghee, possessed enough attack power to ignore every defense.

“What are you doing, you two?”

One hand was clenched into a tight fist. In the other, she held a ladle.

Sensing that things were getting serious, I hurriedly opened my mouth.

“Lady Kim. I think you’ve forgotten, but this son of yours has a birthday today.”

“So?”

“It means I’m practically thirty. Wouldn’t hitting me in front of other people be a little embarrassing?”

“I’m pushing sixty myself.”

“Ah. Oh…”

I had picked the wrong target.

Deeply acknowledging my mistake, I changed the direction of the conversation.

“Two months—no, not that long ago, I was fighting monsters for my life.”

“Thank goodness you came back safely, son.”

“Thank you, Mother.”

“Then why do you keep fighting with your little sister, who’s eight years younger than you, instead of a monster?”

“Mother. I don’t fight people. Therefore, that thing isn’t my little sister. It’s a monster.”

“Then you’re saying I gave birth to a monster.”

“...!”

“My palm or my ladle—which would you prefer?”

I was cornered. Realizing there was no escape, I closed my eyes and answered quietly.

“My palm.”

“Forearm? Back?”

“I’ll take the back.”

The answer came after careful consideration.

The punishment followed immediately.

“Mom told you—”

*Smack!*

“Not to fight!”

*Smack!*

“Didn’t I?”

*Smack!*

“Eek!”

“Ugh!”

Good heavens. Was this the Flame Divine Palm?

Pain bored into my back, and Hayeon and I screamed.

Even a perfect body known throughout Murim as the Heavenly Martial Physique was useless now.

This was fear and pain engraved directly into the soul.

*I can’t dodge, either.*

If I did, she would apply the crime of insolence and trigger a tenfold event.

In the end, Hayeon and I were released only after receiving Kim Jeonghee’s handprint stamps across our backs.

As Lady Kim turned away, breathing heavily, Team Leader Choi and the Skeleton King watched her with eyes that looked ready to shake out of their sockets.

“Y-Your mother. I was trying to stop them.”

“I am American. Citizen of the United States. Do not touch me. Please.”

Their desperate attempts to survive were almost pitiful.

Of course, Lady Kim gave them a benevolent smile as though nothing had happened.

“Oh-ho-ho. My children were being a little troublesome, weren’t they? I’m sorry. They’re both still immature. I’m making breakfast, so let’s eat together.”

“Th-Thank you.”

“Thank you. Thank you, Jeonghee.”

*What the hell, you son of a bitch?*

I didn’t care about anything else, but the “Thank you, Jeonghee” had earned the Skeleton King a death sentence.

I sent him a silent death threat with my eyes, then headed toward the dining room.

The mansion was enormous, so the distance to the dining room was considerable. But the elevator installed inside the house and the short-range Teleport magic circles made the journey quick.

“...?”

Wait. Now that I thought about it, this was ridiculous.

Why was there a Teleport magic circle inside a mansion?

I stared at Team Leader Choi in disbelief. He answered with a calm expression.

“The mansion is quite large. As I understand it, the circles were installed to reduce travel time.”

“...That’s what Teleport magic circles are normally used for. Of course.”

It was no different from saying, *People eat to fill their stomachs.*

Then again, perhaps all of this really did feel normal to Team Leader Choi.

*He’s a long way from coming from an ordinary family.*

Even a third-generation Korean chaebol heir or the youngest son of a famed swordsmanship family would have to defer to Team Leader Choi.

His maternal grandfather was the immortal hero who had defeated the Demon King Asmodeus in the final battle and saved humanity.

*Cheon Taemin.*

If the birth of some prophet had divided an era into before and after, Cheon Taemin had determined the fate of humanity.

Tens of millions had seen him, and hundreds of millions remembered him.

The vast amount of material proving his existence would remain until countless ages had passed—and until the day humanity met its end.

*And that very Cheon Taemin once lived in this mansion.*

Even Team Leader Choi, his maternal grandson, did not know where he was or whether he was alive. But putting that aside, the thought was moving in its own way.

Though the relentless press had left me imposing on them as a temporary guest, I felt as though I was sharing a space with the immortal hero Cheon Taemin.

*This is incredible.*

I looked around the mansion, where immensely valuable A-rank Magic Gems had been slotted in like batteries to provide a constant supply of energy, and drew in a deep breath.

“Fwoosh.”

Team Leader Choi gave me an uneasy look.

“...What are you doing?”

“Should I say I’m absorbing the energy? Or that I’m sensing the scent of a hero?”

Hayeon rubbed her sore back and muttered,

“He’s just a pervert. He has an olfactory fetish.”

“Would you be quiet, insolent human girl?”

“Really? Mom—mmph!”

“If you don’t want to be murdered tonight, keep your mouth shut.”

I was practically thirty myself. I didn’t want to be beaten in front of other people anymore.

Fortunately, just before Lady Kim, who had sensed something strange, turned around, someone appeared.

“Good morning.”

His smooth, low baritone sounded as though a coffee commercial had started playing automatically.

Even though it was still early in the morning, his slicked-back hair was impeccably styled, and his tailored suit was neat yet dignified.

Butler Kim approached at a measured pace—not too fast, not too slow—and first bowed toward Team Leader Choi.

“Did you sleep comfortably, Young Master?”

Team Leader Choi nodded with practiced ease.

“Yes. I went to bed a little late because there were a few things I had to take care of, but I’m feeling fine.”

“This is regarding the proposal from Mr. Johnson’s side, I presume.”

“There were a few points in the agreement with the Wizard Guild that needed to be adjusted. I’ve organized the matter, so…”

Hayeon, who had been listening to their exchange, muttered,

“Is this a scene from a drama or what?”

“Not a drama. If you want to be precise, probably a web novel.”

A webtoon, maybe. If they turned this kind of fantasy into a TV drama, the production budget would be obliterated.

“Just let it go. You’ll get used to it if you watch long enough.”

“That?”

“...At least try to get used to it.”

In truth, I still found it strange every single time.

Until barely six months ago by modern-world time, I had been an F-rank Hunter who got by on blood sausage gukbap[^1] and cup noodles.

Now the media was praising me as the new hero who would follow in Cheon Taemin’s footsteps, and an S-rank Hunter license made from specially processed top-grade Magic Gems was sitting inside the old leather wallet I still hadn’t gotten around to replacing.

*I should be getting used to this by now, but somehow it isn’t happening.*

Maybe it was because I still had so much left to do.

Just keeping up with the endless incidents erupting in the modern world and Murim while rushing back and forth between the two was already overwhelming.

Perhaps it would be stranger if I could calmly enjoy and grow accustomed to all the wealth and fame that had fallen into my hands.

“It would be best to discuss the details again after breakfast, Young Master.”

“Ah, yes. Let’s do that.”

The short conversation ended just as we reached the dining room with Team Leader Choi and Butler Kim.

No, calling it a dining room seemed inadequate. Banquet hall would have been more fitting.

It was that spacious, neat, and elegant. Robots equipped with advanced AI functions waited at their assigned positions.

And in this space, where everything had been prepared with absolute precision, there was only one thing that hadn’t been prepared.

“Hmm.”

“Just as I thought.”

Everyone except Hayeon and me blinked.

The Skeleton King’s whisper was filled with particularly genuine confusion.

“Wicked human. May I ask you one thing?”

“Go ahead.”

“I was told we were to dine. Why, then, is there nothing whatsoever upon the table?”

The Skeleton King was right.

The enormous table in the center of the banquet hall was completely empty. No dishes, no food—nothing but a perfect blank slate.

I had already guessed the reason, so I quietly nodded.

“That’s how it normally works.”

“What?”

“It’s an absolute rule. Or maybe a species-wide habit. Something along those lines.”

When Mom called us to eat, it meant she was still preparing the meal.

Whether she called once or ten times, saying that the food was ready and we should come out immediately, the result was always the same when we arrived.

Hayeon knew this well. She was already looking for the utensils.

“Sorry, but where are the utensils?”

“Pardon?”

“Utensils. Spoons and chopsticks.”

Team Leader Choi blinked silently, then slowly shifted his gaze toward someone else.

“Butler Kim?”

At that moment, a single stray hair stuck out from Butler Kim’s perfectly arranged pompadour.

“Those functions are all integrated into the robots’ circuits, so they should bring everything automatically… But why aren’t the robots moving?”

Just then, Lady Kim peeked her head out from the kitchen. She had rushed there earlier with a ladle in hand, saying that the soup was boiling.

“Oh, I turned them all off.”

“What?”

“Pardon?”

“I’m sorry to impose on you like this, but I felt as though I’d only be wasting electricity. The children can do it quickly, so please sit down.”

“...”

“...”

There was no way Lady Kim would hear that every robot in the mansion ran on embedded Magic Gems rather than electricity, or that there was no need to save money on the electric bill.

She was a professional housewife who had spent her entire life tightening her belt and raising two children through sheer determination.

As everyone stared at me, speechless, I merely smacked my lips.

“Just accept it. I’ve tried explaining it more than once or twice, but it never gets through.”

Even the living expenses I had sent her over the years had been carefully saved because she couldn’t bear to spend the money.

Thinking of her old days working in a restaurant kitchen, I smiled bitterly, then smacked the Skeleton King on the back of the head.

*Whack!*

“Why me…?”

“What are you doing, asshole? Go help.”

“Wicked human. This is unjust. It is not American either!”

“Then go to America. Though the moment you arrived, they’d realize you were a monster and drag you to the Octagon.”

Team Leader Choi stared at me in bewilderment.

“It’s the Pentagon, Mr. Jin Taekyung…”

“Octagon, Pentagon—what’s the difference? Anyway, you and Butler Kim should go help, too.”

“Pardon?”

“We’re eating together. Everyone should help prepare.”

Team Leader Choi’s eyes wavered.

“Eating… together?”

“You heard me correctly. Hurry up and set out the utensils. I’ll be watching to see whether you do it properly.”

His eyes, which had wavered for a moment, sharpened.

“Watching?”

“Yes.”

“Then what about you, Mr. Jin Taekyung? Are you going to do nothing?”

“It’s my birthday. Even at the Hunter training camp, people were given free time on their birthdays.”

“...”

“What are you waiting for? We need to get ready before the seaweed soup comes out.”

Even though his parents had died and his maternal grandfather, Cheon Taemin, had vanished, and even though Lee Jungryong had thoroughly excluded him afterward, Team Leader Choi was still a young master from a wealthy household.

This must have been something he had never experienced in his life.

I snickered as I watched him walk away with Butler Kim, wearing a dazed expression I had never seen before. Then I sat down and pulled out my smartphone.

*There’s nothing better than the news for figuring out what’s going on.*

*Tap. Tap-tap.*

After a few touches, I accessed one of the large communities restricted to Hunters.

Then I saw an article that had been posted only ten minutes earlier, and my hand suddenly stopped.

[Former Ares Vice Guild Master Lee Jungryong, 68. National funeral to be held tomorrow.]

[Where is the immortal hero Cheon Taemin?]

[Amid global attention, Ares Guild members who remained in Sichuan Province depart the country. Attention from around the world pours onto Hunter Go Jun, former head of security for the late Lee Jungryong…]

“Go Jun.”

Right. That guy was still around.

[^1]: Gukbap is a Korean dish of rice served in hot soup.
## Chapter artifact 554

# Chapter 554

The monster wave in Sichuan Province, dubbed the Small Cataclysm, had devoured an enormous number of things.

Buildings, people, hope…

The casualties numbered more than four million, while property damage amounted to hundreds of trillions.

But as someone once said, people leave their names behind when they die. Even among the countless dead, certain names stood out above the rest.

[Search Efforts Exhausted, but the Hero’s Remains Were Never Found]

[Who Was the Late Lee Jungryong?]

[The Immortal Hero Cheon Taemin Always Had One Person at His Side]

[Wu Heixing and Lee Jungryong: Their Deaths Were the Same, but Their Nobility Was Not]

[Late Lee Jungryong to Receive National Funeral… Waves of Mourning Pour In from Around the World]

Every article occupying the top of the major forum sites contained the same person’s name.

Lee Jungryong.

Another hero of the Great Cataclysm, who had wielded full authority over the Ares Guild in place of the vanished Cheon Taemin.

*No. A hero of the past now, I suppose.*

Lee Jungryong was dead.

The world had been told that his death was the work of the Lich, but I was the one who had actually finished him off.

*Yes. That day.*

I had broken Wu Heixing’s neck while he begged me to spare him, then driven the blade of my spear into Lee Jungryong’s chest and reduced him to ash.

There had been no other choice. Even though I suspected they might stab me in the back, I had gone with them all the way to the Lich’s stronghold because that was the last chance I was willing to give them.

The word *last* left no room for a next time.

*Even if it hadn’t happened then, I would have killed him eventually.*

If Wu Heixing had been like a fish bone stuck in my throat, Lee Jungryong had been a blade digging into it.

He was as strong as a beast of prey and as cunning as a fox.

When I had first encountered him, he had seemed like an insurmountable wall. The reason I had been able to bring him down was that my rate of growth had far surpassed anything he had imagined possible.

*If Lee Jungryong had been a little more daring, the result might have been different…*

But his judgment had been wrong, and this was the result.

Me, looking at articles about his death on my smartphone on the first day of the new year.

Then, suddenly, the last words he had left behind flashed through my mind.

*I… don’t regret it. Never.*

At the time, Lee Jungryong had definitely been smiling.

His entire body was drenched in blood and battered beyond recognition, yet as he smiled brightly, his eyes burned with the obsession and fury he had refused to let go of until the very end.

As though this wasn’t the end.

As though he would become a vengeful spirit after death and continue tormenting me.

Well, now that he was dead, he probably couldn’t torment me as a ghost. But I did agree with him in one respect: this wasn’t the end.

There was still one person left in this world who was practically Lee Jungryong’s other self.

*Go Jun.*

Lee Jungryong’s blindly devoted Head of Security.

No—his Disciple.

I stared intently down at my smartphone, then clicked on an article.

*Tap.*

The screen was instantly filled with an image.

It showed Ares Guild members departing Sichuan Province, along with Go Jun, whose face was stiff with tension.

[ Ares Guild Heads Home for the Funeral of the Late Lee Jungryong ]

[Who Is Go Jun, Head of Security for the Late Vice Guild Master Lee Jungryong?]

I checked the headlines in the bold font and scrolled down. A long stream of comments appeared.

> May the deceased rest in peace.

> Lee Jungryong is dead… One of the great stars has fallen.

> I don’t know whether Jun Dragon was a good person. I heard some pretty suspicious stories about him, too.  
> └ I agree with what you’re saying, but when you get right down to it, those were just unverified rumors. And do you really think you can run a dinosaur of a Guild like Ares without a single drop of dirty water splashing out? Just shut up, press X, and express your joy. Considering what Lee Jungryong did during the Great Cataclysm, that’s the least you can do.

> But who’s Go Jun? They say he was Lee Jungryong’s Head of Security, but this is the first time I’ve seen him.  
> └ Everyone who knows anything knows him. You’re either not a Hunter or you haven’t been around long.  
> └ How did you know? I spent all my time buried in a study room, only awakened by accident, and now I don’t know anything. If you know something, please teach me.  
> └ I don’t know either, honestly. This is my older brother’s account.  
> └ You fucking bastard.  
> └ Waaah. I’m a baby fucking bastard.

> This thread above is a complete shitshow. Hunters with any real standing or experience probably know him, though. That Go Jun guy is famous as Jun Dragon’s right-hand man. He suddenly appeared about ten years ago and caused quite a stir at the time, but after that, Jun Dragon always brought him along to official events.  
> └ You’re right. I just searched iTube, and he was standing behind Lee Jungryong even at last year’s UN General Assembly. I only searched for a moment, and there are already this many results. If someone seriously dug into it, they’d probably find a mountain of information.  
> └ Was he a Disciple Lee Jungryong raised himself?  
> └ There’s definitely a king-possibility. Other communities are already digging into Go Jun’s personal information. Apparently, he came from an orphanage sponsored by Lee Jungryong. He just never took the ranker test. They say his ability is above even the top rankers.  
> └ Then is he the next Vice Guild Master of Ares?  
> └ No one knows what will happen, but wouldn’t he be the most likely candidate? Unless Cheon Taemin shows himself, Go Jun will probably take over without much trouble. Strength plus legitimacy. With that kind of pure bloodline, even Voldemort would shed a tear before leaving.  
> └ Agreed. His face looks exactly like a Death Eater. Probably in Slytherin.  
> └ If you attack him personally, the Ares Guild might attack you.  
> └ Speaking of pure bloodlines, I heard something strange recently.  
> └ ?  
> └ ??  
> └ What is it?  
> └ I’m too scared to say exactly who, but… you know. There’s someone in the ㅍㅎ Guild who’s Cheon Taemin’s—never mind. Sorry, I’m deleting this myself. Please don’t mention it.  
> └ Ah, fuck.  
> └ There are two ways to make someone angry. The first is to start saying something and then stop.  
> └ Ha… Thanks to some bastard, I’m not sleeping tonight.

*Click.*

A sudden noise made me lift my eyes from my smartphone.

Team Leader Choi had set the tableware down beside me and was looking at me with a faint trace of displeasure in his eyes.

“What are you reading so intently?”

“A story about you in the article comments, Team Leader Choi.”

“Pardon?”

“It would be faster to show you directly. Just a moment.”

I turned my eyes back to the smartphone and smacked my lips.

The comment had already been deleted in the brief time it took me to look away.

*He said he was scared and would delete it himself. He really deleted it and ran.*

“What comment was it?”

“It’s already been deleted. But it was definitely about you.”

“If it was about me… was it related to my maternal grandfather?”

I gave a small nod.

I wasn’t the only one who had drawn attention because of the Small Cataclysm in Sichuan Province.

When the entire world had been in an uproar over the monster wave caused by the Lich, the media and public everywhere had been busy mentioning my name.

But at some point, Team Leader Choi’s existence had gradually begun to become known as well.

*A needle in a bag.*[^1]

Team Leader Choi was a needle in a bag.

Not only had he performed brilliantly on the battlefield with abilities that had advanced another step after learning martial arts from me, but he was also handsome enough to knock a celebrity’s jaw sideways. The attention of the so-called “face-obsessed” fans alone was impossible to ignore.

*And he was also Cheon Taemin’s only living blood relative.*

But Lee Jungryong had kept Team Leader Choi’s existence completely secret while he was alive, and Team Leader Choi had done the same.

Until then, the two of them had been a dinosaur and an ant. Even if revealing his identity turned him into a golden ant, he would still be an ant.

And now that Lee Jungryong was dead, the truth they had hidden—whether by choice or circumstance—was slowly rising to the surface.

What made me suspicious was how natural and perfectly timed the process felt.

I gazed steadily at Team Leader Choi.

“This was what you intended, wasn’t it, Team Leader Choi?”

“To be honest, yes. I determined that now was the right time.”

“I’m surprised you answered so honestly. Were you always this kind of person?”

“What else would I have to hide from you, Mr. Jin Taekyung? Of course, even if I’m being this honest, you still have plenty of secrets.”

“...Why do you have to put it that way?”

I felt a small stab of guilt in my chest.

I had already known that Team Leader Choi, the person I had spent the most time with in the modern world since obtaining the System, had always been suspicious of my identity.

I had even heard him say it directly.

But now that he had come straight at me like this, I had nothing to say.

I awkwardly scratched my chin before speaking.

“Putting that aside, may I ask you a few questions?”

“Please do. Seaweed soup will be served soon, so you will have to hurry.”

“It’s just… if you were going to do this, wouldn’t it have been better for me to reveal the truth about Lee Jungryong?”

Lee Jungryong’s and Wu Heixing’s deaths had been announced as the work of the Lich.

The truth about their deaths had been buried, which was why the public had been mourning them with a certain amount of goodwill.

Wu Heixing had always been a rotten bastard, and the atrocities involving his family had been exposed, so people continued cursing him even after his death. But Lee Jungryong was being remembered as a great star who had fallen.

*They were even giving him a national funeral. That said everything.*

But if the truth had been revealed, the situation would have been different.

Even without concrete evidence, it would have been difficult to dismiss my testimony as nonsense. I was a new hero who had already built an impressive reputation.

If that had happened, Lee Jungryong’s honor would have fallen into the dirt, and Team Leader Choi’s plan would have proceeded smoothly as well.

“But you told me at the time not to tell the media about what Lee Jungryong had done.”

Team Leader Choi calmly nodded.

“Yes. I did.”

“Why?”

The answer that came next struck my ears without a moment’s hesitation.

“Because I didn’t want to soil what belonged to me.”

“What?”

“Vice Guild Master Lee Jungryong was certainly a man with an ugly side. He helped my maternal grandfather and made major contributions during the Great Cataclysm, but he gradually became corrupted. He took full control of the Ares Guild and committed all kinds of crimes. The important thing is…”

Team Leader Choi continued in a dry voice.

“The arrows of blame would not be directed at Lee Jungryong alone. They would be directed at the entire Ares Guild.”

“...!”

“The Ares Guild’s influence is immense. Even though my maternal grandfather has been absent for a long time and Lee Jungryong is dead, people still have absolute faith in the Ares Guild’s power.”

*Clink.*

“Mr. Jin Taekyung.”

Team Leader Choi ran his fingers over the perfectly clean tableware, his eyes sinking into deep stillness.

“I don’t want food with filth splashed on it. Even if there are hairs in the food and maggots swarming inside, it must look better than anything else on the surface. It must come into my hands with all of its influence intact.”

I had overlooked it.

The power carried by the name Ares. Its influence.

And Team Leader Choi…

He wanted to take possession of the Ares Guild whole, without a single blemish. He wanted to make its power and influence entirely his own.

Removing the hair Lee Jungryong had planted and picking out the vermin would come afterward.

“I have waited a long time for this moment.”

Team Leader Choi’s eyes glinted coldly as he murmured the words under his breath.

[^1]: A Korean idiom meaning that exceptional talent will eventually reveal itself, even when hidden.

# Checkpoint Review — 300–304

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

# Chapters 300–304

## Plot

Jin Taekyung returns alive from the Black Wizard’s Black Forest after the Peace Guild and rescue teams have presumed him dead. Go Jun, acting on Lee Jungryong’s orders, attacks him despite instructions to avoid conflict, but Taekyung defeats him with one blow. Taekyung warns Lee Jungryong that no one can touch the Peace Guild while he is alive, declares himself the Fire King’s successor, and forces Seoul Branch President Lee Woojoong and more than two hundred Hunters to conceal what they witnessed. He later reveals privately that the defeated Named Monster is still alive: the Skeleton Warlord remains in his Inventory, supplies Skeletons for Guild training, and is mockingly called Warlordmon.

The public celebrates Taekyung’s survival and the defeat of a second Named Monster, while his interview becomes an international sensation. He accepts a limited number of lucrative media and advertising offers, secretly uses his increased wealth to secure his family, and moves them into their remodeled former home. The Peace Guild trains against controlled Skeleton forces, though the level difference now produces few gains.

A week after Hayeon’s college entrance exam, Team Leader Choi shows the Guild footage of a Monster Wave near Nanchong in Sichuan Province. A Named Monster Lich, a powerful undead archmage, has devastated the city with overwhelming forces and claimed the surrounding territory. China requests Taekyung’s help specifically at the behest of Xiao Yang, the General Secretary of China’s Central Committee.

## Continuity

- Taekyung survived the Named Monster raid and has hunted two Named Monsters alone.
- Go Jun suffered catastrophic internal injuries and lost consciousness after Taekyung’s single-blow counterattack.
- Taekyung warned Lee Jungryong that the Peace Guild is untouchable while Taekyung lives; Lee’s response remains unknown.
- Lee Woojoong and over two hundred Association Hunters agreed to deny or suppress their memories of Taekyung’s confrontation.
- The Skeleton Warlord is alive, stored in Taekyung’s Inventory when not deployed, and secretly controlled by him. The government accepted its bones and armor fragments as proof of its defeat.
- Warlordmon provides Skeletons for controlled Peace Guild training, under threat that Guild deaths will bring consequences.
- Taekyung’s family lives in the remodeled former home, surrounded by covert security that his mother and Hayeon do not know about.
- Hayeon completed the college entrance exam and believes she missed a perfect score by one English question.
- A Monster Wave near Nanchong has caused approximately three hundred thousand estimated casualties in its first twenty-four hours.
- The responsible Named Monster is a Lich whose power far exceeds the ordinary Liches known during the Great Cataclysm. It claims territory and threatens anyone who enters.
- China deployed more than one thousand Hunters, and Choi has received a request for Taekyung to join the response.
- The Sichuan catastrophe occurred ten days earlier but has been concealed from ordinary worldwide news; the reason remains unresolved.
- The exact role China wants Taekyung to perform, the Lich’s full strength, and the possible spread of its Monster Wave remain unknown.
- International interview requests remain pending; Taekyung has not accepted them despite their potential benefit to the Peace Guild.

## Translation Decisions

- Use **Warlordmon** for 워로드몬, **Quick Attack** for 전광석화/전광, and **Body Slam** for 몸통박치기.
- Use **college entrance exam** for 수능 and **seventh-tier school grades** for 내신 7등급.
- Use **Monster Wave**, **Lich**, **Sichuan Province**, **Nanchong City**, **Public Security Armed Forces Division**, and **Five-Starred Red Flag**.
- Use **Xiao Yang** for 샤오 양 and retain the General Secretary/chongseogi-to-Jongseok mishearing gag with an explanatory footnote.
- Retain **Fire King** for 화왕 and use **the Blazing Flame** for 열화 in Taekyung’s lineage declaration.
- Render 뚱인데요 as **“This is Patrick”** and retain established explanatory treatment for the forty-ninth-day memorial rite.

## Durable state

{
  "active_continuity": [
    "Jin Taekyung survived the Named Monster raid and publicly returned alive after being presumed dead.",
    "Taekyung killed the Named Monster; Team Leader Choi states that Taekyung has now hunted two Named Monsters alone.",
    "Taekyung's live interview reached 200 million views within twenty-four hours, generating worldwide memes and international interview requests.",
    "Taekyung accepted a limited selection of high-paying advertisements, interviews, and television appearances after receiving extensive domestic and overseas interest.",
    "The Skeleton Warlord remains alive, stored in Taekyung's Inventory when not being used, and is forced to provide troops for controlled Guild training.",
    "The government audit accepted the Warlord's bones and armor fragments as evidence of a defeated Named Monster without discovering Taekyung's control.",
    "Hayeon completed the college entrance exam and believes she missed a perfect score by one English question.",
    "Taekyung's family moved into their remodeled former home.",
    "Taekyung secretly placed covert security around his family by purchasing nearby houses and hiring guards.",
    "The Peace Guild's new members are gaining combat experience against Skeletons under controlled conditions.",
    "A Monster Wave devastated a small city near Nanchong in Sichuan Province, with approximately three hundred thousand estimated casualties during its first twenty-four hours.",
    "The Monster Wave was caused by a Named Monster Lich whose power and fire magic are far beyond ordinary Liches known during the Great Cataclysm.",
    "The Lich claims territory and threatens to kill and rob anyone who enters it.",
    "China's Public Security Armed Forces deployed more than one thousand Hunters against the Monster Wave.",
    "Team Leader Choi received a request from China for Taekyung to participate in the crisis response.",
    "The request came specifically from Xiao Yang, the General Secretary of China's Central Committee."
  ],
  "continuity_sources": [
    304
  ],
  "open_questions": [
    "How will Lee Jungryong respond to Go Jun's defeat and Taekyung's warning?",
    "Will Taekyung accept any international interview offers for the Peace Guild's benefit?",
    "What exact role does China want Taekyung to perform in the Monster Wave response?",
    "Why has the Sichuan catastrophe remained absent from worldwide news ten days after it occurred?",
    "How powerful is the Lich, and how far will its Monster Wave spread?"
  ],
  "safe_through": 304,
  "temporary_decisions": [
    "Use Warlordmon as the comic nickname for the Skeleton Warlord.",
    "Use “This is Patrick” for 뚱인데요 in the live-broadcast gag.",
    "Use Quick Attack for 전광석화 and 전광, and Body Slam for 몸통박치기.",
    "Use “college entrance exam” for 수능.",
    "Use “seventh-tier school grades” for 내신 7등급.",
    "Use Monster Wave for 몬스터 웨이브 and Lich for 리치.",
    "Use Xiao Yang for 샤오 양, with the General Secretary/chongseogi-to-Jongseok wordplay retained."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 300

# Chapter 300

The Black Wizard’s Black Forest. No, now that I thought about it, it would be more accurate to call it the Skeleton Warlord’s Black Forest.

In any case, this gloomy forest was disgustingly huge and complicated. If the Warlord hadn’t been able to look down over the inside of the Gate as if it were the palm of its hand, I would have gotten lost along the way.

- I knew you were wicked, but you’re stupid too. What would you have done without me?

“Right. Which way do we go from here?”

- Turn right one hundred paces ahead.

“……How does this bastard even know the words ‘turn right’?”

One well-captured Warlord beat ten navigation systems.

Swoooosh!

Following the Warlord’s directions, I shot forward at a dazzling speed.

Perhaps it was thanks to the half-jiazi of internal energy I had gained while performing True Qi Guidance on Team Leader Choi, but even as I used my movement technique with all my strength, my internal energy continued surging up like an inexhaustible spring.

*More is always better.*

How long had I been running like that? The sounds of people and their conversations gradually began to draw closer.

My unbelievably enhanced eyesight picked out familiar faces beyond the brush, hundreds of meters away.

*Team Leader Choi and Butler Kim. Uncle Kkeokjeong and Song Song too?*

I could also see the new Guild members I had sent outside about an hour earlier.

No, forget about them. Why were the people who should’ve been busting their asses circulating their qi here?

But the question only lasted a moment before facts I had forgotten flashed through my mind.

*Oh. I forgot.*

I had already expected the situation outside to become something of a disaster.

That was why I had planned to deal with the Warlord and the Skeleton army before immediately leaving, but the unexpected discovery of an EXP factory had gotten me so excited that I had made the mistake of leaving the scene.

*Things must have gone completely insane outside by now.*

Of course, considering how chaotic things had supposedly become, they had taken quite a while to arrive. At least an hour had passed since I sent the new Guild members out of the Gate.

*I can explain the situation. It’ll be fine.*

That was when I was just about to leave the brush and approach them.

“The skull emblem! Y-yes, this is the armor the Named Monster was wearing!”

“We found a dagger too! This isn’t equipment used by Skeletons!”

“It’s the dagger Senior Jin Taekyung used!”

At the successive shouts, Im Kkeokjeong suddenly burst into tears.

“Hk, nghh!”

“……?”

- ……?

“Taekyung. Taekyung… Nghh!”

No way. Was this what I thought it was?

As I stood there with my mouth hanging open, the Warlord rolled its green, glowing eyes toward me.

- It seems those humans think you’re dead.

“Uh, yeah. There seems to be a huge misunderstanding.”

- Then shouldn’t you stop hiding like a rat and go out there?

But the situation was already spiraling out of control.

Song Song and Butler Kim suddenly began shedding tears, and even the Guild members lowered their heads with red-rimmed eyes.

The path was weighed down by grief and mourning.

“…….”

No. I couldn’t possibly go out there in this atmosphere.

What would happen if I showed up now and said, *Surprise! You thought I was dead, but I’m alive!*

*What would happen? I’d get cursed out.*

Just thinking about cleaning up the aftermath made me break into a cold sweat. Even so, I had to clear up the misunderstanding before the atmosphere got any worse.

Of course, there was someone I needed to deal with first.

“You stay in there for a while.”

- Hm? What does that mean?

“I don’t know if it’ll work… People might be startled, so just get inside for now.”

- Inside where?

Ignoring the Warlord’s puzzled question, I immediately muttered the command in my mind.

*Open Inventory. Store.*

Pop.

At the same time as the command, the Warlord’s skull vanished from my hand.

The Inventory was a space that living creatures could not enter. However, since the Skeleton Warlord was an undead monster that had lost its vitality long ago, it seemed to work.

“Oh, it worked.”

- Gah! Where is this?

“What the hell? You can talk from inside?”

Was it because the Inventory and I were connected?

I had never put anything alive inside before, so this was a first.

As I marveled at the situation, the Warlord’s shrill voice rang through my head.

- What have you done to me? Release me this instant!

“Yeah. I can’t release you.”

- Do you think you’ll get away with this?

“I think I’ll live a long and healthy life, stay safe and sound, and never grow old or die.”

- It’s so suffocating! I’m going insane in here!

“Why would you suffocate? You don’t breathe in the first place.”

- You insolent wretch!

“Ah, you’re loud. Should I just make you disappear?”

The Warlord answered in a suddenly much brighter voice.

- This is a more comfortable space than I expected.

“Good. Rest comfortably. And even if you do come out, don’t say a word in front of the people.”

- Understood. But…

“But what?”

- For a wicked human, you seem to have quite a few friends. A considerable number of intruders have entered again.

A moment later, I narrowed my eyes when I spotted hundreds of Hunters approaching like a cloud.

The Warlord was only half right. There certainly were a considerable number of people, but they weren’t friends.

Especially the bastard charging at the front like a victorious general.

*Go Jun?*

Why the hell had he come here?

And the middle-aged man clinging to him like his soulmate was a face I had seen several times on television and in the newspapers.

*The Seoul Branch President came too?*

The Ares Guild and the Seoul Branch had both shown up.

This had become much bigger than I expected. And that made it even harder for me to go out.

I was anxiously waiting for the right moment when I heard the conversation between the two men and let out a hollow laugh.

“Would you look at these bastards.”

The conversation was fragmented, but it was enough to understand the situation.

Lee Jungryong had sent Go Jun to eliminate me as a potential danger, while the Association President wanted to seize the powerful connection that was Lee Jungryong.

Well, this was…

“Beautiful. Absolutely beautiful.”

The man trying to delay a rescue operation just to properly kill one person, and the man eagerly accepting that proposal—both of them were pieces of shit in the same cesspool.

Even if it dirtied my hands, I had to clean up this shit myself. If pieces of shit like these were scattered along the road, it would be hard to walk around without a care in the world.

“It’s too late to regret it. The dead don’t come back.”

I could see Go Jun snickering as he taunted Team Leader Choi. Without hesitation, I pushed through the brush and walked out.

“What the fuck are you talking about, you goddamn bastard?”

At least one of them needed to be taught a lesson.

* * *

“……!”

Shock, disbelief, bewilderment.

With every step I took, gazes filled with different emotions flew toward me and struck my face.

As I passed, I patted the shoulders of Team Leader Choi and the Guild members, who had frozen at my appearance.

Greetings could wait. I needed to clean up that lump of shit before it began to stink even worse.

Step. Step. Tap.

Two people stood where my final step came to a stop.

“You were… alive?”

“J-Jin Taekyung, Hunter?”

I stared at the two pairs of trembling eyes—Go Jun and the Seoul Branch President—then turned toward Go Jun.

“Why? Disappointed that I’m alive?”

“……There’s no way.”

“That’s strange. It sounds like your answer came half a beat late.”

“You’re imagining things.”

Go Jun continued in a calmer voice.

“We were all searching for you. Where were you?”

“Oh, I went nearby to take a piss. But when I got back, you’d practically finished the funeral and even held the forty-ninth-day memorial rite.”[^1]

“Urinate?”

“I drank a lot of water before entering the Gate.”

“You take a long time to relieve yourself.”

“It’s a symbol of virility. If you’re interested, I can show you how to make a rainbow with my piss. It’s really pretty.”

“……You seem perfectly fine, judging by the nonsense you’re spouting.”

“I’m always perfectly fine. But…”

I continued with a faint smile.

“Are you sick? The way nothing but dogshit keeps pouring out of your mouth makes me think you might have rabies.”

“……!”

“Listening to you was pretty entertaining. You were making a whole fucking production out of whether to give me a commendation plaque.”

Go Jun wasn’t the only one whose face had stiffened.

The Seoul Branch President, who had been listening to our conversation while silently swallowing, interrupted with a flushed face.

“Young man, your mouth is filthy.”

“Yes, my mouth is a little filthy. But who are you?”

At my curt reply, the Association President frowned.

“You don’t know me?”

“Are you the president?”

“I am not.”

“Then you should introduce yourself. How else would I know?”

“Good heavens. In all my years…”

Clicking his tongue, the Association President thrust out his chest with an arrogant expression full of authority.

His fat chest bulged beneath the suit jacket he had gone to the trouble of wearing into the Gate.

“I’m Lee Woojoong.”

“Oh, Lee Woojoong.”

I scratched my chin with an innocent expression.

“Then do you happen to know Kim Jeonghee?”

“Kim Jeonghee? You mean that senior figure in the Association?”

“No. She’s my mother.”

“……Hm?”

“Mrs. Kim Jeonghee. My mother.”

The Association President was briefly rendered speechless before asking in an incredulous tone,

“So what? What do you want me to do about it?”

“That’s what I wanted to ask you. It’s basic to say who you are, where you’re from, your position, and your name. If you cut off everything before and after and just say ‘Lee Woojoong,’ what am I supposed to do with that? You might as well have said, “Gynecomastia.””

“What did you say?”

“So who are you, exactly, Lee Woojoong?”

“I’m Lee Woojoong! The Seoul Branch President of the Hunters Association!”

“Ah. Nice to meet you.”

“Y-you…!”

“Two twos make four. Two threes make six. Two nines make—fucking eighteen.”

“What an outrageously rude man!”

I snickered as the Association President’s face turned bright red, as if he were about to explode.

I knew perfectly well that the Seoul Branch President was one of the most important posts of all. Even so, I made no effort to hide my contempt because he was a human being who deserved to be despised.

*A man who’s supposed to be responsible for Hunters’ safety and rights pulled something like this.*

If anyone other than me had remained in this Gate, he would never have escaped death.

The Association President had known that, yet he had delayed for an entire hour. All so he could curry favor with the Ares Guild—or rather, Lee Jungryong.

“Jin Taekyung, what the hell kind of person are you?”

I stared coldly at the Association President as he shouted and pointed a finger at me.

“What kind of person am I? I’m a person who killed two Named Monsters by myself. While waiting for a rescue team for an entire hour.”

“Th-that…”

The Association President flinched at my aura and took a step backward.

But the distance between us didn’t widen. I advanced as far as he retreated.

Step.

One step.

“President Lee Woojoong.”

“B-back off.”

Step.

Another step.

“If you’re the Association President, work for the Hunters Association. Don’t work for a Guild.”

“I-I don’t know what you’re talking about.”

“Would you like me to make it clear? In front of everyone?”

Step. Tap.

As I took the third and final step, a strong hand seized my shoulder.

“That’s far enough.”

I grinned at Go Jun, who had stepped in front of me.

“Get your hand off me. You smell like shit.”

“Do you make a hobby of escalating things?”

“Why? Are you scared?”

“Scared?”

Go Jun whispered into my ear with a dry laugh.

“You’re the ones who should be afraid. Everyone behind me is either an Ares Guild Hunter or an Association Hunter. If you want to get out of here alive, you’d better watch your mouth.”

“Oh, so if things go badly, you’re planning to bury every single person here and leave? That’s a lot of bodies. Can you handle it?”

“That’s why I’m holding back. Consider yourself lucky.”

“That sounds scary. But are you all right after I beat the shit out of you last time? Did you drink a good potion?”

Go Jun’s gaze turned cold.

“What a childish taunt.”

“Look in a mirror. Judging by your expression, it worked pretty damn well.”

“I’m telling you one last time. Back off.”

“For the final final time, take your hand off me.”

Huff.

Hot breath carrying a foul odor poured from his mouth.

Go Jun glared at me with sunken eyes, then took several steps back and muttered,

“If it hadn’t been for my Master’s special order… you would have died here.”

“Your Master? Oh, Jungryong?”

“……!”

“How’s Jungryong doing? Isn’t it about time you found him a place in a retirement community?”

That was the decisive blow.

Go Jun trembled from head to toe as if he had been shocked by electricity. His eyes opened wide, and a flash of light different from the one I had seen when we fought at the hospital surged through them.

“If you think things will go the same way as last time… I’ll make you regret it.”

“Regret?”

I smiled brightly and spread both arms wide.

“You’ve got a long tongue. Stop making a spectacle of yourself and get over here.”

Whoooosh!

[^1]: *49jae* is a Korean Buddhist memorial observance culminating on the forty-ninth day after a person’s death.
## Chapter artifact 301

# Chapter 301

Go Jun was filled with confidence.

*I can do this.*

It had been more than thirty years ago. He had lost his parents in the Great Cataclysm and become an orphan when he met Lee Jungryong.

*“I’ve had my eye on you for a while. Would you like to follow me?”*

*“Me?”*

*“Yes. You have outstanding talent.”*

Only then did he understand.

How an ordinary orphan like him had been able to grow up receiving the best education in the best possible environment. Who the anonymous benefactor he had never once seen was.

Lee Jungryong was no Daddy Long-Legs from a fairy tale, but that was reason enough for Go Jun to follow him.

*“Yes, sir.”*

*“From now on, call me Master.”*

That was how everything began.

He had to learn movements he had never seen before and how to breathe properly alongside other children, but Go Jun loved every part of it.

His once-tender hands blistered, then developed calluses. They burst, healed, and hardened… Go Jun’s life was the same.

He grew as tough as his pain had been, and eventually came to stand at Lee Jungryong’s right hand.

*“Starting today, you’re the Head of Security.”*

*“Please tell me what I should and shouldn’t do.”*

*“Follow my orders, and never go against them. That’s all.”*

His Master Lee Jungryong’s answer was burned deeply into Go Jun’s mind.

He lived according to the milestones his Master had set for him. Sometimes in the shadows, sometimes in the light…

He handled countless tasks for Lee Jungryong and never left an opening.

Unlike the Hunters who exaggerated their abilities and lived flashy lives, he quietly hid his true strength and completed every task Lee Jungryong assigned him.

Even within Ares Guild, everyone could only guess at his abilities. Lee Jungryong was the only person who knew Go Jun’s true strength.

*“Doesn’t it frustrate you?”*

*“What do you mean?”*

*“Always staying by my side.”*

*“I’ve never thought about it.”*

*“With your abilities, you could make a name for yourself anywhere right now.”*

*“I have no interest in that. I’ll always remain by your side, Master.”*

*“Ha-ha. You seem even more dependable than usual today.”*

He had meant every word. Every member of the security team had received Lee Jungryong’s teachings, but no Disciple worshipped and revered him as blindly as Go Jun did.

Outstanding ability and unwavering loyalty.

Ironically, those two qualities were what led Go Jun to defy Lee Jungryong’s orders.

“If it hadn’t been for Master’s special order… you would have died here.”

“Your Master? Oh, Jungryong?”

“……!”

“How’s Jungryong doing? Isn’t it about time he started looking for a place in a retirement community?”

It was an insult Go Jun could not endure. To him, Lee Jungryong was his parent, his Master, and practically a god.

It was only natural for the eyes of a fanatic whose god had been insulted to turn savage.

*You piece of shit… I’ll tear you apart.*

The moment his Master’s order to avoid a clash with the Peace Guild was wiped clean from his mind, aura had already gathered around his fist.

“If you think things will go the same way as last time… I’ll make you regret it.”

Go Jun already knew Jin Taekyung’s abilities from their brief clash at the hospital a week ago.

But that confrontation had been carried out under his Master’s orders. Go Jun had shown less than half of his actual strength.

Now Jin Taekyung would pay dearly for taking him lightly.

*I’ll use everything I have and finish this in one blow.*

He had no concern for the aftermath. He only wanted to punish, brutally, the man who had insulted his Master.

And Go Jun was confident in his abilities.

“Die!”

Whoooosh!

With a terrifying crack of air, his fist shot forward at the speed of a ray of light.

The distance between him and Jin Taekyung was only three steps.

The man standing there with a wide smile and both arms spread open was completely defenseless.

In the slowed-down world, Go Jun’s fist drove forward with enough force to pierce Taekyung’s chest.

Taekyung did not move an inch.

*It’s over, brat.*

That was the exact moment a triumphant smile appeared at the corner of Go Jun’s mouth.

Kkwaaang!

A thunderous boom split the sky.

But Go Jun did not hear it. He felt the overwhelming rebound force traveling from the end of his fist, along with lava-like heat sweeping through his insides.

*What is this…?*

His vision suddenly flooded white, and agony engulfed him as if a red-hot knife were tearing through his stomach.

Something spilled from his mouth, which had fallen open without his realizing it.

“Hurk!”

Splaash.

Bent over like a shrimp, Go Jun vomited up his insides and stared with bulging eyes.

Blood. It was nothing but blood.

Between the dark-red pool soaking the ground, pale objects of unknown identity were scattered.

It did not take long for him to realize that they were pieces of his internal organs.

“W-what the hell is…”

As Go Jun stared blankly at the pool of his own blood, someone’s foot suddenly entered his field of vision.

“Didn’t you say you’d make me regret it?”

“……!”

“That’s strange. It doesn’t look like anything special to me.”

He did not need to lift his head to confirm.

He knew whose foot was standing in his blood. He knew whose voice was both ice-cold and burning with heat.

*How… how did I lose in a single blow…?*

One clash.

It was a pillar of fire that would reduce to ashes the painstakingly built tower Go Jun had spent the last thirty years constructing.

*Is this even possible?*

Go Jun’s entire body trembled.

Pain?

No.

What dominated him now was fear—the same emotion he had felt from only one person in his entire life: his Master, Lee Jungryong.

“Raise your head.”

That very fear seizes Go Jun by the hair and slowly raises his head.

A foot submerged in a pool of blood. A leg straight and hard as steel. A torso made of flexible, powerful muscles like those of a wild beast.

And then…

There were eyes.

In the black forest, shrouded in faint darkness on every side, two eyes filled with burning flames stared down at Go Jun.

“Give this message to your Master.”

Hot breath brushed against his ear. A voice as quiet as breathing continued, audible only to him.

“As long as I’m here, no one can lay a hand on the Peace Guild.”

“……!”

Go Jun’s eyelids trembled. A hoarse voice leaked between his bloodstained lips.

“What… what are you?”

“Me?”

The answer that came a moment later did not ring in his ears. It echoed inside his head.

—A descendant of the Fire King. I am the successor to the Blazing Flame.

The voice sounded like an auditory hallucination.

Go Jun did not even realize it was Sound Transmission, let alone understand what the words meant.

There was only one word in his mind.

*Monster…*

The last thing Go Jun saw was the face of the young man, Jin Taekyung, smiling playfully.

Then his body collapsed like a rotten old tree.

* * *

Slump. Thud!

A suffocating silence descended.

No one dared to speak. No one could even move. Hundreds of trembling pairs of eyes swept over my entire body.

I stared absently at the unconscious Go Jun, then gave a brief assessment.

“So why the fuck did you have to act up? You’re nothing special, you bastard.”

“……!”

“……!”

The air froze in an instant.

When I tore my gaze away from Go Jun and turned my head, gasps burst out from every direction.

One person’s reaction was especially violent.

“President.”

“Eek!”

Lee Woojoong, the Seoul Branch President, flinched and hurriedly looked away before answering.

“D-did you call me?”

“Why are you suddenly speaking formally? You were talking so casually until a minute ago.”

The President’s face turned deathly pale as he stammered.

“M-me? I was?”

“Don’t you remember?”

“Lately, lately my memory hasn’t been very good, so I keep forgetting things…”

“Oh, is that so? Then you’ve already forgotten everything that happened between us today?”

“……!”

“Judging by your expression, your memory seems pretty good.”

If he could not understand a hint that obvious, he never would have reached a high-ranking position like this.

The President hurriedly shook his head at my question.

“No. How could I? I-I’ll make sure everyone keeps quiet.”

“Keep quiet?”

“Gah, that’s not what I meant.”

“The people who came with you must have poor memories too, huh? Isn’t that right?”

“Y-yes. Yes, exactly. Those guys all suffer from short-term amnesia. Don’t you?”

More than two hundred Association Hunters had followed their direct superior into the Gate, and they nodded frantically.

“That’s right.”

“Of course. I don’t even remember my own name.”

“Wait, where is this? Who am I?”

Who the hell said that last one?

I barely managed to suppress my urge to check his face.

“Well, that worked out nicely.”

Following my broad smile, the President and the other Hunters forced smiles onto their faces.

Well, there were far too many eyes watching us. I hadn’t expected this much to silence everyone completely.

Now, the next thing…

“Hey, who’s in charge over there?”

“I am.”

A sharp-eyed middle-aged man stepped forward. He was an A-rank Hunter and a team leader in Ares Guild.

He still looked unable to believe what he was seeing as he glanced back and forth between me and the fallen Go Jun. Then he bit his lip.

“I don’t know what circumstances entangled you with Team Leader Seok… but you’ve made a serious mistake.”

Judging by his words, he clearly did not know the exact circumstances behind the incident.

I grinned and answered him.

“Life’s full of this and that. What can you do?”

“Aren’t you worried about how the Vice Guild Master will react when he hears about this?”

“Worried? No. But I am looking forward to it. Be sure to report it to Lee Jungryong.”

At my answer, the middle-aged man and every Ares Guild member standing behind him flinched.

I did not know whether it was because of the way I had addressed Lee Jungryong or because of my shameless attitude.

I was more curious about Lee Jungryong’s reaction when he heard the report than about what they thought.

*Looks like Mr. Jungryong is in for one hell of a headache.*

In this little play, Lee Jungryong’s role was the cleanup man.

Since he would not want any noise leaking out, he would have to cover people’s eyes and ears and shut down every speaker carrying the sound outside.

*And here I thought it hadn’t even been two weeks since that incident. He’s already showing his teeth again… Impressive. Very.*

It sent a chill down my spine to think about Lee Jungryong’s decision to bare his teeth the instant an opportunity appeared, even though it had barely been any time since we finalized our deal.

*What if I had really died here?*

That would have ended this fight for good. Without me, the Peace Guild would have had no chance against Ares, an unbeatable giant.

At the same time, I realized something once again.

*If I let my guard down in this fight, even for a moment, it’s over.*

This war could only end for good; there would be no truce. The enemy would keep baring its teeth whenever it saw an opening.

“Hoo.”

In any case, the bare minimum had been taken care of.

Or so I thought.

“……”

“……”

“……”

“……”

Four pairs of terrifying eyes stared at me.

Dozens more demanded an explanation.

*Ah. I forgot about our Guild.*

I had forgotten something important. But where was I supposed to begin, and where was I supposed to stop?

After thinking for a moment, I opened my mouth.

“I went to take a piss.”

“……”

Silence flowed through the area.

Song Song suddenly spoke. Her voice was gentler than any I had ever heard from her before.

“Taekyung.”

“Yeah?”

“Can I kill you?”

“…I’ll explain outside.”

Right. Let’s get out of here.
## Chapter artifact 302

# Chapter 302

More than thirty minutes had passed since the rescue team was deployed.

Hunters from other Guilds who had been assigned to guard the perimeter in case of an unforeseen incident had already drawn their weapons, while network personnel were reporting on the situation with microphones and cameras.

The commotion was not limited to the ground.

Dozens of combat helicopters flew through the sky, and countless drones equipped with cameras hovered overhead, broadcasting the entire scene across Korea.

“What are you watching so intently?”

“A live news broadcast.”

“News? You barely watch variety shows. What got into you? Did something happen?”

“Do you carry your phone around as a decoration? It’s been over two hours since the Named Monster caused all this chaos, you idiot. Try looking at the internet once in a while.”

“Holy shit, there’s a headline saying, ‘Named Monster Appears… Jin Taekyung Presumed Dead.’ Is this real?”

“I don’t know. I can’t hear anything, so don’t talk to me.”

At home, at school, at work, and even on crowded public transportation during rush hour, everyone was staring at a television or the phone in their hand.

The HunterTV iTube channel’s live stream had surpassed one hundred thousand concurrent viewers long ago.



Did Lord Fuck really die?

Don’t say shit like that.

That’s not saying shit. Honestly, at this point, his chances of survival are slim. The golden window for a rescue operation is fifteen minutes, and there hasn’t been a word for over an hour. On top of that, they’re dealing with a Named Monster.

Still, the rescue force looked no joke. I’ve never seen so many A-rank Hunters gathered in one place.

That’s what I’m saying—what are they rescuing? You don’t rescue a corpse. You recover it. No wonder the Peace Guild Team Leader was screaming that they were fucking bastards earlier. Safety matters, sure, but they should save the person first.

Fact check: Lord Fuck is already considered almost certainly dead. The Hunters deployed there appear to be focusing on raiding the Named Monster rather than rescuing him. Since there has been no word even from the rescue team, it is also possible that the battle has already begun—or that they have been wiped out.

What? Wiped out? What happens if they get wiped out too?

What do you mean, what happens? The Named Monster starts a food tour. It’ll probably eat the people waiting outside as appetizers. An emergency evacuation order has already been issued for the surrounding area.

Fuck, I’ve got such a thick layer of fat I wouldn’t even taste good. Can’t we just cook it some ramen?;

Are you another fucking idiot? You think it’ll go back into the Gate just because it’s full?

Guys, for a Named Monster like that, what’s the maximum?

What does “what’s the maximum” even mean?

How many people can it take at most?

Another idiot has joined the chat.

Do the guys cracking jokes right now have nothing but udon noodles for brains? Have you thought about what will happen if the next time a Gate opens, it’s monsters that come out instead of people?



As one commenter had bluntly pointed out, the situation was more serious than expected.

The Hunters deployed there possessed overwhelming strength, but their opponent was a Named Monster.

If it possessed power beyond anything they could imagine, an enormous catastrophe would occur.

There had been precedents of a single powerful Named Monster causing tens of thousands of casualties and destroying an entire city.

As time passed, tension began to seep into the chat window as well.



There really hasn’t been any news. Someone should have come out by now.

Isn’t a rescue operation normally like this?

Nope. Communication devices don’t work inside Gates, so normally someone has to be sent out every thirty minutes to let everyone know they’re still alive.

Then why hasn’t anyone come out? They said the battle site was just a stone’s throw from the Gate.

Are they fighting the Named Monster? Shouldn’t they deploy Central Plains forces?



Just then, the broadcast camera caught the Gate’s magic field rippling like a wave.

At the same time, the chat window, which had been filled with heated arguments, began scrolling upward at a maddening speed.



They’re coming out!!!

The magic field just moved—yessssss!

Go go go go go go go!

Please let it be people.

I want to see Lord Fuck. I hope he’s alive.



On the internet, on television, and at the scene itself, countless people—roughly half the population of Korea—were watching the changes taking place at the Gate.

And then, in the next moment—

Whoooosh!

The swirling magic field of the Gate began vomiting out several objects.

Human arms and legs. Clad in gleaming armor and armed with weapons, they marched out in neat ranks.

They were not monsters, but the Hunters who had entered earlier.

“Woooooah!”

The explosive cheer from the crowd startled the middle-aged man in a suit at the head of the group.

But he soon broke into a smile, his double chin folding as he waved his hand.

“Yes. I’ve returned, everyone! We’re all safe!”



I’ve been wondering since earlier—who’s that guy?

Lee Woojoong. Read “Seoul Branch President” as “idiot.” Everyone already knows he’s incompetent.

Why is that asshole Lee Woojoong grandstanding?

The guy who went in for a rescue operation is the only one wearing a suit, lmao.

Lee Woojoong, man boobs, whatever you are—quit blocking the screen and move. Seriously.



The chat window was being flooded with criticism.

The cameras mounted on the drones avoided Lee Woojoong and filmed the Hunters emerging behind him.

First came the government-affiliated Hunters from the Association, which had led the operation. Then the cameras captured the Ares Guild members walking out with grim expressions.

They were carrying a stretcher covered with a large sheet. As it swayed with each step, one blood-soaked hand slipped out from beneath the cloth.

Pop-pop-pop! Click, click!

Camera flashes burst from every direction. A wave of mourning spread among the people watching the scene.



Ah… I didn’t want it to turn out like this.

Jin Taekyung really died in the end.

May he rest in peace.

May he rest in peace. I hope he finds peace in heaven.



It was at that moment, with everyone swept up in grief, that a voice rang out.

“That startled me. Why are there so many of these?”

“……!”

The news anchor who had been solemnly reporting Jin Taekyung’s death, the photographer who had been pressing his camera shutter without pause, and the chat window covered with messages wishing the deceased peace—all of them stopped what they were doing and stared at one person with their eyes wide open.

“Wow, look at all these cameras. By the way, is it really okay to broadcast something like this live?”

The young man looked around as if he found everything fascinating.

There was no one who did not know the name of the man wearing simple leather armor with a spear strapped to his back.



…Isn’t that Jin Taekyung?

Huh?

?????

Why is hyung there…?

Am I the only one seeing a ghost?



As everyone floundered in a bottomless pit of confusion, one field reporter was the first to recover. He thrust a microphone toward Jin Taekyung.

“J-Jin Taekyung, is that you?”

“No. This is Patrick.”

“Huh?”

“I’m kidding. It’s me.”

*That bastard was joking? On live television, no less?*

Dazed by the completely unexpected dumb joke, the reporter pulled himself together and asked another question.

“So you didn’t die after all.”

“Seeing as I’m doing this interview here, it looks like I didn’t.”

“Then who is the person on the stretcher that came out earlier?”

“Oh, that.”

Jin Taekyung scratched his neck before answering.

“Well, how should I put it… He’s a Hunter who was injured fighting bravely. It’s not that serious, so he’ll recover soon.”

“Then where is the Named Monster?”

“The Named Monster? There isn’t one.”

“What? Are you saying there was no Named Monster in the first place?”

“No, there was one.”

Jin Taekyung calmly added:

“Now there isn’t.”

It was the moment a legend was born.



* * *



“I have something I’d like to ask…”

Team Leader Choi suddenly raised his head from the newspaper covered in curling foreign letters.

“Why exactly is Jin Taekyung in my office?”

“Why? Am I not allowed to drop by?”

“You come here more often than I do, despite the fact that I’m the owner.”

“Come on, these things happen. I only stopped by briefly after coming to see your face.”

“The door was locked.”

“It was open.”

“You broke the lock.”

“Really? How strange.”

“I’m asking just in case—really, just in case…”

Team Leader Choi removed the glasses he had been wearing and asked calmly,

“Are you coming here because of the seventeenth-century-style Russian imperial sofa made by the Russian furniture master Sorkovache?”

I was sprawled across the sofa when I answered.

“Absolutely not.”

“Do you realize that saying that while lying like that is not very persuasive?”

“Nope. Ah, this is comfortable.”

The price tag made it uncomfortable, but once I leaned my back against it, I couldn’t pull myself away.

As befitted a chaebol—no, a third-generation hero—Team Leader Choi’s office was packed with things like this.

A state-of-the-art hologram TV with unbelievable picture quality was one of them.



“The next video we’d like to show you is the sensational clip that’s been heating up the past week. Johnson, have you seen it?”

On the screen, a Black man nodded at the long-nosed white man’s question. For some reason, his name being Johnson made me curious.

“Of course, Conan. I’ve already memorized all the lines.”

“What lines?”

“You know, the last thing he said.”

It was a popular American talk show, famous enough that even I had heard of it.

The co-host, Johnson, opened his mouth with a serious expression.

“It wath there. Now it’th gone.”

“Ha-ha! Exactly the same.”

“…….”

*Exactly the same, my ass. Does he have actual snails in his ears instead of cochleae?*

I shook my head and turned off the TV.

They were bound to play *that interview* again as stock footage, so turning it off myself at this point was the wise choice.

“His popularity shows no sign of fading.”

“I know. I never imagined something I said without thinking would become this huge.”

“I’m afraid I have a different opinion.”

Team Leader Choi had already quickly prepared a cup of coffee. He sat down across from me and continued.

“It wasn’t the words that became a hot topic. It was the person. You hunted two Named Monsters, alone at that. It’s only natural for the whole world to take notice.”

A week had already passed, but the impact of that day had not faded. If anything, it was burning hotter than ever.

My official interview video on iTube surpassed two hundred million views within twenty-four hours, shattering the record previously held by an idol singer. Edited videos and all kinds of memes were pouring out from every corner of the world.

And on top of that…

“We received an interview request from the American broadcaster CNM.”

“Again?”

“I already told you that BCC in the United Kingdom made an offer. They want to invite you as a special guest and said they can give you up to twenty minutes for a live interview.”

“Special indeed. Really.”

Interview requests were pouring in from the flagship broadcasters of major countries whose names everyone knew.

Of course, I had not accepted a single one. By now, merely hearing about them gave me a throbbing headache.

“Are you still thinking about it?”

“Yes. If it’s for the Peace Guild’s growth, I should do everything I can, but…”

I lowered my voice until only Team Leader Choi could hear me.

“All of this is bullshit, you know.”

That was right. This was the most important thing.

None of what surrounded me was actually true.

Team Leader Choi spoke with a tense expression.

“That… Did you bring it again today?”

“Of course.”

With the solemn expression of a priest performing a ritual to summon a god, I chanted the incantation.

“Come forth, Warlordmon!”

Inventory. Summon.

At the command I called out in my mind, a black, glossy skull appeared on my palm with a loud clatter.

“Who are you calling Warlordmon?! I am the master of the Black Forest and the commander of the great Army of the Dead! I’m a Skeleton Warlord!”

“Warlordmon, forward roll!”

“You crazy human!”

“Warlordmon, Quick Attack!”

Papapapapat!

Team Leader Choi watched me clutch the Warlord’s skull and shake it at insane speed. Then he muttered as if he had reached enlightenment.

“Why on earth did you capture that thing and bring it back…?”
## Chapter artifact 303

# Chapter 303

A week earlier, the four people who had heard my entire story reacted in ways that were all the same—and yet completely different.

*“You controlled a captured Named Monster and used it to raid? Hahaha! You’re fucking insane!”*

*“……Are you actually fucking crazy?”*

*“I’m sorry to say this, but… are you really insane, Hunter Jin Taekyung?”*

*“You’re insane. I’ll pretend I didn’t hear any of this.”*

The only person who laughed was Im Kkeokjeong. Song Song, Butler Kim, and Team Leader Choi looked at me as if I were a mental patient.

But what could I do? The moment the interview ended, the media erupted like an active volcano, and before an hour had passed, I had become a celebrity known by half the population of Korea.

“I should have stopped you even then.”

Papapapapat!

Team Leader Choi lamented as he watched Warlordmon’s Quick Attack.

But the water had already been spilled, and considering how badly I had spilled it, everything had been cleaned up without a hitch.

“Still, it all worked out.”

Even the government-affiliated audit team, famous for its thoroughness, failed to discover the truth behind the incident.

That was only natural. No one could have imagined such a thing. Besides, there was evidence to back up that version of events.

“The mana distribution survey conducted with a mana meter came back clean. They even found bones along with fragments of the armor the Skeleton Warlord was wearing, so it was an open-and-shut case.”

Everything leaves a trace.

Unlike the other Skeletons, which had melted or been smashed apart by One Annihilation, the Warlord’s bones were unbelievably hard and had managed to retain their shape perfectly.

Those bones, still saturated with powerful mana, were accepted as crucial evidence proving the existence and defeat of a Named Monster.

“Come to think of it, didn’t they put those broth bones up for auction? I wonder how much they sold for.”

- Broth bones?! Do not refer to my noble body in such a manner!

“You still don’t understand your situation. Warlordmon, Body Slam.”

Thump! Thump! Thump!

Bouncing off the office wall like a tennis ball, the Warlord clicked its jawbone mournfully.

- Ah, my loyal soldiers. I long to see you.

“So, where’s this month’s tribute of troops?”

- ……I shall replenish them as soon as possible.

Just then, the office door opened with a click.

A pair of shapely legs started to step inside, then stopped short. Looking at the light-brown eyes above them, I asked,

“What are you doing? Aren’t you coming in?”

“……Jin Taekyung, you crazy bastard. If you were me, would you want to enter a room where someone was playing ball with a talking skeleton?”

“Yeah.”

I waved the Skeleton Warlord at the revolted Song Song.

“Warlordmon, scare her.”

“Eeeeeeek! Don’t! I said don’t!”

“Warlordmon, wag your tail.”

- I do not have a tail.

“Then use Quick Attack.”

Papapapapat!

- Urrrgh, urrrghhhh!

“Eeeeeeeek!”

Thank God for the sound-blocking spell.

Just as Song Song’s screams and the Skeleton Warlord’s howls formed an exquisite harmony like an a cappella performance, Team Leader Choi’s phone, which had been lying on the table, rang.

“Everyone, be quiet for a moment.”

Several minutes passed as Team Leader Choi stared intently at the screen. Then his lips finally parted.

“I think I’ll have to step away.”

“Did something happen?”

Team Leader Choi shook his head at my question.

“I’ll tell you once this matter is confirmed. And, Miss Song.”

“Yes?”

“First, cancel the additional raid scheduled for next week. I expect to be neglecting my duties for several days, so please assist Butler Kim.”

At that moment, Butler Kim needed ten bodies and still wouldn’t have enough. He was busy handling the aftermath of the incident, commanding the Guild members during raids, and training in the Jin Family’s Cultivation Technique all at once.

Of course, he was sharing the work with the other four people, myself included. But as the Guild Master, his workload was on an entirely different level.

“Got it. That’s easy enough. It’s not like we can make Uncle Kkeokjeong do it.”

Song Song nodded readily, then paused and looked at me.

“But what are you going to do?”

“Me?”

“Who else could I be talking about? There’s no one here but you.”

“Warlordmon, Quick—”

“If you do that one more time, I’ll kill you. I mean it.”

“……Attack.”

That was probably enough.

I casually slipped Warlordmon into my Inventory as it spasmed reflexively like one of Pavlov’s dogs.

“I’m getting ready to leave work.”

“Leave work? I’m working overtime today.”

“I have somewhere to be.”

“Oh, really? What could possibly be so important that you get to leave on time while everyone else is still working?”

I answered with a huge yawn.

“An exam.”

“An exam? What kind of exam?”

“What kind do you think? Don’t you even know what day it is?”

Song Song blinked for a moment, then her eyes widened.

It was the middle of November. Even the busiest person alive would know what day it was. It was the day of an exam important enough for the news to run a countdown.

“Are you taking the college entrance exam?”

“Are you crazy? My sister is.”

I checked the clock hanging on the office wall.

Five in the afternoon. If I left now, I thought I could arrive in time for the end.

“I’m heading out. Hang in there. You too, Song-i.”

I rose from the soft sofa and left the office.

I could picture my mother praying fervently near the test center and Hayeon working her way through the questions.

*I’m worried. She probably hasn’t been able to study properly lately because of me.*

For the past few months, Hayeon had been exposed to the media because of the various problems surrounding me and had been forced to endure intense attention from everyone around her.

For a student on the verge of taking the college entrance exam, it was devastating.

*I feel bad.*

I hoped the results would reflect all the effort she had put in.

With an uneasy feeling in my chest, I headed for the test center. An hour later, I saw Hayeon’s gloomy face and realized that what I had feared had come to pass.

“You… No, never mind. You worked hard.”

“Yes, sweetheart. You worked so hard.”

At my mother’s and my words, Hayeon gave a faint smile.

“Well, this is something. The man whose face is so hard to see actually came all the way here.”

“My little sister is taking the college entrance exam. Of course I had to come, you idiot.”

“Even after disguising yourself like that?”

“Is it that obvious?”

“Yes. Sunglasses and a mask at night look really stupid. They make you stand out even more.”

“Damn it. No wonder people kept staring at me.”

“Are you an idiot? Of course people are going to stare if you disguise yourself that blatantly.”

Hayeon’s grayish smile was as wilted and feeble as she was. Seeing how completely drained she looked only made me feel guiltier.

“You okay?”

Hayeon answered with a depressed expression.

“No.”

“I’m sorry. It’s because of me.”

“I thought I’d get a perfect score, but I got one wrong in English.”

“As your brother, all I’ve done is cause you trouble like this. I’m so sorry I can’t even bring myself to look you in the face… What did you say?”

“I got one wrong. I missed a perfect score on the college entrance exam by one question!”

Thud! Thud!

I stared blankly at Hayeon as she kicked the ground in frustration.

*Is she crazy?*

She got only one question wrong across every subject on the college entrance exam?

I knew she was smart, but I had no idea she was this smart.

*No, more importantly, how does she already know she got one wrong?*

Was that why she had come out thirty minutes late?

Either way, one thing was certain. This winter was going to be a fairly warm one for our family.

And…

“I got one wrong! If I’d gotten just one more right, I would have had a perfect score, but I missed it!”

If I left this lunatic alone, the students and parents around us would set up a net over heaven and earth to hunt our family down.

“Stop talking nonsense and let’s go eat.”

“Let go! How could someone with seventh-tier school grades understand how I feel?”

“Keep your voice down, please.”

I grabbed my hysterical sister by the back of the neck and dragged her away. From inside my Inventory, the Skeleton Warlord muttered,

- Blood truly cannot lie.

You’re getting one hundred Quick Attacks. Guaranteed.

* * *

Time flew by.

With Hayeon’s college entrance exam finally over, our family moved into our old house after the remodeling was completed, and my mother shed tears of emotion at the unexpected gift.

“Son… Thank you so much. I don’t know what to say.”

“It’s nothing. Please don’t say that.”

“I’m grateful too, son.”

“Hayeon, do you want to end your life now that your college entrance exam is over?”

Resolving the matter I had kept in mind for so long left me feeling much lighter.

But something still nagged at me.

*They might reach out to my family.*

Taking a family member hostage was a simple yet effective tactic.

I didn’t think Lee Jungryong, who had a weakness, would resort to such a method, but I had to prepare for the worst.

*I’ll keep making money anyway, so there’s no reason to hold back.*

Top Hunters were high-income earners—wealthy enough to be called walking small and midsize businesses.

But even those top Hunters couldn’t compare to my income.

I finished raids several times faster than other people, and I often played solo.

A Hunter’s outstanding skill naturally drew in wealth.

And if there was one more thing that came with it, it was fame.

“Butler Kim, could you handle the interview and advertising offers that have come in for me?”

“All of them?”

“No. Just the important ones with high pay.”

Even though I accepted only a tiny fraction of the hundreds of offers, an enormous sum of money was deposited into my account.

The interest people showed in me was that intense, both in Korea and abroad.

A few advertisements, interviews, and appearances on television talk shows. That was more than enough.

The number in my bank account became morbidly obese, and the Peace Guild’s stock price shot up.

Two birds with one stone. A double gain.

“May I ask one important favor?”

“Of course. Anything.”

“Please look into a security company. A reliable one.”

“Heh-heh. Leave it to me.”

My mother and Hayeon didn’t notice a thing.

They didn’t know that the houses on either side of ours and the ones across the street had been secretly purchased. They didn’t know that several seemingly happy married couples were actually secret bodyguards.

They were merely puzzled.

“Son, did you know a lot of married couples live around here?”

“Really?”

“Yes. I run into them every time I go to the neighborhood market. There are young couples and older couples, but every single one of them seems to be childless.”

“It’s the age of low birth rates.”

“Oppa, there are only two men living next door. They walk around with their arms linked.”

“……It’s the age of gender equality.”

That made them stand out way too much!

A few days after I asked the company to rearrange the personnel, a KakaoTalk message arrived from Hayeon.

> **Jin Hayeon**
>
> Wow
>
> This time two women moved in
>
> They walk around with their fingers interlaced all the time;;

“…….”

Could this security company really be trusted?

Contrary to my concerns, the bodyguards did an excellent job.

Reports came in every thirty minutes, and they never took their eyes off my family.

I was so busy I barely had time to breathe, but everything was proceeding smoothly. Even so, there was one disappointing thing.

My leveling up.

Ding.



> **System**
>
> - You defeated a Lv.70 Skeleton Archer!
>
> - You gained an extremely small amount of EXP!
>
> - The difference in power is substantial. The amount of EXP gained is drastically reduced.

“Oh, shit. God, please!”

Contrary to my desperate hopes, the EXP factory was no longer of much help to me.

Three or four level-ups. That was all.

- Heh-heh. I do not know what these things you call EXP and level-ups are, but this is good news. Human, this is what comes of greed!

“But if I erase you, I can probably get one more level-up, right?”

- ……I shall try harder. Please, anything but that!

“Hoo. I’ll put that off for now. But you’ll keep offering up your tribute of troops.”

- Why?! You said there was nothing left to gain from killing my soldiers!

“That’s true for me. Our Guild members still need to gain experience of their own.”

- Experience?

“We can use them to give our people some combat practice. Have your subordinates rehearse their acting. Tell them to make it convincing without letting on that they’re going easy on us. Of course, you know what happens if anyone on our side dies, right?”

- ……You intend to suck the marrow from my bones. Just how cruel can the human race be?

The Skeleton Warlord lamented, but I already held its leash.

The new Guild members gained real combat experience—well, almost real—against the Skeletons, who were excellent supporting actors.

*That’s right. Work hard and grow big and strong.*

It was exactly one week after Hayeon’s college entrance exam when Team Leader Choi appeared.

“Long time no see, everyone. But before we discuss what happened, I need to show you this first.”

With a tired voice and a stiff smile, he looked at us, pulled a USB drive from inside his jacket, and connected it to the hologram TV.

“This is a video from China.”

Beep.

The video began playing with a chilly electronic tone.
## Chapter artifact 304

# Chapter 304

Inside the office, every source of light had been blocked out. When a holographic video began playing in the darkness, I was suddenly overcome by the sensation that I was there at the scene myself.

*This place is…*

Everything was gray. I couldn’t see even an inch ahead of me.

Only after I saw the massive wings of an eagle skim past dangerously close did I realize where the video had begun.

*The sky.*

The drone capturing the entire scene descended rapidly to avoid the fine dust filling the atmosphere.

Whoooosh.

After descending through the fierce wind for some time, what finally emerged was a city engulfed in flames.

Boom! Rumble-rumble-rumble!

“Eeeeeek!”

“Aaaaaah!”

The factories belching smoke exploded one after another. Massive buildings collapsed like dominoes, while people who looked like tiny dots screamed and fled in every direction.

It was pandemonium.

There were too many people to count individually.

Thousands were visible at a glance. If the people the camera had failed to capture were included, there had to be tens of thousands.

“What the hell is this…?”

A lament escaped me before I could stop it. Was this because of a factory explosion?

No. It was because I had discovered creatures racing through the maze-like city, wreaking destruction and slaughter.

“Grrrrrrr!”

“Graaah!”

Massive bodies. Strength and Agility that could only belong to monsters.

Their eyes gleamed with killing intent as they swept across their surroundings. Then, with a series of hideous roars, they began moving in search of targets.

*Why are there monsters there?*

The question lasted only a moment before I realized the answer myself.

There was only one possibility in a situation like this.

*Monster Wave.*

During the Great Cataclysm, Gates had been passageways connecting Earth to another world known as the Demon Realm.

But after the Demon King Asmodeus disappeared, the monsters’ power weakened, and Gates became doors that only humans could freely pass through.

There was one exception.

If the mana inside a Gate exceeded its capacity, everything changed.

*When a dam breaks, the water comes rushing out.*

That was a Monster Wave, and the result was the scene the holographic video was showing us now.

“Kyaaaaaa!”

“P-please, save me…!”

Squish!

The zoomed-in camera showed the urban center where a massacre was taking place.

Monsters slaughtered and destroyed without restraint while humans died helplessly around them.

Some were impaled on monster claws. Others were trampled to death beneath the feet of the fleeing crowd.

Amid that pit of chaos, a mother and daughter running for their lives caught my eye.

“Bingbing! Hold Mommy’s hand tight!”

That was when the woman shouted urgently.

Whoosh! Thunk!

A spear flew from a dark alley, pierced the woman through the chest, and embedded itself in the ground.

She vomited up a mouthful of blood, then her body went limp.

The child, who had witnessed her mother’s death right before her eyes, burst into tears.

“Mommy!”

But it wasn’t over yet. More than a hundred Orcs poured out of the dark alley and advanced toward the child.

They had taken up ideal positions to block the fleeing civilians’ escape routes.

One Orc who appeared to be their leader raised an axe and brought it down toward the crying child.

Whish! Slice!

“Krk?”

The leader stared down at his arm with bewilderment.

The thick arm that had been holding the axe had been cleanly severed below the elbow. A man was standing before him now, though the Orc hadn’t noticed him arrive.

“How dare you monsters lay hands on the people of China?”

A dazzling aura flashed.

Slice!

The leader’s head was severed. Before it could even hit the ground, a thunderous cry burst from the man’s mouth.

“Public Security Armed Forces Division!”

“Yes!”

The answer rang out loudly.

The man was not alone. Even now, Hunters belonging to the Public Security Armed Forces, their armor emblazoned with China’s Five-Starred Red Flag, were steadily joining the battlefield.

The man shouted, his eyes burning.

“Kill every last one of those stinking bastards!”

“For the people!”

Sh-sh-sh-shk!

With a tremendous roar, more than a thousand Hunters charged forward.

China still had a population of well over a billion despite suffering enormous losses during the Great Cataclysm.

The strength of each individual was unknown, but it would not be an exaggeration to say that China could mobilize more Hunters than any other country in the world.

“Wipe them all out!”

“Waaah! Long live the People’s Republic of China!”

A thousand Hunters charged as one.

The monsters rampaging through the city had no intention of simply standing by and watching. When every kind of monster gathered in one place, their numbers easily surpassed a thousand as well.

“Gwoooooo!”

“Kya-woo!”

Thud-thud-thud-thud-thud!

Monsters and humans. Humans and monsters.

Two waves that could never coexist rushed toward each other.

Eyes shining with resolve, and killing intent directed at the enemy.

The incredible force of the scene filled the office, so intense that it was hard to believe we were watching a holographic video.

The drone captured the two groups rapidly closing the distance between them from high above.

Five hundred meters. Three hundred. One hundred…

Just as the deafening noise reached its peak and the two sides were about to collide—

“Perish in the flames of the inferno. Fire Rain.”

A cold, lifeless voice.

At the same time, the gray sky split open.

Kiiiiing.

It was a sight I had never seen before.

About thirty meters above the ground, not far from the drone, the air peeled open as though something had sliced through it.

A massive ball of flame emerged from a vortex writhing with black energy.

Whoooosh!

The Chinese Hunters stopped without realizing it and stared blankly at the sight.

“This can’t be.”

“This is… a dream.”

Sadly, it was all real.

Crack!

A sphere of flame dozens of meters in diameter split into four pieces. Each of the four pieces split into dozens more, and those dozens became hundreds of fragments.

A rain of fire slammed into the ground.

Whoooom! KABOOM!

Rrrrrumble!

The surroundings were dyed red by the deafening explosions.

The drone was thrown off balance by the aftershock. When it finally steadied itself, the being responsible for creating that spectacular scene was staring directly at it.

“A human device, I see.”

The voice had no inflection or vitality.

The figure had pulled a robe marked with strange patterns low over his head. He extended one finger and pointed at the drone.

“I shall kill you all and take everything. Anyone who sets foot on my territory will pay for it with their life.”

Bzzzzzt!

The instant that finger, twisted like the root of an ancient tree, moved, the video cut out amid a burst of static.

The gray sky filled with fine dust disappeared. So did the scene on the ground, one that deserved to be called the end of the world.

The hologram vanished, and a heavy silence descended over the office.

I was the first to speak.

“What the hell is that bastard?”

“He’s the man behind this Monster Wave. No—he isn’t a man, so I suppose that phrase isn’t quite right.”

Team Leader Choi continued in a subdued voice.

“The Named Monster Lich. That is what he is.”

* * *

A Lich.

A fallen archmage. An apex monster reigning at the top of the pyramid of countless undead.

The Lich that had supposedly vanished after the Great Cataclysm had appeared. It had caused an enormous catastrophe, as though celebrating its return after several decades.

Team Leader Choi pulled out the USB drive and spoke.

“November fifth. This footage was taken exactly ten days ago by a reconnaissance drone belonging to Chinese intelligence. It shows a small city near Nanchong, Sichuan Province. The estimated casualties so far are approximately three hundred thousand. We still don’t have an accurate tally.”

Sichuan.

I was more familiar with it as the region where Qingcheng and Emei of the Nine Sects and One Gang were located, along with the Tang Clan, one of the Five Great Families.

Of course, the Murim was an entirely different world that merely resembled China, and what the hologram had shown us was a massive catastrophe.

“Three hundred thousand?”

“Yes.”

“That’s fucking insane…”

“And that is only the record from the first twenty-four hours after the Wave began.”

A chill ran down my spine.

The estimated casualties for a single day alone were three hundred thousand. Had humanity ever suffered this much damage from a Monster Wave since the Great Cataclysm?

“Are Liches normally this powerful?”

I directed the question not at Team Leader Choi, but at Butler Kim—the only living witness among us who had experienced the Great Cataclysm firsthand.

His eyes trembled like ripples on water.

“Could that possibly be the case? The Liches I saw with my own eyes during the Great Cataclysm were all powerful beings, certainly… but that one is on an entirely different level. Its fire magic was enough to give me goose bumps just watching it.”

Butler Kim was an A-rank mage whose specialty was fire magic.

If someone who had experienced every kind of hardship during the Great Cataclysm spoke like that, it was easy to understand just how powerful the Lich that had appeared this time was.

*Where the hell did something like that come from?*

The burning city and the people collapsing in pools of blood flickered before my eyes. The enormous rain of fire striking the earth had been a disaster in the truest sense of the word.

At the very end, I remembered the declaration the creature had made toward the camera.

*I shall kill you all and take everything. Anyone who sets foot on my territory will pay for it with their life.*

No one else could have understood what it said, but I could.

Thanks to the Integrated Language Pack, part of the System, I had heard its words clearly and understood what they meant.

That merciless undead monster would never be satisfied with a single small city.

Three hundred thousand people in one day? With the power it had displayed, the number of casualties might already be ten times higher by now.

“Goddamn it…”

I didn’t particularly like China, but no sane person would see such a terrible disaster and laugh, saying that they had gotten what they deserved.

A bitter taste filled my mouth as I thought of the people who had died helplessly and the little girl crying after losing her mother. That was when a thought suddenly occurred to me.

*Wait.*

As I recovered somewhat from the shock, something strange struck me.

It had been ten days since a catastrophe of this magnitude had occurred, yet the world was peaceful.

And more importantly…

*Where had Team Leader Choi gotten this information?*

If it had been the Ares Guild—or Lee Jungryong—I could have understood. They were one of the most prominent Guilds in the world, and their intelligence network was excellent.

But Team Leader Choi was merely the leader of a team in an ordinary mid-sized Guild. If he knew about it, news of the Sichuan disaster should already have been broadcasting around the world.

*There’s something going on.*

I wasn’t the only one who had reached that conclusion.

Everyone was looking at Team Leader Choi, demanding an explanation with their eyes.

He was not the kind of person who would fail to notice that atmosphere.

“One week ago, I received an unexpected message.”

That was the day Hayeon finished her college entrance exam.

That day, Team Leader Choi had spent a long time staring at his phone before leaving, saying that something important had come up.

“It was a message from China, wasn’t it?”

Team Leader Choi nodded.

“Yes. More precisely, they were courting one particular person, asking him to take part in this crisis.”

“Putting everything else aside, they specifically asked for me? From China?”

“Yes. ‘He’ wanted you.”

“Who is he?”

A name slipped from Team Leader Choi’s lips.

“Xiao Yang.”

“Gah!”

“Xiao Yang?”

“Young Master. Is that true?”

The moment they heard that name, everyone in the room widened their eyes. Naturally, I did the same.

I stared at Team Leader Choi with my mouth hanging open, then finally managed to speak.

“X-Xiao Yang requested me?”

“Yes.”

“But who is Xiao Yang?”

“……”

Why did they all look like that? It was possible that I didn’t know.

Team Leader Choi’s eyelids trembled for a long moment before he finally opened his mouth.

“Xiao Yang is the General Secretary of China’s Central Committee.”

“Jongseok?”[^1]

“The General Secretary! The President—the President of the country!”

“Holy shit.”

[^1]: Taekyung mishears *chongseogi* (“general secretary”) as the Korean given name Jongseok.

# Checkpoint Review — 75–79

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

# Chapters 75–79

## Plot

Taekyung logs out after roughly twenty days in Murim, finding that only 2:05:35 has passed in the modern world. He reunites with Seong Jinho, signs a contract to join Team Leader Choi’s new Peace Guild, and learns that the deal includes a 500 million won signing bonus, a 50 million won monthly salary, a seventy-percent settlement share, housing, and other benefits. The Guild house is Sooni’s Super, a dilapidated corner store in Bucheon.

Taekyung meets the Guild’s other members: Im Kkeokjeong, Song Song, and Butler Kim. He immediately develops feelings for Song Song and awkwardly attempts to confess during the Guild’s first gathering, but Team Leader Choi repeatedly interrupts him by turning the occasion into a membership celebration. The gathering ends with Song Song drunk and the others revealing their backgrounds: Choi formerly led a team in the Ares Guild, Song Song served on that team, and Butler Kim is a retired mage and former Hunter. Choi establishes Butler Kim as Guild Master and himself as Team Leader.

The next morning, the hungover members learn that the Peace Guild must begin working. Choi presents footage of the Bucheon Terminal Guild’s raid against seven B-rank Minotaurs in The Minotaur’s Labyrinth. Although the monsters were defeated, two C-rank Hunters died. Taekyung uses Qi Sense to assess the Peace Guild’s members—Choi Minwoo at Level 75, Kim Hwajong at Level 80, Song Song at Level 64, and Im Hyeokjun at Level 24—and concludes that their first raid will be dangerous.

## Continuity

- Taekyung is a Peace Guild member and has completed the Guild Membership achievement, receiving 10 points.
- His Peace Guild contract provides a 500 million won signing bonus, a fixed monthly salary of 50 million won, a seventy-percent settlement share, housing, a car, and other benefits.
- The Peace Guild has five members: Guild Master Butler Kim, Team Leader Choi, Taekyung, Im Kkeokjeong, and Song Song. Choi leads Team 1; Taekyung, Im, and Song Song are its members.
- Sooni’s Super is the Guild house, located in a dilapidated, Gate-dense district of Bucheon. The property cost slightly more than 2 billion won per pyeong.
- Im Kkeokjeong joined after Choi recruited him while he was hospitalized. He is married and has two children.
- Song Song previously worked under Choi in the Ares Guild. Taekyung is attracted to her, but his interrupted confession leaves her response unclear.
- Butler Kim is a retired mage and former Hunter. He and Taekyung trained at Nonsan’s 28th Regiment, 1st Battalion, but Kim’s former rank and wider background remain unknown.
- The Peace Guild is preparing for its first raid. The Bucheon Terminal Guild’s recent raid against seven B-rank Minotaurs killed two C-rank Hunters despite defeating all the monsters, establishing the danger of the upcoming operation.
- The members’ displayed Levels are Choi Minwoo 75, Kim Hwajong 80, Song Song 64, and Im Hyeokjun 24.
- Essence of the Himalayas temporarily increases Taekyung’s Intelligence by 1 for one hour.
- In Murim, Taekyung, Jin Mukyung, and Hyuk Mujin are traveling to Eung-hyeon to visit the Mount Heng Sword Sect. The forced [Yesterday’s Enemy, Today’s Ally] Quest—to deliver Jin Wikyung’s New Year’s Day invitation—remains unresolved.
- The identity and sponsor of the assassin who attacked Taekyung and Hyuk Mujin remain unconfirmed. The possible connection to Song Sword Sect is also unresolved.
- Jin Wikyung still plans to summon Shanxi’s sects on New Year’s Day and may seek the Alliance Leader position. Whether the sects will respond remains unknown.

## Translation Decisions

- Retain **Peace Guild**, **Ares Guild**, **Guild Master**, **Team Leader Choi**, **Butler Kim**, **Song Song**, **Miss Song**, **Im Kkeokjeong**, and **Sooni’s Super**.
- Use **Minotaur**, **Bucheon Terminal Guild**, and **The Minotaur’s Labyrinth**.
- Retain **Qi Sense**, **Essence of the Himalayas**, **Sleep Mode**, **Return**, **Returnee**, **New Year’s Day**, **Alliance Leader**, and **Quest**.
- Use **mage** for 마법사, **Senior** for Taekyung’s deferential address to Butler Kim, and **haejangguk** and **makgeolli** with concise cultural footnotes.
- Retain **pyeong**, with a footnote explaining that it is approximately 3.3 square meters.

## Durable state

{
  "active_continuity": [
    "Taekyung successfully logged out after roughly twenty days in Murim; his watch showed 2:05:35 in the modern world, and he states that ten modern-world days now correspond to one hour in Murim.",
    "Taekyung currently has fifteen years of internal energy. Circulating his qi slightly increases his internal energy, and Sleep Mode normally keeps his sleep below three hours except when he is seriously injured.",
    "Seong Jinho is thirty, has lived with Taekyung as a friend and brother for years, and now plans to move out of the goshiwon soon, though the date is not fixed.",
    "Team Leader Choi owns the café where he meets Taekyung and gives him a contract; Taekyung signs it, after which a System alert appears.",
    "After ten days of Mukyung's training, Taekyung mastered the Jin Family's Spear Technique and Jin Family's Manoeuvre Technique; the Training? Trial! Quest succeeded and granted a Level Up, an Inventory reward, and notice of an additional reward.",
    "Hyuk Mujin remains badly injured and under treatment after the attack; the unidentified assassin may be the Head Elder's hidden disciple.",
    "Jin Mukyung reunited with Jin Wikyung after three years but remains detached and prioritizes sword training. Jin Wikyung plans to summon every Shanxi sect on New Year's Day and may seek to become Alliance Leader.",
    "Wipeng leads thirty elites south under the pretext of pursuing the nonexistent assassin, visited Song Sword Sect, and delivered Wikyung's summons as both summons and warning; Wikyung found no information on Dark Heaven in the family records.",
    "Gong Yacheong is recovering and will take charge of the rebuilt Sakju Branch; Socheon and Soyul will accompany him in six months. Soyul is five and does not know her parents are dead.",
    "The Returnee title grants Taekyung All Stats +10 and activates Login and Logout. Taekyung accepted that he was half-finished, asked Mukyung for help, and received a System time limit of 9 days 20 hours 23 minutes.",
    "Childeuk is an injured former meal-delivery servant who became a Level 12 martial artist directly under Jin Wikyung; Wikyung publicly embraced and praised him after acknowledging a minor misunderstanding.",
    "Lee Seowol is the new female Sect Leader of the Mount Heng Sword Sect. Taekyung received the forced Yesterday's Enemy, Today's Ally Quest to deliver an invitation for New Year's Day; its completion and Reward remain unknown.",
    "Taekyung, Mukyung, and Hyuk Mujin departed for Eung-hyeon in a four-horse carriage because Lee Seowol requested their visit and Mukyung may learn Peak martial arts.",
    "Taekyung is a member of the Peace Guild, completed the Guild Membership achievement, and received 10 points. His contract provides a 500 million won signing bonus, a fixed monthly salary of 50 million won, a seventy-percent settlement share, housing, a car, and other benefits.",
    "The Peace Guild's Guild house is Sooni's Super, a dilapidated corner store in Bucheon's Gate-dense district, on property purchased from the former owner's surviving family for slightly more than 2 billion won per pyeong.",
    "Im Kkeokjeong joined the Peace Guild after Team Leader Choi recruited him while hospitalized. He is married and has two children.",
    "The Peace Guild has five members: Taekyung, Team Leader Choi, Butler Kim, Im Kkeokjeong, and Song Song. Butler Kim is the Guild Master, Team Leader Choi leads Team 1, and the other three are team members.",
    "Essence of the Himalayas increases Taekyung's Intelligence by 1 for one hour.",
    "Team Leader Choi formerly served as a Team Leader in the Ares Guild, where Song Song was a member of his team. Butler Kim is a retired mage and former Hunter who trained at Nonsan's 28th Regiment, 1st Battalion, as did Taekyung.",
    "The Peace Guild is preparing for its first raid. Choi Minwoo is Level 75, Kim Hwajong Level 80, Song Song Level 64, and Im Hyeokjun Level 24.",
    "A Bucheon Terminal Guild raid against seven B-rank Minotaurs ended with the monsters defeated but two C-rank Hunters dead, making Taekyung judge the Peace Guild's coming raid dangerous."
  ],
  "continuity_sources": [
    79
  ],
  "open_questions": [
    "The identity and sponsor of the assassin who attacked Taekyung and Hyuk Mujin remain unconfirmed.",
    "It remains unresolved whether Hyuk Mujin will actually become the next Master of the Gatekeeper Pavilion.",
    "It remains unresolved whether the Shanxi sects will answer Jin Wikyung's summons and whether he will become Alliance Leader.",
    "It remains unresolved whether Song Sword Sect has any connection to the attack.",
    "The reason the System displayed the same 2-hour-22-minute Time Limit twice remains unexplained.",
    "The nature of the minor misunderstanding that injured Childeuk remains undisclosed.",
    "Taekyung's prior relationship with Lee Seowol and the missing details of his memories about her remain unclear.",
    "Butler Kim's former Hunter rank and background remain unclear, and it is unclear whether Song Song heard Taekyung's interrupted confession."
  ],
  "safe_through": 79,
  "temporary_decisions": [
    "Use gongcheong seokyu for 공청석유 with a footnote explaining the elixir and petroleum pun; use junzi for 군자 and Junzi Sword for 군자검 with a cultural footnote; render 도덕책 as ethics textbook with a footnote explaining the pun.",
    "Retain Hyung-nim for 형 and 형님 in Taekyung's deferential speech; use Three Questions Gorge for 삼문협, Great Hero for 대협, and Ghost Sword for 귀검.",
    "Use Alliance Leader for 맹주 and summon for 소집; use New Year's Day for 원단 and close the sect's gates for 봉문.",
    "Use Sleep Mode for 수면 모드, Medicine King Hall Master for 약왕당주, four-horse carriage for 사두마차, and goshiwon for 고시원 with a footnote.",
    "Use Return for 귀환, Returnee for 귀환자, Ren and Du meridians for 임독양맥, Heart Demon for 심마, Paralysis Acupoint for 마혈, and Mute Acupoint for 아혈.",
    "Use fist-and-kicking technique for 권각술 and recognition for 인정; render 낙류검 as Falling Flow Sword, 질풍십이권 as Twelve Gale Fists, 화염신장 as Flame Divine Palm, and 분근착골 as Tendon-Splitting and Bone-Twisting.",
    "Render 비급 제작 as Martial Arts Manual Creation, 맷집 as Toughness, 천무지체 as Heavenly Martial Physique, 장칠득 as Jang Childeuk, Martial Artist Jang for 장 무인, 인의예지 as benevolence, righteousness, propriety, and wisdom, 호환 as killed by a tiger, 일각 as fifteen minutes, and 모태 솔로 as lifelong single; use “Let's eat noodles” for 국수 먹자 with a cultural footnote.",
    "Use Squad Leader for 조장님, Third Young Master for 삼공자님, Mujin for 무진아, seventh-tier student for 내신 칠 등급, Team Leader Choi for 최 팀장, Designer-Brand Junkie for 명품충, Qi Sense for 기감, Peace Guild for 평화, Essence of the Himalayas for 히말라야의 정수, Sooni's Super for 순이네 수퍼, Song Song for 송송이, Miss Song for 송이 씨, Taurus for 황소자리, Ares Guild for 아레스 길드, Senior for 선배님, Young Master for 도련님, Guild Master for 길드장님, Minotaur for 미노타우로스, Bucheon Terminal Guild for 부천터미널 길드, The Minotaur's Labyrinth for 미노타우로스의 미로, haejangguk for 해장국, and makgeolli for 막걸리."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 75

# Chapter 75

The way to tell the modern world apart from Murim is, oddly enough, by smell and temperature.

The smell of sweat inside a VR helmet. The heat inside a capsule warmed just right by sunlight streaming through the window.

“Phew.”

Once I took off the helmet and climbed out of the capsule, I finally felt like I could breathe. It was still only the difference between a scalding bath and a hot bath, though.

*How much time has passed?*

I checked the watch on my wrist. The cheap twelve-thousand-won digital watch I had bought from a street stall in front of the Hunter training center about seven years ago had the advantage of coming with an alarm and stopwatch function.

Beep.



[02:05:35]



Two hours, five minutes, and thirty-five seconds.

I had spent around twenty days in Murim, so the timing roughly matched what had happened last time.

*Since I came to the modern world, the time ratio must have been reversed.*

Now that I had logged out, ten days in the modern world amounted to one hour in Murim. I washed myself in the communal shower of the goshiwon[^1] and returned to my room.

Just as I was about to close the door, a black shadow shot upward.

“Wah!”

Of course. It was Seong Jinho.

“Oh. My. God. What a surprise.”

“……What’s with that reaction? You knew I was here?”

“Your inhaling and exhaling were extremely intense. Mr. Jinho, were you excited?”

My five senses had grown sharper with each passing day. I could pick up every sound and movement around me without even using Qi Sense.

He seemed to have been waiting in silence, but to my ears, every tiny movement and breath he made sounded like thunder.

“Breathe a little more quietly. You’re supposedly the goshiwon manager, so it would be a problem if people filed complaints because your breathing was too loud.”

“Damn it. How did you know? You’re just an F-rank Hunter…… Oh, right. You became C-rank a while ago.”

“Look at the way you talk. Making fun of me for being F-rank has really become a habit.”

“Hey, if you were my age, would you remember something that happened barely a week ago? I can’t even remember what side dishes I ate yesterday.”

“A week?”

Was that really all the time that had passed?

To me, it had been well over a month. To Jinho-hyung, it had been barely a week. I felt a subtle sense of disconnect.

“Hey. Why do you look like that? Is something wrong?”

“What do you mean, something’s wrong? Anyway, what brings you here?”

“Listen to the way you talk. Are we some kind of business relationship that we can only see each other when there’s business involved?”

“Just get to the point. Keep it short.”

Jinho-hyung’s face hardened. Had I gone too far with the teasing?

Come to think of it, I had been too indifferent lately. Even before returning to Murim, I hadn’t been able to see him often because of all sorts of problems……

“Buy me dinner.”

“…….”

“Grilled pork belly. Teppanyaki. Fried chicken and beer.”

Shit. Of course.

And he even had the nerve to choose the menu himself.

“Did I leave money with you?”

“Your money is my money. And my money is my money, isn’t it?”

“Pronounce that properly. Unless you want to feel the fist of a C-rank Hunter.”

Jinho-hyung flinched and rubbed his palms together.

“Please, sir. Use your money to put some grease on my parched stomach.”

“…….”

Talk about changing his tune. Even Udyr would weep.

It was absurd, but I let out a quiet laugh. My stomach had also been screaming after going nearly a month without a proper meal.

*Let’s eat something decent for once.*

I spoke in a solemn voice.

“I approve of your attitude. Lead the way.”

“Where would you like to go, sir?”

“I’m tired of grilled pork belly and teppanyaki. Let’s go for something pricier today.”

“Th-then, sir!”

Jinho-hyung’s eyes widened.

“Hanwoo![^2] The pasture-raised beef famous for its incredible marbling?”

“What the hell are you talking about? We’re going out for gopchang.[^3]”

“…….”

“If you don’t like it, starve.”

Thump.

Jinho-hyung grabbed my shoulder and spoke with a solemn expression.

“I’ve always wanted to eat that.”

The early dinner that began at five that afternoon ended at a third-round makgeolli bar, and Jinho-hyung was completely plastered.

“Krroooorr.”

“…….”

I had seen this scene somewhere before.

As I felt a strange sense of déjà vu and hoisted Jinho-hyung onto my back, my phone rang.



〈Designer-Brand Junkie

**Designer-Brand Junkie**

See you tomorrow at the same time, same place.



It was a short text message. The sender was Team Leader Choi.



* * *



The downside—and upside—of Sleep Mode was that it reduced the amount of time I needed to sleep. Other than when I had suffered serious injuries fighting Jopil, I had never slept for more than three hours.

*It’s useful for training.*

Three in the morning.

I woke up in peak condition and sat cross-legged. At some point, circulating my qi had become how I began and ended every day.

Fwoosh.

A wave of internal energy began to flow.

The fifteen years of internal energy surging from my dantian cleansed the waste products accumulated inside my body and breathed vitality into dormant acupoints.

Ding.

> **System**
>
> - You have finished circulating your qi.
>
> - Your internal energy has increased very slightly.

By the time I opened my eyes at the System notification, more than two hours had passed. If I were in Murim, I would have gone straight to the training yard to warm up, but the real world came with all sorts of restrictions.

Especially in a goshiwon, where the rooms were packed together like a chicken farm.

*Damn goshiwon. I need to get out of here soon.*

This was an age when training was done with money, too. People who made good money had several spacious private training rooms, while people like me had no choice but to adapt to poor conditions.

“Huff. Inhale.”

I spent the entire morning running around the neighborhood, then continued with basic bodyweight exercises without taking a break after I returned. Maybe it was because my Stats had increased, but instead of getting tired, I felt more and more energized.

Watching me, Jinho-hyung asked with a horrified look:

“Don’t you get tired?”

“Not really.”

“I’ve never seen anyone do one-arm push-ups as easily as you. How many have you done?”

“I don’t know. I counted to three hundred, then got too lazy to keep counting.”

“You’re a monster. Is that normal for a C-rank Hunter?”

“By the way, Seong Jinho.”

“Huh?”

“Why are you here?”

Jinho-hyung had appeared ten minutes earlier with a haggard face, and he still hadn’t left my room.

“Can’t you tell? I came to eat ramen.”

Tap tap. Ssshhk.

He naturally dropped a raw egg onto the noodles, which were almost cooked.

His control of the burner flame to leave the egg perfectly runny was worthy of a Peak master.

“Give me three reasons you have to stuff your face with that here.”

“First, there’s no TV in my room. Second, there’s a TV in your room. Third, ramen tastes best when you eat it while watching TV.”

The words poured out of him like a flowing stream, and my blood started boiling.

“Just buy one! If you don’t have money, take mine!”

“Ah, maybe not. I’m leaving soon anyway. Why bother adding to my luggage?”

“Then stop coming in and out of here and bothering me…… Huh? What did you just say?”

“What?”

“No, wait. You’re leaving?”

“Ah, that.”

Jinho-hyung scratched his matted hair.

“It just worked out that way. The date isn’t set yet, but I’m planning to move out soon. I can’t stay holed up here forever.”

“…….”

“Why are you looking at me like that?”

“No, it’s nothing.”

I awkwardly looked away.

Who living in a goshiwon didn’t have a story of their own? I had mine, and Jinho-hyung had his. It would be rude to ask for the reason.

*Still, it’s a shame.*

He was someone I’d spent years with, like a friend and a brother. And now he was leaving so suddenly.

Caught up in complicated feelings, I cautiously opened my mouth.

“Hyung, by any chance……”

“I know what you’re about to say, but I respectfully decline.”

Had he realized what I was going to say? Jinho-hyung cut me off decisively and continued.

“Kid, I’m thirty years old. I’ll fill my own bowl.”

“Then there’s nothing I can do.”

I had thought I could probably live with Jinho-hyung, but my premature meddling seemed to have pricked his pride.

With a crumpled expression, he opened the lid of the pot.

“You should’ve just said so from the start.”

“What are you talking about? You weren’t even planning to.”

“What nonsense. I only cooked one because you said you weren’t eating.”

“……?”

Wait a second. How had the conversation suddenly ended up here?

After several seconds of silence, I finally spoke.

“What are you talking about? What’s this about cooking something all of a sudden?”

“Obviously, ramen.”

Jinho-hyung glared at me with a threatening look.

“There’s always someone who says he isn’t eating, then asks for a bite when you cook it well. How many times have I fallen for that one with you?”

“…….”

“So a C-rank Hunter reaches into his poor hyung’s bowl? Are you even human?”

“…….”

So when he had been talking about his bowl earlier, he had meant an actual bowl.

I wanted to throw his own words right back at him.

*Is that thing even human?*

I was a fucking idiot for thinking I could live with someone like him.

Feeling deeply ashamed of myself, I threw on some clothes. It was almost time to meet Team Leader Choi.

Bang!

I slammed the door hard enough to break it and left. One last shout rang out behind me.

“If you’re going to the market, get some kimchi!”

Ah, I wanted to kill him.



* * *



*Where was the place again?*

I dredged up my memories from about twenty days ago and arrived at the meeting place.

It was a large café in the heart of a forest of skyscrapers. A handsome man sitting by the window spotted me and waved.

“Over here.”

I didn’t need him to say anything. There were dozens of tables in the café, yet Team Leader Choi was the only customer sitting inside.

*He’s still handsome.*

Wearing a thin casual suit, Team Leader Choi looked as though he had just stepped out of a fashion shoot. A successful man in his twenties who had everything: looks, money, personality……

No. Leave personality out of it.

After exchanging a brief handshake, we sat down.

“Have you eaten?”

“No.”

Team Leader Choi tilted his head.

“Really? You look like you’ve eaten ramen.”

“…….”

Damn it. This guy’s nose was incredible.

It was too embarrassing to explain the whole story about what had happened at the goshiwon, so I hurriedly changed the subject.

“It’s lunchtime, but there’s no one here.”

“We’re closed.”

“What?”

“The windows are covered with curtains, and there’s a ‘Closed’ sign on the door. Of course no one’s coming in.”

I looked around. Just as Team Leader Choi had said, everything was covered up.

I had assumed the café would naturally be open since it was the meeting place, so I hadn’t noticed. The whole situation was so strange that I blinked.

“But you’re open right now.”

The lights inside were bright, and the air-conditioning kept the place cool. I could glimpse at least ten employees, so why had they closed the door?

Team Leader Choi answered calmly.

“We have to. There’s a customer.”

“You said you weren’t open.”

“That’s up to the owner, isn’t it?”

“Uh…… Team Leader, I’m asking just to be sure.”

“You don’t need to ask. This café is mine.”

Right. I had figured as much.

Thinking back, the café had also been empty except for the two of us the last time we met.

*I keep digging, and the hole never ends.*

I clicked my tongue and said:

“Team Leader, you have a lot of money.”

“I have enough that I don’t need to worry about running short. That’s why I can put a contract like this in front of you.”

Team Leader Choi smiled gently and handed me a folder.

“Now, shall we talk business?”

There was no reason to hesitate any longer. I nodded firmly.

“Let’s.”

An hour later, the System alert rang out just as I finished signing the last page.

Ding.

[^1]: A goshiwon is a very small, inexpensive room-for-rent housing arrangement, often with shared facilities.

[^2]: Hanwoo is a Korean breed of native cattle whose beef is prized for its marbling.

[^3]: Gopchang is a Korean dish made from grilled intestines, usually beef intestines.
## Chapter artifact 76

# Chapter 76

Ding.



> **System**
>
> - You have joined the **Peace Guild**!
>
> - You have completed the **Guild Membership** achievement!
>
> - You receive 10 points as an achievement reward.



*This counts as an achievement too?*

Whenever a System message like this appeared, I felt like I had become some kind of hero. An achievement, huh? That was quite an impressive way to package joining a Guild just to make money.

*Well, I’m not complaining.*

Ten points was a pretty sweet reward on its own, but after hearing what Team Leader Choi said next, I had to keep forcing down the corners of my mouth, which kept trying to shoot upward.

“The signing bonus will be processed by the end of today. As for your housing and any other matters…”

A 500 million won signing bonus, a fixed monthly salary of 50 million won, and a seventy-percent settlement share.

A house and a car provided by the Guild, along with dozens of other benefits.

I had already checked everything in the contract several times, but hearing it laid out like this still made it feel new.

*I’ve really made it.*

Until barely three months ago, I couldn’t have imagined my life turning out like this.

The Sleeping Dragon of Shanxi in Murim, and a Hunter in the real world who casually earned hundreds of millions of won a year.

“Team Leader.”

“As for equipment rentals, you can use anything you want apart from my collection… Huh?”

“Could you slap me once? If this is a dream, I’d like to wake up quickly.”

The moment I finished speaking, my vision flashed.

Thwack!

*Wham?* Not *smack*?

I rubbed my stinging jaw and muttered, “You really don’t hold back.”

“I have trouble refusing a request.”

“I don’t think I told you to use your fist.”

“You didn’t tell me not to use it, either.”

“……”

Without the newly acquired **Toughness** stat, I might have gone sprawling in a most undignified fashion.

*Right. This guy was a B-rank Hunter.*

The fist he had thrown without even taking a stance had landed squarely on my jaw. The power and the point of impact had both been perfect.

“Still, don’t people usually use a slap?”

“There are exceptions. So? Are you feeling more awake now?”

“……Very much so.”

“Good. It’s better for making a first impression if you meet them while you’re in your right mind.”

I looked at Team Leader Choi, bewildered by his sudden remark.

“First impression? Who are we meeting?”

“Who do you think?”

Team Leader Choi continued with a smile.

“The other Guild members.”

“Ah.”

Only then did I remember something I had completely forgotten.

A Guild needed at least three people to be established.

“Shall we get going, then?”

Team Leader Choi pointed out the window. A sleek black limousine was gliding into the parking lot in front of the café.



* * *



“Congratulations.”

The owner of that deep, dignified voice, the sort that belonged in a coffee commercial, was Butler Kim. Even in the sweltering summer, he was dressed in a suit and was expertly driving the limousine.

“Oh, yes. Thank you.”

For some reason, I found it difficult to speak naturally in front of this man. Was it because of the image of a butler I had only ever seen in dramas?

*No. If that were the reason, Team Leader Choi would be even worse.*

After thinking about it for a moment, I decided it was because of Butler Kim’s distinctive atmosphere. The unfamiliarity of riding in a limousine for the first time might have had something to do with it, too.

*A limousine.*

The interior was spacious and stocked with all sorts of things. For example, the small refrigerator Team Leader Choi had just opened.

“Would you like something to drink?”

“Sure.”

I happened to be thirsty.

“Water? Alcohol?”

“You have alcohol?”

Team Leader Choi nodded.

“Of course. Anything you want.”

“Then I’ll have soju and beer. Half and half.”

“……I’ll give you water.”

The bottle of water Team Leader Choi handed me didn’t have even the most ordinary brand name on it.

He told me it had been brought in from somewhere in the Himalayas, and I clicked my tongue inwardly.

*That must cost a ridiculous amount.*

What a fucking waste of money. Still, when I took a sip, it was refreshingly cold.

Gulp.

Ding.



> **System**
>
> - You have consumed **Essence of the Himalayas**.
>
> - Your Intelligence increases by 1 for one hour.



……So this was what all that fucking money was for. Well, this was how wealth got redistributed and the economy stayed active. Right.

The limousine came to a stop while I was wondering whether I could sneak a few bottles away.

Butler Kim spoke in his characteristic deep voice.

“We’ve arrived.”

The moment I got out of the car, my jaw dropped at the sight before me.

A skyscraper towered into the sky. Its exterior gleamed even without direct sunlight, as if it had undergone some kind of magical treatment, and guards in formal uniforms stood waiting at the entrance.

“Wow. Woooow.”

As I continued to marvel at the sight, Team Leader Choi approached me.

“Impressive, isn’t it? It wouldn’t be an exaggeration to say that all the branches of Korea’s top one hundred Guilds are gathered here. There are even branches of foreign mega-Guilds whose names you know just from hearing them.”

I answered without taking my eyes off the building.

“Land must be insanely expensive here.”

“It is. You could call this the center of Gate activity around Bucheon.”

“Like Gangnam in the old days?”

“Neither of us lived through that era, but…… from what I understand, this would be more than that, if anything.”

The value of land had been turned upside down long ago.

Though it had happened before I was born, middle-aged Hunters who had lived through the pre-Great Cataclysm era sometimes became nostalgic and went on about what things had been like back then.

“Back then, if you owned even one house in Gangnam, people said you were born with a silver spoon in your mouth.”

“People used to joke that Bundang was above heaven. That’s how valuable the land there was.”

“It was that expensive?”

“Expensive enough to make you puke. At least until the monsters invaded.”



I knew what happened after that. In the early days of the Great Cataclysm, well-developed metropolitan areas and densely populated regions were the first targets of the monster armies, and humanity had been helpless against them.

Present-day Gangnam and Bundang were cities that had already been destroyed once and rebuilt. After the Great Cataclysm, true prime real estate was divided into two types.

*Safe zones and Gate-dense areas.*

Safe zones, where the chance of a Gate appearing was close to zero, were the best places for ordinary people to live. Gate-dense areas, meanwhile, had the ideal conditions for Hunter Guilds to establish themselves.

*Like a snack bar in front of an elementary school.*

There were around a hundred Gates in Bucheon. Many of them were low-level Gates, but by sheer number, it was still one of the ten most densely concentrated regions in all of Korea.

*And this was the center of it.*

I could tell just by looking at the skyscrapers packed around us. This was a neighborhood where your average small or mid-sized Guild couldn’t even set foot.

*What kind of money did this guy have?*

Just as I was looking at Team Leader Choi with awe, he spoke.

“Let’s work hard and move somewhere like that, too.”

“I’ll devote my loyalty to you…… Huh?”

“Pardon?”

“No, what?”

“What’s wrong?”

*Damn it, why do you think? Are you asking because you don’t know?*

I barely swallowed the words that had risen to my throat before managing to speak.

“You said we’d arrived?”

“Yes, we have.”

I abruptly turned toward Butler Kim.

“Butler Kim, is this the place?”

“It is.”

Butler Kim nodded without hesitation, then added, “However, I believe you’re looking in the wrong direction.”

“The wrong direction?”

“Yes. If you turn your head a little to the right from where you’re standing, you should see it.”

I turned my head as he instructed. After a brief silence, I spoke.

“What is that run-down building?”

Amid the luxurious skyscrapers, the building standing there all by itself looked especially small and dilapidated.

Butler Kim kindly explained.

“Strictly speaking, it’s a supermarket.”

“More precisely, it looks like a corner store.”

I narrowed my eyes and glared at the collapsing store. The yellowed sign read:



**Sooni’s Super**



“Who’s Sooni? What a tacky name.”

“She was an old woman who had lived here for seventy years.”

“Now that I think about it, it’s quite elegant. Sounds like a name that promises a long life.”

“She passed away two months ago.”

“Ah.”

*Why is this happening to me?*

“She was incredibly stubborn, so during the redevelopment of the Gate-dense area, she refused no matter how much money they offered. By then, the other Guilds had already established themselves… In the end, we purchased the property from her surviving family.”

“So that Sooni’s Super is our Guild house?”

“Precisely.”

I stared at the half-collapsed Sooni’s Super with mixed feelings.

A Guild house was the face of a Guild. Its signboard. No matter how expensive the land in this neighborhood was, they had really chosen a place like that……

*No, wait. For a newly established Guild, this is incredible.*

It was only that my expectations had been too high. In an industry crawling with scams, Team Leader Choi had shown me enough sincerity that I could trust him and follow his lead.

“Team Leader Choi.”

“Yes, Taekyung?”

I grabbed Team Leader Choi’s hand.

“I’ll really work hard. I don’t care whether our Guild house is Sooni’s Super or Sooni’s Building.”

Team Leader Choi answered with an awkward expression.

“I’m glad you understand.”

“You know what they say. Though the beginning is humble, its end will be magnificent!”

“It’s already magnificent. Butler Kim, how much did it cost to purchase that lot?”

Butler Kim answered.

“A little over two billion won per pyeong.[^1]”

“……Two billion won per pyeong?”

“Yes.”

After a brief silence, I spoke.

“I believe the beginning is magnificent, but the end will be even more magnificent.”

“……”

“……”

The gazes of Team Leader Choi and Butler Kim struck me like arrows. Just as they stared at me with expressions that seemed to ask, *What kind of asshole is this?* a sound rang out.

Screeeech. Crash!



**Sooni’s Super**



The sign, whose decades-old lettering had been neatly written in Hancom Batang, slammed into the ground.

“……It’ll look fine once we remodel.”

Team Leader Choi muttered in a tiny voice. Then the door of the store opened, and someone stepped out.

“Oh dear, it fell again.”

The powerful man grumbled as he lifted the fallen sign with one hand. At the appearance of this completely unexpected person, my mouth fell open.

“Uncle Kkeokjeong?”

The good-natured middle-aged E-rank Hunter, Im Kkeokjeong, spotted us and waved with a bright smile.

“Hey, Taekyung!”

*What the hell? How did this happen?*

While I stood there dumbfounded, Im Kkeokjeong approached and patted me on the shoulder.

“You little punk. Been doing well? I heard you became C-rank.”

“No, why are you here?”

“Hahaha! Why am I here? Is there something wrong with a Guild member being at the Guild house?”

After letting out a hearty laugh, he continued.

“I was stuck lying in the hospital when Team Leader Choi suddenly came to see me and asked if I wanted to join the Guild. I said yes without a second thought.”

Team Leader Choi, who had been looking sadly at the fallen sign, added, “He seemed like someone I could trust.”

“That young man knows what loyalty means. Mr. Kim over there doesn’t say much, but he’s a really good man. And Miss Song goes without saying.”

“No, wait. Just a second.”

What was going on here?

I asked as calmly as I could, “You joined recently?”

“Yeah.”

Team Leader Choi cut in again.

“He seemed like someone I could trust.”

“That young man knows what loyalty means. Mr. Kim over there doesn’t say much, but…”

“I heard that part. What about the others?”

“Huh?”

“Where are the other Guild members? Surely these four aren’t all of us?”

“Of course not.”

Im Kkeokjeong answered firmly, then added, “Miss Song went shopping. She said she’d throw you a welcome party.”

“Miss Song? She’s the last one?”

“Yeah. Including Miss Song, there are five of us. She left over an hour ago, so she should be back soon.”

I couldn’t hear anything that came after that.

*There are five of us.*

*Is this a dream?*

Im Kkeokjeong’s booming voice snapped me out of my daze as I stared at the collapsing Sooni’s Super.

“Oh, there she is. Miss Song! Over here, over here! The newbie’s here!”

I followed Im Kkeokjeong’s gaze and turned my head.

The final Guild member of the ultra-tiny Guild, and one of its founding members.

*She* was there.

[^1]: A pyeong is a traditional Korean unit of area equal to approximately 3.3 square meters.
## Chapter artifact 77

# Chapter 77

When two men sit around tilting their glasses of liquor, all kinds of topics are bound to come spilling out. Money, people, the future…

Of all those topics, the one Jinho hyung preferred was women.

Whenever he got drunk, he became the saddest man in the world and reminisced about his first love.

*I first met her when I was a high school sophomore.*

*This guy's drunk again.*

*It was March, the start of a new school year, with flowers in full bloom. She opened the classroom door and walked in, and then…*

*You must have been dazzled. The bells of heaven must have started ringing in your ears—ding, ding, ding?*

*Huh? How did you know?*

*Because I've heard this story more than a hundred times. The bells of heaven, my ass. Go write a novel.*

*That's because you don't understand love, you punk. Then again, what would a lifelong single know?*

*It's not that I couldn't date. I chose not to.*

*You lifelong-single bastards always say that. Is there some kind of guidebook? You've never even liked anyone, have you?*

*……I think I have.*

*Oh, forget it. What good is it to tell you a hundred or a thousand times? You have to experience it yourself to understand. Pour me another drink.*

The reason I suddenly remembered that drinking session from a few months ago was simple.

*Hyung was right.*

Ding—ding—

I could hear them. The bells.



* * *



Miss Song.

She had a slender figure and a tiny face. An angel with grocery bags hanging from both hands spotted me and stopped short.

“Who are you?”

Her captivating yet refreshing voice made my mind go blank, while her delicate, doll-like features made my heart pound.

*My God.*

I swallowed dryly. It felt as though I had spent the past twenty-seven years as a lifelong single just for this day.

A simulation was already running in my head.

*Our home will be a country house with a yard. Two children and one cat. Perfect.*

The dating cells that had never budged, even while I circulated my qi, were springing to life.

I opened my mouth to speak in the lowest voice I could manage. Jinho hyung, a self-proclaimed master of romance, had always stressed that I should use a deep, resonant voice with a woman I liked.

“I’m…”

“This is Jin Taekyung. You’ve heard about him too, right, Miss Song? You know, the one I told you about last time. I said my beloved little brother had reawakened as a C-rank Hunter.”

“Oh, you’re that person? You’re younger than I expected.”

“……”

I gently stepped on Im Kkeokjeong’s foot, who had interrupted me out of nowhere, and opened my mouth again.

“Yes. I’m the very…”

“Why did you buy so much? We have a restaurant reserved.”

“It’s expensive and the portions are tiny. Why go there? We can just grill some meat inside.”

“……”

*Team Leader Choi. I’m going to kill you with my own hands. I really am.*

I glared at the meddlers one after another. Butler Kim had been about to say something, but he quietly closed his mouth under my murderous stare.

*This is my only chance.*

It was the perfect moment. No one was interrupting, and Miss Song was looking right at me. I spoke in an attractive, deep voice.

“Hello. My name is Jin Taekyung. I’m twenty-seven years old and recently became a C-rank Hunter. My birthday is April 22. I’m a Taurus, and my blood type is RH-positive, type A. My hobbies are reading and film criticism. I hope we get along.”

“……”

“……”

“……”

In the still silence, no one said a word. At last, her red lips parted.

“Oh, yes.”

Miss Song stared straight at me with her deerlike eyes. Her expression suggested that she had been utterly enchanted by my cavernous voice. And I had even highlighted my intellectual side by mentioning reading and film criticism. This was a hundred-percent success.

*Thank you, Jinho hyung. If this works out, drinks are on me.*

Just as I was cheering inside, Team Leader Choi interrupted in a stammering voice.

“W, why don’t we talk over a meal? Miss Song must be tired from grocery shopping.”

My anger at being interrupted again vanished without a trace the moment I heard her name.

“Song is your first name?”

“Song Song. Song Song is my name.”

Miss Song—or rather, Song Song—answered in a calm voice before slipping inside the store. I stood there blankly, repeating her name to myself.

“Song Song…”

My God, even her name was beautiful. So charming. So dazzling.

She was my type from head to toe. I was half out of my mind at the thought that I had met my fated partner when Team Leader Choi's voice snapped me out of it.

“Mr. Jin.”

“Yes, yes?”

“Um… Never mind. Take your time coming in.”

Team Leader Choi let out a deep sigh and turned away. *What was wrong with him?*

“Did I do something wrong?”

At my question, Butler Kim, who was following Team Leader Choi, stopped short.

“Um… Stay strong.”

Once the two of them left, only Im Kkeokjeong and I remained.

“Hyung-nim. Did I make some kind of mistake?”

“A mistake? No. You committed a crime.”

“A crime?”

“Yes. A crime you could never be forgiven for.”

“Gasp.”

Had I really done something wrong? Just as my heart sank, Im Kkeokjeong continued with a solemn expression.

“The crime of stealing a woman's heart.”

“……!”

“You little punk. Even I almost fell for you. Did you see Miss Song's expression? She was completely smitten. It's over. You won!”

“R-Really?”

“Congratulations, Taekyung! Let's eat noodles!”[^1]

“Hyung-nim!”

I could not contain my emotion and threw myself into Im Kkeokjeong's arms. He laughed heartily and patted me on the back.

“How many kids are you going to have? What? Two? Don't stop there—make it three! Hahahaha!”

[^1]: In Korean, “eating noodles” is a traditional expression associated with celebrating someone's wedding.

* * *



Inside the store.

Team Leader Choi and Butler Kim, who had been pressed right up against the door, turned to face each other.

“What do you think, Butler Kim?”

“I can only admire the Young Master's wise decision to block out the sound with a magic item.”

“Right?”

“Precisely.”

As if they had planned it, the two men glanced over their shoulders. Song Song was busily preparing the meal.

“If Miss Song heard that conversation just now…”

“Even if Miss Song quit the Guild on the spot, we would have to pay the penalty.”

“Where did he learn lines like that? Could it be that you used to say things like that when you were young, Butler Kim?”

Butler Kim answered with a stern expression.

“Young Master, that remark was highly unpleasant to hear. Lines like that did not exist even before the Great Cataclysm.”

“Mr. Jin is a lifelong single, right?”

“If he is not, then starting today I am no longer Butler Kim. I am Butler Park.”

“Hunter Im seems to have problems too.”

“I hate to say this, but I wanted to put a muzzle on him.”

“Hunter Im is unmarried, right?”

“Unfortunately, yes. He even has two children.”

“How on earth…?”

“I wonder the same thing.”

The Guild's future was bleak.

It was at that moment, while the two men shook their heads with gloomy expressions, that a voice came from behind them.

“Excuse me.”

Song Song stood there wearing an apron, one hand on her hip as she looked at the two men.

“What are you two whispering about? You haven't lifted a finger to help while I was preparing everything.”

“Oh, Miss Song. It's just…”

“We'll clean up after the meal.”

“Never mind that. The food is ready, so come and eat. And call Mr. Im and…”

Song Song continued with a sigh.

“That… Taurus, too.”



* * *



In front of the grill, which had been heated to just the right temperature, I opened my mouth with a solemn expression.

“Miss Song.”

Song Song stopped just as she picked up the tongs and scissors.

“Yes?”

“Give them to me. I'll grill the meat.”

“It's okay. You can help clean up afterward.”

“My hobby is grilling meat, and my specialty is cutting it.”

“……I thought your hobbies were reading and film criticism?”

“That was only the tip of the iceberg.”

When I nudged Im Kkeokjeong's foot under the table, immediate backup arrived.

“You wouldn't know this, Miss Song, but this guy can grill meat like nobody's business. One time, he was working five grills at once, just—huh? And when you bite into it, the juices flood your mouth. Fireworks start going off in your head!”

I added one more point in a dignified tone.

“I'm a Taurus.”

“That's right! A Taurus man can grill meat, and he's pure-hearted and honest and so steadfast…”

Crack.

Team Leader Choi set down the broken wooden chopsticks and muttered, “I'm sorry. I couldn't control my strength.”

“Here.”

Song Song handed him a new pair of chopsticks as if she had been waiting for it. My heart sank.

I hated to admit it, but the beautiful woman and handsome man made a wonderful pair.

*No way. It can't be.*

I tried to deny it, but my heart felt heavy.

With a gloomy expression, I placed the meat on the grill.

Sizzle.

What kind of relationship did Song Song have with Team Leader Choi?

Sizzle.

It was obvious they had known each other for a long time. She wouldn't be a founding member of the Guild for no reason.

Sizzle.

Come to think of it, that bastard Team Leader Choi was suspicious. He had been interrupting our conversation from the start. And why had he broken perfectly good chopsticks and ruined the mood?

Sizzle.

A B-rank Hunter claiming he could not control his strength? What kind of excuse was that? Was he showing off how strong he was in front of Song Song? I could tie a knot in metal chopsticks, too…

“Excuse me.”

I looked up with a start. Eyes as clear as a lake were staring straight at me.

“It's burning.”

“Yes, yes?”

“The meat. It's burning.”

“Gasp!”

Sizzle-sizzle-sizzle.

I hurriedly flipped the meat, but it was already too late.

“I'll do it.”

“No. I will.”

“Come to think of it, since you're here for the first time today, it's only right that I grill the meat and serve you.”

My God. She wasn't just an angel on the outside.

*Oh, Miss Song. You’re an ethics textbook.*[^2]

[^2]: In Korean, “ethics textbook” is a pun on a phrase meaning “what on earth are you?”

I fell for her gentle nature all over again.

Slice. Slice.

Sizzle.

After taking the tongs from me, she grilled and cut the meat with practiced skill.

I watched her in a daze.

*She even looks beautiful while grilling meat.*

Her hair was loosely twisted into a bun, and her slender, pale hands moved busily. Every one of her movements seemed to shine.

“Hmm.”

How much time had passed? She had been watching the meat carefully when she spoke.

“It’s done. Could you hand me a plate?”

“Yes, ma'am.”

She neatly placed the fully cooked meat into a disposable container. I had noticed it earlier, but this was clearly not something she had done only once or twice.

“You must have done this a lot.”

“Yes.”

“Did you work part-time at a barbecue restaurant?”

“Yes.”

“Wow. For how long?”

“Two years.”

“Wow, when?”

“When I was in high school.”

“Huh. Not many people worked part-time jobs back then.”

“Oh, yes.”

*What am I going to do? Even her resourcefulness is exactly my type.*

Her answers seemed strangely short, but that had to be my imagination. I showered her with plenty of little responses to keep the conversation going.

*The conversation itself is going smoothly.*

Jinho hyung had said that you had to start by finding common ground if you wanted someone to like you. I spoke passionately.

“We're pretty similar. I used to work two or even three shifts in a day. One day, after I finished work and came home…”

“Oh, yes. But, um.”

“Yes?”

“You seem a little close. The grill is still hot…”

Without realizing it, I had leaned my entire body toward Song Song.

“It's fine. I'll just get a little burned. Hahaha!”

“You should still be careful.”

“I'm really fine. You don't have to worry.”

“……”

Song Song's expression seemed strangely dark. *Could it be…?*

*Is she worried that I might get hurt?*

It was shocking. She was thinking about me this much even though we had only met today.

And then I knew for certain. She was interested in me, too.

Jinho hyung's voice reached me from somewhere, like a hallucination.

*Do you know what the most important virtue is when it comes to becoming a couple? Courage.*

*Taekyung, remember this. A man with courage wins the beauty.*

*Hyung, I think I finally understand. And thank you.*

*That's right. Let's be brave.*

I looked at her with a trembling heart. What I was about to say was something I had never once said in my entire twenty-seven years of life.

“Miss Song. Starting today, you and I are on day one…”

At that moment, Team Leader Choi jumped to his feet and shouted.

“Day one! Today is the first day Hunter Jin Taekyung has become part of our Guild family! Butler Kim?”

“Yes, Young Master! The soju is ready!”

The usually unhurried Butler Kim filled the shot glasses at lightning speed.

Glug-glug-glug!

Not a gentle trickle—it was pouring full blast.

Half of it spilled, while the other half was poured in with such force that I was left speechless. But there was something I absolutely had to say.

“Miss Song. Let me say it again. You and I…”

Team Leader Choi raised his glass high.

“To our Guild!”

“Miss Song. Ignore them and listen to me.”

Song Song answered.

“To our Guild!”

“……”

She didn't hear me, right? Yes. She couldn't have heard me.
## Chapter artifact 78

# Chapter 78

Every Hunter is a heavy drinker.

Even an F-rank Hunter, the lowest classification, possesses physical abilities and a metabolism far beyond those of an ordinary person.

There is a reason people say that while some Hunters do not drink, there are none who cannot.

“Hic. One more glass.”

Well, there was one here.

Miss Song’s eyes had already gone half-glazed as she furiously shook her empty glass.

“One more glaaass!”

*She’s pretty even when she’s drunk… No, that’s not the point. Isn’t this getting a little dangerous?*

I looked at Miss Song with concern.

*She must have drunk too quickly.*

The moment the drinking party had begun in earnest, she had chugged an entire bottle of soju straight from the bottle and had been like this ever since. Every now and then, she slurred incomprehensible things about someone having no damn tact and rotten luck clinging like a curse.

*Is something bad going on?*

While Im Kkeokjeong was filling her glass, I leaned toward Team Leader Choi and whispered.

“Team Leader. Did something happen to Miss Song?”

Team Leader Choi answered with an awkward expression.

“……Something did happen.”

“I knew it.”

“Something that happened very recently, too.”

“Oh. Ah.”

Miss Song’s misfortune was my misfortune. Just sitting there and watching her was breaking my heart.

“Whew. I hope things work out for her.”

“……”

“……”

Team Leader Choi, along with Butler Kim, who was sitting beside him, stared at me with strange expressions.

This was starting to feel weird.

“What?”

“Nothing.”

“People can be like that when they’re young.”

It was a lukewarm answer, but that was not important right now.

Crack.

“Drink! Drink until you drop dead today!”

Miss Song had opened her third bottle of soju and was going wild.

“Ha-ha-ha! This is why I really like Miss Song!”

Like a fish in water—no, like a bandit who’d found booze—Im Kkeokjeong egged her on from beside her.

“Shouldn’t we stop her?”

“Ah, Miss Song?”

“Yes.”

Team Leader Choi shrugged.

“It’s fine. It’s not like I’ve only known her for a day or two. That’s just how Miss Song gets when she drinks.”

“Even so… No, wait a second.”

I stared intently at Team Leader Choi.

I had thought he was suspicious for a while, but now I had finally caught him.

“How do you know what Miss Song is like when she drinks?”

“Because I’ve drunk with her.”

“……”

Was this bastard making fun of me? Did he think I was asking because I didn’t understand that?

“That’s not what I mean.”

“Then what do you mean?”

“I mean…”

Now that he had put it that way, I had nothing to say. When I thought about it, who was I to question the relationship between the two of them?

Just as I was rendered speechless, Team Leader Choi suddenly opened his mouth.

“You’ve heard of Ares, right?”

“Of course.”

Ares, the god of war.

The name of a god who appeared in ancient Greek and Roman mythology. These days, though, it was famous for something else.

“Who in Korea doesn’t know the Ares Guild?”

The pride and joy of Korea’s Hunters.

Hundreds of Guilds existed in Korea, but only one stood at the top: the Ares Guild. The achievements they had made from the early days of the Great Cataclysm to the present were too numerous to count.

*They’re legends. Plain and simple.*

They appeared in educational comics, educational animations, movies, novels, and all kinds of other media. They had even made it into textbooks.

The Ares Guild held a position in Korea comparable to a living King Sejong or an active General Yi Sun-sin. No, perhaps even higher.

*They’re famous all over the world, after all.*

If you asked most foreigners, *Do you know King Sejong? King-God-General Yi Sun-sin?* they would probably respond, *What the hell is this Asian guy talking about?* But the Ares Guild was different.

*Do you know Ares?*

*Oh, yeah!*

Even a tough-as-nails Texas grandpa would tap his twin pistols and understand. That was the accepted truth among scholars.

“Why are you asking about the Ares Guild?”

Team Leader Choi swallowed a mouthful of beer before answering.

“Because I used to be there.”

“Oh. I see… Huh?”

What had I just heard?

I blinked for a while before finally speaking.

“You used to belong to the Ares Guild?”

“I was a Team Leader. Though I was still pretty low-ranking.”

The Ares Guild had high standards. They selected only the best and trained them to become even better. Team Leader Choi had called himself a low-ranking member, but the fact that he had become a Team Leader there was already incredible.

Though at the moment, he just looked like a lunatic to me.

“Then why did you leave?”

Money, honor, and status.

It was the best job any Hunter—or any man—could dream of. And he had kicked it all away and left!

“Were you ostracized at work or something?”

Team Leader Choi thought about it for a moment before answering.

“That might have been the case. Miss Song was the only person who treated me normally.”

“……Then was Miss Song in the Ares Guild too?”

“She was on my team. I found out about her drinking habits during team dinners.”

I swallowed hard.

*These people are total elites.*

My gaze moved back and forth between Team Leader Choi, who was sipping his beer, and Miss Song, who was drinking straight from the bottle, before stopping on one person.

“Could it be that Butler Kim also…?”

“Me?”

Butler Kim smiled kindly and waved his hand.

“I retired a long time ago. Ha-ha-ha.”

“What?”

So he was a former Hunter.

Suddenly, I remembered the sense of incongruity I had always felt whenever I dealt with Butler Kim. I had also never once tried to assess him with my Qi Sense.

*What is this man’s real identity?*

Just as I was about to raise my Qi Sense, Im Kkeokjeong, who had been enthusiastically inhaling meat and liquor whether or not we were talking, spoke up.

“Oh, the burner went out. Miss Song, do we have another gas canister?”

“Hic. That was the last one.”

“Aw, we can’t let the momentum die. Should we just eat it?”

Im Kkeokjeong grumbled as he flipped a piece of meat that was still mostly raw. Butler Kim smiled gently at him.

“That won’t do.”

The next moment, two things happened at once.

Snap!

Butler Kim snapped his fingers.

Fwoosh!

A wave of scorching heat burst forth. Blue flames shot precisely up over the grill, heating the plate and cooking the meat in an instant before vanishing.

“This is…”

Im Kkeokjeong and I shouted at the same time.

“A mage!”

“It’s cooked incredibly well!”

“……”

“What? Taekyung, hurry up and eat.”

*Forget it, old man.*

I shook my head back and forth.

More importantly, who would have thought Butler Kim was a mage? No wonder something about him had always felt strange.

“You really fooled me.”

Butler Kim picked up a well-cooked piece of meat.

“I had no intention of fooling you. As I told you, I’m already a retired has-been.”

*Has-been, my ass.*

If Butler Kim was a has-been, half the mages still active today ought to bow their damn heads.

*At least B-rank.*

He could summon flames with a single snap of his fingers and control them precisely enough to cook the meat just right without burning or undercooking it. Judging from the circumstances, he had probably belonged to the Ares Guild as well before retiring.

If he had been active during the Great Cataclysm, too…

*……This guy’s a big shot.*

And on top of that, he was an incredibly senior one.

I asked cautiously.

“Um, which Hunter training center did you graduate from?”

“Nonsan.[^1] What about you, Mr. Taekyung?”

“Gasp. Me too. The 28th Regiment, 1st Battalion.”

“Really? What a coincidence. I was in the 28th Regiment, 1st Battalion too. Which company were you in?”

“Second Company.”

“Then it wasn’t a coincidence. I suppose it was fate. Ha-ha.”

There was no need for further discussion. I stood up and bent deeply at the waist.

“Nice to meet you, Senior.”

[^1]: Nonsan is home to Korea’s main Army recruit training center.

There is a saying in Korea about school ties, hometown ties, and blood ties.[^2] Hunters were no different.

The probability of awakening was 0.1 percent—one in a thousand. Because the odds were so slim, it was rare for someone you knew from ordinary society to awaken. The Hunter training center, which might seem like nothing special, was where a Hunter’s network began.

“You don’t have to go that far. Please, sit down.”

“You can speak comfortably with me.”

“I don’t really stand on ceremony…”

Just as Butler Kim and I were creating a warm senior-junior atmosphere, Team Leader Choi suddenly cut in.

“Butler Kim. Why don’t you do as Mr. Jin says?”

*What an ill-mannered bastard. How dare he tell such a senior what to do…*

*Hmm. He can do that.*

Come to think of it, Team Leader Choi was the bigger shot. He employed a mage from the Ares Guild as his butler.

*What kind of family does he come from?*

Was his grandfather the president and his father the prime minister?

As my curiosity continued to grow, Team Leader Choi went on.

“I think it’s time we sorted out everyone’s forms of address. You’re the face of our Guild, after all. We can’t keep calling you Butler Kim or Uncle forever, can we?”

Butler Kim considered it for a moment before answering.

“I’ll follow the Young Master’s wishes.”

Team Leader Choi nodded and swept his stern gaze over everyone present.

“Then from now on, we’ll all address Butler Kim as Guild Master. No objections, correct?”

Im Kkeokjeong and Miss Song answered.

“Man, this meat is incredible. Is it because it was grilled with magic?”

“The booze is going in. Booze! Down it goes, down it goes!”

“……”

Team Leader Choi gazed at the two of them with regret before turning his eyes toward me. I had raised one arm conspicuously.

“What does that mean?”

“I have a question.”

*At least this guy is a little better.*

Team Leader Choi spoke with an expression that seemed to say as much.

“Go ahead.”

“Wasn’t Team Leader Choi the Guild Master?”

“……”

Team Leader Choi wore an expression as if he had been betrayed, then pulled something from inside his coat and handed it to me. I took it and looked at it. It was a business card.

“I have this.”

“What does it say?”

“Choi Minwoo, Team Leader of Team 1, Peace Guild.”

“Yes. I’m the Team Leader.”

“Oh.”

“Butler Kim is the Guild Master. I’m the Team Leader. The other three are team members. Do you understand now?”

I didn’t know whether Butler Kim was a boss in name only or merely a figurehead, but I nodded anyway. If I didn’t, Team Leader Choi looked like he might cry.

“Did everyone else understand?”

At Team Leader Choi’s question, Im Kkeokjeong and Miss Song answered.

“Wow, even the liquor tastes amazing. Is it because we have magically grilled meat for an appetizer?”

“How long are you going to make me do the shoulder dance? It’s dislocated! Dislocated! Dislocated!”

“……”

*Hey, are you crying?*

[^2]: School ties, regional ties, and blood ties are traditionally regarded in Korea as major sources of social connections and influence.
## Chapter artifact 79

# Chapter 79

I woke with a dull headache and looked around. I was in an unfamiliar place—a spacious, clean hotel room.

Only then did the memories of last night gradually come back to me.

*Right. We went to a hotel for the second round and had a champagne party.*

Good God, a champagne party at a hotel.

Put that way, it made me feel like I had become the third-generation heir to some chaebol family. Though, come to think of it, Team Leader Choi might actually be one.

“Khrrr-heeeurk. Khrrp!”

“……”

That man really was a bandit.

What kind of snore sounded like someone shouting? Hyung Jinho snored pretty loudly too, but next to this guy, it was practically on mute.

*If I were the hotel manager, I would’ve kicked him out long ago—*

Knock, knock.

“Who is it?”

For a moment, I thought it was a hotel employee coming to inform us of our forced eviction. But it wasn’t. A clear, refreshing voice came from the other side of the door.

“It’s me. Song Song.”

*Wait. Who?*

“J-just a moment!”

I dashed to the door at the speed of light. Before opening it, I didn’t forget to spray on some of the perfume provided in the room and check my clothes.

Click.

My heart pounded when I looked into Miss Song’s limpid, lake-like eyes. I somehow managed to squeeze out a trembling voice.

“G-good morning. Did you sleep well?”

“No. I kept waking up because of the snoring.”

“Oh.”

Not a good start. I blamed Im Kkeokjeong, who was still snoring ferociously, and quickly changed the subject.

“But what brings you here?”

“It’s time for breakfast.”

“……Breakfast?”

Miss Song looked at me as if something were wrong.

“Yes. Why?”

*Why? Because I’m happy.*

Who would’ve thought I’d live to see the day I had breakfast alone with a woman? And not just any woman—she was exactly my type. I felt as if my eyes were growing moist.

*At last, an oasis has appeared in my desert of a life.*

I wouldn’t have minded eating combat rations for breakfast if I could eat them with her. I answered with determination.

“I’ll get ready right now.”

“Then could you wake Uncle Kkeokjeong first?”

“……Why Kkeokjeong Hyung-nim?”

“Didn’t you check the chat?”

Miss Song held out her smartphone.

The group chat we had created for the Guild last night was open on the screen.

> **Peace Guild**
>
> **Team Leader Choi**  
> Is everyone awake?
>
> **Butler Kim**  
> I’m up.
>
> **Song Song**  
> I’m up too.
>
> **Team Leader Choi**  
> What about the other two?
>
> **Song Song**  
> They’re snoring.
>
> **Team Leader Choi**  
> ……Wake them up and come to the restaurant on the first floor.

“……”

Damn it. And just when I was getting excited. That was my life for you.

Miss Song turned away, leaving me looking dejected.

“Then I’ll go down first.”

I stared longingly at her retreating back as she walked away on light, graceful steps.

“Even her back is pretty.”

“Khrrp, khrrr-heeeurk!”

“……”

*Is this guy really not a former bandit?*

* * *

I barely managed to wake Im Kkeokjeong before heading down to the first floor.

Team Leader Choi, who was sitting by the window, waved when he saw us.

“I ordered ahead. Eat before it gets cold.”

Since it was a hotel breakfast, I had expected something like an absurdly tiny serving of pasta. But what arrived on the table was a steaming bowl of haejangguk.[^1]

“Ah, now that’s Team Leader Choi!”

“You really know what you’re doing, Team Leader.”

I still had some of last night’s hangover left, but one bowl of haejangguk seemed like it would make circulating my qi unnecessary.

Team Leader Choi shook his head at our reactions.

“Miss Song ordered it. I wanted pasta.”

“Miss Song did?”

“Yes.”

His dark expression suggested that he had really wanted it.

Still, I never would’ve expected Miss Song to order hangover soup. Judging by her appearance, she looked like a pampered young lady from a wealthy family. But after what she had shown us yesterday, and now this, she had a surprisingly down-to-earth side.

Slurp.

“Ah, this is good. What are you all doing? You should eat while the broth’s still hot.”

Watching Miss Song eat her haejangguk with such gusto warmed a corner of my heart. She had such a healthy appetite.

*So this is what it means when simply looking at someone fills you up.*

In a state where I could no longer tell whether the food was going into my nose or my mouth, the meal finally came to an end. While everyone except me sagged back in their seats, bloated with food, Team Leader Choi spoke.

“Now that we’ve eaten, shall we move somewhere else?”

What? Wasn’t this supposed to be the part where we went home and rested?

“Move where?”

Im Kkeokjeong cut in while patting his stuffed belly.

“Where else? We’ve got to keep the party going from yesterday. How about makgeolli today?[^2] I know a good place.”

“Oh, I really like makgeolli too.”

[^2]: Makgeolli is a traditional Korean rice wine with a milky appearance and a mildly sweet, tangy flavor.

Butler Kim, who had been quietly listening to us, smiled and continued.

“Unfortunately, it would be better to go there for our next Guild dinner. We have something more important to take care of today.”

The Guild Master was Butler Kim, but he wasn’t the one who made the decisions.

With everyone’s eyes on him, Team Leader Choi opened his mouth.

“We’ve eaten, drunk, and rested. Now it’s time to work.”

It was the Peace Guild’s first raid.

* * *

Humanity was thrown into shock by the Great Cataclysm.

Gates began appearing without warning one day, and unidentified creatures poured out of them.

“W-what is that?”

“A monster! It’s a monster!”

If aliens with thin limbs and oversized heads had invaded, people might have been less surprised. But these creatures hadn’t come in spaceships, and they didn’t shoot guns.

“Skreeee!”

“Karuk! Krrruuuk!”

With their terrible stench and eyes gleaming with killing intent, the monsters tore humans apart like sheets of paper as they swept through cities and set them ablaze.

They were monsters that seemed as if they belonged in novels, movies, or myths.

The Minotaur was one of them……or so I had learned in history class.

“You know what a Minotaur is, right?”

Im Kkeokjeong answered proudly.

“Of course. I saw them in a Greek and Roman mythology comic when I was in elementary school. They were pretty cool—huge muscles and everything.”

“……What about you, Taekyung?”

“I’ve never even seen one.”

A Minotaur was among the stronger monsters in the B-rank category. It had been roughly five hundred light-years away from me, an eternal F-rank Hunter.

“That’s all right. You can see one now.”

“……”

*Is a Gate a zoo? Are we going there just to sightsee?*

Team Leader Choi handed me a tablet, answering as breezily as if this had nothing to do with him.

“Here.”

“What is this?”

“It’s a next-generation tablet powered by a C-rank Magic Gem. With its elegant design and outstanding performance, it’s sold exclusively to a select number of VIPs……”

“Just give me the conclusion.”

“I put some raid footage on it. Watch.”

He could’ve just said that from the start. Im Kkeokjeong and I put our heads together and watched the video stored on the tablet.

“All right, stay calm. Stay calm. Especially the tanks! Keep those shields up. If they break through, everyone here is dead. Of course, I’ll kill you before that happens.”

“Yes, sir!”

Around fifteen Hunters formed an orderly formation at the raid leader’s command. Every one of them was visibly tense.

*Tanks, melee and ranged damage dealers. There’s a mage and even a healer.*

Their teamwork seemed decent, and so did the team composition.

And then……

*So that’s a Minotaur.*

A B-rank monster, something I had only ever seen in monster encyclopedias, appeared on the screen.

“Moooooo!”

A cow’s head on a human body. Seven half-human, half-beast Minotaurs advanced toward the intruders.

No—they charged.

“Mooooooo!”

Their bellowing echoed through the cave. Rock dust shook loose and fell in little showers as the battle began.

“Ranged! Fire!”

The raid leader screamed himself hoarse. At the same time, around twenty arrows infused with mana struck the head of the lead Minotaur.

Fwish-fwish-fwish!

Focusing fire on one target instead of using a wide-area attack had been a good choice. Aiming precisely for its head had been especially effective.

No matter how strong a B-rank monster was, it couldn’t reinforce its eyeballs.

The Minotaur clawed at its own face in agony. The finishing blow came from the companions following behind it.

Crunch!

A dark iron club smashed the cow’s head apart.

And then—

Thud, thud, thud!

*Huh.*

They used the dead Minotaur’s corpse as a shield and charged straight ahead. Arrows and magic rained down, but they only shredded the corpse. The Minotaurs hiding behind it were unharmed.

*These bastards……*

They knew how to use their heads. They were at least as intelligent as goblins, while being dozens of times stronger.

Which made them even more dangerous.

“Hold!”

“Urrrgh!”

At the team leader’s shout, the veins stood out on the tanks’ arms and necks. Their shields, covered in hazy mana, blocked the iron clubs carrying tremendous force.

Wham! Wham! Wham!

A small shadow suddenly dropped from the air between them. A Hunter from the stealth category drove a blackened dagger into another Minotaur’s eye before disappearing.

“Moooo……”

B-rank monsters weren’t invincible. With the support of the other melee damage dealers, archers, and mage, two more Minotaurs fell in the blink of an eye.

But the crisis came quickly.

*They’re breaking through!*

No sooner had the thought occurred to me than the wavering tank line collapsed.

Kra-koom!

“Graaagh!”

“Healer! Healer!”

Screams and roars filled the cave. Through the clouds of dust, I could see the cow-headed monsters tearing through the formation and swinging their iron clubs.

“Moooooo!”

“Tanks, damage dealers! Ranged, don’t hold back your mana—pour it all in! Ranged, open up some distance!”

Wham-wham-wham!

“Mooooooo!”

“Healeeeer!”

The video continued for about ten minutes before cutting off. The battle hadn’t ended yet. The camera had simply been smashed by an iron club.

“Mooooooo!”

Bzzzt.

As the Minotaur’s roar rang out, the screen filled with static and faded to black and white. Im Kkeokjeong swallowed hard.

“……This is no joke.”

*Of course it isn’t, old man.*

I handed the tablet back to Team Leader Choi and asked,

“What Guild was that?”

“It was footage of the Bucheon Terminal Guild’s raid last week.”

“……”

*Whoever named that Guild had some incredible naming sense.*

Not that I had any room to talk, considering I belonged to the Peace Guild, but at least our name was better than Bucheon Terminal Guild.

“What was the result?”

“The Minotaurs were wiped out. Two Hunters died.”

People dying during raids wasn’t particularly rare. Being a Hunter meant repeatedly drawing close to death, then running away from it.

Even so, I couldn’t help feeling heavy-hearted. It was a burden the survivors would have to carry for the rest of their lives.

Just as I did now.

“I see.”

That was all I could say. I pulled out my smartphone and searched for it. Several related articles appeared.

> **A Bucheon Guild: The Sacrifice Brought on by a Reckless Raid**
>
> On the sixteenth, C-rank Hunters identified as Mr. Lee and Mr. Park died in the B-rank Gate *The Minotaur’s Labyrinth*. The Hunter Association authorities……

So the people who died had been C-rank Hunters. That made sense. A small-to-medium Guild like that couldn’t possibly have a talent pool large enough to fill a raid team of fifteen B-rank Hunters.

*Then……*

I quickly looked over the Guild members. The Qi Sense I had activated a moment earlier had already brought up their Level windows.

Ding. Ding. Ding.

> **System**
>
> **Level 75 — Choi Minwoo**
>
> **Level 80 — Kim Hwajong**
>
> **Level 64 — Song Song**

The next moment, my eyes met Im Kkeokjeong’s.

“What’s wrong?”

“It’s nothing.”

I answered as casually as I could and turned away, but my thoughts were anything but casual.

> **System**
>
> **Level 24 — Im Hyeokjun**

*This raid is dangerous.*

[^1]: Haejangguk, literally “hangover soup,” is a Korean soup traditionally eaten after drinking to help ease a hangover.

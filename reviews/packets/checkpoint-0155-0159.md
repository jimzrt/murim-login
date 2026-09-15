# Checkpoint Review — 155–159

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

# Chapters 155–159

## Plot

Jin Wikyung manages the Jin Family’s rapid postwar expansion and secretly coordinates with the Shanxi Provincial Office against roughly five hundred mounted bandits near Datong. Wipeng offers to lead useful reinforcements. Huashan sends the Three Plum Blossom Elites and reports that Mae Jonghak has disappeared, presumably to find Cheongpung.

Cheongpung continues training Jin Taekyung and Hyuk Mujin through brutal sparring. Taekyung loses dozens of times but gradually reads and imitates Cheongpung’s Huashan techniques, while Cheongpung recognizes the rough, fierce Wildness underlying Taekyung’s martial arts. Mujin reaches Level 50 and resolves to become Taekyung’s right arm or heart while earning recognition under his own name.

With three days remaining before New Year’s Day, Taekyung must defeat Cheongpung to complete *Sword Saint Training: A Secondhand Experience—2*. He spends 50 Stat Points each on Agility and Strength, causing his spear to resonate with his energy and emit a Spear Cry. Cheongpung responds with the Zaha Divine Technique, Sword Energy, and numerous Huashan arts. During the exchange, Cheongpung explains Mae Jonghak’s teaching that martial arts are empty space to be accepted and filled. Taekyung understands the lesson, completes the System Quest *Beyond the Wall*, and changes class to Peak Master. Their duel continues, and no victory over Cheongpung has yet been confirmed.

## Continuity

- Taekyung is now a Peak Master after completing *Beyond the Wall*; he spent 50 points on Agility and 50 on Strength, and his weapon resonated with his energy.
- *Sword Saint Training: A Secondhand Experience—2* still requires Taekyung to defeat Cheongpung before New Year’s Day. The duel’s final result remains unresolved.
- Cheongpung is a twenty-year-old Peak master raised and trained by Mae Jonghak. He knows numerous Huashan martial arts, can use the Zaha Divine Technique and Sword Energy, and still has no martial title.
- Cheongpung identifies Taekyung’s rough, unrefined martial arts and naturally emerging aura as Wildness. Taekyung can increasingly read and imitate Cheongpung’s forms.
- Hyuk Mujin has reached Level 50 after repeated defeats by Cheongpung and is determined to become a notable martial artist in his own right.
- Mae Jonghak taught Cheongpung that martial arts are empty space: one must accept them as they are and fill them in. This teaching triggered Taekyung’s breakthrough.
- Huashan’s Three Plum Blossom Elites—Baek Museong, Chulwoo, and Eunhyang—are traveling to meet Cheongpung after Huashan reported Mae Jonghak missing.
- Jin Wikyung is directing the Jin Family’s branch expansion and pursuing government support against the mounted-bandit alliance near Datong. Wipeng has offered to lead martial reinforcements.
- The meaning of the crane that supposedly delivered Cheongpung to Mae Jonghak, Mae’s destination, Taecho Village, Cheongpung’s future title, the other members of the Three Hands of Zhongnan, and the novel beginning with *군림……* remain unresolved.

## Translation Decisions

- Render **검성 수련 간접 체험기-2** as “Sword Saint Training: A Secondhand Experience—2,” **벽을 넘어서** as “Beyond the Wall,” and **절정 고수** as “Peak Master.”
- Render **야성** as “Wildness,” **창명** as “Spear Cry,” and **검명** as “Sword Cry.”
- Render **자하신공** as “Zaha Divine Technique,” **암향표** as “Dark Fragrance Drift,” **오행매화보** as “Five-Element Plum Blossom Steps,” **복호권** as “Crouching Tiger Fist,” and **매화오품지** as “Plum Blossom Five-Point Finger.”
- Preserve the wordplay between **무공** meaning “martial arts” and **무공** meaning “empty space” in Mae Jonghak’s teaching.
- Retain established renderings including “Huashan,” “Three Plum Blossom Elites,” “Spear Technique,” “Manoeuvre Technique,” “Peak realm,” and “Wildness.”

## Durable state

{
  "active_continuity": [
    "The City Lord's luncheon requirement concluded with Prince Shangshan's Token obtained as the Quest Reward; Zhu Bao is expected at the Jin Family's grand banquet in roughly fifteen days. Zhu Bao is ten years old, has trained in martial arts daily for three years, is an exceptionally skilled young swordsman personally named Zhu Bao, and admires Jin Taekyung.",
    "Taekyung accepted and completed Beyond the Wall after spending 50 points on Agility and 50 on Strength; the System changed his class to Peak Master, and his weapon resonated with his energy.",
    "Hong Jin and Li Feng are pursuing the Shaanxi–Shanxi trade project through Huashan, with Li Feng acting as intermediary and the Seongun Escort Bureau proposed as the base.",
    "Cheongpung is twenty years old, a Peak master raised by Mae Jonghak, knows numerous Huashan martial arts, can use the Zaha Divine Technique and Sword Energy, has no martial title, and teaches Taekyung and Mujin using Mae's training method.",
    "Mae Jonghak remained in deep seclusion at a hidden Huashan residence for at least ten years; Cheongpung came to Huashan at about age three or four rather than being born there.",
    "Huashan was sealed after Mae Jonghak entered the sleeping Sect Leader's quarters, left a dagger and handwritten letter, and disappeared; the search for his residence remains ongoing.",
    "Baek Museong is Huashan's Lone Crane and the first of the Three Plum Blossom Elites; Chulwoo and Eunhyang are his junior disciples and fellow Elites, and all three are traveling to meet Cheongpung again.",
    "Li Feng left Huashan after becoming discouraged by Cheongpung's extraordinary talent, not because of his defeat by Gong Ilhyuk; the other two members of the Three Hands of Zhongnan remain unknown.",
    "Hong Jin is a eunuch who formerly served the late Emperor, was ordered to assist Prince Shangshan, has served him since infancy, and is the power behind the Shanxi Provincial Office.",
    "Jin Mukyung lost to Cheongpung four days before the luncheon, then secluded himself to train; the defeat clarified his ambition and strengthened his Sword Energy.",
    "Jin Wikyung is the thirty-five-year-old Lesser Family Head and future Family Head, directing the Jin Family's expansion and branch stabilization while aiming to establish it as a great family.",
    "Taekyung previously failed to force open the Conception and Governor Vessels, suffering slight acupoint damage and a one-point reduction in Sinews and Meridians.",
    "Taekyung has a private training ground in a rebuilt pavilion at the Jin Family; Hyuk Mujin accepted his invitation to train with him and Cheongpung.",
    "Wall Lizard Technique training is complete: Taekyung and Mujin climbed the cliff ten times, Taekyung acquired the technique, gained 10 Stat Points and 10 Skill Points, and upgraded Beginner Trainee to Intermediate Trainee.",
    "Wipeng offered to personally lead useful martial artists against approximately five hundred mounted bandits gathering near Datong; Huashan sent the Three Plum Blossom Elites and reported Mae Jonghak missing.",
    "Taekyung's second Cheongpung-training Quest requires him to defeat Cheongpung at least once before New Year's Day.",
    "Cheongpung had only ever sparred with Mae Jonghak before leaving Huashan and is adjusting with difficulty to fighting people outside his grandfather's instruction; he considers Taekyung and Jin Mukyung the strongest people he has met since leaving Huashan.",
    "Cheongpung identifies Taekyung's rough, unrefined martial arts and naturally emerging aura as Wildness; Taekyung can increasingly read and imitate Cheongpung's forms during sparring.",
    "Hyuk Mujin has resolved to become strong enough to be remembered as Jin Taekyung's right arm or heart and by the name Hyuk Mujin; he is now Level 50 after recent training and sparring.",
    "Cheongpung's teaching that martial arts are empty space—something to accept and fill—triggered Taekyung's breakthrough into the Peak realm, while their duel's final outcome remains unsettled."
  ],
  "continuity_sources": [
    159
  ],
  "open_questions": [
    "What did Mae Jonghak mean by saying a crane delivered Cheongpung to him, and did he actually go to the Jin Family after breaking seclusion to find Cheongpung?",
    "What are the names and individual identities of the other two members of the Three Hands of Zhongnan?",
    "What is the full title of the wuxia novel beginning with 군림…… that Taekyung read through volume thirty-four?",
    "Was the Emperor's reported suspicion of his younger brother the reason Prince Shangshan was sent to Shanxi, and what danger does the imperial succession pose?",
    "What martial title will Cheongpung eventually acquire?",
    "What circumstances led Hong Jin to become a eunuch and come to the frontier in something like exile?",
    "What is Taecho Village, and why does Taekyung say “again” after landing?",
    "Can Taekyung defeat Cheongpung before New Year's Day?"
  ],
  "safe_through": 159,
  "temporary_decisions": [
    "Render 전하 as “His Highness” as the formal royal address and 왕 as “king” when used literally; render 초일류 as “advanced First Rate,” 군문 as “military,” 풍운검군 as “Wind-and-Cloud Sword Lord,” and 오촌 당숙 as “father's cousin.”",
    "Render 태사부 as “Grandmaster,” 사숙 as “Martial Uncle,” 자하신공 as “Zaha Divine Technique,” 근위대 as “royal guard,” and 근위대 갑옷 세트 as “Royal Guard Armor Set.”",
    "Render 비무행 as “dueling tour,” 청강검 as “blue-steel sword,” 광염 as “light-flames,” 검명 as “Sword Cry,” and 창명 as “Spear Cry.”",
    "Render 검신 as “Sword God,” 검성 as “Sword Saint,” 임독양맥 as “Conception and Governor Vessels,” 기해 as “qi sea,” 근맥 as “Sinews and Meridians,” 사해오호 as “Four Seas and Five Lakes,” and 환골탈태 as “Bone Transformation.”",
    "Render 연무장 as “training ground,” 수련동 as “training hall,” 청석 as “bluestone,” 십팔반병기 as “eighteen traditional weapons,” 찍고 땡 as “touch-and-go method,” 천응 as “Heavenly Eagle,” 강시 as “jiangshi,” 태초 마을 as “Taecho Village,” 벽호공 as “Wall Lizard Technique,” and 낙안봉 as “Falling Goose Peak.”",
    "Render 황하방 as “Yellow River Gang,” 소공문 as “Sogong Sect,” 남부상회 as “Southern Merchant Guild,” 내당주 as “Inner Hall Master,” 내외당 as “Inner and Outer Halls,” and 세가 as “great family.”",
    "Render 암향표 as “Dark Fragrance Drift,” 복호권 as “Crouching Tiger Fist,” 천근추 as “Thousand-Catty Drop,” 야성 as “Wildness,” 오행매화보 as “Five-Element Plum Blossom Steps,” 공수납백인 as “Empty-Hand Seizes the Blade,” 매화오품지 as “Plum Blossom Five-Point Finger,” 벽을 넘어서 as “Beyond the Wall,” and 절정 고수 as “Peak Master.”",
    "Retain Taekyung's instant-noodle flavor joke with “mild Neoguri,” “Jin Ramen spicy flavor,” and “Puramyeon spicy flavor”; render 천근거력 as “the force to move a thousand catties,” and preserve the 무공/무공 wordplay as “martial arts” and “empty space.”"
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 155

# Chapter 155

A silent room. Six or seven scholars were frantically immersed in their work.

With haggard faces, they processed the bamboo slips piled up like mountains one by one while reporting various matters to the master of the office.

“There’s been a dispute between the Yellow River Gang and the Sogong Sect. They’ve asked our family to mediate, but…”

“Tell them we’ll arrange a place on New Year’s Day and discuss it then. Inform the Inner Hall Master in advance.”

“What should we do about the matter concerning the Five Gates of Shanxi?”

“Ah, is this related to the third one?”

“Yes. The heads of the Five Gates of Shanxi are waiting to convey their apologies.”

“Send them back. If they were truly sorry, the heads themselves should have come in person instead of sending their hands and feet. Inform the Inner Hall Master of that, too.”

“Next, there’s a matter from the Southern Merchant Guild…”

Even while receiving reports, the master of the office, Jin Wikyung, never looked up from the bamboo slips.

But at the next report, even he had no choice but to raise his head.

“Lesser Family Head, the mounted bandits from the northern plateau are showing suspicious movements near Datong.”

“Mounted bandits? Is this information from the Lower District Sect?”

“Yes. If we leave them alone, they’ll launch a large-scale raid against the common people.”

“How large is their force?”

“Five mounted-bandit groups have formed an alliance. Around five hundred men are gradually gathering.”

“Mounted bandits, huh? They’ve been a constant nuisance.”

Jin Wikyung rubbed the space between his brows with a tired expression.

It was true that the Jin Family of Taiyuan possessed formidable power, but it still lacked the strength to cover all of Shanxi Province.

That was also why the mounted bandits kept watching for an opportunity despite knowing that the Red Wind Band had been annihilated.

“Should we draft some martial artists?”

At the scholar’s question, Jin Wikyung immediately shook his head.

“No.”

“We have more martial artists joining our family than we can count. We have enough manpower.”

“We’ve already shed too much blood for that. Besides, those we accepted this time still lack experience. Even if we recruit several hundred, several hundred will die.”

The Mount Heng Sword Sect.

One of the legs supporting the tripod of Shanxi Province had broken, and the water inside was beginning to spill over.

They had to devise a countermeasure before they were scalded by the boiling water.

After thinking for a moment, Jin Wikyung spoke.

“For the time being, focus on establishing and stabilizing branches in each prefecture and county. That is our top priority.”

“Lesser Family Head!”

The scholar cried out in surprise. The others, who had been focused on their own tasks, also raised their heads.

Hundreds of mounted bandits were supposedly invading, and yet establishing branches was the top priority. Did that mean they did not care whether the common people died?

As disappointment spread across the scholars’ faces, Jin Wikyung continued.

“Instead, request assistance from the Five Gates of Shanxi. Two hundred should be about right… What do you think?”

“That won’t come close to being enough.”

There was no one in this office, at least, who could speak so bluntly to the Lesser Family Head of the Jin Family of Taiyuan.

Jin Wikyung grinned as he looked at Wipeng, who had just entered through the door.

“Is that so? I thought it would be enough.”

“What sort of people are the Five Gates of Shanxi now? They’re obsessed with clawing at one another for scraps. They’ll hide their carefully trained elites inside their walls and send us a force packed with clueless Second Rate and Third Rate martial artists.”

“That sounds plausible.”

“It’s not just plausible. That’s what will happen nine times out of ten. The mounted bandits will see all those peach-fuzzed little punks and be so delighted their mouths will split open.”

“Haha. So we have to step in?”

“What else can we do? If you attach some useful men to the force, I’ll go there myself. Then the Five Gates of Shanxi won’t be able to pull any sneaky tricks.”

“Exactly. Isn’t the Ghost Sword more frightening than a ghost?”

At Jin Wikyung’s teasing tone, Wipeng shook his head from side to side.

“Enough of that. Tell me what you have in mind.”

“What do you mean?”

“You already have a plan, don’t you?”

“What plan? I thought your idea was pretty good.”

“Good grief. Since when have you listened to my words so attentively?”

“Every word that comes out of your mouth is a golden rule to me.”

Wipeng let out a deep sigh and turned toward the scholar standing blankly nearby.

“What do you think?”

“Y-yes?”

A thin frame and a pale, washed-out face. He was the very picture of a pale-faced scholar who did nothing but pore over books in his room.

Startled by Wipeng’s sudden question, he stammered out an answer.

“I-I think it’s insufficient.”

“Is that all?”

“We should draft more men…”

Watching him, Jin Wikyung cut in with a laugh.

“That’s enough. And you.”

The scholar, already cowed by Wipeng’s sharp aura, flinched.

“Yes.”

“Send word to the Five Gates of Shanxi and the Shanxi Provincial Office. Tell them mounted bandits are swarming around Datong and that we request their assistance.”

“The Shanxi Provincial Office?”

“The people are in danger. The government ought to step forward. Ah, casually give the Five Gates of Shanxi a hint about it, too.”

“Judging by the government’s passive attitude over the past several years, the chances of that succeeding are slim.”

“Then make it succeed.”

Jin Wikyung’s face lost its smile as he added one more thing.

“Isn’t that your job?”

“Ah.”

The scholar’s mind snapped awake. He was exhausted from staying up several nights, but he had been thinking far too simply.

Request help from Shanxi Province? The countermeasure proposed by Wipeng, a man who was a martial artist down to his bones, was much more plausible.

“I apologize.”

“You’re still inexperienced, so I understand. But what our family needs isn’t scholars. We need wise men who can offer the best possible measures for the sake of our family. I hope you’ll remember that.”

There was nothing the scholar could say. Seeing that not only the man before him but everyone else had reddened faces, Jin Wikyung spoke again.

“You’re all tired, so go in and rest for today.”

No one would refuse an order to rest. Especially not those who had been surviving on brief naps with bamboo slips for pillows for three straight days.

Once the scholars dragged their exhausted bodies out, Wipeng pulled over an empty chair.

“Are they newly recruited?”

“Being on my own was too much. Still, they’re better than nothing.”

“I’m not sure. They all seem rather bland.”

“How many of them studied in order to join our family? It’s only natural.”

Jin Wikyung stretched his arms high. The loud cracking of bones echoed through the room.

“It’s only been a few days. We need to separate the jade from the stones and send away those who need to go.”

“Is that why you didn’t inform them of the secret agreement with the Shanxi Provincial Office?”

“Why is a secret agreement called a secret agreement? The fewer people who know about it, the better.”

In truth, securing the assistance of the Shanxi Provincial Office was not particularly difficult. Hadn’t he and Deputy Military Commissioner Hong Jin already exchanged plenty through their conversation five days earlier?

“Our family hasn’t fully established itself yet. It would be troublesome if rumors spread that we had entered into a secret agreement with the government under these circumstances.”

“That’s true. Even more so if they weren’t rumors but facts.”

The conversation Jin Wikyung had exchanged with Hong Jin had included several topics that the small and medium-sized sects of Shanxi Province—and especially the Five Gates of Shanxi—would not welcome.

If the Seongun Escort Bureau heard what Jin Wikyung and Hong Jin had discussed, they might collapse frothing at the mouth.

“So, are the other preparations going well?”

“Yes. I’ve completed the personnel changes as you ordered. The heads of the Inner and Outer Halls have been left in place, and we’ve established three new squads…”

The report flowing from Wipeng’s mouth concerned the first matter Jin Wikyung had handled immediately after the war ended.

The Jin Family of Taiyuan was like a rising sun. To the hot-blooded young people of Shanxi Province, it was the finest choice available.

To embrace the endless stream of people coming to them, the family had to widen its arms even further.

“…That’s how I handled it, but since our numbers are expected to continue growing, we’ll likely need to reorganize again later.”

“That’s what we should hope for.”

Jin Wikyung tried to appear calm as he listened to Wipeng’s report.

The Jin Family of Taiyuan had been slowly but steadily declining since the Great Faction War. Yet the Jin Family of Taiyuan now was rapidly recovering its former glory.

*No. Perhaps it will become even stronger than it was before the Great Faction War.*

If that happened…

That would be when they truly earned the right to be called a great family.

They would break free of their status as a frontier martial family and stand shoulder to shoulder with the great powers of the realm.

*A great family. A great family, huh.*

Just thinking about it made his heart race.

Just as every martial artist dreamed of becoming the Martial God, Jin Wikyung had long dreamed of raising his family onto the foundation of a great family.

*New Year’s Day is almost here.*

On that day, before all the sects of Shanxi Murim, the Jin Family of Taiyuan would be recognized as the undisputed hegemon of Shanxi Province.

Jin Wikyung had no doubt that the first day of the coming year would become the Jin Family of Taiyuan’s first stepping-stone—and the harbinger of its rise—as a great family.

And it was at the very moment he secretly clenched his fists that—

“Um, may I come in?”

“Hm? Of course.”

The owner of the voice that appeared next was the scholar who had just left.

“What is it? Did you leave something behind?”

“It’s not that…”

Under the puzzled gazes of Jin Wikyung and Wipeng, the scholar carefully continued.

“There’s some news I failed to report.”

“You’re a stubborn one. You’ve been working hard for days without even getting proper sleep. Don’t worry about it. Go in and get some rest.”

“No. I should have told you earlier, but I forgot…”

“Now, now, it’s all right. I said go rest.”

Wipeng added his voice.

“My lord is right. You aren’t a jiangshi. You need to get enough rest so you can have the strength to work again tomorrow…”

“Huashan has sent the Three Plum Blossom Elites.”

Jin Wikyung and Wipeng shot to their feet at the same time.

“What!”

“What did you say?”

Who were the Three Plum Blossom Elites?

They were Plum Blossom Swordsmen, known as Huashan’s finest. Among them were three outstanding prodigies who stood above the rest.

In particular, Baek Museong, Huashan’s Lone Crane, was a major figure regarded as the future Sect Leader who would carry Huashan’s future on his shoulders.

Having heard that, there was no way the two men’s eyes would not bulge.

“Is that really true?”

“Yes. I meant to tell you at the end, but I forgot. And there’s one more thing.”

“One more?”

“Another? Tell us quickly!”

The visit of the Three Plum Blossom Elites was shocking enough, and now he was saying there was something else.

The scholar continued with a frown.

“They say the Grandmaster has disappeared. He seems to have gone to our family, so they asked us to send word if we happen to meet him… But who is the Grandmaster?”

The scholar was still unfamiliar with the realities of Murim and wondered what this was all about. Jin Wikyung and Wipeng, however, stood with their mouths hanging open.

“If Huashan’s Grandmaster is…”

“Th-the, th-the…”

Sword Saint Mae Jonghak.

The two men could not bring themselves to say the name aloud. They merely moved their lips and swallowed hard.

Huashan still wanted to keep the Sword Saint’s whereabouts secret. At times like this, it was best to keep one’s mouth shut.

“Th-the… What did you say?”

“Th-that thing. You know, that sort of thing.”

“Yes?”

“You can leave now. Erase everything that just happened from your mind. Understood?”

The scholar bowed with a bewildered expression and left. Only then did the words they had been holding back burst out.

“The Sword Saint is coming!”

“Shh! Lower your voice. We don’t even know for certain yet.”

Despite his words, Wipeng’s face had also flushed bright red. To a swordsman like him, Sword Saint Mae Jonghak was greater than even the Jade Emperor.

To think they might be able to meet such a person in the flesh! No, perhaps he might even receive instruction from him.

“B-but why would the Sword Saint come to our family?”

“What else could it be?”

“Ah.”

He had been so excited that he had momentarily forgotten who was currently staying at the Jin Family of Taiyuan.

“That Sword Saint broke his seclusion to look for his beloved disciple.”

“It’s only a guess for now, but that’s highly likely. I hear he raised him like his own grandson. How deep must his affection be?”

Jin Wikyung grinned broadly.

Whatever the reason, the Sword Saint’s visit was something to welcome with open arms—not only as a martial artist, but also as the Lesser Family Head of the Jin Family of Taiyuan.

“You said his name was Cheongpung, right? Where is he now? I seem to remember hearing a while ago that he was training the youngest in the Wall Lizard Technique.”

“The Wall Lizard Technique training ended two days ago, and now he’s…”

“And now?”

“He’s beating the crap out of the Third Young Master.”

“What!”
## Chapter artifact 156

# Chapter 156

*Thud!*

Timing, speed, strength. And finally, the point of impact.

That blow had landed perfectly. There was just one unfortunate fact: that perfect blow had buried itself in my solar plexus.

“Guh!”

In an instant, excruciating pain robbed me of my breath. Through my blurred vision, I saw Cheongpung raising his fist.

“W-wait!”

“Why?”

“You hit me in the solar plexus. My solar plexus.”

“Grandfather said that once a fight begins, you have to beat your opponent into a pulp.”

“This is a spar!”

“Grandfather also said that you have to treat spars like real battles if you want to survive in the harsh martial world.”

I had nothing to say. It wasn’t some old man who ran the neighborhood supermarket teaching him this. It was the Sword Saint. What could I possibly say? And it wasn’t as if the advice to treat everything like a real battle was wrong.

Once I gave up on everything, I felt at peace.

“…Fine, fuck it. Hit me.”

“Yes!”

*Smack!*

> **System**
>
> Powerful hit! **Toughness** increased by 2.

My vision flashed white, and the strength drained from my legs. Against my will, my body slowly toppled backward.

*I can’t crack the back of my head.*

Fortunately, what I feared didn’t happen. Hyuk Mujin had already passed out and fallen over, and his butt cushioned the back of my head.

*It’s filthy. Filthy, but soft. Filthy, but firm.*

This bastard had an apple-shaped ass, minimum.

I almost wondered if he had been doing Pilates or yoga between shifts at the Gatekeeper Pavilion.

Using Hyuk Mujin’s butt as a pillow, I looked up at the sky. Maybe it was because I was seeing it after getting beaten senseless, but the sky looked yellow.

*Check Quest.*

*Ding.*

> **System**
>
> **Quest**
>
> **Sword Saint Training: A Secondhand Experience—2**
>
> Cheongpung, exhilarated by your outstanding results, has presented a second training challenge.
>
> Knock him down at least once before New Year’s Day!
>
> **Grade:** Peak
>
> **Restriction:** Those who have completed the prerequisite Quest
>
> **Mission:** Win the duel against Cheongpung (Incomplete)
>
> **Reward:** ???
>
> **Cheongpung** is very pleased.
>
> **Failure:** ???
>
> **Cheongpung** is very saddened.

The thought that I would win at least once had vanished the moment the spar began.

My duel with Cheongpung was even more one-sided than my duel with Jin Mukyung, and that much more brutal.

*How does he know this many martial arts?*

I had seen more than a dozen different martial arts over the past two days alone.

Just when I thought I might be getting used to the Taeeul Miri Palm, he would bring out the Falling Flower Chasing Shadow Palm. Just as that technique began to look familiar, the Crouching Tiger Fist would come flying out.

On top of that, countless supreme techniques that had helped turn Huashan into one of the Nine Sects and One Gang had seeped into every part of Cheongpung’s body.

*The roots of his martial arts are Huashan. The one who taught him was the Sword Saint.*

Didn’t this guy need a balance patch?

“Heh heh. Hehehehe.”

As I let out nothing but hollow laughter, Cheongpung approached and asked,

“Benefactor, are you all right?”

“If you’re going to ask that, then go easy on me.”

“But then it wouldn’t be training. Doing something half-heartedly is worse than not doing it at all…”

“Your grandfather said that, didn’t he?”

“Gasp! How did you know? Have you ever lived on Lotus Peak?”

“...No.”

I was born and raised in Gyeonggi Province, you punk.

I let out a deep sigh and pulled myself upright. Hyuk Mujin, who had been unconscious for quite some time, still hadn’t moved an inch.

“What did you do to him? Isn’t he going to die at this rate?”

“I did try to control my strength, but I guess I was a little inexperienced.”

“Control your strength?”

“Yes. In all the years I’ve been alive, I’ve only ever had one sparring partner.”

Cheongpung had spent his entire life sparring with a Supreme Peak master known as the Sword Saint, as casually as if they were sharing meals. Naturally, he would have learned only how to fight at full strength.

He continued with sad eyes.

“Now that I’ve come out into the world, it’s much harder than I expected. Because I’m so clumsy, I hurt the Senior from the Zhongnan Sect, and now even Warrior Hyuk...”

This backwoodsman’s adjustment to the martial world was proving rather difficult.

I scratched the back of my head and said,

“Don’t worry about that. The Zhongnan guy was someone who deserved to get hit, and Mujin won’t take it to heart. It’s training, after all.”

“Really?”

“Yes. You’re getting better and better, so don’t worry too much.”

Cheongpung smiled brightly, as though none of that had ever happened.

“Benefactor, did you know?”

“How would I know?”

“Of all the people I’ve met in Murim, I like you best, Benefactor!”

I drew up my internal energy.

“Back off right now. If you lay even one fingertip on me, I’ll bite my tongue and die.”

“Because even if I hit you with all my strength, you always get back up!”

“Oh.”

“And you feel the best when I hit you!”

Listen to the way he said that.

Relief and irritation surged through me at the same time. I had wondered why he seemed to be beating me so enthusiastically. Without realizing it, I had become a sandbag for testing punching power.

*No wonder my Toughness kept shooting up.*

I hadn’t invested much in Toughness, the last stat I had acquired. Even so, it had caught up with the combat stats I had poured points into.

*Should I be grateful for this?*

It had only been a few days of short-term training, but I was certainly seeing substantial results.

I had gained a considerable boost in stats while scaling the cliff and learning the Wall Lizard Technique. Now I was experiencing Huashan martial arts firsthand while raising my Toughness like crazy.

“Please continue to take good care of me. I’m learning a lot by hitting you, Benefactor.”

“...Ah. Yes.”

I wanted to smack Cheongpung on the back of the head as he bowed politely, but I held myself back. I knew there was no real malice behind anything he said.

Part of me also felt relieved.

*If this guy had been even stronger, I really would’ve been screwed.*

Cheongpung was a mountain I absolutely had to climb.

If he had been holding back while fighting me, I would have been more offended than anything else.

Consideration from someone you wanted to defeat never felt like consideration.

I spoke in a solemn voice.

“Let me ask one thing of you.”

“Anything, Benefactor.”

“When you fight me, give it everything you’ve got.”

“Everything I’ve got?”

“Yes. Your best. That’s all I need.”

Cheongpung stared at me for a moment, then nodded.

“Understood.”

“Thank you—”

*Ssssss.*

Before I could finish speaking, the heat of the Zaha Divine Technique blazed up from Cheongpung’s entire body like a wildfire, burning through the cold winter air.

His eyes, already tinged with a faint violet hue, fixed on me.

“I’ll really give it my best, Benefactor.”

“...Oh. So this is your best?”

Damn it. I’d forgotten about that.

At my vacant stare, Cheongpung smacked his forehead.

“Oh, right. I’m sorry. I’m a little slow on the uptake.”

“It’s all right. As long as you understood me eventually, that’s—”

*Shing.*

This time, Sword Energy rose in a long, surging blade from the sword in Cheongpung’s hand.

“I’m ready to give it my best now.”

“Ah...”

“Benefactor, I’ll really do my best! No matter how hard I fight you, you’re bound to get back up anyway!”

I wasn’t so sure. I had a feeling I wouldn’t be getting back up this time.

I silently stared at the undulating energy of the Zaha Divine Technique and the blazing Sword Energy before finally managing to speak.

“L-let’s put away the Sword Energy.”

Let me live too, you bastard.

* * *

*Whoosh!*

The spearhead tore through the air. It was a fast, sharp attack. Cheongpung dodged by rolling his shoulder, but the second and third attacks followed like a storm.

“Hah!”

With a shout, spearheads rained down. The martial art itself was simple and heavy.

But the movements of the man wielding the spear were light and fast. Hidden between his efficient movements were unpredictable attacks.

*Swish! Swish-swish-swish!*

A smile formed at the corner of Cheongpung’s mouth as he narrowly dodged the spearheads.

*Wow, this is fun. Was Benefactor always this good?*

He beamed as he watched the young man pressing him relentlessly.

Jin Taekyung. They had not known each other for long, but he was the Benefactor who had helped Cheongpung in so many ways.

When Jin Taekyung had given him every last candied hawthorn skewer[^1] the first time they met, Cheongpung had nearly cried.

[^1]: Traditional fruit skewers coated in hardened sugar.

*He’s a good person. He gave me something this precious.*

Grandfather had been wrong. He had said Murim was overflowing with frightening people who were vicious and utterly ruthless, but everyone Cheongpung had met was gentle and kind-hearted.

Even the Senior from the Zhongnan Sect, whom Cheongpung had injured through his own mistake not long ago, wasn’t unpleasant at all.

*He’s my Senior, so he can’t be a bad person.*

As far as Cheongpung knew, Seniors and Juniors were not connected by an ordinary relationship. They shared a close bond tied by something thicker than blood.

And Grandfather had always told him to protect the weak.

The Senior from the Zhongnan Sect had been weak in martial arts. Cheongpung had felt terrible for hurting him.

*But...*

It was nice that there was no reason to feel bad about Jin Mukyung and Jin Taekyung.

They were the strongest people Cheongpung had met since leaving Huashan. Even now, as he exchanged blows with Jin Taekyung, he was enjoying himself immensely.

*Whoosh!*

Cheongpung easily dodged the spear thrusting toward his shoulder, then burst out laughing despite himself.

“Hehe.”

“You laughing?”

“Because I’m having fun.”

“You really need to watch what you say. That’s dangerous.”

*Swish-swish-swish!*

Six killing attacks and twice as many feints came raining down from every direction. But Cheongpung was no longer where he had been.

Jin Taekyung pierced the faint afterimage and shouted with the expression of someone who had seen a ghost.

“What the hell was that?”

“Dark Fragrance Drift. Hehe.”

“That’s cheating!”

“Would you like me to teach you?”

“Great Hero Cheongpung, as for me, I’ve been barely scraping by in this harsh world using the lowly Jin Family’s Manoeuvre Technique...”

“Oh, right. Grandfather told me not to teach it to anyone.”

“This little bastard?”

*Whoosh!*

Jin Taekyung changed direction and thrust low.

Just before the fiercely spinning spearhead pierced his instep, Cheongpung raised his foot with dazzling speed and pressed the spearhead down toward the ground instead.

*Craaaack!*

“Wow, that was a little dangerous.”

But Jin Taekyung wasn’t listening to him. With a short shout, he lifted the spear shaft beneath Cheongpung’s foot.

“Hah!”

“Benefactor, that won’t work. This is the Thousand-Catty Drop[^2]—”

[^2]: A catty is a traditional East Asian unit of weight; the technique’s name evokes immense downward force.

*Whoosh!*

The next moment, Cheongpung felt himself floating.

Jin Taekyung’s tremendous strength swung the spear shaft skyward. Cheongpung’s feet were thrown clear, leaving him stepping on empty air.

He lost his balance for an instant and hurriedly drew up his internal energy.

*Boom! Boom! Swish-swish!*

The force of the Falling Flower Chasing Shadow Palm struck the air and shoved his body backward. A split second later, Jin Taekyung’s spear stabbed and slashed through the space where Cheongpung had been.

*Wow.*

Jin Taekyung’s strength was beyond Cheongpung’s imagination, even if it was still inferior to his grandfather’s.

No. It wasn’t merely his strength.

He possessed incredible stamina, enough to fall countless times and keep getting back up; agility that shouldn’t have been possible with that physique; and monstrous Toughness.

*Even the way he uses martial arts is different from everyone else.*

Cheongpung was a Peak master. He had been raised by the Sword Saint and grown up watching the Sword Saint’s martial arts.

He could gauge an opponent’s level from a single move and half a form of the martial arts they displayed.

*Young Hero Jin Mukyung was sharp.*

Jin Mukyung, whom he had dueled several days ago, possessed an aura that seemed capable of cutting anyone who touched it, and his martial arts were the same.

But despite sharing the same blood, Jin Taekyung’s disposition and martial arts were the exact opposite of his brother’s.

*What should I call this?*

Though his martial arts were rough, still unrefined, and otherwise unremarkable, his movements created a strange tension. His aura seeped out naturally…

“Whew. You coming? If not, I’ll go to you.”

At the sight of the man striding toward him, Cheongpung finally thought of a word.

*Wildness.*

A beast hell-bent on biting through its prey’s throat.

Jin Taekyung’s claws had not yet been honed, and that was precisely why they seemed even larger.
## Chapter artifact 157

# Chapter 157

Since ancient times, people had said that the masters of famous mountains were spirit creatures. Huashan, one of the Central Plains’ Five Great Mountains, was no exception.

Before human feet ever touched it, tigers had ruled over its lofty, sprawling forests.

These spirit creatures possessed the majesty of kings and the ferocity of beasts. When their territory was invaded, they grew furious and soon began attacking the unwelcome trespassers who had entered without permission.

“Wow, and then?”

“When the loss of human life became severe, the Huashan Sect had no choice but to step in. That was how the Crouching Tiger Fist was born.”

*A fist technique that subdues tigers. The Crouching Tiger Fist.*

Cheongpung remembered clearly what his grandfather had told him when he learned the Crouching Tiger Fist long ago.

“Pung, the Crouching Tiger Fist is a powerful martial art capable of subduing the king of the mountains. If you master this one technique, no one your age will be able to stand against you. Do you understand?”

“Yes!”

As a child, Cheongpung had believed his grandfather’s words without question.

But now, ten years later—

*Whack!*

“Ow, that hurt.”

“…Huh?”

For the first time, he realized that even his grandfather could be wrong.

* * *

It was the third day since I had begun sparring with Cheongpung. During my forty-fifth duel, I witnessed him stumble over his words for the first time.

“B-Benefactor, are you all right?”

“I know. That was the Crouching Tiger Fist, right?”

I had watched it with my own eyes, and I had even experienced it firsthand by getting hit.

Getting knocked out after taking the Crouching Tiger Fist to the solar plexus had happened yesterday.

I had committed the way Cheongpung moved when he used the Crouching Tiger Fist to memory—the footwork he used, the position of his shoulders, and even the sequence of forms that followed.

And yet I had still allowed myself to be hit.

There was no doubt about it. Cheongpung was one step ahead of me.

“What was the name of that form just now?”

At my question, Cheongpung answered with a dazed expression.

“One Fist Subdues the Tiger.”

A single fist that knocked down a tiger? It certainly possessed enough destructive power to justify the name. If I hadn’t been getting so much better at taking hits with every duel, I would have dropped to my knees just like yesterday.

*Should I take comfort in the fact that I’m doing much better than yesterday?*

My ability to take a hit wasn’t the only thing that had improved. By experiencing Cheongpung’s martial arts with my own body, I was gradually getting used to them.

“All right, let’s go again.”

But Cheongpung didn’t seem to have any intention of doing that.

“How did you dodge it?”

“Huh?”

“I was aiming precisely around your Fengwei acupoint…”

The Fengwei acupoint was located around the ribs. I had twisted my body in an attempt to dodge, only to take the blow squarely in the middle of my abdomen.

Since I had avoided his intended target, could this technically count as dodging? I shrugged.

“I just struggled to avoid getting hit even once. I got hit in the end, though.”

“Did you see the sequence of forms?”

After being beaten up for several days, I could make out the forms vaguely. Where and how an attack would come from. How the next form would follow.

*The problem is that I’m still clumsy at it.*

I rubbed my aching abdomen and answered.

“After taking this many hits, I should be able to read at least that much. Every time you hit me, I kept my eyes wide open and watched.”

Wasn’t keeping your eyes open even while getting hit and figuring out your opponent’s sequence of forms the most basic thing?

“Hmm, that’s strange. I’ve only used the Crouching Tiger Fist a few times.”

“That’s why it took me a little longer to figure out than the others.”

“The others?”

“Yes. The Plum Blossom Fist was pretty easy. Maybe because you used it the most during our duels, but I could more or less figure it out.”

Cheongpung clapped with an exclamation of admiration.

“Wow, can you show me?”

“It’s nothing difficult.”

I performed a poor imitation of the Plum Blossom Fist. My footwork and movements were both terribly awkward, but every form came from the Plum Blossom Fist Cheongpung had used in our duels.

*This much is easy.*

At some point after I began learning martial arts, I realized something.

A technique required an understanding of martial arts and the internal-energy control to match it. But copying the form itself was easy.

*I moved like this here, didn’t I? Probably?*

From the first form to the seventh. I occasionally stumbled, but I managed to perform them as naturally as possible without much difficulty. Then I turned my head.

“That’s about it for now… Young Hero Cheongpung?”

“Ah, yes, Benefactor.”

“Is something wrong? Why do you look like that?”

“No, it’s just…”

Cheongpung stared at me with an oddly complicated expression before hesitantly opening his mouth.

“I suddenly remembered something my grandfather once said.”

“The Sword Saint old man—I mean, your grandfather?”

“Yes. He used to call me a thief.”

“It’s all right. When I was young, I secretly took a thousand won from my mother’s wallet and got beaten half to death.”

“That’s not what I mean…”

Cheongpung let out a deep sigh.

“He always said that while teaching me martial arts. He called me a thief who stole martial arts.”

“Oh.”

That was a compliment, right? To think a talent freak like Cheongpung was praising me.

As I stood there dumbfounded, Cheongpung said,

“Benefactor, you’re definitely a genius of martial arts.”

“A genius? Me?”

“Yes.”

*A genius, my ass…*

No, wait. He was right.

When I thought about it, I had mastered the Jin Family’s Manoeuvre Technique and spear technique—both First Rate martial arts—in barely two or three months.

Of course, the System had carried me through all of it.

“It’s just a shortcut. I’m pretty good at using my body, that’s all. My eyes are good, too. Heh heh.”

“My grandfather used to say that martial arts are seventy percent eyes and thirty percent feet.”

“I think he was right about that, but either way, I’m not a genius.”

“Think about it carefully. I’m sure something similar happened before.”

Was that true?

I suddenly remembered my childhood. I had always been good at sports because of my natural athletic ability, but martial arts specifically…

*Oh. There was one.*

When my expression changed, Cheongpung nodded as though to say he had been right.

“See? Something like that happened, didn’t it?”

“There was one. Taekwondo.”

“Taekwondo?”

“It’s something like a martial art.”

Back in elementary school, I had been tricked into enrolling at a taekwondo academy by the promise of receiving a portable game console.

The older high school students had put on a taekwondo demonstration, and after watching it exactly twice, I could follow all eight Taegeuk forms.[^1]

[^1]: Taegeuk forms are a standardized sequence of eight color-belt patterns in taekwondo.

Of course, I beat up a middle-school student two years older than me and got kicked out less than a week later.

*Could that have been it?*

Come to think of it, even back when I had been an F-rank Hunter, I had been pretty good at copying almost anything.

My poor physical abilities had simply held me back.

If someone at the bottom of the Hunter ranks tried to imitate the movements of a mid-rank Hunter, he wouldn’t be able to generate any destructive power. He would only end up tearing his groin apart.

*But things are different now.*

Overflowing internal energy. Excellent physical abilities. And martial arts learned in Murim.

Now that I thought about it, I might not be a genius of martial arts, but I did seem to have a fair amount of talent.

“How long did it take you to learn the Plum Blossom Fist, Young Hero Cheongpung?”

“One month.”

“One month?”

From my own experience, the Plum Blossom Fist was a Huashan martial art, but it wasn’t complicated enough to take that long.

And this guy had taken a month to learn it, while I had managed to roughly copy it after three days?

*That’s insane.*

As I grinned so broadly that the corners of my mouth nearly split, Cheongpung added,

“It took me a whole month to achieve Great Attainment, so my grandfather scolded me terribly.”

“…”

Right. Of course.

As I stared at him in disbelief, Cheongpung muttered,

“Still… it doesn’t feel very good. Having someone copy my martial arts.”

A dangerous aura rose from him.

* * *

After regaining consciousness, Hyuk Mujin stared blankly at the training ground.

*This is incredible.*

The training ground had already been half reduced to rubble.

More than half of the bluestone carefully laid by stonemasons famous throughout Shanxi Province had been smashed apart, and the destruction was continuing at a rapid pace.

*Clang! Ka-ka-ka-clang!*

Despite the season, the center of the training ground was scorching hot. Spear and sword clashed amid bursts of flame.

The owners of the weapons moved at dazzling speed, exchanging blows so quickly that even Hyuk Mujin, a First Rate master, struggled to follow them.

*How can they be that fast?*

Cheongpung wore white martial robes, while Jin Taekyung wore black. The two young men were starkly different at a glance, yet the fact that they were around the same age was simply astonishing.

*That Cheongpung fellow is a monster.*

He had an ordinary build and a gentle appearance. If he spent half a day walking around Taiyuan, he would probably encounter three or four young men his age who looked much like him.

But that ordinary-looking young man concealed an identity no one could easily have guessed.

*The heir who inherited everything from the Sword Saint Mae Jonghak.*

*Whoosh! Whoosh!*

Beneath the high-riding sun, Jin Taekyung’s spearhead flashed.

His forms were heavy and concise, but with power and speed added to them, they transformed into an extremely fast spear technique that made Hyuk Mujin dizzy just watching it.

*What if that spear were aimed at me?*

Hyuk Mujin shook his head from side to side.

It was embarrassing, but he had no confidence that he could last even a full quarter hour. No, perhaps even that thought was nothing more than consolation meant to preserve his pride.

But Cheongpung was different.

*Swish, swish-swish-swish!*

The spearhead came at him from every direction, only to slice uselessly through empty air. Cheongpung’s face remained calm as he effortlessly dodged every attack.

Then his hand blurred.

A streak of light split the air.

*Whoosh! Boom!*

“Hng!”

Jin Taekyung let out a groan amid the thunderous impact. He had barely blocked the sword, but sword strikes poured toward him like a torrential downpour.

Hyuk Mujin watched the scene with his mouth falling open.

At that moment, one thought filled his mind.

*Graceful.*

That was the only way to describe it.

Cheongpung’s movements were delicate and fluid, like the brushstrokes of a master painter. They resembled flower petals drifting and fluttering down at the end of the season.

Hyuk Mujin watched in a daze before suddenly muttering,

“Plum Blossom Sword Technique…”

He had never seen Huashan martial arts before.

But he could be certain of one thing. The very essence of Huashan martial arts had seeped into every one of Cheongpung’s movements.

*He’s a monster. He really is a monster.*

But “monster” was not a word that applied only to Cheongpung.

*Swish-swish-swish-swish!*

*Ka-ga-gang!*

Another man was blocking every strike of the Plum Blossom Sword Technique unleashed by the Sword Saint’s disciple.

The young man with a powerful build and striking, ruggedly handsome features ground his teeth.

“Fuck, Huashan made its martial arts a fucking nightmare!”

If Huashan had heard the thick profanity Jin Taekyung spat out, the entire sect would have turned upside down.

A rough aura poured from his body.

The domineering force of it momentarily suppressed Cheongpung’s graceful movements, and then flowed straight into a counterattack.

*Whoooosh! Boom!*

A powerful strike.

Cheongpung’s body flew through the air after blocking the spear amid the thunderous impact. Jin Taekyung had knocked aside Cheongpung’s offensive with a single move, but he immediately frowned.

“Ow, that stings.”

*Slice.*

Before his words had even ended, the black martial robes he wore split open in a long tear.

Several long wounds scored his exposed chest, blood welling freely from them.

“What martial art was that?”

“The Heavenly Eagle Claw.”

“You really have everything.”

“Would you like me to teach you?”

“You’re allowed to teach me?”

“Oh, I just remembered. My grandfather told me not to teach it to outsiders.”

“Again? I knew you’d say that.”

“Would you like to join Huashan?”

“No!”

Jin Taekyung shouted and kicked off the ground, charging forward.

His movements were instinctive, like those of a wild beast, yet they barely retained the form of martial arts. Hyuk Mujin shuddered.

*Why does that man get scarier the longer I watch him?*

Every person possessed something called an aura.

Jin Taekyung’s aura was tenacious and fierce. There was something about it that made anyone watching him feel afraid.

*It isn’t about his martial arts.*

Jin Taekyung was certainly a highly skilled master, but he was not yet the equal of Cheongpung, the Sword Saint’s disciple and a true Peak master.

Yet Hyuk Mujin had watched him from close by for the past several months, and he could say this with certainty.

*Even if the sky fell, that man would survive.*

Hyuk Mujin was certain Jin Taekyung would somehow return alive no matter what kind of hell he was thrown into.

Three Peak masters had tried to kill him so far, but in the end, they had been the ones to fall. In Murim, the one who survived was the strong one.

And Jin Taekyung had survived to the bitter end.

Besides…

*Captain’s growth is beyond imagination.*

It was something Hyuk Mujin knew because he had watched him from closer than anyone else.

From the moment Jin Taekyung had defeated Jopil, One Question, One Kill, after a desperate battle to the present, when he was fighting Cheongpung.

Jin Taekyung was growing stronger every day.

*And that’s true even now.*

Just a few days ago, he hadn’t been able to last even a hundred moves against the supreme techniques of Huashan that Cheongpung unleashed.

But now?

Hyuk Mujin alone had watched the exchange go well beyond three hundred moves. Even after being struck by the Heavenly Eagle Claw, a martial art that could be learned only by disciples of Huashan’s main sect, all Jin Taekyung said was, “Ow, that stings.”

*He’s a monster. A monster.*

Everyone around them was around the same age, and they were all Peak or advanced First Rate. Wasn’t that taking things too far? It seemed as though nothing but monsters surrounded him.

With a deep sigh, Hyuk Mujin remembered what Jin Taekyung had said a few days earlier while training the Wall Lizard Technique.

*If you don’t want to lose something precious, then risk your life and do it now. Working yourself to death while you’re still breathing is better than dying, isn’t it?*

Those words were true.

You had to work yourself to death to survive and become strong. Every moment was precious if you wanted to avoid being swept away by the waves of Murim.

Hyuk Mujin watched the two men spar for a while longer, then got to his feet.

*I can’t finish this with just my little toe.*

He had to become stronger. Strong enough to be acknowledged as Jin Taekyung’s right arm—or perhaps his heart.

And…

*Strong enough for everyone to remember the name Hyuk Mujin.*

He gripped his sword case tightly.
## Chapter artifact 158

# Chapter 158

Seven days and nights.

Seven days and nights had passed since I began sparring with Cheongpung. I thought with my eyes closed.

*If I’m supposed to defeat Cheongpung before New Year’s Day, just like the Quest says…*

There were only three days left. How many times had I fought Cheongpung by now?

All I knew was that we had dueled at least sixty times. Of course, I had lost every single one of them without exception.

*He hasn’t even used Sword Energy.*

Cheongpung wasn’t fighting at full strength. It was an enormous handicap for a Peak master not to use Sword Energy, but Cheongpung was still strong even without it.

He had learned Huashan’s supreme martial arts under the guidance of Sword Saint Mae Jonghak since childhood.

Even Jin Mukyung, considered one of the greatest young prodigies in the current orthodox Murim, had lost to Cheongpung.

*Although Jin Mukyung was injured at the time… this is definitely different.*

I recalled Cheongpung’s movements, which I had seen so many times that I was sick of them.

They were the very definition of grace.

That was probably a characteristic of the martial arts he had learned, but it was only possible because his own strength supported them.

*He’s simply a cut above me.*

Of course, I hadn’t shown him everything, right down to my underwear.

I still had One Annihilation, the Inventory System, and the Unnamed Sword, which could stand against Cheongpung’s Sword Energy.

But this was a spar, not a life-and-death duel.

*I have to win with martial arts.*

As far as I was concerned, the System was my final card.

In a battle where life and death could be decided by the smallest margin, the System could overturn the tide of battle. But if even a System-assisted attack was blocked, then all that awaited me was death.

It was literally my final card. There was nothing after that.

*I can’t rely on the System every time I fight.*

The world was vast, and there were many masters.

To prepare for powerful enemies who could appear at any moment, sharpening my martial arts had to come first.

“Whew.”

With a deep exhale, the forty-five years of internal energy that had been flowing steadily curled back up in my dantian.

> **System**
>
> - You have successfully completed circulating your qi.
> - The realm of the Jin Family’s Cultivation Technique has risen slightly.
> - Your stamina is restored and your fatigue relieved.

When I opened my eyes, the first thing I saw was Cheongpung and Hyuk Mujin locked in a fierce battle.

*Whack! Whack-whack-whack!*

“Gaaagh!”

“…”

I take that back. It wasn’t a fierce battle. Mujin was just getting beaten until his head nearly burst.

Hyuk Mujin was unable to keep his senses amid the forms of the Crouching Tiger Fist raining down like a sudden shower. He gritted his teeth.

“Hah!”

The sword in his hand shot forward like a ray of light.

The forms weren’t particularly unpredictable, nor did the sword technique reveal any extraordinary profundity, but his fundamentals were solid. He had probably swung that same sword thousands, perhaps tens of thousands, of times by now.

*Swish! Swish-swish!*

Head, shoulder, then chest. After avoiding three attacks in an instant, Cheongpung found Hyuk Mujin’s sword thrusting toward his chest.

*Whooosh!*

A clean, sharp strike without any unnecessary movement.

Unfortunately, his opponent was too strong.

“Wow, you’ve improved a lot!”

Between Cheongpung’s index and middle fingers, the blade he had seized trembled under the force being applied to it.

Empty-Hand Seizes the Blade.[^1]

It was a technique possible only when one’s martial arts were overwhelmingly superior to the opponent’s.

Humiliated by the unexpected display, Hyuk Mujin’s face flushed red.

“Hngh!”

“It won’t do you any good to put more force into—”

Cheongpung’s eyes suddenly widened.

Hyuk Mujin had appeared to be putting more strength into the sword he had seized, but he abruptly released the hilt and lunged into Cheongpung’s arms.

*Look at that bastard.*

I let out a quiet laugh. I had a pretty good idea why Hyuk Mujin, who had used honest martial arts until now, had suddenly pulled something like that.

*They say even a dog at a village school can recite poetry after three years.*

That was a method I often used. Abandoning the weapon that was as precious as life itself to a martial artist, catching the enemy off guard, and taking advantage of the opening.

It was a good attempt. But if there was one problem, it was that his opponent was far too strong for a trick like this.

*Boom!*

With a sound like a drum bursting, someone’s body went flying. I grinned as I looked down at Hyuk Mujin, who had landed right in front of my feet.

“Did you lose?”

After coughing and gagging for a while, Hyuk Mujin answered irritably.

“You saw everything. Why are you asking?”

“What number was that?”

“That makes ninety.”

“You’ll hit a hundred soon. How about Hundred Battles, Hundred Losses as your nickname?”

“I’ll pass.”

“Still, the last one wasn’t bad.”

Hyuk Mujin’s ears twitched at my praise.

“Really?”

“Yeah. But the difference in skill was way too great. Size up your opponent before trying that.”

“I knew it. I was wondering why you were praising me for once.”

“Do you think you could have landed even one hit with a move like that?”

“If Young Hero Cheongpung hadn’t used a palm technique, I could have hit him at least once.”

As Hyuk Mujin grumbled with his lower lip sticking out, Cheongpung ran over with an innocent expression.

“Are you all right?”

“No, weren’t you going to use only fist techniques?”

“I was going to start using palm techniques now. You’ve improved much faster than I expected.”

“Ahem. Then go ahead and do that.”

Look at him. Mujin’s mouth was about to split open.

Normally, I would have interrupted to give him a hard time, but I agreed with Cheongpung to a considerable extent.

*He really is improving quickly.*

I wasn’t the only one who had grown over the past week. Hyuk Mujin had as well.

Even though he had Cheongpung’s help, he had completed his Wall Lizard Technique training despite having far inferior stats. He had also improved enough for Cheongpung to bring out his palm techniques first.

*That’s not all.*

I activated Qi Sense to check Hyuk Mujin’s Level.

> **System**
>
> - You used **Qi Sense**. At your current six-star realm, you can search for targets at Level 80 or below within 60 jang.
> - **Qi Sense** has identified the target.
>
> **Lv. 50 Hyuk Mujin**

Only ten days ago, Hyuk Mujin had been Level 48. But after training, he had gone up two Levels.

*Level 50? Already?*

By checking Levels with the System, I could roughly gauge an opponent’s strength.

The problem was that most people’s Levels either stagnated or rose so slowly that it was difficult to notice.

*But this guy’s Level keeps shooting up.*

I suddenly remembered when I had first met Hyuk Mujin.

Back then, he had been only Level 20. He wasn’t anywhere near me—I had already passed Level 60—but even so, his Level-up speed was no joke.

*Maybe it’s because he’s been dragged around with me.*

Now that I thought about it, he had gone through every kind of hardship while traveling with me. Had actual combat naturally trained him?

Under my gaze—as though I were studying some fascinating creature—Hyuk Mujin asked,

“Why are you looking at me like that?”

“Huh? Nothing. I was just thinking that you really have improved a lot.”

“Ahem. Ahem!”

“That was me being generous. From now on, you’ll get the pinky.”

“…You’re awfully stingy.”

“Never heard the phrase about a painful pinky?”

“So I’m your painful pinky, Captain?”

“No. It’s just a saying. Remember it.”

“…”

“All right, our Great Hero Hyuk Mujin of Hundred Battles, Hundred Losses can step back now.”

“I told you I’m not using that nickname!”

I let Hyuk Mujin’s shout pass in one ear and stepped forward after steadying my breathing.

“How about circulating your qi once?”

Cheongpung smiled brightly.

“I barely moved, so I didn’t even sweat. Why would I?”

Mujin was going to cry. He really was.

I smiled along with Cheongpung’s radiant expression.

“You’re going to sweat a little now.”

“Someone at your level makes an interesting opponent, Benefactor.”

That was an unusually challenging tone for Cheongpung. But based on everything I had seen so far, this was his true nature—the competitive pride of Cheongpung the martial artist.

I clearly remembered how he hadn’t smiled even once while fighting Jin Mukyung with his sword.

“It’s going to get less fun now.”

“That’s all right. Winning is always fun. Hehe.”

“Are you sure you won’t regret saying that?”

“Yes! I’m already winning without using Sword Energy!”

“…”

Damn. That hit a nerve.

I calmed my shaken heart after being struck by such blatant facts and gripped my spear tightly.

“This time will be different.”

“My grandfather told me something. He said only weaklings say things like that. True masters show it through their actions.”

“Don’t worry. That’s what I intend to do now.”

“I’m looking forward to it.”

I looked at Cheongpung, who was still grinning from ear to ear, and murmured inwardly.

*Open Status Window.*

> **System**
>
> **Status Window**
>
> **Lv. 64 Jin Taekyung**
>
> **Job:** First Rate martial artist  
> **Fame:** 2,400 (+250)  
> **Titles:** 5 (Title effects active)
>
> - **Returnee** (All stats +10)
> - **Sleeping Dragon of Shanxi** (All stats +15, Fame +200)
> - **Scion of a Great Family** (All stats +5, Fame +50)
> - **Gambler** (Combat-related stats +10% in one-on-one combat)
> - **Intermediate Trainee** (Training speed +20%)
>
> **Strength:** 205 (+30)  **Stamina:** 207 (+30)  
> **Agility:** 200 (+30)  **Intelligence:** 40 (+30)  
> **Charm:** 40 (+30)  **Internal Energy:** 45 years  
> **Toughness:** 200 (+30)
>
> **Remaining Points:** 100
>
> - Distribute your remaining points.

My combat stats had finally broken through 200 thanks to training the Wall Lizard Technique and sparring. And I still had the points I had diligently saved in preparation for encountering an enemy.

At this moment, I wasn’t envious even of the greatest under heaven.

“I was really saving these up… but I’m using them because of you.”

“Huh?”

“Sword Energy, the Zaha Divine Technique—anything is fine. Give it everything you’ve got.”

“Then it’ll be too bland.”

“You should taste it before deciding whether it’s spicy or bland.”

Before I had even finished speaking, an order had already been delivered to the System in my head.

*Assign fifty points to Agility.*

*Whooosh.*

It was a force only I could feel in this world.

The moment an unprecedented power, whose origin I could not identify, flowed through my entire body like a wave—

“Let’s start with mild Neoguri.”[^3]

*Whooosh!*

My spear began moving at a speed it had never reached before.

* * *

*Swish—boom!*

Cheongpung twisted his neck. His hair, tied tightly behind his head, burst through the air.

But the spear’s movement did not end there.

*Whoom—whooosh!*

More than ten spear images charged in from every direction. Cheongpung stepped forward without hesitation.

*Crack!*

The remaining bluestone shattered, and dirt erupted into the air.

Jin Taekyung looked at Cheongpung, who had retreated three jang in an instant, and asked,

“I knew you’d do that. Dark Fragrance Drift?”

“I mixed it with the Five-Element Plum Blossom Steps.”[^2]

“Can you even do that?”

“It worked, didn’t it?”

“And how does it taste?”

“It’s bland. Very bland.”

“That can happen. For now.”

After finishing his sentence, Jin Taekyung suddenly shuddered from head to toe and grinned.

“From now on, Jin Ramen spicy flavor.”

The incomprehensible words had barely left his mouth when Jin Taekyung charged.

The spearhead rose as if it would pierce the sun, then slashed downward with a terrifying sound as it tore through the air.

*Whoooooosh!*

At that moment, Cheongpung drew his sword. Vivid violet Sword Energy had already gathered along its blade.

No—the Zaha Divine Technique was flowing from his entire body, not just his sword.

*Boom!*

Force collided with force.

A thunderous roar rang out as though the sky itself were splitting apart.

The smile vanished from Cheongpung’s lips. A considerable backlash traveled through his aching wrist.

*How?*

It was different. Far too different.

Even the phrase *looking at someone with new eyes* failed to describe it.

Before he could even rub his eyes, Jin Taekyung had grown stronger—and then stronger again.

*And his internal energy…*

The Zaha Divine Technique was an internal-energy cultivation technique of the Extreme Yang nature. But the internal energy transmitted through Jin Taekyung’s spear was no less powerful.

Cheongpung felt a faint trembling from the spearhead pressing down on his sword.

*Vrrr, vrrr.*

They said that those who reached the wall of the Peak realm could hear someone crying before breaking through it.

A martial artist’s weapon, as precious as life itself, was the first to notice its owner’s transformation.

Internal energy that had reached the realm, and a physique ready to become a Peak master.

When all of those conditions were met, this was the sound that rang out.

*A Sword Cry?*

It wasn’t a sword. It was a spear.

So it was a Spear Cry.

As Cheongpung stared with his mouth hanging open, Jin Taekyung grinned.

“All right. From now on, Puramyeon spicy flavor.”

*Krrrnnng.*

With the force to move a thousand catties, the spear’s cry rang out even louder.[^4]

[^1]: *Empty-Hand Seizes the Blade* is a technique for catching an opponent’s weapon between the bare fingers.

[^2]: *Five-Element Plum Blossom Steps* is a footwork technique combining Five-Element movement with Plum Blossom steps.

[^3]: Neoguri, Jin Ramen, and Puramyeon are instant-noodle names; Taekyung uses their flavor labels as a joke.

[^4]: A catty is a traditional East Asian unit of weight. “A thousand catties” is an expression for tremendous force.
## Chapter artifact 159

# Chapter 159

Fifty points to Agility. And fifty points to Strength.

That made a hundred points in total. I had poured them all in at once—a massive number of points that would normally take ten Level-ups to earn—but I didn’t regret a single one.

*Points really are the best. Always thrilling. Always new.*

The toes kicking off the ground and the hand gripping the spear shaft cried out.

The me of now was far stronger than I had been only a few seconds ago.

And at last, I had taken the first step toward winning this duel.

*I’ll end this quickly.*

*Whoooooosh!*

The instant the spearhead came crashing down with a terrifying sound, a violet haze rose from Cheongpung’s entire body.

*The Zaha Divine Technique.*

It was proof that Cheongpung had finally begun fighting at full strength. But there was still one crucial thing left in this match.

*Whoooosh!*

As expected, a streak of Sword Energy shot up from Cheongpung’s waist.

Sword Energy, the exclusive domain of Peak masters, possessed enough cutting power to slice through steel.

I hadn’t yet crossed the wall into the Peak realm. I couldn’t meet it head-on.

I had to either retreat a step or factor in the spear being destroyed and continue with my next attack.

But…

*What is this feeling?*

A strange sense of déjà vu. My heart pounded, and my vision grew sharp. In a world that seemed to have slowed down, the cool spear shaft in my grip trembled.

*Vrrr. Vrrrr.*

Keep the head cool. Keep the heart hot.

That was how I had fought for seven years…but this time was different. This was instinct. Nothing but instinct ruled over my entire being.

*I can do it.*

Like a man possessed, I put more strength into the descending spearhead.

Forty-five years of internal energy raced along my fingertips toward the spearhead. The trembling in my grip grew stronger, and Cheongpung’s violet Sword Energy dazzled my eyes.

That was all.

*Boom!*

Two enormous forces collided.

A thunderous roar and brutal gusts of wind. Cheongpung’s eyes opened wide.

And then…

*It’s fine.*

The snow-white spearhead was still there.

The spearhead pressing down on Cheongpung’s Sword Energy trembled, not even a hairline crack running across it.

*Vrrrrrrr.*

It sounded like hundreds of bees beating their wings.

*How is this possible?*

Was this also the effect of raising my Strength? Or was it simply a coincidence?

At that moment, the answer to my question rang out.

> **System**
>
> - You have finished preparing to step into a new realm.
> - Your weapon is resonating with your energy.
> - Quest *Beyond the Wall* has been generated.

*Ah.*

It wasn’t the effect of raising my Strength. Nor was it a coincidence.

This was the natural order of things. After enduring countless hardships, I had finally come face-to-face with the wall. Now I had to cross it.

The wall of the Peak realm—a wall countless people had failed to overcome.

*A Peak master.*

True superhumans who wielded Sword Energy, or Aura.

A shiver ran through me at the thought alone. Memories from the past flashed before my eyes like a cheap monochrome film.

A mere F-rank Hunter, one of countless others, had made it this far. There had been countless crises, and someone had made a sacrifice.

> **System**
>
> **Quest:** *Beyond the Wall*
>
> Would you like to accept this Quest?
>
> **Y / N**

I had crossed the boundary between life and death countless times. I had to cross a mere Peak wall with ease if I didn’t want to be ashamed of the days I had lived through.

*Obviously yes.*

> **System**
>
> - You have accepted the Quest!

*Ding.*

As the cheerful System notification rang out, I pulled up the corners of my mouth.

My thoughts had been long, but only a short time had passed. I whispered to Cheongpung, who was looking up at me with bewildered eyes.

“Now, it’s Puramyeon spicy flavor.”[^3]

I’ll show you what Korean spice tastes like.

* * *

*Krrrnnng.*

Compared to roughly a minute ago, my Strength had risen by twenty-five percent.

It was the difference between heaven and earth. Cheongpung was visibly flustered by my sudden transformation.

“B-Benefactor. Where did this sudden strength come from?”

“It’s Korean rice power. Especially gukbap.”[^1]

“Pardon?”

“I used to eat two bowls of pork-bone hangover soup every morning. And five bowls of rice.”

“What does that even—gasp!”

*Krrrnnng.*

Cheongpung swallowed a breath as my force continued to build.

He had Sword Energy and the Zaha Divine Technique, but neither was having much effect. The spear, resonating while filled to the brim with my qi, had grown sturdy enough that even Sword Energy could no longer cut it.

*I have a real shot at winning.*

But Cheongpung was not an opponent who would go down easily.

“Hup!”

With a short shout, an incredible force knocked the spearhead upward.

It had only been lifted a handspan, but the instant Cheongpung escaped the pressure, he didn’t let the opportunity pass.

“I’m sorry. I took you far too lightly, Benefactor.”

Before he had even finished speaking, an invisible force shot from his palm.

The Taeeul Miri Palm. A secret ultimate technique of Huashan, personally taught to him by the Sword Saint himself.

“Hngh!”

*Bam-bam-bam!*

Sharp pain shot through me as I staggered backward five steps in succession.

Thank goodness I had improved my bones and muscles as well as my Sinews and Meridians with every Level-up. Otherwise, I would have been in serious trouble.

“Damn, that hurt.”

Cheongpung stared at me with the wide, startled eyes of a rabbit.

“A Seven-Star Taeeul Miri Palm…”[^2]

“Don’t say that. Now I want some cider.”

“Pardon?”

There it was. Exactly the reaction I expected.

The instant Cheongpung asked what I meant, my spear was already thrusting toward his chest.

A perfectly timed surprise attack. But there was no way it would end with just that.

As if answering my thoughts, Sword Energy slammed into the spearhead.

*Clang!*

*I wasn’t expecting it to work.*

With no expectations, there was no disappointment. And since my emotions remained steady, my forms did as well.

*Next, the waist.*

*Whoooosh!*

Cheongpung twisted his waist as the spear moved.

The gust raised by the spearhead silently sliced through his shirt. A faint line of blood appeared across the exposed flesh.

A small gain was still a gain.

*Next, the neck.*

I turned with the motion and swung the spear shaft at Cheongpung’s neck.

*Boom!*

That was not the sound that should have come from a collision between a human body and a steel spear.

But Cheongpung had martial arts—the Zaha Divine Technique, both one of the greatest internal-energy cultivation techniques under heaven and a protective qi art.

I clicked my tongue as I watched the violet energy around him grow denser.

*Even so, how can there be absolutely no damage? This is outright cheating.*

Talk about a plum-blossom silver spoon. How was I supposed to spar with this kind of unfair advantage?

But I didn’t have time to complain. Cheongpung had closed the distance to right in front of me in barely half a step, and the Sword Energy he scattered filled my vision.

*Whoooosh!*

The tip of his sword bloomed with flowers.

The movement was so fluid it was beautiful. But if I let myself be mesmerized, I would soon find myself standing before a sign for Mount Beimang.

The Plum Blossom Sword Technique I had watched until now was frightening martial arts—extremely intricate and complicated forms.

When Cheongpung wielded it, it felt as though I were trapped in a rainstorm.

But…

*I can see it.*

I opened my eyes wide. My breathing slowed, and my vision sharpened. The sound of my heartbeat was like thunder, and the spear trembled in my hands.

*Vrrrr. Vrrrrr.*

The spear was ringing.

At this moment, the spear and I were practically one body.

The spear shaft no longer felt cool.

*Shishishishik!*

Sword and spear became a blur.

I continuously deflected and knocked away the Sword Energy pouring down like rain.

Ten times, twenty, maybe thirty…

Cheongpung was tenacious and sharp beyond anyone I had ever fought.

When I countered the Sword Energy digging toward my waist, the Taeeul Miri Palm flew at me. When I avoided the Taeeul Miri Palm, the Crouching Tiger Fist aimed for my chest.

*Thud!*

The shoulder that blocked the Crouching Tiger Fist throbbed.

A momentary pain. As my movements slowed for an instant, Cheongpung opened the fist he had curled shut.

Air burst from the tips of his five fingers.

*Ah, damn it. Right, he had that too.*

The moment I realized it, I bent my waist backward like a bow.

The Plum Blossom Five-Point Finger. He had shown it only once during his duel with Jin Mukyung.

*Pip-pip-pit!*

Five streams of finger force grazed the bridge of my nose and earlobe by a hair.

*He really is strong.*

I felt it again: Cheongpung was not an ordinary swordsman.

He was not only the heir of the Sword Saint Mae Jonghak. He had also mastered Huashan’s secret techniques—in other words, he was a complete gift set of Huashan martial arts.

I wiped away the blood seeping from my wounds and spoke.

“You’re coming on a little strong, aren’t you?”

“That’s what I’d like to say to you, Benefactor. Honestly, you surprised me.”

“Why? Because someone who seemed like no big deal is fighting much better than expected?”

“Yes!”

“…”

“You’re better than I thought. Seriously. And…”

“And?”

“It’s fun.”

As I watched the faint smile on Cheongpung’s lips, I thought about it.

Setting his competitive pride aside, this guy simply loved martial arts themselves. He was proving to me how frightening a genius who truly enjoyed martial arts could be.

“Aren’t you the same as me, Benefactor?”

“Young Hero Cheong, do you know what my dream is?”

“…”

“To retire in one piece and put up a building in my name. I’ll collect rent and spend my old age in comfort as a landlord.”

“A landlord?”

“Put simply, um… Yes. You can think of it as being one of those people up in the sky.”

“Ah-ha.”

Cheongpung nodded as though he understood.

“You want to become the Martial God.”

“No, that’s not what I meant. Where did the Martial God come from?”

“Is that not it?”

“No. It’s completely different.”

“But you do seem to like martial arts.”

“Me? Not to that extent.”

“Your expression looks happy.”

Only then did I realize that the corners of my mouth had been raised the entire time.

*Since when?*

As I stood lost in thought, Cheongpung smiled brightly.

“If you’ve caught your breath, shall we start again?”

“…How long have you known?”

“It’s a method I’ve used on my grandfather many times.”

People really were all alike. I burst out laughing.

“You’re more perceptive than I expected.”

“My sword is faster.”

*Tsssss.*

The moment violet Sword Energy surged from Cheongpung’s blade, the spear in my hands trembled violently.

* * *

*Clang!*

The First Form of the Jin Family’s Spear Technique. The spear thrust straight ahead was blocked by the sword blade.

The Jin Family’s Spear Technique was an honest martial art. Simple and rough.

It was clearly a First Rate martial art, but when it came to subtle principles, it was far too simple.

*Compared to Huashan’s secret techniques, it falls hopelessly short.*

Martial arts ultimately came down to combinations of movements.

Thrust, strike, cut.

Through the circulation of internal energy, the slightest change in angle, and the forms that followed one another, one could create endless variations.

I had attained mastery after arduous effort, but the Jin Family’s Spear Technique and the Jin Family’s Manoeuvre Technique lacked that kind of subtlety.

*Whoooooosh! Clang!*

In that respect, my opponent was a terrible match for me.

Cheongpung was a Peak master with eyes sharp enough to see through my martial arts at a glance.

As if he had decided to stop holding back, he began pressing the attack in earnest.

*Whoosh! Bam-bam!*

*Sword techniques, fist techniques, palm techniques, hand techniques, even claw techniques.*

He really was a genius of martial arts. He chained together roughly ten different martial arts, yet every movement fit perfectly into the next, like interlocking gears.

His eyes shone like morning stars, and his breathing was slow and steady.

*So this is what it means to be the Sword Saint’s Disciple.*

An excellent Master and excellent martial arts.

And talent on top of that.

The world was always unfair. And over the past seven years, I had learned how to adapt to that unfair world.

*Persist, move slowly, and never give up.*

That was my way.

I had never wanted to be a tortoise that caught up with a rabbit far ahead.

Crossing the finish line was enough.

Surviving and retiring. That was the greatest dream a lowest-rank Hunter could have.

*I had to claw my way to survival.*

I learned everything in the Gates. Goblins holding rusty knives and firing poison needles were my sparring partners.

Unlike duels in the Murim, I had to stake my life on every fight. But that was why I learned faster.

And then…

*I came to the Murim.*

*Clang-clang-clang! Slash!*

My side burned. I could feel blood flowing, but I didn’t make the stupid mistake of checking the wound.

The human body was weaker than you might think, and stronger in its own way. Even if some blood was flowing, the bleeding would soon stop once it clotted.

“Ugh!”

Funny enough, Cheongpung’s weak stomach gave me an opening.

I charged at the Cheongpung who had faltered.

*Second Form of the Jin Family’s Spear Technique.*

*Whoooooosh!*

It had been about a week after I fell into the Murim, I think.

I found two martial arts manuals in a dust-covered archive: the Jin Family’s Spear Technique and the Jin Family’s Manoeuvre Technique.

If you asked why I learned them, the answer was simple.

*To survive.*

To me, the Murim was another Gate.

I had to learn if I wanted to survive.

That was how I entered the world of martial arts. Before I knew it, several months had passed.

And then everything changed completely.

*Shishishishik! Bam!*

*Hngh.*

The Plum Blossom Five-Point Finger.

The instant I avoided the five streams of finger force, the Taeeul Miri Palm struck me.

I had poured in a full hundred points, but I still hadn’t caught up to Cheongpung.

However, to fight someone who already knew the Jin Family’s Spear Technique inside and out, I had no choice but to keep charging forward like a rhino.

*Third Form of the Jin Family’s Spear Technique. Fourth Form.*

The Jin Family’s Spear Technique grew more powerful the farther it advanced. Its footwork was designed to match.

Its essence was to pressure an opponent with simple forms tailored for actual combat.

*If I can’t do it with my teeth, I’ll do it with my gums.*

My understanding of martial arts might be lacking, but my stats were not inferior.

As I pressed forward, Cheongpung retreated.

Riding the momentum, I thrust and slashed with all my strength. Even as I panted until my mouth tasted sweet, I suddenly remembered the conversation I had just had with Cheongpung.

*But you like martial arts, don’t you?*

*Me? Not to that extent.*

*Then why have you been smiling?*

That was obviously because…

*It’s fun.*

*Whoooooosh! Boom!*

Sword and spear collided.

The bluestone laid neatly across the training ground shattered into powder and scattered through the air.

As the thick cloud of dust cleared, Cheongpung came into view.

His smile was clear and bright, completely at odds with the situation we were in.

“Martial arts are fun, right?”

After thinking for a moment, I nodded without a word.

“Why did you say they weren’t earlier?”

“Let’s just call it a difference in how we’ve lived.”

For seven years, I had lived as though I were being chased by something invisible.

Guilt, perhaps. Or a sense of responsibility.

Or maybe it was simply self-satisfaction, a way to rationalize all of it.

As he watched me hesitate, Cheongpung spoke.

“My grandfather once told me something. He said, ‘Martial arts? They’re nothing special!’”

“Hmm? The Sword Saint?”

“It’s true.”

Cheongpung continued with an aggrieved expression.

“He said it wasn’t martial arts, but empty space[^4]. Since it’s empty to begin with, you just accept it as it is and fill it in.”

“Accept it as it is and fill it in.”

“I’m serious. You can ask my grandfather later…”

Cheongpung’s voice gradually faded, then cut off completely.

I closed my eyes.

In the pitch-black darkness, forgetting the passage of time and the place I was in, I muttered a single sentence as though possessed.

*Accept it as it is and fill it in…*

Why did those words keep catching at my heart?

The more I repeated them, the harder my heart pounded and the more my entire body itched.

It felt as though the boulder weighing down my chest were shifting.

*It isn’t martial arts. It’s empty space. Accept it as it is and fill it in…*

I didn’t know whether several seconds or several hours passed.

In the darkness, even the flow of time seemed to have stopped.

In that suffocating darkness, where it would not have been strange for a day, two days, three days, or even a year to pass, I opened my eyes.

“Benefactor, how do you feel?”

Instead of answering Cheongpung’s question, I looked around.

Hyuk Mujin was dozing in the corner, while the ink-dark sky was filled with a cluster of stars that looked ready to pour down at any moment.

Was this really the world I knew?

“Was my grandfather right?”

It was Cheongpung’s second question.

I answered in a hoarse voice.

“No. Not at all.”

Martial arts were fucking hard.

Still…

*Ding.*

> **System**
>
> - Quest *Beyond the Wall* has been successfully completed!
> - Your class has changed to **Peak Master**!

Now I knew one thing.

[^1]: *Gukbap* is soup served with rice; *bone haejangguk* is a hearty pork-bone soup traditionally eaten as hangover food.

[^2]: The Korean word for “seven-star” also appears in *Chilsung Cider*, a Korean lemon-lime soft drink, setting up Taekyung’s next line.

[^3]: Puramyeon is an instant-noodle brand. Taekyung uses its spicy flavor as the next step in his escalating flavor joke.

[^4]: Mae’s line is a wordplay on two Korean terms pronounced *mugong*: “martial arts” and “empty space.”

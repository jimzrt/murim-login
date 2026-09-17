# Checkpoint Review — 295–299

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

# Chapters 295–299

## Plot

The leading Skeleton Knight evolves into a speaking Level 105 Skeleton Warlord after defeating the Black Forest’s former ruler. Its Summon the Dead and Commander’s Rally skills create and strengthen a massive undead army, but Jin Taekyung tricks the Warlord into concentrating the force and destroys most of it with One Annihilation. After surviving as a damaged skull, the Warlord bargains for its life and agrees to supply Skeletons as the Peace Guild’s contracted EXP factory manager while retaining control of the Black Forest and its undead.

The Warlord reveals that a black wizard summoned and controlled it, but an unexplained surge in magical power recently freed it. Taekyung begins harvesting resurrected Skeletons for EXP, Magic Gems, and Equipment. When the Warlord detects intruders, Taekyung approaches the Gate with its skull.

Meanwhile, the Hunter Association delays the rescue for one hour and eight minutes despite the arrival of more than thirty A-rank Hunters and an Ares Guild contingent. Choi Minwoo leads more than fifty Peace Guild members into the Black Forest, where they find a scorched trail and no life within three hundred meters. Believing Taekyung and the Named Monster dead, the Guild mourns while the Seoul Branch President and Go Jun treat the outcome as a successful avoidance of further casualties. Go Jun taunts Choi and blames the Peace Guild, only for Taekyung to return alive, mock the premature forty-ninth-day memorial rite, and challenge Go Jun to fight.

## Continuity

- The Skeleton Warlord is a Level 105 Named Monster, former ruler of the Black Forest, and commander of its undead.
- The Warlord can speak, use Summon the Dead and Commander’s Rally, and raise Skeletons on demand.
- Taekyung and the Warlord have an agreement: the Warlord retains nominal authority and supplies Skeletons as the Peace Guild’s EXP factory manager.
- The Warlord’s sudden magical-power surge freed it from the black wizard’s control despite its lack of Magic Gems; the cause remains unknown.
- Taekyung has repeatedly harvested the Warlord’s resurrected Skeletons for EXP, Magic Gems, and Equipment. He has not yet tested whether humans can absorb Magic Gems.
- The Hunter Association delayed the rescue response for one hour and eight minutes. The Seoul Branch President deferred to Go Jun and initially blocked the Peace Guild’s entry.
- Choi Minwoo, Butler Kim, Song Song, and Im Kkeokjeong left their secret cultivation training to join the rescue. Choi led more than fifty Peace Guild members into the Gate.
- Taekyung survived the Black Forest devastation and is now directly confronting Go Jun; the Seoul Branch President is also present.
- Choi Minwoo remains at Four Stars in the Jin Family’s Cultivation Technique and possesses hidden internal energy equivalent to one jiazi. Its origin and his grandfather’s involvement remain unresolved.
- Taekyung’s failed breakthrough into the Supreme Peak realm, the Warlord’s anomalous evolution, and the black wizard’s identity and intentions remain unresolved.

## Translation Decisions

- Render **비급제작** as “Martial Arts Manual Creation,” **마나 연공법** as “Mana Cultivation Method,” **진기도인** as “True Qi Guidance,” **소주천** as “Small Circulation,” and **일주천** as “complete circulation.”
- Render **삼화취정** as “Three Flowers Gather at the Crown,” **무아지경** as “Trance,” **내가고수** as “I’m a Master,” **칠 성** as “Seven Stars,” and **사 성(成)** as “Four Stars.”
- Render **수련자** as “Trainee” and **훈련 교관** as “Training Instructor.”
- Render **흑마법사의 검은 숲** as “Black Wizard’s Black Forest,” **망자 소환** as “Summon the Dead,” **사령관의 고무** as “Commander’s Rally,” and **경험치 공장장** as “EXP factory manager.”
- Render **도사견** as “Tosa mastiff,” **댕댕이** as “pup,” **49재** as “forty-ninth-day memorial rite” with an explanatory footnote, and **산화하다** in the destruction context as “be oxidized.”

## Durable state

{
  "active_continuity": [
    "The Peace Guild remains committed to its members and continues expanding through selective Hunter recruitment, generous support, and exclusive Gate rights.",
    "Taekyung leads accelerated training raids for Peace Guild recruits, with Kim Jinsoo acting as the third-week trainees' operational deputy.",
    "The A-rank Black Wizard's Black Forest contains a large undead army and was ruled by a black wizard or necromancer.",
    "The Skeleton Warlord commands the undead and serves as the Peace Guild's contracted EXP factory manager.",
    "The Warlord's sudden surge in magical power freed him from the black wizard's control despite having no Magic Gems; the cause remains unknown.",
    "Taekyung has completed repeated training raids without trainee deaths so far, though injuries have occurred.",
    "Team Leader Choi and three other senior Guild members remain focused on cultivating the Jin Family's Cultivation Technique.",
    "Choi Minwoo reached Four Stars and possesses a hidden mass of internal energy equivalent to one jiazi.",
    "The Hunter Association delayed the rescue response at the Black Forest for one hour and eight minutes while the Peace Guild demanded entry.",
    "Choi Minwoo led more than fifty Peace Guild members into the Black Forest after declaring that they would take the lead.",
    "The rescue party found a scorched trail, no life within three hundred meters, and apparent evidence that Taekyung and the Named Monster had died together.",
    "Go Jun and the Seoul Branch President treated the apparent death as a successful outcome and taunted Choi Minwoo before Taekyung returned alive.",
    "Taekyung survived and returned to the trail, challenging Go Jun after mocking the premature forty-ninth-day memorial rite."
  ],
  "continuity_sources": [
    299
  ],
  "open_questions": [
    "Who actually taught Jin Taekyung the Jin Family's Cultivation Technique?",
    "What history led Lee Jungryong to regard the unrelated Cheon Taemin as his older brother?",
    "How extensive are Ares Guild's undisclosed forces beyond its officially registered Hunters?",
    "Will Im Kkeokjeong's reattached arms and trauma recover sufficiently for him to return to Hunter work?",
    "What is the origin of the large qi mass in Team Leader Choi's dantian, and what did his grandfather do to him?",
    "What prevented Taekyung from completing his breakthrough into the Supreme Peak realm?",
    "What caused the Skeleton Warlord's sudden magical-power increase and unusual evolution, and what will result from Taekyung's contract with it?",
    "What will happen when Taekyung confronts Go Jun and the Seoul Branch President after returning alive?"
  ],
  "safe_through": 299,
  "temporary_decisions": [
    "Render 비급제작 as “Martial Arts Manual Creation,” 마나 연공법 as “Mana Cultivation Method,” and 사 성(成) as “Four Stars.”",
    "Render 진기도인 as “True Qi Guidance,” 소주천 as “Small Circulation,” and 일주천 as “complete circulation.”",
    "Render 삼화취정 as “Three Flowers Gather at the Crown,” 무아지경 as “Trance,” 내가고수 as “I'm a Master,” and 칠 성 as “Seven Stars.”",
    "Render 수련자 as “Trainee” and 훈련 교관 as “Training Instructor.”",
    "Render 도사견 as “Tosa mastiff,” 댕댕이 as “pup,” 망자 소환 as “Summon the Dead,” and 사령관의 고무 as “Commander's Rally.”",
    "Render 정몽주 as “Jeong Mong-ju,” 단심가 as “Song of My Single Heart,” 통합 언어 팩 as “Unified Language Pack,” and 우렁각시 as “snail bride” with a footnote.",
    "Render 49재 as “forty-ninth-day memorial rite,” with an explanatory footnote.",
    "Render 서울 중앙 협회장 as “Seoul Branch President,” 경호팀장 as “Head of Security,” and 산화하다 in the destruction context as “be oxidized.”"
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 295

# Chapter 295

Shining armor. A dark green cloak fluttering like wings. Purple ghost fire burning in empty eye sockets.

And then… there was a voice.

- Come. Down. Hu. Man.

The moment I heard that metallic, scraping voice, I nearly fell out of the tree.

*It spoke?*

This wasn’t the first time something like this had happened. The Wyvern I’d killed in the past, “One-Eyed Carus,” had been capable of speech too.

But a monster speaking wasn’t something you could take lightly.

“A Named Monster…”

The words slipped from my mouth like a groan.

That was right. As far as anyone knew, only Named Monsters could use language.

And that very Named Monster had just been born before my eyes.

No—not born.

It had *evolved*.

> **System**
>
> **Level 105 Skeleton Warlord**

Evolution?

I had never heard or seen a Named Monster appear like this before.

*What is this, Digimon?*

*So monsters were that kind of monster? They could evolve, too?*

I’d already been thrown about five hundred light-years away from an ordinary life, and even I was bewildered. The other Guild members’ reactions went without saying.

“What is that?”

“Wait, didn’t it just say something?”

“I’ve never seen anything like that, not even in a monster encyclopedia…”

Of course they hadn’t.

Named Monsters were mutated species. Every individual had different traits and varying levels of strength. No one could know what they were like until they appeared.

*But why now, of all times?*

I licked my dry lips.

I didn’t know how powerful that Skeleton Warlord was, but it clearly possessed strength worthy of a Named Monster.

*And on top of that, there are two A-rank monsters—the Skeleton Knights.*

The remaining hundred and fifty or so were all B-rank Skeleton Mages or Warriors. They were practically an army, which made them extremely troublesome.

However, if I took on the Warlord and the two Knights—their leader and core forces—we had a fight we could win.

*We’ve been raiding nonstop until now.*

Only fifty Guild members had entered the Gate.

But more than half of them were Tosa mastiffs who had endured my whip and gone through hellish special training.

They had fought so many Skeletons over the past week that they were sick of the sight of them. If they responded calmly, they could handle two or three times their own numbers.

*And the new recruits are quite capable, too.*

We paid salaries at least as high as the major Guilds, so we had selected only the best.

This time, I had personally participated in multiple evaluations, including the interviews, and even scored their potential for growth.

To withstand the typhoon that was Ares Guild, I had selected only the finest saplings and transplanted them into the Peace Guild’s front yard.

*A little risk is unavoidable, but this is a fight worth taking on.*

Team Leader Choi and the other three had suspended most of their Guild duties and were focusing entirely on training the Jin Family’s Cultivation Technique.

If they had been here, the battle would have been much easier. But even if they had been present, I wouldn’t have sent them in.

A dagger hidden up one’s sleeve was lethal precisely because it was hidden. I couldn’t reveal it in a place with so many eyes watching.

Once I had finished thinking, I called out to one person.

“Jinsoo!”

“Yes, sir!”

Kim Jinsoo, who was effectively acting as the deputy team leader, answered promptly. I pointed at the Skeleton Warlord with the dagger in my hand.

The green ghost fire burning in its hollow eye sockets was still fixed on me.

“That’s a Named Monster.”

A sharp gasp rose from among the Guild members.

Most of them had been Hunters for less than two years. Even after surviving twenty years in this field, it was difficult to encounter a Named Monster. The tension was plain on their faces.

But Kim Jinsoo was different. His surprise lasted only a moment before he calmly nodded.

“I see.”

“Oh? You’re doing a pretty good job pretending to be calm.”

“I’m a little flustered myself, but we can’t just stand there in a daze and take it.”

Well, look at him.

I’d known from the beginning that he had guts, but this was a boldness unusual for someone in his first year.

Perhaps sensing my gaze, Kim Jinsoo gave a small smile and added,

“If this were a hopeless situation, you would have sent the retreat signal long ago. Am I right?”

“Hmm.”

“…Uh, did I get that wrong?”

“No.”

I let out a quiet laugh and shook my head.

“You’re right. This is a fight we can take on.”

“Oh.”

“I’ll handle those three over there. You handle the rest. How long can you hold out?”

Kim Jinsoo thought briefly before answering.

“The new recruits don’t have much experience… but we should still be able to hold out for an hour.”

“An hour?”

“Yes. At least an hour.”

The instant Kim Jinsoo answered confidently, the Skeleton Warlord slowly opened its jaw and released a strange resonating sound that defied description.

- G. R. A. A. A. A. H!

Beep!

> **System**
>
> **Level 105 Skeleton Warlord** has used a Special Skill!
>
> Special Skill **Summon the Dead** has activated!
>
> The sleeping dead answer their commander’s call!

It was a howl that sent a chill down my spine—and a cry that awakened the cursed dead.

Crack. Crack-crack-crack!

Soil burst upward, and the ground trembled. Piles of pale skeletons rose from all around us, took shape, and joined the ranks.

Bone Swords covered in dirt. Wooden shields tangled with fine roots. Among the Skeleton Warriors, I could even see Mages wearing necklaces engraved with skulls.

Even the A-rank monsters known as Skeleton Knights had increased by two.

Adding the newcomers to the existing Skeleton army brought their numbers to well over three hundred.

“…”

“…”

I watched the scene in silence before finally speaking.

“Jinsoo.”

“Yes.”

“Can you still do an hour?”

“Uh, well…”

“Be honest.”

“…I think we can manage about thirty minutes.”

“Really?”

“Yes. The situation has gotten a little worse, but I think we can do it.”

Kim Jinsoo continued, eyeing the Skeleton Warlord with a dubious expression.

“If that bastard doesn’t pull any more crap.”

“He looks like he will.”

“No way.”

- G. R. A. A. A. A. H!

“See? Wasn’t I right?”

Kim Jinsoo let out a groan.

“Oh, please.”

Beep!

> **System**
>
> **Level 105 Skeleton Warlord** has used a Special Skill!
>
> Special Skill **Commander’s Rally** has activated!
>
> The strength, Agility, and magic of the monsters under the Skeleton Warlord’s command have been enhanced!
>
> The enemies’ momentum rises sharply!

The Skeleton Warlord howled!

The effect was incredible!

“Wow…”

I activated Qi Sense and saw that every single one of them had gained five Levels.

The aura radiating from the Skeleton army of more than three hundred was on an entirely different level from before.

I turned my head slightly and found Kim Jinsoo staring blankly into space.

“Thirty minutes. Still possible?”

“…”

The bastard was cursing at me with his eyes now.

To be fair, even I thought it was unreasonable. Clicking my tongue, I gave the next order without hesitation.

“Fall back slowly. Don’t provoke them.”

“How far should we retreat?”

“To the path right in front of the Gate. Make sure we can get out at any time.”

“The path is narrow, so it should be easier to fight them there.”

“Exactly.”

As Kim Jinsoo had said, the path in front of the Gate was so narrow that five adult men could barely pass through shoulder to shoulder.

Even Skeletons, who were relatively thin by necessity, could only pass through seven or eight at a time.

However…

“Go straight out.”

There was no head-on battle with them in my revised plan.

“Huh?”

“Take the kids and get outside the Gate.”

Kim Jinsoo’s face filled with dismay.

“Then what about you, Senior?”

“Do you think they’ll play tag while you’re leaving? Someone has to buy time.”

“Senior! That’s dangerous!”

“Jinsoo. No—my dear Peace Guild members.”

I looked down with a solemn expression. Fifty Guild members were staring up at me, stretching their necks like baby birds.

“I—and the Peace Guild—always put the safety of our Guild members first.”

Several of the Tosa mastiffs muttered in voices barely loud enough to hear.

“That’s the biggest load of bullshit I’ve heard this year.”

“I think I nearly died seven times this week.”

“More like ten for me.”

Meanwhile, the eyes of the day-one pups trembled.

“Senior!”

“Ahh, Lord Fuck!”

“You’d go this far for us…!”

I continued in a voice thick with emotion.

“I’ll risk any danger for your safety. Even if my arm gets blown off! Even if my leg gets blown off! I will send every one of you back into the arms of those who love you!”

Several of them shouted with emotion.

“We can fight!”

“Please let us fight alongside you!”

I bit my lip tightly and shook my head.

“I can’t! In a situation like this, someone has to make the sacrifice, and I’m the best one to step forward!”

“But still…!”

Whoooosh! Shrrrk!

Before anyone could continue, an ominous black aura came flying toward us.

The Skeleton Warlord had sliced straight through a massive tree dozens of meters tall and several meters around. It shouted in a voice like metal scraping against metal.

- I. Will. Kill. Every. Last. One. Of. You!

Tap!

I leaped lightly from the tree and shouted,

“Everyone, return to the Gate! I’ll cover the rear!”

This time, no one tried to stop me.

The army of more than three hundred Skeletons had begun advancing.

Clatter. Thud. Clatter. Thud.

The monsters moved in perfect ranks and files, their aura utterly menacing.

The Warlord’s special skill had strengthened their steps, filling them with power. Faint lights flickered inside their hollow skulls.

- GRAAAAH!

When one of the Skeleton Knights, serving as a deputy commander, let out a fierce cry, rusted arrows and attack magic rose from the rear and shot toward the Peace Guild members.

Fwish-fwish-fwish! Whoooosh!

“Block them!”

“Tanks! Don’t lower your shields! Keep retreating slowly!”

“Commence covering fire!”

The two groups were about three hundred paces apart. To retreat safely, we needed to widen the distance further.

I swung White Flame and blocked the army’s advance.

“You bastards! How dare you threaten our precious Peace Guild members!”

Sssshhhk! Crack!

The force-loaded spear shaft shattered bones, and the Spear Energy extending from the transparent spearhead sliced in every direction.

Just as I killed ten of them in one blow, three Skeleton Knights charged in at once.

- GRAAAAH!

- GRAAAAH!

Sssshhhk!

Three streams of black aura grazed different parts of my body by the narrowest margin.

As blood trickled from my nape, sliced by the force of the wind, anguished cries erupted from among the Guild members who had already entered the narrow path.

“Senior!”

“Look out!”

Clang-clang-clang!

I deflected the aura that kept boring relentlessly into me and shouted with difficulty,

“Go! I’ll catch up soon!”

“But…!”

“Jinsoo! Go!”

Kim Jinsoo hesitated before leading the Guild members toward the Gate and shouting,

“You have to come back!”

I gave him a faint smile and nodded.

“Yeah.”

“I’m sorry, Senior!”

“It’s fine. Go!”

“Urgh!”

Kim Jinsoo hesitated until the very end, but then his back disappeared beyond the Gate.

Now, only I and the hundreds of Skeletons packed tightly into the narrow path remained.

- F. O. O. L. I. S. H.

Clatter-clatter-clatter!

The Skeleton Warlord emerged through the gap between the bones that split apart like the Red Sea.

- H. A. V. E. Y. O. U. R. E. S. I. G. N. E. D. Y. O. U. R. S. E. L. F. T. O. D. I. E, H. U. M. A. N?

But I wasn’t listening to it.

Only after thoroughly scanning the surroundings with hawk eyes did I let out a sigh of relief.

“Phew. They’re finally all gone.”

- …?

“The kids are way too sentimental for their own good. When the Team Leader tells you to go, you run. What do you mean, help? Right?”

I wiped the blood from my nape. I’d tried to keep the cut shallow, but it was deeper than expected. About 0.2 centimeters?

“Damn. That’s a waste of blood.”

The purple ghost fire in the Warlord’s eye sockets flickered uneasily.

- W. H. A. T. I. N. T. H. E. W. O. R. L. D. A. R. E. Y. O. U. P. L. O. T. T. I. N. G?

“Nothing much.”

Looking at the EXP—no, the Skeleton army—filling the narrow path without a single gap, I smiled with satisfaction.

“You’re all going to die here. That’s all you need to know.”

- W. H. A. T?

Instead of answering, I drew a deep breath.

The muscles throughout my body writhed, and the fire dragon coiled inside my dantian began to move according to the formula of the Fire Gate Divine Technique.

And then, in the next instant, I shot forward as one with the spear shaft in my hand.

“One Annihilation.”

KRAAAAAAASH!
## Chapter artifact 296

# Chapter 296

How much time had passed?

He could no longer remember his name, his family, his friends or lover… He could not even remember where he had been born or what kind of life he had lived.

After passing through a long, deep darkness, he suddenly came to his senses and found himself in a forest.

*Where is this?*

The question lasted only a moment.

Soon, he was seized by the instincts of a monster and began fighting without purpose. He fought the humans who had once been his own kind, and he fought monsters as well.

Once an outstanding knight in life, he grew stronger as he cultivated his mana. He even surpassed the black wizard who ruled the vast Black Forest and controlled every dead thing sleeping within it.

- Y. You bastard! How dare a mere Skeleton Knight…!

- G. A. A. A. A!

Crack!

The fallen knight became the new master of the Black Forest.

And at last, he rose to become a chosen being.

Commander of the Skeleton army.

Skeleton Warlord was his new name.

*So this is what it feels like?*

It was astonishing. Everything around him had changed. He did not know why, but the mana flowing through the Black Forest had grown denser, and immense power surged through his body, despite it being nothing more than bones.

To him, newly reborn as something else, a mere handful of humans was utterly insignificant.

*There aren’t many of them, and they’re all terrified.*

To humans, death was simply another name for fear.

Since he had already become one of the dead, the humans’ fear was nothing but amusing.

*Run. Then bring me more—more lives!*

He was now the master of the Black Forest and the commander of the dead.

The larger groups of humans they brought would soon become his soldiers. Once he commanded thousands, tens of thousands of the dead…

The Black Forest would no longer be enough for him.

Only then could he be reborn not as the commander of the dead, but as a true lord.

*I will leave this place and conquer a wider territory.*

That was when, as he watched the fifty or so humans flee in panic with satisfaction, one of them caught his eye.

*That one…*

A human was surrounded by three Skeleton Knights, exchanging blows with them in a frantic battle.

Strangely enough, unlike the other humans who spoke in a bizarre language, every word that came from this one’s mouth was understandable.

“I’m fine! Hurry up and go!”

How was this possible? Such fluent demon-world speech?

He knew nothing of the System applied to Jin Taekyung, and even less about the Unified Language Pack.

He simply wanted to turn that one—who seemed useful enough for a human—into one of the dead and take him as a subordinate.

- F. O. O. L. I. S. H. H. U. M. A. N.

But he should have known.

The foolish one was himself.

“Phew. They’re finally all gone.”

- …?

He should never have led his entire army into this narrow path.

“You’re all going to fucking die here. That’s all you need to know.”

- W. H. A. T?

He would soon learn the answer to his question.

“One Annihilation.”

Whoooosh!

The moment a whirlwind of blue flame rose into the air, the Skeleton Warlord felt fear creeping over him.

It was an emotion he had forgotten long ago—the fear of death, which had already become his companion rather than something to fear.

- E. V. E. R. Y. O. N. E. D. O. D. G. E—!

The Warlord could not finish speaking.

Blue flames swept through the narrow path and engulfed him and hundreds of Skeletons.

KRAAAAAAASH!

* * *

> **System**
>
> All internal energy and Stamina have been depleted!
>
> Status abnormality: **Exhaustion** has been applied!
>
> Defeated **Level 92 Skeleton Knight**!
>
> Gained a considerable amount of EXP!
>
> Defeated **Level 75 Skeleton Warrior**!
>
> Gained a small amount of EXP!
>
> Defeated **Level 78 Skeleton Mage**!
>
> Gained a small amount of EXP…!

.

.

.

Beep. Beep. Beep.

The System notifications kept drilling into my ears without pause.

My vision spun, and my legs buckled.

I had never imagined the spear shaft in my hand could feel this heavy.

As the spearhead slowly collapsed toward the ground, I barely managed to drive it into the earth and use it to support my body.

*Fuck, I’m dying.*

One Annihilation was the only—and strongest—skill I possessed. It used internal energy and Stamina as fuel to produce more explosive power than anything else.

Unlike the first time, I had gained enough control over the force I imbued into it as my martial arts realm rose. But the aftermath was still devastating.

*One Annihilation is as dangerous as it is destructive. I won’t survive long if I keep thinking in terms of all or nothing.*

The best choice was to draw the greatest result from the smallest amount of power.

As someone who always pursued efficient combat, I could not recklessly use One Annihilation. A final move meant that if it failed, there would be no next move.

But this time was different.

*If I don’t use it now, when will I get another chance?*

A narrow path. Hundreds of monsters packed together without a single gap.

It was practically a stage built for One Annihilation.

I had exhausted my full strength and fallen into the **Exhaustion** status, but there was a contingency for every action.

Beep.

> **System**
>
> Massacre!
>
> Gained a massive amount of EXP!
>
> Level Up!
>
> Gained Points!
>
> All status abnormalities have been recovered!

At the same time as the notification I had been waiting for, a refreshing sensation swept through my entire body.

Whoooosh.

The dantian that had been emptied by the aftermath of One Annihilation filled once more, and strength returned to my trembling limbs.

Only then did my whitened vision clear, allowing me to see the results of One Annihilation.

“Wow…”

I had expected something, but this was beyond my imagination.

I could only marvel at the sight spread out before me.

Crackle. Crackle-crackle.

The narrow path had been widened to twice its original breadth by the force of One Annihilation.

The enormous trees and rocks that had filled the surroundings had been uprooted, and piles of bones engulfed in flames were slowly burning across the blackened ground.

*How many did I send straight to the grave in one shot?*

There were still some that were breathing—

No. They were already dead undead monsters, so I had to correct that to *still moving*.

In any case, fewer than fifty of them were left. Even those were practically incapable of fighting.

*Did I kill… about three hundred?*

Now I understood why the System had called it a massacre.

Of course, compared to that grand choice of words, the EXP it gave me was absolutely pathetic.

“What’s the point of leveling up only once? So stingy.”

Clicking my tongue, I began finishing off the remaining Skeletons.

With the EXP required for each level rising like a mountain, every single trash mob mattered.

- Kreeeek. Krik.

Crack!

I crushed the skull of a Skeleton that was crawling along with both legs missing.

Beep.

> **System**
>
> Defeated **Level 73 Skeleton Warrior**!
>
> Gained a small amount of EXP!

Damn. The EXP really was stingy.

I grumbled as I turned my head to search for the next monster.

Then my eyes flew open, and a warm feeling spread through one corner of my chest.

“Oh. Ohhh. Could that be…!”

With excitement building, I approached the creature buried in the mound of dirt.

A Skeleton, trembling with only its head remaining.

The green ghost fire that had once blazed like a torch had shrunk to a tiny flame, like a candle flickering in the wind. But it was still enough to identify him.

[Level 105 Skeleton Warlord]

I smiled broadly and waved at the skull.

“Nice to meet you, friend!”

- ……

“You were here! Why didn’t you say so sooner? Why were you just sitting there?”

- Krik. Kreeeek?

*Look at this sly bastard, pretending to be a Skeleton Warrior.*

I deliberately raised the spearhead with a disappointed expression.

“Ah, what? You were just a trash mob. I guess I’ll kill you.”

- W. A. I. T!

“Whoa. It can talk. Could it be…?”

- Y. E. S. That. Is. Right. It. Is. I.

The Skeleton Warlord opened its eyes wide and continued.

- Master. Of. The. Black. Forest. Commander. Who. Leads. The. Dead. This. Body. Is. The. Warlord.

“Wow! Warlord!”

- Only. Now. Do. You. Recognize. Me?

“Wow! EXP!”

- … W. H. A. T?

The Warlord sensed something was wrong and hurriedly continued.

- Surely you do not intend to kill me?

*This bastard… Look how smoothly he talks now that he’s desperate.*

“Who said anything about killing? You’re already dead.”

- Could this body not die and die again, a hundred times over?

“…Are you Jeong Mong-ju?”[^1]

*Has this guy actually read the Song of My Single Heart?*

When I stared at him in disbelief, the Warlord began clacking its jaw.

- Human. Instead. Of. This. Why. Do. You. Not. Make. A. Deal. With. Me?

“A deal?”

- That. Is. Right. I. Can. Give. You. Many. Things.

“Lead with an offer.”

- Lead. With. An. Offer? What. Does. That. Mean?

“Tell me what you can give me. I’ll listen and decide.”

The Warlord was silent for a moment, as if thinking hard, then answered.

- I. Am. The. Ruler. Of. The. Forest. I. Shall. Bestow. This. Vast. Black. Forest. Upon. You!

“The Black Forest is ours.”

- …?

“We have exclusive rights to the Gate, so it doesn’t matter.”

- Exclusive. Rights. To. The. Gate? I. Do. Not. Know. What. That. Is. But. Becoming. The. Ruler. Of. The. Forest. Would. Be. Far. Better!

“No, it wouldn’t. I much prefer coming here whenever the monsters respawn and farming them by luring them together.”

- L. Luring. Them. Together? How. Dare. A. Mere. Human. Hunt. Us!

“Yeah. I’m thinking of sending one more on its way right now.”

Crack.

When I tightened my grip around its skull, the Warlord’s jaw began trembling violently as it shouted in panic.

- Wait! Wait! I. Just. Heard. A. Strange. Sound!

“Come to think of it, you don’t even have a cochlea. How can you hear sounds? What a fascinating creature.”

- There. Is. A. Crack. In. The. Crown. Of. My. Skull! If. This. Continues. I. Will. Be. Erased!

“Wow! Fucking sweet EXP!”

- You. Insolent. Wretch! I. Am. The. Ruler. Of. The. Black. Forest. And. The. Commander. Of. The. Dead—

Crack!

- O. Ruler. Of. The. Black. Forest! O. Lord. Of. The. Dead! Please. Show. Mercy!

“….”

*This bastard changes sides at least as fast as Hyuk Mujin.*

It was certainly novel to have such a long conversation with a monster, but it was time to stop playing around.

“Inventory open. Summon dagger.”

Shing.

When I held the dark-blue blade in front of its eyes, the Warlord asked anxiously,

- W-what are you going to do, sir?

“Huh? Nothing much. Close your eyes and stay still. It’ll be over soon.”

- O. Over? What. Do. You. Mean?

“Shh. Keep your jaw still. If even a bone gets cut, the resale value will drop.”

The corpse of the Wyvern I had killed before, One-Eyed Carus, had been worth its weight in gold. But I had no idea which parts of this Skeleton would be valuable.

*Still, a Named Monster’s skull as a decorative piece ought to sell for a pretty penny, right?*

A prize was still a prize. Its bones gleamed with a black sheen and were actually rather beautiful.

I planned to erase him for good first, then collect the bones nearby.

- Wait! Please, wait!

Clack! Clack-clack-clack-clack!

God, this guy was noisy.

Just as I was about to grab the Warlord’s jaw, which kept jerking up and down without pause, he shouted.

- E. E. EXP! I. Will. Give. You. EXP!

“Huh? I’m already here to take it. Will you stay still? Besides, you don’t even know what EXP is.”

- No! I. Will. Give. It. To. You! I. Will. Have. My. Subordinates. Find. It. And. Bring. It. To. You. Somehow!

“What the hell are you talking about? EXP isn’t an item…”

I stopped speaking.

A thought had flashed through my mind.

*Could this actually work?*

“You said you were the master of the Black Forest, right?”

- Y. Yes. Yes, yes!

“How many subordinates do you have?”

- All! All of them! Not right away, but if I search the Black Forest, I can summon more than a thousand!

“A thousand?”

- More than a thousand even at the bare minimum! Have you forgotten who I am?

“A Skeleton Warlord.”

- Y. Yes. No soldier can defy its commander. The lesser creatures would never dare oppose me!

“Hmm.”

- I will find whatever you want, even if I have to search the entire Black Forest—or turn it upside down!

Looking into his green eyes, which flickered with desperate pleading, I organized my thoughts.

The deliberation did not last long.

“Hey.”

- Yes.

“Let’s work together on a job.”

- What. Kind. Of. Job…?

“Something like that. You just have to do what I tell you.”

At my sinister smile, the Warlord’s skull began to tremble.

[^1]: Jeong Mong-ju was a fourteenth-century Korean scholar-official remembered for *Dansimga*, or “Song of My Single Heart,” a poem about unwavering loyalty.
## Chapter artifact 297

# Chapter 297

Inhale. Exhale.

Choi Minwoo took a long, deep breath.

As he accepted the qi permeating the air, he awakened the mass of qi sleeping in his lower abdomen.

*Mana.*

The source of an Awakened's power. Their greatest weapon against monsters.

But Jin Taekyung, the man who had taught him the Jin Family's Cultivation Technique, called mana by another name.

*Internal energy.*

Jin Taekyung was a mysterious man. The more Minwoo saw of him, the more mysterious he became. He had carried out and succeeded at things no one else would have dared to imagine.

There was no way anything taught by such a man could be ordinary.

Dantian, internal energy, circulating his qi, the Jin Family's Cultivation Technique…

Minwoo was surprised every time he encountered another side of Taekyung. This time, however, he was even confused.

*He taught me the Mana Cultivation Method as if it were nothing.*

Choi Minwoo knew how extraordinary the Jin Family's Cultivation Technique was.

No. Any Hunter—or even an ordinary person with the slightest bit of knowledge—would realize it immediately.

If a Hunter was a sword, the Jin Family's Cultivation Technique was a whetstone.

Even a dull sword became sharp when honed against one.

Considering both the technique's effectiveness and its rarity…

Its value would quite literally be astronomical.

*The sheer boldness to casually hand over such an incredible secret art, the skill to defeat a Named Monster alone, the courage not to back down even before Lee Jungryong and the Ares Guild… Is there anyone else like him?*

Day by day, Choi Minwoo was realizing just how remarkable Jin Taekyung was.

And how incredibly lucky he himself was.

*I can't disappoint him.*

That was why Choi Minwoo devoted himself to practicing the Jin Family's Cultivation Technique, even cutting into his sleeping hours.

And the results were appearing even now.

Swoooosh.

He had been so focused on circulating his qi that he had lost track of time. The immense qi flowed through hundreds of acupoints, swelling ever so slightly.

It was an energy whose very existence he had not even known about until a week ago.

For a moment, the conversation he had shared with Jin Taekyung that day flashed through Choi Minwoo's mind.



“Wow, Team Leader.”

“Yes?”

“Did you happen to eat anything good when you were young? Ginseng, perhaps, or one of those round pills?”

“Not at all. My meals were always organic, but I never took anything separately.”

“You probably never even caught a common cold from childhood until now. Right?”

“That is correct. How did you know?”

“Your muscles and bones… No, I mean, your body is just exceptionally well-built.”

“Is that so? But every Hunter should have a good body, shouldn't they?”

“It isn't because you're a Hunter. Your physical abilities are simply outstanding to begin with. In my opinion, perhaps your grandfather did something for his grandson.”

“My grandfather…?”

“Yes. Doesn't anything come to mind?”

“I'm not sure. I was too young, so I don't remember much. Butler Kim told me that my grandfather came to see me once in a while, but… that's all.”

“Hmm. Personally, I think that's the only answer.”



Choi Minwoo suddenly thought of his grandfather. Was the last time he'd seen him before he started elementary school?

The face he remembered was blurry, while the photographs uploaded online were clear. In many ways, the two of them had clearly been far from a close grandfather and grandson.

*But if such a huge mass of energy had been hidden inside me… Could my grandfather really have done something?*

The unexpected trace of his grandfather made Choi Minwoo's heart pound.

As if responding to him, the energy coursing through his body trembled.

The enormous qi Jin Taekyung called *one jiazi*[^1] made one final, sweeping circuit before settling gently into the dantian beneath his navel.

At that moment, Choi Minwoo opened his eyes, a tingling pleasure running through him.

“Phew.”

The afterglow of circulating his qi lingered in his long exhalation.

Choi Minwoo did not know it, but he had just reached Four Stars in the Jin Family's Cultivation Technique. It was an astonishingly rapid achievement, one that was hard to believe he had accomplished in only a week.

Yet it had been possible because Choi Minwoo possessed one jiazi of immense internal energy and such exceptional Muscles and Bones that even Jin Taekyung had nodded in approval.

*The others aren't done yet.*

When Choi Minwoo looked around, he saw three people still absorbed in circulating their qi.

They were seated at regular intervals around the room: Butler Kim, Song Song, and Im Kkeokjeong.

The fact that all four of them were learning the Jin Family's Cultivation Technique was an absolute secret.

They were currently in Choi Minwoo's privately owned training room, which had ironclad security.

*I shouldn't disturb them.*

Jin Taekyung had already drilled the danger of qi deviation into his ears until they practically hurt.

Choi Minwoo slipped out of the training room as carefully as possible, then picked up the cell phone he had turned off for a while.

Less than a minute later, his jaw dropped.

Breaking news was updating across his phone screen at a blinding speed.



- The return of a Named Monster! Korea in crisis!

- An anomaly at the A-rank Gate, **Black Wizard's Black Forest**.

- Jin Taekyung volunteers as bait. Witness testimonies: “He possesses a noble spirit of sacrifice.” “A Benefactor I will never forget.”

- Hunter Association formulating a response and preparing to dispatch a rescue team.

- Peace Guild representative: “We are currently unable to reach the leadership…”

- Netizens unleash criticism over the Association's sluggish response. Jin Taekyung has been isolated for twenty minutes.

- Will a miracle occur?



“W-what is this?”

What did they mean, sacrifice? And what did they mean, isolated?

Jin Taekyung was supposed to be running the Gate with his Guild members. Why were they calling it a sacrifice?

And where had this Named Monster come from all of a sudden?

Choi Minwoo stood frozen with his eyes wide, then hurriedly pulled himself together.

*This isn't the time for this.*

He knew Jin Taekyung's abilities well enough.

But if Taekyung had volunteered as bait and sent his Guild members out first, then he must have been facing an overwhelming threat.

*This is… really dangerous.*

Just as Choi Minwoo gripped his phone hard enough to crush it, the firmly closed door of the training room opened, and three people emerged.

“Ah, that feels refreshing.”

“Uncle, doesn't my skin look better?”

“Ah, Young Master. You were already out—”

“Butler Kim!”

One urgent cry was enough.

The three of them immediately sensed that something serious had happened, and their faces hardened.

Butler Kim calmly asked, “What happened?”

“We have to go to Jin Taekyung. Right now!”

* * *

The entrance to the A-rank Gate, **Black Wizard's Black Forest**, was already swarming with people.

Hunters from the Association and other Guilds who had been dispatched for safety. Even reporters who had come to risk their lives for an exclusive story.

The voices of well over several hundred people filled the area with a constant murmur.

“Do you think Jin Taekyung is dead?”

“It doesn't look good. We haven't heard a thing for an hour now.”

“But he already defeated a Named Monster once…”

“Ah, that Wyvern? He was incredible, sure. He was incredible, but…”

The Senior reporter who had been speaking with his junior tapped the ash from his cigarette.

“You're a Hunter-section reporter in name, so think about it. Didn't you hear the interview with the Peace Guild members who were with Jin Taekyung earlier? They said there weren't just one Named Monster, but several hundred more monsters. That's a completely different situation.”

“It was that bad?”

“Hey, the only reason things have gotten this far is because it's Jin Taekyung. If it were anyone else, we wouldn't even be saying things like ‘probably’ or ‘it's difficult.’ What Hunter do you think could hold out alone for an hour? Rescue preparations, my ass. They'd already be preparing to recover his body.”

The junior reporter let out a low groan.

“So it's really that bad.”

“We're completely fucked. And we're crazy too, hanging around here trying to scribble out an article in the middle of all this.”

“Still, they wouldn't have allowed reporters in if some degree of safety wasn't guaranteed, right?”

“Can't you see them over there? More than thirty A-rank Hunters came.”

The Senior reporter gestured with his chin. Dozens of Hunters who looked impressive at a glance had gathered there.

The ones who stood out most were the Hunters wearing an emblem of a crossed sword and shield over their chests.

“The Ares Guild sent people too.”

“They just got here. They're the kind of bastards who would blow off even the government if they decided the odds weren't in their favor… I have no idea what brought them here.”

“Did they come to rescue Jin Taekyung?”

“Who knows? Maybe. Or maybe they want to swallow up the Named Monster for themselves.”

Named Monsters were worth an unbelievable amount.

Even the Wyvern Jin Taekyung had killed most recently, One-Eyed Carus, had been worth a trillion-won-level sum despite having only just awakened as a Named Monster.

“But… with this many people, shouldn't the rescue operation be starting now? We have enough forces.”

“We do. But I doubt those guys see it that way.”

“What?”

“Never mind. Forget it.”

The Senior reporter fell silent after that.

He had worked in this field for nearly twenty years and was a veteran among veterans. Eyes and ears were everywhere around him, and he had seen and heard plenty as a result.

*Jin Taekyung must have gotten on their nerves.*

He had recently heard some strange news from a reliable source.

There were signs of unusual tension between the Myeongdong and Peace Guilds.

Only a handful of people knew about it, and the rumor had quickly been exposed as nothing more than trash gossip. But the reporter's instincts, honed over many years, whispered that something was happening.

*And then there's the Ares Guild.*

There was nothing strange about Korea's largest Guild stepping forward when a Named Monster appeared.

But something felt wrong. It was an uneasiness he could not explain with words.

The reporter was looking toward the gathered leadership when he suddenly frowned.

*You're going to rub your palms raw, you idiot.*

The Seoul Branch President, who could be considered the person in overall charge of this operation, was busily rubbing his palms in front of a man who looked to be in his thirties.

*What was that guy's name again? Plaster statue? Go Jun?*

He was supposedly the Ares Guild's security team leader. The man was said to be Lee Jungryong's right-hand man, practically no different from the Guild Master himself.

Watching the Seoul Branch President fawn over him as if he would cut out his own liver for the man, the reporter could vaguely understand why the rescue team was being delayed.

“These bastards sure are having fun.”

That was what the Senior reporter muttered in a voice barely loud enough to hear before grinding out his half-smoked cigarette.

“The Peace Guild!”

“What? Where?”

“Hey, hey! Get the cameras ready!”

With the crowd's commotion and the cries of the broadcasting crews, everyone's attention turned toward one place.

Four people.

Three men and one woman carved their way through the crowd like they were parting the Red Sea, then stood before the Gate.

Until Hunters from the Seoul Branch moved to stop them.

“Get out of our way.”

The low, steady voice of the young man at the front, Choi Minwoo, was answered by the Seoul Branch President, who had hurried over.

“Safety has not yet been confirmed. We need more time before we can begin the rescue operation…”

“More time? Here?”

“Just a little longer. Just a little will be enough.”

“Nearly an hour has already passed.”

His voice was calm, but his eyes flickered with flames. The three people behind him looked the same.

“We have to save him now.”

“Not yet. Follow procedure.”

“Whose procedure? The Association's? Or…”

In the brief instant that followed, Choi Minwoo's gaze swept over Go Jun, standing behind the Association president.

Clenching his lips tightly, he continued.

“Withdraw the Association's Hunters. The Peace Guild will enter on its own.”

“You know that would violate regulations.”

The president answered in an authoritative tone and snapped his fingers.

Hunters belonging to the Seoul Association surrounded the Peace Guild members, their expressions openly displeased.

“It won't take much longer. Be patient and wait.”

Those words snapped the last thread of Choi Minwoo's patience.

He shouted as if spitting out a ball of fire.

“My friend is in there!”

Click. Flash!

The cameras captured the scene, and dazzling flashes erupted.

Choi Minwoo paid them no attention. His furious shouts continued.

“He could die! We have to save him!”

When he thought of Jin Taekyung fighting for his life against a Named Monster leading an army of hundreds of Skeletons, his anger erupted like an active volcano.

“Get the hell out of the way, you fucking bastards!”

* * *

The Skeleton Warlord spoke in a majestic voice.

- In the commander's name, I order you. Rise, my loyal subordinates. My army's mighty soldiers!

At that moment, someone struck the Warlord's skull with lightning-fast hands.

Whack!

“Damn it, seriously. That spell is pointlessly fucking long. I told you to make it quick.”

- ……

“Are you not going to answer?”

- …Yes, sir.

The Warlord muttered in a resigned voice.

- Come on, grow. Skeletons, skeletons…

Whoooosh!

Demonic qi burst from the Warlord and spread through the Black Forest.

A bright smile appeared on the young man's lips as he watched Skeletons spring up one after another from the clearing.

“Wow. Another bumper harvest.”

[^1]: *Jiazi* is a traditional sixty-year cycle, used here as a unit of internal energy.
## Chapter artifact 298

# Chapter 298

“Come on, grow. Skeletons, skeletons…”

Beep!



> **System**
>
> - Lv. 105 Skeleton Warlord has used a special Skill!
>
> - Special Skill, Summon the Dead, has been activated!
>
> - The sleeping dead answer the Commander's call!

I had never felt so at ease.

Every time I saw a Skeleton spring up like a bean sprout, happiness welled up in a corner of my heart.

*Is this what it feels like to be a farmer?*

What a bumper harvest. A truly magnificent harvest.

I smiled brightly and swung my sickle—no, my spear—to begin reaping.

Every time I smashed the skull of a Skeleton that had only just awakened, a beautiful sound rang out.

Ding. Ding. Ding.



> **System**
>
> - You have defeated Lv. 71 Skeleton Warrior!
>
> - You have gained a small amount of EXP!
>
> - You have defeated Lv. 70 Skeleton Archer!
>
> - You have gained a small amount of EXP!

The Skeleton Warlord, forced to offer up his subordinates as EXP, muttered in a sorrowful voice.

> - Ah, my soldiers. Forgive your disloyal commander. To be caught in the schemes of a wicked human and erased without even getting to demonstrate your true strength…

I was about to swing my spear at the next one when I suddenly stopped.

“What did you just say?”

> - I called you a wicked human!

Well, look at this guy.

He was supposed to be groveling, yet he glared at me and talked back. The anger of being demoted from commander of the great undead army to EXP factory manager seemed to have driven out his fear of destruction.

> - I would rather be destroyed than offer my soldiers to you!

“Whether you get destroyed or not is for me to decide. More importantly, say what you said earlier again.”

> - Wicked human!

“Not that.”

> - Not that? Then what?

“You said you hadn’t even shown your true strength, right?”

> - …What of it?

“Come to think of it, you have one strange Skill. Something called Commander's Rally, or whatever.”

> - H-how do you know about that?!

“Oh, right. No wonder something felt off. I forgot about that.”

I smiled brightly and patted the Warlord's skull.

“Use it.”

The Warlord asked again, sounding genuinely baffled.

> - Commander's Rally? Why?

“It raises their Levels when they get the buff. I need to squeeze out as much EXP as possible.”

> - …!

“So hurry up and use it. Depending on how you perform, I might even let you go.”

> - R-really?

“There’s a saying in the human world. A man’s word is worth a thousand pieces of gold. It means that a man always keeps his word.”

> - A man who lost his mama? What a strange saying.

“Why would he lose his mama? Making mom jokes now, you fucking bastard? Maybe I should just destroy you.”

Crack.

When I tightened my grip around his head, the Skeleton Warlord cried out in alarm.

> - Wait! There’s a crack in my bone! My bone!

“Lord, I’m sending one up.”

> - Wait!

“So are you going to do it or not?”

The Warlord’s green pupils shifted anxiously from side to side.

For a Skeleton, he displayed a surprisingly wide range of emotions. Before long, he finally managed to force out an answer.

> - I-I’ll do it.

“Good choice.”

> - But do not misunderstand. This is not submission. It is a contract!

“A contract?”

> - That’s right! Not obedience, but a contract mutually agreed upon by both parties!

“…This bastard is more human than I am, despite being a Skeleton. So what are the terms of this contract?”

> - In exchange for cooperating with you, wicked human, guarantee the position I currently hold.

“The master of the Black Forest and commander of the undead army?”

> - Correct! In addition, cease this indiscriminate and barbaric slaughter!

“…”

What had I just heard?

To be told to stop indiscriminate and barbaric slaughter by a monster of all things left my head spinning for a moment.

“Are you out of your mind? Is that something a monster is supposed to say?”

> - How insulting. I am a Skeleton Warlord possessed of cool judgment and intelligence. Though I may have become a fallen undead, the spirit of chivalry is engraved deep within my soul.

“…If you had upheld chivalry, you wouldn’t have fallen like this in the first place.”

> - …The truth is, my memories from when I was alive were erased when I became undead.

“Then don’t go on about chivalry. You’re a real piece of work.”

Still, perhaps because he was a Named Monster, he was definitely different from ordinary monsters that were consumed by instinct and did nothing but howl.

*Anyway, a contract.*

I thought it over carefully before finally opening my mouth.

“Fine. I’ve decided.”

> - Human. Will you accept my contract?

“No. I don’t want to.”

> - …Huh?

As I watched the green light in his eyes shake in confusion, I continued.

“I’m okay with the first proposal. You can be the master of the Black Forest and the commander of the army, or whatever. But…”

> - But?

“From now on, you’re the Peace Guild’s EXP factory manager. In exchange for guaranteeing your position, supply me with as many Skeletons as I want.”

> - That’s absurd!

“Don’t like it?”

> - I would rather be destroyed than become a human puppet!

“Your wish has been received, valued customer.”

Crack.

The Skeleton Warlord, a crack running across the crown of his skull, answered in a solemn voice.

> - On second thought, it is not such a bad contract.

“…”

> - A commander cannot abandon his soldiers. Human, as the master of the Black Forest and commander of the undead army, I accept your proposal.

“You said you’d rather be destroyed than become a human puppet.”

> - When a commander disappears, the army falls apart. Do not misunderstand. I am merely enduring this momentary humiliation for the sake of the soldiers waiting for me.

“But you have to offer up those very soldiers.”

> - I will remember their noble sacrifice until the day I am destroyed. So, how many troops is this month’s tribute—no, how many tribute troops do you require?

“…”

Look at him, giving them away without holding back since he wasn’t the one being destroyed.

At this point, he wasn’t a puppet. He was a snail bride.[^1]

When I stared at him with an utterly dumbfounded expression, the world’s first pro-human Named Monster, the Skeleton Warlord, hurriedly began chanting.

> - Grow stronger, Skeletons, Skeletons!

Beep!



> **System**
>
> - Lv. 105 Skeleton Warlord has used a special Skill!
>
> - Special Skill, Commander's Rally, has been activated!
>
> - The Strength, Agility, and Magic of the monsters under the Skeleton Warlord's command have been enhanced!
>
> - The enemies' Levels have increased by 5!

*…He can do it all by himself now.*

* * *

The harvest was easy.

The first time was difficult, but after doing it two or three times, I got the hang of it.

The Skeleton Warlord made full use of his abilities as a commander to fill his tribute ranks as quickly as possible.

> - Army! Rally together!

Clatter, clatter!

Around a hundred newly grown Skeletons gathered in one place. All I had to do was scatter Spear Energy at the monsters that had gathered at his command, and EXP came pouring down.

Swoooosh! Boom!

Ding. Ding. Ding.

The sound of EXP being deposited made the corners of my mouth rise. Watching the scene, the Warlord muttered in a satisfied voice.

> - Hmm. This is much faster and easier.

“…”

> - Human. Did you see my command ability? This is the dignity of a commander.

What a pro-human bastard.

Watching him take pride in discovering an efficient way to offer up his soldiers, I felt like I finally understood why his soul had become corrupted.

If the winds of liberation ever swept through the Black Forest, the Skeleton independence fighters would put him at the top of their purge list.

*This is giving me the strange feeling that I’m the invader.*

Feeling oddly unsettled, I began collecting the loot.

Skeletons were one of the most dirt-poor monster species around. Their so-called by-products were either rusty weapons that could cause tetanus or half-rotted bones.

You could at least get beef and bone broth from a Minotaur corpse. Apparently, no matter how long you simmered these, all you got was the taste of a grave.

“Oh, a Magic Gem and some Equipment.”

At least Skeleton Knights, which appeared about as often as beans in a drought, sometimes left behind one or two Magic Gems and decent pieces of Equipment, like this.

Of course, even that only happened once in a while.

“With a Magic Gem this size, it should easily fetch tens of millions of won.”

It had been a good decision to send the Guild members away. I got to monopolize the EXP and the Magic Gems too—the best of both worlds.

As I happily pocketed a Magic Gem the size of an adult’s fist, the Warlord asked me a question.

> - Wicked human. What are you doing?

“You can see what I’m doing. I’m collecting the rewards for my labor.”

> - Do you intend to absorb it later?

“Absorb it? Don’t be ridiculous. Of course I’m selling it.”

> - Foolish. Magic Gems are the source of power. Is it not only natural to eat them and grow stronger?

“That’s something monsters like you do. Humans are different.”

It was already well known, but humans were not monsters’ only enemies.

It was perfectly normal for monsters to fight among themselves, and some even ate enemy monsters to grow stronger in the process.

> - Is that so? Humans are truly an incomprehensible lot. You could become stronger by absorbing Magic Gems… Is money really so wonderful?

“Money is something we need whether we like it or not, to get by. Besides, humans can’t absorb Magic Gems.”

The energy contained in Magic Gems was commonly called demonic qi. It was the foundation of a monster’s strength, but to humans, it was no different from poison.

It was a type of qi, but it was easier to understand if you thought of it as a contaminant.

After I gave him a rough explanation, the Warlord tilted his skull.

> - You cannot absorb it? That is strange. The human group I encountered long ago used Troll blood to heal their bodies.

“Ah, potions? That undergoes a purification process…”

> - Then why not purify Magic Gems? Just as you do with the Troll blood you call potions.

“If it were that simple, we would have purified them long ago. You really are simple, just like a monster.”

If Troll blood was a fruit-flavored drink with one percent fruit flavoring, then a Magic Gem was one hundred percent fresh fruit juice.

People couldn’t even remove all the poison from potions, yet this guy was suggesting that they absorb Magic Gems.

I let out a short laugh and continued.

“Anyway, humans can’t absorb Magic Gems.”

> - Why?

“Stop asking questions, you question-mark murderer. That’s the established academic consensus. I’ve never heard or seen anything like that.”

> - I have never heard of a human like you, either.

I was about to smack the Warlord’s skull when I stopped.

*Wait. That actually makes sense.*

*There’s no need to be bound by common sense all the time.*

Was I not an existence beyond common sense myself?

The phrase *established academic consensus* merely referred to a conclusion drawn from what was known.

*The Mana Cultivation Method was the same.*

Only a tiny handful of people knew it existed.

I had never thought about it before getting entangled with the Ares Guild.

Before monsters appeared and after they did, their private league had remained unchanged, and their secrets had continued to be shared within the boundaries they had established.

*Absorbing a Magic Gem…*

*Should I try it once?*

Just as I was about to open my Inventory and take out another Magic Gem, the Warlord spoke.

> - Heh heh. You look like you just got punched. Wicked and foolish human.

“Oh. Do you want me to give your skull an Annihilation Punch?”

> - …A rash remark. I apologize.

“You apologized within three seconds, so I’ll let it slide.”

The Skeleton Warlord, having avoided destruction by the universal rule, muttered.

> - There is no greater humiliation. Consider yourself fortunate that I have not grown stronger, human.

“For a Skeleton Knight, becoming the master of the Black Forest through a coup was quite a career.”

> - I am a Warlord now! The master of the Black Forest and—

“Commander of the undead army. Yeah, yeah. I’m getting calluses on my ears from hearing it.”

I only learned later that he had taken over the Black Forest.

He had actually defeated the black wizard, who was practically the forest’s true master. He must have absorbed a truly incredible amount of Magic Gems.

“So this is a complete human—or rather, Skeleton—victory. Going from an ordinary Skeleton Knight to the master of the Black Forest, and even evolving into a Warlord… You must have absorbed an enormous number of Magic Gems from the black wizard, right?”

> - What are you talking about? He did not possess any Magic Gems.

“Huh?”

> - Besides, the black wizard was the one who summoned me directly. Until recently, his commands were absolute. A summoned creature cannot disobey its summoner.

“Then how…”

> - You mean, how was I able to defeat him?

The Skeleton Warlord’s green pupils narrowed.

> - I do not know the reason myself. Not long ago, I suddenly felt that I had escaped his control. Perhaps you could say that I climbed one step higher when my magical power surpassed that of my summoner.

“Suddenly?”

> - Yes. My magical power grew tremendously, all at once.

What was he talking about?

Yet, just as the Warlord said, he could not properly explain what had happened to him either.

After thinking about it for a long while, the only thing he added was this:

> - Borrowing a human expression, it felt as if I had been possessed by a ghost.

“…Is that something a Skeleton can say?”

*Maybe that bastard isn’t a Skeleton after all.*

It was at that moment, as I stared at the Warlord with an incredulous expression, that—

> - Hmm?

The Warlord’s skull rolled around atop his neck before stopping in one direction.

Looking south with his green pupils shining, he clicked his jawbones and spoke.

> - An intruder.

“An intruder?”

> - I am the master of the Black Forest. I know everything that happens within the forest. More wicked humans have just set foot in my territory.

“They’re my friends, you idiot.”

Whack!

After enthusiastically smacking him across the back of the head, I picked up the Warlord’s skull and started walking toward the Gate entrance.

[^1]: A snail bride is a figure from a Korean folktale: a mysterious spirit who secretly performs household chores for a poor man.
## Chapter artifact 299

# Chapter 299

“It looks like we can begin now.”

The Seoul Branch President’s signal to proceed came more than ten minutes after the Peace Guild, led by Choi Minwoo, had begun protesting.

A Gate was a fierce battlefield where life and death could be decided in an instant. No one expected Jin Taekyung to survive after being left alone against a Named Monster commanding a force of hundreds of Skeletons.

“Do you think he’s still alive?”

“It’s been exactly one hour and eight minutes. We should be grateful if we can at least recover his body.”

“Damn it. This isn’t a rescue operation. It’s a body-recovery operation.”

“Can they really keep doing this? Every second matters, yet they’re dragging their feet.”

“What else can they do? It isn’t an ordinary A-rank Gate. A Named Monster appeared. If you look at it from the Association’s perspective, their position is understandable. If they rush in and a major disaster occurs, it’ll be over for everyone.”

Hunters preparing to enter and reporters filming the entire situation chattered in groups.

Some were furious about the delayed rescue operation. Others defended the Association’s decision.

But no one spoke of Jin Taekyung’s survival. There was no need to add needless words to an obvious fact.

“Still, the Peace Guild really got screwed.”

“Yeah. Jin Taekyung is already… Well, it’s unfortunate, but that’s how things turned out. And the Peace Guild openly raised hell with the Seoul Branch President in front of the cameras. The backlash is going to be brutal.”

“Exactly. That guy’s a political appointee, and he’s already ridiculously sensitive about the media.”

Choi Minwoo’s face grew rigid as he listened to the whispers around him.

The disadvantages the Peace Guild would suffer later?

He didn’t care about any of that.

*Who the hell says he’s dead?*

He wanted to charge out right then and there. He wanted to grab the collars of the idiots spouting nonsense, then knock down the Association Hunters blocking his way.

And yet, he had waited until now because of something Butler Kim had said while restraining him more than ten minutes earlier.

> *Didn’t you say so yourself, Young Master? That you trusted Mr. Jin Taekyung more than you trusted yourself?*

Those words had forcibly cooled his anger.

It was true. Taekyung had always shown them miracles, turning the impossible into the possible. Today was simply another continuation of that.

He had believed it.

He wanted to believe it.

*Isn’t that right, Mr. Jin Taekyung?*

Choi Minwoo took a deep breath and stepped forward. More than fifty Peace Guild members followed behind him, their faces filled with resolve.

“Our Peace Guild will take the lead.”

The Seoul Branch President replied with an unpleasant look.

“That falls under my authority as the commander of this operation. But the way you’re speaking sounds more like a notification than a request.”

“That’s correct.”

“What?”

“Would you like me to repeat myself? I said it was a notification.”

Before the Association President could say anything else, Choi Minwoo continued in a cold voice.

“I have no intention of delaying any longer, and no reason to keep talking with you. The Peace Guild will take the lead.”

“How dare you—!”

The Association President’s face turned red enough to burst.

That was when a toneless voice came from behind him.

“Let them.”

The Association President turned his head.

Standing where his gaze fell was Go Jun, Lee Jungryong’s right-hand man and head of his security team. He had his arms folded and wore an expressionless face.

“Team Leader Seok?”

“Please consider the feelings of the Peace Guild members who have lost a colleague they shared hardships with. The media will look favorably on it as well.”

“B-but there’s a Named Monster inside the Gate. If we put Hunters whose abilities haven’t been verified at the front, something unfortunate could happen…”

The Association President had been about to continue when Go Jun’s dry gaze silenced him.

For a moment, he had forgotten. His opponent was not merely a team leader in the Ares Guild. He was Lee Jungryong’s head of security—and his right-hand man.

More importantly, the “unfortunate incident” Go Jun wanted was precisely what the Association President was worried about.

The Association President’s deliberation was brief.

“Let the Peace Guild take the lead. Then, three minutes later, the Association and the Ares Guild will…”

But Choi Minwoo had already turned around and begun walking toward the Gate.

The gazes of the Association President, Go Jun, and countless others clung to him, but he paid them no attention.

“Let’s go. We’re going to save Mr. Jin Taekyung.”

At Choi Minwoo’s quiet words, a roar thundered across the grounds, loud enough to make their ears ring.

Butler Kim, Im Kkeokjeong, Song Song, and more than fifty Peace Guild members followed Choi Minwoo, cutting through the hundreds of Hunters like a current as they advanced toward the Gate.

That was when a deep shout burst from Butler Kim’s mouth.

“All Peace Guild members, form an attack formation!”

Clack-clack-clack!

Armor and blades flashed in the sunlight as they moved. In an instant, the more than fifty Peace Guild members transformed into a wedge formation and shot forward like a single arrow.

At the very front was Choi Minwoo, charging toward the magic field with a thunderous cry.

“Enter!”

Swoooosh!

Had the Gate’s magic ever felt this unpleasant?

Choi Minwoo opened his eyes with a crawling sense of foreboding in one corner of his chest.

His heart sank.

*This is…*

Scorched earth.

Was there a more fitting way to describe the sight before him?

The trail visible from the hill where the Gate entrance stood was completely engulfed in flames.

*Mr. Jin Taekyung.*

The foreboding he had felt while passing through the Gate seemed to be slowly taking shape.

Im Kkeokjeong spoke from behind him in a trembling voice.

“Team Leader Choi. Could Taekyung have…”

“Stop. We’re in the middle of an operation. Jumping to personal conclusions is prohibited.”

But this time, even Team Leader Choi’s words failed to give them strength.

The situation before them looked that hopeless. Im Kkeokjeong wasn’t the only one shaken. Every Peace Guild member was in turmoil.

*No. That can’t be.*

Choi Minwoo bit down hard on his lip as if to steady himself, then moved forward with heavy steps.

“We’re continuing our approach. Don’t lower your guard, and keep advancing.”

Preparing for the possible appearance of monsters, they cautiously moved forward.

And yet, the closer they came to the trail, the deeper the despair felt by the Peace Guild members grew.

“This can’t be.”

A mountain of broken bones and weapons. Ash blanketing the blackened earth.

There was no trace of life anywhere in that place, where only death and destruction flowed over everything. The same was true of the one person they had desperately hoped to find.

*Dead? Him?*

One question flashed through everyone’s mind.

The longer someone had known Jin Taekyung, the more blankly they blinked at this unbelievable reality.

In the suffocating silence, Butler Kim’s words sounded like a doctor’s final verdict.

“According to the results of the detection magic… we found no movement or living creatures within a three-hundred-meter radius.”

Choi Minwoo’s eyelids trembled.

“You mean…”

“I’m sorry.”

Butler Kim answered with a devastated expression and extended his hand. From the direction toward which his fingertips pointed, something rose into the air and slowly flew toward them.

“That’s…”

“Judging by the considerable magic I can sense from it, it appears to be a trace left by the Named Monster.”

The object in Butler Kim’s hand was a palm-sized metal fragment.

Its black sheen had not faded despite being covered in ash. When a skull emblem that looked terrifying even at a glance came into view, several people sucked in startled breaths.

“The skull emblem! Th-that’s the armor the Named Monster was wearing!”

“That’s right! We saw it clearly.”

Then someone searching the area shouted as if screaming.

“There’s a dagger here too! That isn’t equipment used by Skeletons!”

“It belongs to Senior Jin Taekyung. It’s the one he used all the time.”

In the atmosphere shrouded by shock, Butler Kim spoke in a subdued voice.

“It appears he was oxidized along with every enemy, including the Named Monster…”

“……!”

The air surrounding the trail seemed to crackle.

Now everything was certain. Jin Taekyung was dead. He had thrown away his own life, taking his enemies with him as companions on the road to the afterlife and leaving his comrades behind.

It was Im Kkeokjeong’s wail that finally broke the silence that seemed as if it would never end.

“Ghk. Nghh…”

The small tremor that began in his hands climbed up through his arms, shoulders, and back before spreading throughout his entire body. Tears poured from Im Kkeokjeong’s large eyes.

“Taekyung… Taekyung…”

No one mocked him as his massive frame shook with sobs.

The size of their grief might have differed, but everyone there felt the same.

Grief over Jin Taekyung’s death. Guilt that they had been unable to fight alongside him. And the helplessness they felt toward themselves.

The Peace Guild members’ eyes grew red and bloodshot, while tears ran down Butler Kim’s and Song Song’s cheeks.

Only one person did not cry: Choi Minwoo.

*He’s dead. Jin Taekyung is dead.*

With dark eyes, he looked around the trail, where acrid smoke still rose into the air.

It felt as though Taekyung might be hiding somewhere even now, ready to spring out like a jack-in-the-box.

*I thought you would survive any situation.*

His chest suddenly felt tight. It was the first time he had felt this way since losing his parents.

His grief swelled like a balloon, stretched taut as if it might burst at any moment.

That was when a voice drifted over.

“My, what a gruesome sight.”

“Jin Taekyung is nowhere to be seen. It seems he really is dead.”

Choi Minwoo slowly turned around. Hundreds of people had just entered the trail and come into view.

At the front of the Association and the Hunters who had participated in the rescue operation stood two men.

“It looks like the rescue operation has failed. Wouldn’t you agree, Association President?”

“Indeed. Everything’s been reduced to ash. I wonder if we’ll even be able to find the body. That aside, where is the Named Monster?”

“We’ll have to search thoroughly, but according to the detection magic, it appears all the problems you were concerned about have been resolved.”

At Go Jun’s words, the Association President’s heavily furrowed face opened into a broad smile.

“Oh, that’s welcome news. I thought we might have another casualty on our hands.”

“We were able to reduce the casualties thanks to your judgment, Association President.”

“What are you saying? This was all thanks to the Ares Guild stepping forward. Once everything is wrapped up, I’ll make absolutely certain that you receive a commendation plaque. Ha ha. It’ll be the first achievement of my term, so I’m thinking of holding a grand ceremony… Guild Master Lee Jungryong will be there too, won’t he?”

“He’s not the Guild Master. He’s the Vice Guild Master.”

“Ah, right. Goodness, I’ve been getting so forgetful lately.”

A dry smile appeared at the corner of Go Jun’s mouth.

“That can happen. And when the commendation plaque is presented, the Vice Guild Master will be delighted to attend as well.”

“I’ll get to see him again after all this time. Please put in a good word for me, Team Leader Seok.”

“I’m sure he’ll be greatly pleased even if I simply pass along exactly what I saw and heard.”

“Ha ha.”

The conversation between Go Jun and the Association President was a sharp needle—a needle capable of popping Choi Minwoo’s ballooning emotions.

“Shut your mouth.”

“……!”

Every sound came to an abrupt halt.

The Association President belatedly realized what he had heard, and his face twisted in rage. But Go Jun was one step ahead of him.

“You should watch your mouth.”

“I told you to shut it.”

“Young man, you don’t know the meaning of manners. Don’t you agree, Team Leader Choi Minwoo of the Peace Guild?”

His words had a barb.

To Go Jun, Choi Minwoo was a kite with its string cut. The Ares Guild, founded by his grandfather, was as good as being in Lee Jungryong’s hands already. And now that Jin Taekyung, the troublesome figure, was dead, there was no reason to keep his fangs hidden.

“I understand that you’re upset over the death of a Guild member, but you seem to need to calm down.”

Choi Minwoo muttered through clenched teeth.

“You could have saved him if you hadn’t dragged your feet.”

“We did our best. The Association President’s judgment was correct, too. And…”

Go Jun continued in his dry voice.

“You people bear responsibility as well. Don’t you agree?”

“……!”

“What were you doing when Jin Taekyung died? Leisurely reading a newspaper in your office? Or sitting in a bar since noon?”

Choi Minwoo bit his lip. Every word Go Jun said was true.

Because he trusted Jin Taekyung, he had abandoned everything else and devoted himself to training.

But…

At least he should not have done that.

Another needle flew at him as he struggled to speak.

“You killed Jin Taekyung. All of you killed him—the pathetic weaklings who forgot your duty.”

“……!”

Go Jun let out a short laugh.

“It’s too late to regret it. The dead don’t come back.”

That was when Choi Minwoo clenched his fists so tightly they felt ready to burst.

“What the fuck are you saying, you motherfucking bastard?”

A low but powerful voice pierced everyone’s ears.

Those who did not recognize the voice were bewildered by the sudden profanity. Those who knew it froze like stone statues.

*No way…*

Choi Minwoo slowly turned his head.

Far away, one person was trudging down the trail toward them.

“You finished the whole forty-ninth-day memorial rite while I was off taking a piss, you fucking bastard.”[^1]

Jin Taekyung spat out a wad of phlegm.

“Bring it, you son of a bitch.”

[^1]: *49jae* is a Korean Buddhist memorial observance culminating on the forty-ninth day after a person’s death.

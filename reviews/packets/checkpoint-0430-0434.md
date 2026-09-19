# Checkpoint Review — 430–434

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

# Chapters 430–434

## Plot

Jin discovers that the Arch Lich’s magic-circle fragments share patterns and symbols with the Moving Formation from Murim. The assembled circle appears to have absorbed life force to accumulate mana, but neither Jin nor the Skeleton King can decipher its symbols, and the System offers no explanation. Jin recognizes possible links among the formation, the Arch Lich’s circle, phenomena involving the Blood Lord and Western Heaven Demon Lord, and his junk capsule.

At the ruined city, Go Jun confronts Jin over Lee Jungryong’s death. Jin admits killing Lee and Wu Heixing, defeats and mutilates Go Jun, but spares him and demands that Ares Guild’s retaliation end with Lee. Magic Johnson learns the truth, accepts Jin as a friend, and agrees to protect Jin’s people and support his growth. Jin plans to exploit Ares Guild’s leadership vacuum while strengthening Peace Guild rather than starting an open war.

Twenty days after the Small Cataclysm, Jin secretly helps rescue survivors in Sichuan but is exposed during a live CCTV broadcast, turning his denial and irreverent remarks into a sensational international scoop. After reuniting with his mother, Hayeon, and his allies, Jin departs China aboard a chartered aircraft. Chairman Shao Yang confirms that Jin’s fifty-trillion bounty will be paid and reveals that Xiao Shen is his grandson. Jin logs in during the flight and begins returning to the other world.

## Continuity

- The Arch Lich’s magic-circle fragments can be assembled into a massive circle whose patterns and symbols match the Moving Formation from Murim.
- The circle’s apparent life-force absorption and mana accumulation remain the Skeleton King’s inference, not a confirmed decipherment.
- The connection among the two worlds, the Moving Formation, the Arch Lich’s circle, the battle phenomena, and Jin’s junk capsule remains unresolved.
- Go Jun survives Jin’s retaliation but is grievously mutilated. Jin deliberately spares him, and three immobilized A-rank Ares Hunters remove him from the scene.
- Magic Johnson knows Jin killed Lee Jungryong and Wu Heixing, accepts Jin as a friend, and has agreed to protect Jin’s people and aid his growth.
- Jin intends to use Peace Guild’s growth and Ares Guild’s leadership vacuum to encourage defections and weaken Ares without openly declaring war.
- Chairman Shao Yang is purging Wu Xueming and leading Crown Prince Party figures while reorganizing the military.
- Jin’s mother and Hayeon have left China with him aboard the chartered aircraft.
- Xiao Shen is Chairman Shao Yang’s grandson, and Shao Yang has promised Jin’s official fifty-trillion bounty.
- Jin has logged in aboard the departing aircraft and begun returning to Murim/the other world.
- Wei Fenghu continues grieving Lei Fei while maintaining a respectful relationship with Jin.
- The Skeleton King continues pursuing a human identity as Stone-King and may remain concealed in Jin’s Inventory or an extradimensional pocket.

## Translation Decisions

- Render **移动阵** as **Moving Formation**, **小格局变动** as **Small Cataclysm**, and ** 아공간 포켓** as **extradimensional pocket**.
- Use **Magic Johnson**, **Skeleton King**, **Stone-King**, **Golgoli**, **Chairman Shao Yang**, **Xiao Shen**, **Faye Chen**, and **Team Leader Choi**.
- Render **형님** as **hyung** when Xiao Shen addresses Jin.
- Preserve Jin’s dry, profane, self-deprecating voice; the Skeleton King’s grandiose, Internet-influenced insults; and Magic Johnson’s familiar tone.
- Keep the circle’s function explicitly uncertain, using **life-force absorption** rather than presenting it as established fact.
- Use **mental-manipulation magic** or **memory-manipulation magic** for the prohibited technique.

## Durable state

{
  "active_continuity": [
    "The Arch Lich's magic-circle fragments match the patterns and symbols of the Moving Formation Jin saw in Murim, and can be assembled into one enormous circle.",
    "The circle appears to have absorbed human life force to accumulate mana, but this remains the Skeleton King's inference rather than a confirmed decipherment.",
    "Jin suspects that the Murim formation, the modern world's magic circle, the battle phenomena involving the Blood Lord and Western Heaven Demon Lord, and his junk capsule are connected.",
    "Magic Johnson knows Jin killed Lee Jungryong and Wu Heixing, accepts Jin as a friend, and has agreed to help protect Jin's people and support his growth.",
    "The Skeleton King remains hidden in Jin's Inventory or an extradimensional pocket when necessary and continues pursuing a human-world identity as Stone-King.",
    "Chairman Shao Yang has begun a political purge against Wu Xueming and leading Crown Prince Party figures, accompanied by a sweeping military reorganization.",
    "Jin's mother and Hayeon have left China with him aboard the chartered aircraft.",
    "Jin is using Ares Guild's leadership vacuum and Peace Guild's expected growth to encourage defections without openly declaring war.",
    "Chairman Shao Yang is Xiao Shen's grandfather and has promised Jin's fifty-trillion bounty after Jin saved Xiao Shen.",
    "Jin has logged in aboard the departing aircraft and begun returning toward the other world."
  ],
  "continuity_sources": [
    434,
    433
  ],
  "open_questions": [
    "What do the shared patterns and symbols represent, and why did the Arch Lich possess a circle matching the Moving Formation?",
    "What connection links the two worlds, the battle phenomena, and the junk capsule?",
    "How will Magic Johnson respond to what he now knows about Jin and the magic circle?",
    "How will Ares Guild's leadership vacuum affect its Hunters and influence?"
  ],
  "safe_through": 434,
  "temporary_decisions": [
    "Render 매직 존슨 as “Magic Johnson,” 스켈레톤 킹 as “Skeleton King,” 스톤-킹 as “Stone-King,” and 골골 as “Golgoli.”",
    "Render the suspected function of the circle as “life-force absorption” while preserving the uncertainty of the inference.",
    "Use “mental-manipulation magic” or “memory-manipulation magic” for 정신 조작 마법 and preserve its status as a serious felony.",
    "Preserve Jin's dry, profane voice and the Skeleton King's grandiose, Internet-influenced insults.",
    "Render 아공간 포켓 as “extradimensional pocket.”"
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 430

# Chapter 430

My eyelids began to tremble before I even realized it.

*Why is this here…?*

I remembered it clearly.

Immediately after the Sichuan Blood History—after the Western Heaven Demon Lord had nearly killed me several times—I had followed the Sect Leaders of the Qingcheng and Emei Sects to a cave in an unnamed cliff.

The space hidden behind the Mystic Gate Formation had been truly vast, and a gigantic formation had been carved into its center.

A formation filled with strange patterns and symbols, printed in color on the paper I was holding now.

But… could that thing, which the Sect Leaders of Qingcheng and Emei had named the Moving Formation, still be called a formation?

I hurriedly shoved the paper toward Magic Johnson.

“Johnson. This—what is this?”

「Huh? What?」

“Why is this here…? No, where did you get it?”

Taken aback by my sudden reaction, Magic Johnson answered with a bewildered expression.

「It’s a magic circle discovered in the city the Arch Lich used as its base.」

“A magic circle?”

「Yes, a magic circle. I was already in the middle of researching it because of this… Why? Jin, have you seen it somewhere before?」

“Are there more?”

「Of course. Every sheet of paper I was looking at before you came in is related to it.」

“What?”

Then everything piled up on the desk was related to it?

I looked at the several dozen sheets of paper scattered across the floor.

“Excuse me for a moment.”

「Jin? Jin?」

“Has he finally gone mad? How tragic, you vile and ugly human.”

I paid no attention to Magic Johnson’s flustered calls or the Skeleton King’s nonsense.

With my mouth pressed tightly shut, I rapidly skimmed through the stack of printed papers.

Each sheet contained its own patterns and symbols. After examining all of them, I realized one thing.

*This is…*

There was no mistake. The strange patterns and symbols were identical to the ones I had seen in Murim. Their arrangement and orientation were merely different.

And if I assembled all these papers together like pieces of a puzzle, they would form one enormous magic circle.

*What the hell kind of situation is this?*

It felt as if someone had struck the back of my head with a sledgehammer.

I stared silently at the papers for a long time before finally opening my mouth.

“You said this was discovered at the Arch Lich’s base, right?”

Magic Johnson had a cigar between his lips by then. When I looked at him and asked, he exhaled smoke before answering.

「That’s right. I didn’t even know something like this existed at first, but it seems to have been discovered soon after the investigation team was deployed. I received it through the coalition forces on the second day.」

“You received it?”

「They asked for my advice. They couldn’t figure out exactly what kind of function the magic circle had, either. They probably contacted the other two as well.」

The other two were probably the Grand Mages besides Magic Johnson. They were the greatest mages alive and true experts in the field.

And that meant this magic circle was a new kind that had never been revealed before.

“So, did you figure anything out through your research?”

「Not precisely yet, but I’ve gotten a general idea of the magic circle’s purpose.」

“Its purpose?”

「Yes. Fortunately, I have a friend who knows quite a bit about that sort of thing.」

I was just about to ask who he meant when someone suddenly interrupted in an arrogant voice.

“That would be this very body. The universe’s most insanely handsome man, born in Atlanta, Georgia, United States. Known as Stone-King.”

That was right. Why had I forgotten about this bastard?

He was a native of the Demon Realm and a Named Monster, so he was bound to know something.

I pressed the Skeleton King, who was spouting nonsense.

“Quit talking bullshit and tell me what you know.”

“Call me Mr. King from now on, and I shall consider it.”

“Mr. King, my ass. You kumquat-looking bastard.”

“Fucking Korean.”

“You son of a bitch.”

“Whoa, whoa!”

When I raised my hand, the Skeleton King instinctively scurried backward and shouted in alarm.

“All right! I said all right!”

“Talk, you bastard.”

The Skeleton King regarded me warily before opening his mouth.

“It appears to be a magic circle for absorbing life force.”

“Absorbing life force?”

“That is correct. It seems the Arch Lich used it to absorb the energy of other humans and accumulate power. With all that mana gathered, it was able to control countless monster legions and open Gates.”

China was a vast continent.

Even after suffering enormous casualties during the Great Cataclysm, it still had a population equivalent to one-fifth of the world’s total.

And the population living in Sichuan Province alone was approximately eighty million—according to official statistics, at least.

The monster wave had caused casualties numbering in the millions. If the people who had yet to be officially counted were included, the number would swell to something truly enormous.

*And a considerable number of those people must have been sacrificed to provide mana. Considering the scale of what that bastard had done, it all adds up.*

I bit down hard on my lip and asked the Skeleton King again.

“Are you sure?”

“That is merely my personal inference. I cannot guarantee it.”

“Why not?”

The Skeleton King clicked his tongue.

“Vile human. Can you determine the meaning of magic circles used by other humans simply by looking at them?”

“That’s…”

“Of course you cannot. This body is no different. I can raise and command soldiers according to the abilities granted to me, but I cannot wield dark magic like this.”

Damn it. He was completely right.

Just as Hunters and monsters were classified according to their individual traits, the Skeleton King possessed only that much ability.

His answer wasn’t what I had hoped for, and I could not help feeling deflated. But one important question remained.

“Then how did you guess that it was a life-force absorption magic circle? Can only monsters recognize patterns and symbols like these?”

If the Skeleton King knew these strange patterns and symbols, and if I could learn what they meant from him, I might finally be able to identify the formation I had seen in Murim.

I looked at the Skeleton King expectantly, but the answer that emerged a moment later left me utterly deflated.

“I do not know what those things mean. I could guess what the magic circle was for only because I’m undead.”

The Skeleton King pointed at Magic Johnson and continued.

“When I first saw something like this on paper, I did not know what it was. But when I visited the site with that human I’m grateful to, I could sense it clearly. I could smell countless deaths—more than even I could guess at. That was when I first realized it.”

“Oh…”

I could not hide my disappointment.

If even Magic Johnson, a Grand Mage, and the Skeleton King, a Named Monster, could not understand them, then figuring out the meaning of those patterns and symbols right away was practically impossible.

*Damn it.*

What on earth was happening?

The formation carved into the center of the cave. The patterns and symbols that had appeared in the magic circle discovered this time. The bizarre phenomena I had witnessed during my battle with the Blood Lord and the Western Heaven Demon Lord…

I desperately denied the ominous thought that flashed through my mind.

*That can’t be. It’s impossible.*

Was this a coincidence? Or was it fate?

And if it was fate, what did this connection that had appeared out of nowhere mean?

After pacing silently around the suite for a long time, I suddenly spoke.

“I need to see it in person.”

「Huh?」

“Hmm?”

“Johnson. I can visit the site that bastard went to, right?”

Magic Johnson thought for a moment before nodding.

「It’s classified, but you should be allowed to go, Jin. However, only the two of us can show ourselves. We’ll have to take that friend in an extradimensional pocket, like last time.」

“That’s good enough. Let’s leave right away.”

「All right, let’s do that. It seems Jin knows something, too.」

Just as Magic Johnson and I were about to set off, the Skeleton King interrupted in a dignified voice.

“I apologize for interrupting, humans, but this body has pressing business. You two may go without me.”

“……?”

「……?」

“The female employee at the hotel front desk is exceptionally beautiful. Though covered in human skin, the curves of the skeleton beneath it are exquisite.”

I quietly asked,

“So?”

“What do you mean, ‘so’? I am informing you that I shall be spending the night out today. You should keep that in mind. Now, I must go arrange a date with the beauty… But, vile human.”

“What?”

“May I ask why you suddenly took out a spear?”

“Ah, this?”

I casually waved White Flame, which I had somehow already pulled from my Inventory.

“It’s nothing. I was going to stab you when you turned around.”

“I see.”

“Exactly.”

“……”

“Why aren’t you leaving? The employees will be getting off work soon. You should hurry and persuade her to have dinner with you.”

The Skeleton King hesitated, and an awkward smile formed around his mouth.

“Come to think of it, I suppose I can take my time making a move on her.”

“Wow, then you’ve got some free time. In that case…”

I smiled brightly and pulled out one of the extradimensional pockets I had acquired to conceal the existence of my Inventory from other people.

“Get in there, asshole.”

“……Uh-huh.”

The Skeleton King answered dejectedly and slipped inside the extradimensional pocket.

* * *

The moment I saw the magic circle with my own eyes, I understood what the Skeleton King had meant.

Or perhaps it only seemed that way because I had heard his explanation immediately beforehand.

Regardless, the sight overwhelmed me, and one word surfaced in my mind before I could stop it.

*Death.*

It was a dark magic circle so enormous that the one I had seen in the cave could not even compare.

Although its mana had been cut off and it had lost its original function, even the traces of death left behind by the countless lives it had once claimed had not disappeared.

And… that was all I could feel.

「Jin. What do you think? Do you have any idea what it is?」

“No. Not at all.”

The patterns and symbols, arranged in an incomprehensible sequence, were still impossible to decipher.

Just as it had in Murim, the System remained silent. After wandering around the area for several hours without gaining anything, I had no choice but to turn back.

“Mr. Johnson, and Jin. We prepared an escort so you won’t encounter any inconvenience on your way back…”

“We’re fine.”

“Yes. Then I hope to see you again next time.”

We left the security chief and his guards behind. They had given us a salute at an angle sharp as a knife.

After confirming that no one was nearby, Magic Johnson quietly moved his lips.

「Jin. You knew something, didn’t you?」

“…A dream. I think I saw something similar in a dream.”

「Hmm.」

“Johnson. Can I look around by myself for a moment?”

「Of course. How long do you think it’ll take?」

“I’ll be back soon.”

I began walking slowly through the ruins.

Although it was well past midnight, the city was as bright as noon, and countless people and machines were working to clear away the ruins.

Similar work was probably underway throughout the cities caught up in the war.

*Sichuan would be the same.*

China’s Sichuan and Murim’s Sichuan were completely different worlds. Murim was not the modern world’s past, and the modern world was not Murim’s future.

But a connection linking those utterly different worlds had appeared—and this was not the first time.

*The capsule.*

Everything surrounding me had begun with the junk capsule I had picked up at a recycling center.

*How? Why? For what reason?*

Each step brought new questions to mind, leaving my thoughts in complete disarray.

“Phew.”

At my deep sigh, the Skeleton King—who had been moved from the extradimensional pocket into my Inventory—asked,

“Are you all right, vile human?”

“Are you worried about me now?”

“No. If you are all right, let us return to the hotel quickly. Johnson told me a few days ago that there’s a club nearby with a great crowd.”

“……”

*Give me back my touching moment, you lunatic.*

I considered telling him that the club Johnson had mentioned was a gay bar, but held my tongue.

“Forget it. What do I expect from you?”

“When are we returning?”

“I’m going, you bastard. I said I’m going!”

It happened at that exact moment.

“Where are you in such a hurry to go? Hell?”

At the sound of the voice—harder and colder than ever before—I slowly turned around.

Without realizing it, I must have ventured deep into the ruins. Beyond the relatively dark ruins, a familiar figure was making his way through a collapsed building toward me.

“Hell is where your old man went. If I die, I’ll go to heaven.”

The eyes of Go Jun—the Disciple of Lee Jungryong and Head of Security—settled into a cold, icy stare.
## Chapter artifact 431

# Chapter 431

“Vile human. Who is that human?”

So there is one. A human with no sense of fear.

I muttered inwardly and slowly looked around.

The desolate outskirts were far from the center, abandoned by everyone. Even the light illuminating the city as brightly as day had yet to reach this place.

And from among the ruins, a single person came walking out, casting a shadow.

“There must be some kind of connection between us. We keep running into each other.”

Go Jun answered my greeting in a cold voice.

“Not a connection. Bad blood.”

“Then what should we call the fact that we happened to meet in a place like this? Coincidence?”

The answer that came back was as sharp as a blade.

“Inevitability.”

“Clear enough. So have you been following me around like a stray dog since earlier?”

“When did you realize?”

“Since the Stone Age, you bastard. You stared at me so much that I thought you were going to bore holes in my face.”

I had felt the gaze of someone secretly watching me immediately after I came out from examining the magic circle.

It was an unpleasant, sticky gaze, completely different from the curious and admiring eyes of the others.

And at a time like this, there were very few people who would show hostility toward me.

“Either you or those Crown Prince Party Chinese bastards. But the latter are too busy cleaning up the shit they’ve scattered everywhere… It was obvious, wasn’t it?”

That had clearly struck the mark, but there was not the slightest trace of surprise on Go Jun’s face.

“As expected. So that’s how it was.”

“As expected?”

“I thought you would notice. Otherwise, you wouldn’t have left Magic Johnson behind and come all the way out here alone.”

Well, look at this bastard.

Only then did I understand why Go Jun hadn’t been surprised. He had sent me a signal. A signal to follow him.

This wasn’t surveillance, nor was it a lure. It was the scene both Go Jun and I had wanted.

Of course, the outcome of this meeting would be very different from what he expected.

“There’s something I want to ask.”

Go Jun didn’t wait for an answer. He stared straight at me and simply continued with what he had come to say.

“Was it you?”

It was a short, simple question, but there was more than enough meaning packed inside it. I tilted my head and asked back with an innocent expression.

“What was?”

“You know.”

“You don’t happen to think that I killed Uncle Jungryong, do you?”

At the sound of Lee Jungryong’s name, Go Jun’s eyes shook violently. Without waiting for his answer, I covered my mouth with both hands.

“My God, how could you have such a horrible thought? Are you serious?”

“Stop that disgusting act. Do you think I’m asking because I don’t know?”

“Then why are you asking? Didn’t you watch the press conference?”

“I did. You spouted nothing but nonsense and lies from beginning to end.”

Drip. Drip.

Drops of blood fell from the fist he had clenched so tightly that it had turned white. Go Jun glared at me with eyes burning with rage.

“There are only two people here—you and me. Tell me the truth with your own mouth.”

“Vile human. How dare you leave this Atlanta-born Stone-King out of it!”

One more monster for the count.

More precisely, two people and one monster. Though I wasn’t sure whether the Skeleton King could still be called a monster.

“Hm.”

I scratched the back of my head while looking at Go Jun, then opened my mouth.

“That’s right. I killed him.”

“……!”

“Lee Jungryong and Wu Heixing. I took care of both of them. Those lunatics came up with a ridiculous scenario. They planned to kill only me without even touching the Arch Lich. And the result… You know what happened, right?”

An assumption and the truth were two entirely different things.

Even if he had already guessed the truth, hearing a definite answer from the mouth of his enemy was a completely different matter.

I drove the final nail into the coffin for Go Jun, whose body was trembling violently.

“They were that kind of people. What else was I supposed to do? I bought both of them tickets to the United States. Ah, I gave Uncle Jungryong first class.”

“You—you dared to do that to him…!”

Whoosh!

The killing intent erupting from Go Jun’s entire body froze the air around us.

I stared at his fingers twitching toward the hilt of his sword, then abruptly opened my mouth.

“What do you think you’re doing?”

“……!”

Go Jun’s eyes widened. At the same time, the killing intent swirling around us vanished as if it had been washed away.

No—it had been crushed beneath the wave of qi flowing from me.

In the space where the dominant force had changed in an instant, I slowly began to walk.

“You’ve improved by leaps and bounds since the last time I saw you. If you think about it, you’re far better than Wu Heixing. Just what I’d expect from the Disciple Lee Jungryong trained at his side.”

Step.

“With that said…”

Step.

With every step I took, Go Jun’s face grew paler.

The gap between our powers was overwhelming. A rabbit could not defeat a tiger. The moment he made even the slightest movement to draw his sword, my teeth would sink into his neck.

“You should look at where you’re lying before you stretch out your legs. What are you doing, settling into a grave?”

Bang!

Compressed air exploded from the tip of a finger I had raised leisurely.

With a sharp crack, a single stream of Finger Qi shot toward Go Jun, who had frozen like a stone statue. And then—

Clang!

It sent the sword strapped to his waist flying far into the distance.

Watching Go Jun’s frozen expression twist while his eyes remained wide open, I let out a short laugh.

“What? Did you think I was going to kill you?”

“……Why?”

“If you want to die that badly, come more secretly and be ready to truly die. Don’t set up a half-assed trap like you did today.”

I thrust out my hand like lightning. Go Jun didn’t even have time to react.

Bang!

The three streams of Finger Qi I fired pierced somewhere beyond the thick darkness. A moment later—

Thud-thud-thud!

Three unconscious black shadows fell from the air in the distance, accompanied by faint impacts.

Each one was a high-level Hunter who had trained in stealth abilities and concealed himself with various kinds of magic, but none of them could evade my Qi Sense, sharpened even further by the opening of my Middle Dantian.

“Were you secretly filming me, you hidden-camera bastard?”

Tap. Tap.

Clicking my tongue, I tapped Go Jun on the cheek. A voice full of spite slipped between his clenched teeth.

“Do you think you people will get away with this?”

“You people?”

“We—the Ares Guild—will not fall. We will definitely avenge that person’s death…”

Smack!

Blood spattered together with teeth. I gripped Go Jun tightly by the collar and slapped him across the face again.

Smack!

One more time.

Smack!

Again.

Smack!

Inner-Family Heavy Hand.

Rather than tearing through his bones and flesh, the internal energy in my palm burrowed into Go Jun’s body and rattled his brain.

I grabbed the throat of Go Jun, who staggered helplessly, unable to keep his balance like a drunken man.

“Remember what I’m about to say. Remember it clearly.”

“Ghk!”

A bloody foam burst out with his groan and splattered across my face. An unfamiliar man was reflected in his unfocused eyes, his expression numb as he continued speaking.

“You started this, but I’ll be the one to finish it.”

In the end, the modern world was also ruled by the logic of power.

The abilities possessed by superhumans called Hunters—or the power held by those with equivalent authority—allowed them to set the rules according to their own tastes and break them without hesitation. No matter what they did, they were never given a yellow card or a red card.

When Lee Jungryong cut off Uncle Kkeokjeong’s arm to keep him in check, that had been perfectly natural to people like them. But—

“You shouldn’t have done that.”

Now that a new referee had entered the game, the rules had to change as well. And the new rules were very simple.

I pressed Go Jun’s Mute Acupoint and muttered quietly.

“An eye for an eye. A tooth for a tooth.”

I twisted both his arms and pulled with all my strength, as though wringing out laundry.

Crack-crack-crack!

With a horrible tearing sound, two arms came away from his body.

An enormous amount of blood poured out, and the whites of his bulging eyes showed. A silent scream spilled from his mouth, its Mute Acupoint sealed.

“It’s not over yet.”

I shoved my fingers into the ragged stumps of his arms. The Scorching Yang Qi in my hand seared his flesh, inflicting even greater pain. I pinned down his writhing body and grabbed him by the ankles.

“This won’t be enough for someone like you.”

Crack!

The Strength in my body could grind even a thousand-geun boulder into powder. The bones forming both his legs shattered in an instant, splitting into hundreds of pieces.

“……!”

He struggled without making a sound.

I poured internal energy into Go Jun’s body as he passed out from unimaginable pain.

When the light returned to his fading eyes, I smashed his shattered legs with my fist.

Boom! Boom! Boom!

By the time I finally stopped punching, what lay sprawled across the ground was no longer a human being but a large lump of meat.

The faint breath leaking from his nose and mouth was the only proof that he was still alive.

The Skeleton King, who had watched the entire scene from inside my Inventory, spoke in a trembling voice.

“Human.”

I answered in a dry voice.

“What?”

“N-No, it’s just…”

His voice trailed off, but I already knew what the Skeleton King wanted to say.

“Yeah. It’s cruel.”

“……”

“But it was necessary.”

The helplessness of being unable to do anything. Pain so unbearable that death would seem a hundred or a thousand times better.

And the fear that they could find themselves in the same situation at any time if their opponent simply put his mind to it.

I needed to plant all of those things in the enemy’s heart and engrave them into his bones.

Of course, there was another option that would leave the fewest loose ends.

*Death.*

The tips of my fingers twitched before I realized it.

If I applied just a little—just a tiny bit more—force, I could kill Go Jun.

It was the perfect opportunity to eliminate even the slightest possibility.

But…

*The timing isn’t right.*

The doubts surrounding the truth would not disappear.

The conspiracy theory that humanity’s first trip to the moon was a lie, and the conspiracy theories claiming that countless famous people recorded in history were still alive, all followed the same pattern.

If Lee Jungryong disappeared, followed by Wu Heixing and then Go Jun as well—and if it came to light that I had “happened” to be here at exactly the right time—the rumors surrounding me would no longer be conspiracy theories.

So I had to end it here.

Right now, after planting fear of me and the overwhelming gap between our powers.

“I’ll say this one last time.”

“……!”

Go Jun’s body flinched. In a voice lower and more emotionless than ever, I bit out each word one by one.

“Let it end with Lee Jungryong. No one else.”

My breath, hot as lava, touched his body, and the figure lying facedown began to convulse.

Like a rabbit sensing the tiger’s teeth digging into its neck.

“Hide your teeth. Hide your claws. If you do that… nothing will happen.”

If he had intended to kill, he should have been prepared to die.

Lee Jungryong had been my greatest enemy and obstacle, and in the end, he had paid the price for what he had done.

What I was offering now was a proposal of reconciliation.

No—a demand.

And Go Jun had only one choice left.

His head gave the faintest nod.

As I stared into his two eyes drenched in fear and terror, I pressed his Sleep Acupoint, took several high-grade potions from my Inventory, and poured them over his body.

Hissssss.

I watched him heal rapidly, then suddenly turned my head.

“So… that’s more or less what happened.”

At that moment, a layer of space peeled away, revealing a huge Black man. Magic Johnson looked at me with a complicated expression before opening his mouth.

“I think there’s a lot we need to talk about.”

“I was thinking the same thing.”

As we spoke, the Skeleton King muttered quietly.

“What about the club?”

“That’s a gay bar, dumbass.”
## Chapter artifact 432

# Chapter 432

Magic Johnson was a good man.

He was the same way both on the battlefield and in society.

No matter the situation, he was always cheerful and never lost his smile. He had shown particular kindness to Team Leader Choi and me, even secretly resolving the matter concerning the Skeleton King for us.

But there was no trace of playfulness or laughter in the way Magic Johnson was looking at me now.

He silently stared at me with a complicated gaze filled with mixed emotions before suddenly opening his mouth.

“Which parts were true?”

“Everything. From beginning to end. Everything you saw and heard.”

I put particular emphasis on the word *everything*. And Magic Johnson was not dull enough to miss what I meant.

“…So you knew from the beginning.”

“As you know, I’m a little sensitive.”

“And that didn’t matter?”

“I didn’t expect you to follow me. But I thought it might not be such a bad thing.”

“I was curious. And part of me was worried, too. It was obvious that you knew something about that mysterious pattern, but you were trying to hide it.”

Before we parted, when Magic Johnson had asked about the magic circle, I had made the excuse that I had seen something like it in a dream.

Of course, I hadn’t said that to make him believe me. It had been a roundabout way of telling him not to ask for now.

“So I followed you, just in case…”

Magic Johnson let his voice trail off as he looked around at the surroundings, which were covered entirely in blood.

“Looks like I shouldn’t have followed you.”

It was a major incident in which two S-rank Hunters—each practically the face of his own country—had died. One of them had even been a comrade who had once fought alongside Magic Johnson on the same battlefield.

Sometimes, certain kinds of truth were uncomfortable.

For Magic Johnson, this must have been one of those uncomfortable truths.

“Do you regret it?”

“A little. Maybe it would have been better if I hadn’t known.”

Magic Johnson let out a quiet sigh and looked straight at me.

“Jin. Why are you telling me all this?”

“I wonder.”

“You were the only one who knew the truth. If you wanted to, you could have covered it up. The same goes for him.”

I glanced at Go Jun, who had lost consciousness, and shook my head.

“This wasn’t the kind of thing I could hide simply by keeping quiet. No matter how much I denied it, that bastard wouldn’t have believed me anyway. Lee Jungryong and that guy were both ticking time bombs. They were dangerous enough to threaten my people.”

“Jin. You… were enemies with them. You had been enemies for a long time.”

“Yes. If you’re in a situation where you can’t eliminate an enemy, you have to make them afraid of you—afraid enough that they’ll never dare look at you again. A bomb with its detonator removed won’t explode.”

“Then what about me? Why did you tell me this?”

“You already know. In a situation like this, there are only two kinds of people you can choose.”

I continued slowly, enunciating each word.

“An enemy. Or a friend.”

“……!”

“I thought Johnson would believe me. Because you’re my friend.”

Magic Johnson let out a low groan and stared at me with a complicated gaze filled with every kind of emotion.

“Just because someone’s your friend doesn’t mean you believe everything they say, Jin.”

“But you believed me. You didn’t doubt me even once during our entire conversation.”

“……”

“Help me. Help me protect my people and grow stronger.”

At some point, I had begun to feel everything around me changing.

In Murim, Dark Heaven had begun to stir. In the modern world, the Arch Lich—a Named Monster unlike any that had come before it—had slaughtered millions and brought about a catastrophe.

And then there were the mysterious patterns and symbols that had appeared in both worlds.

Or perhaps they were something that could be called *dark magic*.

*Could all of this really be a coincidence?*

Everything that happened in the world was connected by invisible links. To keep everything from toppling one after another like dominoes, I had to prepare.

And to do that, I desperately needed one ally.

“Johnson.”

“…Damn it.”

Magic Johnson was silent for a moment before letting out a deep sigh.

“Do you know something?”

“…?”

“That day. If you hadn’t asked me to teleport you to the place where the monster army was waiting, I might have suspected you.”

That single remark signaled his acceptance.

My face brightened, and Magic Johnson let out a helpless laugh.

“Damn it. Now that things have turned out this way, I can’t help it. Let’s clean up the area before the patrol gets here.”

He waved his hand, and the blood splattered in every direction vanished without a trace.

After clearing the surroundings in an instant with Clean magic, Magic Johnson looked at Go Jun on the ground and furrowed his brow.

“This man is a problem… I’d like to erase his memories entirely, but the situation is complicated. What a pain.”

“Huh?”

My ears perked right up.

I suddenly remembered how, when I had stormed into the Myeongdong Guild in the past, the mages from the Ares Guild had used memory-manipulation magic on the Myeongdong Guild members at the scene.

“You can do that?”

“It would obviously be difficult, but it isn’t impossible. Still, the stronger the target’s mental fortitude and the more extensive the memories you have to alter, the harder it becomes.”

“Oh.”

“He seems quite strong. In the worst case, we could fail and even leave traces that someone attempted to manipulate his mind.”

Go Jun was strong enough to qualify as an S-rank Hunter, despite his current condition.

Unlike Wu Heixing, he also had a fairly strong will, so attempting something like that could be a needless gamble.

“Leaving traces would be a problem.”

“Indeed. If we were discovered, we couldn’t avoid punishment. Mental-manipulation magic is a serious felony.”

Lee Jungryong and the Ares Guild had carried out such things without the slightest hesitation.

Even if someone noticed, they wouldn’t dare question it. Everyone knew how much power and influence they possessed.

“Still, if we tried it and succeeded…”

“Under federal law, the minimum sentence would be one hundred years in prison without parole. Want to try?”

I answered without even taking a breath.

“No.”

“Good boy. That’s a wise decision.”

A minimum sentence of one hundred years without parole?

If I got caught, I’d rot in prison without a chance. Even if I escaped, I’d spend the rest of my life as an internationally wanted fugitive.

I might even end up with a ten-billion-beri bounty on my head, living as a pirate on Somalia’s Grand Line, just like in a manga.

Just thinking about it was horrifying…

“It’s a shame. If this were Korea, it might be worth trying.”

“Korea? Why?”

“If you spread money around, hired a lawyer who used to be a chief prosecutor, and took advantage of *jeongwan yewu*,[^1] you probably wouldn’t get much of a sentence.”

“Jeongwan yewu? What’s that?”

“It’s a thing. Ah, if you said you’d done it while drunk after downing about five bottles of soju,[^2] you might even get a suspended sentence.”

Magic Johnson laughed loudly as if he had heard an incredible joke.

“Don’t say ridiculous things, Jin. What kind of country is that?”

“……”

“You’re serious? My God.”

In any case, memory-manipulation magic was out of the question.

I left Go Jun where he lay and began walking.

The three A-rank Hunters Go Jun had hidden away were frozen like stone statues, their Paralysis Acupoints struck by the Finger Qi I had fired at them.

“You saw everything, right?”

The three men looked up at me with eyes filled with terror.

Sometimes, watching someone else suffer could instill more fear than suffering yourself.

They had been unable to move even a finger as they watched Go Jun get brutally and thoroughly crushed. Their souls had almost left their bodies.

“I remember all three of your faces. Getting your personal information is only a matter of time.”

That was how powerful people had always operated.

If you couldn’t kill someone, you had to instill fear in them the same way. You had to make sure they could never bare their teeth at you again.

“If we meet like this again… I’ll kill you.”

Whoosh!

The killing intent that erupted in an instant sliced through and pressed down on everything around us.

After reining in my qi, I slowly swept my gaze across their corpse-pale faces before suddenly thrusting out a hand.

Crack!

“Ghk!”

“Hah, huff…”

At last, the men were released from the pressure points and exhaled the breaths they had been holding.

Their bloodshot eyes were wet, and saliva and vomit dribbled from their open mouths.

“I’ll give you ten seconds. Get that bastard out of here.”

It was obvious who *that bastard* referred to.

Before I had even finished speaking, the three men struggled to their feet and rushed toward Go Jun.

They hoisted their still-unconscious superior onto one of their backs and vanished at lightning speed.

I threw one final word after them.

“Erase everything that happened today from your memories. And think carefully. Which ship do you need to be aboard to keep yourselves alive?”

“……!”

“……!”

“……!”

The Ares Guild was a massive, sturdy ship.

But Cheon Taemin, its great captain, had vanished without a trace long ago, and Lee Jungryong—the man who had taken the helm after him—had also met his death.

The ship that had seemed destined to sail the seas forever had begun to list.

A captain couldn’t abandon his ship, but the sailors hired to work aboard it were different.

If they wanted to, they could find a new ship and a new shipowner.

*That should have been enough for them to understand.*

The three men hesitated for a moment after hearing my words before disappearing into the darkness.

They gave me no answer and showed no particular reaction, but I knew.

They would never forget what I had said.

They would turn it over in their minds dozens and hundreds of times before passing it on to their other companions. And little by little, water would begin filling the bottom of the enormous ship called the Ares Guild.

“Ooh, vile human. Ooooooh.”

“This is what you call strategy, you idiot.”

“You’re an idiot, so how are you this devious and cunning?!”

“……You son of a bitch.”

He wasn’t wrong, but it pissed me the fuck off.

Let’s just say that after several years of Hunter life, I had learned various things through experience.

Magic Gems were now an essential power source for cutting-edge civilization. As a result, enormous amounts of capital had naturally gathered. And where there was capital, people gathered as well—and all kinds of things were bound to happen among them.

*I’ve thrown out what I know for now… If I wait, someone will bite.*

Just as a sect’s standing in Murim was determined by the martial artists it possessed, the standing of a modern Guild was determined by how impressive its Hunters were.

And Go Jun could never fill the void left by Lee Jungryong.

Just as Lee Jungryong had never been able to fill the gap left by Cheon Taemin.

It was only a matter of time before the fish that had spotted another tasty bait beyond that empty space began swimming away.

“You’re not holding back. Are you planning to go to war with the Ares Guild?”

I shrugged at Magic Johnson’s words.

“It’s not something I can’t do, but we need to make it look good.”

“Make it look good?”

“The Peace Guild is going to grow enormously from now on. I’m here, and Team Leader Choi is attracting attention from the media.”

“Oh, I heard about that, too. Apparently Choi’s been incredible lately.”

The spotlight from the world’s media was aimed at me, but the more I avoided contact with the press, the more attention was directed toward Team Leader Choi.

He belonged to the same Peace Guild as me and was one of the very few people allowed to visit my hospital room.

On top of that, he had achieved remarkable results during this monster wave and possessed looks that could rival a celebrity’s.

*The greatest secret still hasn’t been revealed.*

If the truth—that he was Cheon Taemin’s own flesh and blood—were made public as well, the media would undoubtedly go into a frenzy.

“Anyway, it’s only a matter of time before the Peace Guild takes off. The Ares Guild’s influence will shrink day by day.”

“Hmm. That’s certainly possible.”

Magic Johnson nodded before suddenly opening his mouth.

“But, Jin.”

“Yes?”

“What exactly do you know about the magic circle—”

“Oh, right. The club!”

“Huh?”

“You said you were going to a club with the Skeleton King.”

“Wait, wait, Jin!”

“Golgoli. Let’s go to the club!”

“Yes! Raise your ribs and scream!”

I hurried away while listening to the Skeleton King’s nonsense.

Then, as I looked up at the faint moonlight, a thought suddenly crossed my mind.

*I should head back soon.*

The time was approaching.

The time to return to another world—to Murim.

[^1]: *Jeongwan yewu* is the unofficial preferential treatment often afforded to lawyers who formerly served as judges or prosecutors, particularly through their old professional connections.

[^2]: Soju is a clear Korean distilled liquor, commonly served in small glasses.
## Chapter artifact 433

# Chapter 433

On the latest-model hologram TV, a respectable-looking middle-aged news anchor opened his mouth.

“Twenty days have passed since the monster wave in Sichuan Province—a tragedy dubbed the ‘Small Cataclysm’—finally came to an end. Across the continent, the cries of suffering people fill the air. CCTV correspondent Zhang Weijia is at the scene.”

As soon as he finished speaking, the screen changed.

Amid ruins that had completely collapsed and turned to ash, a young reporter wearing various kinds of protective gear faced the camera and began to speak.

“Large-scale restoration work is currently underway throughout Sichuan Province. Aid from countries around the world continues to arrive, but the traces left by the war are nothing short of horrific.”

The camera slowly panned across the surroundings.

The young reporter dispatched to cover the story was not the only person there. Countless people from different countries, speaking different languages and holding different nationalities, filled the ruins.

“Lift on three! One, two!”

“Hup!”

*Thud-thud-thud. Boom!*

There were places that heavy machinery could not enter.

Large-bodied Hunters lifted chunks of stone and concrete instead of weapons, while mages continuously cast detection magic in search of possible survivors.

“How is it?”

“There don’t seem to be any survivors within a hundred-meter radius. Let’s move a little and try again…”

“Here! Here! We’ve got a survivor reading! Hurry!”

Whenever a severely injured survivor was rescued, healers rushed over and poured potions and healing magic into them.

When a child who had reached the brink of death finally drew a steady breath, the people around them exchanged deeply moved smiles.

But the joy lasted only a moment.

The reporter’s next words brought everyone back to the cruel reality.

“According to the government authorities, the casualties identified so far total four million. Property damage has reached 2.3 trillion yuan. This is the greatest damage suffered since the Great Cataclysm, exceeding the losses from the Great Sichuan Earthquake by dozens of times.”

In barely a month, millions had died or been injured, and an astronomical amount of money had vanished.

Even more frightening was the fact that all of this was merely the damage tallied *so far*.

Considering everything from the plunging stock market to the damage this incident had inflicted on various industries, China would suffer badly in the days ahead.

The Chinese people were consumed by grief and fury at the news, directing the arrows of a billion people’s anger in a single direction.

The young reporter standing there was no exception. His voice rose, boiling with indignation.

“This monster wave was like a natural disaster beyond the power of human beings to stop. But if everyone had joined forces to prepare for the disaster and respond quickly, the situation would have been very different. Chairman Shao Yang has offered a profound apology for this and released the transcript of last month’s meeting.”

The contents were shocking.

The transcript of the Communist Party’s highest-level committee meeting, previously hidden from the public, captured the sharp conflict in its entirety. Chairman Shao Yang’s faction had insisted on asking countries around the world for help immediately, while the Crown Prince Party had argued that they should draw on the power of Zhonghua and fight with the spirit of chivalry.

And one person stood out above all the rest.

The star of the transcript was an old politician who had lost everything after losing his only son, Wu Heixing.

“Committee Member Wu Xueming, Premier of the State Council and a member of the Central Politburo Standing Committee, spent more than fifty years in politics. It has been revealed that he committed countless acts of corruption while leading the Crown Prince Party, the largest faction in the country.”

If the outcome had been good, what was happening now would never have come to pass.

But the power of Zhonghua and the spirit of chivalry he had gone on about during the meeting at the beginning of the Small Cataclysm had sounded like nothing but bullshit even to those steeped in Zhonghua ideology. In the end, they had become the laughingstock of the entire world.

On top of that, it came to light that his past military-related corruption had led to accidents in which tanks stopped and helicopters crashed. Wu Xueming was driven to the edge of a cliff.

And Chairman Shao Yang, a seasoned politician, did not miss the perfect opportunity.

“Committee Member Wu Xueming used his guanxi with prominent figures in the military, political, and business worlds to embezzle astronomical sums of money. We are currently investigating every circumstance connected to this incident.”

In truth, the large-scale purge had already begun.

Of the seven standing committee members who could be considered the highest-ranking members of the Communist Party, the Crown Prince Party’s leading figures—including Wu Xueming—had been summoned one after another. A sweeping reorganization of the military had also taken place.

The media merely pointed its cameras wherever the government directed them and recited whatever the government chose to show.

Several more investigations and trials still awaited them, but no one was unaware that they were nothing more than formalities.

“Comrades of the people. They will pay the price they deserve. That is justice—”

“Hey, mister.”

The young reporter’s furious voice, raised in neglect of his duty as a journalist, was abruptly cut off by someone. At the same time, his mind went completely blank.

*What kind of lunatic interrupts a live broadcast…?*

This was a colossal broadcasting disaster.

The staff at the scene, the main anchor at the broadcasting station’s desk, and even the director watching the TV from his office all stood there with their mouths hanging open.

But the person responsible for creating this entire situation could not have been calmer.

No—instead, he spoke to the reporter in an irritated voice.

“Move aside. It’s fine that you’re covering the story, but you’re getting in the way of the work.”

“Pardon?”

“Did someone shove stinky tofu in your ears? I’m telling you to go somewhere else instead of blocking the way and filming in the middle of ongoing work.”

The young reporter’s face turned as white as paper. He stammered and looked around.

The staff were terrified because of the colossal broadcasting disaster, while the Hunters nearby wore expressions that seemed to say they were glad someone had finally spoken up.

For a brief moment, the reporter managed to escape his panic. With a forced smile, he spoke to the man.

“I-I’m sorry. It seems we made a mistake.”

“To hell with sorry… Ugh, my throat.”

*Khhk—ptooey.*

The man, covered in dust from head to toe, spat out a wad of black phlegm and continued.

“It’s only a mistake if you didn’t know. I saw you slip the person in charge some money before coming in, so what are you talking about?”

“Excuse me! What exactly are you saying?”

“What am I saying? I saw the whole thing. Wanna bet your balls?”

At that moment, the cameraman watching everything unfold right in front of him felt his balls tremble.

*We’re fucked.*

CCTV, his employer, was China’s largest broadcasting station and one of the five biggest in the world.

And now, during the nine-o’clock evening news broadcast watched by tens of millions of people, someone was proposing a bet involving his balls.

The young reporter was already begging the man with an expression as if his testicles had been cut off.

“S-Sir, please…”

“Hey, kid. Move while I’m asking nicely.”

“This is a broadcast. So please watch your language…”

“Wow, you’re really slow on the uptake. There’s a survivor under where you’re standing, so I’m telling you to move.”

“What?!”

The reporter and every member of the staff leaped back as if they had been burned.

Only then did the man nod.

He strode over to a massive pile of concrete and placed a hand on it.

“That’s better. Don’t get in the way. Move back. You’ll get hurt.”

*Whoosh! Boom!*

There was no need to look for people to help.

A chunk of concrete that had taken several Hunters to move flew like a pebble, while rock and ground split apart like cheesecake whenever the man’s hand blurred.

*Papapapapak!*

It happened in the blink of an eye. Before there was even enough time to cook a cup of instant noodles, the man emerged from the deep pit where he had disappeared.

And in his arms, he carried a tiny old woman.

“What… What is this…?”

The broadcasting staff, speechless at the astonishing sight, were pushed aside by the Hunters who came running over.

When a healer in a pure-white robe hurried over with a potion, the man waved a hand.

“Not yet. She’s too weak to handle a potion.”

“W-Wait. You look like a close-combat Hunter, but this is my area of expertise…”

“Hmm. I don’t think so.”

The man calmly answered and placed a hand against the old woman’s back.

Warmth began to rise, strong enough to be felt from several meters away. A faint trace of color returned to the old woman’s pallid face.

“Move her somewhere warm first. Keep her body temperature up with magic. Once she regains consciousness, you should be able to use a potion or healing magic.”

The healer looked back and forth between the old woman and the man with a dazed expression before speaking.

“T-Thank you, sir.”

“There’s no need to thank me for doing what anyone should do, and I’m no sir either. Let’s leave it at that. And…”

The man hesitated briefly before continuing in a low, subdued voice.

“She’s the last one. In this area.”

“Ah…”

The people who realized what he meant let out low groans.

The Hunters were among them, as were the broadcasting staff. They found themselves accepting his claim, yet could not hide their bewilderment.

*Why?*

Even with only a slight turn of the head, they could see hundreds of Hunters using magic and cutting-edge equipment to search for survivors. It was only natural to trust them rather than the man standing in front of them. They should have dismissed his words as nonsense, but…

*Somehow, I believe him.*

Why?

As they watched the astonishing scene unfold before their eyes, the phrase *broadcasting disaster* vanished completely from their minds.

Two other thoughts surfaced in its place.

*No way. Could it be?*

“It’s only my personal opinion. So please don’t give up until the very end.”

Without realizing it, the cameraman raised the camera that had drooped toward the ground.

Then he called out to the man, who had bowed his head slightly and was about to turn away.

“C-Could you be Mr. Jin?”

His question spoke for everyone present.

The man was covered in so much dust that his features could not even be properly distinguished.

But what he had shown them in that brief moment had clearly reminded them of one person…

“No.”

The answer came without even a breath’s hesitation. The cameraman asked again.

“Y-You’re not?”

“Are you talking about Jin Taekyung? I appreciate the mistake, but why would he be here? According to the news, you can’t even see hide nor hair of him. Who knows what he’s doing?”

That was true. Jin Taekyung was a hero who had not shown even the tip of his nose since the press conference, after all.

It was almost absurd that they had arrived at this conclusion based on nothing more than a vague feeling.

Just as the cameraman let out a sigh, the young reporter suddenly spoke.

“Then may I ask you one question?”

“No. Take care.”

“Do you have any thoughts on the claim that Mr. Jin is a descendant of Chen Lin, the Ming Dynasty general who fought in the Imjin War?”[^1]

At that moment, the man walking away spun around like lightning.

“Why is everyone always talking about descendants? Then, for fuck’s sake, is Asmodeus a descendant of Einstein? Even if it’s bullshit, at least make it remotely plausible…”

“Ah…”

“Uh…”

A silence descended, as if the world had stopped.

The man, Jin Taekyung, opened his mouth toward the people staring blankly at him.

“You all know I was joking, right?”

“…”

“I just stopped by while passing through.”

“…”

“Please edit this out. And cut the balls comment, too.”

The reporter, finally recovering from the shock, barely managed to squeeze out his voice.

“It’s live, sir.”

“Oh.”

Jin Taekyung nodded with a devastated expression and asked again.

“Live? You’re not joking—you mean for real?”

“Yes.”

“Then from what point to what point…?”

“I’m sorry, but from the beginning to the end…”

“Any idea what the ratings are?”

“I just checked the messages. They say we’ve broken through thirty percent.”

“Oh. I see.”

Jin Taekyung was silent for a moment before walking away.

The young reporter, whose life had just been turned around from a colossal broadcasting disaster into a sensational scoop, called out to him in an anguished voice.

“S-Sir! Where are you going?”

The answer came, drained of all energy.

“Home.”

He was telling the truth.

A flight formation of dozens of aircraft flew across the sky and landed on the vast expanse of ground that had been cleared cleanly.

It was the aircraft formation that would take him back to Korea while he was briefly going to another world.

[^1]: The Imjin War was the Japanese invasion of Korea from 1592 to 1598. Chen Lin was a Ming Dynasty general who fought in the war.
## Chapter artifact 434

# Chapter 434

“Have you looked in a mirror?”

That was the first thing Team Leader Choi, the first to step off the aircraft, said to me.

I had roughly guessed it, since the people around me hadn’t recognized me, but was I really that much of a mess?

“No. Is it bad?”

“Yes. Bad enough that even your family couldn’t recognize you, Mr. Jin.”

“We’re not talking about anyone else, but Mom would recognize me. She gave birth to me after carrying me for nine months.”

“We watched the news together on the way here. While watching your interview, she asked who that filthy person was and why he was being so rude.”

“…Seriously?”

I looked over Team Leader Choi’s shoulder.

Mom poked her head through the gap in the open entrance of the private jet and spoke in a tiny voice.

“Sorry, son.”

She vanished immediately after saying that, and a slim face took her place. It belonged to Hayeon, whose skin glowed as if she had been sleeping and eating well for the past several days.

“I recognized you right away! I’m the only one who did, right?”

“Who are you? I’m an only child.”

“Holy crap.”

I ignored Hayeon’s words and asked Team Leader Choi,

“That brat badmouthed me the most, right?”

“Yes. She was having a great time egging your mother on.”

Yep. She was definitely my sister.

Perhaps she had heard our conversation, because Hayeon quickly pulled her head back inside. She wasn’t just good at studying—she was quick on the uptake, too.

“It’s nice to see such a harmonious family.”

“If we got this harmonious twice, someone would disappear from the family register.”

Team Leader Choi answered with a straight face.

“That would still be better. I don’t have a family, either. Except for my maternal grandfather, whose whereabouts I don’t know.”

“…Why are you doing this to me?”

“I was joking.”

“Please use your turn signal before cutting in like that.”

Team Leader Choi chuckled quietly at my grumbling and reached out a hand.

At a short activation word, an item containing Clean magic flashed brightly.

A cool breeze made of mana swept over my entire body, blowing away all the dust and grime covering me in one go.

“Thanks. Much better.”

“Don’t mention it. Anyway, you’re busy right up to the very end. You suddenly disappeared on the day you were leaving, and it put us in quite a difficult position.”

“You’re making it sound worse than it was. I was planning to come back in time anyway.”

Under Team Leader Choi’s silent, searching gaze, I scratched the back of my head and continued as if I were making an excuse.

“I just stopped by in case something happened.”

“Mr. Jin.”

“I know what you’re going to say.”

“Even if you already know, I still have to say it.”

Team Leader Choi looked me in the eye and spoke clearly.

“You can’t save everyone. Mr. Jin, you… did your best.”

I smiled bitterly.

I had witnessed many deaths, both in the modern world and in Murim.

Sometimes I had been a spectator, far removed from the events. Other times, I had been directly involved.

And every time everything ended, I always found myself asking the same question.

Just as I was now.

*Was this really the best I could do?*

The best.

The greatest and finest thing possible. Giving something everything you had.

Those two words frightened me more than anything. There was no fixed standard for them.

“Doing your best” was a standard you could meet only by judging yourself.

But regret always remained. Even if it was no more than a few grains of dust, as long as it sank into the deepest part of your heart, you couldn’t say you had truly done your best.

Because the best meant having no regrets at all.

“Nice weather today.”

I muttered for no particular reason as I looked up at the sky, then grinned at Team Leader Choi.

“Let’s call it second-best. I’ll feel better that way.”

“It’s different from what you think and how other people see it. For us, it was the best—and more.”

That voice did not belong to Team Leader Choi.

I already knew he was there, so I did not startle. I turned my head instead.

The owner of the aged voice spoke to me with a gentle smile.

“So… you’re leaving in the end, Mr. Jin.”

I smiled back at Chairman Shao Yang.

“The hotel rates were more expensive than I expected.”

“They’re merchants, are they not? It is only natural for them to charge for the services they provide.”

“I might have stayed if they’d given me a discount, but I thought they were overcharging me because I’m a foreigner.”

“Oh dear. So that happened. Shall this old man give them a stern talking-to and persuade you to stay a little longer?”

“The bus has already left. It would be rude to chase it down the road and ask the driver to open the door.”

“Then I suppose I have no choice but to let you go. Ha ha.”

What kind of hotel would charge me and overcharge me in a situation like this?

There was no way that would happen.

We exchanged light jokes while confirming each other’s intentions, then clasped hands.

“You have given us more help than I can possibly comprehend.”

His voice and eyes were filled with sincerity.

The people who had accompanied the Chairman also bowed politely to me.

A few familiar faces were scattered among them. Xiao Shen and Wei Fenghu, the Minister of National Defense, were among them.

I gave the two of them a subtle nod and answered jokingly,

“I only did what I had to do. And more importantly, it wasn’t volunteer work. You know that, right?”

“Ha ha. Of course.”

I had momentarily forgotten, but the bounty on the Arch Lich’s head had been an astounding fifty trillion.

The bounty was so astronomical that the compensation I would receive for the month-long war would look like pocket change by comparison.

It was an amount I had never even imagined possessing in my entire life, so it was still difficult to believe.

*Fifty trillion.*

Only half a year ago, I had been eating seven-thousand-won bowls of bone hangover soup to save money, then boiling ramen because that alone hadn’t been enough to fill my stomach.

Maybe that was why I felt more dazed than happy.

“Um, but…”

Chairman Shao Yang raised his eyebrows.

“Are you really giving it to me?”

The instant I finished speaking, Team Leader Choi stepped firmly on my foot, while the Chairman’s wrinkled eyes curved gently.

“Why? Do you not wish to receive it?”

“No, no!”

My vehement answer spread a ripple of laughter through the crowd.

Chairman Shao Yang laughed heartily and patted my shoulder.

“Did I not say so? Paying a proper price for work done is only natural.”

They say China is the Middle Kingdom because it’s too large to be a small nation and too narrow-minded to be a Great Nation, but this old man was damn generous.

I awkwardly scratched my chin.

There was nothing wrong with receiving the money according to the contract, but accepting a fifty-trillion bounty in the middle of such a devastating situation made me feel like a thief rummaging through someone else’s pantry.

“If things are difficult, you can pay me in installments.”

“If you are worried about rebuilding the damage, that is something our country must handle. Your bounty is being processed quickly, Mr. Jin, so it will be paid officially soon.”

After finishing, Chairman Shao Yang leaned toward my ear and whispered,

“When I plowed up the fields and pulled out the rotten stalks, piles of gold came tumbling out. So you need not feel uncomfortable, Mr. Jin.”

I wondered what he was talking about, then realized it concerned the Crown Prince Party.

According to the news, the assets seized so far already amounted to hundreds of trillions.

And they hadn’t even touched Wu Xueming, the faction’s de facto leader, or the other members of its leadership.

*Now that’s some corruption.*

A country’s landmass must be proportional to its people’s nerve.

Still, they had ended up penniless and behind bars, so justice had been served to some extent.

I answered with a much lighter heart.

“Then I’ll accept it gratefully.”

“What are you saying? Thanks to you, we were able to prevent an even greater catastrophe. On behalf of all the people who could not be here today, I once again offer you my thanks, Mr. Jin.”

Before I could stop him, Chairman Shao Yang and his attendants bowed courteously.

The people gathered here were the major officials who moved an entire nation.

They were China’s body and, in many ways, its head.

I was momentarily flustered when a familiar voice slipped into my ear.

“Should I get down on my knees, too?”

“Faye Chen.”

She approached with a playful expression and poked me in the cheek.

“You worked hard, young man.”

“Not at all. Everyone worked hard…”

“Of course everyone worked hard. But if you hadn’t defeated the Arch Lich, there wouldn’t be any peace like this. That’s what everyone thinks, I’m sure. Except for that unpleasant prince, of course.”

Prince Felix, dressed in a dazzling uniform and draped in a snow-white cloak, let out an irritated cough and stared at me.

“What?”

“I pay you respect, Korean commoner.”

“…I appreciate it, but could you leave off the last few words?”

“I pay you respect, Korean commoner.”

“Are you doing this on purpose?”

“I mean it sincerely.”

“Of course you do, you bastard. I am a commoner.”

“That is not what I meant.”

Prince Felix suddenly extended his hand.

But unlike usual, he did not present the back of his own hand. Instead, he grabbed mine and pulled it toward him.

Then, while I was still too stunned to react, he kissed the back of my hand and stepped away.

*What the fuck?*

Faye Chen burst into loud laughter at the sight of me, unable to say a word from sheer absurdity, while Prince Felix calmly spoke his piece.

“I have shown you respect. It shall never happen again, so let your family treasure the honor for generations to come. Until next time.”

Prince Felix delivered his final words without changing his expression, then strode away with his attendants.

Magic Johnson, who had watched the entire scene, smacked his lips.

“Charming.”

“…You have a type like that?”

“Respect it.”

“He has a spouse.”

“That is why I’m holding myself back.”

We should never let him visit a Korean convenience store. The moment he took a bite of tuna mayo, the world would be hit by an unprecedented upheaval.

I shook my head in disbelief as Team Leader Choi spoke to me quietly.

“Mr. Jin. It’s time to leave.”

He was not speaking only to me, but to everyone gathered there.

I nodded and offered the people my final farewells.

I did not forget Xiao Shen and Wei Fenghu, with whom I had spent a considerable amount of time.

“Take care.”

“We’ll definitely meet again, hyung.”

Xiao Shen, who was only in his early twenties, rubbed his reddened eyes with his sleeve before continuing.

“I will become a Hunter as outstanding as you, hyung, and become head of the public security forces responsible for everyone’s safety.”

“You’re still young, but you’re already blinded by the desire for power. That job must be brutal.”

“I’m ashamed to say this, but I’ve decided to accept my grandfather’s help.”

“Good. He’ll give you plenty of advice, so listen carefully and carve every word into your bones. I don’t know what kind of person he is, but I’m sure he’ll give you good advice that will help you in every way…”

My words were cut off by something Xiao Shen said.

“You know him, too, hyung.”

“Huh? Know what?”

“My grandfather.”

“What are you talking about? The only grandfathers I know are Butler Kim from my Guild and the owner of the real-estate office outside my goshiwon.[^1]”

Chairman Shao Yang cut in with a laugh.

“Ha ha. This old man is here as well, you know.”

“Oh, come on. You’re joking…”

Wait a minute.

The corners of my eyes began to twitch.

*Shao Yang. Shao Shen. Shao, Shao?*

I had dismissed it because Xiao was a common Chinese surname, like Kim or Park in Korea, but now that I thought about it, their faces looked strangely similar, too.

“Don’t tell me…”

“Yes, that’s right.”

“Even Mr. Jin reacts just like everyone else. There is no helping it.”

“…I think I’m going to be sick.”

“Hyung?”

“Mr. Jin?”

What kind of novel was this?

*The Younger Friend I Made in China Turned Out to Be the Chinese Chairman’s Grandson.*

Even the title sounded unrealistic.

Why was everyone I met born with a silver spoon in their mouth?

I was briefly overcome by panic, but eventually managed to squeeze out my voice.

“Oh. I see.”

“I am grateful to you not only as Chairman, but also as a grandfather who has been reunited with his grandson. It is a debt this old man will never be able to repay.”

“Ah… Take your time.”

I had unintentionally saved the grandson of China’s Chairman.

Still dazed, I exchanged final farewells with the grandfather and grandson. Then my gaze happened to fall on one person.

*Wei Fenghu.*

It was no mistake that the smile at the corner of his mouth seemed empty.

Unlike his superior, he had lost someone of his own blood whom he loved.

We stared at each other in silence for a brief moment before speaking at the same time.

“Goodbye.”

“Take care, Mr. Jin. You have truly worked hard.”

It was a short conversation, but it was enough.

“Well, then.”

I gave everyone a small bow and followed Team Leader Choi onto the waiting aircraft.

Mom examined me with an expression that was both worried and happy. Meanwhile, Hayeon, who had been taking little sips of champagne while using the opportunity to her advantage, gave me a shy smile when our eyes met.

“Oppa, do you want a glass?”

“What do you mean, a glass? You’re a minor. Hey, take her glass away.”

The Skeleton King had transformed into a human form early on and was sitting in one of the seats. He ignored us completely and muttered in a dark voice.

“It won’t stand… I’m a eunuch…”

Team Leader Choi, seated beside him, offered consolation.

“Keep your chin up. I’ll ask Mr. Johnson nicely next time.”

“Really?”

I almost smacked him, but a quiet laugh escaped me instead.

It finally felt like I was back where I belonged.

My beloved family, more than anyone else, and my colleagues and friends.

Even though we were inside a chartered plane rather than a house, I felt an indescribable sense of comfort.

*Yes. This is enough.*

“We will now begin takeoff. Passengers in the cabin, please…”

An announcement rang out, and the aircraft rose toward the sky under the escort of the flight formation.

After spending a long time laughing, talking, and sharing stories, I suddenly sensed that the time had come.

I watched the people who had fallen into deep sleep from their accumulated fatigue, then lay down in a comfortable seat.

*Login.*

Ding.

Darkness covered my vision along with the familiar notification, and I departed.

Toward another world and another group of people waiting for me far away.

[^1]: A goshiwon is a very small, inexpensive room-for-rent housing arrangement common in South Korea.

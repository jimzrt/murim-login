# Checkpoint Review — 980–984

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

# Chapters 980–984

## Plot

Jin Mukyung wakes recovering from the battle at Eight Spring Gorge and presses Jin Taekyung to tell him the losses. Three days after the victory, he learns that more than five thousand people were killed or wounded, including over three thousand dead. Cheol Mubaek died giving Mukyung an opening against the Demon Bird and left him the Shura Annihilating Fist manual.

The Murong Family’s attack on the Hebei Peng Family is exposed. Jeong Hogun leads forces to the Murong estate, where Namho prevents the execution of its remaining household and offers those proven innocent a chance to rebuild as the Murong household under a new Family Head. Murong Yeonghwi and other fugitives remain at large.

An imperial proclamation brands Dark Heaven traitors and calls on martial artists to join the government in punishing them. At Eight Spring Gorge, tens of thousands honor the fallen on the Double Ninth Festival. As Taekyung sees Jin Wikyung and Lee Seowol mourning their uncles, a mysterious chime sounds.

## Continuity

- The battle at Eight Spring Gorge ended in victory, but Shanxi and its allies suffered more than five thousand casualties, including over three thousand dead.
- Cheol Mubaek is dead; he left Jin Mukyung the Shura Annihilating Fist manual. Peng Cheolhu remains unconscious from severe injuries.
- Dark Heaven has been declared traitorous, and the imperial proclamation says the war has begun.
- About a hundred Murong survivors, including Murong Su, are to be interrogated. If proven innocent, they may rebuild as the Murong household under a new Family Head. Murong Yeonghwi and several dozen others escaped.
- Lee Seowol is mourning her uncle, Cheol Mubaek.
- The source and significance of the chime at the chapter’s end are unknown.

## Translation Decisions

- Distinguish 모용세가 as the dissolved “Murong Family” from 모용가 as the surviving “Murong household” or lineage.
- Render 천호 as “Thousand Captain,” 상산후 as “Marquis of Shangshan,” and 황도 as “Imperial Capital.”

## Durable state

{
  "active_continuity": [
    "The imperial proclamation declares Dark Heaven traitors and calls on martial artists to join the government in punishing them; the war has begun.",
    "At Eight Spring Gorge, tens of thousands honor the fallen with chrysanthemums and cornelian berries on the Double Ninth Festival.",
    "Lee Seowol is mourning the death of her uncle, Cheol Mubaek.",
    "About a hundred Murong Family survivors, including Murong Su, are to be interrogated; if proven innocent, they may rebuild as the Murong household under a new Family Head."
  ],
  "continuity_sources": [
    984
  ],
  "open_questions": [
    "Will the Murong survivors’ innocence be established, allowing the household to rebuild under Murong Su or another Family Head?",
    "What is the source or significance of the chime that sounds at the chapter’s end?"
  ],
  "safe_through": 984,
  "temporary_decisions": [],
  "version": 1
}

## Reading copies

## Chapter artifact 980

# Chapter 980

Jin Mukyung’s eyes were wide open. It was quite a sight.

Maybe it was because the way I remembered him had always been so stiff and curt.

“Hey, you awake?”

I greeted him, glad to see him.

Though he was looking right at me, his dazed, unfocused eyes wavered.

“F-Father…”

Maybe it was because he’d been unconscious for so long.

His hoarse voice trailed off before he could finish.

Seeing how confused he looked, Hyuk Mujin, standing beside him, spoke up with worry written all over his face.

“Um, could there be something wrong with his head?”

“That’s strange. The Medicine King Hall Master examined him and said there wasn’t much to worry about.”

“Even monkeys fall from trees. No matter how famous the Medicine King Hall Master is as a physician in Shanxi Province, he can still make a mistake. He’s getting on in years, too.”

“Hmm. You think so?”

“To be honest, I had a bad feeling about him. Isn’t he the old geezer who threatens to ram a giant needle into a patient’s Huiyin Acupoint if they refuse treatment? Captain, don’t you remember when he pulled that on you while we were trading blows with the Mount Heng Sword Sect?”

Of course I remembered.

The Medicine King Hall Master had been terrifying when he’d announced he was going to perform a forced opening ceremony with a needle as thick as my forearm.

*Still, for all his temper, he seemed to know his stuff.*

I’d confirmed it myself several times, too.

There were limits to examining someone’s insides by channeling internal energy into them, but even taking that into account, Jin Mukyung’s condition wasn’t all that serious.

Of course, that was considering he’d just fought a Supreme Peak master who was a level above him.

“Go get the Medicine King Hall Master first. Oh, and if you can…”

“I’ll bring Great Hero Jeok too, if possible. Right?”

“Yeah.”

That kid was quick on the uptake.

Now he knew what I meant before I even finished saying it.

Hyuk Mujin gave a small bow and turned away. He’d just started to walk when—

“Where… am I?”

His lips were cracked like drought-stricken fields. His voice came out in broken, hoarse bursts.

But it was too soon to relax.

Jin Mukyung’s eyes were only just beginning to focus again, so I cautiously waved my palm in front of him.

“Can you see this?”

“I can… see it. But where is this…?”

“Where do you think? The Jin Family of Taiyuan.”

“If that’s… the case…”

I could guess what he was going to ask.

For Jin Mukyung, who was struggling to force the words out, I gave him the answer he wanted most.

“We won.”

“Ah.”

“The nomads who were left completely surrendered to us, and everyone in the Murong Family was either killed or captured.”

“What about… the others?”

His questions kept coming, one after another. I pretended not to hear and ignored them.

I couldn’t tell him yet.

Not yet.

“I’ll tell you later.”

“What?”

“Your eyes still look pretty out of it. Tell me how many fingers I’m holding up.”

Jin Mukyung knew better than anyone that he still wasn’t completely back to himself.

I changed the subject without making it obvious and held up three fingers. Jin Mukyung frowned at me, then answered.

“Three.”

“Good. And now?”

“Five.”

He was answering right away. Looked like his head was finally clearing.

But there was one last, most important step.

With a grave expression, I took off my shoe and stuck out my toes.

“And now?”

Jin Mukyung was quiet for a moment. Then he spoke.

Unlike before, his voice was astonishingly firm.

“Move your filthy foot before I kill you.”

“Hmm. Perfect. Feeling more like yourself now, patient?”

Jin Mukyung let out a shallow sigh.

“Yeah, you son of a bitch.”

“Now, now. You can’t talk like that to your own brother. Spit while lying down, and it’ll land on your own face.”

I didn’t bother adding *though in reality, I was an outsider with not a drop of their blood in me.*

At least in the world I was living in now—the Murim—the three sons of the Jin Family of Taiyuan had been born to the same parents.

But at that one teasing remark, an odd swirl of emotion surfaced on Jin Mukyung’s face for the briefest moment.

“What’s with you?”

“Nothing you need to know. It’s just…”

Jin Mukyung hesitated, then continued.

“I just had a strange dream.”

“A strange dream? A nightmare?”

“Not quite a nightmare… I don’t know. It was just strange.”

He looked a little confused as he said it, but I shrugged as if it were nothing.

*Well, it happens. I have all kinds of dreams every time I pass out.*

I was used to it.

No—maybe it was one of the chronic problems shared by Hunters and Murim people alike.

When you kept brushing up against death, your state of mind was bound to change. And an unsettled mind often revealed itself in dreams.

“So, how do you feel?”

“How do I feel…”

Jin Mukyung tried to sit up in bed too quickly and frowned.

“I’ve broken bones. Three, from what I can tell right now.”

I nodded, satisfied.

It was a good sign if the patient could feel the pain and judge his own condition.

“Exactly. That matches the Medicine King Hall Master’s diagnosis.”

“My muscles hurt so much I can’t even move. It feels like someone tore every muscle in my body to shreds.”

“Of course you’re in pain. You fought like an animal. That’s perfectly normal.”

“My internal injury… For some reason, it’s not as bad as I expected.”

I puffed out my chest, as if I’d been waiting for him to say that.

“I put in a little effort.”

“You did?”

“Yep. You can thank me.”

Jin Mukyung stared at me for a while, then nodded.

“I see.”

“That’s it?”

“Yeah.”

“Hmm. That’s strange. People who were raised right usually say thank you in a situation like this.”

“……Didn’t you just say something about spitting while lying down?”

“Me? When?”

I put on an innocent, confused expression. Jin Mukyung let out a small sigh.

“Thank you.”

“I don’t feel any sincerity.”

“Thank you. I mean it.”

“Hmm. Somehow it feels like I’m making you bow down and thank me.”

“……”

“Let’s say that one was practice. One more time. And mean it this time.”

Jin Mukyung took a deep breath before answering.

“I survived thanks to you. I’m truly grateful.”

I wanted to tease him some more, but from the look in his eyes, I figured I’d better stop here.

Hiding my disappointment, I patted his shoulder.

“Good. That’s more like it. I’ll make sure to pass along your thanks.”

“Even after all this time, you’re exactly the same… What? Pass them along? What do you mean?”

“It’s nothing. Don’t worry about it. There were some people who helped a little while treating your internal injury.”

“Helped? Who?”

“They’re here. The Fire King and the Bow Saint. They’re both pretty nice people.”

“……?”

“Oh, right. You passed out early, so you wouldn’t know. Somehow, they ended up coming with me.”

Jin Mukyung had seen Jeok Cheongang while I was staying with the Jin Family of Taiyuan, so that was one thing. But the Bow Saint’s presence must have come as a major shock to him, weak as he still was.

Jin Mukyung barely steadied his ragged breathing and forced out his words.

“The Bow Saint? The one I know?”

“Yeah.”

“The Bow Saint from the Great Faction War? The one who uses a bow?”

“Ah. I thought so too, but if you mess around with that bow enough, it turns into a pair of blades. Kind of like a transforming robot. It’s pretty cool the first time you see it.”

“A crippled old servant…?”

“No, not a disabled old servant. A transforming robot. Though you probably wouldn’t understand even if I explained it.”

Just as I’d expected, Jin Mukyung had no idea what I was talking about. He stared at me with a dead look in his eyes.

“What the hell are you talking about?”

“Forget it. Let’s move on.”

“Yeah, that’s probably for the best. So the crippled old servant you mentioned… No, the Bow Saint really is one of the Three Saints I know?”

I nodded kindly at Jin Mukyung, whose words were starting to trip over themselves.

“Exactly.”

“……How did you even meet them?”

“At the Imperial Palace.”

“The Imperial Palace?”

“Yeah. The very same Imperial Palace everyone in the land has heard of.”

“No, how did you even get there?”

“This is a bit of a long story, so I’ll give you the short version.”

For Jin Mukyung, who looked even more confused than when he’d first woken up, I gave him a quick summary, neatly organized by my brilliant mind.

First: I went to the Imperial Palace and met the Emperor. It was a pretty scary place.

Second: We all worked together to defeat the Eastern Heaven Demon Lord.

Third: Right afterward, I learned about the conspiracy surrounding Shanxi Province. The Emperor gave me an official post and even saw me off.

“……That’s what happened. Got it?”

Hyuk Mujin, who’d been listening to my concise and lucid explanation, muttered under his breath.

“My diary from when I was six was more detailed than that.”

Jin Mukyung, who’d been staring blankly the whole time, finally spoke up.

“Are you actually insane?”

Hmm.

There were ordinary people everywhere who couldn’t understand the thought process of a genius.

In any case, after hearing the bare minimum, Jin Mukyung finally understood the situation and nodded.

“So those two treated my internal injury.”

“Right. They lived up to their reputations.”

“And you got thanked even though you did nothing.”

“Nothing? They’re my connections. I accepted the thanks on their behalf, as their representative.”

“Do you know what?”

“No, how would I? I haven’t said anything yet.”

“Sometimes, talking to you makes me feel like I’m losing my mind.”

“I’m a pretty cheerful guy. Ordinary people can’t always handle it.”

I flashed him a deliberately obnoxious grin. A bitter smile touched Jin Mukyung’s lips too.

“Is that all?”

“What?”

“Is that really the only reason you’re pretending to be so much cheerier than usual, talking nonstop and acting so restless?”

I scratched the back of my head.

“Who knows? I’m not sure what you’re getting at.”

“It reminds me of two years ago. I came back to the family after a long time, and the hopeless good-for-nothing had become a completely different person.”

“……”

“The sudden change was strange, but deep down, I was a little happy. The youngest, who seemed to have been reborn as an entirely new person, turned out to be a pretty decent guy the more I got to know him.”

Jin Mukyung added,

“At the very least, he wasn’t someone who’d laugh and chatter thoughtlessly while leaving behind the deaths and sacrifices of so many people.”

At that moment, the corners of my mouth—which I’d forced upward—relaxed.

Jin Mukyung looked straight at me. I was no longer smiling.

“You know you can’t avoid this any longer, so answer me honestly.”

The air grew heavy. My stiff expression was reflected in Jin Mukyung’s wavering eyes.

“Who was it, and how many people were sacrificed?”
## Chapter artifact 981

# Chapter 981

Jin Mukyung didn’t know how much time had passed.

But after all the stories had been told, and a long silence had followed, there was only one thing he could say.

“I’m tired.”

And so Jin Mukyung was left alone.

He raised his body, aching as if it might break apart, and leaned his upper half against the bed. Then he stared blankly out the window.

Beneath the first light spreading from the distant east, he watched his younger brother’s back as he left the pavilion with a subordinate. He recalled the words he’d heard moments ago.

*Five thousand.*

Just two syllables.

Far too short to hold the weight of thousands of lives. It didn’t feel real.

But it was, without a doubt, reality.

*Of the five thousand casualties, over three thousand died. The rest suffered injuries, big and small, and many were left crippled.*

Of the fifteen thousand people of Shanxi who’d gathered at Eight Spring Gorge that day, a third had been killed or wounded.

Many of them had been government soldiers from the Shanxi Provincial Office, relatively weak in martial arts. But Jin Mukyung knew they, too, were part of *us*—people who had put down roots and lived on this land.

*…A great victory.*

*Yeah. A great victory. One for the history books.*

More than five thousand had become casualties, but in a single night they’d annihilated an army of well over thirty thousand.

They’d won an incredible victory against foreign enemies who outnumbered and overpowered them. It was no exaggeration to say they’d written a new page in the history of the Great Nation.

And yet, not a single person looked happy as they spoke of the great victory.

Those who took what belonged to others reveled in their victories. But those who fought to protect what was theirs mourned what they’d lost along the way.

The bodies and blood left behind by those who’d departed this world were a burden the survivors alone had to bear.

*The Hebei Peng Family lost more than half its forces. Great Hero Peng, the Thunderbolt Saber King, still hasn’t regained consciousness.*

The great tiger of the Peng Family, who’d lorded over Hebei for generations, still hadn’t woken from his grievous injuries.

No one could have anticipated that the North Heaven Demon Lord—someone he’d considered a friend—would betray him. And the martial arts he’d used in his sudden ambush were in no way inferior to those of the Thunderbolt Saber King.

*Even after we took down Jamukha and the North Heaven Demon Lord, things didn’t go smoothly. If we hadn’t subdued the nomads, we would probably have suffered much heavier losses.*

Even though they’d joined the battlefield quite some time ago, the Murong Family had remained relatively intact until the fighting was nearly over.

If Jamukha had lived to see it, he would have realized the truth too late—and trembled.

Just as he’d used Temur to put the tribes of the eastern steppe in front as human shields, the North Heaven Demon Lord had used Jamukha to minimize the Murong Family’s losses.

The law of the survival of the fittest applied everywhere.

*That’s when the final battle began.*

Knowing their end was near, the Murong Family fought with everything they had.

While their allies were dying all around them, they took the Temporary Strength Pill they’d held back until then and fought to open an escape route alongside the western steppe nomads who’d refused to abandon their cause even after Jamukha’s death.

Their number was a staggering five thousand.

The people of Shanxi and the Hebei Peng Family were exhausted from the long battle, despite their soaring morale. The thousands of enemies, strengthened beyond their limits, scattered in every direction to avoid the three Supreme Peak masters, tearing through the weakened encirclement and fleeing.

No—they tried to flee.

Until, beyond the dim dawn light creeping through the darkness of night, they heard a roar that shook the whole world.

Until they faced three armies emerging beneath banners that should never have appeared here.

*We didn’t expect that either. They arrived much sooner than we thought.*

They said the scent of plum blossoms from Huashan had filled the ridge, replacing the chrysanthemums of the Double Ninth Festival, soaked in blood and stripped of their fragrance.

A group led in a charge by a hundred Peak masters swept through the enemy beneath the fluttering banner of the Murim Alliance. New guests also arrived in the narrow gorge, which had fallen quiet after the terrible battle.

Their brilliant golden armor gleamed as they rode forward like the wind, seated in their saddles. The world called them the Embroidered Uniform Guard.

*And that was the end of it.*

A dense fog of blood flowed over the gorge and wrapped around the broad basin.

With the first light of dawn, reinforcements swept in from every direction and crushed the enemy. The Bow Saint and the Fire King dominated the battlefield, while Jin Taekyung drove his spearhead into the chest of Murong Wijin, Head Elder of the Murong Family, who had resisted until the very end.

The battle—and the war—ended that day.

It began and ended with the Double Ninth Festival.

It left behind joy at a great victory—and a sorrow heavier and greater still.

Three full days had passed like that. At last, Jin Mukyung had regained consciousness, and his younger brother had told him everything that had happened. Now that brother was walking away, growing smaller beyond the window.

Before he left, he’d left behind an old book.

*He asked me to give it to you. No—to hyung.*

Remembering his brother’s last words, tossed out as he walked through the door, Jin Mukyung blinked like someone who’d only just woken from sleep.

“…Ah.”

A stifled groan escaped him.

Through his vision, slowly clouding over, he could no longer see Jin Taekyung’s back.

Only the four characters written on the cover of the book resting on his knees stood out, sharply etched in his eyes.

Shura Annihilating Fist.

It was the last trace an old master had left in this world—and the legacy of his martial lineage, entrusted to the Sword Demon of the Jin Family of Taiyuan.

Another victim who’d fought back-to-back with him that day, three days ago, but hadn’t survived.

*Great Hero Cheol.*

Jin Mukyung thought of Cheol Mubaek, the Tiger of Mount Heng.

He’d risked his life to buy a moment for Mukyung as he fought a powerful enemy—the Demon Bird.

He remembered the last sight of him, grinning with bloodied teeth. He also remembered a day two years ago, when Cheol had come up to him as he was leaving the Mount Heng Sword Sect and asked, as if making a joke—

*“I hear you’re crazy about martial arts.”*

*“Pardon?”*

*“So, I was wondering—are you interested in Seowol?”*

*“I’m sorry, what are you talking about all of a sudden…?”*

*“Exactly what I said. I don’t have much to offer, so I can’t give you gold or silver, but if the two of you got together, I’d gladly give you the Shura Annihilating Fist manual…”*

*“Uncle Cheol!”*

*“Goodness. You’ll burst my eardrums. You’ve barely become Sect Leader and you’re already trying to boss me around?”*

It was strange.

He’d thought of Cheol as no more than a passing connection. So why was the sound of his hearty laughter so vivid in his memory?

Why did this heavy ache press down on one corner of his chest?

*So that’s what this is.*

Only then did Jin Mukyung realize what the emotions surrounding him were.

Sorrow. Anger. And…

Self-reproach for what he’d already lost.

*If I’d been stronger. If I’d been just a little stronger that day.*

He could have protected them. He could have saved more people.

But he hadn’t.

Even though he’d tried with all his might, even though he’d swung his sword without rest through the pitch-black darkness where each day felt like ten years, he hadn’t been able to reach them.

*If it had been you instead of me—or you all—everything would have been different.*

The first time he met Cheongpung, Mukyung had felt a wall between them.

Jin Taekyung’s astonishingly rapid growth had rekindled the longing in his heart that had once died down.

He’d been called a genius from the day he first picked up a sword. But only after seeing the two of them for what they truly were had he finally understood.

If he’d been born with talent bestowed by Heaven, then those two had brought theirs down from Heaven.

*How can I… How can I reach you? How do I stop losing people?*

An indescribable whirlpool of emotions.

That was when Jin Mukyung, his eyes empty, stared out the window where his younger brother had disappeared.

*Tap.*

A faint sound came from the crack beneath the firmly shut door.

Then a familiar voice reached his ears.

“Hey, Mujin. Remember that time?”

Jin Mukyung’s eyes widened. He’d thought his younger brother had left, but now he heard his voice again. A stiff reply followed, stiff enough to sound awkward.

“Um. W-Which time do you mean?”

“You know, when we formed that recon squad and kept busting our asses.”

“Oh. Ah, yes. I remember.”

“Yeah, I saw a lot of things I wish I hadn’t back then. I just… at some point, I started feeling so pathetic and angry at myself. Why was I only this good? Why did all those people whose faces I’d gotten to know, passing them back and forth, have to die?”

“…”

“But you know what pissed me off the most?”

On the other side of the unseen door, Jin Taekyung leaned back against it and continued, as if talking to himself.

“This goddamn feeling never gets any easier, no matter how hard I try. Nothing changes.”

Jin Mukyung’s eyes trembled.

He clenched his fist with all his strength, forgetting even the pain, and squeezed his eyes shut. The voice continued in his ears.

“It’s always the same. I thought if I got stronger than I am now, I could stop bad things from happening. I thought if I could use Sword Energy and put out Force like it was nothing, I’d never have to go through shit like that again…”

A quiet sigh drifted through the crack beneath the door.

“No. That’s not how it is. I still feel like shit every time. It was just me being selfish.”

More, more, more.

The stronger a person became, the more they wanted. Their hopes grew grander, and their sense of responsibility swelled until it felt ready to burst.

Jin Mukyung thought of himself as a boy.

Had the boy who’d swung his sword endlessly simply because he loved it ever felt the kind of responsibility he felt now?

Back then, all he had was talent. He hadn’t even thought about restoring the family’s fortunes.

He listened as the voice continued to reach his ears, clearer with every word.

“But I know, right? If we just throw in the towel, it’s over.”

Jin Taekyung no longer waited for a reply. Hyuk Mujin, who’d been offering awkward responses like a puppet, didn’t either.

As if he were speaking for someone else to hear, Jin Taekyung continued.

“We just have to keep trying. Do the best we can with what we can do right now. If you despair and give up because nothing changes, that’s when hell really begins. Because later, you realize that all the effort you put in meant fewer people were taken from you.”

“……!”

“So just keep doing what you’ve been doing. Keep at it, like you always have.”

The bitterness in his voice slowly faded. A brief silence fell—and then, all at once, a fierce whistle cut through the air.

*Whoosh—thwack!*

“Ow! Why’d you hit me?”

“Answer me, you bastard. When someone’s talking, you’re supposed to give them a little something back. Don’t make it so damn awkward.”

“Seriously, you’re doing this now? You’re not even talking to me… Mmph, mmph!”

Hearing a strangled noise and the scrape of something being dragged away, Jin Mukyung smiled faintly.

Then, with a voice clear enough to slip through the crack in the door, he saw the unwelcome guests off as they left the pavilion.

“Thank you. Truly.”

It seemed they’d heard him. Their footsteps paused for a moment, then quickly disappeared.
## Chapter artifact 982

# Chapter 982

I’m a selfish bastard.

As long as I and the people around me can be happy, I hardly care what happens anywhere else.

But every now and then, I feel like I’ve changed somewhere along the way.

Like the time I got so concerned about someone beating himself up and crying that I put on a ridiculous little show.

“Sometimes, when I look at you, Captain, I get this feeling.”

It had been a while since I’d left the pavilion, practically running away from Jin Mukyung.

As we walked in silence, Hyuk Mujin suddenly spoke up. I answered him.

“Don’t think about it. No—just don’t say it.”

“Why not?”

“Because I don’t want to hear it.”

“It’s not because you’re embarrassed, is it?”

He was right.

That was why I’d been doing my best to ignore Hyuk Mujin’s gaze as he stared at me.

“It’s just…”

“Just what?”

“I somehow felt concerned, so I stuck my nose in where it didn’t belong. That’s all.”

And the words I’d said to Jin Mukyung through the door had been the conclusion I’d reached after a long time thinking about it.

I didn’t know if it was the right answer, but if it could comfort him even a little right now, that was enough.

In the end, most problems were solved through time and experience.

The answer wasn’t something someone else could give you. You had to find it yourself.

*This is only the first step for him.*

He was an unparalleled genius born of the Jin Family of Taiyuan, and in this world, at least, he was my older brother. But Jin Mukyung was only in his mid-twenties.

He’d spent all his time honing his martial arts, so his real combat experience could be counted on one hand. He still wasn’t used to the grief that came with it.

If I could bring him even a little comfort, I’d say a few embarrassing words like that tens or hundreds of times over.

Jin Mukyung’s heart and the direction of his steps were set toward the righteous path, without a hair’s breadth of deviation.

The more he grew, the more livable the world would become.

*Keep walking. Don’t sit down. Just keep walking, and walking, and walking.*

At the end of that road was an answer.

There was light.

I believed that.

With all my heart.

“But, Captain. Can I tell you something?”

“What?”

“This isn’t the right way. If we keep going, it’s a dead end.”

I fell silent for a moment, then looked at Hyuk Mujin in disbelief.

“Wait… Why are you only telling me now, you bastard?”

“Well, you suddenly got this intense look in your eyes and started making a cool face.”

“…”

I wanted to hit him.

I really did.

* * *

There had been far too much going on over the past three days for me to tell Jin Mukyung everything.

A great battle, with tens of thousands of enemies and allies tangled together.

Three days had already passed since the day the people of Shanxi won a great victory, but the fallout and aftereffects were severe.

When unexpected guests show up and make a mess of the place, cleaning up is ultimately the homeowner’s job.

From the very day we won, Jin Wikyung had more work than ten people could handle. Before he’d even recovered from the exhaustion of battle, he had to start dealing with the aftermath.

Of course, those around him didn’t just stand by and watch.

“From this moment on, I’ll give the Lesser Family Head three options. Listen to all of them, one by one, and then choose the one you like.”

The first to step forward was the Medicine King Hall Master.

At a glance, he looked like a stubborn old man. But with a menacing gleam in his eyes that didn’t match his calm tone, he glanced back and forth between the long needle in his hand and Jin Wikyung, then said:

“You can keep ignoring my orders and working until you ruin your health and die. Or you can get treated now, take it easy, and live a long life. Or, if you’d rather not drag it out, you can die by my hand. Which will it be?”

Only then did Jin Wikyung start taking proper time to rest. The people who saw it debated fiercely behind his back.

Was his face as pale as a corpse that day because he was exhausted—or because of the Medicine King Hall Master’s long needle?

Hyuk Mujin put it plainly.

“It was definitely the needle. Didn’t you see that old man’s eyes? If he hadn’t learned medicine, he’d probably have carved out a place for himself in Dark Heaven by now.”

In any case, what mattered was that Jin Wikyung had finally relented. And the help of others had played a large part in making that choice possible.

“That quack they call the Medicine King Hall Master is absolutely right. You focus on recovering. The others will take care of the rest.”

The battle on the Double Ninth Festival had ended in victory, but we still couldn’t be sure that every threat had disappeared.

Still, the very presence of a giant like the Fire King, Jeok Cheongang, was enough to wipe away even the slightest worry.

And so was the return of the Bow Saint, who had finally appeared before the world again after vanishing for decades.

“I’ll go to Hebei.”

The Bow Saint left immediately after the battle, leaving only that brief remark behind.

The Thunderbolt Saber King’s son, Peng Cheolyeong—the current Family Head of the Hebei Peng Family and the Iron Blood Saber—had no choice but to return to Hebei with her, leading the family members who were able to travel.

It was only natural.

The North Heaven Demon Lord—no, Murong Baek—hadn’t been the only one to betray us.

It meant the entire Murong Family had joined Dark Heaven. Two days later, the news carried by a messenger eagle to the Jin Family of Taiyuan proved that at least part of our prediction had been right.

“As we expected, trouble broke out in Hebei.”

Even though he’d been forced to rest by several people, taking documents out of Jin Wikyung’s hands was nearly impossible.

The instant the messenger eagle arrived at the Jin Family of Taiyuan, Jin Wikyung received the news. He immediately called me in and told me what had happened in Hebei.

“Looks like the Murong Family had been targeting both Shanxi and Hebei from the start. Under the pretense of coming to support us, they crossed Hebei while leaving part of their forces behind to launch a surprise attack on the Peng Family.”

The bloodshed that had swept through the region on the Double Ninth Festival hadn’t been confined to Shanxi Province.

Caught off guard by the Murong Family’s sudden betrayal, the Hebei Peng Family had suffered heavy losses. With the Thunderbolt Saber King and many of their strongest masters away, they’d barely managed to defend their family home after fighting to the death.

“But even that would only have bought them time. If everything had been delayed by two days, something irreversible would have happened.”

But just as the family stood on the brink of ruin, Peng Cheolyeong, its Family Head, finally arrived.

Behind him, accompanying the roar with which he announced his arrival, were more than five hundred family members who’d returned from Shanxi with him, along with several hundred martial artists from the Jinzhou Yan Family, a vassal family of the Hebei Pengs.

If that had been all, the battle would have been a hard one for the Hebei Peng Family.

They’d already suffered devastating losses in the surprise attack, and Peng Cheolyeong had only a thousand exhausted, hastily assembled troops at his command.

But leading them was a giant whom even Peng Cheolyeong, Family Head of the Hebei Peng Family, would not dare step ahead of.

“Once Senior Bow Saint made up her mind, the outcome was already decided.”

It was another victory for us—and a terrible defeat for the Murong Family.

A defeat that deserved to be called unrecoverable.

And so the Murong Family was annihilated.

Several dozen enemies, including its Lesser Family Head, Murong Yeonghwi, barely escaped the battlefield and vanished. But who knew?

“Unless they have a Moving Formation hidden somewhere, they’ll be caught soon enough. Our eyes are everywhere.”

Jin Wikyung’s confidence wasn’t an empty boast.

Even if the dark clouds cast by Dark Heaven eventually covered everyone’s heads, for now, the orthodox Murim factions still ruled the land.

The Murong Family had made an enemy of the world.

Unless they could break through the Jin Family of Taiyuan and the Hebei Peng Family, there was no way to escape into the vast Central Plains. To the east, the Great Nation’s warships guarded the open sea.

And the Great Steppe—their roots and little more than the final destination for outlaws—was already practically under the Jin Family of Taiyuan’s control.

“Release the tribespeople to hunt them down. Even if it takes them to the ends of the earth.”

It wasn’t a request.

As Shanxi’s Alliance Leader, the great victor, and the master who had broken a defeated hunting dog to heel, Jin Wikyung gave his first order.

“You wouldn’t want to leave trouble for the future, either. Would you, Temur?”

“I… will obey.”

The young chieftain who had once dreamed of uniting the vast steppe as its Great Khan submitted helplessly.

It was only natural.

He was a defeated commander who had betrayed his brothers and his tribespeople because he feared death.

As for the former, he’d been given a pretext—that he’d fallen into Jamukha and the North Heaven Demon Lord’s schemes—and the false absolution that submitting to the Jin Family of Taiyuan had prevented even greater losses. But the latter was different.

If the whole truth came out, Temur would die.

Not at our hands, or Dark Heaven’s—but at the hands of his own tribespeople.

That was the leash Jin Wikyung held tight. The hunting dog couldn’t even think of betraying him.

From the moment Temur accepted Jin Wikyung’s offer and joined the attack on the Murong Family, all his other options had effectively disappeared.

*It’s disgusting, but now that we’ve got a leash on him, we need him on our side.*

How many lives had Temur’s petty cowardice and instinct for survival cost?

“Go. You’re pissing me off just standing there.”

Temur lowered his head at my contemptuous words and left. Then I called over the man who could take care of the remaining problem for good.

“You called?”

His brilliant golden armor drew everyone’s eyes wherever he went.

His expression and speech were as stiff as the helmet tucked under his arm.

I looked at Jeong Hogun, Thousand Captain of the Embroidered Uniform Guard, and deliberately frowned.

“What’s with you? Why do you look so fine?”

“Because I fought well.”

“Or did you just show up at the end and take all the credit?”

“Is that what you say to a Benefactor who traveled thousands of li to help you?”

“Hey, you’ve got to remember that I helped you first. What would you have done if I hadn’t been there at the Imperial Palace?”

“What would I have done? The Bow Saint would have helped.”

“…Huh. Now that I think about it, you’re right.”

“…I didn’t expect you to admit it just like that.”

A brief silence settled between us. Then, as if on cue, Jeong Hogun and I both chuckled.

I’d been teasing him for no reason, but I was grateful to the guy.

Just as he was grateful to me, I felt the same way about him.

“I called you because I have a favor to ask.”

“A favor?”

“Yeah. It might be a little—or rather, a pretty difficult favor.”

“Someone might die.”

I quietly nodded. Jeong Hogun answered without a moment’s hesitation.

“Then I refuse.”

“Ah.”

His tone was as sharp as a blade.

I swallowed a groan at his unexpected, unequivocal refusal. Then Jeong Hogun continued in a low voice.

“An order.”

“What?”

“I can’t grant a personal favor. But an order is different.”

Only then did I understand what Jeong Hogun meant, and I gave a short laugh.

“Why go this far?”

“That is the law of the Great Nation’s military.”

He was an interesting guy.

And for a moment, I thought that it was people like Jeong Hogun who made a nation like the Great Nation possible.

Then, as he wished, I spoke.

“Jeong Hogun, Thousand Captain of the Embroidered Uniform Guard.”

Jeong Hogun bowed his head with a respectful expression, as if nothing had happened.

“Give your order.”

“Lead the Embroidered Uniform Guard under your command to Liaoning.”

Liaoning Province.

The Murong Family’s stronghold—and the last trouble waiting to be dealt with.

At my order, Jeong Hogun struck his armor.

“I receive the command of the Marquis of Shangshan.”
## Chapter artifact 983

# Chapter 983

By the time the thousand Embroidered Uniform Guards led by Jeong Hogun crossed Hebei and reached Liaoning Province, not only the martial artists in the region but even the common people knew the whole truth.

The nomads’ invasion. The Murong Family’s betrayal.

And, finally, the existence of Dark Heaven lurking behind it all.

For that reason, not even the most hot-blooded martial artists dared stand in the Embroidered Uniform Guard’s way.

There were two main reasons.

The first was the force and authority of the Embroidered Uniform Guard, one of the Great Nation’s finest elite forces. The second was another banner flying alongside the imperial flag.

The Murim Alliance.

Even a renowned veteran of the martial world who had loudly insisted that martial artists should handle Murim affairs themselves would have had no choice but to accept it quietly before the Murim Alliance’s towering banner.

Now that the two great powers guiding the world had joined forces, all that remained was to punish the Murong Family.

Before long, everyone’s attention focused on one place.

Shenyang, Liaoning Province.

The home of the Murong Family, which had once founded a nation after thundering across the continent with a single charging spear and a composite bow.

Now, it stood on the brink of ruin.

“Surround it.”

Thud-thud-thud-thud!

Jeong Hogun’s terse command shook the earth.

There was no need for all thousand Embroidered Uniform Guards to take action.

The authority of the Marquis of Shangshan, personally appointed by the Son of Heaven not long ago, was vast enough to encompass the entire northern frontier. And when the Embroidered Uniform Guard—the force said to knock birds from the sky—arrived, Liaoning Province’s City Lord had rushed out to greet them and immediately handed over every military force at his disposal.

Thud. Thud. Thud.

The first thousand cavalrymen galloped out to surround the Murong Family estate. Heavily armored infantry filled every gap with shields, spears, and swords.

Finally, the archers took their positions. Everything was ready.

Like any Murim family on the frontier, the Murong Family estate was a fortress made by nature itself. And now it was sealed off without a single gap.

Grrrrrr.

With a heavy grinding sound, the iron gate slowly began to open.

A man dressed in white as snow appeared beyond it. Jeong Hogun spoke.

“Loose.”

The order came without the slightest hesitation.

The archers, already in formation and prepared for this moment, knew what to do.

Fwoosh!

For an instant, part of the sky turned black. Hundreds of arrows cut through the air and fell with deadly force. The man in white frantically swung his sword in front of them.

Clang-clang-clang!

Steel met steel, sparks flying.

When the storm of arrows swept past the gate, all that remained was the man, his face stricken, and the anguished cries of those calling out to him.

“Young Master!”

“You mustn’t! Please, come back!”

“What are you doing? Bring the Young Master back—!”

The man firmly waved them back instead of answering. He bit his lip, fixed his gaze on Jeong Hogun in the distance, and took a heavy step forward.

Step.

Jeong Hogun watched him in silence, then spoke again.

“Loose.”

Once more, a rain of arrows fell, and the blade flashed.

But this time, there was one difference: blood was now spattered across the ground.

Thud-thud.

The shoulder pierced by an arrow began to twitch. But the man’s steps didn’t stop. He continued forward until some of the arrows in the third volley pierced his body.

Thwack!

At last, the man’s knees buckled. His once-white clothes had long since turned red.

Still, when the members of the family could no longer bear it and rushed out through the gate, his shout held not the slightest trace of pain.

“Stop! Have you all forgotten my orders?”

“B-but—!”

“Don’t come any closer. No matter what happens, you must not act rashly!”

The family members who had started to run through the gate clenched their teeth and stopped.

The man gave a small nod, then used his sword as a cane to stagger back to his feet.

At last, he faced Jeong Hogun, who was slowly riding toward him.

“We finally meet. I suppose it was worth risking my life.”

Jeong Hogun looked down at him quietly from the saddle.

Up close, the man was a young man who looked barely twenty.

“Are you of the Murong bloodline?”

“I am. My father committed a crime that cannot be forgiven.”

They said blood could not lie.

Looking at the young man’s distinctly foreign features, Jeong Hogun suddenly recalled a face he had seen while collecting the dead, just after the fierce battle around Eight Spring Gorge had ended.

“Then, are you Murong Baek’s…?”

“I was his seventh son, born in his old age. The son of a sinful father.”

The young man answered calmly and cupped his hands in greeting.

“I am Murong Su, the Murong Family’s Seventh Young Master. I greet Thousand Captain Jeong.”

“You know who I am.”

“I have eyes and ears of my own. I heard you were coming, of course.”

“Then why did you stay here?”

“If I fled like my elder brothers, I would be admitting with my own actions that I was a traitor and an enemy of the Murim world.”

“Nothing will change just because you stayed. Still, let’s hear your second reason.”

The young man, Murong Su, lowered his hands and lifted his head.

His gaze at Jeong Hogun was clear, and his voice was calm.

“Someone has to take responsibility, don’t they?”

“…Responsibility.”

“I’m the only direct descendant left at the family estate. Everyone connected to the crime has either died or fled.”

Beneath his deeply pulled-down helmet, Jeong Hogun silently looked at Murong Su. Then his gaze shifted past the young man’s shoulder.

“Then who are those people who stayed with you?”

“I don’t know if you’ll believe me, but they, too, were betrayed by my father. And they aren’t people who could really be called members of the Murong bloodline.”

From Murong Su’s answer, Jeong Hogun could guess the identities of the people who had stayed behind.

People so excluded within the family that they could not have come close to the truth.

They must have been distant branches of the family, or people whose temperaments simply hadn’t fit with the rest.

And among them were surely former guests who had become part of the Murong Family without sharing a drop of its blood.

With only one exception.

“Did you not know about your father’s crimes, either?”

“I neither knew nor didn’t know. I only had a vague sense that something was wrong.”

“And?”

“I simply watched from a distance.”

“Was it your affection for your own blood?”

“I don’t know when I became a member of the Murong Family, seeing as I’m the son of a barbarian mother, born of low status, with little martial talent to speak of…”

Murong Su continued with a bitter smile.

“But there’s one thing I know for sure. The best I can do is save the people who remain.”

“So in the end, you’re the only one left. Murong Su, Murong Baek’s son. A traitor’s blood.”

“That’s right. So, the others—”

“Execute them on the spot.”

At Jeong Hogun’s firm interruption, all color drained from Murong Su’s face.

“What do you mean—”

“The Murong Family Head, Murong Baek, and his family colluded with foreign enemies, disrupted the order of the Great Nation, and caused immense harm throughout the northern frontier. This was clearly an act of treason. Not the slightest mercy can be shown in punishing it.”

“Thousand Captain!”

Blood mingled with the cry he forced out.

Crack. Murong Su snapped the arrows lodged throughout his body. His face was painted with an anguish beyond words.

“Didn’t I tell you? They—they…”

He coughed, spitting blood.

Murong Su fell to his knees, unable to finish speaking. At that moment, the family members who had watched every second of the scene from a distance could no longer bear it. They rushed through the iron gate.

“Young Master!”

“No! The Young Master is innocent!”

As they ran toward him, crying out in desperation, Jeong Hogun slowly raised a hand.

In Murong Su’s wide-open eyes, he could see hundreds of archers drawing their bows taut.

There was no choice left.

One small gesture. Or one short command.

And it would all be over. Everything.

“N-no! Please, stop!”

Murong Su’s desperate plea broke through with a spray of dark red blood.

And then, a hoarse old voice spoke from behind Jeong Hogun.

“People only show their true hearts when their lives are in danger. Don’t you agree, Thousand Captain of the Embroidered Uniform Guard?”

It was a small, elderly man.

His skin was dark, and his striking features made it clear he was not Han.

But what made the old man look especially unusual was that he wasn’t riding a horse or a mule. He was riding a person.

A huge man, one who could be compared to a bear.

“Taishan can’t understand what you’re saying. Has Namho gone senile?”

“Damn it, you’re at it again.”

The old man, Namho, didn’t flinch.

As if he had been waiting for the moment, he pulled out a chunk of jerky and stuffed it into Taishan’s mouth. Then he nodded toward Jeong Hogun.

“Anyway. In this old man’s opinion, this is probably enough for now. What do you think?”

After a moment’s thought, Jeong Hogun lowered his hand.

As his fingers slowly relaxed, hundreds of taut bowstrings lowered in silence.

“First, we’ll escort them to the government office. We’ll decide how to deal with the survivors after a thorough interrogation.”

“Do that. An old man like me doesn’t have the power to stop you from going that far. Even that much is more than they could have hoped for.”

Namho shrugged, then patted Taishan on the crown of his head.

The enormous man lowered himself, bringing Namho roughly eye to eye with Murong Su, who could only blink, still unable to make sense of what was happening.

“Did you say your name was Murong Su?”

“Y-yes. But who exactly are you, Old Man?”

“You don’t need to know the name of an old man like me. Just know that I belong to the Murim Alliance.”

“The Murim Alliance…!”

“Oh, one more thing. I’m also the Blazing Flame Divine Dragon’s—no, the Marquis of Shangshan’s representative.”

Namho smiled bitterly at Murong Su’s face, which had gone stiff as stone.

“Don’t look so surprised. I’m only offering you a chance.”

“A chance…?”

“Yes. A chance for those who haven’t strayed from the orthodox path.”

Namho knew.

No—Jin Taekyung knew.

Even in deep darkness, there was light. And even in a brilliant beam of light, there was darkness.

That was exactly why Jin Taekyung had sent Namho here.

Eliminating a future threat didn’t always mean eliminating the people themselves.

If what remained was not diseased grass and trees, but strong, green shoots, there was no reason to rip them out by the roots.

*“If we’re the orthodox faction, shouldn’t we at least live up to the name?”*

Remembering what Jin Taekyung had said before leaving the Jin Family of Taiyuan, Namho smiled faintly.

Then he spoke to Murong Su—and to all of them, the entire group who had run breathlessly to his side despite being reduced to barely a hundred people.

“From this moment on, the Murong Family no longer exists.”

“…”

“Those who abandoned benevolence and righteousness and strayed from the orthodox path can no longer belong to the Murim Alliance’s orthodox factions, nor can they be a great family.”

His voice was so powerful that it was hard to believe it came from such a small man. Though he hadn’t infused it with a single scrap of internal energy, every word rang clearly in their ears.

“But if anyone still walks the right path, the Murim Alliance will not cast them aside. That is the right thing to do.”

Namho fixed his eyes on Murong Su and continued.

“As I said, the Murong Family no longer exists. But the Murong household is another matter.”

This wasn’t a decision he had made on his own.

Every sect in the north had agreed to it. The Murim Alliance had decided.

“If your innocence is proven in the future, the Murong family will have another chance to prove itself under a new Family Head.”

“…”

“…”

At that moment, the hundred or so members of the family trembled.

A final chance had been given to people who had thought everything was over.

They had been given the chance to prove their innocence—to prove themselves.

All thanks to the sacrifice and courage of the one man who hadn’t abandoned them to the very end.

“Young Master!”

No longer retainers of the Murong Family but of the Murong household, they surrounded Murong Su with fervent voices and shining eyes.

The man they would soon call their Family Head.

As Namho watched the scene with a calm gaze, he suddenly remembered something he had forgotten and smiled faintly.

The Five Great Families.

Together with the Nine Sects and One Gang, they were the fifteen pillars holding up the vast world of the Nine Provinces.

He already knew who would fill the fifth empty seat, left behind by the Murong name.

No—in fact, all the martial world knew.
## Chapter artifact 984

# Chapter 984

The saying that words without feet can travel a thousand *ri* was wrong. They could travel ten thousand—or even farther—in the blink of an eye.

The chain of events in the north spread with astonishing speed, and without end.

From person to person, on the beating wings of messenger eagles, and with the pounding hooves of horses galloping behind messengers’ hurried whips.

Before long, the fallout from the truth that had come to light was enough to shake the entire Central Plains.

“How could the Murong Family…!”

“That’s impossible. It can’t be true!”

Disbelief was the first emotion martial artists felt when they heard the news.

Of course it was.

The traitors exposed before the whole world weren’t groups rooted in demonic, heterodox arts, like the Yangtze River Channel League or the Green Forest Alliance. They were none other than the Murong Family.

One of the Five Great Families of the world.

Though based at the very edge of the north, it was a true great family, renowned from the vast lands of Liaoning all the way to the Central Plains.

And yet that very Murong Family had supposedly joined forces with Dark Heaven.

Worse, it wasn’t the work of a few disloyal members. Most of the family, including its Family Head, Murong Baek, had been involved.

The shock this unbelievable news dealt to those who heard it was beyond words.

“The Family Head, the Divine Spear of the Imugi, was a man who distinguished himself in the Great Faction War. Why would he—or the Murong Family—do such a thing…?”

But their disbelief lasted only a moment.

The Beggars’ Sect, the Lower District Sect, Huashan, and the Hebei Peng Family—

and the Murim Alliance, the heart of the martial world—

all officially confirmed that every word of it was true, without the slightest falsehood.

Even the giant beyond the martial world—who existed, yet might as well not have—confirmed it.

“Clear the way!”

Groups of government soldiers, some with dozens of men and others with hundreds, swept through the land.

They had once leaned against their spears, spending their days with languid faces in a peace that had lasted so long. Now, fully armed, they carried out their orders with eyes sharp beneath their helmets, watching every direction.

“Hey, what’s going on?”

“How should I know? But with things this tense, I’d guess it has something to do with whatever happened in the Imperial Capital recently.”

“Oh, I heard about that too. You mean those bastards called Dark Heaven? I heard from a martial artist I know that they went on another rampage…”

This wasn’t happening in just one place.

Seeing the soldiers’ sudden change in demeanor, people gathered, feeling both alarmed and on edge.

Before long, they were able to read the proclamations the soldiers had posted all around before leaving.



Let it be known to all under Heaven, to all the people:



That was how the proclamation began. It had been written in a single flowing hand by the finest men of letters in each province. Pressed forward beneath the gazes of the crowd, the scholars who stepped up to read it aloud found their voices trembling more and more as time went on.

“…Th-therefore, I shall join forces with the martial men outside government service to make an example of the traitorous band known as Dark Heaven. This is my will and Heaven’s decree.”

Even after the lengthy recitation ended, the gathering remained silent as the grave.

Those who understood the proclamation stared wide-eyed, like the scholars reading it. The country folk who didn’t understand shifted their eyes from side to side and whispered under their breath.

“What in the world does that mean?”

“I don’t rightly know. Seems like ‘martial men who don’t belong to the government’ means martial artists, though… Couldn’t they just say it plain? Why’d they have to write it so fancy?”

They were people who lived one day at a time, earning what they ate.

They had been born with nothing to learn but hard work and how to use their bodies. Their pockets were always light, but their shoulders weighed a thousand *geun*. How likely was it that they could read a line of writing properly?

But there were always people who couldn’t stand silence and ignorance.

“It is an imperial decree personally issued by His Majesty. He has declared Dark Heaven a band of traitors and announced to all his people that he will join forces with the martial artists of the world to punish them.”

Only then did people look down.

Beneath the tiny letters, a clear seal had been stamped.

It was the mark of the imperial seal, an object reserved for only one person in all the vast Nine Provinces—one that countless people had never even seen.

Even the illiterate could tell at a glance that it was no ordinary seal.

“This is more serious than I expected. They’re even calling on the martial world to lend its blades and spears.”

At the young scholar’s sudden remark, someone else murmured with a sigh.

“I’ve heard all the rumors about Dark Heaven, but… I never thought it was this bad.”

The first to hear news from every corner of the world were martial artists and merchants.

People outside those circles rarely had their ear to the ground unless they had special connections. And even when something happened, in truth, they didn’t give it much thought.

The Great Nation stood on a firm foundation.

The countless purges and provincial warlord rebellions that had followed its founding were long over.

With the passage of time, the world had settled into peace. Even during the calamity more than fifty years ago that martial artists called the Great Faction War, the common people had suffered almost no harm.

Why?

It was simple.

Even the fanatics from far to the west, who bore the chilling name of the Demonic Cult, had feared the Great Nation joining the war.

They had wanted it to be seen as nothing more than a struggle between martial-world factions.

But…

“This time will be different. Unlike any other.”

Even when Shaolin Temple’s Abbot, once considered the equal of a living Buddha, entered nirvana and the grounds where only peaceful wooden fish once sounded ran red with blood, no one there had felt anything beyond sorrow.

It was the same when they heard that the Daoists of Qingcheng and Emei, who seemed like immortals, had fallen, and that the Sichuan Tang Clan—whose people were known even among ordinary folk as a fearsome bunch—had suffered terrible losses.

That was the Murim everyone knew.

In that cruel forest, where spears and swords ran wild in place of green trees, even venerable monks and Daoists could die at any moment.

No, there was another reason they had watched everything without much concern.

*Come on. Whatever happens, surely it won’t reach us.*

They lived in different worlds, behind different walls.

The people had entrusted their safety to the Great Nation’s walls. All they had done was watch the martial artists fight their fierce battles in their own domain.

Now and then, they pitied the unlucky common folk caught up in Murim affairs and killed. But that was all.

A fire blazing hundreds of *ri* away couldn’t warm everyone.

The people’s feelings and attention burned hot for a moment, then quickly cooled.

Compared to the whole, the victims were only a handful, a tiny minority. The rest could wake up tomorrow just fine.

They had the Great Nation, a great and sturdy wall.

But that unshakable faith was crumbling to pieces at that very moment.

“W-wait, sirs. Then what you’re saying is…”

Gulp.

The old scholar spoke for the village elder, who couldn’t continue and could only swallow dryly.

The truth no one wanted to believe, or even hear.

The truth they had no choice but to face.

“That’s right. It’s exactly what you think.”

A quiet sigh escaped him.

The old scholar looked down at his wrinkled hands, etched with the marks of time.

He thought of how they had once been white and smooth.

He thought of his younger self, who had been unable to go any farther, blocked by an age of chaos that refused to end despite all the possibilities that had once lain before him. He thought of those turbulent years.

Slowly, he continued.

“The war has already begun.”

“……!”

“……!”

Some clenched their teeth and fists. Others squeezed their eyes shut.

Soundless shock surged through the crowd like a wave.

The two characters for *war* spread in every direction, carried on wide-open eyes and slackened lips.

Along broad avenues, through narrow, dark alleys, and in the hurried footsteps of those rushing to carry the unbelievable news onward.

War.

The flames of a great war that would burn everything to ash.

At that moment, the old scholar saw it.

The darkness that had slumbered for so many years had finally awoken, painting everyone’s faces with despair.

And suddenly, he silently mouthed the unfamiliar name that appeared in the proclamation, beneath the imperial decree as lofty as the heavens.

Jin Taekyung of the Jin Family of Taiyuan.

No—the Marquis of Shangshan, Jin Taekyung.

The foremost contributor to stopping this rebellion, a martial artist so young he was barely more than a boy, and yet raised to the rank of marquis.

*I don’t know much about the affairs of the martial world… but one thing is certain.*

The old scholar had once served in government. He could guess well enough what future awaited that young martial artist, who had achieved something without precedent—and something that would never be repeated.

*I don’t know who you are, but please, give it everything you have and keep moving forward. Not only for the martial world you’ve always known, but for this country as well.*

Along with words that would never reach him, the old scholar bowed toward the proclamation.

First, to the Son of Heaven, who watched over all things from the distant Imperial Capital.

Second, to the countless departed spirits who would shed their blood and fall to protect this world.

And lastly, to the new marquis who stood at the heart of the martial world by virtue of the solemn imperial decree.

The old scholar continued to bow.

In full view of the crowd, he did so quietly and without complaint, giving everything he could in the way of sincerity and respect.

And thousands of *ri* away, in a narrow gorge, bright yellow chrysanthemums were coloring the landscape in every direction.



* * *



I’d heard of the Double Ninth Festival a few times in passing, but that was about all I knew.

As a Korean born and raised, I’d always observed the big holidays like Lunar New Year and Chuseok. But I didn’t have so much time on my hands that I could take an interest in the customs of those guys on the continent.

But today, I, too, followed the customs of the Double Ninth Festival.

I held an armful of bright yellow chrysanthemums, more than enough to overflow my arms, and awkwardly wore a pouch of cornelian berries at my side.

It was a way to honor those who had passed before they could celebrate the Double Ninth Festival themselves.[^1]

We had to keep moving forward, leaving their sacrifice behind us.

*Whoosh.*

Wind from far away stirred the chrysanthemums in my arms.

The wind came out of nowhere, insistently tugging the petals by the hand. Several, large and small, gave in and went along with it.

Before long, they fluttered through the air like a rain of flowers.

They swept along the Eight Spring Gorge, winding through it on the breeze. Long ago, the people who had lived in this land had given the place that name.

*Ah.*

I swallowed the exclamation that almost escaped me.

It was beautiful, and at the same time, unbearably sad.

And I wasn’t the only one who felt that way. Tens of thousands of people filled the Eight Spring Gorge, and I knew they felt it too.

Watching the yellow petals fall, I found myself wondering: Even now, as they drifted farther and farther away with the wind, were they only petals? Or were they the souls of those who had willingly thrown away their lives to protect what they cherished?

There was no single right answer.

There was no need to find one.

We could believe whatever we wanted to believe. Whenever this day came around, we would return here and remember them.

Each in our own way.

With laughter. With chrysanthemums and cornelian berries.

Or…

With tears.

Drip. Drip, drip.

My senses, far beyond the limits of human beings, sometimes gave me information I didn’t want.

Like the tears wetting the leather shoes of a man whose head was bowed and whose body was trembling slightly.

No, like raindrops.

*Yeah. That’s how it is.*

I quietly looked up at the sky.

I couldn’t bring myself to look at Jin Wikyung like that, or at Lee Seowol silently mourning the death of her uncle, who had been her strongest support, or at the countless others in tears.

*Whoosh.*

The wind blew again.

A shower of flowers rose high, then fell, wrapping around everyone as if to comfort them.

Yet beneath the clearest sky imaginable, countless raindrops kept falling.

The Double Ninth Festival had passed, but the chrysanthemums hadn’t withered.

I knew that those who had left and those who remained were all here together.

And I knew, too, that because of them, the road we had to walk from here had grown wider and brighter.

*Ding.*

A clear chime rang out in the sky, mingling with the shower of flowers.

[^1]: On the Double Ninth Festival, people traditionally wore cornelian berries and admired chrysanthemums.

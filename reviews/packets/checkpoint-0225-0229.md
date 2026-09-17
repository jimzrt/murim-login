# Checkpoint Review — 225–229

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

# Chapters 225–229

## Plot

Jin Taekyung and Butler Kim defeat the Star Guild ambush. Butler Kim uses Earthquake to incapacitate the attackers, while Taekyung tests Won Myunghoon’s surrender and kills him when Won launches a concealed attack. Kim Jonghun is found bound and gagged, and the Gate opens unexpectedly as the survivors emerge before waiting reporters.

Taekyung gives HunterTV an exclusive live statement revealing that The Black Wyvern’s Nest was a Mutated Gate containing the Named Monster Carus, whom he killed. The investigation confirms the deaths of seven raid participants and Won’s role in numerous crimes and cover-ups. Hidden footage and Jonghun’s confession expose Won’s wider wrongdoing, while prosecutors resolve the legal dispute over Taekyung’s killing in his favor.

Carus’s processed remains sell secretly at Christie’s to Qatar’s Prince Cheonsur for approximately 500 billion won, leaving Taekyung about 530 billion won after fees. He establishes a Peace Guild support foundation for the families of fallen comrades, Great Cataclysm veterans, and single-parent families. After discussing the money with his mother and Hayeon, he prepares to move them into their former family home.

Before dawn, Taekyung asks Jeok Cheongang to teach him martial arts. Jeok accepts and departs with him for a year of training in Anhui. Taekyung tells Jin Mukyung that he and Cheongpung will attend the Star-Array Grand Banquet in one year. Cheongpung claims Mae Jonghak permitted him to become Jeok’s Disciple and follow Taekyung, while Baek Museong remains uncertain whether to escort him to Huashan or search for Mae. Jin Wikyung entrusts Taekyung to Jeok and reserves an important private discussion with him before departure.

## Continuity

- Won Myunghoon is dead. Taekyung killed him after Won violated his surrender with a concealed Aura-infused dagger attack; the System recorded Won as Level 80 and awarded EXP.
- Butler Kim is an A-Rank mage whose Earthquake can incapacitate roughly a dozen veteran B-Rank Hunters.
- Kim Jonghun survived the ambush and confessed the Star Guild’s crimes while mentally shaken.
- The investigation confirmed that seven raid participants died in The Black Wyvern’s Nest; Won’s death made eight.
- Leaked footage from a concealed PSV-96K camera exposed Won’s crimes, cover-ups, and connections to political and business figures. Prosecutors resolved the self-defense dispute favorably for Taekyung.
- Carus’s remains sold for approximately 500 billion won. Taekyung is directing hundreds of billions through a Peace Guild support foundation and plans to support his family financially.
- Taekyung has left immediately with Jeok Cheongang for a year of martial-arts training in Anhui.
- Jin Wikyung has an important private matter to discuss with Jeok before or during the departure.
- Taekyung and Cheongpung intend to attend the Star-Array Grand Banquet in one year; whether Jin Mukyung will attend remains unresolved.
- Cheongpung claims Mae Jonghak authorized him to become Jeok’s Disciple, but Mae has been missing for over a month. Baek Museong’s decision to escort Cheongpung to Huashan or search for Mae remains unresolved.
- Jin Mukyung continues isolated training: ten thousand sword strikes without internal energy, plus one hundred strikes for every mistake.
- Lee Seowol asked Taekyung to address her as Young Lady rather than Sect Leader. Chulwoo agreed not to pursue Eunhyang.

## Translation Decisions

- Retain “The Black Wyvern’s Nest,” “Mutated Gate,” “Named Monster,” “Carus,” “Yeti’s Necklace,” “Star-Array Grand Banquet,” and “Jeok Cheongang.”
- Render 어스퀘이크 as “Earthquake,” and retain “Aura,” “Fear,” and “Magic Gem.”
- Render the concealed camera designation as “PSV-96K,” Christie’s and Sotheby’s as named, and 3천억 as “300 billion won.”
- Render 처리했습니다 in Taekyung’s account of Won’s death as “disposed of him,” preserving the bureaucratic euphemism.
- Render 일만격 as “ten thousand strikes,” 추가 백 회 as “one hundred additional strikes,” 안휘성 as “Anhui,” 행낭 as “travel bag” or “luggage,” and 반 시진 as “half a shichen.”
- Render 소저 as “Young Lady” when referring to Lee Seowol’s requested form of address; retain “Young Lady Lee” in Taekyung’s address to her.
- Retain “Disciple” for Cheongpung’s claimed relationship to Jeok Cheongang.

## Durable state

{
  "active_continuity": [
    "Taekyung has left immediately with Jeok Cheongang for a year of martial-arts training in Anhui.",
    "Jeok Cheongang is responsible for guiding Taekyung during the journey and training.",
    "Jin Wikyung entrusted Taekyung to Jeok and reserved an important private discussion with him.",
    "Taekyung and Cheongpung intend to attend the Star-Array Grand Banquet in one year.",
    "Jin Mukyung is isolated in an unlit training cave, practicing ten thousand sword strikes without internal energy and adding one hundred strikes per mistake.",
    "Mukyung’s defeat by Cheongpung after roughly three hundred exchanges continues to drive his training.",
    "Cheongpung claims Mae Jonghak permitted him to become Jeok’s Disciple and follow Taekyung.",
    "Baek Museong will either escort Cheongpung to Huashan or search for Mae Jonghak after receiving a message from the main sect.",
    "Taekyung warned Chulwoo not to pursue Eunhyang, and Chulwoo accepted the warning.",
    "Lee Seowol asked Taekyung to address her as Young Lady rather than Sect Leader."
  ],
  "continuity_sources": [
    229
  ],
  "open_questions": [
    "What important matter does Jin Wikyung need to discuss privately with Jeok Cheongang?",
    "Did Mae Jonghak actually grant Cheongpung permission to become Jeok’s Disciple, and where is Mae now?",
    "Will Baek Museong escort Cheongpung to Huashan or search the Central Plains for Mae Jonghak?",
    "Will Jin Mukyung eventually attend the Star-Array Grand Banquet?"
  ],
  "safe_through": 229,
  "temporary_decisions": [
    "Use ten thousand strikes for 일만격.",
    "Use Anhui for 안휘성.",
    "Use travel bag or luggage for 행낭.",
    "Use Young Lady for 소저 when Lee Seowol requests Taekyung’s address."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 225

# Chapter 225

Crack!

With a grisly sound, white teeth shot into the air.

They had been maintained so meticulously that they gleamed even in the darkness. It had all become pointless now, though.

“Puh-haaaack!”

Thud!

Won Myunghoon flew several meters before slamming his back into a tree and coughing.

The teeth that had remained in his mouth fell out in little clumps, mixed with blood. When he finally raised his head, his face was twisted in shock.

“H-How could this…”

It had happened in the blink of an eye.

And it wasn’t only Won Myunghoon. Every Star Guild member stared at me with an expression of disbelief.

“How? Because I’m stronger than you.”

“T-That can’t be.”

“Yeah. It can.”

At my breezy answer and the single step I took forward, Won Myunghoon’s body began to tremble.

“Don’t come any closer!”

“Did I come here? You’re the ones who were waiting for me.”

It was already too late to turn back. I intended to make sure they understood exactly what happened when they bared their teeth at me.

Perhaps sensing the danger, Won Myunghoon shouted as if throwing a fit.

“What are you waiting for, you bastards?”

“G-Guild Master.”

“There are only two of them! If we back down here, every last one of us is going to die!”

The Star Guild members had hesitated, but at his command, they raised their weapons. Won Myunghoon gritted his teeth around the few that remained.

“I’ll handle this bastard. Get the old man first!”

I stopped walking.

“What did you just say?”

“Why? Did I hit a nerve?”

Won Myunghoon snorted and glared at me with burning eyes.

“Jin Taekyung, you bastard. I don’t know what kind of bullshit trick you pulled, but it ends here.”

“Bullshit trick?”

“Don’t pretend you don’t know. You obviously found some high-performance acceleration Equipment somewhere and put it on…”

“Oh, that’s what you mean?”

I widened my eyes in surprise.

Won Myunghoon’s imagination was astonishing. He was somehow rationalizing the reason he had lost.

“That’s a pretty original idea. But compared to that, isn’t this hostage situation a little too cliché?”

“Cliché or not, the important thing is that it always works.”

“Maybe…”

I let my voice trail off.

While I exchanged those few words with Won Myunghoon, the Star Guild members charged toward Butler Kim with their tanks at the front.

“I think things might be a little different this time.”

“What?”

The moment Won Myunghoon questioned me, Butler Kim—who had been massaging his lower back—drove his long staff into the ground.

It was a light movement. Yet the power that flowed from the end of his staff shook the earth.

Then his deep voice rang out, like the final switch on a bomb.

“Turn it upside down. Earthquake.”

Rumble!

The primeval forest trembled violently.

Cracks split the solid ground. Dirt and rocks shot into the air, exposing the trunks of trees that had sunk their roots deep into the earth. Flocks of nameless birds took flight.

—Screeeech!

They were the only ones able to escape the earthquake.

Unfortunately for the Star Guild members, they had no wings. The cracked and shattered ground surged up like triangular waves and swallowed them whole.

“Everyone, get out of the way—urk!”

“Gyaaaaaaah!”

Rooooar!

After the waves swept through, only groans and screams drifted sporadically through the forest.

The Star Guild members were crushed beneath an enormous weight of earth and rubble, barely able to keep their heads above the surface as they gasped for breath.

The man who had rendered around a dozen veteran B-Rank Hunters incapable of fighting with a single spell could not have looked more at ease.

“Young friends, you have no manners toward your Senior. Relax and close your eyes, all of you. Unless you want to be buried alive.”

It was a chilling voice, unlike anything I had heard from him before.

Only then did the Star Guild members realize Butler Kim’s true abilities. Their faces went pale as they lowered their heads.

Well, except for one person.

“An A-Rank mage…!”

A-Rank Hunters were rare, but A-Rank mages and healers were rarer still. The Star Guild members had probably never expected Butler Kim—who always kept his hands folded behind his back and laughed amiably—to be an A-Rank mage.

I grinned at Won Myunghoon, whose body was trembling.

“The hostage situation failed. What are you going to do now?”

“……”

“That’s why I told you not to bare your teeth.”

Won Myunghoon had been standing there blankly, like a man whose soul had left his body. At last, he managed to open his mouth.

“What are you? What are all of you?”

“You already know. The Peace Guild. We want to live up to our name, but the people around us won’t cooperate.”

Won Myunghoon bit his lip.

He could never have imagined that one wrong choice would lead to a result like this.

But it was already too late to turn back. A hyena cornered at the edge of a cliff had only two options left.

*Run. Or submit.*

Won Myunghoon chose the latter.

Clang!

The spear slipped from his hand and rolled across the ground.

“……I surrender.”

“You surrender?”

I walked toward Won Myunghoon. After kicking the fallen spear far away, I watched as he lowered his head in resignation.

“This suddenly?”

“……”

Even though I was standing right in front of him, he did not move. I asked the man who refused to answer with his head bowed.

“Once you get out, you’re looking at life imprisonment at minimum. You know how serious a crime what you did in a Gate is, don’t you?”

After hesitating, Won Myunghoon spoke.

“Because it’s better than dying.”

“Better than dying… Yeah, that’s true.”

If he survived, there would still be a chance. Death, on the other hand, was absolute. Whatever lay beyond it was something he would find out afterward.

People with a lot to lose were afraid of death. Won Myunghoon was one of them.

“Raise your head.”

“……All right.”

I stared into his eyes.

In those twin pupils, dark as an abyss, some unknowable light swirled.

Fear of the future that awaited him. Anxiety over death.

And then…

Thump!

“Taekyung. Please.”

“……”

“Just once. Give me one last chance. Killing a man like me will only leave you with a bad taste in your mouth.”

“It’ll leave a bad taste, but you won’t be punished. If you’re threatened with murder in a Gate, self-defense is recognized. You know that too.”

“B-But still.”

Won Myunghoon swallowed hard.

“If you kill me, it’s murder. The fact that you’ll become a murderer won’t change.”

Murderer.

The word rolling around on the tip of my tongue left a foul taste.

I looked down at Won Myunghoon, who was kneeling and begging for his life in a servile voice, then opened my mouth.

“I’ll trust you.”

“Taekyung!”

“One favor. Don’t betray my trust.”

I tossed him a rope with instructions to bind himself, then turned around.

That was when—

“Ha-ha-ha! You stupid bastard!”

A shout filled with joy rang out, followed by killing intent from behind me.

I turned my head and saw Won Myunghoon charging right up to me. Somehow, he was holding a dagger infused with Aura.

“Die!”

Whoosh! Slash!

Blood sprayed into the air with a short rush of displaced air. The joy that had brightly lit Won Myunghoon’s face gave way to puzzlement.

“……Huh?”

Thud.

A moment later, something fell to the ground.

It was a wrist, severed cleanly at the joint, still clutching the dagger whose Aura had vanished.

“That should’ve been twice as fast.”

I shook the blood from the dagger in my hand. In that brief instant, I had drawn a weapon from my Inventory, and the fight had ended in a heartbeat.

A short silence—but one that felt like an eternity.

Then Won Myunghoon’s mouth slowly fell open, and a horrific scream burst forth.

“Gyaaaaaaaaaaah!”

As I watched him writhe in agony, my heart remained as calm and peaceful as a lake.

I felt no sense of betrayal at having trusted someone who should never have been trusted. Not even the slightest regret.

Because…

“Thanks. For doing exactly what I believed you would.”

I had never trusted Won Myunghoon in the first place.

Not since the moment I received Yeti’s Necklace. Not since the moment he ignored my warning and bared his teeth at me again.

“You were exactly that kind of person.”

“Urgh, gyaaaaah!”

“If I leave you alive, you’ll bare your teeth at me again someday. Like a thorn lodged in the throat, you’ll find some way to come back if you survive.”

Slice. Slice.

My dagger severed the tendons in his calf. Blood spattered, and his knee buckled. Just as I pressed the razor-sharp blade against his neck—

“Hunter Jin Taekyung!”

Several dozen meters away, Butler Kim was watching me with a look of concern.

“There is no need to go that far.”

“That’s right. That’s why I let him go once.”

“But killing a monster and murdering someone are different. I’d rather do it myself—”

I replied in a calm voice.

“I know.”

“……Pardon?”

“I already know that very well.”

How many people had I killed by now? Dozens? No, a hundred?

The world I had lived in had never been forgiving. In Gates, I had to kill monsters. In the Murim, I had to kill people.

I was no lofty junzi. I was a Hunter and a martial artist with a family and people I had to protect. If it was necessary to survive or become stronger, I was willing to get blood on my hands.

To me, there was no great difference between a monster and Won Myunghoon before me.

*Because he’s an enemy.*

Whoever that enemy was, if they were capable of harming me or my people someday, the right thing to do was to eliminate the source of the trouble.

“So don’t stop me.”

“……!”

Butler Kim had also fought his way through countless battlefields.

He must have understood from that brief conversation alone. What kind of person I was, and what decision I had made.

He regarded me with a grave look, then gave a small nod.

“Urgh. P-Please, spare me…”

“Spare you?”

I looked down at Won Myunghoon as he groaned.

He had once been the idol I looked up to as a child—the man who shone brighter than anyone among countless stars.

But I would put those old memories of him in a time capsule and bury them deep underground.

I whispered in a quiet voice.

“If you were going to try to kill someone, you should’ve been prepared to die, too.”

“Ta-Taekyung. Please…”

Slice!

The dagger cut deep through his throat. Won Myunghoon’s eyes bulged as he looked up at me with a desperate gaze.

He tried to cover his throat with his one remaining hand, but he could not stop the blood—or his life—from pouring out.

Grrrgh. Thud.

The moment his body collapsed with a wet, rattling gurgle—

> **System**
>
> - You have defeated **Lv. 80 Won Myunghoon**!
>
> - You have acquired a considerable amount of EXP!

The System announced the enemy’s death.

“Let’s go.”

Butler Kim nodded as he watched me with a strange look in his eyes.

“We have more baggage to take with us now.”

He waved his staff, and the Star Guild members buried in the earth floated gently into the air.

As I watched magical ropes being summoned and binding them tightly together like strings of dried fish, I suddenly spoke.

“Wait a moment, Butler Kim.”

“……?”

“We need to add one more person.”

A short while later, I followed the direction indicated by my Qi Sense and found a man with a gag in his mouth.

For some reason, he was bound tightly to a tree. And he was someone I knew.

“The Star Guild’s Team One Leader?”

* * *

Most of the reporters who had flocked to cover the joint raid by the Peace Guild and the Star Guild—or rather, Jin Taekyung and Won Myunghoon’s raid—had left long ago.

But there were always exceptions. A young man wearing thick, horn-rimmed glasses and eating ramen was one of them.

“Being the youngest is so miserable. So miserable.”

At the young man’s lament, his colleague snickered as he picked up some instant kimchi.

“You’ve only been here two months, and you already have plenty to say.”

“Come on. You haven’t been here that long either, Senior.”

“Hey. Back in my day, I kept my mouth shut and worked. If they told me to stay, I stayed. If they told me to do something, I did it.”

“But isn’t this a bit much? How can they make us wait around for days just to cover one Hunter?”

“You haven’t changed since college. If you don’t like it, stick around long enough to build up some seniority.”

The young man stared glumly at the cup ramen, its surface shimmering with floating oil.

“It’s an A-Rank Gate. It’ll take at least three days for them to come out…”

“Three days? We should be grateful if they don’t stay the whole week.”

“A week?”

“It’s an A-Rank Gate. Once they’re inside, they might as well get everything they can out of it.”

“……Ugh.”

The young man shuddered as if the mere thought gave him goose bumps.

Seeing the other junior reporters in the same situation gathered around him and eating their meals only made him feel more depressed.

“I wish they’d come out soon.”

“They definitely won’t be out today. Like you said, even if they come out quickly, it’ll take three days. Get some sleep. Want to go to a sauna together? Maybe play some billiards?”

“Billiards?”

“Yeah. There’s plenty to do around here. The local businesses just rip you off.”

“Then maybe one game of billiards…”

The young reporter was tempted by his Senior’s offer. He had just started to lift himself from his seat when—

Whoooooosh.

The enormous door standing before them—the Gate—gave off a strange sound.

The mana that had been as still as the surface of a lake began to swirl, and urgent shouts erupted from all around them.

“The Gate! The Gate is opening!”

“Already? What the hell?”

“The cameras! Get them over here, quickly!”

The area fell into chaos in an instant. The reporters who had been idly passing the time shot to their feet and crowded in front of the Gate.

The young reporter and his Senior were no exception. They claimed a spot at the front faster than anyone else, their minds reeling.

“What’s happening? Why are they coming out already?”

“How should I know? Set up the equipment!”

Cameras began rolling, and flashes burst without pause.

The reporters had sensed that something had happened, and their prediction proved exactly right.

Whoosh!

Around a dozen people burst from the swirling vortex of mana.

Everyone who saw them stood with their mouths hanging open.

“……W-What happened?”
## Chapter artifact 226

# Chapter 226

Click, click!

A barrage of camera flashes blinded me. You’d think I would have gotten used to it by now, but apparently I really was a caterpillar that had to eat pine needles.

“Mr. Jin Taekyung! Did you clear the Gate?”

“If not, why did you come out so quickly?”

Questions rained down from the reporters. If the Gate security guards hadn’t been there, they looked ready to jam their microphones into my mouth already.

But that lasted only a moment. Before long, the initial frenzy gradually died down, replaced by confused voices.

“But… why is Jin Taekyung covered in blood like that?”

“The numbers don’t add up, either. The people behind him are Star Guild members.”

“They’re even tied up.”

“Where’s Won Myunghoon? I don’t see him, either!”

I could roughly imagine what we must have looked like on camera.

Me, drenched in the blood of monsters and Won Myunghoon. A dozen or so Star Guild members tied together in a line. And Butler Kim holding the rope in his hand as though he were walking a dog.

*I suppose that reaction makes sense.*

I licked my dry lips, then shook my head at Butler Kim as he tried to step forward on my behalf.

He had clearly tried to stop me, and I had refused. Since this had happened because of my choice, I was the one who had to deal with the aftermath.

“Mr. Jin Taekyung! What happened?”

“Please, just give us one comment!”

The commotion lasted only a moment. The reporters, who had caught the scent of a scoop, went wild.

I calmly watched the frenzied press corps before asking the young reporter at the front a question. He wore thick, horn-rimmed glasses.

“Who do you work for?”

The young man in horn-rimmed glasses flinched.

“Pardon? M-Me?”

“Yes. You.”

“Uh, well, that is…”

He had been shouting the loudest from the front, but apparently hadn’t expected anything like this to happen.

After panicking for a moment, the young man finally managed to speak.

“H-HunterTV.”

“Oh. Them.”

HunterTV was a channel that focused on Hunter-related issues and information.

It was a cable channel, but it was also a major broadcaster that drew higher ratings than terrestrial networks.

Since it was connected to what I was about to say, both the reporter and I were lucky.

“I’ll take questions.”

“Pardon?”

“There are too many microphones. I’ll focus on one.”

“So… an exclusive?”

“Whatever you want to call it. Shall we begin?”

He still looked like a greenhorn, but he was a reporter all the same.

The bewilderment vanished from his face, and his eyes shone brightly behind his glasses.

“How about a live broadcast?”

“A live broadcast?”

“Yes. Like at the Association last time. Real-time streaming.”

A real-time stream.

After a moment’s thought, I nodded.

“Let’s do that.”

* * *

iTube was the number-one video-sharing website.

Millions of channels, from individuals to organizations, were registered on the platform. Among them, HunterTV was a massive channel with several million subscribers in Korea alone.

At the same moment, the phones of HunterTV subscribers going about their daily lives all rang with the same notification.

Bzzzzt.

[HunterTV has started a live stream.]

[“Jin Taekyung Exclusive Live Broadcast.”]

The view count reached 100,000 almost immediately.

The screen was still black from the sudden influx of viewers. The chat window blazed like a furnace packed with firewood.

What is this? Why is there suddenly a Jin Taekyung exclusive live broadcast?

No idea. Feels like it hasn’t even been a day since Lord Fuck entered the Gate.

It’s an A-Rank Gate. He’s already out?

The buffering is absolute garbage.

Now I want some Butter Rings.

Oh, the screen’s up.

Everyone shut up and welcome Lord Fuck with the proper reverence.

Pop.

After the short but seemingly endless buffering ended, the video began to play.

The viewers saw a huge Gate and a young man standing tall in front of it. Their fingers flew across their screens.

It’s Lord Fuck!

Oh my god, fuck.

Please insult me!

Smack my ass, too!

Cut it out, you lunatics.

Jin Taekyung’s popularity was through the roof.

He had saved countless lives by suppressing a B-Rank Gate. His approachable, down-to-earth personality—unlike what people expected from an A-Rank Hunter—and even his bizarre stunt of accidentally swearing during an official press conference had kept him at the center of attention day after day.

But the frenzy lasted only a moment. The viewers soon noticed something strange and began voicing their doubts.

Why does he look like that?

Did Lord Fuck get hurt? He’s covered in blood.

The numbers are cut in half, too. And they’re tied up;;

What the hell is this? Something happened.

What’s HunterTV doing? If you’re going to start a broadcast, at least ask some questions.

Perhaps feeling the chaos in the chat, the HunterTV reporter finally opened his mouth.

“I’ll ask you directly. What happened inside the Gate?”

“It would take too long to explain everything from beginning to end… May I give you a summary?”

“Please do.”

Vrrrrr.

The camera zoomed in, capturing Jin Taekyung’s face in full.

His face was smeared with blood and dust, but his eyes shone calmly. Then a composed voice flowed between his parted lips.

“There was a Named Monster.”

“……!”

“It was a Mutated Gate.”

The noise from the scene suddenly fell silent, as though someone had pressed a mute button.

After pausing for a moment, the chat began scrolling upward like mad.

??

???

Wait, why is there a Named Monster here;;;

They must all be dead. No wonder so many people were missing;;

Is Won Myunghoon dead, too? I haven’t seen him since earlier;

Holy shit…

A major incident.

That was the phrase that flashed through everyone’s minds.

Even the reporter in horn-rimmed glasses, who had been holding the microphone toward Jin Taekyung, forgot his duty and stood there with his mouth hanging open.

*A Named Monster.*

Everyone knew how destructive they could be.

Five years earlier, a Named Monster that appeared in Central and South America had possessed enough power to destroy a small city on its own.

Although it was eventually defeated after several days of fighting, the damage had been enormous.

Hundreds of Hunters had died, along with ten times as many civilians.

It had been an incident that drew the attention of the entire world. Neither the reporters nor the viewers could have been unaware of it.

If that was really a Named Monster, surviving was a miracle;

No. Wait a second.

Then that means there’s still a Named Monster inside the Gate;;;

So what? It’s inside the Gate, isn’t it? Doesn’t that make it fine?

Did this bastard just get here from Mars? You idiot, don’t you know what happens when the mana level exceeds a Gate’s capacity? The monsters come pouring out.

The catastrophe in Central and South America a few years ago happened because the mana level exceeded the limit and the Gate opened;;

The Black Wyvern’s Nest? Does anyone know where it is?

Holy shit;; Get the reporters out of there first.

The reporters who had been staring back and forth between Jin Taekyung and the chat as if hypnotized suddenly came to their senses.

“A Named Monster!”

“Hey, get out of here right now! Grab the cameras!”

No scoop was worth more than their lives.

Just as the reporters, sensing the threat of death, began wading into chaos, someone who had been watching the entire situation finally spoke.

“Ah, the raid monster has already been taken down, so you don’t have to worry too much.”

The clear voice pierced everyone’s ears.

The reporters who had been trying to flee in a panic and the viewers staring at their phone screens while swallowing nervously both wondered if they had heard correctly.

“Pardon?”

“……What did you say?”

????

I think I heard that wrong.

What did Lord Fuck just say?

He says he killed a Named Monster…?

Who did?

Lord Fuck.

What did he kill?

A Named Monster.

Can he even do that?

I don’t know…

The camera, shaking as though caught in an earthquake, regained its focus. Dozens of cameras turned toward the young man’s calm face.

The reporter in horn-rimmed glasses asked Jin Taekyung in a trembling voice.

“C-Could you say that one more time?”

“It’s just as I said.”

“Then you really killed a Named Monster…”

“Yes. I killed it.”

He killed it? A Named Monster?

Everyone’s jaws dropped at the unbelievable words that had come from Jin Taekyung’s mouth. One reporter finally recovered enough to blurt out a question.

“T-Then did the others die in the process?”

“Seven dead. The rest are safe…”

He let his voice trail off, thought for a moment, then continued in an unwavering voice.

“Oh, I need to add Won Myunghoon to the death toll. Eight in total.”

“W-Won Myunghoon? Why did he…”

“Uh, well…”

Jin Taekyung hesitated briefly before adding another word.

“I got him.”

“……Pardon?”

“Ah, not caught. I killed—no, that sounds strange, too. Give me a moment.”

Before the aftershock of the Named Monster bomb had even faded, a second bomb went off.

The dozens of reporters at the scene and the 100,000 viewers watching the screen were left half dazed.

*What the hell is he talking about?*

At the exact moment everyone had the same thought, Jin Taekyung finally found what he considered the most appropriate expression.

“This is probably the best way to put it. I ‘disposed of him.’”

“…….”

“…….”

At the end of the heavy silence, a single line appeared in the frozen chat.

Did that guy just come back from sorting recyclables at home?

* * *

Everything proceeded quickly and smoothly. The investigation team dispatched in an emergency dug into the truth of the incident with speed and thoroughness.

It was a case drawing attention from countless people. If they missed even one detail, they might be cursed out for the rest of their lives.

“Handle this properly. Miss even one thing and you’re finished—finished!”

“This has already been reported all the way to the Blue House. If we slip up, we’re all going over a cliff together.”

The government and the Hunter Association’s leadership were both on edge.

Contrary to their concerns, however, it did not take long for every detail to be revealed beyond a doubt.

“Holy shit… He killed this thing by himself?”

“He actually killed it.”

The investigators were stunned when they confirmed that the enormous Named Monster lay gruesomely dead.

By then, every Star Guild member who had participated in the raid was tied to a cold metal chair in an interrogation room.

“I don’t know anything.”

“Look, Hunter. It’s going to come out in no time anyway. Why make things difficult?”

“I’m telling you. I don’t know anything.”

“Ha, you bastard… You’d spill everything with one mental spell, but you still have to be annoying.”

“Did you just swear at me? Just because you’re a prosecutor, you think you can do whatever you want? And don’t you know mental magic is illegal?”

Their lives were on the line. They couldn’t give up the comfortable lives they had enjoyed as B-Rank Hunters and rot in prison for the rest of their lives.

The prosecutors were racking their brains over the Star Guild members’ stubborn denials when an unexpected savior appeared.

“I-I’ll tell you everything.”

Kim Jonghun, the Star Guild’s Team 1 Leader, confessed to everything that had happened before he had fully recovered from his shaken state.

It was a perfect testimony. On top of that, an anonymous informant had sent a USB drive and a note.

> The Hapsburphon family, a long-established German family of equipment makers, has produced rare and highly practical items. One of their representative products is the PSV-96K camera, which cannot be detected by any detection magic and functions normally even in Gates with unstable mana…

The prosecutor in charge looked at the note with an incredulous expression and asked the investigator,

“What is this supposed to mean?”

“They filmed the whole raid. There’s footage on the USB. Open it and you’ll see. That bastard Won Myunghoon was a real piece of shit.”

“Filming is illegal, isn’t it?”

“It is.”

“It was the Peace Guild, right?”

“Wouldn’t you say so?”

“…….”

“Let that much slide. Every Guild with enough clout does it. They didn’t leak it to civilians, and thanks to them, we secured conclusive physical evidence. We both benefit from this…”

Bang!

An employee burst through the door and held out his phone.

“H-Have you seen this?”

The number-one real-time search term was boldly displayed across the screen:

“Won Myunghoon Raid Footage Leaked.”

As the ugly side of a former star people remembered fondly was revealed, the internet boiled like a cauldron over hot coals.

What a fucking bastard.

My head is ringing. Is this really true? It’s not staged, is it?

Good riddance. Killing him was the right call.

Still, it’s clearly murder. Killing Won Myunghoon was a bit much…

└ Are you Myunghoon?

└ Can Wi-Fi reach hell?

└ Did King Yama set up a hotspot for you?

└ You’re calling this murder? Don’t you know what self-defense means?

Only two days had passed since the incident. Yet the backlash was fiercer than anything people could remember.

Every time the suspicions surrounding Won Myunghoon that had been buried in secret came to light, people boiled over with anger.

And when that heat of fury had swept through, they always ended with the same question.

So what is Jin Taekyung doing?

└ At this hour? Probably sleeping.

└ Probably sorting recyclables.
## Chapter artifact 227

# Chapter 227

“Thank you for your hard work.”

A man wearing a shabby suit held out his hand.

His skin was dry and his eyes were sunken. Apparently, the investigator hadn’t been exaggerating when he said the man hadn’t been home in a week.

“You’re the one who worked hard, Prosecutor. Me? Not really.”

I shook hands with the prosecutor in charge and looked around.

The spacious room had a soft bed, a sofa, and even a state-of-the-art wall-mounted TV.

When I was first summoned by the prosecutors’ office, I had imagined a cold, dark interrogation room. Instead, they had led me to a hotel suite.

“I didn’t expect to be treated this well.”

“The higher-ups are very interested in this case. But would you mind if I sat down for a moment?”

“Oh, sure.”

“Thank you.”

The prosecutor replied in a tired voice, then collapsed onto the sofa.

“There was some debate, to be honest. We had our own arguments over whether Mr. Jin Taekyung’s actions constituted self-defense or excessive force.”

That was the part that had been bothering me, too.

It had been a killing in a situation where I could have subdued him. Killing Won Myunghoon had gone beyond the limits allowed by self-defense.

Of course, even if I went back a week, I would make the same choice.

“So I assume the issue was resolved favorably?”

“Of course. Do you think I would have come alone if it hadn’t been? I would’ve brought Hunters from the Ministry of Justice.”

The prosecutor spoke jokingly, but his eyes passed over the morning newspaper lying on the table.

He saw the Black Wyvern’s corpse, which took up nearly the entire front page, and clicked his tongue.

“Though, even if I had brought them, they probably wouldn’t have been much help.”

“I’m a law-abiding citizen. The kind who could live without laws.”

“There was a movie called *Law Abiding Citizen*. Its protagonist killed a prosecutor and even a judge.”

“……”

What was this? Was he asking me to hit him?

The prosecutor gave a quiet laugh at my expression and stood up.

“I should be going. I have an incredible backlog of work.”

“I’m glad I could lend a hand.”

“You didn’t just lend a hand. You created the work for us. Once we started digging, things kept coming out like a sweet-potato vine.”

I had suspected that Won Myunghoon had plenty of skeletons in his closet.

But once the investigation properly began, his past was so ugly that I found myself wondering what kind of man he was.

Among the countless crimes he had committed were several cases similar to what had happened a week ago.

*The incident eight years ago was the same.*

Won Myunghoon had been a monster created by the media.

When his brief burst of popularity began to fade and the spotlight went out, he tried to create scandals himself to draw the public’s attention.

But in the process, the star Hunter who had enjoyed the greatest popularity at the time died. Amid the Association’s suspicions and the public’s uneasy gaze, Won Myunghoon quietly faded from memory.

“He covered up everything thoroughly. With money, with power, and sometimes by making people disappear in what looked like Gate accidents.”

There had also been countless lobbying efforts to minimize the case.

In the end, the political and business figures connected to him had to appear before the cameras in wheelchairs and masks.

Along with their favorite line:

*I will cooperate fully with the investigation.*

Whether the investigation would be conducted properly, and whether they would cooperate with it in good faith, remained to be seen. But one thing was certain.

The prosecutor spoke with conviction.

“At least half of them are going down.”

The wildfire had already spread beyond anyone’s control. Putting it out would take more than pulling up a weed or two.

Won Myunghoon’s death had only been the beginning.

“I hope that’s what happens.”

“It has to. It will.”

He offered what sounded like a farewell and reached for the doorknob. Then he paused and turned around.

“I was so distracted that I forgot to say this.”

“……?”

His formerly straight back bent deeply.

“Thank you. All of this is thanks to you, Mr. Jin Taekyung.”

I’m a simple man. I killed the raid monster because I had a grudge to repay, and I killed Won Myunghoon because he was my enemy.

But the world called me a hero who had prevented a major catastrophe and brought justice.

It was a little burdensome, but…

*Well, it wasn’t so bad.*

I smiled and nodded. A faint smile crossed the prosecutor’s exhausted face.

* * *

I went underground with the investigator I had grown familiar with over the past week.

“You don’t need to worry. We took extensive security measures.”

Just as he had said, there wasn’t a single reporter—or even a camera—in the underground parking lot.

Instead, some familiar faces were waiting for me.

“Son!”

“Oppa!”

Two people rushed at me with cries that sounded like screams, and I hugged them both.

No, let me correct that. I hugged Mom and pushed Hayeon away with my palm.

“Son! Are you all right? You’re not hurt anywhere?”

“I’m fine. Just a few scratches.”

Mom ran her hands over my entire body with an expression that made it look as though she had lost ten years of her life. Then she sucked in a breath.

“S-Scratches? Where? You’re hurt?”

“No, I misspoke.”

“You said you got scratched!”

“I said I wanted some of your *saengchae muchim*.[^1] I just got the words mixed up.”

[^1]: A seasoned raw-vegetable dish; *saengchae* sounds similar to the Korean word for “scratch.”

“Taekyung, you’re lying again, aren’t you? You fought a terrifying monster like that. How could you not have a single injury?”

“It was big, but it was a gentle kid.”

“Son, are you going to keep playing with words? Mom is serious right now, so take your clothes off.”

“……How am I supposed to do that here? This is crazy.”

I had the reflexes to dodge bullets, but somehow I couldn’t evade Mom’s hands.

*Had she learned some kind of grappling technique?*

As I struggled helplessly, my household-register mate with the other set of chromosomes asked with a shocked expression,

“……Why did I get pushed away?”

“You have to ask?”

“I’m asking because I don’t know.”

“If you don’t know, you deserve a hit.”

Flick!

“Ow! Mom! Oppa hit me!”

“Can’t you two sit still?”

Hayeon clutched her forehead with a wounded expression while Mom shouted at us.

In the middle of the chaos, I noticed someone watching us with a smile.

“Don’t just stand there smiling. Please stop them.”

“Isn’t this proof that your family is close? I’m actually jealous.”

His legs were long and straight, like a model’s. He looked as though he had just stepped out of a magazine shoot as he gripped my shoulder firmly.

“You’ve been through a lot, Mr. Jin Taekyung.”

“You too, Team Leader Choi.”

But where was everyone else?

Team Leader Choi noticed me looking around and spoke.

“They all wanted to come, but I stopped them. There are too many eyes watching.”

“Oh.”

“Reporters are camped out everywhere. I’ll take you home first. We can talk on the way.”

An underground parking lot wasn’t exactly the best place to catch up. Especially not with a prosecutor’s investigator watching us.

We got into a high-end sedan with heavily tinted windows. With a pleasant vibration, the car began making its way through the forest of skyscrapers.

“A lot happened while you were being questioned, though I assume you know most of it.”

“I watched it all on TV. I turned off my phone because I was getting so many calls.”

Terrestrial television, cable, radio.

These days, wherever I turned, I heard my name and Won Myunghoon’s.

Politics, the economy, the Hunter industry—it felt as though all of Korea was in an uproar.

*I’ve heard it so much I’m sick of it.*

Even the national anthem got tiring once it reached the second verse.

Team Leader Choi glanced at my expression and smiled.

“There’s one important thing I should tell you.”

“It’s not about dinner, is it?”

“No. It’s related to what happened.”

“Team Leader, please. I’m begging you.”

“It’s about processing the Named Monster’s remains.”

“Please tell me. I’m begging you.”

“……”

I raised myself from the passenger seat and looked at Team Leader Choi with sparkling eyes.

Mom and Hayeon, sitting in the back seat, perked up their ears as well.

“Remains? Is that really so important?”

“Mom, what are you, someone from the Korean Empire? Of course it’s incredibly important!”

“Oh, come on. Mom knows that much. I just don’t have a feel for how important it is…”

Even though plenty of products made from monster byproducts had reached the market, they were still luxuries reserved for the wealthy.

To Mom, who had spent her entire life tightening her belt, they might as well have belonged to another world.

Team Leader Choi explained in a gentle voice to Mom, who let her sentence trail off.

“It depends on the monster. But in the case of the Named Monster Mr. Jin Taekyung killed, its value is astronomical.”

“R-Really? I only saw it in photographs, but it did look terrifying.”

“As you saw, it was an extremely powerful monster. That’s why its value was estimated at 300 billion won.”

“Oh, I see.”

A brief silence followed Mom’s answer.

There wasn’t even the sound of breathing. In the complete silence, I blinked without a word, then barely managed to speak.

“How much?”

“300 billion won.”

Team Leader Choi added another sentence in the same calm tone.

“Oh, that’s the starting price for the auction.”

“T-The starting price?”

“Yes. The processing was completed three days ago, and Christie’s has already…”

“Wait. Who’s Christie?”

Hayeon looked at me with an expression of disbelief.

“What do you mean, who’s Christie? You don’t know Christie’s?”

*What an idiot. And he’s my brother.*

That was exactly what Hayeon’s expression said.

I racked my brain to preserve my authority as her older brother, but the only thing that came to mind when I heard the name Christie was a blonde beauty.

“A-American billionaire’s daughter?”

“……”

“Or someone from Hong Kong? European royalty? A Hollywood actress…”

Team Leader Choi came to my rescue as I broke into a cold sweat.

“It’s a famous auction house. Along with Sotheby’s, it competes for the top position in the industry.”

“Oh.”

I thought I had heard of it. Or maybe I hadn’t.

I had spent my childhood doing nothing but exercising, and my adulthood working like an ox. How was I supposed to know about things like that?

Team Leader Choi, who was knowledgeable about this sort of thing, continued smoothly.

“Christie’s approached us first. They offered to charge a much lower auction commission than Sotheby’s if we entrusted the sale to them.”

“S-So?”

“Christie’s appraisers assessed the value of the remains. At present, the starting price is 300 billion won. Since this requires your consent, we’ve put off the final decision.”

*Was this really happening in the real world?*

I sat there dazed with my mouth hanging open, then smacked Hayeon on the forehead as she poked her head between the driver’s and passenger’s seats.

Smack!

“Ow!”

“It’s real.”

“Why did you hit me?”

“Because I’m precious.”

Only after hearing her scream did it finally sink in.

Before long, I would become a wealthy man with an enormous fortune.

“S-Son, what does this mean? Three hundred billion won?”

“Calm down. It’s not all mine.”

I didn’t know how high the final bid would go, but the Hunter industry had clear rules for dividing the proceeds. Raids were team efforts, after all.

Even if I had killed it entirely by myself, the same principle would apply.

But Team Leader Choi’s next words were astonishing.

“It’s your share, Mr. Jin Taekyung. Every last won.”

“……Pardon?”

“The others all agreed. So I hope you won’t say anything more about this matter.”

“They all agreed?”

They could each have received anywhere from several billion won at the low end to tens of billions at the high end.

For an ordinary person, it was an irresistible temptation and an obvious right to claim.

As I stared at him in shock, Team Leader Choi smoothly turned the steering wheel and replied,

“I’m not shameless enough to accept money for merely watching. The others and I have at least that much conscience and conviction.”

“You didn’t have to go that far…”

“It wasn’t something that required any consideration. You’ve shown us enough consideration already, so think about what you want to do with the money.”

At Team Leader Choi’s firm words, I became mute as though I had swallowed honey and closed my mouth.

300 billion won. Christie’s auction.

The words swirling through my head made it hard to think. Mom and Hayeon, who had been frozen like statues for some time, were probably in an even worse state.

*This is surreal.*

I rubbed my stiff face with my palm.

An unimaginable fortune would soon be rolling into my hands. What should I do with it?

One fantasy led to another. A private jet, a luxury yacht, bundles of cash stacked like mountains, and a leopard wearing a collar…

Before long, all those fantasies faded like fog.

Only then could I clearly think about what I should do with the money and look at the world around me.

“Team Leader Choi.”

“Yes?”

“May I ask you for a favor?”

The corner of Team Leader Choi’s mouth lifted slightly.

“Anything.”
## Chapter artifact 228

# Chapter 228

Time passed quickly.

One issue followed another, each bigger than the last, while new truths and suspicions continued surfacing everywhere.

Before we knew it, a week had passed in the blink of an eye—and a new article took over the portal sites.

[GojoseonTV] Christie’s Secret Auction Held Behind Closed Doors. Winner: Qatar’s Prince Cheonsur. Final Winning Bid: Approximately 500 Billion Won!

The short article came with a single photograph, but its impact was enormous.

That was because of the gigantic body visible behind the Middle Eastern prince, who was grinning broadly with a turban wrapped around his head.

**Top Comment:** Isn’t that the thing? The Named Monster Lord Fuck caught this time?

└ It is;;; I’ve seen it so many times that I can recognize it from the hide pattern alone. But some lunatic actually bought that for 500 billion.

└ The Middle Eastern prince’s class blew me away, and Lord Fuck’s majesty after earning 500 billion in one shot made me shit myself.

└ Son, what did you shit? You didn’t see something strange, did you? Mom believes in our son. Love you~

Many people were envious and impressed, but there were also those who viewed the matter sourly.

**Top Comment:** Jin Taekyung caused all kinds of chaos, never gave a single interview, and then sold the monster behind everyone’s backs. Am I the only one bothered by this?

└ Personally, I really don’t like him. Killing Won Myunghoon on his own authority was excessive force, if you look at it one way. But the prosecutors’ office only questioned him as a witness and then quietly let the matter fade away. It feels like they’re giving him special treatment because he’s famous.

└ Same here. Upvoted.

There’s a saying that when your cousin buys land, your stomach hurts.[^1]

If even friends and blood relatives could make you feel that way, celebrities you only knew through the media were another matter entirely.

Not long after the article was posted, a bloody battle broke out among the netizens.

[^1]: A Korean proverb about feeling jealous when someone close to you prospers.

**Top Comment:** Are the idiots who posted the comments above the Three Stooges?

└ I’m shocked that crap like that has more than a thousand recommendations lol. Why are there so many people who can’t stand seeing others do well?

└ Exactly. What chaos are they talking about? Did the Dodong Sect punch a hole in their brains? How many people are alive thanks to Lord Fuck by now?

└ Jin Taekyung. Well, look at this rotten son of a—… As a public figure… what a nasty bastard, only filling his own pockets… Don’t forget that the entire nation is watching @~!

└ “Self-interest,” lol. The only interest here is the deposits building up in your parents’ bodies; what’s coming out of my mouth is pure profanity.

└ What are you talking about, public figure? He was a hyung who was wearing sweatpants and boiling ramen in the corner of his room until a month ago. And that way of talking is disgusting.

└ You young whippersnappers… Your tongues are sharp~!!!

└ Dentures confiscated for one month.

└ Hearing aid confiscated for two months.

└ Banned from the senior center for three months.

Even as people everywhere had their dentures and hearing aids confiscated and were banned from the senior center, the fighting didn’t stop.

Despite the fierce backlash, those criticizing Jin Taekyung stubbornly continued arguing their case.

You little brats… hehe. You’ve put knives on your fingers… You ignorant, rotten bastards~~!! Ignoring you… is the answer! @!~~

└ Cane confiscated.

I don’t use a cane… you bastard~~

└ Wheelchair confiscated.

You nameless lowlifes… Where do you think you’re pulling this red nonsense from…!!!!!

└ Park Hyeongseok. I gave my name, so are we done?

Young Hyeongseok, go back to your mommy, suck some more milk, and study harder~~`!!

└ You go suck some more.

└ You’re a goddamn lowborn son of a bitch.

It was a truly bloody battle.

The article reached one million views in just a day and racked up tens of thousands of comments.

As the two sides exchanged sharp comments and snarled at each other, another article went up.

[HunterTV Exclusive] Jin Taekyung Donates Hundreds of Billions to Gate Victims and Establishes Support Foundation

Hunter Jin Taekyung has drawn attention by donating hundreds of billions of won and establishing a support foundation for Gate victims under the name of the Peace Guild.

The necessary procedures had begun even before the Christie’s auction started…

**Top Comment:** Everyone who’s been calling him a public figure and accusing him of self-interest, gather here. Bang your heads against the floor.

└ Tsk, tsk… Nothing has even been properly revealed yet, and you’re acting filthy and cocky… Look at the truth straight…!

└ LOL. Hey, are you crying?

└ LMAOOOOOO

But seriously;;; What the hell is with him throwing several hundred billion won around? Honestly, that’s even more amazing than the satisfying defeat of all the people who’d been maliciously trying to muddy the waters.

└ Agreed. What the hell is Lord Fuck? Is making money just easy for someone at his level, so he decided to make a generous gesture?

└ I don’t think it’s that. He just doesn’t seem particularly greedy for money. Either way, I was genuinely impressed.

└ Height, looks, personality, money. He has everything. Isn’t that cheating?

└ PH3D, PH3D…….

└ What does that mean?

└ Please have a three-centimeter dick.

└ Oh.

The fight ended with the trolls’ defeat, and public opinion was once again filled with admiration for Jin Taekyung.

He had already prevented two major catastrophes and possessed the strength to defeat a Named Monster all by himself. On top of that, the generosity to donate hundreds of billions of won.

It was the moment his image as an unassuming hero and a truly big-hearted man became firmly established.

* * *

—Let me update you on the progress regarding the establishment of the foundation…

“Team Leader Choi.”

I cut off Team Leader Choi’s voice over the phone in a trembling voice.

“That’s enough. Please don’t say anything more.”

—……Would you like to cancel the foundation’s establishment if you’re that reluctant to part with the money?

“No. Absolutely not!”

—Then why are you acting like this?

“Because I hate parting with the money.”

—Pardon?

“I hate giving it up, but this is necessary. Please continue.”

—Is this one of those rice cakes in a painting situations?

“It’s a rice cake in my hand. I’m starving, but I’m barely managing not to eat it.”

The secret Christie’s auction attended by wealthy people from around the world had ended a short while ago.

Exactly twenty-four hours later, my bank account was filled with an endless string of zeros.

*Five hundred billion.*

To be precise, after every fee had been deducted, it came to approximately 530 billion won.

The unit wasn’t hundreds or thousands. It was *eok*—hundreds of millions.[^2]

It was literally an *eok*-inducing sum, and I nearly cried out myself.

[^2]: *Eok* is both the Korean unit for one hundred million and an exclamation of shock.

*How much money was this, exactly?*

It was an astronomical amount—enough to change my life, no, enough to let me and my descendants live in luxury for generations.

But I had already made my decision. I knew where to spend the money and how to use it in the most proper and worthwhile way.

“So please continue. I’m trusting you with this, Team Leader Choi.”

—Understood. Then let’s start with the people on the list you gave us last time.

“Please take good care of it.”

The families of the team members whose lives had stopped on that day three years ago would be the foundation’s first recipients.

The money couldn’t fill the empty spaces left by their lost family members, but it could help them pursue their dreams without having to worry about anything.

—Next are the veterans who fought during the Great Cataclysm and single-parent families. Is that right?

“Yes. Please proceed that way.”

After exchanging a few more words, I ended the call.

When I left the room, I saw Mom and Hayeon sitting at the kitchen table and eating fruit.

The moment I approached, a fork with a piece of apple speared on it suddenly appeared in front of me.

“Son, have some apple. It’s sweet.”

“Uh, okay.”

Crunch.

The sweet flesh broke apart in my mouth. I quietly ate the fruit while listening to the conversation between the two of them.

Friends, studying, someone who lived nearby, dramas…

Sometimes I let out a quiet laugh, and sometimes I nodded along in agreement.

Then, at some point, I suddenly spoke.

“Everyone’s okay, right?”

“Hm? What do you mean, son?”

“What?”

“Um. I mean, about this whole thing. Is there anything bothering you?”

Hayeon tilted her head to one side.

“Are you trying to talk about the money?”

“……”

“I knew this would happen. Mom, didn’t I tell you yesterday? I said this human was definitely going to act like this.”

Mom smacked Hayeon’s skinny forearm, which was as thin as a twig.

“You! How can you call your brother, who’s eight years older than you, ‘this human’?”

“Ow, that hurts! Stop hitting me.”

Hayeon answered irritably, folded her arms, and leaned back against the chair.

“Excuse me.”

“……Excuse me?”

“What else should I call you? My household-register mate?”

She was my one and only little sister, eight years younger than me. Under normal circumstances, I would have flicked her forehead just for fun, but somehow today didn’t feel like the right time.

Hayeon looked at me and let out a deep sigh.

“Oppa.”

“Hm?”

“What’s the thing Mom says the most?”

I wondered. What was it?

It didn’t take long to remember. It was something I heard every time I came home—or at least once every few days over the phone.

“Take care of yourself?”

“Exactly. You know it well.”

She poked the apple and held the fork out to me.

“Eat. Eat, and take care of yourself.”

“……”

“What good would several hundred billion do us? Besides not being able to spend it all, it’s obvious we wouldn’t even know how to use it properly.”

I mechanically chewed the apple in my mouth. It was sweet, and it stung like fire—enough to make the tip of my nose tingle.

*When did she grow up this much?*

This had been a difficult choice for me.

The truth was, I wasn’t particularly good or righteous.

I was an ordinary older brother who wanted to do everything his only sister asked of him, and an ordinary son who wanted to let his mother, who had struggled alone for so long, live in comfort.

And several hundred billion won was more than enough to turn every fantasy I had ever imagined into reality.

*With this kind of money…*

I had agonized over it. Even after making my decision, I continued to agonize.

But all of it had been pointless.

People praised me as both a hero and a big-hearted man, but they were wrong.

The person with a bigger heart than mine was my sister, who was eight years younger than me.

She had inherited all of Mom’s best qualities. Even those eyes that curved into crescents whenever she smiled.

“Son, as I always say…”

“A parent anywhere in the world can’t spend money their child earned by bleeding. Yes, I know.”

“Good. You know it well.”

“But now you’ll have to spend some of it. I plan to earn a lot from now on.”

“Then buy me a massage chair.”

“A massage chair?”

“Yeah. I thought about what I would want first if my son became successful and gave me a present, but that was the only thing I could come up with.”

I laughed along with Mom.

My heart felt lighter, as though I had finally set down a heavy burden I had been carrying for a long time.

“Then let’s go look at one together tomorrow. We can look at furniture while we’re at it.”

“Furniture?”

“Actually, the furniture in our house is pretty old, too. Mom, when someone gives you something like this, you should accept it while it’s being offered.”

I wondered what expression she would make when she learned that I meant furniture for the house we would soon be moving into.

Even more so when she learned that it was the place where our family had lived back when the three of us had been four.

*I’d love to go there right now, but…*

I wanted to save it as something to look forward to tomorrow—or rather, to what came next.

Realizing that the time had finally come, I rose from my seat.

“Where are you going?”

“Son, there’s still plenty of fruit left.”

I smiled broadly at the two disappointed faces and answered,

“It’s okay. I think I’ll take a nap.”

This time, I was going to sleep for a very long time.

* * *

Whoooosh.

The winter wind, already nearing the end of the season, blew past.

Darkness had long since swallowed the surroundings, while the illuminated pavilion shone brightly.

The old man gazing at the wavering flames suddenly spoke.

“Who is it?”

A clear voice answered moments later.

“It’s me.”

“……Is that you?”

At first, he couldn’t easily tell.

In the span of one or two shichen, the young man’s footsteps had become as light as his voice.

*Has he gained some kind of enlightenment?*

The old man had been able to sense his presence from fifty paces away, but had only noticed him when he came within thirty.

It was hard to say whether that was impressive or strange.

Despite the smile at the corner of his mouth, a gruff voice slipped from the old man’s lips.

“Didn’t I tell you to come when daylight broke?”

“It was hard to wait. The answer’s already decided, so why waste time?”

“Tsk, tsk. For a martial artist to be this impatient…”

“You said it yourself, Old Master. Sleep is a luxury for a martial artist. Train during that time. Am I wrong?”

“Hah! You really are something.”

That was the attitude of a martial artist—and of a Disciple who regarded his master’s words as golden maxims.

The old man couldn’t hold back any longer and let out a hearty laugh. When he waved his gaunt hand, a gentle blast of heat swept through the pavilion and flung open the door.

Standing before it was Jin Taekyung, wearing a broad, refreshing smile.

“Old Master. Please teach me martial arts.”

The old man, Jeok Cheongang, the Fire King, smiled with delight.

“All right. I’ll teach you everything I know.”
## Chapter artifact 229

# Chapter 229

“……You’re leaving? For an entire year?”

“Yes.”

“So you finally decided?”

When I nodded, an indescribably complicated look passed over Jin Wikyung’s face. Joy, disappointment, pride….

After remaining silent for a long while, he performed a deep formal bow toward Jeok Cheongang.

“Please take good care of our youngest—no, Taekyung. Great Hero Jeok.”

“I heard you, so get up. He may be lacking, as you said, but this old man will guide him properly, so stop worrying. Ahem!”

“…….”

*When did I say that? He asked you to take good care of me. I don’t remember him saying I was lacking.*

But Jeok Cheongang was not someone I could reason with.

He calmed the twitching corner of his mouth and opened it again.

“Daylight has broken, so I intend to leave at once.”

“What? Today?”

“Obviously. Once a man makes up his mind, he must act without hesitation.”

Jin Wikyung’s expression grew even gloomier. He looked back and forth between Jeok Cheongang and me with a face covered in storm clouds, then let out a deep sigh.

“Understood. I’ll prepare your travel bags immediately.”

“What do I need travel bags for? I won’t need them. Is this training or a tour of the martial world?”

“Where are you headed?”

“Anhui. It’s close enough on foot.”

A sudden sense of foreboding made me ask,

“How far is it?”

Jin Wikyung answered,

“At least a month.”

“What?”

“And that’s on horseback.”

*Has this old man gone senile?*

Jeok Cheongang caught my expression and shouted,

“That’s only for those slowpokes! At this old man’s pace, it won’t even take a month and a half!”

“…….”

*No, damn it. If that’s how we’re measuring things, a jet would still be faster. So why are we walking?*

I quickly grabbed Jin Wikyung’s hand.

“Pack my bags nice and full, please.”

“You little—!”

“Otherwise, I’m not going.”

“What did you say?”

“I come from a family with money. I have no intention of wandering around begging for food. Since we’re going anyway, let’s travel comfortably.”

Why deliberately suffer when I had money? If I could travel comfortably, that was obviously the best option.

I had already left behind a soft bed and logged in. I didn’t want to take things that far.

And besides….

“There are places I need to stop by before leaving.”

“Gnnngh.”

As Jeok Cheongang groaned, Jin Wikyung added,

“I also have something important to discuss with you.”

“You have something to say to me?”

“Yes. It won’t take very long.”

“If you intend to waste my time with some trivial matter, forget it.”

Jin Wikyung firmly shook his head.

“It is important enough that Great Hero Jeok should know about it.”

*What could it be?*

Even I had rarely seen him look so serious.

Jeok Cheongang stared silently at Jin Wikyung, then clicked his tongue.

“Half a shichen. No longer.”

“That will be enough.”

This time, he turned his head toward me.

“The same goes for you.”

“Yes, sir.”

That was more than enough time for me as well.

Afraid they might change their minds, I answered immediately and left the study so the two of them could speak in private.

Clear sunlight and a cool breeze greeted me outside—weather that could hardly still be called winter.

“Ah, what beautiful weather.”

Finding my next destination was easy.

I looked up at the blue sky and began walking toward the cliff visible in the distance.

* * *

Whoooosh.

With a heavy boom, an iron sword cleaved through the air.

Once, then again, his stance flawless and without the slightest deviation.

How long had it been since he had begun each day with ten thousand strikes?

The young man gripping the sword’s hilt did not know.

He was in a cave where no light entered, and he had long since forgotten the passage of time.

Swish!

The tip of the sword wavered.

It was a tiny difference, but to the young man, it was an unforgivable mistake.

According to the rule he had set for himself, one mistake meant one hundred additional strikes.

*Again.*

The young man silently swung his sword.

It was a brutal physical regimen that had to be completed using nothing but raw strength and stamina, without relying on any internal energy.

An ordinary martial artist would have collapsed from exhaustion long ago.

But the young man, Jin Mukyung, was different.

*I’ll do it perfectly. No matter how many times it takes. No matter how many years.*

He had picked up a sword at the age of five. He liked the sound of the wind brushing his ears whenever he swung it, and he enjoyed soaking himself in sweat.

More than twenty years passed that way.

At some point, people began calling him by another name.

> “He reached Peak at twenty. There’s no other word for it but genius.”

> “Are you the Heaven Shaking Sword?”

He had only trained because he loved martial arts and enjoyed becoming stronger. Yet he had come to be called both the pride of his family and a genius of martial arts.

There had been times when he was proud of the martial reputation he had earned for himself.

But he eventually realized that it was all nothing more than hollow fame—an empty name with nothing inside it.

*Cheongpung.*

Swish!

The moment he thought of that name, the tip of his sword twitched.

One hundred additional strikes.

He forced himself to close his eyes and steady his breathing, but his shaken heart was impossible to rein in.

Before he knew it, Jin Mukyung was remembering the day he had first faced Cheongpung.

*He’s strong.*

That was his first thought upon seeing the boy.

He had a clear, boyish face and an ordinary build. A single iron sword hung carelessly from his waist. His attitude and posture could not have been more sloppy, but Mukyung had known immediately.

And his prediction soon became reality.

It had been the most bone-deep defeat of his life.

When he remembered the moment he had knelt after roughly three hundred exchanges, his teeth clenched on their own and his hand tightened around the hilt.

Swish! Swish-swish!

The disturbance in his heart showed itself plainly in his sword.

His stable stance collapsed, and his movements—once as precise as if measured with a ruler—became disordered.

One hundred strikes, two hundred, three hundred….

Just as his mistakes were multiplying like a snowball, a familiar voice came from beyond the iron door blocking the training hall.

“Why does it sound so murderous in there?”

“……!”

Jin Mukyung’s body, which had been swinging the sword as if possessed, came to an abrupt stop.

“Is that you?”

“Why ask when you already know? You’re hurting my feelings.”

There was no doubt.

Within the Taiyuan Jin Family, only one person could speak to Jin Mukyung that obnoxiously.

Thinking of the younger brother standing beyond the iron door, Mukyung asked,

“How long have you been there?”

“About fifteen minutes?”

“……I see.”

Despite the casual tone of the answer, his face darkened.

He thought he had let his emotions take hold of him and failed to notice the other’s presence.

“Go. I’m training.”

“Training, my ass. If anything, you’re venting your anger.”

“What?”

“You sound furious just from the noise. Nothing you do in that state could possibly count as training.”

Jin Mukyung’s eyes trembled faintly.

He was astonished that Taekyung had seen straight through his condition despite the iron door between them and the distance of more than ten jang.

*This guy…. Could he have improved again in that short time?*

His rate of growth was truly frightening.

But before his surprise had even faded, Jin Taekyung continued,

“I’m leaving.”

“You’re leaving?”

“Yeah. I decided to learn martial arts from the Fire King—or rather, Old Master.”

“……!”

Mukyung had heard that the Fire King had visited the family.

In the past, he would have immediately rushed out of the training hall, bowed until his forehead touched the ground, and begged the Fire King to teach him even a single move.

But he endured.

More than anyone, he knew that this was a process he had to understand for himself.

*But why would he teach that boy…? No. There are more than enough reasons.*

The man beyond that iron door was a true monster—someone who deserved to be called a genius. The Fire King would have recognized his true worth.

Having accepted that explanation inwardly, Mukyung spoke.

“Have you become his Disciple?”

“Not exactly. It’s a Disciple-but-not-a-Disciple, kind-of-a-Disciple relationship. Something like that.”

“……What the fuck are you talking about?”

“Don’t try to understand. Is this the first time something like this has happened?”

“That’s true.”

“Yeah, just let it go.”

A brief silence passed.

Then, as if they had made an agreement, the two of them let out quiet chuckles at the same time.

Even they had to admit that the conversation had taken a ridiculous turn.

“Did you come just to tell me that? Are you hoping for a send-off?”

“A send-off? I know better than to expect one.”

“Then?”

“One year remains.”

Taekyung’s calm voice continued.

“The Star-Array Grand Banquet.”

“The Star-Array Grand Banquet.”

Jin Mukyung muttered the words like a groan.

The Star-Array Grand Banquet was a banquet hall of countless stars spread across the Nine Provinces and Eight Wastes, the Four Seas and Five Lakes.

“Why are you telling me that?”

“I’m going to attend. Cheongpung and I both are.”

“……What are you trying to say?”

“That’s something you’ll have to think about on your own. Oof.”

Along with the sound of someone rising from his seat, Taekyung’s final words reached him.

“I’m going. See you later.”

Step. Step.

The sound of footsteps gradually faded until it stopped completely.

Silence settled over the training hall.

Jin Mukyung stared blankly at the iron door beyond which the other’s presence had vanished.

*The Star-Array Grand Banquet.*

He was not a fool.

He understood perfectly well why Jin Taekyung had come to the training hall and why he had brought up the Star-Array Grand Banquet.

“One year….”

Muttering the words under his breath, Jin Mukyung gripped the sword’s hilt.

His turbulent heart and wavering sword tip had both settled into calm before he knew it.

“Goodbye. See you later.”

He murmured the farewell he had failed to give his younger brother as he departed on a long journey, then swung his sword like lightning.

Whoooosh.

It was a perfect strike, without the slightest error.

* * *

After leaving the training hall, I headed straight for the study.

Waiting for me there was an empty chair with no one sitting in it—and a message delivered through one of the guards.

“He told me to wait at the main gate?”

“Yes. Those were his exact words.”

*Did something happen?*

I set the question aside and walked toward the main gate.

Not long after, I came face-to-face with several familiar people.

“Captain!”

“Benefactor!”

“You’re finally here, Young Master Jin?”

Hyuk Mujin, Cheongpung, and Wolhwa.

But they were not alone.

Over the shoulders of the three who had approached me first, I could see the others as well.

Lee Seowol, awkwardly waving one hand, and the Three Plum Blossom Elites, standing there with expressions that seemed to say they had no idea where they were or who they were.

“How did you all know to come here?”

Wolhwa smiled sweetly.

“Because we’re the Lower District Sect.”

“……Did you plant a spy?”

“Oh my, a spy? Would we need one when we have such an excellent informant right there?”

I followed Wolhwa’s finger and saw Hyuk Mujin proudly holding out a heavy travel bag.

“By order of the Lesser Family Head, I packed your luggage, Captain!”

“……Ah. So you’re the culprit.”

“Pardon?”

“Nothing. Good job.”

I had wanted to leave as quietly as possible, but apparently nothing ever went according to plan.

The moment I accepted the travel bag with a sigh, Cheongpung grabbed me by the collar and clung to me.

“Benefactor! I want to go with you! I want to become Grandpa Jeok’s Disciple!”

“Then go get permission.”

“Whose permission?”

“Whose do you think? Great Hero Mae Jonghak, the Sword Saint.”

“I already got it! He said it was okay!”

Baek Museong muttered with an expression of someone who had already seen everything life had to offer.

“He’s been missing for more than a month already. How exactly did you get his permission…?”

*That man really does have the hardest job in the world all to himself.*

After finally pulling Cheongpung away, I asked Baek Museong,

“What are you planning to do now?”

“Either escort Martial Uncle Cheongpung back to the main sect or search the Central Plains for Grandmaster’s trail. I suppose it will be one or the other.”

“Yikes.”

At my reaction, Baek Museong let out a hearty laugh.

“Haha. Is anything in life ever easy? I intend to leave as soon as a message arrives from the main sect.”

*What a rock-solid mind.*

I even felt a little respect for him.

After finishing my conversation with Baek Museong, I turned my head.

Beside the small Eunhyang, a giant nearly two meters tall flinched.

“Hey.”

“……Wh-what?”

“I’m just saying we should forget what happened before and get along.”

I smiled brightly and offered him my hand.

The giant, Chulwoo of the Defeated Flower Fist, hesitated before taking it.

“Th-then this means we’re reconciled….”

Crack.

“Gah!”

“You’re such a baby. Don’t let it show. Smile.”

With the sound of bones shifting out of place, the hand of Chulwoo, a man twice my size, crumpled as though it had been crushed beneath a press.

I tightened my grip and whispered into his ear,

“Don’t make a move on her. You know what I mean, right?”

“I-I got it!”

“Good. Keep that attitude for the rest of your life.”

When I released his hand, Chulwoo sucked in a breath and hurriedly backed away.

Watching him, Eunhyang, the youngest of the Three Plum Blossom Elites, could only marvel.

“……I never knew there was someone stronger than Senior Brother Chul. The world really is vast.”

Then again, it could feel awfully small, too.

No matter how large this continent was, people who were meant to meet would eventually meet.

I would probably see these people again someday.

“If fate brings us together, let’s meet again.”

“It was nice meeting you, too.”

I gave Eunhyang a slight nod and turned around.

One person remained.

“…….”

“…….”

An awkward silence hung between Lee Seowol and me.

I didn’t think things had been this awkward at first. I had no idea why Lee Seowol seemed more difficult to deal with every time I saw her.

*Maybe it’s because I received a proposal?*

Even if it was a political marriage, a proposal was still a proposal.

I struggled through the awkwardness and finally opened my mouth.

“Um, Sect Leader Lee.”

“Please call me Young Lady.”

“Ah, yes. Then, Young Lady Lee.”

“Yes. Go ahead.”

I looked at Lee Seowol’s slightly lowered eyelids and brought out the words I had prepared.

“May peace prevail throughout your household.”

“…….”

“May your business prosper as well, and, um, whatever. Anyway, I hope everything you do goes well.”

*Great. Nice job. For the Sect Leader of a whole sect, there couldn’t be a better blessing than that.*

Just as I smiled contentedly and began watching Lee Seowol’s reaction, a sharp, ringing voice came from the distance.

“What are you grinning so foolishly about?”

A short old man appeared in the distance.

With Jin Wikyung and Wipeng flanking him, he seized me by the nape before I had a chance to say anything.

“The road ahead is long. Hurry up and follow me.”

“W-wait a second.”

Whoooosh!

But it was already too late.

The faces of the people behind me quickly grew distant.

Jin Wikyung waved a handkerchief with reddened eyes and shouted,

“Our youngest! Come back safe and sound!”

*……That only makes me more nervous!*

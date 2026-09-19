# Checkpoint Review — 440–444

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

# Chapters 440–444

## Plot

Jin Taekyung receives a massive public welcome in Korea and resolves to protect his family and companions. He forces the Skeleton King to join Peace Guild under a prepared contract, while Magic Johnson announces negotiations between his Wizard Guild and Peace Guild. Go Jun, meanwhile, searches the former Arch Lich stronghold in China for Lee Jungryong’s holographic recorder, hoping to find evidence against Taekyung despite being consumed by fear after their confrontation.

Back aboard Mu Song’s fleet, Taekyung trains under Jeok Cheongang to adapt to his opened Middle Dantian. The group investigates the symbols shared by the Arch Lich’s magic circle and Dark Heaven’s formations, suspecting a connection to black magic. After nearly ten days on the Yangtze, they reach Hubei, where the Yangtze River Channel League’s local strongholds have inexplicably failed to contact Mu Song. A clash with local officials is resolved through Jin Wikyung’s connection to Provincial Administration Commissioner Yi Hongcheon, and Jeok’s identity as the Fire King is revealed.

The Zhuge Clan then welcomes the group into its heavily guarded Hubei compound. Lesser Family Head Zhuge Gyun escorts them through eight gates to the Inner Hall, where his father, Family Head Zhuge Feng, awaits them. The clan’s covert inspections and disguised guards indicate an unexplained emergency affecting its territory.

## Continuity

- Taekyung is publicly recognized as Korea’s S-rank-level Hunter; the World Hunter Association will send a testing team to Korea rather than require him to visit its headquarters.
- Taekyung has opened his Middle Dantian and is training under Jeok Cheongang while learning to control the resulting changes.
- Taekyung continues crossing between Murim and the modern world and is investigating the common symbols found in the Arch Lich’s magic circle and Dark Heaven’s formations.
- Mungyeong remains with the group while concealing his identity as the former Divine Physician and Slaughter Saint.
- The Skeleton King’s undead identity remains hidden. He has been ordered to join Peace Guild as Stone-King, and Magic Johnson’s Wizard Guild is negotiating with Peace Guild.
- Go Jun is expected to inherit command of Ares Guild and is searching for Lee Jungryong’s holographic recorder.
- The group has reached Hubei with Mu Song’s Water Dragon Stronghold fleet. Nearby Yangtze River Channel League strongholds have not reported Mu Song’s arrival.
- Jin Wikyung can invoke his relationship with Yi Hongcheon, the new Hubei Provincial Administration Commissioner.
- The Zhuge Clan is led by Family Head Zhuge Feng; his son Zhuge Gyun is Lesser Family Head, and Zhuge Gonghu was Gyun’s great-grandfather and Jeok Cheongang’s old friend.
- The Zhuge Clan is conducting covert inspections and deploying disguised martial artists because of an unidentified emergency. Zhuge Feng is about to receive Taekyung’s group.

## Translation Decisions

- Preserve Taekyung’s dry, profane humor; the Skeleton King’s grandiose “this king” diction and “vile human” address; and Jeok Cheongang’s irreverent insults.
- Render 시부럴 as “sibu-leol,” 시벌좌 as “Lord Fuck,” and 시부럴좌 as “Lord Sibu-leol.”
- Use “Team Leader Choi,” “Mr. Jin Taekyung,” “my youngest,” “Old Master,” and “Senior” for established forms of address.
- Keep Peace Guild, Wizard Guild, guild house, Inventory, Magic Johnson, black magic, poison human, World Hunter Association, and established martial-arts terminology.
- Render Zhuge titles and locations as “Divine Mechanism Zhuge,” “Fan-Wisdom King,” “Crouching Dragon Guest,” “Mount Fulong,” and “Mount Longzhong.”

## Durable state

{
  "active_continuity": [
    "Jin Taekyung continues crossing between the modern world and Murim while investigating the symbols shared by the Arch Lich's magic circle and Dark Heaven's formations.",
    "The shared symbols remain the only known common ground between the two worlds, and Taekyung suspects they are connected to black magic.",
    "Taekyung has opened his Middle Dantian and is adapting to the resulting changes in his martial ability.",
    "Mungyeong remains with Taekyung's group while concealing his former Divine Physician and Slaughter Saint identity from most companions.",
    "The Skeleton King's undead identity remains concealed from the public, and Taekyung has ordered him to join Peace Guild under a prepared contract.",
    "Go Jun is expected to succeed Lee Jungryong as Ares Guild's captain and is searching China for Lee's holographic recorder.",
    "Taekyung's group has entered the Zhuge Clan's Inner Hall in Hubei after traveling with Mu Song's Water Dragon Stronghold fleet.",
    "The Yangtze River Channel League's nearby Hubei strongholds have not contacted Mu Song despite knowing of his arrival.",
    "Jin Wikyung has political ties with Yi Hongcheon, the newly appointed Hubei Provincial Administration Commissioner, and used them to resolve the harbor incident.",
    "Zhuge Gyun is the Zhuge Clan's Lesser Family Head, Zhuge Feng is its current Family Head, and Zhuge Gonghu was Gyun's great-grandfather.",
    "The Zhuge Clan is performing covert inspections and deploying disguised martial artists in its own territory because of an unexplained emergency.",
    "Family Head Zhuge Feng is waiting to receive Taekyung's group."
  ],
  "continuity_sources": [
    444,
    443
  ],
  "open_questions": [
    "What are the origin and purpose of the symbols shared by the Arch Lich's magic circle and Dark Heaven's formations, and are they truly connected to black magic?",
    "Why does Mungyeong continue accompanying Taekyung's group despite being unable to explain the impulse?",
    "What confidential matter is Jin Wikyung withholding?",
    "What are the terms of the Peace Guild–Wizard Guild agreement, and what evidence is contained in Lee Jungryong's holographic recorder?",
    "What emergency has caused the Zhuge Clan's covert security measures and the fear surrounding its territory?"
  ],
  "safe_through": 444,
  "temporary_decisions": [
    "Render 시부럴 as “sibu-leol,” 시벌좌 as “Lord Fuck,” and 시부럴좌 as “Lord Sibu-leol.”",
    "Preserve the Skeleton King's grandiose, mock-offended voice and Taekyung's dry, profane humor.",
    "Render 최 팀장님 as “Team Leader Choi,” 진태경 씨 as “Mr. Jin Taekyung,” 막내야 as “my youngest,” 노야 as “Old Master,” and 노 선배님 as “Senior.”",
    "Keep Peace Guild, guild house, Inventory, Magic Johnson, established martial-arts terminology, black magic, poison human, World Hunter Association, and Wizard Guild unchanged.",
    "Render 신기제갈 as “Divine Mechanism Zhuge,” 파선지왕 as “Fan-Wisdom King,” 와룡객 as “Crouching Dragon Guest,” 복룡산 as “Mount Fulong,” and 융중산 as “Mount Longzhong.”"
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 440

# Chapter 440

The day Jin Taekyung’s private jet landed at Incheon International Airport, cameras from around the world turned toward Korea.

The countless flashes erupting without pause were bright enough to make people forget that the sun was already setting. Despite the midwinter cold, hundreds of thousands of people packed the surrounding area and sent up a blazing cheer for the hero’s return.

And at the center of it all stood one man, staring blankly at the scale of the welcome, which had far surpassed anything he had expected.

“...What the hell is all this, goddammit?”

His voice was as small as an ant, but the news outlets from around the world had brought in their best equipment. They didn’t miss the young hero’s offhand remark.

“What the sibu-leol?”

“Que veut-elle dire par là?”

“Was meint sie damit?”

It was already famous that Korean profanity was so diverse that even translation devices struggled with it.

Western reporters who failed to properly understand the rich meaning of *sibu-leol* hesitated, but Korean reporters who had mastered every bizarre curse imaginable since their school days moved like lightning.

“Write it up! Hurry and get the article online! We have to be first!”

“W-With this?”

“You idiot, don’t you know that everything Jin Taekyung does is breaking news right now? Stop wasting time talking nonsense. Get a shot of the way his mouth moved when he cursed, grab the audio, and upload it immediately!”

“Yes, Senior! But, Senior… won’t this cause trouble?”

“Trouble? What trouble?”

“If it looks like we’re attacking Jin Taekyung, we could suffer a backlash. You know, the Jin Taekyung profanity controversy or something…”

The veteran reporter scowled at his junior.

*Was that kid in his second year now, or his third? After working in the field this long, he should have learned to think, but he was still hopelessly slow on the uptake.*

The veteran reporter barely held back a curse when he remembered that the idiot in front of him was the bureau chief’s nephew.

“Hey. Reporter Hong.”

“Yes.”

“Jin Taekyung is allowed to swear.”

“What?”

“Politicians and celebrities become the worst people alive if they curse at a public event in this country. But when Jin Taekyung starts swearing, people nearly die of happiness. Do you understand?”

“Yes, yes, Senior!”

Only then did the junior nod. The veteran reporter let out a deep sigh and looked at his smartphone.

The chatroom for the live stream currently airing on iTube, the world’s largest video-sharing website, was already exploding out of control.

ㅅㅂㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋSibu-leol.

Lord Fuck… *he* is back.

Lord Balls is here too. I saw him say he’d bet his balls on the Chinese news earlier and laughed my ass off, seriously lmao.

King Taekyung. The bastard who accomplished something incredible, told every interview to fuck off, and wrapped up his official press conference in thirty minutes…

And yet he fought like hell to rescue the survivors until the very end…

The bastard who bet his balls instead of money on a Chinese state-run broadcast watched by at least ten million people…

The bastard who kept saying *sibu-leol* in front of the entire world…

King Taekyung. Infinitely warmhearted, but completely insane…

ㅋㅋㅋㅋㅋㅋ Is he even a Hunter, or is he some kind of eccentric?

Nope, he’s Lord Sibu-leol.

ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ Lord Sibu-leol is pretty good.

ㅋㅋㅋㅋㅋㅋㅋㅋ Actually, didn’t King Taekyung say something like that in one of his earlier interviews? He asked people to stop calling him Lord Fuck.

Really? Got it, hyung! From today on, I’ll call him Lord Sibu-leol!

He doesn’t like Lord Fuck? Then we have to call him Lord Sibu-leol from now on lmao.

Lord Fuck + Lord Balls = Lord Sibu-leol.

Look at that buildup lmao. At this point, was it intentional?

Hello, everyone. What do you think about the fact that Mr. Jin is a descendant of Jin Chui, who was a Ming dynasty general? China is a great and powerful country, so if he were to become a naturalized citizen, it would be an even better opportunity for him. Oh, and for the record, I’m Korean.

??????

Why are you suddenly dumping jajang sauce in here…

Take care on your way home, Wang.

If that bastard is Korean, then I’m an Asgardian. I drank beer with Thor in Valhalla yesterday.

Heh, Chinese as expected. You give yourself away immediately because you’re an idiot lmao. Of course, Jin Taekyung is an idiot too. I’m Korean as well, but I think it’s a nuisance to everyone when he uses such vulgar language at an official event like today. At the very least, there’s something to learn from our neighboring country Japan when it comes to national character.

????

Jajang sauce wasn’t enough, so now you’re dumping wasabi on us too…

Heh, that sounds like some Japanese right-winger trembling with rage at King Taekyung. Why are you so stupid?

??? : Magdonaldo. Ssankyu!

Please watch your own country’s broadcasts. Stop coming to Korea’s official channel and pretending to be Korean.

Lmao, it’s hilarious how hard you’re denying reality. I really am Korean.

Where do you live?

Seoul City, Busan District.

Ha…

There’s a reason people call this place Hell Joseon.[^1] What is this, left Azure Dragon and right White Tiger? We’ve got left jajang and right wasabi.

There’s even a Devil Fruit user up north.

??? : Uncle-in-law, uncle-in-law, total barrage!

Don’t get baited by weirdos. Watch the broadcast. The car parade is just about to start.

It really is. Don’t get angry over pointless stuff, hyungs. Let’s just watch King Taekyung.

[^1]: “Hell Joseon” is a cynical nickname for South Korea, comparing modern society to the rigid and oppressive Joseon era.

Broadcast networks, cable channels, and general programming channels were all showing the scene. On top of that, viewers around the world were watching through iTube’s live stream.

With an uncountable number of people watching, the large limousine bus carrying Jin Taekyung and his companions began to move.

The cheers grew louder, flashes burst everywhere, and drones filled the sky overhead, painting patterns across the night.

Wow, this is insane. There are so many people that the cameras can’t even fit them all in the frame ㄷㄷ;

This is bigger than the Olympics. How many drones are there, anyway?

A lot, I guess?

I know that much…

I got goose bumps when the bus started moving without me even realizing it. Is it really possible for your heart to feel this grand?

The limousine bus carrying Jin Taekyung and his companions moved at ten kilometers per hour through a wall of people.

Brilliant fireworks exploded without pause, and flower petals scattered by the crowd whirled through the air on the wind.

At first, Jin Taekyung watched the situation with an awkwardly stiff expression. Before long, however, he smiled and waved at the crowd.

*They’re people who like me.*

Six months ago, Jin Taekyung had been no more than a grain of sand on a beach.

An F-rank Hunter who could be found anywhere, unnoticed by anyone and swept away when a wave passed over him.

He had never once imagined that a day like this would come.

*I only dreamed of retiring without dying…*

He had gained far too much. He had been forced to walk a thorny path with death spread out in every direction, but the fruit hanging along the way had been sweet. Power beyond his wildest imagination, enormous wealth, and even fame.

And…

“You’ve worked hard, my son.”

“I’m incredibly proud of you too, Mr. Jin Taekyung, but these flashes are so bright that I can barely see your face. How long are those reporters planning to keep doing this?”

His family, who had always been with him.

His mother’s warm hand stroking his back made his throat tighten, while the sight of his sister scrunching up her face against the flashes made him let out a quiet laugh.

“Mom worked harder than I did. You too, Sis.”

“I know. I know Mom and Oppa worked harder.”

“I thought you were barely human, but you have a shred of conscience after all.”

“Wow, listen to him.”

“Smile, you idiot. Do you have any idea how many cameras are filming us right now?”

After hugging the two of them with that joking remark, Jin Taekyung met a pair of eyes watching him from behind his family.

“You’ve truly worked incredibly hard, Mr. Jin Taekyung.”

“You too, Team Leader Choi. I’m just a big, dumb brute who’s good at using strength. I would’ve had a really hard time without you.”

“I only did what I had to do. And I will continue to do the same.”

“You’re saying something scary with a smile.”

“You know, don’t you? That this isn’t the end.”

He knew.

That was why he hardened his resolve even further.

Jin Taekyung had made it this far after crossing a perilous field of thorns. He couldn’t allow his precious family and friends to walk the same path.

Even if his feet became covered in blood and he collapsed from the pain, he would protect them from the threats drawing ever closer.

Sometimes they would join forces. And even if it meant sacrificing himself…

“Please take care of me. From now on, too.”

Team Leader Choi stared at the hand Jin Taekyung extended. Then a deep dimple appeared beside his mouth.

“Yes. Always.”

Just as the two clasped hands firmly, a grumbling voice rang out inside Jin Taekyung’s head.

—You’re all having a grand old time.

*Are you still sulking?*

—Who is sulking?! Does this body, reborn as the great king, look like it would feel such a worthless human emotion?

*You’re definitely sulking.*

—I am not!

The attention seeker—no, the Skeleton King—who had been forced to hide in the Inventory for the time being had been sulking bitterly for quite a while.

Jin Taekyung smiled faintly and muttered inwardly.

*Hey.*

—Do not speak to me!

*Thanks for everything up to now. I’m counting on you from here on out, too.*

—H-Hmm.

After letting out a fake cough, the Skeleton King continued in a hesitant voice.

—Since you put it that way, I shall consider it.

*Consider what?*

—Going with you, you vile human, of course.

*Oh, you don’t need to consider that.*

—What?

*You have to join Peace Guild no matter what. I’ve already had the contract drawn up, so go put your thumbprint on it. No, wait. Your fingerprints won’t turn up in a records check, so I guess you’ll have to stamp it with your skull.*

—What is this?! Is this not a liberal democratic country?!

*Yeah. No. I’m going to milk you like a slave, right down to your marrow.*

—Release this body immediately! Turn the car around!

Unable to hold it in any longer, Jin Taekyung burst out laughing and leaned toward the driver’s seat.

“Could we go to the next destination like this?”

“Pardon?”

The startled driver stammered out a reply.

“That’s different from the instructions we received beforehand.”

“Can’t we?”

“I’m sorry, but we can’t.”

“We really can’t?”

“I’m afraid not…”

“Seriously, truly, we can’t?”

The driver answered in a voice halfway to giving up.

“…It seems we might be able to.”

“Then please take us to Peace Guild’s guild house.”

The driver relayed the information to his superior. After passing through several levels of reporting, the higher-ups were bewildered but readily agreed.

And the roughly three thousand drones moved along with the seemingly endless car parade.

The limousine bus carrying Jin Taekyung and his companions eventually came to a stop in front of Peace Guild’s guild house.

Every moment of their meeting with the Guild members waiting there was captured by cameras and broadcast across the world.

Even after midnight passed and the long-awaited Christmas Eve arrived, the fervor did not die down.

No. The dying flames only received fresh firewood and a new gust of wind, as though competing with one another.

People could see the name Jin Taekyung everywhere, and for someone still suffering from severe aftereffects, it was an unbearable torment.

—This morning, the United States’ S-rank Hunter Magic Johnson announced through his official social-media account that he is pursuing some kind of agreement with Peace Guild—

*Bang!*

The announcer’s face vanished from the holographic television. The man who had smashed the machine let out a scream.

“Jin Taekyung, Jin Taekyung, Jin Taekyung!”

*Bang! Crash!*

His eyes were bloodshot. Powerful qi fired from the ends of his wildly swinging fists smashed everything around him and reduced it to dust.

That name was more hateful than any other.

At the same time, it was the name of the man who had shown him a fear he could never forget!

“Aaaaaaaagh!”

Just as the man, Go Jun, was howling in the devastated space, a faint stir accompanied by a cautious voice reached his ears.

“T-Team Leader.”
## Chapter artifact 441

# Chapter 441

“T-Team Leader. May I come in for a moment?”

His voice was taut with tension.

Seok Go Jun reached toward the door while glaring at it with bloodshot eyes.

*Crack!*

A powerful force shot through the air, tearing and crumpling the iron door like a sheet of paper.

The security-team employee who witnessed the incredible sight from a few feet away swallowed a startled breath.

“Gasp.”

“I told you not to let anyone approach.”

The team member met Go Jun’s red glare head-on, and a shiver ran down his spine.

He had heard his colleagues talk about the extreme change in their direct superior, who had always been as precise and cold as a machine. But facing him like this, the team member’s voice trembled with fear despite himself.

“I-It’s just that… there’s something I need to report…”

“Put it off.”

His low voice sounded as though it had been dragged up from the depths of an abyss.

The team member wanted to do exactly that. But if it had been something trivial, they would never have drawn lots to decide who would deliver the report.

Swallowing hard, he squeezed out his courage and spoke.

“The head of the investigation team contacted us urgently. They said they discovered a strange object whose identity they couldn’t determine…”

Go Jun, who had been about to turn away, came to an abrupt stop.

“A strange object?”

“Yes, Team Leader.”

“Could it be—”

“No, sir.”

Worried that the sparks might fly his way, the team member hurriedly continued.

“After checking, we confirmed that none of the late Vice Guild Master’s belongings have been found yet.”

“Are you sure?”

“Yes. We’re keeping the team members dispatched to the site under constant watch in case they try to pocket something. There’s no doubt.”

“And?”

“Pardon?”

“There’s only one report I need from those bastards. A report saying they found what I need.”

Go Jun’s eyes sank into darkness.

Even now, with the Crown Prince Party—closely tied to the Ares Guild—on the decline, the Ares Guild’s influence and power remained intact.

Greed did not disappear just because the person in charge changed or the government was replaced. Everyone had it.

Even a straight bamboo stalk bent when it could no longer bear its weight. Go Jun had created that weight with tens of billions of won.

The head of the investigation team managing the city that had once been the Arch Lich’s stronghold and the senior officials under him were no different.

“Tell those bastards to find it, no matter what it takes. And tell them not to contact me again until they do.”

There was no such thing as a favor in this world without a price. Go Jun had bought them with a fortune, and if they failed to deliver what he wanted, he intended to retaliate accordingly.

That was how important the object he was searching for was.

Not merely because it was a keepsake of the Master he had followed like a father. It could also become a powerful weapon capable of driving someone into an inescapable corner.

*A holographic recorder.*

Lee Jungryong had been the true master of the immensely influential Ares Guild, and he always carried a small holographic recorder on his person in case something happened.

He had carried it on the day he met his death at Jin Taekyung’s hands, too.

*All the evidence is in there. If I can find it, then afterward…*

At that very moment, the flames burning in Go Jun’s eyes began to shake violently.

*Afterward… what am I supposed to do?*

Before he knew it, the face of one man—someone he hated beyond measure and feared even more—flashed before his eyes.

*…Jin Taekyung.*

Just thinking of that name made his heart sink and his hands and feet tremble.

The indifferent gaze that had looked down at him beneath the faint moonlight and the dry voice that had accompanied it clouded his eyes and ears like an apparition.

*I’ll say this one last time.*

The voice had burrowed into Go Jun’s ears as he howled from pain he had never imagined possible.

*Let Lee Jungryong be the end of it. Hide your teeth and put away your claws. If you do that… nothing will happen.*

Every bone in his body had been crushed like matchsticks, and his living flesh had been torn away as though it were being wrung out. He had been forced to struggle in a bottomless swamp of pain without ever managing to swing his weapon properly.

If Lee Jungryong had been a wall Go Jun could never cross and a Master he revered, Jin Taekyung was something no one had ever seen before.

No. He was like…

“A monster.”

The single word that escaped Go Jun without his realizing it was steeped in all the emotions and fear he felt.

And in the next instant, when he came to his senses, Go Jun realized something.

His hatred of Jin Taekyung was nothing compared to the fear he carried.

Jin Taekyung’s existence was fear itself, branded forever into Go Jun’s soul like a mark burned into flesh. At the same time, it was another name for the perfect helplessness he had felt for the first time in his life.

“T-Team Leader?”

Go Jun did not answer the team member’s call. He lowered his head with his teeth clenched, and his gaze fell on his own trembling hands.

*What the hell is this…*

*Crunch.*

Go Jun bit his lips until they bled, then raised his head. Ignoring the team member’s bewildered stare at the sight of his frightened superior, he opened his mouth.

“Tell the head of the investigation team to bring me that damn strange object. I don’t know what it is, but I need to see it for myself.”

“But a moment ago, you said—Ah, understood.”

Realizing his mistake, the team member hurriedly bowed and left the room.

Only after walking a considerable distance down the corridor did he finally release the breath he had been holding. Then he gestured toward the hotel employees waiting nearby.

“Wait here for a while. Go in once he’s calmed down. And the new room is ready, right?”

The Chinese hotel employees nodded with calm expressions.

This was not the first time Go Jun had gone on a rampage. It had already happened several times over the past week.

But what did it matter?

Until a few days ago, the hotel had belonged to a local notable in Sichuan Province. After the Ares Guild purchased it, the Koreans standing before them had become their new employers.

They were the best employers imaginable, even handing out generous overtime pay to ensure their secrecy.

“There’s no point saying any more. We all know the situation, so let’s do our jobs properly.”

The team member tossed a thick envelope to them, wiped the sweat from his brow, and walked away.

It was already a problem that they still hadn’t managed to leave this cursed land of China. But the uneasy state of the man who would become the Ares Guild’s new captain after Lee Jungryong kept sticking in his mind.

*Could that rumor really have been true?*

He remembered something that had been circulating quietly within the security team.

And he remembered his own unsettled feelings.

*The treatment is incredible, but if Team Leader stays like that from now on…*

There would be no problem if Go Jun remained the head of security. The enormous warship called the Ares Guild was not so fragile that one mistake by a helmsman could make it capsize.

But if he became the new captain, that was a different story.

*Damn it. I’ve never had to worry about something like this before.*

The team member muttered to himself and pulled a smartphone from inside his suit jacket. It was a work phone that left no records and could not be traced.

After a long series of rings, someone answered.

“Ah, Mr. Park. I was waiting for your call.”

“I’ll get straight to the point. Our team leader wants to see the object you mentioned in person.”

“In person?”

“Yes, in person. Our team leader wants to avoid people’s attention as much as possible right now, so you understand what I’m saying, correct?”

The recipient of the call, the head of the investigation team, cleared his throat.

“Cough. That may be difficult. Since this is the Arch Lich’s former stronghold, there are also foreign personnel dispatched by the United Nations, and security is tighter than you might expect…”

“Name your price. But there must not be a single mistake.”

A short while later, the team member ended the call and clicked his tongue.

“Those bastards. All they care about is money. Well, I suppose that’s why this worked out.”

The world did not change easily. Faced with overwhelming money and power, the word *impossible* had no meaning.

Since joining the Ares Guild’s security team, he had witnessed countless situations where the impossible had been made possible.

And that fortresslike power would naturally be inherited by one man.

*Team Leader Go Jun.*

The Ares Guild’s new captain.

The team member was only one of countless rowers, but Go Jun was different. When his thoughts reached that point, he suddenly became curious about the one person Go Jun feared so much.

*Jin Taekyung.*

People’s mouths could never be sealed completely.

The rumor had begun when three Hunters who had secretly left with Go Jun one day a week earlier opened their mouths.

For now, only a tiny number of people within the security team—who could be called Go Jun’s closest associates—knew the truth. But soon, it would spread like an epidemic.

*If it’s true…* *Haa. Things have gotten seriously complicated.*

The team member took a deep breath and sharpened his gaze.

From this point on, he would have to agonize over countless decisions. Should he remain on his current ship, or set sail for a new one?

If he did not want to become anyone’s enemy, his only option was to leave this line of work entirely.

*I need to keep my head on straight. Yeah.*

For now, his first priority was bringing back the object the head of the investigation team had smuggled out.

As he traveled to the place they had agreed to meet, he suddenly found himself envying Jin Taekyung.

*Damn. If I had fifty trillion won like that bastard, I’d go straight to Europe and live like royalty.*

He was rich too, owning several buildings, but human greed was never easily satisfied.

It was like wanting an expensive yacht and helicopter after buying a luxury foreign car, then wanting a private jet of your own after that.

The team member smacked his lips in envy.

*I wonder what that Jin Taekyung is doing right now. Having a luxury-yacht party with Playboy models?*

* * *

Beneath the blazing sunlight, well-tanned bronze muscles rippled.

Their identity was that of beautiful model women from around the world who had gathered to enjoy a yacht party with me…

“One, two!”

“Heave-ho!”

…No. They were the river bandits of the Water Dragon Stronghold.

I gazed sorrowfully at the musclebound monsters working busily around me.

*A yacht party, my ass.*

I had only ever seen those on the internet, and I planned to keep it that way.

Reality was not a yacht party with beautiful women. It was standing on a deck packed with musclebound river bandits who had been put through onboard personal training, staring out at the Yangtze.

No. There was one more thing.

*Whoosh!*

I had to dodge the finger flicks our boisterous Old Master, Fire King Jeok Cheongang, sent flying whenever he got bored.

“Oh? You dodged?”

“…This is training to dodge them, isn’t it? You said I had to maintain a mind as clear as a mirror and heighten my senses to become accustomed to the Middle Dantian.”

Jeok Cheongang answered shamelessly.

“That one was meant to hit you. How dare you look away during training?”

“I was looking away with both eyes.”

“Don’t push me. Want me to gouge them out?”

Eyes blazing with fury, Jeok Cheongang raised his fingers like claws and continued.

“Do you think this training looks easy? Even with your full concentration, you’ll barely manage to avoid them.”

“Fine, fine. I understand. I said I understand.”

Grumbling, I shut my eyes. Then, in the next moment, I quietly opened them again.

“But…”

“What?”

“Didn’t I just dodge that perfectly even while looking away?”

“Oh. So you did.”

“…?”

“…?”

“!”

“!”

What the hell was this?

Jeok Cheongang had pressed his lips tightly together beneath my incredulous stare. Then he suddenly exploded in anger.

“Not like that! Do it like that brat! Like him!”

The direction of his fingertip pointed toward a young man sitting cross-legged without the slightest movement.

For some reason, Cheongpung had been forced to participate in training alongside me.

“Look at that brat. He may be a little strange normally, but when it matters, he does everything perfectly. His posture hasn’t wavered, and he’s maintaining a thin, long, steady breath. An unwavering mind and posture, no matter what happens around him. That is what it means to be clear as a mirror and still as water.”

After showering Cheongpung with praise without even stopping to breathe, Jeok Cheongang pointed at him and continued.

“Watch carefully how he dodges. Now, when I send a finger flick…”

*Whoosh! Thud!*

A finger flick struck Cheongpung in the temple, and his eyes flew open.

He looked around with his eyelids drooping sleepily, then rubbed his head once the pain finally seemed to register.

“Ow. That hurts…”

Then he returned to his dream faster than light.

I stared at Jeok Cheongang and asked,

“Clear as a mirror? What?”

“Clear as a mirror… Forget it. You and that brat, both of you. To hell with all of it!”

The Yangtze was peaceful today, too.
## Chapter artifact 442

# Chapter 442

Like the Yangtze flowing majestically onward, time passed slowly but steadily.

It was late afternoon on the fourth day since we had left Sichuan by Murim reckoning. As I sat on the deck, a familiar presence approached.

“What are you doing?”

I knew who it was just from the footsteps.

Without taking my eyes off the Yangtze, I answered,

“What does it look like I’m doing?”

Hyuk Mujin approached with a limp and answered without hesitation.

“Looks like you’re just sitting there.”

“I’m thinking.”

“About what?”

“About the peace of Murim.”

After a brief silence, a hearty laugh burst out.

“Pfft-hahaha! That’s the funniest joke I’ve heard all year. Just like you, Captain.”

“No. I take it back. I just thought of something else.”

“What?”

“There’s a certain bastard who always takes everything I say for dog shit. But maybe because he’s been feeling better lately, he doesn’t seem able to control his mouth. So I’m wondering whether I should beat him a few times. What do you think?”

Hyuk Mujin thought for a moment before asking,

“It isn’t the person I’m thinking of, is it?”

“Probably.”

“Who is it?”

“There is someone. A man named Hyuk Mujin.”

“…”

“Be quiet unless you want another taste of the Yangtze.”

Hyuk Mujin nodded frantically, practically having a seizure.

“Please, anything but that…!”

A few days earlier, after sentencing him to the Yangtze-dipping punishment, I had immediately logged out, leaving Hyuk Mujin to spend an entire shichen sightseeing at the Yangtze Aquarium.

The moment Mungyeong’s superb medical skills had restored him to a reasonable condition, he had even cast out a fishing line, declaring that he would catch every last one of the bastards who had bitten his nose and turn them into sashimi.

“Fine, calm down. Why are you here?”

“Huh?”

“I’m asking what you want. You must have a reason.”

Hyuk Mujin asked in a wounded voice,

“Do I really need a reason to come see you? Between us?”

“If you don’t have one, you get a taste of the Yangtze.”

“I do! I have one!”

“Then spit it out.”

“This might just be my impression, but…”

Hyuk Mujin continued hesitantly.

“Have you been worried about something lately?”

“Why?”

“Just because. Recently, whenever I look at you, you seem like you have a lot on your mind.”

“I do?”

“Yes. And, well… To be honest, nothing particularly significant has happened lately compared to before. But somehow, you’re the only one who seems tired and busy. That’s the best way I can put it.”

“…”

“You also seem to be sleeping more often.”

When had this bastard gotten so perceptive?

Under my strange gaze, Hyuk Mujin scratched the back of his head.

“Well, that’s just the impression I got. Am I wrong?”

“Yeah. You are.”

Naturally, my answer was a lie, and Hyuk Mujin’s guess was exactly right.

Since first setting foot in Murim, I had never gone back and forth between the two worlds as often as I had recently.

*Looking back, every one of those trips was my own choice.*

Sometimes a Quest had blocked the Logout function, but most of the time, I had made the decision myself.

If I had crossed over to the other world and spent time there while walking across thin ice, my tension would have collapsed, and I would have been unable to overcome the crisis.

But recently, the situation had changed.

*Both the modern world and Murim have made it over one mountain.*

How long had it been since both worlds had grown quiet at the same time?

Murim had been a minefield where disturbances never stopped from the beginning, while even the relatively peaceful modern world had begun to grow chaotic after my conflict with Lee Jungryong.

For the first time in a long while—or rather, for the first time since I had obtained the System—I had found peace in both worlds.

But deep down, I had a suspicion bordering on certainty.

The current peace would not last long.

The calm before the storm. The brief peace I had been given felt like the stillness on the night before a storm broke.

That was why I was busily traveling between the two worlds to prepare for the storm that would soon arrive. It was also why, even with the spectacular Yangtze scenery spread out before me, I was hunched over a mystery that refused to yield.

*What the hell is this, anyway?*

I stared intently at the paper in my hand.

The not particularly high-quality xuan paper was covered with strange patterns and symbols I had drawn myself.

They came in various types and forms. Though each differed only slightly, they looked like mysterious letters from a detective novel.

No. I would almost prefer that to be the case. Then I wouldn’t have to worry about them this much.

“What is that?”

“A storm.”

“Huh?”

“To be honest, I don’t really know either.”

No, perhaps I already knew and simply did not want to believe it.

These patterns and symbols were the only common ground between two worlds whose flow of time, history, and culture were all different.

In the modern world, they had been found in the Arch Lich’s magic circle. In Murim, they had appeared in Dark Heaven’s formations.

And now, deep in my heart, I was turning over a single word.

*Black magic.*

The martial arts of those Murim deemed demonic and heterodox—what people commonly called demonic martial arts. I had no idea how bizarre or far-ranging they could be.

But the more I looked back on everything I had personally seen and experienced, the more it resembled black magic.

*The Blood Lord, the Western Heaven Demon Lord, even the formation found in the cave.*

The way the Blood Lord recovered from Jeok Cheongang’s Dance of the Fire God and Demon was like that of a Troll, not a human. The Lord of Heaven worshiped by the Western Heaven Demon Lord had appeared before me by borrowing the body of a subordinate who was already dead.

On top of that, the formations used by the black-robed men who had stained Shaolin and Sichuan with blood in service to their respective leaders were astonishingly similar to what the modern world called a Warp Gate.

*At this point, it would be strange not to have suspicions.*

At the same time… the fact that I did not want to believe it easily was my reality.

Black magic in Murim.

It was more serious than discovering that a female friend I had a crush on had used the bathroom in my house and left the toilet seat up.

*Where? How? Why?*

My head was full of question marks. An investigation was already underway in the modern world, but I felt like I was wandering through fog with no end in sight.

And even more frightening was the unknown something waiting beyond that fog, still refusing to reveal itself.

If every one of my fears turned out to be true, then…

“What are you looking at so intently?”

The voice shattered my deep thoughts and brought me back to reality. I frowned.

Not because my train of thought had been interrupted, but because of the sour stench stabbing at my nose.

Suppressing the nausea rising instinctively, I asked,

“Did you not wash again?”

Gung Gibang, who had subtly pressed his butt against the spot beside me, nodded.

“It’s only natural for a beggar not to wash. Is there a problem?”

Hyuk Mujin opened his mouth with a queasy expression.

“Young Hero Gung, are you perhaps a poison human? The moment you came within three jang of me, my head started spinning and I began dry-heaving.”

“A Beggars’ Sect disciple washes only three times in his life: when he is born, when he enters the Beggars’ Sect, and when he dies.”

I spoke to Gung Gibang, who was spouting bullshit.

“Then go dunk yourself in the river before I kill you right now. And since you’re doing it anyway, scrub off some of that grime while you’re at it.”

“No. I hate water. Especially since that day.”

Ah. Right. He was a victim of the Yangtze, too.

Gung Gibang answered with a severe expression, then glanced at the paper in my hand.

“Were you looking at that again?”

“Again? Young Hero Gung, you knew about it?”

At Hyuk Mujin’s question, Gung Gibang nodded.

“Of course. A few days ago, he suddenly told me to follow him and showed it to me. He asked whether I had ever seen it somewhere before. Naturally, I told him I was seeing it for the first time.”

“Captain, is this how you discriminate between people?”

I gave the wounded Hyuk Mujin a warm smile.

“Yes. It is.”

“…”

“I showed it to you because you’re the Successor Beggar. I thought you might know something. Satisfied?”

Gung Gibang, who had found something to tease Hyuk Mujin about, snickered.

“He showed it to Mungyeong, too.”

“Hey, that’s…”

I had opened my mouth, but I could not reveal Mungyeong’s identity, so I shut it again.

It wasn’t only because I saw Mungyeong several jang away, watching us as he pointedly stroked a large acupuncture needle.

*Seriously.*

“Look, you Hyuk bastard. This is where you stand. Not in the heart, but in the little toe. Ow!”

*Grab—whoosh!*

Listening to him had become so irritating that my ears hurt. I grabbed Gung Gibang by the collar and threw him over the railing.

He flailed in midair, then crashed into the river with a single shriek.

Splash!

He must have hit the water fairly hard, because the spray reached the ship’s railing.

Then, in the next moment, Cheongpung, who had been giggling at the surprise event, suddenly screamed.

“No! Mimi!”

What now?

Wondering what had happened, I looked more closely and doubted my eyes.

A horned snake, pure white from head to tail, was swimming desperately toward us while thrashing around like a lunatic.

The clear waters of the Yangtze were turning pitch-black around Gung Gibang’s body, and several fish that had been swimming peacefully nearby were floating belly-up.

“…What the fuck?”

Even the Thousand-Year Poison Horned Snake was reacting like that. Was Hyuk Mujin right? Was Gung Gibang really a poison human?

The river bandits who witnessed this utterly absurd water-pollution spectacle in real time began seriously debating whether Gung Gibang belonged to the Beggars’ Sect or the Sichuan Tang Clan.

I let out a deep sigh and gestured toward them.

“Get him out quickly. If you want to keep working as river bandits on the Yangtze.”

The river bandits realized that their livelihood was under threat and began bustling about.

* * *

After that, I continued traveling between the modern world and Murim once or several times a day, taking care of what needed to be done and continuing my investigation.

News that my Peace Guild and the Wizard Guild led by Magic Johnson had entered into some sort of agreement became a major topic of conversation among Hunters around the world.

But to ordinary people, the bigger story was still about me, the individual named Jin Taekyung.

> World Hunter Association: “Jin Taekyung is an undeniable S-rank Hunter and a hero who has saved countless lives. It is absurd that he is still only an A-rank Hunter.” He is scheduled to visit the Association headquarters for a brief test, after which his S-rank Hunter license will be issued. A passionate personal invitation from the World Hunter Association!

> Breaking News: Jin Taekyung flatly rejects the Association’s offer. “I have circumstances that make it difficult to go right now. I’ll stop by when I have time.” The World Hunter Association is thrown into confusion.

> World Hunter Association issues a new statement: “This is unprecedented. S-rank Hunter testing and licensing have always been conducted at the Association headquarters.”

> Jin Taekyung: “I didn’t say I wouldn’t take the test. I said I’d go later. And I can take the test in Korea, so what’s the problem? Before you start talking about precedent, let’s try doing things efficiently.”

> A senior Hunter Association official, wounded in his pride, issues a threat: “Then we cannot issue you an S-rank Hunter license.”

> Urgent Breaking News: A brief post uploaded to social media reads, “Then don’t. Where do you get off threatening me? Sibu-leol.” The account is revealed to be Jin Taekyung’s official social-media account… How is the public reacting? “That’s so satisfying.” “Cooler than the soda we drank during the Thousand-Li March.”

> World Hunter Association: “The official’s statement was a personal slip, not the position of the organization. We apologize.” Final decision made to dispatch a testing team to Korea for Jin Taekyung.

> Japanese Prime Minister Koizumi: “Jin Taekyung is fun, cool, and sexy. I will definitely have him naturalized as a Japanese citizen. Because that is my ‘promise’…”

Leaving behind the countless incidents and remarks surrounding me, I returned to Murim.

And then…

“I can finally breathe again. Damn Yangtze.”

Alongside Jeok Cheongang’s heartfelt exclamation, the bow of the fast ship that had continued its voyage for nearly ten full days entered Hubei Province.
## Chapter artifact 443

# Chapter 443

Ten days of sailing had been anything but easy.

We hadn’t been traveling on some massive cruise ship. We’d been stuck on a wooden vessel, going back and forth between musty cabins and damp decks. Ports? With our schedule so tight, we’d simply kept our eyes ahead and sailed on.

Under the circumstances, even Jeok Cheongang—and the river bandits who called the Yangtze their home turf—looked delighted.

Of course, one person was happier than all the rest.

“Ohhh, finally…”

Mu Song, who had been forced into volunteering his talents all the way to Hubei Province, trembled with emotion.

He had been sunk in grief ever since one of his fast ships had gone down, but now he shouted in a powerful voice as if he had forgotten all the hardships he had endured.

“Lower the anchor! Get it down before another second passes and we can leave this damn—!”

Jeok Cheongang, who had been nodding in satisfaction, turned to look at him.

“This damn what?”

Mu Song had accidentally spoken his true feelings and shook his head at tremendous speed.

“N-no, sir. I meant the Yangtze.”

“Of course you meant the Yangtze. That’s what this old man meant, too.”

“…”

“Unless you were calling us damnable?”

“W-why would I ever do that?”

He certainly looked like he would.

While Mu Song sweated beneath Jeok Cheongang’s narrowed gaze, the river bandits immediately recognized their leader’s crisis and sprang into action.

The fast ships gradually slowed, lined up along the pier, and dropped anchor. A small murmur rose from the people gathered near the harbor.

“That flag…”

“The Yangtze River Channel League. It’s the Yangtze River Channel League!”

“What does it say underneath? Water Dragon Stronghold? I’ve never heard of it.”

“It’s a river stronghold based in Sichuan. Water Dragon Stronghold is the one led by Ship-Fire Boy Mu Song, the second Disciple of the Seafaring King.”

“Now that you mention it, I think I’ve heard of it. But why are those bastards in Hubei when they’re supposed to be in Sichuan?”

“How should I know? Damn river bandits. Things have been tense enough lately as it is…”

“Shh. Keep your voice down. Some young man is looking this way. Nothing good comes from getting tangled up with Murim.”

The group of merchants whose eyes met mine hurriedly left.

And they weren’t the only ones.

A fisherman with a face darkened by the sun grabbed his net and scurried away. A vendor selling his catch folded up his stall at the speed of light.

In the distance, an official dressed in formal robes watched us carefully while being escorted by government troops.

Their eyes held undisguised wariness.

*What the hell? This atmosphere is completely different from Sichuan.*

The Yangtze River Channel League might have been a river-bandit organization built on the foundation of plunder, but it had its own rules and system.

I had heard that they didn’t simply rush in whenever they saw an opportunity, kill everyone in sight, and strip a ship bare. Sometimes they even protected vessels from rogue river bandits, and under normal circumstances, they only collected a set toll before allowing ships to pass.

*They did test the waters during the Great Faction War, but in the end, they sided with the orthodox faction.*

When something comes in, something has to go out.

During the upheaval that decided the direction of the Murim world, the Yangtze River Channel League had supported the orthodox faction and paid the government enough bribes to keep everyone satisfied.

In other words, they were legal thugs for hire wearing the mask of legitimacy—tolerated by both sides and allowed to carry on.

They couldn’t exactly be called good people, but this was Murim, where all kinds of lunatics ran wild. Even if they weren’t gentlemen, they were at least respectable scoundrels.

*That’s why ordinary people in Sichuan didn’t react much.*

Their attitude had been more like, *Those vagrant bastards are back again, and they still haven’t died?* They hadn’t openly avoided us like this.

I tilted my head as I watched the people scatter in every direction.

*Is it just a difference in atmosphere from one region to another?*

But if that was all it was, Mu Song’s expression seemed far too grim.

He stared at the suddenly empty harbor with a deeply furrowed brow, then called over his right-hand man.

“Have we received no word from our brothers in the League?”

“No, Stronghold Lord. They must have known we were coming, but for some reason, there has been no contact.”

“Not even from Dangyang Stronghold or Honghu Stronghold?”

“That is correct.”

“Even if the others didn’t know, Donghu Stronghold is where Uncle Hwang is. There is no way he failed to hear that we were coming…”

Mu Song muttered with a serious expression before continuing,

“Once we disembark, send out the swiftest men and find out what is happening. Contact our nearby brothers immediately as well.”

“Yes, Stronghold Lord.”

At Mu Song’s gesture, the river bandits under his command moved as one. We were no exception. We had finished preparing to disembark some time ago.

Jeok Cheongang, who was finally leaving the Yangtze behind, led the way at once. I followed, then Jin Wikyung, Cheongpung, Hyuk Mujin, and Gung Gibang.

Mungyeong was there too, blending quietly into the crowd as if he were both present and absent.

At last, Jeok Cheongang—the Fire Pokémon finally free of his type disadvantage—wore a bright smile across his face.

“Whew. I can finally breathe again. This is why people are meant to live with their feet on land.”

But Jeok Cheongang’s happiness didn’t last long.

“You there. Stop.”

The voice was filled with authority. An official who had approached without us noticing swallowed nervously as he looked at us.

He glanced back at the hundreds of government troops standing behind him, puffed out his chest, and continued.

“I’ve heard from the people here that you came from Sichuan. Is that correct?”

“You people? Correct?”

Jeok Cheongang blinked and repeated the official’s words back at him.

“Are you addressing this old man?”

“That is correct.”

“That is correct?”

The official’s eyes wavered uneasily. But he quickly steeled himself and raised his voice.

“Ahem! Answer only what this official asks. State clearly where you came from and for what purpose!”

“Ahem? ‘Answer me’? ‘Why don’t you tell me’?”

“N-no, this old man…”

“This old man?”

*Don’t. Don’t do it. Please, just stop.*

They say women get butterflies when a handsome man repeats a question like that, but from the perspective of someone watching, it was nothing short of a horror movie.

I hurriedly stepped in before Jeok Cheongang could launch a Flame God Palm into the arrogant official’s chest.

“Why don’t you talk to me?”

“There’s nothing to discuss with a wet-behind-the-ears brat!”

“…”

I had just pulled him out of a tiger’s jaws, and this was how he talked to me?

I wanted to knock his head clean off, but I held back and continued.

“We did come from Sichuan, and we have business here.”

“Then what is this business?”

“Well…”

At that moment, someone shouted in a voice filled with excitement.

“Steamed fish topped with lots of minced chili peppers!”

“Cheongpung, you son of a bitch!”

“What? Benefactor, it really is delicious. It’s so good that if two people eat it and one of them dies, the other wouldn’t even notice…”

I didn’t know whether it was really so delicious that one person could die without the other noticing, but from the official’s expression, it was clear that we looked like people who ought to die.

His face flushed bright red as he bellowed,

“How dare you mock this official!”

“Wait, mister. That’s not what he meant…”

“It is suspicious enough that you came from Sichuan under the flag of the Yangtze River Channel League, and now you claim you came here to eat steamed fish? You’re the sort of people who won’t shed a tear until you see the coffin. Guards, arrest these men at once!”

“Yes, sir!”

What the hell was this development?

Before I could say another word, hundreds of government troops with military discipline drilled into them surrounded us with spears. Jin Wikyung clicked his tongue softly and stepped forward.

“You’re rather quick-tempered.”

Even by modern standards, Jin Wikyung was tall. In Murim, he was considered a giant.

The official swallowed hard as he looked at the Ural Mountains of his shoulders and the muscles bulging beneath his clothes.

“W-who are you?”

“I am Jin Wikyung of the Jin Family of Taiyuan in Shanxi. I won’t waste words, so why don’t you withdraw your men here?”

Before the official could answer, Jin Wikyung’s deep voice continued.

“It seems you haven’t been informed yet, but we are martial artists who received direct permission to pass from the City Lord of Sichuan Province.”

“The City Lord of Sichuan Province?”

“If you doubt me, you may verify it. But before that, it would be wise to withdraw your men. There is no reason to throw away perfectly good lives.”

The official flinched, and the spearpoints of the government troops surrounding us trembled as well.

They knew it too. No matter how hard they had trained or how elite they were, they couldn’t defeat us.

But that was how the world worked. The lower-ranked men shed the blood, while the higher-ranked men guarded their pride. I saw the official’s eyes harden.

“How dare you… Do you even know who this official is?”

Jin Wikyung didn’t change his expression as he opened his mouth.

“I do. You are naturally attached to the Hubei Provincial Administration Commission, which handles civil and financial affairs. Judging by your robes, you are a Judicial Inquirer of the secondary sixth rank. I do not know why someone responsible for legal matters has come all the way here to arrest innocent people, however.”

“…”

“Oh, by the way. Do you know a man surnamed Yi whose given name is Hongcheon?”

A trembling voice escaped between the official’s lips.

“T-that person is the Provincial Administration Commissioner who was newly appointed not long ago.”

“I see. I thought I had heard something about him. From Shanxi’s Assistant Administrator of the Six Ministries to Hubei’s Provincial Administration Commissioner. That is quite a promotion. It should be celebrated.”

“M-might I ask what your relationship is with the Provincial Administration Commissioner?”

Jin Wikyung smiled faintly. At some point, his posture and tone had naturally begun to look down on the official.

“I’ve met him a few times and shared a drink or two. I helped him out when he needed it.”

“Gasp!”

“What? Is there something else you’d like to hear?”

“N-no, sir!”

The official’s rigid back bent like a mollusk.

After quickly folding himself into a deep bow toward Jin Wikyung, he turned on his subordinates and roared,

“You fools! What are you doing? Put away those ugly blades at once!”

“Yes, sir!”

“Can you believe these idiots don’t even know how to handle a situation like this? Please forgive our rudeness!”

Jin Wikyung kindly patted the official on the shoulder.

“It’s all right. People make mistakes in life, like you did today.”

“This man Son can only be deeply grateful for your heart as vast as the sea!”

“Apologize to these men directly. Especially the man you spoke to first. He is a highly respected elder of Murim.”

“I-I had no idea. Then, might I ask his sobriquet…?”

“He is Great Hero Jeok Cheongang, the Fire King.”

“…”

“We came straight to Hubei after the Sichuan Blood History, traveling aboard a ship borrowed from the Yangtze River Channel League. Oh, of course, we didn’t come solely to eat steamed fish.”

*Stop it. You’re going to make him cry.*

The official kept looking back and forth between us with a face that seemed ready for suicide, bending at the waist five times a second.

Jin Wikyung then nudged me lightly in the ribs.

“What do you think, my youngest? Your big brother looks cool, doesn’t he?”

“…”

“You would have been cool if you’d stopped before that last line.”

“Once you establish a connection with the government, there are a lot of advantages. If you ever find yourself in a difficult situation, use my name.”

If he could say something like that with such confidence, he must have cultivated quite a few connections.

According to Gung Gibang, the Jin Family of Taiyuan’s meteoric rise over such a short period was virtually unprecedented.

If Jin Mukyung, who was undoubtedly continuing his grueling training at the Jin Family even now, was a genius of martial arts, then Jin Wikyung was an all-rounder who possessed everything a Family Head needed.

“My youngest, don’t you think I look cool? Hm?”

“…”

Yes. Apart from things like this, he was a perfect Family Head.

I was still trying to push away the increasingly clingy Jin Wikyung when it happened.

“Everyone, stand aside.”

At the sound of the deep voice infused with profound internal energy, the people who had been murmuring some distance away from the harbor split to either side.

At the same time, dozens of martial artists carrying considerable qi approached us with measured steps.

*That’s…*

I narrowed my eyes.

Written in cloud-like calligraphy across the pure-white silk martial robes they wore was:

**Zhuge Clan.**
## Chapter artifact 444

# Chapter 444

The Zhuge Clan.

It was a famous family that appeared at least once in every modern wuxia novel.

Not a single character with the surname Zhuge was ever stupid, and none of them were conspicuously strong, either.

They were supposedly one of Murim’s great families, yet martial arts seemed more like their minor than their major.

That made sense. The Zhuge Clan’s true strength came not from their bodies, but from their minds.

They were a family of wise men skilled in broad scholarship, strategy, and mechanisms and formations.

As a result, the world called them the Divine Mechanism Zhuge, and in Murim, they handled practically every role that required brains.

If the name of the Murim Alliance’s strategist in a novel you were reading didn’t begin with Zhuge, it could even feel unsettling.

Perhaps it was because that image of the Zhuge Clan had been so firmly lodged in my mind that I felt strange seeing these martial artists stride toward us without hesitation.

But unfamiliarity wasn’t the only emotion I felt.

Clack-clack-clack-clack!

The Zhuge Clan’s martial artists lined up on either side of the road like iron towers. A single person slowly walked between them.

The slender young man wearing robes so white they were almost blinding opened his mouth.

“Last night, the stars were unusually bright. It seems they were heralding the arrival of honored guests. I am the Zhuge Clan’s Lesser Family Head…”

I raised my hand high and shouted in delight.

“Galgyun!”

“Not ‘Galgyun’… I’m Zhuge Gyun.”

A heavy silence fell.

The Zhuge Clan’s martial artists, who still had no idea who I was, looked at me as if I were some kind of madman. Jeok Cheongang looked at me with a hint of confusion.

“You know this fellow?”

“Yes. I met him at the Star-Array Grand Banquet last time. But this is the first I’ve heard that he’s the Zhuge Clan’s Lesser Family Head.”

“Even someone like you has friends?”

“He’s not my friend. I just call them the Three Idiots…”

“Ahem! Ahem-ahem!”

One of the Three Idiots I had met at the Star-Array Grand Banquet—the Divine Marvel Dragon Zhuge Gyun—hurriedly cleared his throat and cut me off.

Before I could say anything, he turned toward Jeok Cheongang and offered his greetings.

“Zhuge Gyun, a newcomer to Murim, pays his respects to Senior.”

Jeok Cheongang looked Zhuge Gyun up and down before tossing out a question.

“What relation are you to Gonghu?”

“Pardon?”

“I mean the Fan-Wisdom King, Zhuge Gonghu. That bastard was the Murim Alliance’s chief strategist during the Great Faction War.”

I had heard both the title and name of the Fan-Wisdom King Zhuge Gonghu.

He had served as the mind of the Murim Alliance during the Great Faction War and was the foremost contributor to turning the grim tide of the war.

That was one reason he had been praised as one of the Ten Kings alongside the other Supreme Peak masters.

*What a way to refer to someone like that.*

I had gotten used to seeing Jeok Cheongang act this way, but to everyone else, it must have been a whole new world.

Jin Wikyung swallowed hard, while the Zhuge Clan’s martial artists stood there with their mouths hanging open, doubting their own ears.

Of course, our Fire King Jeok Cheongang didn’t care about any of that. Ramming straight into things with blazing force was practically the Fire Gate Clan’s trademark.

“Why aren’t you answering?”

His expression was unpleasant enough already, but when he actually frowned, he looked like a murderous demon.

Even Zhuge Gyun—a lunatic who was no slouch himself—was so flustered that he stammered.

“M-my great-grandfather.”

“Is that so? I thought you looked a little like him. You look like you’d have a good head on your shoulders. You also look like you have no manners.”

“…”

Now that was imposing.

Since Jeok Cheongang was a man from two generations ago who had lived well past a hundred, even the elders of most prestigious clans and sects couldn’t dare object when he called them, “Hey,” “you,” or “bastard.”

He could chew people up with martial arts and digest them with seniority—the Bodhidharma’s-skull-water story of Murim.[^1]

With the atmosphere growing increasingly awkward, I gave Jeok Cheongang a light poke in the side.

“Come on. That’s enough.”

“What? Can’t this old man say even that much?”

“Even so, he’s been dead for ten years…”

“What do these greenhorns know? If this old man had died, Zhuge Gonghu would have done the same. He and I have been calling each other bastard for years.”

“…”

“…”

Not brotherly terms. Bastardly terms.

While everyone flinched once again at his innovative choice of words, Jin Wikyung was the first to recover and address Zhuge Gyun.

“Thank you for the Zhuge Clan’s hospitality.”

A true professional was a true professional. At the Star-Array Grand Banquet, Zhuge Gyun had seemed like a man with a screw loose, but as the Lesser Family Head of his clan, he responded appropriately.

“Think nothing of it. I hope your journey here was not too uncomfortable.”

“If a person is comfortable in both body and mind, how can he call himself a martial artist—”

“It was damn uncomfortable. How dare you make this old man come all the way here? I’ll hear the reason, and if it’s nothing important, then a Flame Divine Palm will…”

“Oh, seriously! I said that’s enough!”

“You dare grab this old man’s sleeve! Let go, you all-brawn bastard!”

While I tried to restrain Jeok Cheongang, who had flown off the handle, Jin Wikyung hurriedly continued.

“I know this is rude, but let’s put the pointless conversation aside and hurry. Please, let’s hurry.”

“A wise decision. Zhuge Wuhou, who laid the foundations of our family, would have smacked his feather fan and agreed.”

The government troops and Zhuge Clan martial artists were the first to clear a path at the dramatic show of unity between the two Lesser Family Heads. The river bandits from the Water Dragon Stronghold who had joined our party followed behind them.

As we moved, I felt countless wary gazes and heard people whispering as they watched us.

*What the hell is going on?*

Was this why Jin Wikyung had said we needed to pass through Hubei?

My question didn’t last long. The moment we climbed into the carriage, Mungyeong quietly opened his mouth.

“It seems we are one person short.”

“What?”

I looked around and only then noticed that someone was missing.

“Wait. Where did he go?”

“Here, Benefactor!”

“…”

When the hell had that bastard gotten over there?

Cheongpung was standing in front of a street stall that had not yet been folded, stuffing himself with freshly steamed fish. He raised one hand high and shouted.

“I’ll finish eating and come!”

“Stop talking bullshit and get your ass over here!”

Please.

Just for one day, let’s live like human beings. Like human beings.

With my heart in tatters, the carriage began to move.

Even after it raced down the well-kept road and disappeared from sight, people’s eyes continued to follow us like shadows.

* * *

Unlike Emei, Qingcheng, and the Tang Clan—the prestigious great powers of Sichuan Province—which had established their bases on mountains or in remote areas, the Zhuge Clan occupied the center of a major thoroughfare.

Just the people passing outside the carriage window numbered well over several hundred.

Their faces were darkened by the sun, and whenever they spotted the carriage bearing the Zhuge Clan’s emblem, they bowed their heads.

“Why are there so many people here?”

Zhuge Gyun, sitting across from me, answered my mutter.

“The Yangtze is practically Hubei’s lifeline. It makes the vast surrounding lands fertile, so people gather here. And because the harvest is plentiful every year, smiles never leave their faces.”

“Really? The people I saw at the ferry about one shichen ago looked like their smiles had left forever.”

“That…”

Zhuge Gyun closed his mouth, his expression suddenly serious in a way that didn’t suit him, and looked away.

“I’ll tell you after we reach the family compound.”

Something must have happened. At the Star-Array Grand Banquet, he had been an endless fountain of nonsense, so it was telling that he looked like this now.

Given the mood, I didn’t ask any further questions and turned my head toward the window.

*Something definitely feels wrong.*

And the more time passed, the stronger that feeling became.

The government troops, who were usually so lax, had their eyes wide open as they checked people’s hopae at various points, while martial artists in ordinary clothes hid among the commoners.[^2]

Their martial prowess, which I sensed only briefly as we passed, was far from low. Dark Heaven immediately came to mind, but Jeok Cheongang’s Sound Transmission a moment later cleared that up.

*—They’re Zhuge Clan people. For some reason, they’re hiding their identities and even moving covertly.*

*They’re doing this practically in their own front yard?*

I suddenly remembered what had happened a few days earlier and asked,

*—Old Master, did you hear anything?*

*—About what?*

*—You know. Last time, you left with my eldest brother for a while.*

*—I did.*

*—Didn’t you hear why we had to come to Hubei then? Something about Wudang or the Zhuge Clan?*

Jeok Cheongang’s brow furrowed slightly as he looked at me.

*—What good would it do this old man to hear that?*

*—Pardon?*

*—If we’re going, we’re going. Why are you prying into every little thing? I was merely badgering him to get here as quickly as possible. I told him I’d sink every fast ship if he didn’t.*

*—…Ah. Right.*

I wasn’t sure whether to call that cool or fiery.

I shook my head and glanced at Mungyeong.

The boy had been chatting with Hyuk Mujin with a bright smile, showing no sign of irritation. But then one of his eyebrows lifted slightly.

A private Sound Transmission reached my ears.

*—What.*

*—…I haven’t even said anything yet.*

*—Don’t stare at me for no reason. If you want to see tomorrow morning’s sun.*

This was terrifying. Was I even supposed to breathe properly?

I sighed inwardly and turned my gaze toward the view beyond the carriage’s latticed window.

Mount Longzhong, also called Mount Fulong because the greatest strategist under heaven—a man who had shaped the history of an era—once lived there in seclusion.

And spread across a vast stretch of land, the Zhuge Clan finally came into view.

*They said this was Hubei Province’s wealthiest family.*

Their ancestor, Zhuge Kongming, had been famous for his frugality. But his descendants had not devoted their naturally sharp minds solely to scholarship and mechanisms and formations.

They had made full use of fertile land that produced plentiful harvests every year and the Yangtze’s waterways, which crossed the entirety of Hubei Province, to amass enormous wealth.

I began to grasp the extent of that wealth before we even passed through the Zhuge Clan’s main gate.

“Why aren’t we getting out? Haven’t we arrived?”

Zhuge Gyun answered with an expression that seemed to say he had no idea what I was talking about.

“Pardon? It would take a long time to walk from here to the Inner Hall. We still have seven more gates to pass through, so just sit back.”

“…Is it really that big?”

“This is the reduced version. Our family suffered considerable damage during the Great Faction War.”

“This is insane. You’re sweeping up gold and silver with a rake. Didn’t your ancestor leave some instruction to live frugally? Wasn’t he an incorruptible scholar or something?”

Zhuge Gyun answered in a solemn voice without changing his expression.

“Studying scholarship costs more than a few coins. Do you know how expensive books are? Besides, our family separately supports scholars as well.”

“…”

“You need a comfortable environment to pass the civil-service examinations and advance in martial arts. When you’re hungry, you can’t think about anything. You only become anxious.”

“Uh… right.”

It wasn’t what I had expected, but if I thought about it carefully, every one of his points made sense.

After patiently explaining the importance of capital, Zhuge Gyun concluded his speech by saying that even his ancestor, Zhuge Wuhou, had been born with a silver spoon in his mouth.

By then, the carriage had passed through a total of eight gates and was entering the Inner Hall.

“Now, please get down and follow me. The Family Head is waiting.”

“The Family Head would be…”

“My father.”

I had heard about him from Jeok Cheongang.

During the Great Faction War, Zhuge Gonghu had lost his only son. In accordance with the principle of eldest-son succession, he had given his young grandson the position of Lesser Family Head.

That young grandson was Zhuge Feng, the Crouching Dragon Guest—the current Family Head of the Zhuge Clan and Zhuge Gyun’s father.

“Family Head, I’ve brought the honored guests.”

At Zhuge Gyun’s serious voice, now completely devoid of humor, the firmly closed doors slowly opened.

[^1]: This refers to a Korean Buddhist anecdote in which a monk drinks water from a skull in the dark and finds it sweet, only to recoil after seeing the skull in daylight. The phrase is used for the way perception changes once one understands the truth.

[^2]: A *hopae* was a personal identification tablet used in premodern Korea and China.

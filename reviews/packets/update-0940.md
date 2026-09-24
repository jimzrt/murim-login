<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0940.txt",
      "sha256": "26d4e3a5e0d0fbf5394675c2d78ed552c5e4cedb1d9d63a7be0dd8f3c1a3d3c2",
      "bytes": 13168
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "b0153d33d3128cc6adb79367bf4f0ab29106283e317fcbeb14dae6f3edc15b0b",
      "bytes": 2707
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "c83d671253dcc6207dec6e7e72f91d57c7a1f177dfbc45158e25b99121e8e54c",
      "bytes": 232276
    },
    {
      "path": "characters/Baek Yeon.md",
      "sha256": "f8bd92b92df2e92d6941df63a7d744c0b62fb3612eabd30af42bcf8c6caaa880",
      "bytes": 951
    },
    {
      "path": "characters/Cang Gong.md",
      "sha256": "ae96c9c2c792edb6056d7d7f7c693e3a0ebace40e34a8ece4fedb5012065a266",
      "bytes": 778
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "a8c6c4489369627d3c801af833782327c0a29fface2867cf526b616b8213d7ec",
      "bytes": 759
    },
    {
      "path": "characters/Eastern Heaven Demon Lord.md",
      "sha256": "0634132c8318a3bcb24da4822c0ac09c21e9cb0bfc7dc18cd557990d7d3bfa8c",
      "bytes": 838
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "67823a3287de87843ea9926de027ec4dc333ef68658de0fa154ea9e5dcd8c394",
      "bytes": 1445
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "31c15482ec6dd79649dd369292cbebf3f170d6a693db7233c8b01154d2d80dc5",
      "bytes": 1204
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "635117bbf0523b5a8c2c643717ac35b74e453c288e63b7802107f0d3e2a84114",
      "bytes": 1343
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "890a299bf3d7038b552ead4ac2f137a08a8237fe7465d69544aa2ef238632e3b",
      "bytes": 622
    },
    {
      "path": "characters/Peng Cheolhu.md",
      "sha256": "73bf67703ef58d84bcb41b1cb631097dcb4282ac2d082ce6e5b24ccc9ebbe2e8",
      "bytes": 680
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "0e2d532f2af4d7be69c6e65c1cef25321d7cf2235ebf140c6de94d6147d63060",
      "bytes": 266948
    }
  ],
  "estimated_tokens": 12942
}
-->

# Durable State Update — Chapter 940

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

For each matched character, check whether this chapter adds clear, durable
evidence that improves Role, Personality, Voice, or Relationships. Update a
field when it corrects or meaningfully sharpens the existing profile; otherwise
leave it unchanged. Voice guidance should capture observable register, cadence,
word choice, or address habits that help distinguish the character in English.
Do not infer a stable voice from one situational line or generic personality
adjectives. Keep “Not established” only when this chapter provides no reliable
voice evidence; never replace it with unsupported specificity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 940. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 940. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history. For a new profile, describe voice only when the chapter supports
a useful, stable distinction; otherwise say “Not established”.
`names` contains only newly required Korean-to-English rows that are absent from
Exact glossary matches; Korean keys must occur in the source. Do not repeat
glossary matches. The controller drops rows already in the names ledger.
`address_pairs` contains only newly required speaker→addressee rows that
are absent from Matched address pairs. Speaker and addressee must be Hangul source
spellings such as 진태경 or 혁무진, never English names. Arabic digits are
allowed in titles such as 1팀장. At least one endpoint must occur in the source.
Before returning JSON, verify every `speaker` and `addressee` value contains at
least one Hangul character; use the Korean source spelling even when the same
person's English name appears in the reading copy. If no valid new pair exists,
return `"address_pairs": []`.
The controller drops pairs already in the address ledger. Do not invent
risk-register rows. Beat plot paragraphs are plain strings; continuity and
translation decisions are concise list items.
Return this exact shape:

{
  "chapter": 940,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 940,
    "continuity_sources": [940],
    "active_continuity": ["active fact"],
    "open_questions": ["unresolved question"],
    "temporary_decisions": ["temporary translation decision"]
  },
  "names": [
    {"korean": "source spelling", "english": "English rendering", "notes": "brief note"}
  ],
  "address_pairs": [
    {
      "speaker": "진태경",
      "addressee": "문경",
      "kinship": "kinship or role relation",
      "normal_address": "established English address",
      "speech_level": "speech level",
      "notes": "brief note"
    }
  ],
  "profile_updates": [
    {
      "path": "characters/Listed Profile.md",
      "current": "- **Role:** exact current full line",
      "replacement": "- **Role:** finished replacement full line"
    }
  ],
  "profile_creations": [
    {
      "filename": "English Name.md",
      "korean": "source name",
      "english": "English Name",
      "aliases": [],
      "role": "stable role",
      "personality": "stable traits",
      "voice": "stable voice",
      "relationships": "stable relationships"
    }
  ]
}

Use empty arrays when no name, address-pair, or profile change is required.
`profile_creations` is only for characters with no existing `characters/` file.
If the person already appears under Listed compact profiles, use `profile_updates`.

## Prior durable context

```json
{
  "active_continuity": [
    "The Emperor was poisoned with Blood Soul Gu after the coup; it has reached his marrow, and the Divine Physician says his vitality is at its limit and cannot guarantee he will survive another couple of months.",
    "Taekyung’s System quest requires him to remove the Blood Soul Gu from the Emperor’s head and successfully treat him; its reward and failure consequence are unknown.",
    "The Emperor prepared for his death by transferring loyal retainers and his power base to Zhu Bao, and avoids meeting his younger brother to spare him the grief of an impending farewell.",
    "The Emperor has publicly exposed Dark Heaven and declared his intent to crush it; war against Dark Heaven has begun.",
    "Ma Sanbao escaped and evaded the Imperial Army’s three-day search.",
    "Taekyung found and opened the Eastern Heaven Demon Lord’s hidden iron chest; it contains old bamboo slips, recent papers, and a small silk pouch of unknown significance.",
    "The System update reward is a durable pocket watch that appears broken and bears the faint inscription “A broken clock is right twice a day.”",
    "The Bow Saint says the Martial God chose her; she tested Taekyung in the banquet-hall battle to confirm he was the chosen one and assess his power and character.",
    "The Bow Saint remembers the dead and counts casualties after every battle; she says 1,319 orthodox fighters died at Mount Small Hua and 2,562 allies died in the banquet hall.",
    "Jeok Cheongang considers Taekyung his one and only Disciple and is furious that the Bow Saint put him in danger.",
    "A missive found among the Eastern Heaven Demon Lord’s belongings warns that Dark Heaven’s main force will cross the northern grasslands and invade Shanxi before the Double Ninth Festival, about half a month away; the sender is unknown and the warning is not yet confirmed."
  ],
  "continuity_sources": [
    938,
    939
  ],
  "open_questions": [
    "What is the Martial God’s identity, and what is the full nature of his connection to the chosen one and the Bow Saint?",
    "How far has Dark Heaven infiltrated the Great Nation, and which officials or commanders are involved?",
    "Where is Ma Sanbao, and what is his current status?",
    "Who sent the Shanxi Annihilation Plan missive, and will Dark Heaven’s invasion proceed as described?",
    "What do the papers, bamboo slips, and silk pouch from the Eastern Heaven Demon Lord’s chest contain, and what is their significance?"
  ],
  "safe_through": 939,
  "temporary_decisions": [
    "Taekyung intends to keep the pocket watch for half a month before deciding whether to give it to Mujin."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 궁성     | **Bow Saint**                 | —              |
| 벽력도왕   | **Thunderbolt Saber King**    | Peng Cheolhu   |
| 십왕     | **Ten Kings**       |
| 무림맹    | **Murim Alliance**               |
| 암천     | **Dark Heaven**                  |
| 하북팽가   | **Hebei Peng Family**            |
| 무인     | **martial artist**                               | Default term                                          |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 운기조식   | **circulate one's qi**                           | Usually better as a verb than a proper-name technique |
| 정파     | **orthodox faction**                             |                                                       |
| 마교     | **Demonic Cult**                                 |                                                       |
| 중원     | **Central Plains**                               |                                                       |
| 전각     | **pavilion**                                 | Use “hall” only when established for a specific named building |
| 산서     | **Shanxi**             |
| 정마대전   | **Great Faction War**         |
| 백연 | **Baek Yeon** | Commander of the Embroidered Uniform Guard. |
| 창공 | **Cang Gong** | The bedridden East Depot leader for whom Ma Sanbao acts. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 동천마군 | **Eastern Heaven Demon Lord** | Title of the absurd masked antagonist in Jin's nightmare. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 전서응 | **messenger eagle** | Emergency courier used by the Lower District Sect. |
| 오대세가 | **Five Great Families** | Major Murim grouping. |
| 천자 | **Son of Heaven** | Honorific title for the Emperor. |
| 하북 | **Hebei** | Province where Hyuk Family Textile Shop has a branch. |
| 선황 | **the late Emperor** | The former Emperor whom Hong Jin served. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 게르 | **ger** | Traditional nomadic dwelling contrasted with Central Plains wooden buildings. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 일각 | **fifteen minutes** | Quarter of a shichen; used for the remaining completion time. |
| 절강성 | **Zhejiang Province** | Province where the Geumwa Merchant Group ranks among the top three merchant groups. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 오대 | **Five Squads** | Named Tang Clan organizational group in Tang Sadok's mobilization order. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 절강 | **Zhejiang** | Region from which the boat travels east. |
| 이전 | **Two Halls** | Top-level Murim Alliance organizational grouping. |
| 전서 | **missive** | A written message exchanged or delivered in secret. |
| 파리 | **Paris** | The city containing Ares Guild's branch attacked at the chapter's end. |
| 금의위 | **Embroidered Uniform Guard** | Imperial guard force mentioned by Hong Jin. |
| 태조 | **Taizu** | The Great Nation’s founding emperor. |
| 금위군 | **Imperial Guards** | Imperial force distinct from the Embroidered Uniform Guard. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 혁무진 | 적천강 | subordinate_to_overwhelming_elder | Great Hero Jeok | deferential and fearful | Mujin uses 적 대협 while reporting Jeok’s orders and Taekyung’s awakening. |
| 적천강 | 혁무진 | overwhelming_elder_to_junior_martial_artist | you stupid fool | blunt and mocking | Jeok calls Mujin a 멍청한 놈 after knocking him down during the attempted escape. |
| 시비 | 진태경 | household_servant_to_visiting_young_hero | Young Hero Jin | formal-polite | The maid summons Taekyung to meet the Family Head. |
| 적천강 | 벽력도왕 | rival_martial_master_to_rival_martial_master | Virility Saber King | insulting and taunting | Jeok coins 정력도왕 as a taunting replacement for the established title. |
| 벽력도왕 | 적천강 | rival_martial_master_to_rival_martial_master | Jeok Cheongang | boisterous and hostile-teasing | The Thunderbolt Saber King calls Jeok by name before their argument escalates. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 벽력도왕 | 진태경 | elder martial master to younger rival | you | boisterous and confrontational | Peng addresses Taekyung as 네놈 while discussing Peng Dojin. |
| 진태경 | 백연 | young martial artist confronting an imperial military commander | you | casual and insulting | Refers to Baek as 이 양반 while challenging his conduct. |
| 백연 | 천자 | imperial officer addressing the Emperor | Your Majesty | formal, deferential in address but openly defiant in private counsel | Baek uses formal honorifics while sharply confronting the Emperor over their shared undertaking. |
| 천자 | 백연 | Emperor addressing his military commander | Baek Yeon | familiar and authoritative | The Emperor addresses Baek by name and gives him a direct warning. |
| 진태경 | 황제 | guest of the Emperor’s younger brother addressing the Emperor | Your Majesty | formal and deferential in address, despite blunt challenges | Taekyung repeatedly addresses the Emperor as 폐하. |
| 백연 | 진태경 | imperial commander confronting a young martial artist | Jin Taekyung | measured and familiar, using 자네 | Baek Yeon cautions Taekyung about his words and asks whether he must cause a scene. |
| 황제 | 진태경 | Emperor addressing a subject and Prince Shangshan’s guest | Jin Taekyung | formal and authoritative | The Emperor addresses Taekyung by his family and personal name before asking what to do with the two officials. |
| 적천강 | 창공 | hostile opponents | you; you bastard | blunt and threatening | Jeok Cheongang uses 네놈, 이 불알 없는 놈, and 호로새끼 while taunting Cang Gong. |
| 창공 | 적천강 | hostile opponents | Fire King Jeok Cheongang | taunting and sardonic | Cang Gong names Jeok by his title, then comments on how alike master and disciple are. |
| 적천강 | 동천마군 | enemies | you | blunt and informal | Jeok Cheongang addresses the Eastern Heaven Demon Lord with hostile familiarity. |
| 동천마군 | 적천강 | enemies | you | informal | The Eastern Heaven Demon Lord speaks to Jeok Cheongang during their duel. |
| 황제 | 동천마군 | former ruler addressing a former subject, now an enemy | you | measured and formal | The Emperor asks why the Demon Lord betrayed his father, the late Emperor. |
| 동천마군 | 황제 | former subject addressing the Emperor, now an enemy | you; you bastards | hostile and contemptuous | He denies ever being loyal to the imperial family and accuses the rulers of betrayal. |
| 진태경 | 동천마군 | young martial artist confronting an enemy | ugly-ass big bro | casual, profane, and taunting | Jin calls out to the Demon Lord after returning to the hall. |
| 동천마군 | 진태경 | enemy recognizing the spear wielder | Jin Taekyung | shouted, informal | The Demon Lord cries Taekyung's name after identifying him as the spear's owner. |
| 황제 | 백연 | Emperor to the imperial court’s foremost military commander and trusted comrade | Baek Yeon | Direct and familiar; framed as a request rather than an order | The Emperor asks Baek Yeon to sound the war drum. |
| 궁성 | 진태경 | elder who spent decades searching for the chosen one | you | casual and teasing | Uses 너/널 while testing and praising Taekyung. |
| 진태경 | 궁성 | chosen one addressing the elder who sought him | you | polite, shifting to familiar-casual under stress | Begins with formal-polite phrasing, then speaks more casually as the conversation intensifies. |
| 적천강 | 궁성 | old acquaintance and fellow martial master | you; nasty old hag | blunt and familiar | Uses a contemptuous insult while expressing concern for his Disciple. |
| 궁성 | 적천강 | old acquaintance and fellow martial master | you | familiar and lightly teasing | Speaks with dry familiarity about his unchanged, impulsive nature. |

## Listed compact profiles

### Baek Yeon.md

# Baek Yeon (백연)

- **Safe through:** Chapter 935
- **Aliases:** Blood Envoy
- **Role:** Baek Yeon is the Commander of the Embroidered Uniform Guard, a martial arts instructor to the Emperor, and the Blood Envoy who helped the fourth prince seize the throne and led the purge.
- **Personality:** Politically assured and controlled, Baek Yeon is fiercely loyal to the Emperor and deeply admires the burdens he has borne, while showing warmth and concern beneath his stern manner.
- **Voice:** Baek Yeon speaks with measured formality in public, but with the Emperor he shifts easily into familiar teasing and earnest, eloquent praise.
- **Relationships:** Baek Yeon is the Emperor’s trusted confidant and former martial arts instructor, and he is entrusted with protecting Zhu Bao; he commands the Embroidered Uniform Guard and treats Taekyung as a dangerous potential obstacle.

### Cang Gong.md

# Cang Gong (창공)

- **Safe through:** Chapter 939
- **Aliases:** None
- **Role:** Cang Gong is the Eastern Heaven Demon Lord’s assumed identity, through which he became the East Depot’s Brush-Holding Eunuch and a power second only to the Emperor.
- **Personality:** Calculating and self-assured, he is driven by vengeance and believes the rulers and the world betrayed him first.
- **Voice:** Dry and sardonic, he delivers taunts and judgments in measured statements.
- **Relationships:** He was raised by a master and fellow disciples in the Maoshan Sect, whose members died resisting the forced relocation of the capital; Ma Sanbao is his disciple, and he regards Jin Taekyung as a potential recruit.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 939
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Eastern Heaven Demon Lord.md

# Eastern Heaven Demon Lord (동천마군)

- **Safe through:** Chapter 939
- **Aliases:** Wei Zhong
- **Role:** The Eastern Heaven Demon Lord was Wei Zhong, the East Depot’s Seal-Holding Eunuch and a former Maoshan Sect disciple who commanded the dead with a bell; Jin Taekyung killed him with blue-white flames.
- **Personality:** His hatred grew from losing his family and sect, but recognizing his own lonely childhood in Zhu Bao ultimately moved him to relinquish his vengeance and choose a less harmful final act.
- **Voice:** He speaks in measured, almost lyrical phrasing, recounting the past before turning to pointed accusations.
- **Relationships:** Ma Sanbao is his Disciple; he holds the Emperor responsible for Taizu’s actions against the Maoshan Sect.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 939
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and an active member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented; despite being naturally fearful, he faces danger and remains loyal to the person he serves, with irreverent self-deprecation and a taste for glory. He is suspicious of Taekyung, bluntly critical of the family's disgraced third son, and an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; with Taekyung, blunt and occasionally incredulous, while using breezy, irreverent banter to defuse tense situations.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad; he regards Taekyung as the person who has repeatedly saved him and now believes he may be able to save Taekyung in turn. As a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Fire Dragon Pavilion members accompanying Taekyung. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 939
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; believes there is no absolute justice and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and says they have shared everything since he accepted him; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and remains Peng Cheolhu's rival.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 939
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader.
- **Personality:** Hungry, self-aware, dryly observant, and pragmatic under pressure; accepts extreme personal risk when duty and the lives of others demand it.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; So Gyo says he is the chosen one spoken of by the Martial God, while the Bow Saint sought him for decades and relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 939
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Peng Cheolhu.md

# Peng Cheolhu (벽력도왕)

- **Safe through:** Chapter 938
- **Aliases:** Thunderbolt Saber King
- **Role:** Peng Cheolhu is the Thunderbolt Saber King, a Ten Kings master and Great Hero of the Hebei Peng Family.
- **Personality:** Boisterous, hot-tempered, argumentative, and protective toward those connected to his close friend Hong Dao.
- **Voice:** Loud, blunt, confrontational, and prone to disguising embarrassment or retreat as serious martial instruction.
- **Relationships:** Long-standing rival and friend of Jeok Cheongang; close friend of Hong Dao; protective toward Hong Dao's Disciple Unnamed.

## Korean source

```text
＃940화



모래 먼지를 머금은 서늘한 밤바람에 초원의 게르가 몸을 떨던 그때, 만 리 밖에 세워진 거대한 성벽 뒤의 사람들은 아침을 맞이하고 있었다.

태양이 떠오르기까지는 아직 한참이나 이른, 사방을 에워싼 캄캄한 어둠 속에서.

두두두두!

깊은 밤을 깨우는 거친 말발굽 소리.

무려 백여 기에 이르는 전령(傳令)들은 그 어떤 절차도 없이 일곱 개의 문을 빠져나갔고, 앞서 날려 보낸 수십여 마리의 전서응(傳書鷹)이 그러했듯 제각각의 목적지를 향해 바람처럼 사라졌다.

그리고 이 모든 명령을 내린 한 사람은, 파리한 안색으로 속속들이 도착하는 보고를 듣고 있었다.

“모든 전령들이 지금 막 칠문(七門)을 통과했습니다!”

“육부(六部)에 속한 중신들에게 지엄하신 황명을 하달했나이다!”

“도찰원(都察院)이 폐하의 명을 기다립니다!”

“한림원(翰林院)과 통정사(通政司)의 신료들이 칙령을 준비 중입니다!”

“오호도독부(五虎都督部)에서 보고드립니다! 폐하의 명을 받들어 즉각 군함 삼백 척을 비롯한 수군 십만과 금위군을…….”

“그만.”

불현듯 흘러나온 황제의 한 마디에, 주위의 모든 소음이 씻은 듯이 사라졌다.

천자의 권위는 절대적이다.

비록 이제 고작 삼대(三代)에 접어든 대국의 역사였으나, 작금의 황제가 지닌 힘은 천하를 통일한 태조에 버금가거나 그 이상이라 할 수 있었다.

“소란스럽구나.”

황제의 낮은 뇌까림에, 모두가 숨조차 제대로 쉬지 못하고 엎드려 부복했다.

“황공하옵니다, 폐하!”

“죽여 주시옵소서!”

스륵.

작게 고개를 내저은 황제는 말없이 길게 늘어진 옷소매를 펄럭였다.

무언의 명령을 읽어 낸 이들이 조심스러운 몸짓으로 뒷걸음쳐 사라지자, 드넓은 대전(大殿)에는 어느새 단 두 사람만이 남아 있었다.

“무슨 말만 하면 죽여 달라고 난리로군. 일각만 더 저런 소리를 들었다면 짐이 스스로 혀를 깨물었을지도 몰라.”

씁쓸하게 웃는 황제의 모습에, 금의위 지휘사 백연이 굳은 얼굴로 입을 열었다.

“아무리 농담이라도 그런 말씀은 마십시오.”

“어차피 농담인데 뭐 어떤가. 더군다나…….”

황제는 비스듬히 옥좌에 몸을 기대며 말을 이었다.

“이런 상황에서 죽을 생각은 추호도 없어.”

여전히 창백한 안색이었으나, 새로운 위기에 직면한 그의 안광은 야광주처럼 번뜩이고 있었다.

“충분히 예상은 했지만…… 생각했던 것 이상이로군. 이리도 발 빠르게 움직일 줄이야.”

백연은 황제의 말에 십분 동의했다.

암천(暗天).

이름부터가 불길하기 짝이 없는 저 반역도당의 무리는 생각 이상으로 거대했고, 또한 치밀함마저 갖추고 있었다.

과거 그가 선황을 모시던 시절, 머나먼 서쪽 땅으로부터 들불처럼 일어난 어느 종교 세력보다도 더.

“오십여 년 전이었습니다. 마교(魔敎)라 불리는 자들이 중원으로 향한 것이.”

“정마대전(正魔大戰).”

혼잣말처럼 중얼거린 황제는 희끗희끗한 턱수염을 쓰다듬었다.

비록 그가 태어나기도 훨씬 전의 일이었지만, 물경 십만에 달하는 사이비(似而非)들이 중원 땅에 발을 디뎠다는 것은 모르는 이가 없을 만큼 엄청난 사건이었다.

그들이 단지 듣기 좋은 말에 홀린 촌무지렁이들이 아니라, 굳건한 신앙심과 창칼로 무장한 군대였다는 점에서 더더욱.

“마교의 기세가 하늘을 찌르자, 정파에 속한 무림인들이 선황 폐하께 주청을 드렸습니다. 저들은 대국의 질서를 어지럽히는 외적(外敵)이니, 황군을 일으켜 토벌을 명해 달라는 청이었지요.”

“짐도 알고 있네.”

황제가 백연을 응시하며 덧붙였다.

“참전에 가장 크게 반대한 이가 바로 백연, 자네라는 것도.”

백연은 작게 고개를 끄덕여 수긍했다.

그건 틀림없는 사실이었다.

바로 이 자리에서 조정의 중신들을 며칠간 치열한 갑론을박을 주고받았고, 토벌령을 진지하게 고심하던 선황은 이전에 보인 적 없던 백연의 간곡한 모습에 뜻을 접어야만 했다.

“소장이 왜 그토록 반대했는지, 폐하께서는 짐작하시는 바가 있으십니까?”

“크게 두 가지 이유라고 생각하네. 그중 첫 번째는 마교가 대국의 힘을 두려워하여 백성들을 해치지 않았기 때문이고, 두 번째는……. 창공(廠公), 그자 때문이었겠지.”

“맞습니다. 저와 달리 창공은 누구보다 앞장서서 외적을 물리치자고 주장했습니다.”

“옳은 선택이었네. 그때 아바마마께서 창공의 손을 들어 주었다면, 대국 또한 적지 않은 피를 흘려야 했을 테니.”

“황실의 힘을 약화하려는 의도가 분명했습니다. 그렇기에 더욱 반대할 수밖에 없었지요.”

고금의 역사를 통틀어도 상처 없는 승리는 없다.

한 사람의 무인이기 이전에 일군을 이끄는 장수였던 백연은 그 사실을 알고 있었고, 온 힘을 다해 대국의 참전을 막았다.

창공. 아니, 동천마군은 그 무렵부터 이미 요주의 인물이었으니까.

물론 그의 반대로 인하여 수많은 정파 무림인들이 희생되었지만, 백연은 조금도 후회하지 않았다.

그는 황제와 대국을, 더불어 백성을 위한 선택을 한 것뿐이었다.

무림맹과 마교라는 두 바위가 서로를 향해 맹렬하게 부딪치는 것을 지켜보다가 개입해도 늦지 않았다.

그리고 그 기다림의 결과는, 공멸(共滅)에 가까운 정파의 승리였다.

“그때, 소장은 차라리 마교가 승리하길 바랐습니다.”

백연의 말을 들은 황제가 혀를 찼다.

“자네, 오늘따라 지나치게 솔직하군.”

“어쩔 수 없는 사실입니다. 정파에 속한 무림인 중 상당수는 백성들의 신망을 얻고 있어 토벌할 명분이 없지만, 살아남은 것이 마교라면 이야기가 다르지요.”

커다란 바위는 옮기기조차 버겁다.

하지만 수없이 깨지고 부딪친 끝에 남은 돌멩이라면.

그리고 그 돌멩이가 백성들에게 해를 끼칠 만큼 뾰족하다면, 백연은 한 치의 망설임도 없이 망치를 들어 그것을 부쉈을 것이다.

무림(武林)이라는 무법자들의 울타리를 완전히 허물어트렸을 것이다.

“그러나, 만약 자네 말대로 되었다면 오늘날에 이르지도 못했겠지.”

황제의 나직한 목소리가 넓은 대전을 울렸다.

맞다. 참으로 모순되는 말이지만, 바로 그 무림인들의 도움으로 역적들을 처단하고 대업을 완수할 수 있었다.

그리고…… 이제는 그 모순을 바로잡을 때였다.

“온 힘을 다해 도울 생각일세. 그들을, 아니 우리 모두를 위해서.”

쿵.

백연은 한쪽 무릎을 꿇으며 고개를 숙였다.

곧 정마대전 때와는 비교도 안 되는 혈풍(血風)이 몰아칠 것이다.

암천은 마교보다 강력하고, 비교도 안 될 정도로 위험한 존재였다.

단순히 무림에만 국한되지 않은, 천하(天下)를 뒤엎을 전란이 시작되고 있었다.

“천하의 지배자이신 황제 폐하께 감히 아뢰옵건대, 신에게 명을 내려 주소서.”

깊은 밤 진태경으로부터 전달받은 정보는 뜻하지 않은 불행이었으나, 대업을 완수하기 위해 철저한 준비를 끝마쳐 두었던 것은 불행 중 다행이다.

수백 척의 함대와 수천의 장수.

그리고 황실의 깃발을 휘날리는 수십 만의 대군이 명령을 기다리고 있었으니.

“금의위 지휘사 백연에게 명한다.”

준엄한 음성과 함께, 황제는 천천히 병든 몸을 일으켜 세웠다.

황금빛 수실로 용을 아로새긴 새하얀 침의(寢衣)가 아닌, 육중한 갑옷을 걸친 그는 거침없는 발걸음으로 대전을 가로질렀다.

철컥, 철컥.

한 걸음. 또 한 걸음.

옥좌를 내려온 황제가 백연을 손수 일으켜 세우며 입을 열었다.

“짐의 친정(親征)을, 전군에 알려라.”

“……!”

동요를 감추지 못한 백연의 눈동자가 일순간 파르르 떨렸다.

황제의 친정이 가진 파급력 때문만이 아니다. 살날이 얼마 남지 않은 황제의 각오가 느껴졌기 때문이었다.

“폐하.”

그러나 백연이 간신히 쥐어짜 낸 목소리는 끝끝내 이어지지 못했다.

말없이 고개를 가로젓는 황제의 모습을 본 충신은, 그저 먹먹한 심정이 되어 이를 악물 수밖에 없었으니.

“신, 금의위 지휘사 백연……지엄하신 황명을 받들겠나이다.”

대답 대신 희미하게 웃은 황제는 백연을 지나쳐 나아갔다.

활짝 열려 있는 철문 밖으로 보이는 세상은, 아직도 캄캄한 어둠에 휩싸여 있었다.

마치 얼마 남지 않은 자신의 미래처럼.

‘그래도, 이 또한 나쁘지 않군.’

비록 몸뚱어리는 죽어가고 있으나, 정신은 그 어느 때보다 맑았다.

처음이자 마지막이 될 친정.

침대가 아닌 전장에서 죽음을 맞이하는 것은, 비극이 아닌 축복이 될 것이다.

누군가에 의해 잠시나마 삶의 의지를 되살릴 수 있었던 것 또한.

“가세, 백연.”

황제는 죽어 가는 이라고는 믿을 수 없을 만큼 환하게 웃으며 말을 이었다.

“짐에게 한 약속을 지키지 못하고 먼저 떠나는, 어느 무엄한 무뢰배를 배웅해 줘야 하지 않겠나.”



* * *



한 시진.

그것이 동천마군이 남긴 철궤(鐵櫃)를 처음 손에 넣은 순간부터 지금에 이르기까지 걸린 시간이었다.

“모든 준비가 끝났습니다.”

귓가로 흘러들어온 혁무진의 보고에 나는 지그시 감고 있던 눈을 떴다.

평소와는 달리 깊게 가라앉은 녀석의 눈빛과 표정이, 지금의 상황이 얼마나 급박하게 흘러가는지 설명하는 듯했다.

“가자.”

그 외에 더 이상 무슨 말이 필요할까.

짤막한 대답과 함께 전각 밖으로 나선 나는 무언가에 홀린 듯이 움직였다.

이미 한 차례 운기조식을 했음에도 머릿속은 어지럽기만 했다.

‘보름.’

고작 보름.

그것이 중양절(重陽節)까지 남은 시간이었다. 아니, 어쩌면 그보다도 짧을 수도 있다.

동천마군이 보관하고 있던 전서에는, 암천의 본대가 북부 초원을 통해 산서성을 침공하는 시점은 중양절 이전이라고 적혀 있었으니까.

‘어쩌면 열흘. 아니, 당장 내일일지도 모른다.’

나는 흘러나오려는 신음을 애써 삼켰다.

급박한 것을 넘어 위급하다.

이곳, 황도가 위치한 절강성에서 산서성까지의 거리는 무려 만 리.

제아무리 황실의 전서응이 빠르게 움직이더라도 최소 열흘은 걸릴 수밖에 없는 거리다.

‘과연 내가 늦지 않게 도착할 수 있을까.’

모두와 함께 황궁을 나서면서도 마음속의 의구심은 무겁게 가슴을 짓눌렀다.

그런 내 모습을 줄곧 물끄러미 바라보던 적천강이 문득 입을 열기 전까지는.

“한 오십 년쯤 됐나? 벽력도왕(霹靂刀王) 그놈과 사소한 시비가 붙어 크게 한판 싸웠던 적이 있었지.”

마치 혼잣말이라도 하듯, 내 시선을 슬쩍 피한 적천강이 말을 이었다.

“평소에는 한참 아래로 보던 놈이라 무시하는 마음이 없지 않았는데, 막상 손을 섞어 보니 상당히 강하더군. 내색은 안 했지만, 상당히 놀라웠다.”

말고삐를 쥔 채 묵묵하게 나아가던 궁성이 말을 받았다.

“그는 강한 사람이에요. 아마 당신이 아니었다면 십왕(十王) 중에서도 으뜸이었겠지요.”

“음. 역시 그랬겠지?”

고개를 주억거린 적천강이 나를 힐끔 바라보며 덧붙였다.

“하긴, 하북팽가가 괜히 오대세가겠나. 그만한 저력이면 어떤 놈들과 붙어도 충분히 이길 수 있지. 하북은 물론 산서 쪽 상황도 훤히 들여다볼 만큼의 정보력도 있고.”

그제야 문득 알 것 같았다.

이 뜬금없는 대화가, 전부 나를 안심시켜 주기 위한 것이라는 사실을.

‘허.’

무슨 말을 해야 할까. 그저 고마울 따름이다.

그리고 나도 모르게 흘러나오려는 실소를 삼킨 그 순간이었다.

“그래, 인사도 없이 이대로 떠날 속셈이었나?”

도무지 어울리지 않는 능청스러운 목소리와 함께, 거대한 철문 앞에서 나를 기다리고 있던 황제가 소리 내어 웃었다.
```

## Final English reading copy

```markdown
# Chapter 940

While the gers on the grasslands shivered in the cool night wind, heavy with sand, people behind a massive wall ten thousand li away were greeting the morning.

It was still far too early for sunrise. Darkness surrounded them on every side.

*Thudthudthudthud!*

Rough hoofbeats shattered the dead of night.

More than a hundred messengers passed through the Seven Gates without a single formality. Like the dozens of messenger eagles sent ahead of them, they vanished into the wind, each bound for a different destination.

And the man who had given all these orders listened as reports came in one after another, his face pale.

“All the messengers have just passed through the Seven Gates!”

“The Imperial Decree has been delivered to the high ministers of the Six Ministries!”

“The Censorate awaits Your Majesty’s command!”

“The officials of the Hanlin Academy and the Transmission Office are preparing the edict!”

“A report from the Five Tiger Commandery! In accordance with Your Majesty’s command, we are immediately preparing three hundred warships, one hundred thousand naval troops, and the Imperial Guards—”

“Enough.”

At the Emperor’s sudden command, every sound around him vanished as if washed away.

The Son of Heaven’s authority was absolute.

Though the Great Nation was only in its third generation, the power wielded by its current Emperor equaled—or perhaps surpassed—that of Taizu, who had unified the realm.

“How noisy.”

At the Emperor’s quiet murmur, everyone prostrated themselves, barely daring to breathe.

“We beg Your Majesty’s forgiveness!”

“Please execute us!”

*Rustle.*

The Emperor gave a small shake of his head and silently waved his long sleeve.

Those who understood the unspoken command backed away and disappeared with careful steps. Before long, only two people remained in the vast main hall.

“Every time I say anything, they start begging me to kill them. If I’d had to listen to that for another fifteen minutes, I might’ve bitten through my own tongue.”

At the Emperor’s bitter smile, Baek Yeon, Commander of the Embroidered Uniform Guard, spoke with a stern expression.

“Even as a joke, please don’t say such things.”

“It’s only a joke. What does it matter? Besides…”

The Emperor leaned at an angle against the throne and continued.

“I have not the slightest intention of dying in a situation like this.”

His face was still pale, but as he faced a new crisis, his eyes gleamed like luminous pearls.

“I expected trouble, but this is beyond what I imagined. I didn’t think they’d move so quickly.”

Baek Yeon wholeheartedly agreed.

Dark Heaven.

That rebellious faction, whose very name was ominous, was larger than expected—and far more methodical.

Even more so than a religious movement that had once erupted like a grass fire from a distant western land, back when Baek Yeon had served the late Emperor.

“It was more than fifty years ago. That was when the people called the Demonic Cult headed for the Central Plains.”

“The Great Faction War.”

The Emperor murmured to himself and stroked his graying beard.

Though it had happened long before he was born, everyone knew of the momentous event when no fewer than a hundred thousand so-called heretics set foot in the Central Plains.

Especially because they weren’t merely country bumpkins lured in by sweet words. They were an army armed with unwavering faith and spears and swords.

“When the Demonic Cult’s momentum reached the heavens, the martial artists of the orthodox factions petitioned the late Emperor. They said the Demonic Cult was a foreign enemy disrupting the Great Nation’s order, and asked him to raise the Imperial Army and order a campaign against them.”

“I know.”

The Emperor looked at Baek Yeon and added,

“And I know you were the strongest opponent of joining the war.”

Baek Yeon gave a small nod in acknowledgment.

It was true.

Here, in this very place, the high ministers of the court had argued fiercely for days. The late Emperor had seriously considered ordering a campaign, but Baek Yeon had pleaded with him so earnestly—more than he had ever seen him do before—that the Emperor finally gave up the idea.

“Can Your Majesty guess why I opposed it so strongly?”

“I think there were two main reasons. The first was that the Demonic Cult feared the Great Nation’s power and wasn’t harming the people. And the second was… Cang Gong.”

“That’s right. Unlike me, Cang Gong was the first to insist that we drive out the foreign enemy.”

“You made the right choice. If Father had sided with Cang Gong back then, the Great Nation would have shed a great deal of blood.”

“It was clear he intended to weaken the imperial house. That was all the more reason I had to oppose it.”

There had never been a victory without wounds, not in all of history.

Baek Yeon knew that as a commander who led an army, not merely as a martial artist. He had done everything in his power to keep the Great Nation out of the war.

Cang Gong—or rather, the Eastern Heaven Demon Lord—had already been a person of interest back then.

Of course, countless orthodox martial artists had died because of Baek Yeon’s opposition. But he didn’t regret it in the least.

He had simply made the choice that was best for the Emperor and the Great Nation—and, by extension, the people.

It wouldn’t have been too late to intervene after watching the two great powers, the Murim Alliance and the Demonic Cult, crash violently into each other.

And the result of that wait had been an orthodox victory that came close to mutual destruction.

“Back then, I actually hoped the Demonic Cult would win.”

The Emperor clicked his tongue at Baek Yeon’s words.

“You’re unusually honest today.”

“It can’t be helped. Many martial artists of the orthodox factions have the people’s trust, so we’d have no grounds to launch a campaign against them. But it would’ve been different if the Demonic Cult had survived.”

A massive boulder was too heavy even to move.

But what about a pebble left behind after being smashed and battered again and again?

And if that pebble had jagged edges sharp enough to harm the people, Baek Yeon would have taken up his hammer without the slightest hesitation.

He would have torn down the lawless fence that was Murim once and for all.

“But if things had gone as you hoped, we wouldn’t have made it to the present day.”

The Emperor’s low voice echoed through the vast hall.

He was right. It was deeply ironic, but they had relied on those very martial artists to put down the traitors and accomplish their great undertaking.

And now… it was time to set that contradiction right.

“I intend to help with everything I have. For their sake—and for all of us.”

*Thump.*

Baek Yeon lowered his head and went down on one knee.

A storm of bloodshed would soon descend—one that would make the Great Faction War seem insignificant.

Dark Heaven was more powerful than the Demonic Cult, and incomparably more dangerous.

A war was beginning that would not be confined to Murim. It would overturn the world.

“Your Majesty, ruler of all beneath the heavens, I humbly ask that you give me your orders.”

The information Jin Taekyung had delivered in the dead of night was an unexpected misfortune. But it was fortunate that they had already made thorough preparations to accomplish their great undertaking.

Hundreds of warships and thousands of officers.

Hundreds of thousands of troops, the imperial banners flying above them, were waiting for their command.

“I command Baek Yeon, Commander of the Embroidered Uniform Guard.”

With a solemn voice, the Emperor slowly rose, his ailing body standing upright.

He was no longer wearing his white sleeping robe, embroidered with a golden dragon in silk thread. Now, clad in heavy armor, he strode across the hall without hesitation.

*Clank. Clank.*

One step. Then another.

The Emperor descended from the throne and personally raised Baek Yeon to his feet.

“Announce to the entire army that I will personally lead the campaign.”

“……!”

Baek Yeon’s eyes trembled for an instant, unable to hide his shock.

It wasn’t only the impact of the Emperor taking command in person. He could feel the resolve of a man who had little time left to live.

“Your Majesty.”

But the words Baek Yeon struggled to force out never came.

The loyal subject saw the Emperor silently shake his head. All he could do was clench his teeth, his heart heavy.

“I, Baek Yeon, Commander of the Embroidered Uniform Guard… will obey Your Majesty’s solemn command.”

The Emperor gave him a faint smile instead of an answer, then walked past him.

The world beyond the wide-open iron gates was still shrouded in darkness.

Just like his own future, brief and shrouded in darkness.

*Still, this isn’t so bad.*

His body might be dying, but his mind was clearer than ever.

The first campaign he would lead in person—and the last.

To meet his end on a battlefield instead of in bed would be a blessing, not a tragedy.

And so was the fact that someone had briefly brought his will to live back to life.

“Come, Baek Yeon.”

The Emperor smiled brightly—so brightly it was hard to believe he was a dying man—and continued,

“We should see off a certain insolent rogue who’s leaving before me without keeping his promise to me.”

* * *

One shichen.

That was how much time had passed since I’d first gotten my hands on the iron chest left behind by the Eastern Heaven Demon Lord.

“Everything’s ready.”

At Hyuk Mujin’s report in my ear, I opened my eyes, which I’d kept tightly shut.

The look in his eyes and his expression were unusually grave. They seemed to say everything about how urgently the situation was unfolding.

“Let’s go.”

What else was there to say?

I gave a brief reply and stepped out of the pavilion, moving as if in a daze.

Even after circulating my qi once, my mind was still a mess.

*Half a month.*

Only half a month.

That was all the time left until the Double Ninth Festival. Or maybe even less.

The missive the Eastern Heaven Demon Lord had kept said Dark Heaven’s main force would invade Shanxi Province through the northern grasslands before the festival.

*It could be ten days. No—even tomorrow.*

I swallowed the groan rising in my throat.

This wasn’t just urgent. It was an emergency.

The distance from here, Zhejiang Province, where the imperial capital stood, to Shanxi Province was a full ten thousand li.

No matter how quickly the Imperial Court’s messenger eagles flew, the trip would take at least ten days.

*Can I get there in time?*

Even as I left the imperial palace with everyone else, doubt weighed heavily on my heart.

Then Jeok Cheongang, who had been watching me in silence the whole time, suddenly spoke.

“Was it about fifty years ago? I got into some petty dispute with that Thunderbolt Saber King bastard and ended up in a real fight.”

As though he were talking to himself, Jeok Cheongang glanced away from me and continued.

“I’d always looked down on him as someone far beneath me, so I didn’t think much of him. But when we actually traded blows, he was pretty strong. I didn’t show it, but I was surprised.”

The Bow Saint, who had been riding quietly with the reins in hand, replied.

“He’s a strong man. If it hadn’t been for you, he probably would’ve been the greatest of the Ten Kings.”

“Hmm. I suppose so.”

Jeok Cheongang nodded, then glanced at me and added,

“Still, the Hebei Peng Family didn’t become one of the Five Great Families for no reason. With that kind of strength, they could beat just about anyone. And they have enough intelligence-gathering power to keep a clear eye on what’s happening not only in Hebei but in Shanxi, too.”

Only then did I think I understood.

This completely random conversation was all meant to put me at ease.

*Heh.*

What was I supposed to say? I was just grateful.

And just as I swallowed the dry laugh threatening to slip out, someone spoke.

“So, were you planning to leave just like this without saying goodbye?”

With a breezy voice that didn’t suit him at all, the Emperor laughed aloud. He’d been waiting for me in front of the enormous iron gates.
```

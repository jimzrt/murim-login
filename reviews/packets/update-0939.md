<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0939.txt",
      "sha256": "60d56fed89d471588e79e9cd33f49676e44aa0acc6d2034bf691e1e0cf6fba4f",
      "bytes": 13382
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "3ebe5e0d5018151c5bbef976b0e04b8f57513a240e29323e91f9e518da6f2a7a",
      "bytes": 2416
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "c83d671253dcc6207dec6e7e72f91d57c7a1f177dfbc45158e25b99121e8e54c",
      "bytes": 232276
    },
    {
      "path": "characters/Cang Gong.md",
      "sha256": "e9328041f3cae4edbc2c8dd4138766554c1273a602bcd519637c462a9d8136f6",
      "bytes": 778
    },
    {
      "path": "characters/Chinggen.md",
      "sha256": "29bcaed0a39312b660b31bec24cec9d7d7d53fc46bd3f5a8aa421484b2916250",
      "bytes": 611
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "b5a189dc559592d86da7c87e9a4c5587cc435c0daa3246a2d58b14f8c5be1b0b",
      "bytes": 759
    },
    {
      "path": "characters/Eastern Heaven Demon Lord.md",
      "sha256": "f975350e452cc1e35c18335b8882378ac49bc16aeb55b89cd1e0c0e94c27ec01",
      "bytes": 838
    },
    {
      "path": "characters/Hong Jin.md",
      "sha256": "02f8d892ecf5a84bb693737525d8a7343bcb1da7f895254fee049ce204410064",
      "bytes": 853
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "a587cb28cafef786952194354b0813656c0942e8aad74e5a125bad2c074add81",
      "bytes": 1445
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "98021dd9ae878426b4faf11b9651e6771719a0cee57fd7d4082c638b1a6608bc",
      "bytes": 1204
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "708f9352902825eed7adcefef5d1cc5688a17922dd1f68ee456062ec8756679e",
      "bytes": 1343
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "eeb7a26f581b21781f3334280b42a11cc9eeddd4071dc5b56e3e0d953e275de0",
      "bytes": 622
    },
    {
      "path": "characters/Temur.md",
      "sha256": "a50953f280942687f96dd999483e49e15f223c1b08cb76d6744ed2596ef8b516",
      "bytes": 622
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "0e2d532f2af4d7be69c6e65c1cef25321d7cf2235ebf140c6de94d6147d63060",
      "bytes": 266948
    }
  ],
  "estimated_tokens": 12604
}
-->

# Durable State Update — Chapter 939

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
1 and safe_through 939. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 939. Profile updates may replace only one
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
  "chapter": 939,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 939,
    "continuity_sources": [939],
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
    "Jeok Cheongang considers Taekyung his one and only Disciple and is furious that the Bow Saint put him in danger."
  ],
  "continuity_sources": [
    937,
    938
  ],
  "open_questions": [
    "What is the Martial God’s identity, and what is the full nature of his connection to the chosen one and the Bow Saint?",
    "How far has Dark Heaven infiltrated the Great Nation, and which officials or commanders are involved?",
    "Where is Ma Sanbao, and what is his current status?",
    "What do the papers, bamboo slips, and silk pouch from the Eastern Heaven Demon Lord’s chest contain, and what is their significance?",
    "What is the significance, if any, of the broken pocket watch given as the System update reward?"
  ],
  "safe_through": 938,
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
| 태원진가   | **Jin Family of Taiyuan**        |
| 암천     | **Dark Heaven**                  |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 중원     | **Central Plains**                               |                                                       |
| 강호     | **martial world**                                | Prefer “Murim” where the setting itself is meant      |
| 제자     | **Disciple**                                 |
| 전각     | **pavilion**                                 | Use “hall” only when established for a specific named building |
| 칭호               | **Title**                      |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 창공 | **Cang Gong** | The bedridden East Depot leader for whom Ma Sanbao acts. |
| 칭겐 | **Chinggen** | Northern Gaoyuan chieftain commanding one hundred tribespeople; restrains Temur. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 동천마군 | **Eastern Heaven Demon Lord** | Title of the absurd masked antagonist in Jin's nightmare. |
| 홍진 | **Hong Jin** | Level 22 man at the City Lord's luncheon; delicate in appearance and voice. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 테무르 | **Temur** | Northern Gaoyuan chieftain commanding one hundred tribespeople; claims descent from the khans. |
| 평화 | **Peace Guild** | Guild name. |
| 전서구 | **messenger pigeon** | Pigeon delivering the Lower District Sect's Jeongyang Branch report. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 전서응 | **messenger eagle** | Emergency courier used by the Lower District Sect. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 마유주 | **mare's-milk wine** | Fermented alcoholic drink offered at the gathering. |
| 게르 | **ger** | Traditional nomadic dwelling contrasted with Central Plains wooden buildings. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 촌각 | **moments** | Short intervals disappearing from Jeok's day. |
| 식경 | **half an hour** | Time limit given for the requested reports. |
| 화룡각 | **Fire Dragon Pavilion** | New name chosen for Taekyung's pavilion. |
| 이전 | **Two Halls** | Top-level Murim Alliance organizational grouping. |
| 전서 | **missive** | A written message exchanged or delivered in secret. |
| 건청궁 | **Qianqing Palace** | The Emperor's palace, where Baek Yeon meets him. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 홍진 | 진태경 | political_host_to_young_martial_artist | Young Hero Jin; Young Master Jin; Sleeping Dragon of Shanxi | polite, coaxing, and probing | Uses respectful forms while steering Taekyung toward relaying the Escort Bureau proposal and teasing him with the Seongun Escort Bureau. |
| 진태경 | 홍진 | young_martial_artist_to_political_official | Comrade Chairman—no, Deputy Military Commissioner | casual and teasing, then formally corrective | Deliberately jokes with an inappropriate title before correcting himself to Hong Jin's official office. |
| 테무르 | 칭겐 | fellow_chieftain | Chinggen | familiar and argumentative | Temur addresses his fellow chieftain by name while defending their khan lineage. |
| 칭겐 | 테무르 | fellow_chieftain | Temur | familiar and cautioning | Chinggen uses Temur's name while warning him not to act rashly. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 혁무진 | 적천강 | subordinate_to_overwhelming_elder | Great Hero Jeok | deferential and fearful | Mujin uses 적 대협 while reporting Jeok’s orders and Taekyung’s awakening. |
| 적천강 | 혁무진 | overwhelming_elder_to_junior_martial_artist | you stupid fool | blunt and mocking | Jeok calls Mujin a 멍청한 놈 after knocking him down during the attempted escape. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 혁무진 | 조장님 | pavilion_member_to_squad_leader | Captain | deferential and dubious | Mujin questions whether the pasture should be called the Nanman Ranch instead of the Nanman Beast Palace. |
| 홍진 | 혁무진 | imperial aide addressing a martial artist accompanying the prince | Martial artist Hyuk | polite and conversational | Uses 혁 무인 when asking whether Mujin knows of an exception. |
| 혁무진 | 홍진 | martial artist addressing a senior official and political ally | Comrade Hong | casual and coaxing | Hyuk Mujin addresses Hong Jin as 홍 동지님 while trying to calm him and de-escalate the confrontation. |
| 적천강 | 창공 | hostile opponents | you; you bastard | blunt and threatening | Jeok Cheongang uses 네놈, 이 불알 없는 놈, and 호로새끼 while taunting Cang Gong. |
| 창공 | 적천강 | hostile opponents | Fire King Jeok Cheongang | taunting and sardonic | Cang Gong names Jeok by his title, then comments on how alike master and disciple are. |
| 적천강 | 동천마군 | enemies | you | blunt and informal | Jeok Cheongang addresses the Eastern Heaven Demon Lord with hostile familiarity. |
| 동천마군 | 적천강 | enemies | you | informal | The Eastern Heaven Demon Lord speaks to Jeok Cheongang during their duel. |
| 진태경 | 동천마군 | young martial artist confronting an enemy | ugly-ass big bro | casual, profane, and taunting | Jin calls out to the Demon Lord after returning to the hall. |
| 동천마군 | 진태경 | enemy recognizing the spear wielder | Jin Taekyung | shouted, informal | The Demon Lord cries Taekyung's name after identifying him as the spear's owner. |
| 궁성 | 진태경 | elder who spent decades searching for the chosen one | you | casual and teasing | Uses 너/널 while testing and praising Taekyung. |
| 진태경 | 궁성 | chosen one addressing the elder who sought him | you | polite, shifting to familiar-casual under stress | Begins with formal-polite phrasing, then speaks more casually as the conversation intensifies. |
| 적천강 | 궁성 | old acquaintance and fellow martial master | you; nasty old hag | blunt and familiar | Uses a contemptuous insult while expressing concern for his Disciple. |
| 궁성 | 적천강 | old acquaintance and fellow martial master | you | familiar and lightly teasing | Speaks with dry familiarity about his unchanged, impulsive nature. |

## Listed compact profiles

### Cang Gong.md

# Cang Gong (창공)

- **Safe through:** Chapter 931
- **Aliases:** None
- **Role:** Cang Gong is the Eastern Heaven Demon Lord’s assumed identity, through which he became the East Depot’s Brush-Holding Eunuch and a power second only to the Emperor.
- **Personality:** Calculating and self-assured, he is driven by vengeance and believes the rulers and the world betrayed him first.
- **Voice:** Dry and sardonic, he delivers taunts and judgments in measured statements.
- **Relationships:** He was raised by a master and fellow disciples in the Maoshan Sect, whose members died resisting the forced relocation of the capital; Ma Sanbao is his disciple, and he regards Jin Taekyung as a potential recruit.

### Chinggen.md

# Chinggen (칭겐)

- **Safe through:** Chapter 236
- **Aliases:** None
- **Role:** Northern Gaoyuan chieftain commanding one hundred tribespeople and claiming descent from the khans
- **Personality:** Prudent, restrained, and attentive to the danger posed by the gathering's other powers
- **Voice:** Measured, familiar, and cautioning
- **Relationships:** Temur is his fellow chieftain, and Chinggen repeatedly restrains Temur's recklessness; Black Sand recruited both chieftains into a four-way alliance to attack the Jin Family of Taiyuan

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 938
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Eastern Heaven Demon Lord.md

# Eastern Heaven Demon Lord (동천마군)

- **Safe through:** Chapter 937
- **Aliases:** Wei Zhong
- **Role:** The Eastern Heaven Demon Lord was Wei Zhong, the East Depot’s Seal-Holding Eunuch and a former Maoshan Sect disciple who commanded the dead with a bell; Jin Taekyung killed him with blue-white flames.
- **Personality:** His hatred grew from losing his family and sect, but recognizing his own lonely childhood in Zhu Bao ultimately moved him to relinquish his vengeance and choose a less harmful final act.
- **Voice:** He speaks in measured, almost lyrical phrasing, recounting the past before turning to pointed accusations.
- **Relationships:** Ma Sanbao is his Disciple; he holds the Emperor responsible for Taizu’s actions against the Maoshan Sect.

### Hong Jin.md

# Hong Jin (홍진)

- **Safe through:** Chapter 937
- **Aliases:** None
- **Role:** Hong Jin is Eunuch Hong, a former Deputy Military Commissioner of Shanxi Province and East Depot member who is now responsible for the East Depot and remains a trusted aide to Prince Shangshan.
- **Personality:** Composed, socially deft, and ambitious, Hong Jin became a eunuch to escape poverty and save his family, then used his abilities to pursue a broader life.
- **Voice:** Delicate and deferential with Prince Shangshan, but warm, familiar, and playfully forthright with trusted allies.
- **Relationships:** Hong Jin is devoted to Prince Shangshan and is trusted by the Emperor to take responsibility for the East Depot; he is a longtime friend of Ma Sanbao and a trusted ally of Jin Taekyung.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 938
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and an active member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented; despite being naturally fearful, he faces danger and remains loyal to the person he serves, with irreverent self-deprecation and a taste for glory. He is suspicious of Taekyung, bluntly critical of the family's disgraced third son, and an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; with Taekyung, blunt and occasionally incredulous, while using breezy, irreverent banter to defuse tense situations.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad; he regards Taekyung as the person who has repeatedly saved him and now believes he may be able to save Taekyung in turn. As a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Fire Dragon Pavilion members accompanying Taekyung. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 938
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; believes there is no absolute justice and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and says they have shared everything since he accepted him; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and remains Peng Cheolhu's rival.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 938
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader.
- **Personality:** Hungry, self-aware, dryly observant, and pragmatic under pressure; accepts extreme personal risk when duty and the lives of others demand it.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; So Gyo says he is the chosen one spoken of by the Martial God, while the Bow Saint sought him for decades and relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 938
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Temur.md

# Temur (테무르)

- **Safe through:** Chapter 236
- **Aliases:** None
- **Role:** Northern Gaoyuan chieftain commanding one hundred tribespeople and claiming descent from the khans
- **Personality:** Hot-tempered, reckless, proud of his khan lineage, and hostile to Han Chinese encroachment
- **Voice:** Blunt, heated, and confrontational
- **Relationships:** Chinggen is his fellow chieftain and restrains him from provoking the Human Butcher; both chieftains accepted Black Sand's proposal for a four-way alliance to attack the Jin Family of Taiyuan

## Korean source

```text
＃939화



‘저놈은…….’

짙은 어둠 너머에서 빠르게 가까워지는 익숙한 얼굴을 확인한 적천강은, 전신을 타고 흘러넘치던 기세를 갈무리했다.

갑작스럽게 찾아온 불청객의 정체가 혁무진이라서?

아니다.

평소와 다른 그의 모습에서, 심상치 않은 기색을 읽었기 때문이었다.

후욱, 훅.

쉴 새 없이 움직이는 두 다리와 거친 호흡.

도대체 얼마나 뛰어다녔던 것인지 땀이 맺혀 있는 얼굴은 다급함으로 가득했다.

‘……무언가 일이 생긴 모양이군.’

지금 이 순간 엄습해 오는 불길한 직감이 착각이길 바라며, 적천강은 어둠 속에서 잠시 방향을 잃고 머뭇거리는 혁무진을 향해 입을 열었다.

“뭘 그리 꾸물대느냐.”

“헛. 적 대협!”

헐레벌떡 달려온 혁무진이 궁성을 발견하고는 멈칫했다.

“무, 무림말학 혁무진이…….”

슥.

가벼운 손짓으로 이어지려는 말을 막아선 궁성이 입을 열었다.

“인사치레는 되었으니 용건부터.”

“다름이 아니라 조장님. 그러니까, 제 주군께서 두 분을 급히 모셔 오라 하셨습니다.”

“두 분?”

“예. 사방을 뒤져 봐도 도무지 두 분의 행방을 찾을 수 없어 주군께 여쭤보았더니 이 장소를 알려 주셔서…….”

문득 궁성이 미간을 좁혔다.

그러나 그 이유는 까마득한 후배가, 그것도 핏덩이나 다름없는 진태경이 감히 자신을 오라 가라 했다는 것에서 오는 불쾌감 때문이 아니었다.

“자세한 이야기는 직접 하시겠다 합니다. 다른 사람들은 이미 모여 있는 상황이고요.”

이어진 혁무진의 말에 궁성이 작게 혀를 찼다.

“생각 이상으로 심각한 일이 생긴 모양이군요. 당신뿐만 아니라 나까지 불러오라 할 정도면.”

적천강은 무거운 얼굴로 고개를 끄덕였다.

그가 아는 진태경은 다소 막 나가는 것 같긴 해도, 정해진 선 안에서만큼은 예의를 철저히 지키는 놈이다.

더군다나 외부인이라 할 수 있는 궁성까지 이렇게 수하를 보내 청할 정도라면, 어느 정도의 사안인지 쉬이 짐작이 가지 않았다.

― 아쉽지만, 오늘의 대화는 여기서 마무리해야 할 것 같네요.

나직하게 귓가를 파고드는 전음(傳音).

아쉬움이라고는 털끝만큼도 느껴지지 않는 궁성의 담담한 얼굴을, 적천강은 착 가라앉은 눈으로 응시했다.

― 그렇겠지. 오늘은.

다음의 대화를 기약하는 대답이다.

아직 하지 않은 말도, 차마 묻지 못했던 질문도 남아 있는 적천강은 이대로 모든 것을 마무리 지을 생각이 추호도 없었다.

― 다음번에는 오늘보다 더 의미 있는 대화를 나누었으면 좋겠군.

그러나 적천강의 뼈 있는 전음에도, 궁성은 시종일관 침착함을 잃지 않았다.

― 그럴 수 있을 겁니다. 굳이 이다음이 아니더라도, 앞으로의 기회는 많으니까.

― 그게 무슨…….

여러 의미가 담긴 대답에 멈칫한 적천강이 말을 이어 가려던 바로 그 순간이었다.

푸드득.

머리 위에서 불현듯 울려 퍼지는, 힘찬 날갯짓 소리.

‘저건.’

고개를 든 적천강은 똑똑히 볼 수 있었다.

아니, 그와 동시에 움직인 궁성은 물론 엉겁결에 그들의 시선을 따라간 혁무진 역시 마찬가지였다.

쉬이익!

아득한 창공 위, 검게 물든 하늘을 가로지르며 날아가는 수십여 마리의 새들.

철저한 훈련을 받은 듯, 제각각의 방향으로 무리 지어 나아가는 날짐승들의 모습이 그들의 눈동자에 비쳤다.

“전서응(傳書鷹)……!”

신음처럼 뇌까린 적천강은 마음 한구석이 무거워지는 것을 느꼈다.

평범한 전서구도 아닌 귀한 전서응을, 그것도 저토록 많이 날려 보냈다는 것은 대국의 황실이 움직였다는 뜻이다.

아마도 자신의 제자가 전해 준 소식으로 인해서.

‘도대체 무슨 일이기에.’

적어도 한 가지만큼은 확실하다.

더는 머뭇거릴 시간 따위는 없다.

“앞장서거라. 어서.”

날이 밝기에는 너무나도 야심한 밤.

어느덧 보이지 않는 동요가 황궁을 휩쓸고 있었다.



* * *



“어찌 된 일이냐.”

그것이 바람처럼 들이닥친 적천강의 첫 마디였고, 나는 대답 대신 손에 들고 있던 것을 내밀었다.

슥.

기름으로 번들거리는 여러 장의 종이를 확인한 적천강의 눈동자가 깊게 가라앉았다.

“전서(傳書)?”

연륜이라면 천하의 누구에게도 뒤지지 않는 노강호답게, 종이의 정체를 정확하게 간파한 그는 내가 건넨 종이 뭉치를 받아 빠르게 훑었다.

그리고 촌각(寸刻)이 흐르기도 전에 고개를 들었다.

바위처럼 딱딱해진 얼굴로.

“여기에 적혀 있는 내용이…… 전부 사실이냐?”

아마 한 식경 전이었다면 적천강의 목소리조차 듣지 못했을 것이다.

그만큼 정신이 없던 상황이었으니까.

하지만 화룡각 대원들에게 상황을 설명하고, 홍진과 건청궁에 대략적인 정보를 전달한 지금은 애써 담담하게 대답할 수 있었다.

물론, 그 대답조차 안개처럼 흐릿했지만.

“모릅니다.”

“그게 무슨!”

“정확하게는, 아직 확인된 바가 없습니다. 다만…….”

나는 굳어 있는 적천강과 이제야 전서를 읽고 있는 궁성, 그리고 전각 내부에 모여 있는 화룡각 대원들을 차례대로 바라보며 말을 이었다.

“상당히 신빙성이 높은 정보죠.”

“그 근거는?”

이번에는 궁성이다. 전서를 내려놓은 그녀의 눈빛은 그 어느 때보다 착 가라앉아 있었다.

“아니, 그 전에 이 전서를 발신한 자가 누구지?”

“그 역시 알 수 없습니다. 암천에서도 상당히 높은 자리에 있는 누군가라는 것밖에는.”

“그런 자가 어찌 네게…….”

말꼬리를 흐린 궁성이 문득 침음성을 흘렸다.

“처음부터 네게 보낸 것이 아니었군.”

정확하다.

이 전서를 보낸 자는, 내가 아닌 다른 누군가에게 정보를 전달할 목적으로 글귀를 적어 내려갔을 테니까.

“설마?”

혼잣말처럼 낮게 뇌까린 적천강을 향해, 나는 고개를 끄덕였다.

“맞습니다. 동천마군(冬天魔君)이 보관하고 있던 물건 중 하나입니다.”

“……!”

“……!”

적천강과 궁성의 눈동자가 크게 뜨였다.

그들이 오기 전 이미 대략적인 상황을 들어 알고 있던 화룡각 대원들 역시 동요를 숨기지 못했다.

저 전서들에 담긴 내용을 한 번이라도 본 이들이라면 당연한 반응이었다.

아직 기름기가 가시지 않은 저 네댓 장의 종이에는 수만 명. 아니, 어쩌면 수십만 명의 목숨이 달린 정보가 적혀 있었으니까.

그리고 그중 하나가 바로 지금 내 발치에 놓여 있다.

툭.

떨리는 손끝으로 집어 든 한 장의 종이.

동시에 가장 먼저 눈동자에 틀어박히는 네 글자.

‘산서멸계(山西滅計).’

언제였는지 모를 과거, 동천마군에게 이 전서를 작성한 누군가는 말하고 있었다.

중양절(重陽節)이 오기 전, 암천의 본대가 북부의 광활한 초원을 넘어 산서성을 침공할 것이라고.

까드득.

나는 이를 악물었다. 터져 나오려는 신음을 삼키며 눈을 감았다.

만약, 만약 이 정보가 사실이라면…….

‘고작 보름.’

그것이 중양절까지 남아 있는 시간이었다.

산서성. 아니, 태원진가에게 남아 있는 시간.



* * *



평화와 분란은 단짝이다.

평화 속에서도 천하 어디에선가는 크고 작은 분란이 벌어지고, 혼란스러운 전쟁통에도 누군가는 평화를 누린다.

치열하고도 길었던 군웅할거(群雄割據)의 시대를 지나, 천하통일의 위업을 달성한 대국이 탄생한 이후에도 그 사실은 달라지지 않았다.

지금까지 그러했고, 현재에도 그러하며, 앞으로도 그럴 테니까.

그리고 이 드넓은 천하에서 가장 끊임없이 분란이 벌어지는 곳을 꼽으라면, 그건 다름 아닌 북부 초원이었다.

풀과 흙, 말들로 가득한 곳.

낮에는 푸른 하늘을 유영하는 날짐승들이, 밤에는 어둠 속에서 몸을 웅크린 들짐승들이 시체를 찾아 떠도는 곳.

군웅할거의 시대 이전.

한때 광활한 영토를 정복하며 천하의 주인을 자처했던 유목민족의 후예는, 여전히 그곳에서 살아가고 있었다.

화려한 궁전이나 높은 성벽이 아닌 천과 풀로 이루어진 게르에서, 걸음마를 뗄 무렵부터 한 몸처럼 지냈던 말들과 함께.

그러나 동시에, 위대한 선조들이 이룩했던 찬란한 과거의 영광은 그들에게서 서서히 잊혀져 가고 있었다.

“음. 나쁘지 않군. 아니, 훌륭해.”

흡족한 목소리로 뇌까린 사내는 연신 술잔을 기울였다.

여느 유목민이 그러하듯 정수리를 깨끗이 밀고 뒤로 길게 땋아 변발(辮髮)을 한 그였으나, 위풍당당한 체구와 이마에 놓인 황금 왕관은 사내를 누구보다 돋보이게 만들었다.

아니, 그와 나란히 상석(上席)에 앉아 있는 또 다른 사내만 아니었다면 분명 그러했을 터였다.

“테무르. 내 형제여, 무엇이 되었든 너무 과하면 독이 되는 법이라는 말을 잊었나?”

깊이가 느껴지는 눈동자와 날렵한 체구.

옆자리의 거한, 테무르를 바라보며 작게 혀를 차는 그의 이마에도 두 마리의 말이 새겨진 황금 왕관이 얹혀 있었다.

“네 말이 맞다, 칭겐. 언제나 항상 그랬지.”

못마땅한 기색을 드러내는 사내, 칭겐을 바라보며 고개를 끄덕인 테무르가 누런 이빨을 드러내며 웃었다.

“하지만 한 가지는 똑똑히 알아 둬. 술은 그 자체로 약이야. 결코 독이 되는 법이 없지.”

“이런, 테무르.”

“좋은 날에 이러지 말고, 함께 술잔이나 기울이는 게 어떤가. 응?”

고개를 절레절레 내젓는 칭겐의 허리춤을 쿡 찌른 테무르가 손에 쥔 술잔을 높이 치켜세우며 외쳤다.

“어찌 생각하는가, 자랑스러운 초원의 형제들이여!”

와아아아!

거대한 게르 안에 모여 있던 수백여 명의 전사들이 환호성을 내지르며 호응하자, 테무르가 껄껄 웃었다.

“그래, 이래야지!”

그는 지금 이 순간이 진심으로 기뻤다.

한때 테무르가 이 게르 안에 모인 전사들의 숫자보다도 적은 부족민들을 이끌었던 것이 불과 이 년 전이다.

하지만 지금은 어떠한가.

황금으로 만든 왕관을 쓰고, 수하들과 함께 말의 젖을 짜서 끓여 낸 마유주(馬乳酒) 대신 저 멀리 중원의 명주(名酒)를 양껏 들이켠다.

자신을 향해 쏟아지는 온갖 환호를 들으며.

“테무르 칸 만세! 칭겐 칸 만세!”

“부디 천수를 누리소서!”

칸.

광활한 초원의 지배자이자, 수만에 달하는 말과 전사를 거느린 왕.

이 얼마나 듣기 좋은 소리인가.

한때는 그저 꿈이었던 그 칭호가 이제는 자신의 것이다.

어릴 적부터 생사고락(生死苦樂)을 함께해 왔던 두 형제는, 분란이 끊이질 않던 초원에 평화와 번영을 가져오며 비로소 칸의 칭호를 얻을 수 있었다.

“저들의 외침이 들리나? 응? 똑똑히 듣고 있느냔 말이야.”

전사들과 함께 어울리던 테무르는 칭겐의 빈 술잔을 가득 채웠다.

나무나 동물의 뼈를 깎아 만든 것이 아닌, 중원 땅에서 들여온 은제 술잔은 영롱하게 빛나며 두 사람의 얼굴을 반사 시키고 있었다.

싱글벙글 웃고 있는 테무르와, 불편한 기색이 역력한 칭겐의 상반된 얼굴을.

“그야 물론 듣고 있지. 하지만 지금은 마냥 웃고 떠들 때가 아닐세, 테무르.”

“허참, 자네 또 그러는군. 웃고 떠드는 것에 때가 어디 있다고?”

“형제여, 내가 전령을 보내 소식을 전하지 않았나?”

“아, 그거 말인가? 들었지.”

테무르가 고기를 질겅질겅 씹으며 말을 이었다.

“하지만 크게 걱정하지 마. 우리가 칸이 되었다고는 하나 초원은 넓어. 손이 안 닿는 곳에서 벌어지는 일까지 어찌할 수는 없지.”

물론 테무르 역시 알고 있었다.

소수의 정찰병들이 드물게 실종되고, 서쪽 끝자락의 초원에서 몇 번의 분란이 벌어졌다는 사실을.

그러나 테무르 입장에서는 별것 아닌 소식이었다.

이 순간의 향락을 잊기에는 턱없이.

“자, 근심 많은 형제여. 우선 잔부터 비우고 얘기하자고.”

테무르가 호쾌하게 웃으며 또다시 칭겐에게 술을 권하던 그 순간.

펄럭.

모래 먼지를 머금은 차가운 바람이, 게르의 입구를 밀어젖혔다.
```

## Final English reading copy

```markdown
# Chapter 939

*That guy……*

Recognizing a familiar face rapidly approaching from beyond the deep darkness, Jeok Cheongang gathered in the aura that had been surging through his entire body.

Was it because the unexpected, unwelcome visitor was Hyuk Mujin?

No.

It was because he sensed something was wrong in the way Mujin looked—so unlike himself.

*Huff, huff.*

His legs wouldn’t stop moving, and his breathing was ragged.

Who knew how far he’d run? Sweat glistened on his face, which was taut with urgency.

*……Something must have happened.*

Hoping the ominous feeling creeping over him at that very moment was a mistake, Jeok Cheongang called out to Hyuk Mujin, who had briefly lost his way in the darkness and hesitated.

“What are you dawdling for?”

“Ah. Great Hero Jeok!”

Hyuk Mujin came rushing over, then stopped short when he spotted the Bow Saint.

“Th-this junior of Murim, Hyuk Mujin……”

With a light gesture, the Bow Saint stopped him from continuing and spoke.

“Save the formalities. Tell us why you’re here.”

“It’s…… Captain. I mean, my lord ordered me to bring the two of you to him at once.”

“The two of us?”

“Yes. I searched everywhere, but couldn’t find either of you. When I asked my lord, he told me where you were……”

The Bow Saint’s brow furrowed.

But it wasn’t because a junior so far below her—Jin Taekyung, who was practically still a child—had dared to summon her as if he could order her around.

“He said he’d explain the details in person. Everyone else is already gathered.”

At Mujin’s words, the Bow Saint clicked her tongue softly.

“Something more serious than I thought must have happened. Serious enough that he sent for not just you, but me as well.”

Jeok Cheongang nodded, his face grave.

He knew Jin Taekyung. The brat could be reckless, but he was meticulous about observing the proper courtesies—at least within certain bounds.

And if he’d even sent a subordinate to summon the Bow Saint, an outsider as far as he was concerned, it was hard to guess just how serious the matter was.

—Unfortunately, I think we’ll have to end our conversation here.

The Bow Saint’s Sound Transmission slipped quietly into his ear.

Jeok Cheongang regarded her impassive face with a heavy gaze. He didn’t detect a trace of regret in it.

—So it seems. For tonight.

His reply promised they’d continue their conversation another time.

There were still things Jeok Cheongang hadn’t said, and questions he hadn’t dared to ask. He had no intention of leaving things as they were.

—I hope our next conversation will be more meaningful than this one.

Even at Jeok Cheongang’s pointed words, the Bow Saint remained composed.

—It will be. There will be plenty of chances, even if not the next time we meet.

—What does that……

Jeok Cheongang faltered at the many possible meanings in her answer. He was just about to continue when—

*Flap, flap.*

The sound of powerful wings suddenly rang overhead.

*That’s……*

Jeok Cheongang looked up and saw it clearly.

So did the Bow Saint, who turned her gaze at the same time, and Hyuk Mujin, who reflexively followed their eyes.

*Whoosh!*

Dozens of birds flew across the distant sky, black against the darkened heavens.

The sight of the creatures in flight moving in separate formations, each heading in a different direction as if thoroughly trained, was reflected in their eyes.

“Messenger eagles……!”

Jeok Cheongang murmured the words like a groan, and felt his heart grow heavy.

Sending out so many precious messenger eagles—not ordinary messenger pigeons—meant the Great Nation’s imperial court was on the move.

Probably because of the news his Disciple had delivered.

*What could have happened?*

At least one thing was certain.

There was no time left to hesitate.

“Lead the way. Hurry.”

It was a night far too deep for dawn to be near.

And now, an invisible unrest was sweeping through the Imperial Palace.

* * *

“What happened?”

Those were Jeok Cheongang’s first words as he burst in like the wind. Instead of answering, I held out what I had in my hand.

*Swish.*

Jeok Cheongang’s eyes sank as he examined the several sheets of paper, slick with oil.

“A missive?”

A veteran martial artist whose experience was second to none in the world, he had immediately recognized the papers. He took the stack from me and skimmed through it quickly.

Before even a few moments had passed, he looked up.

His face had gone as hard as stone.

“Is everything written here…… true?”

If it had been half an hour ago, I might not even have heard Jeok Cheongang’s voice.

I’d been too distracted to think straight.

But now I’d explained the situation to the Fire Dragon Pavilion members and passed along a general outline to Hong Jin and Qianqing Palace. I managed to answer calmly, though the answer itself was still hazy as mist.

“I don’t know.”

“What do you mean!”

“To be precise, none of it has been confirmed yet. But……”

I looked in turn at Jeok Cheongang, rigid with tension; the Bow Saint, who had just begun reading the missive; and the Fire Dragon Pavilion members gathered inside the hall.

“It’s highly credible information.”

“On what grounds?”

This time, it was the Bow Saint. She set down the missive, her gaze more grave than ever.

“No, before that—who sent it?”

“I don’t know that, either. All I know is that it came from someone in a fairly high position in Dark Heaven.”

“How could someone like that send it to you……”

The Bow Saint let her words trail off and gave a low, thoughtful murmur.

“They weren’t sending it to you in the first place.”

Exactly.

Whoever had sent this missive must have written it intending to pass the information to someone other than me.

“Could it be?”

Jeok Cheongang murmured under his breath. I nodded.

“That’s right. It was among the things the Eastern Heaven Demon Lord had kept.”

“……!”

“……!”

Jeok Cheongang and the Bow Saint’s eyes widened.

The Fire Dragon Pavilion members, who had heard the general outline before the two of them arrived, couldn’t hide their agitation, either.

Anyone who had seen even a single line of those missives would have reacted the same way.

The four or five sheets of paper, still slick with oil, held information that could determine the fate of tens of thousands of lives. Maybe even hundreds of thousands.

And one of those sheets was lying at my feet right now.

*Tap.*

I picked up a sheet of paper with trembling fingertips.

Four characters leaped into my eyes at once.

*Shanxi Annihilation Plan.*

At some point in the past, someone had written this missive to the Eastern Heaven Demon Lord. The message was clear: before the Double Ninth Festival, Dark Heaven’s main force would cross the vast northern grasslands and invade Shanxi Province.

*Crack.*

I clenched my teeth. Swallowing the groan that threatened to escape, I closed my eyes.

If—if this information was true……

*Just half a month.*

That was how long remained until the Double Ninth Festival.

The time left to Shanxi Province.

No—the time left to the Jin Family of Taiyuan.

* * *

Peace and turmoil went hand in hand.

Even in times of peace, disturbances great and small broke out somewhere in the world. And even amid the chaos of war, there were people who enjoyed peace.

That had been true after the long, fierce age of rival warlords, when the Great Nation rose to power and achieved the unification of the world.

It had been true until now, was true in the present, and would remain true in the future.

And if you had to name the place in this vast world where turmoil broke out most constantly, it was none other than the northern grasslands.

A place filled with grass, earth, and horses.

By day, birds soared through the blue sky. By night, wild beasts huddled in the darkness and wandered in search of corpses.

Before the age of rival warlords, the descendants of a nomadic people who had once conquered a vast territory and claimed the title of rulers of the world had lived there.

They still lived there now, in gers made of cloth and grass rather than splendid palaces or towering walls, alongside the horses they’d been as inseparable from as their own bodies since they first learned to walk.

And yet, the shining glory of the great past their ancestors had built was slowly fading from their memories.

“Hmm. Not bad. No—excellent.”

The man murmured with satisfaction, taking another sip from his cup.

Like any other nomad, he had shaved the crown of his head clean and braided his hair into a long queue down his back. But his imposing build and the golden crown on his forehead made him stand out more than anyone.

Or he would have, if not for the other man seated beside him in the place of honor.

“Temur, my brother. Have you forgotten that too much of anything can become poison?”

He had deep-set eyes and a lean build. As he looked at the hulking Temur beside him and clicked his tongue softly, the golden crown on his own forehead gleamed. Two horses were engraved upon it.

“You’re right, Chinggen. You always have been.”

Temur nodded at Chinggen, who looked displeased, then grinned, baring yellow teeth.

“But remember one thing. Alcohol is medicine in and of itself. It can never be poison.”

“Oh, Temur.”

“Come on, don’t be like that on a fine day. Why don’t we raise a cup together, hmm?”

Temur jabbed the head-shaking Chinggen in the waist, then raised his cup high and called out:

“What do you say, proud brothers of the grasslands!”

“Waaah!”

Hundreds of warriors gathered inside the vast ger cheered in response, and Temur roared with laughter.

“That’s more like it!”

He was genuinely happy in that moment.

Only two years ago, Temur had led a tribe with fewer people than the number of warriors now gathered inside this ger.

But look at him now.

He wore a crown of gold and drank his fill of fine liquor imported from the distant Central Plains, instead of mare’s-milk wine made by milking and boiling horses alongside his followers.

All while hearing the cheers pouring down on him.

“Long live Khan Temur! Long live Khan Chinggen!”

“May you live to a ripe old age!”

Khan.

Ruler of the vast grasslands, king of tens of thousands of horses and warriors.

What a wonderful title to hear.

Once only a dream, it now belonged to him.

The two brothers, who had shared life and death together since childhood, had brought peace and prosperity to the endlessly turbulent grasslands—and at last earned the title of Khan.

“Can you hear them? Hm? I said, are you listening?”

Temur, who had been mingling with his warriors, filled Chinggen’s empty cup.

The silver cup imported from the Central Plains—not carved from wood or animal bone—shone brilliantly, reflecting the faces of the two men.

Temur’s was grinning from ear to ear; Chinggen’s was plainly uncomfortable.

“Of course I can hear them. But now isn’t the time to laugh and drink, Temur.”

“Good grief, there you go again. Since when does laughing and drinking need a special occasion?”

“My brother, didn’t I send a messenger with news?”

“Ah, that? I heard.”

Temur chewed noisily on a piece of meat as he continued.

“But don’t worry too much. We may be Khans now, but the grasslands are vast. We can’t do anything about what happens beyond our reach.”

Of course, Temur knew about it, too.

Scouts had occasionally gone missing, and there had been a few disturbances in the westernmost reaches of the grasslands.

But to Temur, it was nothing much.

Not enough to make him forget the indulgence of the moment.

“Come on, my ever-worried brother. Let’s empty our cups first, then talk.”

Temur laughed heartily and was about to offer Chinggen another drink when—

*Flap.*

A cold wind carrying sandy dust pushed open the entrance to the ger.
```

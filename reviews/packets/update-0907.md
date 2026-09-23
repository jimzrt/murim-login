<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0907.txt",
      "sha256": "6b5c51cbd5b83a41690e6392d99980598edfe35b54c67596e4bab78719661d8a",
      "bytes": 13314
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "0b58cdcc41a357b34c62e216af13e96431e5411332c12b481e9c7f1156b6c117",
      "bytes": 1144
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "15b7559bed5551ab89a765328d3f0a3fb2d8b907d46fb1c26625499fb4cab311",
      "bytes": 230936
    },
    {
      "path": "characters/Baek Yeon.md",
      "sha256": "b41303338cd05bde551c7e831ca4f955dfb277d1d696ef76feaf31b65b8bd145",
      "bytes": 837
    },
    {
      "path": "characters/Cang Gong.md",
      "sha256": "5c080557e1682f497d915f9699a723e2e2c0609c8270e8fb3eb08555310f7d54",
      "bytes": 739
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "9724d5f1c5cb35fd4a7eecd0e32262813c423765349cb46397af377011575953",
      "bytes": 759
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "2c8288d53f2e3b5dd5e66aa180bb1e2b5b6fded7e62254264504f13a68e1ae88",
      "bytes": 1445
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "7330d6960f603be01a127dd6e0d29f820089ae69082add3606eb9c2f1ee8c8e0",
      "bytes": 1499
    },
    {
      "path": "characters/Jeong Hogun.md",
      "sha256": "65d26cc4faf55b70586551f1fe0a34bceb0895a54d90ed9274cfd7bec7ec70aa",
      "bytes": 628
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "e90dcb791321290487c16a2d8be523fd2ec8b39fc2cb5fd939c5608210d64c53",
      "bytes": 1372
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "22b8a5fd3fc72e5b85e2a7f0d2273b12b909ac32527de83cecc7c8c6755ba024",
      "bytes": 622
    },
    {
      "path": "characters/Jung Ho.md",
      "sha256": "2bda1f52ef3f288db86d6f40556e98307b40a7f81ef4bab5d506f1024fc73b69",
      "bytes": 699
    },
    {
      "path": "characters/Ma Sanbao.md",
      "sha256": "889c092571d3c3fa42ca9c2310651f477a8b0afe69bdf4e8dd7c9fe137b49489",
      "bytes": 1002
    },
    {
      "path": "characters/So Gyo.md",
      "sha256": "9ab44163e81276790668d169f3002d2dba34bbb328ba97343b2e599b06a54c01",
      "bytes": 900
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "c336a9b74793e3bf73bdc6e4d5a7447e62c84594f5d5258f730ffe7383f34d3d",
      "bytes": 262942
    }
  ],
  "estimated_tokens": 12779
}
-->

# Durable State Update — Chapter 907

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
1 and safe_through 907. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 907. Profile updates may replace only one
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
  "chapter": 907,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 907,
    "continuity_sources": [907],
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
    "Ma Sanbao was Cang Gong's disciple and was killed by Jin Taekyung during the banquet-hall battle.",
    "Taekyung is badly injured, his hands severely damaged and his internal energy depleted.",
    "Jeok Cheongang is fighting Cang Gong, now called the Eastern Heaven Demon Lord.",
    "The banquet-hall battle continues as the Emperor and So Gyo remain on the sidelines.",
    "Ma claimed the Emperor used Taekyung and Jeok Cheongang to eliminate So Gyo; this remains unconfirmed.",
    "So Gyo's identity and allegiance remain unknown.",
    "Silent figures have appeared near Hyuk Mujin's group on the way to the Jiangsu–Zhejiang border."
  ],
  "continuity_sources": [
    906
  ],
  "open_questions": [
    "Who is So Gyo, and where does her allegiance lie?",
    "What is the nature of Cang Gong's power and his relationship to the Lord of Heaven?",
    "Why are the Emperor and So Gyo staying out of the battle, and is Ma's claim that the Emperor used Taekyung true?",
    "Who are the silent figures surrounding Mujin's group?"
  ],
  "safe_through": 906,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 삼성     | **Three Saints**    |
| 태원진가   | **Jin Family of Taiyuan**        |
| 무림맹    | **Murim Alliance**               |
| 암천     | **Dark Heaven**                  |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 시스템              | **System**                     |
| 체력               | **Stamina**                    |
| 태원     | **Taiyuan**            |
| 백연 | **Baek Yeon** | Commander of the Embroidered Uniform Guard. |
| 창공 | **Cang Gong** | The bedridden East Depot leader for whom Ma Sanbao acts. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 정호군 | **Jeong Hogun** | Commander of the Embroidered Uniform Guard force confronting Jin. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 정호 | **Jung Ho** | Middle-aged Shaolin martial monk leading the traveling group. |
| 마삼보 | **Ma Sanbao** | The East Depot’s Brush-Holding Eunuch and second-in-command. |
| 소교 | **So Gyo** | The palace attendant leading the group assigned to serve Prince Shangshan. |
| 화염신장 | **Flame Divine Palm** | Jopil's deadly palm technique, noted when Taekyung compares Jopil with Mukyung. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 개방 | **Beggars' Sect** | Murim organization counted among the Nine Sects and One Gang. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 천주 | **Lord of Heaven** | Authority invoked by the masked attackers. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 살수 | **assassin** | Professional killer considered as a possible suspect. |
| 중단전 | **Middle Dantian** | Martial energy center opened by Jin during the battle. |
| 화룡각 | **Fire Dragon Pavilion** | New name chosen for Taekyung's pavilion. |
| 궁인 | **palace attendant** | Former Inner Palace attendant expelled by Baeksang. |
| 초일류 | **Supreme First Rate** | Realm attained by each Baekcheon Unit member. |
| 애향 | **Aehyang** | The City Lord’s favored concubine. |
| 금의위 | **Embroidered Uniform Guard** | Imperial guard force mentioned by Hong Jin. |
| 동창 | **East Depot** | Imperial agency named by Hong Jin. |
| 건청궁 | **Qianqing Palace** | The Emperor's palace, where Baek Yeon meets him. |

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
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 정호 | 진태경 | Shaolin Discipline Hall Master to patient and Benefactor | Benefactor Jin | formal-polite | Jung Ho repeatedly uses 진 시주 and 시주. |
| 진태경 | 정호 | patient to Shaolin Discipline Hall Master | Monk | polite and familiar | Taekyung addresses Jung Ho as 스님. |
| 혁무진 | 조장님 | pavilion_member_to_squad_leader | Captain | deferential and dubious | Mujin questions whether the pasture should be called the Nanman Ranch instead of the Nanman Beast Palace. |
| 진태경 | 정호군 | young martial artist to senior imperial officer | Commander Jeong | casual and teasing, then conciliatory | Jin addresses him by rank while trying to defuse the standoff. |
| 백연 | 정호군 | commander to subordinate | you | direct and commanding | Uses 네 while testing Jeong Hogun’s obedience. |
| 진태경 | 백연 | young martial artist confronting an imperial military commander | you | casual and insulting | Refers to Baek as 이 양반 while challenging his conduct. |
| 진태경 | 황제 | guest of the Emperor’s younger brother addressing the Emperor | Your Majesty | formal and deferential in address, despite blunt challenges | Taekyung repeatedly addresses the Emperor as 폐하. |
| 소교 | 진태경 | palace attendant addressing a martial artist and guest under escort | Young Master Jin | formal and respectful, but firm | Addresses him as 진 공자 while escorting him and warning him not to investigate. |
| 진태경 | 소교 | palace attendant and martial artist under imperial scrutiny | you | formal-polite, controlled and challenging | Taekyung addresses So Gyo as 당신 while questioning her presence and demanding an explanation. |
| 백연 | 진태경 | imperial commander confronting a young martial artist | Jin Taekyung | measured and familiar, using 자네 | Baek Yeon cautions Taekyung about his words and asks whether he must cause a scene. |
| 소교 | 백연 | political ally addressing a senior military commander | you | informal and direct | So Gyo uses 당신 and speaks without formality; no personal name or title is established. |
| 백연 | 소교 | military commander addressing a powerful political ally | you | formal and deferential | Baek Yeon uses 그대 while questioning So Gyo; she speaks without formality, which he accepts as her due. |
| 마삼보 | 정호군 | East Depot de facto leader to Embroidered Uniform Guard Thousand Captain | Commander Jeong | courteous and controlled | Ma Sanbao addresses him as 정 천호 while asserting procedural limits and drawing him into a conversation. |
| 정호군 | 마삼보 | Embroidered Uniform Guard Thousand Captain to East Depot official | Eunuch Ma | formal and guarded | Jeong Hogun addresses him as 마 태감 and shows wariness despite his restrained replies. |
| 마삼보 | 진태경 | political ally recruiting a young martial artist | you; my friend | courteous and familiar | Ma uses 자네 and 이보게 while explaining his choice of Jin and inviting him to join the restoration army. |
| 진태경 | 마삼보 | young martial artist addressing the East Depot’s Brush-Holding Eunuch and prospective ally | you; Brush-Holding Eunuch | polite and direct | Jin asks Ma why he withheld information and presses him for a clear answer; he refers to him as 태감. |
| 황제 | 진태경 | Emperor addressing a subject and Prince Shangshan’s guest | Jin Taekyung | formal and authoritative | The Emperor addresses Taekyung by his family and personal name before asking what to do with the two officials. |
| 적천강 | 창공 | hostile opponents | you; you bastard | blunt and threatening | Jeok Cheongang uses 네놈, 이 불알 없는 놈, and 호로새끼 while taunting Cang Gong. |
| 창공 | 적천강 | hostile opponents | Fire King Jeok Cheongang | taunting and sardonic | Cang Gong names Jeok by his title, then comments on how alike master and disciple are. |
| 황제 | 소교 | Emperor questioning a political ally | you | quiet and direct | The Emperor questions So Gyo through Sound Transmission about why she is only watching. |
| 소교 | 황제 | political ally answering the Emperor | Your Majesty | calm and direct | So Gyo answers the Emperor through Sound Transmission without wavering. |

## Listed compact profiles

### Baek Yeon.md

# Baek Yeon (백연)

- **Safe through:** Chapter 905
- **Aliases:** Blood Envoy
- **Role:** Baek Yeon is the Commander of the Embroidered Uniform Guard, a former martial arts instructor to the Crown Prince, and the Blood Envoy who helped the fourth prince seize the throne and led the purge.
- **Personality:** Politically assured and controlled, he enforces authority with ruthless decisiveness but speaks with striking defiance to the Emperor in private when their shared undertaking is at stake.
- **Voice:** Not established
- **Relationships:** He commands the Embroidered Uniform Guard and serves the Emperor, carrying out the late Emperor’s final command to plan for the future alongside the fourth prince; he treats Taekyung as a dangerous potential obstacle.

### Cang Gong.md

# Cang Gong (창공)

- **Safe through:** Chapter 906
- **Aliases:** None
- **Role:** Cang Gong is a formidable martial artist who has taken the bestowed title Eastern Heaven Demon Lord and intends to take Jin Taekyung to the Lord of Heaven for recruitment.
- **Personality:** Calculating and self-assured, he admires Taekyung's ability while believing the Lord of Heaven's power will make him submit.
- **Voice:** Dry and sardonic, he delivers taunts and judgments in measured statements.
- **Relationships:** He serves the Lord of Heaven, recalls a former master and fellow disciples as family, and is Ma Sanbao's master; he regards Jin Taekyung as a potential recruit.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 906
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 903
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and an active member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented; despite being naturally fearful, he faces danger and remains loyal to the person he serves, with irreverent self-deprecation and a taste for glory. He is suspicious of Taekyung, bluntly critical of the family's disgraced third son, and an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; with Taekyung, blunt and occasionally incredulous, while using breezy, irreverent banter to defuse tense situations.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad; he regards Taekyung as the person who has repeatedly saved him and now believes he may be able to save Taekyung in turn. As a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Fire Dragon Pavilion members accompanying Taekyung. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 906
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm, the occupant of the chief seat of the Murim Alliance's Five Kings Hall, and a trusted confidant who accepts Jin as himself despite knowing that he travels between Murim and another world resembling the realm of immortals.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; believes there is no absolute justice and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He deeply trusts Jin Taekyung, his publicly acknowledged Disciple and intended heir, regards him as the light of his later years, and will stand by him whatever path he chooses; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and remains Peng Cheolhu's rival.

### Jeong Hogun.md

# Jeong Hogun (정호군)

- **Safe through:** Chapter 890
- **Aliases:** None
- **Role:** Jeong Hogun is a Thousand Captain of the Embroidered Uniform Guard and a highly skilled martial artist whose force includes dozens of Peak masters.
- **Personality:** Disciplined and resolute, he follows imperial orders without hesitation and reads the political consequences of events with care.
- **Voice:** Formal and rigid, emphasizing duty to imperial authority.
- **Relationships:** Jeong Hogun serves under Baek Yeon’s command in the Embroidered Uniform Guard.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 906
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader.
- **Personality:** Hungry, self-aware, dryly observant, and pragmatic under pressure; accepts extreme personal risk when duty and the lives of others demand it.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; Ma Sanbao recruited Jin and Jeok for the restoration effort supporting Prince Shangshan, but their alliance is now in question after Ma confronted Jin during the banquet-hall battle.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 906
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Jung Ho.md

# Jung Ho (정호)

- **Safe through:** Chapter 890
- **Aliases:** None
- **Role:** Middle-aged Shaolin martial monk and Master of Shaolin's Discipline Hall who leads the traveling group and wields a Zen staff hung with prayer beads.
- **Personality:** Humble, observant, principled, and concerned with the safety of commoners.
- **Voice:** Formal, restrained, and admonitory, with Buddhist phrasing.
- **Relationships:** Unnamed is his young Martial Uncle; he leads the Shaolin monks traveling with him, addresses Sama Pyo as a Benefactor, and is recognized by Jin Taekyung as Park Jung Ho, a former Garam Middle School classmate.

### Ma Sanbao.md

# Ma Sanbao (마삼보)

- **Safe through:** Chapter 906
- **Aliases:** None
- **Role:** Ma Sanbao was the East Depot’s Brush-Holding Eunuch and a Supreme Peak martial artist who secretly led a restoration effort for Prince Shangshan and served as disciple of the Eastern Heaven Demon Lord.
- **Personality:** He is vigilant and patient, concealing his loyalties while awaiting the moment to act for the late Emperor.
- **Voice:** He speaks in measured, courteous language and uses calm repetition, feigned agreement, and procedural reminders to steer conversations while keeping sensitive details guarded.
- **Relationships:** Ma Sanbao was a longtime friend and former East Depot cohort of Hong Jin, led the restoration effort for Prince Shangshan, and recruited Jin Taekyung and Jeok Cheongang as allies; Jin killed him during the banquet-hall battle after Ma revealed his allegiance to his master, the Eastern Heaven Demon Lord.

### So Gyo.md

# So Gyo (소교)

- **Safe through:** Chapter 906
- **Aliases:** None
- **Role:** A palace attendant assigned to Prince Shangshan who is a Supreme Peak master and has a mission to keep Jin Taekyung alive; her identity and allegiance remain unconfirmed.
- **Personality:** Calm, calculating, and self-possessed; she conceals her strength and identity and can be openly taunting.
- **Voice:** Measured and composed, shifting from deferential formality to casual, pointed taunts and threats.
- **Relationships:** She poses as the leader of the palace attendants assigned to Prince Shangshan and is Jin Taekyung’s opponent, yet believes he may be the person she seeks and the person foretold by “that person”; she says only she and the Emperor know a secret she withheld from Baek Yeon, while her true allegiance remains unknown.

## Korean source

```text
＃907화



마삼보와의 전투가 그 어느 때보다 치열하고 힘들었다는 말은 하지 않겠다.

내가 지금껏 헤쳐 지나온 수라장 속에서, 놈보다 훨씬 더했던 강적들은 지금 당장 헤아려 보더라도 몇 명이나 더 있었으니까.

그러나 한 가지 분명한 사실은, 오늘의 마삼보가 나보다 강했다는 것이다.

‘아니, 정확히는 내가 평소보다 약했던 거겠지.’

시스템은 사실상 봉인당한 것이나 다름없었고, 일섬의 여파로 망가진 몸은 뜻대로 움직여 주지 않았다.

하지만 그럼에도 불구하고, 지금 이 순간 두 다리로 서 있는 것은 바로 나였다.

약육강식(弱肉强食)의 법칙이 지배하는 이 비정한 세상에서, 마삼보가 저지른 실수는 사소했지만 치명적이었다.

자신 스스로를, 나보다 한 수 위의 강자로 착각했다는 것.

“날 사로잡을 생각이었으면…… 처음부터 죽일 각오로 덤볐어야지.”

나는 공허해진 마삼보의 눈을 들여다보며 속삭였다. 그리고 놈의 목줄기를 관통한 단창을 더욱 깊숙이 밀어 넣었다.

퍼걱, 콰드득.

섬뜩한 소리와 함께 살갗을 뚫고 튀어나오는 뼛조각.

정확히 경동맥(頸動脈)을 끊고 쇄골을 따라 심장 어림까지 밀어 넣은 뒤에야 단창에서 손을 뗐고, 그제야 비로소 자유를 되찾은 마삼보의 몸뚱어리는 천천히 기울었다.

마치 나무 뿌리처럼 몸속 깊숙이 심어진 단창 한 자루와 함께.

쿵, 철벅.

비록 적을 처치했다는 시스템 메시지도, 특유의 맑은 종소리도 없었지만 이것으로 충분하다.

‘드디어 한 놈.’

피 웅덩이에 잠긴 채 미동도 하지 않는 시체를 바라보며 숨을 헐떡이던 나는, 공력을 실은 외침을 토해 냈다.

“태원진가의 진태경이, 동창 병필태감 마삼보를 죽였다!”

그리고 그 외침의 의미를 모두가 이해하기도 전에, 창칼이 난무하는 전장으로 뛰어들었다.

쉭, 퍼걱!

움직임은 짧고 간결하게. 최소한의 공력만을 담아서.

피하고, 때리고, 부쉈다.

콰직!

천상천하 만마앙복. 이제는 듣는 것만으로도 지긋지긋한 그 여덟 글자를 주문처럼 중얼거리던 놈의 안면을 으스러트린 순간.

쐐애액!

형체를 알아볼 수 없을 만큼 망가진 이목구비와 함께 허물어지는 시체의 좌우로 날아드는 칼날을 피해 고개를 틀었다.

캉!

한 뼘 차이로 스쳐 지나간 두 개의 칼날이 서로를 향해 부딪친다. 나는 귓가로 전해지는 진동을 무시하며 갈기갈기 찢어진 손아귀를 뻗었다.

퍼엉!

뜨겁게 달아오른, 압축된 공기가 터져 나간다.

고작 삼성(三成)의 공력을 담아 펼친 화염신장이었지만, 그 일장에 실린 힘과 열기는 어지간한 절정 고수조차 단번에 절명시킬 만한 위력을 지니고 있었다.

“커헉……!”

검붉은 핏물을 흩뿌리며 튕겨 나가는 신형.

하지만 저 이름 모를 적의 생사(生死)는 이미 내 관심을 떠났다. 그가 남긴 다른 무언가라면 모를까.

턱.

이미 주인의 손아귀를 빠져나간 검자루를, 나는 부드럽게 잡아채는 동시에 휘둘렀다.

쏴아아악!

공간이 갈라진다. 검신을 휘감은 화염이 대기를 달구고 살과 뼈를 태운다.

단순하지만 쾌속하게. 동시에 막을 수 없을 만큼 강하게.

그리고 그 끝에, 적들의 피와 비명이 있었다.

푸화악!

“크아악!”

나는 분수처럼 뿜어져 나오는 핏물을 뒤집어쓰며 전진했다. 사방에서 들이닥치는 무수한 날붙이의 파도를 피하고, 튕겨 내고, 이내 고스란히 되돌려 주었다.

검이 부러진다면 창으로. 창이 꺾인다면 도끼와 비수로.

그것마저 없다면 강철보다 단단한 팔과 다리로.

으드득!

꽈앙!

막아서는 모든 적들의 뼈를 부수고 살을 짓이겼다.

그 과정에서는 만류귀종(萬流歸宗)이라는 거창한 단어까지 꺼낼 필요도 없었다.

세상의 모든 병장기는 보다 효율적인 전투를 위해 탄생된 것이고, 무공의 존재 이유 역시 마찬가지였으니까.

찌르고, 베고, 타격하고.

내가 정의한 무공이란 수많은 점(點)과 선(線)의 연결이다.

목숨을 걸었다면 수단과 방법을 가리지 않아야 한다.

가장 빠르고 확실하게 적을 죽일 수 있다면 병장기의 형태는 중요치 않다.

바로 지금처럼.

콰드드득!

기이한 각도로 목이 꺾인 시체가 허물어진다.

죽이고 또 죽여도 끝없이 앞을 가로막은 적들의 입술은 쉴 새 없이 주문 같은 단어를 읊조리고 있었지만, 나는 놈들의 눈동자에 떠오른 감정을 느낄 수 있었다.

‘두려움.’

후욱, 후.

나는 흘러나오려는 거친 숨소리를 애써 억눌렀다. 전신의 근육이 감전된 것처럼 욱신거렸고, 마삼보의 검을 붙잡았던 손은 이제 고통조차 제대로 느껴지지 않았다.

그런 미친 짓을 벌였으니, 아마도 끔찍한 꼴이 되어 있겠지.

하지만 조금이라도 약한 모습을 보여서는 안 된다.

무리 지어 사냥하는 늑대들은 아무리 굶주려도 포효하며 달려드는 사자에게는 이빨을 드러내지 못한다.

놈들이 사자의 목덜미에 이빨을 박아넣으려 하는 것은, 그 사자가 뒷걸음질 쳤기 때문일 것이다.

철벅.

무겁게 앞으로 내디딘 발걸음에, 발목까지 고여 버린 핏물이 출렁인다.

어느덧 내 몸 곳곳에 아로새겨진 크고 작은 상처들에서 흘러나오는 그것처럼, 밤에 비친 핏물은 검붉었다.

‘할 수 있을까.’

나는 문득 극심한 피로를 느꼈다.

어림잡아 일백은 넘게 쳐 죽였음에도 시야를 가득 메운 적들이 보인다.

최소 초일류에서 절정의 끝자락까지 도달한 대국의, 아니 암천의 정예들.

개개인의 무위는 물론, 광신도처럼 천주를 섬기는 저들을 모두 쓰러트려야만 그곳으로 향할 수 있다.

아직도 끝나지 않은, 어쩌면 끝없이 이어질 것만 같은 경천동지(驚天動地)의 전투를 이어 가고 있는 적천강의 곁으로.

‘빌어먹을.’

모르겠다.

황제의 도움 없이도 승기(勝機)를 잡아가고 있는 이 와중에도, 왜 가슴 한구석이 불안하게 떨리는지.

먹구름 가득한 밤하늘이 왜 저렇게 불길하게 느껴지는지.

아니, 사실은 알고 있었다.

‘이 정도로 끝이 아니야.’

아무리 고개를 돌려도 보이지 않는다. 황제의 곁을 지켜야 할 살수들이, 건청궁의 수문장 역할을 하던 두 쌍둥이 초절정 고수도.

심지어 이 대연회장에 있는 금의위의 숫자조차 내가 아는 것의 절반밖에 되지 않는다.

‘그리고 그건 창공 역시 마찬가지지.’

황제와 창공.

더는 돌이킬 수 없는 강을 건넌 두 사람은 아직 모든 전력을 드러내지 않았다. 자신의 수를 감추고, 상대가 먼저 수를 내보이길 기다리고 있는 것이 틀림없다.

설령 지금쯤 황도 전체가 절반으로 나뉘어 피 튀기는 혈전을 벌이고 있다고 해도, 나는 놀라지 않을 자신이 있었다.

‘시발.’

개 같은 일이다.

하지만 그럼에도, 나는 싸워야 했다.

살아남아야 했다.

폭우처럼 쏟아져 내리는 화살 비 아래에서 달려드는 암천의 개들에게서도. 그리고 적인지 아군인지조차 모를 황제와 소교에게서도.

‘도대체 무슨 꿍꿍이냐.’

나는 고개를 돌려 저 멀리 높게 세워진 연단을 바라보았다.

백연과 소교.

단번에 이 전황을 뒤집을 수 있는 두 초절정 고수를 좌우로 거느린 채, 전장을 주시하고 있는 황제의 모습이 보였다.

몇 안 되는 궁인들에게 둘러싸여 있는 애향과 어째서인지 무릎을 꿇고 있는 어린 왕의 모습도 함께.

그리고 그런 그들의 모습에 잠시 시선을 빼앗긴 그 순간, 하늘을 가로지른 무수한 파공성이 뒤늦게 귓가를 파고들었다.

쉬쉬쉬쉬쉭!

머리 위로 드리워지는 짙은 어둠.

오직 나 한 사람만을 노리고 쏘아진 수백여 개의 화살촉이 번뜩인 동시에, 머릿속에 든 붉은색 경종이 세차게 울렸다.

‘젠장.’

움직이기도 전에 알 수 있었다.

저 화살들을 전부 피하는 건 불가능에 가깝다는 것을.

이미 나는 지쳤고, 육신과 감각은 굼떠졌으며, 일류 고수들이 공력을 실어 쏘아낸 저 수많은 화살을 모조리 피하기에는 너무나도 개방된 공간에 동떨어져 있었다.

‘최소한의 힘을 이용해서, 치명상만 피하는 수밖에.’

이를 악문 나는 바닥에 꽂혀 있던 주인 잃은 창을 뽑아 드는 동시에, 남은 한 손으로 하늘을 향해 손을 뻗었다.

우우웅.

주위를 에워싼 공기가 파르르 떨린다.

최대한 체력을 아끼기 위해 전투 중에도 아주 위험한 상황이 아닌 경우에는 사용을 자제해 왔던 중단전(中丹田)이었지만, 지금은 쓰고 달고를 가릴 때가 아니었다.

써도 삼켜야 한다.

스스로 감내해야 한다.

고작 여기에서 허무하게 쓰러질 생각은 추호도 없었으니까.

그리고 귓가를 찢는 듯한 맹렬한 파공성과 함께 날아드는 화살을 향해 주먹을 그러쥐려던 그 순간.

“귀갑(龜甲)! 방(防)!”

어딘지 모르게 익숙한 누군가의 외침과 함께, 섬광 같은 속도로 들이닥친 일단의 무리가 주위를 에워쌌다.

커다란 방패를 앞세운 채.

터터터텅!

불똥이 어둠 속을 선명히 밝힌다. 꺾이고 부러진 무수한 화살 파편이 사방으로 비산했고, 약간의 시간 차를 두고 들이닥친 두 번째 화살비를 향해 수십여 개의 언월도(偃月刀)가 번뜩였다.

“참(斬)!”

쉬쉬쉬슁, 서걱!

반월의 형태로 뻗어 나간 도기(刀氣)가 화려하게 하늘을 수놓았다.

일종의 막을 형성한 그 강력한 기운은 쏘아진 화살들을 모조리 베어 부수었고, 조각 조각난 파편들은 그들이 걸친 황금빛 갑옷의 틈새를 파고들 수 없었다.

촤륵, 투두두둑!

힘을 잃고 떨어지는 무수한 파편들.

그 광경을 말없이 바라보던 나는, 깊게 눌러쓴 투구 아래로 보이는 익숙한 얼굴을 향해 입을 열었다.

“이거, 고맙다고 해야 하나?”

금의위 천호. 정호군이 담담하게 대꾸했다.

“고맙다는 말도 할 줄 알았나?”

“사실 자주 하는 편은 아니지.”

“그럴 것 같았다. 물론 애초부터 기대도 안 했지만.”

“그러는 넌?”

“빚을 진 경우라면 고맙다고 하는 편이지. 지금처럼.”

철컥.

정호군이 황금빛 갑주를 두드리는 군례(軍禮)와 함께 말을 이었다.

이제까지와는 다른, 정중한 말투로.

“고맙소. 폐하를, 우리를 도와줘서.”

“……허.”

“묻고 싶은 말도, 하고 싶은 말도 많겠지. 하지만 그 일은 모든 것이 끝난 뒤로 미뤄 뒀으면 하오.”

빌어먹을.

말도 꺼내기 전에 이런 식으로 나온다면 할 말이 없어진다.

작게 혀를 찬 나는, 사방에서 들이닥치는 적들을 응시하며 입을 열었다.

“야, 하나만 묻자.”

“무엇이든지.”

“저기서 관음 중인 저 인간, 아군은 맞냐?”

관음이라는 단어에서 움찔한 정호군이 고개를 끄덕였다.

“적어도 황제 폐하께서는, 그렇소. 우린 아군이오.”

적어도?

구태여 앞에 붙인 그 세 글자의 의미를, 나는 즉각 알아차렸다.

‘소교는 아니라는 거군. 아니, 정확히는 이놈도 모르는 거겠지.’

틀림없다.

이제는 산 사람이 아니게 된 마삼보도, 심지어 창공조차도 모르는 듯했으니까.

정체를 알 수 없는 저 여자가, 도대체 누구이며 어떤 생각을 품고 있는지.

그리고 이처럼 알려지지 않은 불확실성은, 곧 위험을 의미한다.

‘……시바. 애들 떼놓고 오길 잘했네.’

내심 중얼거린 나는 조금 전 손에 넣은 주인 없는 창을 들어, 물밀듯이 밀려오는 적들을 향해 겨누었다.

지금쯤 오지 않을 무림맹의 원군을 기다리며, 안전한 곳에서 머무르고 있을 화룡각 대원들을 떠올리며.

나중에야 앵무새처럼 조장님을 외치며 난리를 피우겠지만, 그래도 여기에 남아 있었다면 진작 죽었어도 이상하지 않았을…….

“조장니임!”

“……?”

“조장니이이임!”

뭐여, 시벌.

마치 귀신에 홀린 듯한 기분으로 돌아선 나는, 저 멀리서 모습을 드러낸 익숙한 얼굴들을 발견했다.

“조장니이이이임!”

정확히는 화룡각 대원들의 선두에서 고래고래 외치는 혁무진과.

두두두두두!

그 뒤를 꼬리처럼 달라붙은 무수한 검은 인영들을.
```

## Final English reading copy

```markdown
# Chapter 907

I won’t say the fight with Ma Sanbao was fiercer and more difficult than any I’d ever fought.

There had been plenty of stronger opponents in the hellish battlefields I’d fought my way through. Even now, I could name several who’d been far worse than him.

But one thing was certain: today, Ma Sanbao had been stronger than me.

*No. More precisely, I was weaker than usual.*

The System was practically sealed, and my body—wrecked by the aftereffects of One Annihilation—wouldn’t move the way I wanted it to.

And yet, at this very moment, I was the one standing on two feet.

In this merciless world ruled by the law of the jungle, Ma Sanbao had made a mistake. A small one, but a fatal one.

He’d mistaken himself for someone a step above me.

“If you wanted to take me alive… you should’ve come at me ready to kill me from the start.”

I whispered as I looked into Ma Sanbao’s hollow eyes. Then I drove the short spear through his throat even deeper.

*Squish. Crack.*

Bone fragments burst through his skin with a sickening sound.

Only after the spear had severed his carotid artery and slid along his collarbone to somewhere near his heart did I let go. At last free of my grip, Ma Sanbao’s body slowly tilted over.

Along with the spear buried deep in him like a tree root.

*Thud. Splash.*

There was no System message saying I’d defeated an enemy. No clear, familiar chime, either.

But this was enough.

*Finally. One down.*

I stared at the corpse lying motionless in a pool of blood, panting, then let out a shout charged with internal energy.

“Jin Taekyung of the Jin Family of Taiyuan has killed Ma Sanbao, Brush-Holding Eunuch of the East Depot!”

Before anyone could even grasp what that shout meant, I charged back into the battlefield, where swords and spears clashed.

*Whoosh! Thud!*

Short, simple movements. Only the bare minimum of internal energy.

I dodged, struck, and smashed.

*Crack!*

The face of a man muttering those eight words like a mantra—“Heaven above, earth below. All demons bow in reverence”—caved in.

*Whsssh!*

I jerked my head aside, avoiding the blades that flew in from both sides of the collapsing corpse, its features mangled beyond recognition.

*Clang!*

The two blades that had missed me by a hand’s breadth struck each other. Ignoring the vibrations reaching my ears, I thrust out my hand, its grip torn to ribbons.

*Boom!*

Compressed air, heated until it glowed, burst outward.

The Flame Divine Palm I unleashed held only three-tenths of my internal energy. Even so, the force and heat packed into that palm strike were enough to kill all but the most exceptional Peak masters on the spot.

“Gah—!”

The man’s body flew backward, spraying dark red blood.

But whether that nameless enemy lived or died was no longer my concern. What he’d left behind was another matter.

*Tap.*

The sword had already slipped from its owner’s grasp. I caught the hilt smoothly and swung it in one motion.

*Shhhh!*

Space split open. Flames coiled around the blade, scorching the air, flesh, and bone.

Simple, but fast. And so powerful it couldn’t be stopped.

At the end of it were the enemies’ blood and screams.

*Fwoosh!*

“Gaaah!”

I pushed forward, drenched in blood spraying like a fountain. I dodged the countless blades crashing in from every direction, knocked them aside, then sent them flying right back where they came from.

When the sword broke, I used a spear. When the spear snapped, I used an ax or a dagger.

If I had nothing else, I used arms and legs harder than steel.

*Grit!*

*Boom!*

I broke the bones and crushed the flesh of every enemy in my way.

There was no need to reach for some grand concept like all streams returning to the sea.

Every weapon in the world had been made to fight more efficiently. Martial arts existed for the same reason.

Stab. Slash. Strike.

To me, martial arts were a chain of points and lines.

If your life was on the line, you used every means at your disposal.

If it could kill the enemy as quickly and reliably as possible, the shape of the weapon didn’t matter.

Just like now.

*Cr-rack!*

A corpse collapsed, its neck bent at an unnatural angle.

The enemies kept pouring in, their lips endlessly murmuring those mantra-like words, no matter how many I killed. But I could see the emotion rising in their eyes.

*Fear.*

*Huff. Huff.*

I struggled to suppress my ragged breathing. Every muscle in my body throbbed as if I’d been electrocuted, and the hand that had gripped Ma Sanbao’s sword could barely feel pain anymore.

After pulling something that crazy, I was probably in terrible shape.

But I couldn’t show even the slightest weakness.

Wolves hunted in packs, but no matter how hungry they were, they couldn’t bare their teeth at a lion that roared and charged at them.

They only tried to sink their teeth into a lion’s nape when it started backing away.

*Splash.*

My heavy footstep sent the blood pooled around my ankles rippling.

Like the blood still seeping from the countless wounds carved into my body, the blood reflecting the night sky was dark red.

*Can I do this?*

Suddenly, I felt exhausted to my very bones.

I’d killed well over a hundred of them, by my rough count, and still the enemies filled my field of vision.

The Great Nation’s—no, Dark Heaven’s—elite troops. Every one of them was at least Supreme First Rate, some nearing the peak of Peak.

I had to defeat them all, every last fanatic who worshiped the Lord of Heaven, before I could reach Jeok Cheongang, who was still fighting a thunderous battle that seemed like it would never end.

*Goddammit.*

I didn’t know.

Even as we gained the upper hand without the Emperor’s help, why did one corner of my heart keep trembling with unease?

Why did that storm-clouded night sky feel so ominous?

No. I did know.

*This isn’t over.*

No matter how I looked, I couldn’t see them. The assassins who should have been protecting the Emperor. The twin Supreme Peak masters who’d served as the gatekeepers of Qianqing Palace.

Even the Embroidered Uniform Guards in this great banquet hall numbered only half as many as I knew to be here.

*And it’s the same for Cang Gong.*

The Emperor and Cang Gong.

The two men had crossed a point of no return, yet neither had revealed all their forces. No doubt they were holding back their cards, waiting for the other to make the first move.

Even if the entire imperial capital had split in two by now, locked in a bloody battle, I wouldn’t have been surprised.

*Fuck.*

This was a shitty situation.

But even so, I had to fight.

I had to survive.

I had to survive the Dark Heaven dogs charging at me beneath a rain of arrows—and the Emperor and So Gyo, whose allegiance I couldn’t even guess.

*What the hell are you planning?*

I turned my head and looked at the raised platform in the distance.

Baek Yeon and So Gyo.

The Emperor was watching the battlefield with those two Supreme Peak masters at his sides, each powerful enough to turn the tide of the battle in an instant.

I also saw Aehyang, surrounded by a handful of palace attendants, and the young king, kneeling for some reason.

For just a moment, my attention was drawn to them. Then the countless whistles that had crossed the sky belatedly reached my ears.

*Whoosh-whoosh-whoosh-whoosh!*

A thick darkness spread over my head.

Hundreds of arrowheads flashed as they fell, all aimed at me alone. At the same moment, a red alarm bell rang violently inside my head.

*Shit.*

I knew before I even moved.

Dodging all those arrows was next to impossible.

I was already exhausted. My body and senses had grown sluggish, and I was stranded in far too open a space to avoid every arrow shot by First Rate masters using their internal energy.

*I have to use as little strength as possible and avoid a fatal injury.*

I clenched my teeth, pulling an abandoned spear from the ground as I raised my remaining hand toward the sky.

*Whummm.*

The air surrounding me trembled.

I’d avoided using my Middle Dantian except in the most dangerous situations, even during battle, to conserve my stamina. But now wasn’t the time to be picky about what was bitter and what was sweet.

Even if it was bitter, I had to swallow it.

I had to bear it myself.

There was no way in hell I was going to fall here, of all places.

Just as I clenched my fist, ready to meet the arrows hurtling toward me with a ferocious whistle that seemed to tear through my ears—

“Shield formation! Defend!”

At a familiar shout from somewhere, a group rushed in at lightning speed and surrounded me.

They held up massive shields.

*Bam-bam-bam!*

Sparks lit up the darkness. Countless broken and splintered arrow fragments scattered in every direction. A second rain of arrows came moments later, and dozens of crescent-bladed polearms flashed toward them.

“Slash!”

*Whoosh-whoosh-whoosh! Slice!*

Blade Force spread across the sky in brilliant half-moons.

The powerful energy formed a kind of barrier, slicing apart every arrow that flew toward them. The scattered fragments couldn’t pierce the gaps in their golden armor.

*Clatter. Thud-thud-thud!*

Countless fragments lost their momentum and fell.

I watched in silence, then spoke to the familiar face beneath a helmet pulled low.

“Should I thank you for that?”

Jeong Hogun, Thousand Captain of the Embroidered Uniform Guard, answered without a hint of emotion.

“I didn’t know you knew how to say thank you.”

“I don’t do it very often.”

“I figured as much. I wasn’t expecting it in the first place.”

“What about you?”

“When I owe someone a debt, I say thank you. Like now.”

*Clank.*

Jeong Hogun struck his golden armor with a military salute, then continued.

His tone was different now. Respectful.

“Thank you for helping His Majesty. And us.”

“……Huh.”

“I’m sure you have plenty to ask me, and plenty you want to say. But I’d like you to save it until after this is over.”

Goddammit.

If he came out with something like that before I could even open my mouth, there was nothing left to say.

I clicked my tongue quietly and looked toward the enemies pressing in from all sides.

“Hey, let me ask you one thing.”

“Anything.”

“That guy over there playing peeping Tom—is he on our side?”

Jeong Hogun flinched at “peeping Tom,” then nodded.

“At least His Majesty is. We are on your side.”

*At least?*

I immediately understood why he’d gone out of his way to add that qualifier.

*So not So Gyo. No—more precisely, he doesn’t know, either.*

There was no doubt.

Even Ma Sanbao, who was no longer among the living, and Cang Gong seemed not to know.

Who that mysterious woman was, or what she had in mind.

And unknown variables like her meant danger.

*…Shit. Good thing I left the kids behind.*

I muttered to myself and raised the ownerless spear I’d picked up moments ago, aiming it at the enemies surging toward us.

I thought of the Fire Dragon Pavilion members who were probably waiting somewhere safe, expecting the Murim Alliance reinforcements that weren’t coming.

They’d probably make a huge fuss later, parroting “Captain” over and over. Still, if they’d stayed here, they’d have been dead by now. Or at least, it wouldn’t have been surprising if they were.

“Captain!”

“……?”

“Captaaaain!”

What the hell?

I turned around, feeling as though I’d been possessed by a ghost, and spotted familiar faces appearing in the distance.

“Captaaaaaain!”

More precisely, I saw Hyuk Mujin at the head of the Fire Dragon Pavilion members, hollering at the top of his lungs.

*Rumble-rumble-rumble!*

And countless black figures trailing behind him like a tail.
```

<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0578.txt",
      "sha256": "be818d98dbb8db858c73ac1f192cf43042fe39201f51eda5649cf1032bd64d87",
      "bytes": 14035
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "8b554b8fdcf4c567300e8d64fb793abf032af2f46b44b830d6d0e8a9678b6ecf",
      "bytes": 2091
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "979337dec45c6d24df237cb0ad58355d3ce4d797870bdd238aec038545cf3071",
      "bytes": 182422
    },
    {
      "path": "characters/Cheon Taemin.md",
      "sha256": "77f1e21cc537b500cc694817bb2a2ee495fc37502d78498687042a7d3be4372a",
      "bytes": 730
    },
    {
      "path": "characters/Cheonwoo.md",
      "sha256": "5de3bc620be42570ade9d17666493afec35e14cc4ffd45b4afbdcaccbfd280ac",
      "bytes": 590
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "d84e50a9bfad259c977f382a4b58a18487466a7db30ff21c6c9ac71c821929e2",
      "bytes": 553
    },
    {
      "path": "characters/Go Jun.md",
      "sha256": "663d2332fbf51f809b031db215e995f6e2b7cf0a74b9505cfd889deb9a52794b",
      "bytes": 976
    },
    {
      "path": "characters/Hwa-jong.md",
      "sha256": "ab0c79bcfca80e6543776894f7c4a2807283f3966fc3a7810df5c5f5c9127273",
      "bytes": 562
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "c23c27251ae62397af8b2381def0e68683ecc60b57de70bd32b978851941cb35",
      "bytes": 2280
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "db8faff2f413fa72d758ec9283dd132b4fde7869fd11bbaa3b15ccd050c97d6a",
      "bytes": 622
    },
    {
      "path": "characters/Kim Hwajong.md",
      "sha256": "40ce54cc2fc0cc5de277af61c58053acb9a7e4306243e083073baa5cbe62b0f4",
      "bytes": 536
    },
    {
      "path": "characters/Lee Jungryong.md",
      "sha256": "1078be1bf40e6edad8f6c8168d5ca63795ca29d72031da89f7fb5af539c9b6a6",
      "bytes": 1384
    },
    {
      "path": "characters/Song Cheonwoo.md",
      "sha256": "4afee18504ff64bc09f68bafbe65ae170dccae6e926707517bfc277e5777a2da",
      "bytes": 1076
    },
    {
      "path": "characters/Team Leader Choi.md",
      "sha256": "72b2c0d60b88c616b057282a8603a32f030bf6baa274aee7602ee3f0ad7d9204",
      "bytes": 894
    },
    {
      "path": "characters/Won Myunghoon.md",
      "sha256": "35c198c9bc5a75e50f33e6de6107b6925379bfa50517219e19dd570bbf96bc76",
      "bytes": 1760
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "4a5eddc3bae4d911d482b6b8d8dab4f2ad1d27d864cb7faeeb0aea4afb791a80",
      "bytes": 179227
    }
  ],
  "estimated_tokens": 12998
}
-->

# Durable State Update — Chapter 578

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 578. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 578. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history.
`names` contains only newly required Korean-to-English rows that are absent from
Exact glossary matches; Korean keys must occur in the source. Do not repeat
glossary matches. The controller drops rows already in the names ledger.
`address_pairs` contains only newly required speaker→addressee rows that are
absent from Matched address pairs. Speaker and addressee must be Hangul source
spellings such as 진태경 or 혁무진, never English names. Arabic digits are
allowed in titles such as 1팀장. At least one endpoint must occur in the source.
The controller drops pairs already in the address ledger. Do not invent
risk-register rows. Beat plot paragraphs are plain strings; continuity and
translation decisions are concise list items.
Return this exact shape:

{
  "chapter": 578,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 578,
    "continuity_sources": [578],
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
    "Song Cheonwoo says Cheon Taemin suddenly collapsed more than twenty years ago and has remained unconscious, but no one knows why.",
    "Song Cheonwoo and Lee Jungryong concealed Taemin's condition, waited two years, conducted experiments, and purged aides who knew the truth.",
    "Song survived by negotiating the European regional director position and saving his family.",
    "Hwa-jong was not told about Taemin's condition and remains loyal to Choi Minwoo.",
    "Song claims Taemin is still alive, but his location is unknown and Area A is only suspected.",
    "Choi Minwoo will verify the facts before seeking payment for Song's crimes.",
    "Song describes his disclosure as atonement for wrongs against Taemin and Choi.",
    "Hundreds of yetis are attacking across an avalanche beyond the crevasse.",
    "Busan's Kraken has been eliminated, but more than one thousand Mermen remain across Haeundae and Gwangalli while the Peace Guild and other forces contain the disaster.",
    "Song Cheonwoo warned Choi Minwoo that Go Jun is preparing a trap related to Choi's maternal grandfather.",
    "Song met Choi disguised by an illusion spell inside the Peace Guild-owned Yeti's Winter Range Gate in Pyeongchang."
  ],
  "continuity_sources": [
    577
  ],
  "open_questions": [
    "What caused Cheon Taemin's collapse, and what happened during his more than twenty years of unconsciousness?",
    "Is Cheon Taemin actually being kept in Area A of Ares Guild headquarters?",
    "What trap is Go Jun preparing, and can Song Cheonwoo's warning be trusted?",
    "Who empowered and released the Kraken, and did that person engineer the Monster Wave?",
    "Why did Song Cheonwoo choose this moment to reveal the truth to Choi Minwoo?"
  ],
  "safe_through": 577,
  "temporary_decisions": [
    "Use Green Garden for 녹지원.",
    "Use Yeti's Winter Range for 예티의 겨울 산맥.",
    "Use Stone King for 스톤 킹 and Skeleton King for 스켈레톤 킹.",
    "Use Area A for A구역.",
    "Use Hwa-jong for 화종."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 김화종    | **Kim Hwajong**   |
| 최민우    | **Choi Minwoo**   |
| 천태민    | **Cheon Taemin**  |
| 이정룡    | **Lee Jungryong** |
| 원명훈    | **Won Myunghoon** |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 살기     | **killing intent**                               |                                                       |
| 일격     | **One Strike**                         |
| 아이템              | **Item**                       |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 대격변     | **Great Cataclysm**   |
| 사천     | **Sichuan**            |
| 천우 | **Cheonwoo** | Name shown in a Level Window; one of the five current Five Gates scions. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 고준 | **Go Jun** | Personal name of Team Leader Seok; Lee Jungryong's prized Disciple. |
| 화종 | **Hwa-jong** | Butler Kim's personal name. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 송천우 | **Song Cheonwoo** | Ares Guild Director, former third-ranked Korean Hunter, and longtime European regional branch director. |
| 송이 | **Song-i** | Short form used for Song Song; Taekyung's love interest. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 와이번 | **Wyvern** | High-tier dragonkin monster. |
| 용족 | **dragonkin** | Monster classification including wyverns and drakes. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 준이 | **Jun** | Family nickname used in the form Jun's dad. |
| 석고준 | **Go Jun** | Source full-name form for the established Go Jun, also known as Team Leader Seok. |
| 도련님 | **Young Master** | Address used for Team Leader Choi by Butler Kim. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 예티 | **yeti** | Monster species in the Gate's name and raid dialogue. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 김화종 | 진태경 | senior_Hunter_to_younger_Hunter | Mr. Jin | formal-polite | Hwajong addresses Taekyung as 진태경 씨 while proposing an exchange of stories. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 진태경 | 원명훈 | younger_brother_to_older_friend | hyung | casual-but-junior | Taekyung asks Won to speak casually and adopts hyung after they establish a friendly younger-brother relationship. |
| 원명훈 | 진태경 | older_friend_to_younger_brother | Taekyung | casual-affectionate | Won calls Taekyung 태경아 and welcomes him as a good younger brother. |
| 이정룡 | 진태경 | senior S-rank Hunter to younger Hunter and adversary | Young man | polished, teasing, and veiled-threatening | Uses a genial tone and indirect threats while trying to make Taekyung release the captives. |
| 진태경 | 이정룡 | younger Hunter to senior S-rank Hunter and adversary | you | polite but mocking and defiant | Taekyung answers Lee's soft threats with the wolf-and-tiger metaphor and refuses to yield. |
| 이정룡 | 고준 | Master to Disciple | Go Jun | familiar and testing | Lee switches from Seok's office title to his personal name while considering whether he can defeat Taekyung. |
| 고준 | 이정룡 | Disciple to Master | Master | deferential | Go Jun responds to Lee's personal-name address as 스승님. |
| 이정룡 | 천태민 | younger_to_older_brother_by_choice | older brother | reverent and familiar; internal | Lee Jungryong uses 형님 in unspoken thoughts and regards Cheon Taemin as an older brother despite having no blood relation. |
| 석고준 | 최민우 | Ares security leader to rival Guild Master | Team Leader Choi Minwoo | formal but barbed | Uses 평화 길드 최민우 팀장님 while belittling Choi and blaming the Peace Guild for Taekyung's apparent death. |
| 진태경 | 석고준 | returning Hunter to hostile Ares security leader | you fucking bastard | hostile and profane | Taekyung directs his final insults and challenge at Go Jun after returning alive. |
| 석고준 | 진태경 | hostile_opponents | brat | hostile and overconfident | Go Jun addresses Taekyung internally as 애송아 while launching his full-strength attack. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 최민우 | 진태경 | trusted allied team leader to younger allied Hunter | Mr. Jin | formal-polite and concerned | Choi warns Jin about the danger of the operation and affirms his deep trust. |
| 진태경 | 최민우 | younger allied Hunter to allied team leader | Team Leader Choi | polite, familiar, and teasing | Jin jokes with Choi while acknowledging and dismissing his concern. |
| 고준 | 진태경 | Ares Guild combatant confronting the killer of his Master | you | hostile and informal | Go Jun uses 너 while demanding Jin confess to Lee Jungryong's death and threatening retaliation. |
| 진태경 | 고준 | dominant adversary confronting Lee Jungryong's Disciple | you | contemptuous and informal | Jin uses 너 and 놈 while overpowering Go Jun and ordering him to end the conflict with Lee Jungryong. |
| 송천우 | 석고준 | adversary; captor of Song's children | you | shocked and confrontational | Song reacts directly to Go Jun's admission that he took the children. |
| 화종 | 최민우 | butler_to_Young_Master | Young Master | formal and deferential | Butler Kim consistently addresses Choi Minwoo with the established deferential title. |
| 송천우 | 화종 | former_allies | Hwa-jong | familiar and informal | Song uses Hwa-jong's personal name, prompting Hwa-jong to reject the familiarity. |
| 화종 | 송천우 | former_allies_now_hostile | you | formal and cold | Hwa-jong challenges Song's right to expect Choi's trust and rejects their former intimacy. |
| 송천우 | 최민우 | older_former_ally_to_younger_former_ally | Minwoo | familiar and informal | Song addresses Choi by his given name while discussing the meeting place and surveillance. |
| 최민우 | 화종 | Young Master to butler | Butler Kim | formal and respectful | Choi refers to Hwa-jong as 김 집사님 while discussing the concealed truth. |
| 최민우 | 송천우 | temporary ally to rival | Regional Director | formal and cutting | Choi uses 지사장님 while condemning Song's survival and concealment. |

## Listed compact profiles

### Cheon Taemin.md

# Cheon Taemin (천태민)

- **Safe through:** Chapter 577
- **Aliases:** Slayer
- **Role:** Cheon Taemin is Ares Guild Master and the world's greatest Hunter, known as the Slayer for killing the Demon King and creating the first Mana Cultivation Method during the Great Cataclysm, and he is believed to remain alive after more than twenty years of unconsciousness, with Area A only suspected as his location.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** Maternal grandfather of Team Leader Choi and Jin Taekyung and father of Soyeong; regarded by Lee Jungryong as an older brother despite their lack of blood relation.

### Cheonwoo.md

# Cheonwoo (천우)

- **Safe through:** Chapter 577
- **Aliases:** None
- **Role:** One of the five current Five Gates of Shanxi scions and a First Rate martial artist present at Honghwa Inn.
- **Personality:** Pampered and contemptuous toward Cheongpung's group as part of the five scions' collective mockery.
- **Voice:** Mocking in the group's exchange; no distinct individual speech is established.
- **Relationships:** Associates with Seongryong, Myeonghwa, Sohye, and Jintae as a group of current Five Gates scions.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 577
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Go Jun.md

# Go Jun (고준)

- **Safe through:** Chapter 577
- **Aliases:** Team Leader Seok
- **Role:** Go Jun is Ares Guild's Vice Guild Master, Lee Jungryong's disciple and former Head of Security, and the de facto successor to Lee's Ares legacy who passed the S-rank Hunter qualification assessment with a very high score but lacks Lee's legitimacy.
- **Personality:** Disciplined and controlled under ordinary pressure, fiercely loyal to Lee Jungryong, but consumed by humiliation and rage when Ares Guild's authority is challenged.
- **Voice:** Dry, controlled, and formal with subordinates; deferential when addressing his Master.
- **Relationships:** Disciple and direct protégé of Lee Jungryong, Go Jun inherited Lee's Ares Guild legacy after his death, regards Jin Taekyung and Choi Minwoo as enemies seeking to take it away, and has seized Song Cheonwoo's children as leverage while calling it protection.

### Hwa-jong.md

# Hwa-jong (화종)

- **Safe through:** Chapter 577
- **Aliases:** Butler Kim
- **Role:** Hwa-jong is Choi Minwoo's loyal butler and personal escort.
- **Personality:** Loyal, vigilant, and uncompromising toward perceived threats to Choi Minwoo.
- **Voice:** Formal and deferential toward Choi Minwoo, cold and openly hostile toward Song Cheonwoo.
- **Relationships:** Hwa-jong serves Choi Minwoo and was formerly close to Song Cheonwoo, but their relationship ended over loyalty and ambition.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 576
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, a Supreme Peak master who possesses the Heavenly Martial Physique and superhuman physical strength, has manifested Force, opened his Middle Dantian, crossed the wall into true mastery, has achieved Three Flowers Gather at the Crown but not Five Qi Returning to Origin, can perceive the texture of qi well enough to sever layered magic, can resist high-level monster Fear through exceptional mental strength, is publicly recognized as an S-rank-level Hunter while formally retaining an A-rank license pending testing, can command coordinated raids against powerful monsters, serves as one of the two pavilion masters of the Alliance Leader's direct Fire Dragon Pavilion, leads its first mission to Nanman, and is the Peace Guild's wealthy patron in the modern world.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor and assigned him a final task to incorporate martial principles into his learned martial arts but declined Taekyung's recruitment after Cheongpung reached him first, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate, student, and trusted manager of media and official arrangements, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, and Xiao Shen regards him as an older brother after Jin saved him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 576
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Kim Hwajong.md

# Kim Hwajong (김화종)

- **Safe through:** Chapter 577
- **Aliases:** Butler Kim
- **Role:** Level 80 mage known as Butler Kim; former Class 3 instructor at the Hunter Training Center; arrives at the confrontation between Im Chunsoo and Jin Taekyung
- **Personality:** Gentle and composed
- **Voice:** Gentle and measured
- **Relationships:** Former instructor of Im Chunsoo, who remains terrified of and obedient to him; addresses Im Chunsoo familiarly as Chunsoo

### Lee Jungryong.md

# Lee Jungryong (이정룡)

- **Safe through:** Chapter 577
- **Aliases:** None
- **Role:** Former Vice Guild Master of Ares Guild, one of Korea's two S-rank Hunters, and a Supreme Peak-level martial artist who was killed by Jin Taekyung.
- **Personality:** Outwardly genial, calm, and humorous; calculating, opportunistic, manipulative, coercive, and ruthless when challenged
- **Voice:** Smooth, good-natured, and indirect, using teasing conversation and veiled threats before becoming openly furious
- **Relationships:** Master of Park Jihoon and Go Jun (Team Leader Seok), whom he personally selected and trained; longtime Great Cataclysm acquaintance of Park Tae Seop; adversary of Jin Taekyung; knew Team Leader Choi from childhood; has an antagonistic history with Kim Hwajong, who saved his life at the collapse of Mapo Bridge eighteen years earlier; was visibly shaken by learning that Choi is Cheon Taemin's maternal grandson; regarded Cheon Taemin as an older brother despite no blood relation and long held him in respect and fear; secretly supported the orphanage where Lee Dongseok grew up and was regarded by Dongseok as a father; operated as Ares Guild's senior authority beneath its Guild Master; concealed Taemin's condition with Song Cheonwoo and participated in purging aides who knew the truth.

### Song Cheonwoo.md

# Song Cheonwoo (송천우)

- **Safe through:** Chapter 577
- **Aliases:** Director Song
- **Role:** Ares Guild Director and former A-rank Hunter who reached third place among Korean rankers, briefly headed the Hunter training center, and led Ares Guild's European regional branch for twenty years; he now leads an internal faction capable of threatening Go Jun.
- **Personality:** Highly ambitious, honor-obsessed, politically calculating, and determined to use his final opportunity to reclaim influence before retirement.
- **Voice:** Not established.
- **Relationships:** Song Cheonwoo followed Cheon Taemin since before Team Leader Choi was born, was Lee Jungryong's former friend and rival, helped conceal Taemin's condition and purge aides who knew the truth, negotiated the European regional director position to save himself and his family, is aligned with Choi against Go Jun, has had his children seized by Go Jun as leverage, and has told Choi that Taemin is probably alive but may be in Area A.

### Team Leader Choi.md

# Team Leader Choi

- **Safe through:** Chapter 577
- **Aliases:** Choi Minwoo (최민우)
- **Role:** Team Leader Choi is Cheon Taemin's only living blood relative and is positioning himself to take control of the Ares Guild after Lee Jungryong's death.
- **Personality:** Strategic, candid, controlled, and possessive of the power and influence he intends to inherit.
- **Voice:** Dry, formal, and direct, with calm candor and carefully chosen metaphors.
- **Relationships:** Choi Minwoo is Cheon Taemin's maternal grandson and only living blood relative, was kept out of public knowledge by Lee Jungryong, is closely integrated with Jin Taekyung's family, seeks to acquire the Ares Guild intact, and now knows that Song Cheonwoo and Lee concealed Taemin's collapse and purged aides while he investigates Taemin's fate.

### Won Myunghoon.md

# Won Myunghoon (원명훈)

- **Safe through:** Chapter 281
- **Aliases:** None
- **Role:** Thirty-nine-year-old A-rank Hunter, former top-one-hundred ranker and celebrity entertainer, and CEO of the Star Guild in Incheon; returned toward active Hunter work after an eight-year absence following the Myeongdong Station Mutated Gate Catastrophe, in which his close friend and fellow A-rank star Hunter Do Minsu and around thirty others died; survived the incident, was tried and cleared, and later retired from entertainment; led an ambush against the returning Peace Guild survivors, surrendered, attempted a surprise attack on Jin Taekyung, and was killed by Taekyung.
- **Personality:** Charismatic, sociable, image-conscious, and calculating; publicly warm and self-deprecating, but privately dismissive of weaker Hunters and coldly serious when assessing danger..
- **Voice:** Friendly and casual, with easy humor and a warm older-brother tone that turns serious when making his recruitment offer.
- **Relationships:** Taekyung's longtime favorite Hunter; regarded Taekyung as a good younger brother and offered to recruit him into the Star Guild and make him a star Hunter, but Taekyung declined both the Guild transfer and the proposed entertainment-agency route; privately resented the rejection; took in and raised Kim Jonghun, who has worked with him for more than ten years; during the raid crisis, Taekyung ordered him and the Star Guild members to leave and warned him not to bare his teeth again; Won then set an ambush for the returning Peace Guild survivors, surrendered after Taekyung defeated him, attempted to kill Taekyung in a surprise attack, and was killed by Taekyung.

## Korean source

```text
＃578화



콰아아앙!

마나(Mana)라 불리는 막대한 기의 파동에 땅거죽이 뒤집히고, 솟구친 눈더미가 거대한 벽을 만든다.

그리고 사방이 새하얗게 물든 그 순간.

찌직.

눈부신 빛줄기가 송천우의 옷소매를 찢고 튀어나왔다.

가느다랗고 예리한 형태의 검신은, 오직 지금 이 순간의 일격을 위해 개조한 기병(奇兵)이다.

‘미안하다.’

들리지 않을 짤막한 사과와 함께, 송천우는 섬광처럼 움직였다.

쉭.

하체는 낮게. 뒷발은 곧게. 앞발은 비스듬히 굽히며. 무기를 쥔 손에는 힘을 실어 일격을 내뻗는다.

감히 헤아릴 수조차 없을 만큼 수많은 시도 끝에 완성된 동작이 물 흐르듯 이어지고, 눈부신 오라에 휩싸인 검신이 공간을 꿰뚫었다.

슈화악!

모든 것을 가르는 날카로운 파공성.

현역에서 물러나 어느덧 칠순에 접어든 노인이 되었지만 송천우는 누구도 부정할 수 없는 강자였다.

대격변의 소용돌이를 견디며 전신에 각인된 감각, 그리고 몸 안에 웅크린 강대한 마나는 흘러간 세월을 부정한다.

그런 자신의 일격을, 아직 서른도 채 되지 않은 애송이가 막을 수는 없었다.

‘끝이다.’

송천우는 확신했다.

적어도 다음 순간. 바람과 눈의 벽을 관통한 검신이 무언가에 의해 가로막히기 전까지는 그랬다.

카가각!

“……!”

검신을 타고 전해지는 강렬한 반발력. 송천우의 눈이 부릅떠짐과 동시에 굉음이 울려 퍼졌다.

콰아아앙!

마나와 마나의 충돌. 그 여파로 일어난 칼바람이 사방을 할퀴었다.

눈의 장벽이 허물어지고 눈더미가 흩날린다.

그 사이에, 깊게 가라앉은 한 사람의 눈동자가 있었다.

“이거였습니까. 석고준이 준비했다는 함정이.”

평평한 검면으로 일격을 받아 낸 최민우의 모습에, 송천우는 침음성을 흘렸다.

“네가 어떻게…….”

있을 수 없는 일이었다. 그는 수년 전, 이십 대 초반의 최민우가 유럽지사에 머물렀을 때를 똑똑히 기억하고 있었다.

비록 타고난 재능은 뛰어났으나 그에 비해 실력은 훨씬 못 미쳤던 애송이.

그러나…….

드드드득!

검신을 타고 전해지는 힘으로 알 수 있었다.

지금 자신과 검을 맞대고 있는 이 청년이, 더 이상 애송이라 불릴 수 없는 강자로 거듭났다는 것을.

그리고 자신의 계획에 중대한 차질이 생겼다는 사실을.

‘핏줄은 못 속인다는 건가.’

천태민.

마음을 짓누르는 세 글자에 문득 검이 무겁게 느껴진다. 하지만 돌아가기에는 너무 멀리 와 버렸다.

오래전 그는 강을 건넜고, 스스로 배를 침몰시켰다. 석고준에게 붙잡혀 있을 혈육을 지키기 위해서는 물러설 수 없었다.

‘이 자리에서 죽여야 한다. 반드시.’

으득, 송천우는 이를 악물었다. 노화(老化)을 잊은 단단한 육체를 타고 강대한 마나가 샘솟았다.

손목이 호선을 그림과 동시에 예리한 검 끝이 평평한 검면 위를 미끄러졌다.

카각, 쉭!

그야말로 간발의 차였다. 아슬아슬하게 최민우의 목 옆을 스쳐 지나간 검 끝이 허공을 꿰뚫었다.

검압(劍壓)을 이기지 못하고 갈라진 목덜미에서 핏줄기가 솟구쳤다.

그 광경을 바라본 한 사람이 비명처럼 외쳤다.

“도련님!”

슬픔, 다급함, 그리고 분노가 담긴 외침.

수백 미터의 거리를 순식간에 좁힌 그가 소매를 떨치자, 주위의 대기가 뜨겁게 달아올랐다.

화르르르륵!

마나로 이루어진 화염이 솟구쳐 송천우의 앞을 가로막았다. 설산의 눈이 녹아내리고 증발한다.

그 뜨거운 열기 속, 송천우는 볼 수 있었다.

호흡을 가다듬으며 물러나는 최민우의 어깨너머로 가까워지는 노집사의 모습을.

“자네 왔나.”

송천우는 담담하게 김 집사를 응시했다.

한때 서로를 형과 동생으로 불렀던 그를. 전장에서 믿고 등을 맡길 수 있었던 몇 안 되는 동료를.

그러나 그것은 두 사람 모두에게, 흘러간 과거가 되어버렸다.

“당신을 원망했지만, 증오한 적은 없었습니다. 하지만…….”

화륵.

세찬 열기가 뿜어졌다. 허공에서 생성된 불꽃이 김 집사의 손을 휘감으며 새로운 형태를 갖추었다.

어느새 양손에 불의 채찍을 든 그의 모습을, 송천우는 아련한 시선으로 바라보았다.

“이제야 비로소 자네 같군. 내가 알던 그 김화종이 맞아.”

김 집사. 아니 김화종은 불의 채찍을 감아쥔 채 걸음을 내디뎠다.

저벅.

언제나 차분하던 눈동자에는 용암이 끓어오르고 있었다.

흐르는 세월 속에서도 한결같이 충성심을 유지했던 노 집사는, 어느덧 혈기왕성했던 과거의 모습으로 돌아가 있었다.

“아가리 닥쳐. 이 개 좆 같은 새끼야.”

“……!”

지금껏 본 적 없는 김화종의 모습에 최민우가 입을 벌린 그 순간.

쉭, 화아악!

휘둘려진 검의 궤적을 따라, 세 사람 사이를 가로막았던 불의 장벽이 갈라졌다.

그리고 최민우는 볼 수 있었다.

담담한 얼굴로 자신들을 응시하는 송천우의 얼굴과, 어느샌가 그의 목에 걸려 있는 새하얀 목걸이를.

‘저건.’

그리고 한없이 눈에 익은 그 목걸이의 이름이, 송천우의 입술 사이로 흘러나왔다.

“예티의 목걸이다. 네가 이곳으로 오라고 했을 때, 반드시 쓰임새가 있을 거라 생각했지.”

송천우는 문득 고개를 돌렸다. 그의 시선이 닿은 곳에, 크레바스 너머에서 눈사태와 함께 쏟아지는 수백 마리의 예티가 있었다.

“그리고 이번에는 내 생각이 맞았던 것 같구나. 그렇지 않느냐?”

- 캬우우우우!

이곳을 향해 쇄도하는 수백 마리의 예티를 보며, 최민우는 검자루를 움켜쥔 손아귀에 저절로 힘이 들어가는 것을 느꼈다.

‘예티의 목걸이라니.’

최민우도, 심지어는 김화종도 저 작은 목걸이가 어떤 기능을 하는지는 알고 있었다.

불과 몇 달 전, 블랙 와이번의 둥지에서 원명훈이 진태경을 함정에 빠트리기 위해 준비했던 마법 아이템이었으니까.

‘용족(龍族) 몬스터를 끌어들이는 노예의 표식.’

몬스터들 사이에도 위계가 있는 법.

설산에서 살아가는 거인, 예티는 용족의 노예였고 먹잇감이었다. 하지만 [예티의 목걸이]에는 용족 몬스터를 끌어들이는 기능만이 있는 것이 아니었다.

이 목걸이는, 용족의 노예였음을 알리는 표식인 동시에 예티에게는 동족이라는 증표다.

“당신……!”

송천우를 향한 최민우의 외침은 이어지지 못했다.

콰아아아아! 타다닥!

엄청난 양의 눈사태. 그 위를 파도 타듯 질주한 수백 마리의 예티가 크레바스를 뛰어넘었다.

가장 가까운 곳에는 송천우가 있었지만, 예티의 채취가 묻은 목걸이를 차고 있는 한 그는 동족이나 다름없었다.

- 크워어어어!

흉포한 괴성에 눈밭이 흔들렸다.

자신의 머리 위를 뛰어넘어 두 사람을 향해 달려가는 수백 개의 그림자를 힐끗 바라본 송천우가 입을 열었다.

“화종이. 자네는 빠져 있어야겠군.”

“이 씹어먹어도 시원치 않을 개새끼가!”

창노한 외침을 토해 낸 김화종이 불의 채찍을 휘둘렀다.

후우우웅! 쾅!

막대한 열기를 지닌 불꽃이 사방을 가로지르고 불태운다. 그러나 마력으로 강력해진 데다 수백에 달하는 예티들은 동족의 희생에도 아랑곳하지 않았다.

아니, 오히려 더욱 흉포한 마력을 피워 올렸다.

- 크워어어어어!

“……!”

중과부적(衆寡不敵).

김화종이 입술을 질끈 깨문 그때, 최민우의 나직한 목소리가 귓가를 파고들었다.

“괜찮습니다, 김 집사님.”

“도련님!”

“오히려 예티가 있다면 제 싸움도 힘들어집니다.”

“하지만……!”

“가세요. 이곳은 제가 맡을 테니.”

뭐라 반문하려던 김화종이 멈칫했다.

짧은 순간, 최민우의 흔들림 없는 눈동자를 바라본 노 집사는 말없이 땅을 박찼다.

양손에서 휘둘려진 불의 채찍이 수백 마리의 예티를 유인했다.

콰과과광!

- 캬우우!

열기와 함께 수백 마리의 예티가 멀어진다. 동시에 송천우가 걸음을 내디뎠다.

사박. 눈을 밟으며 한 걸음 앞으로 나아간 송천우의 손이 흐릿해졌다. 눈부신 오러에 휩싸인 검이 사방을 찢어발겼다.

슈화아아악! 서걱!

오러는 마나의 진정한 힘이 담긴 정수(精髓)다.

극도로 예리하고 파괴적인 기운이 힘차게 뻗어나가 공간을 갈랐다. 바람도, 눈도, 암석도 그것을 막을 수는 없었다.

단 한 가지 방법이 있다면, 그건 바로 또 다른 오러뿐이었다.

쉬쉭! 서걱!

쉴 새 없이 사방을 난도질하는 검격에 피부가 갈라지고 핏방울이 튄다.

종횡으로 베어 오는 빛줄기를 아슬아슬하게 피해 낸 최민우의 눈동자가 깊게 가라앉았다. 손아귀에 들린 검자루에 힘이 실렸다.

후우우웅.

[영웅의 혼]. 숭고한 영웅이 남긴 검이 진동한다.

설산을 닮은 새하얀 오러가 검신을 휘감으며 솟구치고, 양손으로 검을 굳게 말아쥔 최민우의 상반신이 부드럽게 회전했다.

쉬이이잉.

오러와 오러. 빛과 빛.

색이 다른 두 개의 섬광이 맞닿은 순간.

구구구궁!

거대한 충격파와 함께 설산이 흔들렸다. 반경 수십 미터의 눈더미가 가루가 되어 흩날리고 바스라진다.

그리고 온통 하얗게 물든 공간을 가로지르는 희끗한 신형들이 있었다.

쉬쉬쉬쉭!

쾅! 콰과광!

두 개의 신형. 두 개의 검. 각기 다른 주인을 가진 오러가 공간을 가로질러 충돌한다.

그럴 때마다 엄청난 충격파가 터져 나오며 눈더미를 밀어 내고 지면을 뒤집었다.

오랜만에 본연의 모습을 드러낸 암록색 지반 위에 붉은 액체가 툭, 떨어졌다.

주르륵.

최민우는 손목을 타고 흐르는 뜨거운 핏물을 느꼈다. 어깨는 욱신거렸고, 어느새 이마에 맺힌 식은땀이 눈썹을 건드렸다.

하지만 피를 지혈하거나 땀을 닦은 시간 따위는 주어지지 않는다.

그와 마주한 상대는 지금 이 순간에도 살의(殺意)가 담긴 검격을 퍼붓고 있었으니까.

쉬이잉! 서걱!

말 그대로 한 끗 차이. 단단한 암석으로 이루어진 지면이 두부처럼 잘려 나갔다.

아슬아슬하게 공격을 피해 낸 최민우가 짧은 호흡을 내뱉었다. 전신이 따끔거릴 만큼 살기를 내뿜은 적의 얼굴이 시야에 들어온다.

‘송천우.’

대격변이 낳은 영웅이자 한때 이정룡과 함께 손꼽히는 헌터였던 그의 실력은 실로 무시무시했다.

알려져서는 안 될 진실을 알고 있음에도 살아남을 수 있었던 이유 중 하나다.

쉬잉!

최민우가 고개를 비틀자, 맹렬한 바람과 함께 머리카락이 흩날렸다. 조금만 늦었다면 잘려 나간 것은 머리카락이 아니라 목이었을 것이다.

하지만 어째서일까. 사천에서 느꼈던 죽음의 공포가 느껴지지 않는 이유는.

피식.

오히려 실소가 흘러나왔다. 언젠가 이 자리에 없는 누군가와 나누었던 대화가 문득 생각나서였다.



‘이게 약간 미친 소리 같긴 한데. 가끔 죽을 것 같은 상황에서 웃음이 나올 때가 있어요.’

‘상당히 미치셨군요.’

‘그런데…… 웃음이 나오면 이상하게 꼭 이기더라고.’



그날 지나가듯 나눴던 대화가, 왜 하필 지금 같은 상황에 생각나는지는 모르겠다.

하지만 최민우는 이제 서야 그가 했던 말을 조금이나마 알 것 같았다.

‘난 죽지 않는다.’

그건 스스로에 대한 믿음이고, 끝까지 포기하지 않는 자만이 갖출 수 있는 의지다.

그것은 최민우가 지치고 상처 입은 몸으로 수천에 달하는 몬스터를 향해 걸어갔을 때, 비로소 자신의 것으로 만든 깨달음이었다.

쉬잉, 서걱!

허벅지로부터 불에 덴 듯한 통증이 일었다.

순간 신형을 비틀거리는 최민우의 모습에 송천우의 움직임이 한층 거세졌다.

쉬쉬쉬쉭! 서걱!

이번엔 팔이었고.

푹!

그다음은 옆구리였다.

그러나 최민우는 고통을 감내하며 나아갔다.

빗발치는 검격을 맞받아치며 끊임없이 한 걸음, 한 걸음을 내딛는 그의 손에서, 한 자루의 검이 진동하고 있었다.

우우우웅.

[영웅의 혼]. 원령이 되어서도 자신의 사명을 다했던 영웅으로부터 그에게 이어진 검.

자격을 갖춘 이에게, 더욱 큰 힘을 부여하는 명검.

후우우우웅!

검신이 몸을 떨었다. 휘황한 광채가 오라를 부풀렸다.

그 거대한 빛에, 송천우의 눈이 부릅떠졌다.

“너……!”

“마지막으로, 한 가지만 더 묻겠습니다.”

차가운 눈빛과 달리 목소리는 뜨거웠다.

최민우는 나직한 목소리와 함께, 모든 힘을 실은 일격을 내질렀다.

“내 몸 안에 흐르는 피가, 누구의 것인지 잊었습니까?”

“……!”

쉬이잉!

거대한 빛줄기가 공간을 갈랐다.

그리고 앞을 가린 그 눈부신 섬광 속에서, 송천우는 가슴을 가로지르는 한 줄기의 벼락을 느꼈다.

서걱!
```

## Final English reading copy

```markdown
# Chapter 578

*BOOOOM!*

The ground heaved beneath a massive wave of energy called mana, and the snow that burst into the air rose into a colossal wall.

Then, at the instant everything turned white—

*Zzt.*

A dazzling streak of light tore through Song Cheonwoo’s sleeve and shot outward.

The slender, razor-sharp blade was a weapon modified for the sole purpose of delivering this strike at this exact moment.

*I’m sorry.*

Along with that brief apology no one could hear, Song Cheonwoo moved like a flash of light.

*Swish.*

His lower body stayed low. His rear foot remained straight. His front foot bent at an angle. He drove strength into the hand gripping his weapon and thrust it forward.

The motion, perfected through more attempts than anyone could count, flowed together as smoothly as water. Wrapped in blinding aura, the blade pierced through space.

*SHWAAA!*

A sharp crack split the air, cutting through everything.

Song Cheonwoo had retired from active duty and was now an old man nearing seventy, but he remained a powerhouse no one could deny.

The instincts engraved throughout his body after surviving the vortex of the Great Cataclysm—and the tremendous mana coiled within him—refused to acknowledge the years that had passed.

There was no way some youngster who was not even thirty could block that strike.

*It’s over.*

Song Cheonwoo was certain of it.

At least, he was—until the next instant, when the blade piercing through the wall of wind and snow was stopped by something.

*SKRAAAK!*

“……!”

A powerful resistance traveled up the blade. Song Cheonwoo’s eyes flew open, and a thunderous roar rang out.

*BOOOOM!*

Mana collided with mana. The gale created by the impact clawed at everything around them.

The wall of snow collapsed, and the snowdrifts scattered.

Between them, a pair of eyes sat deep and still.

“So this is it. The trap Go Jun prepared.”

Song Cheonwoo let out a low groan at the sight of Choi Minwoo, who had caught the strike with the flat of his blade.

“How did you……?”

It was impossible. Song Cheonwoo remembered clearly when Choi Minwoo, still in his early twenties, had stayed at the European regional branch several years ago.

The youngster had possessed outstanding natural talent, but his actual ability had fallen far short of it.

But now…

*Rrrrrumble.*

He could tell from the force traveling along their crossed blades.

The young man locking swords with him was no longer someone who could be called a youngster. He had grown into a formidable warrior.

And Song Cheonwoo’s plan had suffered a major setback.

*So blood really does tell.*

Cheon Taemin.

The three syllables weighed heavily on his heart, and suddenly his sword felt heavier. But he had come too far to turn back now.

Long ago, he had crossed the river and sunk his own boat. He could not retreat if he wanted to protect the blood relatives Go Jun had taken hostage.

*I have to kill him here. No matter what.*

Song Cheonwoo clenched his teeth. Mana surged through his solid body, which had seemingly forgotten how to age.

As his wrist traced an arc, the sharp tip of his sword slid across the flat of Choi Minwoo’s blade.

*Clack. Swish!*

It had been a hair’s breadth. The sword tip narrowly grazed past Choi Minwoo’s neck and pierced empty air.

A stream of blood spurted from his neck, split open by the sword pressure.

Someone watching the scene cried out like a scream.

“Young Master!”

The shout carried sorrow, urgency, and fury.

The newcomer crossed hundreds of meters in an instant. When he flung his sleeve, the air around them heated rapidly.

*Fwoooosh!*

Flames made of mana erupted and rose between Song Cheonwoo and the others. The snow on the mountain melted and evaporated.

Amid the scorching heat, Song Cheonwoo could see the old butler drawing closer over Choi Minwoo’s shoulder as the young man retreated and steadied his breathing.

“You’ve come.”

Song Cheonwoo calmly stared at Butler Kim.

The man with whom he had once shared the bond of older and younger brothers. One of the few comrades he had trusted enough to leave his back to on the battlefield.

But that had become a thing of the past for both of them.

“I resented you, but I never hated you. However……”

*Fwoosh.*

A fierce heat burst forth. Flames formed in midair, coiled around Butler Kim’s hands, and took on a new shape.

Song Cheonwoo gazed wistfully at the man now holding a whip of fire in each hand.

“You finally look like yourself. You really are the Kim Hwajong I knew.”

Butler Kim—no, Kim Hwajong—tightened his grip on the whips of fire and took a step forward.

*Thud.*

Lava seemed to boil in the eyes that had always remained calm.

The old butler, who had preserved his loyalty without wavering through all the years that had passed, had returned to the vigorous figure he had been in the past.

“Shut your fucking mouth, you piece of shit.”

“……!”

At the sight of Kim Hwajong as he had never seen him before, Choi Minwoo opened his mouth.

Then—

*Swish! FWOOSH!*

Following the arc of the sword as it swung, the wall of fire separating the three of them split apart.

And Choi Minwoo saw it.

Song Cheonwoo’s calm face as he stared at them—and the brilliantly white necklace that had somehow appeared around his neck.

*That’s…*

The name of the necklace, so painfully familiar, slipped from Song Cheonwoo’s lips.

“It’s a Yeti’s Necklace. When you told me to come here, I knew it was bound to come in handy.”

Song Cheonwoo suddenly turned his head. Beyond the crevasse, hundreds of yetis came surging down with the avalanche.

“And this time, it seems I was right. Don’t you agree?”

—Kyaaaaaaar!

As he watched the hundreds of yetis charging toward them, Choi Minwoo felt his grip tighten instinctively around his sword hilt.

*A Yeti’s Necklace.*

Choi Minwoo—and even Kim Hwajong—knew what function the small necklace possessed.

Only a few months earlier, Won Myunghoon had prepared it as a magic item to trap Jin Taekyung in the Black Wyvern’s nest.

*A slave’s mark that draws in dragonkin monsters.*

There were hierarchies even among monsters.

Yetis, giants who lived in the snow-covered mountains, were the slaves and prey of dragonkin. But the Yeti’s Necklace did more than simply attract dragonkin monsters.

It marked its wearer as a slave of the dragonkin—and, to yetis, as one of their own kind.

“You……!”

Choi Minwoo’s shout toward Song Cheonwoo never finished.

*RUMBLE! Rat-a-tat!*

An enormous avalanche surged forward. Hundreds of yetis raced across it as though riding a wave, then leaped over the crevasse.

Song Cheonwoo was the closest to them, but as long as he wore the necklace carrying the scent of a yeti, he was no different from one of their kind.

—Kraaaaaar!

The savage roar shook the snowfield.

Song Cheonwoo glanced at the hundreds of shadows leaping over his head and charging toward the other two before speaking.

“Hwa-jong. You should stay out of this.”

“You dog-shit bastard! I’ll tear you apart!”

Kim Hwajong let out a furious cry and swung his whips of fire.

*Whoooosh! BOOM!*

Flames carrying tremendous heat swept across everything around them and set it ablaze. But the hundreds of yetis, strengthened by magic power, paid no attention even as their own kind fell.

If anything, they raised even more ferocious magic power.

—Kraaaaaar!

“……!”

There were simply too many of them.

Kim Hwajong clenched his lips tightly. At that moment, Choi Minwoo’s quiet voice reached his ears.

“It’s all right, Butler Kim.”

“Young Master!”

“If the yetis are here, my fight will only become more difficult.”

“But……”

“Go. I’ll handle things here.”

Kim Hwajong, who had been about to argue, stopped short.

For a brief moment, the old butler stared into Choi Minwoo’s unwavering eyes. Then he silently kicked off the ground.

The whips of fire swinging from both hands drew the hundreds of yetis away.

*RUMBLE!*

—Kyaaaa!

Hundreds of yetis retreated alongside the heat. At the same time, Song Cheonwoo stepped forward.

*Crunch.*

Song Cheonwoo took one step through the snow. His hand blurred.

The sword wrapped in dazzling aura tore through everything around it.

*SHWAAAAK! Slice!*

Aura was the essence containing the true power of mana.

An extremely sharp and destructive force surged forward, cleaving through space. Neither wind, snow, nor rock could stop it.

If there was only one way to stop it, that way was with another aura.

*Swish! Slice!*

The sword strikes slashed ceaselessly in every direction. Skin split, and drops of blood flew.

Choi Minwoo narrowly evaded the streaks of light cutting across him. His eyes sank deeply, and strength filled the hand gripping his sword hilt.

*Whoooosh.*

*Hero’s Soul.* The sword left behind by a noble hero trembled.

Pure white aura, resembling the snowy mountain, coiled around the blade and surged upward. Choi Minwoo gripped the sword tightly with both hands and smoothly rotated his upper body.

*Shiiiiing.*

Aura against aura. Light against light.

The instant two flashes of different colors met—

*RUMBLE-RUMBLE-RUMBLE!*

A massive shock wave shook the snowy mountain. Snowdrifts within a radius of dozens of meters turned to powder and scattered, breaking apart in the air.

Then pale figures streaked across the space turned completely white.

*Swish, swish, swish!*

*BOOM! CRASH!*

Two figures. Two swords. Auras belonging to different masters crossed space and collided.

Every time they did, tremendous shock waves erupted, pushing away snowdrifts and ripping up the ground.

Red liquid dropped onto the dark green ground, revealed for the first time in ages beneath the snow.

*Trickle.*

Choi Minwoo felt hot blood running along his wrist. His shoulder throbbed, and cold sweat had already formed on his forehead, brushing against his eyebrows.

But he was given no time to staunch the bleeding or wipe away the sweat.

The opponent facing him was still raining down sword strikes filled with killing intent.

*SHIIING! Slice!*

It was truly a matter of a single hair. The ground, made of solid rock, was sliced apart like tofu.

Choi Minwoo narrowly avoided the attack and let out a short breath. The enemy’s face entered his field of vision, radiating killing intent so intense that his entire body prickled.

*Song Cheonwoo.*

A hero born from the Great Cataclysm and once one of the most renowned Hunters alongside Lee Jungryong, Song Cheonwoo possessed truly terrifying skill.

His skill was one of the reasons Song Cheonwoo had survived despite knowing a truth that could never be allowed into the open.

*Shing!*

Choi Minwoo twisted his head, and his hair scattered in the fierce wind. If he had been even a moment slower, it would not have been his hair that was cut off, but his neck.

But why?

Why did he not feel the terror of death he had experienced in Sichuan?

*Heh.*

Instead, a quiet laugh escaped him. He had suddenly remembered a conversation he had once shared with someone who was not here.

*“This might sound a little crazy, but sometimes I start laughing when I’m in a situation where I feel like I’m going to die.”*

*“You really are quite insane.”*

*“But… whenever I start laughing, I always end up winning somehow.”*

He did not know why that conversation, exchanged so casually that day, had come to mind in a situation like this.

But Choi Minwoo finally felt as though he understood, at least a little, what that person had meant.

*I won’t die.*

It was faith in oneself, and a will possessed only by those who never gave up until the very end.

It was an enlightenment Choi Minwoo had made his own when he walked toward thousands of monsters in a body exhausted and wounded.

*Shing. Slice!*

A burning pain flared from his thigh.

At the sight of Choi Minwoo staggering as he twisted his body, Song Cheonwoo’s movements grew even more violent.

*Swish, swish, swish! Slice!*

This time, his arm.

*Thunk!*

Then his flank.

But Choi Minwoo continued forward, enduring the pain.

He met the rain of sword strikes head-on and kept taking one step after another. In the hand advancing without pause, a single sword was trembling.

*Whoooom.*

*Hero’s Soul.* A sword passed down to him from a hero who had fulfilled his mission even after becoming a vengeful spirit.

A legendary sword that bestowed even greater power upon those who possessed the qualifications.

*Fwoooooom!*

The blade trembled. A brilliant radiance caused the aura to swell.

Song Cheonwoo’s eyes widened at the enormous light.

“You……!”

“One last question.”

Unlike his cold gaze, his voice was hot.

Along with those quiet words, Choi Minwoo drove forward a strike carrying all his strength.

“Have you forgotten whose blood flows through my body?”

“……!”

*Shiiing!*

A massive streak of light cleaved through space.

And within the blinding flash that filled his vision, Song Cheonwoo felt a bolt of lightning slash across his chest.

*Slice!*
```

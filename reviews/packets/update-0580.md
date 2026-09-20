<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0580.txt",
      "sha256": "7c052b0e12a61ad8fd907ccb90212b08d96c4b6c788629de803d81bfbfb8a6f9",
      "bytes": 14499
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "015e15fa7b00d04205f1a05866034cda04d9a8d32509dffe2f919bd51f76a694",
      "bytes": 2434
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "979337dec45c6d24df237cb0ad58355d3ce4d797870bdd238aec038545cf3071",
      "bytes": 182422
    },
    {
      "path": "characters/Cheonwoo.md",
      "sha256": "db46cceb4c51fbbbd9605467898a4f6a744eff1a74e0a7624408009d28ed4013",
      "bytes": 590
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "7cb81304f5ef7be5386a2b1bd24288d7275b3d9debc302a9798fcb1e2113ac6d",
      "bytes": 553
    },
    {
      "path": "characters/Go Jun.md",
      "sha256": "8452a3eeaf672a5a728731c4b878d8b592e3d6534b6e2156ec69b02276dbe290",
      "bytes": 976
    },
    {
      "path": "characters/Go Se-won.md",
      "sha256": "661b197812e8596b7097fa6e8f49ab25e3a4c35865a6197d3fa18cb68138df5e",
      "bytes": 811
    },
    {
      "path": "characters/Hwa-jong.md",
      "sha256": "fc26639225f8ec716f2477fa40199dc11c6d1675d73e0fa824ed3f9d8ba8b250",
      "bytes": 562
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "69d0aa164d544197e9e7c971fd499d89d7c540293ee574215a1e60544408c8da",
      "bytes": 2280
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "74c74fbf3bcbfd0d813c5693856b496efccf7f7bf66da6e77ee961444f92d562",
      "bytes": 622
    },
    {
      "path": "characters/Kim Hwajong.md",
      "sha256": "7ac3cccd1607a9ba28fbee5c276430faf1552ebe43b2e30df6c4900609c5161b",
      "bytes": 538
    },
    {
      "path": "characters/Lee Jungryong.md",
      "sha256": "040252fcb99f6670c4e29a06bd073d35204a1113b218dd242f6922062acc09c4",
      "bytes": 1384
    },
    {
      "path": "characters/Song Cheonwoo.md",
      "sha256": "c8bc9c0aa048d5acb21cf33d5fe8716ca32f2ba1e3b4aed62d360bcd3b410955",
      "bytes": 1144
    },
    {
      "path": "characters/Team Leader Choi.md",
      "sha256": "336d356e21a5d4573793f7ed45d3ff982be308f198b0424273565d4d524b7245",
      "bytes": 956
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "0182f9d2518c8c81bc854119661e6d4bcfa60d67a608359582708c049f8d256f",
      "bytes": 179452
    }
  ],
  "estimated_tokens": 12933
}
-->

# Durable State Update — Chapter 580

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 580. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 580. Profile updates may replace only one
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
  "chapter": 580,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 580,
    "continuity_sources": [580],
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
    "Choi Minwoo has confirmed Song's account enough to treat Taemin's status as genuine while continuing to investigate.",
    "Busan's Kraken has been eliminated, but more than one thousand Mermen remain across Haeundae and Gwangalli while the Peace Guild and other forces contain the disaster.",
    "Song Cheonwoo warned Choi Minwoo that Go Jun is preparing a trap related to Choi's maternal grandfather.",
    "Go Jun seized Song Cheonwoo's children as leverage, forcing Song to attack Choi despite their temporary alignment against Go Jun.",
    "Song Cheonwoo used the Yeti's Necklace to bring hundreds of yetis into the confrontation; Kim Hwajong diverted them while Choi fought Song.",
    "Choi Minwoo defeated Song Cheonwoo with Hero's Soul and kept him alive as a witness.",
    "Song survived treatment and escaped into a crevasse, leaving his location unresolved."
  ],
  "continuity_sources": [
    579
  ],
  "open_questions": [
    "What caused Cheon Taemin's collapse, and what happened during his more than twenty years of unconsciousness?",
    "Is Cheon Taemin actually being kept in Area A of Ares Guild headquarters?",
    "What trap is Go Jun preparing, and can Song Cheonwoo's warning be trusted?",
    "Who empowered and released the Kraken, and did that person engineer the Monster Wave?",
    "Where did Song Cheonwoo go after escaping into the crevasse, and can he be recovered as a witness?"
  ],
  "safe_through": 579,
  "temporary_decisions": [
    "Use Yeti's Winter Range for 예티의 겨울 산맥.",
    "Use Stone King for 스톤 킹 and Skeleton King for 스켈레톤 킹.",
    "Use Area A for A구역.",
    "Use Hwa-jong for 화종.",
    "Use Hero's Soul for 영웅의 혼, Yeti's Necklace for 예티의 목걸이, and Hyung for 형님 when Song addresses Cheon Taemin."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 김화종    | **Kim Hwajong**   |
| 최민우    | **Choi Minwoo**   |
| 이정룡    | **Lee Jungryong** |
| 상태               | **Status**                     |
| 명성               | **Fame**                       |
| 몬스터     | **monster**           |
| 길드      | **Guild**             |
| 길드장     | **Guild Master**      |
| 부길드장    | **Vice Guild Master** |
| 팀장      | **Team Leader**       |
| 마정석     | **Magic Gem**         |
| 천우 | **Cheonwoo** | Name shown in a Level Window; one of the five current Five Gates scions. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 고준 | **Go Jun** | Personal name of Team Leader Seok; Lee Jungryong's prized Disciple. |
| 고세원 | **Go Se-won** | Ares Guild Head of Security and Team Leader. |
| 화종 | **Hwa-jong** | Butler Kim's personal name. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 송천우 | **Song Cheonwoo** | Ares Guild Director, former third-ranked Korean Hunter, and longtime European regional branch director. |
| 평화 | **Peace Guild** | Guild name. |
| 아레스 | **Ares Guild** | The leading Guild in Korea; formerly employed Team Leader Choi and Song Song. |
| 사장님 | **Boss** | Address for the restaurant owner; contextually rendered as ma'am in one reply |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 준이 | **Jun** | Family nickname used in the form Jun's dad. |
| 석고준 | **Go Jun** | Source full-name form for the established Go Jun, also known as Team Leader Seok. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 광안 | **Guang'an** | Sichuan location where the party boards Mu Song's ship. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 텔레포트 | **Teleport** | Taekyung's label for the Blood Lord's unexplained disappearance. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 부산 | **Busan** | City where the Haeundae Gate crisis occurs. |
| 광안대교 | **Gwangan Bridge** | Busan suspension bridge central to Taekyung's childhood memory and the current disaster. |
| 크라켄 | **Kraken** | Sea monster leading the Monster Wave; newly identified in this chapter. |
| 머맨 | **Merman** | Sea monster species serving under the Kraken. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 사장님 | visitor_to_restaurant_owner | Boss | polite but sarcastic | Maintains a superficially respectful address while baiting the owner during the confrontation. |
| 사장님 | 진태경 | restaurant_owner_to_employee_son | you / you little punk | condescending-aggressive | Uses hostile informal forms while trying to intimidate Taekyung. |
| 김화종 | 진태경 | senior_Hunter_to_younger_Hunter | Mr. Jin | formal-polite | Hwajong addresses Taekyung as 진태경 씨 while proposing an exchange of stories. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 이정룡 | 진태경 | senior S-rank Hunter to younger Hunter and adversary | Young man | polished, teasing, and veiled-threatening | Uses a genial tone and indirect threats while trying to make Taekyung release the captives. |
| 진태경 | 이정룡 | younger Hunter to senior S-rank Hunter and adversary | you | polite but mocking and defiant | Taekyung answers Lee's soft threats with the wolf-and-tiger metaphor and refuses to yield. |
| 이정룡 | 고준 | Master to Disciple | Go Jun | familiar and testing | Lee switches from Seok's office title to his personal name while considering whether he can defeat Taekyung. |
| 고준 | 이정룡 | Disciple to Master | Master | deferential | Go Jun responds to Lee's personal-name address as 스승님. |
| 석고준 | 최민우 | Ares security leader to rival Guild Master | Team Leader Choi Minwoo | formal but barbed | Uses 평화 길드 최민우 팀장님 while belittling Choi and blaming the Peace Guild for Taekyung's apparent death. |
| 진태경 | 석고준 | returning Hunter to hostile Ares security leader | you fucking bastard | hostile and profane | Taekyung directs his final insults and challenge at Go Jun after returning alive. |
| 석고준 | 진태경 | hostile_opponents | brat | hostile and overconfident | Go Jun addresses Taekyung internally as 애송아 while launching his full-strength attack. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 최민우 | 진태경 | trusted allied team leader to younger allied Hunter | Mr. Jin | formal-polite and concerned | Choi warns Jin about the danger of the operation and affirms his deep trust. |
| 진태경 | 최민우 | younger allied Hunter to allied team leader | Team Leader Choi | polite, familiar, and teasing | Jin jokes with Choi while acknowledging and dismissing his concern. |
| 고준 | 진태경 | Ares Guild combatant confronting the killer of his Master | you | hostile and informal | Go Jun uses 너 while demanding Jin confess to Lee Jungryong's death and threatening retaliation. |
| 진태경 | 고준 | dominant adversary confronting Lee Jungryong's Disciple | you | contemptuous and informal | Jin uses 너 and 놈 while overpowering Go Jun and ordering him to end the conflict with Lee Jungryong. |
| 석고준 | 고세원 | Ares Vice Guild Master to Head of Security | you | curt and informal | Go Jun tells Go Se-won that he is later than usual when Se-won enters the wrecked office. |
| 고세원 | 석고준 | subordinate_to_Vice_Guild_Master | Vice Guild Master | formal-deferential | Uses 부길드장님 while trying to stop Go Jun from watching the broadcast. |
| 송천우 | 석고준 | adversary; captor of Song's children | you | shocked and confrontational | Song reacts directly to Go Jun's admission that he took the children. |
| 고세원 | 송천우 | Ares security-team leader to Ares regional branch director | Director | formal-polite but threatening | Go Se-won repeatedly addresses Song as 지사장님 while escorting him out. |
| 송천우 | 고세원 | Ares regional branch director to security-team leader | Go Se-won | informal and confrontational | Song directly calls Go Se-won by name while challenging his knowledge of Go Jun's plans. |
| 화종 | 최민우 | butler_to_Young_Master | Young Master | formal and deferential | Butler Kim consistently addresses Choi Minwoo with the established deferential title. |
| 송천우 | 화종 | former_allies | Hwa-jong | familiar and informal | Song uses Hwa-jong's personal name, prompting Hwa-jong to reject the familiarity. |
| 화종 | 송천우 | former_allies_now_hostile | you | formal and cold | Hwa-jong challenges Song's right to expect Choi's trust and rejects their former intimacy. |
| 송천우 | 최민우 | older_former_ally_to_younger_former_ally | Minwoo | familiar and informal | Song addresses Choi by his given name while discussing the meeting place and surveillance. |
| 최민우 | 화종 | Young Master to butler | Butler Kim | formal and respectful | Choi refers to Hwa-jong as 김 집사님 while discussing the concealed truth. |
| 최민우 | 송천우 | temporary ally to rival | Regional Director | formal and cutting | Choi uses 지사장님 while condemning Song's survival and concealment. |

## Listed compact profiles

### Cheonwoo.md

# Cheonwoo (천우)

- **Safe through:** Chapter 579
- **Aliases:** None
- **Role:** One of the five current Five Gates of Shanxi scions and a First Rate martial artist present at Honghwa Inn.
- **Personality:** Pampered and contemptuous toward Cheongpung's group as part of the five scions' collective mockery.
- **Voice:** Mocking in the group's exchange; no distinct individual speech is established.
- **Relationships:** Associates with Seongryong, Myeonghwa, Sohye, and Jintae as a group of current Five Gates scions.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 579
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Go Jun.md

# Go Jun (고준)

- **Safe through:** Chapter 579
- **Aliases:** Team Leader Seok
- **Role:** Go Jun is Ares Guild's Vice Guild Master, Lee Jungryong's disciple and former Head of Security, and the de facto successor to Lee's Ares legacy who passed the S-rank Hunter qualification assessment with a very high score but lacks Lee's legitimacy.
- **Personality:** Disciplined and controlled under ordinary pressure, fiercely loyal to Lee Jungryong, but consumed by humiliation and rage when Ares Guild's authority is challenged.
- **Voice:** Dry, controlled, and formal with subordinates; deferential when addressing his Master.
- **Relationships:** Disciple and direct protégé of Lee Jungryong, Go Jun inherited Lee's Ares Guild legacy after his death, regards Jin Taekyung and Choi Minwoo as enemies seeking to take it away, and has seized Song Cheonwoo's children as leverage while calling it protection.

### Go Se-won.md

# Go Se-won (고세원)

- **Safe through:** Chapter 569
- **Aliases:** Head of Security
- **Role:** Go Se-won is Ares Guild's Head of Security and a Team Leader with privileged access to restricted Section A.
- **Personality:** Composed and confident in public, he is mildly uncomfortable with Ares Guild's increasingly severe discipline but obeys its policy.
- **Voice:** Calm and deferential toward superiors, but blunt and decisive when issuing orders.
- **Relationships:** Go Se-won reports to Vice Guild Master Go Jun, commands Ares Guild's thirty-member security team, personally ordered and cleaned up the abduction of Song Cheonwoo's family, and is married with a young son, Sangho, while his wife is pregnant with their second child.

### Hwa-jong.md

# Hwa-jong (화종)

- **Safe through:** Chapter 579
- **Aliases:** Butler Kim
- **Role:** Hwa-jong is Choi Minwoo's loyal butler and personal escort.
- **Personality:** Loyal, vigilant, and uncompromising toward perceived threats to Choi Minwoo.
- **Voice:** Formal and deferential toward Choi Minwoo, cold and openly hostile toward Song Cheonwoo.
- **Relationships:** Hwa-jong serves Choi Minwoo and was formerly close to Song Cheonwoo, but their relationship ended over loyalty and ambition.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 579
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, a Supreme Peak master who possesses the Heavenly Martial Physique and superhuman physical strength, has manifested Force, opened his Middle Dantian, crossed the wall into true mastery, has achieved Three Flowers Gather at the Crown but not Five Qi Returning to Origin, can perceive the texture of qi well enough to sever layered magic, can resist high-level monster Fear through exceptional mental strength, is publicly recognized as an S-rank-level Hunter while formally retaining an A-rank license pending testing, can command coordinated raids against powerful monsters, serves as one of the two pavilion masters of the Alliance Leader's direct Fire Dragon Pavilion, leads its first mission to Nanman, and is the Peace Guild's wealthy patron in the modern world.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor and assigned him a final task to incorporate martial principles into his learned martial arts but declined Taekyung's recruitment after Cheongpung reached him first, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate, student, and trusted manager of media and official arrangements, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, and Xiao Shen regards him as an older brother after Jin saved him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 579
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Kim Hwajong.md

# Kim Hwajong (김화종)

- **Safe through:** Chapter 579
- **Aliases:** Butler Kim
- **Role:** Kim Hwajong is a Level 80 mage known as Butler Kim and Choi Minwoo's loyal butler and personal escort.
- **Personality:** Gentle and composed
- **Voice:** Gentle and measured
- **Relationships:** Kim Hwajong formerly instructed Im Chunsoo, who remains terrified of and obedient to him, and serves Choi Minwoo as butler and personal escort, having become Choi's only family.

### Lee Jungryong.md

# Lee Jungryong (이정룡)

- **Safe through:** Chapter 579
- **Aliases:** None
- **Role:** Former Vice Guild Master of Ares Guild, one of Korea's two S-rank Hunters, and a Supreme Peak-level martial artist who was killed by Jin Taekyung.
- **Personality:** Outwardly genial, calm, and humorous; calculating, opportunistic, manipulative, coercive, and ruthless when challenged
- **Voice:** Smooth, good-natured, and indirect, using teasing conversation and veiled threats before becoming openly furious
- **Relationships:** Master of Park Jihoon and Go Jun (Team Leader Seok), whom he personally selected and trained; longtime Great Cataclysm acquaintance of Park Tae Seop; adversary of Jin Taekyung; knew Team Leader Choi from childhood; has an antagonistic history with Kim Hwajong, who saved his life at the collapse of Mapo Bridge eighteen years earlier; was visibly shaken by learning that Choi is Cheon Taemin's maternal grandson; regarded Cheon Taemin as an older brother despite no blood relation and long held him in respect and fear; secretly supported the orphanage where Lee Dongseok grew up and was regarded by Dongseok as a father; operated as Ares Guild's senior authority beneath its Guild Master; concealed Taemin's condition with Song Cheonwoo and participated in purging aides who knew the truth.

### Song Cheonwoo.md

# Song Cheonwoo (송천우)

- **Safe through:** Chapter 579
- **Aliases:** Director Song
- **Role:** Ares Guild Director and former A-rank Hunter who reached third place among Korean rankers, briefly headed the Hunter training center, and led Ares Guild's European regional branch for twenty years; after leading a faction against Go Jun, he survived Choi Minwoo's defeat and escaped into a crevasse as a severely wounded witness.
- **Personality:** Highly ambitious, honor-obsessed, politically calculating, and determined to use his final opportunity to reclaim influence before retirement.
- **Voice:** Not established.
- **Relationships:** Song Cheonwoo followed Cheon Taemin since before Team Leader Choi was born, was Lee Jungryong's former friend and rival, helped conceal Taemin's condition and purge aides who knew the truth, negotiated the European regional director position to save himself and his family, is aligned with Choi against Go Jun, has had his children seized by Go Jun as leverage, and has told Choi that Taemin is probably alive but may be in Area A.

### Team Leader Choi.md

# Team Leader Choi

- **Safe through:** Chapter 579
- **Aliases:** Choi Minwoo (최민우)
- **Role:** Team Leader Choi is Cheon Taemin's only living blood relative, a formidable aura-wielding swordsman who wields Hero's Soul, and is positioning himself to take control of the Ares Guild after Lee Jungryong's death.
- **Personality:** Strategic, candid, controlled, and possessive of the power and influence he intends to inherit.
- **Voice:** Dry, formal, and direct, with calm candor and carefully chosen metaphors.
- **Relationships:** Choi Minwoo is Cheon Taemin's maternal grandson and only living blood relative, was kept out of public knowledge by Lee Jungryong, is closely integrated with Jin Taekyung's family, seeks to acquire the Ares Guild intact, and now knows that Song Cheonwoo and Lee concealed Taemin's collapse and purged aides while he investigates Taemin's fate.

## Korean source

```text
＃580화



크라켄(Kraken)이라 불리는 네임드 몬스터가 수천의 머맨을 이끌고 부산에 상륙했다는 충격적인 소식은 빠르게 퍼졌다.

그리고 고세원은 뉴스 속보가 뜨기도 전에 그 정보를 접한 몇 안 되는 인물 중 하나였다.

‘몬스터 웨이브라니.’

그도 사람이다. 부산은 오백만에 달하는 인구가 거주하는 대도시. 비록 자신과 그들은 일면식조차 없지만, 그래도 무수한 민간인들이 희생당할 것을 생각하니 기분이 썩 좋지 않았다.

‘이 부분에 있어서만큼은 진태경이 있어서 다행이군.’

저벅저벅.

고세원의 모습에 본사 내부를 오가던 길드원들이 황급히 길을 텄다.

빠른 발걸음으로 그들을 지나쳐 간 고세원이 작은 목소리로 중얼거렸다.

“경호팀. 응답 바람.”

삐빅.

귓가에서 들려오는 미세한 기계음과 함께, 즉각적인 응답이 뒤를 이었다.

- 3팀. 송신 완료.

- 2팀. 송신 완료.

- 1팀. 송신 완료.

“VIP 뵈러 가니까 A구역 열고, 현 위치 및 인원 보고해.”

고세원은 상관의 허락을 받아 부산에 경호팀을 투입할 생각이었다.

사람들을 구해서이기도 했지만, 최근 망가진 아레스 길드의 이미지 개선에도 도움이 될 테니까.

그러나 뒤이어 차례대로 들려오는 팀장들의 보고에, 그는 문득 눈살을 찌푸렸다.

- 3팀 전원. 런던에서 표적의 가족을 감시 중입니다.

- 2팀. 전원. 런던에서 복귀 후 본사 A구역에서 대기 중입니다.

- 1팀. 현재원 아홉 명. 런던에서 복귀 후 본사 100층에서 대기 중입니다.

“1팀장. 다시 말해 봐. 뭐라고?”

- 1팀. 현재원 아홉 명. 본사 100층에서 대기…….

“뒷말은 필요 없으니 집어치우고.”

고세원은 나직한 목소리와 함께 마법진으로 발을 내디뎠다.

화아악.

텔레포트 마법이 발동되었음을 뜻하는 새하얀 빛과 함께 A구역으로 이동한 그가 말을 이었다.

“왜 열 명이 아니라, 아홉 명이지?”

- 긴급한 일이 생겨서 그렇습니다.

“긴급한 일이라. 제외된 인원은?”

- 김호중입니다.

“김호중?”

- 예.

건조한 1팀장의 목소리를 들으며 고세원은 A구역의 복도를 가로질렀다. 날카로운 구둣발 소리만큼이나 그의 심경도 불편해졌다.

“그건 희한한 일이군. 나는 보고 받은 기억이 없거든.”

- 죄송합니다.

“사과 말고 이유를 묻는 거다. 무단이탈인가?”

- 당연히 아닙니다.

그래, 당연히 아니겠지. 고세원은 내심 중얼거렸다.

경호팀은 죽은 이정룡이 길러 낸 사냥개다.

이정룡은 오래전부터 엄청난 규모의 고아원과 보육원을 은밀히 운영하고 있었고 갈 곳 없는 고아들에게 충성심을 새겨 넣었다.

자신도 그랬고, 저들도 마찬가지다.

그중에서도 1팀은 가장 충성스럽고 뛰어난 놈들만 속한 곳이었다. 그런 1팀에서 무단 이탈자가 나온다는 건 몬스터 웨이브보다 희박한 확률이었다.

특히 사라진 김호중이라는 인물은 더더욱 그렇다.

‘그렇다는 건…….’

아레스 길드에는 많은 숫자의 중진과 원로들이 있지만, 경호팀은 오직 두 사람의 명령만 따른다.

그중 한 사람인 고세원에게도 아무런 보고 없이 김호중이 사라졌다는 사실은, 단 한 가지를 의미했다.

뚜벅.

막힘없이 나아가던 걸음이 우뚝 멈췄다.

고세원이 아무런 명패도, 장식도 되어 있지 않은 문을 말없이 응시하던 그때. 문 너머에서 누군가의 경쾌한 목소리가 울려 퍼졌다.

“들어와. 밖에서 서성거리지 말고.”

“……!”

마른침을 삼킨 고세원은 문을 열고 들어갔다. 깔끔하게 정리된 방 안에는 그의 하나뿐인 직속 상관이 그를 기다리고 있었다.

“오늘 날씨 좋네. 안 그래, 고 팀장?”

“예.”

짧게 목례를 취한 고세원의 시선이 빠르게 주위를 훑었다.

석고준의 입가에 걸린 기분 좋은 웃음과 손에 들린 위스키 잔. 그리고 한 손에서 굴려 대는 무언가까지.

‘뭐지?’

평소의 석고준이 아니다. 고세원은 이 방안의 모든 것이 낯설고 불안하게 느껴졌다.

그건 어쩌면 귓가를 파고드는 소음 때문일지도 몰랐다.

까드득. 까득.

거슬리는 마찰음에 석고준의 목소리가 섞여들었다.

“김호중 그 친구는 고 팀장이 신경 안 써도 될 거야. 내가 따로 시킨 일이 있었거든.”

“그렇군요.”

“어떤 일인지 궁금하지는 않고?”

두 사람의 시선이 허공에서 부딪쳤다. 오늘따라 유난히도 붉은 석고준의 눈동자를 바라보며, 고세원이 정중히 고개를 숙였다.

“아닙니다. 부길드장님 지시 사항이라면 그럴 만한 이유가 있었겠죠.”

“그거 듣기 좋은 대답이네. 그렇지 않아도 요즘 고 팀장이 나한테 섭섭해하는 것 같았는데. 아무래도 내가 나이도 어리고, 또 고 팀장이 원체 스승님을 잘 따랐으니까.”

“그럴 리 있겠습니까. 전(前) 부길드장님께 은혜를 입었던 것은 사실이지만, 그렇다고 해서 제 충성심이 줄어드는 것은 아닙니다.”

“그런가? 그럼 다행이고.”

까드득.

다시 한번 손아귀에 쥔 무언가를 마찰시킨 석고준이 기분 좋게 웃으며 술잔을 흔들었다.

“날씨도 좋은데, 같이 한잔할까?”

고세원이 침착하게 대답했다.

“송구스럽습니다만…….”

“안 마신다는 뜻이지? 안타깝군. 좋은 술인데.”

느긋하게 술잔을 비운 석고준을 말없이 바라보던 고세원이 문득 입을 열었다.

“그보다 긴급히 보고드릴 사항이 있습니다.”

“말해.”

“부산에서…….”

다음 순간, 고세원은 말꼬리를 흐렸다. 술잔을 내려놓은 테이블 위에 놓인 홀로그램 PC를 보았기 때문이었다.

일시 정지된 화면 속에는 엄청난 크기의 문어와 처참히 무너진 광안대교의 모습이 담겨 있었다.

“부산에서, 뭐?”

“…….”

잠시 침묵하던 고세원이 중얼거렸다.

“이미 알고 계셨군요.”

석고준이 낮은 웃음소리를 흘렸다.

“알고 있었지. 누구보다 먼저.”

변함없는 경쾌한 목소리에 가슴이 쿵 내려앉는다.

설마 했던 불안감이 실체를 드러내는 것을 느끼며, 석고준은 애써 담담하게 입을 열었다.

“그렇다면 김호중은…… 지금 부산에 있는 겁니까?”

“조금 전에는 궁금하지 않다고 했던 것으로 기억하는데.”

“죄송합니다. 저도 모르게 그만.”

“됐어. 어차피 고 팀장도 알아야 하니까.”

기분 좋게 대꾸한 석고준이 빈 술잔에 위스키를 가득 채우며 말을 이었다.

“맞네. 김호중 그 친구는 지금 내 지시로 부산에 있지.”

잠시 뭔가를 생각하던 석고준이 덧붙였다.

“지금쯤이면 없을 수도 있고.”

“……!”

“그러지 말고 앉아서 술 한잔하지. 계속 올려다보니 목이 아픈데.”

이번만큼은 고세원도 거절하지 못했다. 아니, 거절할 이유가 없었다.

격랑이 몰아치는 마음을 진정시키기 위해서는 술이라도 마셔야 했으니까.

벌컥, 벌컥.

독한 위스키를 단번에 털어 넣자 비로소 숨이 트이는 듯했다.

텅 빈 크리스털 잔을 쥔 채 머뭇거리던 고세원은 간신히 목소리를 쥐어 짜냈다.

“부길드장님. 어떻게 그런 일이 가능하셨는지는 모르겠지만, 이런 방식으로는 저들에게 그리 큰 타격을 줄 수 없습니다.”

“왜 그렇게 생각하지?”

“그가. 아니, 진태경이 있지 않습니까. 아크 리치도 잡은 놈입니다. 이번 몬스터 웨이브도 빠르게 진압 중이고요. 이건 평화 길드의 명성을 더해 주는 것밖에 되지 않습니다.”

“그래. 그렇지. 진태경. 참 대단한 놈이야.”

상관의 분노를 감수하고 꺼낸 이름이었지만, 예상과 달리 석고준의 입가에 맺힌 미소는 여전했다.

그리고 그 부드러운 미소에, 고세원은 더욱 큰 불길함을 느꼈다.

“부길드장님. 설마…….”

“지휘관을 잡으려면 장수를 유인해야지. 알려진다면 난리가 나겠지만, 후환(後患)도 없을 거야.”

“……!”

“진태경은 지금 당장으로서는 어쩌지 못해. 하지만 최민우라면 이야기가 다르지. 그렇지 않나?”

까드득. 까득.

거슬리는 마찰음과 함께, 고세원의 뇌리에 한 사람의 이름이 벼락처럼 스쳐 지나갔다.

“송천우. 송천우로군요.”

“정답이야. 상으로 한 잔 더 주지.”

고세원은 떨리는 손끝을 감추며 술을 받았다. 어디서부터 어디까지 잘못되었는지, 그의 머리로는 도무지 가늠하기가 힘들었다.

다만 이 와중에도 상관의 계획이 실패할 것이라는 확신이 들었다.

“……최민우는 조심성이 많은 인물입니다. 표면적으로는 평화 길드의 주인이자, 오랫동안 곁에서 충성을 바친 김화종도 있습니다.”

“알아. 김화종에 관해서는 스승님께서도 여러 번 말씀하셨으니까. 게다가 다른 경호 인력까지 생각한다면 송천우, 그 늙은이 혼자서는 무리겠지.”

“부길드장님. 그럼 도대체 왜.”

까드드득!

순간, 크게 울려 퍼진 마찰음에 고세원의 목소리가 파묻혔다.

대답 대신 피식 웃은 석고준이 손바닥을 폈다. 내내 손에 쥐고 있던 무언가가 마침내 모습을 드러냈다.

달걀만 한 크기에, 심연을 끌어모아 가둔 듯한 어둠을 품은 그것의 명칭이 고세원의 입술 사이로 흘러나왔다.

“마정석…….”

단순한 마정석이었다면 놀라지도 않았을 것이다.

지금 석고준의 손바닥 위에 올려진 것은 네임드 몬스터에게서만 나올 수 있는, 이른바 S급 마정석이라 불리는 것이었다.

정화를 거치지 않은 순수한 마력(魔力)이 그 안에서 회오리쳤다.

“부, 부길드장님.”

이제야 알았다. 어떻게 그가 인위적으로 몬스터 웨이브를 일으킬 수 있었는지.

탄식과 두려움이 섞인 고세원의 부름에, 석고준은 나직이 뇌까렸다.

“최민우. 놈은 오늘. 반드시 죽는다.”

그리고 최민우를 죽이는 것은 둘 중 하나가 될 것이다.

가족을 인질로 잡힌 노인. 혹은 석고준 자신조차 정체를 명확히 알 수 없는 또 다른 존재.

“확실한 것은, 송천우에게는 선택지가 없다는 거지.”

작게 중얼거린 석고준이 기분 좋게 웃었다.

습관적으로 목에 걸린 낡은 목걸이를 어루만지는 그의 눈동자에서 어둠이 일렁였다.



* * *



어찌 그토록 심각한 몸 상태로 움직일 수 있었느냐고 누군가 묻는다면, 송천우는 두 글자로 답할 것이다.

의지.

말 그대로 그건 의지였다. 혼신의 의지로 끌어올린 마지막 힘. 일흔에 접어든 노인은 죽을힘을 다하여, 스스로를 죽음으로 내던졌다.

파팟! 후웅!

세상이 느려졌다.

차가운 눈의 감촉이 사라지고 붕 뜬 부유감(浮游感)이 전신을 사로잡는다.

찰나를 쪼개고 쪼갠 짧은 순간 속, 송천우는 자신을 바라보는 두 쌍의 부릅뜬 눈동자와 눈이 마주쳤다.

최민우와 김화종. 두 사람의 눈이 그렇게 묻는 듯했다.

‘어째서?’

송천우는 내심 두 사람이 품은 의문에 대한 답을 중얼거렸다.

‘이 방법밖에는 없으니까.’

아마 며칠 전이었다면 최민우가 내민 손을 잡았을 것이다.

하지만 마지막으로 마주한 석고준은…… 괴물이 되어 있었다.

송천우는 그의 눈에서 광기(狂氣)를 느꼈다. 자신이 살아서 이곳을 나간다면, 놈은 한 치의 망설임도 없이 가족들을 제거할 것이다.

그건 평화 길드도, 심지어 진태경이나 ‘그분’께서도 해결할 수 없는 일이었다.

‘그래, 결국 이렇게 되는군.’

뇌리를 스치는 짧은 상념과 함께, 송천우는 새카만 어둠을 향해 추락했다.

도무지 끝을 알 수 없는 어둠은 괴물의 아가리 같았고, 자신의 인생 같기도 했다.

‘니체였던가.’

누군가 그랬다. 심연을 들여다보고 있으면, 그도 심연이 된다고.

송천우는 뒤늦게 그 사실을 깨달았지만 모든 것이 늦어 버린 후였다.

쐐애애애애액!

싸늘하고도 맹렬한 바람이 전신을 후려친다.

사나운 바람의 울음 속에서, 며칠 전 한 사람과 나누었던 대화가 귓가를 파고드는 듯했다.



‘이건.’

‘넣어 두십시오. 지사장님께서도 아시다시피 워낙 위험한 물건이니까. 물론 비싸기도 하고요.’

‘……네놈. 미쳤구나.’

‘당신도 미쳐야 할 거요. 가족들을 살리고 싶다면.’



미친놈이었고, 미친 대화였다.

그리고 송천우는 하루가 십 년과도 같은 고민 끝에, 마지막까지 ‘그것’을 사용하지 않았다.

‘마지막으로 잘한 일인가.’

맹렬해지는 바람 속, 송천우는 어둠 속에서 무언가가 가까워지는 것을 느끼며 눈을 감았다.

퍼걱! 우두두두둑!

길었던 추락의 끝.

가장 먼저 목이 부러지고, 전신의 뼈마디가 으스러진다.

그리고 다음 순간. 송천우는 흐릿해지는 의식 너머로 무언가의 울음소리를 들었다.

- 크르르르.

지금껏 들어 본 적 없는, 스산한 괴물의 울음소리.

그는 뭐라 말하고 싶었지만, 오랜 세월 심연에 웅크리고 있던 존재는 먹잇감의 유언을 허락하지 않았다.

콰직!

어둠이 찾아왔다.

거대한 이빨이 생명이 빠져나간 육신을 부수고 피를 삼켰다.

괴물이 아닌 사람으로 죽고 싶었던 노인이 끝끝내 사용하지 않은, 포켓 깊숙한 곳에 넣어 둔 무언가까지.

화아악.

어둠. 그 자체가 빛이 되어 뿜어나왔다.
```

## Final English reading copy

```markdown
# Chapter 580

The shocking news that a Named Monster called the Kraken had landed in Busan, leading thousands of Mermen, spread quickly.

And Go Se-won was one of the few people who had received the information before the breaking news even appeared.

*A Monster Wave…*

He was human, too. Busan was a major city with a population approaching five million. He did not even know those people, but the thought of countless civilians being sacrificed still left a bitter taste in his mouth.

*At least Jin Taekyung is there.*

*Step. Step.*

Guild members moving through the headquarters hurriedly cleared a path when they saw Go Se-won.

He passed them at a brisk pace and muttered in a low voice,

“Security Team. Respond.”

*Beep.*

A faint mechanical sound came from his earpiece, followed by immediate replies.

—Team Three. Transmission complete.

—Team Two. Transmission complete.

—Team One. Transmission complete.

“I’m going to see a VIP. Open Area A and report your current locations and personnel.”

Go Se-won intended to obtain his superior’s permission to deploy the security teams to Busan.

It was partly to rescue people, but it would also help repair Ares Guild’s recently shattered image.

However, his brow gradually furrowed as the team leaders reported in one after another.

—All of Team Three are monitoring the target’s family in London.

—Team Two has returned from London and is waiting in Area A of headquarters.

—Team One currently has nine members. We returned from London and are waiting on the hundredth floor of headquarters.

“Team Leader of Team One. Say that again. What did you say?”

—Team One currently has nine members. We are waiting on the hundredth floor of headquar—

“Forget the rest.”

Go Se-won stepped onto a magic circle as he spoke in a quiet voice.

*Whoosh.*

A flash of pure white light signaled the activation of the Teleport spell, and he moved to Area A.

“Why are there nine instead of ten?”

—Because an urgent matter came up.

“An urgent matter. Who is missing?”

—Kim Ho-jung.

“Kim Ho-jung?”

—Yes.

Listening to the Team Leader’s dry voice, Go Se-won crossed the hallway in Area A. His mood soured with each sharp click of his dress shoes.

“That’s strange. I don’t remember receiving any report.”

—My apologies.

“I’m not asking for an apology. I’m asking for the reason. Did he leave without permission?”

—Of course not.

*Of course not.*

Go Se-won muttered inwardly.

The security team was a pack of hunting dogs raised by the dead Lee Jungryong.

For a long time, Lee Jungryong had secretly operated enormous orphanages and children’s homes, instilling loyalty in orphans who had nowhere else to go.

He had been the same way. So were they.

And Team One consisted of only the most loyal and capable members. The odds of a member of Team One going AWOL were even lower than the odds of a Monster Wave.

Especially someone like the missing Kim Ho-jung.

*Which meant…*

Ares Guild had many senior executives and elders, but the security team obeyed the orders of only two people.

The fact that Kim Ho-jung had disappeared without reporting to Go Se-won, one of those two people, could mean only one thing.

*Step.*

His unimpeded stride came to an abrupt halt.

Go Se-won silently stared at a door with no nameplate or decoration when a bright voice rang out from beyond it.

“Come in. Don’t loiter outside.”

“...!”

Swallowing hard, Go Se-won opened the door and entered. In the neatly arranged room, his sole direct superior was waiting for him.

“Nice weather today. Don’t you think so, Team Leader Go?”

“Yes.”

Go Se-won gave a brief bow, then quickly swept his gaze around the room.

The pleasant smile at Go Jun’s lips. The whiskey glass in his hand. And the object he was rolling around in his other hand.

*What is that?*

This was not the Go Jun he usually knew. Everything in the room felt strange and unsettling to Go Se-won.

Perhaps it was because of the noise drilling into his ears.

*Grind. Grate.*

Go Jun’s voice blended with the irritating sound of friction.

“You don’t need to worry about that Kim Ho-jung fellow, Team Leader Go. I gave him a separate assignment.”

“I see.”

“Aren’t you curious what kind of assignment it was?”

Their gazes collided in midair. Looking into Go Jun’s unusually red eyes, Go Se-won politely lowered his head.

“No. If it was the Vice Guild Master’s order, I’m sure there was a good reason.”

“That’s a nice answer to hear. I thought you’d been feeling a little hurt by me lately. I’m younger than you, after all, and you were always especially devoted to Master.”

“How could that be? It’s true that I owed a debt to the former Vice Guild Master, but that does not lessen my loyalty.”

“Is that so? Then that’s a relief.”

*Grind.*

Go Jun rubbed the object in his grasp once more, then smiled pleasantly and swirled his glass.

“The weather is nice. How about a drink?”

Go Se-won answered calmly.

“I’m sorry, but…”

“You mean you won’t drink? What a shame. It’s good liquor.”

Go Jun leisurely emptied his glass. Go Se-won watched him in silence before suddenly speaking.

“There is an urgent matter I need to report.”

“Go ahead.”

“In Busan…”

Go Se-won trailed off the moment he saw the holographic PC sitting on the table where Go Jun had set down his glass.

The paused screen showed an enormous octopus and the devastated remains of Gwangan Bridge.

“In Busan, what?”

“…”

After a brief silence, Go Se-won murmured,

“You already knew.”

Go Jun let out a low laugh.

“I did. Before anyone else.”

The bright voice had not changed, but Go Se-won felt his heart sink.

As the unease he had tried to dismiss revealed its true shape, he forced himself to speak calmly.

“Then Kim Ho-jung… Is he in Busan right now?”

“I seem to remember you saying you weren’t curious a moment ago.”

“I’m sorry. It slipped out.”

“Forget it. You need to know, anyway.”

Go Jun answered pleasantly as he filled his empty glass with whiskey.

“That’s right. Kim Ho-jung is in Busan on my orders.”

After thinking for a moment, Go Jun added,

“He might be gone by now.”

“...!”

“Don’t just stand there. Sit down and have a drink. My neck hurts from looking up at you.”

This time, Go Se-won could not refuse. No—there was no reason to refuse.

He needed to drink, if only to calm the turmoil raging inside him.

*Gulp, gulp.*

He downed the strong whiskey in one swallow, and only then did he feel as if he could breathe again.

Clutching the empty crystal glass, Go Se-won hesitated before barely squeezing out his voice.

“Vice Guild Master. I don’t know how you managed to make something like this happen, but this method cannot inflict much damage on them.”

“Why do you think that?”

“He… No, Jin Taekyung is there. He’s the man who even took down an Arch Lich. He’s already suppressing this Monster Wave quickly. All this will do is add to the Peace Guild’s reputation.”

“Yes. That’s right. Jin Taekyung. He really is something.”

Go Se-won had brought up the name despite knowing he might provoke his superior’s anger. Yet contrary to his expectations, the smile remained on Go Jun’s lips.

And that gentle smile made Go Se-won feel even more uneasy.

“Vice Guild Master. Don’t tell me…”

“If you want to capture the commander, you have to lure out the general. It’ll cause an uproar if this becomes known, but there won’t be any consequences afterward.”

“...!”

“Jin Taekyung is untouchable for now. But Choi Minwoo is a different story. Don’t you agree?”

*Grind. Grate.*

Along with the irritating sound of friction, one name flashed through Go Se-won’s mind like a bolt of lightning.

“Song Cheonwoo. It’s Song Cheonwoo.”

“Correct. I’ll give you another drink as your reward.”

Go Se-won accepted the drink, hiding the trembling of his fingertips. He could not begin to estimate where things had gone wrong.

Even so, he was certain that his superior’s plan would fail.

“…Choi Minwoo is a cautious man. On the surface, he is the master of the Peace Guild, and he also has Kim Hwajong, who has served him loyally at his side for a long time.”

“I know. Master mentioned Kim Hwajong several times. And if we include the other security personnel, Song Cheonwoo couldn’t handle it alone.”

“Vice Guild Master. Then why in the world—”

*Graaaate!*

The loud sound of friction drowned out Go Se-won’s voice.

Instead of answering, Go Jun let out a short laugh and opened his palm. The object he had been clutching all along finally revealed itself.

It was about the size of an egg, filled with darkness that looked as though it had gathered an abyss and sealed it inside. Its name slipped from Go Se-won’s lips.

“A Magic Gem…”

He would not have been surprised if it had been an ordinary Magic Gem.

But the object resting on Go Jun’s palm could only come from a Named Monster. It was what people called an S-grade Magic Gem.

Pure, unrefined mana churned inside it.

“V-Vice Guild Master.”

Only now did Go Se-won understand how Go Jun had been able to cause the Monster Wave artificially.

At Go Se-won’s voice, filled with both dread and lament, Go Jun muttered quietly,

“Choi Minwoo. That man will die today. Without fail.”

And the one who killed Choi Minwoo would be one of two things.

An old man whose family had been taken hostage.

Or another being whose identity even Go Jun himself could not clearly determine.

“One thing is certain. Song Cheonwoo has no choice.”

Go Jun murmured softly and smiled with satisfaction.

As he habitually stroked the old necklace around his neck, darkness flickered in his eyes.

* * *

If someone asked how Song Cheonwoo had managed to move in such a serious physical condition, he would answer with one word.

Will.

That was exactly what it was. The last strength he had dragged up through sheer willpower. The nearly seventy-year-old man threw himself toward death with every ounce of strength he had left.

*Flash! Whoosh!*

The world slowed.

The cold sensation of snow disappeared, replaced by a buoyant feeling that seized his entire body.

In that brief moment, split and split again into fragments, Song Cheonwoo met the wide-open eyes of two people staring at him.

Choi Minwoo and Kim Hwajong. Their eyes seemed to ask the same question.

*Why?*

Song Cheonwoo muttered an answer to the question in their hearts.

*Because this is the only way.*

If it had been a few days ago, he probably would have taken Choi Minwoo’s hand.

But Go Jun, whom he had faced for the last time, had become… a monster.

Song Cheonwoo had sensed madness in his eyes. If Song Cheonwoo left this place alive, Go Jun would eliminate his family without the slightest hesitation.

Neither the Peace Guild, nor even Jin Taekyung or *that person*, could resolve that problem.

*So this is how it ends, in the end.*

Along with that fleeting thought, Song Cheonwoo fell toward the pitch-black darkness.

The darkness had no end in sight. It resembled the mouth of a monster.

It also resembled his life.

*Was it Nietzsche?*

Someone had said that if you stared into the abyss, you became the abyss as well.

Song Cheonwoo realized that too late.

By then, everything was already too late.

*SHWAAA!*

A cold, savage wind battered his entire body.

Amid the howl of the vicious wind, a conversation he had shared with someone a few days ago seemed to press into his ears.

*“This.”*

*“Put it away. As you know, Director, it’s an extremely dangerous object. It’s expensive, too.”*

*“…You bastard. You’re insane.”*

*“You need to be insane, too. If you want to save your family.”*

The man had been insane, and it had been an insane conversation.

And after agonizing over it for what felt like ten years in a single day, Song Cheonwoo had not used *it* until the very end.

*Was that the last thing I did right?*

As the wind grew more violent, Song Cheonwoo sensed something approaching through the darkness and closed his eyes.

*Crack! Crunch, crunch, crunch!*

The end of his long fall.

First, his neck broke. Then every bone in his body was crushed.

And in the next moment, Song Cheonwoo heard the cry of something through his fading consciousness.

—Grrrr.

It was the eerie cry of a monster unlike anything he had ever heard before.

He wanted to say something, but the being that had crouched in the abyss for countless years did not allow its prey any last words.

*Crack!*

Darkness came.

Enormous teeth crushed the body from which life had already fled and drank its blood.

Even the object Song Cheonwoo had kept deep in his pocket—something he had never used until the end because he wanted to die as a human being, not as a monster.

*Whoosh.*

The darkness itself became light and burst forth.
```

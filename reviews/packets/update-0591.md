<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0591.txt",
      "sha256": "6e5279fd236811c1cbe015c7ff5f8e6e7e770d7fefa2cb6e79ffeabfaaa2667a",
      "bytes": 22645
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "f7a6dc6d973fd4aac3dc8ddf9099b9b8aa3a2337894df5e4bcd785a7a2320b86",
      "bytes": 3169
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "774d8cc5ec7f4a500f461f0481a4619f9e38ab5848bfb9966cf2bb3eb4c3f0ce",
      "bytes": 184774
    },
    {
      "path": "characters/Cheonwoo.md",
      "sha256": "26280f844dfbef30e9e7c9e4e9f13c1dadcde1dbff2538c2977f0a315d701c61",
      "bytes": 590
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "72610b3a93e17e78cd876f5f797a944b148a4180287f837542550c14e2a3b150",
      "bytes": 553
    },
    {
      "path": "characters/Go Jun.md",
      "sha256": "1e340d8f1ddab3afb4d793fab9b2a417ffd7964256e3cfae898a4000e63284ee",
      "bytes": 1030
    },
    {
      "path": "characters/Go Se-won.md",
      "sha256": "a2352d1156e2917cc115d3ae2ea50b5dcf3240c7579472139e5c59267d244f08",
      "bytes": 760
    },
    {
      "path": "characters/Hwa-jong.md",
      "sha256": "30c28e308ed0eb0d16ef04fce1b3ca71b4588e212a99ea34becbbbec2e3e7d42",
      "bytes": 646
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "1ff894925ea95395468932d56e9ff8245d4bac32d5aea0259083257cc1b34158",
      "bytes": 2315
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "f0e09f8316b86f65e6823d4665dff2d5d2ca54362d5ecb151a96bbbbe1501d2e",
      "bytes": 622
    },
    {
      "path": "characters/Kim Hwajong.md",
      "sha256": "da0f5646a3d63a903730c1cdf7ccc598e54b6e55c0dc73959c5ac4961c8f4880",
      "bytes": 694
    },
    {
      "path": "characters/Lee Jungryong.md",
      "sha256": "253a85717cb8460dd3d870f7b0f3c7c23e6f938fc6c444aeee7285e12fcbe356",
      "bytes": 1384
    },
    {
      "path": "characters/Song Cheonwoo.md",
      "sha256": "e3dfcef55b8e71712353d58e30cb74996a7463c9a05b6504bc15d4beb9e8637f",
      "bytes": 1080
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "1a4c6696b137cb34859d9ded97221658ba834a502778abb81fe8a8ca5aeeff21",
      "bytes": 182018
    }
  ],
  "estimated_tokens": 17592
}
-->

# Durable State Update — Chapter 591

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 591. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 591. Profile updates may replace only one
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
  "chapter": 591,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 591,
    "continuity_sources": [591],
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
    "Kim Hwajong died after sacrificing himself to restrain Behemoth, and Choi Minwoo remains unconscious after being transported from the battlefield.",
    "Behemoth's Turbid Abyss is a Supreme Peak Magic Gem that absorbed another source of mana and requires purification before use.",
    "Jin has entered Ares Guild headquarters, incapacitated roughly two hundred elite Ares Hunters, and continues toward Go Jun while the Skeleton King protects the Peace Guild and its people.",
    "Go Jun intends to kill Jin Taekyung within one year and relies on Ares's political, prosecutorial, corporate, and media influence plus Lee Jungryong's corruption ledger for protection.",
    "Go Se-won openly opposes Go Jun's crimes and cover-up orders and intends to resign if he survives.",
    "Cheon Taemin collapsed more than twenty years ago and remains unconscious at an unknown location, with Area A only suspected.",
    "Song Cheonwoo and Lee Jungryong concealed Taemin's condition and purged those who knew the truth.",
    "Busan's Kraken is dead, but more than one thousand Mermen remain across Haeundae and Gwangalli.",
    "Go Jun seized Song Cheonwoo's children, used an S-grade Magic Gem to cause the Busan Monster Wave, and targeted Choi Minwoo.",
    "Song Cheonwoo was killed by an unidentified monster after falling into an abyss; the object in his pocket released darkness that became light.",
    "Jin concludes that Go Jun used a stand-in to make it appear that Song Cheonwoo returned to the United Kingdom, then destroys a lifelike statue of Lee Jungryong and orders Ares's remaining defenders to choose a side."
  ],
  "continuity_sources": [
    590
  ],
  "open_questions": [
    "What caused Cheon Taemin's collapse, and what happened during his more than twenty years of unconsciousness?",
    "Is Cheon Taemin actually being kept in Area A of Ares Guild headquarters?",
    "What is the unidentified being involved in Go Jun's plan, and is it connected to the monster that killed Song Cheonwoo?",
    "What was the object Song Cheonwoo kept in his pocket, and what did its release of darkness and light accomplish?",
    "What is the old necklace Go Jun wears, and why does it matter to his plan?"
  ],
  "safe_through": 590,
  "temporary_decisions": [
    "Use Yeti's Winter Range for 예티의 겨울 산맥, Stone King for 스톤 킹, Behemoth for 베히모스, and Behemos for 베헤모스; use Area A for A구역 and Mount Balwang for 발왕산.",
    "Use Hero's Soul for 영웅의 혼, Hyung for 형님, S-grade Magic Gem for S급 마정석, Hell Fire for 헬 파이어, and Hellfire Mage for 겁화의 마법사.",
    "Use final rally for 회광반조, Young Master for 도련님, Rodin's The Thinker for 로댕의 생각 난 사람, and Teleport for 텔레포트.",
    "Use Code Red for 코드 레드, Multi Shot for 멀티 샷, Binding for 바인딩, Tower Shield for 타워 실드, and great tiger for 대호.",
    "Use Flame-Extinguishing Divine Fist for 멸염신권, Flame Divine Palm for 화염신장, White Flame for 백염, Force for 강기, and eight-tenths mastery for 팔 성."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 김화종    | **Kim Hwajong**   |
| 이정룡    | **Lee Jungryong** |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 돌파     | **break through** / **breakthrough**             | Realm advancement                                     |
| 살기     | **killing intent**                               |                                                       |
| 검기     | **Sword Energy**                                 | When functioning as projected weapon qi               |
| 사형     | **Senior Brother**                           |
| 일격     | **One Strike**                         |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 레이드     | **raid**              |
| 길드      | **Guild**             |
| 길드장     | **Guild Master**      |
| 부길드장    | **Vice Guild Master** |
| 팀장      | **Team Leader**       |
| 탱커      | **tank**              |
| 대격변     | **Great Cataclysm**   |
| 천우 | **Cheonwoo** | Name shown in a Level Window; one of the five current Five Gates scions. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 고준 | **Go Jun** | Personal name of Team Leader Seok; Lee Jungryong's prized Disciple. |
| 고세원 | **Go Se-won** | Ares Guild Head of Security and Team Leader. |
| 화종 | **Hwa-jong** | Butler Kim's personal name. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 송천우 | **Song Cheonwoo** | Ares Guild Director, former third-ranked Korean Hunter, and longtime European regional branch director. |
| 금나수 | **grappling technique** | Close-combat wrist-lock technique; rendered descriptively |
| 화염신장 | **Flame Divine Palm** | Jopil's deadly palm technique, noted when Taekyung compares Jopil with Mukyung. |
| 아레스 | **Ares Guild** | The leading Guild in Korea; formerly employed Team Leader Choi and Song Song. |
| 화시 | **fire arrow** | Flaming arrow Lee Seowol fires to signal Cheol Mubaek. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 허공섭물 | **Seizing an Object Through Empty Space** | Technique Jeok Cheongang uses to lift Jang Taebo remotely. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 염화일로 | **Flamefire Path** | Fire Gate Clan signature movement technique; Jeok Cheongang has reached its ninth stage. |
| 석고준 | **Go Jun** | Source full-name form for the established Go Jun, also known as Team Leader Seok. |
| 경호팀장 | **Head of Security** | Go Jun's security-team office under Lee Jungryong. |
| 겁화 | **hellfire** | Destructive fire energy used by Taekyung. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 심맥 | **heart meridian** | Meridian severed by an infiltrator to commit suicide. |
| 지풍 | **Finger Qi** | Invisible qi attack fired by the Western Heaven Demon Lord. |
| 꺽정 | **Kkeokjeong** | Jin's injured ally, addressed as Uncle Kkeokjeong. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 쓰촨 | **Sichuan** | Variant spelling used for the region associated with the pattern Jin recognizes. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 인자 | **ninja** | Japanese assassin skilled in concealment and concealed weapons. |
| 칠공 | **seven apertures** | The seven bodily openings through which Taekyung's overflowing heat escapes. |
| 국가장 | **national funeral** | State funeral held for Lee Jungryong. |
| 정룡 | **Jungryong** | Cheon Taemin's trusted associate who joined the Peace Guild. |
| 사냥개 | **hunting dog** | Jin's demeaning metaphor for Ares personnel who obey Go Jun. |
| 철옹성 | **impregnable fortress** | Metaphor for Ares Guild's entrenched defenses. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 김화종 | 진태경 | senior_Hunter_to_younger_Hunter | Mr. Jin | formal-polite | Hwajong addresses Taekyung as 진태경 씨 while proposing an exchange of stories. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 이정룡 | 진태경 | senior S-rank Hunter to younger Hunter and adversary | Young man | polished, teasing, and veiled-threatening | Uses a genial tone and indirect threats while trying to make Taekyung release the captives. |
| 진태경 | 이정룡 | younger Hunter to senior S-rank Hunter and adversary | you | polite but mocking and defiant | Taekyung answers Lee's soft threats with the wolf-and-tiger metaphor and refuses to yield. |
| 이정룡 | 고준 | Master to Disciple | Go Jun | familiar and testing | Lee switches from Seok's office title to his personal name while considering whether he can defeat Taekyung. |
| 고준 | 이정룡 | Disciple to Master | Master | deferential | Go Jun responds to Lee's personal-name address as 스승님. |
| 진태경 | 석고준 | returning Hunter to hostile Ares security leader | you fucking bastard | hostile and profane | Taekyung directs his final insults and challenge at Go Jun after returning alive. |
| 석고준 | 진태경 | hostile_opponents | brat | hostile and overconfident | Go Jun addresses Taekyung internally as 애송아 while launching his full-strength attack. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 중년인 | 진태경 | veteran civilian Hunter to celebrated allied Hunter | Mr. Jin | formal-polite and awed | The casualty clerk addresses Jin as 진 선생님 after Jin asks him to list Lei Fei among the dead. |
| 진태경 | 중년인 | celebrated Hunter to older fellow Hunter | sir | casual and teasing | Jin addresses the older Hunter as 아저씨 while joking with him and giving him instructions. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 고준 | 진태경 | Ares Guild combatant confronting the killer of his Master | you | hostile and informal | Go Jun uses 너 while demanding Jin confess to Lee Jungryong's death and threatening retaliation. |
| 진태경 | 고준 | dominant adversary confronting Lee Jungryong's Disciple | you | contemptuous and informal | Jin uses 너 and 놈 while overpowering Go Jun and ordering him to end the conflict with Lee Jungryong. |
| 팀원 | 석고준 | subordinate security-team member to security-team leader | Team Leader | fearful formal-polite | The team member repeatedly addresses Go Jun as 팀장님 while reporting the strange object. |
| 석고준 | 고세원 | Ares Vice Guild Master to Head of Security | you | curt and informal | Go Jun tells Go Se-won that he is later than usual when Se-won enters the wrecked office. |
| 고세원 | 석고준 | subordinate_to_Vice_Guild_Master | Vice Guild Master | formal-deferential | Uses 부길드장님 while trying to stop Go Jun from watching the broadcast. |
| 송천우 | 석고준 | adversary; captor of Song's children | you | shocked and confrontational | Song reacts directly to Go Jun's admission that he took the children. |
| 고세원 | 송천우 | Ares security-team leader to Ares regional branch director | Director | formal-polite but threatening | Go Se-won repeatedly addresses Song as 지사장님 while escorting him out. |
| 송천우 | 고세원 | Ares regional branch director to security-team leader | Go Se-won | informal and confrontational | Song directly calls Go Se-won by name while challenging his knowledge of Go Jun's plans. |
| 팀원 | 고세원 | security-team subordinate to security-team leader | Team Leader | alarmed formal address | A security-team member calls out to Go Se-won when Song grabs him. |
| 팀원 | 팀장 | team member to team leader | Team Leader Kim | casual, familiar, and dialectal | Team members use forms including 햄 and informal greetings when addressing Kim. |
| 송천우 | 화종 | former_allies | Hwa-jong | familiar and informal | Song uses Hwa-jong's personal name, prompting Hwa-jong to reject the familiarity. |
| 화종 | 송천우 | former_allies_now_hostile | you | formal and cold | Hwa-jong challenges Song's right to expect Choi's trust and rejects their former intimacy. |
| 팀장 | 중년인 | Hunter_team_leader_to_stranger | Boss | casual and polite | The Team Leader mistakes disguised Song for an ordinary raid customer and warns him not to proceed. |
| 고세원 | 경호팀 | security-team commander to subordinate unit | Security Team | terse operational command | Calls the unit over radio before requesting status reports. |
| 팀장 | 팀원 | freelance team leader to subordinate team member | asshole/punk | insulting-casual | The Team Leader addresses the subordinate with 새꺄 and 인마 while joking and complaining over drinks. |
| 길드원 | 진태경 | Peace Guild member to allied S-rank Hunter | Hunter Jin Taekyung | formal-polite and hesitant | A Guild member addresses Taekyung as 진태경 헌터님 while asking whether Choi should be awakened. |

## Listed compact profiles

### Cheonwoo.md

# Cheonwoo (천우)

- **Safe through:** Chapter 590
- **Aliases:** None
- **Role:** One of the five current Five Gates of Shanxi scions and a First Rate martial artist present at Honghwa Inn.
- **Personality:** Pampered and contemptuous toward Cheongpung's group as part of the five scions' collective mockery.
- **Voice:** Mocking in the group's exchange; no distinct individual speech is established.
- **Relationships:** Associates with Seongryong, Myeonghwa, Sohye, and Jintae as a group of current Five Gates scions.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 587
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Go Jun.md

# Go Jun (고준)

- **Safe through:** Chapter 590
- **Aliases:** Team Leader Seok
- **Role:** Go Jun is Ares Guild's Vice Guild Master, Lee Jungryong's disciple and former Head of Security, and the de facto successor to Lee's Ares legacy who passed the S-rank Hunter qualification assessment with a very high score but lacks Lee's legitimacy.
- **Personality:** Disciplined and controlled under ordinary pressure, fiercely loyal to Lee Jungryong, but consumed by humiliation and rage when Ares Guild's authority is challenged.
- **Voice:** Dry, controlled, and formal with subordinates; deferential when addressing his Master.
- **Relationships:** Disciple and direct protégé of Lee Jungryong, Go Jun inherited Lee's Ares Guild legacy after his death, regards Jin Taekyung and Choi Minwoo as enemies seeking to take it away, has seized Song Cheonwoo's children as leverage, and used an S-grade Magic Gem to trigger the Busan Monster Wave while targeting Choi.

### Go Se-won.md

# Go Se-won (고세원)

- **Safe through:** Chapter 587
- **Aliases:** Head of Security
- **Role:** Go Se-won is Ares Guild's Head of Security and a Team Leader with privileged access to restricted Section A.
- **Personality:** Composed and confident in public, he is mildly uncomfortable with Ares Guild's increasingly severe discipline but obeys its policy.
- **Voice:** Calm and deferential toward superiors, but blunt and decisive when issuing orders.
- **Relationships:** Go Se-won reports to Vice Guild Master Go Jun, commands Ares Guild's thirty-member security team, carried out Go Jun's abduction orders, and now opposes his Monster Wave crimes and intends to resign if he survives.

### Hwa-jong.md

# Hwa-jong (화종)

- **Safe through:** Chapter 590
- **Aliases:** Butler Kim
- **Role:** Hwa-jong was Choi Minwoo's loyal butler and personal escort who sacrificed his life to restrain Behemoth and died after Jin Taekyung killed it.
- **Personality:** Loyal, vigilant, and uncompromising toward perceived threats to Choi Minwoo.
- **Voice:** Formal and deferential toward Choi Minwoo, cold and openly hostile toward Song Cheonwoo.
- **Relationships:** Hwa-jong serves Choi Minwoo and was formerly close to Song Cheonwoo, but their relationship ended over loyalty and ambition.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 590
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, a Supreme Peak master who possesses the Heavenly Martial Physique and superhuman physical strength, has manifested Force, opened his Middle Dantian, crossed the wall into true mastery, has achieved Three Flowers Gather at the Crown but not Five Qi Returning to Origin, can perceive the texture of qi well enough to sever layered magic, can resist high-level monster Fear through exceptional mental strength, is publicly recognized as an S-rank-level Hunter while formally retaining an A-rank license pending testing, can command coordinated raids against powerful monsters, serves as one of the two pavilion masters of the Alliance Leader's direct Fire Dragon Pavilion, leads its first mission to Nanman, has withdrawn from the Peace Guild, and has entered Ares Guild headquarters to confront Go Jun.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor and assigned him a final task to incorporate martial principles into his learned martial arts but declined Taekyung's recruitment after Cheongpung reached him first, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate, student, and trusted manager of media and official arrangements, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, and Xiao Shen regards him as an older brother after Jin saved him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 590
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Kim Hwajong.md

# Kim Hwajong (김화종)

- **Safe through:** Chapter 590
- **Aliases:** Butler Kim
- **Role:** Kim Hwajong was a Level 80 mage known as Butler Kim and Choi Minwoo's loyal butler and personal escort who sacrificed his life to restrain Behemoth and died after Jin Taekyung killed it.
- **Personality:** Gentle and composed as Butler Kim, but retains a fiery temperament and a habit of swearing.
- **Voice:** Gentle and measured
- **Relationships:** Kim Hwajong formerly instructed Im Chunsoo, who remains terrified of and obedient to him, and serves Choi Minwoo as butler and personal escort, having become Choi's only family.

### Lee Jungryong.md

# Lee Jungryong (이정룡)

- **Safe through:** Chapter 590
- **Aliases:** None
- **Role:** Former Vice Guild Master of Ares Guild, one of Korea's two S-rank Hunters, and a Supreme Peak-level martial artist who was killed by Jin Taekyung.
- **Personality:** Outwardly genial, calm, and humorous; calculating, opportunistic, manipulative, coercive, and ruthless when challenged
- **Voice:** Smooth, good-natured, and indirect, using teasing conversation and veiled threats before becoming openly furious
- **Relationships:** Master of Park Jihoon and Go Jun (Team Leader Seok), whom he personally selected and trained; longtime Great Cataclysm acquaintance of Park Tae Seop; adversary of Jin Taekyung; knew Team Leader Choi from childhood; has an antagonistic history with Kim Hwajong, who saved his life at the collapse of Mapo Bridge eighteen years earlier; was visibly shaken by learning that Choi is Cheon Taemin's maternal grandson; regarded Cheon Taemin as an older brother despite no blood relation and long held him in respect and fear; secretly supported the orphanage where Lee Dongseok grew up and was regarded by Dongseok as a father; operated as Ares Guild's senior authority beneath its Guild Master; concealed Taemin's condition with Song Cheonwoo and participated in purging aides who knew the truth.

### Song Cheonwoo.md

# Song Cheonwoo (송천우)

- **Safe through:** Chapter 590
- **Aliases:** Director Song
- **Role:** Ares Guild Director and former A-rank Hunter who reached third place among Korean rankers, briefly headed the Hunter training center, and led Ares Guild's European regional branch for twenty years; after being forced to attack Choi Minwoo to protect his hostage family, he fell into an abyss and was killed by an unidentified monster.
- **Personality:** Highly ambitious, honor-obsessed, politically calculating, and determined to use his final opportunity to reclaim influence before retirement.
- **Voice:** Not established.
- **Relationships:** Song Cheonwoo followed Cheon Taemin since before Team Leader Choi was born, was Lee Jungryong's former friend and rival, helped conceal Taemin's condition and purge aides who knew the truth, negotiated the European regional director position to save himself and his family, and had his children seized by Go Jun as leverage that forced him to attack Choi Minwoo.

## Korean source

```text
＃591화



뚜. 뚜. 뚜.

스마트폰 너머로 한참이나 이어지던 연결음이 어느 순간 뚝 끊겼다.

동시에 기다리던 누군가의 목소리 대신, 익숙하면서도 여전히 낯선 여성의 음성이 귓가를 파고들었다.

- 연결이 되지 않아, 삐 소리 후 소리샘으로 연결되오며…….

평소였다면 끊었을 거다. 아니, 전화도 하지 않았을 거다.

하지만 중년인은 어렴풋이 짐작하고 있었다. 지금 녹음될 자신의 목소리가, 어쩌면 가족에게 남기는 유언이 될지도 모른다는 사실을.

삐이.

신호가 시작되었지만, 차마 입술이 떨어지지 않았다.

무슨 말을 해야 할까. 둘째를 배 속에 품은 아내와 이제 겨우 네 살이 된 자식에게.

그리고 중년인, 고세원이 고심 끝에 입을 열려던 순간이었다.

구구구궁.

건물 전체를 울리는 미세한 진동과 함께, 밖에서 대기하고 있던 경호팀원의 목소리가 문 틈새 사이로 흘러들어왔다.

“팀장님, 가 보셔야 할 것 같습니다.”

“…….”

“팀장님?”

“기다려, 나간다.”

짤막한 대답과 함께 고세원은 통화를 종료했다.

그래, 어쩌면 이건 누군가의 계시인지도 모른다. 죽지 말고 살아남아서 가족들을 만나라는 계시.

만약 그게 아니라면…….

‘유언조차 남길 자격이 없다는 거겠지.’

내심 씁쓸하게 중얼거린 고세원은 문을 열었다. 딱딱하고 무미건조한, 익숙한 얼굴의 경호팀원이 그를 기다리고 있었다.

“죄송합니다. 다름이 아니라 밖에서…….”

“알아, 가지.”

담담하게 말을 끊은 고세원이 발걸음을 옮겼다. 조명이 꺼진 복도를 가로지른 그는 곧 볼 수 있었다.

최상층에 걸맞은 거대한 원형 홀과 완전 무장을 갖춘 일백여 명의 최정예 길드원들을.

그리고…… 홀 안을 가득 메우며 뿜어져 나온 홀로그램 영상을.

- 꽈앙!

굉음과 함께 섬광이 터져 나오고.

- 쉬이이잉!

양 진형에서 솟구친 빛줄기가 서로를 향해 쏘아진다.

- 크아아악!

- 탱커어! 대형 정비!

비명과 고함이 곳곳에서 난무했다. 마치 눈앞에서 벌어지는 것처럼 생생한 그 광경 속에, 서로를 향해 얽혀드는 수백의 헌터가 있었다.

불과 몇 분 전까지만 하더라도 한 길드에 소속되어 있던 그들은 적이 되어 싸우고 있었다.

‘저건.’

고세원은 깊게 가라앉은 눈빛으로 홀로그램 속에서 벌어지는 치열한 전투를 바라보았다.

가장 선두에서 활약하고 있는 낯익은 얼굴들은 송천우가 이끄는 계파의 길드 내 중역들이다.

‘반(反) 아레스라……. 결국 이렇게 되는군.’

머리가 사라진 몸은 곧 쓰러지기 마련이다.

하지만 이번만큼은 아니었다. 송천우라는 머리는 제거되었지만, 잘려 나간 자리에서는 그보다 더욱 강력한 머리가 자라났다.

그렇기에 사형 선고를 받은 몸뚱어리가 일어날 수 있었던 것이다.

홀로그램 영상 속, 인간과 몬스터의 핏물을 뒤집어쓴 채 걸어 나오는 청년이 바로 저들의 새로운 구심점이었다.

“괴물…….”

홀로그램을 바라보던 누군가가 신음처럼 중얼거린 그 순간. 청년, 진태경을 중심으로 청백색의 겁화(劫火)가 타올랐다.

- 화륵. 콰아아아아!

한 줄기의 불꽃이 사방을 불사르며 공간을 가로질렀다.

크고 단단한 타워 실드가 산산조각 나며 부서지고, 철벽처럼 버티고 있던 수십여 명의 탱커가 동시에 튕겨져 나가자 팽팽하게 유지되던 균형이 단번에 무너졌다.

- 크아아악!

- 지금이다! 쳐!

솟구치는 핏물과 쓰러지는 사람들 사이, 단숨에 한 개의 레이드 팀을 무력화시킨 불꽃은 멈추지 않고 계속해서 쏘아졌다.

- 쐐애애애액!

그것은 꺼지지 않는 불꽃이었고, 막을 수 없는 유성이었다.

폭격도 견딜 수 있다는 천장이 도미노처럼 무너지고 층층이 대기하고 있던 병력들이 짚단처럼 쓰러졌다.

불꽃이 움직이는 속도를 따라가지 못한 홀로그램 영상이 잠시 흔들리면, 그는 이미 새로운 층에서 새로운 적들을 쓰러트리고 있었다.

- 마, 막……!

- 꽈아아앙!

그 어떤 것으로도 막을 수 없는 압도적인 무력. 진태경은 한 줄기의 불꽃이 되어 막힘없이 쏘아졌다.

층층이 대기하고 있던 병력들이 속절없이 무너져 내리자, 아직까지도 반신반의하며 결정을 내리지 못하던 송천우 계파의 중역들이 마침내 무기를 거꾸로 들었다.

- 여, 여기는 85층! 김종필 상무와 13팀이 배반. 컥!

- 본부 응답하라! 97층에서 반란이……!

- 쉬이이잉, 퍼엉!

물살이 강해지면 파도가 되고, 눈덩이는 구를수록 그 크기를 부풀리는 법.

현재의 상황이 바로 그랬다. 거세게 타오른 불길이 한 방향을 벗어나 사방으로 번져나가고 있었다.

그리고 고세원은 알고 있었다. 분노를 가라앉히기 전까지, 끝끝내 한 사람을 집어삼키기 전까지 진태경이라는 불꽃은 꺼지지 않을 것이라는 사실을.

“표, 표적이 100층을 돌파했습니다!”

“열두 개 층에서 동시다발적으로 교전이 일어나는 중입니다. 위험 분자들이 표적에게 합류하여 아군과 맞서고 있습니다!”

“표적이 홀로 움직입니다! 103층! 아니, 104층으로 진입했습니다!”

다급한 외침이 사방에서 빗발친다. 처음 최상층으로 불려 왔을 때만 해도 여유롭던 중역들의 얼굴은 어느덧 초조함으로 물들어 있었다.

“이, 이봐. 고 팀장. 하나만 물어봐도 되겠나?”

고세원은 홀로그램 영상에서 눈을 떼지 않은 채 대답했다.

“말씀하십시오, 최 전무님.”

“아까부터 궁금했던 건데 말이야…….”

꿀꺽.

목울대가 일렁린다. 마른침을 삼킨 반백의 최 전무가 모두의 의문을 대신해 입을 열었다.

“도대체. 도대체 부길드장님은 어디 계신 건가?”

고세원은 문득 고개를 돌려 주위를 바라보았다. 일백에 달하는 이들 중, 누구보다 앞서 싸워야 할 한 사람의 얼굴은 어디에도 보이지 않았다.

그러나 암담한 현실과는 반대로 마음은 오히려 더욱 홀가분해진다.

‘그래. 이것으로 된 거겠지.’

물라면 물었고, 짖으라면 짖었다.

대격변이 낳은 수많은 전쟁 고아 중 하나였던 자신이 지금의 위치에 오를 수 있었던 것은 충실한 사냥개로 살았기 때문이었다.

참으로 아이러니하게도, 그 사실이 스스로를 역겹게 만들었다.

‘이것을 마지막으로 그간의 빚은 모두 갚았다. 이제 내가 죽건, 살건 더 이상 당신이랑은 아무 상관도 없어.’

끝끝내 나타나지 않는 누군가를 향해 마음속으로 뇌까린 고세원은 힘주어 검자루를 뽑았다.

스르릉.

날선 소음 사이로 담담한 목소리가 섞여들었다.

“부길드장님은…… 그는 오지 않을 겁니다.”

“뭐, 뭐라고?”

“그러니 살고 싶거든 싸우십시오. 여러분이 그 동안 받아 먹은 먹이는 이제 와서 토해 낼 수 없을 만큼 많으니까.”

이 자리의 모두가 사냥개다. 주인이 주는 먹이를 받아 먹으며 풍요로운 삶을 영위해 온 그들에게, 더 이상의 선택권은 없었다.

‘그래, 나도 마찬가지지.’

문득 실소를 흘리는 고세원의 모습에 중역들이 눈을 부릅뜬 그때, 비명 같은 외침이 거대한 홀을 쩌렁쩌렁 울렸다.

“119층! 표적이 119층을 돌파했습니다!”

“……!”

“……!”

그 말의 의미를 이해하지 못하는 사람은 없었다.

적어도 자신들이 매일같이 출근하는 이 초고층 빌딩이, 120층으로 이루어져 있다는 것 정도는 모두가 알고 있었으니까.

‘온다, 그가.’

피할 수 없는 싸움.

전신 갑주를 착용한 채 한 손에는 검을, 다른 한 손에는 창을 쥔 고세원이 무거운 마음으로 입을 열었다.

“포메이션. 전투 준비.”

나직한 목소리가 일백명의 귓가를 파고든 그 순간.

구구구궁! 콰앙!

거대한 진동을 동반한 굉음과 함께, 세계에서 손꼽히는 마천루(摩天樓)가 흔들렸다.

지금껏 그 누구도 도전할 수 없었고, 도전하지 않았던 철옹성의 최상층에 초대받지 않은 손님이 발을 디뎠다.

저벅.

피어오른 먼지 구름 사이로 보이는 한 사람의 인영.

고세원은 전신의 털이 곤두서는 듯한 감각과 함께, 온힘을 다해 손에 쥐고 있던 창을 흩뿌렸다.

후웅, 쐐애애애액!



* * *



스걱!

나를 향해 쇄도하던 창 한 자루가 먼지구름과 함께 갈라진다.

백염이 그린 궤적을 따라 깨끗해진 시야 너머, 왠지 낯익은 중년인의 얼굴이 눈에 들어왔다.

‘어디서 봤더라.’

의문과 동시에 얼마 되지 않은 기억이 뇌리를 스친다.

이정룡의 국가장이 치러지던 그때, 석고준의 곁을 그림자처럼 지키던 새로운 경호팀장. 그것이 바로 중년인의 정체였다.

그때 지나가듯 들었던 이름이 아마…….

“고세원.”

나직한 부름에 중년인. 고세원의 눈동자가 가늘게 떨렸다.

그것이 내가 그의 이름을 알고 있기 때문인지, 아니면 앞서의 공격을 너무나도 쉽게 파훼했는지는 모르겠다.

다만 확실한 건 드디어 내 질문에 제대로 된 대답을 해 줄 만한 놈을 찾았다는 것이다.

나는 로비에서부터 지금까지 수십 번도 넘게 던진 그 질문을 다시 한 번 입에 담았다.

“석고준. 어디 있어?”

말이 끝나기도 전에 고세원의 손에서 섬광이 뻗어 나왔다.

쐐애애액, 쾅!

간발의 차로 빗나간 투척용 창이 작은 크레이터를 만들며 틀어박힌다. 그리고 그것이 신호였다.

쉬쉬쉬쉭!

마지막 최상층에서 나를 기다리고 있던 것은 고세원뿐만이 아니었다.

거대한 홀을 메운 백여 명의 아레스 길드원. 한 사람, 한 사람이 상위 헌터라 부르기에 부족함 없는 그들이 일제히 공격을 퍼부었다.

화아악!

거대한 기가 요동쳤다. 홀 내부가 푸르고, 붉고, 환한 빛으로 가득 찼다.

지금까지와는 비교할 수도 없는 위력과 촘촘한 화망(火網)을 갖춘 공격 앞에서, 나는 홀로 걸음을 내디뎠다.

저벅. 공력이 실린 발끝이 지면을 밟음과 동시에 피어오른 불꽃이 공기를 뜨겁게 달군다.

‘염화일로(炎火一路).’

화륵, 쐐애애애액!

단 한 걸음이면 족했다. 십 수 미터의 공간을 지워 버린 나는 허공을 향해 일장을 후려쳤다.

청백색의 겁화 앞에 화살이 녹아내리고, 허공을 격하고 날아들던 마법이 모조리 해제되었다.

퍼엉!

물, 땅, 바람, 화염.

열양지기가 불러온 초고온의 열기는 상성조차 무시했다.

4대 원소로 이루어진 공격 마법이 폭발하듯 사방으로 퍼져 나가자 선두의 탱커들이 신속하게 타워 실드를 치켜세웠다.

쾅!

상당한 충격에 가해졌음에도 불구하고 한 치의 흔들림조차 없다. 일말의 피해도 없이 마법의 여파를 막아 낸 타워 실드가 비스듬히 기울었다.

동시에 스물에 달하는 신형이 강철의 벽을 다리처럼 밟으며 솟구쳤다.

파팟!

나는 본능적으로 깨달았다.

이 자리에 모인 이들 전부는 아레스 길드 내에서도 정예로 분류되는 실력자들이었지만, 지금 달려들고 있는 이놈들은…… 격이 다르다는 것을.

‘살기(殺氣).’

간결하고 신속한 움직임. 침착하게 가라앉은 무미건조한 눈빛에서 능숙한 살인자의 냄새가 풍겼다.

빛살처럼 찌르고 휘둘려진 이십여 개의 무기가 번쩍 빛났다.

쉬이이익!

그리고 전신을 향해 쏘아지는 맹렬한 바람 앞에서, 나는 그만 참지 못하고 피식 웃었다.

“지랄한다. 병신 새끼들.”

“……!”

느려진 세상 속, 무미건조한 그들의 표정 위에 경악이 떠오르는 것이 보였다. 하지만 이미 되돌리기에는 너무 늦었다. 나도, 놈들도.

서걱!

백염의 창날을 타고 청백색의 강기가 뻗어나간 순간, 날아들던 무기가 힘을 잃고 분리된 육신이 좌우로 갈라졌다.

일격으로 다섯 개의 몸뚱어리를 열개로 늘리는 마법을 선보인 나는 텅 빈 허공을 향해 주먹을 뻗었다.

퍼엉!

터져 나간 것은 압축된 공기뿐만이 아니다.

은밀히 접근하던 암살자가 머리 없는 시체가 되어 기울어질 때, 놈의 손에 들려 있던 사슬낫은 이미 내 의지에 따라 움직이고 있었다.

쐐애애액, 푸푹!

허공섭물에 의해 휘둘려진 사슬낫이 누군가의 목에 틀어박힌다.

갑작스럽게 찾아온 죽음에 침착하던 눈동자가 부릅떠진 순간, 내 손바닥이 추락하려는 그의 가슴을 짚었다.

퍼엉!

화염신장의 장력이 노린 것은 확인 사살이 아니다. 이미 죽음을 맞이한 동료를 방패삼아 창을 내지르려던 또 다른 적이다.

“크아아악!”

비명과 함께 칠공(漆工)에서 터져 나오는 핏물.

온몸의 심맥이 가닥가닥 끊긴 놈이 고개를 떨구기도 전에 내 신형은 또 다른 적을 찾아 움직이고 있었다.

뻐억!

내뻗은 주먹이 머리를 부수고.

쉭, 푸푸푹!

쾌속하게 쏘아 보낸 지풍이 목과 가슴을 관통한다. 무기를 떨어트린 손아귀로 핏물이 솟구치는 목을 막아 보지만 역부족이다.

“꺼흑. 꺽.”

빠르게 빛이 빠져나가는 눈동자. 이내 힘없이 허물어지는 마지막 적의 모습을, 나는 서늘한 눈빛으로 바라보았다.

‘전부 너희들이 자초한 거다.’

평소의 나였다면 놈들을 살려 두었을지도 모른다. 하지만 오늘은, 지금은 달랐다.

과거 꺽정 아저씨가 블랙 헌터에 당했을 때처럼. 나는 멈추지 않을 생각이었다. 멈출 수 없었다.

‘이 자리에서 보여 줘야 한다. 두 번 다시 같은 일이 벌어지지 않도록.’

나는 무림인이 되기 훨씬 전부터 헌터였다.

21세기에서 태어나고, 이성과 법이 존재하는 문명사회를 살아온 현대인이기도 했다. 그렇기에 쓰촨에서 석고준을 제거하지 못했다.

혼란과 파괴 속에서 제거할 수 있었던 이정룡과 달리, 당시의 석고준은 법치(法治)라는 두 글자로 만들어진 울타리 속에 있었으니까.

하지만 이제는…… 모든 것이 소용없게 되었다.

내 선택으로 목숨을 건진 석고준은 끝끝내 돌아갈 수 없는 강을 건넜고, 나는. 아니 우리는 김화종을 잃었다.

언제나 정중하면서도 부드러운 미소로 말을 건네던 반백의 노집사를 영영 볼 수 없게 되었다.

그것이 내가 이곳에 온 이유다.

법치라는 이름의 울타리를 무너트리고, 스스로 무법자(無法者)가 된 이유.

철벅.

피에 젖은 걸음소리가 유난히도 크게 울려 퍼진다.

거대한 홀 내부는 어느덧 숨 막히는 정적에 잠겨 있었다. 눈앞에서 벌어진 살육으로 인해 얼어붙은 사람들.

그러나 그중 내가 찾는 얼굴은 어디에도 보이지 않는다. 내 의문에 가장 확실한 대답을 해 줄 수 있는 유일한 사람도.

‘고세원.’

석고준의 오른팔을 찾기 위해 고개를 그 순간. 아주 미세하고도 은밀한 파공성이 감각에 닿았다.

쉬이이잉!

나는 돌아섬과 동시에 양손을 합장(合掌)하듯 부딪쳤다.

꽝! 하는 굉음과 함께 손에 붙잡힌 예리한 검날이 내 이마 위에서 멈췄다.

검의 주인, 고세원이 담담한 목소리로 입을 열었다.

“날 찾았나?”

“그래.”

나는 대답과 함께 양손에 힘을 가했다. 동시에 강대한 마나로 형성시킨 검기(劍氣), 아니 오러가 청백색의 강기 앞에 굴복했다

 엄청난 공력을 이기지 못한 검신이 붉게 달아오르며 녹아내렸다.

투두둑. 치이익!

그리고 한때 검이라 불렸던 쇳물이 지면으로 떨어진 순간. 나는 한껏 열기를 머금은 손을 내질렀다.

퍼엉!

일장(一掌)이면 충분했다. 중첩된 방어 마법이 깨져 나가고 갑옷이 부서진다.

그러나 내부를 뒤흔드는 충격에도 고세원은 쓰러지지 않았다. 솟구치는 핏물을 삼킨 그가 건틀렛으로 내 어깨를 붙잡았다.

아니, 붙잡으려 했다.

타다닥, 퍼엉!

물 흐르듯 이어진 금나수(禁拿囚). 그리고 다시 한번 터져 나온 열기에 고세원이 뒷걸음질 치며 손을 뻗었다.

쉭! 건틀렛 사이로 솟구친 칼날이 아슬아슬하게 턱을 스친다. 나는 따끔한 통증을 느끼며 그의 팔목을 붙잡아 비틀었다.

우두둑! 콰직!

인간의 한계를 아득히 벗어난 악력에 건틀렛이 박살나고, 살이 찢어지며 새하얀 뼈가 튀어나왔다.

분명 생각했던 것 이상의 엄청난 고통일 텐데, 고세원은 비명도 지르지 않고 창백해진 얼굴로 한 마디를 툭 내뱉었다.

“끝인가?”

“아니, 아직.”

망설임 없이 대답한 나는 다른 팔을 붙잡았다.

콰드득!

흡. 하고 헛숨을 들이키는 소리가 들렸다.

끝끝내 고통을 참지 못하고 벌어진 고세원의 입술 사이로 핏물과 함께 파르르 떨리는 목소리가 흘러나왔다.

“적당히 하고…… 끝내지.”

“그럴 생각이다. 석고준 그 새끼가 어디에 있는지만 들은 후에.”

“고용 계약서에 명시된 기밀 유지 서약에 따라 알려 주지 못하겠다면?”

나는 고세원의 쇄골을 움켜잡으며 대답했다.

“최소한 적당히로 끝나진 않겠지.”

내 말에 고세원이 힘없이 웃었다.

“아무리 헤집어도 찾지 못했나 보군. 당연한 일이지.”

안타깝게도 그 말은 사실이었다.

끊임없이 몰려드는 사냥개 무리를 쉴 새 없이 때려잡고, 빌딩 내부를 초토화시킨 지금에조차 놈은 나타나지 않았다.

지금까지 얻은 정보 중 유일한 소득이 있다면 그건 바로 놈이 머무르는 비밀 구역의 정체다.

“A구역. 어디인지 넌 알고 있을 것 같은데.”

쿨럭.

핏물을 토해 낸 고세원이 중얼거렸다.

“잘못 걸렸군. 곧 사표를 낼 생각이었는데.”

“혓바닥이 길다. 입 닥치고 털어놔.”

“어렵지 않은 일이지. 하지만 조건이 있다.”

“고, 고 팀장. 설마 저 미친 새끼가!”

어디에나 눈치 없는 놈들이 하나씩은 끼어 있기 마련이다. 하지만 앞으로 나섰던 이름 모를 중역은 곧 조용해졌다.

눈치 없는 것과는 별개로, 목에 지풍을 맞고도 말을 이어 나갈 수 있는 사람은 흔치 않았다.

“조건?”

“그래.”

그리고 고세원이 꺼낸 말은, 나로서도 예상치 못한 것이었다.

“……죽여 달라고?”

고세원이 작게 고개를 끄덕였다. 고통에 경련하면서도 여전히 차분한 그의 눈동자에 내 모습이 비쳤다.

“예전처럼 돌아가기에는 너무 늦었어. 이 자리에서 깔끔하게. 그거면 충분해.”

“…….”

“알아들었다고 생각하지.”

거칠게 숨을 몰아쉰 고세원이 파르르 떨리는 손가락을 들어 어딘가를 가리켰다.

그리고 마침내 알게 된 A구역의 정체에, 나는 멈칫할 수밖에 없었다.

‘허공?’

언뜻 이해하기 힘든 일이었지만, 세상은 그런 것을 마법이라 부른다.

심지어 나는 마법보다 더 위험하고 신비로운 일들을 겪어 온 당사자였다.

‘어디냐.’

텅 빈 허공을 뚫어져라 노려보길 잠시. 나는 피로에 흠뻑 젖은 몸으로부터 낯선 감각이 찾아오는 것을 느꼈다.

‘이건.’

보이지 않는다. 그러나 느껴진다.

매우 은밀하고, 거대한 기운으로 둘러싸인 또 다른 공간이.

그건 존재를 인식하고 있어야만 알아차릴 수 있을 만큼 완벽하게 감춰진 공간이었고, 약속을 지킨 고세원은 파랗게 질려 가는 입술을 달싹였다.

“이제 죽…….”

우우우웅.

말이 끝나기도 전에 어딘가에서 진동음이 울렸다.

그리고 다음 순간, 전신 갑주가 부서지며 드러난 고세원의 정장 하의 주머니에서 미끄러진 스마트폰이 땅바닥을 굴렀다.

툭. 지이잉.

[아내]라고 적힌 발신인의 이름과 함께, 금이 간 화면 속에 한 가족의 사진이 떠올랐다.

환하게 웃고 있는 어린아이와 아내. 그리고 무뚝뚝한 표정의 고세원.

“…….”

순간 침묵이 흘렀다. 나는 말없이 스마트폰 화면 속 사진처럼 금이 간 고세원의 표정을 바라보았다.

죽여 달라던 그의 말을, 이제는 되돌아갈 수 없다고 말하던 담담한 목소리를 떠올리며 입술을 뗐다.

“하나만 묻자.”

“……?”

“왜 오늘이 마지막 출근이지?”

머뭇거리던 고세원이 한숨처럼 대답했다.

“일하다 보니 적성에 안 맞더군. 특히…… 상사가 좆 같아.”

“그래. 알았다.”

고세원은 알고 있을까. 지금의 대답이 자신의 운명을 결정지었다는 것을.

나는 조용히 공력을 끌어올렸다

주먹이 아닌, 다리를 향해.

“당신…….”

쾅!

이어지는 목소리가 굉음에 파묻힌다.

나는 이미 까마득한 허공을 향해 솟구치고 있었다.

맹렬한 바람과, 보이지 않는 손길이 사로잡는 듯한 부유감과, 허락받지 못한 자는 들여보내지 않는 미지의 공간을 느꼈다.

하지만…… 나는 무법자다. 허락이 필요 없는.

‘저곳.’

모든 것에는 흐름이 있다.

나는 심호흡하며 눈을 감았다. 동시에 손에 들린 창날로부터 터져 나온 청백색의 강기가, 허공을 찢었다.

쏴아아악!
```

## Final English reading copy

```markdown
# Chapter 591

Beep. Beep. Beep.

The ringing continued for a long while through the smartphone before abruptly cutting off.

At the same time, instead of the voice he had been waiting for, a familiar yet still strange female voice slipped into his ear.

“Your call cannot be connected. After the beep, you will be connected to voicemail…”

Under normal circumstances, he would have hung up. No—he would never have called in the first place.

But the middle-aged man had a vague suspicion. The voice he was about to record might become the last words he left for his family.

Beeeeeeep.

The tone began, but his lips refused to move.

What was he supposed to say? To his wife, who was carrying their second child, and his child, who had only just turned four?

And just as the middle-aged man—Go Se-won—was finally about to speak after much thought…

Rumble…

A faint vibration shook the entire building. At the same time, the voice of a security-team member waiting outside seeped through the crack in the door.

“Team Leader, I think you need to come out.”

“……”

“Team Leader?”

“Wait. I’m coming.”

With that brief reply, Go Se-won ended the call.

*Yes. Maybe this is a sign from someone. A sign telling me to stay alive and meet my family again.*

*If it isn’t…*

*Then I suppose I don’t even deserve to leave a will.*

Go Se-won muttered bitterly to himself before opening the door. A security-team member with a hard, expressionless, familiar face was waiting for him.

“I’m sorry. It’s just that something happened outside…”

“I know. Let’s go.”

Go Se-won calmly cut him off and started walking. After crossing the unlit corridor, he soon saw it.

A massive circular hall worthy of the top floor, and more than a hundred fully armed elite Guild members.

And…

A holographic image filling the hall.

*BOOM!*

A flash erupted with a deafening explosion.

*Fwoooooosh!*

Rays of light surged from both formations and shot toward each other.

“Graaaaaah!”

“Tanks! Reorganize the formation!”

Screams and shouts erupted everywhere. Hundreds of Hunters tangled with one another in a scene so vivid that it seemed to be happening right in front of them.

Only a few minutes ago, they had belonged to the same Guild.

Now they were fighting as enemies.

*That’s…*

Go Se-won watched the fierce battle in the hologram with deeply sunken eyes.

The familiar faces fighting at the very front were Guild executives from the faction led by Song Cheonwoo.

*An anti-Ares faction… So this is how it ends.*

A body without a head was bound to collapse.

But not this time.

Song Cheonwoo, the head, had been removed, but an even more powerful head had grown from the severed neck.

That was why a body sentenced to death had been able to rise again.

In the hologram, a young man walked forward covered in the blood of humans and monsters. He was the new focal point of those people.

“A monster…”

Someone staring at the hologram muttered the word like a groan.

At that moment, hellfire blazed around the young man—Jin Taekyung.

*Fwoosh! KABOOOOOM!*

A single streak of flame scorched everything in its path as it tore across the space.

Large, sturdy Tower Shields shattered into pieces. Dozens of tanks who had stood firm as an iron wall were sent flying all at once, and the balance that had held steady collapsed in an instant.

“Graaaaaah!”

“Now! Hit them!”

Amid surging blood and falling bodies, the flames that had incapacitated an entire raid team in one blow continued to shoot forward without stopping.

*Screeeeeech!*

They were flames that could not be extinguished and a meteor that could not be stopped.

The ceiling that was supposedly capable of withstanding bombardment collapsed like a line of dominoes, and the forces waiting on each floor fell like bundles of straw.

Whenever the holographic image shook because it could not keep up with the speed of the moving flames, he was already on another floor, cutting down a new group of enemies.

“St-Stop him…!”

*KABOOOOOM!*

Overwhelming force that nothing could block.

Jin Taekyung had become a single streak of flame, shooting forward without obstruction.

As the troops waiting on each floor collapsed helplessly, the Guild executives from Song Cheonwoo’s faction—who had remained uncertain and unable to make a decision—finally turned their weapons around.

“W-We’re on the eighty-fifth floor! Managing Director Kim Jong-pil and Team Thirteen have betrayed us. Gah!”

“Headquarters, respond! There’s a revolt on the ninety-seventh floor…!”

*Fwoosh! Boom!*

When a current grows stronger, it becomes a wave. The farther a snowball rolls, the larger it becomes.

That was exactly what was happening now.

The flames that had burned fiercely in one direction had broken free and were spreading everywhere.

And Go Se-won knew.

The flame called Jin Taekyung would not go out until his anger had settled—until it had finally swallowed one person whole.

“The target has broken through the hundredth floor!”

“Engagements are taking place simultaneously across twelve floors! Dangerous elements have joined the target and are engaging our forces!”

“The target is moving alone! He’s on the 103rd floor! No—he’s entered the 104th!”

Urgent shouts rained down from every direction. When they had first been summoned to the top floor, the executives had worn relaxed expressions. Now, their faces were colored with anxiety.

“H-Hey, Team Leader Go. May I ask you something?”

Go Se-won answered without taking his eyes off the hologram.

“Go ahead, Executive Director Choi.”

“I’ve been wondering about this for a while…”

The man’s throat bobbed.

Executive Director Choi, whose hair was half gray, swallowed dryly before opening his mouth on behalf of everyone present.

“Where… where on earth is the Vice Guild Master?”

Go Se-won suddenly turned his head and looked around.

Among the nearly one hundred people gathered there, the face of the one man who should have been fighting at the very front was nowhere to be seen.

Yet contrary to the bleak reality, Go Se-won’s heart felt lighter.

*Yes. This should be enough.*

When he was told to fetch, he fetched. When he was told to bark, he barked.

He had been one of the countless war orphans born from the Great Cataclysm. The reason he had risen to his current position was that he had lived as a faithful hunting dog.

Ironically, that fact made him disgusted with himself.

*With this, I’ve repaid every debt I owed you. Whether I live or die from now on has nothing to do with you anymore.*

Go Se-won muttered those words in his heart toward the person who still refused to appear, then firmly drew his sword.

*Shing.*

His calm voice mingled with the sharp metallic sound.

“The Vice Guild Master… He isn’t coming.”

“W-What did you say?”

“So if you want to live, fight. You’ve consumed so much food from him that there’s no way you can vomit it all back up now.”

Everyone in that room was a hunting dog.

They had accepted the food their master gave them and enjoyed lives of prosperity. They had no choices left.

*Yes. I’m the same.*

A hollow laugh escaped Go Se-won.

The executives opened their eyes wide at the sight.

Then a scream rang through the enormous hall.

“The 119th floor! The target has broken through the 119th floor!”

“……!”

“……!”

There was no one who failed to understand what those words meant.

At the very least, everyone knew that the skyscraper where they reported to work every day was made up of 120 floors.

*He’s coming.*

An unavoidable battle.

Wearing full-body armor, Go Se-won held a sword in one hand and a spear in the other as he opened his mouth with a heavy heart.

“Formation. Prepare for battle.”

His quiet voice reached the ears of a hundred people.

At that moment—

Rumble! KABOOM!

With a deafening roar accompanied by a tremendous vibration, one of the world’s most famous skyscrapers shook.

An uninvited guest had set foot on the top floor of an impregnable fortress that no one had ever been able—or willing—to challenge.

*Step.*

A lone silhouette appeared through the rising cloud of dust.

Go Se-won felt every hair on his body stand on end. With all his strength, he hurled the spear in his hand.

*Whoosh! Screeeeeech!*

* * *

*Slice!*

A spear rushing toward me split apart along with the cloud of dust.

Beyond the view cleared by the path of White Flame, I caught sight of a middle-aged man’s face that seemed strangely familiar.

*Where have I seen him before?*

As the question crossed my mind, a recent memory surfaced.

At Lee Jungryong’s national funeral, there had been a new Head of Security standing beside Go Jun like a shadow.

That was the identity of the middle-aged man.

The name I had heard in passing back then was probably…

“Go Se-won.”

At my quiet call, the middle-aged man’s—Go Se-won’s—eyes trembled faintly.

I didn’t know whether it was because I knew his name or because I had deflected his earlier attack so easily.

What I did know was that I had finally found someone who could give me a proper answer to my question.

I asked the same question I had thrown out dozens of times since entering the lobby.

“Where is Go Jun?”

Before I had even finished speaking, a flash of light shot from Go Se-won’s hand.

*Whoosh! KABOOM!*

The thrown spear missed me by a hair and embedded itself in the floor, creating a small crater.

That was the signal.

*Fwish-fwish-fwish!*

Go Se-won wasn’t the only one waiting for me on the final top floor.

More than a hundred Ares Guild members filled the enormous hall. Every one of them was skilled enough to be called a high-level Hunter, and they unleashed their attacks all at once.

*Fwoosh!*

Massive qi churned.

The hall filled with blue, red, and brilliant light.

Faced with an attack whose power and dense barrage could not even be compared to anything I had encountered so far, I stepped forward alone.

*Step.*

The instant my foot, charged with internal energy, touched the ground, flames rose and heated the air.

*Flamefire Path.*

*Fwoosh! Screeeeeech!*

A single step was enough.

After erasing a dozen meters of space, I swung a palm strike into the air.

Arrows melted before the blue-white hellfire, and every spell flying through the air was dispelled.

*BOOM!*

Water, earth, wind, and flame.

The superheated air summoned by Scorching Yang Qi ignored even elemental affinities.

As the attack Magic made up of the four elements exploded outward in every direction, the tanks at the front swiftly raised their Tower Shields.

*KABOOM!*

Despite the tremendous impact, they did not shake even an inch.

The Tower Shields tilted diagonally after blocking the aftermath of the Magic without suffering the slightest damage.

At the same time, nearly twenty figures surged upward, using the steel wall as a set of stairs.

*Pat-pat-pat!*

I realized it instinctively.

Everyone gathered here was an elite capable of being classified among Ares Guild’s best.

But these people rushing toward me were on another level.

*Killing intent.*

Their movements were concise and swift. A practiced killer’s scent wafted from their calm, emotionless eyes.

More than twenty weapons stabbed and slashed at the speed of light, flashing brightly.

*Screeeeeech!*

Faced with the fierce wind shooting toward my entire body, I couldn’t help letting out a quiet laugh.

“What a load of bullshit. You fucking morons.”

“……!”

In the slowed world, I could see astonishment rise over their emotionless faces.

But it was already too late to turn back.

For them and for me.

*Slice!*

The moment blue-white Force extended along White Flame’s spearhead, the incoming weapons lost their strength and the bodies attached to them split apart to either side.

With a single strike, I demonstrated the magic of turning five bodies into ten.

Then I thrust my fist toward the empty air.

*BOOM!*

What burst apart was not merely compressed air.

As an assassin who had been approaching stealthily tilted over as a headless corpse, the chain sickle in his hand was already moving according to my Will.

*Whoosh! Thud!*

Wielded by *Seizing an Object Through Empty Space*, the chain sickle embedded itself in someone’s neck.

The calm eyes widened at the sudden arrival of death.

At that moment, I planted my palm against his chest as he began to fall.

*BOOM!*

The palm force of *Flame Divine Palm* was not aimed at confirming the kill.

It was aimed at another enemy who had tried to use his already-dead comrade as a shield while thrusting his spear.

“Graaaaaah!”

Blood burst from his seven apertures with his scream.

Before the man whose heart meridians had been severed throughout his body could even lower his head, I was already moving toward another enemy.

*Crack!*

My extended fist crushed his head.

*Fwish! Fwoosh!*

The Finger Qi I fired at high speed pierced his neck and chest.

He dropped his weapon and tried to block the neck from which blood was gushing, but it was useless.

“Ghk. Guh…”

The light rapidly faded from his eyes.

I watched the last enemy collapse limply with a cold gaze.

*You brought this on yourselves.*

If it had been any other day, I might have left them alive.

But today—right now—was different.

Just as when Uncle Kkeokjeong had been attacked by the Black Hunters, I had no intention of stopping.

I couldn’t stop.

*I have to show them here. So the same thing never happens again.*

I had been a Hunter long before I became a martial artist of the Murim.

I had also been a modern man born in the twenty-first century, someone who had lived in a civilized society where reason and the law existed.

That was why I had been unable to eliminate Go Jun in Sichuan.

Unlike Lee Jungryong, whom I had been able to eliminate amid chaos and destruction, Go Jun had been protected by a fence built from the two-syllable Korean term for the rule of law.

But now…

None of it mattered anymore.

Go Jun had survived because of my choice, then crossed a river from which he could never return.

And I—or rather, we—had lost Kim Hwajong.

I would never again see the silver-haired old butler who had always spoken to me with a polite, gentle smile.

That was why I had come here.

Why I had torn down the fence called the rule of law and made myself an outlaw.

*Splash.*

My footsteps, soaked in blood, rang unusually loudly.

The enormous hall had fallen into suffocating silence.

The people frozen by the slaughter that had taken place before their eyes.

But the face I was looking for was nowhere to be seen.

Neither was the only person who could give me the most certain answer to my question.

*Go Se-won.*

I turned my head to search for Go Jun’s right hand.

At that moment, a faint and stealthy sound of something cutting through the air reached my senses.

*Whoosh!*

I turned around and slammed my hands together as though in prayer.

*KABOOM!*

The razor-sharp blade caught between my hands stopped just above my forehead.

The owner of the sword, Go Se-won, spoke in a calm voice.

“Were you looking for me?”

“Yes.”

As I answered, I tightened my grip with both hands.

At the same time, the Sword Energy—or rather, Aura—formed from tremendous mana yielded before the blue-white Force.

The sword blade, unable to withstand my overwhelming internal energy, glowed red and melted.

*Drip, drip. Hiss!*

The metal that had once been called a sword fell to the ground.

I thrust out the hand that held a tremendous amount of heat.

*BOOM!*

A single palm strike was enough.

Layered defensive Magic shattered, and his armor broke apart.

But despite the impact shaking his insides, Go Se-won did not fall.

He swallowed the blood surging up his throat and grabbed my shoulder with his gauntlet.

No—he tried to grab it.

*Tap-tap-tap! BOOM!*

A flowing grappling technique followed seamlessly.

Then, as heat erupted once more, Go Se-won staggered backward and thrust out his hand.

*Fwish!*

A blade shot out between the gauntlet’s plates and grazed my chin.

I felt a stinging pain, grabbed his wrist, and twisted.

*Crack! KRAK!*

Under a grip far beyond human limits, the gauntlet shattered.

His flesh tore, and stark white bone thrust out.

It must have been agonizing beyond anything he had imagined, but Go Se-won did not scream.

His face had gone pale as he casually spoke one word.

“Is it over?”

“No. Not yet.”

I answered without hesitation and grabbed his other arm.

*KRAK!*

“Hk…”

He sucked in a hollow breath.

In the end, Go Se-won could not endure the pain. Blood seeped between his lips as his trembling voice escaped.

“Take it easy… and finish it.”

“That’s the plan. After I hear where that bastard Go Jun is.”

“What if I can’t tell you because of the confidentiality agreement stipulated in my employment contract?”

I grabbed Go Se-won by the collarbone and answered.

“Then it definitely won’t end with just taking it easy.”

Go Se-won laughed weakly.

“Looks like you couldn’t find him, no matter how much you rummaged around. Naturally.”

Unfortunately, that was true.

Even after beating down the endless stream of hunting dogs and reducing the inside of the building to ruins, he still had not appeared.

If there was one thing I had gained from all the information I had collected so far, it was the identity of the secret area where he was staying.

“Area A. I’m guessing you know where it is.”

*Cough.*

Go Se-won spat out blood and muttered.

“I got unlucky. I was planning to submit my resignation soon.”

“Your tongue’s getting long. Shut up and spill it.”

“It isn’t difficult. But I have one condition.”

“T-Team Leader Go. Surely that crazy bastard isn’t—!”

There was always at least one person who failed to read the situation.

But the nameless executive who stepped forward soon fell silent.

Being oblivious was one thing. Few people could keep talking after taking Finger Qi to the throat.

“Your condition?”

“Yes.”

What Go Se-won said next was something I hadn’t expected, either.

“You… want me to kill you?”

Go Se-won gave a small nod.

Even as pain wracked his body, his eyes remained calm, reflecting my face.

“It’s too late to go back to the way things were. Do it cleanly, here. That’s enough.”

“……”

“I think you understand.”

Breathing heavily, Go Se-won raised a trembling finger and pointed somewhere.

And when I finally learned the identity of Area A, I couldn’t help stopping in surprise.

*Empty air?*

It was difficult to understand at a glance, but the world called such things Magic.

Besides, I had personally experienced things even more dangerous and mysterious than Magic.

*Where is it?*

I stared intently at the empty air for a moment.

Then, from my body drenched in exhaustion, I felt an unfamiliar sensation emerge.

*What is this?*

I couldn’t see it.

But I could feel it.

Another space, surrounded by an enormous and highly concealed energy.

It was hidden so perfectly that it could only be detected by someone who recognized its existence.

Go Se-won had kept his promise.

His lips, turning blue, moved.

“Now… kill me…”

Rumble…

Before he could finish speaking, a vibration sounded from somewhere.

Then, the full-body armor broke apart, and the smartphone slipped from the trouser pocket of the suit beneath it. It rolled across the floor.

*Clunk. Bzzzt.*

The cracked screen lit up with a family photograph beneath the caller name: **Wife**.

A young child and a wife smiling brightly.

And Go Se-won with an impassive expression.

“……”

Silence fell.

Without saying a word, I looked at Go Se-won’s cracked expression, resembling the photograph on the cracked smartphone screen.

I recalled the words with which he had asked me to kill him, and the calm voice that had said it was too late to return.

Then I opened my mouth.

“Let me ask you one thing.”

“……?”

“Why is today your last day at work?”

Go Se-won hesitated before answering with a sigh.

“After working here, I realized it wasn’t suited to me. Especially… my boss is a fucking asshole.”

“Yeah. Got it.”

Did Go Se-won know?

Did he know that his answer had just decided his fate?

I quietly raised my internal energy.

Not toward my fist.

Toward my legs.

“You…”

*KABOOM!*

The rest of his voice was swallowed by the explosion.

I was already surging upward into the distant empty air.

I felt the fierce wind, the sensation of floating as though invisible hands had seized me, and the unknown space that refused entry to anyone without permission.

But…

I was an outlaw.

I didn’t need permission.

*There.*

Everything had a flow.

I took a deep breath and closed my eyes.

At the same time, blue-white Force burst from the spearhead in my hand and tore through the empty air.

*Swoooooosh!*
```

<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0587.txt",
      "sha256": "be719b84e8b89655433e7a152b92055381c780d2d60d474ca07d8776277a2414",
      "bytes": 14517
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "7649c2b0a220c5ef083f08c9571bc795af8ce3df46d192347da06bd11cca5a65",
      "bytes": 2681
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "2ba9fa2ec443fb21cad6b5b046d24f06296923cf9ee19452ea5d6c732c881609",
      "bytes": 183685
    },
    {
      "path": "characters/Cheon Taemin.md",
      "sha256": "408ed4bbe2cc83dd17630ecbf8e29293362c071d42fc3499084aaabad51c166e",
      "bytes": 730
    },
    {
      "path": "characters/Cheonwoo.md",
      "sha256": "567c7fbfc71c1151c52ad2a781e1a7073f08639b9ebba9b686b15825a4a807f1",
      "bytes": 590
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "7c24fced6d231a537d1752353476bccdfe463b9562e089fcce36668c15804445",
      "bytes": 553
    },
    {
      "path": "characters/Go Jun.md",
      "sha256": "f57a470db33a374358b1c26da7e16de2027032771f13821359605ae64c502ae8",
      "bytes": 1030
    },
    {
      "path": "characters/Go Se-won.md",
      "sha256": "c868677660390ea00b3d4848d8abcf35140bc201bb0b073c080e4db734a69e3b",
      "bytes": 850
    },
    {
      "path": "characters/Hwa-jong.md",
      "sha256": "af6c1f796352dc94f813e68bde071b4cb578eb4ceda908c15c0345357195a11c",
      "bytes": 646
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "555865cdc02ca59ed7f0580709e76ff7cbff7f17c9df44dac92088ad49d67de2",
      "bytes": 2317
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "e4b818196b8aaa2c9ee16b5f886f45f9b2fb6818951d03af29930248dbea4e02",
      "bytes": 622
    },
    {
      "path": "characters/Kim Hwajong.md",
      "sha256": "651bd06cb430733ab1e4584eb37966cf11c9d1d64395f45a78464b381a5138a1",
      "bytes": 694
    },
    {
      "path": "characters/Lee Jungryong.md",
      "sha256": "b8b1fbfeffca406d382747a45b95f0d0a5a47ea3a9a59a66c79221a044352e17",
      "bytes": 1384
    },
    {
      "path": "characters/Song Cheonwoo.md",
      "sha256": "2e9cd623def662693a167efd8f41885af131695acc5d8a414104d08fbdc5dc7a",
      "bytes": 1080
    },
    {
      "path": "characters/Team Leader Choi.md",
      "sha256": "a5071ebe6dcfe1065c0cb5a473d7befaeda5a3fc6a827ad9b6e7b24b3ad9a81a",
      "bytes": 1035
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "03c508039e959d670aacf33f65a2e1ca64a8c08c8f20ecb5399c5623c471aeb8",
      "bytes": 181236
    }
  ],
  "estimated_tokens": 13729
}
-->

# Durable State Update — Chapter 587

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 587. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 587. Profile updates may replace only one
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
  "chapter": 587,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 587,
    "continuity_sources": [587],
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
    "Kim Hwajong died after sacrificing himself to restrain Behemoth, and Choi Minwoo remains unconscious beside him.",
    "Behemoth's Turbid Abyss is a Supreme Peak Magic Gem that absorbed another source of mana and requires purification before use.",
    "Jin Taekyung identifies Go Jun as the culprit behind the day's Monster Wave and deaths.",
    "Jin Taekyung has withdrawn from the Peace Guild and is heading to Ares Guild; Skeleton King remains to protect the Guild and its people.",
    "Cheon Taemin collapsed more than twenty years ago and remains unconscious for an unknown reason.",
    "Song Cheonwoo and Lee Jungryong concealed Taemin's condition and purged those who knew the truth.",
    "Taemin is believed to be alive, but his location is unknown; Area A is only suspected.",
    "Busan's Kraken is dead, but more than one thousand Mermen remain across Haeundae and Gwangalli.",
    "Go Jun seized Song Cheonwoo's children, used an S-grade Magic Gem to cause the Busan Monster Wave, and targeted Choi Minwoo.",
    "Song Cheonwoo was killed by an unidentified monster after falling into an abyss; the object in his pocket released darkness that became light.",
    "Jin Taekyung killed Behemoth with One Annihilation and lost Exhaustion and Internal Energy Depletion through the resulting level-up."
  ],
  "continuity_sources": [
    586,
    585
  ],
  "open_questions": [
    "What caused Cheon Taemin's collapse, and what happened during his more than twenty years of unconsciousness?",
    "Is Cheon Taemin actually being kept in Area A of Ares Guild headquarters?",
    "What is the unidentified being involved in Go Jun's plan, and is it connected to the monster that killed Song Cheonwoo?",
    "What was the object Song Cheonwoo kept in his pocket, and what did its release of darkness and light accomplish?",
    "What source of mana did Behemoth's Turbid Abyss absorb, and what purification process will make it usable?"
  ],
  "safe_through": 586,
  "temporary_decisions": [
    "Use Yeti's Winter Range for 예티의 겨울 산맥, Stone King for 스톤 킹, Skeleton King for 스켈레톤 킹, Behemoth for 베히모스, and Behemos for 베헤모스.",
    "Use Area A for A구역, Hwa-jong for 화종, and Behemoth's Turbid Abyss for 베히모스의 혼탁한 심연.",
    "Use Hero's Soul for 영웅의 혼, Hyung for 형님, S-grade Magic Gem for S급 마정석, Hell Fire for 헬 파이어, and Hellfire Mage for 겁화의 마법사.",
    "Use final rally for 회광반조 and Young Master for 도련님.",
    "Use Internal Energy Depletion for 공력 소진 and Teleport for 텔레포트."
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
| 무인     | **martial artist**                               | Default term                                          |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 게이트     | **Gate**              |
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
| 대한민국 | **Korea** | Country reference. |
| 아레스 | **Ares Guild** | The leading Guild in Korea; formerly employed Team Leader Choi and Song Song. |
| 강원도 | **Gangwon Province** | Province named in Taekyung’s joke about the Minotaur’s next life. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 청와대 | **Blue House** | Presidential office mentioned in an online comment about proposed legislation. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 검찰 | **prosecutors’ office** | Government prosecutorial institution that summons and investigates Taekyung. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 준이 | **Jun** | Family nickname used in the form Jun's dad. |
| 석고준 | **Go Jun** | Source full-name form for the established Go Jun, also known as Team Leader Seok. |
| 경호팀장 | **Head of Security** | Go Jun's security-team office under Lee Jungryong. |
| 쓰촨 | **Sichuan** | Variant spelling used for the region associated with the pattern Jin recognizes. |
| 국회의사당 | **National Assembly** | Government building visible from the skyscraper. |
| 부산 | **Busan** | City where the Haeundae Gate crisis occurs. |
| 평창 | **Pyeongchang** | Location in Gangwon Province where the Gate is situated. |
| 베히모스 | **Behemoth** | Mythical monster emerging from the Pyeongchang Gate. |
| 정룡 | **Jungryong** | Cheon Taemin's trusted associate who joined the Peace Guild. |
| 종로 | **Jongno** | Destination named by Taekyung. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 김화종 | 진태경 | senior_Hunter_to_younger_Hunter | Mr. Jin | formal-polite | Hwajong addresses Taekyung as 진태경 씨 while proposing an exchange of stories. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 이정룡 | 진태경 | senior S-rank Hunter to younger Hunter and adversary | Young man | polished, teasing, and veiled-threatening | Uses a genial tone and indirect threats while trying to make Taekyung release the captives. |
| 진태경 | 이정룡 | younger Hunter to senior S-rank Hunter and adversary | you | polite but mocking and defiant | Taekyung answers Lee's soft threats with the wolf-and-tiger metaphor and refuses to yield. |
| 이정룡 | 고준 | Master to Disciple | Go Jun | familiar and testing | Lee switches from Seok's office title to his personal name while considering whether he can defeat Taekyung. |
| 고준 | 이정룡 | Disciple to Master | Master | deferential | Go Jun responds to Lee's personal-name address as 스승님. |
| 이정룡 | 천태민 | younger_to_older_brother_by_choice | older brother | reverent and familiar; internal | Lee Jungryong uses 형님 in unspoken thoughts and regards Cheon Taemin as an older brother despite having no blood relation. |
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
| 송천우 | 천태민 | former subordinate to revered older brother by respect | Hyung | reverent and familiar; shocked | Song Cheonwoo recognizes Cheon Taemin's blood in Choi Minwoo and mutters 형님 while facing Choi. |
| 고세원 | 경호팀 | security-team commander to subordinate unit | Security Team | terse operational command | Calls the unit over radio before requesting status reports. |
| 김화종 | 천태민 | loyal subordinate and trusted comrade to Guild Master | Guild Master | formal and respectful | Kim addresses Taemin as 길드장님 after joining the Peace Guild. |
| 길드원 | 진태경 | Peace Guild member to allied S-rank Hunter | Hunter Jin Taekyung | formal-polite and hesitant | A Guild member addresses Taekyung as 진태경 헌터님 while asking whether Choi should be awakened. |

## Listed compact profiles

### Cheon Taemin.md

# Cheon Taemin (천태민)

- **Safe through:** Chapter 584
- **Aliases:** Slayer
- **Role:** Cheon Taemin is Ares Guild Master and the world's greatest Hunter, known as the Slayer for killing the Demon King and creating the first Mana Cultivation Method during the Great Cataclysm, and he is believed to remain alive after more than twenty years of unconsciousness, with Area A only suspected as his location.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** Maternal grandfather of Team Leader Choi and Jin Taekyung and father of Soyeong; regarded by Lee Jungryong as an older brother despite their lack of blood relation.

### Cheonwoo.md

# Cheonwoo (천우)

- **Safe through:** Chapter 586
- **Aliases:** None
- **Role:** One of the five current Five Gates of Shanxi scions and a First Rate martial artist present at Honghwa Inn.
- **Personality:** Pampered and contemptuous toward Cheongpung's group as part of the five scions' collective mockery.
- **Voice:** Mocking in the group's exchange; no distinct individual speech is established.
- **Relationships:** Associates with Seongryong, Myeonghwa, Sohye, and Jintae as a group of current Five Gates scions.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 585
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Go Jun.md

# Go Jun (고준)

- **Safe through:** Chapter 586
- **Aliases:** Team Leader Seok
- **Role:** Go Jun is Ares Guild's Vice Guild Master, Lee Jungryong's disciple and former Head of Security, and the de facto successor to Lee's Ares legacy who passed the S-rank Hunter qualification assessment with a very high score but lacks Lee's legitimacy.
- **Personality:** Disciplined and controlled under ordinary pressure, fiercely loyal to Lee Jungryong, but consumed by humiliation and rage when Ares Guild's authority is challenged.
- **Voice:** Dry, controlled, and formal with subordinates; deferential when addressing his Master.
- **Relationships:** Disciple and direct protégé of Lee Jungryong, Go Jun inherited Lee's Ares Guild legacy after his death, regards Jin Taekyung and Choi Minwoo as enemies seeking to take it away, has seized Song Cheonwoo's children as leverage, and used an S-grade Magic Gem to trigger the Busan Monster Wave while targeting Choi.

### Go Se-won.md

# Go Se-won (고세원)

- **Safe through:** Chapter 580
- **Aliases:** Head of Security
- **Role:** Go Se-won is Ares Guild's Head of Security and a Team Leader with privileged access to restricted Section A.
- **Personality:** Composed and confident in public, he is mildly uncomfortable with Ares Guild's increasingly severe discipline but obeys its policy.
- **Voice:** Calm and deferential toward superiors, but blunt and decisive when issuing orders.
- **Relationships:** Go Se-won reports to Vice Guild Master Go Jun, commands Ares Guild's thirty-member security team, personally ordered and cleaned up the abduction of Song Cheonwoo's family, and now knows that Go Jun used an S-grade Magic Gem to trigger the Busan Monster Wave and target Choi Minwoo through Song Cheonwoo.

### Hwa-jong.md

# Hwa-jong (화종)

- **Safe through:** Chapter 586
- **Aliases:** Butler Kim
- **Role:** Hwa-jong was Choi Minwoo's loyal butler and personal escort who sacrificed his life to restrain Behemoth and died after Jin Taekyung killed it.
- **Personality:** Loyal, vigilant, and uncompromising toward perceived threats to Choi Minwoo.
- **Voice:** Formal and deferential toward Choi Minwoo, cold and openly hostile toward Song Cheonwoo.
- **Relationships:** Hwa-jong serves Choi Minwoo and was formerly close to Song Cheonwoo, but their relationship ended over loyalty and ambition.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 586
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, a Supreme Peak master who possesses the Heavenly Martial Physique and superhuman physical strength, has manifested Force, opened his Middle Dantian, crossed the wall into true mastery, has achieved Three Flowers Gather at the Crown but not Five Qi Returning to Origin, can perceive the texture of qi well enough to sever layered magic, can resist high-level monster Fear through exceptional mental strength, is publicly recognized as an S-rank-level Hunter while formally retaining an A-rank license pending testing, can command coordinated raids against powerful monsters, serves as one of the two pavilion masters of the Alliance Leader's direct Fire Dragon Pavilion, leads its first mission to Nanman, and has just withdrawn from the Peace Guild after identifying Go Jun as the Monster Wave culprit.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor and assigned him a final task to incorporate martial principles into his learned martial arts but declined Taekyung's recruitment after Cheongpung reached him first, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate, student, and trusted manager of media and official arrangements, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, and Xiao Shen regards him as an older brother after Jin saved him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 586
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Kim Hwajong.md

# Kim Hwajong (김화종)

- **Safe through:** Chapter 586
- **Aliases:** Butler Kim
- **Role:** Kim Hwajong was a Level 80 mage known as Butler Kim and Choi Minwoo's loyal butler and personal escort who sacrificed his life to restrain Behemoth and died after Jin Taekyung killed it.
- **Personality:** Gentle and composed as Butler Kim, but retains a fiery temperament and a habit of swearing.
- **Voice:** Gentle and measured
- **Relationships:** Kim Hwajong formerly instructed Im Chunsoo, who remains terrified of and obedient to him, and serves Choi Minwoo as butler and personal escort, having become Choi's only family.

### Lee Jungryong.md

# Lee Jungryong (이정룡)

- **Safe through:** Chapter 586
- **Aliases:** None
- **Role:** Former Vice Guild Master of Ares Guild, one of Korea's two S-rank Hunters, and a Supreme Peak-level martial artist who was killed by Jin Taekyung.
- **Personality:** Outwardly genial, calm, and humorous; calculating, opportunistic, manipulative, coercive, and ruthless when challenged
- **Voice:** Smooth, good-natured, and indirect, using teasing conversation and veiled threats before becoming openly furious
- **Relationships:** Master of Park Jihoon and Go Jun (Team Leader Seok), whom he personally selected and trained; longtime Great Cataclysm acquaintance of Park Tae Seop; adversary of Jin Taekyung; knew Team Leader Choi from childhood; has an antagonistic history with Kim Hwajong, who saved his life at the collapse of Mapo Bridge eighteen years earlier; was visibly shaken by learning that Choi is Cheon Taemin's maternal grandson; regarded Cheon Taemin as an older brother despite no blood relation and long held him in respect and fear; secretly supported the orphanage where Lee Dongseok grew up and was regarded by Dongseok as a father; operated as Ares Guild's senior authority beneath its Guild Master; concealed Taemin's condition with Song Cheonwoo and participated in purging aides who knew the truth.

### Song Cheonwoo.md

# Song Cheonwoo (송천우)

- **Safe through:** Chapter 586
- **Aliases:** Director Song
- **Role:** Ares Guild Director and former A-rank Hunter who reached third place among Korean rankers, briefly headed the Hunter training center, and led Ares Guild's European regional branch for twenty years; after being forced to attack Choi Minwoo to protect his hostage family, he fell into an abyss and was killed by an unidentified monster.
- **Personality:** Highly ambitious, honor-obsessed, politically calculating, and determined to use his final opportunity to reclaim influence before retirement.
- **Voice:** Not established.
- **Relationships:** Song Cheonwoo followed Cheon Taemin since before Team Leader Choi was born, was Lee Jungryong's former friend and rival, helped conceal Taemin's condition and purge aides who knew the truth, negotiated the European regional director position to save himself and his family, and had his children seized by Go Jun as leverage that forced him to attack Choi Minwoo.

### Team Leader Choi.md

# Team Leader Choi

- **Safe through:** Chapter 584
- **Aliases:** Choi Minwoo (최민우)
- **Role:** Team Leader Choi is Cheon Taemin's only living blood relative, a formidable aura-wielding swordsman who wields Hero's Soul, and is mobilizing every available power to unseat Go Jun from Ares Guild leadership; he was rendered unconscious in the Pyeongchang battle and carried away by Hwa-jong.
- **Personality:** Strategic, candid, controlled, and possessive of the power and influence he intends to inherit.
- **Voice:** Dry, formal, and direct, with calm candor and carefully chosen metaphors.
- **Relationships:** Choi Minwoo is Cheon Taemin's maternal grandson and only living blood relative, was kept out of public knowledge by Lee Jungryong, is closely integrated with Jin Taekyung's family, seeks to acquire the Ares Guild intact, and now knows that Song Cheonwoo and Lee concealed Taemin's collapse and purged aides while he investigates Taemin's fate.

## Korean source

```text
＃587화



공기, 시간.

모든 것이 멈춰 버린 것 같았다. 서울특별시 종로구에 위치한 아레스 길드, 그중에서도 극비리에 감춰진 A구역의 주인에게는 그랬다.

‘어떻게?’

오직 그 의문만이 머릿속을 맴돌았다.

석고준은 옆에 고세원이 있다는 사실도 잊은 채, 굳은 얼굴로 벽면에 설치된 홀로그램 TV를 바라보았다.

정부와 각종 매체에서 띄운 수십여 대의 무인 정찰기로 송신된 영상이 생중계를 통해 흘러나오고 있었다.

- 지금 보고 계신 곳은, 몬스터 웨이브가 발생한 강원도 평창 인근의 발왕산(發王山)입니다. 그리고…….

공영방송의 아홉 시 뉴스를 진행하는 간판 아나운서의 목소리가 흘러나왔다. 침착하고 진중하던 평소와는 달리, 화면에 보이지 않는 그는 잔뜩 격앙되어 있었다.

- 국민 여러분, 보이십니까! 네임드 몬스터인 베히모스의 사체입니다! 그 주위에는 재앙 속에서 살아남은 생존자들이 구급 헬기로 이송되고 있…….

석고준의 눈꺼풀이 파르르 떨렸다.

처참히 토막난 마수의 사체와 생존자들. 그리고 상황을 설명하는 평화 길드원과 아나운서의 목소리가 그의 분노를 더욱 키웠다.

쾅!

굉음과 함께 지난 한 달 사이 열 번도 넘게 교체된 최신형 홀로그램 TV가 먼지가 되어 흩어졌다.

하지만 석고준에게는 아무런 상관도 없는 일이었다.

호흡기를 낀 채 이송되는 최민우가 화면에 잡힌 순간, 모든 것이 무의미해져 버렸다.

‘살아남았다. 최민우가.’

그 사실이 그의 마음을 무겁게 짓눌렀다.

석고준에게 있어 최민우는 죽어 마땅한 놈이었고, 죽여야 할 놈이었다.

그래서 함정을 팠다.

진태경을 부산으로 유인하고, 송천우를 이용하여 이이제이(以夷制夷), 양패구상(兩敗俱傷)을 계획했다.

하지만……

‘무엇이 잘못되었나.’

석고준의 눈동자에 붉은빛이 일렁였다. 그의 손아귀에서는 정화되지 않은 S급 마정석 두 개가 끊임없이 마찰하고 있었다.

까드득. 까득.

무엇을 놓친 것일까.

까드득. 까득.

완벽했다고 생각했다. 아니, 정말로 완벽했을지도 모른다.

다만 이 완벽한 계획의 유일한 결함이 있었다면, 자신의 반대편에는 완벽 이상의 존재가 있었다는 사실이었다.

‘진태경.’

놈이다. 모든 매체가 베히모스의 마력장(魔力障)에 가로막혀 자세한 상황은 알 수 없었지만, 놈이 틀림없었다.

살아 있는 신과 같았던 스승, 이정룡을 죽이고 자신에게 씻을 수 없는 공포를 각인시킨 그놈이 다시 한번 훼방을 놓은 것이다.

절대 피할 수 없는 덫을 놓고 함정을 팠는데도. 그런데도 또다시!

까드드드득!

울분에 찬 외침 대신 소름 끼치는 마찰음이 집무실 내부를 가득 채웠다.

솟구치는 분노를 억누른 석고준은 간신히 목소리를 쥐어 짜냈다.

“송천우…… 송천우는?”

질문에도 돌아오는 대답이 없자, 천둥 같은 고함이 터져 나왔다.

“어찌 되었느냐고 묻지 않나!”

“…….”

“고 팀장! 고세원!”

분노를 토해 내는 상관을 말없이 바라보던 경호팀장, 고세원이 건조한 목소리로 대답했다.

“저희가 입수한 생존자 및 사상자 명단에는 없습니다.”

“게이트 출입 기록은?”

“마찬가지입니다. 사실상 해당 게이트를 소유하고 있는 평화 길드 측에서 일부러 흔적을 남기지 않았던 것으로 예상됩니다.”

“그래, 그렇겠지. 최민우 그 애새끼가 다른 걸 몰라도 조심성 하나는 대단하니까. 응? 안 그래?”

“……예.”

어떤 비밀이 울타리를 넘어가지 않는다는 것은, 극비의 장점이자 단점이다.

석고준은 거칠게 머리를 쓸어올렸다. 앞에 놓인 위스키를 병째로 들이킨 그가 중얼거렸다.

“그래. 그렇다면 일이 개같이 틀어지긴 했어도 어쩌진 못할 거야. 송천우는 미리 준비해 둔 대역으로 알리바이를 입증하든가, 그게 어려워지면 단독 범행으로 몰아가면 돼. 부산은 흔적도 안 남았으니 신경 쓸 것 없고. 그렇지?”

“하지만 부길드장님. 평창 건은 송천우의 단독 범행으로 처리하기에는 사안이 너무 큽니다. 입수한 정보에 따르면 명목상이긴 해도 평화 길드장인 김화종이 사망했고, 송천우는 엄연히 아레스 소속이라…….”

“이봐, 고 팀장.”

순간, 고세원은 전신을 엄습하는 한기를 느꼈다. 얼어붙은 그의 모습이 석고준의 붉은 눈동자에 고스란히 비쳤다.

“그럼 그 큰 사안을, 작게 만들어야지.”

“부, 부길드장님.”

“수백억이든, 수천억이든 상관없어. 검찰에 돈 뿌리고, 국회의사당에 앉아 있는 노인네들 협박하고, 카메라랑 마이크 든 놈들 멱살 잡으라고. 그게 자네가 할 일 아닌가?”

“……!”

고세원의 눈동자가 잘게 떨렸다. 한 사람으로부터 흘러나오는 악의(惡意)와 소름 끼치는 기세가 그를 짓누르고 있었다.

‘어떻게 이런…….’

놀라움을 넘어 경악스러웠다. 불과 몇 달 만에 사람이 이렇게까지 변할 수 있는지. 타락할 수 있는지.

그리고 지금 자신을 억누르는 압도적인 힘은 대체 무엇인지.

아연한 눈빛으로 석고준을 바라보던 고세원의 뇌리에, 문득 며칠 전 들었던 송천우의 목소리가 울려 퍼졌다.



‘인간과 괴물의 경계. 석고준 그놈은…… 이미 괴물이 되어 버렸어.’



맞다. 석고준은, 그의 상관은 이미 괴물이 되어 버렸다.

신앙에 가까운 충성심을 이용하여 수하를 죽음으로 내몰고, 수천. 수만. 어쩌면 수십 만의 사상자가 발생할지도 모를 몬스터 웨이브를 두 번이나 인위적으로 일으켰다.

단순히 자신의 적을 처치한다는 이유 하나만으로.

‘인간으로서 지녀야 할 최소한의 본분도 잊어버린, 괴물.’

고세원이 자신이 느낀 동요를 감추기 위해 안간힘을 쓰던 그때, 석고준이 재차 입을 열었다.

“확실히 처리해. 최민우가 살아남긴 했지만, 적어도 송천우는 처리했으니 이번만 잘 넘어가면 문제없겠지.”

어느덧 평정심을 되찾은 석고준의 목소리는 서늘했다.

비록 외부의 적은 쓰러트리지 못했지만, 내부의 적을 없앴으니 절반의 성공은 달성한 것이나 다름없었다.

이제 대역으로 세운 가짜 송천우가 곧 은퇴 절차를 밟고 사라지면 모든 것이 끝난다.

어떤 소문과 비난도 아레스 길드를 무너트리진 못할 것이었다.

“삼십 년이야. 자그마치 삼십 년이라고. 정계, 재계, 검찰, 미디어…… 모두 아레스의 그늘 밑에서 컸어.”

까드득. 까득.

반석(盤石)을 세운 것은 천태민이지만, 그가 의식을 잃은 뒤 기둥과 지붕을 만든 것은 이정룡이다.

오래전 아레스가 후원했던 젊은 정치인들은 국무총리가 되고, 여당 대표가 되고, 야당의 거물로 자리매김했다. 재계와 검찰. 미디어도 마찬가지다.

아레스 길드가 게이트라는 다이아몬드 광산에서 얻은 천문학적인 금액 중 일부는 검은돈으로 사방에 흩뿌려졌고, 그 씨앗은 울창한 숲이 되어 철옹성을 감쌌다.

석고준은 그 사실을 누구보다 잘 알고 있는 사람 중 하나였다.

그가 스승으로부터 물려받은 것 중에는, 온갖 비리와 약점이 빼곡히 기록된 장부 역시 포함되어 있었으니까.

“설령 모두가 손가락질한다 해도, 정작 우릴 지켜 주는 건 이 세상이다.”

조급함과 분노로 잊고 있었다. 자신이 지닌 힘이 어느 정도인지.

그리고 완전히 여유를 되찾은 석고준의 입가에 진한 웃음이 맺힌 그 순간이었다.

“틀렸습니다.”

“뭐?”

고세원은 형용할 수 없는 눈빛으로, 눈앞에 있는 괴물이자 자신의 상관을 똑바로 직시했다.

“아레스의 이름으로 키워 낸 늙은 정치인들도, 검찰총장도, 일제부터 내려온 기업과 언론 재벌도 부길드장님을 지켜 주진 못합니다.”

“고 팀장. 너 이게 지금…….”

“어느 정도는 맞는 말입니다. 아레스라는 이름이 고작 손가락질과 비난 따위로 무너지지 않을 테니까요. 하지만 온 세상이 지켜 준다고 해도, 한 사람만은 막지 못할 겁니다.”

“……!”

순간, 석고준의 신형이 우뚝 굳었다.

감히 자신의 면전에 대고 헛소리를 지껄이는 경호팀장의 멱살을 잡아챌 생각은 이미 저 멀리 날아간 후였다.

뇌리를 강타한 한 사람의 이름 때문이었다.

‘진태경.’

떨리는 상관의 눈빛에서 생각을 읽어 낸 고세원이 가라앉은 목소리로 말을 이었다.

“잊으셨습니까. 지금 부길드장님께서 믿고 계시는 그 세상을 손수 가꾸셨던 분이, 누구의 손에 쓰러졌는지.”

“……!”

뒤통수를 후려치는 듯한 충격에, 석고준은 자신도 모르게 이를 악물었다.

안타깝게도 눈앞의 빌어먹을 놈이 지껄이는 말들은 모두 헛소리가 아닌 사실이었다.

‘스승님.’

그랬다. 이정룡. 아레스의 주인이자 대한민국의 왕이나 다름없던 그의 스승도 결국 진태경의 손에 죽임을 당했다.

온 세상이 그의 것이었으나 정작 누구도 이정룡을 지켜 주지 못했다.

석고준의 악문 잇새로 끓어오르는 음성이 흘러나왔다.

“고 팀장…… 너 이 새끼.”

“누군가는 반드시 해야 할 말을 했을 뿐입니다.”

“닥쳐라.”

“그것이 부길드장님의 지시라면, 받들겠습니다. 하지만 제 말을 흘려넘겨 듣지는 말아 주십시오.”

“말했지. 그 주둥이 닥치라고.”

드드드득!

순간 석고준의 전신에서 폭발하듯 터져 나온 거대한 기운에, 집무실이 지진이라도 난 것처럼 흔들렸다.

실로 압도적인 힘 앞에 고세원의 안색이 창백하게 변했지만, 그건 지금 그가 느끼고 있는 혐오감에 비하면 아무것도 아니었다.

‘괴물.’

고세원의 눈동자를 스치는 감정을 읽어 낸 석고준이 이빨을 드러내며 물었다.

“고 팀장, 갑자기 미치기라도 한 건가? 정신이라도 나간 거야?”

“…….”

“그나마 실력이 쓸 만해서 팀장 자리에 앉혔을 뿐인데. 팔자에도 없는 감투를 쓰니 세상도 달라 보였어?”

분노에 찬 웃음을 흘린 석고준이 말을 이었다.

“고 팀장, 자네는 겁쟁이고 버러지야. 충언(忠言)이라는 말로 그럴듯하게 포장했지만, 정작 스승님과 나보다 진태경을 더 두려워하지.”

“……아닙니다.”

“발뺌하기에는 늦었어. 서로 인정할 건 하자고. 그래, 진태경 그 개새끼가 강한 건 사실이니까. 하지만 언제까지 그 새끼가 내 머리 위에 있을까? 응?”

까드득. 까득!

“어차피 시간 문제라고. 내가, 내가 놈을 죽이기로 마음먹은 이상. 충분히 그럴 만한 방법을 찾…… 빌어먹을. 알겠나?”

까드드득!

스산한 목소리와 마찰음이 섞여 들었다. 석고준은 붉어지다 못해 핏빛에 가까워진 눈동자로 고세원을 노려보았다.

감히 씻을 수 없는 죄를 저지른 수하를 향해 상체를 기울이자, 낡은 목걸이가 흘러나와 고세원의 눈앞에서 핑글핑글 돌았다.

“고 팀장, 고세원. 이 은혜도 모르는 버러지 새끼야.”

“…….”

“길어 봐야 일 년이다. 진태경…… 네가 그토록 두려워하는 그놈은 결국 내 손에 죽어. 쓰촨이든, 서울이든 상관없어. 누구도 눈치챌 수 없게, 스승님 때와 같은 방식으로 놈을 죽일 거다.”

“…….”

“그때까지 이 세상은 내 편이야. 내가 먼저 이 성을 나서기 전까지, 누구도 나를 건드릴 수 없다고. 이 멍청한 새끼야.”

복수를 생각하는 환희와 한 사람을 향한 광기가 섞여든다. 그 혼탁하기 짝이 없는 눈빛을 말없이 바라보던 고세원은 문득 입을 열었다.

“일 년. 길군요.”

“뭐?”

“부길드장님께서 어떤 방법을 찾으셨는지는 몰라도…… 진태경은, 그는 그때까지 기다려 주지 않을 겁니다.”

“그럼. 당장 놈이 쳐들어오기라도 할 것 같나?”

“예.”

짤막한 대답에 석고준은 소리 내어 웃었다. 얼굴이 일그러지고 집무실이 떠나가도록 웃다가, 돌연 착 가라앉은 표정으로 입술을 뗐다.

“병신 같은 새끼. 여긴 아레스 길드다. 앞으로 넘어지면 청와대고, 뒤로 자빠지면 국회의사당이야. 온 세상을 적으로 돌리는 미친 짓을, 그놈이 할 것 같나?”

“제가 아는 누군가는 인위적으로 몬스터 웨이브를 일으켰다더군요. 그보다 덜한 미친 짓을, 진태경이라고 못 하겠습니까.”

“……!”

“그리고, 부길드장님.”

고세원은 자신도 모르게 실소를 흘렸다. 진태경의 일거수일투족을 감시하고, 과거를 조사하며 알게 된 사실이 떠올라서였다.

“진태경은 미친놈입니다. 모르셨습니까?”

“이 개……!”

석고준의 눈동자가 부릅떠진 그 순간.

구구구구구궁!

아레스 길드 본사. 100층이 넘는 초고층 빌딩이 몸을 떨었다.

잦아드는 굉음 너머로 들려오는 고세원의 목소리가 석고준의 귓가를 파고들었다.

“아마도 저 미친놈을 상대하는 게 제 마지막 임무가 되겠군요. 그동안 감사했습니다, 부길드장님. 살아남는다면 정식으로 사표를 제출하겠습니다.”

지금까지의 감사와 인간으로서의 혐오를 담아 깊숙이 허리를 숙인 고세원이 굳게 닫혀 있던 문을 열어젖혔다.

비상을 알리는 사이렌 소리가 아레스 길드를 깨우고 있었다.
```

## Final English reading copy

```markdown
# Chapter 587

The air. Time.

Everything seemed to have stopped.

That was how it felt to the master of Area A, hidden in the strictest secrecy within Ares Guild in Jongno, Seoul.

*How?*

Only that question circled through his mind.

Seok Go Jun had forgotten that Go Se-won was standing beside him. With a rigid expression, he stared at the holographic television mounted on the wall.

Footage transmitted from dozens of unmanned reconnaissance drones deployed by the government and various media outlets was streaming live.

“Right now, you’re looking at Mount Balwang, near Pyeongchang in Gangwon Province, where the Monster Wave occurred. And…”

The voice of the anchor of the public broadcaster’s nine o’clock news flowed through the room. Unlike his usual calm, serious delivery, the unseen anchor sounded highly agitated.

“Can you see this, everyone? This is the corpse of the Named Monster Behemoth! Around it, survivors of the disaster are being transported by emergency helicopters…”

Go Jun’s eyelids trembled.

The brutally dismembered corpse of the monster. The survivors. The voices of the Peace Guild members and the anchor explaining the situation.

All of it stoked his fury.

Bang!

With a thunderous explosion, the latest-model holographic television—replaced more than ten times over the past month—burst apart and scattered into dust.

Go Jun did not care.

The instant Choi Minwoo appeared on the screen, being transported with a respirator over his face, everything else became meaningless.

*He survived. Choi Minwoo survived.*

That fact weighed heavily on his heart.

To Go Jun, Choi Minwoo was a bastard who deserved to die. A bastard who had to die.

That was why he had laid the trap.

He had lured Jin Taekyung to Busan and used Song Cheonwoo to make his enemies destroy one another, ensuring that both sides would be crippled.

But…

*What went wrong?*

A red light flickered in Go Jun’s eyes. In his hand, two unpurified S-grade Magic Gems were grinding constantly against each other.

Crk. Crk.

What had he missed?

Crk. Crk.

He had thought the plan was perfect.

No—perhaps it really had been perfect.

If there had been one flaw in that perfect plan, it was the fact that something beyond perfection had stood on the other side.

*Jin Taekyung.*

It had to be him. The Behemoth’s mana barrier had blocked every media outlet from learning the details of the situation, but there was no doubt.

That bastard who had killed Lee Jungryong—his Master, a man who had seemed like a living god—and carved an indelible terror into Go Jun’s mind had interfered yet again.

Even after he had laid a trap that should have been impossible to avoid. Even then, once again!

Crkkkk!

Instead of a roar filled with resentment, a chilling grinding sound filled the office.

Suppressing the fury surging inside him, Go Jun barely managed to force out his voice.

“Song Cheonwoo… What about Song Cheonwoo?”

When no answer came, a thunderous shout erupted.

“I asked what happened to him!”

“……”

“Team Leader Go! Go Se-won!”

Go Se-won, the Head of Security, had been silently watching his superior vent his rage. He answered in a dry voice.

“He isn’t on any of the survivor or casualty lists we obtained.”

“What about the Gate access records?”

“Nothing there either. We believe the Peace Guild, which effectively owns that Gate, deliberately left no traces behind.”

“Of course. That makes sense. Even if Choi Minwoo is a little bastard, he’s extremely careful. Isn’t he?”

“……Yes.”

A secret that never crossed the walls was both the advantage and the disadvantage of complete secrecy.

Go Jun roughly ran a hand through his hair. Then he lifted the whiskey in front of him and drank straight from the bottle before muttering.

“Fine. Even if things went to hell, there’s nothing they can do about it. Song Cheonwoo can either prove his alibi with the double we prepared in advance, or, if that becomes difficult, we can make it look like he acted alone. There were no traces left in Busan, so we don’t need to worry about that. Right?”

“But, Vice Guild Master, the Pyeongchang incident is too serious to be handled as Song Cheonwoo’s lone crime. According to the information we obtained, Kim Hwajong—the nominal Guild Master of the Peace Guild—died, and Song Cheonwoo is unquestionably a member of Ares…”

“Listen, Team Leader Go.”

At that moment, Go Se-won felt a chill seize his entire body. His frozen figure was reflected clearly in Go Jun’s red eyes.

“Then make the serious matter smaller.”

“V-Vice Guild Master.”

“Whether it costs tens of billions or hundreds of billions, I don’t care. Scatter money through the prosecutors’ office. Threaten the old men sitting in the National Assembly. Grab the collars of anyone carrying a camera or microphone. Isn’t that your job?”

“……!”

Go Se-won’s eyes trembled violently. The malice radiating from one man, along with his horrifying aura, pressed down on him.

*How can someone become like this…?*

It was more than astonishing. It was horrifying.

Could a person really change this much in only a few months? Could someone really fall this far?

And what, exactly, was the overwhelming power bearing down on him now?

As Go Se-won stared at Go Jun in stunned disbelief, Song Cheonwoo’s voice from several days earlier suddenly echoed through his mind.

*The boundary between humans and monsters. That bastard Go Jun… has already become a monster.*

It was true.

Go Jun—his superior—had already become a monster.

He had used the loyalty of his subordinates, bordering on religious devotion, to send them to their deaths. He had artificially caused two Monster Waves that could result in thousands, tens of thousands, perhaps even hundreds of thousands of casualties.

All for the single purpose of eliminating his enemies.

*A monster that has forgotten even the minimum duty a human being should possess.*

As Go Se-won struggled desperately to hide his agitation, Go Jun opened his mouth again.

“Deal with it properly. Choi Minwoo survived, but at least Song Cheonwoo has been taken care of. If we get through this one time, there shouldn’t be a problem.”

Go Jun had regained his composure, and his voice was cold.

He had failed to bring down the external enemy, but he had eliminated the internal one. That was as good as achieving half a victory.

Once the fake Song Cheonwoo he had installed went through the retirement process and disappeared, everything would be over.

No rumor or condemnation would be enough to bring down Ares Guild.

“It’s been thirty years. Thirty whole years. Politics, business, the prosecutors’ office, the media… They all grew beneath Ares’s shadow.”

Crk. Crk.

Cheon Taemin had built the foundation, but after Taemin lost consciousness, it was Lee Jungryong who had built the pillars and roof.

The young politicians Ares had supported long ago had become prime ministers, ruling-party leaders, and opposition heavyweights. The corporate world, the prosecutors’ office, and the media were no different.

Some portion of the astronomical sums Ares Guild earned from Gates—the diamond mines of this world—had been scattered everywhere as dirty money. Those seeds had grown into a dense forest surrounding an impregnable fortress.

Go Jun was one of the people who knew that fact better than anyone.

Among the things he had inherited from his Master was a ledger filled with every kind of corruption and weakness.

“Even if everyone points fingers at us, this world itself is what protects us.”

He had forgotten that in his impatience and fury.

He had forgotten just how much power he possessed.

And just as Go Jun’s confidence fully returned and a deep smile spread across his lips—

“You’re wrong.”

“What?”

Go Se-won looked straight at the monster before him—his superior—with an indescribable expression.

“The old politicians raised in Ares’s name, the Prosecutor General, the corporate dynasties and media conglomerates whose roots stretch back to the Japanese occupation—they won’t protect you, Vice Guild Master.”

“Team Leader Go. What are you saying right now…”

“Some of what you said is true. Ares’s name will not collapse over something as simple as pointing fingers and condemnation. But even if the entire world protects you, there is one person it cannot stop.”

“……!”

Go Jun’s body abruptly froze.

The thought of grabbing the Head of Security by the collar for daring to spout nonsense in his face had already flown far away.

It was because of the name of the one person who had struck him in the mind.

*Jin Taekyung.*

Reading the thought in his trembling superior’s eyes, Go Se-won continued in a low voice.

“Have you forgotten? Whose hands brought down the person who personally cultivated the world you now trust?”

“……!”

The shock struck Go Jun like a blow to the back of the head. He clenched his teeth without realizing it.

Unfortunately, the words being spoken by the bastard in front of him were not nonsense. They were all facts.

*Master.*

It was true. Lee Jungryong—Ares’s master and a man who had been no different from the king of Korea—had ultimately been killed by Jin Taekyung’s hand.

The entire world had belonged to Lee Jungryong, yet no one had been able to protect him.

A boiling voice seeped through Go Jun’s clenched teeth.

“Team Leader Go… You little bastard.”

“I only said what someone had to say.”

“Shut up.”

“If that is your order, Vice Guild Master, I will obey. But please don’t dismiss my words without hearing them.”

“I said shut your mouth.”

Rumble!

A massive aura burst from Go Jun’s entire body like an explosion. The office shook as though an earthquake had struck.

Go Se-won’s face turned pale before that truly overwhelming power, but compared to the disgust he felt now, the fear was nothing.

*Monster.*

Go Jun read the emotion passing through Go Se-won’s eyes and bared his teeth.

“Team Leader Go, have you suddenly gone mad? Have you lost your mind?”

“……”

“I only put you in the position of team leader because your abilities were at least useful. Did wearing a title that was never meant for you suddenly make the world look different?”

Go Jun let out a laughter filled with fury before continuing.

“Team Leader Go, you’re a coward and a piece of trash. You wrapped it in pretty words and called it loyal counsel, but you’re more afraid of Jin Taekyung than you are of my Master and me.”

“……That isn’t true.”

“It’s too late to deny it. Let’s at least admit what we both know. Yes, that bastard Jin Taekyung is strong. That’s a fact. But how long can he stay above my head? Hmm?”

Crk. Crk!

“It’s only a matter of time. Now that I—now that I’ve decided to kill that bastard—I’ll find a way worthy of it… Damn it. Do you understand?”

Crkkkk!

His chilling voice mingled with the grinding sound. Go Jun glared at Go Se-won with eyes that had reddened until they were nearly blood-colored.

He leaned his upper body forward toward the subordinate who had dared to commit an unforgivable crime. An old necklace slipped out and spun slowly in front of Go Se-won’s eyes.

“Team Leader Go. Go Se-won. You ungrateful piece of trash.”

“……”

“A year at most. Jin Taekyung… That bastard you’re so afraid of will die by my hand. I don’t care whether it’s Sichuan or Seoul. I’ll kill him without anyone realizing what happened—the same way Master was killed.”

“……”

“Until then, this world is on my side. Until I leave this fortress myself, no one can touch me. You stupid bastard.”

The joy of revenge and the madness directed at one person had become intertwined. Go Se-won silently watched those impossibly murky eyes before suddenly opening his mouth.

“One year. That’s a long time.”

“What?”

“I don’t know what method you found, Vice Guild Master, but… Jin Taekyung won’t wait that long.”

“What, do you think he’s going to come charging in right now?”

“Yes.”

At the short answer, Go Jun laughed aloud. He laughed until his face twisted and the office seemed ready to fall apart from the sound. Then, suddenly, his expression sank, and he parted his lips.

“You pathetic idiot. This is Ares Guild. If we fall forward, we hit the Blue House; if we fall backward, we hit the National Assembly. Do you really think he’ll do something insane enough to make the entire world his enemy?”

“I hear someone I know artificially caused a Monster Wave. Do you really think Jin Taekyung is incapable of doing something less insane than that?”

“……!”

“And, Vice Guild Master.”

Go Se-won let out a bitter laugh without realizing it. He had remembered what he learned while monitoring Jin Taekyung’s every move and investigating his past.

“Jin Taekyung is a lunatic. Didn’t you know?”

“You bas—!”

At that moment, Go Jun’s eyes widened.

Rumble-rumble-rumble!

Ares Guild headquarters shook. The skyscraper of more than one hundred floors trembled from top to bottom.

Beyond the thunderous roar as it began to subside, Go Se-won’s voice pierced Go Jun’s ears.

“Dealing with that lunatic will probably be my final mission. Thank you for everything, Vice Guild Master. If I survive, I’ll submit my formal resignation.”

Carrying both his gratitude for everything until now and his disgust toward Go Jun as a human being, Go Se-won bowed deeply.

Then he flung open the tightly closed door.

Sirens announcing an emergency were waking Ares Guild.
```

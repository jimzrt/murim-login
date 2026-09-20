<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0590.txt",
      "sha256": "b99e609dabd2e5c7333d0b15947a69601b864b7e61a8096bba467f5f7788f428",
      "bytes": 14371
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "5a285484949aae1561c9d6b203b5528354f42b3ff854ee24aa4006a5824fb36e",
      "bytes": 2914
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "60528794283cf5bbb39f243344e2c2737402e0bfba64ad7912657f1c5a331ccd",
      "bytes": 184299
    },
    {
      "path": "characters/Cheonwoo.md",
      "sha256": "d364d5f11cf59a62f56ca6cd62bbeb37a3709a28dabcf10a65b57e6bf88b7844",
      "bytes": 590
    },
    {
      "path": "characters/Go Jun.md",
      "sha256": "d72e8a6a2e138fdeda05d737387a67e81fb7d6b8faa5e3a38544a1a17ad25d2a",
      "bytes": 1030
    },
    {
      "path": "characters/Hwa-jong.md",
      "sha256": "e2f4b26655747096e227d3e089bad64cc36be97f270ea753711cda8d9a3fb85a",
      "bytes": 646
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "7f097e5188ce66b207f96dc6c99019bfaeb08971c4ea8e0f0c98dc669b82f710",
      "bytes": 2315
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "e342318fc6aa469472c3661a77596e17e799c2aa552dc914bb91fdea1c0fd4e7",
      "bytes": 622
    },
    {
      "path": "characters/Kim Hwajong.md",
      "sha256": "dafef1a2f12116daf521e181a0ad963eab7f05ebc5155099ebab62943490c4a2",
      "bytes": 694
    },
    {
      "path": "characters/Lee Jungryong.md",
      "sha256": "fa994024ae0af2d238fb917473cae12473b307c2ac65e816d8205a54d27f93a7",
      "bytes": 1384
    },
    {
      "path": "characters/Song Cheonwoo.md",
      "sha256": "5a805ea4ae89d76429240c6510103cc5f8b514a07426b1a173f04fdb66f3050b",
      "bytes": 1080
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "871361570d10187aa81457f4204c1745bc734eca545eda422e62ed2a4d25ab2c",
      "bytes": 181458
    }
  ],
  "estimated_tokens": 12375
}
-->

# Durable State Update — Chapter 590

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 590. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 590. Profile updates may replace only one
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
  "chapter": 590,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 590,
    "continuity_sources": [590],
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
    "Jin identifies Go Jun as the culprit behind the Monster Wave and deaths and has entered Ares Guild headquarters to confront him; Skeleton King remains to protect the Peace Guild and its people.",
    "Go Jun intends to kill Jin Taekyung within one year and relies on Ares's political, prosecutorial, corporate, and media influence plus Lee Jungryong's corruption ledger for protection.",
    "Go Se-won openly opposes Go Jun's crimes and cover-up orders and intends to resign if he survives.",
    "Cheon Taemin collapsed more than twenty years ago and remains unconscious at an unknown location, with Area A only suspected.",
    "Song Cheonwoo and Lee Jungryong concealed Taemin's condition and purged those who knew the truth.",
    "Busan's Kraken is dead, but more than one thousand Mermen remain across Haeundae and Gwangalli.",
    "Go Jun seized Song Cheonwoo's children, used an S-grade Magic Gem to cause the Busan Monster Wave, and targeted Choi Minwoo.",
    "Song Cheonwoo was killed by an unidentified monster after falling into an abyss; the object in his pocket released darkness that became light.",
    "Jin has incapacitated roughly two hundred elite Ares Hunters in the Guild lobby while deliberately restraining lethal force."
  ],
  "continuity_sources": [
    589
  ],
  "open_questions": [
    "What caused Cheon Taemin's collapse, and what happened during his more than twenty years of unconsciousness?",
    "Is Cheon Taemin actually being kept in Area A of Ares Guild headquarters?",
    "What is the unidentified being involved in Go Jun's plan, and is it connected to the monster that killed Song Cheonwoo?",
    "What was the object Song Cheonwoo kept in his pocket, and what did its release of darkness and light accomplish?",
    "What is the old necklace Go Jun wears, and why does it matter to his plan?"
  ],
  "safe_through": 589,
  "temporary_decisions": [
    "Use Yeti's Winter Range for 예티의 겨울 산맥, Stone King for 스톤 킹, Behemoth for 베히모스, and Behemos for 베헤모스.",
    "Use Area A for A구역 and Mount Balwang for 발왕산.",
    "Use Hero's Soul for 영웅의 혼, Hyung for 형님, S-grade Magic Gem for S급 마정석, Hell Fire for 헬 파이어, and Hellfire Mage for 겁화의 마법사.",
    "Use final rally for 회광반조, Young Master for 도련님, Rodin's The Thinker for 로댕의 생각 난 사람, and Teleport for 텔레포트.",
    "Use Code Red for 코드 레드, Multi Shot for 멀티 샷, Binding for 바인딩, Tower Shield for 타워 실드, and great tiger for 대호."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 김화종    | **Kim Hwajong**   |
| 이정룡    | **Lee Jungryong** |
| 절정     | **Peak**          |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 제자     | **Disciple**                                 |
| 선배     | **Senior**                                   |
| 몬스터     | **monster**           |
| 길드      | **Guild**             |
| 팀장      | **Team Leader**       |
| 힐러      | **healer**            |
| 천우 | **Cheonwoo** | Name shown in a Level Window; one of the five current Five Gates scions. |
| 고준 | **Go Jun** | Personal name of Team Leader Seok; Lee Jungryong's prized Disciple. |
| 화종 | **Hwa-jong** | Butler Kim's personal name. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 송천우 | **Song Cheonwoo** | Ares Guild Director, former third-ranked Korean Hunter, and longtime European regional branch director. |
| 화염신장 | **Flame Divine Palm** | Jopil's deadly palm technique, noted when Taekyung compares Jopil with Mukyung. |
| 아레스 | **Ares Guild** | The leading Guild in Korea; formerly employed Team Leader Choi and Song Song. |
| 사장님 | **Boss** | Address for the restaurant owner; contextually rendered as ma'am in one reply |
| 화시 | **fire arrow** | Flaming arrow Lee Seowol fires to signal Cheol Mubaek. |
| 송이 | **Song-i** | Short form used for Song Song; Taekyung's love interest. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 멸염신권 | **Flame-Extinguishing Divine Fist** | Named fist technique Taekyung announces at the chapter's end. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 준이 | **Jun** | Family nickname used in the form Jun's dad. |
| 석고준 | **Go Jun** | Source full-name form for the established Go Jun, also known as Team Leader Seok. |
| 영국 | **United Kingdom** | Country associated with BCC. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 부산 | **Busan** | City where the Haeundae Gate crisis occurs. |
| 평창 | **Pyeongchang** | Location in Gangwon Province where the Gate is situated. |
| 정룡 | **Jungryong** | Cheon Taemin's trusted associate who joined the Peace Guild. |

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
| 진태경 | 석고준 | returning Hunter to hostile Ares security leader | you fucking bastard | hostile and profane | Taekyung directs his final insults and challenge at Go Jun after returning alive. |
| 석고준 | 진태경 | hostile_opponents | brat | hostile and overconfident | Go Jun addresses Taekyung internally as 애송아 while launching his full-strength attack. |
| 중년인 | 진태경 | veteran civilian Hunter to celebrated allied Hunter | Mr. Jin | formal-polite and awed | The casualty clerk addresses Jin as 진 선생님 after Jin asks him to list Lei Fei among the dead. |
| 진태경 | 중년인 | celebrated Hunter to older fellow Hunter | sir | casual and teasing | Jin addresses the older Hunter as 아저씨 while joking with him and giving him instructions. |
| 고준 | 진태경 | Ares Guild combatant confronting the killer of his Master | you | hostile and informal | Go Jun uses 너 while demanding Jin confess to Lee Jungryong's death and threatening retaliation. |
| 진태경 | 고준 | dominant adversary confronting Lee Jungryong's Disciple | you | contemptuous and informal | Jin uses 너 and 놈 while overpowering Go Jun and ordering him to end the conflict with Lee Jungryong. |
| 힐러 | 진태경 | healer addressing the rescuer who stabilized the survivor | sir | deferential and grateful | The healer thanks Jin as 선생님 after witnessing his rescue and treatment. |
| 송천우 | 석고준 | adversary; captor of Song's children | you | shocked and confrontational | Song reacts directly to Go Jun's admission that he took the children. |
| 송천우 | 화종 | former_allies | Hwa-jong | familiar and informal | Song uses Hwa-jong's personal name, prompting Hwa-jong to reject the familiarity. |
| 화종 | 송천우 | former_allies_now_hostile | you | formal and cold | Hwa-jong challenges Song's right to expect Choi's trust and rejects their former intimacy. |
| 팀장 | 중년인 | Hunter_team_leader_to_stranger | Boss | casual and polite | The Team Leader mistakes disguised Song for an ordinary raid customer and warns him not to proceed. |
| 길드원 | 진태경 | Peace Guild member to allied S-rank Hunter | Hunter Jin Taekyung | formal-polite and hesitant | A Guild member addresses Taekyung as 진태경 헌터님 while asking whether Choi should be awakened. |

## Listed compact profiles

### Cheonwoo.md

# Cheonwoo (천우)

- **Safe through:** Chapter 587
- **Aliases:** None
- **Role:** One of the five current Five Gates of Shanxi scions and a First Rate martial artist present at Honghwa Inn.
- **Personality:** Pampered and contemptuous toward Cheongpung's group as part of the five scions' collective mockery.
- **Voice:** Mocking in the group's exchange; no distinct individual speech is established.
- **Relationships:** Associates with Seongryong, Myeonghwa, Sohye, and Jintae as a group of current Five Gates scions.

### Go Jun.md

# Go Jun (고준)

- **Safe through:** Chapter 589
- **Aliases:** Team Leader Seok
- **Role:** Go Jun is Ares Guild's Vice Guild Master, Lee Jungryong's disciple and former Head of Security, and the de facto successor to Lee's Ares legacy who passed the S-rank Hunter qualification assessment with a very high score but lacks Lee's legitimacy.
- **Personality:** Disciplined and controlled under ordinary pressure, fiercely loyal to Lee Jungryong, but consumed by humiliation and rage when Ares Guild's authority is challenged.
- **Voice:** Dry, controlled, and formal with subordinates; deferential when addressing his Master.
- **Relationships:** Disciple and direct protégé of Lee Jungryong, Go Jun inherited Lee's Ares Guild legacy after his death, regards Jin Taekyung and Choi Minwoo as enemies seeking to take it away, has seized Song Cheonwoo's children as leverage, and used an S-grade Magic Gem to trigger the Busan Monster Wave while targeting Choi.

### Hwa-jong.md

# Hwa-jong (화종)

- **Safe through:** Chapter 588
- **Aliases:** Butler Kim
- **Role:** Hwa-jong was Choi Minwoo's loyal butler and personal escort who sacrificed his life to restrain Behemoth and died after Jin Taekyung killed it.
- **Personality:** Loyal, vigilant, and uncompromising toward perceived threats to Choi Minwoo.
- **Voice:** Formal and deferential toward Choi Minwoo, cold and openly hostile toward Song Cheonwoo.
- **Relationships:** Hwa-jong serves Choi Minwoo and was formerly close to Song Cheonwoo, but their relationship ended over loyalty and ambition.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 588
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, a Supreme Peak master who possesses the Heavenly Martial Physique and superhuman physical strength, has manifested Force, opened his Middle Dantian, crossed the wall into true mastery, has achieved Three Flowers Gather at the Crown but not Five Qi Returning to Origin, can perceive the texture of qi well enough to sever layered magic, can resist high-level monster Fear through exceptional mental strength, is publicly recognized as an S-rank-level Hunter while formally retaining an A-rank license pending testing, can command coordinated raids against powerful monsters, serves as one of the two pavilion masters of the Alliance Leader's direct Fire Dragon Pavilion, leads its first mission to Nanman, has withdrawn from the Peace Guild, and has entered Ares Guild headquarters to confront Go Jun.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor and assigned him a final task to incorporate martial principles into his learned martial arts but declined Taekyung's recruitment after Cheongpung reached him first, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate, student, and trusted manager of media and official arrangements, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, and Xiao Shen regards him as an older brother after Jin saved him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 588
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Kim Hwajong.md

# Kim Hwajong (김화종)

- **Safe through:** Chapter 588
- **Aliases:** Butler Kim
- **Role:** Kim Hwajong was a Level 80 mage known as Butler Kim and Choi Minwoo's loyal butler and personal escort who sacrificed his life to restrain Behemoth and died after Jin Taekyung killed it.
- **Personality:** Gentle and composed as Butler Kim, but retains a fiery temperament and a habit of swearing.
- **Voice:** Gentle and measured
- **Relationships:** Kim Hwajong formerly instructed Im Chunsoo, who remains terrified of and obedient to him, and serves Choi Minwoo as butler and personal escort, having become Choi's only family.

### Lee Jungryong.md

# Lee Jungryong (이정룡)

- **Safe through:** Chapter 587
- **Aliases:** None
- **Role:** Former Vice Guild Master of Ares Guild, one of Korea's two S-rank Hunters, and a Supreme Peak-level martial artist who was killed by Jin Taekyung.
- **Personality:** Outwardly genial, calm, and humorous; calculating, opportunistic, manipulative, coercive, and ruthless when challenged
- **Voice:** Smooth, good-natured, and indirect, using teasing conversation and veiled threats before becoming openly furious
- **Relationships:** Master of Park Jihoon and Go Jun (Team Leader Seok), whom he personally selected and trained; longtime Great Cataclysm acquaintance of Park Tae Seop; adversary of Jin Taekyung; knew Team Leader Choi from childhood; has an antagonistic history with Kim Hwajong, who saved his life at the collapse of Mapo Bridge eighteen years earlier; was visibly shaken by learning that Choi is Cheon Taemin's maternal grandson; regarded Cheon Taemin as an older brother despite no blood relation and long held him in respect and fear; secretly supported the orphanage where Lee Dongseok grew up and was regarded by Dongseok as a father; operated as Ares Guild's senior authority beneath its Guild Master; concealed Taemin's condition with Song Cheonwoo and participated in purging aides who knew the truth.

### Song Cheonwoo.md

# Song Cheonwoo (송천우)

- **Safe through:** Chapter 587
- **Aliases:** Director Song
- **Role:** Ares Guild Director and former A-rank Hunter who reached third place among Korean rankers, briefly headed the Hunter training center, and led Ares Guild's European regional branch for twenty years; after being forced to attack Choi Minwoo to protect his hostage family, he fell into an abyss and was killed by an unidentified monster.
- **Personality:** Highly ambitious, honor-obsessed, politically calculating, and determined to use his final opportunity to reclaim influence before retirement.
- **Voice:** Not established.
- **Relationships:** Song Cheonwoo followed Cheon Taemin since before Team Leader Choi was born, was Lee Jungryong's former friend and rival, helped conceal Taemin's condition and purge aides who knew the truth, negotiated the European regional director position to save himself and his family, and had his children seized by Go Jun as leverage that forced him to attack Choi Minwoo.

## Korean source

```text
＃590화



모든 것은 한순간에 시작되고, 끝났다.

화륵.

멸염신권(滅炎神拳). 그 이름에 걸맞은 강대한 열기가 청백색의 불꽃으로 화하여 솟구치고.

꽈아아앙!

다음 순간 터져 나온 거대한 굉음이 모든 소음을 집어삼켰다.

겹겹이 설치된 강력한 방어 마법도, 단단하기 그지없는 마법 재료로 만들어진 천장도 초고온의 열기에 무너지고 녹아내렸다.

쾅! 쾅! 콰앙!

하나, 셋, 다섯. 열.

천장이 사라지면 다음 천장이 나타나고, 또 다른 천장이 눈앞을 가로막는다.

그러나 불의 기둥이 되어 솟구친 나는 가로막는 모든 것을 부수고, 뚫고, 녹여 내며 나아갔다.

쿵, 쩌저적.

얼마나 높이 솟구친 걸까. 얼마나 많은 천장을 부수었을까.

마침내 내 신형이 멈추었을 때, 일렁이는 불길 너머에는…….

“쳐!”

만반의 준비를 끝마친 사람, 아니 적들이 있었다.

쐐애애애액!

이 순간만을 기다리고 있었다는 듯, 적들은 화살과 마법 따위를 일시에 쏘아 보냈다.

그리고 수많은 개의 빛줄기가 나를 향해 쏘아진 그 순간, 나는 누구에게도 들리지 않을 명령어를 마음속으로 뇌까렸다.

‘인벤토리. 수납.’

쉭.

서늘한 창대의 감촉이 손아귀에서 사라진다. 나는 아직 가라앉지 않은 불길을 양손에 끌어모아 쌍장(雙掌)을 내질렀다.

‘화염신장(火焰神掌).’

화륵. 콰아아아!

팔 성에 이른 화염신장. 양 손바닥을 타고 뛰쳐나온 화룡이 용틀임한다.

끔찍한 열기가 양옆으로 펼쳐진 넓은 복도를 휩쓸었다. 마법, 화살, 그리고 사람까지.

“크아아아아악!”

“힐러, 힐러어!”

불길이 사그라진 자리에 남은 것은 비명과 악취다. 살 익는 냄새와 고통에 찬 외침이 곳곳에서 흘러넘쳤다.

만약 내가 전력을 다했다면, 이중 태반은 비명도 지르지 못하고 타 죽었을 것이다.

“이, 이게 어떻게……!”

나는 목소리가 들려온 방향을 따라 고개를 돌렸다.

복도의 끝에서 십여 명의 힐러가 입을 딱 벌린 채 자신들의 눈 앞에 펼쳐진 광경을 바라보고 있었다.

“뭐 합니까. 존나게 뛰어와서 동료들 안 살리고.”

덤덤하게 말을 건네는 내 모습에, 팀장급으로 보이는 중년 여성이 입술을 깨물었다.

“진태경 씨, 도대체 당신이 왜?”

“반드시 해야 할 일이 있으니까. 그리고 당신들이 그런 날 가로막았으니까.”

“무슨 사정이 있는진 모르겠지만, 그래도 이건…… 이건 너무하지 않나요?”

두려움과 분노가 뒤섞인 눈동자와 마주치자 천하에 다시 없을 나쁜 놈이 된 기분이다. 그래서인지는 몰라도 헛웃음이 나왔다.

그들의 옷에 박혀 있는 아레스 길드의 엠블럼이 거슬렸고, 그 뻔뻔한 행태가 기가 막혔다.

굳이 떠나려던 발걸음을 멈춘 이유는 바로 그 때문이었다.

“너무하긴 씨발. 당신들이 너무하지.”

“뭐, 뭐?”

“코드 레드. 그 네 글자에 나 죽이겠다고 우르르 몰려온 인간들이 할 소린 아닌 것 같은데.”

“……!”

“한 사람만 만나면 충분하다고 했다. 구태여 애꿎은 싸움을 피하려고도 했다. 하지만 먼저 선공을 펼친 건 당신들이고, 쓰러진 것도 당신들이야.”

이해한다. 저들이 김화종의 죽음과 직접적인 연관이 없다는 것 정도는. 머리가 꾸민 일을 손과 발이 어찌 알겠나.

하지만 단지 명령이 떨어졌다고 해서, 사람이 사람을 죽이라는 명령에 집결한 그들의 행동이 없는 일이 되는 것은 아니다.

“도대체 당신이 왜. 무슨 사정이 있는지는 모르겠지만…….”

내리깔린 신음 위, 입술 사이로 흘러나온 나직한 목소리가 검게 그을린 복도를 울렸다.

“개소리 좀 하지 마. 묻기 전에 생각했어야지. 왜 진태경 저 새끼가 갑자기 저러는 걸까. 사람도 많이 살리고, 몬스터도 많이 잡는다고 주위에서 칭찬이 자자한 새끼가 왜 우리 길드에서 석고준 데려오라고 난동을 피운 걸까. 그리고 왜 저놈을 죽이라는 명령이 떨어졌을까.”

요즘 세상이 그러더라. 나보고 영웅이라고.

결론부터 말하자면 아니다. 나는 숭고한 희생정신도 부족하고, 돈도 밝히고, 일면식도 없는 타인보다는 내 사람을 위해 살고 싶다.

하지만…… 한편으로는 부끄럽지 않게 살아왔다고 생각했다.

내 분수에 넘치는 이 힘을 얻게 된 후에는 되도록 다른 사람을 위해 사용했다고 믿었다.

스스로가 어떤 사람인지. 이 선택이 맞는지 늘 의심하고 또 의심했다.

“그런데 왜. 왜. 왜.”

나는 계속해서 공허한 물음을 던졌다. 시야에 담긴 얼빠진 얼굴들이 혐오스러웠고, 역겨웠다.

“사람에게 사람을 죽이라는데, 왜 당신들은 명령에 대한 의심도 없이 여기에 와 있지?”

아무도 대답하지 않았지만, 답은 나 스스로도 이미 알고 있다.

저들이 석고준의 손발조차 되지 못하는 손톱들이라서다. 석고준이, 아레스가 주는 먹이를 받아먹고 사는 개들이라서 그런 거다.

임무를 수행하면 더 많은 부와 명예를 얻을 수 있으니까. 그렇기에 지금까지 그래 왔던 것처럼 나를 막아선 거다.

“석고준 그 새끼가 무슨 짓을 벌였는지 짐작은 하고 있나? 만약 부산과 평창에서 일어난 몬스터 웨이브가 그놈이 인위적으로 발생시킨 거라면?”

말이 끝나기가 무섭게 곳곳에서 외침이 터져 나왔다.

“개소리!”

“말도 안 돼!”

그래. 이럴 줄 알았지. 그래서 여기까지 오게 된 거고.

나는 불신에 찬 그들의 표정을 보며 너털웃음을 터트렸다.

참 재미있다. 영웅이라 불리는 한 사람이 아레스 길드에 쳐들어온 이유에 대해서는 침묵하는데, 다른 일에 관해서는 부정부터 하고 본다는 것이.

“윗놈들이 날 쓰러트리는 대가로 뭘 약속했나? 길드 내에서의 초고속 승진? 몇 대가 먹고살아도 될 만큼의 재산?”

“……!”

“부탁인데 애들 키울 양육비가 부족해서, 홀어머니를 모시고 살아서, 뭐 그런 개 같은 소리는 하지 마. 당신들은 지금도 그렇게 배고픈 처지가 아니잖아.”

이 자리의 모두는 성공한 인생이다. 원했든, 원치 않았든. 어느 날 갑작스럽게 각성했고 아레스 길드에 들어올 만큼 뛰어난 기량을 선보였다.

그렇게 얻은 부와 명예를 탓할 생각은 없다. 한때 나 역시 꿈꿨던 모습이니까.

다만 오늘 그들의 선택이 역겹게 느껴지는 이유는…… 더 많은 것을 얻기 위해 잘못된 선택을 하고서도 스스로를 정당화시키는 모습 때문이었다.

개개인이 침묵하던 집단 전체가 침묵하는 법. 그들은 그렇게 아레스라는 철옹성의 수비군이 되었다.

“그러니까.”

나는 깊이 심호흡했다. 정신적인 피로과 분노, 혐오를 비롯한 여러 감정이 뒤섞여 가슴이 울렁거렸다.

“말도 안 되는 지랄염병 떨지 말고 자빠져 있어. 포션 쪽쪽 빨고 힐 받으면서 생각하라고. 오늘이 내 두 번째 생일이구나. 그렇게.”

“…….”

“…….”

사방이 고요했다. 주위에서 끊임없이 새어 나오던 신음도 이제는 더 이상 들리지 않았다.

서 있는 자들, 누워 있는 자들 모두가 눈을 감거나 굳게 입을 다물었다.

나는 떨리는 시선들을 무시하며 걸음을 옮겼다. 마지막 인사도 빼놓지 않았다.

“병신들.”

저들이 내 말을 듣고 뭔가를 깨달았는지, 혹은 변함없는 사냥개의 마인드인지는 관심 없다. 지금 내 목표는 오직 한 사람뿐이니까.

그리고 아직도 보이지 않는 그 씨벌 놈에게 닿기 위해서는…… 뚫고 나가야 장애물이 많이 남아 있었다.

사박.

내디딘 발걸음이 잘 정리된 잔디를 밟았다.

아직 세상은 쌀쌀하기 그지없는 겨울인데, 복도를 지나자 중심에 펼쳐져 있는 정원은 싱그러운 봄이었다.

몇 층인지 모를 이곳에는 흐드러지게 피어 있는 수백 송이의 꽃과, 그보다는 적은 숫자의 적들이 나를 기다리고 있었다.

“많이도 모였네. 씨벌 놈들.”

쉭!

인사에 대한 대답 대신 한껏 마나를 머금은 화살이 돌아왔다.

정확히 눈을 노린 것으로 보아 화살을 쏜 놈은 야박한 놈이었고, 화살에 실린 마나의 양을 생각하면 죽이려고 쏜 것이 확실했다.

그러니 이 경우에는 받은 만큼 돌려주는 것이 맞다. 적어도 내 방식은 그랬다.

턱, 쉬잉!

나는 화살을 손아귀로 붙잡음과 동시에 흩뿌렸다.

처음 쏘아진 것보다 두 배는 빠르고 강하게 주인에게 되돌아간 화살촉이 반짝인 그 순간.

카앙!

마찰음과 함께 새하얀 검신이 파르르 떨렸다.

엄청난 크기의 대검으로 화살을 튕겨낸 50대의 중년인이 깊게 가라앉은 눈빛으로 나를 응시했다.

몸에 밴 관록이며, 그 기세가 절정의 끝자락에 다다른 무림인을 연상케 하는 인물이었다.

“듣던 대로 성격이 급하군, 후배.”

“처음 뵙겠습니다, 선배님.”

나는 후배다운 공손한 태도로 손가락 마디를 꺾었다. 우둑. 핏물에 굳은 마디에서 뼈 어긋나는 소리가 들렸다.

“지금이라도 물러나시면 조용히 지나가겠습니다. 아, 조금 전에 화살 쏜 저 새끼는 예외고요.”

철썩!

내 말이 끝나기 무섭게 한 사람의 고개가 돌아간다.

번개 같은 속도로 오른쪽에 있던 궁수의 뺨을 후려갈긴 중년인이 나를 바라보았다.

“아직 젊고 멍청한 놈이야. 선처를 부탁하네.”

“실수가 아니었습니다. 손모가지는 부러트려야죠.”

“그 정도면 감지덕지겠지. 살아남는 게 중요한 거니까.”

뭐지, 이 양반?

지금까지 상대했던 아레스 소속 길드원들과는 뭔가 다르다. 문득 의구심 어린 시선으로 바라보는 내게, 중년인이 담담한 목소리로 말을 이었다.

“그리고 자네가 건넨 제안은 고맙긴 하네만, 아무래도 거절해야 할 것 같네. 이래 보여도 나름 길드 중역이라서. 자네 바짓가랑이라도 붙잡고 늘어져야 하거든.”

“그럼 좋은 꼴 못 보실 텐데.”

“어쩌겠나. 나도 결국 사냥개인데. 지금까지의 상황을 보면 결과는 뻔하겠지만 되도록 살살 부탁하지.”

뭘까. 저 태도는.

말없이 중년인을 물끄러미 바라보던 나는 문득 한 가지 짐작에 이르러 입을 열었다.

“송천우. 아니, 송 지사장 쪽 계파군요.”

내 말을 들은 중년인의 눈이 커졌다. 정답이라는 뜻이다.

더불어 내가 저들과 싸울 이유 역시 사라져 버렸다.

송천우는 아레스 길드 내부에서 자신만의 세력을 이끌고 석고준과 대립각을 세우던 인물이었으니, 눈앞의 중년인 역시 그와 뜻을 함께하던 인물이었을 것이다.

“알고…… 있었나?”

“가까운 사람에게 들었습니다. 굳이 싸울 필요 없으니 물러서십시오.”

중년인이 헛웃음을 흘렸다.

“적의 적은 아군이다?”

“적어도 지금은 힘도, 시간도 낭비하기 싫습니다.”

사박.

내가 다시 발걸음을 옮긴 순간. 중년인이 대검을 비스듬히 바로 세웠다.

명백하게 공격을 준비하는 자세. 그의 착잡한 목소리가 귓가에 닿았다.

“그만 멈추게. 나도 이러기 싫지만 어쩔 수 없어.”

나는 발걸음을 멈추지 않으며 대답했다.

“이러기 싫은데 왜 이 자리에 있습니까. 그냥 시키는 것밖에 할 수 없는 사냥개라서?”

“……!”

“석고준이 두려우면 두렵다고 하세요. 어쩔 수 없다는 말로 포장하지 말고.”

비단 중년인뿐만이 아니다. 나를 향하는 모두의 시선이 파르르 떨렸다.

아랑곳하지 않고 나아가는 내 발걸음만큼, 일백이 넘는 그들 역시 뒷걸음질 치고 있었다.

담담했던 중년인의 표정 위로 보이지 않는 금이 그어졌다.

“이미 대세는 기울었어. 오늘 아침 송 지사장님이 영국으로 돌아갔다더군. 그게 의미하는 바가 뭐겠나? 어떻게든 살길을 찾아야 했네. 사냥개 노릇을 해서라도.”

송천우가 오늘 아침에 영국으로 갔다니, 당연히 거짓이 틀림없다. 석고준이 내세운 대역임을 확신한 내가 피식 웃었다.

“그 사냥개 주인이 오늘 죽는다면?”

“……!”

모두의 눈이 부릅떠진다. 나는 허공을 향해 손을 뻗었다. 동시에 인벤토리에서 불러온 백염이 비스듬히 내리그어졌다.

쉬잉!

허공을 가로지르는 한 줄기 선.

모두가 헛숨을 삼켰지만 뿜어지는 핏물도, 죽음도 없었다.

새하얀 창날을 타고 쏘아진 강기가 베어 낸 것은 인간이 아닌 무언가였으니까.

서걱, 쿠웅!

정원의 중심에 놓인 화려한 분수대. 그 위를 밟고 우뚝 선 거대한 석상이 조각나며 허물어졌다.

이미 죽고 없는, 한 사람을 본 따 만들어진 석상의 잔해가 꽃들을 깔아뭉갠다.

몸통에서 분리된 머리가 구르고 굴러 내 발치에 닿았다.

나는 단순한 석상이라고 부를 수 없을 만큼 생동적인 석상의 얼굴을, 어렵지 않게 알아볼 수 있었다.

‘이정룡.’

그렇다.

오늘, 모든 것을 갖고자 했던 효웅(梟雄)이 세운 이 화려한 왕궁은 무너진다.

괴물이 되어 버린 제자와 함께.

나는 넋 나간 사람들을 향해 한마디를 툭 내뱉었다.

“둘 중 하나다. 무기를 내려놓고 길을 트던가, 그것도 아니라면 내 뒤를 지키든가.”

“……!”
```

## Final English reading copy

```markdown
# Chapter 590

Everything began and ended in an instant.

Fwoosh.

Flame-Extinguishing Divine Fist. True to its name, its overwhelming heat transformed into blue-white flames and surged upward.

Kuwaaaaaang!

The tremendous roar that erupted the next moment swallowed every other sound.

Layer after layer of powerful defensive Magic—and even the ceiling, made from exceptionally durable magical materials—collapsed and melted beneath the extreme heat.

Boom! Boom! KABOOM!

One, three, five. Ten.

Whenever one ceiling disappeared, another appeared, and then yet another ceiling blocked my path.

But I surged upward as a pillar of fire, smashing, piercing, and melting everything that stood in my way.

Boom. Crackle.

How high had I risen? How many ceilings had I destroyed?

At last, when my body came to a stop, beyond the wavering flames…

“Fire!”

There were people waiting for me—no, enemies who had finished making every possible preparation.

Screeeeech!

As if they had been waiting for this moment alone, the enemies fired arrows, Magic, and everything else at once.

And at the moment countless rays of light shot toward me, I muttered a command in my mind that no one could hear.

*Inventory. Store.*

Swish.

The cool sensation of the spear shaft disappeared from my grip. I gathered the flames that had not yet died down into both hands and thrust out my palms.

*Flame Divine Palm.*

Fwoosh. Whoooooosh!

Flame Divine Palm at eight-tenths mastery. A fire dragon burst from both palms and writhed through the air.

Terrible heat swept through the wide corridor stretching out on either side. Magic, arrows, and even people were caught in it.

“Graaaaaaaaaah!”

“Healer! Healeeer!”

What remained where the flames subsided was screaming and foul stench. The smell of flesh roasting and cries of agony overflowed from every direction.

If I had used my full strength, more than half of them would have burned to death without even managing to scream.

“H-How could this…?”

I turned my head toward the voice.

At the end of the corridor, a dozen or so healers stood with their mouths hanging open, staring at the scene before them.

“What are you doing? Run your asses over here and save your comrades.”

At my flat remark, a middle-aged woman who looked like a Team Leader bit her lip.

“Mr. Jin Taekyung, why on earth are you…?”

“Because there’s something I absolutely have to do. And because you people got in my way.”

“I don’t know what your circumstances are, but still… This is too much, isn’t it?”

When I met her eyes, filled with fear and anger, I felt like the worst bastard in the world. Maybe that was why a hollow laugh escaped me.

The Ares Guild emblem sewn into their clothes irritated me, and their shameless behavior was absurd.

That was precisely why I stopped instead of simply walking away.

“Too much? Fuck, you’re the ones who went too far.”

“W-What?”

“I don’t think people who came swarming over to kill me over those words—Code Red—have any right to say that.”

“……”

“I said meeting one person would be enough. I even tried to avoid an unnecessary fight. But you were the ones who attacked first, and you’re the ones who went down.”

I understood. They had no direct connection to Kim Hwajong’s death. How could the hands and feet know what the head had planned?

But the fact that an order had been given did not erase what they had done. They had gathered at an order to kill one person.

“Why are you doing this? I don’t know what your circumstances are, but…”

Above the low groans, a quiet voice slipped between my lips and echoed through the blackened corridor.

“Don’t spout bullshit. You should’ve thought about it before asking. Why did that bastard Jin Taekyung suddenly start acting like this? Why did a guy everyone praised for saving people and killing monsters come to our Guild and cause a scene, demanding that we bring out Go Jun? And why was an order given to kill him?”

These days, people called me a hero.

To give them the conclusion first: I wasn’t.

I lacked any noble spirit of self-sacrifice. I cared about money. And rather than living for strangers I had never met, I wanted to live for my own people.

But… at the same time, I thought I had lived without shame.

After gaining this power far beyond my station, I believed I had used it for other people whenever possible.

What kind of person was I? Was this choice right? I questioned myself again and again.

“Then why? Why? Why?”

I kept throwing out those empty questions. The vacant faces in my view disgusted and repulsed me.

“When you’re told to kill a person, why did you come here without even questioning the order?”

No one answered, but I already knew the answer myself.

Because they were nothing more than fingernails—not even Go Jun’s hands and feet. Because they were dogs living off the food Go Jun and Ares Guild gave them.

They could gain more wealth and honor by carrying out their mission. That was why, just as they had always done, they had stood in my way.

“Do you even have any idea what that bastard Go Jun has done? What if the Monster Waves in Busan and Pyeongchang were artificially caused by him?”

The moment I finished speaking, shouts erupted from every direction.

“Bullshit!”

“That’s impossible!”

Right. I knew they would react like this. That was why I had come all the way here.

Looking at their distrustful expressions, I let out a hearty laugh.

It was fascinating. They remained silent about why a man called a hero had invaded Ares Guild, yet when it came to other matters, they immediately denied everything.

“What did the higher-ups promise you in exchange for taking me down? A lightning-fast promotion within the Guild? Enough wealth to feed several generations?”

“……”

“Please, don’t give me bullshit about not having enough money to raise your kids or needing to support your widowed mother. You’re not starving right now.”

Every person here had succeeded in life. Whether they had wanted it or not, they had awakened one day and displayed enough skill to enter Ares Guild.

I had no intention of blaming them for the wealth and honor they had gained. I had once dreamed of that kind of life myself.

But the reason their choices disgusted me today was… that they had made the wrong choice to gain more, then tried to justify themselves.

That was how a group made up of individuals who had remained silent learned to fall silent as one. That was how they became the defenders of Ares, an impregnable fortress.

“So.”

I drew a deep breath. Mental exhaustion, anger, disgust, and countless other emotions churned in my chest.

“Stop spouting this fucking nonsense and lie down. Suck down your potions and get healed while you think about it. *Today is my second birthday.* Think of it that way.”

“……”

“……”

Silence filled every direction. Even the groans that had constantly seeped through the corridor could no longer be heard.

Those still standing and those lying on the ground alike either closed their eyes or firmly shut their mouths.

Ignoring their trembling gazes, I started walking. I didn’t leave out one final greeting.

“Fucking morons.”

I had no interest in whether they realized something after hearing my words or whether they still possessed the mentality of hunting dogs. My only target was one person.

And to reach that fucking bastard who still had not shown himself… there were plenty of obstacles left to break through.

Step.

My foot landed on neatly trimmed grass.

The world was still in the middle of a bitterly cold winter, but after passing through the corridor, the garden spread out at its center was a lush spring.

I had no idea what floor this was. Hundreds of flowers bloomed in profusion, and a smaller number of enemies waited for me among them.

“A lot of you gathered. You fucking bastards.”

Swish!

Instead of an answer to my greeting, an arrow packed with mana flew back at me.

Judging by how precisely it aimed for my eye, the archer who had fired it was a mean bastard. And considering the amount of mana infused into it, there was no doubt he had fired to kill.

So in this case, returning what I had received was the right thing to do.

At least, that was my way.

Clack. Swish!

I caught the arrow in my hand and flung it away in the same motion.

The arrowhead flashed as it returned to its owner twice as fast and twice as powerfully as when it had first been fired.

Kang!

A white blade trembled with a sharp metallic ring.

A middle-aged man in his fifties stared at me with deeply sunken eyes. He had deflected the arrow with an enormous greatsword.

His seasoned bearing and aura, which had reached the far edge of Peak, reminded me of a Murim martial artist.

“You’re as hot-tempered as I heard, junior.”

“It’s nice to meet you, Senior.”

With the polite attitude of a junior, I cracked my knuckles.

Crack.

The hardened joints, caked with dried blood, gave a sound like bones shifting out of place.

“If you withdraw now, I’ll pass through quietly. Ah, except for the bastard who fired that arrow.”

Slap!

The instant I finished speaking, one man’s head snapped to the side.

The middle-aged man slapped the archer on his right across the face with lightning speed, then looked at me.

“He’s still young and stupid. I ask for your leniency.”

“That wasn’t a mistake. I’ll have to break his wrist.”

“That much should be more than enough to be grateful for. Surviving is what matters.”

*What was with this guy?*

He was different from the Ares Guild members I had fought so far. As I stared at him suspiciously, the middle-aged man continued in a calm voice.

“Your offer is appreciated, but I’m afraid I have to decline. Even if I don’t look it, I’m a Guild executive. I have to cling to your trouser leg and hang on.”

“You won’t see a pretty sight.”

“What can I do? I’m a hunting dog too, in the end. Given the situation, the result is obvious, but I’d appreciate it if you went easy on me.”

What was it about his attitude?

I silently studied the middle-aged man. Then I suddenly arrived at a conclusion and opened my mouth.

“Song Cheonwoo. No—you’re with Director Song’s faction.”

The middle-aged man’s eyes widened at my words.

That meant I was right.

And it also meant I had no reason to fight them.

Song Cheonwoo had led his own faction within Ares Guild and openly opposed Go Jun. The middle-aged man in front of me must have shared his convictions.

“You… knew?”

“I heard it from someone close to him. There’s no need for us to fight, so step aside.”

The middle-aged man let out a hollow laugh.

“The enemy of my enemy is my ally?”

“At least for now, I don’t want to waste my strength or time.”

Step.

The instant I started walking again, the middle-aged man raised his greatsword diagonally.

It was an unmistakable stance preparing to attack. His troubled voice reached my ears.

“Stop. I don’t want to do this either, but I have no choice.”

I answered without stopping.

“If you don’t want to do this, why are you here? Because you’re just a hunting dog who can do nothing but obey orders?”

“……”

“If you’re afraid of Go Jun, then say you’re afraid. Don’t cover it up by saying you have no choice.”

It wasn’t only the middle-aged man. Everyone looking at me had trembling eyes.

As I continued forward without caring, the more than one hundred people in front of me also began backing away.

An invisible crack appeared across the middle-aged man’s calm expression.

“The tide has already turned. I heard Director Song returned to the United Kingdom this morning. What do you think that means? I had to find some way to survive. Even if it meant becoming a hunting dog.”

Song Cheonwoo had gone to the United Kingdom that morning? It was obviously a lie.

Certain that Go Jun had put forward a stand-in, I let out a quiet snort of laughter.

“What if that hunting dog’s master dies today?”

“……”

Everyone’s eyes opened wide.

I stretched a hand toward the empty air. At the same time, White Flame, summoned from my Inventory, slashed down diagonally.

Swish!

A single line cut across the air.

Everyone sucked in a breath, but no blood sprayed out, and no one died.

The Force shot along the white spearhead had cut something that was not human.

Slice. Crash!

The enormous stone statue standing atop the ornate fountain at the center of the garden broke into pieces and collapsed.

The remains of a statue modeled after a man who was already dead crushed the flowers beneath it.

Its head, severed from the body, rolled and rolled until it reached my feet.

The statue was too lifelike to be called a mere stone figure, and I recognized the face without difficulty.

*Lee Jungryong.*

That was right.

Today, this magnificent palace built by an ambitious warlord who had wanted to possess everything would collapse.

Along with his disciple, who had become a monster.

I tossed out a single remark toward the dumbstruck people.

“There are two choices. Put down your weapons and clear a path, or watch my back.”

“……”
```

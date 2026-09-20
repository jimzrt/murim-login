<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0566.txt",
      "sha256": "87f32d6e63a4732291e1a812f4eb50fb1f82c74b95038d9a5454fc424b51e7a3",
      "bytes": 14423
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "4a9eae2591ad8166a86f2d39726e0a6d65a7a209a01ae364fe9b2ebb7640655f",
      "bytes": 4964
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "fbb3b35f81876df0e77d50f433e62148196b97467f3b179548f5e4611be0bd97",
      "bytes": 179364
    },
    {
      "path": "characters/Cheon Taemin.md",
      "sha256": "b22901afdae2579dfc3f05d724dbe19be88fa76827b01481077a9afcc6bd123b",
      "bytes": 590
    },
    {
      "path": "characters/Cheonwoo.md",
      "sha256": "7d1c104c5b8cb28f4384c87a08cc761f100e75e9bed85f6721f7abda7861674f",
      "bytes": 590
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "0ea1ec2c0051e4483321425209a87706675cf7803489671ca1c3810d20121dc2",
      "bytes": 553
    },
    {
      "path": "characters/Go Jun.md",
      "sha256": "ff81b00cd1c4b3f590f345c59382430c4fa185723d445ad88545e8c93b58daab",
      "bytes": 898
    },
    {
      "path": "characters/Go Se-won.md",
      "sha256": "1aad17a2e14e133c840364fc021ea797df46c0d84f691751e521a7f7ed742385",
      "bytes": 635
    },
    {
      "path": "characters/Human Butcher.md",
      "sha256": "a0e283525cc1decd0a844f760ffd221386820c40ed27f510924e6eab096f42c0",
      "bytes": 667
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "406c0f7160e67bc8652f70b70a87ae6d7ee0000a25102307e29310bcb81d4d19",
      "bytes": 2280
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "712979154c872d3bc4d355f20213a3b49f2c0e9d7f3d1c53c3568364483491f4",
      "bytes": 622
    },
    {
      "path": "characters/Lee Jungryong.md",
      "sha256": "2984bc2fa53734e66eaff4aea5c62330bee649a975b5e0b883647e89787141f4",
      "bytes": 1182
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "fb9f4c91090bab9ca0a852ecfcd9331d0a8f5d5ebe4e17dc77c3f0f509bfd93e",
      "bytes": 173940
    }
  ],
  "estimated_tokens": 12635
}
-->

# Durable State Update — Chapter 566

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 566. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 566. Profile updates may replace only one
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
  "chapter": 566,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 566,
    "continuity_sources": [566],
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
    "Magic Johnson's chip contains more than twenty videos and attached materials showing simultaneous Gate and monster crises across Europe, the Middle East, West Africa, Southeast Asia, and elsewhere; worldwide mana levels are up seven percent year over year.",
    "The videos show strengthened monsters increasingly ignoring normal type advantages, with many under-defended Gates causing major casualties before suppression.",
    "Taekyung suspects this may mark the beginning of a second Great Cataclysm and plans to accelerate the project he has been developing since Murim to prevent Korea from becoming a hellish peninsula.",
    "Team Leader Choi says the crisis has exceeded the limit of national concealment and that delaying disclosure would only increase public confusion.",
    "Choi's immediate priority is reinforcing Gate defenses, despite the resulting reduction in Peace Guild's raid personnel and ability to use all its Gates.",
    "Choi will pursue action against Ares Guild alongside Gate defense; he has identified a major Ares figure who is a former Great Cataclysm war hero, Lee Jungryong's former most-trusted friend, and the leader of the largest faction threatening Go Jun.",
    "The Peace Guild remains the apparent counterweight to Ares Guild, whose authority and Go Jun's legitimacy have already been weakened by defections and public exposure.",
    "Taekyung is a Supreme Peak master, publicly recognized as S-rank-level while retaining an A-rank license, leads the Fire Dragon Pavilion's first Nanman mission, and is Peace Guild's wealthy modern-world patron.",
    "The Fire Dragon Pavilion's six-member first mission is entering Nanman through the Journey to Nanman Quest, whose reward is a linked quest and whose failure penalty is Can't Go to Nanman.",
    "Mungyeong ended Taekyung's direct training and assigned him the final task of incorporating martial principles into his learned martial arts; Cheongpung accompanies Mungyeong.",
    "Dark Heaven remains a monster-like threat capable of causing rifts and creating mutants, while the mechanism behind Jang Sam's transformation remains unresolved.",
    "The Mount Song Resolution restored the Murim Alliance with Mae Jonghak as Alliance Leader and Jeok Cheongang heading the Five Kings Hall; Zhuge Feng's Demon-Sealing Formation still blocks mana from the exposed Gate while Jang Taebo processes the Water God Dragon's remains."
  ],
  "continuity_sources": [
    565,
    564
  ],
  "open_questions": [
    "What is the Lord of Heaven's identity, how is he connected to the dangerous force Taekyung associates with his original world, and how can Dark Heaven open Gates?",
    "What will Taekyung's party find in Nanman, and what does the Southern Heaven Demon Empress intend there?",
    "What process created Jang Sam's mutant form, whether Dark Heaven's mutants can absorb human energy, and whether it relates to the Mutated Gate?",
    "What will result from the duel between Jeok Cheongang and Nangong Cheon, and why did Ju Hwaran and Sama Pyo's political engagement end?",
    "What is causing worldwide mana levels to rise, and who is the Ares figure leading the internal faction threatening Go Jun?"
  ],
  "safe_through": 565,
  "temporary_decisions": [
    "Render 건량 as dry rations, 광서 as Guangxi, 대별산 as Mount Daebyeol, 만리행 as Ten-Thousand-Li Journey, and 고잉메리호 as Going Merry.",
    "Render 반 시진 as half a shichen and retain Nanman, Nanman Beast Palace, Fire Dragon Pavilion, Great Hero, and Young Lady Ju.",
    "Render 남만행 as Journey to Nanman, 남만을 못 가 as Can't Go to Nanman, 면구 as disguise mask, 역용술 as disguise technique, 각주님 as Pavilion Master, 로그아웃 as Logout, and 동기화 as Synchronization.",
    "Render 일기당천 as One Against a Thousand, 거인의 포효 as Giant's Roar, 타락한 엔트 as Corrupted Ent, 붉은 눈 as Red Eye, 치코리타 as Chikorita, 대마도사 as Grand Mage, 순간이동 as Teleportation, 텔레포트 as Teleport, 변이 게이트 as Mutated Gate, and 몬스터 웨이브 as Monster Wave.",
    "Render 모하비 사막 as Mojave Desert, 애리조나주 as Arizona, 대의 as greater cause, 순수혈통 as pureblood, 국부 as Founding Father, 위저드(Wizard) 길드 as Wizard Guild, 조셉 바이든 as Joseph Biden, 펠릭스 왕자 as Prince Felix, 곽한구 as Gwak Hangu, 역곡 as Yeokgok, 오크의 황무지 as Orc Wasteland, 오크 로드 as Orc Lord, 국회의사당 as National Assembly, 고세원 as Go Se-won, 경호팀장 as Head of Security, A구역 as Section A, 신성불가침 as sacrosanct, 바티칸 as Vatican, 영구 임대 as permanent lease, 혈안 as bloodshot, 매직 존슨 as Magic Johnson, 썩코춘 as Sseokkochoon, 길드 하우스 as Guild House, 자이언트 맨티스 as Giant Mantis, 파이어 레인 as Fire Rain, and 파트라슈 as Patrache."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 천태민    | **Cheon Taemin**  |
| 이정룡    | **Lee Jungryong** |
| 삼성     | **Three Saints**    |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 상태               | **Status**                     |
| 헌터      | **Hunter**            |
| 길드      | **Guild**             |
| 길드장     | **Guild Master**      |
| 부길드장    | **Vice Guild Master** |
| 팀장      | **Team Leader**       |
| 랭커      | **ranker**            |
| 대격변     | **Great Cataclysm**   |
| 귀가      | **your family**                                                 |
| 대사      | **Master** for a senior Buddhist monk                           |
| 천우 | **Cheonwoo** | Name shown in a Level Window; one of the five current Five Gates scions. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 고준 | **Go Jun** | Personal name of Team Leader Seok; Lee Jungryong's prized Disciple. |
| 고세원 | **Go Se-won** | Ares Guild Head of Security and Team Leader. |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 아레스 | **Ares Guild** | The leading Guild in Korea; formerly employed Team Leader Choi and Song Song. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 주신 | **God of Drinking** | Wipeng's drinking epithet. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 준이 | **Jun** | Family nickname used in the form Jun's dad. |
| 석고준 | **Go Jun** | Source full-name form for the established Go Jun, also known as Team Leader Seok. |
| 경호팀장 | **Head of Security** | Go Jun's security-team office under Lee Jungryong. |
| 영국 | **United Kingdom** | Country associated with BCC. |
| 푸린 | **Furin** | Russian president mentioned in a forum headline. |
| 인천 | **Incheon** | Location of the airport welcome and presidential greeting. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 이정룡 | 진태경 | senior S-rank Hunter to younger Hunter and adversary | Young man | polished, teasing, and veiled-threatening | Uses a genial tone and indirect threats while trying to make Taekyung release the captives. |
| 진태경 | 이정룡 | younger Hunter to senior S-rank Hunter and adversary | you | polite but mocking and defiant | Taekyung answers Lee's soft threats with the wolf-and-tiger metaphor and refuses to yield. |
| 이정룡 | 고준 | Master to Disciple | Go Jun | familiar and testing | Lee switches from Seok's office title to his personal name while considering whether he can defeat Taekyung. |
| 고준 | 이정룡 | Disciple to Master | Master | deferential | Go Jun responds to Lee's personal-name address as 스승님. |
| 이정룡 | 천태민 | younger_to_older_brother_by_choice | older brother | reverent and familiar; internal | Lee Jungryong uses 형님 in unspoken thoughts and regards Cheon Taemin as an older brother despite having no blood relation. |
| 진태경 | 석고준 | returning Hunter to hostile Ares security leader | you fucking bastard | hostile and profane | Taekyung directs his final insults and challenge at Go Jun after returning alive. |
| 석고준 | 진태경 | hostile_opponents | brat | hostile and overconfident | Go Jun addresses Taekyung internally as 애송아 while launching his full-strength attack. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 고준 | 진태경 | Ares Guild combatant confronting the killer of his Master | you | hostile and informal | Go Jun uses 너 while demanding Jin confess to Lee Jungryong's death and threatening retaliation. |
| 진태경 | 고준 | dominant adversary confronting Lee Jungryong's Disciple | you | contemptuous and informal | Jin uses 너 and 놈 while overpowering Go Jun and ordering him to end the conflict with Lee Jungryong. |
| 석고준 | 고세원 | Ares Vice Guild Master to Head of Security | you | curt and informal | Go Jun tells Go Se-won that he is later than usual when Se-won enters the wrecked office. |
| 고세원 | 석고준 | subordinate_to_Vice_Guild_Master | Vice Guild Master | formal-deferential | Uses 부길드장님 while trying to stop Go Jun from watching the broadcast. |

## Listed compact profiles

### Cheon Taemin.md

# Cheon Taemin (천태민)

- **Safe through:** Chapter 563
- **Aliases:** Slayer
- **Role:** Ares Guild Master; humanity's great hero and the world's greatest Hunter; killed the Demon King and is known as the Slayer; created the first Mana Cultivation Method during the Great Cataclysm.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** Maternal grandfather of Team Leader Choi and father of Soyeong; regarded by Lee Jungryong as an older brother despite their lack of blood relation.

### Cheonwoo.md

# Cheonwoo (천우)

- **Safe through:** Chapter 133
- **Aliases:** None
- **Role:** One of the five current Five Gates of Shanxi scions and a First Rate martial artist present at Honghwa Inn.
- **Personality:** Pampered and contemptuous toward Cheongpung's group as part of the five scions' collective mockery.
- **Voice:** Mocking in the group's exchange; no distinct individual speech is established.
- **Relationships:** Associates with Seongryong, Myeonghwa, Sohye, and Jintae as a group of current Five Gates scions.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 565
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Go Jun.md

# Go Jun (고준)

- **Safe through:** Chapter 565
- **Aliases:** Team Leader Seok
- **Role:** Go Jun is Ares Guild's Vice Guild Master, Lee Jungryong's disciple and former Head of Security, and the de facto successor to Lee's Ares legacy who passed the S-rank Hunter qualification assessment with a very high score but lacks Lee's legitimacy.
- **Personality:** Disciplined and controlled under ordinary pressure, fiercely loyal to Lee Jungryong, but consumed by humiliation and rage when Ares Guild's authority is challenged.
- **Voice:** Dry, controlled, and formal with subordinates; deferential when addressing his Master.
- **Relationships:** Disciple and direct protégé of Lee Jungryong, Go Jun inherited Lee's Ares Guild legacy after his death and regards Jin Taekyung and Choi Minwoo as enemies seeking to take it away.

### Go Se-won.md

# Go Se-won (고세원)

- **Safe through:** Chapter 563
- **Aliases:** Head of Security
- **Role:** Go Se-won is Ares Guild's Head of Security and a Team Leader with privileged access to restricted Section A.
- **Personality:** Composed and confident in public, he is mildly uncomfortable with Ares Guild's increasingly severe discipline but obeys its policy.
- **Voice:** Calm and deferential toward superiors, but blunt and decisive when issuing orders.
- **Relationships:** Go Se-won reports to Vice Guild Master Go Jun and commands Ares Guild security personnel.

### Human Butcher.md

# Human Butcher (인도)

- **Safe through:** Chapter 562
- **Aliases:** None
- **Role:** Former mysterious Han Chinese mounted-bandit power in Northern Gaoyuan commanding fifty subordinates; a Peak master killed by an unnamed old man in a single move
- **Personality:** Cold, intimidating, and murderous; he kills people as though slaughtering livestock
- **Voice:** Cold, curt, and quietly threatening
- **Relationships:** He is one of four powerful participants at the Northern Gaoyuan gathering, intimidates Temur, and has claimed Ghost Sword Wipeng as his personal target in the proposed attack

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 565
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, a Supreme Peak master who possesses the Heavenly Martial Physique and superhuman physical strength, has manifested Force, opened his Middle Dantian, crossed the wall into true mastery, has achieved Three Flowers Gather at the Crown but not Five Qi Returning to Origin, can perceive the texture of qi well enough to sever layered magic, can resist high-level monster Fear through exceptional mental strength, is publicly recognized as an S-rank-level Hunter while formally retaining an A-rank license pending testing, can command coordinated raids against powerful monsters, serves as one of the two pavilion masters of the Alliance Leader's direct Fire Dragon Pavilion, leads its first mission to Nanman, and is the Peace Guild's wealthy patron in the modern world.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor and assigned him a final task to incorporate martial principles into his learned martial arts but declined Taekyung's recruitment after Cheongpung reached him first, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate, student, and trusted manager of media and official arrangements, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, and Xiao Shen regards him as an older brother after Jin saved him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 565
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Lee Jungryong.md

# Lee Jungryong (이정룡)

- **Safe through:** Chapter 565
- **Aliases:** None
- **Role:** Former Vice Guild Master of Ares Guild, one of Korea's two S-rank Hunters, and a Supreme Peak-level martial artist who was killed by Jin Taekyung.
- **Personality:** Outwardly genial, calm, and humorous; calculating, opportunistic, manipulative, coercive, and ruthless when challenged
- **Voice:** Smooth, good-natured, and indirect, using teasing conversation and veiled threats before becoming openly furious
- **Relationships:** Master of Park Jihoon and Go Jun (Team Leader Seok), whom he personally selected and trained; longtime Great Cataclysm acquaintance of Park Tae Seop; adversary of Jin Taekyung; knew Team Leader Choi from childhood; has an antagonistic history with Kim Hwajong, who saved his life at the collapse of Mapo Bridge eighteen years earlier; was visibly shaken by learning that Choi is Cheon Taemin's maternal grandson; regards Cheon Taemin as an older brother despite no blood relation and has long held him in respect and fear; operates as Ares Guild's senior authority beneath its Guild Master

## Korean source

```text
＃566화



최 팀장의 입에서 흘러나온 이야기는 전혀 예상치 못했던 부분이었다.

마력 수치 상승률이 높지 않았다면 오히려 이쪽에 더 흥미를 느꼈을 만큼.

‘배반자라니.’

이번 사건을 통해 아레스 길드원 중 몇몇이 우리 쪽으로 둥지를 옮기긴 했지만, 그것은 단순한 이적이었을 뿐이고 그들의 위치는 아레스 내에서도 널리고 널린 일반 길드원이었다.

하지만 내부의 배반자는 차원이 다르다.

‘심지어 그 배반자가 거물이기까지 하다면 더더욱.’

무림식 항렬로 따지면 전대 고수.

대격변을 겪은 원로 세대라는 것만으로도 벌써 구미가 당기는데, 무려 석고준을 위협할 수 있는 내부 파벌의 수장이란다.

아, 군침 싹 도네.

“……진태경 씨?”

“아, 예. 왜요?”

“우선 이것부터 좀.”

뭔가 했더니, 손수건이다. 눈을 깜빡이는 내게 최 팀장이 떨떠름한 표정으로 턱을 가리켰다.

“뭐 때문인지는 몰라도 지금 입가에 침이 잔뜩 고였습니다.”

“……아.”

“흐를 것 같, 으.”

으 뭔데. 침 좀 흘릴 수도 있지.

소매로 입가를 훔친 나는 대뜸 본론을 꺼냈다.

“그래서 누굽니까? 그 배반자가.”

“배반자라. 그 사람이 들으면 싫어할 만한 단어군요. 그는 뭐랄까…… 아마 스스로를 동업자라고 불리길 원할 겁니다. 아니면 아레스 길드의 차기 부길드장이거나.”

“그게 뭔 개떡 같은 소리예요? 최 팀장님 말 들어 보면 이미 얼추 말 맞춘 것 같고, 각 나오니까 배반자라고 부르는 건데. 정신 승리 뭐 그런 건가?”

내 반문에 대답한 것은 최 팀장이 아니었다. 조용히 선 채로 대화를 듣던 김 집사가 나직한 목소리로 입을 열었다.

“그는 명예욕이 많은 인물입니다.”

“명예욕이요?”

“사람이 나이가 들고, 죽음이 가까워지기 시작하면 명예에 집착하기 시작하죠. 아니, 그가 살아온 인생을 돌이켜 보면 탐욕(貪慾)이라는 단어가 더 적절할지도 모르겠습니다.”

김 집사가 누군가에 대해 이렇게 신랄한 어조로 말한 적이 있던가?

굳이 한 사람을 꼽자면 이정룡인데, 과거 김 집사가 그를 향해 내비친 감정이 분노라면 이번 인물을 향한 것은 경멸에 가깝다.

‘저 양반이 이 정도로 노골적인 감정을 드러내는 건 정말 흔치 않은데.’

직접 보고 들은 바에 의하면 예수나 부처 못지않은 인격자가 바로 김 집사다.

뭐, 소싯적에는 상당히 불같은 성미의 소유자였던 것 같지만 그거야 말 그대로 소싯적 얘기고.

‘그나저나 진짜 누구지?’

살아온 인생 운운하면서까지 까는 걸 보면 잘 아는 사이가 분명한데, 아레스 길드에 방귀깨나 뀌는 간부들이 워낙 많아서 선뜻 떠오르는 이름이 없다.

그리고 그런 내 궁금증을 알아차린 것처럼, 최 팀장이 불쑥 입을 열었다.

“송 이사. 송천우는 그런 사람이죠.”

“송천우. 송천우…….”

왠지 모르게 낯익은 그 이름을 스마트폰에 검색하자, 한 인물에 대한 정보가 짤막하게 떴다.

사실 정보라고 하기에도 민망한 게, 생년월일과 지금까지의 생애 몇 줄. 젊었던 시절과 함께 페이지 대문에 나란히 걸려 있는 한 사람의 사진이 전부다.

다만 아주 성과가 없는 것은 아니었다.

“어? 이 사람 혹시?”

“본 적이 있습니까?”

“네. 헌터 훈련소 복도에 항상 걸려 있는 액자에서 본 것 같은데. 아닌가?”

“아마 진태경 씨의 기억이 맞을 겁니다. 그는 이십여 년 전, 짧게나마 헌터 훈련소장직을 맡았으니까요.”

“아.”

비록 규정이 정립되기 전의 일이라지만, 헌터 훈련소장은 많은 전공을 쌓은 최상위 랭커만 오를 수 있는 자리.

‘이 정도면 진짜 거물 같긴 한데.’

그런데 이름값에 비하면 정보가 턱없이 부족하다.

이 정도라면 지금까지 쌓은 전공이나 썰도 상당할 텐데 약력 두세 줄이 전부고, 인물 페이지 업데이트도 삼 년 전이 마지막이다.

‘삼 년 전이라니.’

어지간한 B급 연예인도 이 정도는 아니겠다. 눈살을 찌푸린 내가 다른 정보를 찾기 위해 화면을 두드리던 그때였다.

우우웅.

미세한 진동과 함께 스마트폰 화면에 알림이 떴다.



〈 최 팀장님



최 팀장님

[파일 첨부]



“뭐예요. 갑자기?”

“그게 빠를 것 같아서 말입니다. 아마 인터넷 검색으로는 그에 관한 자세한 정보를 얻기 어려울 겁니다.”

“그럴 리가요. 요즘 세상이 어떤 세상인데.”

“그럼 지금 보낸 첨부 파일은 지우겠습니다.”

“하지만 성의를 봐서 보내 주신 파일은 읽겠습니다.”

“…….”

“한국말은 끝까지 들으세요.”

최 팀장에게 뼈와 살이 되는 조언을 해 준 나는 첨부 파일을 열었다. 앞서 인터넷에서 본 것과는 반대로, 이번에는 수십 페이지에 달하는 분량이다.

나는 빠르게 화면에 떠오른 정보를 머릿속에 집어넣기 시작했다.

이름은 송천우. 나이는 70대.

당연하게도 A급 헌터이며, 20년 전에는 국내 3위까지 기록했던 최상위 랭커 출신이다.

당시의 1, 2위가 바로 그 천태민과 이정룡이라는 사실을 떠올리면 이 사람 역시 상당한 강자임을 알 수 있었다.

대격변 당시 쌓은 전공으로는 굵직한 전투에 참여한 이력만 수십 회에 달하며, 국내보다는 해외의 활약이 두드러졌기 때문인지 영국, 독일, 프랑스를 포함한 8개국에서 훈장까지 받았다.

그 외의 약력은…… 일일이 따져 보기 힘들 만큼 더럽게 많다.

“경력이 화려하네요. 왜 이런 사람을 기억 못 했지?”

“생각보다 국내에서는 그리 잘 알려진 인물이 아닙니다. 지난 활약 자체가 해외에서 두드러지는 편이고, 종전 이후 국내에서의 활동도 매우 짧으니까요.”

“아. 그러네요.”

헌터 훈련소장이라는 굵직한 경력이 있지만, 4년의 임기 중 절반도 채우지 못한 상태에서 자진 사퇴 했다고 적혀 있다.

공식적인 사유는 건강상의 문제라고 하는데…….

“두 달 뒤, 아레스 길드 유럽 총괄 지사장으로 발령.”

소리 내어 지문을 읽자 최 팀장이 고개를 끄덕였다.

“그게 국내에서의 마지막 경력입니다. 이십 년 전부터 지금까지, 송천우의 직책은 유럽 총괄 지사장으로 고정되어 있었습니다. 그러니 저나 진태경 씨처럼 젊은 세대의 헌터들은 그를 잘 알지 못하죠.”

“최 팀장님은 빼시죠. 아마 송천우라는 인물을 누구보다 잘 아는 사람 중 하나일 것 같은데. 아닙니까?”

“왜 그렇게 생각하십니까?”

“누굴 바보로 아시나. 천태, 죄송합니다. 어쨌든 그분과도 상당히 연관이 있어 보이고, 김 집사님도 아실 정도니까 연결 고리는 있겠죠. 한 가지 더 예를 들면…….”

“예를 들면?”

생각은 그리 길지 않았다. 그리 오래되지 않은 기억 하나를 끄집어 올린 나는 한 마디를 툭 내뱉었다.

“유럽 총괄 지사장.”

“……!”

“전에 최 팀장님이 그랬었죠. 아레스 길드에 있을 당시에는 해외 지사만 뺑뺑이 돌았었다고. 아마 그중에서도 유럽권이었던 것 같은데.”

최 팀장의 입가에 희미한 웃음이 번진다. 정답이다.

“용케 기억하고 계시는군요.”

“저 그렇게 멍청한 놈 아니라니까.”

“진태경 씨 짐작이 맞습니다. 송천우는 제가 태어나기 전부터 외조부님을 따랐었고, 5년 전, 제가 유럽지사로 발령 나자 지사장 권한으로 곁에 두었습니다.”

“그럼 혹시 사적인 친분은…….”

“다시 생각해 보니 곁에 두었다는 표현은 어울리지 않는군요. 감시와 격리로 정정하겠습니다.”

“……쥐똥만큼도 없으시구나. 예. 계속하세요.”

“제가 직접 보고 겪은 바에 의하면, 송천우라는 인물은 품고 있는 야심의 크기에 비해 능력이 부족한 사람입니다. 과거의 경쟁 상대가 워낙 나빴던 이유도 있었겠죠.”

경쟁 상대?

이건 생각해 볼 것도 없다. 나는 한 사람의 이름을 중얼거렸다.

“이정룡.”

“산의 주인은 한 명뿐이어야 합니다. 비록 한때 친구였을지라도, 둘 중 하나는 산을 떠나야 했죠.”

이제야 아귀가 맞아떨어진다. 왜 이 정도의 인물이 종전한 지 얼마 되지도 않아 국내를 떠야 했는지.

자그마치 20년 동안이나 유럽 총괄 지사장이라는 허울 좋은 직책에 머물러야 했는지.

‘좌천이군.’

맞다. 이건 명백한 좌천이다.

아레스 길드 내부에서 벌어진 권력 투쟁에서 승리한 이정룡은 경쟁자였던 송천우를 유럽으로 유배 보냈고, 그는 사람들의 뇌리에서 천천히 잊혔다.

아니, 이정룡이라면 ‘잊히도록’ 만들었을 것이다.

‘그렇다면 이건…….’

지금 내가 읽고 있는 자료는 인터넷 따위에서 긁어모을 수 있는 찌라시가 아니다.

전문가의 마사지가 들어간 철저한 자료 조사고, 더 나아가 사찰(伺察)에 가깝다.

‘왜 굳이 따로 파일을 보내 주나 했더니.’

내심 중얼거린 나는 스마트폰 화면을 응시했다.

오 년 전을 마지막으로 업데이트가 중지된 인터넷 인물 페이지와는 달리, 자료의 마지막 페이지는 최근의 일을 다루고 있었다.



· 2046년 11월 15일. 영국 대사 주제 파티 도중 은퇴에 관하여 이야기. 음성 파일 첨부.

· 2046년 11월 28일. 서울 삼성동에 300평 규모의 2층 저택 매입. 은퇴 후 거주 목적으로 보임.

· 2047년 1월 1일. 인천공항을 통해 입국. 아레스 길드 이사회에 속한 주요 인물들과 비밀리에 회동. 정확한 인원 수와 명단은 추가 자료에 첨부.

· 2047년 1월 2일. 이정룡 영결식 참석. 정, 재계 인물을 비롯하여 길드 내 주요 인물들과 2차 회동.

· 2047년 1월 4일. 공석인 부길드장 선임 건에 관하여 아레스 길드 공식 이사회. 세 차례의 재투표 끝에 석고준 선임 가결.

.

.



약 두 달 전부터 지금까지, 송천우의 행적에 관한 정보가 빼곡하다.

그리고 텍스트를 읽는 것만으로도 그의 심경에 어떤 변화가 일어났는지, 똑똑히 알 수 있었다.

“송천우 이 양반. 아주 야심 차게 재기를 꿈꾸고 있군요.”

내 말에 최 팀장이 고개를 끄덕였다.

“11월에 사석에서 사임하겠다는 뜻을 넌지시 전했고, 국내에 은퇴 후 머무를 저택까지 매입했습니다. 하지만…….”

“이정룡이 죽었죠.”

“예. 아무도 생각지 못한 이변이었을 겁니다. 은퇴를 앞둔 누군가에게는 마지막 기회로 여겨졌을 거고요.”

“게다가 상대는 이정룡도 아니고 석고준. 최 팀장님과 힘을 합치면 해볼 만하다고 생각했겠죠.”

석고준이 부길드장직을 승계하기 위해 세 번이나 재투표를 했다는 사실이 바로 그 증거다.

은퇴를 앞둔 70대의 송천우는 온 사방에서 힘을 끌어모아 마지막 한 방을 노리고 있는 것이다.

“연세도 지긋하신 분이, 참 정력적으로 사시네.”

내 중얼거림에 최 팀장이 피식 웃었다.

“그게 권력이 가진 마력 아니겠습니까. 그 덕분에 제게도 기회가 온 거고요.”

“좋아요. 다 좋긴 한데.”

뭘까. 이 기분은. 모래를 한 움큼 씹은 것처럼 입안이 까끌거린다.

말없이 화면에 비친 송천우의 얼굴을 빤히 바라보던 그때, 최 팀장의 나직한 목소리가 귓가를 파고들었다.

“그리고 만약 이 일이 성공한다면…… 오랜만에 조손(祖孫)이 얼굴을 마주할 수 있겠죠.”

뭔 손?

멍하니 눈을 깜빡이던 나는, 얼마 지나지 않아 그 말의 의미를 깨달았다.

“설마?”

인류를 구원한 21세기의 구세주. 사람들의 뇌리에 영원히 기억될, 그러나 어느 날 홀연히 보이지 않는 장막 너머로 모습을 감춘 불멸의 영웅.

‘천태민.’

하나뿐인 핏줄이 위기에 처했을 때에도, 이정룡이 죽었음에도 결코 모습을 드러내지 않았던 그다.

그리고 영웅의 핏줄을 타고난 외손자는, 어느새 웃음기가 사라진 얼굴로 입을 열었다.

“송천우. 그자는 알고 있었습니다. 제 외할아버지께서 어디에 계신지.”



* * *



경호팀장 고세원은 자신의 앞에 놓인 찻잔을 가만히 내려다보았다.

따끈하던 찻잔은 이미 차갑게 식어 있었고, 일부러 남긴 약간의 찻물 위에는 찻잎 찌꺼기가 둥둥 떠다녔다.

‘신세가 꼭 나 같군.’

보고를 마친 뒤, 한 시간이 넘도록 찻잔만 바라보고 있었더니 이제는 정까지 들 지경이었다.

하지만 어쩔 수 없는 노릇이다. 그는 있는 사실 그대로를 보고할 뿐. 명령을 내리는 사람이 아니었으니까.

또한 이번에 자신이 전달한 사안의 중대함을 생각한다면, 지난번처럼 온 사방을 박살 내지 않은 것만으로도 다행이었다.

‘장고(長考)라. 길게 생각하는 만큼 좋은 결과가 나오기 마련이지.’

하지만 다음 순간 들려온 상관의 한 마디에, 고세원은 자신의 바람이 완전히 빗나갔다는 것을 깨달았다.

“죽여.”

“예?”

“죽이라고. 자식, 손주. 며느리. 전부다.”

툭.

테이블에서 떨어진 파일철이 바닥에 부딪히며 펼쳐진다.

송천우라고 적힌 세 글자. 그리고 광대뼈가 도드라진 그의 얼굴 사진을 바라보는 석고준의 눈에서 불길이 일렁였다.

“이 늙은이가 노망이 났나…….”
```

## Final English reading copy

```markdown
# Chapter 566

What came out of Team Leader Choi’s mouth was completely unexpected.

If the rate at which mana levels were rising hadn’t been so high, it might even have been the part that interested me most.

*A traitor?*

A few Ares Guild members had transferred over to our side because of this incident, but that had been nothing more than a simple job change. They were ordinary Guild members whose positions within Ares were a dime a dozen.

But an internal traitor was on an entirely different level.

*Especially if that traitor is a big shot.*

In Murim terms, he was a master from the previous generation.

The fact that he belonged to the elder generation that had lived through the Great Cataclysm was already enough to pique my interest, but apparently he was also the head of an internal faction powerful enough to threaten Go Jun.

*Oh, now that’s appetizing.*

“……Mr. Jin Taekyung?”

“Oh, yes. What is it?”

“Here, first of all.”

I wondered what he meant, only to find a handkerchief. When I blinked at him, Team Leader Choi pointed awkwardly at my chin.

“I don’t know why, but you have quite a bit of drool around your mouth.”

“……Oh.”

“It looks like it’s about to dr—ugh.”

What the hell was that reaction? Anyone could drool a little.

I wiped the corner of my mouth with my sleeve and got straight to the point.

“So who is it? The traitor.”

“Traitor. That’s a word he wouldn’t like very much if he heard it. How should I put it… He would probably prefer to call himself a business partner. Or perhaps the next Vice Guild Master of Ares Guild.”

“What kind of bullshit is that? From what you’ve said, you’ve already more or less struck a deal with him. If it looks like betrayal, I’m going to call him a traitor. Is he just telling himself otherwise to feel better?”

Team Leader Choi wasn’t the one who answered my question.

Butler Kim, who had been standing quietly and listening to our conversation, spoke in a low voice.

“He is a man with a great desire for honor.”

“Honor?”

“When a person grows old and begins to approach death, they often become obsessed with honor. No… Considering the life he has lived, the word *greed* might be more appropriate.”

Had Butler Kim ever spoken so harshly about anyone?

If I had to name one person, it would be Lee Jungryong. But if the emotion Butler Kim had shown toward Lee in the past was anger, then what he felt toward this person was closer to contempt.

*It’s rare for that old man to show his feelings so openly.*

From everything I had personally seen and heard, Butler Kim was a man of character on par with Jesus or Buddha.

Well, he seemed to have had quite a fiery temper in his younger days, but that was exactly what it was—something from his younger days.

*But who is it, really?*

Judging by how severely he was criticizing the man’s entire life, they clearly knew each other well. But there were so many Ares Guild executives who wielded considerable influence that no name immediately came to mind.

Then, as if he had noticed my curiosity, Team Leader Choi spoke up.

“Director Song. Song Cheonwoo is that kind of person.”

“Song Cheonwoo. Song Cheonwoo……”

The name felt oddly familiar. When I searched for it on my smartphone, a small amount of information about one person appeared.

Calling it information was almost embarrassing. There was a date of birth, a few lines about his life up to the present, and two photographs of the same man displayed side by side at the top of the page, including one from his younger days.

Still, it wasn’t completely useless.

“Huh? Is this man perhaps…?”

“Have you seen him before?”

“Yes. I think I’ve seen him in one of the framed photographs that are always hanging in the halls of the Hunter training center. Am I mistaken?”

“Your memory is probably correct. More than twenty years ago, he briefly served as the head of the Hunter training center.”

“Oh.”

Although this had been before the regulations were properly established, the position of head of the Hunter training center could only be held by a top-ranking ranker with an impressive record of achievements.

*He really does seem like a big deal.*

But compared to his reputation, the information available on him was pitifully sparse.

Someone with a career like this should have accumulated plenty of achievements and stories by now, yet all there was were two or three lines of biography. The last update to his profile had been three years ago.

*Three years ago?*

Even a middling B-list celebrity would have more information than this. I frowned and began tapping at the screen in search of something else.

That was when it happened.

*Bzzzz.*

Along with a faint vibration, a notification appeared on my smartphone screen.

> **Team Leader Choi**
>
> **Team Leader Choi**
>
> *[File attached]*

“What’s this? Why all of a sudden?”

“I thought this would be faster. You will probably have difficulty finding detailed information about him through an Internet search.”

“Come on. What kind of world do we live in these days?”

“Then I’ll delete the attached file.”

“But since you went to the trouble, I’ll read the file you sent.”

“……”

“Listen to the end when someone is speaking Korean.”

After giving Team Leader Choi some advice that would surely nourish his body and soul, I opened the attached file.

Unlike what I had seen online, this time the file was dozens of pages long.

I began rapidly absorbing the information appearing on the screen.

His name was Song Cheonwoo. He was in his seventies.

Naturally, he was an A-rank Hunter, and twenty years ago, he had been a top-ranking ranker who had reached third place in Korea.

Considering that the people in first and second place at the time had been Cheon Taemin and Lee Jungryong, it was clear that this man was also an extraordinary fighter.

His achievements during the Great Cataclysm included dozens of records of participation in major battles. Perhaps because his accomplishments had stood out more overseas than in Korea, he had even received medals from eight countries, including the United Kingdom, Germany, and France.

As for the rest of his career…

There was so much of it that it was a pain to go through piece by piece.

“His career is incredible. How did I never remember this man?”

“He is not as well known in Korea as you might expect. His past achievements were more prominent overseas, and his activities in Korea after the war were also very brief.”

“Ah. I see.”

He had a major career as head of the Hunter training center, but the file said that he had voluntarily resigned before completing even half of his four-year term.

The official reason was health problems, but……

“Two months later, he was appointed head of Ares Guild’s European regional branch.”

When I read the passage aloud, Team Leader Choi nodded.

“That was his last position in Korea. From twenty years ago until now, Song Cheonwoo’s position has remained fixed as head of the European regional branch. That is why Hunters of the younger generation, like me and Mr. Jin Taekyung, do not know much about him.”

“Leave yourself out of that. You’re probably one of the people who knows Song Cheonwoo better than anyone else. Am I wrong?”

“Why do you think that?”

“Who do you take me for, an idiot? Cheon Tae—sorry. Anyway, you seem to have quite a connection with that person, and Butler Kim knows him too, so there has to be a link. To give one more example……”

“For example?”

I didn’t need long to think. I pulled out one relatively recent memory and tossed out a single phrase.

“Head of the European regional branch.”

“……!”

“You said it yourself before. When you were with Ares Guild, you were constantly being sent around to overseas branches. I think one of those places was Europe.”

A faint smile spread across Team Leader Choi’s lips.

I had guessed correctly.

“You actually remember that.”

“I’m not as stupid as you think.”

“Your guess is correct. Song Cheonwoo had followed my maternal grandfather since before I was born. Five years ago, when I was assigned to the European branch, he used his authority as branch director to keep me close.”

“Then perhaps you had some personal relationship with him……”

“Now that I think about it, ‘kept him close’ is not the right expression. Let me correct that to surveillance and isolation.”

“Then you don’t have even the tiniest bit of a personal relationship. Right. Please continue.”

“From what I personally saw and experienced, Song Cheonwoo is a man whose abilities fall short of the size of his ambitions. That may also have been because his past rival was exceptionally formidable.”

His rival?

There was no need to think about it.

I murmured one man’s name.

“Lee Jungryong.”

“There can only be one master of a mountain. Even if the two of them had once been friends, one of them had to leave the mountain.”

Everything finally fell into place.

Why a man of this caliber had been forced to leave Korea not long after the war ended.

Why he had been made to remain in the impressive-sounding position of head of the European regional branch for no less than twenty years.

*He was demoted.*

That was right. This was an unmistakable demotion.

After winning the power struggle within Ares Guild, Lee Jungryong had exiled his rival, Song Cheonwoo, to Europe, where he had slowly faded from people’s memories.

No.

If it had been Lee Jungryong, he would have made sure Song Cheonwoo was *forgotten*.

*Then this is…*

The material I was reading was not some piece of trash scraped together from the Internet.

It was an exhaustive investigation polished by experts, and more than that, it was close to surveillance.

*So that’s why he sent me a separate file.*

I muttered inwardly as I stared at the smartphone screen.

Unlike the online profile, whose updates had stopped five years ago, the final page of the file dealt with recent events.

- **November 15, 2046.** Discussed retirement during a party hosted by the British ambassador. Audio file attached.
- **November 28, 2046.** Purchased a two-story mansion on a 300-pyeong lot in Samseong-dong, Seoul. Appears to be intended as his residence after retirement.
- **January 1, 2047.** Entered Korea through Incheon International Airport. Held a secret meeting with key figures on Ares Guild’s board of directors. Exact number and names attached in supplemental materials.
- **January 2, 2047.** Attended Lee Jungryong’s funeral. Held a second meeting with major figures in the political and business worlds, as well as key members of the Guild.
- **January 4, 2047.** Official Ares Guild board meeting concerning the appointment of a Vice Guild Master. After three revotes, Go Jun’s appointment was approved.

.

.

.

The file was packed with information about Song Cheonwoo’s movements from roughly two months ago until the present.

And simply by reading the text, I could clearly tell that something had changed in his state of mind.

“Song Cheonwoo is dreaming of a very ambitious comeback.”

Team Leader Choi nodded at my words.

“In November, he subtly expressed his intention to resign in a private setting, and he even purchased a mansion in Korea where he could stay after retirement. But……”

“Lee Jungryong died.”

“Yes. It must have been an upheaval that no one expected. For someone on the verge of retirement, it would have seemed like one last opportunity.”

“And his opponent wasn’t Lee Jungryong, but Go Jun. He must have thought that if he joined forces with you, he had a chance.”

The fact that Go Jun had needed three revotes to assume the position of Vice Guild Master was proof of that.

Song Cheonwoo, a man in his seventies approaching retirement, was gathering support from every direction and aiming for one final strike.

“He’s a pretty energetic man for someone his age.”

Team Leader Choi let out a quiet laugh at my muttering.

“Isn’t that the magic of power? It is also thanks to that magic that I was given an opportunity.”

“Fine. That’s all well and good, but……”

What was this feeling?

My mouth felt gritty, as if I had chewed on a handful of sand.

I had been silently staring at Song Cheonwoo’s face displayed on the screen when Team Leader Choi’s quiet voice pierced my ears.

“And if this succeeds…… a grandparent and grandchild may finally be able to meet face-to-face after a long time.”

“What hand?”

I blinked blankly. It didn’t take long for me to realize what he meant.

“No way?”

The savior of the twenty-first century who had rescued humanity.

The immortal hero who would be remembered forever in people’s hearts, yet had suddenly vanished one day behind an invisible curtain.

*Cheon Taemin.*

Even when his only blood relative was in danger, and even after Lee Jungryong’s death, he had never shown himself.

And his maternal grandson, born of the hero’s blood, spoke with the smile gone from his face.

“Song Cheonwoo knew where my maternal grandfather was.”

* * *

Go Se-won, the Head of Security, quietly looked down at the teacup sitting before him.

The tea that had once been warm had already gone cold, and tea-leaf residue floated on the small amount of tea he had deliberately left behind.

*This situation is just like me.*

He had spent more than an hour staring at the teacup after finishing his report. He had almost grown attached to it.

But there was nothing he could do.

All he could do was report the facts exactly as they were. He was not the one who gave orders.

Besides, considering the gravity of what he had just reported, it was fortunate that his superior had not destroyed everything around him as he had last time.

*Long deliberation. The longer he thinks, the better the result will be.*

But the next moment, one word from his superior made Go Se-won realize that his hopes had been completely misplaced.

“Kill him.”

“Excuse me?”

“I said kill him. His children. His grandchildren. His daughters-in-law. All of them.”

*Thud.*

The file folder fell from the table, struck the floor, and opened.

The three Korean characters spelling *Song Cheonwoo*.

Flames flickered in Go Jun’s eyes as he stared at the photograph of the man with prominent cheekbones.

“This old bastard has gone senile……”
```

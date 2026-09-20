<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0577.txt",
      "sha256": "81dc081d695e854733f2b5bdc30e30ce1562cf550ba6ea18a6f6a7c81ae28cd6",
      "bytes": 13015
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "db8b43860922b553b7652785fd90cb69c2ef80a76ea554ec8d17840814a3cf91",
      "bytes": 1575
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "979337dec45c6d24df237cb0ad58355d3ce4d797870bdd238aec038545cf3071",
      "bytes": 182422
    },
    {
      "path": "characters/Cheon Taemin.md",
      "sha256": "99cf1af812b24a87f0b4f14621cc347f67760bc8ce18b6dc03141963c88ad430",
      "bytes": 607
    },
    {
      "path": "characters/Cheonwoo.md",
      "sha256": "4990397f284c446f6558d791901e523665d60fe3f7a9164efec479d20a034782",
      "bytes": 590
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "48ddd2091c3a7a863790c428c1b6f769303ec6bff23c1a0f0f1d25e041d94ec2",
      "bytes": 553
    },
    {
      "path": "characters/Go Jun.md",
      "sha256": "a324eac67bd68d4e8d25415a4d29a3398cf3951e4df8f9e247ee321d5ba8c241",
      "bytes": 976
    },
    {
      "path": "characters/Hwa-jong.md",
      "sha256": "1605beaefde4905fbe17ab11d6ef00d98954ed892dd20576a04e1541947618af",
      "bytes": 562
    },
    {
      "path": "characters/Kim Hwajong.md",
      "sha256": "f8b7ecf43bf42ec2b13090497062e465303d13ca99985225052d37b59b8bbfd8",
      "bytes": 536
    },
    {
      "path": "characters/Lee Jungryong.md",
      "sha256": "cbf6c9803e20340b7c565aa0ac5b6c3d847c6675e5c0c6be2aa37f457fe2f424",
      "bytes": 1281
    },
    {
      "path": "characters/Song Cheonwoo.md",
      "sha256": "445671bc44f1fcab5014f5a1479581861e1c76e994c58b95a72521a808187580",
      "bytes": 1013
    },
    {
      "path": "characters/Team Leader Choi.md",
      "sha256": "cac5563c3555be65205dedee3f4ff8641a59dca260583c063c339fb5f786df77",
      "bytes": 904
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "3aecb7a74b2fdb7e72da2bb4d026cde072621b2acdccca691171c95ab6dce63e",
      "bytes": 178893
    }
  ],
  "estimated_tokens": 10205
}
-->

# Durable State Update — Chapter 577

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 577. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 577. Profile updates may replace only one
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
  "chapter": 577,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 577,
    "continuity_sources": [577],
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
    "Busan's Kraken has been eliminated, but more than one thousand Mermen remain across Haeundae and Gwangalli while the Peace Guild and other forces contain the disaster.",
    "Song Cheonwoo warned Choi Minwoo that Go Jun is preparing a trap related to Choi's maternal grandfather.",
    "Song met Choi disguised by an illusion spell inside the Peace Guild-owned Yeti's Winter Range Gate in Pyeongchang.",
    "Ares Guild headquarters contains a restricted secret Area A whose existence and name Choi already knew.",
    "Song claims Choi's maternal grandfather is in Area A and lost consciousness more than twenty years ago, but the information is uncertain.",
    "Butler Kim's personal name is Hwa-jong, and his former alliance with Song Cheonwoo ended over loyalty and ambition."
  ],
  "continuity_sources": [
    576
  ],
  "open_questions": [
    "Who empowered and released the Kraken, and did that person engineer the Monster Wave?",
    "Is Choi Minwoo's maternal grandfather actually in Area A of Ares Guild headquarters?",
    "What happened to Choi Minwoo's maternal grandfather when he lost consciousness more than twenty years ago?",
    "What trap is Go Jun preparing, and can Song Cheonwoo's warning be trusted?"
  ],
  "safe_through": 576,
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

| 김화종    | **Kim Hwajong**   |
| 최민우    | **Choi Minwoo**   |
| 천태민    | **Cheon Taemin**  |
| 이정룡    | **Lee Jungryong** |
| 상태               | **Status**                     |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 몬스터     | **monster**           |
| 길드      | **Guild**             |
| 천우 | **Cheonwoo** | Name shown in a Level Window; one of the five current Five Gates scions. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 고준 | **Go Jun** | Personal name of Team Leader Seok; Lee Jungryong's prized Disciple. |
| 화종 | **Hwa-jong** | Butler Kim's personal name. |
| 송천우 | **Song Cheonwoo** | Ares Guild Director, former third-ranked Korean Hunter, and longtime European regional branch director. |
| 아스모데우스 | **Asmodeus** | Demon King referenced in Taekyung's sarcastic comparison; does not appear directly. |
| 아레스 | **Ares Guild** | The leading Guild in Korea; formerly employed Team Leader Choi and Song Song. |
| 사장님 | **Boss** | Address for the restaurant owner; contextually rendered as ma'am in one reply |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 석고준 | **Go Jun** | Source full-name form for the established Go Jun, also known as Team Leader Seok. |
| 슬레이어 | **Slayer** | Cheon Taemin's title after killing the Demon King. |
| 마왕 | **Demon King** | The being Cheon Taemin killed. |
| 도련님 | **Young Master** | Address used for Team Leader Choi by Butler Kim. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 성도 | **Chengdu** | Sichuan destination of Taekyung's party. |
| 시리 | **City** | Second word in one of the necromantic chants. |
| 성하 | **Seongha** | Hunter named during the cave battle. |
| 예티 | **yeti** | Monster species in the Gate's name and raid dialogue. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 이정룡 | 고준 | Master to Disciple | Go Jun | familiar and testing | Lee switches from Seok's office title to his personal name while considering whether he can defeat Taekyung. |
| 고준 | 이정룡 | Disciple to Master | Master | deferential | Go Jun responds to Lee's personal-name address as 스승님. |
| 이정룡 | 천태민 | younger_to_older_brother_by_choice | older brother | reverent and familiar; internal | Lee Jungryong uses 형님 in unspoken thoughts and regards Cheon Taemin as an older brother despite having no blood relation. |
| 석고준 | 최민우 | Ares security leader to rival Guild Master | Team Leader Choi Minwoo | formal but barbed | Uses 평화 길드 최민우 팀장님 while belittling Choi and blaming the Peace Guild for Taekyung's apparent death. |
| 송천우 | 석고준 | adversary; captor of Song's children | you | shocked and confrontational | Song reacts directly to Go Jun's admission that he took the children. |
| 화종 | 최민우 | butler_to_Young_Master | Young Master | formal and deferential | Butler Kim consistently addresses Choi Minwoo with the established deferential title. |
| 송천우 | 화종 | former_allies | Hwa-jong | familiar and informal | Song uses Hwa-jong's personal name, prompting Hwa-jong to reject the familiarity. |
| 화종 | 송천우 | former_allies_now_hostile | you | formal and cold | Hwa-jong challenges Song's right to expect Choi's trust and rejects their former intimacy. |
| 송천우 | 최민우 | older_former_ally_to_younger_former_ally | Minwoo | familiar and informal | Song addresses Choi by his given name while discussing the meeting place and surveillance. |

## Listed compact profiles

### Cheon Taemin.md

# Cheon Taemin (천태민)

- **Safe through:** Chapter 575
- **Aliases:** Slayer
- **Role:** Ares Guild Master; humanity's great hero and the world's greatest Hunter; killed the Demon King and is known as the Slayer; created the first Mana Cultivation Method during the Great Cataclysm.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** Maternal grandfather of Team Leader Choi and Jin Taekyung and father of Soyeong; regarded by Lee Jungryong as an older brother despite their lack of blood relation.

### Cheonwoo.md

# Cheonwoo (천우)

- **Safe through:** Chapter 576
- **Aliases:** None
- **Role:** One of the five current Five Gates of Shanxi scions and a First Rate martial artist present at Honghwa Inn.
- **Personality:** Pampered and contemptuous toward Cheongpung's group as part of the five scions' collective mockery.
- **Voice:** Mocking in the group's exchange; no distinct individual speech is established.
- **Relationships:** Associates with Seongryong, Myeonghwa, Sohye, and Jintae as a group of current Five Gates scions.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 576
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Go Jun.md

# Go Jun (고준)

- **Safe through:** Chapter 576
- **Aliases:** Team Leader Seok
- **Role:** Go Jun is Ares Guild's Vice Guild Master, Lee Jungryong's disciple and former Head of Security, and the de facto successor to Lee's Ares legacy who passed the S-rank Hunter qualification assessment with a very high score but lacks Lee's legitimacy.
- **Personality:** Disciplined and controlled under ordinary pressure, fiercely loyal to Lee Jungryong, but consumed by humiliation and rage when Ares Guild's authority is challenged.
- **Voice:** Dry, controlled, and formal with subordinates; deferential when addressing his Master.
- **Relationships:** Disciple and direct protégé of Lee Jungryong, Go Jun inherited Lee's Ares Guild legacy after his death, regards Jin Taekyung and Choi Minwoo as enemies seeking to take it away, and has seized Song Cheonwoo's children as leverage while calling it protection.

### Hwa-jong.md

# Hwa-jong (화종)

- **Safe through:** Chapter 576
- **Aliases:** Butler Kim
- **Role:** Hwa-jong is Choi Minwoo's loyal butler and personal escort.
- **Personality:** Loyal, vigilant, and uncompromising toward perceived threats to Choi Minwoo.
- **Voice:** Formal and deferential toward Choi Minwoo, cold and openly hostile toward Song Cheonwoo.
- **Relationships:** Hwa-jong serves Choi Minwoo and was formerly close to Song Cheonwoo, but their relationship ended over loyalty and ambition.

### Kim Hwajong.md

# Kim Hwajong (김화종)

- **Safe through:** Chapter 288
- **Aliases:** Butler Kim
- **Role:** Level 80 mage known as Butler Kim; former Class 3 instructor at the Hunter Training Center; arrives at the confrontation between Im Chunsoo and Jin Taekyung
- **Personality:** Gentle and composed
- **Voice:** Gentle and measured
- **Relationships:** Former instructor of Im Chunsoo, who remains terrified of and obedient to him; addresses Im Chunsoo familiarly as Chunsoo

### Lee Jungryong.md

# Lee Jungryong (이정룡)

- **Safe through:** Chapter 570
- **Aliases:** None
- **Role:** Former Vice Guild Master of Ares Guild, one of Korea's two S-rank Hunters, and a Supreme Peak-level martial artist who was killed by Jin Taekyung.
- **Personality:** Outwardly genial, calm, and humorous; calculating, opportunistic, manipulative, coercive, and ruthless when challenged
- **Voice:** Smooth, good-natured, and indirect, using teasing conversation and veiled threats before becoming openly furious
- **Relationships:** Master of Park Jihoon and Go Jun (Team Leader Seok), whom he personally selected and trained; longtime Great Cataclysm acquaintance of Park Tae Seop; adversary of Jin Taekyung; knew Team Leader Choi from childhood; has an antagonistic history with Kim Hwajong, who saved his life at the collapse of Mapo Bridge eighteen years earlier; was visibly shaken by learning that Choi is Cheon Taemin's maternal grandson; regarded Cheon Taemin as an older brother despite no blood relation and long held him in respect and fear; secretly supported the orphanage where Lee Dongseok grew up and was regarded by Dongseok as a father; operated as Ares Guild's senior authority beneath its Guild Master

### Song Cheonwoo.md

# Song Cheonwoo (송천우)

- **Safe through:** Chapter 576
- **Aliases:** Director Song
- **Role:** Ares Guild Director and former A-rank Hunter who reached third place among Korean rankers, briefly headed the Hunter training center, and led Ares Guild's European regional branch for twenty years; he now leads an internal faction capable of threatening Go Jun.
- **Personality:** Highly ambitious, honor-obsessed, politically calculating, and determined to use his final opportunity to reclaim influence before retirement.
- **Voice:** Not established.
- **Relationships:** Song Cheonwoo followed Cheon Taemin since before Team Leader Choi was born, was Lee Jungryong's former friend and rival, was exiled to Europe after Lee's victory, is aligned with Choi against Go Jun, has had his children seized by Go Jun as leverage, and has given Choi an uncertain report that Cheon Taemin is in Area A and has been unconscious for over twenty years.

### Team Leader Choi.md

# Team Leader Choi

- **Safe through:** Chapter 576
- **Aliases:** Choi Minwoo (최민우)
- **Role:** Team Leader Choi is Cheon Taemin's only living blood relative and is positioning himself to take control of the Ares Guild after Lee Jungryong's death.
- **Personality:** Strategic, candid, controlled, and possessive of the power and influence he intends to inherit.
- **Voice:** Dry, formal, and direct, with calm candor and carefully chosen metaphors.
- **Relationships:** Choi Minwoo is Cheon Taemin's maternal grandson and only living blood relative, was kept out of public knowledge by Lee Jungryong, is closely integrated with Jin Taekyung's family, seeks to acquire the Ares Guild intact, and is investigating Song Cheonwoo's uncertain report that Cheon Taemin is in Area A and has been unconscious for over twenty years.

## Korean source

```text
＃577화



딱딱하게 굳은 얼굴. 송천우를 응시하던 최민우의 눈빛이 가늘게 떨렸다.

“그게…… 무슨 말입니까.”

“믿지 못하겠지만, 틀림없는 사실이다.”

송천우가 한숨처럼 말을 이었다.

“어느 날, 갑작스럽게 벌어진 일이었다. 그 누구도 예상치 못했지.”

“……!”

최민우는 자신도 모르게 주먹을 움켜쥐었다.

송천우를 결코 신뢰하지 않는 그였지만, 지금 마주한 눈앞의 노인에게서는 일말의 거짓도 느껴지지 않았다.

‘그럼, 정말로?’

순간 최민우의 심장이 쿵, 하고 내려앉았다. 어느새 맺힌 식은땀 한 방울이 목덜미를 타고 굴러떨어진다.

굳게 다물어져 있던 입술 사이로 간신히 끄집어낸 목소리가 흘러나왔다.

“하지만 저는 그 누구에게도 그런 사실을 들은 적이 없습니다. 심지어 외할아버님의 측근이셨던 김 집사님께서도…….”

최민우의 말이 끝나기도 전, 송천우가 고개를 가로저었다.

“말해 주지 않은 것이 아니라, 못 한 것이다.”

“그렇다는 건…….”

“미안하구나.”

안 한 것과 못 한 것.

고작 한 글자 차이지만 그 차이는 크다. 말에 담긴 뜻을 깨달은 최민우가 송천우를 노려보았다.

“김 집사님께도 감췄던 겁니까. 그토록 중요한 사실을.”

칠순의 노인은 조용히 고개를 끄덕였다. 부쩍 늙은 목소리가 입술을 비집고 흘러나왔다.

“화종이. 저 친구는 언제나 충성스러웠다. 그리고 그 마음은 종전(終戰) 이후 태어난 한 생명에게 고스란히 이어졌지. 어린 나이에 불의의 사고로 부모를 잃고, 홀로 남겨진 어린아이 말이다.”

“……!”

“모든 것이 달라진 그 날에도, 그분의 가장 충실한 심복은 네 곁에 있었다.”

최민우는 자신도 모르게 고개를 돌렸다.

멀찍이 떨어진 눈밭에서 이곳을 직시하고 있는 한 사람이 시야에 들어온다.

맹렬하게 몰아치는 눈보라에 송천우의 목소리가 파묻히지 않았다면, 나는 듯이 달려와 배신자를 죽이려 들었을 충복이었다.

“이거였습니까? 단둘이 걷자고 한 이유가.”

“어쩔 수 없었다. 그가 듣고 있었다면 대화가 이어지지 못했을 테니까.”

“만약 그때 김 집사님께서 외할아버님에 관한 소식을 들었다면, 당신들은 이미…….”

언제나 침착하고 냉철하던 태도는 더 이상 찾아볼 수 없다.

시퍼런 불길이 일렁이는 최민우의 눈빛에, 송천우는 감히 시선을 마주하지 못하고 고개를 돌렸다.

“처음에는 그저 당황스러웠다. 그분이 금방 의식을 회복하시리라 생각하고 우선 극비에 부쳤지.”

사박.

힘없는 발걸음과 함께, 늙수그레한 목소리가 이어졌다.

“하지만 그렇게 한 달. 반년. 그리고 일 년이 지나자, 문득 묘한 생각이 들더군. 어쩌면…… 그분께서는 영영 깨어나시지 못하는 것이 아닌가 하는 생각이.”

송천우와 이정룡.

처음만 해도 설마 했던 두 사람의 마음은 시간이 흐름에 따라 점점 확신으로 굳혀졌고, 그 생각은 또 다른 감정으로 변화했다.

“다시 일 년이 흐르자, 우리는 서로가 가진 탐욕을 확인할 수 있었다.”

감히 그 누구도 범접할 수 없던 절대자, 천태민이 남긴 빈자리를 차지하고 싶다는 탐욕. 아레스 길드라는 거대한 성의 주인이 되고 싶다는 욕심.

“숙청은 어느 날 은밀하게 시작되었다. 이미 아레스 길드와 멀어진 김화종과는 달리, 그분의 상태를 알고 있던 최측근들 몇이 게이트에서 죽음을 맞이했지.”

최민우는 입술을 질끈 깨물었다.

고대부터 현대에 이르기까지, 진실을 묻기 위한 가장 확실한 방법은 죽음이다.

이정룡과 송천우 역시 같은 길을 택했다. 아직 살아 있는 왕의 제위를 찬탈하기 위하여.

으득.

거스러미 하나 없이 매끈한 입술이 터지고, 붉은 선혈이 턱을 타고 흘러내린다.

분노가 담긴 최민우의 발걸음이 새하얀 눈 위에 점점이 떨어진 핏방울을 밟았다.

“그 와중에 지사장님은 용케 살아남으셨군요. 참으로 질긴 목숨입니다.”

최민우의 신랄한 어조에 송천우가 무력한 목소리로 대답했다.

“이정룡의 입장에서도 날 제거하는 건 쉽지 않았으니까. 더군다나 아레스 길드를 사이에 두고 싸우는 과정에서 사이좋게 오물을 나눠 묻힌 사이라 발설할 가능성도 적었다고 판단했겠지. 사실이기도 했고.”

진실을 아는 것은 죽을 이유가 되지만, 함께 진흙탕을 뒹굴었다면 살아남을 이유가 된다.

그리고 최민우의 눈에 비친 송천우는 마지막까지 이정룡에게 맞서 싸울 만한 그릇이 아니었다.

“그 협상의 대가가 유럽 총괄 지사장 자리였습니까?”

“그래. 덕분에 나와 가족들의 목숨만은 건질 수 있었다.”

최민우는 크게 심호흡했다. 이제야 좀처럼 풀리지 않던 머릿속의 퍼즐이 완벽하게 짜 맞춰지는 기분이었다.

그토록 냉정하고 철저하던 이정룡이 왜 굳이 송천우를 살려 두었는지.

그리고 하나뿐인 혈육이자 세계의 상징이 되어 버린 외할아버지가 왜 이십 년이 넘도록 모습을 드러내지 않았는지.

- 쿠워어어어!

어디선가 들려오는 예티의 포효가 최민우의 심정을 대신하는 듯했다.

‘빌어먹을.’

까득.

온 힘을 다해 말아쥔 주먹에서 뼈 어긋나는 소리가 들렸다.

당장이라도 소리치고 싶다. 왜 그랬느냐고. 도대체 무엇을 위해 그런 짓을 벌였느냐고.

있는 힘껏 고함을 지르고, 멱살을 붙잡고, 허리춤에 매어 둔 검을 빼내어 앞서가는 저 노인의 등을 찌르고 싶었다.

하지만…….

스륵, 툭.

검파(劍把)를 향해 움직이던 손은 목적을 달성하지 못하고 힘없이 떨어졌다.

아직은 때가 아니다. 송천우의 죗값을 받아 내는 것은 적어도 모든 사실을 확인한 후여야 했다.

세차게 뛰는 심장을 애써 가라앉힌 최민우가 떨리는 목소리로 입을 열었다.

“외할아버님께서 쓰러지신 이유가 뭡니까?”

사박. 눈을 밟는 소리와 함께 앞서가던 송천우의 걸음이 우뚝 멈췄다.

어느새 그의 앞에는 텅 빈 허공만이 펼쳐져 있었다.

크레바스(Crevasse). 설산과 빙하지대에서 나타난다는 균열은 거대했고, 도무지 깊이를 짐작할 수 없는 내부는 심연처럼 어두웠다.

“이유. 이유라…….”

발 앞에 펼쳐진 어둠을 바라보던 송천우가 낮게 뇌까렸다.

“모른다.”

“확실히 하십시오. 모르는 건지. 모르는 척하고 싶은 것인지.”

“나나 이정룡이 무슨 수작을 부렸다고 생각하는 것이냐? 다른 누구도 아닌 그분께?”

“그건…….”

최민우는 문득 입을 다물었다. 자신의 외조부가 어떤 사람인지 다시 한번 떠올랐기 때문이었다.

천태민. 인류가 낳은 불멸의 영웅. 지구에 강림한 수많은 몬스터와 그들의 군주, 마왕 아스모데우스를 쓰러트린 최초이자 최후의 헌터.

살아남은 인류는 자신들을 구한 영웅에게 슬레이어(Slayer)라는 이명을 붙여 주었고, 그것은 헌터들이 누구도 범접할 수 없는 강자에게 바치는 경의이기도 했다.

“나는 그분을 존경했고, 두려워했다. 그리고 그건 이정룡도 마찬가지였지. 만약 그렇지 않았다면 몇 년 동안이나 그분이 깨어나시길 기다리지는 않았을 것이다.”

맞다. 존경과 두려움의 대상이었던 천태민이 쓰러진 후에도 송천우와 이정룡은 쉽사리 움직이지 못했다.

그런 그들이 탐욕을 드러내기까지는 2년이라는 시간과 천태민의 상태를 확인하기 위한 수많은 실험. 그리고 약간의 불안감이 섞인 확신이 필요했다.

“그렇다면 도대체……?”

등 뒤로 들려오는 혼란스러운 목소리에, 송천우가 고개를 가로저었다.

“그 이유는 누구도 짐작할 수 없겠지. 하지만 한 가지는 확실하다. 그분께서는 아직도 살아 계시다는 것.”

이 다음으로 묻고자 했던 질문의 답이 송천우의 입술 사이로 흘러나왔다. 혼란스러운 마음을 가다듬은 최민우가 물었다.

“그렇게 생각한 근거는 뭡니까.”

“그분께서 돌아가셨다면, 이정룡이 굳이 지금까지 나를 살려 둘 리 없을 테니까.”

“……!”

“다만 그분을 어디에 모셔 두었는지는 정확하지 않다. 지금으로서는 A구역이 의심될 뿐이지.”

“A구역…….”

낮게 뇌까린 최민우는 문득 고개를 들었다.

그의 시선이 크레바스 앞에 선 채 거대한 균열을 하염없이 내려다보는 송천우의 등에 닿았다.

“마지막으로 몇 가지 물어볼 것이 있습니다.”

“뭐든지 물어보거라.”

말없이 그의 뒷모습을 바라보던 최민우가 불쑥 한마디를 던졌다.

“이유가 궁금합니다.”

“……이유?”

“그렇습니다. 하필이면 지금 모든 것을 털어놓는 이유. 지금은 협력 관계지만, 곧 머지않은 미래에 또 다른 경쟁자가 될 제게 이런 중요한 사실을 알려 준 이유가.”

적의 적은 동지. 최민우와 송천우는 그런 관계였다.

석고준을 끌어내리기 위해, 아레스 길드를 자신의 것으로 만들기 위해 일시적으로 손을 잡았을 뿐. 그 이상도 이하도 아니다.

그렇기에 최민우는 더더욱 송천우의 태도를 이해할 수 없었다.

‘갑자기 변했어.’

마지막으로 비밀리에 만남을 가진 것이 고작해야 일주일 전이다.

그때만 해도 송천우의 태도는 조심스러웠고, 말과 행동에서는 희미한 경계가 묻어 나왔었다.

한때나마 이정룡과 정적(政敵) 관계에 놓였던 사람답게, 이 일시적인 동맹이 성공적으로 목적을 달성함과 동시에 깨진다는 것을 알고 있던 것이다.

‘그런데 왜?’

천태민의 신변에 관한 정보는 극비 중의 극비요, 훗날의 대립을 생각한다면 최민우를 물러나게 할 수도 있는 중요한 무기다.

단순히 한순간의 감정에 사로잡혀 허심탄회하게 털어놓을 수 있는 이야기가 아니었다.

스륵.

최민우의 손끝이 검자루에 닿은 그때. 묵묵히 까마득한 허공을 내려다보던 송천우의 신형이 천천히 돌아섰다.

“이유라.”

노인의 목소리는 담담하면서도 침착했다.

처음 게이트 앞에서 만날 때만 해도 머뭇거리고 잘게나마 떨렸던 음성은 더이상 찾아볼 수 없었다.

최민우가 그의 시선이 자신의 손을 향했다고 느낀 순간, 나직한 목소리가 이어졌다.

“속죄(贖罪)라고 해 두는 것이 좋겠구나.”

최민우는 검을 쥔 손에 힘을 더하며 물었다.

“무엇에 대한 속죄입니까.”

“늦었지만 언젠가 말하고 싶었다. 그분과, 그리고 네게 저지른 잘못에 대해서.”

“이십 년도 더 늦었군요.”

“그래, 늦었지. 하지만 어쩔 수 없었다.”

“변명입니다.”

최민우가 단호하게 대답한 그 순간이었다.

구구구구궁!

온통 새하얀 눈에 파묻힌 설산(雪山)이 몸을 떨었다. 수십 미터의 폭을 지닌 크레바스 너머에서 눈사태가 일어나고 있었다.

지금 이 순간에도 거칠게 굽이치는 눈의 파도 위에, 털로 뒤덮인 거인들이 있었다.

- 쿠워어어어어!

- 카우우!

흉포한 포효가 설산을 떨어 울렸다.

언뜻 보기에도 수백 마리에 달하는 예티의 돌진에, 최민우가 문득 중얼거렸다.

“희한한 일이군요.”

“뭐가 말이냐?”

“예티는 보통 십여 마리 전후로 모여 무리 생활을 합니다.”

“그래, 그랬었지.”

사박. 스르릉.

크레바스를 등진 송천우의 걸음이 앞으로 나아갔고, 최민우의 허리춤에 매여 있던 검이 뽑혀져 나왔다.

죽어서도 본분을 다했던, 어느 영웅이 남긴 검이었다.

“좋은 검이구나.”

낮게 뇌까린 송천우가 다시 한 번 걸음을 내디뎠다.

최민우의 어깨너머에서는 이미 한 사람이 쏘아지고 있었다.

“도련님!”

늙은 충복의 외침을 들으며, 송천우가 중얼거렸다.

“이해해라. 어쩔 수 없었다.”

그리고 다음 순간.

콰아아앙!

굉음과 함께 눈보라가 휘몰아쳤다.
```

## Final English reading copy

```markdown
# Chapter 577

Choi Minwoo’s face had gone rigid. His eyes, fixed on Song Cheonwoo, trembled faintly.

“What… do you mean?”

“You may not believe me, but it is an undeniable fact.”

Song Cheonwoo continued with a sigh.

“It happened suddenly one day. No one saw it coming.”

“……!”

Without realizing it, Choi Minwoo clenched his fists.

He had never trusted Song Cheonwoo in the slightest, but he could not sense even a trace of falsehood from the old man standing before him.

*Then is it really true?*

For an instant, Choi Minwoo’s heart sank with a thud. A bead of cold sweat had formed before he knew it, rolling down the back of his neck.

A voice barely escaped between his tightly pressed lips.

“But I’ve never heard anything like that from anyone. Not even Butler Kim, who was my maternal grandfather’s closest aide…”

Before Choi Minwoo could finish, Song Cheonwoo shook his head.

“He did not choose not to tell you. He could not.”

“Then…”

“I am sorry.”

There was a difference between choosing not to do something and being unable to do it.

Only one character separated the two phrases, but the difference was enormous. Realizing what Song Cheonwoo’s words meant, Choi Minwoo glared at him.

“You hid it from Butler Kim too? Something this important?”

The septuagenarian quietly nodded. His voice, suddenly much older, forced its way between his lips.

“Hwa-jong. That man was always loyal. And he gave that same loyalty, whole and undiminished, to a life born after the war ended. A young child who lost his parents in an unfortunate accident and was left all alone.”

“……!”

“Even on the day everything changed, your grandfather’s most loyal aide was at your side.”

Choi Minwoo turned his head without realizing it.

A figure standing far away in the snow came into view, staring directly at them.

Had Song Cheonwoo’s voice not been swallowed by the howling blizzard, that loyal servant would have flown over and tried to kill the traitor.

“Was this why you asked me to walk with you alone?”

“It was unavoidable. If he had been listening, we would not have been able to continue this conversation.”

“If Butler Kim had heard about my maternal grandfather back then, you two would already have…”

The calm, cool composure he always maintained was nowhere to be found.

Blue flames seemed to flicker in Choi Minwoo’s eyes. Song Cheonwoo did not dare meet his gaze and turned his head away.

“At first, we were merely confused. We thought he would regain consciousness soon, so we kept it strictly confidential.”

*Crunch.*

His weary footsteps continued, followed by his aged voice.

“But then a month passed. Then half a year. Then a year. And a strange thought suddenly occurred to me. What if… he never woke up?”

Song Cheonwoo and Lee Jungryong.

At first, neither man had dared believe it. But as time passed, their suspicions gradually hardened into certainty—and that certainty changed into another emotion.

“Another year passed, and we discovered the greed we each carried.”

The greed to take the empty place left behind by Cheon Taemin, the absolute ruler no one had ever dared approach. The desire to become the master of the enormous fortress called Ares Guild.

“The purge began in secret one day. Unlike Kim Hwajong, who had already grown distant from Ares Guild, several of the closest aides who knew about his condition met their deaths in Gates.”

Choi Minwoo bit down hard on his lip.

From ancient times to the modern day, the surest way to bury the truth was death.

Lee Jungryong and Song Cheonwoo had chosen the same path. They intended to usurp the throne while its king was still alive.

*Crack.*

His smooth, flawless lips split open, and bright red blood trickled down his chin.

Choi Minwoo’s furious steps trampled the drops of blood falling onto the pure white snow.

“You managed to survive all that, Regional Director. You really are tenacious.”

Song Cheonwoo answered Choi Minwoo’s cutting sarcasm in a feeble voice.

“It was not easy for Lee Jungryong to eliminate me, either. Besides, while we fought over Ares Guild, we had both gotten equally covered in filth. He must have judged that I was unlikely to reveal anything. And he was right.”

Knowing the truth could be a reason to die. But if you had wallowed together in the mud, it could also be a reason to survive.

And in Choi Minwoo’s eyes, Song Cheonwoo was not the kind of man who could have continued resisting Lee Jungryong to the very end.

“Was the price of that negotiation the position of European regional branch director?”

“Yes. Thanks to it, I was able to save my life and the lives of my family.”

Choi Minwoo took a deep breath. At last, the puzzle that had refused to fit together in his mind seemed to be falling perfectly into place.

Why Lee Jungryong, so cold and thorough, had gone out of his way to keep Song Cheonwoo alive.

And why his only blood relative, the man who had become a symbol of the world, had not appeared for more than twenty years.

—Kraaaaaaar!

A yeti’s roar echoed from somewhere, as though voicing Choi Minwoo’s feelings.

*Damn it.*

*Crack.*

The bones in his tightly clenched fist shifted with a harsh sound.

He wanted to scream. He wanted to ask why they had done it. What in the world had driven them to such a thing?

He wanted to shout with all his strength, seize Song Cheonwoo by the collar, draw the sword hanging at his waist, and stab the old man in the back as he walked ahead.

But…

*Swish. Thud.*

The hand moving toward his sword hilt failed to reach its destination and dropped limply.

*It is not time yet.*

He could demand payment for Song Cheonwoo’s sins only after confirming every fact.

Forcing down the pounding in his chest, Choi Minwoo spoke in a trembling voice.

“Why did my maternal grandfather collapse?”

*Crunch.*

Along with the sound of footsteps pressing into the snow, Song Cheonwoo’s stride came to an abrupt halt.

An empty void now stretched out before him.

A crevasse.

The enormous crack said to appear in snow-covered mountains and glacial regions was dark inside, like an abyss whose depth could not be gauged.

“Why. Why, you ask…”

Song Cheonwoo stared down at the darkness spread before his feet and muttered in a low voice.

“I do not know.”

“Be precise. Do you not know? Or do you merely want to pretend you do not know?”

“Do you think Lee Jungryong or I pulled some kind of trick? On him, of all people?”

“That…”

Choi Minwoo suddenly fell silent. He had remembered once more what kind of person his maternal grandfather was.

Cheon Taemin.

An immortal hero born from humanity. The first and last Hunter to defeat the countless monsters and their lord, the Demon King Asmodeus, who descended upon Earth.

The surviving human race gave the hero who had saved them the title Slayer, a name that also expressed the reverence Hunters offered to a powerhouse no one could approach.

“I respected him, and I feared him. Lee Jungryong was the same. If he had not, we would not have waited for him to awaken for so many years.”

It was true. Even after Cheon Taemin, the object of their respect and fear, collapsed, Song Cheonwoo and Lee Jungryong had been unable to act easily.

It took two years, countless experiments to confirm Cheon Taemin’s condition, and a certainty laced with a measure of anxiety before those men finally revealed their greed.

“Then what in the world…?”

At the confused voice coming from behind him, Song Cheonwoo shook his head.

“No one can guess the reason. But one thing is certain. He is still alive.”

The answer to the question Choi Minwoo had been about to ask slipped from Song Cheonwoo’s lips. Gathering his confused thoughts, Choi Minwoo asked,

“What is your basis for thinking that?”

“If he had died, Lee Jungryong would never have kept me alive until now.”

“……!”

“But I do not know exactly where he is being kept. For now, I merely suspect Area A.”

“Area A…”

Choi Minwoo muttered the words under his breath and suddenly raised his head.

His gaze settled on Song Cheonwoo’s back as the old man stood before the crevasse, gazing down endlessly into the enormous crack.

“There are a few more things I want to ask.”

“Ask whatever you wish.”

Choi Minwoo silently studied his back before abruptly speaking.

“I want to know why.”

“……Why?”

“Yes. Why are you telling me everything now? We are cooperating for the moment, but in the not-too-distant future, I will become another rival of yours. Why tell me something this important?”

The enemy of my enemy is my ally.

That was the relationship between Choi Minwoo and Song Cheonwoo.

They had joined hands temporarily to bring down Go Jun and make Ares Guild their own. Nothing more and nothing less.

That was why Choi Minwoo understood Song Cheonwoo’s attitude even less.

*He has suddenly changed.*

They had met in secret only a week ago.

Back then, Song Cheonwoo had been cautious, and a faint wariness had shown through his words and actions.

As someone who had once stood as Lee Jungryong’s political rival, he knew that this temporary alliance would fall apart as soon as it successfully achieved its purpose.

*Then why?*

Information about Cheon Taemin’s whereabouts was a secret within a secret. Considering the confrontation that would come later, it was also a powerful weapon that could force Choi Minwoo to withdraw.

It was not something he could reveal openly on a whim, swept away by a momentary emotion.

*Swish.*

Just as Choi Minwoo’s fingertips touched his sword hilt, Song Cheonwoo, who had been silently staring down into the distant void, slowly turned around.

“The reason…”

The old man’s voice was calm and composed.

The hesitation and faint tremor that had colored his voice when they first met outside the Gate were gone.

The moment Choi Minwoo felt Song Cheonwoo’s gaze settle on his hand, the old man continued in a quiet voice.

“Let us call it atonement.”

Choi Minwoo tightened his grip on the sword and asked,

“Atonement for what?”

“I wanted to tell you someday, even if it was late. About the wrongs I committed against him—and against you.”

“You are more than twenty years too late.”

“Yes, I am late. But it could not be helped.”

“An excuse.”

Choi Minwoo answered firmly.

That was when—

*Rumble, rumble, rumble!*

The snow-covered mountain trembled beneath its blanket of white. An avalanche was taking place beyond the crevasse, which stretched dozens of meters across.

Even now, fur-covered giants stood atop the violently surging waves of snow.

—Kraaaaaaaaaar!

—Kauu!

Feral roars reverberated through the mountain.

At the sight of hundreds of yetis charging toward them, Choi Minwoo suddenly muttered,

“That is strange.”

“What is?”

“Yetis usually live in groups of around a dozen.”

“Yes. They used to.”

*Crunch. Shing.*

Song Cheonwoo, his back to the crevasse, stepped forward. The sword hanging from Choi Minwoo’s waist slid free of its sheath.

It was a sword left behind by a hero who had fulfilled his duty even in death.

“That is a fine sword.”

Song Cheonwoo muttered the words under his breath and took another step.

Over Choi Minwoo’s shoulder, someone was already launching himself forward.

“Young Master!”

As he heard the old loyal servant’s shout, Song Cheonwoo muttered,

“Understand. It could not be helped.”

And then—

*BOOM!*

A thunderous explosion erupted, and a blizzard came whirling toward them.
```

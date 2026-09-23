<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0738.txt",
      "sha256": "eb328e2b8ca1ccaf0576c47bfa65dc6c2f13547312ad7d9910ae2249e2efdda1",
      "bytes": 11918
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "043476abff490cfbe5898a34b493893d64c675b0e7f5b0f7abeb9a0fe3781d71",
      "bytes": 2355
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "99d3841f1c09c0bb4a871f04e2889051053cfd2ab04f960c03e22c52e7535e83",
      "bytes": 212637
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "f857ebccacb0fdf1909d4c7fe047b88da4865005c3b64838502f0dd48f42ecc0",
      "bytes": 553
    },
    {
      "path": "characters/Human Butcher.md",
      "sha256": "1ac77e1347f5ad6bbd84e3287e682b7fcdf45f655b3ab43d11d209dca5323d8e",
      "bytes": 667
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "3aacf9e8d4173f799ff8929f7edc70d7d1bd50a3bc612abf9cfd6df793d48290",
      "bytes": 2011
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "109e6402825a59c0a872f7e44a99ebd4e4c62b5a8f1411f47d336400ab4a05bf",
      "bytes": 622
    },
    {
      "path": "characters/Michael.md",
      "sha256": "12ced14e9019e20670d6d994bb8987d3850e23c347158bc555cab9f6eeb68537",
      "bytes": 754
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "fc30c90edfddef79c04e28a4d0f6e22dcca49b2245fa59567be43490bef68055",
      "bytes": 226197
    }
  ],
  "estimated_tokens": 9247
}
-->

# Durable State Update — Chapter 738

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 738. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 738. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history.
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
  "chapter": 738,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 738,
    "continuity_sources": [738],
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
    "A Monster Wave destroyed Ares Guild's Paris branch, causing approximately three hundred casualties; forty-five survivors were rescued.",
    "Michael Silbert engineered the Paris disaster through a deal with insane Middle Eastern fanatics who wanted weapons for revenge.",
    "Michael and Huginn prepared a media operation to portray Odin Guild as Paris's protector and conceal its role in the disaster.",
    "Ten fanatic Hunters were brought from the desert to carry out coordinated terrorist attacks; after the London attack, eight attacks remain.",
    "Michael is stronger than any S-rank Hunter Jin has previously faced and uses political consequences and hidden threats as weapons.",
    "Jin, Team Leader Choi, and the Skeleton King know Michael is responsible but lack evidence sufficient to expose him publicly.",
    "Jin refrained from attacking Michael after Choi and the Skeleton King restrained him, recognizing that the resulting political fallout could endanger Ares Guild and the Skeleton King's identity.",
    "The forced Quest Chain of Terror Attacks is active and cannot be refused.",
    "Cheon Taemin remains unconscious, leaving Ares Guild vulnerable to consequences arising from the Paris disaster.",
    "Idle Bystander continues to reduce Jin's abilities by ten percent during its thirty-day duration."
  ],
  "continuity_sources": [
    737
  ],
  "open_questions": [
    "What is the source and reach of Michael's unusually reliable intelligence, including his knowledge of the Pentagon's operations?",
    "What were the gifts delivered by Huginn, and what purpose did they serve?",
    "How did Odin Guild obtain or prepare its Mana Cultivation Method?",
    "Why is Michael so certain that Cheon Taemin will not intervene?",
    "What are the targets and methods of the eight remaining terrorist attacks?"
  ],
  "safe_through": 737,
  "temporary_decisions": [
    "Render 최 팀장 as Team Leader Choi and 미카엘 실베르트 as Michael Silbert.",
    "Render 샤오 양 주석 as Chairman Xiao Yang; 메이산 as Meishan, 쯔양 as Ziyang, and 쑤이닝 as Suining.",
    "Render 수수방관 as Idle Bystander.",
    "Render 차도살인지계 as \"the stratagem of borrowing another's knife to kill.\"",
    "Render 연쇄 테러 as Chain of Terror Attacks."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 대주     | **Squad Leader** / **Commander**             |
| 일격     | **One Strike**                         |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 길드      | **Guild**             |
| 길드장     | **Guild Master**      |
| 팀장      | **Team Leader**       |
| 대격변     | **Great Cataclysm**   |
| 공자      | **Young Master**                                                |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 미카엘 | **Michael** | Guild Master of Odin Guild. |
| 아레스 | **Ares Guild** | The leading Guild in Korea; formerly employed Team Leader Choi and Song Song. |
| 그리스 | **Grease** | Spell used to make the ogres lose their footing. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 신성 | **Morning Star** | Term in the summons referring to the Master of Morning Star. |
| 존슨 | **Johnson** | Co-host of the American talk show that replays Taekyung's viral interview. |
| 영국 | **United Kingdom** | Country associated with BCC. |
| 중국 | **China** | Country from which Team Leader Choi’s video originates. |
| 오대 | **Five Squads** | Named Tang Clan organizational group in Tang Sadok's mobilization order. |
| 중화 | **Zhonghua** | Patriotic term used in Shao Shen’s rallying speech. |
| 화기 | **fire qi** | The fire nature imparted to internal energy by the Fire Gate Divine Technique. |
| 모스크바 | **Moscow** | Russian city used in Taekyung's modern-world comparison. |
| 마비 | **Paralyzed** | Status abnormality inflicted by Kraken's Ink. |
| 알라 | **Allah** | Deity invoked by the Middle Eastern terrorist groups' rhetoric. |
| 중동 | **Middle East** | Region associated with the terrorist group and reported experiments. |
| 필립 | **Philip** | U.S. military or political official introduced by first name only. |
| 오딘 | **Odin** | The name of the world's greatest Guild, invoking the Norse god. |
| 파리 | **Paris** | The city containing Ares Guild's branch attacked at the chapter's end. |
| 런던 | **London** | City targeted in the next terrorist attack. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 진태경 | 존슨 | Allied Hunter to Grand Mage | Johnson | polite and familiar | Jin repeatedly addresses Magic Johnson directly while requesting explanations and permission to visit the site. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 736
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Human Butcher.md

# Human Butcher (인도)

- **Safe through:** Chapter 699
- **Aliases:** None
- **Role:** Former mysterious Han Chinese mounted-bandit power in Northern Gaoyuan commanding fifty subordinates; a Peak master killed by an unnamed old man in a single move
- **Personality:** Cold, intimidating, and murderous; he kills people as though slaughtering livestock
- **Voice:** Cold, curt, and quietly threatening
- **Relationships:** He is one of four powerful participants at the Northern Gaoyuan gathering, intimidates Temur, and has claimed Ghost Sword Wipeng as his personal target in the proposed attack

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 737
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple, the Fire Gate Clan's nineteenth successor, and the Pavilion Master of the Fire Dragon Pavilion within the Murim Alliance, a Supreme Peak master with the Heavenly Martial Physique and Force, a publicly recognized S-rank-level Hunter who formally retains an A-rank license, a traveler between Murim and another world resembling the realm of immortals, and the creator of the beginner-accessible Smiling Mana Cultivation Method.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate, trusted manager of media and official arrangements, and now the Peace Guild's Guild Master, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 737
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Michael.md

# Michael (미카엘)

- **Safe through:** Chapter 737
- **Aliases:** None
- **Role:** Michael is the Guild Master of Odin Guild, one of the world's most powerful absolute authorities, and the hidden architect of a coordinated chain of terrorist attacks using recruited fanatic Hunters.
- **Personality:** Controlled, calculating, condescending, and confident in his intelligence and ability to manipulate events.
- **Voice:** Polite and conversational when relaxed, but quietly authoritative and coercive when asserting control.
- **Relationships:** Michael personally selected and trained Huginn, commands Odin Guild's hidden alliance, and regards Jin Taekyung as a serious adversary.

## Korean source

```text
＃738화



새해라는 단어에는 묘한 마력이 있다.

또 다른 일 년을 시작한다는 설렘. 모든 것이 작년보다는 나아질 것이라는 막연한 기대감.

그러나 새로운 달력의 첫 장을 넘기기도 전인 1월의 어느 날, 사람들이 품었던 설렘과 기대감은 한순간에 무너져 내렸다.

- 긴급 속보입니다. 지금으로부터 불과 한 시간 전 전해 드렸던 파리의 소식에 이어, 영국 런던에서 두 번째 몬스터 웨이브가 발생했습니다. 현재 런던 도심지는 극심한 혼란에 휩싸여 있으며, 영국 국왕 필립 2세는…….

- 또 다른 긴급 속보입니다! 인도 뭄바이에서 다시 한번 몬스터 웨이브가 발생했습니다! 이는 단 하루 사이 발생한 세 번째 몬스터 웨이브로, 대격변 이후 전례가 없던…….

- 맙소사. 모두 보고 계십니까? 리우데자네이루의 상징이, 구세주 그리스도(Cristo Redentor)가 무너지고 있습니다!

그것은 재앙의 시작이었다.

가장 먼저 프랑스의 뤽상부르크 공원이 피로 물들었고, 유서 깊은 역사를 간직한 런던 브리지가 무너졌으며, 600톤이 넘는 브라질의 거대 예수상이 건물과 인간을 덮치며 쓰러졌다.

구구구궁!

굉음과 함께 지면이 흔들렸다.

겨우 몸을 가누고 있던 사람들을 기다리고 있던 것은, 폭발과 함께 솟구친 화염 너머로 들려오는 무언가의 울음소리였다.

- 크르르르…….

몬스터 웨이브(Monster Wave).

재앙과 동일어가 되어 버린 그 명칭대로, 공간을 찢고 나타난 몬스터 군단은 파도가 되어 사방을 휩쓸었다.

- 크워어어어!

“모, 몬스터다!”

“피해!”

“꺄아아악!”

눈부신 문명으로 세워 올린 빌딩 숲이 비명에 잠겼다.

누군가는 도망쳤고, 누군가는 몬스터에게 붙잡혀 갈기갈기 찢겨 죽었으며, 또 다른 누군가는 빛나는 무기를 들고 이 세상의 것이 아닌 괴물들과 맞서 싸웠다.

“포메이션! 물러서지 마라!”

“원거리 부대, 발사!”

쿠구궁. 콰아아앙!

인간과 몬스터. 몬스터와 인간.

처음부터 양립할 수 없는 두 종족은 서로를 향해 달려들었고, 프랑스 파리에서 시작된 불길은 전 세계 곳곳으로 옮겨붙었다.



[모스크바의 붉은 광장, 몬스터에 의해 피로 물들다]

[다시 한번 중국에 들이닥친 재앙, 화염에 휩싸인 자금성]

[하루 만에 일어난 다섯 번의 몬스터 웨이브. 소식을 접한 교황 우르바노 8세, “오, 신이시여.”]

[여섯 번째 몬스터 웨이브 발생지는 뉴욕. 충격에 휩싸인 월 스트리트.]

[비행 몬스터에 의해 점령된 도쿄 타워. 추락한 항공자위대가 불러온 2차 피해.]

[첫 번째 몬스터 웨이브를 신속히 진압한 오딘 길드장 미카엘 실베르트, 파리에서 입수한 CCTV 공개 “이것은 단순한 재앙이 아니라, 목적이 있는 테러가 확실하다”]



최소 수백만, 혹은 천만이 넘는 인구가 거주하는 대도시들이 혼란에 휩싸였다.

쉴 새 없이 이어지는 충격적인 뉴스들을 TV와 스마트폰으로 지켜보던 사람들은 할 말을 잃었다.

재앙(災殃).

지금 벌어지는 이 모든 상황을 설명할 수 있는 유일한 단어.

그와 동시에 전염병처럼 번진 공포는 사람들의 이성을 마비시켰다.

“여보세요? 뉴스 봤지? 지금 당장 학교로 데리러 갈 테니까…….”

“아니, 자네 지금 뭐 해?”

“보면 모르십니까. 짐 챙기죠.”

“이 사람이, 아직 퇴근하려면 한참 남았는데 그게 무슨 소리야?”

“씨발, 지금 그게 중요합니까? 전 일단 가족부터 챙기고 봐야겠습니다.”

“야, 야! 김 과장!”

몬스터 웨이브는 아무도 예측할 수 없는 자연재해와 같았고, 사람들은 하던 일을 내려놓고 혼이 나간 것처럼 움직였다.

가족들이 기다리고 있을 집으로. 혹은 생존 가능성이 조금이라도 높을 비상 대피소로.

텅텅 빈 사무실을 증명하듯 대부분의 업무와 도로는 마비되었고, 지하철에 모여든 사람들은 스마트폰을 손에서 놓지 못했다.

지금 그들을 짓누르고 있는 것은 보이지 않은 극심한 공포와 불안감이었다.

당장 이곳에서 몬스터 웨이브가 발생할지도 모른다는 공포. 그로 인하여 자신이나 소중한 사람이 목숨을 잃을 수도 있다는 불안감.

위이이이잉.

- 임시 비상사태. 임시 비상사태입니다. 인근에 거주하고 계신 주민들께서는 만일의 사태를 대비하여 비상 대피소로…….

전 세계 각국에서 동시다발적으로 선포된 비상사태.

거리에는 쉴 새 없이 경보음이 울려 퍼졌고, 각종 중화기로 무장한 군대와 긴급 소집된 헌터들은 긴장한 얼굴로 정부의 지시를 기다렸다.

머리 위에 뜬 태양, 혹은 달이 각 나라의 시차에 맞춰 자취를 감출 때까지.

긴 기다림 끝에 정부의 새로운 발표가 나오기 전까지.

- 임시 비상사태를 해제합니다.

이는 프랑스 파리에서 첫 몬스터 웨이브가 발생한 지 24시간 만이었고, 이 세상이 종말하는 그날까지 이어질 것 같던 그날의 재앙은 이집트 카이로를 끝으로 막을 내렸다.

단 하루 만에 10번의 몬스터 웨이브라는, 전례 없는 끔찍한 기록을 남기며.

그리고 그중 다섯 번의 몬스터 웨이브를 성공적으로 막아 낸 영웅이 수많은 카메라 앞으로 나섰다.

“앞으로도 우리 오딘 길드는, 여러분의 검과 방패가 되어 본분을 다할 것입니다.”

미카엘 실베르트.

희생된 이들의 넋을 기리며 뜨거운 눈물을 흘리는 그의 모습에 사람들은 함께 울었다.

수많은 사람을 구한 영웅과 오딘 길드를 향해 모두가 환호했다.

아니, 정확히 모두는 아니었다.



* * *



쾅!

굉음과 함께 십여 개의 홀로그램 TV가 먼지처럼 바스러졌다.

조금 전만 하더라도 한 사람의 얼굴이 떠올라 있던 허공을 응시하던 나는, 문득 입을 열었다.

“사과해야 하나요?”

가까운 소파에 앉아 있던 최 팀장이 고개를 저었다.

“괜찮습니다. 어차피 진태경 씨가 나서지 않았다면 제 손으로 부쉈을 테니까요.”

저건 결코 과장이나 빈말이 아니다.

나는 한껏 움켜쥔 최 팀장의 주먹을 바라보았다. 새하얗게 물든 그의 주먹에서는 핏방울이 점점이 떨어지고 있었다.

미처 닦아 내지 못한 몬스터의 녹색 핏물과 함께.

툭. 투둑.

새하얀 양털 카펫이 붉고 푸르게 물들어 가고 있었지만, 방 안의 누구도 신경 쓰지 않았다.

그저…… 주위를 둘러싼 모든 것이 차갑고 공허하게만 느껴졌다.

‘당했다. 그것도 완벽하게.’

열 번.

자그마치 열 번의 몬스터 웨이브 중 단 한 번도 막지 못했다. 아니, 어쩌면 막을 수 없었다는 표현이 정확할 것이다.

‘처음부터 계획되어 있었으니까.’

적어도 수천, 혹은 수만 킬로미터씩 떨어진 대도시에서 발생한 몬스터 웨이브를 막는 것은 불가능했다.

설령 매직 존슨과 함께였다 해도 상황은 달라지지 않았을 것이다.

오늘 발생한 몬스터 웨이브는 처음부터 끝까지 계획된 테러였고, 시간과 장소를 가리지 않고 터진 폭탄이었으니.

그리고 뒤늦게 소식을 듣고 도착한 우리를 기다리고 있던 것은 또 다른 폐허와 시신들이었다.

다만 파리에서의 몬스터 웨이브와 약간의 차이가 있다면, 이후 몬스터 웨이브가 발생한 곳의 위치였다.

‘놈들이 노렸던 건, 아레스 길드의 해외 지부가 아니었어.’

미카엘 실베르트와 손을 잡은 테러범들이 향한 곳은 다양했다. 수많은 인파로 붐비는 관광 명소, 이름만 대면 알 만한 대기업의 본사 등.

그러나 그중에서도 가장 많은 표적이 되었던 것은, 다름 아닌 아레스와 같은 거대 길드의 지부였다.

“도대체 왜?”

불쑥 내뱉은 한 마디에 고개를 든 최 팀장을 향해, 나는 한 단어를 덧붙였다.

“표적.”

설명은 그것으로 충분했다. 공허한 눈빛으로 허공을 바라보던 최 팀장이 문득 입을 열었다.

“고립입니다.”

“고립?”

“네. 아레스 길드를 고립시키는 것. 그것이 미카엘 실베르트의 노림수겠죠.”

“하지만 어째서 파리 지부처럼…….”

말을 이으려던 나는 멈칫했다.

실타래처럼 꼬인 머릿속을 빠르게 오가는 여러 생각들. 그 어딘가에, 미처 보지 못했던 답이 있었다.

‘중동 테러 단체.’

미카엘 실베르트와 손잡은 놈들의 임무는 아직 끝나지 않았다.

이 끔찍한 하루를 마무리 지을 마지막 일격이, 아레스 길드를 전 세계에서 고립시킬 시퍼런 칼날이 우리를 향해 짓쳐 들고 있었다.

어쩌면 지금 이 순간에도.



* * *



저벅. 저벅.

어둠 속에서 울려 퍼지는 발걸음 소리는 유난히도 크게 울려 퍼졌다.

그것이 수십여 명이나 되는 머릿수 때문인지, 아니면 그들이 가로지르는 그 공간이 어두컴컴한 동굴이라 그런 것인지는 알 수 없었지만 한 가지는 확실했다.

이곳은 아무도 모르고, 누구도 찾아올 수 없는 장소였다.

저벅.

끝없이 앞으로 나아갈 것 같던 발걸음이 동시에 멈췄다.

칠흑 같은 어둠 속에서 무언가가 일렁였다.

“인샬라.”

귓가에 대고 속삭이는 듯이 들려온 한마디에, 수십여 명의 사람들은 무릎을 꿇고 엎드렸다.

그리고 동시에 입을 열어 답했다.

“인샬라.”

신의 뜻대로.

그것은 그들을 하나로 묶는 주문이자 신의 위대함을 되새기는 기도였고, 어둠 너머에서 일렁이던 인영(人影)은 비로소 모습을 드러냈다.

슥.

긴 로브가 땅을 스쳤다. 사람들은 더욱 깊숙이 머리를 숙이며 한 목소리로 중얼거렸다.

“미천한 알라의 종이, 위대하신 선지자를 뵙나이다.”

선지자(先知者).

감히 얼굴조차 제대로 마주할 수 없는 존재를 칭하는 그 세 글자는, 그들에게 있어 신성불가침의 영역에 있었다.

“고개를 들라.”

성별도, 나이도 구분할 수 없는 신비로운 목소리에 사람들은 몸을 부르르 떨었다.

그리고 땅에 얼굴을 박으며 대답했다.

“이 미천한 종복들이 어찌 감히 위대하신 선지자를 마주하겠습니까.”

“명령을 거두어 주십시오.”

화악.

어디선가 불어온 한 줄기의 바람이 그들을 감싸 안았다.

뒤이어 바람에 섞인 선지자의 목소리가 귓가로 전해졌다.

“그들은 어찌 되었느냐.”

선지자가 말하는 ‘그들’이 누구를 뜻하는지 모르는 사람은 아무도 없다.

그들 중 가장 앞에 엎드려 있던 노인이 입을 열었다.

“맡은 바 임무를 끝마치고 신의 품으로 돌아갔나이다.”

선지자가 가볍게 고개를 끄덕였다.

“인샬라. 마땅히 그리 되었을 것이다.”

“인샬라.”

사막을 넘어 오대양 육대주로 흩어진 열 명의 전사들. 그들은 신의 전사로서 임무를 완수했고, 신의 품으로 돌아갔다.

그리고 이제는 핏값을 돌려받아야 할 때. 선지자는 신비로운 목소리로 입을 열었다.

“온 세상에 알려라. 이 모든 재앙이 무엇으로 비롯되었는지.”
```

## Final English reading copy

```markdown
# Chapter 738

There was a strange magic in the words *New Year*.

The excitement of beginning another year. The vague hope that everything would be better than it had been the year before.

But one day in January, before people had even turned the first page of their new calendars, that excitement and hope collapsed in an instant.

—This is an emergency news bulletin. Following the news from Paris that we reported only an hour ago, a second Monster Wave has occurred in London, United Kingdom. Central London is currently engulfed in extreme chaos, and King Philip II of the United Kingdom is…

—Another emergency bulletin! A Monster Wave has occurred once again in Mumbai, India! This is the third Monster Wave to occur in a single day, an unprecedented event since the Great Cataclysm…

—Oh my God. Are you all seeing this? The symbol of Rio de Janeiro, the Christ the Redeemer statue—Cristo Redentor—is collapsing!

It was the beginning of a catastrophe.

First, France’s Luxembourg Gardens were stained with blood. Then London Bridge, which had stood through a long and storied history, collapsed. And Brazil’s colossal statue of Jesus, weighing over six hundred tons, toppled over, crushing buildings and people beneath it.

*Rumble, rumble, rumble!*

The ground shook with a deafening roar.

Those barely managing to keep their balance were met by the sound of something crying out beyond the flames that erupted with the explosion.

—Grrr…

Monster Waves.

True to the name that had become synonymous with disaster, legions of monsters tore through space and appeared, sweeping in every direction like a wave.

—Kraaaargh!

“M-Monsters!”

“Run!”

“Aaaah!”

The forest of skyscrapers built by dazzling civilization filled with screams.

Some people fled. Some were seized by monsters, torn apart, and killed. Others raised shining weapons and fought against creatures that did not belong to this world.

“Formation! Don’t retreat!”

“Ranged units, fire!”

*Boom! Boom! KABOOM!*

Humans and monsters. Monsters and humans.

The two species, incapable of coexisting from the very beginning, charged at one another. And the flames that had begun in Paris, France, spread to every corner of the world.



[Red Square in Moscow stained with blood by monsters]

[Disaster strikes China once again—the Forbidden City engulfed in flames]

[Five Monster Waves in a single day. Upon hearing the news, Pope Urban VIII says, “O God.”]

[The sixth Monster Wave occurs in New York. Wall Street plunged into shock.]

[Tokyo Tower seized by flying monsters. Crashed Air Self-Defense Force aircraft cause secondary damage.]

[Odin Guild Master Michael Silbert rapidly suppresses the first Monster Wave. Releases CCTV footage obtained in Paris: “This is not a simple disaster. It is undoubtedly a terrorist attack with a purpose.”]



Metropolises inhabited by at least several million—or even more than ten million—people were thrown into chaos.

People watching the shocking news reports one after another on their televisions and smartphones were left speechless.

*Disaster.*

It was the only word that could explain everything happening now.

At the same time, the fear spreading like a plague paralyzed people’s reason.

“Hello? You saw the news, right? I’m going to pick you up at school right now, so…”

“Hey, what are you doing?”

“What does it look like? I’m packing.”

“You idiot, there’s still a long time before you get off work. What are you talking about?”

“Fuck, is that what matters right now? I need to take care of my family first.”

“Hey, hey! Section Chief Kim!”

Monster Waves were like natural disasters that no one could predict, and people abandoned whatever they were doing and moved about like they had lost their souls.

Toward the homes where their families were waiting. Or toward emergency shelters where their chances of survival might be even slightly higher.

As if to attest to the empty offices, most work and road traffic had ground to a halt, and the people crowding into the subways could not bring themselves to put down their smartphones.

What weighed them down now was an extreme fear and anxiety they could not see.

The fear that a Monster Wave might occur right there at any moment. The anxiety that they—or someone precious to them—might lose their life because of it.

*Wheeeeeeeen.*

—Temporary state of emergency. This is a temporary state of emergency. Residents living nearby are advised to prepare for any eventuality and proceed to an emergency shelter…

States of emergency were declared simultaneously in countries around the world.

Warning sirens rang through the streets without pause, while soldiers armed with all kinds of heavy weapons and Hunters summoned in an emergency waited for instructions from their governments, tense-faced.

Until the sun—or moon—hanging overhead disappeared according to each country’s time zone.

Until, after a long wait, the governments issued new announcements.

—The temporary state of emergency is hereby lifted.

It had been only twenty-four hours since the first Monster Wave occurred in Paris, France. The disaster of that day, which had seemed as though it might continue until the world ended, finally came to a close with Cairo, Egypt.

Leaving behind the unprecedented and horrifying record of ten Monster Waves in a single day.

And the hero who had successfully stopped five of those Monster Waves stepped before countless cameras.

“From this day forward, Odin Guild will continue to fulfill its duty by becoming your sword and shield.”

Michael Silbert.

As people watched him shed hot tears while mourning the souls of the fallen, they cried along with him.

Everyone cheered for the hero who had saved countless people, and for Odin Guild.

No—not everyone.



* * *



*Bang!*

With a deafening roar, more than a dozen holographic televisions crumbled into dust.

I stared at the empty air where a man’s face had appeared only moments ago. Then I suddenly opened my mouth.

“Should I apologize?”

Team Leader Choi, sitting on the nearest sofa, shook his head.

“It’s fine. If you hadn’t stepped in, I would have smashed them myself.”

That was no exaggeration or empty courtesy.

I looked at Team Leader Choi’s tightly clenched fist. Blood was slowly dripping from his whitened knuckles.

Along with the green monster blood he had not yet managed to wipe away.

*Drip. Drip.*

The white wool carpet was gradually becoming stained red and green, but no one in the room cared.

Everything around us simply felt cold and empty.

*We got played. And perfectly.*

Ten.

Out of ten Monster Waves—ten of them—we had failed to stop even one. No, perhaps it would be more accurate to say that we had been unable to stop them.

*Because they had been planned from the start.*

It was impossible to stop Monster Waves occurring in major cities thousands, or even tens of thousands, of kilometers apart.

The situation would not have changed even if Magic Johnson had been with us.

The Monster Waves that occurred today had been planned terrorist attacks from beginning to end—bombs detonating without regard for either time or place.

And when we finally heard the news and arrived, what awaited us were more ruins and corpses.

There was only one slight difference between the Monster Wave in Paris and the ones that followed: the locations where the later Monster Waves occurred.

*Their targets weren’t Ares Guild’s overseas branches.*

The terrorists who had joined hands with Michael Silbert had headed for all kinds of places. Tourist attractions crowded with people. The headquarters of major corporations recognizable by name alone.

But the most frequently targeted sites of all had been the branches of major Guilds like Ares.

“Why?”

At my abrupt question, Team Leader Choi raised his head. I added one word.

“Targets.”

That was explanation enough.

Team Leader Choi stared into empty space with hollow eyes, then suddenly opened his mouth.

“Isolation.”

“Isolation?”

“Yes. Isolating Ares Guild. That must be Michael Silbert’s objective.”

“But why do it like the Paris branch…?”

I stopped before I could finish.

Various thoughts raced through my tangled mind like threads being unwound. Somewhere among them was an answer I had failed to see.

*A Middle Eastern terrorist organization.*

The mission of the men who had joined hands with Michael Silbert was not over yet.

The final strike that would bring this horrific day to a close—the keen, ice-cold blade that would isolate Ares Guild from the entire world—was rushing toward us.

Perhaps even now.



* * *



*Step. Step.*

The sound of footsteps echoing through the darkness was unusually loud.

I could not tell whether it was because there were several dozen people, or because the space they were crossing was a dark cave. But one thing was certain.

This was a place no one knew about and no one could reach.

*Step.*

The footsteps that had seemed destined to continue forever came to a simultaneous halt.

Something rippled in the pitch-black darkness.

“Inshallah.”

At the single word that sounded as though it had been whispered directly into their ears, several dozen people dropped to their knees and prostrated themselves.

Then they opened their mouths and answered in unison.

“Inshallah.”

God willing.

It was an incantation that bound them together and a prayer that reminded them of God’s greatness. And the silhouette wavering beyond the darkness finally revealed itself.

*Swish.*

A long robe brushed against the ground.

The people bowed their heads even lower and murmured with one voice.

“This lowly servant of Allah humbly greets the great Prophet.”

*The Prophet.*

That title, used for a being whose face they did not even dare properly meet, occupied a sacred and inviolable place among them.

“Raise your heads.”

At the mysterious voice whose gender and age could not be discerned, the people trembled.

Then, pressing their faces into the ground, they answered.

“How could these lowly servants dare to face the great Prophet?”

“Please withdraw your command.”

*Whoosh.*

A single gust of wind blew in from somewhere and enveloped them.

Then the Prophet’s voice, mingled with the wind, reached their ears.

“What became of them?”

No one had any doubt whom the Prophet meant by *them*.

The old man prostrated at the very front opened his mouth.

“They completed the missions entrusted to them and returned to the embrace of God.”

The Prophet gave a slight nod.

“Inshallah. It was only right that they should.”

“Inshallah.”

Ten warriors had crossed the desert and scattered across the five oceans and six continents. As warriors of God, they had completed their missions and returned to the embrace of God.

And now it was time to collect the blood price.

The Prophet spoke in a mysterious voice.

“Let the whole world know what brought about all this disaster.”
```

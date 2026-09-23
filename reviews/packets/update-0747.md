<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0747.txt",
      "sha256": "93da62c78618d934b7bcf0b5d321e2e0b7747e8a4ab081982a751fc06800fdeb",
      "bytes": 13014
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "f48c59e2b08cadf41bb6fec157fba2487fc3ae0cae3f4515c14844fe0ee1edd5",
      "bytes": 2485
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "64f553c31c5e261211eb4ac850967ef5f11af09dc7388c8cd9d817de5270c193",
      "bytes": 215679
    },
    {
      "path": "characters/Baek Hanseong.md",
      "sha256": "c6d68d6a20ce08d428d1aa38ecdacc0770b6171e6103f1d1e8fe4764836a9cc2",
      "bytes": 861
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "76411218a443dc53e30f2abea6e753160e2968ed3890aa3cfb5e636c21792e8d",
      "bytes": 553
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "fd1f8ffde30c11c9b0461b5007fe758f3c9383733f81c5bf4ac75a037530cdd9",
      "bytes": 2011
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "9a769a21aa016798fbedbb8c9c5bdbbb2dd90a9705d47c8f7409e66f9edc48bc",
      "bytes": 622
    },
    {
      "path": "characters/The Prophet.md",
      "sha256": "e40831a22f541b41b32442bf4c817afdc462554f7ca1ffb0f4a69ecf19ffb9b3",
      "bytes": 644
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "20c3f46b71b5baf33904439e4807b7c5b429d84d83db8e2ae3027d09893d4a3a",
      "bytes": 228924
    }
  ],
  "estimated_tokens": 10036
}
-->

# Durable State Update — Chapter 747

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 747. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 747. Profile updates may replace only one
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
  "chapter": 747,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 747,
    "continuity_sources": [747],
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
    "The Prophet commands the revived Hasasin and is preparing another judgment after the earlier attacks called Allah's Judgment.",
    "The Prophet can create a transparent concealment barrier that cannot be detected by science or Magic.",
    "The Prophet possesses at least ten unrefined S-rank Magic Gems that retain their original power.",
    "The retired Grand Mage Siegfried Wassmann was found dead in his sealed hideout after his life force was apparently drained by unknown magic.",
    "Michael Silbert remains the strongest suspect in Siegfried's death and possesses unexplained overwhelming power after a painful transformation.",
    "Jin has accepted the Supreme Peak Quest Unknown Death, whose mission is to discover the truth behind Siegfried's death.",
    "Mana levels and magical power continue rising, with mutation Gates now occurring several times daily.",
    "Michael and Huginn continue manipulating media coverage to undermine Jin's public support and damage Ares Guild.",
    "Magic Johnson is investigating stolen research materials from Siegfried's laboratory but has not yet produced results.",
    "Huginn has completed an undisclosed operation whose consequences remain pending.",
    "An enormous ancient monster has awakened in the deep sea, a colossal tsunami is approaching Tokyo, and Tokyo Bay has now collapsed.",
    "The Prophet's identity, age, and gender remain unknown, while Al-Nizar is established as the loyal S-rank Hunter leading the Hasasin."
  ],
  "continuity_sources": [
    746
  ],
  "open_questions": [
    "Who killed Siegfried Wassmann, by what magic, and why?",
    "How did Michael Silbert learn about A Area and Cheon Taemin's condition, and did he order Siegfried's death?",
    "What role do The Prophet, the revived Hasasin, and their planned judgment play in the terrorist campaign and Siegfried's death?",
    "What is Huginn's undisclosed operation, and can its consequences actually bring Jin down?",
    "What is the identity and purpose of the ancient monster, and how are it, the approaching tsunami, and Tokyo Bay's collapse connected?"
  ],
  "safe_through": 746,
  "temporary_decisions": [
    "Render 선지자 as The Prophet.",
    "Render 스켈레톤 킹 as Skeleton King.",
    "Render A구역 as A Area.",
    "Render 마력 as magical power, distinct from mana.",
    "Render 지크프리트 바스만 as Siegfried Wassmann and 실베르트 as Silbert."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 살기     | **killing intent**                               |                                                       |
| 상태               | **Status**                     |
| 장비               | **Equipment**                  |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 길드      | **Guild**             |
| 팀장      | **Team Leader**       |
| 대격변     | **Great Cataclysm**   |
| 도사      | **Daoist**                                                      |
| 백한성 | **Baek Hanseong** | Twenty-seventh President of Korea and youngest president elected in Korean history. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 선지자 | **The Prophet** | Mysterious religious leader directing the terrorist warriors. |
| 아스모데우스 | **Asmodeus** | Demon King referenced in Taekyung's sarcastic comparison; does not appear directly. |
| 평화 | **Peace Guild** | Guild name. |
| 아레스 | **Ares Guild** | The leading Guild in Korea; formerly employed Team Leader Choi and Song Song. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 마왕 | **Demon King** | The being Cheon Taemin killed. |
| 미국 | **United States** | Country associated with the talk show and CNM. |
| 중국 | **China** | Country from which Team Leader Choi’s video originates. |
| 대통령 | **President** | Title for Korea's head of state. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 텔레포트 | **Teleport** | Taekyung's label for the Blood Lord's unexplained disappearance. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 장성 | **Great Wall** | Wall used in the discussion of the Outer Lands. |
| 외교부 | **Ministry of Foreign Affairs** | Korean government ministry angered by the Chinese branch director's damage to cultural relics. |
| 신인 | **divine man** | Descriptive term for a human who became something beyond humanity. |
| 재생 | **Regeneration** | The masked man's rapid recovery from shattered bones and severe wounds. |
| 마력 | **magical power** | Distinct from mana; the Skeleton King's area of expertise. |
| 도쿄 | **Tokyo** | City visible behind Huginn's departing ship. |
| 심해 | **deep sea** | Unexplored ocean depths where the ancient monster awakens. |
| 도쿄만 | **Tokyo Bay** | Port area where Sugihara Gyoiku works. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 진태경 | 대통령 | Hunter_to_President | Mr. President | formal-polite | Taekyung addresses the President respectfully during their airport greeting. |
| 대통령 | 진태경 | President_to_Hunter | Mr. Jin Taekyung | formal-polite | The President addresses Taekyung by name at the airport photo line. |

## Listed compact profiles

### Baek Hanseong.md

# Baek Hanseong (백한성)

- **Safe through:** Chapter 733
- **Aliases:** None
- **Role:** Twenty-seventh President of Korea and the youngest president elected in Korean history who leads the government's public response to the Mutated Gate crisis, supports Jin Taekyung in public appearances, and publicly backs the national project to release Cheon Taemin's Mana Cultivation Method.
- **Personality:** Confident, politically shrewd, composed, and willing to needle Lee Jungryong while advancing his anti-Ares stance.
- **Voice:** Polite, self-assured, calm, and lightly teasing.
- **Relationships:** Political counterpart to Lee Jungryong who has established a cooperative relationship with Jin Taekyung and Choi Minwoo while seeking to restrain the power concentrated in their two Guilds.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 745
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 746
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple, the Fire Gate Clan's nineteenth successor, and the Pavilion Master of the Fire Dragon Pavilion within the Murim Alliance, a Supreme Peak master with the Heavenly Martial Physique and Force, a publicly recognized S-rank-level Hunter who formally retains an A-rank license, a traveler between Murim and another world resembling the realm of immortals, and the creator of the beginner-accessible Smiling Mana Cultivation Method.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate, trusted manager of media and official arrangements, and now the Peace Guild's Guild Master, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 746
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### The Prophet.md

# The Prophet (선지자)

- **Safe through:** Chapter 746
- **Aliases:** None
- **Role:** The Prophet is the mysterious leader of the revived Hasasin, a Middle Eastern terrorist organization preparing further attacks against apostates and Western heretics.
- **Personality:** Religiously fervent, commanding, and shrouded in an intentionally indistinct identity.
- **Voice:** Mysterious, genderless, and age-indeterminate, speaking in solemn religious imperatives.
- **Relationships:** The Prophet commands the ten warriors and is revered as a sacred figure by the followers.

## Korean source

```text
＃747화



먹구름에 휩싸인 하늘 아래, 스기하라 교이쿠는 멍하니 생각했다.

‘도대체 무슨 일이 벌어진 거지?’

한낱 평범한 민간인에 불과한 그의 정신은 자신에게 일어난 상황을 받아들이지 못했다.

벌벌 떨리는 팔다리는 이미 주인의 의지를 벗어났고, 짠내 나는 바닷물을 한껏 들이킨 속은 구조 헬기의 거친 움직임을 버티지 못했다.

아니, 교이쿠가 진정 버틸 수 없었던 것은 갑작스럽게 들이닥친 끔찍한 현실일지도 몰랐다.

“우욱, 쿠웨에엑!”

더러운 토사물이 사방으로 튀었다.

그중 일부는 교이쿠와 함께 구호용 그물에 실려 있던 다른 이들에게 닿았지만, 누구도 불평하거나 신경 쓰지 않았다.

그저 혼이 나간 눈빛으로 발아래에 펼쳐진 광경을 바라볼 뿐.

콰드드드득!

부서지고, 함몰되며, 휩쓸린다.

수십 미터. 어쩌면 수백 미터에 이를지도 모르는 거대한 파도.

직접 보고 있음에도 믿을 수 없는 바다의 재앙이 모든 것을 집어삼키고 있었다.

하루에도 수백 척의 선박이 드나들던 도쿄만의 항구는 이미 흔적도 없이 사라졌고, 각각 수만 톤에 달하는 화물선은 스티로폼처럼 부서진 채 파도를 따라 가까운 공업 단지를 덮쳤다.

구궁, 꽈아아앙!

굉음과 동시에 맹렬하게 솟구친 화염이 사람들의 비명을 집어삼켰다.

끊임없이 울려 퍼지는 경보음 아래, 개미 떼처럼 작게 보이는 자동차와 인파가 재앙을 피해 뿔뿔이 흩어지고 있었다.

이 끔찍한 재앙을 피해.

자신들에게 닥친 운명을 받아들이지 못한 채.

그리고 살기 위해 발버둥 치는 그들의 등 뒤로, 거대한 음영(陰影)이 드리워졌다.

콰아아아아!

“아, 아아…….”

상공에서 그 모든 광경을 지켜보던 생존자들은 넋 나간 탄식을 흘렸다.

대격변 이후 수십 년간 피땀 흘려 복구했던 터전이, 찬란한 문명이 무너져 내리고 있었다.

늘 방파제에 가로막혀 흩어지던 새하얀 포말도, 푸르던 바닷물도 이제는 붉게 물들었다.

가로막는 모든 것을 부수고 휩쓸며 나아가는 저 거대한 파도를 막을 수 있는 것은 아무것도 없었다.

아니, 설령 파도가 가라앉는다고 해도 마찬가지일 것이다.

이건 단순한 자연재해가 아니니까.

항구와 공업 단지를 집어삼킨 저 깊은 물결 아래에는, 그보다 더한 재앙이 도사리고 있었으니까.

기적적으로 살아남은 생존자들은 그 진실을 알고 있었고, 그렇기에 자신들의 맞은편에서 날아오는 수십여 대의 전투기들을 발견하고 피를 토하듯 부르짖을 수밖에 없었다.

“아, 안 돼!”

“오지 마!”

하지만 그들의 간절한 외침은 어디에도 닿지 않았다.

소닉 붐(Sonic Boom)을 일으키며 하늘을 가로지른 전투기 편대에도, 이 사태를 수습하기 위해 전투기에 몸을 실은 일본의 정예 헌터들에게도.

그리고…… 오랜 잠에서 깨어난 심해(深海)의 괴물에게도.

고오오오옹.

낮지만 거대한 울림이 사그라지던 파도를 일으켜 세웠다.

거세지던 바람이 폭풍이 되어 휘몰아치고, 어느샌가 하늘을 가린 수많은 먹구름 사이에서 굉음이 울려 퍼졌다.

구구구구궁.

살아 숨쉬는 근방의 모든 생명체가 석상처럼 굳은 채 멍하니 하늘을 바라보았다.

그것은 뼛속 깊이 각인된 공포였고, 살아 있기 때문에 느끼는 본능적인 직감이었다.

힘.

자연이 가진 힘. 그러나 동시에 자연적이지 않은 힘.

“저게 도대체 뭐…….”

대기하고 있던 헌터들에게 하강 명령을 전달하려던 파일럿이 신음처럼 뇌까린 그 순간.

화아악!

하늘에서 내리꽂힌 수백, 수천 줄기의 뇌전(雷電)이 온 세상을 하얗게 물들었다.



* * *



긴급 소집된 일본 방위성(防衛省) 작전 통제실은 조용했다.

숨 막히는 침묵. 소리 없이 움직이는 목울대와 흐릿한 눈동자들.

수십여 명의 고위 관료와 장군들이 있음에도 누구 하나 먼저 입을 여는 자가 없었다.

그들이 할 수 있는 것이라고는, 혼이 빠져나간 눈빛으로 통제실 내부에 설치된 홀로그램 화면을 응시하는 것이 전부였다.

‘지금…… 지금 무슨 일이 벌어진 거지?’

모두의 머릿속을 점령한 단 하나의 생각.

그만큼 그들이 확인한 광경은 충격적이었다.

홀로그램 화면을 가득 메울 만큼 강렬한 섬광. 자신들도 모르게 눈을 감았던 그들이 볼 수 있던 것은 지상으로 추락하는 수십여 대의 항공기들과 그것을 집어삼킨 파도뿐이었다.

“저, 전멸……입니다.”

눈치 없는 누군가의 보고가 힘없이 침묵을 깨트렸고, 그것은 모두가 마주하기 싫은 진실이었다.

모든 것이 사라졌다. 아니, 죽었다.

수백, 수천 줄기의 번개는 범위 안에 존재하는 모든 것들을 잿더미로 만들었다.

기적적으로 살아남은 이들을 태우고 이동하던 구조 헬기들도, 항공 자위대가 자랑하는 전투 편대와 긴급 동원한 수백의 헌터들도 그렇게 끝장났다.

하지만 작전 통제실을 죽음 같은 침묵으로 몰아넣은 것은, 이미 열 개에 달하는 시(市)를 집어삼키고 수도마저 위협하는 저 쓰나미의 존재 때문만은 아니었다.

괴물.

지금으로부터 수십여 년 전 사라졌던, 그렇기에 두 번 다시 나타나지 않으리라 생각했던 괴물의 모습을 그들은 보았다.

“……스사노오(スサノオ).”

바다와 폭풍을 다스린다고 하여 붙여진 괴물의 별칭.

그러나 그 이름을 신음처럼 중얼거린 어느 장성은 황급히 입을 다물었다.

다음 순간 자신을 노려보는 방위대신(防衛大臣)의 시선을 느꼈기 때문이었다.

“그, 그게…….”

“주둥이 닥치고 있게, 요시무라.”

다급히 변명하려는 목소리를 틀어막은 일본 방위대신은 주위를 둘러보았다.

당장 대책을 내놓아야 할 그들 중 절반은 아직도 충격에서 벗어나지 못한 채 허우적거리고 있었고, 남은 절반은 다시 한번 그의 입술이 열리기만을 기다리고 있었다.

마치 먹이를 기다리는 아기 새처럼.

혹은, 자신들을 대신하여 이번 사태의 책임을 대신해 줄 유일한 희생양을 원하는 것처럼.

뿌득.

늙은 방위대신은 이를 갈았다.

이토록 많은 장성과 관료들이 있거늘, 아무리 둘러봐도 마땅한 사람이 없다.

멍청하고 겁 많은 총리대신은 일찌감치 벙커에 처박혔고, 능력 있고 책임감 있는 극소수의 지휘관들은 이 방위성 통제실에 들어올 만큼 훌륭한 뒷배를 두지 못했으니까.

결국, 당장 총대를 짊어질 사람은 한 사람뿐이었다.

‘이런 무능력한 놈들!’

방위대신은 자신 역시 다이묘 출신인 선조 덕분에 출세한 것을 까맣게 잊고 내심 욕설을 퍼부었지만, 당장 눈앞에 들이닥친 현실을 부정할 만큼 무지하지는 않았다.

“전력을, 전력을 다해 저놈을 막게. 자위대건, 헌터건 상관없어. 할 수 있는 모든 수단을 전부 동원하란 말이다!”

“네, 넵!”

“그리고…….”

쾅!

주름진 손으로 테이블을 내리친 방위대신은, 차마 말을 잇지 못하고 눈을 질끈 감았다.

‘정말, 정말 이렇게까지 해야 한단 말인가!’

머릿속을 스치는 짧은 고민.

하지만 그것도 잠시뿐이었다.

이미 상황을 걷잡을 수 없는 방향으로 치달았고, 더욱 큰 재앙을 최대한 막기 위해서는 ‘그’의 존재가 누구보다 적격이었으니까.

“세계에 도움을 청하게. 특히 그자는 어떤 외교적 대가를 치르더라도 반드시 불러야 해.”

“예?”

“그자라면…….”

브로콜리를 먹는 어린아이처럼 파르르 떨리는 입술.

영문을 모르겠다는 표정으로 자신을 바라보는 사람들을 향해, 방위대신은 피를 토하듯 외쳤다.

“그자! 그 조센징을 부르란 말이다! 진태겨엉!”

대 황국신민으로서의 자존심이 용납할 수 없었지만, 그에게 더 이상의 선택권은 없었다.

저 괴물은, 레비아탄(Leviathan)은 하늘이 내린 악마였으니까.

‘그 악몽을 다시 한번 반복할 수는 없다!’

그리고 얼마 지나지 않아 통제실 곳곳에 설치된 크고 작은 홀로그램 TV에서 흘러나온 뉴스는, 진태경을 택한 방위대신의 선택이 옳았음을 알려주고 있었다.

- 전 세계가 다시 한번 불길에 휩싸였습니다. 지금으로부터 열흘 전, 사상 초유의 연쇄 테러를 일으킨 바 있던 이른바 ‘선지자’는 동영상을 통해 두 번째 연쇄 테러를 예고…….

- 속보입니다. 미국 맨해튼에서 몬스터 웨이브가 발생했습니다. 이를 시작으로 미국을 비롯한 전 세계가 초비상 사태에 진입…….

- 현재 몬스터 웨이브가 발생한 국가에 한하여 입, 출국 금지령이 내려졌습니다. 이에 따라 일본 도쿄를 지원하기 위한 헌터 임시 소집령이 일부 무산되었으며, 가장 가까운 아시아에서는 한국만이 유일하게 지원 가능한 것으로 판단…….



* * *



- 일본 국방성이 외교부를 통해 정식으로 긴급 지원을 요청했습니다.

백한성 대통령에게서 전달받은 그 소식은, 모든 것이 시작되었음을 알리는 신호탄이었다.

“아레스와 평화 길드가 선발대로 출발합니다. 최소 B급 이상, 자원하는 이들만을 대상으로 한 다섯 개 팀이 이미 대기 중입니다.”

최 팀장의 대처는 누구보다 빨랐다.

그는 도쿄의 소식을 처음으로 접한 순간부터 소집령을 내려놓은 상태였고, 백한성 대통령은 가장 빠르고 안전하게 목적지로 향할 수 있도록 공군을 준비시켰다.

“텔레포트 마법진은요?”

필요한 장비를 챙기며 건넨 물음에 최 팀장이 고개를 저었다.

“시도는 해 볼 수 있겠지만, 지금으로서는 실패할 확률이 너무 높습니다. 그렇지 않아도 열흘 전 있었던 몬스터 웨이브로 도쿄 일대의 마력 분포도가 급격히 상승했는데, 벌써 세 배 이상의 수치를 기록 중이에요.”

“빌어먹을. 중국 생각나네.”

“예. 그때와 같은 상황입니다.”

마나와 마력은 서로에게 상극이다.

지금처럼 마력 분포도가 급격하게 증가하고 불안정할 때 공간 이동을 시도했다간, 몸이 단단한 쇳덩어리라 해도 1000피스짜리 퍼즐처럼 분해될 수도 있다.

“그럼 소요 시간은요?”

“인근 기상 악화를 고려해서 30분 정도로 예상하고 있습니다.”

“30분…….”

물론 넓은 공항 활주로에 안전 착륙하는 일 따위는 없을 거다.

이미 일본이 자랑하는 도쿄 국제공항은 개 박살 났을 확률이 90% 이상이니까.

‘남은 10%는 우리가 가는 길에 박살 날 확률이고.’

나는 크게 심호흡했다.

머릿속에서는 일본 국방성에서 보냈던 영상이 다시 한번 재생되고 있었다.

거대한 삼각파도에 휩쓸리는 해상 자위대와 수몰되는 육지.

일본 해안선을 따라 설치되어 있던 광범위 방어 마법도 우습게 깨트린 그것은 수만 명이 넘는 사람들을 집어삼키고, 무수한 벼락으로 남은 희망마저 잿더미로 만들었다.

아득한 신화로부터 전해져 내려온 자신의 힘을 증명하듯이.

‘레비아탄.’

대격변 당시 해상을 지배했던 바다의 악마.

마왕 아스모데우스가 거느린 가장 강력한 S급 몬스터들 중 하나였으나, 그의 죽음과 함께 자취를 감춘 재앙.

누군가는 레비아탄이 마왕과 함께 죽음을 맞이했다고 주장했고, 누군가는 놈이 살아남아 때를 기다리고 있을 뿐이라며 반박했지만 어떠한 증거나 입증도 없이 시간은 하염없이 흘렀다.

그리고 오늘.

레비아탄이라는 악몽이 되살아났다. 삼십여 년이라는 세월을 뛰어넘어 바로 이 세상에.

‘놈이 나타난 것이 우연일까, 아니면…….’

누군가에게 의도된 필연(必然)일까.

해결되지 않는 그 의문을 마음속으로 뇌까리며, 나는 모든 준비를 끝마친 채 기다리고 있던 헌터들과 항공기를 향해 걸음을 내디뎠다.

저 멀리서 불어오는 바람에 희미한 피비린내가 섞여 있는 듯했다.
```

## Final English reading copy

```markdown
# Chapter 747

Beneath a sky shrouded in dark clouds, Sugihara Gyoiku thought blankly.

*What the hell is happening?*

His mind, belonging to nothing more than an ordinary civilian, could not process what had happened to him.

His trembling limbs had already stopped obeying their owner’s will, and his stomach, full of salty seawater, could not withstand the rough movements of the rescue helicopter.

No—perhaps what Gyoiku truly could not endure was the horrifying reality that had suddenly come crashing down on him.

“Ugh—bwaaaargh!”

Dirty vomit sprayed in every direction.

Some of it hit the other people loaded into the rescue net with Gyoiku, but no one complained or even seemed to care.

They simply stared at the scene unfolding below them with empty eyes.

*Crack!*

It broke, collapsed, and was swept away.

A gigantic wave dozens of meters high—perhaps even hundreds.

Even though they were witnessing it with their own eyes, they could not believe the disaster unfolding across the sea as it swallowed everything in its path.

The port of Tokyo Bay, where hundreds of ships had entered and departed every day, had already vanished without a trace. Cargo ships weighing tens of thousands of tons were shattered like Styrofoam, then carried along by the waves into the nearby industrial complex.

*Rumble—BOOM!*

With a deafening roar, fierce flames surged upward and swallowed the people’s screams.

Beneath the constant wail of alarms, cars and crowds that looked tiny as swarms of ants scattered in every direction to escape the disaster.

To escape the horrifying calamity.

Unable to accept the fate that had befallen them.

And behind those struggling desperately to survive, an enormous shadow fell across the ground.

*Whoooosh!*

“Ah… Ahhh…”

The survivors watching the whole scene from above let out vacant moans.

The land they had painstakingly rebuilt through decades of sweat and blood after the Great Cataclysm was collapsing. A magnificent civilization was falling apart.

The white foam that had always scattered against the breakwaters and the blue seawater had both turned red.

Nothing could stop that enormous wave as it smashed through and swept away everything in its path.

No—even if the wave itself subsided, it would make no difference.

Because this was not merely a natural disaster.

Beneath the deep waters that had swallowed the port and industrial complex, an even greater calamity was lurking.

The survivors who had miraculously lived through it knew the truth. That was why, upon spotting dozens of fighter jets flying toward them from the opposite direction, they could only scream as though coughing up blood.

“N-No!”

“Don’t come here!”

But their desperate cries reached no one.

Not the squadron of fighter jets streaking across the sky with sonic booms.

Not the elite Japanese Hunters who had boarded those aircraft to deal with the situation.

And not the deep-sea monster that had awakened from its long sleep.

*Goooooong.*

A low but immense rumble stirred up the waves that had begun to subside.

The strengthening wind turned into a storm and howled through the air, while thunderous roars soon echoed among the countless dark clouds covering the sky.

*Rumble, rumble…*

Every living thing in the vicinity froze like a statue and stared blankly at the sky.

It was a fear engraved deep in their bones—a primal instinct they could feel simply because they were alive.

Power.

The power of nature. But at the same time, a power that was not natural.

“What the hell is that…?”

The pilot was muttering in a groan as he prepared to relay the order for the Hunters on standby to descend.

At that moment—

*Fwoosh!*

Hundreds, thousands of bolts of lightning plunged down from the sky and flooded the entire world with white light.

* * *

The Japanese Ministry of Defense’s operations control room, hastily called into session, was silent.

A suffocating silence. Throats moving soundlessly. Eyes clouded with shock.

Although dozens of high-ranking officials and generals were present, not a single person spoke first.

All they could do was stare with vacant eyes at the holographic screen installed inside the control room.

*What… What the hell just happened?*

A single thought occupied everyone’s mind.

That was how shocking the scene they had witnessed was.

A flash of light so intense that it filled the holographic screen. When the people who had instinctively closed their eyes finally opened them again, all they could see were dozens of aircraft plunging toward the ground—and the waves swallowing them whole.

“Th-They’ve been… completely wiped out.”

An oblivious report feebly broke the silence, revealing the truth that everyone wanted to avoid facing.

Everything had vanished.

No—they had died.

The hundreds, thousands of lightning bolts had turned everything within their range to ash.

The rescue helicopters carrying those who had miraculously survived. The fighter squadron proudly fielded by the Air Self-Defense Force. The hundreds of Hunters mobilized in an emergency.

They had all been finished.

But the thing that had plunged the operations control room into deathly silence was not merely the tsunami that had already swallowed as many as ten cities and now threatened the capital.

It was the monster.

They had seen the form of a monster that had vanished several decades ago—one they had believed would never appear again.

“……Susanoo.”

That was the monster’s nickname, given because it was said to rule the sea and storms.

But the general who muttered the name like a groan hurriedly closed his mouth.

The next moment, he felt the Defense Minister’s glare fixed on him.

“Th-That was…”

“Shut your trap, Yoshimura.”

The Japanese Defense Minister cut off the man’s hurried excuse and looked around the room.

Half of the people who needed to produce a solution immediately were still floundering in shock. The other half waited for his lips to open again.

Like baby birds waiting for food.

Or like people hoping for a single scapegoat who could take responsibility for this disaster in their place.

*Crack.*

The elderly Defense Minister ground his teeth.

There were so many generals and officials, yet no matter where he looked, there was no suitable person.

The foolish, cowardly Prime Minister had buried himself in a bunker long ago, while the very few capable and responsible commanders did not have powerful enough backers to enter the Ministry of Defense’s control room.

In the end, there was only one person who could shoulder the blame right now.

*These incompetent bastards!*

The Defense Minister cursed them inwardly, completely forgetting that he himself had risen through the ranks thanks to an ancestor from a daimyo family.

Still, he was not so ignorant that he could deny the reality bearing down on them.

“Stop that thing with everything we have! I don’t care whether it’s the Self-Defense Forces or Hunters. Mobilize every resource at our disposal!”

“Yes, sir!”

“And…”

*Bang!*

The Defense Minister slammed his wrinkled hand against the table, then squeezed his eyes shut without being able to continue.

*Do we really… do we really have to go this far?*

A brief hesitation passed through his mind.

But it lasted only for a moment.

The situation had already spiraled beyond control, and to prevent an even greater disaster as much as possible, *that man* was more qualified than anyone else.

“Ask the world for help. And that man in particular—we must bring him here, no matter what diplomatic price we have to pay.”

“What?”

“If it’s him…”

His lips trembled like a child being forced to eat broccoli.

Then, facing the people staring back at him with no idea what he meant, the Defense Minister shouted until it seemed as though he were coughing up blood.

“That man! I said call that Chōsenjin![^1] Jin Taekyuuung!”

His pride as a subject of the Great Japanese Empire could not accept it, but he had no other choice.

That monster—Leviathan—was a demon sent down by heaven.

*We can’t let that nightmare happen again!*

Not long afterward, news broadcast on large and small holographic televisions installed throughout the control room informed them that the Defense Minister had made the right choice by selecting Jin Taekyung.

> —The entire world has once again been engulfed in flames. Ten days ago, the figure known as “The Prophet,” who carried out an unprecedented series of terrorist attacks, announced a second series of attacks in a video…

> —Breaking news. A monster wave has occurred in Manhattan, United States. Beginning with this incident, the United States and the rest of the world have entered a state of emergency…

> —At present, entry and exit bans have been imposed on countries where monster waves have occurred. As a result, part of the emergency Hunter mobilization order intended to support Tokyo, Japan, has fallen through. Among the countries in the nearest region of Asia, only Korea is believed to be capable of providing support…

* * *

“Japan’s Ministry of Defense has officially requested emergency assistance through the Ministry of Foreign Affairs.”

The news delivered to us by President Baek Hanseong was the starting gun announcing that everything had begun.

“Ares Guild and Peace Guild are heading out as the advance team. Five teams are already waiting—B-rank or higher, and limited to volunteers only.”

Team Leader Choi’s response had been faster than anyone’s.

The moment he first heard what had happened in Tokyo, he had already issued the mobilization order. President Baek Hanseong had prepared the Air Force so that we could reach our destination as quickly and safely as possible.

“What about the Teleport Magic circle?”

Team Leader Choi shook his head at my question as I gathered the equipment we needed.

“We could try it, but the probability of failure is far too high right now. The magical-power distribution around Tokyo rose sharply because of the monster wave ten days ago, and it’s already measuring more than three times the previous level.”

“Damn it. This reminds me of China.”

“Yes. It’s the same situation as back then.”

Mana and magical power were natural opposites.

If we attempted spatial movement while the magical-power distribution was rising sharply and growing unstable like this, our bodies could be broken apart like a thousand-piece puzzle—even if they were solid lumps of iron.

“Then how long will it take?”

“Taking the worsening weather in the area into account, we estimate about thirty minutes.”

“Thirty minutes…”

Of course, we would not be making a safe landing on a broad airport runway.

There was at least a ninety-percent chance that Tokyo International Airport, once the pride of Japan, had already been blown to absolute shit.

*And the remaining ten percent is the chance it’ll be blown to shit on our way there.*

I took a deep breath.

The video sent by Japan’s Ministry of Defense replayed in my mind.

The Maritime Self-Defense Force being swept away by a gigantic triangular wave. The land being submerged.

The wave had shattered the extensive defensive Magic installed along Japan’s coastline as though it were nothing, swallowed tens of thousands of people, and turned even the last remnants of hope to ash beneath countless lightning bolts.

As though proving the power ascribed to it by myths passed down from time immemorial.

*Leviathan.*

The devil of the sea that had ruled the waters during the Great Cataclysm.

One of the most powerful S-rank monsters commanded by the Demon King Asmodeus, it was a calamity that had vanished along with his death.

Some claimed that Leviathan had died alongside the Demon King. Others argued that the monster had survived and was merely waiting for the right time.

But without any evidence or proof, time continued to pass.

And today—

The nightmare known as Leviathan had been resurrected.

It had crossed more than thirty years to return to this world.

*Was its appearance a coincidence, or…*

An inevitability intended by someone?

Muttering the unresolved question inwardly, I finished my preparations and began walking toward the Hunters and aircraft waiting for me.

The wind blowing from far away seemed to carry a faint smell of blood.

[^1]: A derogatory Japanese term for a Korean.
```

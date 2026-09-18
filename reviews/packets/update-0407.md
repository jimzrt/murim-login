<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0407.txt",
      "sha256": "f351b07c78f1c1309d760349df0112905916c5d49aa6f1025a8f6480d8a82588",
      "bytes": 14015
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "45af17648d9b26f4489e4afb546955ce55e3dc311f3989579232b1d057d43f95",
      "bytes": 1857
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "98361f9134cc47341aab6e25afaad0b495a260eda103ac56ee8d1a70b17b1cc4",
      "bytes": 136795
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "a0b9517ec63f39cf9c4a50fdee6d1e1c7375e6b0debb116dd78ab422177e1741",
      "bytes": 533
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "f1b799624420a5f024297b7d0c8c187975d6eaac1c7a9e3fce312da5f158c718",
      "bytes": 1212
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "c5087f20a9290c81ceb660b2db7d586f706da143de37f1a7053728ee2b3f1f44",
      "bytes": 622
    },
    {
      "path": "characters/Lee Jungryong.md",
      "sha256": "f8e5de4ae07c3f1c8fe29e8b2c191aaab581b3f808772f73a0c792836ce9a0da",
      "bytes": 1163
    },
    {
      "path": "characters/Wei Fenghu.md",
      "sha256": "d79601585b72b8ce66cdaee90aa2a10379ce51d8481cef1acc80ea0d44681727",
      "bytes": 560
    },
    {
      "path": "characters/Wu Heixing.md",
      "sha256": "98b0a3953808c700696a51f0e494f2733d68c465ca6b7c8a44611b0a5e9572d6",
      "bytes": 735
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "5a370b9eab3a8b2a8dea47a1c877bcd72e6faed970588ea5e4276879fbaa893b",
      "bytes": 120486
    }
  ],
  "estimated_tokens": 10505
}
-->

# Durable State Update — Chapter 407

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 407. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 407. Profile updates may replace only one
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
  "chapter": 407,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 407,
    "continuity_sources": [407],
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
    "The five-front human forces have spent a week winning through mobile warfare and are advancing toward Suining City, with Jin Taekyung’s western front and Lee Jungryong’s northern front among the fastest.",
    "Jin Taekyung and Team Leader Choi suspect that the sudden decline in the monsters’ number and quality is unnatural because the Arch Lich would not normally be defeated so easily.",
    "Wei Fenghu understands the same concern about the unexpectedly favorable battlefield situation.",
    "Jin Taekyung has demonstrated Hero’s Soul and the Flame-Extinguishing Divine Fist while routing lizard men on the western front.",
    "The Arch Lich has remained absent from the war but is now gathering mana in a ruined space and summoning an adversary.",
    "Seong Jinho is living with Jin Taekyung as his roommate and remains openly proud of Jin’s rise as a Hunter."
  ],
  "continuity_sources": [
    406
  ],
  "open_questions": [
    "Who is Lei Fei’s unidentified lord, what is the lord’s origin, and how does the lord relate to the Arch Lich’s objective?",
    "What happened to the Second Fiend assigned to the Qingcheng attack?",
    "Why has the Arch Lich withheld itself from the war, and what is it preparing now?",
    "What kind of being was the Skeleton Warlord before it became an undead commander?",
    "What specific situation will allow Jin to draw out Hero’s Power more strongly?"
  ],
  "safe_through": 406,
  "temporary_decisions": [
    "Render 영웅의 혼 as Hero’s Soul and 영웅의 힘 as Hero’s Power.",
    "Render 기동전 as mobile warfare.",
    "Render 쑤이닝시 as Suining City.",
    "Render 연대장 쉔 as Regimental Commander Shen.",
    "Render 도람프 as Doramp, 마이구미 신지로 as Maigumi Shinjiro, and 푸린 as Furin."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 이정룡    | **Lee Jungryong** |
| 삼류     | **Third Rate**    |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 살기     | **killing intent**                               |                                                       |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 상태               | **Status**                     |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 팀장      | **Team Leader**       |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 웨이펑후 | **Wei Fenghu** | Minister of National Defense under China's Central Military Commission. |
| 우헤이싱 | **Wu Heixing** | Chinese S-rank Hunter who provokes Jin and nearly draws his sword. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 준이 | **Jun** | Family nickname used in the form Jun's dad. |
| 존슨 | **Johnson** | Co-host of the American talk show that replays Taekyung's viral interview. |
| 미국 | **United States** | Country associated with the talk show and CNM. |
| 중국 | **China** | Country from which Team Leader Choi’s video originates. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 국방부 | **Ministry of National Defense** | Government ministry referenced in Taekyung's comparison about the steady passage of time. |
| 쑤이닝시 | **Suining City** | City in Sichuan Province and the operation's final destination. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 이정룡 | 진태경 | senior S-rank Hunter to younger Hunter and adversary | Young man | polished, teasing, and veiled-threatening | Uses a genial tone and indirect threats while trying to make Taekyung release the captives. |
| 진태경 | 이정룡 | younger Hunter to senior S-rank Hunter and adversary | you | polite but mocking and defiant | Taekyung answers Lee's soft threats with the wolf-and-tiger metaphor and refuses to yield. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 웨이펑후 | 진태경 | senior_military_official_to_ally | Mr. Jin | formal-polite | Wei Fenghu addresses Jin while inviting him to walk to the operations headquarters. |
| 진태경 | 웨이펑후 | Foreign Hunter to senior military official | General, Commander, or Supreme Leader | Polite but flustered | Jin jokingly cycles through grand titles while trying to interrupt Wei's emotional request. |
| 우헤이싱 | 진태경 | hostile S-rank Hunter to foreign Hunter and provocation target | peninsula bangzi | insulting and confrontational | Wu repeatedly addresses Jin with anti-Korean slurs. |
| 우헤이싱 | 이정룡 | younger S-rank Hunter to senior Ares Guild authority | Mr. Lee | formal and deferential | Wu addresses Lee respectfully despite his usual hostility toward Koreans. |
| 웨이펑후 | 이정룡 | senior military official to senior foreign S-rank Hunter | Mr. Lee | formal and concerned | Wei asks Lee whether something is wrong. |
| 필릭스 | 이정룡 | British prince to senior S-rank Hunter | Jungryong Lee | formal through a translation device | Felix permits Lee to omit His Highness and gives his own preferred form of address. |
| 진태경 | 필릭스 | Korean S-rank Hunter addressing a British prince | His Highness | mock-formal and sarcastic | Felix demands formal address, and Jin complies by calling him His Highness while continuing to mock him. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 404
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who has sworn never to kill again.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 406
- **Aliases:** Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, and a Supreme Peak master who has manifested Force and crossed the wall into true mastery.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother; Jeok Cheongang is his Master; Cheongpung is his trusted companion and only true martial rival; Choi Minwoo is his subordinate and student; his mother and sister Hayeon are among those he protects.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 406
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Lee Jungryong.md

# Lee Jungryong (이정룡)

- **Safe through:** Chapter 406
- **Aliases:** None
- **Role:** Vice Guild Master of Ares Guild, one of Korea's two S-rank Hunters, and a Supreme Peak-level martial artist who directs Ares Guild operations.
- **Personality:** Outwardly genial, calm, and humorous; calculating, manipulative, coercive, and ruthless when challenged
- **Voice:** Smooth, good-natured, and indirect, using teasing conversation and veiled threats before becoming openly furious
- **Relationships:** Master of Park Jihoon and Go Jun (Team Leader Seok), whom he personally selected and trained; longtime Great Cataclysm acquaintance of Park Tae Seop; adversary of Jin Taekyung; knew Team Leader Choi from childhood; has an antagonistic history with Kim Hwajong, who saved his life at the collapse of Mapo Bridge eighteen years earlier; was visibly shaken by learning that Choi is Cheon Taemin's maternal grandson; regards Cheon Taemin as an older brother despite no blood relation and has long held him in respect and fear; operates as Ares Guild's senior authority beneath its Guild Master

### Wei Fenghu.md

# Wei Fenghu (웨이펑후)

- **Safe through:** Chapter 406
- **Aliases:** None
- **Role:** Wei Fenghu is the Minister of National Defense under China's Central Military Commission and a four-star general.
- **Personality:** Courteous, reserved, and authoritative.
- **Voice:** Formal and measured, addressing Jin as Mr. Jin.
- **Relationships:** Wei Fenghu is Lei Fei’s maternal uncle who raised him as his own son; after Lei Fei’s death, he entrusted Lei Fei’s sword to Jin Taekyung.

### Wu Heixing.md

# Wu Heixing (우헤이싱)

- **Safe through:** Chapter 404
- **Aliases:** None
- **Role:** Wu Heixing is a Chinese S-rank Hunter known for frequent media exposure and scandal who secretly practices martial arts, including an internal-energy cultivation technique and fist-and-foot martial arts.
- **Personality:** Arrogant, status-conscious, abusive, and fiercely proud of his power, he responds to humiliation with anger, jealousy, and fear.
- **Voice:** Loud, insulting, entitled, and dependent on national and political status.
- **Relationships:** He is openly hostile toward Jin Taekyung and Faye Chen, and resents Jin receiving Chairman Shao Yang's attention.

## Korean source

```text
＃407화



다니엘 이노우에는 일본계 미국인이다.

네이비 씰(Navy SEALs) 대원이었던 그는 서른 살의 나이에 A급 헌터로 각성, 전역 후 민간 군사 기업에 취직하여 자신의 능력을 십분 발휘하고 있었다.

용병 일은 그럭저럭 이노우에의 적성에 맞았다. 한 해의 절반을 중동과 아프리카 분쟁 지역에 머물러야 했지만 엄청난 보수와 장기간의 휴식기를 가질 수 있었으니까.

이번 중국에서 터진 몬스터 웨이브에 참여하게 된 것도 비슷한 맥락이었다.

「헤이, 닌자. 무슨 생각해?」

불쑥 말을 건네는 동료의 질문에 이노우에는 눈을 가늘게 떴다.

「닥쳐, 샘. 그놈의 닌자 타령은 지겹지도 않냐?」

「뭐 어때. 이쯤 되면 네가 익숙해져야지.」

「지긋지긋해서 그런다. 너도 일곱 살 때부터 닌자, 사무라이라고 불려 봐. 정신병 걸릴 것 같다고.」

「왜, 난 좋을 것 같은데?」

「빌어먹을 양키 자식.」

「그렇게 불러 주면 고맙지. 난 양키스 팬이거든.」

자그마한 체격의 백인이 이노우에의 투덜거림에 낄낄거리며 웃었다.

「이제 받아들이라고. 이 정도면 운명이야. 네가 가진 능력도 완전히 닌자잖아.」

「……제기랄.」

이노우에는 작게 욕설을 중얼거렸다.

동료의 말마따나 그가 각성 후 부여받은 능력은 은신에 최적화되어 있었다.

그 덕분에 첩보와 요인 암살의 스폐셜 리스트가 되었지만, 닌자라는 이미지까지 완전히 굳혀져 버렸다.

「여자 친구가 임신했다며? 아기 이름은 나루토 어때?」

이노우에는 계속해서 깐죽거리는 동료를 향해 중지를 치켜세웠다.

「네 아들 이름을 사스케로 하면 생각해 보지.」

「오, 나쁘지 않은데?」

두 사람의 대화에 주위에서 피식거리는 웃음이 새어 나왔다.

조금 전만 해도 딱딱하게 경직되어 있던 분위기가 풀어지자, 이노우에와 그의 동료도 서로를 향해 슬쩍 웃어 보였다.

두 사람은 이미 수년째 호흡을 맞춰 온 단짝이다. 방금의 대화 역시 임무 시작 전 긴장을 풀어 주려는 꽁트에 가까웠다.

‘긴장이 너무 과하면 오히려 실수를 연발하기 마련이지.’

전투도 마찬가지지만 지금과 같은 첩보 작전은 더더욱 그렇다.

통신도, 마법도 사용할 수 없는 미지의 땅. 더군다나 상대는 멍청하고 잔인하기만 한 반군 지도자가 아니라, 전대미문의 몬스터 웨이브를 일으킨 아크 리치(Arch Lich)였다.

‘전황이 아무리 유리하다 해도 방심은 금물이야.’

내심 뇌까린 이노우에가 스무 명의 첩보 대원들을 향해 입을 열었다.

「자, 지금부터 2인 1조로 나누어 침투한다. 의사 전달은 수신호로, 위급할 시 소지한 신호탄을 쏴. 각자의 목적지와 루트는 모두 빈틈없이 숙지했겠지?」

「예.」

「좋아, 그럼…… 세 시간 뒤, 이곳에서 다시 만나자. 해산.」

작전 개시를 알리는 이노우에의 말에 고개를 끄덕인 첩보 대원들이 곳곳으로 흩어졌다. 은밀하고도 신속하게 사라지는 그들을 바라본 파트너, 샘이 턱짓했다.

「슬슬 우리도 가 볼까, 닌자?」

「그래. 이 속 편한 양키 놈아.」

「너무 그러지 말라고. 네 실력은 최고야. 세 시간 후면 아크 리치가 입고 있는 팬티 색깔까지 알아낸 다음 복귀하고 있겠지.」

「……정말 그랬으면 좋겠군.」

나직한 한숨을 내쉰 이노우에는 걸음을 내디뎠다. 쑤이닝시 전역을 뒤덮은 희끄무레한 안개가 축축하게 그의 전신을 감싸 왔다.



* * *



멈추지 않을 것 같던 다섯 개 전선의 진격이 멈췄다.

아크 리치가 있는 쑤이닝시에서 200km 떨어진 지점. 재정비와 휴식을 취하고 있던 우리에게 반가운 얼굴이 찾아왔다.

「한국 친구들, 그동안 잘 지냈어?」

주위에서 상당한 기의 파동이 느껴진다 싶더니, 역시 그였다. 나는 매직 존슨과 주먹을 부딪치며 대답했다.

“그럭저럭요.”

「진. 사랑스러운 미라클 보이. 보고 싶었어.」

“죄송한데 사랑스러운, 은 빼 주실래요?”

「그럼 크레이지 보이로 할게. 미친 짓을 벌인 건 사실이니까.」

매직 존슨이 씩 웃으며 덧붙였다.

「더할 나위 없이 영웅적인 행동이기도 했지. 여기 있는 최도 마찬가지고.」

[영웅의 혼]을 정성스럽게 손질하고 있던 최 팀장이 작게 고개를 숙였다.

“다시 뵙게 되어 반갑습니다. 미스터 존슨.”

「최, 너무 그러지 마. 딱딱해지잖아.」

“……!”

“……!”

「물론 분위기가.」

매직 존슨이 껄껄거리며 웃었다.

이 정도면 우리의 반응을 즐기는 게 확실하다. 덩치에 안 맞게 장난기가 넘친단 말이지.

뭐, 우리도 이제는 모든 것이 장난이라는 사실을 알고 있다.

매직 존슨을 만날 때마다 항상 케겔 운동을 하던 최 팀장도 피식 웃으며 물었다.

“그런데 어쩐 일로 오셨습니까?”

「총사령부로부터 긴급 호출. 중요한 사안이야.」

나는 문득 눈살을 찌푸리며 중얼거렸다.

“어쩐지 데자뷰 같은데. 이거 어디서 많이 본 전개 아니에요?”

「걱정할 것 없어, 진. 지난번과 같은 일은 없을 테니까.」

지난번과 같은 일이란, S급 헌터들이 자리를 비운 사이 본진이 개 털리는 상황을 뜻한다.

뭐, 지금은 전선 간의 간격이 좁혀진 덕분에 모여봤자 엎어지면 코 닿을 거리라서 괜찮겠지만.

‘굳이 통신으로 하지 않는 건 그만큼 중요한 사안이라는 거겠지.’

연합군의 연이은 승리와 몬스터들이 물러날수록 아크 리치의 권역은 쑤이닝시까지 축소되었고, 현재 지점에서는 통신과 마법 모두 원활한 수준이다.

“뭐 때문에 모이는 건지 알고 계세요?”

「아니. 하지만 장담컨대 그리 유쾌한 사안은 아닐 거야. 내 목숨을 걸지.」

“…….”

아니, 제발 그딴 걸로 목숨 걸고 장담하지 마. 우리에게 좀 더 희망을 심어 줘.

하지만 세상 당당한 매직 존슨은 나와 최 팀장을 향해 손을 내밀었다.

「어쨌든 이미 모두 모여 있어. 너희가 마지막 손님이야.」

“그럼 부탁드리겠습니다. 미스터 존슨.”

최 팀장은 별 망설임 없이 손을 맞잡았고, 이미 매직 존슨표 텔레포트를 겪어 본 나는 눈꺼풀을 떨며 그의 손가락을 잡았다.

“제발 안전 운행 부탁드립니…… 갸아아아아악!”

쏴아아악.

전신이 음료수 캔처럼 찌그러지는 듯한 감각과 함께, 나는 새로운 공간으로 내팽개쳐 졌다.

“갸아아아아…….”

“…….”

“…….”

젠장. 하필이면 여기냐.

말없이 나를 응시하는 십여 쌍의 눈동자. 황당함이 담긴 S급 헌터와 중국 고위 장성들의 시선에, 나는 비명을 멈추고 슬그머니 빈 자리에 앉았다.

“회의 시작 안 합니까?”

잠시 말을 잇지 못하던 웨이펑후 국방부장이 입을 열었다.

「……그럼 회의를 시작하겠소.」

이어진 회의에서 중점적으로 다뤄진 주제는 하나. 바로 첩보대의 유일한 생존자가 전해 온 정보였다.

「첩보대를 맡은 다니엘 이노우에는 예정된 작전 시간을 훌쩍 넘긴 여덟 시간 만에 쑤이닝시에서 탈출했고, 3만여 마리에 달하는 몬스터 군단을 발견했다고 전했소.」

3만이라…….

엄청난 대병력이긴 하지만, 예상했던 범위 안에 충분히 들어가는 수치다.

아크 리치의 몬스터 군단은 일주일 전 패퇴한 것을 시작으로 속절없이 물러나기만 했고, 그 과정에서 어마어마한 병력 손실을 감수해야 했다.

“국방부장의 표정을 보아하니 그게 전부는 아닌 것 같구려.”

이 자리에 모인 이들 중 웨이펑후 국방부장에게 저렇게 편하게 하오체를 쓸 수 있는 사람은 몇 없다.

그리고 이정룡은 나와의 개인적인 감정을 떠나 충분히 그럴 자격이 되는 사람이다.

「이 선생이 하신 말씀이 맞소. 직접 목격하여 산출한 것으로만 추정 3만이며, 실제 숫자는…….」

“두 배, 어쩌면 그 이상일 수도 있겠군.”

「그렇소.」

“……음.”

곳곳에서 침음성이 흘러나왔다. 마지막을 위해 비축해 놓은 힘이 있을 거라곤 생각했지만 그 정도였을 줄이야.

웨이펑후는 진중한 얼굴로 말을 이었다.

「하지만 대다수의 몬스터가 중, 하급일 거요. 그나마 위안이 되는 부분이지.」

「그건 우리도 마찬가지예요, 웨이펑후.」

말없이 술잔을 기울이던 파이 첸의 한 마디에 필릭스 왕자가 고개를 끄덕였다.

「그 말대로다. 기대 이상으로 많은 병력이 아군에 합류하긴 했지만, 승리를 확신하긴 어렵지.」

「빌어먹을. 그놈의 몬스터는 죽여도 죽여도 끝이 없군.」

우헤이싱의 투덜거림에 나는 참지 못하고 피식 웃었다.

「왜 웃지?」

“웃기니까 웃지. 인마.”

「뭐?」

“누가 들으면 네가 엄청 열심히 싸운 것 같잖냐. 일주일 전 몬스터 군단 습격 때 일찍 가면 위험할까 봐 우회하려고 했던 새끼가.”

“……!”

표정이 볼만하다.

모를 줄 알았나 본데, 이미 우헤이싱의 추태는 모든 전선에 소문이 쫙 퍼진 상태였다.

“너도 고생한 건 알겠는데, 나나 다른 사람들 앞에서 징징거리진 마라. 보면 짜증 나려고 하니까.”

「이익……!」

“자영업자신가. 왜 이렇게 자꾸 이익거려.”

얼굴이 벌겋게 달아오른 우헤이싱은 당장이라도 달려들 것처럼 몸을 움찔거렸지만, 놈이 할 수 있는 행동은 딱 거기까지였다.

패배의 뼈아픈 기억은 오래 간다.

평생 남들에게 떠받들어졌던 온실 속 화초는 찬바람에도 시들기 마련이다.

물론 전혀 다른 종류의 화초도 있다.

이를테면…… 지금 내 옆자리에 있는 최 팀장이라든지.

“두 분 다 그만하시지요.”

차분한 목소리로 만류하는 최 팀장을 바라본 우헤이싱이 눈깔을 부라렸다.

「지금 나한테 명령한 거냐?」

“그렇게 받아들이셨다면 유감입니다, 우헤이싱.”

「너…….」

자신의 기세에도 눈 하나 깜짝하지 않고 대답하는 최 팀장의 모습에, 우헤이싱이 벌떡 일어났다.

아니, 일어나려 했다.

“앉아.”

「……!」

송곳처럼 쏘아 보낸 기세에 놈의 신형이 덜컥 굳었다.

놀란 눈동자로 나를 바라보는 다른 S급 헌터들의 시선도.

나는 깊게 가라앉은 이정룡의 눈빛을 힐끗 바라본 뒤 말을 이었다.

“착각할까 봐 말하는데, 명령 맞아.”

「너, 너……!」

“앉아. 이게 마지막이다.”

쏴아아악!

파도처럼 밀려드는 기파에 우헤이싱의 아랫입술이 파르르 떨렸다.

어쩌면 놈은 무림에서도 천재 축에 드는 놈일지도 모른다.

아니, 맞다. 30대에 S급 헌터가 됐다는 건 그만한 재능이 뒷받침되지 않고서야 불가능한 일이니까.

‘하지만 반쪽짜리지.’

각성은 불로소득이다. 놈은 복권에 당첨된 것처럼 스무 살이 되자마자 뛰어난 능력을 부여받았고 마나를 얻었다.

거기에 무림인들처럼 공력을 쌓고 초절정의 무공을 익힌다?

글쎄…… 무공을 익힌다면 기술적인 측면이 보완되겠지만 거기까지 도달하기도 전에 떨어져 나갈 게 분명하다.

가진 바 재능에 비해 노력과 의지는 삼류 수준이니까.

“그만하지.”

팽팽한 분위기를 무너트린 것은 이정룡의 부드러운 중저음이었다.

환갑이 훌쩍 넘었음에도 미중년의 모습을 한 구렁이가 웃음기 띤 얼굴로 나를 응시한다.

“성장한 게 실력뿐인 줄 알았더니, 살기(殺氣)도 짙어졌군.”

나는 무감각한 눈으로 마주보며 대꾸했다.

“이곳저곳에서 구르다 보니 독기가 생기더라고요.”

“서부 전선이 유독 치열했다는 이야기는 들었지.”

“틀린 말은 아닙니다. 서부 전선 오쉴?”

“정중하게 거절하겠네. 오죽 치열했으면 셋밖에 살아남지 못했을까.”

“……!”

“늙을수록 겁이 많아져서 탈이야. 허허.”

전신의 피가 싸늘하게 식는 기분이다.

그날의 참혹했던 전장이 눈앞을 스쳐 지나가고, 어느샌가 내 입가에는 희미한 웃음이 맺혀 있었다.

“하고 싶은 말이 뭡니까?”

“아군끼리 적대하는 것보다 생산적인 고민을 해 보세. 마지막 전투에 대한 대책이 좋겠군. 진태경, 자네 생각은 어떤가?”

나는 나직하게 의자 팔걸이를 두드렸다.

속이 뒤틀리는 기분이었지만 이정룡의 말은 정곡을 찔렀다.

맞다, 지금은 당장 코앞까지 닥친 전투를 대처해야 할 때다.

그리고 내 머릿속에는 한 가지 생각이 떠올랐다.

“결사대.”

“결사대?”

사람들의 시선이 모여든다. 누군가는 동의한다는 듯이 고개를 끄덕이고, 누군가는 불안한 표정이다.

하지만 내 이성과 본능이 말하고 있었다.

이것이 가장 피해를 최소화하고 승리를 거둘 수 있는 최선의 방안이라고.

“최정예를 모아 머리를 칩시다.”

아크 리치가 소멸하면, 언데드 군단은 허물어진다.
```

## Final English reading copy

```markdown
# Chapter 407

Daniel Inoue was Japanese American.

A former Navy SEAL, he had awakened as an A-rank Hunter at the age of thirty. After leaving the military, he joined a private military company, where he put his abilities to excellent use.

Mercenary work suited Inoue reasonably well. He had to spend half of every year in conflict zones across the Middle East and Africa, but in exchange, he received enormous pay and long stretches of time off.

His decision to participate in the monster wave that had erupted in China had been made for much the same reason.

“Hey, ninja. What are you thinking about?”

At his comrade’s sudden question, Inoue narrowed his eyes.

“Shut up, Sam. Aren’t you sick of that damn ninja crap yet?”

“What’s the big deal? At this point, you should be used to it.”

“I’m sick of it because of that. Try being called a ninja or samurai since you were seven. It’ll drive you insane.”

“Why? Sounds good to me.”

“You damn Yankee bastard.”

“I’ll take that as a compliment. I’m a Yankees fan.”

The small white man snickered at Inoue’s grumbling.

“Just accept it already. At this point, it’s fate. Your abilities are completely ninja-like, too.”

“…Damn it.”

Inoue muttered a quiet curse.

Just as his comrade had said, the ability he had received upon awakening was optimized for stealth.

Thanks to it, he had become a specialist in espionage and targeted assassinations. But it had also cemented his image as a ninja.

“I heard your girlfriend’s pregnant. How about naming the baby Naruto?”

Inoue raised his middle finger at his relentlessly annoying comrade.

“If you name your son Sasuke, I’ll think about it.”

“Oh, not bad.”

Quiet snickers escaped from the people around them.

The stiff, rigid atmosphere loosened, and Inoue and his comrade exchanged faint smiles.

The two had been close friends and partners for years. Their exchange had been little more than a skit meant to ease the tension before the mission began.

*When the tension gets too high, people tend to make one mistake after another.*

The same was true of combat, but even more so of an espionage operation like this one.

An unknown land where neither communications nor magic could be used. And their opponent was not some stupid, brutal rebel leader, but the Arch Lich who had unleashed an unprecedented monster wave.

*No matter how favorable the battlefield is, letting our guard down is out of the question.*

After silently reminding himself of that, Inoue addressed the twenty intelligence operatives.

“Listen up. From this point on, we’ll infiltrate in pairs. Use hand signals to communicate, and fire the signal flare you’re carrying if there’s an emergency. You’ve all memorized your destinations and routes without missing anything, right?”

“Yes.”

“Good, then… we’ll meet back here in three hours. Dismissed.”

At Inoue’s words announcing the start of the operation, the intelligence operatives nodded and scattered in every direction. Watching them disappear silently and swiftly, his partner Sam jerked his chin toward the path ahead.

“Should we get moving too, ninja?”

“Yeah. You carefree Yankee bastard.”

“Don’t be like that. Your skills are the best. In three hours, you’ll be back after finding out even the color of the Arch Lich’s underwear.”

“…I really hope that’s true.”

With a quiet sigh, Inoue stepped forward. The pale fog covering all of Suining City clung damply to his entire body.

* * *

The advance of the five fronts, which had seemed as though it would never stop, finally came to a halt.

Two hundred kilometers from Suining City, where the Arch Lich was located, a welcome face came to visit us while we were resting and reorganizing.

“Hey, Korean friends. How have you been?”

I sensed a considerable wave of qi nearby, and sure enough, it was him. I bumped fists with Magic Johnson and answered.

“Pretty well.”

“Jin. My lovable Miracle Boy. I missed you.”

“Sorry, but could you leave out the ‘lovable’ part?”

“Then I’ll call you Crazy Boy. You did pull off something crazy, after all.”

Magic Johnson grinned as he added,

“It was also an incredibly heroic act. The same goes for Choi here.”

Team Leader Choi, who was carefully polishing Hero’s Soul, lowered his head slightly.

“It’s good to see you again, Mr. Johnson.”

“Choi, don’t be like that. You’re making things stiff.”

“……!”

“……!”

“Of course, I mean the atmosphere.”

Magic Johnson threw back his head and laughed.

At this point, it was obvious that he enjoyed watching our reactions. He was surprisingly playful for a man of his size.

Well, by now, we knew that everything was a joke whenever we met Magic Johnson.

Even Team Leader Choi, who always did Kegel exercises whenever he met him, gave a quiet laugh before asking,

“But what brings you here?”

“An emergency summons from headquarters. It’s an important matter.”

I frowned and muttered,

“This feels like déjà vu. Haven’t we seen this setup before?”

“Don’t worry, Jin. Nothing like last time will happen.”

By “nothing like last time,” he meant a situation where our main camp got completely wrecked while the S-rank Hunters were away.

Well, the distance between the fronts had narrowed now. Even if everyone gathered together, we were practically close enough to touch noses if we fell over, so it should be fine.

*They aren’t handling this over communications because it must be that important.*

As the Allied Forces continued winning and the monsters retreated, the Arch Lich’s territory had shrunk all the way back to Suining City. At our current location, both communications and magic worked smoothly.

“Do you know what we’re gathering for?”

“No. But I can guarantee that it won’t be a pleasant matter. I’ll stake my life on it.”

“……”

Please. Don’t stake your life on something like that. Give us a little more hope.

But Magic Johnson, as confident as ever, held out his hands toward Team Leader Choi and me.

“Anyway, everyone’s already there. You two are the last guests.”

“Then please lead the way, Mr. Johnson.”

Team Leader Choi took his hand without hesitation. Having already experienced Magic Johnson’s teleportation once, I nervously grabbed his fingers.

“Please drive safely—Gyaaaaaaaah!”

Whoosh!

Along with the sensation of my entire body being crushed like a soda can, I was flung into a new space.

“Gyaaaaaaa…”

“……”

“……”

Damn it. Of all places, it had to be here.

A dozen pairs of eyes stared at me in silence. Under the dumbfounded gazes of the S-rank Hunters and senior Chinese generals, I stopped screaming and quietly took a seat in an empty chair.

“Are we not starting the meeting?”

After a moment at a loss for words, Defense Minister Wei Fenghu finally spoke.

“…Then let us begin the meeting.”

The meeting that followed focused on a single subject: the information delivered by the sole survivor of the intelligence team.

“Daniel Inoue, who was in charge of the intelligence team, escaped from Suining City after eight hours—far beyond the scheduled operation time—and reported discovering a monster army numbering around thirty thousand.”

Thirty thousand…

It was an enormous force, but still within the range we had expected.

The Arch Lich’s monster army had suffered its first defeat a week ago and had been retreating helplessly ever since. In the process, it had been forced to endure tremendous losses.

“Judging by the minister’s expression, that isn’t all, is it?”

Few people here could speak to Minister Wei that casually. Lee Jungryong was one of them, and regardless of his personal feelings toward me, he had more than earned that right.

“Mr. Lee is correct. The estimate based only on what he personally witnessed is thirty thousand. The actual number…”

“Could be twice that, perhaps even more.”

“That is correct.”

“…Hmm.”

Low groans rose from several places around the room. We had expected the enemy to be holding back strength for the final battle, but not that much.

Wei Fenghu continued in a solemn voice.

“But most of the monsters are likely to be mid- or low-level. That is the one small consolation.”

“That applies to us too, Wei Fenghu.”

At the remark from Faye Chen, who had been silently sipping from a liquor glass, Prince Felix nodded.

“That is true. More troops than expected have joined our side, but it would be premature to assume victory.”

“Damn it. Those monsters never end, no matter how many we kill.”

I couldn’t help snorting at Wu Heixing’s grumbling.

“Why are you laughing?”

“Because it’s funny, you idiot.”

“What?”

“Anyone listening to you would think you’d been fighting incredibly hard. You’re the asshole who tried to take a detour during the monster army’s attack a week ago because you were afraid going there early might be dangerous.”

“……!”

His expression was a sight to behold.

He must have thought no one knew, but Wu Heixing’s disgrace had already spread across every front.

“I know you’ve had a rough time too, but don’t whine in front of me or everyone else. It’s starting to piss me off just looking at you.”

“Iik…!”[^1]

“What are you, self-employed? Why do you keep going *iik*?”

[^1]: *Iik* is an angry Korean grunt that sounds identical to the Korean word for “profit.”

Wu Heixing’s face turned bright red. His body twitched as though he might charge at me at any moment, but that was as far as he could go.

The bitter memory of defeat lasted a long time.

Even a hothouse flower that had spent its entire life being treated like royalty would wither in a cold wind.

Of course, there were flowers of an entirely different sort.

Like Team Leader Choi, sitting beside me.

“That’s enough, both of you.”

At Team Leader Choi’s calm intervention, Wu Heixing glared at him.

“Are you ordering me around?”

“If that’s how you took it, that’s unfortunate, Wu Heixing.”

“You…”

Wu Heixing shot to his feet at Team Leader Choi’s complete lack of reaction to his intimidation.

No, he tried to stand.

“Sit.”

“……!”

My aura shot out like an awl, and his body locked in place.

The other S-rank Hunters looked at me with startled eyes as well.

I glanced at Lee Jungryong’s deeply sunken gaze before continuing.

“Just so there’s no misunderstanding, yes, that was an order.”

“You, you…!”

“Sit. I’m not saying it again.”

Whoosh!

A wave of aura surged toward him, and Wu Heixing’s lower lip trembled.

Maybe he really was a genius, even by Murim standards.

No, he was. Becoming an S-rank Hunter in his thirties would have been impossible without that level of talent.

*But he was only half the package.*

Awakening was an unearned windfall. Like someone who had won the lottery, he had been granted extraordinary abilities and mana the moment he turned twenty.

And then he was supposed to build up internal energy like a Murim practitioner and learn Supreme Peak martial arts?

*Well…*

If he learned martial arts, it would make up for his technical shortcomings. But there was no doubt he would drop out long before he reached that point.

Compared to his talent, his effort and will were Third Rate.

“Enough.”

Lee Jungryong’s gentle baritone broke the tension.

The old snake, still looking like a handsome middle-aged man despite being well past sixty, watched me with a smile.

“I thought only your skills had improved, but your killing intent has grown stronger too.”

I met his eyes with an impassive gaze and replied,

“Rolling around in all sorts of places tends to put an edge on you.”

“I heard the western front was particularly fierce.”

“That’s not wrong. Want to come see the western front?”

“I must politely decline. If it was fierce enough that only three people survived, I think I’ll pass.”

“……!”

“The older I get, the more cowardly I become. Ho ho.”

The blood in my entire body seemed to turn cold.

The horrifying battlefield from that day flashed before my eyes, and before I knew it, a faint smile had formed at the corner of my mouth.

“What are you trying to say?”

“Let’s think about something more productive than attacking our own allies. Planning for the final battle would be a good place to start. Jin Taekyung, what do you think?”

I quietly tapped the armrest of my chair.

My stomach twisted, but Lee Jungryong’s words had struck the heart of the matter.

He was right. The battle bearing down on us was practically at our doorstep. That was what we needed to deal with now.

And then one thought came to me.

“A suicide squad.”

“A suicide squad?”

Everyone’s eyes turned toward me. Some nodded as though they agreed, while others looked uneasy.

But both my reason and my instincts were telling me that this was the best way to minimize our losses and win the battle.

“We gather our very best and take out the head.”

Once the Arch Lich is destroyed, the undead army will collapse.
```

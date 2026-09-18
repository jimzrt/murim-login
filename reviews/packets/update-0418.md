<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0418.txt",
      "sha256": "656bc7df40f767512893c6894418532d1cb2cf29fe9337ace4fd54fae3ec881f",
      "bytes": 13788
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "74b7f6ec0a0a379bbd52483f0a25fb63beb041e76ecfd3e1ef44245afe3ef76b",
      "bytes": 1728
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "0c65c80cca3b94ba7b9a821e4917bcc55788f61aae6d0adf00efe413959aaa83",
      "bytes": 139066
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "b84850573636a3c75435046f4f3b8207238319ad788e729fd6a54b515d9e4bf1",
      "bytes": 533
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "2c34726480e18553fbe830583f70081a45c29cc9949d5953018e315a397acb2b",
      "bytes": 1270
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "31bb4bf492ace988bb9618bf4971d447a9b12a748f36e2e78fc4ca701e292afd",
      "bytes": 622
    },
    {
      "path": "characters/Lee Jungryong.md",
      "sha256": "0870fdeefeb541c2c1519d23123bc19f572e08571ecf6df1dd646f437a1b022a",
      "bytes": 1178
    },
    {
      "path": "characters/Team Leader Choi.md",
      "sha256": "92b56017a62919450bc72b1cf9944a1149f0df7561bd3a8d7d22f3a1e1459bf7",
      "bytes": 535
    },
    {
      "path": "characters/Wu Heixing.md",
      "sha256": "316cb19de8db587af59ab213f0fd1bb51fe3abc5756c915920065ac44de9dc2d",
      "bytes": 762
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "940557f954a71b0f703d9dc184cddc2db5445f6e50fa5b0710904f654a04fb88",
      "bytes": 128217
    }
  ],
  "estimated_tokens": 11041
}
-->

# Durable State Update — Chapter 418

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 418. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 418. Profile updates may replace only one
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
  "chapter": 418,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 418,
    "continuity_sources": [418],
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
    "Lee Jungryong and Wu Heixing have openly betrayed Jin Taekyung and intended to use him as a disposable fighter against the Arch Lich.",
    "Wu Heixing fears the Arch Lich and planned to let Jin die, while Lee Jungryong seeks to prolong the war for personal gain.",
    "Jin Taekyung has begun fighting both Lee Jungryong and Wu Heixing, has wounded Lee, and currently holds Wu by the throat.",
    "Jin's memories of Lei Fei, the five hundred Public Security Armed Forces Department Hunters, Team Leader Choi, and Shao Shen have strengthened his resolve to risk himself against monsters.",
    "The city remains in the process of transforming into one enormous Gate through the Arch Lich's anchored mana.",
    "The Quest One Who Returned from Death remains active, keeping Login unavailable until the Quest ends.",
    "The Skeleton Warlord continues to suffer unexplained dizziness and nausea while urging Jin to turn back."
  ],
  "continuity_sources": [
    417
  ],
  "open_questions": [
    "Will Jin Taekyung kill Lee Jungryong and Wu Heixing, and will Wu survive Jin's grip?",
    "Can Jin defeat Lee and Wu and still confront the Arch Lich?",
    "Can the three Hunters stop the city's Gate transformation?",
    "What is causing the Skeleton Warlord's dizziness and insistence that they turn back?"
  ],
  "safe_through": 417,
  "temporary_decisions": [
    "Render 아크 리치 as Arch Lich.",
    "Render 게이트화 as Gate transformation.",
    "Render 어둠에 잠식된 도시 as City Consumed by Darkness.",
    "Render 죽음에서 돌아온 자 as One Who Returned from Death.",
    "Render 착짱죽짱 as “The only good chink is a dead chink.”"
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 최민우    | **Choi Minwoo**   |
| 이정룡    | **Lee Jungryong** |
| 열화문    | **Fire Gate Clan**               |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 심법     | **cultivation technique**                        | Especially internal cultivation                       |
| 초식     | **form**                                         | Numbered technique movement                           |
| 살기     | **killing intent**                               |                                                       |
| 장문인    | **Sect Leader**                              |
| 시스템              | **System**                     |
| 경험치              | **EXP**                        |
| 명성               | **Fame**                       |
| 헌터      | **Hunter**            |
| 길드      | **Guild**             |
| 팀장      | **Team Leader**       |
| 사천     | **Sichuan**            |
| 귀가      | **your family**                                                 |
| 공자      | **Young Master**                                                |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 우헤이싱 | **Wu Heixing** | Chinese S-rank Hunter who provokes Jin and nearly draws his sword. |
| 하연 | **Hayeon** | Jin Taekyung’s younger sister |
| 평화 | **Peace Guild** | Guild name. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 태자 | **Crown Prince** | Title of the Emperor's older brother who was reportedly assassinated. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 트롤 | **Troll** | Monster species with extraordinary regenerative ability. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 화룡신창 | **Fire Dragon Divine Spear** | Taekyung's spear technique, at the seventh stage in this chapter. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 중국 | **China** | Country from which Team Leader Choi’s video originates. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 대통령 | **President** | Title for Korea's head of state. |
| 주석 | **Chairman** | Political title used for Xiao Yang. |
| 화룡일미 | **Fire Dragon's Single Tail** | A form of the Fire Dragon Divine Spear. |
| 천격 | **Heavenly Strike** | A Fire Dragon Divine Spear form used by Taekyung against Hwangbo Eom. |
| 겁화 | **hellfire** | Destructive fire energy used by Taekyung. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 태자당 | **Crown Prince Party** | The faction associated with General Liao. |
| 푸린 | **Furin** | Russian president mentioned in a forum headline. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 하연 | 진태경 | younger_sister_to_older_brother | oppa | casual-familiar; pleading for important requests | Hayeon habitually puts 오빠 first when making an important request. |
| 진태경 | 하연 | older_brother_to_younger_sister | Sis | casual-familiar | Taekyung addresses Hayeon as 동생아 during their fly investigation. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 이정룡 | 진태경 | senior S-rank Hunter to younger Hunter and adversary | Young man | polished, teasing, and veiled-threatening | Uses a genial tone and indirect threats while trying to make Taekyung release the captives. |
| 진태경 | 이정룡 | younger Hunter to senior S-rank Hunter and adversary | you | polite but mocking and defiant | Taekyung answers Lee's soft threats with the wolf-and-tiger metaphor and refuses to yield. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 우헤이싱 | 진태경 | hostile S-rank Hunter to foreign Hunter and provocation target | peninsula bangzi | insulting and confrontational | Wu repeatedly addresses Jin with anti-Korean slurs. |
| 우헤이싱 | 이정룡 | younger S-rank Hunter to senior Ares Guild authority | Mr. Lee | formal and deferential | Wu addresses Lee respectfully despite his usual hostility toward Koreans. |
| 진태경 | 우헤이싱 | adversarial S-rank Hunters | you idiot | insulting-casual | Mocks Wu's cowardice and orders him to stop complaining. |
| 이정룡 | 우헤이싱 | senior S-rank Hunter to younger allied S-rank Hunter | Mr. Wu | polished and formally coaxing | Lee publicly draws Wu into agreement with the suicide-squad plan. |
| 최민우 | 진태경 | trusted allied team leader to younger allied Hunter | Mr. Jin | formal-polite and concerned | Choi warns Jin about the danger of the operation and affirms his deep trust. |
| 진태경 | 최민우 | younger allied Hunter to allied team leader | Team Leader Choi | polite, familiar, and teasing | Jin jokes with Choi while acknowledging and dismissing his concern. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 417
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who has sworn never to kill again.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 417
- **Aliases:** Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, and a Supreme Peak master who has manifested Force and crossed the wall into true mastery.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and student, his mother and sister Hayeon are among those he protects, and the Skeleton Warlord is his captive undead commander.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 417
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Lee Jungryong.md

# Lee Jungryong (이정룡)

- **Safe through:** Chapter 417
- **Aliases:** None
- **Role:** Vice Guild Master of Ares Guild, one of Korea's two S-rank Hunters, and a Supreme Peak-level martial artist who directs Ares Guild operations.
- **Personality:** Outwardly genial, calm, and humorous; calculating, opportunistic, manipulative, coercive, and ruthless when challenged
- **Voice:** Smooth, good-natured, and indirect, using teasing conversation and veiled threats before becoming openly furious
- **Relationships:** Master of Park Jihoon and Go Jun (Team Leader Seok), whom he personally selected and trained; longtime Great Cataclysm acquaintance of Park Tae Seop; adversary of Jin Taekyung; knew Team Leader Choi from childhood; has an antagonistic history with Kim Hwajong, who saved his life at the collapse of Mapo Bridge eighteen years earlier; was visibly shaken by learning that Choi is Cheon Taemin's maternal grandson; regards Cheon Taemin as an older brother despite no blood relation and has long held him in respect and fear; operates as Ares Guild's senior authority beneath its Guild Master

### Team Leader Choi.md

# Team Leader Choi

- **Safe through:** Chapter 417
- **Aliases:** Choi Minwoo (최민우)
- **Role:** Allied team leader and Hunter who analyzes battlefield conditions during the Arch Lich operation.
- **Personality:** Calm, analytical, and steady under extreme battlefield pressure.
- **Voice:** Measured and logical, using clear tactical explanations.
- **Relationships:** Works alongside Jin Taekyung and Lee Jungryong in the coalition against the Arch Lich.

### Wu Heixing.md

# Wu Heixing (우헤이싱)

- **Safe through:** Chapter 417
- **Aliases:** None
- **Role:** Wu Heixing is a Chinese S-rank Hunter known for frequent media exposure and scandal who secretly practices martial arts, including an internal-energy cultivation technique and fist-and-foot martial arts.
- **Personality:** Arrogant, status-conscious, abusive, and fiercely proud of his power, he responds to humiliation with anger and protects himself even while his allies die.
- **Voice:** Loud, insulting, entitled, and dependent on national and political status.
- **Relationships:** He is openly hostile toward Jin Taekyung and Faye Chen, and resents Jin receiving Chairman Shao Yang's attention.

## Korean source

```text
＃418화



가끔 누군가의 목숨을 거둘 때마다, 목숨을 구걸하는 적들의 간절한 목소리와 눈빛을 마주할 때마다 그런 의문이 들고는 했다.

도대체, 왜, 어째서.

지금껏 스스로가 했던 행동들을 생각하지 않는지. 모든 일에 존재하는 인과를 남에게서 찾으려 하는지.

‘늦었어.’

누군가를 죽이고자 했다면 그 반대의 경우도 생각해야 하는 법.

이미 씨는 뿌려졌고, 마침내 수확의 시간이다.

나는 우헤이싱의 핏발 선 눈동자를 응시하며 속삭였다.

“내가 왜 그런 위험을 감수해야 하지?”

「……!」

대답을 듣기 위해 던진 물음은 아니었다.

더 이상 들을 것도, 볼 것도 없다. 나는 망설임 없이 우헤이싱의 목줄기를 잡아 비틀었다.

우두둑.

강철도 종잇장처럼 찢어 버리는 악력에 살이 짓이겨지고 뼈가 조각난다.

부릅뜬 채 굳어 버린 놈의 눈동자에서 마지막 빛이 빠져나갔다.

버둥거리던 몸이 축 늘어짐과 동시에, 시스템 알림이 울렸다.

띠링.



- [Lv.135 우헤이싱]을 처치했습니다!

- 상당량의 경험치를 얻었습니다!

- 명성치를 얻지 못했습니다. 해당 인물을 처치한 것이 알려진다면 상당한 파장이 예상됩니다!



바로 그때였다. 이십여 미터 밖에서 신형을 일으켜 세운 이정룡이 입을 연 것은.

“한 치의 망설임도 없구나.”

나는 숨이 끊긴 우헤이싱을 내던지며 대답했다.

“죽여야 할 놈이었으니까.”

“저 아이의 아비가 누구인지 아느냐?”

“들어 보긴 했지. 수십 년 전쯤 공자 묘에 오함마 내리찍던 놈 중 하나였다고.”

“그리고 그 어린 홍위병은 자라 중국 정치계의 최고 거물이자 태자당의 우두머리가 되었지. 샤오 양 주석도 감히 그를 어쩌지 못해.”

“캬, 시벌. 어메이징 대륙이네. 우리나라로 치면 숭례문 방화범이 대통령 된 거 아냐. 안 그래?”

“이해하려 할 필요는 없다. 다만 한 가지 알아야 할 사실은, 10억 인구 중 가장 강력한 권력자가 쉰이 넘어서야 얻은 외동아들을 네 손으로 죽였다는 게다.”

“내가? 아니지.”

나는 천연덕스럽게 웃었다.

“우헤이싱은 아크 리치와 접전을 벌인 끝에 사망한 거야.”

“……!”

“말했잖아, 묘비명도 정해 뒀다고. 나쁜 짱깨, 착한 중국인이 되어 이곳에 잠들다. 물론 그 옆에는 당신 묘비가 있을 거고.”

알 수 없는 표정으로 나를 바라보던 이정룡이 피식 실소를 흘렸다.

“교활한 놈이로고.”

“너희가 짠 시나리오 괜찮더라. 내가 좀 쓰자.”

“마음대로 하거라. 어차피 네 뜻대로 되진 않을 테니.”

“글쎄…….”

나는 널브러진 우헤이싱의 시신을 턱짓으로 가리키며 말을 이었다.

“지금까지는 어느 정도 내 뜻대로 된 것 같은데?”

“그래, 그 부분만큼은 나와 같구나.”

“뭐?”

눈살을 찌푸린 나를 바라보며, 이정룡이 잔잔하게 웃었다.

“우헤이싱은 귀가 얇고 입이 가벼운 놈이지. 함께 무언가를 도모하기에는 형편없지만, 그런 놈이라 해도 이용할 구석은 충분하다.”

“……무슨 개소리야?”

“말하자면, 이런 뜻이지.”

이정룡이 손에 든 무언가를 누르자, 짙은 안개 사이를 뚫고 콘크리트 조각에 닿은 빔이 홀로그램을 띄웠다.

10초 남짓한 짧은 홀로그램 영상에는 목숨을 애걸하는 우헤이싱과 한 치의 망설임도 없이 목을 꺾는 내 모습이 그대로 담겨 있었다.

“허.”

나는 헛웃음과 함께 입을 열었다.

“화질 좋네. 누가 보면 오해하기 딱 좋은 영상 같아.”

“그렇지. 늦둥이 외아들을 잃은 늙은 아버지라면 특히.”

“무편집본으로 보여 줄 생각은?”

“마력의 영향 때문인지, 아마 오작동으로 인해 영상의 앞부분이 날아갈 것 같구나.”

“그거참, 우연치고는 기가 막히네.”

“이걸 본 사람이라면 누구나 기가 막힐 수밖에 없을 터. 평소 헐뜯기 좋아하는 이들은 물론이고, 널 신봉하던 이들조차 돌아서겠지. 네가 그토록 아끼는 사람들도 대중의 비난 속에서 서서히 무너질 게다.”

평화 길드, 그리고 엄마와 하연이.

이정룡의 말을 듣는 순간 눈앞을 스쳐 지나간 이름과 얼굴들이다.

나는 우헤이싱의 시신을 밟으며 걸음을 내디뎠다.

저벅.

“처음부터 이럴 생각이었나?”

“애당초 우헤이싱은 도구였을 뿐, 그 이상의 존재가 될 수 없었다.”

저벅.

이정룡 역시 나를 향해 걸음을 옮겼다.

하지만 그의 전신에서 흘러나오는 기운은 지금까지에 비할 바가 아니었다.

그것이 우헤이싱의 죽음에도 이정룡이 평정심을 잃지 않을 수 있었던 이유였다.

목적을 달성한 교활한 맹수가, 비로소 숨겨 둔 발톱을 꺼낸 것이다.

“빌어먹을, 어쩐지 쉽더라니.”

내 푸념에 이정룡이 메마른 웃음을 지었다.

“한 가지는 칭찬해 주마. 넌 내 예상을 훨씬 뛰어넘었어.”

“마지막으로 묻자. 도대체 왜 이렇게까지 하는 거지?”

“너 같은 핏덩이가 짐작이나 할 수 있을까.”

저벅.

“최 팀장, 아니 최민우가 그렇게 겁났나?”

“그 입, 닥치지 못할까.”

콰아아아아!

순간 밀어닥친 거대한 기파가 안개를 밀어 내고 공간을 장악한다.

예리하게 날 선 살기에 피부가 따끔거렸다. 잔잔하던 이정룡의 눈동자 위에는 지금껏 볼 수 없었던 노기가 떠올라 있었다.

“오롯이 내 힘으로 얻어 낸 자리다. 평생에 걸쳐 쌓아 올린, 나만의 제국이란 말이다!”

그건 꾹꾹 눌러 왔던 분노였고, 실로 오랜만에 표출하는 감정이었다.

이정룡은 불길이 쏟아지는 듯한 눈빛으로 나를 노려보며 한 음절, 한 음절 씹듯이 내뱉었다.

“그 누구도 무너트릴 수 없다. 너도, 민우 그 아이도, 그리고…… 설령 형님조차도!”

형님?

난데없이 튀어나온 그 두 글자에 대해 의문을 표할 시간은 내게 주어지지 않았다.

저벅.

유난히 무겁고 깊은 소리를 남긴 한 걸음.

동시에 이정룡의 신형이 물처럼 일렁였다.

잔상(殘像)을 남긴 채 사라진 맹수는 어느새 코앞으로 다가와 있었다.

쉬이이이잉!

눈앞을 가득 메운 빛무리. 나는 허리를 비틀며 백염(白炎)을 휘둘렀다.

빛과 화염이 맞닿은 순간, 하늘이 갈라지는 듯한 굉음이 울려 퍼졌다.

꽈아아앙!



* * *



폭발은 거대했다.

간신히 버티고 있던 고층 빌딩이 터져 나가듯 무너지고, 유리와 콘크리트가 셀 수도 없을 만큼 작은 조각으로 분해되어 사방을 꿰뚫었다.

수십 킬로미터 밖에서도 느껴질 법한 격돌의 여파.

연달아 이어지는 붕괴와 굉음 속에서, 나는 발을 뻗었다.

쉬익!

갈라지는 먼지구름 너머로 허공을 딛고 우뚝 선 한 사람이 모습을 드러냈다.

언제나 속을 짐작할 수 없던 투명한 눈동자는 불길을 토해 내고 있었다.

“진태경-!”

누가 먼저랄 것도 없었다.

나는 지면을 부수며 솟구쳤고, 그는 허공을 밟으며 내리꽂혔다.

서로를 향해 휘두른 검과 창의 궤적이 정확히 맞닿은 순간, 어마어마한 충격파가 전신을 휩쓸었다.

약속이라도 한 것처럼 동시에 튕겨 나간 우리는, 이미 폐허가 된 도시의 구조물을 밟으며 재차 쏘아졌다.

쐐애애애액, 꽈앙!

굉음과 함께 창날을 흘려 낸 검 끝이 곧장 목젖을 향해 찔러 들어왔다.

펑!

고개를 틀자 파공성과 함께 잘려 나간 머리카락이 흩날린다.

하지만 이것으로 끝이 아니었다.

쉬쉬쉬쉭!

이정룡의 검이 새하얀 빛이 되어 쏘아졌다.

검신을 타고 흘러나온 강기(罡氣)의 그물.

눈앞을 가득 메운 빛의 향연에, 나는 단전에 잠들어 있던 모든 공력을 깨웠다.

삼 갑자의 열양지기가 들불처럼 일어나 사지백해로 스며든다. 투명한 창날을 타고 솟아오른 푸른 겁화가 용의 꼬리처럼 부드럽게 일렁였다.

‘화룡일미(火龍一尾).’

후우우웅!

단 한 번의 휘두름.

부챗살처럼 뻗어 나간 화룡의 꼬리에 쇄도하던 강기의 일부가 사라졌다.

이제는 날카로운 발톱으로 헐거워진 그물을 찢어 버릴 차례다.

‘천격(天格).’

고작 두 초식으로 이루어진 화룡신창(火龍神槍).

그러나 화룡신창을 창안한 열화문의 옛 장문인은 천하제일창이라는 수식어를 얻었고, 생애 마지막 순간 자신의 무공에 대한 짤막한 유언을 남겼다.



‘일평생을 바쳤지만 완성하지 못한 무공. 그럼에도 천하제일이라 부를 수 있는 창술.’



그의 말은 사실이었다.

화룡신창은 그런 무공이다. 단 두 초식만으로도 천하제일이라 자부할 수 있는 창술, 그리고…….

콰아아아아!

전력이 실린 천격이 강기의 그물을 찢고 전방을 휩쓸었다.

어찌할 새도 없이 순식간에 들이닥친 화염을 바라보던 이정룡이 힘찬 기합과 함께 검을 내리그었다.

“합!”

쉬익!

검 끝에 화염이 갈라졌다.

좌우로 생겨난 불꽃의 길을 따라 화살처럼 쏘아진 신형이 무수한 검격을 쏟아 냈다.

슈슈슈슈슉!

가슴, 목, 어깨, 팔과 다리…….

찰나라고 부를 수 있을 만큼 짧은 시간 속.

빛살처럼 휘두르고 베어지는 검의 궤적 앞에서, 나는 문득 경이로움에 사로잡혔다.

‘어떻게, 어떻게 이럴 수 있지?’

나는 헌터다. 동시에 무인이기도 하다.

아니, 어쩌면 플레이어(Player)라는 이름이 어울리는 존재일지도 모른다.

무더운 여름날 분리수거장에 버려진 VR 캡슐을 주운 날, 시스템이라는 이름의 새로운 힘을 얻었으니까. 현대와 무림을 아우르는 유일한 존재가 되었으니까.

하지만…….

쾅!

한 치의 군더더기도 없는 움직임, 완벽에 가까운 힘의 조절, 그리고 기의 컨트롤까지.

이정룡의 공격을 받아친 나는 내심 감탄했다. 그것은 이정룡이 어떤 사람인가를 떠나, 그가 갖춘 실력에 대한 놀라움이었다.

‘이 정도일 줄이야.’

초절정의 경지에 오른 뒤, 현대에서 나를 상대할 만한 사람은 많지 않을 거라 생각했다.

그리고 사천에 와서 여러 S급 헌터들을 만난 후 그런 생각은 더더욱 굳어졌다.

그들 개개인이 품은 기운이 아무리 크다 할지라도, 이곳에는 무공이 존재하지 않으니까.

소위 말해 헌터라는 이들은 효율적인 전투를 할 뿐, 효율적인 기의 운용에 있어서 까막눈이나 다름없었다.

이정룡? 현대에서는 마나 연공법이라 불리는 심법을 익혔다지만, 크게 다르지 않을 것이라 생각했다.

그리고 지금 깨달았다.

내 오만함이, 잘못된 판단을 낳았다는 것을.

서걱!

허벅지가 시원해지더니, 이내 불길처럼 뜨거운 고통이 잇따랐다.

하지만 어째서일까, 긴 잠에서 깬 것처럼 정신이 들고 눈앞이 맑아지는 이유는.

서걱, 서걱, 서걱!

팔, 종아리, 그리고 목덜미.

핏물이 솟구치고, 강기를 통해 유입된 기운에 공력이 흐트러진다.

비틀거리는 나를 향해 끊임없이 검격을 쏟아붓는 이정룡의 얼굴을 바라보았다.

땀으로 번들거리는 이마, 동시에 승리를 확신하는 듯한 눈빛과 입가에 걸린 미소.

‘아, 마음에 안 드네.’

저 웃음도, 저런 인간이 이 정도의 힘을 가졌다는 사실도 마음에 들지 않는다. 나는 울컥 솟구치는 무언가를 느끼며 백염을 휘둘렀다.

꽈앙!

일 합.

앞서 베인 상흔에서 피가 흐르고 고통이 전해졌다. 그러나 나는 말없이 재차 창을 내질렀다.

한 걸음 물러났던 이정룡이 담담한 미소를 지으며 부딪쳐 왔다.

쾅!

이 합.

두 걸음을 물러난 이정룡이 뜻밖이라는 얼굴로 나를 바라보았다.

아직도 그런 힘이 남아 있었나? 표정 위로 고스란히 드러난 그의 생각을 읽을 수 있었다.

‘그야 물론이지.’

나는 내심 중얼거리며, 창을 고쳐 쥐고 미약하게 전해져 오는 통증을 무시하며 발을 내디뎠다.

쾅! 쾅! 꽈앙!

세 번, 네 번, 다섯 번.

창과 검이 부딪치고 굉음이 터져 나올 때마다 이정룡의 안색이 굳는다.

입가에 맺혀 있던 미소는 사라진 지 오래였다.

“놈……!”

평소 고양이 발바닥처럼 부드럽던 목소리 대신, 으르렁거리는 듯한 외침을 들으니 왠지 모르게 웃음이 나왔다.

스스로의 힘에 도취된 나는 그의 실력을 과소평가하는 오판을 저질렀지만, 그건 이정룡 역시 마찬가지다.

이정룡이 드러낸 발톱은 충분히 강하고 날카로우나, 내 숨통을 끊어 놓기에는 역부족이었다.

“정룡아.”

크게 숨을 들이켜자 퀴퀴한 공기와 악취가 밀려온다. 그럼에도 속이 뻥 뚫린 것처럼 후련했다.

그래, 이제야 알겠다.

“발톱 자르자.”

이정룡은 오늘, 이 자리에서 죽는다.
```

## Final English reading copy

```markdown
# Chapter 418

Sometimes, whenever I took someone's life, whenever I met the desperate voices and eyes of enemies begging for their lives, I found myself wondering.

*Why? Why on earth?*

Why didn't they stop to think about what they themselves had done? Why did they look to others for the causes of everything that happened?

*Too late.*

If you tried to kill someone, you had to consider the possibility of the opposite happening, too.

The seeds had already been sown, and at last, it was time to harvest.

I stared into Wu Heixing's bloodshot eyes and whispered,

“Why should I take that kind of risk?”

「……!」

I hadn't asked the question to hear an answer.

There was nothing more to hear or see. Without hesitation, I grabbed Wu Heixing by the neck and twisted.

*Crunch.*

Flesh was crushed and bones splintered beneath a grip strong enough to tear steel like paper.

The last light faded from his wide, frozen eyes.

As his struggling body went limp, a System notification rang out.

> **System**
>
> - Defeated **Lv. 135 Wu Heixing**!
> - Gained a substantial amount of **EXP**!
> - Gained no **Fame**. If it becomes known that you killed this person, significant repercussions are expected!

That was when Lee Jungryong, who had been standing more than twenty meters away, rose to his feet and spoke.

“You don't hesitate at all.”

I threw Wu Heixing's lifeless body aside and answered,

“He was someone who needed to die.”

“Do you know who that boy's father is?”

“I've heard of him. Apparently, he was one of the men who took a sledgehammer to Confucius's tomb decades ago.”[^1]

“And that young Red Guard grew up to become the most powerful man in Chinese politics and the leader of the Crown Prince Party. Even Chairman Shao Yang dares not touch him.”

“Damn, this continent is fucking amazing. In our country, it'd be like the arsonist who burned down Sungnyemun becoming President. Don't you think?”

“There is no need to try to understand it. But there is one fact you must know. You killed, with your own hands, the only son that the most powerful man among one billion people had after turning fifty.”

“I did? No, I didn't.”

I smiled shamelessly.

“Wu Heixing died after engaging in a fierce battle with the Arch Lich.”

“……!”

“I told you, I already decided on the epitaph. *The only good chink is a dead chink.* Of course, your gravestone will be right beside his.”

Lee Jungryong stared at me with an inscrutable expression, then let out a quiet laugh.

“You're a crafty one.”

“I liked the scenario you two came up with. Let me use it.”

“Do as you please. It won't go according to your wishes anyway.”

“Maybe…”

I continued, gesturing toward Wu Heixing's sprawled corpse with my chin.

“So far, it looks like things have gone more or less according to my wishes.”

“Yes. In that respect, you're like me.”

“What?”

As I frowned, Lee Jungryong gazed at me with a faint smile.

“Wu Heixing is easily swayed and loose-lipped. He's a terrible choice for plotting anything together, but even a man like that has his uses.”

“...What the fuck are you talking about?”

“In other words, this is what I mean.”

When Lee Jungryong pressed something in his hand, a beam pierced through the thick fog and struck a piece of concrete, projecting a hologram.

The short holographic video, barely ten seconds long, showed Wu Heixing begging for his life and me breaking his neck without a moment's hesitation.

“Huh.”

I let out a hollow laugh.

“That's some good image quality. The kind of video that would be perfect for giving people the wrong idea.”

“Exactly. Especially for an old father who has lost his late-born only son.”

“Are you planning to show them the unedited version?”

“Perhaps because of the mana's influence, an error will probably cause the beginning of the video to be lost.”

“What an incredible coincidence.”

“Anyone who sees this will have no choice but to be outraged. Not only those who enjoy slandering others, but even the people who worshipped you will turn away. The people you cherish so dearly will slowly crumble beneath the public's condemnation.”

The Peace Guild.

And Mom and Hayeon.

Those were the names and faces that flashed before my eyes the moment I heard Lee Jungryong's words.

I stepped forward, pressing my foot onto Wu Heixing's corpse.

*Step.*

“Did you plan this from the beginning?”

“Wu Heixing was merely a tool from the start. He could never become anything more.”

*Step.*

Lee Jungryong also began walking toward me.

But the qi flowing from his entire body was on an entirely different level from before.

That was why he had remained calm even after Wu Heixing's death.

The crafty beast had achieved its objective and finally drawn the claws it had kept hidden.

“Damn it. No wonder it seemed so easy.”

At my complaint, Lee Jungryong gave a dry laugh.

“I'll praise you for one thing. You far exceeded my expectations.”

“Let me ask one last time. Why are you going this far?”

“Could a brat like you possibly guess?”

*Step.*

“Were you really that afraid of Team Leader Choi—no, Choi Minwoo?”

“Can't you shut that mouth of yours?”

*Kuwaaaaaaaang!*

A massive wave of energy surged forth, driving back the fog and seizing control of the space.

The sharply honed killing intent made my skin prickle. Anger unlike anything I had ever seen rose in Lee Jungryong's formerly placid eyes.

“This is a position I earned entirely through my own strength. An empire of my own, built over the course of my entire life!”

It was anger he had kept pressed down, an emotion he was expressing for the first time in a very long while.

Lee Jungryong glared at me with eyes that seemed to pour fire and spat out each syllable as though chewing on it.

“No one can bring it down. Not you, not that boy Minwoo, and... not even my hyung!”

Hyung?

I wasn't given time to question that unexpected word.

*Step.*

One step left behind an unusually heavy, profound sound.

At the same time, Lee Jungryong's form rippled like water.

The beast that vanished, leaving behind an afterimage, had already arrived right in front of me.

*Fweeeeeeeeng!*

A mass of light filled my vision. I twisted my waist and swung White Flame.

The moment light and flame collided, a thunderous roar rang out as though the sky itself had split apart.

*Kwaaang!*

* * *

The explosion was enormous.

The high-rise building that had barely been holding together collapsed as if it had burst apart, while glass and concrete broke into countless tiny fragments that pierced through everything in every direction.

The aftershock of the clash was powerful enough to be felt dozens of kilometers away.

Amid the successive collapses and thunderous booms, I thrust out my foot.

*Fwish!*

Beyond the split dust cloud, a man standing tall in midair appeared.

His transparent eyes, which had always been impossible to read, were spewing flames.

“Jin Taekyung!”

Neither of us waited for the other.

I shattered the ground as I leaped upward, while he stepped on empty air and drove himself downward.

The trajectories of the sword and spear we swung at each other met with perfect accuracy, and an immense shock wave swept across our bodies.

We were hurled backward at the same time, as though we had planned it. Then we kicked off the structures of the already-ruined city and shot toward each other again.

*Shweeeeeek—Kwang!*

With a thunderous boom, Lee Jungryong's sword swept my spearhead aside and thrust straight toward my throat.

*Boom!*

I twisted my head aside, and severed strands of hair scattered through the air with a sharp whistle.

But it wasn't over.

*Shwish-shwish-shwish!*

Lee Jungryong's sword shot forward as a streak of pure white light.

A net of Force flowed along the blade.

Faced with a spectacle of light filling my vision, I awakened all the internal energy sleeping in my dantian.

Three jiazi of Scorching Yang Qi rose like a wildfire and seeped into my four limbs and hundreds of bones. Blue hellfire surged along the transparent spearhead, rippling smoothly like a dragon's tail.

*Fire Dragon's Single Tail.*

*Whoooooosh!*

A single swing.

Part of the Force rushing toward me vanished beneath the fire dragon's tail, which spread outward like the ribs of a fan.

Now it was time to tear apart the loosened net with sharp claws.

*Heavenly Strike.*

The Fire Dragon Divine Spear consisted of only two forms.

And yet the former Sect Leader of the Fire Gate Clan who created it earned the epithet of the greatest spearman under heaven, leaving behind a brief final testament about his martial arts.

*“A martial art I devoted my entire life to but failed to complete. Even so, it is a spear art worthy of being called the greatest under heaven.”*

His words had been true.

That was what the Fire Dragon Divine Spear was. A spear art that could proudly call itself the greatest under heaven after only two forms, and...

*Kuwaaaaaang!*

Heavenly Strike, unleashed with all my power, tore through the net of Force and swept across everything ahead of it.

Lee Jungryong, watching the flames rush toward him in an instant before he had any chance to react, brought his sword down with a powerful shout.

“Ha!”

*Fwish!*

The flames split at the tip of his sword.

His form shot forward like an arrow along the paths of flame that opened to either side, unleashing countless sword strikes.

*Shu-shu-shu-shu-shuk!*

Chest, throat, shoulder, arms, legs...

Within a span of time so short it could be called an instant—

As I faced the sword's trajectories, swinging and cutting like rays of light, I was suddenly seized by wonder.

*How? How can this be possible?*

I was a Hunter. At the same time, I was a martial artist.

No. Perhaps I was a being better suited to the name *Player*.

On a sweltering summer day, I had picked up a discarded VR capsule at a recycling station and gained a new power called the System. I had become the only being who stood astride both the modern world and the Murim.

But still...

*Boom!*

Movements without a single wasted inch, nearly perfect control of power, and even control over qi.

After parrying Lee Jungryong's attack, I was inwardly amazed. It had nothing to do with what kind of person Lee Jungryong was. I was simply stunned by the skill he possessed.

*So he was this strong.*

After reaching the Supreme Peak realm, I had thought there would not be many people in the modern world capable of matching me.

After coming to Sichuan and meeting several S-rank Hunters, that belief had only grown stronger.

No matter how much energy each of them possessed, martial arts did not exist here.

The so-called Hunters could fight efficiently, but when it came to efficient qi manipulation, they were practically illiterate.

Lee Jungryong? I knew he had learned a cultivation technique called a mana cultivation technique in the modern world, but I had assumed it wouldn't be much different.

And now I realized it.

My arrogance had led me to the wrong conclusion.

*Shlack!*

My thigh suddenly felt cool, followed by a pain as hot as fire.

But why did my mind clear and my vision sharpen as though I had just awakened from a long sleep?

*Shlack, shlack, shlack!*

My arm, calf, and the back of my neck.

Blood spurted out, and the qi carried through his Force disrupted the flow of my internal energy.

I looked at Lee Jungryong's face as he continued raining sword strikes down upon me while I staggered.

His forehead glistened with sweat. At the same time, his eyes seemed certain of victory, and a smile hung at the corners of his mouth.

*Ah, I don't like this.*

I didn't like that smile. I didn't like the fact that a man like him possessed this level of strength.

Feeling something surge up inside me, I swung White Flame.

*Kwaang!*

The first clash.

Blood flowed from the cuts inflicted earlier, and pain spread through me. But without a word, I thrust the spear forward again.

Lee Jungryong, who had stepped back, charged into me with a calm smile.

*Boom!*

The second clash.

Lee Jungryong stepped back twice and looked at me with an expression of surprise.

*Did he still have that much strength left?*

His thoughts were written plainly across his face.

*Of course I do.*

I muttered inwardly, adjusted my grip on the spear, ignored the faint pain spreading through me, and stepped forward.

*Boom! Boom! Kwaang!*

Three times. Four times. Five times.

Each time spear and sword collided and thunderous roars burst forth, Lee Jungryong's expression grew harder.

The smile that had lingered around his mouth had disappeared long ago.

“You bastard...!”

Hearing that growling shout instead of the voice that was usually as soft as a cat's paw somehow made me laugh.

Intoxicated by my own strength, I had underestimated his abilities and made a foolish mistake.

But Lee Jungryong had done the same.

The claws he had revealed were certainly strong and sharp, but they weren't enough to finish me off.

“Jungryong.”

I drew in a deep breath, and stale air and a foul stench flooded my lungs.

Even so, I felt refreshed, as though something inside me had been blown wide open.

Yes. Now I understood.

“Let's clip those claws.”

Lee Jungryong would die here today.

[^1]: The reference is to the Red Guards' attack on Confucius's tomb during the Cultural Revolution.
```

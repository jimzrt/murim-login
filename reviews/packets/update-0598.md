<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0598.txt",
      "sha256": "4257e16333574d9b05ee92c743deb8a41ebe1ac74eae34d80959007066734b8d",
      "bytes": 12972
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "a0a365d3729be8b5902b29740d78cadb39f518a94ebdef4709bc1cc788a2383c",
      "bytes": 1253
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "72e05f2585e78105b93d649d7ba968d745458df9a21a30d6354e4b90322089ca",
      "bytes": 185422
    },
    {
      "path": "characters/Go Jun.md",
      "sha256": "90586e3bbf31757f6d46647bf6727ecdae82587125c2fe3bfcfee3b13e4e9656",
      "bytes": 817
    },
    {
      "path": "characters/Go Se-won.md",
      "sha256": "b50cc30f24ba98638b286615b394ece93cee832dff1e31eab63a6551519dfae6",
      "bytes": 880
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "0e10f2f2db243f4146f876b6663921c3be463b0ae17fff3ac8618bed6ee36781",
      "bytes": 1672
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "58468076c963d5dae2fcb8403f0415f2f7b67dec66b7ff9461cc57d2ea2c3acb",
      "bytes": 622
    },
    {
      "path": "characters/Lee Jungryong.md",
      "sha256": "21849d399bf53a3729586dfb6a3616430416bb008c8b3cb5cfd029d6d06d7dbd",
      "bytes": 1384
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "001235945cdf33b045e7990829e346a113f1ad9297fb827ecf61632549abaa12",
      "bytes": 183850
    }
  ],
  "estimated_tokens": 10590
}
-->

# Durable State Update — Chapter 598

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 598. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 598. Profile updates may replace only one
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
  "chapter": 598,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 598,
    "continuity_sources": [598],
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
    "Team Leader Choi regards Kim Hwajong as family and is grieving his death, finally breaking down after Jin leaves the room.",
    "President Baek Hanseong has assigned a temporary security detail to protect Jin and his family while the current crisis settles.",
    "Jin remains booked without detention; the main allegation concerns injuries to more than five hundred casualties, while self-defense is likely to be recognized.",
    "Go Se-won is being held in a special detention center and has requested a meeting with Jin to repay a debt.",
    "Jin decides to visit Go Se-won and accepts an escort from the President's security detail."
  ],
  "continuity_sources": [
    597
  ],
  "open_questions": [
    "What debt does Go Se-won intend to repay to Jin?",
    "What will Go Se-won reveal when Jin visits him?",
    "How will the authorities ultimately resolve the charges against Jin?"
  ],
  "safe_through": 597,
  "temporary_decisions": [
    "Use Team Leader Choi for 최 팀장.",
    "Use Butler Kim for 김 집사.",
    "Use Skeleton King for 스켈레톤 킹.",
    "Use President's Security Service for 대통령 경호실.",
    "Use booked without detention for 불구속 입건."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 이정룡    | **Lee Jungryong** |
| 무인     | **martial artist**                               | Default term                                          |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 장비               | **Equipment**                  |
| 헌터      | **Hunter**            |
| 길드      | **Guild**             |
| 길드장     | **Guild Master**      |
| 부길드장    | **Vice Guild Master** |
| 팀장      | **Team Leader**       |
| 탱커      | **tank**              |
| 고준 | **Go Jun** | Personal name of Team Leader Seok; Lee Jungryong's prized Disciple. |
| 고세원 | **Go Se-won** | Ares Guild Head of Security and Team Leader. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 아레스 | **Ares Guild** | The leading Guild in Korea; formerly employed Team Leader Choi and Song Song. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 청와대 | **Blue House** | Presidential office mentioned in an online comment about proposed legislation. |
| 검찰 | **prosecutors’ office** | Government prosecutorial institution that summons and investigates Taekyung. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 준이 | **Jun** | Family nickname used in the form Jun's dad. |
| 석고준 | **Go Jun** | Source full-name form for the established Go Jun, also known as Team Leader Seok. |
| 경호팀장 | **Head of Security** | Go Jun's security-team office under Lee Jungryong. |
| 대통령 | **President** | Title for Korea's head of state. |
| 중화 | **Zhonghua** | Patriotic term used in Shao Shen’s rallying speech. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 화기 | **fire qi** | The fire nature imparted to internal energy by the Fire Gate Divine Technique. |
| 상호 | **Sangho** | Go Se-won's young son. |
| 정룡 | **Jungryong** | Cheon Taemin's trusted associate who joined the Peace Guild. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 이정룡 | 진태경 | senior S-rank Hunter to younger Hunter and adversary | Young man | polished, teasing, and veiled-threatening | Uses a genial tone and indirect threats while trying to make Taekyung release the captives. |
| 진태경 | 이정룡 | younger Hunter to senior S-rank Hunter and adversary | you | polite but mocking and defiant | Taekyung answers Lee's soft threats with the wolf-and-tiger metaphor and refuses to yield. |
| 이정룡 | 고준 | Master to Disciple | Go Jun | familiar and testing | Lee switches from Seok's office title to his personal name while considering whether he can defeat Taekyung. |
| 고준 | 이정룡 | Disciple to Master | Master | deferential | Go Jun responds to Lee's personal-name address as 스승님. |
| 진태경 | 석고준 | returning Hunter to hostile Ares security leader | you fucking bastard | hostile and profane | Taekyung directs his final insults and challenge at Go Jun after returning alive. |
| 석고준 | 진태경 | hostile_opponents | brat | hostile and overconfident | Go Jun addresses Taekyung internally as 애송아 while launching his full-strength attack. |
| 고준 | 진태경 | Ares Guild combatant confronting the killer of his Master | you | hostile and informal | Go Jun uses 너 while demanding Jin confess to Lee Jungryong's death and threatening retaliation. |
| 진태경 | 고준 | dominant adversary confronting Lee Jungryong's Disciple | you | contemptuous and informal | Jin uses 너 and 놈 while overpowering Go Jun and ordering him to end the conflict with Lee Jungryong. |
| 진태경 | 대통령 | Hunter_to_President | Mr. President | formal-polite | Taekyung addresses the President respectfully during their airport greeting. |
| 대통령 | 진태경 | President_to_Hunter | Mr. Jin Taekyung | formal-polite | The President addresses Taekyung by name at the airport photo line. |
| 석고준 | 고세원 | Ares Vice Guild Master to Head of Security | you | curt and informal | Go Jun tells Go Se-won that he is later than usual when Se-won enters the wrecked office. |
| 고세원 | 석고준 | subordinate_to_Vice_Guild_Master | Vice Guild Master | formal-deferential | Uses 부길드장님 while trying to stop Go Jun from watching the broadcast. |
| 아빠 | 진태경 | father to son | Taekyung | affectionate informal | Addresses his young son warmly as Taekyung. |
| 진태경 | 아빠 | son to father | Dad | childlike informal | Taekyung addresses his father as Dad in the childhood flashback. |
| 고세원 | 경호팀 | security-team commander to subordinate unit | Security Team | terse operational command | Calls the unit over radio before requesting status reports. |
| 길드원 | 진태경 | Peace Guild member to allied S-rank Hunter | Hunter Jin Taekyung | formal-polite and hesitant | A Guild member addresses Taekyung as 진태경 헌터님 while asking whether Choi should be awakened. |
| 고세원 | 진태경 | Ares security leader to hostile invading Hunter | you | calm, resigned, and confrontational | Go Se-won asks Jin whether he was looking for him and negotiates with him after losing the fight. |
| 진태경 | 고세원 | invading Hunter to hostile Ares security leader | Go Se-won | direct, questioning, and threatening | Jin calls Go Se-won's name, demands Go Jun's location, and questions why Go Se-won considers the day his last day at work. |
| 중역 | 고세원 | Ares executive_to_Head_of_Security | Team Leader Go | urgent and coercive | Pressures Go Se-won to kill Jin and accept the promised Vice Guild Master position. |
| 경호원 | 진태경 | government_security_officer_to_protected_Hunter | Hunter Jin Taekyung | formal and deferential | The security officers repeatedly address Jin as 진태경 헌터님 while explaining his temporary protection and legal status. |

## Listed compact profiles

### Go Jun.md

# Go Jun (고준)

- **Safe through:** Chapter 597
- **Aliases:** Team Leader Seok
- **Role:** Go Jun was Ares Guild's Vice Guild Master, Lee Jungryong's Disciple and former Head of Security, the de facto successor to Lee's Ares legacy, and a mutated monster who was killed by Jin Taekyung in Area A.
- **Personality:** Disciplined and controlled under ordinary pressure, fiercely loyal to Lee Jungryong, but consumed by humiliation and rage when Ares Guild's authority is challenged.
- **Voice:** Dry, controlled, and formal with subordinates; deferential when addressing his Master.
- **Relationships:** Go Jun inherited Lee Jungryong's Ares legacy after becoming his Disciple and regarded Jin Taekyung and Choi Minwoo as enemies before his death.

### Go Se-won.md

# Go Se-won (고세원)

- **Safe through:** Chapter 597
- **Aliases:** Head of Security
- **Role:** Go Se-won is Ares Guild's former Head of Security and Team Leader, now held in a special detention center after surrendering, subduing the remaining loyalists, and giving decisive testimony that Go Jun caused the two monster waves.
- **Personality:** Weary after thirty years of serving Ares as a hunting dog, he is morally conflicted but decisive when he finally breaks with the Guild's loyalists.
- **Voice:** Calm and deferential toward superiors, but blunt and decisive when issuing orders.
- **Relationships:** He formerly served Vice Guild Master Go Jun as Ares Guild's Head of Security; after exposing Go Jun's role, he is held in a special detention center and has requested a meeting with Jin Taekyung.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 597
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, a Supreme Peak master with the Heavenly Martial Physique and Force, publicly recognized as an S-rank-level Hunter while formally retaining an A-rank license.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor and assigned him a final task to incorporate martial principles into his learned martial arts but declined Taekyung's recruitment after Cheongpung reached him first, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate, student, and trusted manager of media and official arrangements, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, and Xiao Shen regards him as an older brother after Jin saved him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 597
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Lee Jungryong.md

# Lee Jungryong (이정룡)

- **Safe through:** Chapter 595
- **Aliases:** None
- **Role:** Former Vice Guild Master of Ares Guild, one of Korea's two S-rank Hunters, and a Supreme Peak-level martial artist who was killed by Jin Taekyung.
- **Personality:** Outwardly genial, calm, and humorous; calculating, opportunistic, manipulative, coercive, and ruthless when challenged
- **Voice:** Smooth, good-natured, and indirect, using teasing conversation and veiled threats before becoming openly furious
- **Relationships:** Master of Park Jihoon and Go Jun (Team Leader Seok), whom he personally selected and trained; longtime Great Cataclysm acquaintance of Park Tae Seop; adversary of Jin Taekyung; knew Team Leader Choi from childhood; has an antagonistic history with Kim Hwajong, who saved his life at the collapse of Mapo Bridge eighteen years earlier; was visibly shaken by learning that Choi is Cheon Taemin's maternal grandson; regarded Cheon Taemin as an older brother despite no blood relation and long held him in respect and fear; secretly supported the orphanage where Lee Dongseok grew up and was regarded by Dongseok as a father; operated as Ares Guild's senior authority beneath its Guild Master; concealed Taemin's condition with Song Cheonwoo and participated in purging aides who knew the truth.

## Korean source

```text
＃598화



특별한, 이라는 수식어가 붙은 것들에는 그만한 이유가 있는 법.

현재 고세원이 머무르고 있다는 특별 구치소가 바로 그랬다.

“정지. 잠시 신원 확인 절차가 있겠습니다.”

딱딱한 말투와 짙은 선글라스 너머로 보이는 날카로운 눈빛.

방탄복과 자동소총으로 무장한 군인의 말에, 운전석에 앉은 청와대 경호원이 얇은 카드를 내밀며 대답했다.

“이미 구치소장님께 연락이 갔을 텐데요.”

“죄송하지만, 이곳에서는 누구든 같은 절차를 밟아야 합니다.”

칼 같은 태도를 고수한 군인은 마법 감별기로 위장 여부까지 마친 뒤에야 차단기를 올렸고, 잠시 후 나는 소문으로만 듣던 특별 구치소의 실체를 조금이나마 엿볼 수 있었다.

빈틈없는 장비로 무장한 채 경비를 서는 백여 명의 군인들과 그 사이사이에 군인으로 위장한 채 숨어 있는 헌터들.

그것으로도 모자라 곳곳에 설치된 중화기는 물론이고 은밀히 감춰진 마법 트랩까지.

‘어지간한 놈들은 뼈도 못 추리겠는데.’

이곳은 아직 판결이 내려지지 않은 미결수(未決囚)들을 수용한 구치소다. 그럼에도 중범죄자만을 수용한 교도소보다 경계의 수준이 훨씬 삼엄했다.

그건 본관 앞에서 우리를 기다리고 있는 구치소장만 봐도 잘 알 수 있는 부분이었다.

“허허, 기다리고 있었습니다.”

구치소장은 치킨집 할아버지처럼 푸근한 인상의 소유자였지만, 그가 품고 있는 기운은 결코 푸근하지 않았다.

전직 A급 헌터라는 화려한 전적을 보유한 구치소장은 호의적인 태도로 나를 맞이했다.

“처음 태경 씨 소식을 듣고 속이 다 후련하더군요. 이건 구치소장으로서 할 말은 아니긴 한데…… 솔직히 여기 있는 새끼들을 볼 때마다 메이스로 대가리를 박살 내고 싶은 마음이 굴뚝 같아요. 내가 그거 참느라 탈모까지 온 것 아닙니까.”

“……아, 예.”

사람 좋아 보이는 구치소장의 충격 고백은 당황스러울 정도다. 떨떠름하게 대꾸한 나는 그의 반짝이는 머리를 보며 중얼거렸다.

“많이 참으셨나 보네요.”

“참아야지, 뭘. 그래도 가끔 못 참겠다 싶으면 한 번씩 때리기도 합니다. 물론 악질인 놈들에 한해서.”

“예?”

“포션 한 컵에 힐 넉넉하게 넣어 주면 싹 회복되는데, 지들이 뭘 어쩌겠습니까. 어차피 증거가 없어요, 증거가.”

“…….”

“범죄자 새끼들은 맞아야 돼요. 특히 여기 있는 놈들은 더 그래.”

청와대 경호원들은 이걸 대통령한테 보고해야 하나, 하는 표정을 지었고 나는 한 사람의 생존 여부가 걱정되기 시작했다.

“혹시 고세원이 아직 살아 있습니까?”

“아, 그 친구.”

구치소장이 껄껄 웃으며 말을 이었다.

“당연히 멀쩡합니다. 첫날에는 대형 사고라도 칠 것 같아서 걱정했는데…… 말도 고분고분하게 잘 듣고, 검찰 쪽 얘기 들어 보면 진술도 순조롭게 진행되는 것 같더라고요. 내가 태경 씨 오신다고 해서 특별히 접견실도 싹 비워 뒀으니 따라오시면 됩니다.”

나와 경호원들은 구치소장을 따라 내부로 들어갔다.

어둡고 차가운 복도. 쇠창살 대신 합금으로 이루어진 철문이 닭장처럼 줄지어 붙어 있었고, 문 앞에 설치된 소형 홀로그램 송출기로 그들의 움직임과 표정 하나하나를 뚜렷하게 관찰할 수 있었다.

‘소문은 익히 들었는데, 직접 보는 건 또 처음이네.’

특별 구치소가 특별한 이유는, 이곳에 임시 수용 중인 수감자들이 모두 기본적으로 각성자이기 때문이다.

죄목과는 관계없이 범죄를 저지른 자의 신분이 각성자라면 즉시 이곳으로 끌려온다.

아직 유죄 판결이 내려지지 않은 미결수라고는 해도 삼엄한 경계와 감시의 눈길을 피할 수는 없다.

‘각성자니까.’

최하급으로 분류되는 F급 각성자조차 건장한 성인 남성 두셋 정도는 쉽게 제압할 수 있다.

만약 그보다도 등급이 높고, 정식 훈련을 통해 헌터 라이센스를 취득한 자라면 두말할 것도 없었다.

“말이 미결수지, 사실 유죄인 게 확실한 놈들이 대부분이라 무슨 짓을 할지 몰라요. 탈옥 시도하는 놈들도 일 년에 두세 명씩은 꼭 나오는 편이고. 여기서 판결받고 특별 교도소로 넘어가면 아예 기회가 없을 거거든. 거긴 완전히 지옥이라.”

복도를 가로지르며 설명하던 구치소장이 유난히도 두껍고 단단해 보이는 철문 서너 개를 가리키며 덧붙였다.

“아, 이번에 들어온 저 새끼들은 특히 주의해서 감시하고 있습니다. 아무래도 잃을 게 없는 놈들이라 그런지 상당히 거칠더군요.”

누군가 싶어 문 앞에 떠오른 홀로그램을 확인해 보니, 최상층에서 스치듯 봤던 아레스 길드의 중역들이다.

고세원과 다른 아레스 길드원들에 의해 제압당하여 이쪽으로 넘겨진 모양이었다.

미라처럼 전신에 마나 억제기를 찬 채 누워 있는 그들을 유심히 들여다본 나는 진심을 담아 부탁했다.

“존나 야무지게 패 주세요.”

“안 그래도 그럴 생각입니다. 오랜만에 현역 때 쓰던 메이스에 윤활율 좀 발라 뒀죠.”

“역시 소장님은 다 계획이 있으시군요.”

내 칭찬에 흐뭇하게 웃은 구치소장이 물었다.

“아, 그런데 태경 씨는 앞으로 어떻게 되는 겁니까? 나야 잘 풀리길 바라지만 법이라는 게 또 워낙 복잡하니까.”

“글쎄요. 아직까지는 잘.”

“기왕이면 이쪽으로 오시면 좋겠네요. 내가 잘해 드릴게.”

“……아, 예.”

갑자기 윤활유로 번들거리는 메이스가 생각나는 건 왜일까.

내가 잠시 좋지 않은 상상을 떠올리는 사이, 미로처럼 길고 복잡한 복도가 끝나고 커다란 문이 나타났다.

보안 검색대에서 모든 절차를 끝마치자 구치소장이 설명했다.

“접견은 진태경 씨 혼자서. 상부 특별 요청으로 동석 경비나 시간 제한은 없겠지만 내부는 모두 녹음 및 촬영되니 유의해 주시기 바랍니다.”

현재 고세원의 상황을 생각하면 이 정도 제재는 당연하다. 내가 고개를 끄덕이자 굳게 닫혀 있던 문이 열렸다.

철컥.

문이 열림과 동시에 싸늘한 한기가 느껴진다. 영화 속에서 봤던 검찰 조사실과 흡사한 그 공간에는 익숙한 얼굴이 나를 기다리고 있었다.

“왔군. 생각했던 것보다 훨씬 빨리.”

고세원. 바로 그였다.

불과 이틀 사이 부쩍 초췌해진 그는 문이 닫히자 의자를 가리키며 말을 건넸다.

“계속 서 있지 말고 그만 앉지. 올려다보고 있자니 목이 아파서.”

철그럭.

몸을 움직일 때마다 육중한 쇳소리가 울려 퍼졌다. 목과 팔, 다리로 연결된 사슬을 훑는 내 시선을 알아차린 고세원이 어깨를 으쓱해 보였다.

“마나 억제기야. 불편하긴 해도 이 정도면 괜찮은 대접이지.”

나는 의자를 끌어당겨 앉으며 대답했다.

“하긴, 오는 길에 보니까 당신 친구들은 거의 피라미드 입주 직전이던데.”

“누구? 박 전무? 이 상무? 그것도 아니면…….”

“둘 다일걸. 누가 전무고 상무인지는 모르겠지만.”

“그것도 그렇군. 어차피 누구든 내 친구는 아니지만.”

이런 상황에서도 특유의 담담한 태도는 여전하다. 그런 고세원을 말없이 바라보던 나는 불쑥 입을 열었다.

“고맙다고 해야 하나?”

뜬금없는 말이었지만 무슨 뜻인지 못 알아들을 고세원이 아니었다. 피식 실소를 흘린 그가 대답했다.

“오래전부터 생각했던 일이었어. 단지 계기가 필요했던 것뿐이지.”

“후회는?”

“추호도 없다.”

고세원의 안색은 초췌했지만, 눈빛은 그 어느 때보다 맑았다. 어쩌면 내가 그를 살려 준 이유도 저 눈빛 때문이었는지도 모른다.

아레스 길드의 모두가 나를 분노와 두려움이 섞인 눈으로 바라보았을 때, 그는 맑고 담담한 눈빛을 잃지 않았다.

죽음을 앞둔 그 순간에도.

“이번 일로 잃을 게 많았을 텐데.”

“얻은 만큼 잃은 거지. 가진 게 아무것도 없었던 전쟁고아, 그때로 돌아간 것뿐이야. 무엇보다 소중한 가족을 지켰으니 그걸로 만족해야지.”

누구에게나 변화의 기회는 찾아온다. 아마 고세원에게는 가족이 바로 그 변화의 계기였을 것이다.

아마도 코앞까지 들이닥친 죽음 앞에서 걸려온 마지막 전화가, 그에게 지금의 선택을 하게끔 이끌지 않았을까 싶었다.

“그때 배경 화면 봤어. 아들 귀엽더라. 씩씩하게 생겼던데. 벌써 체격도 다부진 게, 나중에 커서 탱커 하면 딱이겠어.”

“딸이야.”

“아…….”

첫째 딸은 아빠를 닮는다더니.

의도치 않게 딸을 상대로 아탱딱을 시전한 내가 입을 다물자, 작게 한숨을 내쉰 고세원이 말했다.

“혹시 도움을 줄 수 있을까 싶어 불렀는데, 그럴 마음이 쏙 사라지게 만드는군.”

“…….”

“뭐, 됐고. 어찌 되었건 진태경 당신이 날 찾아왔다는 건 이미 이야기를 전해 들었다는 뜻이겠지?”

이렇게 주제가 넘어가서 다행이라고 생각하며, 나는 고개를 끄덕였다.

“뭐라고 전달받았나?”

“당신이 나한테 갚아야 할 빚이 있다던데. 더 이상 자세히는 못 들었어.”

“그럼 제대로 들었군. 다른 사람을 통해 전달하기에는 영 석연치 않아서 입을 다물고 있었지.”

석연치 않아?

현재 진행 중인 모든 수사와 취조에 순순히 임하고 있는 고세원이다.

자신이 지금껏 저지른 잘못까지 여과 없이 드러내며, 일종의 고해성사를 하고 있는 그가 말하지 않은 것이 있다니.

‘역시 뭔가가 있어.’

내가 곧이어 심상치 않은 이야기가 흘러나올 것을 직감한 것과 동시에, 고세원이 귓불을 만지작거렸다.

상호 간에 약속된 수신호는 아니었지만, 그 행동이 품은 의미를 알아차리는 것은 그리 어려운 일이 아니었다.

스아아아아.

단전에서 끌어올린 공력이 견접실 내부를 에워쌌다.

순식간에 소리가 차단된 공간. 마나 억제기를 차고 있음에도 그 사실을 알아차린 고세원이 입가를 문지르는 척하며 속삭였다.

“길드 본사에 숨겨진 비밀 구역은 A구역 하나뿐만이 아니야.”

“뭐?”

“A구역을 잘 찾아봐. 그 안에, 또 다른 비밀 구역이 있으니까.”

또 다른 비밀 공간이라니.

예상치도 못한 고세원의 말에, 잠시 눈을 깜빡이던 내가 황급히 되물었다.

“위치. 정확한 위치는?”

그리고 내 기대와 달리, 돌아오는 대답은 굵고 짧았다.

“나도 모른다.”

“뭐라고?”

“알면 말해 줬겠지. 하지만 그곳은 이정룡 부길드장님과 석고준만 출입할 수 있는 장소였다. 어디에 있는지, 어떻게 출입하는지도 알 수 없어. 그나마 내가 그곳의 존재를 알아차린 것도 경호팀장이 된 직후였어.”

한때나마 석고준의 최측근으로 인정받았던 고세원이다. 그런 그조차 또 다른 비밀 구역이 존재한다는 것까지만 알 뿐. 그 이상은 몰랐다.

“그렇다면 혹시…….”

“당연히 그곳에 무엇이 있는지, 그곳에서 무엇을 하는지도 모른다. 내가 아는 것은 딱 거기까지야.”

칼 같은 어조로 이어지려던 말을 잘라 낸 고세원이 말을 이었다.

“이미 정부 측 조사팀이 A구역을 샅샅이 뒤지고 있겠지만 아직 알아차리진 못했을 거다.”

“어째서?”

“만약 발견했다면, 다른 어떤 정보보다 먼저 그곳에 대해 내게 물었을 테니까.”

“……!”

“그러니 진태경. 네가 찾아봐라. 그곳에 어떤 비밀이 숨겨져 있을지는 모르겠지만.”

내가 계속해서 뭔가를 물어보려던 그때. 육중한 쇳소리와 함께 굳게 닫혀 있던 문이 열렸다. 구치소장과 청와대 경호원들이 미심쩍은 표정으로 물었다.

“소리가 들리지 않던데. 무슨 문제라도 있습니까?”

고세원이 담담하게 대꾸했다.

“접견 끝났습니다.”
```

## Final English reading copy

```markdown
# Chapter 598

There is always a reason behind things described as *special*.

The special detention center where Go Se-won was currently being held was no exception.

“Stop. We’ll need to verify your identities.”

The soldier’s tone was rigid, and his sharp eyes showed clearly beyond his dark sunglasses.

He was armed with body armor and an automatic rifle. The Blue House security officer in the driver’s seat held out a thin card as he answered.

“You should have already received a call from the warden.”

“I’m sorry, but everyone has to go through the same procedure here.”

The soldier maintained his razor-sharp attitude. Only after checking for disguises with a magic detector did he raise the barrier arm, and a short while later, I finally got a glimpse of the special detention center I had only heard about through rumors.

Roughly a hundred soldiers stood guard, armed to the teeth, while Hunters disguised as soldiers hid among their ranks.

And as if that weren’t enough, heavy weapons had been installed throughout the facility, along with magic traps concealed in various places.

*Most people wouldn’t be able to walk out of here in one piece.*

This was a detention center for suspects awaiting trial—people who had not yet been convicted. Even so, its security was far tighter than that of a prison reserved exclusively for serious criminals.

I could tell just by looking at the warden waiting for us in front of the main building.

“Ho-ho. I’ve been waiting for you.”

The warden had a warm, genial appearance, like an old man who ran a fried-chicken restaurant.

But the energy he gave off was anything but warm.

A former A-rank Hunter with an impressive record, the warden greeted me with a friendly attitude.

“When I first heard the news about you, I felt so relieved. This isn’t something I should say as the warden, but… honestly, every time I see the bastards in here, I feel like smashing their heads in with a mace. Isn’t that why I’ve gone bald from holding myself back?”

“……Oh. Right.”

The warden’s shocking confession was disconcerting. I answered awkwardly, then muttered as I looked at his shining head.

“You must have held yourself back a lot.”

“What else could I do? Still, sometimes I just can’t stand it anymore, so I hit them once or twice. Only the truly vicious ones, of course.”

“Pardon?”

“Give them a cup of potion and plenty of healing, and they recover completely. What can they do about it? There’s no evidence. No evidence.”

“……”

“Criminal bastards need to be beaten. Especially the ones in here.”

The Blue House security officers wore expressions that seemed to ask whether they should report this to the President, and I began to worry about whether one particular person was still alive.

“Is Go Se-won still alive, by any chance?”

“Ah, that fellow.”

The warden continued with a hearty laugh.

“Of course he’s perfectly fine. I was worried he might cause some major incident on his first day, but… he listens well, and from what I’ve heard from the prosecutors’ office, his testimony seems to be proceeding smoothly. I had the visitation room completely cleared out especially because you were coming, so just follow me.”

The security officers and I followed the warden inside.

The corridors were dark and cold. Alloy doors were lined up in rows like cages instead of iron bars, and small hologram projectors installed in front of each door allowed us to observe every movement and expression inside with perfect clarity.

*I’d heard all about this place, but this is my first time seeing it in person.*

The special detention center was special because every prisoner temporarily held there was an Awakened.

Regardless of their charges, anyone who committed a crime while possessing the status of an Awakened person was brought here immediately.

They might not have been convicted yet, but that didn’t mean they could avoid the facility’s severe security or the eyes watching them.

*Because they’re Awakened.*

Even an F-grade Awakened could easily subdue two or three grown men.

If they were higher-ranked and had obtained a Hunter license through formal training, that went without saying.

“They may technically be awaiting trial, but most of them are obviously guilty, so you never know what they might try. Two or three people attempt to escape every year without fail. Once they’re convicted here and transferred to a special prison, they won’t have any chance at all. That place is a complete hell.”

As he explained while crossing the corridor, the warden pointed toward three or four metal doors that looked particularly thick and sturdy.

“Ah, and we’re keeping a particularly close eye on those bastards who were brought in this time. They’re pretty rough, probably because they have nothing left to lose.”

I checked the hologram floating in front of the door to see who he meant.

They were the Ares Guild executives I had glimpsed briefly on the top floor.

It seemed they had been subdued by Go Se-won and the other Ares Guild members before being sent here.

They were lying there like mummies, mana suppressors strapped over their entire bodies. I stared at them intently, then made a heartfelt request.

“Please beat the shit out of them—good and proper.”

“I was planning to. I even put some grease on the mace I used back when I was active.”

“You really do have everything planned, Warden.”

The warden smiled in satisfaction at my praise, then asked,

“Ah, but what’s going to happen to you, Hunter Jin Taekyung? I hope things work out for you, but the law is a complicated thing.”

“Who knows? I still have no idea.”

“If possible, I’d actually like you to come over here. I’ll treat you well.”

“……Oh. Right.”

Why did I suddenly picture a mace glistening with lubricant?

While I was entertaining that unpleasant thought, the long, complicated corridor—which had twisted like a maze—finally came to an end, and a large door appeared.

After every procedure at the security checkpoint had been completed, the warden explained,

“The visit will be with Jin Taekyung alone. By special request from above, there will be no accompanying guard or time limit, but please be aware that everything inside will be recorded and filmed.”

Given Go Se-won’s current situation, those restrictions were only natural. When I nodded, the firmly closed door opened.

*Click.*

A chill swept over me the moment the door opened. The room looked like an interrogation room at the prosecutors’ office, just like the ones I had seen in movies.

A familiar face was waiting for me there.

“You came. Much sooner than I expected.”

It was Go Se-won.

He looked noticeably more haggard than he had only two days ago. Once the door closed, he pointed toward a chair.

“Don’t just stand there. Sit down. My neck hurts from looking up at you.”

*Clank.*

Heavy metallic sounds rang out whenever he moved. Go Se-won noticed my gaze as I looked over the chains connected to his neck, arms, and legs, then shrugged.

“It’s a mana suppressor. It’s uncomfortable, but this is decent treatment, all things considered.”

I pulled out a chair and sat down.

“I suppose. On the way here, I saw that your friends were almost ready to move into a pyramid.”

“Who? Executive Director Park? Managing Director Lee? Or…”

“Probably both. I don’t know which one is the executive director and which one is the managing director.”

“I suppose that’s true. Either way, neither of them is my friend.”

Even in a situation like this, his characteristically calm attitude remained unchanged.

I stared at Go Se-won in silence, then suddenly opened my mouth.

“Should I thank you?”

It was an unexpected question, but Go Se-won wasn’t the kind of person who would fail to understand what I meant.

He let out a quiet laugh and answered.

“It was something I’d been thinking about for a long time. I only needed a reason to act.”

“Do you regret it?”

“Not in the slightest.”

Go Se-won’s face was haggard, but his eyes were clearer than ever.

Perhaps that gaze was the reason I had saved him.

When everyone in Ares Guild had looked at me with a mixture of anger and fear, he had never lost that calm, lucid gaze.

Not even when he was standing on the verge of death.

“You must have lost a lot because of this.”

“I lost as much as I gained. I’ve only gone back to the way I was then—a war orphan who had nothing. More importantly, I protected my precious family. I should be satisfied with that.”

Everyone gets a chance to change.

For Go Se-won, that chance had probably been his family.

Perhaps the final phone call that came just as death was closing in had led him to make the choice he had made.

“I saw the background picture on your phone. Your son was cute. He looked sturdy, too. He’s already got a solid build. He’d be perfect as a tank when he grows up.”

“She’s my daughter.”

“Ah……”

They say the eldest daughter takes after her father.

When I fell silent after accidentally assigning someone’s daughter to the tank class, Go Se-won let out a small sigh.

“I called you because I thought you might be able to help me, but you make me lose the desire to ask.”

“……”

“Well, never mind. In any case, the fact that you came to see me means you’ve already heard about it, right?”

I was relieved that the subject had changed so smoothly, and I nodded.

“What did they tell you?”

“I was told you had a debt to repay me. I couldn’t hear anything more specific.”

“Then you heard correctly. It didn’t sit right with me to pass it along through someone else, so I kept quiet.”

*It didn’t sit right with him?*

Go Se-won was cooperating willingly with every investigation and interrogation currently underway.

He was even exposing his own wrongdoing without filtering anything out, almost as if he were making a confession.

And yet there was something he hadn’t mentioned.

*As I thought, something’s going on.*

Just as I sensed that something serious was about to come out, Go Se-won began fiddling with his earlobe.

It wasn’t a prearranged signal between us, but it wasn’t difficult to understand what the gesture meant.

*Fwoosh.*

The internal energy I drew up from my dantian spread around the visitation room.

The sound was cut off in an instant.

Despite wearing a mana suppressor, Go Se-won noticed what had happened. Pretending to rub the corner of his mouth, he whispered,

“Area A isn’t the only secret area hidden inside the Guild headquarters.”

“What?”

“Search Area A carefully. There’s another secret area inside it.”

Another hidden space.

I blinked for a moment at Go Se-won’s completely unexpected words, then hurriedly asked,

“Where is it? What’s the exact location?”

But contrary to my expectations, the answer that came back was low and brief.

“I don’t know.”

“What did you say?”

“If I knew, I would have told you. But only Vice Guild Master Lee Jungryong and Go Jun were allowed to enter that place. I don’t know where it is or how to get inside. I only realized it existed shortly after I became Head of Security.”

Go Se-won had once been recognized as one of Go Jun’s closest men. Even he only knew that another secret area existed. He knew nothing beyond that.

“Then perhaps…”

“Of course, I don’t know what’s inside or what they do there. That’s all I know.”

Go Se-won cut off what I was about to say in a razor-sharp tone, then continued.

“The government investigation team must be searching Area A from top to bottom by now, but they probably haven’t noticed it yet.”

“Why not?”

“If they had found it, they would have asked me about it before anything else.”

“……!”

“So, Jin Taekyung. You find it. I don’t know what kind of secret is hidden there, but…”

Just as I was about to ask him something else, the firmly closed door opened with a heavy metallic sound.

The warden and the Blue House security officers looked at us suspiciously.

“We couldn’t hear anything. Is there a problem?”

Go Se-won answered calmly.

“The visit is over.”
```

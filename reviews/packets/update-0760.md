<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0760.txt",
      "sha256": "a95f0009475d1b602d894f8ecfeb1797c4bfc1b0f3ddfae5c2d916bf5c8418a6",
      "bytes": 13052
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "535e51df0b8ccf2d260da1cdad14cc1e19920e4e732a9e1e0c189636e3e1d664",
      "bytes": 2204
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "d0cf7e61284ab429d66f765fa11a15b14e0854d19b153dc5f22c023992678cdb",
      "bytes": 220165
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "9b729496f164cf0e02644103208b360e8f41ea69b26e617f3b4becd6a00692b7",
      "bytes": 553
    },
    {
      "path": "characters/Leviathan.md",
      "sha256": "a43679f83aac80b79df70776504f5b3c71c2b597fd26c6b2dae4631a6e2e55de",
      "bytes": 666
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "a628ec35238fc5d5f903f50a7d3e3b81571e0cbf7cd3a47f045248cae288e7dc",
      "bytes": 235197
    }
  ],
  "estimated_tokens": 9066
}
-->

# Durable State Update — Chapter 760

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 760. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 760. Profile updates may replace only one
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
  "chapter": 760,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 760,
    "continuity_sources": [760],
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
    "The Munich Monster Wave has breached its barrier, releasing an army of Minotaurs led by an S-rank Minotaur Lord.",
    "Germany has evacuated most civilians from Munich and deployed military forces and roughly ten thousand Hunters against the Monster Wave.",
    "Germany has prepared Uran, its nuclear-weapon contingency, as a last resort.",
    "Joel Schumacher, Germany's S-rank Hunter and national symbol, was severely wounded fighting the Minotaur Lord.",
    "Jin Taekyung has arrived in Munich and is protecting Schumacher from the Minotaur Lord.",
    "Jin's Broken Body debuff and battle fatigue remain active.",
    "Jin secretly stored Leviathan's corpse and the two Japanese-government S-rank Magic Gems in his Inventory while publicly claiming they were destroyed.",
    "Jin suspects Michael Silbert lured Leviathan with an unrefined S-rank Magic Gem, but he has no proof.",
    "Jin acquired the Hope of the Sea Title after the Aquatic Rescue Worker Title was enhanced and renamed.",
    "The Main Quest: Cataclysm is active, but its mission, reward, and failure conditions are unknown.",
    "Michael Silbert remains engaged in the Cape Town Monster Wave after his forces began suppressing the South African disaster."
  ],
  "continuity_sources": [
    759
  ],
  "open_questions": [
    "Can Jin defeat the Minotaur Lord and stop the Munich Monster Wave?",
    "What does the Main Quest: Cataclysm require, and what new age of disaster is approaching?",
    "Can Jin prove that Michael Silbert lured Leviathan with an unrefined S-rank Magic Gem?",
    "What did Leviathan mean by saying that humanity and the world awakened it?",
    "Who is the unidentified figure in Cape Town, and which friend is waiting?"
  ],
  "safe_through": 759,
  "temporary_decisions": [
    "Render 망가진 신체 as Broken Body.",
    "Render 수상 구조대원 as Aquatic Rescue Worker.",
    "Render 바다의 희망 as Hope of the Sea.",
    "Render 격변 as Cataclysm in the Main Quest title, distinct from 대격변 as Great Cataclysm.",
    "Render 미노타우로스 로드 as Minotaur Lord, 우란 as Uran, and 위버맨쉬 as Übermensch."
  ],
  "version": 1
}
```

## Exact glossary matches

| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 초식     | **form**                                         | Numbered technique movement                           |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 일격     | **One Strike**                         |
| 상태               | **Status**                     |
| 스킬               | **Skill**                      |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 지능               | **Intelligence**               |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 길드      | **Guild**             |
| 팀장      | **Team Leader**       |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 레비아탄 | **Leviathan** | Ancient S-rank sea monster associated with Asmodeus. |
| 평화 | **Peace Guild** | Guild name. |
| 아레스 | **Ares Guild** | The leading Guild in Korea; formerly employed Team Leader Choi and Song Song. |
| 미노타우로스 | **Minotaur** | B-rank monster species. |
| 만년한철 | **Ten-Thousand-Year Cold Iron** | Material that destroys Pung Yang's Body-Protecting Qi when the Unnamed Sword satisfies a specific condition. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 화룡신창 | **Fire Dragon Divine Spear** | Taekyung's spear technique, at the seventh stage in this chapter. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 무아지경 | **Trance** | State Taekyung briefly enters during the energy digestion. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 화룡일미 | **Fire Dragon's Single Tail** | A form of the Fire Dragon Divine Spear. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 뮌헨 | **Munich** | Second word in one of the necromantic chants. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 비도 | **throwing blade** | Mungyeong throws one past Taekyung's neck. |
| 고든 | **Gordon** | Pentagon employee tasked with repairing smashed warning lights. |
| 만족 | **Man people** | An ethnic group mentioned by the Poison Flower Pavilion owner. |
| 마장동 | **Majang-dong** | Seoul district associated with livestock and meat markets. |
| 마력 | **magical power** | Distinct from mana; the Skeleton King's area of expertise. |
| 슈마허 | **Schumacher** | Surname of Germany's S-rank Hunter Joel Schumacher. |

## Matched address pairs

(No matching address pairs.)

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 759
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Leviathan.md

# Leviathan (레비아탄)

- **Safe through:** Chapter 757
- **Aliases:** None
- **Role:** Leviathan was an ancient S-rank sea monster and ruler of the sea who was killed by Jin Taekyung after the deep-sea hunt, leaving a final warning that the Cataclysm was approaching.
- **Personality:** Ravenous, domineering, and driven by instinctive hunger for magical power and food.
- **Voice:** Its spoken voice is not established; it communicates in Demon Realm language.
- **Relationships:** Leviathan once served the Demon King Asmodeus, its master, and withdrew into the deep sea after Asmodeus fell.

## Korean source

```text
＃760화



위버, 뭐?

분명히 내 이름을 부른 뒤에 뭐라 중얼거렸던 것 같은데, 힐끗 뒤를 돌아보니 조엘 슈마허는 이미 콘크리트 더미에 머리를 기댄 채 쓰러져 있었다.

‘아주 하얗게 불태웠구만.’

사실 그럴 만도 하다. 잠깐 지켜본 바에 의하면 그는 분명 무아지경(無我之境)의 상태에서 싸우고 있었으니까.

깨달음을 얻어 더 위대한 영역으로 나아가는 꿈의 순간.

안타깝게도 슈마허는 그 순간의 끝자락에 다다르지 못하고 기습당했지만, 아마 다시 눈을 떴을 때는 한층 강해져 있을 것이다.

“깨울까?”

“어차피 지금은 깨워도 못 일어나니까 그냥 놔둬. 그 사람 안 죽게 잘 지키고.”

“들었지? 잘생긴 인…… 아니, 최 팀장?”

“……알겠습니다.”

자연스럽게 짬 때리는 스킬을 보니 저 새끼도 인간 다 됐다.

물론 지금 같은 상황에서는 스켈레톤 킹이 전력상으로 훨씬 도움이 되는 것이 사실이라, 나는 타박 대신 조용히 전음(傳音)을 흘려보냈다.

- 어떻게 해야 하는지는 알지?

- 이 몸을 어린아이 취급 하는군.

- 읊어 봐.

퉁명스러운 의념이 돌아왔다.

- 인간들의 이목이 있으니 최대한 마력을 억제하고, 불가피하게 권능을 사용할 할 때는 절대 들키지 않게.

- 좋아.

- 이제 만족하나?

- 이 정도면 어린아이까지는 아니고, 중학생쯤은 되겠네.

- ……아직 서른도 안 된 인간 주제에 감히. 이 몸은 백 년도 넘게 산 어르신이다.

- 엄밀히 말하자면 백 년도 넘게 죽어 있는 거 아니냐.

“뭣이!”

육성으로 발끈하는 스켈레톤 킹의 외침에 피식 실소를 흘린 나는, 창날을 비스듬히 늘어트리며 중얼거렸다.

“할 말 다 했으니까 가라, 이제.”

남의 것처럼 낯선, 모래알처럼 건조한 목소리.

잠시나마 입가를 스쳤던 웃음기는 이미 흔적도 없이 사라진 후다.

나는 주춤거리며 이쪽을 노려보는 거대한 괴물을 향해 손가락을 까딱거렸다.

“넌 이리 오고.”

- 크르르…….

미노타우로스 로드.

놈의 아가리에서 불쾌한 악취와 함께 낮은 울음소리가 흘러나온다. 피처럼 붉은 눈동자에는 이미 경계심이 가득했다.

- 넌. 누. 구. 냐.

“나?”

내 등장과 함께 소강상태에 빠진 전장의 중심에서, 나는 천천히 걸음을 내디디며 말을 이었다.

“마장동 창잡이.”

- ……강. 하. 다. 인. 간.

대부분의 미노타우로스는 숫자도 셀 줄 모르는 소 대가리들이지만, 어떤 종류의 몬스터이건 간에 등급이 높을수록 지능도 발달한다.

특히 S급 몬스터는 그중에서도 특출난 힘을 부여받은 괴물들.

그렇기에 내가 나타난 그 순간부터, 미노타우로스 로드는 지면에 고정된 것처럼 움직임을 멈춘 상태였다.

놈은 이미 본능적으로 깨달아 버린 것이다.

자신의 힘으로는 결코 나를 꺾을 수 없다는 것을.

“확실히 눈치가 빠르네. 바로 안 달려드는 걸 보면.”

- ……!

저벅. 쿵.

겹쳐 들리는 두 개의 발걸음.

내가 다가간 거리만큼 뒤로 물러난 미노타우로스 로드가 돌연 맹수처럼 포효했다.

- 카우우우우!

화아아악!

거구를 중심으로 부풀어 오른 마력이 전장 구석구석으로 뻗어 나간다.

그와 동시에 일찌감치 이상한 낌새를 느끼고 하나둘씩 공격을 멈춰 가던 수천 마리의 미노타우로스가 흉광(凶光)을 번뜩이며 달려들었다.

놈들과 전투를 벌이던 헌터들이 아닌. 바로 우리를 향해.

- 쿠워어어!

구구구구궁!

괴성과 함께 지축이 흔들린다. 온 사방에서 밀려드는 무수한 소 떼 무리를 바라보던 스켈레톤 킹이 중얼거렸다.

“아니, 우리 아직 안 갔는데…….”

“그러게 빨리 갔어야지.”

“그럼 이런 상황에서는 권능 살짝 써도 되나? 군단이 필요할 것 같아서.”

“몬스터인 걸 알리고 싶으면 차라리 인터넷 방송을 하지 그러냐. 스켈레톤 군단 생성 미션 한번 하면 별풍선 쓸어 담겠다.”

“빌어먹을. 이제 와서 길 좀 비켜 달라고 부탁해도 안 들어주겠지?”

스켈레톤 킹의 개소리에 최 팀장이 대꾸했다.

“그런 걸 고민할 시간에 무기나 드십시오.”

스르릉.

목소리와 동시에 뽑혀 나오는 은빛 검신. 몬스터들을 향해 겨누어진 [영웅의 검]이 눈부신 오라를 머금었다.

그리고 뒤이어 또렷하게 모두의 귓가를 파고드는 최 팀장의 침착한 목소리.

“포메이션. 갖춰.”

처처처척!

뮌헨을 구원하기 위해 온 것은 우리 셋뿐만이 아니다.

레비아탄과의 전투에서는 별다른 활약을 하지 못한 아레스와 평화 길드의 헌터 이백여 명도 함께였고, 정예 중의 정예인 그들은 한 치의 흔들림도 없이 적들을 맞이할 준비를 끝마쳤다.

“전투 방침을 정해 주십시오.”

최 팀장도, 스켈레톤 킹도. 힘겨운 싸움을 이어 가던 도중에 간신히 위기를 넘긴 전장의 헌터들도.

모두가 내 입을 바라보고 있었다.

오직 나 한 사람의 명령만을.

그리고 바로 지금 이 순간, 그들에게 내가 해 줄 말은 하나밖에 없었다.

“싹 다 죽여.”

스아아아아.

하단전에 똬리를 틀고 있던 화룡(火龍)이 깨어나 사지백해로 스며든다.

사람들이 내지르는 거대한 함성을 신호탄 삼아, 나는 힘차게 지면을 박찼다.

콰앙!

전신을 스치는 세찬 바람.

단숨에 수십여 미터의 공간이 지워지고 투우(鬪牛)처럼 돌진하는 미노타우로스 군단이 코앞까지 성큼 다가온다.

아니, 다가온 것은 놈들이 아닌 바로 나다.

후우.

숨을 내뱉음과 동시에 호흡을 멈추고, 비스듬히 늘어트린 창대를 일으켜 세운다. 강대한 열양지기가 화염이 되어 투명한 창날에 깃들었다.

그리고…… 쏟아낸다.

‘바로 지금.’

화룡신창 일초식.

화룡일미(火龍一尾).

후웅, 화아아아악!

초고온의 열풍(熱風)과 함께 허공을 가로지르는 불꽃의 선.

용의 꼬리처럼 부드럽게 휘어진 기운이 전방을 휩쓸었다. 합금도 우습게 관통하는 뿔을 녹이고, 괴물들의 뼈와 가죽을 태웠다.

콰아아아아!

단 일격.

파도가 되어 쏟아진 화염이 수십 마리에 달하는 미노타우로스를 집어삼켰고, 비명은 어디에도 없었다.

단말마조차 내지르지 못한 채 까맣게 타오르는 그 끔찍한 광경에, 뒤이어 달려오던 놈들조차 돌격을 멈추고 주춤거렸다.

- 크워어어어!

부하들을 앞세운 우두머리의 괴성이 놈들을 재촉했지만, 본능적인 두려움에 사로잡힌 놈들의 귓가에는 들리지 않았고 그 짧은 망설임의 대가는 혹독했다.

서걱!

절삭음과 함께 허공으로 두둥실 떠오른 목과 사지.

단숨에 놈들 사이로 파고든 나는 미친 듯이 날뛰었다.

뒤늦게 정신을 차린 한 놈이 휘두른 메이스를 몸뚱어리와 함께 가르고, 두꺼운 가죽으로 뒤덮인 가슴을 손등으로 후려쳤다.

콰직!

뼈가 으스러지는 섬뜩한 소리와 함께 튕겨 나간 거체가 진형을 무너트린다.

이미 숨이 끊긴 동료의 몸뚱어리를 밀어 내며, 황급히 몸을 일으켜 세운 미노타우로스들의 머리 위로 무수한 마법과 화살이 날아들었다.

쉬쉭, 푸푸푹!

퍼엉! 치지지직!

오라가 맺힌 화살에 머리와 눈을 관통당한 놈들은 비교적 편안한 죽음을 맞이한 편이다.

마나로 생성된 화염 덩어리가 가죽을 태우고, 수십 줄기로 갈라져 쏟아진 전류가 사방을 환하게 물들였으니까.

- 크륵, 크르륵!

쿵! 털썩.

경련과 함께 줄줄이 쓰러지는 괴물들. 불과 전류가 만들어 낸 매캐한 연기 사이로 낯익은 얼굴이 가장 먼저 튀어나왔다.

“으아아아! 이 쳐 죽일 몬스터 놈들아!”

쐐애애액, 퍼걱!

아니, 자연스러운 동족상잔은 둘째치고 저건 또 어디서 주워 온 거야.

거대한 할버드를 손에 쥔 스켈레톤 킹이 미노타우로스 서너 마리를 단숨에 반으로 쪼갰다.

그리고 뒤이어 달려드는 놈들을 향해 다시 한번 휘두르려던 찰나, 연기 사이로 푸른 오라가 뻗어 나왔다.

서걱!

군더더기 없는 움직임과 조금의 낭비도 없는 최소한의 힘.

깔끔하게 목을 갈라 낸 최 팀장이 입을 열었다.

“돌격.”

나직하지만 힘 있는 목소리.

마나가 실린 그 한 마디가 외침이 되어 전장 구석구석으로 파고든 바로 그 순간.

“와아아아아!”

“이 개 씨발 새끼들아아!!”

“모조리 죽여라! 우리의 고향을 지키자!”

두두두두두!

거대한 함성과 함께 무수히 많은 헌터들의 군세(軍勢)가 물결처럼 들이닥쳤다.

비록 레비아탄이 일으켰던 파도처럼 높고 크지는 않았으나, 번뜩이는 그들의 눈동자에는 그것을 뛰어넘는 힘이 담겨 있었다.

반드시 이 땅을 빼앗기지 않겠다는 의지.

오늘 이 자리에서 죽어간 동료들을 향한 슬픔과 눈앞의 괴물들을 위해 남겨 둔 복수심.

그리고 그런 그들의 선두에, 내가 있다.

후웅, 펑!

빛살처럼 내지른 일권(一拳)의 끝에서 압축된 공기가 터져 나간다.

머리가 흔적도 없이 사라진 괴물이 썩은 통나무처럼 쓰러지고, 새롭게 모습을 드러낸 적들을 향해 무수한 창격(窓格)이 쏟아졌다.

쉬쉬쉬쉭!

베고, 찌르고, 동시에 비틀며 부순다.

강기(罡氣)가 서린 만년한철을 막을 수 있는 것은 아무것도 없었다.

단단한 병장기를 두부처럼 베어 낸 창날은 그 뒤에 숨어 있던 주인마저 갈라 버렸고, 특수 디버프의 영향을 받고 있음에도 이미 한계를 초월한 육체는 몬스터조차 아득히 뛰어넘었다.

바로 지금처럼.

- 크워어어!

후우웅!

괴성과 함께 옆구리를 향해 파고드는 묵직한 파공성.

세 마리의 미노타우로스를 꼬챙이처럼 꿰어 버린 나는, 인식과 동시에 남은 한 손을 뻗었다.

턱.

맨홀 뚜껑만큼이나 커다란 주먹이 가로막힌다.

그에 비하면 한참이나 작은 내 손바닥에 의해.

그것도 우스우리만치 쉽게.

- 크워?

미노타우로스가 김 진사 댁 누렁소처럼 순박하게 눈을 깜빡인다.

그 어울리지 않는 모습에 실소를 흘린 나는, 손바닥에 가로막혀 파르르 떨리는 주먹의 힘을 부드럽게 위로 흘려보냈다.

후웅!

한 뼘 위의 허공을 후려치는 주먹.

하지만 한순간에 표적을 놓친 놈과는 달리, 내가 번개처럼 내뻗은 발끝은 정확한 힘과 타이밍으로 괴물의 가슴에 닿았다.

콰직!

섬뜩한 파열음과 함께 힘을 이겨 내지 못한 몸뚱어리가 튕겨 나간다. 일직선의 경로에 위치한 동료들을 휩쓸며 멀리, 저 멀리.

뒤에서 이 모든 광경을 지켜보던 자신의 우두머리를 향해.

그리고…….

서걱! 촤아아악!

이미 숨이 끊긴 몸뚱어리가 반으로 갈라졌다. 분수처럼 솟구치는 핏물 사이로 미노타우로스 로드가 나를 노려보고 있었다.

피처럼 붉은 눈동자와 부하의 피로 물든 양날 도끼.

그러나 나는 이미 알고 있다.

저 눈동자 깊숙한 곳에 웅크린 무언가를.

어느덧 경계심에서 두려움으로 변화한 그 감정이, 자꾸만 놈을 뒷걸음질 치게 만들고 있었다.

“도망치고 싶냐?”

- ……!

“그래. 도망치고 싶을 수는 있지. 그런데…….”

후우우웅! 퍼걱!

우두머리를 지키기 위해 사방에서 달려들던 수십 마리의 미노타우로스가 튕겨 나간다. 처참하게 피곤죽이 된 놈들을 마지막으로 마침내 탁 트인 앞길.

창날에 묻은 피를 털어 낸 내가 천천히 말을 이었다.

“올 때는 좆대로 왔어도, 갈 때는 아니지.”

- 너……!

쾅!

뒤늦은 외침을, 발끝에서 터져 나온 굉음이 집어삼킨다.

공간을 지우며 빛살처럼 쇄도하는 나를 향해, 이를 악문 미노타우로스 로드가 양날 도끼를 집어던졌다.

쉬이이이잉!

파공성과 함께 덮쳐 오는 어둠. 아니, 마력.

단 한 번의 발구름으로 낮게 허공을 가로지르던 나는 몸을 비틀었다.

후웅.

짙은 혈향을 머금은 거센 바람이 코끝을 스쳤고, 나는 창을 뻗었다.

“뒈져.”

퍼걱!

이번에도 단말마는 없었다.
```

## Final English reading copy

```markdown
# Chapter 760

“Über, what?”

He had definitely called my name before muttering something, but when I glanced back, Joel Schumacher was already collapsed against a pile of concrete with his head resting on it.

*He really burned himself out.*

And it was understandable. From what I had seen, he had clearly been fighting in a state of Trance.

A dreamlike moment when one gained enlightenment and advanced into a greater realm.

Unfortunately, Schumacher had been ambushed before he could reach the end of that moment, but when he opened his eyes again, he would probably be stronger than before.

“Should I wake him?”

“He won’t be able to get up even if you wake him right now, so just leave him. Make sure that man doesn’t die.”

“You heard him, right? Handsome per—no, Team Leader Choi?”

“…Understood.”

Seeing how naturally that bastard dumped the work on someone else, I realized he had truly become human.

Of course, in a situation like this, the Skeleton King would be far more useful as a fighting force. So instead of scolding him, I quietly sent a message through Sound Transmission.

*You know what you need to do, right?*

*You treat this body like a child.*

*Recite it.*

A curt thought came back.

*There are human eyes watching, so suppress your magical power as much as possible. And when using your power is unavoidable, make absolutely certain that no one notices.*

*Good.*

*Are you satisfied now?*

*This is enough to make you about middle-school age, not a child.*

*…How dare you, a human who is not even thirty yet. This body is an elder who has lived for over a hundred years.*

*Strictly speaking, haven’t you been dead for over a hundred years?*

“What!”

At the Skeleton King’s outraged shout, spoken aloud, I let out a quiet laugh and lowered the spearhead at an angle.

“I’ve said everything I needed to say, so go. Now.”

My voice was unfamiliar, like someone else’s, and dry as sand.

The trace of laughter that had briefly touched my lips was already gone without a trace.

I crooked a finger at the enormous monster glaring at me, its movements hesitant.

“You. Come here.”

—Grrr…

The Minotaur Lord.

A low growl escaped its maw along with an unpleasant stench.

Its blood-red eyes were already filled with wariness.

—Who. Are. You.

“Me?”

In the center of the battlefield, which had fallen into a lull with my arrival, I slowly took a step forward and continued speaking.

“The Majang-dong Spearman.[^1]”

[^1]: Majang-dong is a Seoul district known for its livestock and meat markets.

—…Strong. Hu. Man.

Most Minotaurs were cow-headed idiots who could not even count, but no matter what kind of monster it was, the higher its grade, the more its intelligence developed.

S-rank monsters in particular were creatures granted exceptional strength even among their kind.

That was why, from the moment I appeared, the Minotaur Lord had stopped moving, as if fixed to the ground.

It had already realized instinctively.

That it could never defeat me with its own strength.

“You’re pretty quick on the uptake. The fact that you haven’t charged me yet proves it.”

—…!

Step. Boom.

Two footsteps overlapped.

The Minotaur Lord, which had retreated as far as I had advanced, suddenly roared like a wild beast.

—Moooooo!

Fwoosh!

Magical power swelled around its massive body and spread into every corner of the battlefield.

At the same time, thousands of Minotaurs that had sensed something strange long ago and gradually stopped attacking flashed murderous eyes and charged.

Not at the Hunters fighting them.

At us.

—Kwooooo!

Rumble-rumble-rumble!

The earth shook beneath their monstrous cries. The Skeleton King looked at the countless herds of bulls surging in from every direction and muttered,

“But we haven’t left yet…”

“That’s why we should’ve left sooner.”

“Then can I use a little power in this situation? I think we need an army.”

“If you want to announce that you’re a monster, why not start an internet broadcast? You could rake in virtual gifts with a ‘Skeleton Army Creation’ stream.”

“Damn it. They wouldn’t listen even if I asked them to make way now, would they?”

Team Leader Choi answered the Skeleton King’s bullshit.

“Stop worrying about that and draw your weapon.”

Shing.

At the same time as his voice, a silver blade slid free. The **Hero’s Sword**, pointed toward the monsters, radiated a dazzling aura.

Then Team Leader Choi’s calm voice clearly pierced everyone’s ears.

“Get in formation.”

Clack-clack-clack!

We were not the only ones who had come to save Munich.

More than two hundred Hunters from the Ares Guild and Peace Guild had come with us as well. Though they had not played much of a role in the battle against Leviathan, they were the elite of the elite and prepared to face the enemy without the slightest hesitation.

“Please give us our orders.”

Team Leader Choi.

The Skeleton King.

Even the Hunters on the battlefield who had barely survived one crisis while continuing their grueling fight.

Everyone was looking at my mouth.

Waiting for a command from me alone.

And at this very moment, there was only one thing I could say to them.

“Kill every last one.”

Whoooooosh.

The fire dragon coiled within my lower dantian awakened and seeped into every part of my body.

Taking the crowd’s thunderous roar as my signal, I kicked off the ground with all my strength.

Boom!

A fierce wind brushed past my entire body.

Dozens of meters disappeared in an instant, and the Minotaur army charging like bulls in a fighting ring came stomping right up to my face.

No.

It was not them that had come closer.

It was me.

Whoosh.

As I exhaled, I stopped breathing and raised the spear shaft I had been holding diagonally. Powerful Scorching Yang Qi became flames and settled into the transparent spearhead.

And then…

I unleashed it.

*Right now.*

Fire Dragon Divine Spear, first form.

Fire Dragon’s Single Tail.

Whoom—fwoooosh!

A line of flame cut across the air amid a wave of superheated wind.

The energy curved smoothly like a dragon’s tail and swept across everything in front of me. It melted the horns that could pierce alloy with ease and burned through the monsters’ bones and hides.

Kaaaaaaboom!

One strike.

The flames that poured out like a wave swallowed dozens of Minotaurs, and there were no screams anywhere.

The sight of them burning black without even managing a final cry was so horrific that even the Minotaurs charging in behind them stopped their advance and faltered.

—Kwooooo!

The leader’s roar, urging its subordinates forward, could not be heard by those seized by instinctive fear.

And they paid dearly for that brief hesitation.

Slash!

Heads and limbs floated into the air with the sound of cutting flesh.

I plunged straight into their midst and went berserk.

I cleaved apart one Minotaur’s body along with the mace it had swung after belatedly regaining its senses, then struck the thick hide covering another’s chest with the back of my hand.

Crack!

With a chilling sound, its bones shattered and its massive body was flung away, disrupting the formation.

As the Minotaurs hurriedly got back to their feet, pushing away the bodies of their already dead comrades, countless spells and arrows flew over their heads.

Whish, thud-thud-thud!

Boom! Bzzzzzt!

The ones whose heads and eyes were pierced by aura-coated arrows were among the fortunate. They received relatively peaceful deaths.

Fireballs created from mana burned their hides, while electricity split into dozens of streams and poured down, lighting up every direction.

—Krrk, krrrk!

Boom! Thud.

The monsters collapsed one after another amid violent spasms. Through the acrid smoke created by the fire and electricity, a familiar face burst out first.

“Graaaaaah! You goddamn monsters!”

Whoooosh—crack!

Putting aside the natural monster-on-monster slaughter, where had he even found that?

The Skeleton King, gripping an enormous halberd, cleaved three or four Minotaurs in half at once.

And just as he was about to swing again at the ones charging in behind them, a blue aura shot through the smoke.

Slash!

With clean movements and only the minimum force necessary, Team Leader Choi opened his mouth after neatly cleaving through a neck.

“Charge.”

His voice was quiet but powerful.

The instant that single word, infused with mana, became a shout and spread through every corner of the battlefield—

“Waaaaaah!”

“You fucking bastards!”

“Kill them all! Protect our homeland!”

Thud-thud-thud-thud!

Along with the enormous roar, an army of Hunters came surging in like a wave.

It was neither as high nor as vast as the wave Leviathan had raised, but the power burning in their flashing eyes surpassed it.

The will to never let this land be taken from them.

The grief they felt for the comrades who had died here today, and the thirst for revenge they had saved for the monsters in front of them.

And at the very front of them, there I was.

Whoom—boom!

Compressed air exploded from the end of the punch I drove forward like a beam of light.

A monster whose head had vanished without a trace collapsed like a rotten log, and countless spear strikes rained down upon the enemies newly revealed behind it.

Whish-whish-whish!

I cut, stabbed, twisted, and crushed all at once.

Nothing could block the Ten-Thousand-Year Cold Iron wrapped in Force.

The spearhead that sliced through sturdy weapons like tofu split apart the owners hiding behind them as well, and despite the effects of the special debuff, my body—which had already transcended its limits—stood far beyond even the monsters.

Just like now.

—Kwooooo!

Whoooom!

A heavy roar of air being split apart bored toward my side along with the monster’s cry.

After skewering three Minotaurs like meat on a skewer, I extended my remaining hand the moment I sensed the attack.

Thud.

A fist as large as a manhole cover was blocked.

By my much smaller palm.

And with laughable ease.

—Kwo?

The Minotaur blinked innocently, like the yellow ox at Scholar Kim’s house.

I let out a quiet laugh at the absurd sight and gently redirected the force of the fist trembling against my palm upward.

Whoom!

Its fist struck the air a handspan above.

But unlike the monster, which had lost its target in an instant, the tip of my foot shot forward like lightning and struck the monster’s chest with perfect force and timing.

Crack!

With a chilling burst, its body, unable to withstand the force, was sent flying.

Far away. Very far away.

It swept away every comrade in its straight-line path.

Toward its own leader, which had been watching the entire scene from behind.

And then…

Slash! Fwoooosh!

The already lifeless body was cleaved in half. Through the blood that gushed upward like a fountain, the Minotaur Lord glared at me.

Blood-red eyes.

A double-bladed axe stained with the blood of its subordinate.

But I already knew.

I knew what was crouching deep within those eyes.

The emotion that had changed from wariness to fear was making the monster retreat step by step.

“Do you want to run?”

—…!

“Of course you might want to run. But…”

Whoooom! Crack!

Dozens of Minotaurs that had rushed in from every direction to protect their leader were flung away. At last, after the monsters had been reduced to gruesome heaps of blood and flesh, the path ahead lay wide open.

I shook the blood from my spearhead and slowly continued.

“You came here however the fuck you pleased, but leaving isn’t up to you.”

—You…!

Boom!

The belated cry was swallowed by the thunderous sound exploding from my toes.

As I erased the distance and shot forward like a beam of light, the Minotaur Lord clenched its teeth and threw its double-bladed axe.

Whoooooosh!

Darkness came rushing toward me with a roar of air being split apart.

No.

Magical power.

I had crossed the low air like a beam of light with a single push off the ground, and I twisted my body.

Whoom.

A fierce wind thick with the smell of blood brushed past the tip of my nose, and I thrust out my spear.

“Die.”

Crack!

This time, too, there was no final cry.
```

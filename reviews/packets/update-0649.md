<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0649.txt",
      "sha256": "e635a8d84d7b268e7ffb83dfc9e2ba43219f68a761ee172c7697a3a20f320799",
      "bytes": 13331
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "526de19b109ca7a41660a52c1b3811a743b0283ea0ca224b8a8035fefc571ed3",
      "bytes": 2671
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "c60d77664c271582e2323ff18e216f423a3d9b066bfd2d0518707c75257990ed",
      "bytes": 199345
    },
    {
      "path": "characters/Baeksang.md",
      "sha256": "ef8f7e7ddb3440eec1202227378844b8a70fcae9f064d10ca0544450d618efaf",
      "bytes": 794
    },
    {
      "path": "characters/Gung Gibang.md",
      "sha256": "d613466b75cf9fd2f972afaeda30f0cd44d1b0f6b077f24460197b93c2f0fd01",
      "bytes": 686
    },
    {
      "path": "characters/Ju Hwaran.md",
      "sha256": "73719655f7d0f9cec5e239ca55d0c4c793471cc13601133a0feedfc250936db0",
      "bytes": 1131
    },
    {
      "path": "characters/Namho.md",
      "sha256": "90dc8e2028ebfece2a03f1fd85a95382d7bfdf2c05e6f8741f7154d43b865dc0",
      "bytes": 843
    },
    {
      "path": "characters/Sama Pyo.md",
      "sha256": "bcf6d803a8d8122985ff20e1ec7374b5897158555b145ff548ffc801206bd69d",
      "bytes": 899
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "cc841fd78f655a8c2c901792b0d81f41171f63a57ec7b65618226da0b50ac0ee",
      "bytes": 528
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "634ee76740dd1f8888e7e9c7f86b94b96db9ad200ed419b7980b365e55bf3084",
      "bytes": 204908
    }
  ],
  "estimated_tokens": 10789
}
-->

# Durable State Update — Chapter 649

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 649. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 649. Profile updates may replace only one
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
  "chapter": 649,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 649,
    "continuity_sources": [649],
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
    "Jin Taekyung has majority-backed admission to the Nanman tribal grand council.",
    "Baeksang attacked Jin Taekyung at the council and withdrew with the pro-Baeksang faction after being stopped; he remains coldly hostile toward Jin.",
    "More than ten thousand Bai people and roughly half of Nanman's chieftains remain hostile to Jin.",
    "The Blood Monk is an unidentified bald, beardless, apparently middle-aged martial artist using a steel Zen staff who has killed several hundred people in Guizhou.",
    "Namho considers it highly likely that Dark Heaven is behind the Blood Monk, though this remains unconfirmed.",
    "Ju Hwaran, Song Ilseom, and Hyuk Mujin are investigating the Blood Monk in Guizhou for reconnaissance and possible combat.",
    "Baeksang's hostility toward the Central Plains may come from grief over losing his only child or from a grudge against the orthodox Murim, and his possible alliance with Dark Heaven could endanger Nanman.",
    "Approximately two hundred Ailao Mountain warriors remain inside the Thousand-Year Spider webs, which appear to shield them from the Poison Mist.",
    "The missing ferocious beasts, Ailao Mountain's Wraith, and the pure-white eggs in the Poisonblood Grounds remain unexplained.",
    "An unidentified entity who recognizes Jin Taekyung has killed two informants.",
    "The Martial God once annihilated five Supreme Peak fiends and five hundred Blood Ghost Squad members alone, later appeared as a young boy, and then disappeared; Jin suspects a possible connection to Cheon Taemin.",
    "The Beast Miao King is Baeksang's sworn elder brother and childhood companion and is trying to preserve their bond while asking Jin and Baeksang to set aside their conflict."
  ],
  "continuity_sources": [
    648
  ],
  "open_questions": [
    "What are the Blood Monk's identity, purpose, destination, and connection to Dark Heaven?",
    "Is Baeksang acting from grief, resentment toward the orthodox Murim, or an alliance with Dark Heaven?",
    "Where did the missing ferocious beasts go, and what does Ailao Mountain's Wraith intend to do with the pure-white eggs?",
    "Who is the hidden entity that recognizes Jin Taekyung, and what is the nature of their past connection?",
    "Are the Martial God and Cheon Taemin connected, and where did the Martial God go after disappearing?"
  ],
  "safe_through": 648,
  "temporary_decisions": [
    "Use Tribal Grand Council for 부족 대회의.",
    "Use Blood Monk for 혈승.",
    "Use Soul-Chasing Guest for 추혼객.",
    "Use Killing Buddha for 살불.",
    "Use Fire Courtyard for 화원."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 주화란    | **Ju Hwaran**      |
| 태원진가   | **Jin Family of Taiyuan**        |
| 무림맹    | **Murim Alliance**               |
| 암천     | **Dark Heaven**                  |
| 남만야수궁  | **Nanman Beast Palace**          |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 사파     | **unorthodox faction**                           |                                                       |
| 중원     | **Central Plains**                               |                                                       |
| 전각     | **pavilion**                                 | Use “hall” only when established for a specific named building |
| 시스템              | **System**                     |
| 태원     | **Taiyuan**            |
| 공자      | **Young Master**                                                |
| 소저      | **Young Lady**                                                  |
| 백상 | **Baeksang** | Great chieftain of the Bai people and Yayul Cheok's sworn younger brother. |
| 궁기방 | **Gung Gibang** | Beggars' Sect Successor Beggar and finalist. |
| 남호 | **Namho** | Hidden Shadow Pavilion code name; literally associated with amber from the south. |
| 사마표 | **Sama Pyo** | Young Sect Leader of the Black Dragon Demon Gate. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 삼공자 | **Third Young Master** | Title used for Jin Taekyung. |
| 기감 | **Qi Sense** | Taekyung's sensory technique; its range reaches seventy meters in this chapter. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 태자 | **Crown Prince** | Title of the Emperor's older brother who was reportedly assassinated. |
| 개방 | **Beggars' Sect** | Murim organization counted among the Nine Sects and One Gang. |
| 연무장 | **training ground** | Private martial-arts practice area at Taekyung's newly rebuilt pavilion. |
| 한족 | **Han Chinese** | Ethnic designation used by the steppe chieftains. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 아미타불 | **Amitabha** | Buddhist invocation spoken by the unidentified arriving group. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 은영각 | **Hidden Shadow Pavilion** | Former Murim Alliance intelligence organization. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 아미 | **Emei** | Short form for Emei Sect. |
| 화란 | **Hwaran** | Familiar short form of Ju Hwaran. |
| 살수 | **assassin** | Professional killer considered as a possible suspect. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 암기 | **hidden weapon** | Term used in Mungyeong's promise not to throw one. |
| 고든 | **Gordon** | Pentagon employee tasked with repairing smashed warning lights. |
| 내궁 | **Inner Palace** | The inner compound of the Nanman Beast Palace. |
| 인시 | **Insi** | The traditional time period from three to five in the morning. |
| 인벤토리 | **Inventory** | System storage summoned by Jin. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 주화란 | 궁기방 | rescued_survivor_to_benefactor | Benefactor | formal-deferential | Hwaran includes Gung Gibang among the Benefactors when greeting Taekyung's companions. |
| 주화란 | 사마표 | former_fiancés | Young Sect Leader | formal and guarded | Hwaran formally greets her former fiancé. |
| 사마표 | 태산 | Young Sect Leader to subordinate | Taishan | informal and patronizing | Sama Pyo calls Taishan by name while ordering him to leave. |
| 태산 | 사마표 | subordinate to Young Sect Leader | Lord | crude and deferential | Taishan uses 주군 while obeying Sama Pyo. |
| 주화란 | 남호 | pavilion_member_to_hidden_shadow_agent | you / Elder Namho | formal and appreciative | Hwaran respectfully praises the effort Namho invested in mapping Nanman. |
| 남호 | 태산 | guide_to_pavilion_member | Taishan | blunt and exasperated | Namho directly rebukes Taishan for eating the poisonous blood-feeding fungus. |
| 남호 | 사마표 | guide_to_young_sect_leader | Young Sect Leader | blunt and admonishing | Namho warns Sama Pyo that all grass and animals in the territory belong to the Nanman Beast Palace. |
| 남호 | 주화란 | guide_to_escort_bureau_head | Escort King's granddaughter | approving and familiar | Namho praises Hwaran for recalling Ju Gongsan's records about Nanman. |
| 사마표 | 남호 | young_sect_leader_to_guide | Elder Namho | formal and apologetic | Sama Pyo apologizes after Taishan attempts to seize the calf. |
| 태산 | 주화란 | Pavilion member to Pavilion member | Young Lady Ju | clipped, childlike, and deferential | Agrees with Ju Hwaran after she mentions the evening banquet. |

## Listed compact profiles

### Baeksang.md

# Baeksang (백상)

- **Safe through:** Chapter 648
- **Aliases:** None
- **Role:** Baeksang is the middle-aged great chieftain of the Bai people, one of Nanman's four most powerful great tribes.
- **Personality:** Cold, rigid, meticulous, and politically resolute, with a deep but guarded attachment to his sworn elder brother.
- **Voice:** Rigid, formal, restrained, and emotionally distant.
- **Relationships:** Baeksang is Yayul Cheok's sworn younger brother and childhood companion and Yayul Mok's sworn uncle, opposes the Nanman Beast Palace joining the Murim Alliance, remains distrustful of the Central Plains, and may resent the orthodox Murim over the loss of his only child or be secretly aligned with Dark Heaven.

### Gung Gibang.md

# Gung Gibang (궁기방)

- **Safe through:** Chapter 542
- **Aliases:** Successor Beggar, Beggar Prince, pure-blooded beggar, ultimate beggar
- **Role:** Gung Gibang is the Beggars' Sect Successor Beggar and a unique eight-knot disciple.
- **Personality:** Vulgar, aggressive, and quick-tempered.
- **Voice:** Blunt, profane, and vividly threatening.
- **Relationships:** Gung Gibang is a rival finalist alongside Baek Woo and Zhuge Gyun who trades insults with Taekyung, uses Beggars’ Sect intelligence to investigate Tang Taesang’s murder and Dark Heaven’s Hubei forces, and has now found a trace of Honglan.

### Ju Hwaran.md

# Ju Hwaran (주화란)

- **Safe through:** Chapter 647
- **Aliases:** Hwaran
- **Role:** Ju Hwaran is a Level 88 Young Bureau Head, leader of the Yongbong Escort Bureau, a member of the Fire Dragon Pavilion, an experienced Nanman escort guide with route knowledge from the Escort King's records, someone who can understand the Miao and Bai languages, and a volunteer accepted for the scouting mission to investigate the Blood Monk in Guizhou.
- **Personality:** Intelligent, capable, responsible, filial, composed under pressure, and burdened by intense guilt over the escort journey's deaths.
- **Voice:** Clear, polite, restrained, and determined.
- **Relationships:** Escort King Ju Gongsan was her paternal grandfather, Ju Hogun is her father, Heo Jun was her uncle, Sama Pyo was her former fiancé in a political engagement she accepted for her father's sake, Song Ilseom is her direct escort who accompanied her previous journey to Yeongin, and Jin Taekyung is a trusted ally; the Yongbong Escort Bureau has longstanding ties with Yeongin’s inhabitants.

### Namho.md

# Namho (남호)

- **Safe through:** Chapter 648
- **Aliases:** Elder Chao
- **Role:** Namho is an eighty-year-old non-Han Hidden Shadow Pavilion agent who spent more than fifty years operating under the cover of the Poison Flower Pavilion in Nanman and now serves as the Fire Dragon Pavilion’s guide.
- **Personality:** Duty-bound, pragmatic, observant, and willing to use theatrical violence and crude insults to protect an intelligence operation.
- **Voice:** Measured and serious in private, but loudly abusive and convincing when maintaining his local cover.
- **Relationships:** Namho is a Hidden Shadow Pavilion contact for Jin Taekyung and the Fire Dragon Pavilion, receives intelligence from the Pavilion Master, and knows the code used by the Thousand-Faced Fox.

### Sama Pyo.md

# Sama Pyo (사마표)

- **Safe through:** Chapter 648
- **Aliases:** Black Dragon Saber
- **Role:** Young Sect Leader of the Black Dragon Demon Gate, a Morning Star reputed to be no less than the Ten Dragons and Phoenixes, and a member of the Fire Dragon Pavilion.
- **Personality:** Outwardly courteous and smiling, inwardly calculating, but genuinely protective of Taishan and willing to redirect blame onto his subordinate.
- **Voice:** Polite and ingratiating in public, with sardonic humor and controlled evasiveness.
- **Relationships:** Sama Pyo commands the absolutely loyal Taishan, is Sima Gong's son, was Ju Hwaran's former fiancé in a political engagement, and has joined the Fire Dragon Pavilion while openly intending to use Jin Taekyung as a useful card; he is now openly hostile toward fellow member Song Ilseom.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 648
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord.

## Korean source

```text
＃649화



마법과 기계.

온갖 문명의 이기가 발달한 현대와 비교하자면, 무림은 확실히 생활하기 불편한 조건들로 가득하다.

마차에 앉아만 있어도 엉덩이와 허리를 박살 내는 천연 비포장도로.

당연히 스마트폰과 와이파이는 꿈도 꿀 수 없고 전기도 통하지 않는다.

그나마 유일한 방법이 있다면 직접 낙뢰를 맞는 것뿐인데, 전기와 목숨을 등가 교환해야 한다는 점에서 영 가성비가 좋지 않았다.

하지만 살아가는 데에는 아무런 지장이 없었다.

아니, 워낙 파리 목숨이었던지라 신경 쓸 틈도 없었다고 봐야 맞겠다.

그 후에도 뭐, 그럭저럭 괜찮았다.

누군가 말하길 의식주(衣食住)는 사람이 생활하는 데에 있어 가장 중요한 세 가지 요소라는데, 그런 의미에서 보자면 태원진가의 삼공자라는 신분을 가진 나는 제법 호화로운 생활을 누릴 수 있었으니까.

‘딱 한 가지만 빼고.’

나는 심각한 눈빛으로 내궁(內宮)에 속한 이민족 하인을 노려보았다. 아무리 쳐줘도 중학생쯤으로 보이는 어린 녀석이다.

“한 가지만 묻자. 잘 생각하고 대답해라.”

“예?”

“지금 나 한족이라고 무시하냐?”

눈을 동그랗게 뜬 하인이 손을 내저었다.

“아, 아닙니다. 소인이 어찌 감히…….”

“그런데 왜 이런 시궁창으로 날 데려왔지? 분명히 측간에 데려다 달라고 한 것 같은데.”

“이, 이곳이 측간인데요.”

“잘 생각한 뒤에 대답하라고 했을 텐데. 다시 한번 거짓말을 했다가는 네놈 집을 똥으로 가득 채워 주겠다. 중원의 문파 중에 개방이라고 들어 봤지?”

“예? 예. 그 왜, 걸인들로 이루어져 있다는 문파 아닙니까?”

“잘 알고 있군. 내 말 한마디면 거지새끼 수천 명……까지는 아니고 백 명 정도는 데려올 수 있어. 특히 궁기방이라는 놈은 냄새가 무지막지하지. 그놈들이 네놈을 포함한 구족(九族)을 똥지처참할 거다. 그러니까 날 당장 제대로 된 측간으로 안내해!”

내 호통에 화들짝 놀란 하인이 울먹거렸다.

“죄, 죄송합니다. 정말 죄송한데 여기가 그나마 깨끗한 측간인데요.”

빌어먹을. 설마 했는데 이 시궁창이 측간이었다니.

마주하기 싫은 진실을 깨닫자 눈앞이 캄캄해진다. 중원도 이 정도는 아니었는데.

“이런 야만인 새끼들…….”

“예?”

“됐다. 넌 이만 돌아가.”

죄 없는 하인을 돌려보낸 나는, 끔찍한 악취로 가득한 좁은 공간을 바라보다가 조심스럽게 발을 내디뎠다.

끼이이익.

발밑에 놓인 판자가 비명을 질러 댔다. 문까지 닫자 일 인용 화생방에 들어온 기분이다. 나는 굳은 얼굴로 내심 중얼거렸다.

‘설마 백상이 파 놓은 함정인가.’

무협 소설에서 많이 봤다. 엄청난 고수가 측간에서 암살당하는 장면, 뭐 그런 거.

하지만 판자 틈 사이를 확인한 뒤에는 그런 의심마저 사라졌다. 아무리 직업 정신이 투철한 살수라고 해도 여기에 숨어 있을 것 같지는 않았다.

‘아, 제발. 하느님. 부처님. 나무아미타불관세음아멘…….’

일 초가 십 년처럼 느껴지는 시간.

현실을 받아들인 내가 숨을 참으며 볼일을 보던 바로 그 순간이었다.

쐐액, 퍽!

모든 것이 찰나에 벌어진 일이었다.

반사적으로 손을 뻗어 무언가를 붙잡은 나는, 날카로운 파공성과 함께 낡은 문을 파고든 그것을 확인할 수 있었다.

‘화살?’

그리고 인지와 동시에, 나는 번개처럼 신형을 날렸다.

쾅!

문이 박살 나고 신선한 밤공기가 나를 반겼지만, 그것이 전부였다.

주위에는 아무것도 없었다. 그리 멀지 않은 곳에서 들려오는 환호와 악기 소리를 제외하면 아무것도.

하지만…….

‘남동쪽.’

나 정도의 무위라면 화살이 날아온 방향을 유추하는 것은 그리 어려운 일이 아니다. 방향을 짐작한 나는 망설임 없이 지면을 박찼다.

쾅! 쉬쉭!

바람이 전신을 스쳤다.

담벼락을 밟고 솟구쳐 가장 높은 전각 위에 오르자, 내궁의 전경이 발아래에 펼쳐진다.

곳곳을 환하게 밝히는 횃불. 연무장에서 연회를 즐기는 사람들. 도처에서 번을 서고 있는 전사들까지.

‘도대체 누구지?’

아무리 초절정의 경지에 올랐다고 해도 한계는 있다.

한눈에 파악하기에 내궁은 너무 넓었고, 그 안을 오가는 사람들의 숫자는 평소보다 몇 배나 많았다.

그리고 매우 유감스럽게도, 혹시 모를 상황을 대비하여 경계를 취하고 있던 남만야수궁의 전사들은 직업 정신이 투철한 축에 속했다.

“남서쪽! 전각 위!”

“웬 놈이냐!”

삐이이익!

날카로운 호각(號角)소리와 함께 내궁을 순찰하고 있던 전사들이 개미 떼처럼 밀려온다.

물론 사람보다 먼저 도착한 물건도 있었다.

쐐애애액! 쾅!

음, 일이 좀 꼬인 것 같은데.

발치에 처박힌 화살과 창을 바라보며 속으로 중얼거린 나는, 손에 들고 있던 화살을 다시 확인했다.

지금 막 날아온 것들과 비교하면 크기도, 형태도 동일하다.

하지만 내가 미처 발견하지 못했던 가장 큰 차이점이 있었다.

‘이건…….’

화살 깃에 매달려 있는 작은 가죽 뭉치.

그리고 그것의 존재를 깨달은 그 순간, 내가 서 있는 전각 아래에서 수십 개의 횃불이 타올랐다.

“네놈은 지금 포위되었다!”

“당장 정체를 밝히고 투항하라!”

타이밍 한 번 기가 막힌다. 아주 잠깐의 고민 끝에 결정을 내린 나는, 마음속으로 작게 명령어를 읊었다.

‘인벤토리 오픈. 수납.’

띠링.

시스템 특유의 맑은 종소리와 함께, 손아귀에 잡혀 있던 화살이 처음부터 존재하지 않았던 것처럼 사라졌다.

어둠 속에서 벌어지는 일들을 제대로 확인하지 못한 내궁의 전사들이 재차 고함을 내질렀다.

“마지막 권고다. 무장을 해제하고 투항하라!”

“당장 두 손을 머리 위로 올려! 그렇지 않으면 네놈의 대갈통에 화살 구멍을 내 주마!”

“…….”

멘트 살벌한 것 보소. 이게 현지 패치인지 뭔지 하는 그거냐.

남만식 NYPD의 윽박지름에 떨떠름하게 입맛을 다신 나는, 일단 그들이 시키는 대로 두 손을 머리 위로 올렸다.

어차피 내 신분을 알게 되면 오해야 금방 풀릴 테고, 적당한 변명 몇 마디면 끝날 일이다.

여기서 더 문제를 일으키면 나만 더 곤란…… 그런데 이놈들 표정이 왜 이러지?

‘어째 하나같이 귀신이라도 본 것 같은 얼굴들인데.’

그리고 다음 순간, 나는 깨달았다.

휘이잉.

어디선가 불어오는 바람에, 오늘따라 유난히도 하반신이 시원하다는 것을.

화륵.

“아, 아앗……!”

“허어……!”

스포트라이트처럼 나를 비추는 수십 개의 횃불.

그리고 잠시 본분을 잊은 전사들의 탄성을 들으며 나는 생각했다.

‘진짜 좆 됐네.’

바지 추스르는 걸 깜빡했다.



* * *



“이건 진심으로 궁금해서 묻는 건데.”

약 반 시진 만에 마주한 남호는 차분한 얼굴로 침착하게 입을 뗐다.

“너 이 새끼, 암천이지?”

“…….”

“암천이라서 자꾸 이러는 거지? 응?”

“…….”

“그렇지. 암천이 아닐 리가 없지. 아니면 무림맹 각주라는 놈이 남만까지 와서 왜 대족장 명치를 때리고, 달밤에 전각 위에 올라가서 하반신을 훤히 드러내고 있겠어. 애초에 입맹 조지려고 작정을 한 거지, 어? 내 말이 틀렸나?”

탁자 한 자리를 차지하고 앉아 뭔가를 씹고 있던 태산이 번쩍 손을 들었다.

“남호, 암천이 뭔가? 태산이 궁금하다.”

심유한 시선으로 태산을 응시하던 남호가 사마표를 향해 고개를 돌렸다.

“이건 정말 간절한 마음으로 묻는 건데, 저 쳐 죽일 놈의 아가리에 자물통을 채우려면 어떻게 해야 하나?”

“음.”

잠시 생각하던 사마표가 자리에서 일어났다.

“먹을 걸 좀 더 가져오겠소.”

“좋은 생각이군. 하지만 날카로운 통찰력을 지닌 은영각 요원으로서 한마디를 보태자면, 음식을 가져오지 말고 저놈을 음식 앞으로 데려다 놓게. 한마디라도 더 개소리를 들으면 미칠 것 같아서 그래.”

“…….”

“…….”

평소에도 제법 괴팍한 성격의 남호지만, 오늘의 그는 괴팍하다 못해 첨예하다.

오죽하면 눈치 없는 태산조차 겁먹은 얼굴로 사과할 정도였다.

“태산이…… 잘못했다…….”

무시무시한 눈빛으로 태산을 노려본 남호가 호흡을 가다듬었다.

나는 반사적으로 내 차례가 돌아왔다는 것을 깨닫고 먼저 입을 열었다.

“그……. 오해가 좀 있었습니다.”

“오해? 무슨 개 같은 놈의 오해?”

“아니, 말을 그렇게 하지 마시고요. 제 말을 좀…….”

“다 들었어! 다 들었다고! 심지어 본 사람도 있어! 그걸 본 사람이 이백 명이 넘어! 이러려고 주화란을 보낸 거냐? 그런 취향이야?”

“와, 그러고 보니까 주 소저 있었으면 큰일 날 뻔했네. 진짜 없어서 천만다행…….”

“네 이노오오오옴!”

쾅! 우직!

팔순 넘은 노인네가 힘도 좋다. 저 단단한 탁자를 때려 부수다니.

나는 본능적으로 박수를 칠 뻔한 것을 가까스로 참았다.

이 상황에서 한 번만 더 건드렸다가는 남호가 화병으로 죽을 것 같아서였다.

“남 노인. 진정하시오, 진정.”

“후욱. 훅.”

“숨 크게 들이마시고, 내쉬고. 좋소. 바로 그거요.”

사파에 어울리지 않는 걱정스러운 눈빛으로 남호를 다독인 사마표가 나를 향해 입을 열었다.

“어쨌든 각주, 지금 한 말이 사실인가?”

“그래, 인마. 다른 사람한테는 말 못 할 아주 약간의 오해가 있었…….”

“정말 이러려고 주 소저를 보낸 건가?”

“이 시벌 놈이.”

어쩌다 일이 이렇게 되었나. 이러다가 내 별호가 노출신룡으로 바뀔 판이다.

천장을 우러러보며 한탄한 나는 간신히 입을 열었다.

“그게 아니라. 그 전에 습격을 받았어.”

“뭐?”

“습격?”

“오, 태산이. 습격 뭔지 안다.”

순식간에 집중되는 세 명의 시선.

눈을 크게 뜬 남호가 황급히 물었다.

“언제? 어디서 말이냐?”

“측간에서요. 볼일 보고 있었는데 밖에서 화살이 날아오더라고요. 바로 나와서 흉수를 찾으려다 보니 이렇게 된 겁니다. 바지춤 추스를 틈도 없었어요.”

“그렇다면 흉수! 흉수는 잡았느냐?”

“잡았겠습니까? 멀리서 쏜 데다가 내궁에 사람이 워낙 많아서 실패했습니다.”

차라리 비수나 독침 같은 암기가 날아왔다면 쉬웠을 거다. 그런 종류의 무기는 거리가 훨씬 한정되어 있으니까.

하지만 활은 제법 먼 거리에서도 공격이 가능한 원거리 무기였고 그만큼 범인을 찾기 힘들었다.

“하지만 왜 처음부터 말하지 않았느냐? 습격이었다면 바로 궁주에게 고하여 흉수를 색출할 수 있었을 텐데.”

남호의 말도 일리가 있다. 아니, 차라리 사실대로 말할까 고민한 것도 사실이었다.

야밤에 바지 벗고 돌아다니는 변태 취급받는 것보다는 훨씬 나으니까.

하지만…….

“습격은 습격인데, 습격이 아니었던 것 같습니다.”

“뭐?”

“그게 무슨 소리지?”

“태산이. 습격은 아는데 습격이 아닌 습격은 모르겠다. 이해시켜 달라.”

“죽어. 제발 죽어.”

단번에 태산을 진압한 남호가 눈살을 찌푸렸다.

“습격이 아니었다?”

“네.”

“숨겨진 게 있었군. 더 자세히 말해 봐라.”

“나중에서야 알았는데, 화살에 희한한 게 달려 있더라고요.”

나는 대답과 함께 기감을 널리 퍼트렸다.

그리고 주위에 아무도 없는 것을 확인한 뒤, 마음속으로 작게 읊조렸다.

‘인벤토리 오픈. 소환.’

띠링.

맑은 종소리와 함께 손아귀에 잡히는 감촉.

나는 품에 넣어 두었던 손을 자연스럽게 꺼냈다.

그리고 측간을 향해 날아온 화살 한 자루와, 그 끝에 매달려 있던 작은 가죽 주머니를 풀었다.

돌돌 말려 있던 가죽이 탁자 위로 펼쳐진다.

어린아이의 손바닥보다 작은 그것에는, 깨알 같은 글씨로 이렇게 적혀 있었다.



[금일(今日). 인시(寅時). 서문(西門).]



그것은 전서였고, 정체를 알 수 없는 누군가가 내게 보내는 초대장이었다.
```

## Final English reading copy

```markdown
# Chapter 649

Magic and machines.

Compared to the modern world, where all kinds of conveniences born from civilization had developed, the Murim was certainly filled with conditions that made daily life inconvenient.

Natural, unpaved roads that could wreck your hips and back even while you were merely sitting in a carriage.

Smartphones and Wi-Fi were obviously out of the question, and there wasn’t even any electricity.

The only way to get some would have been to take a direct lightning strike, but that didn’t offer much value for money when you had to exchange your life for electricity.

Still, none of that caused any real trouble when it came to living.

No—my own life had always been so precarious that it would be more accurate to say I’d never had time to worry about such things.

After that, things were more or less fine.

Someone once said that food, clothing, and shelter were the three most important things in a person’s life. In that sense, I was able to enjoy a fairly luxurious lifestyle as the Third Young Master of the Jin Family of Taiyuan.

*Except for one thing.*

I glared with a grave expression at the non-Han servant belonging to the Inner Palace. Even giving him the benefit of the doubt, he looked about middle-school age.

“I’m going to ask you just one thing. Think carefully before you answer.”

“Yes?”

“Are you looking down on me because I’m Han Chinese?”

The servant’s eyes went round as he waved both hands.

“N-no, sir. How could this lowly one dare…”

“Then why did you bring me to this shithole? I’m pretty sure I asked you to take me to the latrine.”

“T-this is the latrine, sir.”

“I told you to think carefully before answering. If you lie to me one more time, I’ll fill your entire house with shit. You’ve heard of the Beggars’ Sect, one of the Central Plains’ sects, right?”

“Yes? Yes. Isn’t that the sect made up of beggars?”

“You know it well. With one word from me, I can bring several thousand beggars… Okay, maybe not several thousand. Around a hundred. And there’s one fellow named Gung Gibang whose smell is absolutely monstrous. They’ll shit-dismember you and all nine degrees of your kin. So take me to a proper latrine right now!”

The servant flinched at my roar, his eyes filling with tears.

“I-I’m sorry. I’m truly sorry, but this is the cleanest latrine we have.”

Damn it. I’d thought there was no way, but this shithole really was the latrine.

After realizing the truth I had desperately wanted to avoid, my vision went dark. The Central Plains had never been this bad.

“These savages…”

“Yes?”

“Never mind. You can go.”

After sending the innocent servant away, I stared at the narrow space filled with a horrifying stench, then carefully set one foot inside.

*Creeeak.*

The plank beneath my foot let out a shriek. Once I closed the door, it felt as though I had entered a chemical-warfare chamber for one. With a stiff expression, I muttered inwardly.

*Could this be a trap Baeksang dug for me?*

I had seen it plenty of times in martial-arts novels. A scene where some incredible master gets assassinated in a latrine, or something like that.

But after checking between the gaps in the planks, even that suspicion disappeared. No matter how devoted an assassin might be to his profession, I didn’t think anyone would hide in here.

*Please. God. Buddha. Namu Amitabha, Guanyin, amen…*

One second felt like ten years.

It was just as I had accepted reality and was holding my breath while doing my business.

*Whoosh—thud!*

Everything happened in an instant.

I reflexively reached out and seized the object that had punched through the old door with a sharp whistle.

*An arrow?*

The instant I recognized it, I shot into motion like lightning.

*Boom!*

The door shattered, and fresh night air welcomed me.

But that was all.

There was nothing around me. Nothing except the cheers and musical instruments I could hear from somewhere not too far away.

But…

*Southeast.*

For someone at my level, it wasn’t difficult to work out the direction from which the arrow had come. Once I had a general idea, I kicked off the ground without hesitation.

*Boom! Whoosh!*

The wind swept across my entire body.

I stepped onto a wall and leaped up, climbing onto the highest pavilion. From there, the whole Inner Palace spread out below me.

Torches brightly illuminated every corner. People enjoyed the banquet in the training ground. Warriors stood guard throughout the area.

*Who the hell was it?*

No matter how far one had risen into the Supreme Peak realm, there were limits.

The Inner Palace was too vast to take in at a glance, and there were several times more people moving through it than usual.

And unfortunately, the warriors of the Nanman Beast Palace, who had been on alert against any possible situation, took their professional duties very seriously.

“Southwest! On the pavilion!”

“What kind of bastard are you?”

*Peeeep!*

Along with the sharp sound of a whistle, the warriors patrolling the Inner Palace swarmed in like ants.

Of course, something arrived before the people did.

*Whoooosh! Boom!*

Hmm. Things seemed to have gotten a little complicated.

I glanced at the arrow and spear embedded near my feet, then checked the arrow in my hand once more.

Compared to the ones that had just flown at me, its size and shape were identical.

But there was one major difference I hadn’t noticed.

*This is…*

A small leather bundle hanging from the arrow’s fletching.

The moment I realized it was there, dozens of torches flared to life beneath the pavilion where I stood.

“You are surrounded!”

“Reveal your identity and surrender immediately!”

The timing was incredible.

After a very brief moment of thought, I made my decision and silently recited a command in my mind.

*Open Inventory. Store.*

*Ding.*

With the System’s distinctive clear chime, the arrow in my hand vanished as if it had never existed.

Unable to make out what had happened in the darkness, the warriors of the Inner Palace shouted again.

“This is your final warning! Disarm yourself and surrender!”

“Put both hands above your head right now! Otherwise, we’ll put an arrow hole through your skull!”

“…”

That was a pretty savage script.

Was this what they called a local patch?

I uneasily smacked my lips at the threats from the Nanman version of the NYPD, then raised both hands above my head as instructed.

Once they learned my identity, the misunderstanding would be cleared up quickly. A few reasonable excuses should be enough to end the matter.

If I caused any more trouble, I would only be the one in a worse position…

But why did all of them look like that?

*They look as though they’ve seen a ghost.*

Then, in the next moment, I realized.

*Fwoosh.*

A breeze blew in from somewhere, and I noticed that my lower half felt particularly cool tonight.

*Whoosh.*

“A-ah!”

“Good heavens…”

Dozens of torches shone on me like spotlights.

As I heard the gasps of the warriors who had temporarily forgotten their duties, I thought,

*I’m really screwed.*

I’d forgotten to get my pants back in order.

* * *

“I’m asking this because I’m genuinely curious.”

Namho, whom I met approximately half a shichen later, spoke calmly with a composed expression.

“You bastard, are you Dark Heaven?”

“…”

“You keep doing this because you’re Dark Heaven, right? Huh?”

“…”

“Of course. There’s no way you’re not Dark Heaven. Otherwise, why would the head of a Murim Alliance pavilion come all the way to Nanman, punch a great chieftain in the solar plexus, then climb onto a pavilion in the middle of the night and expose his lower half? You came here determined to screw up the alliance admission from the start, didn’t you? Am I wrong?”

Taishan, who occupied one place at the table and was chewing on something, suddenly raised his hand.

“Namho, what is Dark Heaven? Taishan is curious.”

Namho stared deeply into Taishan’s eyes before turning his head toward Sama Pyo.

“I’m asking this from the bottom of my heart. How do I padlock that fucking bastard’s mouth shut?”

“Hmm.”

After thinking for a moment, Sama Pyo rose from his seat.

“I’ll bring more food.”

“Good idea. But as an agent of the Hidden Shadow Pavilion with sharp insight, let me add one thing. Don’t bring the food here. Take that bastard to the food instead. I think I’ll go insane if I have to listen to even one more word of his bullshit.”

“…”

“…”

Namho was a fairly eccentric man even under normal circumstances, but today, he was more than eccentric.

He was razor-sharp.

He was so frightening that even clueless Taishan looked scared and apologized.

“Taishan… was wrong…”

Namho glared at Taishan with a terrifying gaze, then steadied his breathing.

I instinctively realized it was my turn and spoke first.

“Well… there was a bit of a misunderstanding.”

“A misunderstanding? What kind of dogshit misunderstanding?”

“Please don’t put it like that. Just listen to what I have to say…”

“I heard everything! I heard every last bit of it! There are even witnesses! More than two hundred people saw it! Did you send Young Lady Ju here for this? Is that your thing?”

“Wow, now that you mention it, it would’ve been a disaster if Young Lady Ju had been there. It’s a real blessing she wasn’t…”

“You little baaaastard!”

*Boom! Crack!*

That old man was over eighty, but he sure was strong. He had smashed apart that sturdy table with one blow.

I barely managed to stop myself from applauding on instinct.

If I provoked Namho one more time in this situation, he looked like he might die of anger.

“Elder Nam, calm down. Calm down.”

“Huff. Hah.”

“Take a deep breath, then let it out. Good. That’s it.”

Sama Pyo soothed Namho with a concerned gaze that didn’t suit an unorthodox faction, then turned to me.

“Regardless, Pavilion Master, is what you just said true?”

“Yeah, damn it. There was a very slight misunderstanding that I can’t exactly tell anyone else about…”

“Did you really send Young Lady Ju here for this?”

“You fucking bastard.”

How had things ended up like this? At this rate, my nickname would change to the *Naked Divine Dragon*.

I looked up at the ceiling and lamented before finally opening my mouth.

“That’s not it. I was attacked beforehand.”

“What?”

“An attack?”

“Oh, Taishan knows what an attack is.”

Three pairs of eyes focused on me at once.

Namho’s eyes widened as he hurriedly asked,

“When? Where?”

“In the latrine. I was doing my business when an arrow came flying from outside. I came out immediately to find the culprit, and this is how things ended up. I didn’t even have time to pull up my pants.”

“Then the culprit! Did you catch the culprit?”

“Do you think I did? It was shot from far away, and there were so many people in the Inner Palace that I failed to find him.”

It would have been easier if a dagger or poisoned needle had flown at me instead. Weapons like those had a much more limited range.

But a bow was a long-range weapon capable of attacking from quite a distance, which made finding the culprit that much more difficult.

“But why didn’t you tell us from the beginning? If it was an attack, you could have immediately reported it to the Palace Lord and had the culprit tracked down.”

Namho had a point. In fact, I had considered telling them the truth.

It would have been much better than being treated like a pervert wandering around at night with his pants off.

But…

“It was an attack, but I don’t think it was an attack.”

“What?”

“What does that mean?”

“Taishan knows about attacks, but Taishan does not know about attacks that are not attacks. Explain so Taishan understands.”

“Die. Please die.”

Namho silenced Taishan in a single stroke, then frowned.

“It wasn’t an attack?”

“Yes.”

“Then there was something hidden. Tell me in more detail.”

“I only found out later, but there was something strange attached to the arrow.”

As I answered, I spread my Qi Sense over a wide area.

After confirming that there was no one nearby, I silently recited another command in my mind.

*Open Inventory. Summon.*

*Ding.*

I felt something land in my hand.

I naturally pulled out the hand I had kept inside my robes.

Then I took out the arrow that had flown into the latrine and untied the small leather pouch hanging from its fletching.

The leather, which had been rolled up, unfurled across the table.

It was smaller than a child’s palm, and tiny letters had been written across it.

> Today. Insi[^1]. West Gate.

It was a missive—an invitation from someone whose identity I did not know.

[^1]: Insi is the traditional time period from three to five in the morning.
```

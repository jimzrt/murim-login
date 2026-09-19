<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0514.txt",
      "sha256": "a49c225bb34fe9920ea9a4da2f9a11b9ea2a53d69a9a1115bdb7117fd5655297",
      "bytes": 13189
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "b06d21fe30fdaab97cfa2192950ced1d12a54fdbd549a07cc3792f3bdf91e7ad",
      "bytes": 3932
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "12d2d0290365ca6085ec5f8d7be745aa086d7ac8356e8ce38c2f4aa034ade722",
      "bytes": 163946
    },
    {
      "path": "characters/Bingbing.md",
      "sha256": "61dff65884266d8ba64ee5bf1f59f7bb9d19bf8bbfe9c2f11dbee86490a428f7",
      "bytes": 422
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "07e2df5d551757e60b2062c8c4be02e850509209a6e5a7b988bffd83eb7d2753",
      "bytes": 553
    },
    {
      "path": "characters/Unnamed.md",
      "sha256": "133520c56d2751f7b1cc97e5f6f4f9f8a7bf7244cadaedece193fc00dd1f3bfe",
      "bytes": 831
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "b307fc1effa914a33ab323ed49da0b8cadf029b5fa5a2a8b3f6330f2350aa476",
      "bytes": 154892
    }
  ],
  "estimated_tokens": 9852
}
-->

# Durable State Update — Chapter 514

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 514. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 514. Profile updates may replace only one
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
  "chapter": 514,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 514,
    "continuity_sources": [514],
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
    "Jeok Cheongang's Heart Demon and the dark memories binding him have been expelled; he has entered a new realm and achieved Returned to Youth.",
    "Mungyeong is the Slaughter Saint and former Divine Physician, a Returned to Youth Supreme Peak master and the greatest assassin in history; Mu Song and five Water Dragon Stronghold subordinates know he is exceptionally powerful but not that he is the Slaughter Saint.",
    "Mungyeong is training Taekyung to refine the stability and precision of the violent internal energy produced by the Fire Gate Divine Technique through Rising on Duckweed, Crossing Water.",
    "Zhuge Feng's Demon-Sealing Formation blocks all mana from the exposed Gate by drawing in natural qi, but whether it is permanent and repeatable remains unresolved.",
    "Jang Taebo is the Jin Family of Taiyuan's Master of Ironcraft Hall and is summoning renowned artisans to process the Water God Dragon's remains.",
    "The New Murim Alliance has been publicly announced from Mount Song; Shaolin, Huashan, the Nine Sects and One Gang, and the Five Great Families are moving to join it, while the Black Dragon Demon Gate's Young Sect Leader has arrived in Henan and may be heading there.",
    "Taekyung has abandoned the shark shortcut and intends to reach Henan by his own strength.",
    "The Southern Heaven Demon Empress is traveling toward Yunnan and expects to cause further deaths.",
    "Jin Mukyung remains secluded in the training hall after losing to Cheongpung, refusing to emerge until he achieves a great accomplishment.",
    "Mu Song wants to aid the Murim Alliance, but the Seafaring King alone decides the Yangtze River Channel League's major matters; the League and Green Forest Alliance may become rear threats.",
    "The North Sea Ice Palace remains isolationist, while Jeok Cheongang believes the Nanman Beast Palace will probably support orthodox Murim because of its historical goodwill toward the Fire Gate Clan.",
    "A stranger capable of walking across the Yangtze's surface has approached Taekyung after he released the trained sharks."
  ],
  "continuity_sources": [
    513,
    512
  ],
  "open_questions": [
    "Will the Demon-Sealing Formation remain effective permanently, and can equivalent formations be installed repeatedly if more Gates appear?",
    "What is the Lord of Heaven's identity, and how is he connected to the dangerous force Taekyung associates with his original world?",
    "Where is the Southern Heaven Demon Empress ultimately headed, and what does she intend to do in Yunnan?",
    "Will the Nanman Beast Palace, North Sea Ice Palace, Yangtze River Channel League, and Green Forest Alliance support, ignore, or oppose the New Murim Alliance?",
    "Who is the stranger walking across the Yangtze, and why has he approached Taekyung?"
  ],
  "safe_through": 513,
  "temporary_decisions": [
    "Render 새외무림 as Outer Murim, 새외 as Outer Lands, 북해빙궁 as North Sea Ice Palace, 야수묘왕 as Beast Miao King, and retain Nanman Beast Palace for 남만야수궁.",
    "Render 소뢰음사 as Small Thunderclap Temple, 광풍사 as Mad Wind Society, 포달랍궁 as Potala Palace, 오독문 as Five Poisons Sect, 독곡 as Poison Valley, 천축 as India, and 갠지스강 as Ganges River.",
    "Render 파사국 as Persia, 회교도 as Muslims, 영웅건 as hero headband, 대막 as great desert, 귀염권 as Ghost Flame Fist, and 장성 as Great Wall.",
    "Retain sa-eo for 사어, shark for 상어, Old Master for 노야, this old man/I for 노부, Shark Water-Ski Team for 수상스키단, and swift ship for 쾌조선.",
    "Render 신 무림맹 as New Murim Alliance, 하후검가 as Hahou Sword Family, 사마외도 as demonic and heterodox arts, 흑룡마문 as Black Dragon Demon Gate, 소문주 as Young Sect Leader, 혈곤 as Blood Cudgel, and 도상호 as Do Sangho."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 태원진가   | **Jin Family of Taiyuan**        |
| 소림     | **Shaolin**                      |
| 무림맹    | **Murim Alliance**               |
| 십봉룡    | **Ten Dragons and Phoenixes**    |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 신법     | **movement technique**                           |                                                       |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 낭인     | **wandering martial artist**                     |                                                       |
| 사파     | **unorthodox faction**                           |                                                       |
| 중원     | **Central Plains**                               |                                                       |
| 문주     | **Sect Leader**                              |
| 소문주    | **Young Sect Leader**                        |
| 제자     | **Disciple**                                 |
| 태원     | **Taiyuan**            |
| 하남     | **Henan**              |
| 감숙     | **Gansu**              |
| 정마대전   | **Great Faction War**         |
| 대사      | **Master** for a senior Buddhist monk                           |
| 빙빙 | **Bingbing** | Name or nickname of the child in the Monster Wave footage. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 무명 | **Unnamed** | Dharma name given by Hong Dao; literally means having no name. |
| 섬서 | **Shaanxi** | Province bordering Shanxi. |
| 천자문 | **Thousand Character Classic** | Classical text Childeuk cannot complete. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 주신 | **God of Drinking** | Wipeng's drinking epithet. |
| 천자 | **Son of Heaven** | Honorific title for the Emperor. |
| 소림사 | **Shaolin Temple** | Temple invoked in Chulwoo’s comparison of Baek Museong’s conduct. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 아미타불 | **Amitabha** | Buddhist invocation spoken by the unidentified arriving group. |
| 신성 | **Morning Star** | Term in the summons referring to the Master of Morning Star. |
| 도도 | **Dodo** | Term for the Star-Array Grand Banquet's major gambling matches. |
| 태산북두 | **Mount Tai and Northern Dipper of the Murim** | Honorific description of Shaolin's standing in the Murim. |
| 선장 | **Zen staffs** | Staff weapons carried by the Hundred and Eight Arhats. |
| 아미 | **Emei** | Short form for Emei Sect. |
| 서협 | **Xixia** | Place in southwestern Henan where the Yangtze tributary ends. |
| 흑룡마문 | **Black Dragon Demon Gate** | Unorthodox faction from Gansu. |
| 혈곤 | **Blood Cudgel** | Sobriquet of Do Sangho. |
| 도상호 | **Do Sangho** | Blood Cudgel's personal name. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 무명 | 거한 | monk_to_attacking_dark_path_officer | Benefactor | deferential but frightened | Uses 시주 while pleading with the officer and insisting that he started the attack. |
| 소문주 | 혈곤 | Young Sect Leader addressing a hostile Peak master | Blood Cudgel | Informal and contemptuous | Calls him 혈곤 while offering silver in exchange for his submission. |
| 도상호 | 소문주 | Blood Cudgel addressing the Black Dragon Demon Gate Young Sect Leader | Boy | Rude and informal | Addresses him as 아해야 before challenging him. |

## Listed compact profiles

### Bingbing.md

# Bingbing (빙빙)

- **Safe through:** Chapter 450
- **Aliases:** None
- **Role:** Child fleeing the Monster Wave with her mother in the reconnaissance footage.
- **Personality:** Frightened after witnessing her mother's death.
- **Voice:** Childlike and panicked; cries out for Mommy.
- **Relationships:** Daughter of the woman killed by an Orc spear.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 513
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Unnamed.md

# Unnamed (무명)

- **Safe through:** Chapter 325
- **Aliases:** None
- **Role:** Young Shaolin monk and practical Disciple of Hong Dao; a Peak master who uses oversized Ten-Thousand-Year Cold Iron prayer beads and Arhat Fist, though he has not been formally accepted as a Disciple; entrusted with the Green Jade Buddha Staff by Hong Dao; confronts Han Su inside the Face-Wall Cave rather than surrendering the treasure.
- **Personality:** Naturally timid and introverted, but unable to control himself once angered.
- **Voice:** Timid, deferential, and polite, punctuated by Buddhist invocations.
- **Relationships:** Disciple in practice of Hong Dao; sent by Hong Dao to bring the Master of Morning Star; newly acquainted with Jeok Cheongang and Jin Taekyung.

## Korean source

```text
＃514화



천하 무림의 태산북두, 소림사(少林寺).

중원에 환란이 들이닥칠 때마다 그들은 가장 앞장서서 싸웠다. 천 년 전에도, 백 년 전에도 그러했고 수십 년 전 일어난 정마대전 때도 마찬가지였다.

그 대가로 무림의 어떤 문파보다도 많은 피를 흘려야 했지만, 소림사의 그 누구도 후회하지 않았다.

마땅히 해야 할 일이었으니까. 지금보다 밝은 미래를, 대의(大義)를 위하여 행한 일이었으니까.

그리고 그것은, 잘 닦인 가도(街道)를 가로지르고 있는 일단의 승려들 역시 마음에 품고 있는 뜻이었다.

쉬이이익!

거친 바람에 승려들이 걸친 황색 가사(袈裟)가 나부꼈다.

오늘은 한 줄기의 바람도 불지 않는 청명한 봄날이었으나, 승려들의 걸음을 따라 펼쳐지는 쾌속한 신법은 없던 바람까지 불어 일으키기에 충분했다.

“서협(西峽)이 보입니다.”

스무 명에 달하는 소림사의 승려들. 그중 가장 앞서가던 무승(武僧)의 말에 중년의 승려가 고개를 끄덕였다.

“다행히 늦지는 않겠구나.”

“예. 약속된 시각은 신시(申時) 무렵이니, 아직 한 시진 가까이 남았습니다.”

서협이 넓은 면적을 지닌 군현(郡縣)이라고는 하나 이들은 상당한 경지를 이룬 무승들. 서협의 나루터까지 한 시진이면 평소 걸음으로 이동해도 충분한 여유가 있다.

계산을 끝마친 중년 승려가 손에 든 선장(禪杖)을 흔들었다.

철그럭.

그에 담긴 의미를 알아차린 무승들의 발걸음이 우뚝 멈췄다.

쾌속하게 발휘하던 경신법을 이처럼 한순간에 멈출 수 있다는 것은 무공의 화후가 상당히 깊다는 뜻.

그런 그들의 모습을 만족스럽게 바라본 중년의 승려가 천천히 돌아섰다.

그곳에, 죽립을 깊게 눌러쓴 한 사람이 있었다.

“곧 대로에 접어들 터. 양민들이 불안해할 수도 있으니 지금부터 속도를 줄여도 되겠습니까.”

지극히 공손한 중년 승려의 말에, 죽립 아래로 굳게 다물어진 입술이 달싹였다.

“그리하십시오.”

도무지 나이를 짐작할 수 없을 만큼 잔뜩 쉰 목소리. 찰나 지간 중년 승려를 포함한 모두의 얼굴 위로 슬픔과 안타까움이 스쳤다.

“허락해 주셔서 감사합니다. 사……숙.”

그리고 아직도 익숙해지지 않은 그 호칭을 끝으로, 신형을 돌린 중년 승려와 무승들이 서협을 향해 다시 걸음을 옮긴 바로 그 순간이었다.

- 꺄아아아악!

- 사, 살인이다! 사람이, 사람이 죽었다!

저 멀리 희미하게 들려오는 비명과 외침.

고강한 공력을 지닌 중년 승려가 그 사실을 다른 제자들에게 알리기도 전에, 죽립을 눌러쓴 이가 불쑥 입을 열었다.

“아무래도, 걸음을 서둘러야겠군요.”

“……!”



* * *



쉬이이익!

바람을 가르며 날아드는 스무 개의 신형.

펄럭이는 황색 가사와 빠르게 가까워지는 많은 이의 굳은 얼굴에, 흑룡마문의 젊은 무인이 눈살을 찌푸렸다.

“소림(少林)이라…….”

마주치기 껄끄러운 상대다. 특히 요즘 같은 시기에, 단순무식한 수하가 대로변 한복판에서 사람을 죽였을 때는 더더욱 그렇다.

“이런 멍청한 녀석.”

퍽!

정강이를 얻어맞은 팔척장신의 거한이 앓는 소리를 냈다.

“소문주. 속하, 아프다.”

“그러라고 때린 거다. 내 조심하라고 했거늘, 어찌 그리 앞뒤 가리지 않느냐?”

“그놈. 죽어 마땅했다.”

“후우. 도무지 말이 안 통하는 놈일세. 됐다. 기왕 엎질러진 물, 어쩌겠느냐?”

“주워 담아야 하지 않겠소. 어떻게 해서든 말이오.”

딱딱한 누군가의 목소리에, 거한이 송아지 같은 눈을 깜빡였다.

“소문주. 속하. 아니다.”

“말하지 않아도 된다. 이미 알고 있으니까.”

입가에 빙긋 웃음을 띤 젊은 무인이 돌아섰다. 불과 다섯 걸음 앞, 굳은 얼굴의 중년 승려를 마주한 그가 포권을 취했다.

“소림의 고명하신 스님들을 뵙습니다. 특히 정호대사(丁虎大師)를 이리 빨리 뵙게 될 줄은 몰랐군요.”

중년 승려, 정호의 굵은 눈썹이 꿈틀거렸다.

“빈승을 아시는구려. 다만 초면인 듯한데.”

“초면은 맞지만, 위명은 익히 들었지요.”

“빈승에게는 위명이랄 것이 없소. 대사(大師)라 불릴 만한 사람도 아니고.”

“역시. 아버님께서 말씀해 주신 것처럼 겸손하신 분이시군요.”

“아버님?”

“언제인가 한 번 알려 주신 적이 있습니다. 소림에 실로 성격이 불같은, 아. 불심이 깊고 원칙을 철두철미하게 지키시는 어느 훌륭한 스님에 관해서 말입니다.”

젊은 무인의 시선이 정호의 손에 들려 있던 선장에 닿았다.

“물론 한 자루 선장을 귀신처럼 다룬다는 말씀도 하셨지요. 특이하게도 염주가 주렁주렁 매달린 선장 말입니다.”

“……아미타불. 눈썰미가 좋으시구려.”

“제가 생각한 분이라 다행입니다. 아니었다면 상당히 민망해졌을 테니까요.”

가라앉은 눈빛으로 젊은 무인을 응시하던 정호가 불쑥 입을 열었다.

“그것참 다행이오. 한데 이야기를 듣다 보니, 빈승도 여럿 짚이는 점이 있는 것 같소.”

“경청하지요.”

“시주의 복색은 틀림없이 감숙에 위치한 흑룡마문(黑龍魔門)의 것이고, 느껴지는 기세와 태도는 결코 범상치 않으니…… 필시 풍월로만 듣던 흑룡마문의 소문주가 분명하오. 맞소?”

젊은 무인이 빙긋 웃으며 고개를 숙였다.

“다시 인사 올립니다. 흑룡마문의 소문주. 사마표라 합니다.”

“흑룡도(黑龍刀)의 위명은 익히 들었소. 십봉룡에 비해 결코 모자람 없는 신성이라는 것도.”

정호의 등 뒤에 서 있던 승려들 사이로 작은 동요가 일었다.

그만큼 흑룡도라는 별호는 익히 알려져 있었고, 사파 무림에서도 세 손가락 안에 꼽는 세력을 자랑하는 흑룡마문의 소문주이니 배경도 대단한 셈이었다.

하지만 그들 중 누구도 보지 못했다. 고개 숙인 사마표의 입가에 스치는 비웃음을.

그리고 그가 다시 고개를 들었을 때, 사마표의 얼굴에는 만연한 웃음이 서려 있었다.

“실로 과찬이십니다. 정호대사께서 저 같은 무명 소졸을 이리 높이 평가해 주시니, 몸 둘 바를 모르겠군요.”

“다시 한번 말하지만, 빈승은 대사라고 불릴 만한 사람이 못 되오. 시주를 과대평가할 생각 역시 없고. 그저 입증된 사실을 이야기하는 것뿐이지. 다만…….”

정호가 피 웅덩이에 고꾸라져 있는 시신을 바라보며 말을 이었다.

“이 불행한 시주의 죽음에 관한 사실은, 아직 모르겠구려.”

사마표가 수염으로 까슬까슬한 턱을 문질렀다.

“이게 참, 말하자면 깁니다만.”

“걱정할 필요 없소. 더욱 빠른 방법이 있으니.”

철그럭.

정호의 신호에 날렵한 체구의 무승 하나가 앞으로 나와 시신을 살폈다.

소림에 몸담기 전, 낭인으로 활동하며 숱한 견식을 쌓은 그가 시신의 정체를 알아차리기까지는 그리 오랜 시간이 걸리지 않았다.

“혈곤(血棍)입니다.”

“혈곤 도상호? 틀림없느냐?”

“예. 머리가 으스러지긴 했으나 제자가 판단하기에는 확실합니다.”

“혈곤. 혈곤이라…….”

선장에 매어 둔 염주를 어루만지며 중얼거리던 정호가 사마표를 응시했다.

“시주께서는 알고 있었소?”

“무엇을 말입니까?”

“혈곤이 이틀 전, 섬서에서 무고한 상인 다섯을 죽이고 도주 중이었다는 것.”

“그런 일이 있었습니까.”

“인적 드문 야산에서 벌인 소행이라 안심을 했던 모양이오. 배짱 좋게 하남까지 온 것을 보면.”

“……어허, 이런 천인공노할 자를 보았나.”

사마표가 짐짓 눈살을 찌푸렸다.

하지만 그건 혈곤이 벌인 짓 때문이 아니라, 혈곤처럼 경험 많은 낭인이 작정하고 벌인 일을 불과 이틀 만에 신속하게 파악하고 전달한 정보력 때문이었다.

‘이것이 무림맹의 힘인가, 아니면 소림의 저력인가.’

혈곤 도상호는 제법 유명한 축에 드는 낭인이지만, 그것은 그의 손속이 잔혹하고 스스로에 대해 떠들고 다니기 때문이다.

훨씬 윗줄의 고수가 득실거리는 무림에서 혈곤 정도의 인물을 이렇게까지 상세하게 파악하고 있다는 것은, 거미줄처럼 촘촘한 정보망을 갖추었다는 증거였다.

‘썩 달가운 소식은 아닌데…… 하긴, 그런 일들이 있었으니.’

내심 중얼거린 사마표는 내색하지 않고 입을 열었다.

“다행입니다.”

“무엇이 말이오?”

“제가 엎지른 물이, 알고 보니 썩은 물이었으니 말입니다. 누가 마시기 전에 먼저 손을 쓴 모양새가 아닙니까.”

정호의 안광이 깊게 가라앉았다.

“시주는 그 사실을 모르지 않았소.”

“결과가 좋으니 잘된 것 아닙니까?”

“결과만큼이나 과정 역시 중요한 법. 무슨 말을 한들 사람들이 오가는 대로변에서 살인을 저지른 것은 현명한 처사가 아니었소.”

“위험한 상황이었습니다. 상대가 저를 죽이기 전에 죽여야 했습니다. 아, 물론 그것 역시 제 뜻이 아니었고요.”

사마표가 손을 들어 옆에 서 있던 팔 척 거한을 가리켰다.

“이 녀석이 범인입니다.”

거한이 퉁방울만 한 눈동자를 껌뻑였다.

“소문주. 사람인가.”

“사실은 명명백백하게 밝혀야지. 그 흉악하기 짝이 없는 대초자곤에 묻은 피나 닦고 변명해라.”

“그건. 맞다. 혈곤 죽임. 나다.”

“부디 대사께서 넓은 아량으로 이해해 주십시오. 이 녀석이 무공은 뛰어난데 머리가 좀…….”

손가락을 관자놀이에 대고 빙빙 돌리는 시늉을 하는 사마표를 말없이 응시하던 정호가 입을 열었다.

“시주는, 아니 흑룡마문은 이번 일에 관해 잘 설명해야 할 거요.”

“그럼요. 제가 수하를 제대로 다루지 못해 생긴 일이니 얼마든지 응하겠습니다.”

“시주도 알고 있겠지만, 근래 들어 분위기가 과히 좋지 않소. 특히 양민들은 불안에 떨고 있지.”

현재의 무림은 터지기 직전의 화약고와도 같았다.

천자문도 떼지 못한 일자무식의 촌로도 무림맹이 무림인들의 친목 단체가 아니라는 것 정도는 알았다.

정마대전 당시, 전란에 휘말린 것은 비단 중원의 무림인뿐만이 아니었으니까.

“이런 시기에 대낮의 대로변에서 공공연한 살인이 자행된다면, 안 좋은 시선들이 향할 수밖에 없소.”

“그 말씀, 명심하지요.”

“비록 이 일로 죽은 자가 죄를 짓고 도망치던 혈곤이라고는 하나, 위에서 문책이 있을지도 모르오.”

“기꺼이 해명하겠습니다.”

“근방의 양민들에게도 사과해야 할 거요.”

“그것 역시 걱정하지 않으셔도 됩니다. 원한다면 배상도 하지요.”

정호의 눈썹이 씰룩거렸다.

비록 무승이라고는 해도 오랜 세월 소림에 몸담으며 불자의 길을 걸었던 그다.

이런 일이 벌어졌다는 것도 달갑지 않았고, 소문으로 들은 흑룡마문의 소문주가 보이는 태도도 썩 좋게 보이지 않았다.

하지만 어쩌겠나. 겉으로나마 고분고분하게 고개를 끄덕이니 그저 돌아설 수밖에.

“그럼…… 이것으로 되었소.”

“이것도 인연인데. 잠시 자리를 옮기는 것이 어떻겠습니까?”

“아미타불. 아쉽지만 거절해야겠구려. 맞이하려는 객이 있어서.”

전혀 아쉽지 않은 표정으로 대답한 정호가 돌아서려던 바로 그 순간이었다.

“검.”

“음?”

“검을 쓰시는 분이 아닌 듯합니다만.”

쇠가 긁는 것처럼 잔뜩 쉰 목소리. 죽립을 깊게 눌러쓴 누군가가 말을 이었다.

“시주와는 인연이 없어 보이는 물건입니다. 원주인에게 돌려주시지요.”

“아, 이것 말입니까.”

사마표가 빙긋 웃으며 손에 쥔 검을 바라보았다.

“제 것입니다.”

“빈승의 눈에는 그리 보이지는 않습니다만.”

“실례지만, 스님은 누구십니까?”

“이것과는 아무런 연관도 없지요.”

사마표의 입가에 맺혀 있던 웃음이 흐릿해진 그때, 저 멀리서 누군가의 외침이 들려왔다.

“태원진가! 태원진가다!”
```

## Final English reading copy

```markdown
# Chapter 514

Shaolin Temple, the Mount Tai and Northern Dipper of the Murim.

Whenever turmoil descended upon the Central Plains, Shaolin had always been the first to fight. They had done so a thousand years ago, a hundred years ago, and again during the Great Faction War several decades earlier.

They had shed more blood than any other sect in the Murim as a result, but not a single person in Shaolin Temple regretted it.

It was what they had been meant to do. They had done it for a brighter future—for the greater cause.

And that was the conviction held in the hearts of the group of monks crossing a well-paved road.

Whoosh!

The yellow kasayas draped over the monks fluttered in the fierce wind.

It was a clear spring day without even a breath of wind, but the swift movement techniques carrying the monks forward were more than enough to stir up wind of their own.

“Xixia is in sight.”

There were twenty Shaolin monks. At the words of the martial monk leading them, a middle-aged monk nodded.

“Fortunately, we won’t be late.”

“Yes. The appointed time is around shenshi, so we still have nearly one shichen left.”

Although Xixia covered a broad area, these were martial monks who had reached a considerable realm. Even at their normal pace, a shichen was more than enough time to reach the ferry landing at Xixia.

Having finished his calculations, the middle-aged monk shook the Zen staff in his hand.

Clatter.

The martial monks understood the signal and came to an abrupt stop.

To halt movement techniques that fast in a single instant was proof that their mastery of martial arts had reached a considerable depth.

The middle-aged monk looked over them with satisfaction before slowly turning around.

Someone stood there, wearing a conical hat pulled low over their face.

“We’re about to enter the main road. The commoners may become anxious, so may we slow down from here?”

The middle-aged monk spoke with utmost respect. From beneath the conical hat, tightly closed lips moved.

“Please do.”

The voice was so hoarse that it was impossible to guess the speaker’s age. For a brief instant, grief and pity passed across the faces of everyone present, including the middle-aged monk.

“Thank you for granting permission, Martial… Uncle.”

And with that address, which still had not become familiar to him, the middle-aged monk and the martial monks turned toward Xixia and resumed walking.

That was when—

“Aaaaaah!”

“Murder! Someone’s been killed!”

Faint screams and shouts drifted from far away.

Before the middle-aged monk, whose internal energy was profound, could alert the other disciples, the person wearing the conical hat spoke abruptly.

“It seems we should hurry.”

“……!”

* * *

Whoosh!

Twenty figures flew through the air.

The sight of their fluttering yellow kasayas and the stern faces rapidly drawing closer made the young martial artist of the Black Dragon Demon Gate frown.

“So it’s Shaolin…”

They were an unpleasant group to encounter. Especially at a time like this, with a simple-minded subordinate having killed someone in the middle of a main road.

“What an idiot.”

Thwack!

The towering giant who had been struck in the shin groaned.

“Young Sect Leader. This subordinate hurts.”

“I hit you to make you hurt. I told you to be careful. Why do you always act without thinking?”

“He deserved to die.”

“Whew. There’s really no getting through to you. Fine. The water’s already spilled. What can we do?”

“We should pick it up somehow. No matter what.”

At someone’s curt voice, the giant blinked his large, calf-like eyes.

“Young Sect Leader. This subordinate. No.”

“You don’t need to say it. I already know.”

The young martial artist turned around with a faint smile on his lips. Five steps ahead, he faced the stern middle-aged monk and performed a fist-palm salute.

“It is an honor to meet Shaolin’s eminent monks. I never expected to meet Master Jung Ho so soon.”

The middle-aged monk, Jung Ho, twitched his thick eyebrows.

“You know me. Yet this seems to be our first meeting.”

“It is our first meeting, but I have often heard of your reputation.”

“There is no reputation worth mentioning where this humble monk is concerned. Nor am I worthy of being called a Master.”

“Just as my father told me. You really are a humble man.”

“Your father?”

“He once told me about a truly fiery-tempered monk in Shaolin—ah. I mean, a monk of profound Buddhist faith who follows his principles to the letter.”

The young martial artist’s gaze fell on the Zen staff in Jung Ho’s hand.

“He also told me that you wield a Zen staff like a demon. A staff with prayer beads hanging all over it, no less.”

“……Amitabha. You have a sharp eye.”

“I’m relieved you’re the man I had in mind. It would have been rather embarrassing otherwise.”

Jung Ho regarded the young martial artist with a grave gaze, then spoke abruptly.

“That is fortunate indeed. But as I listen to you, I find that several things seem to fit.”

“I’m listening.”

“Your clothing is unmistakably that of the Black Dragon Demon Gate of Gansu, and the aura and bearing you give off are far from ordinary. You must be the Young Sect Leader of the Black Dragon Demon Gate, whose name I have heard only through rumor. Am I right?”

The young martial artist smiled faintly and lowered his head.

“Allow me to introduce myself again. I am the Young Sect Leader of the Black Dragon Demon Gate, Sama Pyo.”

“I have often heard of the Black Dragon Saber’s reputation. I have also heard that you are a Morning Star in no way inferior to the Ten Dragons and Phoenixes.”

A small stir passed through the monks standing behind Jung Ho.

The sobriquet Black Dragon Saber was that widely known. And as the Young Sect Leader of the Black Dragon Demon Gate, a force counted among the three strongest unorthodox factions, Sama Pyo possessed an impressive background as well.

But none of them saw the sneer that brushed across Sama Pyo’s lips as he lowered his head.

When he raised it again, his face was covered by a broad smile.

“That is excessive praise. To receive such a high opinion from Master Jung Ho despite being an unknown nobody like me, I hardly know where to put myself.”

“I will say it again: I am not worthy of being called a Master. Nor do I intend to overestimate you. I am merely speaking of facts that have already been proven. However…”

Jung Ho looked toward the corpse lying facedown in a pool of blood and continued.

“I am not yet familiar with the facts surrounding this unfortunate man’s death.”

Sama Pyo rubbed his bristly chin.

“Well, it’s a rather long story.”

“There is no need to worry. There is a faster way.”

Clatter.

At Jung Ho’s signal, a martial monk with a slender build stepped forward and examined the corpse.

Before joining Shaolin, he had traveled as a wandering martial artist and accumulated a wealth of experience. It did not take him long to identify the corpse.

“It is Blood Cudgel.”

“Blood Cudgel Do Sangho? Are you certain?”

“Yes. His head was crushed, but I am certain.”

“Blood Cudgel. So it was Blood Cudgel…”

Jung Ho touched the prayer beads hanging from his Zen staff as he muttered, then turned his gaze toward Sama Pyo.

“Did you know?”

“Know what?”

“That Blood Cudgel killed five innocent merchants in Shaanxi two days ago and has been on the run ever since.”

“I was unaware of that.”

“He must have thought himself safe because he committed the crime in a remote mountain area. It seems he grew bold enough to come all the way to Henan.”

“……Good heavens. What a heinous man.”

Sama Pyo deliberately furrowed his brow.

But it was not Blood Cudgel’s crime that troubled him. It was the information network that had identified and relayed the actions of a seasoned wandering martial artist in only two days.

*Is this the power of the Murim Alliance, or Shaolin’s strength?*

Blood Cudgel Do Sangho was a fairly well-known wandering martial artist, but that was because his methods were cruel and he went around boasting about himself.

In a Murim filled with masters far above his level, knowing someone like Blood Cudgel in such detail was proof of an information network as dense as a spiderweb.

*Not exactly welcome news… Though, considering everything that has happened, I suppose it makes sense.*

Sama Pyo kept his thoughts to himself and spoke.

“That is fortunate.”

“What is?”

“The water I spilled turned out to be rotten water. Doesn’t that make it look as though I took care of it before anyone could drink it?”

Jung Ho’s eyes sank deeply.

“You were not unaware of that fact.”

“The outcome is good, so isn’t everything fine?”

“The process is as important as the outcome. No matter what you say, killing someone in the middle of a main road where people were coming and going was not a wise course of action.”

“It was a dangerous situation. He had to be killed before he killed me. Ah, of course, that was not my intention either.”

Sama Pyo raised a hand and pointed at the eight-foot-tall giant standing beside him.

“This fellow is the culprit.”

The giant blinked his enormous, round eyes.

“Young Sect Leader. A person?”

“Facts must be laid bare. Wipe the blood off that vicious two-section staff and make your excuse.”

“That. Correct. Blood Cudgel kill. Me.”

“Please understand him with your generous heart, Master. He is skilled in martial arts, but his head is a little…”

Sama Pyo pressed a finger to his temple and made a slow circling motion.

Jung Ho stared at him in silence before speaking.

“You, or rather, the Black Dragon Demon Gate, will have to explain this matter properly.”

“Of course. This happened because I failed to keep my subordinate in line, so I will cooperate in any way I can.”

“You know this already, but the atmosphere has been far from good lately. The commoners, in particular, are trembling with anxiety.”

The Murim of the present day was like a powder keg on the verge of exploding.

Even an illiterate old villager who could not get through the Thousand Character Classic knew that the Murim Alliance was not merely a social club for martial artists.

During the Great Faction War, it had not been only the martial artists of the Central Plains who were caught up in the war.

“If open murder is committed in broad daylight on a main road at a time like this, people will inevitably look upon us unfavorably.”

“I will bear that in mind.”

“Even if the person who died was Blood Cudgel, a criminal who was fleeing after committing a crime, those above us may still hold you accountable.”

“I will gladly explain myself.”

“You must also apologize to the commoners in the area.”

“You need not worry about that either. I will even pay compensation if they wish.”

Jung Ho’s eyebrow twitched.

Though he was a martial monk, he had spent many years in Shaolin walking the path of a Buddhist.

He was displeased that this had happened, and he was not particularly impressed by the attitude of the Black Dragon Demon Gate’s Young Sect Leader, whose reputation he had already heard.

But what else could he do? Since Sama Pyo was obediently nodding, at least on the surface, Jung Ho had no choice but to turn away.

“Then… that should settle the matter.”

“We have met by fate. Why don’t we move somewhere else for a while?”

“Amitabha. I regret that I must decline. I have a guest to receive.”

Jung Ho answered with an expression that showed no regret whatsoever and was just about to turn away when—

“The sword.”

“Hm?”

“You do not seem to be someone who uses a sword.”

The voice was hoarse, like metal scraping against metal. Someone wearing a conical hat pulled low over their face continued.

“That object appears to have no connection to you. Return it to its rightful owner.”

“Ah, this?”

Sama Pyo smiled faintly as he looked at the sword in his hand.

“It belongs to me.”

“It does not appear so to my eyes.”

“If you do not mind my asking, who are you, Monk?”

“That has nothing to do with this.”

The smile at the corner of Sama Pyo’s mouth faded.

Then, from far away, someone shouted.

“The Jin Family of Taiyuan! It’s the Jin Family of Taiyuan!”
```

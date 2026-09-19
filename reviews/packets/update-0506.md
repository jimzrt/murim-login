<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0506.txt",
      "sha256": "1f3d171a5464a96dd7acb50779f1ef3a6c5461c3d182ed0f272be5b457249b56",
      "bytes": 12897
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "763b68d6545f1d9f10b5b31a5ec6556df3def3e50eaf7a52fbd448df5067447d",
      "bytes": 5441
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "1d4cef5a53e8a98eb5182943fb17f1a6d743e8855edc86f0e9332f4f056751cf",
      "bytes": 160924
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "3aa31fe023e8bd1e4360fa9745d761addbff88842a55f5b5a6e4b7138756a76f",
      "bytes": 1630
    },
    {
      "path": "characters/Mu Song.md",
      "sha256": "ea51b449c92e3b554b38e8c33ad636720ec264b82bd93db290a66fba0f74530b",
      "bytes": 907
    },
    {
      "path": "characters/Mungyeong.md",
      "sha256": "acc209d4a3e951bc2388376a532d9af4960f12726585d2e294d8a5852fe4d13a",
      "bytes": 842
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "d55e1b559aab842913d6859ee4f86aff71a3a23ad89553d949f27b82a0965ae8",
      "bytes": 154523
    }
  ],
  "estimated_tokens": 10977
}
-->

# Durable State Update — Chapter 506

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 506. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 506. Profile updates may replace only one
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
  "chapter": 506,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 506,
    "continuity_sources": [506],
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
    "Mungyeong is the Slaughter Saint and former Divine Physician, a Returned to Youth Supreme Peak master whose assassin instincts remain formidable despite decades spent living as a medical apprentice.",
    "Zhuge Feng's Demon-Sealing Formation blocks all mana from the exposed Gate by drawing in natural qi, but whether it is permanent and repeatable remains unresolved.",
    "Jang Taebo is the Jin Family of Taiyuan's Master of Ironcraft Hall and is summoning renowned artisans to process the Water God Dragon's remains.",
    "War has begun, the New Murim Alliance is being formed at Mount Song, and Taekyung believes Dark Heaven deliberately planned the Gate incident.",
    "Jin Wikyung proposed the Hubei political arrangement through Hongcheon, the new Provincial Administration Commissioner and Prince Shangshan's hidden loyal retainer; the purge of Hubei's dark-path figures was intended to create an opportunity for rival unorthodox factions while warning them.",
    "Around one hundred Level 5 Mutated Minnows, locally called Blood Fish, were captured in the Gate's entrance waterways; the remaining population is unknown, and the fish kill one another.",
    "The Southern Heaven Demon Empress is traveling toward Yunnan and expects to cause further deaths.",
    "Jin Mukyung remains secluded in the training hall after losing to Cheongpung, refusing to emerge until he achieves a great accomplishment.",
    "Jin Taekyung's party has departed for Henan and the New Murim Alliance with Jeok Cheongang.",
    "Zhuge Gonghu's historical gamble directed the thousand-man Black Wind Corps through Mount Jiuhua, allowing Jeok Cheongang to annihilate it and gain the title of Fire King.",
    "The Wudang pursuit party has brought back remains attributed to the Killing Ghost, but their nature is neither beast nor human."
  ],
  "continuity_sources": [
    505,
    504
  ],
  "open_questions": [
    "Will the Demon-Sealing Formation remain effective permanently, and can equivalent formations be installed repeatedly if more Gates appear?",
    "What is the Lord of Heaven's identity, and how is he connected to the dangerous force Taekyung associates with his original world?",
    "Where is the Southern Heaven Demon Empress ultimately headed, and what does she intend to do in Yunnan?",
    "Will the fractured unorthodox factions accept the New Murim Alliance's invitation instead of joining Dark Heaven?",
    "What is the true nature and identity of the remains attributed to the Killing Ghost?"
  ],
  "safe_through": 505,
  "temporary_decisions": [
    "Render 산공독 as Energy-Dispersing Poison, 강력한 산공독 as Potent Energy-Dispersing Poison, 칠보추혼산 as Seven-Step Soul-Chasing Powder, 강력한 칠보추혼산 as Potent Seven-Step Soul-Chasing Powder, 심각한 복통 as Severe Stomachache, 고기 방패 as Meat Shield, 독 장아찌 as Poisoned Pickle, and 독의 as Poison Physician; retain secret martial arts, Master-Disciple relationship, Killing Ghost, and Fake Murim Martial Artist, and preserve 악 as Agh in the Quest interface; render 실명산 as Blindness Powder, 살천문 as Salcheonmun, and 스승의 날 as Teacher's Day.",
    "Render 기억의 파편 as Memory Fragment, 게이트 공략 as Gate Conquest, 텔레포트 as Teleport, 마법 as Magic, 흑풍단 as Black Wind Corps, 혈어 as Blood Fish, 변이된 송사리 as Mutated Minnow, 왜국 as Wa Kingdom, 인자 as ninja, and 절강 as Zhejiang; render 강력한 마비산 as Potent Paralysis Powder, 강력한 미혼산 as Potent Soul-Bewitching Powder, 전신 마비 as Full-Body Paralysis, 독성 흡수 as Poison Absorption, and 해독 as Detoxification.",
    "Render 시산혈해 as sea of corpses and blood and retain Old Master for 노야 with the established rough, profane Taekyung-Jeok banter; render 해시 as hour of the Pig, 한 식경 as half an hour, 타구봉 as Dog-Beating Staff, 창룡 as Azure Dragon, and 무량수불 as Infinite Life Buddha; preserve geun as the traditional weight unit with a footnote.",
    "Render 선천지기 as innate qi, 진원진기 as true-origin qi, 천기 as heavenly patterns, and 후천지기 as acquired qi.",
    "Render 심마 as Heart Demon, 비급 as martial arts manual, 송문고검 as Pine-Pattern Ancient Sword, 반로환동 as Returned to Youth, 생사부 as Book of Life and Death, 기막 as qi curtain, 무극태을검 as Martial Extremity Grand Unity Sword, 이룡 as Two Dragons, 원정 as Origin Essence, 내단 as inner core, 영험한 기운 as sacred energy, 대호 as great tiger, 취팔선권 as Drunken Eight Immortals Fist, 귀면 as Ghost Face, 요단강 as Jordan River, 진룡 as Jin Dragon, 마봉진 as Demon-Sealing Formation, 철기당 as Ironcraft Hall, 철기당주 as Master of Ironcraft Hall, 신룡 as Divine Dragon, 신(新) 무림맹 as New Murim Alliance, 면벽수련 as secluded meditation, 호법 as stand guard, 한나절 as half a day, 일다경 as the time it takes to drink a cup of tea, 촌각 as moments, 진맥 as take one's pulse, 은영술 as concealment techniques, 표창 as throwing blades, 철구 as iron balls, and 현천진인 as Perfected Being Hyeoncheon; render 장문 사형 as Sect Leader Senior Brother."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 적천강    | **Jeok Cheongang** |
| 검성     | **Sword Saint**               | Mae Jonghak    |
| 해상왕    | **Seafaring King**            | Pa Ryun        |
| 무림맹    | **Murim Alliance**               |
| 암천     | **Dark Heaven**                  |
| 장강수로맹  | **Yangtze River Channel League** |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 정파     | **orthodox faction**                             |                                                       |
| 사파     | **unorthodox faction**                           |                                                       |
| 강호     | **martial world**                                | Prefer “Murim” where the setting itself is meant      |
| 가주     | **Family Head**                              |
| 문주     | **Sect Leader**                              |
| 제자     | **Disciple**                                 |
| 선배     | **Senior**                                   |
| 하남     | **Henan**              |
| 사천     | **Sichuan**            |
| 정마대전   | **Great Faction War**         |
| 노부      | **this old man / I**                                            |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 대사      | **Master** for a senior Buddhist monk                           |
| 무송 | **Mu Song** | Lord of Water Dragon Stronghold and disciple of the Seafaring King. |
| 문경 | **Mungyeong** | Young medical apprentice and newly introduced passenger. |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 평화 | **Peace Guild** | Guild name. |
| 송이 | **Song-i** | Short form used for Song Song; Taekyung's love interest. |
| 숙부 | **Uncle** | Lee Seowol's shortened address for Cheol Mubaek. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 노환 | **infirmities of old age** | Jeok Cheongang's age-related illness. |
| 녹림맹 | **Green Forest Alliance** | Bandit alliance receiving Black Mountain Stronghold’s tribute. |
| 호남성 | **Hunan Province** | Province mentioned during Cheongpung's account of his travels. |
| 반로환동 | **Returned to Youth** | Possible explanation for an apparently young Supreme Peak master. |
| 중국 | **China** | Country from which Team Leader Choi’s video originates. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 호북 | **Hubei** | Province on Ju Gongsan's route from Guangdong to Henan. |
| 수룡채 | **Water Dragon Stronghold** | Major river stronghold belonging to the Yangtze River Channel League. |
| 선화아 | **Ship-Fire Boy** | Mu Song's sobriquet; literally a child who lights fires aboard a ship. |
| 채주 | **Stronghold Lord** | Title used for the lord of a water stronghold. |
| 장강 | **Yangtze** | The river controlled by the Yangtze River Channel League. |
| 장강일도 | **Yangtze One Saber** | Hwang Chung's sobriquet. |
| 동정호 | **Dongting Lake** | Lake under which Dangyang and Honghu Strongholds operated. |
| 장강수로채 | **Yangtze River Channel League** | River-bandit organization whose dead Taekyung recalls during the duel. |
| 호북성 | **Hubei Province** | Province where the chapter’s Dark Heaven incidents occurred. |
| 수신룡 | **Water God Dragon** | Legendary name for the true master of Dongting Lake; distinct from the modern Sea Serpent. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 수하 | 채주 | subordinate_to_stronghold_lord | Stronghold Lord | deferential | The subordinate calls Mu Song 채주 while reporting the nearby vessel. |
| 문경 | 무송 | survivor_to_savior_and_authority | Great Hero Mu Song | formal-deferential | Mungyeong credits Mu Song with saving him and asks him to spare Hwang Tae-gu. |
| 무송 | 문경 | stronghold_lord_to_young_passenger | you | gruff-but-considerate | Mu Song offers Mungyeong the right to decide Hwang Tae-gu's fate. |
| 문경 | 적천강 | old_acquaintances | Fire King | familiar and grave | The figure bearing Mungyeong’s name greets Jeok Cheongang by his established epithet. |
| 무송 | 적천강 | junior_martial_artist_to_legendary_martial_master | Great Hero Jeok | formal-deferential | Mu Song respectfully refers to Jeok Cheongang as 적 대협 while worrying that Jeok dislikes him. |
| 적천강 | 문경 | overwhelming elder to old acquaintance | you / little punk | mocking and threatening | Mocks Mungyeong's expression and threatens to poke out his eyes. |
| 적천강 | 무송 | legendary martial master to stronghold lord | you | gruff, coercive, and dismissive | Uses 자네 while ordering Mu Song to take the group only as far as Sichuan and leave the fast ship. |
| 적천강 | 수신룡 | legendary_martial_master_to_dying_spirit_beast | you | wary and trembling | Jeok asks what the Water God Dragon is after witnessing its mental communication. |
| 문경 | 수신룡 | physician_to_dying_spirit_beast | you | guarded and curious | Mungyeong asks whether the Water God Dragon knows him. |

## Listed compact profiles

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 505
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, and Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Mu Song.md

# Mu Song (무송)

- **Safe through:** Chapter 505
- **Aliases:** Ship-Fire Boy
- **Role:** Lord of Water Dragon Stronghold, a Peak master and the Seafaring King's second martial Disciple who controls major Yangtze river traffic in Sichuan, belongs to the Yangtze River Channel League's moderate faction, and is an exceptionally skilled ship captain.
- **Personality:** Ambitious, domineering, impatient with interruptions, and capable of pragmatic cooperation when circumstances demand it.
- **Voice:** Deep and low in private, shifting to dry authority or boisterous command when addressing subordinates and rivals.
- **Relationships:** Mu Song is a member of the Yangtze River Channel League's moderate faction; Hwang Chung, his senior and Uncle Hwang, was the League elder and Donghu Stronghold Lord who was killed in its destruction.

### Mungyeong.md

# Mungyeong (문경)

- **Safe through:** Chapter 505
- **Aliases:** Killing Ghost
- **Role:** Mungyeong is the legendary physician known as the former Divine Physician and Slaughter Saint, a Returned to Youth Supreme Peak master and the greatest assassin in history who passed the Divine Physician title to his Disciple.
- **Personality:** Compassionate, resolute, resourceful, and calm under extreme pressure.
- **Voice:** His Mungyeong persona is timid, deferential, and cheerful, while his Slaughter Saint voice is dry, impassive, and blunt.
- **Relationships:** Dong Feng is his Disciple, Jeok Cheongang is an old acquaintance whom Mungyeong helped break free of his Heart Demon, and Mungyeong was asked to look after and instruct Jin Taekyung after testing his basics.

## Korean source

```text
＃506화



화아아악.

저 멀리 불어오는 북서풍(北西風)에 돛이 크게 부풀었다.

험상궂은 근육질의 수적들은 박자에 맞춰 힘차게 노를 저었고, 빠르게 나아가는 뱃머리를 따라 좌우로 갈라지는 물결은 새하얀 포말을 만들며 사라지길 반복했다.

‘언제 그랬냐는 듯이 평화롭네.’

앞서 벌어진 여러 참극 때문인지, 오늘따라 바다처럼 끝없이 펼쳐진 장강의 풍경이 아름답게 느껴진다.

그런 내 마음을 읽은 것처럼 옆에 서 있던 적천강이 입을 열었다.

“오늘도 변함없이 거지 같은 풍경이군.”

“…….”

“지금 당장 천하에서 사라져야 할 것들을 두 개만 꼽자면 암천과 장강이지.”

마음을 읽긴 개뿔이.

뭐랄까, 참. 여러 의미로 변함이 없어서 좋다. 나는 붉은 머리카락을 흩날리고 있는 그를 바라보며 한숨을 내쉬었다.

“한숨 크게 쉬지 마라. 땅…….”

“한숨 좀 쉰다고 땅 안 꺼져요.”

“아니, 땅에 오르기도 전에 노부의 손에 뒈질 거라고.”

“이야. 예상을 까마득히 벗어나시네.”

“요새 통 못 봤다고 눈 제대로 뜨는 법을 잊은 모양이구나. 네놈의 눈깔 두 개에 각각 불, 손이라고 적혀 있는데 이를 어찌해야 할까.”

“존, 경. 인데요.”

“발, 경. 으로 처맞고 싶으냐?”

“아. 뇨.”

후웅, 빡!

“억!”

순간 눈앞에 번개가 쳤다. 짧은 비명과 함께 뒤통수를 감싸 쥐는 내 모습에 적천강이 흠칫 놀랐다.

“사, 살살 쳤는데 녀석이 엄살은.”

“아니, 이게 엄살로 보이세요? 골이 아주 쿵쿵 울리는구먼.”

“골이…… 울려?”

“제가 아무리 튼튼해도 사람인 이상 당연한 거 아닙니까?”

“……많이 아팠느냐? 이 정도로 세게 때릴 생각은 아니었는데. 어디 한번 보자.”

나는 똥 마려운 강아지처럼 안절부절못하는 적천강의 모습에 피식 실소를 흘렸다.

“왜, 왜 웃는 게냐?”

“그냥요.”

“……?”

“아, 다 나았다. 그보다 이대로면 하남까지 얼마나 걸리려나?”

아무렇지 않게 딴청을 피우는 내 모습에 적천강의 얼굴이 벌겋게 달아올랐다.

“이, 이놈이! 감히 노부를 가지고 놀아!”

빡!

“아, 진짜 아프다고요!”

“그냥 맞아!”

아프다. 정말로.

그런데 왜 맞는 와중에도 자꾸 웃음이 나오는지, 알다가도 모를 일이었다.

‘그리웠던 건가.’

그래, 아마 그랬던 것 같다.

간혹 별것 아니었던 일상이 그리워지는 순간이 있다.

내게는 어릴 적 그토록 따가웠던 아버지의 까슬까슬한 턱수염이 그랬고, 점점 느려지고 약해지는 적천강의 손바닥이 그랬다.

하지만 이제는 괜찮다. 비록 오래전 돌아가신 아버지는 사진으로밖에 볼 수 없지만, 점점 쇠약해지던 적천강은 힘을 되찾았다.

빡!

젊음과 함께 되찾은 적천강의 힘과 속도를 느끼자 자꾸 웃음이 흘러나왔다.

‘좋네. 이런 것도.’

빡! 빡! 빠악!

“……어, 잠깐만.”

“네놈이 감히 노부를 희롱해!”

“어억!”

생각해 보니까 엄청 좋진 않은 것 같다.

아니, 적당히 아파야지 이건 좀 선 넘었잖아.

이미 미친놈처럼 실실거리던 웃음은 씻은 듯이 사라진 지 오래.

계속해서 날아드는 적천강의 두꺼운 손바닥을 피해 필사적으로 몸을 비틀던 바로 그때였다.

“어…… 나중에 다시 와도 되겠습니까?”

갑자기 끼어든 목소리에 적천강의 움직임이 우뚝 멈췄다.

그 틈을 타 잽싸게 빠져나간 나는 목소리의 주인을 방패 삼아 뒤로 숨었다.

갑작스럽게 벌어진 상황에 내 소중한 고기 방패, 아니 선화아(船火兒) 무송이 질겁하며 외쳤다.

“이, 이보게. 후배!”

“후배. 오늘따라 그 말이 참 듣기 좋네요. 선배님.”

“이게 무슨 짓인가!”

“채주직을 계승 중입니다.”

“맞으려면 혼자 맞아!”

“이럴 때 도와주셔야죠. 후배 위하는 선배가 되고 싶지 않으십니까.”

“내가 도대체 왜…… 헉, 적 대협!”

아쉽게도 무송과 함께 맞는 그림은 완성되지 않았다.

흐름이 끊긴 적천강은 불끈 쥐었던 주먹을 내리치는 대신, 입맛을 다시며 무송을 위아래로 훑어보았다.

“뭐, 됐고. 무슨 일이냐?”

무자비한 구타를 예상하며 눈을 질끈 감았던 무송이 황급히 나를 떼어 내며 대답했다.

“부르셨다기에 왔습니다. 수하에게 전해 듣기로는 저를 찾으셨다고…….”

“노부가 말이냐? 언제?”

“부, 분명 언제쯤 하남에 도착하는지 물어보셨다고 들었습니다만.”

가만히 동태를 파악하고 있던 나는 손을 번쩍 들었다.

“어, 그거 제가 한 말 같은데요?”

아까 딴청을 피울 때 혼잣말처럼 중얼거린 말을, 수적 중 누군가가 듣고 무송에게 전한 모양이다.

“……후배였나.”

“네. 그냥 해 본 소리였는데.”

“그래, 그렇군.”

스산한 목소리를 들어 보니 잘못된 소식을 전한 그 수적은 오늘 장강 찍먹 형벌을 피할 수 없을 것 같다.

나는 심상치 않은 눈빛으로 어딘가를 노려보는 무송을 향해 입을 열었다.

“묻고 싶었던 것도 사실이었고요. 언제쯤 도착할 것 같습니까?”

비록 무송이 다른 노강호에 비교하면 새파랗게 젊은 나이라지만 장강에서 일평생을 보낸 베테랑 수적이다.

짧은 시간 동안 뭔가를 가늠하던 그가 입을 열었다.

“생각보다 시일을 많이 줄일 수 있을 것 같네. 오늘 같은 날씨가 이어진다면 아무리 길어도 열흘 안에는 서협(西峽)에 당도할 수 있겠지.”

“서협?”

그간 이곳저곳 부지런히 싸돌아다녔다고 해도, 천하 곳곳의 지명까지 일일이 파악할 수 있을 정도는 아니다.

무림에서는 워낙 눈코 뜰 새 없이 바쁘게 하루하루를 보냈고, 현대에서는 인터넷을 통해 공부를 해 보려 해도 지명과 특정 장소의 위치가 달라 어려움이 있었다.

‘동정호만 해도 그렇지.’

바로 이곳. 무림의 동정호는 호북성에 있지만, 현대 중국 지도에는 호남성에 위치한다.

이와 같은 오차는 두 세상이 비슷하지만 분명 다르다는 결정적인 증거 중 하나다.

“서협이면, 하남입니까?”

내 물음에 적천강이 고개를 끄덕였다.

“하남 남서쪽 끝자락이다. 노부의 기억에 의하면 그쯤에서 장강의 지류가 끝날 테니 그다음부터는 육로로 이동해야겠군. 맞느냐?”

“예. 적 대협께서 하신 말씀이 정확합니다.”

“정마대전 때 서협 인근을 지나갔던 적이 있지. 좋군, 좋아.”

반로환동으로 노환이 완치됨으로써 훨씬 정확해진 기억력이 흡족한 건지, 늦어도 열흘 뒤에는 장강을 벗어날 수 있다는 게 좋은 건지 모르겠다.

어쩌면 둘 다일 수도 있고.

입가에 만족스러운 웃음을 띤 적천강이 문득 무송을 바라보았다.

“그러고 보니 네 녀석도 고생이 많구나. 사천에서 호북, 거기에 이어 하남까지 가게 되지 않았느냐.”

무송이 씁쓸한 표정으로 고개를 저었다.

“이까짓게 고생이겠습니까. 덕분에 비명에 간 황 숙부와 수많은 형제의 눈을 편안히 감겨 줄 수 있게 되었으니, 누가 부탁하지 않아도 제가 마땅히 해야 할 일이지요.”

수신룡이 쓰러진 뒤, 무송을 비롯한 수룡채의 수적들은 시신들의 유골을 한데 모아 장강에 흩뿌렸다.

장강에서 살고 장강에서 죽었으니, 장강수로채의 수적다운 최후라 할 수 있었다.

“그들도 구천(九天)에서 감사하고 있을 겁니다.”

“무생이라 했느냐? 해상왕의 제자치고는 예의범절이 제법이군. 장강일도가 어린놈을 잘 키웠어.”

“제게는 혈육 같은 분이셨지요. 그리고 무생이 아니라 무송입니다. 적 대협.”

“그래, 무생.”

“…….”

혹시 노환이 치료가 덜 된 건가.

순간 그런 의문이 들었지만, 눈알을 부라리는 적천강의 모습을 보니 저건 그냥 우기는 거다.

이름이 뭐건 간에 본인이 무생이라 했으면 개명이라도 하라는 저 눈빛.

뿌리 깊은 유교 사상에 찌든 삼강오륜 마스터의 기세에 무송이 침을 꿀꺽 삼켰다.

“뭐, 왜?”

“아, 아닙니다. 아무것도.”

“그래, 무생.”

어디서 틀니 딱딱거리는 소리 안 들리냐.

보다 못한 나는 이름을 잃어버린 무송에게 구원을 손길을 내밀었다.

사실 그런 이유에서보다는, 개인적으로 궁금했던 일을 묻기 위해서가 더 컸지만.

“그런데 선배님은 다시 사천으로 돌아가실 생각입니까?”

“음?”

“알고 계시지 않습니까. 왜 우리가 하남으로 향하는지.”

내 질문에 담긴 뜻을 파악한 무송의 눈빛이 깊게 가라앉았다.

“무림맹에 참여하는지, 그게 궁금한 모양이군.”

“솔직히 말씀드리자면, 예. 그렇죠.”

“암천의 흉계에 의해 부모처럼 따르던 분과 수많은 형제가 비명횡사했네. 자네라면 어떨 것 같나?”

“무슨 수를 써서라도 원수를 갚을 겁니다.”

“나도 마찬가지일세. 당장이라도 달려가 무림맹에 손을 보태고 싶어. 하지만…….”

입술을 질끈 깨문 무송이 한숨처럼 말을 이었다.

“나는 장강수로맹이라는 큰 울타리에 속한 일개 채주일 뿐, 아무런 결정권이 없네. 본 맹의 중대사는 오직 한 분, 바로 내 스승이자 맹주이신 해상왕께서 결정하실 수 있어.”

강자가 대접받는 무림에서는 흔한 일이다.

일문의 문주, 혹은 가주가 갖는 결정권은 현대에서 철통같은 경영권을 손에 넣은 재벌 일가 오너보다 강력했다.

문제는…….

“근본 없는 수적 집단답군. 하기사, 정마대전 때도 이리저리 손익을 재던 놈들에게 뭔가를 바라는 것도 우스운 일이지.”

그래, 지금 적천강이 말한 바로 저 부분이다.

처음부터 장강수로맹은 정파가 아니었다.

천하 곳곳에 풀뿌리처럼 흩어져 있던 수적들이 맹(盟)의 깃발 아래 모여든 것은 해상왕이라는 강자의 통솔력과 각자의 이권을 보장해 주었기 때문이었다.

‘녹림맹(綠林盟)도 마찬가지라고 들었고.’

장강수로맹이나, 녹림맹이나 애당초 그들의 뿌리는 남의 것을 빼앗기 위해 모인 도적 집단이다.

다만 그들이 지금까지 세력을 유지하고 더욱 크게 성장할 수 있었던 이유는 정마대전에서 정파 무림의 손을 들어 승자가 되었고, 그 공으로 활동을 인정받았기 때문이다.

그나마 정마대전 당시 살아남았던 여타의 사파보다는 훨씬 대접이 괜찮지만, 그렇다고 풀뿌리가 나무뿌리로 변할 리는 없다.

적천강은 못마땅한 눈빛으로 장강의 물결을 바라보며 중얼거렸다.

“노부가 죽기 전에 이 빌어먹을 장강이 말라서 비틀어져야 할 텐데. 그래야 해상왕, 그놈 낯짝이 엉망진창이 되지. 쯧쯧.”

“…….”

“무생 네놈도 잘 생각하거라. 혹여 네 스승이 잘못된 선택을 할 수도 있으니.”

“……그럴 리 있겠습니까.”

면전에서 스승의 욕을 들었음에도 무송은 그저 씁쓸한 미소만 짓는 게 전부다.

그런 그의 반응을 보니 스승인 해상왕과 그리 화기애애한 관계는 아닐 것 같다는 짐작이 얼핏 들었다.

‘그나저나 이런 시점에서 장강수로맹과 녹림맹이 암천 쪽에 붙어 버린다면, 그때는 어떻게 되는 거지?’

답은 금방 나왔다.

제대로 골치 아파지는 거지, 뭐.

암천이 정면에서 다가오는 칼날이라면, 저 두 세력은 등 뒤에서 찔러 들어오는 비수다.

만약 저들이 다른 마음을 먹는다면 제아무리 강대한 정파 무림이라 할지라도 타격을 입을 수밖에 없는 것이다.

“검성이 골머리 꽤나 썩이겠군. 과연 그 두 놈들이 어떤 선택을 할지…….”

나와 비슷한 생각을 떠올렸는지, 적천강이 혼잣말처럼 중얼거리던 바로 그 순간이었다.

“둘이 아니라, 넷이겠지요.”

고개를 돌린 그곳에는, 차분한 표정의 문경이 서 있었다.
```

## Final English reading copy

```markdown
# Chapter 506

Fwoooooosh.

A northwest wind blowing in from far away made the sail billow wide.

The rough, muscular river bandits rowed powerfully in rhythm, and the waves splitting to either side of the swiftly moving bow repeatedly formed white foam before vanishing.

*Peaceful, as if nothing ever happened.*

Perhaps because of the many tragedies that had taken place recently, the seemingly endless expanse of the Yangtze looked beautiful today.

As though he had read my mind, Jeok Cheongang, who had been standing beside me, opened his mouth.

“Same shitty scenery as ever.”

“……”

“If I had to name only two things in the world that should disappear right now, they would be Dark Heaven and the Yangtze.”

So much for reading my mind.

What could I say? In many ways, it was nice that he had not changed.

I sighed as I looked at him, his red hair flying in the wind.

“Don’t sigh so loudly. The ground—”

“The ground won’t sink just because I sigh.”

“No. You’ll be dead by this old man’s hand before you even set foot on land.”

“Wow. You keep exceeding my expectations.”

“You seem to have forgotten how to use your eyes since it’s been so long since you last saw me. Your two eyeballs have ‘dis’ and ‘respect’ written on them. What should I do about that?”

“They say ‘re’ and ‘spect,’ actually.”

“Want me to beat some ‘feet-spect’ into you?”

“N. O.”

Whoom—whack!

“Ugh!”

Lightning flashed before my eyes.

At my short cry and the sight of me clutching the back of my head, Jeok Cheongang flinched.

“I-I barely hit you. What a crybaby.”

“Does this look like I’m exaggerating? My skull is ringing.”

“Your skull is… ringing?”

“Even if I’m sturdy, I’m still human. Isn’t that only natural?”

“……Did it hurt a lot? I didn’t mean to hit you that hard. Let me see.”

I let out a quiet laugh at the sight of Jeok Cheongang fidgeting like a puppy that needed to poop.

“Why—why are you laughing?”

“For no reason.”

“……?”

“Ah, I’m all better. More importantly, how long will it take us to reach Henan at this rate?”

At my attempt to casually change the subject, Jeok Cheongang’s face turned bright red.

“H-how dare you toy with this old man!”

Whack!

“Ah, that really hurt!”

“Just take it!”

It hurt. It really did.

And yet, I couldn’t understand why I kept wanting to laugh even while being beaten.

*Maybe I missed this.*

Yes. That was probably it.

There were moments when I missed ordinary things that had once seemed insignificant.

For me, it had been my father’s rough, prickly beard, which had irritated me so much when I was young.

And it had been the palm of Jeok Cheongang’s hand, which had gradually grown slower and weaker.

But it was all right now.

Although my father had died long ago and I could only see him in photographs, Jeok Cheongang, whose body had been gradually weakening, had regained his strength.

Whack!

Feeling the strength and speed Jeok Cheongang had recovered along with his youth made laughter keep spilling from my mouth.

*This is nice, too.*

Whack! Whack! Whaaack!

“……Wait a second.”

“How dare you mock this old man!”

“Ugh!”

Come to think of it, it wasn’t that nice.

There should be a reasonable limit to how much something hurt. This was crossing the line.

The grin I had been wearing like a lunatic had vanished without a trace long ago.

Just as I was desperately twisting my body to avoid Jeok Cheongang’s thick palms, a voice suddenly cut in.

“Um… would it be all right if I came back later?”

Jeok Cheongang’s movements stopped abruptly.

Taking advantage of the opening, I quickly slipped away and hid behind the owner of the voice, using him as a shield.

Caught in the sudden situation, my precious meat shield—no, Ship-Fire Boy Mu Song—cried out in dismay.

“H-hey, Junior!”

“Junior. That sounds especially nice today, Senior.”

“What are you doing?”

“I’m in the middle of inheriting the Stronghold Lord position.”

“If you’re going to get beaten, get beaten alone!”

“You’re supposed to help me at times like this. Don’t you want to become a Senior who looks after his Junior?”

“Why the hell should I—gasp, Great Hero Jeok!”

Unfortunately, the image of Mu Song and me getting beaten together never came to fruition.

His momentum interrupted, Jeok Cheongang lowered his clenched fist instead of bringing it down and smacked his lips as he looked Mu Song up and down.

“Never mind that. What is it?”

Mu Song had squeezed his eyes shut, expecting merciless violence. He hurriedly pulled me away before answering.

“I came because I heard you summoned me. One of my subordinates told me you were looking for me…”

“This old man summoned you? When?”

“I-I was told you had asked when we would arrive in Henan.”

I had been quietly assessing the situation. Now I raised my hand.

“Oh, I think that was me.”

When I had been muttering to myself while pretending nothing was happening, one of the river bandits must have heard me and passed the message on to Mu Song.

“……It was Junior?”

“Yes. I was just thinking aloud.”

“I see. I see.”

Judging by Jeok Cheongang’s grim voice, the river bandit who had passed along the wrong information probably would not escape a taste of the Yangtze today.

I turned toward Mu Song, who was glaring somewhere with a dangerous look in his eyes.

“To be honest, I did want to ask you. When do you think we’ll arrive?”

Although Mu Song was startlingly young compared with the other old martial-world veterans, he was still an experienced river bandit who had spent his entire life on the Yangtze.

After judging the situation for a short while, he opened his mouth.

“We should be able to cut the travel time considerably. If weather like today’s continues, we’ll reach Xixia within ten days at the latest.”

“Xixia?”

Although I had spent plenty of time roaming all over the place, I was nowhere near knowledgeable enough to know the names of every location throughout the land.

In the Murim, I had been too busy to look up every place name. In the modern world, I had tried studying them online, but it was difficult because the place names and the locations of specific sites were different.

*Dongting Lake alone is like that.*

The Dongting Lake right here was in Hubei Province, but on modern Chinese maps, it was located in Hunan Province.

Discrepancies like this were among the decisive proofs that the two worlds were similar, but definitely different.

“Is Xixia in Henan?”

Jeok Cheongang nodded at my question.

“It’s on the southwestern edge of Henan. If this old man remembers correctly, a tributary of the Yangtze ends around there. From then on, we’ll have to travel by land. Is that correct?”

“Yes. You are exactly right, Great Hero Jeok.”

“I passed near Xixia during the Great Faction War. Good. Very good.”

I couldn’t tell whether he was pleased that his memory had become far more accurate after his infirmities of old age had been cured through Returned to Youth, or because we would be able to leave the Yangtze within ten days at the latest.

Perhaps it was both.

With a satisfied smile on his lips, Jeok Cheongang suddenly looked at Mu Song.

“Come to think of it, you’ve had a hard time as well. You went from Sichuan to Hubei, and now you’re going all the way to Henan.”

Mu Song shook his head with a bitter expression.

“How could this be called hardship? Thanks to it, I can lay Uncle Hwang and the countless brothers who died untimely deaths to rest. It’s something I should do, whether anyone asks me to or not.”

After the Water God Dragon fell, Mu Song and the other river bandits of the Yangtze River Channel League gathered the remains of the dead and scattered them across the Yangtze.

They had lived on the Yangtze and died on the Yangtze. It was a fitting end for the river bandits of the Yangtze River Channel League.

“They must be thanking you from the afterlife.”

“Did you say your name was Mu Saeng? For a disciple of the Seafaring King, you have quite decent manners. Yangtze One Saber raised you well.”

“He was like family to me. And my name isn’t Mu Saeng. It’s Mu Song, Great Hero Jeok.”

“Right, Mu Saeng.”

“……”

Had Jeok Cheongang’s infirmities of old age not been completely cured after all?

The thought crossed my mind for a moment, but seeing his bulging eyes made it clear that he was simply being stubborn.

Whatever Mu Song’s actual name was, Jeok Cheongang’s eyes clearly said that if Jeok Cheongang called him Mu Saeng, Mu Song had better change his name to match.

Mu Song swallowed hard under the imposing aura of a master steeped in the Three Bonds and Five Relationships.[^1]

“What? Why?”

“N-no, it’s nothing.”

“Right, Mu Saeng.”

Could anyone else hear the clacking of dentures somewhere?

Unable to watch any longer, I extended a helping hand to Mu Song, who had lost his name.

Actually, I was more interested in asking something that had been on my mind.

“By the way, Senior, are you planning to return to Sichuan?”

“Hm?”

“You know why we’re heading to Henan, don’t you?”

Understanding what I meant, Mu Song’s expression grew somber.

“You’re wondering whether I’ll participate in the Murim Alliance.”

“To be honest, yes.”

“Dark Heaven’s scheme caused the death of the person I revered like a parent, along with countless brothers. What would you do in my place?”

“I’d do whatever it took to avenge them.”

“I feel the same. I want to rush there and lend a hand to the Murim Alliance right now. But…”

Mu Song bit down hard on his lip and continued with a sigh.

“I’m only a Stronghold Lord belonging to the large umbrella of the Yangtze River Channel League. I have no authority to make decisions. Only one person can decide the League’s major matters: my Master and Alliance Leader, the Seafaring King.”

It was common in the Murim, where the strong were treated with respect.

The authority possessed by the Sect Leader of a sect or a Family Head was even greater than that of the owner of a conglomerate family who held ironclad control over a corporation in the modern world.

The problem was—

“Typical of a rootless bandit organization. Then again, expecting anything from men who weighed their profits and losses even during the Great Faction War is ridiculous.”

Yes. That was exactly the part Jeok Cheongang had pointed out.

The Yangtze River Channel League had never been an orthodox faction.

The river bandits scattered throughout the land like grass roots had gathered beneath the banner of the League because of the leadership of a strong man named the Seafaring King and the guarantee of each group’s interests.

*I’ve heard the Green Forest Alliance is the same.*

The Yangtze River Channel League and the Green Forest Alliance had both originated as bands of thieves who gathered to take what belonged to others.

The only reason they had maintained their power and grown even larger was that they had sided with orthodox Murim during the Great Faction War and emerged victorious. As a reward, their activities had been recognized.

They were treated far better than the other unorthodox factions that had survived the Great Faction War, at least.

But that didn’t mean grass roots could become tree roots.

Jeok Cheongang gazed at the waves of the Yangtze with displeasure and muttered,

“Before this old man dies, I hope this goddamn Yangtze dries up and withers away. Then that bastard Seafaring King’s face will be a complete mess. Tsk, tsk.”

“……”

“You should think carefully too, Mu Saeng. Your Master might make the wrong choice.”

“……That seems unlikely.”

Despite hearing his Master insulted to his face, Mu Song did nothing more than offer a bitter smile.

From his reaction, I had a vague feeling that his relationship with his Master, the Seafaring King, was not particularly warm.

*But what would happen if the Yangtze River Channel League and the Green Forest Alliance sided with Dark Heaven at a time like this?*

The answer came quickly.

It would become a real headache.

If Dark Heaven was a blade approaching from the front, those two factions were daggers stabbing in from behind.

If they decided to harbor ulterior motives, even the mighty orthodox Murim would inevitably suffer a blow.

“The Sword Saint is going to have quite a headache. I wonder what those two will choose…”

Jeok Cheongang was muttering as though to himself, apparently thinking along the same lines as me, when a calm voice interrupted him.

“Not two. Four.”

I turned my head.

Mungyeong was standing there with a composed expression.

[^1]: The Three Bonds and Five Relationships are a traditional Confucian framework of social and familial duties.
```

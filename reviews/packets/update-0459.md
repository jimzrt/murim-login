<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0459.txt",
      "sha256": "1cbeee683c9773b85530040500ee7fa65b916832281b6ad7510eccd60328cbcc",
      "bytes": 12855
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "da9a875d68f77c4834e9cd2b77897cfc1acf86444068589b1e031b54da321990",
      "bytes": 3715
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "bc113e198e994316716e4db6fe6162b98d7df287cd76597c593fdde8e4fe4790",
      "bytes": 149934
    },
    {
      "path": "characters/Dongting Fisherman.md",
      "sha256": "fae7644a7e47b9a8f61416773027ffd7881951f7173a692c2e3ea7f2de3c4224",
      "bytes": 722
    },
    {
      "path": "characters/Gung Gibang.md",
      "sha256": "c77adccd1fb434f05bd495872c2f0f9f2fb0a6d0de033dc1001e37389488ae7d",
      "bytes": 662
    },
    {
      "path": "characters/Heaven-Shaking Venerable Nun.md",
      "sha256": "48ed99778a3ce122fa1ec04db33d55a94d3ebacc71d3629f46c5f8aade50ac4c",
      "bytes": 510
    },
    {
      "path": "characters/Hong Dao.md",
      "sha256": "3f743558dcd1633971b8d19ffbb9cff743dd57bc946e044bbd2b0bf63eb6a85a",
      "bytes": 1001
    },
    {
      "path": "characters/Honglan.md",
      "sha256": "5ed0edebccafc016982725d4d843d9f3bc7e21d68c591addc49272889b5f1db6",
      "bytes": 605
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "22e0b1624770d25299bf31fa0a1762cb4b1f755a40c9a1e0afa5e1d113d47ab8",
      "bytes": 1108
    },
    {
      "path": "characters/Ju Wongong.md",
      "sha256": "929a2e2b26fd5fdd4bfc9f3031fe8e4bfccdea31804b5abcad7b5fe4d1db6257",
      "bytes": 681
    },
    {
      "path": "characters/Prince Shangshan.md",
      "sha256": "af51caec66dd9ea8c33193eb15d49d733f62c23b66ae516b5a2a709e8e619be8",
      "bytes": 914
    },
    {
      "path": "characters/Tang Sadok.md",
      "sha256": "945cef1c9d2cee159e8b132e2ddeb26f2193623a4963d8cf64a1fbad02fda67d",
      "bytes": 758
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "3a4c08745f98d0d04477ed3357932c3a22de50f75a013ff5b6c3889d471fdb40",
      "bytes": 144532
    }
  ],
  "estimated_tokens": 11311
}
-->

# Durable State Update — Chapter 459

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 459. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 459. Profile updates may replace only one
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
  "chapter": 459,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 459,
    "continuity_sources": [459],
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
    "Taekyung completed the unavoidable Peak-grade Quest The Tragedy of Dongting Lake, rescued two people who were the only survivors found, and earned the Water Rescue Worker Title.",
    "Honglan survived the Dongting Lake disaster and regained consciousness; the other rescued survivor was still unconscious when Taekyung received the report.",
    "Jin Wikyung is acting as an inspector for the new Murim Alliance and is cooperating with Taekyung's investigation.",
    "The shared symbols between the Arch Lich's magic circle and Dark Heaven's formations remain unexplained.",
    "The Sea Serpent Society and three Yangtze River Channel League strongholds, including Donghu Stronghold, were destroyed, with more than a thousand casualties, while the perpetrators' whereabouts remain unknown.",
    "The Dongting Fisherman is believed to remain in Hubei Province and is suspected of being a Dark Heaven member involved in the Hubei atrocities.",
    "Wudang is responding to an unidentified killer demon responsible for more than thirty deaths, including twenty pilgrims on Mount Wudang.",
    "The Skeleton King's undead identity remains concealed, and Taekyung has ordered him to join Peace Guild under a prepared contract.",
    "Go Jun is expected to succeed Lee Jungryong as Ares Guild's captain and is searching China for Lee's holographic recorder.",
    "The captured Three Fiends is a former-generation great fiend and Supreme Peak Dark Heaven subordinate whom Taekyung is transporting alive to investigate possible codes or markings.",
    "Qingxia Hall is an influential Hubei social club formed by powerful families' children, and Ju Wongong is its exiled young master who defers to Prince Shangshan while Honglan conceals her real name.",
    "Beggars' Sect, Lower District Sect, and Zhuge Clan intelligence are searching for the people responsible for the Hubei massacres."
  ],
  "continuity_sources": [
    458,
    457
  ],
  "open_questions": [
    "What are the origin and purpose of the symbols shared by the Arch Lich's magic circle and Dark Heaven's formations?",
    "Who destroyed Donghu Stronghold and the related Yangtze River Channel League strongholds, why was no Moving Formation trace left, and was the destruction a diversion?",
    "Is the Dongting Fisherman a member of Dark Heaven, what role did he play in the Hubei atrocities, and who destroyed the boat in Dongting Lake?",
    "Is the killer demon attacking Wudang connected to Dark Heaven?",
    "What evidence is contained in Lee Jungryong's holographic recorder, and what are the terms of the Peace Guild–Wizard Guild agreement?"
  ],
  "safe_through": 458,
  "temporary_decisions": [
    "Render 익양루 as Yiyang Tower.",
    "Render 황철 as Hwang Cheol, 도립군 as Do Ripgun, 광수도귀 as Mad Water Saber Demon, 파랑호 as Wave Fox, 동정호 as Dongting Lake, and 사천혈사 as Sichuan Blood Tragedy.",
    "Render 살귀 as killer demon, 일급 낭인 as First Rate wandering martial artist, 삼괴 as Three Fiends, 대마두 as great fiend, and 마군 as Demon Lord.",
    "Render 시부럴 as “sibu-leol,” 시벌좌 as “Lord Fuck,” and 시부럴좌 as “Lord Sibu-leol.”",
    "Preserve the Skeleton King's grandiose, mock-offended voice and Taekyung's dry, profane humor; render 주원공 as Ju Wongong, 대죽산표국 as Daejuksan Escort Bureau, 형문검가 as Hyungmun Sword Family, 응성상회 as Eungseong Merchant Association, 천룡인 as Celestial Dragon, 사인교 as four-person sedan chair, 홍란 as Honglan, 가기 as singing courtesan, 구족 as the nine branches of kin, and 수상 구조대원 as Water Rescue Worker."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 혁무진    | **Hyuk Mujin**     |
| 굉도     | **Hong Dao**       |
| 법왕     | **Dharma King**               | Hong Dao       |
| 독왕     | **Poison King**               | Tang Taesang   |
| 해상왕    | **Seafaring King**            | Pa Ryun        |
| 하오문    | **Lower District Sect**          |
| 소림     | **Shaolin**                      |
| 암천     | **Dark Heaven**                  |
| 장강수로맹  | **Yangtze River Channel League** |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 강호     | **martial world**                                | Prefer “Murim” where the setting itself is meant      |
| 가주     | **Family Head**                              |
| 은인     | **Benefactor**                               |
| 일격     | **One Strike**                         |
| 상태               | **Status**                     |
| 매력               | **Charm**                      |
| 사천     | **Sichuan**            |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 공자      | **Young Master**                                                |
| 대사      | **Master** for a senior Buddhist monk                           |
| 방장      | **Abbot**                                                       |
| 동정어옹 | **Dongting Fisherman** | Publicly condemned the Yangtze River Channel League and disappeared three days before this chapter. |
| 궁기방 | **Gung Gibang** | Beggars' Sect Successor Beggar and finalist. |
| 경천신니 | **Heaven-Shaking Venerable Nun** | Former Emei Sect Leader and sole Supreme Peak master; killed on Mount Emei. |
| 홍란 | **Honglan** | Stage name of Ju Wongong's Lower District Sect singing courtesan; her real name is concealed. |
| 주원공 | **Ju Wongong** | Qingxia Hall leader who claims distant kinship with the Emperor. |
| 상산왕 | **Prince Shangshan** | The City Lord and a member of the imperial family who orders the luncheon. |
| 당사독 | **Tang Sadok** | Current Family Head of the Sichuan Tang Clan; also called the Myriad-Poison Asura. |
| 송이 | **Song-i** | Short form used for Song Song; Taekyung's love interest. |
| 성주 | **City Lord** | Official who sends the invitation for a gathering with young prodigies. |
| 주표 | **Zhu Bao** | Personal name of Prince Shangshan. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 태상가주 | **Grand Family Head** | Title held by the Azure Sky Sword King as head of the Nangong Family. |
| 소림사 | **Shaolin Temple** | Temple invoked in Chulwoo’s comparison of Baek Museong’s conduct. |
| 사천당문 | **Sichuan Tang Clan** | Martial clan cited for its poison-based cleansing method. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 당문 | **Tang Clan** | Short form for the Sichuan Tang Clan. |
| 아미 | **Emei** | Short form for Emei Sect. |
| 아미파 | **Emei Sect** | Murim sect in Sichuan. |
| 호북 | **Hubei** | Province on Ju Gongsan's route from Guangdong to Henan. |
| 소림혈사 | **Shaolin Bloodshed** | Past incident cited by Hwangbo Eom. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 장강 | **Yangtze** | The river controlled by the Yangtze River Channel League. |
| 해사방 | **Sea Serpent Society** | Hubei association formed by fishermen and boatmen; it was annihilated at Red Cliffs. |
| 동정호 | **Dongting Lake** | Lake under which Dangyang and Honghu Strongholds operated. |
| 청협방 | **Qingxia Hall** | Unofficial Hubei social club formed by influential families' children. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혁무진 | 궁기방 | squad_companion_to_Beggars_Sect_successor | Young Hero Gung | formal-polite, then pointed | Uses 궁 소협 while asking about the culprit and challenging Gung’s insults. |
| 호위 | 당사독 | guard_to_Family_Head | Family Head | formal-deferential | Uses 가주님 while reporting Jin Taekyung's request. |
| 궁기방 | 혁무진 | squad_companions | you; that lunatic | insulting-casual | Gung Gibang mocks Hyuk Mujin's injuries and calls him a lunatic for attacking the Third Fiend. |
| 주원공 | 홍란 | employer to kept singing courtesan | Honglan | commanding | Orders Honglan to greet Taekyung and presents her as the singing courtesan he keeps at his side. |

## Listed compact profiles

### Dongting Fisherman.md

# Dongting Fisherman (동정어옹)

- **Safe through:** Chapter 456
- **Aliases:** None
- **Role:** The Dongting Fisherman is a Supreme Peak master and public critic of the Yangtze River Channel League, a leading suspect in the Donghu Stronghold massacre and possible Dark Heaven member whose Lower District Sect records indicate that he remains in Hubei Province.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** The Dongting Fisherman opposed the Yangtze River Channel League and was monitored by the Lower District Sect for several years after friction with it, while current records place him in Hubei Province.

### Gung Gibang.md

# Gung Gibang (궁기방)

- **Safe through:** Chapter 458
- **Aliases:** Successor Beggar, Beggar Prince, pure-blooded beggar, ultimate beggar
- **Role:** Gung Gibang is the Beggars' Sect Successor Beggar and a unique eight-knot disciple.
- **Personality:** Vulgar, aggressive, and quick-tempered.
- **Voice:** Blunt, profane, and vividly threatening.
- **Relationships:** Gung Gibang is a rival finalist alongside Baek Woo and Zhuge Gyun who trades insults with Taekyung and uses Beggars’ Sect intelligence to investigate Tang Taesang’s murder and search for Dark Heaven’s Hubei forces.

### Heaven-Shaking Venerable Nun.md

# Heaven-Shaking Venerable Nun (경천신니)

- **Safe through:** Chapter 374
- **Aliases:** Blood Rakshasa
- **Role:** Former Emei Sect Leader and the sect's sole Supreme Peak master, killed on Mount Emei by a one-armed middle-aged man.
- **Personality:** Forthright and fearless against enemies.
- **Voice:** Not established.
- **Relationships:** Respected leader of the Emei Sect; she and three Emei Elders were killed in the same attack.

### Hong Dao.md

# Hong Dao (굉도)

- **Safe through:** Chapter 450
- **Aliases:** Dharma King
- **Role:** Abbot of Shaolin and the Murim's Dharma King; master of Unnamed and the only friend to whom Jeok Cheongang had opened his heart; after leaving the Star-Array Grand Banquet, he was found in a massive pit with both legs severed and catastrophic internal injuries, whispered final words to Jeok Cheongang, and died.
- **Personality:** Calm, responsible, quietly playful, and still regarded by Jeok as lazy for sleeping whenever possible.
- **Voice:** Quiet, deep, weighty, and resonant, with casual familiarity when speaking to Jeok Cheongang.
- **Relationships:** Old friend of Jeok Cheongang; master of Unnamed; before his death, entrusted the Green Jade Buddha Staff to Unnamed and used his final words to warn Jeok about Jongni Chu, Dark Heaven, Unnamed, and the Buddhist Staff; sends Unnamed to bring the Master of Morning Star to Shaolin.

### Honglan.md

# Honglan (홍란)

- **Safe through:** Chapter 458
- **Aliases:** None
- **Role:** Honglan is a Lower District Sect courtesan who uses a stage name while serving as Ju Wongong's singing courtesan.
- **Personality:** Discreet about her real identity and professionally alluring.
- **Voice:** Clear, pure, and alluring, with humble formal speech toward honored guests.
- **Relationships:** She is kept at Ju Wongong's side as a singing courtesan, belongs to the Lower District Sect, and can respond to Taekyung through Sound Transmission.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 458
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers and Vice Squad Leader of the Jin Dragon Squad.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Ju Wongong.md

# Ju Wongong (주원공)

- **Safe through:** Chapter 454
- **Aliases:** Qingxia Hall young master
- **Role:** Ju Wongong is an exiled Qingxia Hall young master and a distant imperial relative of the Zhu ruling house who was punished for embezzling wealth while abusing his imperial authority.
- **Personality:** Entitled, status-conscious, theatrical, and amused by violence until his own protection is overcome.
- **Voice:** Pompous and imperious, with formal declarations of rank and authority.
- **Relationships:** His Qingxia Hall entourage and four Peak guards obey him; he asserts kinship with the Emperor.

### Prince Shangshan.md

# Prince Shangshan (상산왕)

- **Safe through:** Chapter 454
- **Aliases:** None
- **Role:** The City Lord and a member of the imperial family; ten-year-old Prince Shangshan, whose personal name is Zhu Bao, is an exceptionally skilled young swordsman who has trained daily for three years.
- **Personality:** Earnest, admiring, and eager to emulate Jin Taekyung; despite his royal dignity, he shows openly childlike enthusiasm for martial arts and Taekyung's reputation.
- **Voice:** Archaic and formal in the manner of a historical drama, with openly eager and childlike reactions beneath his royal diction.
- **Relationships:** Prince Shangshan Zhu Bao is the Emperor's only younger full brother, and his token commands immediate deference from distant imperial relatives such as Ju Wongong; he admires Jin Taekyung and seeks to emulate him.

### Tang Sadok.md

# Tang Sadok (당사독)

- **Safe through:** Chapter 375
- **Aliases:** Myriad-Poison Asura
- **Role:** Current Family Head of the Sichuan Tang Clan, gravely wounded in the Three-Gate Bloodbath and recovering under medical care.
- **Personality:** Grim, cold, blunt, suspicious, and unsentimental, with fierce concern for the Tang Clan’s affairs.
- **Voice:** Hissing, curt, authoritative, and threatening.
- **Relationships:** Tang Taesang was his father and predecessor as Family Head, his unnamed nephew serves as Master of the Gatekeeper Pavilion, and Mimi is his cherished old friend and companion, currently entrusted temporarily to Cheongpung while the clan's future is uncertain.

## Korean source

```text
＃459화



꽃이 물에 젖었다고 하여, 그것이 지닌 본연의 아름다움마저 시드는 것은 아니다.

홍란 역시 마찬가지였다. 힘든 일을 겪은 탓에 초췌해 보였지만 그 모습조차도 한 송이의 수국(水菊) 같았다.

“은인을 뵙습니다.”

그 순간, 나는 흔히들 말하는 ‘옥구슬이 굴러가는 목소리’가 무엇인지 알 것 같았다.

화장기 하나 없는 얼굴은 눈이 부시도록 희었고, 길게 드리워진 속눈썹 아래에는 샛별 같은 두 눈동자가 있었다.

“허어.”

“어찌 이토록 아름다울 수…….”

곳곳에서 흘러나오는 탄성.

홍란의 미모에 감탄하던 이들이 내 눈빛에 황급히 입을 다물고 자리를 떴다.

수백의 인명이 수장(水葬)당한 와중에 보인 자신들의 행동이 부끄럽기도 했을 것이다.

다르게 생각하자면 홍란의 아름다움이 그러한 사실들을 잊을 만큼 대단하다는 뜻도 되겠지만.

‘이런 상황이 아니었다면, 나도 저들과 다르지 않았겠지.’

마음을 가다듬은 내가 입을 열었다.

“깨어나서 다행이네요. 상태는 어떻습니까?”

홍란이 살짝 고개를 숙이며 대답했다.

“비록 은인에 비할 바는 못 되나, 천녀(賤女) 역시 무공을 익힌 몸. 움직이는 데에는 큰 무리가 없는 듯합니다.”

내가 파악한 그녀의 무공은 일류에 간신히 턱걸이하는 수준.

완숙한 일류 고수라고 부르기에는 부족함이 있을지는 몰라도, 신체의 단련과 축기(縮氣)를 통해 공력을 쌓은 무림인의 기력은 평범한 양민들에 비할 바가 아니다.

‘천만다행이었지.’

홍란이 무인이라는 사실은 그녀 자신에게도, 그리고 함께 구해진 다른 한 사람에게도 천운이라 할 수 있었다.

나는 아직 자리를 지키고 있는 군관에게 물었다.

“주원공은 어디 있습니까?”

주원공. 요즘 같은 불온한 분위기 속에서도 동정호에 놀잇배를 띄운 팔자 좋은 방계 황족. 바로 그가 또 다른 생존자다.

“주 공자를 말씀하시는 거라면 철통같은 호위를 붙여 안전한 곳으로 옮겼습니다. 의원의 말에 의하면 일단 큰 고비는 넘겼으나, 언제 의식을 회복할지는 장담할 수 없다 하더군요.”

처음 동정호에 도착했을 때 사람들을 진두지휘하던 바로 그 군관이다.

호북성의 주요 구역 중 하나인 동정호의 안전과 수비를 맡은 그는 딱딱한 얼굴로 말을 이었다.

“이번 일을 알리자 성주께서도 크게 노하셨습니다. 비록 미수에 그쳤으나 황족 시해는 중죄 중의 중죄. 즉시 성내의 함대와 병력을 총동원하여 이 무엄한 역도들을 일벌백계……!”

“황족 시해가 목적이 아니었을 겁니다.”

“예?”

나는 당황한 군관을 응시하며 말을 이었다.

“암천(暗天)이라고. 혹시 들어 보셨을지 모르겠네.”

“암천이라면…… 근래 들어 무림에서 난동을 피우고 있다는 무뢰배 집단이 아닙니까?”

“무뢰배?”

실소가 튀어나오는 단어 선택이다.

소림혈사 이후 이미 민간에도 암천이라는 이름이 알려지기 시작했지만, 눈앞의 군관은 놈들이 얼마나 강하고 무서운 힘을 지녔는지 조금도 가늠하지 못하고 있었다.

곁에 서 있던 궁기방도 기가 찬 표정으로 입을 열었다.

“거, 군관 나리. 그 무뢰배 집단이 소림사 방장이신 법왕(法王) 굉도 대사를 죽인 건 알고 있소?”

“그, 그건.”

“사천당문의 태상가주이신 독왕(毒王) 당사독 대협도, 아미파의 경천신니께서도 비명에 가셨소. 강호를 떨어 울리던 전대 초절정 고수 세 분과 이천여 명에 달하는 무인이 죽었단 말이오. 그런데 무뢰배 집단?”

“그, 그런 소문을 듣긴 했지만, 어느 정도인지는 정확히…… 하면, 이 일이 암천이 벌인 짓이란 말입니까?”

“몰라도 정도가 있지. 허, 참. 지나가던 똥개가 웃겠네.”

“그쯤 해 둬.”

나는 손을 들어 궁기방을 저지했다. 그리고 어느새 부끄러움으로 얼굴이 붉게 달아오른 군관을 향해 말을 이었다.

“어쨌건 말하고 싶은 건, 놈들의 목적이 주원공이 아니었다는 겁니다.”

“그, 그렇게 생각하시는 근거가 뭡니까?”

“암천이 하고자 마음먹었다면, 주원공은 이미 이 세상 사람이 아니었을 테니까.”

“……!”

“원한다면 어떤 방식으로든 죽였을 겁니다. 대낮에 기습해도 막지 못할 텐데 굳이 동정호에 놀잇배를 띄울 때까지 기다렸다가 다른 선박들과 함께 처리한다? 심지어 표적이 죽었는지 살았는지 확실한 생사조차 확인하지 않고?”

암천에게 있어 주원공의 목숨은 보자기 속 물건과 같다. 마음만 먹으면 언제든지 넣었다 뺄 수 있는.

또한 굳이 죄를 짓고 귀양까지 온 방계 황족을 노릴 만한 이유도 마땅치 않았다.

혼란을 일으키기 위해서였다면 차라리 황제나 상산왕 주표가 더 매력적인 표적이다.

나는 단호한 목소리로 말했다.

“놈들의 목적은 황족 시해가 아닙니다. 펼쳐 놓은 그물에 어쩌다가 걸린 물고기 중 하나지.”

“그럼 도대체 무슨 목적으로…….”

“그건 흉수를 잡으면 자연스럽게 알게 되겠죠.”

“예?”

“모든 배후에 암천이 있다는 건 기정사실이고, 직접 이런 짓을 벌인 흉수를 말하는 겁니다.”

멍하니 입을 벌리고 있던 군관이 다급하게 물었다.

“대, 대협께서는 흉수가 누구인지 알고 계신단 말입니까?”

“짐작되는 사람이 있긴 한데…… 아무래도 직접 본 사람의 말이 정확하겠죠.”

나는 고개를 돌려 홍란을 응시했다.

주원공이 사경을 헤매는 지금, 그녀는 모든 것의 실마리를 풀 수 있는 열쇠를 쥔 유일한 목격자다.

“봤습니까?”

짤막한 질문이었지만 그것으로도 충분했다. 나를 비롯한 모두의 시선 속에서, 홍란의 붉은 입술이 스르륵 열렸다.

“네.”

“……!”

“……!”

삽시간에 좌중으로 퍼져나가는 동요와 충격. 그 사이에서 나는 주먹을 꽉 움켜쥐었다.

‘드디어.’

해사방으로부터 이어진 일련의 사건들. 지금까지 털끝 하나 보이지 않던 놈, 혹은 놈들이 모습을 드러내기 시작했다.

마침내 찾은 이 꼬리를 놓쳐서는 안 된다. 있는 힘껏 잡아당겨 몸통까지 끌어낸 뒤 처리해야 한다.

나는 지금까지 희생당한 수많은 이들의 시신들을 떠올리며 재차 물었다.

“본 그대로 말하세요.”

“그것이…….”

주름 하나 없이 매끈한 홍란의 이마에 얕은 골이 팬다.

당시의 상황을 떠올리는 듯, 잠시 머뭇거리며 호흡을 가다듬던 그녀가 입을 열었다.

“모든 일이 창졸 간에 일어났습니다. 한창 분위기가 무르익고 있는데 주위에 있던 군선 두 척이 촌각을 두고 침몰한 것이 시작이었지요.”

나는 홍란의 이야기에 귀를 기울였다.

주원공 역시 방계라고는 하나 엄연한 황족. 호위를 위해 따라붙은 군선 두 척은 갑작스러운 기습에 무너졌고, 한창 흥이 무르익고 있던 놀잇배 역시 혼란에 빠졌다.

“그러나 누구도 막을 수 없었어요. 분명 어떠한 것도 보이지 않았음에도 굉음과 함께 배가 기울더니, 어디선가 날아온 한 줄기 강기(罡氣)가 배를 휩쓸었고 그것으로 끝이었습니다.”

“강기……!”

“틀림없어요. 그 일격으로 주 공자를 호위하는 절정 고수들과 청협방(靑俠房)의 무인들이 대부분 죽었으니까요.”

당시의 상황이 눈앞에 그려지는 듯했다.

강기는 그 무엇보다 파괴적인 힘. 본 적 없는 이라 할지라도 강기를 마주하면 그 눈 부신 빛의 정체를 깨닫게 된다.

그것은 홍란도 마찬가지였고, 주원공의 호위 무사들과 청협방의 얼뜨기들로는 막을 수 없는 일격이었을 것이다.

끔찍한 기억을 떠올린 탓인지, 홍란의 목소리가 가늘게 떨렸다.

“하지만 마지막 순간 호위들이 목숨을 걸고 주 공자를 밀어 냈고, 저는 그분을 끌어안고 강물로 몸을 던졌습니다.”

홍란의 빠른 판단이 그녀 자신과 주원공을 살렸다.

공포로 몸이 굳어 버린 이들은 얼마 지나지 않아 대부분이 몰살당했고, 숨이 붙어 있던 자들 또한 깊은 밤의 추위와 추락하며 얻은 부상을 오래 견딜 수 없었다.

그리고…… 검게 물든 동정호의 강물 속에서 홍란은 빠르게 멀어지는 무언가를 보았다고 했다.

“사람이었어요. 단 한 사람.”

“……!”

꼬리가 모습을 드러내는 순간이다. 입술을 질끈 깨문 내가 재차 물었다.

“확실합니까?”

“제가 어찌 은인께 거짓을 고하겠습니까. 비록 찰나에 불과한 짧은 시간이었으나, 이 두 눈으로 똑똑히 보았습니다.”

홍란은 유일한 목격자이며, 일류의 경지에 이른 무림인이기도 하다. 그런 그녀가 확신할 정도라면 사실일 가능성이 높았다.

‘맞아. 놈이다.’

내 머릿속에 누군가에 대한 생각이 스치던 그때, 넋 나간 표정으로 우리의 이야기를 듣고 있던 군관이 불쑥 입을 열었다.

“지, 지금 다들 제정신이오? 아무리 무림인이라고는 하나, 이곳은 육지가 아니라 동정호요. 대해(大海)처럼 깊고 넓은 동정호란 말이오!”

“그걸 모르는 사람이 여기 있나?”

궁기방은 한숨처럼 중얼거렸고, 혁무진이 혀를 쯧쯧찼다.

“그래서요?”

“그래서긴 뭔 놈의 그래서! 내 귀하들과 같은 무림인들이 얼마나 신묘한 능력을 지녔는지는 익히 들었소만, 이건 너무 허무맹랑하지 않소이까.”

잔뜩 흥분한 군관은 침까지 튀겨가며 외쳤다.

“종종 마주쳤던 장강수로맹의 수적들도 그 정도는 아니오. 한데 이 넓은 강물 위를 어찌 그리 빠르게 헤엄칠 것이며, 대국의 군선을 비롯한 수십 척의 선박을 단신으로 수장시킬 수 있……!”

“그럴 수 있지요. 제가 생각하는 한 사람이라면.”

청아한 목소리가 울려 퍼졌다. 홍란이 모두의 시선 속에서 천천히 입술을 열었다.

“그는 물고기처럼 호흡하고 그보다 빠르게 헤엄치며, 수십 척의 선박을 능히 단신으로 침몰시킬 수 있는 수공(水功)의 고수지요. 귀관께서 알고 계신 수적들이 얼마나 대단한지는 모르나, 적어도 이 동정호에서만큼은 해상왕(海上王)이 온다 해도 그를 당해내지 못할 것입니다.”

홍란의 시선이 막사 너머 푸르른 강물을 향했다.

동정호. 천하에서도 손꼽는 역사와 풍광을 지닌 명승지. 그리고 일평생 동정호를 지킨 한 사람의 늙은 어부.

아니. 전대의 초절정 고수이자, 해상왕과 어깨를 나란히 하는 수공의 고수.

나는 조용히 그의 별호를 뇌까렸다.

“동정어옹(洞庭漁翁).”

“……!”

하오문의 정보가 맞았다. 동정어옹은 아직 호북성을 떠나지 않았다.

죽음을 위장한 채 환한 등잔 밑이라 할 수 있는 이곳, 동정호에 머무르며 모두의 의심과 시선을 피하고 있었던 것이다.

그리고 마침내, 나는 동정어옹이라는 암천의 꼬리를 발견했다.

‘드디어 여기까지 왔다. 이 빌어먹을 늙은이.’

이미 너무나도 많은 희생을 치른 상황. 더 늦기 전에 동정어옹을 붙잡아 암천의 행적과 계획을 샅샅이 밝혀내야 한다.

그것이 더 큰 참극을 막을 수 있는 유일한 길이었다.

그렇기에, 다음 순간 들려온 홍란의 한마디는 길을 밝히는 횃불과도 같았다.

“혹시 은인께서는 알고 계신가요? 동정어옹이 동정호 곳곳에 자신이 머무르는 비처(秘處)를 숨겨 두었다는 걸.”

“이런 말씀을 하시는 건, 혹시?”

“정확한 위치는 모르지만, 짐작이 가는 장소 몇 군데를 알고 있습니다. 준비를 마치신 후 말씀해 주시면 천녀가 직접 안내를 해 드릴 수 있어요.”

“……!”

나는 주먹을 불끈 움켜쥐었다. 그리고 곧장 자리를 박차고 일어났다.

“그곳으로 갑시다. 당장.”
```

## Final English reading copy

```markdown
# Chapter 459

A flower does not lose its natural beauty simply because it has been drenched by water.

The same was true of Honglan. She looked haggard after everything she had been through, but even that appearance was as lovely as a hydrangea blossom.

“It is an honor to see you, Benefactor.”

At that moment, I thought I finally understood what people meant when they described a voice as sounding like jade beads rolling across one another.

Her face, entirely free of makeup, was dazzlingly pale, and beneath her long lashes were two eyes like morning stars.

“Good heavens.”

“How can anyone be this beautiful…?”

Exclamations rose from every direction.

Those who had been admiring Honglan’s beauty hurriedly shut their mouths and left when they noticed my gaze.

Perhaps they were ashamed of behaving that way while hundreds of people had been drowned.

On the other hand, it could also mean that Honglan’s beauty was extraordinary enough to make them forget such a fact.

*If this weren’t the situation we were in, I wouldn’t have been any different from them.*

After composing myself, I spoke.

“I’m glad you’ve regained consciousness. How are you feeling?”

Honglan lowered her head slightly before answering.

“Although I cannot compare to my Benefactor, this lowly woman has also trained in martial arts. I do not seem to have much trouble moving.”

The martial arts I had sensed from her were barely at the First Rate realm.

She might not have been quite skilled enough to be called a fully matured First Rate master, but the vitality of a martial artist who had built up their body and accumulated internal energy was incomparable to that of ordinary civilians.

*Thank heavens.*

The fact that Honglan was a martial artist had been a blessing both for her and for the other person rescued alongside her.

I asked the military officer who was still standing nearby,

“Where is Ju Wongong?”

Ju Wongong. A carefree distant imperial relative who had taken a pleasure boat out on Dongting Lake despite the troubled atmosphere of the times.

He was the other survivor.

“If you mean Young Master Ju, we assigned him an ironclad escort and moved him somewhere safe. According to the physician, he has passed the most dangerous point for now, but they cannot say when he will regain consciousness.”

He was the same military officer who had directed everyone when we first arrived at Dongting Lake.

Responsible for the security and defense of Dongting Lake, one of the major areas of Hubei Province, he continued in his stiff voice,

“When we reported what happened, the City Lord was furious as well. Although they failed, attempting to assassinate a member of the imperial family is the gravest of crimes. We will immediately mobilize the entire fleet and all forces in the city and make an example of these insolent rebels—”

“The murder of an imperial family member was not their objective.”

“What?”

I stared at the confused officer and continued.

“They’re called Dark Heaven. You may have heard of them.”

“Dark Heaven…? Aren’t they a gang of thugs that has been causing trouble in the martial world recently?”

“A gang of thugs?”

A scoff escaped me at his choice of words.

The name Dark Heaven had begun to spread among ordinary people after the Shaolin Bloodshed, but the officer before me had no idea how powerful or terrifying they truly were.

Gung Gibang, who had been standing beside me, also spoke with an incredulous expression.

“Hey, Officer. Do you know that gang of thugs killed Master Hong Dao, the Abbot of Shaolin Temple and the Dharma King?”

“Th-that…”

“The Poison King, Tang Sadok, the Grand Family Head of the Sichuan Tang Clan, was killed too. So was the Heaven-Shaking Venerable Nun of Emei Sect. Three Supreme Peak masters from the previous generation who once shook the martial world, along with more than two thousand martial artists, are dead. And you call them a gang of thugs?”

“I-I have heard those rumors, but I did not know exactly how powerful they were. Then, are you saying that Dark Heaven was responsible for this?”

“There’s a limit to how ignorant a person can be. Good grief. Even a stray dog passing by would laugh.”

“That’s enough.”

I raised a hand to stop Gung Gibang. Then I continued speaking to the officer, whose face had turned red with embarrassment.

“Regardless, what I’m saying is that their objective was not Ju Wongong.”

“Th-then what grounds do you have for thinking that?”

“If Dark Heaven had wanted Ju Wongong dead, he would already be gone from this world.”

“……!”

“If they wanted to kill him, they could have done so by any means. He wouldn’t have been able to stop them even if they ambushed him in broad daylight. Why would they wait until he set a pleasure boat afloat on Dongting Lake, then destroy it along with all the other vessels? And why would they do so without even confirming whether their target was dead or alive?”

To Dark Heaven, Ju Wongong’s life was like an object inside a cloth bundle. If they made up their minds, they could put him in or take him out whenever they wanted.

Besides, there was no obvious reason for them to target a distant imperial relative who had committed a crime and been banished.

If they wanted to cause chaos, the Emperor or Prince Shangshan Zhu Bao would have been far more attractive targets.

I spoke in a firm voice.

“Their objective was not the murder of an imperial family member. He was simply one of the fish that happened to get caught in the net they cast.”

“Then what in the world were they after…?”

“We’ll naturally find out once we catch the culprit.”

“What?”

“I’m talking about the culprit who carried this out directly. The fact that Dark Heaven is behind everything is already certain.”

The officer, who had been staring blankly with his mouth open, hurriedly asked,

“G-Great Hero, are you saying that you know who the culprit is?”

“There is someone I suspect, but the testimony of the person who saw them directly would be more accurate.”

I turned my head and looked at Honglan.

With Ju Wongong hovering between life and death, she was the only witness who held the key to unraveling everything.

“Did you see them?”

It was a short question, but it was enough. With everyone’s eyes fixed on her, Honglan’s red lips slowly parted.

“Yes.”

“……!”

“……!”

Shock and agitation spread through the room in an instant. Amid the commotion, I clenched my fist tightly.

*Finally.*

The series of incidents that had begun with the Sea Serpent Society. The bastard—or bastards—who had remained hidden without revealing even a hair had finally begun to show themselves.

I couldn’t let go of this tail now that I had finally found it. I had to seize it with all my strength, drag it out until I reached the body, and deal with them.

Remembering the countless corpses left behind so far, I asked again.

“Tell us exactly what you saw.”

“It was…”

A shallow furrow appeared on Honglan’s smooth, unlined brow.

She seemed to be recalling what had happened. After hesitating for a moment and steadying her breathing, she began to speak.

“Everything happened in an instant. The festivities were in full swing when the two military ships nearby sank one after another, only moments apart. That was how it began.”

I listened closely to Honglan’s story.

Ju Wongong might have been a distant relative, but he was still a member of the imperial family. The two military ships assigned to escort him had been overwhelmed by a sudden ambush, and the pleasure boat, where the festivities had been reaching their peak, had fallen into chaos as well.

“But no one could stop it. Nothing was visible, yet the ship suddenly tilted with a tremendous roar. Then a single streak of Force flew from somewhere and swept through the vessel. That was all it took.”

“Force…!”

“I am certain. Most of the Peak masters guarding Young Master Ju and the martial artists of Qingxia Hall died from that single attack.”

The scene seemed to unfold before my eyes.

Force was one of the most destructive manifestations of martial energy. Even someone who had never seen it before would understand what that dazzling light was the moment they faced it.

Honglan was no different. It must have been an attack that Ju Wongong’s guards and the bumbling martial artists of Qingxia Hall had been powerless to stop.

Perhaps because she had recalled such a horrifying memory, Honglan’s voice began to tremble faintly.

“But in the final moment, the guards risked their lives to push Young Master Ju away, and I embraced him before throwing myself into the river.”

Honglan’s quick thinking had saved both herself and Ju Wongong.

Those whose bodies had seized up with terror were mostly slaughtered soon afterward, while those who were still breathing could not endure the cold of the deep night or the injuries they had suffered in the fall for long.

And then…

Honglan said that, amid the darkened waters of Dongting Lake, she had seen something rapidly moving away.

“It was a person. Just one.”

“……!”

The moment the tail revealed itself, I bit down hard on my lips and asked again.

“Are you certain?”

“How could I lie to my Benefactor? It was only for the briefest moment, but I saw it clearly with these two eyes.”

Honglan was the sole witness, and she was also a martial artist who had reached the First Rate realm. If she was certain, then it was highly likely to be true.

*That’s right. It was him.*

Just as thoughts of someone flashed through my mind, the military officer, who had been listening to us with a dazed expression, suddenly spoke.

“A-are you all out of your minds? No matter how powerful martial artists are, this is not land. This is Dongting Lake! Dongting Lake is as deep and vast as the open sea!”

“Does anyone here not know that?”

Gung Gibang muttered it like a sigh, while Hyuk Mujin clicked his tongue.

“And?”

“What do you mean, ‘and’! I have heard plenty about the miraculous abilities of martial artists like you, but this is absurd. Even the water bandits of the Yangtze River Channel League whom I have encountered were never capable of such feats. How could anyone swim so quickly across such a vast body of water, much less sink dozens of vessels single-handedly, including the Great Nation’s warships?”

“He could. If he is the man I’m thinking of.”

A clear voice rang out. Under everyone’s gaze, Honglan slowly opened her lips.

“He can breathe like a fish, swim faster than one, and easily sink dozens of vessels by himself. I do not know how formidable the water bandits you know are, but at least here in Dongting Lake, even the Seafaring King himself would be unable to stand against him.”

Honglan’s gaze turned toward the blue-green waters beyond the camp.

Dongting Lake. A scenic site known throughout the land for its long history and beautiful landscapes.

And one old fisherman who had guarded Dongting Lake all his life.

No. A Supreme Peak master of the previous generation, and a master of water arts who stood shoulder to shoulder with the Seafaring King.

I quietly murmured his alias.

“The Dongting Fisherman.”

“……!”

The Lower District Sect’s information had been correct. The Dongting Fisherman had not yet left Hubei Province.

He had faked his death and remained here in Dongting Lake, a place that could be called directly beneath a bright lamp, evading everyone’s suspicions and attention.

And at last, I had found Dark Heaven’s tail—the Dongting Fisherman.

*I’ve finally made it this far. You damn old bastard.*

We had already paid far too high a price in lives. Before any more time passed, I had to capture the Dongting Fisherman and uncover every detail of Dark Heaven’s movements and plans.

It was the only way to prevent an even greater tragedy.

That was why Honglan’s next words felt like a torch lighting the way forward.

“Do you happen to know, Benefactor, that the Dongting Fisherman has hidden secret places where he stays throughout Dongting Lake?”

“You’re saying that you might know where they are?”

“I do not know their exact locations, but I know several places where they might be. Once you have finished preparing, please tell me. This humble woman can guide you there herself.”

“……!”

I clenched my fist tightly. Then I immediately sprang to my feet.

“Let’s go there. Right now.”
```

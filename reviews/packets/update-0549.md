<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0549.txt",
      "sha256": "995153a44b227245635e3298358c96ccecc25a660fa57b859313145e2ec5785b",
      "bytes": 12998
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "66f6baa62950263aa9cf6b97827efc06a5b11c22c4a4fa0ebf729695154a15f1",
      "bytes": 4174
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "3c667f0bcf42efa3b76bcb60deb6ea3b0ced3ba41a52a4549ee1378dde3be14d",
      "bytes": 174118
    },
    {
      "path": "characters/Honglan.md",
      "sha256": "ab4cd9c29b7e8b55658fdfa24566712595b5a128f5447ba3c0656f9651bcb5b6",
      "bytes": 973
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "c143ba140d9529007bb45b191d2145a64730d2f2b7704bf6176d6f8e434938fa",
      "bytes": 1147
    },
    {
      "path": "characters/Ju Hwaran.md",
      "sha256": "928b89d09f24de0d7fba1d110809ce1f3608088e09d329aafa0e42d8f4ca057f",
      "bytes": 935
    },
    {
      "path": "characters/Sama Pyo.md",
      "sha256": "1acd6486281fc1b0546df98e3e917e85ae82a8568eaf8ca8115de62ec9ec5fee",
      "bytes": 840
    },
    {
      "path": "characters/Song Il.md",
      "sha256": "09bd70d7846832b6b462facb85895995e04163903e14803e6fe4724663f7d323",
      "bytes": 964
    },
    {
      "path": "characters/Song Ilseom.md",
      "sha256": "6b6ac84fba7465db69c0e1398c5024514a2aef6d4ce907c2f5853c80170d48d1",
      "bytes": 751
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "2cae7311958bb789737e6ef27ac8f2b54fd44338735a6dd0d003418fed973169",
      "bytes": 528
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "da7a0f36d3644731f927d26a782ad3b0419a695ed924eea713365e0f9cb3d704",
      "bytes": 165874
    }
  ],
  "estimated_tokens": 11112
}
-->

# Durable State Update — Chapter 549

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 549. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 549. Profile updates may replace only one
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
  "chapter": 549,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 549,
    "continuity_sources": [549],
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
    "The Mount Song Resolution restored the Murim Alliance; Mae Jonghak is Alliance Leader, Jeok Cheongang heads the Five Kings Hall, and Murong Yeonghwi oversees Murong Family defenses in Liaoning.",
    "The Two Dragons Pavilion remains divided into Jin Taekyung's Fire Dragon Pavilion and Cheongpung's Azure Dragon Pavilion, with Taekyung now ordered to lead the Fire Dragon Pavilion's first mission to Nanman.",
    "Jin Taekyung is a Supreme Peak master with Three Flowers Gather at the Crown, advanced Qi Sense, exceptional resistance to monster Fear, and public S-rank-level recognition while retaining an A-rank license.",
    "Cheongpung is master of the Azure Dragon Pavilion, creator of Mimi Step, and caretaker of Mimi, whose condition was recently examined by Mungyeong.",
    "Mungyeong ended Taekyung's direct training and assigned him the final task of incorporating martial principles into his learned martial arts.",
    "Zhuge Feng's Demon-Sealing Formation still blocks mana from the exposed Gate, while Jang Taebo processes the Water God Dragon's remains.",
    "Dark Heaven remains an enormous monster-like threat capable of causing rifts and creating mutants; the mechanism behind Jang Sam's transformation remains unresolved.",
    "The Southern Heaven Demon Empress is believed by Taekyung to be moving toward the suspected next target, while Song Ho's dispatch there has received no reply for more than seven days.",
    "The Black Dragon Demon Gate remains a major unorthodox power; Sama Pyo is its Young Sect Leader and Black Dragon Saber, with Taishan as his giant subordinate.",
    "Jin Wikyung is Taekyung's eldest brother and has accepted that Taekyung keeps important secrets, asking to hear them when the crisis is over.",
    "Song Ho remains Chief of the Hidden Shadow Pavilion and has confirmed that its network had already considered the suspected target after the Hubei incidents.",
    "Jeok Cheongang and Mae Jonghak now treat Taekyung's warning about a monster catastrophe as credible enough to justify immediate action."
  ],
  "continuity_sources": [
    548,
    547
  ],
  "open_questions": [
    "What is the Lord of Heaven's identity, how is he connected to the dangerous force Taekyung associates with his original world, and how can Dark Heaven open Gates?",
    "What will Taekyung's party find in Nanman, and what does the Southern Heaven Demon Empress intend there?",
    "What is the outcome of the duel between Jeok Cheongang and Nangong Cheon, the Azure Sky Sword King?",
    "Why did Ju Hwaran and Sama Pyo's political engagement end?",
    "What process created Jang Sam's mutant form, and can Dark Heaven's mutants absorb human energy?"
  ],
  "safe_through": 548,
  "temporary_decisions": [
    "Render 고월루 as Gowolru, 곤륜운룡 as Kunlun Cloud Dragon, 학우 as Hak Woo, 이룡각 as Two Dragons Pavilion before its renaming, 화룡각 as Fire Dragon Pavilion, 청룡각 as Azure Dragon Pavilion, 협 as chivalry, 인의 as humanity, 협객 as knight-errant, 홍학루 as Honghakru, 홍매 as Hongmae, 호거아 as Tiger Giant Child, 도산검림 as a mountain of sabers and a forest of swords, 영물 as spiritual creature, 전도 as complete map of the realm, and 공자후 아크바르 as Confucius Akbar.",
    "Render 탈진 as the capitalized System status Exhaustion; retain Ten Dragons and Phoenixes, Blazing Flame Divine Dragon, Dark Heaven, Murim Alliance, and Old Master.",
    "Render 황보세가 as Hwangbo Family, 소가주 as Lesser Family Head, 은비화 as Dagger Hidden Flower, and 전음 as Sound Transmission.",
    "Preserve the chapter's blunt profanity, financial-therapy humor, monster-comparison humor, Mae Jonghak's carefree 'That can happen' refrain, Taekyung's five-tenths/fifty-fifty phrasing, and Jeok Cheongang's ball-staking humor.",
    "Render 청룡각주 as Azure Dragon Pavilion Master, 오왕전주 as Five Kings Hall Master, 문 할아버지 as Grandpa Mun, 정기 as vital essence, 변이체 as mutant, 시취 as corpse stench, 십단(九團) as Ten Squads—Nine Squads in the characters, and 남만 as Nanman."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 혁무진    | **Hyuk Mujin**     |
| 송일     | **Song Il**        |
| 주화란    | **Ju Hwaran**      |
| 은비화    | **Dagger Hidden Flower**      | Ju Hwaran      |
| 암천     | **Dark Heaven**                  |
| 남만야수궁  | **Nanman Beast Palace**          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 심법     | **cultivation technique**                        | Especially internal cultivation                       |
| 낭인     | **wandering martial artist**                     |                                                       |
| 마교     | **Demonic Cult**                                 |                                                       |
| 중원     | **Central Plains**                               |                                                       |
| 문주     | **Sect Leader**                              |
| 소문주    | **Young Sect Leader**                        |
| 상태               | **Status**                     |
| 사천     | **Sichuan**            |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 소저      | **Young Lady**                                                  |
| 홍란 | **Honglan** | Stage name of Ju Wongong's Lower District Sect singing courtesan; her real name is concealed. |
| 사마표 | **Sama Pyo** | Young Sect Leader of the Black Dragon Demon Gate. |
| 송일섬 | **Song Ilseom** | Young escort captain of the Yongbong Escort Bureau; distinct from Song Il of Zhongnan. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 대한민국 | **Korea** | Country reference. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 벽곡단 | **fasting pills** | Food-substitute pills found in the hidden cave where Cheol trained. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 트롤 | **Troll** | Monster species with extraordinary regenerative ability. |
| 일각 | **fifteen minutes** | Quarter of a shichen; used for the remaining completion time. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 운남 | **Yunnan** | Region from which Jongni Chu comes. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 화란 | **Hwaran** | Familiar short form of Ju Hwaran. |
| 유엽도 | **willow-leaf saber** | Saber wielded by Song Ilseom. |
| 표왕 | **Escort King** | Epithet of Ju Gongsan. |
| 추혼객 | **Soul-Chasing Guest** | Song Ilseom’s former epithet; he was known by it ten years earlier. |
| 일원 | **One Origin** | Named Tang Clan organizational unit in Tang Sadok's mobilization order. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 남천마후 | **Southern Heaven Demon Empress** | Title Honglan uses when revealing her identity. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 새외 | **Outer Lands** | Lands outside the Central Plains and its Murim. |
| 흑룡마문 | **Black Dragon Demon Gate** | Unorthodox faction from Gansu. |
| 식경 | **half an hour** | Time limit given for the requested reports. |
| 귀주 | **Guizhou** | Region whose Murim representatives send a delegate. |
| 호거아 | **Tiger Giant Child** | Epithet for Taishan. |
| 화룡각 | **Fire Dragon Pavilion** | New name chosen for Taekyung's pavilion. |
| 영물 | **spiritual creature** | Known non-human creature contrasted with unheard-of monsters. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 송일섬 | 주화란 | escort_captain_to_young_bureau_head | Hwaran | urgent and familiar | Calls out 화란아 while urgently warning Ju Hwaran before stepping into the confrontation. |
| 주화란 | 혁무진 | rescued_survivor_to_benefactor | Benefactor | formal-deferential | Hwaran includes Mujin among the Benefactors when greeting Taekyung's companions. |
| 주화란 | 송일섬 | bureau_head_to_escort_captain | Captain Song | formal and prosecutorial | Uses his office title, then his personal name, while exposing and confronting him. |
| 주화란 | 사마표 | former_fiancés | Young Sect Leader | formal and guarded | Hwaran formally greets her former fiancé. |
| 사마표 | 태산 | Young Sect Leader to subordinate | Taishan | informal and patronizing | Sama Pyo calls Taishan by name while ordering him to leave. |
| 태산 | 사마표 | subordinate to Young Sect Leader | Lord | crude and deferential | Taishan uses 주군 while obeying Sama Pyo. |

## Listed compact profiles

### Honglan.md

# Honglan (홍란)

- **Safe through:** Chapter 483
- **Aliases:** None
- **Role:** Honglan is a Lower District Sect courtesan who uses a stage name, served as Ju Wongong's singing courtesan, and identifies herself as the Southern Heaven Demon Empress.
- **Personality:** Discreet about her real identity and professionally alluring.
- **Voice:** Clear, pure, and alluring, with humble formal speech toward honored guests.
- **Relationships:** Honglan is kept at Ju Wongong's side as a singing courtesan, belongs to the Lower District Sect, lost her clan and parents overnight as a child, can respond to Taekyung through Sound Transmission, is the sole surviving eyewitness to the Dongting Lake attack who knows several possible locations of the Dongting Fisherman's hidden refuges, corrupted the benevolent imugi in Dongting Lake and used it to kill many people, and can enthrall people and command them.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 548
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and a member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Ju Hwaran.md

# Ju Hwaran (주화란)

- **Safe through:** Chapter 544
- **Aliases:** Hwaran
- **Role:** Level 88 Young Bureau Head and leader of the Yongbong Escort Bureau, responsible for its personnel and contracts after Heo Jun’s betrayal, and now a member of the Fire Dragon Pavilion.
- **Personality:** Intelligent, capable, responsible, filial, composed under pressure, and burdened by intense guilt over the escort journey's deaths.
- **Voice:** Clear, polite, restrained, and determined.
- **Relationships:** Escort King Ju Gongsan was her paternal grandfather and rescued the Guangdong Chen Family’s surviving child, who became Song Ilseom’s grandmother; Ju Hogun is her father, Heo Jun was her uncle, Sama Pyo was her former fiancé in a political engagement she accepted for her father's sake, Song Ilseom is her direct escort, and Jin Taekyung is a trusted ally.

### Sama Pyo.md

# Sama Pyo (사마표)

- **Safe through:** Chapter 544
- **Aliases:** Black Dragon Saber
- **Role:** Young Sect Leader of the Black Dragon Demon Gate, a Morning Star reputed to be no less than the Ten Dragons and Phoenixes, and a member of the Fire Dragon Pavilion.
- **Personality:** Outwardly courteous and smiling, inwardly calculating, but genuinely protective of Taishan and willing to redirect blame onto his subordinate.
- **Voice:** Polite and ingratiating in public, with sardonic humor and controlled evasiveness.
- **Relationships:** Sama Pyo commands the absolutely loyal Taishan, is Sima Gong's son, was Ju Hwaran's former fiancé in a political engagement, and has joined the Fire Dragon Pavilion while openly intending to use Jin Taekyung as a useful card.

### Song Il.md

# Song Il (송일)

- **Safe through:** Chapter 544
- **Aliases:** Roaring Fury Swordsman
- **Role:** Elder of the Zhongnan Sect and the Roaring Fury Swordsman; senior brother of Sect Leader Gong Iljung; came to the Jin Family of Taiyuan to demand redress for Gong Ilhyuk's injury and the alleged insult to Zhongnan; attacked Jin Taekyung with the Heavenly River Thirty-Six Swords, was stopped by Jeok Cheongang, and was publicly humiliated by him.
- **Personality:** Arrogant, domineering, punitive, and confident in his martial power and seniority.
- **Voice:** Gruff, cutting, condescending, and threatening, with formal authority used to pressure those beneath him.
- **Relationships:** Gong Iljung is his junior Sect Leader and martial younger brother; Gong Ilhyuk is a junior Disciple of his sect; he recognizes Baek Museong and Cheongpung through their Huashan and Sword Saint connections.

### Song Ilseom.md

# Song Ilseom (송일섬)

- **Safe through:** Chapter 544
- **Aliases:** Escort Captain Song
- **Role:** Level 110 young escort captain of the Yongbong Escort Bureau, one of its Dragon-Phoenix Three Escorts, and a newly accepted member of Jin Taekyung and Cheongpung’s Fire Dragon Pavilion.
- **Personality:** Blunt, decisive, survival-hardened, and dryly self-aware, with little patience for insults or disorder.
- **Voice:** Forceful and urgent in command, with a rough and confrontational edge.
- **Relationships:** He serves under Ju Hwaran, is Song Pyosan’s son, and his grandmother was the surviving Guangdong Chen child rescued by Ju Gongsan during the Great Faction War.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 544
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord.

## Korean source

```text
＃549화



나는 수천 명의 군단을 이끄는 장군이 아니다.

화룡각의 구성원은 나를 포함한다 해도 고작 여섯 명.

모두가 한자리에 모이는 데에는 한 식경이면 충분했다.

“모두 주목.”

인사도, 존칭도 생략한 채 불쑥 꺼낸 한마디에 심상치 않은 기류를 느낀 다섯 사람의 시선이 집중된다.

아직 이들을 부르러 갔던 혁무진조차 전후 사정을 제대로 알지 못하는 상황.

의문이 서린 얼굴들을 차례대로 응시한 나는 천천히 입술을 뗐다.

“바로 본론부터 들어가자면…… 한 가지 임무를 받았다.”

뺄 것도, 더할 것도 없었다.

나는 있는 그대로를 설명해 주었고, 간단한 브리핑은 일각도 채 흐르기 전에 끝났다.

그리고 모두가 약속이라도 한 것처럼 입을 다문 채 생각에 잠겨 있던 그때, 한 사람이 불쑥 입을 열었다.

“그러니까.”

침착한 목소리의 주인은 익히 아는 얼굴이었다.

흑룡마문(黑龍魔門)의 소문주, 사마표가 나를 응시하며 말을 이었다.

“남만으로 향한다. 이거로군.”

나는 고개를 끄덕였다. 가벼운 정정과 함께.

“정확히는 남만이 아니라, 남만야수궁(南蠻野獸宮)이지.”

남만야수궁. 영물과 독물을 비롯하여 수많은 동물들을 길들이고, 그것들의 움직임을 본 따 무공을 수련한다는 신비의 문파.

동물 보호 협회인지 학대 집단인지는 잘 모르겠지만, 적어도 한 가지는 확실하다.

‘홍란. 아니, 남천마후(南天魔后)가 군침을 흘릴 만한 장소라는 거.’

두 번째 ‘균열’이 일어난다는 가정하에, 암천 입장에서는 남만야수궁만큼 적격인 곳을 찾기도 힘들다.

그야말로 동물의 왕국이요, 천하에서 가장 많은 영물과 독물들이 득실거리는 곳이니까.

유엽도(柳葉刀) 한 자루를 품에 안고 이야기를 듣던 송일섬이 중얼거렸다.

“고생길이 훤하군.”

녀석이 이런 말을 하는 데에는 충분한 이유가 있었다.

남만야수궁이 자리 잡은 남만은 중원에서 운남(雲南)이라고도 불리는 곳.

위치상으로는 사천의 바로 아래에 붙어 있으며 귀주, 광서와 땅을 맞대고 있다.

이렇게 들으면 단지 거리가 멀 뿐, 아무런 문제도 없어 보이지만…….

‘문제는, 남만 자체의 지리와 기후가 엄청나게 지랄 맞다는 거지.’

남만에는 푹푹 찌는 열대 기후에 밀림이 끝도 없이 늘어져 있다고 했다.

잘 정비된 가도(街道)는 눈을 씻고 찾아봐도 없고 대신 잘 큰 맹수나 독충이 인간을 밥차 취급하는, 실로 거지 같은 동네라 할 수 있었다.

‘얼추 들은 것만 해도 이 정도인데…….’

실제로는 어느 정도일지 쉽게 짐작이 가지 않는다.

천하를 그려 넣은 지도에도 어엿하게 들어간 남만이 왜 새외(塞外) 취급받는지 어렴풋이 알 것 같기도 했다.

‘사실 현대적 관점에서 보면 외국이 맞긴 하지.’

운남이 현대에서는 베트남과 미얀마던가. 그쯤 어딘가에 있을 텐데 세계지리 시간에 잠만 처자느라 기억이 가물가물하다.

기억을 되짚고 있던 그때 혁무진이 손을 번쩍 치켜들었다.

“저기, 조장님. 질문이 있는데요.”

“말해.”

“진짜 갑니까?”

“그럼 가짜로 가냐?”

“그, 너무 위험할 것 같은데요.”

“뭐 어때. 지금까지도 항상 위험했는데.”

“……당연하게 말씀하시니까 할 말이 없네요.”

“할 말 없으면 입 다물고 짐이나 싸.”

“언제 출발하는데요?”

“아, 내가 말 안 했나?”

중요한 걸 깜빡했군.

다른 사람들도 목적지와 그 이유에 대해 집중하느라 미처 생각하지 못한 것이 분명했다.

한 사람, 한 사람을 차례차례 바라본 나는 한 마디를 툭 내뱉었다.

“오늘 당장.”

“……!”

“……!”

작은 파문이 순식간에 번져 나간다. 그중에서도 특히 혁무진과, 호거아(虎巨兒) 태산이 그랬다.

“농담이시죠?”

“지금 같은 상황에 농담할 것 같냐?”

“말도 안 돼. 당장 챙겨야 할 옷이나 물자는요?”

“말 돼. 우리가 언제부터 의식주 철저하게 따졌다고. 그냥 벽곡단이나 챙겨.”

후욱, 훅!

깜짝이야. 열양지기인가.

놀라울 만큼 뜨거운 콧김을 뿜어낸 태산이 자리에서 벌떡 일어나며 외쳤다.

“안 된다! 태산이! 오늘 저녁! 고기 먹기로 했다!”

“고기? 고기 좋지.”

나는 혁무진을 향해 한 마디를 덧붙였다.

“들었지? 육포도 챙겨라.”

“육포! 맛없다!”

“……그냥 닥치고 아무거나 처먹어.”

젓가락도 뜯어 먹게 생긴 놈이 입맛 까다로운 것 보소.

내 시선에 담긴 뜻을 알아차린 사마표가 어깨를 으쓱하며 입을 열었다.

“태산. 네 이 녀석.”

“주, 주군.”

“언제까지 그리 천방지축으로 굴 테냐. 만약 계속 생떼를 쓴다면…….”

“태산이. 안 그러겠다. 용서해 줘라. 주군.”

저 덩치 큰 놈이 얼마나 기가 죽었는지, 나도 모르게 미안한 마음이 들 정도다.

앞으로 태산에 관한 일은 사마표에게 맡겨야겠다고 생각한 나는 미간을 찌푸리고 있는 송일섬에게 시선을 돌렸다.

“왜. 너도 불만 있냐?”

“물론. 다른 곳도 아니고 남만이니까.”

작게 혀를 찬 송일섬이 말을 이었다.

“하지만 없는 것으로 치지. 애석하게도 이미 선금을 두둑이 받아 버렸거든. 열 배나 되는 위약금을 지불할 자신도 없고.”

“생각했던 것보다 훨씬 깔끔한데. 마음에 들어.”

“한 번 맺은 계약은 지킨다. 그러지 않았다면 추혼객(追魂客)이라는 이름도 없었어.”

강한 신념과 자부심이 느껴지는 한 마디를 툭 내뱉은 송일섬이 덤덤하게 말을 이었다.

“물론 최종 결정은 내가 아니라 고용주가 하는 거고. 그렇지 않소?”

당연하게도 마지막 물음은 내게 던진 것이 아니다.

처음부터 지금까지, 줄곧 아무 말 없이 어떤 생각에 잠겨 있던 한 사람, 은비화(隱匕花) 주화란이 마침내 입을 열었다.

“제가 어떤 대답을 할지. 이미 알고 있을 것 같은데요. 아닌가요?”

귓가를 파고드는 나긋하면서도 맑은 목소리에, 나는 피식 웃었고 송일섬은 작게 한숨을 내쉬었다.

“내 이럴 줄 알았지. 제기랄, 남만이라니.”

“계약 내용을 다시 상기시켜 드릴 필요는 없을 거라 믿어요. 송 대협.”

앓는 소리를 흘리는 송일섬을 뒤로한 주화란이 나를 물끄러미 응시했다.

신비한 빛을 띤 검푸른 눈동자에 내 얼굴이 비친다. 이렇게 가까이서 보니까 꼭…….

“진 대협?”

“아, 네.”

방금 뭐였지. 잠깐 졸았나.

주화란의 부름에 정신을 차린 나는 내심 중얼거렸다.

‘안 되지. 안 돼.’

벌써부터 이러면 곤란하다. 앞으로의 일을 생각하면 언제나 냉정한 상태에서 상황에 임해야 했다.

몇 번이고 뇌까리며 마음을 다잡은 나는 최대한 침착한 목소리로 입을 열었다.

“잘됐네요. 안 그래도 물어볼 것이 있었습니다. 다름이 아니라…….”

말을 이으려던 그때였다.

“남만으로 향하는 가장 빠른 길과 필요한 것에 대해서겠죠? 좋아요.”

“예?”

“왜요? 제 생각이 틀렸나요?”

“아뇨. 그게 아니라.”

오히려 그 반대다. 너무 정확해서 깜짝 놀랐다.

뭐야, 이거. 설마 독심술이라도 익힌 건가? 관심법. 뭐 그런 거야?

말문이 막힌 채 눈을 깜빡이는 나를 향해, 주화란이 싱긋 웃어 보였다.

“놀라실 것 없어요. 아까부터 제가 할 수 있는 일을 생각하고 있었으니까.”

“아.”

“저도 정식으로 화룡각의 일원이 되었으니, 지난번에 말씀드렸던 것처럼 한 사람 몫을 해내야겠죠.”

톡. 톡톡.

그녀 역시 한 사람의 검수(劍手)라는 것을 알려 주듯, 새하얗지만 거친 손가락이 일정한 속도로 탁자 위를 두드린다.

그리고 이어 흘러나오는 목소리.

“우선 진 대협께서도 말씀하셨듯이, 물자는 최소한으로 하는 것이 좋겠네요. 의복은 필요 없고, 식량도 건량으로 이틀 치면 충분해요.”

“건량이라니! 그것만은 제발! 태산이 죽는다!”

태산의 통곡에 주화란이 재빨리 덧붙였다.

“물론 육포도요.”

“저 새끼 보호자 뭐 하냐. 아, 주 소저는 계속 말씀하세요.”

“네. 그럼…….”

골칫덩이를 치워 버린 주화란은 막힘 없이 말을 이어 갔다.

필요한 물품부터 남만으로 향하는 가장 빠른 길까지.

다행히도 그녀는 수년 전 남만에 표행을 갔던 경험이 있었고, 조부인 표왕이 남긴 기록을 통해 곳곳의 지형과 숨겨진 길 역시 알고 있었다.

코흘리개 시절부터 천하를 방랑하는 낭인의 삶을 살았던 송일섬조차 놀라움을 표할 정도였다.

“그런 길이 있었단 말이오?”

주화란이 자신 있게 고개를 끄덕였다.

“물론이에요. 할아버님의 기록에 따르면 확실해요.”

“나 역시 그곳에 일 년 정도 머물렀던 적이 있소. 하지만 내가 알기로는…….”

“할아버님의 기록에 따르면 확실해요.”

“아니, 그건 아는데. 내 말은.”

“할아버님. 기록.”

“이보시오. 내 말도 좀.”

“표왕.”

“……믿겠소. 믿을 테니까 계속하시오.”

표왕이 누구인가. 자그마치 십만의 마교도가 천하를 뒤덮은 와중에도 그 전설적인 만리행을 성공시킨 레전드 중의 레전드.

바로 그 P왕의 의지를 이은 주 P. 화란은 물 만난 고잉메리호처럼 막힘 없이 나아갔고, 불과 한 식경이 지나기도 전에 남만으로 향하는 모든 경로 계획을 수립하는 기염을 토했다.

“후, 우선은 여기까지네요. 질문 있으신 분?”

후웅!

트롤의 것으로 의심될 만큼 굵은 팔이 번쩍 솟구쳤다.

“네, 뭐든 물어보세요.”

호거라 태산이 딱딱하게 굳은 얼굴로 입을 열었다.

“태산이. 육포 이후로 아무것도 이해 못 했다.”

“…….”

“…….”

어떤 새끼가 노키즈존에 애를 데려왔냐.

나는 날카로운 눈빛으로 한 사람을 쏘아보았다.

“야, 보호자.”

“미안하군.”

텁.

“읍. 읍!”

내 일갈에 즉각 태산의 입을 틀어막은 사마표가 주화란을 향해 고개를 까딱였다.

“미안하오.”

“……괜찮아요.”

말투는 덤덤하지만, 가라앉은 목소리만큼은 숨길 수 없다. 상황이 상황인 만큼 어쩔 수 없는 일일 것이다.

아니, 당연한 일이지.

‘아무리 정략혼이라고 해도 명색이 약혼까지 했던 사이니까.’

얼음 계열 마법만큼이나 쿨하다는 할리우드 코쟁이 놈들이라면 모를까. 내가 살던 현대의 대한민국이나 무림은 유교 걸과 유교 보이들이 수두룩하다.

보는 나까지 어색한데 주화란은 오죽할까.

‘나는 둘 사이에 무슨 일이 있었는지도 자세히 모르고.’

문득 그리 생각하니 기분이 묘해진다.

왠지 모르게 피부에 닿는 옷감의 질감이 거슬리고, 보이지 않는 누군가가 작고 얇은 바늘로 쿡쿡 찌르는 느낌이다.

“조장님?”

“음?”

짧은 상념을 깨트린 것은 혁무진의 부름이었다.

굳이 고개를 돌려 확인할 필요도 없이, 나를 빤히 바라보는 시선들이 느껴진다.

흐트러진 마음을 바로잡은 나는 애써 담담하게 입을 열었다.

“자, 그럼 우선 지금까지 나온 이야기대로 움직인다. 물품은 최소한으로. 주어진 시간은…….”

내 시선을 받은 주화란이 대답했다.

“반 시진. 넉넉잡고 반 시진이면 충분해요. 눈에 띄지 않게 필요한 말과 마차를 수배해야 하니.”

“어디에서 집결하는 게 좋겠습니까?”

“음. 진 대협께서는 어떻게 생각하세요?”

이건 공개된 임무가 아니다. 최대한 빠르면서도, 동시에 은밀하게 움직여야 한다.

그리고 수많은 인파로 들끓는 인근을 조용히 빠져나가기 위해서는 일단 흩어진 뒤 2차 집결지를 결정해야 했다.

“대별산(大別山). 그곳에서 다시 만나죠.”

“좋은 생각이에요.”

고심 끝에 나온 대답에, 주화란을 비롯한 이들이 고개를 끄덕였다.
```

## Final English reading copy

```markdown
# Chapter 549

I was not a general leading an army of thousands.

Even counting me, the Fire Dragon Pavilion had only six members.

It took no more than half an hour for everyone to gather in one place.

“Everyone, pay attention.”

The five people immediately focused their gazes on me, sensing something unusual in the words I had abruptly spoken without so much as a greeting or honorific.

Even Hyuk Mujin, who had gone to summon them, still had no idea what was going on.

I looked over their questioning faces one by one before slowly parting my lips.

“To get straight to the point… I’ve been given a mission.”

There was nothing to leave out or add.

I explained everything exactly as it was, and the short briefing ended in less than fifteen minutes.

Then, just as everyone had fallen silent and begun thinking as though they had made some kind of agreement, one person suddenly spoke.

“So.”

The owner of that calm voice was a familiar face.

Sama Pyo, Young Sect Leader of the Black Dragon Demon Gate, continued while looking at me.

“We’re heading to Nanman.”

I nodded, adding a small correction.

“More precisely, not Nanman itself. The Nanman Beast Palace.”

The Nanman Beast Palace was a mysterious sect that tamed countless animals—including spiritual creatures and venomous beasts—and trained in martial arts modeled after their movements.

I was not sure whether it was an animal protection association or an animal-abuse group, but one thing was certain.

*Honglan. No—the Southern Heaven Demon Empress must be salivating over a place like that.*

Assuming a second “rift” was about to occur, Dark Heaven would have a hard time finding a more suitable location than the Nanman Beast Palace.

It was truly an animal kingdom, a place teeming with more spiritual creatures and venomous beasts than anywhere else under heaven.

Song Ilseom, who had been listening while holding a willow-leaf saber against his chest, muttered,

“Sounds like a miserable journey.”

There was a good reason he had said that.

Nanman, where the Nanman Beast Palace was located, was also called Yunnan in the Central Plains.

It lay directly south of Sichuan and shared borders with Guizhou and Guangxi.

Hearing that, it might have sounded like nothing more than a distant place with no particular problems. But…

*The problem is that Nanman’s geography and climate are unbelievably fucked.*

They said Nanman had a sweltering tropical climate and endless jungles.

There were no well-maintained roads to be found, even if one scrubbed one’s eyes raw. Instead, it was a truly miserable region where fully grown predators and venomous insects treated humans like food delivery.

*That’s only what I’ve heard so far…*

It was difficult to imagine what the place was actually like.

I could vaguely understand why Nanman, despite being properly included on maps of the realm, was still treated as part of the Outer Lands.

*Though from a modern perspective, it really would be a foreign country.*

In the modern world, was Yunnan Vietnam or Myanmar? It had to be somewhere around there, but my memory was hazy because I’d spent world geography class sleeping my ass off.

As I was dredging up those memories, Hyuk Mujin suddenly raised his hand.

“Captain, I have a question.”

“Go ahead.”

“Are we really going?”

“Would we be going fake?”

“I-I think it sounds too dangerous.”

“What does it matter? Everything has been dangerous so far.”

“……You say that so naturally that I have nothing to say.”

“If you have nothing to say, shut your mouth and pack your things.”

“When are we leaving?”

“Ah, did I not mention that?”

I had forgotten something important.

The others had clearly been too focused on the destination and the reason for going to think of it.

I looked at them one by one and tossed out a single sentence.

“Today. Right now.”

“……!”

“……!”

A small ripple spread through the group in an instant. Hyuk Mujin and Taishan, the Tiger Giant Child, were especially affected.

“You’re joking, right?”

“Do I look like I’d joke at a time like this?”

“That makes no sense. What about our clothes and supplies? We need to pack right away.”

“It makes perfect sense. Since when have we ever worried carefully about food, clothing, and shelter? Just bring some fasting pills.”

“Whoosh. Whoosh!”

What the hell? Was that Scorching Yang Qi?

Taishan sprang to his feet, blasting astonishingly hot breath from his nose.

“No! Taishan! Was supposed to eat meat tonight!”

“Meat? Meat sounds good.”

I added one more sentence toward Hyuk Mujin.

“You heard him. Pack some jerky too.”

“Jerky! Tastes bad!”

“……Just shut up and eat whatever the hell you get.”

Look at this guy, who looked like he would eat chopsticks, acting picky about food.

Sama Pyo noticed the meaning in my gaze and shrugged before speaking.

“Taishan. You little rascal.”

“L-Lord.”

“How long are you going to keep behaving so recklessly? If you continue throwing this sort of tantrum, then…”

“Taishan. Won’t do it. Forgive Taishan, Lord.”

The enormous man looked so dejected that I actually felt sorry for him.

*I’ll leave everything involving Taishan to Sama Pyo from now on.*

With that thought, I turned toward Song Ilseom, who was frowning.

“What? Are you dissatisfied too?”

“Of course. It’s Nanman, not somewhere else.”

Song Ilseom clicked his tongue quietly and continued.

“But I’ll overlook it. Unfortunately, I’ve already received a hefty advance payment. And I’m not confident I could afford the tenfold penalty.”

“You’re much more straightforward than I expected. I like it.”

“Once I make a contract, I keep it. If I didn’t, I wouldn’t be known as the Soul-Chasing Guest.”

Song Ilseom tossed out the words with unmistakable conviction and pride, then continued in an even tone.

“Of course, the final decision belongs to the employer, not me. Isn’t that right?”

Naturally, his final question was not directed at me.

Ju Hwaran, the Dagger Hidden Flower, had been sitting in silence and lost in thought from beginning to end. At last, she opened her mouth.

“I think you already know what answer I’m going to give. Don’t you?”

Her clear, gentle voice pierced my ears. I let out a quiet laugh, while Song Ilseom sighed softly.

“I knew this would happen. Damn it. Nanman.”

“I trust I don’t need to remind you of the terms of the contract, Great Hero Song.”

Song Ilseom continued groaning behind her as Ju Hwaran stared at me.

My face was reflected in her dark blue eyes, which held a mysterious light. Seeing them from this close, they looked almost…

“Great Hero Jin?”

“Ah, yes.”

*What was I just thinking? Did I doze off for a moment?*

Ju Hwaran’s call brought me back to my senses.

*No. Don’t.*

This was already a problem. Considering what lay ahead, I needed to face every situation with a clear head.

After repeating that to myself several times and pulling myself together, I spoke as calmly as possible.

“That’s good. I had something to ask you anyway. Namely…”

“About the fastest route to Nanman and what we’ll need? All right.”

“Pardon?”

“Why? Was I wrong?”

“No. That’s not it.”

*It was the exact opposite. She was so accurate that she startled me.*

*What the hell? Has she learned mind reading? Some kind of mind-reading technique?*

As I blinked speechlessly, Ju Hwaran gave me a bright smile.

“There’s no need to be surprised. I’ve been thinking about what I could do since earlier.”

“Oh.”

“I’m now officially a member of the Fire Dragon Pavilion, so I should do my part, as I said I would.”

Tap. Tap-tap.

Her rough, snow-white fingers struck the tabletop at a steady rhythm, as though reminding us that she too was a swordswoman.

Then her voice continued.

“First, as Great Hero Jin said, it would be best to keep our supplies to a minimum. We won’t need extra clothing, and two days’ worth of food in the form of dry rations should be enough.”

“Dry rations? Please, anything but that! Taishan will die!”

At Taishan’s wail, Ju Hwaran quickly added,

“Of course, we’ll bring jerky too.”

“What the hell is his guardian doing? Ah, Young Lady Ju, please continue.”

“Of course. Then…”

After removing the troublesome one from the discussion, Ju Hwaran continued without hesitation.

She went over everything, from the supplies we would need to the fastest route to Nanman.

Fortunately, she had traveled to Nanman on an escort assignment several years earlier. Through the records left behind by her grandfather, the Escort King, she also knew the terrain and hidden roads in various places.

Even Song Ilseom, who had lived as a wandering martial artist and traveled throughout the realm since he had been a snot-nosed child, expressed his surprise.

“There was a road like that?”

Ju Hwaran nodded confidently.

“Of course. According to my grandfather’s records, it’s definitely there.”

“I also stayed there for about a year. But as far as I know…”

“According to my grandfather’s records, it’s definitely there.”

“No, I know that. What I mean is—”

“My grandfather’s records.”

“Excuse me. Could you let me finish?”

“The Escort King.”

“……I believe you. I believe you, so please continue.”

Who was the Escort King?

He was the legend among legends who had successfully completed that legendary Ten-Thousand-Li Journey even while a hundred thousand Demonic Cultists covered the realm.

The will of that very P-King lived on in Ju P. Hwaran.

Like the Going Merry hitting open water, she sailed ahead without a hitch, and before even half an hour had passed, she had completed the entire route plan for traveling to Nanman.

“Whew. I think that covers everything for now. Does anyone have any questions?”

Whoosh!

A thick arm, large enough to belong to a Troll, shot into the air.

“Yes, please ask anything.”

Tiger Giant Child Taishan opened his mouth with a stiff expression.

“Taishan. Understood nothing after jerky.”

“……”

“……”

*Which bastard brought a kid into a no-kids zone?*

I glared sharply at one person.

“Hey, guardian.”

“My apologies.”

Smack.

“Mm. Mm!”

Sama Pyo immediately clamped a hand over Taishan’s mouth after my sharp rebuke, then gave Ju Hwaran a small nod.

“My apologies.”

“……It’s all right.”

Her tone was calm, but she could not hide the lowered voice that accompanied it. Given the circumstances, it could not be helped.

No, it was only natural.

*Even if it was a political marriage, they had been formally engaged.*

Those big-nosed Hollywood bastards, supposedly as cool as ice magic, might be different. Modern Korea, where I had lived, and Murim were both full of Confucian girls and Confucian boys.

It was awkward even for me to watch. How much worse must it have been for Ju Hwaran?

*I don’t even know exactly what happened between them.*

The thought left me feeling strange.

For some reason, the texture of the fabric against my skin began to irritate me. It felt as though someone invisible were poking me again and again with a small, thin needle.

“Captain?”

“Hm?”

Hyuk Mujin’s voice broke through my brief reverie.

I did not even need to turn my head to confirm it. I could feel the gazes fixed on me.

I steadied my scattered thoughts and spoke as casually as I could.

“All right. We’ll move according to what we’ve discussed. Minimal supplies. The time we have is…”

Ju Hwaran answered when she saw my gaze.

“Half a shichen.[^1] Half a shichen at most should be enough. We’ll need to quietly arrange the necessary horses and carriages without attracting attention.”

“Where should we gather?”

“Hmm. What do you think, Great Hero Jin?”

This was not a public mission. We had to move as quickly as possible while remaining discreet.

And to quietly leave the area, which was teeming with countless people, we first needed to split up and choose a secondary meeting point.

“Mount Daebyeol. We’ll meet there.”

“That sounds good.”

Ju Hwaran and the others nodded at the answer I had settled on after careful thought.

[^1]: A shichen is a traditional time unit lasting approximately two hours.
```

<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0462.txt",
      "sha256": "4af8c1d197c612765cbd38bb3e6fa13fa3b453d37eefd4f633fa214b4bb83328",
      "bytes": 13178
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "52d7ff918f65e18a02924dcbf28c886ae57af2dc70b06717ef612db579a9c12d",
      "bytes": 4311
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "1229436a5b294b22f9fc51683bc6b6862493768d94e00291fc7c0ed2112d164e",
      "bytes": 150777
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "648aee1792ed6c37abd64f519e50ad62824b34df80228429a12360a33dc8e830",
      "bytes": 990
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "0a9181ed8002650af702cbf9302135b15a5b4e21dd650f6de5e3a198e9f91485",
      "bytes": 553
    },
    {
      "path": "characters/Dongting Fisherman.md",
      "sha256": "231d87cce293e574d57b66fafa4233adcf6194429cc7f116668bfc0176eb48ae",
      "bytes": 703
    },
    {
      "path": "characters/Gung Gibang.md",
      "sha256": "926eaf1f40d5f8dc907d83dc12ac3ea56e1ec12da8e34e0dbbc6acba3c0f822a",
      "bytes": 662
    },
    {
      "path": "characters/Honglan.md",
      "sha256": "702f65317f7d04783be6ab0ff4cd2f90ea8acc72ebec6fff942a8e4f2213c5e3",
      "bytes": 799
    },
    {
      "path": "characters/Hwang Chung.md",
      "sha256": "7d542e3e96d53b061346b24c0068abc7bd9125299ea1a4b8b25b0589de858715",
      "bytes": 663
    },
    {
      "path": "characters/Hyeongong.md",
      "sha256": "03e6f9a0948e1cb7dad8c2961a5991643f101831ee54ad6f1cc7951d6981aaaf",
      "bytes": 735
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "359d93713a8f9f4b5a5e98c070378e9821a843627c4cb8171d5cf1710bc44e55",
      "bytes": 1108
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "00a343ccbf43f6b6d0783a435bc51ffba22c0f0db3f314af6dc20b44d5984454",
      "bytes": 1574
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "262e89bb0ddcc8270afa091a2b7ff7a35fd3d30a9c64ba3f6cba03684d881b7f",
      "bytes": 622
    },
    {
      "path": "characters/Mungyeong.md",
      "sha256": "dbbdb0683cd54eab306a395c318abb37d463c10baad72e864e20fad58519730d",
      "bytes": 686
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "bfc261d7e738ba259411eb5cbdac861edc63b49dcd2204edfd24405d062d81f6",
      "bytes": 145368
    }
  ],
  "estimated_tokens": 12985
}
-->

# Durable State Update — Chapter 462

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 462. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 462. Profile updates may replace only one
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
  "chapter": 462,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 462,
    "continuity_sources": [462],
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
    "Honglan survived the Dongting Lake disaster and regained consciousness; Ju Wongong also survived but remains unconscious under guard after passing the most dangerous stage of his injuries. Honglan is still recovering and is unfit for combat.",
    "Jin Wikyung is acting as an inspector for the new Murim Alliance and is cooperating with Taekyung's investigation.",
    "The shared symbols between the Arch Lich's magic circle and Dark Heaven's formations remain unexplained.",
    "The Sea Serpent Society and three Yangtze River Channel League strongholds, including Donghu Stronghold, were destroyed, with more than a thousand casualties, while the perpetrators' wider plans remain unknown.",
    "The Dongting Fisherman is a previous-generation Supreme Peak water-arts master comparable to the Seafaring King, remains in Hubei Province, and is suspected of Dark Heaven involvement and the Dongting Lake attack. The Hidden Shadow Ghost is the local name for an unseen killer of boatmen who may be connected to him.",
    "Taekyung, Cheongpung, Hyuk Mujin, Gung Gibang, and Honglan are pursuing the Dongting Fisherman's refuge; the group has now reached the closest of five possible sites and Taekyung is searching underwater with the Water Rescue Worker Title's effects.",
    "Wudang is responding to an unidentified killer demon responsible for more than thirty deaths, including twenty pilgrims on Mount Wudang.",
    "The Skeleton King's undead identity remains concealed, and Taekyung has ordered him to join Peace Guild under a prepared contract.",
    "Go Jun is expected to succeed Lee Jungryong as Ares Guild's captain and is searching China for Lee's holographic recorder.",
    "The captured Three Fiends is a former-generation great fiend and Supreme Peak Dark Heaven subordinate whom Taekyung is transporting alive to investigate possible codes or markings.",
    "Qingxia Hall is an influential Hubei social club formed by powerful families' children, and Ju Wongong is its exiled young master who defers to Prince Shangshan while Honglan conceals her real name; Beggars' Sect, Lower District Sect, and Zhuge Clan intelligence are searching for the people responsible for the Hubei massacres."
  ],
  "continuity_sources": [
    461,
    460
  ],
  "open_questions": [
    "What are the origin and purpose of the symbols shared by the Arch Lich's magic circle and Dark Heaven's formations?",
    "Who destroyed Donghu Stronghold and the related Yangtze River Channel League strongholds, why was no Moving Formation trace left, and was the destruction a diversion?",
    "What is the Dongting Fisherman's exact role in Dark Heaven and the Hubei atrocities, is he the Hidden Shadow Ghost, and which of the five suspected sites contains his refuge?",
    "Is the killer demon attacking Wudang connected to Dark Heaven?",
    "What evidence is contained in Lee Jungryong's holographic recorder, and what are the terms of the Peace Guild–Wizard Guild agreement?"
  ],
  "safe_through": 461,
  "temporary_decisions": [
    "Render 익양루 as Yiyang Tower.",
    "Render 황철 as Hwang Cheol, 도립군 as Do Ripgun, 광수도귀 as Mad Water Saber Demon, 파랑호 as Wave Fox, 동정호 as Dongting Lake, and 사천혈사 as Sichuan Blood Tragedy.",
    "Render 살귀 as killer demon, 은영귀 as Hidden Shadow Ghost, 일급 낭인 as First Rate wandering martial artist, 삼괴 as Three Fiends, 대마두 as great fiend, and 마군 as Demon Lord.",
    "Render 시부럴 as “sibu-leol,” 시벌좌 as “Lord Fuck,” and 시부럴좌 as “Lord Sibu-leol.”",
    "Preserve the Skeleton King's grandiose, mock-offended voice and Taekyung's dry, profane humor; render 주원공 as Ju Wongong, 대죽산표국 as Daejuksan Escort Bureau, 형문검가 as Hyungmun Sword Family, 응성상회 as Eungseong Merchant Association, 천룡인 as Celestial Dragon, 사인교 as four-person sedan chair, 홍란 as Honglan, 가기 as singing courtesan, 구족 as the nine branches of kin, 수상 구조대원 as Water Rescue Worker, and 수공 as water arts."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 혁무진    | **Hyuk Mujin**     |
| 청풍     | **Cheongpung**     |
| 하오문    | **Lower District Sect**          |
| 무당파    | **Wudang**                       |
| 암천     | **Dark Heaven**                  |
| 제갈세가   | **Zhuge Clan**                   |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 생사결    | **life-and-death duel**                          | Explicitly lethal                                     |
| 낭인     | **wandering martial artist**                     |                                                       |
| 제자     | **Disciple**                                 |
| 사천     | **Sichuan**            |
| 본가      | **our family / this family**                                    |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 소협      | **Young Hero**                                                  |
| 도사      | **Daoist**                                                      |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 동정어옹 | **Dongting Fisherman** | Publicly condemned the Yangtze River Channel League and disappeared three days before this chapter. |
| 궁기방 | **Gung Gibang** | Beggars' Sect Successor Beggar and finalist. |
| 홍란 | **Honglan** | Stage name of Ju Wongong's Lower District Sect singing courtesan; her real name is concealed. |
| 황충 | **Hwang Chung** | Lord of Donghu Stronghold, the Seafaring King's sworn brother, and the Yangtze One Saber. |
| 현공진인 | **Perfected Being Hyeongong** | Veteran Wudang Daoist master and the current Sect Leader's Junior Brother. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 문경 | **Mungyeong** | Young medical apprentice and newly introduced passenger. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 반박귀진 | **Returning to Simplicity** | Supreme Peak technique or phenomenon used by Jeok Cheongang. |
| 사천당문 | **Sichuan Tang Clan** | Martial clan cited for its poison-based cleansing method. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 천기 | **heavenly patterns** | Celestial patterns Hong Dao studies to perceive major changes and omens. |
| 반로환동 | **Returned to Youth** | Possible explanation for an apparently young Supreme Peak master. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 계도 | **precept blades** | Blades carried by the Hundred and Eight Arhats. |
| 당문 | **Tang Clan** | Short form for the Sichuan Tang Clan. |
| 호북 | **Hubei** | Province on Ju Gongsan's route from Guangdong to Henan. |
| 장강 | **Yangtze** | The river controlled by the Yangtze River Channel League. |
| 의생 | **medical apprentice** | Mungyeong's occupation. |
| 살수 | **assassin** | Professional killer considered as a possible suspect. |
| 악귀 | **Fiend** | Descriptive epithet applied to the First Fiend. |
| 유령환살보 | **Ghost Illusory Slaughter Step** | Movement technique used by the Slaughter Saint. |
| 이동진 | **Moving Formation** | Dark Heaven's inactive long-distance transportation formation. |
| 푸린 | **Furin** | Russian president mentioned in a forum headline. |
| 동정채 | **Donghu Stronghold** | Stronghold where Mu Song's Uncle Hwang is based. |
| 신기제갈 | **Divine Mechanism Zhuge** | Collective epithet for the Zhuge Clan's intellectual and strategic role. |
| 장강일도 | **Yangtze One Saber** | Hwang Chung's sobriquet. |
| 동정호 | **Dongting Lake** | Lake under which Dangyang and Honghu Strongholds operated. |
| 은영귀 | **Hidden Shadow Ghost** | Local name for an unseen killer targeting boatmen on Dongting Lake. |
| 나룻배 | **ferryboat** | Small ferry used to reach the suspected refuge site. |
| 사공 | **boatman** | Old boatman piloting the ferryboat. |
| 비처 | **secret refuge** | Hidden retreat of the Dongting Fisherman. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
| 청풍 | 진태경 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung repeatedly addresses Taekyung as 은인 after receiving food. |
| 청풍 | 혁무진 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung includes Mujin among his 은인들 after receiving the skewers. |
| 혁무진 | 청풍 | martial artist to young master | Young Master | formal-deferential | Mujin uses 공자께서는 when asking why Cheongpung descended from the mountain. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 진태경 | 청풍 | companion_to_young_martial_artist | Young Master Cheongpung | formal-polite | Taekyung uses 청 공자 while correcting Cheongpung's royal-etiquette mistake. |
| 궁기방 | 진태경 | rival_finalists | you bastard | insulting-casual | Gung Gibang answers Taekyung's collective insult with a profane threat. |
| 진태경 | 궁기방 | rival_finalists | you three idiots | insulting-casual | Taekyung addresses Gung Gibang as part of the trio and threatens them before a duel. |
| 진태경 | 문경 | young_martial_artist_to_medical_apprentice | Young Hero | formal-polite | Taekyung addresses the non-martial Mungyeong as 소협 while praising his actions. |
| 문경 | 진태경 | young_passenger_to_younger_martial_artist | Young Hero | deferential | Mungyeong uses 소협 while asking Taekyung for help boarding the ship. |
| 청풍 | 문경 | martial_companion_to_medical_apprentice | Medical Apprentice | cheerful-polite | Cheongpung addresses Mungyeong as 의생님 while asking him to greet the Tang Clan. |
| 혁무진 | 궁기방 | squad_companion_to_Beggars_Sect_successor | Young Hero Gung | formal-polite, then pointed | Uses 궁 소협 while asking about the culprit and challenging Gung’s insults. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 궁기방 | 혁무진 | squad_companions | you; that lunatic | insulting-casual | Gung Gibang mocks Hyuk Mujin's injuries and calls him a lunatic for attacking the Third Fiend. |
| 궁기방 | 청풍 | martial_companions | Young Hero Cheongpung | formal-polite | Gung Gibang uses 청 소협 while asking why Cheongpung is at the temporary clinic. |
| 중년인 | 진태경 | veteran civilian Hunter to celebrated allied Hunter | Mr. Jin | formal-polite and awed | The casualty clerk addresses Jin as 진 선생님 after Jin asks him to list Lei Fei among the dead. |
| 진태경 | 중년인 | celebrated Hunter to older fellow Hunter | sir | casual and teasing | Jin addresses the older Hunter as 아저씨 while joking with him and giving him instructions. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 홍란 | 진태경 | Lower District Sect courtesan to honored guest | honored guest | humble and formal | Introduces herself with 소녀 and addresses Taekyung as 귀인. |
| 궁기방 | 군관 | martial_artist_to_military_officer | Officer | insulting-casual | Gung Gibang uses 군관 나리 while mocking the officer's ignorance of Dark Heaven. |
| 군관 | 대협 | military_officer_to_martial_hero | Great Hero | formal-deferential | The officer addresses Taekyung as 대협 while asking whether he knows the culprit. |

## Listed compact profiles

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 461
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, the grandson and Disciple of Sword Saint Mae Jonghak, and a Supreme Peak martial master known as the Huashan Divine Dragon.
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, a deep love of martial arts, and a martial artist's competitive pride; he becomes unsettled when someone copies his martial arts
- **Voice:** Dreamy and hazy, with innocent, polite phrasing; he has begun imitating Taekyung's profanity.
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions while Taekyung is his only true martial rival; Tang Sadok has temporarily entrusted Mimi to him.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 461
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Dongting Fisherman.md

# Dongting Fisherman (동정어옹)

- **Safe through:** Chapter 461
- **Aliases:** None
- **Role:** The Dongting Fisherman is a previous-generation Supreme Peak master whose water arts rival the Seafaring King; he is identified as Dark Heaven's tail and suspected perpetrator of the Dongting Lake attack, with hidden refuges throughout the lake.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** The Dongting Fisherman opposed the Yangtze River Channel League and was monitored by the Lower District Sect for several years after friction with it, while current records place him in Hubei Province.

### Gung Gibang.md

# Gung Gibang (궁기방)

- **Safe through:** Chapter 461
- **Aliases:** Successor Beggar, Beggar Prince, pure-blooded beggar, ultimate beggar
- **Role:** Gung Gibang is the Beggars' Sect Successor Beggar and a unique eight-knot disciple.
- **Personality:** Vulgar, aggressive, and quick-tempered.
- **Voice:** Blunt, profane, and vividly threatening.
- **Relationships:** Gung Gibang is a rival finalist alongside Baek Woo and Zhuge Gyun who trades insults with Taekyung and uses Beggars’ Sect intelligence to investigate Tang Taesang’s murder and search for Dark Heaven’s Hubei forces.

### Honglan.md

# Honglan (홍란)

- **Safe through:** Chapter 461
- **Aliases:** None
- **Role:** Honglan is a Lower District Sect courtesan who uses a stage name while serving as Ju Wongong's singing courtesan.
- **Personality:** Discreet about her real identity and professionally alluring.
- **Voice:** Clear, pure, and alluring, with humble formal speech toward honored guests.
- **Relationships:** Honglan is kept at Ju Wongong's side as a singing courtesan, belongs to the Lower District Sect, lost her clan and parents overnight as a child, can respond to Taekyung through Sound Transmission, and is the sole surviving eyewitness to the Dongting Lake attack who knows several possible locations of the Dongting Fisherman's hidden refuges.

### Hwang Chung.md

# Hwang Chung (황충)

- **Safe through:** Chapter 451
- **Aliases:** Yangtze One Saber
- **Role:** Hwang Chung was the Lord of Donghu Stronghold, a moderate-faction elder of the Yangtze River Channel League, and the Seafaring King's sworn brother before he was killed in the stronghold's destruction.
- **Personality:** Calm, clever, and supportive of the orthodox faction during the Great Faction War.
- **Voice:** Not established.
- **Relationships:** Hwang Chung helped the Seafaring King establish the Yangtze River Channel League and is regarded by Mu Song as an uncle and trusted senior.

### Hyeongong.md

# Perfected Being Hyeongong (현공진인)

- **Safe through:** Chapter 450
- **Aliases:** None
- **Role:** Perfected Being Hyeongong is a veteran Wudang Daoist master of the previous generation, the current Sect Leader's Junior Brother, and a Supreme Peak swordsman who reached the ultimate stage of the Taiji Wisdom Sword.
- **Personality:** Hyeongong is humble and self-deprecating about his limited worldly knowledge while carrying the authority of an experienced senior master.
- **Voice:** Measured, respectful, and lightly self-deprecating.
- **Relationships:** Hyeongong is the current Wudang Sect Leader's Junior Brother and a respected senior to Zhuge Feng.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 461
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers and Vice Squad Leader of the Jin Dragon Squad.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 457
- **Aliases:** Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, a Supreme Peak master who has manifested Force, opened his Middle Dantian, crossed the wall into true mastery, can perceive the texture of qi well enough to sever layered magic, and is publicly recognized as an S-rank-level Hunter while formally retaining an A-rank license pending testing.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate, student, and trusted manager of media and official arrangements, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, and Xiao Shen regards him as an older brother after Jin saved him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 457
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Mungyeong.md

# Mungyeong (문경)

- **Safe through:** Chapter 452
- **Aliases:** None
- **Role:** Mungyeong is the legendary physician known as the former Divine Physician and Slaughter Saint, having passed the Divine Physician title to his Disciple.
- **Personality:** Compassionate, resolute, resourceful, and calm under extreme pressure.
- **Voice:** His Mungyeong persona is timid, deferential, and cheerful, while his Slaughter Saint voice is dry, impassive, and blunt.
- **Relationships:** Dong Feng is his Disciple, while Jeok Cheongang, Jin Taekyung, Cheongpung, and the two Sect Leaders know his Slaughter Saint identity.

## Korean source

```text
＃462화



늙은 사공은 자신에게 찾아온 현실이 믿어지지 않았다.

‘이게 다 뭔 일이랴.’

약관 무렵부터 지금까지 근 사십여 년의 세월 동안 사공 노릇을 했지만, 살다 살다 오늘처럼 해괴한 경험은 처음이었다.

파파파파팍!

깎아내릴 듯한 절벽 위를 빠르게 누비는 두 인영. 오늘 처음 보는 광경은 아니지만 볼 때마다 놀랍다.

멍하니 입을 벌린 채 위를 바라보던 사공이 생각했다.

‘저것이 성성이(猩猩. 원숭이)여, 사람이여.’

지금껏 사공으로 일하며 숱한 무림인들을 겪었지만, 저 정도로 놀라운 기예(技藝)를 직접 본 것은 처음이다.

그가 모는 나룻배를 이용하는 무림인들은 대부분 무공도 어중간하고 주머니 사정도 좋지 않은 낭인, 혹은 중소 문파의 제자였으니까.

‘다짜고짜 관군들이 들이닥쳐서 따라오라고 했을 때부터 짐작은 했다만…….’

똑똑히 봤다. 동정호를 책임지고 있는 곽 군관이 쩔쩔매며 존댓말을 사용하는 모습을.

평소 거만하기 짝이 없던 그의 태도를 생각해 봤을 때, 오늘 받은 손님들은 무림에서도 방귀깨나 뀌는 귀인들이 확실했다.

‘이거 잘하면 한몫 챙길 수도 있는 거 아녀?’

은퇴를 생각하고 있던 요즘이다. 근 한 달 사이 끊이지 않는 참극을 들을 때마다 마음 한구석이 불안하고 늙은 삭신이 유난히도 쑤셔 왔었다.

특히 전날 밤 동정호에서 수백 명이 떼거리로 죽임을 당했다는 소식에 반쯤 마음을 굳혔던 늙은 사공이었다.

‘동정호의 신령이 노하신 게지. 천기가 흉흉하니 은영귀 같은 악귀들이 날뛰는 게야.’

뱃사람은 온갖 미신의 신봉자들로 유명하고, 늙은이들은 전설처럼 내려오는 이야기들을 사실처럼 떠들어 대기 마련이다.

평생을 뱃사람으로 살아온 것으로도 모자라 늙기까지 한 그가 은퇴를 결심한 건 당연한 일이었다.

하지만 높으신 분들이 찾으신다는데 별수 있나. 죄인처럼 끌려가 나룻배를 띄웠을 때만 해도 죽음을 각오했었는데…….

파파파파팍!

저 모습을 보니 희망이 샘솟는다.

한목숨 건사하는 것은 물론이요, 한몫 단단히 챙겨서 은퇴할 수 있을 거라는 희망이.

‘대단한 무예를 지닌 것이 틀림없다!’

높은 경지의 무림인은 땅을 접어 달리고, 허공을 걷는다고 했다.

저들이 보여 주는 모습은 늙은 사공이 귀동냥으로 들었던 소문과 크게 다르지 않았다.

당장 우두머리로 보이는 새파란 청년도 물고기라도 되는 것 마냥 거친 강물을 누비고 있지 않나.

‘아니지. 벌써 이번이 네 번째 장소인 걸 생각하면 물고기 같은게 아니라 물고기지, 물고기.’

뭔 놈의 사람이 물갈퀴와 아가미라도 달렸는지, 한 번 물속으로 들어갔다 하면 기본이 한 시진이다.

그런 말도 안 되는 짓을 이미 세 번이나 반복했으니 과연 무림 고수라고 부를 만했다.

‘이 정도 고수들이라면 은영귀 같은 잡귀(雜鬼) 따위는 순식간에 해치울 터.’

살아나가기만 한다면야 한 재산 챙겨서 은퇴하는 건 일도 아니다.

늙은 사공이 희망에 부풀어 있던 그때, 절벽 위에서 외침이 들려왔다.

“청 소협! 거기 뭐 없소?”

“보면 말할게요!”

“뭔가 발견하면 바로바로 말해 주시오!”

“네, 꼭 그럴…… 앗!”

“헉! 뭐요! 무슨 일이오!”

순간 묵직한 긴장감이 주위에 내려앉았다.

늙은 사공과 함께 천천히 이동하는 배 위에서 주변을 살피던 혁무진도, 건너편 절벽에서 날카롭게 눈을 빛내던 궁기방도 숨을 삼켰다.

그리고 모두의 시선 속에서, 청풍이 외쳤다.

“와, 제비집이에요! 저 이렇게 큰 제비집 처음 봐요!”

“…….”

“…….”

“…….”

싸하게 얼어붙은 공기. 사공은 문득 생각했다.

‘……동정호의 신령이시여, 쇤네를 보호하소서.’

저 꼴을 보니 그나마 있던 믿음도 사라질 지경이다.

그렇게 늙은 사공이 아무도 모르게 신령을 향한 기도를 올리고 있던 그때였다.

촤아아아악! 타닥!

물보라와 함께 솟구친 그림자가 나룻배에 사뿐히 착지했다.

거구라고 부를 수 있을 법한 체구와 유연하면서도 강철처럼 단단해 보이는 근육. 그리고 묘하게 잘 어울리는, 헝클어진 머리를 고정한 아름다운 은비녀.

“오셨습니까.”

혁무진의 인사에 진태경이 말없이 고개를 끄덕였다. 미간을 찌푸린 그의 모습에, 늙은 사공이 조심스레 물었다.

“혹시 이번에도?”

사실 물어보나 마나 한 질문이었다. 뭔가를 찾아냈다면 저렇게 표정이 어두울 리 없을 테니까.

미간을 좁힌 채 생각에 잠겨 있던 진태경이 입을 열었다.

“이번이 네 번째. 맞죠?”

“예에. 그러고말굽쇼.”

늙은 사공은 대답하면서도 괜히 눈치가 보였다.

이 대단한 손님들은 이미 앞서 세 번, 그리고 지금까지 도합 네 번이나 허탕을 쳤다.

영 기분이 좋지 않은 무림 고수와 같은 배에 타고 있다는 건 그로서도 결코 유쾌한 일이 아니다.

그나마 한 가지 다행이자 불행인 것은, 마지막 장소가 남았다는 것이었다.

화륵, 솨아아아!

가볍게 공력을 일으켜 물기를 증발시킨 진태경이 물었다.

“마지막 남은 지점까지는 얼마나 걸릴 것 같습니까?”

“지금까지 왔던 방식으로 간다면 한 식경 정도면 충분합니다. 한데…….”

늙은 사공이 침을 꿀꺽 삼킨 뒤 말을 이었다.

“갈수록 바람과 물살이 거세지고 있습니다요. 도착할 때쯤이면 날이 저물기 시작할 테니, 차라리 다음을 노리는 것이 어떨는지요.”

“안 됩니다. 무조건 오늘이어야 해요.”

“하지만 아무래도…….”

“가야 합니다. 지금 당장.”

칼로 베듯 단호한 말투에 늙은 사공은 입을 다물었다.

어째서인지 오늘 날씨는 불길하리만치 좋지 않았다. 청명해야 했을 하늘은 먹구름으로 가득했고 거친 바람과 물살은 도무지 가라앉을 기미가 보이지 않았다.

‘영 느낌이 좋지 않은디.’

과거, 홍수나 폭풍우가 몰아칠 때만 느꼈던 불길함이 노련한 사공의 전신을 쿡쿡 찔렀다.

하지만 사공은 가슴 한구석에 스며드는 불길함을 애써 무시했다.

‘나이를 먹었더니 새가슴이 됐나. 그럴 리가 없지.’

난데없이 홍수나 폭풍우라니. 말도 되지 않는다.

누구보다 강의 변화에 민감한 것이 바로 그와 같은 사공들이었다.

최근 한 달 사이 유난히 물살이 거칠어지긴 했어도, 우기(雨期)도 아닌데 그런 재해가 발생하는 것은 있을 수 없는 일이다.

잠시 고민하던 사공은 누군가의 커다란 손이 자신의 어깨 위에 올라와 있다는 것을 깨달았다.

“사공. 안 가시오?”

“……갑니다요.”

혁무진의 묵직한 음성에 사공은 천천히 배의 방향을 틀기 시작했다.

물론 가장 약해 보이는 놈이 싸가지도 없다며 내심 욕하는 것도 잊지 않았다.

“사공. 지금 속으로 내 욕했소?”

“……!”

사공의 노가 삐끗함과 동시에 나룻배가 흔들렸다.

처음 출발했을 때보다 더욱 거칠어진 급류가 자그마한 선체를 끌어당기자, 진태경이 한 걸음 앞으로 나서며 쌍장을 흩뿌렸다.

퍼펑!

다시 중심을 되찾고 빠르게 나아가는 나룻배.

서서히 어둑해지는 하늘을 바라보는 진태경의 눈동자가 깊게 가라앉았다.

‘헛짚은 건가?’

홍란이 전해 준 하오문의 정보가 가리키는 지점은 총 다섯 곳.

하지만 물 안과 밖을 샅샅이 뒤져도, 동정어옹의 비처라고 할 만한 흔적은 발견되지 않았다.

연이어 허탕을 치자 처음부터 정보가 잘못된 것인가 하는 의문이 드는 것도 당연했다.

잠시 고민하던 진태경이 고개를 저었다.

‘아니, 아직 단정 짓기에는 일러.’

마지막 한 곳이 남았다. 동정어옹의 비처로 의심되는 다섯 군데의 장소 중에서도 가장 깊고 험한 곳.

어쩌면 남은 네 곳을 합친 것보다 더 중요한 위치라고도 할 수 있다.

만약 그곳이 동정어옹의 비처가 맞다면, 그리고 그곳에서 동정어옹과 맞닥트린다면…….

‘생사결(生死決). 목숨을 걸고 싸워야 한다.’

초절정 고수를 상대로 최선을 다하는 것은 당연한 일이지만, 가능한 한 죽이지 않고 사로잡아야 한다.

동정어옹을 찾는 진정한 목적은 더 큰 몸통을 노리기 위함이니까.

암천은 삼두육비(三頭六臂)의 괴물이나 다름없다. 동정어옹을 죽인다면 팔을 하나 잘라 내는 정도지만, 사로잡는다면 몸통을 칠 수 있다.

“몸통. 몸통이라…….”

작게 중얼거리는 목소리가 바람에 섞여 흩어진다.

진태경은 자신도 모르게 머리를 고정한 은비녀를 어루만지며 문득 한 사람을 떠올렸다.

동정호의 맑은 강물을 메웠던 수백여 구의 시신들과 남겨진 자들의 통곡 역시도.

“반드시 잡는다. 이 개자식들아.”

은비녀에서 흘러나온 은은한 향이 코끝을 맴돌았고, 뱃머리가 검게 물들어 가는 강물을 힘차게 갈랐다.



* * *



동정채(洞庭砦).

장강일도 황충이라는 걸출한 초절정 고수의 지휘 아래, 막강한 영향력을 행사했던 호북성 최대의 수채는 이틀 전부터 찾아온 낯선 이들로 붐볐다.

“셋을 셀 테니 당기시오. 하나, 둘. 영차!”

통나무를 묶어 강물 위에 임시방편으로 길을 만드는 이들. 다른 한편에서는 단정한 학관 차림의 중년인들이 곳곳에서 죽간에 무언가를 써 내려가는 중이다.

그중 한 사람에게 도복을 걸친 젊은 도사가 다가가 물었다.

“실례합니다, 대협. 혹 좌측 절벽의 수색은 이미 끝나셨는지요.”

“우선 절반 정도는 그렇지. 지금까지는 어떤 진법의 흔적도 없다고 본가의 이름을 걸고 장담할 수 있네. 무당파 쪽은 어떠한가?”

“잘 진행되어 가고 있습니다. 혹여 모를 사태를 대비하여 경계도 철저히 하고 있으니 염려하지 않으셔도 됩니다.”

신기제갈(神機諸葛)이라 불리는 제갈세가의 문인들. 그리고 현공진인을 따라 동정채로 온 무당파의 도사들이 그들의 정체였다.

이틀 전만 해도 찾아볼 수 없던 이 낯선 방문자들은 삼삼오오 무리 지어 절벽을 수색하고, 암천의 흔적을 찾기 위해 총력을 기울이고 있었다.

하지만 사방에 깔린 수많은 이목과 밝게 타오르는 횃불로도 알아채지 못한 한 사람의 존재가 있었다.

스윽.

어떠한 소리도, 기척도 존재하지 않는 움직임.

작고 날렵한 인영은 조용하고 은밀하게 절벽으로 향했다. 적게 잡아도 수십에 달하는 사람들을 마주했지만, 누구도 그의 정체를 알아채지 못했다.

고금제일의 살수가 펼치는 유령환살보(幽靈幻殺步) 역시 마찬가지였다.

‘번거롭군.’

내심 중얼거린 문경이 걸음을 내디뎠다.

허공을 밟고 새처럼 뛰어오른 그의 신형이 빠르게 절벽을 누볐다.

아무도 신경 쓰지 않는 소년 의생의 은밀한 수색은 얼마 가지 않아 끝났다.

‘없다. 확실해.’

동정채의 본거지가 마련된 이 공간은 거대했다.

천 명이 가뿐히 넘는 인구를 수용할 수 있는 섬. 사방은 높은 절벽에 가로막혀 있었고 그 위에는 개척되지 않은 좁은 길이 놓여 있다.

하지만 그뿐이었다.

어디에도 사람의 흔적, 혹은 이동진이라 불리는 진법의 잔재는 느껴지지 않았다.

반박귀진을 넘어 반로환동의 경지에 오른 초절정 고수가 이틀간의 수색 끝에 도출한 결론이다.

문경은 이러한 자신의 판단을 믿었고, 동시에 아직 찾지 못한 곳이 있음을 깨달았다.

‘그래, 한 군데가 남아 있었지.’

절벽에서 내려다보이는 강물은 유난히도 넓고 깊었다.

도저히 들어가고 싶지 않을 만큼.

‘……별수 없나.’

더 큰 희생을 막을 수 있는 길이다.

사천당문이 내려다보이는 어느 이름 모를 언덕에서 헤어진 늙은 제자의 얼굴이 눈앞을 스쳤다.

‘알았다. 이 녀석아.’

문경은 조용히 허공을 향해 몸을 던졌다.

스며들 듯이 강물 깊숙이 파고든 그의 신형이 부드럽게 미끄러지며 저 깊숙이 향했다.
```

## Final English reading copy

```markdown
# Chapter 462

The old boatman could not believe the reality unfolding before him.

*What in the world is going on?*

He had worked as a boatman for nearly forty years, ever since he had been around twenty. In all that time, he had never experienced anything as bizarre as today.

*Tap-tap-tap-tap!*

Two figures raced across the sheer cliff above him. It was not the first time he had seen them today, but the sight still amazed him every time.

The boatman stared upward with his mouth hanging open.

*Are those apes or people?*

He had encountered countless martial artists during his years as a boatman, but this was the first time he had ever witnessed martial arts of such astonishing caliber firsthand.

Most martial artists who used his ferryboat were wandering martial artists with mediocre skills and shallow pockets, or disciples of small and middling sects.

*I had my suspicions when the government troops suddenly showed up and ordered me to follow them…*

He had seen it clearly: Officer Gwak, who was in charge of Dongting Lake, had been visibly flustered as he addressed these people with honorifics.

Considering how arrogant the man usually was, there was no doubt that today’s passengers were important figures who carried considerable weight even in the Murim.

*If things go well, I might be able to make a tidy sum.*

He had been considering retirement lately. Whenever he heard about the nonstop tragedies of the past month, unease had settled in one corner of his heart, and his old bones had begun aching more than usual.

He had nearly made up his mind after hearing that hundreds of people had been slaughtered en masse on Dongting Lake the previous night.

*The spirit of Dongting Lake must have grown enraged. The heavenly patterns are ominous, so evil spirits like the Hidden Shadow Ghost are running wild.*

Boatmen were famous for believing in all sorts of superstitions, and old men were prone to retelling legends as though they were facts.

It was only natural that a man who had spent his entire life as a boatman—and had grown old doing it—would decide to retire.

But if important people were calling for him, what choice did he have? When they had dragged him away like a criminal and ordered him to launch the ferryboat, he had been prepared to die.

*Tap-tap-tap-tap!*

But seeing those figures filled him with hope.

Hope that he could survive, of course, but also hope that he might make enough money to retire in comfort.

*They must possess incredible martial arts!*

They said martial masters of the highest realms could fold the earth beneath their feet and walk through the air.

What those people were doing was not much different from the rumors the old boatman had heard secondhand.

Even the young man who appeared to be their leader was charging through the rough water as though he were a fish.

*No, that’s not right. This is already the fourth location. He isn’t fish-like—he’s an actual fish.*

What kind of human being had webbed feet and gills? Every time that young man went underwater, he stayed there for at least one full shichen.

He had already repeated that impossible feat three times. If anyone deserved to be called a martial master, it was him.

*Masters like these could deal with some miscellaneous Fiend like the Hidden Shadow Ghost in an instant.*

If he could only make it out alive, retiring with a fortune would be easy.

Just as the old boatman was brimming with hope, a shout rang out from the cliff above.

“Young Hero Cheongpung! Did you find anything?”

“I’ll tell you when I see something!”

“If you discover anything, tell us immediately!”

“Yes, I certainly will… Ah!”

“Gasp! What is it? What happened?”

A heavy tension abruptly settled over the area.

Hyuk Mujin, who was scanning the surroundings from the slowly moving ferryboat, swallowed hard. So did Gung Gibang, who was watching the opposite cliff with sharply gleaming eyes.

Then, under everyone’s gaze, Cheongpung shouted,

“Wow, it’s a swallow’s nest! I’ve never seen one this big before!”

“…”

“…”

“…”

The air froze solid.

The boatman suddenly thought,

*…Spirit of Dongting Lake, please protect this old man.*

Seeing the people above, he was about to lose what little faith he had left.

That was when it happened.

*Whooosh! Splash!*

A shadow shot out of the water amid a spray of droplets and landed lightly on the ferryboat.

The figure had a build large enough to be called massive, with flexible yet seemingly steel-hard muscles. A beautiful silver hairpin that suited him strangely well held his disheveled hair in place.

“Welcome back.”

At Hyuk Mujin’s greeting, Jin Taekyung silently nodded.

His brow was furrowed. The old boatman cautiously asked,

“Nothing this time either?”

It was a pointless question. If he had discovered something, his expression would not have been so dark.

Jin Taekyung remained deep in thought, his brows drawn together, before opening his mouth.

“This is the fourth location, right?”

“Yes, that it is.”

The old boatman answered, but he could not help watching Taekyung’s mood.

These incredible passengers had already come up empty-handed three times. Including this place, they had failed to find anything four times in total.

Riding in the same boat as martial masters who were clearly in a foul mood was hardly pleasant.

The one thing that was both fortunate and unfortunate was that one final location remained.

*Fwoosh. Hissss!*

Jin Taekyung lightly circulated his internal energy, evaporating the water clinging to him, and asked,

“How long do you think it will take to reach the final location?”

“If we continue at the pace we’ve kept so far, about half an hour should be enough. But…”

The old boatman swallowed before continuing.

“The wind and current are growing stronger the farther we go. It’ll be starting to get dark by the time we arrive, so perhaps it would be better to try the next day.”

“No. It has to be today.”

“But, surely…”

“We have to go. Right now.”

His tone was as decisive as a blade slicing through something. The old boatman closed his mouth.

For some reason, the weather today was ominously foul. The sky, which should have been clear, was filled with dark clouds, while the fierce wind and current showed no sign of settling down.

*I’ve got a bad feeling about this.*

The foreboding he had felt only in the past, when floods or storms were bearing down on them, pricked at every inch of the veteran boatman’s body.

But he forced himself to ignore the unease seeping into his chest.

*Have I grown timid with age? That can’t be it.*

A sudden flood or storm? It made no sense.

Boatmen like him were more sensitive to changes in the river than anyone.

The current had certainly grown unusually rough over the past month, but it was not the rainy season. A disaster of that scale was impossible.

The boatman was still considering it when he realized that a large hand had settled on his shoulder.

“Boatman. Aren’t you going?”

“…I’m going.”

At Hyuk Mujin’s weighty voice, the boatman slowly began adjusting the ferryboat’s course.

Of course, he did not forget to curse inwardly at the rude fellow who looked like the weakest of the group.

“Boatman. Were you cursing me just now?”

“……!”

The boatman’s oar slipped, and the ferryboat rocked.

The rapids had grown even rougher than when they first set out, dragging at the small hull. Jin Taekyung stepped forward and swept both palms outward.

*Boom!*

The ferryboat regained its balance and surged ahead.

As Taekyung gazed at the sky slowly darkening above them, his eyes sank deep.

*Did we get the wrong place?*

The information Honglan had passed on from the Lower District Sect pointed to five locations in total.

But even after searching thoroughly both in and out of the water, they had found no trace that could be called the Dongting Fisherman’s secret refuge.

After coming up empty-handed one place after another, it was only natural to wonder whether the information had been wrong from the beginning.

Taekyung thought for a moment, then shook his head.

*No. It’s too early to decide that.*

One final place remained. Of the five locations suspected to contain the Dongting Fisherman’s secret refuge, it was the deepest and most treacherous.

It might even have been more important than the other four combined.

If it really was the Dongting Fisherman’s refuge—and if they encountered him there…

*It’ll be a life-and-death duel. We’ll have to fight with our lives on the line.*

Against a Supreme Peak master, giving one’s all was only natural. But Taekyung had to capture him without killing him if at all possible.

The true reason he was searching for the Dongting Fisherman was to reach the larger body behind him.

Dark Heaven was practically a three-headed, six-armed monster. Killing the Dongting Fisherman would be like cutting off one of its arms. Capturing him would let them strike at its body.

“The body. The body, huh…”

His quiet mutter scattered into the wind.

Without realizing it, Taekyung touched the silver hairpin holding back his hair and suddenly thought of one person.

He also remembered the hundreds of corpses that had filled the clear waters of Dongting Lake, and the wails of those left behind.

“I’ll catch you. Every last one of you bastards.”

A faint fragrance drifted from the silver hairpin and lingered at the tip of his nose. At the same time, the bow of the ferryboat forcefully split the river, which had begun turning black.

* * *

Donghu Stronghold.

The largest water stronghold in Hubei, which had once wielded tremendous influence under the command of the outstanding Supreme Peak master Hwang Chung, the Yangtze One Saber, had been crowded with unfamiliar visitors since two days ago.

“Pull when I count to three. One, two. Heave!”

Some people were tying logs together to make a makeshift path across the river. Elsewhere, middle-aged men dressed in neat scholar’s robes were writing something on bamboo slips.

A young Daoist wearing a robe approached one of them and asked,

“Excuse me, sir. Has the search of the left cliff already been completed?”

“About half of it. I can stake our family name on the fact that we haven’t found any trace of a Formation so far. How is Wudang doing?”

“It is progressing smoothly. We are also maintaining a strict watch in case anything unexpected happens, so you need not worry.”

They were the Zhuge Clan’s disciples, known collectively as Divine Mechanism Zhuge. The others were Daoists from Wudang who had accompanied Perfected Being Hyeongong to Donghu Stronghold.

These unfamiliar visitors, who had been nowhere to be seen two days ago, had formed groups and were searching the cliffs, devoting all their efforts to finding traces of Dark Heaven.

But even with countless eyes and ears spread throughout the area, and bright torches burning everywhere, they failed to notice one person.

*Swish.*

His movements made no sound and left no trace.

The small, lithe figure quietly and stealthily headed toward the cliff. He passed dozens of people at the very least, yet not one of them noticed who he was.

The same was true of the Ghost Illusory Slaughter Step, performed by the greatest assassin in history.

*What a nuisance.*

Mungyeong muttered inwardly as he stepped forward.

He stepped on empty air and leaped like a bird, his figure quickly sweeping across the cliff.

The stealthy search conducted by the young medical apprentice whom no one paid attention to ended soon afterward.

*Nothing. I’m certain.*

The area where Donghu Stronghold’s headquarters had been established was vast.

It was an island capable of comfortably housing more than a thousand people. High cliffs surrounded it on every side, and narrow, undeveloped paths ran along their upper reaches.

But that was all.

He could not sense a trace of human presence anywhere, nor any remnants of a Formation known as a Moving Formation.

That was the conclusion reached by a Supreme Peak master who had surpassed Returning to Simplicity and reached the realm of Returned to Youth after two days of searching.

Mungyeong trusted his judgment. At the same time, he realized that there was still one place they had not searched.

*That’s right. One place remains.*

The river visible from the cliff was unusually wide and deep.

Deep enough that even he had no desire to enter it.

*…I suppose I have no choice.*

It was a way to prevent an even greater sacrifice.

The face of the old disciple he had parted from on an unknown hill overlooking the Sichuan Tang Clan flashed before his eyes.

*All right, you rascal.*

Mungyeong quietly threw himself into the air.

His figure plunged deep into the river as though melting into it, then slid smoothly toward the depths.
```

<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0533.txt",
      "sha256": "456cfa7873b8744ae458e9c593f862e1103adea16dfcd2aeaab8d166174e6540",
      "bytes": 12727
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "2ab9b664ea7ffb94bd7ae5e35a8fffdaaa5ddb4176fe85f53cf9993e8cb95195",
      "bytes": 3527
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "bcfa782104c00a468f32aeead5cbab95387bc75d449114c87e3d92e5ad938d49",
      "bytes": 169868
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "4e49e9c58f697c64b6c202824803da60a2c263d57eb66b11ef295c39d68e560f",
      "bytes": 553
    },
    {
      "path": "characters/Gung Gibang.md",
      "sha256": "0ed762365385ad999ed7fa237c46d314969e13fc61c5b0076678f3569cb1089b",
      "bytes": 686
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "eccb62a199f12b1dfbde12e26bbc41ec662359ee10e1a4166d28556c26e1adbd",
      "bytes": 1108
    },
    {
      "path": "characters/Jin Mukyung.md",
      "sha256": "4ddf6ba3547690ef70bbe14f51fdfc54705ef2b876c94013d1d01834c0735f19",
      "bytes": 1497
    },
    {
      "path": "characters/Ju Hwaran.md",
      "sha256": "e3b66a91172d596abbe61096d3075479556ed25db39439adc74f28cbf18e131e",
      "bytes": 930
    },
    {
      "path": "characters/Murong Yeonghwi.md",
      "sha256": "ad9fba3b031a101058ba6246f338837e9c8e96e2460fa5946e86a2b890643e63",
      "bytes": 400
    },
    {
      "path": "characters/Sama Pyo.md",
      "sha256": "823dd9bc742cb160cb3ff344ffc504cc76fe39fa9bfb16e5de56e6afc29d59c4",
      "bytes": 630
    },
    {
      "path": "characters/Song Il.md",
      "sha256": "e55d3f3fb9e3735f45d9fe764fbbeb3bb1194cf58bb4bc8492da7e6da0f1fa9a",
      "bytes": 964
    },
    {
      "path": "characters/Song Ilseom.md",
      "sha256": "865198f1414ce40757d4a6875253e5d5a4f14601725f33bdd3e1bfdd1c2f68be",
      "bytes": 889
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "690ff0e887f0437fb3ff4166f30d068b8bf3b5fd0b07144e9c903533893a85e6",
      "bytes": 160285
    }
  ],
  "estimated_tokens": 11465
}
-->

# Durable State Update — Chapter 533

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 533. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 533. Profile updates may replace only one
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
  "chapter": 533,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 533,
    "continuity_sources": [533],
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
    "The Mount Song Resolution formally restored the Murim Alliance; Mae Jonghak is its Alliance Leader, and Song Ho commands the Hidden Shadow Pavilion under his authority.",
    "Jin Taekyung and Cheongpung's prominent role in raising the Murim Alliance flag made them objects of intense attention among Murim factions.",
    "Taekyung believes the Zhongnan Sect resents him, the Jin Family of Taiyuan, and Jeok Cheongang after its repeated humiliations and will obstruct them.",
    "Cheongpung created Mimi Step from Mimi's movements; it is a snake-like footwork technique fast enough that Taekyung could barely track it with his naked eyes, and Cheongpung has recently lost his appetite while refining it.",
    "Mungyeong ended Taekyung's direct training and assigned him a final task of incorporating martial principles into his learned martial arts.",
    "Zhuge Feng's Demon-Sealing Formation still blocks all mana from the exposed Gate, while Jang Taebo is summoning artisans to process the Water God Dragon's remains.",
    "The Southern Heaven Demon Empress is traveling toward Yunnan and expects to cause further deaths.",
    "Unnamed, Hong Dao's practical Disciple, is a scarred Supreme Peak master and Jung Ho's young Martial Uncle after enduring Repentance Cave and receiving Shaolin's Great Restoration Pill.",
    "The Black Dragon Demon Gate remains a major unorthodox power descended from the Demonic Cult's Twelve Branches; Wudang's second report identifies Jang Sam as the Killing Ghost and links his transformation to the Blood Fish.",
    "Jin Taekyung remains a Supreme Peak master with Three Flowers Gather at the Crown, advanced qi perception, exceptional resistance to monster Fear, and public S-rank-level recognition despite retaining an A-rank license.",
    "Ju Hwaran has reunited with Taekyung at Gowolru, while Song Ilseom remains her direct escort.",
    "The unidentified giant who attacked Hwangbo Ak is traveling with Taekyung's group, has an enormous appetite, and remains unidentified; an unfamiliar young martial artist has also appeared after helping Hyuk Mujin."
  ],
  "continuity_sources": [
    532,
    531
  ],
  "open_questions": [
    "What is the Lord of Heaven's identity, how is he connected to the dangerous force Taekyung associates with his original world, and how can Dark Heaven open Gates?",
    "Where is the Southern Heaven Demon Empress ultimately headed, and what does she intend to do in Yunnan?",
    "What is the outcome of the duel between Jeok Cheongang and Nangong Cheon, the Azure Sky Sword King?",
    "Who is the unidentified giant accompanying Ju Hwaran and the two men, and what is his relationship to her?",
    "Who is the unfamiliar young martial artist who helped Hyuk Mujin, and why has he come to Taekyung?"
  ],
  "safe_through": 532,
  "temporary_decisions": [
    "Render 고월루 as Gowolru, 곤륜운룡 as Kunlun Cloud Dragon, and 학우 as Hak Woo.",
    "Render 탈진 as the capitalized system status Exhaustion; retain Ten Dragons and Phoenixes, Blazing Flame Divine Dragon, Dark Heaven, Murim Alliance, and Old Master.",
    "Render 황보세가 as Hwangbo Family, 소가주 as Lesser Family Head, 은비화 as Dagger Hidden Flower, and 전음 as Sound Transmission.",
    "Preserve the chapter's blunt profanity, financial-therapy humor, and monster-comparison humor.",
    "Retain the unidentified giant's clipped, childlike speech and render his exaggerated food count literally."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진무경    | **Jin Mukyung**    |
| 혁무진    | **Hyuk Mujin**     |
| 송일     | **Song Il**        |
| 주화란    | **Ju Hwaran**      |
| 제갈세가   | **Zhuge Clan**                   |
| 십봉룡    | **Ten Dragons and Phoenixes**    |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 낭인     | **wandering martial artist**                     |                                                       |
| 후기지수   | **young prodigy** / **rising martial artist**    | Contextual, not a title                               |
| 정파     | **orthodox faction**                             |                                                       |
| 사파     | **unorthodox faction**                           |                                                       |
| 문주     | **Sect Leader**                              |
| 소문주    | **Young Sect Leader**                        |
| 사천     | **Sichuan**            |
| 감숙     | **Gansu**              |
| 청해     | **Qinghai**            |
| 정마대전   | **Great Faction War**         |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 공자      | **Young Master**                                                |
| 소저      | **Young Lady**                                                  |
| 도사      | **Daoist**                                                      |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 궁기방 | **Gung Gibang** | Beggars' Sect Successor Beggar and finalist. |
| 모용영휘 | **Murong Yeonghwi** | A blood relative of the Murong Family regarded as an overwhelmingly powerful young prodigy. |
| 사마표 | **Sama Pyo** | Young Sect Leader of the Black Dragon Demon Gate. |
| 송일섬 | **Song Ilseom** | Young escort captain of the Yongbong Escort Bureau; distinct from Song Il of Zhongnan. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 기감 | **Qi Sense** | Taekyung's sensory technique; its range reaches seventy meters in this chapter. |
| 사마외도 | **demonic, heterodox arts** | Suspected martial-arts origin of Pung Yang's insidious forms. |
| 내상 | **Internal Injury** | System condition label for internal injury. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 천룡 | **Heavenly Dragon** | The ideal form Jeok Cheongang wishes Taekyung to become. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 계도 | **precept blades** | Blades carried by the Hundred and Eight Arhats. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 화란 | **Hwaran** | Familiar short form of Ju Hwaran. |
| 연검 | **flexible sword** | Ju Hwaran's weapon. |
| 수강 | **Palm Force** | Force generated through a palm technique. |
| 삼국지 | **Romance of the Three Kingdoms** | Classic historical novel referenced in Taekyung's comparison. |
| 열화신룡 | **Blazing Flame Divine Dragon** | New sobriquet bestowed on Jin Taekyung. |
| 제갈 | **Zhuge** | Surname used for Sir Zhuge. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 촌각 | **moments** | Short intervals disappearing from Jeok's day. |
| 흑룡마문 | **Black Dragon Demon Gate** | Unorthodox faction from Gansu. |
| 흑룡도 | **Black Dragon Saber** | Sama Pyo's sobriquet. |
| 모용세가 | **Murong Family** | One of the Five Great Families, based in Liaoning. |
| 공동파 | **Kongtong Sect** | Sect belonging to the Nine Sects and One Gang. |
| 고월루 | **Gowolru** | Three-story inn where the meeting was scheduled. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진무경 | 혁무진 | senior martial artist to subordinate | Hyung Mujin | blunt-senior | Mukyung deliberately misnames Hyuk Mujin as 형무진 before ordering him to stop the carriage. |
| 혁무진 | 진무경 | subordinate to Second Young Master | Second Young Master | deferential | Uses 이공자님 while correcting Mukyung's deliberate misnaming and accepting his orders. |
| 송일섬 | 주화란 | escort_captain_to_young_bureau_head | Hwaran | urgent and familiar | Calls out 화란아 while urgently warning Ju Hwaran before stepping into the confrontation. |
| 주화란 | 혁무진 | rescued_survivor_to_benefactor | Benefactor | formal-deferential | Hwaran includes Mujin among the Benefactors when greeting Taekyung's companions. |
| 주화란 | 궁기방 | rescued_survivor_to_benefactor | Benefactor | formal-deferential | Hwaran includes Gung Gibang among the Benefactors when greeting Taekyung's companions. |
| 주화란 | 송일섬 | bureau_head_to_escort_captain | Captain Song | formal and prosecutorial | Uses his office title, then his personal name, while exposing and confronting him. |
| 송일섬 | 궁기방 | senior_martial_artist_to_Beggars_Sect_successor | Successor Beggar | blunt and irritated | Uses 후개 while objecting to Gung Gibang’s spitting and insults. |
| 궁기방 | 송일섬 | Beggars_Sect_successor_to_young_escort_captain | Young Hero Song | casual and admiring | Uses 송 소협 while praising the famous Soul-Chasing Guest and comparing their looks. |
| 혁무진 | 궁기방 | squad_companion_to_Beggars_Sect_successor | Young Hero Gung | formal-polite, then pointed | Uses 궁 소협 while asking about the culprit and challenging Gung’s insults. |
| 궁기방 | 혁무진 | squad_companions | you; that lunatic | insulting-casual | Gung Gibang mocks Hyuk Mujin's injuries and calls him a lunatic for attacking the Third Fiend. |
| 거한 | 사마표 | Subordinate addressing the Black Dragon Demon Gate Young Sect Leader | Young Sect Leader | Crude and deferential | Uses 소문주 in short, childlike replies. |
| 사마표 | 거한 | Young Sect Leader addressing his giant subordinate | This fellow | Informal and patronizing | Refers to him as 이 녀석 while assigning him responsibility for Do Sangho's death. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 532
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Gung Gibang.md

# Gung Gibang (궁기방)

- **Safe through:** Chapter 532
- **Aliases:** Successor Beggar, Beggar Prince, pure-blooded beggar, ultimate beggar
- **Role:** Gung Gibang is the Beggars' Sect Successor Beggar and a unique eight-knot disciple.
- **Personality:** Vulgar, aggressive, and quick-tempered.
- **Voice:** Blunt, profane, and vividly threatening.
- **Relationships:** Gung Gibang is a rival finalist alongside Baek Woo and Zhuge Gyun who trades insults with Taekyung, uses Beggars’ Sect intelligence to investigate Tang Taesang’s murder and Dark Heaven’s Hubei forces, and has now found a trace of Honglan.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 532
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers and Vice Squad Leader of the Jin Dragon Squad.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jin Mukyung.md

# Jin Mukyung (진무경)

- **Safe through:** Chapter 529
- **Aliases:** Heaven Shaking Sword; Jin Family Second Young Master
- **Role:** Jin Mukyung is the second son of the Jin Family of Taiyuan, a twenty-three-year-old cadet at Heaven’s Gate Temple, and a young Peak-level genius swordsman who has remained secluded in the training hall for more than a year after losing to Cheongpung and refuses to emerge until he achieves a great accomplishment.
- **Personality:** Reserved, terse, and easily irritated by exaggerated praise; glares coldly when Taekyung identifies him
- **Voice:** Quiet and resonant; clipped and blunt in direct speech
- **Relationships:** Taekyung’s older brother and current martial arts instructor; returned to the Jin Family after several years away; three years earlier, he flatly refused seven-year-old Zhu Bao’s request for an autograph

### Ju Hwaran.md

# Ju Hwaran (주화란)

- **Safe through:** Chapter 532
- **Aliases:** Hwaran
- **Role:** Level 88 Young Bureau Head and leader of the Yongbong Escort Bureau, responsible for its personnel and contracts after Heo Jun’s betrayal and now investigating at least two escort captains suspected of aiding his scheme.
- **Personality:** Intelligent, capable, responsible, filial, composed under pressure, and burdened by intense guilt over the escort journey's deaths.
- **Voice:** Clear, polite, restrained, and determined.
- **Relationships:** Escort King Ju Gongsan was her paternal grandfather and rescued the Guangdong Chen Family’s surviving child, who became Song Ilseom’s grandmother; Ju Hogun is her father, Heo Jun was her uncle, and Jin Taekyung’s earlier reassurance remains emotionally vivid to her as she calls out to him after a long separation.

### Murong Yeonghwi.md

# Murong Yeonghwi (모용영휘)

- **Safe through:** Chapter 526
- **Aliases:** None
- **Role:** Murong Yeonghwi is a blood relative of the Murong Family and an overwhelmingly powerful young prodigy.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** He is a blood relative of the Murong Family.

### Sama Pyo.md

# Sama Pyo (사마표)

- **Safe through:** Chapter 515
- **Aliases:** Black Dragon Saber
- **Role:** Young Sect Leader of the Black Dragon Demon Gate and a Morning Star reputed to be no less than the Ten Dragons and Phoenixes.
- **Personality:** Outwardly courteous and smiling, inwardly calculating, and willing to redirect blame onto his subordinate.
- **Voice:** Polite and ingratiating in public, with sardonic humor and controlled evasiveness.
- **Relationships:** Commands a giant subordinate and is the son of a man who previously told him about Jung Ho.

### Song Il.md

# Song Il (송일)

- **Safe through:** Chapter 532
- **Aliases:** Roaring Fury Swordsman
- **Role:** Elder of the Zhongnan Sect and the Roaring Fury Swordsman; senior brother of Sect Leader Gong Iljung; came to the Jin Family of Taiyuan to demand redress for Gong Ilhyuk's injury and the alleged insult to Zhongnan; attacked Jin Taekyung with the Heavenly River Thirty-Six Swords, was stopped by Jeok Cheongang, and was publicly humiliated by him.
- **Personality:** Arrogant, domineering, punitive, and confident in his martial power and seniority.
- **Voice:** Gruff, cutting, condescending, and threatening, with formal authority used to pressure those beneath him.
- **Relationships:** Gong Iljung is his junior Sect Leader and martial younger brother; Gong Ilhyuk is a junior Disciple of his sect; he recognizes Baek Museong and Cheongpung through their Huashan and Sword Saint connections.

### Song Ilseom.md

# Song Ilseom (송일섬)

- **Safe through:** Chapter 532
- **Aliases:** Escort Captain Song
- **Role:** Level 110 young escort captain of the Yongbong Escort Bureau and one of its Dragon-Phoenix Three Escorts who developed his martial ability on battlefields, was known as the Soul-Chasing Guest ten years ago, and plans to remain one more month to help Ju Hwaran purge traitors before seeking an elixir for Ju Hogun in Xianyang.
- **Personality:** Blunt, decisive, survival-hardened, and dryly self-aware, with little patience for insults or disorder.
- **Voice:** Forceful and urgent in command, with a rough and confrontational edge.
- **Relationships:** He serves under Ju Hwaran, is Song Pyosan’s son, and his grandmother was the surviving Guangdong Chen child rescued by Ju Gongsan during the Great Faction War.

## Korean source

```text
＃533화



앞서 소란이 일어난 삼 층은 이미 싹 비워진 지 오래였다.

무림인들 간의 싸움으로 난간이며 벽면까지 무너진 흉흉한 상황에, 아무렇지 않게 술잔을 기울일 만큼 간 큰 이들은 많지 않았다.

게다가 고월루에 드나들 수 있을 만큼 풍족하고 신분 높은 무림인들은 객잔이 아니라 주루를 찾기 마련.

그러니 그런 상황에서도 웃고 있는 불청객의 정체를 유추하는 것은 그리 어려운 일이 아니었다.

‘무림인.’

굳이 생각해 볼 필요도 없는 문제다.

많이 쳐 줘야 이제 이립이나 되었을까 싶은 사내는 시원시원한 미남형이었고 허리춤에는 거무튀튀한 색을 띤 도갑이 매달려 있었다.

그리고…….

‘기세.’

나는 내심 탄성을 흘렸다. 사내에게서 느껴지는 힘과 기세는 지금껏 내가 만난 십봉룡의 그 누구보다도 강했다.

심지어 폐관에 들어가기 전의 진무경보다도.

‘그럼 설마?’

아직 만나지 못한 누군가의 이름이 뇌리를 스친다.

일기천룡(一騎天龍) 모용영휘. 모용세가의 대공자이며 무림 제일의 후기지수라 불리는 열 명의 용과 봉황 중에서도 첫손가락에 꼽히는 자.

‘기감으로 이름을 확인해 봐야 하나.’

혹시나 하는 마음으로 바라보던 그때, 똥 마려운 표정으로 다가온 혁무진이 입을 열었다.

“그, 여기는 제 지인입니다. 조장님을 꼭 한번 뵙고 싶다고 해서…….”

나는 사내를 응시하며 입을 열었다.

“무진아.”

“예?”

“정말 궁금해서 물어보는 건데, 그거 믿으라고 한 소리는 아니지?”

“흡.”

“사실대로 고한다. 실시.”

“……바지에 똥을 지렸는데 저자가 도와줬습니다.”

“대충 알 만하네. 넌 이따가 보자. 옆으로 빠져 있어.”

혁무진이 자살 마려운 표정으로 물러나자 사내의 입가에 맺힌 웃음이 짙어졌다.

“이거 참. 생각 이상으로 눈치가 빠르군.”

“눈치랄 것까지야. 포목점 아들놈한테 이런 친구가 있는 게 더 이상한 일이니까.”

“흠, 그건 몰랐는데. 사실은 그다지 큰 기대도 안 했지만.”

“그런데 초면에 자기소개가 늦으신데. 누구?”

“지나가던 과객이라네.”

“말도 짧으시고.”

“듣기 뭣하면 그쪽도 말 놓지 그러나. 편하게.”

묘한 놈이다. 지금까지 만난 녀석들과도 느낌이 달랐다. 나는 느슨하게 팔짱을 끼며 대답했다.

“그럼 그러지 뭐. 편하게.”

그런 내 모습에 사내가 소리 내어 웃었다.

“열화신룡에 대해서는 소문으로만 들었는데, 듣던 것보다 재미있는 성격이로군.”

“이쪽 입장에서는 엄청 재미있는 상황은 아닌데. 그나저나 자기소개는 여전히 지나가던 과객으로 할 생각인가?”

“날 모르는 모양이군. 이미 벌써 몇 사람은 아는 눈치인데.”

말이 끝남과 동시에 사내의 시선이 향한 곳에는 주화란과 궁기방, 그리고 송일섬이 있었다.

불과 촌각 전만 해도 희미한 웃음을 띠고 있던 주화란이 딱딱해진 표정으로 입을 열었다.

“오랜만에 뵙네요, 소문주.”

소문주?

나도 모르게 의문 섞인 목소리가 입술 사이를 비집고 흘러나왔다.

“주 소저. 아는 사이입니까?”

“한 번 만난 적이 있어요. 감숙성(甘肅省)에서.”

“감숙이라면…….”

정마대전 당시 청해, 사천과 더불어 가장 큰 피해를 입은 지역이다. 구파일방 중에서는 공동파가 위치한 땅이기도 했다.

나는 물끄러미 사내를 바라보았다.

“아무리 살펴봐도 공동파 도사처럼 보이지는 않는데. 내 눈이 잘못된 거면 지금 말해.”

“아니, 제대로 봤네. 오히려 그 반대지.”

사내가 어깨를 으쓱하며 말을 이었다.

“오히려 나 같은 사마외도(邪魔外道)와 엮인 걸 알면 공동파가 기분 나빠할걸. 물론 이쪽도 마찬가지지만.”

“사마외도?”

“흑룡마문(黑龍魔門)이라고 들어 봤는지 모르겠군.”

흑룡마문. 기억 속에서 그 네 글자를 떠올리는 데에는 그리 오랜 시간이 걸리지 않았다.

“들어 보긴 했지.”

언제였던가, 감숙성을 주름잡는 사파 문파에 대해 들었던 기억이 있다.

제아무리 공동파의 위세가 구파일방 중에서도 가장 약한 축에 든다 해도, 세인들로부터 배척받는 사파가 그렇게까지 힘이 있다는 이야기에 상당한 신선함을 느끼기도 했다.

‘이제야 알겠네. 왜 이놈이 십봉룡에 들지 못했는지.’

함께 자리하고 있는 송일섬과 비슷한 경우라고 할 수 있었다.

아무리 주위에서 천하 무림, 무림 동도를 부르짖어도 결국 그들만의 리그가 존재하는 법.

사람들, 아니 정파 무림인들은 재물에 검을 파는 낭인과 예비 범죄자나 다름없는 사마외도를 십봉룡에 끼워 넣기 싫었던 거다.

“그래서, 그 흑룡마문의 소문주씩이나 되는 분이 여긴 무슨 일로?”

내 물음에 사내가 문득 미간을 좁혔다.

“그게 끝인가?”

“그럼 뭐가 더 필요한데?”

“그건…….”

“아, 더 말하고 싶으면 별호나 대 봐. 까먹을 수는 있지만 일단 알고는 있어야지.”

“……흑룡도(黑龍刀) 사마표.”

“이름은 안 물어봤는데. 뭐, 일단 알겠다.”

“…….”

“그나저나 이름 멋있네. 혹시 사마의랑 무슨 관계냐?”

“뭐?”

“뭐긴 뭐야, 사마의라고. 삼국지 나오는 그 사마의.”

사내, 아니 사마표가 당혹감에 물든 표정으로 대답했다.

“성씨만 같을 뿐, 아무런 관계도 없다.”

“그래? 아쉽네. 제갈세가랑 철천지원수면 내가 아는 놈 하나 소개해 주려고 했는데.”

“……그렇다고 제갈세가와 사이가 좋은 것도 아니지.”

“어. 그건 그러네. 그럼 용건이나 말해 봐.”

묘한 눈빛으로 나를 바라보던 사마표가 입을 열었다.

“수하를 데리러 왔다.”

“수하?”

“그래. 저기 앉아 있는 저 곰 같은 녀석.”

누굴 향한 말인지 모르는 사람은 이 중에 단 한 명도 없다. 나를 포함한 사람들의 시선이 한곳으로 쏠렸다.

팔척장신의 거한은 엄청난 덩치가 무색하게도 잔뜩 몸을 수그린 채 사마표의 눈치를 살피는 중이었다.

“태산(太山). 일어나라.”

저놈도 흑룡마문이었어?

그나저나 누가 지었는지는 몰라도 이름 한번 기똥차게 어울리네.

사마표의 부름에 그야말로 산 같은 떡대를 지닌 거한, 태산이 어눌한 목소리로 대답했다.

“주군. 나, 태산이 아니다. 사람 잘못 봤다.”

“…….”

쟤는 진짜 지력 스탯 좀 찍어야 할 것 같은데.

사마표가 끌끌 혀를 찼다.

“사고뭉치 녀석 같으니. 내가 자리를 비우기만 하면 사고를 치는구나. 그만하고 일어나거라.”

“안 된다. 아직 음식 안 나왔다.”

“이런 곰 같은 놈을 보았나. 그렇게 먹고도 모자란단 말이냐?”

“오늘. 여섯 끼. 겨우 먹었다.”

“뭐라? 여섯 끼?”

사마표가 딱딱하게 굳은 얼굴로 중얼거렸다.

“겨우 여섯 끼라니. 내상이라도 입은 게냐?”

“…….”

“…….”

시바, 어이가 없어서 말이 다 안 나오네.

나를 포함한 모두가 할 말을 잃은 사이, 잠시 고민하던 사마표가 고개를 끄덕였다.

“좋아. 그럼 먹고 가자.”

“식사! 좋다! 태산이 여기 있는 음식 다 먹을 거다!”

내가 진심을 담아 입을 열었다.

“제발 태산인지 금수강산인지 하는 저놈 데리고 꺼져 주면 안 될까.”

어딜 이 미친놈들이 은근슬쩍 합석하려고.

내 단호한 태도에 사마표가 눈살을 찌푸렸다.

“야박하군.”

“맞다! 야박하다! 그런데 주군. 야박한 게 뭔가?”

“태산아. 그건 야이씨박새끼들의 줄임말이란다.”

햇님반 어린이에게 친절하게 설명해 준 나는 계단을 가리키며 말을 이었다.

“그러니까 이제 제발 가라. 씨박새끼들아.”

“……!”

순간 묵직한 공기가 주위를 짓눌렀다.

주화란은 숨을 뱉으며 허리에 찬 연검에 손을 가져갔고, 느슨한 자세로 앉아 있던 송일섬은 몸을 바로 세웠다.

그리고 이처럼 갑작스러운 그들의 경계심은 단 한 사람을 향하고 있었다.

‘사마표.’

하지만 놈은 움직이지 않았다. 그저 눈동자가 조금 커졌고, 알 수 없는 생각이 담긴 눈빛으로 날 응시할 뿐이다.

이내 굳게 다물어졌던 입술이 열리며 부드러운 목소리가 흘러나왔다.

“신선하군. 감숙에서, 아니 지금껏 살아오면서 한 번도 겪지 못했던 경험이야.”

“처음이 어렵지, 두 번째부터는 쉬워. 앞으로 많이 해 줄 테니까 걱정 마.”

“앞으로도 많이?”

“내 생각에는 자주 보게 될 것 같은데. 아니면 말고.”

“확실히 다르군. 달라. 그렇지 않으냐?”

마지막에 덧붙인 물음은 나를 향한 것이 아니다.

퉁방울만 한 눈동자를 뒤룩뒤룩 굴리고 있던 태산이 고개를 끄덕였다.

“주군. 맞다. 저 사람. 다르다.”

“그래, 그런 듯싶구나.”

도통 뜻을 알 수 없는 미소가 입가에 떠올랐다가 사라진다.

그리고 다음 순간, 사마표가 한참 위에 있는 태산의 목덜미를 붙잡고 끌어올렸다.

“환영받지 못하는 자리에 오래 있기는 힘들겠다. 이만 가자, 이 녀석아.”

“태산. 아쉽다. 하지만 주군 따른다. 말 잘 듣는다.”

“그럼 이만 가 보도록 하지. 다음에 또 보자고. 열화신룡. 그리고 주 소저도.”

그것이 마지막이었다.

두 사람이 계단을 내려간 뒤, 얼마 지나지 않아 객잔의 문이 닫히는 소리가 들리자 주화란의 굳어 있던 얼굴이 살짝 풀렸다.

“후우.”

나지막한 한숨. 이어 송일섬 역시 바로 세웠던 허리를 등받이에 느슨하게 기댔다.

“전보다 더 강해졌군. 아니, 위험해졌다고 해야 하나.”

그 말을 듣자 아까부터 품고 있던 의문이 더 깊어졌다.

지금까지의 모습을 보면 저쪽과 일면식은 물론 어떤 일이 있었던 건 분명한데…….

‘뭐지?’

그런 내 기색을 눈치챘는지, 누군가가 탁자 아래로 내 발을 건드렸다.

툭. 툭.

볼 것도 없이 궁기방이다. 신호를 전달한 녀석이 거스러미가 가득한 입술을 달싹였다.

- 아무 말도 하지 마. 묻지도 마.

- 왜?

- 그냥 하지 마. 시발 새끼야.

이 자식이 미쳤나. 도대체 뭐길래 이래?

하지만 사람 심리라는 게 뻔하다. 굳이 당사자에게 물어보진 않아도, 그 사실을 아는 누군가에게는 어떻게 해서든 듣고 싶어지는 것이다.

- 뭔데 그래.

- 싫어. 안 말해 줄란다.

- 왜?

- 들어 봤자 좋을 것 없으니까.

그때 궁기방의 바로 옆자리, 나와 곧장 마주 보는 위치에 앉아 있던 주화란이 웃는 얼굴로 접시를 건넸다.

“이거 드셔 보세요. 진 대협.”

“아, 예에.”

웃어야 하는데, 어째서인지 웃음이 안 나온다.

나는 주화란에게 받은 음식을 쑤셔 넣으며, 계속해서 전음을 보냈다.

- 말해.

- 싫다니까.

- 말하라고.

- 싫다고.

이 새끼가 그런데 진짜.

차라리 아는 척이라도 하지 말든가. 하도 철벽처럼 꿈쩍하지 않으니 부아가 치민다.

그리고 내가 재차 전음을 날리려던 바로 그 순간이었다.

“아, 진 대협. 깜빡하고 말씀을 못 드린 게 있는데.”

“좋게 말할 때 뭔지 말하라, 예?”

하마터면 큰 실수를 할 뻔했다.

입에 가득 음식을 넣은 채 고개를 든 내게, 주화란이 말을 이었다.

“저 사람이요. 흑룡마문의 소문주.”

“사마표요?”

“음. 네.”

“어…… 무슨 일이라도 있었습니까?”

“일이라면 일이고. 아니라면 아닌데.”

나를 물끄러미 바라보던 주화란이 한 마디를 던졌다.

아니, 그건 폭탄이었다.

“저 사람. 한때 제 정혼자였어요.”

“푸우우우웃!”

“꺄아아아악!”

“으아아악!”
```

## Final English reading copy

```markdown
# Chapter 533

The third floor, where the commotion had broken out earlier, had been completely cleared out long ago.

Not many people were bold enough to calmly sip their drinks in a place where a fight between martial artists had brought down the railings and even parts of the walls.

Besides, martial artists wealthy and important enough to enter Gowolru generally sought out restaurants rather than inns.

So it wasn’t difficult to guess the identity of the uninvited guest who was still smiling despite everything.

*A martial artist.*

There was no need to think about it any further.

The man looked no more than thirty, with open, strikingly handsome features, and a blackish saber scabbard hung from his waist.

And then there was…

*His aura.*

I couldn’t help exclaiming inwardly. The power and aura I felt from him were stronger than those of any member of the Ten Dragons and Phoenixes I had encountered so far.

Even stronger than Jin Mukyung before he entered seclusion.

*Could it be?*

The name of someone I had yet to meet flashed through my mind.

Murong Yeonghwi, the One-Ride Heavenly Dragon. The eldest son of the Murong Family, and one of the foremost among the ten dragons and phoenixes known as the greatest young prodigies in the Murim.

*Should I use Qi Sense to confirm his name?*

Just as I was watching him with that thought in mind, Hyuk Mujin approached with an expression like he was about to shit himself and opened his mouth.

“Um, this is an acquaintance of mine. He said he really wanted to meet you, Captain…”

I stared at the man and spoke.

“Mujin.”

“Yes?”

“I’m asking because I’m genuinely curious. You didn’t actually expect me to believe that, did you?”

“Ghk.”

“Report honestly. Now.”

“……”

“I shit my pants, and he helped me.”

“I figured it was something like that. We’ll talk later. Step aside.”

As Hyuk Mujin backed away with an expression like he wanted to kill himself, the smile at the corners of the man’s mouth deepened.

“Well, this is something. You’re even more perceptive than I expected.”

“It’s not that impressive. It’s more unusual for the son of a textile-shop owner to have a friend like you.”

“Hm. I didn’t know that. Though, to be honest, I didn’t have particularly high expectations.”

“You’re taking your time introducing yourself for someone we’ve just met. Who are you?”

“I’m merely a passing traveler.”

“Your speech is pretty casual, too.”

“If that bothers you, drop the formalities yourself. Relax.”

What a strange guy. He felt different from everyone else I had met until now. I loosely crossed my arms and answered.

“Sure. Let’s keep it casual.”

The man laughed out loud at my response.

“I had only heard about the Blazing Flame Divine Dragon through rumors, but you’re even more interesting than I’d heard.”

“It’s not exactly a fun situation from where I’m standing. Anyway, are you still planning to introduce yourself as a passing traveler?”

“You don’t seem to know who I am. A few people here already look like they recognize me.”

As soon as he finished speaking, his gaze turned toward Ju Hwaran, Gung Gibang, and Song Ilseom.

Ju Hwaran, who had been wearing a faint smile only moments ago, spoke with a stiff expression.

“It’s been a while, Young Sect Leader.”

Young Sect Leader?

A puzzled voice slipped from my lips before I could stop it.

“Young Lady Ju. You know him?”

“We met once. In Gansu.”

“Gansu…”

Along with Qinghai and Sichuan, Gansu had suffered some of the heaviest damage during the Great Faction War. It was also where the Kongtong Sect, one of the Nine Sects and One Gang, was located.

I stared at the man.

“No matter how closely I look, you don’t seem like a Daoist of the Kongtong Sect. If I’m wrong, tell me now.”

“No, you saw correctly. If anything, it’s the opposite.”

The man shrugged and continued.

“If Kongtong found out it had been associated with a demonic, heterodox practitioner like me, it would be displeased. Of course, I feel the same way.”

“A demonic, heterodox practitioner?”

“You may or may not have heard of the Black Dragon Demon Gate.”

Black Dragon Demon Gate. It didn’t take long for me to recall those four words.

“I’ve heard of it.”

At some point, I had heard about the unorthodox sect that dominated Gansu.

Even though the Kongtong Sect was considered one of the weaker members of the Nine Sects and One Gang, I had found it rather surprising that an unorthodox faction rejected by the public could wield that much power.

*Now I understand why this guy isn’t one of the Ten Dragons and Phoenixes.*

His situation was similar to Song Ilseom’s.

No matter how loudly people cried out about the world’s Murim and their fellow martial artists, there was always a league of their own.

People—or rather, orthodox martial artists—had no desire to include wandering martial artists who sold their swords for money and demonic, heterodox practitioners no different from would-be criminals among the Ten Dragons and Phoenixes.

“So, what business does someone as important as the Young Sect Leader of the Black Dragon Demon Gate have here?”

At my question, the man suddenly furrowed his brow.

“Is that all?”

“What else do you need?”

“That…”

“If you want to say more, give me your sobriquet. I might forget it, but I should at least know it.”

“……Black Dragon Saber. Sama Pyo.”

“I didn’t ask for your name. But all right, now I know.”

“……”

“Your name is pretty cool, though. Are you related to Sima Yi?[^1]”

“What?”

“What do you mean, what? Sima Yi. The one from *Romance of the Three Kingdoms*.”

[^1]: “Sama” is the Korean reading and “Sima” the Mandarin reading of the same surname, 司馬.

The man—or rather, Sama Pyo—answered with an awkward expression.

“Our surnames are the only thing we have in common. We have no relation.”

“Really? What a shame. If you were sworn enemies of the Zhuge Clan, I was going to introduce you to someone I know.”

“……That doesn’t mean I have a good relationship with the Zhuge Clan.”

“Yeah, that makes sense. Now tell me why you’re here.”

Sama Pyo studied me with a strange gaze before speaking.

“I came to retrieve my subordinate.”

“Your subordinate?”

“Yes. That bear-like fellow sitting over there.”

Not a single person present could have wondered who he meant. Everyone’s gaze, including mine, turned in the same direction.

The towering giant was crouched down so deeply that his enormous size seemed almost wasted, watching Sama Pyo nervously.

“Taishan. Get up.”

*That guy is from the Black Dragon Demon Gate, too?*

Still, whoever named him had chosen a name that fit him perfectly.

At Sama Pyo’s call, the giant—whose physique truly resembled a mountain—answered in a clumsy voice.

“Lord. I am not Taishan. You mistook person.”

“……”

*He really needs to put some points into intelligence.*

Sama Pyo clicked his tongue.

“You troublemaker. You cause trouble every time I leave you alone. Enough. Get up.”

“Cannot. Food not out yet.”

“What a bear of a man. You’ve eaten that much and you’re still not full?”

“Today. Ate six meals. Barely.”

“What? Six meals?”

Sama Pyo muttered with a rigid expression.

“Only six meals? Have you suffered an Internal Injury?”

“……”

“……”

*For fuck’s sake. I’m speechless.*

While everyone—including me—lost all ability to speak, Sama Pyo thought for a moment and nodded.

“All right. Then we’ll eat before we go.”

“Food! Good! Taishan eat all food here!”

I spoke with complete sincerity.

“Could you please take that guy—Taishan or the entire scenic landscape, or whatever—and get the hell out of here?”

*Why are these lunatics trying to slip into our table?*

Sama Pyo frowned at my firm refusal.

“How stingy.”

“That’s right! Stingy! But Lord, what is stingy?”

“Taishan, it’s short for ‘you fucking bastards.’”

After kindly explaining it to a child from the Sunshine Class, I pointed toward the stairs and continued.

“So go now. You fucking bastards.”

“……!”

A heavy silence pressed down on the room.

Ju Hwaran let out a breath and reached for the flexible sword at her waist, while Song Ilseom, who had been sitting in a relaxed posture, straightened his body.

And their sudden vigilance was directed at only one person.

*Sama Pyo.*

But he didn’t move.

His eyes widened slightly, and he merely stared at me with an unreadable look.

Then his tightly closed lips parted, and a gentle voice flowed out.

“How refreshing. I’ve never had an experience like this in Gansu—or in my entire life.”

“The first time is the hardest. It gets easier from the second time onward. I’ll give you plenty more of it from now on, so don’t worry.”

“Plenty more in the future, too?”

“I have a feeling we’ll be seeing each other often. If not, forget it.”

“You’re certainly different. Very different. Don’t you agree?”

The question he added at the end wasn’t directed at me.

Taishan, who had been rolling his enormous eyes around, nodded.

“Lord. Correct. That person. Different.”

“Yes, so it seems.”

A mysterious smile appeared at the corners of Sama Pyo’s mouth, then vanished.

The next moment, Sama Pyo reached up and grabbed Taishan by the nape of his neck, far above his own head, then hauled him upright.

“It seems difficult to stay somewhere we aren’t welcome. Let’s go, you fool.”

“Taishan disappointed. But Taishan follows Lord. Obeys well.”

“Then we’ll be off. See you next time, Blazing Flame Divine Dragon. And Young Lady Ju.”

That was it.

After the two of them descended the stairs, the sound of the inn’s door closing reached us a short while later. Ju Hwaran’s stiff expression relaxed slightly.

“Whew.”

She let out a quiet sigh. Then Song Ilseom relaxed as well, leaning back against his chair.

“He’s stronger than before. No, perhaps I should say he’s more dangerous.”

Hearing that, the question I had been carrying since earlier grew even deeper.

Judging by everything I had seen, they had clearly experienced something together—more than merely having met once…

*What was it?*

Perhaps someone noticed my expression, because a foot tapped mine beneath the table.

Tap. Tap.

There was no need to look. It was Gung Gibang. His chapped lips moved after sending the signal.

*—Don’t say anything. Don’t ask anything.*

*—Why?*

*—Just don’t, you fucking bastard.*

*What the hell is wrong with this guy? What could possibly be so serious?*

But human nature was simple. Even if I didn’t ask the person involved directly, I still wanted to hear the story from someone who knew about it.

*—What is it?*

*—I don’t want to. I’m not telling you.*

*—Why?*

*—Because you won’t gain anything from hearing it.*

At that moment, Ju Hwaran, who was sitting right beside Gung Gibang and directly across from me, handed me a plate with a smile.

“Please try this, Great Hero Jin.”

“Ah, yes.”

I was supposed to smile, but for some reason, I couldn’t.

I shoved the food Ju Hwaran had given me into my mouth and continued sending Sound Transmissions.

*—Tell me.*

*—I said no.*

*—Tell me.*

*—I said I won’t.*

*This bastard, seriously.*

He could at least have pretended not to know anything. But he refused to budge, stonewalling me so completely that I grew irritated.

And it was at the exact moment I was about to send another Sound Transmission that Ju Hwaran spoke.

“Oh, Great Hero Jin. There’s something I forgot to mention.”

“Tell me what it is while I’m still asking nicely, okay?”

I nearly made a huge mistake.

With my mouth full of food, I raised my head, and Ju Hwaran continued.

“That person. The Young Sect Leader of the Black Dragon Demon Gate.”

“Sama Pyo?”

“Mm. Yes.”

“Um… Did something happen?”

“If you call it something, yes. If you don’t, then no.”

Ju Hwaran stared at me and dropped a single sentence.

No, it wasn’t a sentence.

It was a bomb.

“He used to be my fiancé.”

“Pffft!”

“Aaaaaah!”

“Uaaaaah!”
```

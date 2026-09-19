<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0454.txt",
      "sha256": "38fbceaf87ae79dc362877464fb8a65539f49d23cf92d52d62fef57c4eae6044",
      "bytes": 13937
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "d4bb07092e76f9b042d980c440af9848c336c6a94ed233d171a586cb36d62997",
      "bytes": 2878
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "5ceb4e2130e96b73416093a48ef6f8dbd0481a439d6861b5a7d26bca9fb46bb3",
      "bytes": 149097
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "03e611c0c716689092f5d867fad7a7fd2295f803d9e1971fe59f9a0ebb789e7c",
      "bytes": 944
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "12b0e69691abe3186d8419da341b3dbeb24c9c544d5b6e69f58e4626e1c5e7f2",
      "bytes": 553
    },
    {
      "path": "characters/Gung Gibang.md",
      "sha256": "a5c9f2e1af45b80bf3ee1207d384661c2188616a89e02bd9b3941a6c8a00a2b8",
      "bytes": 609
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "2cac9b3fc3a80ef96fccdc891b10d128a7cb22e1add2d0de1555d86aec373d04",
      "bytes": 1108
    },
    {
      "path": "characters/Ju Wongong.md",
      "sha256": "f901d6f816510ff7287f3269e7d43b99aa336a173323e79cc06e2a14379673d9",
      "bytes": 628
    },
    {
      "path": "characters/Prince Shangshan.md",
      "sha256": "5060dc6f0bc0b5ac13eab3e451a944b330bd83256045b093b6dbbe85bf7ee6ef",
      "bytes": 1019
    },
    {
      "path": "characters/Wolhwa.md",
      "sha256": "f7b881528fd57b51bcb4efe2d6bb9ac05750760ce6ec7493afd7549976e636ca",
      "bytes": 2457
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "e461e36fdfca1b36145d5e3c2c1ab27e0d867d36d7f0c4d6478c5994b61b21fa",
      "bytes": 142508
    }
  ],
  "estimated_tokens": 11394
}
-->

# Durable State Update — Chapter 454

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 454. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 454. Profile updates may replace only one
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
  "chapter": 454,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 454,
    "continuity_sources": [454],
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
    "Taekyung accepted Quest Another Chaos to uncover the truth behind the Hubei incidents and find the culprit.",
    "Jin Wikyung is acting as an inspector for the new Murim Alliance and is cooperating with Taekyung's investigation.",
    "The shared symbols between the Arch Lich's magic circle and Dark Heaven's formations remain unexplained.",
    "The Sea Serpent Society and the Yangtze River Channel League's Hubei strongholds were destroyed, while the Dongting Fisherman disappeared.",
    "Wudang is responding to an unidentified killer demon responsible for more than thirty deaths, including twenty pilgrims on Mount Wudang.",
    "The Skeleton King's undead identity remains concealed, and Taekyung has ordered him to join Peace Guild under a prepared contract.",
    "Go Jun is expected to succeed Lee Jungryong as Ares Guild's captain and is searching China for Lee's holographic recorder.",
    "Taekyung's party has escaped Tianling Falls, reached Zaoyang, and is traveling by land toward the Zhuge Clan.",
    "Qingxia Hall is an influential Hubei social club formed by powerful families' children, and its members are obstructing the party's departure through public confrontations.",
    "Ju Wongong leads the current Qingxia Hall entourage, claims distant kinship with the Emperor, and is now facing Taekyung after his guards were defeated."
  ],
  "continuity_sources": [
    453,
    452
  ],
  "open_questions": [
    "What are the origin and purpose of the symbols shared by the Arch Lich's magic circle and Dark Heaven's formations?",
    "Who destroyed Donghu Stronghold and the related Yangtze River Channel League strongholds, and why was no Moving Formation trace left behind?",
    "Is the Dongting Fisherman a member of Dark Heaven, and who are the other Supreme Peak attackers?",
    "Is the killer demon attacking Wudang connected to Dark Heaven?",
    "What evidence is contained in Lee Jungryong's holographic recorder, and what are the terms of the Peace Guild–Wizard Guild agreement?"
  ],
  "safe_through": 453,
  "temporary_decisions": [
    "Render 황철 as Hwang Cheol, 도립군 as Do Ripgun, 광수도귀 as Mad Water Saber Demon, 파랑호 as Wave Fox, 동정호 as Dongting Lake, and 사천혈사 as Sichuan Blood Tragedy.",
    "Render 살귀 as killer demon and 일급 낭인 as First Rate wandering martial artist.",
    "Render 시부럴 as “sibu-leol,” 시벌좌 as “Lord Fuck,” and 시부럴좌 as “Lord Sibu-leol.”",
    "Preserve the Skeleton King's grandiose, mock-offended voice and Taekyung's dry, profane humor.",
    "Render 주원공 as Ju Wongong, 대죽산표국 as Daejuksan Escort Bureau, 형문검가 as Hyungmun Sword Family, 응성상회 as Eungseong Merchant Association, 천룡인 as Celestial Dragon, and 사인교 as four-person sedan chair."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 혁무진    | **Hyuk Mujin**     |
| 청풍     | **Cheongpung**     |
| 월화     | **Wolhwa**         |
| 하오문    | **Lower District Sect**          |
| 제갈세가   | **Zhuge Clan**                   |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 상태               | **Status**                     |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 공자      | **Young Master**                                                |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 궁기방 | **Gung Gibang** | Beggars' Sect Successor Beggar and finalist. |
| 주원공 | **Ju Wongong** | Qingxia Hall leader who claims distant kinship with the Emperor. |
| 상산왕 | **Prince Shangshan** | The City Lord and a member of the imperial family who orders the luncheon. |
| 주씨 | **Zhu** | Surname of the imperial ruling house. |
| 천자 | **Son of Heaven** | Honorific title for the Emperor. |
| 황상 | **Emperor** | Address or reference to the reigning Emperor. |
| 개방 | **Beggars' Sect** | Murim organization counted among the Nine Sects and One Gang. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 주표 | **Zhu Bao** | Personal name of Prince Shangshan. |
| 선황 | **the late Emperor** | The former Emperor whom Hong Jin served. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 천룡 | **Heavenly Dragon** | The ideal form Jeok Cheongang wishes Taekyung to become. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 존슨 | **Johnson** | Co-host of the American talk show that replays Taekyung's viral interview. |
| 호북 | **Hubei** | Province on Ju Gongsan's route from Guangdong to Henan. |
| 장강 | **Yangtze** | The river controlled by the Yangtze River Channel League. |
| 동정호 | **Dongting Lake** | Lake under which Dangyang and Honghu Strongholds operated. |
| 청협방 | **Qingxia Hall** | Unofficial Hubei social club formed by influential families' children. |
| 천룡인 | **Celestial Dragon** | Taekyung's mocking label for a privileged imperial noble. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 월화 | 혁무진 | inn proprietress and branch leader to visiting martial artist | Young Martial Artist; Martial Artist | polite and teasing | Uses 젊은 무사님 and 무사님 while discussing her profession and correcting Mujin's conduct. |
| 혁무진 | 월화 | Jin Family retainer to Lower District Sect Branch Leader | Young Lady; Branch Leader | formal-polite, then deferential | Initially addresses Wolhwa as 소저, then corrects himself to 지부장님 after learning her identity. |
| 청풍 | 혁무진 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung includes Mujin among his 은인들 after receiving the skewers. |
| 혁무진 | 청풍 | martial artist to young master | Young Master | formal-deferential | Mujin uses 공자께서는 when asking why Cheongpung descended from the mountain. |
| 주표 | 청풍 | prince_to_young_martial_artist | you | formal and gatekeeping | Refuses Cheongpung's autograph until he acquires a martial title. |
| 혁무진 | 궁기방 | squad_companion_to_Beggars_Sect_successor | Young Hero Gung | formal-polite, then pointed | Uses 궁 소협 while asking about the culprit and challenging Gung’s insults. |
| 궁기방 | 혁무진 | squad_companions | you; that lunatic | insulting-casual | Gung Gibang mocks Hyuk Mujin's injuries and calls him a lunatic for attacking the Third Fiend. |
| 궁기방 | 청풍 | martial_companions | Young Hero Cheongpung | formal-polite | Gung Gibang uses 청 소협 while asking why Cheongpung is at the temporary clinic. |

## Listed compact profiles

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 453
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, the grandson and Disciple of Sword Saint Mae Jonghak, and a Supreme Peak martial master known as the Huashan Divine Dragon.
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, a deep love of martial arts, and a martial artist's competitive pride; he becomes unsettled when someone copies his martial arts
- **Voice:** Dreamy and hazy, with innocent, polite phrasing
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions while Taekyung is his only true martial rival; Tang Sadok has temporarily entrusted Mimi to him.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 449
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Gung Gibang.md

# Gung Gibang (궁기방)

- **Safe through:** Chapter 453
- **Aliases:** Successor Beggar, Beggar Prince, pure-blooded beggar, ultimate beggar
- **Role:** Gung Gibang is the Beggars' Sect Successor Beggar and a unique eight-knot disciple.
- **Personality:** Vulgar, aggressive, and quick-tempered.
- **Voice:** Blunt, profane, and vividly threatening.
- **Relationships:** Rival finalist alongside Baek Woo and Zhuge Gyun; trades insults with Taekyung and is helping investigate Tang Taesang’s murder through Beggars’ Sect intelligence.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 453
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers and Vice Squad Leader of the Jin Dragon Squad.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Ju Wongong.md

# Ju Wongong (주원공)

- **Safe through:** Chapter 453
- **Aliases:** Qingxia Hall young master
- **Role:** Ju Wongong is a Qingxia Hall young master who claims to be a distant imperial relative descended from the Emperor's dragon blood.
- **Personality:** Entitled, status-conscious, theatrical, and amused by violence until his own protection is overcome.
- **Voice:** Pompous and imperious, with formal declarations of rank and authority.
- **Relationships:** His Qingxia Hall entourage and four Peak guards obey him; he asserts kinship with the Emperor.

### Prince Shangshan.md

# Prince Shangshan (상산왕)

- **Safe through:** Chapter 377
- **Aliases:** None
- **Role:** The City Lord and a member of the imperial family; ten-year-old Prince Shangshan, whose personal name is Zhu Bao, is an exceptionally skilled young swordsman who has trained daily for three years.
- **Personality:** Earnest, admiring, and eager to emulate Jin Taekyung; despite his royal dignity, he shows openly childlike enthusiasm for martial arts and Taekyung's reputation.
- **Voice:** Archaic and formal in the manner of a historical drama, with openly eager and childlike reactions beneath his royal diction.
- **Relationships:** Commands the unnamed Third-Rank Assistant Military Commissioner to attend the luncheon and hosts the gathering of young Murim prodigies; admires Jin Taekyung and seeks to emulate him; has been invited to the Jin Family's grand banquet in fifteen days, where Taekyung promises to obtain Jin Mukyung's autograph for him.

### Wolhwa.md

# Wolhwa (월화)

- **Safe through:** Chapter 328
- **Aliases:** Eun Sowol (은소월); Wolhwa is the name used at Honghwaru
- **Role:** Shanxi’s foremost information merchant and Level 50 martial artist; Branch Leader of the Lower District Sect’s Shanxi branch with authority to mobilize more than thirty Shanxi branches; formerly posing as a high-ranking courtesan at Honghwaru, a pleasure house in central Taiyuan
- **Personality:** Striking, composed, observant, direct, quietly amused, and capable of ruthless, decisive violence when extracting information; comfortable teasing Taekyung while conducting serious information and negotiation work
- **Voice:** Polite and lightly playful; addresses Taekyung as Young Master Jin and delivers embarrassing observations without raising her voice
- **Relationships:** Knows Taekyung as a Honghwaru regular and the youngest son of the Jin Family; says she likes him, though her sincerity is unclear; has negotiated a mutually beneficial alliance with Jin Wikyung and the Jin Family

## Korean source

```text
＃454화



눈을 부릅뜬 채 굳어 있던 청년, 아니 주원공이 떨리는 목소리로 물었다.

“뭐, 뭐라?”

이놈은 아까부터 귓구멍이 막혔나. 자꾸 했던 말을 반복하게 만드네.

입을 딱 벌린 채 나와 주원공을 번갈아 바라보는 사람들의 시선을 무시하며 재차 입을 열었다.

“내리라고.”

“나, 난 주원공이다!”

“주인공이든 주원공이든. 내려.”

“네놈도 결국 대국의 백성일진대, 황상 폐하의 혈족인 내게 어찌 이리도 무례를 범할 수 있단 말이냐!”

“내 친구 중에 존슨이라고 있거든? 그 사람 있었으면 다른 걸 범했을 거야.”

“……!”

“마지막으로 말한다. 내려.”

무슨 소리인지는 몰라도 사람이라면 누구나 위험을 감지하는 법.

본능적으로 엉덩이를 움찔거리던 주원공이 슬그머니 몸을 일으켰다.

하지만 생전 경험해 본 적 없는 상황에 불안한 듯 눈동자를 굴리면서도, 황족이라는 배경을 믿는지 마지막까지 엄포를 놓는 걸 잊지 않았다.

“이, 이러고도 무사할 것 같으냐!”

“어, 무사할 것 같은데.”

“황족을 능멸하다니, 이건 역모다!”

“탈모만 아니면 돼.”

“뭐 이런 놈이……!”

아무렇지 않게 대꾸했지만, 크게 틀린 말은 아니다.

천자(天子)와 같은 주씨 성에 용의 핏줄을 타고난 자. 그 자체로 존귀한 것이 황족이니까.

비록 무림과 관부가 상호불가침의 관계라는 해도 황족에 대한 무례와 위협은 중죄로 취급받는다.

괜히 아까부터 제갈세가 가솔이 똥 마려운 강아지처럼 끙끙거리는 것이 아니다.

“그, 이제 그만하시는 편이 좋을 듯합니다.”

나는 가솔의 속삭임에 눈살을 찌푸렸다.

“왜요?”

“예, 예?”

“제가 뭐 했어요? 욕을 한 것도 아니고, 그렇다고 죽인다고 협박한 것도 아닌데. 심지어 공격도 저쪽에서 먼저 했어요. 전 사인교에서만 내리라고 한 거고.”

“……아니, 뭐. 따지고 보면 그건 맞는데. 그래도 황족 아닙니까.”

“황족도 황족 나름이지, 팔촌이면 같은 핏줄이 아니라 그냥 피 몇 방울 떨어트린 수준 아닙니까? 당장 제가 장강에 침 좀 뱉으면 저랑 장강이랑 팔촌 정도는 될 것 같은데.”

“헉. 진 대협, 제발.”

“괜찮아요. 어차피 작게 말해서 아무도 못 들었을 테니까.”

그때, 나와 가솔이 속닥거리는 모습을 착각한 주원공이 기세등등한 목소리로 외쳤다.

“이제야 사태를 파악한 모양이군. 하지만 이미 늦었다. 곧 황실의 십만 대군이 출동하여 네놈을 포함한 역도들의 구족(九族)을 멸할 것이니!”

“오, 버스터 콜.”

“아까부터 뭐라는 것이냐, 이 역적놈아!”

“헉!”

“히이익!”

주원공의 눈에 숨길 수 없는 분노가 깃들자, 양민들이 헛숨을 삼키며 바닥에 넙죽 엎드렸다. 이미 곳곳에서는 도망치는 이들까지 속출했다.

괜한 일에 연루되는 것을 피하려는 모양인데, 보는 눈이 적어지는 셈이니 내 입장에서도 나쁠 건 없었다.

‘그나저나 이것들은 심심하면 구족을 들이미네.’

구족 이하로는 취급을 안 해 주나?

한숨을 푹 내쉬는 내게 제갈세가의 가솔이 속삭였다.

“너무 겁먹지는 마십시오. 십만 대군 운운한 것은 허세니까요.”

“……제가 바봅니까? 그걸 믿게.”

“애초에 주 공자는 황족의 권위를 내세워 재산을 착복하다가 귀양 온 상태라, 일을 키울 생각은 없을 겁니다. 그러니 적당한 선에서 사과하고 물러나시지요.”

“잠깐만. 귀양?”

“예.”

“저게?”

“황족이잖습니까. 아무리 먼 방계라고는 해도 핏줄은 무시 못 합니다. 게다가 황위 계승 서열과는 거리가 먼 방계라, 죄를 지어도 적당한 향응을 누릴 수 있게 해 주는 것이지요.”

“요컨대, 하도 좆밥이라 주위에서 신경도 안 쓴다?”

“……진 대협, 제발 말씀을 좀 가려서 하십시오.”

나는 가솔의 푸념을 한 귀로 흘려들으며 피식 웃었다.

황족씩이나 되는 놈이 왜 황궁이 아니라 호북성 대로변에서 망나니들과 친목질을 하고 있나 했더니, 생각했던 것 이상으로 별 볼 일 없는 놈이었다.

뭐, 팔촌 운운했을 때부터 짐작했던 거긴 하지만.

“우선 존귀한 이 몸을 알아보지 못한 네 놈의 그 오만한 눈깔을 파 버리고, 오체분시를 한 다음……!”

“그래. 알겠으니까 그다음은 이거나 보고 다시 이야기하자고.”

나는 일장 연설을 쏟아내는 주원공을 향해, 품에서 꺼낸 물건을 던졌다.

동시에 가슴을 한껏 펴고 있던 놈이 양팔을 허우적거리며 주저앉았다.

“암기다! 암기! 이놈이 황족을 시해하려 한다!”

“……수준 상당하네, 진짜.”

그리고 다음 순간.

주원공의 발 앞에 툭, 하고 떨어진 ‘암기’가 모두의 시선 속에서 찬란한 빛을 흩뿌렸다.

“어?”

의문 어린 눈빛으로 자신의 발 앞에 놓인 물건을 바라보던 주원공이 멍하니 입을 벌렸다.

“어? 어어, 어어어어!”

물음표가 느낌표로, 분노가 경악으로 바뀌기까지는 그리 오랜 시간이 걸리지 않았다.

구름과 용이 음각된 상산왕 주표의 증표와 나를 번갈아 바라보던 주원공이 무겁게 입을 뗐다.

“내 자비를 베풀어, 그대를 용서하겠노라.”

“…….”

지랄한다.



* * *



“그래서, 동정호 가는 길이셨다고?”

“그렇다! 아니, 그렇소!”

내 부드러운 음성에 주원공이 힘차게 고개를 끄덕였다.

그가 고용한 청협방의 꽃 병풍들은 뒤늦게 도착한 관군들과 함께 사람들을 입단속 시키고 있었고, 기어코 만두 대량 구매에 성공한 청풍은 동정호라는 말에 눈을 동그랗게 떴다.

“와아, 동정호!”

비로소 이 만두 귀신의 신분을 알게 된 주원공이 불안한 눈빛으로 청풍의 허리춤에 찬 검을 힐끗거렸다.

“그, 그대가 원한다면 초대해 줄 수도 있소만…….”

내가 중얼거렸다.

“마음에도 없는 소릴 하시네.”

“착각이다! 아니, 착각이오.”

“그럼 평소에도 착각을 자주 하는 성격이신가? 조용히 지나가려는 사람도 공격하는 걸 보면 그런 것 같기도 하고.”

“그건…… 내 다시 한번 사과드리리다. 상산왕 전하의 증표를 갖고 계신 줄은 꿈에도 몰랐소.”

“아, 증표가 없었으면 십만 대군을 끌고 와서 구족을 멸하고, 눈깔 뽑은 다음 오체분시를 했을 것이다?”

“무, 무슨 그런 말씀을. 허, 허허허.”

억지로 웃는 모습이 안쓰러울 지경이다.

‘나도 증표의 효과가 이 정도일 줄은 몰랐는데.’

주원공이 이토록 저자세로 나오는 데에는 다 이유가 있었다.

동물도 순종, 잡종을 따지는데 천하에서 가장 고귀한 핏줄이라는 황족은 오죽하겠나.

같은 황실의 피가 흐른다고 해도 상산왕 주표는 천자의 하나뿐인 동복동생이자, 그가 직접 임명한 유일한 번왕(藩王)이기도 하다.

선황 사후, 제위를 둘러싼 다툼에서 수많은 핏줄을 제거한 냉혹한 황제의 아픈 손가락이 바로 상산왕 주표다.

반면 주원공은 팔촌이나 떨어진 방계 황족.

직계 황족이 가진 정통성과 권위. 촌수로 따져도 주원공에게 있어 상산왕 주표는 까마득하게 높은 집안 어르신인 것이다.

‘이런 걸 이이제이(以夷制夷)라고 하는 거지.’

오랑캐는 오랑캐로 무찌르고, 약한 천룡인은 강한 천룡인으로 무찌르는 법.

내 열렬한 팬클럽 회장이 이 정도라니, 정말이지 생각할수록 가슴이 웅장해진다.

“뭐, 아무튼 그건 그렇다 치고. 동정호에는 가서 뭐 하시려고?”

“그, 그게. 날씨가 좋아서 뱃놀이를 좀…….”

어이없어하는 내 표정에 주원공이 황급히 말을 고쳤다.

“뱃놀이 겸, 요새 호북성의 분위기가 영 좋지 않다고 하니 민생을 살피려고 했소.”

“……그전에 본인 인생부터 살펴야 하지 않을까. 뒷구멍으로 한 재산 빼돌리다가 귀양 오신 거라며?”

“큼, 크흠!”

“그런데 사람들을 이렇게 잔뜩 끌어모아서 뱃놀이를 가? 그것도 이 시국에?”

호북성에 눈 있고 귀 달린 이들은 최근 끊이지 않는 흉흉한 소문에 불안에 떠는데, 귀양 온 황족이란 놈은 동정호에서 초호화 뱃놀이라니.

이시국 씨가 들었으면 오함마로 골통을 깨부숴도 할 말이 없다.

‘하여간에 있는 것들이란.’

고개를 절레절레 저은 나는 자리에서 일어났다.

적당히 잡음 없이 마무리되었으니 더는 신경 쓰지 않고 떠날 생각이었는데, 주원공의 눈에는 다르게 비친 모양이었다.

“자, 잠깐만. 어딜 가시는 거요?”

“동정호에 뱃놀이하러 가는 것보다는 바쁜 몸이라. 왜 그러시는데?”

“마음 상했다면 내 다시 한번 사과드리겠소. 그런 의미에서…….”

말꼬리를 흐린 주원공이 눈짓하자, 미리 준비하고 있던 청협방의 무인들이 행렬 사이사이 위치한 화려한 가마를 메고 왔다.

천을 걷지도 않았는데, 은은한 향기가 코끝을 파고든다.

‘이거 설마.’

옛말에 그런 속담이 있다. 설마가 사람 잡는다. 이번에도 마찬가지였다.

“모습을 보이거라.”

주원공의 말이 떨어지기가 무섭게 가마의 문이 스르륵 열렸다.

그리고 다음 순간, 조심스럽게 가마에서 내리는 한 여인의 모습에 나도 모르게 한 줄기 탄성이 입술을 비집고 흘러나왔다.

“……허.”

흔히들 연예인을 두고 예쁘다, 잘생겼다고들 말한다.

하지만 눈앞의 이 여인은, 그런 세간의 기준을 뛰어넘는 무엇인가가 있었다.

‘아름답다.’

그래, 아마도 이 표현이 가장 적당할 것이다.

여인은 그 정도로 아름다웠다. 이미 주원공의 속셈을 짐작했던 나조차도 감탄할 만큼.

궁기방이 황급히 침으로 세수를 하고, 혁무진이 넋을 놓을 만큼. 고기만두와 야채만두를 양손에 올려두고 고민하던 청풍이 만두를 모조리 떨어트릴 만큼 대단한 미모였다.

잔잔하게 흐르는 충격 속에서 주원공의 목소리가 들려왔다.

“본인이 곁에 두고 있는 가기(歌妓)요. 보시다시피 그 용모는 가히 천하절색이라 부를 만하고, 음율을 다루는 솜씨가 뛰어나 이 아이의 연주를 들으면 모두가 넋을 놓지.”

글쎄, 굳이 연주가 없어도 사람의 혼을 쏙 빼놓을 것 같은데.

숨길 수 없는 감탄이 드러난 내 표정에 피식 웃은 주원공이 여인에게 말했다.

“무엇 하느냐? 어서 인사 올리지 않고.”

붉은 입술이 천천히 열렸다.

“소녀, 홍란(紅蘭)이라 합니다. 귀인을 뵙게 되어 기쁘기 한량없습니다.”

“……오.”

“……와.”

“……이야.”

외모에 대한 충격이 가시기도 전에 곳곳에서 탄성이 튀어나온다. 정갈하게 맑으면서도 고혹적인 목소리.

홍란. 붉은 난초라는 이름이 누구보다 어울리는 여인이다.

‘물론 실제 이름도 다르고, 평범한 가기도 아니지만.’

홍란 역시 월화를 포함한 대부분의 기생들처럼 본명을 숨기고 있었다.

그리고 무공에 관해서는 일초 반식도 모르는 주원공과 달리, 미약하게나마 무공을 익힌 몸이기도 했다.

- 하오문?

내 전음에 가녀린 어깨가 움찔하더니, 이내 홍란의 고개가 살짝 끄덕여졌다.

‘하오문이라, 어쩐지 그럴 것 같더라니.’

개방 다음으로 많은 문도를 보유한 문파가 바로 하오문이다.

옆에 있는 주원공은 그 사실을 모르는 듯했지만, 다른 하오문의 기생들처럼 홍란 역시 제 한 몸을 지킬 만한 수준의 무공을 익혔다.

“자, 어떻소. 진 대협. 기회를 준다면 본 공자가 제대로 대접하리다. 물론 대협의 옆자리에는 홍란이가 앉을 것…….”

네가 이러고도 안 따라오나 보자. 득의양양하게 말하는 주원공의 얼굴에 그렇게 쓰여 있다. 홍란을 물끄러미 바라본 내가 웃으며 입을 열었다.

“됐고, 서로 가던 길이나 마저 갑시다.”

“그럼 다 함께 자리를 옮겨서, 응? 바, 방금 뭐라 하셨소?”

“뭘 그렇게 당황하신대. 분명히 바쁜 일이 있다고 말했던 것 같은데. 내가 기억력이 안 좋은 건가?”

“아, 아니. 그래도 홍란이가 있는데…….”

나는 손을 들어 주원공의 말을 가로막았다. 이미 쓸데없는 일에 휘말리는 바람에 시간을 소모했다. 내가 미인에 눈이 팔려 따라갈 놈이었다면, 지금까지 살아남지도 못했을 것이다.

“그쪽도 적당히 놀고. 집 들어가서 조용히 있는 게 좋을 거야. 그럼 이만.”

마지막 한 마디와 함께 몸을 돌리려던 그때, 주원공이 무언가를 내밀었다.

“잠깐! 그럼 이거라도.”

“……?”

“내 소문을 듣자 하니 상산왕 전하께서 진 대협에게 서명을 받았다고 들었소. 부디 내게도 같은 것을…….”

“……!”

조만간 팬카페가 잎새 2단계가 될 것 같다.
```

## Final English reading copy

```markdown
# Chapter 454

The young man who had been frozen with his eyes wide open—or rather, Ju Wongong—asked in a trembling voice,

“W-what did you say?”

Had this bastard’s ears been plugged since earlier? He kept making me repeat myself.

Ignoring the people staring back and forth between Ju Wongong and me with their mouths hanging open, I spoke again.

“Get down.”

“I-I am Ju Wongong!”

“Whether you’re the main character or Ju Wongong, get down.”

“Though you are ultimately a subject of the Great Nation, how dare you show such disrespect to me, a member of His Majesty the Emperor’s bloodline?”

“I have a friend named Johnson. If he were here, he would have violated something else.”

“……!”

“I’ll say it one last time. Get down.”

Though he had no idea what I meant, anyone could sense danger.

Ju Wongong’s butt twitched instinctively, and he slowly rose to his feet.

Yet even as his eyes darted about anxiously at a situation he had never experienced before, he did not forget to issue threats until the very end. Perhaps he trusted in his imperial background.

“D-do you think you’ll get away with this?”

“Yeah. I think I will.”

“To insult an imperial relative? This is treason!”

“As long as it’s not hair loss.”

“What kind of bastard says things like that…!”

Although I answered casually, I was not entirely wrong.

The imperial family possessed the same Zhu surname as the Son of Heaven and carried the blood of dragons. That alone made them noble.

Even though the Murim and the government maintained a relationship of mutual noninterference, disrespecting or threatening an imperial relative was treated as a serious crime.

That was why the Zhuge Clan retainer had been groaning like a dog that needed to relieve itself.

“P-perhaps it would be best if you stopped now.”

I frowned at the retainer’s whisper.

“Why?”

“Pardon?”

“What did I do? I didn’t swear at him, and I didn’t threaten to kill him. He even attacked first. All I did was tell him to get down from the four-person sedan chair.”

“……Well, that is true when you look at it that way. But he is an imperial relative.”

“Imperial relatives come in all grades. If he’s an eighth-degree relative, doesn’t that mean he isn’t really related by blood, but merely has a few drops of blood somewhere in common? If I spit into the Yangtze right now, the Yangtze and I would probably be about eighth-degree relatives.”

“Gasp. Great Hero Jin, please.”

“It’s all right. I spoke quietly, so no one could have heard us anyway.”

At that moment, Ju Wongong, who had misunderstood our whispering, shouted in a triumphant voice,

“It seems you have finally grasped the gravity of the situation. But it is already too late. The imperial court’s hundred thousand troops will soon be dispatched to exterminate the nine branches of your kin, along with all other traitors!”

“Oh. A Buster Call.”

“What have you been saying this whole time, you traitorous bastard?”

“Gasp!”

“Eek!”

When unmistakable fury appeared in Ju Wongong’s eyes, the commoners swallowed their breaths and prostrated themselves on the ground. Some had already begun fleeing in every direction.

They seemed intent on avoiding involvement in a needless incident. That meant fewer eyes watching us, so I had no complaints.

*They keep threatening people with the nine branches of their kin whenever they get bored.*

Did they not bother with anything less?

As I let out a deep sigh, the Zhuge Clan retainer whispered,

“Do not be too frightened. His talk of a hundred thousand troops is only a bluff.”

“……Do you think I’m an idiot? Why would I believe that?”

“Master Ju was exiled for embezzling a fortune while throwing around his imperial authority. He has no intention of escalating the matter. So please apologize and withdraw at an appropriate point.”

“Wait. Exiled?”

“Yes.”

“Him?”

“He is an imperial relative. No matter how distant his branch may be, his blood cannot be ignored. Besides, he is a distant branch with no chance of inheriting the throne, so even when he commits a crime, they allow him to enjoy a certain amount of special treatment.”

“In short, he’s such a fucking nobody that no one around him even bothers with him?”

“……Great Hero Jin, please choose your words more carefully.”

I let the retainer’s complaint go in one ear and out the other, then gave a quiet laugh.

I had wondered why someone who was supposedly an imperial relative was socializing with a gang of thugs on a main road in Hubei rather than staying in the imperial palace. He was even more insignificant than I had imagined.

Though I had already guessed as much when he started talking about being an eighth-degree relative.

“First, I shall gouge out those arrogant eyeballs of yours for failing to recognize this noble self, then tear you limb from limb, and afterward—”

“Yeah, yeah, I get it. Let’s talk about the rest after you look at this.”

I threw an object from inside my robe at Ju Wongong as he delivered his long speech.

At the same time, the man who had been puffing out his chest flailed both arms and sat down hard.

“It’s a hidden weapon! A hidden weapon! This bastard is attempting to assassinate an imperial relative!”

“……Your level is truly something else.”

And then.

The “hidden weapon” landed with a soft clack in front of Ju Wongong’s feet, scattering a brilliant light beneath everyone’s gaze.

“Huh?”

Ju Wongong stared at the object before his feet with a puzzled look, then opened his mouth blankly.

“Huh? Huh? Huhhhhhh?”

It did not take long for his question marks to become exclamation marks, or for his anger to turn into shock.

He looked back and forth between me and the token of Prince Shangshan Zhu Bao, engraved with clouds and a dragon. Then he spoke heavily.

“I shall show you mercy and forgive you.”

“……”

What a load of crap.

* * *

“So you were on your way to Dongting Lake?”

“That is correct! No, I mean, yes, that is so!”

Ju Wongong nodded energetically at my gentle voice.

The decorative showpieces from Qingxia Hall whom he had hired were keeping people quiet alongside the government troops, who had arrived late. Meanwhile, Cheongpung, who had somehow succeeded in buying dumplings in bulk, opened his eyes wide at the mention of Dongting Lake.

“Wow! Dongting Lake!”

Ju Wongong had finally learned the identity of this dumpling ghost. His uneasy gaze flicked toward the sword hanging at Cheongpung’s waist.

“W-well, I could invite you along if you wished…”

I muttered,

“You don’t mean that at all.”

“That is a misunderstanding! No, I mean, you misunderstand.”

“Do you often misunderstand things in your daily life? You attacked people who were trying to pass peacefully, so it would seem that way.”

“That was… I shall apologize once again. I never dreamed that you possessed His Highness Prince Shangshan’s token.”

“Oh, I see. If I hadn’t had the token, you would have brought a hundred thousand troops to exterminate my nine branches of kin, gouged out my eyes, and dismembered me?”

“W-why would you say such a thing? Ha, ha-ha-ha.”

His forced laughter was almost pitiful.

*I didn’t know the token would have this much power, either.*

There was a reason Ju Wongong was being so humble.

Even animals distinguished between purebred and mixed-breed. How much more would the imperial family—the most noble bloodline in the world—care about such distinctions?

Even though the same imperial blood ran in their veins, Prince Shangshan Zhu Bao was the Son of Heaven’s only younger full brother and the sole prince he had personally appointed.

After the late Emperor’s death, the ruthless Emperor eliminated countless blood relatives in the struggle for the throne. Prince Shangshan Zhu Bao was that ruthless Emperor’s one soft spot.

Ju Wongong, on the other hand, was an imperial relative from a branch eight degrees removed.

The direct imperial line possessed legitimacy and authority. Even by counting degrees of kinship, Prince Shangshan Zhu Bao was a distant and exalted elder of the household to Ju Wongong.

*This is what they call using barbarians to defeat barbarians.*

Defeat barbarians with barbarians, and defeat a weak Celestial Dragon with a strong Celestial Dragon.

The chairman of my fan club was this formidable. The more I thought about it, the more my chest swelled with pride.

“Well, putting that aside, what are you planning to do at Dongting Lake?”

“W-well, the weather is nice, so I thought I would take a boat ride…”

At the unimpressed expression on my face, Ju Wongong hurriedly corrected himself.

“I intended to take a boat ride while also checking on the people’s welfare, since I heard the mood in Hubei Province has been rather grim lately.”

“……Shouldn’t you inspect your own life first? I heard you were exiled for siphoning off a fortune through back channels.”

“Ahem! Ahem!”

“And you brought all these people along for a boat ride? In times like these?”

Everyone with eyes and ears in Hubei Province was trembling with anxiety because of the ominous rumors that had continued without pause. Meanwhile, an exiled imperial relative was planning a luxurious boat ride on Dongting Lake.

If Mr. Current Situation heard about this and smashed Ju Wongong’s skull with a sledgehammer, Ju Wongong would have no grounds to complain.

*That’s rich people for you.*

I shook my head and rose from my seat.

The matter had been settled without too much noise, so I intended to leave without giving it any more thought. But Ju Wongong seemed to see things differently.

“W-wait a moment. Where are you going?”

“I’m a busy man. Why would I go boating on Dongting Lake? What is it?”

“If I have offended you, I shall apologize once again. In that spirit…”

Ju Wongong trailed off and gave a meaningful glance.

The Qingxia Hall martial artists who had been waiting in advance came forward carrying several ornate sedan chairs positioned among the procession.

The cloth curtains had not even been lifted, yet a faint fragrance slipped into my nostrils.

*Don’t tell me…*

There is an old saying: the thing you say “surely not” about is the thing that gets you. This time was no different.

“Show yourself.”

The moment Ju Wongong finished speaking, the sedan chair’s door slowly opened.

And then, when a woman carefully stepped down from the sedan chair, a quiet exclamation escaped my lips before I could stop it.

“……Huh.”

People often describe celebrities as pretty or handsome.

But the woman before me possessed something beyond those ordinary standards.

*Beautiful.*

Yes. That was probably the most appropriate word.

The woman was beautiful enough to make even me gasp in admiration, despite having already guessed Ju Wongong’s intentions.

Beautiful enough for Gung Gibang to hurriedly wash his face with spit, for Hyuk Mujin to lose himself in a daze, and for Cheongpung—who had been holding a meat dumpling in one hand and a vegetable dumpling in the other while trying to decide between them—to drop every single dumpling.

Amid the quiet shock flowing through the crowd, Ju Wongong’s voice reached me.

“She is the singing courtesan I keep at my side. As you can see, her beauty is worthy of being called the most beautiful in the world. She is also skilled in music, and anyone who hears her play loses himself completely.”

I was not so sure. It seemed as though she could steal a person’s soul without playing a single note.

Ju Wongong gave a quiet laugh at the admiration that could not be hidden from my face, then spoke to the woman.

“What are you waiting for? Hurry and greet him.”

Her red lips slowly opened.

“This humble girl is Honglan. It is my greatest pleasure to meet such an honored guest.”

“……Oh.”

“……Wow.”

“……Amazing.”

Before the shock of her appearance had even faded, exclamations arose from every direction.

Her voice was clear and pure, yet alluring.

Honglan. A woman whose name, meaning red orchid, suited her better than anyone.

*Of course, it wasn’t her real name, and she wasn’t an ordinary singing courtesan, either.*

Like most courtesans, including Wolhwa, Honglan was hiding her real name.

And unlike Ju Wongong, who did not know even a single martial move or half a stance, she had learned a small amount of martial arts.

—Lower District Sect?

Her slender shoulder twitched at my Sound Transmission, and Honglan gave a slight nod.

*The Lower District Sect. I had a feeling that was the case.*

After the Beggars’ Sect, the Lower District Sect possessed more disciples than any other sect.

Ju Wongong beside me did not seem to know that, but like the other Lower District Sect courtesans, Honglan had learned enough martial arts to protect herself.

“So? What do you think, Great Hero Jin? If you give me the opportunity, this Young Master will treat you properly. Of course, Honglan will sit beside you…”

*Let’s see you refuse to come along after this.*

That was written plainly across Ju Wongong’s smug face.

I stared at Honglan for a moment, then smiled and spoke.

“Forget it. Let’s each continue on our way.”

“Then we can all move somewhere else together, hm? W-wait. What did you just say?”

“Why are you so flustered? I’m pretty sure I said I had something urgent to do. Is my memory failing me?”

“N-no. But Honglan is here…”

I raised a hand and cut Ju Wongong off.

I had already wasted time by getting dragged into something pointless. If I were the kind of man who would lose his head over a beautiful woman and follow her somewhere, I would not have survived this long.

“Don’t overdo the partying, either. You’d be better off going home and staying quiet. See you.”

I was about to turn away after that final remark when Ju Wongong held something out to me.

“Wait! Then at least take this.”

“……?”

“I heard that His Highness Prince Shangshan received your autograph, Great Hero Jin. Please give me one as well…”

“……!”

At this rate, my fan café would be reaching Leaf Level 2 soon.[^1]

[^1]: Korean online fan communities often use graded membership tiers named after stages of a leaf’s growth.
```

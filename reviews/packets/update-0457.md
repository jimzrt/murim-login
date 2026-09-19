<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0457.txt",
      "sha256": "56e634b93eb1fbcc7c569e57cad26c5b3cbd16567ac4b1958562848d9cbc229a",
      "bytes": 13207
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "0876a1db40c5931839c940a4d103d01987c4d42c2a2ffb76727d139a86a7ef0c",
      "bytes": 3530
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "211370e461eafa4a6f6c3341c672a3b51e5a301942d7ed6d2107b41eb18ba52b",
      "bytes": 149649
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "e5de8112ed03fc64aa589066a99172fadc928ea39c8784117f207df4f140ebc8",
      "bytes": 944
    },
    {
      "path": "characters/Gung Gibang.md",
      "sha256": "e5bd370153f6f0a7d508084a36bd2ccad0d557c6f23f604a4d54aa5629889e8b",
      "bytes": 662
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "52bd917820f94e7d351407a5251c09932210906857ec3b43f90e285b20231ddc",
      "bytes": 1108
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "132c3d01aef66ef872e37a750dff4fc8a3b4f5c3c607d40a62a26ee0de77b9b3",
      "bytes": 1574
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "5921944a887b9482edf7afb8cb4f8d7371b5aecd8397e104eb4072f44d225103",
      "bytes": 622
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "1d7107a8fccbd7f22fc575f87ee5c27e0f5f94254f8deee40b1e0f78feb0b44d",
      "bytes": 144359
    }
  ],
  "estimated_tokens": 10463
}
-->

# Durable State Update — Chapter 457

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 457. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 457. Profile updates may replace only one
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
  "chapter": 457,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 457,
    "continuity_sources": [457],
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
    "The Sea Serpent Society and three Yangtze River Channel League strongholds, including Donghu Stronghold, were destroyed, with more than a thousand casualties, while the perpetrators' whereabouts remain unknown.",
    "The Dongting Fisherman is believed to remain in Hubei Province and is suspected of being a Dark Heaven member involved in the Hubei atrocities.",
    "Wudang is responding to an unidentified killer demon responsible for more than thirty deaths, including twenty pilgrims on Mount Wudang.",
    "The Skeleton King's undead identity remains concealed, and Taekyung has ordered him to join Peace Guild under a prepared contract.",
    "Go Jun is expected to succeed Lee Jungryong as Ares Guild's captain and is searching China for Lee's holographic recorder.",
    "Taekyung's party has left the Zhuge Clan for Dongting Lake, reached Wuhan, and heard that a boat has sunk in Dongting Lake.",
    "The captured Three Fiends is a former-generation great fiend and Supreme Peak Dark Heaven subordinate whom Taekyung is transporting alive to investigate possible codes or markings.",
    "Qingxia Hall is an influential Hubei social club formed by powerful families' children, and Ju Wongong is its exiled young master who defers to Prince Shangshan while Honglan conceals her real name.",
    "Beggars' Sect, Lower District Sect, and Zhuge Clan intelligence are searching for the people responsible for the Hubei massacres."
  ],
  "continuity_sources": [
    456,
    455
  ],
  "open_questions": [
    "What are the origin and purpose of the symbols shared by the Arch Lich's magic circle and Dark Heaven's formations?",
    "Who destroyed Donghu Stronghold and the related Yangtze River Channel League strongholds, why was no Moving Formation trace left, and was the destruction a diversion?",
    "Is the Dongting Fisherman a member of Dark Heaven, what role did he play in the Hubei atrocities, and who sank the boat in Dongting Lake?",
    "Is the killer demon attacking Wudang connected to Dark Heaven?",
    "What evidence is contained in Lee Jungryong's holographic recorder, and what are the terms of the Peace Guild–Wizard Guild agreement?"
  ],
  "safe_through": 456,
  "temporary_decisions": [
    "Render 황철 as Hwang Cheol, 도립군 as Do Ripgun, 광수도귀 as Mad Water Saber Demon, 파랑호 as Wave Fox, 동정호 as Dongting Lake, and 사천혈사 as Sichuan Blood Tragedy.",
    "Render 살귀 as killer demon, 일급 낭인 as First Rate wandering martial artist, 삼괴 as Three Fiends, 대마두 as great fiend, and 마군 as Demon Lord.",
    "Render 시부럴 as “sibu-leol,” 시벌좌 as “Lord Fuck,” and 시부럴좌 as “Lord Sibu-leol.”",
    "Preserve the Skeleton King's grandiose, mock-offended voice and Taekyung's dry, profane humor.",
    "Render 주원공 as Ju Wongong, 대죽산표국 as Daejuksan Escort Bureau, 형문검가 as Hyungmun Sword Family, 응성상회 as Eungseong Merchant Association, 천룡인 as Celestial Dragon, 사인교 as four-person sedan chair, 홍란 as Honglan, 가기 as singing courtesan, and 구족 as the nine branches of kin."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 혁무진    | **Hyuk Mujin**     |
| 청풍     | **Cheongpung**     |
| 절정     | **Peak**          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 살기     | **killing intent**                               |                                                       |
| 기녀     | **courtesan**                                    |                                                       |
| 은인     | **Benefactor**                               |
| 시스템              | **System**                     |
| 퀘스트              | **Quest**                      |
| 보상               | **Reward**                     |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 궁기방 | **Gung Gibang** | Beggars' Sect Successor Beggar and finalist. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 천무지체 | **Heavenly Martial Physique** | Named physique or constitution mentioned hypothetically by Jin Mukyung. |
| 기감 | **Qi Sense** | Taekyung's sensory technique; its range reaches seventy meters in this chapter. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 일각 | **fifteen minutes** | Quarter of a shichen; used for the remaining completion time. |
| 동정호 | **Dongting Lake** | Lake under which Dangyang and Honghu Strongholds operated. |

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
| 혁무진 | 궁기방 | squad_companion_to_Beggars_Sect_successor | Young Hero Gung | formal-polite, then pointed | Uses 궁 소협 while asking about the culprit and challenging Gung’s insults. |
| 궁기방 | 혁무진 | squad_companions | you; that lunatic | insulting-casual | Gung Gibang mocks Hyuk Mujin's injuries and calls him a lunatic for attacking the Third Fiend. |
| 궁기방 | 청풍 | martial_companions | Young Hero Cheongpung | formal-polite | Gung Gibang uses 청 소협 while asking why Cheongpung is at the temporary clinic. |

## Listed compact profiles

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 456
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, the grandson and Disciple of Sword Saint Mae Jonghak, and a Supreme Peak martial master known as the Huashan Divine Dragon.
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, a deep love of martial arts, and a martial artist's competitive pride; he becomes unsettled when someone copies his martial arts
- **Voice:** Dreamy and hazy, with innocent, polite phrasing
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions while Taekyung is his only true martial rival; Tang Sadok has temporarily entrusted Mimi to him.

### Gung Gibang.md

# Gung Gibang (궁기방)

- **Safe through:** Chapter 456
- **Aliases:** Successor Beggar, Beggar Prince, pure-blooded beggar, ultimate beggar
- **Role:** Gung Gibang is the Beggars' Sect Successor Beggar and a unique eight-knot disciple.
- **Personality:** Vulgar, aggressive, and quick-tempered.
- **Voice:** Blunt, profane, and vividly threatening.
- **Relationships:** Gung Gibang is a rival finalist alongside Baek Woo and Zhuge Gyun who trades insults with Taekyung and uses Beggars’ Sect intelligence to investigate Tang Taesang’s murder and search for Dark Heaven’s Hubei forces.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 456
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers and Vice Squad Leader of the Jin Dragon Squad.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 455
- **Aliases:** Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, a Supreme Peak master who has manifested Force, opened his Middle Dantian, crossed the wall into true mastery, can perceive the texture of qi well enough to sever layered magic, and is publicly recognized as an S-rank-level Hunter while formally retaining an A-rank license pending testing.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate, student, and trusted manager of media and official arrangements, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, and Xiao Shen regards him as an older brother after Jin saved him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 455
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

## Korean source

```text
＃457화



“동정호! 동정호에서 배가 침몰했다!”

“도, 도와주시오! 사람들이 물에 빠졌소!”

댕, 대앵-!

저 멀리에서 들려온 비명 같은 외침과 함께, 날카로운 경종(警鐘) 소리가 어둠 너머에서 울려 퍼졌다.

하지만 그보다 한발 먼저 내 귓가를 파고든 소리가 있었다.

띠링.

‘이건…….’

익숙한 알림. 서늘한 불길함이 등골을 훑어내린다. 나는 눈앞에 떠오른 반투명한 시스템 창을 바라보았다.



- 돌발 퀘스트, [동정호의 비극]이 생성되었습니다!

- 당신은 퀘스트를 거절할 수 없습니다!



퀘스트



[동정호의 비극]



동정호(洞庭湖)는 천하에서도 손꼽히는 명승지입니다.

시인 묵객들은 익양루에 올라 아름다운 경관을 즐기며 풍월을 읊고, 권세와 재물이 있는 자들은 크고 화려한 놀잇배를 띄워 며칠 밤낮을 즐깁니다.

그러나 오늘, 이 맑고 푸르른 호수는 부서진 배의 잔해와 시신들로 가득합니다.

누군가가 나서지 않는다면, 아직 살아 있는 이들 역시 같은 운명을 맞이하게 될 것입니다!



등급 : 절정

제한 : 진태경

임무 : 인명 구조 (미완료)

보상 : ???

실패 : 사람들의 죽음

* 이미 상당한 시간이 흐른 상황. 더 늦기 전에 사람들을 구조해야 합니다!





퀘스트 창의 마지막 줄을 모두 읽어 내렸을 때, 작은 홀로그램 창이 허공에 떠올랐다.



제한 시간 : 45분 36초



빌어먹을. 한 시간도 되지 않는다니.

‘조금이라도 지체했다가는…… 모두가 죽는다.’

어쩌다가 이런 참사가 벌어졌는지 생각할 겨를조차 없다. 일 분, 어쩌면 일 초에 한 사람의 목숨이 달려 있을지도 모른다.

단전의 공력을 최대한으로 끌어올린 내가 입을 열었다.

“지금부터 죽을힘을 다해 동정호까지 달려. 사람들부터 구한다.”

쉬이이이익!

대답은 없었다. 딱딱하게 굳은 얼굴들과 더욱 빨라진 속도만이 있을 뿐.

그렇게 저 멀리서부터 울려 퍼지는 외침과 경종을 나침반 삼아, 우리는 달리고 또 달렸다.

그리고 제한 시간의 앞자리가 4에서 2로 바뀌었을 무렵. 우리는 비로소 볼 수 있었다.

화륵, 콰아아아아!

너른 강물 위에서 화마에 휩싸인 채 타오르는 수십 척의 크고 작은 선박과 사방에서 울려 퍼지는 수많은 외침을.

“배를 가져오시오! 나룻배라도 좋으니 어서!”

“사공이 부족합니다!”

“더! 사람들을 더 불러와라! 이 지경이 되었는데도 군선은 대체 어디에서 무엇을 하는 것이냐!”

“아아, 아아아!”

한 걸음, 한 걸음씩 가까워질수록 눈앞의 광경이 일목요연하게 드러난다.

동정호의 강가에서 쉴 새 없이 뛰어다니는 백여 명의 사람들과 느리게 나아가는 작은 나룻배 몇 척.

‘저 정도로는 안 돼.’

그들로서는 필사적인 노력이겠지만, 구해야 하는 인명의 숫자에 비해서는 턱없이 부족하다.

초인이라 부르기에 손색없는 무공을 지닌 나조차도 현장을 본 순간 숨이 턱하고 막힐 정도였다.

‘어떻게 구해야 하지?’

동정호가 크다는 사실은 익히 들어 알고 있었지만, 막상 눈으로 확인하니 그 면적은 예상을 훌쩍 뛰어넘었다.

이만큼 넓은 강에 선박이 다닥다닥 붙어 있을 리가 있나. 떨어진 거리를 봐서는 선박마다 최소 수백 장의 거리를 두고 놀고 있었음이 틀림없었다.

당장 눈에 보이는 것만 이 정도니, 보이지 않는 곳에서는 얼마나 많은 배와 사람들이 물에 잠겨 있을까.

‘빌어먹을.’

입술을 질끈 깨문 나는 속도를 더욱 높였다.

흡사 바람처럼 내달리는 우리의 모습을 발견한 사람들의 웅성거림이 커졌다.

그중 관부 소속으로 보이는 군관 하나가 다급하게 외쳤다.

“무, 무림인이십니까? 제발 부탁이니 도와…….”

“긴말 필요 없고. 배 좀 빌립시다.”

“예?”

나는 얼빠진 얼굴로 되묻는 군관을 뒤로하고 벼락처럼 외쳤다.

“궁기방, 혁무진. 나룻배를 부숴라!”

쐐애애애액!

두 사람의 움직임에는 어떠한 의문이나 망설임도 존재하지 않았다.

내 양옆을 스쳐 지나가며 쏘아진 궁기방과 혁무진이 힘찬 기합성과 함께 장력과 검을 흩뿌렸다.

서걱, 콰과광!

사람들에 의해 다급히 옮겨지던 나룻배 두 척이 수백 개의 나뭇조각으로 변한 것은 순식간이었다.

뭐라 할 새도 없이 벌어진 일에 순간 넋이 나갔던 군관이 비명처럼 외쳤다.

“이, 이게 무슨 짓이오!”

뒤를 이어 경악에 찬 외침들이 곳곳에서 튀어나왔다.

“나, 나룻배가……!”

“저놈들이 이 사달을 일으킨 흉수요! 사람들을 구하지 못하게 만드는 것이 틀림없소!”

충격과 분노가 빠르게 전염된다. 사방에서 쏟아지는 온갖 욕설과 살기 어린 시선들. 하지만 나는 신경 쓰지 않았다.

아니, 신경 쓸 틈이 없었다고 해야 옳았다.



제한 시간 : 28분 52초



이제 남은 시간은 고작 30분 남짓.

지금 같은 행동에 대한 이유를 설명해 봤자 희생자만 늘어날 뿐이다.

그리고 천만다행으로, 이 자리에는 내 의도를 이해하고 행동으로 옮길 수 있는 세 명의 무림인이 있었다.

“청풍, 궁기방!”

“알았다!”

“네, 은인!”

내 외침이 의미하는 바를 깨달은 궁기방과 청풍이 나룻배의 파편을 집어 들었다. 그리고 어둠에 잠긴 동정호를 향해 힘차게 흩뿌렸다.

쉬쉬쉬쉭, 촤악!

어둠을 가르며 날아간 수십 개의 나무 파편이 동정호 곳곳에 떨어진다.

“저, 저런!”

“이건 설마…….”

이제야 내 의도를 알아챈 몇몇 사람이 눈을 크게 떴지만, 저 정도 개수로는 부족하다.

어쩌면 우리의 발이 닿기 전 가라앉을지도 모르는 일이다.

그렇다면…….

‘직접 길을 만들며 가는 수밖에.’

빠른 판단과 동시에, 나는 힘차게 발을 굴렀다.

쿠웅!

강가에 쌓여 있던 모래와 먼지가 일거에 솟구치자 미처 대비하지 못한 사람들이 기침을 토해 냈다.

모두의 시야가 가려진 바로 그때를 틈타, 나는 손을 뻗었다.

그리고 축축하고 단단한 목재의 촉감과 함께 오직 나만이 사용할 수 있는 명령어를 외쳤다.

‘인벤토리 수납.’

띠링. 띠링. 띠링.



- [나룻배의 파편]이 인벤토리에 보관되었습니다!

- [나룻배의 파편]이 인벤토리에…….



귓가를 파고드는 알림과 더불어 허공에 녹아드는 것처럼 사라지는 나무 조각들.

사람들의 의심을 피할 정도의 적당량만을 남겨 둔 내가 힘있게 외쳤다.

“청풍과 궁기방은 나와 함께, 혁무진은 남아서 배와 사람을 모은다!”

“조, 존명(遵命)!”

아까부터 숨이 턱에 차 있던 혁무진이 외침을 쥐어 짜낸 그때, 나와 청풍, 그리고 궁기방의 신형은 이미 컴컴한 동정호를 향해 쏘아지고 있었다.

쏴아아악!

아랫배에서 솟구친 뜨거운 열기가 다리를 향해 내려간다.

천무지체(天武肢體)라고 오인될 만큼 완벽한 근육과 탄력을 지닌 신체에 고강한 공력이 깃들었다.

‘바로 지금!’

꽈앙!

발끝으로부터 터져 나온 거대한 충격파가 지면을 누르고 출렁이던 강물을 밀어 냈다. 모래와 자갈이 가루가 되어 흩날리고, 서늘한 바람이 전신을 스쳤다.

손을 뻗으면 밤하늘에 총총히 박혀 있는 별을 잡아챌 수 있을 것 같았다.

하지만 그것도 잠시뿐.

도약 뒤에는 추락이 있는 법이다.

후우우웅!

거세게 출렁이는 검은 강물이 빠르게 가까워진다.

그리고 야생 동물과 같은 안력(眼力)은 반쯤 잠겨 들어간 나뭇조각을 발견하기에 아무런 부족함도 없었다.

툭. 투웅!

착지는 가벼웠고, 뒤를 이은 두 번째 도약은 무거웠다.

나와 청풍, 궁기방은 재차 몸을 날렸다.

미리 뿌려 둔 나룻배의 파편을 디딤돌 삼아 한 번. 그리고 두 번, 세 번…….

그와 같은 행동을 몇 번이나 반복하고 나서야, 비로소 멀게만 느껴졌던 선박이 육안으로도 또렷하게 구분할 수 있을 만큼 가까워졌다.

하지만 좁혀지는 거리와 함께 마음속의 불길함 역시 커가고 있었다.

‘생기가…… 느껴지지 않는다.’

살아 있다면 응당 있어야 할 생존자들의 비명도, 움직임도 느껴지지 않았다.

그리고 내가 느낀 불길함이 현실로 나타나는 데에는 그리 오랜 시간이 걸리지 않았다.

타닥.

이미 선체 대부분이 물에 잠긴 선박 위.

뱃머리에 발을 디딘 궁기방과 청풍이 신음처럼 중얼거렸다.

“이건.”

“……은인.”

두 사람의 목소리가 수백 장 밖에서 들려오는 것처럼 희미하게 들려온다.

그 숨 막히는 적막 속에서, 나는 멍하니 주위를 둘러보았다.

내 시선이 닿는 곳마다 강물 위로 떠 올라 있는 무수한 시신과 부서진 선박의 잔해가 스친다.

죽었다. 모두가 죽었다.

화려한 비단을 걸친, 상인으로 보이는 배불뚝이 사내. 비쩍 마른 초라한 행색의 수부(水夫). 흥을 돋우기 위해 불려온 듯한 악공과 기녀들까지.

당장 눈에 보이는 숫자만 어림잡아도 수백이다.

이 검은 강물 위에는 흥겨운 풍악도, 사람들의 웃음도 존재하지 않는다.

남은 것은 파괴와 죽음. 그리고 망자들의 얼굴에 뚜렷이 새겨진 공포뿐이다.

‘어떻게 이런 일이.’

순간 머릿속이 텅 비어 버린 듯했다.

나는 홀린 듯이 파편을 밟으며 강물 위를 누볐다. 한 사람의 생존자라도 더 찾기 위해 [기감]을 아낌없이 사용했다.

하지만…….

삐빅.



- [기감]이 실패했습니다.

- 범위 내에서 원하는 대상의 기운을 감지하지 못했습니다.



시스템은 그 어느 때보다 냉정했다.

반투명한 홀로그램 창과 거슬리는 실패 알림음으로 주위의 생존자가 전무(全無)하다는 것을 알려 주었다.

“……도대체 이게 무슨.”

참담한 심정으로 뇌까리던 그때, 문득 뇌리를 번개처럼 스치는 생각이 있었다.

‘잠깐, 시스템?’

나는 황급히 고개를 들어 허공을 바라보았다.

아직도 사라지지 않은 반투명한 홀로그램 창이 시선에 닿았다.



제한 시간 : 9분 43초



“……!”

무언가로 뒤통수를 강하게 얻어맞은 기분이다.

정말 생존자가 없다면 퀘스트가 취소되거나, 실패했다는 알림이 떴어야 했다. 시스템은 그 어떤 것보다 빠르고 직관적이니까.

하지만 퀘스트는 여전히 진행 중이었고 제한 시간을 알리는 시스템 창 역시 사라지지 않았다.

이것이 의미하는 것은 한 가지뿐이다.

순간 딱딱하게 굳어 버린 내게, 궁기방이 조심스러운 목소리로 말을 건넸다.

“안타깝지만 더 이상 생존자를 찾는 건 무의미해 보…….”

“있어. 생존자.”

“뭐?”

“보이지 않을 뿐이야. 이곳보다 훨씬 더 먼 어딘가에 생존자가 있어. 분명히.”

뭔가 말하려던 궁기방이 확신에 찬 내 표정에 얼굴을 굳혔다. 청풍 역시 평소와 다른 진중한 목소리로 입을 열었다.

“만약 은인의 말씀이 맞다면…….”

“찾아서 구해 내야지. 무슨 수를 써서라도.”

나를 물끄러미 바라보던 궁기방이 고개를 끄덕였다.

“흩어져야겠군. 주위에 가라앉은 배를 뜯어서 이용한다면 반 시진 정도는 더 가능할지도 몰라.”

“앞으로 일각이야. 두 사람 모두 그 안에 최대한 멀리까지 찾아보고, 생존자를 발견하지 못한다면 돌아와.”

제한 시간이 의미하는 바는 곧 생존자에게 남은 시간. 그 이상 수색은 무의미하다.

이상할 만큼 단호한 내 말투에 두 사람이 의아한 기색을 내비쳤지만, 이내 별말 없이 수긍했다.

“그러도록 하지.”

“일각. 명심할게요, 은인.”

“그럼 지금부터 각자의 방향으로 흩어진다. 잠시 후에 보자.”

텅, 쐐애애액!

말을 끝마친 나는 뱃머리를 박차고 도약했다.

시시각각 줄어드는 제한 시간을 바라보며 모든 공력과 감각을 최고조로 끌어올린 채 망망대해와도 같은 동정호를 달리고, 또 달렸다.



제한 시간 : 1분 12초



‘늦은 건가.’

그리고 모든 것을 포기하려던 그 순간.

“사, 살려 주…….”

아주 작고 희미한, 누군가의 목소리가 귓가에 닿았다.
```

## Final English reading copy

```markdown
# Chapter 457

“Dongting Lake! A boat has sunk in Dongting Lake!”

“P-please, help us! People have fallen into the water!”

*Clang, clang—!*

Along with the scream-like shouts rising in the distance, the sharp sound of an alarm bell rang out from beyond the darkness.

But another sound had reached my ears a moment earlier.

*Ding.*

*This is…*

A familiar notification.

A chill of foreboding ran down my spine. I stared at the translucent System window floating before my eyes.

> **System**
>
> - An unexpected Quest, **The Tragedy of Dongting Lake**, has been generated!
> - You cannot refuse the Quest!
>
> **Quest**
>
> **The Tragedy of Dongting Lake**
>
> Dongting Lake is one of the most scenic places under heaven.
>
> Poets and men of letters climb Yiyang Tower to enjoy the beautiful scenery and compose verses about nature, while those blessed with power and wealth set large, splendid pleasure boats afloat and spend days and nights enjoying themselves.
>
> But today, this clear, blue-green lake is filled with the wreckage of shattered boats and corpses.
>
> If someone does not step forward, those who are still alive will meet the same fate!
>
> **Grade:** Peak
>
> **Restriction:** Jin Taekyung
>
> **Mission:** Rescue people (Incomplete)
>
> **Reward:** ???
>
> **Failure:** The deaths of the people
>
> *A considerable amount of time has already passed. You must rescue the people before it is too late!*

When I finished reading the final line of the Quest window, a small holographic window appeared in the air.

> **System**
>
> **Time Limit:** 45 minutes 36 seconds

Damn it. Less than an hour.

*If we waste even a little time… everyone will die.*

There was not even time to wonder how such a catastrophe had happened. A single life might depend on every minute—or even every second.

I drew as much internal energy as possible from my dantian and opened my mouth.

“Run to Dongting Lake with everything you have from this moment on. We save the people first.”

*Whoosh!*

No one answered. There were only rigid faces and an even faster pace.

Using the cries and alarm bells rolling in from the distance as our compass, we ran and ran.

And when the first digit of the time limit changed from four to two, we were finally able to see it.

*Fwoom, kwoooosh!*

Dozens of large and small vessels burned across the broad waters, engulfed in flames, while countless shouts rang out from every direction.

“Bring boats! Even a ferry will do, so hurry!”

“We don’t have enough boatmen!”

“More! Bring more people! How can the warships still be nowhere to be seen when things have come to this?”

“Ahhh! Ahhh!”

With every step closer, the scene before us came into sharper focus.

More than a hundred people ran nonstop along the shore of Dongting Lake, while several small ferries moved slowly across the water.

*That won’t be enough.*

They were making a desperate effort, but it was woefully inadequate for the number of people who needed rescuing.

Even I, whose martial arts were more than worthy of being called superhuman, felt my breath catch the moment I saw the scene.

*How are we supposed to rescue them?*

I had heard many times that Dongting Lake was enormous, but seeing it with my own eyes, its size far exceeded my expectations.

There was no way the vessels would be packed close together on such a vast lake. Judging from the distances between them, every ship must have been out enjoying itself at least several hundred zhang from the others.[^1]

And this was only what I could see immediately. How many more boats and people were submerged beyond my sight?

*Damn it.*

I bit down hard on my lip and increased my speed.

The murmurs of the people who noticed us racing toward them like the wind grew louder.

One military officer, who appeared to belong to the authorities, shouted urgently,

“A-are you martial artists? Please, help—”

“No time for explanations. We’re borrowing some boats.”

“Pardon?”

I left the dumbfounded officer behind and shouted like thunder.

“Gung Gibang, Hyuk Mujin! Smash the ferries!”

*Whoosh!*

There was no hesitation or doubt in either man’s movements.

Gung Gibang and Hyuk Mujin shot past my sides, shouting as they sent palm force and sword strokes flying.

*Slash, boom!*

The two ferries being hurriedly moved by the people were transformed into hundreds of pieces of wood in an instant.

The military officer, momentarily stunned by what had happened before he could even say anything, screamed,

“What in the world are you doing!”

Shocked cries erupted from every direction.

“T-the ferries…!”

“Those bastards are the villains who caused this disaster! They must be trying to keep us from rescuing the people!”

Shock and anger spread rapidly. All manner of curses poured in from every side, along with gazes brimming with killing intent.

But I did not care.

No—saying I had no time to care would have been more accurate.

> **System**
>
> **Time Limit:** 28 minutes 52 seconds

There were barely thirty minutes left.

Even if I explained why I had done what I did, it would only lead to more casualties.

And fortunately, three martial artists were present who could understand my intentions and put them into action.

“Cheongpung, Gung Gibang!”

“Got it!”

“Yes, Benefactor!”

Gung Gibang and Cheongpung understood what my shout meant. They picked up the ferry fragments and hurled them with all their strength toward Dongting Lake, which lay shrouded in darkness.

*Whoosh, splash!*

Dozens of pieces of wood flew through the darkness and fell across the lake.

“W-what!”

“Could this be…?”

Several people finally realized my intentions and widened their eyes, but that number of fragments was not enough.

They might sink before we could even reach them.

In that case…

*We have no choice but to make a path ourselves.*

The moment I made the decision, I stamped down hard.

*Boom!*

The sand and dust piled along the shore surged into the air all at once, making the unprepared people cough.

Taking advantage of the moment when everyone’s vision was obscured, I reached out.

Along with the damp, hard feel of the wood, I called out the command only I could use.

*Inventory: Store.*

*Ding. Ding. Ding.*

> **System**
>
> - **Ferry Fragment** has been stored in your Inventory!
> - **Ferry Fragment** has been stored in your Inventory…

The notifications pierced my ears as the pieces of wood vanished into the air as if dissolving into it.

I left behind only enough fragments to avoid arousing suspicion, then shouted forcefully,

“Cheongpung and Gung Gibang, come with me. Hyuk Mujin, stay here and gather boats and people!”

“Y-yes, sir!”

Just as Hyuk Mujin, who had been gasping for breath since earlier, squeezed the words out, the figures of Cheongpung, Gung Gibang, and me had already shot toward the darkened Dongting Lake.

*Whoosh!*

Hot energy surged from my lower abdomen and flowed down toward my legs.

Powerful internal energy filled a body with such perfect muscles and elasticity that it could have been mistaken for a Heavenly Martial Physique.

*Now!*

*Boom!*

A massive shock wave burst from my toes, pressed down against the ground, and shoved back the rippling water. Sand and gravel scattered as dust, while a cool wind swept across my entire body.

If I reached out, I felt as though I could pluck the stars scattered across the night sky from the heavens.

But that lasted only a moment.

Every leap was followed by a fall.

*Whoooosh!*

The black water, surging violently, rushed toward us.

And my vision, keen as a wild animal’s, had no trouble spotting the pieces of wood half-submerged in the water.

*Tap. Thump!*

My landing was light, but the second leap that followed was heavy.

Cheongpung, Gung Gibang, and I launched ourselves forward again.

We used the ferry fragments we had scattered in advance as stepping stones—once, then twice, three times…

Only after repeating the process several more times did the vessel that had seemed so far away finally draw close enough to distinguish clearly with the naked eye.

But as the distance closed, the foreboding in my heart grew as well.

*I can’t feel any life force.*

There were no screams or movements from survivors—nothing that should have been there if they were alive.

And it did not take long for the foreboding I felt to become reality.

*Tap.*

On the vessel, most of whose hull was already submerged, Gung Gibang and Cheongpung landed on the bow and muttered like men groaning in pain.

“This is…”

“…Benefactor.”

Their voices sounded faint, as though they were coming from hundreds of zhang away.

In that suffocating silence, I looked around blankly.

Everywhere my gaze fell, countless corpses floated on the water alongside the wreckage of shattered ships.

They were dead.

Everyone was dead.

A potbellied man who appeared to be a merchant, dressed in splendid silk. A gaunt, shabby-looking boatman. Musicians and courtesans who seemed to have been hired to liven up the festivities.

Even the number immediately visible to me was easily in the hundreds.

There was no lively music or laughter on the black water.

All that remained was destruction and death—and the fear plainly etched across the faces of the dead.

*How could this have happened?*

For a moment, my mind seemed to go completely blank.

As if possessed, I walked across the water by stepping on the fragments. I used Qi Sense without holding anything back, searching for even one more survivor.

But…

*Beep.*

> **System**
>
> - **Qi Sense** has failed.
> - The qi of the desired target could not be detected within range.

The System was more merciless than ever.

The translucent holographic window and grating failure notification told me that there was not a single survivor nearby.

“What in the world…”

I muttered in despair when a thought suddenly flashed through my mind like lightning.

*Wait. The System?*

I hurriedly raised my head and stared into the air.

The translucent holographic window was still there.

> **System**
>
> **Time Limit:** 9 minutes 43 seconds

“……!”

It felt as though someone had struck me hard in the back of the head.

If there truly were no survivors, the Quest should have been canceled or a failure notification should have appeared. The System was faster and more direct than anything.

But the Quest was still in progress, and the System window displaying the time limit had not disappeared.

There could be only one meaning.

As I stood there, frozen stiff, Gung Gibang spoke to me in a cautious voice.

“Unfortunately, it seems pointless to keep searching for survivors…”

“There are survivors.”

“What?”

“We just can’t see them. There are survivors somewhere much farther away than this. I know it.”

Gung Gibang had been about to say something, but his expression hardened when he saw the certainty on my face.

Cheongpung spoke as well, his voice more serious than usual.

“If what Benefactor says is true…”

“Then we find them and save them. No matter what it takes.”

Gung Gibang stared at me for a moment, then nodded.

“We’ll have to split up. If we tear apart the sunken boats around here and use them, we might be able to keep going for another half a shichen.[^2]”

“You have fifteen minutes from now. Both of you search as far as you can within that time. If you don’t find any survivors, come back.”

The time limit meant the amount of time remaining for the survivors. Searching beyond that point would be meaningless.

The unusual firmness of my tone made the two of them look puzzled, but they soon nodded without another word.

“We’ll do that.”

“Fifteen minutes. I’ll remember, Benefactor.”

“Then split up in your respective directions now. See you shortly.”

*Thump, whoosh!*

When I finished speaking, I kicked off from the bow and leaped.

As I watched the time limit shrink by the second, I pushed all my internal energy and senses to their peak and ran and ran across Dongting Lake, vast as an open sea.

> **System**
>
> **Time Limit:** 1 minute 12 seconds

*Am I too late?*

And just as I was about to give up on everything—

“P-please, save me…”

A tiny, faint voice reached my ears.

[^1]: A **zhang** is a traditional Chinese unit of distance, roughly 3.3 meters.

[^2]: A **shichen** is a traditional time unit of roughly two hours.
```

<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0402.txt",
      "sha256": "4a8a69208b19c55b6efbf1ef77e91e432b0ed487aaaf5f6b442860a5986f62a1",
      "bytes": 13692
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "6633b9b24b273c59d08c38504e2f2223b75b8096b24331fb887432f453cb25d3",
      "bytes": 1709
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "1c37814ef5658d9022f66b3b32127bb21705dc26d6967091945cae0f256c3753",
      "bytes": 135760
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "a65c75bcf500ab9b11e139ae9a06d227e55589ecdfbe5475e2c535ffcb640012",
      "bytes": 533
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "ab6dfde6b0ea84f6f4c111d59edb8e2f9b3f83de81a00ffd4147037363132375",
      "bytes": 1212
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "a057669a9aa12e2c25a0d733bb3dd48a423fe0fa054065d4259e81213e1b5c56",
      "bytes": 622
    },
    {
      "path": "characters/Lei Fei.md",
      "sha256": "956a80d6a32d76efb6a08cd63ef0ec6ee499251424e106cd0fd01a0c0609d4d0",
      "bytes": 866
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "486e259149e9e064de2dc060343871404409ffe5ce427d77bb9bb7dd90417624",
      "bytes": 117494
    }
  ],
  "estimated_tokens": 9441
}
-->

# Durable State Update — Chapter 402

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 402. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 402. Profile updates may replace only one
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
  "chapter": 402,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 402,
    "continuity_sources": [402],
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
    "The black knight is confirmed to be Lei Fei, the missing Chinese S-rank Hunter.",
    "Lei Fei was raised by Wei Fenghu, whom he regards as both uncle and father, and his human memories include an unnamed wife and daughter.",
    "Lei Fei is now a level-140 undead Death Knight Lord and supreme commander of the legion of the dead.",
    "Lei Fei serves an unidentified lord and was corrupted by the Arch Lich.",
    "Lei Fei can imitate Jin's martial arts, including the Flame Divine Palm, but his copied techniques remain imperfect.",
    "Jin's Fire Dragon Armor has lost durability during the battle.",
    "Jin has pierced Lei Fei's chest with White Flame using Seizing an Object Through Empty Space.",
    "Lei Fei's condition after being pierced remains unresolved."
  ],
  "continuity_sources": [
    401,
    400
  ],
  "open_questions": [
    "Who is Lei Fei's lord, what is the lord's origin, and how does the lord relate to the Arch Lich's objective?",
    "Can Lei Fei resist the word-spell and retain or recover his human identity?",
    "What happened to Lei Fei's wife and daughter during the Gaoping District Monster Wave?",
    "What is Lei Fei's condition after Jin pierces his chest with White Flame?",
    "What happened to the Second Fiend assigned to the Qingcheng attack?"
  ],
  "safe_through": 401,
  "temporary_decisions": [
    "Render 나이트메어 as Nightmare.",
    "Use black knight for 검은 기사 and keep it distinct from Death Knight and Death Knight Lord.",
    "Render 언령 as word-spell.",
    "Render 중화 육성 훈련 as Zhonghua Development Training.",
    "Preserve Jin's blunt, profane combat voice."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 제자     | **Disciple**                                 |
| 시스템              | **System**                     |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 레이드     | **raid**              |
| 대격변     | **Great Cataclysm**   |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 레이페이 | **Lei Fei** | Concealed Chinese S-rank Hunter and head of the Public Security Armed Forces Department in Sichuan Province. |
| 기감 | **Qi Sense** | Taekyung's sensory technique; its range reaches seventy meters in this chapter. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 오우거 | **ogre** | B-rank monster species emerging from the Gate. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 와이번 | **Wyvern** | High-tier dragonkin monster. |
| 트롤 | **Troll** | Monster species with extraordinary regenerative ability. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 오성홍기 | **Five-Starred Red Flag** | China's national flag. |
| 겁화 | **hellfire** | Destructive fire energy used by Taekyung. |
| 오성 | **Oseong** | One half of the paired Joseon-era names used in Taekyung's joke. |
| 가고일 | **Gargoyle** | Flying monster species accompanying the Wyverns. |
| 데스나이트 | **Death Knight** | Undead commander type serving under the Black Knight. |
| 공안무력부 | **Public Security Armed Forces Department** | Chinese security organization ordered to assemble during the attack. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 데스나이트 | 인간 | enemy combatants | human | contemptuous and commanding | Used in the Death Knight's warnings to Jin. |
| 데스나이트 | 로드 | subordinate to commanding lord | Lord | fearful and deferential | The Death Knight calls to the Death Knight Lord after Jin overwhelms the army. |
| 진태경 | 레이페이 | former ally and fellow Hunter | Lei Fei | blunt and solemn | Jin addresses Lei Fei by name before telling him to rest. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 401
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who has sworn never to kill again.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 400
- **Aliases:** Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, and a Supreme Peak master who has manifested Force and crossed the wall into true mastery.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother; Jeok Cheongang is his Master; Cheongpung is his trusted companion and only true martial rival; Choi Minwoo is his subordinate and student; his mother and sister Hayeon are among those he protects.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 400
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Lei Fei.md

# Lei Fei (레이페이)

- **Safe through:** Chapter 401
- **Aliases:** None
- **Role:** Lei Fei is a concealed Chinese S-rank Hunter and former head of the Public Security Armed Forces Department in Sichuan Province who now exists as a level-140 undead Death Knight Lord and supreme commander of the legion of the dead.
- **Personality:** Lei Fei's recovered memories show him as dutiful, honorable, family-oriented, and willing to serve as an unseen guardian.
- **Voice:** His human voice is formal and earnest, becoming warm and playful with family.
- **Relationships:** Wei Fenghu is his maternal uncle who raised him as a son; Lei Fei married an unnamed flower-shop owner and had a daughter, trained alongside Wu Heixing, and now serves an unidentified lord after the Arch Lich corrupted him.

## Korean source

```text
＃402화



푸욱!

이건 무엇인가.

뜨겁고, 시원했다.

두 가지 상반된 감각을 느끼며, 검은 기사는 가슴팍을 뚫고 튀어나온 투명한 창날을 내려다보았다.

천천히 고개를 든 그의 시선이 알 수 없는 표정을 한 젊은 인간에게 닿았다.

“이제 그만…… 쉬어라.”

목소리에 담긴 감정은 패자에 대한 조롱도, 승자가 갖는 기쁨도 아니었다. 씁쓸했고, 한편으로는 아련했다.

그 한마디가 검은 기사의 뇌리를 가득 채웠다.

‘쉬어라.’

그리고 다음 순간.

콰창!

검은 기사는 자신을 옭아매고 있던 모든 것이 깨어져 나가는 소리를 들었다.

간신히 형태를 유지하고 있던 칠흑색 갑주가 수백, 수천 개의 조각으로 깨져나가고 강대하던 마력이 휘청였다.

하지만 그중 가장 큰 변화는 그의 정신에서 일어나고 있었다.

‘저건…….’

느려진 세상 속, 흩어지는 갑옷의 파편 사이로 보이는 낡고 자그마한 아이의 신발.

동시에 뇌리를 스치는 수많은 기억들.

‘저, 헌터가 되고 싶어요.’

자신의 꿈을 말하던 어린 소년.

‘네가 자랑스럽구나. 훌륭히 자라주어 고맙다.’

‘감사합니다. 외삼촌. 아니…… 아버지.’

자랑스러운 조카이자 아들이 된 청년.

‘계십니까?’

‘어서 오세요!’

‘……아.’

향기와 온도, 날씨. 모든 것이 좋았던 그 날, 한 여자를 만나 사랑에 빠진 사내.

‘나랑 결혼해 줄래?’

헌터가 되고 싶던 어린 소년은 누군가의 반려자가 되었고.

‘응애, 응애애!’

‘이, 이 아이가…….’

‘아빠가 된 걸 축하해. 여보.’

마침내 한 아이의 아버지가 되었다.

‘압바, 어무아!’

‘으하하! 그래! 우리가 네 아빠고 엄마다!’

어떻게 잊을 수 있을까, 이 세상 누구보다 행복했던 그 순간들을.

핏기가 사라진 창백한 피부 위로 한줄기 눈물이 흘러내렸다.

머릿속을 가득 메웠던 먹구름을 지워 낸 눈물. 마침내 스스로를 기억해 낸 망자(亡子)의 눈물이었다.

‘아, 아아…….’

이제야 알았다. 이제야 알겠다.

그는 손을 뻗어 자그마한 신발을 붙잡았다.

부모의 품에 안겨 울음을 터트리던 이름 모를 아이와 자신이 죽던 그 날 아침에도 활짝 웃으며 배웅해 주던 딸의 모습이 겹쳐졌다.

‘압빠! 빨리 와!’

‘잘 다녀와요. 조심하고.’

아내의 이마에 키스하고, 아이의 볼에 얼굴을 비볐던 것 같다. 수염이 까칠하다며 깔깔 웃는 딸을 안아 주고 현관을 나섰더랬다.

평소와 같은 한마디를 남긴 채.

‘그럼 다녀올게.’

하지만 그 약속은 지켜지지 못했다.

몇 시간 후, 대격변 이후 유례없던 재앙이 시작되었고 그는 혼신의 힘을 다해 싸웠다. 그리고 마침내 한 존재와 마주했다.

‘고결하구나. 인간이여. 이름이 무엇이냐.’

‘나는…….’

붉게 타오르던 안광이 씻은 듯이 사그라들었다.

뿌옇게 물든 회백색 눈동자를 가진 그는 더 이상 검은 기사도, 데스나이트 로드도 아니었다.

‘레이페이. 그게 내 이름이다.’

길었던 어둠에서 벗어난 그가 고개를 들었다.

구름 사이로 비치는 노을빛이 창백한 피부를 불그스름하게 물들였다.



* * *



난데없이 시스템 알림이 울린 것은, 종지부를 찍기 위해 손을 뻗은 바로 그 순간이었다.

띠링.



- 해당 대상에 관한 정보가 변경되었습니다.

- 변경된 정보를 [기감]으로 표시합니다.



[Lv.120 레이페이]



“……!”

예상치 못한 상황에 덜컥 움직임이 멈췄다.

하늘을 바라보던 데스나이트 로드, 아니 레이페이의 회백색 눈동자가 천천히 움직여 나를 향한다. 입술 사이로 흘러나오는 목소리는 공허하고 쓸쓸했다.

「한바탕 악몽을 꾼 것 같아. 아니, 차라리 악몽이었으면 좋겠군.」

이런 현상은 지금껏 듣도 보도 못했다. 말없이 그를 바라보던 나는 입을 열었다.

“정신이 돌아온 겁니까?”

「그래, 이제야 겨우.」

레이페이는 자신의 두 손을 내려다보았다. 창백하고, 부패했다. 나와의 치열한 공방 끝에 살과 뼈가 떨어져 나간 부분도 있었다.

그리고 붉은 핏물에 젖어 있었다. 다름 아닌 인간의 피다.

「내가, 무슨 짓을 한 거지?」

인간을 위해 목숨을 내던졌던 자신이, 몬스터 군단의 사령관이 되어 인간을 학살했다.

그 참담한 현실을 깨달은 그가 어떤 심정일지 감히 짐작할 수 없었다.

“레이페이.”

말해 주고 싶었다. 그건 당신의 의지가 아니었다고. 아크 리치의 마법이 당신의 정신을 사로잡았기 때문이었다고.

그러나 레이페이는 고개를 저었다.

「말하지 않아도 괜찮네. 자네가 무슨 말을 하려 하는지는 이미 알고 있으니. 하지만…….」

레이페이는 자신의 몸뚱어리를 가리키며 말을 이었다.

「지금 내게 허락된 시간은 그리 많지 않은 것 같군.」

그의 말은 전부 사실이었다. 강철과 탄환으로도 뚫을 수 없던 강인한 언데드의 육신은 조금씩, 아주 조금씩 붕괴해 가고 있었다.

또한 역설적이게도, 지금의 레이페이를 지탱하고 있는 것은 아직까지도 그의 몸에 남아 있는 마력이었다.

「우스운 일이지. 언데드가 되어 인간을 죽인 주제에, 그 힘으로 버티고 있다니.」

공허하게 뇌까린 그가 나를 향해 입을 열었다.

「한 가지만 부탁해도 되겠나?」

“……말씀하십시오.”

나는 레이페이가 소멸을 원한다고 생각했다. 고통스러운 모든 것들에서 벗어나 안식하길 소망할 것이라 여겼다.

하지만 다음 순간 레이페이의 입술 사이로 흘러나온 말은 내 예상을 벗어나는 것이었다.

「내 사명을 다할 수 있도록 도와주게.」

“……!”

「헌터가 되던 날 맹세했지. 목숨이 다하는 그 순간까지 몬스터와 싸우겠노라고. 그날의 맹세는 아직 유효하네.」

레이페이는 이미 사명을 다했다. 용맹하게 달려 나갔고, 찬란하게 부서졌다.

데스나이트 로드가 되어 인간과 싸운 것은 아크 리치의 의지였지, 그의 뜻이 아니었다.

그럼에도 불구하고, 지금의 그는 다시 싸우려 한다. 목숨이 다했음에도 다시 한번 자신의 사명을 되새기며 우뚝 서 있다.

그렇기에 나는 묻지 않을 수 없었다.

“왜, 어째서 이렇게까지 하는 겁니까?”

내 물음에, 레이페이가 희미하게 웃었다.

「바보 같은 질문이야.」

“네?”

「수많은 몬스터와 위험이 기다리고 있음에도 자네가 홀로 달려온 이유. 그리고 내가 마지막까지 싸우려 하는 이유. 뭐가 다르지?」

“……!”

「자네는 이미 답을 알고 있어. 그뿐일세.」

답을 알고 있다.

그 한마디를 듣는 순간, 등줄기를 타고 전율이 흐른다.

말문이 막힌 나를 바라본 레이페이가 손을 들어 주위를 가리켰다.

이미 생명이 빠져나간 두 눈동자에, 아직 남아 있는 수많은 몬스터 대군이 비쳤다.

「이것이…… 내 마지막 전투가 되겠군.」

푸푹!

스스로 자신의 가슴에 박혀 있던 백염(白炎)을 뽑아 내게 건넨 그가 검을 치켜세웠다.

S급 헌터를 상징하는 눈부신 오러 블레이드 대신, 불길한 어둠을 띤 마력이 검신을 휘감으며 솟구쳤다.

그러나 그 힘을 사용하는 자는 데스나이트 로드가 아니라, 마지막 사명을 불태우고 있는 어느 헌터다.

「함께 싸우고 싶군. 하지만 그들이 허락해 줄까?」

모르는 사람이 들었다면 뜬금없는 헛소리로 치부했을 것이다.

하지만 나는 레이페이의 말을 이해했고, 백염의 창날을 비스듬히 내리깔며 대답했다.

“오히려 기뻐할 겁니다. 제가 아는 그 사람들이라면.”

「……내 생각과 같군.」

회백색 눈동자에 붉은 기운이 일렁였다.

온 힘을 다해 끌어낸 마력이, 전장 곳곳으로 스며들었다. 레이페이의 입술 사이로 천둥 같은 외침이 터져 나왔다.

「공안무력부(公安武力部)-!」

그리고 다음 순간.

스슥, 투두두둑.

데스나이트 로드, 아니 공안무력부장의 부름에 전장에 몸을 뉘었던 수백의 헌터들이 몸을 일으켰다. 죽음을 딛고 부활한 그들이 각자의 병장기를 움켜잡고 한 자리에 집결한다.

그들의 꼭짓점에, 나와 레이페이가 있었다.

「자네가 앞장서게. 이 싸움은 산 자가 끝내야 해.」

나는 뭔가 홀린 듯이 앞으로 나섰다.

예기치 못한 상황에 당황하던 몬스터 군단이 비로소 흉성(凶聲)을 토해 내며 모여들었다.

이제는 적이 되어 버린 사령관을 향해.

그리고 선두에 선 나를 향해.

저벅. 저벅.

나는 느리지만 힘차게 걸음을 옮겼고.

탁, 타닥.

서서히 속도를 더했다.

레이페이와 언데드로 부활한 수백의 공안무력부 헌터가 내 뒤를 따랐다.

찰랑거리던 잔물결이 파도가 되어 놈들을 덮치기까지는, 그리 오랜 시간이 걸리지 않았다.

그리고 마지막이 될 전투의 입구에서, 레이페이는 목청껏 외쳤다.

「모조리 쓸어 버려라!」

영상 속에서 울려 퍼졌던 그 외침.

부서지고 더럽혀진 갑옷 위, 그들의 상징이자 자부심인 오성홍기가 노을빛을 받아 빛난다.

욱신거리는 가슴을 안고, 나는 빛살이 되어 몬스터들을 향해 쏘아졌다.

쐐애애애액! 콰드드득!



* * *



퍼걱!

지금까지 내가 얼마나 쓰러트렸을까.

수백? 일 천?

서걱! 퍼벙!

모르겠다. 나는 무언가에 사로잡힌 사람처럼 계속해서 나아갔다. 막아서는 모든 것들을 박살 내고, 베고, 찌르고 터트렸다.

화르르륵!

- 쿠아아아악!

- 크아아아!

푸른 겁화가 기둥이 되어 솟구치고, 꺼지지 않는 불길에 휩싸인 몬스터들이 비명을 지른다.

그리고 이내 아무것도 들리지 않게 되었을 때, 나는 문득 제자리에 멈춰섰다.

“헉, 허억.”

숨이 가쁘다. 모래를 한 움큼 씹어 삼킨 것처럼 입안이 텁텁했다.

나는 잠시 잊고 있었던 피로가 몰려드는 것을 느끼며 주위를 둘러봤다.

넓은 대지 위, 서 있는 몬스터는 더 이상 존재하지 않았다.

흉성을 토해 내던 오우거와 트롤도, 허공을 배회하던 와이번과 가고일도.

그리고…….

투둑, 털썩!

언데드로 부활한 공안무력부 헌터들도.

마지막 사명을 다한 그들은 마치 실이 끊긴 인형처럼 차례차례 쓰러졌다.

형용할 수 없는 감정으로 그 모습을 바라보던 나는 그것이 한 가지 사실을 의미한다는 것을 깨달았다.

“……레이페이!”

그는 고요한 전장의 한복판에 앉아 있었다. 한쪽 팔이 잘려 나가고, 옆구리가 뜯겨 나갔는데도 평온한 얼굴로 나를 기다리고 있었다.

「때맞춰 왔군.」

어째서일까, 별것 아닌 그 한마디에 가슴속에서 뭔가 울컥했다.

십 년을 알았던 사람도 아닌데, 나도 모르게 욕이 튀어나왔다.

“빌어먹을…….”

「욕 너무 많이 하지 말게. TV에서 보니 입버릇 같던데, 그러면 여자한테 인기 없어. 애들 교육에도 안 좋지.」

레이페이가 피식 웃으며 말했다. 그는 이미 내가 누구인지 알고 있었다.

“지금 그딴 게 문젭니까? 뭔가 방법이…….”

- 그런 방법은 없다. 간악한 인간.

평소와는 다른, 깊게 가라앉은 목소리의 주인은 스켈레톤 워로드였다.

그를 바라본 레이페이가 눈을 크게 떴다.

「몬스터?」

- 나는 사령관이다. 멍청하지만 조금 대단한 인간.

「몬스터로군. 도대체 어떻게 된 상황인지는 모르겠지만…… 그래, 진태경 자네라면 어련히 알아서 잘하겠지.」

고개를 끄덕인 레이페이는 고개를 들어 하늘을 바라보았다. 천천히 깜빡이는 회백색 눈동자에 온통 붉게 물든 하늘이 비쳤다.

「한 마디만 전해 줄 수 있을까?」

누구에게, 라는 멍청한 질문은 꺼내지 않았다. 그 대상이 누구인지는 이미 알고 있으니까.

「사랑한다고 전해줘. 그리고 돌아가지 못해서 미안하다는 말도.」

망자가 되어 가족에게 남기는 마지막 유언이다.

나는 울렁이는 가슴을 느끼며 대답했다.

“……그렇게 하겠습니다.”

「고맙네. 자네는 좋은 사람이야.」

레이페이는 희미하게 웃으며 하나뿐인 손으로 내 어깨를 두드렸다.

퍼석, 메마른 소리와 함께 손가락이 가루가 되어 부서진다. 그리고 이내 팔이, 다리가, 가슴이…….

마지막 순간, 그의 입술 사이로 한 마디가 흘러나왔다.

「서쪽으로 가게. 이 전쟁을 끝내 줘.」

휘이이잉.

바람이 불었다. 한 움큼의 가루로 변한 영웅이 허공으로 흩날렸다.

멍하니 그 광경을 바라보는 내 시야에, 편대를 지어 날아오는 수십 대의 비행기가 보였다.
```

## Final English reading copy

```markdown
# Chapter 402

Thrust!

*What is this?*

It was hot, yet cool.

Sensing those two contradictory sensations, the black knight looked down at the transparent spearhead protruding through his chest.

He slowly raised his head. His gaze met that of a young human wearing an unreadable expression.

“Enough now…… rest.”

The emotion in the voice was neither mockery toward a defeated opponent nor the joy of a victor. It was bitter—and, in a way, wistful.

That one sentence filled the black knight’s mind.

*Rest.*

And then, in the next moment—

Crack!

The black knight heard the sound of everything binding him shattering apart.

The jet-black armor that had barely maintained its shape broke into hundreds, thousands of fragments, and the mighty mana within him staggered.

But the greatest change was taking place inside his mind.

*That’s……*

In a world that had slowed to a crawl, he saw a small, worn child’s shoe through the fragments of armor scattering around him.

At the same time, countless memories flashed through his mind.

*“I want to become a Hunter.”*

A young boy speaking of his dream.

*“I’m proud of you. Thank you for growing up so well.”*

*“Thank you, Uncle. No…… Father.”*

A young man who had become both a proud nephew and a son.

*“Is anyone there?”*

*“Welcome!”*

*……Ah.*

On a day when everything had been perfect—the scent, the temperature, the weather—a man met a woman and fell in love.

*“Will you marry me?”*

The young boy who had wanted to become a Hunter became someone’s husband.

*“Waaah, waaah!”*

*“T-This child……”*

*“Congratulations on becoming a father, honey.”*

At last, he became the father of a child.

*“Dada, Momma!”*

*“Hahaha! That’s right! We’re your daddy and mommy!”*

How could he ever forget those moments, when he had been happier than anyone else in the world?

A single tear rolled down his bloodless, pale cheek.

It was a tear that wiped away the dark clouds filling his mind. The tear of a dead man who had finally remembered himself.

*Ah…… ahhh……*

Only now did he know. Only now did he understand.

He reached out and grabbed the small shoe.

The unknown child crying in its parents’ arms overlapped with the image of his daughter, smiling brightly as she saw him off on the morning he died.

*“Daddy! Come back soon!”*

*“Have a safe trip. Be careful.”*

He thought he had kissed his wife on the forehead and rubbed his face against his daughter’s cheek. He had hugged his daughter as she laughed and complained that his beard was scratchy, then left through the front door.

Leaving behind the same words he always did.

*“I’ll be back.”*

But that promise was never kept.

A few hours later, a disaster unlike any seen since the Great Cataclysm began, and he fought with every ounce of strength he possessed. At last, he encountered a certain being.

*“How noble. Human, what is your name?”*

*“I am……”*

The red glow burning in his eyes faded as if it had been washed away.

The man with cloudy, gray-white eyes was no longer the black knight, nor the Death Knight Lord.

*“Lei Fei. That is my name.”*

Freed from his long darkness, he raised his head.

The glow of the setting sun shining through the clouds cast a reddish hue over his pale skin.

* * *

The System notification rang out at the exact moment I reached out to deliver the final blow.

Ding.

> **System**
>
> - Information about the target has changed.
> - The changed information is displayed through **Qi Sense**.
>
> **Lv. 120 Lei Fei**

“……!”

My movement abruptly stopped at the unexpected development.

The gray-white eyes of the Death Knight Lord—or rather, Lei Fei—who had been staring up at the sky slowly turned toward me. The voice escaping between his lips was hollow and lonely.

“It feels like I’ve just had a terrible nightmare. No, I almost wish it had been a nightmare.”

I had never heard of or seen anything like this before. I stared at him in silence for a moment, then opened my mouth.

“Have you come back to your senses?”

“Yes. Only now, at last.”

Lei Fei looked down at his own hands. They were pale and rotten. Some of his flesh and bone had fallen away during his fierce exchange with me.

And they were soaked in red blood. Human blood.

“What have I done?”

The man who had once thrown away his life for humanity had become the commander of a monster army and slaughtered humans.

I could not even begin to imagine how he felt after realizing that terrible truth.

“Lei Fei.”

I wanted to tell him. *It wasn’t your will. It happened because the Arch Lich’s magic had seized control of your mind.*

But Lei Fei shook his head.

“You don’t have to say it. I already know what you’re trying to tell me. But……”

Lei Fei gestured toward his own body and continued.

“I don’t think I have much time left.”

Everything he said was true. The sturdy body of the undead, which neither steel nor bullets could pierce, was slowly—very slowly—falling apart.

And, paradoxically, what was sustaining Lei Fei now was the mana that still remained within his body.

“It’s ridiculous. I became an undead and killed humans, yet I’m clinging to existence with that very power.”

After muttering hollowly, he spoke to me.

“May I ask one favor?”

“……Please, go ahead.”

I thought Lei Fei wanted to disappear. I assumed he wished to find rest and escape from everything that had caused him pain.

But the words that slipped from his lips in the next moment were completely different from what I expected.

“Help me fulfill my mission.”

“……!”

“I swore an oath on the day I became a Hunter. I swore that I would fight monsters until the moment my life ended. That oath is still valid.”

Lei Fei had already fulfilled his mission. He had charged forward bravely and shattered magnificently.

The one who had fought humanity after becoming a Death Knight Lord had been acting on the Arch Lich’s will, not his own.

And yet, even now, he wanted to fight again. Though his life had already ended, he stood tall once more, reaffirming his mission.

That was why I could not help asking.

“Why? Why go this far?”

At my question, Lei Fei smiled faintly.

“What a foolish question.”

“What?”

“Why did you come running here alone, even though countless monsters and dangers were waiting for you? And why am I trying to fight until the very end? What’s the difference?”

“……!”

“You already know the answer. That is all.”

I knew the answer.

The moment I heard those words, a shiver ran down my spine.

Lei Fei looked at me, unable to speak, then raised his hand and gestured around us.

The countless monster troops that still remained were reflected in his eyes, which had already lost the light of life.

“This…… will be my final battle.”

Schlk!

Lei Fei pulled White Flame from his own chest and handed it to me, then raised his sword.

Instead of the dazzling aura blade symbolizing an S-rank Hunter, ominous dark mana coiled around the blade and surged upward.

But the one wielding that power was not the Death Knight Lord.

It was a Hunter burning through his final mission.

“I’d like to fight together. But will they allow me?”

Anyone who heard those words without knowing the circumstances would have dismissed them as random nonsense.

But I understood Lei Fei. Angling the spearhead of White Flame downward, I answered.

“They’ll be happy. If they’re the people I know.”

“……You think the same way I do.”

A red light flickered in Lei Fei’s gray-white eyes.

The mana he had dragged forth with all his strength seeped across the battlefield. Then a thunderous cry burst from his lips.

“Public Security Armed Forces Department—!”

And in the next moment—

Rustle. Rattle, rattle.

At the call of the Death Knight Lord—or rather, the head of the Public Security Armed Forces Department—the hundreds of Hunters who had fallen across the battlefield rose to their feet. They had returned from death as undead, and now they gripped their weapons and gathered in one place.

At their apex stood Lei Fei and me.

“You take the lead. The living must finish this fight.”

As if bewitched, I stepped forward.

The monster army, which had been thrown into confusion by the unexpected turn of events, finally gathered together, spewing hostile cries.

Toward the commander who had now become their enemy.

And toward me, standing at the front.

Step. Step.

I walked slowly but firmly.

Tap. Tap-tap.

Then I gradually picked up speed.

Lei Fei and the hundreds of Public Security Armed Forces Department Hunters resurrected as undead followed behind me.

It did not take long for the ripples spreading across the water to become waves and crash over them.

And at the entrance to what would be our final battle, Lei Fei shouted at the top of his lungs.

“Wipe them all out!”

That was the cry that had echoed through the footage.

On their battered, filthy armor, the Five-Starred Red Flag—their symbol and pride—shone in the glow of the setting sun.

Clutching my throbbing chest, I shot toward the monsters like a ray of light.

Whoooooosh! KRA-DOOM!

* * *

Crunch!

How many had I brought down by now?

Hundreds? A thousand?

Slash! Boom!

I had no idea. Like someone possessed, I kept moving forward. I smashed, cut, stabbed, and blew apart everything that stood in my way.

Whoooooosh!

—Kuaaaargh!

—Kraaah!

Blue hellfire surged upward like pillars, and monsters engulfed in flames that would not go out screamed.

Then, when nothing could be heard anymore, I suddenly stopped where I stood.

“Hah, huff.”

I was out of breath. My mouth felt rough and dry, as if I had chewed and swallowed a handful of sand.

Feeling the fatigue I had momentarily forgotten come crashing back over me, I looked around.

Across the wide expanse of land, there were no monsters left standing.

Not the ogres and Trolls that had spewed their hostile cries, nor the Wyverns and Gargoyles that had circled through the air.

And……

Thud. Collapse!

Not even the Public Security Armed Forces Department Hunters who had been resurrected as undead.

Having fulfilled their final mission, they fell one after another like puppets whose strings had been cut.

As I stared at them with indescribable emotions, I realized what their collapse meant.

“……Lei Fei!”

He was sitting in the middle of the silent battlefield. One arm had been severed, and his side had been torn open, yet he waited for me with a peaceful expression.

“You came at just the right time.”

I did not know why, but that insignificant sentence made something surge up inside my chest.

I had not known him for ten years, yet a curse slipped from my lips before I could stop it.

“Damn it……”

“Don’t swear so much. I saw you on television, and it seems to be a habit. Women won’t like that, and it’s not good for children’s education.”

Lei Fei gave a quiet laugh as he spoke. He already knew who I was.

“Is that really the problem right now? There has to be some way……”

—There is no such way, you treacherous human.

The owner of the voice, much deeper and more subdued than usual, was the Skeleton Warlord.

Lei Fei looked at him with wide eyes.

“A monster?”

—I am the commander. You are a foolish but somewhat remarkable human.

“You are a monster, then. I have no idea what’s going on, but…… yes, if you’re Jin Taekyung, I’m sure you’ll handle it somehow.”

Lei Fei nodded, then raised his head toward the sky. His slowly blinking gray-white eyes reflected a sky stained entirely red.

“Could you pass along one message?”

I did not ask the foolish question of *to whom?* I already knew who he meant.

“Tell them I love them. And tell them I’m sorry I couldn’t return.”

It was the final message a dead man left for his family.

Feeling my chest churn, I answered.

“……I will.”

“Thank you. You’re a good person.”

Lei Fei smiled faintly and tapped my shoulder with his one remaining hand.

With a dry, crumbling sound, his fingers broke apart into dust. Soon, his arm, his leg, his chest……

At the very end, a single sentence slipped between his lips.

“Go west. End this war.”

Whoooooosh.

The wind blew. The hero who had turned into a handful of dust scattered through the air.

I stared blankly at the sight. Then I saw dozens of aircraft flying toward us in formation.
```

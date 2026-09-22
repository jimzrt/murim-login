<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0696.txt",
      "sha256": "8f5bb09fe533b79dfeb8d3e2524d21f6b8a701ae056b58fe2516aa239a595bf0",
      "bytes": 12483
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "e17130083dae11846dcc9285db61616e5245c44b21dddf571d4f72f4d72ca9f5",
      "bytes": 1618
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "0fa0ce441bd7946bb616710f6f9fe8a15bb991f8a20474364f6e85f49dd22728",
      "bytes": 205252
    },
    {
      "path": "characters/Baeksang.md",
      "sha256": "cdf9feba8af7154da644ac1cf1fb8540a2c2af0f8ea6c8f3852f195cc3cce199",
      "bytes": 887
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "8f6e8ed126a5ab273d5a54e35f98bab2f3863069c2c46c56dd940968b2c19c7d",
      "bytes": 553
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "7cb9a38737bd18f13c3fee6f7ebfc276d1f3fb7949bcffb49416467fc88c070e",
      "bytes": 1851
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "42ecae9963af648f61cd4310b7ef9fb4b021a4c6fa994fbb573c6f0c86f999f4",
      "bytes": 622
    },
    {
      "path": "characters/Muyaho.md",
      "sha256": "63014d99ca36fcaa426041394fd7b9ea9f3f23f997a78f0c9e9cff74bea9a19c",
      "bytes": 687
    },
    {
      "path": "characters/White Tiger.md",
      "sha256": "bfffd4fbea75be22c581095cc8486886c3affe113f7e233c65301fa71fec00db",
      "bytes": 585
    },
    {
      "path": "characters/Yohi.md",
      "sha256": "85bb77b93452136c260a0309c65f9b953b604b0569ded2b74d2fb278f0f300f9",
      "bytes": 594
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "d54cdb4cc857d508054a1fa5c64e8f88f017bf36c3bc4e306e8f98602313a5a3",
      "bytes": 214419
    }
  ],
  "estimated_tokens": 9868
}
-->

# Durable State Update — Chapter 696

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 696. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 696. Profile updates may replace only one
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
  "chapter": 696,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 696,
    "continuity_sources": [696],
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
    "Nanman Beast Palace is on the verge of civil war, with nearly ten thousand warriors gathered in the Inner Palace.",
    "Five tribal chieftains have left the Outer Palace in support of former Palace Lord Yayul Cheok.",
    "Jin Taekyung and Yohi have returned to the Nanman Beast Palace with the guardian spirit and a vast beast army.",
    "Dark Heaven's scheme has not yet begun at the time Jin reaches the North Gate.",
    "The White Tiger is the guardian spirit of the sacred stone and has regained its silver-white form.",
    "The sacred stone is held in the guardian spirit's mouth and can emit a pillar of light visible from far away.",
    "Jin has split the Nanman Beast Palace's iron gate with blue-white Force.",
    "The beast army has begun its assault, starting the Great War that will decide Nanman's fate."
  ],
  "continuity_sources": [
    695
  ],
  "open_questions": [
    "What will happen inside the Nanman Beast Palace as Jin's group and the beast army advance?",
    "What effect will the sacred stone's pillar of light have on Nanman and the battlefield?",
    "Will Dark Heaven's Rift or another part of its scheme be triggered after Jin's arrival?",
    "Who or what awaits beyond the iron gate, possibly including the Lord of Heaven?"
  ],
  "safe_through": 695,
  "temporary_decisions": [
    "Use Whitey for Jin's nickname 흰둥아.",
    "Use civil war for 내전 and fighting spirit for 전의.",
    "Use the quoted paraphrase “Do everything in your power, then leave the result to Heaven and wait” for 진인사대천명."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 암천     | **Dark Heaven**                  |
| 남만야수궁  | **Nanman Beast Palace**          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 일격     | **One Strike**                         |
| 백상 | **Baeksang** | Great chieftain of the Bai people and Yayul Cheok's sworn younger brother. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 무야호 | **Muyaho** | Yayul Mok's White Tiger's name; it means tiger of the mighty wilds. |
| 백호 | **White Tiger** | Yayul Mok's tiger companion. |
| 요희 | **Yohi** | Female great chieftain of the Yao people. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 박도 | **broad-bladed saber** | Rough weapon swung by the bald swordsman. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 계인 | **Buddhist precept seals** | Seals carved into the foreheads of Shaolin martial monks. |
| 도산검림 | **a mountain of sabers and a forest of swords** | Idiom describing the lethal life of martial artists. |
| 내궁 | **Inner Palace** | The inner compound of the Nanman Beast Palace. |
| 외궁 | **Outer Palace** | The outer compound of the Nanman Beast Palace. |
| 대회의 | **Tribal Grand Council** | Nanman's council of great chieftains. |
| 대족장 | **Great Chieftain** | Title used for the senior Nanman leader who supposedly ordered the inspection. |
| 요서부 | **Western Yao Estate** | Estate inherited by Yohi when she became a Great Chieftain. |
| 궁주 | **Palace Lord** | Title Yohi uses after realizing that Heugung is the Beast Miao King. |
| 수호령 | **guardian spirit** | Ancient title for the Black Tiger. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 요희 | 진태경 | Yao great chieftain to Murim Alliance pavilion master | Jin Taekyung | casual and probing | Identifies him by his full name while allowing him to keep the mask on. |
| 진태경 | 요희 | Fire Dragon Pavilion pavilion master to Yao great chieftain | you | guarded and blunt | Answers Yohi's probing questions directly while warning her about Ju Hwaran. |
| 백상 | 요희 | Bai great chieftain to Yao great chieftain | Yohi | cold and formal | Calls to Yohi from outside the tent at the chapter's end. |
| 백상 | 진태경 | Nanman great chieftain to Murim Alliance Pavilion Head | you bastard | cold, hostile, and contemptuous | Baeksang calls Jin a Han Chinese man, rejects his status, and orders him to leave. |
| 진태경 | 백상 | Murim Alliance Pavilion Head to Nanman great chieftain | you | polite but deliberately provocative | Jin tells Baeksang that Nanman's blood was shed for the world rather than merely for the Central Plains. |
| 진태경 | 백호 | human ally to intelligent spiritual beast | you | casual and familiar | Converses with White Tiger after interpreting its warning. |
| 요희 | 무야호 | human ally to intelligent spiritual beast | you | casual and familiar | Yohi asks Muyaho whether it wants her to ride on its back. |
| 백호 | 진태경 | guardian_spirit_to_human_ally | you | terse and irritated | The White Tiger responds telepathically after Jin calls it Whitey and jokes about its former name. |

## Listed compact profiles

### Baeksang.md

# Baeksang (백상)

- **Safe through:** Chapter 695
- **Aliases:** None
- **Role:** Baeksang is the Palace Lord of the Nanman Beast Palace and the sole Great Chieftain of Nanman, directing the Palace's forces during the crisis surrounding Yayul Cheok's former regime.
- **Personality:** Cold, rigid, meticulous, and strategically resolute, yet burdened by regret, grief over Hwi's death, and a final conflicted impulse to spare others from the coming bloodshed.
- **Voice:** Rigid, formal, restrained, and emotionally distant.
- **Relationships:** Baeksang is Yayul Cheok's sworn younger brother and childhood companion, Yayul Mok's sworn uncle, and the father of deceased Baekhwi, whom the Great Snow Fiend killed; he cultivated Yohi with gold and influence and used her support to advance Dark Heaven's preparations.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 695
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 695
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple, the Fire Gate Clan's nineteenth successor, and the Pavilion Master of the Fire Dragon Pavilion within the Murim Alliance, a Supreme Peak master with the Heavenly Martial Physique and Force, a publicly recognized S-rank-level Hunter who formally retains an A-rank license, and the leader of the assault now entering the Nanman Beast Palace.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 695
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Muyaho.md

# Muyaho (무야호)

- **Safe through:** Chapter 693
- **Aliases:** White Tiger
- **Role:** Muyaho is Yayul Mok's enormous white tiger companion and a renowned Nanman spiritual creature currently sharing an unexplained healing realm with Yohi and Jin Taekyung.
- **Personality:** Muyaho is intelligent enough to understand speech, wary of threats, and strongly food-motivated.
- **Voice:** Muyaho communicates through growls, roars, and gestures rather than human speech.
- **Relationships:** Muyaho is Yayul Mok's cherished companion and returned to Jin with Heugung and Yohi after carrying them through the darkness.

### White Tiger.md

# White Tiger (백호)

- **Safe through:** Chapter 695
- **Aliases:** Whitey
- **Role:** The White Tiger is the guardian spirit of the sacred stone, restored to its former silver-white tiger form and advancing toward the Nanman Beast Palace with a vast beast army.
- **Personality:** Irritable and contemptuous of Jin Taekyung's jokes.
- **Voice:** Telepathic, terse, and easily exasperated.
- **Relationships:** The White Tiger carries Jin Taekyung and Yohi, guards the sacred stone, and advances with Jin's forces.

### Yohi.md

# Yohi (요희)

- **Safe through:** Chapter 695
- **Aliases:** None
- **Role:** Yohi is the female Great Chieftain of the Yao people and has returned to the Nanman Beast Palace alongside Jin Taekyung.
- **Personality:** Yohi is charismatic, proud, perceptive, and fiercely resistant to Heugung's betrayal and coercion.
- **Voice:** Not established.
- **Relationships:** Yohi leads the Yao people, hates Heugung after his betrayal, and is being coerced to support his false account by the threat against Boshan and her people.

## Korean source

```text
＃696화



드드드득!

건물이 흔들리고, 땅이 울린다.

남만야수궁을 감싸 안은 적막함은 이미 깨져 나간 지 오래.

문을 걸어 잠근 채 집 안에 숨어 있던 외궁의 부족민들은 어린 자식들을 품으로 끌어당겼고, 곳곳에 설치된 망루(望樓) 위에서 하릴없이 근무 시간을 보내다 무심코 고개를 돌린 전사들은 눈을 부릅떴다.

“저, 저게 뭐…….”

크아아앙!

천지를 울리는 거대한 포효가, 누군가의 입술 사이로 흘러나온 넋 나간 목소리를 집어삼킨다.

뒤늦게 정신을 차린 전사 중 하나가 비명처럼 외쳤다.

“저, 적이다!”

그러나 대부분의 전사들은 그 말에도 움직이지 않았다. 아니, 움직일 수 없었다.

어찌 그럴 수 있겠는가.

그들은 그저 멍하니 입을 벌린 채 외궁에 나 있는 십여 개의 대로(大路)를 가로지르는 맹수의 대군을 바라볼 수밖에 없었다.

‘이, 이럴 수가.’

그것은 두려울 만큼 경이로운 광경이었다.

수천, 수만에 달하는 숫자의 맹수가 한 몸이 되어 내달리고 있다.

이 자리의 누구도 이러한 광경을 본 적이 없다.

이 땅에서 가장 나이 든 노인조차, 심지어 그의 조부조차 마찬가지일 것이다.

그야말로 재앙(災殃). 혹은 이적(異蹟).

이해할 수 없는 불가해(不可解)의 영역 앞에서, 평범한 전사에 불과한 그들 모두는 석상처럼 굳어 버렸다.

가장 먼저 정신을 차린 상관의 외침 역시 먼 곳에서 들려오는 메아리처럼 귓가에서 흩어질 뿐이었다.

“경종! 경종(警鐘)을 울려라! 당장 내궁에 알려야 한다!”

“아, 아아…….”

“이런 멍청한!”

벌컥 성을 낸 상관이 넋 나간 수하를 밀쳐 냈다. 그리고 경종과 연결된 밧줄을 잡으려던 그때.

그는 문득 조금 전까지만 해도 뜨겁게 내리쬐던 햇볕이 사라졌다는 것을 깨달았다.

솨아아아아.

먹구름?

아니다. 적어도 그가 아는 먹구름은 이처럼 빠르게 움직이지도 않고, 낮게 깔리지도 않는다.

마침내 귓가로 전해지는 기이한 소리와 함께 가까워지는 먹구름의 정체를 확인한 그가, 자신도 모르게 경악에 가득 찬 욕설을 내뱉었다.

“……빌어먹을.”

그 순간.

먹구름이, 아니 광활한 하늘의 한 조각을 검게 물들이며 날아든 수많은 날짐승이 그를 덮쳤다.

솨아아아악!

푸드드득!

종류도, 숫자도 파악할 수 없었다. 날카로운 울음소리와 번쩍이는 부리. 그리고 흩날리는 깃털만이 온 사방에 가득했다.

하나의 거대한 괴물로 화한 날짐승들은 그렇게 폭풍처럼 다섯 개의 망루를 휩쓸었다. 아니, 부수었다.

콰직, 우지끈!

“마, 망루가 무너진다!”

“으아아악!”

하나로 뭉쳐 들이닥치는 날짐승들은, 그야말로 살아 있는 공성추(攻城鎚)나 다름없다.

서서히 기울어지는 세상과 붕 뜨는 듯한 부유감 속, 그들은 산산이 부서진 망루의 잔해와 함께 지상으로 추락했다.

쿠구구궁! 대애앵!

어지간한 장정만큼이나 큰 경종이 가장 먼저 지면을 뒹굴었고, 뒤이어 허공에서 몸을 비튼 전사들이 비틀거리며 땅에 착지했다.

그리고 숨을 헐떡이며 고개를 든 그들의 머리 위로, 거대한 그림자가 드리워졌다.

“백상은 어디 있지?”

“……!”

귓가를 파고드는 나직한 목소리. 하지만 그 자리의 모두는 심장이 얼어붙는 듯한 한기를 느꼈다.

보는 것만으로도 오금이 저릴 만큼 거대한 백호 때문에?

그것이 아니라면 그 뒤로 보이는 수많은 맹수 때문에?

아니다. 오히려 백호에게서 전해지는 느낌은 이상하리만치 따뜻하면서 신비로웠고, 가까이에서 마주한 맹수들의 눈동자는 온순했다.

그들을 얼어붙게 만든 것은 백호의 등에 올라탄 채, 그들을 굽어보는 한 사람의 안광(眼光)이었다.

장대하면서도 완벽하게 균형 잡힌 체구. 아무렇게나 헝클어진 머리카락과 여타 남만인과는 달리 시원시원하게 뻗은 이국적인 이목구비.

그리고…… 그의 손에 들린 한 자루의 새하얀 창.

“진태경!”

비명처럼 부르짖은 누군가의 외침과 함께, 전사들의 손이 본능적으로 허리춤에 찬 병장기를 뽑아 들었다. 정확히는, 뽑으려 했다.

적어도 진태경이 입을 열기 전까지는.

“그거 뽑으면, 좋은 꼴 못 본다.”

“……!”

“그리고 눈깔이 달려 있으면 주위를 둘러봐. 이 자리에 나 말고 누가 있는지.”

남만 땅 전체를 발칵 뒤집어 놓은 흉수. 진태경이 엄청난 숫자의 맹수들과 나타난 이상, 더 놀랄 일도 없을 거라고 생각했다.

하지만 또 다른 한 사람의 얼굴을 확인한 전사들은 눈을 부릅뜰 수밖에 없었다.

저벅.

비교적 작은 덩치를 지닌 또 다른 백호가 그들을 향해 걸음을 내디딘다.

지친 행색으로도 미모를 감출 수 없는 아름다운 여인을 등에 태운 채.

“서, 설마…….”

“요희 대족장님?”

요희. 그녀의 붉은 입술 사이로 낭랑한 목소리가 흘러나왔다.

“나를 알아보겠느냐?”

어찌 모르겠는가. 일 년에 한 번 대회의가 열릴 때마다 사람들 앞에 모습을 드러내는 그녀를 보기 위해 거리가 인산인해를 이루는데.

하지만 무엇보다 그들을 혼란스럽게 만든 것은, 며칠 전 있었던 요서부의 일 이후 죽었다는 소문이 암암리에 퍼진 그녀가 아무런 두려움이나 포박도 없이 진태경과 나란히 하고 있다는 것이었다.

그것도 아득한 숫자의 맹수들을 이끄는 선두에서.

“대, 대족장님. 어찌하여 이런 흉수와 함께…….”

“흉수라.”

작게 중얼거린 요희가 고개를 돌려 진태경을 응시했지만, 진태경의 시선은 그녀를 향하고 있지 않았다.

어느덧 불길함이 감도는 대로의 끝, 외궁과 내궁을 가로막은 거대한 철문을 응시하고 있던 그가 문득 입을 열었다.

“저기 오네, 흉수.”

그리고 다음 순간.

구구구구궁.

무거운 마찰음을 내며 철문이 열리기 시작한다. 높게 쌓아 올린 내궁의 석벽 위로 모습을 드러낸 수많은 화살촉과 함께.

처처처척!

햇빛을 받은 화살촉이 번쩍인다.

한껏 당겨진 활시위와 긴장된 호흡. 일천에 달하는 궁수들이 석벽 위에서 그들을 겨누는 가운데, 철문 뒤에 가려져 있던 한 사람의 인영(人影)이 비로소 모습을 드러냈다.

저벅.

유난히도 크게 울려 퍼지는 발소리.

잡티 하나 묻지 않은 새하얀 옷자락이 땅을 스치고, 담담한 눈빛이 공간을 가로질러 한 사람과 맞닿는다.

“왔구나. 기어코.”

백상. 웅혼한 공력이 실린 그의 목소리에, 진태경은 창날을 늘어트리며 대답했다.

“그래, 왔다.”

이 개새끼야.



* * *



백상.

놈의 얼굴을 마주한 순간, 나는 전신의 공력이 용암처럼 들끓는 것을 느꼈다.

당장이라도 뛰쳐나가고 싶다.

수호령의 등을 박차고 바람처럼 달려가, 내가 할 수 있는 가장 빠르고 강한 일격으로 놈의 목숨을 끊고 싶었다.

하지만…….

스륵.

소매를 붙잡는 가느다란 손가락. 파르르 떨리는 요희의 목소리가 귓가에 전해진다.

“안 돼. 아직은.”

그래, 나도 알고 있다.

지금 백상의 목을 쳐 날린다면, 그건 한 마디도 남지 않은 폭탄의 심지에 불을 붙이는 것이 된다.

백상은, 놈은 그렇게 죽어서는 안 된다. 남만야수궁의 궁주가 아닌, 남만인 모두를 속이고 암천과 붙어먹은 배반자이자 찬탈자로 죽어야 한다.

궁주가 죽는다면 참혹한 전투가 기다리고 있겠지만, 배반자를 위해 싸울 전사는 어디에도 없으니까.

그것이 조금이라도 헛된 희생을 줄일 수 있는 유일한 방법이었고, 내 옆에 선 요희는 모든 진실을 밝히고 코앞까지 들이닥친 전투를 막을 수 있는 결정적인 한 수다.

“가자.”

내 속삭임에 고개를 끄덕인 수호령과 무야호가 걸음을 옮기기 시작했다.

빠르지도, 느리지도 않은 걸음과 함께 나아가는 우리를 따라 일천 개의 화살촉이 움직인다.

명령이 떨어지는 즉시 화살비를 쏘아 보낼 것처럼.

그러나 서서히 좁혀지는 거리만큼, 번쩍이던 화살촉이 흔들리고 팽팽하던 시위가 느슨해진다.

요희를 알아본 이들을 시작으로 작은 동요가 내궁의 석벽 위로 번져 나가고 있었다.

물론 예외는 있었다.

백상. 흔들림 없는 놈의 면상을 바라보며 나는 입을 열었다.

“아무리 그래도 한솥밥 먹던 대족장이 살아 돌아왔는데, 안부 인사 정도는 해야지. 안 그래?”

공력을 실어 내뱉은 목소리가 사방으로 퍼져 나간다.

한층 더 몸집을 불린 동요 속에서, 백상이 굳게 다물려 있던 입술을 뗐다.

“무슨 정이 있어 인사가 필요하겠느냐. 모두 각자의 목적에 의해 맺어진 관계인 것을.”

“……!”

“……!”

나도 모르게 얼굴이 굳는 것이 느껴졌다. 아마 그것은 요희도 마찬가지일 것이다.

우리는 지금, 같은 생각을 공유하고 있었다.

‘어째서?’

내가 아는 백상은 이런 사람이 아니었다. 놈은 교활하고, 간교하다. 남만이 지금과 같은 혼란에 빠진 가장 큰 원인 중 하나는 무공보다 더욱 무서운 놈의 심계(心計)였다.

그런데 인정했다. 요희의 존재를. 그것도 자신을 따르는 모든 이들 앞에서.

꾸국.

창대를 잡은 손에 힘이 들어간다. 이를 악문 나는 타오르는 듯한 눈빛으로 백상을 노려보았다.

“이게 무슨…… 개수작이냐.”

“내가 부정할 거라 생각했더냐?”

내게 되물은 백상이 문득 뒤를 돌아보았다.

활짝 열린 거대한 철문 너머, 도산검림(刀山劍林)을 이루고 있는 수많은 남만 전사들과 석벽 위의 궁수들이 크게 뜬 눈으로 그를 바라보는 중이었다.

“더 이상 무슨 말이 필요하겠느냐. 너희가 알고 있고, 곧 저들도 깨닫게 모든 것들이 전부 진실인 것을.”

“……!”

“그래. 맞다.”

자신을 따르는 전사들에게서 시선을 뗀 백상이 하늘을 바라보았다.

구름 한 점 없이 맑은 날씨. 뜨거운 햇볕이 그의 얼굴에 내려앉는다.

“난 모두를 배신했다.”

공력이 실린 나직한 목소리가 어느샌가 내려앉은 숨 막히는 적막을 깨트린다. 공기를 타고, 바람을 뚫고, 외궁을 가로지른 대로와 내궁의 석벽을 넘어 모두에게 전해진다.

“하루를 십 년처럼 살았다. 오직 한 가지 목적을 이루기 위해서 용서받지 못할 변절자가 되었고, 마침내 이곳까지 왔다.”

불현듯 숨이 막혔다. 이건 자신이 저지른 죄에 대해 고백하고, 용서를 청하는 고해성사가 아니다.

아니, 오히려…….

‘모든 것이 끝났을 때 나타나는 후련함. 그리고 절망.’

자포자기와는 근본부터 다른 감정.

지금의 백상은, 그저 토해 낼 뿐이다. 수십여 년의 세월 동안 하루도 빠짐없이 꾹꾹 눌러 왔던 감정을.

그리고 그토록 바라던 목적을 이루었음에도 절망하는 자신의 모습을 숨김없이 드러내고 있었다.

‘설마.’

순간 번개처럼 뇌리를 스치는 어떤 생각과 함께, 전신의 털이 곤두서는 듯한 감각이 전신을 덮친다.

뒤이어 비명과도 같은 외침이 내 입술을 비집고 뛰쳐나왔다.

“모두 물러……!”

그리고 다음 순간.

구구구궁! 번쩍!

천지를 떨어 울리는 천둥소리가 들리며, 모두의 머리 위로 먹구름이 드리워졌다.

이제는 한 줄기의 햇빛도 찾아볼 수 없는 세상 속에서, 누군가의 목소리가 귓가를 파고들었다.

“어쩌나. 이미 늦어 버렸는데.”
```

## Final English reading copy

```markdown
# Chapter 696

Rumble, rumble, rumble!

Buildings shook, and the earth trembled.

The silence surrounding the Nanman Beast Palace had long since been shattered.

The tribespeople of the Outer Palace, who had locked their doors and hidden inside their homes, pulled their young children into their arms. Warriors who had been spending their shifts listlessly atop the watchtowers scattered throughout the palace happened to turn their heads—and their eyes widened.

“W-what is that…?”

GRAAAAAAAWR!

A tremendous roar that shook Heaven and Earth swallowed the dazed voice that had slipped between someone’s lips.

One of the warriors who came to his senses belatedly shouted as though screaming.

“Th-the enemy!”

But most of the warriors did not move even at those words. No—they could not move.

How could they?

They could only stand there with their mouths hanging open, staring at the army of beasts racing across the dozen or so broad roads running through the Outer Palace.

*Th-this can’t be.*

It was a sight so wondrous that it was terrifying.

Thousands—tens of thousands—of beasts were racing as one.

No one present had ever witnessed anything like it.

Not even the oldest elder in the land. Probably not even his grandfather.

It was a calamity.

Or perhaps a miracle.

Faced with something incomprehensible, something beyond the realm of understanding, every one of them—ordinary warriors all—stiffened like stone statues.

Even the shout of their superior, who was the first to recover, merely scattered around their ears like an echo drifting from far away.

“Sound the alarm! Sound the alarm bell! We have to inform the Inner Palace immediately!”

“Ah… ah…”

“You idiots!”

The enraged superior shoved aside his dazed subordinate. Then, just as he reached for the rope connected to the alarm bell, he realized that the sunlight that had been beating down fiercely only moments ago had vanished.

Whoooooosh.

Dark clouds?

No. At least, the dark clouds he knew did not move this quickly, nor did they hang so low.

At last, he recognized the identity of the dark cloud drawing nearer amid the strange sound reaching his ears, and he involuntarily spat out a curse filled with shock.

“…Goddamn it.”

At that moment—

The dark cloud—or rather, countless flying beasts that had flown in and dyed a section of the vast sky black—descended upon him.

Whoooooosh!

Flap, flap, flap!

He could not determine either their kinds or their number. Sharp cries, flashing beaks, and scattering feathers filled every direction.

The flying beasts, transformed into one enormous monster, swept through five watchtowers like a storm.

No—they smashed them apart.

CRACK! CREEEAK!

“The watchtower’s collapsing!”

“AAAAARGH!”

The flying beasts that had charged in as one were no different from a living battering ram.

As the world slowly tilted and a sensation of floating lifted their bodies, the warriors fell to the ground together with the shattered remains of the watchtower.

Rumble, rumble, rumble! Daaang!

The alarm bell, nearly as large as a grown man, tumbled across the ground first. The warriors who twisted their bodies in midair landed awkwardly after it.

Then, as they panted and raised their heads, a vast shadow fell over them.

“Where is Baeksang?”

“……!”

The quiet voice bored into their ears. Yet everyone there felt a chill that seemed to freeze their hearts.

Was it because of the enormous White Tiger, so massive that merely looking at it made their knees go weak?

Or because of the countless beasts behind it?

No. The sensation emanating from the White Tiger was strangely warm and mysterious, while the eyes of the beasts confronting them at close range were gentle.

What froze them was the gaze of the man sitting atop the White Tiger’s back and looking down at them.

A tall, perfectly balanced physique. Hair tousled without care. Exotic features that extended boldly and cleanly, unlike those of the other Nanman people.

And…

A single pure-white spear held in his hand.

“Jin Taekyung!”

As someone shouted his name like a scream, the warriors instinctively reached for the weapons at their waists.

More precisely, they tried to draw them.

At least, they did until Jin Taekyung opened his mouth.

“If you draw those, you’re not going to like what happens.”

“……!”

“And if you’ve got eyes, look around you. Who else is here besides me?”

Jin Taekyung was the monster blamed for throwing all of Nanman into an uproar. Since he had appeared with an enormous number of beasts, they had thought there could be nothing left to surprise them.

But when the warriors recognized another person’s face, they could not help opening their eyes wide.

Step.

Another White Tiger, relatively smaller in size, took a step toward them.

A beautiful woman whose exhaustion could not conceal her beauty was riding on its back.

“Su-surely not…”

“Great Chieftain Yohi?”

Yohi. A clear voice flowed from between her red lips.

“Do you recognize me?”

How could they not? Whenever the Tribal Grand Council was held once a year, the streets became packed with people hoping to catch a glimpse of her as she appeared before the public.

But more than anything, what confused them was that she—rumored to have died after the incident at the Western Yao Estate several days ago—was standing beside Jin Taekyung without fear or restraints.

And she was at the very front, leading an immeasurable number of beasts.

“G-Great Chieftain. Why are you with a monster like him…?”

“A monster…”

Yohi muttered quietly and turned her head to look at Jin Taekyung, but Jin Taekyung was not looking at her.

He was staring at the end of the broad road, where an ominous feeling lingered—the enormous iron gate dividing the Outer Palace from the Inner Palace.

Then he suddenly spoke.

“There he comes—the monster.”

And the next moment—

Rumble, rumble, rumble.

The iron gate began to open with a heavy grinding sound. Along with the countless arrowheads appearing atop the stone walls of the Inner Palace, which had been built high overhead.

Click, click, click!

The arrowheads flashed in the sunlight.

With bowstrings pulled taut and breath held tight, nearly a thousand archers aimed down at them from atop the stone walls. Then, at last, the silhouette of one person hidden behind the iron gate came into view.

Step.

His footsteps rang out with unusual clarity.

The hem of his spotless white robes brushed the ground, and his calm gaze crossed the space to meet the eyes of one man.

“You came. In the end, you did.”

Baeksang.

His voice carried powerful internal energy. Jin Taekyung lowered the spearhead and answered.

“Yes. I came.”

*You fucking bastard.*

* * *

Baeksang.

The moment I saw his face, I felt the internal energy throughout my body boiling like lava.

I wanted to charge out immediately.

I wanted to kick off the guardian spirit’s back, race toward him like the wind, and end his life with the fastest, strongest strike I could manage.

But…

Slick.

A slender finger caught hold of my sleeve. Yohi’s trembling voice reached my ears.

“No. Not yet.”

Yes. I knew that too.

If I cut Baeksang’s head off right now, it would be like lighting the fuse of a bomb with no time left on it.

Baeksang—he could not die like that. He had to die not as the Palace Lord of the Nanman Beast Palace, but as the traitor and usurper who had deceived all the Nanman people and joined forces with Dark Heaven.

If the Palace Lord died, a brutal battle would await us. But there would be no warriors anywhere willing to fight for a traitor.

That was the only way to reduce the number of needless sacrifices, even if only slightly. And Yohi standing beside me was the decisive card that could reveal the entire truth and prevent the battle now bearing down on us.

“Let’s go.”

At my whisper, the guardian spirit and Muyaho nodded and began to move.

A thousand arrowheads moved along with us as we advanced at a pace that was neither fast nor slow.

As though they were ready to send a rain of arrows the instant the order was given.

However, as the distance slowly narrowed, the arrowheads that had been flashing began to tremble, and the taut bowstrings slackened.

Beginning with those who recognized Yohi, a small disturbance was spreading across the stone walls of the Inner Palace.

Of course, there was one exception.

Baeksang.

Looking at his unmoving face, I opened my mouth.

“Even so, the Great Chieftain you used to share a pot with has come back alive. You should at least say hello. Don’t you think?”

My voice, charged with internal energy, spread in every direction.

As the disturbance swelled even further, Baeksang finally parted his tightly sealed lips.

“What affection is there between us that a greeting should be necessary? We were merely bound together by our respective purposes.”

“……!”

“……!”

I felt my face stiffen despite myself. Yohi had probably reacted the same way.

We were both thinking the same thing.

*Why?*

The Baeksang I knew was not like this. He was sly and cunning. One of the greatest causes of Nanman’s current chaos was his scheming, which was even more frightening than his martial arts.

And yet he had admitted it.

He had acknowledged Yohi’s existence, in front of everyone who followed him.

The hand gripping my spear shaft tightened.

Clenching my teeth, I glared at Baeksang with blazing eyes.

“What the hell is this…? What kind of bullshit are you pulling?”

“Did you think I would deny it?”

Baeksang answered my question, then suddenly turned around.

Beyond the wide-open iron gate, countless Nanman warriors forming a mountain of sabers and a forest of swords, along with the archers atop the stone walls, were staring at him with their eyes wide.

“What more needs to be said? Everything you know—and everything they will soon realize—is true.”

“……!”

“Yes. That is correct.”

Baeksang took his gaze away from the warriors following him and looked up at the sky.

The weather was clear, without a single cloud. Hot sunlight fell across his face.

“I betrayed everyone.”

His quiet voice, charged with internal energy, broke the suffocating silence that had settled over the area.

It traveled on the air, pierced through the wind, crossed the broad road running through the Outer Palace, passed over the stone walls of the Inner Palace, and reached everyone.

“I lived each day as though it were ten years. To accomplish a single purpose, I became an unforgivable turncoat, and at last I made it this far.”

Suddenly, I found it hard to breathe.

This was not a confession in which he admitted the sins he had committed and begged for forgiveness.

No. Rather…

*The relief that comes when everything is over. And despair.*

It was an emotion fundamentally different from giving up.

The Baeksang before us was merely vomiting out the emotions he had pressed down day after day for several decades.

Even after achieving the purpose he had desired for so long, he was revealing without concealment the sight of himself sinking into despair.

*No way.*

Along with a thought that flashed through my mind like lightning, the sensation of every hair on my body standing on end swept over me.

Then a scream burst from my lips.

“Everyone, fall back—!”

And the next moment—

Rumble, rumble, rumble! Flash!

Thunder that shook Heaven and Earth rang out, and dark clouds spread over everyone’s heads.

In a world where not even a single ray of sunlight could be found, someone’s voice bored into my ears.

“What a shame. It’s already too late.”
```

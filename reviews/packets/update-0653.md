<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0653.txt",
      "sha256": "aa942190d97675bde239dcfeb2d11102f6d05313d3cfef536276e9e8f8e7c755",
      "bytes": 12552
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "502171c4e48cf0a2a440f433d4accb355099b6f8c678d2a9a28ae165253abb2b",
      "bytes": 2180
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "2816675828363f5aa2eda7b704c7c1f5c45a36cf153542b6fcb89ef04a3628c4",
      "bytes": 199864
    },
    {
      "path": "characters/Baeksang.md",
      "sha256": "6b41a6ae45f88dcf09eb83764da8d41a09eb9e13356326eba03e430c6ccb775f",
      "bytes": 748
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "565de75a142407c9a19d354d478eee45f578415b8752fbfaeb4c21b274137fcb",
      "bytes": 553
    },
    {
      "path": "characters/Heugung.md",
      "sha256": "18ca8b32506a227f671d208c0bebb582d568808770e405ed3540cbef0a2dc0b1",
      "bytes": 685
    },
    {
      "path": "characters/Namho.md",
      "sha256": "47aef1e5724109ee66d706eedfe272dfb4dd96ac946765eb9fdbaac8b450ca73",
      "bytes": 843
    },
    {
      "path": "characters/Sama Pyo.md",
      "sha256": "99fb51b36a3b31f9a3a15ef654e93bf25182c9b15d15b921281683dbd17b2f30",
      "bytes": 936
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "7c0b8a809717c5cbf87d9c5b080474a42e7697bda10e219b578e7fd91edcfafc",
      "bytes": 585
    },
    {
      "path": "characters/Yohi.md",
      "sha256": "9272c6b14f32089a94941e16f180e9558bf77655c992b1557389927d4d5310f3",
      "bytes": 542
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "88019c0cfd61c3aeb2dd467971aea7a4324db023c59e4689c59c3828ae2f0565",
      "bytes": 205898
    }
  ],
  "estimated_tokens": 10167
}
-->

# Durable State Update — Chapter 653

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 653. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 653. Profile updates may replace only one
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
  "chapter": 653,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 653,
    "continuity_sources": [653],
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
    "Jin remains in the Nanman Beast Palace's Inner Palace as the Third Young Master of the Jin Family of Taiyuan and head of the Fire Dragon Pavilion.",
    "Heugung alleges that Baeksang colluded with Dark Heaven but has no concrete proof.",
    "Heugung has secretly evaded Baeksang's surveillance for more than twenty years, including by learning the Bone-Shrinking Technique.",
    "Heugung claims Baeksang exchanges unexplained monthly missives and disappears alone, monthly since last year.",
    "Heugung's loyal retainers investigated Baeksang's secret refuge twenty years ago, but the refuge was destroyed and the retainers died or vanished.",
    "Heugung genuinely loves Yohi and says she chose wrongly while trying to revive the Yao people.",
    "Heugung offers to testify at the next day's Tribal Grand Council if his and Yohi's safety is guaranteed.",
    "Heugung has staked his life on the truth of his allegations.",
    "Jin has not yet informed the Beast Miao King and intends to consult the Fire Dragon Pavilion first.",
    "A planned nighttime assault targeted the Fire Dragon Pavilion while most of its strongest members were absent.",
    "Sama Pyo killed twenty masked attackers, including seven Peak masters, before Jin returned.",
    "Taishan was awakened by the threat to his meat and drove back the attackers with overwhelming force."
  ],
  "continuity_sources": [
    652
  ],
  "open_questions": [
    "Is Baeksang truly colluding with Dark Heaven, and what evidence can Heugung provide?",
    "What happened at Baeksang's secret refuge, and who destroyed it?",
    "Will the Beast Miao King accept Heugung as a witness and guarantee Heugung's and Yohi's safety?",
    "How knowingly did Yohi align herself with Baeksang's side?",
    "Who organized the masked assault on the Fire Dragon Pavilion, and why was it timed for Jin's absence?"
  ],
  "safe_through": 652,
  "temporary_decisions": [
    "Use Insi for 인시.",
    "Use the hour of the Rabbit for 묘시.",
    "Use Bone-Shrinking Technique for 축골공.",
    "Use Tribal Grand Council for 대회의.",
    "Use missive for 전서."
  ],
  "version": 1
}
```

## Exact glossary matches

| 암천     | **Dark Heaven**                  |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 초식     | **form**                                         | Numbered technique movement                           |
| 검기     | **Sword Energy**                                 | When functioning as projected weapon qi               |
| 사파     | **unorthodox faction**                           |                                                       |
| 전각     | **pavilion**                                 | Use “hall” only when established for a specific named building |
| 일격     | **One Strike**                         |
| 백상 | **Baeksang** | Great chieftain of the Bai people and Yayul Cheok's sworn younger brother. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 흑웅 | **Heugung** | Great chieftain of the Yi people; his name literally means Black Bear. |
| 남호 | **Namho** | Hidden Shadow Pavilion code name; literally associated with amber from the south. |
| 사마표 | **Sama Pyo** | Young Sect Leader of the Black Dragon Demon Gate. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 요희 | **Yohi** | Female great chieftain of the Yao people. |
| 화염신장 | **Flame Divine Palm** | Jopil's deadly palm technique, noted when Taekyung compares Jopil with Mukyung. |
| 화시 | **fire arrow** | Flaming arrow Lee Seowol fires to signal Cheol Mubaek. |
| 북망산 | **Mount Beimang** | Mountain associated with burial grounds; used as a threat to send someone to their death. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 일각 | **fifteen minutes** | Quarter of a shichen; used for the remaining completion time. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 신력 | **divine strength** | Superhuman strength attributed to Taekyung. |
| 살수 | **assassin** | Professional killer considered as a possible suspect. |
| 심맥 | **heart meridian** | Meridian severed by an infiltrator to commit suicide. |
| 지풍 | **Finger Qi** | Invisible qi attack fired by the Western Heaven Demon Lord. |
| 촌각 | **moments** | Short intervals disappearing from Jeok's day. |
| 대초자곤 | **two-section staff** | Weapon carried by Sama Pyo's giant subordinate. |
| 검기상인 | **the level of injuring others with Sword Energy** | Realm description used for Moon Beauty Saber. |
| 칠공 | **seven apertures** | The seven bodily openings through which Taekyung's overflowing heat escapes. |
| 화룡각 | **Fire Dragon Pavilion** | New name chosen for Taekyung's pavilion. |
| 성하 | **Seongha** | Hunter named during the cave battle. |
| 내궁 | **Inner Palace** | The inner compound of the Nanman Beast Palace. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 사마표 | 태산 | Young Sect Leader to subordinate | Taishan | informal and patronizing | Sama Pyo calls Taishan by name while ordering him to leave. |
| 태산 | 사마표 | subordinate to Young Sect Leader | Lord | crude and deferential | Taishan uses 주군 while obeying Sama Pyo. |
| 남호 | 태산 | guide_to_pavilion_member | Taishan | blunt and exasperated | Namho directly rebukes Taishan for eating the poisonous blood-feeding fungus. |
| 남호 | 사마표 | guide_to_young_sect_leader | Young Sect Leader | blunt and admonishing | Namho warns Sama Pyo that all grass and animals in the territory belong to the Nanman Beast Palace. |
| 사마표 | 남호 | young_sect_leader_to_guide | Elder Namho | formal and apologetic | Sama Pyo apologizes after Taishan attempts to seize the calf. |
| 요희 | 흑웅 | Yao great chieftain to Yi great chieftain | big brother | seductive and falsely affectionate | Uses 오라버니 to flatter and manipulate Heugung. |
| 흑웅 | 요희 | Yi great chieftain to Yao great chieftain | my dear | adoring and deferential | Responds to Yohi's manipulation with open infatuation. |
| 백상 | 요희 | Bai great chieftain to Yao great chieftain | Yohi | cold and formal | Calls to Yohi from outside the tent at the chapter's end. |
| 흑웅 | 백상 | younger_great_chieftain_to_senior_great_chieftain | Uncle Baek | deferential and nervous | Heugung addresses Baeksang as 백 숙부 after being confronted by his icy stare. |
| 태산 | 남호 | Fire Dragon Pavilion member to guide | Namho | clipped, childlike, and informal | Taishan directly addresses Namho while asking what Dark Heaven is. |

## Listed compact profiles

### Baeksang.md

# Baeksang (백상)

- **Safe through:** Chapter 651
- **Aliases:** None
- **Role:** Baeksang is the middle-aged great chieftain of the Bai people, one of Nanman's four most powerful great tribes.
- **Personality:** Cold, rigid, meticulous, and politically resolute, with a deep but guarded attachment to his sworn elder brother.
- **Voice:** Rigid, formal, restrained, and emotionally distant.
- **Relationships:** Baeksang is Yayul Cheok's sworn younger brother and childhood companion and Yayul Mok's sworn uncle, opposes the Nanman Beast Palace joining the Murim Alliance, remains distrustful of the Central Plains, and is alleged by Heugung to have colluded with Dark Heaven.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 652
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Heugung.md

# Heugung (흑웅)

- **Safe through:** Chapter 651
- **Aliases:** None
- **Role:** Heugung is the middle-aged great chieftain of the Yi people, one of Nanman's four great tribes.
- **Personality:** Heugung presents as foolish and easily flattered in public but is capable of concealed planning, disguise, and covert contact.
- **Voice:** Heugung speaks with warm enthusiasm and genuine, openly devoted affection toward Yohi.
- **Relationships:** Heugung remains publicly entangled with Baeksang, genuinely loves Yohi, and has secretly contacted Jin Taekyung to expose Baeksang's suspected collusion with Dark Heaven.

### Namho.md

# Namho (남호)

- **Safe through:** Chapter 652
- **Aliases:** Elder Chao
- **Role:** Namho is an eighty-year-old non-Han Hidden Shadow Pavilion agent who spent more than fifty years operating under the cover of the Poison Flower Pavilion in Nanman and now serves as the Fire Dragon Pavilion’s guide.
- **Personality:** Duty-bound, pragmatic, observant, and willing to use theatrical violence and crude insults to protect an intelligence operation.
- **Voice:** Measured and serious in private, but loudly abusive and convincing when maintaining his local cover.
- **Relationships:** Namho is a Hidden Shadow Pavilion contact for Jin Taekyung and the Fire Dragon Pavilion, receives intelligence from the Pavilion Master, and knows the code used by the Thousand-Faced Fox.

### Sama Pyo.md

# Sama Pyo (사마표)

- **Safe through:** Chapter 652
- **Aliases:** Black Dragon Saber
- **Role:** Young Sect Leader of the Black Dragon Demon Gate, a Morning Star reputed to be no less than the Ten Dragons and Phoenixes, and a member of the Fire Dragon Pavilion.
- **Personality:** Outwardly courteous and smiling, inwardly calculating, but genuinely protective of Taishan; in combat he is ruthlessly pragmatic, survival-focused, and unafraid to stake his life.
- **Voice:** Polite and ingratiating in public, with sardonic humor and controlled evasiveness.
- **Relationships:** Sama Pyo commands the absolutely loyal Taishan, is Sima Gong's son, was Ju Hwaran's former fiancé in a political engagement, and has joined the Fire Dragon Pavilion while openly intending to use Jin Taekyung as a useful card; he is now openly hostile toward fellow member Song Ilseom.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 652
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo; becomes explosively violent when his meat is threatened.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord.

### Yohi.md

# Yohi (요희)

- **Safe through:** Chapter 651
- **Aliases:** None
- **Role:** Yohi is the female great chieftain of the Yao people, one of Nanman's four great tribes.
- **Personality:** Yohi's public presence is charismatic and captivating, drawing widespread admiration and affection.
- **Voice:** Not established.
- **Relationships:** Yohi leads the Yao people, seeks to unite Nanman's four great tribes under Yao leadership, and manipulates Heugung alongside Baeksang.

## Korean source

```text
＃653화



“혹시 네 친구들이냐?”

소리 내어 웃은 사마표가 지친 목소리로 대답했다.

“그럴 리가.”

“하긴. 친구치고는 사이가 많이 나빠 보이긴 하네.”

나는 턱을 긁적이며 천천히 주위를 둘러봤다.

가뜩이나 연식이 오래된 전각은 무너져 버렸고, 공터에 무성하게 자라난 잡초는 핏물로 붉게 물들어 있었다.

음. 상황 파악 완료.

‘아주 개판이구만.’

잠깐 처소를 비운 사이에 족히 이십여 구에 달하는 시신이 생겼다. 우렁각시가 와서 청소해 줘도 모자랄 판에 야밤의 습격이라니.

내 등장과 함께 주춤거리는 우렁살수들을 힐끗 바라본 나는, 사마표를 향해 어깨를 으쓱해 보였다.

“오, 그래도 생각보다 좀 하는데.”

상반신이 피투성이가 된 사마표가 거친 숨을 몰아쉬며 대꾸했다.

“그래, 좀 하는 편이지. 사파 잡졸치고는.”

사실 이제는 사파 잡졸이라고 부르기가 미안할 정도다.

중과부적(衆寡不敵)의 상황. 게다가 상당한 수준의 적들을 상대로 이 정도까지 분투했다는 건 정말 목숨을 걸었다는 뜻이니까.

나는 내심 감탄하며 고개를 끄덕였다.

“이 정도까지 했는데 계속 사파 잡졸 취급하기에는 좀 그렇고…… 이제부터는 사파 독종이라고 해 줄게.”

“사파 독종이라. 그것참 고맙군.”

“오, 고마워? 의외네. 듣자마자 지랄할 줄 알았는데.”

“지랄도 힘이 있어야 하는 거다. 그리고 쓰러질 것 같으니까 자꾸 말 걸지 마.”

솔직한 대답에 피식 웃은 내가 입을 열었다.

“그럼 쓰러져.”

“뭐?”

“쓰러지라고. 뒷일은 걱정 말고.”

“제기랄. 좀 더 일찍 말해 주지…….”

감기는 눈과 함께 흐려지는 말꼬리. 동시에 서서히 기울어지는 사마표의 신형을 향해, 나는 발걸음을 뗐다.

스륵. 툭.

순식간에 지워지는 삼 장의 거리.

땅으로 고꾸라지려는 녀석을 붙잡은 그 순간. 날카로운 파공성과 함께 바람이 휘몰아쳤다.

쉭!

등 뒤에서 벌어진 일이었지만 볼 수 있었다. 아니, 날 선 감각을 통해 모든 것을 느끼고 읽을 수 있었다.

내가 새로운 공간으로 발을 디딘 이상, 이곳은 내 권역(圈域)이나 마찬가지다.

뻐억!

뒤도 돌아보지 않고 휘두른 일권에 무언가가 박살 난다. 머리통이 두부처럼 으스러진 복면인 하나가 피웅덩이 위로 처박혔다.

철벅.

허공으로 튄 끈적한 핏물이 내 등을 적신다. 아랑곳하지 않고 비교적 깨끗한 땅 위에 사마표를 눕힌 나는 문득 고개를 들었다. 석상처럼 굳어 있는 복면인들이 보였다.

“그런데 너희는 왜 가만히 있냐? 그나마 조금 전이 마지막 기회였는데.”

“……!”

“……!”

“뭘 그렇게 놀라. 그럼 벨튀만 하고 가려고 했냐, 이 시벌 새끼들아?”

숨 막히는 침묵 속, 복면 위로 드러난 십여 쌍의 눈동자가 세차게 흔들린 다음 순간.

파팟!

쉬이이잉!

처음과는 비교도 안 되는 광풍이 사방을 휩쓸었다.

지금까지 남아 있던 복면인들은 한 사람, 한 사람이 검기상인(劒氣傷人)의 경지에 오른 절정 고수들.

검, 도, 창, 낫……. 저마다의 병장기에서 흘러나온 파괴적인 기운이 허공을 격하며 내 전신 요혈을 노린다.

하지만 나는 한 치의 두려움도 없이 그 모든 것을 지켜보고 읽어 냈다.

기의 흐름. 병장기가 향하는 방향.

그리고 그들의 부릅뜬 눈에 희미하게 깃들어 있는 두려움까지.

그것으로 끝난 거다. 놈들은 이미 이 싸움에서 졌다.

스스로가 한낱 이리에 불과하다는 것을 깨달았다는 점에서. 그럼에도 그 사실을 인정하지 않고 호랑이에게 달려들었다는 점에서.

‘그럼 알려 줘야지. 어떻게든 도망쳐야 했었다는 걸.’

찰나의 순간 머릿속에 떠오르는 수십 개의 초식. 나는 그중 가장 잔인하고 파괴적인 것을 골라 움직였다.

쉬익! 카드득!

부드럽게 몸을 틀자, 아슬아슬하게 스쳐 지나간 네 개의 병장기가 서로를 향해 얽혀든다. 나는 곧게 편 수도(手刀)로 그 중심을 내리그었다.

서걱!

강기에 의해 토막 나는 병장기. 나는 무력화된 애병을 붙잡고 굳어 버린 복면인들 중 한 놈의 복부를 후려쳤다.

화염신장(火焰神掌).

퍼엉!

끔찍한 열기가 몸에 깃든 생기를 불태운다. 나는 칠공(七空)에서 매캐한 연기를 뿜어내며 허물어지는 놈을 뒤로하고 고개를 숙였다.

솨아악! 슁!

부지불식간에 등 뒤에서 날아온 일격.

그러나 내 목을 추수하려던 길쭉한 낫은 허공을 스쳤고, 그와 동시에 내가 뒤로 내뻗은 팔꿈치는 적의 가슴을 직격했다.

콰직!

십여 개의 갈비뼈가 으스러지는 소리와 함께, 헉 하는 단말마가 흘러나온다.

하지만 놈의 목숨을 앗아 간 것은 내 일격이 아닌, 동료가 내지른 창이었다.

푸푹!

이 새끼들 전우애 없는 것 좀 보게.

혀를 찬 나는 가슴을 뚫고 튀어나온 창날을 그대로 붙잡아 힘을 주었다.

콰직!

상대가 검기상인의 경지에 오른 절정 고수라면, 나는 검기성강(劍氣成罡)의 영역에 접어든 초절정 고수다.

나무젓가락을 꺾은 것처럼 창날을 툭 떼어 낸 나는 곧장 주인에게 돌려주었다.

쐐액, 퍼걱!

결과는 당연히 즉사. 미간에 창날이 심어진 복면인은 비명도 지르지 못하고 허물어졌고, 찰나라고 부를 수도 없을 만큼 짧은 시간 동안 세 명의 동료를 잃은 복면인들은 헛숨을 삼켰다.

‘이제 남은 건 일곱.’

나는 담담하게 적들의 머릿수를 헤아리며 걸음을 내디뎠다.

쉭!

바람과 함께 공간이 사라지고 새로운 적이 코앞까지 다가온다. 아니, 다가간 것은 나였다.

“……!”

부릅뜬 눈동자가 무언가를 말하려고 하는 듯했지만, 이미 늦었다. 나는 놈의 목을 잡아챈 손아귀에 힘을 가했다.

우두둑!

‘여섯.’

단번에 축 늘어지는 몸뚱어리에서 생명이 빠져나가는 것이 느껴진다.

자연스럽게 놈이 쥐고 있던 검을 빼앗아 가장 가까운 곳에 위치해 있던 적을 향해 흩뿌렸다.

“흡!”

혼비백산한 호흡과 함께 적이 휘어진 월도(月刀)를 비스듬히 세웠다. 내가 일직선으로 쏘아 보낸 검과 도기가 실린 월도가 부딪쳤다.

콰쾅!

굉음과 함께 뒤집히는 땅. 그리고 비틀거리는 신형이 뿌옇게 피어오른 흙먼지 사이로 걸어 나왔다.

검에 담겨 있던 기운을 이기지 못해 부서진 월도의 파편이 수십개로 나뉘어 놈의 전신에 박혀 있었다.

“그륵. 그르륵…….”

털썩.

가장 큰 파편이 목에 박혀 있었기 때문일까. 놈은 유언도 남기지 못하고 피가래 끓는 소리와 함께 쓰러졌다.

나는 목이 부러진 적의 시신을 밀어 내며 나직하게 입을 열었다.

“이제 다섯.”

“……!”

“……!”

느껴졌다. 숨 막히는 적막을 가득 채운 공포가.

불과 촌각(寸刻) 만에 다섯 명의 절정 고수가 쓰러졌고, 나는 상처 하나 입지 않은 모습으로 다음 먹잇감을 노리고 있었다.

“다음은 누가 덤빌래?”

내 질문에 누구도 대답하지 않았다.

그리고 얼어붙은 채 귀신이라도 본 것처럼 부릅뜬 눈으로 나를 응시하던 복면인들의 선택은, 내가 아닌 또 다른 표적을 노리는 것이었다.

파팟!

남은 다섯 중 셋은 나를, 나머지 둘은 남호와 태산을.

인정한다. 아마 저것이 놈들로서는 최선의 선택이었을 테니까. 하지만 내 인정과는 별개로, 그 선택의 결과마저 최선일 수는 없었다.

“내가 똑똑히 봤다! 저기 저놈들이 닭 다리 두 개 다 처먹었다!”

“다리? 날개도 아니고 다리? 그것도 두 개 다?”

남호의 외침에 믿을 수 없다는 듯이 눈을 깜빡이던 태산이 옆구리에서 찬 대초자곤(大梢子棍)을 뽑아 들었다.

“닭 다리 두 개! 선 넘었다! 너희는 사람이 아니다!”

누가 사람이 아닌지는 투표를 해 봐야 판가름 나겠지만, 태산은 크고 우람한 대초자곤으로 투표 자체를 무의미하게 만들었다.

퍽! 우직!

타고난 신력(神力)은 방어조차 무력화시키기에 충분했다.

무심코 검을 들어 대초자곤을 막은 복면인 중 하나는 그대로 두 손목이 부러졌고, 비명을 지르기도 전에 나머지 한 놈과 사이좋게 머리통이 박살 났다.

콰직!

단말마도 지르지 못한 채 나뒹구는 두 구의 시체.

태산의 등 뒤에 숨어 있던 남호가 주먹을 불끈 움켜쥐며 외쳤다.

“그렇지! 이 죽이고 싶지만 기특한 녀석 같으니!”

“우어어어어! 태산이 기특하다!”

“잘했다! 이 빌어먹을 놈! 매번 죽어라 처먹기만 하더니 네놈이 기어코 밥값을 하는구나!”

악담인지 칭찬인지 모를 말을 하는 남호를 보며 피식 웃은 나는 남아 있는 적들을 향해 입을 열었다.

“자, 이제 셋.”

“……!”

“……!”

“……!”

의미를 알아들은 복면인들의 눈꼬리가 파르르 떨린다.

놈들은 동료가 죽어 나가는 와중에도, 감히 내게 덤벼들 생각조차 못 한 채 뒷걸음질 치던 중이었다.

“혹시나 해서 말하는 건데, 도망치면 죽을 거야. 물론 먼저 북망산 관광 간 너희 친구들보다 훨씬 아프고, 길게 살다가 숨이 끊기겠지.”

꿀꺽.

나직한 목소리로 건네는 내 경고에 누군가의 목울대가 크게 일렁인다.

이들은 하나같이 앞에서 동료들이 어떻게 죽었는지 두 눈으로 똑똑히 지켜봤다. 하지만 도망친다면 오히려 그렇게 죽기를 바라게 될 것이다.

“하지만 이 자리에서 투항하고 내가 원하는 정보를 말해 준다면…… 무슨 수를 써서라도 너희는 살려 준다. 못 믿겠으면 내 목숨이라도 걸지.”

굳이 이렇게 의도를 품고 찾아온 놈들을 살려 두고 싶지는 않지만, 배후는 반드시 알아내야 했다.

나는 머릿속에 떠오르는 이름들을 천천히 읊었다.

“백상. 흑웅. 요희. 이 중에 너희들의 주인이 있다면 당장 실토해라. 또 다른 누군가가 시켜서 한 일이라면, 그것 역시 아는 대로 털어놓고.”

도대체 누구일까. 의심만 갈 뿐, 확정 지을 수 있는 사람이 없었다.

다만 내궁에서 이런 일을 벌일 정도로 대담하며, 이만한 전사들을 습격에 동원할 수 있을 정도의 세력을 지닌 데다가 내 부재를 알아챌 만한 정보력이 있는 이들은 손에 꼽을 만큼 적었다.

‘필시 세 명의 대족장 중 하나겠지.’

그토록 비밀리에 움직였는데 알아차리다니.

누가, 어떻게 알았는지는 모르겠다.

게다가 너무나 절묘한 상황에서의 기습이다.

상황이 이렇다 보니 불과 일각 전 협조를 약속하며 헤어진 흑웅에 대해서도 의심을 품을 수밖에 없었다.

‘이런 식으로 뒤통수를 치기 위해서 만나자고 한 건가? 우선 나를 속이고 화룡각 대원들을 손에 넣어 협박하려고?’

아니면 흑웅을 주시하고 있던 백상, 혹은 요희의 짓일 수도 있었다.

그리고 한 가지 확실한 것은, 이 복면을 뒤집어쓴 습격자들의 입에서 흘러나올 이름이 바로 암천의 주구라는 사실이었다.

“누구냐. 말해라.”

스아아아.

압도적인 기파(氣波)로 놈들을 압박하자, 복면 위로 드러난 이마가 고통스럽게 찡그러졌다.

그리고 다음 순간, 나는 복면에 뒤덮여 있던 놈들의 입 언저리가 들썩이는 것을 볼 수 있었다.

으득.

“……!”

순간 엄습하는 오한. 나는 황급히 지풍(指風)을 날려 놈들의 혈을 짚었지만, 스스로 전신의 심맥(心脈)을 끊은 놈들의 입가에서는 검붉은 핏물이 터져 나오고 있었다.

“그르륵. 컥.”

이런 씨발.
```

## Final English reading copy

```markdown
# Chapter 653

“Are those your friends?”

Sama Pyo burst into laughter and answered in a tired voice.

“No way.”

“Then again, you all seem to be on pretty bad terms for friends.”

I scratched my chin and slowly looked around.

The already ancient pavilion had collapsed, and the weeds growing thickly across the clearing were stained red with blood.

*All right. Situation assessed.*

*What a complete fucking mess.*

In the short time I had been away from the residence, more than twenty corpses had appeared. Even if a snail bride had come to clean the place, she wouldn’t have been enough.[^1] And now we had a nighttime ambush on top of it.

I glanced at the assassins, who had hesitated at my appearance, then shrugged at Sama Pyo.

“Oh, you’re doing a little better than I expected.”

Sama Pyo’s upper body was drenched in blood. He answered between rough breaths.

“Yeah, I’m doing pretty well. For an unorthodox goon.”

In truth, I felt bad calling him an unorthodox goon anymore.

They had been completely outnumbered. And the fact that they had fought this hard against enemies of considerable skill meant they had truly staked their lives on it.

I nodded inwardly, impressed.

“You’ve done enough that it feels wrong to keep treating you like some lowly goon from the unorthodox faction… From now on, I’ll call you an unorthodox hardcase.”

“Unorthodox hardcases. How kind of you.”

“Oh, you’re grateful? Unexpected. I thought you’d start cursing me the moment you heard it.”

“You need energy to curse. And I feel like I’m about to collapse, so stop talking to me.”

I let out a short laugh at his honest answer and opened my mouth.

“Then collapse.”

“What?”

“I said collapse. Don’t worry about what comes after.”

“Damn it. You should’ve said that sooner…”

His words trailed off as his eyes began to close. At the same time, Sama Pyo’s body slowly tilted to the side, and I stepped toward him.

Whoosh. Thud.

The three-zhang gap vanished in an instant.

The moment I caught him before he could pitch face-first into the ground, a sharp whistle split the air and a gust of wind whipped up.

Whoosh!

It happened behind me, but I could see it. No—I could sense and read everything through my sharpened instincts.

Now that I had stepped into a new space, this place was practically my domain.

Crack!

Without even turning around, I swung one fist. Something shattered beneath it. A masked man whose head had been crushed like tofu slammed into a pool of blood.

Splash.

Sticky blood sprayed through the air and soaked my back. Ignoring it, I laid Sama Pyo down on relatively clean ground, then suddenly raised my head.

The masked men stood frozen like stone statues.

“But why are you all standing there? That was your last chance, at least.”

“……”

“……”

“Why are you so surprised? Were you planning to ding-dong ditch me, you fucking bastards?”

In the suffocating silence, the ten pairs of eyes visible above the masks shook violently.

Then—

Papapap!

Whiiiiing!

A gale far fiercer than the first swept out in every direction.

The masked men who remained were all Peak masters at the level of injuring others with Sword Energy.

Sword, saber, spear, sickle…

Destructive energy poured from each of their weapons, cutting through the air and targeting the vital points throughout my body.

But I watched and read all of it without the slightest fear.

The flow of qi. The direction their weapons were aimed.

And even the faint fear reflected in their wide-open eyes.

That was the end of it. They had already lost this fight.

They had realized that they were nothing more than wolves. And yet they had refused to accept it and charged at a tiger.

*Then I’d better teach them. Teach them that they should have run somehow.*

Dozens of forms flashed through my mind in the span of an instant. I chose the cruelest and most destructive one and moved.

Whoosh! Crunch!

I smoothly twisted my body, and the four weapons that had barely missed me tangled together as they crossed toward one another. I brought down a straightened hand blade on their center.

Slash!

The weapons were cut into pieces by Force.

I slammed my palm into the abdomen of one of the masked men who stood frozen, still clutching his now-useless favored weapon.

*Flame Divine Palm.*

Boom!

Terrible heat burned away the life force inside his body. I lowered my head as he crumpled behind me, smoke pouring from his seven apertures.

Shaaak! Whoosh!

A blow flew from behind me without warning.

But the long sickle that had tried to reap my neck passed through empty air, while the elbow I thrust backward struck the enemy squarely in the chest.

Crack!

The sound of more than a dozen ribs breaking rang out, followed by a dying gasp.

But it was not my strike that took his life. It was the spear thrust by his comrade.

Thrust!

*Look at these bastards. Not a shred of comradeship.*

Clicking my tongue, I grabbed the spearhead protruding from his chest and applied force.

Crack!

If my opponent was a Peak master who had reached the level of injuring others with Sword Energy, then I was a Supreme Peak master who had entered the realm where Sword Energy became Force.

I casually snapped the spearhead off as if breaking a pair of wooden chopsticks, then immediately returned it to its owner.

Whoosh! Thunk!

The result was obvious: instant death.

The masked man with the spearhead embedded between his brows collapsed without even managing to scream. The remaining masked men swallowed their gasps after losing three comrades in a span too short to even call a moment.

*Seven left.*

I calmly counted the enemies and stepped forward.

Whoosh!

Space disappeared along with the wind, and a new enemy appeared right in front of me.

No—I was the one who had approached.

“……”

His wide eyes seemed to be trying to say something, but it was already too late. I tightened the hand clamped around his neck.

Crack!

*Six.*

I felt the life drain from his body as it went limp all at once.

I naturally snatched the sword from his hand and sent it flying toward the nearest enemy.

“Hng!”

With a breath that sounded like he had been scared out of his soul, the enemy raised a curved moon saber diagonally.

The sword I had fired in a straight line collided with the moon saber, which was imbued with saber qi.

Boom!

The ground flipped over with a deafening roar. A staggering figure emerged through the dust billowing into the air.

The moon saber had shattered because it could not withstand the energy contained in the sword, and dozens of fragments were embedded throughout the man’s body.

“Grrk. Grrr…”

Thud.

Perhaps because the largest fragment had pierced his throat, he collapsed with blood bubbling in his throat without managing to leave even a last word.

I pushed aside the corpse of the enemy whose neck I had broken and spoke quietly.

“Five left.”

“……”

“……”

I could feel it—the fear filling the suffocating silence.

Five Peak masters had fallen in the span of mere moments, and I was stalking my next prey without a single wound.

“Who wants to come next?”

No one answered my question.

Then the masked men, frozen in place and staring at me with eyes wide as if they had seen a ghost, chose to target someone else instead of me.

Papap!

Of the five remaining men, three targeted me, while the other two targeted Namho and Taishan.

I admitted it. That was probably the best choice available to them.

But regardless of my opinion, the result of that choice could not be called their best.

“I saw it clearly! Those bastards ate both chicken legs!”

“Legs? Not wings, but legs? And both of them?”

Taishan blinked in disbelief at Namho’s shout, then pulled the two-section staff hanging at his side free.

“Two chicken legs! You crossed the line! You are not human!”

We would have needed to hold a vote to determine who was not human, but Taishan made the vote itself meaningless with his enormous two-section staff.

Wham! Crack!

His innate divine strength was more than enough to render even a defense useless.

One of the masked men instinctively raised his sword to block the two-section staff. Both his wrists broke, and before he could even scream, his head was smashed together with that of the other man.

Crack!

Two corpses rolled across the ground without managing to utter a dying cry.

Namho, who had been hiding behind Taishan, clenched his fist and shouted.

“That’s right! You commendable bastard I could just kill!”

“Uaaaaaah! Taishan is commendable!”

“Well done! You goddamn bastard! You’ve done nothing but stuff yourself to death every day, and you finally decided to earn your keep!”

I let out a short laugh as I watched Namho heap abuse on him—though I could not tell whether it was an insult or praise—then spoke to the remaining enemies.

“All right. Three left.”

“……”

“……”

“……”

The corners of the masked men’s eyes trembled as they understood what I meant.

Even while their comrades were dying one after another, they had been backing away without daring to attack me.

“I’m telling you this just in case, but if you run, you’ll die. Of course, unlike your friends who went sightseeing at Mount Beimang first, you’ll die much more painfully after lingering a long time before your breath finally stops.”

Someone’s throat bobbed visibly.

The men had all watched with their own eyes as their comrades died in front of them. But if they ran, they would end up wishing they could die that way instead.

“But if you surrender here and tell me what I want to know… I’ll keep you alive, no matter what it takes. If you don’t believe me, I’ll even stake my life on it.”

I had no desire to let men who had come here with such intentions live, but I had to uncover who was behind this.

I slowly recited the names that came to mind.

“Baeksang. Heugung. Yohi. If one of them is your master, confess right now. And if someone else ordered you to do this, tell me everything you know about that, too.”

*Who could it be?*

I had suspicions, but there was no one I could identify for certain.

Still, only a handful of people were bold enough to cause something like this in the Inner Palace, powerful enough to mobilize warriors of this caliber for an assault, and well-informed enough to notice my absence.

*It has to be one of the three great chieftains.*

They had moved so secretly, and yet someone had noticed.

I did not know who had learned of it or how.

And on top of that, the ambush had come at an incredibly precise moment.

Given the circumstances, I could not help but suspect Heugung, whom I had parted from barely fifteen minutes ago after he promised to cooperate.

*Did he ask to meet me so he could stab me in the back like this? Was he planning to deceive me first, seize the Fire Dragon Pavilion members, and use them to threaten me?*

Or it could have been Baeksang, who had been watching Heugung, or Yohi.

And one thing was certain: whatever name spilled from the mouths of these masked attackers would belong to a Dark Heaven hound.

“Who is it? Speak.”

Ssssss.

I pressed down on them with overwhelming qi, and the exposed foreheads above their masks creased in pain.

Then, in the next moment, I saw the corners of the masked men’s mouths twitch.

Crunch.

“……!”

A chill swept over me. I hurriedly fired Finger Qi and struck their pressure points, but dark-red blood burst from the mouths of the men who had severed their own heart meridians.

“Grrrk. Cough.”

*Fuck.*

[^1]: A snail bride is a figure from a Korean folktale who secretly does housework for a poor man.
```

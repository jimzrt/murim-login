<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0797.txt",
      "sha256": "0a7314c3d69471e34158be73f4858b6cf16b099a4e0eeed10ab8a071ad6403be",
      "bytes": 13643
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "29d96016c75df4771347410eca22f42dd1bf51d3e7fac5c1f4556d891556c99f",
      "bytes": 1745
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "f5113f320abd9b040c1eb157bd4508b9032719ea117d801020b8de1e57b9075c",
      "bytes": 224305
    },
    {
      "path": "characters/Felix.md",
      "sha256": "c99b09c897b408aec8d3462e7864d3655a9229b2512a6f568c8214abfc4884ea",
      "bytes": 531
    },
    {
      "path": "characters/Huginn.md",
      "sha256": "1c0fcd3bd4a37999462a8f25ae639427e2df9d40eb973acfec66fbfce9d18fac",
      "bytes": 682
    },
    {
      "path": "characters/Michael.md",
      "sha256": "e863c16436d0ee62d82e69b2e4b7cf46cfab64579e5edd8b381187d40222df31",
      "bytes": 820
    },
    {
      "path": "characters/The Prophet.md",
      "sha256": "7dabf465b3ad596776583cc9bc431f8593dbfdef6ecdf82ee6a8ed3c3591265d",
      "bytes": 704
    },
    {
      "path": "characters/Yamamoto.md",
      "sha256": "c6c85ada08985abf76d32fee2c9eed11cf70c9c32eb45cbbadd541fed8cf84ac",
      "bytes": 493
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "50bf01a06a4c17b233b64742faa656a6aa6fc183edb6e81ea863a7c7120f45b2",
      "bytes": 246216
    }
  ],
  "estimated_tokens": 9543
}
-->

# Durable State Update — Chapter 797

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 797. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 797. Profile updates may replace only one
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
  "chapter": 797,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 797,
    "continuity_sources": [797],
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
    "Jin Taekyung is the World Hunter Federation’s Alliance Leader and is pursuing the Main Quest [Cataclysm], which requires him to eliminate The Prophet within an unspecified time limit.",
    "The Prophet is fleeing through the desert under concealment; his plan is incomplete, its missing components are not all gathered, and his search window is closing.",
    "The Prophet suspects the Skeleton King sent the magical eagles that pursued him; they have now disappeared.",
    "The Prophet believes Jin Taekyung is behind the setbacks to his plans and recognizes Jin’s rapidly increasing influence.",
    "Yamamoto Genji and Japanese Self-Defense Forces Hunters are in an unmanned evacuation vehicle in the Middle East when it is attacked; the attackers and outcome are unknown.",
    "The cause of Siegfried Wassmann’s death and the deaths of twenty people found in the desert remains unknown.",
    "The Skeleton King and his undead army remain with Xiao Shen after defeating the desert Monster Wave without casualties."
  ],
  "continuity_sources": [
    795,
    796
  ],
  "open_questions": [
    "Who is the current Prophet, and where is he?",
    "What caused the deaths of Siegfried Wassmann and the twenty people in the desert?",
    "What disappeared from the desert without a trace, as described by the Skeleton King?",
    "What components does The Prophet still need, and what is he preparing?",
    "Who attacked Yamamoto Genji’s evacuation vehicle, and what happened to its occupants?"
  ],
  "safe_through": 796,
  "temporary_decisions": [
    "Keep magical power distinct from mana.",
    "Render 질풍불참 as “Swift No-Show” in the Genji/Switch Strike joke."
  ],
  "version": 1
}
```

## Exact glossary matches

| 철수     | **Cheol Soo**      |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 칭호               | **Title**                      |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 팀장      | **Team Leader**       |
| 탱커      | **tank**              |
| 마법사     | **mage**              |
| 대격변     | **Great Cataclysm**   |
| 도사      | **Daoist**                                                      |
| 필릭스 | **Felix** | British prince and S-rank Hunter. |
| 후긴 | **Huginn** | One of the two ravens associated with Odin in Norse mythology. |
| 미카엘 | **Michael** | Guild Master of Odin Guild. |
| 선지자 | **The Prophet** | Mysterious religious leader directing the terrorist warriors. |
| 무닌 | **Muninn** | One of the two ravens associated with Odin in Norse mythology. |
| 야마모토 | **Yamamoto** | Japanese S-rank Hunter named in post-Leviathan media coverage. |
| 평화 | **Peace Guild** | Guild name. |
| 송이 | **Song-i** | Short form used for Song Song; Taekyung's love interest. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 존슨 | **Johnson** | Co-host of the American talk show that replays Taekyung's viral interview. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 이전 | **Two Halls** | Top-level Murim Alliance organizational grouping. |
| 대마도사 | **Grand Mage** | Title used for Magic Johnson. |
| 마력 | **magical power** | Distinct from mana; the Skeleton King's area of expertise. |
| 실베르트 | **Silbert** | Family name in Michael Silbert. |
| 일본 | **Japan** | Country requesting emergency assistance and under Leviathan's attack. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 미카엘 | 후긴 | Odin Guild Master to personally selected fixer | Huginn | formal, familiar, and commanding | Michael calls Huginn by name while inviting him into the study. |
| 후긴 | 미카엘 | loyal retainer to Guild Master | Guild Master | formal-polite and deferential | Huginn reports the Swiss investigation, accepts Michael's orders, and promises to complete the mission. |
| 필릭스 | 존슨 | prince_to_allied_grand_mage | Mr. Johnson | formal-polite | Felix uses a respectful address while speaking with Magic Johnson. |

## Listed compact profiles

### Felix.md

# Felix (필릭스)

- **Safe through:** Chapter 787
- **Aliases:** Prince Felix
- **Role:** British prince and S-rank Hunter who joins the reinforcement force against the Arch Lich.
- **Personality:** Haughty and conscious of royal duty, but increasingly willing to set aside convention and connect with allies as equals.
- **Voice:** Formal, lofty, and aristocratic.
- **Relationships:** Travels with Faye Chen and Magic Johnson and is allied with Jin Taekyung.

### Huginn.md

# Huginn (후긴)

- **Safe through:** Chapter 795
- **Aliases:** None
- **Role:** Huginn is a powerful Odin Guild operative and elite fixer personally selected and trained by Michael, now held captive by Jin Taekyung.
- **Personality:** Polished, condescending, calculating, overconfident, and absolutely loyal to his Guild Master.
- **Voice:** Formal and gentlemanly in presentation, indirect and theatrical at first, then blunt and coercive when delivering an ultimatum.
- **Relationships:** Huginn serves Odin Guild's Guild Master with absolute loyalty and acts as an adversary to Jin Taekyung and Choi Minwoo.

### Michael.md

# Michael (미카엘)

- **Safe through:** Chapter 796
- **Aliases:** None
- **Role:** Michael Silbert was the former Odin Guild Master, executed by Jin Taekyung after the World Hunter Federation’s first resolution.
- **Personality:** Controlled, calculating, condescending, and confident in his intelligence and ability to manipulate events, but increasingly impatient and anxious since learning of Jin Taekyung.
- **Voice:** Polite and conversational when relaxed, but quietly authoritative and coercive when asserting control.
- **Relationships:** Michael personally selected and trained Huginn, commands Odin Guild's hidden alliance, secretly confers with The Prophet, and regards Jin Taekyung's friendship with the monster as his fatal weakness.

### The Prophet.md

# The Prophet (선지자)

- **Safe through:** Chapter 796
- **Aliases:** Muninn (무닌)
- **Role:** The Prophet is the mysterious leader of the revived Hasasin, a Middle Eastern terrorist organization preparing further attacks against apostates and Western heretics.
- **Personality:** Religiously fervent, commanding, and shrouded in an intentionally indistinct identity.
- **Voice:** Mysterious, genderless, and age-indeterminate, speaking in solemn religious imperatives.
- **Relationships:** The Prophet commands the ten warriors, is revered by the followers, and secretly communicates with Michael Silbert through a magic mirror.

### Yamamoto.md

# Yamamoto (야마모토)

- **Safe through:** Chapter 796
- **Aliases:** None
- **Role:** Yamamoto Genji is a Japanese S-rank Hunter whose delayed arrival during the Leviathan incident became a subject of post-raid media discussion.
- **Personality:** Prideful and easily offended, he is prone to self-aggrandizement and paranoid, self-serving assumptions.
- **Voice:** Not established.
- **Relationships:** Not established.

## Korean source

```text
＃797화



본대 지휘부는 불과 며칠 만에 편성된 것치고는 짜임새 있는 체계와 엄청난 전력을 구축할 수 있었다.

세계 헌터 연맹을 주축으로 G20에 속한 강대국들이 가장 먼저 힘을 보탰고, 대격변을 겪으며 정예군으로 거듭난 UN 평화 유지군까지 합류한 상황.

그런 의미에서 지금 이 순간 전략실에 집합한 이들은, 이 거대한 유기체를 움직이는 머리이자 손발이라 할 수 있었다.

“그러니까…….”

한동안 아무 말 없이 내 설명을 듣고 있던 척 헤이글이 천천히 말을 이었다.

“저 퍽킹 테러리스트가, 처음부터 미카엘 실베르트의 뒤를 닦아 주던 놈이다?”

나는 망설임 없이 고개를 끄덕였다.

“네.”

“그놈이 하는 말을 믿나? 후긴 말이야.”

“미쳤습니까? 그런 새끼를 믿게.”

“그럼?”

“놈이 가진 두려움을 믿습니다.”

나를 물끄러미 바라보던 척 헤이글이 시가를 털었다.

“사실인가 보군.”

“적어도 저는 그렇게 느꼈습니다.”

“확신하는 건가?”

“100%는 아니고, 95% 정도. 아무리 후긴이어도 지금 같은 상황에서까지 거짓말을 할 이유는 없으니까요.”

“남은 5%는?”

“칼 들고 면회 중인 분들이 채우고 있겠죠. 아마 지금쯤이면 97%쯤 됐을지도 모르겠네.”

처음 한 번이 어렵지, 그다음부터는 쉽다. 실토를 시작한 이상 후긴은 자신이 아는, 혹은 잊고 있던 기억까지 몽땅 끄집어낼 것이다.

단단한 사람을 무너트리는 것은 고통이 아니라 마음속 두려움 그 자체니까.

‘물론 그 전에 실컷 고문당하겠지만.’

이 자리에 모인 이들도 충분히 짐작하고 있겠지만, 누구도 입 밖으로 소리 내어 말하지 않았다.

지금 우리에게 있어 가장 중요한 것은 걸레짝이 되어 가고 있을 후긴이 아니라 앞으로의 대책이다.

놈이 실토한 모든 것이 진실이라는 가정하에 전략을 새로 수립해야 한다.

저 미친 광신도는 단순한 테러리스트가 아니라, 대마도사를 단신으로 처치할 만큼 뛰어난 실력자니까.

“실력으로 치자면 어느 정도겠습니까?”

최 팀장의 신중한 질문에 척 헤이글이 입맛을 다셨다.

“판단하기 어려워. 놈에 대해 드러난 정보가 없는 거나 마찬가지니까.”

“미스터 헤이글. 실례되는 질문일 수도 있겠지만, 만약 당신이 선지자와 같은 조건에서 지크프리트 바스만을 노렸다면 어땠겠습니까?”

“나야 친하진 않더라도 면식이 있는 상태니까 손쉽게 처치할 수 있었겠지. 하지만 지크프리트의 폐쇄적인 성향을 생각한다면, 글쎄. 거의 불가능에 가까워.”

“그렇다면 혹시…….”

“둘 중 하나겠지. 지크프리트가 제대로 된 대처조차 할 수 없을 만큼 엄청난 실력을 지녔거나. 아니면…… 놈의 정체가 지크프리트와 일면식이 있는 누군가거나.”

“……!”

“……!”

폭탄 같은 한마디에 전략실 내부가 차갑게 얼어붙었다.

척 헤이글이 한 말의 의미는 그만큼 무겁고 충격적이었다.

전자와 후자.

선지자가 둘 중 어디에 해당하는 인물인지는 모르겠으나, 지금껏 예상하던 범위를 아득히 뛰어넘는 강자라는 뜻이니까.

“그런 의미에서 진의 판단이 정확했어. 분산되어 있다가는 각개격파 당하기 딱 좋지. 물론 선지자가 그 정도의 강자라면 수백 명이 모여 있어도 무용지물이겠지만.”

맞는 말이다. 전략 병기나 다름없는 S급 헌터 사이에도 격차는 분명히 존재하니까.

비록 가능성은 희박하지만, 만약 선지자가 미카엘 실베르트와 비견되는 강자라면…… 평균적인 수준의 S급 헌터 셋이 동시에, 그것도 뒤를 받쳐 주는 전력이 있어야 쓰러트릴 수 있을 것이다.

‘문제는 그 정도의 실력자가, 도대체 어디서 불쑥 튀어나왔냐는 건데.’

아무리 생각해도 모르겠다.

이미 내부 청소를 깔끔하게 끝마친 세계 헌터 연맹은 현존하는 S급 및 모든 주요 헌터들의 위치와 상황을 파악하고 있는 상황.

‘내부인은 아니다. 그렇다면?’

알려지지 않은 외부인. 그것도 후긴에게 들은 정보를 종합해 보면 길어 봤자 최근 오 년 전에 등장한 외부인이다.

놈이 선지자를 본 것은 삼 년 전이 처음이었지만, 네 번째 무닌을 마지막으로 본 것은 오 년 전이니까.

반면 지크프리트 바스만은 대격변에서 숱한 전투를 치른 베테랑 중의 베테랑. 그가 제아무리 학구형 마법사라지만, 대마도사라는 칭호는 책과 연구만으로 얻을 수 있는 것이 아니다.

아무리 선지자의 재능이 뛰어날지라도 그 사이에는 메울 수 없는 간극이 존재한다.

몇 년 전, 갑작스럽게 하늘에서 뚝 떨어진 애송이는 죽었다 깨어나도 극복할 수 없는 격차가.

아니, 있긴 하다.

내가 바로 그 격차를 극복한 산증인이니까.

“시스템……?”

“응?”

“아닙니다. 그냥 혼잣말이었어요.”

눈썹을 치켜뜨는 척 헤이글의 모습에, 나는 아무렇지 않은 양 자연스럽게 화제를 돌렸다.

“그보다 철수 진행 상황은 어떻습니까?”

최 팀장이 대답했다.

“현재로서는 수색 중이던 인원 중 7할 이상이 복귀 완료했습니다.”

“생각보다 빠르네요.”

“보유한 모든 수송 수단을 총동원했으니까요. 매직 존슨과 파이 첸, 필릭스 왕자에게도 상황을 전달하고 수색팀 전원 철수를 최우선 명령으로 하달했습니다.”

작전 본부는 이곳이지만, 다른 이들 역시 각자의 능력에 따라 일군(一群)을 맡았다.

이 광활한 땅을 샅샅이 뒤지기 위해서는 분산이 필요했다.

그 많은 수색팀이 매번 복귀를 위해 수천, 수만 킬로미터의 거리를 이동하는 건 멍청한 짓거리니까.

“A1팀도 전원 복귀 완료했습니다.”

“B2팀은 아직 복귀 중입니다. 다만 15분 안에 도착할 것으로 추정 중이며, 계속해서 교신 중입니다.”

“D4팀과는 잠시 교신이 중단된 상태입니다. 마력으로 인한 전파 방해로 추측되며, 만약의 사태를 대비하여 지원팀을 출동시켰습니다.”

최 팀장을 시작으로 곳곳에서 보고가 빗발쳤다.

아직 본부 소속의 수색팀 중 일부가 미복귀했거나 교신이 닿지 않고 있었지만 당장 별다른 걱정은 없었다.

마력 분포도가 상승할수록 마나 통신이나 전파가 흐려지는 것은 자연스러운 현상.

또 설령 몬스터 웨이브 같은 불미스러운 일이 발생하더라도 ‘그 녀석’이라면 문제없이 처리할 수 있을 테니까.

삐빅.

― 긴급 교신, 긴급 교신. F6팀 발신. 전방에 몬스터 군단 출현. 몬스터 유형은 언데드로 추정됨. 지원 요청 바람.

“…….”

“…….”

시선이 마주친 나와 최 팀장이 동시에 한숨을 내쉬었다.

“공격하지 말라고 해요.”

“그, 아마도 아군입니다.”

무전이 울리자마자 자리에서 벌떡 일어났던 척 헤이글이 똥 씹은 표정으로 물었다.

“빌어먹을, 혹시 지금 내가 생각하고 있는 그놈인가?”

“예, 현재 F6팀의 좌표상 그가 확실할 겁니다. 아마도 헷갈린 모양이에요.”

“애들 겁주지 말라고 해. 아직 실제로 본 적이 없는 놈들도 많아서 쓸데없이 혼선이 일어날 수도 있으니까.”

“스켈레톤 킹도 충분히 감안하고 움직일 테니 너무 걱정하실 필요는…….”

삐비빅!

― 긴급 교신! 긴급 교신! 몬스터가 너무 많다! 네임드로 추정되는 보스 몬스터가 미친 듯이 웃고 있다! 무섭다! 지원 요청 바람!

“…….”

추가 무전을 들은 척 헤이글이 짜게 식은 눈빛으로 우리를 바라봤다.

슬쩍 시선을 피한 최 팀장이 혼잣말처럼 중얼거렸다.

“다치는 사람은 없을 겁니다. 아마도…….”

“뒤에 덧붙인 말이 자신 없어 보이는데. 착각인가?”

“예.”

나는 한숨을 푹 내쉬었다.

이 새끼는 애들 좀 챙겨 오라고 보냈더니, 오히려 겁을 주고 있네.

주위에 빙 둘러앉은 수뇌부의 시선을 보아하니, 선지자 이전에 스켈레톤 킹부터 조져야 하는 거 아닌지 고민하는 게 분명하다.

‘오면 뒤졌다.’

내심 중얼거린 그때, 다시 한번 다급한 무전이 울려 퍼졌다.

삐빅.

― 교전 발생! 교전 발생!

“또?”

진짜 뒤졌다.

하지만 스켈레톤 킹을 어떻게 조져야 잘 조졌다고 소문이 날까 고민하는 내 귓가에, 예상치 못한 뒷말이 이어졌다.

― J1팀에서 알린다! 현재 사망 다수! 부상 다수! 최대한 빨리 지원, 끄아아악!

콰득. 촤아아악!

등골을 타고 흐르는 싸늘한 한기.

섬뜩한 파육음과 비명이 무전기를 통해 울려 퍼짐과 동시에, 나를 비롯한 전략실의 모든 사람들이 자리를 박차고 일어났다.

“Fuck!”

“발신 좌표 파악해! 지금 당장!”

“경보 울려! 좌표상 가장 가까운 곳에 위치한 수색팀 즉시 파견해!”

“P3, P4팀이 35km 이내에서 이동 중입니다!”

“명령 하달해! 어서! 스켈레톤 킹에게도 지원 요청하고!”

위이이이잉!

스피커를 타고 터져 나온 경보음이 깊은 어둠을 비집고 퍼져 나간다.

열린 창밖으로 몸을 던져 허공으로 높게 솟구친 나는, 저 멀리서 번쩍이는 섬광을 확인하고 공력을 끌어 올렸다.

파앙!

전신을 스치는 바람에, 비릿한 혈향(血香)이 스며 있는 듯했다.



* * *



후웅, 펑!

묵직한 파공성과 함께 뼈와 살이 터져 나간다.

목이 사라진 시체가 털썩 무릎을 꿇자, 사방에서 분노가 실린 외침이 터져 나왔다.

“안 돼! 하루카!”

“네놈이 감히!”

쉬쉬쉬쉭!

휘몰아친 칼바람이 어둠을 가른다. 풍압에 휩쓸려 솟아오른 모래를 베고, 소중한 동료를 죽인 적을 난도질했다.

아니, 그럴 수 있을 것이라 생각했다.

그들의 발밑에서 솟구친 모래가, 거대한 송곳이 되어 몸뚱어리를 관통하기 전까지는.

푸푹! 콰드드득!

“크륵.”

“커……헉!”

단말마(斷末摩)와 함께 검붉은 핏물이 모래를 적신다.

수백이 일백으로, 일백이 수십으로 줄어들기까지 걸린 시간은 불과 십여 분 남짓.

그 광경을 두 눈으로 똑똑히 지켜본 사람들은 뼛속 깊이 사무치는 공포에 몸을 떨었고, S급 헌터인 야마모토 겐지도 예외는 아니었다.

‘이건, 이건 말도 안 돼.’

질풍불참이니, S급 청소부니 하는 소리를 들어도 결국 그 역시 적지 않은 횟수의 전투를 치른 베테랑 헌터다.

하지만 그런 야마모토 겐지에게도 지금처럼 참혹하고, 일방적인 전투는 처음이었다.

압도적인 힘. 파괴. 공포.

혹은 그가 아는 어떤 단어로도 표현할 수 없는 격차가, 놈에게는 있었다.

겁에 질려 도망칠 수조차 없을 만큼. 뽑아 든 검을 휘두를 수조차 없을 만큼.

“넌, 너는…… 도대체 뭐지?”

서걱!

대답 대신 보이지 않는 바람이 또 하나의 생명을 베어 가른다.

비명과도 같은 고함을 내지르며 달려들었던 탱커가 커다란 타워 실드와 함께 반으로 갈라지자, 어둠 속에서도 선명한 핏물이 허공으로 흩뿌려졌다.

촤아아악. 투두둑!

깊은 밤, 흐릿한 달빛.

그리고 소나기처럼 쏟아지는 핏물 사이로 우뚝 서 있는 한 존재.

사락.

긴 로브 자락이 피에 젖은 모래알을 스치며 돌아선 순간, 야마모토 겐지는 불현듯 기습해 온 적의 정체를 깨달았다.

“서, 선지자……!”

깊게 눌러쓴 로브 아래로 드러난 입꼬리가 부드럽게 솟구친다.

다음 순간, 선지자가 내뻗은 양손이 갈퀴처럼 허공을 내리그었다.

쏴아아악! 서걱!

공간이 일그러졌다고 느낀 것은 착각이었을까.

야마모토 겐지는 멍하니 주위를 둘러보았다. 얼굴이 날아가고, 가슴 한가운데가 뻥 뚫리고, 사지가 날아간 시체가 사방에 가득했다. 어느새 살아 있는 것은 오직 그 하나뿐이었다.

적어도 이 순간에는.

‘죽는다. 틀림없이.’

누구에게나 평등한 것. 죽음에 대한 공포.

저벅.

야마모토 겐지는 자신도 모르게 뒷걸음질 쳤다. 식은땀으로 축축한 손아귀에서 검 자루가 미끄러지는 줄도 몰랐다.

아니, 신경 쓰지 않았다.

살 수만 있다면. 살아서 일본으로 돌아갈 수만 있다면.

하지만 다음 순간, 처음으로 듣는 누군가의 목소리가 그의 귓가를 파고들었다.

“어딜 그리 바삐 가느냐, 어리석은 종아.”

“……!”

그리고 야마모토 겐지가 석상처럼 굳어 버린 그때.

“저기다!”

“누군가 있습니다!”

“포메이션 준비!”

부우우웅.

수송 차량의 엔진음과, 사람들의 고함이 사방에서 울려 퍼졌다.
```

## Final English reading copy

```markdown
# Chapter 797

Though the main force’s command had been assembled in only a few days, it had established a well-organized system and amassed tremendous fighting strength.

The World Hunter Federation had taken the lead, with the Great Nations in the G20 among the first to contribute their strength. Even the UN peacekeeping forces, reforged into elite troops through the Great Cataclysm, had joined them.

In that sense, the people gathered in the strategy room at this very moment were the head and limbs that made this massive organism move.

“So…”

Chuck Hagel, who had listened to my explanation in silence for a while, spoke slowly.

“That fucking terrorist was the one who’d been covering Michael Silbert’s ass from the very beginning?”

I nodded without hesitation.

“Yes.”

“Do you believe what he says? Huginn, I mean.”

“Am I crazy? I’m not going to trust a bastard like that.”

“Then what do you believe?”

“The fear he feels.”

Chuck Hagel studied me for a moment, then tapped the ash from his cigar.

“Sounds like it’s true.”

“At least, that’s how it felt to me.”

“You sure?”

“Not a hundred percent. Maybe ninety-five. Even Huginn has no reason to lie in a situation like this.”

“What about the remaining five percent?”

“The people currently keeping him company with knives in hand will fill that in. Maybe it’s already up to ninety-seven by now.”

The first time was the hard part. After that, it got easier. Now that Huginn had started confessing, he’d drag out everything he knew—or had forgotten he knew.

Pain wasn’t what broke a strong person. It was the fear inside them.

*Of course, he’ll still get plenty of torture before that.*

Everyone gathered here probably had a good idea of what was happening, but no one said it out loud.

What mattered most to us right now wasn’t Huginn, who was probably being reduced to a bloody mess. It was what we’d do next.

We had to draw up a new strategy on the assumption that everything he’d confessed was true.

That lunatic fanatic wasn’t just a terrorist. He was skilled enough to take down a Grand Mage by himself.

“Just how strong are we talking?”

At Team Leader Choi’s cautious question, Chuck Hagel smacked his lips.

“Hard to say. We know next to nothing about him.”

“Mr. Hagel. This may be an impolite question, but if you’d been in the same position as The Prophet and targeted Siegfried Wassmann, how would you have fared?”

“I’d met Siegfried, even if we weren’t close, so I could’ve taken him out easily. But for someone he didn’t know, given how reclusive he was? That’d be close to impossible.”

“Then, could it be…”

“It’s one of two things. Either he was so incredibly strong that Siegfried couldn’t even mount a proper defense. Or…” Chuck Hagel paused. “The Prophet was someone Siegfried had met before.”

“……!”

“……!”

Those explosive words froze the strategy room.

What Chuck Hagel had said was that serious—and that shocking.

The first possibility or the second.

We didn’t know which one applied to The Prophet, but either way, he was far beyond anything we’d expected. He was much stronger than we’d imagined.

“In that sense, Jin’s judgment was right. If we stayed scattered, we’d be easy to pick off one by one. Of course, if The Prophet is that strong, even a few hundred people gathered together might be useless.”

He was right. Even among S-rank Hunters, who were practically strategic weapons, there were clear differences in strength.

It was unlikely, but if The Prophet was comparable to Michael Silbert… it would take three average S-rank Hunters attacking at once, with a supporting force backing them up, to bring him down.

*The problem is, where the hell did someone that strong come from?*

No matter how I looked at it, I couldn’t figure it out.

The World Hunter Federation had already cleaned house. We knew the whereabouts and circumstances of every living S-rank Hunter and all the other major Hunters.

*He’s not an insider. So what is he?*

An unknown outsider. And if I put together what Huginn had told me, this outsider had appeared no more than five years ago.

Huginn had first seen The Prophet three years ago, but the last time he’d seen the fourth Muninn was five years ago.

Meanwhile, Siegfried Wassmann was a veteran among veterans, having fought countless battles during the Great Cataclysm. He might have been a scholarly mage, but no one earned the title of Grand Mage through books and research alone.

No matter how talented The Prophet was, there should have been an unbridgeable gap between them.

A kid who’d dropped out of the sky just a few years ago couldn’t overcome a difference like that, no matter what.

Well, there was one exception.

I was living proof that it could be done.

“The System…?”

“Hm?”

“Nothing. Just talking to myself.”

At Chuck Hagel’s raised eyebrow, I smoothly changed the subject, acting like nothing had happened.

“Anyway, how’s the withdrawal going?”

Team Leader Choi answered.

“So far, more than seventy percent of the people who were out searching have returned.”

“Faster than I expected.”

“We mobilized every transport vehicle we had. We also informed Magic Johnson, Faye Chen, and Prince Felix, and gave top priority to withdrawing every search team.”

This was the operations headquarters, but everyone else was leading their own groups according to their respective abilities.

We had to split up to search this vast region thoroughly.

It would’ve been stupid to make all those search teams travel thousands—sometimes tens of thousands—of kilometers just to report back here every time.

“Everyone from Team A1 has returned.”

“Team B2 is still on its way back. We expect them within fifteen minutes and are staying in contact.”

“We’ve temporarily lost contact with Team D4. We suspect interference from magical power, and we’ve dispatched a support team in case of an emergency.”

Reports poured in from all around the room, starting with Team Leader Choi.

Some of the headquarters’ search teams hadn’t returned yet, or we couldn’t reach them. But there was no immediate reason to worry.

As magical power levels rose, it was natural for mana communications and radio signals to grow hazy.

And even if something unpleasant like a Monster Wave happened, *that guy* would be able to handle it without a problem.

Beep.

—Emergency transmission, emergency transmission. This is Team F6. A monster army has appeared ahead. The monsters appear to be undead. Requesting support.

“……”

“……”

Team Leader Choi and I met eyes and sighed at the same time.

“Tell them not to attack.”

“Uh, they’re probably our allies.”

Chuck Hagel had jumped to his feet as soon as the radio crackled. He asked with a face like he’d bitten into something foul.

“Damn it. Is it that guy I’m thinking of?”

“Yes. Judging by Team F6’s current coordinates, it’s definitely him. They must’ve gotten confused.”

“Tell him not to scare the troops. A lot of them haven’t seen him in person yet. We don’t need pointless confusion.”

“The Skeleton King should take that into account while he’s moving, so there’s no need to worry too much…”

Beep-beep!

—Emergency transmission! Emergency transmission! There are way too many monsters! The boss monster, possibly a named one, is laughing like a maniac! This is terrifying! Requesting support!

“……”

After hearing the additional transmission, Chuck Hagel looked at us with a cold stare.

Team Leader Choi subtly looked away and muttered as if to himself.

“No one will get hurt. Probably…”

“That last bit didn’t sound very confident. Am I imagining things?”

“Yes.”

I let out a long sigh.

I’d sent that bastard to bring the troops back, and now he was scaring them instead.

Judging by the looks on the leadership team’s faces as they sat around us, they were probably wondering if we should deal with the Skeleton King before The Prophet.

*You’re dead when you get back.*

Just as I muttered to myself, another urgent transmission rang out.

Beep.

—Engagement in progress! Engagement in progress!

“Again?”

He was really dead.

But as I wondered how I could deal with the Skeleton King in a way that would make the story of his getting his ass kicked spread far and wide, an unexpected follow-up crackled in my ear.

—This is Team J1! Multiple dead! Multiple injured! Send support as fast as you can, aaagh!

Crunch. Splaash!

A chill ran down my spine.

A gruesome sound of flesh being torn and a scream rang out over the radio. At the same time, everyone in the strategy room—including me—leaped to their feet.

“Fuck!”

“Find the transmitter’s coordinates! Now!”

“Sound the alarm! Dispatch the nearest search team to those coordinates immediately!”

“Teams P3 and P4 are moving within thirty-five kilometers!”

“Get the orders out! Hurry! And request support from the Skeleton King, too!”

Wheeeee!

The alarm blared through the speakers, piercing the deep darkness.

I threw myself out the open window and shot high into the air. When I spotted a flash of light far in the distance, I drew up my internal energy.

Bang!

The wind rushing past my whole body seemed to carry the metallic scent of blood.

* * *

Whoosh. Boom!

With a heavy whoosh of displaced air, bone and flesh burst apart.

The headless corpse dropped to its knees, and furious shouts erupted from every direction.

“No! Haruka!”

“You bastard! How dare you!”

Shing, shing, shing!

A blast of blades sliced through the darkness. They sliced through sand thrown up by the force of their swings, certain they could hack apart the enemy who had killed their precious comrade.

Or so they thought.

Until the sand surging up from beneath their feet became enormous spikes that pierced their bodies.

Thud! Crunch!

“Ghk.”

“Guh…!”

With their final gasps, dark red blood soaked the sand.

Hundreds dwindled to a hundred, and a hundred to dozens. It took only a little over ten minutes.

The people who had watched it all with their own eyes trembled with a fear that sank to the marrow. S-rank Hunter Yamamoto Genji was no exception.

*This… This can’t be real.*

He might have been called Swift No-Show or an S-rank janitor, but Yamamoto was still a veteran Hunter who’d fought in his fair share of battles.

Even for him, this was the most horrific and one-sided fight he’d ever seen.

Overwhelming power. Destruction. Terror.

There was a gulf between them that he couldn’t describe with any word he knew.

He was too terrified to run. Too terrified even to swing the sword he’d drawn.

“What are you… What the hell are you?”

Slice!

Instead of answering, an unseen gust of wind cut through another life.

The tank who’d charged with a scream had been split in two along with his massive tower shield. Blood, vivid even in the dark, sprayed through the air.

Splaash. Thud-thud!

The dead of night. The dim light of the moon.

And one figure standing tall amid the blood falling like a sudden downpour.

Swish.

The long hem of a robe brushed over blood-soaked grains of sand as its wearer turned. At that moment, Yamamoto Genji abruptly realized who the enemy was—the one who’d attacked them by surprise.

“The Prophet…!”

Beneath the low-drawn hood, the figure’s lips curled gently upward.

In the next instant, The Prophet’s outstretched hands raked through the air like claws.

Whooosh! Slice!

Had space itself warped? Or had that just been an illusion?

Yamamoto Genji stared blankly around him. Corpses were scattered everywhere: faces gone, holes punched through the centers of chests, limbs cut off.

Before he knew it, he was the only one still alive.

At least, for the moment.

*I’m going to die. There’s no doubt.*

The one thing equal for everyone: the fear of death.

Step.

Yamamoto Genji took a step backward without realizing it. He didn’t even notice the sword hilt slipping in his sweaty grasp.

No. He didn’t care.

If only he could live. If only he could make it back to Japan alive.

But the next moment, someone’s unfamiliar voice pierced his ear.

“Where are you in such a hurry to go, foolish servant?”

“……!”

Just as Yamamoto Genji froze like a statue—

“Over there!”

“Someone’s there!”

“Get into formation!”

Vrooom.

The roar of transport vehicle engines and people’s shouts rang out all around them.
```

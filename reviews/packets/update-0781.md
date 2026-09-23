<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0781.txt",
      "sha256": "3e304e591494a2fe512a72a9611830efe2083cf72d447b6f73ed0848e0545d86",
      "bytes": 12984
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "aa03f340c6157f3eb1863c491d8de9d1807b3fb578ed43aa05bd88cf7787831a",
      "bytes": 1364
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "d1141814e80b2fb9610ae483c1ba070a6082286f2e06d6c2aaebb97ee1e2636d",
      "bytes": 223318
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "060897ca114be2c9e58d0483d0679801f9a28ba36a48173352e9bb0d9296543f",
      "bytes": 553
    },
    {
      "path": "characters/Fabian.md",
      "sha256": "6429d42ff6e3cd49566d0e139e02622936c638e3f21d1d20f7c327904d29a8ca",
      "bytes": 487
    },
    {
      "path": "characters/Felix.md",
      "sha256": "faa7a42d85324094db88944ac6f084a1c761cfc4d6b4c573168478e7a3e13945",
      "bytes": 464
    },
    {
      "path": "characters/Michael.md",
      "sha256": "0bf6dc316a82f52e7b678d35d0f8cd0a5fe8851f67eef0c5685f13d753508d9f",
      "bytes": 887
    },
    {
      "path": "characters/Southern Heaven Demon Empress.md",
      "sha256": "08e983b717b02cbe06b3b321a70a24021d47c140007acf8fee59f823f5ee7e1e",
      "bytes": 715
    },
    {
      "path": "characters/Team Leader Choi.md",
      "sha256": "bd4408ca1967349b875b86dc0a3485b4c98f536e2553959b05939781a721c09c",
      "bytes": 645
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "94db0ccaf07c837679b7f87b9a78ba95b0663f9720da03df5feccd73c0fb303f",
      "bytes": 242593
    }
  ],
  "estimated_tokens": 9039
}
-->

# Durable State Update — Chapter 781

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 781. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 781. Profile updates may replace only one
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
  "chapter": 781,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 781,
    "continuity_sources": [781],
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
    "Michael Silbert is exposed as someone who absorbs monsters’ magical power to grow stronger while concealing it alongside mana.",
    "Michael recalls that Cheon Taemin once recognized him as a threat; he says Taemin is the only person he fears, but is absent from the gathering.",
    "Michael has awakened a vast power increasingly dominated by darkness.",
    "The Stone King’s identity as a monster has been revealed at the World Hunter Federation gathering, and Jin is protecting him as a friend and comrade-in-arms who saved his life.",
    "Magic Johnson, Chuck Hagel, Faye Chen, Felix, and Choi Minwoo openly side with Jin after Fabian threatens him.",
    "Fabian is the Guild Master of Kronos and an S-rank Hunter active since the Great Cataclysm.",
    "Michael intends to lead the World Hunter Federation and has threatened to seek Jin’s permanent expulsion.",
    "Cheon Taemin remains in a coma and too ill to join the coming war."
  ],
  "continuity_sources": [
    780,
    779
  ],
  "open_questions": [
    "Who will lead the World Hunter Federation, and will its members vote to expel Jin?",
    "What will Michael do now that Jin has exposed his secret and what power has he awakened?",
    "Can Cheon Taemin recover from his coma?"
  ],
  "safe_through": 780,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 최민우    | **Choi Minwoo**   |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 길드      | **Guild**             |
| 길드장     | **Guild Master**      |
| 팀장      | **Team Leader**       |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 파비안 | **Fabian** | Guild Master of Kronos. |
| 필릭스 | **Felix** | British prince and S-rank Hunter. |
| 미카엘 | **Michael** | Guild Master of Odin Guild. |
| 남천마후 | **Southern Heaven Demon Empress** | Title Honglan uses when revealing her identity. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 준이 | **Jun** | Family nickname used in the form Jun's dad. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 존슨 | **Johnson** | Co-host of the American talk show that replays Taekyung's viral interview. |
| 소하 | **Xiao He** | Historical civil official invoked in the same exchange. |
| 국회의사당 | **National Assembly** | Government building visible from the skyscraper. |
| 남천 | **South Heaven** | Dark Heaven power that the Lord of Heaven orders the servants to contact. |
| 마후 | **Demon Empress** | Title used for the Southern Heaven Demon Empress. |
| 균열 | **rift** | The dark rift opening in the cliff behind the Inner Palace. |
| 마력 | **magical power** | Distinct from mana; the Skeleton King's area of expertise. |
| 실베르트 | **Silbert** | Family name in Michael Silbert. |
| 크로노스 | **Kronos** | Guild led by Fabian. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 필릭스 | 존슨 | prince_to_allied_grand_mage | Mr. Johnson | formal-polite | Felix uses a respectful address while speaking with Magic Johnson. |
| 최민우 | 필릭스 | allied_operations_lead_to_prince | Your Highness | polite-formal | Choi greets Felix during the secret meeting. |
| 존슨 | 파비안 | former_comrades_in_arms | Fabian | casual and teasing | Johnson greets Fabian familiarly, then warns him not to act rashly. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 780
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Fabian.md

# Fabian (파비안)

- **Safe through:** Chapter 779
- **Aliases:** None
- **Role:** Fabian is the Guild Master of Kronos, an S-rank Hunter active since the Great Cataclysm.
- **Personality:** Authoritative and quick to condemn perceived betrayal.
- **Voice:** Forceful, accusatory, and declarative.
- **Relationships:** He leads Kronos, has fought alongside Magic Johnson, and opposes Jin Taekyung and the Stone King.

### Felix.md

# Felix (필릭스)

- **Safe through:** Chapter 779
- **Aliases:** Prince Felix
- **Role:** British prince and S-rank Hunter who joins the reinforcement force against the Arch Lich.
- **Personality:** Haughty, self-important, and conscious of royal duty.
- **Voice:** Formal, lofty, and aristocratic.
- **Relationships:** Travels with Faye Chen and Magic Johnson and is allied with Jin Taekyung.

### Michael.md

# Michael (미카엘)

- **Safe through:** Chapter 780
- **Aliases:** None
- **Role:** Michael Silbert is Odin Guild Master and a public hero positioning himself to lead the World Hunter Federation, secretly able to absorb monsters’ magical power while concealing it alongside mana.
- **Personality:** Controlled, calculating, condescending, and confident in his intelligence and ability to manipulate events, but increasingly impatient and anxious since learning of Jin Taekyung.
- **Voice:** Polite and conversational when relaxed, but quietly authoritative and coercive when asserting control.
- **Relationships:** Michael personally selected and trained Huginn, commands Odin Guild's hidden alliance, secretly confers with The Prophet, and regards Jin Taekyung's friendship with the monster as his fatal weakness.

### Southern Heaven Demon Empress.md

# Southern Heaven Demon Empress (남천마후)

- **Safe through:** Chapter 725
- **Aliases:** None
- **Role:** The Southern Heaven Demon Empress was Honglan, the creator of the rift behind the Inner Palace, and was killed after the rift closed.
- **Personality:** Playful, cruel, confident, and casually dismissive of mass death and the suffering of others.
- **Voice:** Light, taunting, amused, and delighted even when discussing murder or imminent catastrophe.
- **Relationships:** She commands and advises Baeksang, treats Jin Taekyung and Yayul Cheok as expendable to the grand plan, and keeps a masked hunting dog whom she trained carefully.

### Team Leader Choi.md

# Team Leader Choi

- **Safe through:** Chapter 779
- **Aliases:** Choi Minwoo (최민우)
- **Role:** Team Leader Choi is Jin Taekyung's meticulous intelligence and operations lead, a trusted ally and natural leader capable of guiding the reestablished World Hunter Federation.
- **Personality:** Calm, pragmatic, meticulous, and emotionally steady under pressure.
- **Voice:** Measured, professional, and reassuring without minimizing responsibility.
- **Relationships:** A trusted ally and operational adviser to Jin Taekyung, and the maternal grandson of Cheon Taemin.

## Korean source

```text
＃781화



구구구궁!

사방을 뒤흔드는 울림.

동시에 빛과 어둠이 뒤섞인 혼탁한 기운이 흘러나와 사방을 잠식하고, 모두의 머리 위로 드리워졌다.

어둡다.

분명 해가 떨어지기에는 이른 시간이건만, 국회의사당 내부는 이미 밤의 첫 페이지에 접어들고 있었다.

휘영청 떠오른 달도, 하늘을 수놓은 별도 없는 밤.

그러나 달빛보다도 흐릿한 안개 속에, 그 어떤 것보다 선명한 존재감을 내뿜는 누군가가 있었다.

저벅. 저벅.

느릿하게 나아가는 발걸음을 따라 공기의 흐름이 바뀐다.

아니, 바뀐 것은 비단 그뿐만이 아니다.

마치 먹물이 번지듯 서서히 검게 물들어 가는 회색빛 눈동자.

백인 특유의 새하얀 피부는 마치 가죽과도 같은 얇은 막(膜)에 감싸져 있었고, 어느새 길고 두꺼워진 전신에서는 전과 비교도 할 수 없는 힘과 탄력이 느껴지는 듯했다.

마치…….

‘인간이 아닌 것처럼.’

그러나 동시에 몬스터도 아니다.

놈의 전신에서 흘러나오는 저 거대한 기운 안에는 분명 마나(Mana) 역시 깃들어 있었으니까.

그럼 나는 저놈을, 미카엘 실베르트를 무엇이라 불러야 할까.

느릿하게 나아가던 발걸음이 이내 멈춘다.

어둠이 찰랑거리는 놈의 눈동자에 경멸 어린 표정을 한 내 얼굴이 비쳤다.

“괴물 같은 새끼.”

아마도 그건 나만의 생각이 아닐 것이다.

수백여 명의 얼굴에 떠오른 경악.

지금 이곳에는 전 세계 각국에서 내로라하는 실력자들이 한자리에 모여 있었지만, 그 누구도 감히 입을 열거나 움직이지 못했다.

그들 한 사람 한 사람이 높은 경지에 올라 있는 만큼, 이 순간 미카엘 실베르트가 발산하는 저 기운이 얼마나 방대하며, 또한 끔찍하리만치 강한지 느낄 수 있었기에.

그와 더불어 앞서 들었던 말의 진정한 의미도 깨달았다.



‘내가 두려워하는 유일한 사람은, 지금 이 자리에 없다.’



나조차도 내심 인정할 수밖에 없었다.

미카엘 실베르트는 결코 광오(狂傲)했던 것이 아니다.

비록 놈이 쌓아 올린 힘의 본질이 더럽고 탁하다 한들, 그 기운의 크기만큼은 지금껏 싸워 왔던 누구와도 비교할 수 없었다.

‘굳이 한 사람을 꼽자면, 바로 남천마후(南天魔后)겠지.’

그러나 둘 사이에는 같으면서도 분명한 차이점이 있다.

남천마후는 ‘균열’로부터 흘러나온 마력을 끊임없이 공급받는다.

반면 미카엘 실베르트는 마력 자체를 마나와 공존시키는 방법을 찾아냄으로써 완전히 자신의 것으로 만들었다.

‘도대체…… 얼마나 많은 마력을 흡수해 왔던 거냐.’

나는 깊게 가라앉은 눈빛으로 미카엘 실베르트를 응시했다.

더 이상 인간도, 그렇다고 몬스터도 아닌 무언가.

어느 절대자의 눈을 피해 장장 수십여 년간 힘을 축적해 온 괴물이 바로 눈앞에 있었다.

지금껏 숨겨 왔던 모든 전력을 아낌없이 드러낸 채.

포식자와도 같은 미소를 띤 놈은 나를 비롯한 모두를 바라보며 굳게 닫혀 있던 입술을 열었다.

“말했잖나. 그가 없는 한, 이제 그 누구도 나를 막을 수 없다고.”

차갑게 얼어붙은 공기와 흔들리는 시선들.

하지만 이 자리에 있는 모든 이들이 미카엘 실베르트의 기세에 압도된 것은 아니었다.

“못 본 사이 농담이 많이 늘었군, 미카엘.”

후우웅.

갑자기 어디선가 바람이 휘몰아친다.

아니, 바람이 아니다. 바람처럼 느껴질 만큼 막대한 마나.

스태프를 쇠파이프처럼 어깨에 걸친 매직 존슨의 등 뒤에서 자욱한 연기가 솟아올랐다.

치지직.

이제는 끄트머리만 남은 시가가 군홧발에 짓이겨진다. 니코틴 보충으로 생기를 되찾은 척 헤이글이 가래를 탁 뱉었다.

미카엘 실베르트를 노려보는 그의 눈동자에서는 화염이 줄기줄기 쏟아지고 있었다.

“지금 했던 말, 다시 한번 지껄여 봐라. 이 빌어먹을 네오 나치 같은 새끼야.”

그뿐만이 아니다.

파이 첸은 이미 활시위를 걸었고, 필릭스 왕자는 기품이 묻어나는 자세로 화려한 보석이 장식된 롱소드를 빼 들었다.

하지만 최 팀장의 행동은 그들과 달랐다.

스릉.

그는 마침내 검집에서 빠져나온 [영웅의 검]을 다른 누군가에게 건넸다.

짤막한 한마디와 함께.

“받으십시오. 저보다는 당신에게 더 어울릴 테니.”

이 예상치 못한 호의에 눈을 깜빡이던 상대는 이내 고개를 끄덕여 감사를 표했다.

그리고 건네받은 검을 말없이 바라보다 문득 입을 열었다.

“지금에서야 하는 말인데…….”

스켈레톤 킹.

망자들의 왕이 미카엘 실베르트를 응시하며 말을 이었다.

“처음 본 그 순간부터 줄곧, 네놈이 마음에 들지 않았다.”

키이잉.

새하얀 이마 위를 가로지른 황금빛 선이 왕관을 그려 낸다.

동시에 그 찬란한 빛과는 어울리지 않는 스산한 기운이 스켈레톤 킹의 전신을 타고 흘렀지만, 이번만큼은 그 누구도 녀석을 향해 무기를 겨누지 않았다.

모든 진실이 밝혀진 지금, 자신들이 쓰러트려야 할 적이 누구인지는 분명했으니까.

츠츠츠츠!

혼탁한 어둠을 베어 가르며 겨누어지는 병장기와 눈부신 광휘(光輝).

하지만 미카엘 실베르트의 얼굴에 맺힌 웃음은 여전했다.

아니, 놈은 오히려 더욱더 짙고 선명해진 미소와 함께 입을 열었다.

“이런, 파비안. 자네도?”

“……!”

난데없이 이름이 호명된 크로노스 길드장이 이를 악물었다.

잘게 떨리는 눈가와 흔들리는 검신.

눈에 띄게 동요하는 그의 모습에 너털웃음을 터트린 미카엘 실베르트는 다른 이들을 향해 고개를 돌렸다.

“크리스토퍼, 페르난두, 조앤, 마르셀, 할리드…….”

차례차례 흘러나오는 거물들의 이름.

미카엘 실베르트의 입술 사이로 튀어나온 불씨는 크로노스 길드장을 시작으로 곳곳으로 번져 나갔다.

하나같이 거대 길드의 주인이거나 S급 헌터이건만, 그들은 이름을 불린 것만으로 석상처럼 굳어 버렸다.

인종, 국적, 성별. 나이.

모든 게 달랐지만, 그들 사이에는 단 한 가지의 공통점이 존재했다.

바로 조금 전까지만 하더라도 미카엘 실베르트를 따르던 지지 세력이라는 것.

그리고 적지 않은 세월 속에 켜켜이 쌓여 온 그들의 관계는, 누구도 짐작할 수 없을 만큼 복잡하고 무거운 것이었다.

“이중 가장 짧은 인연을 따져도 10년을 넘겼으니, 다들 친숙하게 느껴지는군. 자네들도 그렇지 않나?”

대답은 어디에서도 들려오지 않았고, 미카엘 실베르트는 얼어붙은 이들을 향해 웃어 보였다.

“지금 이 모습이 자네들의 선택이라면 말릴 뜻은 없지만…… 모두 다시 한번 생각해 보게. 지금껏 우리가 긴 시간을 함께하며 맺었던 신뢰와 우정에 대해서.”

보이지 않는 동요와 혼란이 퍼져 나가는 것이 느껴졌다.

이건 단순히 정에 호소하는 것이 아니다.

지금 미카엘 실베르트는 자신에게 등을 돌린 이들을 압박하고 있었다.

신뢰와 우정이라는 단어 뒤에 숨어 있는 그림자. 당사자들만이 아는 추악한 비밀을 빌미로.

그렇게 미카엘 실베르트가 던진 불씨는, 이내 사람들의 마음속 깊은 곳에 숨어 있던 두려움과 불안감을 장작 삼아 거세게 타올랐다.

얼마 남지 않은 양심마저 잊게 만드는 놈의 한마디와 함께.

“만약 모든 진실이 세상에 알려진다면, 자네들이 무사할 수 있을까?”

“……!”

“하지만 걱정할 필요 없네. 결국 역사란 승자의 전리품이니까.”

천천히 고개를 돌린 미카엘 실베르트가 나를 바라보며 덧붙였다.

“역사뿐만 아니라, 이 세상 전부가.”

그것이 결정타였다.

그리고 크로노스 길드장을 필두로 무려 전체 인원의 절반에 달하는 헌터들이 일제히 무기를 내린 그 순간.

남의 것처럼 낯선, 차갑게 가라앉은 목소리가 내 입술을 비집고 흘러나왔다.

“그래, 차라리 고맙다. 이런 식으로라도 나와 줘서.”

“뭐?”

미카엘 실베르트의 얼굴에 스친 의문은 그리 오래가지 못했다.

아니, 거의 동시에 터져 나온 누군가의 비명이 놈의 목소리를 집어삼켰다.

“크아아악!”

“커헉!”

서걱, 촤아악!

겹겹이 쌓인 비명 사이로 솟구치는 피 분수.

무기를 내리기 무섭게 사방에서 시작된 기습에, 한발 늦게 사태를 파악한 크로노스 길드장이 고함을 내질렀다.

“이런 개 같은……!”

“나로서도 유감이야, 파비안. 이렇게 되지 않기를 바랐는데.”

어느새 허공에 떠오른 채, 차갑게 대답한 매직 존슨이 스태프를 쥐었다.

우우웅.

파르르 떨리는 공기.

막대한 마나의 흐름과 함께 허공을 수놓은 불과 얼음이 섬광처럼 지상으로 내리꽂혔다.

한때는 전우였던, 그러나 이제는 적이 되어 버린 배신자들을 향하여.

후웅, 퍼버버벅!

“막, 커헉!”

비교적 수준이 떨어지는 A급 헌터 서너 명이 단말마와 함께 무릎을 꿇는다.

그사이 공중의 매직 존슨을 향해 무기를 날리려던 크로노스 길드장은 새로운 손님을 맞이하고 있었다.

“못 본 사이에 완전히 맛이 가 버렸군. 왜 그런 멍청한 선택을 했나, 파비안. 이 병신 새끼야.”

지저분한 군홧발과 몸 전체에서 풍겨오는 매캐한 시가 향.

중년을 넘어 노인에 가까워지는 백인 사내를 마주한 크로노스 길드장이 이를 악물었다.

“척 헤이글.”

결코 만만한 상대가 아니다.

아니, 위험하다.

혹시 아군의 도움을 받을 수 있을까 싶어 돌아봤지만 덧없는 기대였다.

불과 몇 걸음 떨어지지 않은 곳에서 그와 함께 미카엘 실베르트의 편으로 돌아선 S급 헌터들이 또 다른 적들을 맞이하여 고전을 겪고 있었다.

파이 첸, 필릭스 왕자, 그리고 이미 죽은 헌터들을 일으켜 세워 돌격하는 스켈레톤 킹과 최민우까지.

그 신속한 움직임에는, 일체의 망설임도 찾아볼 수 없었다.

“설마 네놈들…… 처음부터?”

“한번 시작한 이상, 뿌리를 뽑아야지.”

광포한 웃음과 함께 척 헤이글이 크로노스 길드장을 향해 달려들었다.

쾅!

격돌과 함께 대기가 터져 나간다.

하지만 이내 사방에서 파도처럼 밀려든 또 다른 굉음과 비명이 그 위를 뒤덮는다. 허공으로 흩뿌려지는 붉은 핏물와 함께.

그래, 적들의 핏물은 붉었다.

몬스터가 아닌 인간의 피.

내가 나고 자란 이 세상에서는 보기 싫었던 그 붉은 피가 국회의사당을, 거대한 원탁을 흠뻑 적시고 있었다.

아마도 그래서일 것이다.

예상했던 상황임에도 이렇게 입맛이 씁쓸하고, 온몸의 피가 들끓는 것은.

스아아아.

단전에 똬리를 틀고 있던 화룡(火龍)이 솟구쳤다.

용암과도 같은 뜨거운 열기가 전신 곳곳으로 스며드는 것을 느끼며, 나는 문득 입을 열었다.

“참 좆 같은 광경이지. 안 그러냐?”

눈앞에서 벌어지는 모든 상황을 뒤로한 채, 그저 말없이 나를 바라보고 있던 미카엘 실베르트가 대답 대신 되물었다.

“지금 벌어지는 이 모든 일이, 설마 자네의 뜻인가?”

“그렇다면?”

“과감한 결단에 박수를 보내지.”

과감한 결단.

그 말이 송곳이 되어 가슴 어딘가를 관통한다.

하지만 나는 내색하지 않고 담담하게 대꾸했다.

“그럼 아가리로만 치지 말고 손뼉을 쳐, 병신아.”

“미안하지만 그건 곤란하네.”

“왜?”

“지금 자네에게 조금이라도 틈을 보이면, 꼭 무슨 일이 벌어질 것 같거든. 물론…….”

미카엘 실베르트가 입가에 맺힌 미소를 지우며 말을 이었다.

“그럴 일은 벌어지지 않겠지만 말일세.”

“글쎄. 정말 그럴까?”

그리고 잠시 침묵이 내려앉은 그 순간.

쉭.

놈과 나 사이에 있던 모든 공간이 지워지고, 거대한 두 개의 기운이 서로를 향해 쏘아졌다.

꽈아아아앙!
```

## Final English reading copy

```markdown
# Chapter 781

*Rumble, rumble, rumble!*

A roar shook everything around us.

At the same time, a murky energy, light and darkness mixed together, poured out, swallowed the room, and hung over everyone’s heads.

Dark.

It was far too early for the sun to have set, yet the National Assembly building had already entered the first page of night.

A night without a bright moon or stars scattered across the sky.

And yet, in the haze—fainter than moonlight—someone radiated a presence clearer than anything else.

*Step. Step.*

The flow of air changed with each slow step he took.

No, it wasn’t only the air that had changed.

His gray eyes were slowly turning black, like ink spreading through water.

The characteristically pale skin of a white man was covered in a thin membrane like leather, and his entire body—now longer and thicker—seemed to radiate strength and elasticity unlike anything he’d shown before.

As if…

*He wasn’t human.*

And yet, he wasn’t a monster, either.

The immense energy pouring from his body clearly held mana within it.

So what should I call that bastard—Michael Silbert?

His slow footsteps finally stopped.

My face, twisted with contempt, was reflected in his eyes, where darkness rippled.

“You monster of a bastard.”

I probably wasn’t the only one thinking that.

Shock spread across hundreds of faces.

The best of the best from countries all around the world had gathered here, but no one dared to speak or move.

Every one of them had reached a high realm. They could feel just how vast—and terrifyingly powerful—the aura Michael Silbert was giving off.

And with it, they understood the true meaning of what he’d said earlier.

*The only person I fear isn’t here right now.*

Even I had to admit it, at least to myself.

Michael Silbert hadn’t been arrogant after all.

No matter how vile and impure the source of his power was, its sheer scale was beyond anything I’d faced before.

*If I had to name one person, it would be the Southern Heaven Demon Empress.*

But the two were alike in one way and clearly different in another.

The Southern Heaven Demon Empress was constantly supplied with magical power flowing from the rift.

Michael Silbert, on the other hand, had found a way to make magical power coexist with mana—and had made it entirely his own.

*Just how much magical power has he absorbed?*

I fixed my eyes on Michael Silbert, my gaze sinking deep.

Something that was no longer human, but wasn’t a monster, either.

A monster that had spent decades building up its power while evading the notice of an absolute being stood before me.

Now, he was revealing every last bit of the strength he’d kept hidden.

With a predator’s smile, he looked at me and everyone else before finally opening his tightly closed lips.

“I told you. As long as he’s not here, there’s no one left who can stop me.”

The air had frozen cold. Eyes wavered around the room.

But not everyone here was overwhelmed by Michael Silbert’s aura.

“You’ve gotten a lot better at joking since I last saw you, Michael.”

*Whoooosh.*

A gust of wind suddenly swept through from somewhere.

No—it wasn’t wind. It was so much mana that it felt like one.

Dense smoke billowed behind Magic Johnson, who had slung his staff over his shoulder like a steel pipe.

*Crackle.*

The last stub of his cigar was crushed beneath a military boot. Chuck Hagel spat out a glob of phlegm, pretending the nicotine had brought him back to life.

Flames streamed from his eyes as he glared at Michael Silbert.

“Say that again. Go on, you damned neo-Nazi bastard.”

And he wasn’t the only one.

Faye Chen had already drawn her bow, and Prince Felix unsheathed an ornate longsword set with brilliant jewels, his bearing full of dignity.

Team Leader Choi, however, did something different.

*Shing.*

At last, the [Hero’s Sword] slid free of its scabbard. He handed it to someone else.

With a brief remark.

“Please take it. It suits you better than it does me.”

The recipient blinked at this unexpected gesture of goodwill, then nodded in thanks.

He silently looked at the sword in his hands before suddenly speaking.

“I’ve been meaning to say this for a while…”

The Skeleton King.

The King of the Dead continued, staring at Michael Silbert.

“From the moment I first met you, I’ve never liked you.”

*Kiiing.*

A golden line crossed the Skeleton King’s pure-white forehead, tracing out a crown.

At the same time, a chilling aura at odds with that brilliant light flowed through his body. But this time, no one raised a weapon against him.

Now that the truth was out, it was clear who their enemy was.

*Shhhhh.*

Weapons and dazzling radiance aimed at Michael Silbert, cutting through the murky darkness.

But the smile on his face remained.

No—he spoke with a smile that had grown even broader and brighter.

“Oh, Fabian. You too?”

“……!”

The Guild Master of Kronos, unexpectedly called by name, clenched his jaw.

His eyelids trembled, and the blade in his hand wavered.

Michael Silbert burst into hearty laughter at his obvious agitation, then turned to the others.

“Christopher, Fernando, Joanne, Marcel, Khalid…”

The names of powerful figures spilled from his lips, one after another.

The sparks that flew from Michael Silbert’s mouth spread from the Guild Master of Kronos to people throughout the room.

Every one of them was either the head of a major Guild or an S-rank Hunter, yet they froze like statues just from hearing their names.

Race, nationality, gender, age.

They were all different, but they shared one thing.

Until just a moment ago, they’d been Michael Silbert’s supporters.

And the relationships they’d built up over so many years were complex and heavy beyond anyone’s imagining.

“Even the shortest of our relationships goes back more than ten years. You all feel like old acquaintances to me. Don’t I to you?”

No answer came from anywhere. Michael Silbert smiled at those frozen in place.

“If this is what you’ve chosen, I won’t stop you… but think it over once more. Think about the trust and friendship we’ve shared all these years.”

I could feel an invisible tremor of unease and confusion spreading.

This wasn’t simply an appeal to their affection.

Michael Silbert was pressuring the people who’d turned their backs on him.

Behind the words *trust* and *friendship* lurked a shadow: the ugly secrets only those involved knew, which Michael was using as leverage.

The spark Michael Silbert had tossed into the room soon blazed into a fire, feeding on the fear and anxiety hidden deep in their hearts.

Then he spoke again, making them forget even the little conscience they had left.

“If the whole truth came out, do you think you’d be safe?”

“……!”

“But you needn’t worry. History is the spoils of the victor, after all.”

Michael Silbert slowly turned his head to look at me and added,

“And not just history. The whole world.”

That was the finishing blow.

And just as Fabian, the Guild Master of Kronos, led nearly half the Hunters in the room in lowering their weapons—

A voice, strange and cold, as if it belonged to someone else, slipped from my lips.

“Yeah. I should thank you, actually. For coming out like this, at least.”

“What?”

The confusion that crossed Michael Silbert’s face didn’t last long.

No—in almost the same instant, someone’s scream erupted and swallowed his voice.

“Argh!”

“Urgh!”

*Slash! Splatter!*

Fountains of blood shot up between overlapping screams.

The ambush began all around us the instant the weapons came down. The Guild Master of Kronos realized what was happening a moment too late and shouted,

“You fucking—!”

“I regret it too, Fabian. I didn’t want things to turn out this way.”

Magic Johnson had already risen into the air. He answered coolly as he gripped his staff.

*Vmmmm.*

The air trembled.

Along with a massive flow of mana, fire and ice filled the sky, then plunged toward the ground like streaks of light.

They were aimed at the traitors who’d once been his comrades-in-arms.

*Whoosh! Thud-thud-thud!*

“St—urgh!”

Three or four A-rank Hunters, relatively weaker than the others, dropped to their knees with dying groans.

Meanwhile, the Guild Master of Kronos, who had been about to hurl his weapon at Magic Johnson in midair, found himself facing a new guest.

“You’ve gone completely off the rails since I last saw you. Why’d you make such a stupid choice, Fabian, you dumb son of a bitch?”

The grimy military boots. The acrid scent of cigars wafting from his entire body.

The Guild Master of Kronos clenched his jaw as he faced the white man, well past middle age and nearing old age.

“Chuck Hagel.”

He was no easy opponent.

No—he was dangerous.

The Guild Master looked back, hoping for help from his allies, but that hope was in vain.

Just a few steps away, the S-rank Hunters who’d turned to Michael Silbert’s side with him were struggling against other enemies.

Faye Chen, Prince Felix, the Skeleton King—who was already raising the dead Hunters and sending them charging—and Choi Minwoo.

There wasn’t a hint of hesitation in their swift movements.

“You bastards… You planned this from the start?”

“Once you start, you have to pull it up by the roots.”

With a ferocious laugh, Chuck Hagel charged at the Guild Master of Kronos.

*Bang!*

The air burst with their collision.

But the next moment, more crashes and screams surged in from every direction like waves, drowning it out. Red blood sprayed into the air.

Right. The enemies’ blood was red.

Human blood, not monster blood.

The sight of that red blood—the one I’d hoped never to see in the world where I was born and raised—was soaking the National Assembly building and the enormous round table.

Maybe that was why, even though I’d expected things to turn out this way, my mouth tasted so bitter and my blood boiled through my whole body.

*Fwoosh.*

The fire dragon coiled in my dantian surged up.

As I felt a heat like molten lava seep through every part of my body, I suddenly spoke.

“Hell of a shitty sight, isn’t it?”

Ignoring everything unfolding right before him, Michael Silbert had been silently watching me. Instead of answering, he asked,

“Are you telling me everything happening right now is by your design?”

“What if it was?”

“I applaud your decisive action.”

*Decisive action.*

The words pierced something in my chest like an awl.

But I kept that to myself and answered calmly.

“Then don’t just flap your gums. Clap your hands, you dumbass.”

“Sorry, but I can’t do that.”

“Why not?”

“Because if I let my guard down even a little around you, I have a feeling something will happen. Of course…”

Michael Silbert’s smile faded as he continued.

“But that won’t happen.”

“Maybe. You sure about that?”

And just as silence fell for a moment—

*Whoosh.*

All the space between us vanished, and two immense forces shot toward each other.

*Kwaaaang!*
```

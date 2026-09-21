<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0606.txt",
      "sha256": "7c70ffadce18c14ea1bb81874960f3e7cb5376ecdfb5717f97c8c34cfed6eafb",
      "bytes": 13320
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "769f66354428ea1fcce179cb7e17a726fdc026eddd5b9bacc6d3c2fe3ddd604d",
      "bytes": 1741
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "b652c8d353493beee32c8077b2fb9decb1846456adfb91aec4b6b7e75b4a6660",
      "bytes": 187474
    },
    {
      "path": "characters/Cheonwoo.md",
      "sha256": "a4958fe651bd99684a87cf1a2b27d180392d0040d3771c7de0c2849a44c640db",
      "bytes": 590
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "58ff2b8b98ce53064b55220d01620bde71c40b5fa7b37024592d5e571ef37965",
      "bytes": 553
    },
    {
      "path": "characters/Go Jun.md",
      "sha256": "373d9b2131878bbad059d8ce8fdb3db6c01d10d122c1990703f55d2f45a02766",
      "bytes": 817
    },
    {
      "path": "characters/Song Cheonwoo.md",
      "sha256": "8bc2eee24f852f79134fa21a222fc9fa566ea52aa6c1ea8cb504ad78df187414",
      "bytes": 1080
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "eeb1d4f8ab87b32e984e1d77cbc520c7415fa90f8506061c604aaf7761719de3",
      "bytes": 187918
    }
  ],
  "estimated_tokens": 9075
}
-->

# Durable State Update — Chapter 606

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 606. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 606. Profile updates may replace only one
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
  "chapter": 606,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 606,
    "continuity_sources": [606],
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
    "Cheon Taemin remains unconscious after more than twenty years and has been moved in his hibernation capsule from Ares Guild's Area A to his former mansion.",
    "Magic Johnson has heavily fortified and concealed Taemin's mansion with layered magic, though additional work is still needed.",
    "Magic Johnson suspects another Grand Mage may know who created the Area A secret space and its magic, and plans to consult the other Grand Mages.",
    "Lee Jungryong and Song Cheonwoo tried and failed to awaken Taemin in the past.",
    "Jin Taekyung, Team Leader Choi, Magic Johnson, and the Skeleton King are keeping Taemin's survival and current location secret.",
    "Team Leader Choi is privately spending time with Taemin after their reunion of more than twenty years.",
    "There are only three Grand Mages in the world.",
    "The Texas incident reported as a Mutated Gate was not a Mutated Gate."
  ],
  "continuity_sources": [
    605
  ],
  "open_questions": [
    "What caused Cheon Taemin's unconscious state and how can he be awakened?",
    "Who created the Area A secret space and its unusually advanced magic?",
    "Did another Grand Mage know about or assist with Taemin's confinement?",
    "What was the true nature of the Texas Gate incident?",
    "What debt does Go Se-won intend to repay to Jin Taekyung, and how will the authorities resolve Jin's charges?"
  ],
  "safe_through": 605,
  "temporary_decisions": [
    "Use maternal grandfather for 외조부 and 외할아버지.",
    "Use Team Leader Choi for 최 팀장.",
    "Use Mutated Gate for 변이 게이트.",
    "Retain Ppoppo as Korean baby-talk for a kiss.",
    "Use Grand Mage for 대마도사."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무신     | **Martial God**               | —              |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 몬스터     | **monster**           |
| 길드      | **Guild**             |
| 팀장      | **Team Leader**       |
| 마정석     | **Magic Gem**         |
| 대격변     | **Great Cataclysm**   |
| 천우 | **Cheonwoo** | Name shown in a Level Window; one of the five current Five Gates scions. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 고준 | **Go Jun** | Personal name of Team Leader Seok; Lee Jungryong's prized Disciple. |
| 송천우 | **Song Cheonwoo** | Ares Guild Director, former third-ranked Korean Hunter, and longtime European regional branch director. |
| 평화 | **Peace Guild** | Guild name. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 준이 | **Jun** | Family nickname used in the form Jun's dad. |
| 석고준 | **Go Jun** | Source full-name form for the established Go Jun, also known as Team Leader Seok. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 존슨 | **Johnson** | Co-host of the American talk show that replays Taekyung's viral interview. |
| 미국 | **United States** | Country associated with the talk show and CNM. |
| 국방부 | **Ministry of National Defense** | Government ministry referenced in Taekyung's comparison about the steady passage of time. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 송천우 | 석고준 | adversary; captor of Song's children | you | shocked and confrontational | Song reacts directly to Go Jun's admission that he took the children. |

## Listed compact profiles

### Cheonwoo.md

# Cheonwoo (천우)

- **Safe through:** Chapter 605
- **Aliases:** None
- **Role:** One of the five current Five Gates of Shanxi scions and a First Rate martial artist present at Honghwa Inn.
- **Personality:** Pampered and contemptuous toward Cheongpung's group as part of the five scions' collective mockery.
- **Voice:** Mocking in the group's exchange; no distinct individual speech is established.
- **Relationships:** Associates with Seongryong, Myeonghwa, Sohye, and Jintae as a group of current Five Gates scions.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 605
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Go Jun.md

# Go Jun (고준)

- **Safe through:** Chapter 604
- **Aliases:** Team Leader Seok
- **Role:** Go Jun was Ares Guild's Vice Guild Master, Lee Jungryong's Disciple and former Head of Security, the de facto successor to Lee's Ares legacy, and a mutated monster who was killed by Jin Taekyung in Area A.
- **Personality:** Disciplined and controlled under ordinary pressure, fiercely loyal to Lee Jungryong, but consumed by humiliation and rage when Ares Guild's authority is challenged.
- **Voice:** Dry, controlled, and formal with subordinates; deferential when addressing his Master.
- **Relationships:** Go Jun inherited Lee Jungryong's Ares legacy after becoming his Disciple and regarded Jin Taekyung and Choi Minwoo as enemies before his death.

### Song Cheonwoo.md

# Song Cheonwoo (송천우)

- **Safe through:** Chapter 605
- **Aliases:** Director Song
- **Role:** Ares Guild Director and former A-rank Hunter who reached third place among Korean rankers, briefly headed the Hunter training center, and led Ares Guild's European regional branch for twenty years; after being forced to attack Choi Minwoo to protect his hostage family, he fell into an abyss and was killed by an unidentified monster.
- **Personality:** Highly ambitious, honor-obsessed, politically calculating, and determined to use his final opportunity to reclaim influence before retirement.
- **Voice:** Not established.
- **Relationships:** Song Cheonwoo followed Cheon Taemin since before Team Leader Choi was born, was Lee Jungryong's former friend and rival, helped conceal Taemin's condition and purge aides who knew the truth, negotiated the European regional director position to save himself and his family, and had his children seized by Go Jun as leverage that forced him to attack Choi Minwoo.

## Korean source

```text
＃606화



변이 게이트가 아니라니. 이건 또 무슨 소리야?

의문은 잠깐이었다. 다음 순간, 매직 존슨이 툭 던진 한 단어를 들은 나는 눈을 크게 떴다.

“테러요?”

「그래, 테러. 범인은 아랍계 남성이었는데, 헌터 라이센스를 위조해서 게이트에 출입하려다가 적발됐지. 문제는 놈의 정체가 중동 테러 집단 소속의 B급 헌터였고, A급 마정석을 소지하고 있었다는 거야. 당연하게도 정화 작업을 거치지 않은 마정석이었지.」

“그거 혹시…….”

「네게는 꽤 익숙한 상황이겠지. 진. 안 그래?」

나는 대답 대신 굳게 입을 다물었다. 머릿속에서는 얼마 전의 기억이 빠르게 스쳐 지나가고 있었다.

석고준. 송천우. 그리고 두 번의 몬스터 웨이브.

두 번 다시 일어나서는 안 되는 일이 끈질기게 이어지고 있었다.

“몬스터 웨이브를 노린 거군요.”

「아마도. 아니, 확실하겠지.」

빌어먹을. 내심 욕설을 중얼거린 내가 다급하게 물었다.

“피해, 피해는요? 혹시 뉴스에서 의도적으로 피해 상황을 숨긴 건…….”

나는 차마 말을 잇지 못하고 말꼬리를 흐렸다.

최근 벌어진 사건들은 그야말로 재앙의 연속이었다.

비록 석고준에 비할 수는 없겠지만 만약 테러 집단 소속의 B급 헌터가 정화되지 않은 A급 마정석을 흡수했다면, 그 자체로도 상당한 피해가 일어났을 것이다.

그리고 그런 내 모습에 매직 존슨은 침착한 어조로 대꾸했다.

「워, 진정해. 진. 뉴스 보도는 전부 사실이었으니까. 천만다행으로 별다른 피해는 없었어.」

“그게 정말입니까?”

「굳이 네게 거짓말을 할 이유가 없지. 안 그래?」

“하지만 어떻게?”

「안 그래도 이번 사건으로 전 세계가 촉각을 곤두세우고 있어. 신분 확인 절차와 마정석 단속도 몇 배는 엄격해졌고, 그 과정에서 걸려든 테러범은 최후의 수단으로 마정석 흡수를 시도했지. 어떻게 됐을 것 같아?」

매직 존슨이 종이컵에 담긴 믹스 커피를 홀짝거리며 말을 이었다.

「결과는 간단해. 놈은 마정석에 담긴 힘을 견디지 못했지. 그나저나 이 커피 맛있는데.」

“아니, 지금 커피가 문제가 아니라. 만약 그랬다면 석고준 때처럼 변이를 일으켰을 텐데요.”

마나(Mana)와 마력(魔力)은 물과 기름처럼 절대 섞일 수 없는 힘이다.

공인받은 S급 헌터이자 현대의 마나 연공법을 익힌 석고준조차 끝끝내 마력을 완전히 흡수하지 못한 것이 바로 그 증거다.

진정한 문제는 그로 인해 일시적으로 폭증하는 힘. 그리고 그 뒤에 기다리고 있을 변이(變異)였다.

‘그런데 결과가 간단하다고?’

별다른 피해가 없었다는 것이 더 이상하게 느껴질 수밖에 없었다.

그리고 다음 순간 들려온 매직 존슨의 대답은 나로서도 예상치 못한 것이었다.

「아니. 터져 버렸어.」

“예?”

「말 그대로야. 산산조각으로 터져 버렸다고. Boom!」

탕탕!

숟가락으로 뚝배기를 두드린 매직 존슨이 어깨를 으쓱해 보였다.

「그리고 모든 게 끝났지. 내가 현장에서 한 일이라고는 폭발의 여파로부터 사람들을 보호하는 것뿐이었어.」

“……!”

「그건 어떤 의미로는, 그래. 확실히 자살 테러라고 부를 만한 일이었지. 하지만 그게 전부였어.」

그 말에 뭔가를 깨달은 나는 내심 중얼거렸다.

‘석고준 때처럼, 이 아니라 그나마 석고준이었기에 가능했던 일이었어.’

처음부터 잘못 생각했다.

이건 결국 그릇의 차이다. 한 사람의 성격이나 도량을 논하는 것이 아니라, 얼마나 많은 힘을 품고 흘러넘치지 않게 유지할 수 있냐는 측면에서 그렇다.

그리고 그런 의미에서 보자면, 죽은 석고준은 충분히 큰 그릇이었다.

놈에게는 마력을 일부 흡수할 뿐만 아니라 잠시나마 유지할 만한 능력이 있었으니까.

‘하지만 석고준조차도 결국 변이를 일으켰지.’

S급 마정석 두 개를 한꺼번에 흡수한 석고준의 그릇은 균형이 깨져 버렸고, 마침내 변이를 일으켰다.

만약 내가 직접 손을 쓰지 않았더라도 놈은 얼마 버티지 못하고 죽음을 맞이했을 가능성이 상당했을 것이다.

‘그러니 평범한 축에 속하는 다른 헌터들은 말할 것도 없었겠지.’

오늘 뉴스의 주인공이 된 테러범은 B급 헌터였음에도 그 힘을 이기지 못하고 현장에서 폭사(爆死)했다.

이건 마정석에 담긴 마력을 조금도 제어하지 못했다는 뜻이다.

「헤이, 진. 이제 좀 감이 잡힌 표정인데.」

나는 빙긋 웃고 있는 매직 존슨을 바라보며 실소를 흘렸다.

“천만다행이네요.”

「다행이지. 이제부터는 어지간한 병신이 아니고서야 오늘 같은 일을 벌이지 못할 테니까.」

매직 존슨의 말은 중요한 흐름을 정확히 짚고 있었다.

이번 테러로 피해가 발생하지 않은 것도 다행이지만, 그보다 더 안도할 만한 일은 뒤에 벌어질 만약의 사태를 예방했다는 것이다.

「테러 집단 쪽에서도 똑똑히 깨달았을 거야. 굳이 냉정하게 말하자면, 이건 놈들 입장에서도 결코 남는 장사가 아니거든.」

훈련받은 헌터는 훌륭한 재원이며, 마정석은 막대한 가치를 지닌 에너지원이다.

테러 집단이 어떤 루트로 정화되지 않은 A급 마정석을 빼돌렸는진 모르나, 오늘 놈들은 보기 좋게 실패했다.

훌륭한 재원과 수십억을 우습게 호가하는 마정석을 허무하게 잃어버린 것이다.

「테러범 놈들도 전략을 수정하겠지. 예전처럼 그 빌어먹을 알라의 요술봉으로 힘없는 민간인들을 노릴 게 분명해. 하지만 방심하기에는 아직 일러.」

작게 한숨을 내쉰 매직 존슨이 말을 이었다.

「사실 요즘 테러 단체의 움직임이 심상치 않아. 특히 아프리카와 중동 지역에서는 게이트나 마정석을 이용한 실험이 이루어지고 있다더군. 펜타곤(Pentagon)으로부터 전달받은 정보라 확실해.」

지금까지 대화에 참여하지 않은 채, 옆에서 스마트폰만 만지작거리고 있던 스켈레톤 킹이 귀를 쫑긋 세웠다.

“펜타곤? 지금 바로 가는 건가? 부비부비 매우 가능인가?”

“……혹시 몰라서 말하는데, 클럽 아니다.”

“이런 제기랄. 드디어 핫걸들을 만나나 했는데.”

꿈도 꾸지 마. 이 자식아…….

펜타곤은 미국 국방부의 본청 청사다.

만약 스켈레톤 킹의 정체가 밝혀진다면 펜타곤의 연구진들이 밤새 파티를 벌일 거다.

물론 철통 같은 경계를 갖춘 실험실에서 온갖 실험 도구로 부비부비를 시도하겠지.

「음. 저 친구를 펜타곤에 데려가면 다들 좋아하긴 하겠군.」

“저나 존슨한테는 별로 안 좋을걸요.”

「그것도 그래. 아마도 국제법 위반으로 재판을 받아야 할걸. 재판 진행 중에 테러 집단이 사고를 친다면 흐지부지될 수도 있겠지만.」

세상 사는 게 이렇게 어렵다.

한 가지 문제를 해결하자마자 또 하나가 튀어나온 걸 보면 알 수 있었다.

‘테러 집단이라.’

석고준이 벌인 일련의 사건들이 세상에 알려지자 전 세계 각국은 충격과 경각심에 휩싸였지만, 테러 집단에게는 또 하나의 무기가 생긴 셈이었다.

매직 존슨이 펜타곤으로부터 입수한 정보가 사실이라면, 놈들은 무슨 수를 써서라도 방법을 찾아낼 것이 분명했다.

“……하필이면 이럴 때.”

내 중얼거림에 매직 존슨의 얼굴 위로 물음표가 떠올랐다.

「하필이면, 이라니?」

“음.”

말할까 말까. 망설이던 나는 고개를 저었다.

“별거 아니니까 신경 안 쓰셔도 돼요.”

「상당히 별거 같고, 엄청나게 신경 쓰이는데.」

“그냥…… 준비하고 있던 일이 있어요. 그런데 존슨의 이야기를 들으니까 지금 당장은 망설여지네요.”

「준비하고 있던 일?」

나는 작게 고개를 끄덕였다.

그건 아직 누구에게도 말하지 않았지만, 이번에 현대로 돌아오며 마음먹은 것 중 하나였다.

나를 위해. 그리고 다른 모두를 위해 오랜 망설임 끝에 결정을 내리고 준비를 해 오고 있었는데…….

‘이렇게 되면 이야기가 달라지지.’

대격변 이후 인류는 평화를 되찾았지만, 전 세계가 평화로운 것은 아니었다.

새롭게 등장한 마나와 각성자들의 존재.

살아남은 강자들은 자신들만의 규칙으로 세상을 재조립했고 끝난 줄 알았던 분쟁은 지금까지도 이어지고 있었다.

‘아니, 오히려 더 심해졌다고들 할 정도니.’

마정석은 석유를 뛰어넘는 가치와 활용성을 지닌 자원이었고, 게이트는 마정석이라는 다이아몬드를 끊임없이 뱉어내는 광산이다.

그러니 이를 둘러싼 분쟁은 끝없이 이어질 수밖에 없었다. 기업가, 길드, 혹은 반군(反軍)이라는 이름으로.

게다가 중동 테러 집단은 더 위험했다.

그들은 각성을 신의 축복으로 여겼으며, 신이 존재한다는 증거 그 자체로 들이밀었다.

무신론자도 각성자가 되는 마당에 그게 뭔 개소리냐 하겠지만, 원래 그런 새끼들한테 논리를 찾는 것부터가 잘못된 거다.



‘신께서 선택한 전사들이여! 진격하라!’

‘신께서 원하신다!’



도대체 어느 신과 교리에서 그런 병신 같은 짓을 하라고 권했는지는 모르겠다.

하지만 가수가 노래를 부르고 대장장이가 쇠를 주무르는 것처럼, 병신들은 병신 짓을 계속해 나가기 마련이다.

병신들은 그렇게 세계 각지에서 싸움을 계속해 나갔고, 죽거나 병신이 되었다.

그리고 그건 지금 이 순간에도 마찬가지다.

‘개 같은 새끼들.’

차라리 스켈레톤 킹이 훨씬 낫다. 비록 시작은 몬스터였을지 모르나 현재에 이르러서는 여느 헌터 못지않은 희생과 헌신을 보여 주었으니까.

‘기특한 녀석.’

그런 마음이 담긴 따뜻한 눈빛에, 스켈레톤 킹이 사나운 눈빛으로 나를 쏘아보았다.

“네놈, 방금 속으로 이 몸을 욕했지.”

“……아니, 어이가 없네.”

“솔직히 말해 봐라. 봐준다.”

“존슨. 이 새끼 그냥 펜타곤 데려가면 안 돼요?”

매직 존슨이 씩 웃으며 대답했다.

「그럴까?」

“들었냐? 넌 이제 끝났다. 이 실험체 새끼야.”

「기왕 이렇게 된 거, 지금 당장 가는 것도 나쁘지 않지.」

“가마솥 준비해 놓으라고 하세요. 이 새끼 사골 좀 끓이게.”

「가마솥은 모르겠고, 실험실은 언제든지 준비되어 있을 거야.」

어째서인지 오늘따라 죽이 척척 맞는다.

천연덕스럽게 내 말을 받아친 매직 존슨이 품에서 스태프를 꺼내며 말을 이었다.

「그럼 식사도 했으니, 슬슬 출발하도록 할까?」

“그거 나쁘지 않…… 잠깐만요.”

반사적으로 맞장구친 나는, 매직 존슨의 스태프를 향해 순환되는 마나의 흐름을 느끼고 떨떠름한 표정을 지었다.

“어, 그럴 필요까진 없는데요.”

「코리아 전통 속담에는 그런 게 있다며? 게이가 한 번 요술봉을 뽑았으면 무라도 뚫어야 한다.」

“……?”

뭔가 이상하고 대단한 쪽으로 확대 해석 된 것 같은데.

난생처음 들어 보는 전통 속담에 혼란스러워하던 나는 침을 꿀꺽 삼켰다.

“아니. 진짜로?”

「그래. 진짜로.」

“농담이 아니라?”

「이틀 전 펜타곤에서 정식 요청이 들어왔어. 진. 네게 자문과 도움을 얻고 싶다더군. 가급적이면 최대한 빨리.」

“예?”

눈을 깜빡이던 나는 허허 웃었다.

“아, 감 잡았다. 이거 미국식 조크네.”

매직 존슨이 심유한 게이의 눈빛으로 나를 응시했다.

「어떻게 알았지? 보여 준 기억이 없는데.」

이게 뭔 소리여. 시벌.

잠시 멍해 있던 내가 황급히 손을 내저었다.

“……아니, 발음을 헷갈렸어요. 조크요. 조크. 개그.”

「알아. 방금은 나도 조크였어.」

흰 이를 드러내며 씩 웃은 매직 존슨이 덧붙였다.

「하지만 펜타곤에 관한 건 조크가 아니야.」

“……!”

「가지. 이미 다른 사람은 준비된 것 같은데. 안 그래?」

나는 매직 존슨의 시선이 향하는 방향을 따라 고개를 돌렸다.

익숙한 인기척과 함께 한 사람의 모습이 시야에 들어왔다.

최 팀장이 가라앉은 목소리로 대답했다.

“물론입니다, 미스터 존슨.”
```

## Final English reading copy

```markdown
# Chapter 606

*It wasn’t a Mutated Gate? What the hell was that supposed to mean?*

My confusion lasted only a moment. The next second, I heard the single word Magic Johnson had tossed out and my eyes widened.

“Terrorism?”

“Yeah, terrorism. The culprit was an Arab man who was caught trying to get into the Gate with a forged Hunter license. The problem was that he was a B-rank Hunter affiliated with a terrorist group in the Middle East—and he was carrying an A-grade Magic Gem. Naturally, it hadn’t undergone purification.”

“That sounds a little…”

“It must be a pretty familiar situation to you, Jin. Am I wrong?”

Instead of answering, I clamped my mouth shut. Memories from not long ago flashed through my mind.

Go Jun. Song Cheonwoo. And two monster waves.

Something that should never happen again had kept happening.

“He was after a monster wave.”

“Probably. No, I’m sure of it.”

*Damn it.*

I cursed inwardly and urgently asked, “What about the casualties? How bad was it? Did the news deliberately hide the damage because—”

I couldn’t bring myself to finish the sentence, and my voice trailed off.

The incidents that had taken place recently had been one disaster after another.

It might not have been comparable to Go Jun, but if a B-rank Hunter from a terrorist group had absorbed an unpurified A-grade Magic Gem, it would have caused considerable damage all by itself.

Seeing my expression, Magic Johnson answered in a calm voice.

“Whoa, calm down, Jin. Everything reported in the news was true. By sheer luck, there wasn’t any significant damage.”

“Are you sure?”

“I have no reason to lie to you. Do I?”

“But how?”

“Everyone around the world has already been on high alert because of this incident. Identity checks and Magic Gem inspections have become several times stricter, and the terrorist was caught during that process. As a last resort, he tried to absorb the Magic Gem. What do you think happened?”

Magic Johnson continued, taking a sip of the instant coffee in his paper cup.

“It’s simple. He couldn’t withstand the power contained in the Magic Gem. By the way, this coffee is pretty good.”

“Forget the coffee. If that happened, he should have mutated the way Go Jun did.”

Mana and magical power were forces that could never mix, like oil and water.

The proof was Go Jun himself—a certified S-rank Hunter who had learned the modern mana cultivation method, yet had ultimately been unable to absorb magical power completely.

The real problem was the temporary surge in power it caused.

And the mutation that waited afterward.

*But the result was simple?*

The fact that there had been no significant casualties felt even stranger.

Then Magic Johnson gave me an answer I never could have expected.

“No. He exploded.”

“What?”

“Exactly what I said. He blew apart into pieces. Boom!”

Bang, bang!

Magic Johnson tapped the earthenware pot with his spoon and shrugged.

“And that was the end of everything. All I did at the scene was protect people from the blast’s aftermath.”

“…”

“In a way, yes. You could definitely call it a suicide attack. But that was all it was.”

At those words, I realized something and muttered inwardly.

*It wasn’t that it was like what happened with Go Jun. It was that what happened with Go Jun had only been possible because it was Go Jun.*

I had been thinking about it wrong from the start.

In the end, it was a matter of the vessel.

Not in terms of a person’s character or breadth of mind, but in terms of how much power they could contain without letting it overflow.

And in that sense, the dead Go Jun had possessed a vessel large enough.

He had been capable not only of absorbing some magical power, but of maintaining it for a short while.

*But even Go Jun eventually mutated.*

Go Jun’s vessel had lost its balance after he absorbed two S-grade Magic Gems at once, and he had finally undergone a mutation.

Even if I hadn’t intervened personally, there was a very good chance he would have died after holding out for only a little longer.

*So ordinary Hunters were out of the question.*

The terrorist who had become the star of today’s news had been a B-rank Hunter, yet he had been unable to withstand the power and exploded on the spot.

That meant he hadn’t been able to control even a little of the magical power contained in the Magic Gem.

“Hey, Jin. You look like you’re starting to get it now.”

I let out a hollow laugh as I looked at Magic Johnson, who was grinning.

“That’s a huge relief.”

“It is. From now on, only a complete idiot could try something like this again.”

Magic Johnson had accurately identified the important trend.

It was fortunate that the terrorist attack had caused no damage, but the greater relief was that it would deter similar incidents in the future.

“The terrorist group must have realized it, too. To put it coldly, this was a terrible trade from their perspective.”

Trained Hunters were valuable assets, and Magic Gems were energy sources worth an enormous amount of money.

I had no idea how the terrorist group had smuggled an unpurified A-grade Magic Gem out, but they had failed spectacularly today.

They had thrown away a valuable asset and a Magic Gem easily worth billions.

“The terrorists will change their strategy, too. Just like before, they’ll probably target powerless civilians with that damn magic wand of Allah. But it’s still too early to let our guard down.”

Magic Johnson let out a quiet sigh before continuing.

“Actually, terrorist organizations have been making some alarming moves lately. Apparently, experiments involving Gates and Magic Gems are being carried out particularly in Africa and the Middle East. The information came from the Pentagon, so it’s reliable.”

The Skeleton King, who had spent the entire conversation fiddling with his smartphone without participating, perked up his ears.

“The Pentagon? Are we going there right now? Is much rub-rub possible?”

“Just in case you’re wondering, it’s not a club.”

“Damn it. I thought I was finally going to meet some hot girls.”

*Don’t even dream about it, you bastard…*

The Pentagon was the headquarters of the United States Department of Defense.

If the Skeleton King’s identity were revealed, the researchers at the Pentagon would hold a party all night.

Naturally, they would try all kinds of rub-rub with every experimental tool imaginable in a laboratory protected by ironclad security.

“Hmm. Everyone would certainly be happy if we took that fellow to the Pentagon.”

“That wouldn’t be very good for you or me.”

“That’s true, too. We’d probably have to stand trial for violating international law. Though if a terrorist group caused an incident during the trial, the whole thing might fizzle out.”

Living in this world was difficult.

I knew that because the moment one problem was solved, another one popped up.

*A terrorist group.*

Once the series of incidents caused by Go Jun became known to the world, every country had been thrown into shock and heightened alertness.

But terrorist groups had gained another weapon.

If the information Magic Johnson had obtained from the Pentagon was true, they would find a way no matter what it took.

“…Of all times.”

A question mark appeared over Magic Johnson’s face at my mutter.

“Of all times? What do you mean?”

“Hmm.”

I hesitated, wondering whether I should tell him, then shook my head.

“It’s nothing. You don’t have to worry about it.”

“It sounds like something, and it’s bothering me a lot.”

“It’s just… there’s something I’ve been preparing. But after hearing what you said, I’m hesitating for now.”

“Something you’ve been preparing?”

I nodded slightly.

I hadn’t told anyone about it yet, but it was one of the decisions I had made after returning to the modern era this time.

For my sake.

And for everyone else’s.

After a long period of hesitation, I had made a decision and had been preparing for it…

*But this changes things.*

After the Great Cataclysm, humanity had regained peace, but the entire world was not peaceful.

The newly emerged mana and the existence of Awakened people.

The powerful survivors had rebuilt the world according to their own rules, and conflicts everyone had thought were over still continued to this day.

*No. Some people would even say they’ve only gotten worse.*

Magic Gems were resources with greater value and usefulness than oil, while Gates were mines that constantly spat out diamonds in the form of Magic Gems.

The conflicts surrounding them could only continue endlessly.

Whether in the name of entrepreneurs, Guilds, or rebels.

And the terrorist groups in the Middle East were even more dangerous.

They considered awakening a blessing from God and held it up as proof of God’s existence.

Someone might ask what the hell that had to do with anything when even atheists could become Awakened, but it was already a mistake to look for logic in people like that.

*Warriors chosen by God! Advance!*

*God wills it!*

I had no idea which god or doctrine had encouraged them to do something so idiotic.

But just as singers sang and blacksmiths worked iron, idiots were bound to keep doing idiotic things.

The idiots continued fighting in every corner of the world, dying or ending up crippled.

And that was still happening at this very moment.

*Bastards.*

The Skeleton King was much better by comparison. He might have started out as a monster, but by this point he had shown as much sacrifice and dedication as any Hunter.

*Good lad.*

At the warmth in my gaze, the Skeleton King glared at me ferociously.

“You just cursed this body in your thoughts.”

“…What the hell? That’s absurd.”

“Tell me honestly. This body will forgive you.”

“Johnson. Can’t we just take this bastard to the Pentagon?”

Magic Johnson grinned and answered.

“Should we?”

“You hear that? You’re finished now, you experimental-subject bastard.”

“Now that it’s come to this, going right away wouldn’t be bad.”

“Tell them to prepare a cauldron. We’ll make some bone broth out of this bastard.”

“I don’t know about a cauldron, but the laboratory will be ready whenever we are.”

For some reason, we were getting along perfectly today.

Magic Johnson casually played along with my remark, then took a staff out of his robes and continued.

“Well, now that we’ve eaten, shall we get going?”

“That doesn’t sound bad… Wait a second.”

I had agreed automatically, but then I felt the mana circulating through Magic Johnson’s staff, and my expression turned uneasy.

“Uh, there’s no need to go that far.”

“There’s a Korean traditional proverb that goes something like this, isn’t there? Once a gay draws his magic wand, he has to pierce even a radish.”

“…?”

Somehow, that had been twisted into something strange and impressive.

Confused by the traditional proverb I was hearing for the first time in my life, I swallowed hard.

“Wait. Seriously?”

“Yeah. Seriously.”

“You’re not joking?”

“Two days ago, the Pentagon sent an official request. Jin, they want to receive your advice and help. Preferably as soon as possible.”

“What?”

I blinked, then let out a hollow laugh.

“Oh, I get it now. This is an American joke.”

Magic Johnson stared at me with the profound gaze of a gay man.

“How did you know? I haven’t shown you that memory.”

*What the hell is he talking about? Fuck.*

I stood there blankly for a moment before hurriedly waving my hands.

“…No, I got the pronunciation mixed up. Joke. Joke. A gag.”

“I know. That was a joke, too.”

Magic Johnson grinned, showing his white teeth, then added,

“But the part about the Pentagon wasn’t a joke.”

“…”

“Let’s go. It looks like someone else is already ready. Isn’t that right?”

I turned my head in the direction of Magic Johnson’s gaze.

Along with a familiar presence, someone entered my field of vision.

Team Leader Choi answered in a subdued voice.

“Of course, Mr. Johnson.”
```

<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0405.txt",
      "sha256": "4f91b61c11ffbca9a1554dccecf3b858811b49e5fb60835cda8f87d95627d4c1",
      "bytes": 13724
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "b139084e548205ed07330e7fc777218e574a734c7b373f45a54c3798bc729b74",
      "bytes": 2452
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "14aa4b4212f88ac520e764f2962b4cfc8a2417ab730afa5b9d560f79471dfc47",
      "bytes": 135975
    },
    {
      "path": "characters/Go Jun.md",
      "sha256": "91124eef349848467162a36e3c667932db690987e436e9b2ffbbca9ecd2b3f00",
      "bytes": 1976
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "5fa1e9619087d5f1c73d7cb26d7f0b4e4f8aba17443d9365da7a2151dfb523d4",
      "bytes": 1212
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "3555634f746ed9ff40e29ab06c7e560a72e433f256d3333e3824cfd4971d14b8",
      "bytes": 622
    },
    {
      "path": "characters/Lee Jungryong.md",
      "sha256": "a876e90628328ae22a4c9afe9422c68d37642a99c0b30eb5c1416b1054c1c9d0",
      "bytes": 1396
    },
    {
      "path": "characters/Wei Fenghu.md",
      "sha256": "a1eab81969303358b6c050bb30fb6844ed78304b729ba9a2e604bf598d2f5e53",
      "bytes": 560
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "d12978c0ab9e786387f0628d45e90a5c2459f9b50f71b26f6bb343bb8b77f691",
      "bytes": 118937
    }
  ],
  "estimated_tokens": 10942
}
-->

# Durable State Update — Chapter 405

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 405. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 405. Profile updates may replace only one
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
  "chapter": 405,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 405,
    "continuity_sources": [405],
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
    "Wei Fenghu and more than four thousand Hunters have reached the Western Front, where the battle left the small city with no recoverable survivors among those who remained to fight.",
    "The known survivors of the Western Front catastrophe are the Public Security Armed Forces Department regimental commander, Jin Taekyung, and one other person recognized by the searchers as the final survivor.",
    "Lei Fei died after completing his final mission, and Jin has asked that Lei Fei be recorded among the dead even though his body cannot be found.",
    "Jin publicly insists that he did not win the battle alone and that the other Hunters fought desperately before his arrival.",
    "Wei Fenghu and five S-rank Hunters are assembled with Jin to pursue the culprit behind the catastrophe and end the war.",
    "Hero's Soul is a Supreme Peak sword that can grant Hero's Power to someone it recognizes as having an upright character.",
    "Hero's Soul rejected Jin and removed Hero's Power when he formed an evil intention.",
    "The Skeleton Warlord absorbed some of the mana released when Lei Fei disappeared and confirms that only a faint trace of Lei Fei's soul remains in Hero's Soul.",
    "The Skeleton Warlord has no memories of its own past and has begun questioning what kind of being it once was.",
    "The wider war against the Arch Lich remains unresolved, and Jin has now committed to the operation intended to end it."
  ],
  "continuity_sources": [
    404,
    403
  ],
  "open_questions": [
    "Who is Lei Fei's unidentified lord, what is the lord's origin, and how does the lord relate to the Arch Lich's objective?",
    "What happened to the Second Fiend assigned to the Qingcheng attack?",
    "Will Jin and the five assembled S-rank Hunters defeat the Arch Lich and end the war?",
    "What kind of being was the Skeleton Warlord before it became an undead commander?",
    "What specific situation will allow Jin to draw out Hero's Power more strongly?"
  ],
  "safe_through": 404,
  "temporary_decisions": [
    "Render 나이트메어 as Nightmare.",
    "Use black knight for 검은 기사 and keep it distinct from Death Knight and Death Knight Lord.",
    "Render 언령 as word-spell.",
    "Render 영웅의 혼 as Hero's Soul and 영웅의 힘 as Hero's Power.",
    "Render 진 선생 and 진 선생님 as Mr. Jin while preserving Jin's blunt, profane voice."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 이정룡    | **Lee Jungryong** |
| 상태               | **Status**                     |
| 체력               | **Stamina**                    |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 길드      | **Guild**             |
| 길드장     | **Guild Master**      |
| 부길드장    | **Vice Guild Master** |
| 팀장      | **Team Leader**       |
| 대격변     | **Great Cataclysm**   |
| 고준 | **Go Jun** | Personal name of Team Leader Seok; Lee Jungryong's prized Disciple. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 웨이펑후 | **Wei Fenghu** | Minister of National Defense under China's Central Military Commission. |
| 아레스 | **Ares Guild** | The leading Guild in Korea; formerly employed Team Leader Choi and Song Song. |
| 전세 | **jeonse lease** | Korean lump-sum deposit lease used in the family's redevelopment-era housing history. |
| 중상 | **Severe Injury** | System condition label causing a major drop in all stats. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 준이 | **Jun** | Family nickname used in the form Jun's dad. |
| 석고준 | **Go Jun** | Source full-name form for the established Go Jun, also known as Team Leader Seok. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 경호팀장 | **Head of Security** | Go Jun's security-team office under Lee Jungryong. |
| 중국 | **China** | Country from which Team Leader Choi’s video originates. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 쓰촨성 | **Sichuan Province** | Source spelling variant of the established Sichuan location. |
| 국방부 | **Ministry of National Defense** | Government ministry referenced in Taekyung's comparison about the steady passage of time. |
| 데스나이트 | **Death Knight** | Undead commander type serving under the Black Knight. |
| 공안무력부 | **Public Security Armed Forces Department** | Chinese security organization ordered to assemble during the attack. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 이정룡 | 진태경 | senior S-rank Hunter to younger Hunter and adversary | Young man | polished, teasing, and veiled-threatening | Uses a genial tone and indirect threats while trying to make Taekyung release the captives. |
| 진태경 | 이정룡 | younger Hunter to senior S-rank Hunter and adversary | you | polite but mocking and defiant | Taekyung answers Lee's soft threats with the wolf-and-tiger metaphor and refuses to yield. |
| 이정룡 | 고준 | Master to Disciple | Go Jun | familiar and testing | Lee switches from Seok's office title to his personal name while considering whether he can defeat Taekyung. |
| 고준 | 이정룡 | Disciple to Master | Master | deferential | Go Jun responds to Lee's personal-name address as 스승님. |
| 진태경 | 석고준 | returning Hunter to hostile Ares security leader | you fucking bastard | hostile and profane | Taekyung directs his final insults and challenge at Go Jun after returning alive. |
| 석고준 | 진태경 | hostile_opponents | brat | hostile and overconfident | Go Jun addresses Taekyung internally as 애송아 while launching his full-strength attack. |
| 웨이펑후 | 진태경 | senior_military_official_to_ally | Mr. Jin | formal-polite | Wei Fenghu addresses Jin while inviting him to walk to the operations headquarters. |
| 진태경 | 웨이펑후 | Foreign Hunter to senior military official | General, Commander, or Supreme Leader | Polite but flustered | Jin jokingly cycles through grand titles while trying to interrupt Wei's emotional request. |
| 웨이펑후 | 이정룡 | senior military official to senior foreign S-rank Hunter | Mr. Lee | formal and concerned | Wei asks Lee whether something is wrong. |
| 데스나이트 | 인간 | enemy combatants | human | contemptuous and commanding | Used in the Death Knight's warnings to Jin. |
| 데스나이트 | 로드 | subordinate to commanding lord | Lord | fearful and deferential | The Death Knight calls to the Death Knight Lord after Jin overwhelms the army. |

## Listed compact profiles

### Go Jun.md

# Go Jun (고준)

- **Safe through:** Chapter 305
- **Aliases:** Team Leader Seok
- **Role:** Leader of Lee Jungryong's security team, an Ares Guild combatant, and Lee's prized Disciple and right-hand man; personally selected and trained by Lee; ordered to monitor Jin Taekyung and deal with him if necessary; attacked Taekyung in the hospital and was defeated before being carried out by a security Hunter; after Lee restored him with mana, reported that Taekyung's strength and speed exceeded his own and that Taekyung had extensive combat experience, then received orders to intensify Peace Guild surveillance, assess its personnel, reinforce the security team, and monitor Ares executives and overseas branches; supported allowing the Peace Guild to lead the Black Forest entry, then taunted Choi Minwoo over Taekyung's apparent death before Taekyung returned alive; joined the delayed rescue operation with the Seoul Branch President and hundreds of Hunters, confronted Taekyung after his return, threatened him while invoking Lee Jungryong's special order, and prepared to fight; defied Lee's order to avoid a clash with the Peace Guild after Taekyung insulted Lee, attacked Taekyung with his full strength, was defeated by a single blow, suffered catastrophic internal injuries, and lost consciousness after Taekyung ordered him to convey a warning to Lee.
- **Personality:** Highly disciplined, fiercely loyal to Lee Jungryong, confident in his abilities, and angered by operational failures that endanger his Master.
- **Voice:** Dry, controlled, and formal with subordinates; deferential when addressing his Master.
- **Relationships:** Disciple and direct protégé of Lee Jungryong; leader of Lee's security detail; regarded by Lee as stronger than Park Tae Seop; after Go Jun's defeat by Jin Taekyung, Lee reaffirmed his faith in Go Jun and promised to give him the strength to defeat Taekyung.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 404
- **Aliases:** Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, and a Supreme Peak master who has manifested Force and crossed the wall into true mastery.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother; Jeok Cheongang is his Master; Cheongpung is his trusted companion and only true martial rival; Choi Minwoo is his subordinate and student; his mother and sister Hayeon are among those he protects.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 404
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Lee Jungryong.md

# Lee Jungryong (이정룡)

- **Safe through:** Chapter 395
- **Aliases:** None
- **Role:** Vice Guild Master of Ares Guild; one of Korea's two S-rank Hunters; effective wielder of Ares Guild's authority in place of its Guild Master; Supreme Peak-level martial artist; gave Park Jihoon his initial orders and is Jihoon's master; visited the Peace Guild's hospital after Taekyung demanded an apology, brought compensation, and demanded the captives after negotiations.
- **Personality:** Outwardly genial, calm, and humorous; calculating, manipulative, coercive, and ruthless when challenged
- **Voice:** Smooth, good-natured, and indirect, using teasing conversation and veiled threats before becoming openly furious
- **Relationships:** Master of Park Jihoon and Go Jun (Team Leader Seok), whom he personally selected and trained; longtime Great Cataclysm acquaintance of Park Tae Seop; adversary of Jin Taekyung; knew Team Leader Choi from childhood; has an antagonistic history with Kim Hwajong, who saved his life at the collapse of Mapo Bridge eighteen years earlier; was visibly shaken by learning that Choi is Cheon Taemin's maternal grandson; regards Cheon Taemin as an older brother despite no blood relation and has long held him in respect and fear; operates as Ares Guild's senior authority beneath its Guild Master

### Wei Fenghu.md

# Wei Fenghu (웨이펑후)

- **Safe through:** Chapter 404
- **Aliases:** None
- **Role:** Wei Fenghu is the Minister of National Defense under China's Central Military Commission and a four-star general.
- **Personality:** Courteous, reserved, and authoritative.
- **Voice:** Formal and measured, addressing Jin as Mr. Jin.
- **Relationships:** Wei Fenghu is Lei Fei’s maternal uncle who raised him as his own son; after Lei Fei’s death, he entrusted Lei Fei’s sword to Jin Taekyung.

## Korean source

```text
＃405화



- 그럼 익일 06시 30분 부로 작전을 시작하겠소. 해당 전선은 하달되는 명령에 따라 빈틈없이 이행해 주시오.

팟.

웨이펑후 국방부장의 발언을 마지막으로 회의가 끝났다.

화면이 꺼진 다섯 개 모니터를 바라보며, 아레스 길드 부길드장 이정룡은 의자에 등을 기댔다.

‘흐름이 빠르군. 생각보다 훨씬’

쉽게 끝날 전쟁이 아니었고, 그렇게 끝나서는 안 되는 전쟁이었다.

중국은 수많은 헌터를 보유한 헌터 강국인 동시에 폐쇄적인 국가다. 세계 각국에 용병 사업으로 손을 뻗친 아레스 길드가 제대로 자리 잡지 못한 몇 안 되는 국가 중 하나이기도 했다.

그렇기에 이정룡은 중국의 안정을 바라지 않았다. 중국이 입는 피해가 커질수록, 파고들 수 있는 틈이 더욱 벌어질 테니까.

백만이 넘는 사상자? 수백조 원의 재산 피해?

그것이 무슨 상관인가. 이번 몬스터 웨이브는 누군가에게는 재앙이겠지만 이정룡에게는 기회였다.

하지만…….

‘이번에도 진태경, 그놈이 문제로군.’

이정룡은 손가락을 들어 천천히 탁자를 두드렸다.

세상일이 뜻대로 흘러가지 않는다는 것 정도는 알았지만, 근래 들어 진태경이 사사건건 앞길을 가로막을 때마다 문득 떠오르는 생각이 있었다.

‘위험한 놈이다.’

진태경의 존재를 처음 알았을 때 느꼈던 흥미로움은 이미 씻은 듯이 사라진 지 오래다.

허리에 닿을락 말락 했던 어린아이가 몇 달 사이 훌쩍 자라 시선을 마주하고 있다면, 어른은 당황할 수밖에 없다.

심지어 그 아이의 성장이 아직 멈추지 않았다면?

‘더욱 위험해지겠지.’

아크 리치의 발호(跋扈)가 이정룡에게 기회였다면, 진태경에게는 날개였다.

놈은 실로 엄청난 전공을 세웠고 전세계의 스포트라이트를 받고 있었다.

또 다른 전쟁이 새로운 영웅을 낳은 것이다. 마치 혼란하던 대격변 시대의 영웅들처럼.

‘사람들은 강자를 두려워하는 동시에 선망하지만, 영웅은 추앙받는 법.’

이정룡은 그 사실을 잘 알고 있었다. 그리고 이 전쟁이 진태경의 활약으로 막을 내리면, 만약 그렇게 된다면 그때는…….

퍼석.

어느새 오러가 실린 손가락 끝이 단단한 목제를 뚫고 가루로 만들어버렸다.

중심부가 뻥 뚫린 탁자를, 이정룡은 묵묵히 내려다보았다.

지금은 작은 구멍에 불과하더라도 그 크기가 점점 커진다면 그때는 걷잡을 수 없다. 탁자가 쓰러지기 전에 구멍을 메워야 한다.

“경호팀장 들어오라고 하게.”

이정룡의 입술 사이로 나직한 목소리가 흘러나오자 문밖에서 대기하고 있던 누군가가 자리를 떴다.

얼마 지나지 않아 익숙한 인기척이 문을 열고 들어왔다.

“찾으셨습니까.”

짧은 시간 동안 달라진 건 진태경뿐만이 아니었다.

이정룡 부길드장의 오른팔이자 경호팀장인 석고준에게도 많은 변화가 있었다.

깊게 가라앉은 어두컴컴한 안광과 메마른 목소리. 사정을 아는 몇몇 인물들은 진태경에게 패배한 후 안 그래도 딱딱하던 인상이 더 음울해졌다면 수군거렸지만, 이정룡의 생각은 달랐다.

“좋아 보이는군.”

“약간의 성취가 있었습니다.”

“겸손도 과하면 보기에 좋지 않다. 오늘 전장에서도 큰 전공을 세웠으니 그 정도면 칭찬받아 마땅하지.”

“……감사합니다.”

오늘, 다섯 개 전선을 노린 몬스터 군단의 갑작스러운 기습은 엄청난 사상자를 남겼지만, 이정룡이 맡은 북부 전선만은 예외였다.

지금까지 전투에 소극적으로 대처하며 전력을 유지한 아레스 길드의 정예들이 몬스터 군단을 도륙했고, 석고준이 우두머리 격인 데스나이트 두 기를 홀로 해치웠기 때문이었다.

“피해는?”

“중상자 11명에, 경상자 46명. 사망자는 없습니다. 중상자들은 회복까지 조금 더 시일이 걸리겠지만 경상자들은 이미 모두 회복시킨 상태입니다.”

헌터와 군인들을 포함한 4천여 명의 사상자는 끼어들 자리가 없었다.

질문하는 이정룡과 대답하는 석고준. 두 사람에게는 아레스 길드만이 아군이었으니까.

“그나저나 안타깝게 됐어. 사령관이 그리 비명에 갈 줄이야. 제법 강단 있던 사람이었는데…….”

말꼬리를 흐리는 이정룡의 모습에, 석고준이 음울하게 가라앉은 눈빛을 빛냈다.

“죄송합니다. 최선을 다해 막아 보려 했지만 몬스터들의 숫자가 너무 많아서 그만.”

“어쩔 수 없지. 시신은 잘 수습했나?”

“워낙 훼손이 심하여 어쩔 수 없이 화장했습니다. 사령관과 함께 사망한 참모진들도 마찬가지입니다.”

“잘했네. 아, 왕오춘 중장이 새로운 사령관이 된 것은 알고 있겠지?”

“예. 안 그래도 인사를 나누고 오는 길입니다.”

왕오춘 중장과 석고준이 초면이 아니라는 것은 이정룡을 포함한 극소수만이 아는 비밀이다.

몇 년 전부터 두 사람은 눈에 띄지 않는 비밀 안가(安家)에서 종종 식사를 함께했고, 그럴 때마다 왕오춘 중장의 승용차 트렁크는 무거워졌다.

“뭐라 하시던가?”

“앞으로 잘 부탁한다더군요.”

이정룡의 입가에 희미한 웃음이 맺혔다.

“그렇지. 함께 싸울 전우(戰友)니까.”

지금쯤 그는 중책을 맡았다는 생각에 기뻐하고 있겠지만 이러한 일련의 상황들이 단순한 행운이 아니라는 사실은 까맣게 모를 것이다.

이제는 한 줌 잿가루가 된, 강단 있던 전임 사령관이 아레스 길드의 소극적인 전투에 관한 보고서를 작성 중이었다는 것 역시.

“잘 지켜 드리게. 사령관을 두 번이나 잃을 수는 없지 않나.”

“알겠습니다.”

전장에서는 무슨 일이 벌어질지 모른다.

사이가 안 좋던 지휘관이 몬스터에게 갈기갈기 찢겨 죽을 수도 있고, 돈을 좋아하는 부패한 군 장성이 새로운 사령관으로 부임할 수도 있는 것이다.

한결 기분이 나아진 이정룡이 입을 열었다.

“내일부터는 고생할 테니 오늘 밤은 푹 쉬어 두게.”

“그 말씀은……?”

“최대한 신속하게 진군. 남아 있는 몬스터들을 쓸어 버리라더군.”

“기동전이군요. 모든 전선에 하달된 명령입니까?”

이정룡이 고개를 끄덕였다.

북부 전선을 비롯한 다섯 개 전선은 내일 아침부터 기동전을 실시, 며칠 후에는 몬스터 군단을 퇴로를 차단하며 촘촘한 포위망을 구축하게 될 것이다.

“분명 놈들도 상당한 전력을 잃었겠지만…… 수적으로 만만치 않을 것 같습니다.”

“이 나라가 가장 내세울 수 있는 게 뭐라 생각하나? 지금 이 순간에도 수백 대의 수송기가 중국 전역에서 헌터들을 운반하고 있지. 하급 헌터라 해도 화살받이로는 쓸 만할 거야.”

담담한 말투로 설명한 이정룡이 말을 이었다.

“자네는 길드의 피해를 최소화하는 것에 집중하게. 혹여나…….”

이정룡이 심유한 눈빛으로 탁자를 바라보았다.

“구멍을 메워야 할 일이 생길지도 모르니.”

“……명심하겠습니다.”

종잡을 수 없는 말이었지만 이정룡은 석고준에게 있어 존경하는 스승이자 신이나 다름없는 존재였다.

별다른 의문을 표하지 않고 묵묵히 고개를 끄덕인 석고준은 문득, 자신이 중요한 질문을 하지 않았다는 것을 깨달았다.

“최종 목적지는 어디입니까?”

이정룡은 대답 대신 손을 들어 한 곳을 가리켰다. 벽면을 가득 메운 쓰촨성의 지도.

푸슉! 손가락 끝에서 쏘아진 바람이 지도의 한 부분을 꿰뚫었다. 석고준의 시선이 구멍 옆에 적혀 있는 지명에 닿았다.

쑤이닝시(遂宁市市).

이번 사태의 모든 것이 시작된 곳. 그곳에 아크 리치가 있었다.



* * *



다음 날 새벽. 잠에서 깨어난 사람들은 자신들이 두 분류로 나누어졌음을 깨달았다.

떠나는 자와 남는 자.

당연하게도 나는 전자였고, 최 팀장과 샤오 쉔은 후자에 해당했다.

그리고 떠날 시간이 코앞으로 다가온 후에야 가까스로 정신을 차린 두 사람은 자신들이 남는다는 사실에 저항하기 시작했다.

“진태경 씨. 전 멀쩡합니다.”

「전 멀쩡합니다, 형님!」

“싸울 수 있습니다.”

「누구보다 열심히 싸울 자신 있습니다!」

……뭐지, 메아리인가?

굳은 얼굴로 외치는 최 팀장과 샤오 쉔을 바라보던 나는 어쩔 수 없이 한 가지를 제안했다.

“으음. 그럼 날 상대로 10분 버티면 데려가 줄게요.”

“…….”

「…….」

- 지금 그걸 말이라고 하는 거냐? 이 양심 없는 간악한 인간이여.

양심은 무슨.

그렇게 따지면 오히려 저 두 사람이 양심이 없는 거다. 아직 제대로 뛰지도 못하면서 전장에 데려가 달라니.

전의를 불태우는 건 좋지만, 이 상태로 전장에 나섰다가는 죽기 딱 좋다.

‘그리고 무슨 언데드 주제에 양심을 따지고 있어.’

팍, 씨. 아주 그냥.

마음속으로 으름장을 놓은 나는 잔뜩 풀이 죽은 두 사람을 향해 말을 이었다.

“우선은 회복에 집중하세요. 며칠 동안 감각을 되살리고 체력이 돌아오면 그때는 전선에 투입될 수도 있으니까. 최 팀장님은 물론, 쉔 너도 마찬가지고.”

“으음.”

「으으음.」

아직도 영 내키지 않아 보였지만, 어쨌건 이제 어느 정도는 수긍하는 분위기다.

사실 두 사람 모두 현재 자신들의 몸 상태를 알고 있으니 여기서 더 억지를 부릴 수도 없겠지.

“그럼 저는 슬슬 가 볼…… 아.”

한 가지를 깜빡했다.

나는 공간 확장 마법이 걸린 주머니를 뒤지는 척하며, 인벤토리에 넣어 두었던 그것을 꺼내 내밀었다.

“자.”

샤오 쉔이 눈을 깜빡였다.

「……형님?」

“뭐 해, 안 받고. 팔 떨어져.”

엉겁결에 내가 내민 것을 받아 든 샤오 쉔이 어리둥절한 얼굴로 물었다.

「이게 뭡니까?」

“선물. 아는 사람이 맡긴 건데, 아무래도 네가 가지는 게 나을 것 같아서.”

「이런 명검을요?」

“왜, 싫어?”

「아, 아니 그건 아니고요. 제가 이런 걸 받아도 될지…….」

다급히 손을 내저은 샤오 쉔이 몽롱한 눈빛으로 [영웅의 혼]의 검자루를 쥐었다.

완벽에 가까운 무게 중심과 균형. 투명한 검신에서는 감출 수 없는 예기가 흐른다.

침을 꿀꺽 삼킨 녀석이 물었다.

「저, 정말 받아도 되는 겁니까?」

“그냥 주는 게 아니라, 자격이 있어서 주는 거다.”

「자격…… 말씀이십니까?」

“그래, 자격.”

지난 전투에서 보여 준 용감함. 타인을 위한 희생. 그거면 충분하다.

이미 오랜 시간 동안 창을 써 온 내가 갖고 있어 봤자 인벤토리에서 썩어갈 뿐이니까.

나보다는 같은 중국인이자 공안무력부 소속인 샤오 쉔이 더 적임자라고 판단했다.

‘검자루를 쥐었는데도 아무 일 없는 것 보면 검의 인정도 받은 셈이고.’

스켈레톤 워로드가 작게 툴툴거렸다.

- 나도 검 잘 쓸 수 있는데…… 검 좋아하는데…….

응? 뭐라고?

새벽에 나 몰래 인벤토리에서 [영웅의 혼]을 잡았다가 비명 지른 찐따의 말이라 잘 안 들리는데?

- ……흥, 됐다. 저런 싸구려 검 따위, 본 사령관에게는 어울리지 않는다!

“…….”

뭐래. 너보다 더 받고 싶은 사람도 가만히 있는데.

마침 생각난 김에, 나는 슬쩍 최 팀장의 눈치를 살폈다.

사실 마지막까지 고민했다. [영웅의 혼]을 샤오 쉔에게 줄지, 최 팀장에게 줄지.

아무래도 최 팀장도 사람이니 섭섭해할 수도 있으니까.

하지만 전부 기우였던 모양이다.

“축하합니다, 쉔 연대장. 정말 좋은 검을 얻으셨군요.”

최 팀장의 진심 어린 축하에, 그제야 정신을 차린 샤오 쉔이 [영웅의 혼]과 그를 번갈아 보았다.

갈등이 느껴지는 눈빛. 그러나 이내 맑은 웃음이 입가에 번진다.

「아무래도 제가 아닌 것 같아요. 이 검의 주인은.」

“……?”

「최 선생님. 저 대신 이 검을 받아주시겠어요?」

이건 예상치 못한 흐름인데. 그래도 뭐.

‘보기 좋네.’

당황한 최 팀장이 정중하게 거절했지만, 이미 마음의 결심을 끝낸 샤오 쉔의 의지가 더 강했다.

서로를 향해 주거니 받거니 하는 두 사람을 바라보던 나는 슬그머니 병동을 빠져나와 걸음을 옮겼다.

문을 닫기 전, 얼핏 최 팀장의 목소리가 귓가에 닿는다.

“제가 지금까지 봐 왔던 검 중에, 가장 마음에 듭니다.”

그래, 그럼 그것으로 된 거다.

나는 이미 집결을 끝낸 병력들 사이로 힘차게 걸음을 내디뎠다.

경외 어린 시선과 함께 인의 장막이 갈라졌다.
```

## Final English reading copy

```markdown
# Chapter 405

“Then we will begin the operation at 06:30 tomorrow. The fronts concerned are to carry out every order they receive without fail.”

Pop.

The meeting ended with Wei Fenghu, the Minister of National Defense, having the final word.

Lee Jungryong, the Vice Guild Master of Ares Guild, leaned back in his chair as he stared at the five monitors whose screens had gone dark.

*The pace is fast. Much faster than I expected.*

It was not a war that would end easily, nor was it a war that should end easily.

China was both a Hunter powerhouse with an enormous number of Hunters and a closed-off country. It was also one of the few countries where Ares Guild, which had extended its reach across the world through its mercenary business, had failed to establish a proper foothold.

That was why Lee Jungryong did not want China to remain stable. The greater the damage China suffered, the wider the opening would become for him to exploit.

More than a million casualties? Hundreds of trillions of won in property damage?

What did any of that matter? This monster wave might have been a disaster for some people, but for Lee Jungryong, it was an opportunity.

But…

*This time too, Jin Taekyung is the problem.*

Lee Jungryong raised a finger and slowly tapped it against the table.

He had always known that the world did not go according to plan, but lately, whenever Jin Taekyung obstructed him at every turn, a thought kept surfacing.

*He’s dangerous.*

The interest Lee Jungryong had felt when he first learned of Jin Taekyung’s existence had long since vanished without a trace.

If a child who had barely reached an adult’s waist suddenly grew by leaps and bounds over the course of several months and met that adult’s gaze head-on, the adult could not help but be flustered.

What if that child’s growth had not yet stopped?

*He’ll become even more dangerous.*

If the Arch Lich’s rampage had been an opportunity for Lee Jungryong, it had given Jin Taekyung wings.

The man had achieved truly incredible military feats and was receiving the attention of the entire world.

Another war had produced a new hero. Just like the heroes of the chaotic Great Cataclysm era.

*People fear the strong even as they envy them, but heroes are worshiped.*

Lee Jungryong knew that better than anyone. And if this war ended because of Jin Taekyung’s exploits—if it did—then…

Crack.

The tip of his finger, infused with aura, had already bored through the solid wood and reduced it to powder.

Lee Jungryong silently looked down at the table, its center punched clean through.

For now, it was only a small hole. But if it continued to grow, it would soon become impossible to control. He had to fill the hole before the table collapsed.

“Have the Head of Security come in.”

When Lee Jungryong’s quiet voice slipped between his lips, someone waiting outside the door left to carry out the order.

Before long, a familiar presence opened the door and entered.

“You called for me?”

Jin Taekyung was not the only one who had changed over such a short period of time.

Go Jun, Lee Jungryong’s right hand and Head of Security, had undergone many changes as well.

His dark eyes had sunk deeply, and his voice had become dry. A few people who knew the circumstances whispered that after losing to Jin Taekyung, his already rigid expression had grown even gloomier.

Lee Jungryong had a different opinion.

“You look well.”

“I’ve made a little progress.”

“Too much humility is unbecoming. You achieved a great feat on today’s battlefield as well. That is more than enough to deserve praise.”

“……Thank you.”

The sudden attack by the monster army targeting five fronts had left an enormous number of casualties, but the northern front under Lee Jungryong’s command had been an exception.

The elite members of Ares Guild had held back their strength and responded cautiously to the fighting until now. When the attack came, they slaughtered the monster army. Go Jun had also defeated two Death Knights, each one acting as a commander, by himself.

“What were our losses?”

“Eleven severely injured and forty-six lightly injured. There were no deaths. The severely injured will need a little more time to recover, but all the lightly injured have already been healed.”

The more than four thousand casualties among the Hunters and soldiers did not enter the equation.

Lee Jungryong asked the questions, and Go Jun answered them. To the two of them, only Ares Guild was on their side.

“It’s unfortunate about the commander, though. To die such an untimely death. He was quite a tough man……”

At Lee Jungryong’s trailing words, a gloomy light flickered in Go Jun’s sunken eyes.

“I’m sorry. I tried to stop them with everything I had, but there were simply too many monsters.”

“It couldn’t be helped. Did you recover the body?”

“The damage was too severe, so we had no choice but to cremate him. The staff officers who died alongside the commander were treated the same way.”

“Good work. Ah, you know that Lieutenant General Wang Ochun is the new commander, don’t you?”

“Yes. I was just on my way back from meeting him.”

Only a very small number of people, including Lee Jungryong, knew that Lieutenant General Wang Ochun and Go Jun were not meeting for the first time.

For several years, the two had occasionally shared meals at inconspicuous safe houses. Each time, the trunk of Lieutenant General Wang Ochun’s sedan grew heavier.

“What did he say?”

“He said he looked forward to working with me.”

A faint smile appeared around Lee Jungryong’s lips.

“Of course. You’re comrades who will fight together.”

By now, Wang Ochun was probably delighted by the thought that he had been entrusted with an important post. He had no idea that this entire chain of events was not mere good fortune.

Nor did he know that his tough predecessor, now reduced to a handful of ashes, had been preparing a report on Ares Guild’s lackluster performance in battle.

“Watch over him carefully. We can’t lose the commander twice, can we?”

“Understood.”

No one knew what might happen on a battlefield.

A commander who had been on bad terms with someone might be torn to pieces by monsters, while a corrupt military general who loved money might be appointed the new commander.

Lee Jungryong, whose mood had improved somewhat, opened his mouth.

“You’ll have a hard time starting tomorrow, so get plenty of rest tonight.”

“What do you mean by that……?”

“They say we’re to advance as quickly as possible and sweep away the remaining monsters.”

“Mobile warfare, then. Is that the order for every front?”

Lee Jungryong nodded.

The five fronts, including the northern front, would begin mobile warfare tomorrow morning. Within a few days, they would cut off the monster army’s retreat and build a dense encirclement around it.

“They must have lost a considerable amount of strength as well, but their numbers won’t be easy to deal with.”

“What do you think this country has the most of? Even now, hundreds of transport planes are carrying Hunters from every corner of China. Even low-ranking Hunters will be useful as arrow fodder.”

Lee Jungryong explained this in a calm voice before continuing.

“Focus on minimizing the Guild’s losses. In case……”

Lee Jungryong gazed deeply at the table.

“There may come a time when you have to fill a hole.”

“……I’ll keep that in mind.”

It was an inscrutable statement, but to Go Jun, Lee Jungryong was both a revered Master and something no different from a god.

Without voicing any questions, Go Jun silently nodded. Then he suddenly realized that he had failed to ask an important question.

“Where is our final destination?”

Instead of answering, Lee Jungryong raised a hand and pointed toward one place: the map of Sichuan Province covering the wall.

Pshk!

Wind shot from the tip of his finger and pierced one section of the map. Go Jun’s gaze landed on the place-name written beside the hole.

Suining City.

The place where everything in this disaster had begun.

The Arch Lich was there.

* * *

The following dawn, those who woke from sleep realized that they had been divided into two groups.

Those who were leaving and those who were staying.

Naturally, I belonged to the former group, while Team Leader Choi and Shao Shen belonged to the latter.

And only when the time to leave was almost upon them did the two men finally come to their senses and begin resisting the fact that they were staying behind.

“Mr. Jin. I’m perfectly fine.”

“I’m perfectly fine, hyung!”

“I can fight.”

“I’m confident I can fight harder than anyone!”

*……What is this, an echo?*

As I looked at Team Leader Choi and Shao Shen shouting with stiff expressions, I had no choice but to make them an offer.

“Hmm. Then if you can last ten minutes against me, I’ll take you with me.”

“……”

“……”

—Is that what you call an offer, you shameless, wicked human?

*What do you mean, conscience?*

If we were going to argue about it, those two were the ones without a conscience. They could barely run properly, yet they wanted me to take them to the battlefield.

It was good that they were burning with the will to fight, but going to the battlefield in their current condition was a perfect way to get themselves killed.

*And what kind of undead talks about conscience?*

*Damn it. Seriously.*

After issuing that threat in my mind, I continued speaking to the two men, who had become thoroughly dejected.

“For now, focus on recovering. If you spend the next few days getting your feel back and your stamina returns, you might be deployed to the front then. That goes for you too, Shen—not just Team Leader Choi.”

“Hmm.”

“Hmmmm.”

They still did not seem happy about it, but at least they appeared somewhat resigned.

In truth, both of them knew the condition their bodies were in. They could not keep forcing the issue forever.

“Then I’ll be going now…… Ah.”

I had forgotten one thing.

I pretended to rummage through the bag enchanted with space-expansion magic, then took out the item I had stored in my inventory and held it out.

“Here.”

Shao Shen blinked.

“……Hyung?”

“What are you waiting for? Take it. My arm’s going to fall off.”

Shao Shen reflexively accepted what I had offered and asked with a bewildered expression.

“What is this?”

“A gift. Someone I know entrusted it to me, but I think you should have it.”

“A sword this fine?”

“What? You don’t like it?”

“No, that’s not it. I’m just wondering whether I should be accepting something like this……”

Shao Shen hurriedly waved his hands, then gripped the hilt of Hero’s Soul with dazed eyes.

Its weight distribution and balance were close to perfect. An edge impossible to conceal flowed from the transparent blade.

After swallowing hard, he asked,

“Can I really accept this?”

“I’m not giving it to you for no reason. I’m giving it to you because you qualify.”

“Qualify……?”

“That’s right. You qualify.”

The courage he had shown in the last battle. His sacrifice for someone else.

That was enough.

If I kept it, it would only rot away in my inventory. I had been using a spear for a long time already.

I judged that Shao Shen, who was both Chinese and a member of the Public Security Armed Forces Department, was more suited to wield it than I was.

*The sword must have recognized him too, considering that nothing happened even after he gripped the hilt.*

The Skeleton Warlord grumbled quietly.

—This commander can use a sword well too…… And this commander likes swords……

*Huh? What was that?*

It was hard to hear the words of a loser who had secretly grabbed Hero’s Soul from my inventory at dawn and screamed.

—……Hmph, forget it. A cheap sword like that is unworthy of this commander!

“……”

*What is he talking about? Someone who wants it more than you is sitting quietly right here.*

Since I was thinking about it anyway, I discreetly glanced at Team Leader Choi.

In truth, I had agonized over it until the very end—whether to give Hero’s Soul to Shao Shen or Team Leader Choi.

Team Leader Choi was human too, after all. He might have felt hurt.

But apparently, all that worry had been for nothing.

“Congratulations, Regimental Commander Shen. You’ve obtained a truly fine sword.”

At Team Leader Choi’s sincere congratulations, Shao Shen finally came to his senses and looked back and forth between Hero’s Soul and him.

Conflict flickered in his eyes. But soon, a clear smile spread across his lips.

“I don’t think I’m the one this sword belongs to.”

“……?”

“Mr. Choi. Would you accept this sword in my place?”

This was an unexpected turn of events. Still……

*That’s nice to see.*

Team Leader Choi was flustered and politely refused, but Shao Shen had already made up his mind, and his resolve was stronger.

As I watched the two of them pass the sword back and forth, I quietly slipped out of the ward and started walking.

Before I closed the door, Team Leader Choi’s voice reached my ears.

“Of all the swords I’ve seen, this is the one I like best.”

Right. That was all that mattered.

I strode energetically among the troops who had already assembled.

A human wall parted before me amid looks of awe.
```

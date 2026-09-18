<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0389.txt",
      "sha256": "d3b89f228a1559fb1d8cf693f875795d806377a55890184720c7c542fce2d61d",
      "bytes": 12860
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "198cca6eb323a6f4fe697d93b60bfc7f4074ed5e37bce785c59f9a581c40e0b0",
      "bytes": 3914
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "e624c1a27f5f8a896bce426e1f41773adca3f1f660fa708733b95c585296ec64",
      "bytes": 134201
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "1e29fad4fb7bebba8a02bc21a2beb538737e133a0330c4a0af11ee603823eb6d",
      "bytes": 533
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "bfe1bedb92617789d7762db05641487666e8f78e50223c297b66084adb15fb29",
      "bytes": 1168
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "a52ce44d8c6721f2c74d1830431a151fb932c6d941f4fdc6634039fb1f247c99",
      "bytes": 622
    },
    {
      "path": "characters/Kim Cheol Soo.md",
      "sha256": "7fb30d9054b54146d24887e765eff39edc9cb5403a480de49ff8ca3d5e3b65fb",
      "bytes": 711
    },
    {
      "path": "characters/Lee Jungryong.md",
      "sha256": "962a1fb0bd39204190b505ae1038cd347b5e3293be865711f9c16cc310de6bba",
      "bytes": 1396
    },
    {
      "path": "characters/Wu Heixing.md",
      "sha256": "3cdcfa5217c3b8df960c9fc6eb2d677c0f3c13397e7ae0074c8f85d808e4f17c",
      "bytes": 720
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "db0675fb9956ea9ed1371d19bbfab675e79cec2697d3b5f4adef5baafad9b32f",
      "bytes": 110936
    }
  ],
  "estimated_tokens": 11221
}
-->

# Durable State Update — Chapter 389

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 389. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 389. Profile updates may replace only one
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
  "chapter": 389,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 389,
    "continuity_sources": [389],
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
    "Jin Taekyung is Level 121, has the Undead Hunter Title, and keeps the strengthened Skeleton Warlord in his Inventory under the mocking name Bones.",
    "Jin Taekyung has crossed the wall into true mastery, while Choi Minwoo has become substantially stronger and more refined.",
    "The Arch Lich's three incomplete Liches were destroyed at Chengdu International Airport, and their testimony identified the Arch Lich as responsible for the undead army's actions.",
    "Wei Fenghu is China's Minister of National Defense under the Central Military Commission, a four-star general, and the current Chairman's right-hand man; Lei Fei remains unconfirmed dead or alive after disappearing with his department's Hunters.",
    "Sichuan Province remains in a wartime emergency involving magical communications interference, flying-monster attacks, and a Monster Wave that has caused at least hundreds of thousands of casualties; the dead may have been raised as undead.",
    "The international S-rank Hunters gathered at Mount Qingcheng have departed for assigned battle regions, with Prince Felix leaving early after receiving a battle signal.",
    "Shao Yang is Chairman of China, Chairman of the Chinese Communist Party's Central Military Commission, and General Secretary; he has convened an emergency United Nations Security Council meeting over the catastrophe.",
    "Faye Chen is an older S-rank Hunter and Great Cataclysm hero with a former film career, a low media profile, and a playful but composed manner toward Jin.",
    "Wu Heixing is an S-rank Hunter hostile toward Jin who secretly uses Sound Transmission and martial arts, including an internal-energy cultivation technique and fist-and-foot martial arts; he remains deeply resentful of Lei Fei and Jin.",
    "Lee Jungryong is the de facto head of the Ares Guild and one of the world's three strongest S-rank Hunters; he has recognized Jin's breakthrough and is now seeking an undisclosed discussion with Wu Heixing.",
    "Jin Taekyung completed Circulate Your Qi and slightly advanced the realm of Fire Gate Divine Technique.",
    "Jin Taekyung is under the nonrefusable Sudden Quest The Desperate War Situation and must reach the front quickly to defeat the enemies."
  ],
  "continuity_sources": [
    388,
    387
  ],
  "open_questions": [
    "Who is the Arch Lich, and what will happen after Jin Taekyung destroys its three servants?",
    "What happened to Lei Fei and the Hunters who disappeared with him?",
    "What happened to the Second Fiend assigned to the Qingcheng attack?",
    "Who is the unidentified person directing Aehyang, and what are they planning?",
    "What important discussion does Lee Jungryong intend to have with Wu Heixing?"
  ],
  "safe_through": 388,
  "temporary_decisions": [
    "Render 열화신룡 as Blazing Flame Divine Dragon, distinct from Huashan Divine Dragon; use Mimi and Mimi-chan for 미미 and 미미쨩, and Third Fiend and Three Fiends for 삼괴.",
    "Render 진인 as Perfected One, 도우 as Fellow Daoist, 신니 as Venerable Nun, 환영진 as illusion formation, and 이동진 as Moving Formation; use Archmage and War Mage for 대마법사 and 워 메이지.",
    "Render 독룡각 as Poison Dragon Pavilion, 가주 대행 as Acting Family Head, 화룡갑 as Fire Dragon Armor, and 공안무력부 as Public Security Armed Forces Department.",
    "Render 사기 as death energy, 의념 as conveyed thoughts, 데스나이트 as Death Knight, 골골 as Bones, 아크 리치 as Arch Lich, 최상급 포션 as Top-Grade Potion, and 상급 포션 as high-grade potion.",
    "Render 시벌좌 as Lord Fuck, 반도의 빵즈 as peninsula bangzi, 짱깨 as chink, 주석 동지 as Chairman Comrade, 전하 as His Highness, and 다급해진 전황 as The Desperate War Situation; preserve Jin's vulgar historical and cultural jokes."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 철수     | **Cheol Soo**      |
| 이정룡    | **Lee Jungryong** |
| 돌파     | **break through** / **breakthrough**             | Realm advancement                                     |
| 살기     | **killing intent**                               |                                                       |
| 가주     | **Family Head**                              |
| 극양                        | **Extreme Yang**      |
| 장비               | **Equipment**                  |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 몬스터     | **monster**           |
| 레이드     | **raid**              |
| 길드      | **Guild**             |
| 팀장      | **Team Leader**       |
| 대격변     | **Great Cataclysm**   |
| 사천     | **Sichuan**            |
| 귀가      | **your family**                                                 |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 김철수 | **Kim Cheol Soo** | C-rank junior Hunter in Myeongdong Guild's Security Team. |
| 우헤이싱 | **Wu Heixing** | Chinese S-rank Hunter who provokes Jin and nearly draws his sword. |
| 평화 | **Peace Guild** | Guild name. |
| 대한민국 | **Korea** | Country reference. |
| 아레스 | **Ares Guild** | The leading Guild in Korea; formerly employed Team Leader Choi and Song Song. |
| 링크 | **Link** | Mental connection between a mage and Familiar |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 주모 | **Lady of the House** | Title used in Wipeng's remark that Jin Wikyung lacks a wife or household mistress. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 아이튜브 | **iTube** | Live-streaming platform hosting the Hunter Association ceremony. |
| 시벌좌 | **Lord Fuck** | Crude online nickname created from Taekyung's accidental broadcast profanity. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 염화일로 | **Flamefire Path** | Fire Gate Clan signature movement technique; Jeok Cheongang has reached its ninth stage. |
| 수능 | **college entrance exam** | National university entrance examination taken by Hayeon. |
| 중국 | **China** | Country from which Team Leader Choi’s video originates. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 쓰촨성 | **Sichuan Province** | Source spelling variant of the established Sichuan location. |
| 중화인민공화국 | **People's Republic of China** | Formal country name shouted by the Chinese Hunters. |
| 주석 | **Chairman** | Political title used for Xiao Yang. |
| 인민해방군 | **People's Liberation Army** | Chinese military deployed to seal off the catastrophe area. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 일원 | **One Origin** | Named Tang Clan organizational unit in Tang Sadok's mobilization order. |
| 중화 | **Zhonghua** | Patriotic term used in Shao Shen’s rallying speech. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 관리 | 진태경 | official_to_young_martial_artist | Young Master | formal-polite | The official addresses Taekyung as 공자 while explaining the consequences of Prince Shangshan's displeasure. |
| 진태경 | 김철수 | visiting Hunter to Security Team Hunter | Hunter Kim Cheol Soo | polite and manipulative | Taekyung addresses him formally while promising to mention his loyalty to the Guild Master. |
| 김철수 | 진태경 | Security Team Hunter to visiting Hunter | Hunter Jin Taekyung | formal-polite and admiring | Initially uses 선생님, then recognizes Taekyung and addresses him as 진태경 헌터님. |
| 이정룡 | 진태경 | senior S-rank Hunter to younger Hunter and adversary | Young man | polished, teasing, and veiled-threatening | Uses a genial tone and indirect threats while trying to make Taekyung release the captives. |
| 진태경 | 이정룡 | younger Hunter to senior S-rank Hunter and adversary | you | polite but mocking and defiant | Taekyung answers Lee's soft threats with the wolf-and-tiger metaphor and refuses to yield. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 우헤이싱 | 진태경 | hostile S-rank Hunter to foreign Hunter and provocation target | peninsula bangzi | insulting and confrontational | Wu repeatedly addresses Jin with anti-Korean slurs. |
| 우헤이싱 | 이정룡 | younger S-rank Hunter to senior Ares Guild authority | Mr. Lee | formal and deferential | Wu addresses Lee respectfully despite his usual hostility toward Koreans. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 382
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who has sworn never to kill again.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 388
- **Aliases:** Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, and a Supreme Peak master who has manifested Force and crossed the wall into true mastery.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother; Jeok Cheongang is his Master; Cheongpung is his trusted companion and only true martial rival; his mother and sister Hayeon are among those he protects.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 388
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Kim Cheol Soo.md

# Kim Cheol Soo (김철수)

- **Safe through:** Chapter 279
- **Aliases:** None
- **Role:** C-rank Hunter in Myeongdong Guild's Security Team; a junior employee who has been with the Guild for roughly one month.
- **Personality:** Rigid, conscientious, strongly patriotic, and intensely loyal to Guild regulations and company duty.
- **Voice:** Earnest and formal; objects directly to unauthorized conduct and reacts fervently to praise from a famous Hunter.
- **Relationships:** Junior colleague of an unnamed senior Security Team Hunter; admires Jin Taekyung and is deeply affected when Taekyung says he will recommend him to Park Tae Seop.

### Lee Jungryong.md

# Lee Jungryong (이정룡)

- **Safe through:** Chapter 388
- **Aliases:** None
- **Role:** Vice Guild Master of Ares Guild; one of Korea's two S-rank Hunters; effective wielder of Ares Guild's authority in place of its Guild Master; Supreme Peak-level martial artist; gave Park Jihoon his initial orders and is Jihoon's master; visited the Peace Guild's hospital after Taekyung demanded an apology, brought compensation, and demanded the captives after negotiations.
- **Personality:** Outwardly genial, calm, and humorous; calculating, manipulative, coercive, and ruthless when challenged
- **Voice:** Smooth, good-natured, and indirect, using teasing conversation and veiled threats before becoming openly furious
- **Relationships:** Master of Park Jihoon and Go Jun (Team Leader Seok), whom he personally selected and trained; longtime Great Cataclysm acquaintance of Park Tae Seop; adversary of Jin Taekyung; knew Team Leader Choi from childhood; has an antagonistic history with Kim Hwajong, who saved his life at the collapse of Mapo Bridge eighteen years earlier; was visibly shaken by learning that Choi is Cheon Taemin's maternal grandson; regards Cheon Taemin as an older brother despite no blood relation and has long held him in respect and fear; operates as Ares Guild's senior authority beneath its Guild Master

### Wu Heixing.md

# Wu Heixing (우헤이싱)

- **Safe through:** Chapter 388
- **Aliases:** None
- **Role:** Wu Heixing is a Chinese S-rank Hunter known for frequent media exposure and scandal who secretly practices martial arts, including an internal-energy cultivation technique and fist-and-foot martial arts.
- **Personality:** Arrogant, status-conscious, abusive, and fiercely proud of his power, he responds to humiliation with anger, jealousy, and fear.
- **Voice:** Loud, insulting, entitled, and dependent on national and political status.
- **Relationships:** He is openly hostile toward Jin Taekyung and resents Jin receiving Chairman Shao Yang's attention.

## Korean source

```text
＃389화



한파가 주춤한 어느 날이었다.

비로소 수능에서 해방된 수험생들은 재수를 준비하거나 놀기 바빴고, 직장인들은 눈 밑에 짙은 다크서클을 드리운 채 대중교통에 몸을 실었다.

그렇게 여느 때와 같은 평화로운 일상 속에서, 그 누구도 예상치 못한 폭탄이 떨어졌다.



[긴급 속보 - 유엔 안전보장이사회 중대 발표]



30분 남짓 길이의 영상은 무거운 눈빛으로 카메라를 응시하던 샤오 양 주석의 한 마디로 시작되었다.

「저는 중화인민공화국의 9대 국가주석이자 유엔 안전보장이사회의 일원으로서, 쓰촨성에서 벌어진 대규모 몬스터 웨이브를 말씀드리고자 이 자리에 섰습니다.」

전 세계의 이목을 집중시키고, 아시아 전체를 뒤흔들 폭탄이었다.



* * *



하루, 이틀, 사흘. 나흘이 지난 후에도 사태는 진정되지 않았다.

대격변 이후 수많은 사건 사고가 있었지만, 이번에 쓰촨성에서 벌어진 몬스터 웨이브는 유례를 찾아볼 수 없을 정도의 규모였다.

샤오 양 중국 주석은 공식 계엄령을 선포했고, 유엔 안전보장이사회의 승인하에 평화 유지군이 전선에 투입되었다.

전 세계의 이목이 집중된 상황.

그중에서도 특히 촉각을 곤두세우는 것은 중국과 인접한 아시아의 국가들이었다.

대한민국 역시 예외는 아니었다. 오늘도 국내 최대 포럼 사이트의 헌터 이슈란은 숯불 위 가마솥처럼 들끓고 있었다.



지금까지의 상황 요약해 준다.



이 중에서 안보리 중대 발표 영상 안 본 놈은 없겠지? 혹시 있으면 나가 뒤져야 됨. 이거 진짜 비상 상황임. 북쪽 수령 놈도 이미 아이튜브로 다 보고 여기 게시판도 눈팅 하고 있을 듯.

아무튼 지들 목숨 걸린 일까지 요약해 달라는 벌레 새1끼들 하도 많길래 참다 참다 쓴다.

1. 쓰촨성에서 원인 불명의 대규모 웨이브 발생. 현재 추정 사상자만 최소 30만.

물론 일주일 전 이야기고 지금은 비교할 수도 없겠지. 사실상 통계가 불가능하다고 봄.

2. 중국 정부가 나섰지만 생각했던 것보다 규모가 미쳤음.

아크 리치라는 놈을 중심으로 최소 수만에 달하는 몬스터 군단 결집.

인민해방군, 공군 개 털리고 공안 무력부 헌터들도 2천 명 넘게 실종(마법 방해로 통신 두절, 인공위성 감시 무력화돼서 생존 여부도 확인 못 함.)

3. 중국 정부가 비밀리에 몇몇 국가에 연락, 사태를 조속히 진압하기 위해 몇몇 S급 헌터들 고용. 이틀 전에 UN 평화 유지군까지 전선 투입해서 분전하는 중.

전투 현황은 안보리에서 업데이트하고 있으니까 관심 있는 놈은 여기 들어가 봐라.

(주소 첨부.)

아래부터는 내 개인적인 생각이니까 읽지 않아도 별 상관없음.

4. 정신머리 똑바로 박힌 사람들은 알겠지만, 지금 보통 심각한 상황이 아니다. 특히 중국 본토는 생지옥임.

쓸 만한 헌터들 끌어다가 전선에 투입하는 통에 관리가 소홀해진 다른 게이트 마력 수치도 불안하고, 모든 방면에서 초인플레이션 현상 일어나고 있음.

이게 진짜 무서운 게, 만약 전선 무너지고 몬스터 군단이 사천 밖으로 진격하게 되면…… 그 뒤는 상상에 맡긴다.

5. 그러니까 다들 ㅈ 되기 전에 마트 가서 비상식량 사 놔라. 물론 사재기로 부당이익 취하란 소리는 아님.

6. 이대로 끝내기에는 아쉬워서 국뽕 추가함.

우리의 시벌좌랑 아레스 길드 정 드래곤이 전선에서 활약 중이란다. 지금까지 빨던 대로 열심히 빨아라.

진짜 끗.



올라온 지 몇 시간 만에 조회수 10만을 돌파한 해당 게시글은 현 상황을 예의주시하고 있던 네티즌들의 댓글로 불타올랐다.



(Best댓글) 글 내용대로 심각한 상황은 맞는데, 글 작성자가 너무 분위기 쎄게 잡은 것도 있음ㅋㅋ S급 헌터들에 일반 헌터만 10만 명 참전했다는데 뭐가 그리 걱정임. 그리고 군대는 놀고 있냐?

└ ㅇㅇ걔들 지금 정비대에서 놀고 있음.

└ ……?

└ 뉴스 못 봤냐. 이번에 중국군 장비 죄다 고장 나서 최대 규모 군납 비리 드러난 거. 최소 수십조 원 규모라고 함. 발 묶인 사단이 한두 개가 아니라더라.

└ 어, 이거 어디서 많이 들어 본 얘기 같은데.

└ 제발 수통 좀 바꿔 줘라. 이 시팔 샛기들아. 작년에 전역했는데 왜 수통에서 아직도 노르망디 물맛이 나냐. 한 모금 마시면 내 이름이 김철수인지 제임스인지 헷갈리더라.

└ 김 상병님. 오늘 석식 명태 순살 조림입니다.

└ 안 먹어 ㅅㅂ

└ 그나저나 장비 고장 때문에 군대 발 묶인 것도 문제긴 한데, 걔들이야 뭐 남아도는 게 병력이라 ㄱㅊ. 어차피 몬스터한테 실질적인 타격을 줄 수 있는 건 헌터들이니까. 사실 그거 말고 더 큰 문제는 따로 있음.

└ 뭔데?

└ 몬스터 개체 수 10만 뚫음.

└ ??

└ ?????

└ 무슨 10만이야 ㅅㅂ; 개소리하지마.

└ 개소리가 아니라 유엔 안보리에서 발표한 오피셜임. 게시글 링크 타고 가서 확인해 봐라. 5분 전에 떴다.

└ 와…… 시발.

└ 윗 댓글 반응 보니까 진짠가 보네 ㅁㅊ;

└ 아니. 그냥 죄다 영어라 뭔 소린지 몰라서 그런 건데. 지금 가글 번역기 돌리고 있음.

└ 미친놈인가.

└ 야 근데 진짜 몬스터 10만 뚫었으면 큰일 난 거 아니냐. 지금까지 일어난 몬스터 웨이브 최대 규모라고 해 봐야 천 마리 안 넘었던 것 같은데;

└ 당연히 이번 웨이브도 초기에는 이 정도 규모 아니었지. 근데 저쪽에 아크 리치가 있는 게 문제야. 그냥 리치만 나타나도 큰 사건인데, 쟤는 학계에도 알려지지 않은 최상위 네임드 몬스터임. 사실상 현재 싸우는 몬스터들 대부분은 아크 리치가 부활시킨 언데드라고 해야 맞다.

└ 아크 리치 : “계왕권 100배.”

└ 그럼 아크 리치만 죽이면 되는 거 아님? 몬스터 대부분이 언데드면 조종자만 죽이면 끝나잖아.

└ ???????

└ 아크 리치를 누가 어떻게 죽이는데, 시벌 놈아. 키보드로 오러 블레이드 쓰는 새끼가 입만 살아 가지고.



치열한 갑론을박.

댓글을 다는 사람 중에는 강 건너 불구경하듯 바라보는 이들도 있었고, 이번 사태를 심각하게 받아들이는 이들도 있었다.

그렇게 종말론과 낙관론이 판을 치는 와중에도 새로운 소식은 끊임없이 업데이트되고 있었다.



(Best댓글) 안보리 오피셜, 한 시간 전 동서부 쪽 전선 뚫림. 다행히 파이 첸이 지원군으로 와서 피해 확산은 막았다고 함.

└ ㄷㄷ진짜네.

└ 동서부 전선이면 우헤이싱 있는 곳 아님?

└ 맞음. 중국 약쟁이 걔.

└ 근데 왜 뚫려. S급 헌터잖아.

└ 중국산 S급 헌터라 그럼.

└ 아…….

└ 파이 첸 없었으면 진짜 큰일 날 뻔했네. 파이 첸은 대격변 출신 웰메이드 헌터라 그런가.

└ 파이 첸은 부모님이 홍콩 국적이라 홍콩산임.

└ 윗 댓글 품질 관리 위원회에서 일하냐? ㅈㄴ 명쾌하네.

└ 그런 김에 한국산 헌터들 소식은 없냐.

└ 정 드래곤은 북부 전선 맡아서 우세 점하는 중이고, 시벌좌는 서부 전선에서 두세 번 승리했다고는 들었는데 그 후로 소식 없는 거 보니까 현상 유지 중인 듯.

└ 음…… 이정룡 실력이야 뭐 다 아니까 걱정은 안 하는데, 시벌좌는 무사하려나. 아직 A급 헌터잖아.

└ ??ㅋㅋㅋㅋ

└ ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ

└ 아직도 시벌좌를 A급 취급하는 순진한 놈이 있눜ㅋㅋㅋㅋㅋㅋㅋㅋ현직 A급 헌터로서 웃음밖에 안 나온다. 진태경 쟤는 그냥 괴물임ㅋㅋ



야야ㅇ야야야!! 지금 안ㄴ보리에서 서ㅂ 전선 현황 발표함!

└ 오, 시벌좌 소식 오랜만이다.

└ 엄청 다급하네. 서부 전선? 뭐라는데?

└ 뚫렸다는데?

└ 어?

└ 어?

└ 뭔 소리야. 설마 시벌좌 죽었음……?

└ 잠깐만. 이게 뭔 내용이지. 얘들아 나 다시 보고 온다. 메인에 떴으니까 너희도 직접 가서 보셈.

└ 아. 갑자기 개후달리네; 당장 들어가 본다.

└ ㄱㄱㄱㄱㄱ



신나게 댓글을 작성하던 네티즌들은 황급히 유엔 안보리 홈페이지에 접속했다.

일시적으로 과도한 접속자가 몰린 탓에 트래픽 초과로 기다리길 한참. 마침내 메인 화면에 뜬 발표 자료을 본 그들은, 자신의 눈과 귀를 의심할 수밖에 없었다.

“……저게 뭐야.”

몬스터 군단과의 대치 상황을 표시해 놓은 지도. 타원형의 전선을 형성한 그곳에는, 송곳처럼 움푹 파고든 서부 전선의 모습이 그려져 있었다.



……방금 확인하고 왔다. 진짜 뚫렸네.

└ 진태경 죽음? 피해 얼마나 됨?

└ 아니, 몬스터 쪽이 뚫렸다고.

└ ??

└ ???

└ 돌파 속도가 너무 빨라서 업데이트가 못 따라간 거였음.

└ ……말이 되냐?

└ 입 다물고 셔터 내려라. 오늘 주모 제삿날이다…….



* * *



곧 치열한 전투가 벌어질 전장은 혼잡했다. 끝없이 펼쳐진 황무지. 무수히 많은 몬스터가 시야에 들어온다.

어디선가 불어온 바람에 놈들이 뿜어내는 짙은 살기와 악취가 묻어 나왔다.

“시부럴 거. 많이도 모였네.”

내 중얼거림에 곁에 서 있던 최 팀장이 대답했다.

“죽여도, 죽여도 끝이 없군요.”

서부 전선에 투입되어 본격적인 전투가 시작된 지 나흘째. 항상 말끔하던 최 팀장의 모습은 더 이상 찾아볼 수 없다.

핏물과 먼지로 뒤덮인 그는 침착하면서도 깊게 가라앉은 눈동자로 날 바라보았다.

“언제 시작합니까?”

“글쎄요, 그건 우리 꼬마 사령관님 의견을 들어 봐야지. 안 그래?”

마지막 물음표는 최 팀장을 향한 것이 아니다.

줄곧 내 곁에서 떨어지지 않고 있던 스물한 살의 ‘꼬마 사령관’. 샤오 쉔이 대답했다.

「저는 진 선생님의 명령에 따르겠습니다!」

녀석의 반짝거리는 눈빛에 실소가 터져 나왔다.

“아직도 그놈의 선생님 타령은. 나한테는 먼저 말 놓으라고 하던 녀석이. 차라리 형님이라고 부르라니까.”

「저, 정말 그래도 됩니까?」

“너만 괜찮으면 된다고 했잖아. 그런데 부하들 보는 앞에서 이래도 되는 거냐? 너 이제 소장 진급 한다며?”

샤오 쉔이 번개 같은 속도로 고개를 저었다.

「아무 문제 없습니다! 혀, 혀, 형님!」

싸울 때는 무서울 정도로 침착한데, 평소에는 왜 이렇게 말을 더듬는지 모르겠다.

나는 뒤에 정렬한 공안무력부 소속의 헌터들을 바라봤다. 자그마치 천여 명에 달하는 숫자.

뜨겁게 달아오른 눈동자에는 강자를 바라보는 선망과 경이로움이 깃들어 있었다.

물론 그중에서도 독보적인 건 샤오 쉔이지만.

「명령을 내려 주십시오. 혀, 형님.」

“명령이라.”

나는 문득 하늘을 올려다봤다.

거대한 날개를 펼친 독수리가 우리의 머리 위를 맴돌고 있었다. 오늘도 느낌이 좋다.

“따라와. 지금껏 해 왔던 것처럼.”

「……!」

“지금 당장.”

나는 대답과 함께 발을 내디뎠다.

쩌저적.

발끝에 실린 만근의 힘에 지면이 거미줄처럼 갈라지며 움푹 꺼진다.

그리고 다음 순간.

쾅!

귀가 먹먹해지는 굉음과 함께, 나는 빛줄기가 되어 쏘아졌다.

‘염화일로(炎火一路).’

추위를 머금은 바람이 달아오르며 열풍으로 변한다.

땅, 바람, 풍경이 빠르게 스쳐 지나가던 그때, 등 뒤에서 거대한 함성이 터져 나왔다.

「돌격! 돌격하라!」

「중화의 후예여! 인민이여! 놈들을 모조리 쓸어버려라!」

「와아아아아!」

두두두두!

캬우우우우!

천지에 울려 퍼지는 인간의 함성과 몬스터의 괴성. 거대한 진동이 지축을 떨어 울린다.

그 혼란의 입구 속에서, 나는 손에 쥔 백염(白炎)을 힘차게 휘둘렀다.

콰아아아!

창날에서 솟아 나온 극양의 강기가, 막아서는 모든 것을 베었다.
```

## Final English reading copy

```markdown
# Chapter 389

It was a day when the cold snap had finally eased.

The students who had at last been freed from the college entrance exam were busy either preparing to retake it or having fun, while office workers boarded public transportation with dark circles hanging heavily beneath their eyes.

Then, in the midst of that peaceful, ordinary routine, a bombshell no one had seen coming dropped.

> **Urgent Breaking News—Major Announcement from the United Nations Security Council**

The video, just over thirty minutes long, began with Chairman Shao Yang staring into the camera with a grave expression.

“I stand before you as the ninth President of the People’s Republic of China and a member of the United Nations Security Council to speak about the massive Monster Wave that has occurred in Sichuan Province.”

It was a bombshell that drew the attention of the entire world and shook all of Asia.

* * *

One day passed, then two, then three. Even after four days, the situation had not calmed down.

There had been countless incidents and disasters since the Great Cataclysm, but the Monster Wave that had occurred in Sichuan Province was unprecedented in scale.

Chairman Shao Yang of China officially declared martial law, and with the approval of the United Nations Security Council, peacekeeping forces were deployed to the front.

The entire world was watching.

The Asian countries bordering China were especially on edge.

Korea was no exception. Even today, the Hunter Issues section of the country’s largest online forum was boiling like a cauldron over charcoal.

**Here’s a summary of the situation so far.**

**There isn’t anyone here who hasn’t watched the Security Council’s major announcement video, right? If there is, go die somewhere. This is a genuine emergency. The supreme leader up north has probably already watched the whole thing on iTube and is lurking on this board, too.**

**Anyway, so many insect bastards kept asking someone to summarize something their own lives depended on that I finally got fed up and wrote this.**

**1. An unexplained massive Wave occurred in Sichuan Province. Current estimated casualties: at least 300,000.**

**Of course, that was a week ago, so the current figure is probably incomparable. At this point, I doubt it’s even possible to gather accurate statistics.**

**2. The Chinese government stepped in, but the scale was far crazier than anyone expected.**

**A monster army numbering at least tens of thousands has gathered around something called an Arch Lich.**

**The People’s Liberation Army and Air Force got absolutely wrecked, while more than two thousand Hunters from the Public Security Armed Forces Department have gone missing. Communications were cut off by magical interference, and satellite surveillance was neutralized, so they can’t even confirm whether those Hunters are alive.**

**3. The Chinese government secretly contacted several countries and hired a number of S-rank Hunters to suppress the situation as quickly as possible. The United Nations peacekeeping forces were deployed to the front two days ago, and they’re fighting desperately.**

**The Security Council is updating the battle situation, so anyone interested can check it out here.**

*(Link attached.)*

**Everything below this is just my personal opinion, so there’s no problem if you skip it.**

**4. Anyone with a properly functioning brain already knows this, but the current situation isn’t merely serious. Mainland China is practically hell on earth.**

**They’re pulling every useful Hunter they can find and sending them to the front, which means the mana levels of other Gates that are being neglected are unstable, too. Hyperinflation is happening in every area.**

**The truly frightening thing is that if the front collapses and the monster army advances beyond Sichuan…… I’ll leave the rest to your imagination.**

**5. So go to the supermarket and buy emergency food before everyone is completely screwed. Of course, I’m not telling you to hoard supplies and make unfair profits.**

**6. It felt like a shame to end it here, so I’m adding some national pride.**

**Our Lord Fuck and the Ares Guild’s Jung Dragon are active on the front. Keep hyping them up as hard as you have been.**

**The end for real.**

Within only a few hours of being uploaded, the post passed 100,000 views and caught fire beneath the comments of netizens who had been watching the situation closely.

> **Best comment:** The situation really is as serious as the post says, but the author is setting the mood way too hard lol. They say S-rank Hunters are fighting alongside 100,000 ordinary Hunters. What’s there to worry about? Is the military just sitting around?
>
> └ Yeah. They’re sitting around in maintenance depots right now.
>
> └ ……?
>
> └ Didn’t you watch the news? All the Chinese military’s Equipment broke down this time, exposing the largest military procurement corruption scandal ever. They say it’s worth at least tens of trillions of won. Apparently, more than one or two divisions are stuck in place.
>
> └ Huh. This sounds like something I’ve heard a lot before.
>
> └ Please change the canteens already, you motherfuckers. I got out last year, but why did the water in my canteen still taste like it came from Normandy? After one sip, I couldn’t even tell whether my name was Kim Cheol Soo or James.
>
> └ Corporal Kim. Tonight’s dinner is boneless pollock braised in sauce.
>
> └ I’m not eating, fuck.
>
> └ Anyway, the military being stuck because of broken Equipment is a problem, but they’ve got manpower to spare, so they’re probably fine. Hunters are the only ones who can actually inflict meaningful damage on monsters, after all. The real problem is something else.
>
> └ What?
>
> └ The monster population has broken through 100,000.
>
> └ ??
>
> └ ?????
>
> └ What do you mean, 100,000? Don’t talk bullshit.
>
> └ It’s not bullshit. It’s official information announced by the United Nations Security Council. Follow the link in the post and check it yourself. It was posted five minutes ago.
>
> └ Wow…… fuck.
>
> └ Judging by the reaction to the comment above, I guess it’s true. Holy shit.
>
> └ No. That’s just because it’s all in English and I don’t understand what it says. I’m running it through Gargle Translator right now.
>
> └ Is this guy insane?
>
> └ Hey, but if the number of monsters really has broken through 100,000, isn’t that a huge problem? Until now, the largest Monster Wave we’d ever seen hadn’t even reached a thousand monsters, had it?
>
> └ Naturally, this Wave wasn’t anywhere near this large in the beginning. The problem is that there’s an Arch Lich over there. Even an ordinary Lich appearing would be a major incident, but that one is an apex named Monster unknown even to academia. Practically speaking, most of the monsters fighting right now are undead resurrected by the Arch Lich.
>
> └ Arch Lich: “Kaioken, times one hundred.”
>
> └ Then can’t we just kill the Arch Lich? If most of the monsters are undead, killing the controller should end everything, right?
>
> └ ???????
>
> └ Who’s going to kill the Arch Lich, and how, you fucking idiot? The guy who uses an Aura Blade with his keyboard has nothing but a mouth.

A fierce debate raged on.

Some of the commenters watched the situation from a safe distance, as though they were watching a fire across a river, while others took the crisis seriously.

Even as doomsday theories and optimism battled for control, new information continued to pour in.

> **Best comment:** Security Council official report: The front in the east-west sector was breached one hour ago. Fortunately, Faye Chen arrived with reinforcements and stopped the damage from spreading.
>
> └ Holy shit, it’s real.
>
> └ If it’s the east-west front, isn’t that where Wu Heixing is?
>
> └ Yeah. That Chinese junkie.
>
> └ But why did it get breached? He’s an S-rank Hunter.
>
> └ Because he’s a Chinese-made S-rank Hunter.
>
> └ Ah……
>
> └ If Faye Chen hadn’t been there, this could’ve become a real disaster. Maybe it’s because Faye Chen is a well-made Hunter forged by the Great Cataclysm.
>
> └ Faye Chen is Hong Kong-made. Her parents had Hong Kong citizenship.
>
> └ Do you work for the comment quality-control committee? That was fucking clear.
>
> └ While we’re at it, does anyone have news about the Korean Hunters?
>
> └ Jung Dragon has taken charge of the northern front and is gaining the upper hand. I heard Lord Fuck won two or three times on the western front, but there hasn’t been any news since then, so I guess he’s maintaining the current situation.
>
> └ Hmm…… I’m not worried about Lee Jungryong, since everyone knows how skilled he is, but is Lord Fuck safe? He’s still an A-rank Hunter, after all.
>
> └ ??ㅋㅋㅋㅋ
>
> └ ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ
>
> └ There’s still an innocent idiot who treats Lord Fuck like an A-rank Hunter lolㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ As a current A-rank Hunter, all I can do is laugh. That Jin Taekyung guy is just a monster lol.

> Hey, hey, h-hey!! The Se-security Council just announced the w-western front status!
>
> └ Oh, news about Lord Fuck. It’s been a while.
>
> └ You sound incredibly frantic. The western front? What does it say?
>
> └ It says it was breached?
>
> └ Huh?
>
> └ Huh?
>
> └ What are you talking about? Don’t tell me Lord Fuck is dead……?
>
> └ Wait. What is this saying? Everyone, I’m going to watch it again and come back. It’s on the main page, so go check it yourselves.
>
> └ Ah. I’m suddenly freaking the hell out; I’m going in right now.
>
> └ Go go go go go.

The netizens who had been enthusiastically writing comments hurriedly accessed the United Nations Security Council website.

An excessive number of visitors had temporarily flooded the site, causing a traffic overload, so they had to wait for quite some time. At last, when the announcement appeared on the main page, they could do nothing but doubt their own eyes and ears.

“……What is that?”

It was a map showing the standoff with the monster army. The front had formed an oval, but the western front had been gouged inward like a spike.

> I just checked. It really was breached.
>
> └ Is Jin Taekyung dead? How bad are the casualties?
>
> └ No, the monsters’ side was breached.
>
> └ ??
>
> └ ???
>
> └ The breakthrough was so fast that the updates couldn’t keep up.
>
> └ ……Does that even make sense?
>
> └ Shut your mouth and pull down the shutters. Today is the Lady of the House’s memorial day….[^1]

[^1]: Korean netizens traditionally call for a tavern proprietress and drinks when celebrating a surge of national pride; the speaker jokes that the tavern is closed because she is dead.

* * *

The battlefield where a fierce battle would soon erupt was crowded. An endless wasteland stretched before us, filled with more monsters than I could count.

The wind blowing from somewhere carried their thick killing intent and stench with it.

“Damn. They sure gathered in force.”

Team Leader Choi, standing beside me, answered my mutter.

“No matter how many we kill, they never seem to end.”

It was the fourth day since we had been deployed to the western front and the battle had begun in earnest. There was no trace left of Team Leader Choi’s usually immaculate appearance.

Covered in blood and dust, he looked at me with calm, deeply sunken eyes.

“When do we begin?”

“Well, we’ll have to hear what our little commander has to say. Right?”

The last question wasn’t directed at Team Leader Choi.

The twenty-one-year-old ‘little commander’ who had remained at my side the entire time answered.

“I’ll follow Teacher Jin’s orders!”

A snort escaped me at his sparkling eyes.

“You’re still on about calling me Teacher. You were the one who told me to drop the formalities first. I told you to call me hyung instead.”

“Are you really sure that’s all right?”

“I told you it was fine as long as you were okay with it. But is this really all right in front of your men? You said you’re getting promoted to major general now, didn’t you?”

Shao Shen shook his head at lightning speed.

“No problem at all! H-hyung, hyung!”

He was frighteningly calm in battle, so I had no idea why he stammered so much in everyday life.

I looked at the Hunters from the Public Security Armed Forces Department lined up behind him. There were roughly a thousand of them.

Their fever-bright eyes held admiration and awe for the strong.

Of course, Shao Shen stood out above all the rest.

“Give the order, h-hyung.”

“The order, huh?”

I suddenly looked up at the sky.

An eagle with enormous wings spread wide circled overhead.

I had a good feeling about today, too.

“Follow me. Just as you’ve done until now.”

“……!”

“Right now.”

I stepped forward as I answered.

Crack.

The force of ten thousand geun packed into my toes made the ground split like a spiderweb and cave inward.

Then, in the next moment—

Boom!

With a deafening roar, I shot forward like a streak of light.

*Flamefire Path.*

The cold-laden wind heated up and transformed into a blast of hot air.

The ground, wind, and scenery flashed past me in an instant. Then a tremendous roar erupted from behind.

“Charge! Charge!”

“Descendants of Zhonghua! People! Sweep them all away!”

“Waaaaaaah!”

Thud-thud-thud-thud!

Kyaaaauuuuu!

The shouts of humans and the howls of monsters rang across heaven and earth. A tremendous vibration shook the foundations of the world.

At the mouth of that chaos, I swung the White Flame in my hand with all my strength.

Whoosh!

The Extreme Yang Force surging from the spearhead cut through everything in its path.
```

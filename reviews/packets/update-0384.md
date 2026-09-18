<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0384.txt",
      "sha256": "6eb54f0157b75e3bccf512101b0943f4dd1f1a75bb80617e6ffe9f24c3218781",
      "bytes": 14681
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "52871c020a8c28bf87d96ad1a8ac2877280193380d6b29e29ff18dc9a8939c72",
      "bytes": 2785
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "42fa027f91faab120864fa37360e0e574903f195a792e9bd2278a4e46ea34fc2",
      "bytes": 133337
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "b45d73c714a019ec67279a7c5baddc99a47880594aa6f405ba392efa53855f24",
      "bytes": 1129
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "2b8cbdc872fa658a9f74385926d17befd27a3f8e4b9c0d9afb1bac9a7b892973",
      "bytes": 622
    },
    {
      "path": "characters/Wei Fenghu.md",
      "sha256": "893a5e219056fd8de323287066ca7a4a77a0c561acbc717cb33c7a0e7ce2e211",
      "bytes": 555
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "6b55f5ee342f42a595e9e5f2d4c4933a177936b8046dcea55d690812b18f53e8",
      "bytes": 104487
    }
  ],
  "estimated_tokens": 10390
}
-->

# Durable State Update — Chapter 384

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 384. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 384. Profile updates may replace only one
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
  "chapter": 384,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 384,
    "continuity_sources": [384],
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

## Prior durable context

```json
{
  "active_continuity": [
    "Jin Taekyung is Level 121, has the Undead Hunter Title, and keeps the strengthened Skeleton Warlord in his Inventory under the mocking name Bones.",
    "The Arch Lich's three incomplete Liches were destroyed at Chengdu International Airport, and their testimony identified the Arch Lich as responsible for the undead army's actions.",
    "Wei Fenghu is China's Minister of National Defense under the Central Military Commission, a four-star general, and the current Chairman's right-hand man.",
    "Sichuan Province is in a wartime emergency involving magical communications interference, flying-monster attacks, and a Monster Wave that began in Gaoping District of Nanchong City.",
    "China has deliberately concealed at least one of its S-rank Hunters, Lei Fei, who led the Public Security Armed Forces Department stationed in Sichuan Province.",
    "Lei Fei disappeared with his department's Hunters when the first Monster Wave began, and neither his death nor his survival has been confirmed.",
    "Wei Fenghu is Lei Fei's maternal uncle, raised him as his own son, believes he is alive, and asked Jin Taekyung to bring him back if found.",
    "Jin Taekyung agreed to Wei Fenghu's request but did not guarantee that Lei Fei would be found alive.",
    "The temporary operations headquarters is at Mount Qingcheng."
  ],
  "continuity_sources": [
    383,
    382
  ],
  "open_questions": [
    "Who is the Arch Lich, and what will happen after Jin Taekyung destroys its three servants?",
    "What happened to Lei Fei and the Hunters who disappeared with him?",
    "What happened to the Second Fiend assigned to the Qingcheng attack?",
    "Who is the unidentified person directing Aehyang, and what are they planning?",
    "What is the true nature and purpose of the Lord of Heaven, and what became of the Western Heaven Demon Lord?"
  ],
  "safe_through": 383,
  "temporary_decisions": [
    "Render 열화신룡 as Blazing Flame Divine Dragon, distinct from Huashan Divine Dragon; use Mimi and Mimi-chan for 미미 and 미미쨩, and Third Fiend and Three Fiends for 삼괴.",
    "Render 진인 as Perfected One, 도우 as Fellow Daoist, 신니 as Venerable Nun, 환영진 as illusion formation, and 이동진 as Moving Formation.",
    "Render 독룡각 as Poison Dragon Pavilion, 가주 대행 as Acting Family Head, 화룡갑 as Fire Dragon Armor, and 공안무력부 as Public Security Armed Forces Department.",
    "Render 사기 as death energy, 의념 as conveyed thoughts, 데스나이트 as Death Knight, 골골 as Bones, and 아크 리치 as Arch Lich.",
    "Render 대교 as Senior Colonel, 동지 as Comrade, 견마지로 as utmost loyalty, and 옥체 as august self; preserve the gukbap wordplay."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 살기     | **killing intent**                               |                                                       |
| 대주     | **Squad Leader** / **Commander**             |
| 생도     | **cadet**                                    |
| 칭호               | **Title**                      |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 레이드     | **raid**              |
| 길드      | **Guild**             |
| 팀장      | **Team Leader**       |
| 마법사     | **mage**              |
| 사천     | **Sichuan**            |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 웨이펑후 | **Wei Fenghu** | Minister of National Defense under China's Central Military Commission. |
| 나비 | **Nabi** | Name used for the black kitten Familiar. |
| 주신 | **God of Drinking** | Wipeng's drinking epithet. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 국밥 | **gukbap** | Korean dish of rice served in hot soup; footnoted in the reading copy. |
| 시벌좌 | **Lord Fuck** | Crude online nickname created from Taekyung's accidental broadcast profanity. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 메이지 | **Mage** | Skeleton subtype mentioned alongside Soldiers and Warriors. |
| 존슨 | **Johnson** | Co-host of the American talk show that replays Taekyung's viral interview. |
| 미국 | **United States** | Country associated with the talk show and CNM. |
| 중국 | **China** | Country from which Team Leader Choi’s video originates. |
| 쓰촨성 | **Sichuan Province** | Source spelling variant of the established Sichuan location. |
| 중화인민공화국 | **People's Republic of China** | Formal country name shouted by the Chinese Hunters. |
| 주석 | **Chairman** | Political title used for Xiao Yang. |
| 청성 | **Qingcheng** | Short form for Qingcheng Sect. |
| 청성산 | **Mount Qingcheng** | Mountain containing the Qingcheng Sect. |
| 사천성 | **Sichuan Province** | Province form used in the title of its chief official. |
| 국방부 | **Ministry of National Defense** | Government ministry referenced in Taekyung's comparison about the steady passage of time. |
| 오대 | **Five Squads** | Named Tang Clan organizational group in Tang Sadok's mobilization order. |
| 삼문혈사 | **Three-Gate Bloodbath** | Name given to Dark Heaven’s coordinated assault on the Tang Clan, Qingcheng, and Emei. |
| 중화 | **Zhonghua** | Patriotic term used in Shao Shen’s rallying speech. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 웨이펑후 | 진태경 | senior_military_official_to_ally | Mr. Jin | formal-polite | Wei Fenghu addresses Jin while inviting him to walk to the operations headquarters. |
| 진태경 | 웨이펑후 | Foreign Hunter to senior military official | General, Commander, or Supreme Leader | Polite but flustered | Jin jokingly cycles through grand titles while trying to interrupt Wei's emotional request. |

## Listed compact profiles

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 382
- **Aliases:** Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, and a Supreme Peak master who has manifested Force.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother; Jeok Cheongang is his Master; Cheongpung is his trusted companion and only true martial rival; his mother and sister Hayeon are among those he protects.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 382
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Wei Fenghu.md

# Wei Fenghu (웨이펑후)

- **Safe through:** Chapter 383
- **Aliases:** None
- **Role:** Wei Fenghu is the Minister of National Defense under China's Central Military Commission and a four-star general.
- **Personality:** Courteous, reserved, and authoritative.
- **Voice:** Formal and measured, addressing Jin as Mr. Jin.
- **Relationships:** Wei Fenghu is Lei Fei’s maternal uncle who raised him as his own son, and he has asked Jin Taekyung to bring Lei Fei back if he is found.

## Korean source

```text
＃384화



청성산(靑城山).

아득한 세월을 간직한 도교의 성지.

그 준엄하고도 압도적인 산세를 마주한다면, 그 누구라 해도 순간 할 말을 잃고 바라보게 된다.

그러나 나는 전혀 다른 의미에서 놀라움을 느끼고 있었다.

‘분명 다르지만…… 닮았어.’

무림의 청성산. 그리고 21세기 현대의 청성산.

지금껏 내가 경험해 온 두 세상은 많은 부분을 닮았다. 무림에서의 지형, 언어, 사람들의 용모와 생활 양식까지.

한때는 어쩌면 무림은 현대의 머나먼 과거가 아닐까, 고민한 적이 있을 정도였다.

‘하지만 아니었지.’

나비효과? 영화에서나 보던 일이 일어났을 리가.

두 세상은 분명 닮았지만, 미묘한 차이가 있었고 역사도 달랐다.

또한 무림의 세상은 현대의 그것보다 좁고 오대양 육대주로 갈라져 있지도 않다.

이역만리의 이국땅에 색목인들이 살기는 하나 그뿐. 거대한 대국의 통치 아래 존재하는 대륙이 저쪽 세상의 중심이다.

중국 사람들이 지겹도록 주장하는 중화(中和)가 곧 무림일지도 모르겠다.

‘그런데 하필이면 이런 것까지 닮았냐.’

사천성을 무자비하게 피로 물들였던 삼문혈사(三門血史)를 겪고 돌아오자마자 쓰촨성의 청성산에 오다니.

단순한 우연인지, 지독한 악연인지 모르겠다.

부디 그런 것까지 닮진 않았으면 좋겠는데…….

「진 선생?」

“진태경 씨.”

“아.”

나는 잠에서 깨어난 사람처럼 고개를 쳐들었다.

어느새 비즈니스 제트기에서 내린 웨이펑후와 최 팀장이 나를 묘한 눈빛으로 바라보고 있었다.

“죄송합니다. 경치에 잠깐 한눈팔려서.”

「이토록 어두운데 청성산의 절경을 볼 수 있다니. 진 선생께서는 대단한 마나의 소유자시군.」

그것도 틀린 말은 아니지만, 초절정의 경지에 오른 지금은 굳이 공력 없이도 어지간하면 안력(眼力)으로 꿰뚫어 볼 수 있다.

내가 미묘한 얼굴로 고개를 끄덕이자 웨이펑후가 감탄했다.

「과연, 한국이 진 선생을 왜 그리 꼭꼭 숨겨 두었는지 이제야 알 것 같구려. 나라의 얼굴이라 할 만한 S급 헌터답소이다.」

“예? 저 아직 자격증으로는 A급인데요.”

「굳이 숨길 필요 없소. 본국에서도 어느 정도는 파악하고 있으니.」

뭐라 말하기도 전에 웨이펑후가 청산유수처럼 말을 이었다.

「S급 헌터가 되기 위해서는 끊임없는 정신 수양과 고된 수련을 통해 깨달음을 얻어야 하는 법. 본국도 수많은 시행착오를 겪어 가며 지금의 헌터들을 육성했는데…… 진 선생처럼 젊은 나이에 그런 경지에 올랐다는 것은 한국 정부의 전폭적인 지원이 있었다는 뜻이겠지.」

“……?”

“……?”

「아, 물론 옆에 계신 최 선생도 훌륭한 헌터요. 이런 분들이 함께하니 나로서는 든든할 뿐이오.」

이게 무슨 든든하게 국밥 말아먹는 소리냐.

짧은 순간 시선을 교환한 나와 최 팀장은 무언의 합의를 보았다.

‘입 다물자.’

‘그냥 갑시다.’

내가 너무 비현실적으로 이 자리까지 올라왔기 때문에 벌어진 해프닝인 듯싶은데, 이미 저쪽에서 붙인 딱지를 굳이 우리 손을 떼 줄 필요는 없다.

당장 이 자리에서 웨이펑후를 납득시키기도 귀찮고.

“음, 약간 오해가 있으신 것 같은데, 때가 되면 제가 차차 말씀드릴게요.”

「오해랄 것 있겠소. 서로 다 사정 아는 처지에.」

“…….”

“…….”

「주석께서도 이미 알고 계신 사안이니, 뵙게 되면 구태여 부정하지 말고 그러려니 하시오.」

알긴 뭘 알아. 나는 피식 웃었다.

‘그나저나 주석이라.’

중화 인민공화국에 존재하는 10억여 명의 인구와 경제, 군사를 한 손에 틀어쥔 왕 같은 존재.

초절정의 경지에 오른 지금에도 현대의 상식이 뿌리박힌 내게 그는 가까우면서도 한없이 먼 존재다.

이번 일이 끝나면 얼굴이나 한 번 볼 수 있으려나?

뭐, 무슨 상관이겠나. 이건 한참 나중에 생각해야 할 문제다.

레이드 수당을 제외하더라도 주급이 무려 백억. 지금의 내게는 손 큰 고용주일 뿐이다. 사람도 구하고, 돈도 버니 일석이조다.

“그렇게 하겠습니다. 뵙게 되면요.”

「좋소. 그럼 뵈러 갑시다.」

“예?”

「내가 말하지 않았나? 지금 지하 벙커에서 기다리고 계시오.」

아니, 이게 도대체 뭔 상황이야.

앞서가는 웨이펑후의 뒷모습을 멍하니 바라보던 나는 최 팀장에게 다가가 빠르게 속삭였다.

“바, 방금 들으셨어요?”

“예, 들었습니다. 하지만 저로서도 좀 의외로군요. 국가 주석이 안전한 베이징을 놔두고 여기까지 오다니. 세간의 평가가 어느 정도 사실인 모양입니다.”

“세간의 평가고 나발이고. 중국 종석이, 종석이가!”

“종석이가 아니라 총서기! 국가 주석이라고!”

「음? 방금 뭐라 하셨소?」

「아무것도 아닙니다. 국방부장님.」

문득 뒤돌아본 웨이펑후를 향해 정중하게 둘러댄 최 팀장이 지금껏 본 적 없는 아주 진지하고 간절한 표정으로 말했다.

“진태경 씨. 주석 앞에서 지금 같은 말실수는 하면 안 됩니다. 아시겠죠? 특히 종석이 얘기는 말도 꺼내지 마세요. 무슨 고등학교 동창 이름도 아니고.”

“어? 어떻게 아셨어요?”

“…….”

방금 최 팀장이 시발이라고 한 것 같은데. 기분 탓이겠지.

나는 깊게 심호흡하며 속으로 중얼거렸다.

‘종석이 아냐. 총서기야. 중국 주석이야.’

태생부터 성골 귀족이었던 최 팀장과 달리 나는 뼛속까지 소시민이다.

평소 중국에 어떤 감정을 품고 있었건 간에, 세계에서 열 손가락 안에 꼽히는 강대국의 지도자를 만난다는 사실에 가슴이 쿵쿵 뛰었다.

‘실수만 하지 말자. 특히 종석이.’

그리고 십 분 후, 나는 깊숙한 지하 벙커에 모인 주요 인물들의 시선을 받으며 중화인민공화국의 지도자와 악수를 나누었다.

「반갑소, 진 선생. 이 늙은이는 중화인민공화국의 국가 주석을 맡고 있는 샤오 양이라 하오.」

좋아, 종석이의 종자도 꺼낼 일은 없다. 한고비를 넘긴 나는 편안한 마음으로 입을 열었다.

“어서 오세요.”

「……?」

“……?”

아, 시벌.



* * *



중국 공산당 중앙군사위원회 주석이자 총서기. 그리고 10억 명이 넘는 인민들의 정점에 선 국가 주석.

샤오 양(Shao Yang).

사람들을 향한 그의 목소리는 부드럽고, 눈빛에는 힘이 실려 있었다.

「여러분도 알다시피, 안타깝게도 나는 군사 전문가도, 뛰어난 장군도 아니오. 일찍이 정치에 몸담아 나이 일흔이 되어서야 작은 뜻을 이룬 협잡꾼일 뿐이지.」

스스로를 협잡꾼이라 지칭하는 말은, 지구에서 네 번째로 거대한 국토와 제일의 인구수를 지닌 국가 수장의 입에서 나온 말이라곤 믿기지 않을 정도로 파격적이었다.

‘이런 뜻이었나? 최 팀장이 말했던 세간의 평가라는 게.’

대충 어떤 사람인지 알 것 같은 느낌이다.

어쩌면 그저 사람들 앞에서 꺼내 든 가면이나 위선일 수도 있다.

하지만 적어도 지금 나를 포함한 모두의 앞에서 말을 이어 가는 노인, 샤오 양 중국 주석에게는 그런 것과는 전혀 다른 종류의 기(氣)가 느껴졌다.

「최선을 다해 주시오. 부디 한 명이라도 더 많은 인민을 구하고, 하루빨리 이 끔찍한 참사를 막아 주시오. 만약 그리 해 주신다면 나는 여러분과 여러분의 나라에 합당한 고마움을 표시하고 이번에 준 도움을 오래도록 기억할 거요.」

사실 저 노인이 어떤 인생을 살아왔고 어떤 정책을 펼치는지 나는 모른다.

다만 자국의 사람들을 구하기 위해 세계 각국에 도움의 손길을 뻗었다는 것에는 큰 점수를 주고 싶다.

「이 늙은이의 말은 여기까지요. 여러분들은 부디 정치와 같은 복잡한 문제는 신경 쓰지 말고, 최소의 희생으로 이 사태를 막을 수 있는 최선의 방도를 찾아 주시길 간곡히 부탁하겠소.」

정치에 일평생을 바친 늙은 정객(政客)은 고개를 돌려 한 사람을 바라보았다.

「웨이펑후 국방부장. 내 오랜 벗이여.」

「예. 존경하는 주석 동지.」

「중앙군사위원회의 전권을 원하나?」

잠시 망설이던 웨이펑후가 무겁게 고개를 끄덕였다.

「그렇습니다.」

「자네라면 그 힘을 잘 사용할 수 있겠지. 하지만 거절하겠네.」

「……주석 동지?」

「회의가 끝나면 명령서를 가져오게. 모든 일의 전권도, 책임도 내가 질 테니.」

순간 중국 종석이가 왜 저러나 싶었는데, 이제 보니 모두 자신이 안고 가겠다는 의지의 표명이었다.

그 광경을 지켜보던 최 팀장이 옆에서 중얼거렸다.

“좋은 리더군요.”

나는 작게 고개를 저었다.

“아뇨. 저한테는 최 팀장님이 최곱니다.”

“진태경 씨…….”

“그러니까 길드 정산 비율 좀 올려 주세요.”

“진태경 씨…….”

같은 말, 다른 느낌.

니 새끼가 그럼 그렇지, 하는 눈빛으로 나를 바라본 최 팀장이 고개를 젓던 그때였다.

「주석께서 퇴장하십니다.」

서기관의 말에 앉아 있던 모두가 자리에서 일어났다. 국가 원수에 대한 최소한의 예우다.

「모쪼록 무운을 비오.」

주석은 이 자리에 있는 한 사람, 한 사람과 눈을 맞추며 말을 건넸다. 물론 나 역시 예외는 아니었다.

그것도 하필이면 맨 마지막에 걸렸다.

「진 선생.」

“……예.”

나를 바라보는 주석의 입가에 희미한 미소가 스쳤다.

「내 진 선생에게 거는 기대가 아주 크오. 비록 서로가 필요로 하는 것을 주고받는 계약이라지만, 어떤 상황에서도 인명을 우선해 주었으면 좋겠소.」

기분 탓인가, 다른 사람들에 비해 유난히 긴 인사말이다. 나는 사람들의 시선을 느끼며 고개를 끄덕였다.

“알겠습니다.”

「부디 꼭 큰 힘이 되어 주시구려.」

그 말을 끝으로 돌아서려던 주석이 멈칫 발걸음을 멈췄다. 그리고 한 마디를 툭 던졌다.

「어서 오시오.」

“…….”

「그럼 이만.」

주석을 배웅하기 위해 동석하고 있던 중국 고위 관계자들이 사라지고, 나는 의자에 털썩 주저앉았다.

‘시벌.’

만약 내가 죽는다면 사인은 수치사다. 설령 몬스터한테 죽는다고 해도 사인은 수치사로 하기로 했다.

‘으아, 으아아아아!’

마음속으로 온 사방을 향해 울부짖는 내 발을 무언가가 지그시 밟았다. 보나 마나 옆에 앉은 최 팀장이 분명했다.

“왜요.”

최 팀장이 작게 헛기침을 내뱉었다.

“크흠.”

“뭐요.”

“크흐흠. 사람들, 사람들.”

“아.”

주위를 둘러본 나는 그제야 깨달았다. 지하 벙커 안, 남녀와 인종이 뒤섞인 십여 명의 사람들이 나를 주시하고 있었다는 것을.

그리고 그중에서도 특히 눈에 띄는 네 사람이 있었다.

‘저들은…….’

중국인 남녀 한 쌍. 그리고 각각 초록빛과 푸른빛을 띤 서양인 사내 둘.

시선을 마주한 것만으로도 느껴진다. 그들의 몸 안에 웅크린 거대한 기운이.

놀랍다기보다는 당연하다는 생각이 앞섰다. 저 네 사람의 정체를 아는 이들이라면 누구나 나와 같을 것이다.

‘S급 헌터.’

존재 자체가 이슈인 사람들. 전 세계에 존재하는 수많은 헌터 중에서도 정점에 선 이들.

TV와 광고에서 지긋지긋하게 보던 얼굴들이 내 눈앞에 있었다.

그리고 지금, 그중 한 사람이 일어나 내게 손을 내밀었다.

「만나서 반가워. 나는……. 아, 혹시 영어를 잘 모르나? 통역 마법을 써 줄 수도 있는데.」

먼저 말을 걸어 줄 거라고는 생각지도 못했다. 나는 얼떨떨한 얼굴로 그가 내민 손을 맞잡으며 대답했다.

“아닙니다. 괜찮아요.”

「오, 이 친구 발음 보게. 미국인이라고 해도 믿겠는데.」

중년의 흑인. 2미터를 훌쩍 넘기는 거구의 그가 푸른 눈을 빛내며 물었다.

「내가 누군지 아는 것 같은데. 안 그래?」

모를 리가 있나. 나는 샤오 양 주석을 마주했을 때보다 더한 떨림을 느끼며 대답했다.

“물론입니다, 매직 존슨(Magic Johnson).”

전 세계에서 오직 세 명만이 부여받은 대마법사의 칭호.

눈앞의 흑인, 매직 존슨은 그 대마법사 중에서도 가장 전투에 특화되어 있다는 워 메이지(War Mage)다.

‘매직 존슨이랑 이야기를 하다니. 살다 보니 이런 날도 다 오네.’

여러모로 오길 잘했다고 생각하는 내게, 세계 최고의 워 메이지가 활짝 웃으며 말을 건넸다.

「하하. 알아봐 주니 고맙군. 사실 나도 전부터 널 알고 있었어.」

“저, 절요?”

「당연하지. 올해 초등학교에 입학한 내 막내딸도 시벌좌를 아는걸.」

“…….”

아니, 저 염병할 별명은 도대체 어디까지 알려진 거야.

시벌좌라는 별명이 영미권에서는 뭐라고 불리려나. 퍽 가이? 퍽 맨?

매직 존슨의 어린 막내딸이 나를 그런 이름으로 알고 있다고 생각하니 하나도 기쁘지 않다.

그리고 기분이 좋지 않은 것은 나뿐만이 아니었던 모양이었다.

「천박하기 짝이 없는 별명이군. 뭐, A급 헌터 나부랭이에게 딱 어울리긴 하지만.」

이제 막 서른쯤 되었을까. 비교적 젊어 보이는 중국인 사내가 비스듬히 팔짱을 끼며 나를 응시했다.

「안 그래, 반도의 빵즈?」

최 팀장이 말릴 틈도 없었다. 이미 내 목소리는 자동 응답기처럼 흘러나온 후였으니까.

“뭐래, 대륙 짱깨 새끼가.”
```

## Final English reading copy

```markdown
# Chapter 384

Mount Qingcheng.

A sacred Taoist site bearing the imprint of ages.

Anyone who stood before its stern, overwhelming mountain ridges would lose their words for a moment and stare.

But I was amazed for an entirely different reason.

*It’s definitely different…but it’s similar.*

Mount Qingcheng in the Murim. Mount Qingcheng in the modern twenty-first century.

The two worlds I had experienced so far resembled each other in many ways. Their terrain, languages, people’s features, and lifestyles were all similar.

At one point, I had even wondered if the Murim might be the distant past of the modern world.

*But it wasn’t.*

The butterfly effect? It wasn’t like something I had only seen in movies could really happen.

The two worlds were certainly similar, but they had subtle differences, and their histories were different as well.

The Murim world was also smaller than the modern one, and it wasn’t divided into five oceans and six continents.

There were people with colored eyes living in far-off foreign lands, but that was all. The continent ruled by a vast Great Nation was the center of that world.

Perhaps the Zhonghua that Chinese people insisted on so tiresomely was the Murim itself.

*But why did even this have to be similar?*

I had just returned from the Three-Gate Bloodbath, which had mercilessly dyed Sichuan Province in blood, only to come to Mount Qingcheng in Sichuan Province.

I couldn’t tell whether it was a simple coincidence or a terrible connection.

I really hoped it wouldn’t be similar in that way, too…

“Mr. Jin?”

“Mr. Jin Taekyung.”

“Ah.”

I raised my head like someone waking from sleep.

Wei Fenghu and Team Leader Choi had already gotten off the business jet and were looking at me strangely.

“Sorry. I got distracted by the scenery for a moment.”

“It is so dark, yet you can see the beauty of Mount Qingcheng. You truly possess extraordinary mana, Mr. Jin.”

That wasn’t wrong, but now that I had reached the Supreme Peak realm, I could generally see clearly with my eyesight alone, without relying on internal energy.

When I nodded with a complicated expression, Wei Fenghu admired me.

“Now I understand why Korea has hidden you away so carefully, Mr. Jin. You are worthy of being called an S-rank Hunter—the face of your nation.”

“Excuse me? I’m still officially A-rank.”

“There is no need to hide it. Our country has already grasped the situation to some extent.”

Before I could say anything, Wei Fenghu continued smoothly.

“To become an S-rank Hunter, one must attain enlightenment through relentless mental cultivation and arduous training. Our country also had to endure countless trials and errors to foster its current Hunters…but to reach such a realm at an age as young as yours means that the Korean government must have given you its full support.”

“…?”

“…?”

“Of course, Mr. Choi beside you is also an excellent Hunter. With people like the two of you working together, I feel reassured.”

*What kind of reassuring gukbap nonsense is that?*[^1]

Team Leader Choi and I exchanged a brief glance and reached a silent agreement.

*Keep your mouths shut.*

*Let’s just go.*

It seemed to be a misunderstanding brought about by the fact that I had reached this position in such an unrealistic way. But there was no reason for us to remove the label they had already stuck on us.

Besides, it would be annoying to convince Wei Fenghu right here.

“Hmm. I think there’s been a slight misunderstanding, but I’ll explain everything bit by bit when the time comes.”

“What is there to misunderstand? We both know each other’s circumstances.”

“…”

“…”

“Even the Chairman already knows about the matter. When you meet him, do not bother denying it. Just accept it as it is.”

*Knows what?* I let out a quiet laugh.

*Speaking of the Chairman…*

He was a kinglike figure who held more than a billion people, the economy, and the military of the People’s Republic of China in one hand.

Even now that I had reached the Supreme Peak realm, he was a being who felt close yet infinitely distant to me, a man with modern common sense rooted in his bones.

*I wonder if I’ll get to see his face after this is over.*

Well, what did it matter? That was a problem to think about much later.

Even without my raid pay, my weekly salary was ten billion won. To me, he was simply a generous employer.

I got to save people and make money—two birds with one stone.

“I’ll do that. When I meet him.”

“Good. Then let us go meet him.”

“Excuse me?”

“Did I not tell you? He is waiting in the underground bunker right now.”

*What the hell was going on?*

I stared blankly at Wei Fenghu’s back as he walked ahead, then approached Team Leader Choi and whispered quickly.

“D-Did you hear that?”

“Yes, I did. But it is unexpected for me as well. For the Chairman of China to leave the safety of Beijing and come all the way here… It seems the public perception of him is at least partly accurate.”

“To hell with public perception. China’s Jongseok—Jongseok!”

“Not Jongseok, General Secretary! The Chairman!”

“Hmm? What did you just say?”

“Nothing, Minister.”

Team Leader Choi politely covered for us when Wei Fenghu suddenly turned around. Then, with an earnest and serious expression I had never seen on him before, he said,

“Mr. Jin Taekyung. You must not make the same kind of verbal mistake in front of the Chairman. Understood? Especially do not even mention Jongseok. It sounds like the name of some high school classmate.”

“Huh? How did you know?”

“…”

*I think Team Leader Choi just said fuck.*

*Must be my imagination.*

*It’s not Jongseok. It’s General Secretary. China’s Chairman.*

Unlike Team Leader Choi, who had been born into the aristocratic elite, I was an ordinary citizen to my core.

No matter what feelings I had normally held toward China, my heart pounded at the thought of meeting the leader of one of the ten most powerful nations in the world.

*Let’s just not make any mistakes. Especially not Jongseok.*

Ten minutes later, beneath the ground in a deep underground bunker, I shook hands with the leader of the People’s Republic of China while receiving the gazes of all the important people gathered there.

“Nice to meet you, Mr. Jin. This old man is Shao Yang, the Chairman of the People’s Republic of China.”

*Good. There was no reason to bring up even a syllable of Jongseok.*

Having cleared that hurdle, I opened my mouth with a relaxed expression.

“Welcome.”

“……?”

“……?”

*Ah, fuck.*

* * *

Chairman of the Chinese Communist Party’s Central Military Commission and General Secretary.

The Chairman who stood at the apex of more than a billion people.

Shao Yang.

His voice directed at the people was gentle, while strength filled his eyes.

“As you all know, unfortunately, I am neither a military expert nor an outstanding general. I am merely a political schemer who entered politics early and managed to achieve one small ambition only after reaching the age of seventy.”

The fact that the leader of the country with the fourth-largest territory on Earth and the largest population called himself a schemer was so unconventional that it was hard to believe the words had come from his mouth.

*So this is what Team Leader Choi meant by the public perception of him?*

I felt as though I had a rough idea of what kind of person he was.

Perhaps it was merely a mask or hypocrisy he had put on before the people.

But at least from the old man speaking before all of us now, including me—Shao Yang, the Chairman of China—I sensed a kind of qi utterly unlike either of those things.

“Please do your best. I ask you to save as many more people as possible and stop this terrible disaster as quickly as you can. If you do so, I will show you and your countries my proper gratitude and remember the help you have given us for a long time.”

The truth was, I didn’t know what kind of life that old man had lived or what policies he had pursued.

But I wanted to give him considerable credit for reaching out to countries around the world for help in order to save his own people.

“That is all this old man has to say. Please do not concern yourselves with complicated matters such as politics. I earnestly ask you to find the best way to stop this situation with the fewest possible sacrifices.”

The old political veteran who had devoted his entire life to politics turned his head and looked at one man.

“Minister of National Defense Wei Fenghu. My old friend.”

“Yes, my respected Chairman Comrade.”

“Do you want the Central Military Commission’s full authority?”

Wei Fenghu hesitated for a moment before heavily nodding.

“That is correct.”

“You could use that power well. But I must refuse.”

“…Chairman Comrade?”

“When this meeting is over, bring me the orders. I will take both full authority over everything and responsibility for everything.”

For a moment, I wondered why China’s Jongseok was acting like that.

But now I understood. He was declaring that he would shoulder everything himself.

Team Leader Choi, who had been watching the scene beside me, murmured,

“He’s a good leader.”

I quietly shook my head.

“No. To me, you’re the best, Team Leader Choi.”

“Mr. Jin Taekyung…”

“So please raise my Guild settlement percentage.”

“Mr. Jin Taekyung…”

Same words. A completely different feeling.

Team Leader Choi was looking at me with an expression that said, *Of course you’d say that, you bastard*, when he shook his head.

“The Chairman is departing.”

At the secretary’s words, everyone who had been seated stood up. It was the minimum courtesy owed to the head of state.

“I wish you all good fortune.”

The Chairman spoke to everyone present, meeting each person’s eyes in turn. Of course, I was no exception.

Unfortunately, I was the very last one.

“Mr. Jin.”

“…Yes.”

A faint smile touched the corners of the Chairman’s mouth as he looked at me.

“I have very high expectations of you, Mr. Jin. Although this is a contract in which we exchange what we each need, I hope you will prioritize human lives in any situation.”

Was it my imagination, or was his farewell unusually long compared to those he had given everyone else?

Feeling the eyes of the others on me, I nodded.

“Understood.”

“Please be a great source of strength to us.”

The Chairman turned to leave, then suddenly stopped. He tossed out one last remark.

“Welcome.”

“…”

“Then I’ll take my leave.”

After the senior Chinese officials who had been present to see the Chairman off disappeared, I sank into a chair.

*Fuck.*

If I died, the cause of death would be death by humiliation.

Even if a monster killed me, I would have the cause of death recorded as death by humiliation.

*Aagh, aaaaaagh!*

As I screamed in every direction inside my mind, something firmly stepped on my foot.

It was obviously Team Leader Choi, who was sitting beside me.

“Why?”

Team Leader Choi gave a small cough.

“Ahem.”

“What?”

“Ahem. People. People.”

“Oh.”

I looked around and finally realized that a dozen or so men and women of various races were staring at me inside the underground bunker.

Four of them stood out in particular.

*Those people are…*

A Chinese man and woman.

And two Western men, one tinged green and the other blue.

I could feel it simply from meeting their gazes—the enormous mana coiled inside their bodies.

Rather than being surprised, I felt that it was only natural. Anyone who knew the identities of those four people would have thought the same way I did.

*S-rank Hunters.*

People who were news simply by existing. The individuals at the very top among the countless Hunters in the world.

The faces I had grown sick of seeing on television and in commercials were right before my eyes.

And now, one of them stood up and extended a hand to me.

“Nice to meet you. I’m… Ah, do you happen not to know English? I can use translation magic for you.”

I had never expected him to speak to me first.

I shook his offered hand with a dazed expression and answered,

“No, it’s fine.”

“Oh, listen to that pronunciation. I’d believe you were American.”

He was a middle-aged Black man, a giant well over two meters tall. His blue eyes glinted as he asked,

“You seem to know who I am. Don’t you?”

How could I not?

I felt even more nervous than I had when I met Chairman Shao Yang.

“Of course, Magic Johnson.”

The title of Archmage, bestowed on only three people in the entire world.

Magic Johnson, the Black man standing before me, was a War Mage—the most combat-focused of those Archmages.

*I’m actually talking to Magic Johnson. I never thought I’d live to see the day.*

As I thought that coming here had been the right choice in more ways than one, the world’s greatest War Mage smiled broadly and spoke to me.

“Haha. Thank you for recognizing me. Actually, I’ve known about you for a while.”

“Y-You know me?”

“Of course. Even my youngest daughter, who started elementary school this year, knows Lord Fuck.”

“…”

*Just how far has that damn nickname spread?*

I wondered what Lord Fuck would be called in the English-speaking world.

*Fuck Guy? Fuck Man?*

The thought of Magic Johnson’s young youngest daughter knowing me by that name did not make me happy in the slightest.

Apparently, I wasn’t the only one who was displeased.

“What a vulgar nickname. Though I suppose it does suit a little A-rank Hunter like you.”

The Chinese man who had just turned thirty, or perhaps was about to, watched me with his arms folded.

“Isn’t that right, you peninsula bangzi?”[^2]

Team Leader Choi had no time to stop me.

My voice had already spilled out like a prerecorded response.

“What the hell are you talking about, you mainland chink bastard?”

[^1]: *Gukbap* is rice served in hot soup. Here, Taekyung twists Wei Fenghu’s confident reassurance into a joke about “hearty” gukbap.

[^2]: *Bangzi* is a derogatory Chinese term for Koreans; “peninsula” refers to Korea.
```

<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0385.txt",
      "sha256": "217b2c833411a34181d7cf7d6068f8c3e37be5a3a0964233cab5516014cdb89d",
      "bytes": 16200
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "8669b2b697d69987b13580c644d6eebc91239dd4c7884da268ee207b848aa72a",
      "bytes": 3407
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "fca64678a95151fd8b5fd88ce860551a57c5d71d9071d28823f1ea2a5473afe3",
      "bytes": 133451
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "e69f8c2e487ba0fc404eddc182ba92ddcb2efd2231973015da4f3e1bfd79e02f",
      "bytes": 1129
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "115bd977e84d8e5c79f44595a79c137134ebaab59b68eb6870834673af1dbb6d",
      "bytes": 622
    },
    {
      "path": "characters/Lee Jungryong.md",
      "sha256": "8bb0587b42dc4238f73293114a81b95b36e683e9e080e1bf5740a2423205ec37",
      "bytes": 1396
    },
    {
      "path": "characters/Wei Fenghu.md",
      "sha256": "20ca561395d308b69cbfd420bb65804490c23e7dbccaab75de42b2483c21f48a",
      "bytes": 555
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "25cf9ee69f291fe3bf126bab7e9f240731e283fed1356be3a24c929e4d4e11ba",
      "bytes": 106470
    }
  ],
  "estimated_tokens": 11606
}
-->

# Durable State Update — Chapter 385

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 385. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 385. Profile updates may replace only one
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
  "chapter": 385,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 385,
    "continuity_sources": [385],
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
    "The temporary operations headquarters is at Mount Qingcheng.",
    "Shao Yang is the Chairman of the People's Republic of China, Chairman of the Chinese Communist Party's Central Military Commission, and General Secretary.",
    "Shao Yang has retained full authority and responsibility for directing China's response to the crisis while asking the Hunters to prioritize human lives.",
    "International S-rank Hunters are gathered at the underground headquarters, including Magic Johnson, one of the world's three Archmages and its most combat-oriented War Mage."
  ],
  "continuity_sources": [
    384
  ],
  "open_questions": [
    "Who is the Arch Lich, and what will happen after Jin Taekyung destroys its three servants?",
    "What happened to Lei Fei and the Hunters who disappeared with him?",
    "What happened to the Second Fiend assigned to the Qingcheng attack?",
    "Who is the unidentified person directing Aehyang, and what are they planning?",
    "What is the true nature and purpose of the Lord of Heaven, and what became of the Western Heaven Demon Lord?"
  ],
  "safe_through": 384,
  "temporary_decisions": [
    "Render 열화신룡 as Blazing Flame Divine Dragon, distinct from Huashan Divine Dragon; use Mimi and Mimi-chan for 미미 and 미미쨩, and Third Fiend and Three Fiends for 삼괴.",
    "Render 진인 as Perfected One, 도우 as Fellow Daoist, 신니 as Venerable Nun, 환영진 as illusion formation, and 이동진 as Moving Formation; use Archmage and War Mage for 대마법사 and 워 메이지.",
    "Render 독룡각 as Poison Dragon Pavilion, 가주 대행 as Acting Family Head, 화룡갑 as Fire Dragon Armor, and 공안무력부 as Public Security Armed Forces Department.",
    "Render 사기 as death energy, 의념 as conveyed thoughts, 데스나이트 as Death Knight, 골골 as Bones, and 아크 리치 as Arch Lich.",
    "Render 대교 as Senior Colonel, 동지 as Comrade, 견마지로 as utmost loyalty, 옥체 as august self, and preserve the gukbap wordplay; retain Lord Fuck and peninsula bangzi for the chapter's insults."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 이정룡    | **Lee Jungryong** |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 사형     | **Senior Brother**                           |
| 선배     | **Senior**                                   |
| 칭호               | **Title**                      |
| 헌터      | **Hunter**            |
| 레이드     | **raid**              |
| 팀장      | **Team Leader**       |
| 마법사     | **mage**              |
| 대격변     | **Great Cataclysm**   |
| 대사      | **Master** for a senior Buddhist monk                           |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 웨이펑후 | **Wei Fenghu** | Minister of National Defense under China's Central Military Commission. |
| 주신 | **God of Drinking** | Wipeng's drinking epithet. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 시벌좌 | **Lord Fuck** | Crude online nickname created from Taekyung's accidental broadcast profanity. |
| 개봉 | **Kaifeng** | City where the preliminary competition will be held. |
| 존슨 | **Johnson** | Co-host of the American talk show that replays Taekyung's viral interview. |
| 미국 | **United States** | Country associated with the talk show and CNM. |
| 영국 | **United Kingdom** | Country associated with BCC. |
| 중국 | **China** | Country from which Team Leader Choi’s video originates. |
| 주석 | **Chairman** | Political title used for Xiao Yang. |
| 국방부 | **Ministry of National Defense** | Government ministry referenced in Taekyung's comparison about the steady passage of time. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 시비 | 진태경 | household_servant_to_visiting_young_hero | Young Hero Jin | formal-polite | The maid summons Taekyung to meet the Family Head. |
| 이정룡 | 진태경 | senior S-rank Hunter to younger Hunter and adversary | Young man | polished, teasing, and veiled-threatening | Uses a genial tone and indirect threats while trying to make Taekyung release the captives. |
| 진태경 | 이정룡 | younger Hunter to senior S-rank Hunter and adversary | you | polite but mocking and defiant | Taekyung answers Lee's soft threats with the wolf-and-tiger metaphor and refuses to yield. |
| 마법사 | 이정룡 | Ares Guild mage subordinate to Vice Guild Master | Vice Guild Master | formal-deferential | Lee's five direct A-rank mages greet him and receive instructions for concealing the battle. |
| 웨이펑후 | 진태경 | senior_military_official_to_ally | Mr. Jin | formal-polite | Wei Fenghu addresses Jin while inviting him to walk to the operations headquarters. |
| 진태경 | 웨이펑후 | Foreign Hunter to senior military official | General, Commander, or Supreme Leader | Polite but flustered | Jin jokingly cycles through grand titles while trying to interrupt Wei's emotional request. |

## Listed compact profiles

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 384
- **Aliases:** Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, and a Supreme Peak master who has manifested Force.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother; Jeok Cheongang is his Master; Cheongpung is his trusted companion and only true martial rival; his mother and sister Hayeon are among those he protects.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 384
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Lee Jungryong.md

# Lee Jungryong (이정룡)

- **Safe through:** Chapter 305
- **Aliases:** None
- **Role:** Vice Guild Master of Ares Guild; one of Korea's two S-rank Hunters; effective wielder of Ares Guild's authority in place of its Guild Master; Supreme Peak-level martial artist; gave Park Jihoon his initial orders and is Jihoon's master; visited the Peace Guild's hospital after Taekyung demanded an apology, brought compensation, and demanded the captives after negotiations.
- **Personality:** Outwardly genial, calm, and humorous; calculating, manipulative, coercive, and ruthless when challenged
- **Voice:** Smooth, good-natured, and indirect, using teasing conversation and veiled threats before becoming openly furious
- **Relationships:** Master of Park Jihoon and Go Jun (Team Leader Seok), whom he personally selected and trained; longtime Great Cataclysm acquaintance of Park Tae Seop; adversary of Jin Taekyung; knew Team Leader Choi from childhood; has an antagonistic history with Kim Hwajong, who saved his life at the collapse of Mapo Bridge eighteen years earlier; was visibly shaken by learning that Choi is Cheon Taemin's maternal grandson; regards Cheon Taemin as an older brother despite no blood relation and has long held him in respect and fear; operates as Ares Guild's senior authority beneath its Guild Master

### Wei Fenghu.md

# Wei Fenghu (웨이펑후)

- **Safe through:** Chapter 384
- **Aliases:** None
- **Role:** Wei Fenghu is the Minister of National Defense under China's Central Military Commission and a four-star general.
- **Personality:** Courteous, reserved, and authoritative.
- **Voice:** Formal and measured, addressing Jin as Mr. Jin.
- **Relationships:** Wei Fenghu is Lei Fei’s maternal uncle who raised him as his own son, and he has asked Jin Taekyung to bring Lei Fei back if he is found.

## Korean source

```text
＃385화



「안 그래, 반도의 빵즈?」

“뭐래, 대륙 짱개 새끼가.”

그 순간, 무거운 적막이 내려앉았다.

매직 존슨과 같은 외국인들은 통역 마법을 사용하면서도 빵즈와 짱깨가 정확히 무슨 의미인지 알아듣지 못해 어리둥절했고, 최 팀장은 작게 혀를 찼으며 한 사람의 얼굴은 돌처럼 딱딱하게 굳었다.

「뭐?」

“뭐, 인마.”

「다시 한번 지껄여 봐라, 빵즈.」

“응. 짱깨.”

「이런 개…….」

“좋아. 정리하자. 나는 개. 너는 짱깨.”

「……!」

놈의 얼굴이 와락 일그러지는 것이 보인다. 자리를 박차고 벌떡 일어나려는 놈을, 옆자리에 앉아 있던 여인이 손을 들어 제지했다.

「그만.」

청량음료처럼 깨끗한 분위기를 지닌 20대 초반의 미녀. 그녀의 입술 사이로 침착한 목소리가 이어졌다.

「부탁이니 적당히 해 줬으면 좋겠는데. 두 사람 모두.」

적당히라…….

잠시 여자를 바라보던 나는 어깨를 으쓱해 보였다.

“뭐, 원하신다면.”

뜻밖의 대답이었는지 그녀의 눈썹이 살짝 휘었다.

「언뜻 듣기로는 만만치 않은 성격이라던데, 생각보다 순순하게 받아들이네?」

“받아들여야죠. 다른 사람도 아니고 당신 부탁인데.”

「미인계에 걸려들었구나? 아, 이래서 예쁘면 피곤하다니까.」

능청스럽게 긴 머리를 쓸어올리는 그녀를 보자 피식 웃음이 나왔다.

“너, 지금 웃었니?”

「생각했던 것보다 재미있는 분 같네요. 파이 첸 씨는.」

파이 첸. 그녀의 이름이다.

대학교 표지 모델 같은 저 용모와 분위기에 속으면 안 된다. 결혼만 하지 않았을 뿐, 쉰 살을 훌쩍 넘긴 장년의 나이니까.

동시에 내게는 까마득한 대선배이자, 대격변의 영웅 중 한 사람이기도 했다.

「처음부터 알고 있었다 이거지. 흠, 요즘 애들은 나 모를 줄 알았는데.」

틀린 말은 아니다. 확실히 파이 첸은 다른 S급 헌터들에 비해 미디어에 노출되는 빈도가 매우 낮았다.

수면 아래에서는 신분을 세탁한 뒤 새로운 삶을 살고 있다는 소식도 심심찮게 들려올 정도였다.

하지만 나는 아주 어릴 때부터 그녀를 알고 있었다.

“저희 어머니가 오랜 팬이시거든요. 그 왜, 이십 년 전쯤에 개봉했던 로맨스 영화에 주연으로 나오셨었잖아요.”

「어머? 그게 도대체 언제 적 이야기니. 그래도 그걸 기억해 주는 사람을 만나니까 반갑네.」

“혹시 나중에 사인받으러 가도 됩니까? 어머니께 파이 첸 씨 사인 가져다드리면 좋아하실 것 같아서요.”

「물론이지. 그리고 앞으로는 그냥 첸 씨라고 해. 풀 네임은 너무 딱딱해 보이잖아. 더 편하게 누님이라고 불러도 되고.」

“예? 무슨 소리세요. 인터넷 검색해 보니까 첸 씨가 저희 어머니보다 다섯 살 많으시던데.”

「……만만치 않네. 듣던 대로.」

하지만 정말 만만치 않은 놈은 따로 있었다.

「이런 자라 좆 같은……!」

끓어오르는 목소리. 우리의 대화로 잠시 잊혔던 놈이 분노에 가득 찬 눈으로 나를 노려보았다.

「이 약소국 빵즈 놈이 감히 누구를 무시하는 거냐. 내가 어떤 사람인 줄 알고!」

“……와, 대사 존나 구려.”

우리를 번갈아 보던 파이 첸이 흥미로운 눈빛으로 턱을 괴었다.

「그러게. 아까부터 궁금했는데 너, 이 애가 누군지는 알고 이러는 거니?」

내 대답을 듣고 싶어 하는 사람은 파이 첸 뿐만 아니었다.

이제 반쯤 해탈한 표정의 최 팀장을 제외한 모두가 내 입만을 바라보고 있었다.

말싸움에서 진 일곱 살 어린애처럼 씨근덕거리는 놈과 미국의 대마법사 매직 존슨. 그리고 영국에서 온 청년까지. 그들을 따라온 수행원들도 예외는 아니었다.

모두의 시선 속에, 나는 고개를 끄덕였다.

「알긴 알죠. 우헤이싱.」

잦은 미디어 노출로는 S급 헌터 중에서도 1, 2위를 다투는 놈이니 모를 수가 없다.

내 대답에 아까부터 빵즈 운운하며 시비를 걸어온 놈, 우헤이싱이 눈을 부릅떴다.

「내가 누구인지 알면서도 그랬단 말이냐?」

“지나가던 개도 알걸? S급 헌터 중에 웬 인간 말종 새끼가 하나 있다는 것 정도는.”

「뭐, 뭐라고?」

“왜? 네 취미가 관심받기. 특기가 범죄 저지른 다음 언론 플레이 하기인 거 모르는 사람이 어디 있다고.”

「……!」

“그러고 보니까 너 이 새끼, 작년쯤에 사고 치지 않았냐? 나라가 내게 허락한 유일한 마약. 뭐 이 지랄 떨면서 공식 SNS에 레이드 한 사진 올리고 한 달 후에 진짜 마약 한 거 걸렸었잖아. 아마 대마초였나?”

“진태경 씨.”

“최 팀장님, 말리지 마세요.”

“대마초가 아닙니다.”

“예?”

불쑥 끼어든 최 팀장이 침착한 목소리로 태경 위키를 수정해 주었다.

“대마초가 아니라 코카인과 필로폰입니다.”

“아, 그랬구나. 알려 주셔서 감사합니다.”

“뭘요. 기왕 이렇게 된 거, 못 할 말이 뭐가 있겠습니까.”

해탈한 표정 보소.

이제는 모든 것을 내려놓고 우화등선(羽化登仙)을 준비 중인 최 팀장을 뒤로한 나는, 우헤이싱을 향해 활짝 웃으며 말을 이었다.

“크으, 어떻게 그런 복선을 깔 생각을 했냐. 이 새끼 최소 우헤이순원. 보랏빛 레이드.”

「뭐, 뭐라고?」

“생각해 보니까 또 있네. 5년 전에 버닝문인가 뭔가 하는 클럽에서 약 타서 성폭행 저지르다가 걸렸던 거. 그거 어떻게 무죄 받았냐? 중국 법으로 이 정도면 두세 번쯤 사형당했어도 이상하지 않은데.”

「……!」

“공산당 최고위층 아들이라는 소문은 들었는데. 돈이랑 권력으로 빠져나온 거야? 이 똑똑한 새끼 보게 이거.”

「주, 주둥이 닥치지 못해! 이 천민 출신 빵즈가 감히!」

얼굴이 시뻘겋게 달아오른 채 고함을 내지르는 우헤이싱의 모습에, 가만히 이 사태를 지켜보던 한 사람이 입을 열었다.

「시끄럽군.」

오만한 목소리가 물 흐르듯 이어졌다.

「경박스럽고 천박해. 듣자 하니 중국 귀족 집안의 핏줄 같은데, 가문의 어른들에게 예법 교육을 받지 못했나?」

목소리의 주인을 확인한 우헤이싱이 입술을 깨물었다.

「다, 당신은…….」

「당신?」

잘 정돈된 갈색 머리카락 아래, 은은한 초록빛 눈동자가 우헤이싱을 천천히 훑더니 떨어진다.

「윌리엄.」

청년의 부름에 뒤에 서 있던 반백의 장년인이 앞으로 나섰다.

먼지 한 톨 묻어 있지 않은 구두와 칼처럼 예리하게 다려진 정장. 우뚝 선 채 좌중을 둘러본 장년인의 입술 사이로 듣기 좋은 중저음이 흘러나왔다.

「케임브리지 공작, 스트래선 백작, 캐릭퍼거스 남작, 가터 훈장의 기사, 시슬 훈장의 기사이신 왕자 필릭스 알렉산더 루이 전하께 모두 일어나 예를 갖추십시오.」

케임브리지 공작이자 스트래선의 백…… 시벌, 뭔 칭호가 저렇게 길어.

어쨌건 필릭스 뭐시기 왕자가 준엄하게 한마디를 덧붙였다.

「다들 편하게 필릭스 왕자 전하라고 부르게.」

“…….”

“…….”

사람들 표정 좀 봐라. 세상에서 제일 불편해 보인다.

물론 그중에서도 가장 압권인 사람은 앞서 내게 천민 운운했던 우헤이싱이었다.

그도 그럴 게, 막상 신분으로 따지면 영국 왕족을 어떻게 이기겠나.

「그, 그러니까 이게…….」

「아하.」

당황하는 우헤이싱을 바라보던 필릭스 왕자가 이제 알았다는 듯 고개를 끄덕였다.

「그렇군. 말 더듬이인가?」

「마, 말더듬이?」

「아니라면 왜 말을 제대로 하지 못하는 거지? 가문에서 스피치 훈련을 받지 못했나?」

왕자 전하 만세.

굳이 직접 나설 필요도 없었다. 영국 왕위 계승 서열 3위가 주사기로 꽂아 주는 탄산에 십이지장까지 톡톡 튀는 기분이다.

입이 찢어질 듯이 웃고 있던 그때, 필릭스 왕자의 시선이 문득 나를 향했다.

「자네.」

“응? 나 말하는 겁니까?”

내 반문에 필릭스 왕자의 뒤에 서 있던 장년인이 입을 열었다.

「케임브리지 공작, 스트래선 백작, 캐릭퍼거스 남작, 가터 훈장의 기사, 시슬 훈장의 기사이신 왕자 필릭스 알렉산더 루이 전하께서 하문하실 때에는…….」

「그만하게. 윌리엄.」

손을 들어 앵무새의 입을 틀어막은 필릭스 왕자가 자애로운 눈빛으로 나를 응시했다.

「본인이 품위를 버리고 이렇게 직접 나선 것은, 평소 신분 격차를 타파해야 한다는 신념을 갖고 있기 때문이라네.」

“……?”

「천민이면 어떻고, 귀족이면 어떤가. 우리는 그저 신 아래 평등한 사람일 뿐인 것을. 그러니 저자의 말에 너무 상처받지 말게.」

아니, 이게 뭔 개소리야.

순간 할 말을 잃은 내게 최 팀장이 넌지시 속삭였다.

“진태경 씨를 천민이라고 생각하는 것 같습니다.”

“……!”

저 왕자 새끼가 미쳤나.

어이없는 표정으로 필릭스 왕자를 바라보는 내게, 천천히 자리에서 일어난 그가 당연하다는 듯한 얼굴로 손등을 내밀었다.

「자, 어서.」

“……어서라니. 이번에는 또 뭔데.”

비서인지 앵무새인지 모를 장년인이 흐뭇한 미소를 띤 채 입을 열었다.

「손등에 입을 맞춰, 필릭스 알렉산더 루이 전하께서 보여 주신 자애로움에 감사를 표하시면 됩니다.」

“…….”

이거 완전 또라이들 아냐.

‘단체로 타입 캡슐 타고 18세기에서 건너왔나, 이 18새기들이.’

잠시 머리가 띵해진 내 귓가에, 최 팀장이 보낸 메시지 마법이 닿았다.

- 안 됩니다.

나는 전음으로 응답했다.

- 뭐가 안 돼요.

- 어쨌든 안 됩니다. 그냥 웃으면서 넘어가십시오. 필릭스 왕자는 원래 좀 별종으로 유명하잖습니까.

- 지금 쟤 손등 부러트리면 더 유명해지지 않을까?

- 안 됩니다. 절대 안 됩니다!

- 손등 조금. 아니면 손가락 하나만이라도.

- 안 된다고!

메시지 마법에 이 정도의 감정이 담길 수 있다니. 최 팀장도 나름대로 절박한 모양이다.

그래, 영국 왕자니까 어쩔 수 없지. 내가 내심 화를 삭이던 그때였다.

「헤이, 시벌좌.」

이건 또 뭐야. 나는 불쑥 다가온 매직 존슨을 경계 어린 눈빛으로 바라봤다.

혐한, 각종 트러블로 유명한 우헤이싱은 애초에 기대부터 안 했지만, TV에서나 보던 S급 헌터들을 실물로 봤다는 기쁨은 서서히 바닥을 드러내고 있었다.

“……아니 제발. 시벌좌 말고 이름으로 부르세요. 제가 존슨을 좆슨이라고 부르면 좋겠어요?”

「음, 듣고 보니 그렇군. 그럼, 진(Jin)?」

“훨씬 낫네요. 그런데 왜요?”

「별건 아니고. 혹시 왕자의 손등에 키스할 생각이 없는 거야?」

충분히 별거 같은데.

어이가 없어진 나는 즉각 되물었다.

“당연하죠. 무슨 중세시대도 아니고. 존슨 같으면 하고 싶겠습니까?”

「난 하고 싶지.」

“예?”

순간 뇌리를 스치는 섬광 같은 깨달음.

깜빡 잊고 있었다. 매직 존슨은 미국의 국민 영웅이자 국민 게이라는 사실을.

타임지가 선정한 ‘세계에서 가장 영향력 있는 성소수자 1위’가 나를 향해 진지한 얼굴로 제안한다.

「그래서 말인데, 내가 진을 대신해서 왕자에게 감사를 표하고 싶어.」

“…….”

이걸 이렇게 포장해 버리네. 하지만 매직 존슨과는 달리 필릭스 왕자는 슬그머니 손등을 회수했다.

「신 아래 우리는 평등한 한 사람의 인간일 뿐. 이런 구닥다리 예법은 없어져야 해. 매직 존슨, 그대의 호의는 나중에 받기로 하지.」

“…….”

저게 조금 전까지만 해도 나한테 손등 내밀던 새끼가 할 말인가? 듣고 있던 파이 첸도 어처구니가 없는지 중얼거렸다.

「어머, 되게 뻔뻔하다. 범죄만 안 저질렀지, 우헤이싱 저 녀석보다 한 수 위일지도 몰라.」

“아무리 그래도 우헤이싱보다는 낫죠. 쟤는 법대로면 사형당했어야 할 놈인데.”

「그것도 그래.」

뒤이은 거물들의 등장에 쭈구리가 되어 있던 우헤이싱의 눈동자에서 불똥이 튀었다.

「이, 이, 이 빵즈 새끼가!」

“그놈의 빵즈 타령 그만하지. 애국가도 2절부터는 힘들다. 내가 너 봐주는 것도 마찬가지고.”

「……봐줘? 네놈 따위가 나를?」

도무지 이해가 가지 않는다는 말투에 내가 고개를 끄덕였다.

“어. 방금 확실해졌네.”

나는 우헤이싱이 어느 수준인지 짐작하고 있지만, 놈은 내가 어떤 사람인지 조금도 알아차리지 못했다.

싸움은 상대를 가늠하는 것부터 시작이다. 이 싸움은 시작하기도 전에 끝났다.

“그러니까 괜히 시비 걸지 말고 좋게 말할 때 가라. 각자 할 일이나 열심히 하자고.”

「A급 헌터 주제에 주석 동지의 기대를 받는다고 하늘 높은 줄 모르고 나대……!」

“아하.”

왜 초면부터 지랄을 떠나 싶었는데, 이거 때문이었구만. 너무 뻔하고 유치한 이유라 실소가 흘러나왔다.

“거 참. 이걸 귀엽다고 하기에는 나이를 너무 처먹었고.”

「……!」

“어떡하냐? 주석님의 기대와 주목을 한몸에 받고 싶은데, 웬 한국 놈한테 밀려서.”

「너…….」

속마음을 들켰다는 걸 깨달은 우헤이싱의 얼굴이 수치심과 분노로 달아올랐다.

어느새 모두의 이목이 쏠린 상황. 자신을 향한 사람들의 한심한 시선을 놈도 뼈저리게 느끼고 있을 것이다.

그리고 저런 부류의 놈들은 지금 같은 상황이 오면…….

‘꼭, 선을 넘기 마련이지.’

내 예상은 정확히 들어맞았다.

스윽.

검파를 향해 아주 미세하게 미끄러지는 녀석의 손끝.

대범한 샤오 양 주석은 신뢰의 증거로 이 자리의 누구에게도 무장 해제를 부탁하지 않았지만, 그의 배려는 우헤이싱에게 독이 될 것이다.

‘뽑아. 망설이지 말고.’

내가 아무리 막 나가는 것 같아도 최소한의 경우는 따진다.

지금까지는 주석의 요청으로 중국을 돕기 위해 왔으니 참았던 것뿐, 놈이 무기라도 뽑아 들면 적당한 선에서 조질 명분을 얻을 수 있다.

‘그래, 더. 더.’

마치 내게 조종이라도 당하는 것처럼, 우헤이싱의 손길이 검파를 잡아채려던 바로 그때.

저벅. 저벅.

조용하던 지하 벙커의 문밖, 복도에 울려 퍼지는 여러 명의 발걸음 소리.

우헤이싱의 손이 멈추고 굳게 닫혀 있던 문이 열린 것은, 거의 동시에 벌어진 일이었다.

그리고 국방부장 웨이펑후와 함께 등장한 한 사람을 발견한 순간, 내 뇌리에서 우헤이싱의 존재를 깨끗하게 잊혔다.

“내가 너무 늦었군. 많이들 기다렸나?”

붓으로 그린 듯한 굵은 이목구비와 옷으로도 숨길 수 없는 단단한 체구.

이제 고작 40대 초반인 중년인의 모습을 하고 있지만, 가죽 안에 숨은 것은 늙은 호랑이요, 교활한 뱀이다.

‘이정룡.’

나와 눈이 마주친 이정룡의 입가에, 진한 웃음이 맺혔다.
```

## Final English reading copy

```markdown
# Chapter 385

“Isn’t that right, you peninsula bangzi?”[^1]

“What the hell are you talking about, you mainland chink bastard?”

A heavy silence descended.

Foreigners like Magic Johnson were using translation magic, but they were still bewildered because they didn’t understand exactly what *bangzi* and *chink* meant. Team Leader Choi clicked his tongue softly, while one man’s face hardened like stone.

“What?”

“What, you bastard?”

“Say that again, you bangzi.”

“Sure. Chink.”

“You fucking—”

“Good. Let’s clear this up. I’m a dog. You’re a chink.”

“……!”

I watched his face twist violently. Just as he was about to shove back his chair and leap to his feet, the woman sitting beside him raised a hand to stop him.

“Enough.”

She was a beautiful woman in her early twenties, with an atmosphere as clean and refreshing as a soft drink. Her calm voice continued from between her lips.

“I’d appreciate it if you both kept it to a reasonable level.”

*A reasonable level…*

I studied her for a moment before shrugging.

“Well, if you ask.”

Perhaps my unexpected answer had caught her off guard, because one of her eyebrows curved slightly.

“I heard you weren’t an easygoing person, but you accept that rather readily.”

“I have to. It’s your request, after all.”

“So you’ve fallen for the beauty trap? Ah, this is why being beautiful is such a burden.”

She casually swept back her long hair, and I let out a quiet laugh.

“Did you just laugh?”

“You’re more interesting than I expected, Ms. Faye Chen.”

Faye Chen. That was her name.

I couldn’t let myself be fooled by her appearance and atmosphere, which made her look like a university brochure model. She wasn’t married, but she was well over fifty.

At the same time, she was a far older Senior than me—and one of the heroes of the Great Cataclysm.

“So you knew from the start. Hm. I thought young people these days wouldn’t know who I was.”

She wasn’t wrong. Compared to the other S-rank Hunters, Faye Chen had appeared in the media remarkably infrequently.

Behind the scenes, there were even frequent rumors that she had assumed a new identity and started a new life.

But I had known about her since I was very young.

“My mother’s been a fan of yours for years. You starred in that romance movie that came out about twenty years ago, didn’t you?”

“Oh, my. That was ages ago. Still, it’s nice to meet someone who remembers it.”

“Would it be all right if I got your autograph sometime? I think my mother would be happy if I brought her one from you.”

“Of course. And from now on, just call me Chen. Your full name sounds too formal. You can even call me big sister if you want to be more comfortable.”

“What? What are you talking about? I looked you up online. You’re five years older than my mother.”

“……You really aren’t easygoing. Just as I heard.”

But there was someone else who truly wasn’t easygoing.

“You fucking lowlife—!”

The voice boiled over. The man who had briefly been forgotten in our conversation glared at me with rage in his eyes.

“How dare a bangzi from such a weak country look down on me? Do you even know who I am?”

“……Wow. That line is fucking awful.”

Faye Chen rested her chin on her hand as she looked between us with interest.

“Indeed. I’ve been wondering for a while—do you even know who this young man is?”

Faye Chen wasn’t the only person who wanted to hear my answer.

Everyone except Team Leader Choi, who now wore an expression halfway to enlightenment, was staring at my mouth.

The man huffing and puffing like a seven-year-old child who had lost an argument, Magic Johnson, the Archmage from the United States, and even the young man from the United Kingdom. Their attendants were no exception.

Under everyone’s gaze, I nodded.

“I know. Wu Heixing.”

When it came to frequent media appearances, he vied for first or second place even among S-rank Hunters, so there was no way I wouldn’t know him.

At my answer, the man who had been picking a fight with me by throwing around the word *bangzi*—Wu Heixing—opened his eyes wide.

“You knew who I was and still behaved that way?”

“Even a stray dog would know. There’s a human piece of shit among the S-rank Hunters.”

“What, what did you say?”

“Why? You don’t know that your hobby is getting attention and your specialty is committing crimes and then manipulating the media?”

“……!”

“Come to think of it, didn’t you cause an incident around last year? *The only drug my country allows me*—you posted a raid photo on your official social media while acting like that, then got caught using actual drugs a month later. Marijuana, wasn’t it?”

“Mr. Jin Taekyung.”

“Don’t stop me, Team Leader Choi.”

“It wasn’t marijuana.”

“What?”

Team Leader Choi abruptly cut in and calmly corrected the Taekyung Wiki.

“It was cocaine and methamphetamine.”

“Oh, I see. Thank you for letting me know.”

“Think nothing of it. Now that things have gone this far, what is there left that I can’t say?”

*Look at that enlightened expression.*

Leaving Team Leader Choi behind as he prepared to abandon all worldly concerns and ascend to immortality, I flashed Wu Heixing a broad smile and continued.

“Damn, how did you think of laying down foreshadowing like that? This bastard is at least Wu Heishunwon. *Purple Raid.*”

“What, what did you say?”

“Come to think of it, there’s something else. Five years ago, you got caught drugging someone and sexually assaulting them at some club called Burning Moon or whatever. How did you get acquitted? Under Chinese law, it wouldn’t have been strange if you’d been executed two or three times over.”

“……!”

“I heard a rumor that you’re the son of one of the Communist Party’s highest-ranking officials. Did you buy your way out with money and power? Look at this clever bastard.”

“Shut your fucking mouth! How dare a bangzi from the lowest class speak to me like that!”

Wu Heixing’s face turned bright red as he shouted. Someone who had been silently watching the situation finally spoke.

“You’re noisy.”

An arrogant voice flowed as smoothly as water.

“You’re frivolous and vulgar. I hear you are descended from one of China’s noble families. Did the elders of your family fail to teach you proper etiquette?”

Wu Heixing bit his lip when he recognized the owner of the voice.

“Y-You’re……”

“*You’re?*”

Beneath his neatly arranged brown hair, a pair of subtly green eyes slowly swept over Wu Heixing before moving away.

“William.”

At the young man’s summons, the middle-aged man with half-gray hair standing behind him stepped forward.

His shoes were spotless, and his suit had been pressed as sharply as a blade. Standing tall and surveying the room, the middle-aged man spoke in a pleasant, low-pitched voice.

“Everyone, rise and show proper respect to His Highness Prince Felix Alexander Louis, Duke of Cambridge, Earl of Strathearn, Baron Carrickfergus, Knight of the Order of the Garter, and Knight of the Order of the Thistle.”

*Duke of Cambridge, Earl of Strathearn… Fuck, why does he have so many titles?*

In any case, Prince Felix added a solemn remark.

“Everyone may simply call me His Highness Prince Felix.”

“……”

“……”

Look at everyone’s faces. They looked more uncomfortable than anyone else in the world.

Of course, the most impressive expression of all belonged to Wu Heixing, who had just called me a lowborn bastard.

It made sense. When it came to social standing, how could he possibly beat British royalty?

“So, this is……”

“Ah.”

Prince Felix looked at the flustered Wu Heixing and nodded as though he had finally understood.

“I see. Are you a stutterer?”

“A-a stutterer?”

“If not, why can’t you speak properly? Did your family fail to provide you with speech training?”

*Long live His Highness the Prince.*

I didn’t even need to step in myself. It felt as though the third person in line to the British throne had injected carbonated water directly into my veins, making it fizz all the way to my duodenum.

Just as I was grinning so widely that my mouth nearly split open, Prince Felix’s gaze suddenly turned toward me.

“You there.”

“Hm? Are you talking to me?”

At my question, the middle-aged man standing behind Prince Felix opened his mouth.

“When His Highness Prince Felix Alexander Louis, Duke of Cambridge, Earl of Strathearn, Baron Carrickfergus, Knight of the Order of the Garter, and Knight of the Order of the Thistle, addresses you—”

“Enough, William.”

Prince Felix raised a hand and stopped the parrot mid-sentence, then looked at me with a benevolent gaze.

“I have personally set aside my dignity and intervened because I believe in overcoming the differences between social classes.”

“……?”

“What does it matter whether someone is lowborn or noble? We are all merely equal human beings beneath God. So do not take that man’s words too much to heart.”

*What the fuck is this supposed to mean?*

I lost my ability to speak for a moment. Team Leader Choi quietly whispered to me.

“I believe he thinks you are lowborn, Mr. Jin.”

“……!”

*Is that prince bastard insane?*

As I stared at Prince Felix with an incredulous expression, he slowly rose from his seat and extended the back of his hand toward me with an expression that suggested this was only natural.

“Come now.”

“Come now? What is it this time?”

The middle-aged man who might have been a secretary or a parrot smiled with satisfaction and opened his mouth.

“Kiss the back of his hand and express your gratitude for the benevolence His Highness Prince Felix Alexander Louis has shown you.”

“……”

*Are these people completely insane?*

*Did this group of eighteenth-century bastards take a time capsule from the past and come here?*

My head throbbed for a moment. Then a message spell from Team Leader Choi reached my ear.

—No.

I answered through Sound Transmission.

—What do you mean, no?

—Whatever it is, no. Just smile and let it pass. Prince Felix is famous for being an eccentric.

—If I break the back of his hand right now, won’t he become even more famous?

—No. Absolutely not!

—Just the back of his hand. Or maybe only one finger.

—I said no!

I hadn’t known that a message spell could convey this much emotion. Team Leader Choi must have been desperate in his own way.

*Fine. He’s a British prince. I can’t do anything about that.*

I was trying to swallow my anger when—

“Hey, Lord Fuck.”

*What now?*

I looked warily at Magic Johnson, who had approached me out of nowhere.

I had never expected much from Wu Heixing, who was famous for his anti-Korean sentiment and all kinds of trouble. But the joy of seeing S-rank Hunters I had only watched on television in person was gradually running out.

“……No, please. Don’t call me Lord Fuck. Use my name. Would you like it if I called you Dickson instead of Johnson?”

“Hmm. Now that you put it that way, I see your point. Then, Jin?”

“That’s much better. But why?”

“It’s nothing special. I was just wondering—are you really not planning to kiss the prince’s hand?”

“That sounds pretty special to me.”

I was dumbfounded and immediately asked back.

“Of course not. What is this, the Middle Ages? Would you want to do it if you were me, Johnson?”

“I would.”

“What?”

A flash of enlightenment shot through my mind.

I had completely forgotten. Magic Johnson was an American national hero—and a national gay icon.

*Time* magazine’s choice for “the world’s most influential LGBT person” was making a serious suggestion to me.

“So, I was thinking that I’d like to express my gratitude to the prince on your behalf, Jin.”

“……”

*He really knows how to package something.*

But unlike Magic Johnson, Prince Felix quietly withdrew the back of his hand.

“We are all equal human beings beneath God. Such outdated etiquette should disappear. Magic Johnson, I shall accept your kind offer at another time.”

“……”

*Was that really something for the same bastard who had just held out his hand to me to say?*

Faye Chen, who had been listening, muttered as though she found it absurd.

“My, he’s shameless. He may be one step above Wu Heixing, even if he hasn’t actually committed any crimes.”

“He’s still better than Wu Heixing. That guy should have been executed under the law.”

“That’s true.”

The arrival of one heavyweight after another had reduced Wu Heixing to a cowering nobody, but sparks flew from his eyes.

“Y-you, you fucking bangzi!”

“Stop going on about bangzi already. Even the national anthem gets tiring by the second verse. The same goes for me going easy on you.”

“……Giving me consideration? You?”

He sounded as though he genuinely couldn’t understand me, so I nodded.

“Yeah. I just became sure.”

I had a rough idea of what level Wu Heixing was at, but he had no idea who I was.

A fight began with gauging one’s opponent. This fight had ended before it had even begun.

“So stop picking a fight with me and leave while I’m asking nicely. Let’s each focus on doing our jobs.”

“You’re getting carried away because you’re an A-rank Hunter favored by Chairman Comrade, acting as if you don’t know how high the sky is—!”

“Ah.”

So that was why he had started this bullshit with me from the moment we met.

The reason was so predictable and childish that a quiet laugh escaped me.

“Come on. You’re way too fucking old for me to call this cute.”

“……!”

“What are you going to do? You want all of the Chairman’s expectations and attention focused on you, but some Korean guy has pushed you aside.”

“You……”

The moment Wu Heixing realized that I had seen through his true feelings, his face flushed with shame and fury.

Everyone’s attention had gathered on us by then. He must have felt the pathetic looks everyone was giving him down to his bones.

And people like him, when placed in a situation like this…

*Always cross the line.*

My prediction was exactly right.

His fingertips slid almost imperceptibly toward the hilt of his sword.

Broad-minded Chairman Shao Yang had not asked anyone present to disarm as a sign of trust, but that consideration would become poison to Wu Heixing.

*Draw it. Don’t hesitate.*

No matter how reckless I might seem, I still observed a minimum standard of propriety.

Until now, I had only held back because I had come to help China at the Chairman’s request. If Wu Heixing drew a weapon, I would have an excuse to rough him up without going too far.

*That’s right. More. Keep going.*

As though he were being controlled by me, Wu Heixing’s hand reached for the sword hilt.

And just as his fingers were about to seize it—

Step. Step.

The sound of several people’s footsteps echoed through the corridor outside the quiet underground bunker.

Wu Heixing’s hand stopped, and the tightly closed door opened at almost the exact same moment.

The moment I saw the person who entered alongside Minister of National Defense Wei Fenghu, Wu Heixing’s existence vanished completely from my mind.

“I’m late. Have you all been waiting long?”

He had thick, sharply defined features that looked as though they had been drawn with a brush, and a solid build that even his clothes couldn’t conceal.

He looked like a middle-aged man barely into his forties, but what hid beneath that skin was an old tiger and a sly snake.

*Lee Jungryong.*

When Lee Jungryong’s eyes met mine, a deep smile spread across his lips.

[^1]: *Bangzi* is a derogatory Chinese term for Koreans; “peninsula” refers to Korea.
```

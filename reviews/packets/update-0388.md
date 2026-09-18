<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0388.txt",
      "sha256": "42101357608853dbee08db91bbea4eaef6f2203d32d447a350ac565693e47e69",
      "bytes": 16073
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "bced235d77986f785d1c1fe113aff551133567e5e9172e4fcf7c7046ae42bcfe",
      "bytes": 3949
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "e624c1a27f5f8a896bce426e1f41773adca3f1f660fa708733b95c585296ec64",
      "bytes": 134201
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "58fb9d7f6829eb42c63d6f7986702b9289a0607a99da5d6bfb93de4d37d2c57b",
      "bytes": 1168
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "53fa99d36161f3f8630adc48537826ba0b3789789787dbe6461983dcc6cc6ab2",
      "bytes": 622
    },
    {
      "path": "characters/Lee Jungryong.md",
      "sha256": "29baafda00c5d6b104833260f021a00bf08e31cd184b2e2e7fd5d79199eb6afc",
      "bytes": 1396
    },
    {
      "path": "characters/Lei Fei.md",
      "sha256": "4d7c15e14c6381e89bfddf3c4cafed407b6145b1f8da4fd26f0a7d805e8902e7",
      "bytes": 535
    },
    {
      "path": "characters/Wei Fenghu.md",
      "sha256": "ed04811136a6368ed9996ca2d8846ab583dcc625004b4379ba15e7cee96b7650",
      "bytes": 555
    },
    {
      "path": "characters/Wu Heixing.md",
      "sha256": "a559d4c8914a9a27403ab545eeb9c37e9f1fa8a4a18471f3787a708a2c8e008f",
      "bytes": 664
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "910858e22a288b16059d6a09230b7ec36e6936e0207f52683f37b5ae6226f0ca",
      "bytes": 110359
    }
  ],
  "estimated_tokens": 12272
}
-->

# Durable State Update — Chapter 388

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 388. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 388. Profile updates may replace only one
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
  "chapter": 388,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 388,
    "continuity_sources": [388],
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
    "Jin Taekyung has crossed the wall into true mastery, while Choi Minwoo has become substantially stronger and more refined.",
    "The Arch Lich's three incomplete Liches were destroyed at Chengdu International Airport, and their testimony identified the Arch Lich as responsible for the undead army's actions.",
    "Wei Fenghu is China's Minister of National Defense under the Central Military Commission, a four-star general, and the current Chairman's right-hand man; Lei Fei remains unconfirmed dead or alive after disappearing with his department's Hunters.",
    "Sichuan Province remains in a wartime emergency involving magical communications interference, flying-monster attacks, and a Monster Wave that has caused at least hundreds of thousands of casualties; the dead may have been raised as undead.",
    "The temporary operations headquarters is at Mount Qingcheng, where international S-rank Hunters are gathered, including Faye Chen, Magic Johnson, and Prince Felix Alexander Louis.",
    "Shao Yang is Chairman of the People's Republic of China, Chairman of the Chinese Communist Party's Central Military Commission, and General Secretary; he retains authority over China's crisis response while asking Hunters to prioritize human lives.",
    "Faye Chen is an older S-rank Hunter and Great Cataclysm hero with a former film career, a low media profile, and a playful but composed manner toward Jin.",
    "Wu Heixing is an S-rank Hunter hostile toward Jin who secretly uses Sound Transmission and martial arts, including an internal-energy cultivation technique and fist-and-foot martial arts.",
    "Prince Felix Alexander Louis is a British royal third in line to the throne who patronizes Jin as lowborn while claiming that all people are equal beneath God.",
    "Lee Jungryong is the de facto head of the Ares Guild and one of the world's three strongest S-rank Hunters; he has recognized Jin's breakthrough and is visibly unsettled by it.",
    "Jin possesses Wu Heixing's acquired Top-Grade Potion after defeating him, while Team Leader Choi has urgently asked Jin to return by text."
  ],
  "continuity_sources": [
    387,
    386
  ],
  "open_questions": [
    "Who is the Arch Lich, and what will happen after Jin Taekyung destroys its three servants?",
    "What happened to Lei Fei and the Hunters who disappeared with him?",
    "What happened to the Second Fiend assigned to the Qingcheng attack?",
    "Who is the unidentified person directing Aehyang, and what are they planning?",
    "Why did Team Leader Choi urgently ask Jin Taekyung to return?"
  ],
  "safe_through": 387,
  "temporary_decisions": [
    "Render 열화신룡 as Blazing Flame Divine Dragon, distinct from Huashan Divine Dragon; use Mimi and Mimi-chan for 미미 and 미미쨩, and Third Fiend and Three Fiends for 삼괴.",
    "Render 진인 as Perfected One, 도우 as Fellow Daoist, 신니 as Venerable Nun, 환영진 as illusion formation, and 이동진 as Moving Formation; use Archmage and War Mage for 대마법사 and 워 메이지.",
    "Render 독룡각 as Poison Dragon Pavilion, 가주 대행 as Acting Family Head, 화룡갑 as Fire Dragon Armor, and 공안무력부 as Public Security Armed Forces Department.",
    "Render 사기 as death energy, 의념 as conveyed thoughts, 데스나이트 as Death Knight, 골골 as Bones, 아크 리치 as Arch Lich, 최상급 포션 as Top-Grade Potion, and 상급 포션 as high-grade potion.",
    "Render 시벌좌 as Lord Fuck, 반도의 빵즈 as peninsula bangzi, 짱깨 as chink, 주석 동지 as Chairman Comrade, and 전하 as His Highness; preserve Jin's vulgar historical and cultural jokes, and use General Liao, Crown Prince Party, and Shanghai Gang for this chapter."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 이정룡    | **Lee Jungryong** |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 운기조식   | **circulate one's qi**                           | Usually better as a verb than a proper-name technique |
| 상태               | **Status**                     |
| 퀘스트              | **Quest**                      |
| 보상               | **Reward**                     |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 길드      | **Guild**             |
| 팀장      | **Team Leader**       |
| 대격변     | **Great Cataclysm**   |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 레이페이 | **Lei Fei** | Concealed Chinese S-rank Hunter and head of the Public Security Armed Forces Department in Sichuan Province. |
| 웨이펑후 | **Wei Fenghu** | Minister of National Defense under China's Central Military Commission. |
| 우헤이싱 | **Wu Heixing** | Chinese S-rank Hunter who provokes Jin and nearly draws his sword. |
| 아레스 | **Ares Guild** | The leading Guild in Korea; formerly employed Team Leader Choi and Song Song. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 열화신공 | **Fire Gate Divine Technique** | Secret internal cultivation technique of the Fire Gate Clan, preserved through one-person succession without leakage. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 존슨 | **Johnson** | Co-host of the American talk show that replays Taekyung's viral interview. |
| 중국 | **China** | Country from which Team Leader Choi’s video originates. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 주석 | **Chairman** | Political title used for Xiao Yang. |
| 국방부 | **Ministry of National Defense** | Government ministry referenced in Taekyung's comparison about the steady passage of time. |
| 중화 | **Zhonghua** | Patriotic term used in Shao Shen’s rallying speech. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 관리 | 진태경 | official_to_young_martial_artist | Young Master | formal-polite | The official addresses Taekyung as 공자 while explaining the consequences of Prince Shangshan's displeasure. |
| 이정룡 | 진태경 | senior S-rank Hunter to younger Hunter and adversary | Young man | polished, teasing, and veiled-threatening | Uses a genial tone and indirect threats while trying to make Taekyung release the captives. |
| 진태경 | 이정룡 | younger Hunter to senior S-rank Hunter and adversary | you | polite but mocking and defiant | Taekyung answers Lee's soft threats with the wolf-and-tiger metaphor and refuses to yield. |
| 웨이펑후 | 진태경 | senior_military_official_to_ally | Mr. Jin | formal-polite | Wei Fenghu addresses Jin while inviting him to walk to the operations headquarters. |
| 진태경 | 웨이펑후 | Foreign Hunter to senior military official | General, Commander, or Supreme Leader | Polite but flustered | Jin jokingly cycles through grand titles while trying to interrupt Wei's emotional request. |
| 우헤이싱 | 진태경 | hostile S-rank Hunter to foreign Hunter and provocation target | peninsula bangzi | insulting and confrontational | Wu repeatedly addresses Jin with anti-Korean slurs. |
| 우헤이싱 | 이정룡 | younger S-rank Hunter to senior Ares Guild authority | Mr. Lee | formal and deferential | Wu addresses Lee respectfully despite his usual hostility toward Koreans. |
| 웨이펑후 | 이정룡 | senior military official to senior foreign S-rank Hunter | Mr. Lee | formal and concerned | Wei asks Lee whether something is wrong. |
| 필릭스 | 이정룡 | British prince to senior S-rank Hunter | Jungryong Lee | formal through a translation device | Felix permits Lee to omit His Highness and gives his own preferred form of address. |

## Listed compact profiles

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 386
- **Aliases:** Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, and a Supreme Peak master who has manifested Force and crossed the wall into true mastery.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother; Jeok Cheongang is his Master; Cheongpung is his trusted companion and only true martial rival; his mother and sister Hayeon are among those he protects.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 386
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Lee Jungryong.md

# Lee Jungryong (이정룡)

- **Safe through:** Chapter 387
- **Aliases:** None
- **Role:** Vice Guild Master of Ares Guild; one of Korea's two S-rank Hunters; effective wielder of Ares Guild's authority in place of its Guild Master; Supreme Peak-level martial artist; gave Park Jihoon his initial orders and is Jihoon's master; visited the Peace Guild's hospital after Taekyung demanded an apology, brought compensation, and demanded the captives after negotiations.
- **Personality:** Outwardly genial, calm, and humorous; calculating, manipulative, coercive, and ruthless when challenged
- **Voice:** Smooth, good-natured, and indirect, using teasing conversation and veiled threats before becoming openly furious
- **Relationships:** Master of Park Jihoon and Go Jun (Team Leader Seok), whom he personally selected and trained; longtime Great Cataclysm acquaintance of Park Tae Seop; adversary of Jin Taekyung; knew Team Leader Choi from childhood; has an antagonistic history with Kim Hwajong, who saved his life at the collapse of Mapo Bridge eighteen years earlier; was visibly shaken by learning that Choi is Cheon Taemin's maternal grandson; regards Cheon Taemin as an older brother despite no blood relation and has long held him in respect and fear; operates as Ares Guild's senior authority beneath its Guild Master

### Lei Fei.md

# Lei Fei (레이페이)

- **Safe through:** Chapter 383
- **Aliases:** None
- **Role:** One of China's concealed S-rank Hunters and head of the Public Security Armed Forces Department stationed in Sichuan Province, currently missing with his unit after the first Monster Wave.
- **Personality:** No personality traits are established.
- **Voice:** No voice traits are established.
- **Relationships:** Wei Fenghu is his maternal uncle and raised him as his own son.

### Wei Fenghu.md

# Wei Fenghu (웨이펑후)

- **Safe through:** Chapter 386
- **Aliases:** None
- **Role:** Wei Fenghu is the Minister of National Defense under China's Central Military Commission and a four-star general.
- **Personality:** Courteous, reserved, and authoritative.
- **Voice:** Formal and measured, addressing Jin as Mr. Jin.
- **Relationships:** Wei Fenghu is Lei Fei’s maternal uncle who raised him as his own son, and he has asked Jin Taekyung to bring Lei Fei back if he is found.

### Wu Heixing.md

# Wu Heixing (우헤이싱)

- **Safe through:** Chapter 387
- **Aliases:** None
- **Role:** Wu Heixing is a Chinese S-rank Hunter known for frequent media exposure and scandal who secretly practices martial arts, including an internal-energy cultivation technique and fist-and-foot martial arts.
- **Personality:** Arrogant, status-conscious, abusive, and quick to anger when humiliated.
- **Voice:** Loud, insulting, entitled, and dependent on national and political status.
- **Relationships:** He is openly hostile toward Jin Taekyung and resents Jin receiving Chairman Shao Yang's attention.

## Korean source

```text
＃388화



“야, 야.”

툭, 툭툭.

옆구리를 건드리는 누군가의 발끝. 간신히 눈을 뜬 우헤이싱의 시야에, 자신을 내려다보는 커다란 형체가 어른거렸다.

「흐으…….」

“나 급한 일이 생겨서 이만 가 봐야 하거든? 혹시 누구 오거나 그러면 알아서 잘 둘러대라.”

「흐으, 흐으으…….」

“포션 부어 줬으니까 엄살 그만 피우고, 인마. 계속 그러면 매직 존슨 불러서 진짜 신음 흘리게 하는 수가 있어. 그럼 간다!”

파팟!

듣는 것만으로도 엉덩이가 욱신거리는 한마디를 남긴 채, 순식간에 멀어져 가는 한 사람의 인기척.

대 자로 뻗어 있던 우헤이싱이 끓어오르는 음성을 내뱉은 것은 그로부터 십여 분이 흐른 뒤였다.

「진태경……!」

부러진 뼈와 살은 상급 포션의 효능으로 회복되었지만, 뼛속 깊이 각인된 고통과 금이 간 자존심까지 치유할 수는 없었다.

‘도대체 어떻게?’

믿을 수 없었다. 제아무리 흥분한 상태였다고는 해도 S급 헌터인 자신이 이렇게까지 철저하게 농락당하다니.

진태경에게 무공을 간파당했다는 것도 충격이지만, 스스로가 지니고 있는 힘에 대단한 자부심을 가진 그로서는 패배에 대한 충격이 더 컸다.

‘내가, 다른 사람도 아닌 이 내가?’

우헤이싱은 태어남과 동시에 헌터의 운명을 타고났다.

그는 유아기 시절 막대한 금액을 들인 마나 적응도 검사를 통해 잠재력을 인정받았고, 중국 공산당 최고위층인 집안은 온갖 지원을 아끼지 않았다.

부패로 축적한 막대한 재산과 권력. 최고의 환경과 지원 아래 성장한 우헤이싱은 스무 살이 되던 해에 A급 헌터로 각성했고, 십 년이 흐른 뒤에는 S급 헌터가 되는 기염을 토했다.

그런데…….

‘그런데 어째서. 내가 저런 소국의 빵즈 놈에게!’

캄캄한 밤하늘을 노려보는 우헤이싱의 눈동자에 기광이 번뜩였다.

그의 눈빛에 서린 것은 분노인 동시에 질투였으며 진태경이 보여 준 힘에 대한 일말의 두려움이었다.

그리고 이러한 감정들은 우헤이싱이 지난 십수 년 동안 지긋지긋하게 느껴 온 것이기도 했다.

이제는 찾을 수 없는 한 사람을 향해, 우헤이싱이 외쳤다.

「네놈의 짓이냐? 죽어서도 날 괴롭히려는 거냐!」

대중과 미디어는 그를 구제 불능 탕아라 욕하는 동시에 중화가 낳은 천재라며 칭송했지만, 우헤이싱을 포함한 극소수의 사람들은 알고 있었다.

진정한 천재는 따로 있음을. 그렇기에 드러내지 않고 감춰 놓았다는 것을.

「대답해라, 레이페이!」

막강한 실력은 물론이고 고결한 심성을 지닌 레이페이는 우헤이싱에게 있어 넘을 수 없는 벽이었다.

처음 그가 실종되었다는 소식을 듣고 얼마나 당황하고 기뻐했던가.

하지만 불과 일주일 만에 또 다른 벽이 나타났다. 진태경이라는 이름으로.

「으아아아아!」

쩌렁쩌렁한 외침에 수풀이 몸을 부르르 떨던 그때였다.

“그 마음, 나도 잘 알지.”

기척도 없이 다가온 누군가의 나직한 목소리에, 우헤이싱은 번개처럼 몸을 일으켜 세웠다.

「누구냐!」

“섭섭하군. 구면이라고 생각했는데.”

저벅.

어둠 속에서 불쑥 걸음을 내디딘 한 사람. 우헤이싱의 눈동자가 크게 뜨였다.

「당신은……?」

희미하게 비치는 달빛 아래, 이정룡이 미소 띤 얼굴로 말을 이었다.

“우리가 긴히 나눌 이야기가 있을 것 같은데. 어찌 생각하나?”

「……!」



* * *



띠링.



- [운기조식]을 완료했습니다!

- [열화신공]의 경지가 미약하게 상승합니다!



기운을 갈무리하고 눈을 떴을 때는 밖이 환하게 밝아 오고 있었다.

마치 이때만을 기다리고 있었다는 듯 스켈레톤 워로드가 냉큼 입을 연다.

- 간악한 인간. 드디어 일어났나?

“안 잤어, 인마.”

- 전투를 앞두고 술을 마시다니. 쯧쯧.

“어차피 술병 날 일 없으니까 조용히 해라.”

술을 많이 마시면 주독(酒毒)이 쌓이는데, 어지간한 내가 고수라면 손쉽게 주독을 몰아낼 수 있다.

강대한 열양지기를 지닌 나는 말할 것도 없지.

‘그러고 보니 엄청나게 마시긴 했지. 파이 첸이 전용기로 실어 온 술을 몽땅 거덜 냈을 정도니까.’

분명히 매직 존슨을 말리러 간 거였는데, 어쩌다가 그렇게 됐는지 나도 잘 모르겠다.

- 그런데 인간. 언제까지 이런 갑갑한 곳에 있을 생각인가?

“안 그래도 갈 생각이야.”

시계를 보니 오전 다섯 시 반. 슬슬 준비해야 할 때다.

임시 숙소로 배정받은 호텔 룸에서 짐을 챙긴 뒤 로비로 내려가자, 커피를 마시고 있는 최 팀장이 보였다.

“어, 팀장님.”

“……나오셨군요.”

슬쩍 보니 눈 밑이 퀭하다. 평소 철저한 자기 관리로 잡티 하나 없던 피부가 까슬까슬해 보인다.

“혹시 안 주무셨어요?”

“진태경 씨 같으면 잠이 오겠습니까?”

“…….”

그건 그래.

어젯밤, 세상에서 가장 다급한 호출 문자를 받고 달려간 내가 목격한 광경은 참혹하기 그지없었다.



‘헤이, 최. 이건 술 게임이잖아. 쿨하게 한 번 하자고. 안 그래?’

‘파이 첸! 도와주십시오, 파이 첸!’

‘으음……. 미안한데 이건 술 게임인걸. 왕의 명령은 절대적이다. 이게 룰 아냐?’

‘아무리 그래도 뽀뽀라니! 저는 술 게임 자체도 처음이란 말입니다! 룰도 제대로 설명 안 해 주셨잖아요!’

‘아. 몰라, 몰라. 2번은 3번의 볼에 입 맞출 것. 이게 내 명령이야.’

‘최. 가만히 있어. 난 네게 속박 마법을 걸고 싶지 않아.’

‘이건 말도 안…… 진태경 씨! 여깁니다, 진태경 씨!’

‘진. 방해하지마. 난 네게 공격 마법을 쓰고 싶지 않아.’



정말이지, 일 분만 늦었어도 대참사가 벌어질 뻔했다.

최 팀장을 구제해 주는 대가로 엄청난 양의 술을 원샷 해야 했지만, 일말의 후회도 없다. 그에 걸맞은 합당한 보상을 약속받았으니.

“혹시 어제 했던 약속, 기억하시죠? 제 정산 비율 조정하기로 한 거.”

“……알고 있습니다. 9대1.”

최 팀장이 싸늘한 눈빛으로 나를 노려보았다.

“어떻게 그런 급한 상황에서 그러실 수가 있습니까? 사람입니까?”

“그럼 지금이라도 찐하게 뽀뽀 한번 하시든가. 마침 저기 오시네, 2번님.”

번호는 2번이지만 게이력은 세계 제일이지.

지금 막 로비에 들어선 거구의 흑인, 매직 존슨을 발견한 최 팀장이 마시고 있던 커피를 뿜었다.

“푸웁! 저 좀, 저 좀 숨겨 주십시오.”

“이미 늦은 것 같은데.”

내 말이 끝나기가 무섭게, 우리를 발견한 매직 존슨이 솥뚜껑만 한 손바닥을 흔들었다.

“헤이, 게이즈!”

보통은 가이즈 아닌가. 잘못 말한 거겠지……?

순간 귀를 의심하는 나와 최 팀장에게 다가온 매직 존슨이 껄껄 웃었다.

「너무 그런 표정 짓지 마. 어제는 내가 너무 흥분해서 아주 약간 장난친 거니까.」

“……진짜 흥분하셨어요?”

「아, 그게 그렇게 되네.」

“말조심해 주세요. 깜짝 놀랐네.”

「하하. 어쨌든 어제는 좀 사정이 있었어.」

“……뭐가 있었다고요?”

「어? 아니, 사정이 그 사정이 아니라.」

“말조심 좀 해 주세요. 진짜 깜짝 놀랐네.”

“제발 두 분 다 그만하시죠. 누가 들을까 봐 겁납니다.”

해탈한 얼굴로 남아 있던 커피를 원샷한 최 팀장이 고개를 돌렸다.

어느새 호텔 정문을 통과한 한 무리의 사람들이 우리를 향해 걸어오고 있었다.

「이제 떠날 시간이오. 선생들.」

그중 선두에 있던 국방부장 웨이펑후의 목소리는 긴장으로 딱딱하게 굳어 있었다.

그의 눈짓에 나이 지긋해 보이는 군 장성 하나가 서류철을 하나씩 나눠 주었다.

“이게 뭡니까?”

「선생들이 배치된 지역과 주둔 병력에 대한 정보요. 물론 저쪽에도 미리 필요한 정보와 연락은 취해 두었소. 지금부터는 지정된 제트기를 타고 이동할 거요.」

아무래도 최첨단 기술이 발달한 현대이다 보니, 이런 것만큼은 편리하다.

잠시 후 웨이펑후의 뒤를 따라 도착한 임시 이륙장에는 삼엄한 경호에 둘러싸인 익숙한 얼굴들이 있었다.

「잘 잤니, 젊은이들?」

「…….」

“늦었군.”

기지개를 쭉 켜며 인사를 건네는 파이 첸. 어제 있었던 일 때문인지 말없이 시선을 내리까는 우헤이싱과 묘한 미소를 짓고 있는 이정룡까지.

인벤토리 안에 고이 넣어 둔 스켈레톤 워로드가 떨떠름한 목소리로 말했다.

- 왠지 모르게 기분 나쁜 인간이로군. 본 사령관은 저자가 썩 마음에 들지 않는다.

“동감이야.”

작게 중얼거린 소리를 들은 파이 첸이 눈썹을 치켜올렸다.

「응? 뭐라고?」

“아닙니다. 그나저나 필릭스 왕자는요?”

「동트기 직전에 떠났어. 왕자가 맡게 된 지역에서 교전 신호가 왔다던데.」

“……그렇군요.”

도착한 지 24시간도 되지 않아 또다시 전투가 벌어지다니.

새삼 전쟁이라는 두 글자에 문득 가슴 한구석이 꾸욱, 하고 조여 온다.

국적도, 자라난 환경도 다르지만 나와 같은 인간이 어딘가에서 무참히 살육당하고 있다고 생각하니 마음이 무거워졌다.

「거기 젊은이.」

“예?”

나를 물끄러미 바라보던 파이 첸이 어깨를 툭 쳤다.

「어깨에 힘 풀어. 무거워서 창이나 제대로 휘두르겠어?」

“…….”

「자책하지도 말고 조급해할 필요도 없어. 모든 죽음에 책임을 지려 하지 말라고.」

책임이라. 잠깐 고민하던 나는 솔직히 대답했다.

“……글쎄요. 그다지 자신은 없네요.”

「뭐, 그런 것치고는 어제 술을 진탕 퍼마시긴 하던데.」

“그건…….”

「알아, 농담이야. 우리 같은 사람들은 그렇게라도 잠시 부담감을 잊는 거지. 당장 내일, 아니 오늘 죽을지도 모르는 목숨이니까.」

밝은 목소리에 어울리지 않는 내용. 대격변이라는 소용돌이를 온몸으로 헤쳐나온 영웅은 고개를 들어 하늘을 바라보았다.

「아, 싸우기 딱 좋은 날씨다.」

그러고는 몸을 돌려 이륙 준비를 끝마친 제트기를 향해 사뿐사뿐 걸음을 옮긴다.

나직한 한마디를 남긴 채.

「모두…… 살아서 보자.」

그녀의 뒷모습이 기체 내부 안으로 사라졌다.

잠시 감회에 찬 눈빛으로 하늘을 올려다보던 매직 존슨이 불쑥 입을 열었다.

「헤이, 최.」

“네?”

「너도 엉덩이에 힘 풀어.」

“…….”

「아니, 어깨에 힘 풀어. 살아서 다시 보자고.」

저거 아무래도 진심이 나온 것 같은데.

최 팀장의 경계 어린 눈빛에 껄껄 웃은 매직 존슨이 파이 첸의 뒤를 이어 기체에 몸을 실었다.

이어 우헤이싱이 도망치듯 발걸음을 옮겼고, 마지막으로 남은 이정룡이 묘한 눈빛으로 나와 최 팀장을 훝었다.

“둘 다 몸조심하게. 이런 곳에서 요절할 수야 없지 않나. 젊은 나이에.”

노인네 말본새 하고는. 정말이지, 의미심장한 한마디다.

얼굴을 굳힌 최 팀장을 대신해, 내가 웃으며 입을 열었다.

“그래야죠. 우린 누구와 다르게 지금 죽어도 호상(好喪)은 아니니까.”

“……!”

“혹시 골로 가시면 부조 넉넉하게 하겠습니다.”

“기대하지.”

짧은 침묵 끝에 한마디를 툭 내뱉은 이정룡이 아레스 길드원들을 이끌고 멀어져 간다. 이제 남은 것은 우리뿐.

있는 힘껏 기지개를 켠 나는 최 팀장의 어깨를 두드렸다.

“가시죠. 팀장님.”

“예. 그래야죠.”

“긴장할 것 없습니다. 엉덩이에 힘 푸세요.”

“…….”

“……농담이었는데. 죄송합니다.”

농담 두 번 하면 사람 죽일 기세다.

슬금슬금 최 팀장의 눈치를 살피며 기체에 오르던 그때였다.

「부대- 차렷!」

등 뒤에서 터져 나온 우렁찬 외침.

국방부장 웨이펑후가 반백의 머리를 흩날리며 우리를 향해 거수경례를 올리고 있었다.

그러자 이륙장을 가득 메운 사람들이 웨이펑후를 따라 경례 자세를 취했다.

자신들의 가족과 친구들을 위해 싸우러 가는 영웅들을 향한 경의.

그들의 경례는 제트기의 문이 닫히고, 까마득한 점이 되어 시야에서 사라질 때까지 끝나지 않았다.

‘거, 참.’

이렇게까지 해 주니 어깨가 무거워질 수밖에.

문득 피로를 느끼며 시트에 몸을 기댄 다음 순간이었다.

치직. 치지직.

- ……답. 응답하라. 여기는…….

갑자기 조종석에서 들려오는 노이즈 낀 무전과 함께 귓속을 파고드는 알림.

띠링.



- 돌발 퀘스트, [다급해진 전황]이 생성되었습니다.

- 당신은 퀘스트를 거절할 수 없습니다. 한시라도 빠르게 도착하여 적들을 물리치십시오!



“…….”

빌어먹을, 내 인생이 이렇지 뭐.

푹 한숨을 내쉰 나는 조종석을 향해 힘차게 외쳤다.

“아저씨, 풀 악셀 땡겨요!”



* * *



「그들은?」

입을 연 것은 팔십 대의 노인이었다. 주름과 검버섯이 가득한 얼굴. 늙은 육신은 소싯적만 못했지만, 그의 눈동자에는 젊었을 적보다 더한 힘이 있었다.

홀로그램 화면으로도 느껴지는 노인의 힘 있는 눈빛에, 마른침을 삼킨 웨이펑후가 대답했다.

「모두 출발했습니다. 주석 동지.」

「전황은 어떤가?」

「마법으로 인한 통신 교란과 결계로 적들의 동태를 쉽게 파악할 수 없습니다만, 최선을 다해 이동을 감지 중입니다.」

「S급 헌터들이 도착한다면…….」

「그들의 힘이라면 충분히 전황을 뒤집을 수 있습니다.」

「속단은 금물이야. 한순간도 방심하지 말게. 수많은 이들의 목숨이 우리의 결정에 달렸네.」

「예. 명심하겠습니다.」

웨이펑후 국방부장과의 짧은 통신이 끝난 후, 샤오 양 중국 주석은 드넓은 회의실에 앉아 생각에 잠겼다.

‘어쩌다 이리되었는지.’

대격변 이후 유례없는 대참사다. 수많은 인력과 자금을 투입했지만 아크 리치를 중심으로 한 몬스터 군단을 막을 수는 없었다.

가급적이면 혼란을 막고 싶었지만…… 더 이상 늦으면 기회는 영영 사라질지도 모른다.

그렇기에 샤오 양은 공산당 내부의 숱한 반대를 무릅쓰고 오늘, 이 자리에 왔다.

「준비되었습니다.」

「……즉시 연결하게.」

비서관의 말에 샤오 양은 감았던 눈을 떴다.

넓은 회의실, 비어 있던 자리 위로 홀로그램으로 이루어진 형체들이 하나둘씩 떠오르기 시작했다.

인종도, 성별도 모두 다른 열넷. 아니 샤오 양을 포함한 열다섯 명의 사람들.

그들 한 사람, 한 사람은 일국의 지도자들이었고 하나의 기구에 속해 있었다.

‘유엔 안전보장이사회(The Security Council).’

늙은 주석은, 무거운 목소리로 긴급회의의 시작을 알렸다.
```

## Final English reading copy

```markdown
# Chapter 388

“Hey. Hey.”

Tap. Tap-tap.

The tip of someone’s foot prodded Wu Heixing in the side. He barely opened his eyes, and a large figure looming over him swam into view.

“Uhhh……”

“I’ve got something urgent to take care of, so I have to get going. If anyone comes by, make up a convincing story for them, will you?”

“Ugh… uuuugh……”

“I poured a potion over you, so quit pretending you’re dying, you bastard. If you keep it up, I might call Magic Johnson and make you produce some real moans. See you!”

Whoosh!

After leaving him with a parting remark that made his butt ache just from hearing it, the person’s presence vanished into the distance in an instant.

It was only ten or so minutes later that Wu Heixing, who had been lying spread-eagled on the ground, finally let out a voice boiling with rage.

“Jin Taekyung……!”

The broken bones and torn flesh had recovered thanks to the high-grade potion, but it couldn’t heal the pain etched deep into his bones or his cracked pride.

*How?*

He couldn’t believe it. No matter how agitated he had been, how could he—a S-rank Hunter—have been so thoroughly toyed with?

The fact that Jin Taekyung had seen through his martial arts was shocking, but Wu Heixing took even greater offense at the defeat itself. He had always been fiercely proud of the power he possessed.

*Me? Me, of all people?*

Wu Heixing had been born with a Hunter’s destiny.

As an infant, he had been recognized for his potential through an extremely expensive mana aptitude test, and his family, part of the highest ranks of the Chinese Communist Party, had spared no expense in supporting him.

Enormous wealth and power accumulated through corruption. Raised in the finest environment with the best possible support, Wu Heixing awakened as an A-rank Hunter at the age of twenty. Ten years later, he achieved the astonishing feat of becoming an S-rank Hunter.

And yet……

*Then why? Why was I defeated by that bastard bangzi from such a tiny country?*

A strange light flashed in Wu Heixing’s eyes as he glared at the pitch-black night sky.

His gaze held anger, jealousy, and even a trace of fear toward the power Jin Taekyung had displayed.

Those were also emotions Wu Heixing had been sickeningly familiar with for more than a decade.

Toward someone who could no longer be found, Wu Heixing shouted.

“Was this your doing? Are you trying to torment me even after you’re dead?!”

The public and media cursed him as an irredeemable delinquent while praising him as a genius born of Zhonghua, but a tiny handful of people, Wu Heixing included, knew the truth.

There was a true genius apart from him. That was why they had kept that person hidden and out of sight.

“Answer me, Lei Fei!”

With not only overwhelming skill but also a noble character, Lei Fei had been an insurmountable wall to Wu Heixing.

How flustered—and delighted—Wu Heixing had been when he first heard that Lei Fei had disappeared.

But within only a week, another wall had appeared.

A wall named Jin Taekyung.

“Gaaaaaaaah!”

It was then that the bushes shuddered at the echoing cry.

“I know that feeling too.”

At the low voice of someone who had approached without making a sound, Wu Heixing sprang upright like lightning.

“Who are you?!”

“That hurts. I thought we knew each other.”

Step.

A man suddenly stepped out of the darkness. Wu Heixing’s eyes widened.

“You’re……?”

Beneath the faint moonlight, Lee Jungryong continued with a smile.

“I believe we have something important to discuss. What do you say?”

“……!”

* * *

Ding.

> **System**
>
> **Circulate Your Qi** completed!
>
> The realm of **Fire Gate Divine Technique** has risen slightly!

By the time I finished gathering my qi and opened my eyes, the world outside was already growing bright.

As though it had been waiting for this exact moment, the Skeleton Warlord immediately opened its mouth.

> “Wicked human. Are you finally awake?”

“I wasn’t asleep, you idiot.”

> “You drank alcohol before a battle. Tsk, tsk.”

“I’m not going to get a hangover, so shut up.”

Drinking too much alcohol caused liquor toxicity to build up, but any decent martial arts master could drive it out with ease.

And with my formidable Scorching Yang Qi, I had even less to worry about.

*Come to think of it, I really did drink a lot. I drank all the alcohol Faye Chen had brought over on her private jet.*

I had definitely gone there to stop Magic Johnson, but I wasn’t entirely sure how things had turned out that way.

> “But human. How long do you intend to remain in this stuffy place?”

“I was planning to leave anyway.”

I checked the time. Five-thirty in the morning. It was about time to get ready.

After packing my things in the hotel room assigned as my temporary lodging, I went down to the lobby and saw Team Leader Choi drinking coffee.

“Oh, Team Leader.”

“……You’ve come out.”

A quick glance revealed dark circles under his eyes. His skin, usually so meticulously cared for that it didn’t have a single blemish, looked rough and dry.

“Did you not sleep?”

“If you were in my position, Mr. Jin, would you have been able to sleep?”

“……”

Fair point.

The sight I had witnessed after racing over in response to the most desperate emergency text in the world the previous night had been nothing short of horrific.

*‘Hey, Choi. It’s just a drinking game. Come on, be cool and do it once. What do you say?’*

*‘Faye Chen! Please help me, Faye Chen!’*

*‘Hmm…… Sorry, but it’s a drinking game. The king’s command is absolute. Isn’t that the rule?’*

*‘Even so, a kiss?! I’ve never even played a drinking game before! You didn’t explain the rules properly!’*

*‘Oh, I don’t know, I don’t know. Number two will kiss number three on the cheek. That’s my command.’*

*‘Choi. Stay still. I don’t want to cast a binding spell on you.’*

*‘This is absurd…… Mr. Jin! Over here, Mr. Jin!’*

*‘Jin. Don’t interfere. I don’t want to cast an offensive spell on you.’*

If I had been even one minute later, a catastrophe would have occurred.

I had been forced to down an enormous amount of alcohol in exchange for rescuing Team Leader Choi, but I didn’t regret it in the slightest. I had been promised fair compensation in return.

“You remember the promise you made yesterday, right? About adjusting my settlement ratio.”

“……I remember. Nine to one.”

Team Leader Choi glared at me coldly.

“How could you do that in such an urgent situation? Are you even human?”

“Then give me a really passionate kiss right now. Number two is coming over, as it happens.”

He might have been number two, but his gayness was second to none in the world.

Team Leader Choi spotted Magic Johnson—a huge Black man who had just entered the lobby—and sprayed coffee all over the place.

“Ptooey! Please, please hide me.”

“I think it’s already too late.”

The moment I finished speaking, Magic Johnson spotted us and waved a hand as big as a cauldron lid.

“Hey, gays!”

Wasn’t it supposed to be *guys*? He must have said it wrong…… right?

Magic Johnson approached us as Team Leader Choi and I stared at him in disbelief, then burst into hearty laughter.

“Don’t look at me like that. I got a little too excited yesterday and played just the tiniest prank.”

“……You were really excited?”

“Ah, that came out wrong.”

“Please watch what you say. You startled me.”

“Haha. Anyway, there were circumstances yesterday.”

“……What kind of circumstances?”

“Huh? No, not *those* circumstances.”

“Please watch your words. You really startled me.”

“Please, both of you, stop. I’m afraid someone will hear you.”

With a look of complete resignation, Team Leader Choi downed the rest of his coffee and turned his head.

A group of people had entered through the hotel’s front doors and was walking toward us.

“It’s time to leave, gentlemen.”

The voice of Wei Fenghu, the Minister of National Defense, who was at the head of the group, was stiff with tension.

At his signal, a military general who looked well into his years handed out folders one by one.

“What are these?”

“Information on the areas where you gentlemen have been assigned and the troops stationed there. Of course, we’ve already provided them with the necessary information and contacted them in advance. From this point on, we will travel by the designated jets.”

I suppose this was one of the conveniences of living in an age where cutting-edge technology had advanced so far.

A short while later, at the temporary airfield we reached by following Wei Fenghu, I saw several familiar faces surrounded by tight security.

“Did you sleep well, young people?”

“……”

“You’re late.”

Faye Chen greeted us while stretching her arms high overhead. Perhaps because of what had happened yesterday, Wu Heixing silently kept his eyes lowered, while Lee Jungryong wore a strange smile.

The Skeleton Warlord, safely stored in my Inventory, spoke in an uncomfortable voice.

> “That human is unpleasant for some reason. This commander does not like him one bit.”

“I agree.”

Faye Chen raised an eyebrow at my quiet mutter.

“Hm? What did you say?”

“Nothing. By the way, where’s Prince Felix?”

“He left just before dawn. Apparently, a battle signal came from the area he was assigned.”

“……I see.”

Another battle, less than twenty-four hours after arriving.

The words *war* suddenly seemed to squeeze a corner of my heart.

Our nationalities and upbringings were different, but knowing that human beings like me were being slaughtered somewhere made my heart heavy.

“Hey, young man.”

“Yes?”

Faye Chen had been staring at me intently. She reached out and gave me a light tap on the shoulder.

“Relax your shoulders. If they’re that heavy, will you even be able to swing your spear properly?”

“……”

“Don’t blame yourself, and don’t be in such a hurry. Don’t try to take responsibility for every death.”

Responsibility.

I thought about it for a moment before answering honestly.

“……I don’t know. I’m not very confident I can do that.”

“Well, you certainly drank yourself senseless yesterday, for someone who feels that way.”

“That was……”

“I know. I’m joking. People like us forget the burden for a little while that way. Our lives might end tomorrow—or even today.”

The content didn’t match her bright voice. The hero who had made her way through the Great Cataclysm with every inch of her body looked up at the sky.

“Ah. Perfect weather for a fight.”

She turned and began walking lightly toward the jet, which had finished preparing for takeoff.

Leaving behind one quiet remark.

“Let’s all…… see each other alive.”

Her back disappeared inside the aircraft.

Magic Johnson gazed up at the sky for a moment with an oddly sentimental look, then suddenly opened his mouth.

“Hey, Choi.”

“Yes?”

“You relax your butt, too.”

“……”

“No, your shoulders. Let’s see each other alive again.”

*That sounded like his true feelings slipping out.*

Magic Johnson laughed heartily at Team Leader Choi’s wary look and boarded the aircraft after Faye Chen.

Wu Heixing followed, walking as though he were trying to escape. Finally, Lee Jungryong, the last one remaining, swept his strange gaze over Team Leader Choi and me.

“Take care of yourselves. We can’t go and die in a place like this, can we? Not at such a young age.”

*What a way for an old man to talk.*

It was an incredibly suggestive remark.

With Team Leader Choi’s face hardening, I smiled and opened my mouth in his place.

“That’s right. Unlike certain people, we’re too young for our deaths to count as a blessing.”

“……!”

“If you do kick the bucket, I’ll make sure to give a generous funeral contribution.”

“I’ll be counting on it.”

After a brief silence, Lee Jungryong tossed out that one remark and led the Ares Guild members away.

Now only Team Leader Choi and I remained.

I stretched as hard as I could, then patted Team Leader Choi on the shoulder.

“Let’s go, Team Leader.”

“Yes. We should.”

“No need to be nervous. Relax your butt.”

“……”

“……That was a joke. I’m sorry.”

*One more joke like that and he looked ready to kill me.*

I was cautiously watching Team Leader Choi’s expression as I boarded the aircraft when it happened.

“Unit—attention!”

A booming shout erupted behind us.

Wei Fenghu stood at attention and saluted us, his half-gray hair fluttering in the wind.

The people filling the airfield followed Wei Fenghu and raised their hands in salute.

It was a gesture of respect for the heroes going to fight for their families and friends.

Their salutes did not end until the jet’s door closed and it disappeared from view as a tiny, distant speck.

*Good grief.*

With this much of a send-off, there was no way my shoulders wouldn’t feel heavy.

I leaned back into my seat, suddenly feeling tired. The next moment—

Crackle. Crrrackle.

“……swer. Respond. This is……”

Along with the static-filled radio transmission suddenly coming from the cockpit, an alert pierced my ears.

Ding.

> **System**
>
> A Sudden Quest, **The Desperate War Situation**, has been generated.
>
> You cannot refuse this Quest. Arrive as quickly as possible and defeat the enemies!

“……”

*Damn it. This is just how my life is.*

I let out a deep sigh, then shouted toward the cockpit.

“Sir, floor it!”

* * *

“Where are they?”

The person who spoke was an old man in his eighties. His face was covered in wrinkles and age spots. His aged body was no longer what it had been in his youth, but his eyes held even greater power than they had back then.

Even through the holographic screen, the old man’s powerful gaze could be felt. Wei Fenghu swallowed hard before answering.

“They have all departed, Chairman Comrade.”

“How is the situation at the front?”

“We cannot easily determine the enemy’s movements because of the communications interference caused by magic and the barriers, but we are doing our best to detect their movement.”

“If the S-rank Hunters arrive……”

“With their strength, they should be more than capable of turning the tide.”

“Don’t jump to conclusions. Do not let your guard down for even a moment. The lives of countless people depend on our decisions.”

“Yes. I will keep that in mind.”

After the brief communication with Wei Fenghu, the Minister of National Defense, Shao Yang, Chairman of China, sat alone in the vast conference room and fell into thought.

*How did things come to this?*

This was an unprecedented catastrophe since the Great Cataclysm. Despite pouring in vast amounts of personnel and money, they had been unable to stop the monster army centered around the Arch Lich.

He had wanted to prevent panic if at all possible, but if they delayed any longer, the opportunity might disappear forever.

That was why Shao Yang had come here today, despite the countless objections within the Communist Party.

“They’re ready.”

“……Connect me immediately.”

At his secretary’s words, Shao Yang opened his eyes.

In the empty seats of the spacious conference room, holographic figures began appearing one after another.

Fourteen people of different races and genders.

No—fifteen, including Shao Yang.

Each of them was the leader of a nation, and they all belonged to a single institution.

*The United Nations Security Council.*

The elderly Chairman announced the start of the emergency meeting in a heavy voice.
```

<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0386.txt",
      "sha256": "4885a393ec1de0b3d19c44efa37157f2d0a4a248f3bcbc1682322f939ee077f2",
      "bytes": 13178
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "24885c132406b9daedfaaaa6e89d61be50202a4d9e7abbe24161274d937f98af",
      "bytes": 3596
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "5c48734164d2fd4e68597373e6e773b1a03c239ab8e07343754ca96554ae3d3e",
      "bytes": 133839
    },
    {
      "path": "characters/Cheon Taemin.md",
      "sha256": "6583efd9a364f08bac5f40d800de749b1eabacc0018e67a23b48115d0c048ee6",
      "bytes": 590
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "8e5cee3183bd79de0518c92ab60079075adafe21d086b44ca32ad0cdffbb152a",
      "bytes": 1129
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "fadf10a58b660fe15611957b257ecd33c76aa2cbb3761a58c3429d58cce24641",
      "bytes": 622
    },
    {
      "path": "characters/Lee Jungryong.md",
      "sha256": "bc35d4a89b71083ca3e679bf9832cc46412a132deb9e57b44577535d871cb21a",
      "bytes": 1396
    },
    {
      "path": "characters/Team Leader Choi.md",
      "sha256": "6fc38ab3039d059eb94f5eeef592dbefed2d2a238be5c7366ca78043631ddf4f",
      "bytes": 1263
    },
    {
      "path": "characters/Wei Fenghu.md",
      "sha256": "1ab7b15739af3174dcc9dcb01fe9cf8cb5abc74afb5031d9f99e8aae8fe84a5c",
      "bytes": 555
    },
    {
      "path": "characters/Wu Heixing.md",
      "sha256": "33dfeef173d6ecde4839edfeea704c844b599d454c94e2bfb81f037c04ed69c5",
      "bytes": 562
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "6ef2f690a1a837f1c76747d969bc2b8a83fe9828b7dfdbd6ff3487786763b7fa",
      "bytes": 108173
    }
  ],
  "estimated_tokens": 10900
}
-->

# Durable State Update — Chapter 386

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 386. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 386. Profile updates may replace only one
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
  "chapter": 386,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 386,
    "continuity_sources": [386],
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
    "Wei Fenghu is China's Minister of National Defense under the Central Military Commission, a four-star general, and the current Chairman's right-hand man; he raised Lei Fei as his own son and asked Jin to bring him back if found.",
    "Sichuan Province remains in a wartime emergency involving magical communications interference, flying-monster attacks, and a Monster Wave that began in Gaoping District of Nanchong City.",
    "China has concealed at least one of its S-rank Hunters, Lei Fei, who disappeared with his department's Hunters when the first Monster Wave began and remains unconfirmed dead or alive.",
    "The temporary operations headquarters is at Mount Qingcheng, where international S-rank Hunters are gathered, including Magic Johnson and Faye Chen.",
    "Shao Yang is Chairman of the People's Republic of China, Chairman of the Chinese Communist Party's Central Military Commission, and General Secretary; he retains authority over China's crisis response while asking Hunters to prioritize human lives.",
    "Faye Chen is an older S-rank Hunter and Great Cataclysm hero with a former film career, a low media profile, and a playful but composed manner toward Jin.",
    "Wu Heixing is an S-rank Hunter whose arrogance and hostility toward Jin have escalated into a public confrontation; he nearly drew his sword before the interruption.",
    "Prince Felix Alexander Louis is a British royal third in line to the throne who patronizes Jin as lowborn while claiming that all people are equal beneath God.",
    "Lee Jungryong has arrived at the underground headquarters with Wei Fenghu, and Jin recognizes him as a dangerous old tiger and sly snake."
  ],
  "continuity_sources": [
    385,
    384
  ],
  "open_questions": [
    "Who is the Arch Lich, and what will happen after Jin Taekyung destroys its three servants?",
    "What happened to Lei Fei and the Hunters who disappeared with him?",
    "What happened to the Second Fiend assigned to the Qingcheng attack?",
    "Who is the unidentified person directing Aehyang, and what are they planning?",
    "What is the true nature and purpose of the Lord of Heaven, and what became of the Western Heaven Demon Lord?"
  ],
  "safe_through": 385,
  "temporary_decisions": [
    "Render 열화신룡 as Blazing Flame Divine Dragon, distinct from Huashan Divine Dragon; use Mimi and Mimi-chan for 미미 and 미미쨩, and Third Fiend and Three Fiends for 삼괴.",
    "Render 진인 as Perfected One, 도우 as Fellow Daoist, 신니 as Venerable Nun, 환영진 as illusion formation, and 이동진 as Moving Formation; use Archmage and War Mage for 대마법사 and 워 메이지.",
    "Render 독룡각 as Poison Dragon Pavilion, 가주 대행 as Acting Family Head, 화룡갑 as Fire Dragon Armor, and 공안무력부 as Public Security Armed Forces Department.",
    "Render 사기 as death energy, 의념 as conveyed thoughts, 데스나이트 as Death Knight, 골골 as Bones, and 아크 리치 as Arch Lich.",
    "Render 시벌좌 as Lord Fuck, 반도의 빵즈 as peninsula bangzi, 짱깨 as chink, 주석 동지 as Chairman Comrade, and 전하 as His Highness; preserve Jin's vulgar historical and cultural jokes."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 최민우    | **Choi Minwoo**   |
| 천태민    | **Cheon Taemin**  |
| 이정룡    | **Lee Jungryong** |
| 무인     | **martial artist**                               | Default term                                          |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 매력               | **Charm**                      |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 길드      | **Guild**             |
| 팀장      | **Team Leader**       |
| 마법사     | **mage**              |
| 대격변     | **Great Cataclysm**   |
| 사천     | **Sichuan**            |
| 청해     | **Qinghai**            |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 웨이펑후 | **Wei Fenghu** | Minister of National Defense under China's Central Military Commission. |
| 우헤이싱 | **Wu Heixing** | Chinese S-rank Hunter who provokes Jin and nearly draws his sword. |
| 평화 | **Peace Guild** | Guild name. |
| 아레스 | **Ares Guild** | The leading Guild in Korea; formerly employed Team Leader Choi and Song Song. |
| 송이 | **Song-i** | Short form used for Song Song; Taekyung's love interest. |
| 태자 | **Crown Prince** | Title of the Emperor's older brother who was reportedly assassinated. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 존슨 | **Johnson** | Co-host of the American talk show that replays Taekyung's viral interview. |
| 미국 | **United States** | Country associated with the talk show and CNM. |
| 영국 | **United Kingdom** | Country associated with BCC. |
| 중국 | **China** | Country from which Team Leader Choi’s video originates. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 주석 | **Chairman** | Political title used for Xiao Yang. |
| 국방부 | **Ministry of National Defense** | Government ministry referenced in Taekyung's comparison about the steady passage of time. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 이정룡 | 진태경 | senior S-rank Hunter to younger Hunter and adversary | Young man | polished, teasing, and veiled-threatening | Uses a genial tone and indirect threats while trying to make Taekyung release the captives. |
| 진태경 | 이정룡 | younger Hunter to senior S-rank Hunter and adversary | you | polite but mocking and defiant | Taekyung answers Lee's soft threats with the wolf-and-tiger metaphor and refuses to yield. |
| 마법사 | 이정룡 | Ares Guild mage subordinate to Vice Guild Master | Vice Guild Master | formal-deferential | Lee's five direct A-rank mages greet him and receive instructions for concealing the battle. |
| 이정룡 | 천태민 | younger_to_older_brother_by_choice | older brother | reverent and familiar; internal | Lee Jungryong uses 형님 in unspoken thoughts and regards Cheon Taemin as an older brother despite having no blood relation. |
| 웨이펑후 | 진태경 | senior_military_official_to_ally | Mr. Jin | formal-polite | Wei Fenghu addresses Jin while inviting him to walk to the operations headquarters. |
| 진태경 | 웨이펑후 | Foreign Hunter to senior military official | General, Commander, or Supreme Leader | Polite but flustered | Jin jokingly cycles through grand titles while trying to interrupt Wei's emotional request. |
| 우헤이싱 | 진태경 | hostile S-rank Hunter to foreign Hunter and provocation target | peninsula bangzi | insulting and confrontational | Wu repeatedly addresses Jin with anti-Korean slurs. |

## Listed compact profiles

### Cheon Taemin.md

# Cheon Taemin (천태민)

- **Safe through:** Chapter 305
- **Aliases:** Slayer
- **Role:** Ares Guild Master; humanity's great hero and the world's greatest Hunter; killed the Demon King and is known as the Slayer; created the first Mana Cultivation Method during the Great Cataclysm.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** Maternal grandfather of Team Leader Choi and father of Soyeong; regarded by Lee Jungryong as an older brother despite their lack of blood relation.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 385
- **Aliases:** Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, and a Supreme Peak master who has manifested Force.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother; Jeok Cheongang is his Master; Cheongpung is his trusted companion and only true martial rival; his mother and sister Hayeon are among those he protects.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 385
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Lee Jungryong.md

# Lee Jungryong (이정룡)

- **Safe through:** Chapter 385
- **Aliases:** None
- **Role:** Vice Guild Master of Ares Guild; one of Korea's two S-rank Hunters; effective wielder of Ares Guild's authority in place of its Guild Master; Supreme Peak-level martial artist; gave Park Jihoon his initial orders and is Jihoon's master; visited the Peace Guild's hospital after Taekyung demanded an apology, brought compensation, and demanded the captives after negotiations.
- **Personality:** Outwardly genial, calm, and humorous; calculating, manipulative, coercive, and ruthless when challenged
- **Voice:** Smooth, good-natured, and indirect, using teasing conversation and veiled threats before becoming openly furious
- **Relationships:** Master of Park Jihoon and Go Jun (Team Leader Seok), whom he personally selected and trained; longtime Great Cataclysm acquaintance of Park Tae Seop; adversary of Jin Taekyung; knew Team Leader Choi from childhood; has an antagonistic history with Kim Hwajong, who saved his life at the collapse of Mapo Bridge eighteen years earlier; was visibly shaken by learning that Choi is Cheon Taemin's maternal grandson; regards Cheon Taemin as an older brother despite no blood relation and has long held him in respect and fear; operates as Ares Guild's senior authority beneath its Guild Master

### Team Leader Choi.md

# Team Leader Choi

- **Safe through:** Chapter 318
- **Aliases:** Choi Minwoo (최민우)
- **Role:** Former Ares Guild team leader and reawakened Hunter publicly classified as C-rank; Guild Master and team leader of the expanding Peace Guild. He manages rookie training and raid assignments. After Jin Taekyung guided his internal energy, he completed the Jin Family's Cultivation Technique, became a martial artist, controlled his scattered mana, nearly doubled his mana reserves, and reached Four Stars after further practice while developing a hidden internal-energy reserve equivalent to one jiazi.
- **Personality:** Calm, observant, practical, and decisive under pressure.
- **Voice:** Polite and measured in ordinary conversation; clipped and commanding during combat.
- **Relationships:** Respects and employs Jin Taekyung, recognizes that Taekyung is far stronger than his public F-rank porter identity suggests, and has repeatedly tried to recruit him into the Peace Guild. He concealed Taekyung's role in defeating the Hobgoblin Great Warrior and continues to treat him as a valuable but closely watched associate. Butler Kim assists Choi with investigations and guild affairs.

### Wei Fenghu.md

# Wei Fenghu (웨이펑후)

- **Safe through:** Chapter 385
- **Aliases:** None
- **Role:** Wei Fenghu is the Minister of National Defense under China's Central Military Commission and a four-star general.
- **Personality:** Courteous, reserved, and authoritative.
- **Voice:** Formal and measured, addressing Jin as Mr. Jin.
- **Relationships:** Wei Fenghu is Lei Fei’s maternal uncle who raised him as his own son, and he has asked Jin Taekyung to bring Lei Fei back if he is found.

### Wu Heixing.md

# Wu Heixing (우헤이싱)

- **Safe through:** Chapter 385
- **Aliases:** None
- **Role:** Wu Heixing is a Chinese S-rank Hunter known for frequent media exposure and a reputation for scandal.
- **Personality:** Arrogant, status-conscious, abusive, and quick to anger when humiliated.
- **Voice:** Loud, insulting, entitled, and dependent on national and political status.
- **Relationships:** He is openly hostile toward Jin Taekyung and resents Jin receiving Chairman Shao Yang's attention.

## Korean source

```text
＃386화



“내가 너무 늦었군. 많이들 기다렸나?”

이정룡은 모여 있는 사람들의 면면을 훑었다. 익숙한 얼굴도, 오늘 처음 보는 이들도 있었다.

대격변 당시 몇 번 마주쳤던 매직 존슨, 파이 첸, 그리고 영국의 애송이 왕자와 중국의 문제아까지.

한 사람, 한 사람과 시선이 마주칠 때마다 지하 벙커에 모인 S급 헌터들이 이정룡을 향해 먼저 인사를 건넸다.

「오랜만이야, 리. 못 본 사이에 더 매력적인 남자가 됐네. 당신을 볼 때마다 고백하고 싶어진다니까.」

“참아 주게, 매직 존슨. 난 그쪽 취향이 아니거든. 여기 있는 파이 첸이라면 모를까.”

이정룡의 천연덕스러운 대꾸에 파이 첸이 긴 머리카락을 쓸어올렸다.

「어머, 이 선생이 나한테 그런 마음이 있는 줄은 몰랐는데. 아쉽네요. 너무 늦게 알아서.」

“아쉬울 게 뭐가 있겠소. 아직 한창때인데.”

「그렇게 말해 주니까 고맙긴 한데, 젊은 친구들이 들으면 비웃어요. 늙은이들끼리 뭐 하는 짓이냐고.」

“정말 그런가?”

이정룡의 시선에 우헤이싱이 다급하게 손을 내저었다.

「아, 아닙니다. 이 선생님. 그럴 리가 있겠습니까.」

“자네 얘기는 많이 들었지. 재능이 뛰어나고, 음. 매사에 솔직한 청년이라고.”

「가, 감사합니다.」

우헤이싱이 황송하다는 듯한 얼굴로 고개를 숙였다.

평소에는 혐한 기질에 한국인을 비하하는 뜻인 빵즈를 입에 달고 사는 그였지만, 감히 이정룡의 앞에서 그런 모습을 보일 만한 담력은 없었다.

우헤이싱의 목덜미에서 식은땀 한 방울이 또르르 굴러떨어졌다.

「이야기를 듣긴 했지만 정말 오실 줄은 몰랐습니다.」

“당연히 와야지. 이웃이 어려우면 돕고 살아야 하는 것 아닌가.”

「이 선생님을 만나 뵙게 되어 영광입니다.」

대격변이 낳은 영웅들인 매직 존슨과 파이 첸조차 이정룡에 비할 수는 없다.

21세기의 예수, 전 세계의 구원자라 불리는 천태민의 의형제이자 바로 그 아레스 길드의 실질적인 수장이니까.

세계에서 손꼽히는 막강한 길드. 그리고 S급 헌터 중에서도 세 손가락 안에 드는 강자. 이정룡.

그와 마주한다면 마땅한 경의를 표해야 한다.

안하무인인 우헤이싱도, 고귀한 혈통을 지닌 왕족도 예외는 아니었다.

“만나서 반갑소. 반갑습니다, 정룡 리.”

“아, 자네가 바로 그 왕자로군.”

「무엄하…….」

손을 들어 비서의 말을 막은 필릭스 왕자가 기품 있게 고개를 살짝 숙였다.

“필릭스. 필릭스라고 부르면 되오. 됩니다.”

통역기를 거친 어색한 한국어와 애매한 말투.

하지만 이것으로 영국 왕위 계승 서열 3위, 필릭스 알렉산더 루이는 다른 이들과 이정룡의 차이를 분명히 했다. 무려 ‘왕자 전하’라는 호칭을 생략하게 해 준 것이다.

물론 이정룡은 신경조차 쓰지 않았다.

‘그래 봤자 애송이들.’

이정룡이 인정하는 것은 매직 존슨과 파이 첸까지다.

성격이야 어쨌건 세간에서는 천재라 불리는 우헤이싱과 필릭스 왕자도 그의 눈에는 이제 막 걷기 시작한 햇병아리에 불과했다.

그리고…… 정작 이정룡의 신경을 거스르는 이들은 따로 있다.

‘평화 길드.’

이정룡의 시선이 한쪽을 향했다. 말없이 서 있는 두 사람을 바라보는 그의 입가에 진한 미소가 맺혔다.

“요즘 들어 자주 보게 되는군. 두 사람 모두 잘 지냈나?”

이정룡이 건넨 인사에, 서로를 바라본 진태경과 최민우가 어깨를 으쓱했다.

“별로.”

“그다지.”

“……?”

뭐지?

이정룡은 자신도 모르게 멈칫했다.

마지막으로 본 것은 불과 한 달도 되지 않은 짧은 시간. 그러나 그를 대하는 두 사람의 태도에는 큰 변화가 있었다.

‘적의(敵意).’

바로 그것이다. 놈들에게서는 예전처럼 뚜렷한 적의와 경계심이 느껴지지 않았다.

담담하기 그지없는 두 사람을 바라보던 이정룡은 곧 그 이유를 깨달을 수 있었다.

‘강해졌다. 전과는 비교할 수 없을 정도로.’

틀림없었다. 도대체 무슨 수로 단기간에 이렇게 성장했는지 궁금해질 만큼, 최민우에게서 느껴지는 기운은 전에 비해 훨씬 더 크고, 정제되어 있었다.

그리고 다른 한 사람, 진태경은.

‘……이건.’

피부와 육감을 통해 느껴졌다. 진태경의 전신에 갈무리된 강대한 기운이. 깊게 가라앉은 놈의 눈동자가.

이것이 의미하는 바는 하나뿐이다.

‘벽을, 넘었다.’

뒤통수를 한 대 얻어맞은 듯한 충격. 이정룡은 동요를 드러내지 않기 위해 안간힘을 써야 했다.

‘도대체 어떻게?’

이전에도 진태경은 분명 강자였다. 어쩌면 전 세계에 존재하는 수많은 A급 헌터들의 머리 위에 선 존재였을 것이다.

단독으로 네임드 몬스터를 둘이나 처치할 정도였으니, 사람들과 언론이 새로운 S급 헌터의 탄생이라며 떠드는 것은 당연했다.

하지만 이정룡은 알고 있었다. 진태경이 아직 ‘벽’을 넘지 못했다는 것을. 녀석의 앞을 가로막은 벽을 넘어 진정한 강자가 되기까지는 아주 오랜 시간이 필요하리라는 사실을.

그런데…….

‘이런 말도 안 되는 일이 벌어지다니.’

놀라움이라는 감정으로 표현할 수 있는 일이 아니다. 자신을 향한 진태경의 덤덤한 눈빛을 마주한 이정룡은, 오랫동안 잊고 있던 감정을 떠올렸다.

불안. 초조.

그건 이정룡이 아레스 길드를 온전히 손에 넣은 후 처음으로 느끼는 불안감이었다.

몇 달 전만 하더라도 그저 우습고 거슬리던 존재. 그런 놈이 자신에게 불안과 초조라는 감정을 일깨워 주었다.

‘이놈…….’

이정룡의 입가에 맺혀 있던 웃음은 씻은 듯이 사라졌다. 굳은 얼굴을 한 그를 웨이펑후가 의아하게 바라봤다.

「이 선생? 무슨 문제라도 있습니까?」

“……별일 아니오.”

「흠. 그럼 이제 회의를 시작해도 되겠습니까?」

말없이 고개를 끄덕이는 이정룡의 시선은 시종일관 한 사람에게 고정되어 있었다.

의자 등받이에 비스듬히 몸을 기댄 청년, 진태경이 혼잣말처럼 중얼거렸다.

“글쎄, 충분히 별일 같아 보이는데.”

“……!”

“뭐, 아니면 말고.”

이정룡은 자신도 모르게 주먹을 힘껏 움켜쥐었다.



* * *



지하 벙커에서 이루어진 회의는 오랫동안 이어졌다.

지난 일주일간 최소 수십 만의 사상자를 발생시킨 몬스터 웨이브다. 그 자체만으로도 이미 엄청난 천재지변이었고, 확실한 전시 상황이었으니 신중에 신중을 기하는 것은 당연했다.

「하여, 오군(五軍)으로 나누어 적들을 압박해 나가는 것이…….」

심각한 얼굴로 말을 이어 나가려는 웨이펑후의 말을 누군가가 가로막았다.

「이보시오. 국방부장 동지.」

「말씀하시오. 랴오 상장.」

정복에 온갖 훈장을 주렁주렁 매단 장년인, 랴오 상장이라 불린 그가 수염을 쓰다듬으며 입을 열었다.

「내 국방부장의 말을 듣자 하니, 너무 답답해서 말이오. 그렇게 지지부진해서야 어느 세월에 저 몬스터 놈들을 처리하겠소?」

이야…….

말투가 보통 띠꺼운 게 아니다. 주석의 오른팔이자 군부 최고위 실권자인 웨이펑후에게 저런 식으로 말을 할 수 있다니.

마치 내 의문을 읽은 것처럼 최 팀장이 메시지 마법을 보냈다.

- 공산당도 각각 파벌이 있습니다. 랴오 상장은 조부 시절부터 공산당 최대 계파인 태자당(太子党)의 성골 출신으로, 샤오 주석과 웨이펑후 국방부장이 속해 있는 상하이방(上海帮)과는 경쟁 관계입니다.

- 태자당이랑 상, 뭐요?

- ……굳이 따지자면 태자당이 1번이고, 상하이방이 2번이라는 소립니다.

- 아.

지금까지 공산당 하면 무조건 일당 체제인 줄 알았는데, 자기네들끼리도 열심히 치고받고 싸우는 모양이다.

- 그런데 그래도 됩니까? 샤오 주석이 손가락으로 딱 가리키면서 저놈은 해로운 놈이다. 한마디 하면 천안문 광장에서 참수당하는 거 아니에요?

- 되니까 하죠.

- ……아니, 뭐. 그렇게 말씀하시니까 할 말이 없네.

- 파벌끼리 합의를 본 겁니다. 대격변 당시 태자당 출신 주석이 하도 실수를 많이 해서 계속 정권을 잡기에는 눈치가 보였던 거죠.

- 아, 핑핑이?

- 예. 핑핑이.

그놈의 대격변이 참 여러 가지를 바꿔 놨구나.

내가 최 팀장으로부터 그런 설명을 듣고 있는 사이, 태자당 성골 유스 출신이라는 랴오 상장은 기똥찬 제안을 내놓았다.

「핵을 씁시다.」

「……?」

「……?」

「샤오 주석에게 정식으로 요청해서, 핵 수십 발을 사천 전역에 날려 버리잔 말입니다. 그럼 깔끔하게 해결될 것 아니오?」

「…….」

「…….」

저런 미친 핵쟁이 새끼를 봤나.

나를 포함한 모두가 어이없는 얼굴로 서로를 바라보았다.

그중에서도 특히 웨이펑후 국방부장의 표정이 압권이다. 그는 권총이 마려운 표정으로 대답했다.

「기각하오.」

「어째서! 지금 상하이방이 아니라고 무시하는 거요!」

「말이 되는 소릴 하시오. 말이 되는 소릴! 그렇게 되면 아직 생존해 있거나 피해를 입지 않은 인민들은! 황폐해지는 국토는 어쩔 거요!」

「대를 위한 소의 희생은 어쩔 수 없소!」

다른 건 모르겠고 그냥 소 대가리 같은데.

조용히 듣고 있던 매직 존슨이 굵은 목소리로 불쑥 입을 열었다.

「핵 공격이 성공했을 때의 피해도 피해지만, 공간 이동 마법으로 핵탄두를 이동시키면 어쩌려고? 예를 들면 북경이라거나.」

「그건 대마법사인 당신이 있으니까…….」

「나? 상대는 보통 리치가 아니야. 만약 아크 리치라는 놈이 나보다 마법이 뛰어나다면, 그땐 정말 돌이킬 수 없는 참사가 일어나. 이미 대격변 초기에도 비슷한 일이 몇 번 있었잖아?」

「그, 그래도…… 이 정도 희생쯤은…….」

「헤이. 머더 퍼커.」

쾅!

깜짝이야. 자리를 박차고 일어난 매직 존슨이 구릿빛 근육을 꿈틀거렸다.

「그만해. 나, 동양인 남자도 좋아하니까. 벌을 내려 줄 수도 있어.」

「……!」

「……!」

지금까지 들어 본 협박 중에 제일 무섭다.

얼굴이 새파랗게 질린 랴오 상장이 구원을 바라는 눈빛으로 주위를 둘러봤지만, 같은 계파에 속해 있는 것으로 짐작되는 관료들은 물론이고 최후의 보루인 우헤이싱도 그의 시선을 외면했다.

‘이게 이렇게 해결되네.’

상대는 미국의 국민 영웅이자 국민 게이.

모두가 매직 존슨이 좋아하는 동양인 남자가 되기 싫어서 안간힘을 쓰는 모양이었다.

물론 랴오 상장이 너무 개소리를 지껄인 것도 크게 한몫했다.

「그만하시오, 두 분 다. 특히 랴오 상장은 턱도 없는 소리 그만하시고.」

짱깨를 진압한 중국인, 웨이펑후의 주도하에 이후 회의는 빠르게 진행되었다.

앞서 나온 의견들을 종합, 설전을 거친 끝에 모두의 동의를 얻어 낸 웨이펑후가 지친 얼굴로 입을 열었다.

「여기 계신 S급 헌터 여섯 분을 여섯 개 방면으로 나누어 배치하겠소. 정식 편제에 따라 방면마다 육, 공군 세 개 사단, 그리고 공안 무력부의 헌터를 파견할 거요.」

중국 세 개 사단에 공안 무력부라.

정확히 그 숫자가 몇이나 될지는 몰라도, 물량 하나만큼은 어마어마할 것이다.

보유한 헌터의 숫자로 따지면 늘 첫째, 둘째를 다투는 중국 아닌가.

‘물론 저쪽도 만만치 않지만.’

피해 사상자 추정치만 수십만 명이다.

아크 리치가 죽은 자들을 언데드로 부활시켰다면…… 그야말로 아득한 숫자의 적들이 우리를 기다리고 있을 것이다.

「이것으로 회의를 끝마치겠소. 여러분들께서는 속히 이동하시오.」

정확한 숫자와 편제를 서면으로 알려 준다는 웨이펑후의 말과 함께, 사람들이 자리에서 일어난 바로 그때였다.

- 잠깐 나 좀 보지.

귓가를 파고드는 누군가의 목소리. 그건 메시지 마법이 아닌, 틀림없는 전음(傳音)이었다.
```

## Final English reading copy

```markdown
# Chapter 386

“I’m late. Have you all been waiting long?”

Lee Jungryong swept his gaze across the gathered people. Some faces were familiar, while others were strangers he was seeing for the first time today.

Magic Johnson and Faye Chen, whom he had encountered several times during the Great Cataclysm. The young British prince. And China’s problem child.

Every time his eyes met someone else’s, the S-rank Hunters gathered in the underground bunker greeted Lee first.

“Long time no see, Lee. You’ve become even more attractive since the last time I saw you. Every time I see you, I feel like confessing my love.”

“Please restrain yourself, Magic Johnson. You’re not my type. Faye Chen here might be, though.”

At Lee’s shameless reply, Faye Chen swept her long hair back.

“Oh my. I had no idea you felt that way about me, Mr. Lee. What a shame. I found out too late.”

“What’s there to regret? You’re still in your prime.”

“Thank you for saying that, but the young people will laugh if they hear you. They’ll ask what the old folks think they’re doing.”

“Is that really how it is?”

Under Lee’s gaze, Wu Heixing hurriedly waved his hands in denial.

“No, no, Mr. Lee. How could that possibly be?”

“I’ve heard a lot about you. You’re exceptionally talented and, hm, a young man who’s honest about everything.”

“Th-thank you.”

Wu Heixing lowered his head, looking deeply humbled by the honor.

He normally had the word *bangzi*—a derogatory term for Koreans—practically glued to his lips, along with his anti-Korean sentiment. But he lacked the nerve to show that side of himself in front of Lee Jungryong.

A bead of cold sweat rolled down the back of Wu Heixing’s neck.

“I’d heard you were coming, but I never expected you to actually show up.”

“Of course I had to come. When a neighbor is in trouble, shouldn’t we help them?”

“It’s an honor to meet you, Mr. Lee.”

Even Magic Johnson and Faye Chen, heroes born during the Great Cataclysm, could not compare to Lee Jungryong.

He was the sworn brother of Cheon Taemin, known as the Jesus of the twenty-first century and the savior of the world. He was also the de facto head of the Ares Guild.

One of the most powerful Guilds in the world. And one of the three strongest people among all the S-rank Hunters.

Lee Jungryong.

Anyone who faced him had to show the proper respect.

Even the overbearing Wu Heixing was no exception. Neither was the prince, despite his noble blood.

“Nice to meet you. A pleasure to meet you, Jungryong Lee.”

“Ah. So you’re that prince.”

“How impudent—”

Prince Felix raised a hand to stop his secretary, then inclined his head with elegant restraint.

“Felix. You may call me Felix. That will do.”

The Korean that came through the translation device was awkward, and his tone was hard to place.

But with those words, Felix Alexander Louis, third in line to the British throne, had made the difference between Lee Jungryong and everyone else perfectly clear.

He had gone so far as to let Lee omit the title *His Highness*.

Of course, Lee Jungryong did not care in the slightest.

*They’re all just brats.*

The only people Lee acknowledged were Magic Johnson and Faye Chen.

No matter their personalities, Wu Heixing and Prince Felix were still called geniuses by the public. But in Lee’s eyes, they were nothing more than chicks that had only just learned to walk.

And the people who truly grated on Lee’s nerves were somewhere else.

*The Peace Guild.*

Lee’s gaze shifted to one side. A deep smile formed at the corners of his mouth as he looked at the two people standing there in silence.

“I seem to be running into you two rather often these days. Have you both been well?”

At Lee’s greeting, Jin Taekyung and Choi Minwoo glanced at each other and shrugged.

“Not really.”

“Not particularly.”

“……?”

What?

Lee Jungryong unconsciously faltered.

It had been less than a month since he had last seen them. Yet something had changed dramatically in the way they treated him.

*Hostility.*

That was it.

The clear hostility and wariness he had sensed from them before were no longer there.

As Lee studied the two people who stood before him with such calm expressions, he soon realized why.

*They’ve grown stronger. So much stronger than before that there’s no comparison.*

There was no doubt about it. Choi Minwoo’s qi was far greater and more refined than before—so much so that Lee found himself wondering how he had managed to grow so much in such a short time.

And the other one, Jin Taekyung—

*……What is this?*

Lee could sense it through his skin and sixth sense: the immense qi contained throughout Jin Taekyung’s body, and the profound stillness in his eyes.

There could only be one meaning.

*He crossed the wall.*

The shock hit Lee like a blow to the back of the head. He had to struggle with all his might to keep his agitation from showing.

*How?*

Jin Taekyung had been a powerful man before, without question. Perhaps he had even stood above the countless A-rank Hunters throughout the world.

He had defeated two Named Monsters on his own. It was only natural that the people and media had been clamoring about the birth of a new S-rank Hunter.

But Lee Jungryong knew that Jin had not yet crossed the wall. He knew that it would take a very long time for the young man to overcome the barrier blocking his path and become a true powerhouse.

And yet—

*How can something this absurd happen?*

This was not something that could be described simply as surprise.

When Lee met Jin Taekyung’s calm gaze, he remembered emotions he had forgotten for a very long time.

Anxiety. Impatience.

It was the first time Lee Jungryong had felt such unease since taking complete control of the Ares Guild.

Only a few months ago, Jin had been nothing more than an amusing and irritating presence. Yet that same man had awakened feelings of anxiety and impatience within him.

*You bastard……*

The smile at the corners of Lee’s mouth vanished as though it had been wiped away. Wei Fenghu looked at his hardened face with puzzlement.

“Mr. Lee? Is something wrong?”

“……It’s nothing.”

“Hmm. Then may we begin the meeting?”

Lee Jungryong nodded without a word, but his gaze remained fixed on one person.

The young man leaning diagonally against the back of his chair, Jin Taekyung, muttered as though speaking to himself.

“Well, it looks like quite a lot is wrong.”

“……!”

“Well, forget it if it’s nothing.”

Without realizing it, Lee Jungryong clenched one fist tight.

* * *

The meeting in the underground bunker continued for a long time.

The Monster Wave had caused at least hundreds of thousands of casualties over the past week. That alone made it an enormous natural disaster and an unmistakable state of war. It was only natural that every decision had to be made with the utmost caution.

“Therefore, we should divide our forces into five armies and gradually pressure the enemy……”

Someone interrupted Wei Fenghu as he continued speaking with a grave expression.

“Minister of National Defense Comrade.”

“Speak, General Liao.”

The middle-aged man called General Liao wore a uniform weighed down with rows of medals. He stroked his beard before opening his mouth.

“After listening to the Minister of National Defense, I found it too stifling to remain silent. At this rate, moving so slowly, when will we ever deal with those monsters?”

*Wow……*

His tone was unbelievably obnoxious.

He was speaking that way to Wei Fenghu, the Chairman’s right-hand man and the highest-ranking man with real power in the military.

As though he had read my thoughts, Team Leader Choi sent me a message spell.

—The Communist Party also has its own factions. General Liao is a pure-blooded member of the Crown Prince Party, the largest faction in the Communist Party since his grandfather’s time. It is a rival faction to the Shanghai Gang, which Chairman Shao and Minister of National Defense Wei Fenghu belong to.

—The Crown Prince Party and Shang…what?

—……If we must rank them, it means the Crown Prince Party is number one and the Shanghai Gang is number two.

—Oh.

Until now, I had assumed that the Communist Party operated under a strictly one-party system. Apparently, they fought among themselves just as enthusiastically.

—But is that really allowed? If Chairman Shao simply pointed at someone and said, “That man is harmful,” wouldn’t they behead him in Tiananmen Square?

—They do it because they’re allowed to.

—……I mean, when you put it that way, I don’t have much to say.

—The factions reached an agreement. During the Great Cataclysm, the Chairman from the Crown Prince Party made so many mistakes that it became awkward for them to keep holding power.

—Ah. Pingping?[^1]

—Yes. Pingping.

[^1]: “Pingping” is a mocking nickname derived from Xi Jinping’s given name.

*That damn Great Cataclysm changed so many things.*

While I was listening to Team Leader Choi’s explanation, General Liao, a pure-blooded product of the Crown Prince Party’s youth ranks, came up with a brilliant proposal.

“Let’s use nuclear weapons.”

“……?”

“……?”

“Let’s formally request it from Chairman Shao and launch dozens of nuclear weapons across Sichuan. Wouldn’t that solve everything nice and cleanly?”

“……”

“……”

*What a fucking nuclear-crazed bastard.*

Everyone, myself included, looked at one another with baffled expressions.

But Wei Fenghu’s expression was the most impressive of all. He looked like he desperately wanted a handgun as he answered.

“Rejected.”

“Why! Are you ignoring me because I’m not part of the Shanghai Gang?”

“Say something that makes sense. Something that makes sense! What about the people who are still alive or haven’t suffered any damage? What are we going to do about the land that will be reduced to a wasteland?”

“Sacrifices for the greater good are unavoidable!”

*I don’t know about the rest, but he sure seems like a total oxhead.*

Magic Johnson, who had been listening quietly, suddenly spoke in his deep voice.

“The damage from a successful nuclear attack would be bad enough, but what are you going to do if someone uses spatial-transference magic to move the warheads? To Beijing, for example.”

“That’s why we have an Archmage like you……”

“Me? Our opponent isn’t an ordinary Lich. If that Arch Lich is more skilled at magic than I am, it could cause a truly irreversible catastrophe. Similar things already happened several times during the early days of the Great Cataclysm, remember?”

“B-but even so…… A sacrifice of this scale……”

“Hey. Motherfucker.”

Bang!

*That startled me.*

Magic Johnson shot to his feet, the muscles of his bronze-colored body rippling.

“Stop it. I like East Asian men, too. I might have to punish you.”

“……!”

“……!”

*That’s the scariest threat I’ve ever heard.*

General Liao’s face turned deathly pale as he looked around for help. But the officials who appeared to belong to his faction avoided his gaze, as did Wu Heixing, his last possible line of defense.

*So this is how it gets resolved.*

His opponent was an American national hero—and a national gay icon.

Everyone seemed desperate not to become one of the East Asian men Magic Johnson liked.

Of course, General Liao’s relentless stream of bullshit had played a major role as well.

“Enough, both of you. Especially you, General Liao. Stop saying things that are completely absurd.”

Under the direction of Wei Fenghu, the Chinese man who had just shut down that chink, the meeting proceeded quickly.

After gathering the opinions that had been raised and settling the arguments, Wei Fenghu secured everyone’s agreement before speaking with a weary expression.

“We will divide the six S-rank Hunters here and deploy them in six directions. According to the official military structure, each direction will receive three Army and Air Force divisions, along with Hunters from the Public Security Armed Forces Department.”

Three Chinese divisions and the Public Security Armed Forces Department.

I didn’t know the exact number of people that meant, but when it came to sheer manpower, it would be enormous.

When it came to the number of Hunters they possessed, wasn’t China always fighting for first or second place?

*Of course, the other side isn’t exactly harmless, either.*

The estimated casualties alone numbered in the hundreds of thousands.

If the Arch Lich had resurrected the dead as undead……

Then an almost unimaginable number of enemies would be waiting for us.

“This concludes the meeting. Please move out as soon as possible.”

Just as everyone rose from their seats after Wei Fenghu said that the exact troop numbers and force organization would be provided in writing, it happened.

“I need a word with you.”

A voice pierced my ear.

It wasn’t a message spell. It was unmistakably Sound Transmission.
```

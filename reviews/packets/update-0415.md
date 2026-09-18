<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0415.txt",
      "sha256": "b288a0234ca45185d08f072c29131de2f58dd3accd920342cb4c703d0180ed23",
      "bytes": 13749
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "e14d998020d891557d539f30ccc96614ed0a3964e8097e9cf7293c2bd54046bb",
      "bytes": 1349
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "b8ee6d0b7bc11219702fb9a07a6525c55958b14ea5143c5a8c7d08eb04fb7753",
      "bytes": 138638
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "d25651ad7d59b769c82be1179074af62476b2ad62d536fbc1be0aa49d9178487",
      "bytes": 533
    },
    {
      "path": "characters/Felix.md",
      "sha256": "4c186e84555fe96bd39d33746f0b5806d11927d2f137d475cfddbea95686ea9d",
      "bytes": 464
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "4a0ac29f110e7264239af21564ea202b46d184b4b2a1fc01be27d8b3a0ad5ddb",
      "bytes": 1270
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "521d3798cdfb66723fb926e0f017b9205abb960e06d5883d4d20955a5125438b",
      "bytes": 622
    },
    {
      "path": "characters/Lee Jungryong.md",
      "sha256": "059f0f28fb37783d60163ccc41aa9360c8575e8c7f8443870c7cf17c70d48192",
      "bytes": 1163
    },
    {
      "path": "characters/Lei Fei.md",
      "sha256": "dd0a6e88cbbb95e532f7cc643f9ccfb416d2b41dc653206362d1a5de882217b8",
      "bytes": 893
    },
    {
      "path": "characters/Wu Heixing.md",
      "sha256": "c7697c8008a2ef417cbb044d00e944a2ac0ec7861fbde46b0da6665d34603062",
      "bytes": 762
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "5a73ca8d3fdadd7171e89c27e1399db49542c6c4e792f05c72636392518914da",
      "bytes": 127082
    }
  ],
  "estimated_tokens": 10947
}
-->

# Durable State Update — Chapter 415

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 415. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 415. Profile updates may replace only one
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
  "chapter": 415,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 415,
    "continuity_sources": [415],
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
    "Jin Taekyung, Lee Jungryong, Wu Heixing, and roughly five hundred suicide-squad members are twenty kilometers from the Arch Lich.",
    "The Arch Lich has an estimated fifty thousand monsters in reserve.",
    "Team Leader Choi believes the Arch Lich withheld its reserve because the front-line battle required fewer forces than expected.",
    "Go Jun has improved in strength and patience and can suppress his killing intent under provocation.",
    "Prince Felix, Faye Chen, and Magic Johnson have arrived through a dangerous teleport.",
    "Ten thousand Hunters from the Western and Eastern Fronts are advancing to reinforce the coalition.",
    "Team Leader Choi has declared that the coalition will win, and Jin Taekyung shares that belief."
  ],
  "continuity_sources": [
    414,
    413
  ],
  "open_questions": [
    "Can the combined forces break through the Arch Lich's fifty-thousand-monster reserve and reach it?",
    "What further defenses await the coalition beyond the Arch Lich's reserve army?"
  ],
  "safe_through": 414,
  "temporary_decisions": [
    "Render 아크 리치 as Arch Lich.",
    "Render 결사대 as suicide squad.",
    "Render 일인군단 as one-person army.",
    "Render 영웅의 혼 as Hero's Soul.",
    "Render 장유유서 as Respect your elders."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 이정룡    | **Lee Jungryong** |
| 돌파     | **break through** / **breakthrough**             | Realm advancement                                     |
| 살기     | **killing intent**                               |                                                       |
| 검기     | **Sword Energy**                                 | When functioning as projected weapon qi               |
| 상태               | **Status**                     |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 길드      | **Guild**             |
| 팀장      | **Team Leader**       |
| 마법사     | **mage**              |
| 도사      | **Daoist**                                                      |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 필릭스 | **Felix** | British prince and S-rank Hunter. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 레이페이 | **Lei Fei** | Concealed Chinese S-rank Hunter and head of the Public Security Armed Forces Department in Sichuan Province. |
| 우헤이싱 | **Wu Heixing** | Chinese S-rank Hunter who provokes Jin and nearly draws his sword. |
| 평화 | **Peace Guild** | Guild name. |
| 아레스 | **Ares Guild** | The leading Guild in Korea; formerly employed Team Leader Choi and Song Song. |
| 송이 | **Song-i** | Short form used for Song Song; Taekyung's love interest. |
| 주신 | **God of Drinking** | Wipeng's drinking epithet. |
| 개방 | **Beggars' Sect** | Murim organization counted among the Nine Sects and One Gang. |
| 허공섭물 | **Seizing an Object Through Empty Space** | Technique Jeok Cheongang uses to lift Jang Taebo remotely. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 라이칸스로프 | **Lycanthrope** | B-rank Gate monster species. |
| 트롤 | **Troll** | Monster species with extraordinary regenerative ability. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 화주 | **strong liquor** | Liquor stored and consumed by the dark-path swordsmen. |
| 일각 | **fifteen minutes** | Quarter of a shichen; used for the remaining completion time. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 준이 | **Jun** | Family nickname used in the form Jun's dad. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 메이지 | **Mage** | Skeleton subtype mentioned alongside Soldiers and Warriors. |
| 존슨 | **Johnson** | Co-host of the American talk show that replays Taekyung's viral interview. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 개방도 | **Beggars' Sect disciple** | Member of the Beggars' Sect. |
| 신력 | **divine strength** | Superhuman strength attributed to Taekyung. |
| 가고일 | **Gargoyle** | Flying monster species accompanying the Wyverns. |
| 데스나이트 | **Death Knight** | Undead commander type serving under the Black Knight. |
| 홍위방 | **Red Guard Gang** | Private army of elite Hunters founded and raised by Wu Heixing's family. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 이정룡 | 진태경 | senior S-rank Hunter to younger Hunter and adversary | Young man | polished, teasing, and veiled-threatening | Uses a genial tone and indirect threats while trying to make Taekyung release the captives. |
| 진태경 | 이정룡 | younger Hunter to senior S-rank Hunter and adversary | you | polite but mocking and defiant | Taekyung answers Lee's soft threats with the wolf-and-tiger metaphor and refuses to yield. |
| 마법사 | 이정룡 | Ares Guild mage subordinate to Vice Guild Master | Vice Guild Master | formal-deferential | Lee's five direct A-rank mages greet him and receive instructions for concealing the battle. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 우헤이싱 | 진태경 | hostile S-rank Hunter to foreign Hunter and provocation target | peninsula bangzi | insulting and confrontational | Wu repeatedly addresses Jin with anti-Korean slurs. |
| 우헤이싱 | 이정룡 | younger S-rank Hunter to senior Ares Guild authority | Mr. Lee | formal and deferential | Wu addresses Lee respectfully despite his usual hostility toward Koreans. |
| 필릭스 | 이정룡 | British prince to senior S-rank Hunter | Jungryong Lee | formal through a translation device | Felix permits Lee to omit His Highness and gives his own preferred form of address. |
| 진태경 | 필릭스 | Korean S-rank Hunter addressing a British prince | His Highness | mock-formal and sarcastic | Felix demands formal address, and Jin complies by calling him His Highness while continuing to mock him. |
| 데스나이트 | 인간 | enemy combatants | human | contemptuous and commanding | Used in the Death Knight's warnings to Jin. |
| 데스나이트 | 로드 | subordinate to commanding lord | Lord | fearful and deferential | The Death Knight calls to the Death Knight Lord after Jin overwhelms the army. |
| 진태경 | 레이페이 | former ally and fellow Hunter | Lei Fei | blunt and solemn | Jin addresses Lei Fei by name before telling him to rest. |
| 레이페이 | 진태경 | former ally and fellow Hunter | you | familiar and respectful | Lei Fei uses 자네 and 하게 while asking Jin to help him fulfill his final mission. |
| 진태경 | 우헤이싱 | adversarial S-rank Hunters | you idiot | insulting-casual | Mocks Wu's cowardice and orders him to stop complaining. |
| 이정룡 | 우헤이싱 | senior S-rank Hunter to younger allied S-rank Hunter | Mr. Wu | polished and formally coaxing | Lee publicly draws Wu into agreement with the suicide-squad plan. |
| 진태경 | 결사대 | commander_to_subordinates | you bastards | blunt and commanding | Jin orders the suicide squad to exploit the opening and wipe out the surrounding monsters. |
| 필릭스 | 진태경 | British prince and S-rank Hunter to allied Korean S-rank Hunter | Jin | lofty and aristocratic | Felix addresses Jin while discussing royal duty and their teleport. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 413
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who has sworn never to kill again.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Felix.md

# Felix (필릭스)

- **Safe through:** Chapter 414
- **Aliases:** Prince Felix
- **Role:** British prince and S-rank Hunter who joins the reinforcement force against the Arch Lich.
- **Personality:** Haughty, self-important, and conscious of royal duty.
- **Voice:** Formal, lofty, and aristocratic.
- **Relationships:** Travels with Faye Chen and Magic Johnson and is allied with Jin Taekyung.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 414
- **Aliases:** Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, and a Supreme Peak master who has manifested Force and crossed the wall into true mastery.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and student, his mother and sister Hayeon are among those he protects, and the Skeleton Warlord is his captive undead commander.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 414
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Lee Jungryong.md

# Lee Jungryong (이정룡)

- **Safe through:** Chapter 414
- **Aliases:** None
- **Role:** Vice Guild Master of Ares Guild, one of Korea's two S-rank Hunters, and a Supreme Peak-level martial artist who directs Ares Guild operations.
- **Personality:** Outwardly genial, calm, and humorous; calculating, manipulative, coercive, and ruthless when challenged
- **Voice:** Smooth, good-natured, and indirect, using teasing conversation and veiled threats before becoming openly furious
- **Relationships:** Master of Park Jihoon and Go Jun (Team Leader Seok), whom he personally selected and trained; longtime Great Cataclysm acquaintance of Park Tae Seop; adversary of Jin Taekyung; knew Team Leader Choi from childhood; has an antagonistic history with Kim Hwajong, who saved his life at the collapse of Mapo Bridge eighteen years earlier; was visibly shaken by learning that Choi is Cheon Taemin's maternal grandson; regards Cheon Taemin as an older brother despite no blood relation and has long held him in respect and fear; operates as Ares Guild's senior authority beneath its Guild Master

### Lei Fei.md

# Lei Fei (레이페이)

- **Safe through:** Chapter 413
- **Aliases:** None
- **Role:** Lei Fei is a concealed Chinese S-rank Hunter and former head of the Public Security Armed Forces Department in Sichuan Province who recovered his human identity after becoming a level-120 undead Death Knight Lord and died fulfilling his final mission.
- **Personality:** Lei Fei's recovered memories show him as dutiful, honorable, family-oriented, and willing to serve as an unseen guardian.
- **Voice:** His human voice is formal and earnest, becoming warm and playful with family.
- **Relationships:** Wei Fenghu is his maternal uncle who raised him as a son; Lei Fei married an unnamed flower-shop owner and had a daughter, trained alongside Wu Heixing, and was corrupted by the Arch Lich before Jin Taekyung restored his identity.

### Wu Heixing.md

# Wu Heixing (우헤이싱)

- **Safe through:** Chapter 414
- **Aliases:** None
- **Role:** Wu Heixing is a Chinese S-rank Hunter known for frequent media exposure and scandal who secretly practices martial arts, including an internal-energy cultivation technique and fist-and-foot martial arts.
- **Personality:** Arrogant, status-conscious, abusive, and fiercely proud of his power, he responds to humiliation with anger and protects himself even while his allies die.
- **Voice:** Loud, insulting, entitled, and dependent on national and political status.
- **Relationships:** He is openly hostile toward Jin Taekyung and Faye Chen, and resents Jin receiving Chairman Shao Yang's attention.

## Korean source

```text
＃415화



전투의 시작은 빠르게 찾아왔다.

광야를 뒤덮으며 파도처럼 밀려드는 짙은 안개와 수만의 몬스터 앞에서, 허공을 밟으며 우뚝 선 검은 피부의 대마도사는 이 전투의 서막을 알리는 한 마디를 내뱉었다.

「파이어 캐논(Fire Cannon).」

솨아아아아.

그를 중심으로 휘몰아치는 막대한 마나. 허공에서 피어오른 다섯 개의 불꽃이 크기를 부풀리고, 이내 포탄처럼 쏘아졌다.

후우우우웅, 꽈앙!

수만의 몬스터로 이루어진 검은 파도가 갈라졌다. 초고온의 열기가 살과 뼈를 태우고 지면을 녹였다.

족히 일천에 달하는 병력을 잿더미로 만들어 버린 광역 마법.

하지만 몬스터는 멈추지 않았고, 그것은 매직 존슨 역시 마찬가지였다.

「워터 블레스터(Water Blaster).」

파이어 캐논의 발현으로 모래알처럼 건조하던 공기가 축축한 습기를 머금었다.

매직 존슨이 양팔을 펼치자 그의 등 뒤로 거대한 파도가 솟아올랐다.

세상의 모든 법칙을 거스르는 광경.

그것은 말 그대로 마법이었고 수많은 마법사 중에서도 최고의 워 메이지(War Mage)가 선보이는 이능, 그 자체였다.

「뒤덮어라.」

늘 유쾌하고 웃음이 끊이질 않던 평소의 모습은 더 이상 찾아볼 수 없다.

매직 존슨은 깊게 가라앉은 눈빛으로 두 손을 떨쳤다. 수십 미터의 파도가 수만의 몬스터 위로 넓고 어두운 그림자를 드리웠다.

콰아아아!

마나를 한껏 머금고 덮쳐 온 파도. 엄청난 수압(水壓)에 짓눌린 몬스터의 몸뚱어리가 터지고 조각났다.

파이어 캐논이 남긴 불길이 꺼지고 사방이 물로 흥건했다. 그리고 매직 존슨은 자신이 무엇을 해야 할지 정확히 알고 있었다.

「내리쳐라. 라이트닝 레인(Lightning Rain).」

순식간이었다. 몬스터들의 머리 위로 새카만 먹구름이 모여들고, 수십 줄기의 낙뢰(落雷)가 내리꽂힌 것은.

콰광! 파지지직!

- 크워어어어어!

- 캬아악!

낙뢰는 공중과 지상을 가리지 않았다.

새카맣게 그을린 가고일과 그리핀이 허공에서 추락했고, 워터 블래스터의 영향으로 흠뻑 젖어 있던 지면이 전류를 전달했다.

살아 있는 몬스터는 외마디 괴성과 함께 몸을 부르르 떨며 무릎을 꿇었으며 언데드는 잿가루가 되어 허물어졌다.

눈앞에서 펼쳐진 믿을 수 없는 광경에, 누군가의 입술 사이로 신음이 흘러나왔다.

「이것이 대마도사…….」

단 세 번의 광역마법이 불러온 결과는 엄청났다.

족히 수천에 달하는 몬스터가 죽거나 전투 불능 상태에 빠졌고 몬스터 군단의 일각이 무너졌으니까.

하지만 홀로 천재지변을 일으킨 대마도사 역시 극심한 피로를 느낄 수밖에 없었다.

「Fuck. 이럴 줄 알았으면 마법 몇 개만 더 아껴 두는 건데.」

마법의 발현은 까다롭다. 특히 매직 존슨의 주특기인 광역 마법은 파괴력만큼이나 정신력과 마나의 소모가 엄청난 수준이었다.

이곳에 도착하기에 앞서 전선에서 쏟아부은 마법을 생각하면 이 정도가 한계다.

「미세스 첸. 나도 늙었나 봐.」

「물러나요. 나이 든 사람끼리 돕고 살아야지. 그리고…….」

손에 들고 있던 위스키병을 내던진 파이 첸이 번개 같은 속도로 옆구리에 매어 둔 활을 꺼내 시위를 당겼다.

텅 비어 있던 활시위에 마나로 이루어진 화살이 맺힌다.

「미세스가 아니라 미스 첸이야. 누구 맘대로 유부녀래?」

코웃음을 친 파이 첸이 활시위를 놓았다. 휘황한 광채를 뿌리는 마나의 화살이 날카로운 파공성과 함께 쏘아진다. 공간을 지우고, 짙은 안개를 갈랐다. 그리고 다음 순간.

콰앙!

거대한 폭발이 일어났다.

수많은 몬스터 사이에 숨어 있던 데스나이트가 단말마도 내지르지 못하고 소멸한 것을 확인한 파이 첸이 재차 활시위를 당겼다.

투투투퉁!

눈 깜짝할 사이에 쏘아진 화살들이 빛줄기가 되어 광야를 가로질렀다. 굉음과 폭발. 한 발, 한 발에 수십 마리의 몬스터가 휩쓸리고 소멸한다.

매직 존슨이 전 세계에서 세 손가락 안에 드는 대마도사요, 최고의 워 메이지라면 파이 첸은 세계 최고의 궁사(弓師)다.

하지만…….

- 그워어어어어!

- 캬우우!

수만에 달하는 몬스터 군단은 그 모든 것을 무시하고 돌격했다.

수십을 쓰러트리면 수십. 수백을 쓰러트리면 수백이 그 자리를 메운다.

짙은 안개에 휩싸여 돌격하는 그들은 평범한 몬스터보다 강했고, 더욱 흉포했다. 이제 남은 것은 피할 수 없는 전면전뿐.

밀려드는 몬스터 군단을 향해, 두 사람이 동시에 발을 내디뎠다.

“아레스 길드. 포메이션 B. 놈들을 돌파한다.”

처처척!

이정룡의 나직한 목소리에, 단 한 사람의 사상자도 없이 이곳까지 도달한 정예 길드원들이 한 몸처럼 움직인다.

그 모습을 유심히 바라본 진태경이 서부 전선에서 데려온 결사대를 향해 말했다.

“전원 포메이션 J.”

「옛!」

「포메이션 J! 대형 갖춰!」

우렁찬 복명복창과 함께 결사대가 신속하게 움직였다.

진태경의 뒤에서 한 줌밖에 안 되는 홍위방 헌터를 끌어모으고 있던 우헤이싱이 서부 전선 결사대원 중 한 명을 붙잡고 물었다.

「거기 애송이. 포메이션 J가 도대체 뭐지?」

우헤이싱을 알아본 샤오 쉔이 눈살을 찌푸리며 대답했다.

「형님께서 정해 주신 전투 대형입니다.」

「그러니까. 그게 무슨 뜻이냐고.」

「그냥. JONNA 싸우라는 의미라고 하시던데요.」

「……!」

우헤이싱은 순간 할 말을 잃었고, 이정룡과 진태경은 약속이라도 한 것처럼 동시에 몸을 날렸다.

그리고 그런 그들의 뒤를 필릭스 왕자와 일만의 헌터가 맹렬히 뒤따랐다.

「으아아아아아!」

- 크와아아아악!

인간과 몬스터.

몬스터와 인간.

먹먹한 함성과 살기가 터져 나온다. 눈부신 속도로 광야를 가로지른 그들은 서로를 향해 이빨과 창칼을 들이밀었다.

쐐애애애액, 콰드드득!

대혈전의 시작이었다.



* * *



허리를 젖히고, 어깨에 힘을 실었다. 물 흐르듯 이어진 동작과 함께 있는 힘껏 팔을 흩뿌렸다.

쐐액, 퍼버버버벅!

내 손을 떠나 쏘아진 백염(白炎)이 수십 마리의 몬스터를 관통하며 길을 만든다.

순간 뻥 뚫린 공백. 망설임 없이 빈틈을 파고든 나는 닥치는 대로 팔과 다리를 휘둘렀다.

뻑!

보이지도 않는 속도로 내지른 일권에 달려드는 라이칸스로프의 머리통이 수박처럼 으스러졌다.

놈의 머리에서 흐른 뇌수가 바닥에 닿기도 전에 나는 솟구쳐 올랐다.

타닥, 쉭!

4m에 달하는 체구. 이미 빛이 사라진 희끄무레한 동공에 내 모습이 비쳤다.

하지만 언데드 트롤이 손에 든 곤봉을 휘두르기도 전에, 내 일장(一掌)이 놈의 가슴을 후려쳤다.

퍼벙!

막대한 열기와 함께 언데드 트롤의 칠공(七空)에서 연기가 모락모락 솟구친다. 내부에 엄청난 타격을 입은 놈은 특유의 재생력을 발휘할 새도 없이 완전한 죽음을 맞이했다.

- 간악한 인간이여! 뒤!

알아, 인마. 어디서 훈수를.

내심 중얼거린 나는 고개를 틀었다. 칠흑빛 마력이 서린 돌격창이 아슬아슬하게 목을 스치며 허공으로 솟구친다.

공중에서 체공할 때를 노린 투창. 좋은 타이밍이었지만 적이 간과한 건 나를 너무 얕봤다는 거다.

“시벌. 뭔 놈의 데스나이트가 이렇게 많아. 치킨집도 아니고.”

창을 피해 가뿐히 착지한 나를 향해, 해골마를 탄 데스나이트가 빠르게 돌격해왔다.

- 여. 기. 까. 지. 다!

후우우웅!

외침과 함께 불길한 마력이 서린 검이 휘둘러진다. 비록 S급 헌터에 비견할 수는 없겠지만, 최상위 A급 헌터에 버금가는 기운이다.

아니, 어쩌면.

‘이 데스나이트 역시 한때 헌터였겠지.’

그래서였을지도 모르겠다. 데스나이트의 모습에서 레이페이를 떠올린 나는 문득 씁쓸해졌고, 그런 내 모습에 스켈레톤 워로드는 비명을 내질렀다.

- 피해라, 인간!

푸푹!

검에 서려 있던 마력이 씻은 듯이 사라졌다.

자신의 가슴을 관통하고 튀어나온 투명한 창날을 물끄러미 바라보던 데스나이트가 힘없이 중얼거렸다.

- 어. 떻. 게.

“여기까지다.”

앞서 데스나이트가 했던 말을 고스란히 돌려준 내가 수도(手刀)를 내리그었다.

“네가 누구였는지는 몰라도, 고생했다.”

서걱, 쿵!

해골마와 데스나이트가 두 쪽으로 갈라져 소멸한다. 앞에서처럼 허공섭물(虛空攝物)로 백염을 끌어당겨 몬스터를 벤 내가 불쑥 입을 열었다.

“웬일로 밥 달라고 안 조르냐.”

- 크흠. 사람을, 아니 본 사령관을 뭘로 보고 감히.

촤아악!

“밥벌레. 자칭 평화주의자라면서 이럴 때만 군침 흘리는 노양심.”

- 뭣이!

“왜, 구구절절 맞는 말 아니냐?”

- 전투에 참여하지 않는 건 너, 간악한 인간도 동의하지 않았느냐! 애초에 다른 인간들에게 들키면 안 된다고 말할 땐 언제고!

“핑계는. 그래서 저 마력, 먹을래, 말래?”

- …….

퍼걱!

“야. 안 들려?”

- 음. 별로 흡수하고 싶지 않다.

“……뭐?”

쉬이이익!

순간 깜짝 놀라는 바람에 공격을 허용할 뻔했다.

크게 창을 휘둘러 십여 마리를 쓸어 버린 내가 심각하게 물었다.

“왜 그래. 소멸할 때가 된 거 아냐?”

- 으음……. 나도 모르겠다. 그냥 기분이 그렇다.

“기분?”

- 그래. 나도 언데드다. 가끔 기분이 싱숭생숭할 때가 있는 법이니 냅두거라.

“……언데드가 싱숭생숭할 때가 어디 있어.”

평소 같았으면 나흘 굶은 개방도 마냥 달려들었을 놈이 왜 이러지?

‘언데드한테도 사춘기가 오나.’

아무리 스켈레톤 워로드가 괴짜 몬스터라고 해도, 말도 안 되는 소리다.

더 이상 녀석에 대해 생각하는 것을 포기하고 몬스터를 베어 나가던 그때였다.

콰과과과과!

반경 십여 미터를 뒤덮은 오러, 아니 검기(劍氣).

순간 텅텅 비어 버린 전선의 중앙에 한 사람이 사뿐히 내려앉았다.

“몬스터의 숫자가 너무 많네. 결사대 전원이 빠져나갈 길을 만드는 건 무리야.”

나는 이정룡이 하는 말의 뜻을 정확히 알아들었다.

“말인즉슨, 소수 정예로 가자?”

“바로 그거지. 숙이게.”

이정룡의 말에 허리를 젖히자 반월의 검기가 날아와 대형 몬스터 서너 마리를 치즈 케이크처럼 잘라 버렸다.

저 검기가 나를 향했다면 어땠을까. 만약 나와 이정룡이 맞붙는다면…….

“자네와 나, 우헤이싱. 이렇게 셋이라면 충분할 걸세.”

나는 메마른 입술을 핥으며 대꾸했다.

“그것참 희한하네요.”

“뭐가 말인가?”

“싸워 보기 전에는 모르는 법 아닙니까. 아크 리치가 얼마나 강한지는 붙어 봐야 알 텐데.”

“S급 헌터가 셋일세. 아크 리치가 아무리 강하다 해도 우리의 상대는 되지 못해.”

우리, 라…….

참 좋은 말인데 어째서일까. 혀끝에서 굴러가는 발음이 영 마음에 들지 않는다.

어쩌면 ‘우리’에 포함된 저들의 면면 때문일지도 모르지.

하지만 나는 이미 결사대 작전을 제안했을 때부터 결심한 상태다. 그런 의미에서 방금 이정룡의 제안은 최선이었다.

“그렇게 하시죠. 우헤이싱은 어디 있습니까?”

콰드드득!

말이 끝나기가 무섭게 몬스터를 헤집고 우헤이싱이 모습을 드러냈다.

전투 중이라고는 믿기지 않을 만큼 깔끔한 이정룡과는 달리 형편없는 몰골을 하고 있었지만, 형형한 눈빛은 힘이 충분하다는 증거였다.

“다행히 늦지 않게 왔군.”

「후욱. 몬스터 따위가 절 막을 수는 없지요.」

저놈, 한 시간 전쯤에 바로 그 몬스터 따위한테 죽을 뻔하지 않았었나?

도무지 나아지지 않는 우헤이싱의 모습에 내심 혀를 차고 있던 그 순간이었다.

“진태경 씨!”

저 멀리서 들려오는 최 팀장의 외침.

그와 나 사이에 존재하는 수백의 몬스터를 너머로 언뜻 최 팀장의 얼굴이 나타났다가 사라진다.

그리고 번쩍이는 무언가가 허공을 빙글빙글 돌아 근처에 꽂혔다.

‘이건…….’

어렵지 않게 알아볼 수 있었던 그것은 바로 [영웅의 혼]이었다. 보이지 않는 곳에서 최 팀장이 외쳤다.

“함께 가겠다는 말은 하지 않을 테니, 대신 그 검을 들고 가세요. 그리고…… 조심하십시오!”

많은 의미가 담긴 말이다. 나는 말 없이 [영웅의 혼]을 뽑았다.

아직도 눈앞을 가득 메운 수많은 몬스터 너머로, 어둠에 휩싸인 도시가 보였다.

“갑시다.”

이정룡이 부드럽게 웃었다.
```

## Final English reading copy

```markdown
# Chapter 415

The battle began quickly.

Before the tens of thousands of monsters and the thick fog that rolled over the wasteland like waves, a black-skinned Archmage stood tall, stepping on empty air, and uttered the first word of the battle.

“Fire Cannon.”

*Fwoooooosh.*

An enormous amount of mana swirled around him. Five flames rose from empty air, swelled in size, and shot forward like cannonballs.

*Fwoooooosh—BOOM!*

The black wave composed of tens of thousands of monsters split apart. Superheated air burned flesh and bone and melted the ground.

An area-of-effect spell that reduced at least a thousand soldiers to ash.

But the monsters did not stop.

And neither did Magic Johnson.

“Water Blaster.”

The air, dry as sand when he cast Fire Cannon, grew damp with moisture.

When Magic Johnson spread both arms, a massive wave rose behind him.

It was a sight that defied every law of the world.

It was magic in the truest sense of the word—the very embodiment of the supernatural power displayed by the greatest War Mage among countless mages.

“Cover them.”

The cheerful man who was always laughing was nowhere to be seen.

Magic Johnson flung both hands out, his gaze grave. A wave dozens of meters high cast a broad, dark shadow over the tens of thousands of monsters.

*Roooooar!*

The wave, brimming with mana, crashed down. Under the tremendous water pressure, the monsters’ bodies burst apart and were torn into pieces.

The flames left behind by Fire Cannon went out, and the surrounding area was flooded with water.

Magic Johnson knew exactly what he had to do next.

“Rain down. Lightning Rain.”

It happened in an instant.

Black storm clouds gathered over the monsters’ heads, and dozens of bolts of lightning came crashing down.

*BOOM! Crackle!*

—Kraaaaaaar!

—Kyaaak!

The lightning struck targets in the air and on the ground indiscriminately.

Blackened Gargoyles and Griffins fell from the air, while the ground, soaked by Water Blaster, carried the current.

The living monsters trembled violently and dropped to their knees with a single shriek. The undead collapsed into piles of ash.

At the unbelievable sight unfolding before our eyes, a groan escaped someone’s lips.

“This is an Archmage…”

The result of only three area-of-effect spells was staggering.

At least several thousand monsters had either died or been rendered incapable of fighting, and one flank of the monster army had collapsed.

But the Archmage who had single-handedly caused a natural disaster could not help but feel exhausted.

“Fuck. If I’d known this would happen, I would’ve saved a few more spells.”

Casting magic was difficult. Magic Johnson’s specialty, area-of-effect magic, consumed an incredible amount of mental strength and mana in proportion to its destructive power.

Considering the magic he had poured out on the front lines before arriving here, this was his limit.

“Mrs. Chen. I guess I’m getting old too.”

“Move aside. Old people have to help one another. And…”

Faye Chen threw away the whiskey bottle in her hand, drew the bow strapped to her side at lightning speed, and pulled back the string.

An arrow made of mana formed on the empty bowstring.

“Not Mrs. Chen. Miss Chen. Who decided I was married?”

Faye Chen snorted and released the bowstring.

The mana arrow, scattering a dazzling radiance, shot forward with a sharp whistle. It erased the space in its path and split through the thick fog.

And then—

*BOOM!*

A huge explosion erupted.

After confirming that the Death Knight hiding among the countless monsters had vanished without even managing a final cry, Faye Chen pulled back her bowstring again.

*Thrum-thrum-thrum!*

The arrows shot in the blink of an eye became streaks of light that crossed the wasteland. Thunderous booms and explosions rang out. With every arrow, dozens of monsters were swept away and annihilated.

If Magic Johnson was an Archmage counted among the top three in the world and the greatest War Mage alive, Faye Chen was the world’s finest archer.

But…

—Gwooooooar!

—Kyaaaaa!

The monster army numbering in the tens of thousands ignored everything and charged.

Whenever dozens fell, dozens more filled their places. Whenever hundreds fell, hundreds more took their place.

Surging through the thick fog, they were stronger and more ferocious than ordinary monsters.

Now, only an unavoidable frontal battle remained.

The two of them stepped forward at the same time, facing the oncoming monster army.

“Ares Guild. Formation B. Break through them.”

*Clatter-clatter-clatter!*

At Lee Jungryong’s low voice, the elite Guild members who had reached this place without suffering a single casualty moved as one.

Jin Taekyung watched them closely, then spoke to the suicide squad he had brought from the Western Front.

“Everyone, Formation J.”

“Yes, sir!”

“Formation J! Get into position!”

With thunderous call-and-response, the suicide squad moved swiftly.

Behind Jin Taekyung, Wu Heixing had been gathering the handful of Red Guard Gang Hunters who remained. He grabbed one of the Western Front suicide-squad members and asked,

“Hey, rookie. What the hell is Formation J?”

Shao Shen, who recognized Wu Heixing, frowned and answered,

“Hyung is the one who came up with this battle formation.”

“So what does that mean?”

“Nothing special. He said it means, ‘Just fucking fight.’”

“…”

Wu Heixing was momentarily speechless, and Lee Jungryong and Jin Taekyung launched themselves forward at the exact same time, as if they had planned it.

Prince Felix and ten thousand Hunters followed fiercely behind them.

“Aaaaaaaaah!”

—Kraaaaaaaargh!

Humans and monsters.

Monsters and humans.

Deafening battle cries and killing intent erupted. Crossing the wasteland at blinding speed, the two sides thrust teeth, spears, and blades at one another.

*Fwoooooosh—Kra-d-d-d-d-k!*

The great battle had begun.

* * *

I leaned back, putting strength into my shoulder. With a fluid motion, I whipped my arm forward with all my strength.

*Whoosh—thud-thud-thud-thud!*

White Flame shot from my hand and pierced through dozens of monsters, opening a path.

A gap suddenly appeared.

Without hesitation, I plunged into the opening and swung my arms and legs at anything within reach.

*Crack!*

My fist shot forward at a speed too fast to see, and the head of the Lycanthrope charging at me crumpled like a watermelon.

Before the brain matter flowing from its skull could even reach the ground, I leaped upward.

*Tap—whoosh!*

It stood nearly four meters tall. My reflection appeared in its pale pupils, long since drained of light.

But before the Undead Troll could swing the club in its hand, my palm struck its chest.

*Boom!*

Along with tremendous heat, smoke rose from the Undead Troll’s seven openings. It had suffered massive internal damage and met its final death before it could even bring its characteristic regenerative power into play.

—Wicked human! Behind you!

*I know, idiot. Who asked for your advice?*

I turned my head. A lance infused with black magic skimmed dangerously past my neck and shot into the air.

It was a thrown spear aimed at the moment I was airborne. The timing was good, but the enemy had made one mistake: it had underestimated me.

“Fuck. Why are there so many Death Knights? This isn’t a chicken joint.”

A Death Knight riding a skeletal horse charged rapidly toward me.

—This. Is. As. Far. As. You. Go!

*Fwoooooosh!*

Along with its shout, the sword infused with ominous magic swung toward me. It could not compare to an S-rank Hunter, but the energy it radiated was comparable to that of a top-tier A-rank Hunter.

Or perhaps…

*This Death Knight must have been a Hunter once too.*

Maybe that was why.

The Death Knight’s appearance reminded me of Lei Fei, and a bitter feeling briefly settled over me.

Seeing me like that, the Skeleton Warlord screamed.

—Dodge, human!

*Thud!*

The magic clinging to the sword vanished as if it had been washed away.

The Death Knight stared blankly at the transparent spearhead that had pierced through its chest and emerged from its back. Then it muttered weakly,

—How…

“This is as far as you go.”

I returned the Death Knight’s own words to it and brought down the edge of my hand.

“I don’t know who you were, but you’ve been through a lot.”

*Slash—thud!*

The skeletal horse and the Death Knight split in two and vanished.

Using Seizing an Object Through Empty Space to pull White Flame toward me, I cut down a monster just as I had before, then suddenly opened my mouth.

“How come you’re not pestering me for food today?”

—Ahem. What do you take me for? How dare you mistake this commander for—

*Slash!*

“Food parasite. You call yourself a pacifist, but you only drool at times like this. Shameless bastard.”

—What did you say?

“Why? Isn’t every word true?”

—You, wicked human, agreed that I should not participate in the battle! And when you told me I couldn’t let the other humans find out about me, when did you suddenly change your tune?

“Quit making excuses. So, are you going to absorb that mana or not?”

—…

*Crack!*

“Hey. You hear me?”

—Hmm. I don’t particularly want to absorb it.

“…What?”

*Fwoooooosh!*

I was so startled that I almost let an attack hit me.

After swinging my spear in a wide arc and sweeping away a dozen monsters, I asked seriously,

“What’s wrong? Is it time for you to vanish?”

—Hmm… I don’t know either. I just feel this way.

“Feel this way?”

—Yes. I’m undead too. Sometimes I feel unsettled. Leave me be.

“…When does an undead get unsettled?”

Normally, he would have charged in like a Beggars’ Sect disciple who had not eaten in four days. Why was he acting like this?

*Can undead go through puberty too?*

No matter how strange a monster the Skeleton Warlord was, that made no sense.

I gave up on thinking about him and continued cutting down monsters.

That was when it happened.

*Rooooooar!*

Aura—no, Sword Energy—covered a radius of more than ten meters.

A person landed lightly in the center of the front line, which had suddenly been emptied.

“There are too many monsters. It’s impossible to make a path for the entire suicide squad to get through.”

I understood exactly what Lee Jungryong meant.

“You’re saying we should go with a small elite force?”

“That’s right. Duck.”

At Lee Jungryong’s words, I leaned backward, and a crescent of Sword Energy flew past me, slicing three or four enormous monsters apart like cheesecake.

*What if that Sword Energy had been aimed at me? If Lee Jungryong and I fought…*

“You, me, and Wu Heixing. The three of us should be enough.”

I licked my dry lips and answered,

“That’s a strange thing to say.”

“What is?”

“You never know until you fight. We’ll only know how strong the Arch Lich is after we face it.”

“There are three S-rank Hunters here. No matter how strong the Arch Lich is, it cannot stand against us.”

*Us…*

It was a wonderful word. So why did I dislike the way it felt rolling off my tongue?

Maybe it was because of the people included in that word.

But I had already made up my mind when I proposed the suicide-squad operation. In that sense, Lee Jungryong’s suggestion was the best option.

“Let’s do that. Where is Wu Heixing?”

*Kra-d-d-d-d-k!*

Before I had even finished speaking, Wu Heixing appeared, tearing through the monsters.

Unlike Lee Jungryong, who looked so clean that it was hard to believe he was in the middle of a battle, Wu Heixing was in terrible shape. But the fierce light in his eyes proved that he still had plenty of strength left.

“Good. You made it in time.”

Wu Heixing let out a ragged breath. “Mere monsters could never stop me.”

*Didn’t that bastard nearly die to those very same monsters about an hour ago?*

A moment later, a shout came from far away.

“Mr. Jin!”

Team Leader Choi’s voice.

His face appeared and vanished in the distance, beyond the hundreds of monsters between him and me.

Then something flashing spun through the air and struck the ground nearby.

*This is…*

I recognized it without difficulty.

It was **Hero’s Soul**.

From somewhere I could not see, Team Leader Choi shouted,

“I’m not going to say I’ll go with you, so take that sword with you instead. And… be careful!”

His words carried many meanings.

Without saying anything, I pulled **Hero’s Soul** from the ground.

Beyond the countless monsters still filling my field of vision, I could see a city shrouded in darkness.

“Let’s go.”

Lee Jungryong smiled gently.
```

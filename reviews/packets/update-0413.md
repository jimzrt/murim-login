<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0413.txt",
      "sha256": "ca1dcb284df1a133b0681258e0eabf34d32b9a158333d697db852d912bd6fcbe",
      "bytes": 13298
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "03a91912cc1880507e10d6b2e699676cc701bcba284d5092d82a97442e295b95",
      "bytes": 1581
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "850bda0db577c6b68d9d4d5d96b2a0cd5b6de0645d410997ab21de7590735d5f",
      "bytes": 137994
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "07213f5ab13f8dc636cf053d09a3659278918852ad7a3583b5b1b976870978fd",
      "bytes": 533
    },
    {
      "path": "characters/Go Jun.md",
      "sha256": "dae6bebe11a20a136ca2524b82d17a08044fa434229d3b6e9f38f8d829a097ac",
      "bytes": 811
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "6d430a905dfa15dd931b255d3ee6c5906e020ebf47bc28d92686e8eed3beb19d",
      "bytes": 1270
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "4d034e04039fdae53c2d4fd0d59ff7f7051dc1602dccd17a494f66d10f284e5f",
      "bytes": 622
    },
    {
      "path": "characters/Lee Jungryong.md",
      "sha256": "d375eedeb429b7e2d5b8901145f9d6176db66078e7085a0655302bdc50b99702",
      "bytes": 1163
    },
    {
      "path": "characters/Lei Fei.md",
      "sha256": "142653f2296cdc261d2a17970712cbb4a8444f0a87d7a34d2138997a7158586b",
      "bytes": 893
    },
    {
      "path": "characters/Wu Heixing.md",
      "sha256": "516d02162a04429deda358003ff597c371fdb0d20761abe040a7376fdbcb8184",
      "bytes": 735
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "ca6b72c80c8c285ab10d6bdc073c6f502541b604057f8a9b21f56facd71d63be",
      "bytes": 125818
    }
  ],
  "estimated_tokens": 10783
}
-->

# Durable State Update — Chapter 413

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 413. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 413. Profile updates may replace only one
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
  "chapter": 413,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 413,
    "continuity_sources": [413],
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
    "Jin Taekyung is leading more than two hundred suicide-squad members through the Arch Lich's battlefield toward Lee Jungryong and Wu Heixing.",
    "Jin's One Annihilation erased ten Darkened Death Knights and Liches, countless elite monsters, and the Arch Lich's observing Familiars.",
    "Jin gained four Levels, massive EXP and Fame, the Title One Against a Thousand, and the new Intimidation stat.",
    "One Against a Thousand enhances Jin's performance against multiple enemies, reduces fatigue consumption, intimidates enemies, and raises allied morale.",
    "The suicide squad used the breach created by One Annihilation to resume its advance as a unified force.",
    "The Arch Lich's Familiar Link was severed, its ten empowered guards were destroyed, and the resulting backlash injured it.",
    "The Arch Lich suspects Jin may be the ancient human Adversary who defeated it in the past."
  ],
  "continuity_sources": [
    412,
    411
  ],
  "open_questions": [
    "Is Jin the ancient human Adversary remembered by the Arch Lich?",
    "What was the Arch Lich's former identity, and what became of the king it once served?",
    "Can Jin and the suicide squad reach Lee Jungryong and Wu Heixing after exploiting the breakthrough?"
  ],
  "safe_through": 412,
  "temporary_decisions": [
    "Render 일기당천 as One Against a Thousand.",
    "Render 위압 as Intimidation.",
    "Render 어둠에 물든 as Darkened.",
    "Render 마계어 as Demon Realm language.",
    "Render 결사대 as suicide squad."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 이정룡    | **Lee Jungryong** |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 제자     | **Disciple**                                 |
| 일격     | **One Strike**                         |
| 상태               | **Status**                     |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 레이드     | **raid**              |
| 길드      | **Guild**             |
| 길드장     | **Guild Master**      |
| 부길드장    | **Vice Guild Master** |
| 팀장      | **Team Leader**       |
| 마법사     | **mage**              |
| 도사      | **Daoist**                                                      |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 고준 | **Go Jun** | Personal name of Team Leader Seok; Lee Jungryong's prized Disciple. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 레이페이 | **Lei Fei** | Concealed Chinese S-rank Hunter and head of the Public Security Armed Forces Department in Sichuan Province. |
| 우헤이싱 | **Wu Heixing** | Chinese S-rank Hunter who provokes Jin and nearly draws his sword. |
| 아레스 | **Ares Guild** | The leading Guild in Korea; formerly employed Team Leader Choi and Song Song. |
| 환각 | **Hallucination** | System effect that the Matador’s Shield can activate against bovine-type monsters. |
| 태자 | **Crown Prince** | Title of the Emperor's older brother who was reportedly assassinated. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 오우거 | **ogre** | B-rank monster species emerging from the Gate. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 와이번 | **Wyvern** | High-tier dragonkin monster. |
| 산주 | **Mountain Lord** | Anhui title for Jeok Cheongang as master of Mount Jiuhua. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 준이 | **Jun** | Family nickname used in the form Jun's dad. |
| 석고준 | **Go Jun** | Source full-name form for the established Go Jun, also known as Team Leader Seok. |
| 도련님 | **Young Master** | Address used for Team Leader Choi by Butler Kim. |
| 경호팀장 | **Head of Security** | Go Jun's security-team office under Lee Jungryong. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 신력 | **divine strength** | Superhuman strength attributed to Taekyung. |
| 태자당 | **Crown Prince Party** | The faction associated with General Liao. |
| 데스나이트 | **Death Knight** | Undead commander type serving under the Black Knight. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 이정룡 | 진태경 | senior S-rank Hunter to younger Hunter and adversary | Young man | polished, teasing, and veiled-threatening | Uses a genial tone and indirect threats while trying to make Taekyung release the captives. |
| 진태경 | 이정룡 | younger Hunter to senior S-rank Hunter and adversary | you | polite but mocking and defiant | Taekyung answers Lee's soft threats with the wolf-and-tiger metaphor and refuses to yield. |
| 이정룡 | 고준 | Master to Disciple | Go Jun | familiar and testing | Lee switches from Seok's office title to his personal name while considering whether he can defeat Taekyung. |
| 고준 | 이정룡 | Disciple to Master | Master | deferential | Go Jun responds to Lee's personal-name address as 스승님. |
| 마법사 | 이정룡 | Ares Guild mage subordinate to Vice Guild Master | Vice Guild Master | formal-deferential | Lee's five direct A-rank mages greet him and receive instructions for concealing the battle. |
| 진태경 | 석고준 | returning Hunter to hostile Ares security leader | you fucking bastard | hostile and profane | Taekyung directs his final insults and challenge at Go Jun after returning alive. |
| 석고준 | 진태경 | hostile_opponents | brat | hostile and overconfident | Go Jun addresses Taekyung internally as 애송아 while launching his full-strength attack. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 우헤이싱 | 진태경 | hostile S-rank Hunter to foreign Hunter and provocation target | peninsula bangzi | insulting and confrontational | Wu repeatedly addresses Jin with anti-Korean slurs. |
| 우헤이싱 | 이정룡 | younger S-rank Hunter to senior Ares Guild authority | Mr. Lee | formal and deferential | Wu addresses Lee respectfully despite his usual hostility toward Koreans. |
| 데스나이트 | 인간 | enemy combatants | human | contemptuous and commanding | Used in the Death Knight's warnings to Jin. |
| 진태경 | 레이페이 | former ally and fellow Hunter | Lei Fei | blunt and solemn | Jin addresses Lei Fei by name before telling him to rest. |
| 레이페이 | 진태경 | former ally and fellow Hunter | you | familiar and respectful | Lei Fei uses 자네 and 하게 while asking Jin to help him fulfill his final mission. |
| 진태경 | 우헤이싱 | adversarial S-rank Hunters | you idiot | insulting-casual | Mocks Wu's cowardice and orders him to stop complaining. |
| 이정룡 | 우헤이싱 | senior S-rank Hunter to younger allied S-rank Hunter | Mr. Wu | polished and formally coaxing | Lee publicly draws Wu into agreement with the suicide-squad plan. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 412
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who has sworn never to kill again.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Go Jun.md

# Go Jun (고준)

- **Safe through:** Chapter 410
- **Aliases:** Team Leader Seok
- **Role:** Leader of Lee Jungryong's security team, an Ares Guild combatant, and Lee's disciple and right-hand man.
- **Personality:** Highly disciplined, fiercely loyal to Lee Jungryong, confident in his abilities, and angered by operational failures that endanger his Master.
- **Voice:** Dry, controlled, and formal with subordinates; deferential when addressing his Master.
- **Relationships:** Disciple and direct protégé of Lee Jungryong; leader of Lee's security detail; regarded by Lee as stronger than Park Tae Seop; after Go Jun's defeat by Jin Taekyung, Lee reaffirmed his faith in Go Jun and promised to give him the strength to defeat Taekyung.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 412
- **Aliases:** Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, and a Supreme Peak master who has manifested Force and crossed the wall into true mastery.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and student, his mother and sister Hayeon are among those he protects, and the Skeleton Warlord is his captive undead commander.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 412
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Lee Jungryong.md

# Lee Jungryong (이정룡)

- **Safe through:** Chapter 411
- **Aliases:** None
- **Role:** Vice Guild Master of Ares Guild, one of Korea's two S-rank Hunters, and a Supreme Peak-level martial artist who directs Ares Guild operations.
- **Personality:** Outwardly genial, calm, and humorous; calculating, manipulative, coercive, and ruthless when challenged
- **Voice:** Smooth, good-natured, and indirect, using teasing conversation and veiled threats before becoming openly furious
- **Relationships:** Master of Park Jihoon and Go Jun (Team Leader Seok), whom he personally selected and trained; longtime Great Cataclysm acquaintance of Park Tae Seop; adversary of Jin Taekyung; knew Team Leader Choi from childhood; has an antagonistic history with Kim Hwajong, who saved his life at the collapse of Mapo Bridge eighteen years earlier; was visibly shaken by learning that Choi is Cheon Taemin's maternal grandson; regards Cheon Taemin as an older brother despite no blood relation and has long held him in respect and fear; operates as Ares Guild's senior authority beneath its Guild Master

### Lei Fei.md

# Lei Fei (레이페이)

- **Safe through:** Chapter 412
- **Aliases:** None
- **Role:** Lei Fei is a concealed Chinese S-rank Hunter and former head of the Public Security Armed Forces Department in Sichuan Province who recovered his human identity after becoming a level-120 undead Death Knight Lord and died fulfilling his final mission.
- **Personality:** Lei Fei's recovered memories show him as dutiful, honorable, family-oriented, and willing to serve as an unseen guardian.
- **Voice:** His human voice is formal and earnest, becoming warm and playful with family.
- **Relationships:** Wei Fenghu is his maternal uncle who raised him as a son; Lei Fei married an unnamed flower-shop owner and had a daughter, trained alongside Wu Heixing, and was corrupted by the Arch Lich before Jin Taekyung restored his identity.

### Wu Heixing.md

# Wu Heixing (우헤이싱)

- **Safe through:** Chapter 411
- **Aliases:** None
- **Role:** Wu Heixing is a Chinese S-rank Hunter known for frequent media exposure and scandal who secretly practices martial arts, including an internal-energy cultivation technique and fist-and-foot martial arts.
- **Personality:** Arrogant, status-conscious, abusive, and fiercely proud of his power, he responds to humiliation with anger, jealousy, and fear.
- **Voice:** Loud, insulting, entitled, and dependent on national and political status.
- **Relationships:** He is openly hostile toward Jin Taekyung and Faye Chen, and resents Jin receiving Chairman Shao Yang's attention.

## Korean source

```text
＃413화



후우웅, 쾅!

거대한 대검이 지면을 박살 낸다. 정확히 반 뼘 차이로 공격을 피해 낸 우헤이싱의 신형이 번개처럼 솟구쳤다.

푸푹!

오우거의 턱 밑을 파고든 검날이 정수리 위로 삐죽 솟아올랐다.

정확하고 군더더기 없는 일격. 박혀 있는 검을 뽑아낸 우헤이싱이 쓰러지는 오우거의 어깨를 밟으며 몬스터들 사이로 떨어져 내렸다.

손에 들린 검은 허공에 무수한 선을 그려 내고 있었다.

‘십이혈라검(十二血羅劍).’

1966년부터 1976년까지 이어진 문화대혁명을 두고 혹자는 천인공노할 행위라며 손가락질했지만, 또 다른 누군가에게는 절호의 기회였다.

마오쩌둥의 오랜 정치적 동지였던 우헤이싱의 조부는 화려하게 비상하며 천문학적인 재산을 착복했고, 홍위병이었던 아들을 징검다리 삼아 각종 문화재와 고서(古書)를 빼돌렸다.

우헤이싱이 익힌 십이혈라검 역시 당시 수중에 넣은 수많은 고서 중 하나였다.

쉬쉬쉬슁!

열두 갈래의 그물이 펼쳐져 사방 십여 미터를 뒤덮는다.

붉은 오러의 그물이 피부와 살을 가르고 뼈를 잘랐다. 수십여 마리의 상위 몬스터가 조각나며 허물어졌다.

실로 S급 헌터다운 무위. 잔뜩 고무된 우헤이싱이 소리쳤다.

「홍위방(紅衛幇)은 뭘 하고 있나! 전부 쓸어 버려라, 이 개자식들아!」

「옛!」

강렬한 마나가 실린 외침이 전장을 뒤흔들었다.

우헤이싱의 가문에서 직접 창설하고 사병으로 육성시킨 삼백여 명의 정예 헌터들은 망설임 없이 빈틈을 비집고 달려들었다.

쉬쉬쉬쉭! 퍼걱!

쐐액! 서걱!

- 크륵, 커흐윽!

「으아아악!」

사방에서 인간과 몬스터의 비명, 핏물이 뒤섞였다.

우헤이싱이 마지막까지 아껴 둔 홍위방의 헌터들은 분명 강자들이었지만, 그들의 적 역시 상위에 속하는 몬스터였다.

후방에 배치되어 있던 정예 몬스터들은 짙은 안개 사이를 누비며 헌터들을 상대했다. 수준을 떠나 서너 배에 달하는 머릿수.

그러나…….

「이 더럽고 냄새나는 놈들이 감히!」

푸푸푸푹!

우헤이싱이라는 S급 헌터의 존재는 불리한 전황을 뒤집기에 충분했다.

비록 방탕한 행실과 성격으로 인해 많은 비난을 받는다고는 하나, 그는 최고의 환경에서 성장한 한 사람의 천재였다.

게다가 우헤이싱은 처음 전선에 투입되었을 때와는 달리 더욱 노련해졌고, 죽음이 난무하는 전장을 겪으며 실력 역시 진일보한 상태였다.

‘할 수 있다! 나는 우헤이싱이다!’

우헤이싱은 가슴 깊숙한 곳에서 솟구치는 고양감을 느끼며 쉴 새 없이 검을 휘둘렀다.

상대는 수만에 달하는 몬스터 군단. 처음에는 두려웠으나 어느새 여기까지 왔다.

조금이라도 부상을 입거나 지치면 고가의 포션을 물처럼 들이켰고, 홍위방 헌터를 방패 삼아 몸을 빼기도 했다.

그리고 지금. 자신의 붉은 오러 블레이드를 막을 수 있는 몬스터는 없었다.

‘누구도 나를 무시 못 하게 만들어 주마. 레이페이. 빌어먹을 빵즈 놈. 그 누구도!’

우헤이싱이 치욕적인 기억을 떠올리며 이를 갈던 그 순간.

쐐애애애액! 뻐억!

눈부신 속도로 날아온 한 자루의 창이 서너 명의 헌터들을 꼬치처럼 꿰며 지면 깊숙이 틀어박혔다.

지금과 같은 전장에서는 쉽게 찾아볼 수 없는 3m 길이의 돌격창.

황급히 고개를 돌려 적을 확인한 우헤이싱이 눈을 부릅떴다.

「데스나이트(Death Knight)!」

두두두두!

해골마에 올라 전장을 가로지르는 그것은 분명 데스나이트였다. 그것도 혼자가 아닌 두 기.

새로 모습을 드러낸 또 다른 데스나이트가 마상에서 창을 치켜세웠다.

「모두 주의……!」

쐐애애애액! 뻐엉!

경고를 내뱉기도 전에 허공을 찢으며 쏘아진 두 번째 돌격창이 한데 뭉쳐 있던 헌터 예닐곱을 관통했다.

최고급 갑옷으로도 막을 수 없는 일격에 팔다리가 솟구치고 상반신을 잃은 몸뚱어리가 털썩 쓰러진다.

난데없는 데스나이트의 등장. 이어 자신들의 눈앞에서 펼쳐진 끔찍한 광경에 홍위방의 헌터들이 굳어 버린 그때였다.

- 다.크. 바.인.(Dark Vine)!

쇠로 긁는 듯한 음산한 목소리가 퍼져나감과 동시에, 변화가 시작되었다.

쩌쩍, 콰드드드득!

단단하던 지면이 거미줄처럼 갈라지고, 그 사이로부터 검은 넝쿨이 솟구쳤다.

마력을 머금은 그것은 살아 있는 생물처럼 움직이며 인간의 팔과 다리를 붙잡거나, 혹은 갑옷으로 가리지 못한 빈틈을 파고들며 꿰뚫었다.

쉬리리릭! 푸푸푹!

「크아아아악!」

「흑마법! 흑마법이다!」

「당황하지 말고 넝쿨을 끊어라! 당장 범위에서 벗어나!」

곳곳에서 울려 퍼지는 비명과 외침.

우두둑. 몸을 휘감아 오는 검은 넝쿨을 파 뿌리처럼 뽑아 내팽개친 우헤이싱은 입술을 질끈 깨물었다.

휘하 헌터들의 죽음 때문이 아니라, 지금과 같은 일련의 상황이 무엇을 뜻하는지 알기 때문이었다.

「리치(Lich)……!」

우헤이싱의 짐작은 정확했다. 모두의 머리 위, 잿빛 하늘을 배회하는 거대한 와이번의 머리에 올라탄 죽음의 마법사가 해골과 뼈로 이루어진 스태프를 들어 지상을 가리켰다.

- 컨.퓨.징(Confusing)!

스아아아!

음산한 외침과 함께 먹구름처럼 쏟아져 내린 마력이 일대를 뒤엎었다.

검은 넝쿨에서 빠져나오기 위해 고군분투하던 헌터들은 난데없이 찾아온 환각과 환청에 몸부림쳤고, 그런 그들은 주위에 도사린 몬스터의 손쉬운 먹잇감이었다.

- 취이이익!

- 그워어어어!

퍼걱! 콰드드득!

「크륵, 컥!」

「사, 살려 줘!」

「어머니! 돌아가시면 안 돼요. 어머니!」

단말마와 함께 쓰러지는 이. 죽어 가면서도 환청과 환각에서 벗어나지 못해 울부짖는 이.

하지만 그중엔 강인한 정신력으로 마법의 영향을 벗어난 이들 역시 있었다.

「가셔야 합니다!」

「도련님!」

주위를 둘러싼 A급 헌터들의 외침에도 우헤이싱의 얼굴은 백지장처럼 새하얗게 질려 있었다.

그의 뇌리에는 한 가지 물음만이 맴돌았다.

‘도대체, 도대체 어떻게 해야 하지?’

하늘에는 리치가, 지상에는 두 기의 데스나이트가 빠르게 다가오고 있는 상황.

후퇴할 수 있을까. 만일 후퇴 한다면 어디로, 어떻게 가야 하는가.

두 기의 데스나이트는 홀로 상대할 수 있겠지만, 리치의 마법과 일대를 물 샐 틈 없이 포위한 저 수많은 몬스터들은?

아무리 생각해도 해답을 찾을 수 없었다.

‘이, 이런 빌어먹을 일이…….’

으드득.

우헤이싱이 부서질 듯이 이를 갈던 찰나.

쉬이이익, 파앙!

압축된 공기가 터져 나가는 파공성와 함께, 저 멀리 지상에서 솟구친 한 줄기의 섬광이 허공을 스쳤다.

그리고 다음 순간, 머리를 잃은 와이번의 거체가 힘을 잃고 추락하기 시작했다.

「이건.」

우헤이싱이 신음처럼 중얼거렸다. 모두가 상황을 잊고 고개를 들어 하늘을 바라보았다.

그들의 시선에 서서히 속도를 더해 추락하는 와이번의 몸뚱어리와 한때 리치라 불렸던 검은 뼈 무더기가 쏟아지는 것이 보였다.

「……이건 말도 안 돼.」

리치가 죽었다. 그것도 단 일격에.

겹겹이 두른 수십 개의 방어 마법을 뚫고 공중에 있는 놈을 정확히 요격한다?

S급 헌터라 할지라도 쉽게 장담할 수 없는 일이다. 우헤이싱은 저만큼 빠르고 강력한 공격을 본 적이 없었다.

하지만 그가 아닌 또 다른 누군가에게는, 숨을 쉬는 것처럼 당연한 일이기도 했다.

전장에서 얼마 떨어지지 않은 곳에서 자신이 벌인 일을 물끄러미 바라보던 그가 문득 입을 열었다.

“투창을 하는 건 오랜만이라 그런지, 확실히 예전 같지 않군.”

그의 뒤에 철탑처럼 시립해 있던 사내가 딱딱한 어조로 대답했다.

“훌륭하셨습니다.”

“음. 아닐세. 무뎌진 것 같아. 나도 나이를 먹었다는 증거겠지.”

“그럴 리가 있겠습니까.”

평소와 같은 경호팀장의 고저 없는 목소리에 그가, 아니 이정룡이 부드럽게 웃었다.

“데스나이트가 보이던데.”

석고준이 묵묵히 고개를 끄덕였다.

“예. 총 두 기더군요.”

“우헤이싱이 막을 수 있다고 생각하나?”

“데스나이트를 말씀하시는 거라면, 어렵지 않게 쓰러트릴 수 있을 겁니다.”

그렇게 말한 석고준은 낮은 목소리로 한마디를 덧붙였다.

“주위에 몬스터만 없다면 말입니다.”

“지금으로서는 어렵다는 이야기로 들리는군.”

“흑마법의 영향이 사라졌다지만 이미 병력 피해가 상당한 반면에, 몬스터의 숫자가 너무 많습니다.”

“그렇다면 있는 힘껏 발버둥 쳐야 할 테고.”

“아주 치열하고, 힘든 싸움이 되겠지요.”

“허어, 그렇다면 도와줘야겠군.”

“조금 더 지켜보는 것이 어떻겠습니까?”

이정룡이 짐짓 눈을 크게 떴다.

“어째서?”

어릴 적부터 이정룡의 가르침을 받은 석고준은 이 모든 순간들이 스승의 시험이라는 것이 안다. 자신이 해야 하는 대답이 무엇인지도.

“위태로운 상황일수록 더 고마워하지 않겠습니까.”

제자의 대답을 들은 스승은 그제야 만족스러운 미소를 띠었다. 덩달아 말투도 바뀌었다.

“그래, 바로 그것이다.”

“전부터 홍위방은 골칫거리였지요.”

“참 웃기는 놈들이지. 인민이니, 공산주의니 부르짖는 놈들이 뒤에서는 헌터로 사병 집단을 꾸리다니.”

“하지만 홍위방을 후원하는 태자당은 저희 쪽에 우호적이지 않습니까?”

“그러니 홍위방이 없어져야 하는 것이다. 늘 나무 그늘에 앉아 햇빛을 피했는데, 나무가 뿌리 뽑혔으니 어찌하겠느냐?”

“다른 나무를 찾든가, 양산을 사야겠지요.”

“우리가 새로운 나무가 되어 줄 것이다. 그렇게 된다면 더 많은 기회가 열리겠지.”

고개를 끄덕인 석고준이 문득 입을 열었다.

“한 가지만 더 여쭤봐도 되겠습니까?”

“말하거라.”

“우헤이싱을 이번 작전에 참여시키신 이유가…… 진태경과 연관이 되어 있습니까?”

그건 석고준이 계속해서 품고 있던 의문이었다.

제아무리 S급 헌터라고는 하지만 저런 얼간이를 어째서?

‘놈은 엄청난 강자다. 설령 스승님이 우헤이싱을 이용하신다 하더라도, 어떤 쓸모가 있을까?’

간혹 그럴 때가 있다.

스승의 생각과 행동에 익숙해졌다 싶었다가도, 그의 의중을 정확히 알 수 없을 때가.

그리고 그럴 때마다 이정룡은 늘 뜻 모를 미소를 짓고는 했다.

바로 지금처럼.

“석 팀장.”

말투도, 분위기도 바뀌었다. 아레스 길드의 경호팀장으로 돌아간 석고준이 깊게 고개를 숙였다.

“예. 부길드장님.”

“자네가 나설 때가 온 것 같은데. 어찌 생각하나?”

고개를 든 석고준은 이정룡의 어깨너머로 보이는 치열한 접전을 확인했다.

엄선해서 뽑은 홍위방의 정예들은 몬스터에 의해 죽어 가고 있었고, 우헤이싱은 데스나이트 두 기 중 하나를 막 쓰러트린 찰나였다.

“이만 가 보겠습니다.”

“모쪼록 다치지 않도록 조심하게.”

짧게 고개를 숙이는 것으로 대답을 대신한 석고준은 준비되어 있던 아레스 길드원들을 이끌고 전장으로 향했다.

몬스터를 향해 돌격하는 그들은 함성을 내지르지는 않았지만, 모든 것을 압도하고도 남는 기세가 있었다.

콰드드드득! 서걱!

몬스터 군단의 한 축이 순식간에 허물어지는 광경을 기껍게 바라보던 이정룡은 문득 바람에 섞여 불어오는 피비린내를 맡았다.

서쪽으로부터 불어온 바람. 그리고 기다리던 한 사람의 등장을 알리는 신호였다.

“때맞춰 왔군.”

작게 뇌까린 이정룡은 저 멀리 지평선을 바라보았다.

기운을 끌어올리자 면도날처럼 예리해진 감각에 한 사람의 외침이 들려왔다.

- 시벌, 다 죽여! 그리고 아까부터 에에에 하는 새끼는 진짜 한 번만 더 하면 몬스터로 간주한다. 알겠냐?

낮은 웃음을 흘린 이정룡은 손을 뻗었다.

그리고 저 어딘가에 있을 진태경을 향해 손아귀를 움켜쥐었다.
```

## Final English reading copy

```markdown
# Chapter 413

*Fwoooosh! Kraaaash!*

A massive greatsword smashed into the ground. Wu Heixing’s body shot upward like lightning, having dodged the attack by the exact distance of half a span.

*Thud!*

The blade that had driven up beneath the ogre’s jaw jutted out above the crown of its head.

A precise, no-frills strike.

Wu Heixing pulled out his sword, stepped on the shoulder of the falling ogre, and dropped among the monsters.

The sword in his hand traced countless lines through the air.

*The Twelve Blood Net Sword.*

Some people had condemned the Cultural Revolution that lasted from 1966 to 1976 as an atrocity that outraged both heaven and humanity. To someone else, however, it had been the opportunity of a lifetime.

Wu Heixing’s grandfather, a longtime political companion of Mao Zedong, had risen spectacularly and embezzled an astronomical fortune. Using his son—a member of the Red Guards—as a stepping stone, he had smuggled away all kinds of cultural artifacts and ancient books.[^1]

The Twelve Blood Net Sword Wu Heixing had learned was one of the countless ancient books his grandfather had acquired at the time.

*Shreeeeek!*

Twelve strands of a net spread out, covering more than ten meters in every direction.

The net of red aura sliced through skin and flesh, cutting bones apart. Dozens of high-tier monsters were shredded and collapsed.

It was truly the prowess of an S-rank Hunter.

Thoroughly emboldened, Wu Heixing shouted.

“Red Guard Gang! What are you doing? Sweep them all away, you bastards!”

“Yes, sir!”

A shout infused with powerful mana shook the battlefield.

The roughly three hundred elite Hunters of the Red Guard Gang, which Wu Heixing’s family had personally founded and raised as a private army, charged into every opening without hesitation.

*Shreeeek! Splurt!*

*Whoosh! Slash!*

—Krrk, khrrrk!

“Aaaaargh!”

The screams of humans and monsters mingled with splashing blood from every direction.

The Red Guard Gang’s Hunters, whom Wu Heixing had kept in reserve until the very end, were unquestionably strong. But their enemies were high-tier monsters as well.

The elite monsters positioned in the rear darted through the thick fog as they fought the Hunters. Regardless of the difference in level, the monsters outnumbered them three or four to one.

And yet…

“You filthy, stinking bastards dare!”

*Stab-stab-stab!*

The existence of an S-rank Hunter named Wu Heixing was enough to turn the unfavorable situation around.

He might have been widely criticized for his debauched behavior and personality, but he was still a genius who had grown up in the best possible environment.

Besides, unlike when he had first been deployed to the front lines, Wu Heixing had become more experienced. After passing through battlefields where death ran rampant, his skills had advanced by another step.

*I can do this! I’m Wu Heixing!*

Feeling exhilaration surge from the depths of his chest, Wu Heixing swung his sword without pause.

His opponents were a monster army numbering in the tens of thousands. He had been afraid at first, but somehow he had made it this far.

Whenever he suffered even a minor injury or began to tire, he gulped down expensive potions like water. He also used the Red Guard Gang’s Hunters as shields when he needed to pull back.

And now, there was no monster capable of blocking his red aura blade.

*I’ll make sure no one can ever look down on me again. Lei Fei. That fucking bangzi bastard. No one!*

That was the moment Wu Heixing ground his teeth at the humiliating memory.

*Fwoooooosh! Boom!*

A spear flew in at blinding speed, skewering three or four Hunters like meat on a skewer before burying itself deep in the ground.

A three-meter-long lance—something rarely seen on a battlefield like this.

Wu Heixing hurriedly turned his head to identify the enemy, then his eyes flew wide.

“Death Knight!”

*Thud-thud-thud-thud!*

The figure riding a skeletal horse and cutting across the battlefield was unmistakably a Death Knight.

And there were two of them, not one.

The other Death Knight that had just appeared raised its lance from horseback.

“Everyone, watch—!”

*Fwoooooosh! Boom!*

Before he could finish his warning, the second lance tore through the air and pierced six or seven Hunters clustered together.

It was a strike that even the finest armor could not stop. Arms and legs flew through the air, while bodies that had lost their upper halves collapsed with a thud.

The sudden appearance of the Death Knights.

Then, as the Red Guard Gang’s Hunters froze at the horrifying sight unfolding before their eyes—

—D-a-r-k. V-i-n-e!

A gloomy voice, scraping like metal, rang out. At the same time, the changes began.

*Crack! Kra-d-d-d-d-k!*

The solid ground split apart like a spiderweb, and black vines surged up through the cracks.

Filled with magical power, they moved like living creatures. Some seized human arms and legs, while others wormed through gaps left exposed by armor and pierced their victims.

*Shrrrrk! Stab-stab!*

“Kyaaaaargh!”

“Black magic! It’s black magic!”

“Don’t panic! Cut the vines! Get out of the area now!”

Screams and shouts rang out everywhere.

*Crack.*

Wu Heixing bit down hard on his lip as he tore up the black vines winding around his body and flung them away like roots.

It was not because his Hunters were dying.

He understood what this entire series of events meant.

“Lich…!”

Wu Heixing’s guess was correct.

High above their heads, a death mage riding atop the head of a giant Wyvern that prowled through the gray sky raised a staff made of skulls and bones and pointed it at the ground.

—C-o-n-f-u-s-i-n-g!

*Whoooooosh!*

With the eerie cry, magical power poured down like dark storm clouds and swallowed the entire area.

The Hunters struggling to escape the black vines suddenly writhed as hallucinations and phantom voices seized them. They became easy prey for the monsters lurking around them.

—Sssssss!

—Gwoooooar!

*Smash! Kra-d-d-d-d-k!*

“Krrk, khk!”

“P-Please, save me!”

“Mother! You can’t die, Mother!”

Some fell with a final scream.

Others continued to howl even as they died, unable to escape the hallucinations and phantom voices.

But there were also those who broke free of the spell through sheer mental strength.

“You have to go!”

“Young Master!”

Despite the shouts of the A-rank Hunters surrounding him, Wu Heixing’s face had gone as pale as a sheet of paper.

Only one question circled through his mind.

*What—what the hell am I supposed to do?*

The Lich was in the sky, while two Death Knights were rapidly approaching from the ground.

Could they retreat?

If they did, where would they go, and how?

Wu Heixing might have been able to face the two Death Knights alone, but what about the Lich’s magic and the countless monsters surrounding the area so tightly that not even water could pass through?

No matter how much he thought about it, he could not find an answer.

*This…this fucking situation…*

*Crack.*

Wu Heixing was grinding his teeth hard enough to break them when—

*Fwoooosh! Bang!*

Along with the sharp crack of compressed air bursting apart, a streak of light shot up from the distant ground and sliced through the sky.

The next moment, the massive body of the Wyvern began to fall, robbed of its head.

“This…”

Wu Heixing muttered the word like a groan.

Everyone forgot the situation around them and looked up at the sky.

Before their eyes, the Wyvern’s body plummeted faster and faster, while a heap of black bones—the being that had once been called a Lich—tumbled down after it.

“…This is impossible.”

The Lich was dead.

And it had died in a single strike.

Someone had pierced through dozens of layers of defensive magic and accurately intercepted a target in midair?

Even an S-rank Hunter could not easily guarantee such a feat.

Wu Heixing had never seen an attack so fast or so powerful.

But to someone else, it was as natural as breathing.

The man who had been quietly watching what he had done from a short distance away suddenly opened his mouth.

“It has been a long time since I threw a spear. I’m definitely not as good as I used to be.”

The man standing behind him like an iron tower answered in a stiff tone.

“You were magnificent.”

“Hmm. No, I wasn’t. I seem to have gotten rusty. I suppose it’s proof that I’ve grown older.”

“How could that be?”

At the Head of Security’s usual flat voice, the man—Lee Jungryong—smiled gently.

“I saw Death Knights.”

Go Jun silently nodded.

“Yes. Two of them in total.”

“Do you think Wu Heixing can stop them?”

“If you mean the Death Knights, he should be able to defeat them without much difficulty.”

Go Jun added in a low voice.

“If there were no monsters around them.”

“So you mean it would be difficult under the current circumstances.”

“The black magic’s influence has disappeared, but the Hunters have already suffered considerable losses, while the monsters are far too numerous.”

“Then they’ll have to struggle with all they’ve got.”

“It will be a fierce and difficult battle.”

“Oh my. Then I suppose we should help them.”

“Would it not be better to watch a little longer?”

Lee Jungryong deliberately widened his eyes.

“Why?”

Go Jun had been taught by Lee Jungryong since childhood. He knew that every one of these moments was a test from his Master.

He also knew what answer he was supposed to give.

“Would they not be more grateful if we helped them when the situation was more precarious?”

Only then, after hearing his Disciple’s answer, did the Master smile in satisfaction. His manner of speaking changed as well.

“Yes. Exactly.”

“The Red Guard Gang has been a nuisance for some time.”

“They’re amusing fellows. They shout about the people and communism, then form a private army out of Hunters behind the scenes.”

“But the Crown Prince Party, which supports the Red Guard Gang, is friendly toward us.”

“That is why the Red Guard Gang must disappear. They have always sat beneath a tree’s shade to avoid the sunlight. Now that the tree has been uprooted, what else can they do?”

“Find another tree or buy a parasol.”

“We will become their new tree. If that happens, even more opportunities will open up.”

Go Jun nodded, then suddenly spoke.

“May I ask one more thing?”

“Go ahead.”

“The reason you had Wu Heixing participate in this operation… Is it related to Jin Taekyung?”

It was a question Go Jun had continued to harbor.

Even if Wu Heixing was an S-rank Hunter, why bring along an idiot like him?

*That man is immensely powerful. Even if Master is using Wu Heixing, what use could he possibly be?*

Sometimes, this happened.

Just when Go Jun thought he had grown accustomed to his Master’s thoughts and actions, he would find himself unable to understand Lee Jungryong’s true intentions.

And whenever that happened, Lee Jungryong would always wear an inscrutable smile.

Just like now.

“Team Leader Seok.”

His tone and the atmosphere both changed.

Returning to his position as the Head of Security for Ares Guild, Go Jun bowed deeply.

“Yes, Vice Guild Master.”

“It seems the time has come for you to step in. What do you think?”

Go Jun raised his head and looked past Lee Jungryong’s shoulder at the fierce battle.

The carefully selected elite Hunters of the Red Guard Gang were being killed by monsters, while Wu Heixing had just defeated one of the two Death Knights.

“I’ll be going.”

“Be careful not to get hurt.”

Go Jun answered with a brief bow and led the waiting Ares Guild members toward the battlefield.

They did not shout as they charged the monsters, but the force they radiated was more than enough to overwhelm everything before them.

*Kra-d-d-d-d-k! Slash!*

Lee Jungryong watched with satisfaction as one flank of the monster army collapsed in an instant.

Then he suddenly caught the smell of blood carried on the wind.

A wind blowing from the west.

A signal announcing the arrival of the person he had been waiting for.

“He arrived right on time.”

Lee Jungryong muttered under his breath and looked toward the distant horizon.

As he raised his qi, his senses sharpened like a razor, and he heard a man shouting.

—Fuck, kill them all! And that bastard who’s been going “Eeeeeeh” this whole time—if he does it one more time, I’m counting him as a monster. Got it?

Lee Jungryong let out a low chuckle and stretched out his hand.

Then he clenched his fist toward Jin Taekyung, who was somewhere out there.

[^1]: The Red Guards were radical youth organizations active during China’s Cultural Revolution.
```

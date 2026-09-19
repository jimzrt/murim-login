<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0441.txt",
      "sha256": "0abf46a1904f8e54b1dd9a75d4c3588b5e4f8d821776b7fcb9b67e82d16b50ef",
      "bytes": 14172
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "682225f2dfa56ca681b9163fdb83698ba1cdf5f4b92d4fdd34ece810e0d9759a",
      "bytes": 1941
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "6613790e0d9d9ccbe774b66d802873da8a449fcbf8a7a07ab85e8417137e41ad",
      "bytes": 144265
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "b882a526608630f2991c231aae4287fc81d0c9c27d88bfe8aa5296e911ced465",
      "bytes": 944
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "5a3e28e9b1b710c7c439bb865a7c00dce43b12263b5d3f303b54baa6522f536d",
      "bytes": 553
    },
    {
      "path": "characters/Go Jun.md",
      "sha256": "1a9353a1e1362e05f5fc41ee9e05ab2cefd832e23f295f72ac1fe73eed8e3e71",
      "bytes": 800
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "05e6ff6558167a4e92ba1278c9e05fdfef03ff0d9ff2468f2de9c4d701b6f118",
      "bytes": 1390
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "c02a08d760f0fdcff382da152a76cc4d6ad82eae4c7d386f06cb75193a5b2abd",
      "bytes": 1526
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "f2143ad2c81489f5ddac2bfefb30c2a335e710efe1e44806ed0e9b09508c4a43",
      "bytes": 622
    },
    {
      "path": "characters/Lee Jungryong.md",
      "sha256": "69a8b330408e211db6ac21255ab00a51cb8b20ff3616bbee9d570c360c92b190",
      "bytes": 1182
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "a06c0053d33c8642fd03ec11d68588fe175db816d2d8ed26f14a8493d7527c5b",
      "bytes": 138548
    }
  ],
  "estimated_tokens": 11835
}
-->

# Durable State Update — Chapter 441

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 441. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 441. Profile updates may replace only one
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
  "chapter": 441,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 441,
    "continuity_sources": [441],
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
    "Jin Taekyung has returned to Korea and received a globally broadcast welcome and car parade at Incheon attended by hundreds of thousands.",
    "Taekyung's public image now includes the nicknames King Taekyung, Lord Fuck, and Lord Sibu-leol.",
    "Taekyung's family was present for his return, and he is resolved to protect them from the dangers he has faced.",
    "Taekyung and Team Leader Choi have reaffirmed their ongoing cooperation and mutual support.",
    "The Skeleton King's undead identity remains concealed from the public, and he was hidden in Inventory during the parade.",
    "Taekyung has ordered the Skeleton King to join Peace Guild under an already prepared contract.",
    "Magic Johnson has publicly announced that he is pursuing an agreement with Peace Guild.",
    "Go Jun remains alive and is consumed by hatred and fear after seeing Taekyung's name; an interrupted report is pending."
  ],
  "continuity_sources": [
    440
  ],
  "open_questions": [
    "Why does Mungyeong continue accompanying Jin Taekyung's group despite being unable to explain the impulse?",
    "How did Jin Taekyung actually open his Middle Dantian?",
    "What confidential matter is Jin Wikyung withholding?",
    "Are Taekyung's suspicions about the mysterious patterns and symbols found in both worlds correct?",
    "What agreement is Magic Johnson pursuing with Peace Guild, and what report is about to reach Go Jun?"
  ],
  "safe_through": 440,
  "temporary_decisions": [
    "Render 시부럴 as “sibu-leol,” 시벌좌 as “Lord Fuck,” and 시부럴좌 as “Lord Sibu-leol.”",
    "Preserve the Skeleton King's grandiose, mock-offended voice and Taekyung's dry, profane humor.",
    "Render 최 팀장님 as “Team Leader Choi” and 진태경 씨 as “Mr. Jin Taekyung.”",
    "Keep Peace Guild, guild house, Inventory, and Magic Johnson as established terms."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 청풍     | **Cheongpung**     |
| 이정룡    | **Lee Jungryong** |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 상태               | **Status**                     |
| 헌터      | **Hunter**            |
| 길드      | **Guild**             |
| 길드장     | **Guild Master**      |
| 팀장      | **Team Leader**       |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 고준 | **Go Jun** | Personal name of Team Leader Seok; Lee Jungryong's prized Disciple. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 평화 | **Peace Guild** | Guild name. |
| 아레스 | **Ares Guild** | The leading Guild in Korea; formerly employed Team Leader Choi and Song Song. |
| 화시 | **fire arrow** | Flaming arrow Lee Seowol fires to signal Cheol Mubaek. |
| 태자 | **Crown Prince** | Title of the Emperor's older brother who was reportedly assassinated. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 선장 | **Zen staffs** | Staff weapons carried by the Hundred and Eight Arhats. |
| 노야 | **Old Master** | Taekyung's private address for Jeok Cheongang. |
| 준이 | **Jun** | Family nickname used in the form Jun's dad. |
| 석고준 | **Go Jun** | Source full-name form for the established Go Jun, also known as Team Leader Seok. |
| 경호팀장 | **Head of Security** | Go Jun's security-team office under Lee Jungryong. |
| 중국 | **China** | Country from which Team Leader Choi’s video originates. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 쓰촨성 | **Sichuan Province** | Source spelling variant of the established Sichuan location. |
| 수룡채 | **Water Dragon Stronghold** | Major river stronghold belonging to the Yangtze River Channel League. |
| 장강 | **Yangtze** | The river controlled by the Yangtze River Channel League. |
| 태자당 | **Crown Prince Party** | The faction associated with General Liao. |
| 중단전 | **Middle Dantian** | Martial energy center opened by Jin during the battle. |
| 쓰촨 | **Sichuan** | Variant spelling used for the region associated with the pattern Jin recognizes. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 청풍 | 진태경 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung repeatedly addresses Taekyung as 은인 after receiving food. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 관리 | 진태경 | official_to_young_martial_artist | Young Master | formal-polite | The official addresses Taekyung as 공자 while explaining the consequences of Prince Shangshan's displeasure. |
| 진태경 | 청풍 | companion_to_young_martial_artist | Young Master Cheongpung | formal-polite | Taekyung uses 청 공자 while correcting Cheongpung's royal-etiquette mistake. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 적천강 | 청풍 | overwhelming_elder_to_young_martial_artist | you / little punk | blunt, amused, and threatening | Jeok Cheongang uses 네, 이놈, and related blunt forms while testing Cheongpung. |
| 청풍 | 적천강 | young_martial_artist_to_overwhelming_elder | Grandpa Jeok | casual-familiar despite deference | Cheongpung uses 적 할아버지 while asking Jeok Cheongang to confirm Taekyung's condition; this is a familial form of address, not literal kinship. |
| 이정룡 | 진태경 | senior S-rank Hunter to younger Hunter and adversary | Young man | polished, teasing, and veiled-threatening | Uses a genial tone and indirect threats while trying to make Taekyung release the captives. |
| 진태경 | 이정룡 | younger Hunter to senior S-rank Hunter and adversary | you | polite but mocking and defiant | Taekyung answers Lee's soft threats with the wolf-and-tiger metaphor and refuses to yield. |
| 이정룡 | 고준 | Master to Disciple | Go Jun | familiar and testing | Lee switches from Seok's office title to his personal name while considering whether he can defeat Taekyung. |
| 고준 | 이정룡 | Disciple to Master | Master | deferential | Go Jun responds to Lee's personal-name address as 스승님. |
| 진태경 | 석고준 | returning Hunter to hostile Ares security leader | you fucking bastard | hostile and profane | Taekyung directs his final insults and challenge at Go Jun after returning alive. |
| 석고준 | 진태경 | hostile_opponents | brat | hostile and overconfident | Go Jun addresses Taekyung internally as 애송아 while launching his full-strength attack. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 고준 | 진태경 | Ares Guild combatant confronting the killer of his Master | you | hostile and informal | Go Jun uses 너 while demanding Jin confess to Lee Jungryong's death and threatening retaliation. |
| 진태경 | 고준 | dominant adversary confronting Lee Jungryong's Disciple | you | contemptuous and informal | Jin uses 너 and 놈 while overpowering Go Jun and ordering him to end the conflict with Lee Jungryong. |

## Listed compact profiles

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 436
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, the grandson and Disciple of Sword Saint Mae Jonghak, and a Supreme Peak martial master known as the Huashan Divine Dragon.
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, a deep love of martial arts, and a martial artist's competitive pride; he becomes unsettled when someone copies his martial arts
- **Voice:** Dreamy and hazy, with innocent, polite phrasing
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions while Taekyung is his only true martial rival; Tang Sadok has temporarily entrusted Mimi to him.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 440
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Go Jun.md

# Go Jun (고준)

- **Safe through:** Chapter 440
- **Aliases:** Team Leader Seok
- **Role:** Leader of Lee Jungryong's security team, an Ares Guild combatant, and Lee's disciple and right-hand man who remains alive after Jin Taekyung grievously mutilated him.
- **Personality:** Highly disciplined, fiercely loyal to Lee Jungryong, confident in his abilities, and capable of suppressing his anger and killing intent under provocation.
- **Voice:** Dry, controlled, and formal with subordinates; deferential when addressing his Master.
- **Relationships:** Disciple and direct protégé of the late Lee Jungryong, Go Jun confronted Jin Taekyung over Lee's death and was forced to accept Jin's demand that the conflict end with Lee.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 438
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is a legendary wandering martial master and Jin Taekyung's Master.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, and casually threatening or violent when dissatisfied. His meeting with Taekyung rekindled his will to live, making him determined to extend his life despite his illness.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 440
- **Aliases:** Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, a Supreme Peak master who has manifested Force, opened his Middle Dantian, crossed the wall into true mastery, can perceive the texture of qi well enough to sever layered magic, and is Korea's publicly recognized representative S-rank Hunter.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate, student, and trusted manager of media and official arrangements, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, and Xiao Shen regards him as an older brother after Jin saved him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 440
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Lee Jungryong.md

# Lee Jungryong (이정룡)

- **Safe through:** Chapter 432
- **Aliases:** None
- **Role:** Former Vice Guild Master of Ares Guild, one of Korea's two S-rank Hunters, and a Supreme Peak-level martial artist who was killed by Jin Taekyung.
- **Personality:** Outwardly genial, calm, and humorous; calculating, opportunistic, manipulative, coercive, and ruthless when challenged
- **Voice:** Smooth, good-natured, and indirect, using teasing conversation and veiled threats before becoming openly furious
- **Relationships:** Master of Park Jihoon and Go Jun (Team Leader Seok), whom he personally selected and trained; longtime Great Cataclysm acquaintance of Park Tae Seop; adversary of Jin Taekyung; knew Team Leader Choi from childhood; has an antagonistic history with Kim Hwajong, who saved his life at the collapse of Mapo Bridge eighteen years earlier; was visibly shaken by learning that Choi is Cheon Taemin's maternal grandson; regards Cheon Taemin as an older brother despite no blood relation and has long held him in respect and fear; operates as Ares Guild's senior authority beneath its Guild Master

## Korean source

```text
＃441화



“티, 팀장님. 잠시 들어가도 되겠습니까?”

바짝 긴장한 목소리.

붉게 충혈된 눈동자로 문을 노려보던 석고준이 손을 뻗었다.

콰득!

허공을 격하며 쏘아진 강대한 기운이 철문을 종잇장처럼 찢고 우그러트린다.

그 엄청난 광경을 코앞에서 목격한 경호팀 소속 직원은 헛숨을 삼켰다.

“흡.”

“아무도 접근하지 말라고 했을 텐데.”

석고준의 붉은 안광과 정면으로 마주한 팀원은 순간 등골이 쭈뼛 섰다.

늘 기계처럼 정확하고 냉철하던 직속 상관의 극단적인 변화는 동료들의 이야기를 들어 알고 있었지만, 이렇게 마주하니 자신도 모르게 두려움으로 목소리가 떨렸다.

“그, 그게. 보고드릴 일이 있어서…….”

“미뤄.”

심연 깊숙한 곳에서 끌어올린 것처럼 낮은 목소리.

팀원도 당연히 그러고 싶었지만, 별것 아닌 일이었다면 제비뽑기로 보고자를 정할 일도 없었을 것이다.

마른침을 삼킨 그가 용기를 쥐어 짜내어 말했다.

“조사단장에게 급하게 연락이 왔습니다. 정체를 알 수 없는 이상한 물건을 발견했다고…….”

거칠게 돌아서려던 석고준의 신형이 우뚝 멈췄다.

“이상한 물건?”

“예. 팀장님.”

“혹시.”

“아, 아닙니다.”

불똥이 튈까 염려한 팀원이 황급히 말을 이었다.

“확인해 본 결과 고인이신 부 길드장님의 유품은 아직 어떤 것도 발견되지 않았습니다.”

“확실해?”

“예. 현장에 파견된 팀원들이 빼돌릴 것을 염려해 수시로 감시 중이니 확실합니다.”

“그래서?”

“예, 예?”

“내가 그놈들에게 받아야 할 보고는 하나뿐이다. 필요로 하는 것을 찾았다는 보고.”

석고준의 눈빛이 컴컴하게 가라앉았다.

아레스 길드와 밀접한 관계를 맺고 있던 태자당이 내리막길을 걷고 있는 지금에도 아레스 길드의 영향력과 힘은 유효했다.

책임자가 바뀌고, 정권이 교체되어도 사람이라면 누구나 가지고 있는 탐욕(貪慾)은 사라지지 않으니까.

꼿꼿한 대나무도 무게를 이기지 못하면 휘어지는 법. 석고준은 수백억이 넘는 돈으로 그 무게를 만들었다.

현재 아크 리치의 본거지였던 도시를 관리하는 조사단장과 주요 간부들도 다르지 않았다.

“그놈들한테 전해. 무슨 수를 써서라도 반드시 찾아내라고. 그전까지는 어떤 연락도 하지 말라고.”

이 세상에 대가 없는 호의는 존재하지 않는다. 석고준은 그들을 거금을 들여 매수했고, 원하는 것을 얻지 못한다면 그에 상응하는 보복을 가할 생각이었다.

그만큼 석고준이 찾고자 하는 물건은 중요한 것이었다.

아버지처럼 따르던 스승의 유품이기 때문만은 아니다. 그것은 누군가를 빠져나올 수 없는 궁지로 몰아넣을 수 있는 강력한 무기도 될 수 있다.

‘홀로그램 녹화기.’

이정룡은 엄청난 영향력을 지닌 아레스 길드의 실질적인 주인이었고, 혹시 모를 상황을 대비하여 늘 소형 홀로그램 녹화기를 몸에 지니고 다녔다.

그리고 그것은 진태경에 의해 죽음을 맞이한 그 날도 마찬가지였다.

‘그 안에 모든 증거가 있다. 그것만 찾는다면, 그 후에는…….’

바로 그 순간, 이글거리던 석고준의 안광이 거세게 요동쳤다.

‘그 후에는. 어떻게 해야 하지?’

어느새 더없이 증오스러우면서도 두려워 마지않는 한 사람의 얼굴이 눈앞을 스치고 있었다.

‘……진태경.’

이름을 생각하는 것만으로도 가슴이 내려앉고 손과 발이 파르르 떨린다.

희미한 달빛 아래에서 자신을 내려다보던 무심한 눈빛과 건조한 목소리가 환영처럼 눈과 귀를 가렸다.



‘마지막으로 말한다.’



지금껏 상상할 수도 없던 고통으로 울부짖던 석고준의 귓가를 파고든 목소리.



‘이정룡 한 사람으로 끝내. 이빨 감추고, 발톱 집어넣어. 그렇게 한다면…… 아무 일도 일어나지 않는다.’



전신의 뼈가 성냥개비처럼 으스러지고 생살이 쥐어짜듯이 뜯겨나갔다. 제대로 무기를 휘둘러보지도 못한 채 끝없는 고통의 늪에서 발버둥 쳐야 했다.

이정룡이 넘을 수 없던 벽이자 존경하는 스승이었다면, 진태경은 지금껏 누구도 본 적 없던 무언가였다.

아니, 그건 마치…….

“괴물.”

석고준이 자신도 모르게 토해 낸 한마디에는 그가 느끼는 감정과 두려움이 고스란히 배어 있었다.

그리고 다음 순간, 정신을 차린 석고준은 깨달았다.

진태경을 향한 자신의 증오는 그가 품은 공포에 비하면 아무것도 아니란 것을.

진태경의 존재는 석고준의 영혼에 영원한 화인(火印)처럼 새겨진 두려움 그 자체였고, 동시에 그가 난생처음 느낀 완벽한 무력감의 다른 이름이었다.

“티, 팀장님?”

석고준은 팀원의 부름에 대답하지 않았다. 이를 악문 채 고개를 떨군 그의 시선에, 부들부들 떨리는 자신의 손이 들어왔다.

‘이, 이런 개 같은 일이…….’

으득.

피가 나도록 입술을 깨문 석고준이 고개를 들었다. 겁에 질린 상관의 모습에 당황한 팀원의 시선을 애써 무시하며 입을 열었다.

“조사단장한테 전해. 그 빌어먹을 이상한 물건을 가져오라고. 뭔지는 몰라도 직접 확인은 해 봐야겠지.”

“하지만 조금 전에는 팀장님께서…… 아, 알겠습니다.”

실수를 깨달은 팀원은 황급히 묵례를 취하고 방을 빠져나왔다.

복도를 한참이나 지난 뒤에야 참았던 숨을 토해 낸 그가 대기하고 있던 호텔 직원들에게 손짓했다.

「잠깐. 여기서 기다렸다가 진정 되시면 그때 들어가. 아, 새로운 방은 준비됐지?」

중국인으로 이루어진 호텔 직원들이 담담한 표정으로 고개를 끄덕였다.

석고준이 난동을 피우는 일은 이번이 처음이 아니었다. 이미 지난 일주일 사이에도 몇 번씩이나 있었다.

하지만 무엇이 문제인가.

며칠 전만 해도 쓰촨성 지역 유지의 소유였던 이 호텔을 아레스 길드가 사들인 뒤부터 눈앞에 있는 한국인들이 바로 자신들의 새로운 고용주였다.

비밀 유지를 위해 근무 외 수당을 잔뜩 안겨 주기도 하는, 그야말로 최고의 고용주.

「더 이상 말하기도 입 아프네. 어차피 다 아는 처지니까, 잘합시다.」

두툼한 봉투를 툭 던진 팀원은 이마에 맺힌 땀을 훔치며 자리를 떠났다.

아직도 이 지긋지긋한 중국 땅을 벗어나지 못하는 것도 문제지만, 이정룡의 뒤를 이어 아레스 길드의 새로운 선장이 될 석고준의 불안한 모습이 자꾸 눈에 밟혔다.

‘설마…… 그 소문이 사실이었나?’

그는 경호팀 내부에서도 은밀히 떠도는 어떤 이야기를 떠올렸다. 그리고 동요하는 자신의 마음도.

‘최고의 대우를 받고 있긴 하지만, 팀장님이 앞으로도 계속 저런 상태라면…….’

석고준이 경호팀장이라면 문제가 되지 않는다. 아레스 길드라는 거대한 전함은 조타수 한 명이 실수한다고 해서 넘어질 만큼 나약하지 않으니까.

하지만…… 그것이 새로운 선장이라면 이야기가 달라진다.

‘제기랄. 이런 걱정을 한 적이 없었는데.’

마음속으로 중얼거린 팀원은 정장 안감에서 스마트폰을 꺼냈다. 아무 기록도 남지 않고 추적도 불가능한 업무용 스마트폰이다.

길게 이어진 신호음 끝에 한 사람이 전화를 받았다.

- 아, 박 선생. 기다리고 있었소.

「본론부터 말씀드리겠습니다. 말씀하신 그 물건, 우리 팀장님께서 직접 보기를 원하십니다.」

- 직접 말이오?

「예, 직접. 지금 팀장님께서는 최대한 사람들의 시선을 피하고 싶어 하시니까, 무슨 말씀을 드리는지 아시겠죠?」

통화의 수신인, 조사단장이 헛기침을 흘렸다.

- 크흠, 그건 좀 곤란할 것 같소만. 아무래도 아크 리치의 본거지다 보니 유엔 측에서 파견된 외부인원들도 있고, 생각 이상으로 보안이 삼엄해서…….

「원하는 액수를 부르십시오. 단, 한 치의 실수도 없어야 합니다.」

잠시 후, 통화를 끝낸 팀원은 작게 혀를 찼다.

“염병할 놈들. 욕심만 많아서. 하긴, 그래서 잘된 건가?”

역시 세상은 쉽게 변하지 않는다. 막대한 돈과 권력 앞에서 불가능이라는 단어는 의미가 없다.

그는 아레스 길드의 경호팀에 들어온 이래 불가능을 가능케 만드는 상황을 수없이 목격했다.

그리고 이 철옹성 같은 힘은 자연스럽게 한 사람이 물려받을 것이다.

‘석고준 팀장.’

아레스 길드의 새로운 선장.

자신은 수많은 노잡이 중 한 사람에 불과하지만 석고준은 다르다. 생각이 여기에까지 이르자 그는 문득 궁금해졌다.

석고준이 그토록 두려워하는 한 사람에 대해서.

‘진태경.’

사람의 입은 완전히 막을 수 없다.

일주일 전의 어느 날, 석고준을 따라 비밀리에 자리를 비웠던 세 명의 헌터가 입을 열었던 것이 소문의 시작이었다.

아직은 최측근이라 할 수 있는 경호팀 내에서도 극소수만이 아는 사실이지만, 곧 전염병처럼 퍼져 나갈 것이다.

‘그게 사실이라면…… 후우, 일 한번 더럽게 꼬였군.’

크게 심호흡한 팀원은 눈에 힘을 줬다.

지금부터 수없이 고민하고 선택해야 한다. 현재의 배에 남을지, 새로운 배로 떠날지.

누구의 적도 되기 싫다면 아예 이 바닥을 뜨는 수밖에 없다.

‘정신 바짝 차려야지. 그래.’

지금 당장은 우선 조사단장이 빼돌린 물건을 가져오는 것이 먼저다.

상대와의 접선을 위해 약속한 장소로 이동하던 그는 문득 진태경이 부러워졌다.

‘젠장. 나도 그놈처럼 50조가 있었다면 당장 유럽으로 건너가서 왕족처럼 사는 건데.’

그 역시 몇 채의 건물을 소유한 부자지만, 사람의 욕심은 쉽게 채워지지 않는다.

고급 외제차를 가지면 고급 요트와 헬기, 그다음은 자신만의 전용기를 사고 싶어지는 것처럼.

팀원은 부러움에 입맛을 다셨다.

‘진태경 그 인간은 지금쯤 뭘 하고 있으려나. 플레이보이 모델들과 호화 요트 파티?’



* * *



강렬한 햇빛 아래, 잘 그을린 구릿빛 근육이 꿈틀거렸다.

그들의 정체는 세계 각국에서 나와 함께 선상 파티를 즐기기 위해 모인 미녀 모델들…….

“하나, 둘!”

“어이 차!”

……이 아니라 수룡채의 수적들이다.

나는 서글픈 시선으로 바쁘게 움직이는 근육몬들을 바라보았다.

‘선상 파티는 무슨.’

그런 건 인터넷에서만 봤고, 앞으로도 보기만 할 생각이다.

현실은 미녀들과의 선상 파티가 아니라, 선상 피티 받은 근육 수적들이 가득한 갑판에서 장강을 바라보는 것이 전부다.

아니, 하나 더 있다.

쉭!

바로 괄괄하신 우리 노야, 화왕 적천강이 심심할 때마다 날려 보내는 탄지(彈指)를 요리조리 피하는 것이다.

“어쭈, 피해?”

“……아니, 이거 피하는 수련이잖아요. 명경지수를 유지하며 감각을 극대화시켜야 중단전에 익숙해진다면서요?”

적천강이 뻔뻔하게 대꾸했다.

“방금 건 맞으라고 보낸 것이다. 어디서 감히 수련 중에 한눈을 팔아?”

“두 눈 전부 팔았는데요.”

“확 그냥. 눈깔을 파 주랴?”

두 눈에 쌍심지를 켠 적천강이 손가락을 갈고리처럼 치켜세우며 말을 이었다.

“이 수련이 그리 쉬워 보이는 줄 아느냐? 정신을 집중해도 피할까 말까다.”

“거 참. 알겠습니다. 알겠다고요.”

투덜거리며 대답한 나는 두 눈을 감았다. 그리고 다음 순간 슬며시 다시 눈을 떴다.

“그런데요.”

“뭐?”

“저 방금 한눈팔면서도 잘 피하지 않았어요?”

“어, 그러네?”

“……?”

“……?”

“……!”

“……!”

뭐야 이거.

내 황당한 시선에 입을 꾹 다물고 있던 적천강이 돌연 벌컥 성을 냈다.

“그렇게 말고! 저놈처럼 하라고! 저놈처럼!”

그의 손끝이 가리키는 방향에는 한 치의 움직임도 없이 가부좌를 튼 채 앉아 있는 청년이 있었다.

무슨 이유에서인지 나와 함께 수련에 강제 참여하게 된 청풍이다.

“저놈을 봐라. 애가 평소에는 좀 이상해도 할 때는 완벽하게 하지 않느냐. 자세도 흐트러지지 않고, 호흡도 가늘고 길게 일정하게 유지 중이지. 주위에서 무슨 일이 벌어지건 간에 흔들림 없는 마음과 자세. 저것이 바로 명경지수다.”

숨도 쉬지 않고 칭찬을 퍼부은 적천강이 손가락으로 청풍을 가리키며 말을 이었다.

“저놈이 어떻게 피하는지 똑똑히 봐라. 자, 이제 내가 탄지를 날리면…….”

쉬익! 퍽!

관자놀이에 탄지를 얻어맞은 청풍이 번쩍 눈을 떴다.

잠이 대롱대롱 매달린 눈동자로 주위를 바라보더니 그제야 고통이 느껴졌는지 머리를 쓰다듬었다.

“아이코. 아파요…….”

그리고 빛보다 빠른 꿈속으로의 복귀.

나는 적천강을 물끄러미 바라보며 물었다.

“명경. 뭐요?”

“명경…… 됐다. 이놈이나 저놈이나. 그냥 다 때려쳐!”

오늘도 장강은 평화롭다.
```

## Final English reading copy

```markdown
# Chapter 441

“T-Team Leader. May I come in for a moment?”

His voice was taut with tension.

Seok Go Jun reached toward the door while glaring at it with bloodshot eyes.

*Crack!*

A powerful force shot through the air, tearing and crumpling the iron door like a sheet of paper.

The security-team employee who witnessed the incredible sight from a few feet away swallowed a startled breath.

“Gasp.”

“I told you not to let anyone approach.”

The team member met Go Jun’s red glare head-on, and a shiver ran down his spine.

He had heard his colleagues talk about the extreme change in their direct superior, who had always been as precise and cold as a machine. But facing him like this, the team member’s voice trembled with fear despite himself.

“I-It’s just that… there’s something I need to report…”

“Put it off.”

His low voice sounded as though it had been dragged up from the depths of an abyss.

The team member wanted to do exactly that. But if it had been something trivial, they would never have drawn lots to decide who would deliver the report.

Swallowing hard, he squeezed out his courage and spoke.

“The head of the investigation team contacted us urgently. They said they discovered a strange object whose identity they couldn’t determine…”

Go Jun, who had been about to turn away, came to an abrupt stop.

“A strange object?”

“Yes, Team Leader.”

“Could it be—”

“No, sir.”

Worried that the sparks might fly his way, the team member hurriedly continued.

“After checking, we confirmed that none of the late Vice Guild Master’s belongings have been found yet.”

“Are you sure?”

“Yes. We’re keeping the team members dispatched to the site under constant watch in case they try to pocket something. There’s no doubt.”

“And?”

“Pardon?”

“There’s only one report I need from those bastards. A report saying they found what I need.”

Go Jun’s eyes sank into darkness.

Even now, with the Crown Prince Party—closely tied to the Ares Guild—on the decline, the Ares Guild’s influence and power remained intact.

Greed did not disappear just because the person in charge changed or the government was replaced. Everyone had it.

Even a straight bamboo stalk bent when it could no longer bear its weight. Go Jun had created that weight with tens of billions of won.

The head of the investigation team managing the city that had once been the Arch Lich’s stronghold and the senior officials under him were no different.

“Tell those bastards to find it, no matter what it takes. And tell them not to contact me again until they do.”

There was no such thing as a favor in this world without a price. Go Jun had bought them with a fortune, and if they failed to deliver what he wanted, he intended to retaliate accordingly.

That was how important the object he was searching for was.

Not merely because it was a keepsake of the Master he had followed like a father. It could also become a powerful weapon capable of driving someone into an inescapable corner.

*A holographic recorder.*

Lee Jungryong had been the true master of the immensely influential Ares Guild, and he always carried a small holographic recorder on his person in case something happened.

He had carried it on the day he met his death at Jin Taekyung’s hands, too.

*All the evidence is in there. If I can find it, then afterward…*

At that very moment, the flames burning in Go Jun’s eyes began to shake violently.

*Afterward… what am I supposed to do?*

Before he knew it, the face of one man—someone he hated beyond measure and feared even more—flashed before his eyes.

*…Jin Taekyung.*

Just thinking of that name made his heart sink and his hands and feet tremble.

The indifferent gaze that had looked down at him beneath the faint moonlight and the dry voice that had accompanied it clouded his eyes and ears like an apparition.

*I’ll say this one last time.*

The voice had burrowed into Go Jun’s ears as he howled from pain he had never imagined possible.

*Let Lee Jungryong be the end of it. Hide your teeth and put away your claws. If you do that… nothing will happen.*

Every bone in his body had been crushed like matchsticks, and his living flesh had been torn away as though it were being wrung out. He had been forced to struggle in a bottomless swamp of pain without ever managing to swing his weapon properly.

If Lee Jungryong had been a wall Go Jun could never cross and a Master he revered, Jin Taekyung was something no one had ever seen before.

No. He was like…

“A monster.”

The single word that escaped Go Jun without his realizing it was steeped in all the emotions and fear he felt.

And in the next instant, when he came to his senses, Go Jun realized something.

His hatred of Jin Taekyung was nothing compared to the fear he carried.

Jin Taekyung’s existence was fear itself, branded forever into Go Jun’s soul like a mark burned into flesh. At the same time, it was another name for the perfect helplessness he had felt for the first time in his life.

“T-Team Leader?”

Go Jun did not answer the team member’s call. He lowered his head with his teeth clenched, and his gaze fell on his own trembling hands.

*What the hell is this…*

*Crunch.*

Go Jun bit his lips until they bled, then raised his head. Ignoring the team member’s bewildered stare at the sight of his frightened superior, he opened his mouth.

“Tell the head of the investigation team to bring me that damn strange object. I don’t know what it is, but I need to see it for myself.”

“But a moment ago, you said—Ah, understood.”

Realizing his mistake, the team member hurriedly bowed and left the room.

Only after walking a considerable distance down the corridor did he finally release the breath he had been holding. Then he gestured toward the hotel employees waiting nearby.

“Wait here for a while. Go in once he’s calmed down. And the new room is ready, right?”

The Chinese hotel employees nodded with calm expressions.

This was not the first time Go Jun had gone on a rampage. It had already happened several times over the past week.

But what did it matter?

Until a few days ago, the hotel had belonged to a local notable in Sichuan Province. After the Ares Guild purchased it, the Koreans standing before them had become their new employers.

They were the best employers imaginable, even handing out generous overtime pay to ensure their secrecy.

“There’s no point saying any more. We all know the situation, so let’s do our jobs properly.”

The team member tossed a thick envelope to them, wiped the sweat from his brow, and walked away.

It was already a problem that they still hadn’t managed to leave this cursed land of China. But the uneasy state of the man who would become the Ares Guild’s new captain after Lee Jungryong kept sticking in his mind.

*Could that rumor really have been true?*

He remembered something that had been circulating quietly within the security team.

And he remembered his own unsettled feelings.

*The treatment is incredible, but if Team Leader stays like that from now on…*

There would be no problem if Go Jun remained the head of security. The enormous warship called the Ares Guild was not so fragile that one mistake by a helmsman could make it capsize.

But if he became the new captain, that was a different story.

*Damn it. I’ve never had to worry about something like this before.*

The team member muttered to himself and pulled a smartphone from inside his suit jacket. It was a work phone that left no records and could not be traced.

After a long series of rings, someone answered.

“Ah, Mr. Park. I was waiting for your call.”

“I’ll get straight to the point. Our team leader wants to see the object you mentioned in person.”

“In person?”

“Yes, in person. Our team leader wants to avoid people’s attention as much as possible right now, so you understand what I’m saying, correct?”

The recipient of the call, the head of the investigation team, cleared his throat.

“Cough. That may be difficult. Since this is the Arch Lich’s former stronghold, there are also foreign personnel dispatched by the United Nations, and security is tighter than you might expect…”

“Name your price. But there must not be a single mistake.”

A short while later, the team member ended the call and clicked his tongue.

“Those bastards. All they care about is money. Well, I suppose that’s why this worked out.”

The world did not change easily. Faced with overwhelming money and power, the word *impossible* had no meaning.

Since joining the Ares Guild’s security team, he had witnessed countless situations where the impossible had been made possible.

And that fortresslike power would naturally be inherited by one man.

*Team Leader Go Jun.*

The Ares Guild’s new captain.

The team member was only one of countless rowers, but Go Jun was different. When his thoughts reached that point, he suddenly became curious about the one person Go Jun feared so much.

*Jin Taekyung.*

People’s mouths could never be sealed completely.

The rumor had begun when three Hunters who had secretly left with Go Jun one day a week earlier opened their mouths.

For now, only a tiny number of people within the security team—who could be called Go Jun’s closest associates—knew the truth. But soon, it would spread like an epidemic.

*If it’s true…* *Haa. Things have gotten seriously complicated.*

The team member took a deep breath and sharpened his gaze.

From this point on, he would have to agonize over countless decisions. Should he remain on his current ship, or set sail for a new one?

If he did not want to become anyone’s enemy, his only option was to leave this line of work entirely.

*I need to keep my head on straight. Yeah.*

For now, his first priority was bringing back the object the head of the investigation team had smuggled out.

As he traveled to the place they had agreed to meet, he suddenly found himself envying Jin Taekyung.

*Damn. If I had fifty trillion won like that bastard, I’d go straight to Europe and live like royalty.*

He was rich too, owning several buildings, but human greed was never easily satisfied.

It was like wanting an expensive yacht and helicopter after buying a luxury foreign car, then wanting a private jet of your own after that.

The team member smacked his lips in envy.

*I wonder what that Jin Taekyung is doing right now. Having a luxury-yacht party with Playboy models?*

* * *

Beneath the blazing sunlight, well-tanned bronze muscles rippled.

Their identity was that of beautiful model women from around the world who had gathered to enjoy a yacht party with me…

“One, two!”

“Heave-ho!”

…No. They were the river bandits of the Water Dragon Stronghold.

I gazed sorrowfully at the musclebound monsters working busily around me.

*A yacht party, my ass.*

I had only ever seen those on the internet, and I planned to keep it that way.

Reality was not a yacht party with beautiful women. It was standing on a deck packed with musclebound river bandits who had been put through onboard personal training, staring out at the Yangtze.

No. There was one more thing.

*Whoosh!*

I had to dodge the finger flicks our boisterous Old Master, Fire King Jeok Cheongang, sent flying whenever he got bored.

“Oh? You dodged?”

“…This is training to dodge them, isn’t it? You said I had to maintain a mind as clear as a mirror and heighten my senses to become accustomed to the Middle Dantian.”

Jeok Cheongang answered shamelessly.

“That one was meant to hit you. How dare you look away during training?”

“I was looking away with both eyes.”

“Don’t push me. Want me to gouge them out?”

Eyes blazing with fury, Jeok Cheongang raised his fingers like claws and continued.

“Do you think this training looks easy? Even with your full concentration, you’ll barely manage to avoid them.”

“Fine, fine. I understand. I said I understand.”

Grumbling, I shut my eyes. Then, in the next moment, I quietly opened them again.

“But…”

“What?”

“Didn’t I just dodge that perfectly even while looking away?”

“Oh. So you did.”

“…?”

“…?”

“!”

“!”

What the hell was this?

Jeok Cheongang had pressed his lips tightly together beneath my incredulous stare. Then he suddenly exploded in anger.

“Not like that! Do it like that brat! Like him!”

The direction of his fingertip pointed toward a young man sitting cross-legged without the slightest movement.

For some reason, Cheongpung had been forced to participate in training alongside me.

“Look at that brat. He may be a little strange normally, but when it matters, he does everything perfectly. His posture hasn’t wavered, and he’s maintaining a thin, long, steady breath. An unwavering mind and posture, no matter what happens around him. That is what it means to be clear as a mirror and still as water.”

After showering Cheongpung with praise without even stopping to breathe, Jeok Cheongang pointed at him and continued.

“Watch carefully how he dodges. Now, when I send a finger flick…”

*Whoosh! Thud!*

A finger flick struck Cheongpung in the temple, and his eyes flew open.

He looked around with his eyelids drooping sleepily, then rubbed his head once the pain finally seemed to register.

“Ow. That hurts…”

Then he returned to his dream faster than light.

I stared at Jeok Cheongang and asked,

“Clear as a mirror? What?”

“Clear as a mirror… Forget it. You and that brat, both of you. To hell with all of it!”

The Yangtze was peaceful today, too.
```

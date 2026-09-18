<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0399.txt",
      "sha256": "af62c706da7d7dbaa37d4e0a35e80805c073b71c6c561584badef4fb3328e81e",
      "bytes": 12439
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "516c336b5205fe9b8a08b8d0e26bbc5d994cd098ef84f49a73aa177af6fc2def",
      "bytes": 1915
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "28828e2044174e8b0239824352891d22de57f15a178e1e60b51291c7c5601da1",
      "bytes": 135438
    },
    {
      "path": "characters/Heavenly Power Demon.md",
      "sha256": "4990a9445551134b9a396c5279d97866f8697df8031c8edd14f6007c548c52ea",
      "bytes": 1018
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "a5a2539cddf7afd0105e2efe3cb1d409f8829997e0bab5e24aca03840c2faa92",
      "bytes": 1390
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "f1ef19cae240804ff6a0913e7078fb1f296277735884d6ee226a242631c195b7",
      "bytes": 1212
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "3ea393c6e4da0e0eb396537554c4c807d661dd5f2dc2aa13e0deb889ce7a0407",
      "bytes": 622
    },
    {
      "path": "characters/Lei Fei.md",
      "sha256": "cc76bf17099cdaea248621e58f0bd4a053fbe2dd2c8133aa7d66367f308df262",
      "bytes": 535
    },
    {
      "path": "characters/Western Heaven Demon Lord.md",
      "sha256": "0e6cf083aec40723158872d9fb12f6288db37a787e431c3d85a6a9b4b81f8c33",
      "bytes": 888
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "cb1780909541b412543c66882a26c82e1d6769bccb5cf0528b5bbaf77dc4d504",
      "bytes": 116792
    }
  ],
  "estimated_tokens": 9953
}
-->

# Durable State Update — Chapter 399

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 399. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 399. Profile updates may replace only one
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
  "chapter": 399,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 399,
    "continuity_sources": [399],
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
    "Team Leader Choi survives his catastrophic injuries after receiving half of the top-grade potion, and Shao Shen receives the remaining half and begins recovering.",
    "Jin Taekyung is standing between Choi and Shao and the Death Knight Lord's army, wielding White Flame and intending to kill every monster that crosses his spear.",
    "Jin killed one Death Knight with the Flame-Extinguishing Divine Fist and has begun overwhelming the surrounding monster army.",
    "The Skeleton Warlord is protecting Choi and Shao at Jin's command in exchange for any wish after the battle.",
    "The level-135 Death Knight Lord commands the monster army and orders the troops to make way for him.",
    "The black knight remains bound to his creator and eternal lord, but strange memories continue surfacing and his hand unconsciously searches between his armor plates.",
    "The fire dragon within Jin's dantian awakened as he prepared to fight the Death Knight Lord.",
    "Lei Fei remains missing with his unit, and Wei Fenghu still wants Jin to bring him back if found."
  ],
  "continuity_sources": [
    398
  ],
  "open_questions": [
    "What is the black knight's identity and origin, and what is the significance of the child, shoe, and emerging memories?",
    "Who is the lord served by the black knight, and what is the Arch Lich's larger objective?",
    "What will happen in Jin Taekyung's confrontation with the Death Knight Lord?",
    "What happened to Lei Fei and the Second Fiend assigned to the Qingcheng attack?"
  ],
  "safe_through": 398,
  "temporary_decisions": [
    "Render 데스나이트 로드 as Death Knight Lord and 스켈레톤 워로드 as Skeleton Warlord.",
    "Render 군주시여 as my lord in the black knight's deferential reply.",
    "Preserve Jin's blunt, profane defiance toward the Death Knights and Death Knight Lord."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 일격     | **One Strike**                         |
| 시스템              | **System**                     |
| 레벨               | **Level**                      |
| 몬스터     | **monster**           |
| 귀가      | **your family**                                                 |
| 천력마 | **Heavenly Power Demon** | Formerly imprisoned Tang Clan criminal; distinct from 천력부, Heavenly Axe. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 레이페이 | **Lei Fei** | Concealed Chinese S-rank Hunter and head of the Public Security Armed Forces Department in Sichuan Province. |
| 서천마군 | **Western Heaven Demon Lord** | Title of the middle-aged antagonist who commands the summoned black-robed hunters. |
| 화염신장 | **Flame Divine Palm** | Jopil's deadly palm technique, noted when Taekyung compares Jopil with Mukyung. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 공수납백인 | **Empty-Hand Seizes the Blade** | Technique for catching an opponent's weapon between bare fingers. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 오우거 | **ogre** | B-rank monster species emerging from the Gate. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 라이칸스로프 | **Lycanthrope** | B-rank Gate monster species. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 멸염신권 | **Flame-Extinguishing Divine Fist** | Named fist technique Taekyung announces at the chapter's end. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 화룡갑 | **Fire Dragon Armor** | Jin Taekyung's renamed bound armor, formerly the Black Dragon Armor. |
| 데스나이트 | **Death Knight** | Undead commander type serving under the Black Knight. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 진태경 | 천력마 | prisoner_feeder_to_prisoner | you | casual and mocking | Taekyung questions the Heavenly Power Demon and mocks him as the Kunlun Sect's public-pissing criminal. |
| 천력마 | 진태경 | prisoner_to_prisoner_feeder | you | gruff and self-possessed | The Heavenly Power Demon speaks of himself as 노부 while questioning Taekyung. |
| 서천마군 | 진태경 | hostile_opponents | you | calm and taunting | Uses 자네 while questioning Taekyung and offering to take him alive. |
| 진태경 | 서천마군 | hostile_opponents | Western Heaven Demon Lord | casual and defiant | Identifies the Demon Lord by title and answers his surrender demand with sarcasm. |
| 서천마군 | 적천강 | hostile_invader_to_unconscious_patient | you | calm and predatory | Says someone wants to see Jeok Cheongang and attempts to move him with Seizing an Object Through Empty Space. |
| 적천강 | 서천마군 | hostile_opponents | you bastard | blunt and threatening | Jeok addresses the Western Heaven Demon Lord with 네놈 while defending Taekyung and ordering him not to touch his Disciple. |
| 데스나이트 | 인간 | enemy combatants | human | contemptuous and commanding | Used in the Death Knight's warnings to Jin. |
| 데스나이트 | 로드 | subordinate to commanding lord | Lord | fearful and deferential | The Death Knight calls to the Death Knight Lord after Jin overwhelms the army. |

## Listed compact profiles

### Heavenly Power Demon.md

# Heavenly Power Demon (천력마)

- **Safe through:** Chapter 367
- **Aliases:** None
- **Role:** Deceased former Elder of the Great Heavenly Demon Divine Cult who led the subjugation of Qinghai and opened the first front of its holy war before transferring three jiazi of internal energy to Jin Taekyung and asking him to kill the Western Heaven Demon Lord.
- **Personality:** Quiet and self-possessed despite his severe imprisonment, he is reflective about the moral ambiguity of the Great Faction War and disillusioned with the Divine Cult's corruption.
- **Voice:** Gruff and dry, with formal self-reference as 노부.
- **Relationships:** He was once an Elder and commander under the Great Heavenly Demon Divine Cult's Cult Leader, has spent more than forty years imprisoned by the Sichuan Tang Clan, and identifies the Western Heaven Demon Lord as one of the Divine Cult's four Protectors who served closest to and led astray the Cult Leader.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 376
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is a legendary wandering martial master and Jin Taekyung's Master.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, and casually threatening or violent when dissatisfied. His meeting with Taekyung rekindled his will to live, making him determined to extend his life despite his illness.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 397
- **Aliases:** Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, and a Supreme Peak master who has manifested Force and crossed the wall into true mastery.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother; Jeok Cheongang is his Master; Cheongpung is his trusted companion and only true martial rival; Choi Minwoo is his subordinate and student; his mother and sister Hayeon are among those he protects.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 397
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Lei Fei.md

# Lei Fei (레이페이)

- **Safe through:** Chapter 393
- **Aliases:** None
- **Role:** One of China's concealed S-rank Hunters and head of the Public Security Armed Forces Department stationed in Sichuan Province, currently missing with his unit after the first Monster Wave.
- **Personality:** No personality traits are established.
- **Voice:** No voice traits are established.
- **Relationships:** Wei Fenghu is his maternal uncle and raised him as his own son.

### Western Heaven Demon Lord.md

# Western Heaven Demon Lord (서천마군)

- **Safe through:** Chapter 378
- **Aliases:** None
- **Role:** Former Protector of the Divine Cult who commands Dark Heaven's assault on the Sichuan Tang Clan, lost the Myriad-Poison Ring to Jin Taekyung, suffered a crushed ankle and a torn wrist, and was temporarily possessed by the Lord of Heaven before the borrowed body was destroyed.
- **Personality:** Cold, detached, patient, and utterly ruthless toward those he interrogates or hunts.
- **Voice:** Controlled and dispassionate, with concise statements delivered in a quiet, threatening tone.
- **Relationships:** Tang Taesang and the Heaven-Shaking Venerable Nun were his latest victims, he lost one arm taking their lives, and the Qilian Three Fiends now submit to him alongside his hundreds of black-robed hunters.

## Korean source

```text
＃399화



쉬익!

강기(罡氣)에 휩싸인 창날을 막을 수 있는 것은 아무것도 없었다. 총알을 튕겨 내는 가죽도, 강철보다 단단한 뼈와 살도.

푸푸푹!

과녁이 넓으니 보너스가 붙는다. 라이칸스로프의 가슴을 관통한 창날은 뒤에 바짝 붙어 있던 놈들까지 꼬치처럼 꿰어 버렸다.

- 크륵, 큭.

부릅뜬 눈동자에 서린 감정은 의문과 억울함이었다.

놈의 눈빛이 수많은 몬스터 중 왜 하필 자신이냐고, 나는 네가 정한 사선(死線)을 넘지 않았다고 항변하는 듯했다.

“아니지.”

나직한 목소리와 함께 창대를 잡아당겼다.

치지직. 라이칸스로프의 발톱이 지면을 긁으며 창 안쪽으로 넘어왔다.

“넘었잖아. 지금.”

- ……!

여기까지다. 빛살 같은 속도로 박혀 있던 창을 뽑아낸 나는, 전면을 향해 횡으로 휘둘렀다.

화륵, 콰아아아!

공기를 태우며 휘몰아친 푸른 불꽃이 몬스터들을 집어삼켰다.

살아 있던 몬스터는 비명과 함께 타 죽었고, 이미 언데드로 변해 있던 놈들은 잿더미로 화했다.

띠링. 띠링. 띠링…….

처치를 알리는 시스템 알림이 쉼 없이 울려 퍼진다.

지금의 이 일격으로 몇 마리가 쓰러졌을까. 수십? 아니면 일백?

나는 일일이 헤아리기보다는 나아가는 것을 택했다. 처음부터 내 목적은 몇 마리의 몬스터를 해치우냐가 아니었으니까.

‘섬멸(殲滅).’

인간과 몬스터의 죽고 죽이는 싸움은 수십 년 동안 이어진 숙명이다.

오늘 이 자리에서 살아남을 수 있는 건 한 개의 종(種)뿐이고, 나는 쓰러지지 않을 것이다.

저벅.

시멘트 바닥 깊숙이 박힌 창을 넘어 발을 내디뎠다. 동시에 수많은 몬스터들이 약속이라도 한 것처럼 뒤로 물러난다.

한 걸음, 두 걸음, 세 걸음.

계속해서 걸음을 옮겨도 몬스터와의 거리는 좁혀지지 않았다. 내가 다가서는 거리만큼, 놈들이 물러서고 있었다.

- 이런 미친…….

등 뒤에서 스켈레톤 워로드가 신음처럼 중얼거렸다.

한 사람의 인간이 수천의 몬스터 군단을 압도하는 광경이다.

이 정도면 인류 역사의 한 페이지는 아닐지라도 한 문단 정도는 장식할 만한 일이 아닐까.

- 어, 어딜 가는 것이냐!

“두 사람이나 잘 지켜. 어차피 멀리 안 간다.”

더 정확히 말하자면, 멀리 나갈 필요가 없어졌다고 해야 맞겠다.

이미 손님이 도착했는데 굳이 마중을 나갈 이유는 없으니까.

‘드디어 왔군.’

내 짐작은 정확했다. 썰물처럼 좌우로 갈라지는 몬스터 군단 사이로, 온통 검은 뼈로 이루어진 해골마에 올라탄 ‘놈’이 모습을 드러냈다. 저 멀리에서.

다그닥, 다그닥.

칠흑빛을 띤 풀 플레이트 메일에 깊이 눌러쓴 투구 아래로는 붉은 안광이 또렷하다.

오우거와 같은 대형 몬스터보다는 훨씬 작은 체구였지만, 놈에게서 흘러나오는 마력은 크고 강대했다.



[Lv.135 데스나이트 로드]



135레벨. 지금까지 상대했던 어느 몬스터에게서도 찾아볼 수 없던 수치다.

천천히 속도를 더해 다가오는 데스나이트 로드를 보며, 나는 문득 생각했다.

‘내가 저놈을 쓰러트릴 수 있을까.’

무림에서 있었던 서천마군과의 싸움은 그야말로 목숨을 건 처절한 사투였다.

서천마군이 처음부터 날 제거할 생각이었다면, 천력마가 공력을 넘겨주지 않았더라면, 레벨업으로 말미암은 기적 같은 회복이 없었다면, 위기의 순간에 적천강이 깨어나 구해 주지 않았다면 서너 번쯤 죽고도 남았을 것이다.

하지만 결국 나는 살아남았고, 보다 더 강해졌다.

그때부터였다. 머릿속에 한 가지 의문이 계속해서 맴돌기 시작한 것은.

‘지금의 나는 어느 정도지?’

시스템은 무공의 경지와 능력치가 올랐다고 말한다.

지금까지 해 왔던 것처럼 스탯을 분배하고 전투를 치렀지만, 강기의 존재를 제외하면 글쎄.

나는 내가 얼마나 강해졌는지에 대해 자각하지 못하겠다.

그건 언제부터인가 늘 쉽고 당연한 일이었으니까.

그리고 지금.

타닥, 두두두!

한 줄기 바람이 되어 나를 향해 쏘아지는 데스나이트 로드를 보며 깨달았다.

놈의 전신에서 폭포처럼 흘러넘치는 강대한 마력에도 흔들리지 않는 스스로의 모습에 알 수 있었다.

‘나는…….’

쐐애애애액!

어느새 바람이 사라지고 섬광이 빈자리를 채운다. 해골마와 한 몸이 되어 들이닥친 데스나이트 로드의 손아귀에 들려 있던 검이 움직였다.

짙은 어둠이 모여들고 내리꽂히는 그 광경이, 너무도 느리게 느껴졌다. 머릿속에 한 가지 확신이 떠올랐다.

‘이 전장의 누구보다 강하다.’

느려진 세상 속, 나는 백염(白炎)을 뻗었다.

창날을 타고 솟구친 청백색의 불꽃이 어둠을 살라 먹었다.



* * *



하늘이 갈라지는 듯한 굉음이 울려 퍼졌다.

콰아아아-!

반경 수백 미터의 지면이 움푹 주저앉고 수십 년간 견고히 버텨온 병원이 붕괴했다.

압축된 공기가 소닉붐(Sonic Boom)처럼 겹겹이 터져 나가며 주위에 있던 모든 것들을 후려치고 날려 보냈다.

그리고 이 모든 일의 중심에, 그 누구도 범접할 수 없는 두 존재가 있었다.

쉭, 쉬쉬쉬쉬쉭! 꽈앙!

찰나의 순간에도 몇 번, 혹은 수십 번.

청백색의 불꽃과 칠흑 같은 어둠이 부딪치고 섞여들 때마다 귀가 먹먹해지는 굉음과 참혹한 파괴가 잇따랐다.

두 존재의 움직임을 볼 수 있는 인간과 몬스터는 아무도 없었다.

그들은 한 차원 위에 존재했고, 자신들만의 세상과 시간 속에서 격돌했다.

쉭!

진태경의 손에 들린 은백색의 창이 허공을 내리그었다.

공간을 찢으며 쏟아져 내리는 청백색의 화염. 그러나 검은 기사는 물러서지 않고 검을 휘둘렀다.

콰앙!

넘실거리는 마력이 화염과 부딪친 순간 덮쳐 오는 엄청난 압력에, 검은 기사가 타고 있던 해골마가 산산이 부서졌다.

하지만 충성스러운 종마이자 A급 몬스터인 나이트메어(Nightmare)의 소멸은 곧 다가올 일들에 비하면 아무것도 아니었다.

쐐애애애액!

어떤 준비 자세도 없는, 그야말로 섬광과도 같은 투창(投槍).

검은 기사는 본능과도 같은 움직임으로 신형을 틀었다. 엄청난 열기가 그의 앞가슴을 스쳐 몬스터들의 사이를 파고들었다.

콰드드드득! 꽈앙!

수십여 마리의 몬스터를 관통한 창날이 지면에 내리꽂히자 굉음과 함께 거대한 크레이터가 생성되었다.

그 여파에 휘말린 몬스터들이 공포에 찬 비명을 내지르기도 전에, 진태경의 신형은 검은 기사를 향해 나아가고 있었다.

스윽.

소리도, 기척도 없는 한 걸음.

검은 기사가 그 사실을 알아차렸을 때는, 수십 미터의 거리를 지우며 목표에 도달한 진태경의 일권(一拳)이 그의 가슴을 향해 쏘아진 직후였다.

“꺼져라.”

- ……!

쾅!

멸염신권(滅炎神拳). 용암보다 더한 열기가 갑옷을 후려쳤다.

엄청난 속도로 튕겨 나간 검은 기사가 허공에서 신형을 뒤집으며 자세를 바로잡았다. 동시에 그의 손이 검자루를 잡고 힘차게 흩뿌려졌다.

쐐애애액! 쉬쉬쉭!

검은 마력이 수십 개의 벼락이 되어 진태경을 향해 쏘아졌다. 하나하나가 경천동지할 위력을 지닌 공격.

그러나 진태경은 이미 그 자리에 없었다.

콰과과광!

희뿌연 먼지구름을 터트리며 쇄도한 진태경이 두 손을 뻗었다.

어느새 방향을 바꾸어 그의 정수리를 향해 내리그어지던 검신을 합장하듯 붙잡았다.

공수납백인(空手納白刃).

푸른 화염에 휩싸인 두 손과 막대한 마력이 서린 검신이 두 존재의 사이에서 파르르 떨렸다.

막아서는 자와 나아가는 자.

쉴 틈 없던 공방을 잠시 멈추게 한 치열한 대립은, 예상치 못한 불청객의 등장으로 깨어졌다.

- 너, 인간이여!

외침과 함께 나타난 데스나이트가 진태경의 등을 향해 메이스를 내리친 그 순간이었다.

퍼벙!

데스나이트는 자신이 언제, 어떻게 죽었는지조차 알지 못했다.

칼날처럼 허공을 내리그은 진태경의 발뒤꿈치에 투구째로 머리가 터져 나갔으니까.

털썩.

그러나 허무한 소멸이었을지언정, 아무런 의미조차 없는 공격은 아니었다.

검은 기사의 붉은 안광이 번쩍 빛남과 동시에 손아귀에 들린 검이 그 어느 때보다 강한 마력을 뿜어냈다.

아주 미세한 틈.

진태경이 데스나이트를 처치하기 위해 공력을 분산시켰던 찰나의 순간은 균형을 무너트리기에 충분했다.

콰득! 촤아아아악!

핏물이 솟구쳤다.

한없이 붉은 그것은 인간의 것이었고, 검은 기사의 검이 진태경의 가슴을 베었다는 흔적이었다.

검은 기사의 머릿속에 한 가지 확신이 스쳤다.

‘끝이다.’

그리고 다음 순간, 화염에 휩싸인 진태경의 주먹이 검은 기사의 옆구리를 후려쳤다.



* * *



콰드드득!

- ……!

데스나이트 로드의 몸뚱어리가 들썩였다.

고통을 느끼지 못하는 언데드 몬스터답게 아무런 비명도 없었지만, 나는 놈의 투구 사이로 보이는 안광에 담긴 의문을 읽었다.

‘어떻게?’

그래, 딱 그런 눈빛이다.

나는 무뚝뚝한 목소리로 대꾸했다.

“너만 갑옷 있는 줄 알았냐?”

펑!

이번에는 화염신장(火焰神掌)이다.

계속된 타격으로 금이 가 있던 데스나이트 로드의 갑옷이 조각나며 깨져 나가는 것이 보였다.

“아팠다. 이 개새끼야.”

우두둑!

건틀릿을 낀 놈의 팔목을 꺾고 그대로 부러트렸다.

이런 공격들이 언데드 몬스터에게 얼마나 의미가 있는지는 모르겠지만, 검을 놓치게 하기에는 충분했다.

철그럭.

쇳소리와 함께 검을 놓친 데스나이트 로드를 기다리고 있는 건 무차별적인 공격이었다.

쾅! 콰득! 퍼벙!

놈의 발등을 밟고 쉴 새 없이 주먹을 내질렀다.

어깨, 팔, 옆구리, 가슴.

순식간에 수십 번의 공격을 허용한 데스나이트 로드가 반격을 시도해 왔지만 상관없었다.

퍽!

- ……?

“놀랄 거 없다. 내 갑옷도 꽤 쓸 만하거든.”

내게는 화룡갑(火龍鉀)이 있으니까.

‘이걸 여기에서 쓰네.’

화룡갑은 서천마군을 처치하고 얻은 신병이기다.

무림에서의 전투 당시 워낙 심하게 망가진 탓에 아직까지도 자체 복구가 진행 중이지만, 50% 정도의 복구율로도 제 몫을 톡톡히 해냈다.

‘완전히 막아 내진 못하는 바람에 죽을 뻔하긴 했지만.’

검에 베였을 때는 나 역시도 눈앞이 아찔했다.

그러나 이 정도 고통쯤은 이미 지긋지긋하게 겪었다.

게다가 이미 나보다 앞서 죽어 갔던 이들이 겪은 고통에 비할 바도 아니었다.

“이건…… 오늘 네가 죽였던 그 사람들 몫이다.”

나는 온 힘을 다해 놈의 얼굴을 후려쳤다.

팔성의 멸염신권에 어떤 상황에서도 견고하던 투구가 박살 나며 놈의 얼굴이 드러났다.

이제 승패의 저울추는 기울었다. 단 한 방. 마지막 일격이면 놈의 목숨을 앗아갈 수 있다.

“그리고 이건…….”

그 순간, 높게 들어 올렸던 주먹이 우뚝 멈췄다.

나는 핏물로 엉겨 붙어 있던 눈꺼풀을 깜빡였다. 아주 잠깐, 내 시선에 닿은 누군가의 얼굴에 시간이 멈춘 듯했다.

낯설지만 익숙한 얼굴. 이미 죽어 있는 새하얀 피부와 붉은 안광을 지닌 그는, 홀로그램 영상 속에서 보던 어느 영웅과 꼭 닮아 있었다.

“……레이페이?”
```

## Final English reading copy

```markdown
# Chapter 399

Whoosh!

Nothing could stop the spearhead wrapped in Force—not leather that could deflect bullets, nor flesh and bone harder than steel.

Puff, puff, puff!

The target was wide, so there was a bonus. The spearhead pierced through the Lycanthrope’s chest and skewered the ones right behind it like meat on a skewer.

—Kreuk, k-kek.

The emotion in its wide-open eyes was a mixture of confusion and indignation.

Its gaze seemed to protest: *Why me, out of all these monsters? I never crossed the death line you drew.*

“No, you did.”

With a quiet mutter, I pulled on the shaft.

Scrape, scrape. The Lycanthrope’s claws raked the ground as I dragged it over to my side of the spear.

“You crossed it. Just now.”

—……!

That was far enough. I yanked the embedded spear free at lightning speed, then swept it horizontally in front of me.

Whoosh, KRAAAASH!

Blue flames whipped through the air, scorching it as they swept forward and devoured the monsters.

The monsters that were still alive burned to death with screams, while those that had already become undead were reduced to ashes.

Ding. Ding. Ding……

System notifications announcing my kills rang out without pause.

How many had fallen from that single strike? Dozens? Or a hundred?

Rather than count every one of them, I chose to keep moving. My goal had never been to kill a certain number of monsters.

*Annihilation.*

The battle between humans and monsters—a fate of killing and being killed—had continued for decades.

Only one species would be able to survive here today, and I would not be the one to fall.

Thud.

I stepped over the spear embedded deep in the cement floor. At the same time, countless monsters retreated as if they had made a pact.

One step. Two steps. Three steps.

No matter how far I continued walking, the distance between me and the monsters did not shrink. They retreated as far as I advanced.

—This is insane……

Behind me, the Skeleton Warlord muttered as if groaning.

A single human was overwhelming an army of thousands of monsters.

Even if it was not enough to fill a page in human history, surely this was worth at least a paragraph.

—W-Where are you going?

“Keep a good eye on those two. I’m not going far anyway.”

More precisely, I no longer had any need to go far.

The guest had already arrived. There was no reason to go out and greet him.

*He’s finally here.*

My guess had been correct. The monster army split apart to the left and right like the tide going out, and ‘he’ appeared among them, riding a skeletal horse made entirely of black bones.

From far away.

Clip-clop, clip-clop.

His full plate armor was pitch-black, and a vivid red glow shone beneath his low-set helmet.

He was far smaller than a large monster like an ogre, but the mana emanating from him was immense and powerful.

> **System**
>
> Lv. 135 Death Knight Lord

Level 135. It was a number I had never seen on any monster I had faced before.

As the Death Knight Lord slowly picked up speed and approached, a thought suddenly occurred to me.

*Can I defeat him?*

My battle with the Western Heaven Demon Lord in Murim had been a desperate struggle in which I had wagered my life.

If the Western Heaven Demon Lord had intended to eliminate me from the very beginning, if the Heavenly Power Demon had not passed his internal energy to me, if I had not experienced that miraculous recovery from leveling up, if Jeok Cheongang had not awakened and saved me at the critical moment, I would have died three or four times over.

But in the end, I had survived—and grown stronger.

That was when one question began circling endlessly in my mind.

*How strong am I now?*

The System said that my martial arts realm and stats had risen.

I had distributed my stats and fought battles just as I always had, but aside from the existence of Force, I wasn’t sure.

I had no real sense of how much stronger I had become.

At some point, it had all become easy and natural.

And now—

Tap-tap, thud-thud-thud!

As I watched the Death Knight Lord shoot toward me like a gust of wind, I realized it.

I remained unshaken by the immense mana pouring from his entire body like a waterfall. That alone told me.

*I am……*

Whoooooosh!

The wind vanished, and a flash of light filled its place. The sword held in the Death Knight Lord’s hand moved as he charged in together with his skeletal horse.

The sight of thick darkness gathering and crashing down seemed to unfold in slow motion. A single certainty surfaced in my mind.

*I am stronger than anyone else on this battlefield.*

In the slowed-down world, I thrust out White Flame.

Blue-white flames surged up along the spearhead and devoured the darkness.

* * *

A roar like the sky splitting apart rang out.

KRAAAASH!

The ground within a radius of several hundred meters caved in, and the hospital that had stood firm for decades collapsed.

Compressed air exploded layer after layer like a sonic boom, striking and hurling away everything around us.

And at the center of it all stood two beings whom no one else could approach.

Whoosh, whoosh-whoosh-whoosh! KABOOM!

Several times, or perhaps dozens of times, in the blink of an eye.

Every time the blue-white flames and pitch-black darkness collided and mingled, deafening roars and terrible destruction followed.

No human or monster could see the movements of the two beings.

They existed on a higher plane, clashing within a world and time of their own.

Swish!

The silver-white spear in Jin Taekyung’s hand slashed downward through empty space.

Blue-white flames poured down, tearing through space. But the black knight did not retreat. He swung his sword.

KABOOM!

The moment the surging mana collided with the flames, the resulting pressure shattered the black knight’s skeletal horse into pieces.

But the disappearance of Nightmare—a loyal warhorse and an A-rank monster—was nothing compared to what was about to happen.

Whoooooosh!

A thrown spear without any preparatory stance. A flash of light itself.

The black knight twisted his body with an instinctive movement. Tremendous heat grazed his chest and burrowed into the monsters behind him.

KRAKAKAK! KABOOM!

When the spearhead that had pierced through dozens of monsters slammed into the ground, a massive crater formed with a thunderous roar.

Before the monsters caught in the aftermath could even let out terrified screams, Jin Taekyung was already moving toward the black knight.

Sshk.

A single step without sound or presence.

By the time the black knight noticed, Jin Taekyung had erased dozens of meters and reached his target. His fist shot toward the black knight’s chest.

“Get lost.”

—……!

Boom!

Flame-Extinguishing Divine Fist. Heat hotter than lava slammed into the armor.

The black knight was flung away at tremendous speed, but he flipped his body in midair and regained his balance. At the same time, his hand seized the hilt of his sword and swept it out with force.

Whoooooosh! Shh-shh-shhk!

Black mana became dozens of lightning bolts and shot toward Jin Taekyung. Every one of the attacks possessed earth-shaking power.

But Jin Taekyung was no longer there.

KRAKABOOM!

Jin Taekyung charged through the cloud of pale dust and extended both hands.

The sword blade, which had changed direction and was now slashing down toward the crown of his head, was caught between his hands as if he were pressing his palms together.

Empty-Hand Seizes the Blade.

His blue-flame-wreathed hands and the blade laden with immense mana trembled between the two beings.

The one who blocked, and the one who advanced.

The fierce confrontation that had briefly halted their relentless exchange was broken by the arrival of an unexpected intruder.

—You, human!

It was the moment a Death Knight appeared with a shout and brought a mace down toward Jin Taekyung’s back.

Boom!

The Death Knight did not even know when or how he had died.

Jin Taekyung’s heel had sliced through the air like a blade and blown apart his head, helmet and all.

Thud.

But even if it had been a futile death, the attack had not been entirely meaningless.

The black knight’s red eye-light flashed, and the sword in his grasp unleashed more mana than ever before.

A gap no wider than a hair.

The instant Jin Taekyung had diverted his internal energy to kill the Death Knight was enough to break the balance.

Crunch! Slash!

Blood gushed out.

It was a shockingly red spray of human blood—the proof that the black knight’s sword had cut across Jin Taekyung’s chest.

A single certainty flashed through the black knight’s mind.

*It’s over.*

And in the next moment, Jin Taekyung’s fist, engulfed in flames, slammed into the black knight’s side.

* * *

Crack!

—……!

The Death Knight Lord’s body jerked.

As befitted an undead monster incapable of feeling pain, he made no sound, but I read the question in the red glow visible between the slits of his helmet.

*How?*

Yes. That was exactly the look in his eyes.

I answered in a flat voice.

“You think you’re the only one with armor?”

Boom!

This time, it was the Flame Divine Palm.

The Death Knight Lord’s armor, already cracked from the repeated blows, broke apart into fragments before my eyes.

“That hurt, you son of a bitch.”

Crack!

I twisted the wrist of the bastard wearing the gauntlet and broke it just like that.

I had no idea how meaningful attacks like these were against an undead monster, but they were enough to make him drop his sword.

Clank.

As the sword fell with a metallic sound, the Death Knight Lord was met with a merciless assault.

Boom! Crack! Bam!

I stepped on his instep and threw punches without pause.

Shoulder. Arm. Side. Chest.

The Death Knight Lord took dozens of attacks in an instant. He attempted a counterattack, but it did not matter.

Thud!

—……?

“Don’t be surprised. My armor’s pretty useful too.”

I had the Fire Dragon Armor.

*I’m using this here.*

The Fire Dragon Armor was a divine weapon I had obtained after defeating the Western Heaven Demon Lord.

It had been damaged so severely during the battle in Murim that it was still repairing itself, but even at a restoration rate of around fifty percent, it had more than done its job.

*Though I almost died because it couldn’t block everything completely.*

When the sword cut me, my vision had swum too.

But I had suffered this much pain more times than I could count.

Besides, it was nothing compared to the pain endured by those who had died before me.

“This is…for the people you killed today.”

I put all my strength into punching him in the face.

A Flame-Extinguishing Divine Fist at the eighth level smashed apart the helmet that had withstood everything, revealing his face.

The balance had tipped. One blow. One final strike would be enough to take his life.

“And this is……”

At that moment, my raised fist stopped dead.

I blinked through eyelids clotted with blood. For just an instant, time seemed to stop when my gaze landed on someone’s face.

A face that was unfamiliar, yet familiar.

With dead-white skin and red eyes, he looked exactly like a certain hero I had seen in a hologram video.

“……Lei Fei?”
```

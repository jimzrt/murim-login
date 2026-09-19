<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0420.txt",
      "sha256": "480ba6a0811a18f52b9e223975e3f9d161f2f3743dd965a74156cea0365f9995",
      "bytes": 12756
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "dba5048bb78a26e52e8c525ab755d145d2eb11f229a94c6714b5e025677f5311",
      "bytes": 1815
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "0c65c80cca3b94ba7b9a821e4917bcc55788f61aae6d0adf00efe413959aaa83",
      "bytes": 139066
    },
    {
      "path": "characters/Cheon Taemin.md",
      "sha256": "6f390ecbe66a13bc2ed39dbb5715c4bf5da7704f580411548fb8d164d256b9dc",
      "bytes": 590
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "233218e31473e5841b155471eb2695d6a91f56aba127b8c8f2e86fc96d23576a",
      "bytes": 533
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "410ac004dc5cb4c3db62adfa2d2a03427e79190acbef67d853b7fdca84e061e0",
      "bytes": 1270
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "9b339909de7caa700fdb60d583a47abba732423a7b3dda188c76e205baf11d72",
      "bytes": 622
    },
    {
      "path": "characters/Lee Jungryong.md",
      "sha256": "6c187b2c295baeb6b6a258c64972b09557dbf6b53a374649bd9f98f7909df658",
      "bytes": 1182
    },
    {
      "path": "characters/Lei Fei.md",
      "sha256": "8c10b13d54cfd4272b57713ac2bcf07ccea3739c3933d9a29fe70f08da02f807",
      "bytes": 893
    },
    {
      "path": "characters/Team Leader Choi.md",
      "sha256": "468eeef74225e824cf486ac3e6fbc11ad1f295a2b363d935502827b7f713d5a3",
      "bytes": 535
    },
    {
      "path": "characters/Wu Heixing.md",
      "sha256": "e7f78285630f78a40a07dcde03e291ed6611a76eff4f97720af772c5cc2927ac",
      "bytes": 795
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "940557f954a71b0f703d9dc184cddc2db5445f6e50fa5b0710904f654a04fb88",
      "bytes": 128217
    }
  ],
  "estimated_tokens": 10431
}
-->

# Durable State Update — Chapter 420

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 420. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 420. Profile updates may replace only one
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
  "chapter": 420,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 420,
    "continuity_sources": [420],
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
    "Jin Taekyung killed Lee Jungryong, who died believing his actions were the ending most suited to him and claiming he had no regrets.",
    "Lee Jungryong first met Cheon Taemin during the early Great Cataclysm, regarded him as an older brother and unreachable hero, and spent much of his life in his shadow.",
    "Jin Taekyung gained a massive amount of EXP and leveled up twice after defeating Lee Jungryong.",
    "Lee Jungryong's edited hologram of Wu Heixing's death remains capable of turning public opinion against Jin and those he protects.",
    "The city remains in the process of transforming into one enormous Gate through the Arch Lich's anchored mana.",
    "The Arch Lich, responsible for the city's Gate transformation, is now present before Jin Taekyung.",
    "The Skeleton Warlord remains frightened and trembling in the Arch Lich's presence, with the cause of his reaction still unexplained.",
    "The Quest One Who Returned from Death remains active, keeping Login unavailable until the Quest ends."
  ],
  "continuity_sources": [
    419
  ],
  "open_questions": [
    "Can the three Hunters stop the city's Gate transformation?",
    "What is causing the Skeleton Warlord's fear, dizziness, nausea, and insistence that they turn back?",
    "What will the Arch Lich do now that it has appeared before Jin Taekyung?"
  ],
  "safe_through": 419,
  "temporary_decisions": [
    "Render 아크 리치 as Arch Lich.",
    "Render 어둠에 잠식된 도시 as City Consumed by Darkness.",
    "Render 죽음에서 돌아온 자 as One Who Returned from Death.",
    "Render 착짱죽짱 as “The only good chink is a dead chink.”",
    "Render 형님 as hyung when Lee uses it, without changing the established Cheon Taemin relationship."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 최민우    | **Choi Minwoo**   |
| 천태민    | **Cheon Taemin**  |
| 이정룡    | **Lee Jungryong** |
| 혈도     | **acupoint** / **vital point**                   | Context dependent                                     |
| 시스템              | **System**                     |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 몬스터     | **monster**           |
| 길드      | **Guild**             |
| 팀장      | **Team Leader**       |
| 대격변     | **Great Cataclysm**   |
| 화산     | **Huashan**            |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 레이페이 | **Lei Fei** | Concealed Chinese S-rank Hunter and head of the Public Security Armed Forces Department in Sichuan Province. |
| 우헤이싱 | **Wu Heixing** | Chinese S-rank Hunter who provokes Jin and nearly draws his sword. |
| 아스모데우스 | **Asmodeus** | Demon King referenced in Taekyung's sarcastic comparison; does not appear directly. |
| 평화 | **Peace Guild** | Guild name. |
| 아레스 | **Ares Guild** | The leading Guild in Korea; formerly employed Team Leader Choi and Song Song. |
| 기감 | **Qi Sense** | Taekyung's sensory technique; its range reaches seventy meters in this chapter. |
| 패밀리어 | **Familiar** | System classification for the flies detected in Taekyung's home. |
| 허공섭물 | **Seizing an Object Through Empty Space** | Technique Jeok Cheongang uses to lift Jang Taebo remotely. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 마왕 | **Demon King** | The being Cheon Taemin killed. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 데스나이트 | **Death Knight** | Undead commander type serving under the Black Knight. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 이정룡 | 진태경 | senior S-rank Hunter to younger Hunter and adversary | Young man | polished, teasing, and veiled-threatening | Uses a genial tone and indirect threats while trying to make Taekyung release the captives. |
| 진태경 | 이정룡 | younger Hunter to senior S-rank Hunter and adversary | you | polite but mocking and defiant | Taekyung answers Lee's soft threats with the wolf-and-tiger metaphor and refuses to yield. |
| 이정룡 | 천태민 | younger_to_older_brother_by_choice | older brother | reverent and familiar; internal | Lee Jungryong uses 형님 in unspoken thoughts and regards Cheon Taemin as an older brother despite having no blood relation. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 우헤이싱 | 진태경 | hostile S-rank Hunter to foreign Hunter and provocation target | peninsula bangzi | insulting and confrontational | Wu repeatedly addresses Jin with anti-Korean slurs. |
| 우헤이싱 | 이정룡 | younger S-rank Hunter to senior Ares Guild authority | Mr. Lee | formal and deferential | Wu addresses Lee respectfully despite his usual hostility toward Koreans. |
| 데스나이트 | 인간 | enemy combatants | human | contemptuous and commanding | Used in the Death Knight's warnings to Jin. |
| 데스나이트 | 로드 | subordinate to commanding lord | Lord | fearful and deferential | The Death Knight calls to the Death Knight Lord after Jin overwhelms the army. |
| 진태경 | 레이페이 | former ally and fellow Hunter | Lei Fei | blunt and solemn | Jin addresses Lei Fei by name before telling him to rest. |
| 레이페이 | 진태경 | former ally and fellow Hunter | you | familiar and respectful | Lei Fei uses 자네 and 하게 while asking Jin to help him fulfill his final mission. |
| 진태경 | 우헤이싱 | adversarial S-rank Hunters | you idiot | insulting-casual | Mocks Wu's cowardice and orders him to stop complaining. |
| 이정룡 | 우헤이싱 | senior S-rank Hunter to younger allied S-rank Hunter | Mr. Wu | polished and formally coaxing | Lee publicly draws Wu into agreement with the suicide-squad plan. |
| 최민우 | 진태경 | trusted allied team leader to younger allied Hunter | Mr. Jin | formal-polite and concerned | Choi warns Jin about the danger of the operation and affirms his deep trust. |
| 진태경 | 최민우 | younger allied Hunter to allied team leader | Team Leader Choi | polite, familiar, and teasing | Jin jokes with Choi while acknowledging and dismissing his concern. |
| 진태경 | 결사대 | commander_to_subordinates | you bastards | blunt and commanding | Jin orders the suicide squad to exploit the opening and wipe out the surrounding monsters. |

## Listed compact profiles

### Cheon Taemin.md

# Cheon Taemin (천태민)

- **Safe through:** Chapter 419
- **Aliases:** Slayer
- **Role:** Ares Guild Master; humanity's great hero and the world's greatest Hunter; killed the Demon King and is known as the Slayer; created the first Mana Cultivation Method during the Great Cataclysm.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** Maternal grandfather of Team Leader Choi and father of Soyeong; regarded by Lee Jungryong as an older brother despite their lack of blood relation.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 419
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who has sworn never to kill again.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 419
- **Aliases:** Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, and a Supreme Peak master who has manifested Force and crossed the wall into true mastery.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and student, his mother and sister Hayeon are among those he protects, and the Skeleton Warlord is his captive undead commander.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 419
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Lee Jungryong.md

# Lee Jungryong (이정룡)

- **Safe through:** Chapter 419
- **Aliases:** None
- **Role:** Former Vice Guild Master of Ares Guild, one of Korea's two S-rank Hunters, and a Supreme Peak-level martial artist who was killed by Jin Taekyung.
- **Personality:** Outwardly genial, calm, and humorous; calculating, opportunistic, manipulative, coercive, and ruthless when challenged
- **Voice:** Smooth, good-natured, and indirect, using teasing conversation and veiled threats before becoming openly furious
- **Relationships:** Master of Park Jihoon and Go Jun (Team Leader Seok), whom he personally selected and trained; longtime Great Cataclysm acquaintance of Park Tae Seop; adversary of Jin Taekyung; knew Team Leader Choi from childhood; has an antagonistic history with Kim Hwajong, who saved his life at the collapse of Mapo Bridge eighteen years earlier; was visibly shaken by learning that Choi is Cheon Taemin's maternal grandson; regards Cheon Taemin as an older brother despite no blood relation and has long held him in respect and fear; operates as Ares Guild's senior authority beneath its Guild Master

### Lei Fei.md

# Lei Fei (레이페이)

- **Safe through:** Chapter 417
- **Aliases:** None
- **Role:** Lei Fei is a concealed Chinese S-rank Hunter and former head of the Public Security Armed Forces Department in Sichuan Province who recovered his human identity after becoming a level-120 undead Death Knight Lord and died fulfilling his final mission.
- **Personality:** Lei Fei's recovered memories show him as dutiful, honorable, family-oriented, and willing to serve as an unseen guardian.
- **Voice:** His human voice is formal and earnest, becoming warm and playful with family.
- **Relationships:** Wei Fenghu is his maternal uncle who raised him as a son; Lei Fei married an unnamed flower-shop owner and had a daughter, trained alongside Wu Heixing, and was corrupted by the Arch Lich before Jin Taekyung restored his identity.

### Team Leader Choi.md

# Team Leader Choi

- **Safe through:** Chapter 418
- **Aliases:** Choi Minwoo (최민우)
- **Role:** Allied team leader and Hunter who analyzes battlefield conditions during the Arch Lich operation.
- **Personality:** Calm, analytical, and steady under extreme battlefield pressure.
- **Voice:** Measured and logical, using clear tactical explanations.
- **Relationships:** Works alongside Jin Taekyung and Lee Jungryong in the coalition against the Arch Lich.

### Wu Heixing.md

# Wu Heixing (우헤이싱)

- **Safe through:** Chapter 418
- **Aliases:** None
- **Role:** Wu Heixing was a Chinese S-rank Hunter known for frequent media exposure and scandal who secretly practiced martial arts, including an internal-energy cultivation technique and fist-and-foot martial arts, before Jin Taekyung killed him.
- **Personality:** Arrogant, status-conscious, abusive, and fiercely proud of his power, he responds to humiliation with anger and protects himself even while his allies die.
- **Voice:** Loud, insulting, entitled, and dependent on national and political status.
- **Relationships:** He is openly hostile toward Jin Taekyung and Faye Chen, and resents Jin receiving Chairman Shao Yang's attention.

## Korean source

```text
＃420화



처음 몬스터를 마주했을 때, 사람들은 무슨 감정을 느꼈을까.

놀라움, 공포, 두려움, 당황?

잘 모르겠다. 내가 태어나기도 전의 일이었고, 굳이 따지자면 엄마 뱃속이 아니라 아버지 쪽에 있을 때였으니까.

하지만 그 역사의 현장에 있던 이들은 오래전부터 전해져 내려온 숱한 전설과 신화를 떠올렸을 것이다.

바로 지금의 나처럼.

‘악마.’

놈을 본 순간 뇌리를 스친 단어였다. 3m에 이르는 거체. 검은 광택이 흐르는 뼈. 인간과 흡사한 체형을 하고 있으나 근본적으로 다른 무언가.

스아아아아.

신화 속에 등장하는 악마의 날개처럼, 놈이 걸친 로브가 살아 있는 생물처럼 펄럭였다.

등장만으로도 세상을 어둡게 만든 악마, 아니 아크 리치의 붉은 안광이 스산한 빛을 뿌렸다.

- 너, 인간이여.

단 한마디.

주위의 공기가 파르르 떨렸다. 인벤토리 안에 존재하는 스켈레톤 워로드가 신음처럼 중얼거렸다.

- 언데드의 군주…….

짙은 공포가 배어 있는 목소리. 힘의 법칙은 몬스터에게도 적용된다.

그래, 스켈레톤 워로드의 말처럼 아크 리치야말로 이 땅에 존재하는 모든 언데드 몬스터의 군주일 것이다.

- 인간. 아직 늦지 않았다. 지금이라도…….

나는 대답 대신 작게 고개를 끄덕였다.

스켈레톤 워로드의 말이 맞다. 나는 아직 늦지 않았고, 충분한 기회가 남아 있었다.

‘놈을 막을 수 있는 기회. 말이지.’

이 거대한 면적의 대도시가 하나의 게이트로 돌변한다면, 그때는 정말 돌이킬 수 없다.

수많은 언데드 몬스터가 전염병처럼 퍼져 나갈 테고 아크 리치의 힘도 한층 강해질 것이다.

‘지금뿐이야.’

크게 심호흡한 나는 손을 뻗었다. 허공섭물로 끌어당긴 백염의 창대가 손아귀에 잡힌다.

무너진 콘크리트 더미를 넘어 터덜터덜 밖으로 나오자, 짙은 안개만이 자욱한 폐허가 나를 기다리고 있었다.

상하좌우. 어디를 둘러봐도 몬스터의 흔적은 보이지 않는다.

아, 취소. 한 놈이 있었지.

“만나서 반갑다. 이 시벌 놈아.”

이십여 미터 위. 허공을 밟고 선 채 나를 굽어보던 아크 리치가 안광을 빛냈다.

- 역시. 마계의 언어를 할 줄 아는군. 잘못 들은 것이 아니었어.

“예습 복습 철저히 했지. 근데 너, 나 아냐?”

- 나는 수백의 눈과 귀를 가진 존재. 줄곧 너를 지켜보고 있었다, 인간.

나는 문득 눈살을 찌푸렸다.

“줄곧?”

- 그렇다. 전장에서의 활약이 대단하더군.

패밀리어 마법이군. 내심 중얼거린 나는 내색하지 않고 혀를 찼다.

“이거 몰카충 새끼였네. 혹시 우리 집 화장실에 설치해 둔 건 아니지?”

- 몰카충이라, 뜻 모를 소리를 하는구나. 인간이여.

“하긴. 화장실 몰카로 봤으면 이미 놀라서 소멸했겠지. 내 거대한 블랙 아나콘다의 눈을 보고 살아남은 놈은 없으니까.”

- 바실리스크(Basilisk)를 말하는 것인가?

바실리스크라면 눈을 마주치는 것만으로도 석화(石化)의 저주를 내린다는 신화 속 괴수다.

대격변 당시에 딱 한 번 모습을 나타냈던 네임드 몬스터이기도 했다.

“뭐, 비슷하지.”

적어도 놀라서 굳어 버린다는 건 마찬가지 아닐까.

하지만 내 대답을 들은 아크 리치의 반응은 예상 밖이었다.

- 그것 때문이로군. 왠지 모르게 네가 익숙하게 느껴지는 이유가.

“뭐?”

- 너, 인간이여. 네게서 죽음의 기운이 느껴진다. 짙고 어두운, 나와 같은 기운이.

“……!”

나는 내심 놀랐다. 아크 리치가 말하는 죽음의 기운이 무엇을 뜻하는지 알 것 같았기 때문이었다.

놈의 한 마디, 한 마디마다 동요를 감추지 못하고 있는 어떤 존재.

‘스켈레톤 워로드.’

아무리 네임드 몬스터라 해도 스켈레톤 워로드 역시 언데드다.

그동안 녀석과 함께하며 내 몸에 밴 냄새를 맡은 걸까, 아니면 인벤토리라는 또 다른 미지의 공간마저 꿰뚫어 본 걸까.

만약 후자라면…… 놈의 능력은 어디까지일까.

나는 [기감]을 일으켰다. 시스템 알림과 함께 푸른 선이 하늘 위로 솟구쳐 올라간다.

동시에 해골 사이로 일렁이던 아크 리치의 안광이 초승달처럼 휘었다.

- 재미있구나.

그리고 다음 순간. 아크 리치의 전신으로부터 뻗어나온 검은 마력이 푸른 선을 후려쳤다.

삐빅!



- [???]이 강력하고도 알 수 없는 힘으로 자신을 보호합니다!

- [기감]이 실패했습니다! 지정한 대상을 파악할 수 없습니다!



설마 했지만, 역시나.

얼굴이 굳은 나를 굽어보던 아크 리치가 낮은 웃음을 흘렸다.

- 흥미로운 인간이로군. 진심으로. 어쩌면…… 내 짐작이 맞을지도 모르겠어.

“무슨 짐작. 네가 곧 뒤질 거라는 짐작?”

- 그런 일은 일어나지 않을 것이다. 나는 모든 언데드의 군주. 저 나약하고도 멍청한 인간들과는 다르니.

아크 리치는 검은 광택으로 이루어진 손을 들어 숨이 끊긴 우헤이싱과, 검은 잿가루로 변한 이정룡을 가리켰다.

- 아주 재미있는 광경이었다. 서로를 죽고 죽이는 모습을 보며 실로 오랜만에 커다란 기쁨을 느낄 수 있었다. 인간이 얼마나 하찮은 생물인지 알 수 있게 도와준 네게 감사를 표하마.

“꺼져.”

- 분노는 인간을 강하게 만들지. 너도 그러한가?

스아아아.

사방을 가득 메우고 있던 안개가 살아 있는 생물처럼 움직였다. 마치 누군가가 허공에 그려 내는 그림처럼, 안개는 어떤 풍경과 형상을 만들어 냈다.

폐허가 된 도시. 핏물이 강을 이루고 시체가 산처럼 쌓인 참혹한 전장의 중심에서, 검을 지팡이 삼아 일어나는 한 사내.

단 한 번 보았을 뿐이지만 잊을 수 없는 얼굴이었다. 아크 리치의 나직한 목소리가 허공으로부터 울려 퍼졌다.

- 레이페이. 분명 그런 이름이었지.

“……!”

- 크고 빛나는 영혼을 가진 자였다. 멀리서 지켜보는 것만으로도 탐이 날 만큼 눈부셨지.

이어지는 작은 손짓에 안개가 스르륵 움직이며 새로운 장면을 그려냈다.

아크 리치를 향해 비틀거리는 발걸음을 옮기는 레이페이, 미처 닿지 못한 채 무릎을 꿇는 레이페이, 분노와 원통함이 서린 얼굴로 하늘을 노려보며 숨을 거둔 레이페이.

그리고…… 아크 리치에 의해 타락한 존재로 거듭나 새로운 주인에게 무릎을 꿇는 레이페이.

아니, 데스나이트 로드.

스아아아.

어디선가 불어온 바람에 안개가 흩어졌다. 아크 리치는 느릿하게 말을 이었다.

- 알고 있나? 고결한 영혼을 지닌 인간은 타락했을 때 더 큰 힘을 발휘한다는 것을. 정말이지 최고의 재료였는데…… 아쉽지만 썩 나쁘지만은 않게 되었어.

나는 천천히 고개를 끄덕였다.

“계속 지껄여 봐.”

- 새로운 재료를 만나게 되었으니까. 더욱 강하고, 거대한 영혼을 지닌 너, 인간이여!

서늘한 음성이 천둥처럼 울려 퍼진다. 아크 리치의 전신으로부터 흘러나온 마력이 먹구름처럼 하늘을 가리고 도시를 어둡게 물들였다.

그리고 그 모든 것들의 중심에 있는, 불길한 태양처럼 타오르는 붉은 안광.

말없이 선 채 그 광경을 바라보던 나는 문득 입을 열었다.

“그래, 그래서…… 이제 다 지껄였냐?”

뱃속이 뜨겁다. 놈을 만나기 전까지 쌓아 두고 억눌렀던 분노가 고개를 든다.

화산지대의 용암처럼 울컥 솟구친다.

“하고 싶은 말 다 지껄였으면…….”

머릿속에서 뚝. 하고 무엇인가가 끊어지는 소리가 났다.

결사대를 이끌며 겪은 수 시간의 전투와, 이정룡과 우헤이싱을 상대하며 쌓였던 정신적인 피로마저 이 순간만큼은 잊을 수 있었다.

“이제 내려와. 이 씨벌놈아.”

앞서 울려 퍼진 아크 리치의 목소리가 천둥이었다면, 내 외침은 용암이었다.

활화산처럼 들끓는 수백 개의 혈도를 타고 화룡이 내달렸다. 백염의 투명한 창날을 뒤덮은 푸른 화염이 초고온의 열기를 내뿜었다.

그리고 다음 순간.

쐐애애애애액! 퍼엉!

온 힘을 다해 쏘아 보낸 불의 창이, 마력으로 이루어진 먹구름을 터트리고 어둠을 찢었다.



* * *



쿠구구구궁! 화악!

땅을 뒤흔드는 진동과 함께, 눈부시도록 푸른 불꽃이 하늘을 수놓았다.

수 킬로미터 밖에서 치열한 접전을 벌이고 있던 인간과 몬스터는 순간 자신들의 상황조차 잊은 채, 멍하니 그 광경을 지켜보았다.

- 크르르륵.

“저건…….”

짙은 안개에 휩싸인 거대한 도시에서 터져 나온 빛은 어떤 것보다 따스했고, 눈이 부셨다.

적어도 우뚝 선 채 도시를 바라보는 한 사람. 최민우에게는 그랬다.

‘진태경 씨.’

그다. 바로 그였다.

진태경을 제외한 누구도 떠오르지 않았다. 그는 살아 있었고, 아크 리치와 전투를 치르고 있다.

아니, 어쩌면 또 다른 누군가와.

‘이정룡. 우헤이싱.’

다른 사람들은 섣부른 우려이며 누명이라 하겠지만, 최민우는 사람이 얼마나 악해질 수 있는지 알고 있었다.

적어도 그가 겪은 이정룡이라는 사람은 그랬다.

그리고 동시에…… 진태경이라는 사람에 대해서도, 잘 알고 있었다.

‘당신은 강합니다. 제가 아는 누구보다.’

언젠가 그는 진태경에게 그렇게 말을 건넸다.

누군가는 비웃겠지만, 최민우는 진심이었다.

그 어떤 S급 헌터도, 심지어 자신의 외할아버지이자 마왕 아스모데우스를 쓰러트린 천태민조차 진태경보다 강할 수는 없다고 생각했다.

그건 실력의 문제가 아니었고, 누구의 오러가 더 크고 강하느냐의 영역은 더더욱 아니었다.

그것은 오직 진태경을 겪은 이들만이 간직한 무언가였다.

‘믿음.’

진태경은 최민우에게 믿음을 주었다.

인류를 구한 영웅인 천태민은 부모를 잃은 어린 손자를 관심 밖으로 밀어냈지만, 진태경은 아니었다.

부와 명예를 속삭이는 주변의 유혹을 뿌리치고 평화 길드에 남아 주었고, 어떤 위험 속에서도 자신의 사람들을 지켰다.

그 상대가 누구라 할지라도.



‘상대는 아레스 길드예요. 위험한 길이 될 겁니다.’

‘내가 또 가시밭길 전문이라.’

‘지금까지와는 비교도 되지 않을 만큼이요.’

‘팀장님.’

‘네?’

‘가끔은 솔직해져도 괜찮습니다.’

‘……!’



처음이었다. 그런 말을 해 준 사람은.

어린 시절부터 늘 곁에 있던 김 집사는 사려 깊고 따뜻한 사람이었으나, 확신을 주지는 못했다.

그렇기에 최민우는 용기 내어 말할 수 있었다.



‘계속……평화 길드와 함께해 주시겠습니까?’

‘그래, 그거지.’



씩 웃던 진태경의 모습을 잊지 못한다. 계약서라고 부르는 종이 몇 장으로 이어진 길드원이 아닌, ‘우리’라고 말할 수 있는 사람들을 얻은 그 날을.

‘이런 것이었나.’

늘 혼자였다. 고립되었고 외로웠다. 아주 오래된 기억에서부터 그는 모든 것에서 동떨어져 있었다.

어린 시절 만난 아이들은 그를 경계했고, 어른들은 수군거렸다.

상처를 받았지만 내색하지 않았다. 나이든 김 집사만이 속을 터놓을 수 있는 유일한 상대였다.

하지만 이제는 아니다. 최민우는 문득 입가에 미소를 띄웠다.

저 멀리, 짙은 안개와 어둠을 뚫고 피어오르는 불꽃을 바라보며 다시금 검을 쥐었다.

서걱!

눈부신 오러와 함께 몬스터의 몸뚱어리가 쪼개졌다.

짧은 순간 내려앉았던 정적과 고요가 깨짐과 동시에, 최민우의 입술 사이로 거대한 외침이 터져 나왔다.

“쳐라-!”

검을 치켜들며 몬스터를 향해 달려나가는 그의 모습은, 수십 년 전 이정룡이 보았던 누군가와 닮아 있었다.
```

## Final English reading copy

```markdown
# Chapter 420

What did people feel when they first encountered a monster?

Surprise, terror, fear, confusion?

I had no idea. It happened before I was born—or, if you wanted to be technical, back when I was on my father’s side rather than inside my mother’s womb.

But those who had stood at the scene of that history must have thought of the countless legends and myths passed down from ancient times.

Just as I was now.

*Demon.*

That was the word that flashed through my mind the instant I saw it. A massive body reaching three meters tall. Bones covered in a black sheen. A shape resembling a human’s, yet fundamentally something else.

*Fwoooosh.*

Like the wings of a demon from mythology, the robe draped over its body fluttered like a living creature.

A demon that darkened the world simply by appearing—or rather, the Arch Lich’s red eyes cast an eerie light.

“Human.”

Just one word.

The air around me trembled. From inside my inventory, the Skeleton Warlord muttered like a groan.

“The lord of the undead…”

His voice was steeped in fear. The law of power applied to monsters, too.

Yes. Just as the Skeleton Warlord had said, the Arch Lich was likely the lord of every undead monster in existence.

“Human. It is not too late. Even now…”

Instead of answering, I gave a small nod.

The Skeleton Warlord was right. It was not too late, and I still had more than enough opportunity left.

*An opportunity to stop that bastard, that is.*

If this enormous metropolis transformed into a single Gate, there would truly be no turning back.

Countless undead monsters would spread like a plague, and the Arch Lich’s power would grow even stronger.

*Now or never.*

After taking a deep breath, I extended my hand. The shaft of White Flame, pulled toward me with Seizing an Object Through Empty Space, landed in my grasp.

I stepped over the piles of collapsed concrete and trudged outside. A ruined wasteland filled with nothing but thick fog awaited me.

Up and down. Left and right.

No matter where I looked, there was no sign of a monster.

Ah, scratch that. There was one.

“Nice to meet you, you fucking bastard.”

More than twenty meters above me, the Arch Lich stood on empty air and looked down. Its red eyes gleamed.

“So it’s true. You know the language of the Demon Realm. I did not mishear you.”

“I studied hard. But you know me, don’t you?”

“I am an entity with hundreds of eyes and ears. I have watched you all along, human.”

I frowned.

“All along?”

“Yes. Your performance on the battlefield was remarkable.”

*A Familiar spell.*

I muttered inwardly but did not let it show. Instead, I clicked my tongue.

“So you’re a hidden-camera creep. You didn’t install one in my bathroom, did you?”

“A hidden-camera creep? You speak nonsense, human.”

“True. If you’d seen me through a hidden camera in my bathroom, you would’ve vanished from shock already. No one has ever survived looking my enormous black anaconda in the eye.”

“Do you mean a Basilisk?”

A Basilisk was a monster from mythology that inflicted a petrification curse simply by making eye contact.

It was also a Named Monster that had appeared exactly once during the Great Cataclysm.

“Something like that.”

At least the part about being so startled that you froze was the same, right?

But the Arch Lich’s response to my answer was unexpected.

“So that is the reason. The reason you feel strangely familiar to me.”

“What?”

“Human. I sense the energy of death from you. A dense, dark energy like my own.”

“…”

I was secretly startled. I thought I knew what the Arch Lich meant by the energy of death.

There was someone who could not hide his agitation at every word the creature spoke.

*The Skeleton Warlord.*

No matter how powerful a Named Monster he was, the Skeleton Warlord was still undead.

Had the Arch Lich caught the scent that had seeped into my body from spending so much time with him? Or had it seen through even that other unknown space called an inventory?

If the latter was true…

*How far do that bastard’s abilities reach?*

I activated Qi Sense. Along with a System notification, a blue line shot up into the sky.

At the same time, the Arch Lich’s red eyes, flickering between its bones, curved like crescent moons.

“How interesting.”

In the next instant, black mana shot from the Arch Lich’s entire body and lashed against the blue line.

*Beep!*

> **System**
>
> - **???** protects itself with a powerful, incomprehensible force!
> - **Qi Sense** failed! Unable to determine the designated target!

I’d had a feeling, and sure enough.

The Arch Lich looked down at my stiffened face and let out a low laugh.

“What an interesting human. Truly. Perhaps… my guess is correct after all.”

“What guess? The guess that you’re about to die?”

“That will not happen. I am the lord of all undead. I am different from those weak and foolish humans.”

The Arch Lich raised a hand made of black, glossy bone and pointed toward Wu Heixing, whose breath had stopped, and Lee Jungryong, who had been reduced to black ash.

“It was a most entertaining sight. Watching you humans kill one another brought me immense joy for the first time in a very long while. I thank you for helping me understand how insignificant humans are.”

“Get lost.”

“Anger makes humans stronger. Is that true of you as well?”

*Fwoooosh.*

The fog filling every direction began to move like a living creature. As though someone were drawing in empty space, it formed a scene and shape.

A ruined city.

At the center of a horrific battlefield where rivers of blood flowed and corpses piled up like mountains, a man was rising with his sword as a cane.

I had seen his face only once, but I could not forget it.

The Arch Lich’s low voice echoed through the air.

“Lei Fei. That was certainly his name.”

“…”

“He possessed a great, radiant soul. He was so dazzling that I coveted him simply by watching from afar.”

With another small gesture, the fog shifted and painted a new scene.

Lei Fei staggering toward the Arch Lich.

Lei Fei dropping to his knees before he could reach it.

Lei Fei glaring at the sky with a face filled with rage and resentment as he breathed his last.

And then…

Lei Fei reborn as a corrupted being by the Arch Lich, kneeling before his new master.

No.

The Death Knight Lord.

*Fwoooosh.*

A wind blew from somewhere, scattering the fog. The Arch Lich continued slowly.

“Do you know? Humans with noble souls wield even greater power after they fall. He truly was the finest material… It was unfortunate, but he did not turn out so badly.”

I slowly nodded.

“Keep talking.”

“I have found new material. You, human—with an even stronger and more massive soul!”

The chilling voice thundered through the air.

Mana flowed from the Arch Lich’s entire body, covering the sky like dark storm clouds and staining the city in darkness.

At the center of it all, its red eyes burned like an ominous sun.

I stood silently and watched the scene. Then I suddenly opened my mouth.

“Yeah, so… are you done talking now?”

My stomach was burning.

The anger I had been storing up and suppressing until I met the Arch Lich was rising to the surface.

It surged like lava in a volcanic region.

“If you’ve said everything you wanted to say…”

Something snapped in my head.

The hours of battle I had endured while leading the suicide squad, along with the mental fatigue that had built up while fighting Lee Jungryong and Wu Heixing, vanished from my mind in that instant.

“Then get down here, you fucking bastard.”

If the Arch Lich’s voice had been thunder, my shout was lava.

A fire dragon raced along the hundreds of acupoints boiling like an active volcano. Blue flames covered White Flame’s transparent spearhead, radiating heat of unimaginable intensity.

And then—

*Shweeeeeek! Boom!*

The spear of flame I launched with all my strength blew apart the dark clouds of mana and tore through the darkness.

* * *

*Rumble-rumble-rumble! Fwoom!*

Along with a vibration that shook the earth, dazzling blue flames spread across the sky.

Several kilometers away, the humans and monsters locked in a fierce battle momentarily forgot even their own circumstances and stared blankly at the spectacle.

“Grrrrr…”

“What is that…?”

The light that burst from the enormous city shrouded in thick fog was warmer and more dazzling than anything else.

At least, that was how it seemed to one man standing tall and gazing at the city.

Choi Minwoo.

*Mr. Jin.*

There was no one else it could be.

Jin Taekyung was alive, and he was fighting the Arch Lich.

No. Perhaps he was fighting someone else, too.

*Lee Jungryong. Wu Heixing.*

Others might call his concern premature and his suspicions a false accusation, but Choi Minwoo knew how evil a person could become.

At least, that was what the Lee Jungryong he had known had been like.

And at the same time…

He knew Jin Taekyung well, too.

*You’re strong. Stronger than anyone I know.*

Choi Minwoo had said those words to Jin Taekyung once.

Some people might have laughed at him, but Choi Minwoo had been sincere.

He believed that no S-rank Hunter—not even Cheon Taemin, his maternal grandfather and the man who had defeated the Demon King Asmodeus—could be stronger than Jin Taekyung.

It was not a matter of skill. Nor was it even a question of whose aura was greater or stronger.

It was something possessed only by those who had experienced Jin Taekyung.

*Faith.*

Jin Taekyung had given Choi Minwoo faith.

Cheon Taemin, the hero who had saved humanity, had turned away from his young grandson after the boy lost his parents.

Jin Taekyung had not.

He had rejected the temptations around him that whispered of wealth and honor, remained with the Peace Guild, and protected his people no matter what danger they faced.

No matter who stood against him.

*“Our opponent is the Ares Guild. It’ll be a dangerous road.”*

*“I’m something of a specialist in thorny roads.”*

*“A road more dangerous than anything we’ve faced so far.”*

*“Team Leader.”*

*“Yes?”*

*“Sometimes it’s okay to be honest.”*

*“…”*

It was the first time.

No one had ever said anything like that to him before.

Butler Kim, who had always been by his side since childhood, was thoughtful and warm, but he had never given Choi Minwoo that certainty.

Jin Taekyung had, and that gave Choi Minwoo the courage to speak.

*“Will you… continue staying with the Peace Guild?”*

*“Yeah. That’s more like it.”*

Choi Minwoo could never forget Jin Taekyung’s crooked grin.

The day he gained people he could call *us*, rather than Guild members connected by a few sheets of paper called a contract.

*So this is what it was.*

He had always been alone.

Isolated and lonely.

From his earliest memories, he had been separated from everything around him.

The children he met as a boy were wary of him, and the adults whispered among themselves.

He had been hurt, but he never let it show. Only the aging Butler Kim had been someone he could truly confide in.

But not anymore.

Choi Minwoo suddenly smiled.

Far in the distance, he watched the flames rising through the thick fog and darkness, then gripped his sword once more.

*Shhk!*

A monster’s body split apart beneath a flash of dazzling aura.

As the brief silence and stillness that had settled over the battlefield shattered, a tremendous cry burst from Choi Minwoo’s lips.

“Attack—!”

Raising his sword and charging toward the monsters, he resembled someone Lee Jungryong had seen several decades ago.
```

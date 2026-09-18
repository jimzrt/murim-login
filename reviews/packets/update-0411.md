<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0411.txt",
      "sha256": "6b2b46d06b7dc5d3f9b518851d4f7534d9e62b4d1f72f1840d7895b222bb1ef5",
      "bytes": 13465
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "9c7cd777804aa1cfcebc4988087c55d59e8c82d9c295752982fd7f57ec4f7688",
      "bytes": 1763
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "9cc33a6438cdb1ff6a4ba404f8c88d5e83d21551fb5fbadf6255af34e9735d73",
      "bytes": 137712
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "160248ef39023dc4e0a5542fa3ba255d0b33d3b53795936e0a64b0c707011865",
      "bytes": 533
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "7f58352545299fb33fadaa7b62a2454d4da64591f91e96fe3fdf3688d93ff640",
      "bytes": 1270
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "1e7a071f6a4cd68d31802099e58a22a7d1cfd42c4624c6b9521bbdab9bf917ac",
      "bytes": 622
    },
    {
      "path": "characters/Lee Jungryong.md",
      "sha256": "15d3a937433ebd3d768f3f5bb9956fcd238f70e94669f80e5df538efe2903b13",
      "bytes": 1163
    },
    {
      "path": "characters/Lei Fei.md",
      "sha256": "fd2b73610bde0f835719c02c2b9763ebbec3c3a253f7a5a513d3ce72457ca42b",
      "bytes": 893
    },
    {
      "path": "characters/Wu Heixing.md",
      "sha256": "4b4ee5075aa895f64ef8e99ab4867db10e143ee6f2bf3da4f351bd47cfdeb501",
      "bytes": 735
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "b2ad3c0d3ec88712e56d0d7ba9542c100bc5db95318ed88cbfd33dc8aad04840",
      "bytes": 123819
    }
  ],
  "estimated_tokens": 10389
}
-->

# Durable State Update — Chapter 411

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 411. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 411. Profile updates may replace only one
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
  "chapter": 411,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 411,
    "continuity_sources": [411],
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
    "The battle for Suining City is underway as allied Hunters and soldiers attack through fog filled with monsters.",
    "The Arch Lich's fog is a strengthening magic that Darkens monsters within its range.",
    "Monsters on the battlefield are stronger than ordinary Gate monsters, from goblins through A-rank species.",
    "Jin Taekyung is advancing toward the Arch Lich with a suicide squad and clearing its path.",
    "Lee Jungryong regards Jin Taekyung as the crack threatening the order he has built and seeks to seal it before collapse.",
    "Lee Jungryong and Go Jun are leading Ares Guild elites and Chinese Hunters into the assault.",
    "Jin Taekyung rescued and healed Burdian, a frontline B-rank Hunter, and ordered him to survive by fighting weaker monsters.",
    "Jin Taekyung has recently leveled up, restoring fatigue and some injuries.",
    "The Skeleton Warlord remains Jin Taekyung's captive undead commander."
  ],
  "continuity_sources": [
    410
  ],
  "open_questions": [
    "Who is Lei Fei's unidentified lord, what is the lord's origin, and how does the lord relate to the Arch Lich's objective?",
    "What happened to the Second Fiend assigned to the Qingcheng attack?",
    "Why has the Arch Lich withheld itself from the war, and what is it preparing now?",
    "What kind of being was the Skeleton Warlord before it became an undead commander?",
    "What specific situation will allow Jin to draw out Hero's Power more strongly?"
  ],
  "safe_through": 410,
  "temporary_decisions": [
    "Render 어둠에 물든 as Darkened.",
    "Render 강기 as Force.",
    "Render 결사대 as suicide squad.",
    "Render 빵즈 as bangzi.",
    "Render 빵셔틀 as run bread."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 이정룡    | **Lee Jungryong** |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 돌파     | **break through** / **breakthrough**             | Realm advancement                                     |
| 상태               | **Status**                     |
| 레벨               | **Level**                      |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 팀장      | **Team Leader**       |
| 마법사     | **mage**              |
| 귀가      | **your family**                                                 |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 레이페이 | **Lei Fei** | Concealed Chinese S-rank Hunter and head of the Public Security Armed Forces Department in Sichuan Province. |
| 우헤이싱 | **Wu Heixing** | Chinese S-rank Hunter who provokes Jin and nearly draws his sword. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 패밀리어 | **Familiar** | System classification for the flies detected in Taekyung's home. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 오우거 | **ogre** | B-rank monster species emerging from the Gate. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 트롤 | **Troll** | Monster species with extraordinary regenerative ability. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 존슨 | **Johnson** | Co-host of the American talk show that replays Taekyung's viral interview. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 창룡후 | **azure dragon's roar** | Battle cry released by Tang Jinhu. |
| 배리어 | **Barrier** | Team Leader Choi's protective spell. |
| 데스나이트 | **Death Knight** | Undead commander type serving under the Black Knight. |

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
| 데스나이트 | 인간 | enemy combatants | human | contemptuous and commanding | Used in the Death Knight's warnings to Jin. |
| 데스나이트 | 로드 | subordinate to commanding lord | Lord | fearful and deferential | The Death Knight calls to the Death Knight Lord after Jin overwhelms the army. |
| 진태경 | 레이페이 | former ally and fellow Hunter | Lei Fei | blunt and solemn | Jin addresses Lei Fei by name before telling him to rest. |
| 레이페이 | 진태경 | former ally and fellow Hunter | you | familiar and respectful | Lei Fei uses 자네 and 하게 while asking Jin to help him fulfill his final mission. |
| 진태경 | 우헤이싱 | adversarial S-rank Hunters | you idiot | insulting-casual | Mocks Wu's cowardice and orders him to stop complaining. |
| 이정룡 | 우헤이싱 | senior S-rank Hunter to younger allied S-rank Hunter | Mr. Wu | polished and formally coaxing | Lee publicly draws Wu into agreement with the suicide-squad plan. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 410
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who has sworn never to kill again.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 410
- **Aliases:** Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, and a Supreme Peak master who has manifested Force and crossed the wall into true mastery.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and student, his mother and sister Hayeon are among those he protects, and the Skeleton Warlord is his captive undead commander.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 410
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Lee Jungryong.md

# Lee Jungryong (이정룡)

- **Safe through:** Chapter 410
- **Aliases:** None
- **Role:** Vice Guild Master of Ares Guild, one of Korea's two S-rank Hunters, and a Supreme Peak-level martial artist who directs Ares Guild operations.
- **Personality:** Outwardly genial, calm, and humorous; calculating, manipulative, coercive, and ruthless when challenged
- **Voice:** Smooth, good-natured, and indirect, using teasing conversation and veiled threats before becoming openly furious
- **Relationships:** Master of Park Jihoon and Go Jun (Team Leader Seok), whom he personally selected and trained; longtime Great Cataclysm acquaintance of Park Tae Seop; adversary of Jin Taekyung; knew Team Leader Choi from childhood; has an antagonistic history with Kim Hwajong, who saved his life at the collapse of Mapo Bridge eighteen years earlier; was visibly shaken by learning that Choi is Cheon Taemin's maternal grandson; regards Cheon Taemin as an older brother despite no blood relation and has long held him in respect and fear; operates as Ares Guild's senior authority beneath its Guild Master

### Lei Fei.md

# Lei Fei (레이페이)

- **Safe through:** Chapter 404
- **Aliases:** None
- **Role:** Lei Fei is a concealed Chinese S-rank Hunter and former head of the Public Security Armed Forces Department in Sichuan Province who recovered his human identity after becoming a level-120 undead Death Knight Lord and died fulfilling his final mission.
- **Personality:** Lei Fei's recovered memories show him as dutiful, honorable, family-oriented, and willing to serve as an unseen guardian.
- **Voice:** His human voice is formal and earnest, becoming warm and playful with family.
- **Relationships:** Wei Fenghu is his maternal uncle who raised him as a son; Lei Fei married an unnamed flower-shop owner and had a daughter, trained alongside Wu Heixing, and was corrupted by the Arch Lich before Jin Taekyung restored his identity.

### Wu Heixing.md

# Wu Heixing (우헤이싱)

- **Safe through:** Chapter 409
- **Aliases:** None
- **Role:** Wu Heixing is a Chinese S-rank Hunter known for frequent media exposure and scandal who secretly practices martial arts, including an internal-energy cultivation technique and fist-and-foot martial arts.
- **Personality:** Arrogant, status-conscious, abusive, and fiercely proud of his power, he responds to humiliation with anger, jealousy, and fear.
- **Voice:** Loud, insulting, entitled, and dependent on national and political status.
- **Relationships:** He is openly hostile toward Jin Taekyung and Faye Chen, and resents Jin receiving Chairman Shao Yang's attention.

## Korean source

```text
＃411화



순간, 세상이 멈춘 듯했다.

뇌가 상황을 이해하는 것보다 본능이 먼저 반응했다.

사람들의 호흡과 몬스터가 토해 내는 괴성이 수 킬로미터 밖에서 들리는 것처럼 멀어지고, 어느 때보다 날 선 감각이 주위의 모든 정보를 받아들였다.

솨아아아.

허공에서 느릿느릿 흩뿌려지는 핏방울과 흙, 먼지. 손을 뻗으면 잡힐 듯한 안개.

그리고…….

‘기(氣).’

느껴졌다. 반경 수백 미터를 에워싼 막대한 기의 움직임이. 머릿속에서 붉은 경종이 울림과 동시에, 나는 지면을 박차고 솟구쳤다.

“피해-!”

꽈아아아앙!

번쩍이는 섬광에 이어 거대한 굉음이 천지를 울렸다. 나는 10여 미터 상공에서 전장을 굽어보았다.

불과 몇 초 전, 내가 서 있던 자리를 중심으로 반경 수백여 미터가 초토화되어 있었다.

사라지지 않은 안개와 피어오른 먼지구름 사이로 지면을 뒤덮은 녹색 핏물과 산산 조각난 몬스터의 사체가 보였다.

‘매직 트랩(Magic Trap).’

모습을 드러내지 않는 적을 상대한다는 것은, 일어날 수 있는 모든 상황에 대비해야 한다는 뜻이다.

‘전쟁에는 인정(人情)이 없으니까.’

인류 역사에 기록된 수많은 전쟁사가 증인이고 검사이며 판사다.

같은 인간들끼리도 전쟁 중에는 온갖 끔찍한 만행을 저지르는데, 하물며 인간도 아닌 몬스터에게 인정이라는 잣대를 들이미는 건 우스운 일이다.

그렇기에 경계심은 전쟁에 있어 필수 덕목이다. 적이 파놓은 함정에 빠질 확률을 줄여 주고, 희생을 최소화할 수 있다.

바로 지금처럼.

타닥.

사뿐히 지면에 내려앉은 나는 손을 뻗었다. 파앙! 압축된 공기가 터져 나가며 먼지구름이 흩어진다.

사방을 가득 메운 핏물과 사체들 사이, 익숙한 얼굴들이 비로소 모습을 드러냈다.

“최 팀장님.”

깊이 심호흡한 최 팀장이 고개를 끄덕였다. 그의 등 뒤로 혼비백산한 얼굴의 결사대 이백여 명이 보였다.

“부상자는 몇 있지만…… 전부 무사합니다.”

“다행이네요.”

“어마어마한 위력의 트랩이었습니다. 이게 없었다면 아마 절 포함한 대부분이 죽었을지도 몰라요.”

스윽, 우우웅.

최 팀장이 손을 내밀어 눈 앞에 펼쳐진 투명한 막을 건드렸다.

그를 포함한 결사대 전원을 감싼 그것은, 수십억 명의 인구 중 세 손가락 안에 꼽히는 대마법사가 스크롤에 한 땀, 한 땀 새겨 넣은 배리어(Barrier) 마법이었다.

“전투가 끝나면 가장 먼저 미스터 존슨을 찾아야겠군요. 그의 마법 덕분에 목숨을 건졌으니.”

“감사의 키스라도 해 주시려고?”

“지금 마음 같아서는 뭘 못 하겠습니까.”

샤오 쉔이 참았던 숨을 토해 내며 최 팀장의 말을 받았다.

「저는 그 이상도 가능합니다. 이건 정말이지…….」

녀석은 말을 잇지 못하고 주위를 둘러봤다.

방금의 폭발은 그만큼 엄청났고, 그 여파로 인해 어림잡아도 천 마리 이상의 몬스터가 죽거나 전투 불능 상태에 빠졌다.

적아(敵我)를 가리지 않는 함정. 아크 리치는 나와 결사대를 잡기 위해 수많은 부하를 장작으로 던져 넣은 것이다.

‘이 새끼 봐라…….’

어느 정도는 예상했지만, 아크 리치의 교활함과 과감함은 생각했던 것 이상이었다.

내 신호가 조금이라도 늦었다면, 그리고 앞서 길을 뚫으며 미끼를 자처하지 않았더라면 결사대 전원이 이곳에서 뼈를 묻어야 했을 거다.

‘바로 그날처럼 말이지.’

평생 잊지 못할 기억. 두 번 다시 그런 비극이 일어나서는 안 된다.

나는 돌아서며 말했다.

“거리를 유지하면서 따라오세요. 우리의 목적은 몬스터를 상대하는 것이 아니라, 놈들을 돌파하는 겁니다.”

결사대는 우렁찬 함성으로 대답을 대신했다. 난데없이 일어난 폭발에 상당수의 아군을 잃고 혼란스러워하던 몬스터 군단이 주춤거리며 물러난다.

위기가 기회로 바뀌는 순간. 지금의 흐름을 놓쳐서는 안 된다.

“돌격-!”

나는 공력을 실은 창룡후(蒼龍吼)와 함께 쏘아졌다. 서걱, 뒷걸음질 치는 몬스터의 목이 허공으로 솟구친다.

폭발의 여파로 공백이 생긴 몬스터 군단을 향해, 이백의 결사대가 송곳처럼 파고들었다. 후방의 본대가 그 뒤를 따라 파도처럼 짓쳐 들었다.

와아아아아아-!

전장을 떨어 울리는 먹먹한 함성. 안개 사이로 퍼져 나가는 녹색 핏물.

그리고 까마득한 상공을 맴돌며 전장을 내려다보는 한 무리의 까마귀 떼가 있었다.



* * *



백골로 만들어진 왕좌 위, 마치 잠든 것처럼 앉아 있던 존재가 불현듯 눈을 떴다.

텅 빈 해골의 동공에서 강렬한 안광이 솟구침과 동시에 나직한 뇌까림이 흘러나왔다.

- 제법이군.

아크 리치에게는 수백 개의 눈과 귀가 있다.

지금, 이 순간에도 전장 곳곳에 배치해 둔 패밀리어(Familiar)는 모든 상황을 빠짐없이 읽어 내고 있었다.

치열한 접전을 벌이는 인간과 몬스터. 그리고 빠른 속도로 돌파해 나가는 인간들의 무리 역시.

‘결사대. 분명 그렇게 불렀었나.’

아크 리치는 문득 한 가지 기억을 떠올렸다. 낡고 케케묵은 기억. 죽음의 강에 잠겨 억겁에 가까운 시간을 보내면서도 잊지 못한, 아니 잊을 수 없었던 기억이다.

‘대적자.’

어찌 잊을 수 있을까. 모든 것의 중심에 있었던 한 인간을. 대적자와 함께 죽음을 무릅쓰고 돌격해 오던 인간들의 결사대를.

‘내 몸에 검을 박아 넣은 것도 놈이었지.’

아크 리치는 칠흑색 뼈로 이루어진 자신의 몸을 바라보았다.

과거의 그는 언데드와 같은 하찮은 존재가 아니었다. 왕의 신임을 받으며 셀 수도 없이 무수한 몬스터를 휘하에 둔 고귀하고도 강대한 존재였다.

그러나 최후의 전투가 벌어지던 날, 그 역시 왕과 함께 쓰러지고 말았다. 그것도 한낱 인간의 손에 의해.

- 그런데…… 대적자는 어디에 있지?

아크 리치는 의문에 찬 목소리를 흘렸다.

패밀리어를 이용해 모든 전선을 살폈건만, 응당 나타나야 할 대적자의 모습은 보이지 않았다. 기억 속에 남은 인간 몇몇을 발견하긴 했지만 그뿐이었다.

‘혹시?’

순간, 무언가를 떠올린 아크 리치의 안광이 거세게 타올랐다.

도저히 믿기지 않지만. 만약, 만약 대적자가 죽었다면. 필멸자의 운명을 맞이했다면?

- 크하, 크하하하!

석상처럼 굳어 있던 몸이 들썩였다. 마력이 담긴 웃음소리에 지면이 흔들리고 대기가 부르르 떨렸다.

주인의 심경에 모종의 변화가 생겼음을 알아차린 호위대가 엎드려 부복했다.

- 군주시여.

- 어찌하여 그러시옵니까.

호위대의 면면은 화려했다. 하나하나가 네임드 몬스터에 버금간다는 데스나이트(Death Knight). 그리고 로브를 깊게 눌러쓴 리치(Lich)의 숫자를 모두 합하면 스물에 달했다.

대적자를 상대하기 위해 만들어 낸 창조물들. 하지만 이제는 생각이 달라졌다.

환희에 찬 웃음을 터트리던 아크 리치가 마침내 입을 열었다.

- 들어라. 내 충실한 종들아.

- 명하시옵소서.

자리에서 일어난 아크 리치가 자신의 충성스러운 신하들을 굽어보았다. 이내 스산한 목소리가 공간을 울렸다.

- 전장으로 가거라. 저 하찮은 인간들을 짓밟고, 쓸어 버려라.

스물의 데스나이트와 리치들은 조금의 의심도 없이 고개를 숙였다.

아크 리치는 이 자리에 있는 모든 언데드의 군주. 그의 명령을 따르는 것에 있어 한 치의 망설임도 있을 수 없었다.

- 군주의 명을 받드옵니다.

한목소리로 대답한 그들은 각자의 방향을 향해 나아갔다.

다시 텅 비어 버린 공간. 홀로 웃음을 흘리던 아크 리치는 해골 왕좌에 앉아 정신을 집중했다.

수많은 패밀리어의 눈과 귀로 전장을 살피던 그가 문득 멈칫했다.

- 그런데…… 저 인간은 도대체 무엇이지?

상공을 누비는 까마귀의 새카만 눈동자에, 피 보라를 일으키며 몬스터를 베어 가는 한 젊은 인간의 모습이 비쳤다.

과거의 기억에는 존재하지 않은 얼굴. 하지만 이미 며칠 전 패밀리어를 통해 본 적 있는 얼굴이다.

- 데스나이트 로드를 쓰러트린 그 인간이로군.

레이페이를 재료로 만들어진 데스나이트 로드는 아크 리치가 탄생시킨 모든 것을 통틀어 최고의 역작이었다.

비록 굳건한 영혼을 지닌 탓에 완전히 복속시키지는 못했지만, 자신의 힘 일부를 직접 부여한 만큼 그 강함이야 의심할 여지가 없었다.

하지만 최고의 전력과 더불어 아까운 마력만 날리게 되었다. 저 하찮은 인간 때문에.

- 거슬리는군. 이 기회에 확실히 처리해야겠어.

제거를 결심한 아크 리치는 사념(思念)을 흘려보냈다.

각 전선으로 향하던 호위대 중 절반이 군주의 명령에 따라 방향을 틀었다.



* * *



콰드드드득!

바람, 무기, 단단하기 그지없는 몬스터의 몸뚱어리.

창날의 궤적에 걸려든 모든 것들이 베어진다.

목이 솟구치고 두꺼운 팔다리가 허공을 날았다.

아직 숨이 붙어 있던 트롤은 재생할 틈도 없이 몸이 조각났고, 반쯤 부패한 상태로 언데드가 된 오우거는 몸을 휘청이다가 뒤이어 날아든 검에 상반신이 날아갔다.

서걱! 서걱! 서걱!

[영웅의 혼]을 휘둘러 순식간에 서너 마리를 베어 버린 최 팀장이 나를 향해 고함처럼 말을 건넸다.

“진태경 씨! 몬스터의 공세가 너무 강합니다!”

그의 말은 사실이었다. 일선을 돌파하자 몬스터의 숫자는 줄어들었지만, 그에 반해 병력의 질은 더더욱 높아졌다.

‘이럴 줄 알았지.’

우리를 잡기 위한 매직 트랩의 장작으로 쓴 전방의 몬스터들은 대부분이 중, 하급에 불과했다.

아크 리치는 정예를 후방에 배치하고 그 밖의 몬스터들을 미끼인 동시에 고기 방패로 삼았다.

‘우리의 힘을 빼놓기 위해서.’

거기에 더해 아까보다 짙어진 안개 역시 전투를 어렵게 만들고 있었다.

안개의 영향으로 몬스터가 강해진 것도 문제였지만, 지금 같은 안개 속에서는 시야와 소리가 잘 전달되지 않는다.

인간보다 감각이 뛰어난 몬스터들에게 유리한 조건일 수밖에 없었다.

물론…….

‘나는 예외지.’

쐐애애액, 뻐억!

힘껏 흩뿌린 창이 예닐곱 마리의 몬스터를 꼬치처럼 꿰뚫었다.

위기를 넘긴 샤오 쉔과 결사대의 헌터가 나를 향해 눈짓으로 감사를 표한다.

“모두 내 쪽으로 뭉쳐!”

「하지만 마법 스크롤이 몇 개 남지 않았습니다. 혹시 또 매직 트랩이 발동되면…….」

“설명할 시간 없어! 긴말 말고 빨리!”

내 외침에 고개를 끄덕인 최 팀장과 샤오 쉔이 결사대와 함께 전진했다.

그들이 무슨 생각을 하는지 모르는 바는 아니지만, 우리는 지금까지 세 번의 매직 트랩을 거쳤고 이곳은 아크 리치가 정예를 모아 놓은 후방이다. 트랩이 발동할 가능성은 희박하다.

“공격 대신 방어 위주로. 전진!”

전투 자체는 어려워졌지만, 갑작스럽게 트랩에 걸릴 확률이 줄어들었으니 나로서는 마음이 가벼워진다.

내 한 몸 빼는 거야 어렵지 않지만 다른 결사대원들은 목숨이 위험해지니까.

‘마지막 목적지까지는 코앞이야. 사상자를 최대한 줄이면서 이정룡, 그리고 우헤이싱과 합류한다.’

서걱! 콰드드득!

문득 쌓여 가는 피로를 느끼며, 선봉에서 길을 뚫고 있던 그 순간이었다.

- 모.두. 물.러.나.라!

- 인간이여. 군주의 명에 따라 내 목숨을 거두겠노라.

모세의 기적처럼 좌우로 갈라지는 몬스터의 장막. 그리고 모습을 드러내는 존재들과 마주한 나는 멍하니 입을 벌렸다.



[Lv.120 어둠에 물든 리치]

[Lv.115 어둠에 물든 데스나이트]



120레벨을 넘나드는 놈들이 무려 열 마리. 순간 숨이 막히고 손발이 덜덜 떨렸다.

그런 내게 최 팀장이 절망 어린 목소리로 외쳤다.

“지금 당장 후퇴해야 합니다!”

“최, 최 팀장님.”

“정신 차리십시오, 진태경 씨!”

“도시락이 왔어요.”

“이대로 가다가는 전멸…… 예?”

나는 떨리는 눈동자로 열 마리의 몬스터, 아니 도시락을 바라보았다.

“도시락 배달이 왔어요.”

“……?”

- ……?

- ……?

물음표 치워, 이 새끼들아.

일섬 나간다.
```

## Final English reading copy

```markdown
# Chapter 411

For a moment, it felt as though the world had stopped.

My instincts reacted before my brain could process the situation.

The breathing of the people around me and the monsters’ howls receded into the distance, as if they were coming from several kilometers away. My senses, sharper than ever, took in every detail around me.

*Fwoooosh.*

Droplets of blood, dirt, and dust drifted slowly through the air. Fog hung close enough to grasp if I reached out my hand.

And then…

*Qi.*

I could feel it—the immense movement of qi surrounding an area several hundred meters in every direction. As a red alarm began blaring in my head, I kicked off the ground and shot upward.

“Get clear—!”

*Kraaa-boooom!*

A flash of light was followed by a tremendous roar that shook heaven and earth. From more than ten meters in the air, I looked down over the battlefield.

The area within a radius of several hundred meters, centered on the spot where I had been standing only a few seconds earlier, had been devastated.

Through the fog that had not yet dissipated and the clouds of dust rising from the ground, I could see green blood covering the earth and monster corpses blown to pieces.

*A Magic Trap.*

Fighting an enemy who refused to show itself meant preparing for every situation that could possibly occur.

*There’s no compassion in war.*

The countless wars recorded throughout human history were witness, prosecutor, and judge.

Even humans committed all kinds of horrific atrocities against one another during war. Expecting compassion from monsters that were not even human was laughable.

That was why vigilance was an essential virtue in war. It reduced the chances of falling into an enemy’s trap and minimized casualties.

Just like now.

*Tap.*

I landed lightly and reached out my hand.

*Bang!*

Compressed air burst outward, scattering the clouds of dust.

Among the blood and corpses filling every direction, familiar faces finally emerged.

“Team Leader Choi.”

Team Leader Choi took a deep breath and nodded. Behind him stood more than two hundred members of the suicide squad, their faces pale with terror.

“A few people are injured…but everyone’s safe.”

“That’s a relief.”

“It was an unbelievably powerful trap. Without this, most of us—including me—would probably have died.”

*Shk. Wooooong.*

Team Leader Choi reached out and touched the transparent barrier spread out before him.

It covered every member of the suicide squad, and it was a Barrier spell painstakingly engraved into a scroll by one of the top three mages among the billions of people in the world.

“When the battle is over, I should find Mr. Johnson first. His magic saved our lives.”

“Are you planning to give him a kiss as thanks?”

“If you’re asking what I feel like doing right now, there’s nothing I wouldn’t do.”

Shao Shen exhaled the breath he had been holding and joined in.

“I’m capable of more than that. This is truly…”

He could not finish and simply looked around.

The explosion had been that tremendous. In its aftermath, more than a thousand monsters had been killed or rendered incapable of fighting.

A trap that had not distinguished friend from foe. The Arch Lich had thrown countless subordinates into it as kindling to catch me and the suicide squad.

*Look at this bastard…*

I had expected as much to some extent, but the Arch Lich’s cunning and boldness went beyond anything I had imagined.

If my signal had been even slightly late, or if I had not volunteered to be bait while breaking through the path ahead, every member of the suicide squad would have been buried here.

*Just like that day.*

A memory I could never forget. A tragedy like that could never happen again.

I turned and spoke.

“Keep your distance and follow me. Our objective isn’t to fight the monsters. It’s to break through them.”

The suicide squad answered with a thunderous shout.

The monster army, confused after suddenly losing a large number of its forces in the explosion, hesitated and began to retreat.

This was the moment when a crisis became an opportunity. We could not let the momentum slip away.

“Charge!”

With an azure dragon’s roar charged with internal energy, I shot forward.

*Slash!*

The head of a retreating monster flew into the air.

The two hundred members of the suicide squad drove into the gap in the monster army like an awl. The main force in the rear followed behind them, surging forward like a wave.

“Waaaaaaaaah!”

A deafening roar shook the battlefield.

Green blood spread through the fog.

And high above, a flock of crows circled as they looked down upon the battlefield.

* * *

The being sitting atop a throne made of white bones, as if asleep, suddenly opened its eyes.

Intense light flared from the pupils of its empty skull, and a low mutter escaped its mouth.

“Not bad.”

The Arch Lich had hundreds of eyes and ears.

Even now, the Familiars placed throughout the battlefield were taking in every detail without missing a thing.

Humans and monsters locked in fierce close combat.

And the group of humans rapidly breaking through the battlefield.

*The suicide squad. That was what they called them, wasn’t it?*

The Arch Lich suddenly recalled something.

It was an old, stale memory—one it had been unable to forget despite spending an eternity submerged in the River of Death. No. One it could not forget.

*The Adversary.*

How could it forget?

A single human who had stood at the center of everything. The human suicide squad that had charged alongside the Adversary, risking death.

*That bastard was the one who drove a sword into my body.*

The Arch Lich looked down at its body, formed from pitch-black bones.

In the past, it had not been some lowly existence like an undead. It had been a noble and mighty being, trusted by a king and commanding countless monsters.

But on the day of the final battle, it had fallen alongside its king.

At the hands of a mere human, no less.

“But…where is the Adversary?”

The Arch Lich’s voice was filled with doubt.

It had surveyed every front through its Familiars, yet the Adversary, who should have appeared, was nowhere to be seen. It had found several humans from its memories, but that was all.

*Could it be?*

The Arch Lich’s eyes flared violently as it realized something.

It was impossible to believe.

But what if—what if the Adversary had died?

What if the Adversary had met the fate of a mortal?

“Kha…khahahaha!”

The body that had been rigid as a statue began to shake.

The laughter, infused with magic, made the ground tremble and the air quiver.

Realizing that something had changed in their master’s mood, the guards dropped to the ground and prostrated themselves.

“My lord.”

“Why do you laugh so?”

The honor guard was an impressive group. There were Death Knights, each comparable to a Named Monster, as well as Liches with their robes pulled deeply over their heads. Their total number came to twenty.

They were creations made to fight the Adversary.

But now, the Arch Lich’s thoughts had changed.

After laughing with delight, the Arch Lich finally spoke.

“Listen, my faithful servants.”

“Give us your command.”

The Arch Lich rose from its seat and looked down upon its loyal retainers. A chilling voice soon echoed through the space.

“Go to the battlefield. Trample those insignificant humans and wipe them out.”

The twenty Death Knights and Liches bowed without the slightest hesitation.

The Arch Lich was the lord of every undead present. When it came to obeying its commands, there was no room for even the smallest doubt.

“We shall carry out our lord’s command.”

They answered in unison and set off in their respective directions.

The space was empty once more.

The Arch Lich, laughing alone, sat down on the skeletal throne and focused its mind.

As it watched the battlefield through the eyes and ears of countless Familiars, it suddenly stopped.

“But…what in the world is that human?”

In the pitch-black eyes of a crow soaring through the sky, the image of a young human cutting through monsters amid a spray of blood was reflected.

It was a face that did not exist in the memories of the past.

But it was also a face the Arch Lich had seen through its Familiars several days earlier.

“That’s the human who defeated the Death Knight Lord.”

The Death Knight Lord, created from Lei Fei, was the Arch Lich’s finest masterpiece among everything it had ever brought into existence.

Although it had been unable to subjugate him completely because of his powerful soul, there could be no doubt about his strength. The Arch Lich had directly bestowed a portion of its own power upon him.

And yet, because of that insignificant human, it had lost its greatest asset and wasted precious mana.

“He’s irritating. I should deal with him properly while I have the chance.”

Having decided to eliminate him, the Arch Lich sent out a thought.

Half of the guards heading toward the various fronts changed direction in accordance with their master’s command.

* * *

*Kra-d-d-d-d-k!*

Wind, weapons, and the bodies of monsters harder than stone.

Everything caught in the path of the spearhead was cut apart.

Heads flew into the air, and thick limbs spun through the sky.

A Troll that was still breathing was chopped to pieces before it had a chance to regenerate. An ogre that had become undead while still half-rotten staggered, only for a sword that came flying a moment later to take off its upper body.

*Slash! Slash! Slash!*

After cutting down three or four monsters in an instant with Hero’s Soul, Team Leader Choi shouted toward me.

“Mr. Jin Taekyung! The monster assault is too strong!”

He was right. Once we broke through the front line, the number of monsters decreased, but the quality of the forces grew even higher.

*I knew it would be like this.*

The monsters in front, used as kindling for the Magic Trap meant to catch us, had mostly been mid- or low-level.

The Arch Lich had placed its elites in the rear and used the other monsters as both bait and meat shields.

*To wear down our strength.*

On top of that, the fog had grown even thicker than before, making the battle more difficult.

The monsters becoming stronger under the fog’s influence was bad enough, but in fog this thick, visibility was limited and sound did not carry well.

It was an unavoidable advantage for monsters, whose senses were superior to those of humans.

Of course…

*I’m the exception.*

*Whoooosh! Bang!*

My spear lashed out with all my strength, skewering six or seven monsters like meat on a skewer.

Shao Shen and the Hunters in the suicide squad, having escaped the crisis, gave me grateful looks.

“Everyone, group up around me!”

“But we only have a few magic scrolls left. If another Magic Trap is activated…”

“No time to explain! Stop talking and move!”

Team Leader Choi and Shao Shen nodded at my shout and advanced with the suicide squad.

I knew what they were thinking, but we had already made it through three Magic Traps, and this was the rear where the Arch Lich had gathered its elites. The chances of another trap being activated were slim.

“Focus on defense instead of attacking. Advance!”

The battle itself had become more difficult, but the reduced chance of suddenly being caught in another trap left me feeling lighter.

Pulling myself out of danger would not be difficult. But the lives of the other members of the suicide squad were at risk.

*We’re right next to our final destination. Minimize casualties and join up with Lee Jungryong and Wu Heixing.*

*Slash! Kra-d-d-d-d-k!*

I was at the front, cutting a path through the monsters, when I suddenly felt the fatigue building in my body.

“Everyone. Fall. Back!”

“Human. By my lord’s command, I shall take my own life.”

The curtain of monsters split apart to the left and right like the parting of the Red Sea.

I stared blankly, my mouth hanging open, as the beings behind it revealed themselves.

> **System**
> - **Lv. 120 Darkened Lich**
> - **Lv. 115 Darkened Death Knight**

There were ten of them, all hovering around Level 120.

For a moment, I could barely breathe, and my hands and feet began to tremble.

Team Leader Choi shouted at me in a voice filled with despair.

“We have to retreat right now!”

“T-Team Leader Choi.”

“Get a grip, Mr. Jin Taekyung!”

“The lunchbox delivery is here.”

“If we keep going like this, we’ll be wiped out…huh?”

With trembling eyes, I stared at the ten monsters.

No—the ten lunchboxes.

“The lunchbox delivery is here.”

“…?”

“…?”

“…?”

Put those question marks away, you bastards.

*One Annihilation, coming up.*
```

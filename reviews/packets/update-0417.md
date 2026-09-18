<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0417.txt",
      "sha256": "fefef3edfce1d29870714b29e3b72115d4eb7f369fce0ec4d2f188697f82389a",
      "bytes": 13275
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "2122d8647d779a7d87eb2fee90c37b8504c8cc599f36f896984627d22e41c5f0",
      "bytes": 1523
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "06dbc0dffecea43d6ec7cccbb46160d84c81f4b192288acc8c31d02e34782bf2",
      "bytes": 138985
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "76eaa74b40fa415e9993d888564083b9313bd1681fc1479b556ed4024a73fb7f",
      "bytes": 533
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "59c6f45ec00a542ae24b8dc481dcfa8a967c375657397c648579bb13d82aafaf",
      "bytes": 1270
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "f54c409185c43d65225fcd53ede6ba5a37452060bc764a5c2cbbb67b982e70d0",
      "bytes": 622
    },
    {
      "path": "characters/Lee Jungryong.md",
      "sha256": "dec50fc5c9b9a25e5ed9726061eff13b6681f98a44e03d5043d741d3431c03fd",
      "bytes": 1163
    },
    {
      "path": "characters/Lei Fei.md",
      "sha256": "5e37b6aedf8167de216a0d9d95ec929f93759403278cb06a76e10ea6394c4e60",
      "bytes": 893
    },
    {
      "path": "characters/Park Jihoon.md",
      "sha256": "f3f084d67d83dc14275ab525501ceea7e7793e8e37a17054e7bfe23a3fa78e17",
      "bytes": 1449
    },
    {
      "path": "characters/Team Leader Choi.md",
      "sha256": "eb2a713fbfdf5a5d1c1cce0f920541202f00af57f42c944d39a4f66bcd9fa270",
      "bytes": 535
    },
    {
      "path": "characters/Wu Heixing.md",
      "sha256": "7712be316e89840d0e8418eee5d2fc5e7e3541c29447afabe4415a893343262b",
      "bytes": 762
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "940557f954a71b0f703d9dc184cddc2db5445f6e50fa5b0710904f654a04fb88",
      "bytes": 128217
    }
  ],
  "estimated_tokens": 11206
}
-->

# Durable State Update — Chapter 417

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 417. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 417. Profile updates may replace only one
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
  "chapter": 417,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 417,
    "continuity_sources": [417],
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
    "Jin Taekyung, Lee Jungryong, and Wu Heixing have entered the Arch Lich's city stronghold after breaking through the monster army.",
    "The city is incompletely transforming into one enormous Gate through the Arch Lich's anchored mana.",
    "The Quest One Who Returned from Death is active, and Login is unavailable until the Quest ends.",
    "The three Hunters are moving stealthily through the fog and conserving strength to confront the Arch Lich.",
    "Jin is convinced that Lee and Wu are more interested in betraying him than confronting the Arch Lich, and Lee has stopped after hearing the accusation.",
    "The Skeleton Warlord claims Korea as his homeland and is urging Jin to turn back because of dizziness and nausea."
  ],
  "continuity_sources": [
    416,
    415
  ],
  "open_questions": [
    "Will Lee Jungryong and Wu Heixing betray Jin Taekyung inside the city?",
    "Can the three Hunters defeat the Arch Lich before the city's Gate transformation is complete?",
    "What is causing the Skeleton Warlord's dizziness and insistence that they turn back?"
  ],
  "safe_through": 416,
  "temporary_decisions": [
    "Render 아크 리치 as Arch Lich.",
    "Render 게이트화 as Gate transformation.",
    "Render 어둠에 잠식된 도시 as City Consumed by Darkness.",
    "Render 죽음에서 돌아온 자 as One Who Returned from Death.",
    "Render 포메이션 J as Formation J, with its joke explained as “Just fucking fight.”"
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 최민우    | **Choi Minwoo**   |
| 이정룡    | **Lee Jungryong** |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 혈도     | **acupoint** / **vital point**                   | Context dependent                                     |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 일격     | **One Strike**                         |
| 상태               | **Status**                     |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 레이드     | **raid**              |
| 길드      | **Guild**             |
| 팀장      | **Team Leader**       |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 레이페이 | **Lei Fei** | Concealed Chinese S-rank Hunter and head of the Public Security Armed Forces Department in Sichuan Province. |
| 박지훈 | **Park Jihoon** | Current name of Taekyung's former middle-school classmate; Hunter in Myeongdong Guild Team 1. |
| 우헤이싱 | **Wu Heixing** | Chinese S-rank Hunter who provokes Jin and nearly draws his sword. |
| 화염신장 | **Flame Divine Palm** | Jopil's deadly palm technique, noted when Taekyung compares Jopil with Mukyung. |
| 송이 | **Song-i** | Short form used for Song Song; Taekyung's love interest. |
| 태자 | **Crown Prince** | Title of the Emperor's older brother who was reportedly assassinated. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 태자당 | **Crown Prince Party** | The faction associated with General Liao. |
| 공안무력부 | **Public Security Armed Forces Department** | Chinese security organization ordered to assemble during the attack. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 박지훈 | 진태경 | former_middle_school_classmates | Taekyung | casual-familiar and teasing | Uses 태경아 and 너 while reconnecting after eleven years. |
| 진태경 | 박지훈 | former_middle_school_classmates | you | casual-familiar and teasing | Uses 너 while joking about Jihoon's wealth, appearance, and school memories. |
| 최민우 | 박지훈 | rival Guild Team Leader to hostile Guild Hunter | Hunter Park Jihoon | formal-polite and controlled | Calls Jihoon through Manager Kim’s phone after the Peace Guild captures Myeongdong personnel. |
| 이정룡 | 진태경 | senior S-rank Hunter to younger Hunter and adversary | Young man | polished, teasing, and veiled-threatening | Uses a genial tone and indirect threats while trying to make Taekyung release the captives. |
| 진태경 | 이정룡 | younger Hunter to senior S-rank Hunter and adversary | you | polite but mocking and defiant | Taekyung answers Lee's soft threats with the wolf-and-tiger metaphor and refuses to yield. |
| 박지훈 | 이정룡 | Disciple to master | Master | terrified and pleading | Jihoon cries out to Lee as Master after Taekyung begins stabbing him. |
| 이정룡 | 박지훈 | master to Disciple | Disciple | commanding, protective, and enraged | Lee restrains himself to protect Jihoon while ordering Taekyung to stop and later carries Jihoon's mutilated body. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 우헤이싱 | 진태경 | hostile S-rank Hunter to foreign Hunter and provocation target | peninsula bangzi | insulting and confrontational | Wu repeatedly addresses Jin with anti-Korean slurs. |
| 우헤이싱 | 이정룡 | younger S-rank Hunter to senior Ares Guild authority | Mr. Lee | formal and deferential | Wu addresses Lee respectfully despite his usual hostility toward Koreans. |
| 진태경 | 레이페이 | former ally and fellow Hunter | Lei Fei | blunt and solemn | Jin addresses Lei Fei by name before telling him to rest. |
| 레이페이 | 진태경 | former ally and fellow Hunter | you | familiar and respectful | Lei Fei uses 자네 and 하게 while asking Jin to help him fulfill his final mission. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 진태경 | 우헤이싱 | adversarial S-rank Hunters | you idiot | insulting-casual | Mocks Wu's cowardice and orders him to stop complaining. |
| 이정룡 | 우헤이싱 | senior S-rank Hunter to younger allied S-rank Hunter | Mr. Wu | polished and formally coaxing | Lee publicly draws Wu into agreement with the suicide-squad plan. |
| 최민우 | 진태경 | trusted allied team leader to younger allied Hunter | Mr. Jin | formal-polite and concerned | Choi warns Jin about the danger of the operation and affirms his deep trust. |
| 진태경 | 최민우 | younger allied Hunter to allied team leader | Team Leader Choi | polite, familiar, and teasing | Jin jokes with Choi while acknowledging and dismissing his concern. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 415
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who has sworn never to kill again.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 416
- **Aliases:** Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, and a Supreme Peak master who has manifested Force and crossed the wall into true mastery.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and student, his mother and sister Hayeon are among those he protects, and the Skeleton Warlord is his captive undead commander.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 416
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Lee Jungryong.md

# Lee Jungryong (이정룡)

- **Safe through:** Chapter 416
- **Aliases:** None
- **Role:** Vice Guild Master of Ares Guild, one of Korea's two S-rank Hunters, and a Supreme Peak-level martial artist who directs Ares Guild operations.
- **Personality:** Outwardly genial, calm, and humorous; calculating, manipulative, coercive, and ruthless when challenged
- **Voice:** Smooth, good-natured, and indirect, using teasing conversation and veiled threats before becoming openly furious
- **Relationships:** Master of Park Jihoon and Go Jun (Team Leader Seok), whom he personally selected and trained; longtime Great Cataclysm acquaintance of Park Tae Seop; adversary of Jin Taekyung; knew Team Leader Choi from childhood; has an antagonistic history with Kim Hwajong, who saved his life at the collapse of Mapo Bridge eighteen years earlier; was visibly shaken by learning that Choi is Cheon Taemin's maternal grandson; regards Cheon Taemin as an older brother despite no blood relation and has long held him in respect and fear; operates as Ares Guild's senior authority beneath its Guild Master

### Lei Fei.md

# Lei Fei (레이페이)

- **Safe through:** Chapter 416
- **Aliases:** None
- **Role:** Lei Fei is a concealed Chinese S-rank Hunter and former head of the Public Security Armed Forces Department in Sichuan Province who recovered his human identity after becoming a level-120 undead Death Knight Lord and died fulfilling his final mission.
- **Personality:** Lei Fei's recovered memories show him as dutiful, honorable, family-oriented, and willing to serve as an unseen guardian.
- **Voice:** His human voice is formal and earnest, becoming warm and playful with family.
- **Relationships:** Wei Fenghu is his maternal uncle who raised him as a son; Lei Fei married an unnamed flower-shop owner and had a daughter, trained alongside Wu Heixing, and was corrupted by the Arch Lich before Jin Taekyung restored his identity.

### Park Jihoon.md

# Park Jihoon (박지훈)

- **Safe through:** Chapter 416
- **Aliases:** Park Jihwang
- **Role:** Hunter in Team 1 of Myeongdong Guild and its covert enforcer; killed Team Leader Jung Hyunwoo after detecting wrongdoing; Jin Taekyung's former middle-school classmate; attended Hankuk University's Business Administration department but has not graduated since awakening; son of a family that has run a Hunter-related business for more than thirty years; gave a taunting, equivocal response when Taekyung accused him of sending the twenty-eight Black Hunters and threatened to end Taekyung and the Peace Guild if Taekyung advanced farther; possesses a separate phone for secret communications, knows hand-to-hand combat comparable to a Peak master's grappling technique, and used a potion to recover from Taekyung's assault before fighting beside Park Tae Seop against him; secret Disciple of Lee Jungryong who was left alive after Taekyung severed both arms and severely injured his leg and shoulder
- **Personality:** Outgoing and teasing in conversation; privately says that he and Taekyung were not close
- **Voice:** Casual, sociable, and teasing with an old classmate
- **Relationships:** Former Garam Middle School classmate of Jin Taekyung; boyfriend of an unnamed woman; works under Myeongdong Guild Master Park Tae Seop while openly challenging the Guild Master's authority

### Team Leader Choi.md

# Team Leader Choi

- **Safe through:** Chapter 414
- **Aliases:** Choi Minwoo (최민우)
- **Role:** Allied team leader and Hunter who analyzes battlefield conditions during the Arch Lich operation.
- **Personality:** Calm, analytical, and steady under extreme battlefield pressure.
- **Voice:** Measured and logical, using clear tactical explanations.
- **Relationships:** Works alongside Jin Taekyung and Lee Jungryong in the coalition against the Arch Lich.

### Wu Heixing.md

# Wu Heixing (우헤이싱)

- **Safe through:** Chapter 416
- **Aliases:** None
- **Role:** Wu Heixing is a Chinese S-rank Hunter known for frequent media exposure and scandal who secretly practices martial arts, including an internal-energy cultivation technique and fist-and-foot martial arts.
- **Personality:** Arrogant, status-conscious, abusive, and fiercely proud of his power, he responds to humiliation with anger and protects himself even while his allies die.
- **Voice:** Loud, insulting, entitled, and dependent on national and political status.
- **Relationships:** He is openly hostile toward Jin Taekyung and Faye Chen, and resents Jin receiving Chairman Shao Yang's attention.

## Korean source

```text
＃417화



모르지 않았다. 단지 기다렸을 뿐이다.

놈들이 송곳니를 들이미는 그 순간을.

“그보다는…… 확신이죠.”

“확신?”

“예.”

나도 모르게 입꼬리가 올라간다. 지금껏 몇 번이고, 몇십 번이고 꾹꾹 눌러 담았던 한마디를 던졌다.

“이 씨벌 새끼들이 아크 리치보다는 내 뒤통수에 더 관심이 있구나. 뭐 그런 확신이요.”

“……!”

「……!」

짧았던 가면극이 막을 내린 그 순간.

저벅.

앞서가던 이정룡의 발걸음이 멈췄고.

파팟!

등 뒤에서 파공성이 일었다. 전신 요혈을 파고드는 세 줄기의 바람.

돌아서지 않아도 볼 수 있었다. 우헤이싱의 손을 떠난 비수가 향하는 곳을. 그리고 내가 해야 할 행동을.

쉬쉬쉭!

목덜미와 척추, 오른팔을 노리고 날아든 세 개의 비수가 목적을 이루지 못하고 허공을 꿰뚫었다.

‘아니, 아니지.’

극도로 끌어올린 감각 덕분일까. 모든 것이 느리고 선명하다.

손을 뻗자 오른팔을 스쳐 지나가던 비수의 손잡이가 잡혔다. 동시에 허리를 틀며 번개처럼 팔을 뿌렸다.

쐐애애애액!

「흡!」

나를 향해 쇄도해 오던 우헤이싱이 황급히 검을 휘둘렀다.

쾅!

먹먹한 굉음과 함께 놈의 신형이 밀려난다. 일그러진 표정을 한 채 재차 달려들려는 우헤이싱을, 나직한 목소리가 막아섰다.

“그만.”

「이 선생님. 어째서……!」

“자네가 상대할 수 있는 자가 아니야. 잠시 기다리게.”

우헤이싱을 제지한 이정룡이 덤덤한 눈빛으로 나를 응시했다.

“눈치가 제법이구나.”

대번에 바뀐 어투에 피식 웃음이 나왔다.

“다 아는 늙은이가 뻔한 소리를. 이 정도 눈치도 없으면 진작 죽었지.”

“언제부터 알고 있었느냐?”

나는 망설임 없이 대답했다.

“처음 만난 그 순간부터.”

명동 길드에 단신으로 쳐들어간 그 날. 이미 이정룡과 나는 물러설 수 없는 대척점에 섰다.

그것은 박지훈 그 개새끼가 블랙 헌터를 시켜 꺽정 아저씨의 양팔을 자를 때부터 정해진 일이었다.

“그때의 일이 부하들의 과잉 충성이었다. 그딴 개소리 할 거면 백태 낀 혓바닥 돌돌 말아서 집어넣어.”

“그럴 리가. 다만 애석할 뿐이다.”

“뭐가. 곧 병풍 뒤에서 향냄새 맡을 당신 미래가?”

이정룡이 고개를 저었다.

“아니. 네가 꽤 마음에 들었었거든.”

“그럼 내 사람 팔을 자르지 말았어야지.”

“가벼운 경고였다. 최민우, 그 아이에게 일깨워 주고 싶었지. 그때만 하더라도 진태경이라는 핏덩이는 그리 큰 고려 대상이 아니었고.”

“지금은?”

이정룡은 부드럽게 웃으며 대답했다.

“내가 직접 이곳에 왔다. 대답이 되었느냐?”

“그 정도면 충분히.”

나는 백염(白炎)을 비스듬히 늘어트린 채, 무너져 있는 콘트리트 파편에 등을 기댔다.

좌측에는 우헤이싱. 우측에는 이정룡. 각자 십여 미터의 간격이 있지만, 아주 찰나의 순간만으로도 사라질 거리다.

“그런데 의외네. 최소한 아크 리치를 처치한 후에 일을 벌일 줄 알았는데.”

「푸핫! 이 멍청한 빵즈 놈 같으니!」

불쑥 끼어든 우헤이싱이 낄낄거렸다.

불과 며칠까지만 해도 내 눈도 제대로 못 마주치던 녀석은 의기양양하게 선언했다.

「아크 리치와 싸우는 건 너다. 진태경.」

“뭔 헛소리…… 아.”

순간 뇌리를 스치는 어떤 생각에, 나도 모르게 헛웃음이 흘러나왔다.

설마 설마 했는데, 정말이지 대단하다. 나와는 뇌 구조 자체가 다르다.

“허, 이 씨벌 새끼들 생각 야무진 거 봐라. 상상 그 이상이네.”

「이제 알겠나? 네가 어떤 상황인지?」

“그러니까…… 애초에 아크 리치와는 싸울 생각이 없었다?”

입꼬리를 말아 올린 우헤이싱이 입을 열었다.

「왜 내가 왜 그런 위험을 감수해야 하지?」

“……!”

「오늘 전투는 패전으로 기록될 거다. 그리고 전사자 명단의 가장 윗줄에는 네 이름이 적혀 있을 거야. 이미 묘비명도 정해 뒀지.」

우헤이싱이 연극배우처럼 손을 벌렸다.

「한국에서 온 빵즈, 아크 리치에 의해 죽다. 어때, 괜찮은 묘비명 아닌가?」

놈의 말이 끝났음에도 나는 한동안 할 말을 찾지 못해 눈을 깜빡였다. 정신 나간 사람처럼 멍했고 전신을 감싼 소름이 가시질 않았다.

놈이 꾸민 흉계 때문에?

아니다. 텅 빈 머릿속에는 우헤이싱이 반문했던 한마디가 계속해서 맴돌고 있었다.

‘왜 그런 위험을 감수해야 하냐고?’

뒤통수를 한 대 맞은 기분이었다. 동시에 지난 한 달간 봐 왔던 무수한 죽음과 참혹하게 훼손된 시신들의 모습이 눈앞을 스쳤다.

혹여나 당신의 어린 자식이 살 수 있지 않을까, 소중히 품에 안은 채 최후를 맞이한 젊은 부모.

몸이 불편해 도망치지도 못하고 뜯어먹힌 노인과 한껏 부푼 만삭의 배를 움켜쥐고 숨을 거둔 임산부.

그리고…….



‘헌터가 되던 날 맹세했지. 목숨이 다하는 그 순간까지 몬스터와 싸우겠노라고. 그날의 맹세는 아직 유효하네.’



마지막 순간까지 자신의 사명을 다한 레이페이와, 죽음을 딛고 일어나 장렬히 돌격하던 오백 명의 공안무력부 헌터들.

최후를 각오하고 한 마리의 몬스터를 더 처치하기 위해 천으로 손과 검자루를 묶은 최 팀장과 샤오 쉔.

‘그러게. 모두 왜 그런 위험을 감수했습니까. 병신같이.’

그들 한 사람, 한 사람의 얼굴이 눈앞을 스친다. 불덩이를 삼킨 것처럼 속이 뜨거워지고 더운 숨결이 토해졌다.

크게 심호흡한 나는 한 사람을 바라보았다.

“말해 봐.”

“무엇을 말이냐.”

“당신도 저놈과 같은 생각인지.”

“다르지. 아주 달라. 저 친구는 아크 리치를 두려워하지만…….”

이정룡이 부드럽게 말을 이었다.

“나는 기회를 잡은 게다. 이 전쟁이 길어질수록, 더 많은 이득을 얻을 수 있을 테니까.”

잠깐의 침묵 후, 나는 작게 고개를 끄덕였다.

“그래, 그렇군.”

콘크리트 파편에서 등을 뗐다. 용암처럼 들끓는 열양지기가 사지 백해와 수백 개의 혈도를 타고 휘몰아친다. 손에 쥔 백염의 창날에서 푸른 불꽃이 일렁였다.

“나도 하나만 묻자.”

“무엇이든지.”

“착짱죽짱. 개씹정룡. 내가 방금 정한 너희 묘비명인데, 마음에 드냐?”

「……!」

“……허허.”

우헤이싱의 얼굴이 와락 일그러지고, 나를 바라보던 이정룡의 눈매가 초승달처럼 휘어진 다음 순간.

쉬이이이잉!

눈부신 섬광이 좌우로부터 뿜어져 나왔다.



* * *



이정룡은 이미 결심을 굳힌 상태였다.

‘방심은 금물. 무슨 수를 써서라도 반드시 죽인다.’

사자는 토끼를 잡을 때도 최선을 다하는 법. 하물며 진태경이라는 늑대를 사냥하기 위해서는 사자 역시 온 힘을 다해야 했다.

제아무리 이정룡 자신이 사자라고는 하나, 늑대의 이빨을 무시할 수는 없으니까.

쉭!

단 한 걸음. 찰나의 순간에 십여 미터의 거리를 좁힌 이정룡의 손이 흐릿해졌다.

어느새 검갑에서 빠져나온 한 자루의 장검이 눈부신 섬광으로 화해 쏘아졌다.

한 사람, 바로 진태경을 향해.

쉬이이이잉!

이번 전쟁 어디에서도 보인 적 없던, 이정룡이 진심을 담아 휘두른 일격이다.

게다가 우헤이싱 역시 공격에 가담한 상태. 진태경과 비교하면 한참이나 부족한 애송이지만, 오러 블레이드를 사용하는 S급 헌터라는 사실에는 변함이 없다.

「죽어어엇!」

잔뜩 핏발 선 눈을 한 우헤이싱이 고함을 내지른 그 순간, 이정룡은 똑똑히 볼 수 있었다.

마치 미끄러지듯 부드러운 진태경의 움직임을. 푸른 불꽃에 휘감긴 창날을.

꽈앙!

두 개의 검과 하나의 창이 부딪쳤다.

사방을 떨어 울리는 굉음과 함께 터져 나온 막대한 기파(氣波)가 건물을 무너트리고 콘크리트를 가루로 만들었다.

쿠궁! 쿠구구구궁!

폭격이라도 일어난 듯한 광경.

지면이 주저앉고 엄청난 진동이 반경 수백 미터를 휩쓸었다.

하지만 이것은 곧 이어질 모든 것의 시작에 불과했다.

쉬쉬쉬쉭!

수십, 수백 개의 선이 허공을 베었다. 눈에 보이지도 않을 만큼 빠른 속도로 움직이는 이정룡의 검이 진태경을 난도질했다.

아니, 그러리라 믿어 의심치 않았다.

화염에 휩싸인 손바닥으로 우헤이싱의 가슴을 후려쳐 날려 보낸 진태경이 창을 내리긋기 전까지는.

화륵, 후우우우웅!

초고온의 열기가 공기를 태우며 타올랐다.

도시 전체를 잠식한 짙은 안개도, 날씨가 부른 습기도 집어삼킨 창날이 맹렬한 기세로 이정룡의 전신을 비스듬히 베어 왔다.

그 모습이 꼭, 창공으로부터 내리 찍히는 용의 발톱과 같았다.

‘이게 무슨…….’

이정룡은 눈살을 찌푸렸다.

진태경의 창날이 자신이 흩뿌린 오러를 지우며 쇄도하고 있었다.

엄청난 열기에 숨이 턱 막히고 몸이 덜컥 굳었다.

서른이 채 되지 않은 눈앞의 청년은, 이정룡이 알고 있던 그 사람이 아니었다.

‘어떻게 그 짧은 시간에 이렇게까지……!’

하지만 예상을 훌쩍 뛰어넘는 진태경의 실력에 놀랐을 뿐, 이정룡 역시 여타의 S급 헌터를 뛰어넘는 한 사람의 초인(超人)이었다.

찰나의 순간, 그는 검신을 눕혀 창날을 가로막았다.

콰아아앙!

진태경의 창은 이정룡이 생각했던 것보다 빠르고, 강했다. 그러나 그것은 이정룡 역시 마찬가지였다.

슁, 쉬쉬쉬쉬쉭!

찰나를 쪼개고 쪼갠 시간 속, 창과 검이 얽히고 부딪쳤다. 벼락과도 같은 섬광과 굉음이 쉴 새 없이 울려 퍼졌다.

카카칵, 창날로 이정룡의 검을 내리누른 진태경이 손을 뻗었다.

화염신장의 열기가 담긴 일장이 이정룡의 가슴에 작렬하기 직전, 번개같이 쏘아진 이정룡의 주먹이 그의 손바닥과 맞닿았다.

퍼벙-!

압축된 공기가 터져 나가는 소리와 함께, 두 사람은 약속이라도 한 것처럼 뒷걸음질 쳤다.

그리고 그 결과는 이정룡에게 있어 놀라움, 그 자체였다.

두 걸음을 물러선 자신과 달리, 진태경은 고작 한 걸음을 물러났을 뿐이었다.

‘내가, 밀렸다는 말이냐?’

오랜 세월 동안 막대한 양의 기운을 축적한 이정룡이었다.

그런데 고작 이십 대 후반의 핏덩이가 그를 물러나게 만들었다.

불과 한 달 남짓한 짧은 시간 동안 일어난 변화라고는 도무지 믿기지 않을 정도다.

‘그뿐만이 아니다.’

도무지 바닥을 알 수 없는 엄청난 힘과 속도. 움직임…… 모든 것이 놀랍다. 이루 말할 수 없을 정도다.

바로 지금처럼.

후우우웅! 슉!

이정룡은 고개를 틀었다. 반 뼘 차이로 스쳐 지나가던 창날이 허공에서 방향을 틀었다.

서걱!

불에 덴 듯한 감각과 점점이 흩뿌려지는 핏방울.

이정룡은 실로 오랜만에 고통이라는 감각을 느끼며 검을 휘둘렀다.

쾅!

서로를 향해 맞댄 병장기. 투명한 창날 너머로 타오르는 청년의 눈동자가 보였다.

시종일관 굳게 다물어져 있던 그의 입술 사이로 착 가라앉은 목소리가 흘러나왔다.

“넌…… 좆 됐어.”

서늘한 진태경의 한마디를 듣는 순간, 이정룡은 문득 자신이 앞서 내린 평가를 정정해야 할 필요가 있음을 깨달았다.

‘사자.’

자신이 틀렸다. 진태경은 늑대가 아니라 한 마리의 사자다.

오랫동안 무리의 우두머리였던 늙은 사자를 몰아내고, 새로운 왕이 될 수도 있는 힘 있는 젊은 숫사자.

카가가가각, 쾅!

늙은 사자는 항거할 수 없는 힘에 의해 튕겨져 나갔다.

그리고 허공에서 신형을 뒤집으며 지면에 착지한 이정룡이 가장 처음으로 목격한 것은, 기습을 시도한 우헤이싱의 목줄기를 움켜쥔 젊은 숫사자의 모습이었다.

「커헉! 내, 내 아버지는 태자당의……!」

“관심 없다.”

「나, 날 살려 주면 반드시 보답하겠다! 컥! 그러니 제발.」

“내가? 날 죽이려 한 널?”

불그스름한 눈빛이 우헤이싱을 향했다.

이내 어디선가 들어 본 한마디가 흘러나왔다.

“왜 내가 왜 그런 위험을 감수해야 하지?”

「……!」

우두둑!
```

## Final English reading copy

```markdown
# Chapter 417

It wasn’t that I didn’t know. I had only been waiting.

Waiting for the moment they sank their fangs into me.

“Rather… certainty.”

“Certainty?”

“Yes.”

The corners of my mouth rose before I could stop them. I threw out the one thing I had pressed down and held back time and time again.

“I’m certain these fucking bastards are more interested in stabbing me in the back than fighting the Arch Lich. Something like that.”

“……!”

“……!”

The moment the brief farce came to an end—

*Step.*

Lee Jungryong’s footsteps stopped.

*Fwish!*

The sound of displaced air rang out behind me. Three streaks of wind bored toward vital points across my body.

I did not need to turn around to see where the daggers Wu Heixing had thrown were headed.

And I knew what I had to do.

*Fwish-fwish-fwish!*

The three daggers aimed at my nape, spine, and right arm failed to reach their targets and pierced empty air.

*No. That’s not it.*

Maybe it was because I had raised my senses to their absolute limit.

Everything was slow and clear.

I reached out and caught the hilt of the dagger that had skimmed past my right arm. At the same time, I twisted my waist and whipped my arm forward like lightning.

*Shraaaaaaaaaash!*

“Hup!”

Wu Heixing, who had been charging toward me, hurriedly swung his sword.

*Boom!*

Along with a muffled, thunderous roar, his body was knocked backward. A low voice stopped Wu Heixing as he prepared to charge again, his face twisted in anger.

“Enough.”

“Mr. Lee. Why…!”

“He’s not someone you can handle. Wait here for a moment.”

Lee Jungryong restrained Wu Heixing and gazed at me with calm eyes.

“Your instincts are quite good.”

His tone had changed so completely that I let out a quiet laugh.

“An old man who knows everything is saying something obvious. If I didn’t have even this much sense, I’d have died a long time ago.”

“When did you know?”

I answered without hesitation.

“The moment we first met.”

The day I stormed into Myeongdong Guild alone. From that moment, Lee Jungryong and I had stood at an impassable point of opposition.

It had been decided the day that bastard Park Jihoon sent Black Hunters to cut off Uncle Kkeokjeong’s arms.

“If you’re going to say that was merely the result of your subordinates’ excessive loyalty, roll up that white-coated tongue and shove it back in your mouth.”

“Of course I wouldn’t. I merely find it regrettable.”

“What do you regret? The future where you’ll be smelling funeral incense behind a folding screen?”

Lee Jungryong shook his head.

“No. I had taken quite a liking to you.”

“Then you shouldn’t have cut off my man’s arms.”

“It was a light warning. I wanted to teach Choi Minwoo that boy a lesson. At the time, a fledgling named Jin Taekyung was not someone we needed to take seriously.”

“And now?”

Lee Jungryong answered with a gentle smile.

“I came here myself. Is that answer enough?”

“That’s more than enough.”

I leaned my back against a pile of collapsed concrete, holding White Flame at an angle.

Wu Heixing stood to my left. Lee Jungryong stood to my right. There were more than ten meters between us, but that was a distance any of us could erase in the blink of an eye.

“But this is unexpected. I thought you’d at least wait until after we killed the Arch Lich before making your move.”

“Pfft! You stupid peninsula bangzi!”

Wu Heixing cut in out of nowhere and snickered.

Only a few days ago, he had been unable to meet my eyes properly. Now he declared triumphantly,

“Fighting the Arch Lich is your job, Jin Taekyung.”

“What kind of bullshit… Ah.”

A certain thought flashed through my mind, and a hollow laugh escaped me.

I had wondered if that could really be the case, but they had actually gone that far.

Their brains were built completely differently from mine.

“Hah. Look at how neatly these fucking bastards thought this through. It’s beyond anything I imagined.”

“Do you understand now? Do you understand what kind of situation you’re in?”

“So… you never intended to fight the Arch Lich in the first place?”

Wu Heixing curled his lips and spoke.

“Why—why should I take that kind of risk?”

“……!”

“Today’s battle will go down as a defeat. And your name will be written at the very top of the list of the war dead. I’ve already decided on your epitaph.”

Wu Heixing spread his arms like a stage actor.

“Bangzi from Korea, killed by the Arch Lich. How about it? Isn’t that a fine epitaph?”

Even after Wu Heixing finished speaking, I could not find anything to say for a while. I stood there blankly, like a madman, and the goose bumps covering my body refused to fade.

Was it because of the scheme he had devised?

No.

One question Wu Heixing had thrown back at me continued to circle through my empty mind.

*Why should I take that kind of risk?*

It felt as though I had been struck in the back of the head.

At the same time, the countless deaths I had witnessed over the past month flashed before my eyes, along with the bodies that had been horribly mutilated.

Young parents who had met their end while holding their precious child tightly, hoping against hope that their little one might survive.

The old and infirm, unable to escape, who had been torn apart and eaten alive.

A pregnant woman who had died clutching her heavily swollen belly.

And…

*The day I became a Hunter, I swore that I would fight monsters until the moment my life ended. That oath still stands.*

Lei Fei, who had fulfilled his mission until the very last moment.

The five hundred Public Security Armed Forces Department Hunters who rose in defiance of death and charged valiantly.

Team Leader Choi and Shao Shen, who had bound their hands to their sword hilts with strips of cloth, prepared to kill one more monster despite knowing they were facing their final moments.

*You’re right. Why did all of them take such risks? Like fucking idiots.*

The face of each and every one of them flashed before my eyes.

My insides burned as though I had swallowed a fireball, and I exhaled a hot breath.

After taking a deep breath, I looked at one person.

“Tell me.”

“What should I tell you?”

“Whether you think the same way as that bastard.”

“I don’t. I’m very different from him. That fellow is afraid of the Arch Lich, but…”

Lee Jungryong continued in a gentle voice.

“I seized an opportunity. The longer this war lasts, the more I stand to gain.”

After a brief silence, I nodded faintly.

“I see.”

I pulled my back away from the concrete rubble. Scorching Yang Qi boiled like lava, surging through my four limbs, bones, and hundreds of acupoints. Blue flames danced along the spearhead of the White Flame in my hand.

“Let me ask you one thing, too.”

“Ask me anything.”

“‘The only good chink is a dead chink. Fucking Lee Jungryong.’ Those are the epitaphs I just came up with for you two. Do you like them?”

“……!”

“……Heh.”

Wu Heixing’s face crumpled, while the corners of Lee Jungryong’s eyes curved like crescent moons.

Then—

*Fwoooooosh!*

Blinding flashes burst from both sides.

* * *

Lee Jungryong had already made up his mind.

*I must not let my guard down. I’ll kill him by any means necessary.*

A lion gave its all even when hunting a rabbit.

All the more so when hunting a wolf named Jin Taekyung. To bring him down, a lion had to use every ounce of its strength.

No matter how much of a lion Lee Jungryong was, he could not afford to ignore the wolf’s fangs.

*Fwish!*

With a single step, Lee Jungryong closed the distance of more than ten meters in an instant, and his hand blurred.

A longsword had already left its scabbard, transforming into a dazzling flash as it shot forward.

Straight at one person—Jin Taekyung.

*Fwoooooosh!*

It was a full-power strike from Lee Jungryong, the likes of which he had not unleashed anywhere else in this war.

And Wu Heixing had joined the attack as well.

Compared to Jin Taekyung, Wu Heixing was a fledgling far behind him in ability, but he was still an S-rank Hunter who used an Aura Blade.

“Dieeeee!”

The instant Wu Heixing shouted with his eyes bloodshot, Lee Jungryong saw it clearly.

Jin Taekyung’s smooth movement, as fluid as sliding across ice.

The spearhead wrapped in blue flames.

*Boom!*

Two swords and one spear collided.

The tremendous wave of qi that erupted with a thunderous roar collapsed buildings and pulverized concrete.

*Rumble! Rumble-rumble-rumble!*

It looked as though a bombardment had taken place.

The ground caved in, and an immense tremor swept across a radius of several hundred meters.

But this was only the beginning of everything that followed.

*Fwish-fwish-fwish-fwish!*

Dozens, then hundreds of lines slashed through the air.

Lee Jungryong’s sword moved too quickly for the eye to follow, shredding Jin Taekyung.

Or rather, Lee Jungryong had been certain that was what would happen.

Until Jin Taekyung struck Wu Heixing in the chest with a palm engulfed in flames and sent him flying, then brought his spear down.

*Fwoosh—whoooooosh!*

Superheated flames blazed up, burning the air.

The spearhead devoured the thick fog that had consumed the entire city and the moisture brought by the weather, then slashed diagonally toward Lee Jungryong’s entire body with ferocious force.

It looked just like the claw of a dragon striking down from the heavens.

*What is this…?*

Lee Jungryong frowned.

Jin Taekyung’s spearhead was rushing toward him, erasing the Aura he had scattered.

The tremendous heat caught his breath and made his body lock up.

The young man before him, not even thirty years old, was no longer the person Lee Jungryong had known.

*How did he improve this much in such a short time…?*

But Lee Jungryong was not merely surprised by Jin Taekyung’s ability, which had far surpassed his expectations.

Lee Jungryong himself was a superhuman who exceeded even the other S-rank Hunters.

In a split second, he turned his blade sideways and blocked the spearhead.

*Kwaaaaaaaaaang!*

Jin Taekyung’s spear was faster and stronger than Lee Jungryong had expected.

But the same was true of Lee Jungryong.

*Swing—fwish-fwish-fwish-fwish!*

Within a moment divided into even smaller moments, spear and sword tangled and collided.

Flashes like lightning and thunderous roars rang out without pause.

*Clack-clack-clack!*

Jin Taekyung pressed down on Lee Jungryong’s sword with his spearhead, then reached out.

Just before the palm strike carrying the heat of the Flame Divine Palm could slam into Lee Jungryong’s chest, Lee Jungryong’s fist shot forward like lightning and met Jin Taekyung’s palm.

*Boom!*

With the sound of compressed air bursting apart, the two men stepped backward as though they had planned it.

And the result was astonishing to Lee Jungryong.

He had retreated two steps.

Jin Taekyung had retreated only one.

*Was I pushed back?*

Lee Jungryong had accumulated an enormous amount of qi over the course of many years.

And yet a fledgling barely in his late twenties had forced him backward.

It was impossible to believe that such a change had occurred in the short span of just over a month.

*That isn’t all.*

His incredible power and speed seemed to have no bottom. His movements, too—everything about him was astonishing. Beyond anything that could be put into words.

Just as he was now.

*Whoooooosh! Fwish!*

Lee Jungryong twisted his head aside.

The spearhead that had passed within half a span of his body changed direction in midair.

*Slash!*

A sensation like being burned, followed by droplets of blood scattering through the air.

Lee Jungryong felt the sensation of pain for the first time in a very long while and swung his sword.

*Boom!*

The weapons met as the two men faced each other.

Through the transparent spearhead, Lee Jungryong could see the young man’s burning eyes.

From between his lips, which had remained tightly sealed the entire time, came a low, flat voice.

“You’re fucked.”

Hearing Jin Taekyung’s chilling words, Lee Jungryong suddenly realized that he needed to correct the assessment he had made earlier.

*A lion.*

He had been wrong.

Jin Taekyung was not a wolf.

He was a lion—a powerful young male lion who might drive out the old lion that had ruled the pride for so long and become the new king.

*Craaaaaack! Boom!*

The old lion was sent flying by an irresistible force.

Lee Jungryong flipped his body in midair and landed on the ground.

The first thing he saw was the young male lion gripping Wu Heixing by the throat after Wu had attempted a surprise attack.

“Guhk! M-my father is with the Crown Prince Party…!”

“I don’t care.”

“If you let me live, I’ll repay you! Guh! Please!”

“Me? Let you live after you tried to kill me?”

A reddish gaze turned toward Wu Heixing.

Then a sentence Lee Jungryong had heard somewhere before slipped from Jin Taekyung’s lips.

“Why—why should I take that kind of risk?”

“……!”

*Crunch!*
```

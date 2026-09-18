<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0410.txt",
      "sha256": "6bdf9a6e4c06a68bb240b8be1f491fcc89cb1aad8570910f11dce5a3d7289018",
      "bytes": 13771
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "8ad95feacfa7aacfd0d66a05a2a2e099068f8bf727ae44d2db69f2931b649214",
      "bytes": 2031
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "ef7b8d7b1e18a76bbc85cfe789f948a4a9c810412be1e64a4530e19b86f7e1d3",
      "bytes": 137619
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "3420e8c753e6d67616bbf0c0873ceb6a6c22c9ac84c31ecadaae6746a91a9808",
      "bytes": 533
    },
    {
      "path": "characters/Go Jun.md",
      "sha256": "db9da36b7e186fb41827520ba59d40219aab0095125f52c00f99f1a123e314fb",
      "bytes": 811
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "9e1846d382bb91f6e243b7178a57906b821be199ba14b532355a42927876d3ce",
      "bytes": 1270
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "f76d958cb2a4575f8d07f10ae0e13b1cd92ea59da968abeaa3e53f9722e0959c",
      "bytes": 622
    },
    {
      "path": "characters/Lee Jungryong.md",
      "sha256": "3aa5e5b6a3ff1b99cc64fafbbba3d993813c66ae4370892002d05756bc5aec8d",
      "bytes": 1163
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "907142dc6d90967cbfbb0df25a0c535429a6cf0ff835e96a5680a29793ce3dd3",
      "bytes": 123471
    }
  ],
  "estimated_tokens": 10436
}
-->

# Durable State Update — Chapter 410

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 410. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 410. Profile updates may replace only one
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
  "chapter": 410,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 410,
    "continuity_sources": [410],
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
    "The Western Front's thousands of Hunters and soldiers are advancing on fog-shrouded Suining City while the other allied fronts surround it.",
    "The battle for Suining City has begun as corpses rise, Skeletons emerge, and monsters move within the encroaching fog.",
    "Jin Taekyung expects defeating the Arch Lich to be the key to stopping the undead threat.",
    "Team Leader Choi deeply trusts Jin Taekyung but fears the operation because Lee Jungryong and Wu Heixing are involved as dangerous, untrustworthy comrades.",
    "Team Leader Choi is a descendant of Cheon Taemin with exceptional martial talent and unusually substantial internal energy.",
    "Jin Taekyung's speech, strengthened by internal energy, has eased the Western Front's tension and encouraged its soldiers before battle.",
    "The Skeleton Warlord remains Jin Taekyung's captive and reluctant companion despite fearing the operation.",
    "The Skeleton Warlord's glossy black skull has acquired a small crack after Jin flicked it."
  ],
  "continuity_sources": [
    409
  ],
  "open_questions": [
    "Who is Lei Fei's unidentified lord, what is the lord's origin, and how does the lord relate to the Arch Lich's objective?",
    "What happened to the Second Fiend assigned to the Qingcheng attack?",
    "Why has the Arch Lich withheld itself from the war, and what is it preparing now?",
    "What kind of being was the Skeleton Warlord before it became an undead commander?",
    "What specific situation will allow Jin to draw out Hero's Power more strongly?"
  ],
  "safe_through": 409,
  "temporary_decisions": [
    "Render 영웅의 혼 as Hero's Soul and 영웅의 힘 as Hero's Power.",
    "Render 기동전 as mobile warfare.",
    "Render 쑤이닝시 as Suining City.",
    "Render 결사대 as suicide squad.",
    "Render 스켈레톤 워로드 as Skeleton Warlord, 아크 리치 as Arch Lich, and 머리를 치다 as take out the head in the context of killing the Arch Lich."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 이정룡    | **Lee Jungryong** |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 레벨               | **Level**                      |
| 경험치              | **EXP**                        |
| 체력               | **Stamina**                    |
| 민첩               | **Agility**                    |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 몬스터     | **monster**           |
| 레이드     | **raid**              |
| 길드      | **Guild**             |
| 팀장      | **Team Leader**       |
| 탱커      | **tank**              |
| 대격변     | **Great Cataclysm**   |
| 도사      | **Daoist**                                                      |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 고준 | **Go Jun** | Personal name of Team Leader Seok; Lee Jungryong's prized Disciple. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 아레스 | **Ares Guild** | The leading Guild in Korea; formerly employed Team Leader Choi and Song Song. |
| 군림 | **The Reign** | Opening fragment of an incomplete wuxia novel title that Taekyung read through volume thirty-four. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 고블린 | **goblin** | Monster species reported at the F-rank Gate. |
| 오우거 | **ogre** | B-rank monster species emerging from the Gate. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 라이칸스로프 | **Lycanthrope** | B-rank Gate monster species. |
| 오크 | **Orc** | Monster species. |
| 준이 | **Jun** | Family nickname used in the form Jun's dad. |
| 석고준 | **Go Jun** | Source full-name form for the established Go Jun, also known as Team Leader Seok. |
| 메이지 | **Mage** | Skeleton subtype mentioned alongside Soldiers and Warriors. |
| 워리어 | **Warrior** | Skeleton subtype mentioned alongside Soldiers and Mages. |
| 경호팀장 | **Head of Security** | Go Jun's security-team office under Lee Jungryong. |
| 중국 | **China** | Country from which Team Leader Choi’s video originates. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 이정룡 | 진태경 | senior S-rank Hunter to younger Hunter and adversary | Young man | polished, teasing, and veiled-threatening | Uses a genial tone and indirect threats while trying to make Taekyung release the captives. |
| 진태경 | 이정룡 | younger Hunter to senior S-rank Hunter and adversary | you | polite but mocking and defiant | Taekyung answers Lee's soft threats with the wolf-and-tiger metaphor and refuses to yield. |
| 이정룡 | 고준 | Master to Disciple | Go Jun | familiar and testing | Lee switches from Seok's office title to his personal name while considering whether he can defeat Taekyung. |
| 고준 | 이정룡 | Disciple to Master | Master | deferential | Go Jun responds to Lee's personal-name address as 스승님. |
| 진태경 | 석고준 | returning Hunter to hostile Ares security leader | you fucking bastard | hostile and profane | Taekyung directs his final insults and challenge at Go Jun after returning alive. |
| 석고준 | 진태경 | hostile_opponents | brat | hostile and overconfident | Go Jun addresses Taekyung internally as 애송아 while launching his full-strength attack. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 409
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who has sworn never to kill again.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Go Jun.md

# Go Jun (고준)

- **Safe through:** Chapter 405
- **Aliases:** Team Leader Seok
- **Role:** Leader of Lee Jungryong's security team, an Ares Guild combatant, and Lee's disciple and right-hand man.
- **Personality:** Highly disciplined, fiercely loyal to Lee Jungryong, confident in his abilities, and angered by operational failures that endanger his Master.
- **Voice:** Dry, controlled, and formal with subordinates; deferential when addressing his Master.
- **Relationships:** Disciple and direct protégé of Lee Jungryong; leader of Lee's security detail; regarded by Lee as stronger than Park Tae Seop; after Go Jun's defeat by Jin Taekyung, Lee reaffirmed his faith in Go Jun and promised to give him the strength to defeat Taekyung.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 409
- **Aliases:** Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, and a Supreme Peak master who has manifested Force and crossed the wall into true mastery.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and student, his mother and sister Hayeon are among those he protects, and the Skeleton Warlord is his captive undead commander.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 409
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Lee Jungryong.md

# Lee Jungryong (이정룡)

- **Safe through:** Chapter 409
- **Aliases:** None
- **Role:** Vice Guild Master of Ares Guild, one of Korea's two S-rank Hunters, and a Supreme Peak-level martial artist who directs Ares Guild operations.
- **Personality:** Outwardly genial, calm, and humorous; calculating, manipulative, coercive, and ruthless when challenged
- **Voice:** Smooth, good-natured, and indirect, using teasing conversation and veiled threats before becoming openly furious
- **Relationships:** Master of Park Jihoon and Go Jun (Team Leader Seok), whom he personally selected and trained; longtime Great Cataclysm acquaintance of Park Tae Seop; adversary of Jin Taekyung; knew Team Leader Choi from childhood; has an antagonistic history with Kim Hwajong, who saved his life at the collapse of Mapo Bridge eighteen years earlier; was visibly shaken by learning that Choi is Cheon Taemin's maternal grandson; regards Cheon Taemin as an older brother despite no blood relation and has long held him in respect and fear; operates as Ares Guild's senior authority beneath its Guild Master

## Korean source

```text
＃410화



‘삼십여 년 만인가?’

이정룡은 마음속으로 중얼거렸다.

바람에 섞여 흘러들어 오는 수많은 몬스터의 악취와 피비린내. 그건 과거의 향수를 불러일으키는 전장의 냄새였다.

‘그래, 실로 오랜만이로군.’

그는 겉모습과는 어울리지 않는 노회한 눈빛으로 서서히 가까워지는 안개를 바라보았다. 어림잡아 수천의 몬스터가 도사리고 있을 희끄무레한 안개는 보는 것만으로도 불길함을 자아냈다.

대부분의 병력들이 동요하고 있었지만, 대격변의 산증인인 이정룡에게는 더없이 익숙한 광경이었다.

“자네 나이가 몇이지?”

이정룡이 불쑥 던진 물음에, 한 걸음 뒤에 서 있던 경호팀장 석고준이 대답했다.

“서른다섯입니다.”

“좋을 때군. 돌이켜 보면 나도 마찬가지였어. 하루하루 죽을 위기를 넘겨야 했지만, 그때는 꿈이 있었거든.”

이정룡은 깊은 눈빛으로 허공을 바라보았다.

젊었을 적 자신의 모습이 저 어딘가에 스쳐 지나가는 듯했다. 살아남겠다는 의지와 최고가 되겠다는 야심을 품은 청년.

그러나 삼십여 년이 지난 지금, 이 자리에 서 있는 사람은 칠순을 코앞에 둔 노인이었다.

“가끔 그런 의심이 들 때가 있지. 지금껏 쌓아 올린 모든 게 허물어지지는 않을까 하는 의심 말일세.”

“저는 추호도 의심치 않습니다.”

“어째서?”

석고준이 입술을 달싹였다.

- 스승님께서 계시니까요.

이정룡이 실소를 흘리며 대답했다.

- 내가 무너진다면 어찌하겠느냐?

- 단언컨대, 그럴 일은 없을 겁니다.

- 나도 누군가를 그렇게 생각했던 시절이 있었다. 누구보다 강하고, 평생을 바쳐도 넘을 수 없는 벽 같은 사람이었지.

- ……!

- 그는 대격변의 시작이고 끝이었으며 전부였다. 인류의 구세주였고 새로운 신이나 다름없었어. 하지만 그 역시 한낱 인간일 따름이었다.

불멸의 업적을 쌓은 영웅은 오랜 세월 모습을 드러내지 않았고 그에 관한 비밀을 아는 자는 손에 꼽는다.

그중 한 사람인 이정룡은 나직하게 말을 이었다.

- 영원한 것도, 확실한 것도 없다. 근래 들어 그런 생각이 많이 드는구나.

- ……진태경 때문입니까?

- 균열이 시작되면 붕괴는 한순간이다. 놈은 균열, 그 자체야.

- 무너지기 전에 균열을 메워야겠군요.

이정룡은 황량한 벌판으로 미끄러지는 안개를 바라보았다. 그의 입술 사이로 칼날을 감춘 부드러운 목소리가 흘러나왔다.

“준비는 되었는가?”

“받들겠습니다.”

깊게 고개 숙여 대답한 석고준이 검을 빼어 들었다.

스르릉. 차차창!

그의 뒤를 따라 동시에 수백, 수천 개의 병장기가 뽑혀져 나왔다.

수많은 레이드와 훈련을 거쳐 탄생한 아레스 길드의 정예들. 그리고 수많은 중국 헌터들의 손에 들린 병기가 뿜어내는 빛이 파도처럼 출렁였다.

“부디 명령을.”

석고준의 말에 이정룡은 천천히 걸음을 옮겼다.

이 자리에 군인과 화기가 설 자리 따위는 없다. 이것은 오롯이 헌터라는 이름의 초인(超人)과 몬스터의 싸움이며 이정룡은 전장의 신으로 군림할 것이다.

“가자.”

이정룡은 한 마디와 함께 바람처럼 쏘아졌다. 벌판을 가득 메운 안개가 그가 휘두른 검의 궤적을 따라 양 옆으로 갈라졌다.

콰아아아-!



* * *



퍼걱!

엄청난 악취를 풍기는 녹색 핏물을 뒤집어쓴 청년은 간신히 구역질을 참아냈다.

아니, 그럴 틈조차 주어지지 않았다는 것이 더 정확한 표현일지도 모른다.

후웅, 쾅!

타워 실드의 윗부분이 깨져 나가며 날카로운 파편이 코끝을 스쳤다. 촥, 핏물이 뿜어지며 혈향이 콧속을 파고든다.

덕분에 지독한 악취가 한결 가셨지만, 청년의 앞에는 죽은 지 얼마 되지 않아 보이는 언데드 오우거가 거대한 쇠몽둥이를 들어 올리고 있었다.

- 그어어어어!

후우우웅.

듣는 것만으로도 머리털이 쭈뼛서는 무시무시한 파공성.

청년은 이를 악물고 다리를 굽혔다. 마나를 불어넣은 타워 실드로 머리를 보호했다.

꽝!

엄청난 충격이 청년의 전신을 휩쓸었다. 이명과 함께 머리가 띵하고 팔이 부러진 것처럼 아프다.

‘아니, 어쩌면 이미 부러졌을지도.’

하지만 팔이 부러진 것 따위는 중요한 축에도 끼지 못했다.

흉포한 울음을 토해 내는 5m 신장의 괴물이 성인 남성만 한 쇠몽둥이를 팔랑개비처럼 휘두르고 있다면 더더욱 그렇다.

쾅! 쾅! 쾅!

미친듯한 공세에 청년은 울음기 섞인 비명을 내질렀다.

「야, 이 자라 좆 같은 새끼야! 왜 이렇게 세!」

청년은 베테랑 축에 속하는 B급 헌터였고 당연히 오우거를 상대해 본 경험도 있다.

오우거는 A급 몬스터답게 엄청난 완력과 체력을 지닌 놈이었지만, 이 정도로 강하지는 않았다.

분명 그랬었는데…….

쾅!

올해 초, 거금을 주고 구매한 고강도 타워 실드가 불과 다섯 번의 몽둥이질로 박살 나는 광경을, 청년은 넋 나간 눈빛으로 바라보았다.

‘이런 미친…… 이것들이 단체로 약이라도 처먹었나.’

강해도 너무 강하다. 희끄무레한 안개 사이로 다시 한번 들어 올려지는 쇠몽둥이를 바라보며, 청년은 마지막을 직감했다.

동시에 한 사람의 이름이 뇌리를 스쳤다.

‘진태경.’

이렇게 죽는 건 전부 그놈 때문이다.

그날, 진태경이 자신을 모른 척하고 지나가기만 했었어도 높으신 윗분께 조인트를 까일 일도 없었을 것이고 최전방 탱커로 차출되지도 않았을 것이다.

그리고 이렇게 죽을 일도 없었겠지.

후우우웅!

피할 엄두도 나지 않는다. 눈앞을 가득 메우며 달려드는 쇠몽둥이를 정면으로 바라볼 용기조차 없다.

눈을 질끈 감은 청년은 자신도 모르게 비명 같은 외침을 내질렀다.

「진태경, 이 빵즈 새끼야-!」

그리고 다음 순간.

서걱! 투두두두둑!

칠흑으로 물든 시야. 시원한 바람이 전신을 스치고, 무언가가 소나기처럼 쏟아 내린다.

이내 한 사람의 목소리가 귓가를 파고들었다.

“뭔 새끼?”

「……어?」

청년은 번쩍 눈을 떴다. 허공에서 점점이 흩뿌려지는 녹색 핏물. 목을 잃은 채 천천히 넘어가는 언데드 오우거의 거체가 보였다. 그리고 잔뜩 찌푸려진 한 사람의 얼굴도.

「……어어?」

“너 지난번 그 새끼지. 버디언.”

쐐액, 퍼걱!

보이지도 않았고, 볼 수도 없었다.

손을 뻗자 단검으로 짐작되는 한 줄기 섬광이 서너 마리의 몬스터를 관통한다. 실 끊긴 인형처럼 허물어지는 몬스터들.

청년의 입술 사이로 엉겁결에 대답이 튀어나왔다.

「아, 아닌데요.」

“아니긴 뭐가 아니야. 시벌놈이.”

파파팟! 파앙!

“위험해 보여서 살려 줬더니, 뭐? 빵즈? 넌 꼭 살아남아라. 늙어 죽을 때까지 빵셔틀만 시킬 테니까.”

서걱, 촤아아악!

이거 혹시 꿈인가?

눈을 한 번 깜빡일 때마다 주위에 있는 몬스터들이 볏짚처럼 쓰러지고 있었다.

푸른 불꽃이 솟구치고, 파공성이 터져 나오면 발 디딜 틈도 없이 빽빽하던 공간이 깨끗하게 청소된다.

모두 한 사람의 손끝에서 시작된 일이었고, 도무지 사람이 행한 것처럼 보이지 않는 일이었다.

청년은 그를 향해 넋 나간 얼굴로 물었다.

「당신은 혹시…… 신입니까?」

잠시 침묵하던 그, 진태경이 되물었다.

“너 혹시…… 병신이니?”

콰드드드득!

푸른 화염이 대지를 휩쓸었다. 강철이 녹아내리고 불길에 휩쓸린 몬스터가 고통에 찬 비명을 내질렀다.

단 한 번의 휘두름으로 수십 마리의 몬스터를 쓸어버린 진태경이 힐끗 청년을 바라보았다.

“야.”

「예? 예?」

“살아남아라. 빵셔틀 시킬 거니까.”

「예?」

“농담하는 거 아냐. 죽으면 내 손에 뒤진다.”

「……!」

“아, 그리고 이거.”

쐐액, 콰창!

빛살처럼 날아온 무언가가 청년의 이마에 부딪혀 산산이 조각났다.

미처 반응하기도 전에 반투명한 액체를 뒤집어쓴 청년의 귓가에 나직한 목소리가 파고들었다.

“이제 멀쩡해질 테니까 다시 싸워. 괜히 오우거한테 까불면 골로 가니까 좀 더 약한 놈들 위주로. 알겠냐?”

스스스스.

미약한 온기와 함께 스며드는 액체, 아니 포션.

전신에 가득한 상처와 부러진 팔이 회복하는 것을 느낀 청년이 멍하니 고개를 끄덕였다.

「예, 예.」

“그럼 간다.”

「조, 조심히 가십시오. 선생님.」

청년은 전장 한복판인 것도 잊은 채 깊숙이 허리를 숙였다.

그리고 다시 고개를 들었을 때, 진태경은 사라지고 일단의 무리가 그를 스쳐 지나가고 있었다.

쉬쉬쉬쉬쉭, 서걱!

진태경이 열어놓은 길을 따라 거침없이 내달리며 무기를 휘두르는 이백여 명의 헌터들.

그중에서도 단연 돋보이는 것은 선두에 선 두 사람이었다.

“&*^%!”

「진형이 허물어졌다! 돌격하라!」

뜻 모를 한국어를 쏟아 내는 미남자와 유난히 앳되어 보이는 어린 헌터.

두 사람의 움직임은 바람 같았고 눈부신 오러에 휩싸인 검신은 몬스터를 조각냈다.

‘결사대.’

이야기는 들었다. 진태경을 포함한 일부 S급 헌터들이 각 전선의 결사대를 이끌고 돌격, 아크 리치를 칠 거라는 걸.

어제만 해도 말도 안 되는 헛소리라 생각했는데…….

‘굉장하다.’

나도 저렇게 될 수 있을까.

망연하게 그 광경을 바라보던 청년은 문득 가슴이 뜨거워졌다. 어디선가 자신도 모르는 힘이 솟구쳐 주체할 수 없었다.

그는 반쯤 박살 난 타워 실드를 치켜세우고, 가장 가까이에 있는 몬스터를 향해 달려들었다.

「이야아아아아!」

- 구어어어어어!

후우우웅, 콰광!

“…….”

젠장. 오우거였다.

완전히 박살 난 타워 실드를 바라본 청년은 냅다 등을 돌려 도망치기 시작했다.

‘오크. 오크 어디 있어!’



* * *



퍽!

‘끝났군.’

주먹 끝으로 전해지는 느낌이 제대로다. 머릿속을 스치는 확신과 함께, 내 목덜미를 향해 이빨을 들이밀던 라이칸스로프의 머리가 터져 나갔다.

띠링.



- [Lv.92 어둠에 물든 라이칸스로프]를 처치하셨습니다!

- 소량의 경험치를 획득했습니다!



라이칸스로프 주제에 레벨이 90대라고?

레벨이 절대적인 지표가 아닌 것은 이미 알고 있던 사실이지만, 이 전장에 모인 몬스터들은 게이트에서 봐 왔던 놈들과는 확실히 달랐다.

‘더 강해.’

레벨도 조금 더 높고, 민첩이나 완력도 뛰어나다.

한두 놈이라면 그러려니 하겠는데, F급 몬스터인 고블린부터 A급 몬스터까지 이 지경이니 이상함을 느끼지 않으면 병신인 수준이었다.

“진태경 씨!”

「형님!」

등 뒤에서 들려오는 다급한 외침에 고개를 돌리자, 내가 뚫은 길을 물샐 틈 없이 메운 몬스터들이 보였다.

놈들을 상대로 치열하게 싸우는 결사대의 모습도.

“전부 꺼져.”

퍼버버버벅!

몬스터들에게 있어 나는 막을 수도 없고, 피할 수도 없는 존재다.

포탄처럼 쏘아진 수십 개의 권영(拳影)이 놈들의 머리 위로 쏟아진다.

더러는 피곤죽이 되어 저 멀리 나가떨어지고, 더러는 그 자리에서 허물어진다.

나는 순간 텅 비어 버린 공간을 향해 쇄도했다.

서거거거걱!

강기(罡氣)를 머금은 창날이 뼈와 살을 가르며 사방을 난도질했다. 쓰러지는 놈들의 숫자만큼, 시스템 알림이 끊임없이 울려왔다.

띠링. 띠링. 띠링.



- [Lv.55 어둠에 물든 오크 워리어]를 처치하셨습니다!

- 극소량의 경험치를 획득했습니다!

- [Lv.83 어둠에 물든 리저드 메이지]를 처치하셨습니다!

- 극소량의 경험치를…….



이어 오랜만에 듣는 경쾌한 종소리까지.



- 레벨 업!

- 레벨 업의 효과로 피로와 일부 부상이 회복됩니다!

- 10포인트를 획득했습니다!

- 몸 상태가 최고조에 달합니다!



느껴진다. 서서히 소모되고 있던 공력이 충만하게 차오르고, 신체에 축적된 피로가 씻은 듯이 사라지는 것이.

하지만 더 중요한 사실이 있었다.

“최 팀장님! 샤오 쉔!”

“예!”

「말씀하십시오!」

나는 전장 전체를 울릴 만큼 큰 목소리로 외쳤다.

“안개! 안개의 범위에서 최대한 벗어나!”

이건 기분 나쁘고 축축하기만 한 안개가 아니라, 아크 리치가 부린 일종의 마법이다.

범위 안의 몬스터를 더욱 강화, 아니 ‘어둠에 물들게’ 하는.

‘빌어먹을 마법.’

내가 주위에 가득한 정체 모를 안개를 노려보던 그 순간.

콰아아아앙!

하늘이 쪼개지는 듯한 굉음이 천지에 울려 퍼졌다.
```

## Final English reading copy

```markdown
# Chapter 410

*Has it been more than thirty years?*

Lee Jungryong muttered to himself.

The stench of countless monsters and the smell of blood drifted in on the wind. It was the scent of a battlefield, one that stirred up nostalgia for the past.

*Yes. It truly has been a long time.*

With a shrewd gaze that seemed at odds with his appearance, he watched the fog slowly draw nearer. The pale fog, where thousands of monsters were presumably lurking, radiated an ominous feeling simply by being there.

Most of the troops were shaken, but to Lee Jungryong—a living witness to the Great Cataclysm—it was an entirely familiar sight.

“How old are you?”

At Lee Jungryong’s sudden question, Go Jun, the head of his security team standing one step behind him, answered.

“Thirty-five.”

“That’s a good age. Looking back, I was the same. I had to survive one brush with death after another every day, but I had dreams back then.”

Lee Jungryong gazed into the empty air with deep eyes.

It was as if his younger self were passing somewhere in the distance—a young man carrying the will to survive and the ambition to become the best.

But more than thirty years later, the man standing here was an old man nearing seventy.

“Sometimes, doubt creeps in. Doubt that everything I’ve built might come crashing down.”

“I have not the slightest doubt.”

“Why not?”

Go Jun’s lips moved.

“Because you are here, Master.”

Lee Jungryong gave a quiet laugh.

“What would you do if I fell?”

“I can guarantee that will never happen.”

“There was a time when I thought of someone that way too. Someone stronger than anyone else, a wall I could never overcome even if I devoted my entire life to it.”

“……!”

“He was the beginning and the end of the Great Cataclysm. He was everything. He was humanity’s savior, no different from a new god. But he, too, was nothing more than a human being.”

The hero who had accomplished immortal feats had not shown himself for a long time, and only a handful of people knew the secrets surrounding him.

As one of those few, Lee Jungryong continued in a low voice.

“Nothing is eternal, and nothing is certain. I’ve been thinking that a lot lately.”

“……Is this because of Jin Taekyung?”

“When a crack begins, collapse comes in an instant. That bastard is the crack itself.”

“Then we must seal it before everything collapses.”

Lee Jungryong watched the fog slide across the desolate plain. A gentle voice with a hidden blade flowed from between his lips.

“Are you ready?”

“I am at your command.”

Go Jun bowed deeply and drew his sword.

*Shing! Clatter!*

Hundreds, then thousands, of weapons were drawn at the same time behind him.

They were the Ares Guild’s elites, forged through countless raids and training. The weapons held by them and by countless Chinese Hunters gleamed and rippled like waves.

“Please give the command.”

Lee Jungryong slowly began to walk.

There was no place here for soldiers or firearms. This was purely a battle between superhumans known as Hunters and monsters, and Lee Jungryong would reign as the god of the battlefield.

“Let’s go.”

With that single word, Lee Jungryong shot forward like the wind. The fog filling the plain split apart on both sides along the path of his sword.

*Kraaash!*

* * *

*Splurt!*

The young man drenched in green blood that reeked horribly barely managed to suppress his gagging.

No—that was not quite right. More accurately, he had not even been given time to gag.

*Whoosh! Boom!*

The upper section of his tower shield shattered, and a sharp fragment grazed the tip of his nose. Blood spurted out, and the scent of it pierced his nostrils.

The foul stench faded somewhat thanks to that, but an undead ogre that appeared to have died only recently was raising a massive iron club in front of him.

“Grrrraaaaah!”

*Whoooooosh.*

The terrifying sound of something tearing through the air was enough to make the hair on his head stand on end.

The young man gritted his teeth and bent his legs. He used the mana-infused tower shield to protect his head.

*Boom!*

A tremendous impact swept through his entire body. His head rang, and his arm hurt as if it had been broken.

*No. Maybe it’s already broken.*

But a broken arm was nowhere near important enough to count among his concerns.

Especially not when a five-meter-tall monster roaring ferociously was swinging an iron club as large as an adult man like a pinwheel.

*Boom! Boom! Boom!*

Under the monster’s insane assault, the young man let out a scream edged with tears.

“You turtle-dicked bastard! Why are you so strong?!”

The young man was a veteran B-rank Hunter, and of course, he had fought ogres before.

As befitted an A-rank monster, an ogre possessed tremendous strength and stamina, but they had never been this strong.

They definitely hadn’t been…

*Boom!*

The young man stared blankly as the high-strength tower shield he had bought for a fortune at the beginning of the year was smashed to pieces in only five blows.

*What the hell… Did all of these things take drugs together?*

They were far too strong. As he watched the iron club rise once more through the pale fog, the young man sensed his end.

At the same time, a name flashed through his mind.

*Jin Taekyung.*

This was all that bastard’s fault.

If Jin Taekyung had simply pretended not to know him and walked past that day, he would never have gotten his shins kicked by some big shot or been drafted as a frontline tank.

And he would not be about to die like this.

*Whoooooosh!*

He did not even dare think about dodging. He lacked the courage even to look straight at the iron club rushing toward him and filling his entire field of vision.

The young man squeezed his eyes shut and unconsciously let out a scream.

“Jin Taekyung, you bangzi bastard!”[^1]

[^1]: *Bangzi* is a derogatory Chinese term for a Korean. Jin twists the insult into a threat to make the Hunter run bread for him, echoing Korean school slang for a bullied errand-runner.

And then, the next moment—

*Slash! Rattle-rattle-rattle!*

His vision was dyed pitch-black. A cool breeze brushed across his entire body, and something poured down like a sudden shower.

Soon, a voice pierced his ears.

“What kind of bastard?”

“……Huh?”

The young man’s eyes flew open. Green blood was scattering through the air in droplets. The enormous body of the undead ogre, now missing its head, was slowly toppling over.

And there was the face of a man scowling deeply.

“……Huh?”

“You’re that bastard from last time. Burdian.”

*Whoosh! Splurt!*

He could not see it. He could not even follow it.

The man reached out, and a streak of light that seemed to be a dagger pierced through three or four monsters. They collapsed like puppets with their strings cut.

An answer escaped the young man’s lips before he could think.

“Uh, no, I’m not.”

“No, my ass. You fucking bastard.”

*Slash! Bang!*

“You looked like you were in danger, so I saved you, and you call me a bangzi? You’d better survive. I’ll make you run bread for me until you die of old age.”

*Slash! Sssshk!*

*Is this a dream?*

Every time the young man blinked, the monsters around him were falling like bundles of straw.

Blue flames erupted, and whenever the air split with a shriek, the space that had been packed so tightly there was nowhere to step was swept clean.

Everything began at a single man’s fingertips, and none of it looked like something a human being could have done.

The young man stared at him blankly and asked,

“Are you… perhaps a god?”

After a moment of silence, the man—Jin Taekyung—asked in return.

“Are you perhaps… a fucking idiot?”

*Graaaaaaak!*

Blue flames swept across the earth. Steel melted, and monsters caught in the blaze screamed in agony.

After wiping out dozens of monsters with a single swing, Jin Taekyung glanced at the young man.

“Hey.”

“Yes? Yes?”

“Survive. I’m going to make you run bread for me.”

“Excuse me?”

“I’m not joking. If you die, I’ll kill you myself.”

“……!”

“Oh, and this.”

*Whoosh! Crack!*

Something flew toward the young man like a ray of light and struck him in the forehead, shattering.

Before he could react, the young man was drenched in translucent liquid, and a quiet voice reached his ears.

“You’ll be fine now, so get back to fighting. Don’t go picking fights with ogres for no reason. Stick to the weaker ones. Got it?”

*Hissss.*

The liquid—no, the potion—seeped into him with a faint warmth.

The young man felt the wounds covering his entire body and his broken arm begin to heal. He nodded blankly.

“Yes, yes.”

“Then I’m off.”

“P-Please be careful, sir.”

Forgetting that he was in the middle of a battlefield, the young man bowed deeply at the waist.

When he raised his head again, Jin Taekyung was gone, and a group was rushing past him.

*Whoosh-whoosh-whoosh! Slash!*

More than two hundred Hunters raced forward without hesitation along the path Jin Taekyung had opened, swinging their weapons.

Two people at the very front stood out above all the rest.

“&*^%!”

“The formation has collapsed! Charge!”

A handsome man spouting incomprehensible Korean and a Hunter who looked especially young.

The two moved like the wind, and their sword blades, wrapped in dazzling aura, cut the monsters apart.

*The suicide squad.*

He had heard the story. Some of the S-rank Hunters, including Jin Taekyung, would lead the suicide squads on each front in a charge against the Arch Lich.

Only yesterday, he had thought it was impossible nonsense…

*Amazing.*

*Could I become like that too?*

As the young man gazed blankly at the scene, his chest suddenly grew hot. Some unknown strength surged up from within him, and he could not contain it.

He raised his half-destroyed tower shield and charged toward the nearest monster.

“Yaaaaaaaah!”

“Grrrraaaaah!”

*Whoosh! Boom!*

“……”

Damn it. It was an ogre.

The young man stared at his completely destroyed tower shield, then immediately turned and ran.

*Orcs. Where are the orcs?!*

* * *

*Thud!*

*It’s over.*

The sensation traveling through the end of my fist was exactly right. With that certainty flashing through my mind, the head of the Lycanthrope snapping its teeth toward the back of my neck exploded.

> **System**
> *Ding!*
> - You defeated Lv. 92 Darkened Lycanthrope!
> - You gained a small amount of EXP!

A Lycanthrope at level 90-something?

I already knew that Level was not an absolute measure, but the monsters gathered on this battlefield were definitely different from the ones I had seen in Gates.

*They’re stronger.*

Their Levels were somewhat higher, and their Agility and strength were superior too.

If it had been one or two monsters, I might have brushed it off. But everything from F-rank goblins to A-rank monsters was like this. You would have to be an idiot not to find it strange.

“Mr. Jin Taekyung!”

“Hyung!”

I turned at the urgent voices coming from behind me and saw monsters filling the path I had opened without leaving a single gap.

The suicide squad was fighting desperately against them.

“Get the hell out of here—all of you.”

*Boom-boom-boom-boom!*

For the monsters, I was an existence they could neither block nor evade.

Dozens of fist shadows shot out like cannonballs and rained down over their heads.

Some were sent flying into the distance as bloody pulp. Others simply collapsed where they stood.

I charged into the space that had momentarily been emptied.

*Slash-slash-slash!*

A spearhead imbued with Force cut through bone and flesh, hacking in every direction. As the monsters fell, System notifications rang out without pause.

> **System**
> *Ding! Ding! Ding!*
> - You defeated Lv. 55 Darkened Orc Warrior!
> - You gained an extremely small amount of EXP!
> - You defeated Lv. 83 Darkened Lizard Mage!
> - You gained an extremely small amount of EXP…

Then came the cheerful chime I had not heard in a long time.

> **System**
> *Ding!*
> - **Level Up!**
> - The effects of leveling up relieve fatigue and heal some injuries!
> - You obtained 10 points!
> - Your physical condition is at its peak!

I could feel it. The internal energy that had been slowly draining away was filling to the brim, and the fatigue accumulated in my body was vanishing as if it had been washed away.

But there was something more important.

“Team Leader Choi! Shao Shen!”

“Yes!”

“Give us your orders!”

I shouted in a voice loud enough to shake the entire battlefield.

“Fog! Get as far outside the fog’s range as possible!”

This was not merely unpleasant, damp fog. It was a kind of magic wielded by the Arch Lich.

Magic that strengthened the monsters within its range—or rather, made them *Darkened*.

*Damn magic.*

At that very moment, as I glared at the mysterious fog filling the area around me—

*Kraaaa-boom!*

A thunderous roar that made it seem as if the sky had split apart echoed across heaven and earth.
```

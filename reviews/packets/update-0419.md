<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0419.txt",
      "sha256": "9ee623b4d7bc2fe1578fcdb6e1994e018f769aaea6f575899a2cb12667cbc9fb",
      "bytes": 13591
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "72629a7cb1382c95cb1ffe673b8d195ae873ccb6e9f882f96a634935c3d62fa2",
      "bytes": 1996
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "0c65c80cca3b94ba7b9a821e4917bcc55788f61aae6d0adf00efe413959aaa83",
      "bytes": 139066
    },
    {
      "path": "characters/Cheon Taemin.md",
      "sha256": "0c524e4203c046e050ef1b305ef0c1f9d3a44cc9e2d5a2d4118df687b1185e9c",
      "bytes": 590
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "d121784078523aa79ecffc1fbb2397936d1847e5fa76abeafc2bd5853cddb86a",
      "bytes": 533
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "dfa552aabaa99478f20e42d03a34f5dfe4feaf17558bfbecb7c4f43161939f4f",
      "bytes": 1270
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "771899b49c5132084e85ed31a7c41af3b640a32a44987ed81d5c6ede5811f7b9",
      "bytes": 622
    },
    {
      "path": "characters/Lee Jungryong.md",
      "sha256": "90c8deb92cb0df72826427c8a3fb95a1d58b353379bd08bc5295faa426022205",
      "bytes": 1178
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "940557f954a71b0f703d9dc184cddc2db5445f6e50fa5b0710904f654a04fb88",
      "bytes": 128217
    }
  ],
  "estimated_tokens": 9986
}
-->

# Durable State Update — Chapter 419

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 419. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 419. Profile updates may replace only one
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
  "chapter": 419,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 419,
    "continuity_sources": [419],
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
    "Jin Taekyung killed Wu Heixing, and the System warned that public knowledge of the killing would cause significant repercussions.",
    "Lee Jungryong recorded an edited hologram of Wu's death and intends to use it to turn public opinion against Jin and those he protects.",
    "Lee treated Wu Heixing as a disposable tool and has begun fighting Jin with his full strength.",
    "Lee's exceptional swordsmanship, Force, and qi control initially wounded Jin and disrupted his internal energy.",
    "Jin recognized his arrogance, endured Lee's assault, and resumed attacking with the Fire Dragon Divine Spear.",
    "Lee claims that no one can destroy the empire he built, including Jin, Choi Minwoo, or his unidentified hyung.",
    "The city remains in the process of transforming into one enormous Gate through the Arch Lich's anchored mana.",
    "The Quest One Who Returned from Death remains active, keeping Login unavailable until the Quest ends.",
    "The Skeleton Warlord continues to suffer unexplained dizziness and nausea while urging Jin to turn back."
  ],
  "continuity_sources": [
    418
  ],
  "open_questions": [
    "Can Jin Taekyung defeat Lee Jungryong after being wounded and having his internal energy disrupted?",
    "Who is the person Lee Jungryong calls hyung, and what connection does he have to Lee's empire?",
    "Can the three Hunters stop the city's Gate transformation?",
    "What is causing the Skeleton Warlord's dizziness and insistence that they turn back?"
  ],
  "safe_through": 418,
  "temporary_decisions": [
    "Render 아크 리치 as Arch Lich and 게이트화 as Gate transformation.",
    "Render 어둠에 잠식된 도시 as City Consumed by Darkness.",
    "Render 죽음에서 돌아온 자 as One Who Returned from Death.",
    "Render 착짱죽짱 as “The only good chink is a dead chink.”",
    "Render 형님 as hyung when Lee uses it, without resolving the person's identity."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 천태민    | **Cheon Taemin**  |
| 이정룡    | **Lee Jungryong** |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 레벨               | **Level**                      |
| 경험치              | **EXP**                        |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 몬스터     | **monster**           |
| 길드      | **Guild**             |
| 대격변     | **Great Cataclysm**   |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 아레스 | **Ares Guild** | The leading Guild in Korea; formerly employed Team Leader Choi and Song Song. |
| 출혈 | **Bleeding** | Effect with a 90% activation chance on a successful spear hit. |
| 화시 | **fire arrow** | Flaming arrow Lee Seowol fires to signal Cheol Mubaek. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 절체절명 | **Life-or-Death Crisis** | Sudden System Quest forcibly accepted during the confrontation at Mount Song. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 이정룡 | 진태경 | senior S-rank Hunter to younger Hunter and adversary | Young man | polished, teasing, and veiled-threatening | Uses a genial tone and indirect threats while trying to make Taekyung release the captives. |
| 진태경 | 이정룡 | younger Hunter to senior S-rank Hunter and adversary | you | polite but mocking and defiant | Taekyung answers Lee's soft threats with the wolf-and-tiger metaphor and refuses to yield. |
| 이정룡 | 천태민 | younger_to_older_brother_by_choice | older brother | reverent and familiar; internal | Lee Jungryong uses 형님 in unspoken thoughts and regards Cheon Taemin as an older brother despite having no blood relation. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |

## Listed compact profiles

### Cheon Taemin.md

# Cheon Taemin (천태민)

- **Safe through:** Chapter 409
- **Aliases:** Slayer
- **Role:** Ares Guild Master; humanity's great hero and the world's greatest Hunter; killed the Demon King and is known as the Slayer; created the first Mana Cultivation Method during the Great Cataclysm.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** Maternal grandfather of Team Leader Choi and father of Soyeong; regarded by Lee Jungryong as an older brother despite their lack of blood relation.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 418
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who has sworn never to kill again.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 418
- **Aliases:** Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, and a Supreme Peak master who has manifested Force and crossed the wall into true mastery.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and student, his mother and sister Hayeon are among those he protects, and the Skeleton Warlord is his captive undead commander.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 418
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Lee Jungryong.md

# Lee Jungryong (이정룡)

- **Safe through:** Chapter 418
- **Aliases:** None
- **Role:** Vice Guild Master of Ares Guild, one of Korea's two S-rank Hunters, and a Supreme Peak-level martial artist who directs Ares Guild operations.
- **Personality:** Outwardly genial, calm, and humorous; calculating, opportunistic, manipulative, coercive, and ruthless when challenged
- **Voice:** Smooth, good-natured, and indirect, using teasing conversation and veiled threats before becoming openly furious
- **Relationships:** Master of Park Jihoon and Go Jun (Team Leader Seok), whom he personally selected and trained; longtime Great Cataclysm acquaintance of Park Tae Seop; adversary of Jin Taekyung; knew Team Leader Choi from childhood; has an antagonistic history with Kim Hwajong, who saved his life at the collapse of Mapo Bridge eighteen years earlier; was visibly shaken by learning that Choi is Cheon Taemin's maternal grandson; regards Cheon Taemin as an older brother despite no blood relation and has long held him in respect and fear; operates as Ares Guild's senior authority beneath its Guild Master

## Korean source

```text
＃419화



이정룡은 문득 생각했다.

‘어디서부터, 무엇이 잘못되었을까.’

형님의 핏줄을 몰아내고 아레스 길드를 장악한 것?

각종 불법을 저질러 끊임없이 길드를 성장시키고, 그러고도 만족하는 법 없이 욕심을 채워 나간 것?

그것도 아니라면…….

‘저 녀석과 적이 된 것?’

이정룡의 시선이 한 사람에게 닿았다. 출혈로 인해 전신 곳곳이 피로 물들어 있는 청년.

하늘을 바라보며 크게 심호흡한 그가 입술을 뗐다.

“정룡아.”

어째서일까. 그 나직한 목소리를 듣는 순간 이정룡은 등골이 서늘해졌다. 상처 하나 입지 않았음에도 날붙이에 베인 기분이다.

그런 그를 바라보는 청년, 진태경의 입가에 광포한 웃음이 맺혔다.

“발톱 자르자.”

“……!”

파팟!

바람이 불고, 두 사람 사이에 존재하던 공간이 사라진 그 순간. 이정룡은 파공성과 함께 검을 휘둘렀다.

쉬익!

눈부신 기의 집약체가 진태경의 몸뚱어리를 갈랐다. 하지만 뿜어져 나와야 할 핏물 대신 바람이 흩어졌다.

실체가 아닌 잔상(殘像). 이정룡의 머릿속에서 붉은색 경종이 울렸다.

‘뒤!’

검을 휘두르기에는 너무 늦었다. 이정룡은 번개처럼 돌아서며 주먹을 내질렀다. 새하얀 오러에 휩싸인 주먹과, 푸른 화염이 실린 손바닥이 부딪쳤다.

꽈앙!

세상이 뒤흔들렸다. 아니, 흔들린 것은 이정룡의 시야였다.

항거할 수 없는 힘에 튕겨 나간 그가 허공에서 몸을 뒤집으며 신형을 바로잡았다.

주먹이 시큰거리고 속에서 무언가가 울컥 솟구쳤다. 하지만 핏물을 뱉어 낼 틈조차 주어지지 않았다.

쐐애애액!

어느새 코앞까지 들이닥친 창날. 진태경이 쏘아 보낸 창이 이정룡의 가슴을 노렸다. 이를 악문 그가 온 힘을 불어넣어 검을 쳐올렸다.

카가가가각! 쾅!

아슬아슬하게 빗나간 창이 콘크리트를 부수며 거대한 크레이터를 남겼다.

창을 흘리는 데에는 성공했지만, 가공할 만한 힘과 회전력에 찢어진 손아귀에서는 피가 튀었다.

하지만 이정룡은 개의치 않고 자욱한 먼지구름 너머로 발을 뻗었다.

퍼엉-!

쾌속한 속도를 이기지 못한 먼지와 안개가 뿔뿔이 흩어졌다. 이정룡이 내디딘 걸음의 끝엔, 한 사람이 있었다.

“저돌적인데? 내 취향이야.”

어느새 새로운 창을 든 진태경이 종횡으로 창날을 내리그었다. 공간이 갈라지고 화염이 솟구쳤다. 이정룡이 내지른 검 끝은 그 중심을 정확히 꿰뚫었다.

후웅, 펑!

압축된 공기가 터져 나갔다. 화염이 갈라지고 새로운 길이 열렸다. 화살처럼 쏘아진 이정룡의 신형이 진태경을 향해 달려들었다.

‘죽어라.’

오직 한 가지 일념(一念)을 담은 검은 휘황하게 빛났고, 빛처럼 빨랐다.

그러나 느려진 세상 속에서 바라본 진태경의 눈은 분명 웃고 있었다.

‘이건…….’

무엇인가 잘못됐다.

이정룡의 생각이 미처 이어지기도 전에, 창을 쥔 진태경의 손이 흐릿해졌다.

동시에 당장이라도 그의 목젖을 파고들 것 같던 검신을 후려치는 거대한 힘이 있었다.

쉭! 꽈앙!

귓가가 먹먹해질 만한 굉음이 울려 퍼졌다. 자의와는 상관없이 십여 미터를 미끄러진 이정룡은 치밀어 오르는 핏물을 삼켰다.

‘아직 끝나지 않았다.’

쓰러져서도, 약한 모습을 보여서도 안 된다. 그는 이정룡이다. 인류 역사상 어느 때보다 격렬했던 대격변이라는 소용돌이를 헤쳐 나온 장본인이자, 시대가 낳은 한 사람의 효웅(梟雄).

이정룡은 거미줄 같은 실금이 간 검을 움켜쥐었다.

‘죽지 않는다. 죽을 수 없다.’

이 자리에 오르기까지 많은 우여곡절이 있었다. 아득한 절망도 겪었고, 참을 수 없이 분노한 날도 있었다.

누군가의 그림자에 가려져, 이인자라는 이름으로 반평생을 살았다.

아니, 어쩌면 지금조차도.

하지만…….

“더 이상은 아니다.”

투둑. 투두두둑.

전신의 혈관이 도드라지고 근육이 부풀었다. 이정룡의 전신에서 일어난 강대한 기운이 사방을 짓눌렀다.

최후의 최후를 위해 남겨 둔 마지막 힘까지 모조리 끌어올린 그는 핏발 선 눈으로 진태경을 노려보았다.

“그는 이제 존재하지 않는 사람이나 다름없다. 세계 최고는…… 바로 나다.”

우우우웅.

이정룡을 둘러싼 모든 것이 부르르 떨렸다. 그런 그를 바라보는 진태경의 눈빛은 일말의 흔들림 없이 차분했다.

“글쎄, 내 생각에는 아닐 것 같은데.”

콰아아아!

두 사람의 전신에서 흘러나온 기파가 사방을 할퀴었다.

찰나를 쪼개고 쪼갠 짧은 순간 속, 그들은 동시에 서로를 향해 달려들었다.



* * *



꽈앙!

격돌은 섬광과도 같았고, 여파는 거대했다. 세상을 뒤흔드는 굉음 속에서 그들은 두 줄기의 바람이 되어 뒤섞였다.

푸른 화염을 머금은 창날과 눈부시도록 밝은 빛에 휩싸인 검이 서로를 향해 날아들었다.

쉬쉬쉬쉬쉭!

공간을 격하며 달려드는 빛무리.

지면을 박차며 솟구친 진태경이 엄청난 기세로 창을 내리꽂았다. 일 격, 이 격, 삼 격. 검을 부딪쳐 갈 때마다 굉음과 함께 엄청난 충격파가 터져 나왔다.

어느새 이정룡의 입가에서 흘러나온 핏물이 점점이 흩뿌려졌다.

“쿨럭.”

순간 휘청이는 신형. 늙은 사자가 찰나 보인 약한 모습에 젊은 숫사자가 이빨을 들이민다.

횡으로 휘둘려진 창날이 이정룡의 옆구리를 힘차게 베어 왔다.

쾅!

지진이라도 난 것처럼 땅이 흔들렸다.

서로의 숨이 닿을 만큼 가까운 거리, 가까스로 창을 막아낸 이정룡은 맞댄 무기 사이로 화염을 쏟아 내고 있는 한 쌍의 눈동자와 시선이 마주쳤다.

‘젊구나. 과거의 내가 그랬던 것처럼.’

어째서였을까. 하필이면 이런 상황에서 문득 그런 생각이 든 이유는.

보잘것없고 초라했던 자신의 옛 모습을 떠올리느라, 화염에 휩싸여 날아드는 진태경의 손바닥을 막지 못한 것은.

퍼엉-!

뜨겁다. 전신을 빈틈없이 보호하고 있던 기운이 깨져 나가고 끔찍한 열기가 폐부로 스며든다.

눈앞을 물들이는 푸른 화염과 고통 속에서, 이정룡의 뇌리에 오래전의 기억들이 쏜살같이 스쳐 지나갔다.



‘이름이?’

‘예?’

‘아, 그쪽한테 물은 거 맞아요.’

‘갑자기 웬 통성명입니까?’



대격변 초기. 수많은 몬스터에 포위된 절체절명의 상황에서 만난 한 사람.



‘그냥. 내 또래로 보이길래. 반가워서.’

‘젊은 친구가 갑자기 말이 짧아지시네. 나보다 한참 어려 보이는데.’

‘그럼 친구 할까요. 난 상관없는데.’

‘……이런 상황에서 그런 말이 나옵니까?’

‘좀 그런가.’



죽음에 대한 공포로 반쯤 미쳐 버린 놈이라고 생각했다.

그 미친놈이 홀연히 앞으로 나서 수천 마리가 넘는 몬스터를 휩쓸어 버리기 전까지는.

콰드드득!



‘이런 미친…….’

‘이때다! 돌격-!’



전투가 끝난 후, 그가 다시 찾아와 던진 물음은 처음과 같았다.



‘이름이?’

‘이정룡……입니다.’

‘이름 멋있다. 그럼 나이는? 오. 내가 다섯 살 많네. 얼마 차이도 안 나는데 그냥 친구 할까요?’

‘아닙니다. 형님.’



그는 빌어먹을 정도로 동안이었고, 믿을 수 없을 만큼 강했다.

A급 헌터 이정룡은 그와의 첫 만남에서 자신의 영웅을, 동시에 넘을 수 없는 거대한 산맥을 발견했다.



‘그런데, 형님.’

‘응?’

‘혹시 성함이…….’

‘아, 내가 아직 말을 안 해 줬구나.’



그는 씩 웃으며 말했었다.



‘천태민.’



천태민. 천태민. 천태민…….

몇 번을 되뇌어도 큰 울림을 남기는 한 사람의 이름. 잊으려 해도 뇌리에 각인 된 얼굴.

이정룡의 인생에 거대한 그림자를 드리운 거인.

“꺼져! 당장 내 앞에서 사라지란 말이다-!”

이정룡은 끓어오르는 음성으로 부르짖었다. 고통으로 새하얗게 물들었던 시야가 유리처럼 깨어져 나가고 귓가를 스치는 바람이 맹렬하다.

정신을 차린 다음 순간, 이정룡은 엄청난 충격과 함께 고층빌딩을 뚫고 차가운 콘크리트에 처박혔다.

콰과광!

“쿨럭.”

입술 사이로 튀어나온 검붉은 핏물.

시야는 흐릿했고 사지 곳곳에서 고통이 엄습했다. 모조리 부서진 갈비뼈가 내장을 건드렸는지 호흡이 힘겨웠으며, 부러진 왼팔과 다리는 힘없이 덜렁거렸다.

‘포션, 포션을…….’

마지막 기회다. 잠시라도 공격이 멈춘 이때 상처를 치료해야 한다.

이정룡은 그나마 성한 오른팔로 옆구리를 더듬었지만, 아공간 주머니가 있어야 할 그곳은 텅 비어 있었다.

대신 그가 발견한 것은 저 멀리 자신을 향해 다가오는 한 사람이었다.

“아, 혹시 이거 찾냐?”

데구르르르. 툭.

마법으로 강화된 유리병 하나가 굴러와 이정룡의 발치에 닿았다.

숨만 붙어 있다면 누구든 살려 낸다는 기적의 물약, 바로 최상급 포션이었다.

다만 그가 기억하는 마지막 상태와는 상당한 차이가 있었지만.

“하도 목이 말라서 마셨는데 진짜 시원하더라. 약수터 어디 다녀?”

천연덕스럽게 말하며 다가오는 그의 모습에, 이정룡은 헛웃음을 흘렸다.

‘진태경.’

이름, 얼굴, 성격. 모든 것이 다르다.

하지만 지금 이 순간, 이정룡은 마침내 깨달을 수 있었다.

진태경을 처음 마주했던 그 날, 가슴 깊숙한 곳에서 느꼈던 불안감과 흥미라는 두 글자로 포장하여 애써 외면했던 익숙함을.

“정룡아.”

귓가를 파고드는 나직한 목소리.

어느새 코앞으로 다가온 진태경의 얼굴 위로 겹쳐지는 한 사람의 모습.

이정룡은 신음처럼 중얼거렸다.

“너는, 넌 도대체 누구냐.”

묻고 싶었다. 미치도록 궁금했다.

어찌하여 이렇게까지 그를 닮을 수 있는지.

그를 따라 무수한 업적을 세우며 영웅이라 추앙받는 자신이 아니라, 저런 F급 헌터 따위가 더 강해질 수 있었는지!

“나?”

다음 순간, 입가에 미소를 띤 진태경이 말을 이었다.

“정룡이 담당일진.”

그리고 먼 곳에서 부딪쳐 돌아오는 메아리처럼, 이정룡의 케케묵은 기억 속에 존재하는 누군가의 얼굴과 목소리가 겹쳐졌다.



‘형제. 의형제지.’



다른 말, 다른 의미를 담아 말한 두 사람 모두 웃고 있었다.

그 빌어먹을 정도로 닮은 웃음을 멍하니 바라보던 이정룡은 천천히, 아주 천천히 입을 열었다.

“나는…….”

수십 년의 세월, 수많은 감정이 떠오르고 사라진다.

찰나에 불과했으나 영원과도 같았던 기다림 끝에, 공허한 목소리가 입술 사이를 비집고 흘러나왔다.

“후회하지 않는다. 결코.”

한 줌의 후회조차 없냐 묻는다면, 아니었다.

그러나 이정룡은 후회할 수 없다. 후회하기 싫었다. 그저 이것이 가장 자신에게 어울리는 최후라 믿었다.

“죽여라.”

환하게 미소 지은 이정룡을 향해, 서늘한 한 마디가 떨어져 내렸다.

“유언. 잘 들었다.”

화르륵.

목소리와는 다른, 푸른 화염을 머금은 창날과 함께.



* * *



초고온의 열기를 머금은 화염은 순식간에 타올랐고, 모든 것을 태운 뒤 사그라졌다.

녹아내린 콘크리트와 검게 그을린 그곳에 남은 것은 한 사람이 있었던 흔적.

그리고 세상에서 오직 한 사람만이 들을 수 있는 종소리뿐이었다.

띠링.



- [Lv.153 이정룡]을 처치했습니다!

- 막대한 경험치를 획득했습니다!

- 레벨 업!

- 레벨 업!



경쾌한 시스템 알림을 들으며 천천히 창을 거둬들였다.

‘빌어먹을 늙은이.’

마지막에 봤던 그 웃음이 자꾸만 생각난다.

이정룡은 어떤 삶을 살았고 마지막엔 무슨 생각을 했을까. 거기에 더해 그가 보여 준 움직임과 이상한 행동들은…….

‘아냐. 나중에 생각하자.’

나로서도 이정룡과의 싸움은 그리 쉽지 않았다.

문득 정신적인 피로가 밀려 왔지만, 아이러니하게도 최상급 포션에 레벨 업 효과까지 부여받은 몸 상태는 가뿐하기 그지없다.

그리고 무엇보다, 내게는 더 나아가야 할 이유가 있었다.

‘아크 리치.’

이 모든 일의 원흉. 그 죽일 놈이 거대한 도시를 게이트로 변화시키기 전, 반드시 처치해야…….

- 이, 이, 인간.

순간 들려온 스켈레톤 워로드의 떨리는 목소리.

나는 전신의 털이 곤두서는 듯한 감각과 함께 고개를 들었다.

그곳에, 놈이 있었다.
```

## Final English reading copy

```markdown
# Chapter 419

Lee Jungryong suddenly wondered.

*Where had things gone wrong? And what had gone wrong?*

Driving out his hyung’s bloodline and seizing control of Ares Guild?

Committing all manner of crimes to make the Guild grow without pause, then continuing to feed his greed without ever learning satisfaction?

Or perhaps…

*That I became enemies with him?*

Lee Jungryong’s gaze settled on one person—a young man whose body was stained with blood from the bleeding wounds covering him.

After looking up at the sky and taking a deep breath, the young man parted his lips.

“Jungryong.”

Why was it? The moment Lee Jungryong heard that quiet voice, a chill ran down his spine. Though he had not suffered a single wound, he felt as if he had been cut by a blade.

Looking at him, Jin Taekyung formed a feral smile.

“Let’s clip those claws.”

“……!”

*Fwish!*

The wind blew, and in the instant the space between them vanished, Lee Jungryong swung his sword with a sharp whistle.

*Shwick!*

A dazzling concentration of qi sliced through Jin Taekyung’s body. But instead of blood, wind scattered through the air.

An afterimage. Not the real thing.

A red alarm bell rang in Lee Jungryong’s mind.

*Behind me!*

It was too late to swing his sword. Lee Jungryong spun around like lightning and drove out his fist.

A fist wrapped in pure-white Force collided with a palm carrying blue flame.

*Kwaang!*

The world shook.

No—the thing shaking was Lee Jungryong’s vision.

Flung backward by an irresistible force, he twisted his body in midair and righted himself.

His fist throbbed, and something surged up from inside him. But he was not even given time to spit out the blood.

*Shweeeeeek!*

A spearhead had already rushed up to his face.

The spear Jin Taekyung had hurled was aimed at Lee Jungryong’s chest. Gritting his teeth, Lee Jungryong poured all his strength into knocking the spear upward with his sword.

*Kagagagagak! Kwaang!*

The spear narrowly missed and smashed through the concrete, leaving behind a massive crater.

Lee Jungryong succeeded in deflecting it, but the spear’s terrifying power and spin tore his hand open, sending blood spraying into the air.

He paid it no mind and thrust his foot through the thick cloud of dust.

*Boom!*

The dust and fog, unable to withstand his blinding speed, scattered in every direction.

At the end of Lee Jungryong’s step stood a single person.

“Reckless, aren’t you? My kind of guy.”

Jin Taekyung was already holding a new spear. He slashed the spearhead down in every direction. Space split apart, and flames surged upward.

The tip of Lee Jungryong’s sword pierced straight through the center.

*Whoom! Boom!*

Compressed air burst outward. The flames parted, opening a new path.

Lee Jungryong’s body shot forward like an arrow along it, charging toward Jin Taekyung.

*Die.*

The sword held a single thought. It shone brilliantly and moved as fast as light.

Yet Jin Taekyung’s eyes, seen within the slowed-down world, were clearly smiling.

*This is…*

Something was wrong.

Before Lee Jungryong could finish the thought, Jin Taekyung’s hand gripping the spear blurred.

At the same time, a tremendous force struck the sword blade that had seemed ready to pierce Jin Taekyung’s throat.

*Shick! Kwaang!*

A thunderous boom rang out, loud enough to leave his ears ringing.

Lee Jungryong slid more than ten meters against his will and swallowed the blood rising in his throat.

*It isn’t over yet.*

He could not fall. He could not show weakness.

He was Lee Jungryong—the one who had made his way through the vortex of the Great Cataclysm, the most violent upheaval in human history, and a ruthless hero born of his age.

Lee Jungryong gripped his sword, now webbed with fine cracks.

*I won’t die. I can’t die.*

There had been countless twists and turns on the road that had brought him here. He had endured distant despair and days of unbearable rage.

He had spent half his life in someone else’s shadow, branded as number two.

No. Perhaps even now…

But—

“Not anymore.”

*Crack. Crack-crack-crack.*

The veins across his body stood out, and his muscles swelled.

Powerful qi erupted from Lee Jungryong’s entire body, pressing down on everything around him.

He dragged up every last scrap of strength he had saved for the very end and glared at Jin Taekyung with bloodshot eyes.

“He’s practically a man who no longer exists. The greatest in the world is… me.”

*Vrrrrrrm.*

Everything surrounding Lee Jungryong trembled.

Jin Taekyung watched him with calm eyes that held not the slightest hint of wavering.

“I don’t think so.”

*Kuwaaaaaang!*

The waves of energy flowing from both men clawed at everything around them.

In a fleeting instant split into countless fragments, they charged toward each other at the same time.

* * *

*Kwaang!*

Their collision was like a flash of light, and the aftermath was enormous.

Amid thunderous booms that shook the world, they became two streams of wind twisting together.

A spearhead wrapped in blue flame and a sword enveloped in dazzling light flew toward each other.

*Shwish-shwish-shwish-shwish!*

Masses of light tore through space as they charged.

Jin Taekyung kicked off the ground and rose into the air, driving his spear down with tremendous force.

One strike. Two strikes. Three.

Every time spear and sword collided, thunderous booms erupted along with immense shock waves.

Before long, blood spilling from the corner of Lee Jungryong’s mouth scattered in droplets.

“Cough.”

His body staggered for an instant.

At the brief glimpse of weakness shown by the old lion, the young male lion bared his teeth.

The spearhead swept horizontally, slashing fiercely toward Lee Jungryong’s side.

*Kwaang!*

The ground shook as though an earthquake had struck.

The two men were so close that their breaths nearly touched. Lee Jungryong barely blocked the spear, and through the weapons pressed against each other, his eyes met Jin Taekyung’s—a pair of eyes pouring flame.

*He’s young. Just as I was in the past.*

Why?

Why had such a thought suddenly come to him at a time like this?

Was it because he was remembering his own old, pathetic self that he failed to block Jin Taekyung’s palm as it came flying through the flames?

*Boom!*

It was hot.

The qi that had been protecting his entire body without a gap shattered, and terrible heat seeped deep into his lungs.

Amid the blue flames filling his vision and the pain, old memories flashed through Lee Jungryong’s mind like arrows.

“Your name?”

“Pardon?”

“Ah, yes. I meant you.”

“What’s this sudden exchange of names?”

“Just because. You looked about my age, and it was nice to see someone my age.”

“Young fellow, suddenly dropping the honorifics, are we? You look much younger than me.”

“Then should we be friends? I don’t mind.”

“……Do you really have time to say things like that in a situation like this?”

“Maybe not.”

A man he had met during the early days of the Great Cataclysm, when they were surrounded by countless monsters in a desperate, life-or-death situation.

Lee Jungryong had thought he was half-mad with fear of death.

At least, he had thought so until that madman suddenly stepped forward and swept away more than a thousand monsters.

*Crack-crack-crack!*

“What the hell…”

“Now! Charge!”

After the battle ended, the man came back and asked him the same question as before.

“Your name?”

“Lee Jungryong… sir.”

“Cool name. How old are you? Oh, I’m five years older. That’s not much of a difference. Should we just be friends?”

“No. Hyung.”

He looked absurdly young and was unbelievably strong.

At their first meeting, A-rank Hunter Lee Jungryong discovered his hero—and, at the same time, an immense mountain range he could never cross.

“By the way, hyung.”

“Yeah?”

“What’s your name…?”

“Oh, I haven’t told you yet.”

The man had grinned and said,

“Cheon Taemin.”

Cheon Taemin. Cheon Taemin. Cheon Taemin…

No matter how many times he repeated the name, it left behind a deep resonance.

Even when he tried to forget it, the face remained etched in his mind.

A giant who cast a massive shadow over Lee Jungryong’s life.

“Get lost! I said get out of my sight right now—!”

Lee Jungryong cried out in a boiling voice.

The vision that had been bleached white with pain shattered like glass, and the wind rushing past his ears was fierce.

When he came to his senses, Lee Jungryong was crashing through a high-rise building and slamming into cold concrete with tremendous force.

*Kwa-gwa-gwang!*

“Cough.”

Dark-red blood spurted between his lips.

His vision was blurred, and pain surged through every part of his body.

Perhaps his shattered ribs had pressed against his organs, because breathing was difficult. His broken left arm and leg dangled uselessly.

*A potion. The potion…*

This was his last chance.

While the attack had stopped, even if only briefly, he needed to heal his wounds.

Lee Jungryong groped at his side with his relatively uninjured right arm, but the place where his dimensional pouch should have been was empty.

Instead, he saw someone approaching him from far away.

“Ah, are you looking for this?”

*Rrrrrroll. Clink.*

A magic-enhanced glass bottle rolled over and came to rest by Lee Jungryong’s feet.

It was a top-tier potion, a miraculous medicine said to save anyone as long as they still had breath in their body.

There was, however, a considerable difference between it and the state Lee Jungryong remembered.

“I was so thirsty that I drank it. Man, it was refreshing. Did you just come back from a mineral spring?”

As Jin Taekyung approached and spoke as casually as ever, Lee Jungryong let out a hollow laugh.

*Jin Taekyung.*

His name, face, and personality were all different.

But at that moment, Lee Jungryong finally understood.

The familiar feeling he had deliberately ignored when he first encountered Jin Taekyung, covering it with the two words *anxiety* and *interest*.

“Jungryong.”

The quiet voice pierced his ears.

Jin Taekyung’s face had drawn close, and superimposed over it was the image of another person.

Lee Jungryong muttered like a groan.

“Who are you? Who the hell are you?”

He wanted to ask. He was desperate to know.

How could Jin Taekyung resemble him so much?

Why could some F-rank Hunter like that grow stronger, rather than Lee Jungryong—the man who had followed in Cheon Taemin’s footsteps, achieved countless feats, and been hailed as a hero?

“Me?”

The next moment, Jin Taekyung smiled and continued,

“Jungryong’s personal bully.”

Then, like an echo rebounding from far away, the face and voice of someone from the depths of Lee Jungryong’s stale memories overlapped with his.

“Brothers. Sworn brothers.”

The two men, speaking different words with different meanings, were both smiling.

Lee Jungryong stared blankly at those goddamn similar smiles, then slowly—very slowly—opened his mouth.

“I…”

Decades of his life and countless emotions rose and faded.

After a wait that lasted no more than an instant yet felt like eternity, a hollow voice forced its way between his lips.

“I don’t regret it. Never.”

If someone asked whether he had not even a handful of regrets, the answer was no.

But Lee Jungryong could not regret it. He did not want to regret it.

He simply believed this was the ending most suited to him.

“Kill me.”

A cold sentence fell toward Lee Jungryong, who was smiling brightly.

“Your last words. I heard them.”

*Fwoom.*

The words were cold. The spearhead that followed them burned with blue flame.

* * *

The flames, carrying heat hot enough to melt anything, roared to life in an instant. After burning everything, they finally died away.

All that remained in the melted concrete and blackened ruins was a trace that someone had once been there.

And the sound of a bell that only one person in the world could hear.

*Ding.*

> **System**
>
> - Defeated **Lv. 153 Lee Jungryong**!
> - Gained a massive amount of **EXP**!
> - Level up!
> - Level up!

Listening to the cheerful System notification, I slowly lowered my spear.

*Damn old man.*

That final smile kept coming back to me.

What kind of life had Lee Jungryong lived? What had he been thinking at the end? And then there were the movements he had shown and his strange behavior…

*No. I’ll think about it later.*

The fight with Lee Jungryong had not been easy for me, either.

A wave of mental exhaustion suddenly washed over me, but ironically, my body felt lighter than ever after receiving the effects of a top-tier potion and leveling up.

And more than anything, I had a reason to keep moving forward.

*The Arch Lich.*

The source of all this.

Before that bastard transformed the enormous city into a Gate, I had to kill—

“H-human.”

The Skeleton Warlord’s trembling voice reached me.

I raised my head, a sensation like every hair on my body standing on end washing over me.

There he was.
```

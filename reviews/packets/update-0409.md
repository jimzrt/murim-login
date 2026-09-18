<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0409.txt",
      "sha256": "425f26dc5a437f8e6ed0dcdbd8f41910007023fbf1898cc6fffd8ec8868a0fdb",
      "bytes": 13557
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "b26c8a93834fe52fe6c3bf7bb10ceba443bbd9f293dde09019b4d5a2572a9f96",
      "bytes": 2081
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "0868a92dfcc79773646904397ba580f5aaf82689129a571f78e9663bf4aca345",
      "bytes": 137375
    },
    {
      "path": "characters/Cheon Taemin.md",
      "sha256": "c605827fb8bfce26e3ca08fe239e66260acb223fffef2ed885a1c50d248f5ec3",
      "bytes": 590
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "aad5b108ae70a7c5e0fb8879ab3073d780d96dcc4c2b1d1825507d3830c60c29",
      "bytes": 533
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "68cfb192f61fa8e34703ca24a3e7babce54dad6592275dec9d95639e2bfb53e1",
      "bytes": 1270
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "01ff096e8356985c6f4eb79f86d99dfcaa8243229179567942892c00c527d94d",
      "bytes": 622
    },
    {
      "path": "characters/Lee Jungryong.md",
      "sha256": "d781e9bc906ee56e7536fc09b5a1a233e239f3a0eed853ac7725dd8110661608",
      "bytes": 1163
    },
    {
      "path": "characters/Team Leader Choi.md",
      "sha256": "a9834eb94c061ef312b77448e7059e0ddabdd246f164c3033181a06a7310c3f7",
      "bytes": 407
    },
    {
      "path": "characters/Wu Heixing.md",
      "sha256": "9beed18699e1615df052fe8fe6b6ef52d506e45d4b949940acffd10c51ad38f1",
      "bytes": 735
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "ac99ecb2ce9be79ba6f784ef24d3d0c5331105f051838212bed5a2e3feaeee27",
      "bytes": 122639
    }
  ],
  "estimated_tokens": 10541
}
-->

# Durable State Update — Chapter 409

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 409. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 409. Profile updates may replace only one
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
  "chapter": 409,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 409,
    "continuity_sources": [409],
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
    "The five allied fronts have halted two hundred kilometers from Suining City after forcing the Arch Lich's territory back to the city.",
    "Daniel Inoue is the sole survivor of the intelligence team sent into Suining City and reports a monster army of roughly thirty thousand by direct observation, with the actual number possibly twice that or more.",
    "Most of the Arch Lich's remaining monsters are expected to be mid- or low-level, while the allied forces also have more troops than previously expected.",
    "The coalition has approved a suicide squad of S-rank Hunters, high-level A-rank Hunters, and veteran B-rank Hunters to eliminate the Arch Lich.",
    "The undead army is expected to collapse if the Arch Lich is destroyed.",
    "Jin Taekyung and Lee Jungryong have joined the suicide squad, while Wu Heixing was compelled to join; Magic Johnson, Prince Felix, and Faye Chen remain behind.",
    "The Skeleton Warlord is still Jin Taekyung's captive undead commander after unsuccessfully seeking freedom.",
    "Lee Jungryong continues to act as Jin Taekyung's adversary while coordinating with him for the final battle."
  ],
  "continuity_sources": [
    408
  ],
  "open_questions": [
    "Who is Lei Fei's unidentified lord, what is the lord's origin, and how does the lord relate to the Arch Lich's objective?",
    "What happened to the Second Fiend assigned to the Qingcheng attack?",
    "Why has the Arch Lich withheld itself from the war, and what is it preparing now?",
    "What kind of being was the Skeleton Warlord before it became an undead commander?",
    "What specific situation will allow Jin to draw out Hero's Power more strongly?"
  ],
  "safe_through": 408,
  "temporary_decisions": [
    "Render 영웅의 혼 as Hero's Soul and 영웅의 힘 as Hero's Power.",
    "Render 기동전 as mobile warfare.",
    "Render 쑤이닝시 as Suining City.",
    "Render 결사대 as suicide squad.",
    "Render 머리를 치다 as take out the head in the context of killing the Arch Lich."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 최민우    | **Choi Minwoo**   |
| 천태민    | **Cheon Taemin**  |
| 이정룡    | **Lee Jungryong** |
| 열화문    | **Fire Gate Clan**               |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 심법     | **cultivation technique**                        | Especially internal cultivation                       |
| 주화입마   | **qi deviation**                                 |                                                       |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 운기조식   | **circulate one's qi**                           | Usually better as a verb than a proper-name technique |
| 진가심법   | **Jin Family's Cultivation Technique** |
| 시스템              | **System**                     |
| 습득               | **Acquired**                   |
| 체력               | **Stamina**                    |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 길드      | **Guild**             |
| 팀장      | **Team Leader**       |
| 탱커      | **tank**              |
| 도사      | **Daoist**                                                      |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 우헤이싱 | **Wu Heixing** | Chinese S-rank Hunter who provokes Jin and nearly draws his sword. |
| 평화 | **Peace Guild** | Guild name. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 무재 | **martial talent** | Innate aptitude for learning martial arts. |
| 열화신공 | **Fire Gate Divine Technique** | Secret internal cultivation technique of the Fire Gate Clan, preserved through one-person succession without leakage. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 아이튜브 | **iTube** | Live-streaming platform hosting the Hunter Association ceremony. |
| 소원 | **Sowon** | Name called out by Im Kkeokjeong during the Wyvern attack. |
| 준이 | **Jun** | Family nickname used in the form Jun's dad. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 존슨 | **Johnson** | Co-host of the American talk show that replays Taekyung's viral interview. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 쓰촨성 | **Sichuan Province** | Source spelling variant of the established Sichuan location. |
| 성도 | **Chengdu** | Sichuan destination of Taekyung's party. |
| 듀라한 | **Dullahan** | Headless undead monster form taken by Yao Wei. |
| 쑤이닝시 | **Suining City** | City in Sichuan Province and the operation's final destination. |

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
| 진태경 | 우헤이싱 | adversarial S-rank Hunters | you idiot | insulting-casual | Mocks Wu's cowardice and orders him to stop complaining. |
| 이정룡 | 우헤이싱 | senior S-rank Hunter to younger allied S-rank Hunter | Mr. Wu | polished and formally coaxing | Lee publicly draws Wu into agreement with the suicide-squad plan. |

## Listed compact profiles

### Cheon Taemin.md

# Cheon Taemin (천태민)

- **Safe through:** Chapter 406
- **Aliases:** Slayer
- **Role:** Ares Guild Master; humanity's great hero and the world's greatest Hunter; killed the Demon King and is known as the Slayer; created the first Mana Cultivation Method during the Great Cataclysm.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** Maternal grandfather of Team Leader Choi and father of Soyeong; regarded by Lee Jungryong as an older brother despite their lack of blood relation.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 407
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who has sworn never to kill again.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 408
- **Aliases:** Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, and a Supreme Peak master who has manifested Force and crossed the wall into true mastery.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and student, his mother and sister Hayeon are among those he protects, and the Skeleton Warlord is his captive undead commander.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 408
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Lee Jungryong.md

# Lee Jungryong (이정룡)

- **Safe through:** Chapter 408
- **Aliases:** None
- **Role:** Vice Guild Master of Ares Guild, one of Korea's two S-rank Hunters, and a Supreme Peak-level martial artist who directs Ares Guild operations.
- **Personality:** Outwardly genial, calm, and humorous; calculating, manipulative, coercive, and ruthless when challenged
- **Voice:** Smooth, good-natured, and indirect, using teasing conversation and veiled threats before becoming openly furious
- **Relationships:** Master of Park Jihoon and Go Jun (Team Leader Seok), whom he personally selected and trained; longtime Great Cataclysm acquaintance of Park Tae Seop; adversary of Jin Taekyung; knew Team Leader Choi from childhood; has an antagonistic history with Kim Hwajong, who saved his life at the collapse of Mapo Bridge eighteen years earlier; was visibly shaken by learning that Choi is Cheon Taemin's maternal grandson; regards Cheon Taemin as an older brother despite no blood relation and has long held him in respect and fear; operates as Ares Guild's senior authority beneath its Guild Master

### Team Leader Choi.md

# Team Leader Choi

- **Safe through:** Chapter 403
- **Aliases:** Choi Minwoo (최민우)
- **Role:** Team Leader Choi is an allied Hunter and team leader who fought on the Western Front.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** Team Leader Choi is an ally of Jin Taekyung and Shao Shen.

### Wu Heixing.md

# Wu Heixing (우헤이싱)

- **Safe through:** Chapter 408
- **Aliases:** None
- **Role:** Wu Heixing is a Chinese S-rank Hunter known for frequent media exposure and scandal who secretly practices martial arts, including an internal-energy cultivation technique and fist-and-foot martial arts.
- **Personality:** Arrogant, status-conscious, abusive, and fiercely proud of his power, he responds to humiliation with anger, jealousy, and fear.
- **Voice:** Loud, insulting, entitled, and dependent on national and political status.
- **Relationships:** He is openly hostile toward Jin Taekyung and Faye Chen, and resents Jin receiving Chairman Shao Yang's attention.

## Korean source

```text
＃409화



선약 없는 방문자가 찾아온 것은 날이 채 밝아 오기도 전의 일이었다.

조심스럽게 텐트 안으로 들어선 그는 가부좌를 튼 채 앉아 있는 나와 눈이 마주쳤다.

“일어나 계셨군요.”

“보시다시피.”

나는 최 팀장을 향해 어깨를 으쓱해 보였다.

“요즘 들어서 통 잠이 안 와서요.”

정확히 말하자면 잠이 줄었다고 해야 맞겠다.

인간의 한계를 뛰어넘은 체력과 삼 갑자에 달하는 고강한 공력이 있다면 어지간한 피로는 운기조식으로 날려 버릴 수 있으니까.

“마나 연공법, 아니 진가심법을 수련 중이셨습니까?”

“예, 뭐. 그렇죠.”

정확히는 열화문의 비전 심법인 열화신공(烈火神功)이지만, 모든 사실을 곧이곧대로 말해 줄 수는 없는 법이다.

“나중에 올 걸 그랬군요.”

“아뇨. 괜찮아요.”

“심법 수련 도중에는 어떤 방해도 금물이라고 하시지 않았습니까? 중간에 끊었다가는 주화입마가 올지도 모른다고…….”

“아, 그건 최 팀장님이고 전 괜찮아요. 수준이 달라서.”

“…….”

당신의 팩트 폭행. 누군가에게는 상처가 될 수 있습니다.

순간 최 팀장의 얼굴 위로 그런 공익 광고 멘트가 스쳐 지나간 것 같은데.

떨떠름한 표정으로 날 바라보던 그가 고개를 절레절레 저었다.

“사실이라 할 말이 없군요.”

“그래도 최 팀장님 정도면 습득력이 엄청난 겁니다. 이건 진심이니까 좀 더 자신감을 가지세요.”

이건 진심이다. 인류 역사상 불굴의 업적을 세운 영웅, 천태민의 핏줄답게 최 팀장은 타고난 무재(武才)가 매우 뛰어났다.

게다가 어떤 이유에서인지 신체 내부에 축적되어 있던 기운도 상당해서, 무공의 진척 속도가 깜짝 놀랄 정도였다.

한 단어로 정리하자면, 준비된 인재라는 거다.

‘우헤이싱처럼 어린 시절부터 무공을 익혔다면…… 아마 지금쯤 S급 헌터의 한 자리를 차지하고 있었겠지.’

살짝 표정이 풀어진 최 팀장이 고개를 끄덕였다.

“진태경 씨에 비하면 어떻습니까?”

“지금 장난하세요? 당연히 제가 더 빨리 익혔죠.”

“…….”

어디에 비비려고.

최 팀장이 아무리 이정룡의 감시와 견제 하에 자랐다고 해도 나와 비교하면 살아온 인생의 결부터가 다르다.

시스템을 얻은 후에도 죽을 뻔한 적이 몇 번인데, 팍 씨. 아주 그냥.

“그나저나 무슨 일로 오셨어요? 그것도 이렇게 이른 시각에.”

“고민이 있어서 실례를 무릅쓰고 찾아왔습니다.”

“고민이요?”

“예.”

“왜요. 혹시 존슨이 고백했어요?”

“신경 안 씁니다. 미스터 존슨 나름대로의 친밀감 표현이라는 걸 알고 있으니까요. 그보다는 길드 업무 관련 내용입니다.”

“길드 업무라면…… 한국에서 무슨 안 좋은 소식이라도 왔어요?”

내 걱정스러운 물음에 최 팀장이 고개를 저었다.

“그건 아니고, 길드원 중 하나가 위험에 빠지는 것 같아서 걱정이 되네요.”

“아하.”

무슨 말인가 했더니. 최 팀장의 말뜻을 알아들은 나는 피식 웃었다.

“그 사람 누군지 알겠네. 키 크고 잘생긴 사람 아니에요? 성격도 끝장나게 좋고.”

“다른 건 모르겠는데, 성격이 끝장나는 것 같긴 합니다. 여러 의미로요.”

“흠, 그럼 내가 아는 사람이 아닌 것 같은데.”

“진태경 씨.”

지금까지 농담처럼 대화를 주고받던 최 팀장이 낮아진 목소리로 말했다.

“무슨 말인지 아시잖습니까.”

“글쎄요.”

“이 작전은 위험합니다.”

“최 팀장님. 저 못 믿으세요?”

“그럴 리 있겠습니까. 진태경 씨는 제가 세상 누구보다 믿는 사람 중 한 명입니다.”

최 팀장이 깊게 가라앉은 눈빛으로 나를 응시했다.

“그리고 세상 누구보다 믿을 수 없는 사람들과 위험한 작전을 수행하려 하고 있고요.”

생각할 것도 없이 두 사람의 이름이 떠오른다.

이정룡과 우헤이싱. 나와는 악연으로 연결된 이들이자, 곧 서로에게 등을 맡겨야 할 전우가 되겠지.

나는 턱을 긁적이며 대답했다.

“믿을 수 없는 사람들이라. 그것만큼 잘 어울리는 표현도 없겠네요.”

“진태경 씨…….”

“저기, 최 팀장님?”

뭔가 말하려던 최 팀장이 입을 다문다. 나는 조용히 손을 들어 문밖을 가리켰다.

“아시다시피 아직 수련이 덜 끝나서요.”

“……!”

“오늘이 지나기 전에 전투가 시작될 겁니다. 머리를 비우고 곧 다가올 전투에 대비하세요.”

말을 잇지 못하던 최 팀장은 복잡한 눈빛으로 나를 바라보았다. 그리고 이내 한숨을 푹 내쉬더니 자리에서 일어났다.

“잠시 후에 뵙죠.”

“그래요. 멀리 안 나갑니다.”

텐트를 빠져나간 최 팀장의 인기척이 서서히 멀어지는 것이 느껴졌다.

그러자 소원권을 환불당한 뒤부터 침울해져 있던 스켈레톤 워로드가 희망에 찬 어조로 입을 열었다.

- 매우 똑똑한 인간이로군. 아직 늦지 않았으니 저 인간의 조언을 받아들이는 게 어떤가?

“애쓴다.”

- 아니, 갈 거면 네놈 혼자 가지. 왜 본 사령관을 데려가느냐는 말이다!

“혼자 죽으면 외롭잖아.”

- 뭣이이이-!

“농담이야. 다만 이게 최선이라 그런 거지.”

- 엄청난 숫자의 몬스터 군단을 뚫고, 아크 리치와 대적하는 게 최선이라고? 혹시 간악한 인간이 아니라 미친 인간인가?

이 언데드 새끼 말하는 본새 보게.

벌을 내려 줄까 고민하던 나는 가부좌를 풀고 침상에 비스듬히 몸을 눕혔다.

“위험한 작전인 건 맞지만, 가능성도 충분하니까 너무 그러지 마라.”

- 막상 가 봤는데 안 되면?

“죽을힘을 다해서 싸워야지. 그럼 가능성이 생겨.”

스켈레톤 워로드가 해탈한 목소리로 중얼거렸다.

- 기적의 논리로군. 본 사령관이 이런 미친 인간과 함께하고 있다니.

“그러면서도 안 떠나잖아.”

- 안 떠나? 못 떠나는 거겠지!

“웃기는 놈일세. 제 발로 돌아올 때는 언제고. 아, 취소. 발이 아니라 두개골이었지.”

- 주위에 본 사령관을 노리는 흉악한 인간들이 득실거리는데 도대체 어쩌란 말이냐?

억울함이 느껴지는 스켈레톤 워로드의 항변에, 나는 작게 실소를 흘렸다.

‘약한 소리 하기는.’

하고 싶은 말은 많지만, 아껴 두기로 했다. 그건 스스로가 깨달아야 하는 부분이니까.

- 웃어? 방금 웃었지!

“내가 언제?”

시치미를 뚝 떼고 화제를 돌렸다.

“어쨌건 간에 아크 리치를 쓰러트리는 게 관건이야. 머리를 잃으면 몸뚱어리는 움직이지 못하니까.”

- 듀라한은 안 그러던데.

“…….”

그건 그러네.

순간 납득하고도 어이가 없어진 나는 인벤토리에서 스켈레톤 워로드를 꺼내 들었다.

“아니, 근데 이 새끼가 아까부터 진짜.”

- 지, 진정해라 인간. 난 틀린 말은 하지 않았다.

“그래, 듀라한은 머리가 없어도 움직이지. 스켈레톤 워로드는 어떻게 되나 보자.”

빡!

번개처럼 후려친 딱밤에 스켈레톤 워로드가 비명을 내질렀다.

- 악, 금! 미간에 금 갔다! 진짜 금 갔다고!

“힘 조절해서 쳤는데 무슨 개소리…… 어, 진짜네.”

좀 더 살살 칠 걸 그랬나. 반지르르한 검은 광택이 흐르는 두개골에 미세한 금이 가 있다.

충격으로 인해 들어 올려진 뼛조각을 슬쩍 만지자 스켈레톤 워로드가 비명을 질렀다.

- 내 뼈! 뼈!

“알았겠으니까 소리 그만 질러, 인마.”

- 안 그래도 요즘 들어 부쩍 뼈가 간질거리고 예민해서 걱정인데, 이 미친 인간이 기어코…… 흐흑.

“…….”

건성 피부야, 뭐야.

이 정도면 조만간 아이튜브에 채널 하나 파서 언데드 뷰티 전문 스트리머로 구독자 100만 끌어모을 기세다.

‘이 새끼 몬스터 아닐지도 몰라…….’

하여간 보면 볼수록 별종이 따로 없다.

황당한 눈빛으로 스켈레톤 워로드를 바라보던 나는 문득 텐트의 한쪽 면을 열어젖혔다. 동쪽으로부터 서서히 고개를 내미는 태양이 보인다.

그것은 오늘 하루, 그리고 곧 다가올 전투를 알리는 신호였다.



* * *



쓰촨 분지의 중부에 위치한 쑤이닝시는 두 개의 시할구와 세 개의 현, 그리고 5000km가 넘는 광활한 면적을 자랑한다.

예로부터 고고한 문화와 그윽한 산수, 농공상업의 발달로 쓰촨성 중부지구의 중심지라 불렸지만 이제는 그 또한 과거의 일이 되어 버리고 말았다.

까악, 까아아악!

흐린 하늘 위, 무리 지어 날아다니던 수많은 까마귀 떼가 대지 위에 널브러진 시신 위로 내려앉았다. 먹잇감을 둔 무리 간의 신경전은 벌어지지 않았다.

어림잡아도 수백 구에 달하는 시신이 곳곳에 널려 있었고, 까마귀들은 한때 인간이었을 부패한 살점을 쪼아 먹으며 배를 불렸다.

인간에게는 더 없을 재앙이, 그들에게는 배부른 태평성대였다.

그러나 까마귀들의 평화로운 식사는 그리 오래 이어지지 못했다.

드득, 드드득.

굉음과 함께 지면으로부터 전해지는 진동에, 까마귀들은 신경질적인 울음을 내뱉으며 일제히 날아올랐다.

허공에서 내뿜어진 검은 깃털 중 몇 개가 바람을 타고 드넓은 분지를 가로질렀다.

흐느적거리며 추락한 깃털을 짓밟은 것은 수많은 걸음과 금속으로 이루어진 전차의 바퀴였다.

쿵, 쿵, 쿵.

지평선을 메운 인간의 군세.

최전방에 선 탱커들이 든 타워 실드가 지면을 스치고, 그 뒤로 수천에 달하는 헌터들이 오와 열을 맞춰 걸음을 옮겼다.

깊게 눌러쓴 투구 밑으로 누군가의 앙다문 입술이 드러났다.

보이지 않는 전운(戰運)에 휩싸인 수천의 인간은 그저 묵묵히 나아갈 뿐이었다.

저 멀리, 희끄무레한 안개에 휩싸인 도시를 향해. 그리고 곧 이어질 전투와 영광스러운 승리를 향해.

그리고 그들의 중심에서, 한 사람이 문득 입을 열었다.

“씨벌, 안개 꼬라지 봐라. 저거 괴물 나오는 재난 영화에서 나왔던 것 같은데. 혹시 그 영화 본 사람?”

심각한 분위기 속 뜬금없이 흘러나온 진태경의 찰진 욕설에, 곳곳에서 피식거리는 실소가 터져 나왔다.

「큽.」

「크흡.」

“뭐야, 나만 봤어? 그 명작을?”

진태경이 어깨를 으쓱하던 그때, 그의 오른편에서 대답이 들려왔다.

“저도 봤습니다.”

“그래요? 최 팀장님은 좀 의왼데.”

“뭐가 말입니까?”

“왠지 영화보다는 뮤지컬이나, 오케스트라 연주. 뭐 그런 것만 볼 것 같은 이미지라서요.”

최민우를 힐끗 바라본 헌터들이 웃음을 참기 위해 입술을 깨물었다.

어느새 딱딱하게 굳어 있던 몸이 풀리고 호흡이 안정된다. 그들은 긴장이 한결 완화되는 것을 느꼈다.

그러는 사이에도 두 사람의 대화는 이어졌다.

“저도 가끔은 기분 전환 삼아 영화를 봅니다. 진태경 씨께서 말씀하신 영화도 재밌게 봤고요.”

“오, 그럼 마지막 반전도 아시겠네.”

“물론이죠. 개인적으로는 참 안타까웠습니다.”

“그러게요. 난 그거 보면서 딱 그 생각이 들더라고.”

진태경은 천천히 말을 이었다.

“마지막까지 포기하지 않았으면 살 수 있었을 텐데. 어떻게든 죽을힘을 다해 싸웠어야지. 뭐 그런 생각.”

목소리는 나직했지만, 힘이 있었다.

웅혼한 공력이 실린 음성은 공기를 울리며 퍼져 나가, 이내 모두의 귓가에 닿았다.

그리고 서부 전선에 속한 수천 명의 헌터와 군인들은 깨달았다.

진태경의 한마디는, 어쩌면 바로 자신들에게 던지는 조언이라는 사실을.

“지금쯤이면, 다른 전선도 우리처럼 쑤이닝시를 포위하고 있겠죠?”

“빈틈없이 에워싸고 있을 겁니다.”

“그리고 곧 전투가 벌어질 테고.”

「우리는 승리할 겁니다.」

단호한 어조로 대답하는 샤오 쉔의 모습에 진태경이 소리 내어 웃었다.

“그래. 그래야지. 그런데…….”

진태경의 웃음소리가 뚝 그쳤다. 그리고 다음 순간, 장난기 어린 눈동자 대신, 깊게 가라앉은 안광이 빈자리를 채웠다.

서늘한 그의 동공에 드넓은 분지가 비쳤다.

“저놈들 생각은 다른 모양이다.”

투둑, 투두두둑.

크르륵……

서서히 몸을 일으키는 시체. 스켈레톤들. 그리고 미끄러지듯이 분지를 덮어 오는 안개와 그 안에 도사린 몬스터의 울음소리.

“지금부터…….”

진태경은 깊이 심호흡했다.

“시작이다.”
```

## Final English reading copy

```markdown
# Chapter 409

The visitor who had not made an appointment arrived before dawn had fully broken.

He carefully entered the tent and met my eyes as I sat cross-legged.

“You were already awake.”

“As you can see.”

I shrugged at Team Leader Choi.

“I haven’t been able to sleep much lately.”

To be precise, I should say I needed less sleep.

With stamina that had surpassed human limits and formidable internal energy amounting to three jiazi,[^1] I could blow away most fatigue by circulating my qi.

“Were you cultivating the Mana Cultivation Method—or rather, the Jin Family’s Cultivation Technique?”

“Yeah, something like that.”

To be exact, it was the Fire Gate Divine Technique, the secret cultivation technique of the Fire Gate Clan. But I couldn’t exactly tell him every last detail.

“I should have come later.”

“No, it’s fine.”

“Didn’t you say that any interruption during cultivation was forbidden? That stopping halfway through could cause qi deviation…”

“Oh, that’s true for you, Team Leader Choi. I’m fine. We’re on different levels.”

“…”

*Warning: your fact attack may hurt someone.*

For a moment, I thought I saw a public-service announcement like that flash across Team Leader Choi’s face.

He looked at me with an uncomfortable expression, then slowly shook his head.

“It is a fact, so I have nothing to say.”

“Even so, your rate of learning is incredible by any standard. I mean that sincerely, so have a little more confidence.”

I meant it. True to his bloodline as the descendant of Cheon Taemin, the hero who had accomplished an indomitable feat in human history, Team Leader Choi possessed extraordinary natural martial talent.

And for some reason, he also had a considerable amount of energy accumulated inside his body, so his progress in martial arts was astonishingly fast.

In short, he was a talent with all the groundwork already laid.

*If he’d learned martial arts from a young age like Wu Heixing… he’d probably hold an S-rank Hunter position by now.*

Team Leader Choi’s expression softened slightly, and he nodded.

“How do I compare to Jin Taekyung?”

“Are you joking? Of course I learned faster.”

“…”

*As if you could compare yourself to me.*

No matter how Team Leader Choi had grown up under Lee Jungryong’s supervision and restraint, the very texture of the lives we had lived was different.

Even after obtaining the System, I’d nearly died several times. Damn it, I’d been through hell.

“Anyway, why did you come? Especially this early.”

“I had something troubling me, so I came despite the imposition.”

“Something troubling you?”

“Yes.”

“Why? Did Johnson confess his love to you?”

“I’m not concerned about that. I know that’s simply Mr. Johnson’s way of showing affection. More importantly, this concerns Guild business.”

“Guild business… Did some bad news come from Korea?”

At my worried question, Team Leader Choi shook his head.

“No. I’m worried because it looks like one of our Guild members is heading into danger.”

“Oh.”

So that was what he meant. Once I understood, I snorted quietly.

“I know who you mean. Tall and handsome, right? With an absolutely wonderful personality.”

“I don’t know about the other qualities, but his personality certainly seems to be something else. In several ways.”

“Hmm. Then I don’t think we’re talking about the same person.”

“Mr. Jin Taekyung.”

Team Leader Choi, who had been trading jokes with me until then, spoke in a lowered voice.

“You know what I mean.”

“Do I?”

“This operation is dangerous.”

“Team Leader Choi. Don’t you trust me?”

“How could I not? You are one of the people in the world I trust more than anyone.”

Team Leader Choi stared at me with deeply serious eyes.

“And you are about to carry out a dangerous operation with people I trust less than anyone in the world.”

Two names came to mind without hesitation.

Lee Jungryong and Wu Heixing. People connected to me by bitter relationships—and comrades who would soon have to entrust their backs to one another.

I scratched my chin and answered.

“‘People I can’t trust.’ I can’t think of a more fitting description.”

“Mr. Jin Taekyung…”

“Team Leader Choi?”

Team Leader Choi closed his mouth as he prepared to say something. I quietly raised a hand and pointed toward the tent flap.

“As you know, I haven’t finished cultivating yet.”

“……!”

“The battle will begin before the day is over. Clear your mind and prepare for the fight ahead.”

Team Leader Choi could not continue. He looked at me with complicated emotions, then let out a deep sigh and rose from his seat.

“I’ll see you shortly.”

“All right. I won’t see you out.”

I felt Team Leader Choi’s presence gradually fade as he left the tent.

Then the Skeleton Warlord, which had been depressed ever since its wish coupon was refunded, spoke in a hopeful tone.

—A very intelligent human. It is not too late. Why not heed that human’s advice?

“You’re really trying.”

—No, if you are going to go, go alone. Why are you taking this commander with you?

“Dying alone would be lonely.”

—Whaaaaaat?!

“I’m joking. It’s just that this is the best option.”

—You call fighting through a gigantic monster army to face the Arch Lich the best option? Are you an evil human—or a lunatic?

Listen to the way this undead bastard talks.

I considered punishing it, then unfolded my legs and reclined diagonally across the bed.

“It is a dangerous operation, but we have a good chance too, so don’t be like that.”

—What if we get there and it doesn’t work?

“Then we fight with everything we’ve got. That’s how we create a chance.”

The Skeleton Warlord muttered in a voice filled with resignation.

—What miraculous logic. This commander is stuck with a madman like you.

“And yet you’re not leaving.”

—Not leaving? You mean I can’t leave!

“What a funny guy. When was it that you came back of your own accord? Ah, never mind. Not feet—your skull.”

—There are vicious humans everywhere around me, all trying to get this commander. What exactly do you expect me to do?

At the Skeleton Warlord’s aggrieved protest, I let out a small laugh.

*Don’t be such a coward.*

I had plenty to say, but decided to save it for later. That was something it needed to realize on its own.

—You laughed. You just laughed!

“When did I?”

I shamelessly pretended nothing had happened and changed the subject.

“Anyway, the key is taking out the Arch Lich. Once it loses its head, its body won’t be able to move.”

—Dullahans can still move without their heads.

“…”

That was true.

I was momentarily convinced, then immediately became dumbfounded. I pulled the Skeleton Warlord out of my Inventory.

“No, but seriously, this bastard has been asking for it.”

—H-Hold on, human. I did not say anything incorrect.

“Right. Dullahans can move without their heads. Let’s see what happens to the Skeleton Warlord.”

*Bash!*

The Skeleton Warlord shrieked when I flicked its skull with lightning speed.

—Agh! A crack! There’s a crack between my brows! I’m telling you, there’s really a crack!

“I hit you while controlling my strength, so what the hell are you talking about… Oh, there really is one.”

Maybe I should have hit it more gently. A tiny crack had appeared in the glossy black skull, its surface gleaming smoothly.

When I lightly touched the bone fragment raised by the impact, the Skeleton Warlord screamed.

—My bone! My bone!

“Fine, I get it, so stop screaming.”

—My bones have been getting increasingly itchy and sensitive lately, and I was already worried, but this madman went and… Sob.

“…”

*Is it suffering from dry skin or something?*

At this rate, it would soon start a channel on iTube and gather a million subscribers as an undead beauty streamer.

*This bastard might not even be a monster…*

The more I saw of it, the more unusual it seemed.

I stared at the Skeleton Warlord in disbelief, then suddenly threw open one side of the tent. The sun was slowly lifting its head in the east.

It was a signal announcing the day ahead—and the battle that would soon begin.

* * *

Suining City lies in the center of the Sichuan Basin and boasts two urban districts, three counties, and a vast area of more than 5,000 square kilometers.

Since ancient times, it had been called the center of central Sichuan Province because of its lofty culture, graceful scenery, and flourishing agriculture, industry, and commerce. But that, too, had now become a thing of the past.

Caw, cawww!

Countless crows flying in flocks across the cloudy sky descended upon corpses sprawled across the ground. No squabbles broke out between the flocks over their prey.

Hundreds of corpses lay scattered everywhere, at the very least, and the crows filled their bellies by pecking at the rotting flesh that had once belonged to humans.

What was the greatest calamity imaginable to humans was an age of plenty for them.

But the crows’ peaceful feast did not last long.

Grk. Grrrk.

At the deep rumble and vibrations rising from the ground, the crows let out nervous cries and took flight all at once.

A few black feathers flung into the air rode the wind across the vast basin.

Countless marching feet and the metal wheels of tanks crushed the feathers as they fluttered down.

Boom. Boom. Boom.

A human army filled the horizon.

The tower shields held by the tanks at the very front scraped against the ground, while thousands of Hunters behind them marched in orderly ranks.

Someone’s tightly pressed lips showed beneath a helmet pulled low.

Thousands of humans swept up in the invisible tide of war simply continued forward in silence.

Toward the city wrapped in pale fog in the distance. Toward the battle that would soon follow—and a glorious victory.

And then, from the center of them all, someone suddenly spoke.

“Fuck, look at that fog. Doesn’t it look like something from one of those disaster movies where monsters come out? Anyone seen that movie?”

Jin Taekyung’s vivid profanity came out of nowhere in the serious atmosphere, and quiet snorts of laughter erupted from various places.

“Heh.”

“Kh.”

“What? I’m the only one who saw it? That masterpiece?”

Just as Jin Taekyung shrugged, an answer came from his right.

“I saw it too.”

“Really? That’s unexpected, Team Leader Choi.”

“What is?”

“You look like the kind of person who’d only watch musicals or orchestral performances, not movies.”

The Hunters who glanced at Choi Minwoo bit their lips to keep from laughing.

Before they knew it, their stiff bodies had relaxed and their breathing had steadied. They felt the tension ease considerably.

Meanwhile, the conversation between the two continued.

“I watch movies occasionally to unwind. I enjoyed the one you mentioned, Mr. Jin.”

“Oh, then you know the final twist too.”

“Of course. Personally, I found it quite unfortunate.”

“Exactly. That’s what I thought while watching it.”

Jin Taekyung continued slowly.

“They could have lived if they hadn’t given up until the very end. They should have fought with everything they had, no matter what. That sort of thing.”

His voice was quiet, but it carried strength.

The voice infused with tremendous internal energy reverberated through the air and spread outward, soon reaching everyone’s ears.

And the thousands of Hunters and soldiers belonging to the Western Front realized something.

That Jin Taekyung’s words might be advice directed straight at them.

“By now, the other fronts are probably surrounding Suining City just like we are, right?”

“They should have it completely surrounded.”

“And the battle will begin soon.”

“We will win.”

At Shao Shen’s firm answer, Jin Taekyung laughed aloud.

“Yeah. We have to. But…”

Jin Taekyung’s laughter abruptly stopped. The next moment, the playful light in his eyes vanished, replaced by a deeply sunken gaze.

The vast basin was reflected in his cold pupils.

“It looks like those guys have a different opinion.”

Tap. Tap-tap-tap.

Grrrk…

Bodies slowly rose to their feet. Skeletons. And fog that slid over the basin, along with the cries of monsters lurking within it.

“From now on…”

Jin Taekyung took a deep breath.

“It begins.”

[^1]: A *jiazi* is a traditional sixty-year cycle.
```

<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0570.txt",
      "sha256": "72838c226d4e5d85a5130428b328580998aa06d3ffc84e48cab12125c1a46d3d",
      "bytes": 13312
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "8bb5d2df624e3fc0ede1c7599882c0eaacf47fe9eec77c5c276a9cf121f0116c",
      "bytes": 4357
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "250fc02867ee15228aeeab8789f3c2b5d972e58743da5dc985cd1398c80d078b",
      "bytes": 179902
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "5b22e66230e1d4adb33196efb9f9cea270c6c13f2269a7696fd1adea1d2e6957",
      "bytes": 553
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "1fc95d34252cc030e7da92ee4ef7de34fd4b843870f9790c5b004009fdca2e71",
      "bytes": 2280
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "8992989343ba6f4394e06313c4b644aa8a7e22a9592949adb4b42a463419b25f",
      "bytes": 622
    },
    {
      "path": "characters/Lee Jungryong.md",
      "sha256": "d6e2d6d21583832ef95b53039228e2d6c1f8c1e91c4544908561bdead194c42f",
      "bytes": 1182
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "b32ea74711b769aa9a49032240d22e035a0df17150b6b3c5ee95c1a23433e412",
      "bytes": 175453
    }
  ],
  "estimated_tokens": 10438
}
-->

# Durable State Update — Chapter 570

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 570. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 570. Profile updates may replace only one
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
  "chapter": 570,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 570,
    "continuity_sources": [570],
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
    "The worldwide Gate and monster crisis may mark the beginning of a second Great Cataclysm, and Taekyung intends to accelerate his project to protect Korea.",
    "Team Leader Choi says the crisis has exceeded the limit of national concealment and is prioritizing Gate defenses despite reducing Peace Guild's raid capacity.",
    "Choi is working with Song Cheonwoo against Go Jun's control of Ares Guild, while Song knows where Choi's maternal grandfather Cheon Taemin is located and Cheon Taemin remains hidden.",
    "Taekyung is a Supreme Peak master publicly recognized as S-rank-level while retaining an A-rank license, leads the Fire Dragon Pavilion's first Nanman mission, and is Peace Guild's wealthy modern-world patron.",
    "The six-member Fire Dragon Pavilion mission is entering Nanman through the Journey to Nanman Quest, whose reward is a linked quest and whose failure penalty is Can't Go to Nanman.",
    "Mungyeong ended Taekyung's direct training and assigned him the final task of incorporating martial principles into his learned martial arts; Cheongpung accompanies Mungyeong.",
    "Dark Heaven remains a monster-like threat capable of causing rifts and creating mutants, while the mechanism behind Jang Sam's transformation remains unresolved.",
    "The Mount Song Resolution restored the Murim Alliance with Mae Jonghak as Alliance Leader and Jeok Cheongang heading the Five Kings Hall; Zhuge Feng's Demon-Sealing Formation still blocks mana from the exposed Gate while Jang Taebo processes the Water God Dragon's remains.",
    "Go Jun has become increasingly ruthless, controls Ares Guild's legacy, has seized Song Cheonwoo's children as leverage, and appears to be arranging Song's quiet elimination.",
    "Go Se-won commands Ares Guild's thirty-member A-rank security team and remains obedient to Go Jun despite growing moral conflict; he personally ordered and cleaned up the abduction of Song's family.",
    "The Skeleton King was the person who applauded Taekyung and appeared as King Fury; Taekyung now trusts him enough to handle suitable emergencies alone and has granted him greater freedom.",
    "Taekyung has spent up to three days isolated in training, nearly completing an as-yet-unidentified new martial endeavor, while abnormal Gates and emergency rescue demands increase."
  ],
  "continuity_sources": [
    569,
    568
  ],
  "open_questions": [
    "What is the Lord of Heaven's identity, how is he connected to the dangerous force Taekyung associates with his original world, and how can Dark Heaven open Gates?",
    "What will Taekyung's party find in Nanman, and what does the Southern Heaven Demon Empress intend there?",
    "What process created Jang Sam's mutant form, whether Dark Heaven's mutants can absorb human energy, and whether it relates to the Mutated Gate?",
    "What will result from the duel between Jeok Cheongang and Nangong Cheon, and why did Ju Hwaran and Sama Pyo's political engagement end?",
    "Will Song Cheonwoo's children survive Go Jun's plan, and what will Taekyung's unfinished training project become?"
  ],
  "safe_through": 569,
  "temporary_decisions": [
    "Render 건량 as dry rations, 광서 as Guangxi, 대별산 as Mount Daebyeol, 만리행 as Ten-Thousand-Li Journey, and 고잉메리호 as Going Merry.",
    "Render 반 시진 as half a shichen and retain Nanman, Nanman Beast Palace, Fire Dragon Pavilion, Great Hero, and Young Lady Ju.",
    "Render 남만행 as Journey to Nanman, 남만을 못 가 as Can't Go to Nanman, 면구 as disguise mask, 역용술 as disguise technique, 각주님 as Pavilion Master, 로그아웃 as Logout, and 동기화 as Synchronization.",
    "Render 일기당천 as One Against a Thousand, 거인의 포효 as Giant's Roar, 투로 as combat sequence, 타락한 엔트 as Corrupted Ent, 붉은 눈 as Red Eye, 치코리타 as Chikorita, 대마도사 as Grand Mage, 순간이동 as Teleportation, 텔레포트 as Teleport, 변이 게이트 as Mutated Gate, and 몬스터 웨이브 as Monster Wave.",
    "Render 현혹 마법 as enchantment magic, 장거리 텔레포트 마법진 as long-distance Teleportation magic, 킹 퓨리 as King Fury, 배리어의 국장 as Director of Barrier, 세종 기지 as King Sejong Station, and 마력 수치 as magic power reading."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 이정룡    | **Lee Jungryong** |
| 상태               | **Status**                     |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 몬스터     | **monster**           |
| 레이드     | **raid**              |
| 길드      | **Guild**             |
| 길드장     | **Guild Master**      |
| 부길드장    | **Vice Guild Master** |
| 팀장      | **Team Leader**       |
| 대격변     | **Great Cataclysm**   |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 평화 | **Peace Guild** | Guild name. |
| 아레스 | **Ares Guild** | The leading Guild in Korea; formerly employed Team Leader Choi and Song Song. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 주신 | **God of Drinking** | Wipeng's drinking epithet. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 텔레포트 | **Teleport** | Taekyung's label for the Blood Lord's unexplained disappearance. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 관리 | 진태경 | official_to_young_martial_artist | Young Master | formal-polite | The official addresses Taekyung as 공자 while explaining the consequences of Prince Shangshan's displeasure. |
| 이정룡 | 진태경 | senior S-rank Hunter to younger Hunter and adversary | Young man | polished, teasing, and veiled-threatening | Uses a genial tone and indirect threats while trying to make Taekyung release the captives. |
| 진태경 | 이정룡 | younger Hunter to senior S-rank Hunter and adversary | you | polite but mocking and defiant | Taekyung answers Lee's soft threats with the wolf-and-tiger metaphor and refuses to yield. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 중년인 | 진태경 | veteran civilian Hunter to celebrated allied Hunter | Mr. Jin | formal-polite and awed | The casualty clerk addresses Jin as 진 선생님 after Jin asks him to list Lei Fei among the dead. |
| 진태경 | 중년인 | celebrated Hunter to older fellow Hunter | sir | casual and teasing | Jin addresses the older Hunter as 아저씨 while joking with him and giving him instructions. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 569
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 566
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, a Supreme Peak master who possesses the Heavenly Martial Physique and superhuman physical strength, has manifested Force, opened his Middle Dantian, crossed the wall into true mastery, has achieved Three Flowers Gather at the Crown but not Five Qi Returning to Origin, can perceive the texture of qi well enough to sever layered magic, can resist high-level monster Fear through exceptional mental strength, is publicly recognized as an S-rank-level Hunter while formally retaining an A-rank license pending testing, can command coordinated raids against powerful monsters, serves as one of the two pavilion masters of the Alliance Leader's direct Fire Dragon Pavilion, leads its first mission to Nanman, and is the Peace Guild's wealthy patron in the modern world.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor and assigned him a final task to incorporate martial principles into his learned martial arts but declined Taekyung's recruitment after Cheongpung reached him first, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate, student, and trusted manager of media and official arrangements, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, and Xiao Shen regards him as an older brother after Jin saved him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 566
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Lee Jungryong.md

# Lee Jungryong (이정룡)

- **Safe through:** Chapter 569
- **Aliases:** None
- **Role:** Former Vice Guild Master of Ares Guild, one of Korea's two S-rank Hunters, and a Supreme Peak-level martial artist who was killed by Jin Taekyung.
- **Personality:** Outwardly genial, calm, and humorous; calculating, opportunistic, manipulative, coercive, and ruthless when challenged
- **Voice:** Smooth, good-natured, and indirect, using teasing conversation and veiled threats before becoming openly furious
- **Relationships:** Master of Park Jihoon and Go Jun (Team Leader Seok), whom he personally selected and trained; longtime Great Cataclysm acquaintance of Park Tae Seop; adversary of Jin Taekyung; knew Team Leader Choi from childhood; has an antagonistic history with Kim Hwajong, who saved his life at the collapse of Mapo Bridge eighteen years earlier; was visibly shaken by learning that Choi is Cheon Taemin's maternal grandson; regards Cheon Taemin as an older brother despite no blood relation and has long held him in respect and fear; operates as Ares Guild's senior authority beneath its Guild Master

## Korean source

```text
＃570화



오전 여덟 시.

새해가 밝았어도 사람들의 일상은 여전했다.

말쑥한 정장을 걸친 직장인들은 피곤한 얼굴로 출근길 발걸음을 재촉했고, 도로는 빽빽하게 들어선 자동차들로 혼잡했다.

빵, 빠앙-!

쉴 새 없이 울리는 클락션 소리에, 중형 밴의 운전석에 앉아 있던 중년인은 반쯤 열어 놨던 창문을 올리며 투덜거렸다.

“씨부랄. 이 개 같은 도로는 대격변을 겪었어도 고쳐지질 않아요. 도대체가 차를 끌고 다니라는 거야, 말라는 거야.”

운전 시 쌍욕은 불가항력과 같다. 특히 부산에서 운전할 때는 더더욱.

중년인은 깜빡이도 없이 끼어들기를 시도하는 소형차를 보며 클락션을 내리쳤다.

빠앙!

하지만 개념이 제대로 박힌 운전자였다면 클락션을 누를 일도 벌어지지 않았을 것이다.

대낮의 하이빔으로 끼어들기를 자축한 소형차가 유유히 멀어졌다. 뒷 유리창에 떡 하니 박아 놓은 문구를 본 중년인이 쌍욕을 내뱉었다.



[아이가 타고 있어요.]



“……옘병, 씨발, 애가 활활 타고 있어서 운전을 저따위로 하나.”

그리고 뒤늦게 자신이 욕을 내뱉었음을 깨달은 중년인은, 옆자리를 바라보며 헛기침을 내뱉었다.

“큼. 이거 나도 모르게 그만.”

조수석에 앉아 있던 젊은 남자가 담담하게 대꾸했다.

“괜찮습니다. 그럴 수도 있죠.”

목소리는 중년인을 향하지만, 시선은 비스듬히 창밖을 향해 기울어져 있다. 그 모습을 힐끗 바라본 중년인이 재차 입을 열었다.

“이름이…… 동석 씨라고 했었나? 맞죠?”

“예.”

“다행이네. 요새 하도 온 사방에서 일이 터지다 보니까 이름 석 자 기억하기도 쉽지 않더라고.”

“그럴 수 있죠. 신경 쓰지 마십시오.”

“아, 지난번에 알려 줬는지는 모르겠는데 내 이름은…….”

“팀장님이라고 부르겠습니다. 그게 편해서요.”

팀장이 얼떨떨하게 눈을 깜빡이던 그때. 칼같이 대답한 남자, 이동석이 한 마디를 툭 던졌다.

“그리고 팀장님.”

“어, 응?”

“신호 바뀌었습니다.”

빠아아앙!

뒤에서 울리는 클락션 소리에 정신을 차린 팀장이 악셀을 밟았다. 거칠게 나아가는 차와 함께 그의 눈살이 찌푸려졌다.

‘거, 어지간히 싸가지 없는 놈일세. 어린노무 쉐끼가.’

내심 중얼거린 팀장은 얼마 지나지 않아 생각을 고쳐먹었다.

그래, 싸가지 좀 없으면 뭐 어떤가. 어차피 하루 얼굴 보고 말 사이. 맡은 바 임무만 제대로 수행해 주면 그것으로 족하다.

‘하긴, 벌벌 떠는 초짜나 주둥이만 나불거리는 놈보다야 백배 낫지.’

팀장은 수년째 프리랜서로 활동 중인 C급 헌터다.

그렇기에 당연히 정감 가고, 예의 바른 놈보다는 차라리 잘 싸우고 싸가지 없는 놈이 낫다는 사실을 잘 알고 있었다.

‘최소한 얼마 전 그 새끼처럼 똥 싸지르고 튀지는 않겠지.’

게이트에서 큰 실수를 저지르고 잠수를 탄 그놈을 대신해서 임시 팀원을 구해야 했는데, 그 결과물이 바로 이동석이었다.

이력서도 흠잡을 곳 없이 괜찮았고, 직접 가늠해 본 바에 의하면 헌터로서의 실력도 상당한 것 같았다. 이런 사람이 프리랜서로 활동하는 것이 의아할 만큼.

‘뭐, 좋은 게 좋은 거니까.’

요즘 같은 시기에는 사람 구하는 것도 일이다.

지금 이 순간에도 라디오에서 작게 흘러나오는 DJ들의 대화는, 최근 벌어지는 헌터 인력 부족의 가장 큰 이유를 이야기하고 있었다.

- 경기도 포천에 거주하시는 20대 신아영 님께서 댓글 달아 주셨네요. 3일 전 집 근처에서 변이 게이트가 터졌어요. 10분 거리에서 이런 일이 벌어지는 바람에 너무 불안해서 불면증에 시달리고 있어요.

- 아이고…… 하필이면 그 동네 사시는 분이었구나. 어떡해.

- 이건 저도 뉴스로 본 기억이 있네요. 자칫하면 큰 피해가 일어날 수도 있는, 굉장히 위험한 상황이었다고 하더라고요.

- 몬스터 웨이브 직전에서 멈춘 게 천만다행이죠. 정말.

팀장은 라디오 볼륨을 키웠다.

겨우 사흘 전 일어난 포천 변이 게이트는 헌터인 그로서는 모를 수 없는 사건이다.

창밖만 바라보던 이동석도 은근히 귀를 기울이는 것이 느껴졌다.

- 그런데 천만다행으로 이번 일 역시 사망자가 나오지 않았다고 하더라고요.

- 네. 몬스터 웨이브를 막은 덕분에 민간 피해는 일절 없었고, 해당 변이 게이트도 신속하게 진압되었다고 합니다.

- 긴급 구조팀라고 하죠? 평화 길드의.

- 맞습니다. 모두가 아시는 진태경 헌터님이 직접 출동한 건 아니지만, 평화 길드 긴급 구조팀이 큰 활약을 선보였다고 하네요.

- 요즘 국내는 물론이고 해외에서 마력 수치 상승이 심각한 문제인데, 전 세계를 통틀어 우리나라가 가장 대응이 신속하고 피해가 미비한 것으로 인정받았습니다.

- 정말 대단한 일이죠. 진태경 헌터님을 비롯한 평화 길드의 긴급 구조팀뿐만 아니라, 이러한 상황 속에서도 몬스터와 싸우는 모든 헌터분들께서도…….

계속해서 이어지는 DJ의 목소리를 들으며, 팀장은 슬쩍 이동석을 바라봤다.

“그러고 보면 동석 씨도 참 대단해.”

“뭐가 말입니까?”

“그렇잖아. 요즘처럼 위험한 시기에 레이드 뛰는 게 쉬운 일이 아니거든.”

마력 수치 증가에 따라 몬스터는 강력해졌고, 일 년에 두어 번 터질까 말까 했던 변이 게이트는 이제 사흘에 한 번꼴로 나타나 아홉 시 뉴스의 헤드라이트를 장식한다.

팀장은 핸들을 꺾으며 말을 이었다.

“나야 식구들 때문에 이러는 거지만, 동석 씨는 아직 20대고 가장도 아니잖아. 젊은이의 패기. 뭐 그런 건가?”

“아닙니다.”

“응?”

“마땅히 해야 할 일이니까 하는 것뿐입니다. 제가 해야 해요.”

단호한 대답과 또렷하게 빛나는 눈동자. 지금까지와는 다른 그의 모습에 팀장이 눈을 깜빡였다.

“그, 그래?”

“예.”

“으응. 뭐, 보기 좋네. 헌터로서의 직업 정신이 아주 투철해.”

막상 상대방이 이렇게 나오니 당황스럽다. 특히 사명감이라는 단어가 어울릴 만큼 굳센 의지로 빛나는 이동석의 눈동자가 그랬다.

‘이놈 뭐야?’

싸가지는 없지만 정의에 불타는 청년. 난세의 영웅이 되기를 꿈꾸는 젊은이. 뭐 그런 건가. 뭐든 간에 별난 놈인 건 확실하다.

내심 중얼거린 팀장은 천천히 브레이크를 밟았다. 게이트 관리소 주차장에 차를 대고 내리자, 중형 밴을 알아본 팀원들이 몰려왔다.

“어이, 김 팀장 왔나?”

“오셨슴까, 햄.”

“일찍 오셨네요, 오빠. 그런데 옆에 계신 분은…….”

“이쪽은 동석 씨. 알지? 이번에 임시로 구했다는 그 친구.”

“아아, 맞나. 딱 보이끼네 스울 사람 맹키로 생깄네.”

“서울 출신 맞을걸요. 동석 씨, 이쪽은 우리 팀원들인데…….”

자연스럽게 고개를 돌린 팀장은 눈을 깜빡였다. 이동석의 상태가 어째 심상치 않았기 때문이었다.

“동석 씨. 혹시 어디 안 좋아?”

“…….”

“저기. 동석 씨?”

굳은 얼굴로 말없이 게이트를 바라보던 이동석이 이마에 맺힌 식은땀을 닦았다.

“아닙니다. 갑자기 조금 긴장이 되어서 그만.”

“음. 그래? 괜찮은 거지?”

“네. 아무런 문제도 없습니다.”

미심쩍은 눈빛으로 이동석을 바라본 팀장이지만, 이미 게이트 앞까지 온 이상 어쩔 수 없었다.

해운대에 위치한 C급 게이트, [세이렌의 검은 강]을 담당하는 관리소장은 이미 저 멀리서 어슬렁어슬렁 다가오고 있었다.

“어, 김 팀. 왔나.”

“예. 조금 늦었습니다.”

“아무 문제 없제? 인원수는 모두 맞췄고?”

이동석을 곁눈질한 팀장이 고개를 끄덕였다.

“그럼요.”

“확실한 기가? 규정 강화된 건 니도 잘 알끼고. 만약에 문제 생기면 니나 내나…….”

“어휴, 압니다. 저나 저희 팀원들이 사고 치는 거 보셨습니까. 어차피 다 점검하실 거면서.”

“요새 상황이 하도 숭하니 걱정돼서 그라제. 글고 점검은 내 안 그래도 그럴라 캤다.”

점검은 금방 끝났다. 이동석을 마지막으로 모든 사항을 체크한 관리소장이 씩 웃었다.

“됐다. 드가라.”

허락이 떨어지자 팀장을 비롯한 모두가 부산스럽게 떠들며 움직였다. 하지만 한 사람, 이동석만은 예외였다.

그는 무리의 끄트머리에서 덜리는 눈동자로 게이트를 응시하고 있었다.

쿵. 쿵.

심장이 거세게 두방망이질 쳤다. 보육원에 있던 시절부터 수족냉증으로 고생하던 그였는데, 지금은 다한증에라도 걸린 것처럼 손바닥이 식은땀으로 흥건했다.

‘긴장하지 말자. 마지막까지 절대.’

자신에게는 임무가 있었다. 반드시 해내야 하는 임무가.

이동석이 크게 심호흡한 그때, 맨 앞에서 걸어가던 팀장이 문득 뒤를 돌아보며 물었다.

“동석 씨. 정말 괜찮은 거 맞아?”

“……예.”

“표정이 안 좋은데. 대답도 늦고. 정신 딴 데다 두고 온 건 아니지?”

“아닙니다.”

팀장은 영원히 알 수 없을 것이다. 이동석이 대답이 늦었던 이유는 다른 곳에 정신이 팔려서가 아니라, 아직 익숙하지 않은 이름이었기 때문이라는 것을.

그리고 이동석은, 아니 그는 단 한 순간도 자신의 목적을 잊은 적이 없었다.

“걱정하지 마십시오. 반드시 해낼 테니까요.”

“뭐?”

팀장은 순간 이해할 수 없다는 표정을 지었지만, 이내 별난 놈이라는 눈빛을 보내고 돌아섰다.

그들은 이미 게이트의 입구에 서 있었다.

“자, 들어가기에 앞서서 모두 다 함께, 오늘도 안전제일!”

“안전제일!”

힘찬 구호가 울려 퍼지자 팀장이 게이트 입구를 향해 걸음을 내디뎠다.

“그럼 진입!”

솨아아악!

일렁이는 마력이 차례차례 사람들을 집어삼킨다.

사람들의 빠른 진입에, 이동석은 문득 고개를 들어 하늘을 바라보았다.

1월의 오전. 하늘은 푸르렀고 바람은 아직 차갑다.

그리고…… 이것이 그가 생전 마지막으로 보는 하늘일지도 모른다.



‘네게 맡겨야 할 임무가 있다.’



며칠 전 들었던 누군가의 목소리가 바람에 섞여 귓가에 닿는다.

그때 자신이 했던 대답도 함께.



‘하겠습니다.’

‘네 목숨이 위험해질 수도 있는 일이다.’

‘어차피 전(前) 부길드장님께서 살려 주신 목숨입니다.’



얼굴 한번 보지 못한 어머니는 지하철 화장실에서 그를 낳았다고 했다.

휴지에 싸여 쓰레기통에 버려졌던 갓난아기는 천운으로 살아남았고, 이정룡이 은밀히 후원하는 보육원으로 보내져 무럭무럭 자라났다.



‘도움이 될 수 있다면…… 뭐든 하겠습니다.’



이정룡은 그에게 있어 아버지였고, 아레스 길드는 아버지와 함께 살던 집이나 다름없었다.

그를 위해서라면 무엇이든 할 수 있었다.



‘맡겨 주십시오.’



굳은 의지가 서린 대답에 상대방은 진한 웃음을 지었었다.

그리고 한 가지 물건을 건네주었다. 지금은 그의 아공간 포켓 깊숙한 곳에 보관되어 있는 그것을.



‘꼭 성공해야 한다.’



그것이 마지막이었다. 명령을 받은 그는 얼굴과 이름을 비롯한 모든 것을 바꾸고 부산으로 내려왔다.

매우 값지고, 위험한 그것을 품에 간직한 채.

“저는…… 반드시 해낼 겁니다.”

어느덧 그의 차례다.

두려움을 애써 억누르며 스스로를 다잡는 중얼거림과 함께, 그는 일렁이는 마력장을 향해 걸음을 옮겼다.

솨아아악!

그리고 약 한 시간 뒤. 게이트 밖의 사람들은 볼 수 있었다.

삐삐삐삐삐!

미친 듯이 상승하는 마력 수치. 그리고 막을 수 없는 속도로 시작된 변화를.

키이이잉.

찢어지는 허공의 틈새, 짙은 죽음의 숨결이 해운대의 모래사장 위를 뒤덮었다.



* * *



세 번의 텔레포트 마법진을 타고 부산에 도착한 나는 즉시 깨달았다. 아니, 느낄 수 있었다.

- 꺄아아아악!

- 크아악!

콰아아아앙!

저 멀리서 들려오는 숱한 비명과, 어마어마한 굉음을. 그리고…….

쿠구구궁!

지축을 울리는 강대한 마력을.

“……시벌.”
```

## Final English reading copy

```markdown
# Chapter 570

Eight in the morning.

Even though the new year had dawned, people's daily lives remained unchanged.

Office workers in neat suits hurried toward work with exhausted faces, while the roads were jammed with cars.

*Honk! Honk—!*

At the ceaseless blare of horns, the middle-aged man behind the wheel of a midsize van rolled up the window he had left half-open and grumbled.

“Fuck. Even after going through the Great Cataclysm, this goddamn road still hasn’t been fixed. Are we supposed to drive or not?”

Swearing while driving was practically an unavoidable force of nature. Especially when driving in Busan.

The middle-aged man laid on the horn at the compact car trying to cut in without using its turn signal.

*Honk!*

But if the driver had possessed even a shred of common sense, there would have been no reason to honk in the first place.

The compact car drifted away, celebrating its lane change with its high beams in broad daylight. When the middle-aged man saw the message plastered across its rear window, he swore again.

> [A child is on board.]

“……Goddamn it. Is the kid literally on fire? Is that why they’re driving like that?”

Only after he had finished did the middle-aged man realize he had cursed. He looked toward the passenger seat and cleared his throat.

“Ahem. That just slipped out.”

The young man sitting beside him answered calmly.

“It’s all right. These things happen.”

His voice was directed at the middle-aged man, but his gaze remained tilted toward the window. The middle-aged man glanced at him before speaking again.

“Your name was…… Dongseok, right?”

“Yes.”

“That’s a relief. With things blowing up all over the place these days, it’s hard enough to remember someone’s full name.”

“These things happen. Don’t worry about it.”

“Ah, I don’t know if I told you last time, but my name is……”

“I’ll call you Team Leader. It’s more comfortable that way.”

The Team Leader blinked in bewilderment. Lee Dongseok had answered without a moment’s hesitation, and now he added:

“And, Team Leader.”

“Uh, yeah?”

“The light changed.”

*Hooooonk!*

The Team Leader snapped out of it at the blaring horn behind him and stepped on the gas. As the van lurched forward, his brow furrowed.

*What an unbelievable little asshole. That young punk.*

After muttering inwardly, the Team Leader soon changed his mind.

*Well, what does it matter if he’s a little rude? We’re only going to see each other for one day. As long as he does the job he was assigned, that’s enough.*

*Still, he’s a hundred times better than some trembling rookie or some loudmouth who only knows how to talk.*

The Team Leader was a C-rank Hunter who had worked as a freelancer for several years.

As such, he knew better than anyone that a guy who fought well and had no manners was preferable to someone likable and polite.

*At least he won’t shit the bed and disappear like that bastard a little while ago.*

They had needed a temporary team member to replace the man who had made a major mistake in a Gate and then gone into hiding. The result was Lee Dongseok.

His résumé was flawless, and based on the Team Leader’s own assessment, his ability as a Hunter seemed considerable. Almost enough to make it strange that he worked as a freelancer.

*Well, good is good.*

These days, finding people was a job in itself.

Even now, the DJs chatting softly on the radio were discussing the main reason for the recent shortage of Hunters.

—We have a comment from Shin Ayoung, a woman in her twenties living in Pocheon, Gyeonggi Province. “A Mutated Gate appeared near my home three days ago. Something like that happened only ten minutes away, and I’ve been so anxious that I’m suffering from insomnia.”

—Oh, no…… You live in that very neighborhood? That’s awful.

—I remember seeing this on the news, too. It was apparently an extremely dangerous situation that could easily have resulted in massive casualties.

—It’s a miracle it stopped just before a Monster Wave. Truly.

The Team Leader turned up the radio volume.

The Pocheon Mutated Gate, which had appeared only three days earlier, was an incident no Hunter could have failed to hear about.

Even Lee Dongseok, who had been staring out the window, seemed to be listening more closely.

—Fortunately, there were no deaths in this incident either.

—That’s right. Because the Monster Wave was stopped, there were no civilian casualties at all, and the Mutated Gate was quickly subdued.

—The Emergency Rescue Team, correct? The one from Peace Guild?

—That’s right. It wasn’t Hunter Jin Taekyung himself who went out there, but Peace Guild’s Emergency Rescue Team apparently put on an impressive performance.

—The rise in magic power readings has become a serious problem not only at home but overseas as well. Our country has been recognized as responding faster and suffering less damage than any other country in the world.

—It’s truly remarkable. Not only Hunter Jin Taekyung and Peace Guild’s Emergency Rescue Team, but all the Hunters fighting monsters in these circumstances deserve our……

As the DJ’s voice continued, the Team Leader discreetly glanced at Lee Dongseok.

“Come to think of it, you’re pretty impressive too, Dongseok.”

“What do you mean?”

“You know what I mean. Raiding in a dangerous time like this isn’t easy.”

As magic power readings rose, monsters grew stronger, and Mutated Gates that once appeared only once or twice a year were now occurring roughly once every three days and making the nine o’clock news headlines.

As he turned the wheel, the Team Leader continued.

“I’m doing this because I have a family, but you’re still in your twenties, and you’re not even the head of a household. Is it youthful ambition or something?”

“No.”

“Hm?”

“I’m only doing what needs to be done. I have to do it.”

His answer was decisive, and his eyes shone with a clarity they had not shown before. The Team Leader blinked at the unfamiliar side of him.

“R-really?”

“Yes.”

“Well, huh. Good for you. That’s some serious professional dedication.”

The Team Leader was taken aback by the young man’s response—especially by Lee Dongseok’s eyes, which shone with such steadfast resolve that *sense of duty* seemed the only phrase for it.

*What the hell is this guy?*

A rude young man burning with a sense of justice. A youth dreaming of becoming a hero in an age of chaos. Something like that.

Whatever the case, he was definitely an unusual guy.

Still muttering inwardly, the Team Leader slowly pressed the brakes. When he parked in the Gate management office’s lot and got out, the team members who recognized the midsize van came rushing over.

“Hey, Team Leader Kim. You made it.”

“You’re here, hyung.”

“You’re early, oppa. But who’s the person beside you……?”

“This is Dongseok. You know him, right? The guy we hired temporarily this time.”

“Ah, is that right? I could tell at a glance. He looks just like someone from Seoul.”

“He probably is from Seoul. Dongseok, these are our team members……”

The Team Leader naturally turned his head, then blinked.

Something about Lee Dongseok’s condition seemed strange.

“Dongseok. Are you feeling sick?”

“…….”

“Hey. Dongseok?”

Lee Dongseok stared silently at the Gate with a rigid expression before wiping the cold sweat from his forehead.

“No. I suddenly became a little nervous.”

“Hmm. Are you all right?”

“Yes. There’s no problem.”

The Team Leader looked at him suspiciously, but now that they had reached the Gate, there was nothing to be done.

The manager of the office responsible for the C-rank Gate located in Haeundae—*Siren’s Black River*—was already shuffling toward them from a distance.

“Oh, Team Leader Kim. You’re here.”

“Yes. We’re a little late.”

“No trouble, right? Got everyone accounted for?”

The Team Leader glanced at Lee Dongseok and nodded.

“Of course.”

“You sure? You know the regulations have been tightened. If something goes wrong, you and me both……”

“Aw, I know. Have you ever seen me or my team cause trouble? You’re going to inspect everything anyway.”

“Things are so bad these days that I can’t help worrying. And I was going to inspect you regardless.”

The inspection ended quickly. After checking every detail, with Lee Dongseok last, the manager grinned.

“All right. Go on in.”

Once they received permission, everyone, including the Team Leader, began moving noisily. Everyone except one person.

At the very back of the group, Lee Dongseok stared at the Gate with trembling eyes.

*Thump. Thump.*

His heart pounded fiercely. He had suffered from cold hands and feet since his days in the orphanage, but now his palms were drenched in cold sweat as if he had developed hyperhidrosis.

*Don’t get nervous. Not until the very end.*

He had a mission. A mission he absolutely had to complete.

Just as Lee Dongseok took a deep breath, the Team Leader, walking at the front, suddenly looked back.

“Dongseok. You really are all right, aren’t you?”

“……Yes.”

“You don’t look so good. And you were slow to answer. You didn’t leave your mind somewhere else, did you?”

“No.”

The Team Leader would never know that the reason Lee Dongseok had been slow to answer was not because his mind was elsewhere, but because he was still not used to the name.

And Lee Dongseok—or rather, he—had not forgotten his purpose for even a moment.

“Don’t worry. I’ll definitely do it.”

“What?”

The Team Leader looked confused for a moment, then turned away with a look that said the young man was strange.

They were already standing at the entrance to the Gate.

“All right, before we go in, everyone together. Safety first, today too!”

“Safety first!”

After the energetic chant rang out, the Team Leader stepped toward the Gate entrance.

“Then, moving in!”

*Whoosh!*

The rippling mana swallowed the people one after another.

As the others entered quickly, Lee Dongseok suddenly lifted his head and looked up at the sky.

It was a January morning. The sky was blue, and the wind was still cold.

And…… this might be the last sky he ever saw.

*There is a mission I need you to undertake.*

Someone’s voice from several days earlier reached his ears, mingling with the wind.

Along with the answer he had given at the time.

*I’ll do it.*

*It’s a mission that could put your life in danger.*

*The former Vice Guild Master saved my life anyway.*

His mother, whose face he had never seen, had apparently given birth to him in a subway restroom.

The newborn wrapped in toilet paper and thrown into a trash can survived by sheer luck, then was sent to an orphanage secretly supported by Lee Jungryong, where he grew up healthy and strong.

*If I can be of help…… I’ll do anything.*

To Lee Dongseok, Lee Jungryong had been a father, and Ares Guild had been no different from the home he had shared with him.

He could do anything for him.

*Leave it to me.*

At that answer, filled with firm resolve, the other person had smiled deeply.

Then he handed Lee Dongseok an object—something now stored deep inside his subspace pocket.

*You absolutely must succeed.*

That was the last thing.

After receiving his orders, he changed everything, from his face to his name, and came down to Busan.

Carrying the extremely valuable and dangerous object close to him.

“I…… will definitely do it.”

His turn had come before he knew it.

Suppressing his fear and steeling himself with a low mutter, he stepped toward the rippling field of mana.

*Whoosh!*

About an hour later, the people outside the Gate saw it.

*Beep beep beep beep!*

A magic power reading rising at a mad pace. And a transformation beginning at a speed that could not be stopped.

*Kiiiiing.*

A tear split open in the air, and a dense breath of death spread across the sandy beach of Haeundae.

* * *

After arriving in Busan via three Teleportation magic circles, I immediately realized it.

No—I could feel it.

—Aaaaaah!

—Aaargh!

*Kwaaaang!*

The countless screams and tremendous explosions coming from far away. And……

*Kuuung!*

The immense mana that shook the earth.

“……Fuck.”
```

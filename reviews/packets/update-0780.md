<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0780.txt",
      "sha256": "e91d0fd834a8d1b4ccc9defd118f73473b66e6d62433d60aceea20736be240d1",
      "bytes": 13009
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "14c86d98946bac84b87b69b9f27db0ee6ea3a68401f21e3a24d110087534b533",
      "bytes": 1084
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "d1141814e80b2fb9610ae483c1ba070a6082286f2e06d6c2aaebb97ee1e2636d",
      "bytes": 223318
    },
    {
      "path": "characters/Cheon Taemin.md",
      "sha256": "560bdd41733960e848759ec54725f335e1820ca7adf304a361913d8c3c9f5980",
      "bytes": 752
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "13e33c508012976e7ab77ec0602d055810073fdbd28fa685002f60ce82b2e2f3",
      "bytes": 553
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "b54feb1d521a6f75e79a7ee0727981d49f6844a83584d2bf18403d805c5ca868",
      "bytes": 2096
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "8856569c9f10e09d9750904343fe3b6c1c51ac18abb45166d1ad744b9db3cd69",
      "bytes": 622
    },
    {
      "path": "characters/Lee Jungryong.md",
      "sha256": "9a17f8475e10ddeac372fb917aeede9d7438f5d4cc6f4a3793a59c52aa9bb665",
      "bytes": 1384
    },
    {
      "path": "characters/Michael.md",
      "sha256": "faf67a1fc892046ce72c0c0b6058e1e71553566b77b8b0e144d34869fe3eed4b",
      "bytes": 859
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "1d8c3c09a97790f1e57e8696a140c54ba5e6db76c9a06b5af6ea7582824fd7c2",
      "bytes": 787
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "94db0ccaf07c837679b7f87b9a78ba95b0663f9720da03df5feccd73c0fb303f",
      "bytes": 242593
    }
  ],
  "estimated_tokens": 10142
}
-->

# Durable State Update — Chapter 780

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 780. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 780. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history.
`names` contains only newly required Korean-to-English rows that are absent from
Exact glossary matches; Korean keys must occur in the source. Do not repeat
glossary matches. The controller drops rows already in the names ledger.
`address_pairs` contains only newly required speaker→addressee rows that
are absent from Matched address pairs. Speaker and addressee must be Hangul source
spellings such as 진태경 or 혁무진, never English names. Arabic digits are
allowed in titles such as 1팀장. At least one endpoint must occur in the source.
Before returning JSON, verify every `speaker` and `addressee` value contains at
least one Hangul character; use the Korean source spelling even when the same
person's English name appears in the reading copy. If no valid new pair exists,
return `"address_pairs": []`.
The controller drops pairs already in the address ledger. Do not invent
risk-register rows. Beat plot paragraphs are plain strings; continuity and
translation decisions are concise list items.
Return this exact shape:

{
  "chapter": 780,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 780,
    "continuity_sources": [780],
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
    "The Stone King’s identity as a monster has been revealed at the World Hunter Federation gathering, and Jin is protecting him as a friend and comrade-in-arms who saved his life.",
    "Magic Johnson, Chuck Hagel, Faye Chen, Felix, and Choi Minwoo openly side with Jin after Fabian threatens him.",
    "Fabian is the Guild Master of Kronos and an S-rank Hunter active since the Great Cataclysm.",
    "Michael intends to lead the World Hunter Federation and has threatened to seek Jin’s permanent expulsion; Jin suspects Michael may himself be no different from a monster.",
    "Cheon Taemin remains in a coma and too ill to join the coming war."
  ],
  "continuity_sources": [
    779,
    778
  ],
  "open_questions": [
    "Who will lead the World Hunter Federation, and will its members vote to expel Jin?",
    "Will Michael act on his threat against Jin, and what does Jin’s reference to Michael’s neck wound imply?",
    "Can Cheon Taemin recover from his coma?"
  ],
  "safe_through": 779,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 천태민    | **Cheon Taemin**  |
| 이정룡    | **Lee Jungryong** |
| 상태               | **Status**                     |
| 몬스터     | **monster**           |
| 길드      | **Guild**             |
| 길드장     | **Guild Master**      |
| 대격변     | **Great Cataclysm**   |
| 도사      | **Daoist**                                                      |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 미카엘 | **Michael** | Guild Master of Odin Guild. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 전세 | **jeonse lease** | Korean lump-sum deposit lease used in the family's redevelopment-era housing history. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 무한 | **Wuhan** | Capital of Hubei Province near Dongting Lake. |
| 대마도사 | **Grand Mage** | Title used for Magic Johnson. |
| 정룡 | **Jungryong** | Cheon Taemin's trusted associate who joined the Peace Guild. |
| 오딘 | **Odin** | The name of the world's greatest Guild, invoking the Norse god. |
| 마력 | **magical power** | Distinct from mana; the Skeleton King's area of expertise. |
| 실베르트 | **Silbert** | Family name in Michael Silbert. |
| 크로노스 | **Kronos** | Guild led by Fabian. |

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
| 태산 | 진태경 | subordinate_to_respected_outsider | Jin Taekyung | clipped and familiar | Taishan says he likes Jin Taekyung but will fight him without hesitation if Sama Pyo commands it. |
| 진태경 | 태산 | pavilion_master_to_pavilion_member | Taishan | forceful and commanding | Taekyung orders Taishan to stop eating the bear. |
| 미카엘 | 진태경 | rival_to_target | you | quietly polite but threatening | Michael warns Jin to reconsider for the sake of Jin's monster friend. |
| 진태경 | 미카엘 | target_to_rival | Go fuck yourself | blunt and profane | Jin rejects Michael's proposal to resurrect the World Hunter Federation. |

## Listed compact profiles

### Cheon Taemin.md

# Cheon Taemin (천태민)

- **Safe through:** Chapter 779
- **Aliases:** Slayer; Sky (the American epithet used for him)
- **Role:** Cheon Taemin is Ares Guild Master and the world's greatest Hunter, known as the Slayer for killing the Demon King and creating the first Mana Cultivation Method during the Great Cataclysm, and he remains unconscious after more than twenty years in a wired mechanical capsule at his former mansion.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** Maternal grandfather of Team Leader Choi and Jin Taekyung and father of Soyeong; regarded by Lee Jungryong as an older brother despite their lack of blood relation.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 779
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 779
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple, the Fire Gate Clan's nineteenth successor, the Pavilion Master of the Fire Dragon Pavilion within the Murim Alliance, a Supreme Peak master with the Heavenly Martial Physique and Force, and a publicly recognized S-rank-level Hunter who formally retains an A-rank license, as well as a traveler between Murim and another world resembling the realm of immortals and the principal Hunter opposing Michael Silbert's terrorist campaign.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real; treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements as well as the Peace Guild's Guild Master, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Magic Johnson is an allied Grand Mage who supplies him with intelligence, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 779
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Lee Jungryong.md

# Lee Jungryong (이정룡)

- **Safe through:** Chapter 778
- **Aliases:** None
- **Role:** Former Vice Guild Master of Ares Guild, one of Korea's two S-rank Hunters, and a Supreme Peak-level martial artist who was killed by Jin Taekyung.
- **Personality:** Outwardly genial, calm, and humorous; calculating, opportunistic, manipulative, coercive, and ruthless when challenged
- **Voice:** Smooth, good-natured, and indirect, using teasing conversation and veiled threats before becoming openly furious
- **Relationships:** Master of Park Jihoon and Go Jun (Team Leader Seok), whom he personally selected and trained; longtime Great Cataclysm acquaintance of Park Tae Seop; adversary of Jin Taekyung; knew Team Leader Choi from childhood; has an antagonistic history with Kim Hwajong, who saved his life at the collapse of Mapo Bridge eighteen years earlier; was visibly shaken by learning that Choi is Cheon Taemin's maternal grandson; regarded Cheon Taemin as an older brother despite no blood relation and long held him in respect and fear; secretly supported the orphanage where Lee Dongseok grew up and was regarded by Dongseok as a father; operated as Ares Guild's senior authority beneath its Guild Master; concealed Taemin's condition with Song Cheonwoo and participated in purging aides who knew the truth.

### Michael.md

# Michael (미카엘)

- **Safe through:** Chapter 779
- **Aliases:** None
- **Role:** Michael Silbert is Odin Guild Master and a public hero positioning himself to lead the World Hunter Federation; he intends to eliminate Jin Taekyung as soon as possible.
- **Personality:** Controlled, calculating, condescending, and confident in his intelligence and ability to manipulate events, but increasingly impatient and anxious since learning of Jin Taekyung.
- **Voice:** Polite and conversational when relaxed, but quietly authoritative and coercive when asserting control.
- **Relationships:** Michael personally selected and trained Huginn, commands Odin Guild's hidden alliance, secretly confers with The Prophet, and regards Jin Taekyung's friendship with the monster as his fatal weakness.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 724
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion; he helped Jin escape the underground prison by blocking the stairs and overpowering the Bai warriors.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo; becomes explosively violent when his meat is threatened.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord, trusts Jin Taekyung as Pavilion Master, and has grown attached to the Fire Dragon Pavilion members.

## Korean source

```text
＃780화



세상에는 수많은 사건과 그에 따른 가능성이 존재한다.

문제는 그중 어느 것도 확실치 않다는 것이다.

아무리 문명이 발달하고, 최첨단 과학이 지금껏 닿을 수 없는 영역까지 도달했어도 완전무결한 100%는 존재하지 않는다.

하물며 기계가 아닌 사람의 일이라면 더더욱.

하지만 지금 이 순간.

“목의 상처는 나았나, 미카엘?”

파르르 떨리는 회색빛 눈동자를 보며 나는 확신했다.

아주 작은 단서로부터 시작된 이 믿을 수 없던 의문이, 비로소 어두컴컴한 실체를 드러냈다는 것을.

마침내 놈을, 미카엘 실베르트를 낭떠러지로 몰았다는 것을.

그러나 나는 입가에 맺혀 있던 웃음을 지웠다.

전세(戰勢)를 뒤집었다는 기쁨보다 눈앞의 상대에 대한 혐오가 더욱 컸기에.

나는 온통 회색빛으로 물든 저 사내의 모든 것을 경멸했다.

“이 버러지 같은 새끼.”

입술을 비집고 흘러나온 목소리가 정적을 깨트린다.

그리고 앞서 스켈레톤 킹의 정체를 밝혔을 때와는 달리, 이번에는 좌중의 그 누구도 나를 비웃지 못했다.

아니, 지금 저들은 조금 전 자신들이 들었던 말을 완전히 이해하지 못하고 있었다.

혹은 너무나 생각지도 못한 진실을 받아들일 수조차 없었거나.

“지금 그게…… 도대체 무슨 소리지?”

크로노스 길드장의 목소리다. 나는 미카엘 실베르트에게 시선을 고정한 채 입을 열었다.

“물어봐, 당사자한테 직접.”

숨 막히는 침묵 속, 수백 쌍의 시선이 미카엘 실베르트를 향해 쏠렸다.

물론 그중에는 이미 조사를 통해 알고 있던, 또는 몰랐던 놈의 지지자들 역시 포함되어 있었다.

“아까 보니까 다들 앞뒤로 열심히 빨아 주던데, 그중에 뭐 하나 제대로 알려 준 놈이 없었나 보네. 하긴, 그럴 만도 하겠지. 안 그래?”

미카엘 실베르트는 대답 대신 나를 물끄러미 응시했다.

아직도 파문이 남아 있는 놈의 회색빛 눈동자에서, 지금쯤 머릿속을 떠다니고 있을 수많은 생각이 읽히는 듯했다.

하지만.

“괜히 힘들게 대가리 굴리지 마라. 이미 알고 있잖아?”

모든 공식이 성립된 이상, 답은 나왔다.

“미카엘 실베르트.”

마치 오랫동안 헤매던 미로를 빠져나온 기분이다.

그리고 사방을 가로막았던 벽을 지나, 마침내 도달한 출구에는 한 사람이 기다리고 있었다.

빛과 어둠. 그 사이 어딘가에서 서성이다 끝끝내 돌아올 수 없는 강을 건넌 회색빛의 괴물이.

놈의 실체를 가리고 있던 장막의 끝자락이.

“넌…….”

나는 참았던 숨을 토해 냈다.

“이제 좆 됐어.”



* * *



미카엘 실베르트는 문득 생각했다.

도대체 언제, 어떻게, 어디서부터 어긋나기 시작한 걸까.

그러나 아무리 생각해도 의문에 대한 답을 찾을 수는 없었다.

현재의 이 모든 상황은 한 존재로부터 비롯되었으니까.

만약 그가 그 답을 알아낸다 해도, 눈앞의 상대는 반드시 또 다른 변수를 만들어 냈을 테니까.

‘진태경.’

무한한 변수의 또 다른 이름.

그의 앞을 가로막기에는 아직 턱없이 젊고, 무모하며, 경박하기까지 한 동양인 청년.

그러나 이제는 미카엘 실베르트도 인정하지 않을 수 없었다.

저 청년은 단순히 치워야 하는 장애물이 아니라, 반드시 부수었어야 하는 또 다른 벽이었다는 사실을.

‘뜨겁구나.’

저 검은 눈동자에 담긴 빛과 같은 열기가.

동시에 지금까지도 낙인(烙印)처럼 남아 있는 목덜미의 상처가 지지듯이 아파 왔다.

툭.

미카엘 실베르트는 자신도 모르게 목을 더듬었다.

하지만 상처를 감추기 위해 목까지 뒤덮은 갑옷의 차가운 감촉이 손끝으로 전해지자, 문득 실소가 흘러나왔다.

변명? 수습?

지금 같은 상황에서는 무의미하다. 되려 추해질 뿐이다.

물방울 하나가 바위를 쪼개는 것처럼, 미카엘 실베르트라는 태산(太山)을 무너트리는 것은 손바닥만 한 포션 한 병으로도 족했다.

‘신체가 포션에 담긴 마나(Mana)를 받아들이지 못하게 된 이상, 어떤 변명도 소용없겠지.’

다만 의문이 남았다.

어떻게 진태경이 이 비밀을 알게 되었는지. 수많은 위험과 불확실성으로 점철된 양날의 검으로 자신을 찌를 마음을 품었는지에 대한 의문이.

그렇기에 미카엘 실베르트는 변명 대신 질문을 택했다.

“하나만 묻지. 어떻게 알았나?”

“……!”

진태경을 향한 짧은 물음. 그러나 그 한 마디가 불러온 여파는 실로 막대했다.

“지금…… 뭐라고?”

“기, 길드장님.”

사실상 인정이나 다름없는 그 말에 가장 큰 충격을 받은 것은 바로 미카엘 실베르트를 열렬히 지지하던 이들이었다.

그러나 그는 석상처럼 굳어 버린 자신의 아군들에게는 시선 한번 주지 않았다.

그저 사람들의 비난 속에서 진실을 밝히던 진태경이 그러했듯이 같은 말을 재차 반복할 뿐이었다.

“어떻게 알았느냐 물었네.”

그리고 곧이어 들려온 대답은, 앞서 던진 질문보다 짧았다.

“지크프리트 바스만.”

“지크프리트?”

“그래, 그 양반이 죽기 전에 참 이것저것 많이도 조사해 놨더라고.”

쉭!

순간 울려 퍼지는 파공성.

마치 화살처럼 날아든 한 장의 종이를 두 손가락으로 받아 낸 미카엘 실베르트는, 맨 윗줄에 적힌 제목을 읊조렸다.

“……마나와 마력의 양립성.”

“대마도사이기 전에 당대 최고의 몬스터 학자였다더니. 별걸 다 연구했더군.”

“분명 남은 연구 자료는 없었을 텐데.”

“그랬겠지. 알려진 바로는.”

미카엘 실베르트는 말없이 손에 들린 종이를 내려다봤다.

빠르게 움직인 회색빛 눈동자가 모든 내용을 읽고, 이해하기까지 걸린 시간은 찰나에 불과했다.

“인간의 신체에 몬스터의 마력을 받아들여 공존시킬 가능성을 연구하다니. 누가 봐도 지크프리트 바스만 정도 되는 괴짜나 할 수 있는 미친 소리지. 물론…….”

진태경의 나직한 목소리가 귓가를 울렸다.

“당신한테는 아니었겠지만.”

미카엘 실베르트는 고개를 들었다. 어느덧 형편없이 구겨진 종이가, 그의 손아귀에서 불길에 휩싸였다.

화륵. 투두둑.

잿가루가 흩날린다. 그 너머에서 착 가라앉은 한 쌍의 눈동자가 불그스름한 열기를 띠었다.

“지크프리트 바스만도 그게 궁금했던 모양이야. 하지만 그런 그조차 끝끝내 입증에는 실패했지. 아니, 어쩌면 금기(禁忌)를 범했다는 생각에 연구를 중단했을지도 몰라.”

진태경은 날아드는 잿가루를 바라보며 말을 이었다.

“이런 자료를 남겨 두면 안 된다는 그만의 의지였는지. 아니면 그를 죽인 누군가의 뜻이었는지는 몰라도…… 해당 연구에 대해서는 남은 자료가 거의 없더라고. 덕분에 저걸 찾아내기까지 시간이 꽤 걸렸지.”

“자네는 바로 이것 때문에 내가 그를 죽였다고 생각하나?”

“처음에는 그렇게 생각했지.”

“처음에는?”

“그래. 하지만 당신이 지크프리트 바스만을 제거한 건 다른 이유가 있어서야.”

“부정하지는 않겠지만, 그렇게 생각한 이유를 묻고 싶군.”

“간단해. 당신은 이 연구 자료를 남겨 둘 만큼 허술하지 않으니까.”

그 말을 들은 직후, 말없이 진태경을 바라보던 미카엘 실베르트는 소리 내어 웃었다.

“그거 고맙군. 자네까지 나를 그런 병신 취급했다면 내심 안타까웠을 거야.”

“고맙긴. 그저 병신이 아니라 씹새끼로 취급했을 뿐이지.”

“하지만 아직 명쾌한 해답이 나오지 않았네. 고작 이런 자료로 나를 의심하기에는 턱없이 부족했을 텐데.”

“아니, 충분했어.”

“어째서?”

“범죄가 벌어지면, 근처에 사는 전과자가 가장 먼저 의심을 받는 건 당연한 이치니까.”

“……!”

“얼마 남지도 않은 그 연구 자료를 다시 한번 살피는데, 문득 그런 생각이 들더라고.”

진태경은 경멸 어린 조소와 함께 고개를 돌렸다.

온통 의문 투성이였던 대마도사의 죽음에 대한 진실까지 밝혀진 지금, 충격에 휩싸인 좌중은 얼어붙은 채 두 사람만을 바라보고 있었다.

“만약 미카엘 실베르트가, 그 씨벌 놈이 정말 이미 반인반마(半人半魔)나 다름없는 상태라면. 이 허무맹랑한 연구 자료를 이미 현실로 이루었다면 어땠을까 하는 생각이.”

완전한 침묵 속, 진태경은 처음 그 생각을 떠올랐던 순간을 되새겼다.

수백 쌍의 눈과 귀 앞에서. 자신이 아닌 다른 누군가가 처음부터 끝까지 철저히 기획한 그 무대 위에서.

마치 홀로 스포트라이트를 받는 주인공처럼 입을 열었다.

“그랬더니…… 마침내 모든 퍼즐이 맞춰졌지.”

누구도 떠올릴 수 없었던 그 가정(假定)이야말로, 바로 이 복잡한 퍼즐을 완성할 마지막 한 조각이었다.

미카엘 실베르트가 스켈레톤 킹의 정체를 알아차릴 수 있었던 이유.

대격변 당시에는 수백 명의 영웅 중 한 사람에 불과했던 그가, 용의 꼬리에서 머리로 성장할 수 있었던 이유.

그리고 오딘 길드의 성장이 천태민의 잠적을 기점으로 시작되었던 이유와 세계 각국의 명사들이 참석한 이정룡의 장례식에서조차 모습을 내비치지 못한 이유까지.

모두 오직 한 가지 때문이었다.

“마력(魔力).”

진태경은 천천히 돌아섰다. 더 이상 흔들리지 않는 회색빛 눈동자를 바라보며 말을 이었다.

“그럴 수 있었던 방법도, 계기도 알 수 없지만…… 당신은 마력을 흡수함으로써 강해질 수 있었어. 마치 몬스터처럼.”

그러나 동시에 마나를 품고 있었기에, 그 기운의 균형을 완벽히 조절하고 숨겨 왔기에 누구도 그의 실체를 알아낼 수 없었다.

심지어는 스켈레톤 킹조차도.

미카엘 실베르트에 관한 대화를 나눌 때마다 입버릇처럼 붙였던 ‘불쾌한 인간’이라는 수식어가 무엇을 뜻하는지, 몬스터인 그조차도 명확히 정의 내리기 어려울 정도였으니까.

이 세상에서 미카엘 실베르트가 누구보다 두려워하고, 자신의 정체를 반드시 숨겨야 하는 존재가 있다면 그건 바로 한 사람뿐이었다.

“천태민. 그분이었다면 네 실체를 알아봤겠지.”

그리고 진태경의 나직한 목소리가 모두의 귓가에 닿은 그 순간.

한 사람의 메마른 입술이 긴 침묵을 깨트리며 달싹였다.

“그래, 그로 인해 오랜 세월을 숨죽이며 살아야 했지. 자네가 지금껏 살아온 인생과 비슷할 만큼, 아주 오랜 세월을.”

무려 삼십여 년의 세월이 지났지만, 미카엘 실베르트는 지금까지도 똑똑히 기억하고 있었다.

새로운 힘을 얻게 된 지 얼마 되지 않았을 무렵.

수많은 이들이 한자리에 모인 가운데 정확히 자신을 응시하고 있던 절대자의 시선을. 그 순간 전신을 옥죈 공포를.

당시에는 터무니없을 만큼 적은 마력을 보유했었기에 더 이상의 시선은 받지 않았으나, 그날 느꼈던 공포는 쉽게 사라지지 않았다.

시간이 흘러 천태민이 자취를 감추고, 지그프리트 바스만에게서 A구역에 얽힌 비밀을 알아낸 후에도.

심지어 이정룡의 장례식 때도 참석하지 않았다.

만에 하나 그가 가진 정보가 틀렸을 수도 있으니까.

천태민이, 자신의 실체를 꿰뚫어 볼 수 있는 유일한 존재를 그곳에서 마주칠지도 모르니까.

하지만…….

“한 가지. 자네가 착각하는 게 있네.”

나직한 목소리와 함께, 미카엘 실베르트는 몸속 깊숙이 잠든 거대한 기운을 일깨웠다.

이미 오래전부터 빛과 어둠이 뒤섞였던, 그러나 어느 날부터 증폭된 어둠으로 짙게 물들어 버린 그 혼탁한 미증유(未曾有)의 기운을.

“이 세상에서 내가 두려워하는 유일한 한 사람은, 지금 이 자리에 없어.”

구구구구궁.

파도처럼 일어난 거대한 기파가, 사방을 짓눌렀다.
```

## Final English reading copy

```markdown
# Chapter 780

The world was full of incidents and all the possibilities that followed from them.

The problem was that none of those possibilities was certain.

No matter how far civilization advanced, no matter how cutting-edge science reached into realms once beyond its grasp, there was no such thing as a perfect, one-hundred-percent certainty.

And that was all the more true when it came to people, rather than machines.

But at this very moment—

“Has the wound on your neck healed, Michael?”

Looking at those trembling gray eyes, I was certain.

The unbelievable question that had begun with the tiniest clue had finally revealed its dark shape.

At last, I’d driven him—Michael Silbert—to the edge of the cliff.

But I wiped the smile from my lips.

My disgust for the man standing before me outweighed any joy at having turned the tables.

I despised everything about the man drenched in gray.

“You filthy piece of shit.”

My voice slipped past my lips and shattered the silence.

And unlike when I’d revealed the Skeleton King’s identity, not one person in the room laughed at me this time.

No. They hadn’t fully understood what they’d just heard.

Or perhaps the truth was so far beyond anything they’d expected that they couldn’t bring themselves to accept it.

“What… what the hell does that mean?”

It was the Guild Master of Kronos. I kept my eyes fixed on Michael Silbert as I answered.

“Ask the man himself.”

In the suffocating silence, hundreds of pairs of eyes turned toward Michael Silbert.

Among them were some of his supporters who’d already known from their investigation, and others who hadn’t.

“From what I saw earlier, you were all busy kissing his ass. Guess none of you had anyone to tell you what was really going on. Well, that figures. Doesn’t it?”

Michael Silbert didn’t answer. He simply stared at me.

There were still ripples in his gray eyes, and I felt as if I could read all the thoughts that must be swirling around in his head.

But—

“Don’t strain yourself trying to figure it out. You already know, don’t you?”

Once every piece of the puzzle was in place, the answer was clear.

“Michael Silbert.”

It felt like I’d finally escaped a maze I’d been wandering through for ages.

And beyond the walls that had hemmed me in on every side, one person waited at the exit.

A gray monster who’d lingered somewhere between light and darkness, then crossed the river from which there was no return.

The last edge of the veil that had hidden his true nature—

“You…”

I let out the breath I’d been holding.

“You’re fucked now.”

* * *

Michael Silbert suddenly wondered:

When had things started going wrong? How? Where had it begun?

But no matter how hard he thought, he couldn’t find an answer.

Everything that had led to this moment had begun with one person.

And even if he did figure it out, the man in front of him would surely have found some other way to change the equation.

*Jin Taekyung.*

Another name for endless variables.

An Eastern young man who was far too young, reckless, and even frivolous to stand in his way.

But Michael Silbert could no longer deny it.

That young man wasn’t merely an obstacle to be removed. He was another wall that Michael should have broken through at all costs.

*So intense.*

The heat in those black eyes.

At the same time, the wound on the back of his neck—still branded there like a burn—throbbed with scorching pain.

Tap.

Without realizing it, Michael Silbert reached for his neck.

But when his fingertips met the cold armor that covered it all the way up to his throat, hiding the wound, a dry laugh escaped him.

Excuses? Damage control?

In a situation like this, they were meaningless. They would only make him look pathetic.

Like a single drop of water splitting a rock, a potion no bigger than his palm was enough to bring down the mountain that was Michael Silbert.

*Now that my body can no longer accept the mana in a potion, no excuse will do me any good.*

But one question remained.

How had Jin Taekyung learned the secret? What had made him willing to stab Michael with a double-edged sword riddled with danger and uncertainty?

So instead of making excuses, Michael Silbert chose to ask.

“I’ll ask you one thing. How did you find out?”

“……!”

It was a brief question directed at Jin Taekyung. But the shock it sent through the room was immense.

“What… what did you just say?”

“Guild Master…”

That was as good as an admission. And the people most shaken by it were the ones who had fervently supported Michael Silbert.

But he didn’t so much as glance at his allies, frozen like statues.

Just as Jin Taekyung had revealed the truth while people hurled accusations at him, Michael repeated himself.

“I asked how you found out.”

And the answer he received was shorter than the question.

“Siegfried Bassman.”

“Siegfried?”

“Yeah. Turns out the old man had investigated all sorts of things before he died.”

Whoosh!

A sheet of paper shot through the air like an arrow. Michael Silbert caught it between two fingers and murmured the title written at the top.

“…The Compatibility of Mana and Magical Power.”

“They say he was the greatest monster scholar of his age, even before you count his being a Grand Mage. Looks like he researched just about everything.”

“There shouldn’t have been any research material left.”

“Sure. That’s what people knew.”

Michael Silbert silently looked down at the paper in his hand.

His gray eyes moved quickly. It took him only an instant to read and understand the entire page.

“Studying the possibility of introducing a monster’s magical power into a human body and making the two coexist. That’s the kind of crazy idea only a lunatic like Siegfried Bassman could come up with. Of course…”

Jin Taekyung’s low voice rang in his ears.

“That wouldn’t have been true for you.”

Michael Silbert raised his head. The sheet, now hopelessly crumpled, caught fire in his grip.

*Fwoosh. Crumble.*

Ash drifted through the air. Beyond it, the eyes that had gone cold now held a reddish glow.

“Looks like Siegfried Bassman was curious about the same thing. But even he never managed to prove it. Or maybe he stopped researching because he thought he’d crossed a taboo.”

Jin Taekyung watched the ash as it drifted toward him and continued.

“Maybe he had his own reasons for not leaving this kind of material behind. Or maybe whoever killed him made sure it was gone. Either way, there was almost nothing left about that research. It took me quite a while to find that.”

“You think this is why I killed him?”

“At first, yeah.”

“At first?”

“Right. But you had another reason for killing Siegfried Bassman.”

“I won’t deny it. But I’d like to know why you think that.”

“It’s simple. You’re not careless enough to leave research materials like this lying around.”

After staring silently at Jin Taekyung for a moment, Michael Silbert laughed out loud.

“I appreciate that. I would’ve been disappointed if even you thought I was an idiot.”

“Don’t mention it. I just thought you were a piece of shit, not an idiot.”

“But you still haven’t given me a clear answer. This material alone wouldn’t have been nearly enough to make you suspect me.”

“No. It was enough.”

“Why?”

“When a crime happens, it’s only natural to suspect the ex-convict who lives nearby first.”

“……!”

“As I looked over what little research material was left, that thought suddenly crossed my mind.”

With a scornful sneer, Jin Taekyung turned his head.

The truth behind the Grand Mage’s death—a mystery from beginning to end—had now been revealed. The stunned crowd stood frozen, staring at the two men.

“What if Michael Silbert, that son of a bitch, really was already as good as half human and half demon? What if he’d already made that absurd research a reality?”

In the utter silence, Jin Taekyung recalled the moment the thought had first come to him.

Before hundreds of watching eyes and ears. On a stage someone other than him had planned meticulously from beginning to end.

He spoke like a leading man standing alone in the spotlight.

“And then… finally, all the pieces fell into place.”

That hypothesis no one else could have thought of was the last piece needed to complete this complicated puzzle.

Why Michael Silbert had realized the Skeleton King’s true identity.

Why a man who’d been just one hero among hundreds during the Great Cataclysm had risen from the dragon’s tail to its head.

Why the Odin Guild had begun to grow around the time Cheon Taemin disappeared, and why Michael hadn’t shown his face even at Lee Jungryong’s funeral, attended by prominent figures from around the world.

There was only one reason.

“Magical power.”

Jin Taekyung slowly turned around. Looking into the gray eyes that no longer wavered, he continued.

“I don’t know how you did it or what gave you the chance, but… you were able to grow stronger by absorbing magical power. Just like a monster.”

At the same time, he’d contained mana within himself, perfectly controlled the balance between the two forces, and concealed them. That was why no one had been able to uncover what he really was.

Not even the Skeleton King.

Whenever the Skeleton King talked about Michael Silbert, he’d call him an “unpleasant human.” Even he, a monster, hadn’t been able to define exactly what made Michael so unpleasant.

If there was anyone in the world Michael Silbert feared more than anyone else, anyone whose eyes he had to avoid at all costs, it was just one person.

“Cheon Taemin. He would’ve seen right through you.”

And at the moment Jin Taekyung’s low voice reached everyone’s ears, someone’s dry lips parted, breaking the long silence.

“That’s why I had to live in hiding for so long. For nearly as long as you’ve been alive.”

More than thirty years had passed, but Michael Silbert still remembered it vividly.

It had been not long after he’d gained his new power.

Among the many people gathered in one place, the absolute being’s gaze had fixed on him—precisely on him. He still remembered the fear that had seized his entire body in that moment.

Back then, he’d possessed so little magical power that the man hadn’t looked his way again. But the fear he’d felt that day never truly went away.

Even after time had passed and Cheon Taemin had vanished. Even after Michael had learned the secrets of Zone A from Siegfried Bassman.

He hadn’t even attended Lee Jungryong’s funeral.

In case the information he had was wrong.

In case he ran into Cheon Taemin there—the one person who could see through him.

But…

“There’s one thing you’ve got wrong.”

In a low voice, Michael Silbert awakened the enormous power that lay dormant deep within him.

That unprecedented, turbulent power in which light and darkness had mingled for years—but which, from a certain day onward, had been stained a deeper and deeper shade by the swelling darkness.

“The only person in this world I fear isn’t here right now.”

*Rumble, rumble, rumble.*

A vast wave of force rose and pressed down on everything around them.
```

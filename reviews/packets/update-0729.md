<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0729.txt",
      "sha256": "729e29d4c17e7c28615d155f797d02e00bee271f4ec002e7456da1d66d38129a",
      "bytes": 12721
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "6b41936bdc2537f6f52c2e1dd5ea78065770fec5edb6ff106c766db7b424811b",
      "bytes": 1985
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "1694d1dfe8c2bd9048cb568ba4fc39178521d1f6c9fe3bc93a548feadc7b34aa",
      "bytes": 210051
    },
    {
      "path": "characters/Baek Hanseong.md",
      "sha256": "fce87333480d97c9420d12f6dee084180dc44e7a370e8518926587140291bac1",
      "bytes": 770
    },
    {
      "path": "characters/Cheon Taemin.md",
      "sha256": "905e364d8a40554237247dfc24b571c7ec0ba692056419828df8991882dd884c",
      "bytes": 752
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "be8dec81bdc053d551f2990dba95ee0d9d00c7ccd96689c7fbf0456169a69f81",
      "bytes": 553
    },
    {
      "path": "characters/Go Jun.md",
      "sha256": "5c817a73c7d010f936de19d11c50eb9bcb0b52716629d8d036e89e55671b4dbc",
      "bytes": 817
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "f7684e0473f1b446d6dd46321f670593e5d986c54b9798cfcc12d3507cea0ff2",
      "bytes": 2011
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "1ed8d86c379c08f60e74176a5d4cb33cfcc65cad70ce4178a5cf35c2f3c2d52e",
      "bytes": 622
    },
    {
      "path": "characters/Lee Jungryong.md",
      "sha256": "a3b07a4f2813b747a86c0ceef139c5a66ba357c73ec9f1a08de1e3035c2b21e9",
      "bytes": 1384
    },
    {
      "path": "characters/Team Leader Choi.md",
      "sha256": "5e05bc1152189dfe2d4d289912923127e65e29109aa66157b5a05ed8f7327646",
      "bytes": 967
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "f22d5c764493ff7be98ef9347cbb6480d02d0e6cef486298e891b0478e9b7de6",
      "bytes": 220759
    }
  ],
  "estimated_tokens": 11588
}
-->

# Durable State Update — Chapter 729

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 729. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 729. Profile updates may replace only one
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
  "chapter": 729,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 729,
    "continuity_sources": [729],
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
    "Jin Taekyung created the stable, beginner-accessible Smiling Mana Cultivation Method and intends to make it publicly available.",
    "The world's increasing mana is strengthening monsters and producing mutation Gates and monster waves.",
    "Jin suppressed rebel groups and terrorist organizations to reduce the danger of the cultivation method being misused.",
    "Major Guilds worldwide are watching Jin and Choi Minwoo, and invisible pressure has delayed Peace Guild's additional overseas expansion.",
    "Choi Minwoo is the Peace Guild Master and has taken control of the Ares Guild.",
    "Jin may reveal the Jin Family's Cultivation Technique if the situation worsens substantially.",
    "Jin, Choi, Im Kkeokjeong, Song Song, and the Skeleton King have committed to a dangerous initiative beyond Korea's domestic scale.",
    "Choi intends to involve President Baek Hanseong, while an unidentified infiltrator has stolen an unknown item from a government evidence storage room."
  ],
  "continuity_sources": [
    728
  ],
  "open_questions": [
    "How will the major Guilds respond when the Smiling Mana Cultivation Method is made public?",
    "Will Jin and Choi be able to release the method without provoking direct interference or retaliation?",
    "How much will public access to the method improve Hunters' ability to resist stronger monsters and mutation Gates?",
    "Will worsening conditions force Jin to reveal the Jin Family's Cultivation Technique as well?",
    "Who was the ghostlike infiltrator, and what item was stolen from the government evidence storage room?"
  ],
  "safe_through": 728,
  "temporary_decisions": [
    "Render 싱글벙글 마나 연공법 as The Smiling Mana Cultivation Method.",
    "Render 심판의 일주일 as The Week of Judgment.",
    "Render 구세주 코인 as the Savior coin.",
    "Preserve Jin's profane comic banter and Choi Minwoo's formal, controlled speech."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 최민우    | **Choi Minwoo**   |
| 천태민    | **Cheon Taemin**  |
| 이정룡    | **Lee Jungryong** |
| 심법     | **cultivation technique**                        | Especially internal cultivation                       |
| 상태               | **Status**                     |
| 레벨               | **Level**                      |
| 로그인              | **Login**                      |
| 헌터      | **Hunter**            |
| 길드      | **Guild**             |
| 길드장     | **Guild Master**      |
| 부길드장    | **Vice Guild Master** |
| 팀장      | **Team Leader**       |
| 대격변     | **Great Cataclysm**   |
| 백한성 | **Baek Hanseong** | Twenty-seventh President of Korea and youngest president elected in Korean history. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 고준 | **Go Jun** | Personal name of Team Leader Seok; Lee Jungryong's prized Disciple. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 아스모데우스 | **Asmodeus** | Demon King referenced in Taekyung's sarcastic comparison; does not appear directly. |
| 평화 | **Peace Guild** | Guild name. |
| 대한민국 | **Korea** | Country reference. |
| 아레스 | **Ares Guild** | The leading Guild in Korea; formerly employed Team Leader Choi and Song Song. |
| 자하신공 | **Zaha Divine Technique** | Huashan internal-energy technique used by Cheongpung. |
| 열화신공 | **Fire Gate Divine Technique** | Secret internal cultivation technique of the Fire Gate Clan, preserved through one-person succession without leakage. |
| 청와대 | **Blue House** | Presidential office mentioned in an online comment about proposed legislation. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 준이 | **Jun** | Family nickname used in the form Jun's dad. |
| 석고준 | **Go Jun** | Source full-name form for the established Go Jun, also known as Team Leader Seok. |
| 슬레이어 | **Slayer** | Cheon Taemin's title after killing the Demon King. |
| 마왕 | **Demon King** | The being Cheon Taemin killed. |
| 제로빅 | **Zerobic** | Name used in a forum joke about the recommended web novel. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 대통령 | **President** | Title for Korea's head of state. |
| 카카오페이지 | **KakaoPage** | Web-fiction platform mentioned by Jin. |
| 국장 | **national funeral** | State funeral reported for Lee Jungryong. |
| 성하 | **Seongha** | Hunter named during the cave battle. |
| 정룡 | **Jungryong** | Cheon Taemin's trusted associate who joined the Peace Guild. |
| 가기 | **singing courtesan** | The favored entertainer identity Honglan used in Hubei. |
| 화신 | **Fire God** | A local deity worshiped by one Nanman believer. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 이정룡 | 진태경 | senior S-rank Hunter to younger Hunter and adversary | Young man | polished, teasing, and veiled-threatening | Uses a genial tone and indirect threats while trying to make Taekyung release the captives. |
| 진태경 | 이정룡 | younger Hunter to senior S-rank Hunter and adversary | you | polite but mocking and defiant | Taekyung answers Lee's soft threats with the wolf-and-tiger metaphor and refuses to yield. |
| 이정룡 | 고준 | Master to Disciple | Go Jun | familiar and testing | Lee switches from Seok's office title to his personal name while considering whether he can defeat Taekyung. |
| 고준 | 이정룡 | Disciple to Master | Master | deferential | Go Jun responds to Lee's personal-name address as 스승님. |
| 이정룡 | 천태민 | younger_to_older_brother_by_choice | older brother | reverent and familiar; internal | Lee Jungryong uses 형님 in unspoken thoughts and regards Cheon Taemin as an older brother despite having no blood relation. |
| 석고준 | 최민우 | Ares security leader to rival Guild Master | Team Leader Choi Minwoo | formal but barbed | Uses 평화 길드 최민우 팀장님 while belittling Choi and blaming the Peace Guild for Taekyung's apparent death. |
| 진태경 | 석고준 | returning Hunter to hostile Ares security leader | you fucking bastard | hostile and profane | Taekyung directs his final insults and challenge at Go Jun after returning alive. |
| 석고준 | 진태경 | hostile_opponents | brat | hostile and overconfident | Go Jun addresses Taekyung internally as 애송아 while launching his full-strength attack. |
| 이정룡 | 백한성 | Ares authority to national head of state | Mr. President | formal-polite | Uses 대통령 각하 while greeting Baek Hanseong. |
| 백한성 | 이정룡 | President to Ares Guild Vice Guild Master | Vice Guild Master Lee | formal-polite | Uses 이정룡 부길드장님 while discussing the Chinese proposal. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 최민우 | 진태경 | trusted allied team leader to younger allied Hunter | Mr. Jin | formal-polite and concerned | Choi warns Jin about the danger of the operation and affirms his deep trust. |
| 진태경 | 최민우 | younger allied Hunter to allied team leader | Team Leader Choi | polite, familiar, and teasing | Jin jokes with Choi while acknowledging and dismissing his concern. |
| 진태경 | 엄마 | son_to_mother | Mom | casual and startled | Jin cries out to his mother as she charges at him during the hospital visit. |
| 고준 | 진태경 | Ares Guild combatant confronting the killer of his Master | you | hostile and informal | Go Jun uses 너 while demanding Jin confess to Lee Jungryong's death and threatening retaliation. |
| 진태경 | 고준 | dominant adversary confronting Lee Jungryong's Disciple | you | contemptuous and informal | Jin uses 너 and 놈 while overpowering Go Jun and ordering him to end the conflict with Lee Jungryong. |
| 진태경 | 대통령 | Hunter_to_President | Mr. President | formal-polite | Taekyung addresses the President respectfully during their airport greeting. |
| 대통령 | 진태경 | President_to_Hunter | Mr. Jin Taekyung | formal-polite | The President addresses Taekyung by name at the airport photo line. |
| 엄마 | 진태경 | mother_to_son | my son | warm and affectionate | Taekyung's mother praises him during the public welcome. |
| 백한성 | 최민우 | President_to_trusted_political_ally | Team Leader Choi | formal-polite, warm, and politically attentive | Baek addresses Choi as 최 팀장님 during the private Blue House breakfast. |
| 최민우 | 백한성 | political_subordinate_to_President | Mr. President | formal-polite | Choi addresses Baek as 대통령님 during the breakfast and departure. |

## Listed compact profiles

### Baek Hanseong.md

# Baek Hanseong (백한성)

- **Safe through:** Chapter 728
- **Aliases:** None
- **Role:** Twenty-seventh President of Korea and the youngest president elected in Korean history; leads the government's public response to the Mutated Gate crisis and supports Jin Taekyung in public appearances.
- **Personality:** Confident, politically shrewd, composed, and willing to needle Lee Jungryong while advancing his anti-Ares stance.
- **Voice:** Polite, self-assured, calm, and lightly teasing.
- **Relationships:** Political counterpart to Lee Jungryong who has established a cooperative relationship with Jin Taekyung and Choi Minwoo while seeking to restrain the power concentrated in their two Guilds.

### Cheon Taemin.md

# Cheon Taemin (천태민)

- **Safe through:** Chapter 727
- **Aliases:** Slayer; Sky (the American epithet used for him)
- **Role:** Cheon Taemin is Ares Guild Master and the world's greatest Hunter, known as the Slayer for killing the Demon King and creating the first Mana Cultivation Method during the Great Cataclysm, and he remains unconscious after more than twenty years in a wired mechanical capsule at his former mansion.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** Maternal grandfather of Team Leader Choi and Jin Taekyung and father of Soyeong; regarded by Lee Jungryong as an older brother despite their lack of blood relation.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 726
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Go Jun.md

# Go Jun (고준)

- **Safe through:** Chapter 611
- **Aliases:** Team Leader Seok
- **Role:** Go Jun was Ares Guild's Vice Guild Master, Lee Jungryong's Disciple and former Head of Security, the de facto successor to Lee's Ares legacy, and a mutated monster who was killed by Jin Taekyung in Area A.
- **Personality:** Disciplined and controlled under ordinary pressure, fiercely loyal to Lee Jungryong, but consumed by humiliation and rage when Ares Guild's authority is challenged.
- **Voice:** Dry, controlled, and formal with subordinates; deferential when addressing his Master.
- **Relationships:** Go Jun inherited Lee Jungryong's Ares legacy after becoming his Disciple and regarded Jin Taekyung and Choi Minwoo as enemies before his death.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 728
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple, the Fire Gate Clan's nineteenth successor, and the Pavilion Master of the Fire Dragon Pavilion within the Murim Alliance, a Supreme Peak master with the Heavenly Martial Physique and Force, a publicly recognized S-rank-level Hunter who formally retains an A-rank license, a traveler between Murim and another world resembling the realm of immortals, and the creator of the beginner-accessible Smiling Mana Cultivation Method.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate, trusted manager of media and official arrangements, and now the Peace Guild's Guild Master, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 728
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Lee Jungryong.md

# Lee Jungryong (이정룡)

- **Safe through:** Chapter 605
- **Aliases:** None
- **Role:** Former Vice Guild Master of Ares Guild, one of Korea's two S-rank Hunters, and a Supreme Peak-level martial artist who was killed by Jin Taekyung.
- **Personality:** Outwardly genial, calm, and humorous; calculating, opportunistic, manipulative, coercive, and ruthless when challenged
- **Voice:** Smooth, good-natured, and indirect, using teasing conversation and veiled threats before becoming openly furious
- **Relationships:** Master of Park Jihoon and Go Jun (Team Leader Seok), whom he personally selected and trained; longtime Great Cataclysm acquaintance of Park Tae Seop; adversary of Jin Taekyung; knew Team Leader Choi from childhood; has an antagonistic history with Kim Hwajong, who saved his life at the collapse of Mapo Bridge eighteen years earlier; was visibly shaken by learning that Choi is Cheon Taemin's maternal grandson; regarded Cheon Taemin as an older brother despite no blood relation and long held him in respect and fear; secretly supported the orphanage where Lee Dongseok grew up and was regarded by Dongseok as a father; operated as Ares Guild's senior authority beneath its Guild Master; concealed Taemin's condition with Song Cheonwoo and participated in purging aides who knew the truth.

### Team Leader Choi.md

# Team Leader Choi

- **Safe through:** Chapter 727
- **Aliases:** Choi Minwoo (최민우)
- **Role:** Team Leader Choi is Cheon Taemin's only living blood relative, a formidable aura-wielding swordsman who wields Hero's Soul, and the current Guild Master of the Peace Guild and Vice Guild Master of Ares Guild after a unanimous board vote.
- **Personality:** Strategic, candid, controlled, and possessive of the power and influence he intends to inherit.
- **Voice:** Dry, formal, and direct, with calm candor and carefully chosen metaphors.
- **Relationships:** Choi Minwoo is Cheon Taemin's maternal grandson and only living blood relative, was kept out of public knowledge by Lee Jungryong, is closely integrated with Jin Taekyung's family, seeks to acquire the Ares Guild intact, knows that Song Cheonwoo and Lee concealed Taemin's collapse and purged aides, and is Kim Hwajong's grandson.

## Korean source

```text
＃729화



나는 살면서 낚시를 해 본 적도 없고, 하는 법도 모른다.

하지만 어떻게 해야 더 많은 물고기를 잡을 수 있는지는 안다.

‘떡밥.’

그것이 우리가 해야 할 일이었다.

사방으로 중대 발표에 대한 떡밥을 뿌리고, 더 많은 물고기. 아니, 사람들의 관심과 주목을 최대한으로 끌어올리는 것.

물론 그 과정에서는 약간의 설득 역시 필요했다.

나와 최 팀장이 이번 낚시로 바라는 건 가져온 양동이를 가득 채우는 수준이 아니라, 넘쳐 흐를 정도의 만선(滿船)이었으니까.

그러나 만선의 꿈을 이루기 위해서는 훌륭한 선원들이 필요했고, 최 팀장이 가장 처음으로 연락한 백한성 대통령도 그중 한 사람이었다.

“예?”

불과 마흔을 갓 넘은 나이로 청와대에 입성하기까지 산전수전 다 겪었을 그는 마나 연공법이라는 단어에 눈을 부릅떴고, 뒤이어 흘러나온 한 사람의 이름에 커피를 엎질렀다.

“그, 그게 사실입니까? 정말 그분께서?”

“예. 제 외조부님께서 직접 창안하신 겁니다. 이 마나 연공법을 모두와 함께 나누시길 원하시더군요.”

“이, 이럴 수가.”

천태민이 누구인가.

살아 있는 구세주이자 인류 역사상 유일무이한 업적을 이룬 영웅.

마왕 아스모데우스를 쓰러트림으로써 대격변을 종식한 슬레이어(Slayer)의 이름 앞에서는 모두가 경의를 표할 수밖에 없었다.

“그런데 왜 마나 연공법 제목이 싱글벙글……?”

“……잘못 꺼냈군요. 지금 보신 건 잊어 주시기 바랍니다.”

까놓고 말해서, 내가 창안자로 알려진다면 마나 연공법 제목이 싱글벙글이건, 앗살라말라이쿰이건 상관없다.

하지만 천태민이라는 이름이 붙은 이상, [싱글벙글 마나 연공법]이라는 제목은 문제가 있다는 것이 나와 최 팀장의 공통된 의견이었다.

“이겁니다, 제 외조부께서 창안하신 마나 연공법이.”

최 팀장이 테이블 위에 올려놓은 것은 깔끔하게 제본된 책자였고, 겉면에는 마나 연공법의 새로운 이름이 적혀 있었다.

“천지심법(天地心法)…….”

“천지심법은 최하급 헌터도 익힐 수 있을 만큼 범용성이 넓고, 안정성 역시 매우 뛰어난 마나 연공법입니다. 익히는 즉시 엄청난 효과를 보기에는 어렵겠지만, 헌터들에게는 분명 큰 도움이 될 겁니다.”

당연히 그래야지. 그러라고 만든 건데.

물론 어른들의 사정으로 인해 이름이 바뀌긴 했지만, 새로운 이름 역시 내가 지은 거다.

나는 약간의 뿌듯함을 느끼며 한마디를 보탰다.

“한마디로, 개 지리는 마나 연공법이라는 거죠.”

최 팀장이 헛기침으로 눈치를 줬지만, 백한성 대통령은 신경 쓰지 않았다.

아니, 신경을 쓸 겨를조차 없어 보였다는 것이 옳은 표현이었다.

그는 홀린 듯이 천지심법의 묘리가 담긴 책자를 바라보다가, 한참이 흐른 뒤에야 뒤늦게 정신을 차렸다.

“그, 그런데 왜 이런 중요한 물건을 굳이 제게…….”

“조력자가 필요합니다.”

봉황 의자는 오이마켓에서 중고 거래로 산 게 아니다.

백한성 대통령은 나와 최 팀장이 자신을 찾아온 이유를 곧장 알아차렸다.

“방파제를 원하시는군요.”

“단지 서로에게 힘이 되었으면 하는 바람뿐입니다.”

“하지만 어떤 거대 길드가 나선다 해도, 그분께서 계시는 한은 어려울 텐데요.”

정확한 판단이다.

단, 사실이라는 가정하에.

‘하지만 안타깝게도 사실이 아니지.’

최대한 외부의 견제를 피한다.

그것이 의식불명 상태에 빠져 있는 천태민의 이름까지 팔아서 싱글벙글, 아니 천지심법을 공개하려는 이유였고, 최 팀장은 우리에게 매우 우호적인 태도를 보여 왔던 백한성 대통령에게도 진실을 이야기할 생각이 없었다.

그 역시 결국 정치인이었으니까.

“저는 물론, 외조부님께서는 어떤 충돌이나 잡음도 원치 않습니다. 그러기 위해서는 정부의 협력이 필요하고요.”

“그 말씀은, 이 마나 연공법의 존재에 관하여 청와대에서 직접 발표해도 된다는 뜻입니까?”

최 팀장이 고개를 저었다.

“양측 간의 협력이 있었고, 이틀 뒤 중대 발표가 있으리라는 것 정도면 충분할 듯싶습니다. 그것만으로도 세간의 이목이 쏠릴 테니까요.”

“바람잡이라…….”

“이번 마나 연공법 발표는 일종의 국책(國策) 사업이라고 알려질 겁니다. 그렇게 된다면 국가적으로도 위상이 올라가겠지요.”

“음.”

지금껏 유례없었던 마나 연공법의 공공화. 그리고 이 역사적인 사건에 항상 따라붙을 대한민국이라는 네 글자와 대통령의 업적.

잠시 후, 백한성 대통령의 입가에 희미한 미소가 떠올랐다.

“오늘따라, 저 태극기가 참 보기 좋군요.”

누가 그랬다.

세상에서 가장 강력한 마약은 국뽕이라고.

펄-럭.



* * *



천태민. 마나 연공법 공공화. 국책 사업.

이 세 가지 키워드는 숯불 위의 가마솥처럼 끓어올랐고, 그 발화점(發火點)은 바로 대한민국이었다.

- 사랑하고 존경하는 국민 여러분. 저는 오늘, 한 가지 중대 발표를 위하여 이 자리에 섰습니다…….

백한성 대통령은 적극적으로 협력하겠다는 약속을 긴급 청와대 공식 회견으로 보여 주었다.

외신을 포함한 수많은 기자와 카메라 앞에서 열변을 토하는 그의 모습은 TV로 생중계됐고, 이내 전 세계로 송출되면서 엄청난 파란을 일으켰다.



[마나 연공법 공공화. 사상 초유!]

[인류의 구세주, 다시 한번 세상을 구하다!]

[살아 있는 전설, 마침내 모습을 드러내나?]



오랫동안 모습을 감추었던 천태민의 이름이 거론된 것으로도 충분히 기삿거리인데, 그가 창안한 마나 연공법이 전 세계에 공개된다니. 그 반응은 가히 폭발적이었다.

아니, 언론은 이미 폭발해 버렸다.

“야! 박 기자! 평화 길드! 평화 길드 연락해 봐!”

“그, 그게. 저도 당연히 연락해 봤는데 찔러도 나오는 게 없습니다.”

“그럼 아레스는? 거기에 줄 대놓은 거 없어? 그쪽에서 몇 번 소스 얻어 온 적 있잖아!”

“그 사람 지금 구치소에 있는데요. 그 왜, 얼마 전에 석고준 사건에 연루되는 바람에…….”

“미치겠네. 최민우 쪽은?”

“어휴. 말도 마세요. 선 대는 것 자체도 불가능에 가깝고, 거긴 찔러 봤자 피 한 방울 안 나옵니다.”

“그럼 진태경은?”

“……걔는 건드리면 제가 피 보죠. 국장님. 저 맞아 죽는 거 보고 싶으세요?”

누가 흘렸는지 모를 소스는 곳곳에서 흘러나오는데, 먼저 접선해 오지 않는 이상 알 도리가 없다.

미치고 팔짝 뛰기 직전인 언론은 그저 어뷰징 기사를 양산할 수밖에 없었고, 인터넷 안에서의 상황은 그보다 더했다.



현재 상황 세줄 요약



1. 천태민이 마나 연공법 만듦.

2. 외손자랑 개쩌는 후배가 공공화 추진. 정부가 숟가락 얹음.

3. 애초에 마나 연공법이 뭔지도 모르는 헌터들도 있었을 텐데, 천태민이 만든 건 범용성이 지려서 최하급 헌터도 익힐 수 있음.

와! 다 함께 레벨 업!



4. 세줄 요약 아님.

└ (작성자) 뭔 개소리야. 깔끔하게 정리해 놨는데.

└ 카카오페이지 뷰어로 보면 세줄 요약 아님.

└ (작성자) 미친 새끼네 이거.



마나 연공법 공공화 ㄷㄷ

└ 글쓴이 천태민 ㄷㄷㄷ

└ 엮은이 진태경 ㄷㄷㄷㄷ

└ 엮은이는 김경식 아니냐.

└ ? 김경식은 누구.

└ 여기도 지진 났네ㅋㅋㅋㅋㅋㅋ

└ 이건 지진 나도 ㅆㅇㅈ. 청와대 공식 회견 보면서 우리 길드 사람들 다 지렸음.



일반인이라서 잘 모르는데, 마나 연공법이 정확히 뭐예요?

└ 쉽게 말하면 극소수만 익힐 수 있는 비전 같은 거임. 무협 소설에 나오는 자하신공이나 열화신공 같은 거. 그런 거 원래 지들끼리만 아는 건데, 그런 거 쌩 까고 걍 전체 공개하겠다는 거 ㅇㅇ

└ 무협 소설 안 봐서 몰라요.

└ ㅇㅋ그럼 음식 레시피 같은 거라고 이해하면 쉬움. 미슐랭 식당 같은 곳에서만 파는 음식들이 다 특정 레시피가 있잖아.

└ 미슐랭이 뭐예요?

└ ㅋㅋ....그럼 어머니들이 꼭 하나씩 갖고 있는 요리 비법 같은 거.

└ 우리 엄마 요리 엄청 못해요. 맛없게 만드는 비법만 아는 것 같아요.

└ 야. 너 몇 살이냐?

└ 아홉 살이요.

└ ㅅㅂ 속 시원하게 욕도 못 하겠네.

└ 팩트) 아홉 살짜리한테 매우 시원하게 욕 갈김.

└ 꺼져ㅅㅂ

└ 나 무협 애독잔데 열화신공은 뭐냐. 자하신공은 앎.

└ ?로그인 무림 안 봄?

└ 제로빅 어서 오고.

└ 걔 작년 추석 때 쉬었더라. 제로빅이 아니라 호로빅임.



언제나 두 갈래로 나뉘어 갑론을박으로 잠잠할 틈이 없던 누리꾼들이었지만, 마나 연공법 공공화에 관련된 기사에는 모두가 한마음 한뜻으로 찬사를 보냈다.

남들은 갖고 있으면서도 온 힘을 다해 숨기는 비전을, 그것도 아무런 제약도 없이 공개한다고 한다.

단지 모두를 위한다는 마음 하나만으로.

사람들에게 있어 마나 연공법 공공화는 헌터만을 위한 일이 아니었다.

헌터들이 강해진다면 최근 들어 잇따라 벌어지는 불안한 사건들을 더욱 신속하게 진압할 수 있고, 이는 곧 일반인들이 훨씬 더 안전해진다는 뜻이기도 했다.

물론, 그것과는 별개로 서운함을 감추지 못하는 이들 역시 있었다.

“음.”

“저희에게 미리 언질이라도 해 주셨다면 좋았을 텐데요.”

아레스 길드.

급변하는 내부 상황 속에도 살아남은 내부 임원들의 조심스러운 항의에, 최민우는 가볍게 고개를 숙였다.

“미리 말씀드리지 못해 죄송합니다. 하지만 정보가 흘러나가기 전에 빨리 처리하는 게 옳다고 생각했습니다.”

젊고 능력 있는 신임 부 길드장의 사과에, 임원들은 서로의 눈치를 살폈다.

저쪽에서 먼저 잘못을 인정하고 사과를 했으니 명분은 갖춰줬다. 두 번 다시 독단할 수 없도록 어느 정도 기를 죽여야 하는 타이밍이다.

하지만 문제는, 저 젊다 못해 새파란 부길드장이 가진 무시무시한 정통성에 있었다.

‘그분께서 직접 나서시다니.’

‘난 얼굴조차 한 번도 못 뵀는데.’

‘외손자를 그만큼 아끼신다는 건가?’

천태민은 그만큼 오랜 기간 모두의 앞에 모습을 드러내지 않았다.

심지어 외부에서 영입된 몇몇 임원은 아레스 길드에 입사한 이후에도 길드장인 그를 마주한 적이 없었고, 상당한 연차의 임원들 역시 이정룡의 장례식 이후 어렴풋이 의심을 품고 있었다.

‘길드장님께 문제가 생겼다.’

합리적인 의심.

의형제나 다름없던 이정룡의 장례식 때도 모습을 드러내지 않던 천태민이다.

당신의 외손자가 이정룡에 의해 사실상 유배나 다름없이 해외 지사를 전전할 때도 나서지 않던 분이 아니었나.

그러나…… 이제는 상황이 달라졌다.

아니, 여전히 마음 한구석에 의심이 남아 있다 해도 티를 내는 건 멍청하기 그지없는 짓이다.

그들에게 있어 천태민이라는 이름은 여전히 경의(敬意) 그 자체였고, 저 새파란 부길드장이 가진 필승 카드는 자신의 외조부뿐만이 아니었으니까.

“다들 조용하시네.”

정적을 깨트리는 나직한 목소리. 스마트폰으로 웹툰을 보고 있던 진태경이 말을 이었다.

“사람이 뭐라고 사과를 하면, 뭐라고 대답들을 하셔야 맞는 건데.”

“……!”

“안 그래요?”

파르르 떨리는 수십 쌍의 눈동자와 일렁이는 목울대.

서로의 눈치를 살피던 임원들이 억지웃음을 지으며 고개를 숙인 그때였다.
```

## Final English reading copy

```markdown
# Chapter 729

I had never gone fishing in my life, and I didn’t know how to do it.

But I did know how to catch more fish.

*Bait.*

That was what we needed.

Scatter bait about the major announcement in every direction and draw in as much interest and attention from as many fish—or rather, people—as possible.

Of course, the process required a little persuasion, too.

Team Leader Choi and I weren’t aiming merely to fill the bucket we’d brought. We wanted a boatload so enormous it would spill over.

But to make that dream a reality, we needed excellent sailors, and the first person Team Leader Choi contacted was President Baek Hanseong.

“Pardon?”

He had gone through every kind of hardship before entering the Blue House at the age of just over forty. His eyes widened at the words *Mana Cultivation Method*, and when the name of one particular person followed, he spilled his coffee.

“I-Is that true? Did he really…?”

“Yes. My maternal grandfather created it himself. He wanted to share this Mana Cultivation Method with everyone.”

“H-How can this be?”

Who was Cheon Taemin?

A living Savior and a hero who had accomplished something unmatched in human history.

Everyone had no choice but to show respect before the name of the Slayer—the man who had defeated the Demon King Asmodeus and brought the Great Cataclysm to an end.

“But why is the Mana Cultivation Method called *Smiling*…?”

“……I took out the wrong one. Please forget what you just saw.”

To be perfectly honest, if I became known as its creator, I wouldn’t care whether the Mana Cultivation Method was called *Smiling* or *As-Salamu Alaykum*.

But since the name Cheon Taemin was attached to it, Team Leader Choi and I agreed that *The Smiling Mana Cultivation Method* was a problem.

“This is the Mana Cultivation Method my maternal grandfather created.”

What Team Leader Choi placed on the table was a neatly bound booklet. Its cover bore the Mana Cultivation Method’s new name.

“*Heaven and Earth Cultivation Technique*……”

“The Heaven and Earth Cultivation Technique is versatile enough for even the lowest-ranking Hunter to learn, and it is also exceptionally safe. It may be difficult to see tremendous effects immediately after learning it, but it will certainly be of great help to Hunters.”

Of course it would. That was what I had made it for.

The name had changed because of adult circumstances, but I had come up with the new name, too.

Feeling a little proud, I added:

“In short, it’s a fucking incredible Mana Cultivation Method.”

Team Leader Choi gave me a pointed cough, but President Baek Hanseong didn’t pay any attention.

No, it would be more accurate to say that he didn’t even have the time to pay attention.

He stared as though possessed at the booklet containing the principles of the Heaven and Earth Cultivation Technique. Only after a long while did he finally come to his senses.

“But why would you bring something this important to me…?”

“We need an ally.”

The phoenix chair wasn’t something President Baek Hanseong had bought used on Oi Market.

He immediately realized why Team Leader Choi and I had come to see him.

“You want a breakwater.”

“We only hope that we can be of strength to each other.”

“But no matter how large a Guild steps forward, it will be difficult as long as he is still here.”

It was an accurate assessment.

Assuming it was true.

*Unfortunately, it isn’t.*

Avoiding interference from outside as much as possible.

That was why we were planning to reveal the Smiling—or rather, the Heaven and Earth Cultivation Technique while borrowing the name of the unconscious Cheon Taemin. Team Leader Choi had no intention of telling the truth even to President Baek Hanseong, who had always shown us a very favorable attitude.

He was a politician, after all.

“Neither I nor my maternal grandfather want any conflict or controversy. To prevent that, we need the government’s cooperation.”

“Are you saying that the Blue House may directly announce the existence of this Mana Cultivation Method?”

Team Leader Choi shook his head.

“It should be enough to announce that there has been cooperation between both sides and that a major announcement will be made in two days. That alone will draw the public’s attention.”

“So you want me to drum up interest……”

“This Mana Cultivation Method’s release will be announced as a sort of national project. If that happens, Korea’s standing will rise as well.”

“Hmm.”

The unprecedented public release of a Mana Cultivation Method. And the name Korea, which would forever accompany this historic event, along with the President’s achievement.

A faint smile appeared around President Baek Hanseong’s lips.

“That Korean flag looks especially beautiful today.”

Someone once said that the most powerful drug in the world was a patriotic high.

*Flap—*

* * *

Cheon Taemin. The public release of the Mana Cultivation Method. A national project.

Those three keywords boiled like a cauldron over charcoal, and their ignition point was none other than Korea.

> “My beloved and respected citizens. I stand before you today to make one major announcement……”

President Baek Hanseong demonstrated his promise to cooperate fully with an emergency official Blue House press conference.

His passionate speech before countless reporters and cameras, including foreign press, was broadcast live on television. Before long, it was transmitted across the world and caused an enormous upheaval.

> [The Mana Cultivation Method Made Public—An Unprecedented Event!]

> [The Savior of Humanity Saves the World Once Again!]

> [The Living Legend Finally Preparing to Reveal Himself?]

The mere mention of Cheon Taemin, who had stayed out of the public eye for so long, was already enough to make headlines. And now the Mana Cultivation Method he had created was going to be revealed to the entire world.

The response was explosive.

No, the media had already exploded.

“Hey! Reporter Park! Peace Guild! Contact the Peace Guild!”

“I-I did, of course, but nothing comes out no matter how much I poke around.”

“Then what about Ares? Don’t you have anyone you can lean on there? We’ve gotten a few sources from them before!”

“That person is in the detention center right now. You know, because he got caught up in the Go Jun incident a while back……”

“This is driving me crazy. What about Choi Minwoo?”

“Oh, don’t even ask. Getting a line into them is practically impossible, and you couldn’t get a single drop of blood out of them even if you poked them.”

“Then what about Jin Taekyung?”

“……If I touch him, I’m the one who’ll bleed. Chief, do you want to watch me get beaten to death?”

Sources of unknown origin were leaking out everywhere, but unless they made contact first, there was no way to figure out who had leaked them.

The media, driven almost to the point of madness, could do nothing but churn out clickbait articles. The situation on the internet was even worse.

> **Three-Line Summary of the Current Situation**
>
> 1. Cheon Taemin created a Mana Cultivation Method.
>
> 2. His grandson and an insanely badass junior are pushing to make it public. The government is jumping on the bandwagon.
>
> 3. There must have been Hunters who didn’t even know what a Mana Cultivation Method was, but the one Cheon Taemin created is so damn versatile that even the lowest-ranking Hunters can learn it.
>
> Wow! Level up together!

> **4. This isn’t a three-line summary.**
>
> └ **Author:** What the fuck are you talking about? I organized it neatly.
>
> └ It’s not a three-line summary when you look at it through the KakaoPage viewer.
>
> └ **Author:** You crazy bastard.

> **The Mana Cultivation Method is going public?!**
>
> └ Written by Cheon Taemin?!
>
> └ Edited by Jin Taekyung?!?!
>
> └ Wasn’t the editor Kim Gyeongsik?
>
> └ ? Who’s Kim Gyeongsik?
>
> └ The site’s shaking here too, lol.
>
> └ This one totally deserves an earthquake. Everyone in our Guild pissed themselves watching the official Blue House press conference.

> **I’m a civilian, so I don’t really know, but what exactly is a Mana Cultivation Method?**
>
> └ To put it simply, it’s a secret technique that only a tiny number of people can learn. Like the Zaha Divine Technique or the Fire Gate Divine Technique from wuxia novels. Those things are normally kept within their own circles, but this guy is saying screw that and making it available to everyone, yeah.
>
> └ I don’t read wuxia novels, so I don’t know.
>
> └ Okay, then think of it like a food recipe. Restaurants with Michelin stars all have their own recipes for the food they sell, right?
>
> └ What’s Michelin?
>
> └ LOL…… Then think of it as the sort of cooking secret every mother has.
>
> └ My mom is a terrible cook. I think she only knows the secret to making food taste bad.
>
> └ Hey. How old are you?
>
> └ Nine.
>
> └ Fuck, now I can’t even properly swear at you.
>
> └ **Fact:** Curses very refreshingly at a nine-year-old.
>
> └ Fuck off.
>
> └ I’m an avid wuxia reader, but what’s the Fire Gate Divine Technique? I know the Zaha Divine Technique.
>
> └ ? You don’t read *Login Murim*?
>
> └ Zerobic, welcome.
>
> └ He took a break over the harvest festival last year. Not Zerobic—Bastardbic.

Netizens were always divided into two camps and never stopped arguing, but when it came to articles about making the Mana Cultivation Method public, they all spoke with one voice and offered nothing but praise.

Someone was going to reveal a secret technique that others possessed but hid with all their might—and reveal it without any restrictions.

Simply out of a desire to help everyone.

For people, the public release of the Mana Cultivation Method was not something meant only for Hunters.

If Hunters became stronger, they could suppress the unsettling incidents occurring one after another much more quickly. That also meant ordinary people would become much safer.

Of course, there were also people who couldn’t hide their disappointment for an entirely different reason.

“Hmm.”

“It would have been nice if you had given us some advance notice.”

Ares Guild.

In response to the cautious complaints of the internal executives who had survived despite the rapidly changing situation within the Guild, Choi Minwoo lowered his head slightly.

“I’m sorry I couldn’t tell you beforehand. But I thought it would be better to handle things quickly before the information leaked.”

Faced with the apology from the young and capable new Vice Guild Master, the executives glanced at one another.

He had admitted his mistake and apologized first, giving them the justification they needed. This was the right time to put him in his place to ensure he would never act unilaterally again.

But the problem was the terrifying legitimacy possessed by that Vice Guild Master who was young—no, barely more than a boy.

*He actually stepped forward himself.*

*I’ve never even seen his face.*

*Does he care about his grandson that much?*

Cheon Taemin had not shown himself before everyone for an incredibly long time.

Some executives recruited from outside had never even encountered their Guild Master after joining Ares Guild, while even executives with considerable seniority had begun harboring vague suspicions after Lee Jungryong’s funeral.

*Something happened to the Guild Master.*

It was a reasonable suspicion.

Cheon Taemin had not appeared even at Lee Jungryong’s funeral, though the two had been practically sworn brothers.

Hadn’t he also refused to intervene when his grandson was sent from one overseas branch to another, practically exiled by Lee Jungryong?

But……things were different now.

No, even if they still harbored doubts in some corner of their minds, revealing them would be unbelievably foolish.

To them, the name Cheon Taemin was still the embodiment of reverence. And the fresh-faced Vice Guild Master’s winning card was not only his grandfather.

“You’re all awfully quiet.”

A low voice broke the silence. Jin Taekyung, who had been watching a webtoon on his smartphone, continued:

“When someone apologizes to you, aren’t you supposed to say something in response?”

“……!”

“Isn’t that right?”

Dozens of pairs of eyes trembled, and throats bobbed nervously.

The executives exchanged glances. Then, just as they bowed their heads with forced smiles—it happened.
```

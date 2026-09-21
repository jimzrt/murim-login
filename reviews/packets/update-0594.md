<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0594.txt",
      "sha256": "4387573dd5ce5540646e452c185e542333fdc58aa6bff5db368b5725260444a1",
      "bytes": 15769
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "cde690a83a73c045ef23d44923d64f57fd39d9c0c52adaba6c99b4ab6c66d970",
      "bytes": 2987
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "1f3f9a4fe0c44b77815f04264b579ba303ec1dde49f21a7096d1a65671caf400",
      "bytes": 185103
    },
    {
      "path": "characters/Cheon Taemin.md",
      "sha256": "6eaeb68abb19e874c78a16922e0c56998ffe87e509a884c9763a8538640bac22",
      "bytes": 730
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "55d7c92d64ca25622810832960724f189d8191334b593e650ec1d14ffc366a48",
      "bytes": 553
    },
    {
      "path": "characters/Go Jun.md",
      "sha256": "f098e8451f11ac8e117693abf1b04676e40dc9583dafc027bf2b31f6761fc60a",
      "bytes": 893
    },
    {
      "path": "characters/Hwa-jong.md",
      "sha256": "ade51bdcad342284fcacd0e0048bcd89f5877a470185b824118caf911a1a5b90",
      "bytes": 646
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "63936977e8eb822c35c78b644d7bc2726051fd7a80725191b4102126e049881f",
      "bytes": 2315
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "4ef8686f514f38b27be968e7167a710ffdaadb1a7f94de3e9b60e0a96ee6159b",
      "bytes": 622
    },
    {
      "path": "characters/Kim Hwajong.md",
      "sha256": "27443ad65de34ddd532713ca5f2463d4e88fd6a1d0f888bc8664770c4fdc1e50",
      "bytes": 694
    },
    {
      "path": "characters/Lee Jungryong.md",
      "sha256": "0ee490ad951a025f9a1f38efa9a5e6f4d295fd0254aab7bde6680d353c3f2551",
      "bytes": 1384
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "61ef24047780dd8c8c21961c6c1395fd6b17ffe5fa8a5aeb489fa4744575956d",
      "bytes": 182490
    }
  ],
  "estimated_tokens": 12530
}
-->

# Durable State Update — Chapter 594

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 594. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 594. Profile updates may replace only one
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
  "chapter": 594,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 594,
    "continuity_sources": [594],
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
    "Kim Hwajong died after sacrificing himself to restrain Behemoth, and Choi Minwoo remains unconscious after being transported from the battlefield.",
    "Behemoth's Turbid Abyss is a Supreme Peak Magic Gem that absorbed another source of mana and requires purification before use.",
    "Jin has devastated Ares Guild headquarters, incapacitated its elite defenders, triggered an internal revolt, and entered concealed Area A while pursuing Go Jun.",
    "Go Jun is Lee Jungryong's Disciple and direct protégé; Lee found him among the war orphans and recognized him as special.",
    "Go Jun remained in Area A and absorbed immense power from an S-grade Magic Gem, which now manifests as demonic energy.",
    "Go Se-won openly opposed Go Jun's crimes, intended to resign, revealed Area A, and has a pregnant wife and a four-year-old child.",
    "Cheon Taemin collapsed more than twenty years ago and remains unconscious at an unknown location, with Area A only suspected.",
    "Song Cheonwoo and Lee Jungryong concealed Taemin's condition and purged those who knew the truth.",
    "Busan's Kraken is dead, but more than one thousand Mermen remain across Haeundae and Gwangalli.",
    "Go Jun seized Song Cheonwoo's children, used an S-grade Magic Gem to cause the Busan Monster Wave, and targeted Choi Minwoo.",
    "Song Cheonwoo was killed by an unidentified monster after falling into an abyss; the object in his pocket released darkness that became light.",
    "Go Jun is impaled by White Flame inside Area A, while Jin has blocked his counterattack with Fire Dragon Armor and continues the fight."
  ],
  "continuity_sources": [
    593
  ],
  "open_questions": [
    "What caused Cheon Taemin's collapse, and what happened during his more than twenty years of unconsciousness?",
    "Is Cheon Taemin actually being kept in Area A of Ares Guild headquarters?",
    "What is inside Area A, and what is the unidentified being involved in Go Jun's plan?",
    "What was the object Song Cheonwoo kept in his pocket, and what did its release of darkness and light accomplish?",
    "What is the black jewel in Go Jun's necklace, and what function does it serve?"
  ],
  "safe_through": 593,
  "temporary_decisions": [
    "Use Area A for A구역, White Flame for 백염, Flamefire Path for 염화일로, Tower Shield for 타워 실드, and hellfire for 겁화.",
    "Use Scorching Yang Qi for 열양지기 and Force for 강기; distinguish Sword Energy from Aura when the source contrasts them, and use Aura Blade for 오러 블레이드.",
    "Use Seizing an Object Through Empty Space for 허공섭물, Flame Divine Palm for 화염신장, Finger Qi for 지풍, and grappling technique for 금나수.",
    "Use hunting dog for 사냥개 and impregnable fortress for 철옹성.",
    "Use Executive Director for 전무 and Managing Director for 상무 in Ares Guild's executive hierarchy; render 마력 as demonic energy."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 김화종    | **Kim Hwajong**   |
| 천태민    | **Cheon Taemin**  |
| 이정룡    | **Lee Jungryong** |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 제자     | **Disciple**                                 |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 길드      | **Guild**             |
| 마정석     | **Magic Gem**         |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 고준 | **Go Jun** | Personal name of Team Leader Seok; Lee Jungryong's prized Disciple. |
| 화종 | **Hwa-jong** | Butler Kim's personal name. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 하연 | **Hayeon** | Jin Taekyung’s younger sister |
| 화염신장 | **Flame Divine Palm** | Jopil's deadly palm technique, noted when Taekyung compares Jopil with Mukyung. |
| 평화 | **Peace Guild** | Guild name. |
| 아레스 | **Ares Guild** | The leading Guild in Korea; formerly employed Team Leader Choi and Song Song. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 트롤 | **Troll** | Monster species with extraordinary regenerative ability. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 준이 | **Jun** | Family nickname used in the form Jun's dad. |
| 석고준 | **Go Jun** | Source full-name form for the established Go Jun, also known as Team Leader Seok. |
| 광안 | **Guang'an** | Sichuan location where the party boards Mu Song's ship. |
| 광안대교 | **Gwangan Bridge** | Busan suspension bridge central to Taekyung's childhood memory and the current disaster. |
| 정룡 | **Jungryong** | Cheon Taemin's trusted associate who joined the Peace Guild. |
| 철옹성 | **impregnable fortress** | Metaphor for Ares Guild's entrenched defenses. |
| 효웅 | **ambitious warlord** | Archetype used for Lee Jungryong as a ruthless, ambitious ruler. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 하연 | 진태경 | younger_sister_to_older_brother | oppa | casual-familiar; pleading for important requests | Hayeon habitually puts 오빠 first when making an important request. |
| 진태경 | 하연 | older_brother_to_younger_sister | Sis | casual-familiar | Taekyung addresses Hayeon as 동생아 during their fly investigation. |
| 김화종 | 진태경 | senior_Hunter_to_younger_Hunter | Mr. Jin | formal-polite | Hwajong addresses Taekyung as 진태경 씨 while proposing an exchange of stories. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 이정룡 | 진태경 | senior S-rank Hunter to younger Hunter and adversary | Young man | polished, teasing, and veiled-threatening | Uses a genial tone and indirect threats while trying to make Taekyung release the captives. |
| 진태경 | 이정룡 | younger Hunter to senior S-rank Hunter and adversary | you | polite but mocking and defiant | Taekyung answers Lee's soft threats with the wolf-and-tiger metaphor and refuses to yield. |
| 이정룡 | 고준 | Master to Disciple | Go Jun | familiar and testing | Lee switches from Seok's office title to his personal name while considering whether he can defeat Taekyung. |
| 고준 | 이정룡 | Disciple to Master | Master | deferential | Go Jun responds to Lee's personal-name address as 스승님. |
| 이정룡 | 천태민 | younger_to_older_brother_by_choice | older brother | reverent and familiar; internal | Lee Jungryong uses 형님 in unspoken thoughts and regards Cheon Taemin as an older brother despite having no blood relation. |
| 진태경 | 석고준 | returning Hunter to hostile Ares security leader | you fucking bastard | hostile and profane | Taekyung directs his final insults and challenge at Go Jun after returning alive. |
| 석고준 | 진태경 | hostile_opponents | brat | hostile and overconfident | Go Jun addresses Taekyung internally as 애송아 while launching his full-strength attack. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 고준 | 진태경 | Ares Guild combatant confronting the killer of his Master | you | hostile and informal | Go Jun uses 너 while demanding Jin confess to Lee Jungryong's death and threatening retaliation. |
| 진태경 | 고준 | dominant adversary confronting Lee Jungryong's Disciple | you | contemptuous and informal | Jin uses 너 and 놈 while overpowering Go Jun and ordering him to end the conflict with Lee Jungryong. |
| 김화종 | 천태민 | loyal subordinate and trusted comrade to Guild Master | Guild Master | formal and respectful | Kim addresses Taemin as 길드장님 after joining the Peace Guild. |
| 길드원 | 진태경 | Peace Guild member to allied S-rank Hunter | Hunter Jin Taekyung | formal-polite and hesitant | A Guild member addresses Taekyung as 진태경 헌터님 while asking whether Choi should be awakened. |

## Listed compact profiles

### Cheon Taemin.md

# Cheon Taemin (천태민)

- **Safe through:** Chapter 587
- **Aliases:** Slayer
- **Role:** Cheon Taemin is Ares Guild Master and the world's greatest Hunter, known as the Slayer for killing the Demon King and creating the first Mana Cultivation Method during the Great Cataclysm, and he is believed to remain alive after more than twenty years of unconsciousness, with Area A only suspected as his location.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** Maternal grandfather of Team Leader Choi and Jin Taekyung and father of Soyeong; regarded by Lee Jungryong as an older brother despite their lack of blood relation.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 593
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Go Jun.md

# Go Jun (고준)

- **Safe through:** Chapter 593
- **Aliases:** Team Leader Seok
- **Role:** Go Jun is Ares Guild's Vice Guild Master, Lee Jungryong's disciple and former Head of Security, the de facto successor to Lee's Ares legacy, and the fugitive occupant of the concealed Area A.
- **Personality:** Disciplined and controlled under ordinary pressure, fiercely loyal to Lee Jungryong, but consumed by humiliation and rage when Ares Guild's authority is challenged.
- **Voice:** Dry, controlled, and formal with subordinates; deferential when addressing his Master.
- **Relationships:** Go Jun inherited Lee Jungryong's Ares legacy after becoming his Disciple, regards Jin Taekyung and Choi Minwoo as enemies, and now threatens Jin's family and Peace Guild allies while wielding power absorbed from an S-grade Magic Gem.

### Hwa-jong.md

# Hwa-jong (화종)

- **Safe through:** Chapter 593
- **Aliases:** Butler Kim
- **Role:** Hwa-jong was Choi Minwoo's loyal butler and personal escort who sacrificed his life to restrain Behemoth and died after Jin Taekyung killed it.
- **Personality:** Loyal, vigilant, and uncompromising toward perceived threats to Choi Minwoo.
- **Voice:** Formal and deferential toward Choi Minwoo, cold and openly hostile toward Song Cheonwoo.
- **Relationships:** Hwa-jong serves Choi Minwoo and was formerly close to Song Cheonwoo, but their relationship ended over loyalty and ambition.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 593
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, a Supreme Peak master who possesses the Heavenly Martial Physique and superhuman physical strength, has manifested Force, opened his Middle Dantian, crossed the wall into true mastery, has achieved Three Flowers Gather at the Crown but not Five Qi Returning to Origin, can perceive the texture of qi well enough to sever layered magic, can resist high-level monster Fear through exceptional mental strength, is publicly recognized as an S-rank-level Hunter while formally retaining an A-rank license pending testing, can command coordinated raids against powerful monsters, serves as one of the two pavilion masters of the Alliance Leader's direct Fire Dragon Pavilion, leads its first mission to Nanman, has withdrawn from the Peace Guild, and has entered Ares Guild headquarters to confront Go Jun.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor and assigned him a final task to incorporate martial principles into his learned martial arts but declined Taekyung's recruitment after Cheongpung reached him first, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate, student, and trusted manager of media and official arrangements, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, and Xiao Shen regards him as an older brother after Jin saved him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 593
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Kim Hwajong.md

# Kim Hwajong (김화종)

- **Safe through:** Chapter 593
- **Aliases:** Butler Kim
- **Role:** Kim Hwajong was a Level 80 mage known as Butler Kim and Choi Minwoo's loyal butler and personal escort who sacrificed his life to restrain Behemoth and died after Jin Taekyung killed it.
- **Personality:** Gentle and composed as Butler Kim, but retains a fiery temperament and a habit of swearing.
- **Voice:** Gentle and measured
- **Relationships:** Kim Hwajong formerly instructed Im Chunsoo, who remains terrified of and obedient to him, and serves Choi Minwoo as butler and personal escort, having become Choi's only family.

### Lee Jungryong.md

# Lee Jungryong (이정룡)

- **Safe through:** Chapter 592
- **Aliases:** None
- **Role:** Former Vice Guild Master of Ares Guild, one of Korea's two S-rank Hunters, and a Supreme Peak-level martial artist who was killed by Jin Taekyung.
- **Personality:** Outwardly genial, calm, and humorous; calculating, opportunistic, manipulative, coercive, and ruthless when challenged
- **Voice:** Smooth, good-natured, and indirect, using teasing conversation and veiled threats before becoming openly furious
- **Relationships:** Master of Park Jihoon and Go Jun (Team Leader Seok), whom he personally selected and trained; longtime Great Cataclysm acquaintance of Park Tae Seop; adversary of Jin Taekyung; knew Team Leader Choi from childhood; has an antagonistic history with Kim Hwajong, who saved his life at the collapse of Mapo Bridge eighteen years earlier; was visibly shaken by learning that Choi is Cheon Taemin's maternal grandson; regarded Cheon Taemin as an older brother despite no blood relation and long held him in respect and fear; secretly supported the orphanage where Lee Dongseok grew up and was regarded by Dongseok as a father; operated as Ares Guild's senior authority beneath its Guild Master; concealed Taemin's condition with Song Cheonwoo and participated in purging aides who knew the truth.

## Korean source

```text
＃594화



콰지직!

섬뜩한 파육음과 함께 지금껏 수백, 수천 번도 넘게 겪었던 느낌이 손끝을 타고 전해진다. 살을 가르고 뼈를 부수는 감각.

어느 순간 익숙해져 버린, 그래서 가끔은 씁쓸함을 느끼게 만드는 바로 그 감각이다.

이런 것에 익숙해졌다는 뜻은 그만큼 많은 생명을 내 손으로 직접 앗았다는 뜻이니까.

하지만 적어도 이번만큼은 아니었다. 죽어 가는 사내를 바라보는 내 마음에는 일말의 씁쓸함도 느껴지지 않았다.

“커……헉!”

바람 빠지는 소리와 함께 흘러나온 단말마. 그와 동시에 단단한 체격의 사내가 무릎을 꿇었다.

쿵.

한때는 섬뜩하기까지 하던 핏빛 안광은 점차 사그라지고, 전신은 눈앞에 들이닥친 죽음 앞에서 가늘게 떨리는 중이었다.

아니, 어쩌면 사내. 석고준이 두려워하는 것은 죽음 그 자체가 아니라 그에게 죽음을 내린 나일지도 모르겠다.

“지, 진태경.”

금방이라도 꺼질 듯한 목소리와 눈빛. 그러나 동정심 따위는 들지 않았다.

상대는 나와 같은 인간이 아니라 괴물이니까.

오늘 나를 비롯한 평화 길드원들이 김화종을 잃은 것처럼, 이름도 모르는 수천여 명의 사람들은 사랑하는 가족과 친구를 잃어야 했다.

그런 미친 짓을 벌인 대가치고는 편한 죽음을 맞이하는 것 같아 불공평하게 느껴질 정도다.

“쿨럭. 이, 이렇게 죽을 수는…….”

무릎을 꿇은 채 고통으로 경련하는 석고준을, 나는 서늘한 눈빛으로 내려다보았다.

“죽어라. 너 같은 병신한테는 산소도 아깝다.”

구구절절한 유언을 들어 줄 생각도, 남기게 해 줄 마음도 없다. 나는 놈의 가슴을 관통한 백염을 힘주어 뽑아냈다.

푸화악!

투명한 창날이 뽑힘과 동시에 미처 증발하지 않은 핏물들이 분수처럼 뿜어져 나온다.

가슴에 주먹만 한 구멍이 뚫린 채 멍하니 나를 올려다보던 석고준의 신형이 천천히 기울었다.

철벅.

그것이 마지막이었다.

자신의 피로 만들어진 웅덩이에 고개를 처박은 그는 눈을 부릅뜬 상태로 움직임을 멈췄다.

그리고 더 이상의 숨도, 한 줌의 생기도 느껴지지 않는 괴물의 시신을 바라보던 나는 문득 깨달았다.

‘끝났구나.’

지난 수십 년간 이정룡에게 충성을 바친 제자이자, 세계에서도 손꼽히는 아레스 길드의 실질적인 주인이 내 손에 죽었다.

두 번의 몬스터 웨이브를 인위적으로 일으켜 수천의 사상자를 발생시키고, 김화종과 이십여 명의 평화 길드원을 희생시킨 대가를 죽음으로 받아 냈다.

‘이것으로…… 정말 끝난 거야.’

하지만 어째서일까. 복수를 끝마쳤음에도 마음 한구석이 텅 비어 버린 듯한 기분이 드는 이유는. 마치 죽은 석고준이 아닌 내 가슴에 구멍이 뚫린 것 같았다.

그건 아마도, 곁을 떠난 이들이 두 번 다시 돌아오지 못한다는 사실을 알고 있기 때문일 것이다.

‘아직도 추우십니까. 여전히 어두우십니까.’

나는 닿지 않을 물음을 던지며 돌아섰다.

감히 상상할 수도 없을 만큼의 무게로 전신을 짓누르는 피로와 졸음을 참으며, 격전으로 초토화된 어두운 복도를 천천히 가로질렀다.

저벅.

걸음걸음마다 사람들의 얼굴과 어떤 기억이 떠올라 눈 앞을 가렸다.

무너지는 광안대교가 보였고 공포에 찬 사람들의 비명이 들렸다. 어느 승용차의 백미러에 매달린 가족사진 속에서 아주 오래전, 한없이 그리운 누군가와 새끼손가락을 걸고 했던 약속을 떠올렸다.



‘하연이가 좀 더 크면, 그리고 태경이 네가 중학생이 되면 그때 다시 바다 보러 오자. 알았지?’

‘진짜?’

‘당연하지. 자, 약속.’



하지만 오늘. 마음 깊은 곳에 간직하고 있던 약속의 장소가 무너졌다.

죄 없는 사람들이 죽고 몬스터가 역병처럼 창궐했다. 최선을 다했으나 더 많은 목숨을 구하지 못했다.

저벅.

비틀거리는 걸음만큼이나 마음 역시 어지러웠다. 그 혼란함 속에서 따뜻한 목소리가 머릿속에서 울려 퍼졌다.



‘자네 잘못이 아니야.’

‘……!’

‘자네는 최선을 다했네.’



죽어 가면서도 나를 위로해 주었던 반백의 노집사는 돌아올 수 없는 여정을 떠났다.

그가 도착한 곳이 밤인지, 낮인지. 추운지, 따뜻한지 나로서는 알 길이 없었다. 다만 바랄 뿐이다.

그 세상이 조금이라도 환하기를. 추위에 떨던 그가 더 따뜻하기를.

그리고…… 마지막으로 만나고 싶어 했던 한 사람이 왔다는 내 거짓말을 끝까지 믿었기를.

저벅.

결과가 없는 과정은 없다. 누군가가 대가를 치러야 한다고 생각했다. 잘못을 저지르면 벌을 받는 것이 순리(順理)라고 믿었다.

그래서 나는 이곳에 왔다. 누구도 범접할 수 없었던 왕궁의 문을 열어젖히고, 난공불락(難攻不落)의 철옹성을 함락시켰다.

싸우고, 싸우고, 또 싸웠다. 그리고 마침내 인두겁을 뒤집어쓴 괴물을 죽이고 나니, 문득 가슴이 공허해지며 한 가지 의문이 들었다.

‘이제 어떻게 해야 하지?’

모든 일의 원흉인 석고준을 처치한다면 조금이라도 이 분노가 사라질 줄 알았다. 후련함에 크게 소리 내어 웃을 수도 있을 것 같았다.

하지만 아니었다. 나는 단 한 번의 손짓으로 거대한 구덩이를 만들고 메울 수도 있지만, 정작 마음의 빈자리는 메우지 못했다.

삼 년 전에도 그랬고, 지금도 마찬가지다.

‘빌어먹을.’

입맛이 썼다. 결국 상처를 감내하는 것은 남은 자들의 몫으로 고스란히 남았다.

석고준에게 너무 고통 없는 죽음을 내린 것이 아닌가 하는 후회가 들 만큼…….

저벅.

나는 문득 발걸음을 멈췄다. 어느새 알 수 없는 위화감이 전신을 사로잡고 있었다. 서늘한 한기가 등골을 타고 스멀스멀 기어올랐다.

‘뭐지, 이 기분은?’

극심한 피로 때문인지. 그게 아니라면 복잡한 마음 때문인지 머릿속이 안개처럼 흐릿했다.

하지만 잠시 후, 우뚝 선 채 생각에 잠겨 있던 나는 마침내 위화감의 정체를 깨달을 수 있었다.

‘분명 석고준은 죽었을 텐데. 그런데 왜…….’

왜 처치를 알리는 시스템 창은 아직까지도 뜨지 않을까.

가슴 한복판에 창날을 박아넣고 장기를 태웠는데. 피 웅덩이에 얼굴을 처박은 채 숨이 멎는 것을 직접 보고 느꼈는데.

“설마.”

나는 낮게 뇌까리며 돌아섰다. 격전으로 인하여 처참히 파괴된 복도에는 유난히 짙은 어둠이 내려앉아 있었다.



* * *



시스템은 절대적이며 즉각적이다.

승리의 순간 찾아온 극심한 피로와 깊은 생각에 잠겨 있던 탓에 이상함을 알아차리지 못했을 뿐, 나는 그 사실을 누구보다 잘 알고 있었다.

그렇기에 석고준이 누워 있던 피 웅덩이가 텅 빈 것을 보고도 크게 놀라지 않았다.

‘살아 있다. 석고준이.’

그것 하나만큼은 확실해졌다.

다만 내가 궁금한 것은, 도대체 어떻게 그럴 수 있느냐는 것이었다.

A구역에는 석고준과 나, 단 두 명뿐이었고 놈은 분명히 죽음을 맞이한 상태였다.

심장이 멎고 호흡이 정지했으니, 최상급 포션으로 반신욕을 한다 해도 살아나는 건 불가능했다.

‘그런데 어떻게?’

나는 의문과 함께 석고준이 남긴 흔적을 쫓아 이동하기 시작했다.

A구역은 극소수의 인원에게만 허락된 비밀 구역답게 미로 같은 구조를 지니고 있었지만, 오직 한 방향을 향해 이어진 핏물을 따라가는 것은 그리 어려운 일이 아니었다.

나는 빠르게 공간을 가로지르며 주위의 정보를 받아들였다.

‘조력자는 없고. 흔적을 지울 틈이나 여유도 없었어.’

놈이 남긴 흔적에서 급박함이 느껴졌다. 홀로 바짝 엎드린 채 필사적으로 기어가는 모습이 눈앞에 스치는 듯했다. 그리고…….

‘마침내 두 다리로 일어났다. 바로 여기에서.’

핏물로 선명히 찍힌 두 개의 족적(足跡). 벽면에는 무수한 손자국 역시 함께 찍혀 있었다.

도대체 뭘까. 놈은 왜 고통으로 몸부림친 걸까. 그리고 나는 얼마 지나지 않아 그 의문에 대한 답을 찾을 수 있었다.

‘저건.’

그것은 피였다.

인간의 선홍빛 피가 아닌, 푸른 빛이 감도는 몬스터의 푸른 핏방울.

이와 같은 것들이 의미하는 바는 명백하다. 손에 닿은 몬스터의 피를 말없이 바라보던 나는 신형을 날렸다.

쉬익!

좌우를 스치는 바람 사이로 짙은 혈향(血香)과 악취가 느껴졌다. 극심한 피로에 휩싸인 와중에도 가까워지는 누군가의 인기척을 느낄 수 있었다.

그리고 내 발걸음이 또 다른 복도에 들어섰을 때.

나는 마침내 두 눈으로 직접 확인할 수 있었다.

마지막으로 봤던 모습과는 너무나도 달라진 그놈을.

“석고준.”

입술 사이로 흘러나온 목소리가 나직하게 울려 퍼졌다. 동시에 비틀거리며 복도를 걸어가던 석고준이, 아니 ‘괴물’이 돌아섰다.

“크륵. 쿠룩.”

무슨 말을 하려는지 모를 쇳소리는 다른 부분들에 비하면 아무것도 아니다.

4m에 이르는 거체와 터질 듯 부푼 팔과 다리는 기괴했고, 종이 다른 생물을 섞어 놓은 듯 제각각의 형태와 특징을 지닌 모습은 끔찍했다.

유일하게 본래의 형태를 유지하고 있는 것이 있다면, 그건 비늘로 반쯤 뒤덮인 인간의 얼굴과 그 사이로 빛나는 핏빛 안광이었다.

“진……태경. 카룩.”

두려움과 증오가 뒤섞인 눈동자가 이쪽을 향한다. 놈의 모습을 위아래로 훑은 나는 혐오를 담아 입을 열었다.

“그렇게까지 살아남고 싶었나? 몬스터가 되면서까지?”

“닥, 쳐라. 이건. 이건 나도 바라지 않았던-”

콰득! 우지직!

그건 순식간에 벌어진 일이었다.

석고준이 말을 잇기도 전, 보이지 않는 손이 움직인 것처럼 난데없이 놈의 오른팔이 꺾이고 푸른 핏물이 터져 나왔다.

“크아아악!”

고통에 찬 비명. 동시에 석고준의 기괴한 몸뚱어리에서 빠른 변화가 시작되었다.

스륵. 투두둑!

몬스터의 그것처럼 두꺼운 가죽과 비늘로 뒤덮인 피부가 아물고, 으스러진 뼈마디가 퍼즐처럼 짜 맞춰진다.

“헉. 허억.”

아직 가시지 않은 고통으로 숨을 헐떡이는 석고준. 그 모습에 나는 놈이 어떻게 여기까지 왔는지 알 것 같았다.

“트롤(Troll). 맞지?”

“……!”

툭 건넨 말에 놈의 눈꺼풀이 파르르 떨린다. 정답이라는 뜻이다.

트롤이라면 두말할 것 없이 압도적인 회복 능력을 지닌 몬스터.

아마도 이번에 석고준이 흡수한 S급 마정석의 원주인이었던 네임드 몬스터는 매우 강력한 트롤이었을 것이다.

그리고…….

‘놈이 흡수한 S급 마정석은 그것 하나뿐만이 아니겠지.’

겉모습만 봐도 짐작할 수 있었다. 기형적으로 부푼 신체와 엄청난 회복력은 트롤의 특징이지만, 몸의 절반을 뒤덮은 비늘과 가죽은 또 다른 몬스터의 흔적이다.

‘변이(變異). 그 자체.’

마력은 마나와는 달리 어둡고 혼탁하며, 인간을 타락시키는 기운이다. 그런데 엄청난 마력을 품은 S급 마정석을 두 개나 흡수했으니 불협화음이 일어나는 것은 당연했다.

“쿠룩. 지금보다 더, 강해질 수. 있었다. 그런데 네놈이. 네놈이…….”

나는 담담하게 놈의 말을 잘랐다.

“더 강해지는 게 아니라, 더 끔찍한 괴물이 됐겠지. 지금 네 모습을 봐라.”

“……!”

“넌 몬스터보다 더한 괴물이야. 헌터도, 인간도 아닌 한낱 괴물. 그게 바로 너다.”

저벅.

말과 함께 걸음을 옮겼다. 부릅뜬 눈으로 나를 바라보던 석고준이 비명처럼 외쳤다.

“오지 마. 크륵! 다가오지 마라!”

“그건 곤란하지. 눈앞에 몬스터가 있는데.”

“이. 이럴 수는!”

핏빛으로 물든 눈동자에는 어느덧 두려움이 가득했다.

아마 놈도 알고 있을 것이다. 가만히 서 있는 것만으로도 붕괴의 조짐을 보이는 이 몸뚱어리로는 결코 날 상대할 수 없다는 것을.

타다닥!

그래서 석고준이 등을 돌려 도망치기 시작했을 때, 나는 조금도 놀라지 않고 백염의 창대를 역수(逆手)로 잡고 쏘아 보냈다.

쐐애애애액! 퍼엉!

화염을 머금은 빛줄기가 놈의 다리를 터트리며 지면에 틀어박힌다. 두 다리를 잃은 석고준이 비명과 함께 버둥거리자 잘려 나간 단면에서 살과 뼈가 빠르게 재생된다.

물론 그것을 구경만 하고 있을 내가 아니었다.

“어디 한 번 재생해 봐. 할 수 있을 때까지.”

퍽!

남은 공력을 끌어모아 쇄도한 나는 발로 놈의 등을 짓밟고 두꺼운 두 팔을 붙잡은 채 끌어당겼다.

콰득. 우지지직!

두 다리에 이어 두 팔까지 잃은 석고준이 비명을 내질렀다.

하지만 나는 눈 하나 깜짝하지 않고 묵묵히 손을 움직였다.

서걱! 푸푹!

지면에 박혀 있던 창을 뽑아, 놈의 몸뚱어리 곳곳을 베고 찔렀다. 회복되려는 단면을 화염신장으로 지지고, 힘주어 잡아 뜯었다.

평소의 나였다면 결코 하지 않았을 잔혹한 손속이었지만, 지금의 나는 한 치의 망설임도 없었다.

콰드드득!

끝없이 계속되는 재생과 파괴. 그리고 이 끝나지 않는 고통의 굴레에서 먼저 나가떨어진 것은 석고준이었다.

“크아아악! 그, 그만!”

잔뜩 쉰 목소리로 비명을 내지른 놈의 눈동자는 전만큼 붉지 않았다. 어느 순간부터 서서히 느려지던 재생력도, 이제는 완전히 멈춰 있었다.

“이, 이제 죽여 주…….”

“안 그래도 그럴 생각이야.”

두 번 다시 살아날 수 없도록. 전보다 더욱 확실한 방법으로.

나는 석고준의 눈을 들여다보며 말을 이었다.

“네가 가는 곳이 천국이든, 지옥이든. 먼저 가서 기다리고 있어라. 그때는 정말 원 없이 죽여 줄 테니까.”

“……!”

그것이 전부였다. 석고준이 이 세상에서 마지막으로 들을 수 있었던 말은.

‘이제 끝이다.’

나는 놈의 대답을 기다리지 않았다. 한 치의 망설임도 없이 투명한 창날을 내리그었다.

서걱! 툭!

예리한 절삭음과 함께 몸뚱어리에서 분리된 머리가 땅바닥을 굴렀다.

그건 천태민 같은 영웅도, 스승인 이정룡 같은 효웅도 되지 못했던 괴물의 최후였다.

띠링.

귓가를 파고드는 익숙한 종소리와 함께, 나는 피 웅덩이에 잠긴 석고준의 머리를 집어 들었다.

그리고 천천히, 비틀거리는 발걸음으로 오직 나 혼자만이 남은 이 공간을 가로질렀다.

피곤했다.
```

## Final English reading copy

```markdown
# Chapter 594

*Crack!*

Along with that grisly tearing sound, a sensation I had experienced hundreds—thousands—of times traveled through my fingertips.

The feeling of flesh splitting and bones breaking.

It was a sensation I had grown used to at some point, and one that occasionally left a bitter taste in my mouth.

Because becoming accustomed to something like this meant I had taken that many lives with my own hands.

But at least this time, things were different. As I looked down at the dying man, I felt not the slightest trace of bitterness.

“Urgh……!”

A final groan escaped with a deflating sound. At the same time, the solidly built man dropped to his knees.

*Thud.*

The blood-red glow in his eyes, once terrifying enough to make anyone flinch, gradually faded. His entire body trembled faintly before the death rushing toward him.

No—perhaps what the man, Go Jun, feared was not death itself, but me, the one who had sentenced him to it.

“J-Jin Taekyung.”

His voice and eyes seemed ready to go out at any moment.

But I felt no pity.

Because my opponent wasn’t human like me. He was a monster.

Just as the members of the Peace Guild, myself included, had lost Kim Hwajong today, thousands of people whose names I did not even know had lost their beloved families and friends.

For the price of committing such madness, his death felt almost too easy. It was unfair.

“Cough. I-I can’t die like this……”

I looked down coldly at Go Jun, who was convulsing in pain on his knees.

“Die. Oxygen is wasted on a piece of shit like you.”

I had no intention of listening to some long-winded last words, nor did I feel like giving him the chance to leave any behind.

I wrenched White Flame out of his chest.

*Fwoosh!*

The instant the transparent spearhead came free, blood that had not yet evaporated sprayed out like a fountain.

With a fist-sized hole in his chest, Go Jun stared blankly up at me. Then his body slowly tilted.

*Splash.*

That was the end.

He plunged his face into a puddle made from his own blood and stopped moving with his eyes still wide open.

As I looked down at the corpse of the monster, no breath or spark of life remaining, I suddenly realized it.

*It’s over.*

The Disciple who had served Lee Jungryong faithfully for decades—and the de facto master of Ares Guild, one of the foremost Guilds in the world—had died by my hand.

He had caused two Monster Waves on purpose, creating thousands of casualties and costing Kim Hwajong and some twenty members of the Peace Guild their lives.

He had paid for it with his life.

*So this really is the end……*

But why?

Why did my heart feel hollow even after my revenge was complete? It was as though the hole was not in Go Jun’s chest, but in mine.

It was probably because I knew that the people who had left my side would never return.

*Are you still cold? Is it still dark?*

I turned away, asking questions that would never reach them.

Resisting fatigue and drowsiness heavy enough to crush my entire body, I slowly crossed the dark corridor, devastated by the fierce battle.

*Step.*

With every step, faces and memories rose before my eyes and obscured my vision.

I saw Gwangan Bridge collapsing and heard the screams of people consumed by terror. In the family photograph hanging from the rearview mirror of a passenger car, I remembered a promise I had made long ago by linking my pinky with someone I missed more than words could say.



“When Hayeon gets a little older, and you, Taekyung, start middle school, let’s come see the sea again. All right?”

“Really?”

“Of course. Here, promise.”



But today, the place from the promise I had kept deep in my heart had collapsed.

Innocent people had died, and monsters had spread like a plague. I had done everything I could, but I had failed to save more lives.

*Step.*

My heart was just as unsteady as my staggering footsteps. Amid that confusion, a warm voice rang out in my mind.



“It wasn’t your fault.”

“……!”

“You did your best.”



The silver-haired old butler who had comforted me even as he died had departed on a journey from which he could not return.

Whether the world he had reached was night or day. Whether it was cold or warm. I had no way of knowing.

I could only hope.

That his world was at least a little brighter. That he, who had trembled in the cold, was somewhere warmer.

And…… that he had believed my lie to the very end—the lie that the person he had wanted to see one last time had come.

*Step.*

Nothing happens without consequences. I believed someone had to pay the price. I believed that being punished for doing wrong was only natural.

That was why I had come here. I had thrown open the gates of a palace no one had dared approach and brought down an impregnable fortress.

I had fought, and fought, and fought again. And after finally killing the monster wearing a human face, I suddenly felt hollow inside and found myself wondering:

*What am I supposed to do now?*

I had thought that if I killed Go Jun, the root of all this evil, at least some of my anger would disappear. I thought I might even laugh out loud in relief.

But I hadn’t.

I could create and fill a massive pit with a single gesture, yet I could not fill the emptiness in my heart.

It had been the same three years ago, and it was the same now.

*Damn it.*

My mouth tasted bitter.

In the end, enduring the wounds was left entirely to those who remained.

I even found myself regretting that I might have given Go Jun a death that was too painless……

*Step.*

I suddenly stopped walking.

By then, an inexplicable sense of wrongness had seized my entire body. A cold chill slowly crawled up my spine.

*What is this feeling?*

Was it because of my extreme fatigue? Or perhaps because of my complicated emotions? My mind was hazy, shrouded in fog.

But after standing motionless and thinking for a moment, I finally realized the source of that wrongness.

*Go Jun should definitely be dead. So why……*

Why had the System window announcing his kill still not appeared?

I had driven a spearhead into the center of his chest and burned his organs. I had watched and felt him stop breathing with my own eyes.

“Don’t tell me.”

I muttered under my breath and turned around.

The corridor, horribly destroyed by the fierce battle, was shrouded in unusually deep darkness.



* * *



The System was absolute and immediate.

I knew that better than anyone. I simply had not noticed anything strange because I had been overwhelmed by exhaustion and deep thoughts in the moment of victory.

That was why I was not terribly surprised when I saw that the puddle of blood where Go Jun had been lying was empty.

*He’s alive. Go Jun is alive.*

That much had become certain.

What I wanted to know was how it was possible.

There had been only two people in Area A: Go Jun and me. And Go Jun had unquestionably been dead.

His heart had stopped and his breathing had ceased. Even if he had soaked in a half-body bath of top-grade potion, reviving him should have been impossible.

*Then how?*

With that question in mind, I began moving after the traces Go Jun had left behind.

Area A had a maze-like structure, befitting a secret zone permitted to only a handful of people. But following the trail of blood leading in one direction was not difficult.

I quickly crossed the space, taking in the information around me.

*There was no accomplice. He didn’t have the time or the chance to erase his traces.*

There was a sense of urgency in the marks he had left behind. It was almost as if I could see him crawling desperately along the floor, pressed flat against it by himself.

And then……

*He finally stood up on two legs. Right here.*

Two clear footprints had been stamped into the blood. Countless handprints marked the walls beside them.

What had happened?

Why had he writhed in agony?

Before long, I found the answer.

*That’s……*

It was blood.

Not the bright-red blood of a human, but blue drops of monster blood with a faint azure sheen.

The meaning of this was obvious.

I silently stared at the monster’s blood that had touched my hand, then shot forward.

*Whoosh!*

Amid the wind brushing past me on either side, I smelled a thick scent of blood and a foul stench. Even while exhausted to the point of collapse, I could sense someone’s presence drawing closer.

And when my footsteps carried me into another corridor—

I finally saw it with my own eyes.

The man who looked so completely different from the last time I had seen him.

“Go Jun.”

My voice echoed quietly between my lips.

At the same time, Go Jun—or rather, the *monster*—turned around as he staggered down the corridor.

“Krrk. Kurruk.”

The metallic growl, impossible to understand, was the least of it.

His enormous body stood four meters tall, while his arms and legs were grotesquely swollen as though they might burst. His appearance was horrifying, as if creatures of different species had been fused together, each part retaining its own shape and characteristics.

If there was one thing that had preserved its original form, it was the human face half-covered in scales, with blood-red eyes shining through the gaps.

“Jin…… Taekyung. Karruk.”

His eyes, filled with both fear and hatred, turned toward me.

I looked him up and down, then opened my mouth with disgust.

“Did you want to survive that badly? Even if it meant becoming a monster?”

“Shut…… up. This…… this wasn’t what I wanted either—”

*Crack! KRAK!*

It happened in an instant.

Before Go Jun could finish speaking, his right arm suddenly twisted as though moved by an invisible hand, and blue blood burst from it.

“GRAAAAH!”

A scream filled with pain rang out.

At the same time, rapid changes began throughout Go Jun’s grotesque body.

*Shlk. Crackle!*

The thick skin covered in hide and scales like a monster’s began to heal, while his crushed joints fitted themselves back together like puzzle pieces.

“Hah. Hah.”

Go Jun panted, the pain not yet gone.

Looking at him, I felt as though I understood how he had made it this far.

“Troll. Right?”

“……!”

At my casually tossed-out question, his eyelids trembled.

That meant I was correct.

A Troll was a monster with overwhelmingly powerful regenerative abilities. There was no question about that.

The Named Monster that had originally owned the S-grade Magic Gem Go Jun had absorbed this time must have been an extremely powerful Troll.

And……

*The S-grade Magic Gem he absorbed wasn’t the only one, was it?*

I could tell just by looking at him.

His grotesquely swollen body and tremendous regenerative power were characteristics of a Troll, but the scales and hide covering half his body were traces of another monster.

*Mutation. Pure and simple.*

Unlike mana, demonic energy was dark and turbid—a force that corrupted human beings.

So it was only natural that disharmony had occurred after he absorbed two S-grade Magic Gems containing an immense amount of demonic energy.

“Kurruk. I could have become stronger. Stronger than this. But you. You……”

I calmly cut him off.

“Not stronger. You would’ve become an even more horrifying monster. Look at yourself.”

“……!”

“You’re worse than a monster. You’re nothing but a monster—neither Hunter nor human. That’s what you are.”

*Step.*

I moved forward as I spoke.

Go Jun stared at me with his eyes wide open, then shouted like a scream.

“Don’t come any closer! Krrk! Don’t come near me!”

“That’s a problem. There’s a monster right in front of me.”

“T-This can’t be!”

His bloodshot eyes were now filled with fear.

He probably knew it, too.

With a body already showing signs of collapse simply from standing still, he had no chance of fighting me.

*Tap-tap-tap!*

So when Go Jun turned his back and began to flee, I was not surprised in the slightest.

I reversed my grip on White Flame’s shaft and hurled it.

*SHWAAAAK! BOOM!*

A streak of light wreathed in flames blasted through his legs and embedded itself in the ground.

As Go Jun, now without either leg, thrashed and screamed, flesh and bone rapidly regenerated from the severed ends.

Of course, I had no intention of standing around and watching.

“Go ahead and regenerate. Keep doing it as long as you can.”

*Thud!*

I gathered up the internal energy I had left and surged forward. I planted my foot on his back, seized his two thick arms, and pulled.

*Crack. KRAKAKAK!*

After losing both legs, Go Jun lost both arms as well and let out a scream.

But I did not so much as blink. I simply continued moving my hands.

*Slice! Stab!*

I pulled the spear from the ground and slashed and stabbed his body in several places. I seared the sections trying to regenerate with the Flame Divine Palm, then gripped them tightly and tore them apart.

It was a level of brutality I would never have shown under ordinary circumstances.

But the me standing here now did not hesitate even for a moment.

*KRAKAKAK!*

Regeneration and destruction continued without end.

And the first one to collapse beneath this never-ending cycle of agony was Go Jun.

“GRAAAAH! S-Stop!”

His eyes were not as red as before when he screamed in a thoroughly hoarse voice.

His regenerative power had begun slowing down at some point.

Now it had stopped completely.

“Now…… kill me……”

“I was planning to anyway.”

So that he could never come back to life again.

In a way even more certain than before.

I looked into Go Jun’s eyes and continued speaking.

“Whether you’re going to heaven or hell, go there first and wait for me. When I get there, I’ll kill you as much as I please.”

“……!”

That was all.

Those were the final words Go Jun would ever hear in this world.

*It’s over now.*

I did not wait for his answer.

Without the slightest hesitation, I brought the transparent spearhead down.

*Slice! Thud!*

With a sharp cutting sound, the head separated from the body and rolled across the ground.

That was the end of the monster who had become neither a hero like Cheon Taemin nor an ambitious warlord like his Master, Lee Jungryong.

*Ding.*

Along with the familiar chime piercing my ears, I picked up Go Jun’s head from the puddle of blood.

Then, with slow, staggering steps, I crossed the space where I alone remained.

I was tired.
```

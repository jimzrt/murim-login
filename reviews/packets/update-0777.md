<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0777.txt",
      "sha256": "b57a8cba09f5b61395045be7882e8a23472593527e9959343de897bd7842d8f2",
      "bytes": 13580
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "0fd46ee72d86865f04608ac60d69c72a34480937465a172d0c0e41ac293fc9e3",
      "bytes": 2208
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "45e50ae77be3c073d1488a74f8e2d08bfe6cbdb99494ab42a6437874780008c2",
      "bytes": 223212
    },
    {
      "path": "characters/Cheon Taemin.md",
      "sha256": "61e8bc704bcd95a40fbe54fed3df6e622171b117cf52e364e0126431584ec263",
      "bytes": 752
    },
    {
      "path": "characters/Go Jun.md",
      "sha256": "df691088271feedfd2b920ac5208e9262d7bfef80cccedaa3bd2f41b29dfac76",
      "bytes": 817
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "ffad690a8337d02306380f5585ce47d59dc006037b5d7d4d81cee449351024b8",
      "bytes": 2096
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "b93bc8a1db85a0ddf5fc30893a157d77b8a96a88ca64af6961f007fd534da6f1",
      "bytes": 622
    },
    {
      "path": "characters/Lee Jungryong.md",
      "sha256": "5c43b531ce5becef946ae9c1c945458fadd5a17ef609da5d38dc4713834c2ada",
      "bytes": 1384
    },
    {
      "path": "characters/Michael.md",
      "sha256": "8e0da3be2775107354d5d4e67b802093e5e6e344e624f822e85c28da52411eb7",
      "bytes": 1024
    },
    {
      "path": "characters/Team Leader Choi.md",
      "sha256": "3a25eabfbc6001843bba8736d7534623b9db8c1ce4e740a60a33d4e1dd3b5c0d",
      "bytes": 602
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "86631aa1d12400218ec7bbba2dca82dc4d4e6ad6a1aeacb4991eab5683d50ceb",
      "bytes": 241432
    }
  ],
  "estimated_tokens": 11465
}
-->

# Durable State Update — Chapter 777

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 777. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 777. Profile updates may replace only one
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
  "chapter": 777,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 777,
    "continuity_sources": [777],
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
    "Jin and Team Leader Choi have returned to Korea and are operating under heightened security before the World Hunter Federation's inaugural ceremony.",
    "Jin's Broken Body continues to drain his strength and cause severe internal pain.",
    "Jin is withholding the discovered clue from Baek because Michael Silbert may have surveillance or a mole near the President.",
    "The Skeleton King remains concealed with Jin and silent, but Michael can sense its presence.",
    "Michael Silbert is positioning himself at the center of the World Hunter Federation while Cheon Taemin remains absent.",
    "Michael's pre-awakening life included poverty in Paris's Tenth Arrondissement, parental abandonment, criminal convictions, and erased records.",
    "Michael awakened during the 2020 Great Cataclysm and survived the Great Battle of Paris before becoming a public hero.",
    "Michael's true strength remains concealed, though his physical strength and qi control are extraordinary.",
    "Jin regards Michael with pity and disgust rather than fear and refuses to submit to him.",
    "The inaugural ceremony of the new World Hunter Federation is underway, and the attendees have learned that Cheon Taemin will not appear.",
    "An unidentified attendee has approached the center of the round table."
  ],
  "continuity_sources": [
    775,
    776
  ],
  "open_questions": [
    "What is Michael's ultimate objective behind the atrocities and sacrifices he has caused?",
    "What is the full extent of Michael's concealed strength?",
    "Is the clue discovered by Jin and his allies genuine, and is their fourth path viable?",
    "What coordinated plan do Michael and The Prophet have for the Federation and the coming crisis?",
    "Who is the unidentified attendee approaching the center of the round table, and what will they do?"
  ],
  "safe_through": 776,
  "temporary_decisions": [
    "Render 파리 대전투 as Great Battle of Paris.",
    "Render 파리 10구 as Paris's Tenth Arrondissement.",
    "Render 망가진 신체 as Broken Body.",
    "Use National Assembly Hall for 국회의사당.",
    "Render 스톤 킹 as Stone King."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 최민우    | **Choi Minwoo**   |
| 천태민    | **Cheon Taemin**  |
| 이정룡    | **Lee Jungryong** |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 선배     | **Senior**                                   |
| 상태               | **Status**                     |
| 명성               | **Fame**                       |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 길드      | **Guild**             |
| 길드장     | **Guild Master**      |
| 부길드장    | **Vice Guild Master** |
| 팀장      | **Team Leader**       |
| 대사      | **Master** for a senior Buddhist monk                           |
| 고준 | **Go Jun** | Personal name of Team Leader Seok; Lee Jungryong's prized Disciple. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 미카엘 | **Michael** | Guild Master of Odin Guild. |
| 아스모데우스 | **Asmodeus** | Demon King referenced in Taekyung's sarcastic comparison; does not appear directly. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 준이 | **Jun** | Family nickname used in the form Jun's dad. |
| 석고준 | **Go Jun** | Source full-name form for the established Go Jun, also known as Team Leader Seok. |
| 마왕 | **Demon King** | The being Cheon Taemin killed. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 존슨 | **Johnson** | Co-host of the American talk show that replays Taekyung's viral interview. |
| 중국 | **China** | Country from which Team Leader Choi’s video originates. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 쓰촨 | **Sichuan** | Variant spelling used for the region associated with the pattern Jin recognizes. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 국회의사당 | **National Assembly** | Government building visible from the skyscraper. |
| 정룡 | **Jungryong** | Cheon Taemin's trusted associate who joined the Peace Guild. |
| 스카이 | **Sky** | American epithet for Cheon Taemin. |
| 인시 | **Insi** | The traditional time period from three to five in the morning. |
| 마력 | **magical power** | Distinct from mana; the Skeleton King's area of expertise. |
| 실베르트 | **Silbert** | Family name in Michael Silbert. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 진태경 | 선배님들 | junior_to_senior_team_members | Seniors | polite-but-threatening | Taekyung addresses the Myeongdong Guild Team 1 Hunters while ordering them to clear a path. |
| 이정룡 | 진태경 | senior S-rank Hunter to younger Hunter and adversary | Young man | polished, teasing, and veiled-threatening | Uses a genial tone and indirect threats while trying to make Taekyung release the captives. |
| 진태경 | 이정룡 | younger Hunter to senior S-rank Hunter and adversary | you | polite but mocking and defiant | Taekyung answers Lee's soft threats with the wolf-and-tiger metaphor and refuses to yield. |
| 이정룡 | 고준 | Master to Disciple | Go Jun | familiar and testing | Lee switches from Seok's office title to his personal name while considering whether he can defeat Taekyung. |
| 고준 | 이정룡 | Disciple to Master | Master | deferential | Go Jun responds to Lee's personal-name address as 스승님. |
| 이정룡 | 천태민 | younger_to_older_brother_by_choice | older brother | reverent and familiar; internal | Lee Jungryong uses 형님 in unspoken thoughts and regards Cheon Taemin as an older brother despite having no blood relation. |
| 석고준 | 최민우 | Ares security leader to rival Guild Master | Team Leader Choi Minwoo | formal but barbed | Uses 평화 길드 최민우 팀장님 while belittling Choi and blaming the Peace Guild for Taekyung's apparent death. |
| 진태경 | 석고준 | returning Hunter to hostile Ares security leader | you fucking bastard | hostile and profane | Taekyung directs his final insults and challenge at Go Jun after returning alive. |
| 석고준 | 진태경 | hostile_opponents | brat | hostile and overconfident | Go Jun addresses Taekyung internally as 애송아 while launching his full-strength attack. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 최민우 | 진태경 | trusted allied team leader to younger allied Hunter | Mr. Jin | formal-polite and concerned | Choi warns Jin about the danger of the operation and affirms his deep trust. |
| 진태경 | 최민우 | younger allied Hunter to allied team leader | Team Leader Choi | polite, familiar, and teasing | Jin jokes with Choi while acknowledging and dismissing his concern. |
| 진태경 | 존슨 | Allied Hunter to Grand Mage | Johnson | polite and familiar | Jin repeatedly addresses Magic Johnson directly while requesting explanations and permission to visit the site. |
| 고준 | 진태경 | Ares Guild combatant confronting the killer of his Master | you | hostile and informal | Go Jun uses 너 while demanding Jin confess to Lee Jungryong's death and threatening retaliation. |
| 진태경 | 고준 | dominant adversary confronting Lee Jungryong's Disciple | you | contemptuous and informal | Jin uses 너 and 놈 while overpowering Go Jun and ordering him to end the conflict with Lee Jungryong. |
| 진태경 | 헌터 | field commander to allied Hunters | you; Hunters | blunt and commanding | Orders the human forces to stop asking questions and kill the fleeing Minotaurs. |
| 미카엘 | 진태경 | rival_to_target | you | quietly polite but threatening | Michael warns Jin to reconsider for the sake of Jin's monster friend. |
| 진태경 | 미카엘 | target_to_rival | Go fuck yourself | blunt and profane | Jin rejects Michael's proposal to resurrect the World Hunter Federation. |

## Listed compact profiles

### Cheon Taemin.md

# Cheon Taemin (천태민)

- **Safe through:** Chapter 776
- **Aliases:** Slayer; Sky (the American epithet used for him)
- **Role:** Cheon Taemin is Ares Guild Master and the world's greatest Hunter, known as the Slayer for killing the Demon King and creating the first Mana Cultivation Method during the Great Cataclysm, and he remains unconscious after more than twenty years in a wired mechanical capsule at his former mansion.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** Maternal grandfather of Team Leader Choi and Jin Taekyung and father of Soyeong; regarded by Lee Jungryong as an older brother despite their lack of blood relation.

### Go Jun.md

# Go Jun (고준)

- **Safe through:** Chapter 767
- **Aliases:** Team Leader Seok
- **Role:** Go Jun was Ares Guild's Vice Guild Master, Lee Jungryong's Disciple and former Head of Security, the de facto successor to Lee's Ares legacy, and a mutated monster who was killed by Jin Taekyung in Area A.
- **Personality:** Disciplined and controlled under ordinary pressure, fiercely loyal to Lee Jungryong, but consumed by humiliation and rage when Ares Guild's authority is challenged.
- **Voice:** Dry, controlled, and formal with subordinates; deferential when addressing his Master.
- **Relationships:** Go Jun inherited Lee Jungryong's Ares legacy after becoming his Disciple and regarded Jin Taekyung and Choi Minwoo as enemies before his death.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 776
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple, the Fire Gate Clan's nineteenth successor, the Pavilion Master of the Fire Dragon Pavilion within the Murim Alliance, a Supreme Peak master with the Heavenly Martial Physique and Force, and a publicly recognized S-rank-level Hunter who formally retains an A-rank license, as well as a traveler between Murim and another world resembling the realm of immortals and the principal Hunter opposing Michael Silbert's terrorist campaign.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real; treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements as well as the Peace Guild's Guild Master, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Magic Johnson is an allied Grand Mage who supplies him with intelligence, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 776
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Lee Jungryong.md

# Lee Jungryong (이정룡)

- **Safe through:** Chapter 751
- **Aliases:** None
- **Role:** Former Vice Guild Master of Ares Guild, one of Korea's two S-rank Hunters, and a Supreme Peak-level martial artist who was killed by Jin Taekyung.
- **Personality:** Outwardly genial, calm, and humorous; calculating, opportunistic, manipulative, coercive, and ruthless when challenged
- **Voice:** Smooth, good-natured, and indirect, using teasing conversation and veiled threats before becoming openly furious
- **Relationships:** Master of Park Jihoon and Go Jun (Team Leader Seok), whom he personally selected and trained; longtime Great Cataclysm acquaintance of Park Tae Seop; adversary of Jin Taekyung; knew Team Leader Choi from childhood; has an antagonistic history with Kim Hwajong, who saved his life at the collapse of Mapo Bridge eighteen years earlier; was visibly shaken by learning that Choi is Cheon Taemin's maternal grandson; regarded Cheon Taemin as an older brother despite no blood relation and long held him in respect and fear; secretly supported the orphanage where Lee Dongseok grew up and was regarded by Dongseok as a father; operated as Ares Guild's senior authority beneath its Guild Master; concealed Taemin's condition with Song Cheonwoo and participated in purging aides who knew the truth.

### Michael.md

# Michael (미카엘)

- **Safe through:** Chapter 776
- **Aliases:** None
- **Role:** Michael Silbert is the Guild Master of Odin Guild, a public hero who helped suppress five Monster Waves and saved Paris twice, the hidden architect of a terrorist campaign, and a survivor of the Great Battle of Paris who erased his pre-awakening criminal records while positioning himself at the center of the World Hunter Federation.
- **Personality:** Controlled, calculating, condescending, and confident in his intelligence and ability to manipulate events, but increasingly impatient and anxious since learning of Jin Taekyung.
- **Voice:** Polite and conversational when relaxed, but quietly authoritative and coercive when asserting control.
- **Relationships:** Michael personally selected and trained Huginn, commands Odin Guild's hidden alliance, secretly confers with The Prophet, and regards Jin Taekyung's friendship with the monster as his fatal weakness.

### Team Leader Choi.md

# Team Leader Choi

- **Safe through:** Chapter 773
- **Aliases:** Choi Minwoo (최민우)
- **Role:** Team Leader Choi is Jin Taekyung's meticulous intelligence and operations lead, a trusted ally and natural leader capable of guiding the reestablished World Hunter Federation.
- **Personality:** Calm, pragmatic, meticulous, and emotionally steady under pressure.
- **Voice:** Measured, professional, and reassuring without minimizing responsibility.
- **Relationships:** A trusted ally and operational adviser to Jin Taekyung.

## Korean source

```text
＃777화



드디어 시작됐구나.

나는 마음속으로 뇌까리며 홀로 걸음을 옮기는 누군가의 뒷모습을 바라보았다.

아니, 나뿐만 아니라 이 자리의 모두가 마찬가지다.

곳곳에 설치된 카메라와 원탁을 채운 삼백여 쌍의 눈동자가 한 사람을, 정확히는 미카엘 실베르트를 따라 움직이고 있었다.

저벅저벅.

일말의 망설임 없이 나아가는 발걸음.

주위의 웅성거림은 이미 사그라든 지 오래다. 약속이라도 한 듯 동시에 입을 다문 사람들은 각기 다른 감정으로 미카엘 실베르트를 바라보는 중이었다.

누군가는 갑작스럽게 나선 그의 모습에 혼란스러워하는 기색을 감추지 못했고, 누군가는 깊어진 눈빛으로 생각에 잠겼으며, 혹은 이 모든 상황이 당연하다는 듯이 고개를 끄덕이거나 옅은 웃음을 띤 이들도 있었다.

나는 그런 사람들의 모습을 모두 눈에 담았다.

그들이 순간 드러낸 감정과 미세한 입꼬리의 움직임마저 빠짐없이 보았고, 수많은 얼굴들을 머릿속에 각인시켰다.

그리고 다음 순간.

슥.

미카엘 실베르트가 발걸음을 멈추었다.

이 거대한 원탁의 중심이자 수십 년간 오직 한 사람을 위해 존재했던 그 공간의 코앞에서.

하지만 놈의 마지막 한 걸음은 보이지 않는 무언가에 가로막힌 것처럼 나아가지 못했고, 굳게 닫혀 있던 입술이 열렸다.

“여러분. 오늘 저는, 참으로 충격적인 소식을 접했습니다.”

잠겨 있는 목소리. 눈가에 맺힌 물기가 조명을 받아 반짝인다.

이 예상치 못한 상황에 동요하는 사람들과 녹화 중인 카메라를 차례차례 응시한 미카엘 실베르트가 말을 이었다.

“발족식이 시작되기 직전, 두 청년이 찾아와 그 소식을 전해 주었습니다. 처음에는 믿기 힘들었지만 결국 현실을 받아들일 수밖에 없었고, 제게는 마음을 추스를 시간이 필요했습니다.”

“그 소식을 전해 주었다는 두 사람이 누구인지, 또 소식의 내용이 무엇인지 알려 주실 수 있으시겠습니까?”

적절한 흐름과 타이밍에 튀어나온 누군가의 질문.

마치 사전에 계획된 것처럼 완벽하다.

아니, 계획된 것이 분명했다.

그리고 대본대로 흘러가는 이 한편의 뮤지컬 속에서, 적절하게 끼어든 단역의 물음에 주인공은 다음 대사를 읊었다.

“저를 찾아온 두 청년의 정체를 밝히는 것은 그리 어렵지 않습니다. 그 두 사람 모두 익히 알려진 인물이고, 지금도 이 자리에 함께하고 있으니 말입니다. 하지만 소식의 내용을 제가 직접 여러분께 말씀드리는 것은 곤란합니다.”

“어째서입니까?”

“제게는 그럴 만한 자격이 없으니까요.”

침착하게 대답한 미카엘 실베르트가 고개를 돌려 나를, 정확히는 내 오른편에 앉은 최 팀장을 바라보며 덧붙였다.

“핏줄을 이어받은 가족이라면 모를까.”

“……!”

아무리 둔감한 사람이라 해도 저 말의 의미를 눈치채지 못하는 것이 이상한 상황.

순식간에 주위를 물샐틈없이 감싼 수백 명의 시선 사이로, 은밀히 전해진 음성이 귓가를 파고들었다.

- 자네가 무슨 마음으로 이곳에 왔는지는 모르겠지만, 지금부터는 한 가지만 기억하게.

미카엘 실베르트.

놈이 나를 바라보고 있었다. 조금 전 흘렸던 악어의 눈물이 아닌, 오직 야망으로 빛나는 두 눈동자로.

- 모든 선택에는, 그에 합당한 결과가 뒤따른다.

“…….”

- 그러니 부디 신중히 선택하길 바라네. 단 한 번뿐인, 돌이킬 수 없는 선택일 테니.

마지막 권고와 함께 쏘아지는 그의 눈빛이, 주위에서 쏟아지는 그 시선들이 너무나도 뜨거워서 나는 그만 눈을 감았다.

그리고 생각했다.

그래. 결국, 이렇게 되는구나.

처음부터…….

‘이 길밖에는 없는 거였구나.’

텅 비어 버린 듯한 공허함과 함께 눈을 떴다. 동시에 시선이 마주친 최 팀장이, 내 눈동자에 담긴 뜻을 읽고 자리에서 일어났다.

드르륵.

새로운 주인보다도 오랜 세월을 버텨 온 의자가 천천히 뒤로 밀려난 그 순간.

“오늘의 발족식의 목적인 대표 선출에 앞서, 제 외조부이신 천태민 헌터께서는…….”

마침내 흘러나온 한 사람의 이름과 함께 찾아온 숨 막히는 고요함 속에서, 구세주의 유일한 혈육은 나직이 말을 이었다.

“병세가 깊어 이번 전쟁에 참전하지 못하게 되셨음을 알려 드립니다.”

“……!”

“……!”

보이지 않는 거대한 충격이, 사방을 휩쓸었다.



* * *



제1 국회의사당에 숨 막히는 침묵이 내려앉았다.

지금 이 순간 혼란과 충격으로 얼어붙은 사람들이 할 수 있었던 것은, 조금 전 자신들이 들었던 그 한 마디를 끊임없이 되새기는 것뿐이었다.



‘제 외조부인 천태민 헌터께서는, 병세가 깊어 이번 전쟁에 참전하지 못하게 되셨음을 알려드립니다.’



발족식이 시작된 지 불과 십여 분만에 터진 폭탄.

아니, 어쩌면 또 다른 의미로의 재앙.

‘스카이가 병환이라니. 이게 도대체 무슨.’

‘그분이 어찌…… 그럴 리 없다. 말도 안 돼.’

가장 거세게 현실을 부정하는 이들은 주로 원로라 불리는 구세대의 헌터들이었다.

천태민을, 인류를 마왕으로부터 구원한 대영웅을 똑똑히 기억하고 있는 그들이 느낀 충격은 그 누구보다 컸다.

당연한 일이었다.

그들의 기억 속에 존재하는 천태민은 인간을 넘어, 현인신(現人神)에 가까운 존재였으니까.

단신으로 수만에 달하는 몬스터 군단을 격멸하고, 강대하기 그지없던 S급 몬스터들의 사지를 찢어발기던 그 모습.

그리고 그 압도적인 무용만큼이나 강렬했던 위엄.

그렇기에 천태민과 함께라면 기꺼이 사지(死地)로 향할 수 있었다.

어깨를 나란히 하고 파도처럼 밀려드는 몬스터들을 가르며 나아가고, 또 나아갔다.

원로들이 끔찍하기 짝이 없는 전장을 기억을 떠올릴 수 있는 것은, 바로 그 기억 속에 천태민이 있었기 때문이었다.

그와 함께 인류의 승리를 이끌었다는 찬란한 영광이 그 안에 스며 있었기 때문이었다.

그런데 병이라니.

마왕 아스모데우스조차 쓰러트린 인류의 구세주가, 전쟁에 참여하지 못할 만큼 병환이 깊어졌다니.

사람들이 느낀 충격은 이내 허탈감이 되었고, 몇몇 원로들은 분노마저 느꼈다.

“도대체, 도대체 이게 무슨 소리인가!”

“병세가 깊다니. 자네의 외조부께서 어떤 분이신지 몰라도 유분수지!”

“자세히 설명해 보게. 그분께서 그럴 리가 없어!”

그러나 목소리까지 높인 원로들의 바람과는 반대로, 천태민의 하나뿐인 외손자는 침착하게 고개를 내저을 뿐이었다.

“제가 말씀드린 것은 모두 틀림없는 사실입니다.”

“자네!”

“선배님들의 마음을 충분히 이해합니다. 몇 달 전의 저 역시 그랬으니까요.”

“그게…… 무슨 말인가?”

“언제나 의문이었습니다. 외조부님께서는 어디 계신지. 도대체 무슨 이유가 있어 그토록 오랜 시간 동안 하나뿐인 손자에게도 모습을 드러내지 않으시는지.”

최민우가 모두를 바라보며 말을 이었다.

“이정룡 부길드장. 그리고 석고준이 사망한 뒤에야 알게 되었습니다. 어느 날 그분께서 알 수 없는 이유로 코마(Coma), 즉 의식불명의 상태에 빠지셨고 극소수의 인물들이 그 사실을 숨기고 있었다는 사실을 말입니다.”

“……!”

다시 한번 거대한 충격이 주위를 휩쓸었다. 그러나 이번 충격이 불러온 침묵은 그리 오래가지 않았다.

“믿기 힘들겠지만 모두 사실이야. 내가 보증하지.”

불쑥 들려온 저음의 목소리에, 사람들의 시선이 한 방향으로 쏠렸다.

줄곧 입을 다문 채 상황을 주시하던 거구의 흑인이 그들을 바라보고 있었다.

“매직 존슨!”

“다, 당신도 알고 있던 거요?”

고개를 끄덕인 매직 존슨이 대꾸했다.

“몇 달 전 저 친구들의 연락을 받고 이 나라에 왔었지. 그곳에서 의식을 잃은 스카이를 보게 될 줄은 몰랐지만.”

“그, 그렇다는 건 정말로…….”

“그래, 내가 알고 있는 모든 지식과 마법을 떠올려봐도 그의 의식을 회복시킬 만한 방법을 찾지 못했어. 물론 다른 누군가에게 털어놓을 수도 없었지. 만약 이 엄청난 비밀이 새어 나간다면 더한 혼란이 생겨날 테니까.”

사람들은 문득 당시의 상황을 떠올렸다.

어느 순간부터 서서히 증가하기 시작한 마력 수치와 이변(異變)들.

중국에서는 아크 리치가 몬스터 군단을 이끌고 쓰촨을 피로 물들였고, 사람들의 불안감은 점차 커져만 가고 있었다.

“하지만 더 이상은 감출 수 없게 됐지. 이제 전 세계가 스카이를 찾고 있고, 오늘로 첫발을 내디딘 세계 헌터 연맹은 UN이 그랬던 것처럼 저들이 원하는 답을 내놓아야 해.”

그 순간 사람들의 머릿속을 스친 단어는 하나였다.

‘지도자.’

천태민이 쓰러진 지금, 그들에게는 어떻게든 새로운 지도자가 필요했다.

구세주의 빈자리를 최대한 메울 수 있는, 이 거대한 원탁에 둘러앉은 삼백여 명의 인물 중 과반수의 지지를 받을 수 있는 새로운 영웅이.

‘그렇다면?’

생각이 거기까지 미쳤을 때, 대다수의 사람들은 이미 마음의 결정을 내린 후였다.

무력. 명성. 인망. 희생정신과 용기. 지도력…….

그들에게는 지도자를 평가하는 각자의 기준이 있었고, 이미 영웅이라 불리는 이들 중에서도 조건을 충족시킬 만한 인물은 한 줌에 불과했으니까.

그리고 그런 의미에서, 절대 빼놓을 수 없는 한 사람이 있었다.

미카엘 실베르트.

수많은 이들의 시선이 그를 스쳐 지나갔다.

그중에는 마침내 때가 왔다는 듯 의기양양하게 미소짓는 이들도 있었고, 신중하게 생각에 잠겨 있는 이들도 있었다.

하지만 미카엘 실베르트는 이처럼 뒤바뀐 상황 속에서도 결코 내색하지 않았다.

이미 마지막 한 걸음만을 남겨 둔 그는, 그다음을 생각하고 있었다.

‘예상했던 시기보다는 이르지만…… 제거해야겠어. 하루라도 빨리.’

벌써 세계 헌터 연맹이라는 절대 권력이 손에 만져지는 듯했지만, 두고두고 거슬릴 장애물은 반드시 치워야 하는 법.

미카엘 실베르트는 깊게 가라앉은 눈동자로 한 사람을 바라보았다.

투표가 시작되는 와중에도 굳게 입을 다문 채, 침묵하고 있는 진태경의 옆에는 담담한 표정을 한 금발의 몬스터가 있었다.



* * *



나는 손에 들린 철 조각을 내려다보며 생각했다.

‘이걸 뭐라고 하더라.’

도편추방제? 도편추첨제?

고대 아테네에서 독재자를 추방할 때 쓰던 방법에서 기원했다고 들었던 것 같은데, 잘은 모르겠다.

다만 확실한 것은 내 손에 들린 것이 도자기 파편이 아닌 타워 실드의 파편이고, 여기에 가장 많이 이름이 쓰인 사람은 추방되는 것이 아니라 세계 헌터 연맹의 지도자가 된다는 것이다.

- 그 반대였으면 참 좋았을 텐데. 안 그러냐?

문득 흘려보낸 전음(傳音)에, 기대하지 않았던 대답이 돌아왔다.

- 그게 무슨 뜬금없는 소리냐.

- 그냥 해 본 소리지, 뭐. 그나저나 이번에는 대답하네?

- 아마도 이게 마지막일 테니까.

나는 철조각을 만지작거렸다.

- 미친 새끼. 웬일인가 했더니, 아직도 그 소리네.

- 네가 무슨 생각을 하고 있는지는 안다. 하지만 그건 너무…….

- 위험하다고?

잠시 침묵하던 스켈레톤 킹이 대답했다.

- 그래. 이 몸은 지금까지도 확신하지 못하겠다.

- 가능성은 반반에 가까워. 그리고 이건 내 짐작이지만, 성공 가능성이 미세하게 더 높고.

- 알고 있나? 그건 모든 것을 잃을 확률이 절반이나 된다는 뜻이다.

- 그래? 나한테는 모든 것을 지킬 수 있는 확률이 절반이나 된다는 뜻으로 들리는데.

- ……!

- 날 믿어.

나는 주위를 둘러보았다. 익숙한 얼굴들, 믿을 만한 사람들이 곁에 있다. 모두가 내 전우고, 친구들이다.

- 나를 정 못 믿겠으면, 우리를 믿든지.

이번 침묵은 처음의 것보다 더 길었다. 그리고 나는 아주 오랜만에, 스켈레톤 킹과 눈을 마주할 수 있었다.

- 왜 이렇게까지 하는 거냐? 그 위험을, 네 가족과 친구들이 다칠 수 있는데도.

나는 대답했다. 어쩌면 처음 녀석을 만난 그날부터 정해져 있던 그 사실 그대로.

- 너도 내 친구니까.
```

## Final English reading copy

```markdown
# Chapter 777

So it’s finally starting.

I muttered to myself as I watched the back of someone walking alone.

Then again, it wasn’t just me. Everyone here was doing the same.

The cameras installed throughout the hall and the three hundred pairs of eyes around the round table followed one man—or, to be precise, Michael Silbert.

*Clop. Clop.*

His footsteps carried him forward without the slightest hesitation.

The murmuring around us had died down long ago. As if they’d all agreed to it, everyone had fallen silent at once, watching Michael Silbert with a different emotion in their eyes.

Some couldn’t hide their confusion at the sight of him suddenly stepping forward. Others looked thoughtful, their eyes growing serious. A few nodded as if the whole situation were only to be expected, or wore faint smiles.

I took in every one of them.

I saw every emotion they let slip in that moment, every subtle twitch at the corners of their mouths, and etched their many faces into my memory.

Then, the next moment—

*Swish.*

Michael Silbert stopped.

Right in front of the center of the enormous round table, a space that had existed for decades solely for one man.

But his final step wouldn’t come. It was as if something invisible stood in his way. His firmly closed lips parted.

“Everyone. Today, I received truly shocking news.”

His voice was choked. Moisture glimmered around his eyes in the light.

After looking in turn at the people shaken by this unexpected turn of events and at the cameras recording it all, Michael Silbert continued.

“Just before the inaugural ceremony began, two young men came to see me and gave me the news. At first, I found it hard to believe. But in the end, I had no choice but to accept reality. I needed some time to compose myself.”

“Could you tell us who the two young men were, and what news they brought?”

Someone’s question came at exactly the right moment.

Perfectly timed, as if it had been planned in advance.

No—as a matter of fact, it had been planned.

And in this musical playing out according to its script, the leading man delivered his next line in response to the bit player’s perfectly placed question.

“It won’t be difficult to reveal the identities of the two young men who came to see me. They’re both well-known figures, and they’re here with us now. But I’m afraid it wouldn’t be appropriate for me to tell you the news myself.”

“Why not?”

“Because I’m not qualified to do so.”

Michael Silbert answered calmly, then turned to look at me—or, more precisely, at Team Leader Choi, seated to my right.

“Unless you’re family by blood, of course.”

“……!”

It would have been strange for anyone, no matter how obtuse, not to understand what he meant.

Hundreds of gazes closed in around us from every direction, leaving no room to escape. Amid them, a voice reached my ear in secret.

*I don’t know what you came here intending to do, but from now on, remember one thing.*

Michael Silbert.

He was looking at me. Not with the crocodile tears he’d shed a moment ago, but with eyes lit only by ambition.

*Every choice comes with consequences to match.*

“……”

*So please, choose carefully. It will be a choice you can make only once—a choice you can never take back.*

His final warning came with a stare, and the gazes pouring in from all around were so hot that I ended up closing my eyes.

And I thought:

*Yeah. So this is how it ends up.*

*From the start…*

*There was no other way.*

I opened my eyes with a hollow emptiness inside me. At the same time, Team Leader Choi met my gaze. He read what was in my eyes and stood up.

*Rrrr.*

The chair, which had endured for ages longer than its new master, slowly scraped backward. At that moment—

“Before we elect a representative, the purpose of today’s inaugural ceremony, I must inform you that my maternal grandfather, Hunter Cheon Taemin…”

At last, the name of one man rang out. In the suffocating silence that followed, the savior’s only blood relative continued in a low voice.

“…has become seriously ill and will be unable to take part in this war.”

“……!”

“……!”

An enormous, unseen shock swept through the room.

* * *

Suffocating silence fell over the First National Assembly Hall.

In that moment, the people frozen by confusion and shock could do nothing but repeat the words they had just heard over and over in their minds.

*“My maternal grandfather, Hunter Cheon Taemin, has become seriously ill and will be unable to take part in this war.”*

A bomb had gone off barely ten minutes after the inaugural ceremony began.

No—perhaps it was a different kind of catastrophe.

*Sky is sick? What on earth does that mean?*

*How could he…? That can’t be right. It’s impossible.*

Those who rejected reality most fiercely were mostly the old-generation Hunters known as the elders.

They remembered Cheon Taemin—the great hero who had saved humanity from the Demon King—better than anyone. And so they felt the shock more deeply than anyone else.

It was only natural.

In their memories, Cheon Taemin was more than human, almost a living god.

He had single-handedly wiped out monster armies tens of thousands strong, and torn the limbs from S-rank monsters of incredible strength.

His overwhelming prowess had been matched by an equally overwhelming presence.

With Cheon Taemin at their side, they had been willing to march into the jaws of death.

They had stood shoulder to shoulder, cutting through monsters surging toward them like waves, advancing again and again.

The elders could bear to recall those horrific battlefields because Cheon Taemin had been there in their memories.

Because those memories were suffused with the shining glory of having led humanity to victory alongside him.

But he was sick?

The savior of humanity, the man who had even defeated the Demon King Asmodeus, had become too ill to take part in the war?

The shock soon gave way to a hollow sense of loss, and some of the elders even felt anger.

“What on earth—what on earth is this supposed to mean?”

“Gravely ill? Even for someone like your maternal grandfather, that’s too much to believe!”

“Explain this properly. There’s no way he could be sick!”

But contrary to the elders’ desperate wishes, Cheon Taemin’s only maternal grandson merely shook his head, calm and composed.

“Everything I’ve told you is absolutely true.”

“Young man!”

“I understand how you feel, Seniors. I felt the same way a few months ago.”

“What… what do you mean?”

“I always wondered where my grandfather was. Why he wouldn’t show himself to his only grandson for so long, no matter what the reason was.”

Choi Minwoo looked around at everyone and continued.

“I only found out after Vice Guild Master Lee Jungryong and Go Jun died. One day, for reasons unknown, he fell into a coma—a state of unconsciousness—and a tiny handful of people had been hiding the truth.”

“……!”

Another enormous shock swept through the room. But the silence it brought didn’t last long.

“It’s hard to believe, but it’s all true. I can vouch for it.”

At the sudden low voice, everyone’s eyes turned in one direction.

A towering Black man, who had been watching the situation in silence, was looking at them.

“Magic Johnson!”

“Y-You knew about this too?”

Magic Johnson nodded before answering.

“I came to this country a few months ago after those friends contacted me. I didn’t expect to see Sky unconscious when I got there, though.”

“Th-Then it really is…”

“That’s right. Even with all the knowledge and Magic I could draw on, I couldn’t find a way to bring him back to consciousness. Of course, I couldn’t tell anyone else. If this incredible secret got out, it would cause even greater chaos.”

People suddenly remembered the situation at the time.

The magical power readings that had begun to rise, and the strange events that had begun to occur.

In China, an Arch Lich had led a monster army and drenched Sichuan in blood. People’s anxiety had only continued to grow.

“But we can’t keep it hidden any longer. The whole world is looking for Sky now, and the World Hunter Federation, which took its first step today, has to give people the answers they want—just as the UN did.”

In that moment, one word crossed everyone’s mind.

*Leader.*

With Cheon Taemin down, they needed a new leader, one way or another.

A new hero who could fill the savior’s absence as much as possible. Someone who could win the support of a majority of the three hundred people gathered around this enormous round table.

*Then…?*

By the time most people reached that thought, they had already made up their minds.

Strength. Fame. Popularity. A spirit of sacrifice and courage. Leadership…

They each had their own standards for judging a leader. And even among those already called heroes, only a handful could meet those requirements.

And in that regard, there was one person who could not be overlooked.

Michael Silbert.

Countless eyes passed over him.

Some smiled triumphantly, as if the moment they had waited for had finally arrived. Others watched with cautious thoughtfulness.

But even with the situation turned upside down, Michael Silbert gave nothing away.

He had only one final step left to take. His thoughts were already on what came after.

*It’s sooner than I expected, but… I’ll have to get rid of him. As soon as possible.*

The absolute power of the World Hunter Federation already seemed within his grasp, but an obstacle that would keep troubling him had to be removed.

Michael Silbert fixed his sunken eyes on one man.

Even as the vote began, Jin Taekyung remained silent, his lips firmly closed. Beside him sat a blond monster with a calm expression.

* * *

I looked down at the scrap of iron in my hand and thought:

*What was this called again?*

Ostracism by lot? Ostracism by ballot?

I thought I’d heard it originated in the method used to banish tyrants in ancient Athens, but I wasn’t sure.

One thing I did know: what I held wasn’t a piece of pottery, but a fragment of a tower shield. And the person whose name appeared on the most fragments wouldn’t be banished—they’d become the leader of the World Hunter Federation.

*Would’ve been nice if it worked the other way around, huh?*

The Sound Transmission I sent off on a whim got an answer I hadn’t expected.

*What the hell are you talking about all of a sudden?*

*Just saying. Anyway, you’re answering me this time.*

*Because this will probably be the last time.*

I fiddled with the piece of iron.

*You crazy bastard. I wondered why you’d answered me, but you’re still on about that.*

*I know what you’re thinking. But that’s too…*

*Dangerous?*

After a brief silence, the Skeleton King answered.

*Yes. Even now, this body cannot be certain.*

*The odds are close to fifty-fifty. And this is only my guess, but the chance of success is a little higher.*

*Do you understand what that means? There’s a fifty percent chance you could lose everything.*

*Really? To me, it sounds like there’s a fifty percent chance I could protect everything.*

*……!*

*Trust me.*

I looked around. Familiar faces. People I could trust, right beside me. They were all my comrades, my friends.

*If you really can’t trust me, then trust us.*

This silence lasted even longer than the first. And for the first time in a long while, I was able to meet the Skeleton King’s eyes.

*Why go this far? Take that risk, even though your family and friends could get hurt?*

I answered with a truth that might have been settled the day I first met him.

*Because you’re my friend, too.*
```

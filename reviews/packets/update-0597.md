<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0597.txt",
      "sha256": "731974a99a4bd44a6fa13500066fd9252713f1aaf5c06be90e4a65b222a4854f",
      "bytes": 12687
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "c0c3f6f8697f9c229f66a7f9079119cf183733e54d80d0d41068e3ff7a6d431e",
      "bytes": 2021
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "f20dd84c382a2d5e2f89fed308e3bd004e9178b8c63d6f382c0dcbff80cfc13c",
      "bytes": 185288
    },
    {
      "path": "characters/Baek Hanseong.md",
      "sha256": "a37dfc84ec7332c8c8f11cba21309c394877f3fc12dfe692f5de356fb750fb2a",
      "bytes": 739
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "fa8376ebc82f0cc90bb918118ca470e8933472bd1cdb4854da9980a8b0003ad5",
      "bytes": 553
    },
    {
      "path": "characters/Go Jun.md",
      "sha256": "a415afb66c82793f285c58e151f98b984dd059ae0b4a6572d3556c8bb297c46f",
      "bytes": 907
    },
    {
      "path": "characters/Go Se-won.md",
      "sha256": "2c246d28ca03edf86c91da16b2b839c4eab082728ebc52d92f805d86c3c281c5",
      "bytes": 975
    },
    {
      "path": "characters/Hwa-jong.md",
      "sha256": "214e5354bd43881e32538ad20b0eb31fda12f6b4679359d83a3962519c42d1a0",
      "bytes": 646
    },
    {
      "path": "characters/Im Kkeokjeong.md",
      "sha256": "1950996fc3ef244028288af10f7bb56cd3ff7dfb10480ef89b36c6d3245ce917",
      "bytes": 1774
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "75274d1daef82b65b35d5a9724e5db942b3e3a6c634778e5c5899be7fb5b1103",
      "bytes": 1764
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "52fd8bb6efc6cfe39f746b25185eebba50fc6128d35aecbfd85f89c9c169e1ca",
      "bytes": 622
    },
    {
      "path": "characters/Kim Hwajong.md",
      "sha256": "d4b939a6f3547c80cb047e0b0a925047276b87d02fe7d3d97ffbdb8b537d7110",
      "bytes": 694
    },
    {
      "path": "characters/Song Song.md",
      "sha256": "5b3cabaa0843082d42ae3a19d16c8a2d8e248f1f09dc84ee7eb54c82be266018",
      "bytes": 939
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "d3add5e63df718f02e9a7ad4c713624df52805b73c77a2736c6929f81df9e48b",
      "bytes": 183010
    }
  ],
  "estimated_tokens": 11529
}
-->

# Durable State Update — Chapter 597

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 597. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 597. Profile updates may replace only one
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
  "chapter": 597,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 597,
    "continuity_sources": [597],
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
    "Jin Taekyung's solo assault on Ares Guild headquarters ended with Go Jun and twenty-five others dead and around five hundred casualties.",
    "Jin publicly said he had only done what he had to do, after which the Blue House halted the live broadcast.",
    "Go Se-won surrendered, subdued the remaining Go Jun loyalists, and testified that Go Jun caused the two monster waves; he is being held in a special detention center and wants to meet Jin to repay a debt.",
    "Jin awakened after two days unconscious in Team Leader Choi's mansion and has physically recovered.",
    "Kim Hwajong's death is confirmed, and Jin remains overcome by grief.",
    "President Baek Hanseong is overseeing the government's response and visited Jin at Team Leader Choi's mansion.",
    "A blond foreigner entered the mansion and announced that Jin had awakened."
  ],
  "continuity_sources": [
    596
  ],
  "open_questions": [
    "Has Choi Minwoo regained consciousness, and has Kim Hwajong's funeral begun?",
    "Who is the blond foreigner, and whom was he addressing when he announced Jin's awakening?",
    "What caused Cheon Taemin's collapse, what happened during his more than twenty years of unconsciousness, and where is he being kept?",
    "What is inside Area A, and what unidentified being was involved in Go Jun's plan?",
    "What were the functions of Song Cheonwoo's pocketed object and the black jewel in Go Jun's necklace?"
  ],
  "safe_through": 596,
  "temporary_decisions": [
    "Use Area A for A구역, Capital Defense Command for 수도방위사령부, and Ares Guild Headquarters for 아레스 길드 본사.",
    "Use Lord Fuck and Lord Sibu-leol for 시벌좌 and 시부럴좌.",
    "Use special detention center for 특별 구치소 and Team Leader Choi's mansion for 최 팀장의 저택.",
    "Use Mr. Go for 고 모씨 and Lee Kanghee for 이강희.",
    "Use Chief Editorial Writer for 주필 and the death penalty for 사형 집행 제도."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 김화종    | **Kim Hwajong**   |
| 송송이    | **Song Song**     |
| 절정     | **Peak**          |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 상태               | **Status**                     |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 길드      | **Guild**             |
| 길드장     | **Guild Master**      |
| 부길드장    | **Vice Guild Master** |
| 팀장      | **Team Leader**       |
| 백한성 | **Baek Hanseong** | Twenty-seventh President of Korea and youngest president elected in Korean history. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 고준 | **Go Jun** | Personal name of Team Leader Seok; Lee Jungryong's prized Disciple. |
| 고세원 | **Go Se-won** | Ares Guild Head of Security and Team Leader. |
| 화종 | **Hwa-jong** | Butler Kim's personal name. |
| 임꺽정 | **Im Kkeokjeong** |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 평화 | **Peace Guild** | Guild name. |
| 아레스 | **Ares Guild** | The leading Guild in Korea; formerly employed Team Leader Choi and Song Song. |
| 송이 | **Song-i** | Short form used for Song Song; Taekyung's love interest. |
| 황상 | **Emperor** | Address or reference to the reigning Emperor. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 석고준 | **Go Jun** | Source full-name form for the established Go Jun, also known as Team Leader Seok. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 경호팀장 | **Head of Security** | Go Jun's security-team office under Lee Jungryong. |
| 대통령 | **President** | Title for Korea's head of state. |
| 꺽정 | **Kkeokjeong** | Jin's injured ally, addressed as Uncle Kkeokjeong. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 임꺽정 | junior_friend | Kkeokjeong hyung | casual-but-junior | After Im asks to be called hyung. |
| 임꺽정 | 진태경 | older_friend | hyung | hearty-casual | “Call me hyung. We’re not even that far apart in age.” |
| 진태경 | 송송이 | guild_member_to_guild_member | Miss Song | formal-polite | Taekyung repeatedly uses 송이 씨 while introducing himself and attempting to court Song Song. |
| 송송이 | 진태경 | guild_member_to_guild_member | Taurus | casual-teasing | Song Song refers to Taekyung by his zodiac sign when calling him to the meal. |
| 송송이 | 임꺽정 | younger_guild_member_to_older_guild_member | Uncle | casual-polite | Song Song uses 아저씨 while asking Im Kkeokjeong to agree that Changsoo is nasty. |
| 김화종 | 진태경 | senior_Hunter_to_younger_Hunter | Mr. Jin | formal-polite | Hwajong addresses Taekyung as 진태경 씨 while proposing an exchange of stories. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 진태경 | 석고준 | returning Hunter to hostile Ares security leader | you fucking bastard | hostile and profane | Taekyung directs his final insults and challenge at Go Jun after returning alive. |
| 석고준 | 진태경 | hostile_opponents | brat | hostile and overconfident | Go Jun addresses Taekyung internally as 애송아 while launching his full-strength attack. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 중년인 | 진태경 | veteran civilian Hunter to celebrated allied Hunter | Mr. Jin | formal-polite and awed | The casualty clerk addresses Jin as 진 선생님 after Jin asks him to list Lei Fei among the dead. |
| 진태경 | 중년인 | celebrated Hunter to older fellow Hunter | sir | casual and teasing | Jin addresses the older Hunter as 아저씨 while joking with him and giving him instructions. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 고준 | 진태경 | Ares Guild combatant confronting the killer of his Master | you | hostile and informal | Go Jun uses 너 while demanding Jin confess to Lee Jungryong's death and threatening retaliation. |
| 진태경 | 고준 | dominant adversary confronting Lee Jungryong's Disciple | you | contemptuous and informal | Jin uses 너 and 놈 while overpowering Go Jun and ordering him to end the conflict with Lee Jungryong. |
| 진태경 | 대통령 | Hunter_to_President | Mr. President | formal-polite | Taekyung addresses the President respectfully during their airport greeting. |
| 대통령 | 진태경 | President_to_Hunter | Mr. Jin Taekyung | formal-polite | The President addresses Taekyung by name at the airport photo line. |
| 석고준 | 고세원 | Ares Vice Guild Master to Head of Security | you | curt and informal | Go Jun tells Go Se-won that he is later than usual when Se-won enters the wrecked office. |
| 고세원 | 석고준 | subordinate_to_Vice_Guild_Master | Vice Guild Master | formal-deferential | Uses 부길드장님 while trying to stop Go Jun from watching the broadcast. |
| 팀장 | 중년인 | Hunter_team_leader_to_stranger | Boss | casual and polite | The Team Leader mistakes disguised Song for an ordinary raid customer and warns him not to proceed. |
| 고세원 | 경호팀 | security-team commander to subordinate unit | Security Team | terse operational command | Calls the unit over radio before requesting status reports. |
| 고세원 | 진태경 | Ares security leader to hostile invading Hunter | you | calm, resigned, and confrontational | Go Se-won asks Jin whether he was looking for him and negotiates with him after losing the fight. |
| 진태경 | 고세원 | invading Hunter to hostile Ares security leader | Go Se-won | direct, questioning, and threatening | Jin calls Go Se-won's name, demands Go Jun's location, and questions why Go Se-won considers the day his last day at work. |
| 진태경 | 김화종 | younger_ally_to_older_butler | Butler Kim | respectful and formal | Asks about Kim Hwajong before entering the morgue and later bids him farewell. |

## Listed compact profiles

### Baek Hanseong.md

# Baek Hanseong (백한성)

- **Safe through:** Chapter 596
- **Aliases:** None
- **Role:** Twenty-seventh President of Korea and the youngest president elected in Korean history; leads the government's public response to the Mutated Gate crisis and supports Jin Taekyung in public appearances.
- **Personality:** Confident, politically shrewd, composed, and willing to needle Lee Jungryong while advancing his anti-Ares stance.
- **Voice:** Polite, self-assured, calm, and lightly teasing.
- **Relationships:** Political counterpart to Lee Jungryong; seeks to bring Jin Taekyung and Choi Minwoo into his camp to restrain Ares Guild and secure continued political power.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 595
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Go Jun.md

# Go Jun (고준)

- **Safe through:** Chapter 596
- **Aliases:** Team Leader Seok
- **Role:** Go Jun was Ares Guild's Vice Guild Master, Lee Jungryong's Disciple and former Head of Security, the de facto successor to Lee's Ares legacy, and a mutated monster who was killed by Jin Taekyung in Area A.
- **Personality:** Disciplined and controlled under ordinary pressure, fiercely loyal to Lee Jungryong, but consumed by humiliation and rage when Ares Guild's authority is challenged.
- **Voice:** Dry, controlled, and formal with subordinates; deferential when addressing his Master.
- **Relationships:** Go Jun inherited Lee Jungryong's Ares legacy after becoming his Disciple, regards Jin Taekyung and Choi Minwoo as enemies, and now threatens Jin's family and Peace Guild allies while wielding power absorbed from an S-grade Magic Gem.

### Go Se-won.md

# Go Se-won (고세원)

- **Safe through:** Chapter 596
- **Aliases:** Head of Security
- **Role:** Go Se-won is Ares Guild's Head of Security and a Team Leader who surrendered after Go Jun's death, subdued the remaining loyalist executives, and gave decisive testimony that Go Jun caused the two monster waves, helping clear Jin Taekyung of most charges.
- **Personality:** Weary after thirty years of serving Ares as a hunting dog, he is morally conflicted but decisive when he finally breaks with the Guild's loyalists.
- **Voice:** Calm and deferential toward superiors, but blunt and decisive when issuing orders.
- **Relationships:** He formerly served Vice Guild Master Go Jun and commands Ares Guild's security forces; after Go Jun's death, he turns the gathered members against the loyalist executives and lets Jin Taekyung pass, while his wife and four-year-old child remain outside the conflict.

### Hwa-jong.md

# Hwa-jong (화종)

- **Safe through:** Chapter 596
- **Aliases:** Butler Kim
- **Role:** Hwa-jong was Choi Minwoo's loyal butler and personal escort who sacrificed his life to restrain Behemoth and died after Jin Taekyung killed it.
- **Personality:** Loyal, vigilant, and uncompromising toward perceived threats to Choi Minwoo.
- **Voice:** Formal and deferential toward Choi Minwoo, cold and openly hostile toward Song Cheonwoo.
- **Relationships:** Hwa-jong serves Choi Minwoo and was formerly close to Song Cheonwoo, but their relationship ended over loyalty and ambition.

### Im Kkeokjeong.md

# Im Kkeokjeong (임꺽정)

- **Safe through:** Chapter 595
- **Aliases:** Im Hyeokjun; Kkeokjeong hyung; Uncle Kkeokjeong
- **Role:** D-rank Hunter and veteran tank in the Peace Guild; after recovering from the Black Hunters’ attack and having both arms reattached, he continues as a Hunter while nearing the end of rehabilitation.
- **Personality:** Good-natured, sociable, modest about his family, and shamelessly confident about their age difference
- **Voice:** Hearty, casual, teasing, and quick to laugh
- **Relationships:** An old acquaintance of Jin Taekyung from the Ilsan manpower office; calls Taekyung his little brother, recommends him to Team Leader Choi, and remembers that Taekyung protected him during an E-Rank Gate attack; married with two children

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 596
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, a Supreme Peak master with the Heavenly Martial Physique and Force, publicly recognized as an S-rank-level Hunter while formally retaining an A-rank license, who defeated Go Jun at Ares Guild headquarters and has awakened after two days unconscious.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor and assigned him a final task to incorporate martial principles into his learned martial arts but declined Taekyung's recruitment after Cheongpung reached him first, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate, student, and trusted manager of media and official arrangements, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, and Xiao Shen regards him as an older brother after Jin saved him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 596
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Kim Hwajong.md

# Kim Hwajong (김화종)

- **Safe through:** Chapter 596
- **Aliases:** Butler Kim
- **Role:** Kim Hwajong was a Level 80 mage known as Butler Kim and Choi Minwoo's loyal butler and personal escort who sacrificed his life to restrain Behemoth and died after Jin Taekyung killed it.
- **Personality:** Gentle and composed as Butler Kim, but retains a fiery temperament and a habit of swearing.
- **Voice:** Gentle and measured
- **Relationships:** Kim Hwajong formerly instructed Im Chunsoo, who remains terrified of and obedient to him, and serves Choi Minwoo as butler and personal escort, having become Choi's only family.

### Song Song.md

# Song Song (송송이)

- **Safe through:** Chapter 595
- **Aliases:** Miss Song
- **Role:** Founding member of the Peace Guild; B-rank healer whose buff magic is powerful enough to be mistaken for an A-rank healer's; Healer Team Leader and temporary head of the Peace Guild's emergency rescue team, which is piloting free public-safety rescues for medium- and low-grade Gates in the capital region.
- **Personality:** Calm, practical, capable, and attentive; speaks briefly and handles domestic work with practiced skill
- **Voice:** Calm, concise, polite, and capable of devastatingly blunt candor
- **Relationships:** Works alongside Team Leader Choi, Butler Kim, Im Kkeokjeong, and Jin Taekyung as a member of the Peace Guild; Jin recruited her to help run its emergency rescue team, while she remains his same-age friend and guildmate after rejecting his confession.

## Korean source

```text
＃597화



지금껏 내가 걸어온 길에는 숱한 죽음과 비명이 내리깔려 있었다.

하지만 단언컨대, 그 어느 때보다 지금처럼 조용하고 숨 막히는 슬픔을 느낀 적은 없었다.

툭. 투두둑.

고요함 너머로 세찬 비바람이 창문을 두드린다.

해야 할 이야기는 이미 한참 전에 끝났지만, 단둘만이 있는 방 안에는 침묵만이 감돌았다.

고개를 돌린 채 하염없이 창밖만 바라보던 최 팀장이 문득 입을 열었다.

“일곱 살 때였을 겁니다. 김 집사님께서 제게 오신 것이.”

기억마저 흐릿한 어린 시절. 그로부터 자그마치 이십 년이 넘는 세월이 흘렀다.

갑작스럽게 부모를 잃은 어린아이는 청년이 되었고, 집사의 머리에는 서리가 내려앉았다.

“이제는 부모님의 목소리마저 흐릿한데, 그분과의 기억은 모든 것이 선명합니다.”

부모가 죽고, 하나뿐인 외조부조차 모습을 감췄을 때, 그의 곁에는 언제나 김 집사가 있었다.

“어느 날 문득 깨달았습니다. 제가 받아 온 그 헌신의 크기와 무게는 가늠할 수 없을 만큼 크다는 것을. 그런데…….”

흐릿해지는 말꼬리와 함께 최 팀장이 고개를 돌린다.

오랫동안 비가 쏟아지는 창밖을 바라보아서일까, 나를 바라보는 그의 눈은 어느새 빗물로 흠뻑 젖어 있었다.

“이제는 돌려줄 수 없게 되었습니다. 앞으로도 영원히.”

툭. 투둑.

그를 알게 된 이후로 처음 보는 모습이었다.

먹먹하게 가라앉은 음성과 함께, 볼을 타고 굴러떨어진 눈물이 새하얀 이불 위로 떨어진다.

아니, 이건 비바람이 창문을 두드리는 소리다. 적어도 지금만큼은 그렇게 생각하기로 했다.

“진태경 씨.”

나는 대답 대신 고개를 끄덕였다.

누구보다 김 집사와 오랜 시간을 함께했던 최 팀장이다. 앞서 내가 느꼈던 슬픔은, 지금 그가 품고 있을 감정에 비하면 아무것도 아니었다.

‘가족이 죽었으니까.’

최 팀장에게 있어 김화종은…… 집사가 아니라 가족이었다. 홀로 남겨진 아이의 곁에 남아 유일한 버팀목이 되어 주었던 가족.

그러니 왜 그를 살리지 못했냐며 나를 원망해도 좋고, 멱살을 잡고 욕을 퍼부어도 괜찮다.

지금은 그래도 된다. 차오르는 것을 말없이 눌러 담는 것보다 넘치는 만큼 쏟아내는 것이 좋다.

나는 최 팀장이 목 끝까지 차오른 감정에 잠겨 허우적거리는 것을 원치 않았다.

그리고 다음 순간. 최 팀장의 한 마디가 귓가를 파고들었다.

“감사합니다.”

“……!”

“그분의 마지막을 지켜 주셔서, 제가 하지 못한 일을 해 주셔서…… 진심으로 감사합니다.”

문득 말문이 막혔다. 뭐라 대답하고 싶었지만, 속에서 차오른 무엇인가가 목에 자물쇠를 채운 기분이었다.

나는 한참 동안 말없이 최 팀장을 바라보다 간신히 목소리를 끄집어냈다.

“최 팀장님.”

말을 잇기도 전에 그가 작게 고개를 저었다.

“저는 괜찮습니다. 정말로.”

뻔히 보이는 거짓말이었고, 알면서도 속아 줄 수밖에 없는 거짓말이었다.

달싹이려던 입술을 굳게 닫은 내게 최 팀장이 희미한 웃음을 지어 보였다.

“못 볼 꼴을 보여 드린 것 같아 민망하군요. 잠시 혼자 시간을 가져도 괜찮겠습니까?”

지금의 그에게 무슨 말을 더 해 줄 수 있을까. 나는 그럴 능력도, 자격도 없는 사람이다.

최 팀장에게는 아직 시간이 필요했다.

혈육이나 다름없던 한 사람의 죽음을 받아들일 시간. 그리고 그의 시신을 마주할 용기를 얻는 시간이.

“그럼 푹 쉬고 계세요. 대기 중인 인원들이 있으니 필요한 게 있으면 언제든지 호출하시고.”

애써 밝게 대답한 나는 자리에서 일어나 문으로 향했다.

그리고 문고리에 손을 얹는 순간, 그에게 해 주고 싶은 마지막 말이 생각났다.

“최 팀장님.”

“네?”

“가끔은 흔들려도 괜찮습니다. 소리 내서 울어도 아무도 듣지 못할 겁니다. 그분을 제외하고는.”

“……!”

“이만 가 보겠습니다.”

이미 돌아서 있던 탓에 내 말을 들은 그가 어떤 감정을 느꼈을지, 어떤 표정을 짓고 있을지는 모르겠다.

하지만 그래서 다행이었다.

달칵.

방을 나와 문을 닫은 그 순간, 그 틈새 너머로 미약한 흐느낌이 들려왔으니까.

그건 내가 지금껏 들은 것 중 가장 조용하고 슬픈 흐느낌이었고, 어떤 상황에서도 흔들리지 않았던 한 사람이 무너지는 소리였다.

“태경아, 최 팀장 상태는 어떻…….”

한 사람의 흐느낌은 나만 들을 수 있는 것이 아니었다.

방에서 빠져나온 내게, 걱정스러운 표정으로 묻던 임꺽정이 문득 입을 다물었다.

그와 함께 복도에서 기다리고 있던 다른 두 사람도 마찬가지였다.

“아. 피곤해. 커피나 한잔 마셔야겠다.”

기지개를 쭉 켠 송송이는 빠른 걸음으로 사라졌고, 나와 눈이 마주친 스켈레톤 킹은 턱을 긁적이며 말했다.

“이 몸도 그, 뭐냐. 커피나 마시러 가야겠다. 요새 통 잠을 못 잤더니 쓰러질 것 같아서…….”

“어? 어어. 나도.”

임꺽정은 그렇다 치고. 언데드 몬스터가 졸려서 커피를 마신다니, 그 말도 안 되는 핑계에 실소를 흘린 나는 녀석의 어깨를 툭툭 두드렸다.

“내 것도 한 잔 타 와.”

“빌어먹을 인간 같으니. 네놈은 손이 없냐, 발이 없냐?”

“대신 창이 있지.”

내 대답에 잠시 침묵하던 스켈레톤 킹이 눈에 힘을 주며 말했다.

“……블랙?”

“믹스.”

“커피 맛도 모르는 놈. 특별히 이번 한 번만 타다 준다. 이번 한 번만.”

욕설을 구시렁거리는 녀석의 뒤를 따라 임꺽정마저 복도를 떠났을 때. 멀리서부터 구둣발 소리가 울려 퍼졌다.

저벅. 저벅.

모습을 드러낸 것은 검은 정장을 차려입은 세 명의 사내였다.

긴 호흡과 절제된 걸음걸이에서 그들이 잘 훈련받은 절정 고수, 아니 A급 헌터라는 것이 느껴졌다.

하지만 이 저택에 발을 디뎠다는 사실 하나만으로도 그들은 평범한 헌터가 아니었고, 길드와는 전혀 다른 성질의 단체에 소속되어 있었다.

“처음 뵙겠습니다, 진태경 헌터님.”

나는 대답 대신 그들을, 아니 그들이 착용한 넥타이핀을 바라보았다.

흑색과 금색이 섞인 배지에는 무궁화와 함께 깨알 같은 글씨가 음각되어 있었다.



[대통령 경호실]



이들이 누구의 지시에 따라 움직이는지는 분명하다.

작게 고개를 끄덕인 내가 입을 열었다.

“백한성 대통령님께서 절 찾으시나 보죠?”

선두에 선 경호원이 군인처럼 딱딱한 말투로 대답했다.

“아닙니다. 각하께서는 30분 전 떠나셨습니다. 정무에 바빠 말없이 떠나야 했던 점, 넓은 마음으로 양해해 달라 하셨습니다.”

방 안에서의 시간이 길어지자 이미 떠난 모양이다. 충분히 그의 상황을 이해하기에 유감 따위는 없었다.

“양해는 무슨. 괜찮습니다. 안 그래도 저 때문에 열 배는 바빠지셨을 텐데.”

“…….”

“……스무 배?”

“크흠.”

“커흐흠.”

차마 말은 못 하고 헛기침만 연발하는 경호원들을 보아하니 오지게 바빠진 건 확실히 알겠다.

아직 바깥 상황을 확인해 보지는 않았지만, 이틀 전의 사건으로 국내뿐만 아니라 전 세계가 뒤집혔을 것이다.

‘충분히 그러고도 남지.’

하루 동안 연달아 터진 몬스터 웨이브도 사상 초유의 사태지만, 그것이 인위적으로 발생한 현상이며 아레스 길드의 부길드장이 이 모든 사태의 주범이라는 건 핵폭탄 이상의 파괴력을 지녔다.

이번 사건의 여파가 얼마나 크고 거대할지, 상황을 잘 모르는 나로서도 쉽게 짐작이 되질 않았다.

“그런데, 그 말씀을 전해 주려고 지금까지 남아 계셨던 겁니까?”

“음. 꼭 그런 것만은 아닙니다.”

“그럼…….”

말꼬리를 흐리는 내게, 세 사람이 정중히 고개를 숙였다.

“대통령 각하의 지시로 진태경 헌터님, 그리고 가족분들의 임시 경호를 맡게 되었습니다. 비록 표면상으로는 감시 역이라 알려졌지만, 편히 생각해 주시길 바랍니다.”

“감시 역?”

“이번 사태가 진정될 때까지만입니다. 아직 이틀밖에 지나지 않았고, 현 상황으로서는 진태경 헌터님께서도 불구속 입건 상태라 말입니다.”

불구속 입건이라. 감시 역과 마찬가지로 썩 좋은 어감은 아니다.

어릴 때부터 고위 정치인들, 재벌 회장님들이 사고만 쳤다 하면 저 타이틀을 들고 나왔기 때문에 익숙하기는 했다.

‘그나마 불구속 입건이라 다행인 건가.’

불구속 입건은 피의자 혹은 피고인에게 신체의 자유를 보장하지만, 사법 기관에서 사건접수가 진행되었다는 뜻이다.

“혐의가 뭡니까?”

“다른 부분은 정상 참작이 가능한 범위이긴 한데…… 아무래도 현재로서는 상해에 관련된 부분이 가장 큽니다.”

가장 상급자로 보이는 경호원이 경의와 두려움이 반쯤 뒤섞인 눈빛으로 말을 덧붙였다.

“이미 알고 계시겠지만, 진태경 헌터님께서 직접 상해를 가하여 크고 작은 부상을 입힌 사상자만 오백여 명이 넘습니다.”

“아.”

“물론 크게 걱정하지 않으셔도 됩니다. 현재 국내외의 분위기나 사건 당시의 정황상 정당방위가 성립될 가능성이 높습니다.”

어느 정도의 처벌은 예상했지만, 내가 처한 상황은 생각보다 훨씬 긍정적이었다.

진실이 밝혀짐과 동시에 국내는 물론 해외에서도 내가 행한 일의 정당성을 인정하는 분위기가 조성되었고, 사망한 석고준은 세계가 인정하는 씨발놈으로 우뚝 섰다는 것이 요지였다.

‘바로 감방 들어가는 건 아닌가 싶었는데.’

아레스 길드 본사로 향하기 직전, 혹여 피해가 갈까 평화 길드에서 탈퇴 의사를 밝힌 것이 무색해질 만큼 상황은 긍정적이었다.

물론 이 모든 것의 시작에는 김화종의 죽음이 있었으니 결코 긍정적이라 할 수 없었지만.

그리고…….

‘이 정도로 주위 상황이 빠르게 진정된 건, 아무래도 확실한 증언 덕분이었겠지.’

문득 한 시간 전쯤 백한성 대통령과 나누었던 대화가 생각난다.

수많은 카메라와 마이크 앞에서도 담담했던 사진 속 중년인의 얼굴도.

‘고세원.’

백한성 대통령이 전해 준 바에 의하면, 특별 구치소에 수감되어 있는 그는 나와의 만남을 바란다고 했다. 갚아야 할 빚이 있다는 말과 함께.

‘갚아야 할 빚이라. 도대체 뭐지?’

비록 짧은 만남이었지만, 내가 느낀 고세원이라는 사람은 단순한 인사치레를 주고받기 위해 그런 요청을 할 만한 인물이 아니었다.

설령 내 짐작이 틀렸다 하더라도 한 번쯤은 만나 이야기를 나누어야 한다.

그는 자신이 가진 모든 것을 버리고 진실을 밝혔으니까.

고세원이 경호팀장까지 오르며 저질렀을 숱한 범죄는 씻을 수 없는 과오(過誤)지만, 내가 그에게 빚을 진 것 또한 틀림없는 사실이었다.

내가 경호원들을 앞에 둔 채 잠시 고민에 잠겨 있던 그때, 복도 끝에서 스켈레톤 킹이 건들거리는 걸음으로 나타났다.

“커피 가져왔다. 처먹어.”

김이 모락모락 피어오르는 믹스 커피를 바라보던 나는, 마침내 짧은 고민을 끝내고 입을 열었다.

“안 먹어.”

“……이런 개 같은 인, 놈을 봤나.”

나는 으르렁거리는 녀석을 뒤로하고, 경호원들을 향해 말했다.

“갑시다. 안내해 주세요.”

“예?”

“고세원이요. 지금 특별 구치소에 수감되어 있다던데.”

잠시 어리둥절한 표정을 짓던 경호원들이 고개를 끄덕였다.
```

## Final English reading copy

```markdown
# Chapter 597

The path I had walked until now had been strewn with countless deaths and screams.

But I could say this with absolute certainty: I had never felt a sorrow as quiet and suffocating as this.

*Tap. Tap-tap.*

Beyond the silence, fierce wind and rain beat against the window.

The conversation we needed to have had ended a long time ago, but silence still lingered in the room where only the two of us remained.

Team Leader Choi, who had been staring endlessly out the window with his head turned away, suddenly opened his mouth.

“It must have been when I was seven. That was when Butler Kim came to me.”

His memories of childhood were already hazy. More than twenty years had passed since then.

The child who had suddenly lost his parents had grown into a young man, while frost had settled in the butler’s hair.

“I can barely remember my parents’ voices anymore, but every memory I have with him is vivid.”

When his parents died and even his only maternal grandfather disappeared, Butler Kim had always remained by his side.

“One day, I suddenly realized that the devotion I had received from him was too great and too heavy to measure. But…”

Team Leader Choi’s words trailed off, and he turned his head.

Perhaps because he had been staring out at the rain for so long, his eyes were now soaked with something that looked like rainwater as he gazed at me.

“Now I can’t give anything back to him. I never will.”

*Tap. Tap-tap.*

It was the first time I had seen him like this since I met him.

Along with his muffled, sunken voice, a tear rolled down his cheek and fell onto the snow-white blanket.

*No. That was the sound of the rain and wind beating against the window.*

At least for now, I decided to think of it that way.

“Mr. Jin.”

I nodded instead of answering.

Team Leader Choi had spent more time with Butler Kim than anyone else. The sorrow I had felt earlier was nothing compared to what he must have been carrying now.

*Because he’d lost someone who was family.*

To Team Leader Choi, Kim Hwajong had been… not a butler, but family. The family who had stayed beside a child left alone and become his only support.

So it would have been all right if he blamed me for failing to save him, or grabbed me by the collar and hurled abuse at me.

He was allowed to do that now. It was better to let everything spill out than to silently force down everything rising inside him.

I didn’t want Team Leader Choi to flounder beneath the emotions surging up to his throat.

And then, the next moment, one of his words pierced my ears.

“Thank you.”

“……!”

“For watching over his final moments. For doing what I couldn’t… I sincerely thank you.”

I was suddenly unable to speak. I wanted to answer him, but something rising inside me seemed to have locked my throat shut.

I stared at Team Leader Choi in silence for a long time before finally forcing out my voice.

“Team Leader Choi.”

Before I could continue, he gave a small shake of his head.

“I’m all right. Really.”

It was an obvious lie, and one I had no choice but to accept despite knowing it was a lie.

As I firmly closed my lips, which had been about to move, Team Leader Choi gave me a faint smile.

“I’m embarrassed that I showed you such an ugly side of me. Would it be all right if I spent some time alone?”

What more could I say to him now? I didn’t have the ability—or the right—to do so.

Team Leader Choi still needed time.

Time to accept the death of someone who had been like blood family to him. Time to find the courage to face his body.

“Then get plenty of rest. There are people waiting outside, so call for us anytime if you need anything.”

I answered as brightly as I could, rose from my seat, and headed for the door.

Then, just as I placed my hand on the doorknob, I thought of one last thing I wanted to tell him.

“Team Leader Choi.”

“Yes?”

“It’s all right to lose your balance sometimes. You can cry out loud. No one will hear you. Except for him.”

“……!”

“I’ll be going now.”

Since my back was already turned, I didn’t know what he had felt upon hearing my words or what expression he had made.

But that was probably for the best.

*Click.*

The moment I left the room and closed the door, I heard a faint sobbing through the gap.

It was the quietest and saddest sob I had ever heard—a sound that belonged to one person collapsing after never once wavering, no matter the situation.

“Taekyung, how is Team Leader Choi doing—”

A person’s sobs weren’t something only I could hear.

Im Kkeokjeong, who had been asking me with a worried expression after I stepped out of the room, suddenly closed his mouth.

The other two people waiting in the hallway with him did the same.

“Ah. I’m tired. I should go have some coffee.”

Song Song stretched widely and disappeared with quick steps. The Skeleton King, whose eyes met mine, scratched his chin and spoke.

“This body also, what was it? I should go have some coffee. I haven’t slept properly lately, and I feel like I’m going to collapse…”

“Huh? Uh, yeah. Me too.”

Im Kkeokjeong was one thing. But an undead monster claiming he was sleepy and needed coffee was such an absurd excuse that I let out a quiet laugh and patted his shoulder.

“Make one for me, too.”

“You miserable excuse for a human being. Do you have no hands or feet?”

“I do have a spear.”

The Skeleton King fell silent for a moment at my answer, then narrowed his eyes.

“……Black?”

“Mix.”

“You don’t even know how coffee is supposed to taste. I’ll make it for you this once. Just this once.”

By the time Im Kkeokjeong had left the hallway after the Skeleton King, who continued grumbling curses under his breath, the sound of dress shoes echoed from the distance.

*Step. Step.*

Three men dressed in black suits appeared.

Their long breaths and measured strides told me that they were well-trained Peak masters—or rather, A-rank Hunters.

But the mere fact that they had set foot in this mansion meant they weren’t ordinary Hunters. They belonged to an organization with a completely different nature from a Guild.

“Pleased to meet you, Hunter Jin Taekyung.”

Instead of answering, I looked at them—or rather, at the tie pins they wore.

The badge, made up of black and gold, bore a hibiscus along with tiny engraved letters.



**President’s Security Service**



It was obvious whose orders they were following.

I gave a small nod and opened my mouth.

“President Baek Hanseong was looking for me?”

The security officer at the front answered in a stiff, military tone.

“No, sir. His Excellency left thirty minutes ago. He asked that you kindly understand that he had to leave without saying goodbye because he was busy with state affairs.”

It seemed he had already left after the time in the room grew longer. I understood his situation well enough that I felt no regret.

“What’s there to understand? It’s fine. I’m sure the President is already ten times busier because of me.”

“……”

“Twenty times?”

“Ahem.”

“Cough.”

Judging by how the security officers could do nothing but repeatedly clear their throats, it was clear that they had become damn busy.

I hadn’t checked on the situation outside yet, but the incident two days ago must have turned not only Korea but the entire world upside down.

*And no wonder.*

The monster waves that had erupted one after another in a single day were an unprecedented catastrophe in themselves. But the fact that they had been artificially caused, and that the Vice Guild Master of Ares Guild was the mastermind behind everything, carried more destructive power than a nuclear bomb.

Even I, who knew little about the situation, couldn’t easily guess how large and far-reaching the aftermath of this incident would be.

“By the way, did you stay here this whole time just to deliver that message?”

“Hmm. It isn’t only that.”

“Then…”

As my words trailed off, the three men bowed politely.

“By order of His Excellency the President, we have been assigned to provide temporary security for Hunter Jin Taekyung and your family. Although we have been described as a surveillance detail on the surface, we ask that you put yourself at ease.”

“A surveillance detail?”

“This will only continue until the current situation has settled down. It has only been two days, after all, and under the current circumstances, Hunter Jin Taekyung remains a suspect who has been booked without detention.”

*Booked without detention.* Like *surveillance detail*, it wasn’t exactly a pleasant term.

I was familiar with it because whenever high-ranking politicians or chaebol chairmen got into trouble, those were the kinds of titles that appeared in the news.

*At least it’s only a booking without detention.*

Being booked without detention meant that the suspect or defendant’s physical freedom was guaranteed, while the case itself had been formally registered with the judicial authorities.

“What are the charges?”

“The other matters fall within the scope of extenuating circumstances, but… at present, the most serious issue is the bodily harm you inflicted.”

The security officer who appeared to be the highest-ranking among them continued, his eyes filled with an equal mixture of respect and fear.

“As you already know, more than five hundred casualties suffered large or small injuries directly inflicted by Hunter Jin Taekyung.”

“Oh.”

“Of course, you don’t need to worry too much. Given the domestic and international atmosphere and the circumstances at the time of the incident, there is a strong possibility that self-defense will be recognized.”

I had expected some degree of punishment, but the situation I was in was far more positive than I had anticipated.

As the truth came to light, the mood both in Korea and abroad had shifted toward acknowledging the legitimacy of my actions. Meanwhile, the dead Go Jun had risen to become a universally recognized fucking bastard.

That was the gist of it.

*I thought I might be going straight to prison.*

Right before heading to Ares Guild Headquarters, I had withdrawn from Peace Guild out of concern that my actions might cause trouble for them. That decision now seemed almost pointless, given how positively things had turned out.

Of course, none of this could truly be called positive, considering that it had all begun with Kim Hwajong’s death.

And then…

*The reason the situation around me settled down so quickly must have been the decisive testimony.*

I suddenly remembered the conversation I had shared with President Baek Hanseong about an hour earlier.

I also remembered the middle-aged man’s face in the photograph—a face that had remained composed even in front of countless cameras and microphones.

*Go Se-won.*

According to what President Baek Hanseong had told me, he was being held in a special detention center and wanted to meet me.

He had said that he had a debt to repay.

*A debt to repay. What the hell was that supposed to mean?*

Although our meeting had been brief, the Go Se-won I had seen didn’t seem like the kind of person who would make such a request merely to exchange empty courtesies.

Even if my guess was wrong, I needed to meet him at least once and talk.

He had thrown away everything he had to reveal the truth.

The countless crimes Go Se-won must have committed while rising to become Head of Security could never be washed away, but it was also an undeniable fact that I owed him a debt.

As I stood in thought in front of the security officers, the Skeleton King appeared at the end of the hallway with a swaggering gait.

“I brought your coffee. Drink it.”

I stared at the steaming cup of instant-mix coffee. At last, I finished my brief deliberation and opened my mouth.

“I’m not drinking it.”

“……You shitty hu—bastard.”

I ignored the growling Skeleton King and spoke to the security officers.

“Let’s go. Show me the way.”

“Pardon?”

“Go Se-won. I heard he’s being held in a special detention center right now.”

The security officers looked momentarily bewildered, then nodded.
```

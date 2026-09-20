<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0581.txt",
      "sha256": "72293c2fb5305753595d168172dce6c729fdac72c8be520a23429d6a0998d04a",
      "bytes": 14097
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "322c420d4b6c81f0ee7328a40600b4dc9c5c03fa21cec625bf3561c0b45e7e96",
      "bytes": 2358
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "8f0f60059c2ed27221697ecd5b6a8dd88f3d0510bf606b931fcc96d9da35c31f",
      "bytes": 182517
    },
    {
      "path": "characters/Cheonwoo.md",
      "sha256": "fa4956ce7b03203c11b793797322c4b55e3b49baf9a4ed0b3419e00593f71c1e",
      "bytes": 590
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "7ab40a4adaa455de1dcd808d2034de19409bab0a0a22086b2d48b03f0c9620b2",
      "bytes": 553
    },
    {
      "path": "characters/Go Jun.md",
      "sha256": "90d09bd1021cb044c88a207db6fa476d21229b16fcb906a7ff0fc5455917cbe4",
      "bytes": 1030
    },
    {
      "path": "characters/Hwa-jong.md",
      "sha256": "48f02eb74d8d2e562e67ced26b35629c0122e16201ea635d5c8ab1755ebcc5c5",
      "bytes": 562
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "726f82c6062b3789e9a44a93e3693b630b9846b4338ad8844cf921fc7a6157f0",
      "bytes": 2280
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "a4ffa8c607d0f207121c9f3a39a935eadfef728056a49bb3def66d7d5c30bd1a",
      "bytes": 622
    },
    {
      "path": "characters/Kim Hwajong.md",
      "sha256": "5f74151db91a6d65d14b3ee9b61fc9891d73cba16f8d735b8c060f04dfe4a517",
      "bytes": 538
    },
    {
      "path": "characters/Sohye.md",
      "sha256": "4df1b55de126371aac66ba0f97bda07151e9efe8a2186ab86853d43f1366cdf3",
      "bytes": 590
    },
    {
      "path": "characters/Song Cheonwoo.md",
      "sha256": "7dadcc3b6e24cd5586bb753b78459f3204f98e356110a67f6f2b02d4c1515b8f",
      "bytes": 1080
    },
    {
      "path": "characters/Team Leader Choi.md",
      "sha256": "68df04305346e3d3cc20b4d37b73bf097023bd5b4a46202ce05336f2d02cd589",
      "bytes": 956
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "fcc7962e4b2335e49a1fb5eadc81a1639d2b28a9061c5baa09a871712fc4ab84",
      "bytes": 179825
    }
  ],
  "estimated_tokens": 12170
}
-->

# Durable State Update — Chapter 581

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 581. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 581. Profile updates may replace only one
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
  "chapter": 581,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 581,
    "continuity_sources": [581],
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
    "Song Cheonwoo says Cheon Taemin suddenly collapsed more than twenty years ago and has remained unconscious, but no one knows why.",
    "Song Cheonwoo and Lee Jungryong concealed Taemin's condition, waited two years, conducted experiments, and purged aides who knew the truth.",
    "Hwa-jong was not told about Taemin's condition and remains loyal to Choi Minwoo.",
    "Song claims Taemin is still alive, but his location is unknown and Area A is only suspected.",
    "Choi Minwoo has confirmed Song's account enough to treat Taemin's status as genuine while continuing to investigate.",
    "Busan's Kraken has been eliminated, but more than one thousand Mermen remain across Haeundae and Gwangalli while the Peace Guild and other forces contain the disaster.",
    "Go Jun seized Song Cheonwoo's children as leverage and used the threat to force Song to attack Choi Minwoo.",
    "Go Jun used an S-grade Magic Gem to artificially cause the Busan Monster Wave and sent Kim Ho-jung to Busan.",
    "Go Jun intends to kill Choi Minwoo through Song Cheonwoo and may be relying on another unidentified being.",
    "Song Cheonwoo was killed after falling into an abyss and being attacked by an unidentified monster.",
    "The unused object in Song Cheonwoo's pocket released darkness that became light after his death."
  ],
  "continuity_sources": [
    580,
    579
  ],
  "open_questions": [
    "What caused Cheon Taemin's collapse, and what happened during his more than twenty years of unconsciousness?",
    "Is Cheon Taemin actually being kept in Area A of Ares Guild headquarters?",
    "What is the unidentified being involved in Go Jun's plan, and is it connected to the monster that killed Song Cheonwoo?",
    "What was the object Song Cheonwoo kept unused in his pocket, and what did its release of darkness and light accomplish?",
    "Can Choi Minwoo survive Go Jun's attempt to kill him?"
  ],
  "safe_through": 580,
  "temporary_decisions": [
    "Use Yeti's Winter Range for 예티의 겨울 산맥.",
    "Use Stone King for 스톤 킹 and Skeleton King for 스켈레톤 킹.",
    "Use Area A for A구역.",
    "Use Hwa-jong for 화종.",
    "Use Hero's Soul for 영웅의 혼, Yeti's Necklace for 예티의 목걸이, Hyung for 형님, and S-grade Magic Gem for S급 마정석."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 김화종    | **Kim Hwajong**   |
| 최민우    | **Choi Minwoo**   |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 상태               | **Status**                     |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 몬스터     | **monster**           |
| 레이드     | **raid**              |
| 길드      | **Guild**             |
| 길드장     | **Guild Master**      |
| 부길드장    | **Vice Guild Master** |
| 팀장      | **Team Leader**       |
| 마정석     | **Magic Gem**         |
| 천우 | **Cheonwoo** | Name shown in a Level Window; one of the five current Five Gates scions. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 고준 | **Go Jun** | Personal name of Team Leader Seok; Lee Jungryong's prized Disciple. |
| 화종 | **Hwa-jong** | Butler Kim's personal name. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 소혜 | **Sohye** | Name shown in a Level Window; one of the five current Five Gates scions. |
| 송천우 | **Song Cheonwoo** | Ares Guild Director, former third-ranked Korean Hunter, and longtime European regional branch director. |
| 평화 | **Peace Guild** | Guild name. |
| 아레스 | **Ares Guild** | The leading Guild in Korea; formerly employed Team Leader Choi and Song Song. |
| 성주 | **City Lord** | Official who sends the invitation for a gathering with young prodigies. |
| 기해 | **qi sea** | Name for the dantian, the place where internal energy begins and gathers. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 준이 | **Jun** | Family nickname used in the form Jun's dad. |
| 석고준 | **Go Jun** | Source full-name form for the established Go Jun, also known as Team Leader Seok. |
| 도련님 | **Young Master** | Address used for Team Leader Choi by Butler Kim. |
| 푸린 | **Furin** | Russian president mentioned in a forum headline. |
| 부산 | **Busan** | City where the Haeundae Gate crisis occurs. |
| 평창 | **Pyeongchang** | Location in Gangwon Province where the Gate is situated. |
| 예티 | **yeti** | Monster species in the Gate's name and raid dialogue. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 김화종 | 진태경 | senior_Hunter_to_younger_Hunter | Mr. Jin | formal-polite | Hwajong addresses Taekyung as 진태경 씨 while proposing an exchange of stories. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 석고준 | 최민우 | Ares security leader to rival Guild Master | Team Leader Choi Minwoo | formal but barbed | Uses 평화 길드 최민우 팀장님 while belittling Choi and blaming the Peace Guild for Taekyung's apparent death. |
| 진태경 | 석고준 | returning Hunter to hostile Ares security leader | you fucking bastard | hostile and profane | Taekyung directs his final insults and challenge at Go Jun after returning alive. |
| 석고준 | 진태경 | hostile_opponents | brat | hostile and overconfident | Go Jun addresses Taekyung internally as 애송아 while launching his full-strength attack. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 최민우 | 진태경 | trusted allied team leader to younger allied Hunter | Mr. Jin | formal-polite and concerned | Choi warns Jin about the danger of the operation and affirms his deep trust. |
| 진태경 | 최민우 | younger allied Hunter to allied team leader | Team Leader Choi | polite, familiar, and teasing | Jin jokes with Choi while acknowledging and dismissing his concern. |
| 고준 | 진태경 | Ares Guild combatant confronting the killer of his Master | you | hostile and informal | Go Jun uses 너 while demanding Jin confess to Lee Jungryong's death and threatening retaliation. |
| 진태경 | 고준 | dominant adversary confronting Lee Jungryong's Disciple | you | contemptuous and informal | Jin uses 너 and 놈 while overpowering Go Jun and ordering him to end the conflict with Lee Jungryong. |
| 팀원 | 석고준 | subordinate security-team member to security-team leader | Team Leader | fearful formal-polite | The team member repeatedly addresses Go Jun as 팀장님 while reporting the strange object. |
| 송천우 | 석고준 | adversary; captor of Song's children | you | shocked and confrontational | Song reacts directly to Go Jun's admission that he took the children. |
| 팀원 | 팀장 | team member to team leader | Team Leader Kim | casual, familiar, and dialectal | Team members use forms including 햄 and informal greetings when addressing Kim. |
| 화종 | 최민우 | butler_to_Young_Master | Young Master | formal and deferential | Butler Kim consistently addresses Choi Minwoo with the established deferential title. |
| 송천우 | 화종 | former_allies | Hwa-jong | familiar and informal | Song uses Hwa-jong's personal name, prompting Hwa-jong to reject the familiarity. |
| 화종 | 송천우 | former_allies_now_hostile | you | formal and cold | Hwa-jong challenges Song's right to expect Choi's trust and rejects their former intimacy. |
| 송천우 | 최민우 | older_former_ally_to_younger_former_ally | Minwoo | familiar and informal | Song addresses Choi by his given name while discussing the meeting place and surveillance. |
| 최민우 | 화종 | Young Master to butler | Butler Kim | formal and respectful | Choi refers to Hwa-jong as 김 집사님 while discussing the concealed truth. |
| 최민우 | 송천우 | temporary ally to rival | Regional Director | formal and cutting | Choi uses 지사장님 while condemning Song's survival and concealment. |

## Listed compact profiles

### Cheonwoo.md

# Cheonwoo (천우)

- **Safe through:** Chapter 580
- **Aliases:** None
- **Role:** One of the five current Five Gates of Shanxi scions and a First Rate martial artist present at Honghwa Inn.
- **Personality:** Pampered and contemptuous toward Cheongpung's group as part of the five scions' collective mockery.
- **Voice:** Mocking in the group's exchange; no distinct individual speech is established.
- **Relationships:** Associates with Seongryong, Myeonghwa, Sohye, and Jintae as a group of current Five Gates scions.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 580
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Go Jun.md

# Go Jun (고준)

- **Safe through:** Chapter 580
- **Aliases:** Team Leader Seok
- **Role:** Go Jun is Ares Guild's Vice Guild Master, Lee Jungryong's disciple and former Head of Security, and the de facto successor to Lee's Ares legacy who passed the S-rank Hunter qualification assessment with a very high score but lacks Lee's legitimacy.
- **Personality:** Disciplined and controlled under ordinary pressure, fiercely loyal to Lee Jungryong, but consumed by humiliation and rage when Ares Guild's authority is challenged.
- **Voice:** Dry, controlled, and formal with subordinates; deferential when addressing his Master.
- **Relationships:** Disciple and direct protégé of Lee Jungryong, Go Jun inherited Lee's Ares Guild legacy after his death, regards Jin Taekyung and Choi Minwoo as enemies seeking to take it away, has seized Song Cheonwoo's children as leverage, and used an S-grade Magic Gem to trigger the Busan Monster Wave while targeting Choi.

### Hwa-jong.md

# Hwa-jong (화종)

- **Safe through:** Chapter 580
- **Aliases:** Butler Kim
- **Role:** Hwa-jong is Choi Minwoo's loyal butler and personal escort.
- **Personality:** Loyal, vigilant, and uncompromising toward perceived threats to Choi Minwoo.
- **Voice:** Formal and deferential toward Choi Minwoo, cold and openly hostile toward Song Cheonwoo.
- **Relationships:** Hwa-jong serves Choi Minwoo and was formerly close to Song Cheonwoo, but their relationship ended over loyalty and ambition.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 580
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, a Supreme Peak master who possesses the Heavenly Martial Physique and superhuman physical strength, has manifested Force, opened his Middle Dantian, crossed the wall into true mastery, has achieved Three Flowers Gather at the Crown but not Five Qi Returning to Origin, can perceive the texture of qi well enough to sever layered magic, can resist high-level monster Fear through exceptional mental strength, is publicly recognized as an S-rank-level Hunter while formally retaining an A-rank license pending testing, can command coordinated raids against powerful monsters, serves as one of the two pavilion masters of the Alliance Leader's direct Fire Dragon Pavilion, leads its first mission to Nanman, and is the Peace Guild's wealthy patron in the modern world.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor and assigned him a final task to incorporate martial principles into his learned martial arts but declined Taekyung's recruitment after Cheongpung reached him first, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate, student, and trusted manager of media and official arrangements, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, and Xiao Shen regards him as an older brother after Jin saved him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 580
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Kim Hwajong.md

# Kim Hwajong (김화종)

- **Safe through:** Chapter 580
- **Aliases:** Butler Kim
- **Role:** Kim Hwajong is a Level 80 mage known as Butler Kim and Choi Minwoo's loyal butler and personal escort.
- **Personality:** Gentle and composed
- **Voice:** Gentle and measured
- **Relationships:** Kim Hwajong formerly instructed Im Chunsoo, who remains terrified of and obedient to him, and serves Choi Minwoo as butler and personal escort, having become Choi's only family.

### Sohye.md

# Sohye (소혜)

- **Safe through:** Chapter 133
- **Aliases:** None
- **Role:** One of the five current Five Gates of Shanxi scions and a First Rate martial artist present at Honghwa Inn.
- **Personality:** Pampered and contemptuous toward Cheongpung's group as part of the five scions' collective mockery.
- **Voice:** Mocking in the group's exchange; no distinct individual speech is established.
- **Relationships:** Associates with Seongryong, Cheonwoo, Myeonghwa, and Jintae as a group of current Five Gates scions.

### Song Cheonwoo.md

# Song Cheonwoo (송천우)

- **Safe through:** Chapter 580
- **Aliases:** Director Song
- **Role:** Ares Guild Director and former A-rank Hunter who reached third place among Korean rankers, briefly headed the Hunter training center, and led Ares Guild's European regional branch for twenty years; after being forced to attack Choi Minwoo to protect his hostage family, he fell into an abyss and was killed by an unidentified monster.
- **Personality:** Highly ambitious, honor-obsessed, politically calculating, and determined to use his final opportunity to reclaim influence before retirement.
- **Voice:** Not established.
- **Relationships:** Song Cheonwoo followed Cheon Taemin since before Team Leader Choi was born, was Lee Jungryong's former friend and rival, helped conceal Taemin's condition and purge aides who knew the truth, negotiated the European regional director position to save himself and his family, and had his children seized by Go Jun as leverage that forced him to attack Choi Minwoo.

### Team Leader Choi.md

# Team Leader Choi

- **Safe through:** Chapter 580
- **Aliases:** Choi Minwoo (최민우)
- **Role:** Team Leader Choi is Cheon Taemin's only living blood relative, a formidable aura-wielding swordsman who wields Hero's Soul, and is positioning himself to take control of the Ares Guild after Lee Jungryong's death.
- **Personality:** Strategic, candid, controlled, and possessive of the power and influence he intends to inherit.
- **Voice:** Dry, formal, and direct, with calm candor and carefully chosen metaphors.
- **Relationships:** Choi Minwoo is Cheon Taemin's maternal grandson and only living blood relative, was kept out of public knowledge by Lee Jungryong, is closely integrated with Jin Taekyung's family, seeks to acquire the Ares Guild intact, and now knows that Song Cheonwoo and Lee concealed Taemin's collapse and purged aides while he investigates Taemin's fate.

## Korean source

```text
＃581화



화륵, 콰앙!

불의 채찍이 지면을 후려쳤다. 쌓여 있던 눈이 녹고 예티의 피가 끓어오른다. 김화종의 악문 잇새로 씹어뱉는 듯한 음성이 흘러나왔다.

“송천우, 이 개새끼가…….”

노집사의 부릅뜨인 눈동자는 불과 몇 초 전까지만 해도 한 사람이 쓰러져 있던 그곳을 노려보고 있었다.

이렇게 끝날 거였다면, 놈이 이런 식의 죽음을 맞이할 거라면 자신의 손으로 죽였어야 했다. 하지만 송천우는 어디서 끌어 올렸는지 모를 마지막 힘을 발휘하여 깊은 균열 속으로 몸을 던졌고, 스스로 선택한 죽음을 맞이했다.

배반자에게는 과분한 최후다. 그리고 그보다 더욱 아쉬운 것은…….

“중요한 증인이 사라졌군요. 죄송합니다, 도련님.”

“아닙니다.”

한숨과도 같은 김화종의 중얼거림에 최민우가 고개를 저었다. 그의 시선은 도무지 깊이를 짐작할 수 없는 크레바스에 못 박혀 있었다.

“김 집사님께서 사과하실 필요 없습니다. 더 주의하지 못한 제 탓이니까요.”

승리는 경계심을 무디게 만든다. 결코 쉽지 않았던 싸움이라 더욱 그랬는지도 몰랐다. 최민우는 채 반의반도 비우지 못한 포션을 자신의 몸에 쏟아부었다.

치이익. 살이 타는 소리와 함께 조금씩 상처가 아물기 시작한다. 그는 미약한 통증을 느끼며 말을 이었다.

“아마도 송천우는 이것이 가족들을 살릴 수 있는 유일한 방법이라고 생각했던 모양입니다.”

“…….”

“상황을 이해하지 못하는 건 아니지만…… 우리가 생각했던 것 이상으로 간절했던 것 같군요.”

김화종이 거친 어조로 중얼거렸다.

“병신 같은 놈. 이렇게 한다고 가족들이 산다는 보장도 없는데 뭣 하러.”

“그만큼 두려웠던 거겠지요. 절망 속에서도 희망을 붙잡는 것이 사람 아니겠습니까.”

나직한 목소리로 대답한 최민우는 크레바스에서 시선을 뗐다. 정확한 깊이는 모르겠으나, 어림잡아도 수백 미터는 될 법한 낭떠러지다. 이미 목숨이 경각에 달려 있던 송천우가 추락에서 살아남을 가능성은 제로에 가까웠다.

“길드원들을 불러야겠습니다. 아니, 길드 하우스에 인력 파견을 지시하는 것이 빠르겠군요.”

이십 년이 넘도록 함께한 두 사람이다. 김화종은 최민우의 뜻을 즉각 알아차렸다.

“시신을 수습하실 생각입니까?”

“가능할지는 모르겠지만 시도 정도는 해 봐야겠죠. 송천우는 아직까지 아레스 길드의 유럽 총괄 지사장입니다.”

숨이 끊겼다고 해도 신분은 남아 있다. 이곳에서 벌어진 일의 절반이라도 증명할 수 있다면, 그 파장은 아레스라는 철옹성을 넘어 석고준을 뒤흔들 것이다.

“살인미수, 살인 청부, 뭐든 간에 그 아레스 길드의 부길드장이라고 해도 벗을 수 없는 오욕(汚辱)이 될 겁니다. 특히 지금 같은 상황에서는 더더욱.”

수십 년간 공들여 쌓아 올린 성은 쉽게 무너지지 않는다. 하지만 석고준은 다르다. 최민우는 모든 힘을 동원하여 그를 성주의 자리에서 끌어내릴 생각이었다.

“이제 전과는 비교도 할 수 없이 바빠질 겁니다. 저도, 김 집사님도.”

김화종이 대견함이 담긴 미소를 지었다.

“이날만을 기다렸습니다.”

“다행입니다. 김 집사님이 늘 제 옆에 계셔서.”

“도련님도 제가 더 늙기 전에 부려 먹으십시오. 석고준, 그놈이 이런 개 같은 일을 벌인 걸 후회하게 만들어 줘야죠.”

“안 그래도 그럴 생각입니다.”

고개를 끄덕인 최민우는 크레바스를 뒤로하고 걷기 시작했다. 송천우와의 격렬했던 전투 때문인지, 아니면 상당량의 피를 흘려서인지 전신을 엄습하는 피로와 함께 발걸음이 무거워졌다.

그리고 조금씩 몽롱해지던 의식 속에서, 지나온 길을 되짚어 보던 최민우의 걸음이 우뚝 멈췄다.

철벅.

눈과 피가 뒤섞인 구정물이 주위에 튀었다. 뒤따르던 김화종이 어리둥절한 목소리로 물었다.

“도련님?”

하지만 최민우는 대답하지 않았다. 혼탁한 구정물로 이루어진 웅덩이. 그 안에 반쯤 잠긴 자신의 발을 말없이 노려보다 문득 중얼거렸다.

“후회.”

“네?”

“김 집사님께서 조금 전 그러지 않으셨습니까. 석고준이 이런 개 같은 일을 벌인 것을 후회하게 해 주겠다고.”

“그랬습니다만, 그게 무슨 문제라도…….”

“‘왜’가 빠져 있었습니다. 석고준이 왜 이런 개 같은 일을 벌였는가에 대한 의문이.”

최민우는 웅덩이를 바라보며 생각했다. 한 걸음만으로도 구정물이 튀고 파문이 일어나는데, 어째서 석고준은 자신을 죽일 암살자로 아레스 길드에 속해 있는 송천우를 보냈을까.

그가 대단한 실력자라서? 아니면 배반자이기 때문에?

둘 다 틀렸다. 이건…….

‘함정.’

벼락과도 같은 그 단어가 뇌리를 스친 그때, 최민우의 몸이 파르르 떨렸다. 마침내 떠오른 깨달음으로 인한 충격 때문이 아니고, 전신을 사로잡은 피로 때문은 더더욱 아니었다.

아니, 처음부터 흔들리는 것은 그뿐만이 아니었다.

드드드득…….

서서히 잠잠해졌던 웅덩이에 또 다른 파문이 일고, 미처 녹지 않은 눈더미가 무너져 내렸다. 대지가 흔들리고 있었다. 설산 전체가 몸을 떨자 곳곳에서 겁에 질린 예티의 울음소리가 울려 퍼졌다. 그리고 이 모든 현상의 중심에, 거대한 울림이 있었다.

쩌적, 구구구구구궁!

최민우와 김화종은 약속이라도 한 것처럼 동시에 고개를 돌렸다. 엄청난 진동과 함께 거미줄처럼 갈라지는 지면. 실처럼 이어진 대지의 균열은 등 뒤의 어둠과 연결되어 있었다.

콰드득. 쩌저저적.

크레바스(Crevasse).

도무지 끝을 짐작할 수 없는 거대한 어둠이 아가리를 벌렸다. 벌어진 틈새로 흘러나온 어둠. 아니, 강대한 마력이 설산을 뒤흔들고 시공을 찢었다.

쏴아아아악!

그리고 두 사람은 볼 수 있었다.

갈라진 공간 너머, 끝없이 펼쳐진 푸른 하늘과 건물들을. 자신들이 살아왔고, 살아가야 할 세상을.

“……몬스터 웨이브(Monster Wave).”

맞닿아 있으나 이어져서는 안 될 두 세상이 연결되었다. 그 재앙의 시작을 알리는 포효가 온 사방을 울렸다.

- 그아아아아아!

마침내 모습을 드러내는 심연(深淵) 앞에서, 김화종이 그 어느 때보다 어둡게 가라앉은 눈빛으로 젊은 주인의 앞을 가로막았다.

저벅.

눈보라가 휘몰아쳤다. 마력에 의해 검게 물든 그것은 더 이상 새하얗지도, 아름답지도 않았다.



* * *



“팀장님. 한잔하시죠?”

넉살 좋게 소주병을 들고 다가오는 팀원의 모습에, 팀장은 퉁명스럽게 대답했다.

“싫어, 새꺄.”

말과는 달리 술잔은 은근슬쩍 들어 올린 상태다. 다 안다는 듯 씩 웃은 팀원이 비어 있는 술잔을 채웠다.

꼴꼴꼴. 잔에 꽉 채운 소주를 한입에 털어 넣은 팀장은 광어 회를 초장에 푹 찍어 삼켰다. 쫄깃한 식감에 기분이 조금이나마 나아졌다.

“……시바, 그래도 맛은 있네.”

“그렇죠? 여기 헌터 커뮤니티에서 유명하다니까요.”

“그래?”

“네. 검색하면 후기도 많이 올라와요. 레이드 끝내고 한잔 걸치면 최고라고.”

“그 인간들이야 레이드 끝내고 마정석도 실컷 주웠으니까 술맛이 좋겠지. 나처럼 공친 새끼는 없을 거 아냐.”

“……아이고. 팀장님 또 이러신다.”

팀장은 입맛을 다셨다. 만약 그가 길드에 소속된 입장이었다면 레이드를 공치건 빠따를 치건 별 상관없었겠지만, 프리랜서 헌터 팀을 이끄는 중이라면 이야기가 다르다. 주머니에서 쌈짓돈을 꺼내서라도 지금 주위에서 웃고 떠드는 녀석들의 일당을 챙겨 줘야 하는 것이다.

물론 넉살 좋게 다가온 이놈도 포함해서.

“팀장님. 화나신 거 아니죠?”

“됐어, 인마. 술이나 한잔 더 줘 봐.”

“옙.”

경례를 척 붙이고 열심히 술을 따르는 팀원의 모습에, 피식 웃은 팀장이 난간 밖으로 시선을 돌렸다. 비록 레이드는 무산되었지만, 얼마 전 내린 눈으로 새하얗게 물든 전경을 바라보며 술을 마시는 것도 썩 나쁘지 않았다.

‘역시 평창이 풍경은 좋아, 풍경은.’

하긴, 이러니까 주위에 스키장을 잔뜩 지었겠지.

내심 중얼거린 팀장은 연신 술잔을 비우며 주위 경관을 감상했다. 오늘도 스키장을 찾은 수많은 인파와 쉴 새 없이 오르내리는 곤돌라는 저 인간들이 얼마나 생각 머리가 없는지 여실히 보여 주었다.

“야, 웃기지 않냐?”

맹렬하게 회를 집어 먹던 팀원이 고개를 들었다.

“뭐가요?”

“산 위에는 떡하니 게이트가 있고, 마력이 7퍼센트나 증가했는데도 저 지랄을 하고 있다는 게.”

심지어 내려와서 확인해 보니 저 아래 부산에는 몬스터 웨이브가 터졌단다. 팀장은 고개를 절레절레 내저었다.

“하긴, 뭐 나 어릴 때 코로나 터졌을 때도 스키장 가던 병신들이 있었지.”

“메로나요?”

“……됐다. 그냥 마저 처먹어.”

한숨을 푹 내쉰 팀장은 다시 술잔을 털었다. 부산에서 벌어지고 있을 일을 떠올리니 가슴이 답답해져 오던 그때였다.

“어, 어어! 어어어어!”

“뭐야.”

“……쟨 또 왜 저래?”

갑작스럽게 터져 나온 외침에, 팀장은 물론이고 주위 시선이 모두 한곳으로 쏠렸다. 아까부터 뭔가를 골똘히 생각하던 20대 여자 헌터가 스마트폰을 미친 듯이 흔들고 있었다.

“와, 대박! 미쳤다! 미쳤어요!”

팀장이 걱정스러운 표정으로 대답했다.

“응. 그런 것 같긴 하다.”

“아뇨, 그게 아니라! 아까 제가 말했었죠. 위에 마스크 쓴 존잘남 어디서 본 것 같다고!”

팀장은 아까 마주쳤던 일단의 헌터들, 그중에서도 맨 뒤에 있던 한 청년을 떠올리며 입을 열었다.

“그래, 그랬지. 그 인간들 덕분에 우리는 오늘 하루 레이드 공쳤고.”

“그런데 그 사람이! 와, 진짜 대단하다. 김소혜. 눈썰미 미쳐 버린 건가? 어떻게 그걸 알아보지?”

“듣다가 미쳐 버릴 것 같으니까 제발 무슨 소린지 좀 얘기해 줄래?”

“이거 보세요, 이거!”

눈앞에 불쑥 들이밀어진 스마트폰에 눈살을 찌푸린 것도 잠시, 화면에 뜬 얼굴을 확인한 팀장이 눈을 크게 치켜떴다.

“뭐야, 이거 진짜야? 닮은 것 같긴 한데…….”

“맞다니까요! 팀장님 저 못 믿으세요?”

“응.”

“아, 씨. 이번에는 확실한 거니까 믿으세요! 제가 아이돌 덕질만 삼십 년을 하면서 길러 온 눈썰미가 있는데!”

“너 스물다섯 살이잖아. 아버지께서도 덕질 하신 거니?”

“아무튼 맞아요! 제 말이 틀리면 오늘 일당 안 주셔도 돼요!”

자본주의의 노예가 일당을 걸다니. 팀장은 그제야 믿을 마음이 생겼다. 더불어 호기심도 함께.

‘만약 이게 사실이면…… 이 정도씩이나 되는 사람이 뭐 때문에 여기까지 온 거지?’

스마트폰에는 연예인이라고 해도 믿을 만큼 잘생긴 얼굴과 함께 짤막한 기사가 떠 있었다.



[평화 길드 최민우 팀장. “긴급 구조팀은 모든 이들을 위한 것”]



거물. 그것도 엄청난 거물이다.

비록 얼굴을 제대로 보지는 못했지만, 사진으로도 느껴지는 침착한 눈빛과 특유의 분위기가 닮은 것도 같았다.

‘이게 사실이라고 치면, 다른 헌터들도 전부 평화 길드 소속이라는 건데.’

최근 들어 워낙 유명해진 인물이라 팀장도 최민우에 관한 이야기를 여러 번 들어 봤다. 하지만 그중 절반만 사실이어도 눈코 뜰 새 없이 바쁠 텐데, 길드원들을 이끌고 평창에 있는 B급 게이트 방문할 이유가 뭐란 말인가.

‘잠깐. 그럼 아까 내려오는 길에 봤던 그 아저씨도?’

문득 거기까지 생각이 미친 순간이었다.

구구구구궁!

거대한 진동이 주위를 휩쓸기 시작했다. 찰나 모든 소음이 멎고 사람들의 고개가 약속이라도 한 듯 한 방향을 향해 돌아갔다. 그리고 그중에서도 가장 빨리 이변을 알아차린 것은 팀장이었다.

진동이 울리기 직전, 그의 시선은 이미 한곳에 닿아 있었기 때문이다.

‘……저곳은…….’

기대를 안고 올라갔다가 허망하게 내려와야 했던 장소. 바로 [예티의 겨울 산맥]이라 불리는 B급 게이트.

그리고 다음 순간, 팀장의 부릅뜬 눈동자에 비친 것은 서서히 무너져 내리는 산의 일부와 그 위에 내려앉은 새카만 어둠이었다. 처참히 무너지는 곤돌라와 건물의 잔해 속에서, 정신을 뒤흔드는 끔찍한 포효가 울려 퍼졌다.

- 그아아아아아!

몬스터 웨이브. 그리고 게이트에 남아 있던 사람들.

숨 막히는 공포에 사로잡혀 있던 팀장은, 간신히 쥐어짜 낸 음성으로 외쳤다.

“신고! 당장 신고해!”

겁먹은 질문이 돌아왔다.

“어, 어디로요?”

“헌터 협회, 평화 길드, 진태경…… 어디든 당장!”
```

## Final English reading copy

```markdown
# Chapter 581

*Whump! BOOM!*

A whip of fire lashed the ground. The snow that had piled up melted, and the yeti blood began to boil. A voice that sounded as if it were chewing out the words spilled through Kim Hwajong’s clenched teeth.

“Song Cheonwoo, you fucking bastard…”

The old butler’s widened eyes were fixed on the place where someone had been lying only a few seconds ago.

If this was how it was going to end—if that bastard was going to meet a death like this—Hwajong should have killed him with his own hands. But Song Cheonwoo had summoned the last of some unknown strength, thrown himself into the deep crevasse, and met the death he had chosen for himself.

A traitor had received a far too generous end.

And what was even more regrettable was…

“We’ve lost an important witness. I’m sorry, Young Master.”

“No.”

Choi Minwoo shook his head at Kim Hwajong’s sigh-like murmur. His gaze remained fixed on the crevasse whose depth could not be estimated.

“You have nothing to apologize for, Butler Kim. It was my fault for failing to be more careful.”

Victory dulled one’s vigilance. Perhaps it was even more understandable after such a difficult battle. Choi Minwoo poured the potion—less than a quarter of which had been used—over his body.

*Hiss.*

The sound of flesh burning filled the air as his wounds began to close little by little. Feeling a faint pain, he continued.

“Song Cheonwoo must have thought this was the only way to save his family.”

“…”

“I understand his situation, but… he must have been more desperate than we realized.”

Kim Hwajong muttered in a rough voice.

“What a damn fool. There wasn’t even any guarantee his family would survive just because he did this. Why the hell would he…”

“He must have been that afraid. Isn’t clinging to hope even in the middle of despair what makes us human?”

Choi Minwoo answered in a low voice, then took his eyes off the crevasse. He did not know its exact depth, but the drop had to be hundreds of meters at the very least. Song Cheonwoo had already been on the verge of death. The odds that he had survived the fall were close to zero.

“We should call the Guild members. No—it would be faster to order the Guild House to dispatch personnel.”

The two men had been together for more than twenty years. Kim Hwajong immediately understood what Choi Minwoo intended.

“You mean to recover the body?”

“I don’t know if it will be possible, but we should at least try. Song Cheonwoo is still Ares Guild’s European regional branch director.”

Even if he had stopped breathing, his status remained. If they could prove even half of what had happened here, the repercussions would extend beyond Ares Guild’s iron fortress and shake Go Jun to his core.

“Attempted murder, murder-for-hire—whatever it is, it will be a disgrace that even Ares Guild’s Vice Guild Master cannot escape. Especially in a situation like this.”

A fortress built through decades of effort did not crumble easily. But Go Jun was different. Choi Minwoo intended to use every bit of power at his disposal to unseat him as lord of that fortress.

“From now on, we’ll be busier than ever. Both you and me, Butler Kim.”

Kim Hwajong smiled proudly.

“I’ve been waiting for this day.”

“I’m glad. That you’re always at my side.”

“You should put me to work before I get any older, Young Master. We have to make that bastard Go Jun regret starting this whole fucking mess.”

“That’s exactly what I intend to do.”

Choi Minwoo nodded and began walking away from the crevasse. Whether it was because of the fierce battle with Song Cheonwoo or the considerable amount of blood he had lost, fatigue swept through his entire body and weighed down his steps.

Then, as his consciousness gradually grew hazy and he retraced the path he had taken, Choi Minwoo came to an abrupt stop.

*Splash.*

Muddy water mixed with snow and blood sprayed around him. Kim Hwajong, who had been following behind him, asked in confusion,

“Young Master?”

Choi Minwoo did not answer. He silently stared down at his foot, half-submerged in a puddle of murky water, then suddenly muttered,

“Regret.”

“Pardon?”

“You said that earlier, Butler Kim. That we needed to make Go Jun regret starting this whole mess.”

“I did, but is something wrong…?”

“You left out the ‘why.’ The question of why Go Jun started this whole mess.”

Choi Minwoo looked down at the puddle and thought.

One step was enough to make the muddy water splash and send ripples across its surface. So why had Go Jun sent Song Cheonwoo—a member of Ares Guild—to assassinate him?

Because Song Cheonwoo was exceptionally skilled?

Or because he was a traitor?

Both were wrong.

This was…

*A trap.*

The word flashed through his mind like a bolt of lightning. Choi Minwoo’s body began to tremble.

It was not from the shock of his realization. It was even less due to the fatigue that had seized his entire body.

No. His body was not the only thing that had been trembling from the beginning.

*Rumble…*

Another ripple spread across the puddle that had slowly fallen still, and a mass of half-melted snow collapsed. The earth was shaking.

As the entire snow-covered mountain trembled, terrified yetis cried out from all around. And at the center of it all was an enormous rumble.

*Crack—RUMBLE, RUMBLE!*

Choi Minwoo and Kim Hwajong turned around at the same time, as if they had planned it.

The ground split apart like a spiderweb amid a tremendous vibration. The cracks in the earth, connected like threads, reached the darkness behind them.

*Crack! Crack-crack-crack!*

A crevasse.

An enormous darkness whose end could not be seen opened its jaws. Darkness poured from the widening gap.

No—the force flowing from it was powerful mana.

It shook the snow-covered mountain and tore through space-time.

*SHWAAAA!*

And the two men saw it.

Beyond the split in space lay an endless blue sky and buildings.

The world they had lived in—and the world they were supposed to continue living in.

“…Monster Wave.”

Two worlds that touched but should never have been connected had become linked. A roar announcing the beginning of the disaster reverberated in every direction.

—GRAAAAAAAH!

Facing the abyss as it finally revealed itself, Kim Hwajong stepped in front of his young master, his gaze darker than ever.

*Step.*

A snowstorm swept around them. Stained black by mana, it was no longer white.

Nor was it beautiful.

* * *

“Team Leader, how about a drink?”

The team member approached with a soju bottle in hand and an easygoing grin. The Team Leader answered brusquely,

“No, asshole.”

Despite his words, his glass was already being raised ever so slightly. The team member grinned as if he knew everything and filled the empty glass.

*Glug, glug, glug.*

The Team Leader tossed back the soju in one gulp, then dipped a piece of flounder sashimi deep into the spicy-sweet dipping sauce and swallowed it. The chewy texture lifted his mood, if only a little.

“…Shit. At least it tastes good.”

“Right? This place is famous in the Hunter community.”

“Really?”

“Yeah. There are tons of reviews if you search for it. They say it’s the best place to have a drink after finishing a raid.”

“Of course it tastes good to those people. They probably picked up Magic Gems by the handful after their raids. It’s not like any of them came up empty-handed like me.”

“…Oh, boy. Here he goes again.”

The Team Leader smacked his lips.

If he had belonged to a Guild, it would not have mattered whether he struck out on a raid or spent the day swinging a bat. But as the leader of a freelance Hunter team, it was different. Even if he had to dig into his own pocket, he had to pay the daily wages of the people laughing and chatting around him.

Including this shameless bastard who had come over to him.

“Team Leader. You’re not angry, are you?”

“Forget it, punk. Pour me another.”

“Yes, sir.”

The team member gave a sharp salute and began pouring. The Team Leader let out a quiet laugh, then turned his gaze beyond the railing.

The raid had fallen through, but drinking while looking out over the snow-white landscape after the recent snowfall was not so bad.

*Pyeongchang really does have beautiful scenery. The scenery, anyway.*

Well, that was probably why they had built so many ski resorts around here.

The Team Leader murmured inwardly, emptied his glass again and again, and took in the view around him. The countless people who had come to the ski resort today and the gondolas constantly traveling up and down the mountain showed just how little common sense those people had.

“Hey. Isn’t this funny?”

The team member, who had been devouring sashimi with great enthusiasm, looked up.

“What is?”

“There’s a Gate sitting right on top of the mountain, and mana has increased by seven percent, but those people are still doing this shit.”

And when he had come down and checked, he had heard that a Monster Wave had broken out in Busan below. The Team Leader shook his head.

“Come to think of it, there were idiots who went skiing even when COVID broke out when I was young.”

“Merona?”[^1]

“…Never mind. Just keep stuffing your face.”

The Team Leader let out a deep sigh and emptied his glass again. His chest was beginning to feel tight as he thought about what must be happening in Busan.

“Uh—uh-oh! Oh, whoa! Whoa, whoa, whoa!”

“What now?”

“…Why is she doing that again?”

At the sudden outburst, every gaze around them—including the Team Leader’s—turned in the same direction. A female Hunter in her twenties, who had been thinking hard about something for a while, was shaking her smartphone like a madwoman.

“Wow! No way! This is insane!”

The Team Leader answered with a worried expression.

“Yeah. It certainly seems that way.”

“No, not that! I told you earlier, didn’t I? I thought I recognized that masked, incredibly handsome guy up there!”

The Team Leader recalled the group of Hunters he had encountered earlier, especially the young man walking at the very back.

“Yeah, you did. Thanks to those people, we came up empty-handed on today’s raid.”

“But it’s him! Wow, this is incredible. Kim Sohye, is your eye for faces really this good? How did you recognize him?”

“I’m going to lose my mind if I keep listening without knowing what you’re talking about, so could you please explain?”

“Look at this! Look at this!”

The Team Leader frowned when she thrust the smartphone right in front of his face. Then he saw the face on the screen and his eyes widened.

“What the hell? Is this for real? They do look alike, I guess…”

“I told you! Don’t you trust me, Team Leader?”

“No.”

“Ah, damn it! This time I’m certain, so believe me! I’ve got an eye for this that I honed through thirty years of idol fandom!”

“You’re twenty-five. Did your father do the idol fandom for you?”

“Anyway, I’m right! If I’m wrong, you don’t have to pay me today!”

A slave to capitalism was betting her daily wages.

Only then did the Team Leader begin to believe her. And he grew curious, too.

*If this is true… why would someone of this stature come all the way here?*

A brief article was displayed on the smartphone alongside a face handsome enough to pass for a celebrity.

> **Peace Guild Team Leader Choi Minwoo:** “Emergency Rescue Teams Are for Everyone”

A big shot.

An extremely big shot.

The Team Leader had not gotten a proper look at his face, but even in the photograph, the calmness in his eyes and his distinctive air seemed similar.

*If this is true, then the other Hunters must all belong to the Peace Guild, too.*

Choi Minwoo had become famous enough recently that the Team Leader had heard about him several times. But even if only half of those stories were true, the man should have been too busy to breathe. Why would he lead his Guild members to a B-grade Gate in Pyeongchang?

*Wait. Then what about that older man I saw coming down earlier?*

The thought had barely reached that point when—

*RUMBLE, RUMBLE, RUMBLE!*

A tremendous vibration began to sweep through the area. For an instant, every sound fell silent, and everyone turned their heads in the same direction as if they had planned it.

The first person to notice the anomaly was the Team Leader.

His gaze had already been fixed on that spot before the vibration began.

*…That place…*

The location he had climbed toward full of expectations, only to descend from in vain.

The B-grade Gate known as Yeti’s Winter Range.

The next moment, what appeared in the Team Leader’s widened eyes was part of the mountain slowly collapsing, with pitch-black darkness settling over it.

Amid the gondolas and buildings crumbling to pieces, a horrifying roar that shook the mind rang out.

—GRAAAAAAAH!

A Monster Wave.

And the people still inside the Gate.

Overcome by suffocating terror, the Team Leader forced out a voice he had barely managed to squeeze together.

“Report it! Right now!”

A frightened question came back.

“W-where?”

“The Hunter Association, the Peace Guild, Jin Taekyung—anywhere! Right now!”

[^1]: Merona is a Korean melon-flavored ice cream bar; its name echoes “Corona” in the original wordplay.
```

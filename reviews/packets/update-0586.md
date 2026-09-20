<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0586.txt",
      "sha256": "8c506ddd3f585fdf9197073c5aff61cf5c88db791e661cab55feed2b101bd224",
      "bytes": 13187
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "277b9abea7df50a09914ff816927d4d614985c26a7f914d39b40dc4bb986ccd6",
      "bytes": 2741
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "bc08995260a037227177c4506d04922f0532db53a950b4181e90e51ea12f3e96",
      "bytes": 183537
    },
    {
      "path": "characters/Cheonwoo.md",
      "sha256": "108d8ef6f72e6dcb4a113be27456c6f62dab9c7a973c0d0784aad77067cc3979",
      "bytes": 590
    },
    {
      "path": "characters/Go Jun.md",
      "sha256": "7a044481db7f6ca65aef6c567314cac15491c04b94b2cfd20f1ae2808e302ee3",
      "bytes": 1030
    },
    {
      "path": "characters/Hwa-jong.md",
      "sha256": "9a6e4ffc27634536278b2b75792b7a374cdf3f13457981ff950de9c5362b7667",
      "bytes": 646
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "9ce039573eeecba2d2dfe1897ec955bb2f08ce35984799ab6dfdc34bcabc7063",
      "bytes": 2280
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "fab8269b750171e09d9eaec7de4d0d35ccb2728fb1d706a11fd398fdaa7ce109",
      "bytes": 622
    },
    {
      "path": "characters/Kim Hwajong.md",
      "sha256": "8cd74fa6e2c7d4b9a7428964891c77efe0d6d838da485fba2e91ca5972735c75",
      "bytes": 694
    },
    {
      "path": "characters/Lee Jungryong.md",
      "sha256": "b405a47ff4f7b51ea9cabd9b57359cbdc6e6fdcb34a74fb923f65ae829d29af6",
      "bytes": 1384
    },
    {
      "path": "characters/Song Cheonwoo.md",
      "sha256": "6285abe4204acde78bf42f2399d95e9f2ff8e130b094e19a80ca1efb23ceb89c",
      "bytes": 1080
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "ec3a0a8b45b6a8cea41b2328fa0f4ae755f7d8b4e97890dc46e1bbad0e28ca99",
      "bytes": 180828
    }
  ],
  "estimated_tokens": 11883
}
-->

# Durable State Update — Chapter 586

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 586. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 586. Profile updates may replace only one
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
  "chapter": 586,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 586,
    "continuity_sources": [586],
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
    "Song claims Taemin is still alive, but his location is unknown and Area A is only suspected.",
    "Choi Minwoo has confirmed enough of Song's account to treat Taemin's status as genuine while continuing to investigate.",
    "Busan's Kraken has been eliminated, but more than one thousand Mermen remain across Haeundae and Gwangalli while the Peace Guild and other forces contain the disaster.",
    "Go Jun seized Song Cheonwoo's children as leverage and used the threat to force Song to attack Choi Minwoo.",
    "Go Jun used an S-grade Magic Gem to cause the Busan Monster Wave and sent Kim Ho-jung to Busan.",
    "Go Jun intends to kill Choi Minwoo through Song Cheonwoo and may be relying on another unidentified being.",
    "Song Cheonwoo was killed by an unidentified monster after falling into an abyss, and the unused object in his pocket released darkness that became light after his death.",
    "Jin Taekyung killed Behemoth with One Annihilation and received a level-up that removed Exhaustion and Internal Energy Depletion.",
    "Kim Hwajong sacrificed his life to restrain Behemoth and died after confirming through Taekyung that Choi Minwoo was safe.",
    "Skeleton King could not save Kim Hwajong despite absorbing the magic in his bones and using a top-grade potion."
  ],
  "continuity_sources": [
    585,
    584
  ],
  "open_questions": [
    "What caused Cheon Taemin's collapse, and what happened during his more than twenty years of unconsciousness?",
    "Is Cheon Taemin actually being kept in Area A of Ares Guild headquarters?",
    "What is the unidentified being involved in Go Jun's plan, and is it connected to the monster that killed Song Cheonwoo?",
    "What was the object Song Cheonwoo kept unused in his pocket, and what did its release of darkness and light accomplish?"
  ],
  "safe_through": 585,
  "temporary_decisions": [
    "Use Yeti's Winter Range for 예티의 겨울 산맥, Stone King for 스톤 킹, Skeleton King for 스켈레톤 킹, Behemoth for 베히모스, and Behemos for 베헤모스.",
    "Use Area A for A구역 and Hwa-jong for 화종.",
    "Use Hero's Soul for 영웅의 혼, Hyung for 형님, S-grade Magic Gem for S급 마정석, Hell Fire for 헬 파이어, and Hellfire Mage for 겁화의 마법사.",
    "Use final rally for 회광반조 and Young Master for 도련님.",
    "Use Internal Energy Depletion for 공력 소진."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 김화종    | **Kim Hwajong**   |
| 이정룡    | **Lee Jungryong** |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 사제     | **Junior Brother**                           |
| 시스템              | **System**                     |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 아이템              | **Item**                       |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 길드      | **Guild**             |
| 길드장     | **Guild Master**      |
| 팀장      | **Team Leader**       |
| 마법사     | **mage**              |
| 마정석     | **Magic Gem**         |
| 대격변     | **Great Cataclysm**   |
| 천우 | **Cheonwoo** | Name shown in a Level Window; one of the five current Five Gates scions. |
| 고준 | **Go Jun** | Personal name of Team Leader Seok; Lee Jungryong's prized Disciple. |
| 화종 | **Hwa-jong** | Butler Kim's personal name. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 송천우 | **Song Cheonwoo** | Ares Guild Director, former third-ranked Korean Hunter, and longtime European regional branch director. |
| 평화 | **Peace Guild** | Guild name. |
| 아레스 | **Ares Guild** | The leading Guild in Korea; formerly employed Team Leader Choi and Song Song. |
| 강원도 | **Gangwon Province** | Province named in Taekyung’s joke about the Minotaur’s next life. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 아이템창 | **Item Window** | System window displaying an item's details. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 허공섭물 | **Seizing an Object Through Empty Space** | Technique Jeok Cheongang uses to lift Jang Taebo remotely. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 소원 | **Sowon** | Name called out by Im Kkeokjeong during the Wyvern attack. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 석고준 | **Go Jun** | Source full-name form for the established Go Jun, also known as Team Leader Seok. |
| 도련님 | **Young Master** | Address used for Team Leader Choi by Butler Kim. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 경호팀장 | **Head of Security** | Go Jun's security-team office under Lee Jungryong. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 소멸 | **Erasure** | Jin's term for the Skeleton Warlord's destruction by the Arch Lich's mana. |
| 텔레포트 | **Teleport** | Taekyung's label for the Blood Lord's unexplained disappearance. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 크라켄 | **Kraken** | Sea monster leading the Monster Wave; newly identified in this chapter. |
| 평창 | **Pyeongchang** | Location in Gangwon Province where the Gate is situated. |
| 베히모스 | **Behemoth** | Mythical monster emerging from the Pyeongchang Gate. |
| 정룡 | **Jungryong** | Cheon Taemin's trusted associate who joined the Peace Guild. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 김화종 | 진태경 | senior_Hunter_to_younger_Hunter | Mr. Jin | formal-polite | Hwajong addresses Taekyung as 진태경 씨 while proposing an exchange of stories. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 이정룡 | 진태경 | senior S-rank Hunter to younger Hunter and adversary | Young man | polished, teasing, and veiled-threatening | Uses a genial tone and indirect threats while trying to make Taekyung release the captives. |
| 진태경 | 이정룡 | younger Hunter to senior S-rank Hunter and adversary | you | polite but mocking and defiant | Taekyung answers Lee's soft threats with the wolf-and-tiger metaphor and refuses to yield. |
| 이정룡 | 고준 | Master to Disciple | Go Jun | familiar and testing | Lee switches from Seok's office title to his personal name while considering whether he can defeat Taekyung. |
| 고준 | 이정룡 | Disciple to Master | Master | deferential | Go Jun responds to Lee's personal-name address as 스승님. |
| 마법사 | 이정룡 | Ares Guild mage subordinate to Vice Guild Master | Vice Guild Master | formal-deferential | Lee's five direct A-rank mages greet him and receive instructions for concealing the battle. |
| 진태경 | 석고준 | returning Hunter to hostile Ares security leader | you fucking bastard | hostile and profane | Taekyung directs his final insults and challenge at Go Jun after returning alive. |
| 석고준 | 진태경 | hostile_opponents | brat | hostile and overconfident | Go Jun addresses Taekyung internally as 애송아 while launching his full-strength attack. |
| 중년인 | 진태경 | veteran civilian Hunter to celebrated allied Hunter | Mr. Jin | formal-polite and awed | The casualty clerk addresses Jin as 진 선생님 after Jin asks him to list Lei Fei among the dead. |
| 진태경 | 중년인 | celebrated Hunter to older fellow Hunter | sir | casual and teasing | Jin addresses the older Hunter as 아저씨 while joking with him and giving him instructions. |
| 고준 | 진태경 | Ares Guild combatant confronting the killer of his Master | you | hostile and informal | Go Jun uses 너 while demanding Jin confess to Lee Jungryong's death and threatening retaliation. |
| 진태경 | 고준 | dominant adversary confronting Lee Jungryong's Disciple | you | contemptuous and informal | Jin uses 너 and 놈 while overpowering Go Jun and ordering him to end the conflict with Lee Jungryong. |
| 송천우 | 석고준 | adversary; captor of Song's children | you | shocked and confrontational | Song reacts directly to Go Jun's admission that he took the children. |
| 진태경 | 마법사 | rescuer assisting the operation | mage; otherwise you | polite emergency imperative | Taekyung orders the exhausted mage to request rescue under his name. |
| 송천우 | 화종 | former_allies | Hwa-jong | familiar and informal | Song uses Hwa-jong's personal name, prompting Hwa-jong to reject the familiarity. |
| 화종 | 송천우 | former_allies_now_hostile | you | formal and cold | Hwa-jong challenges Song's right to expect Choi's trust and rejects their former intimacy. |
| 팀장 | 중년인 | Hunter_team_leader_to_stranger | Boss | casual and polite | The Team Leader mistakes disguised Song for an ordinary raid customer and warns him not to proceed. |

## Listed compact profiles

### Cheonwoo.md

# Cheonwoo (천우)

- **Safe through:** Chapter 584
- **Aliases:** None
- **Role:** One of the five current Five Gates of Shanxi scions and a First Rate martial artist present at Honghwa Inn.
- **Personality:** Pampered and contemptuous toward Cheongpung's group as part of the five scions' collective mockery.
- **Voice:** Mocking in the group's exchange; no distinct individual speech is established.
- **Relationships:** Associates with Seongryong, Myeonghwa, Sohye, and Jintae as a group of current Five Gates scions.

### Go Jun.md

# Go Jun (고준)

- **Safe through:** Chapter 581
- **Aliases:** Team Leader Seok
- **Role:** Go Jun is Ares Guild's Vice Guild Master, Lee Jungryong's disciple and former Head of Security, and the de facto successor to Lee's Ares legacy who passed the S-rank Hunter qualification assessment with a very high score but lacks Lee's legitimacy.
- **Personality:** Disciplined and controlled under ordinary pressure, fiercely loyal to Lee Jungryong, but consumed by humiliation and rage when Ares Guild's authority is challenged.
- **Voice:** Dry, controlled, and formal with subordinates; deferential when addressing his Master.
- **Relationships:** Disciple and direct protégé of Lee Jungryong, Go Jun inherited Lee's Ares Guild legacy after his death, regards Jin Taekyung and Choi Minwoo as enemies seeking to take it away, has seized Song Cheonwoo's children as leverage, and used an S-grade Magic Gem to trigger the Busan Monster Wave while targeting Choi.

### Hwa-jong.md

# Hwa-jong (화종)

- **Safe through:** Chapter 585
- **Aliases:** Butler Kim
- **Role:** Hwa-jong was Choi Minwoo's loyal butler and personal escort who sacrificed his life to restrain Behemoth and died after Jin Taekyung killed it.
- **Personality:** Loyal, vigilant, and uncompromising toward perceived threats to Choi Minwoo.
- **Voice:** Formal and deferential toward Choi Minwoo, cold and openly hostile toward Song Cheonwoo.
- **Relationships:** Hwa-jong serves Choi Minwoo and was formerly close to Song Cheonwoo, but their relationship ended over loyalty and ambition.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 581
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, a Supreme Peak master who possesses the Heavenly Martial Physique and superhuman physical strength, has manifested Force, opened his Middle Dantian, crossed the wall into true mastery, has achieved Three Flowers Gather at the Crown but not Five Qi Returning to Origin, can perceive the texture of qi well enough to sever layered magic, can resist high-level monster Fear through exceptional mental strength, is publicly recognized as an S-rank-level Hunter while formally retaining an A-rank license pending testing, can command coordinated raids against powerful monsters, serves as one of the two pavilion masters of the Alliance Leader's direct Fire Dragon Pavilion, leads its first mission to Nanman, and is the Peace Guild's wealthy patron in the modern world.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor and assigned him a final task to incorporate martial principles into his learned martial arts but declined Taekyung's recruitment after Cheongpung reached him first, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate, student, and trusted manager of media and official arrangements, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, and Xiao Shen regards him as an older brother after Jin saved him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 581
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Kim Hwajong.md

# Kim Hwajong (김화종)

- **Safe through:** Chapter 585
- **Aliases:** Butler Kim
- **Role:** Kim Hwajong was a Level 80 mage known as Butler Kim and Choi Minwoo's loyal butler and personal escort who sacrificed his life to restrain Behemoth and died after Jin Taekyung killed it.
- **Personality:** Gentle and composed as Butler Kim, but retains a fiery temperament and a habit of swearing.
- **Voice:** Gentle and measured
- **Relationships:** Kim Hwajong formerly instructed Im Chunsoo, who remains terrified of and obedient to him, and serves Choi Minwoo as butler and personal escort, having become Choi's only family.

### Lee Jungryong.md

# Lee Jungryong (이정룡)

- **Safe through:** Chapter 580
- **Aliases:** None
- **Role:** Former Vice Guild Master of Ares Guild, one of Korea's two S-rank Hunters, and a Supreme Peak-level martial artist who was killed by Jin Taekyung.
- **Personality:** Outwardly genial, calm, and humorous; calculating, opportunistic, manipulative, coercive, and ruthless when challenged
- **Voice:** Smooth, good-natured, and indirect, using teasing conversation and veiled threats before becoming openly furious
- **Relationships:** Master of Park Jihoon and Go Jun (Team Leader Seok), whom he personally selected and trained; longtime Great Cataclysm acquaintance of Park Tae Seop; adversary of Jin Taekyung; knew Team Leader Choi from childhood; has an antagonistic history with Kim Hwajong, who saved his life at the collapse of Mapo Bridge eighteen years earlier; was visibly shaken by learning that Choi is Cheon Taemin's maternal grandson; regarded Cheon Taemin as an older brother despite no blood relation and long held him in respect and fear; secretly supported the orphanage where Lee Dongseok grew up and was regarded by Dongseok as a father; operated as Ares Guild's senior authority beneath its Guild Master; concealed Taemin's condition with Song Cheonwoo and participated in purging aides who knew the truth.

### Song Cheonwoo.md

# Song Cheonwoo (송천우)

- **Safe through:** Chapter 583
- **Aliases:** Director Song
- **Role:** Ares Guild Director and former A-rank Hunter who reached third place among Korean rankers, briefly headed the Hunter training center, and led Ares Guild's European regional branch for twenty years; after being forced to attack Choi Minwoo to protect his hostage family, he fell into an abyss and was killed by an unidentified monster.
- **Personality:** Highly ambitious, honor-obsessed, politically calculating, and determined to use his final opportunity to reclaim influence before retirement.
- **Voice:** Not established.
- **Relationships:** Song Cheonwoo followed Cheon Taemin since before Team Leader Choi was born, was Lee Jungryong's former friend and rival, helped conceal Taemin's condition and purge aides who knew the truth, negotiated the European regional director position to save himself and his family, and had his children seized by Go Jun as leverage that forced him to attack Choi Minwoo.

## Korean source

```text
＃586화



간혹, 어떠한 종류의 진실은 잔혹하고 차갑다.

그 진실과 마주한 사람은 자신이 처한 상황이 믿기지 않아서, 혹은 믿기 싫어서 눈앞의 진실을 외면하고는 한다.

지금의 나처럼.

“……인간.”

스켈레톤 킹의 목소리가 적막을 깨트리고 귓가를 파고들었을 때, 나는 아주 길고 끔찍한 꿈에서 깬 기분이 들었다.

그리고 다음 순간 그 모든 것이 꿈이 아닌 현실이라는 것을 깨달았다.

‘돌아가셨군요. 정말로.’

마침내 죽음을 맞이한 김화종의 얼굴은 온화했고, 올라간 채로 굳은 입꼬리에는 기쁨이 맺혀 있었다.

그것은 마지막 소원을 이루고 떠날 수 있었던 망자(亡者)가 남긴 미소였다.

하지만 나는 그의 몸으로 계속해서 열양지기를 흘려보냈다. 닿지 않을 물음과 함께.

여전히 추우십니까. 아직도 어두우십니까.

어쩌면 내가 기억하는 노집사는, 지금도 영원히 끝나지 않을 겨울밤을 헤매고 있을지도 모른다.

추위에 떨며, 한 치 앞도 보이지 않는 어둠 속에서 한 사람을 찾고 있을지도 모른다.

그렇기에 나는 멈출 수 없었다.

그것이 점점 차갑게 식어 가는 그의 몸뚱어리에 온기를 불어넣는 이유였다.

턱.

차가운 손길이 어깨에 닿았다. 착 가라앉은 스켈레톤 킹의 목소리가 귓가에 닿았다.

“인간.”

“놔.”

“이제 충분하다. 그만해라.”

그 말은 틀렸다. 충분하지 않다. 그러니 멈출 수도 없었다.

어깨에 닿은 손을 거칠게 뿌리치려던 그때, 스켈레톤 킹이 말을 이었다.

“더 이상은 춥지 않을 테니, 그 인간을…… 그분을 놓아 드려라.”

“……!”

그 말을 듣는 순간, 왜 전신에서 힘이 빠졌을까.

참으로 모를 일이었다.

어쩌면 스켈레톤 킹이 처음으로 한 인간을 향해 공대를 사용했기 때문일 수도, 귓가를 파고든 그 목소리가 유난히 힘이 없어서였을 수도 있었다.

그도 아니라면, 재앙이 스쳐 지나간 이 이름 모를 산등성이를 다시 찾은 손님들 때문일 것이다.

사박.

눈을 밟는 조심스러운 발걸음.

소리를 따라 고개를 돌리자, 비로소 모습을 드러낸 남녀 다섯이 보였다.

길드 하우스 내부에서 한두 번쯤 마주치며 인사를 주고받은 얼굴들이라, 나는 어렵지 않게 그들의 정체를 알아챌 수 있었다.

‘평화 길드원.’

상황이 바뀌었음을 알아채고 돌아온 것이 틀림없다.

이미 나보다 앞서 베히모스와 악전고투를 치르며 지치고 상처 입은 그들은, 넋 나간 눈빛으로 자신들의 눈앞에 쓰러진 마수를 바라보다가 이내 고개를 돌려 이쪽을 바라보았다.

그리고…….

“안 돼!”

“길드장님!”

고함과 비명이 뒤섞여 울려 퍼졌다.

베히모스의 사체를 넘어 다급하게 달려온 그들을 맞이한 것은 영원히 깨지 못할 깊은 잠에 빠진 김화종이었다.

“어, 어떻게 이런.”

“……빌어먹을. 이렇게 될 줄 알았습니다. 이렇게 될 줄 알았다고!”

울음 섞인 비통한 목소리들.

비록 나는 그 자리에 없었지만, 일이 어떻게 흘러갔을지는 눈앞에 선명히 그려졌다.

‘가라고 했겠지. 당신은 괜찮으니 최 팀장과 함께 도망치라고.’

김화종은 그런 사람이다.

그에게는 목숨보다 소중한 것이 있었다. 도련님이라 쓰고 손자라 읽을 수 있었던 한 젊은이가 바로 그러한 존재였다.

못 박힌 듯 서서 모든 것을 지켜보던 나는 문득 입을 열었다.

“최 팀장님을.”

“예, 예?”

거칠고 공허한. 남의 것처럼 낯선 목소리가 흘러나왔다.

“최 팀장님을 그분 곁에 내려놓으세요.”

“……!”

“어서.”

멍하니 나를 바라보던 길드원들이 이내 뜻을 알아채고 고개를 끄덕였다.

그들은 모든 힘을 소진한 채 의식을 잃은 최 팀장을 조심스럽게 지면에 내려놓았다.

나란히 누워 있는 두 사람은, 전혀 닮지 않았으면서도 서로를 닮아 있었다.

‘드디어 만났군요, 두 분.’

나는 말 없이 두 사람의 손을 맞잡게 해 주었다.

기분 탓일까, 순간 김화종의 입가에 맺힌 미소가 더욱 환해지는 것 같았다.

“진태경 헌터님. 차라리 팀장님을 깨우는 것이…….”

길드원 중 한 사람이 조심스럽게 건넨 말에, 나는 고개를 가로저었다.

“안 됩니다.”

“하, 하지만…….”

“그럴 수는 없습니다. 적어도 지금 당장은.”

나는 단호하게 그의 말을 잘랐다. 나 역시 고민해 보지 않은 것은 아니다.

적어도 김화종이 죽음을 맞이하기 전이었다면, 난 무슨 수를 써서라도 최 팀장의 의식을 깨워 두 사람을 대면시켜 주었을 것이다.

하지만…….

‘이미 늦었어.’

김화종은 이미 죽음을 맞이했고, 피로가 누적되어 한계에 다다른 최 팀장의 육체는 온전치 않다.

억지로 의식을 회복시켜 포션을 사용한다 하더라도 그 대가는 몇 배로 돌아와 최 팀장을 덮칠 것이다.

깊이를 짐작할 수 없는 슬픔과 분노도 함께.

망자는 고통 끝에 안식을 얻었지만 살아남은 이는 고통을 간직하고 살아가야 한다.

나는 삼 년 전 그 사실을 깨달았고, 그토록 잔인한 현실을 몸도 성치 않은 최 팀장을 깨워 알려 줄 수는 없었다.

다만 한 가지는 장담할 수 있다.

최 팀장이 의식을 회복하기 전에, 그가 느낄 분노와 슬픔을 조금이라도 잠재울 선물을 가져갈 것이라는 걸.

쐐애애액! 서걱!

어떤 준비 동작도 없이 휘두른 창의 끝에서 바람이 갈라졌다.

반월의 형태로 쏘아진 강기(罡氣)가 쓰러져 있던 베히모스의 거대한 동체를 베어 내자, 스켈레톤 킹이 한숨처럼 중얼거렸다.

“그만해라.”

나는 대답 대신 재차 손에 쥔 창을 휘둘렀다. 한 번, 두 번, 세 번…….

서걱! 서걱! 푸화아악!

몸뚱어리가 토막 나고, 사체에 남아있던 핏물이 분수처럼 솟구친다.

한때 베히모스가 품고 있던 강대한 마력이 사라진 이상, 이제 그것은 한낱 고깃덩어리에 지나지 않았다.

나는 도축업자처럼 망설임 없이 그것들을 베어 냈다. 그 광경을 보다 못한 스켈레톤 킹이 버럭 외치기 전까지.

“그만하라고 했다! 네놈이 이런다고 뭐가 달라지……!”

나는 나직한 목소리로 녀석의 외침을 끊어 냈다.

“충분히 달라질 수 있으니 이러는 거다.”

“뭐?”

스켈레톤 킹이 의아한 표정으로 물었다.

“그게 지금 도대체 무슨 소리냐?”

나는 그 물음에 답하지 않은 채 걸음을 내디뎠다.

한 걸음 만에 수 미터의 거리가 좁혀지고 베히모스의 시체가 코앞으로 가까워졌다.

생전의 위용을 찾아볼 수 없을 만큼 토막 난 사체를 물끄러미 바라보던 나는, 마침내 찾고 있던 것을 발견했다.

아니, 그것은 내가 찾기도 전에 스스로를 알리고 있었다.

우우웅.

공기로부터 전해지는 미세한 떨림. 동시에 느껴지는 혼탁하면서도 강력한 기운.

“……찾았다.”

혹시 앞서 날린 일섬으로 소멸했을까 싶어 걱정했었는데, 다행히도 ‘그것’은 무사했다.

내심 안도의 뜻을 담아 중얼거린 나는 망설임 없이 손을 뻗었다.

쉬익, 탁!

허공섭물(虛空攝物)에 의해 손아귀로 날아온 ‘그것’을, 나는 착 가라앉은 시선으로 응시했다.

그리고 누구에게도 들리지 않게 마음속으로 중얼거렸다.

‘아이템 감정.’

띠링.



아이템창



[베히모스의 혼탁한 심연]

종류 : 마정석

등급 : 초절정

제한 : 無

설명 : 네임드 몬스터이자 태고의 마수, 베히모스가 품은 심연(深淵)이자 마력의 원천.

그러나 모종의 이유로 또 다른 마력을 흡수하여, 순수했던 어둠은 혼탁해지고 더욱 강력해졌다.

이것을 사용하기 위해서는 매우 까다롭고 어려운 정화 작업을 거쳐야 한다.





허공에 떠오른 시스템 창을 확인한 순간, 눈앞이 뜨거워졌다.

하지만 머릿속은 그 어느 때보다 차갑게 가라앉은 채로 회전하고 있었다.

‘베히모스의 혼탁한 심연.’

지금까지 시스템은 단 한 번도 거짓말을 하지 않았다. 그러니 설명란에 적힌 내용 역시 한 치의 틀림 없는 사실일 것이다.

‘모종의 이유로 또 다른 마력을 흡수했다. 그래, 그렇단 말이지.’

크라켄과의 대화 직후, 지난 몇 시간 동안 머릿속을 떠다니던 의문들이 차례차례 순서를 찾아 움직였다.

크라켄에게 마정석을 주어 몬스터 웨이브를 일으킨 범인은 누구인가, 그놈의 뒤에는 누구의 사주가 있는가.

왜 그토록 바쁜 최 팀장이 서울을 떠나 강원도 평창까지 왔으며, 하필이면 이곳에서 왜 다시 몬스터 웨이브가 발생했는가.

그리고 베히모스가 남긴 마정석의 설명은 무엇을 의미하는가.

‘왜. 왜. 왜.’

스스로 질문을 던지고, 스스로 답을 찾았다.

몇 시간으로 느껴질 만큼 짧은 시간이 흐른 뒤, 나는 모든 의문에 관한 답을 도출해 낼 수 있었다.

딱 한 가지, 마지막 퍼즐을 빼고.

‘그래. 마지막 하나.’

그러나 나는 머뭇거리지 않았다. 마지막 남은 퍼즐을 어디에서 찾아야 할지, 이미 알고 있었기 때문이었다.

“오늘, 왜 이곳에 왔습니까?”

내 물음이 향한 곳에는 평화 길드원들이 있었다.

주위의 시선이 자신을 향해 쏠리자, 가장 상급자로 보이는 중년의 헌터가 어두운 표정으로 대답했다.

“최 팀장님께서 극비리에 만나야 할 인물이 있었습니다. 환영 마법으로 모습을 바꾼 남자였죠. 많이 초조해 보였습니다.”

“그게 누굽니까?”

“죄송하지만…… 저를 포함한 모두가 그의 정체를 모릅니다.”

아마도 중년인의 말은 사실일 것이다. 하지만 나는 실망하지 않았다.

임시 경호팀장에게도 알리지 않았던 그의 정체를, 얼마 전 최 팀장의 입으로 직접 들었기 때문이었다.

‘송천우.’

대격변의 영웅이자 아레스 길드의 유럽 총괄 지사장.

그리고…… 이정룡과 석고준. 두 사제(師弟)와 대를 이어 대립하는 정적.

그러나 나는 이미 그와 최 팀장이 극비리에 맺은 임시 협력 관계에 대하여 알고 있었고, 송천우를 범인으로 생각할 만큼 바보가 아니었다.

‘그럴 이유가 없지. 단 하나도.’

송천우는 세월도 이기지 못한 야심가다.

그러니 모든 문제를 떠나, 석고준의 실각을 노리는 그가 든든한 조력자인 최 팀장을 죽이려 한다는 것부터가 어불성설이었다.

결국, 오늘 벌어진 모든 일의 범인은 따로 있다는 뜻이다.

두 사람의 죽음으로 누구보다 큰 이익을 보게 될 사람.

천문학적인 가치와 희소성을 지닌 S급 마정석을 이용하여, 몬스터 웨이브를 일으킬 수 있는 사람.

‘석고준.’

마지막 퍼즐 조각이 맞춰진 순간. 나는 앞으로 해야 할 일이 무엇인지 깨달았다.

그리고 지금 내린 이 선택의 여파가 내 주위에까지 미칠 수 있다는 것 역시도.

‘그렇다면…….’

나는 지그시 눈을 감았다.

이미 돌이킬 수 없다. 이것은 옳고, 그른 것을 떠나 반드시 해야 하는 일이다.

그렇게 다시 눈을 떴을 때, 내 마음과 목소리에는 한 치의 흔들림도 존재하지 않았다.

“만약에, 제가 없는 사이에 팀장님께서 깨어나시면 누구든 전해 주십시오.”

“예? 뭐라고…….”

“S급 헌터 진태경.”

남의 것처럼 낯설고 건조한 목소리가 이어졌다.

“지금 이 시간 부로, 평화 길드에서 탈퇴합니다.”

“……!”

“……!”

얼어붙은 사람들의 표정이 눈에 들어왔다. 일그러진 누군가의 얼굴도 함께.

“네놈, 설마……!”

“넌 여기 남아라. 혹시 모르니 사람들을, 길드를 지켜.”

떠날 사람은 떠나고, 남을 사람은 남아야 한다.

재차 만류하려는 스켈레톤 킹에게 고개를 저어 보인 나는, 석상처럼 굳어 버린 길드원들을 향해 질문을 던졌다.

“혹시 텔레포트 가능하신 분? 손.”

“소, 손.”

엉겁결에 손을 든 마법사가 멍한 얼굴로 물었다.

“그, 그런데 어디로요?”

“종로. 아니…….”

나는 영영 깨어나지 않을 잠에 빠진 노집사를 바라보며 말을 이었다.

“아레스 길드로 갑시다.”
```

## Final English reading copy

```markdown
# Chapter 586

Sometimes, certain kinds of truth are cruel and cold.

People who face such truths often turn away from them because they cannot believe the situation they are in—or because they do not want to believe it.

Like me right now.

“……Human.”

When Skeleton King’s voice broke the silence and pierced my ears, I felt as though I had awakened from a long, terrible dream.

And in the next moment, I realized that none of it had been a dream. It was reality.

*He’s gone. Truly.*

Kim Hwajong had finally met his death. His face was peaceful, and joy lingered at the corners of his lips, which had stiffened in an upward curve.

It was the smile left by a dead man who had been able to fulfill his final wish before departing.

But I continued sending Scorching Yang Qi through his body, along with questions that would never reach him.

*Are you still cold? Is it still dark?*

Perhaps the old butler I remembered was still wandering through an endless winter night.

Perhaps he was shivering in the cold, searching for someone in darkness so deep that he could not see even an inch ahead.

That was why I could not stop.

That was why I continued forcing warmth into his body as it grew colder and colder.

Thud.

A cold hand touched my shoulder. Skeleton King’s voice reached my ears, low and subdued.

“Human.”

“Let go.”

“It is enough now. Stop.”

He was wrong. It wasn’t enough. So I couldn’t stop.

Just as I was about to roughly shake off the hand on my shoulder, Skeleton King continued.

“He will not be cold anymore, so let that human go…… Let that person rest.”

“……!”

Why did all the strength leave my body the moment I heard those words?

I truly did not know.

Perhaps it was because Skeleton King had used honorific speech toward a human for the first time. Or perhaps it was because the voice that had pierced my ears sounded unusually powerless.

If it was neither of those things, then perhaps it was because of the guests who had returned to this nameless mountain ridge after the disaster had passed through.

Crunch.

Cautious footsteps pressed into the snow.

I turned my head toward the sound and finally saw five men and women emerge into view.

They were faces I had encountered once or twice inside the Guild House, exchanging greetings in passing, so I had no trouble recognizing them.

*Peace Guild members.*

They had undoubtedly returned after realizing that the situation had changed.

They had already fought Behemoth desperately ahead of me, exhausting themselves and suffering injuries. With vacant eyes, they stared at the monster collapsed before them. Then they turned their heads and looked in this direction.

And then…

“No!”

“Guild Master!”

Shouts and screams rang out together.

The person who greeted them as they hurried over Behemoth’s corpse was Kim Hwajong, fallen into a deep sleep from which he would never awaken.

“H-How could this happen?”

“……Damn it. I knew this would happen. I knew it!”

Their voices were filled with grief and tears.

Though I had not been there, I could clearly imagine how everything had unfolded.

*He must have told them to go. Told them to run with Team Leader Choi because he was all right.*

That was the kind of person Kim Hwajong was.

There was something more precious to him than his own life. A young man who could be called his Young Master—or, more accurately, his grandson.

I had stood there as though nailed to the ground, watching everything. Then I suddenly opened my mouth.

“Team Leader Choi.”

“Y-Yes?”

A rough, hollow voice slipped from my lips. It sounded unfamiliar, as though it belonged to someone else.

“Lay Team Leader Choi down beside him.”

“……!”

“Hurry.”

The Guild members stared blankly at me. Then, realizing what I meant, they nodded.

They carefully laid Team Leader Choi down on the ground. He had lost consciousness after exhausting every last bit of his strength.

The two men lying side by side looked nothing alike, and yet they resembled each other.

*You finally met, the two of you.*

Without a word, I placed their hands together.

Was it only my imagination? For a moment, the smile at the corners of Kim Hwajong’s lips seemed to grow brighter.

“Hunter Jin Taekyung. Wouldn’t it be better to wake the Team Leader……?”

One of the Guild members spoke carefully. I shook my head.

“No.”

“But…….”

“We can’t do that. At least not right now.”

I cut him off firmly. It wasn’t as though I hadn’t considered it myself.

If Kim Hwajong had not yet met his death, I would have done anything necessary to wake Team Leader Choi and let the two of them meet.

But…

*It’s already too late.*

Kim Hwajong was already dead, and accumulated fatigue had pushed Team Leader Choi’s weakened body to its limit.

Even if I forced him back to consciousness and gave him a potion, the backlash would hit him several times harder—along with immeasurable grief and rage.

The dead had found rest after suffering, but the living had to continue on while carrying their pain.

I had realized that three years ago. I could not wake Team Leader Choi, whose body was already in such poor condition, only to tell him that cruel reality.

There was just one thing I could promise.

Before Team Leader Choi regained consciousness, I would bring him a gift that could soothe even a little of the rage and grief he would feel.

Whoosh! Slash!

The tip of the spear I swung without any preparation split the air.

Force shot out in the shape of a half-moon and sliced through Behemoth’s enormous body, which lay collapsed on the ground. Skeleton King muttered like a sigh.

“Stop.”

Instead of answering, I swung the spear in my hand again.

Once. Twice. Three times……

Slash! Slash! Fwoosh!

The body was cut into pieces, and the blood remaining in the corpse spurted upward like a fountain.

The powerful magic Behemoth had once contained was gone. Now, it was nothing more than a mass of meat.

I cut it apart without hesitation, like a butcher.

That continued until Skeleton King could no longer stand the sight and shouted.

“I said stop! What difference will this make……!”

I cut off his shout in a quiet voice.

“It can make enough of a difference. That’s why I’m doing this.”

“What?”

Skeleton King asked with a puzzled expression.

“What in the world are you talking about?”

I did not answer. I simply stepped forward.

In a single step, I closed several meters of distance, bringing Behemoth’s corpse right before me.

I stared at the chopped-up remains, so mutilated that none of its former majesty remained.

At last, I found what I had been searching for.

No. It had announced itself before I could even find it.

Vrrrrrrm.

A faint vibration traveled through the air. At the same time, I sensed a murky yet powerful energy.

“……Found it.”

I had worried that it might have been erased by the One Annihilation I had fired earlier, but fortunately, *it* was unharmed.

I muttered with a hint of relief and reached out without hesitation.

Whoosh—clack!

Seizing an Object Through Empty Space sent *it* flying into my hand. I stared at it with a solemn gaze.

Then I muttered inwardly, where no one could hear.

*Item Appraisal.*

Ding.

> **System**
>
> **Item Window**
>
> **Behemoth’s Turbid Abyss**
>
> **Type:** Magic Gem  
> **Grade:** Supreme Peak  
> **Restriction:** None  
>
> **Description:** The abyss contained within Behemoth, a Named Monster and primordial beast, and the source of its mana.
>
> For some reason, it absorbed mana from another source. Its once-pure darkness became turbid and grew even more powerful.
>
> An extremely difficult and painstaking purification process must be completed before this can be used.

The moment I read the System Window floating in the air, my eyes grew hot.

But my mind was colder and clearer than ever as it turned over the information.

*Behemoth’s Turbid Abyss.*

The System had never lied to me. That meant the contents of the description were also facts without the slightest error.

*It absorbed another magic power for some reason. So that’s how it is.*

The questions that had been drifting through my head for the past several hours, ever since my conversation with Kraken, began to fall into place one after another.

Who had given Kraken the Magic Gem and caused the Monster Wave? Who was behind him, giving the orders?

Why had Team Leader Choi, who was so busy, left Seoul and come all the way to Pyeongchang in Gangwon Province? Why had another Monster Wave occurred here of all places?

And what did the description of the Magic Gem left behind by Behemoth mean?

*Why? Why? Why?*

I asked myself the questions, then found the answers myself.

A short time passed—though it felt like several hours.

After that, I was able to derive the answer to every question.

Except for one final piece of the puzzle.

*Yes. The last one.*

But I did not hesitate. I already knew where to find the final piece.

“Why did you come here today?”

My question was directed at the Peace Guild members.

When everyone’s attention turned toward him, the middle-aged Hunter who appeared to be the highest-ranking among them answered with a dark expression.

“There was someone Team Leader Choi had to meet in secret. A man who had changed his appearance with illusion magic. He looked extremely anxious.”

“Who was he?”

“I’m sorry, but…… None of us, myself included, knows his identity.”

The middle-aged man was probably telling the truth. But I was not disappointed.

I had heard the man’s identity directly from Team Leader Choi himself not long ago. Even the temporary Head of Security had not been informed.

*Song Cheonwoo.*

A hero of the Great Cataclysm and the European regional director of Ares Guild.

And…… the political rival who had opposed both Lee Jungryong and his disciple Go Jun across two generations.

But I already knew about the secret temporary alliance between him and Team Leader Choi. I was not foolish enough to think Song Cheonwoo was the culprit.

*There was no reason for him to do it. Not one.*

Song Cheonwoo was an ambitious man whom even the passage of time had failed to tame.

Setting everything else aside, the idea that he would try to kill Team Leader Choi—a reliable ally who was working to bring down Go Jun—was absurd from the outset.

In the end, that meant someone else was behind everything that had happened today.

The person who would gain more than anyone from the deaths of the two men.

The person who could use an S-grade Magic Gem of astronomical value and rarity to cause a Monster Wave.

*Go Jun.*

The moment the last piece of the puzzle fell into place, I realized what I had to do.

I also realized that the repercussions of the choice I had just made could spread to the people around me.

*In that case……*

I slowly closed my eyes.

There was no turning back now. Regardless of whether it was right or wrong, this was something I had to do.

When I opened my eyes again, there was not the slightest tremor in my heart or voice.

“If Team Leader Choi wakes up while I’m gone, please make sure someone tells him.”

“Pardon? Tells him what……?”

“S-grade Hunter Jin Taekyung.”

The unfamiliar, dry voice that sounded as though it belonged to someone else continued.

“As of this moment, I am withdrawing from the Peace Guild.”

“……!”

“……!”

The frozen expressions of the people before me came into view.

Along with someone’s twisted face.

“You bastard, don’t tell me……!”

“You stay here. Just in case, protect the people and the Guild.”

Those who were leaving had to leave, and those who were staying had to stay.

I shook my head at Skeleton King when he tried to stop me again, then asked the Guild members who had gone rigid like statues.

“Is anyone here capable of Teleport? Hands.”

“H-Hand.”

A mage raised his hand without thinking and asked with a dazed expression,

“B-But where are we going?”

“Jongno. No……”

I looked at the old butler who had fallen into a sleep from which he would never awaken, then continued.

“Let’s go to Ares Guild.”
```

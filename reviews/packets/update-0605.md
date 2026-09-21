<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0605.txt",
      "sha256": "2c614de59adefc30231630746bddc6745c68f779855c621cb9c0174748ac4ebc",
      "bytes": 13797
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "ebede614938cd29f512f994cfb9f356f0360438874c552b98f5d8aa18dc2ee27",
      "bytes": 2237
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "e92003b960eaa42eb9ed45410e4f31babad4c1342b16b7dedb12b9e1d0e4a307",
      "bytes": 187329
    },
    {
      "path": "characters/Cheon Taemin.md",
      "sha256": "ebfdcfda65fd770e259817ff38ad9885bf1bb3323e19c049e45e400ee3d44569",
      "bytes": 743
    },
    {
      "path": "characters/Cheonwoo.md",
      "sha256": "9d4da20e1006234934460fda8a907cdcfa2fe32fabc6246949cafa227dc95cc3",
      "bytes": 590
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "6a0072cc925837e56fd6d4917389e9eeb513d3438c67ef2eb4ba4e312f3e12a0",
      "bytes": 553
    },
    {
      "path": "characters/Human Butcher.md",
      "sha256": "237ef129473ba9fc67307861863b0364ff46868e4d144526be4ba3318cc9d4cd",
      "bytes": 667
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "eddcec0ea068fe1dac477fd8c5e7a108e61cd0863c82237c9711c76a561c8059",
      "bytes": 1797
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "6a81eee3ea7b1c0a807335e1ed9bbb1806545a315d5c6e0b73f37912538399a5",
      "bytes": 622
    },
    {
      "path": "characters/Lee Jungryong.md",
      "sha256": "94f7594d1a93b23bbcefcd07a472c6ec9be1f32462d8af7c657b88e7554f38ce",
      "bytes": 1384
    },
    {
      "path": "characters/Song Cheonwoo.md",
      "sha256": "8e7735fee0088c30cb54459a75d077551c0b26cc8d84b35e67f3bf069ea0e723",
      "bytes": 1080
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "5a3f6eb71a5486eeeadd8d4e58693a61764d01b63806d846b0aef45fbb5002df",
      "bytes": 186685
    }
  ],
  "estimated_tokens": 11541
}
-->

# Durable State Update — Chapter 605

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 605. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 605. Profile updates may replace only one
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
  "chapter": 605,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 605,
    "continuity_sources": [605],
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
    "Cheon Taemin has been unconscious for more than twenty years and is hidden alive inside a wired mechanical capsule in a secret subspace within Ares Guild's Area A; Team Leader Choi has confirmed that Taemin is his maternal grandfather.",
    "Jin Taekyung discovered and opened the concealed Area A subspace using expanded Qi Sense and Force.",
    "The subspace is Lee Jungryong's private vault and prison, containing approximately five hundred Magic Gems, five S-grade Magic Gems, gold, diamonds, bonds, and priceless artwork.",
    "Lee Jungryong and Song Cheonwoo concealed Cheon Taemin's condition, and Choi Minwoo now controls the Guild power needed to investigate and relocate him.",
    "Choi Minwoo has publicly identified himself as Cheon Taemin's maternal grandson and only living blood descendant.",
    "Choi Minwoo is Guild Master of the Peace Guild and Vice Guild Master of Ares Guild.",
    "Baek Hanseong and Choi Minwoo have established a cooperative relationship concerning the two Guilds and the government's response.",
    "Go Se-won remains the person closest to the surviving secrets of Ares Guild and has not explained what debt he intends to repay to Jin Taekyung.",
    "Jin, Choi, and the Skeleton King are keeping Cheon Taemin's survival and location secret.",
    "Cheon Taemin must be moved covertly by teleportation magic with help from a trusted person who has been contacted but not identified."
  ],
  "continuity_sources": [
    603,
    604
  ],
  "open_questions": [
    "What caused Cheon Taemin to lose consciousness and remain in a vegetative state for more than twenty years?",
    "Who can provide the teleportation magic needed to move Cheon Taemin safely and covertly, and where can he be taken?",
    "What debt does Go Se-won mean to repay to Jin Taekyung?",
    "How will the authorities ultimately resolve the charges against Jin Taekyung?"
  ],
  "safe_through": 604,
  "temporary_decisions": [
    "Use Team Leader Choi for 최 팀장.",
    "Use Butler Kim for 김 집사.",
    "Use President's Security Service for 청와대 경호실.",
    "Use Grandfather for 외할아버지.",
    "Use Guild Association for 길드 협회."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 천태민    | **Cheon Taemin**  |
| 이정룡    | **Lee Jungryong** |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 살기     | **killing intent**                               |                                                       |
| 정파     | **orthodox faction**                             |                                                       |
| 상태               | **Status**                     |
| 퀘스트              | **Quest**                      |
| 보상               | **Reward**                     |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 몬스터     | **monster**           |
| 팀장      | **Team Leader**       |
| 사천     | **Sichuan**            |
| 도사      | **Daoist**                                                      |
| 천우 | **Cheonwoo** | Name shown in a Level Window; one of the five current Five Gates scions. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 송천우 | **Song Cheonwoo** | Ares Guild Director, former third-ranked Korean Hunter, and longtime European regional branch director. |
| 평화 | **Peace Guild** | Guild name. |
| 개방 | **Beggars' Sect** | Murim organization counted among the Nine Sects and One Gang. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 국밥 | **gukbap** | Korean dish of rice served in hot soup; footnoted in the reading copy. |
| 사자후 | **lion's roar** | Taekyung's term for Song Il's crowd-shattering roar. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 준이 | **Jun** | Family nickname used in the form Jun's dad. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 메이지 | **Mage** | Skeleton subtype mentioned alongside Soldiers and Warriors. |
| 존슨 | **Johnson** | Co-host of the American talk show that replays Taekyung's viral interview. |
| 만독지환 | **Myriad-Poison Ring** | Quest title concerning a legendary treasure said to detoxify any poison. |
| 데스나이트 | **Death Knight** | Undead commander type serving under the Black Knight. |
| 중단전 | **Middle Dantian** | Martial energy center opened by Jin during the battle. |
| 텔레포트 | **Teleport** | Taekyung's label for the Blood Lord's unexplained disappearance. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 이전 | **Two Halls** | Top-level Murim Alliance organizational grouping. |
| 순대국밥 | **blood sausage gukbap** | Taekyung's former inexpensive meal; retain gukbap with its established footnote. |
| 대마도사 | **Grand Mage** | Title used for Magic Johnson. |
| 정룡 | **Jungryong** | Cheon Taemin's trusted associate who joined the Peace Guild. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 이정룡 | 진태경 | senior S-rank Hunter to younger Hunter and adversary | Young man | polished, teasing, and veiled-threatening | Uses a genial tone and indirect threats while trying to make Taekyung release the captives. |
| 진태경 | 이정룡 | younger Hunter to senior S-rank Hunter and adversary | you | polite but mocking and defiant | Taekyung answers Lee's soft threats with the wolf-and-tiger metaphor and refuses to yield. |
| 이정룡 | 천태민 | younger_to_older_brother_by_choice | older brother | reverent and familiar; internal | Lee Jungryong uses 형님 in unspoken thoughts and regards Cheon Taemin as an older brother despite having no blood relation. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 데스나이트 | 인간 | enemy combatants | human | contemptuous and commanding | Used in the Death Knight's warnings to Jin. |
| 진태경 | 엄마 | son_to_mother | Mom | casual and startled | Jin cries out to his mother as she charges at him during the hospital visit. |
| 진태경 | 존슨 | Allied Hunter to Grand Mage | Johnson | polite and familiar | Jin repeatedly addresses Magic Johnson directly while requesting explanations and permission to visit the site. |
| 엄마 | 진태경 | mother_to_son | my son | warm and affectionate | Taekyung's mother praises him during the public welcome. |
| 아빠 | 진태경 | father to son | Taekyung | affectionate informal | Addresses his young son warmly as Taekyung. |
| 진태경 | 아빠 | son to father | Dad | childlike informal | Taekyung addresses his father as Dad in the childhood flashback. |
| 송천우 | 천태민 | former subordinate to revered older brother by respect | Hyung | reverent and familiar; shocked | Song Cheonwoo recognizes Cheon Taemin's blood in Choi Minwoo and mutters 형님 while facing Choi. |

## Listed compact profiles

### Cheon Taemin.md

# Cheon Taemin (천태민)

- **Safe through:** Chapter 604
- **Aliases:** Slayer
- **Role:** Cheon Taemin is Ares Guild Master and the world's greatest Hunter, known as the Slayer for killing the Demon King and creating the first Mana Cultivation Method during the Great Cataclysm; he has been unconscious for more than twenty years inside a wired mechanical capsule hidden in a secret subspace within Ares Guild's Area A.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** Maternal grandfather of Team Leader Choi and Jin Taekyung and father of Soyeong; regarded by Lee Jungryong as an older brother despite their lack of blood relation.

### Cheonwoo.md

# Cheonwoo (천우)

- **Safe through:** Chapter 603
- **Aliases:** None
- **Role:** One of the five current Five Gates of Shanxi scions and a First Rate martial artist present at Honghwa Inn.
- **Personality:** Pampered and contemptuous toward Cheongpung's group as part of the five scions' collective mockery.
- **Voice:** Mocking in the group's exchange; no distinct individual speech is established.
- **Relationships:** Associates with Seongryong, Myeonghwa, Sohye, and Jintae as a group of current Five Gates scions.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 604
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Human Butcher.md

# Human Butcher (인도)

- **Safe through:** Chapter 603
- **Aliases:** None
- **Role:** Former mysterious Han Chinese mounted-bandit power in Northern Gaoyuan commanding fifty subordinates; a Peak master killed by an unnamed old man in a single move
- **Personality:** Cold, intimidating, and murderous; he kills people as though slaughtering livestock
- **Voice:** Cold, curt, and quietly threatening
- **Relationships:** He is one of four powerful participants at the Northern Gaoyuan gathering, intimidates Temur, and has claimed Ghost Sword Wipeng as his personal target in the proposed attack

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 604
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, a Supreme Peak master with the Heavenly Martial Physique and Force, publicly recognized as an S-rank-level Hunter while formally retaining an A-rank license; his Middle Dantian is partially activated at 10%, slightly improving the efficiency of his martial arts and internal energy.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor and assigned him a final task to incorporate martial principles into his learned martial arts but declined Taekyung's recruitment after Cheongpung reached him first, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate, student, and trusted manager of media and official arrangements, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, and Xiao Shen regards him as an older brother after Jin saved him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 604
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Lee Jungryong.md

# Lee Jungryong (이정룡)

- **Safe through:** Chapter 604
- **Aliases:** None
- **Role:** Former Vice Guild Master of Ares Guild, one of Korea's two S-rank Hunters, and a Supreme Peak-level martial artist who was killed by Jin Taekyung.
- **Personality:** Outwardly genial, calm, and humorous; calculating, opportunistic, manipulative, coercive, and ruthless when challenged
- **Voice:** Smooth, good-natured, and indirect, using teasing conversation and veiled threats before becoming openly furious
- **Relationships:** Master of Park Jihoon and Go Jun (Team Leader Seok), whom he personally selected and trained; longtime Great Cataclysm acquaintance of Park Tae Seop; adversary of Jin Taekyung; knew Team Leader Choi from childhood; has an antagonistic history with Kim Hwajong, who saved his life at the collapse of Mapo Bridge eighteen years earlier; was visibly shaken by learning that Choi is Cheon Taemin's maternal grandson; regarded Cheon Taemin as an older brother despite no blood relation and long held him in respect and fear; secretly supported the orphanage where Lee Dongseok grew up and was regarded by Dongseok as a father; operated as Ares Guild's senior authority beneath its Guild Master; concealed Taemin's condition with Song Cheonwoo and participated in purging aides who knew the truth.

### Song Cheonwoo.md

# Song Cheonwoo (송천우)

- **Safe through:** Chapter 603
- **Aliases:** Director Song
- **Role:** Ares Guild Director and former A-rank Hunter who reached third place among Korean rankers, briefly headed the Hunter training center, and led Ares Guild's European regional branch for twenty years; after being forced to attack Choi Minwoo to protect his hostage family, he fell into an abyss and was killed by an unidentified monster.
- **Personality:** Highly ambitious, honor-obsessed, politically calculating, and determined to use his final opportunity to reclaim influence before retirement.
- **Voice:** Not established.
- **Relationships:** Song Cheonwoo followed Cheon Taemin since before Team Leader Choi was born, was Lee Jungryong's former friend and rival, helped conceal Taemin's condition and purge aides who knew the truth, negotiated the European regional director position to save himself and his family, and had his children seized by Go Jun as leverage that forced him to attack Choi Minwoo.

## Korean source

```text
＃605화



- 제이콥. 그쪽 상황은 어떤가요? 혹시 다친 건 아니죠?

홀로그램 TV 속. 짙게 눈화장을 한 동양계 여성 아나운서의 물음에 현장에 나가 있던 건장한 흑인 기자가 눈을 찡긋하며 대답했다.

- 제니가 걱정해 준 덕분에 다행히도 무사해요. 다른 분들도 마찬가지고요.

- 변이 게이트가 발생한 현장치고는 믿을 수 없을 만큼 평화로워 보이네요.

- 물론입니다. 다친 사람도 없고 상황도 순식간에 마무리되었거든요. 더군다나 이곳은 텍사스입니다. 남녀 가릴 것 없이 모두가 터프하죠.

- 하하. 그것참 다행이네요. 그런데 위험한 상황 속에서 모두를 구한 영웅은 어디 있나요?

- 제니, 당신과 시청자 여러분께 사과드려야겠어요. 오늘 이 자리를 빛낼 영웅, 매직 존슨은 이미 떠났거든요. 저도 최대한 노력했지만 붙잡을 수 없었어요.

- 아, 저런.

- 급한 일이 있다며 인터뷰를 거절하고 사라져 버리는데, 얼마나 다급해 보였던지 저는 숨겨 둔 애인이라도 만나러 가는 줄 알았다니까요.

- 그렇군요. 그나저나 제이콥, 이번 변이 게이트의 정확한 원인이…….

음. 숨겨 둔 애인이라.

소파에 기댄 채 홀로그램 TV를 시청하던 나는 무심코 흥얼거렸다.

“아빠가 출근할 때 뽀뽀뽀. 매직 존슨 한국 와서 뽀뽀뽀.”

쉭, 파창!

파공성과 동시에 고개를 숙이자, 아슬아슬하게 목덜미를 스친 크리스털 유리잔이 홀로그램 TV를 박살 낸다.

사방으로 튄 파편과 바닥에 흥건하게 고인 물. 순간 나와 시선이 마주친 최 팀장이 담담한 표정으로 입을 열었다.

“아, 이걸 피하네.”

“…….”

“오해하실까 봐 드리는 말씀인데, 고의 맞습니다.”

“……실수라고 변명도 안 하시네.”

“실수가 아니었으니까요. 그나저나 정말 아쉽네요. 조금만 더 빨랐으면 진태경 씨 대가리를…….”

“아니, 사람한테 대가리가 뭡니까. 대가리가.”

“그 방정맞은 아가리를 함부로 놀리니까 대가리 소리가 나오는 겁니다. 사실 진태경 씨 같은 돌머리한테는 대가리라는 단어도 아까워요.”

“어어? 대가리? 아가리?”

“이제부터 제 앞에서 잠들 생각 마십시오. 아가리 벌리고 자면 청산가리 쏟아부을 겁니다.”

“…….”

펀치 라인 미친 건가.

얼마나 열이 받았는지, 씹어뱉는 듯한 말투와 그 안에 스며든 독기에 말문이 턱 막힐 정도다.

잠시 만독지환을 꺼낼까 고민하던 나는 점잖게 손을 내저었다.

“최 팀장님. 진정해요, 진정. 내가 다 잘못했어.”

“지금 진정하게 생겼습니까?”

“아니, 그 상황에서는 어쩔 수 없었다니까. 뉴스 봤잖아요. 변이 게이트 상황 때문에 바쁘다는데 어떡해? 우선은 불러내야지.”

“그렇다고 제 입술을 마음대로 걸어요?”

“킹치만 내 입술을 걸 수는 없었는걸?”

“……!”

쉭! 파창!

와, 이번에는 진짜 위험했다.

다시 한번 아슬아슬하게 공격을 피한 내가 황급히 외쳤다.

“그만! 팀장님! 그만!”

최 팀장이 세 번째 크리스털 잔을 집어 들며 대답했다.

“아가리 다물고 대십시오. 딱 대.”

“뽀뽀 안 했잖아요! 결국 안 했잖아!”

“할 뻔했잖습니까!”

최 팀장이 사자후 뺨치는 포효와 함께 팔을 휘두르려던 그때였다.

벌컥.

노크도 없이 열린 문 앞. 잔뜩 기대감에 차 있는 스켈레톤 킹과 시무룩해 있는 매직 존슨이 보였다.

“작업 끝났는데. 이제 클럽 가나?”

「최, 나도 순정이 있는 사람이야.」

클럽무새와 순정파 대마도사를 말없이 응시하던 최 팀장이 한숨과 함께 손을 내렸다.



* * *



매직 존슨은 뛰어난 워 메이지(War Mage)이기 이전에 대다수의 마법을 구사할 수 있는 대마도사.

연락을 받고 곧장 한국으로 이동한 그에게 우리는 곧장 사실을 털어놓았다.



‘미스터 존슨. 사실은 옮겨야 할 것이 있는데…….’

‘무슨 이유에서건 상관없어. 우선 그 전에 Ppoppo를 받고 싶군. 준비됐지, 최?’

‘아직 준비 안 됐고, 앞으로도 안 될 거고, 영원히 그럴 겁니다.’

‘그럼 곤란하지. 이렇게 극비리에 무슨 물건을 옮기려는지는 몰라도…….’

‘저기, 물건이 아니라 정확히는 사람인데요.’

‘그게 무슨 소리야, 진? 사람이라니? 누굴 도피라도 시키나?’

‘도피라는 말이 적당할지는 모르겠는데, 비슷합니다.’

‘누군데? 설마 극악무도한 범죄자? 아니면 숨겨 둔 애인?’

‘제 외조부십니다.’

‘Oh, Shit. 미안해, 최. 그럴 의도는 아니었는…… 잠깐. 방금 누구라고?’



정황을 모두 들은 후에도 한참이나 말이 없던 매직 존슨은, 직접 천태민의 얼굴을 확인한 후에야 비로소 입을 열었다.



‘빌어먹을. 이게 도대체 무슨 일이야?’

‘보시는 바와 같이 개 같은 경우죠.’

‘통화로 자세히 말하지 못했던 이유가 있었군. 좋아, 당장 급한 것부터 처리하자고. 최, 이분을 이 감옥 같은 곳에서 어디로 옮겨야 하지?’



그 후로는 일사천리였다.

매직 존슨은 최 팀장으로부터 전달받은 좌표로 텔레포트 마법을 펼쳤고 우리 모두는. 아니, 깨어나기 힘든 깊은 잠에 빠진 한 사람은 과거 자신이 머물렀던 저택으로. 그리운 집으로 돌아올 수 있었다.

장장 이십여 년 만의 일이었다.

「공간 왜곡에 결계. 방어 마법은 기본이고 습도 및 온도 조절까지 걸어 뒀어. 또…….」

비트 위의 나그네처럼 쉴 새 없이 온갖 종류의 마법을 읊어 대던 매직 존슨이 숨 가쁜 한마디로 말을 끝맺었다.

「그러니까, 현재 내가 할 수 있는 조치는 모두 취해 뒀다고 보면 돼. 아직 추가 작업이 필요하지만.」

클럽에 가지 못하게 되어 심통이 난 스켈레톤 킹이 중얼거렸다.

“대단한 건 알겠는데, 그게 어느 정도라는 거냐?”

「나와 같은 반열에 있는 대마도사. 혹은 S급 헌터 두세 명이 달려들어서 작정하고 때려 부수지 않는 한 멀쩡하다는 뜻이지.」

“성능 한번 확실하군.”

스켈레톤 킹의 말에 동감이다. 매직 존슨은 정말 말 그대로 현재 자신이 할 수 있는 모든 조치를 취해 놓았다.

어지간한 S급 헌터조차 천태민의 존재와 위치를 알아차릴 수 없게끔.

‘전투계와 마법계는 궤가 다르니까.’

무공 수련에 끝이 없는 것처럼, 마법 역시 마찬가지다.

나 역시 중단전(中丹田)을 개방하지 않았다면 이토록 쉽게 천태민을 찾을 수 없었을 것이다.

「그런데 이 중에 그 비밀 공간을 만든 인물이 누구인지 아는 사람이 있나? A구역이라는 곳도 그렇고, 설치된 마법의 수준이 결코 내 아래가 아니던데.」

“이 몸은 잘 모르겠다. 인간이여.”

나는 냉큼 대답한 스켈레톤 킹의 어깨를 점잖게 두드려 주었다.

“아는 사람이 있냐고 물었잖아. 몬스터가 아니라.”

“넌 지인짜 개새끼다.”

음. 어휘력이 나날이 발전해 가는군.

빡!

어휘력 상승 퀘스트 보상으로 녀석의 뒤통수를 갈겨 준 나는, 매직 존슨을 향해 물었다.

“저도 그게 궁금하긴 한데. 혹시 짐작 가는 사람이라도 있으세요?”

「흠, 글쎄. 따지고 보면 결국 나와 같은 대마도사밖에 없겠지. 그 정도 수준의 마법이라면 더더욱.」

“그럼 혹시…….”

「그 두 사람이냐고?」

미심쩍은 표정으로 입을 다문 내 모습에, 매직 존슨이 사뭇 진지한 표정으로 고개를 저었다.

「아마도 아닐 거야. 다만 짐작 가는 사람이 아주 없는 것도 아니지.」

“짐작 가는 사람이요?”

「음.」

침음성을 흘리며 뭔가 생각에 잠겨있던 매직 존슨이 말을 이었다.

「여기에 관해서는 말을 아끼지. 아직 확신하기에는 일러. 하지만 혹시 모르니 다른 대마도사들을 찾아가 보긴 해야겠군. 얼굴 본 지도 오래됐으니.」

“그럼 감사하죠.”

듣던 중 반가운 소리였다. 대마도사답게 뛰어난 통찰력을 지닌 매직 존슨이 직접 진위 여부를 가리겠다는 뜻이니까.

‘현재 전 세계를 통틀어 대마도사는 단 세 명.’

만약 이정룡의 의도를 빤히 아는 상태에서 그런 의뢰를 받은 대마도사가 있다면…… 이건 결코 넘어갈 수 없는 문제다.

재앙으로부터 인류를 구한 영웅을 죄인처럼 유폐(幽閉)시키는 것에 동조한 죄는 반드시 따져 물어야 한다.

한 사람을 위해서라도.

“최 팀장님.”

내 부름에도 최 팀장은 못 박힌 듯 서 있었다.

차가운 금속으로 이루어진 타원형의 동면 장치 내부, 깊은 잠에 빠진 자신의 외조부를 하염없이 바라보던 그가 문득 입을 열었다.

“정말 오랫동안 기다렸는데…… 깨어나지 못하시는군요.”

어설픈 위로는 안 하는 것만 못하다. 그 사실을 알기에 우리 중 그 누구도 쉽게 입을 열지 못했다.

불멸의 영웅, 천태민은 여전히 의식을 회복하지 못하고 있었다.

‘그것도 무려 이십여 년 전부터.’

원인도, 이유도 모른다. 안타깝게도 최 팀장이 송천우에게 들었다는 이야기들은 전부 사실이었다.

이정룡과 송천우. 두 야망가들 역시 한때 그를 깨우기 위해 백방으로 노력했지만 끝내 결실을 얻지 못했다.

이런 답답한 상황 속에서 지금 당장 우리가 할 수 있는 말은 하나뿐이었다.

“분명히 방법이 있을 겁니다.”

「진의 말이 맞아. 과정이 없는 결과가 존재하지 않듯이, 이유 없는 병 역시 마찬가지지.」

“힘내라. 확실히 아직 죽지는 않았다. 설령 죽는다 해도 이 몸이 데스나이트로 부활시킬 방법을 찾아볼…….”

순간 쏟아진 나와 매직 존슨의 살기 어린 시선에, 말을 멈춘 스켈레톤 킹이 더듬더듬 변명을 내놓았다.

“위, 위로해 주려고 한 말이다.”

“그게 위로냐. 이 시벌놈아?”

「몬스터 머더 퍼커…….」

혹여 들리기라도 할까 싶어 모기만 한 목소리로 스켈레톤 킹을 윽박지르던 그때, 흐릿한 미소를 머금은 최 팀장이 입을 열었다.

“괜찮습니다. 어떻게든 방법을 찾을 수 있겠지요. 살아 계시다는 것만으로도 다행입니다.”

단지 웃고 있다고 해서 즐겁다는 뜻은 아니다.

나도, 매직 존슨도. 심지어 눈치라고는 손가락뼈만큼도 없는 스켈레톤 킹조차도 지금 최 팀장으로부터 전해지는 감정을 느낄 수 있었다.

그리고 약속이라도 한 것처럼 동시에 입을 다문 우리를 향해, 깊게 가라앉은 최 팀장의 목소리가 귓가를 파고들었다.

“하지만…… 적어도 오늘만큼은 쉬고 싶군요. 모두 고생하셨습니다. 정말 감사드립니다.”

차례차례 우리를 바라본 그가 진심을 담아 고개를 숙인다.

그 인사의 의미를 알아차린 나는 가장 먼저 입구를 향해 걸음을 옮겼다.

자그마치 20여 년 만의 재회다. 지금은 서로를 향해 인사 한마디 나눌 수 없는 조손(祖孫)을 위해 자리를 비켜 줘야 할 때였다.



* * *



한국인에게 가장 중요한 것 중 하나가 바로 밥이다.

밥은 먹고 다니냐. 나중에 시간 되면 밥 한번 먹자. 좆밥이냐.

마지막에 좀 이상한 게 끼어 있긴 한데, 욕에서조차 밥이 등장하는 것이 바로 한국 문화라는 거다.

그 말인즉슨, 한국 사람이 일을 끝마쳤으면 함께 밥을 먹어야 하고. 그중 최고는 국물이 있는 밥이라는 뜻이다.

「Gugbab? 이게 뭐지?」

미심쩍은 표정으로 엄마표 순대국밥을 관찰하던 매직 존슨이 수저를 내려놓았다.

「헤이, 진. 토스트 없나?」

“그러지 말고 한 번 드셔 보세요.”

「아냐, 괜찮아. 배 안 고파.」

꼬르르륵.

「……토스트. 정말 없어?」

“있어도 없어요. 정 그러시면 우선 국물만이라도 드셔 보세요. 국물만.”

「제기랄. 코리안 수프 맞아? 왜 이렇게 괴상하게 생겼어?」

투덜거리며 숟가락을 집어든 매직 존슨이 어설픈 손놀림으로 국물을 떠먹었다.

그리고 그것은 게임이 끝났음을 의미했다.

「크어어어어. Fuck Yeah.」

뻑예를 연발하며 순대국을 두 그릇이나 해치운 매직 존슨이 흐뭇하게 웃었다.

「오늘 워낙 사고가 많이 터져서 하루 종일 바빴는데, 이제야 좀 살 것 같군.」

“안 그래도 아까 뉴스 봤어요. 변이 게이트 진압하고 인터뷰도 안 하고 곧장 오셨던데.”

「변이 게이트? 혹시 뉴스 끝까지 안 봤나?」

못 봤지. 최 팀장이 크리스털 잔으로 개박살을 냈으니까.

나는 어깨를 으쓱하며 되물었다.

“왜요?”

「봤으면 그런 소리를 못 했을 테니까.」

매직 존슨이 이쑤시개를 집어 들며 말을 이었다.

「정확히 말하자면, 변이 게이트가 아니었어.」

“예?”

이건 또 뭔 소리야?
```

## Final English reading copy

```markdown
# Chapter 605

“Jacob. How’s the situation over there? You’re not hurt, are you?”

On the holographic TV, an East Asian female anchor with heavily made-up eyes was asking the question. The sturdy Black reporter stationed at the scene winked and answered.

“Thanks to Jenny worrying about me, I’m safe and sound. Everyone else is fine, too.”

“It looks unbelievably peaceful for the site of a Mutated Gate.”

“Of course it does. No one was hurt, and the situation was wrapped up in an instant. Besides, this is Texas. Everyone here is tough, men and women alike.”

“Haha. That’s a relief. But where is the hero who saved everyone in that dangerous situation?”

“Jenny, I’m afraid I owe you and the viewers an apology. The hero who was supposed to grace today’s broadcast, Magic Johnson, has already left. I tried my best, but I couldn’t hold him back.”

“Oh, dear.”

“He refused the interview and disappeared, saying he had something urgent to take care of. He looked so desperate that I thought he was going to meet a secret lover.”

“I see. Anyway, Jacob, about the exact cause of this Mutated Gate…”

Hmm. A secret lover.

Leaning against the sofa and watching the holographic TV, I absentmindedly began to hum.

“When Dad goes to work, Ppoppo. Magic Johnson comes to Korea, Ppoppo.”[^1]

Whoosh! Crash!

I ducked at the sound of something slicing through the air, and a crystal glass narrowly grazed the back of my neck before smashing into the holographic TV.

Shards flew in every direction, and water pooled across the floor. Team Leader Choi, whose eyes met mine, calmly opened his mouth.

“Oh, you dodged that.”

“…”

“I’m telling you this so you don’t misunderstand. It was intentional.”

“…You’re not even going to claim it was an accident?”

“Because it wasn’t an accident. Still, it’s a real shame. If that had been just a little faster, it would’ve smashed Mr. Jin Taekyung’s skull…”

“Hey, you don’t call a person’s head a ‘skull.’ A skull?”

“You keep flapping that obnoxious trap of yours, so yes, I’m calling it a skull. Frankly, even the word ‘skull’ is wasted on a blockhead like you.”

“Whoa, what? ‘Skull’? ‘Trap’?”

“From now on, don’t even think about falling asleep in front of me. If you sleep with your mouth open, I’ll pour cyanide down it.”

“…”

Was that punchline insane or what?

He must have been furious. His words came out as if he were spitting them through clenched teeth, and the venom seeping through them left me momentarily speechless.

I briefly considered taking out the Myriad-Poison Ring, then calmly waved a hand.

“Team Leader Choi. Calm down, calm down. I was completely wrong.”

“Do I look like I can calm down right now?”

“I couldn’t help it in that situation. You saw the news. They said he was busy dealing with a Mutated Gate. What else could I do? I had to get him here first.”

“Even so, do you get to put my lips on the line without asking?”

“But I couldn’t put my own lips on the line, could I?”

“……”

Whoosh! Crash!

Whoa. That one had genuinely been dangerous.

After narrowly dodging the attack once again, I hurriedly shouted.

“Stop! Team Leader! Stop!”

Team Leader Choi picked up a third crystal glass and answered.

“Shut your mouth and stick your head out. Right there.”

“I didn’t kiss him! I didn’t do it in the end!”

“You almost did!”

Team Leader Choi was just about to swing his arm with a roar that could rival a lion’s roar when—

Bang.

The door opened without a knock.

In front of it stood the Skeleton King, brimming with anticipation, and Magic Johnson, looking thoroughly dejected.

“The job’s done. Are we going to a club now?”

「Choi, I’m a romantic too.」

Team Leader Choi stared silently at the club-obsessed parrot and the pure-hearted Grand Mage. Then, with a sigh, he lowered his hand.

* * *

Magic Johnson was not merely an outstanding War Mage, but first and foremost a Grand Mage capable of wielding most forms of magic.

After receiving our call and coming straight to Korea, he heard everything from us.

“Mr. Johnson. There’s something we need to move, actually…”

“Whatever the reason, I want my Ppoppo first. You’re ready, Choi?”

“I’m not ready, I won’t be ready, and I never will be.”

“Then that’s a problem. I don’t know what kind of object you’re trying to move in such strict secrecy, but…”

“Um, it isn’t an object. It’s a person, to be exact.”

“What do you mean, Jin? A person? Are you helping someone escape?”

“I’m not sure whether ‘escape’ is the right word, but it’s similar.”

“Who is it? A heinous criminal? Or a secret lover?”

“He’s my maternal grandfather.”

“Oh, shit. Sorry, Choi. I didn’t mean to—wait. Who did you just say?”

Even after hearing the entire story, Magic Johnson remained silent for a long time. He didn’t speak until he had personally confirmed Cheon Taemin’s face.

“Damn it. What the hell happened here?”

“As you can see, it’s a dogshit situation.”

“There was a reason you couldn’t explain everything over the phone. All right, let’s take care of the urgent matter first. Choi, where are we moving him from this prison-like place?”

After that, everything proceeded at breakneck speed.

Magic Johnson cast Teleport using the coordinates Team Leader Choi had given him, and all of us—no, one person among us, locked in a deep sleep he could not easily wake from—was able to return to the mansion where he had once lived.

To the home he had missed.

It was a return more than twenty long years in the making.

「Space distortion and barriers. Defensive magic is a given, and I’ve even set up humidity and temperature controls. And…」

Like a traveler wandering across a beat, Magic Johnson rattled off every kind of magic without pause before finishing with a breathless sentence.

「So, you can assume that I’ve taken every measure I’m currently capable of taking. Though additional work is still needed.」

The Skeleton King, sulking because he couldn’t go to a club, muttered.

“I understand that it’s impressive, but how impressive are we talking?”

「It means that this place will remain intact unless a Grand Mage on my level—or two or three S-rank Hunters—deliberately attacks it with the intention of smashing it to pieces.」

“That’s some serious performance.”

I agreed with the Skeleton King. Magic Johnson had quite literally taken every measure he could.

He had even made it impossible for most S-rank Hunters to detect Cheon Taemin’s existence or location.

*The combat and magic disciplines operate on different tracks.*

Just as martial arts training had no end, magic was the same.

If I hadn’t opened my Middle Dantian, I would never have been able to find Cheon Taemin so easily.

「By the way, does anyone here know who created that secret space? The same goes for this place called Area A. The level of the magic installed here is definitely not beneath me.」

“This body does not know, human.”

I promptly patted the Skeleton King’s shoulder with dignity.

“He asked whether anyone knew. He wasn’t asking a monster.”

“You’re a real fucking bastard.”

Hmm. His vocabulary was improving every day.

Smack!

After giving him a blow to the back of the head as a reward for his improved vocabulary, I turned to Magic Johnson.

“I’m curious about that, too. Do you have anyone in mind?”

「Hmm, let me think. When you get right down to it, the only people who could have done it are Grand Mages like me. Especially if the magic really is at this level.」

“Then, perhaps…”

「Are you asking whether it was those two?」

I had fallen silent with a doubtful expression, and Magic Johnson shook his head with an unusually serious look.

「Probably not. But it isn’t as if I have no one in mind.」

“Someone you have in mind?”

「Hmm.」

Magic Johnson let out a low hum and seemed to sink into thought before continuing.

「I’ll say no more about this for now. It’s too early to be certain. But just in case, I should visit the other Grand Mages. It’s been a long time since I’ve seen them, anyway.」

“Then I’d appreciate that.”

That was welcome news. Magic Johnson was a Grand Mage with exceptional insight, and he intended to determine the truth for himself.

*There are currently only three Grand Mages in the entire world.*

If a Grand Mage had accepted a request while fully aware of Lee Jungryong’s intentions…

This was not something we could simply let go.

Anyone who had helped imprison a hero who saved humanity from disaster as though he were a criminal would have to answer for that crime.

Even if it was only for one person.

“Team Leader Choi.”

Despite my call, Team Leader Choi remained frozen in place.

Inside the oval-shaped hibernation device made of cold metal, he gazed endlessly at his maternal grandfather, who had fallen into a deep sleep. Then he suddenly spoke.

“I’ve waited for so long… but you still haven’t woken up.”

A clumsy attempt at consolation would have been worse than saying nothing. Knowing that, none of us could bring ourselves to speak easily.

The immortal hero, Cheon Taemin, still hadn’t regained consciousness.

*For more than twenty years.*

We knew neither the cause nor the reason. Unfortunately, everything Team Leader Choi had heard from Song Cheonwoo had been true.

Lee Jungryong and Song Cheonwoo, those two ambitious men, had once tried every possible way to wake him. But in the end, they had achieved nothing.

In this frustrating situation, there was only one thing we could say right now.

“There must be a way.”

「Jin is right. Just as there can be no result without a process, there can be no illness without a reason.」

“Keep your chin up. He definitely isn’t dead yet. Even if he dies, this body will find a way to revive him as a Death Knight…”

The Skeleton King stopped when killing intent poured from both Magic Johnson and me. He stammered out an excuse.

“I-I was trying to comfort him.”

“That’s comfort? You fucking asshole?”

「Monster motherfucker…」

I was berating the Skeleton King in a voice no louder than a mosquito’s buzz so Team Leader Choi wouldn’t overhear when Choi spoke with a faint smile.

“It’s all right. We’ll find a way somehow. It’s a relief that he’s alive.”

Just because someone was smiling didn’t mean they were happy.

I could feel the emotion coming from Team Leader Choi. So could Magic Johnson. Even the Skeleton King, who had not a single finger bone’s worth of tact, could feel it.

And as though we had made a promise, all three of us fell silent.

Team Leader Choi’s voice, sunk deep with emotion, pierced my ears.

“But… at least today, I’d like to rest. Thank you all for your hard work. I truly appreciate it.”

He looked at us one by one, then bowed his head sincerely.

I understood the meaning of that gesture and was the first to walk toward the entrance.

This was a reunion that had come after more than twenty years. For a grandfather and grandson who could not even exchange a single greeting right now, it was time for us to leave them alone.

* * *

One of the most important things to Koreans was rice.

“Have you eaten?”

“Let’s get a meal together sometime when you have time.”

“Are you a rice-dick?”[^2]

The last one was a little strange, but even curses involved rice. That was Korean culture for you.

In other words, when a Korean finished a job, they had to share a meal. And the best kind of meal was rice served in broth.

「Gugbab? What is this?」

Magic Johnson examined Mom’s homemade blood sausage gukbap[^3] with a suspicious expression before putting down his spoon.

「Hey, Jin. Do you have any toast?」

“Come on, just try it.”

「No, it’s fine. I’m not hungry.」

Grrrrr.

「…You really don’t have any toast?」

“Even if there were some, there isn’t. If you’re that reluctant, just try the broth. The broth alone.”

「Damn it. This is Korean soup? Why does it look so strange?」

Grumbling, Magic Johnson picked up his spoon and awkwardly scooped up some broth.

Then he tasted it.

And that meant the game was over.

「Kheeeee. Fuck yeah.」

After repeatedly shouting “Fuck yeah” and devouring two bowls of blood sausage gukbap, Magic Johnson smiled in satisfaction.

「There were so many things going wrong today that I was busy all day. I feel like I can finally breathe.」

“I saw the news earlier, actually. You subdued the Mutated Gate and came straight here without even doing an interview.”

「The Mutated Gate? Did you not watch the news to the end?」

*I couldn’t. Team Leader Choi smashed the TV with a crystal glass.*

I shrugged and asked back.

“Why?”

「Because if you had, you wouldn’t have said that.」

Magic Johnson picked up a toothpick and continued.

「To be precise, it wasn’t a Mutated Gate.」

“What?”

What the hell was he talking about now?

[^1]: “Ppoppo” is Korean baby-talk for a kiss. The line also alludes to *Ppoppo Ppoppo*, a Korean children’s TV program.

[^2]: “Jjotbap” is a vulgar Korean word for a weakling, literally combining “dick” with “rice.”

[^3]: *Gukbap* is a Korean dish of rice served in hot soup. Here, the dish is made with *sundae*, a Korean blood sausage.
```

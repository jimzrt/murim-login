<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0751.txt",
      "sha256": "cc12a0c9798423ae1c92b2dbc244b81f06df5691fff00ac7ab26723034488b0d",
      "bytes": 13550
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "d2626d7fb96c4557758d07c1444cef1069241396fb1b23a3a82acd2c58ee950f",
      "bytes": 2859
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "ff620f70ccdd4d36bc51d8e050777514b1bf2ff1fab814963b33dfc459bd0cd5",
      "bytes": 217680
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "bb316bcc96944df09fb09584b7ec94beceb91a7ac485c31ab9f06f18c83328b0",
      "bytes": 553
    },
    {
      "path": "characters/Go Jun.md",
      "sha256": "51344c2a074a1cdb88605d1c9187f3d3e4e5cf98a518f78ff0d8ae4d2555adbd",
      "bytes": 817
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "6d7ec679350225a3f233e04906becc18387e4eef653ca4f317f01a067075f0e8",
      "bytes": 2011
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "1d8e9675912e3a71fdbba07262994282471ea92901fd34f09325188841e9a34e",
      "bytes": 622
    },
    {
      "path": "characters/Lee Jungryong.md",
      "sha256": "d9cd33b5a7a2562bd576055720b0ea6844d45b1b508887d20cd57f1876141733",
      "bytes": 1384
    },
    {
      "path": "characters/Leviathan.md",
      "sha256": "4218d4df82ea15ea913da133e1164377e2482401d00b64e759686060c3d264bc",
      "bytes": 711
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "95fe2f6cf9cf3c1a470510224da962b5b21dd0ffa96287c5c32546bbdcc0979f",
      "bytes": 230777
    }
  ],
  "estimated_tokens": 11200
}
-->

# Durable State Update — Chapter 751

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 751. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 751. Profile updates may replace only one
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
  "chapter": 751,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 751,
    "continuity_sources": [751],
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
    "The Prophet commands the revived Hasasin and has announced a second series of terrorist attacks after Allah's Judgment.",
    "The Prophet can create a transparent concealment barrier that cannot be detected by science or Magic.",
    "The Prophet possesses at least ten unrefined S-rank Magic Gems that retain their original power.",
    "Siegfried Wassmann was found dead in his sealed hideout after his life force was apparently drained by unknown magic.",
    "Michael Silbert remains the strongest suspect in Siegfried's death and has entered the Japanese battlefield while pursuing his ambition to become the undisputed best.",
    "Jin has accepted the Supreme Peak Quest Unknown Death, whose mission is to discover the truth behind Siegfried's death.",
    "Michael and Huginn continue manipulating events and media coverage against Jin, while Huginn's completed undisclosed operation remains unresolved.",
    "Magic Johnson is investigating stolen research materials from Siegfried's laboratory but has not yet produced results.",
    "Japan's failed response to Leviathan's attack has left roughly one hundred thousand confirmed casualties, and Prime Minister Koizumi is now handling talks with the Korean forces.",
    "Leviathan is severely wounded, has swallowed the Magic Gem it sought, and escaped Jin's follow-up spear attack into the deep sea.",
    "Jin's Broken Body debuff remains active after a Top-Grade Potion removed his other status abnormalities, leaving his combat attributes reduced and risking permanent loss.",
    "The Skeleton King invoked the vengeful spirits of Pearl Harbor during the Japanese command meeting, causing an unexplained supernatural disturbance that Jin interrupted."
  ],
  "continuity_sources": [
    749,
    750
  ],
  "open_questions": [
    "Who killed Siegfried Wassmann, by what magic, and did Michael Silbert order his death?",
    "What is The Prophet's identity, and how are the Prophet's terrorist campaign and Leviathan's reappearance connected?",
    "What is Huginn's undisclosed operation, and can its consequences actually bring Jin down?",
    "Can Jin track Leviathan after the failed spear attack, and what consequences will follow from the Magic Gem Leviathan swallowed?",
    "What occurred after the Skeleton King invoked the vengeful spirits of Pearl Harbor?"
  ],
  "safe_through": 750,
  "temporary_decisions": [
    "Render 선지자 as The Prophet.",
    "Render 레비아탄 as Leviathan and 스사노오 as Susanoo.",
    "Render 마력 as magical power, distinct from mana.",
    "Render 마정 and 마정석 as Magic Gem; render Koizumi's 진상 and 경상 as Jinsang and Gyeongsang.",
    "Render 마계어 as Demon Realm language, 광염 as light-flames, and 진주만의 원혼 as the vengeful spirits of Pearl Harbor."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 이정룡    | **Lee Jungryong** |
| 살기     | **killing intent**                               |                                                       |
| 일격     | **One Strike**                         |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 몬스터     | **monster**           |
| 레이드     | **raid**              |
| 길드      | **Guild**             |
| 팀장      | **Team Leader**       |
| 마정석     | **Magic Gem**         |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 고준 | **Go Jun** | Personal name of Team Leader Seok; Lee Jungryong's prized Disciple. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 레비아탄 | **Leviathan** | Ancient S-rank sea monster associated with Asmodeus. |
| 아레스 | **Ares Guild** | The leading Guild in Korea; formerly employed Team Leader Choi and Song Song. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 준이 | **Jun** | Family nickname used in the form Jun's dad. |
| 석고준 | **Go Jun** | Source full-name form for the established Go Jun, also known as Team Leader Seok. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 존슨 | **Johnson** | Co-host of the American talk show that replays Taekyung's viral interview. |
| 고이즈미 | **Koizumi** | Japanese prime minister quoted in the news. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 이전 | **Two Halls** | Top-level Murim Alliance organizational grouping. |
| 정룡 | **Jungryong** | Cheon Taemin's trusted associate who joined the Peace Guild. |
| 제시 | **Jesse** | The U.S. Secretary of State, introduced by first name. |
| 변이 | **mutation** | The transformation threatening the humans and beasts in the Inner Palace. |
| 마력 | **magical power** | Distinct from mana; the Skeleton King's area of expertise. |
| 일본 | **Japan** | Country requesting emergency assistance and under Leviathan's attack. |
| 마정 | **Magic Gem** | Monster power source; Leviathan seeks an untouched one. |
| 방위대신 | **Defense Minister** | Japanese Defense Minister who controlled the operation's field deployment. |
| 진상 | **Jinsang** | Koizumi's punning address to Jin, retained for the Korean wordplay. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 이정룡 | 진태경 | senior S-rank Hunter to younger Hunter and adversary | Young man | polished, teasing, and veiled-threatening | Uses a genial tone and indirect threats while trying to make Taekyung release the captives. |
| 진태경 | 이정룡 | younger Hunter to senior S-rank Hunter and adversary | you | polite but mocking and defiant | Taekyung answers Lee's soft threats with the wolf-and-tiger metaphor and refuses to yield. |
| 이정룡 | 고준 | Master to Disciple | Go Jun | familiar and testing | Lee switches from Seok's office title to his personal name while considering whether he can defeat Taekyung. |
| 고준 | 이정룡 | Disciple to Master | Master | deferential | Go Jun responds to Lee's personal-name address as 스승님. |
| 진태경 | 석고준 | returning Hunter to hostile Ares security leader | you fucking bastard | hostile and profane | Taekyung directs his final insults and challenge at Go Jun after returning alive. |
| 석고준 | 진태경 | hostile_opponents | brat | hostile and overconfident | Go Jun addresses Taekyung internally as 애송아 while launching his full-strength attack. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 진태경 | 존슨 | Allied Hunter to Grand Mage | Johnson | polite and familiar | Jin repeatedly addresses Magic Johnson directly while requesting explanations and permission to visit the site. |
| 고준 | 진태경 | Ares Guild combatant confronting the killer of his Master | you | hostile and informal | Go Jun uses 너 while demanding Jin confess to Lee Jungryong's death and threatening retaliation. |
| 진태경 | 고준 | dominant adversary confronting Lee Jungryong's Disciple | you | contemptuous and informal | Jin uses 너 and 놈 while overpowering Go Jun and ordering him to end the conflict with Lee Jungryong. |
| 방위대신 | 진태경 | Japanese Defense Minister to foreign Hunter | Jin Taekyung | insulting-shouting | The Minister calls for Jin using a deliberately mangled and contemptuous pronunciation of his name. |
| 진태경 | 방위대신 | foreign Hunter confronting the Japanese Defense Minister | old man | insulting-casual | Jin repeatedly blames the Defense Minister for withholding forces and sarcastically challenges him. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 749
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Go Jun.md

# Go Jun (고준)

- **Safe through:** Chapter 744
- **Aliases:** Team Leader Seok
- **Role:** Go Jun was Ares Guild's Vice Guild Master, Lee Jungryong's Disciple and former Head of Security, the de facto successor to Lee's Ares legacy, and a mutated monster who was killed by Jin Taekyung in Area A.
- **Personality:** Disciplined and controlled under ordinary pressure, fiercely loyal to Lee Jungryong, but consumed by humiliation and rage when Ares Guild's authority is challenged.
- **Voice:** Dry, controlled, and formal with subordinates; deferential when addressing his Master.
- **Relationships:** Go Jun inherited Lee Jungryong's Ares legacy after becoming his Disciple and regarded Jin Taekyung and Choi Minwoo as enemies before his death.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 750
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple, the Fire Gate Clan's nineteenth successor, and the Pavilion Master of the Fire Dragon Pavilion within the Murim Alliance, a Supreme Peak master with the Heavenly Martial Physique and Force, a publicly recognized S-rank-level Hunter who formally retains an A-rank license, a traveler between Murim and another world resembling the realm of immortals, and the creator of the beginner-accessible Smiling Mana Cultivation Method.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate, trusted manager of media and official arrangements, and now the Peace Guild's Guild Master, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 750
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Lee Jungryong.md

# Lee Jungryong (이정룡)

- **Safe through:** Chapter 744
- **Aliases:** None
- **Role:** Former Vice Guild Master of Ares Guild, one of Korea's two S-rank Hunters, and a Supreme Peak-level martial artist who was killed by Jin Taekyung.
- **Personality:** Outwardly genial, calm, and humorous; calculating, opportunistic, manipulative, coercive, and ruthless when challenged
- **Voice:** Smooth, good-natured, and indirect, using teasing conversation and veiled threats before becoming openly furious
- **Relationships:** Master of Park Jihoon and Go Jun (Team Leader Seok), whom he personally selected and trained; longtime Great Cataclysm acquaintance of Park Tae Seop; adversary of Jin Taekyung; knew Team Leader Choi from childhood; has an antagonistic history with Kim Hwajong, who saved his life at the collapse of Mapo Bridge eighteen years earlier; was visibly shaken by learning that Choi is Cheon Taemin's maternal grandson; regarded Cheon Taemin as an older brother despite no blood relation and long held him in respect and fear; secretly supported the orphanage where Lee Dongseok grew up and was regarded by Dongseok as a father; operated as Ares Guild's senior authority beneath its Guild Master; concealed Taemin's condition with Song Cheonwoo and participated in purging aides who knew the truth.

### Leviathan.md

# Leviathan (레비아탄)

- **Safe through:** Chapter 750
- **Aliases:** None
- **Role:** Leviathan is an ancient S-rank sea monster and ruler of the sea that has been severely wounded by Jin Taekyung's One Annihilation, swallowed the Magic Gem it sought, and escaped Jin's follow-up spear attack into the deep sea.
- **Personality:** Ravenous, domineering, and driven by instinctive hunger for magical power and food.
- **Voice:** Its spoken voice is not established; it communicates in Demon Realm language.
- **Relationships:** Leviathan once served the Demon King Asmodeus, its master, and withdrew into the deep sea after Asmodeus fell.

## Korean source

```text
＃751화



정신 나간 제국주의자인 방위대신과 달리, 새롭게 협상 테이블에 앉은 일본 총리는 의외로 말이 통하는 사람이었다.

“지금 당장 방위대신을 끌어내리는 건 불가능하지만, 진 상을 포함한 한국인 여러분들께는 독립 작전권을 드리도록 하겠소.”

“방위성을 통해 각종 물자 및 군사적 지원도 확답해 주십시오. 우리는 협력하고자 귀국의 요청에 응한 것이지, 희생하고자 온 것이 아닙니다.”

정중하지만 단호한 최 팀장의 말에, 일본 총리는 고개를 끄덕였다.

“기꺼이 받아들이겠소. 내 권한 내에서 최대한 힘써 보리다.”

마음 같아서는 방위성의 병신들을 방사능 온천에 담가 버려도 부족하다.

하지만 어쩌겠나, 이미 일은 벌어졌고 할 수 있는 선에서 최선을 다하는 수밖에.

“한데 이미 도망친 괴물을 어떻게 처치할 셈이오?”

“생각해 둔 방법이 있다.”

어디선가 불쑥 튀어나온 대답. 광오한 눈빛으로 일본 총리를 바라보는 스켈레톤 킹을 향해 목을 긋는 시늉을 하자, 움찔한 녀석이 슬쩍 말을 고쳤다.

“방법이 있다요.”

족보에도 없는 존댓말이었지만, 이미 주옥 같은 어록으로 유명한 일본 총리는 그런 걸 신경 쓸 위인이 아니었다.

그는 오히려 호의적인 눈빛으로 스켈레톤 킹을 응시했다.

“오, 스토무-킹. 그대에 대한 소문은 내 익히 들었소.”

“나를. 아니, 저를?”

“물론이오. 이번 일도 그렇지만, 한국에서 몇몇 변이 게이트를 진압할 때부터 알고 있었지.”

자경단 사건이 밝혀지기 전에도 이미 알음알음 대중들 사이에 알려져 있던 스켈레톤 킹이다.

지금까지 알려진 바 없던 최상위 헌터의 등장에 잠시 여론이 집중됐으나 금방 묻혔다.

그만큼 매직 존슨의 신분 세탁이 완벽하기도 했고, 워낙 터무니없는 일이다 보니 몬스터라는 의심은 처음부터 나오지도 않았기 때문이다.

……사실 나 혼자 하도 욕을 처먹어서 그렇다.

“이리 만나게 되어 참으로 반갑구려. 스토무-킹.”

일국의 총리가 자신을 알아본다는 사실에 뿌듯한 표정을 짓고 있던 스켈레톤 킹이 살짝 미간을 좁혔다.

“반갑습니다. 하지만 나는, 아니 제 이름은 스톤 킹이다.”

“그러니 지금 이렇게 부르고 있지 않소. 스토무-킹.”

“스톤 킹이라니까. 자. 천천히 따라해 보시라. 스. 톤. 킹.”

“스. 톤. 킹.”

“이번엔 좀 길게. 스톤. 킹.”

“스톤. 킹.”

“매우 훌륭하구나요! 이제 이어서 해 보십시오.”

“스토무-킹.”

“맙소사. 정말 돌아 버리시겠다. 저는 믿을 수 없다! 당신의 혓바닥은 도대체 어떻게 생겨 먹으신 건가!”

저주받은 열도의 발음 체계와 마계산 왈도체의 환상 콜라보.

참담한 상황을 보다 못해 눈을 질끈 감은 최 팀장을 대신해 내가 교통정리에 나섰다.

“그만합시다. 스톤 킹이건 스토무 킹이건. 스토킹이건 그게 뭔 상관이라고.”

“매우 상관있다! 이 진상 같은 놈아!”

“곧 네 두개골에 금이 가는 것보다?”

“음, 다시 생각해 보니 별 상관은 없을 것 같군.”

“그렇지?”

“물론이다. 그냥 편할 대로 부르면 그게 이름이지.”

“좋은 자세야, 퍽킹. 이제 레비아탄을 추적할 방법을 말해 봐.”

새로 부여받은 이름이 영 마음에 안 드는지, 작게 욕설을 중얼거린 스켈레톤 킹이 입을 열었다.

“우선 전제부터가 틀렸다. 우리는 레비아탄을 추적하는 것이 아니라, 놈을 육지와 최대한 가까운 곳으로 유인해야 한다.”

“유인?”

“그래. 저 바다는 온전히 놈의 영역이다. 괜히 어쭙잖은 방법으로 추적했다간 오히려 영영 놓치게 돼.”

“그 말은…….”

“도망치기에는 너무 극심한 부상이었지. 레비아탄은 아직 멀리 가지 못했을 거다.”

최 팀장이 의문을 제시했다.

“비록 진태경 씨 덕분에 레비아탄이 큰 타격을 입긴 했지만, 정제되지 않은 S급 마정석을 손에 넣은 것으로 압니다. 그 정도면 충분히 상처를 회복하고도 남지 않겠습니까?”

“회복?”

작게 코웃음 친 스켈레톤 킹이 말을 이었다.

“레비아탄이라면 마력의 양이 아무리 많아도 전부 흡수할 수 있겠지. 하지만 마력을 온전히 자신의 것으로 만든다 해도 부상을 완전히 치유하는 건 다른 문제다.”

“음.”

“그 정도의 상처를 회복하기 위해서는 더 많은 마력이 필요하다. 지금쯤 놈도 그 사실을 깨달았을 테고.”

현직 몬스터가 내놓은 의견은 제법 설득력이 있었다.

더군다나 일섬은 시전자의 몸마저 망가트릴 정도의 위력을 지닌 필살(必殺)의 일격.

레비아탄이라는 이름답게 마지막 순간 몸을 틀었지만, 그렇다고 단기간에 나을 수 있는 상처는 아니다.

‘유인. 유인이라.’

그 단어를 곱씹던 내가 문득 입을 열었다.

“빠르게 형세를 판단하고 원하는 것만 얻어 도망칠 만큼 영악한 놈이, 과연 함정에 걸려들까?”

그리고 돌아온 대답은 간단했다.

“걸려들 거다. 조건만 맞는다면.”

“알면서도 들어올 수밖에 없는 함정을 파라?”

“레비아탄을 굶주리고 상처 입은 짐승이라고 생각해야 한다. 놈이 이곳까지 찾아온 이유도 그와 같지.”

최 팀장이 신음처럼 중얼거렸다.

“엄청난 미끼를 준비해야겠군요.”

“그래, 레비아탄이 위험을 무릅쓰고 달려들 정도로 먹음직스러운 미끼가 필요하다.”

그리고 지금 이 시점에서, 레비아탄을 끌어들일 만한 미끼는 하나밖에 없었다.

“저기, 총리님?”

내 은근한 목소리에, 흐리멍덩한 눈으로 우리의 대화를 지켜보고 있던 고이즈미 총리가 대답했다.

“아, 말씀하시오.”

“다름이 아니라, 혹시 일본에 그거 몇 개 있어요?”

“그거라니, 뭘 말하는 거요?”

“모른 척하시긴. S급 마정석이요.”

“……에?”

“잠깐 좀 빌립시다.”

“……에에?”

“어허. 뭘 그렇게 놀라시고 그래. 레비아탄 잡고 돌려드릴게요. 자, 약속.”

나는 눈을 동그랗게 뜬 총리에게 새끼손가락을 들이밀었다.

아, 따서 갚으면 되잖아. 따서.



* * *



현대에서 S급 마정석은 엄청난 값어치를 지닌 보물이다.

대도시 하나를 굴릴 수 있는 최고의 에너지원이기 이전에 전 세계를 통틀어 백여 개 정도밖에 없는 엄청난 희귀성.

그래서인지 적극 협조를 약속한 일본 총리도 처음에는 기겁했다. 물론 마지막에는 울며 겨자 먹기로 내놓을 수밖에 없었지만.

“가져 왔소.”

딸칵.

보안 마법의 해제와 함께 부드러운 벨벳으로 만든 상자가 열린다. 그 안에 자리잡고 있는 것은 형형한 빛을 흩뿌리는 두 개의 마정석이었다.

“흠, 겨우 두 개?”

내 눈빛을 본 일본 총리가 황급히 대답했다.

“우리 일본 정부가 소유한 S급 마정석은 이게 전부요.”

“정말입니까?”

“한 치의 거짓도 없는 사실이오! 내가 내각 의원들과 천황 폐하를 설득하느라 얼마나 애를 먹었는데!”

“만약에 뒤져서 나오면 S급 마정석 하나당…….”

“……진태경 씨?”

“아, 죄송합니다. 이게 하도 습관이 되어 가지고.”

이래서 습관이 무섭다니까.

최 팀장의 만류에 뒤통수를 긁적이는 내 모습에, 아까부터 슬슬 뒷걸음질 치던 일본 총리가 잽싸게 방을 빠져나갔다. 꼭 무사히 돌려줘야 한다는 신신당부와 함께.

하지만 우리만 남은 방 안의 공기는 영 미적지근했다.

“음. 두 개라…….”

“이걸로는 좀 부족한데.”

“이 몸의 생각도 같다. 아직도 상당한 마력을 품고 있지만, 레비아탄을 유인할 만큼은 아니야.”

S급 마정석이 몇 개가 있느냐는 상관없다. 중요한 것은 마정석에 남아 있는 마력의 양과 질이었다.

‘원래대로면 정제되어 있는 게 당연하긴 한데…… 이번에는 용도가 다르니까.’

눈앞에 S급 마정석이 두 개나 있지만, 우리가 원하는 것은 미끼다. 레비아탄이 함정임을 알면서도 달려들 수밖에 없는 먹음직스러운 미끼.

놈이 가져간 것과 같은, 거대하고도 순수한 마력의 덩어리.

‘이 두 개를 함께 미끼로 사용해 봤자, 어차피 정제되지 않은 것에 비하면 한참 못 미친다.’

그리고 이건 비단 나 혼자만이 떠올린 생각이 아니었다.

우리가 엇비슷한 눈빛으로 서로를 바라보던 그때, 스켈레톤 킹이 불쑥 입을 열었다.

“이 몸이 아무리 생각해도 이것들로는 무리다. 차라리 더 가져오는 게 어떤가?”

“더 가져오자는 게 무슨…… 아.”

잠시 잊고 있던 사실이 머릿속을 스친다.

아레스 길드 본사에 숨겨져 있던 A구역. 베일에 싸여 있던 그곳에는 천문학적인 현찰과 예술품, 그리고 마정석들로 가득했고 그중에는 무려 다섯 개의 S급 마정석이 있었다.

“하지만 그것도 이미 정제된 거잖아.”

“그건…… 그렇지.”

입맛을 다신 스켈레톤 킹이 아쉬운 목소리로 덧붙였다.

“그래도 없는 것보단 나을 것 같은데. 어떻게 안 될까?”

당연히 없는 것보단 있는 게 낫다.

하지만 다섯 개가 더해진다고 한들 크게 달라질 것도 없는 것이 현재의 상황이었다.

본래 마정석이란 물건은 더 완벽히 정제되어 있을수록 값어치가 높고, 이정룡과 석고준이 A구역에 꿍쳐두었던 S급 마정석은 말 그대로 최고급이었으니까.

그리고 한 가지 더. 최종 결정권은 소유주에게 있다.

“애초에 불법적인 경로를 통해 입수했을 물건입니다. 세상에 알려지면 언론만 신이 나겠죠.”

그래, 특히 요즘 같은 상황에서는 아주 개지랄이 나겠지. 조금만 틈이 나면 카메라 들고 달려들 하이에나들이 지천에 깔렸다.

최 팀장의 단언에 잠시 생각하던 스켈레톤 킹이 다른 의견을 내놓았다.

“아예 정제되지 않은 마정석들을 끌어모으는 건? 당장 인근 게이트에서 나오는 것들을 모조리 끌어모아서 이곳으로 조달하면…….”

나는 활짝 웃으며 녀석의 어깨를 두드려주었다.

“축하드립니다. 국제법 위반으로 종신형이 선고되었습니다.”

“이런 염병할!”

“싱글벙글 21세기에 온 것을 환영한다. 여기 의외로 존나 살기 힘들어.”

으득.

이를 악문 스켈레톤 킹이 말을 이었다.

“이렇게 된 이상 어쩔 수 없다. 저 마정석들을 미끼로 쓰거나, 아니면 최정예만 선별한 레이드 팀으로 직접 놈을 추적하여 죽이는 수밖에.”

“이야, 세상 참 좋아졌다. 몬스터가 몬스터를 레이드 하자고 주장하는 날이 올 줄이야.”

“방법이 없지 않나!”

방법이라, 글쎄.

나는 최 팀장과 은밀히 시선을 교환했다.

그리고 성을 내는 스켈레톤 킹의 눈치를 살피며 천천히 말문을 뗐다.

“없다고는 안 했는데.”

“뭐?”

“방법이 하나 있긴 해.”

스켈레톤 킹이 반색하며 물었다.

“그게 어떤 방법이지?”

“말하기에 앞서 하나만 알려 줄게. 만약 레이드 팀이 조직되면…… 넌 빠진다.”

“나를 뺀다니. 그게 무슨 소리냐?”

어지간히 의외였는지, 눈을 동그랗게 뜬 녀석을 보며 말을 이었다.

“어쩔 수 없어. 지금으로서는 보는 눈이 많으니까.”

그 말에 담긴 의미를 이해하지 못할 만큼 멍청한 녀석이 아니다. 스켈레톤 킹이 굳은 얼굴로 되물었다.

“만약 이 몸의 힘이 드러날 수도 있으니, 레비아탄과의 전투에서 빼놓겠다?”

“잘 아네.”

“이런 미친. 그걸 지금 말이라고 하는 건가!”

쾅! 우직!

고함과 함께 내리친 주먹이 테이블을 산산조각 낸다. 어느새 코앞까지 다가온 한 쌍의 눈동자에서 실망과 분노가 읽혔다.

“간악한 인간이여. 내가 널 잘못 본 모양이다. 어떻게 이런 상황에서 그런 말을 할 수 있단 말인가!”

“상관없잖아. 넌 몬스터니까.”

“……뭐?”

“레비아탄을 잡아도, 네 정체가 밝혀지면 끝장이야. 그걸 피하려는 것뿐이고.”

우드득.

스켈레톤 킹의 주먹에서 뼈가 어긋나는 소리가 울려 퍼졌다. 믿을 수 없다는 눈빛으로 나를 바라보던 녀석이 피를 토하듯 외쳤다.

“상관없다! 저들을 구할 수 있다면 난 무엇이든 할 수 있다! 이런 재앙을 일으킨 레비아탄을……!”

“무엇이든?”

“어?”

됐다. 걸렸다.

난 흐뭇하게 웃으며 스켈레톤 킹을 바라보았다.

“무엇이든 한다고 했다. 맞지?”
```

## Final English reading copy

```markdown
# Chapter 751

Unlike the Defense Minister, a lunatic imperialist, Japan’s newly seated prime minister was surprisingly reasonable.

“It is impossible to remove the Defense Minister right this moment, but I will grant the Korean people—including Jinsang—independent operational authority.”

“Please also guarantee various supplies and military support through the Defense Ministry. We accepted your country’s request because we wanted to cooperate, not because we wanted to be sacrificed.”

In response to Team Leader Choi’s polite but firm words, the Japanese prime minister nodded.

“I will gladly agree. I shall do everything within the limits of my authority.”

Given how I felt, even throwing the idiots in the Defense Ministry into a radioactive hot spring wouldn’t have been enough.

But what could we do? The damage had already been done. All we could do was our best with what we had.

“But how do you intend to deal with the monster that has already escaped?”

“I have a method.”

The answer suddenly came from somewhere.

When I made a throat-cutting gesture toward the Skeleton King, who was glaring arrogantly at the Japanese prime minister, he flinched and hastily corrected himself.

“I have a method, yo.”

It was a form of honorific speech that had no place in any family tree, but the Japanese prime minister—already famous for his priceless quotes—was not the sort of man to care about details like that.

Instead, he gazed at the Skeleton King with a friendly expression.

“Oh, Stomu-King. I have heard quite a bit about you.”

“Me? I mean… me, sir?”

“Of course. I knew of you not only because of this incident, but also from when you suppressed several mutation Gates in Korea.”

The Skeleton King had already become known among the public here and there, even before the vigilante incident came to light.

For a brief while, public attention focused on the appearance of a top-tier Hunter whose existence had never been revealed. But that attention quickly faded.

Magic Johnson’s identity laundering had been that perfect, and since the whole thing was so absurd, nobody had suspected from the beginning that he was a monster.

*…Actually, it’s because I was the one getting cursed at so much.*

“It is a pleasure to meet you at last, Stomu-King.”

The Skeleton King had been looking proud that the prime minister of an entire country knew who he was. Now, he slightly narrowed his brow.

“It is a pleasure to meet you as well. But I am—no, my name is Stone King.”

“That is why I am calling you that now. Stomu-King.”

“I said Stone King. Here. Repeat after me slowly. S. Tone. King.”

“S. Tone. King.”

“This time, join the first two. Stone. King.”

“Stone. King.”

“Very excellent! Now put it all together.”

“Stomu-King.”

“Good heavens. I really am going to lose my mind. I can’t believe this! What on earth is your tongue made of?”

A cursed archipelago’s pronunciation system in a bizarre collaboration with Demon Realm-style mangled speech.

Unable to watch the tragedy any longer, I stepped in to mediate on Team Leader Choi’s behalf, since he had squeezed his eyes shut.

“Let’s stop. Stone King, Stomu King, stalking—what difference does it make?”

“It makes a tremendous difference! You Jinsang bastard!”

“More than the crack that’s about to appear in your skull?”

“Hmm. Now that I think about it, perhaps it doesn’t matter that much.”

“See?”

“Of course. Just call me whatever is convenient. That becomes my name.”

“Good attitude, Fucking. Now tell us how to track Leviathan.”

Perhaps he disliked his newly bestowed name, because the Skeleton King muttered a quiet curse before opening his mouth.

“First of all, your premise is wrong. We should not be tracking Leviathan. We need to lure the bastard as close to land as possible.”

“Lure it?”

“Yes. That sea is entirely its territory. If we try to track it with some half-baked method, we may lose it forever instead.”

“That means…”

“It was too severely injured to flee very far. Leviathan will not have gone far yet.”

Team Leader Choi raised a question.

“Although Leviathan suffered a heavy blow thanks to Mr. Jin Taekyung, I understand that it obtained an unrefined S-rank Magic Gem. Wouldn’t that be enough for it to recover from its wounds and then some?”

“Recover?”

The Skeleton King gave a small snort and continued.

“If it is Leviathan, it can absorb all the magical power no matter how much there is. But even if it makes that magical power entirely its own, completely healing its injuries is a separate matter.”

“Hmm.”

“It needs far more magical power to recover from wounds of that magnitude. By now, the bastard must have realized that as well.”

The opinion of an actual monster was fairly persuasive.

On top of that, One Annihilation was a killing blow powerful enough to wreck even its caster’s body.

True to its name, Leviathan had twisted its body at the last moment, but those were not wounds that could heal in a short time.

*Lure it. Lure it, huh.*

As I turned the word over in my mind, I suddenly spoke.

“Do you really think a monster cunning enough to assess the situation quickly, take only what it wants, and run away would fall for a trap?”

The answer that came back was simple.

“It will. If the conditions are right.”

“A trap it can’t help but enter, even though it knows it’s a trap?”

“We must think of Leviathan as a hungry, wounded beast. That is also why it came all the way here.”

Team Leader Choi muttered like he was groaning.

“We’ll need to prepare an enormous bait.”

“Yes. We need bait so delicious that Leviathan will risk its life to charge at it.”

And at this point, there was only one thing that could lure Leviathan in.

“Excuse me, Prime Minister?”

At my deliberately mild voice, Prime Minister Koizumi—who had been watching our conversation with dazed eyes—answered.

“Ah, yes. Go ahead.”

“I was wondering… does Japan happen to have a few of those?”

“Those? What are you talking about?”

“Don’t play dumb. S-rank Magic Gems.”

“…What?”

“Let us borrow them for a bit.”

“…What?”

“Now, now. Why are you so surprised? We’ll catch Leviathan and return them. There, it’s a promise.”

I held out my little finger toward the prime minister, whose eyes had gone perfectly round.

*We’ll win one and pay it back. Win it.*

* * *

In the modern world, S-rank Magic Gems were treasures of tremendous value.

Before even considering that they were the finest energy source capable of powering an entire metropolis, there were only around a hundred of them in the entire world. Their rarity alone was astonishing.

Perhaps that was why the Japanese prime minister, despite promising his full cooperation, had initially been horrified. Of course, in the end, he had no choice but to hand them over, even if it was against his will.

“Here they are.”

*Click.*

As the security Magic was deactivated, a box made of soft velvet opened. Inside sat two Magic Gems scattering a brilliant light.

“Hm. Only two?”

The Japanese prime minister hurriedly answered after seeing my expression.

“These are all the S-rank Magic Gems owned by the Japanese government.”

“Really?”

“It is the absolute truth! Do you know how much trouble I went through persuading the cabinet members and His Imperial Majesty?”

“If I dig around and find more, then for every S-rank Magic Gem…”

“…Mr. Jin Taekyung?”

“Oh, sorry. I’ve gotten so used to doing this.”

*This is why habits are scary.*

At Team Leader Choi’s intervention, I scratched the back of my head. The Japanese prime minister, who had been edging backward for a while now, hurriedly slipped out of the room, repeatedly begging us to return the Magic Gems safely.

But once he was gone, the mood in the room was rather lukewarm.

“Hmm. Two…”

“That’s not enough.”

“This body agrees. They still contain a considerable amount of magical power, but not enough to lure Leviathan.”

The number of Magic Gems did not matter. What mattered was the quantity and quality of the magical power remaining inside them.

*Normally, they should obviously have been refined… but this time, we have a different use for them.*

There were two S-rank Magic Gems right in front of us, but what we wanted was bait.

Bait so delicious that Leviathan would have no choice but to charge at it even while knowing it was a trap.

A massive mass of pure magical power, like the one it had taken.

*Even if we use both of these together as bait, they still won’t come close to an unrefined Magic Gem.*

And I was not the only one who had reached that conclusion.

Just as we looked at one another with similar expressions, the Skeleton King suddenly spoke.

“No matter how I think about it, these will not be enough. What about bringing more?”

“What do you mean, bring more… Oh.”

A fact I had briefly forgotten flashed through my mind.

Area A, hidden within the Ares Guild headquarters.

That mysterious place had been filled with astronomical amounts of cash, works of art, and Magic Gems. Among them had been no fewer than five S-rank Magic Gems.

“But those have already been refined.”

“That… is true.”

The Skeleton King smacked his lips and added regretfully,

“Still, they should be better than nothing. Can’t we make it work somehow?”

Of course, having something was better than having nothing.

But even adding five more would not make much difference under the current circumstances.

The more perfectly refined a Magic Gem was, the greater its value. The S-rank Magic Gems that Lee Jungryong and Go Jun had stashed away in Area A were literally top of the line.

And there was one more thing.

The final decision belonged to the owner.

“They must have been obtained through illegal channels in the first place. If the truth gets out, the media will have a field day.”

*Yeah. Especially in a situation like this, it would turn into a complete fucking shitshow. Hyenas with cameras were everywhere, waiting to pounce at the slightest opening.*

After Team Leader Choi’s firm statement, the Skeleton King thought for a moment before offering another idea.

“What if we gather completely unrefined Magic Gems? We could collect every one that emerges from the nearby Gates and bring them all here…”

I smiled broadly and patted him on the shoulder.

“Congratulations. You have been sentenced to life in prison for violating international law.”

“What the goddamn hell!”

“Welcome to the bright and cheerful twenty-first century. It’s surprisingly fucking hard to live here.”

*Crack.*

The Skeleton King clenched his teeth and continued.

“Since it has come to this, we have no choice. We either use those Magic Gems as bait, or we select only the very best and track down and kill the bastard ourselves with a raid team.”

“Wow. The world has really improved. I never thought I’d live to see the day a monster suggested raiding another monster.”

“There is no other way!”

*No other way, huh?*

I exchanged a covert glance with Team Leader Choi.

Then, carefully gauging the angry Skeleton King’s reaction, I slowly began.

“I never said there wasn’t.”

“What?”

“There is one method.”

The Skeleton King brightened and asked,

“What method is that?”

“Before I tell you, there’s one thing you should know. If a raid team is organized… you’re sitting this one out.”

“You’re leaving me out? What do you mean?”

It must have been more unexpected than he could have imagined. I continued as he stared at me with perfectly round eyes.

“We have no choice. There are too many eyes on us right now.”

He was not stupid enough to miss the meaning behind my words. The Skeleton King asked with a stiff expression,

“You mean that because my power might be exposed, you intend to leave me out of the battle with Leviathan?”

“You know it.”

“This is insane! Is that really something you can say right now?”

*Bang! Crunch!*

The fist he brought down with a shout shattered the table. The pair of eyes that had come right up in front of me held clear disappointment and fury.

“Wicked human. I must have judged you wrongly. How can you say such a thing in a situation like this?”

“It doesn’t matter. You’re a monster.”

“…What?”

“Even if we catch Leviathan, once your identity is revealed, you’re finished. I’m only trying to avoid that.”

*Wood crackle.*

The bones in the Skeleton King’s fist shifted with a grinding sound. He stared at me with an expression of disbelief before crying out as though spitting blood.

“It doesn’t matter! If I can save them, I can do anything! Leviathan, the one that caused this disaster—”

“Anything?”

“Huh?”

*Got you. Hooked.*

I looked at the Skeleton King with a satisfied smile.

“You said you would do anything. Right?”
```

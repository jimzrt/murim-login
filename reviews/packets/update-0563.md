<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0563.txt",
      "sha256": "e896a987934d035819f40050f8083d5ae793bbcc97ee11622de27e71745409c8",
      "bytes": 14477
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "565b73a26d4144f08c11394c7bdb7174e2784ae5cee21df55963412d1034ed23",
      "bytes": 4952
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "9f0967adbd903101550da9f904973c292342e891dbb8ce0c6c845586ca21c8dd",
      "bytes": 178462
    },
    {
      "path": "characters/Baek Hanseong.md",
      "sha256": "40d5b7a19177a1dcad59cd08d475a3e7604e31ba79a8ea74826d1f81396ead84",
      "bytes": 753
    },
    {
      "path": "characters/Cheon Taemin.md",
      "sha256": "151a389cddb6e83c500c0c535a8b3b7326f4693b125be38ad690fc93d9417c01",
      "bytes": 590
    },
    {
      "path": "characters/Go Jun.md",
      "sha256": "6193a286b3070d100f29a46c870058e7a1344ffb0b20905e97514d533d1de176",
      "bytes": 793
    },
    {
      "path": "characters/Go Se-won.md",
      "sha256": "3af99ac0d5424c7b5f7d1b3a3942428137063395075fd46deb994d71b5861c2a",
      "bytes": 635
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "fb2aa3e2288221e46588de4627d04889519e7e5282f2a51e687ad78086ebcdd3",
      "bytes": 2280
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "0b7d7072402da073b19036a520f456b278ece1d54bb45a89340636bcf88fa555",
      "bytes": 622
    },
    {
      "path": "characters/Lee Jungryong.md",
      "sha256": "5d5bb81a06c2e8a13bd60e7d5a86297d45f91d3f279739215a8e0fa7dc4724b7",
      "bytes": 1182
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "fd8b7cffbcc9fc25c2ef0d19a749752ebb1c1be4dbefde01d854fd7bf9560dd8",
      "bytes": 172431
    }
  ],
  "estimated_tokens": 12625
}
-->

# Durable State Update — Chapter 563

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 563. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 563. Profile updates may replace only one
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
  "chapter": 563,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 563,
    "continuity_sources": [563],
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
    "Magic Johnson's information records at least thirty-two Mutated Gates in the United States during one week, and the true number is likely higher.",
    "The Peace Guild has risen as the only apparent counterweight to Ares Guild; Team Leader Choi is gathering political, business, and Guild allies to strengthen Peace and weaken Ares, with Magic Johnson and the Wizard Guild supporting him.",
    "Team Leader Choi has confirmed that his blood descends from Cheon Taemin, whose legacy gives him exceptional political and social leverage.",
    "The Fire Dragon Pavilion's six-member first mission is entering Nanman through the Journey to Nanman Quest, whose reward is a linked quest and whose failure penalty is the Title Can't Go to Nanman; the party secretly departed Henan.",
    "Taekyung is a Supreme Peak master with Three Flowers Gather at the Crown, advanced Qi Sense, exceptional resistance to monster Fear, public S-rank-level recognition while retaining an A-rank license, leadership of the Fire Dragon Pavilion's first mission to Nanman, and the Peace Guild's modern-world patronage.",
    "Mungyeong ended Taekyung's direct training and assigned him the final task of incorporating martial principles into his learned martial arts; Cheongpung accompanies Mungyeong and learns through observation.",
    "Mungyeong considers Nanman a plausible site for Dark Heaven's second rift, while Dark Heaven remains a monster-like threat capable of causing rifts and creating mutants; the mechanism behind Jang Sam's transformation remains unresolved.",
    "The Mount Song Resolution restored the Murim Alliance with Mae Jonghak as Alliance Leader and Jeok Cheongang heading the Five Kings Hall; Zhuge Feng's Demon-Sealing Formation still blocks mana from the exposed Gate while Jang Taebo processes the Water God Dragon's remains.",
    "The Southern Heaven Demon Empress is believed to be moving toward the suspected next target, while Song Ho's dispatch there has received no reply for more than seven days.",
    "Im Kkeokjeong's arms have been reattached, his rehabilitation is nearly complete, and he intends to remain a Hunter and Peace Guild member while spending time with his wife and children.",
    "Taekyung is in the modern world in early 2047, has entered the Yeokgok Mutated Gate, and has just killed its Orc Lord to rescue an Ares raid team.",
    "The public believes the Lich killed Lee Jungryong and Wu Heixing; Taekyung knows the actual deaths were caused by him, while Go Jun remains Ares Guild's Vice Guild Master and regards Taekyung and Choi Minwoo as enemies seeking to take Ares away. Go Se-won serves as Ares's Head of Security under Go Jun."
  ],
  "continuity_sources": [
    562,
    561
  ],
  "open_questions": [
    "What is the Lord of Heaven's identity, how is he connected to the dangerous force Taekyung associates with his original world, and how can Dark Heaven open Gates?",
    "What will Taekyung's party find in Nanman, and what does the Southern Heaven Demon Empress intend there?",
    "What is the outcome of the duel between Jeok Cheongang and Nangong Cheon, and why did Ju Hwaran and Sama Pyo's political engagement end?",
    "What process created Jang Sam's mutant form, whether Dark Heaven's mutants can absorb human energy, and whether it relates to the Mutated Gate?",
    "How many additional Gate disasters are being concealed, and what is driving the accelerating Mutated Gate and Monster Wave outbreaks in Korea and abroad?"
  ],
  "safe_through": 562,
  "temporary_decisions": [
    "Render 건량 as dry rations, 광서 as Guangxi, 대별산 as Mount Daebyeol, 만리행 as Ten-Thousand-Li Journey, and 고잉메리호 as Going Merry.",
    "Render 반 시진 as half a shichen and retain Nanman, Nanman Beast Palace, Fire Dragon Pavilion, Great Hero, and Young Lady Ju.",
    "Render 남만행 as Journey to Nanman, 남만을 못 가 as Can't Go to Nanman, 면구 as disguise mask, 역용술 as disguise technique, 각주님 as Pavilion Master, 로그아웃 as Logout, and 동기화 as Synchronization.",
    "Render 일기당천 as One Against a Thousand, 거인의 포효 as Giant's Roar, 타락한 엔트 as Corrupted Ent, 붉은 눈 as Red Eye, 치코리타 as Chikorita, 대마도사 as Grand Mage, 순간이동 as Teleportation, 텔레포트 as Teleport, 변이 게이트 as Mutated Gate, and 몬스터 웨이브 as Monster Wave.",
    "Render 모하비 사막 as Mojave Desert, 애리조나주 as Arizona, 대의 as greater cause, 순수혈통 as pureblood, 국부 as Founding Father, 위저드(Wizard) 길드 as Wizard Guild, 조셉 바이든 as Joseph Biden, 펠릭스 왕자 as Prince Felix, 곽한구 as Gwak Hangu, 역곡 as Yeokgok, 오크의 황무지 as Orc Wasteland, 오크 로드 as Orc Lord, 국회의사당 as National Assembly, 고세원 as Go Se-won, 경호팀장 as Head of Security, and A구역 as Section A."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 천태민    | **Cheon Taemin**  |
| 이정룡    | **Lee Jungryong** |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 일격     | **One Strike**                         |
| 상태               | **Status**                     |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 길드      | **Guild**             |
| 길드장     | **Guild Master**      |
| 부길드장    | **Vice Guild Master** |
| 팀장      | **Team Leader**       |
| 마법사     | **mage**              |
| 백한성 | **Baek Hanseong** | Twenty-seventh President of Korea and youngest president elected in Korean history. |
| 고준 | **Go Jun** | Personal name of Team Leader Seok; Lee Jungryong's prized Disciple. |
| 고세원 | **Go Se-won** | Ares Guild Head of Security and Team Leader. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 대한민국 | **Korea** | Country reference. |
| 아레스 | **Ares Guild** | The leading Guild in Korea; formerly employed Team Leader Choi and Song Song. |
| 사장님 | **Boss** | Address for the restaurant owner; contextually rendered as ma'am in one reply |
| 송이 | **Song-i** | Short form used for Song Song; Taekyung's love interest. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 청와대 | **Blue House** | Presidential office mentioned in an online comment about proposed legislation. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 신성 | **Morning Star** | Term in the summons referring to the Master of Morning Star. |
| 준이 | **Jun** | Family nickname used in the form Jun's dad. |
| 석고준 | **Go Jun** | Source full-name form for the established Go Jun, also known as Team Leader Seok. |
| 경호팀장 | **Head of Security** | Go Jun's security-team office under Lee Jungryong. |
| 대통령 | **President** | Title for Korea's head of state. |
| 시리 | **City** | Second word in one of the necromantic chants. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 황하 | **Yellow River** | River along which civilization began. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 사장님 | visitor_to_restaurant_owner | Boss | polite but sarcastic | Maintains a superficially respectful address while baiting the owner during the confrontation. |
| 사장님 | 진태경 | restaurant_owner_to_employee_son | you / you little punk | condescending-aggressive | Uses hostile informal forms while trying to intimidate Taekyung. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 이정룡 | 진태경 | senior S-rank Hunter to younger Hunter and adversary | Young man | polished, teasing, and veiled-threatening | Uses a genial tone and indirect threats while trying to make Taekyung release the captives. |
| 진태경 | 이정룡 | younger Hunter to senior S-rank Hunter and adversary | you | polite but mocking and defiant | Taekyung answers Lee's soft threats with the wolf-and-tiger metaphor and refuses to yield. |
| 이정룡 | 고준 | Master to Disciple | Go Jun | familiar and testing | Lee switches from Seok's office title to his personal name while considering whether he can defeat Taekyung. |
| 고준 | 이정룡 | Disciple to Master | Master | deferential | Go Jun responds to Lee's personal-name address as 스승님. |
| 마법사 | 이정룡 | Ares Guild mage subordinate to Vice Guild Master | Vice Guild Master | formal-deferential | Lee's five direct A-rank mages greet him and receive instructions for concealing the battle. |
| 이정룡 | 천태민 | younger_to_older_brother_by_choice | older brother | reverent and familiar; internal | Lee Jungryong uses 형님 in unspoken thoughts and regards Cheon Taemin as an older brother despite having no blood relation. |
| 진태경 | 석고준 | returning Hunter to hostile Ares security leader | you fucking bastard | hostile and profane | Taekyung directs his final insults and challenge at Go Jun after returning alive. |
| 석고준 | 진태경 | hostile_opponents | brat | hostile and overconfident | Go Jun addresses Taekyung internally as 애송아 while launching his full-strength attack. |
| 이정룡 | 백한성 | Ares authority to national head of state | Mr. President | formal-polite | Uses 대통령 각하 while greeting Baek Hanseong. |
| 백한성 | 이정룡 | President to Ares Guild Vice Guild Master | Vice Guild Master Lee | formal-polite | Uses 이정룡 부길드장님 while discussing the Chinese proposal. |
| 중년인 | 진태경 | veteran civilian Hunter to celebrated allied Hunter | Mr. Jin | formal-polite and awed | The casualty clerk addresses Jin as 진 선생님 after Jin asks him to list Lei Fei among the dead. |
| 진태경 | 중년인 | celebrated Hunter to older fellow Hunter | sir | casual and teasing | Jin addresses the older Hunter as 아저씨 while joking with him and giving him instructions. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 고준 | 진태경 | Ares Guild combatant confronting the killer of his Master | you | hostile and informal | Go Jun uses 너 while demanding Jin confess to Lee Jungryong's death and threatening retaliation. |
| 진태경 | 고준 | dominant adversary confronting Lee Jungryong's Disciple | you | contemptuous and informal | Jin uses 너 and 놈 while overpowering Go Jun and ordering him to end the conflict with Lee Jungryong. |
| 진태경 | 대통령 | Hunter_to_President | Mr. President | formal-polite | Taekyung addresses the President respectfully during their airport greeting. |
| 대통령 | 진태경 | President_to_Hunter | Mr. Jin Taekyung | formal-polite | The President addresses Taekyung by name at the airport photo line. |
| 석고준 | 고세원 | Ares Vice Guild Master to Head of Security | you | curt and informal | Go Jun tells Go Se-won that he is later than usual when Se-won enters the wrecked office. |

## Listed compact profiles

### Baek Hanseong.md

# Baek Hanseong (백한성)

- **Safe through:** Chapter 305
- **Aliases:** None
- **Role:** Twenty-seventh President of Korea and the youngest president elected in Korean history; delivers China's unofficial diplomatic request and facilitates Korean Guild participation in the Sichuan Catastrophe response.
- **Personality:** Confident, politically shrewd, composed, and willing to needle Lee Jungryong while advancing his anti-Ares stance.
- **Voice:** Polite, self-assured, calm, and lightly teasing.
- **Relationships:** Political counterpart to Lee Jungryong; cooperates with Ares Guild over the Chinese crisis while allowing the Peace Guild to participate at Xiao Yang's request.

### Cheon Taemin.md

# Cheon Taemin (천태민)

- **Safe through:** Chapter 560
- **Aliases:** Slayer
- **Role:** Ares Guild Master; humanity's great hero and the world's greatest Hunter; killed the Demon King and is known as the Slayer; created the first Mana Cultivation Method during the Great Cataclysm.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** Maternal grandfather of Team Leader Choi and father of Soyeong; regarded by Lee Jungryong as an older brother despite their lack of blood relation.

### Go Jun.md

# Go Jun (고준)

- **Safe through:** Chapter 562
- **Aliases:** Team Leader Seok
- **Role:** Go Jun is Ares Guild's new Vice Guild Master, Lee Jungryong's disciple and former security-team leader, and the chief mourner at Lee's national funeral.
- **Personality:** Highly disciplined, fiercely loyal to Lee Jungryong, confident in his abilities, and capable of suppressing his anger and killing intent under provocation.
- **Voice:** Dry, controlled, and formal with subordinates; deferential when addressing his Master.
- **Relationships:** Disciple and direct protégé of Lee Jungryong, Go Jun inherited Lee's Ares Guild legacy after his death and regards Jin Taekyung and Choi Minwoo as enemies seeking to take it away.

### Go Se-won.md

# Go Se-won (고세원)

- **Safe through:** Chapter 562
- **Aliases:** Head of Security
- **Role:** Go Se-won is Ares Guild's Head of Security and a Team Leader with privileged access to restricted Section A.
- **Personality:** Composed and confident in public, he is mildly uncomfortable with Ares Guild's increasingly severe discipline but obeys its policy.
- **Voice:** Calm and deferential toward superiors, but blunt and decisive when issuing orders.
- **Relationships:** Go Se-won reports to Vice Guild Master Go Jun and commands Ares Guild security personnel.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 562
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, a Supreme Peak master who possesses the Heavenly Martial Physique and superhuman physical strength, has manifested Force, opened his Middle Dantian, crossed the wall into true mastery, has achieved Three Flowers Gather at the Crown but not Five Qi Returning to Origin, can perceive the texture of qi well enough to sever layered magic, can resist high-level monster Fear through exceptional mental strength, is publicly recognized as an S-rank-level Hunter while formally retaining an A-rank license pending testing, can command coordinated raids against powerful monsters, serves as one of the two pavilion masters of the Alliance Leader's direct Fire Dragon Pavilion, leads its first mission to Nanman, and is the Peace Guild's wealthy patron in the modern world.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor and assigned him a final task to incorporate martial principles into his learned martial arts but declined Taekyung's recruitment after Cheongpung reached him first, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate, student, and trusted manager of media and official arrangements, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, and Xiao Shen regards him as an older brother after Jin saved him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 562
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Lee Jungryong.md

# Lee Jungryong (이정룡)

- **Safe through:** Chapter 561
- **Aliases:** None
- **Role:** Former Vice Guild Master of Ares Guild, one of Korea's two S-rank Hunters, and a Supreme Peak-level martial artist who was killed by Jin Taekyung.
- **Personality:** Outwardly genial, calm, and humorous; calculating, opportunistic, manipulative, coercive, and ruthless when challenged
- **Voice:** Smooth, good-natured, and indirect, using teasing conversation and veiled threats before becoming openly furious
- **Relationships:** Master of Park Jihoon and Go Jun (Team Leader Seok), whom he personally selected and trained; longtime Great Cataclysm acquaintance of Park Tae Seop; adversary of Jin Taekyung; knew Team Leader Choi from childhood; has an antagonistic history with Kim Hwajong, who saved his life at the collapse of Mapo Bridge eighteen years earlier; was visibly shaken by learning that Choi is Cheon Taemin's maternal grandson; regards Cheon Taemin as an older brother despite no blood relation and has long held him in respect and fear; operates as Ares Guild's senior authority beneath its Guild Master

## Korean source

```text
＃563화



“평소보다 늦었군.”

석고준의 말은 틀렸다. 고세원의 시계는 언제나 정확했고 정해진 출근 시간까지는 아직 상당한 시간이 남아 있었다.

그러니 평소와 달랐던 것은 고세원이 아니라, 오늘따라 유난히도 불편한 그의 심기였을 뿐이었다.

하지만 고세원은 묵묵히 고개를 숙이는 것으로 말을 아꼈다.

“죄송합니다.”

“됐다, 앉아.”

그와 같은 소파에 앉는다는 건 최측근만이 누릴 수 있는 특혜 중 하나다.

하지만 고세원은 이태리제 가죽 소파에 앉기도 전에, 상관의 분노가 아직 끝나지 않았음을 깨달았다.

「러프 뉴스 고현우 기자입니다.」

홀로그램 TV 속, 발언권을 얻은 30대 초반의 기자가 매끄럽게 말을 이었다.

「새해가 밝고 불과 열흘 만에 무려 세 차례의 변이 게이트가 발생했는데요. 이에 대한 대통령님의 생각을 여쭙고 싶습니다.」

고세원의 시선이 자연스럽게 옆을 향했다.

딱딱하게 굳은 얼굴과 핏발 선 눈동자. 석고준의 시선은 홀로그램 영상 속 한 인물을 노려보고 있었다.

‘아.’

문득 오는 길에 봤던 기사 중 하나가 뇌리를 스쳤다. 진태경과 대통령이 신년을 맞아 공식 기자회견을 연다는 소식.

어느 정도 짐작은 했지만, 지금처럼 분노한 상태의 석고준이 저걸 본다는 건 맹독을 삼키는 것이나 다름없었다.

‘어린애한테 스너프 필름을 보여 주는 꼴이지.’

마음을 결정한 고세원이 허리를 굽혀 바닥에 떨어진 리모컨을 집으려던 그때였다.

“경호팀장.”

귓가를 파고드는 성마른 목소리. TV에 시선을 고정한 석고준이 한마디를 툭 내뱉었다.

“놔둬.”

“……올려만 두겠습니다.”

잠시 멈칫한 고세원이 유리 조각이 묻은 리모컨을 털어 소파 앞 탁자에 올려 두는 사이, 홀로그램 TV에서는 40대 초반의 중년인이 발언을 시작하고 있었다.

「좋은 질문입니다.」

듣기 좋은 목소리. 선하지만 만만해 보이지 않는 인상.

대한민국의 27대 대통령이자, 만 40세의 나이로 최연소 당선 기록을 수립한 백한성 대통령이 부드러운 어조로 말을 이었다.

「어제 오후, 청와대 공식 발표를 보신 분이라면 아시겠지만 이번에 잇따라 발생한 변이 게이트는…….」

당황하지 않고 차분한 태도는 사람들로 하여금 신뢰를 불러일으키기 마련이다.

흡입력 있는 목소리로 토해 내는 연설과 중간중간 알 듯 모르게 섞이는 유머는 백한성의 대통령의 장기 중 하나였다. 사람들이 집중하는 것도 당연했다.

흡사 대선 출마 선언 때와 같은 일장연설이 끝나자 기자들 사이에서 힘찬 박수가 터져 나왔다.

“완전히 선거 유세장이 따로 없군.”

분노와 비웃음이 섞인 한마디를 툭 내뱉은 석고준이 중얼거렸다.

“저 안에 있는 놈 중에, 우리가 준 돈 안 받아 처먹은 놈이 얼마나 될까. 응?”

“…….”

“스승님이 계셨을 때는 숨도 제대로 쉬지 못했던 놈들이지. 역대 최연소 대통령? 반(反) 아레스 길드? 백한성 저 새끼도 결국 스승님 발밑이었어.”

씹어뱉는 듯한 목소리에서 과거에는 찾아볼 수 없던 치욕과 분노가 흘러넘쳤다.

조용히 눈을 내리깐 고세원은 머릿속이 차가워지는 것을 느꼈다.

‘사실이지. 이제는 옛날이야기가 되어 버렸지만.’

이정룡의 영향력은 그야말로 막강했다.

자취를 감추기 전에도 세상일에는 별다른 관심이 없던 천태민이 구름 위의 신선이었다면, 이정룡은 지상에 남아 대통령 혹은 왕 이상의 지위를 누렸다.

‘그래. 그땐 그랬지…….’

정계. 재계. 새로운 권력층으로 급부상한 거대 길드의 주인들까지 이정룡에게 허리를 굽혔다.

그는 천태민의 곁에서 엄청난 공을 세운 영웅이었고, 사라진 구세주의 의형제로서 전권을 위임받은 교황이나 다름없었다.

‘또 다른 바티칸.’

대한민국의 국민은 이 150층짜리 초고층 빌딩을 두 번째 청와대라고 부르지만, 실상은 교황이 사는 바티칸에 가까웠다.

무능한 정부와 국회의원들을 욕하는 이들도 아레스 길드라는 이름 앞에서는 쉽게 입을 열지 못했다.

그것은 마치 신성불가침(神聖不可侵)의 영역에 가까웠다.

하지만…….

「이 세상은! 전 세계는! 지금도 변화하고 있습니다! 새로운 국면에 접어들었습니다!」

끝없이 이어지는 박수갈채를 받으며 힘차게 외치는 TV 속 대통령의 말처럼, 모든 것이 뒤바뀌고 있었다.

이정룡이라는 거인이 쓰러지자 그로부터 드리워진 그늘이 걷히기 시작한 것이다.

그리고…… 이 모든 사건의 중심에는 한 사람의 존재가 강력하게 작용했다.

「그러나, 국민 여러분! 저를 포함한 정부는 국민 여러분들의 안전을 위해 온 힘을 다할 것입니다! 지금 제 옆에 앉아 있는 이 청년과 함께! 안팎의 모든 위협으로부터 대한민국을 지켜 낼 것입니다!」

백한성 대통령은 청년의 이름을 직접적으로 호명하지 않았지만, 모두가 그의 이름을 안다.

지난 몇 달 사이, 20대 후반의 청년은 인류 역사상 가장 유명한 인물 중 한 사람이 되었으니까.

「와아아아!」

「진태경! 진태경!」

「시벌! 시부럴!」

그 어느 때보다 우렁찬 환호가 기자 회견장을 떨어 울렸다.

비스듬히 턱을 괸 채 잠들어 있던 청년, 진태경이 번쩍 눈을 뜨더니 미친 듯한 속도로 박수를 치며 대통령을 바라보았다.

「정말이지 대단한 연설이었습니다, 대통령님. 특히 마지막에 하신 말씀은 가슴을 울렁거릴 정도로…….」

「저기, 마지막에는 진태경 헌터님 얘기를 했습니다.」

「아, 잠시만요. 진짜 속 울렁거려요. 갑자기 멀미 날 것 같아요.」

「이거 다 찍히고 있습니다. 우선 침 자국부터 어떻게 좀 닦으시고…….」

「편집, 편집해 주세요. 제발요. 네?」

「시작 전에 몇 번이나 말씀드렸잖습니까. 생방송이라고.」

「맞네. 와, 시부럴 거. 조졌다.」

「생방송입니다. 생방송이라고요, 제발. 진태경 헌터. 예?」

식은땀을 흘리는 40대의 대통령과 20대의 젊은 영웅의 모습은 고스란히 전파를 탔다.

대한민국 방송 역사에 기록될 만큼 엄청난 방송 사고지만, 누구도 진태경을 나무라거나 욕하지 않을 것이다.

지금도 카메라에 잡힌 사람들은 얼굴을 찌푸리긴커녕, 오히려 웃음 가득한 표정으로 그의 이름을 연호하고 있었다.

‘진태경.’

그리고 그 광경을 지켜보던 고세원은 문득 깨달았다.

홀로그램 TV 속 저 청년과 그를 둘러싼 사람들의 반응이, 조금 전 자신이 머릿속에 떠올렸던 어떤 단어와 닮아 있다는 것을.

‘……신성불가침?’

천태민이라는 태양에 비하면 진태경은 아직 횃불에 불과하다.

하지만 한 가지만큼은 부정할 수 없다.

지금의 진태경은, 불멸의 영웅으로 기억된 한 사람과 같은 길을 걷고 있다는 것.

그리고 어쩌면. 진태경의 바람과는 상관없이 주위의 상황이 그를 제2의 천태민으로 만들고자 한다는 것.

「진태경 씨! 이번 일어난 세 번의 변이 게이트를 모두 홀로 진압했다고 들었습니다! 이에 관해 한 말씀 해 주시죠!」

「혼자는 아니었고, 둘이긴 했는…….」

「진태경 씨! 무당일보 김진무 기자입니다!」

「이번 변이 게이트에 관하여 질문이 있습니다!」

마이크를 잡은 기자들이 벌떼처럼 달려들고, 카메라 플래시가 쉴새 없이 터져 나온다.

사방에서 섞여드는 기자들의 질문에 귀를 기울이고 있던 고세원은 문득 기시감을 느꼈다.

‘이건…….’

흐름이 이상하다. 일견 보기에는 자연스럽지만, 누군가에 의해 의도된 어떤 방향으로 모두가 달려가고 있었다.

그리고 다음 순간, 어느 이름 모를 기자의 외침을 들은 고세원은 등골을 엄습하는 한기를 느꼈다.

「이틀 전 진압하신 세 번째 변이 게이트에 관하여 질문이 있습니다! 저희 신문이 입수한 정보에 따르면 해당 게이트는 유명 모 길드가 맡고 있는…….」

“……!”

이거구나. 이거였구나.

섬광 같은 깨달음과 함께, 고세원은 황급히 리모컨을 향해 손을 뻗었다. 하지만 그보다 한발 빠르게 움직인 누군가의 손이 있었다.

콰드드득!

리모컨과 함께 탁자를 박살 낸 석고준의 안광이 붉게 번뜩였다.

“내가 분명히 놔두라고 했을 텐데.”

“하지만 부길드장님…….”

“두 번 말 안 한다.”

실핏줄이 터져 나간 상관의 눈. 이내 이어진 목소리는 소름이 끼칠 만큼 섬뜩했다.

“가만히 있어. 죽기 싫으면.”

“흡……!”

자신도 모르게 헛숨을 삼킨 고세원은 반쯤 뗐던 몸을 무너지듯 소파에 기댔다.

그사이 홀로그램 TV에서는 그가 그토록 우려했던 상황이 벌어지고 있었다.

「맞습니다. 아레스 길드가 담당하는 게이트였어요. 뭐, 무늬는 영구 임대긴 한데. 다들 아시는 것처럼 실소유나 다름없죠.」

거대 길드의 게이트 독점은 알면서도 쉬쉬하는 공공연한 비밀.

그러나 진태경은 생방송으로 진행되는 청와대 공식 기자 회견장에서 서슴없이 치부를 들춘 것으로도 모자라, 심지어는 한발 더 나아갔다.

「정확한 정황이요? 마력 수치는 계속해서 오르고 있는데 구조팀이 안 오는 그런 상황이었죠.」

먹잇감을 포착한 기자들이 앞다투어 나섰다.

그중에는 한때나마 아레스 길드의 검은돈을 받은 이들도 상당한 숫자를 차지하고 있었지만, 돈은 더 큰 돈에 넘어가는 법이다.

「잠깐, 잠깐만요. 기다려도 구조팀이 도착하지 않았단 말입니까?」

진태경이 고개를 끄덕였다.

「네. 최초 상황으로부터 15분이 지나도 안 오더라고요. 그사이에 마력 수치가 점점 더 상승해서 변이 게이트가 되어 버렸고.」

「그건, 구조팀이 제때 도착했다면 게이트가 본격적으로 변이되기 전에 해결할 수 있었을 거라는 뜻입니까?」

「뭐, 100퍼센트 확신은 못 하지만 A급 헌터 한 명이라도 끼워서 조기 투입했으면 아마 자체적으로 해결할 확률이 높았을 겁니다.」

「또 다른 변이 게이트와 달리, 해당 게이트를 담당했던 길드는 엄청난 헌터 인력과 자본을 소유하고 있는 것으로 압니다. 그런데 왜 제때 구조팀을 파견하지 못했다고 생각하십니까?」

「이유라……. 글쎄요.」

잠깐 생각하던 진태경이 아무렇지 않게 한마디를 툭, 하고 던졌다.

「아무래도 그쪽 집안이 요즘 시끄러운 것 같던데요. 사장님이라고 해야 하나? 운영진도 교체되고, 이래저래 혼선이 좀 있었겠죠.」

콰직!

옆에서 무언가가 으스러지는 소리를 들으며, 고세원은 지그시 눈을 감았다.

‘끝났군.’

엄청난 인력과 자본을 소유한 모 거대 길드. 운영진 교체.

두 가지 핵심 키워드만으로도 충분하다. 굳이 인터넷에서 찾아보지 않더라도 알만한 사람은 모두 알 것이다.

비록 아직 정확한 이름이 밝혀지지는 않았지만…….

「심각한 실수이기는 해도 어쩌겠어요. 때마침 제가 있어서 사망자는 나오지 않았으니 개인적으로는 다행이라고 생각합니다. 아, 그리고 이 자리를 빌어 다시 한번 삼가 고인의 명복을 빕니다.」

「훌륭한 답변입니다, 진태경 헌터. 작고하신 고인께서도 고맙고, 대견하게 생각하시리라 믿어 의심치 않습니다.」

빌어먹을. 고세원은 내심 작은 욕설을 중얼거리며 감았던 눈을 떴다.

TV 속에서는 어느새 다시 마이크를 쥔 한국 최연소 대통령이 마지막 일격을 가하고 있었다.

「다행히 사망자 없이 사태를 마무리 지었지만, 이번 일은 우리 정부가 나서서 적극적으로 조사를 시작할 방침입니다. 해당 길드의 소홀한 조치는 이 대한민국의 대통령으로서! 더불어 한 사람의 국민으로서 매우 유감스럽지만, 훌륭한 영웅이셨던 고인의 뜻과 유지는 진태경 헌터에게 고스란히 이어져…….」

대통령의 말은 끝까지 이어지지 못했다. 아니, 정확히 말하자면 고세원은 들을 수 없었다.

“……!”

본능적으로 방어 자세를 취한 순간. 빛살 같은 속도로 뻗어 나간 강대한 마나가 홀로그램 TV를 부수고, 사방을 찢어발겼다.

콰과과과광!

고위 마법사 열 명이 달라붙어 설치한 중첩 보호 마법진이 깨지고, 방탄유리를 비롯한 모든 것이 산산 조각나며 이내 가루로 흩어진다.

그 모든 붕괴의 중심에, 혈안(血眼)을 한 석고준이 있었다.

“감히! 감히! 감히이-!”

쾅! 쾅! 콰아앙!

모든 것에는 한계가 존재한다.

그리고 방금의 한마디는, 부길드장이 된 석고준이 며칠 사이 억누르고 참아 왔던 모든 분노에 불을 붙였다.

“죽인다! 반드시! 반드시 죽인다!!”

꽈아아앙!

석고준은 이정룡의 뒤를 이은 실질적인 후계자지만, 오늘의 기자회견을 본 사람들은 달리 생각할 것이다.

진태경이야말로 새로운 영웅이며, 아직까지도 모습을 드러내지 않은 천태민과 얼마 전 사망한 이정룡의 뜻을 이어받은 유일한 사람이라고.

“진태경! 진태겨영!”

이성을 상실한 채 피를 토하듯 고함을 내지르는 석고준의 모습을 응시하는 고세원의 눈동자가 깊게 가라앉았다.
```

## Final English reading copy

```markdown
# Chapter 563

“You’re later than usual.”

Go Jun was wrong. Go Se-won’s watch was always accurate, and there was still plenty of time before the designated start of the workday.

So it wasn’t Go Se-won who was different from usual. It was simply that his superior was in an unusually foul mood today.

Still, Go Se-won kept his words to a minimum and quietly bowed his head.

“I’m sorry.”

“Enough. Sit down.”

Being allowed to sit on the same sofa as Go Jun was one of the privileges reserved for his closest aides.

But before Go Se-won could even sit down on the Italian leather sofa, he realized that his superior’s anger had not yet run its course.

> “This is reporter Go Hyeon-woo of Rough News.”

The reporter in his early thirties who had been given the floor in the holographic television broadcast continued speaking smoothly.

> “It has only been ten days since the new year began, yet three Mutated Gates have already appeared. What are your thoughts on this, Mr. President?”

Go Se-won’s gaze naturally shifted to the side.

Go Jun’s face was stiff, and his eyes were bloodshot. He was glaring at one person in the holographic footage.

*Ah.*

One of the articles he had seen on the way there suddenly came back to him. It had announced that Jin Taekyung and the President would be holding an official New Year’s press conference.

He had more or less guessed what was happening, but watching the broadcast in his current state was no different from forcing Go Jun to swallow deadly poison.

*Like showing a snuff film to a child.*

Go Se-won had made up his mind and was bending down to pick up the remote from the floor when—

“Head of Security.”

The curt voice stabbed into his ear. Without taking his eyes off the television, Go Jun tossed out a single word.

“Leave it.”

“…I’ll only put it back.”

Go Se-won paused for a moment, then brushed the shards of glass off the remote and placed it on the table in front of the sofa. By then, a middle-aged man in his early forties had begun speaking on the holographic television.

> “That’s an excellent question.”

His voice was pleasant to listen to. His expression was kind, but not the least bit weak.

Baek Hanseong, the twenty-seventh President of Korea and the youngest person ever elected to the office at the age of forty, continued in a gentle tone.

> “As anyone who saw the Blue House’s official announcement yesterday afternoon will know, the series of Mutated Gates that have appeared this time—”

A calm, unruffled attitude naturally inspired trust.

One of President Baek Hanseong’s specialties was delivering stirring speeches in a compelling voice, with bits of humor slipped in here and there so subtly that people weren’t sure whether he had meant them as jokes.

No wonder everyone was paying attention.

When the speech finally ended after what sounded almost exactly like his declaration of candidacy for president, vigorous applause erupted among the reporters.

“It’s practically a campaign rally.”

Go Jun spat out the words, anger and mockery mingling in his voice. Then he muttered,

“How many of those bastards in there haven’t taken the fucking money we gave them, huh?”

“……”

“They couldn’t even breathe properly when Master was around. The youngest president in history? Anti-Ares Guild? That bastard Baek Hanseong was still beneath Master’s feet in the end.”

Humiliation and rage poured from his voice—emotions that had never been visible in him before.

Go Se-won lowered his eyes in silence and felt his thoughts grow cold.

*It’s true. Even if it has become a story from the past now.*

Lee Jungryong’s influence had been overwhelming.

Before Cheon Taemin disappeared, he had shown little interest in worldly affairs and seemed like an immortal living above the clouds. Lee Jungryong, on the other hand, had remained on the ground and enjoyed a status on par with—or even above—that of a president or king.

*Yes. That was how it was back then…*

Politicians. Business leaders. Even the masters of the enormous Guilds that had risen rapidly as a new power class had bowed before Lee Jungryong.

He had been a hero who accomplished incredible deeds at Cheon Taemin’s side, and, as the sworn brother of the vanished savior, he had been no different from a pope entrusted with absolute authority.

*Another Vatican.*

The people of Korea called the 150-story skyscraper a second Blue House, but in reality, it was closer to the Vatican where the pope lived.

Even those who cursed the incompetent government and lawmakers found it difficult to speak freely in the presence of the name Ares Guild.

It had been practically sacrosanct.

But—

> “This world! The entire world! Is changing even now! We have entered a new phase!”

Everything was changing, just as the President shouted while receiving endless applause from the crowd on television.

With the fall of the giant known as Lee Jungryong, the shadow he had cast over the world was beginning to recede.

And at the center of all these events, one person’s presence was exerting a powerful influence.

> “However, my fellow citizens! The government, myself included, will do everything in our power to protect your safety! Together with the young man sitting beside me! Together, we will protect Korea from every threat, both within and without!”

President Baek Hanseong did not call the young man by name, but everyone knew who he was.

Over the past few months, the young man in his late twenties had become one of the most famous people in human history.

> “Waaaaah!”

> “Jin Taekyung! Jin Taekyung!”

> “Fuck! Fucking fuck!”

The cheers that shook the press conference hall were louder than ever.

The young man who had been sleeping with his chin propped at an angle suddenly opened his eyes. Then he began clapping at a frantic speed while staring at the President.

> “That was truly an incredible speech, Mr. President. Especially your final words. They moved me so deeply that I feel—”

> “Um, that last part was about you, Hunter Jin Taekyung.”

> “Ah, wait a moment. My stomach really is churning. I think I’m suddenly getting motion sickness.”

> “All of this is being filmed. Please wipe the drool off your face first—”

> “Please edit that out. Please. All right?”

> “I told you several times before we started. This is live.”

> “Right. Wow, fucking hell. I’m screwed.”

> “It’s live. I said it’s live, please. Hunter Jin Taekyung. Hello?”

The sight of the sweating President in his forties and the young hero in his twenties was broadcast in its entirety.

It was a broadcasting accident that would go down in the history of Korean television, but no one would scold or curse Jin Taekyung for it.

Even now, the people caught on camera were not frowning. Instead, they were shouting his name with faces full of laughter.

*Jin Taekyung.*

Watching the scene, Go Se-won suddenly realized something.

The young man on the holographic television and the reactions of the people surrounding him resembled a word that had come to mind only a moment earlier.

*…Sacrosanct?*

Compared to the sun that was Cheon Taemin, Jin Taekyung was still nothing more than a torch.

But one thing could not be denied.

Jin Taekyung was walking the same path as the man who would be remembered as an immortal hero.

And perhaps, regardless of Jin Taekyung’s wishes, the circumstances around him were trying to turn him into a second Cheon Taemin.

> “Mr. Jin Taekyung! I heard you suppressed all three Mutated Gates that appeared this time by yourself! Would you say a few words about that?”

> “I wasn’t alone. There were two of us, though—”

> “Mr. Jin Taekyung! This is Kim Jin-mu of the Mudang Daily!”

> “I have a question about the Mutated Gates!”

The reporters holding microphones rushed toward him like a swarm of bees, and camera flashes erupted without pause.

As Go Se-won listened to the questions from every direction, he suddenly felt a sense of déjà vu.

*This is…*

Something about the flow was strange. At first glance, it seemed natural, but everyone was racing in a direction someone had deliberately chosen.

Then, when he heard a shout from some unknown reporter, a chill ran down Go Se-won’s spine.

> “I have a question about the third Mutated Gate you suppressed two days ago! According to information obtained by our newspaper, that Gate was being handled by a famous Guild—”

“……!”

*This is it. So this was it.*

The moment enlightenment flashed through him, Go Se-won hurriedly reached for the remote.

But someone else’s hand moved faster.

*Crunch!*

Go Jun crushed the table along with the remote. A red glare flashed in his eyes.

“I believe I told you to leave it alone.”

“But, Vice Guild Master—”

“I won’t say it twice.”

The blood vessels in his superior’s eyes had burst. The voice that followed was so chilling that it raised goose bumps.

“Stay still if you don’t want to die.”

“Ghk—!”

Go Se-won swallowed a breath without meaning to and leaned back against the sofa as though his half-raised body had collapsed.

Meanwhile, the situation he had feared was unfolding on the holographic television.

> “That’s right. It was a Gate handled by Ares Guild. Well, technically, it was under a permanent lease. But as everyone knows, that’s practically the same as owning it.”

The giant Guilds’ monopoly over Gates was an open secret. Everyone knew about it, but no one spoke openly.

Yet Jin Taekyung had not only exposed that ugly truth without hesitation during a live official press conference at the Blue House—he had gone one step further.

> “The exact circumstances? The mana levels kept rising, but the rescue team never came.”

The reporters who had spotted their prey rushed forward one after another.

Quite a few of them had once taken Ares Guild’s black money, but money always gave way to more money.

> “Wait, wait a moment. Are you saying the rescue team never arrived?”

Jin Taekyung nodded.

> “Yes. They still hadn’t come fifteen minutes after the initial situation began. In the meantime, the mana levels kept rising until the Gate became a Mutated Gate.”

> “Does that mean the Gate could have been dealt with before it fully mutated if the rescue team had arrived in time?”

> “Well, I can’t be a hundred percent certain, but if they had sent in even one A-rank Hunter early on, there probably would have been a high chance of resolving it without outside assistance.”

> “Unlike the other Mutated Gates, the Guild responsible for this Gate is known to possess an enormous number of Hunters and vast financial resources. Why do you think it failed to send a rescue team in time?”

> “The reason… Well, I’m not sure.”

Jin Taekyung thought for a moment before casually tossing out his next words.

> “That family seems to be having a lot of trouble these days. Or should I say, the boss? Their management has changed, too, so I imagine there was probably some confusion here and there.”

*Crack!*

Hearing something beside him being crushed, Go Se-won slowly closed his eyes.

*It’s over.*

A certain giant Guild with enormous manpower and capital. A change in management.

Those two key phrases alone were enough. Anyone who knew anything would understand, even without looking it up online.

Although the exact name had not yet been revealed—

> “It was a serious mistake, but what could I do? Fortunately, I happened to be there, so no one died. Personally, I’m just glad about that. Oh, and while I have this opportunity, I’d like to once again offer my deepest condolences to the deceased.”

> “That was an excellent answer, Hunter Jin Taekyung. I have no doubt that the deceased would also be grateful and proud.”

*Damn it.*

Go Se-won muttered a quiet curse inwardly and opened his eyes.

On the television, Korea’s youngest President had taken the microphone again and was delivering the final blow.

> “Fortunately, we were able to bring this incident to an end without any fatalities, but our government intends to take the initiative and begin a thorough investigation. As President of Korea—and as a citizen—I find this Guild’s negligent response deeply regrettable. However, the wishes and legacy of the deceased, who was a great hero, have been passed on in their entirety to Hunter Jin Taekyung—”

The President’s words did not reach the end.

No—in precise terms, Go Se-won could no longer hear them.

“……!”

The instant he instinctively took a defensive stance, powerful mana shot out at the speed of a beam and shattered the holographic television, tearing the surroundings apart.

*Kwa-gwa-gwa-gwang!*

The overlapping protective magic circles installed by ten high-ranking mages shattered. Bulletproof glass and everything else burst into pieces, then scattered as dust.

At the center of the collapse stood Go Jun, his eyes bloodshot.

“How dare you! How dare you! How dare you—!”

*Bang! Bang! Kraaang!*

Everything had its limits.

And that one sentence had just set fire to all the rage Go Jun had forced down and endured over the past several days since becoming Vice Guild Master.

“I’ll kill him! I’ll kill him no matter what!”

*Kwaaaang!*

Go Jun was Lee Jungryong’s de facto successor.

But the people who watched today’s press conference would think differently.

They would believe that Jin Taekyung was the new hero—and the only person who had inherited the will of Cheon Taemin, who had still not revealed himself, and Lee Jungryong, who had died only recently.

“Jin Taekyung! Jin Taekyuuung!”

Go Se-won stared at Go Jun as he screamed until he seemed to be spitting blood, having completely lost his reason.

His gaze grew dark and unfathomable.
```

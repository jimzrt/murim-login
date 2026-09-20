<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0555.txt",
      "sha256": "777b5071304c79e6f81463ec3ee399012c26a8764db38793e474b85d02c20ea6",
      "bytes": 13959
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "0582fdcfb4727b331c7d2b8ef00f17afb232e987b40f67795dc7a801ddcefd64",
      "bytes": 3935
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "083c2edfbe7b4d06082c44376601898ab85cdab281050e8cede7a6170233694c",
      "bytes": 175414
    },
    {
      "path": "characters/Cheon Taemin.md",
      "sha256": "c838bc35bd5e8388ca6da890e63e110eb13fd64ea302a1011fd91b24c22069fe",
      "bytes": 590
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "297cf1ed6cc56687a5f3b87cb40e2cbfad1042cfa251aade345d2d31b5bf582e",
      "bytes": 553
    },
    {
      "path": "characters/Go Jun.md",
      "sha256": "f5e0bf756680e0466c19c4ef28f9ff36ef68b0cc2f1faf8d42e249913e71dc27",
      "bytes": 819
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "fad13bb850362fbea26ef137abb95516cebcc92321997a7ef6e38fe44eef1f15",
      "bytes": 2292
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "27a0db5313bc2b9a032bd74243a696656c1be67e09a2c5c72b55b449998b0c35",
      "bytes": 622
    },
    {
      "path": "characters/Lee Jungryong.md",
      "sha256": "b2c2b5c66671685d72239180a315ce58f2f045a4057539b171bfffe510b506a4",
      "bytes": 1182
    },
    {
      "path": "characters/Team Leader Choi.md",
      "sha256": "4a80288f0efd0928278f097a0cc0099d47312bfffe1d0099afa49262fce08004",
      "bytes": 714
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "f2fcd88e711bdfdba8370312c476aaf6d1ef90fc5464b793863371b52d2aa6d2",
      "bytes": 167924
    }
  ],
  "estimated_tokens": 11725
}
-->

# Durable State Update — Chapter 555

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 555. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 555. Profile updates may replace only one
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
  "chapter": 555,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 555,
    "continuity_sources": [555],
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
    "The Fire Dragon Pavilion's six-member first mission is to enter Nanman through the Journey to Nanman Quest, whose reward is a linked quest and whose failure penalty is the Title Can't Go to Nanman; the party secretly departed Henan.",
    "Taekyung is a Supreme Peak master with Three Flowers Gather at the Crown, advanced Qi Sense, exceptional resistance to monster Fear, public S-rank-level recognition while retaining an A-rank license, and leadership of the Fire Dragon Pavilion's first mission to Nanman.",
    "Mungyeong ended Taekyung's direct training and assigned him the final task of incorporating martial principles into his learned martial arts; Cheongpung accompanies Mungyeong and learns through observation.",
    "Mungyeong considers Nanman a plausible site for Dark Heaven's second rift, while Dark Heaven remains a monster-like threat capable of causing rifts and creating mutants; the mechanism behind Jang Sam's transformation remains unresolved.",
    "The Mount Song Resolution restored the Murim Alliance; Mae Jonghak is Alliance Leader, Jeok Cheongang heads the Five Kings Hall, and Murong Yeonghwi oversees Murong Family defenses in Liaoning.",
    "Zhuge Feng's Demon-Sealing Formation still blocks mana from the exposed Gate, while Jang Taebo processes the Water God Dragon's remains.",
    "The Southern Heaven Demon Empress is believed to be moving toward the suspected next target, while Song Ho's dispatch there has received no reply for more than seven days.",
    "Taekyung is in the modern world on January 1, 2047, staying with Kim Jeonghee and Hayeon at Team Leader Choi's mansion, where Cheon Taemin once lived.",
    "The public believes the Lich killed Lee Jungryong and Wu Heixing; Lee is being honored as a Great Cataclysm hero and is scheduled to receive a national funeral, while Taekyung knows the actual deaths were caused by him.",
    "Go Jun, Lee Jungryong's disciple and former Head of Security, has returned from Sichuan with Ares Guild members and is publicly regarded as a likely successor to Ares leadership.",
    "Team Leader Choi deliberately revealed his connection to Cheon Taemin as the old hero's only living blood relative and intends to acquire the Ares Guild with its influence intact before removing Lee's corruption.",
    "Choi knows that Taekyung keeps secrets about his identity, while Taekyung recognizes that Choi has been waiting for the opportunity created by Lee's death."
  ],
  "continuity_sources": [
    554,
    553
  ],
  "open_questions": [
    "What is the Lord of Heaven's identity, how is he connected to the dangerous force Taekyung associates with his original world, and how can Dark Heaven open Gates?",
    "What will Taekyung's party find in Nanman, and what does the Southern Heaven Demon Empress intend there?",
    "What is the outcome of the duel between Jeok Cheongang and Nangong Cheon, and why did Ju Hwaran and Sama Pyo's political engagement end?",
    "What process created Jang Sam's mutant form, and can Dark Heaven's mutants absorb human energy?",
    "What are Cheon Taemin's current whereabouts and life status, and can Team Leader Choi secure control of Ares Guild?"
  ],
  "safe_through": 554,
  "temporary_decisions": [
    "Render 건량 as dry rations, 광서 as Guangxi, 대별산 as Mount Daebyeol, 만리행 as Ten-Thousand-Li Journey, and 고잉메리호 as Going Merry.",
    "Render 반 시진 as half a shichen and retain Nanman, Nanman Beast Palace, Fire Dragon Pavilion, Great Hero, and Young Lady Ju.",
    "Render 남만행 as Journey to Nanman and 남만을 못 가 as Can't Go to Nanman.",
    "Render 면구 as disguise mask, 역용술 as disguise technique, 각주님 as Pavilion Master, 로그아웃 as Logout, and 동기화 as Synchronization.",
    "Render 소격변 as Small Cataclysm, 낭중지추 as needle in a bag, and 국장 as national funeral."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 최민우    | **Choi Minwoo**   |
| 천태민    | **Cheon Taemin**  |
| 이정룡    | **Lee Jungryong** |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 몬스터     | **monster**           |
| 길드      | **Guild**             |
| 길드장     | **Guild Master**      |
| 부길드장    | **Vice Guild Master** |
| 팀장      | **Team Leader**       |
| 대격변     | **Great Cataclysm**   |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 고준 | **Go Jun** | Personal name of Team Leader Seok; Lee Jungryong's prized Disciple. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 평화 | **Peace Guild** | Guild name. |
| 대한민국 | **Korea** | Country reference. |
| 아레스 | **Ares Guild** | The leading Guild in Korea; formerly employed Team Leader Choi and Song Song. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 너구리 | **Neoguri** | Instant-noodle brand used in Taekyung's flavor joke. |
| 청와대 | **Blue House** | Presidential office mentioned in an online comment about proposed legislation. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 도도 | **Dodo** | Term for the Star-Array Grand Banquet's major gambling matches. |
| 국정원 | **NIS** | South Korea's National Intelligence Service, mentioned in Taekyung's joke. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 준이 | **Jun** | Family nickname used in the form Jun's dad. |
| 석고준 | **Go Jun** | Source full-name form for the established Go Jun, also known as Team Leader Seok. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 대통령 | **President** | Title for Korea's head of state. |

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
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 최민우 | 진태경 | trusted allied team leader to younger allied Hunter | Mr. Jin | formal-polite and concerned | Choi warns Jin about the danger of the operation and affirms his deep trust. |
| 진태경 | 최민우 | younger allied Hunter to allied team leader | Team Leader Choi | polite, familiar, and teasing | Jin jokes with Choi while acknowledging and dismissing his concern. |
| 고준 | 진태경 | Ares Guild combatant confronting the killer of his Master | you | hostile and informal | Go Jun uses 너 while demanding Jin confess to Lee Jungryong's death and threatening retaliation. |
| 진태경 | 고준 | dominant adversary confronting Lee Jungryong's Disciple | you | contemptuous and informal | Jin uses 너 and 놈 while overpowering Go Jun and ordering him to end the conflict with Lee Jungryong. |
| 진태경 | 대통령 | Hunter_to_President | Mr. President | formal-polite | Taekyung addresses the President respectfully during their airport greeting. |
| 대통령 | 진태경 | President_to_Hunter | Mr. Jin Taekyung | formal-polite | The President addresses Taekyung by name at the airport photo line. |

## Listed compact profiles

### Cheon Taemin.md

# Cheon Taemin (천태민)

- **Safe through:** Chapter 554
- **Aliases:** Slayer
- **Role:** Ares Guild Master; humanity's great hero and the world's greatest Hunter; killed the Demon King and is known as the Slayer; created the first Mana Cultivation Method during the Great Cataclysm.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** Maternal grandfather of Team Leader Choi and father of Soyeong; regarded by Lee Jungryong as an older brother despite their lack of blood relation.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 554
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Go Jun.md

# Go Jun (고준)

- **Safe through:** Chapter 554
- **Aliases:** Team Leader Seok
- **Role:** Go Jun is the leader of Lee Jungryong's security team, an Ares Guild combatant, Lee's disciple and right-hand man, and the expected successor to Ares Guild leadership after Lee's death.
- **Personality:** Highly disciplined, fiercely loyal to Lee Jungryong, confident in his abilities, and capable of suppressing his anger and killing intent under provocation.
- **Voice:** Dry, controlled, and formal with subordinates; deferential when addressing his Master.
- **Relationships:** Disciple and direct protégé of the late Lee Jungryong, Go Jun confronted Jin Taekyung over Lee's death and was forced to accept Jin's demand that the conflict end with Lee.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 554
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, a Supreme Peak master who possesses the Heavenly Martial Physique and superhuman physical strength, has manifested Force, opened his Middle Dantian, crossed the wall into true mastery, has achieved Three Flowers Gather at the Crown but not Five Qi Returning to Origin, can perceive the texture of qi well enough to sever layered magic, can resist high-level monster Fear through exceptional mental strength, is publicly recognized as an S-rank-level Hunter while formally retaining an A-rank license pending testing, can command coordinated raids against powerful monsters, and now serves as one of the two pavilion masters of the Alliance Leader's direct Fire Dragon Pavilion while holding its unique Title, Fire Dragon Pavilion Master and leading its first mission to Nanman.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor and assigned him a final task to incorporate martial principles into his learned martial arts but declined Taekyung's recruitment after Cheongpung reached him first, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate, student, and trusted manager of media and official arrangements, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, and Xiao Shen regards him as an older brother after Jin saved him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 554
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Lee Jungryong.md

# Lee Jungryong (이정룡)

- **Safe through:** Chapter 554
- **Aliases:** None
- **Role:** Former Vice Guild Master of Ares Guild, one of Korea's two S-rank Hunters, and a Supreme Peak-level martial artist who was killed by Jin Taekyung.
- **Personality:** Outwardly genial, calm, and humorous; calculating, opportunistic, manipulative, coercive, and ruthless when challenged
- **Voice:** Smooth, good-natured, and indirect, using teasing conversation and veiled threats before becoming openly furious
- **Relationships:** Master of Park Jihoon and Go Jun (Team Leader Seok), whom he personally selected and trained; longtime Great Cataclysm acquaintance of Park Tae Seop; adversary of Jin Taekyung; knew Team Leader Choi from childhood; has an antagonistic history with Kim Hwajong, who saved his life at the collapse of Mapo Bridge eighteen years earlier; was visibly shaken by learning that Choi is Cheon Taemin's maternal grandson; regards Cheon Taemin as an older brother despite no blood relation and has long held him in respect and fear; operates as Ares Guild's senior authority beneath its Guild Master

### Team Leader Choi.md

# Team Leader Choi

- **Safe through:** Chapter 554
- **Aliases:** Choi Minwoo (최민우)
- **Role:** Team Leader Choi is Cheon Taemin's only living blood relative and is positioning himself to take control of the Ares Guild after Lee Jungryong's death.
- **Personality:** Strategic, candid, controlled, and possessive of the power and influence he intends to inherit.
- **Voice:** Dry, formal, and direct, with calm candor and carefully chosen metaphors.
- **Relationships:** Maternal grandson and only living blood relative of Cheon Taemin; was kept out of public knowledge by Lee Jungryong and now seeks to acquire the Ares Guild intact.

## Korean source

```text
＃555화



철탑 같은 체격의 사내였다. 고저 없는 표정은 바위처럼 딱딱했고 입술은 굳게 다물어져 있었다.

그리고…… 눈이 있었다.

붉게 핏발 선 한 쌍의 눈동자. 이루 말할 수 없을 정도의 분노와 슬픔. 또 다른 여러 감정이 뒤섞인 사내의 눈은 마주 보는 것만으로도 오한이 들었다.

그것은 UN 상임 이사국이자 강대국으로 손꼽히는 대한민국의 국무총리라 해도 예외일 수 없었다.

‘무슨 놈의 눈빛이…….’

문을 열고 들어오자마자 칼날처럼 파고드는 시선에, 순간 흠칫한 국무총리는 떨리는 가슴을 애써 진정시켰다.

비록 상대가 국내에서도 손꼽히는 실력을 지닌 헌터라지만 자신 역시 환갑이 되도록 정치라는 진흙탕에서 구른 몸.

이야기를 시작하기도 전에 겁먹을 이유는 없었다.

‘특히, 지금 같은 상황에서는 더더욱.’

한결 여유를 되찾은 국무총리가 사내를 향해 손을 내밀었다.

“어이고, 여기 계셨군요. 석고준 씨.”

자신을 향해 내민 손을 빤히 바라보던 사내, 석고준이 악수 대신 건조한 목소리로 대답했다.

“오랜만입니다, 장 총리님.”

한참 연장자에 대한 예의도, 자국의 국무총리를 대하는 태도도 아니다. 장 총리의 이마에 자글자글한 주름이 맺혔다.

“……허허. 생각했던 것보다 상심이 크신가 보네. 내 그 기분 충분히 이해합니다.”

“이해?”

석고준의 눈동자가 한층 붉어졌다. 지금 그가 어떤 심정인지, 누구도 이해할 수 없을 것이다.

그런데 너구리 같은 늙은이가 감히 웃으며 저딴 말을 지껄이다니.

까득.

말아쥔 주먹에서 뼈 어긋나는 소리가 들렸다.

한때는 말수가 적고 감정 표현이 드물어 석상 같았던 그는, 누구보다 존경하고 따랐던 이정룡의 죽음으로 인해 확연히 다른 사람이 되어 있었다.

“크흠.”

그 사실을 눈치채지 못할 장 총리가 아니다. 불안한 눈빛으로 석고준의 주먹을 바라본 그가 엉거주춤 자리에 앉았다.

“내가 실언을 한 모양이군. 마음 상했다면 사과하리다.”

“……됐습니다. 저도 감정이 격해져 흥분한 모습을 보였군요.”

석고준은 끓어오르는 분노를 애써 진정시켰다.

그는 더 이상 잃을 것도 없던 삼십여 년 전의 고아가 아니었다. 스승에게 물려받은 것을 지켜야 할 사명이 있었고, 이를 위해서는 해결해야 할 일이 산더미였다.

“그런데, 설마 총리님 혼자 오신 겁니까?”

드디어 올 게 왔다. 불쑥 흘러나온 석고준의 물음에, 장 총리는 애써 담담하게 대답했다.

“그렇소만.”

“그럼 대통령께서는?”

“어디 계신지는 이미 석고준 씨도 알 것 같은데.”

장 총리가 빈틈없이 막혀 있는 창밖을 힐끗 바라보았다.

비록 지금은 특수 처리 된 암막 커튼에 가려져 보이지 않지만, 저 커튼만 걷어내면 곧장 청와대가 보인다.

“각하께서는 지금 당장 처리하셔야 할 업무가 많아요. 세 시간 뒤, 정식으로 국가장(國家葬)이 시작되면 그때 오실 거요. 이미 비서실 측에서 전달한 것으로 아는데……?”

말꼬리를 흐리는 장 총리의 모습에, 석고준의 눈빛이 깊게 가라앉았다.

“그래서 한 번 더 여쭤본 겁니다. 제가 전달받은 사안이 믿기지 않아서.”

“뭐요?”

“장 총리님. 아니…….”

스윽.

소파에 기대고 있던 상반신이 장 총리를 향해 기울었다.

석고준의 붉은 눈동자에 늙은 정치인의 모습이 비치고, 오싹한 음성이 입술 사이로 흘러나왔다.

“장택환 씨.”

“……!”

“헛짓거리 그만하고 단도직입적으로 얘기합시다. 당장 돌아가서 대통령 독대 주선해요. 아직 국가장 절차 시작까지 세 시간 남았으니까, 앞으로 한 시간 드립니다.”

“이, 이봐요! 지금 어딜 감히…….”

“감히?”

파스슥.

장 총리의 눈이 부릅떠졌다. 단단한 크리스털 잔이 석고준의 손아귀에서 고운 가루가 되어 흘러내리고 있었다.

그와 함께 뒤바뀐 어투가 그의 귓가를 파고들었다.

“그래, 감히. 감히 당신이 이런 식으로 나오면 안 되지. 지금까지 걸어온 꽃길을 누가 깔아 줬는지 잊었나?”

“다, 당신…….”

늙은 정치인의 목소리가 떨렸다.

석고준의 말은 사실이었다. 그의 수십 년 정치 인생에서 아레스 길드라는 이름은 지울 수 없는 얼룩이다.

장 총리가 흘린 오물을 치우고, 밑을 닦아 주고, 차 트렁크에 무거운 상자를 실은 것이 바로 그들이니까.

하지만…….

“그, 그건 이정룡 부길드장이었소! 당신이 아니란 말이오!”

“맞아. 모두 부길드장님께서 하신 일이었지. 아니, 내 스승님께서.”

석고준의 입가에 건조한 웃음이 맺혔다.

“그리고 이제는 내가 할 일이 되었고.”

“……!”

“착각하지 마. 그분이 돌아가셨어도 아레스 길드는 아직 건재해.”

아레스 길드는 굳건한 철옹성이다.

인류를 구원한 불멸의 영웅이자 구세주인 천태민이 주춧돌을 세웠고, 이정룡은 누구도 넘보지 못할 철벽을 구축했다.

“여의도에, 이 나라에 우리 손이 안 닿는 곳은 없다.”

자본주의 법칙이 지배하는 세상이다.

매번 발표되는 포브스 잡지의 대기업 순위에는 세계 10대 길드 중 어느 곳도 포함되어있지 않지만, 모두가 알고 있다.

거대 길드가 가진 힘과 막대한 부를. 그중에서도 손꼽히는 아레스 길드의 영향력을.

그리고…… 그 힘은 죽은 자로부터 산 자에게 넘겨지게 될 것이다.

“내가 그분에게 물려받은 것이, 유지(遺志)뿐만이라고 생각하나?”

“뭐, 뭐요?”

장 총리의 눈이 커졌다. 국정원으로부터 전해 들은 정보에 의하면 이정룡의 유언장은 없었다. 아니, 없어야 했다.

멋모르는 국민들이야 이래저래 말이 많았지만, 그는 그 정보를 굳게 믿고 있었다.

“그, 그럼 당신이…….”

순간. 석고준의 눈동자가 붉게 빛났다.

“당신이 아니라, 부길드장님이라고 부르는 게 좋을 텐데.”

“……!”

늙은 정치인의 전신이 가늘게 떨렸다. 숨 막히는 침묵 끝에 장 총리가 힘없는 목소리로 입을 열었다.

“석고준 씨. 아니, 석 부길드장이 생각하는 것만큼 상황이 녹록지 않아요.”

석고준의 눈에 서려 있던 붉은 빛이 차츰 사그라들었다. 목소리는 여전히 건조했지만, 한결 부드러워진 어투가 뒤를 이었다.

“압니다. 그러니 우리 장 총리님께서 더 애쓰셔야죠. 다른 분들과 함께.”

“후우. 그게, 참. 쉽지 않습니다. 여러 가지 소문도 있고.”

“소문이라면…….”

“진태경 헌터. 아니, 그에 관하여 이야기하려는 것이 아니오. 물론 그와도 상당한 연관이 있지만.”

진태경이라는 세 글자에 즉각 반응하는 석고준에게 황급히 변명한 장 총리가 말을 이었다.

“석 부길드장도 이미 알고 있지 않습니까. 평화 길드의 그 젊은 팀장 말이오. 이름이 아마 최민우라던가.”

“……계속하십시오.”

“이정룡 전 부길드장께서 작고하신 이후로 주위에서도 이런저런 말들이 많아요. 아무리 뒤를 이을 사람이 있다고 해도…… 아레스 길드가 예전 같지 않은 것도 사실이고.”

이정룡은 그 자체로 상징적인 인물이었다.

천태민의 곁에서 대격변을 잠재운 영웅인 동시에 전 세계를 통틀어도 수위에 꼽히는 S급 헌터.

그가 죽었다고 해서 아레스 길드가 한순간에 붕괴하는 것은 아니지만, 길드의 전력과 영향력이 대폭 축소되는 것은 당연했다.

‘빌어먹을.’

석고준 역시 그 사실을 모르지 않았다. 아니, 누구보다 잘 알고 있었다.

당장 길드 내부 이곳저곳에서 들려오는 잡음과 반발이 바로 그 증거였고, 과거였다면 상상도 못 했을 태도를 취한 장 총리가 증인이었다.

‘스승님이었다면. 스승님이 살아 계셨다면…….’

석고준의 혀끝에서 맴도는 중얼거림은 입 밖으로 새어 나가지 않았다.

더 이상 흔들리는 모습을 보여서는 안 된다. 마음속으로 다짐한 그는 딱딱하게 굳은 얼굴로 입을 열었다.

“장 총리님께서는 걱정도, 시간도 많으신 모양입니다.”

“그게 무슨…….”

“아레스 길드 측에서 해결할 일입니다. 장 총리님께서는 해야 할 일을 하셔야죠.”

“아니, 그게 아니라.”

변명하려는 장 총리를 물끄러미 바라본 석고준이 소파에 등을 기댔다.

“오십 분 남았습니다.”

“오, 오십 분이라니. 무슨 뜻입니까?”

“아까 말씀드린 한 시간에서 십 분 지났으니, 오십 분. 이제 앉아 있을 시간이 없으실 것 같은데. 제 말이 틀립니까?”

“……!”

어떻게 해서든 국가장이 시작되기 전, 대통령과의 독대를 성사시키라는 뜻이 담긴, 명백한 축객령이다.

곧 후들거리는 다리로 일어나 돌아선 장 총리의 귓가에 나직한 목소리가 닿았다.

“한 가지 더. 그분…… 길드장님은 오시지 않습니다. 뒷말 나오지 않게 잘 단속하세요.”

더 이상 무슨 말을 할까.

힘없이 고개를 끄덕인 장 총리가 밀실을 빠져나갔다.

탁.

문 닫히는 소리가 유난히도 크게 울려 퍼졌다. 말없이 텅 빈 자리를 응시하던 석고준의 시선이 문득 자신의 왼팔을 향했다.

두 개의 검은 줄이 표시된 완장. 마땅한 혈육이 없는 이정룡을 위해 상주(喪主)가 된 그였다.

‘스승님. 그곳에서는 평안하십니까.’

부모의 얼굴도 기억하지 못하는데, 피 한 방울 섞이지 않은 이정룡의 얼굴은 사무치게 그립다.

아마 그는 평생토록 자신의 스승을 잊지 못할 것이다. 꼬리표처럼 따라붙는 두 사람의 이름도.

“……진태경. 최민우.”

스승을 죽인 자. 그리고 스승이 이룩한 모든 것을 빼앗으려는 자.

악문 잇새에서 흘러나온 목소리는 뜨거웠고, 눈동자는 어느 때보다 붉게 달아올랐다.

그리고 분노로 몸을 떨던 석고준은 문득 자신의 목을 더듬었다.

차륵.

손가락 끝에 닿은 차가운 금속의 촉감.

석고준은 군데군데 도금이 벗겨져 흉한 모습을 한 목걸이를 풀어 말없이 내려다보았다.

‘스승님.’

그도 안다. 이 목걸이는 이정룡이 아니며 이정룡이 남긴 유품도 아니라는 걸.

그러나 한 가지만은 확실했다.

한때 아크 리치의 본거지였던 폐허 속에서 운 좋게 형태를 유지한 것은 이게 유일했다.

비록 단순한 잡동사니에 불과하지만, 석고준으로서는 조사단장에게 거액의 뇌물을 주고 빼돌릴 만한 의미가 있는 물건이었다.

“……후우.”

깊은 한숨을 내쉰 석고준은 자리에서 일어났다.

그는 이 성대한 장례식의 상주다.

문밖에서 그를 기다리는 수많은 사람과 인사를 나누고, 세계 각지의 언론에 얼굴을 비춰 아레스 길드의 새로운 실세가 누구인지 알려 주어야 했다.

달칵.

문을 열자 복도에 나란히 도열한 수십여 명의 남녀가 고개를 숙였다.

한 사람, 한 사람이 A급 헌터라는 것을 증명하듯, 눈빛은 강렬했고 자그마한 동작에도 힘이 가득했다.

이들이 바로 석고준의 새로운 손발이다.

“가자.”

석고준의 나직한 목소리와 함께, 수십 개의 발걸음이 복도를 가로질렀다.



* * *



아레스 길드의 전(前) 부길드장. 이정룡의 국가장은 5일간 성대하게 치러졌다.

세계 각지의 언론과 거물들이 대한민국을 찾았고, 수십만에 달하는 국민들 역시 국가장이 진행되는 동안 거리에 나와 애도를 표했다.

그러나 모두가 그런 것은 아니었다. 당장 오늘이 배고픈 사람들에게는, 누군가의 죽음은 그리 크게 와닿지 않는 법이다.

촤악!

푸푸푸푹!

“죽여, 지금 찔러!”

“간격 유지! 야! 이 새끼야! 나가지 마!”

- 키에에에엑!

습하고 어두운 동굴 내부.

찢어지는 고성이 울려 퍼지고, 일부러 진흙을 발라 광택을 죽인 병장기는 쉴 새 없이 적의 숨통을 끊기 위해 움직인다.

쉬쉭, 푹!

“성하야!”

“야, 이 몬스터 새끼들아!”

- 키룩. 키리리릭!

헌터와 몬스터의 전투는 치열했고, 한편으로는 처절했다.

그리고 각기 다른 색을 지닌 두 종족의 핏물이 사방에서 솟구치던 바로 그 순간이었다.

구구구구궁!

지축이 흔들리고 동굴 천장의 종유석이 떨어진다.

동시에 어디선가 뿜어져 나온 강대한 마력(魔力)이 게이트 내부를 휩쓴 순간, 인간들은 비명을 내질렀다.

“변이 게이트!”

“이런 씨발……!”

하급 게이트에서 나올 수 있는 마력이 아니다. 최소 중급. 아니 상급. 어쩌면 그 이상일 수도 있었다.

‘이, 이건.’

‘끝이다.’

죽음. 그 단어와 함께 모두의 눈앞에 절망이 내려앉은 바로 그 순간이었다.

“시벌. 옛날 생각나네.”

누군가의 한숨 섞인 목소리가, 컴컴한 동굴 내부를 울렸다.
```

## Final English reading copy

```markdown
# Chapter 555

He was a man with the build of an iron tower. His expression was flat and hard as stone, and his lips were pressed tightly together.

And then… there were his eyes.

A pair of bloodshot eyes. An indescribable mixture of rage and grief, along with several other emotions. Just looking into those eyes sent a chill down the spine.

Even the Prime Minister of Korea—a permanent member of the UN Security Council and one of the world’s great powers—was no exception.

*What the hell is with that look…?*

The Prime Minister flinched at the gaze that pierced into him like a blade the moment he entered the room, then forced himself to calm his trembling heart.

His opponent was one of the most skilled Hunters in Korea, but the Prime Minister himself had spent decades rolling through the political mud and was now sixty.

There was no reason to be intimidated before the conversation had even begun.

*Especially not in a situation like this.*

Having recovered some of his composure, the Prime Minister extended his hand toward the man.

“Oh, there you are. Mr. Go Jun.”

Go Jun stared blankly at the hand held out to him and answered in a dry voice instead of shaking it.

“It’s been a while, Prime Minister Jang.”

It showed neither proper respect for someone considerably older nor the appropriate conduct toward his country’s prime minister. Deep wrinkles gathered across Prime Minister Jang’s forehead.

“…Ha. I suppose you’re more grief-stricken than I expected. I understand how you feel.”

“Understand?”

Go Jun’s eyes grew even redder. No one could understand what he was feeling now.

And yet this old raccoon of a man had the nerve to smile and say something like that.

*Crack.*

The bones in his clenched fist shifted with an audible snap.

Once taciturn and as expressionless as a statue, Go Jun had become an entirely different man after the death of Lee Jungryong, the person he had respected and followed more than anyone.

“Ahem.”

Prime Minister Jang was not so oblivious that he failed to notice. He glanced nervously at Go Jun’s fist before lowering himself awkwardly into a chair.

“I seem to have misspoken. If I offended you, I apologize.”

“…It’s fine. I let my emotions get the better of me as well.”

Go Jun forced down his boiling anger.

He was no longer the orphan from thirty-odd years ago who had nothing left to lose. He had a mission to protect what his Master had passed down to him, and there was a mountain of work he had to deal with in order to fulfill it.

“But did you really come alone, Prime Minister?”

At last, the moment had come. At Go Jun’s sudden question, Prime Minister Jang answered as calmly as he could.

“I did.”

“Then where is the President?”

“I imagine you already know where he is.”

Prime Minister Jang glanced toward the tightly covered window.

The specially treated blackout curtains hid the view for now, but if they were drawn back, the Blue House would be visible immediately.

“The President has a great deal of work to deal with right now. He’ll come when the national funeral officially begins in three hours. I believe the presidential office already conveyed that to you…?”

Prime Minister Jang let his sentence trail off. Go Jun’s eyes sank into a deeper stillness.

“That’s why I asked again. I couldn’t believe what I was told.”

“What?”

“Prime Minister Jang. No…”

*Swoosh.*

Go Jun leaned his upper body forward from where he had been resting against the sofa.

The old politician’s reflection appeared in his red eyes, and a chilling voice slipped between his lips.

“Mr. Jang Taekhwan.”

“……!”

“Stop screwing around and let’s speak frankly. Go back and arrange a private meeting with the President right now. There are still three hours before the national funeral proceedings begin, so I’ll give you one hour.”

“H-Hey! How dare you—”

“How dare I?”

*Crsh.*

Prime Minister Jang’s eyes flew open. The sturdy crystal glass in Go Jun’s hand was crumbling into fine powder and spilling between his fingers.

At the same time, the change in Go Jun’s tone cut into the Prime Minister’s ears.

“That’s right—how dare you. You don’t get to act like this. Have you forgotten who paved the easy road you’ve walked all these years?”

“Y-You…”

The old politician’s voice trembled.

Go Jun was telling the truth. The name Ares Guild was an indelible stain on the Prime Minister’s decades-long political career.

They were the ones who had cleaned up the filth Prime Minister Jang left behind, wiped his ass, and loaded heavy boxes into his car trunk.

But…

“That—that was Vice Guild Master Lee Jungryong! Not you!”

“That’s right. It was all the Vice Guild Master’s doing. No—my Master’s.”

A dry smile touched the corners of Go Jun’s mouth.

“And now it’s my job.”

“……!”

“Don’t get the wrong idea. Even though he has passed away, the Ares Guild is still standing.”

The Ares Guild was an impregnable fortress.

Cheon Taemin, the immortal hero and savior who had rescued humanity, had laid its cornerstone, and Lee Jungryong had built an iron wall that no one could challenge.

“There isn’t a place in Yeouido—or in this country—where our hands can’t reach.”

This was a world ruled by the laws of capitalism.

None of the ten largest Guilds in the world appeared on the corporate rankings published in Forbes magazine every year, but everyone knew.

They knew the power and immense wealth held by the great Guilds. And among them, they knew the influence of the Ares Guild, one of the greatest of all.

And now…

That power would pass from the dead to the living.

“Do you think all he left me was his dying wish?”

“W-What?”

Prime Minister Jang’s eyes widened. According to the information he had received from the NIS, Lee Jungryong had left no will.

No—he was supposed to have left no will.

The ignorant public had been talking about it endlessly, but the Prime Minister had firmly believed the information he had received.

“Then you…”

For an instant, Go Jun’s eyes glowed red.

“You should call me Vice Guild Master, not ‘you.’”

“……!”

The old politician’s entire body trembled faintly. After a suffocating silence, Prime Minister Jang spoke in a weak voice.

“Mr. Go Jun. No, Vice Guild Master Go. The situation isn’t as simple as you think.”

The red light in Go Jun’s eyes gradually faded. His voice remained dry, but his tone softened somewhat.

“I know. That’s why our Prime Minister Jang needs to try harder. Along with the others.”

“Whew. That’s… not easy. There are also a number of rumors.”

“Rumors?”

“Hunter Jin Taekyung. No—I’m not trying to talk about him. Of course, he is connected to this to a considerable degree.”

Prime Minister Jang hurriedly explained himself after seeing Go Jun react immediately to the name Jin Taekyung, then continued.

“You already know about the young Team Leader from the Peace Guild, don’t you? His name is Choi Minwoo, I believe.”

“…Go on.”

“Ever since the late Vice Guild Master Lee Jungryong passed away, people around us have been saying all sorts of things. Even if there is someone to succeed him, it’s true that the Ares Guild isn’t what it used to be.”

Lee Jungryong had been a symbolic figure all by himself.

He was a hero who had suppressed the Great Cataclysm at Cheon Taemin’s side, as well as an S-rank Hunter counted among the very best in the entire world.

The Ares Guild would not collapse in an instant simply because he had died, but it was only natural that its strength and influence would be greatly reduced.

*Damn it.*

Go Jun knew that better than anyone. No—he knew it better than anyone else.

The noise and resistance coming from various places inside the Guild were proof enough. So was the attitude Prime Minister Jang had dared to display—an attitude that would once have been unthinkable.

*If Master had been here. If Master were still alive…*

The mutter that hovered at the tip of Go Jun’s tongue never escaped his lips.

He could not show himself wavering any longer. Having made that resolution, he spoke with his face hardened like stone.

“Prime Minister Jang seems to have plenty of worries and plenty of time.”

“What does that—”

“That’s something the Ares Guild will handle. You should do what you need to do, Prime Minister.”

“No, that’s not what I—”

Go Jun stared silently at the Prime Minister trying to make excuses, then leaned back against the sofa.

“Fifty minutes.”

“F-Fifty minutes? What do you mean?”

“Ten minutes have passed since the one hour I mentioned earlier, so that leaves fifty minutes. It seems you no longer have time to sit around here. Am I wrong?”

“……!”

The meaning was clear: Prime Minister Jang was being ordered to arrange a private meeting with the President by any means necessary before the national funeral began.

Prime Minister Jang rose on trembling legs and turned toward the door. A quiet voice reached his ears.

“One more thing. That person… the Guild Master won’t be coming. Keep everyone in line so there’s no gossip.”

What more was there to say?

Prime Minister Jang nodded weakly and left the room.

*Click.*

The sound of the closing door echoed unusually loudly.

Go Jun stared silently at the empty space, then his gaze shifted toward his left arm.

A mourning band marked with two black stripes. With no suitable blood relative to serve in the role for Lee Jungryong, Go Jun had become the chief mourner.

*Master. Are you at peace there?*

Go Jun could not even remember his parents’ faces, yet he desperately missed the face of Lee Jungryong, who had not shared a drop of his blood.

He would probably never forget his Master for the rest of his life.

Nor would he forget the two names that clung to him like tags.

“…Jin Taekyung. Choi Minwoo.”

The man who had killed his Master.

And the man who intended to take everything his Master had built.

The voice that escaped through his clenched teeth was hot, and his eyes burned redder than ever.

Still trembling with rage, Go Jun suddenly reached up and touched his neck.

*Clink.*

His fingertips brushed against cold metal.

Go Jun unclasped the necklace and stared down at it in silence. Its plating had worn away in places, leaving it with an ugly, battered appearance.

*Master.*

He knew.

This necklace was not Lee Jungryong, nor was it a keepsake he had left behind.

But one thing was certain.

It was the only thing fortunate enough to have retained its shape amid the ruins that had once been the Arch Lich’s stronghold.

It was nothing more than a worthless trinket, but to Go Jun, it had been worth bribing the head of the investigation team with a fortune to smuggle it out.

“…Whew.”

Go Jun let out a deep sigh and rose from his seat.

He was the chief mourner at this grand funeral.

He had to greet the countless people waiting for him outside, appear before media outlets from around the world, and show them who the new power behind the Ares Guild was.

*Click.*

When he opened the door, dozens of men and women standing in formation along the hallway lowered their heads.

Their eyes were intense, and every small movement was filled with power, as though each one were proving that they were an A-rank Hunter.

These were Go Jun’s new hands and feet.

“Let’s go.”

At Go Jun’s quiet command, dozens of pairs of footsteps crossed the hallway.

* * *

The national funeral of Lee Jungryong, the former Vice Guild Master of the Ares Guild, was held on a grand scale for five days.

Media outlets and powerful figures from around the world traveled to Korea, while hundreds of thousands of citizens took to the streets to mourn throughout the funeral.

But not everyone mourned.

For people who were hungry today, someone else’s death was not something that touched them very deeply.

*Slash!*

*Stab-stab-stab!*

“Kill it! Stab it now!”

“Keep your distance! Hey, you bastard! Don’t rush out!”

—Kieeeek!

Inside a damp, dark cave, shrill cries rang out.

Weapons whose shine had been dulled by deliberately coating them in mud moved without pause, seeking to cut off the enemy’s breath.

*Whoosh—thud!*

“Seongha!”

“You monster bastards!”

—Kik. Kiririik!

The battle between the Hunters and the monsters was fierce—and, in its own way, desperate.

Then, just as the blood of the two species, each a different color, spurted in every direction—

*Rumble-rumble-rumble!*

The earth shook, and stalactites fell from the ceiling of the cave.

At the same time, powerful mana erupted from somewhere and swept through the Gate. The humans cried out.

“A Mutated Gate!”

“Fuck…”

This was not mana that could come from a low-level Gate.

At least mid-level.

No—high-level.

Maybe even higher.

*Th-This is…*

*It’s over.*

Just as despair descended before everyone’s eyes alongside the word *death*—

“Fuck. Brings back old memories.”

Someone’s sighing voice echoed through the pitch-black cave.
```

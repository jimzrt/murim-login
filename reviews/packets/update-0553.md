<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0553.txt",
      "sha256": "885780ea069dc56b1a5115d40dc19a62350343e265be6a558cfb1adfc83fab39",
      "bytes": 13589
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "d1ecf1b8b7580d8b070590663f2237a3f88510caeddd24615225febf32007474",
      "bytes": 3641
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "c46ce16d7ca86a3c8a8b7e84dabaa347bc812f25d3ee8ad6859c8ec31ecb4c16",
      "bytes": 175047
    },
    {
      "path": "characters/Cheon Taemin.md",
      "sha256": "15d606ac245d2f13d789485340189a7fa22133669bee3cf2dd674a87ca9fe207",
      "bytes": 590
    },
    {
      "path": "characters/Go Jun.md",
      "sha256": "42693a75606ea70c010380830f3bbb19869ebee37df8a409fa60222b636e480c",
      "bytes": 819
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "0275c712cbe4dd8e98039d339ad9cd5596d02e65e3516fd0c18112d93d640ca2",
      "bytes": 2292
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "19af901dabb4fd3718dd47e83aed4a245b917c2f738dca59028ed67ab18f709f",
      "bytes": 622
    },
    {
      "path": "characters/Kim Jeonghee.md",
      "sha256": "0b507e578589633870063977274546bc3b92e52deb53e6bb218d8e2382215419",
      "bytes": 747
    },
    {
      "path": "characters/Lee Jungryong.md",
      "sha256": "243040a379dbc439ac1d6dc4a75b14409e6ccea044381c731d534dc649ac23ae",
      "bytes": 1182
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "00c2449646751776d416393ccd2c6bce3fb3e056494cc5716f5763783e5bd006",
      "bytes": 166773
    }
  ],
  "estimated_tokens": 11688
}
-->

# Durable State Update — Chapter 553

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 553. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 553. Profile updates may replace only one
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
  "chapter": 553,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 553,
    "continuity_sources": [553],
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
    "The Fire Dragon Pavilion's first mission is to enter Nanman through the Journey to Nanman Quest, whose reward is a linked quest and whose failure penalty is the Title Can't Go to Nanman.",
    "The six-member Fire Dragon Pavilion party secretly departed Henan; Taekyung's carriage was to change horses and reunite with the other two members at Mount Daebyeol before leaving Henan.",
    "Jeok Cheongang remains in Henan and worries about Taekyung's departure, while Mae Jonghak trusts Taekyung to succeed.",
    "Cheongpung is accompanying Mungyeong and learning his martial arts through observation while remaining master of the Azure Dragon Pavilion and caretaker of Mimi.",
    "Mungyeong considers Nanman a plausible site for Dark Heaven's second rift, with a successful attack potentially spreading chaos through Yunnan, Guizhou, Guangxi, and Sichuan.",
    "The Mount Song Resolution restored the Murim Alliance; Mae Jonghak is Alliance Leader, Jeok Cheongang heads the Five Kings Hall, and Murong Yeonghwi oversees Murong Family defenses in Liaoning.",
    "Taekyung is a Supreme Peak master with Three Flowers Gather at the Crown, advanced Qi Sense, exceptional resistance to monster Fear, and public S-rank-level recognition while retaining an A-rank license; he leads the Fire Dragon Pavilion's first mission to Nanman.",
    "Mungyeong ended Taekyung's direct training and assigned him the final task of incorporating martial principles into his learned martial arts.",
    "Zhuge Feng's Demon-Sealing Formation still blocks mana from the exposed Gate, while Jang Taebo processes the Water God Dragon's remains.",
    "Dark Heaven remains an enormous monster-like threat capable of causing rifts and creating mutants; the mechanism behind Jang Sam's transformation remains unresolved.",
    "The Southern Heaven Demon Empress is believed to be moving toward the suspected next target, while Song Ho's dispatch there has received no reply for more than seven days.",
    "Taekyung has returned to the modern world on January 1, 2047, his twenty-eighth birthday, and the Skeleton King is using a human form created by Magic Johnson's illusion magic."
  ],
  "continuity_sources": [
    552,
    551
  ],
  "open_questions": [
    "What is the Lord of Heaven's identity, how is he connected to the dangerous force Taekyung associates with his original world, and how can Dark Heaven open Gates?",
    "What will Taekyung's party find in Nanman, and what does the Southern Heaven Demon Empress intend there?",
    "What is the outcome of the duel between Jeok Cheongang and Nangong Cheon, the Azure Sky Sword King?",
    "Why did Ju Hwaran and Sama Pyo's political engagement end?",
    "What process created Jang Sam's mutant form, and can Dark Heaven's mutants absorb human energy?"
  ],
  "safe_through": 552,
  "temporary_decisions": [
    "Render 건량 as dry rations, 광서 as Guangxi, 대별산 as Mount Daebyeol, 만리행 as Ten-Thousand-Li Journey, and 고잉메리호 as Going Merry.",
    "Render 반 시진 as half a shichen and retain Nanman, Nanman Beast Palace, Fire Dragon Pavilion, Great Hero, and Young Lady Ju.",
    "Render 남만행 as Journey to Nanman and 남만을 못 가 as Can't Go to Nanman.",
    "Render 면구 as disguise mask, 역용술 as disguise technique, 각주님 as Pavilion Master, 로그아웃 as Logout, and 동기화 as Synchronization.",
    "Preserve Taekyung's blunt profanity and toilet humor, Mae Jonghak's dry banter, Mungyeong's dry threatening voice, Hayeon's profane sibling banter, and the Skeleton King's archaic diction."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 천태민    | **Cheon Taemin**  |
| 이정룡    | **Lee Jungryong** |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 사숙     | **Martial Uncle**                            |
| 상태               | **Status**                     |
| 레벨               | **Level**                      |
| 명성               | **Fame**                       |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 길드      | **Guild**             |
| 길드장     | **Guild Master**      |
| 부길드장    | **Vice Guild Master** |
| 팀장      | **Team Leader**       |
| 마정석     | **Magic Gem**         |
| 고준 | **Go Jun** | Personal name of Team Leader Seok; Lee Jungryong's prized Disciple. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 김정희 | **Kim Jeonghee** | Jin Taekyung and Hayeon's mother; restaurant kitchen worker |
| 하연 | **Hayeon** | Jin Taekyung’s younger sister |
| 아스모데우스 | **Asmodeus** | Demon King referenced in Taekyung's sarcastic comparison; does not appear directly. |
| 화염신장 | **Flame Divine Palm** | Jopil's deadly palm technique, noted when Taekyung compares Jopil with Mukyung. |
| 천무지체 | **Heavenly Martial Physique** | Named physique or constitution mentioned hypothetically by Jin Mukyung. |
| 대한민국 | **Korea** | Country reference. |
| 아레스 | **Ares Guild** | The leading Guild in Korea; formerly employed Team Leader Choi and Song Song. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 국밥 | **gukbap** | Korean dish of rice served in hot soup; footnoted in the reading copy. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 준이 | **Jun** | Family nickname used in the form Jun's dad. |
| 석고준 | **Go Jun** | Source full-name form for the established Go Jun, also known as Team Leader Seok. |
| 마왕 | **Demon King** | The being Cheon Taemin killed. |
| 도련님 | **Young Master** | Address used for Team Leader Choi by Butler Kim. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 경호팀장 | **Head of Security** | Go Jun's security-team office under Lee Jungryong. |
| 존슨 | **Johnson** | Co-host of the American talk show that replays Taekyung's viral interview. |
| 미국 | **United States** | Country associated with the talk show and CNM. |
| 중국 | **China** | Country from which Team Leader Choi’s video originates. |
| 쓰촨성 | **Sichuan Province** | Source spelling variant of the established Sichuan location. |
| 여사 | **Lady** | Taekyung's joking sobriquet for Kim Jeonghee. |
| 쓰촨 | **Sichuan** | Variant spelling used for the region associated with the pattern Jin recognizes. |
| 텔레포트 | **Teleport** | Taekyung's label for the Blood Lord's unexplained disappearance. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 비도 | **throwing blade** | Mungyeong throws one past Taekyung's neck. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 하연 | 진태경 | younger_sister_to_older_brother | oppa | casual-familiar; pleading for important requests | Hayeon habitually puts 오빠 first when making an important request. |
| 진태경 | 김정희 | son_to_mother | Mom | casual-familiar and affectionate | Taekyung's first words after entering the restaurant and seeing his mother. |
| 김정희 | 진태경 | mother_to_son | Son | affectionate-familiar | Calls Taekyung 아들 when surprised by his visit and later asks whether he has eaten. |
| 진태경 | 하연 | older_brother_to_younger_sister | Sis | casual-familiar | Taekyung addresses Hayeon as 동생아 during their fly investigation. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 하연 | 김정희 | daughter_to_mother | Mom | casual-familiar | Hayeon calls 엄마 while reporting that Taekyung hit her. |
| 이정룡 | 진태경 | senior S-rank Hunter to younger Hunter and adversary | Young man | polished, teasing, and veiled-threatening | Uses a genial tone and indirect threats while trying to make Taekyung release the captives. |
| 진태경 | 이정룡 | younger Hunter to senior S-rank Hunter and adversary | you | polite but mocking and defiant | Taekyung answers Lee's soft threats with the wolf-and-tiger metaphor and refuses to yield. |
| 이정룡 | 고준 | Master to Disciple | Go Jun | familiar and testing | Lee switches from Seok's office title to his personal name while considering whether he can defeat Taekyung. |
| 고준 | 이정룡 | Disciple to Master | Master | deferential | Go Jun responds to Lee's personal-name address as 스승님. |
| 이정룡 | 천태민 | younger_to_older_brother_by_choice | older brother | reverent and familiar; internal | Lee Jungryong uses 형님 in unspoken thoughts and regards Cheon Taemin as an older brother despite having no blood relation. |
| 진태경 | 석고준 | returning Hunter to hostile Ares security leader | you fucking bastard | hostile and profane | Taekyung directs his final insults and challenge at Go Jun after returning alive. |
| 석고준 | 진태경 | hostile_opponents | brat | hostile and overconfident | Go Jun addresses Taekyung internally as 애송아 while launching his full-strength attack. |
| 진태경 | 엄마 | son_to_mother | Mom | casual and startled | Jin cries out to his mother as she charges at him during the hospital visit. |
| 진태경 | 존슨 | Allied Hunter to Grand Mage | Johnson | polite and familiar | Jin repeatedly addresses Magic Johnson directly while requesting explanations and permission to visit the site. |
| 고준 | 진태경 | Ares Guild combatant confronting the killer of his Master | you | hostile and informal | Go Jun uses 너 while demanding Jin confess to Lee Jungryong's death and threatening retaliation. |
| 진태경 | 고준 | dominant adversary confronting Lee Jungryong's Disciple | you | contemptuous and informal | Jin uses 너 and 놈 while overpowering Go Jun and ordering him to end the conflict with Lee Jungryong. |
| 엄마 | 진태경 | mother_to_son | my son | warm and affectionate | Taekyung's mother praises him during the public welcome. |

## Listed compact profiles

### Cheon Taemin.md

# Cheon Taemin (천태민)

- **Safe through:** Chapter 432
- **Aliases:** Slayer
- **Role:** Ares Guild Master; humanity's great hero and the world's greatest Hunter; killed the Demon King and is known as the Slayer; created the first Mana Cultivation Method during the Great Cataclysm.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** Maternal grandfather of Team Leader Choi and father of Soyeong; regarded by Lee Jungryong as an older brother despite their lack of blood relation.

### Go Jun.md

# Go Jun (고준)

- **Safe through:** Chapter 441
- **Aliases:** Team Leader Seok
- **Role:** Go Jun is the leader of Lee Jungryong's security team, an Ares Guild combatant, Lee's disciple and right-hand man, and the expected successor to Ares Guild leadership after Lee's death.
- **Personality:** Highly disciplined, fiercely loyal to Lee Jungryong, confident in his abilities, and capable of suppressing his anger and killing intent under provocation.
- **Voice:** Dry, controlled, and formal with subordinates; deferential when addressing his Master.
- **Relationships:** Disciple and direct protégé of the late Lee Jungryong, Go Jun confronted Jin Taekyung over Lee's death and was forced to accept Jin's demand that the conflict end with Lee.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 552
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, a Supreme Peak master who possesses the Heavenly Martial Physique and superhuman physical strength, has manifested Force, opened his Middle Dantian, crossed the wall into true mastery, has achieved Three Flowers Gather at the Crown but not Five Qi Returning to Origin, can perceive the texture of qi well enough to sever layered magic, can resist high-level monster Fear through exceptional mental strength, is publicly recognized as an S-rank-level Hunter while formally retaining an A-rank license pending testing, can command coordinated raids against powerful monsters, and now serves as one of the two pavilion masters of the Alliance Leader's direct Fire Dragon Pavilion while holding its unique Title, Fire Dragon Pavilion Master and leading its first mission to Nanman.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor and assigned him a final task to incorporate martial principles into his learned martial arts but declined Taekyung's recruitment after Cheongpung reached him first, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate, student, and trusted manager of media and official arrangements, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, and Xiao Shen regards him as an older brother after Jin saved him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 552
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Kim Jeonghee.md

# Kim Jeonghee (김정희)

- **Safe through:** Chapter 552
- **Aliases:** Hayeon's mom, Taekyung's mom, Ajumma
- **Role:** Fifty-year-old mother of Jin Taekyung and Hayeon; after defending Taekyung from the restaurant owner, she quits her restaurant kitchen job and leaves with him.
- **Personality:** Usually quiet, gentle, patient, and family-protective; becomes fierce when Taekyung or her family is insulted.
- **Voice:** Normally deferential and apologetic at work; calm and direct when defending her family, with sudden profanity under extreme provocation.
- **Relationships:** Widow and mother of Jin Taekyung and Hayeon; her deceased husband lovingly called her Jeonghee.

### Lee Jungryong.md

# Lee Jungryong (이정룡)

- **Safe through:** Chapter 442
- **Aliases:** None
- **Role:** Former Vice Guild Master of Ares Guild, one of Korea's two S-rank Hunters, and a Supreme Peak-level martial artist who was killed by Jin Taekyung.
- **Personality:** Outwardly genial, calm, and humorous; calculating, opportunistic, manipulative, coercive, and ruthless when challenged
- **Voice:** Smooth, good-natured, and indirect, using teasing conversation and veiled threats before becoming openly furious
- **Relationships:** Master of Park Jihoon and Go Jun (Team Leader Seok), whom he personally selected and trained; longtime Great Cataclysm acquaintance of Park Tae Seop; adversary of Jin Taekyung; knew Team Leader Choi from childhood; has an antagonistic history with Kim Hwajong, who saved his life at the collapse of Mapo Bridge eighteen years earlier; was visibly shaken by learning that Choi is Cheon Taemin's maternal grandson; regards Cheon Taemin as an older brother despite no blood relation and has long held him in respect and fear; operates as Ares Guild's senior authority beneath its Guild Master

## Korean source

```text
＃553화



내가 아무리 레벨 업을 하고 능력치를 올려도 달라지지 않는 한 가지 사실이 있다면, 그건 바로 한 사람에게만큼은 여전히 철부지 어린 아들이라는 것이다.

그리고…… 우리 어머니, 친애하는 김정희 여사의 손은 모든 방어력을 무시하는 공격력을 지니고 있었다.

“뭐 하니, 너희?”

꽉 움켜쥔 주먹. 다른 한 손에는 국자. 사태가 심상치 않음을 느낀 나는 재빨리 입을 열었다.

“여사님. 깜빡하신 것 같은데, 이 아들이 오늘 생일입니다.”

“그래서?”

“곧 서른이라는 뜻이죠. 남들 앞에서 손찌검은 좀 그렇지 않을까요?”

“난 내일모레면 환갑이란다.”

“앗, 아아…….”

번지수를 잘못 짚었다.

마음 깊이 실책을 인정한 나는 대화의 방향을 틀었다.

“두 달, 아니 얼마 전에는 몬스터와도 악전고투를 치렀습니다.”

“무사히 돌아와서 천만다행이구나, 아들.”

“감사합니다, 어머니.”

“그런데 왜 몬스터도 아니고, 여덟 살이나 차이 나는 여동생이랑 그렇게 싸워 대니?”

“어머니. 전 사람과는 싸우지 않습니다. 고로 저것은 제 여동생이 아니라 몬스터입니다.”

“그럼 내가 몬스터를 낳았다는 뜻이구나.”

“……!”

“손바닥, 국자. 뭐가 더 낫겠니?”

외통수다. 더는 피할 길이 없음을 깨달은 나는 지그시 눈을 감으며 대답했다.

“손바닥이요.”

“팔뚝? 등?”

“등으로 하겠습니다.”

심사숙고한 끝에 나온 대답에, 즉각적인 응징이 이어졌다.

“엄마가!”

짝!

“싸우지!”

짜악!

“말랬지!”

짜아악!

“꺅!”

“으헉!”

세상에, 화염신장인가.

등짝을 파고드는 격통에 나와 하연이는 비명을 질렀다.

무림에서는 천무지체(天武地體)라고까지 불리는 완벽한 신체도 지금만큼은 아무 소용 없었다. 이건 영혼에 각인 된 두려움이요, 고통이다.

‘피할 수도 없고.’

피했다가는 괘씸죄가 적용되어 열 배 이벤트가 터질 것이 뻔하다.

결국 나와 하연이는 등에 엄마손 인증마크를 찍은 후에야 풀려날 수 있었고, 가쁜 숨을 내쉬며 돌아서는 김정희 여사를 바라보는 최 팀장과 스켈레톤 킹의 동공에서는 지진이 일어났다.

“어, 어머님. 전 말리려고 했습니다.”

“아, 아임 아메리칸. 미합중국 시민. 돈 터치. 플리즈.”

살겠다고 아등바등 애쓰는 모습이 애잔하기까지 하다.

물론 김정희 여사께서는 언제 그랬냐는 듯 자애로운 미소를 지어 보였다.

“호호, 우리 애들이 좀 말썽이었죠. 미안해요. 아직 둘 다 철이 없어서. 아침 만드는 중이니까 같이 들어요.”

“가, 감사합니다.”

“땡큐. 땡큐 정희.”

뭐, 시벌놈아?

다른 건 몰라도 땡큐 정희는 뒤졌다.

스켈레톤 킹을 향해 눈빛으로 살인 예고를 날린 나는 식당으로 향했다.

으리으리한 대저택답게 식당까지의 거리는 상당했지만, 저택 내부에 설치되어 있는 엘리베이터와 단거리 텔레포트(Teleport) 마법진을 사용하면 금방이었다.

“……?”

아니, 생각해 보니까 어이가 없네. 어떻게 저택 내부에 텔레포트 마법진이 있냐.

황당하다는 눈빛으로 최 팀장을 바라보니 그가 덤덤한 표정으로 대답한다.

“워낙 저택이 넓어서요. 이동 시간을 줄이기 위해 설치해 둔 것으로 압니다.”

“……텔레포트 마법진이 보통 그런 용도죠. 당연히.”

밥을 먹는 것은 배를 채우기 위해서입니다. 그런 뻔한 말과 뭐가 다른지 모르겠다.

아니, 어쩌면 최 팀장에게는 이 모든 것이 당연하게 느껴질 만도 하다는 생각도 들었다.

‘아무래도 소시민 집안과는 거리가 한참 멀지.’

대한민국의 재벌 3세도, 검술 명가 막내아들도 최 팀장에게는 몇 수 접어 줘야 한다.

그의 외조부는 최후의 전투에서 마왕 아스모데우스를 쓰러트리고 인류를 구원한 불멸의 영웅이니까.

‘천태민.’

과거 어느 선지자의 탄생이 기원(紀元)을 전, 후로 나누었다면, 천태민은 인류의 운명을 결정지었다.

그의 모습을 수천만 명이 보았고 수억 명이 기억한다.

그의 존재를 증명하는 방대한 분량의 자료는 무수한 세월이 흐르고 인류가 멸망을 맞이할 그 날까지 남아 있을 것이었다.

‘그리고 바로 그 천태민이 한때나마 이 저택에 살았었단 말이지.’

지금은 외손자인 최 팀장조차 그의 행방과 생사여부를 모르지만, 그런 것을 떠나 새삼 감동적이었다.

비록 극성인 주변 언론 탓에 잠시 임시 세입자로 신세를 지고 있긴 해도, 천태민이라는 불멸의 영웅과 같은 공간을 공유한다는 기분이 들어서다.

‘끝내준다.’

그토록 값지다는 A급 마정석을 건전지처럼 박아넣어 끊임없이 에너지를 공급하는 저택 내부를 바라보던 나는 크게 숨을 들이켰다.

“후웁.”

그런 내 모습에 최 팀장이 떨떠름한 표정을 지었다.

“……뭐 하십니까?”

“기운을 받는다고 해야 하나. 영웅의 체취를 느낀다고 해야 하나.”

하연이가 쓰라린 등을 쓰다듬으며 중얼거렸다.

“그냥 변태 새끼예요. 후각 페티쉬가 있거든요.”

“건방진 인간 계집은 조용히 해 줄래?”

“그래? 엄…… 읍!”

“오늘 밤 피살되기 싫으면 입 다물고 있어.”

나도 이제 내일모레면 서른인데, 다른 사람 앞에서 더 이상 맞는 모습을 보여 주긴 싫다.

그리고 다행히도 이상함을 느낀 김정희 여사가 뒤를 돌아보기 직전, 한 사람이 나타났다.

“좋은 아침입니다.”

원두커피 CF가 자동 재생되는 부드러운 중저음의 목소리. 아직 이른 아침임에도 불구하고 칼같이 정리된 포마드 헤어와 깔끔하면서도 중후한 맞춤 정장.

빠르지도 느리지도 않은 걸음으로 다가온 김 집사가 가장 먼저 최 팀장을 향해 고개를 숙여 보였다.

“편안한 밤 되셨습니까, 도련님.”

최 팀장이 익숙하게 고개를 끄덕였다.

“네. 처리해야 할 일이 몇 가지 있어서 좀 늦게 잠자리에 들긴 했지만, 상태는 나쁘지 않습니다.”

“미스터 존슨 측에서 온 제안 때문이군요.”

“위저드(Wizard) 길드와 체결한 협약 중에 조정해야 할 부분이 생겨서 말입니다. 사안은 정리해 두었으니…….”

두 사람이 주고받는 대화를 듣고 있던 하연이가 중얼거렸다.

“드라마의 한 장면이야, 뭐야.”

“드라마는 아니고, 굳이 따지자면 웹소설 아닐까.”

웹툰이라면 모를까. 이런 판타지를 드라마로 만들면 제작비 왕창 깨지겠지.

“그냥 넘어가. 어차피 보다 보면 익숙해져.”

“저게?”

“……익숙해지려고 노력 정도는 해 봐.”

사실 아직도 매번 낯설어서 미칠 지경이다.

따지고 보면 나는 현대 시간으로 불과 반년 전까지는 순대국밥에 컵라면으로 끼니를 때우던 F급 헌터다.

그랬던 나를 언론에서는 최태민의 뒤를 잇는 새로운 영웅으로 추켜세우고, 미처 바꾸지 못한 낡은 가죽 지갑에는 최상급 마정석을 특수 가공한 S급 헌터 자격증이 꽂혀 있다.

‘슬슬 익숙해질 만도 한데, 은근히 잘 안 되네.’

그 이유는 내가 해야 할 일이 많이 남아서인지도 모른다.

당장 현대와 무림. 두 세상을 바쁘게 오가며 쉴 새 없이 터지는 사건을 해결하는 것도 벅찬 상황.

어쩌면 내게 주어진 부와 명성을 온전히 누리며 익숙해지는 것이 더 이상한 거겠지.

“더 자세한 사안은 식사 후 다시 이야기하는 게 좋겠습니다. 도련님.”

“아, 그러시죠.”

때마침 짧은 대화를 끝낸 최 팀장과 김 집사를 따라 걸음을 옮긴 곳은 식당이었다.

아니, 식당보다는 차라리 연회장이라고 부르는 것이 어울리겠다.

그곳은 그만큼 넓었고, 정갈하면서도 우아했으며 뛰어난 AI 기능이 탑재된 로봇들이 각자의 위치에서 우리를 기다리고 있었다.

그리고 모든 것이 철두철미하게 준비된 이 공간에서, 유일하게 준비되지 않은 것이 있었다.

“음.”

“역시.”

나와 하연이를 제외한 모두가 눈을 깜빡였다. 특히 스켈레톤 킹의 속삭임에는 순수한 의구심이 가득했다.

“간악한 인간이여. 하나만 물어봐도 되겠나.”

“말해.”

“무엇이냐. 분명 식사를 하라고 들었거늘, 왜 식탁 위에는 아무것도 없는 것이냐.”

스켈레톤 킹의 말은 사실이었다. 연회장 중앙에 자리한 커다란 테이블은 텅 비어 있었다. 식기도, 음식도 준비되지 않은 완벽한 백지상태.

내심 짐작하고 있던 나는 조용히 고개를 끄덕였다.

“원래 이런 거야.”

“뭐라고?”

“절대적인 규칙. 아니면 종족적인 습성. 뭐 그런 비슷한 거지.”

엄마가 밥 먹으라고 부르는 건 한창 준비 중이라는 뜻이다.

밥 차려 놨으니까 당장 나오라고 한 번을 외치든, 열 번을 외치든 나가 보면 결과는 똑같다.

그 사실을 잘 알고 있는 하연이는 벌써 식기부터 찾는 중이다.

“죄송한데. 여기 수저 어딨어요?”

“네?”

“수저요. 숟가락이랑 젓가락.”

말없이 눈을 깜빡인 최 팀장의 시선이 슬그머니 한 사람을 향해 옮겨졌다.

“김 집사님?”

순간 칼같이 정돈된 김 집사의 포마드에서 잔털 한 가닥이 삐쭉 튀어나왔다.

“전부 로봇 회로에 적용된 부분이기 때문에, 전부 알아서 가져다주…… 그런데 왜 로봇이 안 움직이죠?”

그때, 국이 끓는다며 일찌감치 국자를 들고 주방으로 달려간 김정희 여사가 고개를 빼꼼 내밀었다.

“어머, 그거 전원 꺼 놨는데.”

“예?”

“네?”

“안 그래도 신세 지게 되어서 죄송한데, 괜히 전기세 낭비하는 것 같아서요. 애들 시키면 금방 하니까 자리에 앉아 계세요.”

“…….”

“…….”

어차피 저택의 모든 로봇들이 전기가 아니라 내장된 마정석으로 작동한다는 것도, 전기비 따위 아낄 필요 없다는 것도 김정희 여사의 귀에는 들리지 않을 것이 뻔하다.

상대는 평생 허리띠를 졸라매고 억척스럽게 두 남매를 키운 프로 주부다.

할 말을 잃은 채 나를 응시하는 사람들의 시선에, 나는 입맛만 다셨다.

“그냥 그러려니 하시면 됩니다. 저도 한두 번 말해 본 게 아닌데, 안 통하더라고요.”

지금껏 보내 주었던 생활비도 이 돈을 어떻게 쓰냐며, 차곡차곡 모아 두었던 어머니다.

식당에서 일하시던 옛 모습을 떠올리며 씁쓸하게 웃은 나는 스켈레톤 킹의 뒤통수를 후려쳤다.

빡!

“아니, 왜……?”

“뭐 해, 새꺄. 가서 도와.”

“간악한 인간이여. 이건 부당하다. 미국식도 아니다!”

“그럼 미국 가든가. 당장 입국하자마자 몬스터인거 들키고 옥타곤으로 끌려가겠지만.”

최 팀장이 아연한 눈빛으로 나를 응시했다.

“펜타곤입니다, 진태경 씨…….”

“옥타곤이나 펜타곤이나. 됐고, 최 팀장님이랑 김 집사님도 가서 도우세요.”

“예?”

“함께 먹는 식사잖아요. 다 같이 준비해야죠.”

순간, 최 팀장의 눈빛이 흔들렸다.

“함께 먹는…… 식사?”

“제대로 들으셨네. 그럼 얼른 가서 식기부터 놓으세요. 여기서 잘 하나 안 하나 감시하고 있을 겁니다.”

잠시 흔들렸던 최 팀장의 눈빛이 또렷해졌다.

“감시요?”

“네.”

“그럼 진태경 씨는? 아무것도 안 합니까?”

“전 오늘 생일입니다. 헌터 훈련소에서도 생일인 사람은 자유 시간 줬어요.”

“…….”

“뭐 해요. 미역국 나오기 전에 준비해야지.”

부모님이 돌아가시고, 외조부인 천태민마저 잠적한 이후 이정룡에 의해 철저히 배제되었다고는 해도 귀한 집 도련님은 도련님.

그런 최 팀장으로서는 평생 겪어 보지 못한 일이었을 거다.

지금껏 보지 못한 어벙한 얼굴로 김 집사와 함께 멀어지는 그의 뒷모습을 보며 피식 웃은 나는 자리에 앉아 스마트폰을 꺼냈다.

‘상황을 파악하는 데에는 뉴스만 한 게 없지.’

톡. 톡톡.

몇 번의 터치 후, 헌터들만 가입할 수 있는 대형 커뮤니티에 접속한 나는 불과 10분 전 올라온 기사를 확인하고 문득 손을 멈췄다.



[前아레스 부길드장 이정룡(68세). 내일 국장(國葬) 치러질 예정.]

[불멸의 영웅, 천태민은 어디에?]

[세계의 관심 속에, 쓰촨성에 남아 있던 아레스 길드원 출국. 故이정룡 씨의 경호팀장이었던 석고준 헌터에게 쏟아지는 세계 각지의 관심……]



“석고준이라.”

그래, 이놈이 있었지.
```

## Final English reading copy

```markdown
# Chapter 553

No matter how much I leveled up or increased my stats, there was one fact that never changed.

To one person, I was still nothing more than an immature little son.

And… my mother, dear Lady Kim Jeonghee, possessed enough attack power to ignore every defense.

“What are you doing, you two?”

One hand was clenched into a tight fist. In the other, she held a ladle.

Sensing that things were getting serious, I hurriedly opened my mouth.

“Lady Kim. I think you’ve forgotten, but this son of yours has a birthday today.”

“So?”

“It means I’m practically thirty. Wouldn’t hitting me in front of other people be a little embarrassing?”

“I’m pushing sixty myself.”

“Ah. Oh…”

I had picked the wrong target.

Deeply acknowledging my mistake, I changed the direction of the conversation.

“Two months—no, not that long ago, I was fighting monsters for my life.”

“Thank goodness you came back safely, son.”

“Thank you, Mother.”

“Then why do you keep fighting with your little sister, who’s eight years younger than you, instead of a monster?”

“Mother. I don’t fight people. Therefore, that thing isn’t my little sister. It’s a monster.”

“Then you’re saying I gave birth to a monster.”

“...!”

“My palm or my ladle—which would you prefer?”

I was cornered. Realizing there was no escape, I closed my eyes and answered quietly.

“My palm.”

“Forearm? Back?”

“I’ll take the back.”

The answer came after careful consideration.

The punishment followed immediately.

“Mom told you—”

*Smack!*

“Not to fight!”

*Smack!*

“Didn’t I?”

*Smack!*

“Eek!”

“Ugh!”

Good heavens. Was this the Flame Divine Palm?

Pain bored into my back, and Hayeon and I screamed.

Even a perfect body known throughout Murim as the Heavenly Martial Physique was useless now.

This was fear and pain engraved directly into the soul.

*I can’t dodge, either.*

If I did, she would apply the crime of insolence and trigger a tenfold event.

In the end, Hayeon and I were released only after receiving Kim Jeonghee’s handprint stamps across our backs.

As Lady Kim turned away, breathing heavily, Team Leader Choi and the Skeleton King watched her with eyes that looked ready to shake out of their sockets.

“Y-Your mother. I was trying to stop them.”

“I am American. Citizen of the United States. Do not touch me. Please.”

Their desperate attempts to survive were almost pitiful.

Of course, Lady Kim gave them a benevolent smile as though nothing had happened.

“Oh-ho-ho. My children were being a little troublesome, weren’t they? I’m sorry. They’re both still immature. I’m making breakfast, so let’s eat together.”

“Th-Thank you.”

“Thank you. Thank you, Jeonghee.”

*What the hell, you son of a bitch?*

I didn’t care about anything else, but the “Thank you, Jeonghee” had earned the Skeleton King a death sentence.

I sent him a silent death threat with my eyes, then headed toward the dining room.

The mansion was enormous, so the distance to the dining room was considerable. But the elevator installed inside the house and the short-range Teleport magic circles made the journey quick.

“...?”

Wait. Now that I thought about it, this was ridiculous.

Why was there a Teleport magic circle inside a mansion?

I stared at Team Leader Choi in disbelief. He answered with a calm expression.

“The mansion is quite large. As I understand it, the circles were installed to reduce travel time.”

“...That’s what Teleport magic circles are normally used for. Of course.”

It was no different from saying, *People eat to fill their stomachs.*

Then again, perhaps all of this really did feel normal to Team Leader Choi.

*He’s a long way from coming from an ordinary family.*

Even a third-generation Korean chaebol heir or the youngest son of a famed swordsmanship family would have to defer to Team Leader Choi.

His maternal grandfather was the immortal hero who had defeated the Demon King Asmodeus in the final battle and saved humanity.

*Cheon Taemin.*

If the birth of some prophet had divided an era into before and after, Cheon Taemin had determined the fate of humanity.

Tens of millions had seen him, and hundreds of millions remembered him.

The vast amount of material proving his existence would remain until countless ages had passed—and until the day humanity met its end.

*And that very Cheon Taemin once lived in this mansion.*

Even Team Leader Choi, his maternal grandson, did not know where he was or whether he was alive. But putting that aside, the thought was moving in its own way.

Though the relentless press had left me imposing on them as a temporary guest, I felt as though I was sharing a space with the immortal hero Cheon Taemin.

*This is incredible.*

I looked around the mansion, where immensely valuable A-rank Magic Gems had been slotted in like batteries to provide a constant supply of energy, and drew in a deep breath.

“Fwoosh.”

Team Leader Choi gave me an uneasy look.

“...What are you doing?”

“Should I say I’m absorbing the energy? Or that I’m sensing the scent of a hero?”

Hayeon rubbed her sore back and muttered,

“He’s just a pervert. He has an olfactory fetish.”

“Would you be quiet, insolent human girl?”

“Really? Mom—mmph!”

“If you don’t want to be murdered tonight, keep your mouth shut.”

I was practically thirty myself. I didn’t want to be beaten in front of other people anymore.

Fortunately, just before Lady Kim, who had sensed something strange, turned around, someone appeared.

“Good morning.”

His smooth, low baritone sounded as though a coffee commercial had started playing automatically.

Even though it was still early in the morning, his slicked-back hair was impeccably styled, and his tailored suit was neat yet dignified.

Butler Kim approached at a measured pace—not too fast, not too slow—and first bowed toward Team Leader Choi.

“Did you sleep comfortably, Young Master?”

Team Leader Choi nodded with practiced ease.

“Yes. I went to bed a little late because there were a few things I had to take care of, but I’m feeling fine.”

“This is regarding the proposal from Mr. Johnson’s side, I presume.”

“There were a few points in the agreement with the Wizard Guild that needed to be adjusted. I’ve organized the matter, so…”

Hayeon, who had been listening to their exchange, muttered,

“Is this a scene from a drama or what?”

“Not a drama. If you want to be precise, probably a web novel.”

A webtoon, maybe. If they turned this kind of fantasy into a TV drama, the production budget would be obliterated.

“Just let it go. You’ll get used to it if you watch long enough.”

“That?”

“...At least try to get used to it.”

In truth, I still found it strange every single time.

Until barely six months ago by modern-world time, I had been an F-rank Hunter who got by on blood sausage gukbap[^1] and cup noodles.

Now the media was praising me as the new hero who would follow in Cheon Taemin’s footsteps, and an S-rank Hunter license made from specially processed top-grade Magic Gems was sitting inside the old leather wallet I still hadn’t gotten around to replacing.

*I should be getting used to this by now, but somehow it isn’t happening.*

Maybe it was because I still had so much left to do.

Just keeping up with the endless incidents erupting in the modern world and Murim while rushing back and forth between the two was already overwhelming.

Perhaps it would be stranger if I could calmly enjoy and grow accustomed to all the wealth and fame that had fallen into my hands.

“It would be best to discuss the details again after breakfast, Young Master.”

“Ah, yes. Let’s do that.”

The short conversation ended just as we reached the dining room with Team Leader Choi and Butler Kim.

No, calling it a dining room seemed inadequate. Banquet hall would have been more fitting.

It was that spacious, neat, and elegant. Robots equipped with advanced AI functions waited at their assigned positions.

And in this space, where everything had been prepared with absolute precision, there was only one thing that hadn’t been prepared.

“Hmm.”

“Just as I thought.”

Everyone except Hayeon and me blinked.

The Skeleton King’s whisper was filled with particularly genuine confusion.

“Wicked human. May I ask you one thing?”

“Go ahead.”

“I was told we were to dine. Why, then, is there nothing whatsoever upon the table?”

The Skeleton King was right.

The enormous table in the center of the banquet hall was completely empty. No dishes, no food—nothing but a perfect blank slate.

I had already guessed the reason, so I quietly nodded.

“That’s how it normally works.”

“What?”

“It’s an absolute rule. Or maybe a species-wide habit. Something along those lines.”

When Mom called us to eat, it meant she was still preparing the meal.

Whether she called once or ten times, saying that the food was ready and we should come out immediately, the result was always the same when we arrived.

Hayeon knew this well. She was already looking for the utensils.

“Sorry, but where are the utensils?”

“Pardon?”

“Utensils. Spoons and chopsticks.”

Team Leader Choi blinked silently, then slowly shifted his gaze toward someone else.

“Butler Kim?”

At that moment, a single stray hair stuck out from Butler Kim’s perfectly arranged pompadour.

“Those functions are all integrated into the robots’ circuits, so they should bring everything automatically… But why aren’t the robots moving?”

Just then, Lady Kim peeked her head out from the kitchen. She had rushed there earlier with a ladle in hand, saying that the soup was boiling.

“Oh, I turned them all off.”

“What?”

“Pardon?”

“I’m sorry to impose on you like this, but I felt as though I’d only be wasting electricity. The children can do it quickly, so please sit down.”

“...”

“...”

There was no way Lady Kim would hear that every robot in the mansion ran on embedded Magic Gems rather than electricity, or that there was no need to save money on the electric bill.

She was a professional housewife who had spent her entire life tightening her belt and raising two children through sheer determination.

As everyone stared at me, speechless, I merely smacked my lips.

“Just accept it. I’ve tried explaining it more than once or twice, but it never gets through.”

Even the living expenses I had sent her over the years had been carefully saved because she couldn’t bear to spend the money.

Thinking of her old days working in a restaurant kitchen, I smiled bitterly, then smacked the Skeleton King on the back of the head.

*Whack!*

“Why me…?”

“What are you doing, asshole? Go help.”

“Wicked human. This is unjust. It is not American either!”

“Then go to America. Though the moment you arrived, they’d realize you were a monster and drag you to the Octagon.”

Team Leader Choi stared at me in bewilderment.

“It’s the Pentagon, Mr. Jin Taekyung…”

“Octagon, Pentagon—what’s the difference? Anyway, you and Butler Kim should go help, too.”

“Pardon?”

“We’re eating together. Everyone should help prepare.”

Team Leader Choi’s eyes wavered.

“Eating… together?”

“You heard me correctly. Hurry up and set out the utensils. I’ll be watching to see whether you do it properly.”

His eyes, which had wavered for a moment, sharpened.

“Watching?”

“Yes.”

“Then what about you, Mr. Jin Taekyung? Are you going to do nothing?”

“It’s my birthday. Even at the Hunter training camp, people were given free time on their birthdays.”

“...”

“What are you waiting for? We need to get ready before the seaweed soup comes out.”

Even though his parents had died and his maternal grandfather, Cheon Taemin, had vanished, and even though Lee Jungryong had thoroughly excluded him afterward, Team Leader Choi was still a young master from a wealthy household.

This must have been something he had never experienced in his life.

I snickered as I watched him walk away with Butler Kim, wearing a dazed expression I had never seen before. Then I sat down and pulled out my smartphone.

*There’s nothing better than the news for figuring out what’s going on.*

*Tap. Tap-tap.*

After a few touches, I accessed one of the large communities restricted to Hunters.

Then I saw an article that had been posted only ten minutes earlier, and my hand suddenly stopped.

[Former Ares Vice Guild Master Lee Jungryong, 68. National funeral to be held tomorrow.]

[Where is the immortal hero Cheon Taemin?]

[Amid global attention, Ares Guild members who remained in Sichuan Province depart the country. Attention from around the world pours onto Hunter Go Jun, former head of security for the late Lee Jungryong…]

“Go Jun.”

Right. That guy was still around.

[^1]: Gukbap is a Korean dish of rice served in hot soup.
```

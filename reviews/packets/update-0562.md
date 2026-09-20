<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0562.txt",
      "sha256": "4792afd939cd4c2a2443ab74d828c1d51aa0fc4b9026f904e10e77666a69e997",
      "bytes": 13230
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "f998c9709e94e873cdf937d5b96246d4530faa239fa6282aa90adb193ceba88b",
      "bytes": 4806
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "d8e0a738f01c76cdc4c58e1964c91d6651a780b5bbd9a5e379462e9446934a2d",
      "bytes": 178154
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "297f90bfc7d39df9b882e2faae08ad6642a20d21c6460b0839aff309763b16b6",
      "bytes": 553
    },
    {
      "path": "characters/Go Jun.md",
      "sha256": "bdd522b70ebcce31ea97dbf62bf6aa1f9915302dbab039dc1f8929511322be9a",
      "bytes": 793
    },
    {
      "path": "characters/Human Butcher.md",
      "sha256": "8025a3065c4c963b46aae37ddbd5a0a0e68611a016e28d7f7bfb6c02518ac9c1",
      "bytes": 667
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "cb8abb481887f2fd93c973350ee0b7302313a9fe892d0abbdbf6a249ad493f34",
      "bytes": 2280
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "6a0e4d1e5c20eb40808821493ecc7be8c7e9b9dc83b3f48ea73aea32e2475ba6",
      "bytes": 622
    },
    {
      "path": "characters/Team Leader Choi.md",
      "sha256": "a4f8cf1011000b28899106bcd17bd2b81c5be112794f55f0ac11465c53f5a9e0",
      "bytes": 714
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "99496b429425d3cf3d9a6053dc853ab8ebeda57cf95825a6c13baaff75900706",
      "bytes": 172242
    }
  ],
  "estimated_tokens": 11777
}
-->

# Durable State Update — Chapter 562

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 562. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 562. Profile updates may replace only one
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
  "chapter": 562,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 562,
    "continuity_sources": [562],
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
    "Taekyung is in the modern world in early 2047, staying with Kim Jeonghee and Hayeon at Team Leader Choi's mansion, where Cheon Taemin once lived; he and the Skeleton King have entered the Yeokgok Mutated Gate to conduct a rescue.",
    "The public believes the Lich killed Lee Jungryong and Wu Heixing; Taekyung knows the actual deaths were caused by him, while Go Jun remains Ares Guild's Vice Guild Master and regards Taekyung and Choi Minwoo as enemies."
  ],
  "continuity_sources": [
    561,
    560
  ],
  "open_questions": [
    "What is the Lord of Heaven's identity, how is he connected to the dangerous force Taekyung associates with his original world, and how can Dark Heaven open Gates?",
    "What will Taekyung's party find in Nanman, and what does the Southern Heaven Demon Empress intend there?",
    "What is the outcome of the duel between Jeok Cheongang and Nangong Cheon, and why did Ju Hwaran and Sama Pyo's political engagement end?",
    "What process created Jang Sam's mutant form, whether Dark Heaven's mutants can absorb human energy, and whether it relates to the Mutated Gate?",
    "How many additional Gate disasters are being concealed, and what is driving the accelerating Mutated Gate and Monster Wave outbreaks in Korea and abroad?"
  ],
  "safe_through": 561,
  "temporary_decisions": [
    "Render 건량 as dry rations, 광서 as Guangxi, 대별산 as Mount Daebyeol, 만리행 as Ten-Thousand-Li Journey, and 고잉메리호 as Going Merry.",
    "Render 반 시진 as half a shichen and retain Nanman, Nanman Beast Palace, Fire Dragon Pavilion, Great Hero, and Young Lady Ju.",
    "Render 남만행 as Journey to Nanman, 남만을 못 가 as Can't Go to Nanman, 면구 as disguise mask, 역용술 as disguise technique, 각주님 as Pavilion Master, 로그아웃 as Logout, and 동기화 as Synchronization.",
    "Render 일기당천 as One Against a Thousand, 거인의 포효 as Giant's Roar, 타락한 엔트 as Corrupted Ent, 붉은 눈 as Red Eye, 치코리타 as Chikorita, 대마도사 as Grand Mage, 순간이동 as Teleportation, 텔레포트 as Teleport, 변이 게이트 as Mutated Gate, and 몬스터 웨이브 as Monster Wave.",
    "Render 모하비 사막 as Mojave Desert, 애리조나주 as Arizona, 대의 as greater cause, 순수혈통 as pureblood, 국부 as Founding Father, 위저드(Wizard) 길드 as Wizard Guild, 조셉 바이든 as Joseph Biden, 펠릭스 왕자 as Prince Felix, 곽한구 as Gwak Hangu, 역곡 as Yeokgok, and 오크의 황무지 as Orc Wasteland."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 최민우    | **Choi Minwoo**   |
| 일격     | **One Strike**                         |
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
| 도사      | **Daoist**                                                      |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 고준 | **Go Jun** | Personal name of Team Leader Seok; Lee Jungryong's prized Disciple. |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 평화 | **Peace Guild** | Guild name. |
| 아레스 | **Ares Guild** | The leading Guild in Korea; formerly employed Team Leader Choi and Song Song. |
| 대리 | **Assistant Manager** | Corporate title used by Kim Seonhee |
| 보안팀 | **Security Team** | Sangdong Guild’s surveillance and protection unit. |
| 보안팀장 | **Security Team Leader** | Unnamed leader coordinating the operation. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 철권 | **Iron Fist** | Choo Dohwan's epithet. |
| 청와대 | **Blue House** | Presidential office mentioned in an online comment about proposed legislation. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 오크 | **Orc** | Monster species. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 계인 | **Buddhist precept seals** | Seals carved into the foreheads of Shaolin martial monks. |
| 석고준 | **Go Jun** | Source full-name form for the established Go Jun, also known as Team Leader Seok. |
| 경호팀장 | **Head of Security** | Go Jun's security-team office under Lee Jungryong. |
| 존슨 | **Johnson** | Co-host of the American talk show that replays Taekyung's viral interview. |
| 미국 | **United States** | Country associated with the talk show and CNM. |
| 중국 | **China** | Country from which Team Leader Choi’s video originates. |
| 쓰촨성 | **Sichuan Province** | Source spelling variant of the established Sichuan location. |
| 대통령 | **President** | Title for Korea's head of state. |
| 주석 | **Chairman** | Political title used for Xiao Yang. |
| 마계어 | **Demon Realm language** | Language spoken by monsters from the Demon Realm. |
| 미미 | **Mimi** | Worker at Honghwaru referenced in Taekyung's joke. |
| 쓰촨 | **Sichuan** | Variant spelling used for the region associated with the pattern Jin recognizes. |
| 고이즈미 | **Koizumi** | Japanese prime minister quoted in the news. |
| 텔레포트 | **Teleport** | Taekyung's label for the Blood Lord's unexplained disappearance. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 상주 | **chief mourner** | Funeral role assumed by Go Jun for Lee Jungryong. |
| 대마도사 | **Grand Mage** | Title used for Magic Johnson. |
| 조셉 | **Joseph** | Hunter named in the recorded Monster Wave footage. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 석고준 | 최민우 | Ares security leader to rival Guild Master | Team Leader Choi Minwoo | formal but barbed | Uses 평화 길드 최민우 팀장님 while belittling Choi and blaming the Peace Guild for Taekyung's apparent death. |
| 진태경 | 석고준 | returning Hunter to hostile Ares security leader | you fucking bastard | hostile and profane | Taekyung directs his final insults and challenge at Go Jun after returning alive. |
| 석고준 | 진태경 | hostile_opponents | brat | hostile and overconfident | Go Jun addresses Taekyung internally as 애송아 while launching his full-strength attack. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 중년인 | 진태경 | veteran civilian Hunter to celebrated allied Hunter | Mr. Jin | formal-polite and awed | The casualty clerk addresses Jin as 진 선생님 after Jin asks him to list Lei Fei among the dead. |
| 진태경 | 중년인 | celebrated Hunter to older fellow Hunter | sir | casual and teasing | Jin addresses the older Hunter as 아저씨 while joking with him and giving him instructions. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 최민우 | 진태경 | trusted allied team leader to younger allied Hunter | Mr. Jin | formal-polite and concerned | Choi warns Jin about the danger of the operation and affirms his deep trust. |
| 진태경 | 최민우 | younger allied Hunter to allied team leader | Team Leader Choi | polite, familiar, and teasing | Jin jokes with Choi while acknowledging and dismissing his concern. |
| 진태경 | 존슨 | Allied Hunter to Grand Mage | Johnson | polite and familiar | Jin repeatedly addresses Magic Johnson directly while requesting explanations and permission to visit the site. |
| 고준 | 진태경 | Ares Guild combatant confronting the killer of his Master | you | hostile and informal | Go Jun uses 너 while demanding Jin confess to Lee Jungryong's death and threatening retaliation. |
| 진태경 | 고준 | dominant adversary confronting Lee Jungryong's Disciple | you | contemptuous and informal | Jin uses 너 and 놈 while overpowering Go Jun and ordering him to end the conflict with Lee Jungryong. |
| 진태경 | 대통령 | Hunter_to_President | Mr. President | formal-polite | Taekyung addresses the President respectfully during their airport greeting. |
| 대통령 | 진태경 | President_to_Hunter | Mr. Jin Taekyung | formal-polite | The President addresses Taekyung by name at the airport photo line. |
| 팀원 | 석고준 | subordinate security-team member to security-team leader | Team Leader | fearful formal-polite | The team member repeatedly addresses Go Jun as 팀장님 while reporting the strange object. |
| 진태경 | 미미 | rescuer to companion snake | Mimi or Mimi-chan | informal, pleading | Taekyung calls to Mimi while asking the snake to carry him and the survivors. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 558
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Go Jun.md

# Go Jun (고준)

- **Safe through:** Chapter 560
- **Aliases:** Team Leader Seok
- **Role:** Go Jun is Ares Guild's new Vice Guild Master, Lee Jungryong's disciple and former security-team leader, and the chief mourner at Lee's national funeral.
- **Personality:** Highly disciplined, fiercely loyal to Lee Jungryong, confident in his abilities, and capable of suppressing his anger and killing intent under provocation.
- **Voice:** Dry, controlled, and formal with subordinates; deferential when addressing his Master.
- **Relationships:** Disciple and direct protégé of Lee Jungryong, Go Jun inherited Lee's Ares Guild legacy after his death and regards Jin Taekyung and Choi Minwoo as enemies seeking to take it away.

### Human Butcher.md

# Human Butcher (인도)

- **Safe through:** Chapter 558
- **Aliases:** None
- **Role:** Former mysterious Han Chinese mounted-bandit power in Northern Gaoyuan commanding fifty subordinates; a Peak master killed by an unnamed old man in a single move
- **Personality:** Cold, intimidating, and murderous; he kills people as though slaughtering livestock
- **Voice:** Cold, curt, and quietly threatening
- **Relationships:** He is one of four powerful participants at the Northern Gaoyuan gathering, intimidates Temur, and has claimed Ghost Sword Wipeng as his personal target in the proposed attack

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 561
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, a Supreme Peak master who possesses the Heavenly Martial Physique and superhuman physical strength, has manifested Force, opened his Middle Dantian, crossed the wall into true mastery, has achieved Three Flowers Gather at the Crown but not Five Qi Returning to Origin, can perceive the texture of qi well enough to sever layered magic, can resist high-level monster Fear through exceptional mental strength, is publicly recognized as an S-rank-level Hunter while formally retaining an A-rank license pending testing, can command coordinated raids against powerful monsters, serves as one of the two pavilion masters of the Alliance Leader's direct Fire Dragon Pavilion, leads its first mission to Nanman, and is the Peace Guild's wealthy patron in the modern world.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor and assigned him a final task to incorporate martial principles into his learned martial arts but declined Taekyung's recruitment after Cheongpung reached him first, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate, student, and trusted manager of media and official arrangements, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, and Xiao Shen regards him as an older brother after Jin saved him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 561
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Team Leader Choi.md

# Team Leader Choi

- **Safe through:** Chapter 555
- **Aliases:** Choi Minwoo (최민우)
- **Role:** Team Leader Choi is Cheon Taemin's only living blood relative and is positioning himself to take control of the Ares Guild after Lee Jungryong's death.
- **Personality:** Strategic, candid, controlled, and possessive of the power and influence he intends to inherit.
- **Voice:** Dry, formal, and direct, with calm candor and carefully chosen metaphors.
- **Relationships:** Maternal grandson and only living blood relative of Cheon Taemin; was kept out of public knowledge by Lee Jungryong and now seeks to acquire the Ares Guild intact.

## Korean source

```text
＃562화



그곳은 온 사방이 끝없이 뻗어 있는 황무지였다.

태양은 존재하지 않으나 마력으로 이루어진 어두운 빛이 감돌고, 수백 마리의 오크가 무리를 지어 떠돌다 헌터에 의해 사냥당하는 곳.

아니, 그랬었던 곳.

쿵. 쿵. 쿵.

지면이 몸을 떨었다. 사방을 잠식한 마력이 금방이라도 터져 나갈 것처럼 팽창하며 숨을 옥죈다.

헉. 허억. 가쁜 숨이 흘러나오는 헌터들의 입안에서는 단내가 풍겼다.

동그랗게 등을 맞댄 그들의 주위에는 이미 백여 마리가 넘는 오크들이 널브러져 있었지만, 저 너머에서는 그 열 배에 달하는 몬스터 대군이 밀려오고 있었다.

“티, 팀장님.”

“걱정하지 마라. 우리는 무슨 수를 써서라도 살아 나간다.”

겁에 질린 누군가에게 답하는 팀장의 대답은 목소리는 공허했다.

묻는 이도, 대답하는 이도 이미 어렴풋이 짐작하고 있었다. 그들 모두는 오늘 이 자리에서 살아 나가지 못한다는 것을.

기적적으로 몬스터 대군의 포위망을 뚫는다 해도, 한 놈만큼은 도저히 쓰러트릴 수 없으리라는 것을.

- 크와아아악!

오크 로드.

백만분의 일 확률로 탄생한다는 강력한 변이 개체의 포효에 천 마리가 넘는 오크들은 괴성과 함께 각자의 무기를 부딪쳤다.

- 취이이익!

카캉! 쾅쾅쾅!

그 광경을 바라보는 헌터들의 눈빛에 절망이 스쳤다.

‘끝장이다.’

상대는 오크 로드의 지휘하에 더욱 강력해진 몬스터 대군이다.

강력한 지휘관을 얻은 오크들은 더 이상 수십 마리씩 무리 지어 다니던 오합지졸이 아니었고, 헌터들의 숫자는 고작 스물도 채 되지 않았다.

‘이건…… 이길 수 없는 싸움이야.’

순간 모두의 뇌리를 스친 생각이었다.

설령 그들이 동급의 헌터들을 압도하는 실력자라 해도 그 사실은 달라지지 않았다.

아레스 길드라는 자부심도 코앞에 닥쳐 온 죽음 앞에서는 속절없이 무너졌다.

“……빌어먹을 변이 게이트.”

누군가의 입술 사이로 흘러나온 중얼거림과 함께, 사방을 가득 메운 몬스터들이 일제히 돌격을 시작했다.

그리고 그 선두에, 쳐 죽여도 시원치 않을 오크 로드가 있었다.

- 카르취! 칼립토!

구구구구궁!

알아들을 수 없는 마계어와 함께 쏘아지는 거체.

이를 악문 레이드 팀장이 방패를 들고 마주 달려 나갔다.

뒤에서 그를 부르는 팀원들의 외침이 울려 퍼졌지만, 오직 눈앞의 적을 향해 모든 신경과 힘을 끌어올렸다.

“와라!”

두려움을 애써 몰아내는 커다란 외침.

그를 발견한 오크 로드의 눈동자에 붉은빛이 번뜩인 순간, 손에 들린 거대한 도끼가 팀장의 정수리를 노리고 내리그어졌다.

후웅, 콰아아앙!

단 일격. 그것으로 끝이었다.

믿을 수 없을 만큼 빠르고 강력한 일격은 굉음과 함께 상급 강화 마법이 걸린 타워 실드(Tower Shield)를 산산조각 냈고, 팀장은 양팔이 부러지는 고통도 잊은 채 눈을 부릅떴다.

후우우웅.

도끼의 날이 닿기도 전이었건만, 벌써 옆구리가 베인 듯했다.

주마등과 함께 느려진 세상 속, 자신의 몸뚱어리를 상하로 분리할 두 번째 공격이 날아들고 있었다.

‘아니, 두 번째가 아니라 마지막이겠지.’

팀장은 눈을 감았다. 생애 마지막으로 보는 광경이 저 못생기고 빌어먹을 몬스터가 되는 건 사양하고 싶었다.

그리고 다음 순간. 눈 앞을 가린 칠흑 같은 어둠과 함께, 날카로운 파공성이 귓가를 파고들었다.

쐐애애애액, 뻐억!

기다렸던 고통은 없었다. 스스로도 신기할 만큼. 정말 이게 죽음이란 것이 맞는지 의심이 갈 만큼.

“……?”

뒤늦게 실눈을 뜬 팀장은 멍하니 입을 벌렸다.

불과 다섯 발자국도 떨어지지 않은 거리. 3m에 달하는 오크 로드의 거체가 우뚝 멈춰 있었다.

머리통이 사라진 채로.

“……!”

“……!”

세상이 정지한 듯했다.

인간도, 몬스터도. 움직임을 멈춘 채 그 광경을 바라보았다. 지금 이 순간.

끝없이 펼쳐진 황무지에서 움직이는 것은 단 하나뿐이었다.

드드드득.

오크 로드의 머리를 터트리고, 지면을 관통한 채 부르르 떨리고 있는 한 자루의 창.

그리고 신비롭게 보일 만큼 은은한 빛을 뿌리는 저 창의 주인이 누구인지, 이 자리에 있는 헌터들은 알고 있었다.

‘진태경!’

벼락처럼 뇌리를 스치는 한 사람의 이름과 함께, 지면 깊숙이 박혀있던 창이 솟구쳐 누군가의 손아귀로 빨려 들어갔다.

쐐애애액, 탁.

약속이라도 한 듯. 천천히 고개를 돌린 사람들은 비로소 깨달을 수 있었다.

“변이 게이트를 떠도는 어린 양들이여. 존나게 달려서 내 뒤로 오라.”

코앞에 닥쳤던 죽음의 그림자가, 어느덧 깨끗이 사라졌다는 사실을.



* * *



저벅. 저벅.

중년인의 걸음은 당당했고, 막힘없었다.

청와대와 국회의사당이 한눈에 내려다보이는 초고층 빌딩의 내부로 들어선 후에도 마찬가지였다.

“길드원이시라면 우선 출입증을 제시…….”

“못 보던 얼굴인데. 신입인가?”

“예? 예. 그렇습니다만.”

“하긴, 이러는 거 보면 신입이겠지. 팀장한테 이야기 못 들은 모양이군.”

중년인을 멍하니 바라보던 보안팀 헌터가 헛숨을 삼켰다.

“헉. 죄송합니다. 미처 못 알아뵙고…….”

“괜찮아. 바쁘니까 이제 길이나 좀 비키지.”

“예, 옛.”

외부인, 내부인 가릴 것 없이 누구나 거쳐야 하는 보안 검색대도 중년인을 멈추게 할 수는 없었다.

황급히 고개를 숙인 보안팀 헌터를 힐끗 바라본 그는 목적지로 이동했다.

간단한 수술을 통해 귀밑에 심어 놓은 초소형 통신기에서는 이미 누군가의 목소리가 흘러나오는 중이었다.

- 기다리고 계십니다.

중년인의 입술이 작게 달싹였다.

“위치는?”

- A구역입니다.

150층에 달하는 초고층 빌딩이지만, 설계 지도나 내부 안내판 어디에도 A구역이라는 이름은 찾아볼 수 없다.

그곳은 수많은 길드원 중에서도 극소수의 이들에게만 허락된 공간이니까.

당연하게도 중년인도 그중 하나였다.

“텔레포트 열어 놔.”

- 준비 완료된 상태입니다. 그나저나 보안팀 신입이 부팀, 아, 죄송합니다. 팀장님.

“괜찮으니까 신경 쓰지 마라.”

아직 당사자인 나도 익숙하지 않은데, 뭘.

이어질 뒷말을 내심 중얼거리는 중년인에게, 통신기 너머의 누군가가 말을 이었다.

- 어쨌든 보안팀장에게 통보해서, 해당 인원은 징계 조치하도록 하겠습니다.

전달도, 제안도 아닌 통보다. 언제부터인가 당연한 것이 되었지만 여전히 낯설게 느껴지는 그 단어에, 중년인은 미미하게 눈살을 찌푸렸다.

“뭘 또 그렇게까지…….”

- 팀장님?

“……아니다. 그 문제는 알아서 해결해.”

- 예. 적당히 처리하겠습니다.

적당히, 라는 의미는 최소가 감봉이며 혹은 좌천이라는 이야기다.

잠깐 자신을 가로막았던 젊은 청년을 떠올린 중년인은 마음 한구석이 불편해지는 것을 느꼈지만, 어쩔 수 없었다.

그것이 그가 속한 길드의, 아니 자신들만의 방침이니까.

‘심지어 그 일이 있었던 뒤부터…… 점점 심해지고 있어.’

길드의 철권 통치는 예전부터 익히 알고 있었지만, 최근 있었던 불의의 사건 이후 더욱 극심해지고 있었다.

어쩌면 그것은 아직 신하들로부터 완전히 정통성을 인정받지 못한 새로운 왕의 조급함일지도 모른다.

작게 한숨을 내쉰 중년인이 발걸음과 함께 입을 열었다.

“VIP 현 상황 보고해.”

- 기분이 좋지 않으십니다.

“착각인가? 어제도 비슷한 말을 들었던 것 같은데.”

- ……그, 오늘 조간신문을 보시고 그만.

“더 들을 필요도 없겠군. VIP께서 읽고 계신 거 싹 다 긁어서 보내. 지금 당장.”

중년인의 말이 끝나기 무섭게, 기다렸다는 듯이 보안 마법이 걸린 스마트폰이 부르르 몸을 떨었다.

화면을 가볍게 두드리자 불과 두세 시간 전 인쇄소를 통과한 20여 개 조간신문의 헤드라인이 빼곡하게 떴다.



[사상 초유의 사태…… 잇따른 변이 게이트 출현이 시사하는 바는?]

[불길한 징후. 중국 쓰촨성의 악몽이 한국으로 이어지나.]

[청와대 긴급 발표, “혹시 모를 미연의 사태를 방지하기 위해 평화 길드와 협약 체결, 지금까지의 성과는 고무적.”]

[세 번째 변이 게이트. 그러나 사망자는 제로? 평화 길드 긴급 구조팀을 향한 세계인들의 찬사.]

[미국의 대마도사 매직 존슨. “평화 길드는 새로운 시대의 등불. 진과 최는 선하고 올곧은 청년들.”]

[美 전 대통령 조셉 바이든. “사우스 코리아는 누구도 의심할 수 없는 헌터 강대국이며, 향후 이 시대를 이끌어 나갈 훌륭한 젊은이들을 품고 있다. 이번에 만난 최 역시 그중 하나다.”]

[中 국가 주석 샤오 양, “최 선생은 알려지지 않은 또 한 사람의 영웅. 우리는 쓰촨에서 죽음을 무릅쓰고 싸운 그를 기억한다.”]

[日 총리대신 고이즈미 신지로 역시 SNS에 언급. “제가 알기로 최는 한국인입니다. 그렇기 때문에 그는 일본인이 아닙니다.” 이에 따른 국내 누리꾼들의 반응. “우리 쪽 병신이 아니라 다행이다.”]

[잇따른 거물들의 발언이 불러온 초유의 관심. “도대체 그들이 말하는 최(Choi)는 누구인가?” 알려진 바에 따르면 평화 길드의 최민우 팀장으로 밝혀져…….]

[S급 헌터 진태경. 오늘 아침 대통령과 함께 신년맞이 “국민 소통” 신년 기자회견 참석!]

.

.

.

“……후.”

기사를 모두 읽은 중년인은 뻑뻑한 눈가를 문질렀다. 잊고 있던 피로가 몰려오는 듯했다.

“젠장.”

- 다 읽으셨습니까?

“그래. 차라리 안 읽는 게 나을 뻔했지만.”

- ……말씀 중에 죄송합니다만, 조금 서두르셔야 할 것 같습니다.

“안 그래도 그러려고. 거의 다 왔다.”

저벅.

대답과 함께 중년인은 희미한 빛을 뿌리는 마법진을 밟았다.

지문을 인증하고 마나를 불어넣자, 사용자를 인식한 텔레포트 마법진이 강렬한 섬광을 토해 냈다.

팟!

휘황한 빛무리과 함께 전신이 붕 뜨는 듯한 감각이 그를 사로잡았다.

그리고 다음 순간, 중년인은 눈을 뜸과 동시에 A구역으로의 텔레포트가 성공했음을 깨달았다.

새하얀 대리석과 마정석으로 장식된 실내. 얇은 맞춤 정장을 입은 남녀 십여 명이 그를 향해 허리를 굽혔다.

“오셨습니까, 팀장님.”

사람은 여럿인데, 목소리는 하나다.

마치 기계처럼 움직이는 부하 직원들을 힐끗 바라본 중년인은 천천히 마법진에서 걸어 나왔다.

“VIP는?”

“홀로 개인 집무실에 계십니다.”

“경호 인력 없이? 내가 최소 세 명은 복도에 상주하라고 분명히…….”

쾅!

어디선가 희미하게 울려 퍼진 굉음에 뒷말이 뚝 끊겼다. 대강 상황을 짐작한 중년인이 작게 혀를 찼다.

“내가 가 볼 테니까 한 명만 남고 A구역 비워.”

“예.”

지시가 떨어지자마자 일사불란하게 움직이는 부하들을 뒤로 한 채, 중년인은 드넓은 복도를 걷기 시작했다.

복도에는 침입자를 방비하기 위해 최소 오십 개 이상의 마법 트랩(Magic Trap)이 설치되어 있었지만, 그의 목에 걸린 출입 카드에는 이 지뢰밭을 무사히 지나갈 만한 장치가 숨겨져 있었다.

지이잉.



[경호팀장 고세원]



붉은 광채가 스치고 가자 사방에서 들끓던 마나가 삽시간에 가라앉았다.

끝없이 이어진 복도를 익숙하게 가로지른 중년인, 고세원은 굳게 닫힌 문 앞에서 걸음을 멈췄다.

똑똑.

“고세원입니다.”

문 너머에서 누군가의 성마른 목소리가 들려왔다.

“들어와.”

고세원은 천천히 문고리를 잡고 밀었다.

폭탄이라도 터진 것처럼 난장판이 된 집무실의 정중앙. 소파에 앉아 있던 한 사람이 붉은 빛이 서린 눈동자로 그를 응시했다.

“평소보다 늦었군.”

고세원은 말없이 고개를 숙였다. 널브러진 잔해들 사이로 번쩍이는 명패가 보였다.



[아레스 부길드장 석고준]
```

## Final English reading copy

```markdown
# Chapter 562

It was a wasteland stretching endlessly in every direction.

There was no sun, but dark light formed from mana hung in the air. Hundreds of orcs roamed in packs, only to be hunted down by Hunters.

Or rather, that was what had happened here once.

*Boom. Boom. Boom.*

The ground trembled. The mana consuming the area swelled as though it might burst at any moment, squeezing the breath from their lungs.

The Hunters panted raggedly, their breath carrying a sickly sweet smell.

More than a hundred orcs already lay sprawled around the Hunters, who stood back-to-back in a circle. But beyond them, a monstrous army ten times their number was advancing.

“T-Team Leader.”

“Don’t worry. We’ll get out of here somehow.”

The Team Leader’s reply to the frightened Hunter was hollow.

The person asking and the person answering both already had a vague idea of the truth.

None of them would make it out of this place alive today.

Even if they miraculously broke through the monster army’s encirclement, there was one opponent they would never be able to bring down.

*—Kraaaargh!*

The Orc Lord.

At the roar of the powerful mutated individual said to be born only once in a million chances, more than a thousand orcs let out shrieks and struck their weapons together.

*—Chweeek!*

*Clang! Crash-crash-crash!*

Despair flickered in the Hunters’ eyes as they watched.

*It’s over.*

They were facing an army of monsters made even more powerful under the Orc Lord’s command.

With a powerful commander at their head, the orcs were no longer a rabble that merely wandered around in groups of a few dozen. And the Hunters numbered fewer than twenty.

*This is… a fight we can’t win.*

The thought flashed through everyone’s mind at once.

Even if they were elites capable of overwhelming Hunters of the same rank, that fact would not change.

Their pride in belonging to Ares Guild crumbled helplessly before the death approaching them.

“……Damn Mutated Gate.”

As someone muttered those words, the monsters filling the area began charging all at once.

At the very front was the Orc Lord, a monster so hateful that killing it would never be satisfying enough.

*—Karchwi! Kalipto!*

*Rumble-rumble-rumble!*

The massive body shot forward alongside unintelligible words in the Demon Realm language.

The raid Team Leader gritted his teeth, raised his shield, and charged to meet it.

His team members shouted for him from behind, but he drew every ounce of his strength and concentration toward the enemy in front of him.

“Come on!”

It was a great shout, forced out to drive away his fear.

The moment red light flashed in the Orc Lord’s eyes, the enormous ax in its hands came crashing down toward the Team Leader’s crown.

*Whooosh—crash!*

One strike.

That was all it took.

The blow was unbelievably fast and powerful. With a thunderous roar, it shattered the **Tower Shield** reinforced with high-grade enhancement magic.

The Team Leader’s eyes widened. He forgot even the pain of both arms breaking.

*Whoooosh.*

The ax had not even reached him, yet it already felt as though his side had been sliced open.

The world slowed around him as his life flashed before his eyes. A second attack was hurtling toward him, one that would cleave him in half at the waist.

*No. Not a second attack. The last attack.*

The Team Leader closed his eyes.

He had no desire to spend the last moment of his life looking at this ugly, fucking monster.

And then, in the next instant—

Along with the pitch-black darkness blocking his vision, a sharp sound of something cutting through the air pierced his ears.

*Fwoooooosh—crack!*

The pain he had been waiting for never came.

It was so strange that even he doubted whether this was really death.

“……?”

The Team Leader opened his eyes to narrow slits and stared blankly with his mouth hanging open.

Less than five paces away, the three-meter-tall body of the Orc Lord stood frozen in place.

Its head was gone.

“……!”

“……!”

It was as if the world had stopped.

Humans and monsters alike had ceased moving as they stared at the sight.

At that moment, only one thing moved across the endless wasteland.

*Rrrrrr.*

A single spear that had blown apart the Orc Lord’s head, pierced through the ground, and now trembled violently.

The Hunters there knew who owned that spear, which gave off a soft, almost mystical light.

*Jin Taekyung!*

Along with the name that flashed through their minds like lightning, the spear lodged deep in the ground shot upward and flew into someone’s grasp.

*Fwoooooosh—tap.*

As though they had agreed beforehand, the people slowly turned their heads.

Only then did they realize.

“Lambs wandering through the Mutated Gate. Run your asses off and get behind me.”

The shadow of death that had been looming right before them had vanished without a trace.



* * *



*Tap. Tap.*

The middle-aged man’s stride was confident and unhindered.

Even after entering the interior of the skyscraper overlooking the Blue House and the National Assembly at a glance, nothing changed.

“If you’re a Guild member, please present your access pass first—”

“I haven’t seen your face before. Are you new?”

“Pardon? Yes. Yes, I am.”

“Thought so. You must be new if you’re acting like this. Looks like your Team Leader didn’t tell you.”

The Security Team Hunter, who had been staring blankly at the middle-aged man, sucked in a startled breath.

“I’m sorry. I didn’t recognize you—”

“It’s fine. I’m busy, so move.”

“Y-Yes, sir.”

Not even the security checkpoint that everyone, outsider or insider, had to pass through could stop the middle-aged man.

He gave the Security Team Hunter, who was hurriedly bowing, a sidelong glance before continuing toward his destination.

A voice was already coming through the tiny communication device implanted below his ear through a simple operation.

—He’s waiting for you.

The middle-aged man’s lips moved slightly.

“Where?”

—Section A.

The 150-story skyscraper had no section called A anywhere on its design plans or interior signs.

It was a space granted only to a very small number of people among the countless Guild members.

Naturally, the middle-aged man was one of them.

“Open the Teleport.”

—It’s ready. By the way, about that new Security Team recruit, Deputy Team—ah, sorry. Team Leader.

“It’s fine. Don’t worry about it.”

*Even I’m not used to it yet, so what can you expect?*

As the middle-aged man silently muttered the rest to himself, the person on the other end continued.

—In any case, I’ll notify the Security Team Leader and have the individual disciplined.

It was not a report or a suggestion. It was a notification.

The word had become ordinary at some point, but it still felt unfamiliar. The middle-aged man frowned faintly.

“Is that really necessary?”

—Team Leader?

“……Never mind. Handle it however you see fit.”

—Yes. I’ll take care of it appropriately.

“Appropriately” meant a pay cut at minimum, or possibly demotion.

The middle-aged man thought briefly of the young man who had stopped him and felt a twinge of discomfort in one corner of his heart.

But there was nothing he could do.

That was the policy of the Guild he belonged to.

No—their policy.

*It’s been getting worse ever since that incident.*

He had long known that the Guild was ruled with an iron fist, but its grip had tightened even further since the recent unfortunate incident.

Perhaps it was the impatience of a new king whose legitimacy had not yet been fully acknowledged by his subjects.

The middle-aged man let out a small sigh and spoke as he walked.

“Give me a report on the VIP’s current condition.”

—He is in a bad mood.

“Am I imagining things? I feel like I heard something similar yesterday.”

—……Well, after reading this morning’s newspaper, he—

“That’s enough. Send me everything the VIP is reading. Scrape it all and send it to me. Right now.”

The moment the middle-aged man finished speaking, the smartphone protected by security magic began vibrating as though it had been waiting for his order.

He tapped the screen lightly. The headlines of more than twenty morning newspapers that had left the presses only two or three hours earlier filled the display.



> An Unprecedented Crisis… What Do the Successive Mutated Gates Signify?

> Ominous Signs. Will the Nightmare of China’s Sichuan Province Reach Korea?

> Emergency Blue House Announcement: “To Prevent Any Unforeseen Incidents, We Have Signed an Agreement with the Peace Guild. The Results So Far Are Encouraging.”

> The Third Mutated Gate. Yet Zero Fatalities? Worldwide Praise for the Peace Guild’s Emergency Rescue Team.

> American Grand Mage Magic Johnson: “The Peace Guild Is the Light of a New Age. Jin and Choi Are Good, Upright Young Men.”

> Former U.S. President Joseph Biden: “South Korea Is an Unquestionable Hunter Powerhouse and Home to Wonderful Young People Who Will Lead This Era. The Choi I Met This Time Is One of Them.”

> Chinese Chairman Xiao Yang: “Mr. Choi Is Another Unsung Hero. We Remember How He Risked His Life Fighting in Sichuan.”

> Japanese Prime Minister Shinjirō Koizumi Also Mentions Choi on Social Media: “As Far as I Know, Choi Is Korean. Therefore, He Is Not Japanese.” Domestic Netizens React: “Thank God He Isn’t One of Our Idiots.”

> Unprecedented Interest Following Statements from One Powerful Figure After Another: “Who on Earth Is the Choi They’re Talking About?” Sources Confirm That He Is Choi Minwoo, Team Leader of the Peace Guild……

> S-Rank Hunter Jin Taekyung Attends New Year’s “Communicating with the People” Press Conference with the President!

> .

> .

> .

“……Whew.”

After reading every article, the middle-aged man rubbed his dry, aching eyes.

The fatigue he had forgotten about seemed to come rushing back.

“Damn it.”

—Have you finished reading?

“Yes. It would probably have been better if I hadn’t read them.”

—……I’m sorry to interrupt, but you should hurry.

“I was about to. I’m almost there.”

*Tap.*

As he answered, the middle-aged man stepped onto a magic circle radiating a faint light.

He authenticated his fingerprint and infused it with mana. The Teleportation magic circle recognized its user and released a powerful flash.

*Flash!*

A sensation like his entire body floating into the air seized him amid a dazzling halo of light.

And in the next moment, the middle-aged man opened his eyes and realized that the Teleport to Section A had succeeded.

The interior was decorated with pure white marble and Magic Gems. Around a dozen men and women in tailored suits bowed toward him.

“Welcome, Team Leader.”

There were many people, but only one voice.

The middle-aged man glanced at his subordinates, who moved like machines, and slowly stepped off the magic circle.

“Where’s the VIP?”

“He is alone in his private office.”

“Without any security? I clearly told you to keep at least three people stationed in the hallway—”

*Boom!*

A faint roar echoed from somewhere, abruptly cutting off the rest of his sentence.

The middle-aged man roughly guessed what had happened and clicked his tongue.

“I’ll go. Leave one person behind and clear Section A.”

“Yes.”

His subordinates began moving in perfect order as soon as the command was given. Leaving them behind, the middle-aged man started down the wide corridor.

At least fifty Magic Traps had been installed throughout the hallway to guard against intruders. But the access card hanging around his neck concealed a device that allowed him to pass safely through the minefield.

*Bzzzt.*



> **Head of Security Go Se-won**



As a red radiance swept over the area, the mana boiling all around him settled in an instant.

The middle-aged man, Go Se-won, crossed the seemingly endless corridor with practiced ease and stopped in front of a tightly closed door.

*Knock, knock.*

“This is Go Se-won.”

A sharp voice came from beyond the door.

“Come in.”

Go Se-won slowly grasped the doorknob and pushed it open.

At the center of the office, which had been wrecked as though a bomb had exploded inside, a man sitting on the sofa stared at him with red light glowing in his eyes.

“You’re later than usual.”

Go Se-won silently bowed his head.

Amid the scattered wreckage, a nameplate flashed.



> **Ares Guild Vice Guild Master Go Jun**
```

<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0667.txt",
      "sha256": "d3e81a56964a6cf1289a77a65b6679b340fe9b0686c574ab151436098762e3ec",
      "bytes": 13482
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "f9af45a3d43adf33f0b98ff7c653b3e3b9b0120c9545bb8aaa367f2e4c91a025",
      "bytes": 1985
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "050c006b5f091041d81ee2d3d2c189fc6d9e5840e2ad9aa9bcb1c627b0199019",
      "bytes": 201910
    },
    {
      "path": "characters/Beast Miao King.md",
      "sha256": "fa30fde637262d7674bf8b3cd49e158006f36554ad44aa85c58e5b1a3ceb21cc",
      "bytes": 959
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "09a2d3921126e09691b9901ba937fc8118ac9feaf6f05ade82631aedc7f6e8bc",
      "bytes": 553
    },
    {
      "path": "characters/Dogok.md",
      "sha256": "34263f13a51a91ed274a19e2c71e9d9964bece77af18820622f4519abe20de00",
      "bytes": 406
    },
    {
      "path": "characters/Gisan.md",
      "sha256": "24a3fb393e59eeb90ff76a9ce95f587ab470b4565ac932a9fd2c1b06a0c2d9e4",
      "bytes": 406
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "8e14403d598ac67c492dbd88f7db27e9aa65d4e79e0c90cd472982c877f1b759",
      "bytes": 1907
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "60a59fdd8684d5ed38cd856343cf0d0549554b78ff8527a1e8a71572cab3e6b9",
      "bytes": 622
    },
    {
      "path": "characters/Wonhu.md",
      "sha256": "15d7bec239c6bc192805912d40974bfa112dd81272ff1a269f37e6bfaded63ac",
      "bytes": 406
    },
    {
      "path": "characters/Yayul Mok.md",
      "sha256": "2b2d17850ef3cb3a1db0280af0c7befdf40030b7195be9251c1c26507d0d7d12",
      "bytes": 871
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "29aa69db3afa385987676e935eee2351d038d97abe98f880edd9d0534e275da2",
      "bytes": 207150
    }
  ],
  "estimated_tokens": 11012
}
-->

# Durable State Update — Chapter 667

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 667. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 667. Profile updates may replace only one
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
  "chapter": 667,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 667,
    "continuity_sources": [667],
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
    "Jin Taekyung remains imprisoned in the underground prison, with execution scheduled for noon in two days.",
    "Twenty tribal chieftains, including Baeksang, support Jin's execution, which is the agenda of tomorrow's final Tribal Grand Council.",
    "The Beast Miao King and Baeksang are sworn brothers whose opposing responses to their children's deaths have driven them apart.",
    "Baeksang's only child Hwi was sacrificed after supposed allies abandoned him, leaving Baeksang consumed by grief and resentment toward the Central Plains.",
    "The Beast Miao King chose Nanman's survival and a lasting peace over personal revenge and now supports cooperation with the Central Plains against Dark Heaven.",
    "The Beast Miao King has offered to step down and make Baeksang Palace Lord if Baeksang opens a path for half a shichen.",
    "Baeksang remains visibly conflicted and has not summoned the guards to stop the rescue.",
    "Yayul Mok leads a covert group that has reached the underground prison and ordered it opened."
  ],
  "continuity_sources": [
    666,
    665
  ],
  "open_questions": [
    "Will Yayul Mok's group free Jin before his scheduled execution?",
    "Will Baeksang allow the rescue to proceed and accept the Beast Miao King's offer?",
    "Will Baeksang abandon the execution supported by the twenty chieftains?",
    "What precisely happened to Hwi, and which supposed allies were responsible for abandoning him?",
    "How will the Tribal Grand Council respond if the Beast Miao King steps down or Jin escapes?"
  ],
  "safe_through": 666,
  "temporary_decisions": [
    "Use Escape from Namshank for 남생크.",
    "Use Deputy Stronghold Lord for 부채주 and Stronghold Lord for 채주.",
    "Retain underground prison for 뇌옥.",
    "Capitalize Will when referring to the System-linked martial concept 의지.",
    "Use Middle Dantian and Three Dantians for 중단전 and 삼단전."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 남만야수궁  | **Nanman Beast Palace**          |
| 절정     | **Peak**          |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 돌파     | **break through** / **breakthrough**             | Realm advancement                                     |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 마교     | **Demonic Cult**                                 |                                                       |
| 중원     | **Central Plains**                               |                                                       |
| 정마대전   | **Great Faction War**         |
| 형장      | **Brother** / **Brother [Name]**                                |
| 야수묘왕 | **Beast Miao King** | Leader of the Miao people and master of the Nanman Beast Palace. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 도곡 | **Dogok** | Named member of the Beast Miao King's personal guard, the Seven Miao Tigers. |
| 기산 | **Gisan** | Named member of the Beast Miao King's personal guard, the Seven Miao Tigers. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 원후 | **Wonhu** | Named member of the Beast Miao King's personal guard, the Seven Miao Tigers. |
| 야율목 | **Yayul Mok** | Young Palace Lord of the Nanman Beast Palace. |
| 아혈 | **Mute Acupoint** | System condition label preventing speech. |
| 출혈 | **Bleeding** | Effect with a 90% activation chance on a successful spear hit. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 한족 | **Han Chinese** | Ethnic designation used by the steppe chieftains. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 점혈 | **Pressure-Point Strike** | System-named technique used by Jeok Cheongang on Taekyung. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 전광석화 | **Quick Attack** | Warlordmon’s rapid-movement command; used as a Pokémon-style gag. |
| 전광 | **Quick Attack** | Shortened form of Warlordmon’s rapid-movement command. |
| 뇌옥 | **underground prison** | The Tang Clan's subterranean prison. |
| 묘족 | **Miao people** | Ethnic group the Escort Bureau expects to encounter near Yunnan. |
| 촌각 | **moments** | Short intervals disappearing from Jeok's day. |
| 식경 | **half an hour** | Time limit given for the requested reports. |
| 화룡각 | **Fire Dragon Pavilion** | New name chosen for Taekyung's pavilion. |
| 고든 | **Gordon** | Pentagon employee tasked with repairing smashed warning lights. |
| 백족 | **Bai people** | Ethnic group encountered in Yeongin. |
| 애뇌산 | **Ailao Mountain** | Mountain crossed by the party on the route to the Nanman Beast Palace. |
| 칠묘호 | **Seven Miao Tigers** | The Beast Miao King's personal guard, composed of elite Miao warriors. |
| 야율 | **Yayul** | Name used in Taekyung's colloquial address to the Beast Miao King. |
| 금력단 | **Force-Sealing Pill** | Special pill blocking Jin Taekyung's dantian and preventing internal-energy use. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 중년인 | 진태경 | veteran civilian Hunter to celebrated allied Hunter | Mr. Jin | formal-polite and awed | The casualty clerk addresses Jin as 진 선생님 after Jin asks him to list Lei Fei among the dead. |
| 진태경 | 중년인 | celebrated Hunter to older fellow Hunter | sir | casual and teasing | Jin addresses the older Hunter as 아저씨 while joking with him and giving him instructions. |
| 야율목 | 진태경 | Nanman_Beast_Palace_Young_Palace_Lord_to_Han_intruder_and_Murim_Alliance_Pavilion_Master | you | formal but hostile | Asks Jin's identity and orders him to follow after learning he belongs to the Murim Alliance. |
| 진태경 | 야율목 | Fire_Dragon_Pavilion_Pavilion_Master_to_Nanman_Beast_Palace_Young_Palace_Lord | Mok | casual, teasing, and insulting | Calls him rude and later addresses him as 목아 while jokingly claiming they are friends. |
| 진태경 | 야수묘왕 | younger allied master to Ten Kings elder | Great Hero Yayul | urgent and respectful | Uses 야율 대협 while warning the Beast Miao King not to enter the valley. |
| 야수묘왕 | 진태경 | senior allied master to younger allied master | you | informal and cautionary | Warns Taekyung not to lower his guard and to be careful while crossing the swamp. |
| 야율목 | 야수묘왕 | son_to_father | Father | formal and deferential | Yayul Mok calls out to the Beast Miao King after the rescue party arrives. |

## Listed compact profiles

### Beast Miao King.md

# Beast Miao King (야수묘왕)

- **Safe through:** Chapter 666
- **Aliases:** None
- **Role:** The Beast Miao King is the Palace Lord of the Nanman Beast Palace, the great chieftain of the Miao people, a master among the Ten Kings, and one of only two Supreme Peak masters in Nanman.
- **Personality:** The Beast Miao King is fierce and vigilant, yet pragmatic and willing to sacrifice his position to protect Nanman's survival and the greater cause over personal revenge.
- **Voice:** Low, growling, and forceful.
- **Relationships:** He commands the Nanman Beast Palace, is Baeksang's sworn elder brother and childhood companion, lost his children during the Great Faction War, is responsible for the forces stationed at Ailao Mountain, has ordered Ju Hwaran, Song Ilseom, and Hyuk Mujin to investigate the Blood Monk in Guizhou, and met the Martial God twice more than fifty years ago.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 666
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Dogok.md

# Dogok (도곡)

- **Safe through:** Chapter 633
- **Aliases:** None
- **Role:** Dogok is a member of the Beast Miao King's personal guard, the Seven Miao Tigers.
- **Personality:** No personality traits are established.
- **Voice:** No distinctive voice is established.
- **Relationships:** Dogok serves Yayul Cheok as a personal guard.

### Gisan.md

# Gisan (기산)

- **Safe through:** Chapter 633
- **Aliases:** None
- **Role:** Gisan is a member of the Beast Miao King's personal guard, the Seven Miao Tigers.
- **Personality:** No personality traits are established.
- **Voice:** No distinctive voice is established.
- **Relationships:** Gisan serves Yayul Cheok as a personal guard.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 666
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple, the Fire Gate Clan's nineteenth successor, and the Pavilion Master of the Fire Dragon Pavilion within the Murim Alliance; he is a Supreme Peak master with the Heavenly Martial Physique and Force, publicly recognized as an S-rank-level Hunter while formally retaining an A-rank license, and he is currently imprisoned under Baeksang's order with a public execution scheduled for noon in two days.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 666
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Wonhu.md

# Wonhu (원후)

- **Safe through:** Chapter 633
- **Aliases:** None
- **Role:** Wonhu is a member of the Beast Miao King's personal guard, the Seven Miao Tigers.
- **Personality:** No personality traits are established.
- **Voice:** No distinctive voice is established.
- **Relationships:** Wonhu serves Yayul Cheok as a personal guard.

### Yayul Mok.md

# Yayul Mok (야율목)

- **Safe through:** Chapter 666
- **Aliases:** None
- **Role:** Yayul Mok is the non-Han Young Palace Lord of the Nanman Beast Palace, a spear-wielding warrior who rides a white tiger, and a halting but capable speaker of Han Chinese.
- **Personality:** Protective of Nanman Beast Palace livestock, quick-tempered toward trespassers, and capable of restraint once he recognizes legitimate authority.
- **Voice:** Blunt, commanding, and formal-polite toward strangers, becoming openly insulting when provoked.
- **Relationships:** Yayul Cheok is the Beast Miao King and Yayul Mok's father; Yayul Mok is his only surviving son after three older siblings died in the Great Faction War, Baeksang is his father's sworn younger brother, and his white tiger is a long-bonded companion.

## Korean source

```text
＃667화



잠입. 습격. 마무리까지.

전광석화(電光石火)라고 부를 수밖에 없는 일련의 과정은 불과 촌각 동안 이어졌고, 뇌옥 주위를 지키던 스무 명의 전사들은 이 예기치 못한 기습에 속수무책으로 무너졌다.

“치, 침입……!”

쉭, 투둑!

누군가의 입술 사이로 다급히 튀어나온 목소리가 외침이 되기도 전에 사그라졌다.

빛살과도 같은 속도로 상대의 아혈(啞穴)과 훈혈(暈穴)을 연달아 짚은 야율목은, 허물어지는 백족 전사의 신형을 붙잡아 조용히 땅에 눕혔다.

스윽.

실로 간발의 차. 하마터면 일이 크게 어긋날 뻔했다.

“후우.”

참았던 숨을 토해 낸 야율목은 빠르게 주위를 훑었다.

제각각 다른 가면을 쓴 흑의인 이십여 명이 사방을 경계하며 점혈 당한 이들을 풀숲 사이에 숨기는 중이었다.

- 상황 보고하게.

- 전원 제압했습니다.

야율목이 날린 전음에 원숭이 가면을 쓴 이가 대답했다.

그를 비롯한 흑의인 중 일곱 명이 묘족 내에서도 가장 뛰어난 전사들인 칠묘호(七苗虎)라는 사실은, 야수묘왕과 그들만이 아는 비밀이다.

- 어쩐지 한 명이 안 보인다 싶었는데, 숫자를 헤아려 보니 조금 전 소궁주께서 제압한 자가 마지막이었습니다. 아마 근처에서 소피라도 보고 온 모양이죠.

- 우리 측 피해는?

- 전무 합니다.

- 다행이군. 처음부터 일을 그르칠 뻔했어.

- 많이 곤란해졌겠죠.

사실 지금 그들이 하는 일을 생각한다면, 곤란하다는 표현으로도 부족했다.

표면적으로 봤을 때 현재의 진태경은 용서받을 수 없는 중죄를 저지르고 뇌옥에 갇힌 죄인이다.

그런 그를 탈출시키려 했다는 사실이 밝혀진다면, 남만야수궁의 소궁주인 야율목이라 해도 무사하지 못한다.

‘하지만 반드시 해내야 해.’

야율목은 이마에 맺힌 식은땀을 훔치며 마음속으로 중얼거렸다.

비록 아직 어린 나이였지만 그도 알고 있었다. 이것이 얼마나 대범하면서도 위험한 일인지.

그러나 동시에 옳다고 믿었다.

‘진태경은 아군이다. 우리를 돕기 위해 왔고, 애뇌산에서는 위험에 빠진 전사들을 구하기까지 했어.’

야율목은 여느 남만인이 그렇듯 어릴 때부터 한족에 대한 감정이 좋지 않았다.

적어도 진태경과 화룡각 대원들을 만나기 전까지는 그랬다.

물론 진태경을 좋게 생각한다고 해서 한족 전체를 믿게 된 것은 아니었다. 개인은 개인이고, 단체는 단체니까.

하지만 지금 같은 상황에서 무엇이 옳고 그른가에 대해서는 확신할 수 있었다.

존경해 마지않는 자신의 아버지. 야수묘왕처럼.

- 뇌옥을 여는 열쇠는 확보했나?

- 물론입니다.

고개를 끄덕인 원숭이 가면이 손에 든 열쇠 꾸러미를 건넸다.

뇌옥에 들어가기 위해서는 다섯 개의 열쇠를 오차 없이 차례대로 꽂아 기관(機關)을 작동시켜야 했고, 그들은 이미 그 방법을 알고 있었다.

철컥. 구구궁.

둔중한 소음과 함께 움직이는 거대한 철문.

마침내 지하로 내려가는 계단이 드러나자, 야율목과 칠묘호를 포함한 모두가 신속하게 옷을 뒤집었다.

스르륵. 펄럭.

바람에 흔들리는 횃불이 새하얀 옷자락을 비춘다. 순식간에 백족 전사로 탈바꿈한 그들은 아무 일도 없었다는 듯 뇌옥 주위를 경계했다.

적어도 다음 교대가 있을 한 식경 동안, 그들이 이곳을 지킬 것이다.

‘그사이에 아무 일도 없기를 바랄 수밖에.’

사전에 모든 동선과 위치 등을 파악했다고는 해도, 일이 어떻게 흘러갈지는 아무도 모른다.

마음속으로 작게 뇌까린 야율목은 오늘따라 유난히도 낯설게 느껴지는 백의를 입은 채, 칠묘호와 함께 계단을 타고 지하로 향했다.

‘진태경이 갇혀 있는 곳은 사 층.’

장소는 이미 알고 있다. 그리고 일부 간수와 경비 병력이 뇌옥 내부를 지키고 있다는 것 역시도.

그들이 발소리마저 한껏 죽인 채 이동하던 그때. 저 멀리서 희미한 목소리가 들려오기 시작했다.

“빌어먹을. 자네 혹시 속임수 쓴 거 아냐?”

“말도 안 되는 헛소리 좀 하지 말게. 그냥 겸허하게 패배를 인정해.”

“젠장. 이해가 안 되니까 그렇지. 다섯 판 연속으로 진다는 게 말이 되나? 벌써 두 냥이나 잃었어.”

간수들이 심심풀이 삼아 도박을 하는 것은 흔한 일이었고, 이러한 그들의 방심은 침입자들에게 있어 반가운 것이었다.

“염병. 손바닥 뒤집어 봐.”

“어허. 구질구질하긴. 그만 억울해하고 목소리나 좀 줄이게. 안 그래도 저 한족 놈 때문에 윗분들이 촉각을 곤두세우고 있는 와중에 농땡이 피우는 걸 알게 되면…….”

쉬쉭, 투둑!

흐릿한 어둠 속에서 들려오던 목소리가 뚝 끊겼다.

묘족 내에서 손꼽히는 전사들인 칠묘호는 중원에서도 인정받는 절정 고수들.

간수들은 은밀한 접근을 알아차리지 못했고, 순식간에 점혈 당한 그들은 열쇠를 빼앗긴 채 비어 있던 철창 속에 갇혔다.

- 기산. 도곡. 이곳에 남아라.

- 존명.

- 개미 새끼 한 마리 빠져나가지 못하게 하겠습니다.

자리를 비우면 의심을 사기 마련이다.

칠묘호 중 두 사람을 남긴 야율목은 이동 속도를 높였다. 평소의 걸음보다는 빠르게. 그러나 의심을 사지 않을 만큼.

저벅. 저벅.

거대한 미로처럼 얽혀 있는 뇌옥을 가로지르는 여섯 개의 신형.

그러나 야율목의 바람과는 달리, 모든 것이 예상대로 흘러갈 수는 없었다.

“음? 저자들은 누구지?”

진태경이 갇혀 있는 사 층의 경계는 평소와는 비교도 할 수 없을 만큼 삼엄했고, 간수 외에도 뇌옥 내부를 지키는 전사들의 숫자는 결코 적지 않았다.

“거기 자네들. 멈추게.”

순순히 걸음을 멈춘 야율목은, 호흡을 가다듬으며 길을 막고 있는 이들의 숫자를 헤아렸다.

‘도합 스물.’

심지어 그중 다섯은 절정 고수다.

상대가 백족의 정예 전사라는 것을 알아차린 야율목은 태연한 목소리로 대답했다.

쓰고 있던 가면은 이미 벗은 후였고, 개수가 적은 횃불 덕분에 어두컴컴한 뇌옥의 환경은 정체를 숨기기에 안성맞춤이었다.

“대족장님의 지시를 받고 왔소.”

“대족장님?”

조장 격으로 보이는 백족 전사가 짐짓 눈살을 찌푸렸다.

“나가신 지 얼마 되지도 않았는데. 무슨 일인가?”

“크게 중요한 것은 아니오. 혹시 모르니 죄인에게 다시 금력단(禁力丹)을 복용케 하라 하시더군.”

“흠, 그래?”

“아마 탈옥을 우려하신 모양이오. 나 역시 소문으로만 듣긴 했지만, 워낙 괴물 같은 놈이니.”

야율목의 대답을 들은 백족 전사가 피식 웃었다.

“그렇다고 하긴 하더군. 그래 봤자 이제는 죽을 날만 기다리는 놈이지만.”

“나 역시 그렇게 생각하지만, 세상일이라는 게 어찌 될지는 아무도 모르는 거 아니겠소?”

“뭐, 그렇긴 하지. 그나저나 목소리를 들어 보니 젊은 친구 같은데, 교대해 줄 거 아니면 얼른 다녀오게. 반 각 주지.”

“그럴 생각이오.”

아무렇지 않게 어깨를 으쓱해 보인 야율목은, 얼굴을 드러내지 않으려 살짝 고개를 숙인 채 그들을 향해 다가갔다.

그리고 다음 순간, 검갑을 힘주어 붙잡고 있는 어느 전사의 손을 보고 깨달았다.

‘이미 눈치챘……!’

쉬잉! 서걱!

깨달음과 동시에 섬광이 어깨를 스쳤다.

미약한 통증과 함께 솟구치는 몇 방울의 핏물. 야율목이 몸을 비틀며 두 개의 검을 피해 낸 그때, 벽력과도 같은 외침이 뇌옥 전체를 뒤흔들었다.

“침입자! 침입자다!”

삐이이익!

외침과 함께 터져 나온 날카로운 호각 소리. 곳곳에 대기 중이던 전사들의 다급한 발걸음 소리가 적막을 깨트린다.

수많은 기척을 느낀 야율목은 입술을 질끈 깨물며 외쳤다.

“쳐라!”

그와 동시에.

쉬쉬쉬쉭!

야율목의 등 뒤에서 눈부신 검광(劍光)이 쏟아져 내렸다. 어두컴컴한 불빛 속에서 얽혀든 병장기가 위태롭게 흔들렸다.

캉! 차차창!

서걱!

“크악!”

순식간에 십여 개의 병장기가 부딪치고, 핏물과 비명이 터져 나왔다.

곧이어 앞서 간수로 위장시킨 두 사람까지 상황의 위급함을 알아차리고 가세하자, 불과 찰나의 시간 동안 스물에 달하던 백족 전사들의 절반이 부상을 입고 쓰러졌다.

하지만…….

삐익! 삐이익-!

“무슨 수를 써서라도 막아! 놈들의 목표는 진태경이다!”

“숫자가 적다! 될 수 있으면 사로잡아라!”

경계는 그들이 입수했던 정보보다 훨씬 더 삼엄했다.

하나가 쓰러지면 다섯이, 다섯을 쓰러트리면 열이 늘어나는 상황.

더군다나 진태경을 탈옥시키는 과정에서 같은 남만인을 죽이지 않기로 맹세한 야율목 일행에게는 첩첩산중이나 다름없었다.

쉬쉬쉬쉭!

“계속해서 밀어붙여라!”

사방에서 짓쳐 드는 백족 전사들과 예리하게 날 선 병장기.

순식간에 오십여 명이 넘는 적들에게 둘러싸인 야율목과 칠묘호는 이를 악물고 맞섰다.

차차차창!

서걱!

그러나 그들의 바람과 현실의 차이는 명백했다.

끊임없이 몰려드는 적들은 중과부적(衆寡不敵)이라는 네 글자를 떠올리게 했고, 그 사이사이에 섞여 있는 절정 고수들이 쏘아 보내는 한 수, 한 수는 위협적이기 그지없었다.

쉬쉭, 푹!

“큭!”

갈수록 늘어나는 자잘한 상처와 계속되는 출혈.

야율목과 칠묘호가 쓰러트린 백족 전사의 숫자는 결코 적지 않았지만, 지금 이 순간에도 적들의 머릿수는 계속해서 늘어나고 있었다.

마침내 다른 층에서 대기하고 있던 경비 병력까지 합세한 것이다.

‘빌어먹을.’

어느새 야율목의 등허리는 식은땀으로 축축하게 젖어 있었다.

생각처럼 일이 쉽게 풀리지 않을 거라는 사실은 이미 알고 있었다. 그러나 너무 일찍 발각되었을뿐더러, 뇌옥의 경계는 그가 입수한 정보보다 훨씬 더 삼엄했다.

‘만약 이곳에서 사로잡히기라도 한다면…….’

그때는 모든 상황이 최악으로 치닫는다.

남만야수궁의 소궁주인만큼 목숨을 잃지는 않겠지만, 아버지인 야수묘왕의 정치적 입지는 물론 애당초 목표였던 진태경과 화룡각 대원들은 형장의 이슬로 사라질 것이다.

‘그리고 전쟁이 시작되겠지.’

과거 마교에 맞서 참가했던 정마대전이 아닌, 중원 무림과의 전쟁.

진태경이 죽는다면 그때는 그 무엇도 돌이킬 수 없다.

더불어 그것이야말로 두 부자(父子)가 위험을 무릅쓰고 진태경을 구출하고자 하는, 가장 큰 이유 중 하나였다.

‘어쩔 수 없다.’

피가 나도록 입술을 깨문 야율목이 입술을 달싹였다.

- 원후(猿猴). 부탁한다.

짧은 전음이었지만, 그것으로 충분했다.

칠묘호의 맏형이자, 원숭이 가면을 쓰고 있던 중년인이 검을 흩뿌리며 외쳤다.

“길을 열어라!”

이렇게 된 이상 답은 하나뿐이었다.

목숨을 도외시한 돌파(突破). 그리고 진태경의 구출.

그것이 이 자리의 모두가 위험을 감수하고 이곳에 온 이유였고, 야율목이 생각한 이 상황을 타개할 하나뿐인 방책이었다.

‘진태경. 그가 뇌옥을 빠져나온다면 모두 해결할 수 있다.’

야율목은 품 안에 들어있는 단단한 목갑(木匣)을 더듬었다.

전투가 벌어지기 직전, 진태경에게 금력단을 복용시키고자 왔다고 했던 그의 말은 완전히 틀린 것이 아니었다.

단지 그것이 금력단이 아닌, 공력의 금제를 푸는 해약(解藥)이었을 뿐이다.

차차차창!

푸푹! 서걱!

“크악!”

패색이 짙은 상황 속에서, 뇌옥의 복도가 그리 넓지 않다는 것은 그들에게 있어 유일한 장점이었다.

사방에서 쏟아지는 공격을 무시하며 일점을 파고든 야율목과 칠묘호의 눈앞에, 마침내 어둑한 복도가 기다리고 있었다.

“가시오! 어서!”

충복의 다급한 외침을 뒤로 한 채, 야율목은 온 힘을 끌어올려 신형을 날렸다.

아니, 날리려고 했다.

쉬쉬쉭! 덥석!

다음 순간. 어둠 속에서 뻗어 나온 누군가의 손이 그의 어깨를 붙잡지 않았다면 그랬을 것이다.

“어디 가냐. 바쁜 일 있어?”

“……!”

아주 잠깐, 주위에서 벌어지고 있는 모든 상황을 떠나 침묵하던 야율목이 입을 열었다.

“……네가 왜 거기서 나와?”
```

## Final English reading copy

```markdown
# Chapter 667

Infiltration. Assault. Cleanup.

The sequence of events could only be described as a Quick Attack. It lasted no more than a few moments, and the twenty warriors guarding the area around the underground prison collapsed helplessly before the unexpected ambush.

“I-I—intruders…!”

Sssht—thud!

The urgent voice that burst from someone’s lips died out before it could become a shout.

Moving with the speed of a streak of light, Yayul Mok struck the Mute Acupoint and Dizziness Acupoint one after another. Then he caught the collapsing Bai warrior and quietly lowered him onto the ground.

Sss.

It had truly been a close call. The entire operation had nearly gone badly.

“Whew.”

Yayul Mok exhaled the breath he had been holding and swiftly scanned his surroundings.

Around twenty black-clad figures, each wearing a different mask, kept watch in every direction while hiding those whose pressure points had been sealed among the grass.

—Report.

—Everyone has been subdued.

A man wearing a monkey mask answered Yayul Mok through Sound Transmission.

The fact that he and six of the other men in black were the Seven Miao Tigers, the most outstanding warriors among the Miao people, was a secret known only to them and the Beast Miao King.

—I thought one person was missing. But after counting the numbers, the last one was the man the Young Palace Lord subdued a moment ago. He must have gone nearby to relieve himself.

—Any casualties on our side?

—None.

—Good. We nearly ruined everything before we even began.

—It would have caused quite a problem.

In truth, considering what they were doing, even calling it a problem was an understatement.

On the surface, Jin Taekyung was a criminal imprisoned in the underground prison after committing an unforgivable felony.

If it became known that they had tried to help him escape, even Yayul Mok, the Young Palace Lord of the Nanman Beast Palace, would not escape unscathed.

*But we have to do it.*

Yayul Mok wiped the cold sweat from his forehead and muttered inwardly.

He was still young, but he understood how audacious—and dangerous—this was.

At the same time, he believed it was right.

*Jin Taekyung is an ally. He came here to help us, and he even rescued warriors who were in danger on Ailao Mountain.*

Like any Nanman native, Yayul Mok had disliked the Han Chinese from a young age.

At least, he had until he met Jin Taekyung and the members of the Fire Dragon Pavilion.

Of course, thinking well of Jin Taekyung did not mean he trusted all the Han Chinese. An individual was an individual, and a group was a group.

But in a situation like this, he was certain of what was right and wrong.

Just like his own father, the Beast Miao King, whom he respected beyond measure.

—Did you secure the keys to open the underground prison?

—Of course.

The man in the monkey mask nodded and handed over the bundle of keys in his hand.

To enter the underground prison, five keys had to be inserted in the correct order without a single mistake to activate the mechanism. They already knew how to do it.

Click. Groooan.

A massive iron door moved with a heavy rumble.

At last, when the staircase leading underground was revealed, everyone—including Yayul Mok and the Seven Miao Tigers—quickly turned their clothes inside out.

Sssht. Flutter.

Torchlight swaying in the wind illuminated their pure-white clothes. In an instant, they had transformed into Bai warriors, and they stood guard around the underground prison as though nothing had happened.

They would guard this place for at least half an hour, until the next shift arrived.

*All we can do is hope nothing happens in the meantime.*

Even though they had studied every route and position in advance, no one knew how things would unfold.

Muttering quietly to himself, Yayul Mok descended underground with the Seven Miao Tigers, wearing the white uniform that felt especially unfamiliar today.

*Jin Taekyung is on the fourth floor.*

He already knew the location. He also knew that some of the wardens and guards were stationed inside the underground prison.

Just as they moved with even their footsteps suppressed as much as possible, faint voices began to reach them from far away.

“Damn it. Did you cheat somehow?”

“Don’t talk such ridiculous nonsense. Just humbly admit defeat.”

“Shit. I’m only saying this because I don’t understand. How can someone lose five games in a row? I’ve already lost two nyang.”

It was common for wardens to gamble to pass the time, and their carelessness was welcome news for the infiltrators.

“Damn it. Turn your palm over.”

“Good grief. What a sore loser. Stop feeling wronged and lower your voice. The higher-ups are already on edge because of that Han Chinese bastard. If they find out we’ve been slacking off…”

Sssht—thud!

The voices coming from the hazy darkness abruptly stopped.

The Seven Miao Tigers were warriors counted among the very best of the Miao people, and even the Central Plains recognized them as Peak masters.

The wardens failed to notice their silent approach. After being subdued in an instant, they were stripped of their keys and locked inside an empty cell.

—Gisan. Dogok. Stay here.

—Yes, sir.

—We won’t let even a single ant slip through.

Leaving the post unattended would naturally arouse suspicion.

Yayul Mok left two of the Seven Miao Tigers behind and increased his pace. Faster than an ordinary walk, but not so fast as to invite suspicion.

Step. Step.

Six figures crossed the underground prison, which twisted like a massive maze.

But contrary to Yayul Mok’s hopes, not everything could go according to plan.

“Hmm? Who are those men?”

The security on the fourth floor, where Jin Taekyung was imprisoned, was incomparably tighter than usual. In addition to the wardens, there were quite a few warriors guarding the interior of the underground prison.

“You there. Stop.”

Yayul Mok obediently halted and counted the men blocking their path while steadying his breathing.

*Twenty in total.*

Five of them were even Peak masters.

Realizing that his opponents were elite Bai warriors, Yayul Mok answered in a calm voice.

The mask Yayul Mok had been wearing was already off, and with only a few torches burning, the dim underground prison was ideal for concealing his identity.

“We came at the command of the Great Chieftain.”

“The Great Chieftain?”

The Bai warrior who appeared to be their captain deliberately furrowed his brow.

“He only left a short while ago. What is this about?”

“It is nothing particularly important. He told us to make the criminal take another Force-Sealing Pill, just in case.”

“Hm. Is that so?”

“He must be worried about an escape attempt. I have only heard rumors myself, but apparently the man is a monster.”

The Bai warrior let out a short laugh at Yayul Mok’s answer.

“That is what I’ve heard. But now he is merely a man waiting for the day he dies.”

“I think so as well, but no one knows how things will turn out in this world, do they?”

“Well, that is true. In any case, judging by your voice, you seem young. If you are not here to take over our shift, hurry along. I’ll give you a quarter of an hour.”

“That was our intention.”

Yayul Mok casually shrugged and approached them with his head slightly lowered so they would not see his face.

And then he saw the hand of one of the warriors gripping his scabbard tightly.

*They already noticed us…!*

Shing! Slice!

At the same instant he realized it, a flash of light grazed his shoulder.

A few drops of blood sprang into the air along with a faint sting. Yayul Mok twisted his body and evaded two swords. Then an explosive shout shook the entire underground prison.

“Intruders! We have intruders!”

Peeeeep!

A sharp whistle burst out alongside the shout. The urgent footsteps of warriors waiting throughout the underground prison shattered the silence.

Feeling countless presences, Yayul Mok clenched his teeth and shouted.

“Attack!”

At the same time—

Sssshh-shing!

Brilliant sword light poured down from behind Yayul Mok. Weapons tangled dangerously beneath the dim torchlight.

Clang! Clang-clang!

Slice!

“Gah!”

Around ten weapons collided in an instant, followed by bursts of blood and screams.

Soon, the two men they had disguised as wardens realized how dire the situation was and joined the battle. In the space of a few moments, half of the nearly twenty Bai warriors had been wounded and knocked down.

But…

Peep! Peeeeep!

“Stop them by any means necessary! Their target is Jin Taekyung!”

“There aren’t many of them! Capture them if possible!”

The security was far tighter than the information they had obtained suggested.

Whenever one man fell, five more appeared. Whenever five were knocked down, ten took their place.

What was more, Yayul Mok and his men had sworn not to kill fellow Nanman people while rescuing Jin Taekyung. For them, it was one impossible hurdle after another.

Sssshh-shing!

“Keep pressing forward!”

Bai warriors charged in from every direction, their weapons sharpened to deadly points.

Yayul Mok and the Seven Miao Tigers were surrounded by more than fifty enemies in an instant, but they gritted their teeth and fought back.

Clang-clang-clang!

Slice!

But the difference between their hopes and reality was obvious.

The enemies continued to pour in without end, bringing the four characters *the many defeat the few* to mind. And the attacks launched by the Peak masters mixed among them were terrifyingly dangerous.

Sssht—thunk!

“Ugh!”

Small wounds continued to accumulate, and the bleeding continued.

Yayul Mok and the Seven Miao Tigers had knocked down no small number of Bai warriors, but even now, the enemy’s numbers kept growing.

At last, the guards stationed on the other floors had joined the fight as well.

*Damn it.*

By then, Yayul Mok’s back was damp with cold sweat.

He had already known that things would not go as smoothly as he hoped. But they had been discovered far too early, and the security around the underground prison was much tighter than the information he had received indicated.

*If we get captured here…*

Then the entire situation would spiral into the worst possible outcome.

As the Young Palace Lord of the Nanman Beast Palace, Yayul Mok would not lose his life. But his father, the Beast Miao King, would lose his political standing, while Jin Taekyung and the Fire Dragon Pavilion members—the original targets of the rescue—would be sent to the execution ground.

*And war will begin.*

Not the Great Faction War in which they had once fought against the Demonic Cult, but a war against the Murim of the Central Plains.

If Jin Taekyung died, nothing could be undone after that.

And that was one of the greatest reasons the father and son were risking their lives to rescue him.

*There’s no other choice.*

Yayul Mok bit his lips until they bled and moved them.

—Wonhu. I’m counting on you.

It was a short message through Sound Transmission, but it was enough.

The middle-aged man wearing the monkey mask—the eldest brother of the Seven Miao Tigers—scattered his sword strikes and shouted.

“Open a path!”

Now that things had come to this, there was only one answer.

A breakthrough that disregarded their lives. And Jin Taekyung’s rescue.

That was why everyone here had come despite the danger, and the only way Yayul Mok could think of to overcome this situation.

*Jin Taekyung. If he gets out of the underground prison, everything can be resolved.*

Yayul Mok felt the solid wooden case inside his robes.

The claim he had made just before the battle broke out—that he had come to give Jin Taekyung a Force-Sealing Pill—had not been entirely false.

It was simply not a Force-Sealing Pill. It was an antidote that would release the seal on his internal energy.

Clang-clang-clang!

Thrust! Slice!

“Gah!”

The fact that the underground prison’s corridors were narrow was their only advantage in their increasingly desperate situation.

Ignoring the attacks pouring in from every direction, Yayul Mok and the Seven Miao Tigers forced their way toward a single point. At last, a dark corridor appeared before them.

“Go! Hurry!”

Leaving behind the urgent cry of their loyal retainer, Yayul Mok drew up every ounce of his strength and launched himself forward.

Or he tried to.

Sssshh-shing! Grab!

The next moment, someone’s hand reached out of the darkness and caught him by the shoulder.

Without that, he would have.

“Where are you going? Got somewhere to be?”

“……!”

For a brief moment, Yayul Mok fell silent, ignoring everything happening around him. Then he opened his mouth.

“…Why are you coming out of there?”
```

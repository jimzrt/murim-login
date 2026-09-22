<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0670.txt",
      "sha256": "7d1a7f42da66e7706fc897e76f7039b494c8fa3fc30222564364effe191bcfc9",
      "bytes": 13206
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "d47cde65df2a4776909073d061cd223a87b278344bdcabe0325b4d3c0c223d44",
      "bytes": 2114
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "90fbc5af66a53c979eb81e4f99d3a7bf49ae990d077ae46d7867ad560fdaf362",
      "bytes": 202324
    },
    {
      "path": "characters/Baeksang.md",
      "sha256": "198cdef8a8c849f8532f013ee87b90345c41c2f9aed769d1579fb6a09f883cdd",
      "bytes": 1050
    },
    {
      "path": "characters/Beast Miao King.md",
      "sha256": "0020869ffa60e89b270eb794eb86dff7b562aefb70d3be19adf291e20c88255f",
      "bytes": 830
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "a833b85fc6960d1b650cc6919868800b0750fce77aa88510279bb0f196dd734e",
      "bytes": 553
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "c6d1815a0de97384295905df1ee3239e27ff30c53b44bea42623e4d9f75629f1",
      "bytes": 1858
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "58a84342828c1f8a77912e7c29fec233434e551672dfcf95d82292fdaa71df81",
      "bytes": 622
    },
    {
      "path": "characters/Wonhu.md",
      "sha256": "965a76e1e6640dcfb209e04294511ebc09c37251ef71ca911a3ae6414e12b74a",
      "bytes": 415
    },
    {
      "path": "characters/Yayul Mok.md",
      "sha256": "2068114ce068f17de7c6b64fae267009e782b624d67e618fa7b3fc98bc6b8894",
      "bytes": 869
    },
    {
      "path": "characters/Yohi.md",
      "sha256": "cbb93e2dee7d4ee0520270f8883d725bdb3156b4104668e2e9ef4e2bc659f9f3",
      "bytes": 645
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "28f5d6efc67971f1a1312c4efa0689578fe81890e1c6f610b6860ed8fa2de0dc",
      "bytes": 207911
    }
  ],
  "estimated_tokens": 11439
}
-->

# Durable State Update — Chapter 670

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 670. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 670. Profile updates may replace only one
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
  "chapter": 670,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 670,
    "continuity_sources": [670],
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
    "Jin has escaped the underground prison and completed the Escape from Namshank Quest before the scheduled execution.",
    "The Quest Reward granted Jin a Level Up, removed some injuries and Status Effects, and released the force constricting his Lower Dantian.",
    "Jin still has not fully understood the insufficient power of his Middle Dantian.",
    "Taishan, Yayul Mok, and the Seven Miao Tigers enabled the escape, while the surrendered Bai warriors survived and were confined.",
    "Namho and Sama Pyo were rescued from the Inner Palace; Sama Pyo received an antidote but cannot yet fight at full strength.",
    "Yayul Mok gave Muyaho to Jin and directed him northeast toward the reconnaissance squad.",
    "Yayul Mok and the Seven Miao Tigers remain behind to delay discovery for as long as possible.",
    "Yayul Mok collapsed as Wonhu caught him and entrusted him to Jin's care.",
    "Baeksang and the Tribal Grand Council's response to the defiance of the execution order remains unresolved."
  ],
  "continuity_sources": [
    669,
    668
  ],
  "open_questions": [
    "Can Jin, Taishan, Namho, Sama Pyo, and Muyaho reach the reconnaissance squad and escape Nanman?",
    "Will Yayul Mok and the Seven Miao Tigers survive after remaining behind to delay pursuit?",
    "What punishment will Baeksang and the Tribal Grand Council impose after the rescue is exposed?",
    "What is the exact source and limit of Jin's Middle Dantian force?",
    "How fully will Jin's restored condition affect his ability to fight and escape?"
  ],
  "safe_through": 669,
  "temporary_decisions": [
    "Use Great Chieftain for 대족장 and Escape from Namshank for 남생크.",
    "Use Deputy Stronghold Lord for 부채주 and Stronghold Lord for 채주.",
    "Use underground prison for 뇌옥 and Dizziness Acupoint for 훈혈.",
    "Capitalize Will for 의지; use Middle Dantian for 중단전 and Seizing an Object Through Empty Space for 허공섭물.",
    "Use half a shichen for 반 시진, Lower Dantian for 하단전, and antidote for 해약."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 암천     | **Dark Heaven**                  |
| 남만야수궁  | **Nanman Beast Palace**          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 퀘스트              | **Quest**                      |
| 백상 | **Baeksang** | Great chieftain of the Bai people and Yayul Cheok's sworn younger brother. |
| 야수묘왕 | **Beast Miao King** | Leader of the Miao people and master of the Nanman Beast Palace. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 원후 | **Wonhu** | Named member of the Beast Miao King's personal guard, the Seven Miao Tigers. |
| 야율목 | **Yayul Mok** | Young Palace Lord of the Nanman Beast Palace. |
| 요희 | **Yohi** | Female great chieftain of the Yao people. |
| 추종향 | **tracking scent** | Scent used to guide the messenger hawk. |
| 검강 | **Sword Force** | Higher manifestation than Sword Energy; Pung Yang's is explicitly imperfect because of insufficient enlightenment. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 한족 | **Han Chinese** | Ethnic designation used by the steppe chieftains. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 박도 | **broad-bladed saber** | Rough weapon swung by the bald swordsman. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 천라지망 | **net over heaven and earth** | Jeok Cheongang's figurative threat to pursue a culprit everywhere. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 뇌옥 | **underground prison** | The Tang Clan's subterranean prison. |
| 묘족 | **Miao people** | Ethnic group the Escort Bureau expects to encounter near Yunnan. |
| 촌각 | **moments** | Short intervals disappearing from Jeok's day. |
| 화룡각 | **Fire Dragon Pavilion** | New name chosen for Taekyung's pavilion. |
| 영물 | **spiritual creature** | Known non-human creature contrasted with unheard-of monsters. |
| 성하 | **Seongha** | Hunter named during the cave battle. |
| 백족 | **Bai people** | Ethnic group encountered in Yeongin. |
| 백호 | **White Tiger** | Yayul Mok's tiger companion. |
| 칠묘호 | **Seven Miao Tigers** | The Beast Miao King's personal guard, composed of elite Miao warriors. |
| 야율 | **Yayul** | Name used in Taekyung's colloquial address to the Beast Miao King. |
| 외궁 | **Outer Palace** | The outer compound of the Nanman Beast Palace. |
| 대족장 | **Great Chieftain** | Title used for the senior Nanman leader who supposedly ordered the inspection. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 야율목 | 진태경 | Nanman_Beast_Palace_Young_Palace_Lord_to_Han_intruder_and_Murim_Alliance_Pavilion_Master | you | formal but hostile | Asks Jin's identity and orders him to follow after learning he belongs to the Murim Alliance. |
| 진태경 | 야율목 | Fire_Dragon_Pavilion_Pavilion_Master_to_Nanman_Beast_Palace_Young_Palace_Lord | Mok | casual, teasing, and insulting | Calls him rude and later addresses him as 목아 while jokingly claiming they are friends. |
| 야율목 | 백상 | nephew_to_father's_sworn_younger_brother | Uncle Baeksang | ceremonial and deferential | Yayul Mok formally greets Baeksang as he arrives at the stone door. |
| 백상 | 야율목 | father's_sworn_brother_to_nephew | you | cold and formal | Baeksang questions Yayul Mok about his return, the pasture fire, and the Palace Lord's whereabouts. |
| 야수묘왕 | 백상 | sworn_older_brother_to_sworn_younger_brother | Baeksang | familiar and bittersweet | Yayul Cheok offers Baeksang his preferred fruit wine and asks why he came. |
| 요희 | 진태경 | Yao great chieftain to Murim Alliance pavilion master | Jin Taekyung | casual and probing | Identifies him by his full name while allowing him to keep the mask on. |
| 진태경 | 요희 | Fire Dragon Pavilion pavilion master to Yao great chieftain | you | guarded and blunt | Answers Yohi's probing questions directly while warning her about Ju Hwaran. |
| 백상 | 요희 | Bai great chieftain to Yao great chieftain | Yohi | cold and formal | Calls to Yohi from outside the tent at the chapter's end. |
| 백상 | 진태경 | Nanman great chieftain to Murim Alliance Pavilion Head | you bastard | cold, hostile, and contemptuous | Baeksang calls Jin a Han Chinese man, rejects his status, and orders him to leave. |
| 진태경 | 백상 | Murim Alliance Pavilion Head to Nanman great chieftain | you | polite but deliberately provocative | Jin tells Baeksang that Nanman's blood was shed for the world rather than merely for the Central Plains. |
| 진태경 | 야수묘왕 | younger allied master to Ten Kings elder | Great Hero Yayul | urgent and respectful | Uses 야율 대협 while warning the Beast Miao King not to enter the valley. |
| 진태경 | 백호 | human ally to intelligent spiritual beast | you | casual and familiar | Converses with White Tiger after interpreting its warning. |
| 야수묘왕 | 진태경 | senior allied master to younger allied master | you | informal and cautionary | Warns Taekyung not to lower his guard and to be careful while crossing the swamp. |
| 야율목 | 야수묘왕 | son_to_father | Father | formal and deferential | Yayul Mok calls out to the Beast Miao King after the rescue party arrives. |
| 백상 | 야수묘왕 | Nanman great chieftain to the Nanman Beast Palace Lord | Palace Lord | restrained and apologetic | Apologizes for causing the disturbance after the Beast Miao King stops the fight. |
| 야율목 | 원후 | Young_Palace_Lord_to_elder_personal_guard | Wonhu | formal-commanding | Calls on Wonhu to open a path through the surrounding guards. |
| 원후 | 진태경 | elder personal guard to trusted ally | you | formal and deferential | Wonhu addresses Jin while entrusting the collapsed Young Palace Lord to him. |

## Listed compact profiles

### Baeksang.md

# Baeksang (백상)

- **Safe through:** Chapter 669
- **Aliases:** None
- **Role:** Baeksang is the middle-aged great chieftain of the Bai people, one of Nanman's four most powerful great tribes, and one of only two Supreme Peak masters in Nanman.
- **Personality:** Cold, rigid, meticulous, politically resolute, and strategically manipulative, with enduring grief over Hwi's death and a guarded but still powerful bond with his sworn elder brother that now leaves him visibly conflicted.
- **Voice:** Rigid, formal, restrained, and emotionally distant.
- **Relationships:** Baeksang is Yayul Cheok's sworn younger brother and childhood companion, Yayul Mok's sworn uncle, and the father of his deceased only child Baekhwi, whom the Great Snow Fiend killed during the Great Faction War; he opposes the Nanman Beast Palace joining the Murim Alliance, distrusts the Central Plains because of the alleged wartime betrayal, and is alleged by Heugung to have colluded with Dark Heaven.

### Beast Miao King.md

# Beast Miao King (야수묘왕)

- **Safe through:** Chapter 667
- **Aliases:** None
- **Role:** The Beast Miao King is the Palace Lord of the Nanman Beast Palace, the great chieftain of the Miao people, a master among the Ten Kings, and one of only two Supreme Peak masters in Nanman.
- **Personality:** The Beast Miao King is fierce and vigilant, yet pragmatic and willing to sacrifice his position to protect Nanman's survival and the greater cause over personal revenge.
- **Voice:** Low, growling, and forceful.
- **Relationships:** He commands the Nanman Beast Palace, is Baeksang's sworn elder brother and childhood companion, and is Yayul Mok's father while jointly risking their positions to rescue Jin Taekyung and prevent war with the Central Plains.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 669
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 668
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple, the Fire Gate Clan's nineteenth successor, and the Pavilion Master of the Fire Dragon Pavilion within the Murim Alliance, a Supreme Peak master with the Heavenly Martial Physique and Force, a publicly recognized S-rank-level Hunter who formally retains an A-rank license, and an escaped prisoner still facing public execution at noon in two days.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 668
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Wonhu.md

# Wonhu (원후)

- **Safe through:** Chapter 669
- **Aliases:** None
- **Role:** Wonhu is the eldest member of the Seven Miao Tigers, the Beast Miao King's personal guard.
- **Personality:** No personality traits are established.
- **Voice:** No distinctive voice is established.
- **Relationships:** Wonhu serves Yayul Cheok as a personal guard.

### Yayul Mok.md

# Yayul Mok (야율목)

- **Safe through:** Chapter 669
- **Aliases:** None
- **Role:** Yayul Mok is the non-Han Young Palace Lord of the Nanman Beast Palace, a spear-wielding warrior who rides a white tiger, and a halting but capable speaker of Han Chinese.
- **Personality:** Protective of Nanman Beast Palace livestock, quick-tempered toward trespassers, and capable of restraint once he recognizes legitimate authority.
- **Voice:** Blunt, commanding, and formal-polite toward strangers, becoming openly insulting when provoked.
- **Relationships:** Yayul Cheok is the Beast Miao King and his father, Baeksang is his father's sworn younger brother, and Yayul Mok has risked his position and life to rescue Jin Taekyung, entrusting Muyaho to Jin while he remains behind with the Seven Miao Tigers.

### Yohi.md

# Yohi (요희)

- **Safe through:** Chapter 666
- **Aliases:** None
- **Role:** Yohi is the female great chieftain of the Yao people, one of Nanman's four great tribes.
- **Personality:** Yohi's public presence is charismatic and captivating, drawing widespread admiration and affection.
- **Voice:** Not established.
- **Relationships:** Yohi leads the Yao people, seeks to unite Nanman's four great tribes under Yao leadership, manipulates Heugung alongside Baeksang, and has disappeared from the Inner Palace alongside Heugung after the assault on the Fire Dragon Pavilion.

## Korean source

```text
＃670화



짧지만 긴 시간이었다.

촌각(寸刻)이 칠주야(七晝夜)처럼 느껴질 만큼.

지난 수십여 년의 세월을 하나하나 되짚으며 걷고, 산고를 견디지 못해 숨이 끊인 어미의 품에서 울던 핏덩이가 훌쩍 자라나 헌앙한 청년이 되는 것을 지켜볼 수 있을 만큼.

이렇듯 백상의 고민은 짧으면서도 길었고, 길면서도 짧았다.

그리고 굳게 닫혀 있던 그의 입술이 침묵을 깨트리며 움직였을 때, 고민에 대한 답은 이미 나와 있었다.

“후회할 겁니다.”

야수묘왕이 담담하게 되물었다.

“무엇을 말하는 것이냐. 너를 찾아온 것을? 아니면 진태경을 비롯한 다른 한족들을 구출한 것을?”

“지금까지의 모든 것을.”

“백상, 너처럼 말이냐?”

“다릅니다.”

백상이 굳은 얼굴로 말을 이었다.

“저와 달리 궁주께는 아직 기회가 남아 있습니다. 실수를 되돌릴 수 있는 마지막 기회가.”

“마지막 기회라…….”

“이대로 조용히 돌아가신다면, 이 자리에서 보고 들은 것들은 모두 잊겠습니다. 마치 아무 일도 없던 것처럼.”

“어찌 손바닥으로 하늘을 가릴까. 뇌옥을 지키던 네 수하들을 살려 두라 말했을 때부터 이미 각오하고 있었다.”

“그들에게 함구하라 명령한다면 따를 것입니다. 저를 향한 백족의 충심(忠心) 또한 궁주께서 거느리신 칠묘호에 지지 않으니.”

“그것이…… 네가 보일 수 있는 의형제로서의 마지막 정이냐?”

묵묵히 고개를 끄덕이는 백상을 향해, 야수묘왕은 서글픈 웃음을 지어 보였다.

“그럼 그 마지막 정에 기대어 다시 한번 부탁하마. 반 시진. 반 시진만이라도 그들을 위해 길을 열어 주어라.”

“궁주!”

“설령 돌이킬 수 있다 해도, 돌이키지 않겠다. 그것이 평생을 함께한 우리의 유일한 차이점이지.”

“……!”

백상의 눈꼬리가 파르르 떨렸다.

지금 이 순간 그는 온 힘을 다해 부정하고 싶었다. 당신의 말은 틀렸다고. 당신과 달리 내 앞에는 단 하나의 길만 놓여 있었고, 그 길을 걸을 수밖에 없었다고.

그러나 이미 굳게 다물어진 입술은 열리지 않았고, 그의 손은 어느덧 검자루에 닿아 있었다.

철컥. 스르릉.

짧은 적막을 베어 가르는 서늘한 마찰음. 애검을 늘어트린 백상의 모습을 바라보는 야수묘왕의 눈빛이 깊게 가라앉았다.

“그래. 그것이 네 선택이냐?”

“어쩔 수 없소, 궁주. 지금의 내게는…… 이것만이 최선이니까.”

“어설픈 존대를 듣지 않아도 되니 한결 낫군. 마치 오래전으로 돌아간 것 같아.”

“궁주도 알고 있지 않소. 우리는 두 번 다시 그 시절로 돌아갈 수 없다는 것을.”

“그리 생각하느냐?”

“물론.”

그 단호한 대답에 야수묘왕은 희미하게 웃었고, 결단을 내린 백상은 망설이지 않았다.

츠츠츠츠!

온 사방을 밝히는 휘황한 빛무리. 검강(劍罡)이라 불리는 아득한 기의 집합체가, 목표를 향해 떨어져 내렸다.

서걱!



* * *



눈처럼 새하얀 백호를 필두로 세 마리의 호랑이는 바람처럼 달려 나갔다.

칠묘호의 맏이, 원후(猿猴)는 이미 어둠 너머로 사라진 그들의 뒷모습을 바라보며 중얼거렸다.

“어따, 빠르다.”

소감은 그것이 전부였다.

떠날 이들은 떠났고, 남은 이들은 남았다. 그를 비롯한 다른 이들은 후자가 되기를 스스로 선택했을 뿐이다.

“흐흐.”

원후는 후련한 웃음과 함께 품 안에서 호리병을 꺼냈다.

퐁.

마개를 따기 무섭게 퍼져 나가는 주향. 주위에 있던 묘족 전사들이 동시에 눈을 빛냈다.

“오호.”

“주향 한번 끝내주네. 대형께서 직접 담근 겁니까?”

“허어, 개새끼들만 모아 놨나. 왜 이리들 코가 좋아?”

입으로는 투덜거려도 눈은 웃고 있다. 원후는 어쩔 수 없다는 듯이 모여든 이들에게 호리병을 돌렸다.

“어쩔 수 없군. 얼마 안 되니까 돌아가면서 조금씩 마셔라.”

“내 맹세컨대, 대형 입에는 술 한 방울도 안 들어갈 거요.”

“아, 이건 못 참지.”

껄껄 웃은 묘족 전사들은 순서대로 호리병을 기울였다.

가뜩이나 술 좋아하기로 유명한 남만인들. 그것도 장정이 스물이나 되니 술 한 방울 안 남을 거라는 호언장담은 상당한 신빙성이 있었다.

하지만…….

“크으, 좋다. 이제 대형 차례요. 내 예의상 몇 방울 남겨 뒀지.”

마침내 호리병을 받아 든 원후는 피식 웃고 말았다.

찰랑.

작게 흔들어 본 것만으로도 알 수 있었다. 호리병 안의 술이 채 반도 비워지지 않았다는 것을.

술맛이 좋다며 뻔뻔하게 너스레를 떨고 있는 녀석들을 보고 있자니 실소가 절로 흘러나왔다.

“이거 알고 보니, 개새끼들이 아니라 순 허풍쟁이들이었군.”

“음? 그게 무슨 소리요?”

“그러게. 나이 오십 줄에 벌써부터 노망이라도 나셨나?”

“헛소리 그만하고 들기나 하시오.”

주위의 성화에 원후는 호리병을 기울였다. 자신의 입 안이 아니라, 잡초가 무성하게 자라 있는 땅을 향해.

주르륵.

“한 방울도 아까워하지 마라. 살아남는다면 모두가 둘러앉아 밤새도록 술잔을 기울일 테고, 이 자리에서 쓰러진다면 죽어서도 취할 수 있을 테니.”

“……!”

“……!”

굳은 얼굴로 그 모습을 지켜보던 이들이 슬쩍 입꼬리를 끌어올렸다.

“그래, 그거 좋지.”

“대형께서 뭘 좀 아시네.”

“하긴, 전부터 무공보다는 술에 더 미쳐 있긴 했지. 안 그런가?”

원후도 웃고, 그와 일평생을 함께한 칠묘호도 웃고, 위험한 임무에 기꺼이 자원한 묘족 전사들도 웃었다.

후회? 추호도 없다.

설령 모두가 이 자리에서 죽는다 하더라도, 그들의 유일한 희망은 살아남아 위험을 빠져나갈 테니까.

그렇기에 원후는 기꺼이 웃을 수 있었다.

언제나 모든 일에 앞장섰으며, 솔선수범을 위해 당신의 하나뿐인 후계자마저 이곳으로 보낸 한 사람을 떠올리며.

‘명령을 어긴 죄는…… 훗날 저승에서 달게 받겠습니다, 주군.’

야수묘왕은 물론 야율목 역시 죽음을 두려워하지 않는다.

그들은 수하를 방패를 내세우지도, 그렇다고 겁에 질려 뒷걸음질 치지도 않았다.

야수묘왕은 늘그막에 얻은 하나뿐인 자식을 세상 그 무엇보다 사랑하지만, 원후가 한 짓을 안다면 호통을 칠 것이다. 목숨에는 귀천(貴賤)이 없다면서.

‘그래, 그거면 충분하지. 목숨을 바치는 이유는.’

내심 중얼거린 원후는 텅 빈 호리병을 탈탈 털었다.

그리고 개미 눈물만큼 떨어지는 술을 바라보며 입맛을 다시다가, 이내 사방에 내려앉은 어둠 어딘가를 향해 불쑥 입을 열었다.

“거, 술 좀 있소?”

나직한 대답이 들려왔다.

“근무 중인 것으로 아는데.”

“다 아는 처지에 뭘. 호랑이 좆이나 까 잡수쇼.”

원후는 씩 웃었다.

이미 예정되어 있던 교대 시간은 한참이나 지났고, 어둠 너머에서 뻗어 나오는 기파는 소름이 끼칠 정도로 강대했다.

“그래서, 안 줄 생각이신가?”

“묘족에 술 좋아하는 원숭이가 하나 있다는 소리는 들었지. 받게.”

휘익.

원후는 어둠을 가르며 날아든 물체를 잡아챘다. 그리고 동시에 투박하지만 익숙한 호리병을 확인하고 자신도 모르게 침음성을 흘렸다.

“이건…….”

틀림없다. 다름 아닌 자신의 주군, 야수묘왕이 직접 만들어 항상 지니고 다녔던 바로 그 호리병이다.

“눈에 익은가?”

그 순간 귓가를 파고드는 누군가의 목소리. 천천히 고개를 든 원후의 시야에 한 사람이 들어왔다.

주인을 알 수 없는 피와 오물로 더럽혀진 백의(白衣). 창백하다는 표현이 어울릴 만큼 새하얀 피부.

“……백상.”

백상이 건조한 음성으로 답했다.

“일개 전사 따위가, 감히 대족장의 이름을 함부로 입에 담는가.”

“주군께서는…… 어찌 되셨지?”

“곧 알게 될 것이다.”

스륵. 파파팟!

순식간에 벌어진 일이었다.

백상이 피에 젖은 옷소매를 흔들자, 짙은 어둠 속에서 못 잡아도 일백이 넘는 백족 전사들이 나타나 그들을 포위한 것은.

‘빌어먹을.’

내심 욕설을 중얼거린 원후는 허리춤에 꽂아두었던 박도(朴刀)를 뽑아 들었다.

힐끗 하늘을 바라보니 오늘따라 구름에 달이 가려져 있다. 죽기에는 영 좋지 않은 날이었지만, 한편으로는 다행인 일이다.

달빛이 어두운 날 벌어지는 추격전에서는 도망자가 유리하니까.

‘부디 살아계셔야 합니다, 두 분 모두.’

이제 남은 것은 하나뿐이다.

원후는, 아니 모두는 망설임 없이 병장기를 들고 적들을 향해 달려나갔다.

두려움 따위는 범접할 수도 없을 만큼 거대한 함성과 함께.



* * *



쐐애애애액!

전신을 스치는 바람이 차갑다.

지금 이 순간에도 빠르게 스쳐 지나가는 풍경 속에는 사람의 그림자도, 여러 가지 독특한 형태를 띤 가옥(家屋)도 없었고 오직 풀숲만이 가득했다. 어느덧 외궁(外弓)을 벗어난 것이다.

‘하지만 아직도 남만야수궁의 영역이다. 속도를 늦춰서는 안 돼.’

아니, 어쩌면 척후대에 포함된 화룡각 대원들을 구하기 전까지 쉼 없이 달려야 할지도 모른다.

남만야수궁의 힘은 숲과 평야, 밀림과 늪으로 가득한 이 미지의 땅 전체를 아우르니까.

“미안하지만 조금만 더 부탁한다.”

그르릉.

야율목의 말처럼 역시 영물은 영물이다. 세찬 바람 소리 속에서도 용케 내 말을 알아들은 듯, 낮은 울음소리를 흘린 백호가 한층 속도를 높였다.

파파파팟!

아마 녀석이 이렇게까지 내 말을 잘 따르는 데는, 분명 자신의 등에 묶여 있는 주인의 존재도 한몫했을 것이다.

나는 백호가 나아갈 때마다 작게 흔들리는 신형을 바라보며 한숨을 내쉬었다.

‘야율목.’

정신없이 달리는 사이 외궁을 벗어났지만, 나는 야율목을 깨우지 않았다.

아니, 시도하지 못했다고 하는 것이 옳은 표현일 것이다.

‘정신을 차린다면 어떻게든 돌아가려고 하겠지.’

하지만 지금 돌아간다면 모든 것이 수포로 돌아갈 것이다.

그들이 위험을 무릅쓰고 열어 준 하나뿐인 생로(生路)를 포기한다면, 남은 것은 개죽음뿐일 테니까.

물론 신분이 신분인 만큼 나처럼 당장 처형시키려고 들지는 않겠지만…… 저 녀석이 돌아가고자 한다면 나는 막을 것이다.

야율목을 위해서라도. 녀석을 위해 싸우고 있을 묘족들을 위해서라도. 그리고 화룡각 대원들을 위해서라도.

이기적이라고 해도 좋다. 제 목숨만 아까워한다며 욕하고 손가락질해도 상관없다.

하지만 엿 같게도, 그것이 지금의 내게는 최선의 방책이었다.

‘빌어먹을.’

나는 질끈 입술을 깨물었다.

늦어도 하루, 혹은 반나절 안에 천라지망(天羅蜘網)이 남만 전체에 펼쳐질 터.

그전까지 최대한 멀리 벗어나 척후대를 발견해야 했다.

‘척후대를 이끄는 두 부족장은 사실상 야수묘왕의 충복들. 어쩌면 별다른 전투 없이 세 사람을 구할 수도 있다.’

물론 이건 내가 생각할 수 있는 최상의 결과다.

암천의 개입과 백상의 배반이 확실해졌고, 팔자에도 없는 학살극의 주인공이 된 지금. 어떤 변수가 생길지는 그 누구도 예측할 수 없었다.

‘모든 화룡각 대원들의 구출이 우선. 그리고 그다음은…….’

하지만 내 생각은 그 이상으로 이어지지 못했다.

바스락.

불현듯 멈춘 발걸음.

선두에서 망설임 없이 달려 나가던 백호의 움직임이 우뚝 멈춘 것이다.

“뭐야. 왜 그래?”

크릉.

“네 주인이 했던 말처럼 이대로 북서쪽으로 계속 달리면…….”

크르릉. 킁킁.

뭐지?

두 방향을 연달아 바라보더니, 내 손에 코를 처박고 킁킁 냄새를 맡는다.

출발 전에 그랬던 것처럼.

‘잠깐. 설마?’

그리고 그 순간.

띠링.



- 돌발 퀘스트, [요희의 추종향]이 생성되었습니다!



귓가를 파고드는 퀘스트 알림과 함께, 나는 떠올렸다.

요서부에서 발견했던 요희의 향낭(香囊)을.
```

## Final English reading copy

```markdown
# Chapter 670

It was a short but lengthy span of time.

Short enough to pass in the blink of an eye, yet long enough for a single moment to feel like seven days and nights.

Long enough to walk while looking back over each and every year of the past several decades. Long enough to watch a squalling newborn, crying in the arms of a mother who had died because she could not survive childbirth, grow into a tall and handsome young man.

That was how Baeksang’s deliberation had been both short and long, long and short.

And when his tightly sealed lips finally moved to break the silence, he already had his answer.

“You’ll regret this.”

The Beast Miao King calmly asked in return.

“What will I regret? Coming to find you? Or rescuing Jin Taekyung and the other Han Chinese?”

“Everything that has happened until now.”

“Just like you, Baeksang?”

“It’s different.”

Baeksang continued with a hardened expression.

“Unlike me, you still have a chance, Palace Lord. One last chance to undo your mistake.”

“One last chance…”

“If you return quietly now, I’ll forget everything I saw and heard here. As if nothing ever happened.”

“How can one cover the sky with the palm of one’s hand? I was already prepared for this when I told you to spare your subordinates guarding the underground prison.”

“If I order them to keep silent, they will obey. The Bai people’s loyalty to me is no weaker than that of the Seven Miao Tigers under your command.”

“Is that… the last affection you can show me as your sworn younger brother?”

Baeksang silently nodded.

The Beast Miao King gave him a sorrowful smile.

“Then, relying on that last bit of affection, I’ll ask you one more time. Half a shichen. Open a path for them, even if it’s only for half a shichen.”

“Palace Lord!”

“Even if I could turn back, I would not. That is the one difference between us, after spending our entire lives together.”

“……!”

The corners of Baeksang’s eyes trembled.

At this moment, he wanted with all his strength to deny those words.

*You’re wrong. Unlike you, I had only one path before me. I had no choice but to walk it.*

But his firmly closed lips would not open, and before he knew it, his hand had reached his sword hilt.

Click. Shing.

The cold scrape of metal cut through the brief silence.

The Beast Miao King’s eyes sank deeply as he looked at Baeksang, who held his beloved sword lowered at his side.

“So that is your choice?”

“I had no choice, Palace Lord. For me, right now… this is the best I can do.”

“It’s much better not to hear that awkward formal speech. It feels as though we’ve gone back to the old days.”

“You know as well as I do, Palace Lord. We can never go back to those days.”

“You think so?”

“Of course.”

At that firm answer, the Beast Miao King gave a faint smile.

Baeksang had made his decision. He did not hesitate.

Tssssss!

A dazzling halo of light illuminated the world around them.

A vast gathering of qi known as Sword Force descended toward its target.

Slice!

* * *

Three tigers ran like the wind, led by a snow-white White Tiger.

Wonhu, the eldest of the Seven Miao Tigers, watched their backs disappear into the darkness and muttered,

“Damn, they’re fast.”

That was the entirety of his impression.

Those who were leaving had left, and those who remained had stayed. He and the others had simply chosen for themselves to be the latter.

“Heh heh.”

With a relieved laugh, Wonhu pulled a gourd from inside his robes.

Pop.

The moment he removed the stopper, the scent of liquor spread through the air.

The Miao warriors nearby all lit up at once.

“Oh-ho.”

“That smells incredible. Did Big Brother brew it himself?”

“Hell, did they round up nothing but a pack of fucking mutts? Why are all your noses so sharp?”

Though Wonhu grumbled, his eyes were smiling.

With an expression that said he could not help it, Wonhu passed the gourd around to the men who had gathered.

“Nothing I can do. There isn’t much, so take turns and drink a little.”

“I swear on my life, not a single drop will reach Big Brother’s mouth.”

“Ah, I can’t pass this up.”

The Miao warriors laughed heartily and took turns tipping back the gourd.

The Nanman people were famous for their love of liquor. And with twenty grown men there, their boast that they would not leave a single drop behind seemed quite credible.

But…

“Ahh, that’s good. Now it’s Big Brother’s turn. I left a few drops out of courtesy.”

When Wonhu finally received the gourd, he could only snort with amusement.

Slosh.

He could tell just by shaking it lightly.

The liquor inside was not even half gone.

Looking at the men shamelessly carrying on about how good the liquor tasted, Wonhu let out a laugh.

“Turns out you aren’t fucking mutts after all—just a bunch of blowhards.”

“Hm? What are you talking about?”

“Indeed. Has senility already set in, now that you’re in your fifties?”

“Enough nonsense. Drink.”

At the surrounding urging, Wonhu tilted the gourd.

Not toward his mouth, but toward the ground covered in thick weeds.

Trickle.

“Don’t waste a single drop. If we survive, we’ll all sit together and drink through the night. And if we fall here, we’ll still be able to get drunk after death.”

“……!”

“……!”

The men who had watched him with hardened expressions slowly raised the corners of their mouths.

“Yeah. That sounds good.”

“Big Brother knows what he’s talking about.”

“Come to think of it, you’ve always been crazier about liquor than martial arts. Isn’t that right?”

Wonhu smiled.

So did the Seven Miao Tigers, who had spent their entire lives alongside him.

So did the Miao warriors who had willingly volunteered for this dangerous mission.

Regret?

Not in the slightest.

Even if they all died here, their one and only hope was that those who had left would survive and escape the danger.

That was why Wonhu could smile so freely.

As he thought of the one man who had always stepped forward first in everything, and who had even sent his only heir here to set an example for the others, Wonhu murmured inwardly.

*I’ll gladly accept punishment for disobeying your order… in the afterlife, my lord.*

Neither the Beast Miao King nor Yayul Mok feared death.

They did not use their subordinates as shields, nor did they retreat in terror.

The Beast Miao King loved his only child, whom he had gained late in life, more than anything in the world.

But if he learned what Wonhu had done, he would surely scold him, saying that there was no distinction between lives.

*Yes. That’s reason enough to give up our lives.*

Wonhu shook the empty gourd.

Then, as he watched the last drops of liquor fall like the tears of an ant, he smacked his lips and suddenly spoke toward somewhere in the darkness that had settled all around them.

“Hey, you got any liquor?”

A quiet reply came from the darkness.

“I thought you were on duty.”

“We both know what’s going on, so why bother? Go peel and eat a tiger’s dick.”

Wonhu grinned.

The scheduled shift change had passed long ago, and the waves of energy extending from beyond the darkness were so powerful that they sent chills down his spine.

“So, are you saying you won’t give me any?”

“I’ve heard there’s a monkey among the Miao people who likes liquor. Catch.”

Whoosh.

Wonhu snatched the object flying through the darkness.

At the same time, he recognized the rough but familiar gourd and unconsciously let out a groan.

“This is…”

There was no mistake.

It was none other than the gourd his lord, the Beast Miao King, had made himself and always carried with him.

“Does it look familiar?”

A voice suddenly pierced his ear.

Wonhu slowly raised his head.

A man stood in his field of vision.

His white robes were stained with blood and filth from unknown owners. His skin was so starkly white that *pallid* was the only word for it.

“……Baeksang.”

Baeksang answered in a dry voice.

“How dare a mere warrior casually speak the name of the Great Chieftain?”

“What happened to my lord?”

“You’ll find out soon enough.”

Swish. Papapat!

It happened in an instant.

When Baeksang shook his blood-soaked sleeve, more than a hundred Bai warriors appeared from the deep darkness and surrounded them.

*Damn it.*

Wonhu cursed inwardly and drew the broad-bladed saber tucked into his waist.

He glanced at the sky.

Today, of all days, the moon was hidden behind the clouds.

It was a particularly poor day to die, but in another sense, that was fortunate.

In a pursuit carried out under a moonless sky, the fugitives had the advantage.

*Please, both of you. You have to still be alive.*

Only one thing remained now.

Wonhu—or rather, all of them—raised their weapons and charged toward the enemy without hesitation.

A tremendous roar rose around them, so vast that fear itself could not approach it.

* * *

Whoooooosh!

The wind brushing against my entire body was cold.

Even as the landscape rushed past us, there was not a single person or one of the oddly shaped houses in sight—only thickets everywhere.

We had already left the Outer Palace behind.

*But we’re still within the territory of the Nanman Beast Palace. We can’t slow down.*

No. We might have to keep running without rest until we rescued the Fire Dragon Pavilion members included in the reconnaissance squad.

The power of the Nanman Beast Palace extended across this entire unknown land, filled with forests, plains, jungles, and swamps.

“Sorry, but I’m going to have to ask a little more of you.”

Grrr.

Just as Yayul Mok had said, this really was a spiritual creature.

Even through the roar of the fierce wind, the White Tiger seemed to understand my words. It let out a low growl and increased its speed even further.

Papapapat!

There was probably another reason it obeyed me so well.

Its master was tied to its back.

I let out a sigh as I watched Yayul Mok’s body sway faintly each time the White Tiger moved forward.

*Yayul Mok.*

We had left the Outer Palace while running frantically, but I had not woken him.

No. It would be more accurate to say I couldn’t bring myself to try.

*If he wakes up, he’ll try to go back somehow.*

But if he returned now, everything would be for nothing.

If we gave up the one and only escape route they had risked everything to open for us, all that would remain would be a meaningless death.

Of course, given his status, they probably would not execute him immediately as they intended to do with me…

But if he tried to turn back, I would stop him.

For Yayul Mok’s sake.

For the Miao people fighting for him.

And for the members of the Fire Dragon Pavilion.

It was fine if they called me selfish. I did not care if they cursed me and pointed their fingers at me, saying I only cared about saving my own life.

But damn it, this was the best course of action available to me right now.

*Damn it.*

I bit down hard on my lip.

At most, within a day—or perhaps half a day—the net over heaven and earth would be spread across all of Nanman.

Before that happened, we had to get as far away as possible and find the reconnaissance squad.

*The two tribal chiefs leading the reconnaissance squad are effectively loyal retainers of the Beast Miao King. Perhaps we’ll be able to rescue three people without much of a fight.*

Of course, that was the best possible outcome I could imagine.

With Dark Heaven’s intervention and Baeksang’s betrayal now certain, and with me having become the star of a massacre that had never been in the cards for me, no one could predict what variables might arise.

*Rescuing all the Fire Dragon Pavilion members comes first. And after that…*

But my thoughts did not get any further.

Rustle.

The White Tiger abruptly stopped.

It had been running at the front without hesitation, but its movement came to a sudden halt.

“What’s wrong?”

Grrr.

“As your master said, if we keep running northwest like this…”

Grrrr. Sniff, sniff.

What?

The White Tiger looked in two directions in succession, then buried its nose in my hand and began sniffing.

Just as it had before we set out.

*Wait. Could it be?*

And then, at that very moment—

Ding!

> **System**
>
> - A Sudden Quest, **Yohi’s Tracking Scent**, has been generated!

Along with the Quest notification piercing my ear, I remembered.

The scent pouch belonging to Yohi that I had discovered in the western Yao territory.
```

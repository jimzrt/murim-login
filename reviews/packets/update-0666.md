<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0666.txt",
      "sha256": "aba3e2bd56bfe965ef704e6652b5f885399a8a96b7f0f4afa9fe65d87e090e24",
      "bytes": 12695
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "680dfcd750f5d1f850cae728f628b50738f0430e02976194003810736806c579",
      "bytes": 2407
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "050c006b5f091041d81ee2d3d2c189fc6d9e5840e2ad9aa9bcb1c627b0199019",
      "bytes": 201910
    },
    {
      "path": "characters/Baeksang.md",
      "sha256": "9d4745ff2b848f267e7b7b65409da2a93b2d352091b93959a89d5ef388924e85",
      "bytes": 1158
    },
    {
      "path": "characters/Beast Miao King.md",
      "sha256": "33e71ed664236e276830f34fb265190a0263ba9272759adf1d3fb6174b1e0734",
      "bytes": 814
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "e4b81a5d89a2c174e2978b7cbd977cd5828a9e3784342a0eeeb222de5f123535",
      "bytes": 553
    },
    {
      "path": "characters/Heugung.md",
      "sha256": "099939f074519a89eb6581b5cbf1dabe681ae2e48ce609e02d8fbbfdc9e31e63",
      "bytes": 769
    },
    {
      "path": "characters/Human Butcher.md",
      "sha256": "580c27be08fbadb173154b7a6a791177915d7f1d505c8f1d1ab59edff41e022d",
      "bytes": 667
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "f5128e8d5206c67fd49e0e1acb65866d6990fe44216d11d54695a3003a3f1dde",
      "bytes": 1907
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "f7b90843d4273f0e8119915ce064a9bb5034516e97834eedc3a30e1c4c70b72a",
      "bytes": 622
    },
    {
      "path": "characters/Venerable Wusang.md",
      "sha256": "7e4304f1679023f4f3573692f9b46a69fb257b82a3cd7ac265011408db787fac",
      "bytes": 577
    },
    {
      "path": "characters/Yayul Mok.md",
      "sha256": "8b7fe56e1c51e299abfc843f359c2195b091302097d233be46458184ee76386a",
      "bytes": 871
    },
    {
      "path": "characters/Yohi.md",
      "sha256": "c9f7c14504043890f906af5d0d495dcb376e0c66fb9122b5dbcbe503f8b5b5f3",
      "bytes": 645
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "29aa69db3afa385987676e935eee2351d038d97abe98f880edd9d0534e275da2",
      "bytes": 207150
    }
  ],
  "estimated_tokens": 11588
}
-->

# Durable State Update — Chapter 666

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 666. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 666. Profile updates may replace only one
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
  "chapter": 666,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 666,
    "continuity_sources": [666],
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
    "Jin Taekyung remains imprisoned in the Nanman Beast Palace's underground prison with sealed internal energy and iron balls, and his execution is scheduled for noon in two days.",
    "Taishan is imprisoned in the cell above Jin, with his internal energy sealed and his body bound; he can communicate with Jin through the broken ceiling.",
    "The System's Escape from Namshank Quest requires Jin to escape the underground prison before execution; failure results in death, and the Reward is a Linked Quest.",
    "Taishan remains absolutely loyal to Sama Pyo, trusts Jin as Pavilion Master, and has grown attached to the Fire Dragon Pavilion members.",
    "Jin realizes that the Middle Dantian is moved by Will rather than internal energy and causes the world's qi to ripple despite his sealed internal energy.",
    "Namho and Sama Pyo remain detained separately and are reportedly safe according to Yayul Mok's information.",
    "Ju Hwaran, Song Ilseom, and Hyuk Mujin remain captured elsewhere, which is currently considered safer.",
    "Jin suspects the Blood Monk may be a subordinate of the Southern Heaven Demon Empress and may endanger the reconnaissance squad.",
    "Sudal is leading three swift ships toward Guizhou and has encountered the Blood Monk aboard a crewless Yangtze River Channel League ship.",
    "Baeksang has dismissed his guards and is meeting privately with the Beast Miao King, who came to wait for him in his quarters."
  ],
  "continuity_sources": [
    665,
    664
  ],
  "open_questions": [
    "Is the Blood Monk truly a subordinate of the Southern Heaven Demon Empress?",
    "Will the Blood Monk attack Sudal's ships or use the captured ship to travel to Nanman?",
    "How will Jin escape the underground prison before his execution?",
    "Will the captured reconnaissance members encounter the Blood Monk?",
    "Will the Beast Miao King's private meeting alter Baeksang's planned execution or his alliance with Dark Heaven?"
  ],
  "safe_through": 665,
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
| 종남파    | **Zhongnan Sect**                |
| 암천     | **Dark Heaven**                  |
| 남만야수궁  | **Nanman Beast Palace**          |
| 마교     | **Demonic Cult**                                 |                                                       |
| 중원     | **Central Plains**                               |                                                       |
| 장문인    | **Sect Leader**                              |
| 귀가      | **your family**                                                 |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 대사      | **Master** for a senior Buddhist monk                           |
| 백상 | **Baeksang** | Great chieftain of the Bai people and Yayul Cheok's sworn younger brother. |
| 야수묘왕 | **Beast Miao King** | Leader of the Miao people and master of the Nanman Beast Palace. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 흑웅 | **Heugung** | Great chieftain of the Yi people; his name literally means Black Bear. |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 무상진인 | **Venerable Wusang** | Former Sect Leader of the Zhongnan Sect and master of the Wind-and-Cloud Sword Lord. |
| 야율목 | **Yayul Mok** | Young Palace Lord of the Nanman Beast Palace. |
| 요희 | **Yohi** | Female great chieftain of the Yao people. |
| 평화 | **Peace Guild** | Guild name. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 한족 | **Han Chinese** | Ethnic designation used by the steppe chieftains. |
| 종남산 | **Mount Zhongnan** | Mountain where the Zhongnan Sect’s main sect is located. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 호위장 | **Captain of the Guards** | The Sichuan City Lord's guard captain. |
| 악귀 | **Fiend** | Descriptive epithet applied to the First Fiend. |
| 뇌옥 | **underground prison** | The Tang Clan's subterranean prison. |
| 새외 | **Outer Lands** | Lands outside the Central Plains and its Murim. |
| 제니 | **Jenny** | East Asian news anchor interviewing Jacob. |
| 내궁 | **Inner Palace** | The inner compound of the Nanman Beast Palace. |
| 야율 | **Yayul** | Name used in Taekyung's colloquial address to the Beast Miao King. |
| 대회의 | **Tribal Grand Council** | Nanman's council of great chieftains. |
| 대설산 | **Great Snow Mountain** | Mountain where Baeksang's wartime account reaches its next episode. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 야율목 | 진태경 | Nanman_Beast_Palace_Young_Palace_Lord_to_Han_intruder_and_Murim_Alliance_Pavilion_Master | you | formal but hostile | Asks Jin's identity and orders him to follow after learning he belongs to the Murim Alliance. |
| 진태경 | 야율목 | Fire_Dragon_Pavilion_Pavilion_Master_to_Nanman_Beast_Palace_Young_Palace_Lord | Mok | casual, teasing, and insulting | Calls him rude and later addresses him as 목아 while jokingly claiming they are friends. |
| 야율목 | 백상 | nephew_to_father's_sworn_younger_brother | Uncle Baeksang | ceremonial and deferential | Yayul Mok formally greets Baeksang as he arrives at the stone door. |
| 백상 | 야율목 | father's_sworn_brother_to_nephew | you | cold and formal | Baeksang questions Yayul Mok about his return, the pasture fire, and the Palace Lord's whereabouts. |
| 야수묘왕 | 백상 | sworn_older_brother_to_sworn_younger_brother | Baeksang | familiar and bittersweet | Yayul Cheok offers Baeksang his preferred fruit wine and asks why he came. |
| 요희 | 흑웅 | Yao great chieftain to Yi great chieftain | big brother | seductive and falsely affectionate | Uses 오라버니 to flatter and manipulate Heugung. |
| 흑웅 | 요희 | Yi great chieftain to Yao great chieftain | my dear | adoring and deferential | Responds to Yohi's manipulation with open infatuation. |
| 요희 | 진태경 | Yao great chieftain to Murim Alliance pavilion master | Jin Taekyung | casual and probing | Identifies him by his full name while allowing him to keep the mask on. |
| 진태경 | 요희 | Fire Dragon Pavilion pavilion master to Yao great chieftain | you | guarded and blunt | Answers Yohi's probing questions directly while warning her about Ju Hwaran. |
| 백상 | 요희 | Bai great chieftain to Yao great chieftain | Yohi | cold and formal | Calls to Yohi from outside the tent at the chapter's end. |
| 백상 | 진태경 | Nanman great chieftain to Murim Alliance Pavilion Head | you bastard | cold, hostile, and contemptuous | Baeksang calls Jin a Han Chinese man, rejects his status, and orders him to leave. |
| 진태경 | 백상 | Murim Alliance Pavilion Head to Nanman great chieftain | you | polite but deliberately provocative | Jin tells Baeksang that Nanman's blood was shed for the world rather than merely for the Central Plains. |
| 진태경 | 야수묘왕 | younger allied master to Ten Kings elder | Great Hero Yayul | urgent and respectful | Uses 야율 대협 while warning the Beast Miao King not to enter the valley. |
| 야수묘왕 | 진태경 | senior allied master to younger allied master | you | informal and cautionary | Warns Taekyung not to lower his guard and to be careful while crossing the swamp. |
| 야율목 | 야수묘왕 | son_to_father | Father | formal and deferential | Yayul Mok calls out to the Beast Miao King after the rescue party arrives. |
| 흑웅 | 백상 | younger_great_chieftain_to_senior_great_chieftain | Uncle Baek | deferential and nervous | Heugung addresses Baeksang as 백 숙부 after being confronted by his icy stare. |
| 백상 | 야수묘왕 | Nanman great chieftain to the Nanman Beast Palace Lord | Palace Lord | restrained and apologetic | Apologizes for causing the disturbance after the Beast Miao King stops the fight. |
| 흑웅 | 진태경 | Nanman great chieftain to Central Plains ally and covert contact | you | cautious and informal | Heugung uses 자네 in private Sound Transmission while explaining the missive and Baeksang's alleged collusion. |
| 진태경 | 흑웅 | Central Plains investigator to covert informant and prospective witness | Heugung | blunt and confrontational | Jin questions Heugung's reliability, challenges his claims, and demands proof. |

## Listed compact profiles

### Baeksang.md

# Baeksang (백상)

- **Safe through:** Chapter 665
- **Aliases:** None
- **Role:** Baeksang is the middle-aged great chieftain of the Bai people, one of Nanman's four most powerful great tribes, and one of only two Supreme Peak masters in Nanman; he has imprisoned Jin Taekyung and joined forces with twenty tribal chieftains to arrange Jin's execution at noon in two days.
- **Personality:** Cold, rigid, meticulous, politically resolute, and strategically manipulative, with a deep but guarded attachment to his sworn elder brother and enduring grief, hatred, and betrayal over Baekhwi's death.
- **Voice:** Rigid, formal, restrained, and emotionally distant.
- **Relationships:** Baeksang is Yayul Cheok's sworn younger brother and childhood companion, Yayul Mok's sworn uncle, and the father of his deceased only child Baekhwi, whom the Great Snow Fiend killed during the Great Faction War; he opposes the Nanman Beast Palace joining the Murim Alliance, distrusts the Central Plains because of the alleged wartime betrayal, and is alleged by Heugung to have colluded with Dark Heaven.

### Beast Miao King.md

# Beast Miao King (야수묘왕)

- **Safe through:** Chapter 665
- **Aliases:** None
- **Role:** The Beast Miao King is the Palace Lord of the Nanman Beast Palace, the great chieftain of the Miao people, a master among the Ten Kings, and one of only two Supreme Peak masters in Nanman.
- **Personality:** Fierce and vigilant when confronting threats to the Nanman Beast Palace.
- **Voice:** Low, growling, and forceful.
- **Relationships:** He commands the Nanman Beast Palace, is Baeksang's sworn elder brother and childhood companion, is responsible for the forces stationed at Ailao Mountain, has ordered Ju Hwaran, Song Ilseom, and Hyuk Mujin to investigate the Blood Monk in Guizhou, and met the Martial God twice more than fifty years ago.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 665
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Heugung.md

# Heugung (흑웅)

- **Safe through:** Chapter 661
- **Aliases:** None
- **Role:** Heugung is the middle-aged great chieftain of the Yi people, one of Nanman's four great tribes.
- **Personality:** Heugung presents as foolish and easily flattered in public but is capable of concealed planning, disguise, and covert contact.
- **Voice:** Heugung speaks with warm enthusiasm and genuine, openly devoted affection toward Yohi.
- **Relationships:** Heugung genuinely loves Yohi and had promised to cooperate with Jin Taekyung; he disappeared alongside Yohi after the assault on the Fire Dragon Pavilion, and his death remains unconfirmed after a severed wrist believed to be his was found at her estate.

### Human Butcher.md

# Human Butcher (인도)

- **Safe through:** Chapter 644
- **Aliases:** None
- **Role:** Former mysterious Han Chinese mounted-bandit power in Northern Gaoyuan commanding fifty subordinates; a Peak master killed by an unnamed old man in a single move
- **Personality:** Cold, intimidating, and murderous; he kills people as though slaughtering livestock
- **Voice:** Cold, curt, and quietly threatening
- **Relationships:** He is one of four powerful participants at the Northern Gaoyuan gathering, intimidates Temur, and has claimed Ghost Sword Wipeng as his personal target in the proposed attack

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 665
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple, the Fire Gate Clan's nineteenth successor, and the Pavilion Master of the Fire Dragon Pavilion within the Murim Alliance; he is a Supreme Peak master with the Heavenly Martial Physique and Force, publicly recognized as an S-rank-level Hunter while formally retaining an A-rank license, and he is currently imprisoned under Baeksang's order with a public execution scheduled for noon in two days.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 665
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Venerable Wusang.md

# Venerable Wusang (무상진인)

- **Safe through:** Chapter 662
- **Aliases:** None
- **Role:** Former Sect Leader of the Zhongnan Sect, master of the Wind-and-Cloud Sword Lord, and a Supreme Peak master who died during the Great Snow Mountain battle.
- **Personality:** Righteous, wise, calm, and fair regardless of a person's background.
- **Voice:** Not established.
- **Relationships:** Master of the Wind-and-Cloud Sword Lord; allied with Baeksang and the Beast Miao King during the Great Faction War.

### Yayul Mok.md

# Yayul Mok (야율목)

- **Safe through:** Chapter 664
- **Aliases:** None
- **Role:** Yayul Mok is the non-Han Young Palace Lord of the Nanman Beast Palace, a spear-wielding warrior who rides a white tiger, and a halting but capable speaker of Han Chinese.
- **Personality:** Protective of Nanman Beast Palace livestock, quick-tempered toward trespassers, and capable of restraint once he recognizes legitimate authority.
- **Voice:** Blunt, commanding, and formal-polite toward strangers, becoming openly insulting when provoked.
- **Relationships:** Yayul Cheok is the Beast Miao King and Yayul Mok's father; Yayul Mok is his only surviving son after three older siblings died in the Great Faction War, Baeksang is his father's sworn younger brother, and his white tiger is a long-bonded companion.

### Yohi.md

# Yohi (요희)

- **Safe through:** Chapter 661
- **Aliases:** None
- **Role:** Yohi is the female great chieftain of the Yao people, one of Nanman's four great tribes.
- **Personality:** Yohi's public presence is charismatic and captivating, drawing widespread admiration and affection.
- **Voice:** Not established.
- **Relationships:** Yohi leads the Yao people, seeks to unite Nanman's four great tribes under Yao leadership, manipulates Heugung alongside Baeksang, and has disappeared from the Inner Palace alongside Heugung after the assault on the Fire Dragon Pavilion.

## Korean source

```text
＃666화



때아닌 불청객, 야수묘왕의 갑작스러운 등장에도 백상의 목소리는 차분했다.

“이미 알고 계시지 않습니까, 궁주.”

야수묘왕이 씁쓸하게 웃었다.

백상의 말은 사실이었다. 비록 적지 않은 숫자의 부족장들이 돌아섰지만, 그는 남만야수궁의 주인이다.

적어도 내궁 안에서만큼은 백상의 일거수일투족을 파악하고 있었다.

“뇌옥에서 제법 오래 머물렀더군. 그 아이와 무슨 이야기를 그리 길게 나누었느냐?”

“…….”

진태경과의 대화가 생각난 백상은 자기도 모르게 멈칫했다. 하지만 그의 망설임은 짧았다.

“이틀 뒤 정오, 모두가 지켜보는 앞에서 처형당할 것이라 말했습니다.”

“그리고?”

“그 누구도 막을 수 없다는 사실도 함께 알려 주었지요.”

정확히 자신을 겨냥한 한마디에, 야수묘왕의 눈빛이 깊게 가라앉았다.

“진정 그리 생각하느냐.”

“물론입니다.”

“그렇게 놔두지 않겠다면?”

“궁주는 가장 앞에 선 자일 뿐, 남만의 대사(大事)를 결정하는 권한은 오롯이 대회의에 있다.”

나직하게 읊조린 백상이 말을 이었다.

“잊으셨습니까. 수백 년 전, 이 땅의 선조들이 하나의 깃발 아래 모여 했던 맹세를.”

“……!”

“결과는 달라지지 않습니다. 내일, 마지막 대회의의 안건은 한족 진태경의 처형입니다.”

야수묘왕은 무거운 눈빛으로 백상을 응시했다. 이미 세력의 저울추가 기울었음은 그 역시 알고 있다.

그러나 그가 진태경을 포기했다면, 이 자리까지 찾아오지도 않았을 것이다.

“그게 전부인가?”

“이미 저를 비롯한 부족장 스물이 뜻을 모았습니다. 만일 궁주께서 대회의의 뜻을 저버리고 다른 방법을 택하신 다면…….”

“그걸 묻는 것이 아니다.”

이어지려던 백상의 말을 끊은 야수묘왕이, 한숨처럼 말을 이었다.

“진태경, 그 아이에게 말하지 않았느냐. 휘(輝)에 관한 이야기를.”

“……!”

흔들림 없던 백상의 표정에 실금이 번졌다. 과거에도 그랬고, 현재에도 마찬가지다.

수십여 년간 철면(鐵面)으로 살아온 그를 동요케 할 수 있는 것은, 더는 곁에 두지 못하게 된 자식뿐이다.

그리고 야수묘왕은 그 사실을 누구보다 잘 알 고 있는 사람이었다.

“뇌옥에 사람을 심어 둔 것이 아니다. 그저 짐작했을 뿐이지. 평소와 달리 흔들리고 있는 네 모습을 보고 확신했다.”

“어떻게…….”

“어찌 모르겠느냐. 우리는 평생을 함께했거늘.”

백상은 입을 다물았다. 우리, 라는 두 글자가 유난히도 크게 다가왔다. 두 사람에게 당연했던, 이제는 낯설어져 버린 두 글자.

하지만…….

까드득.

“그건, 궁주와 제가 같은 길에 서 있을 때였지요.”

야수묘왕이 고개를 가로저었다.

“지금도 마찬가지다. 우린 단 한 번도 갈라선 적이 없어.”

“이미 늦었습니다.”

“늦지 않았따. 우리는 여전히 마음으로 맺어진 의형제니까. 지난 잘못은 지금이라도 돌이킬 수 있다.”

“제게는 모두 까마득한 과거의 인연일 뿐입니다.”

“그리고 아우는 지금까지 그 과거에 사로잡혀 있지.”

“……!”

“나 역시 그날을 기억한다. 누구보다 바르고 빛나던 아이가 이 땅에서 사라진 그날을, 어찌 잊을 수 있겠느냐.”

백상은 이를 악물었다. 떠올리는 것만으로도 괴로운 그날의 기억.

동시에 한편으로는 알고 있었다. 그날을 둘러싼 모든 진실이 밝혀졌을 때, 자신만큼이나 분노하고 슬퍼했던 이가 있었음을.

그러나 모두 허사였다.

“나도, 궁주도 무력했습니다. 놈들의 죄를 입증할 증거는 사라졌고, 모든 것이 뒤어이 찾아온 평화에 파묻혔지요.”

모래사장에 찍힌 수많은 발걸음은, 뒤이어 밀려온 파도에 휩쓸려 사라지는 법.

그러나 백상은 기억하고 있었다. 위험에 빠진 자식을 외면했던 그들의 얼굴을 살과 뼈에 새기고 마음으로 곱씹었다.

중원이라는 넓은 모래사장을 모두가 함께 나란히 걸었다고 생각했지만, 실은 이민족이라는 이유로 앞장세워졌을 뿐이었다.

“그 모든 것을 잊을 수도, 돌이킬 수도 없습니다. 한데 궁주는 어찌하여……!”

목소리를 높이려던 백상은 문득 말을 멈췄다. 어느새 야수묘왕의 얼굴에 드리운 슬픔을 보았기 때문이었다.

“내가 잊었다고 생각하느냐? 자식들을 먼저 떠나보낼 수밖에 없었던 이 못난 아비가?”

오십여 년 전.

중원으로 향했던 일만의 전사 중에는 야수묘왕의 자식들 역시 포함되어 있었고, 그들은 살아서 남만 땅을 밟지 못했다.

“아직도 후회한다. 남만야수궁의 궁주가 되지 않았더라면, 전장으로 향하지 않았더라면. 최소한 아비와 함께 싸우겠다는 그 아이들의 청을 거절했다면 어땠을까, 하고.”

“…….”

“아우의 말이 옳다. 우리는 무력했어. 사무치게 분노했고 슬픔으로 울부짖었지만 할 수 있는 것이 없었지. 하지만 남만으로 돌아가야 했다. 십 년 만에 다가온 평화를 밀어내고 또 다른 전쟁을 시작하기에는 모두가 지쳐 있었으니까.”

야수묘왕이 허탈한 웃음을 흘렸다. 당시 새외(塞外)의 세력 중 하나에 불과한 남만과 중원의 격차는 현저했다.

아니, 종남파 하나만 두고 봐도 비교적 열세였다.

당대 장문인이었던 무상진인(無上眞人)은 대협다운 풍모로 많은 이들의 존경을 받고 있었고, 그랬던 그가 대설산에서 벌어진 마지막 전투에서 목숨을 잃자 수많은 문파와 무림인들이 종남산을 찾았다.

“나는 선택했을 뿐이다. 죽은 이들, 살아남은 이들, 그리고 복수와 대의 중에서.”

그 후의 일은 모두가 알고 있는 대로였다.

야수묘왕은 살아남은 이들을 이끌고 남만으로 돌아왔고, 가족을 잃은 이들이 쏟아 내는 수많은 비난과 직면했다.

“내 삶은 후회투성이였다. 허나 그때 내린 선택만큼은 단 한 번도 후회하지 않았다. 그렇게 우리는 하나로 뭉쳤고, 전보다 더욱 부강해졌으며, 과거의 죄인들을 추궁할 힘을 갖추었으니까.”

지금껏 들어 보지 못한 이야기에, 백상의 얼굴이 딱딱하게 굳었다. 그러나 동시에 야수묘왕을 바라보는 그의 눈빛에는 이해하지 못할 감정 역시 섞여 있었다.

“하지만 궁주께서는 이번에도 중원의 편에 서실 테지요.”

야수묘왕은 한 치의 망설임도 없이 대답했다.

“그래, 그럴 것이다.”

“도대체 왜…….”

“단지 나무 한 그루가 병들었다 하여, 숲 전체를 불태우는 것은 멍청한 짓이니까.”

“……!”

“뿌리 뽑아야 하는 것은 그 나무를 병들게 만든 원인이다. 섣불리 숲을 태운다면, 그 불길이 다음으로 향할 곳은 바로 우리다.”

야수묘왕이 탄식처럼 말을 이었다.

“과거 마교가 그러했고, 지금은 암천이 그러하다. 우리는 숲을 지키기 위해 싸운 것이었어. 이 땅 역시 숲의 일부니까.”

중원인도, 남만인도 인정하지 않는 사실이지만 야수묘왕은 알고 있었다.

비록 멀리 떨어져 있으나, 그들은 천하(天下)라 불리는 숲에 함께 살아가고 있다는 것을.

그리고…….

“너도 알고 있지 않으냐, 백상.”

그것을 가장 잘 이해하고 있는 사람이, 바로 흔들리는 눈으로 자신을 바라보고 있는 의제(義弟)라는 것을.

“안다. 이 우형이 무슨 말을 해도 아우의 귀에는 들리지 않는다는 걸. 이미 기억도 나지 않는 옛일이라며, 그 시절의 백상은 오래전 죽어 없어졌다 하겠지.”

야수묘왕의 자식들은 마교에 의해 죽었지만, 백상의 하나뿐인 자식은 아군이라고 믿었던 자들의 외면으로 희생당했다.

그만큼 중원을 향한 분노의 크기도, 깊이도 다를 수밖에.

하지만 백상을 오랫동안 지켜봐 온 야수묘왕은 이미 짐작하고 있었다.

“지금 가는 길을 멈추지 않는다면…… 아우는 후회할 것이다. 과거에도, 지금도, 그리고 앞으로도.”

백상은 대답하고 싶었다. 후회하지 않노라고.

자신의 모든 것이나 다름없는 그 아이, 휘(輝)를 위해서라면 무엇이든 할 수 있다고.

살아서는 복수귀(復讐鬼)라 불려도 좋고, 죽어서는 악귀(惡鬼)라 불려도 기꺼이 웃으며 이 길을 가겠노라고.

‘그런데 왜…….’

왜. 도대체 어째서.

지난 세월 동안 마음속으로 수백, 수천 번을 되뇌었던 그 생각이 지금 이 순간 입 밖으로 흘러나오지 않는 것일까.

이미 두 번 다시 돌아갈 수 없는 길을 지나왔음에도 도대체 무슨 이유로.

‘왜 이러는 것이냐, 백상.’

그리고 백상이 자신의 공허한 마음속으로 답하지 못할 질문을 던진 그 순간.

야수묘왕의 나직한 목소리가 그의 귓가를 파고들었다.

“궁주(宮主)의 자리에서 물러날 수도 있다.”

예상하지 못한 한마디에 백상의 동공이 흔들린다. 그러나 야수묘왕은 어느 때보다 차분한 어조로 말을 이었다.

“잘못 들은 것이 아니다. 아우가 원한다면, 지금 당장이라도 궁주의 자리를 내놓지.”

백상은 혼란스러웠다. 궁주의 자리가 공석이 된다면, 남은 대족장 중 한 사람이 대회의를 거쳐 새로운 궁주로 취임한다.

그러나 흑웅과 요희, 두 대족장이 사라진 지금 이 같은 상황에서 야수묘왕의 제안이 의미하는 바는 명백했다.

“……다른 누구도 아닌 나를, 새로운 궁주로 세우겠다고?”

“그래. 들은 대로다.”

“궁주. 미치기라도 한 겁니까.”

“그럴 리가 있겠느냐.”

남만야수궁을 실질적으로 움직이는 것은 서른두 명의 부족장이지만, 궁주라는 이름이 주는 권위 역시 무시할 수는 없다.

그런데 지금 같은 상황에서 이처럼 말도 안 되는 제의를 하다니.

“도대체 이게 무슨…….”

이해할 수 없다는 눈빛으로 야수묘왕을 바라보던 백상이, 문득 입을 다물었다.

평소와는 다른, 담담하기 그지없는 그의 태도에서 순간 무언가를 깨달은 것이다.

‘설마.’

한 줄기 섬광처럼 뇌리를 스치는 생각. 그와 동시에 야수묘왕이 천천히 입을 열었다.

“반 시진. 반 시진이면 충분하다. 그들을 위해 길을 열어 주어라.”

반 시진이라는 시간, 그리고 ‘그들’이라는 두 글자.

짐작이 확신으로 바뀌는 데는 그것만으로 충분했다. 백상은 끓어오르는 목소리로 물었다.

“도대체 왜, 무슨 이유로 이렇게까지 하는 겁니까?”

곧이어 들려온 야수묘왕의 대답에는 한 치의 흔들림도, 망설임도 존재하지 않았다.

“그들이 우리를 돕기 위해 왔으니까. 과거 우리가 그랬던 것처럼.”

“……!”

“그리고 나는 너를 도울 것이다. 언제나와 같이.”

그러기에는 이미 늦었소.

마음속으로 씹어뱉듯 중얼거린 백상은 밖에서 대기하고 있을 호위장을 불렀다.

아니, 부르려고 했다.

하지만 어째서인지 그의 발도, 입술도 떨어지지 않았다.

백상은 지그시 눈을 감았다. 진즉 흘려보냈어야 할 목소리는 여전히 귓가에 맴돌고 있었다.



‘도대체 얼마나 더 많은 피를 흘릴 셈이냐, 백상.’



* * *



어둠 속을 나아가는 움직임은 조용하고 은밀했다.

쉬쉬쉬쉭!

한 방향을 향해 쏘아지는 인영들의 쾌속함에 바람이 갈라지고, 잎사귀가 흔들린다.

그리고 누군가가 그 사실을 알아챘을 때는 이미 모든 것이 늦어 있었다.

쉭, 투둑!

뻣뻣하게 굳은 채 쓰러지는 몸뚱어리. 그의 손에 들려 있던 횃불을 받아 든 한 인영이 입술을 달싹였다.

“뇌옥을 열어라.”

화륵.

일렁이는 횃불 위로, 야율목의 얼굴이 비쳤다.
```

## Final English reading copy

```markdown
# Chapter 666

Despite the Beast Miao King’s sudden appearance as an unexpected guest, Baeksang’s voice remained calm.

“You already know, don’t you, Palace Lord?”

The Beast Miao King smiled bitterly.

Baeksang’s words were true. Although a considerable number of tribal chieftains had turned against him, he was still the master of the Nanman Beast Palace.

At least within the Inner Palace, he knew Baeksang’s every movement.

“You spent quite a long time in the underground prison. What did you talk about with that boy for so long?”

“……”

Remembering his conversation with Jin Taekyung, Baeksang involuntarily hesitated. But his hesitation was brief.

“I told him that he would be executed at noon two days from now, in front of everyone.”

“And?”

“I also told him that no one could stop it.”

At the precisely aimed remark, the Beast Miao King’s eyes grew dark.

“Do you truly believe that?”

“Of course.”

“And if I refuse to let that happen?”

“The Palace Lord is merely the one standing at the forefront. The authority to decide Nanman’s great affairs belongs solely to the Tribal Grand Council.”

Baeksang recited the words in a low voice, then continued.

“Have you forgotten? The oath our ancestors made hundreds of years ago, when they gathered beneath a single banner on this land.”

“……!”

“The result will not change. Tomorrow, the agenda of the final Tribal Grand Council will be the execution of the Han Chinese Jin Taekyung.”

The Beast Miao King stared at Baeksang with heavy eyes. He knew as well as anyone that the scales of power had already tipped.

But if he had given up on Jin Taekyung, he would never have come here.

“Is that all?”

“Twenty tribal chieftains, including myself, have already united behind this decision. If you abandon the will of the Tribal Grand Council and choose another path…”

“That is not what I am asking.”

The Beast Miao King cut off Baeksang’s words and continued with a sigh.

“Did you not tell Jin Taekyung, that boy, about Hwi?”

“……!”

A crack appeared in Baeksang’s unshaken expression. It had been the same in the past, and it was the same now.

The only person who could shake a man who had lived behind an iron mask for several decades was the child he could no longer keep by his side.

And the Beast Miao King knew that better than anyone.

“I did not plant someone in the underground prison. I merely guessed. Seeing you shaken unlike your usual self confirmed it.”

“How…”

“How could I not know? We have spent our entire lives together.”

Baeksang closed his mouth. The single word *we* struck him with unusual force. A word that had once come naturally to both of them, but had now become unfamiliar.

But then…

Grind.

“That was when the Palace Lord and I stood on the same path.”

The Beast Miao King shook his head.

“It is the same now. We have never parted ways even once.”

“It is already too late.”

“It is not too late. We are still sworn brothers bound together in our hearts. We can turn back the wrongs of the past even now.”

“To me, they are nothing more than ties from a distant past.”

“Then you have been shackled to that past all this time, little brother.”

“……!”

“I remember that day too. How could I forget the day that child, who was more upright and radiant than anyone, disappeared from this land?”

Baeksang clenched his teeth. Merely recalling that day was agonizing.

At the same time, he knew that when all the truth surrounding that day had come to light, someone else had been as furious and grief-stricken as he was.

But it had all been in vain.

“Both the Palace Lord and I were powerless. The evidence proving their crimes had vanished, and everything was buried beneath the peace that came afterward.”

The countless footprints left in a sandy shore were bound to disappear beneath the waves that rolled in afterward.

But Baeksang remembered. He had carved the faces of those who had turned away from his child in danger into his flesh and bones, then chewed over them in his heart.

Baeksang had believed they were all walking side by side across the vast sandy shore called the Central Plains. But in truth, his people had merely been sent to the front because they were foreigners.

“I cannot forget any of it, nor can I turn it back. So why are you…!”

Baeksang, who had been about to raise his voice, suddenly stopped.

He had seen the sorrow clouding the Beast Miao King’s face.

“Do you think I forgot? This useless father, who had no choice but to send his children on ahead?”

More than fifty years ago.

The Beast Miao King’s children had been among the ten thousand warriors who headed for the Central Plains, and they never set foot on Nanman soil alive again.

“I still regret it. I wonder what would have happened if I had not become the Palace Lord of the Nanman Beast Palace, if I had not gone to the battlefield. What if I had at least rejected those children’s request to fight alongside their father?”

“……”

“Your words are right, little brother. We were powerless. We were consumed by fury and howled with grief, but there was nothing we could do. Yet we had to return to Nanman. Everyone was exhausted. We could not push away the peace that had come after ten years and begin another war.”

The Beast Miao King let out a hollow laugh. At the time, the gap between Nanman, which was merely one of the powers of the Outer Lands, and the Central Plains had been overwhelming.

No—even compared with the Zhongnan Sect alone, Nanman had been at a relative disadvantage.

Venerable Wusang, who had been the Sect Leader at the time, was respected by many for his bearing as a Great Hero. When that man lost his life in the final battle at Great Snow Mountain, countless sects and martial artists came to Mount Zhongnan.

“I merely made a choice. Between the dead and the living, between revenge and the greater cause.”

Everything that happened afterward was known to everyone.

The Beast Miao King led the survivors back to Nanman, where he faced the countless accusations poured out by those who had lost their families.

“My life was filled with regrets. But I never regretted that choice—not even once. Because we united as one, grew stronger and more prosperous than before, and gained the power to hold the criminals of the past to account.”

Baeksang’s face hardened at the story he had never heard before. Yet at the same time, an emotion he could not understand was mixed into his gaze as he looked at the Beast Miao King.

“But you will side with the Central Plains again this time.”

The Beast Miao King answered without a moment’s hesitation.

“Yes. I will.”

“Why in the world…”

“Just because one tree is diseased, burning down the entire forest would be foolish.”

“……!”

“What must be uprooted is the cause that made the tree diseased. If we recklessly burn the forest, the next place those flames will reach is us.”

The Beast Miao King continued as though lamenting.

“That was what the Demonic Cult did in the past, and what Dark Heaven is doing now. We fought to protect the forest. This land is part of that forest too.”

Neither the people of the Central Plains nor the people of Nanman acknowledged it, but the Beast Miao King knew.

Though they lived far apart, they shared the forest called the world.

And…

“You know that too, Baeksang.”

The person who understood it best was his sworn younger brother—the man now looking at him with shaken eyes.

“I know. I know that no matter what this foolish older brother says, none of it will reach your ears. You will say that it is an old affair you no longer even remember, and that the Baeksang of that time died a long time ago.”

The Beast Miao King’s children had been killed by the Demonic Cult, but Baeksang’s only child had been sacrificed because people he had believed were allies turned their backs on him.

The scale and depth of their anger toward the Central Plains could not possibly be the same.

But the Beast Miao King had watched Baeksang for a long time. He had already guessed.

“If you do not stop walking down this path… you will regret it. You will regret it as you did in the past, as you do now, and as you will in the future.”

Baeksang wanted to answer.

*I will not regret it.*

For Hwi, the child who was no different from his entire world, he could do anything.

While alive, he was willing to be called a vengeance fiend. Even in death, he would gladly smile and walk this path if people called him a Fiend.

*Then why…*

Why? Why in the world?

Why would the thought he had repeated hundreds and thousands of times in his heart over the years refuse to pass through his lips at this very moment?

Even though he had already walked down a path from which he could never return, why?

*Why are you doing this, Baeksang?*

And at the moment Baeksang asked that question, unable to answer it within his hollow heart, the Beast Miao King’s quiet voice pierced his ears.

“I can step down from the position of Palace Lord.”

Baeksang’s pupils shook at the unexpected words. But the Beast Miao King continued in a calmer voice than ever.

“You did not hear me wrong. If you want it, I will give up the position of Palace Lord right now.”

Baeksang was confused. If the position of Palace Lord became vacant, one of the remaining great chieftains would become the new Palace Lord through the Tribal Grand Council.

But with Heugung and Yohi, the two great chieftains, gone, the meaning of the Beast Miao King’s proposal was obvious.

“You would appoint me, of all people, as the new Palace Lord?”

“Yes. You heard me correctly.”

“Palace Lord. Have you gone mad?”

“Could that be possible?”

The Nanman Beast Palace was truly governed by thirty-two tribal chieftains, but the authority carried by the name of Palace Lord could not be ignored.

And yet, in a situation like this, he was making such an absurd proposal.

“What in the world is this…”

Baeksang stared at the Beast Miao King in incomprehension, then suddenly closed his mouth.

For a moment, he had realized something from the man’s unusually calm, almost detached manner.

*No way.*

A thought flashed through his mind like a streak of lightning.

At the same time, the Beast Miao King slowly opened his mouth.

“Half a shichen. Half a shichen will be enough. Open a path for them.”

The amount of time called half a shichen, and the two words *for them*.

That alone was enough to turn his guess into certainty.

Baeksang asked in a voice boiling with emotion.

“Why in the world? What reason could you possibly have to go this far?”

The Beast Miao King’s answer came without the slightest tremor or hesitation.

“Because they came to help us. Just as we once did.”

“……!”

“And I will help you. As I always have.”

*It is already too late for that.*

Baeksang muttered the words inwardly as though spitting them out, then called for the Captain of the Guards waiting outside.

Or tried to.

For some reason, neither his feet nor his lips would move.

Baeksang slowly closed his eyes. The voice he should have let go long ago still lingered in his ears.

*How much more blood do you intend to spill, Baeksang?*

* * *

The figures moving through the darkness were quiet and stealthy.

Sssshh!

The figures shot toward a single destination at blinding speed, splitting the wind and shaking the leaves.

And by the time someone noticed what was happening, everything was already too late.

Sssht—thud!

A body stiffened and fell. One of the figures caught the torch from his hand and moved his lips.

“Open the underground prison.”

Fwoosh.

Above the wavering torch flame, Yayul Mok’s face appeared.
```

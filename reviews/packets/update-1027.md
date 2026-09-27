<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1027.txt",
      "sha256": "6f948413147f267608b68c2a66d1a2847dd36a7691fafe798024257e006f4150",
      "bytes": 12869
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "55ebb4efb026afb721897fdef8566b3774f59ee99c773c6a45f24dde7b2592e7",
      "bytes": 1690
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "046f3071032d8c15b2687fbc02349b692cc95bf08c9f42b52911e659d45a859e",
      "bytes": 239514
    },
    {
      "path": "characters/Baeksang.md",
      "sha256": "6113875b6ea7c3e78fc8b23c17f01926760b3c69e3dc1946ab37e8254cbfd861",
      "bytes": 935
    },
    {
      "path": "characters/Blood-Sword Demon Lord.md",
      "sha256": "7d06b1a7fe13f4d0f1eddc2370be6a4cc0a117e45353cdca22bb261af3408a61",
      "bytes": 659
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "a85adddbda9317a1a589f548aa9164429a9957f5ee12c346df5708ff1192c5bc",
      "bytes": 760
    },
    {
      "path": "characters/Eastern Heaven Demon Lord.md",
      "sha256": "9261123075c8e16d24955c28cc2c2a6b4265d3a1fe205ef58c34a3c4a4438b67",
      "bytes": 838
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "8f85bdf5730e9a78bc74107c72595542dca44da9d0317b387dbd6dc408aa8dd4",
      "bytes": 1502
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "9b53bd5fb0a17664db51991398c74a18d42308b4bb2167e0bda88e57cbd04f3d",
      "bytes": 1682
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "42927669459622c70ffeca092692f092b03060040257aa2546b3fc60308bc73a",
      "bytes": 623
    },
    {
      "path": "characters/Mae Jonghak.md",
      "sha256": "de4cd78097a26a6cc4157d64f42a519293ca8f0dc3bdbbe9b33c4340e842797e",
      "bytes": 1083
    },
    {
      "path": "characters/Sama Pyo.md",
      "sha256": "94a393060f0c8b9e69e07834e694de3d869ca8e2be004821c26a86867ff7f810",
      "bytes": 1069
    },
    {
      "path": "characters/Tang Sadok.md",
      "sha256": "1f18503b17feb35823a0df33855839ee1e1e2a9a3f528d2576517eeb302c30ce",
      "bytes": 925
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "fcf67bc6cfbc70c2a257c30ba7ba70cada7f28488513fed7350a8eac519e333f",
      "bytes": 278187
    }
  ],
  "estimated_tokens": 13557
}
-->

# Durable State Update — Chapter 1027

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

For each matched character, check whether this chapter adds clear, durable
evidence that improves Role, Personality, Voice, or Relationships. Update a
field when it corrects or meaningfully sharpens the existing profile; otherwise
leave it unchanged. Voice guidance should capture observable register, cadence,
word choice, or address habits that help distinguish the character in English.
Do not infer a stable voice from one situational line or generic personality
adjectives. Keep “Not established” only when this chapter provides no reliable
voice evidence; never replace it with unsupported specificity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 1027. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1027. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history. For a new profile, describe voice only when the chapter supports
a useful, stable distinction; otherwise say “Not established”.
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
  "chapter": 1027,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1027,
    "continuity_sources": [1027],
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
    "Dark Heaven captured Dunhuang after breaching the Jade Gate Pass, with catastrophic losses for the defenders.",
    "Dark Heaven holds one thousand prisoners and threatens to kill them if the proposed meeting conditions are broken.",
    "Jin Taekyung, Jeok Cheongang, and Sama Pyo are going to Dark Heaven’s unarmed, three-person meeting; Sima Gong and the Wind-and-Cloud Sword Lord remain with the defenders.",
    "An unknown visitor is approaching the meeting party on horseback.",
    "Dark Heaven’s new Demon Lord wishes to meet the defenders; the Lord’s identity and reason remain unknown.",
    "An unidentified killer slew all one hundred Great Snow Mountain scouts with identical single-sword strikes; Jeok Cheongang recognizes the wounds but cannot identify the technique.",
    "The Kongtong Sect Leader appears to have escaped Dark Heaven’s pursuit; his whereabouts remain unknown.",
    "Sama Pyo received a secret letter, and Sima Gong ordered him to watch Taekyung’s group; the letter’s sender and contents remain unexplained."
  ],
  "continuity_sources": [
    1025,
    1026
  ],
  "open_questions": [
    "Who is the approaching visitor, and what does the meeting hold for the defenders?",
    "Who is the new Demon Lord, and what is the purpose of the offer?",
    "What will happen to the thousand prisoners?",
    "Who killed the Great Snow Mountain scouts, and what is the origin of the sword technique?",
    "Who sent Sama Pyo the secret letter, what did it say, and are Sima Gong’s orders involving Pyo and Taishan connected to Dark Heaven?"
  ],
  "safe_through": 1026,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 매종학    | **Mae Jonghak**    |
| 검성     | **Sword Saint**               | Mae Jonghak    |
| 창왕     | **Spear King**                | —              |
| 독왕     | **Poison King**               | Tang Taesang   |
| 일신     | **One God**         |
| 태원진가   | **Jin Family of Taiyuan**        |
| 화산파    | **Huashan**                      |
| 암천     | **Dark Heaven**                  |
| 사천당가   | **Sichuan Tang Clan**            |
| 무인     | **martial artist**                               | Default term                                          |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 살기     | **killing intent**                               |                                                       |
| 마교     | **Demonic Cult**                                 |                                                       |
| 강호     | **martial world**                                | Prefer “Murim” where the setting itself is meant      |
| 가주     | **Family Head**                              |
| 장문인    | **Sect Leader**                              |
| 장로     | **Elder**                                    |
| 대장로    | **Head Elder**                               |
| 제자     | **Disciple**                                 |
| 선배     | **Senior**                                   |
| 시스템              | **System**                     |
| 습득               | **Acquired**                   |
| 태원     | **Taiyuan**            |
| 사천     | **Sichuan**            |
| 화산     | **Huashan**            |
| 구화산    | **Mount Jiuhua**       |
| 정마대전   | **Great Faction War**         |
| 노부      | **this old man / I**                                            |
| 백상 | **Baeksang** | Great chieftain of the Bai people and Yayul Cheok's sworn younger brother. |
| 혈검마군 | **Blood-Sword Demon Lord** | Antagonist commanding the army advancing on the Great Snow Mountain. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 동천마군 | **Eastern Heaven Demon Lord** | Title of the absurd masked antagonist in Jin's nightmare. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 사마표 | **Sama Pyo** | Young Sect Leader of the Black Dragon Demon Gate. |
| 당사독 | **Tang Sadok** | Current Family Head of the Sichuan Tang Clan; also called the Myriad-Poison Asura. |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 검강 | **Sword Force** | Higher manifestation than Sword Energy; Pung Yang's is explicitly imperfect because of insufficient enlightenment. |
| 오대세가 | **Five Great Families** | Major Murim grouping. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 강자지존 | **Might Makes Right** | Murim principle invoked as the basis for Mae Jonghak's challenge. |
| 태상가주 | **Grand Family Head** | Title held by the Azure Sky Sword King as head of the Nangong Family. |
| 양천 | **Yangcheon** | Shanxi-area location near which a small martial arts academy operates. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 일각 | **fifteen minutes** | Quarter of a shichen; used for the remaining completion time. |
| 노환 | **infirmities of old age** | Jeok Cheongang's age-related illness. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 천산 | **Tianshan** | Mountain region identified as the Demonic Cult's headquarters. |
| 천주 | **Lord of Heaven** | Authority invoked by the masked attackers. |
| 천독마군 | **Heaven-Poison Demon Lord** | Archfiend of the Heavenly Demon Divine Cult and former second-in-command of the Demonic Cult. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 준이 | **Jun** | Family nickname used in the form Jun's dad. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 당가 | **Tang Family** | Short form for the Sichuan Tang Clan when distinguished from 사천당문. |
| 삼노 | **Three Old Men** | Mocking designation used by the Western Heaven Demon Lord for the aged Qilian Three Fiends. |
| 신교 | **Divine Cult** | Short form used by the Divine Cult's members for the Heavenly Demon Divine Cult. |
| 오대 | **Five Squads** | Named Tang Clan organizational group in Tang Sadok's mobilization order. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 교주 | **Cult Leader** | Leader of the Divine Cult. |
| 마두 | **fiend** | Demonic martial masters from the Great Faction War era. |
| 열화신룡 | **Blazing Flame Divine Dragon** | New sobriquet bestowed on Jin Taekyung. |
| 무한 | **Wuhan** | Capital of Hubei Province near Dongting Lake. |
| 암초 | **reef** | Reefs blocking the narrow water route. |
| 살귀 | **Killing Ghost** | Mungyeong's earlier sobriquet before he became the Slaughter Saint. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 인자 | **ninja** | Japanese assassin skilled in concealment and concealed weapons. |
| 식경 | **half an hour** | Time limit given for the requested reports. |
| 부산 | **Busan** | City where the Haeundae Gate crisis occurs. |
| 서리 | **seori** | Colloquial term for stealing crops or produce from a field. |
| 검마 | **Sword Demon** | A Demonic Cult swordsman whose final technique is compared with One Annihilation. |
| 해남 | **Hainan** | Island region reached by sailing south from Guangxi. |
| 화신 | **Fire God** | A local deity worshiped by one Nanman believer. |
| 천산삼노 | **Three Elders of Tianshan** | The three former Demonic Cult fiends serving the Blood-Sword Demon Lord. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 매종학 | 진태경 | older_ally_to_younger_friend | friend | casual-familiar | Mae Jonghak uses 친구 when arriving at Taekyung's window and asking to talk. |
| 진태경 | 당사독 | visitor_to_Sichuan_Tang_Family_Head | Great Hero Tang Sadok | formal-deferential | Taekyung formally introduces himself and addresses Tang Sadok as 대협. |
| 당사독 | 진태경 | Family_Head_to_visiting_younger_martial_artist | you; fearless brat | blunt and threatening | Tang Sadok uses 너 and later calls Taekyung 겁 없는 놈 while rejecting his challenge. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 중년인 | 진태경 | veteran civilian Hunter to celebrated allied Hunter | Mr. Jin | formal-polite and awed | The casualty clerk addresses Jin as 진 선생님 after Jin asks him to list Lei Fei among the dead. |
| 진태경 | 중년인 | celebrated Hunter to older fellow Hunter | sir | casual and teasing | Jin addresses the older Hunter as 아저씨 while joking with him and giving him instructions. |
| 매종학 | 적천강 | long-standing martial rival and friend | Great Hero Jeok | casual and familiar | Mae addresses Jeok as 적 대협 while discussing the Alliance Leader position. |
| 적천강 | 매종학 | long-standing martial rival and friend | you | blunt and familiar | Jeok addresses Mae as 당신 while recalling their meeting at Mount Jiuhua. |
| 진태경 | 매종학 | younger ally to newly installed Alliance Leader | Alliance Leader | formal and deferential | Uses 맹주님 while formally greeting Mae Jonghak as the Alliance Leader. |
| 사마표 | 적천강 | Young Sect Leader to legendary elder | Great Hero Jeok | formal-deferential | Sama Pyo formally pays his respects to Jeok Cheongang as the Fire King. |
| 적천강 | 사마표 | legendary elder to unorthodox Young Sect Leader | you / young brat | blunt, suspicious, and contemptuous | Jeok addresses Sama Pyo with 네놈 and 어린놈 while probing his lineage and motives. |
| 사마표 | 진태경 | prospective recruit to pavilion master | you | polite, controlled, and candid | Sama Pyo uses 자네 while asking about Taekyung's attitude and admitting his intention to use him. |
| 진태경 | 사마표 | pavilion master to prospective recruit | you / that guy | blunt, informal, and distrustful | Taekyung speaks to and about Sama Pyo with casual forms such as 녀석 and 저놈. |
| 백상 | 진태경 | Nanman great chieftain to Murim Alliance Pavilion Head | you bastard | cold, hostile, and contemptuous | Baeksang calls Jin a Han Chinese man, rejects his status, and orders him to leave. |
| 진태경 | 백상 | Murim Alliance Pavilion Head to Nanman great chieftain | you | polite but deliberately provocative | Jin tells Baeksang that Nanman's blood was shed for the world rather than merely for the Central Plains. |
| 백상 | 대장로 | Palace Lord to Miao Head Elder | Head Elder | cold, coercive, and formal | Baeksang offers the Head Elder a final chance to submit before ordering his imprisonment. |
| 대장로 | 백상 | Miao Head Elder to usurping Palace Lord | Baeksang / you bastard | furious and defiant | The Head Elder condemns Baeksang's betrayal and refuses to abandon Yayul Cheok. |
| 백상 | 중년인 | Nanman Palace Lord to civilian tribesman | you | controlled and grave | Baeksang orders the middle-aged man to flee with his mother and the other civilians through the East Gate. |
| 중년인 | 백상 | Nanman civilian to betrayed Palace Lord | you | hostile, fearful, and grieving | The middle-aged man confronts Baeksang while protecting his mother and condemns him for the deaths and destruction. |
| 진태경 | 황제 | guest of the Emperor’s younger brother addressing the Emperor | Your Majesty | formal and deferential in address, despite blunt challenges | Taekyung repeatedly addresses the Emperor as 폐하. |
| 황제 | 진태경 | Emperor addressing a subject and Prince Shangshan’s guest | Jin Taekyung | formal and authoritative | The Emperor addresses Taekyung by his family and personal name before asking what to do with the two officials. |
| 적천강 | 동천마군 | enemies | you | blunt and informal | Jeok Cheongang addresses the Eastern Heaven Demon Lord with hostile familiarity. |
| 동천마군 | 적천강 | enemies | you | informal | The Eastern Heaven Demon Lord speaks to Jeok Cheongang during their duel. |
| 황제 | 동천마군 | former ruler addressing a former subject, now an enemy | you | measured and formal | The Emperor asks why the Demon Lord betrayed his father, the late Emperor. |
| 동천마군 | 황제 | former subject addressing the Emperor, now an enemy | you; you bastards | hostile and contemptuous | He denies ever being loyal to the imperial family and accuses the rulers of betrayal. |
| 진태경 | 동천마군 | young martial artist confronting an enemy | ugly-ass big bro | casual, profane, and taunting | Jin calls out to the Demon Lord after returning to the hall. |
| 동천마군 | 진태경 | enemy recognizing the spear wielder | Jin Taekyung | shouted, informal | The Demon Lord cries Taekyung's name after identifying him as the spear's owner. |
| 황제 | 신의 | Emperor addressing a physician | Divine Physician | direct and familiar | The Emperor asks whether the Divine Physician left something behind. |
| 신의 | 황제 | physician addressing his patient and sovereign | Your Majesty | formal and deferential | The Divine Physician addresses the Emperor as 폐하 while explaining the treatment. |
| 혈검마군 | 삼노 | former Demonic Cult fiend to subordinate | Elder Three | familiar and contemptuous | Addresses the wounded elder as 삼노 while asking how he compares to the Fire King. |

## Listed compact profiles

### Baeksang.md

# Baeksang (백상)

- **Safe through:** Chapter 925
- **Aliases:** None
- **Role:** Baeksang was the Palace Lord of the Nanman Beast Palace and sole Great Chieftain of Nanman, and he died by the Beast Miao King's hand after confessing to serving Dark Heaven's plan.
- **Personality:** Cold, rigid, meticulous, and strategically resolute, yet burdened by regret, grief over Hwi's death, and a final conflicted impulse to spare others from the coming bloodshed.
- **Voice:** Rigid, formal, restrained, and emotionally distant.
- **Relationships:** Baeksang is Yayul Cheok's sworn younger brother and childhood companion, Yayul Mok's sworn uncle, and the father of Baekhwi, whom he believed the Great Snow Fiend killed but Dark Heaven has kept alive in a deep sleep; he cultivated Yohi with gold and influence and used her support to advance Dark Heaven's preparations.

### Blood-Sword Demon Lord.md

# Blood-Sword Demon Lord (혈검마군)

- **Safe through:** Chapter 1024
- **Aliases:** None
- **Role:** The Blood-Sword Demon Lord is a formidable martial master who commands the force advancing on the Great Snow Mountain and now serves the Lord of Heaven.
- **Personality:** Contemptuous of his former master, he is certain of his new cause and treats those weaker than himself with ruthless disdain.
- **Voice:** Not established
- **Relationships:** He once served the Heavenly Demon and now serves the Lord of Heaven; he has been ordered not to kill Jin Taekyung and wants to meet him.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1024
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Eastern Heaven Demon Lord.md

# Eastern Heaven Demon Lord (동천마군)

- **Safe through:** Chapter 985
- **Aliases:** Wei Zhong
- **Role:** The Eastern Heaven Demon Lord was Wei Zhong, the East Depot’s Seal-Holding Eunuch and a former Maoshan Sect disciple who commanded the dead with a bell; Jin Taekyung killed him with blue-white flames.
- **Personality:** His hatred grew from losing his family and sect, but recognizing his own lonely childhood in Zhu Bao ultimately moved him to relinquish his vengeance and choose a less harmful final act.
- **Voice:** He speaks in measured, almost lyrical phrasing, recounting the past before turning to pointed accusations.
- **Relationships:** Ma Sanbao is his Disciple; he holds the Emperor responsible for Taizu’s actions against the Maoshan Sect.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 1026
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; he distrusts process-first excuses when outcomes fail and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, and insists on protecting Taekyung while urging him not to risk his life; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy, and personally killed his former ally the Junzi Saber after that man joined the Demonic Cult.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1026
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan and the original owner of his current body, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master who can detect and eavesdrop on nearby Sound Transmissions subject to the participants’ relative levels, and a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure, willing to risk himself for others, and unwilling to excuse cruelty as the inevitable price of survival.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; Hyuk Mujin trusts Taekyung to fight beside him and feels no fear when Taekyung is with him; Peng Cheolhu regarded Taekyung as a worthy successor, and the Bow Saint relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1026
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Mae Jonghak.md

# Mae Jonghak (매종학)

- **Safe through:** Chapter 997
- **Aliases:** Sword Saint
- **Role:** Sword Saint and Cheongpung's grandfather who now serves as the New Murim Alliance's Alliance Leader and has ordered Jin Taekyung's first Fire Dragon Pavilion mission to Nanman.
- **Personality:** Playful and easygoing in ordinary company, yet guided by a principled commitment to chivalry that can outweigh strategic caution.
- **Voice:** Friendly, casually familiar, and cheerfully teasing, including when greeting old acquaintances and discussing leadership.
- **Relationships:** Cheongpung's grandfather and martial instructor; taught him the Taeeul Miri Palm; secretly entered Huashan while its Sect Leader slept, left a dagger and handwritten note, and then went into hiding, prompting Huashan's search; fought Jeok Cheongang at Mount Jiuhua more than forty years ago and left after their draw; his old friend Hong Dao left him a letter identifying Jin Taekyung as the Morning Star who would drive away darkness.

### Sama Pyo.md

# Sama Pyo (사마표)

- **Safe through:** Chapter 1026
- **Aliases:** Black Dragon Saber
- **Role:** Young Sect Leader and heir of the Black Dragon Demon Gate, a Morning Star reputed to be no less than the Ten Dragons and Phoenixes.
- **Personality:** Outwardly courteous and calculating, he is protective of Taishan and pragmatic in combat; he recognizes that his father's ruthless, survival-driven worldview shaped him, even as its influence weighs on him.
- **Voice:** Polite and ingratiating in public, with sardonic humor and controlled evasiveness.
- **Relationships:** Sama Pyo commands the absolutely loyal Taishan and is Sima Gong's son and heir; his father's ruthless treatment of family shaped his rise and remains a source of inner constraint. He joined the Fire Dragon Pavilion intending to use Jin Taekyung, and Sima Gong has now ordered him to spy on Taekyung's group. He was Ju Hwaran's former fiancé in a political engagement and is openly hostile toward fellow member Song Ilseom.

### Tang Sadok.md

# Tang Sadok (당사독)

- **Safe through:** Chapter 853
- **Aliases:** Myriad-Poison Asura
- **Role:** Current Family Head of the Sichuan Tang Clan, overseeing its recovery and relying on allied martial artists to help treat patients and guard against another Dark Heaven attack.
- **Personality:** Blunt and unsentimental, yet grateful to those who remain with the Tang Clan; he has consciously chosen to change and speaks candidly about the clan’s vulnerability.
- **Voice:** Hissing, curt, authoritative, and threatening.
- **Relationships:** Tang Taesang was his father and predecessor, his unnamed nephew serves as Master of the Gatekeeper Pavilion, Mimi is his cherished old friend and companion temporarily entrusted to Cheongpung, and he regards Jin Taekyung and Cheongpung as benefactors, openly welcoming Jin with a warmth he usually conceals.

## Korean source

```text
＃1027화



그런 이들이 있다.

주머니를 뚫고 튀어나온 송곳처럼, 바다 한가운데에 우뚝 선 암초처럼, 황야의 들꽃처럼 단연 눈에 띄는 이들이.

그리고 지금 이 순간, 경치를 감상하듯 여유로운 기색으로 가까워지는 그자 역시 마찬가지였다.

다그닥, 다그닥.

천천히 나아가는 말발굽을 따라 흔들리는 잿빛 머리카락.

그리 준수하지도, 못나지도 않은 평범한 이목구비를 지닌 중년인의 동공은 세로로 길게 찢어져 있었다.

하지만 그런 중년인을 유독 돋보이게 만드는 특색이 있다면, 그것은 화염보다도 붉고 그와는 비교도 안 될 만큼 섬뜩한 핏빛 안광(眼光)이었다.

“이렇게 보는 건 처음이로군. 반갑소, 적 선배.”

선배라는 정중한 호칭과 웃음기가 스며 있는 목소리.

바로 그때였다.

십여 장 밖에서 멈춰 선 중년인을, 정확히는 파충류의 그것과도 같은 동공을 본 적천강의 눈동자가 크게 부풀어 오른 것은.

“네놈은 설마…….”

“일전에는 서로 갈 길이 바빠 만나지 못했었지. 참으로 안타까운 일이오. 만약 선배가 그곳에 있었다면, 구양천 그자도 지금쯤 멀쩡히 살아 있었을 테니. 안 그렇소?”

구양천.

언젠가 적천강에게 들었던, 기억 속에 있는 이름이다.

한때 오대세가에 버금가는 위세를 떨쳤다는 구양세가의 가주, 아니 마지막 생존자.

마교에 의해 멸문지화를 겪고 복수귀로 거듭난 구양천을 세상은 창왕(槍王)이라 불렀고, 그 위대한 무인은 정마대전의 끝자락에 다다른 어느 날 이름 없는 들녘에서 발견되었다.

일평생 분신처럼 여겼던 한 자루의 창과 함께, 수십 조각으로 나뉘어서.

백 명도, 천 명도 아닌 단 한 사람에 의해.

마교의 그 누구보다 피를 갈구하던 어느 살인귀에 의해.

“혈검마군(血劍魔君)…….”

나도 모르게 흘러나온 침음성에 중년인, 혈검마군이 활짝 웃었다.



* * *



노환은 참으로 무서운 병이다.

늦은 밤 그림자에 숨어 은밀히 찾아온 도둑처럼 머릿속의 기억을 하나둘씩 빼앗아 가니까.

그렇기에 구화산에 머무를 당시, 나는 적천강에게 의도적으로 옛 기억을 꼬치꼬치 캐물었다.

이렇게라도 그의 노환을 조금이나마 늦추기 위해서. 세월의 저주를 일각이라도 늦추기 위해서.

결론만 말하자면, 그건 우리 둘 모두에게 제법 괜찮은 방법이었다.

그간 대화 상대가 없었던 독거노인은 수없이 오가는 말을 통해 잊고 있던 기억을 떠올렸고, 독거노인의 말벗이 된 젊은 놈은 장장 일백 년을 넘게 살아온 노강호의 기억 속에서 이런저런 정보를 습득할 수 있었으니까.

그리고 그렇게 얻은 정보 중에는, 지금 나를 바라보며 웃고 있는 어느 살귀에 대한 것도 포함되어 있었다.

“이거 기쁜데. 자네가 날 알고 있다니.”

내가 지닌 시스템에는 다른 사람의 마음을 엿볼 수 있는 기능까지는 없다.

하지만 나는 본능적으로, 피부로 느낄 수 있었다.

혈검마군은 단순히 말뿐만이 아니라, 내가 자신을 알고 있다는 사실을 진심으로 기뻐하고 있다는 것을.

마치 어린아이와도 같은 순수함.

끔찍한 혈겁(血劫)을 쌓아 온 살인마가 가지기에는 너무나도 순수한 감정이었기에, 더더욱 소름이 끼쳤다.

“하긴, 내가 예전에는 한 끗발 날렸었지. 여기 있는 이 친구들도 제법 유명했지만, 뭐 그래봤자 마교 입장에서는 쓸 만한 빈객(賓客) 수준이었으니까.”

싱글벙글 웃으며 말하는 혈검마군의 모습에 모욕감을 느낄 법도 한데, 그와 함께 다시 돌아온 천산삼노는 경직된 표정으로 고개를 끄덕일 뿐이었다.

“배, 백번 천번 옳은 말씀이십니다.”

“저희가 어찌 감히 마군(魔軍)께 범접할 수 있겠나이까.”

“한없이 부족함에도 마군을 모실 수 있게 된 것이, 일생의 영광일 따름입니다.”

때맞춰 혈검마군의 똥꼬를 빨아 재끼는 솜씨가 보통이 아닌 것이, 이런 식이면 도대체 하루 몇 번 양치하는 거냐고 물어보고 싶었지만 생각해 보면 천산삼노 입장에서는 당연한 일이었다.

약육강식(弱肉强食), 강자지존(强者至尊).

그 누구보다 노골적으로 강함을 추구하는 자들이 소위 마인(魔人)이라 불리는 저들이고, 혈검마군은 천산삼노와는 비교도 할 수 없는 대마두(大魔頭)였으니까.

당연히 천산삼노 역시 세간의 인식으로는 대마두가 맞았다.

일신의 무위도, 정마대전으로 쌓은 흉명도 그리 불리기에 충분하다.

그러나 한 식경 전 적천강이 직접 저들의 면전에 대고 말했듯이 그들은 태생이 떠돌이 개와 같았다.

그저 다른 개들보다 훨씬 더 흉폭하고, 날카롭고 강한 이빨을 지녔을 뿐.

하지만 장장 일천여 년에 걸쳐 천하 무림과 어깨를 나란히 했던, 미친 광신도 집단에서도 유독 미쳐 있던 광견과는 비교 자체가 불가능했다.

물론, 그 미친개는 이제 다른 주인을 섬기는 것 같지만.

“마교라, 당신은 신교(神敎)라고 불러야 하지 않나?”

내가 불쑥 던진 한마디에, 조금 전 천산삼노를 두고 마교의 빈객 운운했던 혈검마군이 빙긋 웃었다.

“이미 오래전의 일이지. 알면서 묻는군. 새삼스럽게.”

“그래서, 목줄 갈아 끼우니까 밥은 제때 잘 나오고?”

“허어.”

짐짓 눈을 동그랗게 뜬 혈검마군이 적천강을 향해 고개를 돌렸다.

“적 선배. 이거 제자 교육을 어떻게 시킨 겁니까? 아무리 가는 길이 달라도 서로 예의는 지켜야 하는 것 아니오? 나처럼.”

적천강이 담담하게 대답했다.

“네 애미 애비보다는 잘 시켰으니 걱정 말거라.”

멍하니 적천강을 바라보던 혈검마군이 이내 껄껄 웃었다.

“이런. 역시 소문대로구려.”

“네놈은 소문보다 더하구나. 노부가 진즉 잡아 죽이지 못한 것이 한이다.”

“선배의 불같은 성정이야 내 잘 알고 있지, 전장에 나타났다 하면 쓸만한 놈들이 여기저기서 우르르 죽어 나빠지니, 교주가 진노했던 적이 한두 번이 아니오.”

“덕분에 네놈도 고생깨나 했겠군. 네놈이야말로 천마가 가장 가까이에 두고 아끼던 충견이 아니었느냐.”

“실망시켜서 미안하지만, 딱히 고생하진 않았소. 죽어 나가는 만큼 죽여 오면 됐거든.”

혈검마군이 웃음이 어린 목소리로 말을 이었다.

“천독(天毒), 그 멍청한 늙은이가 뒈졌을 때는 해남파(海南波) 장문인으로도 부족해서 창왕의 수급까지 가져와야 했지만, 뭐 어쩌겠소. 나도 좋아서 했던 일인데.”

“천독? 천독마군을 말하는 것이냐?”

“글쎄, 그 외에 다른 천독이 있던가?”

천독마군은 나 역시도 아는 별호다.

천마의 뒤를 이은 마교의 이 인자이자, 이제는 죽고 없는 사천당가의 태상가주, 독왕(毒王) 당사독조차 넘을 수 없었다던 벽.

그랬던 그는 어느 날 화산파의 제자들과 전장에서 맞닥트렸고, 바로 그날 최후를 맞이했다.

노을을 짓누를 만큼 찬란한 자줏빛 검강을 뿜어내는 누군가에 의해.

“검성(劍星), 아니 이제 맹주라고 불러야 하나? 여하튼 매종학에게는 내심 고마운 마음을 품고 있었소. 천독 그 늙은이, 평소에 나를 보던 시선이 영 심상치 않았거든. 다행히도 늦지 않게 죽어준 덕분에 일이 잘 풀렸지.”

신이 난 얼굴로 떠들어 대는 혈검마군을 말없이 지켜보던 나는, 놈이 마지막에 덧붙인 한마디에 미간을 좁혔다.

‘덕분에 일이 잘 풀렸다, 고?’

고수의 상실은 곧 전력의 공백.

그런 의미에서 천독마군의 죽음은 마교에 있어 엄청난 타격이었을 것이다.

그런데도 저렇게 말한다는 건…….

“그때부터였군. 목줄을 바꿔 낀 것이.”

내가 불쑥 던진 말에 혈검마군이 눈살을 찌푸렸다.

“목줄을 바꿨다는 표현은 좀 그렇긴 하지만…… 뭐, 편한 대로 생각하게.”

정마대전이 종결되기도 전에 암천이 등장했다는 사실은 이미 익히 알고 있던 사실이다.

태원진가의 대장로, 남만아수궁의 백상과 황제의 최측근이었던 동천마군까지.

시간을 거슬러 올라가면 암천은 정마대전의 초기부터 태동하고 있었다.

아니, 어쩌면…….

‘정마대전의 시작이, 암천으로 말미암은 것일 수도 있다.’

순간 서늘해지는 등골을 느끼며, 나는 혈검마군을 향해 입을 열었다.

“도대체 언제부터지?”

“언제부터냐니, 그게 정확히 무슨 뜻인지 모르겠군.”

“너희들이, 천주(天主)가 나타난 것이.”

그 순간.

화아아악!

바람이, 강렬한 기의 폭풍이 휘몰아쳤다.

지면을 뒤덮고 있던 새하얀 눈이, 서리가, 그 안에 숨어 있던 흙과 모래가 사방으로 휘날리다 빠르게 가라앉았다.

파스슥.

천천히 떨어져 내리는 자연의 부산물, 그 아래에는 착 가라앉은 눈빛으로 나를 응시하는 혈검마군이 있었다.

“예의가 없군. 확실히.”

웃음기가 사라진 입가와 나지막하게 울리는 목소리.

얼핏 들으면 침착해 보이는 놈의 음성 안에는, 차가운 용암이 흐르고 있었다.

“참으로 희한해. 어느 정도는 이해가 되면서도, 도무지 알 수가 없단 말이지. 그분께서는 굳이 왜…….”

문득 말꼬리를 흐린 혈검마군이, 이내 사람 좋은 얼굴로 웃어 보였다.

“뭐, 그분께서 행하시는 모든 일에는 다 이유가 있겠지. 언제나 그렇듯이. 다만 한 가지 확인하고 싶었을 뿐일세.”

무엇을, 이라고 되물을 필요는 없었다.

다음 순간, 천천히 손을 들어 올리며 혈검마군이 말을 이어갔으니까.

“열화신룡 진태경. 자네는 강해. 내가 피 튀기는 혈전(血戰)을 마다할 만큼. 그리하여 혹 그분께 패배라는 불경을 저지르지 않을까 우려될 만큼.”

보인다. 들린다.

나를 향한 혈검마군의 눈빛과 목소리가.

동시에 느껴진다.

그 안에 담긴 순수한 경탄(敬歎)이.

그리고…….

그 안에 미세하게 숨어 있는 살기(殺氣)가.

“자네의 그 무한한 잠재력과 의협심에 감복했네. 이것만큼은 진심이야.”

“……!”

“……!”

“……!”

그것은 한순간에 벌어진 일이었다.

나와 적천강. 마지막으로 묵묵히 자리를 지키던 사마표까지.

우리가 지면을 박차고 쇄도하는 순서와 시간의 흐름에는 차이가 있을지언정, 아마도 그 안에 담긴 간절함만큼은 같았을 것이다.

드득.

발끝을 따라 흙이 파인다. 모래가 부서진다.

단전에서 솟구친 공력이 한껏 수축한 하체의 근육으로 흘러 들어가고, 이내 폭발했다.

콰아앙!

느려진 세상 속, 풍경이 뒤바뀌었다.

십여 장의 공간을 지우며 우리는 쏘아졌다.

지금 이 순간 적천강과 나는 두 줄기의 맹렬한 불꽃이었고, 사마표는 소리 없는 바람이었다.

그리고 느려진 시간의 흐름 속에서, 불꽃과 바람을 가로막는 세 개의 벽이 솟아올랐다.

“갈(喝)-!”

목소리는 셋이요, 외침은 하나다.

천산삼노.

한낱 떠돌이 개 취급을 받기에는 너무나도 강대한 힘을 지닌 천산의 세 마두가 참고 있던 분노와 기운을 터트렸다.

아득한 세월 동안 서로가 서로를 위해 맞춰 왔던 자연스러운 합격술(合格術)이, 세 개의 벽을 뭉쳐 하나의 거대한 벽으로 탈바꿈시켰다.

콰앙!

천지를 떨어 울리는 일합(一合)의 격돌.

그리고 찰나를 쪼개고 쪼갠 짧은 시간을 가득 메운 그 거대한 굉음과 힘의 파동 속에서, 하늘을 향했던 혈검마군의 손이 마침내 떨어져 내렸다.

마치, 언덕 위에서 오직 하나의 명령만을 기다리고 있던 무수한 칼날들과 같이.

“참(斬)!”

서걱! 푸푸푹!

일천여 개의 목이 굴러떨어지던 그 순간, 혈검마군과 눈이 마주친 나는 전신의 피가 차갑게 식는 것을 느꼈다.

놈은 웃고 있었다.
```

## Final English reading copy

```markdown
# Chapter 1027

There are people who stand out.

Like an awl poking through a pocket. Like a reef rising from the middle of the sea. Like a wildflower blooming in the wilderness.

And right now, the man approaching with the leisurely air of someone admiring the scenery was one of them.

Clip-clop. Clip-clop.

Gray hair swayed with the slow rhythm of the horse’s hooves.

The middle-aged man had ordinary features—neither particularly handsome nor ugly—and pupils that were long and vertically slit.

But if there was one thing that made him stand out, it was his gaze: redder than flame, and infinitely more chilling.

“This is the first time we’ve met like this. It’s good to see you, Senior Jeok.”

The respectful address, the smile in his voice.

That was when it happened.

Jeok Cheongang’s pupils widened as he looked at the middle-aged man who had stopped a dozen or so yards away. More precisely, as he looked at those reptilian pupils.

“You can’t be…”

“We were both too busy to meet the last time. What a shame. If you’d been there, Goyangcheon would still be alive and well by now. Don’t you think?”

Goyangcheon.

A name I remembered from something Jeok Cheongang had told me once.

The Family Head of the Goyang Family, which had once wielded power to rival the Five Great Families—or rather, its last survivor.

After the Demonic Cult wiped out his family, Goyangcheon became a vengeful ghost. The world called him the Spear King, and that great martial artist was found one day in an empty field near the end of the Great Faction War.

He’d been cut into dozens of pieces, alongside the spear he’d considered an extension of himself.

Not by a hundred men, or a thousand. By a single person.

A killer who craved blood more than anyone in the Demonic Cult.

“The Blood-Sword Demon Lord…”

A low groan slipped out of me. The middle-aged man—the Blood-Sword Demon Lord—broke into a wide smile.

* * *

The infirmities of old age are a frightening thing.

Like a thief creeping in under cover of night, they steal away your memories one by one.

That was why, when I was staying at Mount Jiuhua, I deliberately pestered Jeok Cheongang with questions about his old memories.

To slow his illness, even if only a little. To delay the curse of time by even a moment.

In the end, it turned out to be a pretty good arrangement for both of us.

The old man, living alone with no one to talk to, recalled forgotten memories through our countless conversations. And the young man who kept him company picked up all kinds of information from the memories of a veteran martial artist who’d lived for more than a hundred years.

Among the things I’d learned was something about the killer who was now looking at me with a smile.

“I’m glad. You know who I am.”

The System I had couldn’t read other people’s minds.

But instinctively, I could feel it.

The Blood-Sword Demon Lord wasn’t merely saying he was glad I knew him. He was genuinely pleased.

There was a childlike innocence to it.

It was far too pure an emotion for a murderer who’d piled up horrific bloodshed. That only made it more unsettling.

“Still, I used to be somebody. These friends here were fairly famous, too, but from the Demonic Cult’s point of view, they were no more than useful guests.”

The Blood-Sword Demon Lord spoke with a beaming smile. The Three Elders of Tianshan, who might have felt insulted by the remark, only nodded stiffly.

“Y-You are right in every way, a hundred times over.”

“How could we ever presume to compare ourselves to the Demon Lord?”

“Though we are utterly lacking, being allowed to serve the Demon Lord is the honor of a lifetime.”

Their skill at kissing the Blood-Sword Demon Lord’s ass on cue was something else. I wanted to ask how many times a day they brushed their teeth if they kept at it like this, but when I thought about it, it was only natural from their perspective.

Might Makes Right. The strong rule.

Those called fiends were the ones who pursued strength more openly than anyone else, and the Blood-Sword Demon Lord was a great fiend beyond comparison to the Three Elders of Tianshan.

Of course, by the world’s standards, the Three Elders of Tianshan were great fiends, too.

Their individual martial prowess and the infamy they’d earned during the Great Faction War were enough to justify the title.

But as Jeok Cheongang had said to their faces half an hour ago, they were born stray dogs.

Just far more vicious, with sharper and stronger teeth than the other dogs.

Still, there was no comparing them to the one mad dog who stood out even among that insane cult of fanatics, a group that had stood shoulder to shoulder with the Murim world for more than a thousand years.

Of course, that mad dog seemed to serve a different master now.

“The Demonic Cult? Shouldn’t you call it the Divine Cult?”

At my sudden question, the Blood-Sword Demon Lord smiled. A moment ago, he’d been talking about the Three Elders as useful guests of the Demonic Cult.

“That was a long time ago. You know that already, so why ask now?”

“So, with a new collar on, do they feed you on time?”

“Goodness.”

The Blood-Sword Demon Lord widened his eyes in mock surprise and turned to Jeok Cheongang.

“Senior Jeok, how did you teach your Disciple? Whatever path we’ve taken, shouldn’t we still treat each other with respect? Like me.”

Jeok Cheongang answered calmly.

“I taught him better than your parents did, so don’t worry.”

The Blood-Sword Demon Lord stared blankly at Jeok Cheongang, then burst into laughter.

“Well, well. Just as the rumors said.”

“You’re worse than the rumors. I regret never catching and killing you when I had the chance.”

“I know your fiery temper well, Senior. Whenever you showed up on a battlefield, useful people died left and right. The Cult Leader was furious more than once.”

“Then you must have had a hard time, too. Weren’t you the Heavenly Demon’s most cherished guard dog, kept close at hand?”

“Sorry to disappoint you, but I didn’t have much trouble. I just killed as many as were dying.”

The Blood-Sword Demon Lord continued, his voice edged with laughter.

“When Heaven-Poison, that foolish old man, died, killing the Sect Leader of Hainan wasn’t enough. I had to bring back the Spear King’s head, too. But what could I do? I did it because I wanted to.”

“Heaven-Poison? You mean the Heaven-Poison Demon Lord?”

“Well, was there another Heaven-Poison?”

I knew the title Heaven-Poison Demon Lord, too.

The second-in-command of the Demonic Cult after the Heavenly Demon, he’d been an insurmountable wall even for Poison King Tang Sadok, the now-deceased Grand Family Head of the Sichuan Tang Clan.

One day, he’d encountered disciples of the Huashan Sect on a battlefield—and met his end that very day.

At the hands of someone who unleashed a brilliant purple Sword Force, bright enough to weigh down the sunset.

“The Sword Saint—though I suppose I should call him the Alliance Leader now? In any case, I was secretly grateful to Mae Jonghak. That old Heaven-Poison always looked at me strangely. Luckily, he died before it was too late, and things worked out well.”

I watched the Blood-Sword Demon Lord chatter away with a gleeful look. Then I frowned at the last thing he’d said.

*Things worked out well, thanks to him?*

The loss of a master meant a gap in one’s forces.

In that sense, the death of the Heaven-Poison Demon Lord must have been a tremendous blow to the Demonic Cult.

And yet he spoke as if…

“So that’s when you changed collars.”

At my blunt remark, the Blood-Sword Demon Lord furrowed his brow.

“‘Changed collars’ is a bit much… But think whatever you like.”

I already knew Dark Heaven had appeared before the Great Faction War was over.

The Head Elder of the Jin Family of Taiyuan, Baeksang of the Nanman Beast Palace, and even the Eastern Heaven Demon Lord, who’d been the Emperor’s closest confidant…

If you traced things back far enough, Dark Heaven had been taking shape from the very beginning of the Great Faction War.

No, perhaps…

*The Great Faction War itself might have begun because of Dark Heaven.*

A chill ran down my spine as I looked at the Blood-Sword Demon Lord and spoke.

“Just when did it begin?”

“When did what begin? I don’t know exactly what you mean.”

“When you all appeared. The Lord of Heaven.”

In that instant—

Whoosh!

The wind whipped up—a violent storm of energy.

The snow covering the ground, the frost, the dirt and sand buried beneath it all flew in every direction, then quickly settled.

Rustle.

As the debris of nature drifted back down, the Blood-Sword Demon Lord stared at me with a cold, sunken gaze.

“You have no manners. That’s for certain.”

The smile had vanished from his lips. His voice rang low.

It might have sounded calm at first, but cold lava flowed beneath it.

“How strange. I can understand you to a point, and yet I simply can’t understand you at all. Why would that person go out of their way to…”

The Blood-Sword Demon Lord let his words trail off, then smiled again with the good-natured expression of a man everyone liked.

“Well, there must be a reason for everything that person does. As always. I only wanted to confirm one thing.”

I didn’t need to ask what.

The Blood-Sword Demon Lord slowly raised a hand and continued.

“Blazing Flame Divine Dragon Jin Taekyung. You’re strong. Strong enough that I wouldn’t want to risk a bloody battle with you. Strong enough that I worry you might commit the blasphemy of defeating that person.”

I could see it. I could hear it.

The Blood-Sword Demon Lord’s eyes and voice, fixed on me.

And I could feel it, too.

The pure admiration in them.

And…

The faint killing intent hidden inside.

“I’m impressed by your limitless potential and your sense of justice. I mean that.”

“……!”

“……!”

“……!”

It all happened in an instant.

Me and Jeok Cheongang—and last, Sama Pyo, who’d been standing quietly in place.

The order and timing of our push off the ground and our charge differed, but the desperation driving us was probably the same.

Crack.

Our toes gouged the earth. Sand crumbled.

Internal energy surged from my dantian into the muscles of my tensed lower body, then exploded.

Boom!

The world slowed. The scenery shifted.

We shot forward, erasing a dozen yards of distance.

In that moment, Jeok Cheongang and I were two fierce streaks of flame, while Sama Pyo was a silent wind.

And in the slowed flow of time, three walls rose up to block the flame and the wind.

“Ha!”

Three voices, one shout.

The Three Elders of Tianshan.

The three fiends of Tianshan unleashed their pent-up fury and energy, wielding a power too great for anyone to dismiss them as mere stray dogs.

A coordinated technique, honed over ages of working together, merged the three walls into one enormous barrier.

Boom!

A single clash shook heaven and earth.

Amid that tremendous roar and the rippling waves of power that filled a time already split into fragments, the Blood-Sword Demon Lord’s hand, raised toward the sky, finally came down.

Like the countless blades on a hill, waiting for just one command.

“Slash!”

Shhk! Thud-thud-thud!

As a thousand or so heads rolled to the ground, my eyes met the Blood-Sword Demon Lord’s. I felt the blood in my entire body turn cold.

He was smiling.
```

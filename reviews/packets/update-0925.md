<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0925.txt",
      "sha256": "9e18845d4ae297b9557b9204b75a0ced60a36fc39b4454702e4bbe1a516eed31",
      "bytes": 14839
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "0c987d840a87eb59ac59288eb7497413c04ea7bb5cbf5985fd0d8a99443b1e00",
      "bytes": 1597
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "e4f261a256443b1a8267b983fdbd4ae7aa3530803a007681e483b189b757b921",
      "bytes": 231635
    },
    {
      "path": "characters/Baek Yeon.md",
      "sha256": "83b5f751321177641dc7b8cbf283a25c3789903dfd703a59be33a24d86de8997",
      "bytes": 837
    },
    {
      "path": "characters/Baeksang.md",
      "sha256": "8973bd8f6ca87513a945e019050a3b2da648bbfdc735664e497718b18aeac424",
      "bytes": 935
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "f87b3ee902b8d0a241d8d29875c8c01e7969902afbd06503f5a94a0b0015e184",
      "bytes": 759
    },
    {
      "path": "characters/Eastern Heaven Demon Lord.md",
      "sha256": "d50a1b9a778fe4fd63082af32e7ec0da367eec994d98ff6169628c2f763d0917",
      "bytes": 838
    },
    {
      "path": "characters/Hong Jin.md",
      "sha256": "c37beff89842b13390336be2aee6f5770512a67183ae7368bbd6aa56e7208302",
      "bytes": 837
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "4a466cdd496853cd1e31e5d5433208fbefb165c9f7f37386807de7255f356b12",
      "bytes": 1290
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "36b26af553560432e9a70154c49141186052c33e4150d5aa805ff7d8ad31d7dc",
      "bytes": 622
    },
    {
      "path": "characters/Prince Shangshan.md",
      "sha256": "9a9d12892716ac39decf93d0d0a579c93dba6623e01d4acb39254622199fa545",
      "bytes": 1096
    },
    {
      "path": "characters/Wei Zhong.md",
      "sha256": "3315d8844c5ee43f325edbc774399937b4c5838ba4d671df120d75d19cd50de6",
      "bytes": 705
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "8cb5c2ae972283f00b8b56c16eee487e9a5f65c3c8989723ccf0f81ff5e619df",
      "bytes": 265615
    }
  ],
  "estimated_tokens": 13407
}
-->

# Durable State Update — Chapter 925

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
1 and safe_through 925. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 925. Profile updates may replace only one
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
  "chapter": 925,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 925,
    "continuity_sources": [925],
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
    "The Eastern Heaven Demon Lord was Wei Zhong, the East Depot’s Seal-Holding Eunuch; Jin Taekyung killed him with blue-white flames after receiving an undisclosed Sound Transmission.",
    "Prince Shangshan Zhu Bao, now thirteen, dreams of creating an age of peace in which no one suffers the misfortunes he and the Demon Lord endured.",
    "Ma Sanbao remains missing.",
    "So Gyo identified Jin Taekyung as the Martial God’s chosen one and intends to explain the story behind it later; her allegiance remains unknown.",
    "The Salcheonmun vowed to pursue Mungyeong regardless of cost or delay and may pursue Jin Taekyung if it learns he killed Gye Yabu.",
    "Jeok Cheongang, Hyuk Mujin, Ju Hwaran, Song Ilseom, Sama Pyo, Taishan, and the Divine Physician survived and reunited with Jin Taekyung."
  ],
  "continuity_sources": [
    923,
    924
  ],
  "open_questions": [
    "What did Wei Zhong tell Jin Taekyung through Sound Transmission?",
    "Where is Ma Sanbao, and what is his current status?",
    "What does the Martial God’s reference to a chosen one mean for Jin Taekyung, and what story has So Gyo kept to herself?",
    "Will the Salcheonmun pursue Mungyeong or discover that Jin Taekyung killed Gye Yabu?",
    "What enabled Jin Taekyung to return from his seemingly fatal injuries?"
  ],
  "safe_through": 924,
  "temporary_decisions": [
    "Keep “Force” for 강기 distinct from “death energy” for 사기.",
    "Render 반정 as “restoration,” while preserving that it was disguised as a rebellion."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 궁성     | **Bow Saint**                 | —              |
| 태원진가   | **Jin Family of Taiyuan**        |
| 암천     | **Dark Heaven**                  |
| 남만야수궁  | **Nanman Beast Palace**          |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 장로     | **Elder**                                    |
| 대장로    | **Head Elder**                               |
| 제자     | **Disciple**                                 |
| 상태               | **Status**                     |
| 태원     | **Taiyuan**            |
| 사천     | **Sichuan**            |
| 노부      | **this old man / I**                                            |
| 백연 | **Baek Yeon** | Commander of the Embroidered Uniform Guard. |
| 백상 | **Baeksang** | Great chieftain of the Bai people and Yayul Cheok's sworn younger brother. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 동천마군 | **Eastern Heaven Demon Lord** | Title of the absurd masked antagonist in Jin's nightmare. |
| 홍진 | **Hong Jin** | Level 22 man at the City Lord's luncheon; delicate in appearance and voice. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 상산왕 | **Prince Shangshan** | The City Lord and a member of the imperial family who orders the luncheon. |
| 위충 | **Wei Zhong** | The pledge’s first signer and the personal name of Lord Cang Gong. |
| 성주 | **City Lord** | Official who sends the invitation for a gathering with young prodigies. |
| 태자 | **Crown Prince** | Title of the Emperor's older brother who was reportedly assassinated. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 주표 | **Zhu Bao** | Personal name of Prince Shangshan. |
| 황태자 | **Crown Prince** | The Emperor's older brother in Taekyung's recollection. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 기해 | **qi sea** | Name for the dantian, the place where internal energy begins and gathers. |
| 적통 | **orthodox lineage** | The legitimate succession of the Fire Gate Clan's tradition. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 사천성 | **Sichuan Province** | Province form used in the title of its chief official. |
| 사천성주 | **City Lord of Sichuan Province** | Title held by Won Gyun. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 촌각 | **moments** | Short intervals disappearing from Jeok's day. |
| 성하 | **Seongha** | Hunter named during the cave battle. |
| 고든 | **Gordon** | Pentagon employee tasked with repairing smashed warning lights. |
| 궁인 | **palace attendant** | Former Inner Palace attendant expelled by Baeksang. |
| 애향 | **Aehyang** | The City Lord’s favored concubine. |
| 금의위 | **Embroidered Uniform Guard** | Imperial guard force mentioned by Hong Jin. |
| 모산파 | **Maoshan Sect** | Jiangsu sect known for sorcery, destroyed by the founding emperor. |
| 태조 | **Taizu** | The Great Nation’s founding emperor. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 홍진 | 주표 | servant and political aide to prince | His Highness | formal-deferential | Uses the elongated royal call 전하 while summoning Zhu Bao. |
| 진태경 | 주표 | visitor to prince | His Highness, Prince Shangshan | formal-deferential | Addresses Zhu Bao as 상산왕 전하 after kneeling to meet his gaze. |
| 주표 | 진태경 | prince to visiting young hero | Jin Taekyung | formal and inquisitive | Uses the formal second-person address before asking Taekyung's name and requesting an autograph. |
| 홍진 | 진태경 | political_host_to_young_martial_artist | Young Hero Jin; Young Master Jin; Sleeping Dragon of Shanxi | polite, coaxing, and probing | Uses respectful forms while steering Taekyung toward relaying the Escort Bureau proposal and teasing him with the Seongun Escort Bureau. |
| 진태경 | 홍진 | young_martial_artist_to_political_official | Comrade Chairman—no, Deputy Military Commissioner | casual and teasing, then formally corrective | Deliberately jokes with an inappropriate title before correcting himself to Hong Jin's official office. |
| 사천성주 | 진태경 | official_to_imperial_messenger | Messenger of His Highness Prince Shangshan | formal-deferential | The City Lord addresses Taekyung deferentially after seeing Prince Shangshan's Token. |
| 진태경 | 사천성주 | visitor_to_city_lord | City Lord | sarcastic-polite | Taekyung jokingly praises him as our City Lord after making him fund the reward. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 백상 | 진태경 | Nanman great chieftain to Murim Alliance Pavilion Head | you bastard | cold, hostile, and contemptuous | Baeksang calls Jin a Han Chinese man, rejects his status, and orders him to leave. |
| 진태경 | 백상 | Murim Alliance Pavilion Head to Nanman great chieftain | you | polite but deliberately provocative | Jin tells Baeksang that Nanman's blood was shed for the world rather than merely for the Central Plains. |
| 백상 | 대장로 | Palace Lord to Miao Head Elder | Head Elder | cold, coercive, and formal | Baeksang offers the Head Elder a final chance to submit before ordering his imprisonment. |
| 대장로 | 백상 | Miao Head Elder to usurping Palace Lord | Baeksang / you bastard | furious and defiant | The Head Elder condemns Baeksang's betrayal and refuses to abandon Yayul Cheok. |
| 주표 | 홍진 | prince to loyal subject | you | formal and reassuring | Zhu Bao refers to Hong Jin as 그대 while apologizing for the hardship he has endured. |
| 주표 | 백연 | prince addressing an imperial military officer | Commander Baek Yeon | formal and authoritative | Addresses Baek Yeon by name and office while insisting that he answer. |
| 백연 | 주표 | imperial officer addressing a prince | Your Highness | formal and deferential | Uses 전하 when apologizing to and answering Prince Shangshan. |
| 홍진 | 백연 | imperial aide confronting a senior military officer | you | angry and confrontational | Uses 당신 in an indignant outburst. |
| 진태경 | 백연 | young martial artist confronting an imperial military commander | you | casual and insulting | Refers to Baek as 이 양반 while challenging his conduct. |
| 진태경 | 상산왕 | protector addressing a young prince | His Highness | respectful royal address | Taekyung refers to the prince as 상산왕 전하 when ordering Mujin to bring him. |
| 진태경 | 황제 | guest of the Emperor’s younger brother addressing the Emperor | Your Majesty | formal and deferential in address, despite blunt challenges | Taekyung repeatedly addresses the Emperor as 폐하. |
| 상산왕 | 황제 | younger brother addressing the Emperor | Your Majesty | deferential royal address | Shangshan addresses the Emperor as 폐하 while pleading for Taekyung. |
| 백연 | 진태경 | imperial commander confronting a young martial artist | Jin Taekyung | measured and familiar, using 자네 | Baek Yeon cautions Taekyung about his words and asks whether he must cause a scene. |
| 황제 | 진태경 | Emperor addressing a subject and Prince Shangshan’s guest | Jin Taekyung | formal and authoritative | The Emperor addresses Taekyung by his family and personal name before asking what to do with the two officials. |
| 황제 | 위충 | Emperor addressing the East Depot’s Seal-Holding Eunuch | Cang Gong | familiar and authoritative | The Emperor addresses Wei Zhong by his East Depot title while asking after his recovery. |
| 위충 | 황제 | East Depot’s Seal-Holding Eunuch addressing the Emperor | Your Majesty | formal and deferential, with pointed flattery | Wei Zhong uses 폐하 while indirectly challenging the Emperor. |
| 백연 | 위충 | imperial commander confronting the East Depot’s Seal-Holding Eunuch | Wei Zhong | stern and direct | Baek Yeon uses Wei Zhong’s name to order him to stop speaking. |
| 황제 | 동천마군 | former ruler addressing a former subject, now an enemy | you | measured and formal | The Emperor asks why the Demon Lord betrayed his father, the late Emperor. |
| 동천마군 | 황제 | former subject addressing the Emperor, now an enemy | you; you bastards | hostile and contemptuous | He denies ever being loyal to the imperial family and accuses the rulers of betrayal. |
| 진태경 | 동천마군 | young martial artist confronting an enemy | ugly-ass big bro | casual, profane, and taunting | Jin calls out to the Demon Lord after returning to the hall. |
| 동천마군 | 진태경 | enemy recognizing the spear wielder | Jin Taekyung | shouted, informal | The Demon Lord cries Taekyung's name after identifying him as the spear's owner. |
| 황제 | 백연 | Emperor to the imperial court’s foremost military commander and trusted comrade | Baek Yeon | Direct and familiar; framed as a request rather than an order | The Emperor asks Baek Yeon to sound the war drum. |
| 상산왕 | 동천마군 | young imperial prince addressing the enemy who killed his parents and brothers and suffered at the hands of his grandfather | you | formal-polite | He apologizes for his grandfather’s actions using 당신 and deferential speech. |

## Listed compact profiles

### Baek Yeon.md

# Baek Yeon (백연)

- **Safe through:** Chapter 923
- **Aliases:** Blood Envoy
- **Role:** Baek Yeon is the Commander of the Embroidered Uniform Guard, a former martial arts instructor to the Crown Prince, and the Blood Envoy who helped the fourth prince seize the throne and led the purge.
- **Personality:** Politically assured and controlled, he enforces authority with ruthless decisiveness but speaks with striking defiance to the Emperor in private when their shared undertaking is at stake.
- **Voice:** Not established
- **Relationships:** He commands the Embroidered Uniform Guard and serves the Emperor, carrying out the late Emperor’s final command to plan for the future alongside the fourth prince; he treats Taekyung as a dangerous potential obstacle.

### Baeksang.md

# Baeksang (백상)

- **Safe through:** Chapter 853
- **Aliases:** None
- **Role:** Baeksang was the Palace Lord of the Nanman Beast Palace and sole Great Chieftain of Nanman, and he died by the Beast Miao King's hand after confessing to serving Dark Heaven's plan.
- **Personality:** Cold, rigid, meticulous, and strategically resolute, yet burdened by regret, grief over Hwi's death, and a final conflicted impulse to spare others from the coming bloodshed.
- **Voice:** Rigid, formal, restrained, and emotionally distant.
- **Relationships:** Baeksang is Yayul Cheok's sworn younger brother and childhood companion, Yayul Mok's sworn uncle, and the father of Baekhwi, whom he believed the Great Snow Fiend killed but Dark Heaven has kept alive in a deep sleep; he cultivated Yohi with gold and influence and used her support to advance Dark Heaven's preparations.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 924
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Eastern Heaven Demon Lord.md

# Eastern Heaven Demon Lord (동천마군)

- **Safe through:** Chapter 924
- **Aliases:** Wei Zhong
- **Role:** The Eastern Heaven Demon Lord was Wei Zhong, the East Depot’s Seal-Holding Eunuch and a former Maoshan Sect disciple who commanded the dead with a bell; Jin Taekyung killed him with blue-white flames.
- **Personality:** His hatred grew from losing his family and sect, but recognizing his own lonely childhood in Zhu Bao ultimately moved him to relinquish his vengeance and choose a less harmful final act.
- **Voice:** He speaks in measured, almost lyrical phrasing, recounting the past before turning to pointed accusations.
- **Relationships:** Ma Sanbao is his Disciple; he holds the Emperor responsible for Taizu’s actions against the Maoshan Sect.

### Hong Jin.md

# Hong Jin (홍진)

- **Safe through:** Chapter 924
- **Aliases:** None
- **Role:** Hong Jin is a Level 22 Deputy Military Commissioner of Shanxi Province, a eunuch and trusted aide to Prince Shangshan, and a former member of the East Depot.
- **Personality:** Composed, socially deft, and ambitious, Hong Jin became a eunuch to escape poverty and save his family, then used his abilities to pursue a broader life.
- **Voice:** Delicate and deferential, using formal, self-effacing language with Prince Shangshan.
- **Relationships:** Hong Jin is devoted to Prince Shangshan, whom the late Emperor entrusted to his care; the Fourth Prince spared him because of their old ties, and his longtime friend and former East Depot cohort Ma Sanbao stayed behind in the palace.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 924
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader.
- **Personality:** Hungry, self-aware, dryly observant, and pragmatic under pressure; accepts extreme personal risk when duty and the lives of others demand it.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; So Gyo says he is the chosen one spoken of by the Martial God, while her allegiance remains unknown.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 924
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Prince Shangshan.md

# Prince Shangshan (상산왕)

- **Safe through:** Chapter 924
- **Aliases:** None
- **Role:** Prince Shangshan, whose personal name is Zhu Bao, is the Emperor’s thirteen-year-old youngest younger brother, an exceptionally skilled young swordsman, and the heir publicly designated by the Emperor.
- **Personality:** Earnest and compassionate, he takes responsibility for others’ suffering and dreams of a peaceful age founded on justice, care for the people, wise counsel, and accountability, even when doing so demands personal sacrifice.
- **Voice:** Archaic and formal in the manner of a historical drama, with openly eager and childlike reactions beneath his royal diction.
- **Relationships:** Prince Shangshan Zhu Bao is the Emperor’s youngest younger brother, and Hong Jin has been his steadfast caretaker since childhood. Zhu Bao admires Jin Taekyung, calls him a friend, and credits the support of those around him with giving him a different path from the Eastern Heaven Demon Lord, whom he met with compassion.

### Wei Zhong.md

# Wei Zhong (위충)

- **Safe through:** Chapter 924
- **Aliases:** None
- **Role:** Wei Zhong, addressed as Cang Gong, is the East Depot’s Seal-Holding Eunuch and has recovered enough from a prolonged illness to move about.
- **Personality:** Politically perceptive and self-possessed, he uses courteous remarks and veiled barbs to challenge the Emperor.
- **Voice:** He speaks in formal, deferential language, using repeated praise and respectful address to deliver pointed challenges.
- **Relationships:** He has a long-standing connection to the Emperor, with whom he exchanges polite but adversarial remarks about the succession.

## Korean source

```text
＃925화



불길이 솟아올랐다.

맹렬하고도 끔찍한 열기를 머금은, 동시에 한편으로는 이상하리만치 따스하게 느껴지는 불길이.

화아아악.

창날과 함께 육신을 파고든 청백색의 화염은 모든 것을 태우고, 녹였으며, 동시에 감싸 안았다.

한 인간의 불행한 일생을.

마지막에 이르러서야 자신의 잘못을 깨달은 괴물을.

‘잘 가라, 위충.’

전날 연판장에서 보았던 그의 이름을 읊조린 그때였다.

불완전한 축복이자 저주로 한 사람을 옭아매었던, 불사(不死)의 쇠사슬이 깨져나간 것은.

띠링. 띠링. 띠링.

마침내 영원한 안식이 찾아왔음을 알리는 맑은 종소리를 들으며, 나는 백염의 창날을 통해 끊임없이 쏟아붓던 열양지기를 거두어들였다.

온통 까맣게 그을린 그 자리에는, 불과 한 줌도 되지 않는 잿가루만이 남아 있었다.

솨아아아.

우연히 불어온 바람이었을까, 아니면 저 위에서 모든 것을 지켜본 누군가가 베푼 아량이었을까.

나는 바람에 실려 멀리, 저 멀리 퍼져 나가는 잿가루를 물끄러미 바라보았다.

다음 순간, 짧은 침묵을 깨트리며 울려 퍼진 한 사람의 목소리를 들으며.

“사사로이는 황실을 무너트리려 한 역적이었고, 외적(外敵)과 결탁하여 대국을 도탄에 빠트린 죄인이었다.”

나는 시선을 거두지 않으며 반문했다.

“그런 자가 맞기에는 너무 편안한 최후였다고 생각하십니까?”

“그렇다.”

“저 역시 그렇게 생각합니다.”

아무리 반성하고 뉘우쳤다 해도 한번 지은 죄는 사라지지 않는다. 위충이 아닌 동천마군으로서 행한 모든 잘못들은, 그가 지옥에서도 짊어져야 할 짐이다.

“하면, 어찌하여 그랬느냐.”

“그러는 폐하께서는 왜 저를 막지 않으셨습니까.”

목소리의 주인, 황제가 대답했다.

“막고 싶지 않았으니까.”

짧은 대답이지만, 모든 의미가 담긴 대답에 나는 실소를 흘렸다.

“그러셨군요.”

“이제 그대가 답할 차례다.”

“저는.”

잠시 말을 멈춘 나는 입술을 깨물었다.

“……그저, 문득 생각나는 사람들이 있었습니다.”

“그들 역시 위충과 같은 죄인들이겠군. 씻을 수 없는 잘못을 저지른.”

“예. 그리고 동시에 그처럼 잘못된 선택을 후회하는 사람들이었습니다.”

태원진가의 대장로가 그러했고, 남만야수궁의 백상 또한 그랬다.

암천(暗天)이라는 등불을 따라 잘못된 길을 택한 그들은 두 번 다시 발걸음을 되돌릴 수 없었다.

간혹 자신이 왔던 길을 되돌아보며 후회할 뿐, 돌아서기에는 너무 멀리 와 버린 상태였으니까.

그리고 나는 그런 이들을 향해 분노를 쏟아내면서도 한편으로는 안타까움을 느껴야 했다.

조금 더 올바른 선택을 할 수 있었을 텐데.

그랬다면 죄 없는 사람들이 희생당하는 일은 벌어지지 않을 텐데, 하는 생각과 함께.

‘하지만 언제나 늦고 말았지.’

자책도, 후회도 아니다.

이미 엎질러진 물은 어쩔 수 없다.

다만 그들이 선택한 결과는 비난할 수 있을지언정, 그 선택만큼은 감히 내가 비난할 수 없었다.

복수는 쉽고, 용서는 어렵다.

인간이란 본래 그런 동물이다.

“위령비(慰靈碑)를 세울 것이다.”

다시 내려앉은 침묵 속, 불현듯 입을 연 황제가 말을 이었다.

“하나는 오늘 이 자리에서 스러져 간 이들을 위해, 다른 하나는 군웅들의 아귀다툼 속에서 희생당한 백성들을 위해. 그리고 마지막 하나는.”

문득 말을 멈춘 황제의 시선이 저 멀리 바람이 달려간 서쪽을 향했다.

“모산파(茅山派). 그래, 모산파가 좋겠군.”

흡.

예상치 못한 황제의 선언에, 주위에 있던 문무백관이 헛숨을 삼켰다.

모산파에 위령비를 세운다는 것은, 곧 대국의 설립자인 태조(太祖)와 황실의 체면에 먹칠한다는 뜻과 같았으니까.

그러나 그들 중 누군가가 다급하게 입을 열기도 전에, 앞서의 것보다 더한 충격이 주위를 휩쓸었다.

아니, 후려쳤다.

“그리고 이 모든 것은, 짐이 아닌 황태자(皇太子)의 이름으로 행해질 것이다.”

“……!”

“……!”

주변의 공기가 파르르 떨렸다. 모두의 눈이 부릅떠졌다.

황태자.

언젠가 이 광활한 대륙을 물려받을 새로운 지배자.

나 역시 까맣게 잊고 있었다.

오늘 이 자리가 무엇을 위해 만들어진 것이었는지.

피로 얼룩진 이 잔혹한 연회의 끝에, 무엇이 기다리고 있을지.

그리고 지난 십여 년간 공석이었던 바로 그 황태자의 자리가, 지금 이 순간 주인을 맞이하려 하고 있었다.

“상산왕(上山王) 주표(朱標)는 황명을 받들라!”

지쳐 있던 황제의 모습은 이제 어디에서도 찾아볼 수 없다.

일국의 지존만이 지닐 수 있는 위엄으로 가득 찬 음성이 공기를 뚫었다. 바람을 타고 대연회장 전체를 감싸 안았다.

차차차창!

금의위 지휘사 백연을 시작으로 수천의 금의위가 검을 뽑아 하늘을 향해 겨누었다.

그들의 황금빛 갑옷이, 피에 젖은 검신이 번뜩인다.

강철로 이루어진 그 찬란한 물결은, 오직 한 소년을 위해 빛나고 있었다.

원수의 앞에서도 복수가 아닌 용서를 택한, 지난 천 년간 어떤 군주도 이루지 못했던 태평성대(太平聖代)를 꿈꾸는 어린 왕을 향해서.

“아. 아아.”

그리고 이 갑작스러운 상황 앞에서 어쩔 줄 몰라 하는 아우를 향해, 황제는 담담히 입을 열었다.

“감히 황명을 거역할 셈이더냐.”

“폐, 폐하.”

“가까이 오너라.”

“하지만, 하지만 폐하께는 이미…….”

그 순간 상산왕 주표가 하려는 말이 무엇인지, 그의 시선이 어디를 향하는지 알아채지 못한 사람은 없었다.

부른 배를 부여잡은 채 궁인(宮人)들에게 둘러싸여 있는 한 여인.

사천성주의 애첩에서 황제의 후궁이 된 그녀의 이름을, 나는 이미 알고 있다.

‘애향.’

이를 악문 채 이곳을 바라보는 애향의 눈빛에 숨길 수 없는 분노가 느껴진다.

그러나 그런 그녀를 향한 황제의 표정에는 일말의 감정조차 담겨 있지 않았다.

마치, 처음부터 필요에 의해 곁에 두었던 도구를 대하듯이.

‘잠깐, 설마?’

문득 어떤 생각이 머릿속을 스쳐 지나간 그때, 황제가 입을 열었다.

“언젠가 세상에 나올 저 아이는, 이미 죽은 사천성주의 피를 이었다.”

“……!”

“따라서 저 계집도, 태중의 아이도 짐과는 아무런 연관도 없으니 이에 관하여 그 누구도 의문을 제기해서는 안 될 것이다.”

이 파격적인 선언에 문무백관들은 예상치 못한 상황에 당혹스러운 기색이 역력했지만, 나를 비롯한 몇몇 사람들은 확신하고 있었다.

조금 전 황제가 내뱉은 말에는 일말의 거짓도 없다는 것을.

‘설마 했는데, 사실일 줄이야.’

황후와 후궁들이 있음에도 이미 십 년도 넘게 후사를 보지 못했던 황제.

그러나 지금에 이르러 다시 생각해 보면, 후사를 보지 못한 것이 아니라 보지 않았다는 것이 옳았다.

오직 하나뿐인 동생, 상산왕 주표를 위해서.

‘모든 위협으로부터 지켜야 했겠지. 황위를, 그리고 아우를.’

황실의 적통을 이은 유일한 직계.

동시에 암천에게는 황제를 몰아낼 수 있는 모든 명분을 지닌 훌륭한 허수아비.

표면적으로는 어린 동생을 차마 죽이지 못해 유배 보내는 것이나 다름없었지만, 상산왕 주표가 지금껏 살아남을 수 있었던 이유는 황제의 이러한 심계(心界)가 있었기 때문이다.

“아직도 모르겠느냐.”

아우를 위해 후사를 포기했고, 아우를 위해 비정한 형이 되어야 했던 그가 천천히 말을 이었다.

“처음부터 너를 위해 비워 둔 자리였다. 오직 너만이 오를 수 있는 자리였다.”

천하에서 가장 존귀한 황제의 자리에 올랐으나, 그의 목에는 역적이자 폐륜아라는 굴레가 씌워져 있었다.

밤낮을 가리지 않고 정사를 돌보았음에도, 그 굴레로 인해 폭군(暴君)이라 불렸다.

“네가 살아남기를, 짐의 유일한 약점이 되지 않길 바랐다.”

어쩌면 젖도 떼지 못한 어린아이가 황궁을 떠나던 그 날, 멀리서 그 뒷모습을 지켜보던 것은 동천마군만이 아니었을지도 모른다.

“지키기 위해 떠나보내야 했다. 과거에 완전히 뿌리 뽑지 못했던 역적들을 쳐내기 위해, 너를 다시 이 사지(死地)로 불러들여야 했다.”

십여 년의 세월은 결코 짧지 않았다.

동천마군이 흔들린 기반을 바로잡기에도. 황제가 모든 것을 끝낼 일전을 준비하기에도.

그리고 금의위로 하여금 은밀히 귀환시킨 하나뿐인 아우를, 그는 감금이라는 형태로 보호했다.

궁성(弓星)이라 불리는 무적의 고수를 한낱 호위로 삼으면서까지.

“표아(標兒)야.”

메마른 입술 사이로 흘러나온 황제의 음성은 놀라울 만큼 따뜻했다.

동지로, 신하로 가장 오랫동안 함께 했을 백연조차 눈을 크게 뜰 만큼.

오랫동안 혈육을 그리워했던 소년의 몸과 마음을 덜컥 굳게 만들어 버릴 만큼.

“이제, 때가 되었다.”

“……!”

그 나직한 한 마디에, 강물처럼 맑은 눈동자가 파르르 떨렸다.

그러나 그 눈빛에 담겨 있는 것은 망설임이 아닌 결심이었고, 꿈을 향해 나아가는 자만이 지닐 수 있는 의지였다.

“신, 상산왕 주표.”

스륵.

긴 옷자락이 피 웅덩이를 스쳤으나, 사방이 온통 붉게 물든 전장에서도 어린 왕이 지닌 빛은 조금도 바래지 않았다.

“지엄하신 황제 폐하의 명을 받드옵니다.”

황제의 주름진 입가에, 지금껏 그 누구도 보지 못했을 선명한 미소가 번졌다.

“허(許)하노라.”

와아아아아!

천지를 떨어 울리는 거대한 함성 속, 실로 머나먼 길을 헤맨 끝에 마주한 두 사람은 서로를 끌어안았다.

군신(君臣)이 아닌, 형제로서.



* * *



오늘 이 자리에서 새롭게 탄생한 대국의 황태자와 황제가, 두 형제가 서로를 끌어안는 순간 좌중은 치밀어오르는 격동을 삼키지 못하고 몸을 떨었다.

“아아……!”

지난 십여 년간 얼마나 바랐던가.

이 모든 것이 거짓이기를.

괴물처럼 뒤틀리고 그을려 버린 순리(順理)가 언젠가 제자리를 찾기를.

한데.

한데 그렇게 되었다.

차마 입 밖으로 내지 못한 채, 마음속에서만 간절히 바랐던 그 일이 현실이 되어 눈앞에 펼쳐져 있었다.

한 시대의 종막(終幕)이자 새로운 시대의 개막(開幕)을 지켜본 이들의 가슴 속에서, 무어라 형용할 수 없는 감정의 소용돌이가 휘몰아쳤다.

이내 거대한 함성이 되어 사방으로 넘쳐흘렀다.

“황제 폐하 만세!”

“황태자 전하, 천천세!”

“부디, 부디 신을 죽여 주소서!”

무수한 환호와 부르짖음.

진실을 알고 있던 누군가는 어린아이처럼 웃고 울었으며, 거짓에 속아 황제를 비난했던 누군가는 자책과 후회로 신형을 비틀거렸다.

그러나, 그 어디에도 속하지 않는 이들 또한 있었다.

“만세! 만세! 만만세!”

쉴 새 없이 황제의 장수를 기원하는 외침을 토해 내는 메마른 입술과 눈물로 흥건히 젖은 주름진 뺨.

하지만 이 모든 상황을 바라보는 노회한 회색빛 눈동자는 깊게 가라앉아 있었다.

‘일이 이렇게 틀어질 줄이야.’

절대 내뱉어서는 안 될 그 한 마디를, 노인은 조용히 마음속으로 삼켰다.

아직 자신에게 남아 있는 기회를 곱씹으며.

‘허나, 아직 모든 것이 끝난 것은 아니다.’

처음부터 모든 진실을 알고 오직 부귀영화를 위해 동천마군과 손잡은 노인이었으나, 이대로 역적이 되어 구족이 몰살당할 생각 따위는 조금도 없었다.

‘연판장(連判狀). 연판장과 노부의 정체를 아는 몇 사람만 없애면 된다.’

성즉군왕 패즉역적(成卽君王 敗卽逆賊)이라는 말은 틀렸다.

설령 실제로 역모를 꾸몄다 하더라도, 발각당하지 않는 한은 죄가 아니니까.

그리고 과거 황태자의 스승이자, 천하 모든 유생의 우러름을 받으며 대학사(大學士)의 지위까지 올랐던 노인은 이러한 부분에서 매우 치밀했다.

‘반드시 살아남을 것이다. 언제나 그래 왔듯이.’

마음속으로 그 다짐을 되새긴 노인은, 혼란한 인파 속에서 만세를 부르짖으며 조금씩 뒷걸음질 쳤다.

촌각이라도 빨리 황궁 밖에서 대기하고 있을 수하들과 만나야 했다.

자신의 정체를 아는 극소수의 핵심 인물을 제거하고 연판장을 손에 넣는다면 지금과 같은 지위를 유지할 수 있을 테고, 설령 상황이 어렵더라도 가산(家産)을 챙겨 도망칠 수 있을 터였다.

아니, 그렇게 믿었다.

먹먹한 함성 속, 기이할 만큼 또렷한 누군가의 목소리가 귓가를 파고들기 전까지는.

“어딜 그렇게 바쁘게 가세요. 이럴 때일수록 기쁨을 나눠야지.”

“……!”

늙은 몸뚱어리가 덜컥 굳었다.

서서히 고개를 돌린 노인의 시야에, 느긋한 발걸음으로 다가오는 청년의 얼굴이 들어왔다.

“진……태경.”

“에이, 진태경이 뭡니까. 삭막하게.”

청년, 진태경이 빙긋 웃으며 덧붙였다.

“진태경 동지, 라고 하셔야지.”

“그게, 그게 무슨…….”

“몰랐어요? 나도 연판장에 서명했는데?”

“……!”

“어, 이 사람이 아닌가?”

진태경이 고개를 갸웃거린 그때, 서늘한 목소리가 노인의 등 뒤에서 울려 퍼졌다.

“오랜만이네요, 대학사 어른.”

퍽!

목덜미로 전해지는 충격과 동시에 까맣게 물들어가는 시야 속에서, 노인은 한 사람의 이름을 떠올렸다.

‘홍진.’

끝장이었다. 모든 것이.
```

## Final English reading copy

```markdown
# Chapter 925

Flames surged upward.

They carried a fierce, terrible heat—and yet, somehow, they felt strangely warm.

*Fwoosh.*

The blue-white flames that had pierced his body along with the spearhead burned everything, melted everything, and, at the same time, embraced it all.

A man’s unhappy life.

A monster who had realized his mistake only at the very end.

*Goodbye, Wei Zhong.*

That was when I murmured the name I’d seen on the pledge the day before.

The chains of immortality that had bound one man as both an imperfect blessing and a curse shattered.

*Ding. Ding. Ding.*

As I listened to the clear chimes announcing the arrival of eternal rest, I drew back the Scorching Yang Qi I’d been pouring endlessly through White Flame’s spearhead.

All that remained in the thoroughly scorched spot was less than a handful of ash.

*Whoosh.*

Was it a wind that had blown by chance, or the mercy of someone above who had watched over everything?

I gazed blankly at the ashes carried far, far away on the wind.

The next moment, a man’s voice broke the brief silence.

“Privately, he was a traitor who tried to bring down the imperial family, and a criminal who colluded with foreign enemies and plunged the Great Nation into ruin.”

Without taking my eyes off the ashes, I asked, “Do you think that was too peaceful an end for a man like that?”

“I do.”

“I think so, too.”

No matter how much he’d reflected and repented, the crimes he’d committed would not disappear. Everything he had done as the Eastern Heaven Demon Lord, not Wei Zhong, was a burden he would have to carry even in Hell.

“Then why did you do it?”

“Why didn’t you stop me, Your Majesty?”

The Emperor, the owner of that voice, answered.

“Because I didn’t want to.”

It was a short answer, but it held every meaning. I let out a dry laugh.

“I see.”

“Now it’s your turn to answer.”

“I…”

I paused for a moment and bit my lip.

“…There were just some people who suddenly came to mind.”

“Those people were sinners like Wei Zhong, then. People who committed unforgivable wrongs.”

“Yes. And at the same time, they were people who regretted the wrong choices they’d made.”

The Head Elder of the Jin Family of Taiyuan had been like that. So had Baeksang of the Nanman Beast Palace.

Following the guiding light of Dark Heaven, they’d chosen the wrong path and could never turn back.

Sometimes they looked behind them and regretted the road they’d taken, but they’d already come too far to turn around.

And even as I poured my anger onto people like that, I couldn’t help feeling sorry for them, too.

*They could have made a better choice.*

*If they had, innocent people wouldn’t have had to die.*

*But it was always too late.*

It wasn’t self-reproach or regret.

What’s spilled is spilled. Nothing can be done about it.

I could condemn the consequences of their choices, but I couldn’t presume to condemn the choices themselves.

Revenge is easy. Forgiveness is hard.

That’s simply what people are like.

“I will erect memorials.”

In the silence that settled over us again, the Emperor suddenly continued.

“One for those who fell here today, another for the people sacrificed in the battles among the heroes of the realm. And the last one…”

The Emperor paused. His gaze turned toward the west, far away, where the wind had gone.

“The Maoshan Sect. Yes, the Maoshan Sect would be fitting.”

*Gasp.*

At the Emperor’s unexpected declaration, the officials gathered around us sucked in their breath.

Erecting a memorial at the Maoshan Sect was tantamount to tarnishing the dignity of Taizu, the founder of the Great Nation, and of the imperial family.

But before anyone could hurriedly open their mouth, an even greater shock swept through those gathered.

No—struck them.

“And all of this shall be done in the name of the Crown Prince, not Mine.”

“……!”

“……!”

The air around us trembled. Everyone’s eyes flew wide.

The Crown Prince.

The new ruler who would one day inherit this vast continent.

I’d completely forgotten, too.

What this gathering had been arranged for.

What awaited us at the end of this blood-soaked, brutal banquet.

And how the seat of Crown Prince, vacant for more than a decade, was about to find its rightful occupant at this very moment.

“Prince Shangshan Zhu Bao, receive the imperial command!”

The Emperor no longer looked exhausted.

His voice, filled with the majesty only the sovereign of a nation could possess, pierced the air. Riding the wind, it enveloped the entire grand banquet hall.

*Clang! Clang! Clang!*

Starting with Baek Yeon, Commander of the Embroidered Uniform Guard, thousands of guards drew their swords and pointed them toward the sky.

Their golden armor and blood-soaked blades flashed.

That splendid tide of steel shone for one boy alone.

For the young prince who had chosen forgiveness over revenge, even in front of his enemy—the boy who dreamed of an age of peace that no ruler in the past thousand years had ever achieved.

“Ah. Ah…”

The Emperor calmly addressed the younger brother who didn’t know what to do in the face of this sudden turn of events.

“Do you intend to defy the imperial command?”

“Y-Your Majesty.”

“Come closer.”

“But, but Your Majesty already…”

At that moment, no one failed to understand what Prince Shangshan Zhu Bao meant to say, or where his gaze had turned.

A woman stood surrounded by palace attendants, one hand clutching her swollen belly.

I already knew her name. She’d gone from being the favored concubine of the City Lord of Sichuan Province to a consort of the Emperor.

*Aehyang.*

Her eyes, fixed on us through clenched teeth, held an unmistakable anger.

But the Emperor’s expression as he looked at her held not a trace of emotion.

As though she were a tool he had kept at his side only because he needed her.

*Wait. Could it be?*

Just as the thought crossed my mind, the Emperor spoke.

“That child, who will one day be born into this world, carries the blood of the late City Lord of Sichuan Province.”

“……!”

“Therefore, neither that woman nor the child in her womb has anything to do with Me. No one is to raise questions about this.”

The court officials were visibly bewildered by the Emperor’s astonishing declaration. But a few of us, myself included, were certain.

There wasn’t a trace of a lie in what the Emperor had just said.

*I suspected it, but I can’t believe it was true.*

The Emperor hadn’t produced an heir in more than ten years, despite having an Empress and consorts.

But looking back now, it wasn’t that he couldn’t have an heir. He had chosen not to.

For the sake of his one and only younger brother, Prince Shangshan Zhu Bao.

*He must have wanted to protect him from every threat. The throne—and his younger brother.*

The only direct descendant of the orthodox imperial lineage.

And, at the same time, a perfect puppet for Dark Heaven—a figure who gave them every justification they needed to overthrow the Emperor.

On the surface, it had looked as though the Emperor couldn’t bring himself to kill his young brother, so he’d sent him away into exile. But the reason Prince Shangshan Zhu Bao had survived all this time was because of the Emperor’s far-reaching plan.

“Do you still not understand?”

The man who had given up the possibility of an heir for his younger brother, who had been forced to become a coldhearted older brother for his sake, continued slowly.

“I kept that seat empty for you from the very beginning. It was a seat only you could take.”

Though he had ascended the most exalted throne under Heaven, he had been branded a traitor and a monster who had betrayed his own family.

Though he tended to the affairs of state day and night, that brand had made people call him a tyrant.

“I wanted you to survive. I didn’t want you to become My one weakness.”

Perhaps when the infant, not yet weaned, left the imperial palace, the Eastern Heaven Demon Lord hadn’t been the only one watching his retreating figure from afar.

“I had to send you away to protect you. To root out the traitors I hadn’t been able to eradicate completely in the past, I had to bring you back into this deadly place.”

More than a decade was no short stretch of time.

It had been long enough for the Eastern Heaven Demon Lord to shore up his weakened foundations. Long enough for the Emperor to prepare for the decisive battle that would end everything.

And the Emperor had secretly brought his only younger brother back with the help of the Embroidered Uniform Guard, then protected him by keeping him confined.

He’d even made an invincible master known as the Bow Saint serve as a mere bodyguard.

“Bao’er.”

The Emperor’s voice, slipping between his dry lips, was surprisingly warm.

Warm enough to make even Baek Yeon, who had stood by him longest as a comrade and subject, widen his eyes.

Warm enough to make the body and heart of a boy who had longed for his family for so long suddenly go rigid.

“It’s time.”

“……!”

At that quiet sentence, the boy’s clear, river-bright eyes trembled.

But there was no hesitation in his gaze—only resolve, the kind of determination possessed by someone moving toward a dream.

“I, Prince Shangshan Zhu Bao…”

*Swish.*

The long hem of his robe brushed a pool of blood. Yet even on a battlefield stained red in every direction, the light within the young prince had not dimmed in the slightest.

“…humbly accept the command of His Majesty the Emperor.”

A vivid smile, unlike any anyone had ever seen, spread across the Emperor’s wrinkled lips.

“Granted.”

“Waaaaah!”

Amid the earth-shaking roar that resounded through Heaven and Earth, the two men, who had finally found each other after wandering such a long road, embraced.

Not as ruler and subject, but as brothers.

* * *

The Emperor and the newly named Crown Prince of the Great Nation, the two brothers, were embracing at the very place where a new Crown Prince had been born. Those gathered could no longer contain their swelling emotions and trembled.

“Ah…”

For more than a decade, how desperately they had hoped for this.

That all of it was a lie.

That the natural order, twisted and blackened like a monster, would one day return to its proper place.

And yet.

And yet, it had.

The thing they had desperately wished for in their hearts, unable to speak it aloud, had become reality before their eyes.

In the hearts of those who had witnessed the end of one era and the beginning of a new one, an indescribable whirlpool of emotion surged.

Before long, it overflowed in every direction as a tremendous roar.

“Long live His Majesty the Emperor!”

“May His Highness the Crown Prince live a thousand years!”

“Please, please kill me!”

Countless cheers and cries rang out.

Some who knew the truth laughed and wept like children. Others, who had been deceived by lies and had condemned the Emperor, staggered under the weight of their guilt and regret.

But there were also those who belonged to neither group.

“Long live! Long live! Long, long live!”

Dry lips ceaselessly called for the Emperor’s long life; wrinkled cheeks were drenched with tears.

But as his canny gray eyes took in everything unfolding before him, their gaze remained dark and still.

*I never thought things would go this wrong.*

The old man quietly swallowed those words, which he must never let escape his lips.

He turned over the last chance he still had.

*But it’s not over yet.*

The old man had known the whole truth from the beginning and joined hands with the Eastern Heaven Demon Lord solely for wealth and glory. But he had no intention of becoming a traitor and letting his entire clan be slaughtered.

*The pledge. If I can just make the pledge disappear and get rid of the few people who know who I really am…*

The saying “Succeed and you’re a king; fail and you’re a traitor” was wrong.

Even if you actually plotted treason, it wasn’t a crime as long as you weren’t caught.

And the old man, who had once tutored the former Crown Prince and risen to the rank of Grand Academician while earning the reverence of Confucian scholars throughout the realm, had been meticulous about such things.

*I will survive. Just as I always have.*

Repeating that resolve to himself, the old man cried out “Long live!” amid the confusion of the crowd, inching backward.

He had to meet his subordinates waiting outside the imperial palace as quickly as he could.

If he eliminated the handful of key figures who knew his identity and took possession of the pledge, he could keep his current position. And even if things became difficult, he could take his family’s wealth and flee.

No—he believed he could.

Until someone’s voice, strangely clear amid the deafening roar, pierced his ears.

“Where are you off to in such a hurry? At a time like this, you should be sharing in the joy.”

“……!”

The old man’s body went rigid.

He slowly turned his head. A young man was approaching at an unhurried pace.

“Jin… Taekyung.”

“Come on, don’t call me Jin Taekyung. That’s so cold.”

The young man, Jin Taekyung, smiled broadly and added, “You should call me Comrade Jin Taekyung.”

“What, what are you…”

“You didn’t know? I signed the pledge, too.”

“……!”

“Wait, have I got the wrong person?”

Just as Jin Taekyung tilted his head, a chilly voice rang out from behind the old man.

“It’s been a while, Grand Academician.”

*Thwack!*

With the blow to the back of his neck, the old man’s vision went black. As he sank into darkness, one name came to mind.

*Hong Jin.*

It was over.

Everything was over.
```

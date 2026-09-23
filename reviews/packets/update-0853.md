<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0853.txt",
      "sha256": "4a1158c74f206339b3d832f86ab271cd02e93b3f61eda2d4162e47d2885205a7",
      "bytes": 17588
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "f07dfd974c66ae235f510fd161140379945a38396f7be136e44f991a0344b922",
      "bytes": 1504
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "9ee608227056dcd7f9664204342a647fcdcef8c9c49fbfc8a379b8ef6f4de437",
      "bytes": 227906
    },
    {
      "path": "characters/Baeksang.md",
      "sha256": "329c61085128997b07e298ee2b19d840e931d06563a510227dfcdb0b30b96e7d",
      "bytes": 935
    },
    {
      "path": "characters/Hong Jin.md",
      "sha256": "2e02c1cd70118161f908e90045e4a953d51e4647160dcf440042eb19a46df43a",
      "bytes": 973
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "ef8f087208bfc02951bd6edf804536d51299357c5b6f1fdcfa328caa01f639fe",
      "bytes": 1573
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "9e77db14ed83558b11444f7ac6daa4f61737eb76759d44c2b65e3f7590cea662",
      "bytes": 1782
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "8a7d40dbd498e266624f7a89d33a177d9b259ecde19ff3deceacddcc7027b6fd",
      "bytes": 622
    },
    {
      "path": "characters/Mae Jonghak.md",
      "sha256": "40e6a929631309d935830f2441b3c184dc28250e344ee8332e10302798fa98b9",
      "bytes": 1061
    },
    {
      "path": "characters/Namho.md",
      "sha256": "e94d877f69985c85ebad669ca78f71e545e164a4abc61969905cdb65cf2d6e46",
      "bytes": 936
    },
    {
      "path": "characters/Prince Shangshan.md",
      "sha256": "8b9f70a8c53e82eb81d8fb6d41d995c29ff0b678c4214beba870735cb01e9eb2",
      "bytes": 914
    },
    {
      "path": "characters/Song Ho.md",
      "sha256": "4c117c7c6eb39f51d328b7f4f2abe543a7e360642f1223b3aca77aef2f34ee5b",
      "bytes": 767
    },
    {
      "path": "characters/Tang Sadok.md",
      "sha256": "78846265944789023ac22d16d64e364bf0da700e661ac81f715479da1b13b7a9",
      "bytes": 925
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "cc5d369594aaa700470c4324ebb5e5eca4369f4e6e06ade6420e9961524dc80a",
      "bytes": 253241
    }
  ],
  "estimated_tokens": 15763
}
-->

# Durable State Update — Chapter 853

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
1 and safe_through 853. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 853. Profile updates may replace only one
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
  "chapter": 853,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 853,
    "continuity_sources": [853],
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
    "The Divine Physician secured the Blood Soul Gu found in the deceased City Lord of Sichuan Province; it weakens hosts, causes episodes of madness, and eventually kills them.",
    "Jin suspects Dark Heaven’s covert killing of the City Lord is part of a scheme targeting the Great Nation, possibly its imperial family.",
    "Disguised Embroidered Uniform Guard agents appeared in Anhui; informants who followed them were killed. Jin fears they may be heading toward Shanxi and Prince Shangshan.",
    "More than ten messenger pigeons are approaching Jin and Jeok; their message and sender are unknown."
  ],
  "continuity_sources": [
    852
  ],
  "open_questions": [
    "Why did Dark Heaven secretly kill the City Lord of Sichuan Province?",
    "Is Dark Heaven targeting the Great Nation’s Emperor or imperial family, and what is its intended scheme?",
    "How is Prince Shangshan Zhu Bao connected to the suspected scheme, and are the Embroidered Uniform Guard agents heading toward him?",
    "Who sent the approaching messenger pigeons, and what do their messages say?",
    "What prompted the imperial decree against Hong Jin, and what will happen to him and Prince Shangshan?"
  ],
  "safe_through": 852,
  "temporary_decisions": [
    "Render 혈혼고 as “Blood Soul Gu.”",
    "Render 독혈지 as “Poisonblood Grounds.”",
    "Render 대국 as “Great Nation.”",
    "Render 금의위 as “Embroidered Uniform Guard.”"
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 매종학    | **Mae Jonghak**    |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 검성     | **Sword Saint**               | Mae Jonghak    |
| 하오문    | **Lower District Sect**          |
| 무림맹    | **Murim Alliance**               |
| 암천     | **Dark Heaven**                  |
| 사천당가   | **Sichuan Tang Clan**            |
| 남만야수궁  | **Nanman Beast Palace**          |
| 절정     | **Peak**          |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 중원     | **Central Plains**                               |                                                       |
| 가주     | **Family Head**                              |
| 표국     | **Escort Bureau**                            |
| 제자     | **Disciple**                                 |
| 전각     | **pavilion**                                 | Use “hall” only when established for a specific named building |
| 상태               | **Status**                     |
| 산서     | **Shanxi**             |
| 하남     | **Henan**              |
| 사천     | **Sichuan**            |
| 안휘     | **Anhui**              |
| 정마대전   | **Great Faction War**         |
| 백상 | **Baeksang** | Great chieftain of the Bai people and Yayul Cheok's sworn younger brother. |
| 홍진 | **Hong Jin** | Level 22 man at the City Lord's luncheon; delicate in appearance and voice. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 남호 | **Namho** | Hidden Shadow Pavilion code name; literally associated with amber from the south. |
| 상산왕 | **Prince Shangshan** | The City Lord and a member of the imperial family who orders the luncheon. |
| 송호 | **Song Ho** | Elderly martial artist known as the Thousand-Faced Fox. |
| 당사독 | **Tang Sadok** | Current Family Head of the Sichuan Tang Clan; also called the Myriad-Poison Asura. |
| 섬서 | **Shaanxi** | Province bordering Shanxi. |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 전서구 | **messenger pigeon** | Pigeon delivering the Lower District Sect's Jeongyang Branch report. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 성주 | **City Lord** | Official who sends the invitation for a gathering with young prodigies. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 천자 | **Son of Heaven** | Honorific title for the Emperor. |
| 개방 | **Beggars' Sect** | Murim organization counted among the Nine Sects and One Gang. |
| 도지휘동지 | **Deputy Military Commissioner** | Second-rank military office held by Eunuch Hong |
| 주표 | **Zhu Bao** | Personal name of Prince Shangshan. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 청성파 | **Qingcheng Sect** | Sect named in Baek Museong's comparison about disciplinary rules. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 비선 | **Hidden Thread** | Secret intelligence network and its chief hidden informant serving the Family Head. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 천면호리 | **Thousand-Faced Fox** | Epithet of Song Ho. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 은영각 | **Hidden Shadow Pavilion** | Former Murim Alliance intelligence organization. |
| 은영각주 | **Chief of the Hidden Shadow Pavilion** | Office formerly held by Song Ho. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 노야 | **Old Master** | Taekyung's private address for Jeok Cheongang. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 준이 | **Jun** | Family nickname used in the form Jun's dad. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 아미 | **Emei** | Short form for Emei Sect. |
| 청성 | **Qingcheng** | Short form for Qingcheng Sect. |
| 연검 | **flexible sword** | Ju Hwaran's weapon. |
| 호북 | **Hubei** | Province on Ju Gongsan's route from Guangdong to Henan. |
| 성도 | **Chengdu** | Sichuan destination of Taekyung's party. |
| 당가 | **Tang Family** | Short form for the Sichuan Tang Clan when distinguished from 사천당문. |
| 사천성 | **Sichuan Province** | Province form used in the title of its chief official. |
| 사천성주 | **City Lord of Sichuan Province** | Title held by Won Gyun. |
| 일원 | **One Origin** | Named Tang Clan organizational unit in Tang Sadok's mobilization order. |
| 오대 | **Five Squads** | Named Tang Clan organizational group in Tang Sadok's mobilization order. |
| 열화신룡 | **Blazing Flame Divine Dragon** | New sobriquet bestowed on Jin Taekyung. |
| 강소 | **Jiangsu** | Province at the eastern end of the Yangtze route. |
| 독의 | **Poison Physician** | Taekyung's mocking description of Mungyeong after learning how aggressively he uses poison. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 인자 | **ninja** | Japanese assassin skilled in concealment and concealed weapons. |
| 절강 | **Zhejiang** | Region from which the boat travels east. |
| 황하 | **Yellow River** | River along which civilization began. |
| 화룡각 | **Fire Dragon Pavilion** | New name chosen for Taekyung's pavilion. |
| 성하 | **Seongha** | Hunter named during the cave battle. |
| 철옹성 | **impregnable fortress** | Metaphor for Ares Guild's entrenched defenses. |
| 백족 | **Bai people** | Ethnic group encountered in Yeongin. |
| 강태공 | **Jiang Taigong** | Legendary fisherman used as a comparison for Taekyung's baiting skill. |
| 전서 | **missive** | A written message exchanged or delivered in secret. |
| 대족장 | **Great Chieftain** | Title used for the senior Nanman leader who supposedly ordered the inspection. |
| 화신 | **Fire God** | A local deity worshiped by one Nanman believer. |
| 혈혼고 | **Blood Soul Gu** | Rare gu poison found deep in Nanman. |
| 금의위 | **Embroidered Uniform Guard** | Imperial guard force mentioned by Hong Jin. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 홍진 | 주표 | servant and political aide to prince | His Highness | formal-deferential | Uses the elongated royal call 전하 while summoning Zhu Bao. |
| 진태경 | 주표 | visitor to prince | His Highness, Prince Shangshan | formal-deferential | Addresses Zhu Bao as 상산왕 전하 after kneeling to meet his gaze. |
| 주표 | 진태경 | prince to visiting young hero | Jin Taekyung | formal and inquisitive | Uses the formal second-person address before asking Taekyung's name and requesting an autograph. |
| 홍진 | 진태경 | political_host_to_young_martial_artist | Young Hero Jin; Young Master Jin; Sleeping Dragon of Shanxi | polite, coaxing, and probing | Uses respectful forms while steering Taekyung toward relaying the Escort Bureau proposal and teasing him with the Seongun Escort Bureau. |
| 진태경 | 홍진 | young_martial_artist_to_political_official | Comrade Chairman—no, Deputy Military Commissioner | casual and teasing, then formally corrective | Deliberately jokes with an inappropriate title before correcting himself to Hong Jin's official office. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 송호 | 진태경 | senior_martial_artist_to_junior_martial_artist | you | familiar-polite | Uses 자네 while recognizing Taekyung and discussing his preliminary performance. |
| 매종학 | 송호 | savior_to_survivor | you | casual-familiar | Mae uses 자네 while speaking to Song Ho after his identity is recognized. |
| 송호 | 매종학 | rescued_survivor_to_savior | Great Hero; you | formal-deferential and familiar | Song Ho credits Mae with saving his life and addresses him as 대협. |
| 매종학 | 진태경 | older_ally_to_younger_friend | friend | casual-familiar | Mae Jonghak uses 친구 when arriving at Taekyung's window and asking to talk. |
| 진태경 | 당사독 | visitor_to_Sichuan_Tang_Family_Head | Great Hero Tang Sadok | formal-deferential | Taekyung formally introduces himself and addresses Tang Sadok as 대협. |
| 당사독 | 진태경 | Family_Head_to_visiting_younger_martial_artist | you; fearless brat | blunt and threatening | Tang Sadok uses 너 and later calls Taekyung 겁 없는 놈 while rejecting his challenge. |
| 사천성주 | 진태경 | official_to_imperial_messenger | Messenger of His Highness Prince Shangshan | formal-deferential | The City Lord addresses Taekyung deferentially after seeing Prince Shangshan's Token. |
| 진태경 | 사천성주 | visitor_to_city_lord | City Lord | sarcastic-polite | Taekyung jokingly praises him as our City Lord after making him fund the reward. |
| 호위 | 당사독 | guard_to_Family_Head | Family Head | formal-deferential | Uses 가주님 while reporting Jin Taekyung's request. |
| 가솔 | 진태경 | Zhuge Clan retainer to Great Hero | Great Hero Jin | polite and pleading | Uses 진 대협 while urging Taekyung to stop provoking Ju Wongong. |
| 매종학 | 적천강 | long-standing martial rival and friend | Great Hero Jeok | casual and familiar | Mae addresses Jeok as 적 대협 while discussing the Alliance Leader position. |
| 적천강 | 매종학 | long-standing martial rival and friend | you | blunt and familiar | Jeok addresses Mae as 당신 while recalling their meeting at Mount Jiuhua. |
| 천면호리 | 매종학 | intelligence_chief_to_alliance_leader | Alliance Leader | formal and deferential | Requests that Mae move elsewhere with the others before he reports further. |
| 진태경 | 매종학 | younger ally to newly installed Alliance Leader | Alliance Leader | formal and deferential | Uses 맹주님 while formally greeting Mae Jonghak as the Alliance Leader. |
| 송호 | 적천강 | Hidden Shadow Pavilion Chief to legendary senior master | Great Hero Jeok | formal-deferential | Song Ho addresses Jeok while questioning the basis for his confidence in Taekyung. |
| 적천강 | 송호 | senior martial master to allied intelligence chief | you | blunt but reassuring | Jeok directly tells Song Ho to believe Taekyung. |
| 매종학 | 천면호리 | Alliance Leader to Hidden Shadow Pavilion Chief | Chief of the Hidden Shadow Pavilion | casual-but-commanding | Asks Song Ho's view of Taekyung's suspected target. |
| 남호 | 진태경 | Hidden_Shadow_Pavilion_agent_to_mission_leader | Jin Taekyung / you | guarded and familiar | Namho addresses Taekyung as 자네 while explaining the contact and offering guidance. |
| 진태경 | 남호 | mission_leader_to_hidden_shadow_agent | you / Namho | probing and respectful | Taekyung questions Namho’s affiliation and later discusses Dark Heaven’s threat to Nanman. |
| 백상 | 진태경 | Nanman great chieftain to Murim Alliance Pavilion Head | you bastard | cold, hostile, and contemptuous | Baeksang calls Jin a Han Chinese man, rejects his status, and orders him to leave. |
| 진태경 | 백상 | Murim Alliance Pavilion Head to Nanman great chieftain | you | polite but deliberately provocative | Jin tells Baeksang that Nanman's blood was shed for the world rather than merely for the Central Plains. |
| 남호 | 각주 | guide to pavilion master | Pavilion Master | blunt, hostile, and abusive | Namho addresses Jin as 각주 while accusing him of causing the disturbance. |

## Listed compact profiles

### Baeksang.md

# Baeksang (백상)

- **Safe through:** Chapter 723
- **Aliases:** None
- **Role:** Baeksang was the Palace Lord of the Nanman Beast Palace and sole Great Chieftain of Nanman, and he died by the Beast Miao King's hand after confessing to serving Dark Heaven's plan.
- **Personality:** Cold, rigid, meticulous, and strategically resolute, yet burdened by regret, grief over Hwi's death, and a final conflicted impulse to spare others from the coming bloodshed.
- **Voice:** Rigid, formal, restrained, and emotionally distant.
- **Relationships:** Baeksang is Yayul Cheok's sworn younger brother and childhood companion, Yayul Mok's sworn uncle, and the father of Baekhwi, whom he believed the Great Snow Fiend killed but Dark Heaven has kept alive in a deep sleep; he cultivated Yohi with gold and influence and used her support to advance Dark Heaven's preparations.

### Hong Jin.md

# Hong Jin (홍진)

- **Safe through:** Chapter 851
- **Aliases:** None
- **Role:** Level 22 Deputy Military Commissioner of Shanxi Province and a eunuch who has served beside Prince Shangshan since infancy; he formerly served the late Emperor, who ordered him to assist Prince Shangshan, and came to the frontier in something like exile; he remains the power behind the Shanxi Provincial Office, manages the City Lord's luncheon, and redirects a planned Shaanxi–Shanxi trade project toward Huashan.
- **Personality:** Composed and socially deft, Hong Jin is considerate toward those beneath him and dislikes excessive deference, which recalls his impoverished past.
- **Voice:** Delicate, complimentary, and conversational.
- **Relationships:** Hong Jin has served Prince Shangshan since infancy and is devoted to protecting him; he trusts Jin Taekyung as the person best able to keep the prince safe.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 852
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm, the occupant of the chief seat of the Murim Alliance's Five Kings Hall, and a trusted confidant who accepts Jin as himself despite knowing that he travels between Murim and another world resembling the realm of immortals.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; they trust each other deeply but have never formalized their bond. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to the late Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and is a long-standing rival of Peng Cheolhu.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 852
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader.
- **Personality:** Hungry, self-aware, dryly observant, and pragmatic under pressure; accepts extreme personal risk when duty and the lives of others demand it.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; they trust each other deeply, though their bond remains unformalized. Cheongpung is his trusted companion and only true martial rival; Choi Minwoo is his subordinate and trusted manager of media and official arrangements as well as the Peace Guild's Guild Master; Ju Hwaran is a trusted Fire Dragon Pavilion member; Magic Johnson and Chuck Hagel are allied to him; his mother and sister Hayeon are among those he protects; the Skeleton King is his friend and ally; Xiao Shen regards him as an older brother; Jin-ho is his older friend and trusted confidant; he once saved Ju Wongong’s life.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 852
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Mae Jonghak.md

# Mae Jonghak (매종학)

- **Safe through:** Chapter 844
- **Aliases:** Sword Saint
- **Role:** Sword Saint and Cheongpung's grandfather who now serves as the New Murim Alliance's Alliance Leader and has ordered Jin Taekyung's first Fire Dragon Pavilion mission to Nanman.
- **Personality:** Playful, easygoing, and teasing, but capable of handling heavy administrative responsibilities efficiently.
- **Voice:** Friendly, casually familiar, and cheerfully teasing, including when greeting old acquaintances and discussing leadership.
- **Relationships:** Cheongpung's grandfather and martial instructor; taught him the Taeeul Miri Palm; secretly entered Huashan while its Sect Leader slept, left a dagger and handwritten note, and then went into hiding, prompting Huashan's search; fought Jeok Cheongang at Mount Jiuhua more than forty years ago and left after their draw; his old friend Hong Dao left him a letter identifying Jin Taekyung as the Morning Star who would drive away darkness.

### Namho.md

# Namho (남호)

- **Safe through:** Chapter 852
- **Aliases:** Elder Chao
- **Role:** Namho is an eighty-year-old non-Han Hidden Shadow Pavilion agent who spent more than fifty years operating under the cover of the Poison Flower Pavilion in Nanman and now serves as the Fire Dragon Pavilion’s guide.
- **Personality:** Duty-bound, pragmatic, and observant; uses theatrical violence to protect intelligence work and takes a veteran’s concern for the younger generation’s resolve.
- **Voice:** Measured and reflective when advising the younger generation, loudly abusive when maintaining his local cover, and capable of theatrical boasts and dry humor.
- **Relationships:** Namho is a Hidden Shadow Pavilion contact for Jin Taekyung and the Fire Dragon Pavilion, receives intelligence from the Pavilion Master, and knows the code used by the Thousand-Faced Fox.

### Prince Shangshan.md

# Prince Shangshan (상산왕)

- **Safe through:** Chapter 852
- **Aliases:** None
- **Role:** The City Lord and a member of the imperial family; ten-year-old Prince Shangshan, whose personal name is Zhu Bao, is an exceptionally skilled young swordsman who has trained daily for three years.
- **Personality:** Earnest, admiring, and eager to emulate Jin Taekyung; despite his royal dignity, he shows openly childlike enthusiasm for martial arts and Taekyung's reputation.
- **Voice:** Archaic and formal in the manner of a historical drama, with openly eager and childlike reactions beneath his royal diction.
- **Relationships:** Prince Shangshan Zhu Bao is the Emperor's only younger full brother, and his token commands immediate deference from distant imperial relatives such as Ju Wongong; he admires Jin Taekyung and seeks to emulate him.

### Song Ho.md

# Song Ho (송호)

- **Safe through:** Chapter 618
- **Aliases:** Thousand-Faced Fox
- **Role:** Elderly Peak master known as the Thousand-Faced Fox, a martial artist with a prosthetic leg, and current Chief of the Hidden Shadow Pavilion, overseeing a vetted intelligence network that includes highly trained assassins.
- **Personality:** Outwardly genial and relaxed, but observant, forceful, and intimidating when pursuing information.
- **Voice:** Lightly genial and conversational, turning quietly coercive during interrogation.
- **Relationships:** He serves under Mae Jonghak's New Murim Alliance, commands the Hidden Shadow Pavilion, and recognizes Jin Taekyung as Jeok Cheongang's Disciple.

### Tang Sadok.md

# Tang Sadok (당사독)

- **Safe through:** Chapter 852
- **Aliases:** Myriad-Poison Asura
- **Role:** Current Family Head of the Sichuan Tang Clan, overseeing its recovery and relying on allied martial artists to help treat patients and guard against another Dark Heaven attack.
- **Personality:** Blunt and unsentimental, yet grateful to those who remain with the Tang Clan; he has consciously chosen to change and speaks candidly about the clan’s vulnerability.
- **Voice:** Hissing, curt, authoritative, and threatening.
- **Relationships:** Tang Taesang was his father and predecessor, his unnamed nephew serves as Master of the Gatekeeper Pavilion, Mimi is his cherished old friend and companion temporarily entrusted to Cheongpung, and he regards Jin Taekyung and Cheongpung as benefactors, openly welcoming Jin with a warmth he usually conceals.

## Korean source

```text
＃853화



정보란 하나의 조각으로는 절대 완성할 수 없는 퍼즐과 같다.

여러 조각을 모아 짜 맞추지 않는 한, 그것은 정보가 아니라 아무런 가치도 없는 단순한 의문점으로 남을 뿐이다.

지금으로부터 약 보름 전 안휘성에서 모습을 드러낸 금의위(錦衣衛)의 존재 역시 마찬가지였다.

금의위는 그저 작은 조각에 지나지 않았다.

적어도 사천성주가 급사하고, 혈혼고가 발견되기 전까지는.

‘이제는 상황이 달라졌지.’

구파일방의 일원인 아미와 청성, 사천당가와 개방은 말할 것도 없고 상당수가 양민으로 이루어진 하오문 역시 엄연한 무림 문파.

이미 암천과의 전면전이 시작된 이상, 자연스럽게 관(官)에 대한 정보는 후 순위로 밀려날 수밖에 없었다.

당장 자신이 사는 동네에 불이 났는데 옆 동네를 들여다보는 정신 나간 놈은 없으니까.

하지만 그 옆 동네에 불이 옮겨 붙었다면 이야기가 달라진다.

모종의 이유로 보고되지 않았던, 혹은 단순한 의구심 정도로 남았던 정보의 퍼즐 조각들을 모조리 끄집어내야 한다.

그리고 조금 전 사천당가에 도착한 십여 마리의 전서구(傳書鳩)에는 바로 그 조각들이 실려 있었다.

“오셨습니까, 노야(老爺). 자네도.”

중요한 일일수록 가장 먼저 가주에게 보고되는 건 당연지사.

적천강과 나를 향해 간단한 인사를 건넨 당사독의 앞에는 단단히 봉해진 전서(傳書)가 어지럽게 흩어져 있었다.

“저게 모두…… 그것에 관련된 소식입니까?”

“아마도.”

짤막하게 대답한 당사독이 눈짓하자, 그의 옆에서 전서구와 전서의 상태를 꼼꼼히 살피고 있던 노인이 입을 열었다.

“소인이 살핀 바에 의하면 전서구가 공격당한 흔적이나 전서의 훼손은 일절 보이지 않습니다.”

“확실한가? 중요한 일일세.”

“제 목을 걸지요.”

“그거면 충분하네. 때가 되면 다시 기별할 테니 그동안 아무도 들이지 말게.”

“예. 가주님. 쥐새끼 한 마리도 접근하지 못하게 하겠습니다.”

공손한 인사와 함께 방을 빠져나간 노인의 기척이 금세 멀어진다.

적천강의 눈빛에 담긴 뜻을 알아차린 당사독이 먼저 입을 열었다.

“제 말이라면 절대적으로 충성하는 가솔입니다. 반평생이 넘는 세월 동안 이곳에서 전서구를 다루던 자라, 만일을 대비하여 검증을 맡겼습니다.”

당사독이 언급한 ‘이곳’이란, 전각이라기보다는 커다란 새장을 닮아 있었다.

그저 가만히 서 있는 것만으로도 날짐승 특유의 노린내가 코를 찔렀고, 주위에는 크고 작은 새들이 가두어진 철창으로 가득했으며 온갖 색의 깃털이 휘날렸다.

긴 세월 동안 오직 전서구를 훈련 시키거나 주고받는 용도로 쓰였음이 분명한 이곳에, 아직 뜯지 않은 수십 장의 전서가 쌓여 있었다.

“생각보다 양이 많네요. 오기 전에 봤던 전서구의 숫자보다도 훨씬.”

내 말을 들은 당사독이 작게 고개를 끄덕였다.

“나로서도 좀 의외였네. 보통은 전서구가 눈에 띄지 않기 위해서라도 최소한의 정보만을 담아 전달하니까. 하지만 이렇게 한 마리 당 몇 장씩이나 되는 전서를 실어 보냈다는 건…….”

“이렇게 해서라도 전해야 할 정보의 양이 많다는 거겠지.”

문득 입을 연 적천강이 나직하게 덧붙였다.

“그만큼 긴급하다는 뜻이기도 하고.”

첫 번째 전서를 뜯어 내용을 확인한 나는 깨달았다. 앞서 들었던 말이 조금의 과장도 없는 사실이라는 것을.

“뭐라 적혀 있느냐?”

적천강의 물음에 잠시 침묵하던 내가 대답했다.

“안휘에 이어, 호북(湖北)에서 금의위로 추정되는 자들이 모습을 드러냈다는 정보입니다.”

“호북? 정보가 들어온 시점은?”

“지금으로부터 약 보름하고도 닷새 전이요.”

“보름하고도 닷새라. 빌어먹게도 늦었군.”

“당시에는 앞서 안휘성에서 추적이 끊긴 뒤였고, 호북의 개방과 하오문 측에서도 그들의 정체가 금의위라고는 짐작하지 못했던 것 같습니다.”

당사독이 미간을 찌푸리며 입을 열었다.

“애초에 금의위가 아니었을 가능성도 있지 않겠나? 자네가 했던 예상대로라면 현재 그들의 표적은 상산왕일 터인데, 산서로 가고자 했다면 굳이 호북으로 우회할 것 없이 안휘에서 곧장 하남으로 이동하면 그만이야.”

사실이다. 안휘성은 하남과 가장 인접해 있고, 조금만 더 북상(北上)하면 곧장 산서로 진입할 수 있으니까.

그러나 지금 당사독은 한 가지 중요한 사실을 잠시 잊은 것이 틀림없다.

“그들이 금의위라는 가정 하에, 처음부터 변복까지 해 가며 정체를 숨겼다면 당연히 하남을 피하는 것이 맞습니다.”

“그게 무슨…… 아.”

문득 탄성을 흘린 당사독이 한 단어를 토해 냈다.

“무림맹.”

“예, 맞습니다. 하다못해 안휘에서도 꼬리를 밟힐 뻔했는데, 지금의 하남은 철옹성이나 다름없어요.”

거대한 전운(戰運)이 극을 향해 치닫고, 암천과의 전면전이 시작된 상황.

그런데 중원 무림의 모두가 촉각을 곤두세우고 있는 지금, 무림맹 총단(總團)이 위치한 하남을 가로질러 산서로 향한다는 것은 스스로 정체를 까발리겠다는 뜻이나 다름없다.

무림맹은 호구가 아니다.

암천의 끄나풀이건 금의위건, 조금이라도 수상한 이들이 나타난다면 금세 정체가 발각되고 만다.

무림 맹주인 검성 매종학이 허허 웃으며 뒷짐 지고 구경만 한다 해도, 그의 곁에 있는 어느 늙은 여우는 다르다.

‘천면호리(千面狐狸) 송호.’

그가 가진 또 다른 이름은, 무림맹 은영각주(隱影閣主).

언제나 묘한 미소를 띠고 있던 천면호리의 얼굴을 떠올린 바로 그 순간이었다.

바스락.

굳게 닫힌 문틈으로 들려오는 희미한 소음. 하지만 나를 포함한 이 방 안의 누구도 놀라거나 당황하지 않았다.

서서히 가까워지는 인기척의 존재도, 그 정체도 이미 어느 정도 짐작하고 있었기 때문이었다.

끼이이익.

적천강의 눈짓에 내가 손을 뻗었다. 부드러운 기풍(氣風)이 닫혀 있던 문을 열어젖힘과 동시에 한 사람의 모습이 보였다.

아니, 정확히 말하자면 한 사람처럼 보이는 두 사람이다.

앞서 나갔던 당가의 가솔이 남호를 뒤에서 끌어안은 채 목젖에 칼을 들이대고 있었으니까.

“……?”

“……?”

“……?”

저게 도대체 무슨 상황이지.

잠깐 뇌 정지가 오긴 했지만, 답은 금방 나왔다.

당사독의 말이라면 껌뻑 죽는다던 당가의 가솔이, 정말 쥐새끼 한 마리 접근하지 못하게 주위를 지키다가 남호를 발견한 것이다.

이 과정에서 생겨난 사소한 문제는, 남호가 껌뻑 죽을 뻔했다는 거지.

“아직 청춘이시네요. 그 나이에 불타기 쉽지 않은데.”

부비부비 자세로 결박당한 남호가 똥 씹은 얼굴로 대답했다.

“그게 무슨 뜻인가?”

“별거 아닙니다. 그나저나 가만히 있으세요. 괜히 말하면서 목젖 움직이니까 칼날에 베이잖아요.”

“사람 겁주는 것도 정도껏…….”

서걱.

“이런 씨팔, 진짜네.”

“말씀하시지 말라니까.”

“그래서 지금은 복화술 쓰고 있잖나.”

“오, 복화술. 저도 좀 가르쳐 주세요.”

“나중에 기회 되면…… 제기랄. 개소리는 집어치우고 이 작자나 좀 말려보게. 설명을 해도 도무지 들어 처먹질 않아.”

곤경에 처한 남호의 상황을 본 적천강이 흥미로운 듯이 턱을 쓰다듬었다.

“확실히 네 녀석 말대로 충성스럽긴 하구나. 조금만 더 믿음직스러웠으면 애꿎은 사람 하나 죽었겠어.”

“……가끔은 충성이 과하기도 합니다. 이만 풀어주게. 우리 사람이야.”

당사독의 한숨 섞인 목소리에, 눈을 껌뻑거린 당가의 가솔이 그제야 비수를 거두며 물러났다.

사과 한마디 없이 사라지는 그의 모습을 지켜보던 남호가 작게 중얼거렸다.

“별 미친놈 다 보겠군. 이러니까 사천당가가 무림에서…….”

“무림에서?”

당사독의 의미심장한 시선을 마주한 남호가 빛의 속도로 차선을 변경했다.

“천하 오대 세가라 불리는 것 아니겠소.”

존경스러울 정도의 드리프트다. 하긴, 아무리 살 만큼 살았어도 남은 인생을 독살의 불안감 속에서 보낼 수는 없는 법이니까.

“그나저나 왜 이제야 오셨어요? 사람 보낸 지가 언젠데.”

“잠깐 기억을 더듬느라 늦었네. 나도 나이가 들어서 그런지 기억력이 예전 같지 않더라고.”

“기억이요?”

“그래, 기억.”

그것이 정확히 무슨 뜻인지 묻기도 전에, 남호가 내 손에 들린 전서를 향해 턱짓했다.

“지금 보고 있는 그 정보, 출처가 어딘가?”

“각각 개방과 하오문의 호북지부입니다.”

“아니군. 그 옆에 건?”

나는 탁자 위에 널브러진 수십여 장의 전서 중 하나를 추가로 뜯어 확인했다.

“호연상단이라고 되어 있는데. 처음 들어 보는 이름입니다. 안에 적힌 내용은…….”

“청성파 산하의 상단일세. 정확히는 청성파의 속가제자인 호연검(湖沿劍)이 이십 년 전부터 상단주를 맡고 있지. 절정 고수지만 무위보다는 상단 굴리는 솜씨가 훨씬 좋아. 호연상단만 해도 산동 땅에서는 다섯 손가락 안에 드는 규모지.”

“예?”

“아, 그리고 내용은 굳이 말해 줄 필요 없네. 내가 찾는 이름은 따로 있으니까. 자네는 출처가 어딘지만 확인해서 알려 주면 돼.”

“…….”

뭐부터 물어봐야 할지 모르겠다.

분명 정마대전 이후 중원에는 발 한 번 내디딘 적 없는 것으로 아는데, 불과 이십여 년 전 소식까지 어찌 그리 빠삭한지.

아니면 내용 따위는 개나 주고 찾아야 하는 출처가 뭔지.

적천강과 당사독은 눈을 동그랗게 떴고, 어안이 벙벙해진 내가 말없이 쳐다만 보자 남호는 못마땅한 표정으로 혀를 찼다.

“내가 강태공도 아닌데 남만에서 세월만 낚고 있었겠나. 그곳에서도 은영각의 비선(秘線)을 통해 중원 소식을 틈틈이 접했으니 그리 놀랄 것도 없어.”

“아니, 이 정도면 틈틈이 수준이 아닌 것 같은데요? 저라면 들어도 기억 못 할 정보 같은데.”

“늙은이의 소일거리라고 해 두지. 더 할 말 남았나?”

소일거리라기보다는 사실 직업병에 가깝겠지만, 지금 중요한 건 그런 개인적인 궁금증 따위가 아니다.

잠자코 입을 다문 나는 남은 전서들을 빠르게 뜯어 읽기 시작했다.

지금 쌓여 있는 전서는 모두 사천지부에서 통해 전해진 것이지만, 그 출처는 각각 달랐고 남호가 원하는 것을 확인하기 위해서는 내용도 봐야 하니 자연스럽게 정보를 머릿속에서 정리할 수 있었다.

그리고 그 결과는 충격적이었다.

‘안휘와 호북이 전부가 아니었어.’

안휘, 호북, 호남, 강소, 산동.

각 전서에 적힌 내용이 모두 사실이라면, 금의위로 추정되는 이들은 위의 다섯 개 성에서 모습을 드러냈고 이내 자취를 감추었다.

‘이건…….’

분산 이동이다.

교란 목적보다는 눈에 띄지 않기 위한 기동적인 움직임.

그들은 적게는 열 명, 많게는 서른 명으로 나뉘어 각 성으로 흩어졌고 이내 섬서나 산동에 이르러 종적이 묘연해졌다.

‘산서. 산서에서 집결한 거야.’

틀림없다. 최대한 주의를 끌지 않으며 하남을 우회, 대륙의 지형상 옆구리라 할 수 있는 섬서와 산동을 통해 산서성으로 흘러 들어간 것이다.

그리고 그곳에는…….

‘상산왕 주표가 있다.’

덜컥 내려앉은 가슴. 다음 순간 기계적으로 뽑아 든 전서의 내용을 확인하자 나도 모르게 이가 악물렸다.

으득.

“왜 그러나?”

“무슨 내용이길래…….”

나는 대답 대신 손에 든 전서를 펼쳐 내밀었다. 누런 짐승의 가죽 위에는 깨알 같은 글씨로 이렇게 적혀 있었다.



一. 발신. 하오문 산서지부.

二. 상산왕 주표. 금의위 동행.

三. 산서성 종2품 도지휘동지 홍진. 하오문 지원 의뢰 및 상산왕과 합류.

四. 추적 개시. 관(官)의 개입이 우려됨.

五. 추적조 전멸로 인한 작전 중단.

六. 해당 문건은 천(天) 급이며, 의뢰인이 지정한 대상에게 최대한 신속히 정보를 전달해야 함.

七. 열화신룡 진태경. 긴급 수배 요망.



의심을 확신으로 만드는 전서 한 장.

그 안에 담겨 있는 내용을 확인한 당사독과 적천강이 작은 탄식을 토해 냈다.

“……이건.”

“이미 닷새 전이군. 거리를 따져 보았을 때, 사천지부에서도 오늘에서야 정보를 받고 전달한 것이 틀림없다.”

아마도 그럴 것이다. 적어도 사천당가에 모이기 전에 이 전서를 입수했다면 진작 알게 되었을 테니까.

하지만 한발 늦었다. 상산왕은 이미 금의위의 손아귀에 떨어졌고, 바로 그 금의위의 뒤에는 천자가. 혹은 암천이 있다.

‘아니, 암천이 천자를 움직이고 있는지도 모르지.’

과한 억측일 수도 있지만, 혈혼고의 존재만으로도 충분히 의심의 여지가 있는 부분이다.

백족의 대족장이자 남만야수궁의 이 인자였던 백상 역시 그러했으니까.

그리고 이 추측이 사실이라면…….

‘끝장이다. 남만 때와는 비교도 할 수 없어.’

남만야수궁은 하나의 문파이자, 작은 왕국이다.

하지만 대국(大國)은 말 그대로 대국.

폭탄의 크기도, 그 폭탄이 터졌을 때 파장이 미칠 범위도 차원이 다르다.

단지 상상하는 것만으로도 소름이 돋을 만큼.

그래서 어디 있는지도 모르는 상산왕을 찾아 나도 모르게 발걸음부터 옮길 만큼.

저벅.

“어딜 그리 급히 가나.”

목소리의 주인은 적천강도, 당사독도 아니었다.

나는 천천히 고개를 돌렸다. 막상 이쪽은 쳐다보지도 않은 채, 담담하게 어느 전서를 읽고 있는 남호의 모습이 그곳에 있었다.

“가야 합니다. 상산왕을 보호해야 해요.”

“뭐든 좋아. 하지만 어디로 갈 생각인가. 황도가 있는 동쪽? 아니면 산서가 있는 북쪽? 설마 남쪽이나 서쪽은 아니겠지.”

나는 혼란스러운 와중에도 최대한 침착하게 입을 열었다.

“우선 북동쪽으로 방향을 잡아 볼 생각입니다. 개방과 하오문의 힘을 최대한 빌려 그들을 추적하면서요.”

“틀렸어.”

“네? 그게 무슨…….”

너무나도 단호한 어조에 의아해하던 그때, 남호가 말없이 손에 든 전서를 내게 보여 주었다.



一. 발신. 낙조표국.

二. 상산왕 및 금의위 오십 인. 산서성 출(出).

三. 산동과 강소를 거쳐 절강으로 향할 것으로 예상됨.

四. 현재 속도로 미루어 보았을 때, 다음 달 초하루 강소성 진입.

五. 호위 명령 하달. 호위 대상은 상산왕 주표. 참여 인원은 화왕 적천강. 열화신룡 진태경 및 화룡각 전원.



마지막 줄에 적힌 ‘명령 하달’이라는 네 글자를 본 순간, 나는 본능적으로 깨달았다. 이 전서가 어디에서 보내진 것인지.

내게, 아니 적천강에게 명령을 하달할 수 있는 곳은 천하에 오직 한 군데뿐이니까.

“무림맹……!”

“정확히는 은영각이지. 물론 맹주의 재가(裁可)를 거쳤겠지만.”

“낙조표국이라니. 이건 뭡니까? 이미 모든 전서를 살펴봤는데 도대체 어디에서…….”

말꼬리를 흐린 나는 문득 콧속을 파고드는 혈향을 따라 고개를 돌렸다.

도대체 언제 저렇게 된 걸까. 철창에 갇혀 있던 전서구 중 하나가 배가 갈라져 죽어 있었다.

“은영각에서 자주 쓰는 방법이라네. 애꿎은 전서구 입장에서는 억울하겠지만, 우리로서는 녀석들의 배 안에 숨겨두면 더 확실하거든.”

할 말을 잃은 채 바라보는 나. 아니, 모두의 모습에 남호가 담담한 미소를 띠며 말을 이었다.

“아직도 머뭇거릴 여유가 있나? 초하루까지는 보름도 안 남았어. 지금 서둘러 출발한다면 적어도 강소성에서는 상산왕을 따라잡을 수 있을걸세.”

맞다. 더 머뭇거릴 시간 따위는 없었다.

나는 황급히 어둠 속을 향해 쏘아졌다.

남은 시간은 보름 남짓. 한 시라도 서둘러야 한다.
```

## Final English reading copy

```markdown
# Chapter 853

Information is like a puzzle that can never be completed with just one piece.

Unless you gather the pieces and fit them together, they’re not information at all—just questions with no value.

The Embroidered Uniform Guard who appeared in Anhui about fifteen days ago was no different.

They were just one small piece.

At least, they were until the City Lord of Sichuan Province died suddenly and the Blood Soul Gu was discovered.

*Things are different now.*

Emei and Qingcheng, members of the Nine Sects and One Gang; the Sichuan Tang Clan and the Beggars’ Sect—and even the Lower District Sect, whose ranks were largely made up of commoners—were all bona fide Murim organizations.

Now that a full-scale war with Dark Heaven had begun, information about the government was bound to fall down the list of priorities.

If your own neighborhood is on fire, you’d have to be crazy to go looking around the neighborhood next door.

But if the fire spread there, that changed everything.

We had to dig up every puzzle piece of information that had gone unreported for one reason or another—or been dismissed as mere suspicion.

And the dozen or so messenger pigeons that had just arrived at the Sichuan Tang Clan were carrying precisely those pieces.

“Have you arrived, Old Master? You too.”

It went without saying that the most important matters were reported to the Family Head first.

A scattering of tightly sealed missives lay in front of Tang Sadok, who had greeted Jeok Cheongang and me with a brief nod.

“Are those all… messages related to this?”

“Probably.”

At Tang Sadok’s brief reply and glance, the old man beside him—who had been carefully inspecting the messenger pigeons and their missives—spoke up.

“From what I’ve seen, there’s no sign the messenger pigeons were attacked, and none of the missives have been damaged.”

“Are you certain? This is important.”

“I stake my life on it.”

“That’s enough for me. I’ll send for you when the time comes. Until then, don’t let anyone in.”

“Yes, Family Head. I won’t let even a single rat get near.”

The old man bowed politely and left the room. His presence quickly faded into the distance.

Tang Sadok caught the meaning in Jeok Cheongang’s eyes and spoke first.

“He’s a household retainer who’s absolutely loyal to me. He’s handled messenger pigeons here for more than half his life, so I had him check them in case.”

The place Tang Sadok called “here” looked less like a pavilion and more like a huge aviary.

Even standing still, the sharp, musty smell of birds stung my nose. Iron cages of all sizes filled the space, and feathers of every color fluttered through the air.

It was clear that this place had been used for years solely to train messenger pigeons and send and receive their messages. Dozens of unopened missives were piled up inside.

“There are more than I expected. A lot more than the number of pigeons we saw before coming here.”

Tang Sadok gave a small nod at my words.

“I’m surprised, too. Usually, they send only the bare minimum of information to keep the messenger pigeons from attracting attention. But sending several pages on each one means…”

“They had a lot of information they needed to get through, even if they had to send it this way.”

Jeok Cheongang spoke up, then added in a low voice,

“And that means it was urgent.”

I opened the first missive and read it. I realized the words I’d just heard weren’t exaggerated in the slightest.

“What does it say?”

I was silent for a moment before answering Jeok Cheongang’s question.

“After Anhui, people suspected of being members of the Embroidered Uniform Guard appeared in Hubei.”

“Hubei? When did the information come in?”

“About twenty days ago.”

“Twenty days. Damn, that’s late.”

“By then, their trail in Anhui had already gone cold, and it seems neither the Beggars’ Sect nor the Lower District Sect in Hubei guessed they were the Embroidered Uniform Guard.”

Tang Sadok frowned.

“Isn’t it possible they weren’t the Embroidered Uniform Guard at all? If your guess is right and their target is Prince Shangshan, they’d have no reason to detour through Hubei to reach Shanxi. They could’ve gone straight from Anhui to Henan.”

He was right. Anhui was closest to Henan, and they could enter Shanxi by heading just a little farther north.

But Tang Sadok had clearly forgotten one important thing.

“If they are the Embroidered Uniform Guard, and they went so far as to disguise themselves to hide their identities from the start, then of course they’d avoid Henan.”

“What does that mean…? Ah.”

Tang Sadok let out a small exclamation and uttered a single word.

“The Murim Alliance.”

“Exactly. They nearly had their trail picked up even in Anhui. Henan is practically an impregnable fortress right now.”

The vast storm of war was reaching its peak, and the full-scale war with Dark Heaven had begun.

With everyone in the Central Plains Murim on high alert, crossing Henan—the home of the Murim Alliance’s headquarters—to reach Shanxi would be no different from giving away their identities.

The Murim Alliance wasn’t a fool.

Whether they were Dark Heaven’s agents or the Embroidered Uniform Guard, anyone suspicious would be identified in no time.

Even if the Sword Saint, Mae Jonghak, leader of the Murim Alliance, merely stood by with a gentle smile and watched, one old fox beside him would be different.

*Song Ho, the Thousand-Faced Fox.*

He had another title: Chief of the Hidden Shadow Pavilion.

At that very moment, as I pictured the Thousand-Faced Fox’s face, always marked by a faint smile—

Rustle.

A faint sound came from the crack beneath the firmly shut door. But no one in the room, myself included, was surprised or flustered.

We already had a fair idea who was approaching—and who it was.

Creeeak.

At Jeok Cheongang’s glance, I reached out. A gentle current of energy pushed the door open, revealing someone.

No—more accurately, it revealed two people who looked like one.

The Tang Family retainer who had left earlier had Namho pinned in an embrace from behind, a blade pressed to his Adam’s apple.

“……?”

“……?”

“……?”

What the hell was going on?

My brain stalled for a moment, but I quickly figured it out.

The Tang Family retainer who was supposedly so devoted to Tang Sadok that he’d do anything for him had been guarding the place to make sure not even a rat got in. Then he’d found Namho.

The minor problem was that Namho had almost died.

“You’re still young at heart. It’s not easy to get fired up at your age.”

Namho, restrained with the retainer pressed up against his back, replied with a face like he’d bitten into a turd.

“What does that mean?”

“Nothing. Anyway, stay still. Your Adam’s apple moves when you talk, and you’ll cut yourself on the blade.”

“Don’t push it with the threats—”

Slice.

“Shit, you’re right.”

“I told you not to talk.”

“So I’m using ventriloquism now.”

“Oh, ventriloquism. Teach me sometime.”

“Maybe, if I get the chance… Damn it. Cut the crap and get this man to stand down. He won’t listen no matter how much I explain.”

Jeok Cheongang stroked his chin, looking amused at Namho’s predicament.

“You were right about him being loyal. If he were just a little more reliable, he’d have killed an innocent man.”

“……Sometimes his loyalty goes too far. Let him go. He’s one of ours.”

At Tang Sadok’s sighing words, the retainer blinked, finally withdrew his dagger, and stepped back.

Namho watched him leave without so much as an apology and muttered,

“I’ve seen all kinds of lunatics, but this is something else. No wonder the Sichuan Tang Clan is—”

“Is what?”

When Namho met Tang Sadok’s meaningful gaze, he changed course at the speed of light.

“No wonder it’s called one of the Five Great Families under Heaven.”

That was an impressive drift. Still, even if you’d lived a long life, there was no reason to spend whatever you had left worrying about being poisoned.

“Anyway, why did you take so long? It’s been ages since I sent for you.”

“I was thinking back over something. Maybe it’s because I’m getting old, but my memory isn’t what it used to be.”

“Your memory?”

“Yes. My memory.”

Before I could even ask what he meant, Namho nodded toward the missive in my hand.

“That information you’re looking at—where did it come from?”

“The Hubei branches of the Beggars’ Sect and the Lower District Sect.”

“No. What about the one beside it?”

I opened another of the dozens of missives scattered across the table and checked it.

“It says Hoyeon Trading Company. I’ve never heard of it before. The contents say…”

“It’s a trading company under the Qingcheng Sect. More precisely, Hoyeon Sword, a lay disciple of the Qingcheng Sect, has been running it for twenty years. He’s a Peak master, but he’s much better at running a trading company than at martial arts. Hoyeon Trading Company is one of the five largest in Shandong.”

“What?”

“Oh, and there’s no need to tell me what it says. I’m looking for a different name. Just check where each message came from and let me know.”

“……”

I didn’t know what to ask first.

As far as I knew, he hadn’t set foot in the Central Plains since the Great Faction War. How could he know so much about news from twenty years ago?

Or what was the source he wanted me to look for, if he didn’t care about the contents?

Jeok Cheongang and Tang Sadok stared at him with wide eyes. I could only look at him, dumbfounded and silent. Namho clicked his tongue, displeased.

“I’m no Jiang Taigong. Did you think I spent all those years in Nanman just sitting around fishing? I kept up with news from the Central Plains through the Hidden Shadow Pavilion’s Hidden Thread while I was there. There’s nothing to be so surprised about.”

“This seems like more than just keeping up with the news. Even if I heard some of that, I wouldn’t remember it.”

“Call it an old man’s pastime. Anything else you want to say?”

It was probably more like an occupational habit than a pastime, but personal curiosities like that weren’t important right now.

I kept quiet and hurriedly began opening and reading the remaining missives.

They’d all been sent through the Sichuan Branch, but each had a different source. And since I had to read their contents to find what Namho was looking for, I naturally began sorting the information out in my head.

The result was shocking.

*It wasn’t just Anhui and Hubei.*

Anhui, Hubei, Hunan, Jiangsu, Shandong.

If the contents of each missive were true, people suspected of being members of the Embroidered Uniform Guard had appeared in all five provinces, then vanished without a trace.

*This is…*

A dispersed movement.

More likely a mobile strategy to avoid being noticed than a diversion.

They had split into groups of as few as ten and as many as thirty, spread out across the provinces, and then vanished upon reaching Shaanxi or Shandong.

*Shanxi. They gathered in Shanxi.*

There was no doubt. Avoiding Henan and drawing as little attention as possible, they’d gone around it, slipping into Shanxi through Shaanxi and Shandong—the provinces that lay along the continent’s flank.

And there…

*Prince Shangshan Zhu Bao.*

My heart sank. The next moment, I mechanically grabbed another missive. As soon as I read it, my teeth clenched without my realizing.

Crack.

“What is it?”

“What does it say?”

I didn’t answer. I unfolded the missive and held it out. Tiny letters had been written on the yellowed animal hide.

> 1. Sender: Shanxi Branch of the Lower District Sect.
>
> 2. Prince Shangshan Zhu Bao. Accompanied by the Embroidered Uniform Guard.
>
> 3. Hong Jin, Shanxi Province’s Second-Rank Deputy Military Commissioner. Requested support from the Lower District Sect and joined up with Prince Shangshan.
>
> 4. Tracking began. Concern that the authorities may intervene.
>
> 5. Operation suspended after the tracking team was wiped out.
>
> 6. This document is Grade Heaven. Deliver the information to the designated recipient as quickly as possible.
>
> 7. Blazing Flame Divine Dragon Jin Taekyung. Urgent search requested.

One missive that turned suspicion into certainty.

Tang Sadok and Jeok Cheongang read its contents and let out quiet exclamations.

“……This is…”

“This was already five days ago. Judging by the distance, the Sichuan Branch must have received the information and passed it on only today.”

That was probably right. If the missive had reached the Sichuan Tang Clan before we gathered here, I would’ve known about it already.

But we were a step too late. Prince Shangshan had already fallen into the Embroidered Uniform Guard’s hands, and behind the Guard stood the Son of Heaven. Or Dark Heaven.

*No—maybe Dark Heaven is controlling the Son of Heaven.*

It might have been an overreaching assumption, but the existence of the Blood Soul Gu alone gave me reason to suspect it.

Baeksang, the Great Chieftain of the Bai people and the second-in-command of the Nanman Beast Palace, had been the same.

And if that suspicion was true…

*We’re finished. What happened in Nanman won’t even come close.*

The Nanman Beast Palace was a sect and a small kingdom.

But the Great Nation was a great nation in the truest sense.

The size of the bomb—and the extent of the damage when it exploded—would be on another level entirely.

Just thinking about it sent a chill down my spine.

It was enough to make me start walking before I even knew where Prince Shangshan was.

Thud.

“Where are you in such a hurry to go?”

The voice didn’t belong to Jeok Cheongang or Tang Sadok.

I slowly turned around. Namho was calmly reading a missive, without even looking my way.

“We have to go. We need to protect Prince Shangshan.”

“Fine. But where are you planning to go? East, where the imperial capital is? Or north, where Shanxi is? Surely not south or west.”

Even in the midst of my confusion, I did my best to speak calmly.

“I’m thinking we should head northeast first. We’ll use the Beggars’ Sect and the Lower District Sect to track them down.”

“Wrong.”

“What? What do you mean…?”

I was baffled by his utterly firm tone. Namho said nothing, only holding out the missive in his hand.

> 1. Sender: Nakjo Escort Bureau.
>
> 2. Prince Shangshan and fifty members of the Embroidered Uniform Guard. Departed Shanxi Province.
>
> 3. Expected to head for Zhejiang through Shandong and Jiangsu.
>
> 4. At their current speed, they’ll enter Jiangsu Province on the first day of next month.
>
> 5. Escort order issued. The person to be escorted is Prince Shangshan Zhu Bao. Participants: Fire King Jeok Cheongang, Blazing Flame Divine Dragon Jin Taekyung, and every member of the Fire Dragon Pavilion.

The moment I saw the four characters *escort order issued* on the last line, I instinctively realized where the missive had come from.

There was only one place in the world that could issue orders to me—or rather, to Jeok Cheongang.

“The Murim Alliance…!”

“More precisely, the Hidden Shadow Pavilion. Though it must have had the Alliance Leader’s approval, of course.”

“The Nakjo Escort Bureau? What is this? I already checked every missive, so where did this even—”

My voice trailed off. I turned toward the scent of blood creeping into my nostrils.

When had that happened? One of the messenger pigeons in a cage had been disemboweled and lay dead.

“It’s a method the Hidden Shadow Pavilion often uses. It’s rough on the poor pigeon, but hiding the message inside its belly makes it safer for us.”

As everyone stared at him, speechless, Namho gave a calm smile and continued.

“Do we still have time to hesitate? There are fewer than fifteen days until the first of the month. If we leave now, we should be able to catch Prince Shangshan in Jiangsu at the very least.”

He was right. We didn’t have time to hesitate any longer.

I shot into the darkness.

We had a little over fifteen days left. We had to hurry, even if it was only by a single hour.
```

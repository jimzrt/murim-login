<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0904.txt",
      "sha256": "2375e28da08fd43a8fff1407d1474276144be721b0a7248a6d82b132a1b9be7d",
      "bytes": 14694
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "2cc5ede0ce15fa17ddedd2da91b5dcb6f17c1491a938a6bd58d8d42e87911a2e",
      "bytes": 929
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "15b7559bed5551ab89a765328d3f0a3fb2d8b907d46fb1c26625499fb4cab311",
      "bytes": 230936
    },
    {
      "path": "characters/Baek Yeon.md",
      "sha256": "36303fbbf22a8571823d825afb3798c15782309e2fd06dc0b2eaa70de3354e94",
      "bytes": 983
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "2012ab50c420f72b85b7386e7809154c50d73071ee3e962231f9d8d2a0688411",
      "bytes": 1499
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "cc8a546c21f15d3de01280495900ee97ec01579cfa0829506b2e78a5c00ff6dd",
      "bytes": 1369
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "1d87839ccf7e55c0c5d77477831c8918cb8a4ed63386c1c7bbe105b4e7e73e38",
      "bytes": 622
    },
    {
      "path": "characters/Ma Sanbao.md",
      "sha256": "4cb736390b4ce4056fa63e83d50470ecbd18196adf7cde31486aa0e1d79c2221",
      "bytes": 970
    },
    {
      "path": "characters/So Gyo.md",
      "sha256": "7c3dd432d603b587947a5bbcb10ea01a352c8acc9afe0f4fbd65262978599690",
      "bytes": 900
    },
    {
      "path": "characters/Southern Heaven Demon Empress.md",
      "sha256": "ba4c386de1fb523c6725f697031ef85d8a6a8b7f8da8884aa6b7ace69d430f10",
      "bytes": 715
    },
    {
      "path": "characters/Western Heaven Demon Lord.md",
      "sha256": "eef02f23e4e077985fffd62cb316696164c611a27b2f4679de7fa08eb365078c",
      "bytes": 888
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "852d5f73b9e4549b425f01d120cf2dd1002fa4e0bfe8e43a35aab4634191e961",
      "bytes": 262237
    }
  ],
  "estimated_tokens": 13050
}
-->

# Durable State Update — Chapter 904

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
1 and safe_through 904. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 904. Profile updates may replace only one
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
  "chapter": 904,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 904,
    "continuity_sources": [904],
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
    "The Emperor does not want Prince Shangshan endangered.",
    "So Gyo’s identity and allegiance remain unknown, including to Cang Gong.",
    "The Lord of Heaven is searching for Taekyung; Cang Gong wields a chilling power distinct from Yin-Cold Qi.",
    "An unknown figure blocks Taekyung’s attack, and the Fire King enters the banquet hall.",
    "Hyuk Mujin and the Fire Dragon Pavilion party are traveling to the Jiangsu–Zhejiang border on Taekyung’s mission.",
    "Countless silent figures have appeared in the forest near Mujin’s group."
  ],
  "continuity_sources": [
    903
  ],
  "open_questions": [
    "Who is So Gyo, and is she an ally or enemy?",
    "Who blocked Taekyung’s attack, and what is the unfamiliar power Cang Gong used?",
    "Who are the silent figures surrounding Mujin’s group?"
  ],
  "safe_through": 903,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 삼성     | **Three Saints**    |
| 암천     | **Dark Heaven**                  |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 살기     | **killing intent**                               |                                                       |
| 강호     | **martial world**                                | Prefer “Murim” where the setting itself is meant      |
| 제자     | **Disciple**                                 |
| 사형     | **Senior Brother**                           |
| 사제     | **Junior Brother**                           |
| 노부      | **this old man / I**                                            |
| 백연 | **Baek Yeon** | Commander of the Embroidered Uniform Guard. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 마삼보 | **Ma Sanbao** | The East Depot’s Brush-Holding Eunuch and second-in-command. |
| 소교 | **So Gyo** | The palace attendant leading the group assigned to serve Prince Shangshan. |
| 남천마후 | **Southern Heaven Demon Empress** | Title Honglan uses when revealing her identity. |
| 서천마군 | **Western Heaven Demon Lord** | Title of the middle-aged antagonist who commands the summoned black-robed hunters. |
| 화염신장 | **Flame Divine Palm** | Jopil's deadly palm technique, noted when Taekyung compares Jopil with Mukyung. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 천주 | **Lord of Heaven** | Authority invoked by the masked attackers. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 음한지기 | **Yin-Cold Qi** | Cold-aligned energy required in the treatment elixir. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 초인 | **superhuman** | A being who has surpassed ordinary human limits. |
| 시산혈해 | **sea of corpses and blood** | Description of the preceding months of bloodshed. |
| 사냥개 | **hunting dog** | Jin's demeaning metaphor for Ares personnel who obey Go Jun. |
| 서천 | **Western Heaven** | Short form used by the Lord of Heaven for the Western Heaven Demon Lord. |
| 남천 | **South Heaven** | Dark Heaven power that the Lord of Heaven orders the servants to contact. |
| 똥개 | **Ddong Gae** | Taekyung's mocking misremembering of Hwang Gae's name. |
| 서리 | **seori** | Colloquial term for stealing crops or produce from a field. |
| 마후 | **Demon Empress** | Title used for the Southern Heaven Demon Empress. |
| 초일류 | **Supreme First Rate** | Realm attained by each Baekcheon Unit member. |
| 금의위 | **Embroidered Uniform Guard** | Imperial guard force mentioned by Hong Jin. |
| 창공 | **Cang Gong** | The bedridden East Depot leader for whom Ma Sanbao acts. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 서천마군 | 진태경 | hostile_opponents | you | calm and taunting | Uses 자네 while questioning Taekyung and offering to take him alive. |
| 진태경 | 서천마군 | hostile_opponents | Western Heaven Demon Lord | casual and defiant | Identifies the Demon Lord by title and answers his surrender demand with sarcasm. |
| 서천마군 | 적천강 | hostile_invader_to_unconscious_patient | you | calm and predatory | Says someone wants to see Jeok Cheongang and attempts to move him with Seizing an Object Through Empty Space. |
| 적천강 | 서천마군 | hostile_opponents | you bastard | blunt and threatening | Jeok addresses the Western Heaven Demon Lord with 네놈 while defending Taekyung and ordering him not to touch his Disciple. |
| 중년인 | 진태경 | veteran civilian Hunter to celebrated allied Hunter | Mr. Jin | formal-polite and awed | The casualty clerk addresses Jin as 진 선생님 after Jin asks him to list Lei Fei among the dead. |
| 진태경 | 중년인 | celebrated Hunter to older fellow Hunter | sir | casual and teasing | Jin addresses the older Hunter as 아저씨 while joking with him and giving him instructions. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 남천마후 | 진태경 | hostile_supernatural_opponent_to_young_martial_artist | Young Great Hero / Child | lighthearted and taunting | Addresses Taekyung while refusing to explain the Gate. |
| 진태경 | 남천마후 | young_martial_artist_to_hostile_demon_empress | you | hostile and determined | Promises that the Southern Heaven Demon Empress will die when they meet again. |
| 적천강 | 남천마후 | legendary_martial_master_to_hostile_demon_empress | you bitch | blunt and threatening | Threatens to punish her and Lord of Heaven. |
| 남천마후 | 적천강 | hostile_demon_empress_to_legendary_martial_master | Fire King Jeok / you | flattering and mocking | Addresses Jeok Cheongang as the Fire King while praising Lord of Heaven. |
| 아빠 | 진태경 | father to son | Taekyung | affectionate informal | Addresses his young son warmly as Taekyung. |
| 진태경 | 아빠 | son to father | Dad | childlike informal | Taekyung addresses his father as Dad in the childhood flashback. |
| 남천마후 | 천주 | devoted_servant_to_revered_master | Lord of Heaven | reverent and prayerful | The Southern Heaven Demon Empress prays that the Lord of Heaven will remember her loyalty and love. |
| 진태경 | 백연 | young martial artist confronting an imperial military commander | you | casual and insulting | Refers to Baek as 이 양반 while challenging his conduct. |
| 진태경 | 황제 | guest of the Emperor’s younger brother addressing the Emperor | Your Majesty | formal and deferential in address, despite blunt challenges | Taekyung repeatedly addresses the Emperor as 폐하. |
| 소교 | 진태경 | palace attendant addressing a martial artist and guest under escort | Young Master Jin | formal and respectful, but firm | Addresses him as 진 공자 while escorting him and warning him not to investigate. |
| 진태경 | 소교 | palace attendant and martial artist under imperial scrutiny | you | formal-polite, controlled and challenging | Taekyung addresses So Gyo as 당신 while questioning her presence and demanding an explanation. |
| 백연 | 진태경 | imperial commander confronting a young martial artist | Jin Taekyung | measured and familiar, using 자네 | Baek Yeon cautions Taekyung about his words and asks whether he must cause a scene. |
| 소교 | 백연 | political ally addressing a senior military commander | you | informal and direct | So Gyo uses 당신 and speaks without formality; no personal name or title is established. |
| 백연 | 소교 | military commander addressing a powerful political ally | you | formal and deferential | Baek Yeon uses 그대 while questioning So Gyo; she speaks without formality, which he accepts as her due. |
| 마삼보 | 진태경 | political ally recruiting a young martial artist | you; my friend | courteous and familiar | Ma uses 자네 and 이보게 while explaining his choice of Jin and inviting him to join the restoration army. |
| 진태경 | 마삼보 | young martial artist addressing the East Depot’s Brush-Holding Eunuch and prospective ally | you; Brush-Holding Eunuch | polite and direct | Jin asks Ma why he withheld information and presses him for a clear answer; he refers to him as 태감. |
| 황제 | 진태경 | Emperor addressing a subject and Prince Shangshan’s guest | Jin Taekyung | formal and authoritative | The Emperor addresses Taekyung by his family and personal name before asking what to do with the two officials. |

## Listed compact profiles

### Baek Yeon.md

# Baek Yeon (백연)

- **Safe through:** Chapter 901
- **Aliases:** Blood Envoy
- **Role:** Baek Yeon is the Commander of the Embroidered Uniform Guard, a former martial arts instructor to the Crown Prince, and the Blood Envoy who helped the fourth prince seize the throne and led the purge.
- **Personality:** Politically assured and controlled, he enforces authority with ruthless decisiveness but speaks with striking defiance to the Emperor in private when their shared undertaking is at stake.
- **Voice:** Not established
- **Relationships:** He commands the Embroidered Uniform Guard and serves the Emperor; they share an old promise tied to a great undertaking, and Baek urges the Emperor to restore matters before their adversaries' moves unravel it. He orders Jeong Hogun to surveil Prince Shangshan’s party while leaving openings for an approach, and treats Taekyung as a dangerous potential obstacle.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 901
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm, the occupant of the chief seat of the Murim Alliance's Five Kings Hall, and a trusted confidant who accepts Jin as himself despite knowing that he travels between Murim and another world resembling the realm of immortals.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; believes there is no absolute justice and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He deeply trusts Jin Taekyung, his publicly acknowledged Disciple and intended heir, regards him as the light of his later years, and will stand by him whatever path he chooses; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and remains Peng Cheolhu's rival.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 903
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader.
- **Personality:** Hungry, self-aware, dryly observant, and pragmatic under pressure; accepts extreme personal risk when duty and the lives of others demand it.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; Ma Sanbao recruited Jin and Jeok for the restoration effort supporting Prince Shangshan, and Jin has signed its pledge and arranged for Ma to summon Murim Alliance reinforcements.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 903
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Ma Sanbao.md

# Ma Sanbao (마삼보)

- **Safe through:** Chapter 901
- **Aliases:** None
- **Role:** Ma Sanbao is the East Depot’s Brush-Holding Eunuch and Supreme Peak martial artist, leading it in place of the bedridden Cang Gong and organizing a secret restoration effort for Prince Shangshan.
- **Personality:** He is vigilant and patient, concealing his loyalties while awaiting the moment to act for the late Emperor.
- **Voice:** He speaks in measured, courteous language and uses calm repetition, feigned agreement, and procedural reminders to steer conversations while keeping sensitive details guarded.
- **Relationships:** Ma Sanbao is a longtime friend and former East Depot cohort of Hong Jin, leads the restoration effort for Prince Shangshan, and recruited Jin Taekyung and Jeok Cheongang as discreet allies; Jin has signed the pledge and entrusted Ma with summoning Murim Alliance reinforcements.

### So Gyo.md

# So Gyo (소교)

- **Safe through:** Chapter 903
- **Aliases:** None
- **Role:** A palace attendant assigned to Prince Shangshan who is a Supreme Peak master and has a mission to keep Jin Taekyung alive; her identity and allegiance remain unconfirmed.
- **Personality:** Calm, calculating, and self-possessed; she conceals her strength and identity and can be openly taunting.
- **Voice:** Measured and composed, shifting from deferential formality to casual, pointed taunts and threats.
- **Relationships:** She poses as the leader of the palace attendants assigned to Prince Shangshan and is Jin Taekyung’s opponent, yet believes he may be the person she seeks and the person foretold by “that person”; she says only she and the Emperor know a secret she withheld from Baek Yeon, while her true allegiance remains unknown.

### Southern Heaven Demon Empress.md

# Southern Heaven Demon Empress (남천마후)

- **Safe through:** Chapter 903
- **Aliases:** None
- **Role:** The Southern Heaven Demon Empress was Honglan, the creator of the rift behind the Inner Palace, and was killed after the rift closed.
- **Personality:** Playful, cruel, confident, and casually dismissive of mass death and the suffering of others.
- **Voice:** Light, taunting, amused, and delighted even when discussing murder or imminent catastrophe.
- **Relationships:** She commands and advises Baeksang, treats Jin Taekyung and Yayul Cheok as expendable to the grand plan, and keeps a masked hunting dog whom she trained carefully.

### Western Heaven Demon Lord.md

# Western Heaven Demon Lord (서천마군)

- **Safe through:** Chapter 903
- **Aliases:** None
- **Role:** Former Protector of the Divine Cult who commands Dark Heaven's assault on the Sichuan Tang Clan, lost the Myriad-Poison Ring to Jin Taekyung, suffered a crushed ankle and a torn wrist, and was temporarily possessed by the Lord of Heaven before the borrowed body was destroyed.
- **Personality:** Cold, detached, patient, and utterly ruthless toward those he interrogates or hunts.
- **Voice:** Controlled and dispassionate, with concise statements delivered in a quiet, threatening tone.
- **Relationships:** Tang Taesang and the Heaven-Shaking Venerable Nun were his latest victims, he lost one arm taking their lives, and the Qilian Three Fiends now submit to him alongside his hundreds of black-robed hunters.

## Korean source

```text
＃904화



대연회장의 상황은 이미 돌이킬 수 없는 방향으로 치닫고 있었다.

흥겹게 울려 퍼지던 풍악은 이미 사라진 지 오래요, 후계자의 탄생을 축하하며 끝없이 이어지던 천세 삼창은 비명과 고함으로 뒤바뀌었다.

마침내, 도화선에 불이 붙은 것이다.

이제 연회는 끝났다.

하지만 동시에, 아직 끝나지 않은 또 하나의 연회가 남아 있었다.

서로를 향해 웃음 대신 병장기를, 술 대신 피가 흩뿌려질 홍문연(鴻門宴)이.

그리고 이 참혹한 연회의 시작을 알리는 거대한 굉음이, 온 사방을 떨어 울렸다.

콰아아아앙!

지축이 뒤흔들리고 끔찍한 열기가 터져 나온다. 이글거리는 화염과 먼지구름 너머로 한 인영이 섬광 같은 속도로 튕겨져 나온 것은 바로 그때였다.

쐐애애액!

콰드득!

간신히 내디딘 발끝을 따라 두부처럼 으스러지는 지면.

세찬 파공성과 함께 쏘아지던 신형을 간신히 바로 세운 청년, 진태경이 어느새 입에 고인 핏물을 뱉으며 중얼거렸다.

“그래, 한 수 위라 이거지…….”

속도, 힘, 완벽한 기습의 묘리까지 살렸음에도 명백한 격차.

진태경은 손에서 전해지는 저릿저릿한 통증과 함께, 조금 전 자신이 일장을 뻗었던 그 순간을 떠올렸다.

전력을 다한 화염신장이 가슴에 적중하려던 그때, 열양지기를 가볍게 억누르며 전신을 뒤흔들었던 얼음장 같은 기운을.

‘도대체 뭐지?’

그건 어지간한 노강호에 비견될 만큼 숱한 견문을 쌓은 진태경으로서도 처음 느껴보는 종류의 기운이었다.

보다 원초적인, 단순히 음한지기(陰寒之氣)로는 정의 내릴 수 없는 무언가.

하지만 그에 대한 의문을 해결하기에는 모든 것이 턱없이 부족했다.

정보와 경험.

그리고 시간마저도.

저벅. 저벅.

대연회장을 잠식한 혼란 속에서도 선명히 울려 퍼지는 발걸음 소리.

강대한 열양지기의 여파로 인해 처참하게 녹아내린 지면을 산책하듯 가로지르던 창공은 문득 걸음을 멈췄다.

바로 조금 전, 그가 서 있던 바로 그 자리에.

“다섯 걸음. 다섯 걸음이라.”

작게 뇌까리는 목소리에 탄성이 묻어나왔다.

터무니없이 젊은 나이에, 믿기지 않을 만큼 드높은 무위까지 도달한 무인을 향한 감탄이었다.

‘성치 않은 저 몸으로 노부를 다섯 걸음이나 물러서게 만들다니.’

막상 겪어 보니 이제야 알 것 같기도 했다.

무슨 이유로 ‘그분’께서 진태경에게 그토록 관심을 기울이시는지.

그 과정에서 서천마군과 남천마후라는 충복들을 잃었음에도 여전히 저 어린놈을 살려 두라 하시는지.

‘적이라면 가장 큰 걸림돌이 될 것이나, 아군이 된다면 머지않아 삼성(三星)조차 뛰어넘을 괴물.’

사로잡더라도 포섭하지 못하리라는 생각은 추호도 하지 않았다.

그분.

천주(天主)를 뵙게 된다면, 그 항거할 수 없는 절대자의 힘을 한 번이라도 느끼게 된다면 그분의 앞에 무릎 꿇을 수밖에 없을 테니까.

과거의 자신이 그러했듯이.

“천주께 데려가야겠군. 반드시.”

창공이 그렇게 뇌까린 바로 그 순간이었다.

“누구를, 누구한테 데려간다고?”

스아아아.

건조한 목소리와 함께 반경 수십여 장의 공기가 뜨겁게 달아오른다.

지면 위에서 피어오르는 아지랑이 너머로 다가오는 민머리의 중년인을 확인한 창공이 창백한 입술을 달싹였다.

“화왕(火王) 적천강.”

“노부의 존함을 어딜 함부로 입에 올리느냐, 이 불알 없는 놈아.”

“누가 사제지간 아니랄까 봐 언행이 쏙 빼닮았군. 제자가 스승에게 배운 것인지, 스승이 제자에게 배운 것인지는 모르겠지만.”

적천강이 시큰둥하게 대답했다.

“보통은 제자가 스승에게 배우는 법이니라. 네놈처럼 뿌리도 없는 호로새끼는 모르겠지만.”

“뿌리라, 한때는 내게도 그런 것이 있었지. 가족과도 같았던 스승과 사형제들도.”

“그렇군. 그럼 멀쩡한 불알을 자르는 것도 네놈 스승에게 배운 게냐?”

“아니.”

창공의 입가에 살기 어린 미소가 번졌다.

“그 어떤 상황에서도 스스로의 뿌리를 잊지 말라는 가르침을 받았지. 그런 스승님의 말씀을, 나는 단 한 순간도 잊어 본 적이 없다.”

“네놈에게 무슨 구구절절한 사연이 있는지는 모르겠지만…… 가르침이고 나발이고 더는 기억하지 않아도 될 게다.”

적천강이 주먹을 들어 올리며 씩 웃었다.

“이거 한 방 맞은 놈들은 전부 그렇게 됐으니.”

그리고 주위를 힐끗 둘러보며 덧붙였다.

“뭐, 굳이 노부가 아니어도 네놈을 찢어 죽이고 싶어 하는 것들은 널리고 널린 것 같지만.”

적천강의 말은 결코 과장이 아니었다.

무려 이천에 달하는 금의위.

하나같이 초일류에서 절정의 무위를 지닌 대국 제일의 정예군이 그들을 둥그렇게 에워싸고 있었으니까.

그뿐인가.

황제와 황실을 수호하는 금의위보다는 한 수 떨어진다는 평가를 받지만, 역시 정예라고 부르기에는 손색이 없는 금위군들까지 뒤늦게 합류하여 대연회장의 외벽을 점령하여 활시위를 겨누고 있었다.

물경 오천에 달하는 머릿수.

일군(一軍)이라 칭하기에 일말의 부족함도 없을뿐더러, 그 병력의 질은 가히 십만 대군과도 비견될 정도.

그러나 창공은 담담하게 사방을 둘러싼 무수한 창칼과 화살촉을 바라볼 뿐이었다.

정확히는 그들의 어깨너머, 높게 솟은 단 위에서 자신을 바라보고 있는 한 사람을.

“목줄 풀린 사냥개들은 죽을 자리도 못 알아보고 날뛰는데, 약아빠진 주인은 뒷전에 앉아 구경만 하는군.”

언제나 그랬듯이.

작게 덧붙인 창공이 소리 내어 웃었다.

그리고 불현듯.

뚝. 하고 끊어진 웃음소리와 함께 그의 창백한 입술 사이로 거대한 외침이 터져 나왔다.

“쳐라-!”

콰아아아!

음성에 실린 미증유의 공력이 대연회장을 뒤흔든 그 순간.

푹! 서걱!

금의위 중 하나의 가슴 위로 눈부신 검신이 솟아올랐다. 고통도 잊은 채, 황금빛 갑옷을 관통한 그것을 멍하니 바라보던 그가 더듬거리는 목소리로 중얼거렸다.

“도, 도대체 왜…….”

부릅떠진 눈동자에 서린 것은 경악인 동시에 불신이었다.

빠르게 죽음이 다가오는 와중에도, 그는 진심으로 알고 싶었다.

왜, 어찌하여 이토록 어이없게 죽음을 맞이해야 하는 것인지.

십 년이 넘도록 호형호제했던 동기가 왜 뒤에서 자신을 찔렀는지.

“크륵. 도, 동 형?”

왜일까.

어째서일까.

비록 피를 나누지는 않았으나 의형제로 여기겠다고 했다.

함께 격려하고 의를 다지며 이 나라와 황제 폐하께 충성을 다하자고 수십, 수백 번도 넘게 술잔을 기울이며 이야기했다.

그러나 끓어오르는 핏물을 참으며 토해 낸 그 외마디 부름에 돌아온 대답은, 지난 십 년간 들어 본 적 없는 무미건조한 목소리였다.

“천상천하(天上天下). 만마앙복(萬魔仰伏).”

“……!”

그것이 마지막이었다.

콰득.

비틀어 내며 뽑히는 검신과 함께 혼이 떠난 육신이 나동그라진다.

곳곳에서.

푹!

온 사방에서.

서걱!

수도 없이.

촤아아악!

깔끔하게 베어진 목이 지면으로 굴러떨어지고, 잘려 나간 사지와 핏물이 허공으로 솟구쳤다.

이천에 달했던 금의위 중, 물경 수백의 목숨이 그렇게 찰나지간에 사라졌다.

상관. 수하. 혹은 형제처럼 아꼈던 자신들의 동료에 의해서.

“……!”

“……!”

사방에서 먹먹한 고함이 터져 나왔다. 배반한 자와 배반당한 자. 지키려는 자와 빼앗으려는 자가 서로를 향해 얽혀들었다.

카카카캉!

서걱! 푹!

끄아아아악!

메아리와도 같은 비명과 함께 어둠 속에서 번갯불과도 같은 검광(劍光)이 쉴 새 없이 번뜩인다.

횃불을 들고 있던 누군가의 손이 피 웅덩이에 잠겨 꿈틀거렸다.

그리고 어둠 속에서 순식간에 벌어진 이 끔찍한 난전(亂戰) 위로, 또 다른 어둠이 덧씌워졌다.

솨아아아아.

그 소리를 들은 누군가는 비가 내린다고 생각했고, 죽음을 기다리며 헐떡이던 또 다른 누군가는 그리움 속 고향의 드넓은 평원을 떠올렸다.

저 멀리서 불어온 세찬 바람이 평원을 휩쓸면 꼭 이런 소리가 났었으니까.

잘 익은 곡식과 풀이 허리를 굽히고, 마을 잔치가 벌어졌던 커다란 거목(巨木)은 풍성한 가지와 잎사귀를 흔들었으니까.

하지만 두 번 다시 그리운 고향으로 돌아가지 못하리라는 것을, 이름 모를 그는 깨달았다.

‘아.’

하늘 위로 덧씌워진 어둠이, 아니 헤아릴 수 없이 무수한 화살의 비가 쏟아져 내리고 있었다.

그들의 머리 위로, 혹은 그들이 충성을 바치는 황제를 향해서 공간을 뒤덮으며 나아가고 있었다.

쿨럭.

내장 조각이 섞인 핏물을 내뱉으며 그는 마음속으로 중얼거렸다.

이건 아니었는데.

내가 고향을, 가족을 떠난 이유는 이렇게 허무하기 죽기 위해서가 아니었는데.

‘빌어먹을.’

그는 멍하니 짓쳐 드는 어둠을 바라보았다. 이 끔찍한 통증과 절망을 끝내줄 죽음을 기다렸다.

그리고 보았다.

화륵, 콰아아아!

어둠을 집어삼키는 거대한 화염을.

무수한 화살들을 형체도 남기지 않고 불태우는 그 압도적인 열기 속에서, 먹이를 낚아채는 한 마리의 매처럼 지상으로 낙하하는 한 청년을.

콰앙!

분명 천둥 같아야 할 굉음이, 수백여 장은 떨어져 있는 것처럼 흐릿하게 들리는 것은 왜일까.

그는 어두워지는 시야 속에서 생각했다.

저 청년의 이름이 무엇이었는지.

살려 달라는 그 한 마디가, 고향으로 돌려보내 달라는 그 짧은 부탁이 왜 목소리가 되어 흘러나오지 못하는지.

눈앞에 드리워지는 어둠 속에서, 그는 다만 지켜볼 수밖에 없었다.

쉴 새 없이 쏟아지는 화살 비를 불태우는 화염과 청년이 움직일 때마다 짚단처럼 쓰러져 가는 배신자들을.

자신과 같은 피륙으로 이루어진 인간이라고는 믿을 수 없는, 경천동지(驚天動地)의 전투를 시작한 두 존재를.

쾅! 쾅! 콰아아앙!

뜨거운 열기가. 몸서리치는 한기가.

쉬지 않고 사방을 물들이는 화염과 새하얀 섬광이 밤을 불태우고 얼어 붙인다.

지금 이 순간에도 곳곳에서 피를 흩뿌리며 쌓여 가는 수많은 시체를 장작으로 삼아.

그리고 남들보다 조금 더 긴 고통을 느껴야 했던, 불행한 누군가의 목숨을 제물 삼아.

하지만 그 끔찍한 기다림 끝에서, 이름 모를 금의위는 잠시 잊고 있던 청년의 이름을 떠올릴 수 있었다.

‘진태경. 그래, 진태경이었어.’

희한한 일이었다.

피 웅덩이에 잠긴 채, 시산혈해의 한 가운데에서 죽어 가는 와중에도 그는 조금의 추위조차 느끼지 못했다.

‘따뜻하다.’

번뜩이는 창칼 사이로 넘실거리는 화염을 바라보던 그는 쏟아지는 졸음을 이기지 못하고 눈을 감았다.

두 번 다시 돌아가지 못할 고향을 떠올리며.



* * *



호사가들은 말한다.

초절정 고수를 죽일 수 있는 것은 흐르는 세월과 스스로의 방심뿐이라고.

그리고 지금 이 순간, 나는 그 호사가들에게 말해 주고 싶다.

‘그럼 니들이 싸워 보든가.’

초절정 고수도 어차피 피륙으로 이루어진 사람이다.

뭣 모르는 놈들의 시선에는 수백, 수천의 적도 쓰러트리는 초인으로 보일지 몰라도 결국 한계는 있다.

그 수백, 수천 명 중 최소 절반 이상이 절정의 경지에 오른 고수라면 더더욱.

쉬릭, 촥!

누군가 뻗은 창날이 아슬아슬하게 볼을 스치듯 지나간다. 창날에 담긴 공력에 의해 베어져 나가는 살갗은 기본 옵션이고, 그놈에게 되돌려 주는 주먹은 보너스다.

퍼엉!

화염신장에 가슴을 가격당한 금의위, 아니 암천이 심어 놓은 배신자가 실 끊어진 인형처럼 튕겨 나갔다.

볼 것도 없는 즉사.

그러나 빈 자리는 또 다른 누군가로 채워졌고, 그들의 움직임은 한층 신중하면서도 기민해졌다.

‘제기랄.’

차라리 무림인이라면 훨씬 상대하기가 수월했을 것이다. 하지만 놈들은 무인인 동시에 군인이었다. 무공의 강력함과 군대로서의 규율을 지닌 집단.

서걱, 푹!

누군가의 손에서 빼앗은 창을 닥치는 대로 휘둘렀다. 사방을 에워싼 적들의 어깨너머를 노려보며.

‘도대체 왜!’

당장이라도 외치고 싶었다.

왜 돕지 않느냐고.

이런 급박한 상황까지 왔음에도 왜 모든 것을 방관하느냐고.

내 시선이 향한 방향의 끝에는 황제가 있었다. 망부석처럼 그 곁을 지키고 있는 백연과 소교의 모습도 함께.

그리고 지금, 막 한 사람이 추가됐다.

난데없이 시야에 끼어든, 결코 달갑지 않은 손님이.

슈확!

예리한 파공성과 동시에, 주위에서 분전하고 있던 십여 명의 금의위가 움직임을 멈췄다.

믿을 수 없다는 듯이 부릅떠진 눈.

하지만 냉정한 현실을 알려 주듯이 그들의 목 위로 점점 진하게 드러나는 희미한 혈선(血線).

꾸륵, 촤아아악!

몽글몽글하게 맺혀가던 핏물이 분수처럼 뿜어져 나온다. 썩은 고목처럼 쓰러지는 신형들을 스쳐 지나온 그가 나를 바라보며 한숨을 내쉬었다.

“왜 그랬나. 그저 믿고 따라왔다면, 모든 것이 잘 풀릴 수 있었을 텐데.”

옆집 똥개도 알아들을 개소리를 지껄이는 마삼보를 향해, 나는 대답 대신 창날을 내리그었다.

솨악!
```

## Final English reading copy

```markdown
# Chapter 904

The situation in the Grand Banquet Hall had already spiraled beyond anyone’s control.

The festive music had long since fallen silent, and the endless cries of “Ten thousand years!” celebrating the heir’s birth had turned into screams and shouts.

At last, the fuse had been lit.

The banquet was over.

But at the same time, another banquet remained—one that had not yet ended.

A Hongmen Banquet,[^1] where they would turn weapons on one another instead of smiling, and spill blood instead of wine.

Then a tremendous roar announced the start of that horrific feast, shaking everything around it.

*BOOOOM!*

The ground shuddered, and a dreadful wave of heat erupted. At that very moment, a figure shot out from beyond the blazing flames and clouds of dust at the speed of a flash.

*Whooosh!*

*Crunch!*

The ground crumbled like tofu beneath the tip of the foot that barely touched down.

Jin Taekyung, the young man who’d just managed to steady himself after being hurled through the air with a sharp blast, spat the blood pooling in his mouth and muttered,

“So, you’re a cut above me…”

Even after making full use of speed, strength, and the art of a perfect surprise attack, the gap between them had been unmistakable.

Along with the tingling pain in his hand, Jin Taekyung remembered the moment he’d thrust out his palm.

The instant his full-power Flame Divine Palm was about to strike the man’s chest, an icy energy had lightly suppressed his Scorching Yang Qi and shaken his entire body.

*What the hell was that?*

It was a kind of energy Jin Taekyung had never felt before, despite having enough experience to rival most veteran masters.

Something more primal. Something that couldn’t be defined as mere Yin-Cold Qi.

But there was far too little of everything he needed to solve the mystery.

Information. Experience.

And time.

*Clop. Clop.*

Even amid the chaos consuming the Grand Banquet Hall, footsteps rang out clearly.

Cang Gong strolled across the ground, which had melted horribly in the wake of that powerful Scorching Yang Qi. Then he suddenly stopped.

Right where he’d been standing moments earlier.

“Five steps. He made me retreat five steps.”

His low mutter carried a note of admiration.

It was admiration for a martial artist who’d reached astonishing heights at an absurdly young age.

*To make this old man retreat five steps, in that battered condition.*

Now that he’d experienced it firsthand, he thought he finally understood why *that person* had taken such an interest in Jin Taekyung.

Why *that person* had ordered them to keep that young brat alive, even after losing two loyal servants—the Western Heaven Demon Lord and the Southern Heaven Demon Empress—in the process.

*As an enemy, he’d be the greatest obstacle. But as an ally, he’d soon become a monster who could surpass even the Three Saints.*

He never once considered that Jin Taekyung might refuse to join them, even if they captured him.

If he ever met the Lord of Heaven—if he felt even once the power of that irresistible absolute—he’d have no choice but to kneel before him.

Just as Cang Gong himself had once done.

“I’ll have to take him to the Lord of Heaven. No matter what.”

It was at that very moment that Cang Gong muttered those words.

“Take who to whom?”

*Fwoosh.*

With that dry voice, the air within a radius of dozens of yards grew scorching hot.

Cang Gong’s pale lips parted when he saw the bald, middle-aged man approaching through the shimmering haze rising from the ground.

“Fire King Jeok Cheongang.”

“How dare you toss my honored name around, you ball-less bastard?”

“You two really are alike in speech and behavior. You’d think one learned it from the other—though I couldn’t say whether the disciple learned it from the master or the master from the disciple.”

Jeok Cheongang gave him an indifferent reply.

“Usually the disciple learns from the master. Though a rootless bastard like you wouldn’t know that.”

“Roots, huh? I had those once. A master and fellow disciples who were like family.”

“I see. So did you learn to cut off your own balls from your master?”

“No.”

A murderous smile spread across Cang Gong’s lips.

“He taught me never to forget my roots, no matter the circumstances. I have never forgotten his words for even a moment.”

“I don’t know what long-winded sob story you’ve got, but… teaching or whatever, you won’t need to remember it anymore.”

Jeok Cheongang raised his fist and grinned.

“Everyone who’s taken a hit from this old man ended up like that.”

He glanced around and added,

“Well, even without me, looks like there are plenty of people who’d love to tear you apart.”

Jeok Cheongang wasn’t exaggerating.

Nearly two thousand members of the Embroidered Uniform Guard surrounded them in a circle. Every one of them was among the Great Nation’s finest troops, martial artists ranging from Supreme First Rate to Peak.

And that wasn’t all.

The Imperial Guards, considered a cut below the Embroidered Uniform Guard who protected the Emperor and the imperial family, were no less deserving of being called an elite force. They’d arrived late, seized the outer walls of the Grand Banquet Hall, and drawn their bows.

Five thousand men in all.

There wasn’t the slightest doubt they could be called an army. In terms of quality, their forces could rival even an army of a hundred thousand.

And yet Cang Gong calmly looked at the countless spears, swords, and arrowheads surrounding him.

Or, to be precise, he looked past their shoulders, toward the one man watching from atop the high platform.

“The hunting dogs have slipped their leashes and are running wild without even knowing where they’ll die, while their cunning master sits back and watches.”

Just as he always had.

After adding that under his breath, Cang Gong laughed aloud.

Then, abruptly—

His laughter cut off, and a tremendous shout burst from between his pale lips.

“Attack!”

*BOOOOM!*

The unprecedented internal energy carried by his voice shook the Grand Banquet Hall. At that instant—

*Thrust! Slash!*

A dazzling blade burst out of one member of the Embroidered Uniform Guard’s chest. He stared blankly at it, the sword piercing his golden armor, too stunned even to feel the pain. Then he stammered,

“W-Why…?”

His wide eyes held both shock and disbelief.

Even as death rushed toward him, he desperately wanted to know.

Why? Why was he dying so pointlessly?

Why had the comrade he’d called hyung for more than ten years stabbed him in the back?

“Ghk. D-Dong hyung?”

Why?

How could this be?

They weren’t related by blood, but they’d promised to treat each other as sworn brothers.

They’d raised their cups together dozens, hundreds of times, encouraging each other, strengthening their bond, and swearing their loyalty to this country and His Majesty the Emperor.

But when he gasped out that one desperate call, trying to hold back the blood rising in his throat, the answer that came back was a dry voice he’d never heard in ten years.

“Heaven above, earth below. All demons bow in reverence.”

“……!”

That was the last thing he heard.

*Crunch.*

The sword twisted and pulled free. The soulless body toppled to the ground.

Everywhere.

*Thrust!*

All around.

*Slash!*

Countless times.

*Shhhk!*

Necks neatly severed rolled across the ground. Chopped limbs and streams of blood shot through the air.

In the blink of an eye, hundreds of lives vanished from the two thousand members of the Embroidered Uniform Guard.

At the hands of their own comrades—superiors, subordinates, even men they’d cherished like brothers.

“……!”

“……!”

Muffled shouts burst out from every direction. The traitors and the betrayed, those who fought to protect and those who fought to take, clashed with one another.

*Clang-clang-clang!*

*Slash! Thrust!*

“Aaagh!”

Amid echoes of screams, flashes of swordlight flickered ceaselessly through the darkness.

Someone’s hand, still holding a torch, twitched in a pool of blood.

And over the horrific melee that had erupted in an instant beneath the cover of night, another darkness descended.

*Fwoooooosh.*

Some who heard it thought it was raining. Another man, panting as he waited for death, remembered the wide plains of his hometown.

When a strong wind blew in from far away and swept across the fields, it made a sound just like this.

The ripe grain and grasses would bend at the waist. The great tree where the village festival had been held would shake its lush branches and leaves.

But the nameless man realized he’d never return to the hometown he missed.

*Ah.*

The darkness covering the sky wasn’t darkness at all. It was an uncountable rain of arrows pouring down.

They spread across the sky as they rushed toward the people below—or toward the Emperor they’d sworn their loyalty to.

*Cough.*

Spitting blood mixed with bits of his innards, he muttered to himself.

This wasn’t how it was supposed to be.

He hadn’t left his hometown and family just to die this pointlessly.

*Damn it.*

He stared blankly at the darkness rushing toward him, waiting for death to end this terrible pain and despair.

And then he saw it.

*Fwoosh—BOOOOM!*

A tremendous blaze devoured the darkness.

In that overwhelming heat, which burned the countless arrows to nothing, a young man plunged toward the ground like a hawk snatching up its prey.

*BOOM!*

Why did a roar that should have sounded like thunder seem faint, as if it were hundreds of yards away?

As his vision dimmed, he wondered what the young man’s name was.

Why couldn’t the words “Please, save me”—that short plea to send him home—come out as a voice?

He could only watch through the darkness gathering before his eyes: the flames burning the endless rain of arrows, and the traitors falling like bundles of straw whenever the young man moved.

He watched the two beings begin a battle that shook heaven and earth, beings he couldn’t believe were made of the same flesh and blood as him.

*Bang! Bang! BOOOOM!*

Scorching heat. Shuddering cold.

Flames and white flashes dyed every corner of the night, setting it ablaze and freezing it over.

Even now, countless corpses piled up as blood splattered in every direction, used as firewood.

And the life of one unfortunate man, made to suffer a little longer than the others, as its sacrifice.

But at the end of that horrific wait, the nameless member of the Embroidered Uniform Guard managed to remember the young man’s name—the one he’d almost forgotten.

*Jin Taekyung. Right. It was Jin Taekyung.*

It was strange.

Though he lay in a pool of blood, dying amid a sea of corpses and blood, he didn’t feel even the slightest bit cold.

*It’s warm.*

Watching the flames surge between the flashing spears and swords, he couldn’t fight off the sleep pouring over him. He closed his eyes.

Thinking of the hometown he’d never return to.

* * *

People who love to talk say that the only things capable of killing a Supreme Peak master are the passage of time and their own carelessness.

And right now, I wanted to tell those people:

*Then why don’t you try fighting them?*

A Supreme Peak master is still a person made of flesh and blood.

To people who don’t know any better, he might look like a superhuman who can take down hundreds or thousands of enemies. But there are limits.

Especially when at least half of those hundreds or thousands are Peak masters.

*Swish! Thwack!*

The tip of a spear someone thrust out skimmed past my cheek by a hair. Getting my skin sliced open by the internal energy packed into its blade was just the standard package. My fist returning the favor was a bonus.

*Wham!*

The member of the Embroidered Uniform Guard—no, the traitor planted by Dark Heaven—went flying like a puppet with its strings cut after my Flame Divine Palm struck him in the chest.

A clear-cut instant death.

But someone else filled the gap, and their movements grew more cautious and agile.

*Damn it.*

If they’d been ordinary martial artists, they’d have been much easier to deal with. But they were martial artists and soldiers at the same time. A group with the power of martial arts and the discipline of an army.

*Slash! Thrust!*

I snatched a spear from someone’s hands and swung it wildly, glaring past the shoulders of the enemies surrounding me.

*Why the hell?!*

I wanted to shout it right then and there.

Why weren’t they helping?

Why were they just standing by, even when things had gotten this bad?

At the end of the direction I was looking, the Emperor stood there. Baek Yeon and So Gyo were beside him, guarding him like stone statues.

And now someone else had joined them.

An unwelcome guest who’d suddenly stepped into my line of sight.

*Whoosh!*

At the same time as a sharp blast of air, a dozen or so members of the Embroidered Uniform Guard fighting nearby stopped moving.

Their eyes were wide with disbelief.

Then, as if to reveal the cold truth, faint lines of blood appeared on their necks, growing darker by the second.

*Gurgle—SHHHK!*

The blood, gathering in thick beads, sprayed out like fountains. The man who’d swept past the falling bodies, which crumpled like rotten trees, looked at me and sighed.

“Why did you do that? If you’d simply trusted me and followed along, everything could have gone smoothly.”

Instead of answering Ma Sanbao’s bullshit—the kind even the mutt next door could understand—I brought my spearhead down.

*Whoosh!*

[^1]: A Hongmen Banquet is a treacherous feast, named after a famous historical ambush during a banquet.
```

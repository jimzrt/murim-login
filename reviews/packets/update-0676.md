<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0676.txt",
      "sha256": "ca7e54f222555cd856f227ede9c9908e74619faa615528bc7d492cecf583ac44",
      "bytes": 13302
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "1b0bfc6fd88e1a6833e4dda550ec787e9154e0e4a5410ccd35d81774537fbb36",
      "bytes": 2550
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "6c78ffaa1ea268bd2774e6a91268e4e10199d6311a9d431b27a1aba295079287",
      "bytes": 202892
    },
    {
      "path": "characters/Baeksang.md",
      "sha256": "06ead70188c45f830dd294ec618d897428cd9a5f3b93e103769db069e332f498",
      "bytes": 1071
    },
    {
      "path": "characters/Beast Miao King.md",
      "sha256": "ca6d78b28afd8447f07cdf5f030b7d54ed7717596bb4fbd702ba3eb9de6e4213",
      "bytes": 830
    },
    {
      "path": "characters/Blood Lord.md",
      "sha256": "5b69d159842dd6b88fb63cc1f717947485ba43cde445dad704d23cdf26baa2c7",
      "bytes": 830
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "bc0f676460287bd0ad3f7cdc9100b45d87ed05074c90c2fa037d07343e5fd273",
      "bytes": 553
    },
    {
      "path": "characters/Heugung.md",
      "sha256": "78d9281faff612c524e6b3531641006421b95dddf2dddfbfa05078c786092f4d",
      "bytes": 769
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "7cb6b13fc5117c4598fcf4260c702ebf18593e89db6cb76ec89dcbff606c7bc8",
      "bytes": 1702
    },
    {
      "path": "characters/Mae Jonghak.md",
      "sha256": "eadcbb70d80d9a6f9fdae03b5ac25302df182bf9f4fd5b58ca685ed9681b8f35",
      "bytes": 1061
    },
    {
      "path": "characters/Muyaho.md",
      "sha256": "25851813856ce47c379f960ca0dba9c3d2cb0e613867385cb051a2d7b049a6fa",
      "bytes": 580
    },
    {
      "path": "characters/Western Heaven Demon Lord.md",
      "sha256": "a5c04dee60d5a5c159afffffdb55641ef84a748153679b6ec702cfc0ca48d77e",
      "bytes": 888
    },
    {
      "path": "characters/Yayul Mok.md",
      "sha256": "cc7c11e26398ad7918ac4cdeb19b43eabef7c9471fe2446f4223eeb890626cf7",
      "bytes": 864
    },
    {
      "path": "characters/Yohi.md",
      "sha256": "6b72ededec0800c5dfe604b55da64798206f97ab5409ac4ab1b542adb8077b3f",
      "bytes": 645
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "7e200d58e8e3a1187e0dd4b39d26d7a3ce0752ab097097d71117da83357ea7b8",
      "bytes": 209462
    }
  ],
  "estimated_tokens": 12837
}
-->

# Durable State Update — Chapter 676

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 676. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 676. Profile updates may replace only one
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
  "chapter": 676,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 676,
    "continuity_sources": [676],
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
    "Nanman has issued a general mobilization order under Baeksang, with nearly ten thousand troops stationed in the Inner Palace and three tribes moving under his leadership.",
    "The Miao people are under strict surveillance and did not respond to the mobilization order.",
    "Baeksang is the temporary Palace Lord of the Nanman Beast Palace and remains under the Southern Heaven Demon Empress's command.",
    "Baeksang's left arm was severed by Force, and he remains conflicted about opposing his sworn elder brother, the Beast Miao King.",
    "The Southern Heaven Demon Empress ordered Baeksang to find and eliminate the Beast Miao King within three days while Dark Heaven handles Jin Taekyung.",
    "Dark Heaven's decades-long great undertaking is nearing completion and is intended to open a bridgehead from Nanman toward the Central Plains.",
    "Dark Heaven expects the return of the Lord of Heaven at the end of its undertaking.",
    "Jin Taekyung and Muyaho are in Ailao Mountain, following the tracking scent connected to Yohi through a Supreme Peak-grade Quest.",
    "Jin Taekyung believes rescuing Yohi and Heugung could prove his innocence, reveal the truth behind the Nanman tragedy, and change the balance of power.",
    "Jin Taekyung and Muyaho defeated hundreds of ambushing Nanman forces, and Jin captured a tribal chieftain who revealed the mobilization order.",
    "Jin Taekyung suspects Dark Heaven's plan is larger than previously believed and nearing completion."
  ],
  "continuity_sources": [
    675
  ],
  "open_questions": [
    "What exactly is Dark Heaven's great undertaking and how will it bring about the Lord of Heaven's return?",
    "Can Jin Taekyung and Muyaho find and rescue Yohi and Heugung in Ailao Mountain?",
    "What is the purpose of Baeksang's general mobilization and the army stationed in the Inner Palace?",
    "Can the Beast Miao King evade Baeksang's three-day pursuit?",
    "How will Jin Taekyung survive Dark Heaven's direct intervention?"
  ],
  "safe_through": 675,
  "temporary_decisions": [
    "Use Great Chieftain for 대족장 and Palace Lord for 궁주.",
    "Use temporary Palace Lord for 임시 궁주 and Inner Palace for 내궁.",
    "Use Southern Heaven Demon Empress for 남천마후 and Dark Heaven for 암천.",
    "Use Great undertaking for 대사 when it refers to Dark Heaven's plan.",
    "Preserve the Southern Heaven Demon Empress's playful, taunting menace and Jin Taekyung's crude, irreverent narration."
  ],
  "version": 1
}
```

## Exact glossary matches

| 적천강    | **Jeok Cheongang** |
| 매종학    | **Mae Jonghak**    |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 검성     | **Sword Saint**               | Mae Jonghak    |
| 열화문    | **Fire Gate Clan**               |
| 암천     | **Dark Heaven**                  |
| 남만야수궁  | **Nanman Beast Palace**          |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 신법     | **movement technique**                           |                                                       |
| 마교     | **Demonic Cult**                                 |                                                       |
| 시스템              | **System**                     |
| 퀘스트              | **Quest**                      |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 백상 | **Baeksang** | Great chieftain of the Bai people and Yayul Cheok's sworn younger brother. |
| 야수묘왕 | **Beast Miao King** | Leader of the Miao people and master of the Nanman Beast Palace. |
| 혈주 | **Blood Lord** | Title of the unidentified young man encountered by Han Su. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 흑웅 | **Heugung** | Great chieftain of the Yi people; his name literally means Black Bear. |
| 무야호 | **Muyaho** | Yayul Mok's White Tiger's name; it means tiger of the mighty wilds. |
| 서천마군 | **Western Heaven Demon Lord** | Title of the middle-aged antagonist who commands the summoned black-robed hunters. |
| 야율목 | **Yayul Mok** | Young Palace Lord of the Nanman Beast Palace. |
| 요희 | **Yohi** | Female great chieftain of the Yao people. |
| 화염신장 | **Flame Divine Palm** | Jopil's deadly palm technique, noted when Taekyung compares Jopil with Mukyung. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 준이 | **Jun** | Family nickname used in the form Jun's dad. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 성도 | **Chengdu** | Sichuan destination of Taekyung's party. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 피독주 | **poison-warding pearl** | Poison-neutralizing artifact carried by the black-clad attackers. |
| 남천마후 | **Southern Heaven Demon Empress** | Title Honglan uses when revealing her identity. |
| 촌각 | **moments** | Short intervals disappearing from Jeok's day. |
| 오독문 | **Five Poisons Sect** | Formerly dominant Nanman faction destroyed by the Fire Gate Clan. |
| 독물 | **venomous beasts** | Venomous creatures associated with the Nanman Beast Palace. |
| 서천 | **Western Heaven** | Short form used by the Lord of Heaven for the Western Heaven Demon Lord. |
| 남천 | **South Heaven** | Dark Heaven power that the Lord of Heaven orders the servants to contact. |
| 애뇌산 | **Ailao Mountain** | Mountain crossed by the party on the route to the Nanman Beast Palace. |
| 백호 | **White Tiger** | Yayul Mok's tiger companion. |
| 독혈지 | **Poisonblood Grounds** | Hidden poisonous region created by the Five Poisons Sect inside Ailao Mountain. |
| 독무 | **Poison Mist** | Deep green mist covering the Poisonblood Grounds swamp. |
| 야율 | **Yayul** | Name used in Taekyung's colloquial address to the Beast Miao King. |
| 천년지주 | **Thousand-Year Spider** | Monster appearing at the end of the chapter. |
| 인벤토리 | **Inventory** | System storage summoned by Jin. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혈주 | 적천강 | claimed enemy to enemy | your enemy | calm and threatening | The Blood Lord identifies himself as Jeok's enemy and claims to have killed Jeok's most precious friend. |
| 매종학 | 혈주 | legendary_martial_master_to_enemy | you | cold and judgmental | After revealing himself, Mae Jonghak condemns the Blood Lord's accumulated sins and orders him to pay the price. |
| 혈주 | 매종학 | enemy_to_revealed_legendary_master | you | shocked and hostile | The Blood Lord addresses Mae Jonghak with 당신 immediately after recognizing him as the Sword Saint. |
| 서천마군 | 신의 | hostile_invader_to_physician | Divine Physician | calm and mocking | Uses 신의 and 그대 while taunting the physician and dismissing his objections. |
| 신의 | 서천마군 | physician_to_invading_fiend | fiend | defiant and formal | Calls the Western Heaven Demon Lord an 악귀 and orders him to leave. |
| 서천마군 | 적천강 | hostile_invader_to_unconscious_patient | you | calm and predatory | Says someone wants to see Jeok Cheongang and attempts to move him with Seizing an Object Through Empty Space. |
| 적천강 | 서천마군 | hostile_opponents | you bastard | blunt and threatening | Jeok addresses the Western Heaven Demon Lord with 네놈 while defending Taekyung and ordering him not to touch his Disciple. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 적천강 | 남천마후 | legendary_martial_master_to_hostile_demon_empress | you bitch | blunt and threatening | Threatens to punish her and Lord of Heaven. |
| 남천마후 | 적천강 | hostile_demon_empress_to_legendary_martial_master | Fire King Jeok / you | flattering and mocking | Addresses Jeok Cheongang as the Fire King while praising Lord of Heaven. |
| 매종학 | 적천강 | long-standing martial rival and friend | Great Hero Jeok | casual and familiar | Mae addresses Jeok as 적 대협 while discussing the Alliance Leader position. |
| 적천강 | 매종학 | long-standing martial rival and friend | you | blunt and familiar | Jeok addresses Mae as 당신 while recalling their meeting at Mount Jiuhua. |
| 야율목 | 백상 | nephew_to_father's_sworn_younger_brother | Uncle Baeksang | ceremonial and deferential | Yayul Mok formally greets Baeksang as he arrives at the stone door. |
| 백상 | 야율목 | father's_sworn_brother_to_nephew | you | cold and formal | Baeksang questions Yayul Mok about his return, the pasture fire, and the Palace Lord's whereabouts. |
| 야수묘왕 | 백상 | sworn_older_brother_to_sworn_younger_brother | Baeksang | familiar and bittersweet | Yayul Cheok offers Baeksang his preferred fruit wine and asks why he came. |
| 요희 | 흑웅 | Yao great chieftain to Yi great chieftain | big brother | seductive and falsely affectionate | Uses 오라버니 to flatter and manipulate Heugung. |
| 흑웅 | 요희 | Yi great chieftain to Yao great chieftain | my dear | adoring and deferential | Responds to Yohi's manipulation with open infatuation. |
| 백상 | 요희 | Bai great chieftain to Yao great chieftain | Yohi | cold and formal | Calls to Yohi from outside the tent at the chapter's end. |
| 야율목 | 야수묘왕 | son_to_father | Father | formal and deferential | Yayul Mok calls out to the Beast Miao King after the rescue party arrives. |
| 흑웅 | 백상 | younger_great_chieftain_to_senior_great_chieftain | Uncle Baek | deferential and nervous | Heugung addresses Baeksang as 백 숙부 after being confronted by his icy stare. |
| 백상 | 야수묘왕 | Nanman great chieftain to the Nanman Beast Palace Lord | Palace Lord | restrained and apologetic | Apologizes for causing the disturbance after the Beast Miao King stops the fight. |
| 백상 | 남천마후 | Nanman Great Chieftain to hostile demon empress | Southern Heaven Demon Empress | formal and shocked | Baeksang directly identifies the woman who appears before him. |
| 남천마후 | 백상 | Dark Heaven controller to coerced Nanman leader | Great Chieftain Baeksang / Palace Lord | playful, taunting, and threatening | She repeatedly addresses Baeksang while mocking his grief, acknowledging his effort, and issuing her order. |

## Listed compact profiles

### Baeksang.md

# Baeksang (백상)

- **Safe through:** Chapter 675
- **Aliases:** None
- **Role:** Baeksang is the temporary Palace Lord of the Nanman Beast Palace, an over-seventy Great Chieftain of the Bai people, and the leader of Nanman's general mobilization, with nearly ten thousand troops stationed in the Inner Palace.
- **Personality:** Cold, rigid, meticulous, politically resolute, and strategically manipulative, with enduring grief over Hwi's death and a guarded but still powerful bond with his sworn elder brother that now leaves him visibly conflicted.
- **Voice:** Rigid, formal, restrained, and emotionally distant.
- **Relationships:** Baeksang is Yayul Cheok's sworn younger brother and childhood companion, Yayul Mok's sworn uncle, and the father of his deceased only child Baekhwi, whom the Great Snow Fiend killed during the Great Faction War; despite his bond with Yayul Cheok, he has chosen to oppose the Beast Miao King's escape and has surrounded Wonhu's remaining force with Bai warriors.

### Beast Miao King.md

# Beast Miao King (야수묘왕)

- **Safe through:** Chapter 675
- **Aliases:** None
- **Role:** The Beast Miao King is the Palace Lord of the Nanman Beast Palace, the great chieftain of the Miao people, a master among the Ten Kings, and one of only two Supreme Peak masters in Nanman.
- **Personality:** The Beast Miao King is fierce and vigilant, yet pragmatic and willing to sacrifice his position to protect Nanman's survival and the greater cause over personal revenge.
- **Voice:** Low, growling, and forceful.
- **Relationships:** He commands the Nanman Beast Palace, is Baeksang's sworn elder brother and childhood companion, and is Yayul Mok's father while jointly risking their positions to rescue Jin Taekyung and prevent war with the Central Plains.

### Blood Lord.md

# Blood Lord (혈주)

- **Safe through:** Chapter 665
- **Aliases:** None
- **Role:** Young-seeming high-ranking Dark Heaven figure who seeks Jin Taekyung, Cheongpung, and Jeok Cheongang after escaping the confrontation at Mount Song.
- **Personality:** Calm, confident, theatrically frivolous, casually cruel, and ruthlessly destructive; treats allies as disposable tools and enjoys provoking stronger opponents.
- **Voice:** Light, cheerful, and joking even while threatening or killing; turns cold and contemptuous when challenged.
- **Relationships:** He serves the Lord of Heaven alongside the Western Heaven Demon Lord, has received the Lord of Heaven's power for the coming Great War, and still seeks to kill Cheongpung, Jeok Cheongang, and Jin Taekyung.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 674
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Heugung.md

# Heugung (흑웅)

- **Safe through:** Chapter 675
- **Aliases:** None
- **Role:** Heugung is the middle-aged great chieftain of the Yi people, one of Nanman's four great tribes.
- **Personality:** Heugung presents as foolish and easily flattered in public but is capable of concealed planning, disguise, and covert contact.
- **Voice:** Heugung speaks with warm enthusiasm and genuine, openly devoted affection toward Yohi.
- **Relationships:** Heugung genuinely loves Yohi and had promised to cooperate with Jin Taekyung; he disappeared alongside Yohi after the assault on the Fire Dragon Pavilion, and his death remains unconfirmed after a severed wrist believed to be his was found at her estate.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 672
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm, and the occupant of the chief seat of the Murim Alliance's Five Kings Hall.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Mae Jonghak.md

# Mae Jonghak (매종학)

- **Safe through:** Chapter 662
- **Aliases:** Sword Saint
- **Role:** Sword Saint and Cheongpung's grandfather who now serves as the New Murim Alliance's Alliance Leader and has ordered Jin Taekyung's first Fire Dragon Pavilion mission to Nanman.
- **Personality:** Playful, easygoing, and teasing, but capable of handling heavy administrative responsibilities efficiently.
- **Voice:** Friendly, casually familiar, and cheerfully teasing, including when greeting old acquaintances and discussing leadership.
- **Relationships:** Cheongpung's grandfather and martial instructor; taught him the Taeeul Miri Palm; secretly entered Huashan while its Sect Leader slept, left a dagger and handwritten note, and then went into hiding, prompting Huashan's search; fought Jeok Cheongang at Mount Jiuhua more than forty years ago and left after their draw; his old friend Hong Dao left him a letter identifying Jin Taekyung as the Morning Star who would drive away darkness.

### Muyaho.md

# Muyaho (무야호)

- **Safe through:** Chapter 675
- **Aliases:** White Tiger
- **Role:** Muyaho is Yayul Mok's enormous white tiger companion and a renowned Nanman spiritual creature.
- **Personality:** Muyaho is intelligent enough to understand speech, wary of threats, and strongly food-motivated.
- **Voice:** Muyaho communicates through growls, roars, and gestures rather than human speech.
- **Relationships:** Muyaho is Yayul Mok's cherished companion and currently carries Jin while aiding his escape.

### Western Heaven Demon Lord.md

# Western Heaven Demon Lord (서천마군)

- **Safe through:** Chapter 665
- **Aliases:** None
- **Role:** Former Protector of the Divine Cult who commands Dark Heaven's assault on the Sichuan Tang Clan, lost the Myriad-Poison Ring to Jin Taekyung, suffered a crushed ankle and a torn wrist, and was temporarily possessed by the Lord of Heaven before the borrowed body was destroyed.
- **Personality:** Cold, detached, patient, and utterly ruthless toward those he interrogates or hunts.
- **Voice:** Controlled and dispassionate, with concise statements delivered in a quiet, threatening tone.
- **Relationships:** Tang Taesang and the Heaven-Shaking Venerable Nun were his latest victims, he lost one arm taking their lives, and the Qilian Three Fiends now submit to him alongside his hundreds of black-robed hunters.

### Yayul Mok.md

# Yayul Mok (야율목)

- **Safe through:** Chapter 672
- **Aliases:** None
- **Role:** Yayul Mok is the non-Han Young Palace Lord of the Nanman Beast Palace, a spear-wielding warrior who rides a white tiger and speaks Han Chinese haltingly but capably.
- **Personality:** Protective of Nanman Beast Palace livestock, quick-tempered toward trespassers, and capable of restraint once he recognizes legitimate authority.
- **Voice:** Blunt, commanding, and formal-polite toward strangers, becoming openly insulting when provoked.
- **Relationships:** Yayul Cheok is the Beast Miao King and his father, Baeksang is his father's sworn younger brother, and Yayul Mok has risked his position and life to rescue Jin Taekyung, entrusting Muyaho to Jin while he remains behind with the Seven Miao Tigers.

### Yohi.md

# Yohi (요희)

- **Safe through:** Chapter 675
- **Aliases:** None
- **Role:** Yohi is the female great chieftain of the Yao people, one of Nanman's four great tribes.
- **Personality:** Yohi's public presence is charismatic and captivating, drawing widespread admiration and affection.
- **Voice:** Not established.
- **Relationships:** Yohi leads the Yao people, seeks to unite Nanman's four great tribes under Yao leadership, manipulates Heugung alongside Baeksang, and has disappeared from the Inner Palace alongside Heugung after the assault on the Fire Dragon Pavilion.

## Korean source

```text
＃676화



화염신장으로부터 시작된 화염은, 애뇌산의 초입에서 시작되어 삽시간에 사방으로 번졌다.

화륵. 콰아아아!

불교에서 말하는 초열지옥(焦熱地獄)이 있다면 이런 광경이 아닐까 싶다.

쉴 새 없이 흩날리는 잿가루와 매캐한 연기. 그리고 파도처럼 넘실거리며 모든 것을 집어삼키는 화마(火魔).

투둑, 구구구궁!

줄지어 쓰러지는 거목에 지축이 흔들리고 산새들이 일제히 날아오른다.

산림 보호 협회 명예 회장인 적천강이 봤다면 눈을 까뒤집을 만한 광경이었지만, 다행히도 인근에 눈에 띄는 짐승들이 없는 것으로 보아 동물 보호 협회까지 더해질 일은 없을 것 같았다.

‘야생동물이라 그런지 눈치가 빠르네. 벌써 다 도망친건가?’

사실 지금은 어떻게 되어도 상관없다.

굳이 불쌍한 노루 일가족의 터전과 목숨을 빼앗고 싶지는 않지만, 그보다는 암천의 흉계를 저지하는 것과 다른 이들의 목숨이 더 중요하니까.

‘만약 내가 느낀 불길함이 사실이라면…….’

더 이상 머뭇거릴 여유 따위는 없다.

신속하게 달려가던 나는 십여 장 앞을 가로막은 화염의 벽을 확인하고 허공을 향해 손을 뻗었다.

‘인벤토리 오픈. 소환.’

요서부에서 투항할 당시에 백염(白炎)을 꺼내지 않았던 건 옳은 선택이었다.

압수당했다면 가장 중요한 지금 같은 순간에 사용할 수 없었을 테니까.

슥.

손아귀를 가득 채우는 서늘한 감촉. 투명하리만치 새하얀 창날에 사방에서 일렁이는 불꽃이 비친다.

‘지금.’

이미 사방이 불바다로 변해 가는 지금, 열양지기를 실어 쏘아 보내는 멍청한 짓 따위는 하지 않았다.

지금 내게 필요한 것은 강한 힘과 속도. 더불어 간결하면서도 완벽한 동작과 흐름뿐이다.

쉭!

짧은 파공성과 함께, 비스듬히 내리그은 창날의 끝에서 뛰쳐나간 광풍(狂風)이 화염을 찢어발겼다.

화륵, 퍼어어엉!

폭발음과 함께 열린 길.

새하얀 터럭 위로 바짝 엎드린 나는, 불길에 가로막혀 잠시 주춤하고 있던 무야호의 귓가에 속삭였다.

“가자.”

- 크릉.

낮은 울음소리로 대답을 대신한 백호가 빛살처럼 신형을 날렸다.

파도처럼 넘실거리는 화염이 그런 우리의 뒤를 바짝 추격했지만, 이런 혼란 속에서도 녀석은 자신의 목적지를 정확히 알고 있었다.

파파파팟!

빠르게 스쳐 지나가는 풍경. 하늘 높이 뜬 달은 구름에 가려져 있고, 그 아래에서 불길을 등진 채 쉼 없이 나아가던 나는 왠지 모를 익숙함에 중얼거렸다.

“설마…….”

그리고 다음 순간, 뇌리를 스친 어떤 생각에 나는 문득 입을 다물었다.

아니, 어쩌면 설마가 아닐 것이다.

분명 낯설어야 할 이 길과 주위 풍경이 익숙하게 느껴진다는 것은, 단 한 가지 사실만을 의미하니까.

‘독혈지(毒血地).’

과거 남만 전체를 공포로 몰아넣었던 오독문의 멸문 이후, 남만의 금지(禁地)로 불리게 된 애뇌산.

그리고 애뇌산에서도 가장 깊고 은밀한 곳에 위치한 독혈지.

만일 내 짐작이 맞다면…… 우리는 지금 바로 그 독혈지로 향하고 있다. 어쩌면 남만에서 가장 위험할지도 모르는 그 장소로.

‘하지만 지금쯤 그곳은 적지 않은 병력들이 지키고 있을 텐데.’

남만야수궁은 어중이떠중이만 모여 있는 촌구석 문파가 아니다.

극히 드문 독물인 천년지주가 다섯 마리씩이나 나타나고, 오랜 시간 동안 그 누구도 발견하지 못했던 독혈지가 모습을 드러내자 남만야수궁은 적지 않은 숫자의 병력을 파견했다.

혹시 남아 있을지도 모를 오독문의 잔재와 위험을 뿌리 뽑기 위함이었다.

‘아무리 등하불명(燈下不明)을 노렸다고는 해도, 그런 곳으로 숨어들었다고?’

그리고 내가 떠올린 의문이 해결되기까지는, 그리 오랜 시간이 걸리지 않았다.

- 크르르…….

어느 순간 서서히 느려지는 발걸음.

무언가를 느끼고 이빨을 드러낸 무야호의 모습에 나는 일이 생겼음을 직감했고, 이내 매캐한 연기 사이로 스며드는 비릿한 냄새가 인간의 혈향(血香)이라는 것을 깨달았다.

‘그래. 그렇단 말이지.’

내심 중얼거린 나는 독혈지의 입구를 바라보았다. 거대한 괴수의 아가리처럼 벌려져 있는 그곳은, 처음 왔던 그때처럼 알 수 없는 위험으로 가득해 보였다.

아니, 어쩌면 그때 이상으로.

‘하긴, 쉬웠으면 초절정 등급 퀘스트가 아니지.’

어쩐지 일이 생각보다 쉽게 풀린다 싶었다. 하지만 백상과는 다른 의미로, 지금의 나는 돌아가기에는 너무 멀리 왔다.

당장 눈앞의 위험을 피해 간다면, 그 뒤에는 더 큰 위험이 들이닥칠 것이다.

지금 이 순간조차 산림을 휩쓸며 다가오는 등 뒤의 화염처럼.

스윽.

무야호의 등에서 내린 나는, 평소 녀석이 좋아하던 턱밑을 살살 긁어 주며 말을 건넸다.

“아무래도 우리가 함께하는 건 여기까지인 모양이다. 지난번과 다른 건, 이번에는 돌아오지 않아도 된다는 거야.”

- 크릉?

“더 늦기 전에 돌아가. 너라면 불길을 뚫고 빠져나갈 수 있을 거다.”

- 크르릉…….

무야호는 작은 울음소리와 함께 내 눈을 물끄러미 바라보았다.

나는 이 영민한 백호의 청백색의 눈동자에 떠오른 갈등과 두려움을 느낄 수 있었다.

뛰어난 본능을 지닌 존재답게, 녀석도 이미 짐작하고 있는 듯했다.

들어가기는 쉬워도 나가는 것은 어렵다는 걸.

어쩌면 두 번 다시 야율목을 보지 못할 수도 있다는 걸.

그럼에도 지난번처럼 쉽게 발길을 돌리지 못하는 것은, 그간 나름대로 우리 사이에 정이 쌓였기 때문일 것이다.

“나도 죽으러 가는 거 아니다. 그러니 걱정하지 말고 먼저 떠나. 네 주인이 기다리고 있을 테니.”

안심시키는 말과 함께 부드럽게 목덜미를 쓸어 주자, 그제야 천천히 고개를 끄덕인 무야호가 잠시 멈춰 있던 신형을 날렸다.

- 크아아앙!

쉬이익!

아직 불길이 미치지 않은 언덕이 아닌, 독혈지의 입구를 향해서.

“야! 야 인마!”

당황 섞인 외침을 토해 냈지만 이미 붙잡기에는 늦은 상황.

이 예기치 못한 일에 잠깐 몸이 굳은 그때, 우렁찬 포효와 함께 희뿌연 독무(毒霧) 사이로 닥돌했던 백호가 비틀비틀 걸어 나왔다.

- 크륵. 쿨럭.

“……피독주 줄까?”

멈칫하며 내 시선을 피한 백호가, 슬그머니 고개를 끄덕였다.



* * *



무야호는 내가 생각했던 것 이상으로 독혈지에 빠르게 적응했다.

피독주를 물다 못해 꿀꺽 삼켜 버린 녀석은 기민한 반사신경으로 곳곳에서 밀려오는 독물들을 처리했고, 경신법 좀 익혔다는 절정 고수들도 주저할 만큼 큰 폭을 가진 늪을 단 한 번의 도약으로 뛰어넘었다.

그러나 점점 더 깊숙한 곳으로 향할수록, 녀석의 움직임과 호흡 역시 조심스러워졌다.

솨아아아.

독혈지 내부를 잠식한 독무로 인해 쉽사리 분간할 수 없는 시야. 알 수 없는 무언가가 풀을 스치는 소리와 물 떨어지는 소리만 드문드문 들려올 뿐, 사방은 소름이 끼칠 만큼 적막했다.

‘지난번에 야수묘왕과 함께 왔을 때도 이 정도는 아니었는데.’

입구에서 혈향을 맡았을 때부터 느꼈지만, 이건 결코 좋은 징조가 아니다.

아마도…… 아니, 상당히 높은 확률로 며칠 전 남만야수궁이 독혈지에 파견한 이들은 이미 이 세상 사람이 아닐지도 모르겠다는 생각이 문득 뇌리를 스쳤다.

‘만약 그렇다면, 분명 그놈 짓이겠지.’

이름과 별호도, 얼굴도 드러나지 않은 초절정 고수.

촌각도 걸리지 않은 짧은 시간 동안 요서부를 피로 물들이고 흑웅과 요희를 납치해 간 그놈이라면 충분히 벌일 수 있는 일이다.

어쩌면 놈이 아니라, ‘놈들’일 가능성도 농후했다.

암천(暗天).

마교의 뒤를 이어 등장한 놈들의 전력은, 지금까지 드러난 것만으로도 무시무시한 수준이다.

특히 내가 직접 부딪혀 보기까지 한 혈주와 서천마군의 무위는…… 시스템을 바탕삼아 수많은 단련과 사선을 넘나드는 전투로 급성장한 지금의 나조차 감히 승리를 장담할 수 없을 정도다.

‘비록 겪어 본 적은 없지만, 남천마후 역시 놈들과 비교해도 떨어지지 않을 만한 실력자일 테고.’

그렇기에 홀로 적지로 향하고 있는 나로서는 더욱 긴장될 수밖에 없었다.

혈주와 맞닥트렸을 때는 검성(劍星) 매종학이 있었고, 그 어느 때보다 죽음에 가까웠던 서천마군과의 결전에서는 적천강의 도움이 있었으니까.

‘하지만 이곳에 남천마후가 있다면…….’

내가 살아서 동료들을, 가족들을 다시 만날 수 있을까.

툭.

그리고 인지하지도 못한 사이에 맺힌 식은땀 한 방울이, 목덜미를 타고 미끄러지던 바로 그 순간이었다.

할짝.

쓰라릴 만큼 까슬까슬한 감촉.

혓바닥으로 목덜미를 핥아 준 백호가 천연덕스럽게 모른 척하는 모습을 보니, 나도 모르게 피식 실소가 흘러나왔다.

“긴장하지 말라고?”

- 그르릉.

별것 아닌 일이지만 이상하게 마음이 편안해진다.

생각해 보면 지금까지 죽을 위기를 수두룩하게 겪었는데, 여기까지 와 놓고 새삼 식은땀을 흘리다니.

이렇게 긴장했다간 오히려 몸이 굳어 제대로 싸우기조차 힘들다.

‘그래, 시발. 어차피 한두 번이냐.’

열화문의 계승자이자 화왕의 후인이 갖춰야 할 필수 덕목, 노빠꾸 정신을 몸과 마음에 되새긴 나는 독무를 향해 일장(一掌)을 뻗었다.

퍼엉!

적막함을 깨트리는 파공성.

독과는 극상성인 열양지기. 그중에서도 강맹하기 이루 말할 수 없는 화염신장(火焰神掌)의 열기가 뻗어 나가자, 짙은 독무가 산산이 부서져 흩어지고 어두웠던 독혈지가 붉게 물든다.

스스스슥!

황급히 빛과 열기를 피해 움직이는 희한한 형태의 독물들.

마침내 환하게 드러난 미로처럼 얽힌 길을 노려보던 나는, 공력을 실어 포효하듯 내질렀다.

“나와! 이 개새끼들아!”

- 크아아아앙!



* * *



도대체 어떻게 된 일일까.

어느 순간, 불현듯 정신을 차린 요희(妖姬)는 한 치 앞도 분간할 수 없는 어둠 속에서 눈을 깜빡였다.

“아.”

언제나 고혹적이던 목소리는 반쯤 쉬어 있었고, 오랫동안 움직이지 않았던 탓인지 전신 곳곳이 욱신거렸다.

그리고 그제야 서서히 떠오르기 시작하는 기억의 파편들.

“……!”

자신도 모르게 심장이 덜컥 내려앉고, 잠시 풀어졌던 몸이 다시 석상처럼 굳었다.

말없이 파르르 떨리는 요희의 눈동자에는 믿을 수 없는 기억들이 스쳐 지나가고 있었다.

비명. 시체. 피.

그리고 그 모든 것을 만들어 낸 한 사람의 얼굴.

요희가 반사적으로 비명을 내지르려던 그때, 어둠 속에서 한껏 숨죽인 목소리가 들려왔다.

“진정하시오, 요희.”

“흡……!”

“놀랄 것 없소. 나요, 나.”

간신히 비명을 삼킨 요희는 두방망이질 치는 가슴을 진정시켰다.

서서히 어둠에 익숙해진 그녀의 눈동자에 익숙한 인영이 잡혔다.

“흐, 흑웅? 정말 흑웅 오라버니예요?”

“맞소. 기억나지 않으시오?”

기억이 순차적으로 돌아오는 데에는 약간의 시간이 걸렸다.

요희는 ‘그’에게 마지막까지 저항하던 흑웅의 모습을 떠올리며 중얼거렸다.

“저도 모르게 잠시 잊고 있었어요. 그런데 말투가 왜 평소랑…….”

그리 멀리 떨어지지 않은 어둠 속, 요희가 깨어나는 것을 기다리고 있던 흑웅이 쓴웃음을 머금었다.

“여러 가지 사정이 있었소. 그대에게도 쉽사리 말할 수 없었던 사정이.”

정중한 어조와 말투.

요희는 언제나 헤실헤실 웃으며 누이라 부르던 흑웅의 이와 같은 모습이 낯설게 느껴졌지만, 지금 당장은 그게 중요한 것이 아니었다.

“이곳은 어디죠? 그, 그자는 어디 있고요?”

“나도 모르오. 눈을 떠 보니 이곳이더군.”

쇠사슬로 결박된 몸과 옴짝달싹도 하지 않는 공력.

요희가 절망에 빠진 눈으로 사방을 더듬던 바로 그때. 둔중한 소음과 함께 희미한 빛이 쏟아졌다.
```

## Final English reading copy

```markdown
# Chapter 676

The flames born from Flame Divine Palm began at the entrance of Ailao Mountain and spread in every direction in the blink of an eye.

*Fwoosh. Roooar!*

If the Scorching Hell described in Buddhism existed, I imagined it would look something like this.

Ash drifted endlessly through the air, mixing with acrid smoke. A fire demon rolled like a wave, devouring everything in its path.

*Crack. Rumble!*

The earth shook as massive trees toppled one after another, and every mountain bird took flight at once.

It was the sort of sight that would have made Jeok Cheongang, honorary chairman of the Forest Protection Association, roll his eyes back in horror. Fortunately, there didn’t seem to be any noticeable beasts nearby, so it looked like the Animal Protection Association wouldn’t be getting involved too.

*They’re wild animals, so I guess they’re quick on the uptake. Did they all run away already?*

Honestly, I didn’t care what happened now.

I had no desire to take away the home and lives of some poor family of muntjacs, but stopping Dark Heaven’s sinister scheme and saving everyone else’s lives mattered more.

*If the ominous feeling I sensed is real…*

I no longer had the luxury of hesitating.

As I ran forward at full speed, I spotted a wall of flame blocking the path roughly forty yards ahead and reached toward the air.

*Open Inventory. Summon.*

It had been the right choice not to take White Flame out when I surrendered at the Western Yao Estate.

If it had been confiscated, I wouldn’t have been able to use it at the most important moment like this.

*Shing.*

A cool sensation filled my hand. Flames flickering in every direction were reflected across the spearhead, which was white enough to appear transparent.

*Now.*

With the entire area already turning into a sea of fire, I didn’t do something stupid like infuse the spear with Scorching Yang Qi and fire it away.

What I needed now was power and speed. Along with simple yet perfect movements and flow.

*Whoosh!*

With a sharp whistle, a violent gust burst from the tip of my diagonally slashed spear and tore the flames apart.

*Fwoosh! Boom!*

A path opened amid the explosion.

I lay flat against the white fur and whispered beside Muyaho’s ear, who had briefly hesitated in front of the flames.

“Let’s go.”

- *Grrr.*

The White Tiger answered with a low growl and shot forward like a beam of light.

The flames rolling like waves pursued us close behind, but even amid the chaos, Muyaho knew exactly where it was going.

*Papat!*

The scenery flashed past at incredible speed. The moon hanging high in the sky was hidden behind clouds, and as I continued forward without pause with the fire at my back, I muttered at the strange familiarity I felt.

“Don’t tell me…”

The next moment, a thought flashed through my mind, and I abruptly closed my mouth.

No. Maybe it wasn’t a matter of *don’t tell me* at all.

The fact that this path and the surrounding scenery, which should have been unfamiliar, felt so familiar could mean only one thing.

*The Poisonblood Grounds.*

Ailao Mountain had become known as one of Nanman’s forbidden lands after the destruction of the Five Poisons Sect, which had once plunged all of Nanman into terror.

And the Poisonblood Grounds lay in the deepest, most secluded part of Ailao Mountain.

If my guess was right, we were heading straight there. To a place that might be the most dangerous in all of Nanman.

*But by now, a considerable number of troops should be guarding it.*

The Nanman Beast Palace wasn’t some backwater sect filled with assorted riffraff.

When as many as five extremely rare Thousand-Year Spiders appeared and the Poisonblood Grounds, which no one had discovered for so long, revealed itself, the Nanman Beast Palace dispatched a sizable force.

They had intended to root out any remnants of the Five Poisons Sect and any dangers that might still remain.

*Even if they were counting on hiding right under their noses, did they really crawl into a place like that?*

It didn’t take long for the question in my mind to be answered.

- *Grrrr…*

At some point, Muyaho’s steps gradually slowed.

The White Tiger bared its teeth, having sensed something, and I immediately realized that something had happened. Soon after, I realized that the metallic smell seeping through the acrid smoke was the scent of human blood.

*I see. So that’s how it is.*

Muttering inwardly, I looked toward the entrance to the Poisonblood Grounds.

It yawned open like the mouth of a gigantic monster, seemingly filled with unknown dangers just as it had been when I first came here.

No. Maybe it was even worse than before.

*Well, if it were easy, it wouldn’t be a Supreme Peak-grade Quest.*

I had started to think things were going more smoothly than expected. But unlike Baeksang, I had come too far to turn back, though for a different reason.

If I avoided the danger directly in front of me, an even greater danger would come rushing in behind me.

Just like the flames sweeping through the forest and closing in behind me at this very moment.

*Rustle.*

I climbed down from Muyaho’s back and gently scratched beneath its chin, the spot it usually liked, as I spoke.

“It looks like this is where we part ways. The difference from last time is that this time, you don’t have to come back.”

- *Grrr?*

“Go back before it gets any later. You can break through the flames and escape. I know you can.”

- *Grrrr…*

Muyaho gazed at me silently with a small whimper.

I could sense the conflict and fear reflected in the blue-white eyes of the intelligent White Tiger.

As befitted a creature with extraordinary instincts, it seemed to have already guessed.

That entering would be easy, but getting out would be difficult.

That it might never see Yayul Mok again.

Even so, it couldn’t turn away as easily as it had last time, probably because a certain bond had formed between us in the time since.

“I’m not going there to die. So don’t worry and leave first. Your master will be waiting for you.”

As I reassured it and gently stroked the back of its neck, Muyaho finally nodded slowly and launched itself forward after a brief pause.

- *GRAAAWR!*

*Whoosh!*

Not toward the hill the flames had yet to reach, but toward the entrance to the Poisonblood Grounds.

“Hey! Hey, you idiot!”

I shouted in surprise, but it was already too late to catch it.

For a moment, my body stiffened at the unexpected turn of events. Then, with a mighty roar, the White Tiger that had charged headlong into the pale Poison Mist came staggering back out.

- *Krrk. Cough.*

“…Want a poison-warding pearl?”

The White Tiger hesitated, avoided my gaze, and gave a small nod.

* * *

Muyaho adapted to the Poisonblood Grounds much faster than I had expected.

As if biting down on the poison-warding pearl weren’t enough, it gulped the thing down whole. With nimble reflexes, it dealt with the venomous beasts surging in from every direction and cleared a swamp so wide that even Peak masters who had learned a movement technique would have hesitated to cross it in a single leap.

However, the deeper we went, the more cautious its movements and breathing became.

*Whooosh…*

The Poison Mist that had swallowed the inside of the Poisonblood Grounds made it impossible to see clearly. Only the occasional sound of something unknown brushing against the grass or water dripping reached our ears. Everywhere around us was silent enough to make my skin crawl.

*It wasn’t this bad even when I came here with the Beast Miao King last time.*

I had sensed it from the moment I smelled blood at the entrance, but this was definitely not a good sign.

A thought suddenly crossed my mind.

Perhaps… No, with a fairly high probability, the people the Nanman Beast Palace had dispatched to the Poisonblood Grounds a few days ago were no longer of this world.

*If that’s true, it must be that bastard’s work.*

A Supreme Peak master whose name, sobriquet, and face had never been revealed.

Someone who had dyed the Western Yao Estate in blood and kidnapped Heugung and Yohi in less than a moment could certainly have done this.

It was also highly possible that it wasn’t just one bastard, but *them*.

Dark Heaven.

The strength of those who had appeared after the Demonic Cult was terrifying, even judging only by what they had revealed so far.

In particular, the martial prowess of the Blood Lord and the Western Heaven Demon Lord, whom I had personally faced…

Even I, who had used the System as a foundation to grow rapidly through relentless training and countless life-or-death battles, couldn’t dare guarantee victory against them.

*Though I’ve never faced her myself, the Southern Heaven Demon Empress must be a master whose skill is no less than theirs.*

That was why, as I headed alone into enemy territory, I couldn’t help but be even more tense.

When I had encountered the Blood Lord, Sword Saint Mae Jonghak had been there.

And during my decisive battle with the Western Heaven Demon Lord—the battle that had brought me closer to death than any other—Jeok Cheongang had helped me.

*But if the Southern Heaven Demon Empress is here…*

Would I be able to survive and see my comrades and family again?

*Drip.*

It was at that exact moment, when a bead of cold sweat formed without me even realizing it and slid down the back of my neck.

*Lick.*

The sensation was rough enough to sting.

When the White Tiger licked the back of my neck and pretended nothing had happened, a quiet laugh escaped me.

“Are you telling me not to be nervous?”

- *Grrrr.*

It was a trivial thing, but it strangely put me at ease.

Come to think of it, I had gone through countless brushes with death until now. And yet here I was, breaking into a cold sweat now that I had come this far.

If I stayed this tense, my body would stiffen and I wouldn’t even be able to fight properly.

*Yeah, fuck it. It’s not like this is my first time.*

I reaffirmed in body and mind the no-brakes mentality that was an essential virtue for the successor of the Fire Gate Clan and the heir of the Fire King, then thrust one palm toward the Poison Mist.

*Boom!*

The sharp sound of displaced air shattered the silence.

The heat of Flame Divine Palm, which possessed the Scorching Yang Qi that was the natural enemy of poison—an unimaginably fierce heat—surged forward.

The thick Poison Mist broke apart and scattered, and the dark Poisonblood Grounds turned red.

*Hssssss!*

Strange-shaped venomous beasts hurriedly moved away from the light and heat.

As I glared at the maze of tangled paths that had finally been revealed, I infused my voice with internal energy and roared.

“Come out, you fucking bastards!”

- *GRAAAAAAWR!*

* * *

How had this happened?

At some point, Yohi suddenly came to her senses and blinked in the darkness, unable to see even an inch ahead.

“Ah.”

Her usually alluring voice was half-hoarse, and her entire body ached from having remained motionless for so long.

Only then did fragments of memory gradually begin to rise to the surface.

“……!”

Her heart dropped without her realizing it, and her body, which had relaxed for a moment, stiffened again like a stone statue.

In Yohi’s trembling eyes, memories she couldn’t believe were flashing past.

Screams. Corpses. Blood.

And the face of the one person who had created all of it.

Just as Yohi instinctively tried to scream, a tightly hushed voice came from the darkness.

“Calm yourself, Yohi.”

“Gasp…!”

“There’s nothing to be surprised about. It’s me.”

Yohi barely managed to swallow her scream and calm her pounding heart.

As her eyes slowly adjusted to the darkness, a familiar silhouette came into view.

“Heugung? Is it really you, big brother Heugung?”

“That’s right. Don’t you remember?”

It took a little time for her memories to return in sequence.

Remembering Heugung resisting *him* until the very end, Yohi murmured,

“I must have forgotten for a moment without realizing it. But why are you speaking so differently from usual…?”

In the darkness not far away, Heugung had been waiting for her to wake up. He gave a bitter smile.

“There were various circumstances. Circumstances I couldn’t easily tell even you.”

His tone and manner of speaking were respectful.

Yohi found this side of Heugung—who usually wore a goofy grin and called her “my dear”—strange, but that wasn’t what mattered right now.

“Where are we? Wh-where is that man?”

“I don’t know either. I opened my eyes and found myself here.”

Her body was bound in iron chains, and her internal energy would not move at all.

Just as Yohi searched her surroundings with despairing eyes, a dull noise sounded and faint light poured in.
```

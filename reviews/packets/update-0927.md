<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0927.txt",
      "sha256": "114788b363dc9597ae56a3ef0a221ad7ee7e6b6366a79eb7435d8284cee66675",
      "bytes": 12792
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "7ffe7291470febc1e9d24c5aa238fc0a0b4fea225b1a863036f1f1eb869539a1",
      "bytes": 1140
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "0666305ef3a14502bbfe5c72134a55888b76af6f3fad7264eaf0463c809292b0",
      "bytes": 231946
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "65012df9eb18cc3a77058167fe8412a7c91e89505d9e21aaba57e42675eb83bb",
      "bytes": 1325
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "33f272f13c6a017d4d29f5a03c3185c74c8d94f437a05aff84531e4a03b946a8",
      "bytes": 759
    },
    {
      "path": "characters/Eastern Heaven Demon Lord.md",
      "sha256": "a6d73a78da728fcd7b6efc3e9dd35695a440edd41c6916b22fc386b95e57074e",
      "bytes": 838
    },
    {
      "path": "characters/Hong Jin.md",
      "sha256": "2b59296bcd0ed27821978daf9c8a3f70f0013611590f028e9197443c3a697455",
      "bytes": 837
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "b9cd2e3c8823776688e17dc040272dd240c9a888e77c9a410340228493708bed",
      "bytes": 1244
    },
    {
      "path": "characters/Jin Mukyung.md",
      "sha256": "f4460239d5a8481f51bbc2b4eb528a1368865e9f350f36dde9204a00bf4726c1",
      "bytes": 1497
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "4207facd14689ed40af0650e37cac994e1d9bce748b17014e59ce81efc944899",
      "bytes": 1290
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "3960f5650aec7465c98be960af4d61cf996dff62886de24f641e770aaa08579a",
      "bytes": 622
    },
    {
      "path": "characters/Ma Sanbao.md",
      "sha256": "4b31308d490391580308257d5aad1fb753bef5d284d0f02f453ddc97e1a0fd73",
      "bytes": 850
    },
    {
      "path": "characters/Martial God.md",
      "sha256": "9c178b1306846a29f51d244690e9ce703a636e95d0d19fbabbc8cdec67638f0e",
      "bytes": 752
    },
    {
      "path": "characters/Prince Shangshan.md",
      "sha256": "80329a602140dde7cdd9a27c90c3dc7fe6007c1454c4c4d5ffc362fbba083010",
      "bytes": 1042
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "f4cb7597df6e2e3b6621149821277f1cbaab9bc9cf705d626aaacff9cc908122",
      "bytes": 266209
    }
  ],
  "estimated_tokens": 13214
}
-->

# Durable State Update — Chapter 927

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
1 and safe_through 927. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 927. Profile updates may replace only one
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
  "chapter": 927,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 927,
    "continuity_sources": [927],
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
    "Zhu Bao is Crown Prince; the Emperor is his older brother and supports his compassionate vision of rulership.",
    "The Emperor has ordered a purge of treason suspects while promising to spare the innocent after their connections are established.",
    "The Bow Saint says Taekyung is the chosen one mentioned by the Martial God, yet is in an irrecoverable state despite supposedly having powers to escape death."
  ],
  "continuity_sources": [
    925,
    926
  ],
  "open_questions": [
    "Why is Taekyung in an irrecoverable state, and what powers was he supposed to possess as the Martial God’s chosen one?",
    "What story has So Gyo kept to herself?",
    "Where is Ma Sanbao, and what is his current status?",
    "What did Wei Zhong tell Taekyung through Sound Transmission?",
    "Will the Salcheonmun pursue Mungyeong or discover that Taekyung killed Gye Yabu?"
  ],
  "safe_through": 926,
  "temporary_decisions": [
    "Keep “Force” for 강기 distinct from “death energy” for 사기.",
    "Render 황태제 as “Crown Prince” in this succession context."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 진무경    | **Jin Mukyung**    |
| 적천강    | **Jeok Cheongang** |
| 청풍     | **Cheongpung**     |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 검성     | **Sword Saint**               | Mae Jonghak    |
| 무신     | **Martial God**               | —              |
| 궁성     | **Bow Saint**                 | —              |
| 일신     | **One God**         |
| 삼성     | **Three Saints**    |
| 태원진가   | **Jin Family of Taiyuan**        |
| 암천     | **Dark Heaven**                  |
| 천무학관   | **Heaven's Gate Temple**         |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 중원     | **Central Plains**                               |                                                       |
| 제자     | **Disciple**                                 |
| 생도     | **cadet**                                    |
| 시스템              | **System**                     |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 사천     | **Sichuan**            |
| 화산     | **Huashan**            |
| 구화산    | **Mount Jiuhua**       |
| 정마대전   | **Great Faction War**         |
| 공자      | **Young Master**                                                |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 동천마군 | **Eastern Heaven Demon Lord** | Title of the absurd masked antagonist in Jin's nightmare. |
| 홍진 | **Hong Jin** | Level 22 man at the City Lord's luncheon; delicate in appearance and voice. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 마삼보 | **Ma Sanbao** | The East Depot’s Brush-Holding Eunuch and second-in-command. |
| 상산왕 | **Prince Shangshan** | The City Lord and a member of the imperial family who orders the luncheon. |
| 이공자 | **Second Young Master** | Title used for Jin Mukyung. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 성주 | **City Lord** | Official who sends the invitation for a gathering with young prodigies. |
| 천자 | **Son of Heaven** | Honorific title for the Emperor. |
| 주표 | **Zhu Bao** | Personal name of Prince Shangshan. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 화산신룡 | **Huashan Divine Dragon** | Title given to Cheongpung after the Star-Array Grand Banquet. |
| 낭중지추 | **needle in a bag** | Idiom meaning exceptional talent eventually reveals itself. |
| 사천성 | **Sichuan Province** | Province form used in the title of its chief official. |
| 사천성주 | **City Lord of Sichuan Province** | Title held by Won Gyun. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 괴력난신 | **supernatural powers** | Term for extraordinary and unnatural powers. |
| 열화신룡 | **Blazing Flame Divine Dragon** | New sobriquet bestowed on Jin Taekyung. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 고든 | **Gordon** | Pentagon employee tasked with repairing smashed warning lights. |
| 제시 | **Jesse** | The U.S. Secretary of State, introduced by first name. |
| 궁인 | **palace attendant** | Former Inner Palace attendant expelled by Baeksang. |
| 화신 | **Fire God** | A local deity worshiped by one Nanman believer. |
| 혈혼고 | **Blood Soul Gu** | Rare gu poison found deep in Nanman. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진무경 | younger_to_older_brother | hyung | casual-but-junior | Retain hyung for 형 in Taekyung's greeting; Mukyung then punishes the casual speech. |
| 진무경 | 진태경 | older_to_younger_brother | youngest | blunt-senior | 막내 / youngest; may taunt that lasting a quarter-hour would make Taekyung the older brother. |
| 청풍 | 진태경 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung repeatedly addresses Taekyung as 은인 after receiving food. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 진태경 | 청풍 | companion_to_young_martial_artist | Young Master Cheongpung | formal-polite | Taekyung uses 청 공자 while correcting Cheongpung's royal-etiquette mistake. |
| 홍진 | 주표 | servant and political aide to prince | His Highness | formal-deferential | Uses the elongated royal call 전하 while summoning Zhu Bao. |
| 진태경 | 주표 | visitor to prince | His Highness, Prince Shangshan | formal-deferential | Addresses Zhu Bao as 상산왕 전하 after kneeling to meet his gaze. |
| 주표 | 진태경 | prince to visiting young hero | Jin Taekyung | formal and inquisitive | Uses the formal second-person address before asking Taekyung's name and requesting an autograph. |
| 홍진 | 진태경 | political_host_to_young_martial_artist | Young Hero Jin; Young Master Jin; Sleeping Dragon of Shanxi | polite, coaxing, and probing | Uses respectful forms while steering Taekyung toward relaying the Escort Bureau proposal and teasing him with the Seongun Escort Bureau. |
| 진태경 | 홍진 | young_martial_artist_to_political_official | Comrade Chairman—no, Deputy Military Commissioner | casual and teasing, then formally corrective | Deliberately jokes with an inappropriate title before correcting himself to Hong Jin's official office. |
| 주표 | 청풍 | prince_to_young_martial_artist | you | formal and gatekeeping | Refuses Cheongpung's autograph until he acquires a martial title. |
| 홍진 | 청풍 | political_official_to_young_martial_artist | Young Master | formal and curious | Uses 공자께서는 while asking whether Cheongpung has always lived on Huashan. |
| 청풍 | 진무경 | young_martial_artist_to_renowned_senior_martial_artist | Young Hero Jin Mukyung | deferential and excited | Cheongpung calls him 진천검 진무경 소협 and later 진 소협 while seeking his duel. |
| 진무경 | 청풍 | senior_martial_artist_to_newly_met_young_martial_artist | Young Hero | deferential and expectant | Mukyung addresses Cheongpung as 소협 while asking whether Great Hero Mae descended from Huashan. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 적천강 | 청풍 | overwhelming_elder_to_young_martial_artist | you / little punk | blunt, amused, and threatening | Jeok Cheongang uses 네, 이놈, and related blunt forms while testing Cheongpung. |
| 청풍 | 적천강 | young_martial_artist_to_overwhelming_elder | Grandpa Jeok | casual-familiar despite deference | Cheongpung uses 적 할아버지 while asking Jeok Cheongang to confirm Taekyung's condition; this is a familial form of address, not literal kinship. |
| 사천성주 | 진태경 | official_to_imperial_messenger | Messenger of His Highness Prince Shangshan | formal-deferential | The City Lord addresses Taekyung deferentially after seeing Prince Shangshan's Token. |
| 진태경 | 사천성주 | visitor_to_city_lord | City Lord | sarcastic-polite | Taekyung jokingly praises him as our City Lord after making him fund the reward. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 주표 | 홍진 | prince to loyal subject | you | formal and reassuring | Zhu Bao refers to Hong Jin as 그대 while apologizing for the hardship he has endured. |
| 홍진 | 마삼보 | Longtime friend and former East Depot cohort | Ma Constable; Eunuch Ma | Familiar and respectful | Hong uses both forms while acknowledging Ma’s former and current standing. |
| 마삼보 | 홍진 | Longtime friend and former East Depot cohort | Hong Constable | Familiar and respectful | Ma addresses Hong by his former East Depot title. |
| 진태경 | 상산왕 | protector addressing a young prince | His Highness | respectful royal address | Taekyung refers to the prince as 상산왕 전하 when ordering Mujin to bring him. |
| 진태경 | 황제 | guest of the Emperor’s younger brother addressing the Emperor | Your Majesty | formal and deferential in address, despite blunt challenges | Taekyung repeatedly addresses the Emperor as 폐하. |
| 상산왕 | 황제 | younger brother addressing the Emperor | Your Majesty | deferential royal address | Shangshan addresses the Emperor as 폐하 while pleading for Taekyung. |
| 마삼보 | 진태경 | political ally recruiting a young martial artist | you; my friend | courteous and familiar | Ma uses 자네 and 이보게 while explaining his choice of Jin and inviting him to join the restoration army. |
| 진태경 | 마삼보 | young martial artist addressing the East Depot’s Brush-Holding Eunuch and prospective ally | you; Brush-Holding Eunuch | polite and direct | Jin asks Ma why he withheld information and presses him for a clear answer; he refers to him as 태감. |
| 황제 | 진태경 | Emperor addressing a subject and Prince Shangshan’s guest | Jin Taekyung | formal and authoritative | The Emperor addresses Taekyung by his family and personal name before asking what to do with the two officials. |
| 적천강 | 동천마군 | enemies | you | blunt and informal | Jeok Cheongang addresses the Eastern Heaven Demon Lord with hostile familiarity. |
| 동천마군 | 적천강 | enemies | you | informal | The Eastern Heaven Demon Lord speaks to Jeok Cheongang during their duel. |
| 마삼보 | 동천마군 | disciple_to_master | Master | deferential | Ma Sanbao addresses the Eastern Heaven Demon Lord as 스승님 when rejoining him. |
| 황제 | 동천마군 | former ruler addressing a former subject, now an enemy | you | measured and formal | The Emperor asks why the Demon Lord betrayed his father, the late Emperor. |
| 동천마군 | 황제 | former subject addressing the Emperor, now an enemy | you; you bastards | hostile and contemptuous | He denies ever being loyal to the imperial family and accuses the rulers of betrayal. |
| 진태경 | 동천마군 | young martial artist confronting an enemy | ugly-ass big bro | casual, profane, and taunting | Jin calls out to the Demon Lord after returning to the hall. |
| 동천마군 | 진태경 | enemy recognizing the spear wielder | Jin Taekyung | shouted, informal | The Demon Lord cries Taekyung's name after identifying him as the spear's owner. |
| 상산왕 | 동천마군 | young imperial prince addressing the enemy who killed his parents and brothers and suffered at the hands of his grandfather | you | formal-polite | He apologizes for his grandfather’s actions using 당신 and deferential speech. |
| 황제 | 주표 | older brother addressing his younger brother and newly appointed Crown Prince | Bao’er | intimate and authoritative | The Emperor uses a warm childhood-style name before commanding Zhu Bao to accept the succession. |
| 주표 | 황제 | younger brother and Crown Prince addressing the Emperor | Your Majesty | formal and deferential | Zhu Bao formally accepts the Emperor’s command. |

## Listed compact profiles

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 889
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, the grandson and Disciple of Sword Saint Mae Jonghak, a Supreme Peak martial master known as the Huashan Divine Dragon, the creator of the snake-inspired Mimi Step footwork technique, and the master of the Azure Dragon Pavilion within the Alliance Leader's Two Dragons Pavilion.
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, a deep love of martial arts, competitive pride, unusual resistance to monster-induced Fear, and discomfort when someone copies his martial arts.
- **Voice:** Dreamy and hazy, with innocent, polite phrasing; he has begun imitating Taekyung's profanity.
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions while Taekyung is his only true martial rival; Tang Sadok has temporarily entrusted Mimi, now a large horned snake, to him, and Cheongpung is accompanying Mungyeong while learning his martial arts through observation to become stronger and adapt to this world.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 926
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Eastern Heaven Demon Lord.md

# Eastern Heaven Demon Lord (동천마군)

- **Safe through:** Chapter 926
- **Aliases:** Wei Zhong
- **Role:** The Eastern Heaven Demon Lord was Wei Zhong, the East Depot’s Seal-Holding Eunuch and a former Maoshan Sect disciple who commanded the dead with a bell; Jin Taekyung killed him with blue-white flames.
- **Personality:** His hatred grew from losing his family and sect, but recognizing his own lonely childhood in Zhu Bao ultimately moved him to relinquish his vengeance and choose a less harmful final act.
- **Voice:** He speaks in measured, almost lyrical phrasing, recounting the past before turning to pointed accusations.
- **Relationships:** Ma Sanbao is his Disciple; he holds the Emperor responsible for Taizu’s actions against the Maoshan Sect.

### Hong Jin.md

# Hong Jin (홍진)

- **Safe through:** Chapter 926
- **Aliases:** None
- **Role:** Hong Jin is a Level 22 Deputy Military Commissioner of Shanxi Province, a eunuch and trusted aide to Prince Shangshan, and a former member of the East Depot.
- **Personality:** Composed, socially deft, and ambitious, Hong Jin became a eunuch to escape poverty and save his family, then used his abilities to pursue a broader life.
- **Voice:** Delicate and deferential, using formal, self-effacing language with Prince Shangshan.
- **Relationships:** Hong Jin is devoted to Prince Shangshan, whom the late Emperor entrusted to his care; the Fourth Prince spared him because of their old ties, and his longtime friend and former East Depot cohort Ma Sanbao stayed behind in the palace.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 926
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; believes there is no absolute justice and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He deeply trusts Jin Taekyung, his publicly acknowledged second Disciple and intended heir; warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, remains Peng Cheolhu's rival, and is the target of an attack by the assassin Heaven's Slaughter.

### Jin Mukyung.md

# Jin Mukyung (진무경)

- **Safe through:** Chapter 533
- **Aliases:** Heaven Shaking Sword; Jin Family Second Young Master
- **Role:** Jin Mukyung is the second son of the Jin Family of Taiyuan, a twenty-three-year-old cadet at Heaven’s Gate Temple, and a young Peak-level genius swordsman who has remained secluded in the training hall for more than a year after losing to Cheongpung and refuses to emerge until he achieves a great accomplishment.
- **Personality:** Reserved, terse, and easily irritated by exaggerated praise; glares coldly when Taekyung identifies him
- **Voice:** Quiet and resonant; clipped and blunt in direct speech
- **Relationships:** Taekyung’s older brother and current martial arts instructor; returned to the Jin Family after several years away; three years earlier, he flatly refused seven-year-old Zhu Bao’s request for an autograph

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 925
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader.
- **Personality:** Hungry, self-aware, dryly observant, and pragmatic under pressure; accepts extreme personal risk when duty and the lives of others demand it.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; So Gyo says he is the chosen one spoken of by the Martial God, while her allegiance remains unknown.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 925
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Ma Sanbao.md

# Ma Sanbao (마삼보)

- **Safe through:** Chapter 920
- **Aliases:** None
- **Role:** Ma Sanbao is the East Depot’s Brush-Holding Eunuch and a Supreme Peak martial artist who secretly led a restoration effort for Prince Shangshan as a disciple of the Eastern Heaven Demon Lord.
- **Personality:** He is vigilant and patient, concealing his loyalties while awaiting the moment to act for the late Emperor.
- **Voice:** He speaks in measured, courteous language and uses calm repetition, feigned agreement, and procedural reminders to steer conversations while keeping sensitive details guarded.
- **Relationships:** Ma Sanbao was a longtime friend and former East Depot cohort of Hong Jin, served the Eastern Heaven Demon Lord, and led a restoration effort for Prince Shangshan.

### Martial God.md

# Martial God (무신)

- **Safe through:** Chapter 926
- **Aliases:** None
- **Role:** An unidentified legendary martial artist regarded as a pinnacle above the Ten Kings; more than fifty years ago, he defeated five Supreme Peak fiends and five hundred Blood Ghost Squad members alone.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** He met the Beast Miao King twice more than fifty years ago, appearing first as a white-bearded elder and later as a young boy; Mae Jonghak received several teachings from him, while his identity, whereabouts, and possible connection to Cheon Taemin remain unknown.

### Prince Shangshan.md

# Prince Shangshan (상산왕)

- **Safe through:** Chapter 926
- **Aliases:** None
- **Role:** Prince Shangshan, whose personal name is Zhu Bao, is the Emperor’s thirteen-year-old younger brother, an exceptionally skilled young swordsman, and the newly appointed Crown Prince.
- **Personality:** Earnest and compassionate, he takes responsibility for others’ suffering and dreams of a peaceful age founded on justice, care for the people, wise counsel, and accountability, even when doing so demands personal sacrifice.
- **Voice:** Archaic and formal in the manner of a historical drama, with openly eager and childlike reactions beneath his royal diction.
- **Relationships:** Zhu Bao is the Emperor’s younger brother and Crown Prince, and Hong Jin has been his steadfast caretaker since childhood. He admires Jin Taekyung and calls him a friend; his compassion for the Eastern Heaven Demon Lord reflects the different path made possible by those who supported him.

## Korean source

```text
＃927화



알 수 없는 전율이 등골을 타고 찌르르 울렸다.

죽음조차 피할 수 있는 괴력난신(怪力亂神)의 힘.

귀신과도 같은 기이한 힘이라고밖에 정의할 수 없는 그것의 실체를, 나는 누구보다 잘 알고 있었으니까.

‘시스템(System).’

밑창이 뚫린 배처럼 서서히 가라앉아 가던 내 인생에 찾아온 행운.

가장 큰 위기인 동시에 기회를 부여해 준 힘.

그러나 무림이라 불리는 이 세상에서 나를 제외하고 시스템의 존재를 알고 있는 것은 단 한 사람뿐이다.

화왕 적천강.

그가 아닌 그 누구도 내가 지닌 힘의 진정한 실체를 알 수 없다.

비단 궁성뿐만이 아니라, 아주 가까이에서 나와 함께한 극소수의 인물들 역시 마찬가지다.

‘어렴풋이 뭔가 있다는 것 정도는 짐작할 수 있어도, 단지 그뿐이겠지.’

쉴 틈 없이 사선(死線)을 넘나들었다.

평범한 누군가였다면 몇 번이나 죽음을 맞이했을 상황에서도 살아남았고, 무림 역사상 유례가 없을 만큼 빠른 속도로 성장했다.

그럼에도 불구하고, 사람들은 내가 가진 힘의 명확한 실체를 모른다.

아니, 내 입으로 직접 진실을 털어놓기 전까지는 알 수 없다.

시스템은 그런 힘이니까.

괴력난신이라는 네 글자로도 전부 담을 수 없는, 사람이라면 감히 짐작조차 할 수 없는 이능(異能)이니까.

‘설령 그 사람이 궁성이라고 해도 예외는 아니지.’

찰나의 순간 느꼈던 충격은 이미 갈무리한 지 오래다.

다만 나 스스로는 도무지 해결할 수 없는 한 가지 의문이 남아있다면, 극소수의 인물만이 알고 있는 내 특별함이 어찌 ‘저들’에게까지 알려졌는지에 대한 것이었다.

‘궁성. 그리고…….’

무신(武神).

오랜 세월 자취를 감추었던 두 거인의 그림자가 지금 이 순간 내 머리 위로 드리워진다.

땀을 적셔 주는 그늘이 아닌, 일종의 어둠처럼.

한편으로는 오싹하리만치.

나는 바싹 마른 입술을 핥았다. 입안은 모래를 한 움큼 씹어 삼킨 것처럼 까끌거렸다.

‘도대체 뭘, 어디까지 알고 있는 거지?’

내가 들리지 않는 물음을 마음속으로 흘려보낸 그때였다.

깊게 가라앉은 눈동자로 내 모습을 물끄러미 응시하던 궁성이 문득 입을 연 것은.

“생각했던 것보다는 침착하구나. 횡설수설 변명이라도 늘어놓을 줄 알았는데. 아니면 모른 척을 하거나.”

나는 애써 담담하게 대꾸했다.

“그러면, 뭐가 달라집니까?”

“없어. 아무것도. 너도 알고 있잖아?”

그 반문을 듣는 순간 확실해졌다.

눈앞의 이 여자. 궁성은, 줄곧 나를 주시해 왔다는 것을.

그리고 내가 생각하는 것 이상으로 많은 사실을 알고 있다는 것을.

‘그렇다면 설마……. 아니, 그럴 리는 없다.’

불현듯 뇌리를 스친 어떤 의문을 지워 내며, 나는 날 선 음성으로 입을 열었다.

“언제부터였습니까.”

“짧은 질문에 여러 의미가 담겨 있는 것 같은데, 글쎄. 이걸 뭐라 대답해 줘야 할지 모르겠으니 오늘 일부터 말해 볼까.”

궁성이 좌우로 늘어선 꽃들을 부드럽게 매만지며 말을 이었다.

“열화신룡 진태경. 분명 죽었어야 할 네가 일어나는 모습을 본 순간 비로소 확신할 수 있었지. 무신께서 말씀하신 선택받은 자가 누구인지.”

“그 사람. 아니, 그분이 어떻게…….”

“어떻게 널 알고 있느냐고?”

나는 동요를 억누르며 고개를 끄덕였다.

전신의 신경이 곤두서는 듯한 기분.

이 대답에 따라 모든 것이 송두리째 뒤바뀌고, 앞으로의 흐름은 뒤틀릴 것이다.

나 자신조차 예측할 수 없는 방향으로.

그리고 다음 순간 울려 퍼진 궁성의 짧은 대답은, 내 사고를 정지시키기에 충분했다.

“그야 모르지.”

“그게, 그게 무슨.”

“나뿐만 아니라 그분도 모르셨을 거야. 당연한 일이지. 내가 그 서신(書信)을 발견한 건 네가 태어나기도 전의 일이었으니까.”

“……서신? 제가 태어나기도 전에?”

“그래. 내가 처음 그 서신을 발견한 건, 정마대전이 종결된 후에도 몇 번이나 강산이 뒤바뀐 어느 날이었지.”

궁성의 침착한 목소리가 새벽 공기에 섞여 귓가로 흘러들었다.

“처음에는 단지 어느 이름 모를 고인(古人)의 흔적이라고 생각했다. 하지만 아니었어. 그 서신은 무신께서 내 앞으로 남긴 것이었으니까.”

“그럼 그 서신에는, 도대체 어떤 내용이 적혀 있던 겁니까.”

“그분께서 준비하신 안배(按排). 아니, 어쩌면 일종의 예언(豫言).”

“……!”

“더불어 그 내용에는 항상 빠지지 않고 등장하는 단어가 있었고.”

갑갑하다. 마치 가슴 한구석에 커다란 돌덩어리가 얹힌 기분이다.

나는 목소리를 쥐어 짜냈다.

“선택받은 자.”

“맞아. 그리고 그 선택받은 자는 비단 어느 한 사람만을 지칭하는 것이 아니었지.”

사박. 사박.

조심스럽게 내디딘 발걸음이 풀잎을 피해 나아간다.

흐릿한 달빛이 정원을 거니는 궁성의 머리 위로 쏟아져 내렸다.

“믿을 수 없었지만, 믿을 수밖에 없었어.”

그분은, 무신이니까.

숨길 수 없는 경외가 담긴 한 마디.

달빛만큼이나 희미한 목소리로 덧붙인 궁성은 발걸음에 맞춰 천천히 말을 이었다.

“그렇게 수십여 년 만에 세상으로 나와 천하를 떠돌았지. 대부분은 중원에 머물렀고, 한때는 서쪽의 끝없는 사막으로, 또 언젠가는 초원을 넘어 이끼와 얼음으로 가득한 북해(北海)로 향하기도 했었다.”

무신의 서신에 적힌 ‘선택받은 자’를 찾는 여정은 모래밭에서 단 하나의 특별한 모래알을 찾아내는 것과 같았고, 궁성은 이 모든 짐을 홀로 짊어져야 했다.

“누구의 도움도 받을 수 없었지. 서신에는 임무를 성공하기 전까지 이에 관련된 사실이 단 하나라도 알려져서는 안 된다고 적혀 있었으니까.”

그러나 궁성은 포기하지 않았다.

흡사 예언과도 같았던 무신의 안배에는, 선택받은 자라 불리는 존재가 반드시 필요했다.

“온 세상이 암흑으로 물들 때, 등불이 되어 길을 밝힐 자. 마침내 새로운 하늘을 열어 아침을 불러올 유일한 사람.”

낮게 읊조린 궁성이 고개를 돌려 하늘을 바라보았다.

“하지만 나이도, 얼굴도, 이름이나 성별조차 모르는 누군가를 찾아 그토록 찾아 헤맸음에도, 선택받은 자는 좀처럼 나타나지 않았지.”

당연한 일이었다.

이 광활한 천하에 살아가는 단 한 사람. 심지어 아직 태어났는지조차 모르는 이를 찾는 것은 불가능에 가까운 일이니까.

“다만 완전한 불가능은 아니었어. 그분께서 서신에 남긴 내용이 사실이라면, 눈부신 속도로 두각을 드러낼 수 있을 테니까.”

낭중지추(囊中之錐).

주머니 속의 송곳은 반드시 튀어나오기 마련이다.

어느 곳에 있더라도, 얼마나 수많은 인파에 파묻혀 있더라도.

“떠도는 소문들을 좇아 선택받은 자라고 생각되는 이들을 찾아갔지만, 천하의 기재들이 모인다는 천무학관(天武學館)에서도 별다른 확신은 얻지 못했지.”

천무학관이라면 태원진가의 이공자이자, 내 둘째 형인 진무경이 잠시 몸담았던 곳이었다.

내로라하는 명문대파의 후예들은 물론, 온갖 재능 넘치는 이들이 넘쳐흐르는 인재의 요람.

그러나 제각각 뛰어난 재능을 지닌 천무학관의 생도들조차 궁성이 생각하는 ‘선택받은 자’의 기준에는 턱없이 부족했다.

“하나같이 출중했으나, 오직 그뿐이었다. 모두 명백한 한계가 있었지. 그들에게도, 그리고 나에게도.”

줄곧 말없이 궁성의 이야기를 듣고 있던 나는 그제야 깨달았다.

무신이라는 두 글자가 가진 거대한 그늘에 가려졌을 뿐, 다른 삼성(三星)들과 같이 자취를 감추었던 그녀가 왜.

무슨 이유로 황궁에 머무르고 있었는지.

“이용했던 거군요. 황실의 정보망을.”

“이용보다는 협력이라는 말이 어울리겠지. 사 황자였던 작금의 천자가 반정을 일으키기 전이었으니.”

“그럼 혹시 황제도…….”

“아니. 어렴풋이 짐작만 할 뿐, 그는 아무것도 몰라. 그것이 내가 제시한 조건 중 하나였고, 그가 황위에 오른 뒤부터 천하 곳곳의 정보를 알게 되었다는 것이 중요하지.”

궁성은 힘의 균형을 단번에 뒤집을 수 있는, 상당한 무게를 지닌 저울추였다.

궁인(宮人)으로 위장한 그녀는 황제의 곁에 머무르며 천하 각지에서 일어나는 크고 작은 일들을 속속들이 알게 되었고, 정체를 알 수 없는 초절정 고수의 존재는 동천마군의 움직임을 억제시키는 결과를 낳았다.

“여러모로 옳은 선택이었다. 황궁에 머무르며 그간 보고 듣지 못했던 것들을 알 수 있었으니.”

그중 하나는 황실에까지 깊게 뿌리를 내린 암천(暗天)의 존재였고, 다른 하나는…….

“내 눈이 닿지 않는 곳에서 성장하고 있던 누군가였지.”

하늘을 바라보고 있던 궁성이 시선을 돌렸다. 허공에서 맞부딪친 그 눈빛에, 나는 조용히 숨을 삼켰다.

“태원진가. 진태경. 처음에는 낯설면서도 관심이 가지 않았다. 산서(山西)에서 두 번째 소식이 들려오기 전까지는.”

“두 번째 소식이라면.”

“화왕 적천강이 제자를 들였다는 믿을 수 없는 이야기였지.”

궁성이 희미하게 웃으며 덧붙였다.

“물론, 그로부터 상당한 시일이 지난 후에 들려온 소식들은 그보다 훨씬 놀라웠지만.”

태원진가가 산서성을 제패하고 일 년이 흐른 뒤.

구화산에서의 폐관 수련을 끝마치고 하산한 나는 전과는 비교도 할 수 없이 달라져 있었다.

일신의 무위도, 마음가짐도.

그리고 그런 나를 기다리고 있는 여러 굵직한 사건들도.

“너에 관한 소식을 들을 때마다 점점 더 흥미가 생겼다. 아니, 그건 흥미 이상이었어.”

선택받은 자.

밤을 밝히는 등불이자, 새로운 하늘의 아침을 열 자.

궁성이 오랫동안 찾아 헤맸던 미지의 존재가 조금씩 장막 뒤에서 모습을 드러내고 있었다.

“그렇기에 이제는 직접 확인해야 했다. 내 마음속의 저울에 올려둔 두 사람 중 누가 선택받은 자인지 알아야 했으니까.”

두 사람.

유독 선명하게 귓가를 파고든 그 단어에, 내 머릿속을 섬광처럼 스치는 한 사람의 이름이 있었다.

“……청풍(淸風).”

불현듯 내뱉은 한 마디에, 궁성이 작게 고개를 끄덕였다.

“그래. 화산신룡 청풍. 그 아이 역시 선택받은 자일 가능성이 충분했지. 만약 대연회장에서의 네 모습을 보지 못했다면, 나는 검성의 제자를 선택받은 자라 여겼을 것이다.”

그러나 궁성의 입장에서는 둘 모두를 부를 필요는 없었을 것이다.

둘 중 한 사람이 선택받은 자라는 생각은 이미 어느 정도 확고해진 상황.

더군다나 내게는 이번에 벌어진 사건과 얽힐 만한 충분한 연결 고리가 존재했으니.

“너와 상산왕, 아니 황태제와의 인연은 이미 알고 있었다. 암천이 먼저 손을 뻗어 아군인 양 홍진에게 연락을 취했을 때, 차라리 잘되었다고 여겼지. 하지만 확실한 무언가가 더 필요했어.”

순간, 나는 문득 떠올렸다.

처음 홍진에게 연락을 취한 것은 마삼보였다는 것을.

그러나 내가 황궁이라는 사지(死地)에 뛰어든 이유는, 비단 주표를 구하기 위해서였음이 아니었다는 것을.

“혈혼고(血魂蠱)…….”

누군가가 쇠망치로 뒤통수를 후려친다면 이런 기분일까.

나는 신음하듯 말을 이었다.

“사천성주의 몸에 혈혼고를 심은 것이, 바로 당신이었습니까?”

쓴웃음을 짓고 있는 궁성의 얼굴이, 낙인처럼 눈동자에 틀어박혔다.
```

## Final English reading copy

```markdown
# Chapter 927

An inexplicable shiver ran down my spine.

The power of supernatural forces—the kind that could even evade death.

I knew better than anyone what that power was, the only way to define it being as something uncanny, like the work of ghosts.

*The System.*

A stroke of luck that had come to me when my life was slowly sinking like a boat with a hole in its hull.

A power that had given me both my greatest crisis and my greatest opportunity.

And yet, in this world called Murim, there was only one person besides me who knew the System existed.

The Fire King, Jeok Cheongang.

No one else could know the true nature of the power I possessed.

That included not only the Imperial Palace, but also the handful of people who had been at my side, even up close.

*They might have some vague sense that there’s something there, but that’s as far as it goes.*

I’d crossed the line between life and death more times than I could count.

I’d survived situations that would have killed an ordinary person several times over, and I’d grown at a pace without precedent in Murim’s history.

Even so, no one knew exactly what my power was.

No—not unless I told them the truth myself.

That was the kind of power the System was.

A supernatural ability no human could even begin to imagine, one that couldn’t be contained by the four characters of *supernatural powers*.

*Even if that person is the Bow Saint, she’s no exception.*

The shock I’d felt in that fleeting moment had long since settled.

But one question remained, one I couldn’t answer on my own: how had *they* learned about something only a handful of people knew about me?

*The Bow Saint. And…*

The Martial God.

The shadows of two giants who had vanished from the world long ago were falling over me at this very moment.

Not like shade cooling me from the sun, but like a kind of darkness.

It was enough to make my skin crawl.

I licked my dry lips. My mouth felt as rough as if I’d swallowed a fistful of sand.

*What on earth do they know, and how much?*

Just as I sent the unspoken question drifting through my mind, the Bow Saint—who had been watching me in silence with deeply shadowed eyes—suddenly spoke.

“You’re calmer than I expected. I thought you might ramble on with excuses. Or pretend you didn’t know.”

I forced myself to answer evenly. “Would that change anything?”

“No. Nothing at all. You know that, too, don’t you?”

The moment I heard that reply, I knew for certain.

This woman before me—the Bow Saint—had been watching me all along.

And she knew more than I’d imagined.

*Then could it be…? No. That can’t be.*

I pushed away the question that had suddenly flashed through my mind and spoke in a sharp voice.

“Since when?”

“That short question seems to hold several meanings. Let’s see… I’m not sure how to answer it. Why don’t I start with what happened today?”

The Bow Saint gently brushed the flowers lining either side of the path as she continued.

“Blazing Flame Divine Dragon Jin Taekyung. The moment I saw you rise when you should surely have been dead, I finally became certain who the chosen one the Martial God spoke of was.”

“How could that man—no, how could the Martial God…”

“How does he know about you?”

I nodded, keeping my agitation in check.

It felt as if every nerve in my body were drawn taut.

Everything could change completely depending on this answer. The course of what came next could twist in a direction even I couldn’t predict.

The Bow Saint’s brief reply the next moment was enough to bring my thoughts to a halt.

“Why would I know?”

“What does that—”

“Neither I nor he could have known. It’s only natural. I found that letter before you were even born.”

“…A letter? Before I was born?”

“Yes. I first found it one day, after many years had passed since the Great Faction War ended—after the mountains and rivers had changed more than once.”

The Bow Saint’s calm voice mingled with the early morning air and drifted into my ears.

“At first, I thought it was simply the trace of some unknown ancient. But I was wrong. The letter had been left for me by the Martial God.”

“Then what, exactly, did the letter say?”

“An arrangement he had made. No—perhaps a kind of prophecy.”

“……!”

“And there was one word that always appeared in its contents.”

My chest felt tight, as though a great stone had been placed in the hollow there.

I forced the words out.

“The chosen one.”

“That’s right. And ‘the chosen one’ didn’t point to any one specific person.”

*Step. Step.*

Her careful footsteps moved through the grass, avoiding each blade.

Faint moonlight poured over the Bow Saint’s head as she walked through the garden.

“I couldn’t believe it, but I had no choice.”

Because he was the Martial God.

Her voice held an awe she couldn’t conceal.

The Bow Saint added, in a voice as faint as the moonlight, and continued slowly, matching her steps.

“So, after several decades, I went out into the world and traveled the land. I spent most of my time in the Central Plains, but at one point I went to the endless desert in the west, and at another I crossed the grasslands and traveled as far as the Northern Sea, full of moss and ice.”

The journey to find the “chosen one” mentioned in the Martial God’s letter was like searching a field of sand for one special grain. The Bow Saint had to shoulder the entire burden alone.

“I couldn’t ask anyone for help. The letter said that not a single detail related to the mission could be revealed before it was completed.”

But the Bow Saint never gave up.

The Martial God’s arrangement, which was almost like a prophecy, required someone called the chosen one.

“When the whole world is covered in darkness, they will become a lamp and light the way. They are the one person who will finally open a new sky and bring the dawn.”

The Bow Saint murmured those words, then turned her head toward the sky.

“But even after I searched and searched for someone whose age, face, name, and even gender I didn’t know, the chosen one never appeared.”

Of course not.

Finding a single person in this vast land—someone who might not even have been born yet—was almost impossible.

“But it wasn’t completely impossible. If what he wrote in the letter was true, the chosen one would be able to distinguish themselves at a dazzling pace.”

A needle in a bag.

A needle in a pouch was bound to poke out eventually.

No matter where it was, or how deeply it was buried in a crowd.

“I followed the rumors and sought out the people I thought might be the chosen one. But even at Heaven’s Gate Temple, where the brightest talents in the land gather, I couldn’t find any real certainty.”

Heaven’s Gate Temple was where my second older brother, Jin Mukyung, had spent some time as the Second Young Master of the Jin Family of Taiyuan.

It was a cradle of talent, overflowing with gifted people of every kind, along with the heirs of the most prominent sects.

But even the cadets of Heaven’s Gate Temple, each with their own remarkable talents, fell far short of the Bow Saint’s idea of the chosen one.

“They were all outstanding, but that was all. Every one of them had an obvious limit. They had limits, and so did I.”

I’d been listening to the Bow Saint in silence until then. At last, I understood why she—like the other Three Saints—had disappeared from public view, hidden in the vast shadow cast by the Martial God.

And why she had been staying in the Imperial Palace.

“You were using the imperial information network.”

“‘Cooperating with’ would be more accurate than ‘using.’ That was before the current Emperor, then the Fourth Prince, launched the restoration.”

“Then does the Emperor know…?”

“No. He only has a vague suspicion. He knows nothing. That was one of the conditions I set. And it matters that after he ascended the throne, I gained access to information from every corner of the land.”

The Bow Saint was a weighty counterbalance—one powerful enough to tip the balance of power in an instant.

Disguised as a palace attendant, she stayed by the Emperor’s side and learned every detail of the large and small events unfolding across the land. The existence of an unidentified Supreme Peak master also had the effect of restraining the Eastern Heaven Demon Lord’s movements.

“In many ways, it was the right choice. Staying in the Imperial Palace let me learn things I’d never seen or heard before.”

One of those things was Dark Heaven, which had sunk its roots deep into the imperial court. And the other was…

“Someone who was growing beyond the reach of my eyes.”

The Bow Saint had been looking up at the sky, but now she turned her gaze toward me. Our eyes met in midair, and I quietly swallowed.

“The Jin Family of Taiyuan. Jin Taekyung. At first, the names were unfamiliar, and they didn’t interest me. At least until the second report from Shanxi.”

“What second report?”

“The unbelievable news that the Fire King, Jeok Cheongang, had taken on a Disciple.”

The Bow Saint added a faint smile.

“Of course, the reports that came in quite some time after that were far more surprising.”

A year after the Jin Family of Taiyuan conquered Shanxi Province, I finished my secluded training on Mount Jiuhua and came down from the mountain.

I was incomparably different from before.

In my martial prowess. In my state of mind.

And in the major events waiting for me.

“Every time I heard news about you, I became more and more interested. No—that wasn’t just interest.”

The chosen one.

A lamp to light the night, the one who would open the way to a new dawn.

The unknown person the Bow Saint had long searched for was gradually emerging from behind the curtain.

“That’s why I had to see for myself. I needed to know which of the two people I’d been weighing in my mind was the chosen one.”

Two people.

The word cut through my ears with unusual clarity. A name flashed through my mind like lightning.

“…Cheongpung.”

At the word that slipped out of me, the Bow Saint gave a small nod.

“That’s right. Cheongpung, the Huashan Divine Dragon. He, too, had every chance of being the chosen one. If I hadn’t seen you at the grand banquet hall, I would have believed the Sword Saint’s Disciple was the chosen one.”

But the Bow Saint wouldn’t have needed to call both of us here.

She was already fairly certain that one of the two was the chosen one.

And I had plenty of connections that might have tied me to the events that had just taken place.

“I already knew about your connection with Prince Shangshan—no, the Crown Prince. When Dark Heaven reached out to Hong Jin first, pretending to be an ally, I thought it might actually work out well. But I needed something more conclusive.”

Just then, something suddenly came back to me.

Ma Sanbao had been the one who first contacted Hong Jin.

And I hadn’t thrown myself into the deadly place that was the Imperial Palace only to save Zhu Bao.

“Blood Soul Gu…”

Was this what it felt like to get hit in the back of the head with a sledgehammer?

I continued as if groaning.

“Were you the one who planted the Blood Soul Gu in the City Lord of Sichuan Province?”

The Bow Saint’s bitter smile branded itself into my eyes.
```

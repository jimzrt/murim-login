<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0895.txt",
      "sha256": "eb5095407fe93336254b33ba01f864081b0ddb7062551e2840fee8df6ef699d4",
      "bytes": 14401
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "97cdcc3e4025e2a600fa05034dbb12fb90331096490c1777b46f24b729d42920",
      "bytes": 1747
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "e97b0d558b9273a9257e26e760fa1192201c3613127339daa699815904154f1b",
      "bytes": 230652
    },
    {
      "path": "characters/Baek Yeon.md",
      "sha256": "f298f090479dfe0d40f89c19370c6324438aacbf326eb7f7487672e7adabb783",
      "bytes": 983
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "45240235f6f2b227e40caec0a381b63201b9c382477c207a91758daa0343d4ec",
      "bytes": 759
    },
    {
      "path": "characters/Hanga.md",
      "sha256": "d07db61229ca08e473c4f71110da06bf161982be31efbb5c78d001309207a4da",
      "bytes": 568
    },
    {
      "path": "characters/Hong Jin.md",
      "sha256": "71f608a49f6982bf8b3e698ac1e34db0d4b217c864a52f3c5790303d5c9ea1de",
      "bytes": 837
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "37d6f4a002cff198f5aa73d72ca9867b71344235e1d3d8d388e3fca1b1640e98",
      "bytes": 1499
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "62376e632b1925ee4c4781f2615591c2f6ba746012c98410137bd1d4271dd96a",
      "bytes": 1782
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "79eaf29bcb16a4099236c56a8542fc67d155755eb2a3977e00f04768e220e6c3",
      "bytes": 622
    },
    {
      "path": "characters/Ma Sanbao.md",
      "sha256": "aa3454205cea6eab1972e247ba74bc32af2a5c917a3920a7decb136c551dc525",
      "bytes": 834
    },
    {
      "path": "characters/Mae Jonghak.md",
      "sha256": "9784070d2a793549893d756f199776c8e3597d12d980a391e5e51ba48564380b",
      "bytes": 1061
    },
    {
      "path": "characters/Prince Shangshan.md",
      "sha256": "61cbf4c796f5d560b4431a20b9faa604bd550be776ccc0f8580698b66da6b657",
      "bytes": 952
    },
    {
      "path": "characters/So Gyo.md",
      "sha256": "4d88a1d930b5155fbb1b012002595eb1514b19e1782097dbd7a9f3c3806e8ec4",
      "bytes": 900
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "af87898701cd3bcdd001b0e14aa053b12518f5955ff7259643b4a58f979cdcfb",
      "bytes": 260878
    }
  ],
  "estimated_tokens": 13668
}
-->

# Durable State Update — Chapter 895

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
1 and safe_through 895. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 895. Profile updates may replace only one
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
  "chapter": 895,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 895,
    "continuity_sources": [895],
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
    "The grand banquet is approaching, and the group expects a decisive conflict may occur there.",
    "The enemy sees a decisive battle as the quickest route to controlling the Great Nation, but its confidence remains unexplained.",
    "The restoration army has spent more than a decade preparing for the coup.",
    "The old assassin Jin encountered may be the One-Legged Ghost Killer, a famed Qinghai assassin; Namho says the identification is uncertain and the man is currently an ally.",
    "Jin is troubled by the alliance with the old assassin and intends to ask Ma Sanbao why he brought the assassins into the cause.",
    "Jin recognizes that he has killed people without seeking alternatives and is trying to become better.",
    "The Divine Physician says his Master destroyed Salcheonmun because its members felt no regret or remorse for their deeds.",
    "Hong Dao foresaw an unknown calamity and identified Jin Taekyung as the Morning Star, whose light would persist through the coming darkness.",
    "Jeok Cheongang sees protecting those he still has as his cause and will support Jin whatever path he chooses.",
    "Ma Sanbao confirms that he hired the assassins; his reasons remain unknown."
  ],
  "continuity_sources": [
    893,
    894
  ],
  "open_questions": [
    "What accounts for the enemy's confidence that the decisive battle's outcome is assured?",
    "Why did Ma Sanbao hire the assassins and bring them into the cause?",
    "Is the old assassin Jin encountered truly the One-Legged Ghost Killer?",
    "What will happen at the approaching grand banquet?",
    "Who is So Gyo, and why did she release Jin?"
  ],
  "safe_through": 894,
  "temporary_decisions": [],
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
| 일신     | **One God**         |
| 삼성     | **Three Saints**    |
| 무림맹    | **Murim Alliance**               |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 생사결    | **life-and-death duel**                          | Explicitly lethal                                     |
| 마교     | **Demonic Cult**                                 |                                                       |
| 제자     | **Disciple**                                 |
| 전각     | **pavilion**                                 | Use “hall” only when established for a specific named building |
| 보상               | **Reward**                     |
| 백연 | **Baek Yeon** | Commander of the Embroidered Uniform Guard. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 항아 | **Hanga** | Local village boy who lives near Jang Taebo. |
| 홍진 | **Hong Jin** | Level 22 man at the City Lord's luncheon; delicate in appearance and voice. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 마삼보 | **Ma Sanbao** | The East Depot’s Brush-Holding Eunuch and second-in-command. |
| 상산왕 | **Prince Shangshan** | The City Lord and a member of the imperial family who orders the luncheon. |
| 소교 | **So Gyo** | The palace attendant leading the group assigned to serve Prince Shangshan. |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 전세 | **jeonse lease** | Korean lump-sum deposit lease used in the family's redevelopment-era housing history. |
| 내상 | **Internal Injury** | System condition label for internal injury. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 오대세가 | **Five Great Families** | Major Murim grouping. |
| 천자 | **Son of Heaven** | Honorific title for the Emperor. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 군림 | **The Reign** | Opening fragment of an incomplete wuxia novel title that Taekyung read through volume thirty-four. |
| 선황 | **the late Emperor** | The former Emperor whom Hong Jin served. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 화주 | **strong liquor** | Liquor stored and consumed by the dark-path swordsmen. |
| 일각 | **fifteen minutes** | Quarter of a shichen; used for the remaining completion time. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 반로환동 | **Returned to Youth** | Possible explanation for an apparently young Supreme Peak master. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 백중 | **Baekjung** | Traditional Buddhist observance during which the Shaolin attack occurs. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 준이 | **Jun** | Family nickname used in the form Jun's dad. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 살수 | **assassin** | Professional killer considered as a possible suspect. |
| 오대 | **Five Squads** | Named Tang Clan organizational group in Tang Sadok's mobilization order. |
| 열화신룡 | **Blazing Flame Divine Dragon** | New sobriquet bestowed on Jin Taekyung. |
| 푸린 | **Furin** | Russian president mentioned in a forum headline. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 위압 | **Intimidation** | System attribute strengthened by the achievement reward. |
| 대역 | **stand-in** | Jin's term for the substitute Go Jun used to fake Song Cheonwoo's departure. |
| 화신 | **Fire God** | A local deity worshiped by one Nanman believer. |
| 금의위 | **Embroidered Uniform Guard** | Imperial guard force mentioned by Hong Jin. |
| 동창 | **East Depot** | Imperial agency named by Hong Jin. |
| 창공 | **Cang Gong** | The bedridden East Depot leader for whom Ma Sanbao acts. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 홍진 | 진태경 | political_host_to_young_martial_artist | Young Hero Jin; Young Master Jin; Sleeping Dragon of Shanxi | polite, coaxing, and probing | Uses respectful forms while steering Taekyung toward relaying the Escort Bureau proposal and teasing him with the Seongun Escort Bureau. |
| 진태경 | 홍진 | young_martial_artist_to_political_official | Comrade Chairman—no, Deputy Military Commissioner | casual and teasing, then formally corrective | Deliberately jokes with an inappropriate title before correcting himself to Hong Jin's official office. |
| 진태경 | 항아 | visiting_adult_to_local_child | little one | friendly and coaxing | Questions Hanga and offers food in exchange for information. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 매종학 | 진태경 | older_ally_to_younger_friend | friend | casual-familiar | Mae Jonghak uses 친구 when arriving at Taekyung's window and asking to talk. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 매종학 | 적천강 | long-standing martial rival and friend | Great Hero Jeok | casual and familiar | Mae addresses Jeok as 적 대협 while discussing the Alliance Leader position. |
| 적천강 | 매종학 | long-standing martial rival and friend | you | blunt and familiar | Jeok addresses Mae as 당신 while recalling their meeting at Mount Jiuhua. |
| 진태경 | 매종학 | younger ally to newly installed Alliance Leader | Alliance Leader | formal and deferential | Uses 맹주님 while formally greeting Mae Jonghak as the Alliance Leader. |
| 홍진 | 백연 | imperial aide confronting a senior military officer | you | angry and confrontational | Uses 당신 in an indignant outburst. |
| 진태경 | 백연 | young martial artist confronting an imperial military commander | you | casual and insulting | Refers to Baek as 이 양반 while challenging his conduct. |
| 홍진 | 마삼보 | Longtime friend and former East Depot cohort | Ma Constable; Eunuch Ma | Familiar and respectful | Hong uses both forms while acknowledging Ma’s former and current standing. |
| 마삼보 | 홍진 | Longtime friend and former East Depot cohort | Hong Constable | Familiar and respectful | Ma addresses Hong by his former East Depot title. |
| 백연 | 천자 | imperial officer addressing the Emperor | Your Majesty | formal, deferential in address but openly defiant in private counsel | Baek uses formal honorifics while sharply confronting the Emperor over their shared undertaking. |
| 천자 | 백연 | Emperor addressing his military commander | Baek Yeon | familiar and authoritative | The Emperor addresses Baek by name and gives him a direct warning. |
| 진태경 | 상산왕 | protector addressing a young prince | His Highness | respectful royal address | Taekyung refers to the prince as 상산왕 전하 when ordering Mujin to bring him. |
| 진태경 | 황제 | guest of the Emperor’s younger brother addressing the Emperor | Your Majesty | formal and deferential in address, despite blunt challenges | Taekyung repeatedly addresses the Emperor as 폐하. |
| 상산왕 | 황제 | younger brother addressing the Emperor | Your Majesty | deferential royal address | Shangshan addresses the Emperor as 폐하 while pleading for Taekyung. |
| 소교 | 진태경 | palace attendant addressing a martial artist and guest under escort | Young Master Jin | formal and respectful, but firm | Addresses him as 진 공자 while escorting him and warning him not to investigate. |
| 진태경 | 소교 | palace attendant and martial artist under imperial scrutiny | you | formal-polite, controlled and challenging | Taekyung addresses So Gyo as 당신 while questioning her presence and demanding an explanation. |
| 백연 | 진태경 | imperial commander confronting a young martial artist | Jin Taekyung | measured and familiar, using 자네 | Baek Yeon cautions Taekyung about his words and asks whether he must cause a scene. |
| 소교 | 백연 | political ally addressing a senior military commander | you | informal and direct | So Gyo uses 당신 and speaks without formality; no personal name or title is established. |
| 백연 | 소교 | military commander addressing a powerful political ally | you | formal and deferential | Baek Yeon uses 그대 while questioning So Gyo; she speaks without formality, which he accepts as her due. |

## Listed compact profiles

### Baek Yeon.md

# Baek Yeon (백연)

- **Safe through:** Chapter 889
- **Aliases:** Blood Envoy
- **Role:** Baek Yeon is the Commander of the Embroidered Uniform Guard, a former martial arts instructor to the Crown Prince, and the Blood Envoy who helped the fourth prince seize the throne and led the purge.
- **Personality:** Politically assured and controlled, he enforces authority with ruthless decisiveness but speaks with striking defiance to the Emperor in private when their shared undertaking is at stake.
- **Voice:** Not established
- **Relationships:** He commands the Embroidered Uniform Guard and serves the Emperor; they share an old promise tied to a great undertaking, and Baek urges the Emperor to restore matters before their adversaries' moves unravel it. He orders Jeong Hogun to surveil Prince Shangshan’s party while leaving openings for an approach, and treats Taekyung as a dangerous potential obstacle.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 894
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Hanga.md

# Hanga (항아)

- **Safe through:** Chapter 835
- **Aliases:** None
- **Role:** Local village girl, Jang-pal’s daughter, who lives near Jang Taebo and regularly visits him.
- **Personality:** Curious, energetic, observant, and already attentive to the value of information and food.
- **Voice:** Childlike, direct, and inquisitive, with an occasional surprisingly worldly remark.
- **Relationships:** Calls Jang Taebo Grandpa; Jang Taebo is his elderly neighbor and only conversational companion.

### Hong Jin.md

# Hong Jin (홍진)

- **Safe through:** Chapter 889
- **Aliases:** None
- **Role:** Hong Jin is a Level 22 Deputy Military Commissioner of Shanxi Province, a eunuch and trusted aide to Prince Shangshan, and a former member of the East Depot.
- **Personality:** Composed, socially deft, and ambitious, Hong Jin became a eunuch to escape poverty and save his family, then used his abilities to pursue a broader life.
- **Voice:** Delicate and deferential, using formal, self-effacing language with Prince Shangshan.
- **Relationships:** Hong Jin is devoted to Prince Shangshan, whom the late Emperor entrusted to his care; the Fourth Prince spared him because of their old ties, and his longtime friend and former East Depot cohort Ma Sanbao stayed behind in the palace.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 894
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm, the occupant of the chief seat of the Murim Alliance's Five Kings Hall, and a trusted confidant who accepts Jin as himself despite knowing that he travels between Murim and another world resembling the realm of immortals.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; believes there is no absolute justice and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He deeply trusts Jin Taekyung, his publicly acknowledged Disciple and intended heir, regards him as the light of his later years, and will stand by him whatever path he chooses; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and remains Peng Cheolhu's rival.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 894
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader.
- **Personality:** Hungry, self-aware, dryly observant, and pragmatic under pressure; accepts extreme personal risk when duty and the lives of others demand it.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; they trust each other deeply, though their bond remains unformalized. Cheongpung is his trusted companion and only true martial rival; Choi Minwoo is his subordinate and trusted manager of media and official arrangements as well as the Peace Guild's Guild Master; Ju Hwaran is a trusted Fire Dragon Pavilion member; Magic Johnson and Chuck Hagel are allied to him; his mother and sister Hayeon are among those he protects; the Skeleton King is his friend and ally; Xiao Shen regards him as an older brother; Jin-ho is his older friend and trusted confidant; he once saved Ju Wongong’s life.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 894
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Ma Sanbao.md

# Ma Sanbao (마삼보)

- **Safe through:** Chapter 894
- **Aliases:** None
- **Role:** Ma Sanbao is the East Depot’s Brush-Holding Eunuch and Supreme Peak martial artist, leading the Depot in place of its bedridden leader, Cang Gong.
- **Personality:** He is vigilant and patient, concealing his loyalties while awaiting the moment to act for the late Emperor.
- **Voice:** He speaks in measured, courteous language and uses calm repetition, feigned agreement, and procedural reminders to steer conversations while keeping sensitive details guarded.
- **Relationships:** Ma Sanbao is a longtime friend and former East Depot cohort of Hong Jin, leads the effort to enthrone Prince Shangshan, and confirms he hired the assassins, though his reason remains unknown.

### Mae Jonghak.md

# Mae Jonghak (매종학)

- **Safe through:** Chapter 855
- **Aliases:** Sword Saint
- **Role:** Sword Saint and Cheongpung's grandfather who now serves as the New Murim Alliance's Alliance Leader and has ordered Jin Taekyung's first Fire Dragon Pavilion mission to Nanman.
- **Personality:** Playful, easygoing, and teasing, but capable of handling heavy administrative responsibilities efficiently.
- **Voice:** Friendly, casually familiar, and cheerfully teasing, including when greeting old acquaintances and discussing leadership.
- **Relationships:** Cheongpung's grandfather and martial instructor; taught him the Taeeul Miri Palm; secretly entered Huashan while its Sect Leader slept, left a dagger and handwritten note, and then went into hiding, prompting Huashan's search; fought Jeok Cheongang at Mount Jiuhua more than forty years ago and left after their draw; his old friend Hong Dao left him a letter identifying Jin Taekyung as the Morning Star who would drive away darkness.

### Prince Shangshan.md

# Prince Shangshan (상산왕)

- **Safe through:** Chapter 889
- **Aliases:** None
- **Role:** Prince Shangshan, whose personal name is Zhu Bao, is the Emperor’s twelve-year-old youngest younger brother and an exceptionally skilled young swordsman.
- **Personality:** Earnest and compassionate, he takes responsibility for his loyal subjects’ hardship, admires Jin Taekyung, seeks candid counsel, and shows composure beyond his years in the face of death and political danger.
- **Voice:** Archaic and formal in the manner of a historical drama, with openly eager and childlike reactions beneath his royal diction.
- **Relationships:** Prince Shangshan Zhu Bao is the Emperor’s youngest younger brother; the late Emperor entrusted Hong Jin with his care. Zhu Bao admires Jin Taekyung, seeks to emulate him, and calls him a friend; the Emperor says he will take care of Zhu Bao.

### So Gyo.md

# So Gyo (소교)

- **Safe through:** Chapter 894
- **Aliases:** None
- **Role:** A palace attendant assigned to Prince Shangshan who is a Supreme Peak master and has a mission to keep Jin Taekyung alive; her identity and allegiance remain unconfirmed.
- **Personality:** Calm, calculating, and self-possessed; she conceals her strength and identity and can be openly taunting.
- **Voice:** Measured and composed, shifting from deferential formality to casual, pointed taunts and threats.
- **Relationships:** She poses as the leader of the palace attendants assigned to Prince Shangshan and is Jin Taekyung’s opponent, yet believes he may be the person she seeks and the person foretold by “that person”; she says only she and the Emperor know a secret she withheld from Baek Yeon, while her true allegiance remains unknown.

## Korean source

```text
＃895화



동굴처럼 캄캄한 전각 내부.

나는 창밖에서 들려오는 거센 빗소리를 들으며, 조금 전 들었던 말의 의미를 조용히 곱씹었다.

마치 처음부터 기다리고 있던 것처럼 나를 이곳으로 안내해 준 환관의 모습도 함께.

“이미 알고 있던 겁니까.”

마삼보가 고개를 끄덕였다.

“두 시진 전쯤에 살수들로부터 보고가 들어왔네. 자네에게 정체를 발각당했다고. 그들은 이 상황이 의뢰를 완수하는 것에 있어 걸림돌이 되는 건 아닐까 우려하더군.”

어지간히 눈치 없는 놈이 아닌 이상, 저 우려라는 말이 굉장히 순화된 표현이라는 것쯤은 짐작할 수 있다.

그 상대가 살수들이라면 더더욱.

“그러니까, 태감께서 고용한 살수들이 절 죽이려 했다는 거군요.”

“꼭 그런 건 아니지만, 자네도 알잖나. 살수들이 어떤 부류의 인간들인지.”

“직접 겪어 본 적은 없지만 대충은 압니다. 그리고 그런 자들을 태감께서는 이번 일에 끌어들이셨고요.”

“나로서도 어쩔 수 없었네. 합당한 보수만 쥐여 준다면 누구보다 충성스러워지는 자들이었으니까.”

“그래서, 그들에게 제 처우에 관해 뭐라 하셨습니까?”

“……이보게.”

미간을 좁힌 채 나를 응시하던 마삼보가 한숨처럼 말을 이었다.

“나를 천자와 같은 미치광이로 보지 말게. 자네는 상산왕 전하를 돕기 위해 천릿길을 마다하고 달려온 사람이고, 그들은 보수를 약속받고 의뢰를 수행하는 살수들일 뿐이야. 누가 더 믿을 만한 아군이겠나?”

“그건…….”

“그래, 당연히 자네야. 이것으로 충분한 대답이 됐나?”

아직은 아닙니다.

불쑥 튀어나오려는 그 한마디를, 나는 가까스로 입 안에 가두었다.

‘그래, 아직은 아니지.’

지금까지의 경험 때문일까.

아니면 저 빗줄기처럼 차가워진 머릿속 때문일까.

나는 본능적으로 깨달았다. 지금의 생각을 상대에게 모두 털어놓는 것은 그리 좋은 선택이 아니라고.

그 대신 수긍하듯 고개를 끄덕이며, 잠시 뒤로 미뤄 두었던 의문을 꺼냈다.

“그럼 소교, 그 여자에 대해서도 알고 있었습니까?”

“아닐세. 내가 구태여 살수들에 대한 정보를 숨긴 것은 자네와 같은 무림인들이 그들을 어떤 시선으로 바라보는지 익히 알고 있었기 때문이었지만…… 그 여인은 달라.”

지금 이 순간 마삼보의 얼굴 위로 그늘이 드리워졌다고 느껴진 것은, 결코 주위가 어둡기 때문만은 아닐 것이다.

“소교라는 이름을 쓰는 그 여인에 대해 미리 알려 주지 못한 것은, 우리 역시 그녀에 대해 잘 몰랐기 때문일세.”

“몰랐다고요? 다른 누구도 아닌 동창이?”

금의위와 동창은 천하 곳곳에 뿌리내린 엄청난 규모의 정보 단체.

그런데 그런 동창이, 제아무리 역모 직후 세력이 축소되었어도 본진이나 다름없는 황실의 정황을 몰랐다는 것은 쉽게 이해하기 힘들다.

“더 자세히 말씀해 주십시오.”

“알겠네. 그래야 자네에게 조금이라도 더 믿음을 줄 수 있을 테니까.”

내 눈빛에 담긴 불신을 읽어 낸 마삼보가 씁쓸하게 웃으며 말을 이었다.

“지금으로부터 십여 년 전이었네. 소교, 아니 정체불명의 고수가 처음 모습을 드러낸 것은.”

솨아아아.

서서히 잦아들기 시작한 빗소리 너머로, 그의 목소리가 스며들었다.



* * *



모든 이야기가 끝났다.

일각(一刻) 남짓한 시간 동안 쉬지 않고 말을 이어 간 마삼보는 옆구리에 찬 호리병을 꺼냈고, 나는 혼란스러운 눈빛으로 그를 바라보았다.

“왜 이제야 이런 중요한 정보들을 말해 주는 겁니까? 만약 조금 더 일찍 알았다면…….”

“불안했으니까.”

막 호리병을 기울이려던 마삼보가 말을 이었다.

“변명처럼 들리겠지만 어쩔 수 없었네. 현재 끌어모은 아군의 전력만으로는 그녀를 감당할 수 없을 것 같았어.”

호리병 입구 사이로 독한 주향(酒香)이 흘러나온다. 내 시선을 눈치챈 마삼보가 손에 들고 있던 호리병을 던졌다.

“한잔하겠나? 어지간히 술이 땡기는 표정인데.”

툭.

반사적으로 손을 뻗어 호리병을 받아 낸 나는 잠시 망설이다가 그대로 입가에 가져갔다.

복잡한 이야기를 들었으니 술이 간절할 수밖에 없는 상황.

어차피 항아리째 마셔도 그리 취하지도 않으니 벌컥벌컥 들이켰다.

목으로 넘길 때마다 불처럼 뜨거운 도수와 함께 입 안을 가득 채운 독한 주향이 느껴졌다.

천하의 객잔 어디에서나 파는 값싼 술, 화주(火酒)였다.

“북방이 고향이라 그런지, 화통하게도 마시는군.”

눈살을 찌푸린 채 입 안에 남아 있는 화주를 꿀꺽 삼킨 내가 대꾸했다.

“의외네요. 좀 좋은 술을 드실 줄 알았는데.”

“왜, 동창 병필태감은 화주 같은 싸구려는 안 마실 줄 알았나?”

피식, 작게 실소를 흘린 마삼보가 고개를 내저었다.

“아무리 높은 자리에 올랐어도 내 본질은 화주일세. 어디에서나 볼 수 있는 밑바닥 인생이었던 것도, 속에 감춘 것을 쉽게 보이지 않는 것도 닮았지. 황궁에서 오랫동안 살아남으려면 화주가 가진 독한 주향처럼 속마음을 감춰야 하거든. 그런 의미에서는 소교 그 여인과 같은 부류라고도 할 수 있겠군.”

그래, 소교.

나는 조용히 그 이름을 곱씹었다. 조금 전 들었던 믿지 못할 이야기와 함께.

“전부 사실입니까?”

“들어 보니 어때, 거짓이라고 생각하나?”

“저는 대답을 듣고 싶은 겁니다.”

“확답을 원한다면, 그래. 모든 것이 단 한 치의 거짓도 없는 사실일세. 내 목숨을 걸지.”

굳은 얼굴로 대답한 마삼보가 문득 창가를 향해 고개를 돌렸다.

창밖 너머, 부쩍 가늘어진 빗줄기를 바라보는 그의 눈은 깊게 가라앉아 있었다.

“단언컨대 소교. 그 여자만 아니었다면 그날의 역모는 성공할 수 없었을 거야. 창공(廠公)께서 지금처럼 병석에 누워 계실 일도 없었겠지.”

소교가 처음 모습을 드러낸 것은 십여 년 전, 황궁이 전화(戰火)에 휩싸인 그 날이었다고 했다.

“홍진 그 친구는 줄곧 선황 폐하의 곁에 머무르느라 몰랐겠지만, 말했다시피 우리 동창은 그날의 역모를 막기 위해 최선을 다했었네.”

마삼보의 이야기가 사실이라면, 지금은 병마를 이기지 못해 쓰러진 창공은 대단한 걸물이었다.

백연보다도 먼저 선황을 모셨으며, 일신의 무공 또한 황실 제일의 무장이라 불리던 백연과 어깨를 나란히 할 만한 수준이라고 평할 정도였으니.

“가장 먼저 낌새를 알아차린 것도 창공 어른이셨지. 그분께서는 황도 외곽의 금위군을 소환하고, 황궁 내의 동창과 함께 반역자들을 격퇴하려 하셨네.”

당시의 마삼보 역시 창공의 휘하에 있었고, 황궁 내의 금의위를 물리치고 선황의 신병만 재탈환한다면 충분한 승산이 있다고 판단했다.

한 사람이 나타나기 전까지는.

“백연과 창공 어른 간의 생사결은 백중세(伯仲勢)였네. 그 흐름이 그대로 유지만 되었더라면 능히 역모를 진압할 수 있었을 거야. 금위군이 합류한다면 금의위로서도 버티기 힘들었을 테니까. 하지만…….”

마삼보가 딱딱한 음성으로 말을 이었다.

“세상일이 뜻대로 되는 것은 아니더군.”

전신을 흑의(黑衣)로 감싼 정체불명의 고수가 나타나면서 전세는 급격히 기울었다.

백연과 흑의인.

두 초절정 고수의 합공을 이기지 못한 창공은 극심한 내상과 함께 쓰러졌고, 팽팽한 접전의 흐름은 그대로 허물어졌다.

“당시 아군의 전력은 결코 금의위에 비해 뒤떨어지지 않았었네. 유일한 패인(敗因)은 바로 그 흑의인…… 아니, 이제는 소교라고 불러야 할 정체불명의 고수였지.”

마삼보는 목이 타는지 내게 돌려받은 호리병을 기울이려 했지만, 어느새 파르르 떨리는 손끝에서 미끄러진 그것은 힘없이 바닥을 나뒹굴었다.

텅. 데구르르.

공허한 소리와 반쯤 남았던 술이 울컥 흘러넘친다.

무거운 눈빛으로 바닥에 고여 가는 술을 내려다보던 마삼보가 혼잣말처럼 중얼거렸다.

“그때 목격했던 무위는 정말이지…… 소름이 끼칠 정도였네. 그 압도적인 기세 앞에서 나는 아무것도 할 수 없었어.”

나는 문득 떠올렸다.

시종일관 봄바람처럼 잔잔하던 소교의 기운을. 그리고 찰나의 순간 그녀를 중심으로 솟구쳤던 그 무시무시한 기파를.

“분명 그것 역시 전력을 다한 게 아니었겠지.”

넘을 수 없는 거대한 벽을 마주한다면 그런 기분이었을까.

지금껏 수많은 강자를 만났지만, 적아를 포함해서 그 정도의 위압감을 느끼게 만든 이들의 머릿수는 불과 열 명도 채 되지 않았다.

‘그리고 그들 모두 삼성(三星)에 속한 이들이거나, 그와 충분히 비견되는 고수들이었고.’

무인이라면 누구나 꿈꾸는 초절정의 경지를 벗어나, 더 높은 지고의 영역에 발을 디딘 자들.

긴 세월 동안 심신을 갉아먹던 심마를 떨쳐 내고 비로소 반로환동의 경지에 이른 적천강이 그러하듯, 소교 역시 만부부당(萬夫不當)이라는 표현이 부족하지 않을 만한 고수였다.

“그래서 날 택한 거였군요. 아니, 저와 제 스승님을.”

“맞네. 앞서 말했던 그대로지.”

이미 모든 진실을 밝힌 상황.

마삼보는 무거운 얼굴로 말을 이었다.

“상산왕을 위해 천 리 길을 마다하지 않고 달려와 줄 사람. 결과에 대한 보상보다 인의(人意)를 최우선으로 삼을 만한 누군가. 그리고…….”

“황제의 곁에 머무르는 정체불명의 고수를 상대할 만한 또 다른 강자. 화왕(火王) 적천강. 맞습니까?”

잠시 침묵하던 마삼보가 힘없이 고개를 끄덕였다.

“정확하네. 홍진에게 밀서를 보낼 때 자네의 이름을 써 넣은 것도 그런 이유에서였지. 하나뿐인 제자가 위험을 무릅쓰고 황궁으로 향한다면, 그 스승 역시 함께하리라는 것은 어렵지 않게 예상할 수 있었으니까.”

“그럼 남만에서 벌어진 상황을 모두 알고 있던 것도?”

“전부터 예의주시하고 있었지. 남만이 아닌 자네를.”

“왜 진작 무림맹에 정식으로 도움을 요청하지 않았습니까? 차라리 그편이 훨씬 나았을 텐데요.”

“현 맹주인 검성 매종학에 대해서는 나 역시 아는 바가 적지 않네. 창공께서는 그를 가리켜 이 시대에 몇 안 남은 진정한 협객이라고도 하셨고.”

“그렇다면 굳이 저나 스승님을 택할 이유가 없지 않습니까?”

“비밀은 드러나지 않을수록 좋지 않겠나. 그 비밀이 역모(逆謀)라면 더더욱.”

“아.”

침음성을 흘리는 내 모습에 마삼보가 씁쓸하게 웃었다.

“말이 좋아 반정군(反正軍)일 뿐. 세상 사람들의 눈에는 우리야말로 대역죄인이 아니겠나. 더군다나 이 일에 무림과의 연관성이 밝혀진다면 결코 좋은 방향으로 흘러가지 않을 터.”

무림은 엄연히 대국이라는 울타리 안에 존재하는 숲이지만, 나라의 법치를 정면으로 거스르는 집단이기도 하다.

그러니 무림맹이 개입한다는 건, 황위를 둘러싼 이 중요한 싸움에 일종의 외세(外勢)를 끌어들이는 것과 진배없는 셈이다.

그것도 목줄도 없이 울타리를 벗어난 맹수들을.

“물론 현 무림맹주 역시 우리를 도우려는 심산이었을걸세. 자네에게 상산왕 전하를 호위하라는 밀명을 내린 것만 보아도 알 수 있지.”

“사실입니다. 저희로서도 황실의 움직임 하나하나에 촉각을 곤두세워야 하는 상황이기도 하고요.”

“하지만 도움을 줄 수 있는 것도 딱 그 정도야. 정식으로 반정군에 가담하라고 한다면, 과연 무림맹의 수뇌부들 중 몇 명이나 동의하겠나?”

“그건…….”

나는 말꼬리를 흐렸다.

역모.

떠올리는 것만으로도 등골이 서늘해지는 단어.

마교 내부에서 마치 왕처럼 군림했다던 천마라면 모를까, 지지를 통해 선출된 무림맹주가 독단적으로 이와 같은 결정을 내릴 수는 없다.

구파일방과 오대세가. 그리고 무림맹의 깃발 아래에 선 수많은 문파들까지.

그들 대부분의 지지를 얻는 것은 사실상 불가능에 가깝다.

옳고 그름을 떠나, 역모는 단 한 순간에 패가망신에 이를 수 있는 위험한 도박이니까.

“그런 의미에서 열화신룡 진태경. 자네에게 정식으로 묻겠네.”

줄기차게 쏟아지던 빗소리도 어느새 거짓말처럼 멎었다. 어둠 속에서 마삼보의 눈동자가 번뜩였다.

“나와, 아니 우리와 손을 잡겠나?”

힘이 실린 목소리가 또렷하게 귓가를 파고들었다.

“우리를 도와 이 어지러운 천하의 질서를 바로 세우고, 상산왕 전하를 보위에 올리겠나?”

“……!”

나도 모르게 파르르 떨리는 신형.

뒤죽박죽 뒤엉킨 머릿속에서 한 줄기 벼락이 내리꽂힌다.

짧았지만 그 어느 때보다 길었던 침묵 속, 말없이 마삼보를 응시하던 나는 불현듯 입을 열었다.

“지난번에 보여 주셨던 그 연판장(連判狀). 지금도 갖고 있습니까?”

그 말에 담긴 의미를 깨달은 마삼보의 입가에, 환한 미소가 번졌다.
```

## Final English reading copy

```markdown
# Chapter 895

The pavilion’s interior was as dark as a cave.

Listening to the heavy rain outside the window, I quietly turned over the meaning of what I’d just heard.

And the image of the eunuch who’d led me here as if he’d been waiting for me from the start.

“You already knew?”

Ma Sanbao nodded.

“About two shichen ago, the assassins reported that you’d discovered their identities. They were concerned the situation might interfere with completing the job.”

You’d have to be remarkably oblivious not to realize that *concerned* was a considerable understatement.

Especially when the people involved were assassins.

“So the assassins you hired tried to kill me.”

“Not exactly, but you know what kind of people assassins are.”

“I’ve never dealt with them firsthand, but I have a general idea. And you brought people like that into this affair.”

“I had no choice. If you pay them a fair price, they become more loyal than anyone.”

“So what did you tell them to do about me?”

“…My friend.”

Ma Sanbao fixed me with a furrowed brow, then continued with a sigh.

“Don’t mistake me for a madman like the Son of Heaven. You came all this way, a thousand li, to help His Highness Prince Shangshan. They’re merely assassins carrying out a job they were promised payment for. Which of you is the more trustworthy ally?”

“Well…”

“Exactly. You are. Is that answer enough?”

Not yet.

I barely managed to keep the words from slipping out.

*Right. Not yet.*

Was it because of everything I’d experienced up to now?

Or because my mind had grown as cold as the rain outside?

Instinct told me it wouldn’t be a good idea to lay all my thoughts bare.

Instead, I nodded as if I understood and brought up the question I’d set aside for a moment.

“Then did you know about So Gyo, too?”

“No. I deliberately withheld information about the assassins because I knew how people like you in Murim would see them, but… she’s different.”

The shadow I thought I saw fall over Ma Sanbao’s face just then wasn’t only because of the darkness around us.

“We didn’t tell you about that woman who goes by So Gyo because we didn’t know much about her ourselves.”

“You didn’t know? The East Depot, of all people?”

The Embroidered Uniform Guard and the East Depot were enormous intelligence organizations with roots all across the land.

It was hard to understand how the East Depot could have failed to learn what was happening in the imperial palace, which was practically its own stronghold—even after its influence had shrunk in the wake of the coup.

“Tell me more.”

“All right. It may help you trust me, even a little.”

Ma Sanbao read the distrust in my eyes and continued with a bitter smile.

“It was more than ten years ago. That was when So Gyo—or rather, the unidentified master—first appeared.”

As the rain slowly began to ease, his voice filtered through it.

* * *

The story was over.

Ma Sanbao had spoken without pause for about fifteen minutes. He pulled the flask from his belt, and I looked at him, still bewildered.

“Why are you only telling me this important information now? If I’d known sooner…”

“I was afraid.”

Ma Sanbao had just raised the flask to his lips. He went on.

“It may sound like an excuse, but I couldn’t help it. I didn’t think the forces I’ve gathered so far would be able to handle her.”

The harsh aroma of liquor drifted from the flask’s mouth. Noticing my gaze, Ma Sanbao tossed it to me.

“Want a drink? You look like you could use one.”

I reached out reflexively and caught the flask.

After hesitating for a moment, I brought it to my lips.

After hearing a story that complicated, a drink was only natural.

I could drink straight from the jar and still hardly get drunk, so I took several long gulps.

The liquor’s burning strength went down my throat, its harsh aroma filling my mouth.

It was strong liquor, the cheap kind sold at any inn in the land.

“Maybe it’s because you’re from the north, but you certainly drink with gusto.”

I grimaced and swallowed the liquor still in my mouth.

“Surprising. I thought you’d drink something better.”

“What, you figured the East Depot’s Brush-Holding Eunuch wouldn’t drink cheap stuff like this?”

Ma Sanbao let out a small laugh and shook his head.

“No matter how high I’ve risen, strong liquor is what I am at my core. Like the cheap stuff you can find anywhere, I was once a man from the bottom of society. And like it, I don’t show people what I keep inside. If you want to survive for long in the imperial palace, you have to hide your true feelings like the harsh aroma of strong liquor. In that sense, I suppose I’m the same kind of person as So Gyo.”

So Gyo.

I quietly turned the name over in my mind, along with the unbelievable story I’d just heard.

“Is all of it true?”

“What do you think? Does it sound like a lie?”

“I want an answer.”

“If you want certainty, then yes. Every word is true—not a single lie. I stake my life on it.”

Ma Sanbao answered with a solemn expression, then suddenly turned toward the window.

Beyond it, the rain had grown much lighter. His eyes, fixed on the thinning rain, had sunk deep.

“I can say this with certainty: without So Gyo, that coup would never have succeeded. Cang Gong wouldn’t be bedridden as he is now, either.”

So Gyo had first appeared more than ten years ago, on the day the imperial palace was engulfed in flames of war.

“Hong Jin may not have known, since he stayed by the late Emperor’s side the whole time, but as I said, the East Depot did everything it could to stop the coup.”

If Ma Sanbao’s story was true, then Cang Gong, now fallen to illness, had been a remarkable man.

He had served the late Emperor even before Baek Yeon, and Ma Sanbao said his martial arts were on a level comparable to Baek Yeon’s, despite Baek being hailed as the strongest warrior in the imperial family.

“Lord Cang Gong was the first to sense something was wrong. He summoned the Imperial Guards from the outskirts of the capital and planned to drive back the rebels alongside the East Depot inside the palace.”

At the time, Ma Sanbao had also served under Cang Gong. He’d judged they had a good chance of winning if they could defeat the Embroidered Uniform Guard inside the palace and retake the late Emperor.

That was, until one person appeared.

“The life-and-death duel between Baek Yeon and Lord Cang Gong was evenly matched. If things had stayed that way, we could have put down the coup. The Embroidered Uniform Guard wouldn’t have been able to hold out once the Imperial Guards joined us. But…”

Ma Sanbao continued in a stiff voice.

“Things don’t always go the way you want.”

The battle turned sharply against them when an unidentified master, dressed all in black, appeared.

Baek Yeon and the figure in black.

Cang Gong couldn’t withstand the combined assault of the two Supreme Peak masters. He collapsed with severe Internal Injuries, and the balance of the battle fell apart.

“Our forces were no weaker than the Embroidered Uniform Guard. The only reason we lost was that figure in black… No, that unidentified master I should now call So Gyo.”

As if his throat had gone dry, Ma Sanbao tried to raise the flask I’d returned to him. But it slipped from his fingertips, which had started to tremble.

It hit the floor with a hollow thud and rolled.

The flask was still half full, and the liquor spilled out in a rush.

Ma Sanbao stared down at the puddle forming on the floor, his eyes heavy, then murmured as if to himself.

“Her skill that day was… chilling. I couldn’t do a thing in the face of that overwhelming aura.”

I suddenly remembered So Gyo’s energy, calm as a spring breeze from beginning to end. And the terrifying wave of power that surged from her in that brief instant.

“Surely she wasn’t even going all out.”

Was that what it felt like to stand before an insurmountable wall?

I’d met plenty of powerful people, but fewer than ten—enemy or ally—had ever made me feel that kind of pressure.

*And every one of them was one of the Three Saints, or a master who could stand as their equal.*

They had moved beyond the Supreme Peak realm that every martial artist dreamed of, stepping into an even higher, exalted realm.

Just as Jeok Cheongang had cast off the Heart Demon that had gnawed at him for so many years and at last reached the realm of Returned to Youth, So Gyo, too, was a master who could rightly be called *a match for ten thousand men*.

“So that’s why you chose me. No, me and my Master.”

“That’s right. Just as I told you before.”

Now that he’d revealed the whole truth, Ma Sanbao continued with a grave expression.

“Someone who would come a thousand li to help Prince Shangshan. Someone who’d put human decency ahead of any reward. And…”

“Another master who could face the unidentified expert at the Emperor’s side. The Fire King, Jeok Cheongang. Am I right?”

Ma Sanbao was silent for a moment, then nodded weakly.

“Exactly. That’s why I wrote your name in the secret letter I sent to Hong Jin. It wasn’t hard to guess that if you, Jeok Cheongang’s only Disciple, risked going to the imperial palace, your Master would come along.”

“Then you knew everything that happened in Nanman, too?”

“I’ve been keeping an eye on things for a while. Not on Nanman—on you.”

“Why didn’t you ask the Murim Alliance for help officially? That would have been much better.”

“I know quite a bit about the current Alliance Leader, Sword Saint Mae Jonghak. Cang Gong once called him one of the few true chivalrous heroes left in this age.”

“Then there was no reason to choose me or my Master.”

“The less a secret is exposed, the better, don’t you think? Especially when that secret is a coup.”

“Ah.”

I let out a low groan, and Ma Sanbao smiled bitterly.

“We may call ourselves a restoration army, but in the eyes of the world, aren’t we the traitors? And if our ties to Murim were revealed, things would never go well for us.”

Murim existed within the Great Nation’s borders, but it was also a society that openly defied the laws of the land.

So if the Murim Alliance intervened, it would be like bringing in a foreign force to this crucial struggle over the throne.

A pack of beasts that had slipped beyond the fence, with no leash on them.

“Of course, the current Alliance Leader was probably willing to help us. You can tell from the secret order he gave you to guard Prince Shangshan.”

“That’s true. We also have to keep a close eye on every move the imperial family makes.”

“But that’s about as far as he can go. If he formally asked them to join the restoration army, how many of the Alliance’s leaders would agree?”

“Well…”

My voice trailed off.

Coup.

Just thinking of the word sent a chill down my spine.

Maybe the Heavenly Demon, who’d supposedly ruled the Demonic Cult like a king, could make that kind of decision alone. But the Alliance Leader, elected through the support of others, couldn’t.

The Nine Sects and One Gang. The Five Great Families. And all the other sects under the Murim Alliance’s banner.

Getting support from most of them was practically impossible.

Right or wrong, a coup was a dangerous gamble that could ruin you in an instant.

“In that case, Blazing Flame Divine Dragon Jin Taekyung, I’ll ask you directly.”

The pounding rain had stopped as if by magic. Ma Sanbao’s eyes flashed in the darkness.

“Will you join forces with me—or rather, with us?”

His voice was full of conviction, cutting clearly through the silence.

“Will you help us restore order to this troubled land and put His Highness Prince Shangshan on the throne?”

“……!”

My body trembled before I could stop it.

A bolt of lightning struck through the tangled mess in my head.

After a brief silence that somehow felt longer than any other, I stared at Ma Sanbao and suddenly spoke.

“Do you still have that joint pledge you showed me last time?”

At the meaning behind my words, a bright smile spread across Ma Sanbao’s face.
```

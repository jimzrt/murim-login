<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0923.txt",
      "sha256": "f7e759895dc3d843030a5c9ebda65ec1bf4276b2a54a750915f43ffadafc048a",
      "bytes": 14458
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "791ed30d97b670e57f539ed73f308598848370f0737bf78f830d65791b8bb305",
      "bytes": 1771
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "e4f261a256443b1a8267b983fdbd4ae7aa3530803a007681e483b189b757b921",
      "bytes": 231635
    },
    {
      "path": "characters/Baek Yeon.md",
      "sha256": "53a3fea370ef0707c7871161eaa7a5e4efb3438674d0bc853fc6dda464081dca",
      "bytes": 837
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "77315f0f40c2165e614e05016756c5c817a8c1e229985d97f72bdbe8b9704e86",
      "bytes": 759
    },
    {
      "path": "characters/Eastern Heaven Demon Lord.md",
      "sha256": "d42ff5c93d80a16096c3b66e4fa91eebc9e5fb3bc4c646836b40c401244812ee",
      "bytes": 806
    },
    {
      "path": "characters/Hong Jin.md",
      "sha256": "5150284bba214c6b95d660d580a97581d5d87a336b826a4d0c81bfdbcc6599f8",
      "bytes": 837
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "c70903ac0ee90791a6f72b13f499369e1d34bbf2dc643a3553db28b9aab9dc44",
      "bytes": 1244
    },
    {
      "path": "characters/Jeong Hogun.md",
      "sha256": "0c984efe45a9398cb6559fb419092797ce5c621ab78581c0aa294864b1962764",
      "bytes": 628
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "0bd3b0039b9d1efaa81679a62d41d939e7a60828386e4bf1b3f5664e7a08a6f5",
      "bytes": 1290
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "501c9e7f85b5134eaae691a5220c07e8297c17f62f76c23956c965490eac3347",
      "bytes": 622
    },
    {
      "path": "characters/Jung Ho.md",
      "sha256": "3356eeae8654c1b1b1afd06aa27d0e9779c6718ce0f0dd9f5633c197d4145da4",
      "bytes": 699
    },
    {
      "path": "characters/Prince Shangshan.md",
      "sha256": "b2ac9fc10824517604ab947672d264a85aa65efa204303195539f84bde253321",
      "bytes": 998
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "21fe7ebbf3c46e6a6c651cab2cf39578c984d9cc64cf538e5662e8d6ad657b81",
      "bytes": 265353
    }
  ],
  "estimated_tokens": 13245
}
-->

# Durable State Update — Chapter 923

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
1 and safe_through 923. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 923. Profile updates may replace only one
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
  "chapter": 923,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 923,
    "continuity_sources": [923],
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
    "So Gyo is the Bow Saint; her two curved swords can join into the bow’s original form.",
    "So Gyo identifies Jin Taekyung as the Martial God’s chosen one and intends to explain the long story behind it later; her allegiance remains unknown.",
    "The Eastern Heaven Demon Lord remains alive at the scene; he claims Dark Heaven’s agents are spread throughout the land and predicts civil war and an invasion of the Central Plains.",
    "The rebel battle at the grand banquet hall has ended; the apparent ringleaders are being kept alive for questioning.",
    "Ma Sanbao is missing.",
    "The Salcheonmun vowed to pursue Mungyeong regardless of cost or delay and may pursue Jin Taekyung if it learns he killed Gye Yabu.",
    "Jeok Cheongang, Hyuk Mujin, Ju Hwaran, Song Ilseom, Sama Pyo, Taishan, and the Divine Physician survived and reunited with Jin Taekyung.",
    "The Eastern Heaven Demon Lord’s mother and Master were killed; he remembers their suffering vividly but can barely recall their happy faces."
  ],
  "continuity_sources": [
    922
  ],
  "open_questions": [
    "What enabled Jin Taekyung to return from his seemingly fatal injuries?",
    "What is the Eastern Heaven Demon Lord’s condition, and what information does he hold about Dark Heaven and the Lord of Heaven?",
    "Where is Ma Sanbao, and what is his current status?",
    "What does the Martial God’s reference to a chosen one mean for Jin Taekyung, and what story has So Gyo kept to herself?",
    "Will the Salcheonmun pursue Mungyeong or discover that Jin Taekyung killed Gye Yabu?"
  ],
  "safe_through": 922,
  "temporary_decisions": [
    "Keep “Force” for 강기 distinct from “death energy” for 사기."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 궁성     | **Bow Saint**                 | —              |
| 살성     | **Slaughter Saint**           | —              |
| 태원진가   | **Jin Family of Taiyuan**        |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 강호     | **martial world**                                | Prefer “Murim” where the setting itself is meant      |
| 큰형     | **eldest brother**                           |
| 태원     | **Taiyuan**            |
| 백연 | **Baek Yeon** | Commander of the Embroidered Uniform Guard. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 동천마군 | **Eastern Heaven Demon Lord** | Title of the absurd masked antagonist in Jin's nightmare. |
| 홍진 | **Hong Jin** | Level 22 man at the City Lord's luncheon; delicate in appearance and voice. |
| 정호군 | **Jeong Hogun** | Commander of the Embroidered Uniform Guard force confronting Jin. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 정호 | **Jung Ho** | Middle-aged Shaolin martial monk leading the traveling group. |
| 상산왕 | **Prince Shangshan** | The City Lord and a member of the imperial family who orders the luncheon. |
| 송이 | **Song-i** | Short form used for Song Song; Taekyung's love interest. |
| 태자 | **Crown Prince** | Title of the Emperor's older brother who was reportedly assassinated. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 주표 | **Zhu Bao** | Personal name of Prince Shangshan. |
| 황태자 | **Crown Prince** | The Emperor's older brother in Taekyung's recollection. |
| 선황 | **the late Emperor** | The former Emperor whom Hong Jin served. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 성군 | **sage king** | Desired form of rulership proclaimed for Prince Shangshan. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 중독 | **Poisoned** | System status abnormality caused by the poisons. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 독의 | **Poison Physician** | Taekyung's mocking description of Mungyeong after learning how aggressively he uses poison. |
| 저승사자 | **Grim Reaper** | Mungyeong's threatening self-description during the banter. |
| 황족 | **Huang tribe** | Nanman tribe involved in a recently settled dispute. |
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
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 정호 | 진태경 | Shaolin Discipline Hall Master to patient and Benefactor | Benefactor Jin | formal-polite | Jung Ho repeatedly uses 진 시주 and 시주. |
| 진태경 | 정호 | patient to Shaolin Discipline Hall Master | Monk | polite and familiar | Taekyung addresses Jung Ho as 스님. |
| 주표 | 홍진 | prince to loyal subject | you | formal and reassuring | Zhu Bao refers to Hong Jin as 그대 while apologizing for the hardship he has endured. |
| 진태경 | 정호군 | young martial artist to senior imperial officer | Commander Jeong | casual and teasing, then conciliatory | Jin addresses him by rank while trying to defuse the standoff. |
| 주표 | 백연 | prince addressing an imperial military officer | Commander Baek Yeon | formal and authoritative | Addresses Baek Yeon by name and office while insisting that he answer. |
| 백연 | 주표 | imperial officer addressing a prince | Your Highness | formal and deferential | Uses 전하 when apologizing to and answering Prince Shangshan. |
| 백연 | 정호군 | commander to subordinate | you | direct and commanding | Uses 네 while testing Jeong Hogun’s obedience. |
| 홍진 | 백연 | imperial aide confronting a senior military officer | you | angry and confrontational | Uses 당신 in an indignant outburst. |
| 진태경 | 백연 | young martial artist confronting an imperial military commander | you | casual and insulting | Refers to Baek as 이 양반 while challenging his conduct. |
| 진태경 | 상산왕 | protector addressing a young prince | His Highness | respectful royal address | Taekyung refers to the prince as 상산왕 전하 when ordering Mujin to bring him. |
| 정호군 | 상산왕 | imperial guard officer escorting the prince | His Highness | formal and deferential | Hogun formally reports that he has come to escort the prince. |
| 정호군 | 홍진 | Embroided Uniform Guard officer addressing a senior imperial official | Deputy Military Commissioner | formal and admonishing | Hogun tells Hong Jin to mind his words. |
| 진태경 | 황제 | guest of the Emperor’s younger brother addressing the Emperor | Your Majesty | formal and deferential in address, despite blunt challenges | Taekyung repeatedly addresses the Emperor as 폐하. |
| 상산왕 | 황제 | younger brother addressing the Emperor | Your Majesty | deferential royal address | Shangshan addresses the Emperor as 폐하 while pleading for Taekyung. |
| 홍진 | 정호군 | Embroided Uniform Guard officers of equal rank | Thousand Captain Jeong | polite and direct | Hong Jin addresses Jeong Hogun by rank and surname. |
| 백연 | 진태경 | imperial commander confronting a young martial artist | Jin Taekyung | measured and familiar, using 자네 | Baek Yeon cautions Taekyung about his words and asks whether he must cause a scene. |
| 황제 | 진태경 | Emperor addressing a subject and Prince Shangshan’s guest | Jin Taekyung | formal and authoritative | The Emperor addresses Taekyung by his family and personal name before asking what to do with the two officials. |
| 적천강 | 동천마군 | enemies | you | blunt and informal | Jeok Cheongang addresses the Eastern Heaven Demon Lord with hostile familiarity. |
| 동천마군 | 적천강 | enemies | you | informal | The Eastern Heaven Demon Lord speaks to Jeok Cheongang during their duel. |
| 황제 | 동천마군 | former ruler addressing a former subject, now an enemy | you | measured and formal | The Emperor asks why the Demon Lord betrayed his father, the late Emperor. |
| 동천마군 | 황제 | former subject addressing the Emperor, now an enemy | you; you bastards | hostile and contemptuous | He denies ever being loyal to the imperial family and accuses the rulers of betrayal. |
| 진태경 | 동천마군 | young martial artist confronting an enemy | ugly-ass big bro | casual, profane, and taunting | Jin calls out to the Demon Lord after returning to the hall. |
| 동천마군 | 진태경 | enemy recognizing the spear wielder | Jin Taekyung | shouted, informal | The Demon Lord cries Taekyung's name after identifying him as the spear's owner. |
| 황제 | 백연 | Emperor to the imperial court’s foremost military commander and trusted comrade | Baek Yeon | Direct and familiar; framed as a request rather than an order | The Emperor asks Baek Yeon to sound the war drum. |

## Listed compact profiles

### Baek Yeon.md

# Baek Yeon (백연)

- **Safe through:** Chapter 920
- **Aliases:** Blood Envoy
- **Role:** Baek Yeon is the Commander of the Embroidered Uniform Guard, a former martial arts instructor to the Crown Prince, and the Blood Envoy who helped the fourth prince seize the throne and led the purge.
- **Personality:** Politically assured and controlled, he enforces authority with ruthless decisiveness but speaks with striking defiance to the Emperor in private when their shared undertaking is at stake.
- **Voice:** Not established
- **Relationships:** He commands the Embroidered Uniform Guard and serves the Emperor, carrying out the late Emperor’s final command to plan for the future alongside the fourth prince; he treats Taekyung as a dangerous potential obstacle.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 922
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Eastern Heaven Demon Lord.md

# Eastern Heaven Demon Lord (동천마군)

- **Safe through:** Chapter 922
- **Aliases:** None
- **Role:** The Eastern Heaven Demon Lord is a former Maoshan Sect disciple who commands the dead with a bell and has spent half a century infiltrating the imperial court while building a far-reaching rebellion.
- **Personality:** His hatred of rulers is rooted in the loss of his family and the destruction of the Maoshan Sect; the grief endures, while memories of their happiness have faded.
- **Voice:** He speaks in measured, almost lyrical phrasing, recounting the past before turning to pointed accusations.
- **Relationships:** Ma Sanbao is his Disciple; he holds the Emperor responsible for Taizu’s actions against the Maoshan Sect.

### Hong Jin.md

# Hong Jin (홍진)

- **Safe through:** Chapter 899
- **Aliases:** None
- **Role:** Hong Jin is a Level 22 Deputy Military Commissioner of Shanxi Province, a eunuch and trusted aide to Prince Shangshan, and a former member of the East Depot.
- **Personality:** Composed, socially deft, and ambitious, Hong Jin became a eunuch to escape poverty and save his family, then used his abilities to pursue a broader life.
- **Voice:** Delicate and deferential, using formal, self-effacing language with Prince Shangshan.
- **Relationships:** Hong Jin is devoted to Prince Shangshan, whom the late Emperor entrusted to his care; the Fourth Prince spared him because of their old ties, and his longtime friend and former East Depot cohort Ma Sanbao stayed behind in the palace.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 922
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; believes there is no absolute justice and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He deeply trusts Jin Taekyung, his publicly acknowledged second Disciple and intended heir; warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, remains Peng Cheolhu's rival, and is the target of an attack by the assassin Heaven's Slaughter.

### Jeong Hogun.md

# Jeong Hogun (정호군)

- **Safe through:** Chapter 915
- **Aliases:** None
- **Role:** Jeong Hogun is a Thousand Captain of the Embroidered Uniform Guard and a highly skilled martial artist whose force includes dozens of Peak masters.
- **Personality:** Disciplined and resolute, he follows imperial orders without hesitation and reads the political consequences of events with care.
- **Voice:** Formal and rigid, emphasizing duty to imperial authority.
- **Relationships:** Jeong Hogun serves under Baek Yeon’s command in the Embroidered Uniform Guard.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 922
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader.
- **Personality:** Hungry, self-aware, dryly observant, and pragmatic under pressure; accepts extreme personal risk when duty and the lives of others demand it.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; So Gyo says he is the chosen one spoken of by the Martial God, while her allegiance remains unknown.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 922
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Jung Ho.md

# Jung Ho (정호)

- **Safe through:** Chapter 915
- **Aliases:** None
- **Role:** Middle-aged Shaolin martial monk and Master of Shaolin's Discipline Hall who leads the traveling group and wields a Zen staff hung with prayer beads.
- **Personality:** Humble, observant, principled, and concerned with the safety of commoners.
- **Voice:** Formal, restrained, and admonitory, with Buddhist phrasing.
- **Relationships:** Unnamed is his young Martial Uncle; he leads the Shaolin monks traveling with him, addresses Sama Pyo as a Benefactor, and is recognized by Jin Taekyung as Park Jung Ho, a former Garam Middle School classmate.

### Prince Shangshan.md

# Prince Shangshan (상산왕)

- **Safe through:** Chapter 915
- **Aliases:** None
- **Role:** Prince Shangshan, whose personal name is Zhu Bao, is the Emperor’s twelve-year-old youngest younger brother, an exceptionally skilled young swordsman, and the heir publicly designated by the Emperor.
- **Personality:** Earnest and compassionate, he takes responsibility for his loyal subjects’ hardship, admires Jin Taekyung, seeks candid counsel, and shows composure beyond his years in the face of death and political danger.
- **Voice:** Archaic and formal in the manner of a historical drama, with openly eager and childlike reactions beneath his royal diction.
- **Relationships:** Prince Shangshan Zhu Bao is the Emperor’s youngest younger brother; the late Emperor entrusted Hong Jin with his care. Zhu Bao admires Jin Taekyung, seeks to emulate him, and calls him a friend; the Emperor says he will take care of Zhu Bao.

## Korean source

```text
＃923화



죽음 앞에서 두려움을 느끼지 않는 사람이 몇이나 될까.

매우 드물다.

아니, 없다.

물론 천하를 거꾸로 뒤집어 탈탈 털어 보면 몇 명 나올 수도 있겠지만, 양민들과는 궤를 달리하는 간덩이 사이즈를 자랑하는 무림인 중에서도 그런 미친놈은 없을 거라 단언할 수 있다.

자신의 삶을 살아온 한 사람으로서 죽음을 두려워하는 건 그만큼 당연한 일이니까.

치열한 전장에서 무수히 생사를 넘나든 백전노장(百戰老將)도, 아직 솜털도 가시지 않은 애송이도 죽음 앞에서는 누구나 평등하게 공포를 느끼기 마련이다.

더군다나 그 죽음 앞에, 차마 입에 담을 수 없는 끔찍한 고문 풀코스가 예약되어 있다면 더더욱.

하지만 어디에나 예외는 있기 마련이다.

지금 이 순간, 황제의 앞에서 크게 소리 내어 웃고 있는 동천마군처럼.

“으하, 으하하하하!”

사지를 잃고 널브러진 처참한 행색.

그러나 그의 웃음소리는 승자의 그것처럼 쩌렁쩌렁하게 울려 퍼졌다.

몇 번, 혹은 수십 번에 걸쳐 연장했던 완전한 죽음이 비로소 눈앞에 다가왔음에도 지금의 동천마군에게서는 한 줌의 두려움도 찾아볼 수 없었다.

단순히 고통을 느끼지 못하는 몸이라서?

‘아니야.’

설령 괴물이 아닌 평범한 인간이었더라도 그는 지금처럼 웃었을 것이다.

자신의 모든 것을 앗아 간 황실과 대국을 저주하며 기꺼이 고문과 죽음을 받아들였을 것이다.

아득한 세월 속, 동천마군에게 남은 감정은 원통함뿐이니까.

제 손으로 직접 복수를 완성 짓지 못했다는 자책과 후회.

그것이 전부였다.

더할 것도, 뺄 것도 없는 유일한 사실이자 결과였다.

“끝났군. 완전히.”

귓가로 전해지는 적천강의 뇌까림이 의미하는 바는 명백했다.

이제 어떤 달콤한 말과 행동으로도 동천마군에게서 정보를 얻어내는 것은 불가능하다.

광야를 달리는 말이 뒤를 돌아보지 않는 것처럼, 그의 길은 이미 오래전에 정해져 있었으니.

“저런 눈을 가진 놈을 본 적이 있지. 시간 낭비할 필요 없이 당장 숨통을 끊어 후환을 없애는 것만이 상책이다.”

비단 나만을 향한 말이 아니다.

지금의 적천강은 이 자리의 모두에게 말하고 있었다.

같은 전장에서 함께 적과 맞서 싸운 이들에게 그가 보일 수 있는 최대한의 경의이자, 한 사람에게 건네는 제안이었다.

이 광활한 대륙을 지배하는 자.

바로 황제에게.

“폐하.”

머리부터 발끝까지 핏물을 뒤집어쓴 금의위 천호, 정호군이 반 토막 난 검을 들고 앞으로 나섰다.

“부디 하명하시옵소서.”

그러나 황제는 대답하지 않았다.

굳게 입을 다문 채 지친 얼굴로 동천마군을 굽어보던 그가 입을 연 것은, 얼마간의 시간이 흐른 뒤였다.

“어찌 생각하느냐.”

처음에는 몰랐다.

저 물음이 누굴 향한 것인지.

하지만 정확하게 나를 응시하는 황제의 시선과, 뒤이어 둑이 무너지듯 터져 나온 사람들의 반응을 보며 깨달았다.

지금 이 순간 바로 그 황제가, 동천마군의 처우를 다른 누구도 아닌 내게 묻고 있다는 것을.

“폐, 폐하!”

“아니 될 말씀입니다!”

“만천하의 지존이신 폐하께서 조정의 중신도 아닌 일개 백성에게, 그것도 강호의 무뢰배에게 어찌……!”

“강호의 무뢰배라.”

낮게 뇌까린 황제가 주위를 둘러보았다. 어느새 그의 곁에는 관복을 차려입은 대소신료가 사방을 에워싸고 있었다.

황제와 동천마군.

양측이 오직 서로를 향해 집중했기에 상당수가 살아남을 수 있었던 그들의 얼굴을 차례대로 응시하던 황제가 천천히 말을 이었다.

“참으로 희한한 일이다. 그대들이 말하는 강호의 무뢰배는 악전고투를 치르며 저리 피투성이가 되었는데, 조정의 중신들이라는 자들은 이 치열한 전투 속에서도 어찌 그리 멀쩡한 모습들인지.”

“……!”

“……!”

삽시간에 사방이 조용해졌다.

단번에 모두의 입을 닥치게 만든 황제의 고개가 나를 향해 돌아왔다.

“이제 대답해 보아라. 네 생각을 듣고 싶으니.”

모르겠다.

황제가 왜 이 많은 이들 중에 굳이 나를 지목했는지.

또 내게 어떤 대답을 원하는지.

그러나 그 이상으로 깊게 고민하지는 않았다. 언제나 그랬듯이 나는 내 할 말을 하면 되니까.

“만약 제가 저놈을 죽이는 것에 반대한다면, 살려 주실 겁니까?”

누구도 예상치 못했던, 폭탄 같은 한 마디에 헛숨을 삼키는 소리가 곳곳에서 들려온다.

심지어는 동천마군조차 웃음을 그친 채 눈을 부릅떴다.

하지만 황제는 여전히 흔들림 없는 눈빛으로 나를 바라보며 입을 열었다.

“불가(不可).”

“이유가 뭡니까?”

이 얼토당토않은 질문은 정말 몰라서 묻는 것이 아니다.

모두에게 알려 주어야 한다.

설령 이 황궁 밖의 사람들이 모를지라도, 이 자리에 있는 사람들만큼은.

그리고 이런 내 의도를, 황제 역시 짐작하고 있으리라 믿었다.

“저자는 천고의 역적이다. 오랜 세월 동안 아바마마의 눈과 귀를 가리고, 독을 이용하여 황태자 형님을 비롯한 황실 일가 대부분을 천천히 죽음으로 몰아넣었지.”

보이지 않는 동요가 퍼져 나간다.

밝혀지지 않았던 비사(祕史)에 모두가 숨을 죽였다.

지금껏 세상에 알려진 바에 따르면, 모든 악의 축은 황제 그 자신이었으니까.

“짐이 그 사실을 알았을 때는 이미 모든 것이 늦어 있었다. 대국을 무너트리려는 역적들이 황실을 장악하고 대부분의 실권을 틀어쥐고 있었으니.”

그 뒤에 어떤 일이 일어났을지는, 이 자리의 모두가 충분히 유추할 수 있었다.

허수아비로 전락한 황제. 이미 독에 중독되어 버린 황자들.

고귀하고 위대한 핏줄을 이은 그들에게는 더 이상의 시간도, 사람도 없었다.

변함없는 충심으로 금의위를 지켜 낸 어느 노장(老將)과 제위와는 거리가 멀어 외방(外方)을 떠돌았던 대국의 네 번째 황자를 제외한다면.

“남아 있던 방법은 하나뿐이었지.”

그렇게 역모(逆謀)의 탈을 뒤집어쓴 반정(反正)이 일어났다.

십수 년 전 바로 이곳, 대연회장에서.

그렇게 하룻밤 만에 조정의 중신 수백여 명이 죽고, 머지않아 수만 명이 유배되거나 처형당했다.

그리고 사황자는 거침없이 숙청의 칼을 휘둘렀다.

대국을 무너트리려 한 역적들의 시체를 계단 삼아, 만백성의 보이지 않는 눈총과 저주를 뒤로한 채.

한편으로는 머지않아 모든 진실을 밝혀 이 오욕을 씻어 내리라 다짐하며.

“그럼 선황 폐하를 포함한 황족들을 유폐시킨 건…….”

“어떻게든 완치시키고자 했으나 어의(御醫)들조차 자세한 원인을 알지 못했다. 다만 그들이 말하길, 이 천하를 구름처럼 떠돌며 저승사자조차 내쫓는 어느 명의가 있으니 그를 찾는다면 방법이 있을 거라더군.”

“신의(神醫).”

“그래.”

내가 혼잣말처럼 흘린 뇌까림에, 황제가 씁쓸하게 덧붙였다.

“하지만 끝끝내 그를 찾을 수 없었지.”

나 역시 살성에게 직접 들은 적이 있다.

살성과 신의는 천하 각지를 떠돌며 백성들에게 의술을 베풀었고, 그 은덕을 잊지 않은 백성들은 황실의 추적으로부터 그들을 숨겨 주었다는 이야기를.

‘만약 그때 황실이 그들을 찾았다면…….’

역사는 뒤바뀌었을 것이다.

설령 황실에 짙은 죽음의 그림자를 드리운 독의 정체가 혈혼고(血魂蠱)라 해도, 내가 아는 살성과 신의라면 어떻게든 방법을 찾을 수도 있었을 테니까.

하지만 그 공교로운 운명의 끝은 선황과 황태자들을 비롯한 여러 황족들의 죽음이었고, 제위와 동떨어져 있던 사황자는 비로소 완전한 찬탈자이자 패륜아가 되었다.

“왜 밝히지 않은 겁니까? 이 모든 진실을.”

“밝히지 않은 것이 아니라 못한 것이다. 어느 순간부터 짐이 하는 모든 언행은 찬탈자의 변명에 불과했으니까. 마지막 순간에서야 본래의 정신을 되찾으신 아바마마께서 짐에게 선위(禪位)하겠노라 말씀하셨을 때, 비로소 현실을 깨달았지.”

그것은 영원히 지울 수 없는 낙인이었다.

정식으로 선위를 받아 대국의 사황자에서 천하의 지배자가 되었음에도, 사람들은 믿지 못할 진실에 등을 돌렸다.

야심에 눈이 멀어 아비를 옥좌에서 끌어내린 찬탈자.

그것으로도 부족했는지 수많은 가문과 황족들을 죽음으로 몰아간 학살자이자 패륜아.

대국을 파멸의 구렁텅이로 몰아가던 역적들은 충의지사(忠毅志士)가 되었지만, 그와는 반대로 대국을 지키고자 했던 이들은 역한 오물을 뒤집어써야 했다.

그러나…….

그럼에도 불구하고, 계속해서 나아갈 수밖에 없었다.

대국 전체에 그늘을 드리운 이 거대한 잡초를 완전히 뿌리 뽑아야 했으니까.

“황도를 손에 넣고 수많은 역적들을 쳐냈지만, 가장 큰 줄기는 살아남았다. 그날의 반정은 절반의 성공에 불과했어.”

당시의 동천마군은 지금과 같은 괴물이 아니었다.

그는 궁성과 백연에 맞서 싸우다가 회복할 수 없는 극심한 부상을 입었고, 한 가지 거래를 제안했다.

자신의 목숨과 대국 전체의 명운을 맞바꾸자는 거래를.

“짐에게는……. 거부할 수 없는 제안이었지.”

황제가 곧 천하요, 천하의 중심지가 곧 황도라.

그러나 황제와 황도만이 천하의 전부는 아니었다.

그날 동천마군의 숨통을 끊었다면, 대국은 절반으로 나뉘어 거대한 전란(戰亂)에 휩싸였을 것이다.

풍전등화의 위기 앞에서 사황자가 택한 유일한 길은, 이미 오래전 동천마군과 결탁하여 때를 기다리고 있던 이들에게는 또 다른 반란의 명분이었기에.

“그것만큼은 막아야 했다. 더 이상의 피를 흘릴 수는 없었어.”

걸음마와 함께 검을 잡았다.

손아귀의 굳은살이 당연하게 느껴지고, 말고삐의 감촉이 익숙해질 무렵 전장으로 출진했다.

매번 뛰어난 무예와 병법(兵法)으로 일군을 이끌며 큰 공을 세웠으나, 전장에 나설 때마다 마음속으로 읊조리곤 했다.

이 전쟁이 마지막이라고.

마지막이어야 한다고.

제위? 장군으로서의 군공?

필요 없었다.

그것들에 대한 미련은 이미 오래전에 버렸다.

총명하고 선한 큰형님은 능히 성군(聖君)이 될 재목이었고, 그가 수십 차례의 크고 작은 전쟁에 참여한 이유는 자신의 형이 다스릴 새로운 천하가 평안키를 바랐을 뿐이었다.

그저 그뿐이었다.

그런데. 그런데…….

“결국 이렇게 되어 버렸군.”

스릉.

사황자는, 황제는 검을 뽑았다.

무수한 망자들을 베어 넘겼음에도 피 한 방울 묻지 않은 오색창연한 검신 너머로 나를 바라보며 물었다.

“태원진가의 진태경. 네게 다시 물으마. 짐이 저자를 죽임에 있어, 더 이상의 이유가 필요한가?”

내가 대답했다.

“말씀하신 것만으로 충분합니다.”

복수의 순간만을 기다려온 것은 비단 한 사람뿐만이 아니다.

“그럼 되었다.”

담담하지만 한편으로는 끓어오르는 대답과 함께, 황제는 검을 내리그었다.

가족의 원수를 향해.

나라와 백성을 도탄에 빠트리려 한 만고의 역적을 향해.

아니, 내리그으려 했다.

황제의 보검이 일도양단의 기세로 나아가던 그 순간, 누군가의 낭랑한 목소리가 울려 퍼지기 전까지는.

“아직, 한 가지가 빠졌습니다.”

쉬익!

날카로운 파공성이 불었다.

동천마군의 목젖에 닿기 직전 아슬아슬하게 검을 멈춰 세운 황제가, 내가, 이 자리의 모두가 고개를 돌렸다.

그리고 보았다.

군데군데 피가 묻은 의복을 걸친 채, 침착하면서도 슬픈 눈빛을 한 어느 소년을.

상산왕 주표.

모두의 시선이 어린 왕을 향하고 있었지만, 어린 왕은 오직 한 사람을 바라보고 있었다.

아직 성장이 덜 끝난 자그마한 발걸음 역시도.

“전하. 전하!”

지금껏 보이지 않던 얼굴.

아마도 전투가 시작됨과 동시에 주인의 곁으로 향했을 홍진이 다급하게 그를 불렀지만, 상산왕 주표는 발걸음을 멈추지 않았다.

사박.

한 걸음.

사박.

또 한 걸음.

누구도 그를 막지 못했다.

지금 이 순간 모두의 눈동자에 비친 소년은 사내였다.

어린 왕이 아닌 또 한 명의 군주였다.

그리고 그 사내이자 군주의 고개가, 천천히 숙여졌다.

죽음 앞에서도 완전히 분노를 벗어던지지 못한 한 사람을 향해.

다름 아닌 자신의 부모와 형제를 죽인 원수를 향해.

스륵.

옷자락이 피 웅덩이를 스쳤다. 동천마군을 향해 깊게 허리를 굽힌 상산왕이 입을 열었다.

“미안하오. 당신에게는 어떤 위로도 되지 않겠지만……. 내 조부께서 하신 일에 대해 진심으로 사과드리겠소.”

“……!”

“……!”

모두가 할 말을 잃었다.

나도, 황제도, 궁성과 화왕도.

그리고, 동천마군조차도.

“아.”

벌어진 입술 사이로 흘러나온 나직한 신음.

떨리는 눈빛으로 상산왕을 바라보던 그가 이내 흐릿하게 웃었다.

“참으로 빌어먹을 일이로군.”

푹!

살갗에 닿아 있던 검신이, 그의 목을 파고들었다.
```

## Final English reading copy

```markdown
# Chapter 923

How many people feel no fear in the face of death?

Very few.

No—none.

Of course, if you turned the whole world upside down and shook it out, you might find a few. But I can say with certainty that even among Murim warriors, whose guts are in a league of their own compared to ordinary people, there isn’t a madman like that.

After all, it’s only natural for someone who has lived their life to fear death.

Whether it’s a battle-hardened veteran who’s crossed the line between life and death countless times on brutal battlefields, or a green kid whose baby fat hasn’t even faded, everyone feels fear in the face of death.

All the more so when a full course of unspeakably horrific torture awaits you before death.

But there are exceptions to everything.

Like the Eastern Heaven Demon Lord, laughing loudly before the Emperor at this very moment.

“Ha! Hahahahaha!”

He was a wretched sight, sprawled on the ground with all four limbs gone.

But his laughter rang out like that of a victor.

Though the complete death he’d delayed once, or perhaps dozens of times, had finally come within reach, there wasn’t a trace of fear in the Eastern Heaven Demon Lord now.

Was it simply because his body couldn’t feel pain?

*No.*

Even if he’d been an ordinary human instead of a monster, he would have laughed just the same.

He would have cursed the imperial court and the Great Nation that had taken everything from him, and gladly accepted torture and death.

After all those distant years, the only emotion the Eastern Heaven Demon Lord had left was bitterness.

Self-reproach and regret that he hadn’t been able to complete his revenge with his own hands.

That was all.

The sole truth and outcome, with nothing to add or take away.

“It’s over. Completely.”

The meaning behind Jeok Cheongang’s muttering was clear.

No amount of sweet talk or kind gestures could get information out of the Eastern Heaven Demon Lord now.

Like a horse galloping across a wilderness without looking back, his path had been set long ago.

“I’ve seen eyes like that before. There’s no need to waste time. The only sensible thing is to cut off his breath now and eliminate the threat.”

He wasn’t speaking only to me.

Jeok Cheongang was speaking to everyone here.

It was the greatest respect he could show the people who had fought beside him on the same battlefield—and a proposal addressed to one man.

The ruler of this vast continent.

The Emperor.

“Your Majesty.”

Jeong Hogun, a Thousand Captain of the Embroidered Uniform Guard, stepped forward. Blood covered him from head to toe, and he held a sword broken in half.

“Please, give your command.”

But the Emperor didn’t answer.

He kept his lips pressed shut, gazing down at the Eastern Heaven Demon Lord with an exhausted face. Only after some time had passed did he speak.

“What do you think?”

At first, I didn’t know who he was asking.

But as the Emperor’s gaze settled squarely on me, and the people around us erupted as if a dam had burst, I understood.

At this very moment, the Emperor was asking me—not anyone else—what should be done with the Eastern Heaven Demon Lord.

“Y-Your Majesty!”

“You mustn’t!”

“How could Your Majesty, the sovereign of all under Heaven, ask an ordinary subject—one of those lawless ruffians from the martial world, no less—”

“Lawless ruffians from the martial world, you say.”

The Emperor muttered softly and looked around. Before I knew it, officials in full court dress had surrounded him on every side.

The Emperor turned his gaze from one face to the next. The Emperor and the Eastern Heaven Demon Lord had been so focused entirely on each other that many of these officials had survived. Then the Emperor continued, slowly.

“It is a strange thing. The martial-world ruffian you speak of fought desperately and ended up covered in blood, while you ministers of the court somehow look untouched after such a fierce battle.”

“……”

“……”

Silence fell in an instant.

The Emperor’s words shut everyone up. He turned his head toward me.

“Now answer me. I want to hear what you think.”

I didn’t know.

I didn’t know why, out of all these people, the Emperor had singled me out.

Or what answer he wanted from me.

But I didn’t dwell on it. As always, I could just say what I had to say.

“If I opposed killing him, would you let him live?”

A single, explosive question that no one had expected. I heard people around us catch their breath.

Even the Eastern Heaven Demon Lord stopped laughing and opened his eyes wide.

But the Emperor looked at me without wavering and answered.

“No.”

“Why not?”

I wasn’t asking because I truly didn’t know the answer to this outrageous question.

Everyone needed to know.

Even if no one outside the imperial palace ever learned the truth, the people here needed to hear it.

I believed the Emperor understood that much, too.

“He is a traitor without equal in all history. For many years, he blinded and deafened My Father, and used poison to slowly drive most of the imperial family—including My Crown Prince Brother—to their deaths.”

A ripple of shock spread through the crowd.

Everyone held their breath at the hidden history that had never been revealed.

As far as the world knew, the root of all evil was the Emperor himself.

“When I learned the truth, it was already too late. Traitors who sought to bring down the Great Nation had seized control of the imperial family and tightened their grip on most of the real power.”

Everyone here could imagine what had followed.

An Emperor reduced to a puppet. The princes already poisoned.

There was no more time, no more people for those born of a noble and great bloodline to rely on.

Except for one old general who had protected the Embroidered Uniform Guard with unwavering loyalty, and the Great Nation’s fourth prince, who was far from the throne and had been wandering the provinces.

“There was only one way left.”

And so came a restoration disguised as a rebellion.

More than a decade ago, right here in this grand banquet hall.

In a single night, several hundred high-ranking court officials died. Before long, tens of thousands more were exiled or executed.

And the fourth prince wielded the sword of purging without hesitation.

He climbed the bodies of the traitors who had tried to destroy the Great Nation, with the unseen glares and curses of its people at his back.

All the while, he swore that one day soon he would reveal the whole truth and wash away this disgrace.

“Then, the reason the late Emperor and the other members of the imperial family were confined…”

“We tried every way we could to cure them, but even the Imperial Physicians couldn’t determine the cause. They said there was a great physician who wandered the world like a cloud, driving away even the Grim Reaper. If we could find him, they said, there might be a way.”

“The Divine Physician.”

“Yes.”

The Emperor added bitterly to my mutter, spoken almost to myself.

“But in the end, I could never find him.”

I’d heard it directly from the Slaughter Saint, too.

The Slaughter Saint and the Divine Physician had wandered all across the land, treating the people. The people, never forgetting their kindness, had hidden them from the imperial court’s search.

*If the imperial court had found them then…*

History would have changed.

Even if the poison that cast its long shadow of death over the imperial family had been the Blood Soul Gu, the Slaughter Saint and the Divine Physician I knew might have found some way to deal with it.

But the cruel twist of fate ended with the deaths of the late Emperor, the crown princes, and several other members of the imperial family. The fourth prince, who had been far removed from the throne, became a usurper and a parricide in every sense.

“Why didn’t you reveal it? The whole truth?”

“It wasn’t that I didn’t reveal it. I couldn’t. At some point, everything I said and did amounted to nothing more than a usurper’s excuse. Only when My Father regained his senses at the very end and told Me he would abdicate in My favor did I finally understand the reality.”

It was a stain that could never be erased.

Even after the fourth prince had formally succeeded to the throne and become the ruler of all under Heaven, people turned their backs on a truth they couldn’t believe.

A usurper, blinded by ambition, who had dragged his father from the throne.

As if that weren’t enough, a murderer and parricide who had led countless families and members of the imperial clan to their deaths.

The traitors who had driven the Great Nation toward ruin became loyal patriots. Meanwhile, those who had tried to protect it had to wear the stench of filth.

And yet…

Even so, he had no choice but to keep moving forward.

He had to tear out this enormous weed that cast its shadow over the entire Great Nation.

“I took the capital and purged countless traitors, but the main root survived. That restoration was only half a success.”

The Eastern Heaven Demon Lord hadn’t been the monster he was now.

He’d fought against the Bow Saint and Baek Yeon, and suffered injuries so severe he could never recover. Then he proposed a deal.

A bargain: his life in exchange for the fate of the entire Great Nation.

“For Me… it was an offer I couldn’t refuse.”

The Emperor was the realm, and the capital was the heart of the realm.

But the Emperor and the capital weren’t all there was to the realm.

If the Eastern Heaven Demon Lord had been killed that day, the Great Nation would have split in two and plunged into a massive war.

With the country hanging by a thread, the only path the fourth prince could choose would have given those who had conspired with the Eastern Heaven Demon Lord long ago, and had waited for the right moment, another excuse to rebel.

“I had to stop that. I couldn’t let any more blood be spilled.”

He’d taken up the sword as soon as he could walk.

By the time the calluses on his hands felt natural and the reins were familiar to his touch, he was marching off to war.

Time and again, he’d led armies with outstanding martial skill and strategy, earning great victories. But whenever he went to the battlefield, he would murmur to himself:

*This will be the last war.*

*It has to be the last.*

The throne? Military honors as a general?

He didn’t need any of it.

He’d given up on those things long ago.

His brilliant, kind eldest brother had all the makings of a sage king. The only reason he’d taken part in dozens of great and small wars was that he wanted the new world his brother would rule to be peaceful.

That was all.

And yet. And yet…

“So this is how it ended.”

*Shing.*

The fourth prince—the Emperor—drew his sword.

Through the richly colored blade, not stained with a drop of blood despite having cut down countless dead, he looked at me and asked:

“Jin Taekyung of the Jin Family of Taiyuan. I ask you once more. Do I need any further reason to kill him?”

I answered.

“What you’ve told us is enough.”

He wasn’t the only one who had been waiting for the moment of revenge.

“Then that settles it.”

His answer was calm, but heat simmered beneath it. The Emperor brought his sword down.

Against the enemy of his family.

Against the traitor of all time, who had plunged his country and its people into misery.

Or rather, he was about to bring it down.

The Emperor’s treasured sword was moving with enough force to split the man in two when a clear young voice rang out.

“One thing is still missing.”

*Whoosh!*

A sharp sound cut through the air.

The Emperor stopped his sword just short of the Eastern Heaven Demon Lord’s throat. He, I, and everyone else turned our heads.

And saw him.

A boy in clothes stained here and there with blood, his eyes calm and sad.

Prince Shangshan, Zhu Bao.

Everyone was looking at the young prince, but the young prince was looking at only one person.

Even his small steps, with his growing years not yet behind him, carried him forward.

“Your Highness! Your Highness!”

Hong Jin, a face that hadn’t been visible until now, called after him in a panic. He must have gone to his master’s side as soon as the battle began. But Prince Shangshan didn’t stop walking.

*Step.*

One step.

*Step.*

Another.

No one could stop him.

At that moment, the boy reflected in everyone’s eyes was a man.

Not a young prince, but another ruler.

And the man, the ruler, slowly bowed his head.

Toward a man who hadn’t been able to cast off all his fury, even in the face of death.

Toward the enemy who had killed his parents and brothers.

*Swish.*

The hem of his clothes brushed against a pool of blood. Prince Shangshan bent deeply toward the Eastern Heaven Demon Lord and spoke.

“I’m sorry. I know this won’t comfort you, but… I sincerely apologize for what my grandfather did.”

“……”

“……”

Everyone was left speechless.

Me, the Emperor, the Bow Saint, and the Fire King.

Even the Eastern Heaven Demon Lord.

“Ah.”

A quiet groan slipped between his parted lips.

He stared at Prince Shangshan with trembling eyes, then gave a faint smile.

“What a damnable thing.”

*Thud!*

The blade that had been resting against his skin pierced his throat.
```

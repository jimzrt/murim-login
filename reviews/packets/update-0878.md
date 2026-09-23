<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0878.txt",
      "sha256": "b085f2c039578b75f1bc981af00394332d44cf082a08e6e403c22de8c5950ef4",
      "bytes": 13182
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "3cbe47bf8a7c35722ed4abeeff446af8f055d1c368b63f166d3699e04b325e9e",
      "bytes": 1958
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "77f7f9625d663fdeec408b3696199ba3f21d98f335ae9eae4e9465caec345d0f",
      "bytes": 230213
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "5446126467a74d89b13b9613379479e188c1a71b95dda297fdf51f9b25d2ad97",
      "bytes": 759
    },
    {
      "path": "characters/Hong Jin.md",
      "sha256": "891d06e8395b7f35035c50f4eb4082636913a9271864fe8d2ba5de458e2d8c0b",
      "bytes": 837
    },
    {
      "path": "characters/Human Butcher.md",
      "sha256": "d79679d14ce5b252f53df8ca8bb10ab2581debc53faf81c701284c0e650a434c",
      "bytes": 667
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "91e603099d6105379f80ea1ca996e55278dbc8c46b19fd654f8242b952eed09c",
      "bytes": 1511
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "330e40f40057700a658fd560e57a5a9ed71c39634b3ec4f6f0830ae147a64a4c",
      "bytes": 1782
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "0624e3afd81f243d7fe30310b07a235f09f07f93bfd5467083df73d748f95400",
      "bytes": 622
    },
    {
      "path": "characters/Namho.md",
      "sha256": "33f74663922f5d43b0f5f606bd28f33d1411021bd9c4bdc13af979e90b972a15",
      "bytes": 973
    },
    {
      "path": "characters/Prince Shangshan.md",
      "sha256": "069de09d0a414f24bbf7b9110612973b0312b3d71baa449e338d13dd3646cbe4",
      "bytes": 952
    },
    {
      "path": "characters/Sama Pyo.md",
      "sha256": "96bef3aa79cd408c573b68608b3b631533cd6505654e8f6c72018d5884af792e",
      "bytes": 936
    },
    {
      "path": "characters/Song Il.md",
      "sha256": "8dc9e5241913d7c07943b0af3b15859f3c05a777cc171533777ce763fcef11a3",
      "bytes": 964
    },
    {
      "path": "characters/Song Ilseom.md",
      "sha256": "9722a67b6859126f53be625baaf4975b359271b7b1bae3703a9b11ca695daaea",
      "bytes": 1074
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "12b0a3b35e85436437b5c82856d853dff31449970144a556568ca1a7bccbf7be",
      "bytes": 787
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "d9384e9ac1b5e8435b4526eb3ad43743df747a3184af7f49792e9027db164ec5",
      "bytes": 258472
    }
  ],
  "estimated_tokens": 14000
}
-->

# Durable State Update — Chapter 878

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
1 and safe_through 878. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 878. Profile updates may replace only one
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
  "chapter": 878,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 878,
    "continuity_sources": [878],
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
    "The Emperor has confined Prince Shangshan in Qianqing Palace; Taekyung returned without him.",
    "Taekyung gave Shangshan the Myriad-Poison Ring for protection against poisoning.",
    "The palace attendants assigned to Shangshan are First Rate martial artists who carry flexible swords.",
    "Taekyung suspects the Emperor is connected to Dark Heaven, but this is unconfirmed.",
    "Hong Jin believes Aehyang is very likely pregnant; the pregnancy and the Emperor’s plans remain unconfirmed.",
    "The late Emperor died after a period of mental confusion while in confinement; Taekyung suspects Blood Soul Gu may have been involved, but this is unconfirmed.",
    "The City Lord of Sichuan Province showed strange symptoms before his death, and Blood Soul Gu was found in his corpse.",
    "Hong Jin plans to contact Ma Sanbao about Shangshan’s danger and has received a personal request from Taekyung whose contents are not revealed.",
    "Jeok Cheongang is undercover at the Hyuk Family Textile Shop in Hangzhou and has received a message claiming to be from the Blazing Flame Divine Dragon."
  ],
  "continuity_sources": [
    876,
    877
  ],
  "open_questions": [
    "Is Aehyang pregnant, and what does the Emperor intend for her and Shangshan?",
    "Did the Emperor or Dark Heaven use Blood Soul Gu against the late Emperor and the City Lord of Sichuan Province?",
    "Will the Myriad-Poison Ring protect Shangshan from Blood Soul Gu?",
    "What personal task has Taekyung asked Ma Sanbao to perform?",
    "Who brought Jeok Cheongang the message, and what does it say?"
  ],
  "safe_through": 877,
  "temporary_decisions": [
    "Render 기관진식 as “mechanisms and formations”; retain “Third Shadow,” “First Shadow,” “No Shadow,” and “Marquis Within the Passes.”",
    "Use “imugi,” not “dragon,” for the creature Taekyung killed at Dongting Lake."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 송일     | **Song Il**        |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 양기     | **yang qi**                                      |                                                       |
| 보법     | **manoeuvre technique** / **footwork technique** | Named Jin technique uses “Manoeuvre”                  |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 낭인     | **wandering martial artist**                     |                                                       |
| 제자     | **Disciple**                                 |
| 생도     | **cadet**                                    |
| 몬스터     | **monster**           |
| 산서     | **Shanxi**             |
| 노부      | **this old man / I**                                            |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 소저      | **Young Lady**                                                  |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 홍진 | **Hong Jin** | Level 22 man at the City Lord's luncheon; delicate in appearance and voice. |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 남호 | **Namho** | Hidden Shadow Pavilion code name; literally associated with amber from the south. |
| 상산왕 | **Prince Shangshan** | The City Lord and a member of the imperial family who orders the luncheon. |
| 사마표 | **Sama Pyo** | Young Sect Leader of the Black Dragon Demon Gate. |
| 송일섬 | **Song Ilseom** | Young escort captain of the Yongbong Escort Bureau; distinct from Song Il of Zhongnan. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 금나수 | **grappling technique** | Close-combat wrist-lock technique; rendered descriptively |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 주신 | **God of Drinking** | Wipeng's drinking epithet. |
| 촉금 | **Shu brocade** | Fine brocade brought from Sichuan. |
| 도지휘동지 | **Deputy Military Commissioner** | Second-rank military office held by Eunuch Hong |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 인피면구 | **human-skin mask** | Disguise made from peeled human facial skin. |
| 삼매진화 | **Samadhi True Fire** | Internal-energy flame demonstrated by the unnamed old man. |
| 허공섭물 | **Seizing an Object Through Empty Space** | Technique Jeok Cheongang uses to lift Jang Taebo remotely. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 내가고수 | **I'm a Master** | System Title granted to Taekyung. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 살수 | **assassin** | Professional killer considered as a possible suspect. |
| 열화신룡 | **Blazing Flame Divine Dragon** | New sobriquet bestowed on Jin Taekyung. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 촌각 | **moments** | Short intervals disappearing from Jeok's day. |
| 고든 | **Gordon** | Pentagon employee tasked with repairing smashed warning lights. |
| 만족 | **Man people** | An ethnic group mentioned by the Poison Flower Pavilion owner. |
| 신인 | **divine man** | Descriptive term for a human who became something beyond humanity. |
| 전서 | **missive** | A written message exchanged or delivered in secret. |
| 진화 | **evolution** | The transformation the Southern Heaven Demon Empress claims the rift will produce. |
| 화신 | **Fire God** | A local deity worshiped by one Nanman believer. |
| 선계 | **realm of immortals** | The other world that Jin travels to and from. |
| 동창 | **East Depot** | Imperial agency named by Hong Jin. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 홍진 | 진태경 | political_host_to_young_martial_artist | Young Hero Jin; Young Master Jin; Sleeping Dragon of Shanxi | polite, coaxing, and probing | Uses respectful forms while steering Taekyung toward relaying the Escort Bureau proposal and teasing him with the Seongun Escort Bureau. |
| 진태경 | 홍진 | young_martial_artist_to_political_official | Comrade Chairman—no, Deputy Military Commissioner | casual and teasing, then formally corrective | Deliberately jokes with an inappropriate title before correcting himself to Hong Jin's official office. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 송일 | 진태경 | hostile Zhongnan Elder to accused outsider | you / Jin Taekyung | hostile and threatening | Song Il questions Taekyung's identity and later threatens him over Gong Ilhyuk's injury. |
| 송일 | 적천강 | former rescued junior to former rescuer | Great Hero Jeok | formal, fearful, and defensive | Uses 적 대협 while insisting that Jeok has no business interfering in the dispute. |
| 적천강 | 송일 | former rescuer to former rescued junior | Zhongnan brat; you; insolent bastard | blunt, mocking, and humiliating | Jeok recalls Song's youthful arrogance and addresses him with contempt while publicly disciplining him. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 중년인 | 진태경 | veteran civilian Hunter to celebrated allied Hunter | Mr. Jin | formal-polite and awed | The casualty clerk addresses Jin as 진 선생님 after Jin asks him to list Lei Fei among the dead. |
| 진태경 | 중년인 | celebrated Hunter to older fellow Hunter | sir | casual and teasing | Jin addresses the older Hunter as 아저씨 while joking with him and giving him instructions. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 사마표 | 태산 | Young Sect Leader to subordinate | Taishan | informal and patronizing | Sama Pyo calls Taishan by name while ordering him to leave. |
| 태산 | 사마표 | subordinate to Young Sect Leader | Lord | crude and deferential | Taishan uses 주군 while obeying Sama Pyo. |
| 태산 | 진태경 | subordinate_to_respected_outsider | Jin Taekyung | clipped and familiar | Taishan says he likes Jin Taekyung but will fight him without hesitation if Sama Pyo commands it. |
| 사마표 | 적천강 | Young Sect Leader to legendary elder | Great Hero Jeok | formal-deferential | Sama Pyo formally pays his respects to Jeok Cheongang as the Fire King. |
| 태산 | 적천강 | subordinate of a Young Sect Leader to legendary elder | Fire King | clipped, childlike, and deferential | Taishan gives his awkward greeting and expresses admiration for Jeok's strength. |
| 적천강 | 사마표 | legendary elder to unorthodox Young Sect Leader | you / young brat | blunt, suspicious, and contemptuous | Jeok addresses Sama Pyo with 네놈 and 어린놈 while probing his lineage and motives. |
| 적천강 | 태산 | legendary elder to giant subordinate | you / strange fellow | blunt, startled, and grudgingly tolerant | Jeok addresses Taishan as 네놈 while reacting to his greeting and appetite. |
| 사마표 | 진태경 | prospective recruit to pavilion master | you | polite, controlled, and candid | Sama Pyo uses 자네 while asking about Taekyung's attitude and admitting his intention to use him. |
| 진태경 | 사마표 | pavilion master to prospective recruit | you / that guy | blunt, informal, and distrustful | Taekyung speaks to and about Sama Pyo with casual forms such as 녀석 and 저놈. |
| 진태경 | 송일섬 | pavilion master to prospective member | Song Ilseom | direct and evaluative | Taekyung directly names Song Ilseom while comparing his qualifications with Hwaran's. |
| 송일섬 | 사마표 | fellow_pavilion_member_to_hostile_fellow_member | you | hostile and casual | Song Ilseom discusses fighting Sama Pyo and answers him while preparing to move away. |
| 사마표 | 송일섬 | fellow_pavilion_member_to_hostile_fellow_member | you | controlled and antagonistic | Sama Pyo responds to Song Ilseom's accusations and proposes moving aside to fight. |
| 남호 | 진태경 | Hidden_Shadow_Pavilion_agent_to_mission_leader | Jin Taekyung / you | guarded and familiar | Namho addresses Taekyung as 자네 while explaining the contact and offering guidance. |
| 진태경 | 남호 | mission_leader_to_hidden_shadow_agent | you / Namho | probing and respectful | Taekyung questions Namho’s affiliation and later discusses Dark Heaven’s threat to Nanman. |
| 남호 | 태산 | guide_to_pavilion_member | Taishan | blunt and exasperated | Namho directly rebukes Taishan for eating the poisonous blood-feeding fungus. |
| 남호 | 사마표 | guide_to_young_sect_leader | Young Sect Leader | blunt and admonishing | Namho warns Sama Pyo that all grass and animals in the territory belong to the Nanman Beast Palace. |
| 사마표 | 남호 | young_sect_leader_to_guide | Elder Namho | formal and apologetic | Sama Pyo apologizes after Taishan attempts to seize the calf. |
| 진태경 | 태산 | pavilion_master_to_pavilion_member | Taishan | forceful and commanding | Taekyung orders Taishan to stop eating the bear. |
| 태산 | 남호 | Fire Dragon Pavilion member to guide | Namho | clipped, childlike, and informal | Taishan directly addresses Namho while asking what Dark Heaven is. |
| 진태경 | 상산왕 | protector addressing a young prince | His Highness | respectful royal address | Taekyung refers to the prince as 상산왕 전하 when ordering Mujin to bring him. |
| 중년인 | 상산왕 | unknown imperial subject addressing a prince | His Highness, Prince Shangshan | formal and deferential | Addresses him as 상산왕 전하 while remarking on seeing him grown. |
| 진태경 | 황제 | guest of the Emperor’s younger brother addressing the Emperor | Your Majesty | formal and deferential in address, despite blunt challenges | Taekyung repeatedly addresses the Emperor as 폐하. |
| 상산왕 | 황제 | younger brother addressing the Emperor | Your Majesty | deferential royal address | Shangshan addresses the Emperor as 폐하 while pleading for Taekyung. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 877
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Hong Jin.md

# Hong Jin (홍진)

- **Safe through:** Chapter 877
- **Aliases:** None
- **Role:** Hong Jin is a Level 22 Deputy Military Commissioner of Shanxi Province, a eunuch and trusted aide to Prince Shangshan, and a former member of the East Depot.
- **Personality:** Composed, socially deft, and ambitious, Hong Jin became a eunuch to escape poverty and save his family, then used his abilities to pursue a broader life.
- **Voice:** Delicate and deferential, using formal, self-effacing language with Prince Shangshan.
- **Relationships:** Hong Jin is devoted to Prince Shangshan, whom the late Emperor entrusted to his care; the Fourth Prince spared him because of their old ties, and his longtime friend and former East Depot cohort Ma Sanbao stayed behind in the palace.

### Human Butcher.md

# Human Butcher (인도)

- **Safe through:** Chapter 876
- **Aliases:** None
- **Role:** Former mysterious Han Chinese mounted-bandit power in Northern Gaoyuan commanding fifty subordinates; a Peak master killed by an unnamed old man in a single move
- **Personality:** Cold, intimidating, and murderous; he kills people as though slaughtering livestock
- **Voice:** Cold, curt, and quietly threatening
- **Relationships:** He is one of four powerful participants at the Northern Gaoyuan gathering, intimidates Temur, and has claimed Ghost Sword Wipeng as his personal target in the proposed attack

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 877
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm, the occupant of the chief seat of the Murim Alliance's Five Kings Hall, and a trusted confidant who accepts Jin as himself despite knowing that he travels between Murim and another world resembling the realm of immortals.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He deeply trusts his publicly acknowledged Disciple and intended heir Jin Taekyung, warmly regards Ju Hwaran and hopes she and Jin grow closer, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and remains Peng Cheolhu's rival.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 876
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader.
- **Personality:** Hungry, self-aware, dryly observant, and pragmatic under pressure; accepts extreme personal risk when duty and the lives of others demand it.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; they trust each other deeply, though their bond remains unformalized. Cheongpung is his trusted companion and only true martial rival; Choi Minwoo is his subordinate and trusted manager of media and official arrangements as well as the Peace Guild's Guild Master; Ju Hwaran is a trusted Fire Dragon Pavilion member; Magic Johnson and Chuck Hagel are allied to him; his mother and sister Hayeon are among those he protects; the Skeleton King is his friend and ally; Xiao Shen regards him as an older brother; Jin-ho is his older friend and trusted confidant; he once saved Ju Wongong’s life.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 876
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Namho.md

# Namho (남호)

- **Safe through:** Chapter 855
- **Aliases:** Elder Chao
- **Role:** Namho is an eighty-year-old non-Han Hidden Shadow Pavilion agent who spent more than fifty years undercover in Nanman and maintained contact with Central Plains intelligence through the Pavilion’s Hidden Thread; he now guides the Fire Dragon Pavilion.
- **Personality:** Duty-bound, pragmatic, and observant; uses theatrical violence to protect intelligence work and takes a veteran’s concern for the younger generation’s resolve.
- **Voice:** Measured and reflective when advising the younger generation, loudly abusive when maintaining his local cover, and capable of theatrical boasts and dry humor.
- **Relationships:** Namho is a Hidden Shadow Pavilion contact for Jin Taekyung and the Fire Dragon Pavilion, receives intelligence from the Pavilion Master, and knows the code used by the Thousand-Faced Fox.

### Prince Shangshan.md

# Prince Shangshan (상산왕)

- **Safe through:** Chapter 877
- **Aliases:** None
- **Role:** Prince Shangshan, whose personal name is Zhu Bao, is the Emperor’s twelve-year-old youngest younger brother and an exceptionally skilled young swordsman.
- **Personality:** Earnest and compassionate, he takes responsibility for his loyal subjects’ hardship, admires Jin Taekyung, seeks candid counsel, and shows composure beyond his years in the face of death and political danger.
- **Voice:** Archaic and formal in the manner of a historical drama, with openly eager and childlike reactions beneath his royal diction.
- **Relationships:** Prince Shangshan Zhu Bao is the Emperor’s youngest younger brother; the late Emperor entrusted Hong Jin with his care. Zhu Bao admires Jin Taekyung, seeks to emulate him, and calls him a friend; the Emperor says he will take care of Zhu Bao.

### Sama Pyo.md

# Sama Pyo (사마표)

- **Safe through:** Chapter 855
- **Aliases:** Black Dragon Saber
- **Role:** Young Sect Leader of the Black Dragon Demon Gate, a Morning Star reputed to be no less than the Ten Dragons and Phoenixes, and a member of the Fire Dragon Pavilion.
- **Personality:** Outwardly courteous and smiling, inwardly calculating, but genuinely protective of Taishan; in combat he is ruthlessly pragmatic, survival-focused, and unafraid to stake his life.
- **Voice:** Polite and ingratiating in public, with sardonic humor and controlled evasiveness.
- **Relationships:** Sama Pyo commands the absolutely loyal Taishan, is Sima Gong's son, was Ju Hwaran's former fiancé in a political engagement, and has joined the Fire Dragon Pavilion while openly intending to use Jin Taekyung as a useful card; he is now openly hostile toward fellow member Song Ilseom.

### Song Il.md

# Song Il (송일)

- **Safe through:** Chapter 855
- **Aliases:** Roaring Fury Swordsman
- **Role:** Elder of the Zhongnan Sect and the Roaring Fury Swordsman; senior brother of Sect Leader Gong Iljung; came to the Jin Family of Taiyuan to demand redress for Gong Ilhyuk's injury and the alleged insult to Zhongnan; attacked Jin Taekyung with the Heavenly River Thirty-Six Swords, was stopped by Jeok Cheongang, and was publicly humiliated by him.
- **Personality:** Arrogant, domineering, punitive, and confident in his martial power and seniority.
- **Voice:** Gruff, cutting, condescending, and threatening, with formal authority used to pressure those beneath him.
- **Relationships:** Gong Iljung is his junior Sect Leader and martial younger brother; Gong Ilhyuk is a junior Disciple of his sect; he recognizes Baek Museong and Cheongpung through their Huashan and Sword Saint connections.

### Song Ilseom.md

# Song Ilseom (송일섬)

- **Safe through:** Chapter 855
- **Aliases:** Escort Captain Song
- **Role:** Level 110 young escort captain of the Yongbong Escort Bureau, one of its Dragon-Phoenix Three Escorts, and a newly accepted member of Jin Taekyung and Cheongpung’s Fire Dragon Pavilion; he is currently bound and unconscious under the reconnaissance squad's guard after being struck at a Sleep Acupoint.
- **Personality:** Blunt, decisive, survival-hardened, and dryly self-aware, with little patience for insults or disorder and practical survival skills such as making disguise masks.
- **Voice:** Forceful and urgent in command, with a rough and confrontational edge.
- **Relationships:** He serves under Ju Hwaran and has expressed concern that she not be hurt or die needlessly; he is Song Pyosan’s son, his grandmother was the surviving Guangdong Chen child rescued by Ju Gongsan during the Great Faction War, and he remains openly hostile toward fellow Fire Dragon Pavilion member Sama Pyo.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 855
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion; he helped Jin escape the underground prison by blocking the stairs and overpowering the Bai warriors.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo; becomes explosively violent when his meat is threatened.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord, trusts Jin Taekyung as Pavilion Master, and has grown attached to the Fire Dragon Pavilion members.

## Korean source

```text
＃878화



귓가를 파고든 전음(傳音)을 들은 직후, 적천강이 보인 움직임은 실로 기민하면서도 자연스러웠다.

“아, 최상급의 촉금(蜀錦)을 찾는다고? 그럼 진작 말씀하셨어야지. 안으로 들어오쇼.”

“아니, 잠깐만. 나는 그저…….”

손님으로 위장한 사내는 뭐라 항변하려 했지만, 손목으로부터 전해지는 적천강의 무시무시한 기운에 입을 딱 벌렸다.

“흡.”

전신이 으스러질 듯한 압박감.

본능적으로 공력을 일으켜 손목을 보호해 봐도 소용없었다.

아니, 불길이 쏟아지는 적천강의 눈동자를 본 순간 일말의 의지마저 잿더미처럼 허물어졌다.

‘뭔 놈의 눈빛이…….’

이건 사람이 아니다. 타고난 맹수요, 포식자다.

사내는 자신의 의지와는 상관없이 뻣뻣하게 굳은 채 포목점 깊숙한 곳으로 끌려갔다.

사방에 산더미처럼 쌓인 면포(綿布)와 비단 사이, 보이지 않던 으슥한 곳에서 두 개의 인영이 유령처럼 나타난 것은 그때였다.

저벅.

등잔의 흐릿한 불빛 너머로 이립 언저리로 보이는 두 청년의 얼굴이 드러난다.

하나는 모래라도 씹은 것처럼 표정이 무미건조했고, 다른 하나는 잘생겼으나 간교해 보일 만큼 위로 치켜 올라간 눈꼬리가 유일한 흠이었다.

각각의 특징상 여러모로 사람을 상대하기에는 영 좋지 않은 인상들.

그중 유난히 삭막한 인상의 청년이 먼저 입을 열었다.

어색하기 그지없는 투로.

“어이, 적 씨. 무슨 일이야?”

적천강이 대답했다.

“어이, 적 씨? 피똥 싸고 싶어서 환장을 했군.”

“……아, 지금은 아닙니까?”

“척 보면 모르겠느냐. 그 눈치로 낭인 생활은 어찌했누.”

“죄송합니다.”

고개를 꾸벅 숙인 삭막한 인상의 청년, 송일섬이 조심스럽게 입을 열었다.

“그자가 누구인지 여쭤봐도 되겠습니까?”

“손님.”

짤막하게 대꾸한 적천강이 덧붙였다.

“한데 전음을 쓰더군. 열로 시작해서 용으로 끝나는 별호를 대면서.”

송일섬이 즉각 대답했다.

“오늘 장사는 이만 접겠습니다.”

“문단속 잘해라. 아, 그전에 가게 주변 한 바퀴 돌아보고 수상한 놈 있으면 그 새끼도 잡아서 끌고 와.”

“예. 그런데 만약 불가피한 경우라면…….”

“뭘 물어보고 자빠졌느냐. 그런 상황에는 일단 멱부터 따고 봐야지.”

“알겠습니다.”

“대신 뒤처리는 깔끔하게 하거라. 눈에 안 띄게.”

“염려 마십시오.”

정중하게 고개를 숙인 송일섬은 곧장 자리를 떴고, 이야기를 듣고 있던 사내는 오금이 저려 오는 것을 느꼈다.

여기가 포목점인가, 아니면 도살장인가.

‘설마…… 살수 집단?’

자신이 받은 지시 중 이런 내용은 어디에도 없었다.

사내의 입 안이 바짝바짝 말라 가던 그때, 아직 자리에 남아 있던 또 다른 청년이 입을 열었다.

“저는 뭘 하면 되겠습니까?”

“나머지 불러와라. 한 사람도 빼놓지 말고 싹 다.”

“지금 당장 모두를 불러오는 건 어렵습니다. 한 명은 지금 밖에 있어서요.”

“염병할, 어떤 호로새끼가 그새를 못 참고 싸돌아다닌단 말이냐?”

“그게, 주 소저입니다.”

“잠시 나갈 수도 있지. 음. 그렇고말고. 주위 상황을 알아보려고 나간 것 같은데 참으로 기특하군.”

“…….”

“눈깔 그렇게 뜨지 말고 다른 식충이들이나 불러와라.”

“예.”

“마.”

“예?”

막 돌아서려는 청년을 불러세운 적천강이 눈살을 찌푸렸다.

“눈깔 그렇게 뜨지 말랬지. 노부의 말이 개좆으로 들리느냐?”

“이건 어릴 때부터 눈매가 이래서 어쩔 수 없는…… 아닙니다. 죄송합니다. 훗날 기회가 있으면 다시 태어나도록 하겠습니다.”

“그래. 그래야 환생도 하지. 눈깔도 착하게 뜰 수 있고.”

“예…….”

눈꼬리가 높아 슬픈 청년, 사마표가 힘없는 대답과 함께 자리를 뜨자 적천강이 불현듯 어딘가로 손을 뻗었다.

스윽.

형체 없이 뻗어 나가는 기운에 주위의 대기가 부르르 몸을 떨었다.

허공에 둥둥 뜬 채 날아온 나무 궤짝을 바라보는 사내의 동공도 예외는 아니었다.

‘허공섭물(虛空攝物)!’

사내 역시 나름 비범한 단체에 소속되어 있는지라 난생처음 보는 기예(技藝)는 아니었지만, 저만한 무게의 궤짝을 끌어오기 위해서는 어지간한 내가고수도 집중해야 한다는 사실쯤은 알고 있었다.

한데 눈앞의 중년인은 그걸 너무나도 간단히 해냈다.

그것도 대충 내지른 손짓 한 번으로.

‘설마?’

문득 짚이는 부분이 있던 사내가 조심스럽게 입을 열었다.

“혹, 그대의 별호가 화왕(火王)이오?”

적천강은 대답 대신 마치 신기한 생물을 보듯이 눈을 깜빡였다. 그리고 섬광처럼 사내의 정강이를 걷어찼다.

빡!

“어흑!”

“이 대가리에 피도 안 마른 어린 노무 새끼가 혀가 반 토막이 났나. 뭐? 그대?”

“자, 잠깐! 잠깐! 내 얘기를 들어보시오! 나는……!”

“그대로 가만히 있어라. 움직이면 더 다친다.”

뻑! 뻑! 뻐억!

팔에 멍이 들도록 익혔던 금나수(禁拿囚)도, 다리의 근육이 비명을 지를 때까지 밟았던 보법도 지금만큼은 무소용이었다.

정강이에 이어 복부, 가슴, 마지막으로 콧잔등을 얻어맞은 사내는 그 자리에서 실 끊어진 연처럼 쓰러졌다.

털썩.

물론, 그대로 기절하는 것조차 허락되지 않았지만.

“기상.”

벌떡.

쓰러질 때와는 비교도 안 되는 속도로 일어난 사내가 떨리는 목소리로 입을 열었다.

“화왕 적천강 대협이십니까.”

공손하기 그지없는 어투.

어느새 허공섭물로 끌어당긴 궤짝에 턱 걸터앉은 적천강이, 힘든 수술을 성공적으로 끝낸 외과 의사처럼 만족스러운 표정을 지었다.

“잘린 혓바닥이 이제야 제자리에 붙었군. 오냐, 노부가 적천강이다. 그러는 네놈은 누구냐?”

“소인은…….”

“네깟놈 이름은 알 것 없으니 소속만 말하거라. 대충 보아하니 불알 없는 환관인 건 알겠다만.”

“……!”

“왜, 그게 그리 큰 비밀이었느냐?”

순간 할 말을 잃은 사내. 아니 환관의 모습에, 적천강이 피식 웃으며 말을 이었다.

“하긴, 제법 그럴싸하게 꾸민 건 인정하마. 인피면구에 수염까지 본래 제 것인 양 자연스럽고. 하지만 고작 이 정도로 노부의 눈을 속일 수는 없지.”

“그렇다면 어떻게…….”

“앞서 네놈의 완맥을 짚어 보니 사내라면 응당 지녀야 할 양기(陽氣)가 턱없이 부족하더군. 자, 그럼 황궁 앞마당에서 불알 없는 무림인을 만나는 것과 환관을 만나는 것 중 무엇이 더 가능성이 높은지는 굳이 말 안 해도 알겠지.”

사내가 마른침을 꿀꺽 삼켰다. 적천강의 날카로운 판단도 판단이지만, 자신이 환관이라는 사실을 알면서도 변함없는 그의 태도 때문이었다.

“그럼 소인이 어디에서 왔는지도 아시겠군요.”

“당연한 것 아니겠느냐. 멀쩡한 사내놈들 불알 뜯어내는 악취미를 가진 곳은 세상천지에 황궁밖에 없으니.”

“…….”

“그만 주절대고 노부가 물어본 것에나 대답해라. 정확히 황궁 어디에 속한 몸이지? 상산왕의 오른팔이라는 그 환관 밑에 있는 놈인가? 아니면 동창? 그것도 아니면 황제 뒷구멍이나 핥는…….”

“동창입니다.”

“동창이라, 천하에서 가장 끈질기고 독한 고자들만 모아놨다는 그곳이군. 한데 어째서 동창의 환관이 이곳까지 찾아왔느냐?”

“열화신룡이, 아니 제자분께서 몇 가지 말씀을 전하라 하셨습니다.”

“황제가 덫을 놓는 것은 아니고?”

“절대 아닙니다. 이곳에 머무르고 계시다는 사실을 알려 준 것도 제자분이시고요.”

“그럴듯하군. 하지만 동창의 정보력이라면 어떻게든 알아냈어도 그리 이상하지는 않지. 어찌 증명할 테냐?”

가늘어지는 적천강의 눈매에, 환관이 황급히 대답했다.

“모, 몽수타(夢殊打).”

“뭐라?”

“제자분께서 알려 주신 겁니다. 소인도 당최 무슨 뜻인지는 모르겠으나 이리 전하면 적어도 피똥 쌀 일은 없을 거라고…….”

환관은 조마조마한 심정이었으나, 다행히도 적천강은 그 어눌한 발음의 단어가 무엇을 의미하는지 정확히 알고 있었다.

몬스터.

선계(仙界)를 피로 물들였다는 저세상의 괴물들.

그리고 그것에 대해 아는 이는 천하에 오직 진태경과 자신. 단 두 사람뿐이었다.

“흠. 녀석이 보낸 것이 확실하군.”

“그, 그렇습니다.”

“진즉 말했다면 굳이 때리진 않았을 텐데. 노부의 무례를 용서하게. 고자 양반.”

환관은 고자에게 고자라고 하는 것만큼 무례한 언사가 없다고 말하고 싶었지만, 꾹 눌러 참았다.

괜히 입방정을 떨었다가는 정말 피똥을 싸게 될 수도 있을 테니까.

그저 촌각이라도 빨리 이 자리를 뜨는 것이 유일한 상책(上策)이었다.

슥.

품 깊숙이 숨겨 놓은 자그마한 통을 꺼내 건네자, 적천강의 눈이 깊어졌다.

“진태경. 그 녀석이 노부에게 전하라고 한 서신인가?”

“예.”

“그럼 다른 하나는?”

적천강의 말대로 단단히 밀봉된 통은 총 두 개였다. 환관이 낮은 목소리로 입을 열었다.

“제가 모시는 분께서 전하라 명하신 서신입니다.”

“모시는 분?”

“산서성 도지휘동지 대감을 아시는 것 같습니다만.”

“홍진? 본 적은 없지만 오는 길에 들었지. 제법 착한 고자라던데.”

“……예. 제가 모시는 분께서 그분과 긴밀한 사이입니다. 이 안의 내용이 앞으로 하실 일에 도움이 될 거라 하셨습니다.”

“이게 전부인가? 더 말해 줄 건 없고?”

“그렇습니다. 소인은 단지 심부름꾼에 불과한지라.”

환관에게 주어진 임무는 거기까지였다.

그는 보법까지 펼쳐 가며 황급히 이 넓은 도살장, 아니 포목점을 빠져나갔고 홀로 남은 적천강은 밀봉된 통을 뜯어 돌돌 말린 전서(傳書) 두 장을 꺼냈다.

스륵.

퀴퀴한 포목점 내부의 공기 사이로 기름 먹인 종이 냄새가 섞여든다.

‘아무래도 조진 것 같습니다.’라는 명문(名文)으로 시작되는 진태경의 서신에 이어, 동창의 도움을 받아 작성된 정보를 순식간에 읽어 내려간 적천강이 작게 한숨을 내쉬었다.

“일 한번 더럽게 꼬였군.”

그리고 그 순간.

화륵.

삼매진화(三昧眞火)로 말미암은 불꽃이 두 장의 전서를 집어삼키며 어둠 속에서 몸부림쳤다.

적천강이 눈 깜짝할 사이에 재가 되어 파스스 사라지는 전서를 말없이 응시하던 그때.

“모두 데려왔습니다.”

촌각 전 자리를 떴던 사마표가 익숙한 얼굴들과 함께 다가오다 말고 멈칫했다.

“그자는 어디 있습니까?”

“조금 전에 돌려보냈다. 다행히 수상쩍은 놈은 아니더군.”

“누구였는지 알아내셨습니까?”

“고자였다. 태경이 녀석이 보낸.”

“……예?”

간추려도 너무 간추린 설명에 혼란스러워하는 사마표를 깔끔하게 무시한 적천강이 말을 이었다.

“저 치들은 도대체 어디에 있었기에 이리 늦었느냐?”

흐아암.

아직 졸린 눈으로 하품하는 태산의 옆구리를 쿡 찌른 사마표가 머뭇거렸다.

“그게 그러니까…….”

“구석에 짱박혀서 처자고 있었군.”

“잠시 졸았던 것 같습니다.”

“다음에는 영원히 잠들게 될 거라고 전해라.”

“예.”

“남호는?”

헝클어진 복장으로 씨근덕거리고 있는 노인, 남호를 힐끗 바라본 사마표가 대답했다.

“태산이의 목을 조르고 있었습니다.”

“왜?”

“남 노인이 숨겨 두었던 술을 태산이가 모조리 먹었다는군요.”

아주 잠깐 동안 태산과 남호의 목을 동시에 조르는 달콤한 상상을 떠올린 적천강이 깊은 한숨을 내쉬었다.

“지랄들 떨지 말고, 다들 준비해.”

“실례지만 어떤 것을…….”

“조만간 황궁으로 간다.”

“예? 어떻게 말입니까?”

적천강이 눈을 빛내며 대답했다.

“걱정 말거라. 정식으로 초대받아서 가는 것이니.”
```

## Final English reading copy

```markdown
# Chapter 878

The moment the Sound Transmission pierced his ear, Jeok Cheongang moved with remarkable speed—and complete naturalness.

“Oh, you’re looking for the finest Shu brocade? You should’ve said so earlier. Come on in.”

“No, wait. I was only…”

The man disguised as a customer tried to protest, but the terrifying energy coming from Jeok Cheongang’s grip on his wrist left him gaping.

“Gah.”

The pressure felt like it would crush his entire body.

He instinctively summoned his internal energy to protect his wrist, but it was useless.

No—when he saw the flames pouring from Jeok Cheongang’s eyes, even the last scrap of his will crumbled to ash.

*What the hell is with that look…*

This wasn’t a man. He was a beast born to hunt—a predator.

Frozen stiff against his own will, the man was dragged deep into the textile shop.

Between the towering stacks of cotton cloth and silk, two figures emerged like ghosts from a shadowy corner no one had noticed.

Thud.

In the faint lamplight, the faces of two young men—both appearing to be around thirty—came into view.

One had an expression as flat as if he were chewing sand. The other was handsome, but his upturned eyes were so sly-looking they were his one flaw.

By their respective traits, neither had the sort of face that made dealing with people easy.

The especially austere-looking young man spoke first.

In a painfully awkward tone, he said, “Hey, Mr. Jeok. What’s going on?”

Jeok Cheongang answered, “Hey, Mr. Jeok? You’ve got a death wish, don’t you?”

“……Oh. Not right now?”

“Can’t you tell by looking? How did you survive as a wandering martial artist with that kind of sense?”

“I’m sorry.”

The austere young man bowed his head. Song Ilseom carefully spoke up.

“May I ask who that man is?”

“A customer.”

Jeok Cheongang gave the brief reply, then added, “But he used Sound Transmission. He introduced himself with a title that starts with ‘Blazing’ and ends with ‘Dragon.’”

Song Ilseom replied at once. “I’ll close up for today.”

“Make sure the shop is secured. Oh, first, circle the area. If you see anyone suspicious, grab the bastard and bring him here too.”

“Yes. But what if there’s no other choice…?”

“What the hell are you asking me for? In that situation, slit his throat first.”

“Understood.”

“Just clean up after yourself. Make sure no one notices.”

“Leave it to me.”

Song Ilseom bowed politely and left at once. The man who’d heard their conversation felt his knees weaken.

*Is this a textile shop or a slaughterhouse?*

*Could they be… an assassin organization?*

Nothing in his orders had mentioned anything like this.

As his mouth went dry, the other young man who had stayed behind spoke up.

“What should I do?”

“Bring the rest here. Every last one of them.”

“It’ll be difficult to bring everyone right away. One of them is out at the moment.”

“Damn it, what kind of goddamn idiot can’t sit still for a minute?”

“Well, it’s Young Lady Ju.”

“She’s allowed to go out for a while. Right. Of course. She must’ve gone to check on the situation nearby. How thoughtful of her.”

“……”

“Quit looking at me like that and go bring the other freeloaders.”

“Yes.”

“Hey.”

“Yes?”

Jeok Cheongang stopped the young man as he was turning away and frowned.

“I told you not to look at me like that. Do my words sound like a load of bullshit to you?”

“It’s just that my eyes have looked this way since I was a child, so there’s nothing I can do about it… No. I’m sorry. If I get the chance someday, I’ll be reborn.”

“Good. That way you can reincarnate—and learn to look at people properly.”

“Yes…”

With a weak reply, the young man with the sorrowfully upturned eyes, Sama Pyo, left. Jeok Cheongang suddenly reached out toward something.

Swish.

His energy extended without form, and the air around them trembled.

The man’s pupils trembled too as he watched a wooden chest fly toward them, suspended in midair.

*Seizing an Object Through Empty Space!*

The man belonged to a rather extraordinary organization himself, so this wasn’t the first time he’d seen the technique. But he knew even a skilled internal-energy master would have to concentrate to pull in a chest that heavy.

Yet the middle-aged man before him had done it with ease.

With nothing more than a casual flick of his hand.

*Could it be…?*

Something clicked for the man, and he cautiously spoke.

“Could your title be the Fire King?”

Instead of answering, Jeok Cheongang blinked at him as if he were some curious creature. Then he kicked the man in the shin as fast as a flash.

Crack!

“Gah!”

“You little shit! You’re still wet behind the ears, and half your tongue seems to be missing. What was that—‘you’?”

“W-wait! Wait! Hear me out! I…”

“Stay right where you are. Move and you’ll get hurt worse.”

Thwack! Thwack! Thwack!

The man’s grappling technique, which he’d practiced until his arms were bruised, and his footwork technique, which he’d drilled until the muscles in his legs screamed, were useless now.

After getting hit in the shin, the stomach, the chest, and finally the bridge of the nose, the man collapsed like a puppet with its strings cut.

Thump.

Of course, even passing out wasn’t allowed.

“Up.”

He sprang upright, rising far faster than he’d fallen. His voice trembled as he spoke.

“Are you the Fire King, Great Hero Jeok Cheongang?”

His tone could not have been more respectful.

Jeok Cheongang had somehow pulled the chest closer with Seizing an Object Through Empty Space and perched on it. His expression was as satisfied as a surgeon who’d just completed a difficult operation.

“Your severed tongue has finally grown back in the right place. Good. I am Jeok Cheongang. And who are you?”

“I am…”

“I don’t need to know a nobody like you’s name. Just tell me who you work for. I can tell at a glance you’re an eunuch, anyway.”

“……!”

“What? Is that such a big secret?”

The man—or rather, the eunuch—was momentarily speechless. Jeok Cheongang chuckled and continued.

“I’ll admit, you did a pretty good job disguising yourself. That human-skin mask, even your beard—it all looks natural, like it’s your own. But you can’t fool this old man with something as basic as that.”

“Then how did you…?”

“I felt your pulse earlier. You didn’t have nearly enough yang qi for a man. Now, tell me—which is more likely in the imperial palace courtyard: running into a eunuch, or running into a martial artist without balls? I don’t need to spell it out, do I?”

The eunuch swallowed hard. He was impressed by Jeok Cheongang’s keen judgment, of course, but more than that, he couldn’t believe how little the man’s attitude had changed despite knowing he was an eunuch.

“Then you must know where I came from, too.”

“Of course. The only place in the world with the perverse hobby of ripping the balls off perfectly healthy men is the imperial palace.”

“……”

“Stop rambling and answer what I asked. Exactly where in the imperial palace do you serve? Are you under that eunuch who’s Prince Shangshan’s right hand? The East Depot? Or are you one of the ones licking the Emperor’s…”

“The East Depot.”

“The East Depot, huh? The place that gathers the most persistent and vicious eunuchs in the world. But why would an East Depot eunuch come all the way here?”

“The Blazing Flame Divine Dragon—no, your Disciple asked me to deliver a few messages.”

“Is the Emperor laying a trap?”

“Absolutely not. Your Disciple was the one who told us you were staying here.”

“That sounds plausible. But with the East Depot’s intelligence network, it wouldn’t be surprising if you’d found out somehow anyway. How are you going to prove it?”

At the narrowing of Jeok Cheongang’s eyes, the eunuch hurried to answer.

“M-Mong-su-ta.”

“What?”

“Your Disciple told me to say it. I have no idea what it means, but he said if I passed it on, I’d at least avoid shitting blood…”

The eunuch was on tenterhooks, but fortunately, Jeok Cheongang knew exactly what the clumsy-sounding word meant.

*Monster.*

The monsters from the other world that had stained the realm of immortals with blood.

And there were only two people under heaven who knew about them: Jin Taekyung and himself.

“Hmm. So he definitely sent you.”

“Y-yes.”

“If you’d said that sooner, I wouldn’t have had to hit you. Forgive this old man’s rudeness, my good castrate.”

The eunuch wanted to say that calling a eunuch a castrate was about the rudest thing you could do, but he held his tongue.

If he ran his mouth again, he might really end up shitting blood.

His only sensible move was to leave as soon as possible.

He reached deep into his clothing, took out a small sealed tube, and handed it over. Jeok Cheongang’s eyes grew serious.

“Is this the missive Jin Taekyung told you to deliver to me?”

“Yes.”

“And the other one?”

As Jeok Cheongang had said, there were two tightly sealed tubes. The eunuch spoke in a low voice.

“The person I serve ordered me to deliver this one.”

“The person you serve?”

“You seem to know the Deputy Military Commissioner of Shanxi Province.”

“Hong Jin? I haven’t met him, but I heard about him on the way here. Apparently, he’s a pretty decent eunuch.”

“……Yes. The person I serve is on close terms with him. He said the contents would help with what you’re going to do.”

“Is that all? Nothing else to tell me?”

“That’s right. I’m only a messenger.”

That was as far as the eunuch’s orders went.

He hurried out of the vast slaughterhouse—or rather, the textile shop—using a footwork technique. Left alone, Jeok Cheongang broke the seals and took out two rolled-up missives.

Rustle.

The smell of oil-treated paper mingled with the stale air inside the textile shop.

Jeok Cheongang quickly read the information prepared with help from the East Depot, after Jin Taekyung’s missive began with the eloquent line, *“I’m afraid we may be screwed.”* He let out a quiet sigh.

“What a goddamn mess.”

And just then—

Fwoosh.

Flames from Samadhi True Fire consumed both missives, twisting and writhing in the darkness.

As Jeok Cheongang silently watched the missives turn to ash and vanish with a soft rustle in the blink of an eye—

“I brought everyone.”

Sama Pyo, who’d left moments ago, approached with some familiar faces, then stopped short.

“Where is that man?”

“I sent him back a little while ago. Fortunately, he wasn’t suspicious.”

“Did you find out who he was?”

“An eunuch. One Jin Taekyung sent.”

“……What?”

Jeok Cheongang neatly ignored Sama Pyo’s confusion at such a painfully brief explanation and continued.

“Where the hell were those people that it took you so long to bring them?”

*Yaaawn.*

Sama Pyo nudged Taishan in the side as he yawned, his eyes still sleepy, then hesitated.

“Well, you see…”

“Looks like you were holed up in a corner sleeping.”

“I think I dozed off for a bit.”

“Next time, tell him he’ll be sleeping forever.”

“Yes.”

“What about Namho?”

Sama Pyo glanced at the old man, Namho, who was panting in rumpled clothes, and answered.

“He was choking Taishan.”

“Why?”

“Taishan ate all the liquor Elder Namho had hidden away.”

For the briefest moment, Jeok Cheongang imagined choking Taishan and Namho at the same time. Then he let out a deep sigh.

“Quit screwing around and get ready, all of you.”

“Pardon me, but what should we…”

“We’re going to the imperial palace soon.”

“What? How?”

Jeok Cheongang’s eyes gleamed as he answered.

“Don’t worry. We’ve been formally invited.”
```

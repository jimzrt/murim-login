<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0888.txt",
      "sha256": "65c040e4bf58fa558e47a62ec194e9b1a46920a0c4359198c2b4b1f09fecbb3d",
      "bytes": 13097
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "43be0abc85c5475d3a4db5b3fe50349e507d864d2c31679b12d278d0cf676cee",
      "bytes": 2285
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "77f7f9625d663fdeec408b3696199ba3f21d98f335ae9eae4e9465caec345d0f",
      "bytes": 230213
    },
    {
      "path": "characters/Baek Yeon.md",
      "sha256": "c0adfd3b5e5e4677ee62eec719b9f75794ba8517f97ee907acf6b585a74ddbe1",
      "bytes": 983
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "d21cb3f3d67701279f75bd0ecb81b9fe3c6d8330e3df820d03bf0a614cff0feb",
      "bytes": 759
    },
    {
      "path": "characters/Jang Taebo.md",
      "sha256": "67c6d981d110038140de4e81810983eb9b80fc78d34d55361cfb01b5c2602630",
      "bytes": 778
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "1fd2c8ff70e7d148a0d3f9f48b297993cae3e13ac913597f8329592bf2d080b7",
      "bytes": 1511
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "f96d4b0c73530121a99ef74dcd411b9066ee7bd8df1a4fae82070a3f414c5eb2",
      "bytes": 1782
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "c7d4f3ae06ea37a0edafa900aaaea7576e43a9f9afd8c1f7914bd0b4716952a5",
      "bytes": 622
    },
    {
      "path": "characters/Ma Sanbao.md",
      "sha256": "d946a2df504437bd96d51e2193d47cc4b3141415f22aaf1c9989d6f7cce0e350",
      "bytes": 796
    },
    {
      "path": "characters/Martial God.md",
      "sha256": "c4e3637a7ad155413271c55a67f0e729f2f02f92c8c4986200c97904a65687d5",
      "bytes": 752
    },
    {
      "path": "characters/Prince Shangshan.md",
      "sha256": "70c50cffb2ce75fdf396e234deb5459f8e97ac2f50b47de81992291eb96d49b6",
      "bytes": 952
    },
    {
      "path": "characters/So Gyo.md",
      "sha256": "a283e1ffa5b6634131aa0f246840210465d382ffcf80480a5530ac2e6a363d96",
      "bytes": 730
    },
    {
      "path": "characters/Southern Heaven Demon Empress.md",
      "sha256": "15942a94bfeb463ed4740f5c31bfaa9a9e9c008616e833a3dc6766d35ba0698f",
      "bytes": 715
    },
    {
      "path": "characters/Western Heaven Demon Lord.md",
      "sha256": "9791d3e4e67fa8fa271d22fd6b5e7a5bf052e8cc1ea067fd196761e7ce54a3ff",
      "bytes": 888
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "261f33db68979f080468a08d9b7bc6a9dd935694e74740594050c09d22767904",
      "bytes": 259256
    }
  ],
  "estimated_tokens": 13452
}
-->

# Durable State Update — Chapter 888

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
1 and safe_through 888. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 888. Profile updates may replace only one
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
  "chapter": 888,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 888,
    "continuity_sources": [888],
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
    "The Emperor has confined Prince Shangshan in Qianqing Palace and plans a banquet attended by Shangshan and officials; Taekyung returned without Shangshan.",
    "Ma Sanbao leads a covert faction seeking to enthrone Shangshan; its pact and plans for the banquet remain relevant.",
    "Assassins disguised as laborers are inside the palace; their mission remains unclear.",
    "Taekyung suspects the Emperor is connected to Dark Heaven, but this is unconfirmed.",
    "The late Emperor died after mental confusion while confined; Taekyung suspects Blood Soul Gu may have been involved. Blood Soul Gu was found in the City Lord of Sichuan Province’s corpse after he showed strange symptoms.",
    "So Gyo’s identity and allegiance are unconfirmed; Taekyung suspects a Dark Heaven connection because of her intelligence and knowledge of powerful figures.",
    "So Gyo is a Supreme Peak master who concealed her strength through Returning to Simplicity and wields a flexible sword.",
    "Taekyung’s fight with So Gyo is ongoing; his dantian is overtaxed, his internal energy weakened, and an unidentified streak of light is approaching."
  ],
  "continuity_sources": [
    886,
    887
  ],
  "open_questions": [
    "Who is So Gyo, and whom does she serve?",
    "Who or what is the streak of light approaching Taekyung?",
    "Will the banquet become a confrontation, and what does the Emperor intend?",
    "Did the Emperor or Dark Heaven use Blood Soul Gu against the late Emperor and the City Lord of Sichuan Province?",
    "What preparations has Ma Sanbao’s faction made, and who is the person his allies asked about?"
  ],
  "safe_through": 887,
  "temporary_decisions": [
    "Render 기관진식 as “mechanisms and formations”; retain “Third Shadow,” “First Shadow,” “No Shadow,” and “Marquis Within the Passes.”",
    "Use “imugi,” not “dragon,” for the creature Taekyung killed at Dongting Lake.",
    "Render 연판장 as “a pact bearing their signatures”; retain “Hongmen Banquet” for 홍문연.",
    "Treat 거산 as Taishan’s uncertain name variant, not a confirmed separate person; render 열화단 as “Blazing Flame Troupe” and 마희단 as “circus troupe.”"
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 무신     | **Martial God**               | —              |
| 태원진가   | **Jin Family of Taiyuan**        |
| 암천     | **Dark Heaven**                  |
| 사천당가   | **Sichuan Tang Clan**            |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 살기     | **killing intent**                               |                                                       |
| 중원     | **Central Plains**                               |                                                       |
| 시스템              | **System**                     |
| 레벨               | **Level**                      |
| 헌터      | **Hunter**            |
| 태원     | **Taiyuan**            |
| 사천     | **Sichuan**            |
| 백연 | **Baek Yeon** | Commander of the Embroidered Uniform Guard. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 장태보 | **Jang Taebo** | Former Guild Leader of the Ironcraft Guild; now lives near Jeongyang and is sought as a Master Artisan. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 마삼보 | **Ma Sanbao** | The East Depot’s Brush-Holding Eunuch and second-in-command. |
| 상산왕 | **Prince Shangshan** | The City Lord and a member of the imperial family who orders the luncheon. |
| 소교 | **So Gyo** | The palace attendant leading the group assigned to serve Prince Shangshan. |
| 남천마후 | **Southern Heaven Demon Empress** | Title Honglan uses when revealing her identity. |
| 서천마군 | **Western Heaven Demon Lord** | Title of the middle-aged antagonist who commands the summoned black-robed hunters. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 만년한철 | **Ten-Thousand-Year Cold Iron** | Material that destroys Pung Yang's Body-Protecting Qi when the Unnamed Sword satisfies a specific condition. |
| 주표 | **Zhu Bao** | Personal name of Prince Shangshan. |
| 선황 | **the late Emperor** | The former Emperor whom Hong Jin served. |
| 철기방 | **Ironcraft Guild** | Hubei guild composed mainly of skilled craftsmen and closely associated with the Nine Sects and One Gang. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 일각 | **fifteen minutes** | Quarter of a shichen; used for the remaining completion time. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 염화일로 | **Flamefire Path** | Fire Gate Clan signature movement technique; Jeok Cheongang has reached its ninth stage. |
| 천주 | **Lord of Heaven** | Authority invoked by the masked attackers. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 당가 | **Tang Family** | Short form for the Sichuan Tang Clan when distinguished from 사천당문. |
| 살수 | **assassin** | Professional killer considered as a possible suspect. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 뇌옥 | **underground prison** | The Tang Clan's subterranean prison. |
| 열화신룡 | **Blazing Flame Divine Dragon** | New sobriquet bestowed on Jin Taekyung. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 복마전 | **demon-slaying battleground** | A possible description for Sichuan if Dark Heaven attacks it. |
| 고든 | **Gordon** | Pentagon employee tasked with repairing smashed warning lights. |
| 서천 | **Western Heaven** | Short form used by the Lord of Heaven for the Western Heaven Demon Lord. |
| 남천 | **South Heaven** | Dark Heaven power that the Lord of Heaven orders the servants to contact. |
| 마후 | **Demon Empress** | Title used for the Southern Heaven Demon Empress. |
| 화신 | **Fire God** | A local deity worshiped by one Nanman believer. |
| 금의위 | **Embroidered Uniform Guard** | Imperial guard force mentioned by Hong Jin. |
| 혈사자 | **Blood Envoy** | Baek Yeon’s sobriquet. |
| 건청궁 | **Qianqing Palace** | The Emperor's palace, where Baek Yeon meets him. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 진태경 | 주표 | visitor to prince | His Highness, Prince Shangshan | formal-deferential | Addresses Zhu Bao as 상산왕 전하 after kneeling to meet his gaze. |
| 주표 | 진태경 | prince to visiting young hero | Jin Taekyung | formal and inquisitive | Uses the formal second-person address before asking Taekyung's name and requesting an autograph. |
| 진태경 | 장태보 | younger_visitor_to_elder_master | Elder | polite and persistent | Taekyung repeatedly addresses Jang Taebo as 어르신 while requesting his assistance. |
| 장태보 | 진태경 | elder_master_to_younger_visitor | you | gruff and familiar | Jang Taebo uses 자네 while questioning and dismissing Taekyung. |
| 적천강 | 장태보 | strangers; visiting elder to local smith | Old Man Jang | blunt and familiar | Uses 장 노인 while confirming Jang Taebo’s identity. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 서천마군 | 진태경 | hostile_opponents | you | calm and taunting | Uses 자네 while questioning Taekyung and offering to take him alive. |
| 진태경 | 서천마군 | hostile_opponents | Western Heaven Demon Lord | casual and defiant | Identifies the Demon Lord by title and answers his surrender demand with sarcasm. |
| 서천마군 | 신의 | hostile_invader_to_physician | Divine Physician | calm and mocking | Uses 신의 and 그대 while taunting the physician and dismissing his objections. |
| 신의 | 서천마군 | physician_to_invading_fiend | fiend | defiant and formal | Calls the Western Heaven Demon Lord an 악귀 and orders him to leave. |
| 서천마군 | 적천강 | hostile_invader_to_unconscious_patient | you | calm and predatory | Says someone wants to see Jeok Cheongang and attempts to move him with Seizing an Object Through Empty Space. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 서천마군 | hostile_opponents | you bastard | blunt and threatening | Jeok addresses the Western Heaven Demon Lord with 네놈 while defending Taekyung and ordering him not to touch his Disciple. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 남천마후 | 진태경 | hostile_supernatural_opponent_to_young_martial_artist | Young Great Hero / Child | lighthearted and taunting | Addresses Taekyung while refusing to explain the Gate. |
| 진태경 | 남천마후 | young_martial_artist_to_hostile_demon_empress | you | hostile and determined | Promises that the Southern Heaven Demon Empress will die when they meet again. |
| 적천강 | 남천마후 | legendary_martial_master_to_hostile_demon_empress | you bitch | blunt and threatening | Threatens to punish her and Lord of Heaven. |
| 남천마후 | 적천강 | hostile_demon_empress_to_legendary_martial_master | Fire King Jeok / you | flattering and mocking | Addresses Jeok Cheongang as the Fire King while praising Lord of Heaven. |
| 남천마후 | 천주 | devoted_servant_to_revered_master | Lord of Heaven | reverent and prayerful | The Southern Heaven Demon Empress prays that the Lord of Heaven will remember her loyalty and love. |
| 진태경 | 헌터 | field commander to allied Hunters | you; Hunters | blunt and commanding | Orders the human forces to stop asking questions and kill the fleeing Minotaurs. |
| 주표 | 백연 | prince addressing an imperial military officer | Commander Baek Yeon | formal and authoritative | Addresses Baek Yeon by name and office while insisting that he answer. |
| 백연 | 주표 | imperial officer addressing a prince | Your Highness | formal and deferential | Uses 전하 when apologizing to and answering Prince Shangshan. |
| 진태경 | 백연 | young martial artist confronting an imperial military commander | you | casual and insulting | Refers to Baek as 이 양반 while challenging his conduct. |
| 진태경 | 상산왕 | protector addressing a young prince | His Highness | respectful royal address | Taekyung refers to the prince as 상산왕 전하 when ordering Mujin to bring him. |
| 진태경 | 황제 | guest of the Emperor’s younger brother addressing the Emperor | Your Majesty | formal and deferential in address, despite blunt challenges | Taekyung repeatedly addresses the Emperor as 폐하. |
| 상산왕 | 황제 | younger brother addressing the Emperor | Your Majesty | deferential royal address | Shangshan addresses the Emperor as 폐하 while pleading for Taekyung. |
| 소교 | 진태경 | palace attendant addressing a martial artist and guest under escort | Young Master Jin | formal and respectful, but firm | Addresses him as 진 공자 while escorting him and warning him not to investigate. |
| 진태경 | 소교 | palace attendant and martial artist under imperial scrutiny | you | formal-polite, controlled and challenging | Taekyung addresses So Gyo as 당신 while questioning her presence and demanding an explanation. |

## Listed compact profiles

### Baek Yeon.md

# Baek Yeon (백연)

- **Safe through:** Chapter 874
- **Aliases:** Blood Envoy
- **Role:** Baek Yeon is the Commander of the Embroidered Uniform Guard, a former martial arts instructor to the Crown Prince, and the Blood Envoy who helped the fourth prince seize the throne and led the purge.
- **Personality:** Politically assured and controlled, he enforces authority with ruthless decisiveness but speaks with striking defiance to the Emperor in private when their shared undertaking is at stake.
- **Voice:** Not established
- **Relationships:** He commands the Embroidered Uniform Guard and serves the Emperor; they share an old promise tied to a great undertaking, and Baek urges the Emperor to restore matters before their adversaries' moves unravel it. He orders Jeong Hogun to surveil Prince Shangshan’s party while leaving openings for an approach, and treats Taekyung as a dangerous potential obstacle.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 886
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Jang Taebo.md

# Jang Taebo (장태보)

- **Safe through:** Chapter 851
- **Aliases:** None
- **Role:** Jang Taebo is the former Guild Leader of the Ironcraft Guild and one of the world’s renowned smiths, now the Jin Family of Taiyuan’s Master of Ironcraft Hall.
- **Personality:** Blunt, cantankerous, solitary, and proud; values an untroubled retirement and protects his anonymity, while quietly caring for the neighboring boy Hanga.
- **Voice:** Curt, gruff, and dryly teasing; rejects requests with flat finality.
- **Relationships:** His disciple is the current Guild Leader of the Ironcraft Guild; neighboring boy Hanga is his only conversational partner, and Jang Taebo gives him candy while pretending annoyance.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 886
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm, the occupant of the chief seat of the Murim Alliance's Five Kings Hall, and a trusted confidant who accepts Jin as himself despite knowing that he travels between Murim and another world resembling the realm of immortals.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He deeply trusts his publicly acknowledged Disciple and intended heir Jin Taekyung, warmly regards Ju Hwaran and hopes she and Jin grow closer, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and remains Peng Cheolhu's rival.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 887
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader.
- **Personality:** Hungry, self-aware, dryly observant, and pragmatic under pressure; accepts extreme personal risk when duty and the lives of others demand it.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; they trust each other deeply, though their bond remains unformalized. Cheongpung is his trusted companion and only true martial rival; Choi Minwoo is his subordinate and trusted manager of media and official arrangements as well as the Peace Guild's Guild Master; Ju Hwaran is a trusted Fire Dragon Pavilion member; Magic Johnson and Chuck Hagel are allied to him; his mother and sister Hayeon are among those he protects; the Skeleton King is his friend and ally; Xiao Shen regards him as an older brother; Jin-ho is his older friend and trusted confidant; he once saved Ju Wongong’s life.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 887
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Ma Sanbao.md

# Ma Sanbao (마삼보)

- **Safe through:** Chapter 886
- **Aliases:** None
- **Role:** Ma Sanbao is the East Depot’s Brush-Holding Eunuch and second-in-command, a Supreme Peak martial artist who has secretly remained in the imperial palace.
- **Personality:** He is vigilant and patient, concealing his loyalties while awaiting the moment to act for the late Emperor.
- **Voice:** He speaks in measured, courteous language, using calm reassurances and strategic metaphors to maintain unity while keeping sensitive details guarded.
- **Relationships:** Ma Sanbao is a longtime friend and former East Depot cohort of Hong Jin; he stayed behind to await Prince Shangshan's return and is leading a group seeking to enthrone him.

### Martial God.md

# Martial God (무신)

- **Safe through:** Chapter 850
- **Aliases:** None
- **Role:** An unidentified legendary martial artist regarded as a pinnacle above the Ten Kings; more than fifty years ago, he defeated five Supreme Peak fiends and five hundred Blood Ghost Squad members alone.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** He met the Beast Miao King twice more than fifty years ago, appearing first as a white-bearded elder and later as a young boy; Mae Jonghak received several teachings from him, while his identity, whereabouts, and possible connection to Cheon Taemin remain unknown.

### Prince Shangshan.md

# Prince Shangshan (상산왕)

- **Safe through:** Chapter 887
- **Aliases:** None
- **Role:** Prince Shangshan, whose personal name is Zhu Bao, is the Emperor’s twelve-year-old youngest younger brother and an exceptionally skilled young swordsman.
- **Personality:** Earnest and compassionate, he takes responsibility for his loyal subjects’ hardship, admires Jin Taekyung, seeks candid counsel, and shows composure beyond his years in the face of death and political danger.
- **Voice:** Archaic and formal in the manner of a historical drama, with openly eager and childlike reactions beneath his royal diction.
- **Relationships:** Prince Shangshan Zhu Bao is the Emperor’s youngest younger brother; the late Emperor entrusted Hong Jin with his care. Zhu Bao admires Jin Taekyung, seeks to emulate him, and calls him a friend; the Emperor says he will take care of Zhu Bao.

### So Gyo.md

# So Gyo (소교)

- **Safe through:** Chapter 887
- **Aliases:** None
- **Role:** A palace attendant assigned to Prince Shangshan who has concealed her identity and strength; she is a Supreme Peak master, but her allegiance and purpose remain unconfirmed.
- **Personality:** Calm, calculating, and self-possessed; she conceals her strength and identity and can be openly taunting.
- **Voice:** Measured and composed, shifting from deferential formality to casual, pointed taunts and threats.
- **Relationships:** She poses as the leader of the palace attendants assigned to Prince Shangshan; her true allegiance is unknown, and she is Jin Taekyung’s opponent.

### Southern Heaven Demon Empress.md

# Southern Heaven Demon Empress (남천마후)

- **Safe through:** Chapter 887
- **Aliases:** None
- **Role:** The Southern Heaven Demon Empress was Honglan, the creator of the rift behind the Inner Palace, and was killed after the rift closed.
- **Personality:** Playful, cruel, confident, and casually dismissive of mass death and the suffering of others.
- **Voice:** Light, taunting, amused, and delighted even when discussing murder or imminent catastrophe.
- **Relationships:** She commands and advises Baeksang, treats Jin Taekyung and Yayul Cheok as expendable to the grand plan, and keeps a masked hunting dog whom she trained carefully.

### Western Heaven Demon Lord.md

# Western Heaven Demon Lord (서천마군)

- **Safe through:** Chapter 887
- **Aliases:** None
- **Role:** Former Protector of the Divine Cult who commands Dark Heaven's assault on the Sichuan Tang Clan, lost the Myriad-Poison Ring to Jin Taekyung, suffered a crushed ankle and a torn wrist, and was temporarily possessed by the Lord of Heaven before the borrowed body was destroyed.
- **Personality:** Cold, detached, patient, and utterly ruthless toward those he interrogates or hunts.
- **Voice:** Controlled and dispassionate, with concise statements delivered in a quiet, threatening tone.
- **Relationships:** Tang Taesang and the Heaven-Shaking Venerable Nun were his latest victims, he lost one arm taking their lives, and the Qilian Three Fiends now submit to him alongside his hundreds of black-robed hunters.

## Korean source

```text
＃888화



모든 것은 찰나의 순간에 시작되었고, 끝났다.

쐐애액!

파공성조차 앞질러 들이닥친 한 줄기의 섬광. 그리고…….

콰아아앙!

굉음과 함께 전신을 밀어 내는, 거대한 충격파.

“흡!”

콰드득. 호흡을 삼키며 굳게 뿌리내린 발끝을 따라 땅거죽이 뒤집힌다.

충격의 여파로 휘몰아친 광풍에 연못의 물이 높게 솟구치고, 사방을 뒤덮은 기화요초(琪花瑤草)를 휩쓸었다.

솨아아.

누군가 이 광경을 보았다면 잠시나마 압도되어 탄성을 흘렸을지도 모른다.

헤아릴 수 없이 많은 꽃잎이 바람을 따라 휘몰아치는 것은 실로 장관이었으니까.

하지만 아무리 생각 없고 속 편한 사람이라 해도, 지금 이 현상을 만들어 낸 무언가를 본다면 탄성 대신 신음을 내뱉었을 것이다.

바로 지금의 나처럼.

“이건…….”

말꼬리를 흐린 나는 ‘그것’을 바라보았다.

소나기처럼 떨어져 내리는 연못의 물방울과 꽃잎들 사이, 지면 깊숙이 틀어박힌 채 서늘한 예기(銳氣)를 뿜어내는 그것은 익히 아는 형태의 무기였다.

“언월도(偃月刀)?”

반사적으로 뇌까린 그때. 낮은 중저음의 목소리가 귓가를 파고들었다.

“단순히 언월도라고 하면 섭섭한데.”

목소리가 들려온 방향을 따라 고개를 돌리자 내심 짐작했던, 그러나 이곳에서 만나기 싫었던 얼굴이 보인다.

금의위 지휘사 백연.

세인들이 두려움을 담아 혈사자(血使者)라고도 부르는 그를 향해, 나는 담담하게 입을 뗐다.

“그럼?”

“금룡(金龍). 그 녀석의 이름이야. 벌써 삼십여 년 세월을 함께한 애병이지.”

“금룡이든 금쪽이든 나야 별 관심 없긴 한데, 그래도 의외네.”

“무엇이 말인가?”

“그냥. 당신의 애병이라면 금룡보다는 혈룡(血龍)이 맞지 않나 싶어서.”

뼈 있는 물음에 거침없이 다가오던 백연이 문득 걸음을 멈췄다.

“이미 나에 관한 이런저런 소문을 들었나 보군.”

“익히 들었지. 한 십 년 전쯤에 금쪽이가 잔뜩 포식했겠더라고. 사람을 그렇게 죽여 댔으니.”

“금쪽이가 아니라 금룡이고, 필요한 일이었지.”

“그래, 물론 필요한 일이었겠지.”

나는 소교와 백연을 번갈아 바라보며 빈정거렸다.

“다른 사람들에게는 알려지지 않은 여러 의미에서.”

“글쎄. 굳이 변명하진 않겠네만, 자네가 알거나 짐작하는 것 중 절반만 사실이라고 해도 언행을 신중히 해야 하지 않을까?”

“언행을 신중히 해라?”

나는 헛웃음을 흘렸다.

“이런 좆 같은 상황에서는 황제가 아니라 황제 할아비가 와도 쌍욕 박아야지. 안 그래?”

억지로 입꼬리를 끌어올려 보지만, 가슴 한구석이 꽉 막히는 듯한 답답함마저 어쩔 수는 없었다.

당장 소교 하나 상대하는 것조차 필사(必死)의 각오로 임하려던 마당에, 이제는 백연까지 오다니.

‘이렇게 빨리 오리라곤 예상 못 했는데. 날 제거하는 건 이미 계획된 거였나?’

최악이라는 표현으로도 지금 상황을 모두 담아내기는 역부족이다. 나는 무거운 마음으로 몇 발자국 앞에 놓인 언월도를 움켜쥐었다.

스릉.

단단한 지면을 두부 가르듯 베어 내며 뽑혀 나온, 투명하리만치 맑은 은빛 도신(刀身).

남의 것이기에 낯설면서도 한편으로는 익숙한 그 예기를 느끼자 잠시 가라앉았던 마음이 들끓었다.

“만년한철(萬年寒鐵)이라, 금의위 지휘사라 그런지 무기도 기깔 나네. 금쪽이는 내가 좀 쓴다.”

백연이 턱수염을 쓰다듬으며 대꾸했다.

“곤란한 제안이군.”

“어째서?”

“그것으로 나와 그녀를 베려 할 테니까.”

“그럼 애초에 던지질 말았어야지.”

“급했으니 별수 있나.”

백연이 어깨를 으쓱하며 말을 이었다.

“나름의 깊은 의미도 있다네. 금의위 지휘사로 임명받은 날, 선황(先皇)께서 친히 하사하신 병장기거든.”

“그럼 더 상관없겠네. 선황 그 양반도 내가 쓰는 걸 더 원할 테니까. 이걸로 역적 새끼 때려잡겠다고 하면 저기 저 연못에서 뛰쳐나와서 은쪽이도 던져 줄걸?”

“……!”

“그리고 이건 제안이 아니야. 통보지.”

그 순간, 나는 봤다.

백연의 굵은 눈썹이 잠깐이지만 꿈틀거리는 것을.

그리고 내려앉은 잠깐의 침묵 뒤, 놈의 입술 사이로 침잠한 목소리가 흘러나왔다.

“꼭 이리 소란을 일으켜야겠나?”

“고작 소란 정도로 끝날까.”

나는 대화 도중에 수정한 계획을 조용히 되새겼다.

‘이대로 붙는다면 개죽음밖에 안 돼. 어떻게든 주위의 이목을 최대한 이쪽으로 끌어모아야 한다.’

나보다 윗줄의 고수를, 그것도 둘이나 동시에 상대해야 한다면 그 결과는 어떨까.

깊게 생각해 볼 필요도 없다. 이건 필패(必敗)다.

‘일섬(一殲)이라는 마지막 수가 있긴 하지만, 그조차도 먹혀 들지 장담할 수 없다.’

일섬은 무적이 아니고, 내 몸뚱어리는 이미 한계에 다다랐다.

레벨 업을 이용한 회복력이 있었음에도 이 지경까지 왔는데 시스템이 없는 지금은 어떻겠는가.

‘그야말로 최후의 한 수가 되겠지.’

문제는 목숨까지 불살라 가며 내지를 그 최후의 한 수가, 저승길 길동무 하나 데려가지 못하는 자살 유도 엔딩이 될 수도 있다는 거다.

‘그건 좀, 선 세게 넘네.’

헛방 치고 제풀에 지쳐 죽은 병신 혹은 SSS급 자살 헌터가 되고 싶은 마음은 조금도 없다.

상황이 이렇게 된 이상 전면전으로 끌고 나갈 수밖에.

저들은 저들 나름의, 마삼보를 위시한 반(反) 황제파에게는 그들 나름의 계획이 있었겠지만 지금의 내게는 아무런 상관도 없다.

아니, 저 두 괴물 앞에서는 그런 걸 생각할 여유조차 없다는 것이 옳은 표현일 것이다.

‘기왕 이렇게 된 거, 내가 할 수 있는 모든 지랄을 다 떨어 주마.’

다행히도 황궁 내부에는 조력자가 있다.

정확한 사정은 모르겠으나 마삼보가 끌어들인 무림의 살수들이 있고, 무엇보다 화왕(火王) 적천강이 떡하니 버티고 있었다.

‘기존의 반정 세력은 당연하고.’

충분히 승산 있는 전투.

계산이 섰으니 망설일 필요가 없다. 나는 즉각 이 자리를 벗어날 생각으로 손에 쥔 언월도를 비스듬히 세웠다.

우우웅.

한 주인과 오랫동안 함께한 병장기에는 나름의 혼이 깃든다고 했던가?

낯선 주인, 낯선 기운을 거부하듯 부르르 떨리는 도신을 보니 지금은 태원진가의 가신이 된 철기방(鐵騎幇)의 방주, 장태보가 언젠가 했던 말이 문득 떠올랐다.

하지만…….

‘찌그러져 있어라.’

화륵.

그 잠깐의 반항은 곧이어 솟구친 청백색의 화염과 함께 사라졌고, 나는 전력을 다해 신형을 쏘았다.

아니, 그러려고 했다.

염화일로(炎火一路)의 불꽃이 발끝에서 터져 나오려던 그 순간. 불현듯 귓가를 파고든 소교의 한 마디가 아니더라면.

“후회하기 전에 멈추는 게 좋을 거야.”

“뭐?”

“상산왕 주표.”

“……!”

고작 다섯 글자였지만, 그것만으로도 내 발걸음을 묶어 놓기에는 충분했다.

갑작스러운 이 혼란 속에서 간과하고 있던 한 가지 사실.

맞다.

아직 놈들의 수중에는 그 어린아이가 있다.

상산왕이 건청궁에 있는 한 생사여탈권(生死與奪權)은 황제가 쥐고 있는 것이나 다름없었다.

건청궁은 복마전이다. 당장 내 눈으로 직접 확인한 것만 해도 황제를 비롯해 무려 네 명의 초절정 고수가 포진해 있는.

나나 화왕이 아니라, 설령 무신(武神)이 돌아온다 해도 어린 왕의 턱밑에 닿아 있는 비수까지 어쩌지는 못할 것이다.

“선택해. 어떤 길을 갈지. 그곳에 무슨 결과가 기다리고 있는지도.”

담담한 어조와는 달리 주위를 감싼 그 서늘한 공기 속에서, 나는 악문 잇새 사이로 목소리를 쥐어 짜냈다.

“도대체…… 뭘 얻기 위해 이렇게 하는 거지?”

“알 것 없어. 중요한 건 오늘 당장 네가 이 자리에서 살아남았다는 거겠지.”

살아남아? 내가?

그것도 약점까지 잡은 지금, 암천의 끄나풀들이 나를 이대로 순순히 놔주겠다고?

전혀 예기치 못한 말에 당황한 내가 눈만 깜빡이던 그때, 소교가 덧붙였다.

“나 역시 그러길 바라고.”

“당신도?”

“그래,”

“……어째서?”

“아직은 살려야 할 이유가 있으니까. 그게 내가 맡은 임무이기도 하고.”

순간 나도 모르게 눈동자가 부릅떠졌다.

저것과 비슷한 말을, 나는 불과 몇 달 전에 들은 적이 있었기 때문이다.

그것도 다름 아닌 남천마후(南天魔后)에게서.

바로 그러했기에 지금의 소교와 당시의 남천마후의 모습이 겹쳐질 수밖에 없었다.

‘남천마후는 괴물의 형태로 변하기 직전까지도 내게 살수(殺手)를 최대한 자제했었지. 지금의 소교처럼.’

그렇다면 이것이 가리키는 의미는 하나뿐이다.

남천마후가 그랬듯이 소교도, 아니 천주는 여전히 나를 원하고 있다.

이미 혼이 떠나고 없는 싸늘한 시체가 아닌 바로 나.

열화신룡 진태경을.

‘왜지?’

도무지 이해할 수 없는 상황이었다. 나는 암천의 계획을 사사건건 가로막았고 그 과정에서 서천마군과 남천마후라는 손발을 잘라 내기까지 했으니까.

중원 무림과의 전쟁을 시작한 천주의 입장에서는 씹어 죽여도 시원치 않을 걸림돌 중 하나가 바로 나다.

‘그런데 어째서.’

불현듯 과거의 기억이 뇌리를 스친다.

사천당가의 지하 뇌옥. 분명 숨이 끊겼던 서천마군의 몸을 빌려 잠시나마 마주했던 그 짙은 어둠의 속삭임이.



‘재미있군. 재미있어.’



그리고 그 어둠 속에 스며 있던, 스산한 웃음이.



‘다음에 또 보도록 하지.’



“……!”

그때부터였나.

그것이, 그 한 마디가 시작이었나.

까득.

나도 모르는 새에 하얗게 물든 주먹 위로 핏줄이 도드라진다. 전신의 솜털이 곤두선 채 충격을 가라앉히는 나를, 소교는 담담하게 바라보았다.

“그래서, 대답은?”

나는 눈앞의 적이 있다는 사실도 잊고 지그시 눈을 감았다.

그리고 다음 순간.

쉬릭.

손에 쥔 언월도를 역수(逆手)로 전환하여 빛살처럼 쏘아 보냈다.

쐐애애액! 콰앙!

파공성에 이어 울려 퍼진 굉음.

한 발자국 앞 지면을 깊숙이 파고든 자신의 애병을 회수한 백연이 작게 혀를 찼다.

“돌려주는 방식이 제법 요란하군.”

불과 일각 전이었다면 한껏 비아냥거리는 어조로 받아쳤겠지만, 지금은 아니다.

나는 이를 악문 채 두 사람을 향해 입술을 뗐다.

“상산왕은…… 건드리지 마라.”

“안심하게. 자네가 걱정하는 그런 일은 벌어지지 않을 테니.”

저 대답이 진심인지 거짓인지, 나로서는 알 길이 없다.

다만 다른 방법을 찾아보는 수밖에.

‘그래도 하나는 얻었다. 천주의 명이 있는 한, 놈들이 나를 섣불리 건드릴 수 없다는 것.’

나는 소교와 백연을 향한 살기를 애써 억누르며 걸음을 옮겼다. 무림에서의 표현을 빌리자면, 지금부터야말로 일각이 여삼추다.

곧 황궁에서 개최될 대연회.

그 축제의 장이, 바로 운명을 결정지을 전장이 될 것이다.

‘홍문연(鴻門宴)이라, 누가 항우고 누가 유방일까.’

나는 망설임 없이 돌아서서 걷기 시작했다. 그리고 등 뒤에 남겨진 그들의 시야에서 완전히 사라지기 전, 불현듯 날아든 소교의 목소리를 들었다.

“왜 싸우기를 포기했지? 열화신룡 진태경. 너 역시 상산왕이 황제가 되길 바라나?”

순간 실소가 흘러나왔다.

딱히 대답할 가치도 없는 질문이라서.

하지만 나는 뒤도 돌아보지 않고 계속해서 걸음을 옮기며 대답했다.

“그래, 기왕 하는 거 당연히 그러길 바란다. 하지만 그것 때문만은 아니야.”

“그렇다면?”

“어린애잖아.”

나는 어딘지도 모르는 방향으로 계속해서 나아가며 중얼거렸다.

“아직 어린애라고. 이 미친 새끼들아.”
```

## Final English reading copy

```markdown
# Chapter 888

It all began and ended in the blink of an eye.

Whoosh!

A streak of light came hurtling in faster than the sound of it tearing through the air. And then…

KABOOM!

A deafening blast, followed by a tremendous shock wave that shoved my whole body backward.

“Hngh!”

Crack. I swallowed a breath and dug my feet in. The ground flipped up beneath them.

The gale whipped up by the impact sent the pond water surging high into the air and swept through the rare flowers and plants blanketing the grounds.

Whooosh.

If anyone had seen the scene, they might have been overwhelmed for a moment and gasped in awe.

Countless petals swirling on the wind really were a spectacular sight.

But even the most carefree, clueless person would have groaned instead of gasping if they’d seen what had caused it.

Just like I was doing now.

“This is…”

My voice trailed off as I stared at *it*.

Amid the pond water and petals raining down like a sudden shower, *it* stood embedded deep in the ground, radiating a chilling edge. It was a weapon in a shape I knew well.

“A crescent blade?”

The words slipped out before I could stop them. Then a low, resonant voice pierced my ear.

“Calling it just a crescent blade is a bit of an insult.”

I turned toward the voice. There was the face I’d half expected—and had very much hoped not to see here.

Baek Yeon, Commander of the Embroidered Uniform Guard.

I calmly addressed the man people called the Blood Envoy in fear.

“Then what is it?”

“Golden Dragon. That’s its name. It’s been my trusted weapon for over thirty years.”

“Golden Dragon, Goldie—doesn’t really matter to me either way, but I’m surprised.”

“Surprised by what?”

“Nothing. It just seems like if it’s your trusted weapon, Blood Dragon would suit it better than Golden Dragon.”

Baek Yeon had been approaching without hesitation, but at my pointed question, he came to an abrupt stop.

“Seems you’ve heard a few things about me.”

“Plenty. Sounds like Goldie had quite a feast about ten years ago. You killed a lot of people with it.”

“It’s Golden Dragon, not Goldie. And it was necessary.”

“Sure. I’m sure it was necessary.”

I glanced between So Gyo and Baek Yeon, speaking sarcastically.

“In more ways than the rest of us were told.”

“Perhaps. I won’t bother defending myself, but even if only half of what you know or suspect is true, shouldn’t you be more careful about what you say and do?”

“Careful about what I say and do?”

I let out a hollow laugh.

“In a fucked-up situation like this, I’d cuss out the Emperor himself—or his grandpa. Don’t you think?”

I forced up the corners of my mouth, but I couldn’t do anything about the tightness in my chest.

I’d already been preparing to face So Gyo alone, ready to fight to the death. And now Baek Yeon had shown up, too.

*I didn’t expect him to get here this fast. Was killing me already part of the plan?*

Even calling this the worst possible situation didn’t do it justice. Heavy-hearted, I stepped forward and gripped the crescent blade lying a few paces away.

Shing.

It slid free, cutting through the solid ground as easily as a knife through tofu. The blade gleamed with a clear, almost transparent silver sheen.

It felt unfamiliar because it belonged to someone else, yet that familiar cutting edge made the anger that had briefly settled in me surge back up.

“Ten-Thousand-Year Cold Iron. Guess the Commander of the Embroidered Uniform Guard gets a hell of a weapon. I’m borrowing Goldie.”

Baek Yeon stroked his chin beard as he replied.

“That’s a troubling offer.”

“Why?”

“Because you’ll try to cut me and her down with it.”

“Then you shouldn’t have thrown it over.”

“I was in a hurry. What else could I do?”

Baek Yeon shrugged and continued.

“It also has a deeper meaning to me. The late Emperor personally bestowed it on me the day I was appointed Commander of the Embroidered Uniform Guard.”

“Then all the more reason I don’t care. The late Emperor would rather I used it anyway. If I said I was going to beat the traitorous bastards with it, he’d jump out of that pond and throw me Silverie, too.”

“……!”

“And this isn’t an offer. It’s a statement.”

At that moment, I saw it.

Baek Yeon’s thick eyebrow twitched, just for a moment.

After a brief silence settled between us, his voice slipped through his lips, low and subdued.

“Must you really make such a fuss?”

“Will it end with just a fuss?”

I quietly went over the plan I’d revised while we talked.

*If I fight them here, I’ll just die for nothing. Somehow, I need to draw as many eyes as possible over here.*

What would happen if I had to fight two masters who were both above me?

I didn’t need to think hard about it. I’d lose. No question.

*I do have One Annihilation as a last resort, but I can’t even be sure that would work.*

One Annihilation wasn’t invincible, and my body was already at its limit.

Even with the recovery I got from Level Ups, my body had ended up like this. What would happen now, without the System?

*It’d be the final move in the truest sense.*

The problem was, even if I burned my life away to use it, I might not take a single person with me. It could turn into a suicide mission that got me killed after missing my target.

*That’s a little too far over the line.*

I had no interest in becoming some dumbass who died of exhaustion after whiffing—or an SSS-rank suicide Hunter.

Now that things had come to this, I had no choice but to turn it into an all-out battle.

They had their own plans, and so did the anti-Emperor faction led by Ma Sanbao. But none of that mattered to me now.

No—the more accurate way to put it was that I didn’t have the luxury of thinking about any of that with those two monsters in front of me.

*Since we’re here, I’ll pull every damn stunt I can.*

Luckily, I had allies inside the imperial palace.

I didn’t know all the details, but there were Murim assassins Ma Sanbao had brought in. And above all, the Fire King, Jeok Cheongang, was right there.

*And, of course, the existing forces plotting against the Emperor.*

We had a decent chance of winning this fight.

Now that I’d worked it out, there was no point hesitating. I angled the crescent blade in my hand, ready to leave at once.

Whooom.

They said a weapon that spent a long time with one owner could take on a soul of its own. Seeing the blade tremble as if it rejected its unfamiliar owner and strange energy, I suddenly remembered something Jang Taebo, the former Guild Leader of the Ironcraft Guild and now a retainer of the Jin Family of Taiyuan, had once said.

But…

*Stay bent out of shape.*

Fwoosh.

Its brief resistance vanished as blue-white flames flared up, and I launched myself forward with all my strength.

Or I would have.

If So Gyo’s sudden words hadn’t pierced my ear just as the flames of Flamefire Path were about to burst from my feet.

“You’d better stop before you regret it.”

“What?”

“Prince Shangshan. Zhu Bao.”

“……!”

Just five words, but they were enough to stop me in my tracks.

In all the confusion, I’d overlooked one thing.

Right.

They still had that child.

As long as Prince Shangshan was in Qianqing Palace, the Emperor held his life in his hands.

Qianqing Palace was a demon-slaying battleground. Just from what I’d seen with my own eyes, there were no fewer than four Supreme Peak masters there, including the Emperor.

It wouldn’t matter if it were me or the Fire King. Even if the Martial God himself returned, he couldn’t do anything about the blade at the young prince’s throat.

“Choose which path to take. And think about what awaits you at the end of it.”

Her tone was calm, but in the cold air surrounding us, I had to force my voice through clenched teeth.

“What the hell are you trying to get out of this?”

“You don’t need to know. What matters is that you’ll survive here today.”

*Survive? Me?*

The lackeys of Dark Heaven would just let me go, now that they had leverage over me?

Stunned by her completely unexpected words, I could only blink. Then So Gyo added,

“And I want you to survive, too.”

“You do?”

“Yes.”

“……Why?”

“Because there’s a reason I still need you alive. It’s also the mission I was given.”

My eyes flew open before I knew it.

I’d heard something like that only a few months ago.

From none other than the Southern Heaven Demon Empress.

That was why I couldn’t help seeing the Southern Heaven Demon Empress as she’d been then, overlaid with the So Gyo standing before me now.

*The Southern Heaven Demon Empress had held back from killing me as much as she could, even right up until she was about to turn into a monster. Just like So Gyo is now.*

If so, the meaning could only be one thing.

Just like the Southern Heaven Demon Empress, So Gyo—or rather, the Lord of Heaven—still wanted me.

Not my cold corpse, my soul already gone.

Me.

Jin Taekyung, the Blazing Flame Divine Dragon.

*Why?*

None of it made any sense. I’d thwarted Dark Heaven’s plans at every turn, even cutting off two of their limbs in the process: the Western Heaven Demon Lord and the Southern Heaven Demon Empress.

From the Lord of Heaven’s perspective, after starting a war with the Murim of the Central Plains, I was one of the obstacles he ought to chew to pieces.

*So why?*

A memory from the past flashed through my mind.

The underground prison beneath the Sichuan Tang Clan. The whispers of that deep darkness I’d encountered briefly when it borrowed the body of the Western Heaven Demon Lord, who had unmistakably died.



*“How interesting. How very interesting.”*



And the eerie laughter that had seeped through that darkness.



*“We’ll meet again.”*



“……!”

Had it started then?

Was that one remark where it all began?

Crack.

Without my noticing, the veins stood out on my fist, now gone white. My body hair rose as I tried to settle the shock. So Gyo watched me calmly.

“So, what’s your answer?”

I closed my eyes, forgetting for a moment that I had an enemy right in front of me.

Then, the next instant—

Swish.

I reversed my grip on the crescent blade and shot it away like a beam of light.

Whoosh! Kaboom!

The blade tore through the air, followed by a thunderous boom.

Baek Yeon recovered his weapon from where it had buried itself deep in the ground a step ahead of him and clicked his tongue.

“You have quite a dramatic way of returning it.”

If this had happened just fifteen minutes ago, I’d have fired back with a sarcastic quip. But not now.

I gritted my teeth and spoke to the two of them.

“Don’t… touch Prince Shangshan.”

“Rest assured. Nothing like what you’re worried about will happen.”

I had no way of knowing whether that answer was true or false.

All I could do was look for another way.

*Still, I got one thing out of this. As long as the Lord of Heaven wants me alive, they can’t just move against me.*

Suppressing the killing intent I felt toward So Gyo and Baek Yeon, I started walking. To borrow a saying from Murim, from this moment on, every fifteen minutes would feel like three autumns.

The grand banquet would soon be held in the imperial palace.

That festival would be the battlefield where our fates were decided.

*The Hongmen Banquet. So who’s Xiang Yu, and who’s Liu Bang?*

I turned and walked away without hesitation. Before I’d completely disappeared from their sight, with my back to them, So Gyo’s voice suddenly reached me.

“Why did you give up fighting? Blazing Flame Divine Dragon Jin Taekyung. Do you want Prince Shangshan to become Emperor, too?”

A laugh escaped me.

It wasn’t a question worth answering.

Still, I kept walking without turning around and replied,

“Yeah. Since we’re going this far, of course I want him to become Emperor. But that’s not the only reason.”

“Then what is?”

“He’s a kid.”

I kept walking in a direction I didn’t even know, muttering under my breath.

“He’s still a kid, you crazy bastards.”
```

<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0914.txt",
      "sha256": "ea2eb405de2fb04d85cdf5e118ffe803ef10d6449fa8295cf0aee14353fba4e2",
      "bytes": 14868
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "c117b34d12d29b4dc38cfd227e6e37a827415e0d7d5ab7549b5239092ca2f40f",
      "bytes": 1652
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "66855c040f4342a0b241cbbead8026d866de6b64af95427c21f76fe8c96ddd55",
      "bytes": 231435
    },
    {
      "path": "characters/Baek Yeon.md",
      "sha256": "eb5ab3e7037bb2e3f56db88dd243aea1f15343d9e8539fca7930e6bed6150202",
      "bytes": 837
    },
    {
      "path": "characters/Cang Gong.md",
      "sha256": "783e5a8a574e043233616483780e8614d049982388f2cdddaa3a9d592adbd050",
      "bytes": 765
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "a2e62b415aae2b1021b51166b08a992cc3b939dec67f3dbaaf6546d2a173b84b",
      "bytes": 759
    },
    {
      "path": "characters/Eastern Heaven Demon Lord.md",
      "sha256": "453411c29dd5f181a5dc666761819f5cdb0a2f2d039d83815811f3e35e4009aa",
      "bytes": 731
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "12795d6d344e95d3f197ae9ab14d9d32b4f3fb4be0bc9306f609df8f61fc5d9b",
      "bytes": 1270
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "96031b3161c1a773afc49f300755bbe4e36aed0a95375bc82d494c1cac6dbc92",
      "bytes": 1390
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "ddab84f4c2d3d1af543b6cb6200d503d7ab690160e1aed13fe4508c69d099f98",
      "bytes": 622
    },
    {
      "path": "characters/Ma Sanbao.md",
      "sha256": "86ba96d458d63d83681d354428f8c6fcea0b44bd87f3992b171ed490da1c1bde",
      "bytes": 850
    },
    {
      "path": "characters/Prince Shangshan.md",
      "sha256": "dff00cbb384aedb359a5d07d29aa146a55da4a31bb12fe26631a3561ef4c4abb",
      "bytes": 998
    },
    {
      "path": "characters/So Gyo.md",
      "sha256": "c214bfb2fa54aed4cd03733e70e7571900bb299713db1b5dc798020cf6be192e",
      "bytes": 900
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "3a94cb321253dba01ba17df72780ce292559aa12d2e1c6a31ae7a47a31bc09bc",
      "bytes": 263566
    }
  ],
  "estimated_tokens": 13528
}
-->

# Durable State Update — Chapter 914

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
1 and safe_through 914. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 914. Profile updates may replace only one
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
  "chapter": 914,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 914,
    "continuity_sources": [914],
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
    "Jeok Cheongang vowed to kill every member of Dark Heaven after Hong Dao was killed by the Blood Lord.",
    "Jeok Cheongang still suffers unexplained cold pain after the duel.",
    "The Eastern Heaven Demon Lord survived a seemingly fatal death and can no longer be described as human.",
    "The Eastern Heaven Demon Lord was once a Maoshan Sect disciple; the sect was destroyed resisting the forced relocation of the capital.",
    "The Eastern Heaven Demon Lord’s bell raises the dead as powerful, agile corpses that do not fear injury or death.",
    "Ma Sanbao, the Eastern Heaven Demon Lord’s Disciple, is among the risen dead following him.",
    "Jeok Cheongang is internally injured but his light-flames can burn the risen corpses to ash.",
    "The Eastern Heaven Demon Lord has advanced toward the Emperor and demands an account of Taizu’s actions against the Maoshan Sect.",
    "The banquet-hall battle continues as the risen dead break down the human formation."
  ],
  "continuity_sources": [
    913
  ],
  "open_questions": [
    "What caused Jeok Cheongang’s unexplained cold pain?",
    "How did the Eastern Heaven Demon Lord survive what appeared to be his death?",
    "Can Jeok Cheongang and Jin Taekyung stop the risen dead and protect the survivors?",
    "What did Taizu do to the Maoshan Sect?",
    "What will happen to the Emperor as the Eastern Heaven Demon Lord reaches him?"
  ],
  "safe_through": 913,
  "temporary_decisions": [
    "Keep “undead” as Jin Taekyung’s general term distinct from “jiangshi,” Jeok Cheongang’s Maoshan-related term."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 암천     | **Dark Heaven**                  |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 비급     | **martial arts manual**                          | “martial scroll” where object/context warrants        |
| 정파     | **orthodox faction**                             |                                                       |
| 제자     | **Disciple**                                 |
| 사형     | **Senior Brother**                           |
| 노부      | **this old man / I**                                            |
| 백연 | **Baek Yeon** | Commander of the Embroidered Uniform Guard. |
| 창공 | **Cang Gong** | The bedridden East Depot leader for whom Ma Sanbao acts. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 동천마군 | **Eastern Heaven Demon Lord** | Title of the absurd masked antagonist in Jin's nightmare. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 마삼보 | **Ma Sanbao** | The East Depot’s Brush-Holding Eunuch and second-in-command. |
| 상산왕 | **Prince Shangshan** | The City Lord and a member of the imperial family who orders the luncheon. |
| 소교 | **So Gyo** | The palace attendant leading the group assigned to serve Prince Shangshan. |
| 기감 | **Qi Sense** | Taekyung's sensory technique; its range reaches seventy meters in this chapter. |
| 내상 | **Internal Injury** | System condition label for internal injury. |
| 개방 | **Beggars' Sect** | Murim organization counted among the Nine Sects and One Gang. |
| 선황 | **the late Emperor** | The former Emperor whom Hong Jin served. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 강시 | **jiangshi** | Reanimated corpse from folklore; Childeuk and Hong mistakenly identify Taekyung as one. |
| 육합전성 | **Six-Harmonies Voice Transmission** | Supreme Peak martial art that transmits the user's voice from every direction. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 인내 | **Endurance** | System attribute replacing Toughness. |
| 대성 | **Great Completion** | Completion stage of a martial technique. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 천주 | **Lord of Heaven** | Authority invoked by the masked attackers. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 강소 | **Jiangsu** | Province at the eastern end of the Yangtze route. |
| 초인 | **superhuman** | A being who has surpassed ordinary human limits. |
| 철옹성 | **impregnable fortress** | Metaphor for Ares Guild's entrenched defenses. |
| 고든 | **Gordon** | Pentagon employee tasked with repairing smashed warning lights. |
| 신물 | **divine artifact** | General term for a sacred or divine object, distinct from 신석. |
| 모산파 | **Maoshan Sect** | Jiangsu sect known for sorcery, destroyed by the founding emperor. |
| 태조 | **Taizu** | The Great Nation’s founding emperor. |
| 남경 | **Nanjing** | Former imperial capital in Jiangsu Province. |
| 동창 | **East Depot** | Imperial agency named by Hong Jin. |
| 황도십이궁 | **Twelve Palaces of the Zodiac** | Collective title for twelve Supreme Peak masters representing the imperial court. |
| 금위군 | **Imperial Guards** | Imperial force distinct from the Embroidered Uniform Guard. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 진태경 | 백연 | young martial artist confronting an imperial military commander | you | casual and insulting | Refers to Baek as 이 양반 while challenging his conduct. |
| 진태경 | 상산왕 | protector addressing a young prince | His Highness | respectful royal address | Taekyung refers to the prince as 상산왕 전하 when ordering Mujin to bring him. |
| 진태경 | 황제 | guest of the Emperor’s younger brother addressing the Emperor | Your Majesty | formal and deferential in address, despite blunt challenges | Taekyung repeatedly addresses the Emperor as 폐하. |
| 상산왕 | 황제 | younger brother addressing the Emperor | Your Majesty | deferential royal address | Shangshan addresses the Emperor as 폐하 while pleading for Taekyung. |
| 소교 | 진태경 | palace attendant addressing a martial artist and guest under escort | Young Master Jin | formal and respectful, but firm | Addresses him as 진 공자 while escorting him and warning him not to investigate. |
| 진태경 | 소교 | palace attendant and martial artist under imperial scrutiny | you | formal-polite, controlled and challenging | Taekyung addresses So Gyo as 당신 while questioning her presence and demanding an explanation. |
| 백연 | 진태경 | imperial commander confronting a young martial artist | Jin Taekyung | measured and familiar, using 자네 | Baek Yeon cautions Taekyung about his words and asks whether he must cause a scene. |
| 소교 | 백연 | political ally addressing a senior military commander | you | informal and direct | So Gyo uses 당신 and speaks without formality; no personal name or title is established. |
| 백연 | 소교 | military commander addressing a powerful political ally | you | formal and deferential | Baek Yeon uses 그대 while questioning So Gyo; she speaks without formality, which he accepts as her due. |
| 마삼보 | 진태경 | political ally recruiting a young martial artist | you; my friend | courteous and familiar | Ma uses 자네 and 이보게 while explaining his choice of Jin and inviting him to join the restoration army. |
| 진태경 | 마삼보 | young martial artist addressing the East Depot’s Brush-Holding Eunuch and prospective ally | you; Brush-Holding Eunuch | polite and direct | Jin asks Ma why he withheld information and presses him for a clear answer; he refers to him as 태감. |
| 황제 | 진태경 | Emperor addressing a subject and Prince Shangshan’s guest | Jin Taekyung | formal and authoritative | The Emperor addresses Taekyung by his family and personal name before asking what to do with the two officials. |
| 적천강 | 창공 | hostile opponents | you; you bastard | blunt and threatening | Jeok Cheongang uses 네놈, 이 불알 없는 놈, and 호로새끼 while taunting Cang Gong. |
| 창공 | 적천강 | hostile opponents | Fire King Jeok Cheongang | taunting and sardonic | Cang Gong names Jeok by his title, then comments on how alike master and disciple are. |
| 황제 | 소교 | Emperor questioning a political ally | you | quiet and direct | The Emperor questions So Gyo through Sound Transmission about why she is only watching. |
| 소교 | 황제 | political ally answering the Emperor | Your Majesty | calm and direct | So Gyo answers the Emperor through Sound Transmission without wavering. |
| 적천강 | 동천마군 | enemies | you | blunt and informal | Jeok Cheongang addresses the Eastern Heaven Demon Lord with hostile familiarity. |
| 동천마군 | 적천강 | enemies | you | informal | The Eastern Heaven Demon Lord speaks to Jeok Cheongang during their duel. |
| 마삼보 | 동천마군 | disciple_to_master | Master | deferential | Ma Sanbao addresses the Eastern Heaven Demon Lord as 스승님 when rejoining him. |

## Listed compact profiles

### Baek Yeon.md

# Baek Yeon (백연)

- **Safe through:** Chapter 907
- **Aliases:** Blood Envoy
- **Role:** Baek Yeon is the Commander of the Embroidered Uniform Guard, a former martial arts instructor to the Crown Prince, and the Blood Envoy who helped the fourth prince seize the throne and led the purge.
- **Personality:** Politically assured and controlled, he enforces authority with ruthless decisiveness but speaks with striking defiance to the Emperor in private when their shared undertaking is at stake.
- **Voice:** Not established
- **Relationships:** He commands the Embroidered Uniform Guard and serves the Emperor, carrying out the late Emperor’s final command to plan for the future alongside the fourth prince; he treats Taekyung as a dangerous potential obstacle.

### Cang Gong.md

# Cang Gong (창공)

- **Safe through:** Chapter 912
- **Aliases:** None
- **Role:** Cang Gong is the former Maoshan Sect member who became the East Depot’s Brush-Holding Eunuch and the Eastern Heaven Demon Lord of Dark Heaven.
- **Personality:** Calculating and self-assured, he admires Taekyung's ability while believing the Lord of Heaven's power will make him submit.
- **Voice:** Dry and sardonic, he delivers taunts and judgments in measured statements.
- **Relationships:** He was raised by a master and fellow disciples in the Maoshan Sect, whose members died resisting the forced relocation of the capital; Ma Sanbao is his disciple, and he regards Jin Taekyung as a potential recruit.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 913
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Eastern Heaven Demon Lord.md

# Eastern Heaven Demon Lord (동천마군)

- **Safe through:** Chapter 913
- **Aliases:** None
- **Role:** The Eastern Heaven Demon Lord is a being no longer human, a former Maoshan Sect disciple who commands the dead with a bell.
- **Personality:** His hatred of rulers is rooted in the loss of his family to the violence of the age of chaos and the destruction of the Maoshan Sect, where he had found happiness.
- **Voice:** He speaks in measured, almost lyrical phrasing, recounting the past before turning to pointed accusations.
- **Relationships:** Ma Sanbao is his Disciple; he holds the Emperor responsible for Taizu’s actions against the Maoshan Sect.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 913
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; believes there is no absolute justice and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He deeply trusts Jin Taekyung, his publicly acknowledged Disciple and intended heir, regards him as the light of his later years, and will stand by him whatever path he chooses; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and remains Peng Cheolhu's rival.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 913
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader.
- **Personality:** Hungry, self-aware, dryly observant, and pragmatic under pressure; accepts extreme personal risk when duty and the lives of others demand it.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; Taekyung killed Ma Sanbao during the banquet-hall battle, while Jeong Hogun and the Embroidered Uniform Guard have declared themselves allies of the Emperor, and So Gyo’s allegiance remains unknown.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 913
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Ma Sanbao.md

# Ma Sanbao (마삼보)

- **Safe through:** Chapter 913
- **Aliases:** None
- **Role:** Ma Sanbao is the East Depot’s Brush-Holding Eunuch and a Supreme Peak martial artist who secretly led a restoration effort for Prince Shangshan as a disciple of the Eastern Heaven Demon Lord.
- **Personality:** He is vigilant and patient, concealing his loyalties while awaiting the moment to act for the late Emperor.
- **Voice:** He speaks in measured, courteous language and uses calm repetition, feigned agreement, and procedural reminders to steer conversations while keeping sensitive details guarded.
- **Relationships:** Ma Sanbao was a longtime friend and former East Depot cohort of Hong Jin, served the Eastern Heaven Demon Lord, and led a restoration effort for Prince Shangshan.

### Prince Shangshan.md

# Prince Shangshan (상산왕)

- **Safe through:** Chapter 906
- **Aliases:** None
- **Role:** Prince Shangshan, whose personal name is Zhu Bao, is the Emperor’s twelve-year-old youngest younger brother, an exceptionally skilled young swordsman, and the heir publicly designated by the Emperor.
- **Personality:** Earnest and compassionate, he takes responsibility for his loyal subjects’ hardship, admires Jin Taekyung, seeks candid counsel, and shows composure beyond his years in the face of death and political danger.
- **Voice:** Archaic and formal in the manner of a historical drama, with openly eager and childlike reactions beneath his royal diction.
- **Relationships:** Prince Shangshan Zhu Bao is the Emperor’s youngest younger brother; the late Emperor entrusted Hong Jin with his care. Zhu Bao admires Jin Taekyung, seeks to emulate him, and calls him a friend; the Emperor says he will take care of Zhu Bao.

### So Gyo.md

# So Gyo (소교)

- **Safe through:** Chapter 907
- **Aliases:** None
- **Role:** A palace attendant assigned to Prince Shangshan who is a Supreme Peak master and has a mission to keep Jin Taekyung alive; her identity and allegiance remain unconfirmed.
- **Personality:** Calm, calculating, and self-possessed; she conceals her strength and identity and can be openly taunting.
- **Voice:** Measured and composed, shifting from deferential formality to casual, pointed taunts and threats.
- **Relationships:** She poses as the leader of the palace attendants assigned to Prince Shangshan and is Jin Taekyung’s opponent, yet believes he may be the person she seeks and the person foretold by “that person”; she says only she and the Emperor know a secret she withheld from Baek Yeon, while her true allegiance remains unknown.

## Korean source

```text
＃914화



딸랑.

머릿속에서 울려 퍼지는 듯한 그 또렷한 방울 소리에, 황제는 불현듯 극심한 두통을 느꼈다.

모산파.

흐릿하게나마 기억 속에 남아 있는 이름이었다.

그를 비롯한 모든 황자는 하나같이 제왕학(帝王學)을 배웠고, 대국과 황실의 역사를 꿰고 있어야 했으니까.

그리고 그중에는 모산파에 관련된 기록 역시 있었다.

정확히는 ‘모산의 난’이라 불리는 사건이.



평정(平定) 3년.

태조(太祖)께서 강소성 남경을 황도로 천명하시자, 이에 반발한 모산(茅山)의 반역도당이 무리를 규합하여 맞서다.



비록 사관들이 기록한 역사서에는 짧게 언급되었으나, 그 사건이 지닌 파급력은 상당했다.

길고 치열했던 군웅할거의 시대가 저물고, 대륙 최후의 승자이자 무소불위의 절대자로 자리매김한 초대 황제에게 정면으로 반기를 든 사건이었으니.

‘그랬기에, 그 어느 때보다 무자비했지.’

통일왕조를 설립한 태조는 그 위대한 업적만큼이나 잔혹한 인물이었다.

긴 세월 동안 내려온 사문의 근거지를 빼앗길 위기에 처한 모산파가 천도에 반발하여 세력을 모은다는 소식이 황실에 전해진 그 날, 태조는 즉각 출병(出兵) 명령을 내렸다.

그리고 그로부터 사흘 뒤.

모산파는 세상에서 사라졌다.

그들이 목숨 걸고 지키고자 했던 산은 화마에 휩싸였고, 모산파라는 세 글자와 연관된 모든 것들은 끊임없이 밀려드는 병사들의 칼날에 난자되어 장작으로 던져졌다고 했다.

인간과 가축의 구분 없이.

살아 있는 것과 죽어 있는 것을 가리지 않고.

하지만…….

‘기록이 틀렸다. 살아남은 자가 있었어.’

황제는 송곳처럼 머릿속을 들쑤시는 두통을 참아내며 끝없이 깔린 계단 아래를 굽어보았다.

그곳에는 오직 이날을 위해 기나긴 세월을 인내하며 살아남은, 모산파의 마지막 뿌리가 그를 응시하고 있었다.

원한을 단 한 순간도 잊어 본 적 없는 자만이 보일 수 있는 증오 어린 눈동자로.

“항상 궁금했지. 그대가 무슨 이유로 황실을, 대국을 무너트리려 하는지.”

황제는 천천히 옥좌에서 일어났다. 길고 화려한 용포(龍袍)의 옷자락이 지면을 스쳤다.

스륵.

느릿하게 나아가는 발걸음. 곁에 있던 백연이 굳은 얼굴로 앞길을 가로막았으나, 황제는 멈추지 않았다.

저벅저벅.

한 걸음. 또 한 걸음.

황제는 진홍빛 비단이 깔린 계단을 밟으며 밑으로 향했고, 한때는 군신(君臣)의 관계로 묶여있던 그들은 서로를 향해 조금씩 가까워졌다.

중간에 이르러 황제의 발걸음이 멈추기 전까지는.

그의 갈라진 입술 사이로 나직한 음성이 흘러나오기 전까지는.

“그래서 선황 폐하를, 아바마마를 배신했나?”

“배신?”

불쑥 던져진 물음에, 동천마군은 소리 내어 웃었다.

웃음소리와는 달리 괴물처럼 일그러진 얼굴로.

“누가 누구를 배신했단 말이냐. 단 한 순간도 네놈들에게 충성을 다한 적이 없었거늘.”

실로 오랜 세월을 기다려 왔던 그다.

배신감과 복수심을 되새기며 지샌 밤이 며칠이던가.

멸문의 끝자락에서 스승에게 건네받은 비급들을 익히기 위해 흘린 핏물이 몇 동이던가.

소년은 대국이라는 철옹성을 가장 확실하게 허물어트리기 위해 환관이 되기를 택했고, 청년이 된 어느 날 불현듯 찾아온 불청객의 제안을 받았다.



‘전능하고 위대하신, 천주의 말씀을 전합니다.’



그리고 그날, 청년은 마군(魔軍)이 되었다.

“아직도 모르겠느냐?”

동천마군은 차가운 회색빛 눈동자로 황제를 응시했다.

“배신당한 것은 너희가 아니다.”

그의 아비는 언젠가 태평성대가 도래하리라 입버릇처럼 말했고, 두 형은 붙잡히듯 전장에 끌려가면서도 살아 돌아오겠다고 약속했다.

그리고 지아비와 두 아들을 잃은 그의 어미는, 턱없이 어린 당신의 막내아들만큼은 살아남을 수 있을 거라 믿었다.

하지만 틀렸다.

그들의 믿음은 모조리 배신당했다.

모든 가족을 잃고, 억지로 떠밀린 전장에서 간신히 살아남은 소년에게 기적처럼 찾아온 두 번째 행복마저 앗아 갔다.

“이미 너희가 나를.”

그들 모두를.

“아니, 이 천하를.”

딸랑.

“배신했다.”

시종일관 서늘하던 동천마군의 음성이, 그의 눈빛이 용암처럼 들끓었다.

그에게 있어 먼저 배신당한 것은 자신이다. 만백성이고 천하다.

왕후장상(王侯將相)을 꿈꾸었던 군웅들의 아귀다툼에 가족을 잃었고, 또 다른 가족이 되어 주었던 스승과 사형제들은 무수한 창칼에 난자당했다.

그리고 그 이유는 단 하나였다.

황도 인근에 무림인이 없어야 한다는 태조의 뜻에 반하여 대대로 내려온 자신들의 터전을 지키려 했다는 것.

그뿐이었다.

“그렇기에, 너희는 죽어야만 한다.”

가장 비참하고 끔찍하게.

“오직 그 하나뿐인 소망을 위해, 나는 지금껏 인내하며 기다려 왔으니.”

소년이 청년으로, 청년이 중년으로, 그리고 마침내 백발이 성성한 노인이 되기까지는 참으로 긴 세월이 필요했으나, 그 시간은 결코 헛된 것이 아니었다.

동천마군이 뒤집어쓴 창공이라는 가면은 화려하고 강력했다.

동창의 정보력은 천하에 드리워져 있었고, 대국을 지탱하는 문무백관 중에는 그와 연이 닿아 있지 않은 이가 드물었다.

동천마군인 동시에 창공이었던 그는 황제 다음가는 권력자였다.

비록 용포를 걸치지 않았을 뿐, 일인지하 만인지상의 위상을 지닌 또 한 사람의 절대자였고 조정의 대부분이 그의 손아귀에 놓여 있었다.

심지어는 황실마저도.

“내가, 아니 우리가 바로…….”

자신을 굽어보는 황제를 향해, 동천마군은 끓어오르는 목소리로 말을 이었다.

“대국(大國)이다.”

“……!”

“……!”

주위의 공기가 차갑게 얼어붙었다. 그와 동시에 동천마군의 손에 들린 낡은 요령이 미친 듯이 떨리기 시작했다.

딸랑. 딸랑. 딸랑.

흡사 귀신의 울부짖음과도 같은 음파가 사방으로 퍼져 나간다.

더 크게, 더 멀리.

어느새 드넓은 대연회장을 넘어, 금위군의 시신으로 뒤덮인 석벽까지 닿을 만큼.

이미 처참한 모습으로 널브러진 그들을 죽음에서 일으켜 세울 만큼.

그아아아!

듣는 것만으로도 등골이 서늘해지는 포효가 밤공기를 떨어 울린다. 더욱 광포해지고, 강해진 괴물들은 뇌리에 울려 퍼지는 음파를 따라 나아갔다.

높게 이어진 계단을 향해. 그 중심에 선 황제를 향해.

그리고 파도처럼 밀려드는 망자들의 선두에는, 오직 이날만을 기다려 온 한 사람이 있었다.

“이제, 끝을 보자.”

스스로에게 다짐하듯 뇌까린 한 마디와 함께, 동천마군은 걸음을 내디뎠다.

아니, 단번에 쏘아져 황제를 찢어 죽이려 했다.

그 순간 귓가를 파고든 누군가의 목소리만 아니었다면.

“그만.”

“……!”

“뭘 하려는지는 알겠는데, 그쯤 해 두는 게 좋을 거야.”

우우웅.

공기가 흔들렸다.

분명 목소리의 주인은 하나인데, 들려오는 방향은 여럿이다.

어지간한 초절정 고수라 해도 엄두를 낼 수 없는 육합전성(六合傳聲)의 수법.

그 안에 담긴 무시무시한 공력을 느낀 동천마군이 입술을 깨물었다.

십여 년 전의 뼈아픈 과거를 떠올리며.

어느새 황제의 어깨 너머에서 자신을 굽어보고 있는, 한 여인을 지그시 바라보며.

‘소교(小嬌).’

겉으로는 그저 아름답고 현숙한 미부로 보였던 그녀지만, 이미 과거 한 차례 소교의 개입으로 뼈저린 실패를 겪어야 했던 동천마군은 똑똑히 느낄 수 있었다.

저 가느다란 몸 안에 얼마나 거대한 힘이 깃들어 있는지.

더불어 지난 세월 동안 자신이 얼마나 성장했는지.

그러나 한 가지 사실만큼은 도무지 알 방법이 없었다.

“도대체, 네년은 누구냐.”

깊게 가라앉은 동천마군의 눈동자에 소교의 모습이 고스란히 비쳤다.

암천과 동창의 정보력으로도 알아내지 못한 정체불명의 초인.

어느 날 갑작스럽게 나타나, 그의 육신과 영혼에 씻을 수 없는 상처를 안겨 주었던 일생일대의 대적.

동천마군은 그녀에게 입은 막중한 내상을 끝끝내 치료하지 못하고 스스로를 강시로 만들어야 했음에도, 여전히 소교의 정체를 확신할 수 없었다.

“대답해라. 네가 누구인지.”

정파 무림의 끄나풀이라면 상황이 지금에 이르기까지 방관하지도 않았을 테고, 황실이 비밀리에 키워 낸 고수라면 이미 훨씬 전에 나타나 자신을 저지했어야 옳다.

그러나 소교는 그 무엇도 아니었다.

얼핏 보면 곡도(曲刀)를 닮은 병장기를 각각 양손에 말아쥔 그녀는, 지금 이 순간에도 담담한 시선으로 그를 직시하고 있었다.

과거 전신을 둘러싸고 있던 흑의를 벗어던진 채.

몸 안에 가둔 거대한 힘을 스스럼없이 개방한 채.

스아아아아.

선명하다. 막강하다.

유형화된 미증유의 기운이 소교의 전신을 타고 올올히 피어올랐다. 상황과는 맞지 않는 평온한 목소리가 육방(六方)에서 울려 퍼졌다.

“글쎄, 나름의 사정이 있는 건 이쪽도 피차일반이라 맨입으로 말해 주긴 좀 그렇고…….”

저벅.

천천히 나아가는 발걸음. 그와 동시에 소교의 눈빛이 착 가라앉았다.

“지금이라도 칼 물고 자결하면, 그럼 한 번 정도는 고민해 볼게.”

“……!”

“아, 이제 그 정도로는 안 죽으려나?”

으득.

동천마군은 자신도 모르게 이를 악물었지만, 한 번 멈춰선 발걸음은 쉽게 떨어지지 않았다.

‘어째서.’

오늘날에 이르러서는 사문의 신공절학을 모조리 대성한 그다.

비록 모산파의 절학이 강시술을 비롯한 여러 술법에 치중되어 있다고는 하나, 동천마군은 죽음마저 자신의 것으로 받아들여 또 다른 의미의 초인으로 거듭났다.

한데…….

‘위험하다.’

본능적으로 직감할 수 있었다. 지금 섣부르게 움직였다가는 되려 소교에게 당하고 말리라는 것을.

죽어도 죽지 않고, 통증조차 느끼지 못하는 몸이 되었음에도 동천마군의 기감은 주인을 향해 끊임없이 경고를 보내고 있었다.

“스승님.”

제자인 마삼보의 낮은 목소리가 귓가를 파고들었지만, 동천마군은 미동도 하지 않은 채 말없이 소교를 바라보았다.

현재 그녀에게서 느껴지는 기파는 화왕 적천강과 비등한 수준.

동천마군이 지닌 전력을 가늠한다면 황제와 백연, 그리고 황제의 암중 호위가 있더라도 충분히 승산이 높은 싸움이다.

엄밀히 말해서 동천마군 스스로가 평가한 자신의 무위는 화왕이나 소교보다는 반 수 아래지만, 그를 포함한 휘하의 병력 모두가 끔찍하리만치 질긴 생명력을 바탕으로 동귀어진(同歸於盡)이나 다름없는 공격을 계속해서 이어 나갈 수 있었으니까.

팔다리가 잘려 나가도, 설령 가슴이 관통당한다 해도 그들은 멈추지 않을 것이다.

살아 있는 이들이 모조리 쓰러질 때까지.

저들의 몸뚱어리가, 그 안에 흐르는 피가 얼음장처럼 싸늘하게 식을 때까지.

‘어차피 황제와 상산왕을 잡으면, 혹은 저 여자만 죽이면 모든 것이 끝난다.’

죽고 죽이는 전투는 비단 이 공간에서만 벌어지는 것이 아니다. 지금쯤이면 두 개로 갈라진 대국의 군대가 황도를 중심으로 혈투를 벌이고 있을 테고, 승자는 자신들이다.

동천마군은 굳게 다물려 있던 입을 열었다.

“가라.”

딸랑.

모산파의 신물인 낡은 요령이 묘한 울림을 흘린 그 순간.

드드드드득!

물경 일천을 훌쩍 넘어가는 망자들이, 한때 금위군이라는 이름으로 불렸던 대국의 정예가 어느덧 대연회장을 가로질러 들이닥쳤다.

그아아아아!

그리고 괴성을 토해 내며 파도처럼 밀려드는 망자들의 군세를 향해, 두 줄기의 섬광이 터져 나왔다.

슈화악!

휘황한 빛이 번뜩였다.

동시에 황제의 앞을 가로막은 두 명의 초인. 백연과 소교가 터트린 막강한 강기(罡氣)가 죽은 이의 살점과 뼈를 짓이기고 부수었다.

콰드드득!

단숨에 선두를 으스러트리는 무시무시한 위력. 그러나 두 사람의 무위를 익히 알고 있던 동천마군은 조금도 놀라지 않았다.

‘이미 예상했던 바다.’

그러나 피륙으로 이루어진 인간은 결국 필멸(必滅)의 운명을 타고난 존재.

설령 초인이라 불리는 이들에게도 그 크기와 깊이가 남다를 뿐, 인간으로서 정해진 한계는 있었다.

‘틈을 노려, 단숨에 죽인다.’

동천마군은 깊게 가라앉은 눈으로 걸음을 옮겼다.

제자인 마삼보와 죽음에서 부활한 황도십이궁의 고수를 좌우로 거느린 채, 썩은 핏물과 조각난 시체로 뒤덮여 가는 계단을 밟았다.

철벅.

그리고 바로 그 순간.

“혹시, 지금 많이 바빠?”

상당한 거리를 두고 등 뒤에서 들려온 목소리에, 그는 불현듯 깨달았다.

어느덧 저 멀리서 울려 퍼지던 수하들의 괴성이 잦아들기 시작했다는 것을.

더불어 자신이 생각한 초인의 한계가, 어쩌면 그 이상일지도 모르겠다는 것을.

스륵.

굳은 얼굴로 돌아선 동천마군의 눈동자에, 이토록 빨리 재회하지 못할 거라 생각했던 두 사람의 얼굴이 비쳤다.

“거기 존나 못생긴 오빠. 많이 안 바쁘면 시간 좀 내주라.”

“그래, 노부가 아주 잘해 주마.”

적천강과 진태경.

혈인(血人)이나 다름없는 몰골을 한 그들이 새하얀 이를 내비치며 웃고 있었다.

서로를 꼭 닮은 모습으로.
```

## Final English reading copy

```markdown
# Chapter 914

*Jingle.*

At the clear chime, which seemed to ring inside his head, the Emperor was suddenly seized by a splitting headache.

The Maoshan Sect.

It was a name that remained, however faintly, in his memory.

He and every other prince had studied the art of ruling, and they were expected to know the history of the Great Nation and the imperial family inside and out.

That history included records concerning the Maoshan Sect.

More precisely, the event known as the “Maoshan Rebellion.”

> **Third year of Pyeongjeong.**
>
> When His Majesty Taizu declared Nanjing in Jiangsu the imperial capital, the treasonous Maoshan rebels opposed the decision, rallied their forces, and rose against him.

The event received only a brief mention in the histories written by court historians, but its repercussions had been considerable.

It was an open revolt against the first Emperor, who had ended the long, fierce age of warring heroes and established himself as the continent’s final victor and an absolute ruler with boundless power.

*That was why he’d been more merciless than ever.*

Taizu, founder of the unified dynasty, was as cruel as he was great.

The day the imperial court received word that the Maoshan Sect, facing the loss of its ancestral home after generations of inhabiting it, had gathered its forces to oppose the relocation of the capital, Taizu immediately ordered his troops to march.

And three days later, the Maoshan Sect had disappeared from the world.

The mountain they had risked their lives to protect was engulfed in flames. Everything connected to those three characters—Maoshan Sect—was hacked apart by wave after wave of soldiers and thrown onto the pyres.

No distinction between humans and livestock.

No distinction between the living and the dead.

But…

*The records were wrong. Someone survived.*

The Emperor endured the pain stabbing through his skull and looked down the seemingly endless flight of stairs.

There, gazing back at him, stood the Maoshan Sect’s last surviving root—the one who had endured through the ages for this day alone.

His eyes burned with a hatred that could belong only to someone who had never once forgotten his grudge.

“I’ve always wondered why you wanted to destroy the imperial family and the Great Nation.”

The Emperor slowly rose from his throne. The hem of his long, ornate dragon robe brushed the ground.

*Swish.*

He walked forward at an unhurried pace. Baek Yeon, standing beside him, blocked his path with a rigid expression, but the Emperor did not stop.

*Step. Step.*

One step. Then another.

The Emperor descended the stairs, carpeted in crimson silk, and the two men who had once been bound together as ruler and subject drew closer to each other.

Until the Emperor stopped halfway down.

Until a quiet voice slipped through his cracked lips.

“So you betrayed the late Emperor—my father?”

“Betrayed?”

At the abrupt question, the Eastern Heaven Demon Lord laughed aloud.

His face twisted into a monster’s, at odds with the sound of his laughter.

“Who betrayed whom? I never gave you bastards my loyalty for even a single moment.”

He had waited an awfully long time for this day.

How many nights had he spent reliving his sense of betrayal and thirst for revenge?

How many buckets of blood had he spilled mastering the martial arts manuals his Master had entrusted to him as the sect faced destruction?

The boy had chosen to become a eunuch so he could bring down the impregnable fortress of the Great Nation by the surest means possible. Then one day, when he was a young man, an unwelcome visitor had appeared and made him an offer.

*“I bring you the words of the almighty and great Lord of Heaven.”*

And that day, the young man became part of the demonic army.

“Do you still not understand?”

The Eastern Heaven Demon Lord stared at the Emperor with cold, gray eyes.

“You’re not the ones who were betrayed.”

His father had often said that an age of peace and prosperity would come someday. His two older brothers had been dragged off to the battlefield as though they were captives, yet they had promised they would return alive.

And their mother, who had lost her husband and two sons, had believed that at least her youngest boy—far too young to be on his own—would survive.

But she had been wrong.

Every last one of their hopes had been betrayed.

The boy had lost his entire family. He had barely survived the battlefield he’d been forced into, only for a second happiness—one that had miraculously found him—to be stolen away.

“You betrayed me first.”

All of them.

“No—the whole world.”

*Jingle.*

“You betrayed us.”

The Eastern Heaven Demon Lord’s voice, cold from beginning to end, and his gaze alike began to seethe like molten lava.

To him, he was the one who had been betrayed first. The common people. The world.

His family had been lost in the desperate struggles of heroes dreaming of becoming kings and ministers. His Master and fellow disciples, who had become another family to him, had been hacked apart by countless spears and swords.

And there had been only one reason.

They had tried to protect their ancestral home, passed down through generations, in defiance of Taizu’s decree that no martial artists could live near the imperial capital.

That was all.

“That is why you must die.”

In the most miserable, most horrific way possible.

“For that one wish alone, I have endured and waited all this time.”

It had taken a very long time for the boy to become a young man, the young man to become middle-aged, and finally for his hair to turn white. But those years had not been wasted.

The mask of Cang Gong, which the Eastern Heaven Demon Lord had worn, was magnificent and powerful.

The East Depot’s intelligence network stretched across the world, and few among the civil and military officials who upheld the Great Nation had no connection to him.

As the Eastern Heaven Demon Lord and Cang Gong, he was second in power only to the Emperor.

He might not have worn a dragon robe, but he was another absolute ruler—second to one, above all others—and most of the court lay in his grasp.

Even the imperial family.

“I—or rather, we are…”

The Eastern Heaven Demon Lord’s voice boiled as he spoke to the Emperor looking down at him.

“The Great Nation.”

“……!”

“……!”

The air around them froze. At the same time, the worn bell in the Eastern Heaven Demon Lord’s hand began to tremble wildly.

*Jingle. Jingle. Jingle.*

Waves of sound, like the wails of ghosts, spread in every direction.

Louder. Farther.

Until they crossed the vast banquet hall and reached the stone walls covered in the bodies of the Imperial Guards.

Until they could raise those who already lay there in a pitiful state from the dead.

*GRAAAH!*

A roar that chilled the spine alone shook the night air. The monsters, now more ferocious and powerful, advanced in response to the sound waves ringing through their minds.

Toward the towering stairs. Toward the Emperor standing at their center.

And at the head of the surging wave of the dead was a man who had waited for this day alone.

“Now, let’s see it through to the end.”

With those words, muttered as if making a vow to himself, the Eastern Heaven Demon Lord took a step.

No—he shot forward in an instant, intent on tearing the Emperor to pieces.

If not for the voice that pierced his ear at that very moment.

“Stop.”

“……!”

“I know what you’re trying to do, but you’d better leave it at that.”

*Hummm.*

The air shuddered.

There was clearly only one speaker, but the voice came from several directions.

The Six-Harmonies Voice Transmission technique—one beyond the reach of all but the most exceptional Supreme Peak masters.

Feeling the terrifying internal energy behind it, the Eastern Heaven Demon Lord bit down on his lip.

He remembered the bitter events of more than a decade ago.

Then he fixed his gaze on the woman looking down at him from just behind the Emperor’s shoulder.

*So Gyo.*

She looked, on the surface, like nothing more than a beautiful, elegant woman. But the Eastern Heaven Demon Lord had already suffered a bitter defeat once before because of her intervention. He could feel it clearly.

Just how much power was contained in that slender body.

And, along with that, how much he himself had grown over the years.

But there was one thing he still had no way of knowing.

“Who the hell are you, woman?”

So Gyo’s image was reflected in the Eastern Heaven Demon Lord’s sunken gaze.

An unknown superhuman whose identity had eluded even the intelligence networks of Dark Heaven and the East Depot.

His greatest enemy, who had suddenly appeared one day and inflicted a wound on his body and soul that would never heal.

Even after the grave Internal Injury she had given him refused to heal, forcing him to turn himself into a jiangshi, he still could not be sure who So Gyo was.

“Answer me. Who are you?”

If she were a spy for the orthodox factions, she would not have stood by and watched while things reached this point. If she were a master secretly raised by the imperial family, she should have appeared to stop him long ago.

But So Gyo was neither.

Holding a weapon in each hand, its shape reminiscent of a curved saber, she continued to look straight at him with an untroubled gaze.

She had cast off the black robes that had once covered her from head to toe.

She had freely unleashed the immense power she had kept confined within her body.

*Fwoooosh.*

It was unmistakable. Overwhelming.

An unprecedented energy, made visible, rose strand by strand from all over So Gyo’s body. Her calm voice, at odds with the situation, rang out from all six directions.

“Well, I have my own circumstances, just like you do, so I’m not sure I should tell you for free…”

*Step.*

She walked forward slowly. At the same time, So Gyo’s gaze turned cold.

“If you bite down on a sword and kill yourself right now, I might think about telling you.”

“……!”

“Oh. Would that not kill you anymore?”

*Crack.*

The Eastern Heaven Demon Lord clenched his teeth without realizing it, but his feet, stopped in their tracks, would not move easily.

*Why?*

By now, he had achieved Great Completion in all of his sect’s supreme techniques.

The Maoshan Sect’s arts might have focused on various forms of sorcery, including the art of controlling jiangshi, but the Eastern Heaven Demon Lord had accepted death as his own and become a superhuman in a different sense.

And yet…

*She’s dangerous.*

He knew it instinctively. If he moved carelessly now, So Gyo would get the better of him.

Even though his body could not die or feel pain, his Qi Sense kept sending its master warning after warning.

“Master.”

His Disciple Ma Sanbao’s low voice pierced his ear, but the Eastern Heaven Demon Lord did not move. He simply stared at So Gyo without a word.

The aura he felt from her now was on a level with the Fire King, Jeok Cheongang.

Considering the full strength of the Eastern Heaven Demon Lord, even with the Emperor, Baek Yeon, and the Emperor’s hidden guards present, he still had a good chance of winning.

Strictly speaking, he judged his own martial prowess to be half a step below the Fire King’s or So Gyo’s. But he and all his forces could keep launching attacks as tenacious as a mutual death strike, thanks to their horrifying vitality.

Even if their arms and legs were cut off, even if their chests were pierced, they would not stop.

Not until every living person had fallen.

Not until the bodies of their enemies and the blood flowing through them had gone cold as ice.

*If I capture the Emperor and Prince Shangshan—or kill that woman—this will all be over.*

The battle to the death was not taking place in this hall alone. By now, the armies of the Great Nation, divided into two, would be fighting a bloody battle around the imperial capital, and his side would win.

The Eastern Heaven Demon Lord opened his tightly shut mouth.

“Go.”

*Jingle.*

At the moment the worn bell, a divine artifact of the Maoshan Sect, gave off a strange chime—

*Rumble!*

More than a thousand of the dead, once the elite soldiers of the Great Nation known as the Imperial Guards, charged across the banquet hall.

*GRAAAAH!*

And two streaks of light burst out toward the army of the dead surging like a wave, shrieking as it came.

*Shwaaah!*

Brilliant light flashed.

At the same time, the overwhelming Force unleashed by two superhumans who had stepped in front of the Emperor crushed and smashed the flesh and bones of the dead.

*CRUNCH!*

Their power was enough to crush the vanguard in an instant. But the Eastern Heaven Demon Lord, who knew their abilities well, was not the least bit surprised.

*I expected this.*

But humans, made of flesh and blood, were ultimately fated to perish.

Even those called superhuman had limits set for them as humans, however far beyond ordinary those limits might be.

*I’ll wait for an opening and kill them in one strike.*

With his gaze sunken deep, the Eastern Heaven Demon Lord moved forward.

His Disciple Ma Sanbao and a master of the Twelve Palaces of the Zodiac, returned from the dead, flanked him on either side as he climbed the stairs, now covered in rotten blood and shattered corpses.

*Splash.*

And at that very moment—

“Are you busy right now?”

At the voice from behind him, from quite a distance away, he suddenly realized that the howls of his followers, which had been ringing out in the distance, were beginning to die down.

He also realized that the limits he had assumed applied to superhumans might, perhaps, go even further.

*Swish.*

The Eastern Heaven Demon Lord turned around, his expression rigid. Reflected in his eyes were the faces of two men he hadn’t expected to see again so soon.

“Hey, ugly-ass big bro. If you’re not too busy, make some time for me.”

“Indeed. This old man will take very good care of you.”

Jeok Cheongang and Jin Taekyung, both looking like blood-soaked men, bared their white teeth and grinned.

They looked so much alike.
```

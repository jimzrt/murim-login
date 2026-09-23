<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0906.txt",
      "sha256": "5e1557f8c8e6ed5f98a17134f9a6701c3c26ccd75ba913af278ae51df51b2f48",
      "bytes": 13433
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "eb42e22683fa29e43f38caf1e0fc71a09303d323e878f79c630682e69a19a889",
      "bytes": 1614
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "15b7559bed5551ab89a765328d3f0a3fb2d8b907d46fb1c26625499fb4cab311",
      "bytes": 230936
    },
    {
      "path": "characters/Cang Gong.md",
      "sha256": "c5fcfdda1816dfe014b74e860d998749f791746714e9472f020ea4622d2def21",
      "bytes": 687
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "b716cfe919fb370d34109de61c3c19dddc448ba0762a79a1dbad62f738b6e172",
      "bytes": 759
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "bf5abcb0ade03431d0da76adb043dacedef1c9c0d5ad2741778b3b2bfa0822fc",
      "bytes": 1499
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "434bb29386207342c6c6f9736678aba2046661707f26aae896151517c54ae710",
      "bytes": 1372
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "c98449c19662f6ad6fa67a4da83e62a4c1e02f7b909f22e40e695cba8cfd1bb0",
      "bytes": 622
    },
    {
      "path": "characters/Ma Sanbao.md",
      "sha256": "b6ba56edc33b7822687269a2be1b5e39b69e3ac33d455b327409ff04f8a559d8",
      "bytes": 1021
    },
    {
      "path": "characters/Prince Shangshan.md",
      "sha256": "81619f4ac8a1311a1e020faf5ebe6a2276aaf6db5f505ec2003f64b5df0811be",
      "bytes": 998
    },
    {
      "path": "characters/So Gyo.md",
      "sha256": "04a698f5d8a544b6136de22ce9a93a802d68f1ebb1324e36933e3f2a70f2b399",
      "bytes": 900
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "c336a9b74793e3bf73bdc6e4d5a7447e62c84594f5d5258f730ffe7383f34d3d",
      "bytes": 262942
    }
  ],
  "estimated_tokens": 11996
}
-->

# Durable State Update — Chapter 906

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
1 and safe_through 906. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 906. Profile updates may replace only one
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
  "chapter": 906,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 906,
    "continuity_sources": [906],
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
    "Cang Gong's unfamiliar chilling power is not simply Yin-Cold Qi; he intends to take Taekyung to the Lord of Heaven and believes Taekyung can be recruited.",
    "Attackers have infiltrated the Embroidered Uniform Guard, and the banquet-hall battle and assault on the Emperor are underway.",
    "Jeok Cheongang has joined Taekyung in the battle and is now fighting Cang Gong.",
    "Ma Sanbao killed several Embroidered Uniform Guards and confronted Taekyung, who attacked him; Ma's allegiance and motives are unclear.",
    "So Gyo's identity and allegiance remain unknown; she is watching Taekyung until he reveals his true self.",
    "The Emperor does not want Prince Shangshan endangered.",
    "Baek Yeon’s loyalty to the Emperor is bound to the late Emperor’s final command to plan for the future alongside the fourth prince.",
    "Prince Shangshan regards Taekyung as his only friend and has begged the Emperor to save him.",
    "Hyuk Mujin and the Fire Dragon Pavilion party are traveling to the Jiangsu–Zhejiang border on Taekyung's mission; silent figures have appeared in the nearby forest."
  ],
  "continuity_sources": [
    904,
    905
  ],
  "open_questions": [
    "Who is So Gyo, and is she an ally or enemy?",
    "What is the nature of Cang Gong's unfamiliar power, and what is his relationship to the Lord of Heaven?",
    "Why did Ma Sanbao kill the guards and confront Taekyung, and where does his allegiance lie?",
    "Who are the silent figures surrounding Mujin's group?"
  ],
  "safe_through": 905,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 혈도     | **acupoint** / **vital point**                   | Context dependent                                     |
| 검법     | **sword technique**                              |                                                       |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 생사결    | **life-and-death duel**                          | Explicitly lethal                                     |
| 강호     | **martial world**                                | Prefer “Murim” where the setting itself is meant      |
| 제자     | **Disciple**                                 |
| 일격     | **One Strike**                         |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 레벨               | **Level**                      |
| 창공 | **Cang Gong** | The bedridden East Depot leader for whom Ma Sanbao acts. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 마삼보 | **Ma Sanbao** | The East Depot’s Brush-Holding Eunuch and second-in-command. |
| 상산왕 | **Prince Shangshan** | The City Lord and a member of the imperial family who orders the luncheon. |
| 소교 | **So Gyo** | The palace attendant leading the group assigned to serve Prince Shangshan. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 공수납백인 | **Empty-Hand Seizes the Blade** | Technique for catching an opponent's weapon between bare fingers. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 근골 | **Muscles and Bones** | System attribute increased by 2 during the climb. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 천주 | **Lord of Heaven** | Authority invoked by the masked attackers. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 연검 | **flexible sword** | Ju Hwaran's weapon. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 열화신룡 | **Blazing Flame Divine Dragon** | New sobriquet bestowed on Jin Taekyung. |
| 비처 | **secret refuge** | Hidden retreat of the Dongting Fisherman. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 인자 | **ninja** | Japanese assassin skilled in concealment and concealed weapons. |
| 가기 | **singing courtesan** | The favored entertainer identity Honglan used in Hubei. |
| 동천마군 | **Eastern Heaven Demon Lord** | Title of the absurd masked antagonist in Jin's nightmare. |
| 화신 | **Fire God** | A local deity worshiped by one Nanman believer. |
| 금의위 | **Embroidered Uniform Guard** | Imperial guard force mentioned by Hong Jin. |
| 동창 | **East Depot** | Imperial agency named by Hong Jin. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 진태경 | 상산왕 | protector addressing a young prince | His Highness | respectful royal address | Taekyung refers to the prince as 상산왕 전하 when ordering Mujin to bring him. |
| 진태경 | 황제 | guest of the Emperor’s younger brother addressing the Emperor | Your Majesty | formal and deferential in address, despite blunt challenges | Taekyung repeatedly addresses the Emperor as 폐하. |
| 상산왕 | 황제 | younger brother addressing the Emperor | Your Majesty | deferential royal address | Shangshan addresses the Emperor as 폐하 while pleading for Taekyung. |
| 소교 | 진태경 | palace attendant addressing a martial artist and guest under escort | Young Master Jin | formal and respectful, but firm | Addresses him as 진 공자 while escorting him and warning him not to investigate. |
| 진태경 | 소교 | palace attendant and martial artist under imperial scrutiny | you | formal-polite, controlled and challenging | Taekyung addresses So Gyo as 당신 while questioning her presence and demanding an explanation. |
| 마삼보 | 진태경 | political ally recruiting a young martial artist | you; my friend | courteous and familiar | Ma uses 자네 and 이보게 while explaining his choice of Jin and inviting him to join the restoration army. |
| 진태경 | 마삼보 | young martial artist addressing the East Depot’s Brush-Holding Eunuch and prospective ally | you; Brush-Holding Eunuch | polite and direct | Jin asks Ma why he withheld information and presses him for a clear answer; he refers to him as 태감. |
| 황제 | 진태경 | Emperor addressing a subject and Prince Shangshan’s guest | Jin Taekyung | formal and authoritative | The Emperor addresses Taekyung by his family and personal name before asking what to do with the two officials. |
| 적천강 | 창공 | hostile opponents | you; you bastard | blunt and threatening | Jeok Cheongang uses 네놈, 이 불알 없는 놈, and 호로새끼 while taunting Cang Gong. |
| 창공 | 적천강 | hostile opponents | Fire King Jeok Cheongang | taunting and sardonic | Cang Gong names Jeok by his title, then comments on how alike master and disciple are. |
| 황제 | 소교 | Emperor questioning a political ally | you | quiet and direct | The Emperor questions So Gyo through Sound Transmission about why she is only watching. |
| 소교 | 황제 | political ally answering the Emperor | Your Majesty | calm and direct | So Gyo answers the Emperor through Sound Transmission without wavering. |

## Listed compact profiles

### Cang Gong.md

# Cang Gong (창공)

- **Safe through:** Chapter 905
- **Aliases:** None
- **Role:** Cang Gong is the East Depot leader and a formidable martial artist who intends to take Jin Taekyung to the Lord of Heaven for recruitment.
- **Personality:** Calculating and self-assured, he admires Taekyung's ability while believing the Lord of Heaven's power will make him submit.
- **Voice:** Dry and sardonic, he delivers taunts and judgments in measured statements.
- **Relationships:** He follows the Lord of Heaven and recalls a former master and fellow disciples as family; he now regards Jin Taekyung as a potential recruit.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 905
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 905
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm, the occupant of the chief seat of the Murim Alliance's Five Kings Hall, and a trusted confidant who accepts Jin as himself despite knowing that he travels between Murim and another world resembling the realm of immortals.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; believes there is no absolute justice and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He deeply trusts Jin Taekyung, his publicly acknowledged Disciple and intended heir, regards him as the light of his later years, and will stand by him whatever path he chooses; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and remains Peng Cheolhu's rival.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 905
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader.
- **Personality:** Hungry, self-aware, dryly observant, and pragmatic under pressure; accepts extreme personal risk when duty and the lives of others demand it.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; Ma Sanbao recruited Jin and Jeok for the restoration effort supporting Prince Shangshan, but their alliance is now in question after Ma confronted Jin during the banquet-hall battle.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 905
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Ma Sanbao.md

# Ma Sanbao (마삼보)

- **Safe through:** Chapter 904
- **Aliases:** None
- **Role:** Ma Sanbao is the East Depot’s Brush-Holding Eunuch and Supreme Peak martial artist, leading it in place of the bedridden Cang Gong and organizing a secret restoration effort for Prince Shangshan.
- **Personality:** He is vigilant and patient, concealing his loyalties while awaiting the moment to act for the late Emperor.
- **Voice:** He speaks in measured, courteous language and uses calm repetition, feigned agreement, and procedural reminders to steer conversations while keeping sensitive details guarded.
- **Relationships:** Ma Sanbao is a longtime friend and former East Depot cohort of Hong Jin, leads the restoration effort for Prince Shangshan, and recruited Jin Taekyung and Jeok Cheongang as allies; after killing several Embroidered Uniform Guards and confronting Jin during the banquet-hall battle, his present allegiance and motives are unclear.

### Prince Shangshan.md

# Prince Shangshan (상산왕)

- **Safe through:** Chapter 905
- **Aliases:** None
- **Role:** Prince Shangshan, whose personal name is Zhu Bao, is the Emperor’s twelve-year-old youngest younger brother, an exceptionally skilled young swordsman, and the heir publicly designated by the Emperor.
- **Personality:** Earnest and compassionate, he takes responsibility for his loyal subjects’ hardship, admires Jin Taekyung, seeks candid counsel, and shows composure beyond his years in the face of death and political danger.
- **Voice:** Archaic and formal in the manner of a historical drama, with openly eager and childlike reactions beneath his royal diction.
- **Relationships:** Prince Shangshan Zhu Bao is the Emperor’s youngest younger brother; the late Emperor entrusted Hong Jin with his care. Zhu Bao admires Jin Taekyung, seeks to emulate him, and calls him a friend; the Emperor says he will take care of Zhu Bao.

### So Gyo.md

# So Gyo (소교)

- **Safe through:** Chapter 905
- **Aliases:** None
- **Role:** A palace attendant assigned to Prince Shangshan who is a Supreme Peak master and has a mission to keep Jin Taekyung alive; her identity and allegiance remain unconfirmed.
- **Personality:** Calm, calculating, and self-possessed; she conceals her strength and identity and can be openly taunting.
- **Voice:** Measured and composed, shifting from deferential formality to casual, pointed taunts and threats.
- **Relationships:** She poses as the leader of the palace attendants assigned to Prince Shangshan and is Jin Taekyung’s opponent, yet believes he may be the person she seeks and the person foretold by “that person”; she says only she and the Emperor know a secret she withheld from Baek Yeon, while her true allegiance remains unknown.

## Korean source

```text
＃906화



지금 이 상황을 뭐라 표현해야 할지 모르겠다.

난전(亂戰)?

아니면 혈전(血戰)?

어쩌면 둘 다일 수도 있다. 발길이 닿는 곳마다 이름 모를 누군가의 시체가 밟히고, 지상과 하늘을 가리지 않고 적들의 창칼이며 화살촉이 쉴 새 없이 쇄도하고 있었으니까.

지금 이 순간조차도.

“조심!”

내 외침을 들은 금의위 중 하나가 화들짝 놀라며 허리를 비틀었다.

피핏!

날카로운 파공성과 함께 갈라지는 갑옷.

전장의 혼란을 틈타 그를 기습하려던 배신자의 칼날이 한 끗 차이로 빗나간 순간, 나는 망설임 없이 지면을 나뒹굴던 언월도(偃月刀) 한 자루를 걷어찼다.

쐐애애액! 뻑!

그 흔한 단말마조차 없었다.

섬광처럼 쏘아진 언월도는 표적을 관통한 것으로도 모자라 근처에 있던 적 두어 명을 꼬치처럼 꿰어 냈고, 아슬아슬하게 목숨을 건진 금의위는 나를 향해 살짝 고개를 끄덕여 보였다.

“고맙…….”

그리고, 두 번 다시 고개를 들지 못했다.

푹!

정확히 목젖을 관통한 화살.

피 가래 끓는 소리와 함께 쓰러진 금의위의 시신을 짓밟으며 들이닥친 적들이 닥치는 대로 병장기를 휘두른다.

이런 상황에 어울리지 않는, 그래서 더 소름 끼치게 느껴지는 침착한 목소리와 함께.

“천상천하(天上天下).”

“만마앙복(萬魔仰伏).”

무림으로 넘어오기 전, 마지막으로 상대했던 미친 광신도들이 떠오르는 것은 왜일까.

“미친놈들…….”

외마디 탄식이 곳곳에서 흘러나온다. 자신들이 걸친 황금빛 갑옷의 무게를 증명하기라도 하듯, 갑작스러운 아군의 배신에도 침착하게 전투를 이어 가고 있던 금의위들조차 완전히 다른 사람이 되어 버린 배신자들을 바라보며 두려움을 내비치고 있었다.

아니, 어쩌면 도저히 대적할 수 없을 것 같은 누군가의 무위 때문일지도 모르겠다.

철벅.

앞으로 나선 걸음과 함께, 가죽신이 피 웅덩이에 잠긴다.

자신도 모르게 뒷걸음질 친 금의위 중 한 사람의 입술 사이로 신음 같은 목소리가 흘러나왔다.

“마삼보…….”

그래, 바로 그였다.

병필 태감 마삼보.

동창의 이인자이자 실질적인 우두머리.

아니, 정확히는 그런 신분으로 세상을 속여 왔던 그가 나를 향해 걸음을 떼었다.

다가온다는 표현이 무색해질 만큼, 실로 섬광 같은 속도로.

쐐애액! 쾅!

머리 위에서 벼락처럼 쏟아지는 일격, 일격을 막을 때마다 저릿해지는 손아귀.

전과는 비교할 수도 없이 거칠어진 호흡은 물 흐르듯이 이어져야 할 움직임을 방해한다.

후욱, 훅.

가쁜 호흡을 내뱉으며 생각했다.

내가 이토록 고전하는 이유가 좋지 않은 몸 상태 때문인지. 아니면 그만큼 상대하기 어려운 강적을 만났기 때문인지.

그러나 그 생각조차도 길게 이어지지 못했다.

쉭!

살아 있는 뱀처럼 휘어진 연검(軟劍)이 콧날을 스친다.

갈라진 살갗을 비집고 흘러나오는 뜨거운 핏물. 타는 듯한 통증을 느끼며 물러나는 내 귓가로 낮은 웃음소리가 파고들었다.

“처음의 그 기세는 어디로 갔나, 응?”

나는 대답 대신 고개를 틀었다. 마삼보의 풍성한 소매에서 튀어나온 비수가 빛살처럼 빈 공간을 관통했다.

푹!

섬뜩한 소리와 함께 사라지는 또 하나의 생명.

그리고 아무 일도 없었다는 듯이 이어지는 목소리.

“안타깝군. 네가 피하지 않았더라면 저 젊은 금의위도 멀쩡히 숨이 붙어 있었을 텐데.”

빈정거리는 마삼보를 바라보며 생각했다.

만약 내가 피하지 않았다면 그는 살 수 있었을까?

이 전투에서 살아남아 언젠가 가족들의 곁으로 돌아갈 수 있었을까?

모르겠다. 아무것도.

괜한 죄책감에 기분이 더러워진다. 정작 지금 막 숨이 끊어진 저 금의위에게 미안해야 할 사람은 따로 있는데도.

‘어째서……!’

고개를 돌려 바라보고 싶었다. 나와 적천강. 자신의 수하들마저 이 전장에 몰아넣은 채 방관하는 황제와 소교의 눈을 똑바로 응시하며 묻고 싶었다.

왜, 어떤 이유로 이 지랄 같은 대연회를 열었느냐고.

전황을 뒤집을 힘이 있음에도 왜 나서지 않느냐고.

“도대체 왜!”

그리고 끝끝내 참지 못하고 터트린 그 외침에 답한 것은, 황제도 소교도 아닌 바로 마삼보였다.

“왜 저들이 수수방관하고 있는지, 아직도 모르겠나?”

실소를 터트린 놈이 말을 이었다.

“열화신룡 진태경. 네놈도 결국 황제에게 이용당한 거야. 우리가 자네와 화왕을 이용해서 소교를 제거하려 했던 것처럼.”

“……!”

“차도살인(借刀殺人). 피를 묻히기에는 남의 칼만큼 좋은 것이 없지. 화왕과 열화신룡이라는 명검이라면 더더욱.”

말해 주고 싶다.

그 아가리 닥치라고.

하지만 부정하고 싶은 마음과는 달리, 쉽게 입을 열 수 없었다.

그만큼 충분히 가능성 있는 이야기였으니까.

내가 직접 겪어 본 황제의 성격이라면.

그리고 도무지 정체를 알 수 없는 저 여자, 소교라면.

“너와 네 스승에게 남은 역할은 하나뿐이다. 죽을 때까지 발악하며 싸우다가, 끝끝내 죽는 것.”

쉬쉬쉬쉭!

날카로운 파공성과 함께 수십 개로 늘어난 연검이 사방에서 들이닥친다.

속도의 한계에 도달한 듯한 극쾌(極快)의 검법.

그러나 아무리 많은 잔상이 주위를 빼곡하게 에워싼다 하더라도, 결국 실체는 하나뿐이다.

카앙!

단순히 날붙이끼리의 충돌이라고는 믿기 힘든 굉음과 함께 밀려나는 신형.

이 기세를 놓지 않고 쉼 없이 휘둘려지는 연검 너머로 마삼보의 목소리가 이어졌다.

“대국은, 황제는 늘 그랬지. 이 광활한 천하를 차지한 지배자들에게 있어 나나 자네 같은 무림인은 다스려야 할 백성이 아니야.”

쉬쉬쉭, 핏!

검에 실린 압력을 이기지 못한 살갗이 베인다. 갈라진 살갗 틈새로 흘러나온 옅은 핏물이 허공에 흩뿌려졌다.

“내가 스승님을 따라 그분께 충성을 바치게 된 것도, 네가 오늘 이 자리에서 죽는 것도 결국 그래서다. 황제는 상산왕을 지키고 싶을 뿐이지, 강호의 무뢰배 따위를 구하기 위해 숨겨 둔 패까지 꺼내 들 생각은 없을 테니까.”

“뭐?”

순간 뇌리를 스친 어떤 깨달음에, 나는 눈을 크게 떴다.

상당한 거리가 있음에도 천둥처럼 울려 퍼지는, 저 멀리 적천강과 함께 굉음을 동반한 혈투를 벌이고 있는 한 사람에게 문득 생각이 미쳤기 때문이었다.

‘혹시?’

아니, 혹시가 아니다.

마삼보가 제 입으로 말했으니, 이건 짐작이 아닌 확신이다.

카가가가가각!

제각각 다른 강기가 부딪히며 불꽃을 토해 낸다.

본래는 하나로 이어져 있던. 그러나 마삼보의 강력한 공세에 두 자루의 단창이 되어 버린 그것을 교차시켜 연검을 막아 낸 나는, 코앞에서 멈춘 검신에서 흘러나오는 서늘한 기운을 느끼며 입을 열었다.

“창공. 창공의 제자였나?”

“창공? 감히 누구더러 저 음험하고 나약한 황제의 신하라 하는 것이냐.”

입매를 비틀며, 마삼보가 말을 이었다.

“동천마군(東天魔君). 그것이 바로 위대하시며 전능하신 천주께서 당신의 충복에게 내리신 새로운 이름이다.”

“……!”

“그리고 바로 그 동천마군의 제자가, 네놈을 무릎 꿇릴 테고.”

그 순간.

쉬리릭.

연검 특유의 탄성(彈性)을 머금은 검신이 휘어졌다.

마치 살아 있는 뱀처럼 앞을 가로막은 창대를 타 넘어 들이닥치는 섬광을 바라보며, 나는 교차했던 두 자루의 단창을 힘껏 위로 쳐올렸다.

카앙!

가슴을 향해 들이닥치던 연검의 방향이 뒤틀린다.

그러나 위험한 고비를 넘겼을 뿐, 그것으로 모든 공격이 끝난 것은 아니었다.

뻐억!

흡.

숨이 턱 막히고 시야가 번쩍인다.

훤히 드러난 앞가슴에 일권을 적중당한 나는 연거푸 십여 걸음을 물러났고, 그것은 곧 마삼보에게 있어 놓쳐서는 안 될 기회였다.

팟.

단 한 걸음.

그와 동시에 허깨비처럼 사라져 버린 마삼보의 신형.

그러나 몸 상태와 함께 무뎌진 감각 속에서도, 나는 기민하게 반응했다.

‘왼쪽!’

확신과 동시에 한 손을 흩뿌렸다.

비록 두 동강 난 탓에 긴 사정거리라는 본래의 이점을 잃었으나, 그와는 반대로 투창(投槍)에 최적화된 길이와 속력을 얻게 된 그것은 막강한 힘을 받아 쏘아졌다.

쐐애애액!

대기를 찢어발기는 한 줄기의 강맹한 파공성.

그리고 그 끝에서 울려 퍼진 거대한 충돌음.

콰앙!

굉음과 함께 지면에 가라앉아 있던 먼지가 솟아오르던 그 순간.

솨악!

공간이 갈라졌다.

단창을 튕겨 낸 연검이 휘황한 강기(罡氣)를 뿜어내며 먼지구름을 베어 내며 들이닥쳤다.

마삼보의 것이 분명한, 비웃음 섞인 전음과 함께.

- 걱정 말거라. 딱 죽지 않을 정도로만 베어 줄 테니.

그리고 그건 놈의 실수였다.

느려진 세상 속, 나는 다시 한번 허공을 뒤덮으며 쏟아지는 수십여 개의 검영(劍影)을 또렷하게 응시하고 있었으니까.

‘벤다고? 그것도 죽지 않을 정도로만?’

우스운 일이다.

아직 상대가 멀쩡히 두 다리로 서 있음에도 저따위 헛소리를 지껄이다니.

목숨을 건 생사결에서 승리한 자라면 상대에게 침을 뱉을 자격이 있다. 자신의 강함을 자랑하며 비웃어도 괜찮다.

하지만…….

‘그건 모든 것이 끝났을 때의 이야기지.’

육신은 물먹은 솜처럼 무겁고, 언제나 파도처럼 거침없이 흘러들어오던 공력은 가닥가닥 끊기고 있었지만 상관없다.

내 눈은, 아직 남아 있는 한 자루의 단창을 움켜쥔 손끝은 아직 흔들리지 않았으니.

‘보인다.’

슈확!

정확히 일점(一點)을 관통한 창날의 끝이, 수십의 검영을 지워 내며 실체에 맞닿은 순간.

콰앙!

강렬한 충돌음과 함께 그 여파를 감당하지 못한 신형이 튕겨 나간다.

내가 아닌, 마삼보의 신형이.

콰드득.

힘주어 내디딘 발끝이 지면을 갈아엎는다. 가까스로 흐트러진 신형을 바로 잡은 마삼보가 부릅뜬 눈으로 나를 바라보았다.

팟.

어느덧 자신의 코앞까지 들이닥친 나를.

“놈!”

비명 같은 외침과 함께 마삼보의 연검이 바람을 갈랐다.

극쾌라 칭하기에 부족함이 없는 속도로.

마치 빙하와 같은, 하지만 그보다도 더 차갑고 무자비한 강기를 흩뿌리며.

슈화아악!

그리고 모든 것을 얼려 버릴 듯한 그 기운 앞에서, 나는 전신의 모든 공력을 끌어올렸다.

화륵.

젖어 있던 장작에 불이 붙는다.

뒤틀린 철로처럼 불안정한 혈도를 타고, 그야말로 불길처럼 솟구친 열양지기를 손에 담아 옆구리를 막 파고 들어오던 검신을 붙잡았다.

콰득, 콰아아아!

힘과 힘의 격돌.

동시에 양손에서 전해지는 끔찍한 통증.

정확한 타이밍과 속도에 맞춰 날붙이를 잡는 공수납백인(空手納白刃)이 아닌, 그야말로 무식한 움켜잡기.

“이런 미친……!”

무림인이라면 마삼보의 저 말에 동감할 수밖에 없을 것이다.

이건 말 그대로 미친 짓이니까.

최소 한 수 아래의 하수라면 모를까, 비슷한 수준의 고수.

그것도 더 강한 공력을 지닌 상대로 이런 짓을 벌였다간 단숨에 양팔이 날아가기 마련이니까.

하지만.

‘이런 미친 짓을 하는 놈이, 시스템으로 근골을 뭐 빠지게 올린 사람이라면 얘기가 달라지지.’

내가 주어진 여러 능력치가 우량주라면, 근골은 레벨 업이나 수련을 할 때마다 꾸준하게 쌓여 온 적금이다.

그렇다면 시스템을 얻은 지 일 년이 훌쩍 넘은 지금은?

‘내 레벨이 몇이더라.’

나는 웃었다.

손바닥이 걸레짝이 되어 가는 끔찍한 고통을 참아내며, 터질 것처럼 부릅떠진 마삼보의 눈을 들여다보며.

조금 전 놈이 건넸던 한 마디를 그대로 돌려주었다.

토씨 몇 글자만 바꿔서.

“걱정하지 마. 딱 죽을 정도로만 쑤셔 줄 테니까.”

“……!”

마삼보는 뭐라 외치려 했지만, 그 목소리는 새어 나오지 못했다.

콰드득!

마삼보의 입술이 열리려던 그 순간, 내 손에 들려 있던 단창이 놈의 목줄기를 관통했으니까.

크륵. 컥.

피가래 끓는 소리와 함께, 나를 바라보던 두 눈동자에서 빛이 사그라졌다.
```

## Final English reading copy

```markdown
# Chapter 906

I didn’t know what to call this situation.

A melee?

A bloodbath?

Maybe both. Everywhere I stepped, I was trampling the corpse of someone I didn’t know, while enemy spears, swords, and arrowheads came hurtling in without pause, from the ground and the sky alike.

Even now.

“Look out!”

One of the Embroidered Uniform Guards heard my shout and jolted, twisting at the waist.

*Fffft!*

With a sharp whistle, his armor split open.

The traitor who’d tried to ambush him amid the chaos of battle missed by a hair. Without hesitation, I kicked a crescent blade lying on the ground.

*Whoooosh! Thud!*

There wasn’t even the usual dying cry.

The blade shot out like a flash of light, piercing its target and then skewering a couple of nearby enemies like meat on a spit. The Embroidered Uniform Guard, who’d barely escaped with his life, gave me a slight nod.

“Thank y—”

Then he never raised his head again.

*Thwack!*

An arrow pierced his throat, right through the windpipe.

Enemies rushed in, trampling the fallen guard’s body as he gurgled his last, and swung their weapons at anyone in reach.

All accompanied by a calm voice that had no place in a situation like this—which made it all the more chilling.

“Heaven above, earth below.”

“All demons bow in reverence.”

Why did it bring to mind the deranged fanatics I’d fought right before coming to Murim?

“Fucking lunatics…”

Short cries of dismay rang out here and there. The Embroidered Uniform Guards had continued fighting calmly despite the sudden betrayal of their allies, as if to prove the weight of the golden armor they wore. But even they looked afraid as they watched the traitors, who had become entirely different people.

Or maybe it was because of the martial prowess of someone who seemed impossible to defeat.

*Splash.*

A step forward, and his leather shoe sank into a pool of blood.

One of the Embroidered Uniform Guards had backed away without realizing it. A groan slipped through his lips.

“Ma Sanbao…”

That’s right. It was him.

Ma Sanbao, the East Depot’s Brush-Holding Eunuch.

Its second-in-command and de facto leader.

Or, to be precise, that was the identity he’d used to deceive the world. Now he was walking toward me.

So fast that “approaching” hardly did it justice—he moved like a flash of light.

*Whoosh! BOOM!*

His blows rained down like lightning from above. Every time I blocked one, my hands went numb.

My breathing had grown rougher than before, disrupting movements that should have flowed like water.

*Huff. Huff.*

I panted, wondering whether I was struggling this badly because I was in poor condition—or because I’d run into an opponent that formidable.

But even that thought didn’t last long.

*Shhk!*

The flexible sword curved like a living snake and grazed the bridge of my nose.

Hot blood welled through the split skin. I retreated, feeling a burning pain, as a low laugh crept into my ear.

“What happened to all that momentum you had at the start, hmm?”

Instead of answering, I turned my head. A dagger sprang from Ma Sanbao’s voluminous sleeve and pierced the empty space beside me like a streak of light.

*Thwack!*

Another life vanished with a sickening sound.

And then Ma Sanbao’s voice continued as if nothing had happened.

“That’s a shame. If you hadn’t dodged, that young Embroidered Uniform Guard would still be breathing.”

I looked at Ma Sanbao, who was taunting me, and wondered:

If I hadn’t dodged, would he have survived?

Could he have made it through this battle and returned to his family someday?

I didn’t know. I knew nothing.

The pointless guilt made me feel like shit. Even though the only person who should feel sorry for that guard, whose life had just ended, was someone else.

*Why…?*

I wanted to turn and look. I wanted to stare straight into the eyes of the Emperor and So Gyo, who had thrown me, Jeok Cheongang, and even their own subordinates into this battlefield, only to stand by and watch. I wanted to ask them:

Why had they held this damn banquet?

Why weren’t they acting, even though they had the power to turn the tide?

“Why the hell?!”

The one who answered my shout, which I could no longer hold back, was neither the Emperor nor So Gyo. It was Ma Sanbao.

“Do you still not understand why they’re standing by and doing nothing?”

He let out a derisive laugh and continued.

“Blazing Flame Divine Dragon Jin Taekyung. You were used by the Emperor in the end, too. Just like we tried to use you and the Fire King to get rid of So Gyo.”

“……!”

“Borrowing another’s blade to kill. There’s no better weapon than someone else’s when you don’t want to get blood on your own hands. Especially a fine sword like the Fire King and the Blazing Flame Divine Dragon.”

I wanted to tell him to shut his damn mouth.

But despite how badly I wanted to deny it, I couldn’t bring myself to speak.

Because it was plausible enough.

If the Emperor was anything like the man I’d experienced firsthand…

And if that woman, So Gyo, whose identity I couldn’t make head or tail of…

“The only role left for you and your Master is to fight desperately until you die. And then, in the end, to die.”

*Whoosh-whoosh-whoosh!*

With a sharp whistle, the flexible sword multiplied into dozens of blades, coming at me from every direction.

A sword technique at the limit of speed—so fast it seemed to have reached the very edge of what was possible.

But no matter how many afterimages crowded around me, there was only one real blade.

*Clang!*

A tremendous clash—too loud to believe it came from nothing more than two weapons meeting—sent me sliding back.

As the flexible sword kept swinging without pause, pressing its advantage, Ma Sanbao’s voice continued from beyond the blade.

“The Great Nation, the Emperor—it’s always been like this. To the rulers who hold this vast land, people like you and me, people of Murim, aren’t subjects to govern.”

*Whoosh-whoosh! Slice!*

The pressure of the sword split my skin. Thin streams of blood slipped through the cuts and scattered into the air.

“That’s why I followed my Master and pledged my loyalty to that person. And it’s why you’ll die here today. The Emperor wants to protect Prince Shangshan, nothing more. He won’t bring out even the hidden cards he’s kept in reserve just to save a pack of Murim ruffians.”

“What?”

At a realization that flashed through my mind, my eyes widened.

Even though there was considerable distance between us, I suddenly thought of someone fighting a thunderous battle alongside Jeok Cheongang far away.

*Could it be?*

No, not “could it be.”

Ma Sanbao had said it himself. This wasn’t a guess. It was a certainty.

*Krrrrang!*

Different kinds of Force struck each other and spat sparks.

Originally, it had been one weapon. But under Ma Sanbao’s fierce assault, it had split into two short spears. I crossed them to block the flexible sword, and felt the chill flowing from the blade, which stopped right in front of my face.

“Cang Gong. Were you his disciple?”

“Cang Gong? How dare you call him a servant of that sinister, weak Emperor?”

Ma Sanbao twisted his lips and continued.

“Eastern Heaven Demon Lord. That is the new name the great and all-powerful Lord of Heaven bestowed upon his loyal servant.”

“……!”

“And it’s the disciple of that very Eastern Heaven Demon Lord who will make you kneel.”

At that moment—

*Whirr.*

The blade of the flexible sword bent, its length coiled with the weapon’s natural spring.

Like a living snake, it slid over the spear shaft blocking its way and darted in as a flash of light. I saw it coming and swung my crossed short spears upward with all my strength.

*Clang!*

The flexible sword, which had been rushing toward my chest, veered off course.

But I’d only survived a dangerous moment. The attack wasn’t over.

*Wham!*

*Hk!*

My breath caught, and my vision flashed.

A fist struck my exposed chest. I staggered back more than ten steps in a row, and Ma Sanbao saw his chance. It was one he couldn’t afford to miss.

*Tap.*

Just one step.

At the same time, Ma Sanbao’s figure vanished like an illusion.

Yet even with my dulled senses and battered body, I reacted quickly.

*Left!*

The instant I was sure, I flung one hand out.

Even though splitting it in two had cost it its original advantage of long reach, it had gained a length and speed perfectly suited for throwing. I hurled it with tremendous force.

*Whoooosh!*

A single fierce whistle ripped through the air.

And at its end, a massive impact rang out.

*BOOM!*

Dust that had settled on the ground billowed up with the explosive sound.

Then—

*Shhhhk!*

Space split open.

The flexible sword that had knocked my short spear aside released a brilliant Force. It sliced through the cloud of dust and came at me.

Along with a taunting Sound Transmission that could only have been Ma Sanbao’s.

—Don’t worry. I’ll only cut you enough to leave you barely alive.

And that was his mistake.

In a slowed-down world, I was clearly watching the dozens of sword-images raining down to cover the air once more.

*Cut me? And only enough to leave me alive?*

That was ridiculous.

He was running his mouth like that while his opponent was still standing on two perfectly good legs.

The victor of a life-and-death duel had the right to spit on his opponent. He could boast about his strength and laugh in their face.

But…

*That’s what you do after everything’s over.*

My body was heavy as waterlogged cotton. The internal energy that usually surged in like a wave was faltering, strand by strand.

But it didn’t matter.

My eyes—and the hand gripping the one short spear I still had—hadn’t wavered.

*I see it.*

*Shwoosh!*

The spear tip pierced one precise point, wiping away dozens of sword-images as it met the real blade.

*BOOM!*

The impact sent the figure flying, unable to withstand the force of the collision.

Not me.

Ma Sanbao.

*Crunch.*

The tip of his foot dug into the ground as he planted it with all his strength. He barely steadied his swaying body and stared at me, eyes wide.

*Tap.*

By then, I was right in front of him.

“You bastard!”

Ma Sanbao’s flexible sword cut through the air with a scream of its own.

Its speed was more than worthy of being called extreme.

He scattered Force like a glacier—colder and more merciless than even that.

*Shwoooosh!*

Before that force, which seemed capable of freezing everything solid, I drew on every last bit of internal energy in my body.

*Fwoosh.*

A flame caught in wet firewood.

I poured the Scorching Yang Qi that surged like fire through my acupoints, as unstable as twisted railway tracks, into my hand and grabbed the blade just as it began to pierce my side.

*Krrk, KRAAAASH!*

Power collided with power.

At the same time, horrible pain shot through both hands.

It wasn’t Empty-Hand Seizes the Blade, catching a weapon between bare fingers with the precise timing and speed required.

This was just a brute-force grab.

“You crazy—”

No martial artist could blame Ma Sanbao for saying that.

This really was crazy.

Unless your opponent was at least a level below you, trying something like this against a master of similar skill—

And especially one with greater internal energy—

Would get both your arms cut off in an instant.

But…

*Things are different if the lunatic doing this has been busting his ass to raise his Muscles and Bones through the System.*

If my other stats were blue-chip stocks, then Muscles and Bones were a savings account that had steadily built up every time I leveled up or trained.

So what about now, more than a year after I’d gotten the System?

*What level am I again?*

I smiled.

I endured the horrible pain as my palm turned into a shredded mess, and looked into Ma Sanbao’s eyes, bulging as if they were about to burst.

Then I returned his earlier words with only a couple of words changed.

“Don’t worry. I’ll only stab you enough to kill you.”

“……!”

Ma Sanbao tried to shout something, but no sound came out.

*Krrk!*

Just as his lips began to part, the short spear in my hand pierced his throat.

“Ghk. Kgh.”

His eyes dimmed as he stared at me, while blood bubbled in his throat.
```

<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0901.txt",
      "sha256": "e6a173081051422950680f1d7804d654fbffe35c1fece2ec74995fc4f3a115c1",
      "bytes": 14481
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "4d753ef722f0afb9975d7f8d1a87a7afaaba23f7ba91fe5d7c691b0bcd5d4d51",
      "bytes": 718
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "15b7559bed5551ab89a765328d3f0a3fb2d8b907d46fb1c26625499fb4cab311",
      "bytes": 230936
    },
    {
      "path": "characters/Baek Yeon.md",
      "sha256": "44b1b01352c9ea6efd45841b2033db26149b505cc52e4efbdc17310c3a307c94",
      "bytes": 983
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "fb40d738ffc71c97265ee3bd2e404583d6f554e8285f51b735cd24746ae58286",
      "bytes": 759
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "26801fb6e833bb94002fbabd4fc8bc82cdee458d770437159064e921a5615237",
      "bytes": 1499
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "2f1d2e4b90674a8f50e05906a240194e5c1c7573f7431387c32acf95f8fe23d9",
      "bytes": 1369
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "c7d4d65495f603074ef9539ba01f614c5a8b3455c20b3c92492a2884c00c38b7",
      "bytes": 622
    },
    {
      "path": "characters/Ma Sanbao.md",
      "sha256": "1c9965d7d84f940f5f2b300ad2fbb73cf3d7416ad4e06fafe5cb32430d3ed949",
      "bytes": 970
    },
    {
      "path": "characters/Prince Shangshan.md",
      "sha256": "8f1c12fdb3e8d23187e2693a7a8b4c75605084d4170c3d9652138d7de5ccba47",
      "bytes": 952
    },
    {
      "path": "characters/So Gyo.md",
      "sha256": "d23c6394023b0cba33d042deea436f7af670f8d2a653a0b6026bc8fceb048196",
      "bytes": 900
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "7f21c98206ee120c9ee456402f779538d683726aa1dfdce5ac5ba6ff81eea142",
      "bytes": 261626
    }
  ],
  "estimated_tokens": 12245
}
-->

# Durable State Update — Chapter 901

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
1 and safe_through 901. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 901. Profile updates may replace only one
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
  "chapter": 901,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 901,
    "continuity_sources": [901],
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
    "The imperial birthday banquet is underway; the Emperor has arrived after years of seclusion and taken his place on the throne.",
    "The Emperor appears markedly aged, though his gaze remains sharp.",
    "The Emperor approached Jin Taekyung and asked what should be done with two officials; Taekyung told him to decide whether to kill or spare them.",
    "Ma Sanbao is present at the banquet and is the Emperor’s political adversary."
  ],
  "continuity_sources": [
    900
  ],
  "open_questions": [
    "How will the Emperor respond to Taekyung’s answer?",
    "Why might the Emperor be smoking opium?"
  ],
  "safe_through": 900,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 태원진가   | **Jin Family of Taiyuan**        |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 마법사     | **mage**              |
| 태원     | **Taiyuan**            |
| 형장      | **Brother** / **Brother [Name]**                                |
| 백연 | **Baek Yeon** | Commander of the Embroidered Uniform Guard. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 마삼보 | **Ma Sanbao** | The East Depot’s Brush-Holding Eunuch and second-in-command. |
| 상산왕 | **Prince Shangshan** | The City Lord and a member of the imperial family who orders the luncheon. |
| 소교 | **So Gyo** | The palace attendant leading the group assigned to serve Prince Shangshan. |
| 도발 | **Taunt** | System effect that the Matador’s Shield can activate against bovine-type monsters. |
| 천자 | **Son of Heaven** | Honorific title for the Emperor. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 선황 | **the late Emperor** | The former Emperor whom Hong Jin served. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 성군 | **sage king** | Desired form of rulership proclaimed for Prince Shangshan. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 마왕 | **Demon King** | The being Cheon Taemin killed. |
| 일원 | **One Origin** | Named Tang Clan organizational unit in Tang Sadok's mobilization order. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 초인 | **superhuman** | A being who has surpassed ordinary human limits. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 가기 | **singing courtesan** | The favored entertainer identity Honglan used in Hubei. |
| 금의위 | **Embroidered Uniform Guard** | Imperial guard force mentioned by Hong Jin. |
| 태조 | **Taizu** | The Great Nation’s founding emperor. |
| 동창 | **East Depot** | Imperial agency named by Hong Jin. |
| 창공 | **Cang Gong** | The bedridden East Depot leader for whom Ma Sanbao acts. |
| 위충 | **Wei Zhong** | The pledge’s first signer and the personal name of Lord Cang Gong. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 관리 | 진태경 | official_to_young_martial_artist | Young Master | formal-polite | The official addresses Taekyung as 공자 while explaining the consequences of Prince Shangshan's displeasure. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 관리 | 적천강 | government official to legendary martial master | you | formal, then alarmed and deferential | The official questions Jeok Cheongang, insults him as an old man, and later learns that he is the Fire King. |
| 적천강 | 관리 | legendary martial master to government official | you | blunt and mocking | Jeok Cheongang repeatedly echoes the official's formal phrasing while challenging his authority. |
| 진태경 | 마법사 | rescuer assisting the operation | mage; otherwise you | polite emergency imperative | Taekyung orders the exhausted mage to request rescue under his name. |
| 진태경 | 백연 | young martial artist confronting an imperial military commander | you | casual and insulting | Refers to Baek as 이 양반 while challenging his conduct. |
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
| 마삼보 | 진태경 | political ally recruiting a young martial artist | you; my friend | courteous and familiar | Ma uses 자네 and 이보게 while explaining his choice of Jin and inviting him to join the restoration army. |
| 진태경 | 마삼보 | young martial artist addressing the East Depot’s Brush-Holding Eunuch and prospective ally | you; Brush-Holding Eunuch | polite and direct | Jin asks Ma why he withheld information and presses him for a clear answer; he refers to him as 태감. |
| 황제 | 진태경 | Emperor addressing a subject and Prince Shangshan’s guest | Jin Taekyung | formal and authoritative | The Emperor addresses Taekyung by his family and personal name before asking what to do with the two officials. |

## Listed compact profiles

### Baek Yeon.md

# Baek Yeon (백연)

- **Safe through:** Chapter 900
- **Aliases:** Blood Envoy
- **Role:** Baek Yeon is the Commander of the Embroidered Uniform Guard, a former martial arts instructor to the Crown Prince, and the Blood Envoy who helped the fourth prince seize the throne and led the purge.
- **Personality:** Politically assured and controlled, he enforces authority with ruthless decisiveness but speaks with striking defiance to the Emperor in private when their shared undertaking is at stake.
- **Voice:** Not established
- **Relationships:** He commands the Embroidered Uniform Guard and serves the Emperor; they share an old promise tied to a great undertaking, and Baek urges the Emperor to restore matters before their adversaries' moves unravel it. He orders Jeong Hogun to surveil Prince Shangshan’s party while leaving openings for an approach, and treats Taekyung as a dangerous potential obstacle.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 899
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 895
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm, the occupant of the chief seat of the Murim Alliance's Five Kings Hall, and a trusted confidant who accepts Jin as himself despite knowing that he travels between Murim and another world resembling the realm of immortals.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; believes there is no absolute justice and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He deeply trusts Jin Taekyung, his publicly acknowledged Disciple and intended heir, regards him as the light of his later years, and will stand by him whatever path he chooses; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and remains Peng Cheolhu's rival.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 900
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader.
- **Personality:** Hungry, self-aware, dryly observant, and pragmatic under pressure; accepts extreme personal risk when duty and the lives of others demand it.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; Ma Sanbao recruited Jin and Jeok for the restoration effort supporting Prince Shangshan, and Jin has signed its pledge and arranged for Ma to summon Murim Alliance reinforcements.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 900
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Ma Sanbao.md

# Ma Sanbao (마삼보)

- **Safe through:** Chapter 900
- **Aliases:** None
- **Role:** Ma Sanbao is the East Depot’s Brush-Holding Eunuch and Supreme Peak martial artist, leading it in place of the bedridden Cang Gong and organizing a secret restoration effort for Prince Shangshan.
- **Personality:** He is vigilant and patient, concealing his loyalties while awaiting the moment to act for the late Emperor.
- **Voice:** He speaks in measured, courteous language and uses calm repetition, feigned agreement, and procedural reminders to steer conversations while keeping sensitive details guarded.
- **Relationships:** Ma Sanbao is a longtime friend and former East Depot cohort of Hong Jin, leads the restoration effort for Prince Shangshan, and recruited Jin Taekyung and Jeok Cheongang as discreet allies; Jin has signed the pledge and entrusted Ma with summoning Murim Alliance reinforcements.

### Prince Shangshan.md

# Prince Shangshan (상산왕)

- **Safe through:** Chapter 900
- **Aliases:** None
- **Role:** Prince Shangshan, whose personal name is Zhu Bao, is the Emperor’s twelve-year-old youngest younger brother and an exceptionally skilled young swordsman.
- **Personality:** Earnest and compassionate, he takes responsibility for his loyal subjects’ hardship, admires Jin Taekyung, seeks candid counsel, and shows composure beyond his years in the face of death and political danger.
- **Voice:** Archaic and formal in the manner of a historical drama, with openly eager and childlike reactions beneath his royal diction.
- **Relationships:** Prince Shangshan Zhu Bao is the Emperor’s youngest younger brother; the late Emperor entrusted Hong Jin with his care. Zhu Bao admires Jin Taekyung, seeks to emulate him, and calls him a friend; the Emperor says he will take care of Zhu Bao.

### So Gyo.md

# So Gyo (소교)

- **Safe through:** Chapter 899
- **Aliases:** None
- **Role:** A palace attendant assigned to Prince Shangshan who is a Supreme Peak master and has a mission to keep Jin Taekyung alive; her identity and allegiance remain unconfirmed.
- **Personality:** Calm, calculating, and self-possessed; she conceals her strength and identity and can be openly taunting.
- **Voice:** Measured and composed, shifting from deferential formality to casual, pointed taunts and threats.
- **Relationships:** She poses as the leader of the palace attendants assigned to Prince Shangshan and is Jin Taekyung’s opponent, yet believes he may be the person she seeks and the person foretold by “that person”; she says only she and the Emperor know a secret she withheld from Baek Yeon, while her true allegiance remains unknown.

## Korean source

```text
＃901화



정적.

작은 숨소리조차 들리지 않는, 그야말로 완벽한 정적이 대연회장에 내려앉았다.

오직 한 사람을 향해 부릅떠진 수많은 눈동자와 함께.

‘지금…… 뭐라고?’

‘도대체 무슨 소리를 들은 거지?’

사람들은 동시에 같은 의문을 품었고, 자신들의 시선 끝에 있는 한 청년의 모습을 통해 조금 전 들었던 ‘그 발언’을 떠올릴 수 있었다.



‘죽일 거면 죽이고, 살릴 거면 살리십시오. 그게 폐하 주특기 아닙니까.’



이 자리의 모두가 들을 수 있을 만큼 또렷하게 울려 퍼진 그 한마디.

한 번, 두 번, 열 번을 의심하며 기억을 되짚어도 변함없는 현실에 사람들은 체통도 잊은 채 멍하니 입을 벌렸다. 혀끝에 감도는 욕설을 간신히 삼켜 내며.

‘이런…… 미친놈.’

사실 미친놈이라는 표현조차도 저 청년, 진태경이 벌인 짓거리에 비하면 한참이나 부족한 것이었다.

면전에 대고 도발했다.

비아냥거렸다.

다른 누구도 아닌 황제에게.

물경 수만에 이르는 정적들을 추수하듯 베어 버리고, 대국을 설립한 태조(太祖) 이후 가장 강력한 중앙집권체제를 구축한 저 찬탈자에게.

‘미쳤군. 정말이지 제대로 미쳤어.’

품계가 낮아 말석에 앉아 있던 관리들은 물론이요, 정계의 핵심이라 할 수 있는 고관대작들마저 새하얗게 질린 얼굴로 입을 굳게 다물었다.

있을 수도 없고, 있어서도 안 되는 일이 벌어진 상황.

반역(反易)이라 불러도 이상하지 않은 만행이니 머지않아 벌어질 일은 불 보듯 뻔했다.

죽고, 죽고, 또 죽을 것이다.

진태경과 그 일가(一家)는 물론, 연관이 있는 모든 이가 형장의 이슬로 사라질 것이다.

그리고 금의위가 주도하여 작성할 그 살생부(殺生簿)에는 전혀 상관없는 몇몇 사람의 이름도 포함될 가능성이 농후했다.

이제는 죽고 없는 선황의 충신들.

상산왕을 진정한 후계자로 생각하는 일부 세력이 표적이 될 거란 사실은 그리 어렵지 않게 예상할 수 있었다.

증거? 명분?

그런 것은 중요하지 않았다.

증거도, 명분도 어차피 만들어 내면 그만이다.

고문 기구에 살과 근육이 찢겨 나가는 고통에 몸부림치다 보면 그 어떤 충의지사(忠毅志士)라 해도 죽음을 애걸하게 되니까.

황실 휘하의 고문 기술자들에게는 거짓을 진실로, 진실도 거짓으로 바꿀 수 있는 기술이 있었고, 과거 동창에게 주어졌던 그 역할은 금의위로 넘어온 지 오래였다.

즉, 칼자루는 오직 한 사람에게 달려 있었다.

황제.

이제 그의 명령 한 마디면 모든 것이 끝난다.

이미 진태경이 벌을 내릴 명분을 쥐여 준 이상, 곧 황제가 휘두를 칼날이 무엇을 베어 내도 이상하지 않았다.

설령, 그 마지막 목표가 상산왕이라 해도.

‘이런 말도 안 되는 짓을 벌이다니. 도대체 무슨 생각으로……!’

으득.

이 믿을 수 없는 상황을 모두 지켜보고 있던 대소신료 중 일부는 터져 나오려는 신음을 삼키기 위해 이를 악물어야 했다.

그들 한 사람, 한 사람이 내심 상산왕을 지지하거나, 혹은 연판장에 이름을 적어 반정을 꿈꾸는 이들.

그런 이들에게는 이 모든 상황이 끔찍한 재앙처럼 느껴졌다.

진태경이 상산왕의 빈객 자격으로 황실에 발을 들인 이상, 상산왕 역시 책임을 피할 수 없을 테니까.

‘허, 허허. 이렇게 천명(天命)이 대국을 떠나는구나.’

반정에 관련된 계획을 모르는 이들은 원망스러운 하늘을 개탄했고.

‘원래의 계획에 어긋났지만 어쩔 수 없다. 이렇게 된 이상 지금 당장이라도 나서야…….’

연판장에 서명한 이들은 각오를 다지며, 딱딱하게 굳은 얼굴로 상황을 지켜보는 마삼보를 주시했다.

그의 지시가 떨어지는 즉시 행동을 개시하기 위해서.

하지만 다음 순간.

“그래, 그대의 말이 옳다.”

긴 침묵을 깨트리며 울려 퍼진 황제의 한마디는, 다시 한번 모두를 충격의 구렁텅이로 밀어 넣기에 충분했다.

“그리고 성군(聖君)이 되고자 하는 자는 바른말을 하는 이를 벌하지 않는 법이지.”

“……!”

“……!”

“태원진가의 진태경.”

고요한 적막의 중심에 선 황제는 담담하게 말을 이었다.

“천자의 이름으로, 네가 짐에게 저지른 무례를 용서하마.”

용서.

분명 용서라고 했다.

다른 누구도 아닌 수만 명을 무참히 도륙했던 그가.

역모와 대숙청을 일으켰던 그 잔혹한 황제가.

다시 한번 할 말을 잃어버린 사람들은 절대자의 뒷모습을 멍하니 바라보았다.

단 한 사람을 제외하고서는.

정면으로 마주한 황제의 얼굴에서, 미처 숨기지 못한 감정의 편린을 읽어 낸 진태경은 마음속으로 뇌까렸다.

‘그래, 이렇게 나온단 말이지.’

앞서 황제를 도발했던 것은 목숨을 건 도박이었다.

만약 실패한다면 반정군이 사전에 계획한 모든 것이 뒤틀려 버릴지도 모를 만큼.

‘그렇기에, 바로 지금이어야 했다.’

그리고 그 위험천만한 도박의 결과는 성공이었다.

위험했던 만큼 중요한 열쇠를 얻었고, 황제의 대답은 설마 했던 마음속 의문을 해소해 주기에 충분했다.

‘지금 같은 상황에서 용서라…… 말도 안 되지.’

단 하나의 경우를 제외한다면.

진태경은 조용히 뒷말을 삼켰다.

사방에 흩어져 있던 퍼즐들이 하나씩 맞춰진다.

조금 전까지만 하더라도 터질 것 같던 머릿속이 서서히 맑아지고, 차분하게 가라앉은 마음은 새로운 길을 비추고 있었다.

물론 그럼에도 불구하고, 아직 모든 의문점이 정리된 것은 아니었다.

‘하지만, 도대체 어째서?’

진태경은 황제를 향해 전음을 흘려보냈다.

아니, 정확히는 흘려보내려고 했다.

때마침 이 자리에 도착한 누군가가 아니었다면.

“그토록 자비로운 성군이 되고자 하신다니, 듣던 중 반가운 이야기로군요.”

“……!”

황제보다 진태경이, 그리고 진태경보다 백연의 반응이 조금 더 빨랐다.

불과 다섯 장밖에 떨어지지 않은 어딘가.

늙수그레한 목소리와 함께 아무런 인기척도 없이 나타난 창백한 피부의 노인은, 황제를 향해 읍하며 말을 이었다.

“승하하신 선황 폐하께서도 기뻐하실 겁니다. 그렇지 않습니까?”

스륵.

천천히 들리는 고개와 함께 길게 자라난 백발이 흔들린다.

오랜 세월을 간직한 회색빛 눈동자에 황제의 굳은 얼굴이 담기고, 군데군데 갈라진 입술 사이로 건조한 목소리가 흘러나왔다.

“신, 동창장인태감(東廠掌印太監) 위충(魏忠)이 황제 폐하를 뵙나이다.”



* * *



위충을 본 순간, 나는 반사적으로 어릴 때 봤던 어느 고전 영화를 떠올리고 있었다.

방대한 판타지 세계관에, 마왕이 지닌 힘의 원천인 어떤 목걸이를 부수기 위해 여행을 떠나는 다종족 용사 파티.

그리고 그 중심인물 중 하나인 늙은 마법사.

“……간달프?”

무릎까지 닿을 것 같은 백발에 회색빛 눈동자까지.

사실 굳이 따지자면 ‘매우 아픈 간달프’에 가깝긴 하지만, 어쨌든 닮았다는 건 부정할 수 없는 사실이다.

이로 인한 약간의 애로사항이 있다면, 저 생각이 나도 모르게 육성으로 튀어나왔다는 거다.

‘아.’

상황을 인지하고 입을 다물었지만 이미 늦었다.

황제는 물론이고, 잠시 다른 곳을 향했던 모두의 시선이 내게 꽂혀 있었으니까.

그리고 그중에는 매우 아픈 간달프, 아니 위충 역시 포함되어 있었다.

“자네가 말로만 듣던 바로 그자로군.”

뭐라 대답해야 할까.

잠시 고민하던 내가 대답 대신 작게 고개를 끄덕이자, 실소를 흘린 위충이 다시 황제를 향해 고개를 돌렸다.

“참으로 무례한 자입니다. 그렇지 않습니까? 폐하.”

하지만 황제는 대답하지 않았다.

깊게 가라앉은 눈빛으로 위충을 응시하던 그가 입을 연 것은, 주위의 공기가 차갑다 못해 얼어붙을 무렵이었다.

“그렇지 않아도 그대의 모습이 보이지 않아 슬슬 사람을 보낼까 했는데…… 오랜만이군, 창공(廠公). 그간 무탈했나?”

“제법 긴 시간 동안 요양한 끝에 이렇게나마 거동할 수 있게 되었습니다. 이 모든 것이 황제 폐하의 은덕이 있었기에 가능했던 일이지요.”

“짐의 은덕이라. 확실한가?”

“내로라하는 명의들도 소신의 목숨을 장담하지 못했는데, 이리 나아진 것을 보면 하늘의 뜻이 있어서가 아니겠습니까. 그러니 전부 하늘의 자손이신 폐하의 은덕이라 생각합니다.”

“안타깝군. 짐이 보낸 어의(御醫)의 조언을 따라 탕약을 제조했다면 더 빨리 병마를 이겨 낼 수 있었을 터인데.”

“송구합니다. 하오나 황실 어의가 지어 온 탕약은 소신의 늙은 몸뚱어리가 감당할 수 없을 것 같아 어쩔 수 없이 요양을 택했나이다. 하온데…….”

위충이 문득 수심이 드리워진 얼굴로 황제를 살폈다.

“소신이 실로 오랜만에 뵈어서 그런 것인지, 폐하의 용안(龍顏)이 과히 좋지 않아 보입니다. 혹여 강건하셔야 할 옥체에 병마가 깃든 것은 아니신지요.”

“……!”

순간, 그렇지 않아도 굳어 있던 황제의 눈매에 서늘한 기운이 스쳤다.

“걱정할 필요 없다. 그대가 우려할 정도는 아니니.”

“그렇다면 참으로 다행입니다. 이렇듯 관용을 베푸시는 성군이 되셨으니 만세(萬世), 만만세(萬萬歲)까지 천하를 다스리셔야 하지 않겠습니까.”

느껴진다.

황제와 창공.

두 사람이 서로를 향해 쉼 없이 주고받는 보이지 않는 칼날이.

그리고 어느덧 황제에게서 흘러나오고 있는 거대한 기운이.

우우우웅.

주위의 대기가 요동친다. 비교적 가까이에 있던 몇몇 관리들은 오한을 느끼는 것처럼 새하얗게 질린 얼굴로 몸을 떨었다.

비록 황제라는 후광에 가려져 있으나, 그 역시 초인의 영역에 접어든 한 사람의 초절정 고수.

하지만…….

‘창공은, 저자는 달라.’

처음 그가 나타난 순간부터 깨달았다.

간달프를 닮은 저 창백한 피부의 노인이, 이 자리의 누구보다도 고수라는 사실을.

‘심지어는 백연조차도.’

초절정 고수 간의 전투란 그야말로 찰나지간에 생사가 갈리는 법.

불과 다섯 장 남짓한 거리까지 접근했었음에도 창공의 인기척을 느끼지 못했다는 사실은, 이미 선수(先手)를 빼앗겼다는 뜻이나 다름없었다.

‘이제야 알겠네. 마삼보가 그토록 자신하던 이유를.’

내가 느낀 바에 의하면 창공과 소교의 무위는 비등비등한 수준.

이러한 상황에서 아직 대연회장에 자리하지 못한 적천강과 그 외의 전력이 반정군에 합류한다면, 소교를 손쉽게 쓰러트릴 수 있을 것이다.

물론 그 소교조차 아직 모습을 드러내지 않았지만.

‘아마도 다른 곳에서 상산왕을 호위하고 있겠지.’

상산왕은 매우 중요한 열쇠다.

반정군과 황제, 그 어느 쪽이라 하더라도 결코 적에게 빼앗겨서는 안 되는 존재.

그리고 이와 비슷한 생각을 한 것은 나 혼자뿐만이 아닌 듯했다.

“폐하. 근래 들어 비바람이 기승을 부려서인지 오늘따라 유독 날씨가 서늘한 모양입니다. 저 가엾은 신하들을 위해서라도 관용을 베풀어 주심이 어떠하신지요.”

공손하면서도 여유롭게, 동시에 뼈 있는 말을 담아 부르르 떨고 있는 신하들을 가리킨 창공이 문득 생각났다는 듯이 입을 열었다.

“한데, 상산왕 전하와 회임하신 후궁 마마께서는 어찌하여 보이지 않으십니까? 명실상부한 황실의 일원이신 그 두 분이야말로 황제 폐하와 더불어 이 자리를 빛내 주셔야 할…….”

“그 입 다물어라, 위충.”

딱딱한 음성으로 창공의 말을 끊어 낸 백연이 앞으로 나서려던 그 순간.

“그만.”

손을 들어 그를 멈춰 세운 황제가 서늘한 눈빛으로 위충을 응시했다.

“창공은 신경 쓸 것 없다. 두 사람 또한 이미 이곳으로 오고 있으니.”

“성은이 망극하옵니다. 드디어 언젠가 이 광활한 대국을 통치하실 후계를 뵙게 되겠군요.”

“그래, 그렇게 될 것이다.”

둘 중 누구도 말하지 않았다.

또한 구태여 묻지도 않았다.

자신들이 마음에 담은 진정한 후계자가 누구인지. 상대가 생각하는 후계자는 누구인지.

다만 그들은 기다리고 있을 것이다.

이 연회가 무르익기를. 도화선의 불꽃이 끝까지 타들어 가기를.

그리고 나 역시 마찬가지였다.

“저기. 두 분 대화도 대충 끝나신 것 같은데. 조심스럽게 한 말씀만 드려도 됩니까?”

황제가 대답했다.

“무엇이냐.”

“별건 아닙니다. 이제 저기 저 상석 쪽으로 가실 것 같은데. 이참에 저도 자리 좀 옮겨 주십사 하고요. 웬만하면 창공 어른 옆자리가 좋겠네요.”

“……자리를 옮겨 달라고?”

얼어붙어 있던 대소신료가 한마음 한뜻으로 나에게 찢어 죽일 듯한 시선을 쏘아 보내는 동안, 잠시 할 말을 잃었던 황제를 대신해 창공이 입을 열었다.

“그, 무슨 특별한 이유라도 있나?”

나는 최대한 당당하고 멋있는 표정으로 대답했다.

“아무래도 위쪽 자리가 반찬 가짓수가 더 많아 보여서요.”

물론, 딱히 멋있어 보이지는 않았다.
```

## Final English reading copy

```markdown
# Chapter 901

Silence.

A perfect silence settled over the grand banquet hall—not even the smallest breath could be heard.

Along with it came countless eyes, wide with shock, all fixed on one person.

*What… did he just say?*

*What on earth did I just hear?*

Everyone wondered the same thing at once. Looking toward the young man at the end of their gazes, they recalled the remark they’d just heard.

> “Kill them if you want, or spare them if you want. Isn’t that what Your Majesty does best?”

The words had rung out clearly enough for everyone in the hall to hear.

They doubted their memories once, twice, ten times, but reality refused to change. Forgetting all about decorum, people gaped at him, barely managing to swallow the curses on the tips of their tongues.

*That crazy bastard.*

Even calling him crazy fell far short of describing what that young man, Jin Taekyung, had just done.

He’d provoked the Emperor to his face.

Mocked him.

The Emperor, of all people.

The usurper who had cut down tens of thousands of political enemies like a farmer harvesting crops, then built the strongest centralized regime since Taizu, founder of the Great Nation.

*He’s insane. Completely, utterly insane.*

The officials in the lowest seats, their ranks too low to sit anywhere else, and even the high-ranking ministers at the heart of the political world all turned deathly pale and pressed their lips together.

Something had happened that could never be allowed to happen.

It wouldn’t be strange to call this treason. What came next was as plain as day.

They would die. Die, and die again.

Jin Taekyung and his entire family, along with everyone connected to them, would vanish like dew on the execution ground.

And there was a very good chance the names of several people with no connection to any of it would end up on the Embroidered Uniform Guard’s death list, too.

The late Emperor’s loyal subjects.

It wasn’t hard to predict that some of those who considered Prince Shangshan the rightful heir would become targets.

Evidence? Justification?

None of that mattered.

Evidence and justification could always be manufactured.

Once the pain of flesh and muscle tearing against the instruments of torture had them writhing, even the most loyal subject would beg for death.

The imperial torturers had the skill to turn lies into truth and truth into lies. The East Depot had once been responsible for that work, but that duty had long since passed to the Embroidered Uniform Guard.

In other words, the sword was in one man’s hands alone.

The Emperor’s.

With a single order from him, it would all be over.

Now that Jin Taekyung had given the Emperor grounds to punish him, it wouldn’t be strange if the blade he swung cut down anyone at all.

Even if the final target were Prince Shangshan.

*How could he do something this absurd? What on earth is he thinking…?*

*Grit.*

Some of the assembled officials, who had watched the whole unbelievable scene unfold, clenched their teeth to hold back groans.

Each of them either supported Prince Shangshan in secret or had signed the pledge and dreamed of a restoration. To them, the whole situation felt like a terrible calamity.

Jin Taekyung had entered the imperial court as Prince Shangshan’s guest. The prince wouldn’t be able to escape responsibility, either.

*Heh… So Heaven’s Mandate is leaving the Great Nation.*

Those who knew nothing about the restoration lamented the heavens, bitter with resentment.

*The plan’s gone off course, but there’s no choice now. At this point, we may have to act this very moment…*

Those who had signed the pledge steeled themselves. Their faces rigid, they watched Ma Sanbao, ready to move the instant he gave the order.

But then—

“Indeed. You are right.”

The Emperor’s words broke the long silence, and were enough to plunge everyone into shock once more.

“And one who wishes to become a sage king does not punish those who speak the truth.”

“……!”

“……!”

“Jin Taekyung of the Jin Family of Taiyuan.”

At the center of the quiet, the Emperor continued in an even voice.

“In the name of the Son of Heaven, I forgive you for the disrespect you have shown me.”

Forgive.

He’d said he forgave him.

The very man who had ruthlessly slaughtered tens of thousands.

The cruel Emperor who had launched a rebellion and a great purge.

Everyone who had been at a loss for words stared blankly at the back of the absolute ruler—everyone except one person.

Reading the sliver of emotion the Emperor hadn’t quite managed to hide from his face, Jin Taekyung muttered to himself.

*So this is how he’s playing it.*

Taekyung’s earlier provocation had been a gamble with his life.

If it failed, it could throw the restoration army’s entire plan into disarray.

*That’s why it had to be now.*

And the result of that dangerous gamble was a success.

He’d gained a crucial key, as important as the risk had been. The Emperor’s response was enough to answer the question Taekyung had hardly dared to ask himself.

*Forgiveness in a situation like this… That makes no sense.*

Except in one case.

Jin Taekyung quietly swallowed the rest of his thought.

The scattered pieces of the puzzle were coming together, one by one.

His head, which had felt ready to burst moments ago, was gradually clearing. His mind settled, calm, and a new path came into view.

Even so, not every question had been answered.

*But why on earth…?*

Jin Taekyung sent Sound Transmission toward the Emperor.

Or, more precisely, he tried to.

If someone hadn’t arrived just then, he might have managed it.

“It’s heartening to hear Your Majesty wishes to become such a merciful sage king.”

“……!”

Jin Taekyung reacted a little faster than the Emperor, and Baek Yeon faster still.

Somewhere only five *jang* away, an old man with pale skin appeared without a sound. In a hoarse, aged voice, he continued, cupping his hands toward the Emperor.

“The late Emperor would be pleased as well. Would he not?”

*Rustle.*

The old man slowly lifted his head, his long white hair swaying.

The Emperor’s stiff expression was reflected in eyes the color of ash, bearing the marks of many years. A dry voice slipped between cracked lips.

“Your servant, Wei Zhong, Seal-Holding Eunuch of the East Depot, pays his respects to Your Majesty.”

* * *

The moment I saw Wei Zhong, I reflexively thought of an old fantasy movie I’d watched as a kid.

A motley party of heroes from different races setting off on a journey to destroy a certain necklace, the source of the Demon King’s power, in a vast fantasy world.

And one of the central characters: an old mage.

“…Gandalf?”

The white hair that looked like it reached his knees, those gray eyes…

Strictly speaking, he was closer to “Gandalf who’s very sick,” but there was no denying the resemblance.

The slight problem was that the thought slipped out of my mouth before I could stop it.

*Ah.*

I realized what I’d done and shut my mouth, but it was too late.

Everyone’s eyes had shifted back to me—including the Emperor’s, and Wei Zhong’s, too.

“You must be the very man I’ve heard so much about.”

What was I supposed to say?

I thought it over for a moment, then gave a small nod instead. Wei Zhong let out a snort and turned back toward the Emperor.

“He truly is a rude man. Is he not, Your Majesty?”

But the Emperor didn’t answer.

He gazed at Wei Zhong with eyes sunk deep in thought, and only spoke once the air around them had grown so cold it seemed frozen.

“I was about to send someone to find you, since you were nowhere to be seen… It’s been a long time, Cang Gong. Have you been well?”

“After a rather long period of recuperation, I’ve finally recovered enough to move about. I owe it all to Your Majesty’s grace.”

“My grace, is it? Are you sure?”

“Even the finest physicians couldn’t guarantee your servant’s life. Seeing how much I’ve recovered, surely Heaven must have willed it. So I believe it is all thanks to Your Majesty, the Son of Heaven.”

“That’s unfortunate. If you’d had the decoction made as the imperial physician I sent advised, you might have overcome your illness sooner.”

“I beg your forgiveness. However, I feared my old body couldn’t withstand the medicine prepared by the imperial physicians, so I had no choice but to recuperate instead. But…”

Wei Zhong looked the Emperor over, his face suddenly clouded with concern.

“Perhaps it is only because it has been so long since I last saw you, but Your Majesty’s countenance seems rather poor. Has illness taken hold of your precious body, which ought to be so strong?”

“……!”

A chill passed through the Emperor’s eyes, already hard with displeasure.

“There’s no need to worry. It isn’t as bad as you fear.”

“Then I’m greatly relieved. Now that you’ve become a sage king who shows such mercy, you must rule over the land for ten thousand years—ten thousand times ten thousand years.”

I could feel it.

The invisible blades the Emperor and Cang Gong were endlessly exchanging.

And the immense energy now emanating from the Emperor.

*Rrrrmmm.*

The air around us began to churn. A few officials nearby went pale and trembled as if struck by a chill.

His status as Emperor overshadowed it, but he too had entered the realm of the superhuman. He was a Supreme Peak master.

But…

*Cang Gong is different. That man is something else.*

I’d realized it the moment he appeared.

That pale old man who looked like Gandalf was a greater master than anyone else here.

*Even Baek Yeon.*

A battle between Supreme Peak masters could decide life and death in the blink of an eye.

The fact that Cang Gong had come within five *jang* of us without me sensing him meant he’d all but seized the initiative.

*Now I see why Ma Sanbao was so confident.*

From what I could sense, Cang Gong and So Gyo were evenly matched.

If Jeok Cheongang and the other fighters who hadn’t yet arrived at the Grand Banquet Hall joined the restoration army, they could take down So Gyo with ease.

Of course, So Gyo hadn’t shown herself yet.

*She’s probably somewhere else, guarding Prince Shangshan.*

The prince was a crucial key.

Neither the restoration army nor the Emperor could let him fall into the enemy’s hands.

It seemed I wasn’t the only one thinking along those lines.

“Your Majesty. Perhaps the recent storms have made the weather unusually chilly today. Might Your Majesty show some mercy for the sake of those poor officials, who are trembling over there?”

Cang Gong indicated the shivering officials, his words respectful and relaxed, but carrying a barb. Then, as if a thought had just occurred to him, he spoke again.

“By the way, why are Prince Shangshan and the pregnant Consort not here? The two of them are indisputably members of the imperial family, and ought to be here to lend their presence to this occasion alongside Your Majesty—”

“Silence, Wei Zhong.”

Baek Yeon cut Cang Gong off in a hard voice and was about to step forward when—

“That’s enough.”

The Emperor raised a hand to stop him and stared at Wei Zhong with cold eyes.

“Cang Gong, you needn’t concern yourself. The two of them are already on their way here.”

“I’m deeply grateful for Your Majesty’s grace. At last, I’ll get to meet the heir who will one day rule this vast Great Nation.”

“Yes. You will.”

Neither of them said anything more.

Nor did either bother to ask the other which heir he truly had in mind, or whom the other considered the heir.

They would simply wait.

For the banquet to reach its height. For the fuse to burn all the way down.

And so would I.

“Excuse me. It looks like you two are about done talking. Could I say something, if you don’t mind?”

The Emperor answered.

“What is it?”

“It’s nothing special. You’re probably going to move over to that raised seat over there now. I was wondering if I could move, too. Preferably to the seat next to Cang Gong.”

“…You want to change seats?”

While the officials who’d been frozen in place all glared at me as if they wanted to tear me apart, Cang Gong spoke in the Emperor’s stead, who’d been momentarily lost for words.

“Is, um… there a particular reason?”

I gave him my most confident, dashing look.

“The seats up there seem to come with more side dishes.”

Of course, it didn’t look particularly dashing.
```

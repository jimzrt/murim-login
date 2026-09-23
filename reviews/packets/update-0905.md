<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0905.txt",
      "sha256": "40c7c69be9e47d8ae5b307f4b3a032cb058232e6799c939169ed21ec64aa3f86",
      "bytes": 13012
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "ec305f978b9799721b5d1320772cf0ca11fe851827aafc7fb5af3a6e32a38331",
      "bytes": 1317
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "15b7559bed5551ab89a765328d3f0a3fb2d8b907d46fb1c26625499fb4cab311",
      "bytes": 230936
    },
    {
      "path": "characters/Baek Yeon.md",
      "sha256": "783efc81d77690d12281243258e6465bfde94ba1672c76ec100491868bf75b1a",
      "bytes": 983
    },
    {
      "path": "characters/Cang Gong.md",
      "sha256": "7792fa38ec8457b54241df6360fb75d991699b3032eea30ef80fe89485c4a404",
      "bytes": 687
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "117060e51e79ad06ee9eae731a35636364aeb3041f557828b15f14c9d7057969",
      "bytes": 759
    },
    {
      "path": "characters/Human Butcher.md",
      "sha256": "d00a5dce9f1aee8fba30575b29c0907658f68dc3221b00d699b53feeb4c5d7cc",
      "bytes": 667
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "86cd1ff84f667e1fb556c06cff744987bdae06cc9362a56d8cde9c8e8f3ae2ea",
      "bytes": 1499
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "cfa0a7d86e8769631ced82015d1bc497f94b159406589d27b8db4715fd9e39b2",
      "bytes": 1372
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "93eb0eea39ae7a1cde0b98eadea8f319d62a42e0055632dddf7762d33986d58a",
      "bytes": 622
    },
    {
      "path": "characters/Prince Shangshan.md",
      "sha256": "a4e82af7689387c4c62bd6d82cf89c223cfefb580409f7dc893887738271d48e",
      "bytes": 998
    },
    {
      "path": "characters/So Gyo.md",
      "sha256": "0b7fd22a8f5bd8372905ed049f802a58751fcc488223395b4e2761aa9adb53dc",
      "bytes": 900
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "54846be42db32b693819d1273169fa35c847b5fe45982ce0d273e90e25478c51",
      "bytes": 262602
    }
  ],
  "estimated_tokens": 11979
}
-->

# Durable State Update — Chapter 905

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
1 and safe_through 905. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 905. Profile updates may replace only one
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
  "chapter": 905,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 905,
    "continuity_sources": [905],
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
    "Jeok Cheongang has joined Taekyung in the battle.",
    "Ma Sanbao killed several Embroidered Uniform Guards and confronted Taekyung, who attacked him; Ma's allegiance and motives are unclear.",
    "So Gyo's identity and allegiance remain unknown; she is beside the Emperor with Baek Yeon.",
    "The Emperor does not want Prince Shangshan endangered.",
    "Hyuk Mujin and the Fire Dragon Pavilion party are traveling to the Jiangsu–Zhejiang border on Taekyung's mission; silent figures have appeared in the nearby forest."
  ],
  "continuity_sources": [
    904
  ],
  "open_questions": [
    "Who is So Gyo, and is she an ally or enemy?",
    "What is the nature of Cang Gong's unfamiliar power, and what is his relationship to the Lord of Heaven?",
    "Why did Ma Sanbao kill the guards and confront Taekyung, and where does his allegiance lie?",
    "Who are the silent figures surrounding Mujin's group?"
  ],
  "safe_through": 904,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무인     | **martial artist**                               | Default term                                          |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 마교     | **Demonic Cult**                                 |                                                       |
| 화산     | **Huashan**            |
| 노부      | **this old man / I**                                            |
| 백연 | **Baek Yeon** | Commander of the Embroidered Uniform Guard. |
| 창공 | **Cang Gong** | The bedridden East Depot leader for whom Ma Sanbao acts. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 상산왕 | **Prince Shangshan** | The City Lord and a member of the imperial family who orders the luncheon. |
| 소교 | **So Gyo** | The palace attendant leading the group assigned to serve Prince Shangshan. |
| 전세 | **jeonse lease** | Korean lump-sum deposit lease used in the family's redevelopment-era housing history. |
| 천자 | **Son of Heaven** | Honorific title for the Emperor. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 주표 | **Zhu Bao** | Personal name of Prince Shangshan. |
| 선황 | **the late Emperor** | The former Emperor whom Hong Jin served. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 성도 | **Chengdu** | Sichuan destination of Taekyung's party. |
| 시리 | **City** | Second word in one of the necromantic chants. |
| 초인 | **superhuman** | A being who has surpassed ordinary human limits. |
| 사냥개 | **hunting dog** | Jin's demeaning metaphor for Ares personnel who obey Go Jun. |
| 서리 | **seori** | Colloquial term for stealing crops or produce from a field. |
| 황족 | **Huang tribe** | Nanman tribe involved in a recently settled dispute. |
| 외궁 | **Outer Palace** | The outer compound of the Nanman Beast Palace. |
| 궁인 | **palace attendant** | Former Inner Palace attendant expelled by Baeksang. |
| 금의위 | **Embroidered Uniform Guard** | Imperial guard force mentioned by Hong Jin. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 진태경 | 주표 | visitor to prince | His Highness, Prince Shangshan | formal-deferential | Addresses Zhu Bao as 상산왕 전하 after kneeling to meet his gaze. |
| 주표 | 진태경 | prince to visiting young hero | Jin Taekyung | formal and inquisitive | Uses the formal second-person address before asking Taekyung's name and requesting an autograph. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 주표 | 백연 | prince addressing an imperial military officer | Commander Baek Yeon | formal and authoritative | Addresses Baek Yeon by name and office while insisting that he answer. |
| 백연 | 주표 | imperial officer addressing a prince | Your Highness | formal and deferential | Uses 전하 when apologizing to and answering Prince Shangshan. |
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
| 황제 | 진태경 | Emperor addressing a subject and Prince Shangshan’s guest | Jin Taekyung | formal and authoritative | The Emperor addresses Taekyung by his family and personal name before asking what to do with the two officials. |
| 적천강 | 창공 | hostile opponents | you; you bastard | blunt and threatening | Jeok Cheongang uses 네놈, 이 불알 없는 놈, and 호로새끼 while taunting Cang Gong. |
| 창공 | 적천강 | hostile opponents | Fire King Jeok Cheongang | taunting and sardonic | Cang Gong names Jeok by his title, then comments on how alike master and disciple are. |

## Listed compact profiles

### Baek Yeon.md

# Baek Yeon (백연)

- **Safe through:** Chapter 904
- **Aliases:** Blood Envoy
- **Role:** Baek Yeon is the Commander of the Embroidered Uniform Guard, a former martial arts instructor to the Crown Prince, and the Blood Envoy who helped the fourth prince seize the throne and led the purge.
- **Personality:** Politically assured and controlled, he enforces authority with ruthless decisiveness but speaks with striking defiance to the Emperor in private when their shared undertaking is at stake.
- **Voice:** Not established
- **Relationships:** He commands the Embroidered Uniform Guard and serves the Emperor; they share an old promise tied to a great undertaking, and Baek urges the Emperor to restore matters before their adversaries' moves unravel it. He orders Jeong Hogun to surveil Prince Shangshan’s party while leaving openings for an approach, and treats Taekyung as a dangerous potential obstacle.

### Cang Gong.md

# Cang Gong (창공)

- **Safe through:** Chapter 904
- **Aliases:** None
- **Role:** Cang Gong is the East Depot leader and a formidable martial artist who intends to take Jin Taekyung to the Lord of Heaven for recruitment.
- **Personality:** Calculating and self-assured, he admires Taekyung's ability while believing the Lord of Heaven's power will make him submit.
- **Voice:** Dry and sardonic, he delivers taunts and judgments in measured statements.
- **Relationships:** He follows the Lord of Heaven and recalls a former master and fellow disciples as family; he now regards Jin Taekyung as a potential recruit.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 903
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Human Butcher.md

# Human Butcher (인도)

- **Safe through:** Chapter 893
- **Aliases:** None
- **Role:** Former mysterious Han Chinese mounted-bandit power in Northern Gaoyuan commanding fifty subordinates; a Peak master killed by an unnamed old man in a single move
- **Personality:** Cold, intimidating, and murderous; he kills people as though slaughtering livestock
- **Voice:** Cold, curt, and quietly threatening
- **Relationships:** He is one of four powerful participants at the Northern Gaoyuan gathering, intimidates Temur, and has claimed Ghost Sword Wipeng as his personal target in the proposed attack

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 904
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm, the occupant of the chief seat of the Murim Alliance's Five Kings Hall, and a trusted confidant who accepts Jin as himself despite knowing that he travels between Murim and another world resembling the realm of immortals.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; believes there is no absolute justice and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He deeply trusts Jin Taekyung, his publicly acknowledged Disciple and intended heir, regards him as the light of his later years, and will stand by him whatever path he chooses; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and remains Peng Cheolhu's rival.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 904
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader.
- **Personality:** Hungry, self-aware, dryly observant, and pragmatic under pressure; accepts extreme personal risk when duty and the lives of others demand it.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; Ma Sanbao recruited Jin and Jeok for the restoration effort supporting Prince Shangshan, but their alliance is now in question after Ma confronted Jin during the banquet-hall battle.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 904
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Prince Shangshan.md

# Prince Shangshan (상산왕)

- **Safe through:** Chapter 903
- **Aliases:** None
- **Role:** Prince Shangshan, whose personal name is Zhu Bao, is the Emperor’s twelve-year-old youngest younger brother, an exceptionally skilled young swordsman, and the heir publicly designated by the Emperor.
- **Personality:** Earnest and compassionate, he takes responsibility for his loyal subjects’ hardship, admires Jin Taekyung, seeks candid counsel, and shows composure beyond his years in the face of death and political danger.
- **Voice:** Archaic and formal in the manner of a historical drama, with openly eager and childlike reactions beneath his royal diction.
- **Relationships:** Prince Shangshan Zhu Bao is the Emperor’s youngest younger brother; the late Emperor entrusted Hong Jin with his care. Zhu Bao admires Jin Taekyung, seeks to emulate him, and calls him a friend; the Emperor says he will take care of Zhu Bao.

### So Gyo.md

# So Gyo (소교)

- **Safe through:** Chapter 904
- **Aliases:** None
- **Role:** A palace attendant assigned to Prince Shangshan who is a Supreme Peak master and has a mission to keep Jin Taekyung alive; her identity and allegiance remain unconfirmed.
- **Personality:** Calm, calculating, and self-possessed; she conceals her strength and identity and can be openly taunting.
- **Voice:** Measured and composed, shifting from deferential formality to casual, pointed taunts and threats.
- **Relationships:** She poses as the leader of the palace attendants assigned to Prince Shangshan and is Jin Taekyung’s opponent, yet believes he may be the person she seeks and the person foretold by “that person”; she says only she and the Emperor know a secret she withheld from Baek Yeon, while her true allegiance remains unknown.

## Korean source

```text
＃905화



횃불이 휘청인다. 어둠 속에서도 식별할 수 있는 진한 핏물이 사방에서 터져 나온다.

카카카캉!

푸푹!

잘 벼려진 날붙이들이 맞물리며 번뜩이는 검광(劍光).

그리고 고통 어린 비명과 함께.

― 크아아악!

― 컥, 커헉!

최후를 알리는 단말마(斷末摩)와 함께 이름 모를 누군가가 죽음을 맞이하고, 또 다른 이가 빈자리를 채운다.

반복.

어느 한쪽이 전멸하지 않는 이상 끝나지 않을, 죽음의 반복.

천자라는 두 글자에 실린 무게를 증명이라도 하려는 듯, 한 치의 흔들림도 없이 옥좌에 앉아 있던 황제는 전장으로 돌변한 대연회장을 바라보며 생각했다.

‘오랜만이군. 이런 광경을 보는 것도.’

지금은 화려하게 수 놓인 곤룡포(袞龍袍)를 걸치고 있으나, 불과 십여 년 전의 황제는 갑주를 입고 전장을 누볐던 한 사람의 장군이었다.

황위를 물려받을 가능성도, 그럴 생각도 없었던 대국의 사황자(四皇子).

일군을 이끌고 변방의 군벌과 유목민들을 짓밟았던 그가 옥좌에 오르리라고는 그 누구도 예상치 못했다.

심지어 그 자신조차도.

“모를 일이군. 참으로 모를 일이야. 그렇지 않나?”

문득 흘러나온 황제의 뇌까림에, 철탑처럼 옥좌 옆을 지키고 있던 금의위 지휘사 백연이 무거운 목소리로 대답했다.

“소장의 불찰이오.”

황실을 수호해야 하는 금의위 중 무려 삼분지 일이 칼을 거꾸로 쥐었다.

거기에 더해 외궁 경비를 맡은 금위군까지 쉴 새 없이 화살 비를 쏟아붓는 상황.

배신자들의 존재를 전혀 예측하지 못했던 것은 아니지만, 창공의 그림자는 생각했던 것 이상으로 짙게 드리워져 있었다.

황실. 아니, 이 대국 전체에.

쉬쉬쉬쉭, 터텅!

정확히 황제를 겨냥하고 쏘아 올린 수백여 발의 화살들이 맥없이 튕겨 나간다.

커다란 철제 방패로 벽을 쌓아 공격을 막아 낸 금의위 위사들을 향해 황제가 입술을 달싹였다.

“출(出).”

짧은 명령이었으나, 그것으로 충분했다.

대국 제일의 정예인 금의위 안에서도 가리고 가려 뽑은 일백의 무인들은 망설임 없이 지면을 박차며 쇄도했다.

황제의 곁이 아닌, 죽음과 비명으로 물든 전장으로.

쐐애애애액!

수십여 장의 거리가 단숨에 좁혀진다.

동시에 휘둘려진 일백의 창칼이 휘황한 섬광을 뿜어 내며 배신자들을 향해 들이닥쳤다.

쉬이이잉!

서걱! 푸푸푹!

“크아아악!”

비명과 핏물이 쉴 새 없이 터져 나왔다.

절정의 끝자락에 도달한 무인들의 손끝에서 펼쳐지는, 실로 압도적이면서 끔찍하리만치 강한 무력.

그러나 그것만으로는 전세(戰勢)를 완전히 뒤집을 수 없었다.

이 전장의 중심에는, 그야말로 인간의 한계를 벗어난 진정한 괴물들이 날뛰고 있었으니까.

콰아아아앙!

드드드득!

거대한 굉음과 진동이 사방을 뒤흔들었다. 어둠을 뚫고 높게 솟구친 불꽃의 기둥 너머로 시리도록 새하얀 빛이 뿜어졌다.

슈확!

공간이 갈라진다.

마치 한겨울의 서리를 닮은 그 싸늘한 기운을 느낀 이들은 약속이라도 한 듯이 전신을 파르르 떨었다.

그리고 서서히 기울어지는 시야를 보며 깨달았다.

‘아.’

자신들이 마지막으로 느꼈던 저 냉기가, 바로 죽음이었다는 것을.

쿠쿠쿠쿵!

수십에 달하는 망자들의 육신이 썩은 고목 나무처럼 쓰러진다.

핏물에 흠뻑 젖은 그들의 갑옷은 더는 황금빛으로 빛나지 않았고, 그들을 바라보는 회색빛 눈동자는 서늘하게 가라앉아 있었다.

“고작 이 정도였더냐.”

퍼엉!

대수롭지 않게 내뻗은 일장(一掌)에 전신이 으스러지고.

“황제의 사냥개들이. 황실의 힘이.”

콰드득!

가볍게 구른 진각(震脚)에 반경 수십여 장의 지면이 파도처럼 출렁이며.

“고작 이 정도냐고 물었다!”

콰아아!

강대한 공력을 머금은 외침이 압축된 공기를 터트렸다.

고된 훈련으로 단련된 몸과 마음을 뒤흔들고 고막을 찢었다.

“커헉.”

곳곳에서 흘러나오는 신음.

그리고 피가 흐르는 귓가를 감싸며 비틀거리는 금의위들을 향해 다시 한번 새하얀 섬광이 들이닥쳤다.

아니, 들이닥치려던 그 순간이었다.

화륵.

어디선가 불꽃이 일렁인다.

얼음장처럼 차갑던 공기가 용암처럼 끓어오르기까지 걸린 시간은 찰나에 불과했고, 이내 어둠마저 집어삼켰다.

꽈앙!

만약 화산이 폭발한다면 이런 소리가 날까.

순간 모두의 뇌리를 스친 그 의문을 뒤로한 채 터져 나온 불꽃은, 오직 한 사람을 향해 쏟아지고 있었다.

창백한 피부를 한 노인.

창공의 회색빛 눈동자에 끔찍한 열기가 고스란히 담겼다.

콰아아앙!

격돌. 그리고 폭발.

곧이어 들이닥친 무시무시한 여파는 적아(敵我)를 가리지 않으며 튕겨 냈고, 창공 역시 예외일 수는 없었다.

스스스슥. 턱.

거대한 힘을 이기지 못하고 밀려 나가던 신형이 가까스로 멈춰 선다.

비스듬히 굽혀졌던 허리를 바로 세운 창공의 시선이 한 사람을 향해 틀어박혔다.

“온 힘을 다해 싸워도 모자랄 상황에 어린 것들을 상대로 힘자랑이나 하다니. 나이를 뒷구멍으로 처먹은 놈이로고.”

화왕 적천강.

사방에 피어오르는 아지랑이 속에서 다가오는 그의 모습에, 창공의 입매가 비틀렸다.

“그건 당신 역시 마찬가지지. 결국 화왕(火王)이라는 별호도 무수한 약자들을 죽여서 얻은 것이 아닌가?”

“불알이 없어도 말은 바로 해야 하는 법. 노부가 죽인 마교도들은 단순한 약자가 아니었다. 태워 죽여도 시원치 않을 방화범들이었지.”

“그렇다면 다른 마교도들은 왜 죽였소? 그들은 당신에게 아무런 잘못도 하지 않았을 텐데.”

“어느 날 잠에서 깨 보니 선조 대대로 물려받은 거처가 활활 불타고 있더군. 그럼 기분이 어떨 것 같으냐?”

적천강은 대답을 기다리지 않고 말을 이었다.

“더럽지. 아주 좆같아. 그래서 죄다 궁둥이를 걷어차 저승으로 쫓아 버렸다. 설령 다시 태어난다 해도 두 번 다시 남의 집에 불을 지르지 못하도록.”

“요컨대, 개인적인 복수였다는 뜻이구려.”

“맞다. 그렇지 않아도 그놈들 하는 짓이 썩 마음에 들진 않았거든.”

적천강은 화염이 넘실거리는 주먹을 들어 올리며 덧붙였다.

“바로 네놈처럼 말이다.”

쉬릭, 쾅!

물경 수천에 달하는 병력이 대연회장을 메우고 있었지만, 그중 누구도 보지 못했다.

적천강이 어떻게 움직였는지. 그리고 창공이 어떻게 저 무시무시한 공격을 피했는지.

그러나 능히 초인(超人)이라 불리기에 조금도 손색이 없는, 극소수의 인물들은 예외였다.

“만약 짐이 저 자리에 있었다면, 과연 얼마나 버틸 수 있을까.”

모든 광경을 빠짐없이 지켜보고 있던 황제의 물음에, 백연이 대답했다.

“백초지적.”

“야속할 만큼 망설임이 없군. 그래도 이 경지까지 오르기 위해 적지 않은 노력을 기울였는데.”

쓴웃음을 머금은 황제의 모습에 백연이 담담하게 대꾸했다.

“그 누구라 해도 마찬가지요. 얼마나 오래 버티느냐의 문제이지, 결과는 달라지지 않겠지.”

“백연, 그대가 나선다 하더라도?”

“금의위 지휘사로 임한다면 필승(必勝). 한 사람의 무인으로 싸운다면 석패(惜敗).”

“그렇다면 지금의 그대는 무인인가, 금의위 지휘사인가?”

“소장은 언제나 금의위 지휘사였소. 오직 황제 폐하의 명을 받드는. 그리고…….”

백연이 희미한 목소리로 뇌까렸다.

“선황(先皇)께서 내리신 마지막 명령은, 사 황자와 함께 훗날을 도모하라는 것이었지.”

“……!”

황제의 눈가가 파르르 떨렸다.

어찌 잊을 수 있을까.

그날의 기억을. 마지막으로 들었던 그 목소리를.

그렇게 어언 십여 년이 흘렀다.

감당할 수 없는 짐을 짊어진 청년의 머리에는 나이보다 일찍 찾아온 서리가 내려앉았고, 강보에 싸여 있던 갓난아이는 어엿한 소년이 되어 지금 이 순간을 함께 하고 있었다.

“도대체!”

당장이라도 자신을 붙잡은 궁인들의 손을 뿌리치고 전장으로 달려 나갈 듯이 몸부림치며.

“도대체 무슨 생각이신 겁니까!”

혼란과 분노를 머금은 눈동자로 황제를 노려보고 있었다.

“왜! 어찌하여 저들을 돕지 않으시는 겁니까! 폐하를 위해 목숨 걸고 싸우는 저들을……!”

콰아아앙!

이어지려던 뒷말이 화염과 함께 터져 나온 굉음에 파묻힌다.

다음 순간, 또 다른 전장의 격전지에서 반으로 부러진 창 자루를 지팡이 삼아 일어나는 익숙한 얼굴을 본 상산왕이 작게 신음했다.

“진태경.”

멀리서도 한눈에 알아볼 수 있었다.

아니, 못 알아볼 리가 없었다.

그는 진태경이었으니까.

늘 똑같고 무기력하던 어린 왕의 일상에 처음으로 활기를 불어넣어 준 사람이었고, 그를 왕이 아닌 또 다른 누군가로 대해 준 유일한 인물이었으니까.

상산왕 주표는 똑똑히 기억하고 있었다.

처음으로 진태경을 만났던 그 날을.



‘과인도 그대처럼 될 수 있을까?’



그리고 고심 끝에 건넨 그 물음에, 진태경은 망설임 없이 대답했다.



‘그럼요. 할 수 있습니다.’



상산왕은 진심으로 진태경을 닮고 싶었다.

단지 진태경의 무위가 빼어나서가 아니다.

가문의 천덕꾸러기에 불과했던 그가, 여러 강적을 꺾고 모두의 사랑을 받게 된 것이 놀랍고 부러웠다.

세상 누구보다 존귀한 황족이었음에도 언제나 외로워야 했던 어린 왕은, 어느 젊은 무림인에게서 자신의 모습을 보았다.

며칠 전, 무엄하게도 머리를 쓰다듬던 그 손바닥에서 잊을 수 없는 온기를 느꼈다.



‘꼭 다시 만나길 바라네. 그래야만 과인이 그대에게 진 빚을 갚을 수 있을 테니까.’

‘전하.’

‘응?’

‘모르십니까? 친구 사이에는 빚 같은 거 없습니다.’



처음이었다.

누군가가 자신을 벗이라고 부른 것도.

평범한 어린아이를 대하듯이 머리를 쓰다듬어 준 것도.

그래서 더욱더 약속을 지키고 싶었다. 진태경에게 진 빚을, 호의를 되돌려 주어야 했다.

그는 자신의 하나뿐인 친구였으니까.

“부디, 부디 저자를 살려 주십시오.”

도대체 지금 무슨 일이 벌어지고 있는지, 이 상황에 어떤 내막이 있는지는 모른다.

그러나 상산왕은 망설임 없이 고개를 숙이고 무릎을 꿇었다.

자신의 하나뿐인 친혈육에게.

짧은 명령 한 마디로 여러 초절정 고수들을 움직일 수 있는 대륙의 주인에게 간청했다.

“원하시는 바가 있다면 무엇이든 하겠습니다. 소제(小弟)더러 대국을 떠나라 하시면, 그 역시 명을 따르겠습니다. 다만 이 아우가 처음이자 마지막으로 드리는 부탁만큼은 거절하지 마시옵소서.”

“……!”

“저자를, 진태경을 살려 주십시오. 폐하!”

엎드려 부르짖는 상산왕의 모습을 바라보는 황제의 얼굴 위로 형용할 수 없는 감정이 스쳤다.

안도와 대견함. 혹은 슬픔이라고도 부를 수 있는 그 감정의 소용돌이 끝에, 끝끝내 입 밖으로 뱉지 못한 한 마디가 있었다.

‘폐하가 아니라…… 형님이라고 불러 주지 않겠느냐.’

하지만 달싹이는 입술 사이로는 그 어떤 목소리도 흘러나오지 못했고, 황제는 상산왕의 간청에도 고개를 끄덕이지 않았다.

아니, 그럴 수 없었다.

적어도 오늘 이 전장에 관한 모든 것은, 이미 십여 년 전부터 한 사람에게 맡겨 놓은 후였으니.

― 아무리 생각해도 모르겠군. 이러한 상황에서도 왜 그대가 방관만 하고 있는지.

나직이 귓가를 파고드는 황제의 전음에 소교가 답했다.

― 방관이 아니라, 지켜보는 것입니다.

처음부터 그러했듯 조금의 흔들림도 없이, 진태경을 응시하며.

― 그가 진면목을 드러낼 때까지.
```

## Final English reading copy

```markdown
# Chapter 905

The torches wavered. Dark blood, visible even in the darkness, burst out in every direction.

*Clang-clang-clang!*

*Thrust!*

Well-honed blades met, flashing with swordlight.

And with them came cries of pain.

“Gyaaaagh!”

“Ghk, gah!”

With a dying cry that announced the end, someone nameless met their death, and someone else stepped into the empty space they left behind.

Again and again.

A cycle of death that would not end until one side was wiped out.

As if to prove the weight carried by those two words—Son of Heaven—the Emperor sat on his throne without so much as a tremor, watching the Grand Banquet Hall turn into a battlefield.

*It’s been a long time since I’ve seen a sight like this.*

He wore a dragon robe embroidered in brilliant colors now, but a little over a decade ago, the Emperor had been a general who strode across battlefields in armor.

The fourth prince of the Great Nation, with neither the prospect nor the desire to inherit the throne.

No one could have imagined that the man who led an army to crush border warlords and nomads would one day ascend the throne.

Not even he himself.

“Strange how things turn out. Truly strange. Wouldn’t you agree?”

At the Emperor’s sudden murmur, Commander Baek Yeon of the Embroidered Uniform Guard, who stood beside the throne like an iron tower, replied in a heavy voice.

“This subordinate failed in his duty.”

A full third of the Embroidered Uniform Guard, whose duty was to protect the imperial family, had turned their blades against their own side.

On top of that, the Imperial Guards responsible for the Outer Palace kept raining arrows down without pause.

The Emperor had not been entirely unprepared for the existence of traitors, but Cang Gong’s shadow had fallen far darker than he’d expected.

Over the imperial family—or rather, over the entire Great Nation.

*Shhh-shhh-shh—clang!*

Hundreds of arrows fired straight at the Emperor bounced off harmlessly.

The Emperor moved his lips toward the Embroidered Uniform Guard who had blocked the attack by forming a wall with their massive iron shields.

“Advance.”

It was a short command, but enough.

A hundred martial artists, handpicked from among the finest elite of the Great Nation’s greatest force, launched themselves forward without hesitation.

Not to stay beside the Emperor, but to charge into the battlefield stained with death and screams.

*Whoooosh!*

Dozens of yards vanished in an instant.

At the same time, a hundred spears and swords swung forward, blazing with dazzling light as they bore down on the traitors.

*Whiiing!*

*Slice! Thrust!*

“Gyaaaagh!”

Screams and blood erupted without pause.

The martial prowess of warriors at the very brink of the Peak realm—overwhelming, and horribly powerful.

But that alone could not turn the tide of battle.

At the center of this battlefield, true monsters who had surpassed the limits of human ability were rampaging.

*BOOOOM!*

*Rrrumble!*

A tremendous roar and tremor shook the area. Beyond a pillar of fire that surged high into the air, piercing the darkness, a painfully white light blazed.

*Shhk!*

Space split open.

Those who felt that frigid energy, like frost in the depths of winter, shuddered from head to toe as if on cue.

Then, watching their vision slowly tilt, they understood.

*Ah.*

That cold they’d felt at the end was death.

*Rrrumble!*

Dozens of corpses fell like rotten old trees.

Their armor, drenched in blood, no longer shone gold. The gray eyes looking down at them had settled into a cold gaze.

“Is that all you have?”

*Whump!*

A casual palm strike crushed a man’s whole body.

“The Emperor’s hunting dogs. The might of the imperial family.”

*Craack!*

A light stomp made the ground within dozens of yards ripple like a wave.

“Is that all you have? That’s what I asked!”

“Gwaaaah!”

The shout, filled with immense internal energy, burst through the compressed air.

It shook the bodies and minds hardened by grueling training, and tore at their eardrums.

“Ghk.”

Groans rose from all around.

Then, toward the Embroidered Uniform Guards who staggered, hands pressed to their bleeding ears, another white flash came hurtling toward them.

No—it was just about to.

*Fwoosh.*

Somewhere, flames flickered.

In the blink of an eye, the air that had been cold as ice began to boil like lava, soon swallowing even the darkness.

*BOOM!*

Would it sound like this if a volcano erupted?

Leaving that question in everyone’s minds, the burst of flame came pouring down toward one person alone.

An old man with pale skin.

Cang Gong’s gray eyes held every bit of that terrible heat.

*BOOOOM!*

Impact—and explosion.

The dreadful shock wave that followed hurled friend and foe alike through the air. Cang Gong was no exception.

*Shhhhh. Thud.*

His body was forced back by the immense power, but he managed to stop himself.

Straightening his back, which had bent at an angle, Cang Gong fixed his gaze on one man.

“When the situation demands you fight with everything you have, you waste your strength showing off against children. You must’ve eaten your age through your ass.”

Fire King Jeok Cheongang.

As Jeok approached through the heat haze rising all around him, Cang Gong’s lips twisted.

“And you’re no different. In the end, didn’t you earn the title of Fire King by killing countless weaklings?”

“Even without balls, a man should speak straight. The Demonic Cultists I killed weren’t mere weaklings. They were arsonists I wouldn’t have been satisfied with even if I’d burned them alive.”

“Then why did you kill the other Demonic Cultists? They had done nothing to you.”

“One day, I woke up to find my ancestral home going up in flames. How do you think that felt?”

Without waiting for a reply, Jeok Cheongang continued.

“Filthy. It felt like shit. So I kicked every last one of them in the ass and sent them to the afterlife. That way, even if they were reborn, they’d never set fire to someone else’s home again.”

“In other words, it was personal revenge.”

“That’s right. I didn’t like what those bastards were doing anyway.”

Jeok Cheongang raised a fist wreathed in rolling flames and added,

“Just like you.”

*Swish—BOOM!*

Thousands of soldiers filled the Grand Banquet Hall, but not one of them saw what happened.

How Jeok Cheongang moved. Or how Cang Gong evaded that terrifying attack.

But a tiny handful of people were different. They were more than worthy of being called superhuman.

“If I were in his place, how long could I last?”

In response to the Emperor’s question, as he watched every detail of the battle, Baek Yeon answered,

“A hundred moves.”

“You don’t hesitate to be cruel. Still, I’ve put in no small amount of effort to reach this realm.”

The Emperor wore a bitter smile. Baek Yeon replied without a change in expression.

“It would be the same for anyone. The only question is how long they could last. The outcome would not change.”

“Even if you went out there, Baek Yeon?”

“If I went as Commander of the Embroidered Uniform Guard, victory would be certain. If I fought as a single martial artist, I would lose by a hair.”

“Then what are you now—a martial artist, or the Commander of the Embroidered Uniform Guard?”

“This subordinate has always been the Commander of the Embroidered Uniform Guard. One who obeys only Your Majesty’s commands. And…”

Baek Yeon murmured in a faint voice,

“The late Emperor’s final order was to make plans for the future alongside the fourth prince.”

“……!”

The Emperor’s eyes trembled.

How could he forget?

That day. The voice he heard for the last time.

More than a decade had passed since then.

Frost had settled early on the head of the young man burdened with more than he could bear. The infant who had once been swaddled in blankets had grown into a boy, now sharing this very moment with him.

“What on earth—”

He struggled as if he might shake off the palace attendants’ hands at any moment and rush onto the battlefield.

“What on earth are you thinking?”

His eyes, filled with anger and confusion, were fixed on the Emperor.

“Why? Why won’t you help them? The people risking their lives for Your Majesty…!”

*BOOOOM!*

The rest of his words were swallowed by the roar that burst out with the flames.

The next moment, Prince Shangshan spotted a familiar face in another fierce battle across the hall—a man rising to his feet with a broken spear shaft for a cane—and let out a quiet groan.

“Jin Taekyung.”

He could recognize him at a glance, even from far away.

No. How could he fail to recognize him?

He was Jin Taekyung.

The first person to bring life to the young prince’s dull, unchanging days, and the only one to treat him as someone other than a prince.

Prince Shangshan Zhu Bao remembered clearly the day he first met Jin Taekyung.

“Could I become like you?”

And to that question, asked after much thought, Jin Taekyung had answered without hesitation.

“Of course. You can.”

Prince Shangshan truly wanted to be like Jin Taekyung.

Not simply because Jin Taekyung was a formidable martial artist.

He was amazed and envious that someone who had been no more than the family’s unwanted child had defeated one powerful enemy after another and won everyone’s affection.

Though he was a royal more honored than anyone in the world, the young prince had always been lonely. In one young martial artist, he had seen someone like himself.

A few days ago, that palm had gently ruffled his hair without a trace of propriety. He had felt a warmth he could never forget.

“I hope we meet again. Then I can repay the debt I owe you.”

“Your Highness.”

“Yes?”

“Don’t you know? Friends don’t owe each other anything.”

It was the first time.

The first time someone had called him a friend.

The first time someone had ruffled his hair as if he were an ordinary child.

That was why he wanted all the more to keep his promise. He wanted to return Jin Taekyung’s kindness, to repay what he owed him.

He was his one and only friend.

“Please, please save him.”

Prince Shangshan had no idea what was happening, or what lay behind this situation.

Still, he bowed his head and fell to his knees without hesitation.

Before his only blood relative.

He pleaded with the ruler of the continent, who could move several Supreme Peak masters with a single word.

“If there is anything you wish of me, I will do it. If you order your younger brother to leave the Great Nation, I will obey. But please, do not refuse this request from your brother—the first and last I will ever make of you.”

“……!”

“Save him. Save Jin Taekyung, Your Majesty!”

As the Emperor watched Prince Shangshan prostrate himself and cry out, an indescribable emotion crossed his face.

Relief. Pride. Perhaps even sorrow. At the end of that tumult of feelings, there was something he could never quite bring himself to say.

*Not ‘Your Majesty’… Wouldn’t you call me ‘older brother’?*

But no voice came through his parted lips, and despite Prince Shangshan’s plea, the Emperor did not nod.

No—he could not.

At least as far as everything happening on this battlefield today was concerned, he had already entrusted it to one person, more than a decade ago.

*No matter how I think about it, I can’t understand why you’re doing nothing, even in a situation like this.*

So Gyo answered the Emperor’s quiet Sound Transmission as it slipped into her ear.

*I’m not doing nothing. I’m watching.*

As she had from the beginning, she kept her gaze fixed on Jin Taekyung without the slightest sign of wavering.

*Until he shows his true self.*
```

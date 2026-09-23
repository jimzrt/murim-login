<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0892.txt",
      "sha256": "ca4b5bfae4b3cb96def205ecd54dc7775b045432f100b099543e85ee5fccef5f",
      "bytes": 12753
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "c56791df7f8062a9265407e97eea93fd1325a1dd8a9de96322008a6737306d55",
      "bytes": 1254
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "42391788f53c6c5ac3e1dcd23d6389823b2c8658da1a82bb5b05e797a4f8f5b6",
      "bytes": 230370
    },
    {
      "path": "characters/Blood Lord.md",
      "sha256": "b4a785f664c176b696d5213aa7714291c30b9daaf647a15d4b4ff331c4609bd2",
      "bytes": 927
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "a191d8a13e22cf92daff21b425767ab4167d5d9ef614df863c87ba5724532303",
      "bytes": 759
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "877a3f4b81ef483b52059ebd6f08d5522192d46b470847054fb3b8472e866a81",
      "bytes": 1511
    },
    {
      "path": "characters/Ma Sanbao.md",
      "sha256": "d0bbfbc8f08059004697d534c9595c131ba296838cb8e10be9134fe11bd06354",
      "bytes": 815
    },
    {
      "path": "characters/Martial God.md",
      "sha256": "9f3801577a200834f86a8572af73815a33bb33b62e6596094ee4c8088f6c064e",
      "bytes": 752
    },
    {
      "path": "characters/Namho.md",
      "sha256": "2a48c332af83718d8b8c3b6a8f9927219fabc5d8078a0a91a613772d04076f61",
      "bytes": 973
    },
    {
      "path": "characters/Sama Pyo.md",
      "sha256": "3e14819ac2c32262a0cbf05237467002549a599bf7769c0ec05ebf680fc53608",
      "bytes": 936
    },
    {
      "path": "characters/So Gyo.md",
      "sha256": "82f9b5cde3b89906282a3ad4f8aa5e32e2de90f4353d608c4697d65f922d520f",
      "bytes": 900
    },
    {
      "path": "characters/Southern Heaven Demon Empress.md",
      "sha256": "eb1467a54cb6f8a797ad6464b1d393401d2bba5a543c1de8f70d4e5195660506",
      "bytes": 715
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "46eaeb0d0b4c1ab1ac82efae55a239405a4bdbf9c6f0f78eb8b6b3af6eb0a2e2",
      "bytes": 685
    },
    {
      "path": "characters/Western Heaven Demon Lord.md",
      "sha256": "cfe7e37de487fb6e697f5d7ca046d5deccdceffeebcf5eb22f7a8040b2b38d02",
      "bytes": 888
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "ef6d67de4e1b522d1eeb1f2d24f4e2680eb93774a88bfe09eef62256fc6d8301",
      "bytes": 260549
    }
  ],
  "estimated_tokens": 12402
}
-->

# Durable State Update — Chapter 892

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
1 and safe_through 892. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 892. Profile updates may replace only one
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
  "chapter": 892,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 892,
    "continuity_sources": [892],
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
    "Jin has reunited with the Fire Dragon Pavilion group in the imperial palace and briefed them on the crisis.",
    "Jin reports seeing at least six Supreme Peak masters and powerful Embroidered Uniform Guards; other hidden imperial masters may exist.",
    "So Gyo is a skilled flexible-sword user serving Dark Heaven, but her identity, age, and reason for releasing Jin are unknown.",
    "The grand banquet is approaching, and the group expects a decisive conflict may occur there.",
    "Ma Sanbao leads a restoration army that has spent more than a decade preparing for the coup.",
    "Jin suspects the Emperor believes the outcome will remain unchanged regardless of how fiercely the opposition fights."
  ],
  "continuity_sources": [
    891
  ],
  "open_questions": [
    "Who is So Gyo, and why did she release Jin when she could have subdued him?",
    "What will happen at the approaching grand banquet?",
    "Why does the Emperor appear confident that the outcome cannot be changed?",
    "How many powerful imperial masters remain concealed?",
    "Is So Gyo a once-in-a-millennium prodigy or an old master who has Returned to Youth?"
  ],
  "safe_through": 891,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 적천강    | **Jeok Cheongang** |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 무신     | **Martial God**               | —              |
| 삼성     | **Three Saints**    |
| 십왕     | **Ten Kings**       |
| 무림맹    | **Murim Alliance**               |
| 암천     | **Dark Heaven**                  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 생사결    | **life-and-death duel**                          | Explicitly lethal                                     |
| 정파     | **orthodox faction**                             |                                                       |
| 마교     | **Demonic Cult**                                 |                                                       |
| 중원     | **Central Plains**                               |                                                       |
| 강호     | **martial world**                                | Prefer “Murim” where the setting itself is meant      |
| 선배     | **Senior**                                   |
| 사천     | **Sichuan**            |
| 정마대전   | **Great Faction War**         |
| 노부      | **this old man / I**                                            |
| 도사      | **Daoist**                                                      |
| 혈주 | **Blood Lord** | Title of the unidentified young man encountered by Han Su. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 마삼보 | **Ma Sanbao** | The East Depot’s Brush-Holding Eunuch and second-in-command. |
| 남호 | **Namho** | Hidden Shadow Pavilion code name; literally associated with amber from the south. |
| 사마표 | **Sama Pyo** | Young Sect Leader of the Black Dragon Demon Gate. |
| 소교 | **So Gyo** | The palace attendant leading the group assigned to serve Prince Shangshan. |
| 남천마후 | **Southern Heaven Demon Empress** | Title Honglan uses when revealing her identity. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 서천마군 | **Western Heaven Demon Lord** | Title of the middle-aged antagonist who commands the summoned black-robed hunters. |
| 사마외도 | **demonic, heterodox arts** | Suspected martial-arts origin of Pung Yang's insidious forms. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 선천지기 | **innate qi** | Vital energy said to be damaged by the pill's aftereffects. |
| 천자 | **Son of Heaven** | Honorific title for the Emperor. |
| 선황 | **the late Emperor** | The former Emperor whom Hong Jin served. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 성군 | **sage king** | Desired form of rulership proclaimed for Prince Shangshan. |
| 기해 | **qi sea** | Name for the dantian, the place where internal energy begins and gathers. |
| 오향장육 | **five-spice pork** | Dish Cheongpung packed for the journey. |
| 장천 | **Jangcheon** | Name Jeok Cheongang gave to the orphan who later became Jopil; means “Vast Sky.” |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 중독 | **Poisoned** | System status abnormality caused by the poisons. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 은영각 | **Hidden Shadow Pavilion** | Former Murim Alliance intelligence organization. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 천주 | **Lord of Heaven** | Authority invoked by the masked attackers. |
| 살수 | **assassin** | Professional killer considered as a possible suspect. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 교주 | **Cult Leader** | Leader of the Divine Cult. |
| 사천혈사 | **Sichuan Blood Tragedy** | Earlier incident in which Taekyung witnessed the strange formation. |
| 화룡각 | **Fire Dragon Pavilion** | New name chosen for Taekyung's pavilion. |
| 서천 | **Western Heaven** | Short form used by the Lord of Heaven for the Western Heaven Demon Lord. |
| 남천 | **South Heaven** | Dark Heaven power that the Lord of Heaven orders the servants to contact. |
| 마후 | **Demon Empress** | Title used for the Southern Heaven Demon Empress. |
| 균열 | **rift** | The dark rift opening in the cliff behind the Inner Palace. |
| 마력 | **magical power** | Distinct from mana; the Skeleton King's area of expertise. |
| 금의위 | **Embroidered Uniform Guard** | Imperial guard force mentioned by Hong Jin. |
| 동창 | **East Depot** | Imperial agency named by Hong Jin. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 장천 | 적천강 | disciple_to_master | Master | deferential and pleading | Jangcheon repeatedly begs Jeok Cheongang to accept him as his Disciple. |
| 적천강 | 장천 | master_to_disciple | you / fool | blunt and gruff | Jeok rejects Jangcheon’s pleas, questions his choices, and threatens to send him down the mountain. |
| 혈주 | 적천강 | claimed enemy to enemy | your enemy | calm and threatening | The Blood Lord identifies himself as Jeok's enemy and claims to have killed Jeok's most precious friend. |
| 서천마군 | 신의 | hostile_invader_to_physician | Divine Physician | calm and mocking | Uses 신의 and 그대 while taunting the physician and dismissing his objections. |
| 신의 | 서천마군 | physician_to_invading_fiend | fiend | defiant and formal | Calls the Western Heaven Demon Lord an 악귀 and orders him to leave. |
| 서천마군 | 적천강 | hostile_invader_to_unconscious_patient | you | calm and predatory | Says someone wants to see Jeok Cheongang and attempts to move him with Seizing an Object Through Empty Space. |
| 적천강 | 서천마군 | hostile_opponents | you bastard | blunt and threatening | Jeok addresses the Western Heaven Demon Lord with 네놈 while defending Taekyung and ordering him not to touch his Disciple. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 적천강 | 남천마후 | legendary_martial_master_to_hostile_demon_empress | you bitch | blunt and threatening | Threatens to punish her and Lord of Heaven. |
| 남천마후 | 적천강 | hostile_demon_empress_to_legendary_martial_master | Fire King Jeok / you | flattering and mocking | Addresses Jeok Cheongang as the Fire King while praising Lord of Heaven. |
| 사마표 | 태산 | Young Sect Leader to subordinate | Taishan | informal and patronizing | Sama Pyo calls Taishan by name while ordering him to leave. |
| 태산 | 사마표 | subordinate to Young Sect Leader | Lord | crude and deferential | Taishan uses 주군 while obeying Sama Pyo. |
| 사마표 | 적천강 | Young Sect Leader to legendary elder | Great Hero Jeok | formal-deferential | Sama Pyo formally pays his respects to Jeok Cheongang as the Fire King. |
| 태산 | 적천강 | subordinate of a Young Sect Leader to legendary elder | Fire King | clipped, childlike, and deferential | Taishan gives his awkward greeting and expresses admiration for Jeok's strength. |
| 적천강 | 사마표 | legendary elder to unorthodox Young Sect Leader | you / young brat | blunt, suspicious, and contemptuous | Jeok addresses Sama Pyo with 네놈 and 어린놈 while probing his lineage and motives. |
| 적천강 | 태산 | legendary elder to giant subordinate | you / strange fellow | blunt, startled, and grudgingly tolerant | Jeok addresses Taishan as 네놈 while reacting to his greeting and appetite. |
| 혈주 | 천주 | servant_to_absolute_master | Lord of Heaven | worshipful and deferential | Blood Lord repeatedly addresses the Lord of Heaven while apologizing and receiving power. |
| 천주 | 혈주 | absolute_master_to_servant | Blood Lord | commanding and reproachful | The Lord of Heaven directly rebukes Blood Lord and then empowers him. |
| 남호 | 태산 | guide_to_pavilion_member | Taishan | blunt and exasperated | Namho directly rebukes Taishan for eating the poisonous blood-feeding fungus. |
| 남호 | 사마표 | guide_to_young_sect_leader | Young Sect Leader | blunt and admonishing | Namho warns Sama Pyo that all grass and animals in the territory belong to the Nanman Beast Palace. |
| 사마표 | 남호 | young_sect_leader_to_guide | Elder Namho | formal and apologetic | Sama Pyo apologizes after Taishan attempts to seize the calf. |
| 태산 | 남호 | Fire Dragon Pavilion member to guide | Namho | clipped, childlike, and informal | Taishan directly addresses Namho while asking what Dark Heaven is. |
| 남천마후 | 천주 | devoted_servant_to_revered_master | Lord of Heaven | reverent and prayerful | The Southern Heaven Demon Empress prays that the Lord of Heaven will remember her loyalty and love. |

## Listed compact profiles

### Blood Lord.md

# Blood Lord (혈주)

- **Safe through:** Chapter 891
- **Aliases:** None
- **Role:** Young-seeming high-ranking Dark Heaven figure who directs its sorcerers’ seed experiments and prepares their deployment for the Lord of Heaven’s great cause.
- **Personality:** Confident, cruel, and controlling; readily kills subordinates who disappoint him, but restrains his violence when preserving valuable sorcerers serves Dark Heaven’s goals.
- **Voice:** Light, cheerful, and joking even while threatening or killing; turns cold and contemptuous when challenged.
- **Relationships:** He serves the Lord of Heaven and seeks to advance the Lord’s great cause; he regards the deceased Western Heaven Demon Lord and Southern Heaven Demon Empress as powerful allies whose deaths cost Dark Heaven, and considers Jin Taekyung and Cheongpung formidable adversaries.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 891
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 891
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm, the occupant of the chief seat of the Murim Alliance's Five Kings Hall, and a trusted confidant who accepts Jin as himself despite knowing that he travels between Murim and another world resembling the realm of immortals.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He deeply trusts his publicly acknowledged Disciple and intended heir Jin Taekyung, warmly regards Ju Hwaran and hopes she and Jin grow closer, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and remains Peng Cheolhu's rival.

### Ma Sanbao.md

# Ma Sanbao (마삼보)

- **Safe through:** Chapter 891
- **Aliases:** None
- **Role:** Ma Sanbao is the East Depot’s Brush-Holding Eunuch and Supreme Peak martial artist, leading the Depot in place of its bedridden leader, Cang Gong.
- **Personality:** He is vigilant and patient, concealing his loyalties while awaiting the moment to act for the late Emperor.
- **Voice:** He speaks in measured, courteous language and uses calm repetition, feigned agreement, and procedural reminders to steer conversations while keeping sensitive details guarded.
- **Relationships:** Ma Sanbao is a longtime friend and former East Depot cohort of Hong Jin; he stayed behind to await Prince Shangshan's return and is leading a group seeking to enthrone him.

### Martial God.md

# Martial God (무신)

- **Safe through:** Chapter 888
- **Aliases:** None
- **Role:** An unidentified legendary martial artist regarded as a pinnacle above the Ten Kings; more than fifty years ago, he defeated five Supreme Peak fiends and five hundred Blood Ghost Squad members alone.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** He met the Beast Miao King twice more than fifty years ago, appearing first as a white-bearded elder and later as a young boy; Mae Jonghak received several teachings from him, while his identity, whereabouts, and possible connection to Cheon Taemin remain unknown.

### Namho.md

# Namho (남호)

- **Safe through:** Chapter 891
- **Aliases:** Elder Chao
- **Role:** Namho is an eighty-year-old non-Han Hidden Shadow Pavilion agent who spent more than fifty years undercover in Nanman and maintained contact with Central Plains intelligence through the Pavilion’s Hidden Thread; he now guides the Fire Dragon Pavilion.
- **Personality:** Duty-bound, pragmatic, and observant; uses theatrical violence to protect intelligence work and takes a veteran’s concern for the younger generation’s resolve.
- **Voice:** Measured and reflective when advising the younger generation, loudly abusive when maintaining his local cover, and capable of theatrical boasts and dry humor.
- **Relationships:** Namho is a Hidden Shadow Pavilion contact for Jin Taekyung and the Fire Dragon Pavilion, receives intelligence from the Pavilion Master, and knows the code used by the Thousand-Faced Fox.

### Sama Pyo.md

# Sama Pyo (사마표)

- **Safe through:** Chapter 891
- **Aliases:** Black Dragon Saber
- **Role:** Young Sect Leader of the Black Dragon Demon Gate, a Morning Star reputed to be no less than the Ten Dragons and Phoenixes, and a member of the Fire Dragon Pavilion.
- **Personality:** Outwardly courteous and smiling, inwardly calculating, but genuinely protective of Taishan; in combat he is ruthlessly pragmatic, survival-focused, and unafraid to stake his life.
- **Voice:** Polite and ingratiating in public, with sardonic humor and controlled evasiveness.
- **Relationships:** Sama Pyo commands the absolutely loyal Taishan, is Sima Gong's son, was Ju Hwaran's former fiancé in a political engagement, and has joined the Fire Dragon Pavilion while openly intending to use Jin Taekyung as a useful card; he is now openly hostile toward fellow member Song Ilseom.

### So Gyo.md

# So Gyo (소교)

- **Safe through:** Chapter 891
- **Aliases:** None
- **Role:** A palace attendant assigned to Prince Shangshan who is a Supreme Peak master and has a mission to keep Jin Taekyung alive; her identity and allegiance remain unconfirmed.
- **Personality:** Calm, calculating, and self-possessed; she conceals her strength and identity and can be openly taunting.
- **Voice:** Measured and composed, shifting from deferential formality to casual, pointed taunts and threats.
- **Relationships:** She poses as the leader of the palace attendants assigned to Prince Shangshan and is Jin Taekyung’s opponent, yet believes he may be the person she seeks and the person foretold by “that person”; she says only she and the Emperor know a secret she withheld from Baek Yeon, while her true allegiance remains unknown.

### Southern Heaven Demon Empress.md

# Southern Heaven Demon Empress (남천마후)

- **Safe through:** Chapter 891
- **Aliases:** None
- **Role:** The Southern Heaven Demon Empress was Honglan, the creator of the rift behind the Inner Palace, and was killed after the rift closed.
- **Personality:** Playful, cruel, confident, and casually dismissive of mass death and the suffering of others.
- **Voice:** Light, taunting, amused, and delighted even when discussing murder or imminent catastrophe.
- **Relationships:** She commands and advises Baeksang, treats Jin Taekyung and Yayul Cheok as expendable to the grand plan, and keeps a masked hunting dog whom she trained carefully.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 891
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo; becomes explosively violent when his meat is threatened.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord, trusts Jin Taekyung as Pavilion Master, and has grown attached to the Fire Dragon Pavilion members.

### Western Heaven Demon Lord.md

# Western Heaven Demon Lord (서천마군)

- **Safe through:** Chapter 891
- **Aliases:** None
- **Role:** Former Protector of the Divine Cult who commands Dark Heaven's assault on the Sichuan Tang Clan, lost the Myriad-Poison Ring to Jin Taekyung, suffered a crushed ankle and a torn wrist, and was temporarily possessed by the Lord of Heaven before the borrowed body was destroyed.
- **Personality:** Cold, detached, patient, and utterly ruthless toward those he interrogates or hunts.
- **Voice:** Controlled and dispassionate, with concise statements delivered in a quiet, threatening tone.
- **Relationships:** Tang Taesang and the Heaven-Shaking Venerable Nun were his latest victims, he lost one arm taking their lives, and the Qilian Three Fiends now submit to him alongside his hundreds of black-robed hunters.

## Korean source

```text
＃892화



지금껏 여러 강적을 만났고, 헤아릴 수 없을 정도로 무수한 전투를 치렀지만 이런 경우는 처음이었다.

내게도, 그리고 다른 이들 모두에게도.

“여기서 더욱 판을 키우겠다는 건데…… 이 짐작이 사실이라면 제대로 미친 게 틀림없군.”

적천강의 중얼거림에 남호가 고개를 끄덕였다.

“믿기 어렵지만, 적들에게는 그것이 대국(大國) 전체를 장악할 수 있는 가장 빠른 지름길이긴 합니다.”

맞는 말이다.

이 세상에 캐삭빵만큼 확실한 건 없다. 모든 것을 건 단판 승부가 끝나면 승자는 살아남고 패자는 사라질 것이다.

문제는 적들이 품고 있는 저 확신의 원천이 무엇인지 모르겠다는 거고.

‘도대체 무슨 자신감이지?’

말이 쉬워서 단판 승부지, 이건 단순히 무림인들 사이에서 숱하게 벌어지는 생사결이 아니다.

대국의 명운을 건 엄청난 대격전인 동시에, 황도를 피로 물들이는 혈전이 될 것이 틀림없었다.

‘만약 이 전투에서 우리가 패배한다면, 반정군은 단숨에 뿌리뽑히고 암천과 황제는 대국 전체를 온전히 손에 넣을 수 있다. 하지만 단지 그것뿐일까?’

앞서 남호는 말했다.

그것이 적들에게 있어 가장 빠른 지름길이라고.

하지만 지름길이 언제나 가장 좋은 선택지가 되는 것은 아니다. 사람들이 정해진 길로 이동하는 것은 그럴 만한 이유가 있기 때문이니까.

대로(大路)는 넓고 곧게 뻗어 있다. 조금 돌아갈지언정 편하고 쉽게 목적지로 향할 수 있다.

그러나 지름길은 좁고 복잡하다. 다져지지 않은 땅은 울퉁불퉁하고, 때로는 악취와 위험이 도사린 으슥한 골목을 지나쳐야 할 때도 있다.

‘그런데도 적들은 후자를 택했지. 심지어 나를 미끼로 써 가면서까지.’

큰 그림을 위해서라고는 해도 이러한 일련의 선택들은 무모하게까지 느껴질 정도다.

이미 번번이 암천의 앞길을 가로막은 나를 제지하지 않은 것도, 반드시 승리해야 할 전투의 난이도를 굳이 상향 조정 하는 것도.

그리고 이런 생각을 떠올린 것은 비단 나뿐만이 아니었다.

“어째서지?”

자리에서 일어난 적천강이 주위를 서성거리며 혼잣말처럼 중얼거렸다.

“노부가 황궁에 있다는 사실을 모른다 해도, 이미 남만에서의 일을 파악하고 있다면 충분히 염두에 둘 만한데.”

암천의 정보망은 광활하다. 마삼보도 알고 있는 사실을 소교나 황제가 전해 듣지 못했을 리 없다.

모르긴 몰라도 저들 역시 같은 정보를 입수했을 것이다.

남천마후를 쓰러트리는 과정에서 화왕 적천강이 개입했고, 나와 함께 남만을 떠났다는 것을.

그런데도 나를 놔줬다.

마치 화왕(火王)이라 불리는 포식자의 존재를 전혀 염두에 두지 않는 것처럼. 설령 그 포식자가 이번 전투에 난입한다 해도 승패에는 아무런 지장이 없는 것처럼.

‘이건…… 확실히 이상한데.’

아니, 이상한 것을 넘어 수상할 정도다.

나야 이미 성치 않은 몸인 데다, 천주(天主)에게서 모종의 지시를 받았다는 전제하에 납득할 수 있다.

하지만 적천강은?

이미 정마대전 당시에도 십왕(十王)의 정점이었으며, 조금 더 일찍 참전했다면 능히 삼성(三星)과도 어깨를 나란히 했을 거라는 평가를 받는 괴물 중의 괴물이다.

‘혈주는 그 불가사의한 회복력이 없었다면 몇 번이나 즉사했을 테고, 사천혈사 때는 이제 막 중독에서 벗어난 몸으로 서천마군을 상대했었지.’

물론 가장 최근에 상대했던 남천마후는 예외다.

[균열]에서 흘러나오는 마력으로 말미암아 반쯤은 마물(魔物)이 된 데다, 선천지기까지 불태운 탓에 인간을 벗어난 무위를 선보였으니까.

그런데 그런 적천강까지 염두에 두지 않는다고?

‘지랄.’

나는 가라앉은 눈빛으로 허공을 바라보며 생각했다.

깊이 생각해 보면 이상한 점이 한두 개가 아닌 상황.

확실히 뭔가 있다.

아직 내가 모르는 뭔가가. 알려지지 않은 비밀이.

그리고 이런 의문을 조금이나마 해결시켜 줄 사람을, 나는 한 명 알고 있었다.

“마삼보.”

문득 입술 사이를 비집고 흘러나온 그 이름에, 남호가 감 잡았다는 듯이 고개를 끄덕였다.

“그를 만나러 갈 생각이냐?”

“예. 아무래도 그 사람이라면 이 상황에 대해 뭔가 더 자세히 알 것 같아서요.”

“그래, 동창의 병필 태감이라면 수완 좋기로 소문난 자이니 그럴 수 있지. 그러니 지난 십여 년간 동창을 맡아 사실상의 수장 노릇을 하고 있는 것일 테고.”

마삼보에 대해 언급하고 있자니 문득 떠오르는 생각이 있다.

나는 우선순위에서 잠시 뒤로 미뤄 두었던 이야기를 꺼냈다.

“혹시 은영각(隱影閣)에서 동창에 대한 정보를 수집했던 적이 있습니까? 비단 동창뿐만이 아니라 황실에 관한 거라면 뭐든지요.”

“나야 주야장천 남만에만 틀어박혀 있느라 자세한 사정을 알진 못하지만, 과거에는 한창 그랬다고 들었다.”

“과거라면?”

“생각보다 한참 됐지. 그때가 정마대전 무렵이었으니까…… 벌써 오십 년 가까이 됐구먼. 세월 참 빨라.”

오십 년.

자그마치 반세기다.

흐르는 세월 속에 강산(江山)도, 사람도 늙었다.

그 흐름에 휩쓸린 수많은 이들 중 한 사람인 남호는 허리를 툭툭 두드리며 말을 이었다.

“마교 놈들이 중원으로 휩쓸고 내려오자 무림맹이 탄생했고, 그 과정에서 은영각도 설립됐지. 그런 우리가 가장 먼저 손을 뻗은 곳이 어디였을 것 같으냐?”

“설마?”

멈칫하는 내 모습을 보며 남호가 씩 웃었다.

“지금 생각하는 그곳이 맞다. 그래, 황실이었지.”

“……!”

“쉽게 말해서 십만마도(十萬魔徒)지, 상황만 보자면 물경 십만에 달하는 대군이 외세에서 침략한 꼴이나 다름없었다. 더군다나 놈들은 중원과 달리 완벽한 구심점이 있었고.”

“그랬지. 천마(天魔), 그 호로새끼.”

불쑥 끼어든 적천강을 향해 남호가 고개를 끄덕였다.

“문제는 그 호로새끼가 사실상의 왕, 아니 신이나 다름없었던 것 아니겠습니까.”

정마대전이 그토록 치열했고, 순식간에 끝난 이유다.

각자의 사문(師門)과 수장을 가진 정파 무림과 달리 마도(魔道)에 몸담은 자들은 오직 한 사람. 자신들의 교주인 천마의 뜻에 절대복종했다.

만약 정파에 무신이라는 새로운 구심점이 없었고, 삼성과 십왕을 비롯한 정파의 상징적 고수들이 활약하지 않았다면 이미 마도천하가 되었을 거라는 이야기가 괜히 지금까지 떠도는 것이 아니다.

그리고 그런 천마와 십만마도를 몰아내기 위해, 무림맹은 든든한 동맹을 필요로 했을 테고.

“그래서 황실에 손을 뻗은 겁니까? 함께 천마를 몰아내자고?”

“그랬지. 대국이 우리를 돕는다면 모든 것이 훨씬 수월해졌을 테니까.”

남호가 씁쓸한 어조로 덧붙였다.

“물론 황실 쪽에서는 간만 보다가 뱉어 버렸지만.”

이쯤 되니 나도 더 묻지 않을 수 없을 만큼 궁금해졌다.

처음 말을 꺼낸 목적과는 조금 떨어졌지만, 정마대전 당시 천하 각지에서 벌어진 엄청난 규모의 대전투에서 황실이 개입하지 않았던 이유를 알고 싶었으니까.

“왜 거절당한 겁니까? 십만이나 되는 마교도가 중원을 침범했다면 황실에서도 충분히 나설 만했을 텐데.”

“당시의 천자였던 선황(先皇)이 직접 반대했다고 들었다.”

“선황이요?”

“그래. 중신 여럿이 상소문을 올렸지만 이제 막 즉위한 젊은 황제는 굳게 귀를 닫아걸었지. 대국이 세워진 지 불과 이십 년도 되지 않은 시점이라 민생(民生)을 돌보아야 한다는 것이 그 이유였다.”

남호의 말에 적천강이 코웃음 치며 입을 열었다.

“물론 그럴듯한 개소리지.”

“노선배님의 말씀이 맞습니다. 또다시 병력을 동원하기에는 백성들 눈치도 보이고, 그 피해를 감당하기에는 부담스러우니 정파 무림이라는 방패를 믿고 그저 굿이나 보고 떡이나 먹자는 거였지요.”

“멍청하고 우유부단한 생각이었다. 만약 정마대전에서 마교가 승리했다면, 그 다음은 황실 차례였어.”

“은영각 내부에서도 같은 추측을 했습니다. 천마는 강하고 야망 있는 자였으니 끝내는 대국을 무너트리고 교국(敎國)으로 발돋움했을 거라고요. 하지만 지금껏 언제나 그래 왔듯이, 역사는 결과로 정해지는 것 아니겠습니까?”

고개를 주억거린 남호가 나를 향해 말을 이었다.

“그 이후로는 뭐, 알려진 그대로다. 천마 역시 황실의 개입을 꺼린 탓에 양민들을 최대한 건드리지 않으며 중원 깊숙이까지 진군해 왔고, 십여 년간 이어진 대접전 끝에 정파가 기적적으로 승리했지.”

“그게 끝입니까?”

“그럼 끝이지 뭐가 더 있겠느냐. 아, 굳이 덧붙이자면 알려지지 않은 이야기가 몇 개 있다. 그저 전쟁이 두려웠던 우유부단한 젊은 천자는 또 한 번의 전란 속에서 백성을 지켜 낸 성군이 되었고, 동창과 금의위로 하여금 무림인들을 더욱더 철저하게 감시하게 되었다는 것 정도?”

“……!”

“그게 전부다. 강호의 사건으로 한번 호되게 데일 뻔했으니 어떻게 보면 당연한 이야기지만, 그 후로는 은영각도 황도에 요원을 파견하지 못하게 됐지. 만약 황실의 이목에 걸려 발각된다면 그때는 마교 대신 대국과 전쟁을 벌여야 할 테니까.”

세상에 알려지지 않은 과거의 이야기를 들은 나는, 아니 나를 포함한 화룡각 대원들은 잠시 침묵했다.

심지어 조용히 오향장육을 학살하고 있던 태산이 마저 눈을 끔뻑거리고 있을 정도니, 놀라운 이야기였던 것만큼은 부정할 여지가 없었다.

“아니, 왜 이걸 이제야 얘기해 주시는 거예요?”

“이미 지나간 과거의 이야기니까. 현재만 직시하기에도 바쁜데 케케묵은 낡은 것까지 끄집어 올릴 필요는 없지 않겠느냐?”

어깨를 으쓱한 남호가 문득 눈살을 찌푸렸다.

“한데, 이 이야기가 어쩌다 여기까지 흘렀지? 처음에 물어본 것이 무엇이었느냐?”

“은영각에서 동창에 대한 정보를 수집했던 적이 있냐고 물었는데요. 굳이 동창이 아니어도 좋으니까 황실에 대해서라든지.”

“아, 그래. 그랬지. 그런데 갑자기 그건 왜?”

“다름이 아니라 몇 시진 전쯤에 조금 찜찜한 사실을 알았거든요.”

“찜찜한 사실? 동창에 연관된 것이냐?”

“네. 정확히는 마삼보. 마 태감이요.”

“밑구녕이 찜찜하면 맨손으로라도 닦아야 하는 법. 어디 한번 말해 보거라.”

더러운 말을 쓸데없이 근엄하게 한 적천강이 눈을 빛낸다. 나는 주위를 둘러싼 시선들 속에서 천천히 입을 열었다.

“혹시, 마삼보가 개인적으로 끌어들일 만한 무림인들이 있습니까?”

“무림인들이라면. 어느 문파를 말하는 게냐?”

“어느 문파인지는 잘 모르겠습니다. 생각하시는 것만큼 평범한 무림인들도 아니고요.”

“대관절 그것이 무슨 말이냐?”

“그 무림인들이, 살수(殺手)거든요.”

“……!”

그 순간. 내게 집중되어 있던 사람들의 시선이 두 갈래로 나뉘어 쏟아졌다.

한쪽은 사마표를 향해.

또 다른 한쪽은 신의를 향해.

그리고 아주 잠깐의 침묵이 흐른 뒤, 젊고 늙은 두 사람이 차례대로 입을 열었다.

“왜, 왜 그런 눈으로 날 보는 거요. 나는 착한 사마외도요.”

“저는 이미 오래전에 그 바닥에서 손 뗐습니다. 아, 아니 스승님께서…….”

도둑이 제 발 저린다는 게, 이럴 때 쓰는 표현인가.
```

## Final English reading copy

```markdown
# Chapter 892

I’d faced countless formidable enemies and fought more battles than I could count, but this was a first.

For me—and for everyone else.

“They’re planning to raise the stakes even further… If that guess is right, they’ve got to be completely insane.”

At Jeok Cheongang’s mutter, Namho nodded.

“It’s hard to believe, but for our enemies, it is the fastest shortcut to taking control of the entire Great Nation.”

He was right.

Nothing was more decisive than an all-or-nothing match. Once a single battle with everything on the line was over, the winner would survive, and the loser would disappear.

The problem was that we had no idea what lay behind our enemies’ confidence.

*Where the hell are they getting that confidence?*

It was easy to call it a single decisive battle, but this wasn’t just another life-and-death duel of the kind that happened all the time between martial artists.

It would be an enormous battle with the fate of the Great Nation at stake—and, without a doubt, a bloodbath that would paint the imperial capital red.

*If we lose this battle, the restoration army will be wiped out in an instant, and Dark Heaven and the Emperor will take complete control of the Great Nation. But is that really all?*

Namho had said it earlier.

That this was the fastest shortcut for the enemy.

But the shortcut wasn’t always the best choice. There was a reason people took the established road.

A main road was wide and straight. Even if it took a little longer, you could reach your destination easily and comfortably.

A shortcut, though, was narrow and complicated. The ground was uneven and unpaved, and sometimes you had to pass through shadowy alleys where danger—and foul smells—lurked.

*And yet the enemy chose the latter. They even used me as bait to do it.*

Even if it was for the sake of the bigger picture, a series of choices like these seemed almost reckless.

They hadn’t stopped me, even though I’d repeatedly gotten in Dark Heaven’s way. They’d deliberately made a battle they absolutely had to win that much harder.

And I wasn’t the only one thinking about it.

“Why?”

Jeok Cheongang rose and paced around, muttering as if to himself.

“Even if they didn’t know this old man was in the imperial palace, they should have at least considered the possibility if they knew what happened in Nanman.”

Dark Heaven’s intelligence network was vast. There was no way So Gyo or the Emperor hadn’t heard what even Ma Sanbao knew.

For all I knew, they’d obtained that same information themselves.

That Fire King Jeok Cheongang had intervened in the process of defeating the Southern Heaven Demon Empress, and had left Nanman with me.

And still, they’d let me go.

As if they hadn’t even considered the existence of a predator called the Fire King. As if even if that predator joined the battle, it wouldn’t make the slightest difference to the outcome.

*This… really is strange.*

No, more than strange. Suspicious.

I could understand why they might discount me: I was already in rough shape, and they might have been acting on some kind of instruction from the Lord of Heaven.

But Jeok Cheongang?

He’d already stood at the top of the Ten Kings during the Great Faction War. They said that if he’d joined the war a little earlier, he could have stood shoulder to shoulder with the Three Saints. He was a monster among monsters.

*Without the Blood Lord’s impossible ability to recover, he would’ve died instantly several times over. And during the Sichuan Blood Tragedy, he fought the Western Heaven Demon Lord with a body that had only just recovered from being poisoned.*

Of course, the Southern Heaven Demon Empress, the most recent opponent he’d faced, was an exception.

The magical power flowing from the rift had turned her halfway into a monster. And after burning her innate qi, she’d displayed a level of martial prowess beyond human limits.

But they weren’t even considering Jeok Cheongang?

*Bullshit.*

I stared into the air, my gaze sinking as I thought.

The more I considered it, the more things didn’t add up.

There was definitely something going on.

Something I didn’t know yet. A secret no one had uncovered.

And I knew one person who might help answer at least some of these questions.

“Ma Sanbao.”

At the name that slipped from my lips, Namho nodded as if he’d caught on.

“You’re going to see him?”

“Yes. I think he’d know more about what’s going on.”

“Right. The East Depot’s Brush-Holding Eunuch is famous for his resourcefulness. I suppose that’s why he’s been in charge of the East Depot for the past decade or so, acting as its de facto head.”

Mentioning Ma Sanbao brought something else to mind.

I brought up a question I’d set aside for later.

“Has the Hidden Shadow Pavilion ever gathered information on the East Depot? Or on anything else concerning the imperial household?”

“I spent all my time holed up in Nanman, so I don’t know the details. But I’ve heard that they did quite a bit of that in the past.”

“How far back?”

“Quite a while ago. Around the time of the Great Faction War… That was nearly fifty years ago now. Time really flies.”

Fifty years.

Half a century.

As the years went by, the land and its people grew old.

Namho, one of the countless people swept along by that current, patted his lower back and continued.

“When the Demonic Cult swept down into the Central Plains, the Murim Alliance was formed. The Hidden Shadow Pavilion was established in the process. Where do you think we reached out first?”

“You mean…”

Namho grinned as he watched me hesitate.

“That’s right. The place you’re thinking of. The imperial household.”

“…”

“Put simply, the Hundred Thousand Demonic Disciples amounted to an army of a hundred thousand invading from a foreign land. What’s more, unlike the Central Plains, they had a perfect center of command.”

“They did. The Heavenly Demon, that son of a bitch.”

Jeok Cheongang cut in, and Namho nodded.

“The problem was, that son of a bitch was effectively their king—or rather, practically a god.”

That was why the Great Faction War had been so fierce, and why it had ended so quickly.

Unlike the orthodox faction, whose martial world was made up of people loyal to their own schools and leaders, those who followed the Demonic Path obeyed only one person: their Cult Leader, the Heavenly Demon.

It wasn’t for nothing that people still said the world would have belonged to the Demonic Path if the orthodox faction hadn’t had a new center of command in the Martial God, and if its symbolic masters—including the Three Saints and the Ten Kings—hadn’t fought so fiercely.

And to drive out the Heavenly Demon and his hundred thousand disciples, the Murim Alliance must have needed a powerful ally.

“So the Alliance reached out to the imperial household? To drive out the Heavenly Demon together?”

“That’s right. If the Great Nation helped us, everything would’ve been much easier.”

Namho added bitterly,

“Of course, the imperial household tested the waters for a while, then spat the idea out.”

By this point, I was so curious that I couldn’t help asking more.

It was a little off from what I’d originally wanted to discuss, but I wanted to know why the imperial household hadn’t intervened in the enormous battles that had erupted across the land during the Great Faction War.

“Why did they refuse? If a hundred thousand members of the Demonic Cult had invaded the Central Plains, surely the imperial household could’ve stepped in.”

“I heard the late Emperor, who was the Son of Heaven at the time, opposed it personally.”

“The late Emperor?”

“That’s right. Several high ministers submitted memorials, but the young Emperor, who had only just ascended the throne, firmly shut his ears. The Great Nation had been founded less than twenty years earlier, so he said he needed to take care of the people.”

At Namho’s words, Jeok Cheongang snorted.

“Of course, that’s a load of convincing-sounding bullshit.”

“Senior is right. They didn’t want to risk the people’s displeasure by mobilizing troops again, and they couldn’t bear the cost of the damage. They trusted the orthodox Murim to act as a shield, then sat back to enjoy the show.”

“It was a foolish, indecisive choice. If the Demonic Cult had won the Great Faction War, the imperial household would’ve been next.”

“The Hidden Shadow Pavilion came to the same conclusion. The Heavenly Demon was strong and ambitious. In the end, he would have brought down the Great Nation and established a theocracy. But as always, history is determined by its outcome, isn’t it?”

Namho nodded and turned to me.

“After that, things went as everyone knows. The Heavenly Demon also didn’t want the imperial household to get involved, so his forces advanced deep into the Central Plains while avoiding harm to ordinary people as much as possible. After more than a decade of fierce battles, the orthodox faction won by a miracle.”

“That’s it?”

“What else would there be? Oh, if I had to add anything, there are a few things people don’t know. The indecisive young Son of Heaven, who’d only been afraid of war, became a sage king who’d protected the people through yet another conflict. And he ordered the East Depot and the Embroidered Uniform Guard to keep an even closer watch on martial artists.”

“…”

“That’s all. The imperial household had nearly been burned by an incident in the martial world, so in a way, it was only natural. After that, the Hidden Shadow Pavilion couldn’t send agents into the imperial capital anymore. If the imperial household spotted and exposed them, we’d have to fight the Great Nation instead of the Demonic Cult.”

After hearing about a past unknown to the world, I—and the other members of the Fire Dragon Pavilion—fell silent for a moment.

Even Taishan, who’d been quietly slaughtering the five-spice pork, was blinking. There was no denying it was a shocking story.

“Why are you only telling us this now?”

“Because it’s in the past. We’re busy enough focusing on the present without dragging up old, dusty matters.”

Namho shrugged, then suddenly furrowed his brow.

“Wait, how did we end up talking about this? What was it you asked me at first?”

“I asked whether the Hidden Shadow Pavilion had ever gathered information on the East Depot. It didn’t have to be the East Depot specifically—anything about the imperial household.”

“Oh, right. That’s what it was. Why did you ask?”

“Because I learned something a little unsettling a few shichen ago.”

“Something unsettling? Is it connected to the East Depot?”

“Yes. More specifically, to Ma Sanbao. Eunuch Ma.”

“If your ass feels dirty, you wipe it—even if you have to use your bare hand. Now tell me.”

Jeok Cheongang said something filthy in an unnecessarily solemn tone, his eyes gleaming. Under the many gazes fixed on me, I slowly began to speak.

“Is there anyone Ma Sanbao might personally bring in from the martial world?”

“People from the martial world? Which sect?”

“I don’t know what sect they belong to. And they’re not exactly ordinary martial artists, either.”

“What on earth are you talking about?”

“They’re assassins.”

“…”

At that moment, the gazes that had been fixed on me split in two directions.

One toward Sama Pyo.

The other toward the Divine Physician.

After a brief silence, the two of them spoke in turn, one young and one old.

“Wh-Why are you looking at me like that? I’m one of the good practitioners of demonic, heterodox arts.”

“I left that line of work a long time ago. N-No, I mean my Master…”

Was this what people meant when they said a guilty conscience needs no accuser?
```

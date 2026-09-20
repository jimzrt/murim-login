<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0525.txt",
      "sha256": "3748395551523f5518dda786fa1f6ed4668c9e017b07f986f172bc6a56310355",
      "bytes": 13831
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "d9208d39db000c35a9555a4466d84f94ebb8a21058a590cb96a097b99c136176",
      "bytes": 4345
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "6ec0b673b8c54d42db974bbdb63b12192819a063c879b72e189ea6a046984fd7",
      "bytes": 167560
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "16aa85d2b282165f3f410709b2759e6018004b2804644d4ab93ac6b9f8d8a7eb",
      "bytes": 1006
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "3367447477f9c23c09e3ef851aae0e3e0f39b37cd7a69e597a00245a85092d0a",
      "bytes": 553
    },
    {
      "path": "characters/Heaven-Shaking Venerable Nun.md",
      "sha256": "0b1cbbf97f877084f354a52eadacaf56fa45a0789f2276355338d18e56ed986d",
      "bytes": 510
    },
    {
      "path": "characters/Hong Dao.md",
      "sha256": "8c5691a035d3336eff5e5c38cf44222db9d7873fac48cdfd4c29b5f1a51ae92e",
      "bytes": 1000
    },
    {
      "path": "characters/Human Butcher.md",
      "sha256": "5d04a103e46e376865b6c2bb29c1229f868489b5676d90d47cec15a6c46c8be4",
      "bytes": 667
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "98b2b39f6a0c8d103e86d131696cd890574d96b9aa1cb1e3a5cd4ffb4699ebef",
      "bytes": 1630
    },
    {
      "path": "characters/Mae Jonghak.md",
      "sha256": "003f65e9a9b35a163de2f457da34297a00434d403e1b83bedddc1764e8f96595",
      "bytes": 1062
    },
    {
      "path": "characters/Song Ho.md",
      "sha256": "97d393b8f3be78ca4060a966c0d6bc154b5b9265202c8bb58711e9dd5916a40c",
      "bytes": 726
    },
    {
      "path": "characters/Tang Sadok.md",
      "sha256": "529aff0b638319abc5c62416b7aa306b0221366b344aa884aa5734d582742575",
      "bytes": 758
    },
    {
      "path": "characters/Tang Taesang.md",
      "sha256": "52435c576033510adc5fd56ccb7ea3166a8b92bc4554fb2c6544d6624c920cd2",
      "bytes": 601
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "5055fd089787aa6ed7851e0569df53546ad0b97272966a57ddd5f2bcd686b8b4",
      "bytes": 158189
    }
  ],
  "estimated_tokens": 12948
}
-->

# Durable State Update — Chapter 525

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 525. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 525. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history.
`names` contains only newly required Korean-to-English rows that are absent from
Exact glossary matches; Korean keys must occur in the source. Do not repeat
glossary matches. The controller drops rows already in the names ledger.
`address_pairs` contains only newly required speaker→addressee rows that are
absent from Matched address pairs. Speaker and addressee must be Hangul source
spellings such as 진태경 or 혁무진, never English names. Arabic digits are
allowed in titles such as 1팀장. At least one endpoint must occur in the source.
The controller drops pairs already in the address ledger. Do not invent
risk-register rows. Beat plot paragraphs are plain strings; continuity and
translation decisions are concise list items.
Return this exact shape:

{
  "chapter": 525,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 525,
    "continuity_sources": [525],
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
    "Jeok Cheongang's Heart Demon and the dark memories binding him have been expelled; he entered a new realm, achieved Returned to Youth, and began his long-promised duel with Nangong Cheon, the Azure Sky Sword King.",
    "Mungyeong is the Slaughter Saint and former Divine Physician, a Returned to Youth Supreme Peak master and the greatest assassin in history; he has ended Taekyung's direct training, given him a custom fire-qi pill, taught him martial principles, and assigned him a final task.",
    "Zhuge Feng's Demon-Sealing Formation blocks all mana from the exposed Gate by drawing in natural qi, but its permanence and repeatability remain unresolved.",
    "Jang Taebo is the Jin Family of Taiyuan's Master of Ironcraft Hall and is summoning renowned artisans to process the Water God Dragon's remains.",
    "Mae Jonghak remains the New Murim Alliance's administrator after Jeok Cheongang refused the Alliance Leader position because it was troublesome; Mae accepts the burden because someone must do it.",
    "Song Ho is the reinstated Chief of the Hidden Shadow Pavilion and commands a vetted intelligence network, including five concealed agents whom Taekyung detected inside the Alliance.",
    "The Southern Heaven Demon Empress is traveling toward Yunnan and expects to cause further deaths.",
    "Unnamed, Hong Dao's practical Disciple, endured three months in Repentance Cave, achieved enlightenment, received Shaolin's Great Restoration Pill, and is now a scarred Supreme Peak master and Jung Ho's young Martial Uncle.",
    "The Black Dragon Demon Gate is an ancient unorthodox faction that once belonged to the Demonic Cult's Twelve Branches and now ranks among the Central Plains' strongest unorthodox powers.",
    "Jin Taekyung completed Stage 2 of Fake Murim Practitioner, achieved Single Reed Crossing the River, improved his internal-energy control and attributes, gained 50 bonus points and substantial EXP, leveled up, and achieved Three Flowers Gather at the Crown but not Five Qi Returning to Origin.",
    "Wudang's second report identifies the Killing Ghost as Jang Sam, a fisherman who disappeared near Mount Wudang; Taekyung suspects the Blood Fish caused or participated in his transformation.",
    "Dark Heaven has not opened a second Gate yet, and the Murim Alliance and Hidden Shadow Pavilion are mobilizing against future outbreaks; the Murim world is now gathering under one banner while Jin Mukyung consults faction leaders."
  ],
  "continuity_sources": [
    524,
    523
  ],
  "open_questions": [
    "What is the Lord of Heaven's identity, how is he connected to the dangerous force Taekyung associates with his original world, and how can Dark Heaven open Gates?",
    "Where is the Southern Heaven Demon Empress ultimately headed, and what does she intend to do in Yunnan?",
    "What is the outcome of the duel between Jeok Cheongang and Nangong Cheon, the Azure Sky Sword King?",
    "Did the Blood Fish cause Jang Sam's transformation, and could similar Blood Fish or Gate-related transformations occur elsewhere?",
    "How will Taekyung incorporate Mungyeong's martial principles, and what effect will the custom pill have on him?"
  ],
  "safe_through": 524,
  "temporary_decisions": [
    "Render 새외무림 as Outer Murim, 새외 as Outer Lands, 북해빙궁 as North Sea Ice Palace, 야수묘왕 as Beast Miao King, and retain Nanman Beast Palace for 남만야수궁.",
    "Render 소뢰음사 as Small Thunderclap Temple, 광풍사 as Mad Wind Society, 포달랍궁 as Potala Palace, 오독문 as Five Poisons Sect, 독곡 as Poison Valley, 천축 as India, 갠지스강 as Ganges River, and 대환단 as Great Restoration Pill.",
    "Render 파사국 as Persia, 회교도 as Muslims, 영웅건 as hero headband, 대막 as great desert, 귀염권 as Ghost Flame Fist, and 장성 as Great Wall.",
    "Retain sa-eo for 사어, shark for 상어, Old Master for 노야, this old man/I for 노부, Shark Water-Ski Team for 수상스키단, and swift ship for 쾌조선.",
    "Render 화약고 as powder keg, 칠공 as seven apertures, 단환 as pill, 무적자 as The Invincible, 무리 as martial principles, and 구운몽 as The Dream of the Nine Clouds; preserve the chapter's blunt profanity and monster-comparison humor."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 적천강    | **Jeok Cheongang** |
| 매종학    | **Mae Jonghak**    |
| 청풍     | **Cheongpung**     |
| 굉도     | **Hong Dao**       |
| 검성     | **Sword Saint**               | Mae Jonghak    |
| 법왕     | **Dharma King**               | Hong Dao       |
| 무신     | **Martial God**               | —              |
| 독왕     | **Poison King**               | Tang Taesang   |
| 일신     | **One God**         |
| 삼성     | **Three Saints**    |
| 십왕     | **Ten Kings**       |
| 태원진가   | **Jin Family of Taiyuan**        |
| 화산파    | **Huashan**                      |
| 소림     | **Shaolin**                      |
| 무림맹    | **Murim Alliance**               |
| 암천     | **Dark Heaven**                  |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무인     | **martial artist**                               | Default term                                          |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 낭인     | **wandering martial artist**                     |                                                       |
| 정파     | **orthodox faction**                             |                                                       |
| 사파     | **unorthodox faction**                           |                                                       |
| 중원     | **Central Plains**                               |                                                       |
| 강호     | **martial world**                                | Prefer “Murim” where the setting itself is meant      |
| 가주     | **Family Head**                              |
| 문주     | **Sect Leader**                              |
| 장문인    | **Sect Leader**                              |
| 제자     | **Disciple**                                 |
| 사형     | **Senior Brother**                           |
| 명성               | **Fame**                       |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 하남     | **Henan**              |
| 사천     | **Sichuan**            |
| 화산     | **Huashan**            |
| 팔천협    | **Eight Spring Gorge** |
| 정마대전   | **Great Faction War**         |
| 노부      | **this old man / I**                                            |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 경천신니 | **Heaven-Shaking Venerable Nun** | Former Emei Sect Leader and sole Supreme Peak master; killed on Mount Emei. |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 송호 | **Song Ho** | Elderly martial artist known as the Thousand-Faced Fox. |
| 당사독 | **Tang Sadok** | Current Family Head of the Sichuan Tang Clan; also called the Myriad-Poison Asura. |
| 당사문 | **Tang Taesang** | Former Family Head of the Sichuan Tang Clan and Poison King; Tang Sadok’s father. |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 평화 | **Peace Guild** | Guild name. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 오대세가 | **Five Great Families** | Major Murim grouping. |
| 자하신공 | **Zaha Divine Technique** | Huashan internal-energy technique used by Cheongpung. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 천검진인 | **Heavenly Sword True Person** | Taoist-style title of the current Sect Leader of Huashan, who once commissioned a sword from Jang Taebo. |
| 소림사 | **Shaolin Temple** | Temple invoked in Chulwoo’s comparison of Baek Museong’s conduct. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 한서불침 | **Unaffected by Cold and Heat** | Condition attributed to Taekyung after opening both vessels. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 천면호리 | **Thousand-Faced Fox** | Epithet of Song Ho. |
| 은영각 | **Hidden Shadow Pavilion** | Former Murim Alliance intelligence organization. |
| 은영각주 | **Chief of the Hidden Shadow Pavilion** | Office formerly held by Song Ho. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 아미 | **Emei** | Short form for Emei Sect. |
| 아미파 | **Emei Sect** | Murim sect in Sichuan. |
| 호북 | **Hubei** | Province on Ju Gongsan's route from Guangdong to Henan. |
| 장문령부 | **Sect Leader's Command Token** | Copper token carrying the Zhongnan Sect Leader's authority. |
| 성도 | **Chengdu** | Sichuan destination of Taekyung's party. |
| 오대 | **Five Squads** | Named Tang Clan organizational group in Tang Sadok's mobilization order. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 매종학 | 청풍 | grandfather_to_grandson | Pung | affectionate-instructional | Mae Jonghak calls young Cheongpung 풍아 while teaching him the Crouching Tiger Fist. |
| 적천강 | 청풍 | overwhelming_elder_to_young_martial_artist | you / little punk | blunt, amused, and threatening | Jeok Cheongang uses 네, 이놈, and related blunt forms while testing Cheongpung. |
| 청풍 | 적천강 | young_martial_artist_to_overwhelming_elder | Grandpa Jeok | casual-familiar despite deference | Cheongpung uses 적 할아버지 while asking Jeok Cheongang to confirm Taekyung's condition; this is a familial form of address, not literal kinship. |
| 적천강 | 굉도 | old_friends | Hong Dao | familiar and teasing | Uses Hong Dao's personal name in their casual reunion. |
| 굉도 | 적천강 | old_friends | Fire Gate Sect Leader | familiar and teasing | Teases Jeok as the carefree Fire Gate Sect Leader. |
| 송호 | 청년 | elderly_martial_artist_to_younger_martial_artist | Young Hero | formal-polite | Song Ho calls out to the young man as 소협 at the chapter's end. |
| 매종학 | 송호 | savior_to_survivor | you | casual-familiar | Mae uses 자네 while speaking to Song Ho after his identity is recognized. |
| 송호 | 매종학 | rescued_survivor_to_savior | Great Hero; you | formal-deferential and familiar | Song Ho credits Mae with saving his life and addresses him as 대협. |
| 청풍 | 당사독 | young_martial_artist_to_Sichuan_Tang_Family_Head | Family Head | formal-deferential | Cheongpung addresses Tang Sadok as 가주님 while appealing for help. |
| 당사독 | 청풍 | family_head_to_younger_ally | greenhorn | blunt and protective | Tells Cheongpung not to interfere while calling him a 핏덩이. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 매종학 | 적천강 | long-standing martial rival and friend | Great Hero Jeok | casual and familiar | Mae addresses Jeok as 적 대협 while discussing the Alliance Leader position. |
| 적천강 | 매종학 | long-standing martial rival and friend | you | blunt and familiar | Jeok addresses Mae as 당신 while recalling their meeting at Mount Jiuhua. |
| 천면호리 | 매종학 | intelligence_chief_to_alliance_leader | Alliance Leader | formal and deferential | Requests that Mae move elsewhere with the others before he reports further. |

## Listed compact profiles

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 524
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, the grandson and Disciple of Sword Saint Mae Jonghak, and a Supreme Peak martial master known as the Huashan Divine Dragon.
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, a deep love of martial arts, competitive pride, unusual resistance to monster-induced Fear, and discomfort when someone copies his martial arts.
- **Voice:** Dreamy and hazy, with innocent, polite phrasing; he has begun imitating Taekyung's profanity.
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions while Taekyung is his only true martial rival; Tang Sadok has temporarily entrusted Mimi to him.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 524
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Heaven-Shaking Venerable Nun.md

# Heaven-Shaking Venerable Nun (경천신니)

- **Safe through:** Chapter 459
- **Aliases:** Blood Rakshasa
- **Role:** Former Emei Sect Leader and the sect's sole Supreme Peak master, killed on Mount Emei by a one-armed middle-aged man.
- **Personality:** Forthright and fearless against enemies.
- **Voice:** Not established.
- **Relationships:** Respected leader of the Emei Sect; she and three Emei Elders were killed in the same attack.

### Hong Dao.md

# Hong Dao (굉도)

- **Safe through:** Chapter 519
- **Aliases:** Dharma King
- **Role:** Abbot of Shaolin and the Murim's Dharma King; master of Unnamed and the only friend to whom Jeok Cheongang had opened his heart; after leaving the Star-Array Grand Banquet, he was found in a massive pit with both legs severed and catastrophic internal injuries, whispered final words to Jeok Cheongang, and died.
- **Personality:** Calm, responsible, quietly playful, and still regarded by Jeok as lazy for sleeping whenever possible.
- **Voice:** Quiet, deep, weighty, and resonant, with casual familiarity when speaking to Jeok Cheongang.
- **Relationships:** Old friend of Jeok Cheongang and close friend of Peng Cheolhu; master of Unnamed; before his death, entrusted the Green Jade Buddha Staff to Unnamed, warned Jeok about Jongni Chu, Dark Heaven, Unnamed, and the Buddhist Staff, and sent Unnamed to find the Master of Morning Star.

### Human Butcher.md

# Human Butcher (인도)

- **Safe through:** Chapter 524
- **Aliases:** None
- **Role:** Former mysterious Han Chinese mounted-bandit power in Northern Gaoyuan commanding fifty subordinates; a Peak master killed by an unnamed old man in a single move
- **Personality:** Cold, intimidating, and murderous; he kills people as though slaughtering livestock
- **Voice:** Cold, curt, and quietly threatening
- **Relationships:** He is one of four powerful participants at the Northern Gaoyuan gathering, intimidates Temur, and has claimed Ghost Sword Wipeng as his personal target in the proposed attack

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 524
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, and Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Mae Jonghak.md

# Mae Jonghak (매종학)

- **Safe through:** Chapter 522
- **Aliases:** Sword Saint
- **Role:** Sword Saint and Cheongpung's grandfather; he is the New Murim Alliance's sole identified suitable candidate for Alliance Leader and currently handles its administrative affairs.
- **Personality:** Playful, easygoing, and teasing, but capable of handling heavy administrative responsibilities efficiently.
- **Voice:** Friendly, casually familiar, and cheerfully teasing, including when greeting old acquaintances and discussing leadership.
- **Relationships:** Cheongpung's grandfather and martial instructor; taught him the Taeeul Miri Palm; secretly entered Huashan while its Sect Leader slept, left a dagger and handwritten note, and then went into hiding, prompting Huashan's search; fought Jeok Cheongang at Mount Jiuhua more than forty years ago and left after their draw; his old friend Hong Dao left him a letter identifying Jin Taekyung as the Morning Star who would drive away darkness.

### Song Ho.md

# Song Ho (송호)

- **Safe through:** Chapter 521
- **Aliases:** Thousand-Faced Fox
- **Role:** Elderly Peak master known as the Thousand-Faced Fox and current Chief of the Hidden Shadow Pavilion, overseeing a vetted intelligence network that includes highly trained assassins.
- **Personality:** Outwardly genial and relaxed, but observant, forceful, and intimidating when pursuing information.
- **Voice:** Lightly genial and conversational, turning quietly coercive during interrogation.
- **Relationships:** He serves under Mae Jonghak's New Murim Alliance, commands the Hidden Shadow Pavilion, and recognizes Jin Taekyung as Jeok Cheongang's Disciple.

### Tang Sadok.md

# Tang Sadok (당사독)

- **Safe through:** Chapter 459
- **Aliases:** Myriad-Poison Asura
- **Role:** Current Family Head of the Sichuan Tang Clan, gravely wounded in the Three-Gate Bloodbath and recovering under medical care.
- **Personality:** Grim, cold, blunt, suspicious, and unsentimental, with fierce concern for the Tang Clan’s affairs.
- **Voice:** Hissing, curt, authoritative, and threatening.
- **Relationships:** Tang Taesang was his father and predecessor as Family Head, his unnamed nephew serves as Master of the Gatekeeper Pavilion, and Mimi is his cherished old friend and companion, currently entrusted temporarily to Cheongpung while the clan's future is uncertain.

### Tang Taesang.md

# Tang Taesang (당사문)

- **Safe through:** Chapter 352
- **Aliases:** Poison King
- **Role:** Former Family Head of the Sichuan Tang Clan and Supreme Peak master once renowned as the world’s greatest authority on poison and hidden weapons; he was murdered before the current events.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** Tang Sadok was his only child and successor as Family Head; his murder has placed the Sichuan Tang Clan on a campaign against the unidentified perpetrators.

## Korean source

```text
＃525화



사방이 고요했다. 불과 한 시진 전만 해도 수많은 이들이 드나들던 맹주전(盟主殿)에는 오직 한 사람만이 남아 있었다.

“세월이 참으로 빠르구나.”

청년, 검성 매종학은 작게 뇌까렸다.

허공을 응시하는 그의 시선은 먼 과거 어딘가를 더듬고 있었다. 이제는 기억하는 이조차 몇 남지 않은, 케케묵은 기억이다.

‘다들 그리 가 버렸지.’

매종학과 같은 기억을 공유하던 이들 중 끝까지 천수(天壽)를 누린 사람은 극히 적었다.

대부분은 이름 모를 광야와 들판에 쓰러져 두 번 다시 일어나지 못했다.

정마대전(正魔大戰)이라는 괴물은 그렇게 숱한 죽음을 낳았고, 살아남은 이들을 영웅으로 만들었다.

‘하지만 결국…… 또다시 이리되는군.’

어느덧 강산이 네 번 바뀌고도 남을 만한 시간이 흘렀다.

천하에는 평화가 찾아왔고, 전란의 소용돌이에서 겪어야 했던 고통과 슬픔은 무뎌졌으며 정파 무림은 승리의 영광을 노래했다.

그리고 영원토록 푸를 것만 같던 하늘에, 암천(暗天)이라는 먹구름이 찾아왔다.

‘이제 평화는 끝났다.’

전쟁의 참혹함을 이해하지 못하던 코흘리개 아이는 중년의 나이가 되었고, 병장기를 뽑아 들고 의기를 불태우던 청년은 노인이 되었다.

당시에는 태어나지도 않았던 이들은 의협(義俠)이 아닌 영광을 좇아 하남으로 왔다.

살아온 인생과 성격, 목적. 모든 것이 다르다.

그리고 검성 매종학은 잘 알고 있었다. 다른 누구도 그 자신이, 이들 모두를 이끌고 다시 한번 맞서 싸워야 한다는 것을. 천하를 도탄에 빠트리려는 암천을 상대로 승리해야 한다는 것을.

굳게 닫혀 있던 매종학의 입술 사이로 나지막한 목소리가 흘러나온 것은 그때였다.

“문득 그런 의문이 들고는 하오. 내가 정말 할 수 있을까, 하는 의문이.”

혼잣말이 아니다. 매종학도, 언제부터인가 조용히 문 앞을 지키던 누군가도 그 사실을 알고 있었다.

건장한 체격의 노인, 천면호리(千面狐狸) 송호는 대답과 함께 걸음을 내디뎠다.

“하실 수 있습니다.”

또각.

의족(義足)의 끄트머리가 바닥을 찍는 소리가 유난히도 크게 울려 퍼진다. 늘어트린 백발 사이로 노회한 눈동자가 힘 있게 빛을 발했다.

“아니, 해내셔야 합니다.”

“알고 있소.”

매종학은 가벼운 한숨을 내쉬었다.

“허나 나는 일평생 검밖에 몰랐소. 덕분에 검성(劍星)이라는 허명 역시 얻었지.”

“바로 그 검성이니, 모두가 믿고 따를 것입니다.”

“무인과 지도자의 그릇은 다른 법. 일파(一派)의 장문인조차 되지 못했던 나요.”

“되지 못했던 것이 아니라, 하지 않으셨던 거겠지요.”

천면호리의 말은 사실이었다.

정마대전이 막을 내리고 선대 장문인이 숨을 거두자, 화산파의 제자 모두는 검성 매종학이 자신들의 새로운 장문인이 되리라 믿어 의심치 않았다.

“하지만 거절하셨지요. 결국 장문령부는 제자인 천검진인(天劍眞人)께 돌아갔습니다.”

“당연한 일이었소. 나보다 화산파의 장문인에 적합한 아이였으니까. 그리고…….”

매종학이 허리춤에 찬 애검을 매만지며 말을 이었다.

“난 그저 검이 좋았다오.”

그런 매종학을 가만히 응시하던 천면호리가 불쑥 입을 열었다.

“제가 말씀드렸는지 모르겠군요.”

“무엇을 말이오?”

“그분께서도 한때 같은 고민을 하셨다는 것을 말입니다.”

“그분이라면…… 설마 무신(武神)을 말하는 거요?”

천면호리는 작게 고개를 끄덕였다.

“세인들이 바라보는 그분은 완전무결했습니다.”

“알고 있소. 무신께서는 모든 면에서 뛰어났지. 아니, 압도적이었소.”

“하지만 그분 역시 사람이었습니다. 그리고 마침내 해내셨지요. 어째서인지 지금 이 늙은이의 눈에는 두 분이 겹쳐 보이는군요.”

“……!”

순간, 매종학의 신형이 덜컥 굳었다. 곧은 자세로 자신을 바라보는 노강호를 한동안 말없이 응시하던 그가 불쑥 입을 열었다.

“송 대협.”

“말씀하십시오.”

“참으로…… 좋은 날이오.”

“하늘이 맑습니다.”

“시간을 물어보아도 되겠소?”

“오시(午時)입니다. 모든 이가 한 사람을 기다리고 있지요.”

“내가 늦었구려.”

“늦지 않았습니다. 이제 시작이니까요.”

검성 매종학은 고개를 돌렸다. 활짝 열린 창밖으로 강렬한 햇빛이 쏟아지고 있었다.

‘그래, 참으로 좋은 날이다.’

마음속으로 다시 한번 되뇌는 한 마디. 푸른 하늘을 눈에 담은 그가 천천히 돌아섰다.

동시에 천면호리는 깨달았다. 지금 자신의 눈앞에 있는 이 청년은 더 이상 한 사람의 무인이 아니라는 것을.

“은영각주(隱影閣主).”

귓가를 파고드는 나직한 목소리.

은영각은 맹주전 직속이며, 우두머리인 은영각주에게 명령할 권한을 지닌 이는 오직 한 사람뿐이다.

크게 심호흡한 천면호리는 포권을 취했다.

“은영각주 송호. 맹주님의 하명을 기다립니다.”

다음 순간, 매종학의 입술 사이로 흘러나온 것은 신(新) 무림맹의 시작인 동시에 새로운 무림맹주의 첫 번째 명령이었다.

“깃발을 세우러 가세.”

노강호의 눈꺼풀이 파르르 떨렸다. 이어 젊은이의 그것처럼 힘 있는 외침이 뒤를 이었다.

“존명(尊命)!”



* * *



나는 고개를 들어 하늘을 바라보았다. 푸른 하늘 위, 어느덧 중천에 걸린 태양이 강렬한 햇빛을 뿜어내고 있다.

시원한 바람 한 줄기조차 불어오지 않는 날씨. 문득 머릿속에 스치는 생각 하나가 있었다.

‘뜨겁다.’

뜨거우나 덥지는 않다.

그것은 비단 내가 초절정에 오르며 한서불침(寒暑不侵)의 경지에 다다랐기 때문만은 아니다.

지금 이 순간에도 뜨겁다고 느끼는 것은 햇빛이 아닌, 열기였다. 수많은 이들이 내뿜고 있는 기세라고 불러도 좋았다.

스으으으.

높게 솟은 단상 아래, 헤아릴 수 없을 만큼 수많은 무림인이 뿜어내는 기세에 바람마저 멈춘 듯했다.

아지랑이처럼 피어오르는 기운은 태양으로부터 쏟아지는 햇빛보다 뜨겁게, 동시에 거세게 타오르고 있었다.

그리고 그 열기를 뚫고, 마침내 모두가 기다리던 한 사람이 모습을 드러냈다.

저벅. 저벅.

힘 있는 발걸음 소리가 모두의 귓가를 파고들었다. 단지 그것만으로도 전신이 긴장되고 정신이 깨어난다.

어제까지만 해도 술에 취해 난동을 부리던 낭인도, 서로를 향해 한바탕 드잡이질을 벌인 정파와 사파의 무림인도 마른침을 꿀꺽 삼켰다.

이 모든 것이 한 사람이 뿜어내는 존재감 때문이었다.

‘검성(劍星) 매종학.’

일신, 삼성, 십왕.

구파일방과 오대세가가 천하를 지탱하는 열다섯 개의 기둥이라면, 저 이름의 주인들은 작금의 천하를 새롭게 탄생시킨 영웅들이다.

땅에는 열 명의 왕, 그 위로 펼쳐진 것은 누구도 닿을 수 없는 무신의 하늘. 그 하늘을 수놓은 세 개의 별.

그리고…….

‘그중에서도 가장 빛나는 별.’

검성 매종학. 또 다른 이름은 천하제일검(天下第一劍).

처처처척!

수천에 달하는 무인들이 일시에 갈라진다.

어떤 함성도, 탄성도 들려오지 않는다.

누군가는 검성 매종학의 젊어진 모습에 경악하고, 누군가는 피부로 느껴지는 그의 압도적인 기세에 전율했겠지만, 감히 입 밖으로 소리 내어 말하거나 의문을 표하는 자는 존재하지 않았다.

‘아니, 의심할 수 없겠지.’

저것은 오직 단 한 사람을 위한 길이다.

그리고 인의 장막을 뚫고 마침내 높게 솟은 단상에 오른 거인은, 잔잔한 눈빛으로 주위를 쓸어 보았다.

“오래들 기다리셨소.”

단상 위는 선택받은 자들을 위한 자리다.

소위 명문대파라 불리는 일파(一派)의 문주와 일가(一家)의 가주들. 혹은 출신과 상관없이 지금껏 숱한 명성을 쌓은 협객과 고수들이 이 자리의 주인이다.

‘적천강과 나, 태원진가 역시 마찬가지고.’

하지만 이 단상 위의 사람들이 새로운 무림맹의 주축이라면, 검성 매종학은 무림맹의 주춧돌이자 머리라고 할 수 있다.

나를 포함한 모두는 누가 먼저랄 것도 없이 자리에서 일어나 매종학을 향해 포권을 취했다.

수십 명이 동시에 입을 열었지만, 이어지는 목소리는 한 사람이 말한 것처럼 똑같다.

“맹주님을 뵙습니다.”

그 누구도, 심지어 내 양 옆자리에 앉은 적천강과 청풍조차도 진중한 얼굴로 예의를 갖춘다.

그 모습을 바라보며 흐릿하게 웃은 매종학이 고개를 끄덕이고 돌아섰다.

그리고 다음 순간. 수천, 혹은 일만에 달할지도 모르는 무림인들은 똑똑히 들을 수 있었다.

천지를 뒤흔드는 거인의 목소리를.

“평화는 끝났소.”

“……!”

사방을 에워싼 공기가 터져 나갔다.

우뚝 서 있던 거목이 파르르 떨리고, 단상 아래 운집한 군웅들의 신형이 석상처럼 굳는다.

미증유의 공력을 실어 말을 잇는 매종학에게서, 지금껏 봐 온 엉뚱한 모습은 더 이상 찾아볼 수 없었다.

“전쟁은 이미 시작되었으며, 또 다른 십만마도(十萬魔徒)가 중원을 향해 다가오고 있소.”

정마대전을 겪어 보지 못한 이들은 있을지라도, 그 참혹했던 전란에 대해 모르는 이는 없다.

나이 지긋한 노강호의 눈동자에는 두려움과 분노가 서렸고, 젊은 무인은 알 수 없는 전율로 몸을 떨었다.

“법왕(法王) 굉도.”

다음 순간 이어지는 매종학의 목소리에, 소림사의 승려들이 작게 법호를 읊었다.

“독왕(毒王) 당사문과 아미파의 경천신니(驚天神尼).”

불편한 몸을 이끌고 먼 길을 떠나온 천독수라 당사독이 녹색 안광을 빛냈고, 아미파의 여승들이 눈물을 흘렸다.

“산서성으로부터 흐르기 시작한 피는 하남으로 이어졌고, 사천과 호북에까지 미쳤소.”

불과 일 년 남짓한 시간 동안 숱한 목숨이 유명을 달리했다.

만인에게 칭송받던 노강호도, 이제 풋내기에 불과한 젊은이도 꽃을 피워 보지도 못한 채 쓰러졌다.

‘팔천협(八天峽).’

지금도 눈을 감으면 떠오르는 기억이다.

산서성의 그 비좁은 협곡에서 죽어간 이들이 대체 몇이었나.

하남에서, 사천에서, 호북에서 쓰러진 이들은 누구였나.

나는 그들의 이름도, 생전 갖고 있던 꿈도 모른다.

다만 그렇게 죽어 간 이들이 무엇을 위해 검을 들었는지는 안다.

‘소중한 것을 지키기 위해서.’

콰아아!

매종학의 전신에서 미증유의 기세가 뻗어 나왔다.

자하신공에 근원을 둔 자줏빛 기운이 그의 어깨 위로 파도처럼 넘실거리고 있었다.

“무기를 들고, 맞서 싸워라.”

바뀐 것은 말투와 기세뿐만이 아니다.

지금의 매종학은 검성이며 천하제일검이기 이전에, 모두를 이끄는 무림맹주다.

“같은 피를 나눈 가족을 위하여. 동고동락한 사형제와 사문을 위하여. 그리고…….”

매종학의 입술 사이로, 거대한 외침이 터져 나왔다.

“우리가 살아가는 이 무림을 지키기 위하여, 무기를 들어라!”

거인이 포효한다. 전율이 등허리를 타고 솟구친다.

사방을 가득 메운 무림인들은 참았던 숨을 토해 내며 함성을 내질렀다.

“와아아아아아!”

“멸마(滅魔)를 위하여!”

쉬쉭, 차차차차창!

세상이 온통 빛으로 물들었다. 헤아릴 수 없이 많은 병장기가 머리 위로 쏟아지는 햇빛을 받아 번쩍이고 있었다.

“와아아아아아!”

“협의(俠義)를 위하여!”

쉬쉭, 차차차차창!

세상이 온통 빛으로 물들었다. 헤아릴 수 없이 많은 병장기들이 머리 위로 쏟아지는 햇빛을 받아 번쩍이고 있었다.

그리고 그 눈부시고도 장엄한 광경을 응시하던 매종학은, 자신의 발아래 놓여진 거대한 깃발을 붙잡았다.

무림맹(武林盟).

용사비등한 필체로 써 내려간 세 글자가 적힌 저 깃발을 들어 올리면, 새로운 시대가 시작된다.

그러나 다음 순간, 매종학이 보인 행동은 모두의 예상을 벗어났다.

“적 대협. 도와주시겠소?”

“……!”

피부로 사람들의 동요가 느껴진다. 그리고 말없이 매종학을 바라보던 적천강이 불쑥 입을 열었다.

“깃발이 무거운가?”

“아직은 그런 것 같소.”

“그 깃발은 노부에게도 무겁게 느껴지는군. 그리고 손은 많을수록 좋지.”

다음 순간, 나는 내가 무엇을 해야 할지 깨달았다.

적천강의 눈짓에 앞으로 걸음을 옮긴 나와 청풍은 동시에 깃발을 움켜잡았다.

그리고 힘주어 일으켜 세웠다.

무림맹의 탄생이었다.
```

## Final English reading copy

```markdown
# Chapter 525

The Alliance Leader’s Hall was quiet in every direction. Only one person remained in the hall where countless people had come and gone just one shichen—approximately two hours—earlier.

“How quickly the years pass.”

The young man, Sword Saint Mae Jonghak, murmured the words under his breath.

His gaze was fixed on empty space, reaching back toward some distant point in the past. It was a stale old memory that hardly anyone alive still remembered.

*They all went that way.*

Of the people who shared the same memories as Mae Jonghak, very few had lived out their natural spans.

Most had fallen in nameless wastelands and fields, never to rise again.

The monster known as the Great Faction War had given birth to countless deaths and turned those who survived into heroes.

*But in the end… it’s happening again.*

Enough time had passed for the mountains and rivers to change four times over.

Peace had come to the world. The pain and sorrow endured in the whirlpool of war had faded, and the orthodox Murim had sung of the glory of victory.

Then, beneath a sky that had seemed destined to remain blue forever, a dark cloud called Dark Heaven had appeared.

*Peace is over now.*

The runny-nosed child who had not understood the horrors of war had become middle-aged, while the young man who had drawn his weapon and burned with righteous indignation had grown old.

Those who had not even been born back then had come to Henan in pursuit of glory rather than justice.

Their lives, personalities, and goals were all different.

And Sword Saint Mae Jonghak knew it well. He—and no one else—would have to lead them all into battle once again. He would have to defeat Dark Heaven, which sought to plunge the world into misery.

That was when a low voice slipped between Mae Jonghak’s firmly closed lips.

“Every now and then, I find myself wondering. Wondering whether I can truly do this.”

It was not a soliloquy. Mae Jonghak knew it, as did the person who had been quietly standing guard outside the door for some time.

The sturdy old man, Thousand-Faced Fox Song Ho, stepped forward as he answered.

“You can.”

Clack.

The tip of his prosthetic leg struck the floor, the sound echoing unusually loudly. Beneath his hanging white hair, his shrewd eyes shone with force.

“No—you must.”

“I know.”

Mae Jonghak let out a quiet sigh.

“But I’ve known nothing but the sword my entire life. Thanks to that, I even gained the empty title of Sword Saint.”

“It is precisely because you are the Sword Saint that everyone will trust and follow you.”

“The vessel of a martial artist and the vessel of a leader are different. I couldn’t even become the Sect Leader of a faction.”

“It’s not that you couldn’t. You simply chose not to.”

The Thousand-Faced Fox was speaking the truth.

When the Great Faction War ended and the former Sect Leader passed away, every disciple of Huashan had firmly believed that Sword Saint Mae Jonghak would become their new Sect Leader.

“But you refused. In the end, the Sect Leader’s Command Token went to your Disciple, Heavenly Sword True Person.”

“It was only natural. He was more suited to becoming Huashan’s Sect Leader than I was. And…”

Mae Jonghak ran his fingers over the treasured sword at his waist before continuing.

“I simply liked the sword.”

The Thousand-Faced Fox gazed quietly at Mae Jonghak, then suddenly spoke.

“I don’t know whether I ever told you this.”

“Told me what?”

“That person once struggled with the same concern.”

“If you mean that person… surely you’re talking about the Martial God?”

The Thousand-Faced Fox gave a small nod.

“To the people of the world, that person seemed perfect in every way.”

“I know. The Martial God excelled at everything. No—he was overwhelming.”

“But he was a person too. And in the end, he succeeded. For some reason, these old eyes see the two of you overlapping.”

“……!”

Mae Jonghak’s body abruptly stiffened. After silently regarding the old martial artist standing upright before him for some time, he suddenly spoke.

“Great Hero Song.”

“Yes?”

“It truly is… a fine day.”

“The sky is clear.”

“May I ask the time?”

“It is the wu hour. Everyone is waiting for one person.”

“I’m late.”

“You’re not late. This is only the beginning.”

Sword Saint Mae Jonghak turned his head. Powerful sunlight poured through the wide-open window.

*Yes. It truly is a fine day.*

He repeated the words once more in his heart. After taking in the blue sky, he slowly turned around.

At the same time, the Thousand-Faced Fox realized it.

The young man standing before him was no longer merely a martial artist.

“Chief of the Hidden Shadow Pavilion.”

The quiet voice pierced Song Ho’s ears.

The Hidden Shadow Pavilion was directly subordinate to the Alliance Leader’s Hall, and there was only one person with the authority to command its chief.

Song Ho took a deep breath and clasped his hands.

“Song Ho, Chief of the Hidden Shadow Pavilion. I await the Alliance Leader’s command.”

The next moment, the words that slipped from Mae Jonghak’s lips were the beginning of the New Murim Alliance and the first order of its new Alliance Leader.

“Let’s go raise the flag.”

The old martial artist’s eyelids trembled. Then a powerful cry, as forceful as any young man’s, followed.

“As you command!”

* * *

I raised my head and looked at the sky. The sun, already hanging high in the middle of the blue heavens, poured down fierce sunlight.

Not even a cool breeze stirred in the heat. A thought suddenly flashed through my mind.

*It’s hot.*

It was hot, but not sweltering.

That was not merely because I had reached the state of Unaffected by Cold and Heat after attaining the Supreme Peak realm.

What felt hot at this very moment was not the sunlight, but the heat itself. It would have been just as accurate to call it the aura radiating from countless people.

Sssss.

Below the high platform, the aura released by an immeasurable number of martial artists seemed to have brought even the wind to a halt.

The qi rising like a heat haze burned hotter and fiercer than the sunlight pouring down from the sun.

Then, cutting through that heat, the person everyone had been waiting for finally appeared.

Thud. Thud.

The forceful sound of his footsteps pierced everyone’s ears. That alone was enough to tense their entire bodies and clear their minds.

The wandering martial artist who had been causing a drunken disturbance only yesterday, as well as the orthodox and unorthodox martial artists who had gotten into a full-blown brawl with each other, all swallowed dryly.

Everything was because of the presence radiating from a single person.

*Sword Saint Mae Jonghak.*

The One God, Three Saints, and Ten Kings.

If the Nine Sects and One Gang and the Five Great Families were the fifteen pillars supporting the world, then the people bearing those titles were the heroes who had given the world a new beginning.

Ten kings stood upon the earth. Above them stretched the unreachable sky of the Martial God, and three stars adorned that sky.

And…

*The brightest star of them all.*

Sword Saint Mae Jonghak. Also known as the Number One Sword Under Heaven.

Shhk-shhk-shhk!

The thousands of martial artists split apart all at once.

No cheers or exclamations could be heard.

Some were stunned by Sword Saint Mae Jonghak’s youthful appearance, while others shuddered at the overwhelming aura they could feel against their skin. But not one dared voice a question or say anything aloud.

*No. There’s no room for doubt.*

This was a path meant for one person alone.

And the giant who finally stepped through the ranks of people and climbed onto the high platform swept his calm gaze across the surroundings.

“You’ve all been waiting a long time.”

The platform was a place reserved for the chosen.

The Sect Leaders of factions known as prestigious great sects and the Family Heads of great families. Or, regardless of their origins, heroes and masters who had built up immense fame. They were the people who belonged on this platform.

*Jeok Cheongang and I, as well as the Jin Family of Taiyuan, are no different.*

But if the people on the platform were the pillars of the new Murim Alliance, Sword Saint Mae Jonghak was its foundation and its head.

Without anyone needing to take the lead, everyone including me rose from their seats and clasped their hands toward Mae Jonghak.

Dozens of people spoke at once, but the voices that followed sounded as if they belonged to a single person.

“We greet the Alliance Leader.”

No one held back—not even Jeok Cheongang and Cheongpung, who were seated on either side of me. They all adopted solemn expressions and paid their respects.

Mae Jonghak watched them with a faint smile, nodded, and turned away.

Then, the next moment, the martial artists numbering in the thousands—or perhaps ten thousand—heard it clearly.

The giant’s voice shook heaven and earth.

“Peace is over.”

“……!”

The air surrounding us burst apart.

The towering trees trembled, and the bodies of the heroes gathered below the platform stiffened like statues.

As Mae Jonghak continued speaking with unprecedented internal energy behind his words, there was no trace left of the eccentric figure we had seen until now.

“The war has already begun, and another hundred thousand Demonic Path fighters are approaching the Central Plains.”

There might have been people who had never experienced the Great Faction War, but there was no one who knew nothing of that terrible conflict.

Fear and anger clouded the eyes of the elderly martial artists, while the young martial artists trembled with an inexplicable shiver.

“Dharma King Hong Dao.”

At Mae Jonghak’s next words, the monks of Shaolin softly murmured Buddhist invocations.

“Poison King Tang Taesang and the Heaven-Shaking Venerable Nun of Emei.”

Tang Sadok, the Myriad-Poison Asura, had traveled a long way despite his ailing body, and his green eyes gleamed. The nuns of Emei Sect shed tears.

“The blood that began flowing from Shanxi Province continued into Henan and reached Sichuan and Hubei.”

Countless lives had been lost in little more than a year.

The old martial artists praised by everyone and the young people who were still mere greenhorns alike had fallen before they could ever bloom.

*Eight Spring Gorge.*

The memory still came to me whenever I closed my eyes.

How many people had died in that narrow gorge in Shanxi Province?

Who were the people who had fallen in Henan, Sichuan, and Hubei?

I did not know their names or the dreams they had held in life.

But I knew what they had taken up their swords to protect.

*Something precious.*

Boom!

An unprecedented aura burst from Mae Jonghak’s entire body.

Purple energy rooted in the Zaha Divine Technique rolled over his shoulders like waves.

“Take up your weapons and fight back.”

It was not only his manner of speaking and his aura that had changed.

The Mae Jonghak of this moment was not merely the Sword Saint or the Number One Sword Under Heaven. He was the Alliance Leader guiding everyone.

“For the sake of the families who share our blood. For the sake of the Senior Brothers and fellow disciples, and the sects with which we have shared joy and hardship. And…”

A mighty cry erupted from between Mae Jonghak’s lips.

“To protect this Murim where we live, take up your weapons!”

The giant roared. A shiver rose along my spine.

The martial artists filling every direction exhaled the breaths they had been holding and let out a thunderous cheer.

“Waaaaaah!”

“For the annihilation of the Demonic Path!”

Shhk, chakachachang!

The world was flooded with light. Countless weapons flashed as they caught the sunlight pouring down overhead.

“Waaaaaah!”

“For justice and chivalry!”

Shhk, chakachachang!

The world was flooded with light. Countless weapons flashed as they caught the sunlight pouring down overhead.

As Mae Jonghak stared at the dazzling and magnificent sight, he reached down and grasped the enormous flag lying at his feet.

Murim Alliance.

Those three characters had been written across the flag in a vigorous, flying script. Once he raised it, a new era would begin.

But the next thing Mae Jonghak did was beyond everyone’s expectations.

“Great Hero Jeok. Would you help me?”

“……!”

I could feel the crowd’s agitation against my skin. Jeok Cheongang, who had been silently staring at Mae Jonghak, suddenly spoke.

“Is the flag heavy?”

“It seems to be, for now.”

“That flag feels heavy even to this old man. And the more hands, the better.”

The next moment, I realized what I needed to do.

At Jeok Cheongang’s signal, Cheongpung and I stepped forward and grabbed the flag at the same time.

Then we pulled it upright with all our strength.

The Murim Alliance had been born.
```

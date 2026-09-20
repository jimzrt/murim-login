<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0520.txt",
      "sha256": "9d7df1598b52f63e5476c9e98671da0c3840a98743adbda1012f388fdf69aceb",
      "bytes": 13177
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "dc42952de53f3e8479766d6b9118acdc7bbebd99961bdea79a469be4eae561db",
      "bytes": 4434
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "67498904092521751ef5e7d6014f574e72068fa839b5658d2fea121c1177f46c",
      "bytes": 166038
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "ea44c90a991aa9310d65c37d7b45a171d0dd0db932930e335b4157dcd661fa03",
      "bytes": 553
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "9cf2f50bd4c8ce3d5597359def6bdc2afc5b650daf1252d62b01aa68053c2936",
      "bytes": 1630
    },
    {
      "path": "characters/Jongni Chu.md",
      "sha256": "ab3e9f38d39496ac4951c21ffb20a192e714b05c4c00d08d9a13db7c1564eb9a",
      "bytes": 1451
    },
    {
      "path": "characters/Mae Jonghak.md",
      "sha256": "6c4144b1eb8ae2c8a3f55760e75294631f84173d5b2500cc1864e1158aa388fa",
      "bytes": 1477
    },
    {
      "path": "characters/Shadow Killer.md",
      "sha256": "d5bc0dc806c0a5245b93f22851ac2b3445f962640ad825d6fcd6cfc07b2cb43e",
      "bytes": 784
    },
    {
      "path": "characters/Song Ho.md",
      "sha256": "a3e74b0d7f5b5f8e6ffa75e0754ea6800825cee76c08a6312844d5a73c3b5e99",
      "bytes": 1866
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "5356e51fec07036e7c668c604cc568d18828de713411c12c4c7ec1f04b91c1a8",
      "bytes": 157165
    }
  ],
  "estimated_tokens": 11922
}
-->

# Durable State Update — Chapter 520

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 520. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 520. Profile updates may replace only one
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
  "chapter": 520,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 520,
    "continuity_sources": [520],
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
    "Jeok Cheongang's Heart Demon and the dark memories binding him have been expelled; he has entered a new realm, achieved Returned to Youth, and begun his long-promised duel with Nangong Cheon, the Azure Sky Sword King.",
    "Mungyeong is the Slaughter Saint and former Divine Physician, a Returned to Youth Supreme Peak master and the greatest assassin in history; Mu Song and five Water Dragon Stronghold subordinates know he is exceptionally powerful but not that he is the Slaughter Saint.",
    "Mungyeong is training Taekyung to refine the stability and precision of the violent internal energy produced by the Fire Gate Divine Technique through Rising on Duckweed, Crossing Water.",
    "Zhuge Feng's Demon-Sealing Formation blocks all mana from the exposed Gate by drawing in natural qi, but whether it is permanent and repeatable remains unresolved.",
    "Jang Taebo is the Jin Family of Taiyuan's Master of Ironcraft Hall and is summoning renowned artisans to process the Water God Dragon's remains.",
    "The New Murim Alliance has been publicly announced from Mount Song, and major orthodox and unorthodox factions, eccentric experts, distant great families, and uncertain allied factions are gathering in Henan.",
    "The Southern Heaven Demon Empress is traveling toward Yunnan and expects to cause further deaths.",
    "Jin Mukyung remains secluded in the training hall after losing to Cheongpung, refusing to emerge until he achieves a great accomplishment.",
    "Unnamed, Hong Dao's practical Disciple, endured three months in Repentance Cave, achieved enlightenment, received Shaolin's Great Restoration Pill, and is now a scarred Supreme Peak master and Jung Ho's young Martial Uncle; Shaolin's new Abbot wants to meet Taekyung.",
    "The Black Dragon Demon Gate is an ancient unorthodox faction that once belonged to the Demonic Cult's Twelve Branches and now ranks among the Central Plains' strongest unorthodox powers.",
    "Jin Taekyung completed Stage 2 of Fake Murim Practitioner, achieved Single Reed Crossing the River, improved his internal-energy control and attributes, gained 50 bonus points and substantial EXP, and leveled up.",
    "The Dark Heaven assault near Mount Song has ended in a chaotic misunderstanding: Jeok Cheongang emerged from a burning inn, was mistaken for a Dark Heaven fiend, was identified as the Returned-to-Youth Fire King by Peng Cheolhu, and was separated from the mob by Nangong Cheon."
  ],
  "continuity_sources": [
    519,
    518
  ],
  "open_questions": [
    "Will the Demon-Sealing Formation remain effective permanently, and can equivalent formations be installed repeatedly if more Gates appear?",
    "What is the Lord of Heaven's identity, and how is he connected to the dangerous force Taekyung associates with his original world?",
    "Where is the Southern Heaven Demon Empress ultimately headed, and what does she intend to do in Yunnan?",
    "What is the outcome of the duel between Jeok Cheongang and Nangong Cheon, the Azure Sky Sword King?"
  ],
  "safe_through": 519,
  "temporary_decisions": [
    "Render 새외무림 as Outer Murim, 새외 as Outer Lands, 북해빙궁 as North Sea Ice Palace, 야수묘왕 as Beast Miao King, and retain Nanman Beast Palace for 남만야수궁.",
    "Render 소뢰음사 as Small Thunderclap Temple, 광풍사 as Mad Wind Society, 포달랍궁 as Potala Palace, 오독문 as Five Poisons Sect, 독곡 as Poison Valley, 천축 as India, 갠지스강 as Ganges River, and 대환단 as Great Restoration Pill.",
    "Render 파사국 as Persia, 회교도 as Muslims, 영웅건 as hero headband, 대막 as great desert, 귀염권 as Ghost Flame Fist, and 장성 as Great Wall.",
    "Retain sa-eo for 사어, shark for 상어, Old Master for 노야, this old man/I for 노부, Shark Water-Ski Team for 수상스키단, and swift ship for 쾌조선.",
    "Render 정호 as Jung Ho, 사마표 as Sama Pyo, 흑룡도 as Black Dragon Saber, 대초자곤 as two-section staff, 시주 as Benefactor, 계율원주 as Discipline Hall Master, 십이지파 as Twelve Branches of the Demonic Cult, 모용세가 as Murong Family, 요녕 as Liaoning, 진돗개 하나 as Jindotgae One, 소하문 as Xiao He Gate, 장충도 as Long Serpent Saber, 방가 as Fang Family, 월미도 as Moon Beauty Saber, and 검기상인 as the level of injuring others with Sword Energy."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 적천강    | **Jeok Cheongang** |
| 매종학    | **Mae Jonghak**    |
| 검성     | **Sword Saint**               | Mae Jonghak    |
| 무신     | **Martial God**               | —              |
| 궁성     | **Bow Saint**                 | —              |
| 살성     | **Slaughter Saint**           | —              |
| 삼성     | **Three Saints**    |
| 십왕     | **Ten Kings**       |
| 화산파    | **Huashan**                      |
| 곤륜파    | **Kunlun Sect**                  |
| 무림맹    | **Murim Alliance**               |
| 암천     | **Dark Heaven**                  |
| 남만야수궁  | **Nanman Beast Palace**          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 영약     | **elixir**                                       |                                                       |
| 마적     | **mounted bandits**                              |                                                       |
| 가주     | **Family Head**                              |
| 명성               | **Fame**                       |
| 사천     | **Sichuan**            |
| 청해     | **Qinghai**            |
| 화산     | **Huashan**            |
| 곤륜     | **Kunlun**             |
| 정마대전   | **Great Faction War**         |
| 노부      | **this old man / I**                                            |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 도사      | **Daoist**                                                      |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 종리추 | **Jongni Chu** | Young Peak martial artist from Yunnan; conceals his sect. |
| 암중살 | **Shadow Killer** | The Hidden Shadow Pavilion's finest agent. |
| 송호 | **Song Ho** | Elderly martial artist known as the Thousand-Faced Fox. |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 전서구 | **messenger pigeon** | Pigeon delivering the Lower District Sect's Jeongyang Branch report. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 오대세가 | **Five Great Families** | Major Murim grouping. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 성라대연 | **Star-Array Grand Banquet** | Major martial gathering held in Henan every two or three years. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 천면호리 | **Thousand-Faced Fox** | Epithet of Song Ho. |
| 상승검 | **Always-Victorious Sword** | Jongni Chu's self-styled epithet, coined in this chapter. |
| 은영각 | **Hidden Shadow Pavilion** | Former Murim Alliance intelligence organization. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 당문 | **Tang Clan** | Short form for the Sichuan Tang Clan. |
| 내당 | **Inner Hall** | The Tang Clan's inner hall area. |
| 오대 | **Five Squads** | Named Tang Clan organizational group in Tang Sadok's mobilization order. |
| 마두 | **fiend** | Demonic martial masters from the Great Faction War era. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 무릉도원 | **Wuling Peach Blossom Spring** | Classical image of an idyllic utopia where immortals are said to live. |
| 살귀 | **Killing Ghost** | Mungyeong's earlier sobriquet before he became the Slaughter Saint. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 송호 | 청년 | elderly_martial_artist_to_younger_martial_artist | Young Hero | formal-polite | Song Ho calls out to the young man as 소협 at the chapter's end. |
| 적천강 | 종리추 | legendary_master_to_suspicious_rival | you / tongue-cut bastard | grave and threatening | Questions Jongni Chu about Tianshan and threatens him over harm to Taekyung or Cheongpung. |
| 종리추 | 적천강 | suspicious_rival_to_legendary_master | you | polite and taunting | Refuses to answer Jeok Cheongang directly and hints at the danger to his Disciple. |
| 종리추 | 송호 | old_acquaintances; former_savior_and_survivor | Thousand-Faced Fox Song Ho; you | casual-familiar | Mae Jonghak addresses Song Ho informally, asks about his prosthetic leg, and recalls that Song would be the first to recognize him. |
| 매종학 | 송호 | savior_to_survivor | you | casual-familiar | Mae uses 자네 while speaking to Song Ho after his identity is recognized. |
| 송호 | 매종학 | rescued_survivor_to_savior | Great Hero; you | formal-deferential and familiar | Song Ho credits Mae with saving his life and addresses him as 대협. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 519
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 519
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, and Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Jongni Chu.md

# Jongni Chu (종리추)

- **Safe through:** Chapter 268
- **Aliases:** Always-Victorious Sword; Life-Sustaining Sword
- **Role:** Sword Saint Mae Jonghak, Cheongpung's grandfather, who traveled for a year under the young identity Jongni Chu after Returning to Youth; while using Jongni Chu's identity, he concealed his Supreme Peak realm through Returning to Simplicity, coined Always-Victorious Sword, fought through the Star-Array Grand Banquet, attacked Cheongpung in the semifinal, and left the final after forcing Jin Taekyung out of bounds; he revealed himself at Mount Song, protected Cheongpung from the Blood Lord with the divine Thirty-Six Plum Blossom Swords, treated Jeok Cheongang and Cheongpung after the Blood Lord escaped, and confirmed his identity to Jin Taekyung and Song Ho.
- **Personality:** Approachable, eccentric, relentlessly positive, and unusually eager to form friendships; treats even severe verbal abuse as proof of genuine friendship.
- **Voice:** Friendly, casually familiar, cheerful, and shamelessly persistent.
- **Relationships:** Immediately declares Jin Taekyung his friend after meeting him, follows him through Henan, and travels with Taekyung and the other finalists toward Luoyang after passing the preliminaries; he also immediately befriends the disguised Cheongpung and overwhelms a masked Hidden Shadow Pavilion agent who attacks him.

### Mae Jonghak.md

# Mae Jonghak (매종학)

- **Safe through:** Chapter 515
- **Aliases:** Sword Saint
- **Role:** Sword Saint and Cheongpung's grandfather; more than forty years ago he sought Jeok Cheongang's help against the Demonic Cult, fought Jeok at Mount Jiuhua for seven days and seven nights, and drew with him; after the Great Faction War ended, he devoted himself to martial arts, reached Great Completion, attained higher enlightenment after encountering another wall, unexpectedly Returned to Youth, and traveled the world for a year under the name Jongni Chu while concealing his identity; at Mount Song he protected Cheongpung and attacked the Blood Lord with the divine Thirty-Six Plum Blossom Swords; after the Blood Lord escaped, he confirmed his identity to Jin Taekyung and Song Ho, and Song Ho identified Mae as the Great Hero who had saved his life.
- **Personality:** Not established in this chapter.
- **Voice:** Not established in this chapter.
- **Relationships:** Cheongpung's grandfather and martial instructor; taught him the Taeeul Miri Palm; secretly entered Huashan while its Sect Leader slept, left a dagger and handwritten note, and then went into hiding, prompting Huashan's search; fought Jeok Cheongang at Mount Jiuhua more than forty years ago and left after their draw; his old friend Hong Dao left him a letter identifying Jin Taekyung as the Morning Star who would drive away darkness.

### Shadow Killer.md

# Shadow Killer (암중살)

- **Safe through:** Chapter 267
- **Aliases:** None
- **Role:** The Hidden Shadow Pavilion's finest agent, a masked operative who completed hundreds of missions and served the Thousand-Faced Fox loyally for decades; he was incapacitated by Jongni Chu after attacking him, and contact with him was lost three days before this chapter.
- **Personality:** Disciplined and loyal; when captured, he attempted to bite a poison pellet rather than reveal information.
- **Voice:** His internal narration is terse and grim; his sustained spoken voice is not established before he is incapacitated.
- **Relationships:** Song Ho, the Thousand-Faced Fox, is his superior, whom he served for decades.

### Song Ho.md

# Song Ho (송호)

- **Safe through:** Chapter 482
- **Aliases:** Thousand-Faced Fox
- **Role:** Elderly Peak master known as the Thousand-Faced Fox; he has a wooden prosthetic leg and overwhelming physical strength, was formerly the head of the Murim Alliance's Hidden Shadow Pavilion, and, after Hong Dao sought him out over Dark Heaven, recalled his former subordinates and helped restore the Hidden Shadow Pavilion; he is an intelligence operative and master of disguise who can identify people through their faces, habits, and bone structure; he lost his leg during the final battle against the Demonic Cult decades ago and suffers recurring pain from the old injury; he suspects he previously encountered Jongni Chu and is now investigating him; he attends the Star-Array Grand Banquet's main-event duels every day before leaving during the third day; he now recognizes that Jongni Chu is closely connected to the day his leg was severed and that the connection is not mere coincidence; after receiving a report that Shadow Killer had been found, he sent agents to secure the dueling platform and went there himself when he sensed the clash between Supreme Peak masters; after arriving at Mount Song with hundreds of martial artists, he recognized Jongni Chu as Sword Saint Mae Jonghak and confirmed that Mae had saved his life in the past.
- **Personality:** Outwardly genial and relaxed, but observant, forceful, and intimidating when pursuing information.
- **Voice:** Lightly genial and conversational, turning quietly coercive during interrogation.
- **Relationships:** Takes the Geumwa Merchant Group's merchants away to question them about the young martial artist who drank their Yeoahong; recognizes Jin Taekyung as Jeok Cheongang's Disciple and praises his preliminary performance.

## Korean source

```text
＃520화



청년은 멍하니 창밖을 바라보았다.

참으로 좋은 봄날이었다.

햇빛은 적당하고, 반쯤 열어 둔 창문 사이로 불어오는 산들바람은 선선하다. 어느덧 활짝 만개한 꽃들로부터 풍겨 오는 향긋한 내음까지.

그야말로 인세의 무릉도원(武陵桃源)이라 부를 만했다.

다음 순간 등 뒤에서 불쑥 들려온 누군가의 목소리만 아니었다면, 모든 것이 완벽했을 것이다.

“좋은 날입니다.”

청년은 놀라지 않았다. 이미 가까워지는 기척을 느낀 지 오래였기 때문이다.

그리고 그것은 방금 들려 온 목소리의 주인에게만 해당하는 것이 아니었다.

전후좌우. 위, 아래 어디든.

청년은 주위에서 일어나는 모든 일을 파악하고 받아들였다.

어떤 필요나 스스로의 의지로 행하는 것이 아니라, 그저 숨 쉬듯이 자연스러운 일이었다.

‘야속한 일이지. 봄 풍경도 제대로 즐길 수 없게 되었으니.’

내심 중얼거린 청년이 돌아섰다. 젊은이처럼 풍채가 당당한 노인이 빙그레 웃으며 그를 바라보고 있었다.

“혹시나 하는 노파심에 잠시 들렀더니…… 농땡이를 피우고 계셨군요.”

듣는 것만으로도 연륜이 느껴지는 늙수그레한 목소리.

할아비가 어린 손주를 대하듯 부드러운 어조였지만, 청년은 지금까지의 경험을 통해 잘 알고 있었다.

지금 마주하고 있는 노인에게는 매우 은밀하고도 시퍼렇게 날이 선 칼날이 숨어져 있다는 것을.

“무슨 생각을 그리 하십니까?”

“당신의 적이 내가 아니라서 다행이라는 생각을 잠깐 했소.”

청년의 대답에 노인이 나직한 웃음을 흘렸다.

“누가 들으면 제가 무서운 사람인 줄 알겠습니다, 그려.”

저 사람 좋은 웃음에 속아 넘어가면 안 된다.

저 웃고 있는 얼굴과 머릿속에 얼마나 많은 심모원려(深謀遠慮)가 도사리고 있는지는 아무도 모르니까.

정마대전이라는 격변의 시기, 천하의 정세를 손바닥 보듯 꿰뚫고 숱한 마두를 제거한 무림맹 은영각(隱影閣)의 우두머리가 평범한 인물일 리 없었다.

“다른 사람들은 전혀 그 말에 동의하지 않을 거요, 천면호리(千面狐狸).”

천면호리 송호.

천 개의 얼굴을 가졌다는 은영각의 늙은 여우는 청년의 말에 어깨를 으쓱해 보였다.

“물론 이 늙은이가 두려운 사람도 있기는 하겠지요. 하지만 지금 제 앞에 계신 분께는 해당하지 않는 말 같습니다만.”

“내가 말이오?”

“아닙니까?”

한동안 골똘히 생각에 잠겨 있던 청년이 문득 눈을 동그랗게 떴다.

“어, 그러네.”

“그렇지요?”

“그대의 말이 맞는 것 같소. 다시 생각해 보니 별로 두렵지는 않구려.”

자존심에 목숨을 거는 무림인들이라면 벌써 칼부림이 일어나고도 남았을 대화.

하지만 지금 마주하고 있는 두 사람은 평범이라는 범주에 속하지 않은 인물들이었다.

천면호리 송호의 기분이 조금도 상하지 않은 것에는 상대의 정체도 큰 부분을 차지했다.

“주위를 경계하되, 누구도 두려워하시지 마십시오. 무림맹주(武林盟主)라면 언제나 그리해야 합니다.”

청년, 검성(劍星) 매종학이 떨떠름한 표정으로 대답했다.

“그, 맹주라는 말은 가급적 안 해 줬으면 좋겠는데.”

“이제는 받아들이셔야지요.”

“도무지 익숙해지지 않아서 그렇소.”

“하지만 곧 맹주가 되시지 않습니까.”

“아직은 아니잖소.”

“회초리도 먼저 맞는 게 낫다고 했습니다.”

“늘 의문이었소. 그 회초리를 왜 내가 맞아야 하는지.”

천면호리의 대답은 간결했다.

“무신(武神)께서 없으시니까요.”

무신이라는 별호는 한때 완전무결함을 뜻했다. 아니, 한때가 아니라 지금까지도 마찬가지다.

그를 한 번이라도 마주한 이들은 입을 모아 칭송했고, 기나긴 세월이 흐른 뒤에도 그 거대하고도 찬란한 명성은 천하를 밝히고 있었다.

하지만…….

“그분을 찾을 수 없었습니다.”

무신은 사라졌다. 죽었는지 살았는지, 무엇 때문에 자취를 감추었는지 그 누구도 알지 못했다.

과거 무림맹이 남아 있던 시절. 천면호리는 은영각의 정보망을 총동원하여 천하를 그물질했지만, 그 어디에서도 무신의 흔적을 찾을 수 없었다.

폭풍우가 치던 날 잠시 내리쬐었던 햇볕처럼, 찰나의 순간 밤하늘을 스쳐 지나간 유성처럼.

무신은 그렇게 사라졌다. 하늘이 되어 버린 자신의 별호를 천하에 드리운 채.

“그분께서 자리에 안 계신 이상, 맹주 직을 맡으실 분은 매종학 대협이 유일합니다.”

“허, 나 말고도 적임자는 얼마든지 있을 텐데.”

“또 다른 삼성(三星)과 십왕(十王)을 염두에 두고 하신 말씀이라면, 못 들은 것으로 하겠습니다.”

“아니, 어째서?”

“우선 궁성(弓星)께서는 행적이 묘연합니다.”

“은영각에서 계속 찾고 있지 않소?”

“그걸 암천이 기다려 준답니까? 전서구 띄울까요? 궁성을 찾고 있는데 좀 기다려 달라고?”

“어, 듣고 보니 그러네.”

“…….”

천면호리는 매종학의 머리통을 내리치고 싶은 충동을 참으며 입을 열었다.

“그리고 아무래도 성격적인 면모가, 아시다시피 좀 그렇지 않습니까.”

“난 화끈해서 좋았소만.”

“화끈하게 무림맹 말아먹으면 다른 사람들이 안 좋아할 겁니다.”

“으음. 그런가.”

“그리고 살성(殺星)께서는…… 말해 봤자 입만 아픕니다.”

“그 친구가 의외로 적임자일지도 모르오. 무공도 무공이지만 위압감이 대단했지. 통솔력이 있어 보였소.”

“사람들이 잘 따르긴 할 겁니다. 안 따르는 사람들은 이미 죽어 있을 테니까요.”

“그, 사람을 너무 살귀로 보는 것 아니오?”

“별호부터가 살성인데 제게 뭘 바라시는 겁니까.”

“그것도 그러네.”

진짜 한 대 때릴까.

그런 눈빛으로 매종학을 바라보던 천면호리가 한숨을 내쉬었다.

“십왕에 속하신 다른 분들도 비슷한 이유입니다. 이미 돌아가셨거나, 혹은 또 다른 여러 가지 이유로 맹주 직에 적합하지 않으신 분들이지요.”

무림맹주는 무공만 강하다고 해서 되는 것이 아니다.

중요한 결정을 내릴 수 있는 결단력도 필요하고, 다른 이들을 끌고 갈 만한 인덕과 포용력 역시 요구된다.

그런 의미에서 검성 매종학은 무신의 유일한 대체자였다.

“대협께서는 구파일방, 오대세가의 영수(領袖)들의 인정을 받은 분이십니다. 성정이 바르고 공명정대하여 사문인 화산파라 한들 특별히 우대하지 않고, 남의 말에 귀 기울이시니 맹주의 자격이 충분하다 할 수 있지요.”

신 무림맹의 태동과 더불어 은영각이 공식적으로 부활하고 천면호리 역시 과거의 위상을 되찾았지만, 무림맹주는 그 한 사람의 지지로만 올라갈 수 있는 자리가 아니다.

만인(萬人)의 인정을 받은 자. 무공뿐만 아니라 지도자로서의 면모를 갖춘 자만이 맹주의 자리에 오른다.

‘물론, 반대하는 목소리가 아주 없었던 것은 아니지만.’

뒤이어 떠오르는 생각을 흩어버린 천면호리가 문득 인상을 굳혔다.

“한데, 그런 분께서 한가롭게 봄날 정취나 즐기고 계시다니요.”

매종학이 아쉬운 표정으로 창가를 곁눈질하며 대답했다.

“그저 날이 좋아서 잠시 창밖을 보고 있었을 뿐이오.”

“아니, 지금 밀려 있는 사안이 얼마나 많은데…….”

“아, 맞다. 가져가시오. 한 곳에다 전부 모아뒀으니.”

한바탕 갈구려던 천면호리가 멈칫했다.

“그게 무슨 말씀이십니까?”

“아까 은영각에서 들여온 죽간들 말이오. 정확히는 일흔여덟 개의 안건이지. 전부 처리했소.”

“……?”

처리했다고? 그 많은 안건을 이렇게 짧은 시간 동안?

집무실 한구석, 산더미처럼 쌓인 죽간들을 말없이 바라보던 천면호리가 문득 눈을 가늘게 떴다.

“저 중에서 청해(靑海)에서 온 서신을 보셨습니까?”

“곤륜파 말이오? 물론 봤소. 산적과 마적 떼들을 진압하고 오느라 시일이 촉박하다더군. 때에 맞춰 도착하면 좋겠지만, 조금 늦어도 별 상관은 없을 거요.”

“하면 사천(四川) 쪽의 소식도?”

“모두가 합심하여 당문 재건에 박차를 가하고 있다고 적혀 있더군. 아, 내당(內堂)에 일러 약효가 뛰어난 영약을 준비하라 하시오. 당 가주의 병세가 좋지 않다고 들었는데, 대대적인 원조를 떠나 우선 이렇게라도 도움을 주어야지.”

“그럼 남만야수궁(南蠻野獸宮)에서 도착한 서신은…….”

“그런 게 있었소? 오늘 올라온 안건 중 남만야수궁 관련해서는 일절 못 보았는데.”

그럴 수밖에 없었다. 매종학의 말처럼, 오늘 올려보낸 안건 중에서 남만야수궁에 관련된 내용이 포함된 것은 하나도 없었으니까.

그제야 줄곧 반신반의하던 천면호리의 입가에 은은한 웃음이 맺혔다.

“응? 왜 그러시오?”

“아무것도 아닙니다. 그저 직무에 충실하신 모습이 보기 좋…….”

“너무 그리 음흉하게 웃지 마시오. 다른 사람이 보면 질겁할지도 모르오.”

“…….”

“그나저나 바람이 좋구려. 참으로 좋은 날씨요.”

천면호리의 기분을 잡쳐 놓고 창밖만 하염없이 바라보던 매종학이 불쑥 입을 열었다.

“함께 밖으로 나가 거닐지 않겠소? 이런 날도 오늘로 마지막일지도 모르는데.”

“저는 싫습니다.”

퉁명스럽게 대답한 천면호리가 말을 이었다.

“곧장 다른 안건을 올려보낼 터이니, 맹주께서도 허튼짓하지 마시고 일이나 하십시오.”

“그래도 귀한 객이 오고 있는데, 사람 된 도리로 마중은 나가야지.”

“마중이라고 하셨습니까?”

순간 멈칫한 천면호리가 의족(義足)을 절뚝거리며 창가로 다가갔다.

“저곳을 보시오.”

“……!”

성벽 너머, 서서히 가까워지는 어떤 물체.

상당한 거리가 있는 탓에 흐릿했지만, 공력을 집중하자 저것이 마차라는 것 정도는 쉽게 알아볼 수 있었다.

문제는 왜 저 사두마차의 마부석에 낯익은 얼굴이 앉아 있느냐다.

‘아니, 암중살(暗中殺)이 왜 저기에 있어.’

암중살은 은영각 내에서도 손가락에 꼽히는 정예 요원이다.

성라대연 때는 정체를 숨긴 매종학의 행적을 밟았던 전적이 있고, 과거 정마대전 당시에는 숱한 마두의 목을 취했다.

“아는 얼굴 같구려. 그렇지 않소?”

“맞습니다. 대로변에서 일이 벌어졌다 하여 암중살을 보냈는데…….”

잡으라고 보낸 놈이 모셔오고 있네.

뒷말을 삼키는 천면호리의 귓가에 매종학의 목소리가 닿았다.

“그대가 잠시 자리를 비운 틈에 급보가 왔었소.”

“급보라고 하셨습니까?”

“그렇소. 반가운 얼굴들이 오고 있다는 소식이었지.”

천면호리의 어깨를 툭툭 친 매종학이 창밖으로 몸을 내밀며 중얼거렸다.

“자, 가 봅시다.”



* * *



“환영하오.”

무림맹 내성(內城)으로 진입한 마차가 멈추고, 내리기가 무섭게 들려온 목소리는 제법 귀에 익었다.

‘검성 매종학.’

한때는 상승검 종리추라는 이름으로 알고 있던 그가 나를 발견하고 피식 웃는다.

“잘 지냈나, 친구.”

“…….”

저 컨셉 오래가네.

매종학은 내가 고개를 꾸벅 숙여 보이자 아쉽다는 듯 입맛을 다신 뒤, 이번에는 적천강을 향해 말을 건넸다.

“건강해 보여서 다행이오.”

하품을 쩍쩍하며 주위를 둘러보던 적천강이 미간을 좁혔다.

“노부에게 한 말인가?”

“실로 오랜만이구려. 다시 만나 반갑소.”

“사람 잘못 본 모양이군. 노부는 대가리에 피도 안 마른 놈과는 별다른 인연이…….”

말을 이으려던 적천강이 멈칫한다. 매종학을 위아래로 훑어보던 그의 눈동자가 커졌다.

“설마, 당신?”

“맞소. 나요.”

매종학이 활짝 웃으며 말을 이었다.

“반가운 김에 하는 말인데, 맹주 하실 생각 있소?”

“……?”

“……?”

이게 무림식 조별과제 조장 정하기냐.
```

## Final English reading copy

```markdown
# Chapter 520

The young man gazed blankly out the window.

It was a truly beautiful spring day.

The sunlight was just right, and the breeze drifting through the half-open window was pleasantly cool. Even the flowers, now in full bloom, filled the air with a sweet fragrance.

It was nothing short of a Wuling Peach Blossom Spring in the mortal world.[^1]

Everything would have been perfect if not for the voice that suddenly came from behind him.

“It’s a beautiful day.”

The young man did not startle. He had sensed the approaching presence a long time ago.

And that was not limited to the owner of the voice he had just heard.

Front, back, left, right. Above and below.

The young man perceived and accepted everything happening around him.

It was not something he did out of necessity or conscious will. It came as naturally as breathing.

*How frustrating. I can’t even enjoy the spring scenery properly anymore.*

After muttering inwardly, the young man turned around.

An old man with the imposing bearing of a young man was looking at him with a genial smile.

“I stopped by for a moment out of an old man’s needless concern, only to find you slacking off.”

The old man’s voice was aged enough to convey his years at a single hearing.

His tone was gentle, like a grandfather speaking to his young grandson, but the young man knew from experience that the old man standing before him concealed an extremely stealthy, razor-sharp blade.

“What are you thinking about so intently?”

“I was briefly thinking how fortunate it is that I am not your enemy.”

The old man gave a low chuckle.

“If anyone heard that, they might think I was a frightening man.”

He could not afford to be fooled by that good-natured laugh.

No one knew how many deep schemes and long-term plans lurked behind that smiling face and inside that head.

During the upheaval of the Great Faction War, the leader of the Murim Alliance’s Hidden Shadow Pavilion had seen through the situation across the world as easily as his own palm and eliminated countless fiends. There was no way he could be an ordinary man.

“Other people would never agree with you, Thousand-Faced Fox.”

Thousand-Faced Fox Song Ho.

The old fox of the Hidden Shadow Pavilion, said to possess a thousand faces, shrugged at the young man’s words.

“Of course, there are people who fear this old man. But I do not believe that applies to the person standing before me.”

“Me?”

“Does it not?”

The young man fell into deep thought for a while, then suddenly opened his eyes wide.

“Oh. You’re right.”

“Isn’t it?”

“I suppose you are right. Now that I think about it, you aren’t particularly frightening.”

If ordinary Murim practitioners who staked their lives on their pride had exchanged those words, blades would have been drawn long ago.

But the two men facing each other did not belong to the category of ordinary people.

The reason Thousand-Faced Fox Song Ho was not offended in the slightest had a great deal to do with the identity of the person before him.

“Be wary of your surroundings, but fear no one. That is what an Alliance Leader must always do.”

The young man—Sword Saint Mae Jonghak—answered with a sour expression.

“I’d prefer it if you didn’t call me Alliance Leader whenever possible.”

“You must accept it now.”

“I simply haven’t gotten used to it.”

“But you will soon become the Alliance Leader.”

“Not yet.”

“They say it is better to take the whipping sooner rather than later.”

“I’ve always wondered why I have to be the one taking that whipping.”

Thousand-Faced Fox’s answer was concise.

“Because the Martial God is not here.”

The title Martial God had once meant perfection. No—not once. It still meant the same thing.

Everyone who had met him even once had praised him in unison, and even after the passage of many long years, that vast and brilliant Fame still illuminated the world.

But…

“We could not find him.”

The Martial God had disappeared. No one knew whether he was alive or dead, or what had caused him to vanish without a trace.

Back when the Murim Alliance still existed, Thousand-Faced Fox had mobilized the Hidden Shadow Pavilion’s entire intelligence network to scour the world. Yet he had found no trace of the Martial God anywhere.

Like sunlight that shone down only briefly during a raging storm. Like a meteor that streaked across the night sky for a fleeting instant.

The Martial God had disappeared like that, leaving his own title—which had become the heavens—spread across the world.

“As long as he is not present, Great Hero Mae Jonghak is the only person who can take up the position of Alliance Leader.”

“Hah. There must be plenty of other suitable candidates besides me.”

“If you are referring to the other members of the Three Saints and the Ten Kings, I will pretend I did not hear that.”

“No, why?”

“For one thing, the Bow Saint’s whereabouts are unknown.”

“Isn’t the Hidden Shadow Pavilion still looking for him?”

“Do you think Dark Heaven will wait for us? Should I send a messenger pigeon saying, ‘We are looking for the Bow Saint, so please wait a little longer’?”

“Oh. Now that you mention it, I suppose not.”

“…”

Thousand-Faced Fox held back the urge to bring his fist down on Mae Jonghak’s head and continued.

“And, as you know, his personality is somewhat…”

“I liked him because he was so fiery.”

“If he runs the Murim Alliance into the ground with that fiery personality, other people will not be pleased.”

“Hmm. Is that so?”

“And the Slaughter Saint… There is no point talking about him.”

“That fellow might be more suitable than you think. His martial arts are one thing, but his presence was overwhelming. He seemed to have the ability to command others.”

“People would certainly follow him. Anyone who refused would already be dead.”

“Are you viewing him a little too much as a Killing Ghost?”

“His title is the Slaughter Saint. What exactly do you expect from me?”

“That is true, too.”

Should I really hit him?

Thousand-Faced Fox looked at Mae Jonghak with exactly that thought in his eyes, then sighed.

“The other members of the Ten Kings are unsuitable for similar reasons. Some have already passed away, while others are unfit for the position of Alliance Leader for one reason or another.”

The Alliance Leader could not be someone who was merely strong in martial arts.

He needed the decisiveness to make important choices, as well as the virtue and magnanimity to lead and embrace others.

In that regard, Sword Saint Mae Jonghak was the Martial God’s only true replacement.

“Great Hero, you have received the recognition of the leaders of the Nine Sects and One Gang and the Five Great Families. Your character is upright and fair. You do not give special treatment even to your own sect, Huashan, and you listen to what others have to say. You are more than qualified to become Alliance Leader.”

Along with the birth of the New Murim Alliance, the Hidden Shadow Pavilion had officially been resurrected, and Thousand-Faced Fox had regained his former status. But the position of Alliance Leader was not something one could obtain through a single person’s support.

Only someone recognized by all and possessing the qualities of a leader as well as exceptional martial arts could rise to the position of Alliance Leader.

*Of course, there had been no shortage of voices in opposition.*

Thousand-Faced Fox scattered the thought that had just come to mind and suddenly hardened his expression.

“And yet someone like you is leisurely enjoying the spring weather.”

Mae Jonghak glanced at the window with a regretful expression.

“The weather was nice, so I was only looking outside for a moment.”

“There are so many matters waiting for you right now…”

“Oh, that’s right. Take them with you. I put them all together in one place.”

Thousand-Faced Fox, who had been preparing to give him a thorough scolding, stopped short.

“What do you mean?”

“The bamboo slips brought in from the Hidden Shadow Pavilion earlier. More precisely, there were seventy-eight matters. I handled them all.”

“...?”

He handled them? All those matters in such a short time?

Thousand-Faced Fox silently stared at the bamboo slips piled up like a mountain in one corner of the office. Then his eyes narrowed.

“Did you read the letter from Qinghai?”

“You mean the Kunlun Sect? Of course. It said they were pressed for time because they had to suppress bands of bandits and mounted bandits. It would be good if they arrived on time, but it should not matter much if they are a little late.”

“And the news from Sichuan?”

“It said they were all joining forces and speeding up the reconstruction of the Tang Clan. Oh, tell the Inner Hall to prepare an elixir with exceptional medicinal effects. I heard the Family Head’s condition is poor. Large-scale aid aside, we should at least help in this way for now.”

“Then what about the letter that arrived from the Nanman Beast Palace…?”

“Was there one? I did not see anything related to the Nanman Beast Palace among today’s matters.”

There was no other possibility. Just as Mae Jonghak had said, none of the matters submitted that day contained anything related to the Nanman Beast Palace.

Only then did a faint smile form around Thousand-Faced Fox’s lips, after he had spent all this time half believing and half doubting him.

“Hm? Why are you smiling?”

“Nothing. It simply warms my heart to see you so devoted to your duties…”

“Do not smile so slyly. Someone else might be horrified if they saw you.”

“…”

“In any case, the breeze feels nice. It really is a beautiful day.”

After ruining Thousand-Faced Fox’s mood, Mae Jonghak gazed aimlessly out the window and spoke.

“Would you like to take a walk outside with me? We may not have another day like this after today.”

“I would rather not.”

Thousand-Faced Fox answered curtly, then continued.

“I will send up another matter shortly, so do not do anything pointless, Alliance Leader. Get to work.”

“Even so, an honored guest is arriving. As a matter of basic decency, I should go out to greet them.”

“Did you say greet them?”

Thousand-Faced Fox paused, then limped toward the window on his prosthetic leg.

“Look over there.”

“...!”

Beyond the city wall, an object was slowly drawing closer.

It was blurry because of the considerable distance, but once he focused his internal energy, it was easy to identify the object as a carriage.

The problem was why a familiar face was sitting on the driver’s bench of that four-horse carriage.

*Why is Shadow Killer there?*

Shadow Killer was one of the Hidden Shadow Pavilion’s finest elite agents.

During the Star-Array Grand Banquet, he had tracked Mae Jonghak’s movements while Mae was concealing his identity. During the Great Faction War, he had taken the heads of countless fiends.

“It looks like a familiar face. Don’t you agree?”

“Yes. I sent Shadow Killer because there was trouble on the main road, but…”

He had sent the man to capture them, and now he was bringing them here like honored guests.

Thousand-Faced Fox swallowed the rest of his words as Mae Jonghak’s voice reached his ears.

“An urgent report came while you were away for a moment.”

“An urgent report?”

“Yes. I heard that some welcome faces were on their way.”

Mae Jonghak patted Thousand-Faced Fox’s shoulder twice, then leaned out the window and muttered,

“Come on. Let’s go.”

* * *

“Welcome.”

The carriage entered the Murim Alliance’s Inner City and came to a stop. The voice that greeted us as soon as we got down was fairly familiar.

*Sword Saint Mae Jonghak.*

I had once known him by the name Always-Victorious Sword Jongni Chu. He spotted me and gave a short laugh.

“How have you been, my friend?”

“…”

*That persona is really sticking around.*

When I dipped my head in greeting, Mae Jonghak smacked his lips in disappointment, then turned to Jeok Cheongang.

“It’s good to see that you look healthy.”

Jeok Cheongang, who had been yawning extravagantly while looking around, furrowed his brow.

“Were you speaking to this old man?”

“It has truly been a long time. I am glad to see you again.”

“You must have mistaken me for someone else. This old man has no particular connection with some brat whose blood hasn’t even dried on his head…”

Jeok Cheongang stopped mid-sentence.

His eyes grew wide as he looked Mae Jonghak up and down.

“Could it be you?”

“It is. It’s me.”

Mae Jonghak beamed and continued.

“Since we are meeting again, let me ask. Would you consider becoming the Alliance Leader?”

“...?”

“...?”

*Is this the Murim version of picking a group-project captain?*

[^1]: The Wuling Peach Blossom Spring is a classical image of an idyllic utopia.
```

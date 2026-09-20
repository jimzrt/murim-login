<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0521.txt",
      "sha256": "a2e92a0e561a3385488cb99c311015f094f47d7f80f19bf79c02e65084fc2314",
      "bytes": 13495
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "643217a99f578b07316861e9c1e64fa43112e998e1ad28e8b3649196a998812a",
      "bytes": 4409
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "0b6e68c21428decb151a72df85246307b9e63411f521a4731c3bc6ee31210f94",
      "bytes": 166116
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "1cc7d7555fde561531af34e4e87ad237556d82f26b4b8bb2cfb4f750bb6a2da5",
      "bytes": 1006
    },
    {
      "path": "characters/Hwangso.md",
      "sha256": "e92750a5d34dd7e78144be67759c2bce3d828687549b48063d2a51863ab5f2da",
      "bytes": 698
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "24c6fa58e5a42aa0b1db15dda5f7a52dd85bb9e71066b8d4a6ee69a2ba829556",
      "bytes": 1630
    },
    {
      "path": "characters/Mae Jonghak.md",
      "sha256": "2fae3929a921b39d42633bff13efc833332ce93f52fece1dedb15ea576b10d6d",
      "bytes": 1062
    },
    {
      "path": "characters/Mungyeong.md",
      "sha256": "a274af1d2b7f529a859aa282b8b9db4abad5a19a14c61ac5421261cde8e9e2a5",
      "bytes": 985
    },
    {
      "path": "characters/Peng Cheolhu.md",
      "sha256": "164e6b94605177c0270c3d34c802c847700527416719c95479f9f2d164d1efb0",
      "bytes": 680
    },
    {
      "path": "characters/Song Ho.md",
      "sha256": "666932cbf4e1c998c7a694f95d0ff2d48be6ce87902a3cb79d9078feea251145",
      "bytes": 1866
    },
    {
      "path": "characters/Unnamed.md",
      "sha256": "f4383754fac43c26a5b03ec51e2c7603a0d358e354e0e5157617a22066dbdbf3",
      "bytes": 750
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "5356e51fec07036e7c668c604cc568d18828de713411c12c4c7ec1f04b91c1a8",
      "bytes": 157165
    }
  ],
  "estimated_tokens": 12854
}
-->

# Durable State Update — Chapter 521

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 521. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 521. Profile updates may replace only one
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
  "chapter": 521,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 521,
    "continuity_sources": [521],
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
    "Mungyeong is the Slaughter Saint and former Divine Physician, a Returned to Youth Supreme Peak master and the greatest assassin in history; he is training Taekyung to control the violent internal energy produced by the Fire Gate Divine Technique.",
    "Zhuge Feng's Demon-Sealing Formation blocks all mana from the exposed Gate by drawing in natural qi, but its permanence and repeatability remain unresolved.",
    "Jang Taebo is the Jin Family of Taiyuan's Master of Ironcraft Hall and is summoning renowned artisans to process the Water God Dragon's remains.",
    "The New Murim Alliance has been publicly announced; Mae Jonghak is its sole identified suitable candidate for Alliance Leader and is handling its administrative affairs, while Song Ho has restored the Hidden Shadow Pavilion.",
    "The Southern Heaven Demon Empress is traveling toward Yunnan and expects to cause further deaths.",
    "Jin Mukyung remains secluded in the training hall after losing to Cheongpung, refusing to emerge until he achieves a great accomplishment.",
    "Unnamed, Hong Dao's practical Disciple, endured three months in Repentance Cave, achieved enlightenment, received Shaolin's Great Restoration Pill, and is now a scarred Supreme Peak master and Jung Ho's young Martial Uncle; Shaolin's new Abbot wants to meet Taekyung.",
    "The Black Dragon Demon Gate is an ancient unorthodox faction that once belonged to the Demonic Cult's Twelve Branches and now ranks among the Central Plains' strongest unorthodox powers.",
    "Jin Taekyung completed Stage 2 of Fake Murim Practitioner, achieved Single Reed Crossing the River, improved his internal-energy control and attributes, gained 50 bonus points and substantial EXP, and leveled up.",
    "The Dark Heaven assault near Mount Song ended in a chaotic misunderstanding: Jeok Cheongang emerged from a burning inn, was mistaken for a Dark Heaven fiend, was identified by Peng Cheolhu as the Returned-to-Youth Fire King, and was separated from the mob by Nangong Cheon."
  ],
  "continuity_sources": [
    520,
    519
  ],
  "open_questions": [
    "Will the Demon-Sealing Formation remain effective permanently, and can equivalent formations be installed repeatedly if more Gates appear?",
    "What is the Lord of Heaven's identity, and how is he connected to the dangerous force Taekyung associates with his original world?",
    "Where is the Southern Heaven Demon Empress ultimately headed, and what does she intend to do in Yunnan?",
    "What is the outcome of the duel between Jeok Cheongang and Nangong Cheon, the Azure Sky Sword King?",
    "How will the New Murim Alliance proceed without the missing Martial God, and will Jeok Cheongang accept Mae Jonghak's invitation to become Alliance Leader?"
  ],
  "safe_through": 520,
  "temporary_decisions": [
    "Render 새외무림 as Outer Murim, 새외 as Outer Lands, 북해빙궁 as North Sea Ice Palace, 야수묘왕 as Beast Miao King, and retain Nanman Beast Palace for 남만야수궁.",
    "Render 소뢰음사 as Small Thunderclap Temple, 광풍사 as Mad Wind Society, 포달랍궁 as Potala Palace, 오독문 as Five Poisons Sect, 독곡 as Poison Valley, 천축 as India, 갠지스강 as Ganges River, and 대환단 as Great Restoration Pill.",
    "Render 파사국 as Persia, 회교도 as Muslims, 영웅건 as hero headband, 대막 as great desert, 귀염권 as Ghost Flame Fist, and 장성 as Great Wall.",
    "Retain sa-eo for 사어, shark for 상어, Old Master for 노야, this old man/I for 노부, Shark Water-Ski Team for 수상스키단, and swift ship for 쾌조선.",
    "Render 정호 as Jung Ho, 사마표 as Sama Pyo, 흑룡도 as Black Dragon Saber, 대초자곤 as two-section staff, 시주 as Benefactor, 계율원주 as Discipline Hall Master, 십이지파 as Twelve Branches of the Demonic Cult, 모용세가 as Murong Family, 요녕 as Liaoning, 진돗개 하나 as Jindotgae One, 소하문 as Xiao He Gate, 장충도 as Long Serpent Saber, 방가 as Fang Family, 월미도 as Moon Beauty Saber, 검기상인 as the level of injuring others with Sword Energy, and 내성 as Inner City."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 적천강    | **Jeok Cheongang** |
| 매종학    | **Mae Jonghak**    |
| 청풍     | **Cheongpung**     |
| 검성     | **Sword Saint**               | Mae Jonghak    |
| 벽력도왕   | **Thunderbolt Saber King**    | Peng Cheolhu   |
| 무당파    | **Wudang**                       |
| 무림맹    | **Murim Alliance**               |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 사제     | **Junior Brother**                           |
| 전각     | **pavilion**                                 | Use “hall” only when established for a specific named building |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 화산     | **Huashan**            |
| 구화산    | **Mount Jiuhua**       |
| 노부      | **this old man / I**                                            |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 황소 | **Hwangso** | First-generation disciple of the Gongdao Sect and a reluctant search-party member. |
| 문경 | **Mungyeong** | Young medical apprentice and newly introduced passenger. |
| 송호 | **Song Ho** | Elderly martial artist known as the Thousand-Faced Fox. |
| 무명 | **Unnamed** | Dharma name given by Hong Dao; literally means having no name. |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 기감 | **Qi Sense** | Taekyung's sensory technique; its range reaches seventy meters in this chapter. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 오대세가 | **Five Great Families** | Major Murim grouping. |
| 연무장 | **training ground** | Private martial-arts practice area at Taekyung's newly rebuilt pavilion. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 창천검왕 | **Azure Sky Sword King** | One of the Ten Kings and the Grand Family Head of the Nangong Family. |
| 성라대연 | **Star-Array Grand Banquet** | Major martial gathering held in Henan every two or three years. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 중독 | **Poisoned** | System status abnormality caused by the poisons. |
| 창천 | **azure heaven** | The cloudless sky seen by Namgung Ryong. |
| 일각 | **fifteen minutes** | Quarter of a shichen; used for the remaining completion time. |
| 검왕 | **Sword King** | Short form for the Azure Sky Sword King, Nangong Cheon. |
| 천면호리 | **Thousand-Faced Fox** | Epithet of Song Ho. |
| 은영각 | **Hidden Shadow Pavilion** | Former Murim Alliance intelligence organization. |
| 은영각주 | **Chief of the Hidden Shadow Pavilion** | Office formerly held by Song Ho. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 반로환동 | **Returned to Youth** | Possible explanation for an apparently young Supreme Peak master. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 계도 | **precept blades** | Blades carried by the Hundred and Eight Arhats. |
| 화산신룡 | **Huashan Divine Dragon** | Title given to Cheongpung after the Star-Array Grand Banquet. |
| 호북 | **Hubei** | Province on Ju Gongsan's route from Guangdong to Henan. |
| 장강 | **Yangtze** | The river controlled by the Yangtze River Channel League. |
| 살수 | **assassin** | Professional killer considered as a possible suspect. |
| 장일 | **Jang Il** | Twenty-five-year-old two-knot Beggars' Sect Disciple killed near Emei. |
| 오대 | **Five Squads** | Named Tang Clan organizational group in Tang Sadok's mobilization order. |
| 강소 | **Jiangsu** | Province at the eastern end of the Yangtze route. |
| 비처 | **secret refuge** | Hidden retreat of the Dongting Fisherman. |
| 수신룡 | **Water God Dragon** | Legendary name for the true master of Dongting Lake; distinct from the modern Sea Serpent. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 내성 | **Inner City** | Fortified inner district of the Murim Alliance. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 매종학 | 청풍 | grandfather_to_grandson | Pung | affectionate-instructional | Mae Jonghak calls young Cheongpung 풍아 while teaching him the Crouching Tiger Fist. |
| 적천강 | 청풍 | overwhelming_elder_to_young_martial_artist | you / little punk | blunt, amused, and threatening | Jeok Cheongang uses 네, 이놈, and related blunt forms while testing Cheongpung. |
| 청풍 | 적천강 | young_martial_artist_to_overwhelming_elder | Grandpa Jeok | casual-familiar despite deference | Cheongpung uses 적 할아버지 while asking Jeok Cheongang to confirm Taekyung's condition; this is a familial form of address, not literal kinship. |
| 무명 | 적천강 | junior_monk_to_legendary_martial_master | Great Hero Jeok Cheongang | formal-deferential | Identifies Jeok by the title Fire King and the honorific 대협. |
| 적천강 | 벽력도왕 | rival_martial_master_to_rival_martial_master | Virility Saber King | insulting and taunting | Jeok coins 정력도왕 as a taunting replacement for the established title. |
| 벽력도왕 | 적천강 | rival_martial_master_to_rival_martial_master | Jeok Cheongang | boisterous and hostile-teasing | The Thunderbolt Saber King calls Jeok by name before their argument escalates. |
| 매종학 | 송호 | savior_to_survivor | you | casual-familiar | Mae uses 자네 while speaking to Song Ho after his identity is recognized. |
| 송호 | 매종학 | rescued_survivor_to_savior | Great Hero; you | formal-deferential and familiar | Song Ho credits Mae with saving his life and addresses him as 대협. |
| 청풍 | 문경 | martial_companion_to_medical_apprentice | Medical Apprentice | cheerful-polite | Cheongpung addresses Mungyeong as 의생님 while asking him to greet the Tang Clan. |
| 문경 | 적천강 | old_acquaintances | Fire King | familiar and grave | The figure bearing Mungyeong’s name greets Jeok Cheongang by his established epithet. |
| 적천강 | 문경 | overwhelming elder to old acquaintance | you / little punk | mocking and threatening | Mocks Mungyeong's expression and threatens to poke out his eyes. |
| 적천강 | 수신룡 | legendary_martial_master_to_dying_spirit_beast | you | wary and trembling | Jeok asks what the Water God Dragon is after witnessing its mental communication. |
| 문경 | 수신룡 | physician_to_dying_spirit_beast | you | guarded and curious | Mungyeong asks whether the Water God Dragon knows him. |
| 적천강 | 창천검왕 | long-standing martial rival and duel partner | Azure Sky Sword King | blunt and familiar | Explicitly names him while coming to fulfill their long-delayed duel promise. |
| 창천검왕 | 적천강 | long-standing martial rival and duel partner | Fire King | formal and familiar | Addresses Jeok Cheongang by title while welcoming the promised duel. |
| 창천검왕 | 벽력도왕 | Ten Kings peers | Sir Peng | formal but familiar | Tells Peng to calm himself after Peng's argument with Taekyung. |
| 벽력도왕 | 창천검왕 | Ten Kings peers | Great Hero Nangong | respectful and familiar | Addresses Nangong Cheon while crediting him with preventing a catastrophe. |

## Listed compact profiles

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 517
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, the grandson and Disciple of Sword Saint Mae Jonghak, and a Supreme Peak martial master known as the Huashan Divine Dragon.
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, a deep love of martial arts, competitive pride, unusual resistance to monster-induced Fear, and discomfort when someone copies his martial arts.
- **Voice:** Dreamy and hazy, with innocent, polite phrasing; he has begun imitating Taekyung's profanity.
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions while Taekyung is his only true martial rival; Tang Sadok has temporarily entrusted Mimi to him.

### Hwangso.md

# Hwangso (황소)

- **Safe through:** Chapter 494
- **Aliases:** None
- **Role:** First-generation disciple of the Gongdao Sect in Sichuan, deployed with roughly thirty second- and third-generation disciples to search for the surviving Third Fiend.
- **Personality:** Privileged, impatient, pleasure-seeking, inattentive, and dismissive of the danger surrounding the mission.
- **Voice:** Complaining and casual, with irreverent sarcasm toward his Senior Brother and the search.
- **Relationships:** His Senior Brother supervises him, and his prosperous merchant father forced him into the Murim to establish family connections.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 520
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, and Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Mae Jonghak.md

# Mae Jonghak (매종학)

- **Safe through:** Chapter 520
- **Aliases:** Sword Saint
- **Role:** Sword Saint and Cheongpung's grandfather; he is the New Murim Alliance's sole identified suitable candidate for Alliance Leader and currently handles its administrative affairs.
- **Personality:** Playful, easygoing, and teasing, but capable of handling heavy administrative responsibilities efficiently.
- **Voice:** Friendly, casually familiar, and cheerfully teasing, including when greeting old acquaintances and discussing leadership.
- **Relationships:** Cheongpung's grandfather and martial instructor; taught him the Taeeul Miri Palm; secretly entered Huashan while its Sect Leader slept, left a dagger and handwritten note, and then went into hiding, prompting Huashan's search; fought Jeok Cheongang at Mount Jiuhua more than forty years ago and left after their draw; his old friend Hong Dao left him a letter identifying Jin Taekyung as the Morning Star who would drive away darkness.

### Mungyeong.md

# Mungyeong (문경)

- **Safe through:** Chapter 516
- **Aliases:** Killing Ghost
- **Role:** Mungyeong is the legendary physician known as the former Divine Physician and Slaughter Saint, a Returned to Youth Supreme Peak master and the greatest assassin in history who passed the Divine Physician title to his Disciple.
- **Personality:** Compassionate, resolute, resourceful, and calm under extreme pressure.
- **Voice:** His Mungyeong persona is timid, deferential, and cheerful, while his Slaughter Saint voice is dry, impassive, and blunt.
- **Relationships:** Dong Feng is his Disciple, Jeok Cheongang is an old acquaintance whom Mungyeong helped break free of his Heart Demon, Mungyeong was asked to look after and instruct Jin Taekyung after testing his basics, and Mu Song plus five Water Dragon Stronghold subordinates now know he is an exceptionally powerful master but not that he is the Slaughter Saint.

### Peng Cheolhu.md

# Peng Cheolhu (벽력도왕)

- **Safe through:** Chapter 519
- **Aliases:** Thunderbolt Saber King
- **Role:** Peng Cheolhu is the Thunderbolt Saber King, a Ten Kings master and Great Hero of the Hebei Peng Family.
- **Personality:** Boisterous, hot-tempered, argumentative, and protective toward those connected to his close friend Hong Dao.
- **Voice:** Loud, blunt, confrontational, and prone to disguising embarrassment or retreat as serious martial instruction.
- **Relationships:** Long-standing rival and friend of Jeok Cheongang; close friend of Hong Dao; protective toward Hong Dao's Disciple Unnamed.

### Song Ho.md

# Song Ho (송호)

- **Safe through:** Chapter 520
- **Aliases:** Thousand-Faced Fox
- **Role:** Elderly Peak master known as the Thousand-Faced Fox; he has a wooden prosthetic leg and overwhelming physical strength, was formerly the head of the Murim Alliance's Hidden Shadow Pavilion, and, after Hong Dao sought him out over Dark Heaven, recalled his former subordinates and helped restore the Hidden Shadow Pavilion; he is an intelligence operative and master of disguise who can identify people through their faces, habits, and bone structure; he lost his leg during the final battle against the Demonic Cult decades ago and suffers recurring pain from the old injury; he suspects he previously encountered Jongni Chu and is now investigating him; he attends the Star-Array Grand Banquet's main-event duels every day before leaving during the third day; he now recognizes that Jongni Chu is closely connected to the day his leg was severed and that the connection is not mere coincidence; after receiving a report that Shadow Killer had been found, he sent agents to secure the dueling platform and went there himself when he sensed the clash between Supreme Peak masters; after arriving at Mount Song with hundreds of martial artists, he recognized Jongni Chu as Sword Saint Mae Jonghak and confirmed that Mae had saved his life in the past.
- **Personality:** Outwardly genial and relaxed, but observant, forceful, and intimidating when pursuing information.
- **Voice:** Lightly genial and conversational, turning quietly coercive during interrogation.
- **Relationships:** Takes the Geumwa Merchant Group's merchants away to question them about the young martial artist who drank their Yeoahong; recognizes Jin Taekyung as Jeok Cheongang's Disciple and praises his preliminary performance.

### Unnamed.md

# Unnamed (무명)

- **Safe through:** Chapter 519
- **Aliases:** None
- **Role:** Unnamed is a young Shaolin monk and practical Disciple of the late Hong Dao who achieved enlightenment after three months of treatment and training in Repentance Cave, becoming a Supreme Peak master and Jung Ho's young Martial Uncle.
- **Personality:** Naturally timid and introverted, but unable to control himself once angered.
- **Voice:** His current voice is rough, formal, and polite, punctuated by Buddhist invocations.
- **Relationships:** Hong Dao was his Master; Jung Ho is his Martial Nephew; he carries Hong Dao's will and recognizes the Morning Star whom Hong Dao intended him to find.

## Korean source

```text
＃521화



“반가운 김에 하는 말인데, 혹시 맹주 하실 생각 없소?”

“……?”

“……?”

조별과제 조장이 때려치운다고 하면 조원들이 동요하는 것은 당연지사.

예상을 아득하게 벗어난 매종학의 말에 벽력도왕은 입을 딱 벌렸고, 창천검왕과 무명은 아연한 눈빛으로 매종학을 바라보았다.

‘반가운 거랑 그거랑 도대체 무슨 상관……?’

‘이런 새끼가 무림맹주라니.’

말은 안 했지만 딱 그 표정이다.

그런 상황 속에서 마지막 한 사람, 적천강은 놀라울 정도로 덤덤한 안색으로 입을 열었다.

“평범한 인물이라면 이럴 때 말을 잇지 못할 거요. 하지만 노부는 달라. 근래에 미친놈들을 수두룩하게 만났거든.”

순간 적천강과 눈빛이 마주친 나는 뒤를 돌아보았다.

엄청난 우연의 일치인지, 아무도 없다. 바닥에서 뭔가를 쪼아먹고 있는 참새 한 마리 빼고는.

음, 그렇군. 적천강이 왜 이쪽을 쳐다보는지 드디어 깨달았다.

“새를 좋아하시는지는 몰랐네요. 하긴, 참새가 귀엽긴 하죠.”

“네놈을 보고 있느니라.”

“저요? 갑자기 저를 왜?”

“몰라서 묻느냐?”

“보통은 몰라서 묻죠. 아는데 왜 묻습니까.”

“주둥이를 신나게 나불대는 걸 보니 묻어 버리고 싶구나.”

음, 그럼 곤란해지는데.

잠깐 생각에 잠겨 있던 나는 반신반의하는 표정으로 물었다.

“이건 정말 혹시, 설마, 만에 하나의 경우를 생각해서 말씀드리는 건데. 방금 말씀하신 미친놈들 중에 제 이름이 끼어 있습니까?”

“무조건, 절대적으로, 의심의 여지 없이, 네놈의 이름이 제일 앞줄에 있다.”

“…….”

학창시절 뒤에서 일등은 몇 번 해 봤어도 앞에서 일등 해 보기는 처음이다.

이렇게라도 일 등을 해서 참 기쁘……기는 개뿔. 어이가 없네.

‘다른 사람도 아니고 적천강에게 저런 말을 듣다니. 심지어 청풍보다 순위가 높아.’

정신적 데미지에 눈앞이 아찔하다. 나는 적천강을 지그시 응시하며 입을 열었다.

“제 지인 중에 테스 형이라고 있는데. 그 형님이 그런 말씀을 하셨습니다. 너 자신을 알라.”

“지금 그거, 노부에게 한 말이냐?”

“몰라서 묻는 겁니까?”

“이런 호로…….”

반쯤 치켜들었던 주먹이 멈칫한다. 서서히 모여드는 주위의 시선을 느낀 적천강이 앓는 소리를 내며 매종학을 향해 돌아섰다.

“어쨌든 결론부터 딱 잘라서 대답하자면, 싫소.”

“헛. 어째서?”

“귀찮으니까.”

대답이 걸작이다. 적어도 한 번쯤은 솔깃할 만도 한데, 단순히 귀찮다는 이유로 무림 맹주 자리를 거절하다니.

“허어, 부정할 수 없는 사실이구려.”

“…….”

이건 더 걸작이네. 제발 수긍하지 마. 주변에 슬금슬금 사람들 모여드는 거 안 보여?

‘조졌네.’

이 대화가 퍼져 나가면 조별과제가, 무림맹이 파토 날지도 모른다는 불길한 생각이 스멀스멀 들기 시작한다.

하지만 안타깝게도, 서로를 마주한 두 걸작선은 그런 것 따위 신경 쓰지 않는 상남자들이었다.

“그런 감투는 성미에도 안 맞고, 사람 상대하는 것도 싫소.”

“앗. 나도 그렇소.”

“그럼 때려치우시던가.”

“그건 곤란하오.”

“그 이유는?”

턱을 긁적인 매종학이 한 마디를 툭 내뱉었다.

“누군가는 해야 하는 일이니까.”

“……!”

그저 무공이 좋아 검을 들었고, 검성이라는 별호를 얻은 한 남자.

참혹한 전란의 끝자락에서 부귀영화를 뒤로하고 스스로 야인을 자처하며 산으로 돌아간 진정한 무인(武人).

하지만 검성 매종학은 무인이기 이전에 대협(大俠)이다.

그가 맹주라는 직함을 받아들인 이유는 얄팍한 공명심 때문이 아니었다.

무인인 동시에 대협이라서다.

‘누군가는 해야 하는 일.’

짧지만 깊은 울림이 있는 한마디. 빤히 매종학을 바라보던 적천강이 피식 실소를 흘렸다.

“제법 긴 세월이 흘렀건만, 당신은 변하지 않았구려. 구화산에서 만났던 그 날이 어제라고 생각될 만큼.”

매종학이 눈을 크게 떴다.

“어제라니. 그게 무슨 소리요? 족히 수십 년도 전의 일인데.”

“…….”

“…….”

내 감동 돌려내. 이 인간아.

순간 억울한 감정이 들었던 건 나뿐만이 아니었다. 쏟아지는 사람들의 쎄한 시선에 매종학이 고개를 갸웃거렸다.

“내 기억이 잘못된 건가?”

웃음기가 싹 가신 적천강이 중얼거렸다.

“……정말 변하지 않았군. 오장육부가 문드러지는 기분이야.”

“아직도 몸이 좋지 않소? 중독된 건 다 나았다고 들었는데.”

“그 입 좀 여무시오. 계속 떠들어 대면 노부가 무슨 짓을 할지 모르니까.”

“이제야 하는 말인데, 내게 그런 말을 했던 사람은 적 대협이 처음이었소. 이래서 적 대협이 좋다니까.”

“……청풍, 그놈이랑 정말 그냥 사제지간이오? 핏줄이 이어진 것 아니고?”

이건 진짜 무림 7대 미스터리에 꼽힐 만한 의문이다.

나를 포함한 모두가 두근거리는 마음으로 매종학의 대답을 기다리고 있던 그때였다.

“제가 아는 바에 의하면, 맹주님과 화산신룡 사이에는 아무런 혈연관계도 없습니다.”

등 뒤에서 들려오는 늙수그레한 목소리. 의족(義足)을 단 채 절뚝이며 걸어오는 노인의 얼굴은 낯이 익었다.

‘천면호리 송호.’

전(前) 무림맹 은영각주이자, 신(新) 무림맹의 은영각주로 돌아온 그가 고개를 작게 숙이며 입을 열었다.

“올라가시지요. 다과를 준비해 놓았습니다.”



* * *



무림맹은 많은 사람으로 붐볐다.

가슴팍에 맹(盟)이라는 글자를 은빛 수실로 새겨넣은 이들이 곳곳에 돌아다녔고, 그중에는 병장기를 휴대한 무림인뿐만 아니라 정갈한 문사 차림을 한 이들의 숫자도 적지 않았다.

‘저 사람들은…….’

역시 은영각주라는 직함은 고스톱으로 딴 게 아니다.

내 시선에 담긴 의문을 즉각 알아차린 듯, 나란히 옆에서 걷던 천면호리가 짧게 설명했다.

“저들은 맹주부(盟主部) 직속일세.”

“왠지 구파일방이나 오대세가 쪽은 아닌 것 같은데요.”

“제대로 봤군. 맹주부 직속인만큼, 기밀 유지를 위해 다른 문파에 속하거나 신분이 확실히 검증되지 않은 이들은 선별하지 않았지. 자, 이쪽으로.”

무림맹 내부는 평야처럼 광활하면서도 미로처럼 복잡했다.

고개를 돌리는 곳마다 빼곡하게 솟은 전각 등의 건물이 즐비했고, 저 멀리 보이는 연무장에서는 기합성이 울려 퍼지고 있었다.

처음 마차에 내렸을 때만 해도 그 장소가 내성(內城)에 속하는 곳이라고 생각했는데, 점점 안으로 들어갈수록 경비는 삼엄해졌고 인적은 눈에 띄게 줄어들었다.

‘아니, 그보다는 눈에 보이지 않는다는 표현이 더 정확하겠지.’

아무리 호흡을 죽이고, 고도의 은잠술(隱潛術)을 펼친다고 해도 내게는 느껴진다.

벽면. 천장 위. 어둠 속에 몸을 숨긴 채 이곳을 주시하는 시선과 그들이 품은 기운들이.

“아까부터 궁금했던 건데, 저들이 은영각입니까?”

불쑥 던진 물음에 천면호리의 눈이 살짝 커졌다.

“언제부터 알고 있었나?”

“다섯 번째 문을 지날 때부터.”

“지금도 느껴지나?”

“예.”

“대단하군. 정말이지 대단해. 저들 네 사람은 은영각 내에서도 살수로 길러진 이들인데. 기척을 완벽하게 파악하다니.”

탄성을 흘리는 천면호리의 모습에, 나는 턱을 긁적였다.

“정말 몰라서 그러시는 겁니까, 아니면 시험입니까?”

“응? 그게 무슨 소린가?”

“시험이면 재미없네요. 넷이 아니라 다섯입니다.”

스으윽.

벽면에 걸어놓은 횃불이 작게 흔들렸다가 이내 잠잠해진다.

그건 주위에 은신해 있던 은영각 요원들의 동요를 드러내는 유일한 증거였고, 그들의 우두머리인 천면호리의 눈빛은 깊게 가라앉았다.

“설마 했는데, 우연이 아니었군.”

“사실 찍었습니다.”

“…….”

“농담이고, 수하분들께서 다들 실력이 뛰어나시네요. 하마터면 못 알아채고 지나칠 뻔했습니다.”

천면호리의 눈동자에 번뜩이는 빛이 스쳤다.

그것은 나를 시험했던 조금 전과는 달리 진심이 담긴 경탄과 호기심이 담긴 눈빛이었다.

“실로 놀라운 일이군. 자네의 무위에 대해서는 그간의 정보를 통해 어느 정도 사실에 가깝게 예측했다고 생각했는데…… 근래에 새롭게 깨달음을 얻었나?”

깨달음이라.

나는 열흘간의 장강 표류 수련을 떠올리며 고개를 끄덕였다.

아무래도 문경이 지시한 수련을 하며 얻은 가장 큰 소득은, 무공의 원천이라 할 수 있는 기(氣). 그 자체를 전보다 훨씬 세밀하게 다룰 수 있게 되었다는 것이다.

그 전의 내가 동아줄을 이용했다면, 지금은 실타래라고나 할까.

그러다 보니 자연스럽게 공력의 운용에 대한 이해도 올라갔고, 기감 역시 자연스럽게 날카로워졌다.

“아마도, 조금은요.”

“무시무시한 성장 속도로군. 믿기지 않을 정도야.”

천면호리의 말에, 아까부터 나를 힐끔거리던 벽력도왕이 중얼거렸네.

“확실히…… 적지 않은 세월을 살아오면서 네놈 같은 괴물은 또 처음 보는구나. 내 장손주 녀석과 좋은 경쟁 상대가 되겠어.”

“그, 장손주분 성함이?”

“팽도진.”

“펭도리요? 확실히 스타팅 포켓몬으로 좋죠. 귀엽고.”

“무슨 개소리냐! 팽도진, 팽도진 말이다! 성라대연 때 네 녀석과 접전을 펼쳤던!”

벽력도왕의 외침에 뒷골목 시정잡배처럼 휘적휘적 걸어가던 적천강이 친절하게 설명을 덧붙였다.

“너한테 일각 동안 개처럼 맞다가 항복한 그놈 말이다. 나이가 이립이던가.”

“아하. 이제야 기억나네. 마지막에는 도를 지팡이로 쓰시던데.”

“이, 이이……!”

“괜찮습니다. 원래 젊을 때는 여기저기서 맞기도 하고, 지기도 하는 거죠.”

적천강이 크리스마스 선물을 받은 꼬마처럼 환한 얼굴로 내 말을 받았다.

“팽가야. 그건 나이 들어도 마찬가지니까 너무 기대는 하지 말거라. 아무리 해 봤자 제 할아비처럼 반로환동도 못하고 늙어 죽기밖에 더하겠느냐.”

“이런 개 같은……!”

“크흠.”

아무리 생각해도 이 자리의 최대 피해자는 창천검왕이다.

아무 말도 안 하고 있어도 야무지게 들어오는 데미지에 노검객의 눈 밑 살이 파르르 떨렸다.

이어 들려온 매종학의 한마디는 쐐기를 박는 화룡점정이었다.

“다들 너무 조급해하지는 마시구려. 그냥 하다 보면 자연스럽게 되는 거니까.”

“……!”

“……!”

저게 말이야 방구야.

반로환동이 자연스럽게 되는 거였으면 천하 무림인 중에 절반은 반로환동이었겠다.

벽력도왕과 창천검왕. 두 사람이 한 치의 악의도 담겨 있지 않은 매종학의 말에 화도 못 내고 입을 다문 그때, 지금껏 무림맹에서 본 것 중 가장 크고 높게 솟은 전각 하나가 모습을 드러냈다.

“들어가시지요.”

처음에는 맹주가 거주하는, 뭐 그런 곳인 줄 알았다.

하지만 그 생각은 문을 열고 들어가기도 전에 착각으로 판명 났다.

타다다닥!

“강소(江蘇)에서 서신이 도착했습니다!”

“등급은?”

“지(地)급입니다.”

“관련 안건 정리해서 옮겨. 소평, 황소, 장일팔은 한 식경 안으로 보고 올리도록.”

촤촤촤촥!

바쁘게 돌아다니는 사람들. 전각 곳곳에 복잡하게 얽힌 정체불명의 원통을 통해 이동하는 죽간과 문서들.

이 모든 혼잡한 상황을 유심히 바라보던 천면호리가 입술을 열었다.

“호북(湖北), 무당(武當), 천(天)급.”

짧은 단어의 나열을 들은 문사 복장의 누군가가 고리를 잡아당긴다.

그리고 다음 순간.

쉬잉! 텅!

옆에 늘어져 있던 원통을 타고 떨어진 죽간 하나가 펼쳐졌다.

“여러분들을 이곳으로 모신 이유입니다. 닷새 전, 호북의 무당파로부터 도착한 급보지요.”

그의 말은 들리지도 않았다.

나는 죽간에 적힌 내용을, 아니 그림을 뚫어져라 응시하며 내심 중얼거렸다.

‘수신룡이…… 전부가 아니었군.’

검은 먹으로 그려진 정체불명의 무언가.

그건 누군가에게는 낯설면서도, 누군가에게는 낯익은 어떤 괴물이었다.
```

## Final English reading copy

```markdown
# Chapter 521

“Since it’s good to see you again, let me ask you something. Would you consider becoming the Alliance Leader?”

“...?”

“...?”

If the captain of a group project announced that he was quitting, it was only natural for the other members to panic.

Mae Jonghak’s words had gone far beyond anything I could have expected. The Thunderbolt Saber King’s mouth fell open, while the Azure Sky Sword King and Unnamed stared at Mae Jonghak in stunned silence.

*What does seeing each other again have to do with that...?*

*And this guy is the Alliance Leader?*

They had not said it aloud, but their expressions said exactly that.

In the middle of this situation, the last person present—Jeok Cheongang—opened his mouth with an astonishingly calm expression.

“An ordinary person would be unable to continue speaking at a moment like this. But this old man is different. I have met an awful lot of crazy bastards lately.”

The moment my eyes met Jeok Cheongang’s, I turned around.

By an incredible coincidence, there was no one behind me. Except for a sparrow pecking at something on the ground.

*I see. So that’s why Jeok Cheongang was looking this way.*

“I didn’t know you liked birds. Sparrows are cute, though.”

“I was looking at you.”

“Me? Why are you suddenly looking at me?”

“Are you asking because you don’t know?”

“Usually, people ask because they don’t know. Why would they ask if they already knew?”

“Seeing that mouth flap so happily makes me want to bury you.”

*That would be a problem.*

After thinking for a moment, I asked with a doubtful expression,

“I’m only asking this in case of a genuine maybe, perhaps, one-in-a-million possibility. Was my name included among the crazy bastards you mentioned?”

“Without question. Absolutely. Beyond the slightest doubt, your name is at the very front of the list.”

“...”

I had come in dead last a few times during my school days, but this was the first time I had ever come in first.

*I should be happy that I managed to come in first somehow...*

*No, forget that. This is ridiculous.*

*To hear something like that from Jeok Cheongang of all people. And I ranked higher than Cheongpung.*

The psychological damage made my vision swim. I stared at Jeok Cheongang and opened my mouth.

“I have an older friend named Tess hyung. He once said something like this: ‘Know thyself.’”

“Was that directed at this old man?”

“Are you asking because you don’t know?”

“You little son of a—”

The fist he had raised halfway suddenly stopped.

Jeok Cheongang sensed the gazes gathering around us, let out a pained groan, and turned back toward Mae Jonghak.

“In any case, to give you a clear answer, I refuse.”

“Ho. Why?”

“Because it’s a pain.”

The answer was a masterpiece. He could at least have been tempted once, but he had rejected the position of Alliance Leader simply because it was bothersome.

“Ah. That is an undeniable fact.”

“...”

That was an even greater masterpiece.

*Please don’t agree with him. Can’t you see people slowly gathering around us?*

*We’re screwed.*

If this conversation spread, there was a growing chance that the group project—or rather, the Murim Alliance—would fall apart.

Unfortunately, the two masterpieces facing each other were both shamelessly manly men who did not care about such things.

“That sort of title doesn’t suit my temperament, and I dislike dealing with people.”

“Ah. I’m the same.”

“Then quit.”

“That would be difficult.”

“Why?”

Mae Jonghak scratched his chin and casually tossed out a single sentence.

“Because someone has to do it.”

“...!”

A man who had taken up the sword simply because he loved martial arts, and who had earned the title of Sword Saint.

A true martial artist who, at the end of a brutal war, abandoned wealth and glory, chose to live as a recluse, and returned to the mountains.

But Sword Saint Mae Jonghak was a Great Hero before he was a martial artist.

He had not accepted the title of Alliance Leader out of shallow vanity.

He had accepted it because he was both a martial artist and a Great Hero.

*Because someone has to do it.*

It was a short sentence, but it carried a deep resonance. Jeok Cheongang stared at Mae Jonghak and let out a quiet laugh.

“Many long years have passed, yet you haven’t changed. It feels as though the day we met at Mount Jiuhua was only yesterday.”

Mae Jonghak’s eyes widened.

“Yesterday? What are you talking about? That happened at least several decades ago.”

“...”

“...”

*Give me back my touching moment, you bastard.*

I was not the only one who felt wronged. Under the pointed gazes pouring down on him, Mae Jonghak tilted his head.

“Did I remember incorrectly?”

All traces of laughter vanished from Jeok Cheongang’s face.

“...You really haven’t changed. It feels like my internal organs are rotting.”

“Are you still unwell? I heard you had recovered fully from the poisoning.”

“Shut that mouth of yours. If you keep talking, I don’t know what this old man might do.”

“Now that I think about it, Great Hero Jeok was the first person to say something like that to me. This is why I like you.”

“...Are you and that brat Cheongpung really just Master and Disciple? Are you not related by blood?”

That was a question worthy of being counted among the Seven Great Mysteries of the Murim.

Just as everyone, myself included, waited for Mae Jonghak’s answer with pounding hearts, an old voice came from behind us.

“As far as I know, there is no blood relation between the Alliance Leader and the Huashan Divine Dragon.”

The face of the old man limping toward us on a prosthetic leg was familiar.

*Thousand-Faced Fox Song Ho.*

The former Chief of the Hidden Shadow Pavilion of the Murim Alliance—and now its reinstated Chief—gave a slight bow and opened his mouth.

“Please come upstairs. I have prepared some refreshments.”

* * *

The Murim Alliance was crowded with people.

People bearing the character *Alliance* embroidered in silver thread on their chests moved around in every direction. Among them were not only martial artists carrying weapons, but also quite a few people dressed in neat scholars’ robes.

*Those people...*

The post of Chief of the Hidden Shadow Pavilion was not something Song Ho had won at a card table.

As if he had immediately noticed the question in my gaze, he gave me a brief explanation while walking beside me.

“They are directly under the Alliance Leader’s Office.”

“They don’t look like they’re from the Nine Sects and One Gang or the Five Great Families.”

“You observed correctly. Since they are directly under the Alliance Leader’s Office, we did not select anyone who belonged to another sect or whose identity had not been thoroughly verified, in order to maintain confidentiality. Come this way.”

The interior of the Murim Alliance was as vast as a plain and as complicated as a maze.

Everywhere I turned, pavilions and other buildings rose densely around us. From the training ground in the distance came the shouts of people practicing.

When I first got down from the carriage, I had thought the place belonged to the Inner City. But the farther inside we went, the tighter the security became, and the fewer people we saw.

*No. More accurately, it would be better to say that they had become invisible.*

No matter how completely they suppressed their breathing or how advanced their concealment techniques were, I could still sense them.

On the walls. Above the ceiling. Hidden in the darkness, watching this place.

I could sense the gazes and energy of those concealed around us.

“I’ve been curious about this for a while. Are they members of the Hidden Shadow Pavilion?”

Song Ho’s eyes widened slightly at my sudden question.

“When did you realize?”

“When we passed the fifth door.”

“Can you still sense them?”

“Yes.”

“Impressive. Truly impressive. Those four were raised as assassins within the Hidden Shadow Pavilion. To detect their presence perfectly...”

As Song Ho exclaimed in admiration, I scratched my chin.

“Are you really asking because you don’t know, or is this a test?”

“Hm? What do you mean?”

“If it’s a test, it’s not very fun. There are five of them, not four.”

Ssss.

The torch hanging on the wall trembled slightly, then quickly became still.

It was the only evidence of the agitation among the Hidden Shadow Pavilion agents concealed nearby. The gaze of their leader, Thousand-Faced Fox Song Ho, sank deeply.

“I suspected as much, but it wasn’t a coincidence.”

“Honestly, I just took a guess.”

“...”

“I’m kidding. Your subordinates are all very skilled. I almost failed to notice them and walked right past.”

A flash passed through Song Ho’s eyes.

Unlike the look he had given me when testing me moments earlier, this one contained genuine admiration and curiosity.

“That is truly astonishing. Based on the information I had gathered, I thought I had made a reasonably accurate prediction of your martial ability... Have you gained new insight recently?”

*Insight.*

I recalled the ten-day training session spent drifting down the Yangtze and nodded.

The greatest gain I had obtained from the training Mungyeong had assigned me was the ability to handle qi—the source of martial arts—with far greater precision than before.

If I had been handling a rope before, I was now handling a single strand of thread.

As a result, my understanding of controlling internal energy had naturally improved, and my Qi Sense had sharpened as well.

“Perhaps. A little.”

“Your growth is terrifying. It’s almost impossible to believe.”

At Song Ho’s words, the Thunderbolt Saber King, who had been glancing at me for some time, muttered,

“Indeed... In all the years I’ve lived, you’re the first monster I’ve ever seen like this. You’ll make a good rival for my eldest grandson.”

“Your eldest grandson’s name is...?”

“Peng Dojin.”

“Pengdori? That’s a great starter Pokémon. Cute, too.”

“What the hell are you talking about? Peng Dojin! Peng Dojin! The one who gave you a close fight at the Star-Array Grand Banquet!”

Jeok Cheongang, who had been swaggering along like a back-alley thug, kindly added an explanation.

“The one you beat like a dog for fifteen minutes until he surrendered. Was he thirty?”

“Ah. Now I remember. He used his saber as a cane at the end.”

“Y-you... You...!”

“It’s all right. When people are young, they get beaten here and there, and they lose sometimes.”

Jeok Cheongang accepted my words with a bright expression, like a child who had just received a Christmas present.

“Peng boy, it’ll still be the same when he gets older, so don’t get your hopes up. No matter how hard he tries, he’ll just end up like his grandfather—unable to Return to Youth, growing old and dying.”

“You son of a—!”

“Ahem.”

No matter how I looked at it, the greatest victim here was the Azure Sky Sword King.

Even though he said nothing, he kept taking solid hits from every direction. The skin beneath the old swordsman’s eyes trembled.

Mae Jonghak’s next comment drove in the final nail.

“Don’t be so impatient, everyone. If you just keep at it, it happens naturally.”

“...!”

“...!”

*Was that supposed to be words or a fart?*

If Returning to Youth happened naturally, half the martial artists in the world would have already Returned to Youth.

Just as the Thunderbolt Saber King and the Azure Sky Sword King fell silent, unable even to get angry at Mae Jonghak’s completely unmalicious words, the largest and tallest pavilion I had seen in the Murim Alliance came into view.

“Please come inside.”

At first, I thought it was where the Alliance Leader lived, or something like that.

But that assumption was proven wrong before we even opened the door.

Tap-tap-tap-tap!

“A letter has arrived from Jiangsu!”

“What’s the Grade?”

“Earth Grade.”

“Organize the related matters and relay them. Have So Pyeong, Hwangso, and Jang Il-pal submit their reports within half an hour.”

Whoosh, whoosh, whoosh!

People hurriedly moved around the pavilion. Bamboo slips and documents traveled through mysterious cylinders intricately connected throughout the building.

Thousand-Faced Fox Song Ho watched the entire chaotic scene carefully before opening his mouth.

“Hubei. Wudang. Heaven Grade.”

Someone in scholars’ robes heard the short string of words and pulled on a ring.

The next moment—

Whoosh! Thunk!

A bamboo slip that had fallen through the cylinder hanging beside us unfurled.

“This is why we summoned you here. It is an urgent report that arrived from the Wudang Sect of Hubei five days ago.”

I could not hear what he said.

I stared at the contents written on the bamboo slip—or rather, at the picture—and muttered inwardly.

*The Water God Dragon... wasn’t the whole story.*

Something unidentifiable had been drawn in black ink.

It was a monster unfamiliar to some, yet strangely familiar to others.
```

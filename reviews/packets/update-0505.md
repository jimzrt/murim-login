<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0505.txt",
      "sha256": "d99814e04b0da813850fcd0f0590ce54ee0814539ab03b6ca180a22159a18bb0",
      "bytes": 14071
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "258a7588a129e33c46c88aff5918dc9c8f030488fa7dcf69cb89417f7ee81fd4",
      "bytes": 5645
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "c1e384d5a974bb07a27204ca124cc295e65e87a55a0b54cfbd9baa124b4a2eac",
      "bytes": 160810
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "3ccd0284ff8b65d32860dac1e710b68e8a4fcd4baa4af84de53d9f28a0ccbead",
      "bytes": 1006
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "bee2e8cc73bb3d58d9e183261d8d13a95809d457d8a7c16dcf6642c85eb2a52a",
      "bytes": 553
    },
    {
      "path": "characters/Human Butcher.md",
      "sha256": "273d96f095791e568887a4b954b9915891d341af838aac1b8ff19b96d97b87c0",
      "bytes": 667
    },
    {
      "path": "characters/Hyeongong.md",
      "sha256": "7bb792d51ccebd79d8ab9426ae5b7c6e68999b3f620bcdfc6ec15940543ae376",
      "bytes": 768
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "ad81d5d842adec85fc9eee277809e601b00369a7b18dee02b181ad20602c8a37",
      "bytes": 1610
    },
    {
      "path": "characters/Jin Wikyung.md",
      "sha256": "3cca35db00c51241134f5af16bb8cf93bc55e46b6755f7d4c05b46cbe3a0243f",
      "bytes": 1210
    },
    {
      "path": "characters/Mu Song.md",
      "sha256": "bd87d49235f3e78f197ab5073261c3fc61c764226e68b15527eab12e271f5de5",
      "bytes": 907
    },
    {
      "path": "characters/Mungyeong.md",
      "sha256": "e7f6dd2e1c09da90bafef533335153681192125884354919dd49fa448c0c45e8",
      "bytes": 842
    },
    {
      "path": "characters/Zhuge Feng.md",
      "sha256": "c31fba0e8747506f4b258ec9460a1913c2df2ac38ea43712557e2c49c16e7f92",
      "bytes": 649
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "63ebed2f53e9f6dc1130392389c28109440545feb85267a0b031b13b76ad33d3",
      "bytes": 154086
    }
  ],
  "estimated_tokens": 13959
}
-->

# Durable State Update — Chapter 505

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 505. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 505. Profile updates may replace only one
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
  "chapter": 505,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 505,
    "continuity_sources": [505],
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
    "Jeok Cheongang’s infirmities of old age began immediately after he left Sichuan; his leaking innate qi causes progressive memory and time loss, with seven external days experienced as five days by Jeok in this episode.",
    "Mungyeong is the Slaughter Saint and former Divine Physician, a Returned to Youth Supreme Peak master whose assassin instincts remain formidable despite decades spent living as a medical apprentice.",
    "Jeok Cheongang’s Heart Demon and the dark memories binding him have been expelled, and he has entered a new realm after breaking free of those chains.",
    "Zhuge Feng’s Demon-Sealing Formation blocks all mana from the exposed Gate by drawing in natural qi, but whether it is permanent and repeatable remains unresolved.",
    "Jang Taebo is the Jin Family of Taiyuan’s Master of Ironcraft Hall and is summoning renowned artisans to process the Water God Dragon’s remains.",
    "War has begun, and the New Murim Alliance is scheduled to be founded at Mount Song in about one month, with Taekyung believing Dark Heaven deliberately planned the Gate incident.",
    "Jin Wikyung proposed the Hubei political arrangement through Hongcheon, the new Provincial Administration Commissioner and Prince Shangshan’s hidden loyal retainer; the purge of Hubei’s dark-path figures was intended to create an opportunity for rival unorthodox factions while warning them.",
    "Around one hundred Level 5 Mutated Minnows, locally called Blood Fish, were captured in the Gate’s entrance waterways; the remaining population is unknown, and the fish kill one another.",
    "The Southern Heaven Demon Empress is traveling toward Yunnan and expects to cause further deaths.",
    "Jin Mukyung remains secluded in the training hall after losing to Cheongpung, refusing to emerge until he achieves a great accomplishment.",
    "Jeok Cheongang is expected to travel with Jin Wikyung’s party to the New Murim Alliance after seven days and nights of seclusion, apparently persuaded by Taekyung.",
    "Zhuge Gonghu’s historical gamble directed the thousand-man Black Wind Corps through Mount Jiuhua, allowing Jeok Cheongang to annihilate it and gain the title of Fire King."
  ],
  "continuity_sources": [
    504,
    503
  ],
  "open_questions": [
    "Will the Demon-Sealing Formation remain effective permanently, and can equivalent formations be installed repeatedly if more Gates appear?",
    "What is the Lord of Heaven’s identity, and how is he connected to the dangerous force Taekyung associates with his original world?",
    "Where is the Southern Heaven Demon Empress ultimately headed, and what does she intend to do in Yunnan?",
    "Will the fractured unorthodox factions accept the New Murim Alliance’s invitation instead of joining Dark Heaven?",
    "What lasting abilities or changes will follow Jeok Cheongang’s breakthrough after his Heart Demon was expelled?"
  ],
  "safe_through": 504,
  "temporary_decisions": [
    "Render 산공독 as Energy-Dispersing Poison, 강력한 산공독 as Potent Energy-Dispersing Poison, 칠보추혼산 as Seven-Step Soul-Chasing Powder, 강력한 칠보추혼산 as Potent Seven-Step Soul-Chasing Powder, 심각한 복통 as Severe Stomachache, 고기 방패 as Meat Shield, 독 장아찌 as Poisoned Pickle, and 독의 as Poison Physician; retain secret martial arts, Master-Disciple relationship, Killing Ghost, and Fake Murim Martial Artist, and preserve 악 as Agh in the Quest interface; render 실명산 as Blindness Powder, 살천문 as Salcheonmun, and 스승의 날 as Teacher’s Day.",
    "Render 기억의 파편 as Memory Fragment, 게이트 공략 as Gate Conquest, 텔레포트 as Teleport, 마법 as Magic, 흑풍단 as Black Wind Corps, 혈어 as Blood Fish, 변이된 송사리 as Mutated Minnow, 왜국 as Wa Kingdom, 인자 as ninja, and 절강 as Zhejiang; render 강력한 마비산 as Potent Paralysis Powder, 강력한 미혼산 as Potent Soul-Bewitching Powder, 전신 마비 as Full-Body Paralysis, 독성 흡수 as Poison Absorption, and 해독 as Detoxification.",
    "Render 시산혈해 as sea of corpses and blood and retain Old Master for 노야 with the established rough, profane Taekyung-Jeok banter; render 해시 as hour of the Pig, 한 식경 as half an hour, 타구봉 as Dog-Beating Staff, 창룡 as Azure Dragon, and 무량수불 as Infinite Life Buddha; preserve geun as the traditional weight unit with a footnote.",
    "Render 선천지기 as innate qi, 진원진기 as true-origin qi, 천기 as heavenly patterns, and 후천지기 as acquired qi.",
    "Render 심마 as Heart Demon, 비급 as martial arts manual, 송문고검 as Pine-Pattern Ancient Sword, 반로환동 as Returned to Youth, 강강수월래 as Ganggangsullae, 생사부 as Book of Life and Death, 기막 as qi curtain, 무극태을검 as Martial Extremity Grand Unity Sword, 이룡 as Two Dragons, 원정 as Origin Essence, 내단 as inner core, 영험한 기운 as sacred energy, 대호 as great tiger, 취팔선권 as Drunken Eight Immortals Fist, 귀면 as Ghost Face, 요단강 as Jordan River, 진룡 as Jin Dragon, 마봉진 as Demon-Sealing Formation, 철기당 as Ironcraft Hall, 철기당주 as Master of Ironcraft Hall, 신룡 as Divine Dragon, 신(新) 무림맹 as New Murim Alliance, 면벽수련 as secluded meditation, 호법 as stand guard, 한나절 as half a day, 일다경 as the time it takes to drink a cup of tea, 촌각 as moments, 진맥 as take one’s pulse, 은영술 as concealment techniques, 표창 as throwing blades, and 철구 as iron balls."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진위경    | **Jin Wikyung**    |
| 적천강    | **Jeok Cheongang** |
| 청풍     | **Cheongpung**     |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 태원진가   | **Jin Family of Taiyuan**        |
| 화산파    | **Huashan**                      |
| 무당파    | **Wudang**                       |
| 무림맹    | **Murim Alliance**               |
| 제갈세가   | **Zhuge Clan**                   |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 정파     | **orthodox faction**                             |                                                       |
| 마교     | **Demonic Cult**                                 |                                                       |
| 가주     | **Family Head**                              |
| 장문인    | **Sect Leader**                              |
| 제자     | **Disciple**                                 |
| 사형     | **Senior Brother**                           |
| 전각     | **pavilion**                                 | Use “hall” only when established for a specific named building |
| 선배     | **Senior**                                   |
| 은인     | **Benefactor**                               |
| 명성               | **Fame**                       |
| 태원     | **Taiyuan**            |
| 하남     | **Henan**              |
| 화산     | **Huashan**            |
| 구화산    | **Mount Jiuhua**       |
| 정마대전   | **Great Faction War**         |
| 노부      | **this old man / I**                                            |
| 도사      | **Daoist**                                                      |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 현공진인 | **Perfected Being Hyeongong** | Veteran Wudang Daoist master and the current Sect Leader's Junior Brother. |
| 무송 | **Mu Song** | Lord of Water Dragon Stronghold and disciple of the Seafaring King. |
| 문경 | **Mungyeong** | Young medical apprentice and newly introduced passenger. |
| 제갈풍 | **Zhuge Feng** | Current Family Head of the Zhuge Clan. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 오대세가 | **Five Great Families** | Major Murim grouping. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 반로환동 | **Returned to Youth** | Possible explanation for an apparently young Supreme Peak master. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 계인 | **Buddhist precept seals** | Seals carved into the foreheads of Shaolin martial monks. |
| 노야 | **Old Master** | Taekyung's private address for Jeok Cheongang. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 내신 | **school grades** | School-record grades referenced in Taekyung’s insult. |
| 수룡채 | **Water Dragon Stronghold** | Major river stronghold belonging to the Yangtze River Channel League. |
| 선화아 | **Ship-Fire Boy** | Mu Song's sobriquet; literally a child who lights fires aboard a ship. |
| 일원 | **One Origin** | Named Tang Clan organizational unit in Tang Sadok's mobilization order. |
| 오대 | **Five Squads** | Named Tang Clan organizational group in Tang Sadok's mobilization order. |
| 살귀 | **Killing Ghost** | Mungyeong's earlier sobriquet before he became the Slaughter Saint. |
| 제갈 | **Zhuge** | Surname used for Sir Zhuge. |
| 이룡 | **Two Dragons** | Collective ranking beneath the Ten Kings in Murim gossip. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 적천강 | 청풍 | overwhelming_elder_to_young_martial_artist | you / little punk | blunt, amused, and threatening | Jeok Cheongang uses 네, 이놈, and related blunt forms while testing Cheongpung. |
| 청풍 | 적천강 | young_martial_artist_to_overwhelming_elder | Grandpa Jeok | casual-familiar despite deference | Cheongpung uses 적 할아버지 while asking Jeok Cheongang to confirm Taekyung's condition; this is a familial form of address, not literal kinship. |
| 무인 | 진위경 | vassal_martial_artist_to_lesser_family_head | Lesser Family Head | formal-deferential | The Mount Heng martial artists greet Jin Wikyung as 소가주님 while pledging loyalty. |
| 진위경 | 적천강 | host_to_legendary_guest | Great Hero Jeok | formal-deferential | Introduces himself and pays respects to Jeok Cheongang as the Fire King. |
| 적천강 | 진위경 | elder_to_younger_family_head | you | gruff and teasing | Uses 자네 while mistaking Wikyung for Taekyung’s father and questioning his age. |
| 문경 | 무송 | survivor_to_savior_and_authority | Great Hero Mu Song | formal-deferential | Mungyeong credits Mu Song with saving him and asks him to spare Hwang Tae-gu. |
| 무송 | 문경 | stronghold_lord_to_young_passenger | you | gruff-but-considerate | Mu Song offers Mungyeong the right to decide Hwang Tae-gu's fate. |
| 청풍 | 문경 | martial_companion_to_medical_apprentice | Medical Apprentice | cheerful-polite | Cheongpung addresses Mungyeong as 의생님 while asking him to greet the Tang Clan. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 문경 | 적천강 | old_acquaintances | Fire King | familiar and grave | The figure bearing Mungyeong’s name greets Jeok Cheongang by his established epithet. |
| 진위경 | 막내 | older brother to younger brother | my youngest | intimate and informal | Jin Wikyung uses 막내야 affectionately for Jin Taekyung. |
| 무송 | 적천강 | junior_martial_artist_to_legendary_martial_master | Great Hero Jeok | formal-deferential | Mu Song respectfully refers to Jeok Cheongang as 적 대협 while worrying that Jeok dislikes him. |
| 적천강 | 문경 | overwhelming elder to old acquaintance | you / little punk | mocking and threatening | Mocks Mungyeong's expression and threatens to poke out his eyes. |
| 적천강 | 무송 | legendary martial master to stronghold lord | you | gruff, coercive, and dismissive | Uses 자네 while ordering Mu Song to take the group only as far as Sichuan and leave the fast ship. |
| 청풍 | 무송 | young martial companion to stronghold lord | you | cheerful and familiar | Offers Mu Song his last dumpling and then induces him to buy more in Guang'an. |
| 적천강 | 제갈풍 | senior_martial_artist_to_old_acquaintance | you / ill-mannered brat | blunt, familiar, and teasing | Jeok treats Zhuge Feng as the younger acquaintance he remembers from childhood. |
| 제갈풍 | 적천강 | younger_old_acquaintance_to_legendary_senior | Senior | respectful but relaxed | Zhuge Feng recalls Jeok's earlier visit and addresses him as an old senior. |
| 제갈풍 | 무송 | family_head_to_stronghold_lord | Ship-Fire Boy Mu Song | calm, formal, and pointed | Zhuge Feng stops Mu Song from leaving by saying the coming information concerns him. |
| 무송 | 제갈풍 | stronghold_lord_to_orthodox_family_head | Great Hero Zhuge | formal and concerned | Mu Song addresses Zhuge Feng after realizing why he was asked to remain. |
| 현공진인 | 제갈풍 | senior Wudang master to Zhuge Clan Family Head | Family Head Zhuge | formal-respectful | Uses 제갈가주 while discussing the fast ship and the route. |
| 제갈풍 | 현공진인 | Zhuge Clan Family Head to senior Wudang master | Perfected Being Hyeongong | formal-deferential | Addresses Hyeongong with marked respect and calls his presence a great reinforcement. |
| 진위경 | 무송 | Alliance inspector to Stronghold Lord | Stronghold Lord | formal and cautionary | Uses 채주 while warning Mu Song that the group did not come to spill blood. |
| 제갈풍 | 문경 | old acquaintance to revealed legendary assassin | Slaughter Saint | excited and respectful | Zhuge Feng identifies Mungyeong by his established sobriquet after recognizing his identity. |
| 문경 | 제갈풍 | legendary_senior_to_younger_family_head | you; burden | blunt, insulting, and commanding | Mungyeong orders Zhuge Feng onto his back and dismisses his objections. |
| 청풍 | 제갈풍 | young_martial_artist_to_family_head | Great Hero Zhuge Feng | cheerful and polite | Cheongpung addresses Zhuge Feng as 제갈풍 대협, but deliberately mispronounces the name once as 제갈퐁 for comic effect. |
| 제갈풍 | 청풍 | family_head_to_younger_martial_artist | you | familiar and polite | Zhuge Feng uses 자네 while instructing Cheongpung and responding to his advice. |
| 진위경 | 현공진인 | Lesser Family Head to senior Wudang master | Perfected Being Hyeongong | formal-respectful | Addresses Hyeongong as 진인 while praising the Water God Dragon. |
| 제갈풍 | 진위경 | Zhuge Clan Family Head to Jin Family Lesser Family Head | Lesser Family Head | formal and conciliatory | Uses 소가주 while trying to secure Jin Wikyung's support during the settlement. |
| 진위경 | 제갈풍 | Jin Family Lesser Family Head to Zhuge Clan Family Head | Sir Zhuge | formal with deliberate comic deference | Uses 제갈 대협 while theatrically scolding Taekyung to force Zhuge Feng to concede. |
| 진위경 | 문경 | Jin Family Lesser Family Head to medical apprentice | you | formal-polite | Asks whether Jin Taekyung will arrive soon. |

## Listed compact profiles

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 499
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, the grandson and Disciple of Sword Saint Mae Jonghak, and a Supreme Peak martial master known as the Huashan Divine Dragon.
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, a deep love of martial arts, competitive pride, unusual resistance to monster-induced Fear, and discomfort when someone copies his martial arts.
- **Voice:** Dreamy and hazy, with innocent, polite phrasing; he has begun imitating Taekyung's profanity.
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions while Taekyung is his only true martial rival; Tang Sadok has temporarily entrusted Mimi to him.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 504
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Human Butcher.md

# Human Butcher (인도)

- **Safe through:** Chapter 482
- **Aliases:** None
- **Role:** Former mysterious Han Chinese mounted-bandit power in Northern Gaoyuan commanding fifty subordinates; a Peak master killed by an unnamed old man in a single move
- **Personality:** Cold, intimidating, and murderous; he kills people as though slaughtering livestock
- **Voice:** Cold, curt, and quietly threatening
- **Relationships:** He is one of four powerful participants at the Northern Gaoyuan gathering, intimidates Temur, and has claimed Ghost Sword Wipeng as his personal target in the proposed attack

### Hyeongong.md

# Perfected Being Hyeongong (현공진인)

- **Safe through:** Chapter 496
- **Aliases:** None
- **Role:** Perfected Being Hyeongong is a veteran Wudang Daoist master of the previous generation, the current Sect Leader's Junior Brother, and a Supreme Peak swordsman who reached the ultimate stage of the Taiji Wisdom Sword.
- **Personality:** Hyeongong is humble and self-deprecating about his limited worldly knowledge, carries the authority of an experienced senior master, and openly covets exceptional weapons.
- **Voice:** Measured, respectful, and lightly self-deprecating.
- **Relationships:** Hyeongong is the current Wudang Sect Leader's Junior Brother and a respected senior to Zhuge Feng.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 504
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin and Furnace Fire Pure Blue, and Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Jin Wikyung.md

# Jin Wikyung (진위경)

- **Safe through:** Chapter 504
- **Aliases:** Junzi Sword
- **Role:** Jin Wikyung is the thirty-six-year-old Lesser Family Head and future Family Head of the Jin Family of Taiyuan, the Alliance Leader who unified Shanxi Murim and Shanxi Province's foremost landowner and magnate.
- **Personality:** Calm, authoritative, and politically capable in public; protective and affectionate toward Taekyung beneath a stern mask. Takes responsibility for his people, acts decisively under pressure, and prioritizes family survival.
- **Voice:** Restrained, formal, and commanding with subordinates; openly affectionate, proud, and occasionally exuberant with Taekyung.
- **Relationships:** Jin Wikyung is Taekyung's eldest brother and future Family Head who protects and mentors him, commands Wipeng and the Jin Family's forces, has worked with Jeok Cheongang, and maintains a political connection with Hongcheon, Prince Shangshan's hidden loyal retainer; Jin Mukyung is his younger brother and a potential successor alongside Taekyung.

### Mu Song.md

# Mu Song (무송)

- **Safe through:** Chapter 468
- **Aliases:** Ship-Fire Boy
- **Role:** Lord of Water Dragon Stronghold, a Peak master and the Seafaring King's second martial Disciple who controls major Yangtze river traffic in Sichuan, belongs to the Yangtze River Channel League's moderate faction, and is an exceptionally skilled ship captain.
- **Personality:** Ambitious, domineering, impatient with interruptions, and capable of pragmatic cooperation when circumstances demand it.
- **Voice:** Deep and low in private, shifting to dry authority or boisterous command when addressing subordinates and rivals.
- **Relationships:** Mu Song is a member of the Yangtze River Channel League's moderate faction; Hwang Chung, his senior and Uncle Hwang, was the League elder and Donghu Stronghold Lord who was killed in its destruction.

### Mungyeong.md

# Mungyeong (문경)

- **Safe through:** Chapter 504
- **Aliases:** Killing Ghost
- **Role:** Mungyeong is the legendary physician known as the former Divine Physician and Slaughter Saint, a Returned to Youth Supreme Peak master and the greatest assassin in history who passed the Divine Physician title to his Disciple.
- **Personality:** Compassionate, resolute, resourceful, and calm under extreme pressure.
- **Voice:** His Mungyeong persona is timid, deferential, and cheerful, while his Slaughter Saint voice is dry, impassive, and blunt.
- **Relationships:** Dong Feng is his Disciple, Jeok Cheongang is an old acquaintance whom Mungyeong helped break free of his Heart Demon, and Mungyeong was asked to look after and instruct Jin Taekyung after testing his basics.

### Zhuge Feng.md

# Zhuge Feng (제갈풍)

- **Safe through:** Chapter 504
- **Aliases:** Crouching Dragon Guest
- **Role:** Zhuge Feng is the current Family Head of the Zhuge Clan and father of its Lesser Family Head, Zhuge Gyun.
- **Personality:** Analytical, disarmingly casual, eccentric, and inventive; he treats comfort and time as principles while delivering grave intelligence with unsettling directness.
- **Voice:** Clear, calm, polished, and conversational, with understated humor and pointed questioning.
- **Relationships:** Zhuge Gyun is his son, and Zhuge Gonghu was his grandfather.

## Korean source

```text
＃505화



반로환동(返老還童)은 모든 무림인이 꿈꾸는 경지다.

막대한 공력과 깨달음이 합쳐졌을 때, 인체가 재구성되며 과거의 젊음을 얻게 되는 것이다.

하지만 반로환동이 그리 쉬웠으면 수많은 무림인들이 꿈만 꾸다 죽진 않았을 거다.

이는 하늘의 도움이 없고서야 불가능한 일이었고, 지금 내 옆에는 기나긴 세월 각고의 노력 끝에 바로 그 천운(天運)을 얻은 한 사람이 걷고 있었다.

“제갈세가, 집합.”

타오르는 듯한 붉은 머리카락이 바람에 흩날린다.

탄력 있는 근육으로 이루어진 단단한 체구와 칠 척에 달하는 키. 목소리는 쇠몽둥이처럼 묵직했다.

‘……진짜 적응 안 되네.’

사람이 달라도 이렇게 달라질 수가 있나.

쳐다볼수록 기분이 이상해지는 건 어쩔 수 없다.

내가 알고 있던 화왕(火王) 적천강은 오척단구에 더 늙기도 어려울 만큼 나이든 노인이었지, 기껏해야 40대 중후반으로 보이는 몸짱 중년인이 아니었으니까.

그런 내 시선을 눈치챈 적천강이 걷다 말고 작게 중얼거렸다.

“왜, 왜 또.”

“아니, 그렇잖아요. 진짜 어떻게 이러지? 이거 몇 살 때 모습이에요?”

“환갑 전이었을 거다. 물론 머리카락의 색은 단 한 번도 붉었던 적이 없지만.”

“도대체 어떻게 늙으셨던 겁니까? 나이가 먹으면 키가 줄어드는 거야 당연하긴 한데…… 혹시 팔순쯤에 누구한테 다리 잘리신 적 있어요?”

“잘린 적은 없고. 아까부터 거슬리게 나불대는 어느 놈 다리라면 자를 수 있을 것 같긴 하다.”

나를 향해 눈을 부라리던 적천강이 문득 입맛을 다셨다.

“어쨌건 그렇게 쳐다보지 마라. 노부도 아직 어색하니까.”

“노야 본인도 어색한데, 아니. 노야라고 부르기도 뭐하네.”

“그럼 뭐라고 부르겠느냐?”

“아저씨?”

“…….”

“어이, 적 씨?”

“……뒈지고 싶으냐?”

다행이다. 말투 살벌한 거 보니까 적천강 맞네.

묘한 안도감을 느끼는 사이, 어느새 가까워진 익숙한 얼굴들은 의아한 표정으로 나와 적천강을 바라보고 있었다.

“으응?”

“조장님, 옆에 계신 분은 누구십니까?”

지극히 정상적인 반응이다. 하지만 모든 사정을 알고 있는 문경과 몇몇 사람은 달랐다.

“마, 막내야.”

“어어, 은인. 혹시 옆에…….”

진위경과 청풍. 이 두 사람은 사태 파악이 빨랐다.

진위경은 언제나 평정심을 유지하며 정황을 파악하는 사람이었고, 청풍은 이들 중 문경 다음으로 강한 초절정 고수이니 짐작해도 이상한 일은 아니었다.

그리고 마지막 남은 한 사람, 제갈풍이 무거운 눈빛으로 나를 응시했다.

“적발(赤髮)에 적염(赤髥)이라. 내가 보고 받은 바에 의하면 지금까지 이곳에 출입한 이들 중 저런 특색 있는 생김새의 무인은 없었지. 특히 신경 쓰이는 점은 자네와 나란히 오는 것으로 보아 상당히 친밀한 관계인 것 같은데, 자네는 친구가 없지 않나.”

“……상당히 열 받긴 하는데 틀린 말은 아니네. 그래서요?”

“하여 내 명석한 두뇌로 추측한 바에 의하면, 자네 옆에 있는 저 무인은 혹 반로환동 한 적 노선배가 아닌가 하는 생각이 드는데…… 하하, 어떤가. 제법 그럴듯한 헛소리 아닌가?”

“맞는데요.”

“아닐세. 헛소리야.”

“아니긴 뭐가 아냐. 맞다니까요.”

“헛소리라고 해 주게. 제발.”

“맞다.”

이번 대답은 내가 한 것이 아니다. 짧고 굵은 한마디와 함께 앞으로 나선 적천강의 모습에 주위의 공기가 크게 요동쳤다.

“헉!”

“바, 반로환동이라니.”

“그럼 정녕 저자의 정체가……!”

임시로 세운 나루터 주위에는 이곳을 지키고 조사하기 위해 파견된 무당과 제갈세가의 무인들이 한 트럭이었다.

거기에 더해 우리를 밖으로 데려다줄 선화아 무송과 수룡채의 수적들까지.

주위의 모두가 눈을 부릅뜬 상황에서, 제갈풍의 동공이 흔들렸다.

화왕이 왜 거기서 나와……?

눈동자에 딱 그렇게 쓰여 있다. 사람들의 동요 속, 말없이 적천강을 바라보던 제갈풍이 공손하게 포권을 올렸다.

“노선배님을 뵙습니다. 혹여 무슨 일이 있으신가 싶어 제가 얼마나 노심초사했는지…….”

“왜 마교 놈들이 그 많은 길을 놔두고 구화산에 왔나 했더니, 그런 이유가 있었구나.”

칼 같은 어조에 제갈풍이 어색하게 웃었다.

“무슨 말씀이신지.”

“한 번만 더 모르는 척했다가는 좋은 꼴 못 본다.”

“……혹시 어디서부터 들으셨는지 여쭤봐도 되겠습니까?”

“지혜롭고 현명하신 조부님의 판단이 아니었다면, 부터.”

“음. 다 들으셨군요.”

“다 들었지.”

“만약 제가 한 말이 모두 오해라고 말씀드린다면…….”

“제갈세가에 불을 싸질러 버려야지.”

“아앗…….”

“어쩐지 그 개 같은 마교도 놈들이 그 많은 길을 놔두고 왜 이리 오나 했다.”

적천강은 스산한 눈빛으로 주먹을 말아 쥐었다.

오늘내일할 것 같던 할배 시절에도 저런 눈빛을 하면 모두가 꼬리를 내렸는데, 회춘까지 해 버렸으니 그 기세에 오금이 저릴 지경이다.

“낮잠 자다가 일어났더니 구화산이 타고 있더라. 이 문제에 대해 어찌 생각하느냐?”

“좋지 않다고 생각합니다.”

“그리고?”

제갈풍이 마른 침을 꿀꺽 삼켰다.

“심기가 불편하셨으리라 사료됩니다.”

“참으로 개 같았지. 황급히 달려가지 않았다면 노부의 거처까지 잿더미가 되었을 거야.”

“거처는 무사했군요. 다행입니다.”

“거처 빼고 다 탔다. 노부의 마음도.”

“아아앗.”

“자, 이제 두 가지 선택지를 주마.”

적천강이 손가락 하나를 펼치며 말을 이었다.

“첫째. 노부가 제갈 성을 쓰는 놈들을 모조리 붙잡아 일오횡대로 나란히 세워 놓고 귀싸대기를 갈기는 것.”

내가 그거 장관이겠는데, 라고 생각할 때 제갈풍이 숨도 쉬지 않고 대답했다.

“두 번째 제안을 받아들이겠습니다.”

“그게 뭔지 알고?”

“뭐든 간에 두 번째로 하겠습니다.”

이건 나 같아도 2번 고른다.

무림인이 목숨만큼이나 중요하게 생각하는 것 중 하나가 바로 자존심이다.

화왕 적천강한테 식솔 전체가 줄 싸대기 맞았다는 소문이 퍼지면 그 문파는 그날부터 현판 내려야 한다.

아무리 오대세가의 일원인 제갈세가라 해도 예외는 아니다.

그런 의미에서 보자면 제갈풍의 선택은 현명했다. 하지만 일말의 불안감은 제아무리 그라도 어쩔 수 없었다.

“한데, 무엇입니까?”

“노부의 두 번째 제안 말이냐?”

적천강이 짧게 나 있는 붉은 턱수염을 어루만졌다. 나를 포함한 이 자리의 모두를 천천히 눈에 담은 그가 한 마디를 툭 내뱉었다.

“앞으로 잘해라.”

“노 선배님. 죄송하지만 정확히 그게 무슨…….”

“이미 전란은 시작되었다. 그러니 정마대전 때 제갈세가가 해 왔던 것만큼, 아니 그 이상으로 잘하란 말이다. 네 조부처럼.”

“……!”

“뭐, 따지고 보면 네놈 조부가 마교도와 결탁해서 구화산에 불 지르라고 시킨 것도 아니고. 이미 죽어 땅에 묻힌 놈에게 화내는 것도 우습지. 무덤까지 찾아가서 도로 뒤엎어 버릴 수 없는 노릇 아니냐.”

적천강이 나를 바라보며 말을 이었다.

“그리고, 그날 마교도 놈들이 구화산에 불을 지르지 않았다면 다른 인연도 만들어지지 않았……. 그런데 네놈은 왜 표정이 그 모양이냐?”

나는 황급히 표정을 수습하며 대답했다.

“평소 그대로인데요.”

“……짚이는 게 없지 않지만 넘어가 주마.”

사실 전대 가주의 무덤에 찾아가서 오줌이라도 갈길 줄 알았다고 대답하면 적천강이 날 죽이려 들 거다.

다른 사람들 표정을 보아하니 나 혼자만의 생각은 아니었던 모양이고.

‘그래도 이렇게까지 생각해 주고. 살짝 감동인데.’

적천강의 말마따나, 그가 구화산의 은거기인으로 남아 있었다면 지금 우리가 함께 하는 일도 없었을 것이다.

서로의 존재를 모른 채, 각자의 세상에서 살아가고 있었겠지.

하지만 운명의 시계추는 나를 무림으로 인도했고, 적천강과 이어 주었다.

그리고 이 또한 운명일지는 모르나, 우리는 다시 한번 다음 장소를 향해 나아가야 한다.

‘하남(河南).’

그 한 단어가 뇌리를 가득 채운 그 순간.

시종일관 알 수 없는 표정으로 홀로 떨어져 있던 문경이 불쑥 입을 열었다.

“해가 질 모양입니다.”

어느새 붉게 물든 서산(西山).

그리고 서산보다 붉게 물든 머리카락을 한 적천강이 나를 향해 씩 웃어 보였다.

“이제 가자꾸나.”

“예.”

그래, 가자.

하남으로. 신(新) 무림맹으로.



* * *



“그래, 모두 떠났다고?”

먼저 입을 연 것은 청수한 인상의 노도사였다.

검버섯 하나 피지 않은 피부는 젊은이처럼 팽팽했고, 길게 늘어트린 도포 자락은 눈부시게 희었다.

노도사에게 새로운 소식을 가져온 이 역시 늙기는 매한가지였지만, 누덕누덕 기운 옷차림은 그의 소탈한 성품을 증명하는 것 중 하나였다.

달칵.

찻잔을 내려놓은 남루한 차림의 도사, 현공진인이 대답했다.

“예, 장문 사형.”

어릴 적부터 한 스승 밑에서 동문수학하던 두 소년은 어느덧 존경받는 진인이자 무당파의 기둥이 되어 있었다.

그저 무공만을 좋아했던 현공진인은 초절정의 경지에 올라 명성을 떨쳤고, 그보다 일곱 살이 많았던 사형은 스승의 뒤를 이어 대 무당파의 장문인이 되었다.

바로 그가 청수한 인상의 노도사, 현천진인(賢天眞人)이었다.

“떠나기 전 꼭 한번 만나고 싶었거늘.”

안타까움이 담긴 사형의 뇌까림에 현공진인이 대답했다.

“어쩔 수 없는 일이지요. 장문 사형께서도 만나기 싫어 저를 대신 보내신 게 아니니.”

“그건 그렇지만, 아쉬운 건 어쩔 수 없구나. 태원진가와 화산파가 자랑하는 이룡(二龍)도 그렇지만, 적 선배께서도 깨달음을 얻으셨다니 꼭 뵈었어야 했는데. 허어.”

“하하, 너무 아쉬워하지는 마십시오. 곧 다시 뵙게 될 것입니다.”

“그래, 그렇겠지. 이 서신의 내용이 사실이라면 말이야.”

현천진인은 탁자 위에 놓인 서신을 지그시 내려다보았다.

서신이 들어 있는 봉투의 겉면에는 용사비등한 필체로 이렇게 적혀 있었다.

무림맹(武林盟).

고작 세 글자에 불과하지만, 이에 실린 무게는 두말할 것 없이 무겁다.

무림맹은 정파 무림 그 자체를 상징하는 권위이며, 정마대전과 버금가는 전란이 다가왔다는 증거이기도 했다.

‘정녕…… 이리 시작되는가.’

현천진인의 표정은 무거웠다. 과거 정마대전에 피를 흘리며 쓰러져간 수많은 사형제들의 비명이 노도사의 귓가를 스치는 듯했다.

젊은 시절 겪었던 끔찍한 기억이 반복되려 하고 있었다.

‘불초 제자, 이제야 스승님의 마음을 알 것 같습니다.’

현천진인이 오래전 정마대전에서 입은 부상을 이기지 못해 명을 달리한 스승을 떠올리고 있던 바로 그 순간이었다.

“자, 장문인!”

전각 밖에서 들려오는 다급한 외침.

이상함을 느낀 현천진인이 소매를 내젓자 부드럽게 쏘아진 한 줄기 경력(經力)이 전각의 문을 열어젖혔다.

익숙한 얼굴을 발견한 현공진인이 미간을 좁혔다.

“너는…….”

다급한 외침의 주인은 무당파의 이대 제자로, 추격대에 포함되어 살귀(殺鬼)를 쫓던 이였다.

거친 숨을 몰아쉬는 이대 제자를 바라보던 현공진인이 문득 눈을 크게 떴다.

“설마?”

“예, 놈을 잡았습니다.”

“그거 잘 되었구나! 천인공노할 만행을 저지르던 살귀를 드디어…….”

기뻐하던 현공진인이 말을 멈췄다. 자신과 달리 사형인 현천진인의 얼굴이 심상치 않았기 때문이었다.

그리고 그런 현공진인의 짐작은 정확했다.

어쩔 줄 몰라 하는 이대제자를 말없이 응시하던 현천진인이 나직한 목소리로 말했다.

“살귀를 잡았으니 기뻐해야 마땅하거늘, 네 낯빛이 어둡다. 무슨 일이더냐?”

“그, 그것이.”

“혹, 누가 또 죽거나 다쳤느냐?”

“아닙니다. 그것이 아니라…….”

차마 말을 잇지 못하고 우물쭈물하던 이대 제자가 고개를 숙였다.

“살귀의 시신을 이리 가져오고 있으니, 장문인께서 직접 보고 판단해주심이 좋을 듯합니다.

“이 무슨.”

현천진인의 의문은 그리 오래 이어지지 않았다.

불과 한 식경 뒤, 무당파의 제자들이 옮겨 온 살귀의 실체를 확인한 그는 한참 동안 침묵한 끝에 입을 열었다.

“아무래도…… 하남에 갈 이유가 하나 더 늘었군.”

노도사의 맑은 눈동자에 비친 것은, 짐승도 인간도 아닌 또 다른 무엇이었다.
```

## Final English reading copy

```markdown
# Chapter 505

Returned to Youth was the realm every martial artist in the Murim dreamed of reaching.

When immense internal energy combined with enlightenment, the human body would be reconstructed, granting its owner the youth of the past.

But if Returned to Youth were that easy, countless martial artists would not have died after spending their whole lives dreaming of it.

It was something impossible without Heaven’s help, and walking beside me now was someone who had earned that heavenly luck after years of painstaking effort.

“Zhuge Clan, assemble.”

His blazing red hair fluttered in the wind.

His solid frame was made of taut muscle, and he stood nearly seven feet tall. His voice was as heavy as an iron club.

*…I really can’t get used to this.*

Could a person really change this much?

No matter how long I stared at him, I couldn’t help feeling strange.

The Fire King Jeok Cheongang I knew had been a short, impossibly old man who stood barely five feet tall. He had looked like he could hardly grow any older—not like a fit middle-aged man who appeared to be in his mid-to-late forties.

Jeok Cheongang noticed me staring, stopped walking, and muttered under his breath.

“Why? Why again?”

“No, but seriously. How did this happen? How old were you when you looked like this?”

“I must have been just shy of sixty. Of course, my hair was never red, not even once.”

“How did you get so old, then? I know it’s natural for people to get shorter as they age, but… Did someone cut off your legs when you were around eighty?”

“They weren’t cut off. But if you mean the legs of some bastard who’s been nattering at me since earlier, I might be able to cut those off.”

Jeok Cheongang glared at me, then suddenly smacked his lips.

“Regardless, stop staring at me like that. Even this old man still finds it awkward.”

“Old Master himself finds it awkward, but—no. Calling you Old Master feels weird too.”

“Then what will you call me?”

“Mister?”

“……”

“Hey, Mr. Jeok?”

“……”

“Do you want to fucking die?”

Good. With that murderous way of speaking, he had to be Jeok Cheongang.

As I felt a strange sense of relief, several familiar faces approached and looked between Jeok Cheongang and me with puzzled expressions.

“Huh?”

“Captain, who is the person beside you?”

It was an entirely normal reaction. But Mungyeong and a few others who knew the whole story reacted differently.

“M-my youngest.”

“B-Benefactor. Could the person beside you be…”

Jin Wikyung and Cheongpung grasped the situation quickly.

Jin Wikyung was always the sort of person who remained calm while assessing the circumstances, and Cheongpung was the second-strongest Supreme Peak master among them after Mungyeong. It was hardly strange that they had figured it out.

And then there was the last person, Zhuge Feng, who stared at me with a heavy gaze.

“Red hair and a red beard. According to the reports I received, no martial artist with such distinctive features has entered or left this place until now. What concerns me most is that, judging by the way he is walking beside you, the two of you appear to be quite close. You don’t have any friends, do you?”

“Your words are seriously pissing me off, but you’re not wrong. So?”

“Therefore, using my brilliant intellect, I have reached the conclusion that the martial artist beside you might be Senior Jeok, who has Returned to Youth… Heh. What do you think? Isn’t that a fairly plausible piece of nonsense?”

“He is.”

“No. It’s nonsense.”

“What do you mean, no? I’m telling you it’s true.”

“Please say it’s nonsense. I beg you.”

“It is.”

This time, the answer had not come from me.

With that short, weighty declaration, Jeok Cheongang stepped forward, and the air around us began to tremble.

“Gasp!”

“He’s Returned to Youth?”

“Then could that man truly be…!”

There was a truckload of Wudang and Zhuge Clan martial artists stationed around the makeshift wharf to guard and investigate the area.

On top of that, Ship-Fire Boy Mu Song and the river bandits of Water Dragon Stronghold were there to take us outside.

With everyone around us staring wide-eyed, Zhuge Feng’s pupils shook.

*Why is the Fire King here…?*

That was exactly what his eyes seemed to say.

While everyone else was thrown into an uproar, Zhuge Feng silently looked at Jeok Cheongang, then respectfully raised his cupped hands.

“It is an honor to meet you, Senior. I have been terribly worried, wondering whether something had happened to you…”

“I wondered why those Demonic Cult bastards had come to Mount Jiuhua despite having so many other roads available. So that was the reason.”

At Jeok Cheongang’s razor-sharp tone, Zhuge Feng gave an awkward smile.

“I’m afraid I don’t understand what you mean.”

“Pretend not to know one more time, and you won’t like what happens.”

“May I ask how much you have heard?”

“Starting with, ‘If it hadn’t been for your wise and perceptive grandfather’s judgment.’”

“Ah. So you heard everything.”

“I heard all of it.”

“If I were to say that everything I told you was a misunderstanding…”

“I’ll burn the Zhuge Clan to the ground.”

“Ah!”

“I wondered why those goddamn Demonic Cult bastards had come this way despite having so many roads available.”

Jeok Cheongang slowly clenched his fists, his eyes cold and eerie.

Even when he had looked like an old man who might die at any moment, everyone had backed down whenever he gave them that look. Now that he had Returned to Youth, the force of his aura was enough to make my knees go weak.

“I woke up from my nap and found Mount Jiuhua burning. What do you think of this situation?”

“I don’t think it is a good one.”

“And?”

Zhuge Feng swallowed hard.

“I presume it must have been displeasing.”

“It was fucking awful. If I hadn’t rushed there, even this old man’s residence would have been reduced to ash.”

“Your residence survived, then. That is fortunate.”

“Everything except the residence burned. Including this old man’s heart.”

“Ah!”

“Now, I will give you two choices.”

Jeok Cheongang raised one finger and continued.

“First, I seize every bastard with the Zhuge surname, line them up five abreast, and smack them across the ears.”

*That would be quite a sight.*

While I was thinking that, Zhuge Feng answered without even pausing for breath.

“I will accept the second proposal.”

“Do you know what it is?”

“Whatever it is, I will choose the second one.”

Even I would have picked number two.

One of the things martial artists valued almost as much as their lives was their pride.

If word spread that the entire Zhuge Clan had been slapped in a line by the Fire King Jeok Cheongang, the clan would have to take down its sign from that very day onward.

Even the Zhuge Clan, one of the Five Great Families, would not be exempt.

In that sense, Zhuge Feng had made a wise choice. But even he could not help feeling a trace of unease.

“But what is it?”

“You mean this old man’s second proposal?”

Jeok Cheongang stroked his short red beard. After slowly taking in everyone present, including me, he tossed out a single sentence.

“Do better from now on.”

“Senior, I apologize, but what exactly does that mean…?”

“The war has already begun. So do as well as the Zhuge Clan did during the Great Faction War—no, do even better. Like your grandfather.”

“……!”

“Come to think of it, your grandfather didn’t conspire with the Demonic Cult to order them to set Mount Jiuhua on fire. And getting angry at someone who is already dead and buried is ridiculous. It isn’t as if we can go to his grave and dig it up just to turn it over again.”

Jeok Cheongang looked at me and continued.

“And if those Demonic Cult bastards hadn’t set Mount Jiuhua on fire that day, we would never have formed another connection either… But why do you look like that?”

I hurriedly composed my expression before answering.

“This is my usual expression.”

“……I may have an inkling, but I’ll let it go.”

In truth, if I answered that I had expected him to go to the previous Family Head’s grave and piss on it, Jeok Cheongang would try to kill me.

Judging by everyone else’s expressions, it seemed I was not the only one who had thought of it.

*Still, for him to think this much about it. I’m a little touched.*

As Jeok Cheongang had said, if he had remained a reclusive master in Mount Jiuhua, we would never have ended up working together.

We would have lived in our own worlds, unaware of each other’s existence.

But the pendulum of fate had led me to the Murim and connected me with Jeok Cheongang.

And whether this was fate as well or not, we had to move toward our next destination once more.

*Henan.*

The instant that single word filled my mind, Mungyeong, who had been standing apart with an unreadable expression, suddenly spoke.

“It looks like the sun is about to set.”

The western mountains had already turned red.

And Jeok Cheongang, his hair redder than the western mountains, grinned at me.

“Let’s go now.”

“Yes.”

Right. Let’s go.

To Henan. To the New Murim Alliance.



* * *



“So everyone has left?”

The first person to speak was a refined-looking old Daoist.

His skin was taut and youthful, without a single age spot, and the long hem of his robe was dazzlingly white.

The man who had brought him the news was old as well, but his heavily patched clothes were one indication of his unpretentious character.

Clack.

The shabbily dressed Daoist set down his teacup and answered.

“Yes, Sect Leader Senior Brother.”

The two boys who had studied under the same master since childhood had, before they knew it, become respected Perfected Beings and pillars of Wudang.

Perfected Being Hyeongong, who had loved nothing but martial arts, had reached the Supreme Peak realm and made a name for himself. His Senior Brother, seven years older than him, had succeeded their master and become the Sect Leader of the great Wudang Sect.

He was the refined-looking old Daoist, Perfected Being Hyeoncheon.

“I wanted to meet them at least once before they left.”

At his Senior Brother’s regretful mutter, Hyeongong answered.

“It could not be helped. It was not as if you sent me in your place because you did not wish to meet them.”

“That is true, but I cannot help regretting it. The Two Dragons whom the Jin Family of Taiyuan and Huashan boast of are one thing, but I heard Senior Jeok gained enlightenment as well. I truly should have met him. Sigh.”

“Haha. Please do not regret it too much. We will see him again soon.”

“Yes, I suppose we will. If the contents of this letter are true.”

Hyeoncheon stared down at the letter resting on the table.

Written across the outside of the envelope in a bold, soaring hand were three characters:

**Murim Alliance.**

It was only three characters, but the weight they carried was beyond question.

The Murim Alliance represented orthodox Murim itself. It was also proof that a war rivaling the Great Faction War was approaching.

*Is it truly… beginning like this?*

Hyeoncheon’s expression was heavy.

It seemed as though the screams of the countless Senior and Junior Brothers who had fallen bleeding during the Great Faction War were brushing against the old Daoist’s ears.

The horrific memories he had experienced in his youth were about to repeat themselves.

*This unworthy Disciple finally understands your heart, Master.*

Hyeoncheon was thinking of the master who had died after failing to overcome the injuries he had suffered during the Great Faction War when—

“S-Sect Leader!”

A desperate shout rang out from outside the pavilion.

Hyeoncheon sensed something strange and flicked his sleeve. A soft stream of internal force shot out and flung open the pavilion door.

Hyeongong recognized the familiar face and furrowed his brow.

“You…”

The owner of the desperate cry was a second-generation Wudang Disciple who had been included in the pursuit party chasing the Killing Ghost.

As Hyeongong looked at the second-generation Disciple, who was breathing heavily, his eyes suddenly widened.

“Could it be?”

“Yes. We caught him.”

“Well done! You finally captured the Killing Ghost, who committed such heinous atrocities—”

Hyeongong stopped speaking.

Unlike his own delighted expression, his Senior Brother Hyeoncheon’s face was grim.

And Hyeongong’s suspicion was exactly right.

Hyeoncheon silently stared at the second-generation Disciple, who seemed not to know what to do, then spoke in a low voice.

“We should be celebrating now that the Killing Ghost has been captured, yet your expression is so dark. What happened?”

“Th-that is…”

“Did someone else die or get injured?”

“No. It is not that…”

The second-generation Disciple lowered his head, unable to continue.

“We are bringing the Killing Ghost’s remains here now. I believe it would be best if you saw them and judged for yourself, Sect Leader.”

“What is this supposed to—”

Hyeoncheon’s question did not remain unanswered for long.

Half an hour later, after confirming the true form of the Killing Ghost, whose remains had been carried over by Wudang Disciples, Hyeoncheon remained silent for a long while before finally speaking.

“It seems… I have one more reason to go to Henan.”

Reflected in the old Daoist’s clear eyes was something else entirely—neither beast nor human.
```

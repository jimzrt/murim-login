<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0499.txt",
      "sha256": "b4bc1a4b28110eff85cf8e1c6dfcfc482f776253c8a75c680209200e348e4b9d",
      "bytes": 13259
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "58de626e962e63aa87e475ba5d487a9cdc9fcbbeea7237aae7adf7fab623692b",
      "bytes": 5392
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "4a651a248cb681497ac38d974a9c8f2da2b209a7f3d1b2918004456e2b3e5b73",
      "bytes": 158590
    },
    {
      "path": "characters/Cheol Mubaek.md",
      "sha256": "11199bdbb0a06381e02a0ec16b87b6e5514f78930fe4695465b0c70e93f70644",
      "bytes": 1041
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "96d714776ad9c88f7985ca53c6a5fc6996da9f2a0350eca2940d4c71d2f630eb",
      "bytes": 1006
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "496d1d0fc795ad96739d353b5accb3613b3bf0ecaca41c893e5bde28c10ef307",
      "bytes": 553
    },
    {
      "path": "characters/Jang Taebo.md",
      "sha256": "7416e10e58d987e559b34a9d07cd963824753069a6cfb05668c6ad3c5b9523f6",
      "bytes": 792
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "700568ae4e4f78b0124bbf7819dd2862a6df1a59d3805d6a1c0f1c12da98dd21",
      "bytes": 1547
    },
    {
      "path": "characters/Jin Mukyung.md",
      "sha256": "d33aae1b3c2691a74478cac70107d0cddbe0dfe0ed0f367564f74d9f3724d409",
      "bytes": 2161
    },
    {
      "path": "characters/Jin Wikyung.md",
      "sha256": "422a51c9c6b048488742a0a17dee73448a8b0bed32a0e8157e91eb695e4f64fe",
      "bytes": 1239
    },
    {
      "path": "characters/Lee Seowol.md",
      "sha256": "c9c3b6431696bc404fbd9deadcf27e4911d1d8d483606f8be82e13f4106a3dad",
      "bytes": 1562
    },
    {
      "path": "characters/Pung Yang.md",
      "sha256": "89eabfa40955030cc71dbfefb107ced68aad2cfb6015eb4f7aa6b73d7cc86309",
      "bytes": 1446
    },
    {
      "path": "characters/Wipeng.md",
      "sha256": "3c8e3bb9798fc3534d9610d2767f3822c2a22243bd7d9797bd1a371d441be928",
      "bytes": 954
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "eebb6a55d417a0bf58918cb43c8dd3bd0a4d194812edee7631ef94a7e3eedbb2",
      "bytes": 153941
    }
  ],
  "estimated_tokens": 14534
}
-->

# Durable State Update — Chapter 499

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 499. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 499. Profile updates may replace only one
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
  "chapter": 499,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 499,
    "continuity_sources": [499],
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
    "The Zhuge Clan has sealed the exposed Gate gap with a formation, but whether this is a fundamental or permanent solution remains unresolved; the Gate's residual mana previously mutated local life.",
    "Around one hundred Level 5 Mutated Minnows, locally called Blood Fish, were captured in the Gate's entrance waterways; the remaining population is unknown, and the fish kill one another.",
    "Taekyung suspects Dark Heaven's regeneration, teleportation, and Moving Formation are manifestations of Magic connected to the Gate.",
    "Taekyung told Jeok that he came from another world, that an evil force from it is linked to Dark Heaven, that the corrupted imugi was their work, and that a fully opened Gate could release monsters.",
    "Honglan corrupted the benevolent Dongting Lake imugi and used it to kill many people; the severely injured Dongting Fisherman may be connected to Dark Heaven and the earlier destruction inside the secret refuge.",
    "The Southern Heaven Demon Empress is traveling toward Yunnan and expects to cause further deaths.",
    "Jin Wikyung and Gung Gibang pledged the Jin Family of Taiyuan and the Beggars' Sect to Taekyung's defense; Jin Wikyung has now arrived with the Jin Dragon Squad, Wipeng, and Jang Taebo.",
    "Jeok's innate qi is damaged and steadily diminishing despite the Thousand-Year Snow Ginseng and the Divine Physician's treatment; Taekyung remains uncertain whether Jeok recovered without lasting aftereffects.",
    "Mungyeong is the Slaughter Saint, a Returned to Youth Supreme Peak master and the greatest assassin in history; before becoming the Slaughter Saint, he was called Killing Ghost, and he saved countless people as the Divine Physician. He once belonged to the vanished assassin sect Salcheonmun and taught several assassins there, none of whom are believed alive.",
    "Mungyeong recognizes Taekyung's Heavenly Martial Physique as innate and distinct from Cheongpung's more refined physique.",
    "After seven days and nights of poisoned tests, Taekyung evaded Mungyeong's blinding final sword stroke and demonstrated the basics Mungyeong sought; Mungyeong intends to teach him secret martial arts without a formal Master-Disciple relationship.",
    "Taekyung completed the tests, gained EXP, points, Poison Resistance, sharper Qi Sense, and a clue to enlightenment, while retaining the Water God Dragon's dismantled materials and Origin Essence after the permanent loss of 5 Strength and 5 Agility from Sinews and Meridians damage."
  ],
  "continuity_sources": [
    498,
    497
  ],
  "open_questions": [
    "Will Zhuge Feng's formation permanently seal the Gate gap, and what lies beyond it if the Gate is reopened?",
    "What is the Lord of Heaven's identity, and how is he connected to the dangerous force Taekyung associates with his original world?",
    "Where is the Southern Heaven Demon Empress ultimately headed, and what does she intend to do in Yunnan?",
    "What is the Dongting Fisherman's exact role within Dark Heaven, and how was he connected to the earlier destruction inside the secret refuge?",
    "Has Jeok fully recovered from the Formless Ultimate Poison, and will Taekyung use the Water God Dragon's Origin Essence to aid him?"
  ],
  "safe_through": 498,
  "temporary_decisions": [
    "Render 산공독 as Energy-Dispersing Poison, 강력한 산공독 as Potent Energy-Dispersing Poison, 칠보추혼산 as Seven-Step Soul-Chasing Powder, 강력한 칠보추혼산 as Potent Seven-Step Soul-Chasing Powder, 심각한 복통 as Severe Stomachache, 고기 방패 as Meat Shield, 독 장아찌 as Poisoned Pickle, and 독의 as Poison Physician; retain secret martial arts, Master-Disciple relationship, Killing Ghost, and Fake Murim Martial Artist, and preserve 악 as Agh in the Quest interface; render 실명산 as Blindness Powder, 살천문 as Salcheonmun, and 스승의 날 as Teacher’s Day.",
    "Render 기억의 파편 as Memory Fragment, 게이트 공략 as Gate Conquest, 텔레포트 as Teleport, 마법 as Magic, 혈어 as Blood Fish, and 변이된 송사리 as Mutated Minnow; render 강력한 마비산 as Potent Paralysis Powder, 강력한 미혼산 as Potent Soul-Bewitching Powder, 전신 마비 as Full-Body Paralysis, 독성 흡수 as Poison Absorption, and 해독 as Detoxification.",
    "Render 시산혈해 as sea of corpses and blood and retain Old Master for 노야 with the established rough, profane Taekyung-Jeok banter; render 해시 as hour of the Pig, 한 식경 as half an hour, 타구봉 as Dog-Beating Staff, 창룡 as Azure Dragon, and 무량수불 as Infinite Life Buddha; preserve geun as the traditional weight unit with a footnote.",
    "Render 선천지기 as innate qi, 진원진기 as true-origin qi, and 천기 as heavenly patterns.",
    "Render 심마 as Heart Demon, 비급 as martial arts manual, 송문고검 as Pine-Pattern Ancient Sword, 반로환동 as Returned to Youth, 강강수월래 as Ganggangsullae, 생사부 as Book of Life and Death, 기막 as qi curtain, 무극태을검 as Martial Extremity Grand Unity Sword, 이룡 as Two Dragons, 원정 as Origin Essence, 내단 as inner core, 영험한 기운 as sacred energy, 대호 as great tiger, 취팔선권 as Drunken Eight Immortals Fist, 귀면 as Ghost Face, 요단강 as Jordan River, and 진룡 as Jin Dragon."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진위경    | **Jin Wikyung**    |
| 진무경    | **Jin Mukyung**    |
| 위팽     | **Wipeng**         |
| 이소월    | **Lee Seowol**     |
| 철무백    | **Cheol Mubaek**   |
| 적천강    | **Jeok Cheongang** |
| 청풍     | **Cheongpung**     |
| 검성     | **Sword Saint**               | Mae Jonghak    |
| 혈랑검    | **Blood Wolf Sword**          | Lee Cheonbaek  |
| 항산호    | **Tiger of Mount Heng**       | Cheol Mubaek   |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 무당파    | **Wudang**                       |
| 암천     | **Dark Heaven**                  |
| 십봉룡    | **Ten Dragons and Phoenixes**    |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 영약     | **elixir**                                       |                                                       |
| 비무     | **duel** / **spar**                              | Formal non-lethal martial contest                     |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 문주     | **Sect Leader**                              |
| 제자     | **Disciple**                                 |
| 시스템              | **System**                     |
| 퀘스트              | **Quest**                      |
| 보상               | **Reward**                     |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 하남     | **Henan**              |
| 사천     | **Sichuan**            |
| 항산     | **Mount Heng**         |
| 화산     | **Huashan**            |
| 구화산    | **Mount Jiuhua**       |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 공자      | **Young Master**                                                |
| 소저      | **Young Lady**                                                  |
| 도사      | **Daoist**                                                      |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 장태보 | **Jang Taebo** | Former Guild Leader of the Ironcraft Guild; now lives near Jeongyang and is sought as a Master Artisan. |
| 풍양 | **Pung Yang** | Personal name of the Red Wind Band Leader. |
| 공청석유 | **gongcheong seokyu** | Rare martial-arts elixir; the term also creates a petroleum pun. |
| 적풍단 | **Red Wind Band** | Rising mounted-bandit power from the northern plateau. |
| 소월 | **Seowol** | Short form of Lee Seowol used by Cheol Mubaek. |
| 문주님 | **Sect Leader** | Honorific title Lee Seowol orders the senior figures to use. |
| 벽곡단 | **fasting pills** | Food-substitute pills found in the hidden cave where Cheol trained. |
| 만년한철 | **Ten-Thousand-Year Cold Iron** | Material that destroys Pung Yang's Body-Protecting Qi when the Unnamed Sword satisfies a specific condition. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 주신 | **God of Drinking** | Wipeng's drinking epithet. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 청석 | **bluestone** | Extremely hard stone used for the training-ground floor. |
| 수련동 | **training hall** | Building located roughly two hundred jang from the training ground. |
| 명장 | **Master Artisan** | Master craftsman capable of handling Ten-Thousand-Year Cold Iron |
| 철기방 | **Ironcraft Guild** | Hubei guild composed mainly of skilled craftsmen and closely associated with the Nine Sects and One Gang. |
| 불로초 | **Herb of Eternal Youth** | Spirit herb said to grant eternal youth and immortality. |
| 여의주 | **dragon pearl** | Legendary treasure requested by Jang Taebo. |
| 성라대연 | **Star-Array Grand Banquet** | Major martial gathering held in Henan every two or three years. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 노야 | **Old Master** | Taekyung's private address for Jeok Cheongang. |
| 호북 | **Hubei** | Province on Ju Gongsan's route from Guangdong to Henan. |
| 이무기 | **imugi** | Legendary serpent mentioned as the only comparable creature to a Thousand-Year Poison Horned Snake. |
| 동정호 | **Dongting Lake** | Lake under which Dangyang and Honghu Strongholds operated. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 위팽 | 진위경 | retainer_to_lord | my lord | deferential | 주공; Wipeng is Jin Wikyung’s personal guard. |
| 진무경 | 진위경 | younger_to_older_brother | older brother | formal-but-blunt | Mukyung refers to Wikyung as 형 while remaining emotionally restrained. |
| 진위경 | 진무경 | older_to_younger_brother | little brother | affectionate-casual | Wikyung uses 아우야 and 무경아 with openly affectionate familiarity. |
| 소월 | 철무백 | niece_to_paternal_uncle | Uncle Cheol | familiar-polite | Lee Seowol asks Cheol Mubaek to suppress his heat because she cannot breathe. |
| 철무백 | 소월 | paternal_uncle_to_niece | Seowol | affectionate-familiar | Cheol Mubaek speaks gently to Seowol and says protecting her is his duty. |
| 풍양 | 철무백 | junior_to_older_martial_peer | Senior Cheol | polite and taunting | Pung Yang repeatedly addresses Cheol as 철 선배 while provoking him. |
| 진무경 | 풍양 | challenger_to_bandit_leader | Pung Yang | challenge-shout | Mukyung calls out Pung Yang by name to begin the confrontation. |
| 풍양 | 이소월 | captor_to_coerced_bride | Young Lady | polite and coercive | Pung Yang addresses Seowol as 소저 while threatening her subordinates and demanding marriage. |
| 풍양 | 진무경 | enemy_to_enemy | you / little brat | condescending and taunting | Uses 네놈 and 어린놈 while threatening to sever Mukyung's limbs. |
| 무인 | 이소월 | sect_subordinate_to_sect_leader | Sect Leader | formal-deferential | Surviving Mount Heng martial artists address Seowol by her title during the casualty search. |
| 진무경 | 이소월 | junior_to_sect_leader | Sect Leader | formal-polite | Uses 문주 while greeting Lee Seowol. |
| 철무백 | 진무경 | senior_martial_peer_to_younger_martial_artist | Heaven Shaking Sword | affectionate-teasing | Uses 우리 진천검 while warmly inviting Mukyung to return. |
| 진위경 | 위팽 | lord_to_personal_guard | you | formal-but-familiar | Uses 자네 while assigning Wipeng the banner-preparation task. |
| 위팽 | 진무경 | Jin Family retainer to Second Young Master | Second Young Master | deferential and blunt | Uses 이공자 while directing Mukyung to wash before the guest's arrival. |
| 청풍 | 진무경 | young_martial_artist_to_renowned_senior_martial_artist | Young Hero Jin Mukyung | deferential and excited | Cheongpung calls him 진천검 진무경 소협 and later 진 소협 while seeking his duel. |
| 진무경 | 청풍 | senior_martial_artist_to_newly_met_young_martial_artist | Young Hero | deferential and expectant | Mukyung addresses Cheongpung as 소협 while asking whether Great Hero Mae descended from Huashan. |
| 장태보 | 청풍 | elder_smith_to_young_martial_artist | you / lunatic | gruff and incredulous | Initially treats Cheongpung as a lunatic despite recognizing him as Mae Jonghak's disciple. |
| 적천강 | 장태보 | strangers; visiting elder to local smith | Old Man Jang | blunt and familiar | Uses 장 노인 while confirming Jang Taebo’s identity. |
| 적천강 | 청풍 | overwhelming_elder_to_young_martial_artist | you / little punk | blunt, amused, and threatening | Jeok Cheongang uses 네, 이놈, and related blunt forms while testing Cheongpung. |
| 청풍 | 적천강 | young_martial_artist_to_overwhelming_elder | Grandpa Jeok | casual-familiar despite deference | Cheongpung uses 적 할아버지 while asking Jeok Cheongang to confirm Taekyung's condition; this is a familial form of address, not literal kinship. |
| 위팽 | 청풍 | Jin Family retainer to visiting Huashan martial artist | Young Hero Cheongpung | formal-polite and worried | Uses 청 소협 while warning that Cheongpung's refusal of the Sect Leader's order could strain relations between the Jin Family and Huashan. |
| 진위경 | 이소월 | host_to_new_sect_leader | Young Lady | formal-polite | Jin Wikyung addresses Lee Seowol as 소저 before accepting her oath. |
| 이소월 | 진위경 | new_sect_leader_to_lesser_family_head | Lesser Family Head | formal-deferential | Lee Seowol refers to Jin Wikyung as 소가주님 when describing his summons. |
| 철무백 | 진위경 | sect_elder_to_lesser_family_head | Lesser Family Head | formal-deferential | Cheol Mubaek formally greets Jin Wikyung as the Lesser Family Head of the Jin Family of Taiyuan. |
| 무인 | 진위경 | vassal_martial_artist_to_lesser_family_head | Lesser Family Head | formal-deferential | The Mount Heng martial artists greet Jin Wikyung as 소가주님 while pledging loyalty. |
| 진위경 | 적천강 | host_to_legendary_guest | Great Hero Jeok | formal-deferential | Introduces himself and pays respects to Jeok Cheongang as the Fire King. |
| 적천강 | 진위경 | elder_to_younger_family_head | you | gruff and teasing | Uses 자네 while mistaking Wikyung for Taekyung’s father and questioning his age. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 진위경 | 막내 | older brother to younger brother | my youngest | intimate and informal | Jin Wikyung uses 막내야 affectionately for Jin Taekyung. |
| 진위경 | 장태보 | Lesser_Family_Head_to_elder_smith | Old Master Jang | respectful and formal | Wikyung thanks Jang for coming. |
| 장태보 | 진위경 | elder_smith_to_Lesser_Family_Head | Lesser Family Head | respectful and deferential | Jang speaks with formal respect to Wikyung. |

## Listed compact profiles

### Cheol Mubaek.md

# Cheol Mubaek (철무백)

- **Safe through:** Chapter 187
- **Aliases:** Tiger of Mount Heng
- **Role:** Ninth-generation successor of the Shura Annihilating Fist and Peak master known as the Tiger of Mount Heng; longtime close friend and peer of Lee Cheonbaek; severely injured in battle; entrusted the manual to Lee Seowol and remains her protector
- **Personality:** Fierce, short-tempered, intimidating, and fiercely protective; becomes gentle and attentive toward Seowol
- **Voice:** Roaring and confrontational when rebuking the Mount Heng senior figures; gentle and affectionate when speaking to Seowol
- **Relationships:** Close friend and peer of Lee Cheonbaek; paternal uncle and protector of Lee Seowol; considers Jin Taekyung, Jin Mukyung, and Hyuk Mujin Benefactors for protecting Seowol and enabling the Mount Heng Sword Sect's survival, and vows to repay them even at the cost of his life; feared and respected by the Mount Heng Sword Sect's senior figures

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 494
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, the grandson and Disciple of Sword Saint Mae Jonghak, and a Supreme Peak martial master known as the Huashan Divine Dragon.
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, a deep love of martial arts, competitive pride, unusual resistance to monster-induced Fear, and discomfort when someone copies his martial arts.
- **Voice:** Dreamy and hazy, with innocent, polite phrasing; he has begun imitating Taekyung's profanity.
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions while Taekyung is his only true martial rival; Tang Sadok has temporarily entrusted Mimi to him.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 498
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Jang Taebo.md

# Jang Taebo (장태보)

- **Safe through:** Chapter 498
- **Aliases:** None
- **Role:** Jang Taebo is the former Guild Leader of the Ironcraft Guild and one of the world’s renowned smiths, now a retired master craftsman who forged Taekyung’s White Flame spear.
- **Personality:** Blunt, cantankerous, solitary, and proud; values an untroubled retirement and protects his anonymity, while quietly caring for the neighboring boy Hanga.
- **Voice:** Curt, gruff, and dryly teasing; rejects requests with flat finality.
- **Relationships:** His disciple is the current Guild Leader of the Ironcraft Guild; neighboring boy Hanga is his only conversational partner, and Jang Taebo gives him candy while pretending annoyance.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 496
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin and Furnace Fire Pure Blue, and Jin Taekyung's Master.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Jin Mukyung.md

# Jin Mukyung (진무경)

- **Safe through:** Chapter 443
- **Aliases:** Heaven Shaking Sword; Jin Family Second Young Master
- **Role:** Second son of the Jin Family of Taiyuan; twenty-three-year-old cadet at Heaven’s Gate Temple; a young Peak-level genius swordsman who won the visible exchange with Pung Yang, was then incapacitated by five concealed throwing knives, and survived the battle to recover after Taekyung's intervention; recovered enough from his Internal Injuries to return to the Jin Family of Taiyuan, though he is not yet fully recovered; four days before this chapter, he lost his duel with Cheongpung after roughly three hundred exchanges, secluded himself to train, and sharpened his Sword Energy while resolving to surpass Cheongpung and the other geniuses; he remains secluded in the training hall, subsists on fasting pills, refuses all visitors, and will not return to Heaven’s Gate Temple until he achieves complete mastery; he has learned that Taekyung is leaving with Jeok Cheongang for a year and that Taekyung and Cheongpung plan to attend the Star-Array Grand Banquet in one year.
- **Personality:** Reserved, terse, and easily irritated by exaggerated praise; glares coldly when Taekyung identifies him
- **Voice:** Quiet and resonant; clipped and blunt in direct speech
- **Relationships:** Taekyung’s older brother and current martial arts instructor; returned to the Jin Family after several years away; three years earlier, he flatly refused seven-year-old Zhu Bao’s request for an autograph

### Jin Wikyung.md

# Jin Wikyung (진위경)

- **Safe through:** Chapter 498
- **Aliases:** Junzi Sword
- **Role:** Jin Wikyung is the thirty-six-year-old Lesser Family Head and future Family Head of the Jin Family of Taiyuan, the Alliance Leader who unified Shanxi Murim and Shanxi Province's foremost landowner and magnate.
- **Personality:** Calm, authoritative, and politically capable in public; protective and affectionate toward Taekyung beneath a stern mask. Takes responsibility for his people, acts decisively under pressure, and prioritizes family survival.
- **Voice:** Restrained, formal, and commanding with subordinates; openly affectionate, proud, and occasionally exuberant with Taekyung.
- **Relationships:** Taekyung's eldest brother and future Family Head; Taekyung trusts him as a martial-arts mentor and family protector. Member and acting leader of the Jin Family of Taiyuan. Commands Wipeng and the family's forces. Has worked with Jeok Cheongang, who trained Taekyung under Wikyung's arrangement. Jin Mukyung is his younger brother and a potential successor alongside Taekyung.

### Lee Seowol.md

# Lee Seowol (이소월)

- **Safe through:** Chapter 312
- **Aliases:** None
- **Role:** Eighteen-year-old current Sect Leader of the Mount Heng Sword Sect; third child of Lee Cheonbaek and his last surviving descendant; publicly insists on being addressed as Sect Leader rather than Young Lady; survived Pung Yang's attack with twenty-four other identified survivors; regards the Mount Heng Sword Sect as effectively destroyed but vows to preserve it for those who died defending it; offered the sect's territorial rights to the Jin Family of Taiyuan and proposed marriage to Jin Taekyung in exchange for three Peak martial arts; arrived at the Jin Family on New Year's Day, swore loyalty, and led the Mount Heng Sword Sect into vassalage under the Jin Family; still awaits Taekyung's answer
- **Personality:** Cold, commanding, and composed; capable of stopping a fierce confrontation with a calm request
- **Voice:** Clear and cool, gentle with Cheol Mubaek but frost-cold and firm when asserting her authority
- **Relationships:** Daughter of the deceased Lee Cheonbaek; younger sister of the deceased Young Sect Leader, Lee Seogeun, and Lee Seogwang; Cheol Mubaek's niece and protected charge, to whom he entrusted the Shura Annihilating Fist manual; has proposed marriage to Jin Taekyung in exchange for the Blood Wolf Sword Technique, Blood Wolf Footwork, and Shura Annihilating Fist; during her farewell with Taekyung, she asked him to address her as Young Lady rather than Sect Leader.

### Pung Yang.md

# Pung Yang (풍양)

- **Safe through:** Chapter 268
- **Aliases:** Red Wind Band Leader
- **Role:** Former leader of the Red Wind Band, commanding at least two hundred mounted bandits; became a mounted bandit at thirteen, reached First Rate by age thirty, and rose from squad leader to band leader three years ago; discovered the Crimson Blood martial arts and a case containing five Temporary Strength Pills in a hidden plateau tomb, reached the Peak realm in two years, and could temporarily manifest imperfect Sword Force and powerful Body-Protecting Qi by taking a pill; reached approximately seventy percent mastery of the Crimson Blood Twelve Sabers; after secretly incapacitating Jin Mukyung, resumed killing Mount Heng Sword Sect martial artists; was seriously injured by Taekyung's dagger, defeated One Annihilation, seized Taekyung, and was killed by Taekyung after the Unnamed Sword's Ten-Thousand-Year Cold Iron destroyed his Body-Protecting Qi and pierced his chest; had fled from the steppe and commanded nearly four hundred subordinates before his death
- **Personality:** Foxlike, ruthless, observant, controlled, and willing to kill subordinates who disobey his orders
- **Voice:** Calm, concise, and authoritative when issuing orders
- **Relationships:** Leads the Red Wind Band and controls former members of other mounted-bandit groups who joined his force

### Wipeng.md

# Wipeng (위팽)

- **Safe through:** Chapter 498
- **Aliases:** Ghost Sword; God of Drinking
- **Role:** Jin Wikyung’s personal guard and Commander of the Jin Dragon Squad; one of the Jin Family’s three Peak masters
- **Personality:** Loyal, observant, teasing, capable, and resigned to Jin Wikyung’s impulsive behavior. Respects the dead and urges others to live on their behalf.
- **Voice:** Weary and knowing, with dry humor when addressing Jin Wikyung or Jin Taekyung. Uses Sound Transmission when appropriate.
- **Relationships:** Trusted guard and retainer of Jin Wikyung; a reliable senior ally of Jin Taekyung. He has fought beside the Jin Family in major battles, including the conflict with Mount Heng, and remains alert to threats connected with Dark Heaven. The Human Butcher has claimed him as a personal target in a planned attack.

## Korean source

```text
＃499화



계절은 이미 완연한 봄이었지만, 굽이진 동정호의 물길을 타고 불어온 밤바람은 서늘했다.

두꺼운 천으로 세워진 진위경의 막사 안으로 들어온 장태보는 가장 먼저 화로(火爐) 앞을 차지하고 앉아 몸을 녹였다.

“후우, 이제야 좀 살겠구먼.”

그 모습을 본 진위경이 웃으며 찻잔을 건넸다.

“예까지 오느라 고생 많았소.”

“때마침 하남(河南)에 있었기에 망정이지, 산서(山西)였다면 제아무리 소가주님의 부탁이라 해도 안 왔을 겁니다. 죽을 날만 기다리는 늙은이를 이리 부려먹으시다니.”

나는 장태보의 위협적인 근육을 바라보며 생각했다.

‘충분히 부려먹을 만한데……?’

저 몸 좀 봐라. 이 정도면 정정한 걸 넘어서 짱짱한 거다. 남들이 과로로 수명이 깎여 나갈 때 장태보는 기껏해야 근손실이다.

나와 비슷한 생각을 했는지, 자신의 팔뚝과 장태보의 것을 비교하듯 곁눈질하던 위팽이 입을 열었다.

“사천과 호북에서 있었던 일은 소상히 전해 들었습니다. 혹시나 하는 마음에 하남의 일도 해결할 겸 직접 왔는데, 시기적절한 선택이었군요.”

진위경이 껄껄 웃으며 위팽의 어깨를 두드렸다.

“위팽. 역시 자네는 내 장자방일세!”

“전 무인입니다만.”

“어, 그럼 한신으로 하지.”

“한신은 결국 숙청되지 않았습니까.”

“그럼 소하.”

“소하도 문관 아닙니까.”

“…….”

지금 당장 숙청하고 싶은 표정으로 위팽을 바라보던 진위경이 헛기침을 내뱉었다.

“크흠. 자네, 그동안 내게 쌓인 게 많나 보군.”

일반적인 군신 관계였다면 아이고, 아닙니다. 했겠지만 위팽은 진위경을 대놓고 갈굴 수 있는 거의 유일한 사람이었다.

“예, 많습니다. 모르고 계셨습니까?”

“익히 알고 있었지만 여기까지 찾아와서 이럴 줄은 몰랐지.”

“제가 찾아온 게 아니라 주군께서 부르신 겁니다. 벌써 석 달 가까이 자리를 비우신 건 알고 계십니까? 얼마 전에는 이 문주까지 찾아와 묻더군요. 주군께 무슨 변고라도 생기신 거 아니냐고.”

“커흐흠!”

연신 헛기침을 내뱉는 진위경의 모습을 보니 찔리는 구석이 한둘이 아닌 모양이다.

아니, 잠깐만. 그런데 방금 위팽이 말한 이 문주라는 사람이 설마…….

“혹시 이 소저, 이소월 소저를 말하는 겁니까?”

내 물음에 위팽이 고개를 저었다.

“소저가 아니라, 어엿한 일문(一門)의 문주입니다. 삼 공자.”

“아, 그랬지 참.”

한때 산서성의 패자 자리를 노리던 항산검문(恒山劍門)은 연이은 사건으로 인하여 처참하게 몰락했다.

그러나 혈랑검의 유일한 핏줄이었던 이소월은 내 도움으로 살아남아 태원진가에 충성을 맹세했다.

비록 가신(家臣)의 위치라고 해도 문주는 문주다.

‘마지막으로 본 게…… 벌써 일 년이 넘었나?’

적천강과 함께 태원진가를 떠나 구화산으로 향할 무렵이었으니, 무림에서 흐른 시간으로만 따져도 일 년이고 현대까지 합치면 더욱 길다.

나는 아직도 또렷한 그 날의 기억을 떠올렸다.



‘저기, 이 문주님.’

‘소저요.’

‘네?’

‘소저라고 불러 주세요.’

‘아, 예. 그럼 이 소저.’

‘말씀하세요. 진 공자님.’

‘가내 두루 평안하십시오.’

‘…….’

‘앞으로 문파 사업도 번창하시고, 그 뭐야. 어쨌건 하시는 일마다 모두 잘되시길 바랍니다.’



음. 나름대로 훈훈하게 헤어졌던 것 같다.

내가 기억하는 이소월은 무가의 여식답게 강단도 있고, 적풍단을 이끌고 쳐들어왔던 풍양의 앞에서도 물러서지 않는 사람이니 지금쯤이면 몰락한 항산검문도 제법 성장했겠지.

“그래서, 이 소저는 요즘 잘 지내요?”

잠시 생각하던 위팽이 대답했다.

“잘 지낸다면 잘 지내는 거고, 다른 부분에서는 아닐 수도 있지요.”

“왜요, 일이 잘 안 되나?”

“문파에 관해 물어보신 거라면, 항산검문은 이미 재건을 끝마쳤습니다. 이 문주의 지휘하에 빠르게 성장 중이고 문도의 숫자들도 나날이 증가하는 추세입니다.”

“오.”

“선친의 벗이었던 항산호(恒山虎) 철무백 대협도 은거를 깨고 항산검문의 일에 적극적으로 나서고 있고요.”

“오오.”

그럼 다 잘된 것 같은데?

고개를 갸웃거리는 내 모습에 위팽의 눈이 가늘어졌다.

“삼 공자. 외람되지만 한 가지만 묻겠습니다. 혹시 그 후로 아무런 연락도 안 한 겁니까?”

“연락이요? 무슨 연락?”

“……후. 됐습니다. 못 들은 셈 치십시오.”

이거 어째 분위기가 묘하다. 옆에서 혀를 차는 장태보를 보니 문득 어떤 생각이 뇌리를 스쳤다.

설마? 에이. 아니겠지. 그래도 혹시. 아냐, 그거 아냐.

갑작스럽게 혼란에 빠진 나를 구원한 것은 진위경의 한마디였다.

“이 문주가 잘하고 있다니 다행이군. 그나저나 둘째는 지금 어찌하고 있나? 벌써 몇 달째 보지 못했는데.”

나를 콩벌레 보듯이 쳐다보던 위팽이 한숨과 함께 입을 열었다.

“여전합니다. 수련동에 마련된 벽곡단으로만 끼니를 해결하면서 밖으로는 단 한 걸음도 나오지 않습니다.”

“무경이 그 녀석. 도대체 어찌하려고…….”

진위경의 근심은 괜한 것이 아니다.

내가 구화산으로 향하기 전, 청풍과의 비무에서 패배한 진무경은 그날 이후로 수련동에 처박혀 모습을 드러내지 않았다.

일 년이라는 시간이 흘러 성라대연(星羅大宴)이 열리고, 암천이라는 먹구름이 드리워진 지금에도.

‘허, 대공(大功)을 이루기 전까지는 나오지 않겠다더니.’

한때 천하 무림은 진무경을 천고의 기재라 불렀다.

뛰어난 절기와 영약을 아낌없이 지원받는 구파일방의 적전 제자들조차 그에게 비할 수는 없었고, 진무경은 오래전 몰락한 변방 무가의 핏줄이라는 한계를 딛고 오직 무공만으로 십봉룡(十鳳龍)의 앞줄에 우뚝 섰다.

‘그리고 청풍을 만났지.’

그런 진무경에게 있어 청풍의 존재는 엄청난 충격인 동시에 자극이었을 것이다.

일 년이 훌쩍 지난 지금에도 폐관 수련을 이어가는 것이 바로 그 증거다.

‘반드시 뭔가를 해낼 인간이지. 틀림없어.’

내가 본 진무경은 두말할 필요 없는 천재다.

녀석에게는 검성이라는 지고한 무인의 가르침도, 뛰어난 영약과 절기도 주어지지 않았다.

그럼에도 혼자만의 힘으로 여기까지 왔으니, 폐관을 깨고 나오는 날에는 어떤 모습을 보여 줄지 선뜻 상상이 가지 않았다.

‘문제는 도대체 언제쯤 나오냐는 건데.’

설마 환갑이 다 돼서 나오진 않겠지.

그때까지 벽곡단으로만 버티면 진짜 리스펙하고 형님으로 받들어 모실 의향이 있다.

사실 그 맛대가리 없는 걸 먹으면서 일 년이나 폐관을 이어 온 것만으로도 충분히 대단한 거다.

오죽하면 무당파 도사들도 면벽 수련할 때는 벽곡단 대신 육포 챙겨 간다고 하겠나.

‘고깃집 가서 불판 엎어 버리는 악성 채식주의자들도 벽곡단 한 번 씹으면 바로 삼겹살 찾을 텐데.’

내가 그런 생각을 하는 사이, 이야기의 화제는 어느새 장태보 쪽으로 넘어가 있었다.

“그나저나 소가주, 이제 이 늙은이를 부른 연유를 말해 주시지 않겠습니까?”

장태보의 툴툴거리는 질문에, 진위경이 다짜고짜 한 마디를 툭 내뱉었다.

“철기당(鐵器黨). 어떻소?”

“태원진가 내에 그런 조직이 있다는 말은 처음 들어봅니다만.”

“그럴 거요. 불과 며칠 전 신설된 곳이니까.”

장태보의 미간이 좁혀졌다.

“꽤 익숙한 이름입니다그려. 이 늙은이가 오래전에 몸담았던 철기방 생각도 나고.”

“장 노야를 생각해서 지은 이름이오. 철기당주. 듣기 좋지 않소?”

“소가주님.”

한숨을 내쉰 장태보가 말을 이었다.

“전 이미 오래전에 철기방을 떠난 몸입니다.”

“그렇다면 슬슬 돌아올 때가 된 것 같구려.”

“늙고 지쳐서 망치를 들 힘도 없습니다.”

장태보의 위협적인 근육을 물끄러미 응시하던 진위경이 입술을 달싹였다.

- 막내야.

이쯤 되면 왜 장태보를 여기까지 불렀는지 모를 수가 없다.

이미 진위경의 의중을 눈치채고 있던 나는 등에 메고 있던 백염을 툭 쳐서 떨어트렸다.

터텅!

“어이쿠. 늙고 지쳐서 망치조차 들 힘이 없는 야장이 만든 신병이기를 떨어트리다니!”

“……”

“그토록 다루기 어렵다는 만년한철로 만든 내 창! 누가 만들었는지는 몰라도…….”

장태보가 찢어 죽일 듯한 눈빛으로 나를 노려보았다.

“그만해라.”

“왜요? 어르신 얘기한 거 아닌데.”

“내가 만든 것 아니냐!”

“무슨 소립니까. 망치를 들 힘도 없으신 분이 어떻게 이런 걸 만들어요.”

“……후우. 저 망할 놈.”

땅이 꺼져라 한숨을 내쉰 장태보가 진위경을 바라보았다.

“이러려고 그간 제게 여러 도움을 주신 겁니까?”

“그럴 리가. 아끼는 막내 아우에게 신병이기를 만들어 준 장인에 대한 순수한 호의였소.”

“그럼 제안에 답해 드리지요.”

“경청하겠소.”

“불가(不可). 이게 이 늙은이가 드릴 수 있는 유일한 답입니다. 목에 칼이 들어와도 달라지지 않습니다.”

내가 손을 번쩍 치켜들었다.

“창은요?”

“닥쳐라. 도로 뺏어서 분질러 버리기 전에.”

“만년한철 특. 존나 단단함.”

“……내가 무슨 부귀영화를 누리자고 너 같은 놈에게 창을 만들어 줬을까.”

“그냥 철기당주 하시죠. 우리 쪽에서 이것저것 도움도 받으셨다면서요.”

“재물로 갚고 말지, 이 나이에 또 그런 개고생을 할 것 같으냐?”

“아, 진짜 안 하실 거예요?”

“그럼 어쩔 테냐? 내가 안 하겠다는데.”

“차라리 조건을 알려 주세요. 최대한 맞춰 드릴 테니까.”

“조건?”

장태보의 입가에 문득 득의양양한 웃음이 맺혔다.

“작년 이맘때, 기억하느냐? 그때와 같은 조건을 걸겠다.”

“그때 걸었던 조건이라면, 설마.”

“불로초, 공청석유, 용의 발톱, 여의주. 이중 아무거나 구해 와라.”

띠링.



- 돌발 퀘스트, [어차피 못할 거]가 생성되었습니다!

- 퀘스트 임무 : 장태보가 말한 것 중 하나라도 구해 오기.



터텅, 우당탕!

자리를 박차고 일어난 내가 버럭 외쳤다.

“아니, 그런 게 어디 있어요! 이무기도 아니고 용이라니!”

“이무기든 용이든, 우선 구해 오면 내 태원진가에 뼈를 묻으마. 못 할 거면 가만히 있고.”

띠링.



- 퀘스트 내용이 변경되었습니다.

- 퀘스트 임무 : 이무기의 발톱 구해 오기.



변경된 시스템 창을 확인한 나는 고개를 끄덕였다.

“어, 됐네. 여기요.”

“내 의중은 바뀌지 않으니 헛수고하지 말…… 이게 뭔데 갑자기 주는 것이냐?”

“이무기의 발톱이요.”

“응?”

“이무기의 발톱. 가져오라면서요.”

“……어?”

장태보의 동공에 지진이 일어났다.

천하에서 세 손가락 안에 드는 명장이자 최고의 야장 집단인 철기방의 방주를 역임했던 그다.

이무기의 발톱을 바라보는 장태보의 혼란스러운 눈빛에는 설마 하는 의심과 처음 보는 물질에 대한 경악이 뒤섞여 있었다.

“이, 이무기의 발톱? 정말이냐?”

“길이만 봐도 제 발톱은 아니죠.”

“아, 아니 이걸 도대체 어디서.”

“잡았는데요.”

“뭐?”

“뼈도 있고, 비늘도 있습니다.”

“말도 안 되는 소리!”

“해 뜨면 직접 보러 가세요. 위 대협도 서신으로만 들었을 텐데, 이번 기회에 같이 다녀오시고.”

띠링.



- 돌발 퀘스트, [어차피 못할 거]를 성공적으로 완료했습니다!

- 퀘스트 보상으로 [태원진가]가 [장태보]를 획득했습니다!

- 업적, [와, 이걸 구하네]를 달성했습니다!



경쾌한 시스템 알림과 함께, 진위경이 다정한 손길로 장태보의 어깨를 감싸 안았다.

“앞으로 잘 부탁드리겠소. 철기당주.”

“……!”

태원진가의 전속 도비, 아니 노비로 영입된 장태보의 눈빛은 공허하기 그지없었다.
```

## Final English reading copy

```markdown
# Chapter 499

The season was already well into spring, but the night wind blowing along Dongting Lake’s winding waterways was chilly.

The first thing Jang Taebo did after entering Jin Wikyung’s tent, which had been erected with thick cloth, was claim the spot in front of the brazier and sit down to warm himself.

“Whew. I’m finally starting to feel alive.”

Seeing this, Jin Wikyung smiled and handed him a teacup.

“You must have had a difficult journey getting here.”

“I happened to be in Henan, thankfully. If I’d been in Shanxi, I wouldn’t have come even if the Lesser Family Head himself had asked me. How dare you work an old man who’s only waiting for the day he dies this hard?”

I looked at Jang Taebo’s threatening muscles and thought,

*Seems like he’s more than capable of being worked hard…*

Just look at that body. This went beyond staying fit—he was in fantastic shape. While everyone else was shaving years off their lives from overwork, the worst Jang Taebo suffered was muscle loss.

Perhaps thinking the same thing, Wipeng glanced sideways between his own forearm and Jang Taebo’s before speaking.

“I heard all about what happened in Sichuan and Hubei. I came in person, partly to resolve the matter in Henan while I was at it, and partly because I was worried something might happen. It seems I chose the right time.”

Jin Wikyung laughed heartily and patted Wipeng on the shoulder.

“Wipeng. You really are my Zhang Liang!”[^1]

“I’m a martial artist.”

“Oh, then I’ll go with Han Xin.”

“Han Xin was eventually purged.”

“Then Xiao He.”

“Xiao He was a civil official, too.”

“……”

Jin Wikyung stared at Wipeng with an expression that suggested he wanted to purge him immediately, then cleared his throat.

“Ahem. You seem to have been holding a lot in all this time.”

“Yes, I have. You didn’t know?”

“I knew perfectly well, but I didn’t expect you to come all the way here just to say it to my face.”

“I didn’t come here on my own. My lord summoned me. Do you realize you’ve been away from your post for nearly three months? Not long ago, even Sect Leader Lee came looking for you and asked whether something had happened to you.”

“Cough, cough!”

Judging by how Jin Wikyung kept clearing his throat, he clearly had plenty to feel guilty about.

Wait a second. The Sect Leader Wipeng had just mentioned couldn’t possibly be…

“Are you talking about Young Lady Lee—Lee Seowol?”

At my question, Wipeng shook his head.

“Not Young Lady. She is the bona fide Sect Leader of an established sect, Third Young Master.”

“Oh, right. She is.”

The Mount Heng Sword Sect, which had once aimed to become the dominant power in Shanxi Province, had suffered a devastating collapse after a series of incidents.

However, Lee Seowol, the only surviving blood relative of the Blood Wolf Sword, had survived with my help and sworn loyalty to the Jin Family of Taiyuan.

Even if she held the position of a vassal, a Sect Leader was still a Sect Leader.

*When was the last time I saw her…? More than a year ago already?*

It had been around the time I left the Jin Family of Taiyuan with Jeok Cheongang and headed for Mount Jiuhua. Even by the time that had passed in Murim, it had been a year. If I included the time that had passed in the modern world, it was even longer.

I could still clearly recall the day we parted.



*“Excuse me, Sect Leader Lee.”*

*“Young Lady.”*

*“Pardon?”*

*“Please call me Young Lady.”*

*“Ah, yes. Then, Young Lady Lee.”*

*“Go ahead, Young Master Jin.”*

*“May peace prevail throughout your household.”*

*“……”*

*“And may your sect’s affairs flourish in the future. Whatever it is, I hope everything you do goes well.”*



Hmm. I supposed we had parted on a fairly warm note.

The Lee Seowol I remembered was firm and resolute, as befitted the daughter of a martial family. She had not backed down even in front of Pung Yang, who had attacked with the Red Wind Band.

*The ruined Mount Heng Sword Sect must have grown quite a bit by now.*

“So, is Young Lady Lee doing well these days?”

Wipeng thought for a moment before answering.

“She is doing well, if you mean some things. In other respects, perhaps not.”

“Why? Is something going wrong?”

“If you’re asking about the sect, the Mount Heng Sword Sect has already completed its reconstruction. Under Sect Leader Lee’s command, it is growing rapidly, and the number of its disciples is increasing every day.”

“Oh.”

“Great Hero Cheol Mubaek, the Tiger of Mount Heng and a friend of her late father, has also ended his seclusion and is taking an active role in the affairs of the Mount Heng Sword Sect.”

“Ohh.”

Then everything was going well, wasn’t it?

At my puzzled expression, Wipeng’s eyes narrowed.

“Third Young Master. Forgive me for asking, but may I ask you one thing? Have you really not contacted her at all since then?”

“Contacted her? What kind of contact?”

“……Hah. Never mind. Pretend you didn’t hear that.”

Something about the atmosphere felt strange.

Seeing Jang Taebo clicking his tongue beside me, a thought suddenly crossed my mind.

*No way.*

*Come on. It couldn’t be.*

*But what if…?*

*No. That isn’t it.*

Jin Wikyung rescued me from my sudden confusion with a single remark.

“It’s a relief to hear that Sect Leader Lee is doing well. By the way, what is the second doing these days? I haven’t seen him in months.”

Wipeng looked at me as though I were a pill bug before speaking with a sigh.

“He remains the same. He eats only the fasting pills prepared in the training hall and hasn’t taken a single step outside.”

“Mukyung, that idiot. What in the world is he planning…?”

Jin Wikyung’s concern was not unfounded.

Before I left for Mount Jiuhua, Jin Mukyung had lost a duel against Cheongpung. From that day onward, he had shut himself away in the training hall and refused to show himself.

A full year had passed. The Star-Array Grand Banquet had been held, and Dark Heaven’s shadow now hung over the Murim, yet he was still secluded.

*He said he wouldn’t come out until he achieved something great.*

There was a time when all of Murim called Jin Mukyung a genius the ages had rarely seen.

Even the direct disciples of the Nine Sects and One Gang, who were generously supported with excellent martial arts and elixirs, could not compare to him. Jin Mukyung had overcome the limitations of being descended from a fallen borderland martial family and risen to the forefront of the Ten Dragons and Phoenixes through martial arts alone.

*And then he met Cheongpung.*

For Jin Mukyung, Cheongpung’s existence must have been an enormous shock and an equally enormous stimulus.

The fact that he was still continuing his secluded training more than a year later was proof enough.

*He’s definitely the sort of person who will accomplish something. No doubt about it.*

The Jin Mukyung I knew was an undeniable genius.

He had not been given the Sword Saint’s instruction, nor had he received outstanding elixirs and secret martial arts.

Even so, he had reached this point through his own strength. I couldn’t easily imagine what he would look like when he finally broke his seclusion.

*The question is, when is he actually coming out?*

He wasn’t going to emerge when he was nearly sixty, was he?

If he managed to survive on nothing but fasting pills until then, I would genuinely respect him and treat him as my hyung.

The fact that he had continued his secluded training for an entire year while eating that tasteless crap was already impressive enough.

Even Wudang Daoists brought jerky instead of fasting pills when they practiced wall-facing meditation. What did that tell you?

*Even militant vegetarians who flipped over the grill at a barbecue would start looking for pork belly after chewing on a fasting pill once.*

While I was thinking that, the subject of the conversation had shifted to Jang Taebo.

“By the way, Lesser Family Head, will you tell me why you summoned this old man here?”

In response to Jang Taebo’s grumbling question, Jin Wikyung abruptly tossed out a single phrase.

“Ironcraft Hall. What do you think?”

“I’ve never heard of an organization like that within the Jin Family of Taiyuan.”

“You wouldn’t have. It was established only a few days ago.”

Jang Taebo’s brow furrowed.

“It’s a strangely familiar name. It reminds me of the Ironcraft Guild, where this old man once worked.”

“I named it with Old Master Jang in mind. Master of Ironcraft Hall. Doesn’t it sound good?”

“Lesser Family Head.”

Jang Taebo sighed before continuing.

“I left the Ironcraft Guild a long time ago.”

“Then it seems it’s time for you to return.”

“I’m old and tired. I don’t even have the strength to lift a hammer.”

Jin Wikyung stared meaningfully at Jang Taebo’s threatening muscles, then moved his lips.

—Youngest.

At this point, there was no way I could fail to understand why Jin Wikyung had summoned Jang Taebo all the way here.

I had already realized what my eldest brother was planning, so I lightly tapped the White Flame strapped to my back and knocked it loose.

Clang!

“Oh, no! I dropped a masterwork weapon made by a blacksmith who’s too old and tired to lift even a hammer!”

“……”

“Made from Ten-Thousand-Year Cold Iron, too. Supposedly incredibly difficult to work with. I wonder who could have made my spear…”

Jang Taebo glared at me with murderous eyes.

“Enough.”

“Why? I wasn’t talking about you, Elder.”

“Who else made it?”

“What are you talking about? How could someone without the strength to lift a hammer make something like this?”

“……Hoo. That damned brat.”

Jang Taebo sighed as though the ground itself had collapsed, then looked at Jin Wikyung.

“Was this why you gave me all sorts of help over the past few months?”

“Of course not. It was merely an expression of goodwill toward the artisan who made a masterwork weapon for my beloved youngest brother.”

“Then I’ll give you my answer.”

“I’m listening.”

“No. That is the only answer this old man can give you. Even with a knife at my throat, it won’t change.”

I shot my hand into the air.

“What about the spear?”

“Shut up before I take it back and snap it.”

“Ten-Thousand-Year Cold Iron. Special feature: fucking hard.”

“……Why did I make a spear for a bastard like you? What riches and glory was I hoping to gain?”

“You should just become the Master of Ironcraft Hall. I heard you’ve received all sorts of help from our side.”

“I’ll repay you with money. Do you think I’m going to put myself through that kind of hell again at my age?”

“Ah, seriously? You really won’t do it?”

“Then what are you going to do? I said I wouldn’t.”

“Then just tell me your conditions. I’ll meet as many of them as I can.”

“Conditions?”

A triumphant smile suddenly appeared at the corner of Jang Taebo’s mouth.

“Do you remember this time last year? I’ll set the same conditions as I did then.”

“If you mean the conditions you set back then, surely you don’t mean…”

“The Herb of Eternal Youth, gongcheong seokyu, a dragon’s claw, or a dragon pearl. Bring me any one of them.”

Beep.



> **System**
>
> - A Sudden Quest, **No Way You Can Do It Anyway**, has been created!
>
> - Quest Objective: Obtain at least one of the items Jang Taebo named.



Clang! Crash!

I sprang to my feet and shouted.

“Wait, where are you supposed to find things like that? And you’re asking for a dragon, not even an imugi!”

“Whether it’s an imugi or a dragon, bring me one first. Then I’ll bury my bones in the Jin Family of Taiyuan. If you can’t do it, just stay quiet.”

Beep.



> **System**
>
> - Quest details have been changed.
>
> - Quest Objective: Obtain an imugi’s claw.



After checking the changed System window, I nodded.

“Oh, there we go. Here.”

“My mind hasn’t changed, so don’t waste your effort—what are you suddenly giving me?”

“An imugi’s claw.”

“Huh?”

“An imugi’s claw. You told me to bring you one.”

“……What?”

A tremor ran through Jang Taebo’s pupils.

He was a Master Artisan ranked among the three greatest in the world, and he had once served as the Guild Leader of the Ironcraft Guild, the finest blacksmith organization under Heaven.

As Jang Taebo stared at the imugi’s claw, disbelief and horror at an unfamiliar material mingled in his eyes.

“An imugi’s claw? Is it real?”

“Just look at its length. Obviously it isn’t my claw.”

“No, I mean, where in the world did you…”

“I caught it.”

“What?”

“There are bones and scales, too.”

“That’s impossible!”

“Come take a look yourself after sunrise. Great Hero Wipeng has only heard about it through a letter, too, so you can go together.”

Beep.



> **System**
>
> - The Sudden Quest, **No Way You Can Do It Anyway**, has been successfully completed!
>
> - As a Quest Reward, the **Jin Family of Taiyuan** has acquired **Jang Taebo**!
>
> - Achievement unlocked: **Wow, You Found It!**



Along with the cheerful System notification, Jin Wikyung warmly put an arm around Jang Taebo’s shoulder.

“I look forward to working with you from now on, Master of Ironcraft Hall.”

“……!”

Jang Taebo’s eyes were utterly vacant as he was recruited as the Jin Family of Taiyuan’s personal Dobby—no, slave.

[^1]: Zhang Liang, Han Xin, and Xiao He were three of Liu Bang’s founding ministers. Zhang Liang and Xiao He were civil officials and strategists, while Han Xin was a military commander.
```

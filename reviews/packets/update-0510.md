<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0510.txt",
      "sha256": "a3d4bf0818e783033c8d01bc8e73282b1bd6207f78a2cc3a822243527da42fd5",
      "bytes": 14358
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "2ad67291cbecb8b168af1ac1dd1c655a9730fdec17d8e62fab9acbbd60d9f322",
      "bytes": 4145
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "73c9d885c23e8ca6b2a0ed4668e32bb7c10761c39bc7cd0aac80b8f93e0206d1",
      "bytes": 163106
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "ceef31caf4c29eb48f5462ec5135a90fc2d790988518a5eb1ef72202b9414b36",
      "bytes": 1006
    },
    {
      "path": "characters/Chunsam.md",
      "sha256": "d590f0fb8327447a6fb55124aa2c47f6fe0482bcbff9ac5d392a28cf6360308d",
      "bytes": 559
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "2e4e8c2ee0d6d020d958ba8c119684fb70feba23c9dd6ee169c7088b194cfee1",
      "bytes": 553
    },
    {
      "path": "characters/Gung Gibang.md",
      "sha256": "fc486c15b8715d02d631c4daefe44e5a26082f86c5edeadf8e024a1a9e73b904",
      "bytes": 686
    },
    {
      "path": "characters/Hwang Chung.md",
      "sha256": "2bb3c08b0699f2df38465e713ae8dc323777874fc35b2df32d867d13c634ad7f",
      "bytes": 663
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "966d8deb3784797fdbe618aa1149706b668779590120c4825a82fe2c793ab9df",
      "bytes": 1630
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "ca10f069899dbdb7ff54ac1fe1208f51cf0890f8d6ed663e0e56d014cced6e63",
      "bytes": 1777
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "345d3fc8b1bd8035e1f59d52cc87af8214d75c115cf6021a57ed04c7b1fd9474",
      "bytes": 622
    },
    {
      "path": "characters/Mu Song.md",
      "sha256": "5e24a3aa90b19259c4f2e48ad41c8edbf41dc7d83e26fc63e8c09b2e3a62fa36",
      "bytes": 1074
    },
    {
      "path": "characters/Mungyeong.md",
      "sha256": "f3fc935952579a57a84741ca682cbe24e66b4e5d519ed15a079fb2b31ec54965",
      "bytes": 985
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "d55e1b559aab842913d6859ee4f86aff71a3a23ad89553d949f27b82a0965ae8",
      "bytes": 154523
    }
  ],
  "estimated_tokens": 13925
}
-->

# Durable State Update — Chapter 510

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 510. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 510. Profile updates may replace only one
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
  "chapter": 510,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 510,
    "continuity_sources": [510],
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
    "Jeok Cheongang's Heart Demon and the dark memories binding him have been expelled; he has entered a new realm and achieved Returned to Youth.",
    "Mungyeong is the Slaughter Saint and former Divine Physician, a Returned to Youth Supreme Peak master and the greatest assassin in history; Mu Song and five Water Dragon Stronghold subordinates know he is an exceptionally powerful master but not that he is the Slaughter Saint.",
    "Mungyeong is training Taekyung to refine the stability and precision of the violent internal energy produced by the Fire Gate Divine Technique through Rising on Duckweed, Crossing Water.",
    "Zhuge Feng's Demon-Sealing Formation blocks all mana from the exposed Gate by drawing in natural qi, but whether it is permanent and repeatable remains unresolved.",
    "Jang Taebo is the Jin Family of Taiyuan's Master of Ironcraft Hall and is summoning renowned artisans to process the Water God Dragon's remains.",
    "War has begun and the New Murim Alliance is being formed at Mount Song; Taekyung believes Dark Heaven planned the Gate incident, while Jin Wikyung's Hubei arrangement was designed to create an opening among rival unorthodox factions.",
    "Around one hundred Level 5 Mutated Minnows, locally called Blood Fish, were captured in the Gate's entrance waterways; the remaining population is unknown, and the fish kill one another.",
    "The Southern Heaven Demon Empress is traveling toward Yunnan and expects to cause further deaths.",
    "Jin Mukyung remains secluded in the training hall after losing to Cheongpung, refusing to emerge until he achieves a great accomplishment.",
    "Taekyung's party is traveling by swift ship along the Yangtze toward Henan; Taekyung must practice Rising on Duckweed, Crossing Water behind it for ten days or until arrival.",
    "Mu Song wants to aid the Murim Alliance, but the Seafaring King alone decides the Yangtze River Channel League's major matters; the League and Green Forest Alliance may become rear threats.",
    "The North Sea Ice Palace remains isolationist, while Jeok Cheongang believes the Nanman Beast Palace will probably support orthodox Murim because of its historical goodwill toward the Fire Gate Clan."
  ],
  "continuity_sources": [
    509,
    508
  ],
  "open_questions": [
    "Will the Demon-Sealing Formation remain effective permanently, and can equivalent formations be installed repeatedly if more Gates appear?",
    "What is the Lord of Heaven's identity, and how is he connected to the dangerous force Taekyung associates with his original world?",
    "Where is the Southern Heaven Demon Empress ultimately headed, and what does she intend to do in Yunnan?",
    "Will the Nanman Beast Palace, North Sea Ice Palace, Yangtze River Channel League, and Green Forest Alliance support, ignore, or oppose the New Murim Alliance?",
    "Will Taekyung complete the ten-day Rising on Duckweed, Crossing Water training successfully?"
  ],
  "safe_through": 509,
  "temporary_decisions": [
    "Render 새외무림 as Outer Murim, 새외 as Outer Lands, 북해빙궁 as North Sea Ice Palace, 야수묘왕 as Beast Miao King, and retain Nanman Beast Palace for 남만야수궁.",
    "Render 소뢰음사 as Small Thunderclap Temple, 광풍사 as Mad Wind Society, 포달랍궁 as Potala Palace, 오독문 as Five Poisons Sect, 독곡 as Poison Valley, 천축 as India, and 갠지스강 as Ganges River.",
    "Render 파사국 as Persia, 회교도 as Muslims, 영웅건 as hero headband, 대막 as great desert, 귀염권 as Ghost Flame Fist, and 장성 as Great Wall.",
    "Retain established renderings including Energy-Dispersing Poison, Seven-Step Soul-Chasing Powder, Blood Fish, Mutated Minnow, innate qi, true-origin qi, Heart Demon, Returned to Youth, Demon-Sealing Formation, and New Murim Alliance; use oar, throwing blade, stern, and fire qi for this chapter's newly established terms.",
    "Render 궁예 as Gung Ye with an explanatory footnote, and render 연계 퀘스트 as Linked Quest and 가짜 무림인-2단계 as Fake Murim Martial Artist—Stage 2."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 청풍     | **Cheongpung**     |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 해상왕    | **Seafaring King**            | Pa Ryun        |
| 장강수로맹  | **Yangtze River Channel League** |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 운기조식   | **circulate one's qi**                           | Usually better as a verb than a proper-name technique |
| 기루     | **pleasure house**                               |                                                       |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 하남     | **Henan**              |
| 사천     | **Sichuan**            |
| 귀가      | **your family**                                                 |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 공자      | **Young Master**                                                |
| 춘삼 | **Chunsam** | Lower District Sect martial artist serving as the carriage driver. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 궁기방 | **Gung Gibang** | Beggars' Sect Successor Beggar and finalist. |
| 황충 | **Hwang Chung** | Lord of Donghu Stronghold, the Seafaring King's sworn brother, and the Yangtze One Saber. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 무송 | **Mu Song** | Lord of Water Dragon Stronghold and disciple of the Seafaring King. |
| 문경 | **Mungyeong** | Young medical apprentice and newly introduced passenger. |
| 기감 | **Qi Sense** | Taekyung's sensory technique; its range reaches seventy meters in this chapter. |
| 송이 | **Song-i** | Short form used for Song Song; Taekyung's love interest. |
| 은원 | **gratitude and grudges** | Moral debts that must be repaid. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 소원 | **Sowon** | Name called out by Im Kkeokjeong during the Wyvern attack. |
| 반로환동 | **Returned to Youth** | Possible explanation for an apparently young Supreme Peak master. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 미미 | **Mimi** | Worker at Honghwaru referenced in Taekyung's joke. |
| 호북 | **Hubei** | Province on Ju Gongsan's route from Guangdong to Henan. |
| 수룡채 | **Water Dragon Stronghold** | Major river stronghold belonging to the Yangtze River Channel League. |
| 선화아 | **Ship-Fire Boy** | Mu Song's sobriquet; literally a child who lights fires aboard a ship. |
| 채주 | **Stronghold Lord** | Title used for the lord of a water stronghold. |
| 장강 | **Yangtze** | The river controlled by the Yangtze River Channel League. |
| 의생 | **medical apprentice** | Mungyeong's occupation. |
| 사혈 | **lethal acupoint** | An acupoint whose strike can kill. |
| 열화신룡 | **Blazing Flame Divine Dragon** | New sobriquet bestowed on Jin Taekyung. |
| 장강일도 | **Yangtze One Saber** | Hwang Chung's sobriquet. |
| 천령폭 | **Tianling Falls** | Dangerous waterway leading to Donghu Stronghold. |
| 쾌조선 | **swift ship** | Fast vessel operated by the Yangtze River Channel League. |
| 찍먹형 | **dip-and-taste punishment** | Mu Song's joking threat against sailors who slack off. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 촌각 | **moments** | Short intervals disappearing from Jeok's day. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 청풍 | 진태경 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung repeatedly addresses Taekyung as 은인 after receiving food. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 진태경 | 청풍 | companion_to_young_martial_artist | Young Master Cheongpung | formal-polite | Taekyung uses 청 공자 while correcting Cheongpung's royal-etiquette mistake. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 적천강 | 청풍 | overwhelming_elder_to_young_martial_artist | you / little punk | blunt, amused, and threatening | Jeok Cheongang uses 네, 이놈, and related blunt forms while testing Cheongpung. |
| 청풍 | 적천강 | young_martial_artist_to_overwhelming_elder | Grandpa Jeok | casual-familiar despite deference | Cheongpung uses 적 할아버지 while asking Jeok Cheongang to confirm Taekyung's condition; this is a familial form of address, not literal kinship. |
| 궁기방 | 진태경 | rival_finalists | you bastard | insulting-casual | Gung Gibang answers Taekyung's collective insult with a profane threat. |
| 진태경 | 궁기방 | rival_finalists | you three idiots | insulting-casual | Taekyung addresses Gung Gibang as part of the trio and threatens them before a duel. |
| 수하 | 채주 | subordinate_to_stronghold_lord | Stronghold Lord | deferential | The subordinate calls Mu Song 채주 while reporting the nearby vessel. |
| 진태경 | 무송 | junior_martial_artist_to_senior_martial_artist | Senior | formal-polite | Taekyung uses 선배님 after recognizing Mu Song as a senior martial artist and disciple of the Seafaring King. |
| 문경 | 무송 | survivor_to_savior_and_authority | Great Hero Mu Song | formal-deferential | Mungyeong credits Mu Song with saving him and asks him to spare Hwang Tae-gu. |
| 무송 | 문경 | stronghold_lord_to_young_passenger | you | gruff-but-considerate | Mu Song offers Mungyeong the right to decide Hwang Tae-gu's fate. |
| 진태경 | 문경 | young_martial_artist_to_medical_apprentice | Young Hero | formal-polite | Taekyung addresses the non-martial Mungyeong as 소협 while praising his actions. |
| 문경 | 진태경 | young_passenger_to_younger_martial_artist | Young Hero | deferential | Mungyeong uses 소협 while asking Taekyung for help boarding the ship. |
| 무송 | 진태경 | senior_martial_artist_to_junior_martial_artist | Junior | familiar-teasing | Mu Song calls Taekyung 후배 and jokes about his supposed taste for men. |
| 청풍 | 문경 | martial_companion_to_medical_apprentice | Medical Apprentice | cheerful-polite | Cheongpung addresses Mungyeong as 의생님 while asking him to greet the Tang Clan. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 문경 | 적천강 | old_acquaintances | Fire King | familiar and grave | The figure bearing Mungyeong’s name greets Jeok Cheongang by his established epithet. |
| 궁기방 | 청풍 | martial_companions | Young Hero Cheongpung | formal-polite | Gung Gibang uses 청 소협 while asking why Cheongpung is at the temporary clinic. |
| 청풍 | 미미 | handler_to_companion_snake | Mimi | cheerful-commanding | Cheongpung repeatedly calls and commands the Thousand-Year Poison Horned Snake. |
| 무송 | 적천강 | junior_martial_artist_to_legendary_martial_master | Great Hero Jeok | formal-deferential | Mu Song respectfully refers to Jeok Cheongang as 적 대협 while worrying that Jeok dislikes him. |
| 적천강 | 문경 | overwhelming elder to old acquaintance | you / little punk | mocking and threatening | Mocks Mungyeong's expression and threatens to poke out his eyes. |
| 적천강 | 무송 | legendary martial master to stronghold lord | you | gruff, coercive, and dismissive | Uses 자네 while ordering Mu Song to take the group only as far as Sichuan and leave the fast ship. |
| 청풍 | 무송 | young martial companion to stronghold lord | you | cheerful and familiar | Offers Mu Song his last dumpling and then induces him to buy more in Guang'an. |
| 궁기방 | 무송 | martial companion to Stronghold Lord | Senior Mu Song | pleading-deferential | Begins pleading for Mu Song to save them from Tianling Falls. |
| 무송 | 황충 | junior_martial_artist_to_mentor_like_uncle | Uncle Hwang | familiar-respectful | Mu Song privately addresses Hwang Chung as 황 숙부 and cries out for him after discovering Donghu Stronghold's destruction. |
| 진태경 | 미미 | rescuer to companion snake | Mimi or Mimi-chan | informal, pleading | Taekyung calls to Mimi while asking the snake to carry him and the survivors. |
| 적천강 | 궁기방 | overwhelming_elder_to_younger_martial_artist | you | blunt and threatening | Jeok Cheongang rebukes Gung Gibang for speaking informally and orders him to lie down. |

## Listed compact profiles

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 508
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, the grandson and Disciple of Sword Saint Mae Jonghak, and a Supreme Peak martial master known as the Huashan Divine Dragon.
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, a deep love of martial arts, competitive pride, unusual resistance to monster-induced Fear, and discomfort when someone copies his martial arts.
- **Voice:** Dreamy and hazy, with innocent, polite phrasing; he has begun imitating Taekyung's profanity.
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions while Taekyung is his only true martial rival; Tang Sadok has temporarily entrusted Mimi to him.

### Chunsam.md

# Chunsam (춘삼)

- **Safe through:** Chapter 120
- **Aliases:** None
- **Role:** First Rate Lower District Sect martial artist who posed as the carriage driver for Wolhwa's group
- **Personality:** Silent, disciplined, and lethal; obeys Wolhwa's instructions without hesitation
- **Voice:** Nearly silent; communicates through concise action rather than speech
- **Relationships:** Lower District Sect subordinate serving under Wolhwa; executes a mounted-bandit informant at her direction

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 508
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Gung Gibang.md

# Gung Gibang (궁기방)

- **Safe through:** Chapter 504
- **Aliases:** Successor Beggar, Beggar Prince, pure-blooded beggar, ultimate beggar
- **Role:** Gung Gibang is the Beggars' Sect Successor Beggar and a unique eight-knot disciple.
- **Personality:** Vulgar, aggressive, and quick-tempered.
- **Voice:** Blunt, profane, and vividly threatening.
- **Relationships:** Gung Gibang is a rival finalist alongside Baek Woo and Zhuge Gyun who trades insults with Taekyung, uses Beggars’ Sect intelligence to investigate Tang Taesang’s murder and Dark Heaven’s Hubei forces, and has now found a trace of Honglan.

### Hwang Chung.md

# Hwang Chung (황충)

- **Safe through:** Chapter 462
- **Aliases:** Yangtze One Saber
- **Role:** Hwang Chung was the Lord of Donghu Stronghold, a moderate-faction elder of the Yangtze River Channel League, and the Seafaring King's sworn brother before he was killed in the stronghold's destruction.
- **Personality:** Calm, clever, and supportive of the orthodox faction during the Great Faction War.
- **Voice:** Not established.
- **Relationships:** Hwang Chung helped the Seafaring King establish the Yangtze River Channel League and is regarded by Mu Song as an uncle and trusted senior.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 508
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, and Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 504
- **Aliases:** Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, a Supreme Peak master who possesses the Heavenly Martial Physique and superhuman physical strength, has manifested Force, opened his Middle Dantian, crossed the wall into true mastery, can perceive the texture of qi well enough to sever layered magic, can resist high-level monster Fear through exceptional mental strength, is publicly recognized as an S-rank-level Hunter while formally retaining an A-rank license pending testing, and can command coordinated raids against powerful monsters.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate, student, and trusted manager of media and official arrangements, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, and Xiao Shen regards him as an older brother after Jin saved him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 504
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Mu Song.md

# Mu Song (무송)

- **Safe through:** Chapter 508
- **Aliases:** Ship-Fire Boy
- **Role:** Lord of Water Dragon Stronghold, a Peak master and the Seafaring King's second martial Disciple who controls major Yangtze river traffic in Sichuan, belongs to the Yangtze River Channel League's moderate faction, and is an exceptionally skilled ship captain.
- **Personality:** Ambitious, domineering, impatient with interruptions, and capable of pragmatic cooperation when circumstances demand it.
- **Voice:** Deep and low in private, shifting to dry authority or boisterous command when addressing subordinates and rivals.
- **Relationships:** Mu Song belongs to the Yangtze River Channel League's moderate faction, regards Hwang Chung, his senior and Uncle Hwang, as family, must weigh whether the League will support the New Murim Alliance while the Seafaring King retains authority over major League decisions, and has been threatened by Mungyeong to keep Mungyeong's identity secret with five subordinates.

### Mungyeong.md

# Mungyeong (문경)

- **Safe through:** Chapter 509
- **Aliases:** Killing Ghost
- **Role:** Mungyeong is the legendary physician known as the former Divine Physician and Slaughter Saint, a Returned to Youth Supreme Peak master and the greatest assassin in history who passed the Divine Physician title to his Disciple.
- **Personality:** Compassionate, resolute, resourceful, and calm under extreme pressure.
- **Voice:** His Mungyeong persona is timid, deferential, and cheerful, while his Slaughter Saint voice is dry, impassive, and blunt.
- **Relationships:** Dong Feng is his Disciple, Jeok Cheongang is an old acquaintance whom Mungyeong helped break free of his Heart Demon, Mungyeong was asked to look after and instruct Jin Taekyung after testing his basics, and Mu Song plus five Water Dragon Stronghold subordinates now know he is an exceptionally powerful master but not that he is the Slaughter Saint.

## Korean source

```text
＃510화



선화아(船火兒) 무송은 태생부터 뱃사람이었다.

얼굴도 기억나지 않는 그의 부모는 근방에 유명한 잉꼬부부 수적이었고, 외가와 친가의 가계에도 수적이나 어부가 수두룩했다.

그야말로 뼈대 깊은 수적 집안.

그 때문인지는 몰라도 무송은 육지보다 배에 있는 시간이 훨씬 좋았다.

빽빽한 숲과 들판을 보면 극독을 먹은 것처럼 손발이 저리고 숨이 막히는데, 탁 트인 강과 바다만 보면 생기가 도는 것이다.

그뿐인가. 수적 질로 한몫 단단히 잡은 다른 채주들이 그럴듯한 장원을 매입하고 기루에서 주색잡기를 즐길 때, 그는 배를 꾸미고 그물을 엮어 만든 침대에 누워 장강을 구경했다.

그리고 그럴 때마다 무송이 늘 하는 생각이 있었다.

‘천하가 온통 물로 이루어졌으면 좋겠다. 그럼 평생 배에서만 지낼 수 있을 텐데.’

하지만 지금, 무송은 멍하니 장강을 응시하며 중얼거리고 있었다.

“아, 씨바. 배 존나 느리네. 빨리 내리고 싶다…….”

“……!”

“……!”

순간 싸해지는 분위기.

주위에 있던 수룡채의 수적들은 순간 자신들의 귀를 의심했다.

그리고 눈동자를 뒤룩뒤룩 굴리며 눈짓을 주고받던 그들은 얼마 가지 않아 명쾌한 결론을 내렸다.

‘우리가 잘못 들었나 보네!’

‘그거 맞다. 단체로 귀가 잘못된 게 틀림없어.’

‘두목께서 그런 말을 하실 리 없지.’

무송이 어떤 사람인지는 수룡채의 최고참부터 막내까지, 아니 장강수로맹에 있는 수적 전부가 아는 사실이었다.

뜨거운 뱃사람의 상징! 스승인 해상왕보다도 더 장강을 사랑하는 남자!

그런 사람이 제 목숨만큼이나 아끼는 쾌조선을 느리다며 욕하고, 육지로 가고 싶다고 말할 리가 없…….

“이 짓거리도 때려치우든가 해야지. 개 같아서 진짜.”

“……!”

“……!”

보이지 않는 충격이 갑판을 휩쓸었다. 갑작스러운 무송의 은퇴 의사 표명과 수룡채 해체 위기에 조용해진 사방.

영원히 이어질 것 같던 침묵을 깨트린 건 넋이 나간 어느 수적의 어깨에서 미끄러진 술통이었다.

쿵, 콰직!

술이 가득 담겨 있던지라 무게도 상당했다. 떨어진 목제 통이 박살 남과 동시에 술이 사방으로 튀었다.

그제야 자신만의 상념에서 빠져나온 무송이 눈을 부라렸다.

“이게 무슨 짓거리냐.”

안 그래도 흉악한 면상의 소유자인 무송이다. 술통을 떨어트린 수적은 사색이 되어 넙죽 허리를 굽혔다.

“죄, 죄송합니다!”

“이 새끼가 술 귀한 줄 모르고 확 그냥. 거꾸로 매달아서 그 뭐냐. 장강, 장강…… 그래, 찍먹형에 처할까 보다.”

“주, 죽을죄를 지었습니다. 그러니 제발 그것만은…….”

“조심해라. 가뜩이나 기분 거지 같은데 초치지 말고.”

“예, 옙!”

“됐고, 원상복구나 시켜 놔. 술도 도로 하나 가져다 놓고.”

“예? 하지만…….”

“이놈이 미쳤나. 어디서 감히 토를, 어서 움직이지 못할까!”

“조, 존명!”

필사적인 복명복창과 함께 멀어지는 수하의 뒷모습에, 무송은 한숨을 푹 내쉬었다.

‘뭐 하나 제대로 되는 일이 없군.’

단순한 불평이 아니라, 정말 사실이 그랬다.

호재만 이어져도 부족할 판국에 안 좋은 일만 잇따라 계속되고 있었다.

울며 겨자 먹기로 본거지인 사천을 떠나 호북에 왔고, 얼마 전에는 친혈육 같았던 장강일도 황충을 떠나보내야 했다.

그에 대한 은원(恩怨)은 갚아야 한다는 생각으로 진태경 일행을 하남까지 데려다주기로 했는데…… 아니나 다를까 최악의 상황이 벌어지고야 말았다.

‘끝까지 모르는 척하려고 했는데.’

반로환동 한 것이 확실해 보이는 정체불명의 노고수.

어린 의생의 탈을 쓴 그 맹수가 자신의 정체가 탄로 났음을 알아차려 버렸다.

‘괴물 같은 늙은이. 도대체 정체가 뭐지?’

그간 무송이 면밀하게 관찰해 온 바에 의하면, 이 사실을 아는 사람은 함께 이동하고 있는 일행 중에서도 극소수였다. 기껏해야 화왕 적천강과 진태경 정도?

어디로 튀는지 알 수 없는 청풍도 문경 앞에서는 조용해지는 걸 보면, 저놈도 알고 있을 확률이 높다.

‘제기랄. 이럴 줄 알았으면 차라리 다른 배를 타는 건데.’

현재 하남으로 향하는 수룡채의 쾌조선은 총 두 척이었다. 사람이 많으니 인원을 나눠서 타자는 건 적천강의 강요에 의해서였고, 무송에게는 감히 화왕의 뜻을 거스를 용기가 없었다.

백여 장 앞에서 앞서가고 있는 또 다른 쾌조선에서 편안히 가고 있을 부채주를 생각하자 배가 아플 지경이다.

‘여기에 비하면 저쪽은 꽃밭이지, 꽃밭.’

적어도 다른 배에는 말이 통하는 인물들이 모여 있다.

궁기방의 냄새도 잠깐만 숨을 참으면 해결될 문제고, 청풍이 미미라고 부르는 괴상한 뱀의 묘기를 보는 것도 제법 재미가 쏠쏠했다.

반면 이쪽은?

‘열화신룡 진태경. 화왕 적천강. 그리고 정체를 숨긴 또 다른 노괴.’

그야말로 괴물 집합소라고 해도 과언이 아니다.

그나마 무늬만 후배인 진태경은 무송에게 존댓말이라도 써 주고, 적천강도 자주 보다 보니 그럭저럭 사람 취급은 해 주는데 마지막 한 사람이 문제였다.

‘그 눈빛…….’

문경의 서늘한 눈동자를 떠올린 무송은 자신도 모르게 전신을 바르르 떨었다.

아까부터 계속되는 두목의 이상 행동을 주목하던 고참 수적 하나가 다가와 슬쩍 물었다.

“채주. 괜찮으십니까요?”

“괜찮아 보이냐?”

“전혀 아닌뎁쇼.”

“그럼 뭘 물어봐. 어차피 사정 다 아는 놈이.”

“거참 걱정을 해 줘도 뭐라 하시네. 그나저나 그 노괴(老怪)가 도대체 무슨 겁박을 했길래 안색이…… 읍!”

빛의 속도로 손을 뻗어 수하의 입을 틀어막은 무송이 긴장된 눈빛으로 주위를 둘러봤다.

들은 사람이 없다는 걸 두 번, 세 번 확인하고 나서야 비로소 분노가 솟구쳤다.

“이런 미친놈을 봤나. 죽고 싶어서 환장했느냐?”

“읍읍, 푸하!”

간신히 입막음에서 벗어난 고참 수적이 말을 더듬었다.

“죄, 죄송합니다요. 저도 모르게 그만.”

“내 이미 여러 번 말했지만, 너와 다른 녀석들 모두 그에 관해서는 입도 벙긋하지 마라. 알겠느냐?”

“예에.”

고참 수적은 문경의 정체를 직접 목격한 몇 안 되는 수적 중 하나였다.

불안하게 눈동자를 굴리는 그의 모습에 한숨을 푹 내쉰 무송이 입을 열었다.

“그보다 아까 내가 내린 지시 사항. 모두 철저히 숙지시켜 놨느냐?”

고참 수적이 고개를 끄덕였다.

“그러믄입쇼. 채주께서 말씀하신 대로, 후미에는 얼씬도 하지 말라고 단단히 일러 뒀습니다요.”

“의심하는 놈은 없었고?”

수적들의 머릿수만 수십이다 보니, 멍청하고 눈치 없는 한두 놈은 꼭 끼어있기 마련이었다.

“있었지요. 춘삼이. 채주의 명이라고 했는데도 세 번이나 캐묻길래 식겁했습니다요.”

무송이 뿌드득 이를 갈았다.

“내 그 새끼일 줄 알았지. 춘삼이 그놈 지금 어디 있느냐?”

“장강에 푹 담갔다가 건졌는뎁쇼. 지금 아래에 처박아 뒀으니 다시는 그런 말 안 나올 겁니다요.”

“후우, 잘했다. 앞으로 내가 자리를 비울 때도 애들 단속 철저히 해. 까딱하면 쾌조선이랑 같이 싸그리 장강에 수장(水葬)되는 수가 있다.”

무송의 낯빛은 어두웠다.

화왕 적천강이라는 괴물로도 부족해서, 이제는 반로환동 한 정체불명의 노괴까지 끼어 버렸다. 차라리 그 사실을 몰랐던 때가 그리워질 지경이다.

하늘 같은 채주의 약한 모습에 고참 수적이 초조한 목소리로 물었다.

“이러다가 두 번 다시 사천으로 못 돌아가는 거 아닙니까? 가뜩이나 벌써 두 달 가까이 수채를 비웠는데, 이대로 영영 빌까 걱정입니다요.”

“재수 없는 소리. 호랑이 굴에 들어가도 정신만 차리면 산다고 했다.”

“그건 호랑이고, 반로환동 한 초절정 고수한테는 정신을 골백번 차려도 안 될 것 같은디…….”

생각해 보니 저 말이 맞다.

말문이 막힌 무송이 조용히 입을 다문 바로 그때였다.

“술통을 가져왔는데, 어디에 두면 되겠습니까?”

등 뒤에서 들려오는 목소리. 이 상황에서 술통 운운할 놈은 한 사람밖에 없다.

짜증이 솟구친 무송은 고개를 돌리기도 전에 벌컥 성을 냈다.

“아니, 보자 보자 하니까 아까부터 저 폐급 새끼가……!”

“지금 제게 폐급 새끼, 라고 하셨습니까.”

“……어?”

억겁과도 같은 촌각의 시간.

자신의 어깨 너머를 바라보며 입을 딱 벌린 고참 수적의 모습에, 무송은 단단히 좆 됐음을 직감했다.

더불어 잊고 있던 사실 하나가 뇌리를 스쳤다.

‘아, 여분의 술통을 후미(後尾)에 놔뒀었구나.’

어쩐지 다시 가져오라 할 때 뭔가 말하려다가 말더라니.

무송은 눈앞이 아찔해졌다. 천령폭의 와류에 휘말렸을 때도 두려움을 느끼지는 않았는데, 지금은 식은땀으로 멱을 감아도 될 정도다.

“무송 대협.”

한차례 눈을 질끈 감은 무송이 억지웃음을 지으며 천천히 돌아섰다.

꿈에서도 만나기 싫은 한 사람이 그곳에 있었다.

“어, 어어. 문경이로구나. 무, 무슨 일이니?”

“별일은 아닙니다.”

그 나이대의 소년처럼 빙긋 웃은 문경이 대답했다.

“후미에서 장강을 구경 중이었는데, 수하 분께서 오셨지 뭡니까. 듣기로는 무송 대협께서 술통을 가져오라 명하셨다던데…….”

“내, 내가 말이냐?”

“아닙니까?”

“그, 글쎄, 나는 그런 명령을 내린 기억이…….”

그때, 문경의 등 뒤에서 술통을 어깨에 진 수적이 나타나 빠릿빠릿하게 외쳤다.

“채주님! 명하신 대로 술통을 가져왔습니다!”

무송은 저놈의 주둥아리를 당장 찢어 버리고 싶은 충동을 억누르며 말을 이었다.

“그런 명령을 내린 기억이…… 나는구나. 맞아. 그런 명령을 내리긴 했다. 명백한 실수였지.”

“실수라. 네.”

무송은 자신의 몸 곳곳을 차례차례 응시하는 문경의 시선을 느꼈다.

왠지 모르게 사혈(死血)을 보고 있다고 생각되는 건 단순한 착각일 거다. 착각이어야 한다.

다행히 그의 필사적인 바램이 하늘에 닿았는지, 곧 시선을 거둔 문경이 입을 열었다.

“진노하신 적 대협께서 길길이 날뛰셨습니다. 한 번만 더 이런 일이 생긴다면 그때는 정말 각오하라고 하시더군요.”

물론 적천강은 길길이 날뛰지도, 저런 말을 하지도 않았다.

하지만 무송은 저 말의 의미를 알아듣지 못할 만큼 멍청한 인물이 아니었다.

“아, 알겠다. 적 대협께 명심하겠다고 전해라. 그런데 다만…….”

“말씀하십시오.”

“어쩔 수 없이 꼭 가야 할 일이 있다면 어찌해야겠느냐? 뱃일에 필요한 일이라거나, 식사 문제도 그렇고.”

잠시 생각하던 문경이 대답했다.

“그렇지 않아도 적 대협께서 말씀을 전하라 하셨습니다. 전자의 경우에는 무송 대협 홀로 와서 팔요한 일을 해결하고. 후자의 경우에도 직접 식사를 전하라고 말입니다.”

“……나 혼자 그걸 다하란 말이냐?”

“싫으십니까?”

무송이 얼굴을 굳히며 대답했다.

“내 일생의 소원이었다. 너무 좋아.”

“그렇군요, 그럼 이만 가 보겠습니다. 석식 때 뵙지요.”

무송을 남겨 두고 다시 후미로 향하던 문경은, 문득 발걸음을 멈추고 돌아섰다.

“아, 그리고.”

“또, 또 뭔가 할 말이 남았느냐?”

“식사는 이 인분이면 됩니다. 하남에 도착할 때까지 쭉.”

“으응?”

“진 공자님은 당분간 입맛이 없을 예정이니, 그렇게 알고 계시면 될 듯합니다.”

하남에 도착하려면 족히 열흘은 남았다. 아무리 입맛이 없다 해도 열흘을 꼬박 굶는다는 건 말도 안 되는 소리다.

호기심이 도진 무송은 용기를 쥐어짜 내어 물었다.

“그, 혹시…… 진 후배에게 무슨 일이라도 있느냐?”

“아.”

문득 문경의 입가에 보조개가 패였다.

그것은 그를 괴물로 여기는 무송조차 순간 천진난만한 소년이라고 착각할 만큼 자연스러운 미소였다.

“지금쯤 바쁘실 겁니다. 아주 많이요.”



* * *



간혹, 인간 스마트폰이 된 것 같은 기분을 느끼고는 한다.

배터리가 15% 이하로 떨어지면 알려주는 경고 메시지처럼, 내 눈앞에는 비슷한 내용의 시스템 창이 떠 있었다.

삐빅.



- [공력]의 대부분이 소진되었습니다.

- [운기조식]으로 공력을 보충하십시오. 체내의 공력이 완전히 고갈된다면 상태 이상에 빠질 수 있습니다!



하지만 어째서일까. 당장 공력이 모두 소진되면 이 광활한 장강 한복판에 가라앉을 텐데, 위기감보다는 의문이 더욱 크다.

그리고 그 이유 중 하나는, 분명 저 멀리서 다가오는 어떤 것의 존재 때문임이 확실하다.

스으윽.

아주 은밀히 가까워지는 커다란 몸뚱어리. 수면 위로 삐죽 솟은 지느러미는 왠지 모르게 낯이 익었다.

‘아니, 시발.’

상어가 왜 장강에 있냐.
```

## Final English reading copy

```markdown
# Chapter 510

Ship-Fire Boy Mu Song had been a sailor from birth.

His parents, whose faces he could no longer remember, had been a famous pair of lovebird river bandits in the area. His maternal and paternal family lines were also full of river bandits and fishermen.

He came from a river-bandit family to the bone.

Maybe that was why Mu Song much preferred spending time aboard a boat to being on land.

Whenever he saw dense forests and open fields, his hands and feet tingled and his breath grew tight, as though he had swallowed deadly poison. But whenever he saw a wide-open river or sea, his vitality returned.

And that wasn’t all. While other stronghold lords who had made fortunes as river bandits bought impressive estates and indulged in wine, women, and gambling at pleasure houses, Mu Song decorated his boat, lay on a bed woven from nets, and watched the Yangtze.

Whenever he did, he always had the same thought.

*I wish the entire world were made of water. Then I could spend my whole life on a boat.*

But now, Mu Song was staring blankly at the Yangtze and muttering,

“Ah, fuck. This boat is fucking slow. I want to get off already…”

“……!”

“……!”

The atmosphere instantly turned icy.

The Water Dragon Stronghold river bandits nearby doubted their own ears.

After rolling their eyes around and exchanging glances, they soon reached a clear conclusion.

*We must have heard wrong!*

*That’s right. All our ears must have malfunctioned at once.*

*Our Stronghold Lord would never say something like that.*

Everyone in the Yangtze River Channel League knew what kind of person Mu Song was, from the most senior Water Dragon Stronghold river bandit to the newest recruit.

The very embodiment of a passionate sailor! A man who loved the Yangtze even more than his Master, the Seafaring King!

There was no way a man like that would curse the swift ship he treasured as much as his own life for being slow and say he wanted to go ashore—

“I should quit this whole damn business. It’s fucking miserable.”

“……!”

“……!”

An invisible shock swept across the deck.

The surroundings fell silent at Mu Song’s sudden declaration of his intention to retire and the threat of the Water Dragon Stronghold being disbanded.

The silence, which seemed as though it might last forever, was broken when a liquor barrel slipped from the shoulder of a dazed river bandit.

Boom! Crash!

The barrel had been filled with liquor, so it was quite heavy. The wooden cask shattered when it hit the deck, sending alcohol splashing in every direction.

Only then did Mu Song snap out of his thoughts and glare.

“What the hell are you doing?”

Mu Song already had a fearsome face. The river bandit who had dropped the barrel went pale and bowed deeply at the waist.

“I-I’m sorry!”

“You bastard. You don’t know the value of liquor? I ought to hang you upside down and… What was it? The Yangtze, the Yangtze… Right. I might just sentence you to the Yangtze’s dip-and-taste punishment.”

“I’ve committed a crime worthy of death. Please, anything but that…”

“Be careful. I’m already in a shitty mood, so don’t make things worse.”

“Yes, sir!”

“Enough. Clean everything up and put things back the way they were. And bring another barrel of liquor to replace it.”

“Pardon? But…”

“Are you insane? How dare you talk back to me? Get moving!”

“Y-yes, sir!”

As the subordinate hurried away, shouting frantic acknowledgments, Mu Song let out a deep sigh.

*Nothing is going right.*

This wasn’t a simple complaint. It was the truth.

Even good fortune would not have been enough to make up for it, yet one bad thing after another kept happening.

He had been forced to leave his home base in Sichuan and come to Hubei. Not long ago, he had also had to say goodbye to Hwang Chung, the Yangtze One Saber, who had been like family to him.

Believing he had to settle what he owed Hwang Chung, he had agreed to take Jin Taekyung’s group as far as Henan. But as expected, the worst possible situation had come to pass.

*I was going to keep pretending not to know until the end.*

An unidentified old master who had clearly achieved Returned to Youth.

That beast wearing the guise of a young medical apprentice had realized that his identity had been exposed.

*What kind of monster is that old man? Who the hell is he?*

Based on Mu Song’s careful observations, only a tiny number of people among the group traveling with them knew the truth. At most, the Fire King, Jeok Cheongang, and Jin Taekyung?

Cheongpung was impossible to predict, but the fact that even he became quiet in front of Mungyeong made it highly likely that he knew too.

*Damn it. If I’d known this would happen, I should have taken the other ship.*

The Water Dragon Stronghold currently had two swift ships heading toward Henan. Jeok Cheongang had insisted that they split up because there were so many people, and Mu Song had not possessed the courage to defy the Fire King.

When Mu Song thought of the deputy Stronghold Lord, who was probably enjoying a comfortable journey aboard the other swift ship more than a thousand feet ahead, his stomach hurt.

*Compared to this, that ship is a flower garden. A goddamn flower garden.*

At least the other ship had people he could communicate with.

Gung Gibang’s smell could be dealt with by holding his breath for a moment, and watching the bizarre snake Cheongpung called Mimi perform its tricks was surprisingly entertaining.

But this ship?

*Blazing Flame Divine Dragon Jin Taekyung. Fire King Jeok Cheongang. And another old monster hiding his identity.*

Calling it a gathering of monsters would not be an exaggeration.

At least Jin Taekyung, who was technically his junior, still used formal speech with Mu Song. And since Mu Song saw Jeok Cheongang so often, the Fire King treated him more or less like a person.

But the last man was the problem.

*Those eyes…*

As he recalled Mungyeong’s cold gaze, Mu Song shuddered involuntarily.

One of the senior river bandits, who had been watching the Stronghold Lord’s strange behavior for some time, approached and cautiously asked,

“Stronghold Lord, are you all right?”

“Do I look all right?”

“Not at all, sir.”

“Then why ask? You already know the whole situation.”

“What a thing to say when I’m worried about you. Anyway, what in the world did that old monster threaten you with to make you look so—”

“Ugh!”

Mu Song’s hand shot out at the speed of light and clamped over his subordinate’s mouth. He looked around with tense eyes.

Only after checking twice, then a third time, that no one had heard did his anger finally boil over.

“Have you lost your mind? Are you dying to die?”

“Ugh—pfft!”

The senior river bandit barely escaped Mu Song’s grip and stammered,

“I-I’m sorry, sir. It just slipped out.”

“I’ve already told you several times, but you and everyone else are not to utter a single word about him. Understood?”

“Yes, sir.”

The senior river bandit was one of the few who had personally witnessed Mungyeong reveal his true power.

Mu Song sighed deeply at the man’s anxious, darting eyes before speaking.

“More importantly, did you make sure everyone thoroughly understood the orders I gave earlier?”

The senior river bandit nodded.

“Yes, sir. Just as you ordered, I firmly told everyone not to go anywhere near the stern.”

“Did anyone get suspicious?”

There were dozens of river bandits aboard. With that many people, there was always at least one idiot with no sense of discretion.

“There was one. Chunsam. Even after I told him it was the Stronghold Lord’s order, he kept asking questions three times. Nearly gave me a heart attack.”

Mu Song ground his teeth.

“I knew it would be that bastard. Where is Chunsam now?”

“We dunked him in the Yangtze and hauled him back out. He’s been tossed down below. He won’t be saying anything like that again.”

“Whew. Good work. Keep the others in line even when I’m away. One slip, and every last one of us could end up drowned at the bottom of the Yangtze along with the swift ship.”

Mu Song’s face was dark.

The monster known as the Fire King, Jeok Cheongang, had not been enough. Now they had an unidentified old monster who had achieved Returned to Youth as well. He almost missed the days when he had known nothing about it.

Seeing their godlike Stronghold Lord show such weakness, the senior river bandit asked anxiously,

“At this rate, are we ever going to make it back to Sichuan? We’ve already been away from the Water Dragon Stronghold for nearly two months. I’m worried it might stay vacant forever.”

“Don’t say such unlucky things. They say that even if you enter a tiger’s den, you can survive as long as you keep your head.”

“That works for a tiger. But against a Returned to Youth Supreme Peak master, I don’t think keeping your head a hundred times would do a thing…”

Come to think of it, he was right.

Mu Song quietly closed his mouth, unable to think of a reply.

That was when a voice came from behind him.

“I brought the liquor barrel. Where should I put it?”

Only one person in this situation would talk about a liquor barrel.

Irritation surged through Mu Song. Without even turning around, he snapped,

“Now that I’ve been letting this slide, that worthless bastard has been—”

“Did you just call me a worthless bastard?”

“……Huh?”

An instant that felt like an eternity.

At the sight of the senior river bandit staring over his shoulder with his mouth hanging open, Mu Song realized that he was thoroughly fucked.

At the same time, he remembered one fact he had forgotten.

*Ah. I left a spare liquor barrel at the stern.*

No wonder that subordinate had started to say something when Mu Song told him to bring another one, then stopped.

Mu Song’s vision blurred.

He had not even felt afraid when he was caught in the whirlpool at Tianling Falls. But now, he was sweating hard enough to wash his neck in it.

“Great Hero Mu Song.”

Mu Song squeezed his eyes shut, then slowly turned around with a forced smile.

The one person he never wanted to meet, even in his dreams, was standing there.

“O-oh, Mungyeong. W-what brings you here?”

“Nothing in particular.”

Mungyeong smiled brightly, like an ordinary boy his age, and answered,

“I was watching the Yangtze from the stern when your subordinate came over. I heard that Great Hero Mu Song had ordered him to bring a liquor barrel…”

“I-I did?”

“Didn’t you?”

“Well, I… I don’t remember giving such an order…”

At that moment, a river bandit appeared from behind Mungyeong with a barrel slung over his shoulder and called out briskly,

“Stronghold Lord! I brought the liquor barrel as ordered!”

Mu Song suppressed the urge to tear that subordinate’s mouth apart and continued,

“I… I do remember giving that order. Right. I did give it. It was obviously a mistake.”

“A mistake. I see.”

Mu Song felt Mungyeong’s gaze moving methodically over various parts of his body.

It had to be his imagination that made him feel as though Mungyeong was looking at his lethal acupoints.

It had to be.

Fortunately, perhaps his desperate wish had reached the heavens. Mungyeong soon withdrew his gaze and spoke.

“The enraged Great Hero Jeok was furious. He said that if something like this happened one more time, you had better be prepared.”

Of course, Jeok Cheongang had not gone berserk, nor had he said any such thing.

But Mu Song was not stupid enough to misunderstand what Mungyeong meant.

“Y-yes, I understand. Tell Great Hero Jeok that I’ll bear it in mind. But there is one thing…”

“Go ahead.”

“What should I do if there is something I absolutely have to take care of? Something needed for ship operations, for instance. Or meals.”

Mungyeong thought for a moment before answering,

“Great Hero Jeok told me to pass along further instructions. In the former case, Great Hero Mu Song is to come alone and take care of whatever needs doing. In the latter, you are to deliver the meals yourself.”

“……You mean I have to do all that alone?”

“Does that displease you?”

“It was my lifelong wish. I couldn’t be happier.”

“I see. Then I’ll be going now. I’ll see you at dinner.”

Mungyeong left Mu Song behind and started walking back toward the stern. Then he suddenly stopped and turned around.

“Oh, and one more thing.”

“What else? Is there still something you need to tell me?”

“Two portions will be enough for meals. All the way until we reach Henan.”

“Hmm?”

“Young Master Jin is going to have no appetite for the time being, so keep that in mind.”

There were still at least ten days until they reached Henan. No matter how poor his appetite was, going ten full days without eating was absurd.

Curiosity got the better of Mu Song, and he summoned his courage to ask,

“Um, did something happen to Junior Jin?”

“Oh.”

A dimple appeared beside Mungyeong’s mouth.

It was such a natural smile that even Mu Song, who considered him a monster, mistook him for an innocent boy for an instant.

“He must be busy right now. Very busy.”

* * *

Sometimes, I get the feeling I’ve become a human smartphone.

Like the warning message that tells you when your battery drops below fifteen percent, a similar System window had appeared in front of my eyes.

Beep.

> **System**
>
> - Most of your **internal energy** has been depleted.
>
> - **Circulate your qi** to replenish your internal energy. If your internal energy is completely depleted, you may suffer a Status abnormality!

But why?

If all my internal energy ran out right now, I would sink into the middle of this vast Yangtze. Yet instead of feeling a sense of crisis, I was more puzzled than alarmed.

And one reason for that was surely the presence of something approaching from far away.

Ssssh.

A large body was drawing closer with extraordinary stealth. The fin jutting above the surface looked oddly familiar.

*No, fuck.*

Why the hell was there a shark in the Yangtze?
```

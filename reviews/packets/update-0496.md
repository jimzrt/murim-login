<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0496.txt",
      "sha256": "9419ca23ce5b53bb06b7aaebd61b61155de89a2dd5734c4ab9dc2042f5022a0e",
      "bytes": 14328
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "614fc74bff2c7a1ae0fba84eab6cba506dbd18d8dbe4ac06a9e362448273da01",
      "bytes": 4877
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "d22c2b8f7b9189c4556e810db36d8280ef9bbfd0ee329fde6e15872395b7c26b",
      "bytes": 157932
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "de6788b4ae3e7831b7a6950c23ef0142c6c21010d96aca5c8d79425dabc4eafc",
      "bytes": 553
    },
    {
      "path": "characters/Gung Gibang.md",
      "sha256": "1a2bf1048f34652fc43e05a7185781fe5e78585533f303e58d35de61ee539f5c",
      "bytes": 686
    },
    {
      "path": "characters/Hyeongong.md",
      "sha256": "86cf4266b7671346900bec969edb6b8e558aa31c9b0f987bb4e4b214152f04ea",
      "bytes": 768
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "ad2cff5938b682d7924d0f5fd20327b98b07a5b0f5b5add33f8c4ae0c8a454e2",
      "bytes": 1108
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "558d694e418500b9b692c59689fcfa3a005cbcef14a91bdcde2e4cb7d6c1aef6",
      "bytes": 1547
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "03b87d9bd166a5a1adbd0c6d2a72c5b549160dfb4bb5bdedc860f976551acdb2",
      "bytes": 1777
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "22c00936a678272b7b7f76b3614bfba6783937a504cdc7c9692ca4867738fe62",
      "bytes": 622
    },
    {
      "path": "characters/Mungyeong.md",
      "sha256": "7f151bd57c0be9d6c9edd9ea8a3bdbf73a11477996069e869610c1f82ce77ed8",
      "bytes": 885
    },
    {
      "path": "characters/Zhuge Feng.md",
      "sha256": "d739c8035331cbf28a604fdb55a7c57f5610c40aa3b8e6529634cff86d614aaf",
      "bytes": 649
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "fcd89ef22d5cd9bc5646cb7dfc2a01c58c5dc8bb04ac6b55736f44af7216f5ad",
      "bytes": 153645
    }
  ],
  "estimated_tokens": 13812
}
-->

# Durable State Update — Chapter 496

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 496. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 496. Profile updates may replace only one
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
  "chapter": 496,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 496,
    "continuity_sources": [496],
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
    "The functionally crippled Gate continues leaking faint mana; its residual mana is mutating local life, and the Water God Dragon absorbed all of that mana.",
    "Around one hundred Level 5 Mutated Minnows, locally called Blood Fish, have been captured in the Gate's entrance waterways; the remaining population is unknown, and the fish fight and kill one another.",
    "Taekyung suspects Dark Heaven's regeneration, teleportation, and Moving Formation are manifestations of Magic connected to the Gate.",
    "Taekyung told Jeok that he came from another world, that an evil force from it is linked to Dark Heaven, that the corrupted imugi was their work, and that a fully opened Gate could release monsters.",
    "Honglan corrupted the benevolent Dongting Lake imugi and used it to kill many people; the severely injured Dongting Fisherman may be connected to Dark Heaven and the earlier destruction inside the secret refuge.",
    "The Southern Heaven Demon Empress is traveling toward Yunnan and expects to cause further deaths.",
    "Jin Wikyung and Gung Gibang pledged the Jin Family of Taiyuan and the Beggars' Sect to Taekyung's defense.",
    "Jeok's innate qi is damaged and steadily diminishing despite the Thousand-Year Snow Ginseng and the Divine Physician's treatment; Taekyung is now uncertain whether Jeok recovered without lasting aftereffects.",
    "Mungyeong is the Slaughter Saint, a Returned to Youth Supreme Peak master and the greatest assassin in history; before becoming the Slaughter Saint, he was called Killing Ghost, and he saved countless people as the Divine Physician.",
    "Mungyeong recognizes Taekyung's Heavenly Martial Physique as innate and distinct from Cheongpung's more refined physique.",
    "Mungyeong is testing Taekyung through successive poisoned traps and concealed attacks, intending to teach secret martial arts without a formal Master-Disciple relationship and to correct Taekyung's complacency.",
    "Taekyung detoxified Potent Seven-Step Soul-Chasing Powder, but Sinews and Meridians damage permanently reduced Strength and Agility by 5 each; he has stored the Water God Dragon's dismantled materials and Origin Essence in his inventory."
  ],
  "continuity_sources": [
    495,
    494
  ],
  "open_questions": [
    "What lies beyond the exposed Gate, why has it lost most of its functions, and how far has its residual mana's mutation spread?",
    "What is the Lord of Heaven's identity, and how is he connected to the dangerous force Taekyung associates with his original world?",
    "Where is the Southern Heaven Demon Empress ultimately headed, and what does she intend to do in Yunnan?",
    "What is the Dongting Fisherman's exact role within Dark Heaven, and how was he connected to the earlier destruction inside the secret refuge?",
    "Has Jeok fully recovered from the Formless Ultimate Poison, and will Taekyung use the Water God Dragon's Origin Essence to aid him?"
  ],
  "safe_through": 495,
  "temporary_decisions": [
    "Render 산공독 as Energy-Dispersing Poison, 강력한 산공독 as Potent Energy-Dispersing Poison, 칠보추혼산 as Seven-Step Soul-Chasing Powder, 강력한 칠보추혼산 as Potent Seven-Step Soul-Chasing Powder, 심각한 복통 as Severe Stomachache, 고기 방패 as Meat Shield, 독 장아찌 as Poisoned Pickle, and 독의 as Poison Physician; retain secret martial arts, Master-Disciple relationship, Killing Ghost, and Fake Murim Martial Artist, and preserve 악 as Agh in the Quest interface.",
    "Render 기억의 파편 as Memory Fragment, 게이트 공략 as Gate Conquest, 텔레포트 as Teleport, 마법 as Magic, 혈어 as Blood Fish, and 변이된 송사리 as Mutated Minnow; render 강력한 마비산 as Potent Paralysis Powder, 강력한 미혼산 as Potent Soul-Bewitching Powder, 전신 마비 as Full-Body Paralysis, 독성 흡수 as Poison Absorption, and 해독 as Detoxification.",
    "Render 시산혈해 as sea of corpses and blood and retain Old Master for 노야 with the established rough, profane Taekyung-Jeok banter; render 해시 as hour of the Pig, 한 식경 as half an hour, 타구봉 as Dog-Beating Staff, 창룡 as Azure Dragon, and 무량수불 as Infinite Life Buddha; preserve geun as the traditional weight unit with a footnote.",
    "Render 선천지기 as innate qi, 진원진기 as true-origin qi, and 천기 as heavenly patterns.",
    "Render 심마 as Heart Demon, 비급 as martial arts manual, 송문고검 as Pine-Pattern Ancient Sword, 반로환동 as Returned to Youth, 강강수월래 as Ganggangsullae, 생사부 as Book of Life and Death, 기막 as qi curtain, 무극태을검 as Martial Extremity Grand Unity Sword, 이룡 as Two Dragons, 원정 as Origin Essence, 내단 as inner core, 영험한 기운 as sacred energy, and 대호 as great tiger."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 무당파    | **Wudang**                       |
| 암천     | **Dark Heaven**                  |
| 제갈세가   | **Zhuge Clan**                   |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 가주     | **Family Head**                              |
| 사천     | **Sichuan**            |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 소협      | **Young Hero**                                                  |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 궁기방 | **Gung Gibang** | Beggars' Sect Successor Beggar and finalist. |
| 현공진인 | **Perfected Being Hyeongong** | Veteran Wudang Daoist master and the current Sect Leader's Junior Brother. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 문경 | **Mungyeong** | Young medical apprentice and newly introduced passenger. |
| 제갈풍 | **Zhuge Feng** | Current Family Head of the Zhuge Clan. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 마기 | **demonic qi** | Demonic energy discussed as a possible effect of the pill. |
| 주신 | **God of Drinking** | Wipeng's drinking epithet. |
| 개방 | **Beggars' Sect** | Murim organization counted among the Nine Sects and One Gang. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 제갈무후 | **Zhuge Wuhou** | Honorific title for Zhuge Liang in the Three Visits allusion. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 반로환동 | **Returned to Youth** | Possible explanation for an apparently young Supreme Peak master. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 골검 | **Bone Sword** | Sword wielded by the Skeleton Knights. |
| 미미 | **Mimi** | Worker at Honghwaru referenced in Taekyung's joke. |
| 호북 | **Hubei** | Province on Ju Gongsan's route from Guangdong to Henan. |
| 악귀 | **Fiend** | Descriptive epithet applied to the First Fiend. |
| 이무기 | **imugi** | Legendary serpent mentioned as the only comparable creature to a Thousand-Year Poison Horned Snake. |
| 와룡객 | **Crouching Dragon Guest** | Epithet of Zhuge Feng. |
| 호북성 | **Hubei Province** | Province where the chapter’s Dark Heaven incidents occurred. |
| 혈어 | **Blood Fish** | Local name for the aggressive mutated fish in the Gate's waterways. |
| 살귀 | **Killing Ghost** | Mungyeong's earlier sobriquet before he became the Slaughter Saint. |
| 제갈 | **Zhuge** | Surname used for Sir Zhuge. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 혁무진 | 적천강 | subordinate_to_overwhelming_elder | Great Hero Jeok | deferential and fearful | Mujin uses 적 대협 while reporting Jeok’s orders and Taekyung’s awakening. |
| 적천강 | 혁무진 | overwhelming_elder_to_junior_martial_artist | you stupid fool | blunt and mocking | Jeok calls Mujin a 멍청한 놈 after knocking him down during the attempted escape. |
| 궁기방 | 진태경 | rival_finalists | you bastard | insulting-casual | Gung Gibang answers Taekyung's collective insult with a profane threat. |
| 진태경 | 궁기방 | rival_finalists | you three idiots | insulting-casual | Taekyung addresses Gung Gibang as part of the trio and threatens them before a duel. |
| 진태경 | 문경 | young_martial_artist_to_medical_apprentice | Young Hero | formal-polite | Taekyung addresses the non-martial Mungyeong as 소협 while praising his actions. |
| 문경 | 진태경 | young_passenger_to_younger_martial_artist | Young Hero | deferential | Mungyeong uses 소협 while asking Taekyung for help boarding the ship. |
| 혁무진 | 궁기방 | squad_companion_to_Beggars_Sect_successor | Young Hero Gung | formal-polite, then pointed | Uses 궁 소협 while asking about the culprit and challenging Gung’s insults. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 문경 | 적천강 | old_acquaintances | Fire King | familiar and grave | The figure bearing Mungyeong’s name greets Jeok Cheongang by his established epithet. |
| 궁기방 | 혁무진 | squad_companions | you; that lunatic | insulting-casual | Gung Gibang mocks Hyuk Mujin's injuries and calls him a lunatic for attacking the Third Fiend. |
| 적천강 | 문경 | overwhelming elder to old acquaintance | you / little punk | mocking and threatening | Mocks Mungyeong's expression and threatens to poke out his eyes. |
| 적천강 | 제갈풍 | senior_martial_artist_to_old_acquaintance | you / ill-mannered brat | blunt, familiar, and teasing | Jeok treats Zhuge Feng as the younger acquaintance he remembers from childhood. |
| 제갈풍 | 적천강 | younger_old_acquaintance_to_legendary_senior | Senior | respectful but relaxed | Zhuge Feng recalls Jeok's earlier visit and addresses him as an old senior. |
| 제갈풍 | 진태경 | senior strategist_to_younger_martial_artist | you | calm and familiar | Uses 자네 while inviting Taekyung to continue questioning the Hubei incident. |
| 제갈풍 | 궁기방 | family_head_to_beggars_sect_successor | Successor Beggar | calm and conversational | Uses 후개 when confirming Gung Gibang's guess about the broken weapon. |
| 현공진인 | 제갈풍 | senior Wudang master to Zhuge Clan Family Head | Family Head Zhuge | formal-respectful | Uses 제갈가주 while discussing the fast ship and the route. |
| 제갈풍 | 현공진인 | Zhuge Clan Family Head to senior Wudang master | Perfected Being Hyeongong | formal-deferential | Addresses Hyeongong with marked respect and calls his presence a great reinforcement. |
| 진태경 | 미미 | rescuer to companion snake | Mimi or Mimi-chan | informal, pleading | Taekyung calls to Mimi while asking the snake to carry him and the survivors. |
| 제갈풍 | 문경 | old acquaintance to revealed legendary assassin | Slaughter Saint | excited and respectful | Zhuge Feng identifies Mungyeong by his established sobriquet after recognizing his identity. |
| 문경 | 제갈풍 | legendary_senior_to_younger_family_head | you; burden | blunt, insulting, and commanding | Mungyeong orders Zhuge Feng onto his back and dismisses his objections. |
| 적천강 | 궁기방 | overwhelming_elder_to_younger_martial_artist | you | blunt and threatening | Jeok Cheongang rebukes Gung Gibang for speaking informally and orders him to lie down. |
| 현공진인 | 진태경 | senior Wudang master to younger martial artist | young friend | gentle and polite | Hyeongong uses 진 도우 and 젊은 도우 while greeting and worrying about Taekyung. |
| 진태경 | 현공진인 | younger martial artist to senior Daoist master | Perfected Being | respectful and polite | Uses 진인 while responding to Hyeongong's religious instruction. |
| 진태경 | 제갈풍 | younger martial artist to senior clan head | Sir Zhuge | blunt and challenging | Uses 제갈 대협 while disputing Zhuge Feng's attempted ten-percent claim. |
| 문경 | 혁무진 | traveling_companion_to_traveling_companion | Martial Warrior Hyuk | formal-polite | Mungyeong asks Mujin to deliver water to Taekyung and lets Mujin receive the credit. |
| 혁무진 | 문경 | traveling_companion_to_traveling_companion | Mungyeong | casual-familiar | Mujin recognizes Mungyeong while reacting to Taekyung's dismantling work. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 495
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Gung Gibang.md

# Gung Gibang (궁기방)

- **Safe through:** Chapter 492
- **Aliases:** Successor Beggar, Beggar Prince, pure-blooded beggar, ultimate beggar
- **Role:** Gung Gibang is the Beggars' Sect Successor Beggar and a unique eight-knot disciple.
- **Personality:** Vulgar, aggressive, and quick-tempered.
- **Voice:** Blunt, profane, and vividly threatening.
- **Relationships:** Gung Gibang is a rival finalist alongside Baek Woo and Zhuge Gyun who trades insults with Taekyung, uses Beggars’ Sect intelligence to investigate Tang Taesang’s murder and Dark Heaven’s Hubei forces, and has now found a trace of Honglan.

### Hyeongong.md

# Perfected Being Hyeongong (현공진인)

- **Safe through:** Chapter 495
- **Aliases:** None
- **Role:** Perfected Being Hyeongong is a veteran Wudang Daoist master of the previous generation, the current Sect Leader's Junior Brother, and a Supreme Peak swordsman who reached the ultimate stage of the Taiji Wisdom Sword.
- **Personality:** Hyeongong is humble and self-deprecating about his limited worldly knowledge, carries the authority of an experienced senior master, and openly covets exceptional weapons.
- **Voice:** Measured, respectful, and lightly self-deprecating.
- **Relationships:** Hyeongong is the current Wudang Sect Leader's Junior Brother and a respected senior to Zhuge Feng.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 495
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers and Vice Squad Leader of the Jin Dragon Squad.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 495
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin and Furnace Fire Pure Blue, and Jin Taekyung's Master.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 494
- **Aliases:** Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, a Supreme Peak master who possesses the Heavenly Martial Physique and superhuman physical strength, has manifested Force, opened his Middle Dantian, crossed the wall into true mastery, can perceive the texture of qi well enough to sever layered magic, can resist high-level monster Fear through exceptional mental strength, is publicly recognized as an S-rank-level Hunter while formally retaining an A-rank license pending testing, and can command coordinated raids against powerful monsters.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate, student, and trusted manager of media and official arrangements, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, and Xiao Shen regards him as an older brother after Jin saved him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 494
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Mungyeong.md

# Mungyeong (문경)

- **Safe through:** Chapter 495
- **Aliases:** Killing Ghost
- **Role:** Mungyeong is the legendary physician known as the former Divine Physician and Slaughter Saint, a Returned to Youth Supreme Peak master and the greatest assassin in history who passed the Divine Physician title to his Disciple.
- **Personality:** Compassionate, resolute, resourceful, and calm under extreme pressure.
- **Voice:** His Mungyeong persona is timid, deferential, and cheerful, while his Slaughter Saint voice is dry, impassive, and blunt.
- **Relationships:** Dong Feng is his Disciple, Jeok Cheongang is an old acquaintance who asked him to look after and instruct Jin Taekyung, and Mungyeong is currently testing Taekyung before teaching him secret martial arts without a formal Master-Disciple relationship.

### Zhuge Feng.md

# Zhuge Feng (제갈풍)

- **Safe through:** Chapter 493
- **Aliases:** Crouching Dragon Guest
- **Role:** Zhuge Feng is the current Family Head of the Zhuge Clan and father of its Lesser Family Head, Zhuge Gyun.
- **Personality:** Analytical, disarmingly casual, eccentric, and inventive; he treats comfort and time as principles while delivering grave intelligence with unsettling directness.
- **Voice:** Clear, calm, polished, and conversational, with understated humor and pointed questioning.
- **Relationships:** Zhuge Gyun is his son, and Zhuge Gonghu was his grandfather.

## Korean source

```text
＃496화



“음.”

혁무진은 신중하게 붓을 들었다. 탁자 위, 미리 펼쳐 둔 소첩(小牒)에는 이미 며칠 전부터 적어 놓은 글자로 빼곡했다.



x월 x일. 날씨 지랄 같다가 맑아짐.

꿈을 꿨다. 용을 닮은 괴물이 나오는 악몽이었다. 얼마나 무서웠는지 자다가 오줌을 지렸다.

일어나자마자 속곳과 바지를 빨려고 몰래 개울가로 갔는데, 나보다 먼저 온 궁 소협이 똥 묻은 바지를 빨고 있었다.

더러운 인간 같으니. 거지도 이런 상거지가 따로 없다.

우리 조장님은 왜 굳이 바지에 똥이나 지리는 인간을 데리고 다니시는 건지 모르겠다.

그런데 왜 내가 의방에 있는 거지?



x월 x일. 날씨 맑음.

악몽이 사실이었다.

문경이의 말에 따르면 그 괴물의 정체는 이무기였고, 마기(魔氣)가 골수까지 치밀어 천인공노할 짓을 저질렀다고 했다.

다행히 조장님께서 나서 주신 덕분에 나는 그 마기의 영향을 거의 받지 않았지만, 당분간 일기를 꾸준히 쓰며 기억을 되짚으라는 진단을 받았다.

그나저나 그 말도 안 되는 광경들이 전부 사실이었다니.

듣던 중에 문득 의문이 떠올라 문경에게 물었다. 그 꿈, 아니지. 그 자리에서 싸우는 네 모습을 봤는데 그것도 전부 사실이었냐고.

문경은 아니라고 대답했다. 궁 소협도 합세해서 함께 물어보고 있었는데, 어째서인지 그대로 잠들어 버렸다. 피곤했던 모양이다.

그런데 왜 이마에 피멍이 들어 있지?

모르겠다. 다시 잠이나 자야지.



x월 x일.

사체를 처리하러 갔다. 이무기의 거대함에 한 번 지리고, 조장님의 도축 솜씨에 두 번 지렸다.

골검을 만들어 달라고 했다가 조장님께 골이 울리도록 맞았다.

뼈와 비늘, 살점으로 나뉜 이무기의 사체는 비밀리에 운송할 거라고 들었다.

아, 그리고 어째서인지는 몰라도 분류한 사체의 물량이 상당수 사라졌다.

진노한 현공진인께서 범인 색출을 천명했지만, 말도 안 되는 소리다. 주먹만 한 크기도 아니고 그 많은 양을 누가 훔쳐 간단 말인가.

그렇게 약간의 소란을 뒤로하고 돌아가는 배에 오르자, 어디선가 똥 냄새가 심하게 났다.

참다못해 내가 먼저 그 이야기를 꺼냈더니 말이 끝나기도 전에 조장님께서 궁 소협을 지목하셨다.

본인은 극구 아니라고 부인했지만, 며칠 전에 똥 지린 걸 목격한 나로서는 믿을 수 없는 소리다.

내 옆에 앉은 문경이는 시종일관 표정이 오묘했다.

똥 냄새 때문에 욕을 한 바가지 하고 싶은데 궁 소협의 체면을 생각해서 참는 거겠지.

착한 녀석 같으니. 언제 봐도 순진하고 정이 가는 녀석이다.



x월 x일.

이무기의 사체를 처리한 지 이틀이 지났다.

무슨 일 때문인지는 몰라도 적 대협은 통 보이지 않고, 조장님은 날이 갈수록 수척해지신다.

밤낮없이 독과 암습에 시달리는 사람 같다고 농담을 던졌더니 죽일 듯한 얼굴로 노려보셨다.

괜히 만만하니까 나한테만 난리야.

라고 생각했을 때, 궁 소협이 나와 같은 말을 했다가 맞는 걸 봤다. 기분이 좋아졌다.



x월 x일.

사흘 만에 다시 쓰는 일기다. 왜 그동안 뜸했냐 하면, 달리 쓸 만한 내용이 없었기 때문이다.

적 대협에 이어 조장님도 통 보기 힘들어졌고, 문경이도 어딜 자꾸 쏘다니는지 뜸하다.

나 같은 무인이 남는 시간 동안 뭘 하겠나. 궁 소협과 괜찮은 장소를 물색해 수련했다.

입 냄새가 시궁창 같아서 그렇지, 입 다물고 수련하니까 제법 나쁘지 않다.

반면 어떻게 알았는지 찾아온 청 소협의 조언은 하나같이 쓸모없었다.

무공에 관해 물어보면 돌아오는 대답은 딱 두 가지였다.

그거 되게 쉬워요. 그게 왜 안 돼요?

이 인간아. 그렇게 쉽게 됐으면 내가 아직도 일류겠냐.

답답했는지 시범을 보여 주는데 도통 모르겠다.

수련할 때마다 미미인지 하는 물뱀 놈은 옆에서 혈어(血魚)를 삼키는데, 그래서인지는 몰라도 덩치가 꽤 커진 것 같다. 뿔도 그렇고.

어쩐지 혈어의 씨가 말랐다 싶더니, 저놈 주둥이로 싹 다 들어간 모양이다.



x월 x일.

제갈세가와 무당파의 무인들 몇몇과 제법 친분을 쌓게 됐고, 그 덕분에 몇 가지 소식을 전해 들었다.

제갈세가는 와룡객 제갈풍 대협의 진두지휘 하에 그 틈새를 완전히 틀어막을 진법을 시험 중이라고 한다.

듣기로는 그걸 못 막으면 혈어 같은 괴상한 것들이 계속 생겨날 거라는데, 암천 놈들은 도대체 무슨 기괴막측한 수법으로 저런 것을 만들었는지 모르겠다.

반면 무당파에서는 여전히 그 살귀(殺鬼)를 추적 중이라고 했다.

관부까지 합세해서 호북성을 이 잡듯이 뒤지는데도 색출해 내지 못하는 걸 보면 도망치는 데에 도가 튼 놈임이 분명하다.



x월 x일.

이곳에 온 지 칠 주야째다. 오랜만에 만난 조장님의 안색은 평온했다.

전에는 혼자서 무슨 수련을 하시는 건지 몸에 상처도 많고, 안색도 창백하거나 푸른 빛이 돌았는데 이제 괜찮아지신 모양이다.

그 대신 성격이 좀 날카로워지셨고, 걸음걸이가 유령처럼 변했다.

어찌나 기척을 내지 않는지, 궁 소협과 조장님 욕을 하다가 걸려서 뒈지게 얻어맞았다.

아니, 도대체 그 거리에서 어떻게 욕하는 걸 들었던 거지?

그나저나 맞던 와중에 문경이 만족스러운 표정을 짓던데…… 아마도 착각이겠지.



“으음.”

약 열흘 동안 보고 겪은 일을 적은 일기는 거기까지였다.

그리고 소첩을 가만히 내려다보며 곰곰이 생각에 잠겨 있던 혁무진이 붓으로 첫 획을 그으려던 순간, 밖에서 소란스러운 외침이 들려왔다.

“돼, 됐다!”

“가주님! 저희가 해냈습니다!”

“자네들이 아니라 내가 해낸 걸세! 역시 나는 천재야! 제갈무후시여!”

삐끗! 찍!

마음이 흐트러지니 손이 엇나가고, 손이 엇나가니 붓도 휘청였다.

대문호(大文豪)의 마음가짐으로 글을 쓰려던 혁무진의 얼굴이 와락 일그러졌다.

“대체 어느 놈이!”

분노하는 혁무진의 귓가로 익숙한 목소리가 파고들었다.

“네가 말하는 그놈이 제갈풍 대협이신 것 같은데. 전해 드릴까?”

“어디 한번 해 보십쇼. 그때는 궁 소협 죽고 나 죽는 거지.”

허락도 없이 막사 안으로 들어온 궁기방을 향해 퉁명스럽게 대꾸한 혁무진이 붓을 내려놓았다.

“그런데 밖에는 대관절 무슨 일이랍니까?”

“제갈세가에서 그 틈새를 완전히 틀어막는 것에 성공한 모양이야.”

“진법으로요?”

“그럼 바위로 막겠냐?”

“참나. 못 막을 건 또 뭡니까.”

“근본적인 해결책이 아니잖아. 그리고 그런 식으로 처리할 수 있었으면 진작 틀어막았겠지. 생각을 좀 하고 말해라.”

“아, 그래요? 평소에 생각이 많으셔서 똥 지린 겁니까?”

“오줌 지린 개가 똥 지린 개 나무라는 격이군.”

“똥보단 오줌이 낫죠. 그리고 궁 소협은 두 번이나 쌌잖아요. 지난번에 이무기 사체 처리하러 갔을 때…….”

“와, 진짜 미치겠네. 그거 나 아니라니까!”

가슴을 쾅쾅 두드리는 궁기방의 모습을 본 혁무진이 혀를 찼다.

“거, 발뺌도 정도껏 하셔야지.”

“진짜라고!”

“궁 소협이 아니면 누굽니까? 예? 설마 현공진인께서 쌌겠어요?”

“진태경! 분명히 그놈한테 똥 냄새가 진동했, 헉!”

미처 말을 잇지 못하고 소스라치게 놀란 궁기방이 주위를 둘러보았다.

안 그래도 불과 며칠 전 비슷한 이야기를 하다가 매타작을 겪은 그였다.

“어, 없지?”

혁무진도 덩달아 마른침을 꿀꺽 삼켰다.

그가 아는 진태경은 누가 먼저 욕을 했건 간에 사이좋게 조지는 화끈한 성격의 소유자였다.

“아, 아마도?”

“확실해?”

“그걸 제가 어떻게 압니까. 조장님 기척 눈치챌 정도면 이미 초절정 고수죠. 아니면 유령이거나.”

촉각을 곤두세운 채 주변을 살피던 두 사람은 한숨을 푹 내쉬었다.

고작 말 몇 마디하고 눈치를 보는 자신들의 처지에 문득 허탈함이 밀려왔다.

“우리 언제까지 이렇게 살아야 하냐?”

“조장님 돌아가실 때까지요.”

“만약에 그놈이 나중에 반로환동(返老還童)이라도 하면?”

“혀 깨물고 자결해야죠. 별수 있습니까?”

“빌어먹을. 진태경 그놈은 진짜 괴물이야. 어떻게 그럴 수 있지?”

혁무진은 격하게 고개를 끄덕여 동의했다. 진태경이 망나니였던 시절부터 봐 왔던 그였기에 공감이 되지 않을 수 없었다.

“그건 맞죠. 그것도 하나도 아니고 둘씩이나.”

“청 소협? 그 인간 이야기는 꺼내지도 마. 몇 번 보더니 취팔선권(醉八仙拳)을 엇비슷하게 따라 하더군. 스승님이 아셨다면 문파 비전을 유출했다고 죽이려 드실 거야.”

“오오.”

“……방금 네놈이 무슨 생각을 했는지는 대충 알겠는데, 영원히 입 다물어라. 나 진짜 죽는다.”

“오오오.”

“이런 개 같은 놈을 보았나.”

고개를 절레절레 흔든 궁기방이 불쑥 입을 열었다.

“그런데 네 주군은 뭘 하느라 통 안 보여?”

“저야 모르죠. 수련인 것 같기도 하고, 아닌 것 같기도 하고. 온종일 막사에만 머무르실 때도 있어요.”

“진 대협이야 뭐 원래 이래저래 바쁘시고, 적 대협은 한참 안 보이시던데.”

적천강은 이곳에 도착한 첫날 이후로 완전히 자취를 감췄다.

많은 이가 그의 거취를 궁금해했지만, 안위를 걱정하는 사람은 아무도 없었다.

화왕. 그 두 글자만으로도 스스로를 증명하는 인물이니까.

“천하의 화왕을 누가 해하기라도 하겠습니까?”

“하긴. 제아무리 암천이라 해도 어림없지. 그분을 어찌하려 했다간 기둥뿌리 서너 개는 뽑히고, 이미 주위가 초토화되고도 남았을 거야.”

고개를 끄덕여 수긍한 궁기방이 말을 이었다.

“잠깐. 그러고 보니 요새 문경이도 통 안 보이던데?”

“그러게요. 가끔 볼 때마다 조장님과 함께 있더라고요.”

“그래?”

“예. 아무래도 수련 중에 입은 부상 때문이 아닐까 싶은데…….”

“흠.”

“왜 그러세요?”

“아냐. 냄새가 나.”

“또 지리셨어요?”

“혁무진 이 미친놈아. 그게 아니라. 둘 사이에 뭔가 있다 이 말이지.”

골똘히 생각에 잠겨 있던 궁기방이 문득 미간을 좁혔다.

“잠깐, 설마!”

“설마 뭐요.”

“아직도 모르겠냐? 왜 요즘 들어 두 사람이 종종 함께 있는지?”

혁무진의 표정이 오묘해졌다.

가만히 궁기방의 말을 듣다 보니 짚이는 구석이 있던 것이다.

“그렇다면 혹시…….”

“네가 생각한 그게 맞다.”

“허어. 이럴 수가.”

“생각해 보면 이상한 일이지. 우리에게는 심심하면 주먹을 날리면서, 문경이 녀석에게는 단 한 번의 폭력도 행사하지 않았어.”

“언제부턴가 욕도 거의 안 합니다. 그리고 지난번에 이무기 사체를 처리하러 갔을 때도 수상했어요.”

“진태경이 사라졌을 때, 문경이도 자리에 없었지.”

“맞습니다! 역시 개방의 차기 방주!”

“확실하군. 문경이 그 녀석…….”

궁기방이 딱딱하게 굳은 얼굴로 입을 열었다.

“진가 녀석에게 무공을 배우고 있는 것이 분명해.”

“아아, 문경아! 어쩌다가 그런 끔찍한 선택을!”

혁무진은 진심으로 안타까웠다. 하얗고 깨끗한 백지 같은 문경에게 진태경이라는 먹물이 스며든다고 생각하니 가슴이 찢어졌다.

“그 어린애가 무슨 죄가 있다고!”

“허어, 통탄할 일이로군. 사천에 계신 신의를 뵐 면목이 없어.”

“문경, 문경이는 안 됩니다! 우리와 같은 길을 걷게 할 수는 없어요!”

“이미 엎질러진 물이야. 진태경은 악귀다. 그런 사악한 놈의 손아귀에 떨어진 이상 우리가 손 쓸 방법이 없어.”

“그럼 지금쯤 문경이는…….”

“후우…….”

“아아…….”

두 사람은 동시에 한숨 섞인 탄식을 내뱉었다.

지금쯤 진태경의 마수(魔手)에 의해 죽을 고비를 넘기고 있을 문경을 생각하니, 마음이 천근만근 무거워졌다.

‘문경아. 부디 살아남거라.’



* * *



‘제발 누가 좀 살려 줘.’

서걱!

한 줄기 바람이 목을 스친다.

얼음장처럼 차가웠다가 이내 뜨겁게 달아오르는 통증. 이마를 타고 흘러내린 식은땀 한 방울이 지면으로 툭, 하고 떨어진다.

쉬릭, 타닥!

허공에서 신형을 바로세운 나는 똑바로 정면을 응시했다.

“방금 건 좀 위험했는데요.”

답하는 목소리, 아니 전음(傳音)이 있었다.

- 위험하라고 한 것이다.

“아니, 장난이 아니라 진짜 죽을 뻔했다니까요.”

- 듣던 중 반가운 소식이로군.

도대체 어디일까.

아무리 주위를 둘러봐도 보이지 않는다. 그저 어디서 들려오는지 모를 전음만이 있을 뿐.

“후, 시벌.”

- 뭔 벌?

크게 심호흡한 나는 백염의 창대를 말아쥐었다.

보이지 않는 어딘가에서 나를 지켜보고 있을 누군가를 향해, 씹어뱉듯이 중얼거렸다.

“개 같아서 못해 먹겠네, 진짜.”

쉬잉!

대답 대신 눈부신 검격이 날아들었다.
```

## Final English reading copy

```markdown
# Chapter 496

“Hmm.”

Hyuk Mujin picked up his brush carefully. The small booklet he had spread out on the table was already packed with writing he had begun several days earlier.

X Month X Day. The weather was a damn mess, then cleared up.

I had a nightmare. It was about a monster that looked like a dragon. It was so frightening that I wet myself in my sleep.

As soon as I woke up, I secretly went to the stream to wash my undergarments and trousers, only to find Young Hero Gung already there, washing a pair of shit-stained trousers.

What a filthy bastard. Even a beggar could be more respectable than him.

I have no idea why our Captain insists on dragging around someone who shits his pants.

But why am I in the infirmary?



X Month X Day. Clear skies.

The nightmare was real.

According to Mungyeong, the monster was an imugi, and demonic qi had surged all the way into its marrow, driving it to commit an atrocity that outraged heaven and humanity.

Fortunately, thanks to the Captain stepping in, I was barely affected by the demonic qi. However, I was diagnosed with the need to keep writing in my diary and retracing my memories for the time being.

That aside, I couldn’t believe those ridiculous scenes had all been real.

While listening to Mungyeong, a question suddenly occurred to me. I asked whether that dream—no, whether the sight I had seen of him fighting there had also been real.

Mungyeong answered that it had not. Young Hero Gung joined me in questioning him, but for some reason, I fell asleep on the spot. I must have been tired.

But why do I have a bruise on my forehead?

I don’t know. I should go back to sleep.



X Month X Day.

I went to dispose of the corpse. I shit myself once at the imugi’s enormous size, then a second time at the Captain’s butchering skills.

I asked him to make me a Bone Sword and got beaten until my skull rang.

I heard that the imugi’s corpse, divided into bones, scales, and flesh, would be transported in secret.

Oh, and for some reason, a considerable amount of the sorted remains disappeared.

Perfected Being Hyeongong, enraged, declared that he would find the culprit. But that was ridiculous. It wasn’t a fist-sized amount. Who could steal that much?

After leaving the minor commotion behind and boarding the boat back, I noticed a terrible smell of shit coming from somewhere.

Unable to stand it any longer, I brought it up first. Before I could even finish speaking, the Captain pointed at Young Hero Gung.

He vehemently denied it, but having witnessed him shit himself a few days ago, I couldn’t believe a word he said.

Mungyeong, sitting beside me, wore an odd expression the entire time.

He probably wanted to unload a bucketful of abuse because of the smell, but was holding back out of consideration for Young Hero Gung’s dignity.

What a good kid. He’s so innocent and endearing every time I see him.



X Month X Day.

It has been two days since we disposed of the imugi’s corpse.

I don’t know what happened, but Sir Jeok has disappeared completely, and the Captain grows gaunter by the day.

I joked that he looked like someone being tormented by poison and ambushes day and night, and he glared at me as though he wanted to kill me.

He only makes a fuss at me because I look easy.

Just as I was thinking that, Young Hero Gung said the same thing and I watched him get beaten. I felt better.



X Month X Day.

This is the first time I’ve written in three days. The reason I neglected my diary was that there was nothing worth writing about.

After Sir Jeok, the Captain also became difficult to see, and Mungyeong has been wandering off somewhere or other, so he is rarely around too.

What would a martial artist like me do with his free time? Young Hero Gung and I searched for a decent place and trained.

His breath smells like a sewer, but when he keeps his mouth shut during training, he’s not so bad.

On the other hand, Young Hero Cheongpung’s advice, despite somehow finding us, was useless every time.

Whenever I asked him about martial arts, I got one of two answers.

“It’s really easy.”

“Why can’t you do it?”

You bastard. If it were that easy, would I still be First Rate?

Perhaps because he was frustrated, he demonstrated it for me, but I couldn’t understand a thing.

Every time we trained, that water snake called something like Mimi swallowed Blood Fish beside us. Maybe because of that, he seems to have grown quite a bit. His horns have grown too.

No wonder it seemed as though the Blood Fish had gone extinct. They must have all gone down that bastard’s throat.



X Month X Day.

I’ve become fairly close with several martial artists from the Zhuge Clan and Wudang, and thanks to that, I heard some news.

The Zhuge Clan is testing a formation under the direct command of Sir Zhuge Feng, the Crouching Dragon Guest, apparently one that can completely seal the gap.

I hear that if they can’t block it, strange things like the Blood Fish will continue to appear. I have no idea what bizarre and unfathomable method those Dark Heaven bastards used to create them.

Meanwhile, Wudang is still tracking the Killing Ghost.

Even with the authorities joining the search and turning Hubei Province upside down, they still haven’t found him. He must be an expert at running away.



X Month X Day.

It has been seven days and nights since I came here. The Captain’s complexion was calm when I saw him again after so long.

Before, he had been covered in injuries from whatever training he was doing alone, and his complexion had been pale or even bluish. He seems to have recovered now.

Instead, his temper has grown sharper, and he moves like a ghost.

He gives off so little sign of his presence that he caught Young Hero Gung and me bad-mouthing him and beat us within an inch of our lives.

No, seriously. How did he hear us from that distance?

Come to think of it, Mungyeong had a satisfied expression while I was being beaten…

I must have imagined it.



“Hmm.”

That was as far as the diary recording everything he had seen and experienced over roughly ten days went.

Hyuk Mujin stared down at the small booklet and sank into thought. Just as he was about to draw the first stroke of a new entry, noisy shouts came from outside.

“It worked—it worked!”

“Family Head! We did it!”

“Not you—I did it! As expected, I’m a genius! Zhuge Wuhou!”

Screech! Blot!

His concentration wavered, his hand slipped, and the brush shook.

Hyuk Mujin’s face twisted as he tried to write with the mindset of a great literary master.

“Which bastard was that?”

A familiar voice slipped into his ear as he raged.

“The bastard you’re talking about sounds like Sir Zhuge Feng. Shall I pass along your words?”

“Go ahead. Then Young Hero Gung dies, and I die right after him.”

Hyuk Mujin answered gruffly and put down his brush as Gung Gibang entered the tent without permission.

“But what on earth is going on outside?”

“It looks like the Zhuge Clan succeeded in completely sealing the gap.”

“With a formation?”

“What else? Rocks?”

“Oh, come on. Why couldn’t we block it with rocks?”

“It’s not a fundamental solution. And if it could have been handled that way, they would have sealed it long ago. Think before you speak.”

“Oh, really? Do you shit yourself because you think too much?”

“A dog that pissed itself criticizing a dog that shit itself.”

“Pissing is better than shitting. Besides, Young Hero Gung did it twice. Last time, when we went to dispose of the imugi’s corpse…”

“Ah, this is driving me crazy. I told you, that wasn’t me!”

Hyuk Mujin clicked his tongue as Gung Gibang pounded his chest.

“You should know when to stop denying it.”

“I’m telling you, it’s true!”

“If it wasn’t Young Hero Gung, then who was it? Hmm? Surely you don’t think Perfected Being Hyeongong did it?”

“Jin Taekyung! I swear that bastard reeked of shit—gah!”

Gung Gibang suddenly stopped, his face going pale as he looked around.

Only a few days earlier, he had been beaten half to death after having a similar conversation.

“He’s not here, right?”

Hyuk Mujin swallowed dryly as well.

The Jin Taekyung he knew had a fiery personality. Whoever started the insults, he would happily beat both sides senseless.

“P-probably?”

“You’re sure?”

“How would I know? If you can sense the Captain’s presence, you’re already a Supreme Peak master. Or a ghost.”

The two of them looked around with every sense on high alert, then let out deep sighs of relief.

Suddenly, the absurdity of their situation struck them. They had become afraid after saying only a few words.

“How long are we going to live like this?”

“Until the Captain dies.”

“What if he undergoes Returned to Youth later?”

“Then we bite our tongues and kill ourselves. What else can we do?”

“Damn it. That Jin Taekyung bastard is a real monster. How can anyone be like that?”

Hyuk Mujin nodded vigorously in agreement. He had watched Jin Taekyung since the days when he had been a delinquent, so he couldn’t help but sympathize.

“That’s true. And not just one of them—there are two.”

“Young Hero Cheongpung? Don’t even get me started. After seeing the Drunken Eight Immortals Fist only a few times, he started imitating it pretty closely. If my master found out, he’d try to kill me for leaking our sect’s secret art.”

“Ooh.”

“……I have a fairly good idea what you were just thinking, but keep your mouth shut forever. I’m really going to die.”

“Oooh.”

“You vile bastard.”

Gung Gibang shook his head and suddenly spoke.

“But what is your liege doing? I haven’t seen him at all.”

“I wouldn’t know. He may be training, or he may not. Sometimes he stays in his tent all day.”

“Sir Jin is always busy with one thing or another, and I haven’t seen Sir Jeok in a long time.”

Jeok Cheongang had completely vanished after the first day he arrived.

Many people were curious about his whereabouts, but no one was worried about his safety.

He was the Fire King. Those two words alone were proof enough.

“Who could possibly harm the Fire King?”

“True. Even Dark Heaven wouldn’t dare. If they tried anything, three or four of their pillars would have been ripped out, and the surrounding area would already have been reduced to ashes.”

Gung Gibang nodded in agreement and continued.

“Wait. Come to think of it, I haven’t seen Mungyeong around lately either.”

“Now that you mention it, neither have I. Whenever I see him, he’s with the Captain.”

“Really?”

“Yes. I wonder if it has something to do with the injuries the Captain suffered while training…”

“Hmm.”

“Why?”

“Nothing. Something smells fishy.”

“Did you shit yourself again?”

“Hyuk Mujin, you lunatic. That’s not what I mean. I’m saying there’s something going on between them.”

Gung Gibang narrowed his brow, deep in thought.

“Wait. Could it be?”

“Could what be?”

“You still don’t get it? Why those two have been together so often lately?”

Hyuk Mujin’s expression grew strange.

As he listened to Gung Gibang, something clicked.

“Then perhaps…”

“That’s exactly what you’re thinking.”

“Good heavens. How can this be?”

“If you think about it, it is strange. The Captain punches us whenever he gets bored, but he hasn’t used so much as a single act of violence against Mungyeong.”

“He barely curses at him anymore, either. And he was suspicious the last time we went to dispose of the imugi’s corpse.”

“When Jin Taekyung disappeared, Mungyeong wasn’t there either.”

“Exactly! The Beggars’ Sect’s future Sect Leader never disappoints!”

“Then it’s certain. Mungyeong…”

Gung Gibang’s face stiffened as he spoke.

“He must be learning martial arts from that Jin bastard.”

“Ah, Mungyeong! How did you end up making such a terrible choice?”

Hyuk Mujin was genuinely heartbroken. The thought of ink named Jin Taekyung bleeding into Mungyeong, who was as white and clean as a blank sheet of paper, made his chest ache.

“What sin did that child commit?”

“Alas, what a tragedy. I have no face to show the Divine Physician in Sichuan.”

“Mungyeong, Mungyeong can’t do this! We can’t let him walk the same path as us!”

“The water has already been spilled. Jin Taekyung is a Fiend. Now that Mungyeong has fallen into the hands of such an evil bastard, there’s nothing we can do.”

“Then by now, Mungyeong must be…”

“Whew…”

“Ah…”

The two of them let out sighs filled with simultaneous lament.

Thinking of Mungyeong, who must by now be fighting for his life under Jin Taekyung’s evil clutches, they felt their hearts grow heavy.

*Hang in there, Mungyeong. Please survive.*



* * *

*Please, somebody save me.*

Slash!

A current of wind grazed my neck.

The pain was as cold as ice, then immediately flared hot. A bead of cold sweat ran down my forehead and dropped onto the ground with a soft tap.

Whoosh, tap!

I righted myself in midair and stared straight ahead.

“That was a little dangerous.”

An answering voice came back—or rather, it was Sound Transmission.

—That was the point.

“No, I’m not joking. I really almost died.”

—That is welcome news.

*Where the hell is he?*

No matter how carefully I looked around, I couldn’t see him. There was only the Sound Transmission, impossible to locate.

“Fucking hell.”

—What kind of hell?

I took a deep breath and gripped the shaft of White Flame.

Toward whoever was watching me from somewhere unseen, I muttered as though spitting the words out.

“This is so fucking shitty I can’t keep doing this.”

Whoosh!

In place of an answer, a blinding sword strike flew toward me.
```

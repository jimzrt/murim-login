<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0370.txt",
      "sha256": "7b57ce66da591b76454aa348bf285dbb515675b2206686f7e19e19b5cc402380",
      "bytes": 14929
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "0b087bca30559f705d1b4942d0504823a0544bc301e46cf76279d6d0c80c1d0d",
      "bytes": 3086
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "8695ee04a9b5982dc667b52829c7c885744a08dfc713d418e390be96c8fc6fc7",
      "bytes": 129176
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "141e64c720590253ca9d3e6490df204f48568c2796f79664c2703891c8b2f1b2",
      "bytes": 1044
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "d4c572e4f835ebfa30ec876c5d059b4f4d25b055be24af6ea7e62360e9c0f920",
      "bytes": 690
    },
    {
      "path": "characters/First Fiend.md",
      "sha256": "ee6e49a584113ac6b51b08e6a4d9c7f86e55af20ab322ca99c78b5bb4aa69ef3",
      "bytes": 682
    },
    {
      "path": "characters/Gung Gibang.md",
      "sha256": "196eb92d0c6166ce33b0ebd48775bf258a7799847413170d24b5fee30211bfcb",
      "bytes": 674
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "7b49e75171f204aae8dfae43cbda5322bda9c11ddcea8d9db42498270849f838",
      "bytes": 1182
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "ceba021b11b50e22ddf2714fe0150b650522f525f31f8ce4c032a7a50106a6de",
      "bytes": 1516
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "30c772e75932aac8be776b8786f7ef805df42ad5c120898d02d428317ea5a8ac",
      "bytes": 1217
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "b9e9d678a5956e34e79e1777a38ec3823e80e2e8b6af8c1174c9213cbd9f7cc9",
      "bytes": 622
    },
    {
      "path": "characters/Mungyeong.md",
      "sha256": "0e2ca52cb938ae8c9ab75a7d54ab545f8bcb767455c369ef3ecbc57d4e0549fe",
      "bytes": 702
    },
    {
      "path": "characters/Qilian Three Fiends.md",
      "sha256": "e5c43b17e2aedad90284f7a43c49a2d9cd8223bca677353b9d099bab8c7bb38e",
      "bytes": 677
    },
    {
      "path": "characters/Tang Sadok.md",
      "sha256": "c68c75ca27e68e90612f6a0311b709281018ff6e507fa585ee3f4496527d9476",
      "bytes": 771
    },
    {
      "path": "characters/Venerable Myoryeong.md",
      "sha256": "dfd89b77381e7fc7d12100b182f44e329c875dc5eed8b8d08f3735056133d42d",
      "bytes": 605
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "0a6b715460e0c7da0846518fd952ed59a32ce54a7c50874d17542a692efaab89",
      "bytes": 97823
    }
  ],
  "estimated_tokens": 14363
}
-->

# Durable State Update — Chapter 370

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 370. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 370. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history.
`names` contains only newly required Korean-to-English rows that are absent from
Exact glossary matches; Korean keys must occur in the source. Do not repeat
glossary matches. The controller drops rows already in the names ledger.
`address_pairs` contains only newly required speaker→addressee rows that are
absent from Matched address pairs. Speaker and addressee must be Hangul source
spellings (Arabic digits allowed in titles such as 1팀장; do not romanize). At
least one endpoint must occur in the source. The controller drops pairs already
in the address ledger. Do not invent risk-register rows. Beat plot paragraphs
are plain strings; continuity and translation decisions are concise list items.
Return this exact shape:

{
  "chapter": 370,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 370,
    "continuity_sources": [370],
    "active_continuity": ["active fact"],
    "open_questions": ["unresolved question"],
    "temporary_decisions": ["temporary translation decision"]
  },
  "names": [
    {"korean": "source spelling", "english": "English rendering", "notes": "brief note"}
  ],
  "address_pairs": [
    {
      "speaker": "speaker Korean",
      "addressee": "addressee Korean",
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

## Prior durable context

```json
{
  "active_continuity": [
    "Jeok Cheongang escaped the collapsing underground prison carrying unconscious Jin Taekyung and the awakened Divine Physician; the Heavenly Power Demon’s corpse remained inside.",
    "The Divine Physician is Dong Feng, whose dantian and martial arts were destroyed while shielding Jeok Cheongang; the Slaughter Saint is Dong Feng’s Master.",
    "Jeok Cheongang remains severely weakened after exhausting his internal energy while protecting Taekyung and Dong Feng.",
    "Mungyeong, the Slaughter Saint, killed First Fiend and at least one other Qilian Fiend, and has now intercepted the surviving Third Fiend after disguising himself as First Fiend.",
    "The Third Fiend led the Dark Heaven attack on Emei, escaped the battle, and was wounded by Mungyeong near Chengdu; his fate is unresolved.",
    "Extinction Divine Nun, Heaven-Shaking Venerable Nun’s only Senior Aunt, is an alive Supreme Peak master who emerged from presumed death and forced the Third Fiend to flee Emei.",
    "Jin Taekyung is unconscious after exhausting himself while seeking to save Jeok Cheongang.",
    "Jin Taekyung has reached the Supreme Peak realm through enlightenment and manifested Force; the Fire Gate Divine Technique and Fire Dragon Divine Spear remain at the eighth stage, and White Flame remains in his possession.",
    "The Lord of Heaven temporarily possessed the Western Heaven Demon Lord’s body, which crumbled after One Annihilation; the possessing entity escaped after promising to return.",
    "The Myriad-Poison Ring remains in Jin Taekyung’s possession and cannot be appraised by the System.",
    "Cheongpung remains a Supreme Peak master and has begun treating the gravely wounded Tang Sadok with True Qi Guidance.",
    "Most Dark Heaven remnants from the Sichuan assault have been hunted down or captured, but the fate of the Second Fiend and the Third Fiend remains unresolved."
  ],
  "continuity_sources": [
    369
  ],
  "open_questions": [
    "What becomes of the Third Fiend after Mungyeong severs his wrist and confronts him?",
    "What happened to the Second Fiend who was assigned to the Qingcheng attack?",
    "What is the true nature and purpose of the Lord of Heaven, and what became of the Western Heaven Demon Lord?",
    "Can Jin Taekyung recover, and can Jeok Cheongang protect him and Dong Feng from Dark Heaven and the Slaughter Saint?",
    "What is the full nature of the Slaughter Saint’s connection to the identity or name Mungyeong?"
  ],
  "safe_through": 369,
  "temporary_decisions": [
    "Use Red Slaughter Demon and Red Slaughter Asura Net for 적살마 and 적살수라망; use First Captain for 일 단주 and deputy captain for 부단주.",
    "Use mechanism array for 기관진법.",
    "Maintain Cheongpung’s dreamy, childlike speech while rendering his copied techniques precisely.",
    "Use Ghost Illusory Slaughter Step for 유령환살보.",
    "Render 삼괴 as Third Fiend in singular contexts and Three Fiends only when the collective Qilian group is meant."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 청풍     | **Cheongpung**     |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 검성     | **Sword Saint**               | Mae Jonghak    |
| 암천     | **Dark Heaven**                  |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 중원     | **Central Plains**                               |                                                       |
| 장문인    | **Sect Leader**                              |
| 제자     | **Disciple**                                 |
| 전각     | **pavilion**                                 | Use “hall” only when established for a specific named building |
| 은인     | **Benefactor**                               |
| 시스템              | **System**                     |
| 명성               | **Fame**                       |
| 하남     | **Henan**              |
| 사천     | **Sichuan**            |
| 화산     | **Huashan**            |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 소협      | **Young Hero**                                                  |
| 도사      | **Daoist**                                                      |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 일괴 | **First Fiend** | The Qilian Three Fiend leading the Dark Heaven assault on the Sichuan Tang Clan. |
| 궁기방 | **Gung Gibang** | Beggars' Sect Successor Beggar and finalist. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 문경 | **Mungyeong** | Young medical apprentice and newly introduced passenger. |
| 기련삼괴 | **Qilian Three Fiends** | Three identical brothers from the Qilian Mountains. |
| 당사독 | **Tang Sadok** | Current Family Head of the Sichuan Tang Clan; also called the Myriad-Poison Asura. |
| 묘령 | **Myoryeong** | Dharma name of the middle-aged Emei nun. |
| 내상 | **Internal Injury** | System condition label for internal injury. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 개방 | **Beggars' Sect** | Murim organization counted among the Nine Sects and One Gang. |
| 청성파 | **Qingcheng Sect** | Sect named in Baek Museong's comparison about disciplinary rules. |
| 사천당문 | **Sichuan Tang Clan** | Martial clan cited for its poison-based cleansing method. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 아미타불 | **Amitabha** | Buddhist invocation spoken by the unidentified arriving group. |
| 천년독각사 | **Thousand-Year Poison Horned Snake** | Extremely venomous horned snake used to make Hong Dao's thirty-year-old liquor. |
| 후개 | **Successor Beggar** | Title of the Beggars' Sect successor competing in the preliminaries. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 천라지망 | **net over heaven and earth** | Jeok Cheongang's figurative threat to pursue a culprit everywhere. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 미미 | **Mimi** | Worker at Honghwaru referenced in Taekyung's joke. |
| 당문 | **Tang Clan** | Short form for the Sichuan Tang Clan. |
| 아미 | **Emei** | Short form for Emei Sect. |
| 아미파 | **Emei Sect** | Murim sect in Sichuan. |
| 청성 | **Qingcheng** | Short form for Qingcheng Sect. |
| 화산신룡 | **Huashan Divine Dragon** | Title given to Cheongpung after the Star-Array Grand Banquet. |
| 묘령사태 | **Venerable Myoryeong** | Honorific form for the injured Emei nun. |
| 미미쨩 | **Mimi-chan** | Affectionate form used for Tang Mimi. |
| 회오리치기 | **Whirlwind** | Technique Mimi-chan performs at Cheongpung's command. |
| 삼괴 | **Three Fiends** | Collective form used by the Western Heaven Demon Lord for the Qilian Three Fiends. |
| 뇌옥 | **underground prison** | The Tang Clan's subterranean prison. |
| 지풍 | **Finger Qi** | Invisible qi attack fired by the Western Heaven Demon Lord. |
| 삼문혈사 | **Three-Gate Bloodbath** | Name given to Dark Heaven’s coordinated assault on the Tang Clan, Qingcheng, and Emei. |
| 칠선자 | **Seven Fairies** | Emei’s seven foremost martial artists who deploy the formation. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
| 청풍 | 진태경 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung repeatedly addresses Taekyung as 은인 after receiving food. |
| 청풍 | 혁무진 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung includes Mujin among his 은인들 after receiving the skewers. |
| 혁무진 | 청풍 | martial artist to young master | Young Master | formal-deferential | Mujin uses 공자께서는 when asking why Cheongpung descended from the mountain. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 진태경 | 청풍 | companion_to_young_martial_artist | Young Master Cheongpung | formal-polite | Taekyung uses 청 공자 while correcting Cheongpung's royal-etiquette mistake. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 적천강 | 청풍 | overwhelming_elder_to_young_martial_artist | you / little punk | blunt, amused, and threatening | Jeok Cheongang uses 네, 이놈, and related blunt forms while testing Cheongpung. |
| 청풍 | 적천강 | young_martial_artist_to_overwhelming_elder | Grandpa Jeok | casual-familiar despite deference | Cheongpung uses 적 할아버지 while asking Jeok Cheongang to confirm Taekyung's condition; this is a familial form of address, not literal kinship. |
| 혁무진 | 적천강 | subordinate_to_overwhelming_elder | Great Hero Jeok | deferential and fearful | Mujin uses 적 대협 while reporting Jeok’s orders and Taekyung’s awakening. |
| 적천강 | 혁무진 | overwhelming_elder_to_junior_martial_artist | you stupid fool | blunt and mocking | Jeok calls Mujin a 멍청한 놈 after knocking him down during the attempted escape. |
| 상인 | 적천강 | merchant_to_legendary_martial_master | Great Hero Jeok | deferential and flattering | Praises Jeok Cheongang while presenting the Poison-Averting Ring and requesting help. |
| 적천강 | 상인 | legendary_guest_to_merchant | you | blunt and transactional | Cuts off the merchant’s praise, asks his identity and origin, and accepts the gift without committing to the requested favor. |
| 상인 | 청년 | stranger_to_stranger | Young Brother | formal-polite | A merchant uses 소형제 after noticing the young man's sword, and the young man approves of the address. |
| 청년 | 상인 | stranger_to_stranger | friend | casual and shameless | The young man declares that they should be friends after drinking their Yeoahong. |
| 궁기방 | 진태경 | rival_finalists | you bastard | insulting-casual | Gung Gibang answers Taekyung's collective insult with a profane threat. |
| 진태경 | 궁기방 | rival_finalists | you three idiots | insulting-casual | Taekyung addresses Gung Gibang as part of the trio and threatens them before a duel. |
| 진태경 | 문경 | young_martial_artist_to_medical_apprentice | Young Hero | formal-polite | Taekyung addresses the non-martial Mungyeong as 소협 while praising his actions. |
| 문경 | 진태경 | young_passenger_to_younger_martial_artist | Young Hero | deferential | Mungyeong uses 소협 while asking Taekyung for help boarding the ship. |
| 청풍 | 문경 | martial_companion_to_medical_apprentice | Medical Apprentice | cheerful-polite | Cheongpung addresses Mungyeong as 의생님 while asking him to greet the Tang Clan. |
| 진태경 | 당사독 | visitor_to_Sichuan_Tang_Family_Head | Great Hero Tang Sadok | formal-deferential | Taekyung formally introduces himself and addresses Tang Sadok as 대협. |
| 당사독 | 진태경 | Family_Head_to_visiting_younger_martial_artist | you; fearless brat | blunt and threatening | Tang Sadok uses 너 and later calls Taekyung 겁 없는 놈 while rejecting his challenge. |
| 청풍 | 당사독 | young_martial_artist_to_Sichuan_Tang_Family_Head | Family Head | formal-deferential | Cheongpung addresses Tang Sadok as 가주님 while appealing for help. |
| 혁무진 | 궁기방 | squad_companion_to_Beggars_Sect_successor | Young Hero Gung | formal-polite, then pointed | Uses 궁 소협 while asking about the culprit and challenging Gung’s insults. |
| 묘령사태 | 진태경 | injured_allied_nun_to_young_hero | Young Hero Jin | formal-deferential | Uses 진 소협 after recognizing that Taekyung already understands the likely connection between the attacks. |
| 당사독 | 문경 | Family Head to visiting medical apprentice | you | blunt and probing | Asks whether Mungyeong is the Divine Physician's Disciple. |
| 당사독 | 청풍 | family_head_to_younger_ally | greenhorn | blunt and protective | Tells Cheongpung not to interfere while calling him a 핏덩이. |
| 일괴 | 청풍 | enemy_to_assigned_target | greenhorn; brat | mocking and bloodthirsty | Calls Cheongpung the Sword Saint's successor and boasts that he will leave him barely breathing. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 문경 | 적천강 | old_acquaintances | Fire King | familiar and grave | The figure bearing Mungyeong’s name greets Jeok Cheongang by his established epithet. |

## Listed compact profiles

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 368
- **Aliases:** Huashan Divine Dragon
- **Role:** Twenty-three-year-old Huashan outsider, grandson and Disciple of Sword Saint Mae Jonghak, a Supreme Peak master who grievously wounded First Fiend before the Slaughter Saint killed him and then reached the wounded Tang Sadok to provide treatment.
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, a deep love of martial arts, and a martial artist's competitive pride; he becomes unsettled when someone copies his martial arts
- **Voice:** Dreamy and hazy, with innocent, polite phrasing
- **Relationships:** Mae Jonghak is his grandfather and martial instructor; Baek Museong is his Martial Nephew; Jin Taekyung and Hyuk Mujin are his Benefactors and companions, while Taekyung has become his only true martial rival; he now faces the unidentified newcomer Mungyeong after First Fiend’s death.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 369
- **Aliases:** Medicine Immortal
- **Role:** Legendary physician also known as Dong Feng and Mungyeong's Master, whose dantian and martial arts were destroyed and wrist broken while shielding Jeok Cheongang, and who is now awake and escaping with Jin Taekyung.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** The Slaughter Saint is his Master; Dong Feng is traveling with Jeok Cheongang and Jin Taekyung after being rescued from the underground prison.

### First Fiend.md

# First Fiend (일괴)

- **Safe through:** Chapter 369
- **Aliases:** Fiend
- **Role:** Leader of the Qilian Three Fiends and former commander of the Dark Heaven assault on the Sichuan Tang Clan, grievously wounded by Cheongpung and killed by the Slaughter Saint.
- **Personality:** Ruthless, sadistic, arrogant, and delighted by violence and destruction.
- **Voice:** Cackling, mocking, and openly threatening.
- **Relationships:** The Second and Third Fiends are his younger brothers; he served the Western Heaven Demon Lord and led the black-clad attackers against Tang Jinhu and the Tang Clan until his death.

### Gung Gibang.md

# Gung Gibang (궁기방)

- **Safe through:** Chapter 360
- **Aliases:** Successor Beggar, Beggar Prince, pure-blooded beggar, ultimate beggar
- **Role:** Beggars' Sect Successor Beggar and unique eight-knot disciple who remains at Dong Feng's hidden clinic with Hyuk Mujin to guard Venerable Myoryeong.
- **Personality:** Vulgar, aggressive, and quick-tempered.
- **Voice:** Blunt, profane, and vividly threatening.
- **Relationships:** Rival finalist alongside Baek Woo and Zhuge Gyun; trades insults with Taekyung and is helping investigate Tang Taesang’s murder through Beggars’ Sect intelligence.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 369
- **Aliases:** Swift Wind Sword
- **Role:** A Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers and Vice Squad Leader of the Jin Dragon Squad, and remains at Dong Feng's hidden clinic with Gung Gibang to guard Venerable Myoryeong.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 368
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** A legendary wandering martial master and Jin Taekyung's Master and intended heir to the Fire Gate Clan, Jeok Cheongang is awake but weakened and survived the confrontation with the Western Heaven Demon Lord.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, and casually threatening or violent when dissatisfied. His meeting with Taekyung rekindled his will to live, making him determined to extend his life despite his illness.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 369
- **Aliases:** Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, who has reached the Supreme Peak realm through enlightenment and manifested Force but is currently unconscious after exhausting himself to save Jeok Cheongang.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother; Jeok Cheongang is his Master; Cheongpung is his trusted companion and only true martial rival; his mother and sister Hayeon are among those he protects.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 369
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Mungyeong.md

# Mungyeong (문경)

- **Safe through:** Chapter 369
- **Aliases:** None
- **Role:** Young medical apprentice and Disciple of Dong Feng who arrived at the besieged Sichuan Tang Clan and killed First Fiend after Cheongpung wounded him.
- **Personality:** Compassionate, resolute, resourceful, and calm under extreme pressure.
- **Voice:** Initially timid and deferential, he becomes clear, composed, and eloquent when arguing for mercy and justice.
- **Relationships:** Dong Feng is his Master; Jeok Cheongang recognizes him as the Slaughter Saint, and he has now disguised himself as First Fiend to intercept the fleeing Third Fiend.

### Qilian Three Fiends.md

# Qilian Three Fiends (기련삼괴)

- **Safe through:** Chapter 369
- **Aliases:** Three Fiends
- **Role:** First Fiend and at least one other brother are dead; the Third Fiend, who led the Emei attack, escaped and was intercepted by Mungyeong, while the Second Fiend’s fate remains unknown.
- **Personality:** Bloodthirsty and notorious throughout Qinghai, but fearful and submissive before the Western Heaven Demon Lord.
- **Voice:** The brothers speak in near-unison with frightened, deferential phrasing.
- **Relationships:** They serve the Western Heaven Demon Lord and address him as their superior.

### Tang Sadok.md

# Tang Sadok (당사독)

- **Safe through:** Chapter 368
- **Aliases:** Myriad-Poison Asura
- **Role:** Current Family Head of the Sichuan Tang Clan, gravely wounded after being forced to watch the clan’s destruction but still alive and receiving treatment from Cheongpung.
- **Personality:** Grim, cold, blunt, suspicious, and unsentimental, with fierce concern for the Tang Clan’s affairs.
- **Voice:** Hissing, curt, authoritative, and threatening.
- **Relationships:** Tang Taesang was his father and predecessor as Family Head, his unnamed nephew serves as Master of the Gatekeeper Pavilion, and the Thousand-Year Poison Horned Snake was his father's final gift and is his cherished companion.

### Venerable Myoryeong.md

# Venerable Myoryeong (묘령)

- **Safe through:** Chapter 351
- **Aliases:** Myoryeong
- **Role:** Middle-aged Emei Sect nun who survived an attack that killed the Emei Sect Leader and three Elders, bears the Black Hand Seal, and is receiving treatment from Dong Feng with an expectation of full recovery.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** She came from the Emei Sect to assist Taekyung's search and, after surviving the attack, identified the killer as a one-armed middle-aged man.

## Korean source

```text
＃370화



사천당문은 예로부터 폐쇄적이기로 유명한 가문이었다.

어지간히 이름난 명사조차 쉽게 드나들 수 없고, 출가외인(出嫁外人)이 가문의 무공과 기밀을 누출할까 염려한 탓에 데릴사위를 들여 당씨 성을 잇게 했다.

이러한 방식으로 수백 년을 존속한 사천당문의 문이 활짝 열린 것은, 불과 칠 주야 전의 일이었다.

“거기, 기둥 똑바로 세워!”

“셋 세면 당긴다. 자. 하나, 둘-!”

단단한 체구의 인부들이 밧줄을 당기고, 돌과 목재를 실어나른다.

너른 부지 위, 검붉은 핏자국이 남아 있는 주춧돌 위로 건물이 서서히 형태를 갖춰 나갔다.

거기서 멀리 떨어진 어느 곳에서는 수십의 승려들이 모여 염불(念佛)을 외었다.

“원아진생무별염 아미타불독상수 심심상계옥호광…….”

파르라니 깎은 머리, 정기가 서린 눈빛을 한 승려의 정체는 아미파의 여승들이었다.

그들의 앞에는 수많은 목관이 불길에 휩싸여 타오르고 있었다.

“부디 극락왕생하시길. 그대들의 절개와 넋을 잊지 않겠습니다.”

몇 번의 낮과 밤이 바뀌었지만, 불길은 아직도 꺼지지 않았다.

삼문혈사(三門血史)에서 유명을 달리한 희생자들은 그만큼 많았고, 그중에서도 특히 사천당문이 입은 인명손실은 극심했다.

“후우…….”

“묘령사태, 피곤해 보이시는데 잠시라도 쉬시는 것이…….”

“아닙니다. 명진 도장. 해야 할 일을 하는 것뿐이니 괘념치 않으셔도 됩니다. 계속하시지요.”

파리한 안색의 중년 여승을 바라보던 도사가 무겁게 고개를 끄덕였다.

잠시 후 검을 찬 무림인들이 수십여 개의 목관을 들고 줄지어 걸어왔다.

그중에는 청성파의 도사도 있었고, 중소 문파의 제자들도 있었으며 땟국물이 줄줄 흐르는 거지도 있었다.

그런 그들의 뒤로 헐레벌떡 뛰어가는 것은 한 무리의 의원들이었다.

“갑자기 환자가 피를 토했다니. 안정된 것 아니었나?”

“그걸 알면 내가 지금 여기 있겠소? 심각한 내상을 입은 건 분명한데 도무지 무슨 증상인지…….”

“빨리 흩어져서 신의를 모셔와라!”

아미의 여승과 청성의 도사, 개방의 거지들과 크고 작은 문파에서 파견한 무인들. 거기에 더해 목수, 석공과 의원을 비롯한 양민들까지.

헤아릴 수 없이 많은 이가 사천당문의 경내를 누비며 각자의 역할을 충실히 하고 있었다.

높이 솟은 전각. 활짝 열린 창 너머로 이 광경을 지켜보던 젊은 거지, 궁기방은 피곤한 듯한 목소리로 중얼거렸다.

“살다 살다 이런 광경을 볼 줄은 몰랐군. 그것도 사천당문에서.”

그러자 침상에 누워 있던 혁무진이 대꾸했다.

“보지만 말고 가서 좀 도우십쇼. 후개라고 농땡이만 피우지 말고.”

“농땡이?”

눈을 부릅뜬 궁기방이 자신의 몸을 가리켰다.

새하얀 붕대로 칭칭 감긴 상반신. 한쪽 다리에는 임시로 부목을 댔다. 삼괴를 상대하면서 얻은 영광의 상처였다.

“지금 내 꼴을 보고도 그런 말이 나오나? 이게 농땡이야? 어?”

“궁 소협만 다쳤습니까?”

콧방귀를 뀐 혁무진이 보란 듯이 지렁이처럼 몸을 꿈틀거렸다.

궁기방과는 달리 전신이 붕대로 감겨 있는 그의 모습은 목내이(木乃伊)를 연상케 했다.

“이 정도는 다쳐야지 아, 이 녀석 고생 좀 했구나. 하는 겁니다. 아시겠어요?”

“……!”

궁기방은 몸을 부르르 떨었다. 분명히 크게 다치지 않은 건 자신의 무공이 더 높았다는 반증인데, 왠지 모르게 진 기분이다.

“난 붕대를 다섯 번이나 갈았다!”

“전 살아 있는 게 기적입니다. 그리고 그거야 몸이 하도 지저분하니까 그런 것 아닙니까. 참다못한 의원이 궁 소협 때 밀어 주다가 지쳐서 실신했다던데. 사실이에요?”

“…….”

“됐습니다. 더 말 섞어 봤자 입 냄새만 나지. 말이 나왔으니 말인데, 다음에는 이빨도 좀 닦아 달라고 하십쇼. 궁 소협이랑 대화할 때마다 저잣거리 똥개 엉덩이에 대고 말하는 기분이에요.”

실로 악랄한 혓바닥이 아닌가.

잠시 할 말을 잃었던 궁기방은 천장을 바라보며 한탄했다.

“삼괴가 저놈을 죽였어야 했는데.”

“어? 선 넘네?”

“도대체 너 같은 놈이 어떻게 그 격전에서 살아남은 건지, 아직도 모르겠다.”

“정 궁금하면 우리 조장님이랑 이 년만 붙어 다녀 보시든가.”

“……그건 사양하지.”

늘 티격태격하는 궁기방과 혁무진이 유일하게 일치하는 의견이 있다면, 그건 바로 진태경에 관한 문제였다.

세상의 온갖 평지풍파(平地風波)를 합쳐 놓은 듯한 존재. 그 어떤 위기 속에서도 용케 살아남는 끈질긴 생명력과 집념.

그리고 이제는 아득하게 느껴질 만큼의 무위를 갖춘 진태경을 보고 있노라면, 도무지 이게 같은 사람인가 싶을 정도였다.

‘그런 사람이 하나 더 있긴 하지.’

‘그래, 저놈.’

같은 생각을 떠올린 두 사람의 고개가 동시에 한 방향을 향해 움직였다.

“미미, 회오리치기!”

취리릭!

“잘했어, 미미! 이번에는 공중 날기!”

취릭?

“아, 이건 안 되는구나. 그럼 이번에는…….”

혁무진과 궁기방은 생각했다. 뱀에게 공중을 날라고 시키는 저 괴상한 청년이, 정말 검성의 후인이자 기련삼괴 중 가장 강하다는 일괴를 단신으로 쓰러트린 화산신룡이 맞는지.

“저기, 궁 소협.”

“왜.”

“원래 살짝 맛이 가야 초절정 고수가 될 수 있는 겁니까?”

“……몰라. 이제는 나도 정말 모르겠다.”

궁기방은 대답을 회피했다.

그의 스승도 제법 괴팍한 축에 드는 성격이지만, 진태경이나 청풍만큼은 아니었다.

검성과 화왕을 보면 제자들이 스승을 닮은 건지도 몰랐다.

“그런데 저 뱀은 도대체 뭐예요?”

“저렇게 큰 뿔이 달린 뱀은 이무기 빼면 하나뿐이야. 천년독각사.”

“어렸을 때 본 영물백과(靈物百科)에서는 온통 검은 빛을 띤 엄청난 독물이라던데.”

청풍이 외쳤다.

“미미. 엎드려!”

취릭!

“저걸 보면 독물이 아니라 그냥 동물 같은데.”

“제 말이요.”

“그런데 청 소협은 왜 여기 있는 거야? 별로 다치지도 않았더만.”

“아까 밖에서 큰 소리 나는 거 못 들었습니까? 그거 청 소협이 도와준답시고 나섰다가 전각 부순 거래요.”

“……아.”

동시에 할 말을 잃은 두 사람은 나란히 침상에 누워 천장을 바라봤다.

구 할에 달하는 건물이 파손되는 와중에도 용케 형태를 유지한 전각은, 중요한 환자들을 모아 둔 임시 의방(醫方)으로 쓰이는 중이었다.

어디선가 흘러들어 온 탕약 냄새를 맡던 혁무진이 문득 중얼거렸다.

“꿈 같네요.”

“그러게.”

삼문혈사가 일어난 그 날로부터 어언 칠 주야.

사천 무림이 결집하여 펼친 천라지망에 사천 곳곳을 피로 물들인 암천의 흑의인들은 대부분 죽거나 사로잡혔고 감쪽같이 사라졌던 삼괴마저 정체 모를 괴인에 의해 붙잡혔다. 그로써 짧은 전란은 막을 내렸다.

하지만…….

“이게 끝이 아닐 것 같은데. 궁 소협은 어떻게 생각합니까?”

“그걸 말이라고. 여기서 끝나면 내 손바닥에 장을 지지겠다.”

비단 두 사람뿐만이 아닌 모두가 느끼고 있는 위기였다.

고작 두 달 남짓한 시간 동안 하남과 사천이 피로 물들었다.

곧 삼문혈사에 관한 소식이 대륙 끄트머리까지 퍼진다면 천하인들은 깨닫게 될 것이다.

어느새 암천이라는 먹구름이 코앞까지 다가왔음을.

바야흐로 부정할 수 없는 난세(亂世)의 시작이었고, 영웅들은 그러한 난세 속에서 태어나는 법이었다.

혁무진의 시선이 자연스럽게 닫혀 있는 문 너머를 향했다.

“궁 소협이 생각하기에 조장님께서 언제쯤 깨어나실 것 같습니까?”

“글쎄, 나라고 방도가 있나. 우선 문경의 말에 의하면 아무 문제도 없다 하니 기다리는 수밖에.”

“말이 나왔으니 말인데, 문경이가 나이에 비해서 실력이 좋긴 하지만 조장을 맡기기에는 좀 그렇지 않습니까?”

“신의도 바쁘시니까 그런 거겠지. 적천강 대협께서도 기력을 회복 중이시고, 당사독 대협 같은 중환자들도 워낙 많다 보니까 어쩔 수 없다.”

“이해는 합니다. 이해는 하는데, 아무리 신의의 제자라고 하지만 문경이는 좀……. 그 어린 것이 알면 얼마나 알겠습니까?”

우려 섞인 혁무진의 말에 청풍이 번쩍 고개를 쳐들었다.

“어어, 하지 마세요. 죽어요.”

“청 소협?”

“방금 하셨던 말, 문 할. 아니 문경이 앞에서는 특히 하지 마세요.”

“예? 갑자기 그게 무슨…….”

“안 돼요. 정말 안 돼요.”

“……?”

혁무진과 궁기방이 어리둥절한 얼굴로 서로의 얼굴을 바라보는데 청풍이 갑자기 헙, 하고 숨을 삼켰다.

“미미야! 어디 갔어, 미미야!”

잠깐 눈을 뗀 사이 사라진 천년독각사를 청풍이 애타게 찾던 그 순간, 굳게 닫힌 문 너머에서 억눌린 외침이 터져 나왔다.

“컥! 야, 이 뱀 새끼야!”

세 사람의 시선이 허공에서 부딪쳤다.

동시에 한 사람을 부르는 여러 개의 이름이 전각 밖까지 쩌렁쩌렁 울려 퍼졌다.

“은인!”

“조장님!”

“진태경!”

그 외침에 밖에서 각자의 일을 하고 있던 사람들 사이에서도 일대 소란이 일어났다.

“방금 들었나?”

“혹시 깨어나신 건가?”

“이 소식을 장문인께 알려라! 어서!”



* * *



악몽을 꿨다.

한 치 앞도 보이지 않는 칠흑 같은 어둠 속, 한 마리의 뱀이 천천히 목을 조 여오는 꿈을.

숨이 막혔고, 눈앞이 새하얗게 물들었다.

그리고 다음 순간, 나는 참았던 숨을 토해 내며 눈을 떴다.

“커헉!”

취릭.

“……?”

취릭? 이거 뭐여, 시벌.

삼 초간의 사고 정지.

마침내 악몽의 정체를 깨달은 나는 목에 칭칭 감겨 있는 뱀의 뿔을 잡아챘다.

“야, 이 뱀 새끼야!”

천년독각산지 미미쨩인지, 이름이 뭐였건 상관없다. 오늘부터 이 새끼 이름은 뱀술이다.

“넌 오늘부터 이슬만 먹고 산다. 참이슬.”

붕붕 휘둘러 힘차게 바닥에 내리찍으려던 그때, 굳게 닫혀 있던 문이 박살 나며 한 사람이 뛰쳐 들어왔다.

“은인-!”

청풍의 쩌렁쩌렁한 외침에 골이 울린다.

녀석의 등 뒤로 지렁이처럼 꿈틀거리는 혁무진과 한 발로 콩콩 뛰어오는 궁기방이 보였다.

“조장님!”

“진태경!”

“……너희는 꼴이 왜 그 모양이냐.”

혁무진이 힘차게 몸을 튕기며 대답했다.

“삼괴. 그 미친 노괴가 절 이렇게 만들었습니다.”

궁기방이 친절하게 부연설명을 덧붙였다.

“살아남은 것이 천운이다. 혁무진 저 미친놈이 흙에 돌을 섞어서 삼괴에게 던졌거든. 때마침 칠선자가 나서서 막아 주지 않았다면 오체분시 됐을 거다.”

“……?”

아니, 삼괴는 또 누구고 칠선자는 누구야. 김선자는 나 고등학생 때 학생주임 이름인데…….

‘이런 미친놈들.’

지하 뇌옥에서 살아남았다는 안도감도 잠시, 나는 두통을 느끼며 이마를 감쌌다.

분명히 신의의 거처에 처박혀 있으랬는데, 그새를 못 참고 기어 나와 죽자고 싸운 모양이다.

목숨을 건졌기에 망정이지, 죽었으면 어쩔 뻔했나.

“너희들 죽고 싶어서 환장했냐? 또 무슨 사고를 친 거야?”

“……?”

“……?”

“뭐, 왜?”

이놈들 표정이 왜 이래?

청풍을 제외한 우리 세 사람은 어리둥절한 얼굴로 시선을 교환했다.

“무슨 문제 있냐?”

“당연히 있지.”

“조장님이 시키셨잖아요. 가서 아미파 구원하라고.”

첫 번째 대답은 궁기방이고, 그다음은 혁무진이었다.

둘다 헛소리라 나는 짐짓 눈살을 찌푸렸다.

“무슨 소리야. 내가?”

“예. 분명히 문경이한테 그렇게 들었는데. 혹시 머리 다치셨어요?”

그럴 리가.

눈을 뜨자마자 느낄 수 있었다. 전신에서 끓어오르는 강대한 기운.

눈 앞에 펼쳐진 시야와 나를 둘러싼 대자연의 기운이 또렷하고 생생하게 느껴졌다.

‘이것이 초절정…….’

당장이라도 이 힘을 시험해 보고 싶다. 지금쯤 산더미처럼 쌓여 있을 시스템 메시지도.

물론 그전에 이런 헛소리를 계속 듣는 대신 한 가지를 물어봐야 했다.

“다들 무사하냐?”

내가 말한 ‘다들’에 누가 포함되어 있는지는 녀석들도 알고 있을 것이다.

환하게 웃은 청풍이 대답 대신 커다란 창문을 활짝 열어젖혔다.

“은인께서 직접 확인하세요.”

나는 홀린 것처럼 천천히 창가를 향해 걸어갔다.

따스한 봄바람이 얼굴을 스쳤고, 이상할 만큼 조용한 공기가 창밖으로 고개를 내민 나를 반긴다.

“아.”

아래를 내려다본 나는 할 말을 잃었다.

그곳에 사람들이 있었다.

여승, 도사, 목수와 같은 장인으로 보이는 이도 있고 새하얀 의복을 걸친 의원도 있다. 헤아릴 수 없을 만큼 무수히 많은 시선에 담긴 감정은 하나였다.

‘경외.’

다음 순간, 그들은 약속이라도 한 것처럼 예를 취했다.

누군가는 포권을 취하고, 누군가는 작게 고개를 숙였으며, 누군가는 깊이 엎드려 절했다.

동시에 하나가 된 거대한 목소리가 흘러나왔다.

“열화신룡(烈火神龍)을 뵙습니다!”

한 줄기의 전율이 정수리부터 발끝까지 관통하며 훑어내린 그 순간.

띠링.



- 당신의 업적과 명성은 중원 전체에 울려 퍼질 것입니다.

- 새로운 별호를 획득했습니다!



귓가를 파고드는 시스템 알림과 함께, 나는 저 멀리 보이는 한 사람을 발견했다.

- 잘했다.

나는 적천강을 따라 웃었다.
```

## Final English reading copy

```markdown
# Chapter 370

The Sichuan Tang Clan had long been famous for its reclusive nature.

Even prominent figures could not easily come and go. And because the clan feared that a daughter who married out might leak its martial arts and secrets, they brought in a son-in-law to carry on the Tang surname.

The gates of the Sichuan Tang Clan, which had endured for hundreds of years in this manner, had been thrown wide open only seven days ago.

“Over there! Set that pillar straight!”

“Pull when I count to three. Ready. One, two—!”

Strongly built laborers pulled on ropes and carried stones and lumber.

Across the spacious grounds, buildings were slowly taking shape atop foundation stones still stained dark red with blood.

Far away, dozens of Buddhist nuns had gathered and were chanting prayers.

“May I have no other thought at the end of this life, with Amitabha alone beside me, my heart forever bound to the light from the white curl between his brows…”

The monks, their heads shaved close and their eyes filled with spiritual energy, were nuns of Emei Sect.

In front of them, countless wooden coffins burned within the flames.

“May you be reborn in the Pure Land. We will never forget your loyalty and your spirits.”

Several days and nights had passed, but the fires still had not gone out.

That was how many victims had died in the Three-Gate Bloodbath. The Sichuan Tang Clan, in particular, had suffered catastrophic losses.

“Whew…”

“Venerable Myoryeong, you look exhausted. You should rest, even if only for a little while…”

“No, Daoist Myeongjin. I am only doing what must be done, so please do not concern yourself. Let us continue.”

The Daoist gazed at the middle-aged nun’s pale complexion, then slowly nodded.

A short while later, martial artists with swords at their waists came walking in a line, carrying several dozen wooden coffins.

Among them were Daoists of Qingcheng Sect, disciples from small and mid-sized sects, and beggars with grime running down their bodies.

A group of physicians came running along behind them.

“The patient suddenly started vomiting blood? Weren’t they stable?”

“If I knew that, would I be here right now? The patient clearly suffered serious internal injuries, but I can’t make sense of these symptoms…”

“Spread out and bring the Divine Physician! Quickly!”

Emei nuns, Qingcheng Daoists, Beggars’ Sect beggars, and martial artists dispatched from sects both great and small. Along with them were ordinary people—carpenters, stonemasons, physicians, and more.

Countless people moved through the grounds of the Sichuan Tang Clan, each faithfully performing their own role.

From a tall pavilion, a young beggar watched the scene through an open window and muttered in a weary voice.

“I never thought I’d live to see something like this. And in the Sichuan Tang Clan, no less.”

Hyuk Mujin, lying on a bed, answered him.

“Stop watching and go help. Don’t slack off just because you’re the Successor Beggar.”

“Slack off?”

Gung Gibang opened his eyes wide and pointed at himself.

His upper body was tightly wrapped in spotless white bandages. One leg had been fitted with a temporary splint.

They were glorious wounds, earned while fighting the Third Fiend.

“Are you seriously saying that after looking at me? This is slacking off? Huh?”

“Are you the only one who got hurt?”

Hyuk Mujin snorted, then deliberately wriggled his body like an earthworm.

Unlike Gung Gibang, he was wrapped in bandages from head to toe, making him look like a mummy.

“You have to get hurt this badly before people say, ‘Ah, this kid must have had a rough time.’ You understand?”

“……!”

Gung Gibang shuddered.

The fact that he had not been seriously injured clearly proved that his martial arts were superior. Yet somehow, he felt as though he had lost.

“I changed my bandages five times!”

“I’m lucky to be alive. And that’s only because your body was so filthy. I heard a physician tried to scrub you clean, then passed out from exhaustion. Is that true?”

“……”

“Forget it. There’s no point talking to you anymore; all I get is bad breath. Since we’re on the subject, ask them to brush your teeth next time, too. Every time I talk to you, it feels like I’m speaking into the ass of a street mutt.”

What a vicious tongue.

Gung Gibang was speechless for a moment, then gazed up at the ceiling and lamented.

“The Third Fiend should have killed that bastard.”

“Hey. That’s crossing a line.”

“I still don’t understand how someone like you survived that battle.”

“If you’re really that curious, stick with our Captain for two years.”

“……I’ll pass.”

If there was one thing Gung Gibang and Hyuk Mujin, who were always bickering, agreed on, it was Jin Taekyung.

A man who seemed to embody every upheaval in the world.

A tenacious vitality and stubborn determination that somehow allowed him to survive any crisis.

And now, Jin Taekyung had reached such distant heights in martial prowess that they could hardly believe he was human like them.

*There is one more person like that.*

*Yeah. That guy.*

The two men thought the same thing, and their heads turned in unison toward one direction.

“Mimi, Whirlwind!”

Sssrrk!

“Good job, Mimi! This time, fly through the air!”

Sssrrk?

“Oh. You can’t do that. Then this time…”

Hyuk Mujin and Gung Gibang wondered whether the bizarre young man telling a snake to fly really was the Huashan Divine Dragon—the successor of the Sword Saint who had defeated First Fiend, the strongest of the Qilian Three Fiends, all by himself.

“Say, Young Hero Gung.”

“What?”

“Do you have to be a little unhinged to become a Supreme Peak master?”

“……I don’t know. I really don’t know anymore.”

Gung Gibang dodged the question.

His own master was rather eccentric, but not to the extent of Jin Taekyung or Cheongpung.

Then again, looking at the Sword Saint and the Fire King, perhaps disciples really did resemble their masters.

“But what exactly is that snake?”

“A snake with horns that big? Other than an imugi, there’s only one possibility. A Thousand-Year Poison Horned Snake.”

“When I was young, I read an encyclopedia of spirit creatures that described it as an extremely venomous creature that was black all over.”

Cheongpung shouted.

“Mimi! Lie down!”

Sssrrk!

“Looking at it now, it doesn’t seem poisonous. It just looks like an animal.”

“That’s what I’m saying.”

“But why is Young Hero Cheongpung here? He barely got hurt.”

“Didn’t you hear that loud crash outside earlier? They say Young Hero Cheongpung went out to help and ended up destroying a pavilion.”

“……Oh.”

The two men lost their words at the same time. They lay side by side on their beds and stared at the ceiling.

The pavilion had somehow retained its shape even after nine-tenths of the building was damaged. It was now being used as a temporary clinic for the most important patients.

Hyuk Mujin caught the scent of medicinal decoctions drifting in from somewhere and suddenly muttered,

“It feels like a dream.”

“Tell me about it.”

Seven days had passed since the Three-Gate Bloodbath.

The black-clad men of Dark Heaven who had stained every corner of Sichuan with blood had mostly been killed or captured by the net over heaven and earth formed by the united forces of Sichuan’s Murim. Even the Third Fiend, who had vanished without a trace, had been captured by a mysterious figure.

And with that, the brief war had come to an end.

But…

“I don’t think this is over. What do you think, Young Hero Gung?”

“Do you even have to ask? If this is really the end, I’ll brand my palm.”

It was a sense of crisis shared by everyone, not only the two of them.

In barely two months, Henan and Sichuan had been stained with blood.

Once news of the Three-Gate Bloodbath spread to the farthest reaches of the continent, the people of the world would realize it.

The dark cloud called Dark Heaven had already reached their doorstep.

It was the undeniable beginning of an age of turmoil, and heroes were born in such times.

Hyuk Mujin’s gaze naturally turned toward the closed door.

“When do you think our Captain will wake up?”

“Who knows? Do I look like I have an answer? According to Mungyeong, there’s nothing wrong with him, so all we can do is wait.”

“Since we’re talking about it, Mungyeong may be skilled for his age, but isn’t he a little young for us to entrust Captain to him?”

“The Divine Physician is busy, I suppose. Great Hero Jeok is still recovering his strength, and there are so many critical patients, including Great Hero Tang Sadok. There’s no helping it.”

“I understand. I do. But even if he is the Divine Physician’s Disciple, Mungyeong is a little… What could that child possibly know?”

At Hyuk Mujin’s worried words, Cheongpung abruptly lifted his head.

“Uh-oh. Don’t. You’ll die.”

“Young Hero Cheongpung?”

“What you just said—don’t say it in front of Grandpa Mun. I mean, especially not in front of Mungyeong.”

“What? Why are you suddenly saying that?”

“No. Really, don’t.”

“……?”

Hyuk Mujin and Gung Gibang exchanged bewildered looks.

Then Cheongpung suddenly sucked in a breath.

“Mimi! Where did you go, Mimi?”

At that moment, Cheongpung began desperately searching for the Thousand-Year Poison Horned Snake that had vanished during the brief moment he looked away.

From beyond the tightly closed door came a strangled shout.

“Ghk! You damn snake!”

The three men’s gazes collided in midair.

At the same time, several voices calling one person’s name rang out all the way outside the pavilion.

“Benefactor!”

“Captain!”

“Jin Taekyung!”

The people working outside caused an uproar as well.

“Did you hear that?”

“Could he have woken up?”

“Tell the Sect Leader! Quickly!”

* * *

I had a nightmare.

In an abyss of pitch-black darkness where I could not see an inch ahead, a snake slowly tightening around my neck.

I couldn’t breathe, and my vision turned white.

Then, in the next instant, I opened my eyes and exhaled the breath I had been holding.

“Ghk!”

Sssrrk.

“……?”

*Sssrrk? What the fuck?*

My brain stopped working for three seconds.

At last, I realized what my nightmare had been. I grabbed the horn of the snake tightly wrapped around my neck.

“You damn snake!”

Whether it was a Thousand-Year Poison Horned Snake or Mimi-chan, I didn’t care what its name had been. Starting today, this bastard’s name was Snake Liquor.

“You’re living on dew from now on. Chamisul.”[^1]

I was about to swing it around and slam it forcefully onto the floor when the tightly closed door exploded inward and someone came rushing through.

“Benefactor!”

Cheongpung’s thunderous shout made my skull ring.

Behind him, I saw Hyuk Mujin wriggling like an earthworm and Gung Gibang hopping along on one leg.

“Captain!”

“Jin Taekyung!”

“……Why do you two look like that?”

Hyuk Mujin bounced his body energetically and answered.

“The Third Fiend. That crazy old monster did this to me.”

Gung Gibang helpfully added an explanation.

“Surviving was a miracle. That lunatic Hyuk Mujin threw dirt mixed with stones at the Third Fiend. If the Seven Fairies hadn’t stepped in and blocked the attack, he would have been torn limb from limb.”

“……?”

Who the hell were the Three Fiends, and who were the Seven Fairies? Kim Seonja was the name of my high school student-affairs teacher…

*These lunatics.*

My relief at surviving the underground prison lasted only a moment before I pressed a hand to my forehead, feeling a headache coming on.

I had clearly told them to stay put at the Divine Physician’s residence, but they apparently could not resist crawling out and fighting to the death.

Thank goodness they had survived. What would have happened if they had died?

“Were you two desperate to die? What kind of trouble did you cause this time?”

“……?”

“……?”

“What? Why are you looking at me like that?”

The three of us, excluding Cheongpung, exchanged bewildered looks.

“Is there a problem?”

“Of course there is.”

“You told us to go save Emei Sect, Captain.”

The first answer came from Gung Gibang. The second came from Hyuk Mujin.

They were both talking nonsense, so I deliberately frowned.

“What are you talking about? I did?”

“Yes. That’s what Mungyeong told us. Did you hit your head?”

That couldn’t be it.

The moment I opened my eyes, I could feel it. Powerful qi surged throughout my entire body.

Everything before my eyes and the natural qi surrounding me felt clear and vivid.

*So this is Supreme Peak…*

I wanted to test this power immediately. And the System messages that must have piled up like a mountain by now.

But before I could keep listening to this nonsense, there was one thing I needed to ask.

“Is everyone all right?”

They knew who I meant by *everyone*.

Instead of answering, Cheongpung threw open the enormous window.

“You can see for yourself, Benefactor.”

As if in a trance, I slowly walked toward the window.

A warm spring breeze brushed across my face. An oddly quiet atmosphere greeted me as I leaned my head out beyond the window.

“Ah.”

I looked down and lost my words.

There were people below.

There were nuns, Daoists, and craftsmen who appeared to be carpenters. There were also physicians wearing spotless white robes. The emotion held in the countless gazes turned toward me was one thing.

*Awe.*

The next moment, they paid their respects as though they had made an agreement beforehand.

Some formed a fist-and-palm salute. Some bowed their heads slightly. Others prostrated themselves and bowed deeply.

A vast voice rose as one.

“We pay our respects to the Blazing Flame Divine Dragon!”

At that moment, a single shiver pierced down from the crown of my head to the tips of my toes.

Ding.

> **System**
>
> Your accomplishments and Fame will resound throughout the Central Plains.
>
> You have acquired a new sobriquet!

Along with the System alert that pierced my ears, I spotted someone in the distance.

“Well done.”

I smiled back at Jeok Cheongang.

[^1]: Chamisul is a Korean soju brand whose name literally means “true dew.”
```

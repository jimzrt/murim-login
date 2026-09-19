<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0449.txt",
      "sha256": "fcff63d1fed09e1655263ab139fe69bb9d50d2398611dd7578df5303d744581f",
      "bytes": 14290
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "3acee77f7030515b7a06e19f0aef833d67a851c284b999658e12dd84bf526b10",
      "bytes": 3562
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "0c458c86a6b931390e5a2443f0fd733099444706c713e793a228bad6b6af75bc",
      "bytes": 147114
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "acc322f5ac2b6e9732d0509f4c97841a0e077b86781ca2854758ff1df4794446",
      "bytes": 944
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "e437a126d2f3d933439b48c706757a45d41b54ad74883217ad849f9b3092fdb9",
      "bytes": 553
    },
    {
      "path": "characters/Dongting Fisherman.md",
      "sha256": "4d9d090a85ac5e693f41aad4e3c5bb8ee45bf3b3ec49e3f6dec56d6bb5fd6170",
      "bytes": 472
    },
    {
      "path": "characters/Gung Gibang.md",
      "sha256": "015ef7058ccf02f66c63a06acebb896843caf8086b259a205b8431153e6cc5e8",
      "bytes": 609
    },
    {
      "path": "characters/Hwang Chung.md",
      "sha256": "ccf184fa19566759c7c31a683f4b0c43368c7da14202c8d45ac38e11236a031b",
      "bytes": 609
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "bd0138519772a7a9dfba2360b813ca0652831000a972e7c3b2a427ccf5de446a",
      "bytes": 1108
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "91035a14c1936f9080df4568775427127539c08312c3e7c2c56590362093abd4",
      "bytes": 1470
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "610a2d34710e63ca19bf802547d6966efe3719869f146f1cdac339ad85eda6bc",
      "bytes": 1574
    },
    {
      "path": "characters/Jin Wikyung.md",
      "sha256": "fe858f29e2bab38ae1490d5de2dd86f39140ddbe486cfc84ccb3377d094806a8",
      "bytes": 1239
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "224931a7d147dbd8f487ca5e16fc0696bfd9cea97608445006ae229ce8720b2c",
      "bytes": 622
    },
    {
      "path": "characters/Mu Song.md",
      "sha256": "f98cfdbb547b58795e257d55400a8a615ceffee87790183830e561663f48ef92",
      "bytes": 870
    },
    {
      "path": "characters/Mungyeong.md",
      "sha256": "8d9b45d5159859f72ddf6fe2dbddb771c33d540bec773d09097bc82cf80029ef",
      "bytes": 686
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "f7a8ba21ab08ce9afe4a660a88181d789b840bea502245f25223d9100c670b5f",
      "bytes": 142278
    }
  ],
  "estimated_tokens": 14655
}
-->

# Durable State Update — Chapter 449

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 449. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 449. Profile updates may replace only one
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
  "chapter": 449,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 449,
    "continuity_sources": [449],
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
    "Taekyung accepted the Quest Another Chaos to uncover the truth behind the Hubei incidents and find the culprit.",
    "Jin Wikyung is acting as an inspector for the new Murim Alliance, and Taekyung is cooperating with his investigation.",
    "The shared symbols between the Arch Lich's magic circle and Dark Heaven's formations remain unexplained and may relate to black magic.",
    "The Sea Serpent Society was destroyed at Red Cliffs, the Dongting Fisherman disappeared after condemning the Yangtze River Channel League, and the League is implicated only by circumstantial evidence.",
    "Dangyang Stronghold and Honghu Stronghold vanished after taking control of Sea Serpent Society territory, while Donghu Stronghold remains inaccessible beyond Tianling Falls.",
    "Hwang Chung, the Yangtze One Saber, is the Seafaring King's sworn brother, a moderate-faction elder, and Lord of Donghu Stronghold; his involvement remains unproven.",
    "The Dongting Fisherman's broken Black Bamboo Fishing Rod was found, and Zhuge Feng ordered Mu Song to guide the group to Donghu Stronghold.",
    "Mungyeong remains with Taekyung's group while concealing his former Divine Physician and Slaughter Saint identity from most companions.",
    "The Skeleton King's undead identity remains concealed from the public, and Taekyung has ordered him to join Peace Guild under a prepared contract.",
    "Go Jun is expected to succeed Lee Jungryong as Ares Guild's captain and is searching China for Lee's holographic recorder.",
    "Taekyung's group survived the unusually violent Tianling Falls aboard four fast ships and reached Donghu Stronghold.",
    "Donghu Stronghold gave no reply to the Yangtze River Channel League's signal, and a corpse surfaced near its landing."
  ],
  "continuity_sources": [
    448,
    447
  ],
  "open_questions": [
    "What are the origin and purpose of the symbols shared by the Arch Lich's magic circle and Dark Heaven's formations, and are they connected to black magic?",
    "Why does Mungyeong continue accompanying Taekyung's group despite being unable to explain the impulse?",
    "What confidential matter is Jin Wikyung withholding?",
    "What are the terms of the Peace Guild–Wizard Guild agreement, and what evidence is contained in Lee Jungryong's holographic recorder?",
    "Who destroyed the Sea Serpent Society, caused the disappearances of the Yangtze River Channel League strongholds and Dongting Fisherman, and what happened inside Donghu Stronghold, whose signal went unanswered and where a corpse surfaced?"
  ],
  "safe_through": 448,
  "temporary_decisions": [
    "Render 황충 as Hwang Chung, 장강일도 as Yangtze One Saber, 천령폭 as Tianling Falls, and 흑죽조간 as Black Bamboo Fishing Rod.",
    "Render 시부럴 as “sibu-leol,” 시벌좌 as “Lord Fuck,” and 시부럴좌 as “Lord Sibu-leol.”",
    "Preserve the Skeleton King's grandiose, mock-offended voice and Taekyung's dry, profane humor.",
    "Render 최 팀장님 as “Team Leader Choi,” 진태경 씨 as “Mr. Jin Taekyung,” 막내야 as “my youngest,” 노야 as “Old Master,” and 노 선배님 as “Senior.”",
    "Keep Peace Guild, guild house, Inventory, Magic Johnson, established martial-arts terminology, black magic, poison human, World Hunter Association, Wizard Guild, Sea Serpent Society, Red Cliffs, and Dongting Fisherman unchanged; render 현공진인 as “Perfected Being Hyeongong” and 화왕질리언 as “Fire King Zilean.”"
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 진위경    | **Jin Wikyung**    |
| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 청풍     | **Cheongpung**     |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 해상왕    | **Seafaring King**            | Pa Ryun        |
| 소림     | **Shaolin**                      |
| 무당파    | **Wudang**                       |
| 암천     | **Dark Heaven**                  |
| 제갈세가   | **Zhuge Clan**                   |
| 장강수로맹  | **Yangtze River Channel League** |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 마교     | **Demonic Cult**                                 |                                                       |
| 가주     | **Family Head**                              |
| 제자     | **Disciple**                                 |
| 사천     | **Sichuan**            |
| 정마대전   | **Great Faction War**         |
| 노부      | **this old man / I**                                            |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 동정어옹 | **Dongting Fisherman** | Publicly condemned the Yangtze River Channel League and disappeared three days before this chapter. |
| 궁기방 | **Gung Gibang** | Beggars' Sect Successor Beggar and finalist. |
| 황충 | **Hwang Chung** | Lord of Donghu Stronghold, the Seafaring King's sworn brother, and the Yangtze One Saber. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 무송 | **Mu Song** | Lord of Water Dragon Stronghold and disciple of the Seafaring King. |
| 문경 | **Mungyeong** | Young medical apprentice and newly introduced passenger. |
| 화염신장 | **Flame Divine Palm** | Jopil's deadly palm technique, noted when Taekyung compares Jopil with Mukyung. |
| 송이 | **Song-i** | Short form used for Song Song; Taekyung's love interest. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 숙부 | **Uncle** | Lee Seowol's shortened address for Cheol Mubaek. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 오대세가 | **Five Great Families** | Major Murim grouping. |
| 천자 | **Son of Heaven** | Honorific title for the Emperor. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 노야 | **Old Master** | Taekyung's private address for Jeok Cheongang. |
| 호북 | **Hubei** | Province on Ju Gongsan's route from Guangdong to Henan. |
| 수룡채 | **Water Dragon Stronghold** | Major river stronghold belonging to the Yangtze River Channel League. |
| 선화아 | **Ship-Fire Boy** | Mu Song's sobriquet; literally a child who lights fires aboard a ship. |
| 채주 | **Stronghold Lord** | Title used for the lord of a water stronghold. |
| 장강 | **Yangtze** | The river controlled by the Yangtze River Channel League. |
| 의생 | **medical apprentice** | Mungyeong's occupation. |
| 오대 | **Five Squads** | Named Tang Clan organizational group in Tang Sadok's mobilization order. |
| 이동진 | **Moving Formation** | Dark Heaven's inactive long-distance transportation formation. |
| 동정채 | **Donghu Stronghold** | Stronghold where Mu Song's Uncle Hwang is based. |
| 해사방 | **Sea Serpent Society** | Hubei association formed by fishermen and boatmen; it was annihilated at Red Cliffs. |
| 장강일도 | **Yangtze One Saber** | Hwang Chung's sobriquet. |
| 천령폭 | **Tianling Falls** | Dangerous waterway leading to Donghu Stronghold. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진위경 | younger_to_eldest_brother | brother | familiar-but-respectful | Self-corrects from the personal name to kinship: “Jin Wikyung—I mean, my brother?”; 큰형 is eldest brother. |
| 진위경 | 진태경 | eldest_to_youngest_brother | youngest | affectionate-protective | Uses youngest-brother address; openly affectionate beneath a public mask. |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
| 혁무진 | 진위경 | Jin Family subordinate to Lesser Family Head | Lesser Family Head | deferential | Uses 소가주님 while confessing that he accepted Taekyung's invitation. |
| 진위경 | 혁무진 | Lesser Family Head to direct family subordinate | you | formal-but-familiar | Uses 자네 while recognizing Mujin and instructing him to keep helping Taekyung. |
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
| 무인 | 진위경 | vassal_martial_artist_to_lesser_family_head | Lesser Family Head | formal-deferential | The Mount Heng martial artists greet Jin Wikyung as 소가주님 while pledging loyalty. |
| 진위경 | 적천강 | host_to_legendary_guest | Great Hero Jeok | formal-deferential | Introduces himself and pays respects to Jeok Cheongang as the Fire King. |
| 적천강 | 진위경 | elder_to_younger_family_head | you | gruff and teasing | Uses 자네 while mistaking Wikyung for Taekyung’s father and questioning his age. |
| 궁기방 | 진태경 | rival_finalists | you bastard | insulting-casual | Gung Gibang answers Taekyung's collective insult with a profane threat. |
| 진태경 | 궁기방 | rival_finalists | you three idiots | insulting-casual | Taekyung addresses Gung Gibang as part of the trio and threatens them before a duel. |
| 진태경 | 무송 | junior_martial_artist_to_senior_martial_artist | Senior | formal-polite | Taekyung uses 선배님 after recognizing Mu Song as a senior martial artist and disciple of the Seafaring King. |
| 문경 | 무송 | survivor_to_savior_and_authority | Great Hero Mu Song | formal-deferential | Mungyeong credits Mu Song with saving him and asks him to spare Hwang Tae-gu. |
| 무송 | 문경 | stronghold_lord_to_young_passenger | you | gruff-but-considerate | Mu Song offers Mungyeong the right to decide Hwang Tae-gu's fate. |
| 진태경 | 문경 | young_martial_artist_to_medical_apprentice | Young Hero | formal-polite | Taekyung addresses the non-martial Mungyeong as 소협 while praising his actions. |
| 문경 | 진태경 | young_passenger_to_younger_martial_artist | Young Hero | deferential | Mungyeong uses 소협 while asking Taekyung for help boarding the ship. |
| 무송 | 진태경 | senior_martial_artist_to_junior_martial_artist | Junior | familiar-teasing | Mu Song calls Taekyung 후배 and jokes about his supposed taste for men. |
| 청풍 | 문경 | martial_companion_to_medical_apprentice | Medical Apprentice | cheerful-polite | Cheongpung addresses Mungyeong as 의생님 while asking him to greet the Tang Clan. |
| 혁무진 | 궁기방 | squad_companion_to_Beggars_Sect_successor | Young Hero Gung | formal-polite, then pointed | Uses 궁 소협 while asking about the culprit and challenging Gung’s insults. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 문경 | 적천강 | old_acquaintances | Fire King | familiar and grave | The figure bearing Mungyeong’s name greets Jeok Cheongang by his established epithet. |
| 궁기방 | 혁무진 | squad_companions | you; that lunatic | insulting-casual | Gung Gibang mocks Hyuk Mujin's injuries and calls him a lunatic for attacking the Third Fiend. |
| 궁기방 | 청풍 | martial_companions | Young Hero Cheongpung | formal-polite | Gung Gibang uses 청 소협 while asking why Cheongpung is at the temporary clinic. |
| 무송 | 적천강 | junior_martial_artist_to_legendary_martial_master | Great Hero Jeok | formal-deferential | Mu Song respectfully refers to Jeok Cheongang as 적 대협 while worrying that Jeok dislikes him. |
| 적천강 | 문경 | overwhelming elder to old acquaintance | you / little punk | mocking and threatening | Mocks Mungyeong's expression and threatens to poke out his eyes. |
| 적천강 | 무송 | legendary martial master to stronghold lord | you | gruff, coercive, and dismissive | Uses 자네 while ordering Mu Song to take the group only as far as Sichuan and leave the fast ship. |
| 청풍 | 무송 | young martial companion to stronghold lord | you | cheerful and familiar | Offers Mu Song his last dumpling and then induces him to buy more in Guang'an. |
| 궁기방 | 무송 | martial companion to Stronghold Lord | Senior Mu Song | pleading-deferential | Begins pleading for Mu Song to save them from Tianling Falls. |
| 진위경 | 무송 | Alliance inspector to Stronghold Lord | Stronghold Lord | formal and cautionary | Uses 채주 while warning Mu Song that the group did not come to spill blood. |

## Listed compact profiles

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 448
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, the grandson and Disciple of Sword Saint Mae Jonghak, and a Supreme Peak martial master known as the Huashan Divine Dragon.
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, a deep love of martial arts, and a martial artist's competitive pride; he becomes unsettled when someone copies his martial arts
- **Voice:** Dreamy and hazy, with innocent, polite phrasing
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions while Taekyung is his only true martial rival; Tang Sadok has temporarily entrusted Mimi to him.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 445
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Dongting Fisherman.md

# Dongting Fisherman (동정어옹)

- **Safe through:** Chapter 446
- **Aliases:** None
- **Role:** The Dongting Fisherman is a public critic of the Yangtze River Channel League who disappeared after condemning it.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** The Dongting Fisherman opposed the Yangtze River Channel League; his current whereabouts are unknown.

### Gung Gibang.md

# Gung Gibang (궁기방)

- **Safe through:** Chapter 448
- **Aliases:** Successor Beggar, Beggar Prince, pure-blooded beggar, ultimate beggar
- **Role:** Gung Gibang is the Beggars' Sect Successor Beggar and a unique eight-knot disciple.
- **Personality:** Vulgar, aggressive, and quick-tempered.
- **Voice:** Blunt, profane, and vividly threatening.
- **Relationships:** Rival finalist alongside Baek Woo and Zhuge Gyun; trades insults with Taekyung and is helping investigate Tang Taesang’s murder through Beggars’ Sect intelligence.

### Hwang Chung.md

# Hwang Chung (황충)

- **Safe through:** Chapter 448
- **Aliases:** Yangtze One Saber
- **Role:** Hwang Chung is the Lord of Donghu Stronghold, a moderate-faction elder of the Yangtze River Channel League, and the Seafaring King's sworn brother.
- **Personality:** Calm, clever, and supportive of the orthodox faction during the Great Faction War.
- **Voice:** Not established.
- **Relationships:** Hwang Chung helped the Seafaring King establish the Yangtze River Channel League and is regarded by Mu Song as an uncle and trusted senior.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 448
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers and Vice Squad Leader of the Jin Dragon Squad.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 448
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master, and Jin Taekyung's Master.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, and pathologically afraid of water. His meeting with Taekyung rekindled his will to live, making him determined to extend his life despite his illness.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 446
- **Aliases:** Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, a Supreme Peak master who has manifested Force, opened his Middle Dantian, crossed the wall into true mastery, can perceive the texture of qi well enough to sever layered magic, and is publicly recognized as an S-rank-level Hunter while formally retaining an A-rank license pending testing.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate, student, and trusted manager of media and official arrangements, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, and Xiao Shen regards him as an older brother after Jin saved him.

### Jin Wikyung.md

# Jin Wikyung (진위경)

- **Safe through:** Chapter 448
- **Aliases:** Junzi Sword
- **Role:** Jin Wikyung is the thirty-six-year-old Lesser Family Head and future Family Head of the Jin Family of Taiyuan, the Alliance Leader who unified Shanxi Murim and Shanxi Province's foremost landowner and magnate.
- **Personality:** Calm, authoritative, and politically capable in public; protective and affectionate toward Taekyung beneath a stern mask. Takes responsibility for his people, acts decisively under pressure, and prioritizes family survival.
- **Voice:** Restrained, formal, and commanding with subordinates; openly affectionate, proud, and occasionally exuberant with Taekyung.
- **Relationships:** Taekyung's eldest brother and future Family Head; Taekyung trusts him as a martial-arts mentor and family protector. Member and acting leader of the Jin Family of Taiyuan. Commands Wipeng and the family's forces. Has worked with Jeok Cheongang, who trained Taekyung under Wikyung's arrangement. Jin Mukyung is his younger brother and a potential successor alongside Taekyung.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 446
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Mu Song.md

# Mu Song (무송)

- **Safe through:** Chapter 448
- **Aliases:** Ship-Fire Boy
- **Role:** Lord of Water Dragon Stronghold, a Peak master and the Seafaring King's second martial Disciple who controls major Yangtze river traffic in Sichuan and belongs to the Yangtze River Channel League's moderate faction.
- **Personality:** Ambitious, domineering, impatient with interruptions, and capable of pragmatic cooperation when circumstances demand it.
- **Voice:** Deep and low in private, shifting to dry authority or boisterous command when addressing subordinates and rivals.
- **Relationships:** Mu Song is a member of the Yangtze River Channel League's moderate faction; Hwang Chung, his senior and Uncle Hwang, is the League elder and Donghu Stronghold Lord whom Mu Song firmly believes is innocent.

### Mungyeong.md

# Mungyeong (문경)

- **Safe through:** Chapter 448
- **Aliases:** None
- **Role:** Mungyeong is the legendary physician known as the former Divine Physician and Slaughter Saint, having passed the Divine Physician title to his Disciple.
- **Personality:** Compassionate, resolute, resourceful, and calm under extreme pressure.
- **Voice:** His Mungyeong persona is timid, deferential, and cheerful, while his Slaughter Saint voice is dry, impassive, and blunt.
- **Relationships:** Dong Feng is his Disciple, while Jeok Cheongang, Jin Taekyung, Cheongpung, and the two Sect Leaders know his Slaughter Saint identity.

## Korean source

```text
＃449화



기이할 정도로 강해진 천령폭의 물살을 넘어 동정채의 영역으로 진입했을 때부터, 선화아 무송의 가슴은 조금씩 빠르게 뛰고 있었다.

‘황 숙부. 소질이 왔습니다.’

동정채의 채주인 장강일도(長江一刀) 황충은 무송에게 스승과도 같은 존재였다. 아니, 어쩌면 그 이상일지도 모른다.

무송의 진짜 스승인 해상왕은 그리 살가운 성격이 아니었고 그들의 관계는 마른 모래처럼 퍽퍽했다.

어린 시절, 무송이 혹독한 질타와 수련을 버틸 수 있었던 것은 황충의 따뜻한 조언과 배려 덕분이었다.

‘소질은 믿고 있습니다. 숙부께서는 그러실 분이 아니라는 것을요.’

장강수로맹의 누구보다 진중하고 생각이 깊은 사람.

그런 황충이 해사방과 동정어옹을 이와 같은 방식으로 제거하는 최악의 악수(惡手)를 뒀을 리는 없다.

그에 대한 굳건한 믿음이 있었기에 무송 역시 직접 이 자리에 오기를 택했다.

그러나 이런 그의 믿음과는 별개로 불안감은 시시각각 크기를 부풀리고 있었다.

‘왜 이렇게 조용하지?’

그가 아는 장강일도 황충은 매사에 철두철미하고 신중한 사람이다. 천령폭(天靈瀑) 하나만을 믿고 수채의 방비를 소홀히 할 리 없었다.

동정채는 장강 위에 세워진 천혜의 요새.

만약 허락받지 않은 침입자들이 천령폭을 넘는다면, 그들은 곧 수백 장 길이의 협곡과 그 위에서 침입자들을 맞이하는 수많은 화살촉을 볼 수 있을 것이다.

하지만…….

‘이미 목전이거늘. 어찌하여 아무런 답도 없단 말인가.’

장강수로맹의 깃발을 높이 올리고, 북을 울려 신호를 보냈음에도 사방은 전처럼 고요했다.

짙은 안개에 휩싸인 섬을 바라보던 무송의 가슴이 거세게 두방망이질 쳤다.

‘무언가 잘못되었다.’

뇌리를 스치는 한줄기 생각. 그가 느낀 정체 모를 불안감은 얼마 지나지 않아 실체를 드러냈다.

“변고가 생긴 듯합니다.”

“그게 무슨……!”

어린 의생, 문경의 말에 고개를 돌린 무송은 말을 잇지 못하고 숨을 삼켰다.

곧이어 선상에 있던 사람들 사이로 동요가 들불처럼 번졌다.

“저, 저건…….”

“시체! 시체다!”

이 자리의 모두는 피와 죽음에 익숙한 무림인. 시체라면 질릴 정도로 봐 왔던 그들이지만 이번만큼은 상황이 달랐다.

이곳은 동정채다. 해사방의 핵심 인물들이 전멸하고 동정어옹마저 사망이 확실시되는 현재, 더욱 거칠어진 천령폭을 넘어 이곳까지 올 수 있는 자는 호북성에 전무하다고 볼 수 있었다.

그런데 난데없이 시체라니.

동요하는 사람들 사이, 침묵하고 있던 무송이 목소리를 쥐어 짜냈다.

“……당장 끌어올려라. 확인해 보아야겠다.”

“예, 옙!”

수룡채의 수적들이 곧장 움직이기도 전에, 한 사람이 앞으로 성큼 나섰다.

“물러나라.”

불과 촌각 전까지만 해도 길길이 날뛰던 화왕 적천강이 착 가라앉은 음성을 내뱉으며 손을 뻗었다.

공간을 격하고 쏘아진 고강한 공력이 물에 잠긴 시체를 끌어당겼다.

쉬익, 텅!

둔중한 소음과 함께 쾌조선의 갑판 위로 내려앉은 한 구의 시신.

상반신의 절반이 사라져 있고 얼굴이 부풀어 오른 시신을 확인한 무송이 눈을 부릅떴다.

“이, 이자는…….”

“아는 사람입니까?”

성큼 다가온 진태경의 물음에, 무송이 망연한 표정으로 고개를 끄덕였다.

“소조귀(小潮鬼) 왕필. 황 숙부의 오른팔이자 동정채의 부채주일세.”

호북성의 장강을 호령하는 동정채다. 그런 동정채의 부채주이자 장강일도 황충의 오른팔이니 이름과 별호가 알려진 것은 당연지사.

소조귀라는 별호에 터져 나오는 탄식을 뒤로한 진태경이 딱딱하게 굳은 얼굴로 무송을 응시했다.

“부채주? 확실합니까?”

“틀림없네. 비록 시신이 심각하게 훼손되었으나 얼굴을 못 알아볼 정도는 아니야.”

“……제기랄.”

진태경의 얼굴이 딱딱하게 굳었다. 비단 그 혼자만이 아니라 상황을 인지한 모두가 마찬가지였다.

평범한 수적이어도 불길하기 짝이 없는 일인데, 하물며 동정채의 부채주이자 호북 무림에 이름이 자자한 장강수로맹의 초절정 고수라니.

이와 같은 일련의 상황이 의미하는 것은 명백했다.

‘동정채에 변고가 생겼다.’

모두의 뇌리를 순간적으로 스친 생각을 가장 먼저 행동으로 옮긴 것은 진태경이었다.

쉬익!

눈부신 속도로 선상을 가로질러 쾌조선의 후미에 도착한 그는 온 힘을 다해 양팔을 뻗었다.

퍼엉! 퍼어어엉!

화염신장(火焰神掌)에 실린 열양지기가 수분을 증발시키고 쾌조선을 앞으로 밀어 낸다.

그제야 충격을 벗어난 이들이 진태경을 따라 움직였다.

“수부(水夫)들은 어서 제자리로 돌아가 노를 잡아라! 한시가 급한 상황이다!”

“다른 배에도 이 사실을 알려야 한다! 어서 신호를 보내라!”

둥, 둥, 두웅!

다급한 외침과 북소리가 고요를 깨트렸다.

어지러운 혼란 속에서, 무송은 사방에 울려 퍼지는 북소리보다 더욱 크고 거칠게 뛰는 자신의 가슴을 느끼며 고개를 들었다.

그리고 다음 순간.

“……!”

그는, 아니 모두는 볼 수 있었다.

쾌조선의 뱃머리를 따라 서서히 흩어지는 안개 너머, 산산이 부서진 나루터와 강물을 가득 메운 수많은 시신을.



* * *



“이런 씨팔……!”

나도 모르게 큰 목소리로 튀어나온 욕설. 하지만 아무도 내게 눈치를 주거나 탓하지 않았다.

그럴 경황이 없거나, 어쩌면 그들이 하고 싶은 말을 내가 대신해 주었기 때문일지도 모른다.

그만큼 눈 앞에 펼쳐진 광경은 참혹했다.

“지옥도가 따로 없군.”

“……어떻게 이럴 수가.”

적천강은 심유하게 가라앉은 목소리로 중얼거렸고, 늘 밝던 청풍은 떨리는 눈동자로 주위를 바라보았다.

녀석의 시선이 향하는 곳마다 무너진 가옥과 시신들이 즐비했다.

나루터 주위에서 목격한 시신들은 섬에 내려앉은 무수한 죽음 중 일부에 불과했다.

“조, 조장님. 저기…….”

“알고 있어.”

떨리는 목소리로 나를 부르는 혁무진을 애써 외면했다.

녀석이 가리키는 방향에 무엇이 있는지, 이미 보았기 때문이다. 나도 모르게 이가 악물어졌다.

‘어린아이들과 무공을 익히지 않은 양민들.’

섬에는 동정채의 수적들만이 있는 것이 아니었다.

그들은 각자의 일가 피붙이를 이 안전한 천혜의 요새에 데려왔고, 그렇게 모인 사람들은 하나의 마을을 이루게 되었다.

그리고…….

‘모두 죽었어.’

이제 막 젖이나 뗐을 법한 어린아이, 병약한 노인과 아녀자들. 목숨을 걸고 그들을 지켜야 할 수백의 수적들까지.

단 한 사람의 예외도 없이 죽음을 맞이했다.

나와 일행들은 물론이고 무당파와 제갈세가의 무인들, 무송이 이끄는 수룡채의 수적들이 한나절이 넘는 시간 동안 섬을 샅샅이 뒤진 끝에 나온 결과다.

그리고 그 무수한 죽음 속에는 한 사람의 이름 역시 포함되어 있었다.

“황 숙부!”

짐승과도 같은 무송의 포효가 저 멀리서 울려 퍼지자, 궁기방이 착잡한 목소리로 중얼거렸다.

“기어코 찾은 모양이군.”

누군가는 말한다. 사람의 목숨에는 경중(輕重)이 없다고.

하지만 분명 경중은 나뉘어 있다. 망자가 생전 어떤 사람이었고, 나와 어떤 관계였느냐에 따라 무게는 달라진다.

적어도 무송에게 있어 장강일도 황충은 그런 사람이었을 것이다.

“가주께서 급히 모셔오라 하셨습니다.”

다급하게 달려온 제갈세가 무인의 말에 진위경이 고개를 끄덕였다.

“황 대협에 관련된 일이겠군.”

“예. 지금 막 황 대협의 시신이 발견되었습니다. 한데…….”

“가세. 나머지는 제갈 가주께 직접 듣도록 하지.”

우리는 가타부타 말없이 걸음을 옮겼다.

그의 죽음을 추모하기 위해서가 아니라, 망자가 된 장강일도 황충이 그만큼 중요한 인물이기 때문이다.

일행 중 유일하게 안면이 있는 적천강의 얼굴이 굳어 있는 이유 역시 슬픔 때문이 아니었다.

- 네 녀석은 어찌 생각하느냐?

문득 귓가를 파고드는 한 줄기 전음에, 나는 발걸음을 늦추며 대답했다.

- 노야와 같은 생각입니다.

- 노부가 어떤 생각인 줄 알고?

- 저와 같은 생각이요.

- 화염신장이 마렵구나.

- 저도 아까부터 오줌 마려운데 참고 있습니다. 노야도 참으세요. 지금 할 말 정리 중이니까.

나는 지난 한나절 동안 고민했던 생각들을 차분하게 풀어냈다.

- 동정채는 오직 천령폭을 넘어야만 올 수 있는 천혜의 요새. 제가 이곳 상황을 자세히는 몰라도, 장강일도 황충이라는 초절정 고수와 휘하의 수적들을 쓰러트리려면 어지간한 전력으로는 꿈도 못 꾸겠죠.

- 똥개도 제 앞마당에서는 한 수 먹고 들어가는 법인데, 장강에서 잔뼈가 굵은 놈들을 상대하려면 압도적인 힘이 필요하다.

적천강의 전음이 이어졌다.

- 특히 장강일도는 정마대전 당시 마교를 상대로 모든 수전(水戰)에서 대승을 거둔 물귀신 같은 놈이니, 동정채를 몰살시키기 위해서는 족히 두 배 이상의 전력이 필요했을 게다.

동정채의 두 배라…….

나도 이곳에 오고서야 안 사실이지만, 동정채의 규모는 여타의 수채들과는 비교를 불허한다.

당장 지금껏 발견된 시신의 숫자만 일천이 넘어가니, 그 규모만으로는 일파(一派)라 불러도 부족함이 없을 정도다.

‘무송도 그런 말을 한 적이 있었지. 동정채는 장강수로맹의 총단 다음으로 강성한 수채라고.’

당장 주위만 둘러봐도 알 수 있는 사실이었다.

비록 지금은 모든 것이 산산이 부서지고 파괴되었지만, 일개 수채가 오십여 척에 달하는 선박으로 함대를 구성하고 도시의 번화가에서나 볼 법한 가옥으로 거주지를 만들었다.

구파일방이나 오대세가와 같은 명문대파에 비견될 수준은 아니더라도, 장강일도가 거느린 휘하 수적들 역시 상당한 정예였을 것이다.

그리고 이런 동정채를 상대로 두 배의 전력을 투입할 수 있는 집단은 결코 많지 않다. 아니, 손에 꼽는다.

- 그만한 전력과 선박을 동원할 수 있는 곳이라면…….

- 노부가 알기로는 호북성에서 단 네 곳뿐이다. 그중 하나는 이미 없어진 것이나 다름없고.

- 무당파, 제갈세가, 관부. 그리고 해사방. 맞습니까?

- 그렇다. 하지만 해사방은 생업을 위해 모인 이들이 대부분이라 고수의 숫자가 턱없이 부족하고, 무당파와 제갈세가는 힘이 있으나 동정채를 칠 만한 이유나 명분이 없지.

- 관부도 마찬가지겠군요.

- 물론이다. 무림과 관이 상호 불가침의 관계라는 것은 삼척동자도 아는 사실. 만에 하나 천자가 황명(皇命)을 내려 토벌코자 했다 하더라도 이처럼 천하의 이목을 속이고 은밀하게 처리하지는 못했을 것이다.

무림은 천하라는 숲속 깊숙이 뿌리내린 나무다.

가지를 치기에는 이미 너무 높이 자랐고, 섣불리 찍어 넘어트리기에는 도리어 도끼날이 상할까 염려된다.

이는 지금껏 숲의 주인이 여러 번 바뀌었음에도 무림이 존속할 수 있던 이유기도 했다.

천자라는 나무꾼조차 쉽사리 도끼를 들이댈 수 없는 거목(巨木).

그것이 무림이고, 이 거목에 솟아난 수많은 가지와 잎사귀는 힘을 합치거나 때로 서로를 꺾으며 자라 왔다.

장강수로맹은 그중에서도 제법 굵은 나뭇가지다.

천하 각지에 흩어진 수채를 한자리에 모은다면 일군(一群)이라 부르기에 손색이 없고, 고수의 숫자 역시 구파일방이나 오대세가에 비해 크게 뒤지지 않는다.

그런데 바로 그 장강수로맹의 가지가 꺾였다. 정체를 알 수 없는 누군가에 의해서.

- 노야께서는 흉수가 무당, 제갈, 관부, 해사방. 이 네 곳 중 하나라고 생각하십니까?

- 하루에도 수백 척이 넘는 선박이 오가는 물길이다. 수많은 이목을 피해 그만한 전력을 동원하여 천령폭을 넘는다는 건…… 매우 힘든 일이지.

- 매우 쉬운 일일 수도 있죠.

나는 아까부터 혀끝에서 맴돌던 한 마디를 툭 뱉었다.

- 암천(暗天)이라면.

- ……!

- 놈들은 굳이 수백, 수천의 병력을 선박에 싣고 천령폭을 넘을 필요가 없습니다. 워프, 아니 이동진이라고 불리는 그 진법이 이곳 어딘가에 숨겨져 있다면 그걸로 모든 것이 해결되니까요.

암천은 이미 소림과 사천에서 그것을 증명했다.

만약 내 짐작이 사실이라면, 장강을 오가는 수많은 이목이 눈치채지 못한 것도 충분히 설명이 된다.

한동안 말이 없던 적천강이 작게 침음을 흘렸다.

- 노부만 그리 생각하는 것이 아니었구나.

- 이런 일에서 암천을 배제하기에는…… 냄새가 너무 구립니다.

- 하지만, 왜 하필 장강수로맹이란 말이냐?

- 글쎄요.

나는 저 멀리, 서서히 가까워지는 익숙한 얼굴들을 바라보며 말을 이었다.

- 그건, 지금부터 알아봐야죠.
```

## Final English reading copy

```markdown
# Chapter 449

From the moment they crossed the unnaturally powerful current of Tianling Falls and entered the territory of Donghu Stronghold, Ship-Fire Boy Mu Song’s heart had been beating faster and faster.

*Uncle Hwang. I’ve come.*

Hwang Chung, the Yangtze One Saber and Lord of Donghu Stronghold, was like a master to Mu Song. No—perhaps he was even more than that.

Mu Song’s true Master, the Seafaring King, was not a warm man, and their relationship was as dry and barren as sand.

When Mu Song was young, it was Hwang Chung’s warm advice and consideration that allowed him to endure the harsh scolding and training.

*I believe in you, Uncle. You’re not the kind of man who would do such a thing.*

Hwang Chung was the most serious and thoughtful person in the Yangtze River Channel League.

There was no way a man like him would have made the worst possible move by eliminating the Sea Serpent Society and the Dongting Fisherman in such a manner.

Because of his unshakable faith in Hwang Chung, Mu Song had chosen to come here in person.

But regardless of that faith, his unease continued to grow with every passing moment.

*Why is it so quiet?*

The Hwang Chung he knew, the Yangtze One Saber, was thorough and cautious in everything he did. He would never neglect the stronghold’s defenses just because he trusted in Tianling Falls.

Donghu Stronghold was a natural fortress built on the Yangtze.

If unauthorized intruders crossed Tianling Falls, they would soon see a gorge several hundred zhang long, along with countless arrowheads waiting to greet them from above.

But…

*We’re already right in front of it. Why hasn’t there been any reply?*

Even after they raised the Yangtze River Channel League’s flag high and beat the drums to send a signal, the surroundings remained as quiet as before.

Mu Song’s heart pounded violently as he stared at the island shrouded in thick fog.

*Something has gone wrong.*

That single thought flashed through his mind. Before long, the vague unease he had felt revealed its true form.

“It seems something has happened.”

“What do you mean…!”

At the words of the young medical apprentice Mungyeong, Mu Song turned his head—then could not finish his sentence. He swallowed hard.

A moment later, unrest spread like wildfire among the people aboard the ships.

“Th-that’s…”

“A corpse! It’s a corpse!”

Everyone present was a martial artist accustomed to blood and death. They had seen enough corpses to grow sick of them, but this time was different.

This was Donghu Stronghold. At a time when the Sea Serpent Society’s key figures had been wiped out and the Dongting Fisherman was all but confirmed dead, there should have been no one in Hubei Province capable of crossing the even more violent Tianling Falls to reach this place.

And yet a corpse had appeared out of nowhere.

Amid the agitation, Mu Song, who had remained silent, forced his voice out.

“...Pull it aboard at once. We need to identify it.”

“Y-yes, sir!”

Before the river bandits of Water Dragon Stronghold could move, someone strode forward.

“Stand back.”

Fire King Jeok Cheongang had been raging only moments ago. Now, he spoke in a low, settled voice as he stretched out one hand.

Powerful internal energy shot across the distance and seized the corpse submerged in the water.

Whoosh—bang!

With a heavy thud, the body landed on the deck of the fast ship.

Half of its upper body was gone, and its face was bloated. Mu Song’s eyes widened when he saw it.

“This man…”

“Do you know him?”

Jin Taekyung strode over to him, and Mu Song nodded dazedly at the question.

“Little Tide Demon Wang Pil. Uncle Hwang’s right-hand man and the Deputy Stronghold Lord of Donghu Stronghold.”

Donghu Stronghold ruled the Yangtze in Hubei Province. Naturally, the name and sobriquet of its Deputy Stronghold Lord—and the right-hand man of the Yangtze One Saber Hwang Chung—were widely known.

Ignoring the sighs that escaped at the name Little Tide Demon, Jin Taekyung stared at Mu Song with a stiff expression.

“Deputy Stronghold Lord? Are you certain?”

“Without a doubt. The corpse is badly damaged, but not so badly that I can’t recognize his face.”

“...Damn it.”

Jin Taekyung’s face hardened. It was the same for everyone who understood what this meant.

Even if it had been an ordinary river bandit, the event would have been ominous. But this was the Deputy Stronghold Lord of Donghu Stronghold—and a Supreme Peak master of the Yangtze River Channel League, whose name was renowned throughout Hubei Murim.

The meaning of this chain of events was obvious.

*Something has happened at Donghu Stronghold.*

Jin Taekyung was the first to turn the thought that had flashed through everyone’s minds into action.

Whoosh!

He crossed the deck at blinding speed and reached the stern of the fast ship, then thrust both arms forward with all his strength.

Boom! Booooom!

The Scorching Yang Qi carried by the Flame Divine Palm evaporated the river water and propelled the fast ship forward.

Only then did the others recover from their shock and begin moving after him.

“Boatmen, get back to your positions and take hold of the oars! Every second counts!”

“Tell the other ships! Send them a signal at once!”

Boom, boom, boooom!

Urgent shouts and drumbeats shattered the silence.

Amid the confusion, Mu Song raised his head, feeling his own heart pounding louder and more violently than the drums echoing around him.

And then—

“...!”

He saw it.

No—all of them saw it.

Beyond the fog slowly dispersing along the bow of the fast ship were a shattered ferry landing and countless corpses filling the river.

* * *

“What the fucking hell…!”

The curse burst from my mouth at full volume before I could stop it. But no one gave me a disapproving look or blamed me.

Maybe they were too distracted to care. Or maybe I had simply said what they all wanted to say.

That was how horrific the scene before us was.

“This is nothing short of hell.”

“...How could this happen?”

Jeok Cheongang muttered in a deeply subdued voice, while Cheongpung, who was usually so cheerful, looked around with trembling eyes.

Everywhere he looked, there were collapsed houses and corpses.

The bodies we had seen around the ferry landing were only a fraction of the countless deaths that had descended upon the island.

“C-Captain. Over there…”

“I know.”

I forced myself to ignore Hyuk Mujin, who was calling to me in a trembling voice.

I already knew what was in the direction he was pointing. My teeth clenched before I even realized it.

*Children and commoners who never learned martial arts.*

Donghu Stronghold was not inhabited solely by river bandits.

The stronghold’s people had brought their families and blood relatives to this safe, natural fortress, and the people gathered there had formed a village of their own.

And…

*They’re all dead.*

Children who had only just been weaned. Frail old people and women. Even the hundreds of river bandits who should have risked their lives to protect them.

Every single one of them had died.

That was the result after my companions and I, along with the martial artists of Wudang and the Zhuge Clan and the river bandits of Water Dragon Stronghold under Mu Song, had searched every corner of the island for more than half a day.

And among those countless dead was one particular person.

“Uncle Hwang!”

Mu Song’s beastlike roar echoed from far away. Gung Gibang muttered in a heavy voice.

“Looks like he finally found him.”

Some people said that no human life was more valuable than another.

But that was not true. There was certainly a difference in weight. The weight of a person’s death changed depending on who they had been in life and what relationship they had shared with you.

For Mu Song, at least, the Yangtze One Saber Hwang Chung must have been such a person.

“The Family Head ordered me to escort you to him at once.”

At the words of the Zhuge Clan martial artist who came running up to us, Jin Wikyung nodded.

“This concerns Great Hero Hwang, I presume.”

“Yes. Great Hero Hwang’s corpse was just found. However…”

“Let’s go. We’ll hear the rest directly from the Family Head.”

Without another word, we began walking.

Not to mourn his death, but because the dead Yangtze One Saber Hwang Chung was important enough to warrant it.

The reason Jeok Cheongang, the only person among us who had known him, wore such a hard expression was not grief, either.

—What do you think?

At the Sound Transmission that suddenly slipped into my ear, I slowed my steps and answered.

—The same as you, Old Master.

—You know what this old man is thinking?

—The same thing I am.

—I’m getting an urge to use the Flame Divine Palm.

—I’ve needed to piss since earlier, too, but I’ve been holding it in. You should hold it in as well, Old Master. I’m organizing what I want to say.

I calmly laid out the thoughts I had been considering over the past half day.

—Donghu Stronghold is a natural fortress that can only be reached by crossing Tianling Falls. I don’t know the details of the situation here, but defeating the Supreme Peak master Hwang Chung and the river bandits under him would be impossible for any ordinary force.

—Even a mongrel gets the upper hand on its own doorstep. To face men who have spent their entire lives on the Yangtze, you would need overwhelming strength.

Jeok Cheongang’s Sound Transmission continued.

—The Yangtze One Saber in particular is like a ghost of the water. During the Great Faction War, he achieved overwhelming victories against the Demonic Cult in every naval battle. To wipe out Donghu Stronghold, the attacker would have needed at least twice its forces.

Twice the forces of Donghu Stronghold…

I had only realized it after coming here, but Donghu Stronghold was on a scale utterly incomparable to the other water strongholds.

The number of corpses discovered so far had already surpassed a thousand. In terms of size alone, it would not have been an exaggeration to call it a faction.

*Mu Song said something like that before, too. Donghu Stronghold is the second most powerful water stronghold in the Yangtze River Channel League, after its headquarters.*

I only had to look around to understand.

Everything had been shattered and destroyed, but this one water stronghold had once assembled a fleet of more than fifty ships and built a settlement of homes that would not have looked out of place in a bustling city.

It might not have reached the level of a prestigious great faction such as the Nine Sects and One Gang or the Five Great Families, but the river bandits under the command of the Yangtze One Saber had undoubtedly been highly elite as well.

And there were very few groups capable of deploying twice that force against Donghu Stronghold.

No—only a handful.

—If there is a place capable of mobilizing that many men and ships…

—As far as this old man knows, there are only four such places in Hubei Province. One of them is already practically gone.

—Wudang, the Zhuge Clan, the government, and the Sea Serpent Society. Correct?

—Correct. But most of the Sea Serpent Society are fishermen and boatmen who gathered for their livelihood, so they have far too few masters. Wudang and the Zhuge Clan possess the strength, but neither has any reason or justification to attack Donghu Stronghold.

—The government is the same.

—Of course. Even a child knows that Murim and the authorities maintain a relationship of mutual noninterference. Even if the Son of Heaven had issued an imperial edict to subjugate the stronghold, they could not have carried it out secretly in a way that deceived the eyes of the entire world.

Murim was a tree rooted deep within the forest that was the world.

It had grown too tall to prune its branches, and anyone who tried to chop it down carelessly would risk damaging the blade of their own ax.

That was one of the reasons Murim had survived even though the master of the forest had changed many times.

A massive tree that even the Son of Heaven, the woodcutter, could not easily raise his ax against.

That was Murim. The countless branches and leaves that had grown from that great tree had flourished by joining forces—and, at times, by breaking one another.

The Yangtze River Channel League was one of the thicker branches.

If the water strongholds scattered throughout the world were gathered in one place, they would be more than worthy of being called a great faction, and their number of masters was not far behind that of the Nine Sects and One Gang or the Five Great Families.

And now that very branch of the Yangtze River Channel League had been broken.

By someone whose identity was unknown.

—Do you think the culprit is one of those four places: Wudang, the Zhuge Clan, the authorities, or the Sea Serpent Society?

—This is a waterway crossed by hundreds of ships every day. Avoiding all those eyes while mobilizing enough force to cross Tianling Falls would be… extremely difficult.

—It might have been extremely easy.

I finally let out the words that had been circling the tip of my tongue.

—If it was Dark Heaven.

—...!

—They had no need to load hundreds or thousands of soldiers onto ships and cross Tianling Falls. If a warp—no, if the formation they call a Moving Formation were hidden somewhere around here, that would explain everything.

Dark Heaven had already proved it in Shaolin and Sichuan.

If my guess was correct, it would also fully explain how they had gone unnoticed by the countless eyes traveling along the Yangtze.

Jeok Cheongang remained silent for a while before letting out a low groan.

—So this old man is not the only one who thinks so.

—In a situation like this, excluding Dark Heaven… the smell is far too damn foul.

—But why the Yangtze River Channel League?

—I don’t know.

I continued speaking as I looked toward the familiar faces slowly approaching from the distance.

—We’ll have to find that out now.
```

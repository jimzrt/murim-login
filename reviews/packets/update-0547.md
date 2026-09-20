<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0547.txt",
      "sha256": "e349423e7296d0ea8fbf058523f2a0eb6ff24bce4e0f70fe6213a20702173e51",
      "bytes": 15282
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "83dedefac347fcf7eaf659a52fd38b730bf7fb3801f718f2e432224cfc14e2af",
      "bytes": 4476
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "fb02223d0849c4a4274033dfcb37dd0b666a24e95e84955f5d4494b10d58c755",
      "bytes": 173659
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "c8ea569f3f501baa0fa0f92d7584f2d8c5eecf80696e778f7b2bf08d0eff16a6",
      "bytes": 1371
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "fd7e213efa1cabc5a32b3bffe1cc296178fa01e18991c2b7de13203205d3d22f",
      "bytes": 553
    },
    {
      "path": "characters/Hwangbo Ak.md",
      "sha256": "4c27aac87227819b9bc13e0c8e75cc593afe4ae67f3e162484cf23588a9fdc8b",
      "bytes": 846
    },
    {
      "path": "characters/Hwangbo Gun.md",
      "sha256": "3865c57e5317538d11f58e311a240d4b3b37b3a5542ea82d5e89feb95fc20a8d",
      "bytes": 716
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "8ae1d13ea811bbe47deae30c8b92b7ba450a571f281aa3bff3612f2160781297",
      "bytes": 1702
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "bc8ac26794919f497076710e15974e8bb7a63e72f68483d113e1e408996dce82",
      "bytes": 2252
    },
    {
      "path": "characters/Jin Wikyung.md",
      "sha256": "424acf5530842ef2d42759ca7c6b220a970435c8694feccee632095188238b92",
      "bytes": 1210
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "c386956ea9d9e9abd909d67e05b083d7fcfd39616e65e22dd7f1e9d1aca3f539",
      "bytes": 622
    },
    {
      "path": "characters/Mae Jonghak.md",
      "sha256": "e6db4b7c5d3f23d38e731c0d370d2b11f6a26e161cb75a1d80ea0f77ab1036a5",
      "bytes": 985
    },
    {
      "path": "characters/Peng Cheolhu.md",
      "sha256": "c4f9133ae6612101b200278563c2f3e712f94535dd0c32bb5c615018e36cd4f5",
      "bytes": 680
    },
    {
      "path": "characters/Song Ho.md",
      "sha256": "8dce6e9dcd92876d71d8e1b9eab87f7d5203b485edcd5361fd58d59b392c2225",
      "bytes": 767
    },
    {
      "path": "characters/Yan Hwapyeong.md",
      "sha256": "da2323e11d2847deb9b3ca7c0ba8c166e9892e1bb33560cae750bbbf6879dfe8",
      "bytes": 661
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "e190d1f4dfdecc6495d6974499268ad909f972ce7efdd79c30e42b78daed2e44",
      "bytes": 164631
    }
  ],
  "estimated_tokens": 16073
}
-->

# Durable State Update — Chapter 547

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 547. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 547. Profile updates may replace only one
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
  "chapter": 547,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 547,
    "continuity_sources": [547],
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
    "The Mount Song Resolution formally restored the Murim Alliance; Mae Jonghak is its Alliance Leader, Jeok Cheongang heads the Five Kings Hall, and Murong Yeonghwi is an Outer Hall Squad Leader remaining in Liaoning to oversee Murong Family defenses.",
    "The Two Dragons Pavilion remains the overall organization but is divided into Jin Taekyung's Fire Dragon Pavilion and Cheongpung's Azure Dragon Pavilion; both pavilion masters have largely honorary authority.",
    "Jin Taekyung holds the unique Title Fire Dragon Pavilion Master; his total Fame has surpassed 10,000, some Title effects have strengthened, Charm and Intimidation have greatly increased, and he has leveled up.",
    "The Five Kings Hall contains five of the Ten Kings, with Jeok Cheongang occupying its chief seat despite resenting the appointment.",
    "Tang Sadok and the Sichuan Tang Clan publicly support Jin Taekyung and Cheongpung, while Taekyung expects the resentful Zhongnan Sect to obstruct them.",
    "Cheongpung created Mimi Step, is recognized by Mungyeong as having Grandmaster potential, cares for Mimi, and is now master of the Azure Dragon Pavilion.",
    "Mungyeong ended Taekyung's direct training, assigned him a final task of incorporating martial principles into his learned martial arts, and accepted Cheongpung's offer to accompany him.",
    "Zhuge Feng's Demon-Sealing Formation still blocks all mana from the exposed Gate, while Jang Taebo is summoning artisans to process the Water God Dragon's remains.",
    "The Southern Heaven Demon Empress is traveling toward Yunnan and expects to cause further deaths.",
    "The Black Dragon Demon Gate remains a major unorthodox power; Sama Pyo is its Young Sect Leader and Black Dragon Saber, and Taishan is his giant subordinate.",
    "Jin Taekyung remains a Supreme Peak master with Three Flowers Gather at the Crown, advanced qi perception, exceptional resistance to monster Fear, and public S-rank-level recognition despite retaining an A-rank license; he intends to advance toward the coming war while protecting his family, companions, subordinates, and Master.",
    "Jang Sam, a Hubei fisherman missing for a month, reappeared as a mutant Killing Ghost with a horn and four arms; the mechanism behind his transformation and his ability to absorb human energy remain unresolved."
  ],
  "continuity_sources": [
    546,
    545
  ],
  "open_questions": [
    "What is the Lord of Heaven's identity, how is he connected to the dangerous force Taekyung associates with his original world, and how can Dark Heaven open Gates?",
    "Where is the Southern Heaven Demon Empress ultimately headed, and what does she intend to do in Yunnan?",
    "What is the outcome of the duel between Jeok Cheongang and Nangong Cheon, the Azure Sky Sword King?",
    "Why did Ju Hwaran and Sama Pyo's political engagement end?",
    "What process created Jang Sam's mutant form, and can Dark Heaven's mutants absorb human energy?"
  ],
  "safe_through": 546,
  "temporary_decisions": [
    "Render 고월루 as Gowolru, 곤륜운룡 as Kunlun Cloud Dragon, 학우 as Hak Woo, 이룡각 as Two Dragons Pavilion before its renaming, 화룡각 as Fire Dragon Pavilion, 청룡각 as Azure Dragon Pavilion, 협 as chivalry, 인의 as humanity, 협객 as knight-errant, 홍학루 as Honghakru, 홍매 as Hongmae, and 호거아 as Tiger Giant Child; render 전 정혼자 contextually as former fiancé or former fiancée.",
    "Render 탈진 as the capitalized System status Exhaustion; retain Ten Dragons and Phoenixes, Blazing Flame Divine Dragon, Dark Heaven, Murim Alliance, and Old Master.",
    "Render 황보세가 as Hwangbo Family, 소가주 as Lesser Family Head, 은비화 as Dagger Hidden Flower, and 전음 as Sound Transmission.",
    "Preserve the chapter's blunt profanity, financial-therapy humor, monster-comparison humor, and Mae Jonghak's carefree 'That can happen' refrain; render 고잉무림호 as Going Murim ship, 대종사 as Grandmaster, 왕희지 as Wang Xizhi, and 영창 피아노 as Young Chang piano.",
    "Render 청룡각주 as Azure Dragon Pavilion Master, 오왕전주 as Five Kings Hall Master, 문 할아버지 as Grandpa Mun, 정기 as vital essence, 변이체 as mutant, 시취 as corpse stench, and 십단(九團) as Ten Squads—Nine Squads in the characters; retain Taishan's clipped, childlike, literal speech and Taekyung's closing 'we're fucked.'"
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 진위경    | **Jin Wikyung**    |
| 적천강    | **Jeok Cheongang** |
| 매종학    | **Mae Jonghak**    |
| 청풍     | **Cheongpung**     |
| 팽철후    | **Peng Cheolhu**   |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 검성     | **Sword Saint**               | Mae Jonghak    |
| 벽력도왕   | **Thunderbolt Saber King**    | Peng Cheolhu   |
| 권왕     | **Fist King**                 | Yan Hwapyeong  |
| 종남파    | **Zhongnan Sect**                |
| 무림맹    | **Murim Alliance**               |
| 암천     | **Dark Heaven**                  |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 마교     | **Demonic Cult**                                 |                                                       |
| 강호     | **martial world**                                | Prefer “Murim” where the setting itself is meant      |
| 가주     | **Family Head**                              |
| 장문인    | **Sect Leader**                              |
| 선배     | **Senior**                                   |
| 은인     | **Benefactor**                               |
| 명성               | **Fame**                       |
| 산서     | **Shanxi**             |
| 하남     | **Henan**              |
| 사천     | **Sichuan**            |
| 정마대전   | **Great Faction War**         |
| 노부      | **this old man / I**                                            |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 소협      | **Young Hero**                                                  |
| 대사      | **Master** for a senior Buddhist monk                           |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 황보악 | **Hwangbo Ak** | Lesser Family Head of the Hwangbo Family and member of the Ten Dragons and Phoenixes. |
| 황보군 | **Hwangbo Gun** | Family Head of the Hwangbo Family and father of its Lesser Family Head. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 송호 | **Song Ho** | Elderly martial artist known as the Thousand-Faced Fox. |
| 언화평 | **Yan Hwapyeong** | Personal name of the Fist King and last descendant of the Jinzhou Yan Family. |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 전서구 | **messenger pigeon** | Pigeon delivering the Lower District Sect's Jeongyang Branch report. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 오대세가 | **Five Great Families** | Major Murim grouping. |
| 풍운검군 | **Wind-and-Cloud Sword Lord** | Epithet of Gong Iljung, the Zhongnan Sect's Sect Leader. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 아미타불 | **Amitabha** | Buddhist invocation spoken by the unidentified arriving group. |
| 신성 | **Morning Star** | Term in the summons referring to the Master of Morning Star. |
| 천면호리 | **Thousand-Faced Fox** | Epithet of Song Ho. |
| 은영각 | **Hidden Shadow Pavilion** | Former Murim Alliance intelligence organization. |
| 반로환동 | **Returned to Youth** | Possible explanation for an apparently young Supreme Peak master. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 마공 | **demonic martial arts** | Martial arts that appear to defy common principles. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 아미 | **Emei** | Short form for Emei Sect. |
| 호북 | **Hubei** | Province on Ju Gongsan's route from Guangdong to Henan. |
| 황보 | **Hwangbo** | Surname form used when addressing Hwangbo Eom. |
| 외당 | **Outer Hall** | The Tang Clan's outer hall area. |
| 내당 | **Inner Hall** | The Tang Clan's inner hall area. |
| 장일 | **Jang Il** | Twenty-five-year-old two-knot Beggars' Sect Disciple killed near Emei. |
| 오대 | **Five Squads** | Named Tang Clan organizational group in Tang Sadok's mobilization order. |
| 열화신룡 | **Blazing Flame Divine Dragon** | New sobriquet bestowed on Jin Taekyung. |
| 이무기 | **imugi** | Legendary serpent mentioned as the only comparable creature to a Thousand-Year Poison Horned Snake. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 암기 | **hidden weapon** | Term used in Mungyeong's promise not to throw one. |
| 식경 | **half an hour** | Time limit given for the requested reports. |
| 맹주전 | **Alliance Leader's Hall** | Hall directly associated with the Murim Alliance Leader. |
| 황보세가 | **Hwangbo Family** | Hwangbo Ak's established martial family and the long-standing hegemon of Shandong. |
| 산동권룡 | **Shandong Fist Dragon** | Hwangbo Ak's sobriquet among the Ten Dragons and Phoenixes. |
| 화룡각 | **Fire Dragon Pavilion** | New name chosen for Taekyung's pavilion. |
| 오왕전 | **Five Kings Hall** | Organization containing five of the Ten Kings. |
| 화룡각주 | **Fire Dragon Pavilion Master** | Unique Title awarded to Jin Taekyung. |
| 오왕전주 | **Five Kings Hall Master** | Mae Jonghak's teasing title for Jeok Cheongang. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진위경 | younger_to_eldest_brother | brother | familiar-but-respectful | Self-corrects from the personal name to kinship: “Jin Wikyung—I mean, my brother?”; 큰형 is eldest brother. |
| 진위경 | 진태경 | eldest_to_youngest_brother | youngest | affectionate-protective | Uses youngest-brother address; openly affectionate beneath a public mask. |
| 청풍 | 진태경 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung repeatedly addresses Taekyung as 은인 after receiving food. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 진태경 | 청풍 | companion_to_young_martial_artist | Young Master Cheongpung | formal-polite | Taekyung uses 청 공자 while correcting Cheongpung's royal-etiquette mistake. |
| 매종학 | 청풍 | grandfather_to_grandson | Pung | affectionate-instructional | Mae Jonghak calls young Cheongpung 풍아 while teaching him the Crouching Tiger Fist. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 적천강 | 청풍 | overwhelming_elder_to_young_martial_artist | you / little punk | blunt, amused, and threatening | Jeok Cheongang uses 네, 이놈, and related blunt forms while testing Cheongpung. |
| 청풍 | 적천강 | young_martial_artist_to_overwhelming_elder | Grandpa Jeok | casual-familiar despite deference | Cheongpung uses 적 할아버지 while asking Jeok Cheongang to confirm Taekyung's condition; this is a familial form of address, not literal kinship. |
| 무인 | 진위경 | vassal_martial_artist_to_lesser_family_head | Lesser Family Head | formal-deferential | The Mount Heng martial artists greet Jin Wikyung as 소가주님 while pledging loyalty. |
| 진위경 | 적천강 | host_to_legendary_guest | Great Hero Jeok | formal-deferential | Introduces himself and pays respects to Jeok Cheongang as the Fire King. |
| 적천강 | 진위경 | elder_to_younger_family_head | you | gruff and teasing | Uses 자네 while mistaking Wikyung for Taekyung’s father and questioning his age. |
| 송호 | 청년 | elderly_martial_artist_to_younger_martial_artist | Young Hero | formal-polite | Song Ho calls out to the young man as 소협 at the chapter's end. |
| 적천강 | 벽력도왕 | rival_martial_master_to_rival_martial_master | Virility Saber King | insulting and taunting | Jeok coins 정력도왕 as a taunting replacement for the established title. |
| 벽력도왕 | 적천강 | rival_martial_master_to_rival_martial_master | Jeok Cheongang | boisterous and hostile-teasing | The Thunderbolt Saber King calls Jeok by name before their argument escalates. |
| 송호 | 진태경 | senior_martial_artist_to_junior_martial_artist | you | familiar-polite | Uses 자네 while recognizing Taekyung and discussing his preliminary performance. |
| 매종학 | 송호 | savior_to_survivor | you | casual-familiar | Mae uses 자네 while speaking to Song Ho after his identity is recognized. |
| 송호 | 매종학 | rescued_survivor_to_savior | Great Hero; you | formal-deferential and familiar | Song Ho credits Mae with saving his life and addresses him as 대협. |
| 매종학 | 진태경 | older_ally_to_younger_friend | friend | casual-familiar | Mae Jonghak uses 친구 when arriving at Taekyung's window and asking to talk. |
| 진태경 | 선배님들 | junior_to_senior_team_members | Seniors | polite-but-threatening | Taekyung addresses the Myeongdong Guild Team 1 Hunters while ordering them to clear a path. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 중년인 | 진태경 | veteran civilian Hunter to celebrated allied Hunter | Mr. Jin | formal-polite and awed | The casualty clerk addresses Jin as 진 선생님 after Jin asks him to list Lei Fei among the dead. |
| 진태경 | 중년인 | celebrated Hunter to older fellow Hunter | sir | casual and teasing | Jin addresses the older Hunter as 아저씨 while joking with him and giving him instructions. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 매종학 | 적천강 | long-standing martial rival and friend | Great Hero Jeok | casual and familiar | Mae addresses Jeok as 적 대협 while discussing the Alliance Leader position. |
| 적천강 | 매종학 | long-standing martial rival and friend | you | blunt and familiar | Jeok addresses Mae as 당신 while recalling their meeting at Mount Jiuhua. |
| 벽력도왕 | 진태경 | elder martial master to younger rival | you | boisterous and confrontational | Peng addresses Taekyung as 네놈 while discussing Peng Dojin. |
| 천면호리 | 매종학 | intelligence_chief_to_alliance_leader | Alliance Leader | formal and deferential | Requests that Mae move elsewhere with the others before he reports further. |
| 벽력도왕 | 매종학 | Ten Kings peer to Ten Kings peer | Sword Saint | familiar and blunt | Asks Mae what was discussed in the sealed meeting. |
| 매종학 | 벽력도왕 | Ten Kings peer to Ten Kings peer | Peng | casual and admonitory | Calls him 팽가야 and tells him to remain quiet. |
| 황보악 | 진태경 | fellow_Ten_Dragons_and_Phoenixes_member | you; damned bastard | angry-insulting | Hwangbo reacts to Taekyung's barefoot-running joke with 이 빌어먹을 놈. |
| 진태경 | 황보악 | stronger_master_to_Hwangbo_Lesser_Family_Head | Hwangbo Ak | casual and taunting | Taekyung calls Hwangbo by name while ordering him to reconcile and warning him to leave. |
| 진위경 | 청풍 | Jin Family Lesser Family Head to young martial companion | Young Hero Cheongpung | formal-polite | Uses 청 소협 while summoning Cheongpung to the Alliance Leader's Hall. |
| 청풍 | 매종학 | grandson to grandfather | Grandpa | casual-familiar | Repeatedly calls Mae Jonghak 할아버지 while mistaking the Alliance Leader's summons as a family visit. |
| 진태경 | 매종학 | younger ally to newly installed Alliance Leader | Alliance Leader | formal and deferential | Uses 맹주님 while formally greeting Mae Jonghak as the Alliance Leader. |
| 황보군 | 매종학 | old_battlefield_comrade_to_current_alliance_leader | Great Hero Mae; Alliance Leader | formal-deferential | Hwangbo Gun begins with Great Hero Mae, then switches to the formal Alliance Leader. |
| 매종학 | 황보군 | old_battlefield_comrade_to_family_head | you | casual-familiar | Mae uses 자네 while addressing Hwangbo Gun. |

## Listed compact profiles

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 546
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, the grandson and Disciple of Sword Saint Mae Jonghak, a Supreme Peak martial master known as the Huashan Divine Dragon, the creator of the snake-inspired Mimi Step footwork technique, and the master of the Azure Dragon Pavilion within the Alliance Leader's Two Dragons Pavilion.
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, a deep love of martial arts, competitive pride, unusual resistance to monster-induced Fear, and discomfort when someone copies his martial arts.
- **Voice:** Dreamy and hazy, with innocent, polite phrasing; he has begun imitating Taekyung's profanity.
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions while Taekyung is his only true martial rival; Tang Sadok has temporarily entrusted Mimi, now a large horned snake, to him, Mungyeong recently examined her condition, and Mungyeong accepted Cheongpung's offer to accompany him after Cheongpung pledged to learn by observation rather than formal instruction.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 546
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Hwangbo Ak.md

# Hwangbo Ak (황보악)

- **Safe through:** Chapter 540
- **Aliases:** Shandong Fist Dragon
- **Role:** Hwangbo Ak is the Lesser Family Head of the Hwangbo Family, a member of the Ten Dragons and Phoenixes, and a young martial prodigy.
- **Personality:** Proud, self-obsessed, status-conscious, and easily humiliated.
- **Voice:** Polite and ceremonious in public but sharp, dismissive, and indignant when challenged.
- **Relationships:** Baek Woo is his longtime friend and fellow Ten Dragons and Phoenixes member; he is infatuated with Ju Hwaran, resents her apparent preference for Jin Taekyung, carries a lasting grudge against Jin Mukyung after their Heaven's Gate Temple encounter, and now regards Taekyung with anger and fear after being publicly humiliated and warned.

### Hwangbo Gun.md

# Hwangbo Gun (황보군)

- **Safe through:** Chapter 540
- **Aliases:** None
- **Role:** Family Head of the Hwangbo Family and father of its late-born only son, the Lesser Family Head.
- **Personality:** Status-conscious, politically resentful, and fiercely protective of his only son; willing to exaggerate grievances to secure favorable treatment.
- **Voice:** Formally deferential toward superiors but aggrieved and forceful when defending his family's standing.
- **Relationships:** Old battlefield comrade of Mae Jonghak; father of the Hwangbo Family's Lesser Family Head; politically opposed to Jin Taekyung and the Black Dragon Demon Gate.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 546
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm, and the occupant of the chief seat of the Murim Alliance's Five Kings Hall.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 545
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, a Supreme Peak master who possesses the Heavenly Martial Physique and superhuman physical strength, has manifested Force, opened his Middle Dantian, crossed the wall into true mastery, has achieved Three Flowers Gather at the Crown but not Five Qi Returning to Origin, can perceive the texture of qi well enough to sever layered magic, can resist high-level monster Fear through exceptional mental strength, is publicly recognized as an S-rank-level Hunter while formally retaining an A-rank license pending testing, can command coordinated raids against powerful monsters, and now serves as one of the two pavilion masters of the Alliance Leader's direct Fire Dragon Pavilion while holding its unique Title, Fire Dragon Pavilion Master.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor and assigned him a final task to incorporate martial principles into his learned martial arts but declined Taekyung's recruitment after Cheongpung reached him first, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate, student, and trusted manager of media and official arrangements, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, and Xiao Shen regards him as an older brother after Jin saved him.

### Jin Wikyung.md

# Jin Wikyung (진위경)

- **Safe through:** Chapter 546
- **Aliases:** Junzi Sword
- **Role:** Jin Wikyung is the thirty-six-year-old Lesser Family Head and future Family Head of the Jin Family of Taiyuan, the Alliance Leader who unified Shanxi Murim and Shanxi Province's foremost landowner and magnate.
- **Personality:** Calm, authoritative, and politically capable in public; protective and affectionate toward Taekyung beneath a stern mask. Takes responsibility for his people, acts decisively under pressure, and prioritizes family survival.
- **Voice:** Restrained, formal, and commanding with subordinates; openly affectionate, proud, and occasionally exuberant with Taekyung.
- **Relationships:** Jin Wikyung is Taekyung's eldest brother and future Family Head who protects and mentors him, commands Wipeng and the Jin Family's forces, has worked with Jeok Cheongang, and maintains a political connection with Hongcheon, Prince Shangshan's hidden loyal retainer; Jin Mukyung is his younger brother and a potential successor alongside Taekyung.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 545
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Mae Jonghak.md

# Mae Jonghak (매종학)

- **Safe through:** Chapter 546
- **Aliases:** Sword Saint
- **Role:** Sword Saint and Cheongpung's grandfather who now serves as the New Murim Alliance's Alliance Leader.
- **Personality:** Playful, easygoing, and teasing, but capable of handling heavy administrative responsibilities efficiently.
- **Voice:** Friendly, casually familiar, and cheerfully teasing, including when greeting old acquaintances and discussing leadership.
- **Relationships:** Cheongpung's grandfather and martial instructor; taught him the Taeeul Miri Palm; secretly entered Huashan while its Sect Leader slept, left a dagger and handwritten note, and then went into hiding, prompting Huashan's search; fought Jeok Cheongang at Mount Jiuhua more than forty years ago and left after their draw; his old friend Hong Dao left him a letter identifying Jin Taekyung as the Morning Star who would drive away darkness.

### Peng Cheolhu.md

# Peng Cheolhu (벽력도왕)

- **Safe through:** Chapter 545
- **Aliases:** Thunderbolt Saber King
- **Role:** Peng Cheolhu is the Thunderbolt Saber King, a Ten Kings master and Great Hero of the Hebei Peng Family.
- **Personality:** Boisterous, hot-tempered, argumentative, and protective toward those connected to his close friend Hong Dao.
- **Voice:** Loud, blunt, confrontational, and prone to disguising embarrassment or retreat as serious martial instruction.
- **Relationships:** Long-standing rival and friend of Jeok Cheongang; close friend of Hong Dao; protective toward Hong Dao's Disciple Unnamed.

### Song Ho.md

# Song Ho (송호)

- **Safe through:** Chapter 537
- **Aliases:** Thousand-Faced Fox
- **Role:** Elderly Peak master known as the Thousand-Faced Fox, a martial artist with a prosthetic leg, and current Chief of the Hidden Shadow Pavilion, overseeing a vetted intelligence network that includes highly trained assassins.
- **Personality:** Outwardly genial and relaxed, but observant, forceful, and intimidating when pursuing information.
- **Voice:** Lightly genial and conversational, turning quietly coercive during interrogation.
- **Relationships:** He serves under Mae Jonghak's New Murim Alliance, commands the Hidden Shadow Pavilion, and recognizes Jin Taekyung as Jeok Cheongang's Disciple.

### Yan Hwapyeong.md

# Yan Hwapyeong (언화평)

- **Safe through:** Chapter 545
- **Aliases:** Fist King
- **Role:** Yan Hwapyeong is the Fist King and last descendant of the Jinzhou Yan Family who joined the Murim Alliance when a hundred thousand demonic soldiers invaded the Central Plains.
- **Personality:** Selfless, resolute, and warm-hearted, he helps others without regard for old grievances.
- **Voice:** Blunt and self-effacing in the remembered account of his words.
- **Relationships:** He is the last descendant of the Jinzhou Yan Family and currently sits among the Murim Alliance's senior masters.

## Korean source

```text
＃547화



대회의실에 싸늘한 침묵이 내려앉았다.

사실 말을 꺼내기 전에도 충분히 예상했던 반응이다.

그리고 이 자리에 있는 수십여 명의 사람들 중, 누가 가장 먼저 나를 향해 날 선 말을 내뱉을지도.

“그걸, 지금 말이라고 하나?”

어떻게 예상을 벗어나는 법이 없냐.

나는 기다렸다는 듯이 입을 연 반백의 중년인을 보며 내심 혀를 찼다.

저 사람의 이름과 신분은 이미 들어서 알고 있다. 지난번 회동 때부터 하도 째려보길래 뭐 하는 인간인가, 했더니 역시나 간접적인 인연이 있었거든.

‘씨는 못 속인다더니.’

확실히 부자지간이라 그런지 닮긴 닮았다. 날카롭게 솟구친 눈매도, 사람을 깔보는 오만한 눈빛과 말투도.

“내 말이 안 들리는 모양이군.”

반백의 중년인. 산동권룡(山東拳龍) 황보악의 아버지이자 황보세가의 가주인 황보군의 물음에, 나는 천천히 눈을 깜빡였다.

“당연히 들리죠. 설마 안 들리겠습니까?”

“그런데 왜 대답이 없지?”

“질문이 웃기잖아요. 제 입으로 한 말이니까 당연히 말이라고 생각해서 한 거지. 제가 뭐 짐승처럼 울음소리라도 냈어요?”

옆자리에 앉은 청풍이 귀를 쫑긋 세웠다.

“은인, 그런 소리도 낼 수 있어요?”

“청 소협은 입 다물고 있어. 배 속에 있는 만두 토해 내기 싫으면.”

“고마워요…….”

이를 지켜보는 황보군의 표정이 와락 구겨졌다.

“이 자리가 어떤 자리인 줄 모르느냐!”

“그거 모르고 온 사람 있습니까.”

“한데 명성이 자자하신 노선배님들 앞에서, 그런 뻔한 말을 상스럽게 내뱉다니!”

“그래서 말 안 하려고 했잖습니까. 그리고 이건 노선배님들 입장도 들어 봐야죠. 어떻게 생각하십니까?”

갑작스러운 내 물음에 매종학이 고개를 끄덕였다.

“그건 진 각주 말이 맞지. 나는 별 상관없네. 말이 험하긴 해도 현실을 직시해야지.”

“매, 맹주님!”

당황함이 가득 묻어 나오는 황보군의 외침을, 나는 잽싸게 가로챘다.

“예. 바로 그 무림 맹주님의 고견, 잘 들었습니다. 내친김에 우리 오왕전주님께서는?”

적천강이 벌레 보는 듯한 눈빛으로 황보군을 바라봤다.

“뭘 묻고 자빠졌느냐. 좆 된 거 맞지. 저놈의 헛소리는 신경 쓸 것 없으니 계속해라.”

“화끈한 대답 감사합니다.”

고개를 돌려 황보군을 응시한 내가 어깨를 으쓱해 보였다.

“그렇다는데요, 바로 그 노선배님들께서.”

“……!”

이 자리에 노선배라고 칭할 만한 사람들은 차고 넘치지만, 적천강과 매종학에 비견할 수 있는 자는 아무도 없다.

구파일방과 오대세가의 주인들이 분대장을 맡은 실세 상병에 말년 병장이라면, 무림 맹주인 매종학은 대대장이요 적천강은 주임 원사인 것이다.

‘짬에서 밀리면 입 다물어야지.’

짬도 짬인데. 심지어 계급장 떼고 덤벼도 화왕표 불 주먹 한 방이면 훅 간다.

이것이 나와 청풍을 곱게 보지 않는 이들, 그중에서도 대표 주자라 할 수 있는 종남파 장문인 풍운검군조차 입을 꾹 다물고 있는 이유였다.

그리고 그건 황보군이 외톨이 신세가 되었다는 뜻이나 다름없었다.

‘누울 자리를 보고 다리를 뻗지. 그러게 왜 혼자 나서서 저래.’

황보군도 정마대전 때는 방귀깨나 뀌었다고 들었는데. 원래도 정치 감각이 떨어졌던 건지, 아니면 삼대독자 외아들에 관련된 일로 폭주 기관차가 된 건지 모르겠다.

나는 안타까움을 담은 구슬픈 멜로디를 흥얼거렸다.

“나는 개똥벌레. 친구가 없네.”

“이, 이 어린놈이 감히!”

여기서 끝낼 수는 없지. 나는 야무지게 준비해 둔 콤보를 꽂아 넣었다.

“응애. 나 애기 각주.”

“노오옴-!”

쿠당탕!

자리를 박차고 일어난 그의 불끈 쥔 주먹에 핏줄이 툭툭 불거진다.

아무런 이득도, 본전도 찾지 못한 황보군이 분노에 가득 찬 눈으로 나를 노려보던 그 순간이었다.

“놈이라……. 외람되지만 황보 가주께 한 가지만 여쭙겠습니다.”

불현듯 들려온 한마디.

부드러운 목소리 속엔 단단한 심지가 느껴졌다.

어느새 황보군을 응시하는 진위경의 눈동자는 서늘하게 가라앉아 있었다.

“묻건대, 황보 가주께서는 무림맹 내에서의 직책이 어찌 되십니까?”

“……!”

“아무리 화룡각주의 연배가 어리다 해도, 그는 화왕 적천강 대협의 진전을 이은 후인이자 무림맹의 각주입니다. 강호의 배분을 따져 보아도 결코 황보 가주의 아래가 아니지요.”

정곡이다. 아픈 부분을 찔린 황보군의 얼굴이 딱딱하게 굳었다.

그는 산동지방의 패자인 황보세가의 가주지만, 한 지방의 방비를 책임지는 외당 단주(團主)에 그쳤다.

그러니 공식적인 무림맹 직책 서열상으로는 내당 각주인 내 아래라고 할 수 있었다.

“그건…….”

말을 잇지 못하고 입술을 질끈 깨문 황보군이 도움을 청할 곳을 찾아 주위를 둘러본다.

하지만 그의 기대와는 달리, 황보군을 향한 사람들의 반응은 뜨뜻미지근했다.

“아미타불. 이만 자중하는 게 어떻겠소, 황보 시주.”

“허어, 신성한 맹주전에서 이런 소란이라니.”

“열화신룡. 아니, 화룡각주의 편을 드는 것이 아닐세. 두 사람 다 그만하면 되었으니 이만 자리에 앉게.”

내가 천연덕스럽게 대답했다.

“저는 처음부터 자리에 앉아 있었습니다.”

“그럼 한 사람만 남았군.”

누구를 가리키는 말인지는 명백하다.

그리고 이제는 멈춰야 한다는 이성적인 판단과 동한 지방의 패자이자 일가의 가주가 지닌 마지막 자존심 사이에서 갈등하던 황보군을 향해, 결정 장애를 해결할 수 있는 한마디가 날아들었다.

“귓구녕에 암기라도 박았느냐?”

화왕 적천강. 그의 짤막한 한마디와 함께 대회의실의 공기가 뜨겁게 달아오른다.

붉은 안광이 감도는 두 눈동자에 얼어붙은 황보군의 모습이 비쳤다.

“앉아. 지금 당장.”

“……!”

화아아악!

허공을 격하며 덮쳐 오는 기세에, 황보군의 눈이 부릅떠졌다. 아니, 대회의실에 자리한 모두가 마찬가지였다.

“으음.”

말없이 상황을 지켜보던 권왕 언화평이 신음을 흘리고.

“저, 적가. 네놈……!”

벽력도왕 팽철후의 시선이 격동한다.

그만큼 적천강의 기세는 강대했고, 또 하나의 태양처럼 압도적이었다.

아직 절정의 경지에 머무르는 자도, 이미 초절정에 오른 이들도 그의 힘을 느낄 수 있었다.

‘반로환동(返老還童).’

무공이라는 이름의 산맥은 험난하며 광활하다. 때로는 가파른 협곡을 지나쳐야 하고 깎아내린 듯한 절벽을 올라야 한다.

그리고 적천강은…… 그 끝에 존재하는 봉우리에 우뚝 선 위대한 무인이다.

지금의 그는 화왕(火王)이라는 별호를 뛰어넘는 존재가 되어 있었다. 이 자리의 또 다른 한 사람과 함께.

“적 대협.”

검성 매종학의 나직한 목소리가 울려 퍼진 순간, 대회의실을 휩쓸던 열풍(熱風)이 사라졌다.

순식간에 자신의 기세를 갈무리한 적천강이 퉁명스럽게 대꾸했다.

“무슨 일 있었소?”

“흠.”

“알겠소. 알았다니까. 저놈이 너무 시끄럽게 굴기에 겁 좀 준 것뿐이오.”

농담이 아니라, 두 번 겁줬다가는 오줌이라도 지릴 거다.

적천강이 말하는 ‘그놈’은 이미 새하얗게 질린 얼굴로 자리에 앉아 있었으니까.

“이제야 조용해졌군.”

작게 중얼거리는 적천강을 부드럽게 질책하는 눈빛으로 바라본 매종학이 입술을 뗐다.

어느덧 그의 시선은 나를 똑바로 향하고 있었다.

“화룡각주.”

“네.”

“자네는 산서와 하남. 그리고 사천과 호북에서 암천의 흉계에 맞섰지.”

정확히 말하자면 휘말렸다고 해야겠지만, 나는 조용히 고개를 끄덕였다.

이곳은 무림맹의 대회의장. 황보군을 상대하는 것과 앞으로의 중대사를 논하는 것은 비교할 수 없는 차이가 있다.

“그렇습니다.”

“예상컨대 자네만큼 암천에 잘 아는 사람은 드물겠지. 하여 본 맹주는 자네의 고견(高見)을 묻고 싶네.”

“저는 그 현장에 있었을 뿐. 확실한 정황과 천하 곳곳에서 무슨 일이 벌어지는지는 은영각에서 더 잘 알고 있을 겁니다. 이미 모든 것을 알려 드리기도 했고요.”

“직접 보고 겪은 그대로를 원하네. 그 모든 상황을 겪은 자네가 속에 품은 생각을.”

그래. 이렇게 나와야지.

앞에 던진 말은 앞으로 해야 할 말을 위한 밑밥에 불과하다.

한두 번의 양보와 사양은 미덕이고, 무림 맹주로서의 권위를 지닌 매종학이 이렇게까지 내 의견을 묻는다면 그만큼 힘이 실리기 마련이다.

‘좋아.’

나는 작게 심호흡했다.

지금까지의 내 위치가 자동차 뒷좌석이었다면 지금부터는 조수석이다.

짙은 안개가 낀 새벽, 내비게이션도 없이 초행길에 나선 운전자에게 내가 아는 모든 것을 알려 줄 수는 없다.

그러나 과속방지턱이 어디에 있는지, 지금 달려가는 이 길 앞에 무엇이 기다리고 있는지 정도는 말해 줄 수 있을 것이다.

‘얼마 전부터 머릿속을 떠나지 않던 그 불길한 생각도.’

생각을 정리하고 고개를 들자, 대회의실의 모든 사람이 오직 나 한 사람만을 바라보고 있었다.

수십 쌍의 시선.

이미 시작된 전쟁에서 수백, 수천의 목숨을 살릴 수도. 죽일 수도 있는 이들이다.

그들이 고작 약관을 넘긴 어린 핏덩이의 말을 얼마나 마음에 새길지는 미지수지만…….

‘상관없다. 이 전쟁에서 승리할 수 있다면. 조금이라도 위험과 희생을 줄일 수 있다면.’

지금 당장. 내가 할 수 있는 일을 해야 한다.

그런 생각 때문일까. 다음 순간 내 입술 사이로 흘러나온 목소리에는 평소와 다른 힘이 실려 있었다.

“암천은…….”



* * *



두 시진 뒤. 사람들이 모두 빠져나간 대회의실에는 단 세 사람만이 남아 있었다.

조금 전까지만 하더라도 수십여 명의 사람들이 자리했던 의자는 텅 비어 있었지만, 어느 순간부터 내려앉은 침묵은 떠나지 않았다.

아마 맹주전을 나간 이들 역시 지금쯤 그럴 것이라고, 천면호리 송호는 생각했다.

‘그럴 만도 하지.’

진태경의 입에서 흘러나온 말들은 그만큼 충격적이었다.

암천의 존재와 위험성을 모르는 사람은 없었지만, 그 젊은 청년만큼 위기를 경고한 사람은 아무도 없었다.

‘심지어 나조차도.’

은영각은 천하 각지의 정보를 끌어모아 수많은 예측을 쏟아낸다.

하루에도 수백 마리에 달하는 전서구가 가느다란 발목에 정보를 매달고 날아들고, 얼마 지나지 않아 다시 떠난다.

그렇기에 은영각의 수장인 천면호리는 암천이 얼마나 위험한 단체인지 모르지 않았다.

‘하지만…….’

열화신룡. 연달아 파란을 일으키는 화룡각의 젊은 주인의 생각은 예상을 훨씬 뛰어넘었다.

사람들이 위험을 말할 때 그는 재앙을 예고했고, 누군가가 과거 정마대전의 예를 들어 무림맹의 승리를 논할 때면 신랄하게 응대했다.



‘우리가 지금 마교랑 싸웁니까? 상대는 암천입니다, 암천.’

‘암천이 보여 준 것들은 단순한 마공이 아닙니다. 그러니까 이걸 뭐라 해야 하냐면, 아. 미치겠네. 좋아요. 일단 마공이라 칩시다.’

‘무슨 이유인지는 모르겠지만, 암천이 잠시나마 조용해진 이 틈에 바로 반격을 시작해야 합니다. 이대로 가다가는 끝장입니다. 다 죽어요.’

‘너무 과하지 않냐고 하신 분 누굽니까. 거기 가주님. 혹시 사지가 으스러져도 다시 살아나는 놈이나, 이무기랑 싸워 보셨어요? 한 식경 전쯤에 괴물 보고 오늘 저녁 뭐 먹을지밖에 생각 안 하셨습니까?’

‘우리가 싸워야 하는 상대는 평범한 사람이 아닙니다. 암천은 하나의 거대한 괴물이고, 얼마 후면 정말 저런 괴물들과 싸워야 할지도 모릅니다.’

‘제가 말이 좀 과했네요. 그런데 할 말은 해야겠습니다. 지금 당장 할 수 있는 모든 조치를 취해야 합니다. 특히 집에 신줏단지처럼 모셔 둔 신물이 있으면 더더욱 그렇고요.’



천면호리 송호는 문득 미간을 찡그렸다.

진태경이 말을 시작한 순간부터 의족이 연결된 부위가 욱신거리기 시작하더니, 이제는 불같은 통증이 일어나고 있었다.

‘불과 일 년 전만 하더라도 이렇지 않았는데.’

어느 순간부터 다시 시작된 통증은 노인이 되어 버린 그를 괴롭히기 시작했다.

마치 이럴 때가 아니라고 경고하는 것처럼.

심지어 오늘은 젊은 청년과 함께다.

‘마치 알고 있는 것 같았다. 나와 은영각. 아니 다른 모두가 모르는 어떤 사실을 미리 겪고 예측하는 듯했어.’

예측? 아니다. 천면호리 송호는 조금 전 자신이 떠올렸던 생각을 스스로 정정했다.

‘예언. 예언과도 같았지.’

문제는 그것이 정말 예언이냐는 의문이다.

천하의 누구보다 암천과 맞닿아 있는 그 청년의 말을 정말 믿어도 되는 것일까.

어디까지가 진실이고 과장일까.

천면호리가 고심에 잠겨 있던 바로 그 순간이었다.

“믿게.”

“예?”

번쩍 고개를 든 천면호리를 향해, 대회의실에 남아 있던 적천강이 말을 이었다.

“믿으라고 했네.”

“적 대협.”

“알아. 무슨 말을 하려는지. 하지만…….”

적천강의 어조가 문득 부드러워졌다.

“노부가 아는 그 녀석은, 단 한 번도 틀린 적이 없었지.”

“……!”

절대적인 신뢰가 느껴지는 한마디에 천면호리가 멈칫한 순간. 대회의장에 남아 있던 세 명 중 마지막 한 사람. 매종학이 불현듯 입을 열었다.

“세상에는, 정보로 짐작할 수 없는 확신이 존재하는 법일세.”

“맹주. 혹시 그 말씀은……?”

“맞네.”

자리에서 일어난 매종학이 천천히 말을 이었다.

“그를 호출하게. 화룡각에 첫 임무를 맡겨야겠네.”
```

## Final English reading copy

```markdown
# Chapter 547

A chilling silence descended over the great conference hall.

The reaction had been easy enough to predict even before I opened my mouth.

So had the identity of the first person among the dozens gathered here to spit something sharp at me.

“Do you call that something to say?”

*How does he never fail to live down to my expectations?*

I clicked my tongue inwardly as I watched the middle-aged man with half-white hair speak as though he had been waiting for his chance.

I already knew his name and status. He had glared at me so fiercely during our last gathering that I had wondered what his problem was. As it turned out, we had an indirect connection.

*They say blood never lies.*

The resemblance was unmistakable. The sharply raised eyes, the arrogant gaze that looked down on others, even the way he spoke.

“It seems you didn’t hear me.”

The middle-aged man with half-white hair was Hwangbo Gun, the Family Head of the Hwangbo Family and the father of Shandong Fist Dragon Hwangbo Ak. I slowly blinked at his question.

“Of course I heard you. Do you really think I didn’t?”

“Then why didn’t you answer?”

“Because your question is ridiculous. Of course I considered it speech—it came out of my own mouth. Did I make some kind of animal noise?”

Cheongpung, seated beside me, pricked up his ears.

“Benefactor, can you make animal noises too?”

“You keep your mouth shut, Young Hero Cheongpung. Unless you want to puke up the dumplings in your stomach.”

“Thank you…”

Hwangbo Gun’s face twisted violently as he watched us.

“Do you not understand what kind of gathering this is?”

“Is there anyone here who didn’t know?”

“And yet you dare speak so crudely in front of all these esteemed Seniors!”

“That’s why I was trying not to say anything. Besides, we should hear the Seniors’ opinions too. What do you think?”

At my sudden question, Mae Jonghak nodded.

“Fire Dragon Pavilion Master Jin is right. I have no problem with it. His words may be rough, but we need to face reality.”

“A-Alliance Leader!”

The panic in Hwangbo Gun’s cry was obvious, and I quickly cut him off.

“Yes. We’ve heard the esteemed opinion of the Murim Alliance Leader. While we’re at it, what does our Five Kings Hall Master think?”

Jeok Cheongang looked at Hwangbo Gun as though he were a bug.

“What the hell are you asking for? We’re fucked, aren’t we? Ignore that bastard’s nonsense and continue.”

“Thank you for the fiery answer.”

I turned to Hwangbo Gun and shrugged.

“That’s what those esteemed Seniors have to say.”

“……!”

There were plenty of people here who could be called Seniors, but not one of them could compare to Jeok Cheongang and Mae Jonghak.

If the heads of the Nine Sects and One Gang and the Five Great Families were influential corporals serving as squad leaders and veteran sergeants nearing discharge, then Murim Alliance Leader Mae Jonghak was a battalion commander, while Jeok Cheongang was a command sergeant major.

*If you’re behind in seniority, you should keep your mouth shut.*

And it wasn’t just seniority. Even if he tore off his insignia and challenged Jeok Cheongang as an equal, one punch from the Fire King would send him flying.

That was why even Wind-and-Cloud Sword Lord, the Sect Leader of the Zhongnan Sect and perhaps the foremost among those who disliked Cheongpung and me, kept his mouth firmly shut.

Which meant Hwangbo Gun had been left all alone.

*You have to look before you stretch out your legs. Why did he step forward by himself?*

I had heard that Hwangbo Gun had wielded considerable influence during the Great Faction War. I did not know whether he had always lacked political sense, or whether he had become a runaway locomotive over matters involving his only son, the sole heir of three generations.

I hummed a mournful melody.

“I’m a firefly. I have no friends.”

“You insolent young punk!”

There was no way I could end things there. I drove in the combo I had prepared so carefully.

“Waaah. I’m a baby Pavilion Master.”

“You braaaat!”

Crash!

Hwangbo Gun sprang to his feet, the veins bulging across his tightly clenched fists.

He glared at me with fury, having gained nothing and not even managed to break even, when a voice suddenly rang out.

“‘Punk’… I beg your pardon, but may I ask you one question, Family Head Hwangbo?”

The gentle voice carried a firm resolve beneath it.

Jin Wikyung’s eyes, which had somehow settled coldly on Hwangbo Gun, were devoid of warmth.

“May I ask what position you hold within the Murim Alliance, Family Head Hwangbo?”

“……!”

“Regardless of how young the Fire Dragon Pavilion Master may be, he is the successor to Great Hero Jeok, the Fire King, and a Pavilion Master of the Murim Alliance. Even if we consider seniority within the martial world, he is certainly not beneath you, Family Head Hwangbo.”

He had struck the bull’s-eye. Hwangbo Gun’s face stiffened as his sore spot was hit.

He was the Family Head of the Hwangbo Family, the hegemon of Shandong, but his official position was merely Outer Hall Squad Leader, responsible for the defenses of a single region.

In terms of the Murim Alliance’s official hierarchy, that placed him beneath me, an Inner Hall Pavilion Master.

“That…”

Hwangbo Gun bit down hard on his lips, unable to continue. He looked around for somewhere to seek help.

But contrary to his expectations, the people around him responded without much enthusiasm.

“Amitabha. Would it not be best for you to exercise some restraint, Benefactor Hwangbo?”

“Heavens. Such a disturbance in the sacred Alliance Leader’s Hall.”

“Blazing Flame Divine Dragon. No, I am not taking the Fire Dragon Pavilion Master’s side. Both of you have had enough, so sit down.”

I answered without a hint of shame.

“I’ve been sitting down from the start.”

“Then only one person remains.”

It was obvious whom he meant.

Hwangbo Gun was torn between his rational judgment, which told him he needed to stop, and the last shred of pride possessed by the hegemon of Shandong and Family Head of a great family.

Then a single remark flew toward him, one that solved his indecision.

“Did you get a hidden weapon stuck in your ear?”

It was the Fire King, Jeok Cheongang.

With his brief words, the atmosphere in the great conference hall heated up.

Hwangbo Gun’s frozen figure was reflected in his eyes, which glowed with a red light.

“Sit down. Right now.”

“……!”

Whoooosh!

As his aura surged through the air and crashed over them, Hwangbo Gun’s eyes flew wide.

No—not just his. Every person in the great conference hall reacted the same way.

“Hmm.”

Fist King Yan Hwapyeong, who had been watching the situation in silence, let out a low groan.

“J-Jeok! You bastard…!”

The Thunderbolt Saber King Peng Cheolhu’s gaze churned.

That was how powerful Jeok Cheongang’s aura was. It was overwhelming, like another sun.

Those still in the Peak realm could feel his strength. So could those who had already reached the Supreme Peak realm.

*Returned to Youth.*

The mountain range called martial arts was rugged and vast. Sometimes, one had to pass through steep ravines or climb cliffs as sheer as though they had been carved away.

And Jeok Cheongang…

He was a great martial artist standing proudly atop the peak at the very end.

The man he was now had surpassed the title of Fire King.

Together with one other person in this room.

“Great Hero Jeok.”

The moment Sword Saint Mae Jonghak’s low voice rang out, the hot wind sweeping through the great conference hall vanished.

Jeok Cheongang gathered his aura in an instant and answered gruffly.

“What happened?”

“Hmm.”

“All right. I understand. I only scared him a little because he was making too much noise.”

It was no joke. If he scared him twice, Hwangbo Gun would probably wet himself.

The “bastard” Jeok Cheongang was referring to was already sitting in his seat with a deathly white face.

“It’s finally quiet.”

Mae Jonghak looked at Jeok Cheongang with a gentle but reproachful gaze before parting his lips.

By then, his eyes were fixed directly on me.

“Fire Dragon Pavilion Master.”

“Yes.”

“You have opposed Dark Heaven in Shanxi and Henan, as well as Sichuan and Hubei.”

To be precise, I had been dragged into those incidents, but I quietly nodded.

This was the great conference hall of the Murim Alliance. Dealing with Hwangbo Gun and discussing matters of such importance were two entirely different things.

“That’s right.”

“Few people know Dark Heaven as well as you do. Therefore, I would like to hear your opinion.”

“I was merely present at those incidents. Hidden Shadow Pavilion probably knows the concrete details and what is happening throughout the world better than I do. I already told you everything I knew.”

“I want to hear what you saw and experienced yourself. I want to hear the thoughts held by the person who went through all of it.”

*There we go.*

The words I had spoken before this were nothing more than bait for what I needed to say next.

Yielding and demurring once or twice were virtues. And if Mae Jonghak, with all the authority of the Murim Alliance Leader, went this far to ask for my opinion, it would lend that opinion all the more weight.

*All right.*

I took a small breath.

If my position until now had been the back seat of a car, I had just moved into the passenger seat.

I could not tell a driver setting out along an unfamiliar road in the thick fog of dawn everything I knew, especially without a navigation system.

But I could tell him where the speed bumps were and what awaited us farther down the road we were racing along.

*Even that ominous thought that has refused to leave my mind lately.*

When I finished organizing my thoughts and raised my head, every person in the great conference hall was looking at me.

Dozens of pairs of eyes.

They were people who could save—or kill—hundreds, even thousands, of lives in a war that had already begun.

It was impossible to know how deeply they would take the words of a kid barely past twenty to heart, but…

*It doesn’t matter. If we can win this war. If I can reduce the danger and sacrifice even a little.*

I had to do what I could right now.

Perhaps because of that, the voice that escaped my lips a moment later carried a force unlike its usual tone.

“Dark Heaven…”

* * *

Two shichen later,[^1] only three people remained in the great conference hall after everyone else had left.

The chairs that dozens of people had occupied earlier stood empty, but the silence that had settled over the room at some point refused to leave.

Thousand-Faced Fox Song Ho thought that the people who had left the Alliance Leader’s Hall were probably in the same state by now.

*They had every reason to be.*

The words that had poured from Jin Taekyung’s mouth were that shocking.

No one was unaware of Dark Heaven’s existence or its danger, but no one had warned of the crisis as fiercely as that young man.

*Not even me.*

The Hidden Shadow Pavilion gathered information from every corner of the world and produced countless predictions.

Hundreds of messenger pigeons flew in every day with information tied to their slender ankles, then departed again not long after.

As the head of the Hidden Shadow Pavilion, Thousand-Faced Fox Song Ho was not ignorant of how dangerous Dark Heaven was.

*But…*

The young master of the Fire Dragon Pavilion, Blazing Flame Divine Dragon Jin Taekyung, whose actions had caused one upheaval after another, had thought far beyond Song Ho’s expectations.

When people spoke of danger, he announced disaster. When someone cited the Great Faction War and argued that the Murim Alliance would prevail, he answered with biting sarcasm.

“Are we fighting the Demonic Cult right now? Our opponent is Dark Heaven, Dark Heaven.”

“What Dark Heaven showed us isn’t ordinary demonic martial arts. So what should we call it? Ah, this is driving me crazy. Fine. Let’s call it demonic martial arts for now.”

“I don’t know why, but while Dark Heaven has gone quiet for a little while, we need to begin our counterattack immediately. If we continue like this, we’re finished. Everyone dies.”

“Who said I was being too extreme? You there, Family Head. Have you ever fought something that came back to life even after all four of its limbs had been crushed? Or an imugi? About half an hour ago, did you see a monster and think of nothing but what to eat for dinner?”

“Our opponent is not an ordinary person. Dark Heaven is one enormous monster, and before long, we may have to fight monsters like that.”

“I may have gone a little too far. But I have to say this. We need to take every measure we can right now. Especially if you have some sacred object enshrined at home like a household god.”

Song Ho suddenly furrowed his brow.

From the moment Jin Taekyung began speaking, the area where his prosthetic leg was attached had started to throb. Now, a searing pain had broken out there.

*It wasn’t like this even a year ago.*

The pain that had resumed at some point had begun tormenting him again after he had grown old.

As though warning him that this was no time for such things.

And today, he was even in the company of that young man.

*It was as though he knew. As though he had experienced something in advance and was predicting some truth that I and the Hidden Shadow Pavilion—no, that everyone else—knew nothing about.*

A prediction? No.

Thousand-Faced Fox Song Ho corrected the thought he had just formed.

*A prophecy. It was like a prophecy.*

The question was whether it truly was one.

Could he really trust the words of that young man, whose life had brushed against Dark Heaven more closely than anyone else’s?

Where did the truth end and the exaggeration begin?

It was at that exact moment, while Song Ho was lost in thought, that a voice spoke.

“Believe him.”

“Hm?”

Jeok Cheongang, who remained in the great conference hall, continued when Song Ho looked up sharply.

“I said you should believe him.”

“Great Hero Jeok.”

“I know what you’re going to say. But…”

Jeok Cheongang’s tone suddenly softened.

“The kid I know has never once been wrong.”

“……!”

Song Ho froze at those words, which carried absolute trust.

Then Mae Jonghak, the last of the three people remaining in the hall, suddenly spoke.

“There are certainties in this world that cannot be inferred from information.”

“Alliance Leader. Do you mean…?”

“That’s right.”

Mae Jonghak rose from his seat and continued slowly.

“Have him summoned. We must assign the Fire Dragon Pavilion its first mission.”

[^1]: A shichen is a traditional Chinese time unit lasting approximately two hours.
```

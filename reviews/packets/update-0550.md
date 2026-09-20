<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0550.txt",
      "sha256": "8d5bcdf83b23357f1c6fe4114b78fa0deda7501ca4ce91b8ef5b8fe238e20659",
      "bytes": 12692
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "eecdc2ac6f9c0b0bcbd04f430e93c32e527c61ea706feeb55586eda4a811cf3a",
      "bytes": 3190
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "8f5da66569a6ad674a557886cf6911e213f5ede53dd7180d8fb02515c8a52244",
      "bytes": 174793
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "a3cc575164fc465a91c7a1dfa1e4115dfc51f2c0d6dc6e3a2e22a6dab2e60312",
      "bytes": 1371
    },
    {
      "path": "characters/Human Butcher.md",
      "sha256": "101d2983da2a27f2c08c89176a0b330cfa02ce1529988ccf1e261ed02b475d84",
      "bytes": 667
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "3fb6d3bcb48756bb66d4eb67b058085a5e8515f2dbcd70d37b22ee39d4b7045d",
      "bytes": 1147
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "23db5cd1933ff60846338df33b3a5754341d566faae15a75fcdb7a0b8e017acb",
      "bytes": 1702
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "a7794e1c909e163a8e194f843ae47da2f3a976c23766452823dd91bc7164f257",
      "bytes": 2292
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "87ebd2264499418d17b494c32ffea7c0221b27057aadb334c1cbb8a998563f80",
      "bytes": 622
    },
    {
      "path": "characters/Ju Hwaran.md",
      "sha256": "53d40d53557288686c6de0696be2ff6c4b52754902b4cfeec64e73533354db4f",
      "bytes": 959
    },
    {
      "path": "characters/Mae Jonghak.md",
      "sha256": "c1e02ec19e95af451cfbce81a9a08e8ca2d18677020a27b5db5d8000caf0fa35",
      "bytes": 1061
    },
    {
      "path": "characters/Mungyeong.md",
      "sha256": "3bcb747bbc926142f70d1a0a06a46d9b923e3569825e8ef59b9a747ccdf67579",
      "bytes": 1233
    },
    {
      "path": "characters/Song Il.md",
      "sha256": "9f2e0d2dba897be4e140cad2bf22f685bf924bd5a78704dd7c58027ffd20aa7e",
      "bytes": 964
    },
    {
      "path": "characters/Song Ilseom.md",
      "sha256": "016d4e97f4eb6195a1b6706e9a99ad05597bf1d9dfc5b76a148fd21080c8eb1f",
      "bytes": 751
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "da7a0f36d3644731f927d26a782ad3b0419a695ed924eea713365e0f9cb3d704",
      "bytes": 165874
    }
  ],
  "estimated_tokens": 13905
}
-->

# Durable State Update — Chapter 550

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 550. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 550. Profile updates may replace only one
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
  "chapter": 550,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 550,
    "continuity_sources": [550],
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
    "The six-member Fire Dragon Pavilion, led by Jin Taekyung, must depart immediately for the Nanman Beast Palace and regroup at Mount Daebyeol after arranging discreet transport.",
    "Ju Hwaran is a capable Fire Dragon Pavilion member with prior Nanman escort experience and route knowledge from the Escort King's records.",
    "The Mount Song Resolution restored the Murim Alliance; Mae Jonghak is Alliance Leader, Jeok Cheongang heads the Five Kings Hall, and Murong Yeonghwi oversees Murong Family defenses in Liaoning.",
    "Jin Taekyung is a Supreme Peak master with Three Flowers Gather at the Crown, advanced Qi Sense, exceptional resistance to monster Fear, and public S-rank-level recognition while retaining an A-rank license.",
    "Cheongpung is master of the Azure Dragon Pavilion, creator of Mimi Step, and caretaker of Mimi, whose condition was recently examined by Mungyeong.",
    "Mungyeong ended Taekyung's direct training and assigned him the final task of incorporating martial principles into his learned martial arts.",
    "Zhuge Feng's Demon-Sealing Formation still blocks mana from the exposed Gate, while Jang Taebo processes the Water God Dragon's remains.",
    "Dark Heaven remains an enormous monster-like threat capable of causing rifts and creating mutants; the mechanism behind Jang Sam's transformation remains unresolved.",
    "The Southern Heaven Demon Empress is believed by Taekyung to be moving toward the suspected next target, while Song Ho's dispatch there has received no reply for more than seven days.",
    "The Black Dragon Demon Gate remains a major unorthodox power; Sama Pyo is its Young Sect Leader and Black Dragon Saber, with Taishan as his giant subordinate.",
    "Jin Wikyung is Taekyung's eldest brother and has accepted that Taekyung keeps important secrets, asking to hear them when the crisis is over.",
    "Jeok Cheongang and Mae Jonghak now treat Taekyung's warning about a monster catastrophe as credible enough to justify immediate action."
  ],
  "continuity_sources": [
    549,
    548
  ],
  "open_questions": [
    "What is the Lord of Heaven's identity, how is he connected to the dangerous force Taekyung associates with his original world, and how can Dark Heaven open Gates?",
    "What will Taekyung's party find in Nanman, and what does the Southern Heaven Demon Empress intend there?",
    "What is the outcome of the duel between Jeok Cheongang and Nangong Cheon, the Azure Sky Sword King?",
    "Why did Ju Hwaran and Sama Pyo's political engagement end?",
    "What process created Jang Sam's mutant form, and can Dark Heaven's mutants absorb human energy?"
  ],
  "safe_through": 549,
  "temporary_decisions": [
    "Render 건량 as dry rations, 광서 as Guangxi, 대별산 as Mount Daebyeol, 만리행 as Ten-Thousand-Li Journey, and 고잉메리호 as Going Merry.",
    "Render 반 시진 as half a shichen and retain Nanman, Nanman Beast Palace, Fire Dragon Pavilion, Great Hero, and Young Lady Ju.",
    "Preserve Taekyung's blunt profanity and financial, monster, no-kids-zone, and P-King humor, along with Taishan's clipped childlike speech."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 매종학    | **Mae Jonghak**    |
| 청풍     | **Cheongpung**     |
| 송일     | **Song Il**        |
| 주화란    | **Ju Hwaran**      |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 검성     | **Sword Saint**               | Mae Jonghak    |
| 살성     | **Slaughter Saint**           | —              |
| 태원진가   | **Jin Family of Taiyuan**        |
| 암천     | **Dark Heaven**                  |
| 남만야수궁  | **Nanman Beast Palace**          |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 살기     | **killing intent**                               |                                                       |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 중원     | **Central Plains**                               |                                                       |
| 은인     | **Benefactor**                               |
| 시스템              | **System**                     |
| 명성               | **Fame**                       |
| 퀘스트              | **Quest**                      |
| 보상               | **Reward**                     |
| 칭호               | **Title**                      |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 헌터      | **Hunter**            |
| 태원     | **Taiyuan**            |
| 하남     | **Henan**              |
| 사천     | **Sichuan**            |
| 소협      | **Young Hero**                                                  |
| 공자      | **Young Master**                                                |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 문경 | **Mungyeong** | Young medical apprentice and newly introduced passenger. |
| 송일섬 | **Song Ilseom** | Young escort captain of the Yongbong Escort Bureau; distinct from Song Il of Zhongnan. |
| 삼공자 | **Third Young Master** | Title used for Jin Taekyung. |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 운남 | **Yunnan** | Region from which Jongni Chu comes. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 화란 | **Hwaran** | Familiar short form of Ju Hwaran. |
| 의생 | **medical apprentice** | Mungyeong's occupation. |
| 맹주전 | **Alliance Leader's Hall** | Hall directly associated with the Murim Alliance Leader. |
| 귀주 | **Guizhou** | Region whose Murim representatives send a delegate. |
| 화룡각 | **Fire Dragon Pavilion** | New name chosen for Taekyung's pavilion. |
| 광서 | **Guangxi** | Region bordering Nanman. |

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
| 매종학 | 청풍 | grandfather_to_grandson | Pung | affectionate-instructional | Mae Jonghak calls young Cheongpung 풍아 while teaching him the Crouching Tiger Fist. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 적천강 | 청풍 | overwhelming_elder_to_young_martial_artist | you / little punk | blunt, amused, and threatening | Jeok Cheongang uses 네, 이놈, and related blunt forms while testing Cheongpung. |
| 청풍 | 적천강 | young_martial_artist_to_overwhelming_elder | Grandpa Jeok | casual-familiar despite deference | Cheongpung uses 적 할아버지 while asking Jeok Cheongang to confirm Taekyung's condition; this is a familial form of address, not literal kinship. |
| 혁무진 | 적천강 | subordinate_to_overwhelming_elder | Great Hero Jeok | deferential and fearful | Mujin uses 적 대협 while reporting Jeok’s orders and Taekyung’s awakening. |
| 적천강 | 혁무진 | overwhelming_elder_to_junior_martial_artist | you stupid fool | blunt and mocking | Jeok calls Mujin a 멍청한 놈 after knocking him down during the attempted escape. |
| 송일 | 진태경 | hostile Zhongnan Elder to accused outsider | you / Jin Taekyung | hostile and threatening | Song Il questions Taekyung's identity and later threatens him over Gong Ilhyuk's injury. |
| 송일 | 청풍 | hostile Zhongnan Elder to younger martial artist | Sword Saint's heir / you | hostile and threatening | Song Il identifies Cheongpung as the Sword Saint's heir and demands that he face the consequences of injuring Gong Ilhyuk. |
| 송일 | 적천강 | former rescued junior to former rescuer | Great Hero Jeok | formal, fearful, and defensive | Uses 적 대협 while insisting that Jeok has no business interfering in the dispute. |
| 적천강 | 송일 | former rescuer to former rescued junior | Zhongnan brat; you; insolent bastard | blunt, mocking, and humiliating | Jeok recalls Song's youthful arrogance and addresses him with contempt while publicly disciplining him. |
| 매종학 | 진태경 | older_ally_to_younger_friend | friend | casual-familiar | Mae Jonghak uses 친구 when arriving at Taekyung's window and asking to talk. |
| 송일섬 | 주화란 | escort_captain_to_young_bureau_head | Hwaran | urgent and familiar | Calls out 화란아 while urgently warning Ju Hwaran before stepping into the confrontation. |
| 주화란 | 진태경 | escort_bureau_leader_to_famous_younger_martial_artist | Young Hero Jin | formal-deferential | Hwaran introduces herself as the Young Bureau Head and formally greets Taekyung as 진 소협. |
| 진태경 | 주화란 | visitor_to_young_bureau_head | Young Lady Ju | formal-polite | Taekyung uses 주 소저 while announcing that his party must leave. |
| 주화란 | 혁무진 | rescued_survivor_to_benefactor | Benefactor | formal-deferential | Hwaran includes Mujin among the Benefactors when greeting Taekyung's companions. |
| 주화란 | 청풍 | rescued_survivor_to_benefactor | Benefactor | formal-deferential | Hwaran includes Cheongpung among the Benefactors when greeting Taekyung's companions. |
| 주화란 | 송일섬 | bureau_head_to_escort_captain | Captain Song | formal and prosecutorial | Uses his office title, then his personal name, while exposing and confronting him. |
| 진태경 | 문경 | young_martial_artist_to_medical_apprentice | Young Hero | formal-polite | Taekyung addresses the non-martial Mungyeong as 소협 while praising his actions. |
| 문경 | 진태경 | young_passenger_to_younger_martial_artist | Young Hero | deferential | Mungyeong uses 소협 while asking Taekyung for help boarding the ship. |
| 청풍 | 문경 | martial_companion_to_medical_apprentice | Medical Apprentice | cheerful-polite | Cheongpung addresses Mungyeong as 의생님 while asking him to greet the Tang Clan. |
| 문경 | 적천강 | old_acquaintances | Fire King | familiar and grave | The figure bearing Mungyeong’s name greets Jeok Cheongang by his established epithet. |
| 적천강 | 문경 | overwhelming elder to old acquaintance | you / little punk | mocking and threatening | Mocks Mungyeong's expression and threatens to poke out his eyes. |
| 문경 | 혁무진 | traveling_companion_to_traveling_companion | Martial Warrior Hyuk | formal-polite | Mungyeong asks Mujin to deliver water to Taekyung and lets Mujin receive the credit. |
| 혁무진 | 문경 | traveling_companion_to_traveling_companion | Mungyeong | casual-familiar | Mujin recognizes Mungyeong while reacting to Taekyung's dismantling work. |
| 매종학 | 적천강 | long-standing martial rival and friend | Great Hero Jeok | casual and familiar | Mae addresses Jeok as 적 대협 while discussing the Alliance Leader position. |
| 적천강 | 매종학 | long-standing martial rival and friend | you | blunt and familiar | Jeok addresses Mae as 당신 while recalling their meeting at Mount Jiuhua. |
| 청풍 | 매종학 | grandson to grandfather | Grandpa | casual-familiar | Repeatedly calls Mae Jonghak 할아버지 while mistaking the Alliance Leader's summons as a family visit. |
| 진태경 | 매종학 | younger ally to newly installed Alliance Leader | Alliance Leader | formal and deferential | Uses 맹주님 while formally greeting Mae Jonghak as the Alliance Leader. |
| 문경 | 청풍 | martial_master_to_prospective_companion | you | blunt and informal | Mungyeong questions Cheongpung about Mimi Step and why he offered to accompany him. |
| 진태경 | 송일섬 | pavilion master to prospective member | Song Ilseom | direct and evaluative | Taekyung directly names Song Ilseom while comparing his qualifications with Hwaran's. |

## Listed compact profiles

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 548
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, the grandson and Disciple of Sword Saint Mae Jonghak, a Supreme Peak martial master known as the Huashan Divine Dragon, the creator of the snake-inspired Mimi Step footwork technique, and the master of the Azure Dragon Pavilion within the Alliance Leader's Two Dragons Pavilion.
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, a deep love of martial arts, competitive pride, unusual resistance to monster-induced Fear, and discomfort when someone copies his martial arts.
- **Voice:** Dreamy and hazy, with innocent, polite phrasing; he has begun imitating Taekyung's profanity.
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions while Taekyung is his only true martial rival; Tang Sadok has temporarily entrusted Mimi, now a large horned snake, to him, Mungyeong recently examined her condition, and Mungyeong accepted Cheongpung's offer to accompany him after Cheongpung pledged to learn by observation rather than formal instruction.

### Human Butcher.md

# Human Butcher (인도)

- **Safe through:** Chapter 541
- **Aliases:** None
- **Role:** Former mysterious Han Chinese mounted-bandit power in Northern Gaoyuan commanding fifty subordinates; a Peak master killed by an unnamed old man in a single move
- **Personality:** Cold, intimidating, and murderous; he kills people as though slaughtering livestock
- **Voice:** Cold, curt, and quietly threatening
- **Relationships:** He is one of four powerful participants at the Northern Gaoyuan gathering, intimidates Temur, and has claimed Ghost Sword Wipeng as his personal target in the proposed attack

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 549
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and a member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 548
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm, and the occupant of the chief seat of the Murim Alliance's Five Kings Hall.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 548
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, a Supreme Peak master who possesses the Heavenly Martial Physique and superhuman physical strength, has manifested Force, opened his Middle Dantian, crossed the wall into true mastery, has achieved Three Flowers Gather at the Crown but not Five Qi Returning to Origin, can perceive the texture of qi well enough to sever layered magic, can resist high-level monster Fear through exceptional mental strength, is publicly recognized as an S-rank-level Hunter while formally retaining an A-rank license pending testing, can command coordinated raids against powerful monsters, and now serves as one of the two pavilion masters of the Alliance Leader's direct Fire Dragon Pavilion while holding its unique Title, Fire Dragon Pavilion Master and leading its first mission to Nanman.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor and assigned him a final task to incorporate martial principles into his learned martial arts but declined Taekyung's recruitment after Cheongpung reached him first, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate, student, and trusted manager of media and official arrangements, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, and Xiao Shen regards him as an older brother after Jin saved him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 548
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Ju Hwaran.md

# Ju Hwaran (주화란)

- **Safe through:** Chapter 549
- **Aliases:** Hwaran
- **Role:** Ju Hwaran is a Level 88 Young Bureau Head, leader of the Yongbong Escort Bureau, a member of the Fire Dragon Pavilion, and an experienced Nanman escort guide with route knowledge from the Escort King's records.
- **Personality:** Intelligent, capable, responsible, filial, composed under pressure, and burdened by intense guilt over the escort journey's deaths.
- **Voice:** Clear, polite, restrained, and determined.
- **Relationships:** Escort King Ju Gongsan was her paternal grandfather and rescued the Guangdong Chen Family’s surviving child, who became Song Ilseom’s grandmother; Ju Hogun is her father, Heo Jun was her uncle, Sama Pyo was her former fiancé in a political engagement she accepted for her father's sake, Song Ilseom is her direct escort, and Jin Taekyung is a trusted ally.

### Mae Jonghak.md

# Mae Jonghak (매종학)

- **Safe through:** Chapter 548
- **Aliases:** Sword Saint
- **Role:** Sword Saint and Cheongpung's grandfather who now serves as the New Murim Alliance's Alliance Leader and has ordered Jin Taekyung's first Fire Dragon Pavilion mission to Nanman.
- **Personality:** Playful, easygoing, and teasing, but capable of handling heavy administrative responsibilities efficiently.
- **Voice:** Friendly, casually familiar, and cheerfully teasing, including when greeting old acquaintances and discussing leadership.
- **Relationships:** Cheongpung's grandfather and martial instructor; taught him the Taeeul Miri Palm; secretly entered Huashan while its Sect Leader slept, left a dagger and handwritten note, and then went into hiding, prompting Huashan's search; fought Jeok Cheongang at Mount Jiuhua more than forty years ago and left after their draw; his old friend Hong Dao left him a letter identifying Jin Taekyung as the Morning Star who would drive away darkness.

### Mungyeong.md

# Mungyeong (문경)

- **Safe through:** Chapter 546
- **Aliases:** Killing Ghost
- **Role:** Mungyeong is the legendary physician known as the former Divine Physician and Slaughter Saint, a Returned to Youth Supreme Peak master and the greatest assassin in history; he was the sole survivor of an assassin training cohort that began with three hundred candidates and passed the Divine Physician title to his Disciple.
- **Personality:** Compassionate, resolute, resourceful, and calm under extreme pressure.
- **Voice:** His Mungyeong persona is timid, deferential, and cheerful, while his Slaughter Saint voice is dry, impassive, and blunt.
- **Relationships:** Dong Feng is his Disciple, Jeok Cheongang is an old acquaintance whom Mungyeong helped break free of his Heart Demon, Mungyeong was asked to look after and instruct Jin Taekyung and has now ended that direct training after teaching him martial principles and giving him a custom fire-qi pill, Cheongpung has offered him companionship and Mungyeong accepted, and Mu Song plus five Water Dragon Stronghold subordinates know he is an exceptionally powerful master but not that he is the Slaughter Saint.

### Song Il.md

# Song Il (송일)

- **Safe through:** Chapter 549
- **Aliases:** Roaring Fury Swordsman
- **Role:** Elder of the Zhongnan Sect and the Roaring Fury Swordsman; senior brother of Sect Leader Gong Iljung; came to the Jin Family of Taiyuan to demand redress for Gong Ilhyuk's injury and the alleged insult to Zhongnan; attacked Jin Taekyung with the Heavenly River Thirty-Six Swords, was stopped by Jeok Cheongang, and was publicly humiliated by him.
- **Personality:** Arrogant, domineering, punitive, and confident in his martial power and seniority.
- **Voice:** Gruff, cutting, condescending, and threatening, with formal authority used to pressure those beneath him.
- **Relationships:** Gong Iljung is his junior Sect Leader and martial younger brother; Gong Ilhyuk is a junior Disciple of his sect; he recognizes Baek Museong and Cheongpung through their Huashan and Sword Saint connections.

### Song Ilseom.md

# Song Ilseom (송일섬)

- **Safe through:** Chapter 549
- **Aliases:** Escort Captain Song
- **Role:** Level 110 young escort captain of the Yongbong Escort Bureau, one of its Dragon-Phoenix Three Escorts, and a newly accepted member of Jin Taekyung and Cheongpung’s Fire Dragon Pavilion.
- **Personality:** Blunt, decisive, survival-hardened, and dryly self-aware, with little patience for insults or disorder.
- **Voice:** Forceful and urgent in command, with a rough and confrontational edge.
- **Relationships:** He serves under Ju Hwaran, is Song Pyosan’s son, and his grandmother was the surviving Guangdong Chen child rescued by Ju Gongsan during the Great Faction War.

## Korean source

```text
＃550화



모두가 떠난 뒤. 혁무진이 필요한 것을 챙긴다며 부산스럽게 사라지자 홀로 남게 된 나는 조용히 입을 열었다.

“퀘스트 창 오픈.”

띠링.



퀘스트



[남만행(南蠻行)]



무림 맹주 매종학이 화룡각에 첫 번째 임무를 부여했습니다.

이제 당신은 남만으로 향하여 혹시 모를 상황에 능동적으로 대처해야 합니다.

당신과 화룡각의 앞길에 무엇이 있을지는 알 수 없는 상황.

늘 주위를 경계하고, 유연한 사고방식으로 행동하십시오.



등급 : 절정

제한 : 진태경 및 화룡각 인원

임무 : 남만 진입 (미완료)

보상 : 연계 퀘스트

 ???

실패 : 칭호, [남만을 못 가] 획득

 명성 및 신뢰도 대폭 하락





[남만행]은 매종학에게 임무를 받으며 생성된 퀘스트였다.

설명이나 임무 칸만 봐도 알 수 있듯이, 이번에는 시스템도 딱히 이렇다 할 힌트를 던져 주지 않았다.

‘제한 시간도 없고.’

그만큼 시간이 넉넉해서가 아니라, 한 치 앞도 모르는 상황이라는 것으로 해석되는 건 결코 과민 반응이 아닐 것이다.

작게 한숨을 내쉰 나는 퀘스트 창을 껐다.

‘아무 일도 일어나지 않는다면 그건 그것대로 다행이긴 한데…….’

만약 일이 터진다면 걷잡을 수 없다. 그리고 나는 화룡각의 인원들을 이끌고 신속히 사태를 진압, 무사히 귀환해야 한다.

혼자 먹고살기도 힘든 상황에서 책임자가 되다니. 새삼 각주라는 두 글자가 마음을 무겁게 짓누르던 그때였다.

“저어…….”

불쑥 귓가를 파고드는 목소리.

뒤를 돌아보니 웬 보따리를 든 청풍이 반쯤 부서진 문 앞에서 멀뚱멀뚱 이쪽을 쳐다보고 있었다.

“은인, 들어가도 돼요?”

“……누가 들으면 항상 허락 맡고 들어온 줄 알겠네.”

문 멀쩡할 때는 노크도 안 하고 벌컥벌컥 잘도 들어오던 녀석이, 박살 난 문 앞에서 저러고 있으니 기도 안 찬다.

실소를 흘린 나는 청풍을 향해 손짓했다.

“그냥 들어와. 안 그래도 한 번 보러 가려고 했는데, 잘됐네.”

“굳이 허락하지 않아도 그럴 생각이었다.”

들려온 대답은 당연하게도 청풍의 입에서 흘러나온 것이 아니었다. 나는 유령처럼 나타난 문경을 보며 떨떠름하게 중얼거렸다.

“청 소협한테 한 말이었는데요.”

“그래서 말했을 텐데. 네놈 허락은 필요 없다고.”

아무렇지 않게 별채 안으로 들어선 문경이 탁자 위에 놓인 잔과 흐트러진 의자들을 힐끗 바라보았다.

“누가 왔다 간 모양이군. 네놈과 혁가를 포함해서 총 여섯. 그중 한 명은 여인이고.”

“그걸 어떻게 아셨어요?”

“보면 안다.”

건조한 문경의 대답에, 청풍이 천진난만한 어조로 한 마디를 덧붙였다.

“다른 분들이 떠나는 거 보고 왔어요. 사람 없을 때 찾아와야 할 것 같아서.”

“…….”

“…….”

뭐여, 시벌.

불신이 가득 담긴 내 눈빛에 문경이 뭐 어쩔거냐는 표정으로 재차 입을 열었다.

“보면, 안다.”

“그 보면 안다는 게, 진짜 눈으로 봐서 아는 거였습니까?”

“이런 것 따위 굳이 보지 않더라도 알 수 있었다.”

“먼 산 보지 마십쇼. 어차피 주위에 건물만 가득해서 산도 안 보이는데.”

“대신 네놈의 앞날이 보이는군. 한마디만 더 지껄이면 이 방에 혈향이 가득 찰 것 같은 기분이야.”

“…….”

빌어먹을 노인네. 이러면서 본인은 의생이니 어쩌니 코스프레나 하고 있다니.

악랄한 폰의생의 만행에 치를 떤 나는 청풍을 향해 고개를 돌렸다.

“그런데 무슨 일이야?”

“작별 인사를 드리려고요.”

“뭐?”

청풍이 뒤통수를 긁적이며 웃었다.

“아까 맹주전 앞에서 저한테 먼저 가라고 하셨을 때, 왠지 은인께서 곧 떠나실 것 같았거든요. 헤헤.”

직접 말한 적도 없는데, 청풍도 내심 어느 정도 짐작을 했던 모양이다.

잠시 망설이던 나는 선선히 고개를 끄덕였다.

“맞아. 임무야.”

“아앗. 그럼 어디로 가세요?”

“남만.”

“남……만이요?”

내 대답에 청풍의 눈동자가 휘둥그레진다. 뭔가를 생각하던 문경이 나직하게 뇌까렸다.

“남만이라면, 야수궁?”

“예.”

“그 괴이한 현상. 균열 때문이로군.”

“맞습니다. 두 번째 균열이 일어난다면, 아무래도 암천 입장에서는 그곳만큼 적격인 장소를 찾기 힘들 테니까요.”

“충분히 가능성 있는 이야기다. 더군다나 중원과의 거리가 멀고도 험하니, 남만야수궁이 당한다면 운남(雲南)을 시작으로 혼란이 들불처럼 번져 나갈 테고.”

나 역시 문경의 생각과 같다.

만약 정말 암천이 남만에서 흉계를 꾸미고 있으며, 그 계획이 성공한다면 전화(戰火)의 불길은 운남성 한 곳에서 멈추지 않는다.

‘맞닿아 있는 귀주(貴州), 광서(廣西). 그리고 지난번 전투로 상당한 피해를 입은 사천(四川)까지 옮겨붙겠지.’

귀주성과 광주성은 특히나 기반이 취약한 곳이다.

각 성에 존재하는 문파와 무림인들의 숫자가 다른 지방보다 적고, 그 세력이 지닌 힘 역시 떨어지니 더 빠르게 타오를 것이 분명했다.

“이런 상황에서 남만행이라, 험난한 여정이 되겠군.”

“아무 일도 생기지 않는다면 다행이고, 아니라면…… 무슨 수를 써서든 막아 내야죠.

“고작 여섯이서 말이냐?”

“무려 여섯이죠.”

“……?”

“제가 소문에 듣기로는 그중에 화왕과 살성에게서 가르침을 받은 젊고 잘생긴 초절정 고수가 하나 있다라고요. 혹시 들어 보신 적 없습니까?”

“못 들어 봤다. 특히 잘생겼다는 소리는 단 한 번도.”

“……아, 예.”

칼같이 자르는 것 보소. 내 헛소리를 단번에 틀어막은 문경이 청풍을 바라보며 말을 이었다.

“대신 다른 소문은 들어 봤지. 만두에 환장하는 어느 놈이 젊은 의생 하나를 붙잡고 눈대중으로 무공을 익히고 있다는 것.”

“어?”

지금 내가 뭘 들은 거지?

생각이 얼굴 위로 고스란히 드러난 모양이다. 내 표정을 본 문경이 고개를 끄덕였다.

“아마도 네놈이 지금 생각하고 있는 그게 맞을 거다.”

“정말입니까?”

“사실이다.”

“아니, 왜 킹갓검성을 놔두고 굳이 성격도 더러운…… 죄송합니다. 말이 헛나왔네요.”

나는 어느새 소매에서 소검(小劍)을 꺼낸 문경의 스산한 눈빛을 애써 외면하며 청풍을 바라보았다.

“만약에 협박당하는 거라면 눈을 두 번 깜빡여.”

“이런 쳐죽일…….”

“헤헤. 전부 사실이에요, 은인.”

청풍을 물끄러미 응시하던 나는 어깨를 으쓱해 보였다.

“알아. 나도 농담 한번 해 본 거야.”

굳이 듣지 않아도 안다. 녀석이 왜 문경을 찾아갔는지. 그로부터 무엇을 얻고자 하는지.

‘강해지기 위해서. 이 세상에 맞춰 변하기 위해서.’

일 년도 더 지난 이야기다.

객잔으로 향하는 내게, 거지꼴을 한 웬 젊은 놈이 다가와 대뜸 당과 하나만 달라고 부탁한 것은.

나는 혁무진의 만류에도 그에게 모든 당과를 주었고 그렇게 청풍과의 인연이 시작되었다.

‘많이 달라졌지. 나도, 저 녀석도.’

가문의 수치라 불리던 태원진가의 삼공자는 무림을 격동시키는 초절정 고수가 되었고, 무공을 사랑하고 세상에서 겪는 크고 작은 일들이 마냥 좋았던 젊은 천재는, 어느 날부터인가 단단한 심지를 품게 되었다.

보이지는 않지만 느껴진다.

다른 이들은 알 수 없는 청풍의 변화를, 나를 비롯한 극소수의 주변인들은 알고 있었다.

툭.

문득 손을 뻗어 청풍의 어깨를 두드리자 녀석의 눈이 동그랗게 떠졌다.

“은인?”

“그냥. 힘내라고.”

빤히 나를 바라보던 청풍의 눈매가 초승달처럼 휘었다.

“네. 은인도요.”

“당연히 내가 더 힘내야지. 그나마 청 소협은 믿을 만한 구석이라도 있지, 이쪽은 비빌 수 있는 언덕도 없거든.”

말없이 나와 청풍의 대화를 지켜보던 문경이 불현듯 입을 열었다.

“그러고 보니 그 언덕이 보이지 않는데.”

“그 언덕은 하남에 남고, 저와 다른 사람들만 떠납니다.”

“오래 살고 볼 일이군. 화왕, 그자가 그런 결정을 내리다니.”

“낯간지럽지만 대의(大義)라고 해 두죠. 지금 상황에서는 더 많은 손이 필요하니까요.”

대답하는 와중에도 마음 한구석이 공허했다.

아마도 적천강을 처음 만난 이후, 그와 떨어져 움직이게 되는 것이 처음이라 그런 것일지도 모르겠다.

적천강이 오랜 시간 동안 의식을 잃었을 때도 우리는 늘 함께였으니까.

‘하지만 이제는 홀로서기를 해야 할 때.’

적천강의 품 안은 크고 넓었지만, 그 안에 계속 머무르기에는 내가 너무 일찍 성장해 버렸다.

그리고 격변하는 상황은 우리 두 사람의 동행을 허락하지 않을 것이다.

‘혹시……?’

문득 뇌리를 스치는 한 가지 생각에, 나는 슬쩍 고개를 돌려 창밖을 바라보았다.

그러나 대로변을 오가는 얼굴들은 온통 낯설고 흐릿하다.

기다리는 사람은 끝끝내 모습을 보이지 않았다.

‘거, 너무하시네.’

그래도 마지막인데 얼굴 정도는 보러 와 주지.

혀끝에서 맴돌다 사라지는 한 마디.

임무를 받고 집무실을 떠나기 전 미리 작별 인사를 하긴 했지만, 섭섭한 감정이 드는 것은 어쩔 수 없다.

나 역시 헌터이며 무림인이기 전에 한 명의 사람이기에.

“……뭐, 금방 다시 보겠지.”

“그게 무슨 소리냐?”

“별것 아닙니다. 그냥 혼잣말이었어요.”

내가 아쉬운 마음을 뒤로하고 창밖에서 눈을 떼려던 바로 그때, 저 멀리서 자그마한 짐 마차 한 대가 덜컹거리며 다가오기 시작했다.

비단 하남이 아니어도 어디서나 볼 수 있는 광경이지만, 마부석에 변복(變服)으로 신분을 숨긴 절정 고수가 앉아 있다면 이야기가 달라진다.

‘송일섬.’

드디어 왔군.

호언장담대로 반 시진 안에 모든 준비를 끝마친 주화란이 은밀하게 하남을 빠져나갈 마차를 보낸 것이 틀림없다.

이미 아래층에서는 계단을 올라오는 혁무진의 인기척이 느껴지고 있었다.

‘슬슬 떠날 때인가?’

이 별채도 제법 익숙해졌는데, 이번 생에는 역마살이 제대로 낀 모양이다.

주위를 한 번 둘러본 나는 두 사람을 향해 인사를 건넸다.

“늦기 전에 이만 가 봐야겠네요. 여기까지 찾아와 줘서 감사합니다. 청 소협도.”

머뭇거리던 청풍이 줄곧 손에 들고 있던 봇짐을 불쑥 내밀었다.

“이거요, 은인.”

“이게 뭐야?”

“만두요. 하남에서 제일 맛있는 가게에서 샀어요. 먹고 싶었는데 은인 생각하면서 꾹 참았어요.”

문경이 조용히 덧붙였다.

“오는 길에 족히 다섯 개는 처먹었다. 꾹 참은 게 그 정도지.”

“앗, 아아앗…….”

이미 냄새로 알고는 있었지만, 그래도 감동은 감동이다. 설령 다섯 개를 빼먹었어도 그 감정은 달라지지 않는다.

“고마워. 잘 먹을게. 그럼 이만.”

피식 웃으며 봇짐을 받고 돌아선 그때, 귓가를 파고드는 한 줄기 전음(傳音)이 있었다.

- 그거 아느냐? 지금까지 내 가르침을 받은 놈들은 모두 죽었다.

“……!”

- 그러니 헛되이 죽지 말거라. 네놈이 남만에서 죽어 버리면, 내가 지금까지 참은 것이 아까워지니까.

참으로 살벌한 걱정이 아닐 수 없다. 그러나 중요한 것은, 손에 들린 만두처럼 그 마음이 확실히 전해졌다는 것이다.

우뚝 선 채로 작게 고개를 끄덕인 나는 곧장 걸음을 옮겼다.

저벅.

유난히도 크게 울려 퍼진, 힘찬 걸음이었다.
```

## Final English reading copy

```markdown
# Chapter 550

After everyone left, Hyuk Mujin busily disappeared to gather what we needed, leaving me alone. I quietly opened my mouth.

“Quest Window Open.”

*Ding.*

> **System**
>
> **Quest**
>
> **Journey to Nanman**
>
> Murim Alliance Leader Mae Jonghak has given the Fire Dragon Pavilion its first mission.
>
> You must now head to Nanman and proactively respond to any unforeseen circumstances.
>
> It is impossible to know what lies ahead for you and the Fire Dragon Pavilion.
>
> Always remain alert and act with a flexible mindset.
>
> **Grade:** Peak
>
> **Restriction:** Jin Taekyung and Fire Dragon Pavilion members
>
> **Mission:** Enter Nanman (Incomplete)
>
> **Reward:** Linked Quest
>
> ???
>
> **Failure:** Gain the Title **Can't Go to Nanman**
>
> **Fame** and **Trust** drop significantly.

The Journey to Nanman had been created when Mae Jonghak gave me the mission.

As I could tell from the description and mission fields, the System had not offered any particularly useful hints this time.

*There’s no time limit, either.*

That did not mean we had plenty of time. It meant we were entering a situation where we had no idea what might happen even a moment from now.

I let out a quiet sigh and closed the Quest Window.

*If nothing happens, that would be fortunate in its own way…*

But if something did happen, it could quickly spiral out of control. I would have to lead the Fire Dragon Pavilion, bring the situation under control as quickly as possible, and return safely.

I could barely make a living on my own, and now I had become responsible for other people. Just then, the two words *Pavilion Master* suddenly felt much heavier.

“Um…”

A voice abruptly slipped into my ear.

I turned around and saw Cheongpung standing in front of the half-destroyed door, staring blankly at me with a bundle in his arms.

“Benefactor, may I come in?”

“Anyone listening would think you always ask permission before coming in.”

When the door had been intact, he had barged in without even knocking. Seeing him stand there like that in front of the wreckage was almost too ridiculous.

I let out a quiet laugh and waved him inside.

“Just come in. I was planning to go see you anyway, so this works out.”

“I was going to come in whether you gave permission or not.”

The answer, of course, had not come from Cheongpung.

I looked at Mungyeong, who had appeared like a ghost, and muttered awkwardly,

“I was talking to Young Hero Cheongpung.”

“Like I said, I don’t need your permission.”

Mungyeong entered the annex without a care, then glanced at the cups on the table and the disordered chairs.

“Someone has been here. Six people in total, including you and Hyuk. One of them was a woman.”

“How did you know that?”

“You can tell if you look.”

At Mungyeong’s dry answer, Cheongpung added in his innocent tone,

“I saw the others leaving. I thought I should come when no one else was here.”

“…”

“…”

*What the fuck?*

At my deeply suspicious stare, Mungyeong opened his mouth again with an expression that seemed to ask what I intended to do about it.

“If you look, you know.”

“When you said ‘if you look,’ did you actually mean looking with your eyes?”

“You could tell without looking at something like this.”

“Don’t stare off at distant mountains. There are buildings everywhere, so you can’t see any mountains anyway.”

“Instead, I can see your future. If you say one more word, I have a feeling this room will be filled with the smell of blood.”

“…”

*Damn old man. And he still pretends to be a medical apprentice.*

I shuddered at the evil fake physician’s behavior and turned toward Cheongpung.

“So what brings you here?”

“I came to say goodbye.”

“What?”

Cheongpung scratched the back of his head and smiled.

“When you told me to go on ahead outside the Alliance Leader’s Hall earlier, I had a feeling you were about to leave soon. Hehe.”

Even though I had never told him directly, it seemed Cheongpung had guessed to some extent.

After hesitating briefly, I nodded readily.

“That’s right. It’s a mission.”

“Ah! Then where are you going?”

“Nanman.”

“Nan…man?”

Cheongpung’s eyes went wide at my answer. Mungyeong, who seemed to have been thinking about something, muttered quietly,

“If it’s Nanman, then the Nanman Beast Palace?”

“Yes.”

“That strange phenomenon. It must be because of the rift.”

“That’s right. If a second rift occurs, Dark Heaven would have a hard time finding a more suitable place than that.”

“It is certainly possible. Moreover, the distance from the Central Plains is great and the terrain is difficult. If the Nanman Beast Palace were to fall, the chaos would begin in Yunnan and spread like wildfire.”

I agreed with Mungyeong’s assessment.

If Dark Heaven really was plotting something in Nanman and its plan succeeded, the flames of war would not stop in Yunnan Province alone.

*It would spread to neighboring Guizhou and Guangxi—and even Sichuan, which suffered considerable damage in the last battle.*

Guizhou and Guangxi were particularly vulnerable.

The number of sects and martial artists in each province was smaller than in other regions, and their overall strength was weaker as well. The flames would unquestionably spread faster there.

“Going to Nanman in a situation like this. It will be a difficult journey.”

“It would be fortunate if nothing happens. If it does, though… we’ll have to stop it by any means necessary.”

“With only six people?”

“A whole six.”

“…”

“I heard a rumor that among them is a young, handsome Supreme Peak master who was taught by the Fire King and the Slaughter Saint. Have you ever heard of him?”

“I haven’t. Especially not the part about him being handsome.”

“Ah. Right.”

He cut that down with such precision.

Mungyeong had effortlessly blocked my nonsense, then continued while looking at Cheongpung.

“But I have heard another rumor. About a certain man obsessed with dumplings who has latched onto a young medical apprentice and is learning martial arts by watching him.”

“Huh?”

*What did I just hear?*

My thoughts must have shown clearly on my face. Mungyeong nodded when he saw my expression.

“That is probably exactly what you are thinking.”

“Really?”

“It is true.”

“Why would he pass up the almighty Sword Saint and go out of his way to learn from someone with such a foul temper—sorry. That came out wrong.”

At some point, Mungyeong had drawn a small sword from his sleeve. I deliberately avoided his chilling gaze and looked toward Cheongpung instead.

“If you’re being blackmailed, blink twice.”

“You little bastard…”

“Hehe. It’s all true, Benefactor.”

I stared at Cheongpung for a moment, then shrugged.

“I know. I was just making a joke.”

I did not need to hear the answer to know why he had sought out Mungyeong, or what he wanted to gain from him.

*To become stronger. To change himself to fit this world.*

It had been more than a year since we first met.

I had been heading toward an inn when a ragged young man suddenly approached me and asked for a single piece of sweetmeat.

Despite Hyuk Mujin’s protests, I gave him all my sweetmeats. That was how my connection with Cheongpung began.

*We’ve both changed a lot. Me and him.*

The Third Young Master of the Jin Family of Taiyuan, once called the family’s disgrace, had become a Supreme Peak master who shook the Murim.

And the young genius who loved martial arts and delighted in every large and small experience the world offered had, at some point, developed a firm core within himself.

The change could not be seen, but it could be felt.

Only a very small number of people close to Cheongpung, myself included, knew about the transformation that others could not perceive.

*Tap.*

I suddenly reached out and patted Cheongpung on the shoulder. His eyes went round.

“Benefactor?”

“Nothing. Just telling you to hang in there.”

Cheongpung stared at me, then his eyes curved into crescents.

“Yes. You too, Benefactor.”

“Of course I need to try harder. At least Young Hero Cheongpung has something reliable to lean on. I don’t even have a hill to lean against over here.”

Mungyeong had been silently watching our exchange when he suddenly spoke.

“Come to think of it, I don’t see that hill.”

“That hill is staying in Henan. Only the rest of us are leaving.”

“Well, now I’ve seen everything. To think the Fire King would make such a decision.”

“It’s embarrassing to say it, but let’s call it the greater good. We need more hands in the current situation.”

Even as I answered, a hollow feeling remained in one corner of my heart.

Perhaps it was because this was the first time since meeting Jeok Cheongang that I would be moving separately from him.

Even when Jeok Cheongang had been unconscious for a long time, we had always been together.

*But now it’s time for me to stand on my own.*

Jeok Cheongang’s protection had been vast and generous, but I had grown too quickly to remain there forever.

And the turbulent situation would not allow the two of us to keep traveling together.

*Could it be…?*

At one thought that suddenly crossed my mind, I turned slightly and looked out the window.

But every face passing along the main road was unfamiliar and indistinct.

The person I was waiting for never appeared.

*Come on. That’s a little harsh.*

Still, this was the last chance before I left. Couldn’t he at least come see me?

The words lingered at the tip of my tongue before vanishing.

I had said goodbye in advance before leaving the office after receiving the mission, but I could not help feeling disappointed.

Before I was a Hunter or a martial artist, I was still a person.

“…I’ll see them again soon, anyway.”

“What does that mean?”

“It’s nothing. I was just talking to myself.”

Just as I was about to turn my eyes away from the window and leave my disappointment behind, a small baggage cart began rattling toward us in the distance.

It was a sight one could see anywhere, not just in Henan. But the situation changed when a Peak master with his identity concealed beneath a disguise was sitting on the driver’s bench.

*Song Ilseom.*

He had finally arrived.

Ju Hwaran must have finished all the preparations within half a shichen, just as she had boasted, and sent a carriage that could leave Henan discreetly.

I could already sense Hyuk Mujin coming up the stairs from downstairs.

*Is it about time to leave?*

I had grown fairly familiar with this annex. But I seemed to have been saddled with a wandering fate in this life.

I looked around once, then spoke to the two of them.

“I should get going before it gets any later. Thank you for coming all the way here. You too, Young Hero Cheongpung.”

Cheongpung hesitated, then suddenly held out the bundle he had been carrying the entire time.

“This, Benefactor.”

“What is it?”

“Dumplings. I bought them from the best shop in Henan. I wanted to eat them, but I held back while thinking of you, Benefactor.”

Mungyeong quietly added,

“He stuffed down a good five on the way here. That’s what ‘holding back’ amounted to.”

“Ah, aah…”

I had already known from the smell, but I was still touched. Even if he had eaten five of them, that feeling did not change.

“Thanks. I’ll enjoy them. Then I’ll be going.”

I let out a quiet laugh, accepted the bundle, and turned around.

That was when a single strand of Sound Transmission slipped into my ear.

—Do you know? Everyone who has received my teachings up to now has died.

“…!”

—So don’t die a pointless death. If you die in Nanman, all that I’ve put up with until now will have been for nothing.

It was a terrifying way to worry about someone. But the important thing was that, just like the dumplings in my hands, his feelings had come through unmistakably.

I stood there and gave a small nod before immediately setting off.

*Step.*

It was a powerful stride that echoed unusually loudly.
```

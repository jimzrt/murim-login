<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0548.txt",
      "sha256": "432e4e988f0ea235950a004787333e13b76cc7297e42ef71d70cd95762c13562",
      "bytes": 16740
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "afb3592ea292804dab1276f681f8a7975c41dc861c7bd6fb74a306288f31adf0",
      "bytes": 4412
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "fb02223d0849c4a4274033dfcb37dd0b666a24e95e84955f5d4494b10d58c755",
      "bytes": 173659
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "1e8d904b0a360dea00af7b0b153a7e895a9f2f31435452e977f2e2e9f7db92c9",
      "bytes": 1371
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "aabfc424de711d37b3f06c9705206a07df9f0c874befaf402a000f9b1328bfa9",
      "bytes": 1147
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "bc8a6231f92e7fa8d2736bb0ca72344715096f6e239b82bffb90a847409e4dab",
      "bytes": 1702
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "cae89126f4b9d8b5c4c7c589d761856c04b4e52759dbabd26f3b6d33f5f865bc",
      "bytes": 2252
    },
    {
      "path": "characters/Jin Wikyung.md",
      "sha256": "b9857362115f934e350d30c6f5d8fcaac4062b559578efde6bd7d9a23acd8381",
      "bytes": 1210
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "5a249a1ebabd2d628cf3c1fd3d21cd3076994bb7a4f00b23079bd1c0b0861d57",
      "bytes": 622
    },
    {
      "path": "characters/Mae Jonghak.md",
      "sha256": "11576eff75207393a441f08b31a4ab1ce044f5a7792c4bf765e0c05024214a26",
      "bytes": 985
    },
    {
      "path": "characters/Song Ho.md",
      "sha256": "22cd4224bcb242ef77474bb14db62b84e74a7c7df1fa27a3d6f6e8e19267cfd0",
      "bytes": 767
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "b7a67fa9b0452b13c1b873eae2aa39730a966ba9a88586b4f7fb1a2f3902dd88",
      "bytes": 165679
    }
  ],
  "estimated_tokens": 15699
}
-->

# Durable State Update — Chapter 548

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 548. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 548. Profile updates may replace only one
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
  "chapter": 548,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 548,
    "continuity_sources": [548],
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
    "The Mount Song Resolution formally restored the Murim Alliance; Mae Jonghak is its Alliance Leader, Jeok Cheongang heads the Five Kings Hall, and Murong Yeonghwi remains in Liaoning overseeing Murong Family defenses.",
    "The Two Dragons Pavilion remains the overall organization but is divided into Jin Taekyung's Fire Dragon Pavilion and Cheongpung's Azure Dragon Pavilion; both pavilion masters have largely honorary authority.",
    "Jin Taekyung is a Supreme Peak master with Three Flowers Gather at the Crown, advanced qi perception, exceptional resistance to monster Fear, and public S-rank-level recognition despite retaining an A-rank license; he now awaits the Fire Dragon Pavilion's first mission.",
    "Cheongpung created Mimi Step, is recognized by Mungyeong as having Grandmaster potential, cares for Mimi, and is master of the Azure Dragon Pavilion.",
    "Mungyeong ended Taekyung's direct training, assigned him a final task of incorporating martial principles into his learned martial arts, and accepted Cheongpung's offer to accompany him.",
    "Zhuge Feng's Demon-Sealing Formation still blocks all mana from the exposed Gate, while Jang Taebo is summoning artisans to process the Water God Dragon's remains.",
    "The Southern Heaven Demon Empress is traveling toward Yunnan and expects to cause further deaths.",
    "The Black Dragon Demon Gate remains a major unorthodox power; Sama Pyo is its Young Sect Leader and Black Dragon Saber, and Taishan is his giant subordinate.",
    "Jang Sam, a Hubei fisherman missing for a month, reappeared as a mutant Killing Ghost with a horn and four arms; the mechanism behind his transformation and his ability to absorb human energy remain unresolved.",
    "Hwangbo Gun is the Hwangbo Family Head and an Outer Hall Squad Leader of the Murim Alliance, formally beneath Taekyung's Fire Dragon Pavilion Master position.",
    "Taekyung has warned the Alliance that Dark Heaven is an enormous monster-like threat rather than an ordinary demonic-martial-arts enemy and that the current lull must be used for immediate counterattack and preparation.",
    "Jeok Cheongang declares that Taekyung has never been wrong, and Mae Jonghak orders Taekyung summoned for the Fire Dragon Pavilion's first mission."
  ],
  "continuity_sources": [
    547,
    546
  ],
  "open_questions": [
    "What is the Lord of Heaven's identity, how is he connected to the dangerous force Taekyung associates with his original world, and how can Dark Heaven open Gates?",
    "Where is the Southern Heaven Demon Empress ultimately headed, and what does she intend to do in Yunnan?",
    "What is the outcome of the duel between Jeok Cheongang and Nangong Cheon, the Azure Sky Sword King?",
    "Why did Ju Hwaran and Sama Pyo's political engagement end?",
    "What process created Jang Sam's mutant form, and can Dark Heaven's mutants absorb human energy?"
  ],
  "safe_through": 547,
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
| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 매종학    | **Mae Jonghak**    |
| 청풍     | **Cheongpung**     |
| 무림맹    | **Murim Alliance**               |
| 암천     | **Dark Heaven**                  |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 신법     | **movement technique**                           |                                                       |
| 마적     | **mounted bandits**                              |                                                       |
| 은인     | **Benefactor**                               |
| 몬스터     | **monster**           |
| 노부      | **this old man / I**                                            |
| 공자      | **Young Master**                                                |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 송호 | **Song Ho** | Elderly martial artist known as the Thousand-Faced Fox. |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 화염신장 | **Flame Divine Palm** | Jopil's deadly palm technique, noted when Taekyung compares Jopil with Mukyung. |
| 기감 | **Qi Sense** | Taekyung's sensory technique; its range reaches seventy meters in this chapter. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 화주 | **strong liquor** | Liquor stored and consumed by the dark-path swordsmen. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 천면호리 | **Thousand-Faced Fox** | Epithet of Song Ho. |
| 은영각 | **Hidden Shadow Pavilion** | Former Murim Alliance intelligence organization. |
| 은영각주 | **Chief of the Hidden Shadow Pavilion** | Office formerly held by Song Ho. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 준이 | **Jun** | Family nickname used in the form Jun's dad. |
| 호북 | **Hubei** | Province on Ju Gongsan's route from Guangdong to Henan. |
| 성도 | **Chengdu** | Sichuan destination of Taekyung's party. |
| 외당 | **Outer Hall** | The Tang Clan's outer hall area. |
| 괴력난신 | **supernatural powers** | Term for extraordinary and unnatural powers. |
| 이무기 | **imugi** | Legendary serpent mentioned as the only comparable creature to a Thousand-Year Poison Horned Snake. |
| 호북성 | **Hubei Province** | Province where the chapter’s Dark Heaven incidents occurred. |
| 수신룡 | **Water God Dragon** | Legendary name for the true master of Dongting Lake; distinct from the modern Sea Serpent. |
| 남천마후 | **Southern Heaven Demon Empress** | Title Honglan uses when revealing her identity. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 식경 | **half an hour** | Time limit given for the requested reports. |
| 맹주전 | **Alliance Leader's Hall** | Hall directly associated with the Murim Alliance Leader. |
| 천하제일검 | **Number One Sword Under Heaven** | Mae Jonghak's title. |
| 화룡각 | **Fire Dragon Pavilion** | New name chosen for Taekyung's pavilion. |
| 화룡각주 | **Fire Dragon Pavilion Master** | Unique Title awarded to Jin Taekyung. |

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
| 매종학 | 청풍 | grandfather_to_grandson | Pung | affectionate-instructional | Mae Jonghak calls young Cheongpung 풍아 while teaching him the Crouching Tiger Fist. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 적천강 | 청풍 | overwhelming_elder_to_young_martial_artist | you / little punk | blunt, amused, and threatening | Jeok Cheongang uses 네, 이놈, and related blunt forms while testing Cheongpung. |
| 청풍 | 적천강 | young_martial_artist_to_overwhelming_elder | Grandpa Jeok | casual-familiar despite deference | Cheongpung uses 적 할아버지 while asking Jeok Cheongang to confirm Taekyung's condition; this is a familial form of address, not literal kinship. |
| 혁무진 | 적천강 | subordinate_to_overwhelming_elder | Great Hero Jeok | deferential and fearful | Mujin uses 적 대협 while reporting Jeok’s orders and Taekyung’s awakening. |
| 적천강 | 혁무진 | overwhelming_elder_to_junior_martial_artist | you stupid fool | blunt and mocking | Jeok calls Mujin a 멍청한 놈 after knocking him down during the attempted escape. |
| 무인 | 진위경 | vassal_martial_artist_to_lesser_family_head | Lesser Family Head | formal-deferential | The Mount Heng martial artists greet Jin Wikyung as 소가주님 while pledging loyalty. |
| 진위경 | 적천강 | host_to_legendary_guest | Great Hero Jeok | formal-deferential | Introduces himself and pays respects to Jeok Cheongang as the Fire King. |
| 적천강 | 진위경 | elder_to_younger_family_head | you | gruff and teasing | Uses 자네 while mistaking Wikyung for Taekyung’s father and questioning his age. |
| 송호 | 청년 | elderly_martial_artist_to_younger_martial_artist | Young Hero | formal-polite | Song Ho calls out to the young man as 소협 at the chapter's end. |
| 송호 | 진태경 | senior_martial_artist_to_junior_martial_artist | you | familiar-polite | Uses 자네 while recognizing Taekyung and discussing his preliminary performance. |
| 매종학 | 송호 | savior_to_survivor | you | casual-familiar | Mae uses 자네 while speaking to Song Ho after his identity is recognized. |
| 송호 | 매종학 | rescued_survivor_to_savior | Great Hero; you | formal-deferential and familiar | Song Ho credits Mae with saving his life and addresses him as 대협. |
| 매종학 | 진태경 | older_ally_to_younger_friend | friend | casual-familiar | Mae Jonghak uses 친구 when arriving at Taekyung's window and asking to talk. |
| 진위경 | 막내 | older brother to younger brother | my youngest | intimate and informal | Jin Wikyung uses 막내야 affectionately for Jin Taekyung. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 진태경 | 수신룡 | hostile martial artist to monster | you, sibu-leol eel bastard | blunt, insulting, and fearless | Taekyung directly insults the emerged Water God Dragon before attacking it. |
| 적천강 | 수신룡 | legendary_martial_master_to_dying_spirit_beast | you | wary and trembling | Jeok asks what the Water God Dragon is after witnessing its mental communication. |
| 남천마후 | 진태경 | hostile_supernatural_opponent_to_young_martial_artist | Young Great Hero / Child | lighthearted and taunting | Addresses Taekyung while refusing to explain the Gate. |
| 진태경 | 남천마후 | young_martial_artist_to_hostile_demon_empress | you | hostile and determined | Promises that the Southern Heaven Demon Empress will die when they meet again. |
| 적천강 | 남천마후 | legendary_martial_master_to_hostile_demon_empress | you bitch | blunt and threatening | Threatens to punish her and Lord of Heaven. |
| 남천마후 | 적천강 | hostile_demon_empress_to_legendary_martial_master | Fire King Jeok / you | flattering and mocking | Addresses Jeok Cheongang as the Fire King while praising Lord of Heaven. |
| 진위경 | 남천마후 | family_head_to_hostile_demon_empress | you | formal and defiant | Swears that she cannot touch Taekyung. |
| 매종학 | 적천강 | long-standing martial rival and friend | Great Hero Jeok | casual and familiar | Mae addresses Jeok as 적 대협 while discussing the Alliance Leader position. |
| 적천강 | 매종학 | long-standing martial rival and friend | you | blunt and familiar | Jeok addresses Mae as 당신 while recalling their meeting at Mount Jiuhua. |
| 천면호리 | 매종학 | intelligence_chief_to_alliance_leader | Alliance Leader | formal and deferential | Requests that Mae move elsewhere with the others before he reports further. |
| 진위경 | 청풍 | Jin Family Lesser Family Head to young martial companion | Young Hero Cheongpung | formal-polite | Uses 청 소협 while summoning Cheongpung to the Alliance Leader's Hall. |
| 청풍 | 매종학 | grandson to grandfather | Grandpa | casual-familiar | Repeatedly calls Mae Jonghak 할아버지 while mistaking the Alliance Leader's summons as a family visit. |
| 진태경 | 매종학 | younger ally to newly installed Alliance Leader | Alliance Leader | formal and deferential | Uses 맹주님 while formally greeting Mae Jonghak as the Alliance Leader. |
| 송호 | 적천강 | Hidden Shadow Pavilion Chief to legendary senior master | Great Hero Jeok | formal-deferential | Song Ho addresses Jeok while questioning the basis for his confidence in Taekyung. |
| 적천강 | 송호 | senior martial master to allied intelligence chief | you | blunt but reassuring | Jeok directly tells Song Ho to believe Taekyung. |

## Listed compact profiles

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 547
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, the grandson and Disciple of Sword Saint Mae Jonghak, a Supreme Peak martial master known as the Huashan Divine Dragon, the creator of the snake-inspired Mimi Step footwork technique, and the master of the Azure Dragon Pavilion within the Alliance Leader's Two Dragons Pavilion.
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, a deep love of martial arts, competitive pride, unusual resistance to monster-induced Fear, and discomfort when someone copies his martial arts.
- **Voice:** Dreamy and hazy, with innocent, polite phrasing; he has begun imitating Taekyung's profanity.
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions while Taekyung is his only true martial rival; Tang Sadok has temporarily entrusted Mimi, now a large horned snake, to him, Mungyeong recently examined her condition, and Mungyeong accepted Cheongpung's offer to accompany him after Cheongpung pledged to learn by observation rather than formal instruction.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 545
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and a member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 547
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm, and the occupant of the chief seat of the Murim Alliance's Five Kings Hall.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 547
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, a Supreme Peak master who possesses the Heavenly Martial Physique and superhuman physical strength, has manifested Force, opened his Middle Dantian, crossed the wall into true mastery, has achieved Three Flowers Gather at the Crown but not Five Qi Returning to Origin, can perceive the texture of qi well enough to sever layered magic, can resist high-level monster Fear through exceptional mental strength, is publicly recognized as an S-rank-level Hunter while formally retaining an A-rank license pending testing, can command coordinated raids against powerful monsters, and now serves as one of the two pavilion masters of the Alliance Leader's direct Fire Dragon Pavilion while holding its unique Title, Fire Dragon Pavilion Master.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor and assigned him a final task to incorporate martial principles into his learned martial arts but declined Taekyung's recruitment after Cheongpung reached him first, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate, student, and trusted manager of media and official arrangements, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, and Xiao Shen regards him as an older brother after Jin saved him.

### Jin Wikyung.md

# Jin Wikyung (진위경)

- **Safe through:** Chapter 547
- **Aliases:** Junzi Sword
- **Role:** Jin Wikyung is the thirty-six-year-old Lesser Family Head and future Family Head of the Jin Family of Taiyuan, the Alliance Leader who unified Shanxi Murim and Shanxi Province's foremost landowner and magnate.
- **Personality:** Calm, authoritative, and politically capable in public; protective and affectionate toward Taekyung beneath a stern mask. Takes responsibility for his people, acts decisively under pressure, and prioritizes family survival.
- **Voice:** Restrained, formal, and commanding with subordinates; openly affectionate, proud, and occasionally exuberant with Taekyung.
- **Relationships:** Jin Wikyung is Taekyung's eldest brother and future Family Head who protects and mentors him, commands Wipeng and the Jin Family's forces, has worked with Jeok Cheongang, and maintains a political connection with Hongcheon, Prince Shangshan's hidden loyal retainer; Jin Mukyung is his younger brother and a potential successor alongside Taekyung.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 547
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Mae Jonghak.md

# Mae Jonghak (매종학)

- **Safe through:** Chapter 547
- **Aliases:** Sword Saint
- **Role:** Sword Saint and Cheongpung's grandfather who now serves as the New Murim Alliance's Alliance Leader.
- **Personality:** Playful, easygoing, and teasing, but capable of handling heavy administrative responsibilities efficiently.
- **Voice:** Friendly, casually familiar, and cheerfully teasing, including when greeting old acquaintances and discussing leadership.
- **Relationships:** Cheongpung's grandfather and martial instructor; taught him the Taeeul Miri Palm; secretly entered Huashan while its Sect Leader slept, left a dagger and handwritten note, and then went into hiding, prompting Huashan's search; fought Jeok Cheongang at Mount Jiuhua more than forty years ago and left after their draw; his old friend Hong Dao left him a letter identifying Jin Taekyung as the Morning Star who would drive away darkness.

### Song Ho.md

# Song Ho (송호)

- **Safe through:** Chapter 547
- **Aliases:** Thousand-Faced Fox
- **Role:** Elderly Peak master known as the Thousand-Faced Fox, a martial artist with a prosthetic leg, and current Chief of the Hidden Shadow Pavilion, overseeing a vetted intelligence network that includes highly trained assassins.
- **Personality:** Outwardly genial and relaxed, but observant, forceful, and intimidating when pursuing information.
- **Voice:** Lightly genial and conversational, turning quietly coercive during interrogation.
- **Relationships:** He serves under Mae Jonghak's New Murim Alliance, commands the Hidden Shadow Pavilion, and recognizes Jin Taekyung as Jeok Cheongang's Disciple.

## Korean source

```text
＃548화



“잘했다.”

대회의실을 나서자마자 진위경이 건넨 말에, 나는 피식 웃는 것으로 대답을 대신했다.

“왜 그러느냐?”

“글쎄요. 말하는 내용과 다르게 표정이 좋지 않아서?”

“아.”

그제야 딱딱하게 굳어 있던 얼굴이 풀린다. 하지만 진위경의 입가에 맺힌 웃음은 금방 꺼질 듯이 흐릿했다.

“사실 네 말을 어찌 받아들여야 할지 모르겠구나. 그만큼 오늘의 너는…….”

“괜찮습니다. 사실 이런 반응이 당연한 거예요.”

말꼬리를 흐리는 진위경을, 나는 이해했다. 그가 지금 어떤 심정인지 알 것 같았기 때문이다.

‘같은 상황이었다면 나도 마찬가지였겠지.’

이 세상에서 죽음이라는 단어는 생각만큼 무겁지 않다.

현대의 살인 사건은 드물며 TV를 포함한 대중 매체로 알려지지만, 이곳에서는 빈번하게 목격되기 때문이다.

치안이 좋은 도시라면 그나마 낫다. 그러나 그 밖의 양민들은 위치에 따라 산적이나 마적의 위협 속에서 살아가야 한다.

무림인은 말할 것도 없다.

‘칼끝을 걷는 삶.’

오죽하면 도산검림(刀山劍林)이라 하겠나.

그렇기에 그들은 늘 죽음을 각오한다. 투지를 불태우고 무공을 단련한다. 그리고 눈앞의 진위경 역시 한 사람의 무림인이었다.

문제는, 그를 포함한 모두가 자라난 환경이다.

무림에서는 죽이는 것도, 죽는 것도 사람이었다. 맹수와 영물(靈物)이 있었지만, 적어도 그것들의 정체는 듣도 보도 못한 괴물이 아니었다.

하지만 오늘 나는…… 그 괴물들이 이 세상을 뒤덮을 것이라는 주장을 피력했다.

사람과 괴물이 죽고 죽이는 싸움이 시작되리라 예견했다.

‘내가 했던 말이 얼마나 와닿았는지는 모르겠지만, 그래도 위기감은 충분히 느꼈겠지.’

내 이야기가 이어질수록 누군가는 불신 어린 시선을 보냈고 누군가는 혼란스러워하면서도 깊은 생각에 잠겼다.

당장 모두가 믿지는 않더라도, 귀 기울여 들었다는 것만으로도 소기의 목적은 달성했다고 생각한다.

‘그나마 상대가 무림인들이고, 확실한 물증이 있어서 이 정도라도 먹힌 거지.’

늙은 선비들이 청중이었다면 공자후 아크바르를 외치며 괴력난신 반대 시위를 벌였겠지만, 대회의실에 모인 이들은 그렇게까지 앞뒤가 꽉 막힌 족속들이 아니었다.

최소한 자신들의 눈앞에 팔 네 개 달린 괴물의 시체가 놓여 있는 상황에서는 그랬다.

‘수신룡의 사체도 마찬가지고.’

부위별로 분리 한 수신룡의 사체는 아직 극비리에 운송 중이다.

하지만 내 인벤토리에는 만일을 대비하여 슬쩍 해 두었던 부산물 일부가 있었고, 그것은 중요한 물증이 되기에 충분했다.

“그러고 보니 막내야. 그건 어디서 난 것이냐? 분명 빠지는 것 없이 챙긴 것으로 아는데.”

“예?”

“그 왜. 호북에서 쓰러트린 이무기의…….”

“콜록, 콜록. 콜로로록!”

억지로 쥐어 짜낸 기침을 토해 내자, 옆에서 대화를 듣고 있던 청풍이 품 안을 뒤적거렸다.

“은인. 당과 드릴까요? 기침에는 당과가 최고예요.”

“……싫어. 최악이야.”

“네에.”

도대체 언제부터 당과가 기적의 신약이 됐냐.

단호한 실험 거부에 매드 사이언티스트 청풍이 시무룩한 얼굴로 당과를 제 입에 문다. 그 모습을 지켜보던 진위경이 피식 실소를 흘렸다.

“알겠다. 더 묻지 않으마.”

“음. 그럼 감사하고요.”

머쓱하게 턱을 긁적이는 나를, 한동안 물끄러미 응시하던 진위경이 불쑥 입을 열었다.

“문득 그런 생각이 들고는 한다. 네가, 우리 막내가 내가 알던 그 아이가 맞는지.”

“……!”

“구태여 묻지 않겠다. 더 이상의 의문도 품지 않으마. 다만 지금껏 네게 말하지 못한 한 가지 바람은 있다.”

진위경의 부드러운 목소리가 이어졌다.

“언젠가 이 모든 것이 마무리되고 적절한 때가 오면, 네가 미처 말하지 못한 이야기들을 듣고 싶구나.”

말하지 못한 이야기라. 나는 마음속으로 뇌까렸다.

‘언제쯤 그때가 올까.’

하지만 정말 진위경의 말대로 이 모든 것들이 마무리된다면. 그리고 마음의 준비가 끝난다면…… 누구에게도 말할 수 없었던 나만의 비밀을 직접 말할지도 모르겠다.

그런 날이 올지도 모르겠다.

“……알겠습니다.”

그리고 내가 씁쓸하게 웃으며 고개를 끄덕인, 바로 그 순간이었다.

“여기 있었군. 화룡각주.”

또각.

늙수그레한 목소리와 함께 둔탁한 소음이 울려 퍼진다. 고개를 돌리자 그곳에는 무림맹 은영각주, 천면호리 송호가 있었다.

“회의는 이미 한 식경 전에 끝났을 터인데. 아직도 여기에 남아 있다니. 우연인가?”

그의 물음에 내가 고개를 저었다. 지금까지 무림맹에 남아 있던 것은, 비단 진위경과의 대화를 위해서만이 아니다.

“필연일 겁니다.”

“필연이라. 그래, 그렇군.”

도무지 속을 짐작할 수 없는 노회한 눈동자에 묘한 빛이 스친다. 짧은 침묵 끝에 천면호리가 입을 열었다.

“따라오게, 화룡각주. 무슨 일인지는 이미 알고 있겠지?”

안다. 누가 나를 보고자 하는지도. 어떤 이유에서인지도.

그리고 이어지는 천면호리의 한마디는 짐작을 확신으로 바꿔 주었다.

“맹주께서 찾으시네.”



* * *



탁.

등 뒤에서 문이 닫히는 소리가 유난히도 크게 울렸다. 맹주전 내부에 마련된 집무실에는 이미 두 사람이 나를 기다리고 있었다.

“왔느냐?”

덤덤한 적천강의 물음에 이어 무림 맹주 매종학이 손짓했다.

“자리에 앉게. 그리고 자네들은 잠시 나가 있고.”

나나, 내 뒤를 따라 곧장 집무실로 들어온 천면호리에게 하는 말이 아니다. 모습을 드러내지 않은 또 다른 이들에게 건네는 말이었다.

스윽.

매종학의 말이 끝나기 무섭게 유령처럼 사라지는 기척들.

항상 그의 주위를 지킨다는 비밀 호위들마저 자리를 비키자, 나는 비어 있는 의자에 앉으며 입을 열었다.

“수준이 엄청나네요. 기척이 거의 느껴지지 않던데요.”

“이 방에 출입하는 대다수는 그마저도 모르지. 그걸 알아챈 자네가 대단한 거야.”

“모르더라도 짐작은 하지 않을까요? 무림 맹주씩이나 되는 분께 호위 하나 없는 것도 이상하잖습니까.”

“아. 그것도 그렇군.”

또래의 청년처럼 턱을 긁적인 매종학이 문득 나를 바라본다. 맑고 깊은 눈동자에 내 얼굴이 비쳤다.

“먼저, 자네가 대회의실에서 한 말들은 인상 깊게 들었네.”

“그러셨다니 다행입니다. 다른 분들은 어떨지 모르겠네요.”

“전부 믿지는 않더라도, 경시하지는 못할 걸세. 내 약속하지.”

가볍게 건네는 말도 누구의 입에서 흘러나왔느냐에 따라 달라진다.

그리고 그 대상이 무림맹의 맹주라면, 막강한 무게감이 실리는 것은 당연지사였다.

‘내 주장에 한층 힘이 더해지겠군.’

나쁘지 않은 흐름이다. 자연스럽게 내 얼굴이 살짝 풀리자 매종학이 빙긋 웃었다.

“걱정했던 모양이군.”

“아니라고 하면 거짓말이죠.”

“말이 나왔으니 묻겠는데, 자네는 스스로의 주장을 얼마나 확신하고 있나?”

“오 할. 반반입니다.”

내 대답에 천면호리의 얼굴이 딱딱하게 굳었다.

“지금…… 오 할이라고 했나?”

“예. 생각하신 것보다 너무 적어서 그러십니까?”

“빌어먹을. 그 반대지. 천하가 괴물로 뒤덮일 확률이 절반이나 된다는 소리 아닌가!”

천면호리의 탄식에는 짧은 욕설이 포함되어 있었지만, 지금만큼은 아무도 신경 쓰지 않았다.

나 역시 기분이 나쁘기는커녕 안도감이 들었다.

반응을 보니 최소한 이 자리에 모인 이들만큼은 내 주장을 이미 기정사실로 받아들였다는 것을 알았기 때문이었다.

“오 할이나 되는 근거는?”

평정심을 잃지 않은 매종학의 물음에, 나는 망설임 없이 정해진 대답을 내놓았다.

“제가 지금까지 암천을 상대하며 보고 느낀 전부입니다.”

그때, 말없이 차 대신 독한 화주를 홀짝거리던 적천강이 불쑥 입을 열었다.

“네놈의 판단이 틀렸을 수도 있다.”

“평생 욕 오지게 먹어도 좋으니까, 제발 그랬으면 좋겠습니다.”

진심이다. 차라리 내 예측이 완전히 빗나가서 사실 암천이 별것 아닌 놈들이고, 변이 몬스터 같은 놈들도 나타나지 않았으면 좋겠다.

나 한 사람 욕먹는 정도로 해피엔딩을 볼 수 있다면 남는 장사니까.

그러나…….

“미친 얘기 같지만, 전부 사실이에요.”

“염병할. 미치겠군.”

“그 정도로 안 믿기십니까?”

“믿기 싫다. 네 녀석이 하는 말이 아니었다면 그랬을 게다.”

“……!”

갑자기 치고 들어오는 감동 뭐야. 어쩔 거야, 이거.

탁.

그러나 감동이고 나발이고. 술병을 거칠게 내려놓은 적천강이 나를 노려보았다.

“차라리 거짓말이라고 말해라. 지금이라도 이실직고한다면 화염신장 세 대 정도로 끝내줄 테니.”

“이 자리에서 제 불알을 걸고 맹세컨대. 그냥 하는 소리가 아닙니다. 그리고 화염신장 세 대 맞으면 저 죽어요.”

“후우.”

깊은 한숨을 내쉰 적천강이 매종학과 천면호리를 향해 입술을 뗐다.

“노부도 믿기 싫지만…… 저놈이 하는 말이 전부 사실인 모양이오. 최소한 자기 불알을 걸 때만큼은 진심이거든.”

“…….”

진위 여부를 정하는 기준이 좀 이상하긴 한데, 어쨌든 내 진심이 제대로 전해지긴 한 모양이다.

그리고 우려가 현실로 나타남과 동시에 집무실에 내려앉은 침묵은, 잠시 후 들려온 매종학의 한 마디에 의해 깨져 나갔다.

“한 가지만 더 묻겠네.”

“두 개 물어보셔도 되는데요.”

“아니, 하나면 충분해.”

스윽.

매종학이 말과 함께 손가락을 까딱였다.

동시에 그의 등 뒤, 가득 쌓여 있는 죽간들 사이에서 커다란 두루마리가 날아와 우리가 앉아 있는 탁자 위로 펼쳐졌다.

촤르륵.

두루마리에 적혀 있는, 아니 그려져 있는 것을 확인한 내가 중얼거렸다.

“이건…….”

“보는 그대로일세. 천하의 전도(全圖)지.”

매종학의 말처럼 그건 천하 곳곳의 지리와 지형, 거기에 더해 지명을 표기한 지도였다.

하지만 내가 지금껏 무림에서 봤던 어느 지도보다도 크고, 특별한 차이가 있었다.

“각 문파의 위치까지 표시되어 있군요.”

“무림맹을 위해 만들어진 것이니까. 그럼 묻건대…….”

매종학의 덤덤한 목소리가 귓가를 파고들었다.

“자네는, 암천의 다음 목표가 어디라고 생각하나?”

“확신할 수 없습니다.”

“천하의 그 누가 미래를 확신할 수 있겠나. 단순한 짐작으로도 충분하네.”

단순한 짐작이라…….

말없이 생각에 잠겨 있던 나는, 불현듯 손을 들어 지도의 한 부분을 짚었다.

쿡.

“이곳입니다.”

반응은 즉각적이었다.

적천강은 작게 욕설을 중얼거렸고, 천면호리의 눈동자에는 기광이 번뜩였으며, 매종학은 나를 향해 상체를 기울였다.

“그곳을 택한 이유는?”

“만약 호북에서 벌어진 일이 반복된다면, 암천의 입장에서는 이곳만큼 적격인 곳을 찾기 힘들 겁니다.”

“바로 그 ‘균열’을 말하는 게로군.”

“예.”

“자네는 균열이 다시 한번 일어나리라 확신, 아니 짐작하고 있나?”

“가능성은 차고 넘친다고 생각합니다. 그 일은 천재지변이 아니라, 암천이 계획하고 벌인 일이었으니까요.”

최초는, 두 번째가 있기에 만들어진 수식어.

수신룡의 기억을 잠시나마 엿본 것은 오직 나 한 사람에게만 허락된 일이었다.

그렇기에 자신 있게 제시할 물증도, 확신도 없었지만 암천이 ‘그곳’을 노릴 확률은 농후했다.

나는 침착하게 말을 이었다.

“당장 암천이 무슨 일을 벌일지는 저도 모릅니다. 바로 다음 목표가 이곳이 아닐 수도 있죠. 하지만 적어도 한 사람만큼은, 이미 그곳을 향해 움직였을 겁니다.”

“남천마후(南天魔后).”

매종학의 입술 사이를 비집고 흘러나온 한 사람의 별호를 듣는 순간, 호북에서 목격한 수많은 시신이 눈앞을 스쳐 지나간다.

나도 모르게 주먹에 힘이 들어갔다.

“맞습니다. 남천마후라면…… 반드시 그곳을 염두에 두고 있을 겁니다.”

“이번에도 단순한 짐작인가?”

“짐작입니다. 확신에 가까운.”

확신할 수 있는 것은 없다. 다만 얼마 전부터 뇌리를 떠나지 않던 한가지 생각이, 상당한 가능성을 품고 있다고 생각했을 뿐이다.

그리고 조용히 고개를 끄덕인 매종학이 한 사람에게 시선을 던졌다.

“어찌 생각하나? 은영각주.”

“화룡각주의 의견에 속하도 한 몫 거들지요.”

즉각 대답한 천면호리 송호가 말을 이었다.

“이미 전서를 보낸 지 칠 주야가 넘었습니다. 답신이 도착하지 않는 것을 보니, 이미 문제가 생겼을 가능성이 적지 않습니다.”

“이미 예상은 했지만…… 빠르군.”

“예. 미리 선별해 둔 외당(外堂)의 병력을 이동시킬 수도 있겠지만, 자칫하면 늦을 가능성도 있겠지요.”

전서? 미리 선별해 둔 병력?

내 표정에 담긴 의문을 읽은 천면호리가 덤덤한 표정으로 입을 열었다.

“은영각의 눈과 귀는 천하 곳곳에 흩뿌려져 있다네. 이와 같은 짐작을 한 것은 자네뿐만이 아니야.”

“……이미 ‘그곳’을 염두에 두고 계셨군요.”

“정확히는 호북성에서 일어난 일의 정황을 보고받은 직후였지. 다만 균열이라 불리는 그 괴이한 현상은 나와 본 각의 누구도 예상치 못했던 일이었어.”

나는 잠시 잊고 있던 사실을 떠올렸다.

눈앞의 늙은 무림인은 사십여 년 전에도, 지금도 은영각의 수장이라는 것을.

그리고 이 자리에는 그와 나에게 명령을 내릴 수 있는 유일한 인물이 존재한다는 것을.

“화룡각주 진태경.”

평소와 다른, 묵직한 목소리가 집무실 내부를 울린다.

천하제일검(天下第一劍)이라 불리는 위대한 무인이자 작금 무림의 정점에 선 자. 매종학이 맑고도 푸른 눈빛으로 나를 응시했다.

“자네에게 첫 번째 명령을 내리겠네.”



* * *



쉬이이익!

내딛는 걸음을 따라 맹렬한 바람이 일어난다.

다른 사람의 이목 따위는 신경 쓰지 않고 신법까지 발휘하여 처소로 도착한 나는 힘차게 문을 열어젖혔다.

콰앙!

문이 열림과 동시에 익숙한 얼굴이 보인다.

별채 안에서 빈둥거리다가 벌떡 일어난 혁무진은, 나와 박살 난 문을 번갈아 보더니 작게 중얼거렸다.

“오셨습…… 이야. 주인장이 피눈물 흘리겠구만. 저거 교체한 지 한 식경도 안 된 건데.”

하지만 지금은 주인장의 슬픔에 공감할 만한 여유가 없다.

나는 잘 다녀왔다는 인사 대신 한 마디를 툭 내뱉었다.

“전부 소집해.”

“예?”

혁무진이 어안이 벙벙한 표정으로 되물었다.

“다짜고짜 그게 무슨. 아니, 그 전에 뭘요?”

“화룡각(火龍閣).”

“예에?”

“임무다. 지금 당장.”

“잠깐. 잠깐만요! 조장님, 갑자기 왜요? 어디로 가는데요?”

눈이 화등잔만 해진 채 떠드는 혁무진을 향해, 나는 나직한 목소리로 대답했다.

“남만(南蠻).”
```

## Final English reading copy

```markdown
# Chapter 548

“Well done.”

The moment we stepped out of the great conference hall, Jin Wikyung said those words. I answered with a quiet laugh.

“Why are you laughing?”

“I don’t know. Maybe because your expression doesn’t match what you’re saying?”

“Ah.”

Only then did the stiffness leave his face. But the smile at the corners of Jin Wikyung’s mouth looked as though it might fade at any moment.

“To be honest, I don’t know how I should take what you said. Today, you were just so…”

“It’s all right. This reaction is only natural.”

I understood why Jin Wikyung had trailed off. I thought I could understand how he felt.

*If I were in his position, I would have reacted the same way.*

In this world, the word *death* was not as heavy as one might expect.

Murders were rare in the modern world and became known through television and other forms of mass media. Here, people witnessed death frequently.

Things were at least somewhat better in cities with good public order. But outside them, commoners had to live under the threat of bandits or mounted bandits, depending on where they were.

Martial artists were another matter entirely.

*A life spent walking along the edge of a blade.*

There was a reason people called it a mountain of sabers and a forest of swords.

That was why they were always prepared to die. They stoked their fighting spirit and trained their martial arts. And Jin Wikyung, standing before me, was a martial artist too.

The problem was the environment he and all the others had grown up in.

In Murim, people killed people, and people died by human hands. There were fierce beasts and spiritual creatures, but at least everyone knew what they were. They were not unheard-of monsters.

But today, I had claimed that…

Those monsters would cover this world.

I had predicted that a battle would begin in which humans and monsters killed one another.

*I don’t know how much my words really sank in, but they must have felt the danger clearly enough.*

As I continued speaking, some people looked at me with disbelief, while others sank into deep thought despite their confusion.

Even if they did not all believe me immediately, the fact that they had listened carefully meant I had achieved my modest goal.

*At least my audience was made up of martial artists, and I had hard evidence. That’s the only reason my words got through at all.*

If old Confucian scholars had been the audience, they would have shouted “Confucius Akbar!” and staged a protest against supernatural powers. But the people gathered in the great conference hall were not quite so narrow-minded.

At least, not with the corpse of a four-armed monster lying right in front of them.

*The same went for the Water God Dragon’s remains.*

The Water God Dragon’s remains had been separated by body part and were still being transported under the strictest secrecy.

But I had some of the byproducts I had quietly slipped into my inventory just in case, and they were more than sufficient as important physical evidence.

“Come to think of it, Youngest. Where did you get that? I was certain it had all been collected without a single piece missing.”

“What?”

“You know. The imugi you defeated in Hubei…”

“Ahem. Ahem. Cough-cough-cough!”

When I forced out a series of coughs, Cheongpung, who had been listening to our conversation beside me, rummaged through his robes.

“Benefactor. Would you like a sweetmeat? Sweetmeats are the best medicine for a cough.”

“…No. They’re the worst.”

“Yes.”

*When did sweetmeats become miracle medicine?*

At my firm refusal to participate in his experiment, the mad scientist Cheongpung looked dejected and popped a sweetmeat into his own mouth. Jin Wikyung watched him and let out a quiet laugh.

“I understand. I won’t ask any further.”

“Good. I appreciate that.”

As I awkwardly scratched my chin, Jin Wikyung stared at me for a long moment before suddenly speaking.

“Sometimes, I find myself wondering. Whether you, our youngest, are really the same child I knew.”

“……!”

“I won’t ask you outright. Nor will I harbor any further doubts. But there is one wish I have never told you about.”

His gentle voice continued.

“When all of this is over someday, and the time is right, I would like to hear the stories you have not yet been able to tell.”

*The stories I haven’t been able to tell.*

I repeated the words silently to myself.

*When will that time come?*

But if everything really ended as Jin Wikyung said, and if I had finished preparing myself mentally…

Perhaps I would tell him myself the secret I had never been able to share with anyone.

Perhaps such a day would come.

“…I understand.”

And it was at that exact moment, when I gave him a bitter smile and nodded, that—

“There you are, Fire Dragon Pavilion Master.”

*Tap.*

A dull sound rang out with the elderly voice. I turned my head and saw Song Ho, the Chief of the Hidden Shadow Pavilion of the Murim Alliance—the Thousand-Faced Fox.

“The meeting ended half an hour ago. Yet you are still here. Is that a coincidence?”

I shook my head.

The reason I had remained in the Murim Alliance until now was not merely to speak with Jin Wikyung.

“It must have been inevitable.”

“Inevitability, is it? Yes, I suppose so.”

A strange light flickered through the old fox’s crafty eyes. After a brief silence, the Thousand-Faced Fox spoke again.

“Come with me, Fire Dragon Pavilion Master. You already know what this is about, don’t you?”

I did.

I knew who wanted to see me. I knew why.

And the Thousand-Faced Fox’s next words changed my guess into certainty.

“The Alliance Leader is looking for you.”

* * *

*Thud.*

The sound of the door closing behind me echoed unusually loudly. Two people were already waiting for me in the office inside the Alliance Leader’s Hall.

“Have you arrived?”

After Jeok Cheongang’s flat question, Murim Alliance Leader Mae Jonghak gestured toward a seat.

“Sit down. And you all, wait outside for a moment.”

He was not speaking to me or to the Thousand-Faced Fox, who had entered the office right behind me. He was speaking to other people who had not revealed themselves.

*Swish.*

The moment Mae Jonghak finished speaking, several presences vanished like ghosts.

Even the secret guards who always remained around him withdrew. I sat in the empty chair and spoke.

“They’re incredibly skilled. I could barely sense their presence.”

“Most people who enter this room don’t even realize that much. You’re impressive for noticing.”

“Even if they don’t know, wouldn’t they at least guess? It would be strange for someone as important as the Murim Alliance Leader to have no guards at all.”

“Ah. That’s true as well.”

Mae Jonghak scratched his chin like a young man his age and suddenly looked at me. My face was reflected in his clear, deep eyes.

“First, I found what you said in the great conference hall quite impressive.”

“I’m glad to hear that. I don’t know what the others thought.”

“Even if they don’t believe everything, they won’t be able to dismiss it. I promise you that.”

A light remark carried different weight depending on whose lips it came from.

And when the speaker was the Alliance Leader of the Murim Alliance, it was only natural for those words to carry tremendous authority.

*That will give my argument even more weight.*

It was not a bad development. As my expression relaxed slightly, Mae Jonghak smiled.

“You must have been worried.”

“I’d be lying if I said I wasn’t.”

“Since we are on the subject, let me ask you. How certain are you of your own claim?”

“Five-tenths. Fifty-fifty.”

The Thousand-Faced Fox’s face went rigid.

“Did you just say… five-tenths?”

“Is that less than you expected?”

“Damn it. It’s the opposite! You’re saying there’s a fifty-percent chance that the world will be covered in monsters!”

The Thousand-Faced Fox’s lament contained a brief curse, but no one paid attention to it this time.

Rather than feeling offended, I felt relieved.

Their reactions told me that, at the very least, the people gathered here had already accepted my claim as fact.

“What grounds do you have for that fifty percent?”

Mae Jonghak’s question remained calm. I gave him the answer I had already prepared without hesitation.

“Everything I’ve seen and felt while fighting Dark Heaven.”

At that moment, Jeok Cheongang, who had been sipping strong liquor instead of tea, suddenly spoke.

“You could be wrong.”

“I would be more than happy to be cursed out for the rest of my life if that were true.”

I meant it.

I would much rather have my prediction be completely wrong, with Dark Heaven turning out to be nothing special and no mutant monsters ever appearing.

If getting cursed out by everyone meant I could see a happy ending, it would be a bargain.

But…

“It sounds insane, but it’s all true.”

“Damn it. This is driving me crazy.”

“Is it really that hard to believe?”

“I don’t want to believe it. If it were anyone but you saying it, I wouldn’t.”

“……!”

*Where did that sudden burst of emotion come from? What am I supposed to do with this?*

*Thud.*

But emotional or not, to hell with all that. Jeok Cheongang slammed his liquor bottle down and glared at me.

“Tell me it’s a lie instead. If you confess right now, I’ll let you off with three strikes from the Flame Divine Palm.”

“I swear on my balls, right here and now, that I’m not making this up. And three strikes from the Flame Divine Palm would kill me.”

“Whew.”

Jeok Cheongang let out a deep sigh and turned toward Mae Jonghak and the Thousand-Faced Fox.

“This old man doesn’t want to believe it either, but it seems everything that punk says is true. At least when he stakes his balls, he’s sincere.”

“……”

The standard for determining whether something was true was a little strange, but somehow my sincerity seemed to have gotten through.

And just as my worst fears began to take shape, the silence that descended over the office was broken by Mae Jonghak.

“I have one more thing to ask.”

“You can ask two things if you want.”

“No. One is enough.”

*Swish.*

Mae Jonghak crooked one finger as he spoke.

At the same time, a large scroll flew from among the bamboo slips piled behind him and unfurled across the table where we were seated.

*Rustle.*

I stared at what was written—or rather, drawn—on the scroll and muttered,

“This is…”

“You are looking at exactly what you think you are. A complete map of the realm.”

As Mae Jonghak had said, it was a map marked with the geography and terrain of various parts of the realm, along with their names.

But it was larger than any map I had seen in Murim, and there was one particularly notable difference.

“It even shows the locations of the various sects.”

“It was made for the Murim Alliance. Now, let me ask you…”

Mae Jonghak’s calm voice pierced my ears.

“Where do you think Dark Heaven’s next target will be?”

“I can’t be certain.”

“Who in this world can be certain of the future? A simple guess will do.”

*A simple guess…*

I remained silent, lost in thought. Then, suddenly, I raised my hand and pointed to one part of the map.

*Tap.*

“This place.”

The reactions were immediate.

Jeok Cheongang muttered a quiet curse. A sharp light flashed in the Thousand-Faced Fox’s eyes, while Mae Jonghak leaned his upper body toward me.

“Why did you choose that place?”

“If what happened in Hubei happens again, Dark Heaven would be hard-pressed to find a more suitable place.”

“You are referring to that ‘rift.’”

“Yes.”

“Do you believe—or rather, do you guess—that the rift will happen again?”

“I think the possibility is more than high enough. What happened was not a natural disaster. It was something Dark Heaven planned and caused.”

*The word “first” only exists because there is a second.*

Only I had been allowed to glimpse the Water God Dragon’s memories, even if only briefly.

That meant I had no physical evidence or certainty I could confidently present. But the probability that Dark Heaven was targeting *that place* was high.

I continued calmly.

“I don’t know what Dark Heaven is going to do right now. This may not be its next target. But at least one person must have already set out for that place.”

“The Southern Heaven Demon Empress.”

The moment Mae Jonghak spoke the title, countless corpses I had witnessed in Hubei flashed before my eyes.

My fist clenched before I realized it.

“That’s right. If it’s the Southern Heaven Demon Empress… she must have that place in mind.”

“Is that another simple guess?”

“It’s a guess. One close to certainty.”

There was nothing I could be certain of. I merely believed that the thought that had refused to leave my mind for some time carried a considerable likelihood.

Mae Jonghak nodded quietly and turned his gaze toward one person.

“What do you think, Chief of the Hidden Shadow Pavilion?”

“I agree with the Fire Dragon Pavilion Master, and I will add my own support.”

Song Ho answered immediately and continued.

“It has been more than seven days and nights since we sent the dispatch. Since no reply has arrived, there is a considerable chance that trouble has already occurred.”

“I expected that much, but… that was fast.”

“Yes. We could move the Outer Hall forces we had selected in advance, but we might already be too late.”

The Thousand-Faced Fox read the question in my expression and spoke in a calm voice.

“The Hidden Shadow Pavilion’s eyes and ears are scattered throughout the realm. You are not the only one to have made this guess.”

“…You had already been considering that place.”

“To be precise, we began considering it immediately after receiving a report on the circumstances surrounding what happened in Hubei Province. However, that strange phenomenon called a rift was something neither I nor anyone else in this Pavilion anticipated.”

I recalled something I had momentarily forgotten.

The elderly martial artist before me had been the head of the Hidden Shadow Pavilion forty years ago, and he was still its head now.

And there was one person in this room who could issue orders to both him and me.

“Fire Dragon Pavilion Master Jin Taekyung.”

A heavy voice unlike his usual one rang through the office.

Mae Jonghak, the great martial artist known as the Number One Sword Under Heaven and the man standing at the pinnacle of Murim today, stared at me with clear blue eyes.

“I am giving you your first order.”

* * *

*Whoosh!*

A fierce wind rose with every step I took.

Ignoring the eyes of everyone around me, I even used my movement technique to hurry back to my residence. When I arrived, I flung open the door with all my strength.

*Bang!*

The moment the door flew open, I saw a familiar face.

Hyuk Mujin had been lounging around inside the annex before jumping to his feet. He looked back and forth between me and the shattered door, then muttered,

“Welcome back… Wow. The owner is going to cry tears of blood. That door was replaced less than half an hour ago.”

But I had no time to sympathize with the owner’s sorrow.

Instead of greeting him and saying I had returned safely, I tossed out a single sentence.

“Summon everyone.”

“What?”

Hyuk Mujin stared at me, dumbfounded.

“What are you talking about all of a sudden? Wait, summon what?”

“The Fire Dragon Pavilion.”

“What?”

“It’s a mission. Right now.”

“Wait. Hold on! Captain, why all of a sudden? Where are we going?”

I answered the wide-eyed Hyuk Mujin in a low voice.

“Nanman.”
```

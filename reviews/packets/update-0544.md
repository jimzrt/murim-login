<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0544.txt",
      "sha256": "968d8386b17992fb4f70949cbe281fdbe5154544c5137dc245efd4c37a599e95",
      "bytes": 12704
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "2959ecd71d80ce58db8b82eac16affa872a7d431d453465fd0e065721a8dffb4",
      "bytes": 4451
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "eb6d8b5412220de793f1ab7ce0727cc4156c219aced15305267b5fe7d3ec0780",
      "bytes": 171914
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "899199bd626fef8d0624ec7ccad43d3938d636ce5df297efd7bc58639e8721d3",
      "bytes": 1370
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "75e8029535f27c81efc8544557aaffd6afcb337af5bdcacff5822b31e23b839c",
      "bytes": 1108
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "9a3e2d91bfef96c783f54927d49f8d25a462d5628d53285fa770656cb2a8337b",
      "bytes": 1630
    },
    {
      "path": "characters/Ju Hwaran.md",
      "sha256": "7d9779d55d13a441daa9c5657082cb4925f5081bb57062e7fdaebfdd6dfdbcfc",
      "bytes": 935
    },
    {
      "path": "characters/Mae Jonghak.md",
      "sha256": "1ce610233d54f02c972f1034405954f4851b04df2f966ec207eb66041aebfad9",
      "bytes": 985
    },
    {
      "path": "characters/Mungyeong.md",
      "sha256": "03dacc25479abba654529e43894540ec9138dacbdb1cae082f70702d64ffbac9",
      "bytes": 1233
    },
    {
      "path": "characters/Sama Pyo.md",
      "sha256": "cc69e5a5b274a4c018df1b4d4c0bcabdf8e5a02c80e8d74be5adc39a748842cc",
      "bytes": 810
    },
    {
      "path": "characters/Song Il.md",
      "sha256": "b315e1cfc1827a215978f14ac290ac926a6216571597eafd0f3976851c7e6f69",
      "bytes": 964
    },
    {
      "path": "characters/Song Ilseom.md",
      "sha256": "c908822b80ef13382880c503ed73b32ee620636b5ff058964138f60d9f4e6b56",
      "bytes": 751
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "5e5e7b949a37249dee79e809f0f35d6eb6734915723c98b5b2a1170d8b33a0b1",
      "bytes": 487
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "e190d1f4dfdecc6495d6974499268ad909f972ce7efdd79c30e42b78daed2e44",
      "bytes": 164631
    }
  ],
  "estimated_tokens": 13312
}
-->

# Durable State Update — Chapter 544

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 544. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 544. Profile updates may replace only one
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
  "chapter": 544,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 544,
    "continuity_sources": [544],
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
    "The Mount Song Resolution formally restored the Murim Alliance; Mae Jonghak is its Alliance Leader, and Song Ho commands the Hidden Shadow Pavilion under his authority.",
    "Mae Jonghak formally appointed Jin Taekyung and Cheongpung as the two pavilion masters of the Alliance Leader's direct Two Dragons Pavilion, and their appointments are public throughout Henan.",
    "Tang Sadok and the Sichuan Tang Clan publicly support Jin Taekyung and Cheongpung and acknowledge an unrepayable debt to them.",
    "Taekyung believes the Zhongnan Sect resents him, the Jin Family of Taiyuan, and Jeok Cheongang after its repeated humiliations and will obstruct them.",
    "Cheongpung created Mimi Step from Mimi's movements; it is a snake-like footwork technique fast enough that Taekyung could barely track it with his naked eyes, and Mungyeong recognizes Cheongpung as having the makings of a Grandmaster.",
    "Mimi is now a large horned snake under Cheongpung's care, eats dumplings, sweets, and Blood Fish, and has recently had her condition examined by Mungyeong.",
    "Mungyeong ended Taekyung's direct training and assigned him a final task of incorporating martial principles into his learned martial arts; Mungyeong has accepted Cheongpung's offer to accompany him.",
    "Zhuge Feng's Demon-Sealing Formation still blocks all mana from the exposed Gate, while Jang Taebo is summoning artisans to process the Water God Dragon's remains.",
    "The Southern Heaven Demon Empress is traveling toward Yunnan and expects to cause further deaths.",
    "The Black Dragon Demon Gate remains a major unorthodox power descended from the Demonic Cult's Twelve Branches; Sama Pyo is its Young Sect Leader and Black Dragon Saber, Taishan is his giant subordinate, and Sama Pyo has disobeyed Sima Gong while pursuing a path he believes still serves his father's goals.",
    "Jin Taekyung remains a Supreme Peak master with Three Flowers Gather at the Crown, advanced qi perception, exceptional resistance to monster Fear, and public S-rank-level recognition despite retaining an A-rank license.",
    "The Two Dragons Pavilion has accepted Ju Hwaran and Song Ilseom; recruitment interviews drew a huge crowd, Jeok Cheongang's attack on Old Man Ilyang drove many applicants away, and Sama Pyo remains under consideration after applying."
  ],
  "continuity_sources": [
    543,
    542
  ],
  "open_questions": [
    "What is the Lord of Heaven's identity, how is he connected to the dangerous force Taekyung associates with his original world, and how can Dark Heaven open Gates?",
    "Where is the Southern Heaven Demon Empress ultimately headed, and what does she intend to do in Yunnan?",
    "What is the outcome of the duel between Jeok Cheongang and Nangong Cheon, the Azure Sky Sword King?",
    "Why did Ju Hwaran and Sama Pyo's political engagement end?",
    "Which additional companions will join the Two Dragons Pavilion, including whether Sama Pyo will be accepted, what name it will receive, and whether Taekyung can complete the System Quest?"
  ],
  "safe_through": 543,
  "temporary_decisions": [
    "Render 고월루 as Gowolru, 곤륜운룡 as Kunlun Cloud Dragon, 학우 as Hak Woo, 이룡각 as Two Dragons Pavilion, 협 as chivalry, 인의 as humanity, 협객 as knight-errant, 홍학루 as Honghakru, 홍매 as Hongmae, and 호거아 as Tiger Giant Child; render 전 정혼자 contextually as former fiancé or former fiancée.",
    "Render 탈진 as the capitalized system status Exhaustion; retain Ten Dragons and Phoenixes, Blazing Flame Divine Dragon, Dark Heaven, Murim Alliance, and Old Master.",
    "Render 황보세가 as Hwangbo Family, 소가주 as Lesser Family Head, 은비화 as Dagger Hidden Flower, and 전음 as Sound Transmission.",
    "Preserve the chapter's blunt profanity, financial-therapy humor, monster-comparison humor, and Mae Jonghak's carefree 'That can happen' refrain; render 고잉무림호 as Going Murim ship, 대종사 as Grandmaster, 왕희지 as Wang Xizhi, and 영창 피아노 as Young Chang piano.",
    "Render 일기천룡 as One-Ride Heavenly Dragon and Taishan's speech as clipped, childlike, and literal; render 일양노 and 열양노 as Old Man Ilyang, 원철 as Won Cheol, 흑혈도 as Black Blood Saber, 노귀산 as No Guisan, 원썬 as One Sun, 흑야왕 as Black Night King, and 녹림투왕 as Green Forest Battle King."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 매종학    | **Mae Jonghak**    |
| 청풍     | **Cheongpung**     |
| 송일     | **Song Il**        |
| 주화란    | **Ju Hwaran**      |
| 쾌풍검    | **Swift Wind Sword**          | Hyuk Mujin     |
| 은비화    | **Dagger Hidden Flower**      | Ju Hwaran      |
| 종남파    | **Zhongnan Sect**                |
| 암천     | **Dark Heaven**                  |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무인     | **martial artist**                               | Default term                                          |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 낭인     | **wandering martial artist**                     |                                                       |
| 표국     | **Escort Bureau**                            |
| 시스템              | **System**                     |
| 명성               | **Fame**                       |
| 퀘스트              | **Quest**                      |
| 보상               | **Reward**                     |
| 노부      | **this old man / I**                                            |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 소협      | **Young Hero**                                                  |
| 소저      | **Young Lady**                                                  |
| 문경 | **Mungyeong** | Young medical apprentice and newly introduced passenger. |
| 사마표 | **Sama Pyo** | Young Sect Leader of the Black Dragon Demon Gate. |
| 송일섬 | **Song Ilseom** | Young escort captain of the Yongbong Escort Bureau; distinct from Song Il of Zhongnan. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 반로환동 | **Returned to Youth** | Possible explanation for an apparently young Supreme Peak master. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 준이 | **Jun** | Family nickname used in the form Jun's dad. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 화란 | **Hwaran** | Familiar short form of Ju Hwaran. |
| 표왕 | **Escort King** | Epithet of Ju Gongsan. |
| 광동진가 | **Guangdong Chen Family** | Family whose last child Ju Gongsan carried to Henan during the Great Faction War. |
| 광동 | **Guangdong** | Province under Demonic Cult control during the war. |
| 검동 | **sword boy** | Young attendant hired by wandering martial artists to carry swords and perform dangerous errands. |
| 추혼객 | **Soul-Chasing Guest** | Song Ilseom’s former epithet; he was known by it ten years earlier. |
| 일원 | **One Origin** | Named Tang Clan organizational unit in Tang Sadok's mobilization order. |
| 열화신룡 | **Blazing Flame Divine Dragon** | New sobriquet bestowed on Jin Taekyung. |
| 이룡 | **Two Dragons** | Collective ranking beneath the Ten Kings in Murim gossip. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 흑룡도 | **Black Dragon Saber** | Sama Pyo's sobriquet. |
| 식경 | **half an hour** | Time limit given for the requested reports. |
| 이룡각 | **Two Dragons Pavilion** | Named pavilion whose masters are identified as Taekyung and Cheongpung at the chapter's close. |
| 호거아 | **Tiger Giant Child** | Epithet for Taishan. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 청풍 | 혁무진 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung includes Mujin among his 은인들 after receiving the skewers. |
| 혁무진 | 청풍 | martial artist to young master | Young Master | formal-deferential | Mujin uses 공자께서는 when asking why Cheongpung descended from the mountain. |
| 매종학 | 청풍 | grandfather_to_grandson | Pung | affectionate-instructional | Mae Jonghak calls young Cheongpung 풍아 while teaching him the Crouching Tiger Fist. |
| 적천강 | 청풍 | overwhelming_elder_to_young_martial_artist | you / little punk | blunt, amused, and threatening | Jeok Cheongang uses 네, 이놈, and related blunt forms while testing Cheongpung. |
| 청풍 | 적천강 | young_martial_artist_to_overwhelming_elder | Grandpa Jeok | casual-familiar despite deference | Cheongpung uses 적 할아버지 while asking Jeok Cheongang to confirm Taekyung's condition; this is a familial form of address, not literal kinship. |
| 혁무진 | 적천강 | subordinate_to_overwhelming_elder | Great Hero Jeok | deferential and fearful | Mujin uses 적 대협 while reporting Jeok’s orders and Taekyung’s awakening. |
| 적천강 | 혁무진 | overwhelming_elder_to_junior_martial_artist | you stupid fool | blunt and mocking | Jeok calls Mujin a 멍청한 놈 after knocking him down during the attempted escape. |
| 송일 | 청풍 | hostile Zhongnan Elder to younger martial artist | Sword Saint's heir / you | hostile and threatening | Song Il identifies Cheongpung as the Sword Saint's heir and demands that he face the consequences of injuring Gong Ilhyuk. |
| 송일 | 적천강 | former rescued junior to former rescuer | Great Hero Jeok | formal, fearful, and defensive | Uses 적 대협 while insisting that Jeok has no business interfering in the dispute. |
| 적천강 | 송일 | former rescuer to former rescued junior | Zhongnan brat; you; insolent bastard | blunt, mocking, and humiliating | Jeok recalls Song's youthful arrogance and addresses him with contempt while publicly disciplining him. |
| 송일섬 | 주화란 | escort_captain_to_young_bureau_head | Hwaran | urgent and familiar | Calls out 화란아 while urgently warning Ju Hwaran before stepping into the confrontation. |
| 주화란 | 혁무진 | rescued_survivor_to_benefactor | Benefactor | formal-deferential | Hwaran includes Mujin among the Benefactors when greeting Taekyung's companions. |
| 주화란 | 청풍 | rescued_survivor_to_benefactor | Benefactor | formal-deferential | Hwaran includes Cheongpung among the Benefactors when greeting Taekyung's companions. |
| 주화란 | 송일섬 | bureau_head_to_escort_captain | Captain Song | formal and prosecutorial | Uses his office title, then his personal name, while exposing and confronting him. |
| 청풍 | 문경 | martial_companion_to_medical_apprentice | Medical Apprentice | cheerful-polite | Cheongpung addresses Mungyeong as 의생님 while asking him to greet the Tang Clan. |
| 문경 | 적천강 | old_acquaintances | Fire King | familiar and grave | The figure bearing Mungyeong’s name greets Jeok Cheongang by his established epithet. |
| 적천강 | 문경 | overwhelming elder to old acquaintance | you / little punk | mocking and threatening | Mocks Mungyeong's expression and threatens to poke out his eyes. |
| 문경 | 혁무진 | traveling_companion_to_traveling_companion | Martial Warrior Hyuk | formal-polite | Mungyeong asks Mujin to deliver water to Taekyung and lets Mujin receive the credit. |
| 혁무진 | 문경 | traveling_companion_to_traveling_companion | Mungyeong | casual-familiar | Mujin recognizes Mungyeong while reacting to Taekyung's dismantling work. |
| 매종학 | 적천강 | long-standing martial rival and friend | Great Hero Jeok | casual and familiar | Mae addresses Jeok as 적 대협 while discussing the Alliance Leader position. |
| 적천강 | 매종학 | long-standing martial rival and friend | you | blunt and familiar | Jeok addresses Mae as 당신 while recalling their meeting at Mount Jiuhua. |
| 주화란 | 사마표 | former_fiancés | Young Sect Leader | formal and guarded | Hwaran formally greets her former fiancé. |
| 사마표 | 태산 | Young Sect Leader to subordinate | Taishan | informal and patronizing | Sama Pyo calls Taishan by name while ordering him to leave. |
| 태산 | 사마표 | subordinate to Young Sect Leader | Lord | crude and deferential | Taishan uses 주군 while obeying Sama Pyo. |
| 청풍 | 매종학 | grandson to grandfather | Grandpa | casual-familiar | Repeatedly calls Mae Jonghak 할아버지 while mistaking the Alliance Leader's summons as a family visit. |
| 문경 | 청풍 | martial_master_to_prospective_companion | you | blunt and informal | Mungyeong questions Cheongpung about Mimi Step and why he offered to accompany him. |
| 사마표 | 적천강 | Young Sect Leader to legendary elder | Great Hero Jeok | formal-deferential | Sama Pyo formally pays his respects to Jeok Cheongang as the Fire King. |
| 태산 | 적천강 | subordinate of a Young Sect Leader to legendary elder | Fire King | clipped, childlike, and deferential | Taishan gives his awkward greeting and expresses admiration for Jeok's strength. |
| 적천강 | 사마표 | legendary elder to unorthodox Young Sect Leader | you / young brat | blunt, suspicious, and contemptuous | Jeok addresses Sama Pyo with 네놈 and 어린놈 while probing his lineage and motives. |
| 적천강 | 태산 | legendary elder to giant subordinate | you / strange fellow | blunt, startled, and grudgingly tolerant | Jeok addresses Taishan as 네놈 while reacting to his greeting and appetite. |

## Listed compact profiles

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 543
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, the grandson and Disciple of Sword Saint Mae Jonghak, a Supreme Peak martial master known as the Huashan Divine Dragon, the creator of the snake-inspired Mimi Step footwork technique, and now one of the two pavilion masters of the Alliance Leader's direct Two Dragons Pavilion.
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, a deep love of martial arts, competitive pride, unusual resistance to monster-induced Fear, and discomfort when someone copies his martial arts.
- **Voice:** Dreamy and hazy, with innocent, polite phrasing; he has begun imitating Taekyung's profanity.
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions while Taekyung is his only true martial rival; Tang Sadok has temporarily entrusted Mimi, now a large horned snake, to him, Mungyeong recently examined her condition, and Mungyeong accepted Cheongpung's offer to accompany him after Cheongpung pledged to learn by observation rather than formal instruction.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 543
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers and Vice Squad Leader of the Jin Dragon Squad.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 543
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, and Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Ju Hwaran.md

# Ju Hwaran (주화란)

- **Safe through:** Chapter 543
- **Aliases:** Hwaran
- **Role:** Level 88 Young Bureau Head and leader of the Yongbong Escort Bureau, responsible for its personnel and contracts after Heo Jun’s betrayal, and now a member of the Two Dragons Pavilion.
- **Personality:** Intelligent, capable, responsible, filial, composed under pressure, and burdened by intense guilt over the escort journey's deaths.
- **Voice:** Clear, polite, restrained, and determined.
- **Relationships:** Escort King Ju Gongsan was her paternal grandfather and rescued the Guangdong Chen Family’s surviving child, who became Song Ilseom’s grandmother; Ju Hogun is her father, Heo Jun was her uncle, Sama Pyo was her former fiancé in a political engagement she accepted for her father's sake, Song Ilseom is her direct escort, and Jin Taekyung is a trusted ally.

### Mae Jonghak.md

# Mae Jonghak (매종학)

- **Safe through:** Chapter 543
- **Aliases:** Sword Saint
- **Role:** Sword Saint and Cheongpung's grandfather who now serves as the New Murim Alliance's Alliance Leader.
- **Personality:** Playful, easygoing, and teasing, but capable of handling heavy administrative responsibilities efficiently.
- **Voice:** Friendly, casually familiar, and cheerfully teasing, including when greeting old acquaintances and discussing leadership.
- **Relationships:** Cheongpung's grandfather and martial instructor; taught him the Taeeul Miri Palm; secretly entered Huashan while its Sect Leader slept, left a dagger and handwritten note, and then went into hiding, prompting Huashan's search; fought Jeok Cheongang at Mount Jiuhua more than forty years ago and left after their draw; his old friend Hong Dao left him a letter identifying Jin Taekyung as the Morning Star who would drive away darkness.

### Mungyeong.md

# Mungyeong (문경)

- **Safe through:** Chapter 539
- **Aliases:** Killing Ghost
- **Role:** Mungyeong is the legendary physician known as the former Divine Physician and Slaughter Saint, a Returned to Youth Supreme Peak master and the greatest assassin in history; he was the sole survivor of an assassin training cohort that began with three hundred candidates and passed the Divine Physician title to his Disciple.
- **Personality:** Compassionate, resolute, resourceful, and calm under extreme pressure.
- **Voice:** His Mungyeong persona is timid, deferential, and cheerful, while his Slaughter Saint voice is dry, impassive, and blunt.
- **Relationships:** Dong Feng is his Disciple, Jeok Cheongang is an old acquaintance whom Mungyeong helped break free of his Heart Demon, Mungyeong was asked to look after and instruct Jin Taekyung and has now ended that direct training after teaching him martial principles and giving him a custom fire-qi pill, Cheongpung has offered him companionship and Mungyeong accepted, and Mu Song plus five Water Dragon Stronghold subordinates know he is an exceptionally powerful master but not that he is the Slaughter Saint.

### Sama Pyo.md

# Sama Pyo (사마표)

- **Safe through:** Chapter 543
- **Aliases:** Black Dragon Saber
- **Role:** Young Sect Leader of the Black Dragon Demon Gate and a Morning Star reputed to be no less than the Ten Dragons and Phoenixes.
- **Personality:** Outwardly courteous and smiling, inwardly calculating, but genuinely protective of Taishan and willing to redirect blame onto his subordinate.
- **Voice:** Polite and ingratiating in public, with sardonic humor and controlled evasiveness.
- **Relationships:** Sama Pyo commands the absolutely loyal Taishan, is Sima Gong's son, was Ju Hwaran's former fiancé in a political engagement, and has applied to join the Two Dragons Pavilion while openly intending to use Jin Taekyung as a useful card.

### Song Il.md

# Song Il (송일)

- **Safe through:** Chapter 543
- **Aliases:** Roaring Fury Swordsman
- **Role:** Elder of the Zhongnan Sect and the Roaring Fury Swordsman; senior brother of Sect Leader Gong Iljung; came to the Jin Family of Taiyuan to demand redress for Gong Ilhyuk's injury and the alleged insult to Zhongnan; attacked Jin Taekyung with the Heavenly River Thirty-Six Swords, was stopped by Jeok Cheongang, and was publicly humiliated by him.
- **Personality:** Arrogant, domineering, punitive, and confident in his martial power and seniority.
- **Voice:** Gruff, cutting, condescending, and threatening, with formal authority used to pressure those beneath him.
- **Relationships:** Gong Iljung is his junior Sect Leader and martial younger brother; Gong Ilhyuk is a junior Disciple of his sect; he recognizes Baek Museong and Cheongpung through their Huashan and Sword Saint connections.

### Song Ilseom.md

# Song Ilseom (송일섬)

- **Safe through:** Chapter 543
- **Aliases:** Escort Captain Song
- **Role:** Level 110 young escort captain of the Yongbong Escort Bureau, one of its Dragon-Phoenix Three Escorts, and a newly accepted member of Jin Taekyung and Cheongpung’s Two Dragons Pavilion.
- **Personality:** Blunt, decisive, survival-hardened, and dryly self-aware, with little patience for insults or disorder.
- **Voice:** Forceful and urgent in command, with a rough and confrontational edge.
- **Relationships:** He serves under Ju Hwaran, is Song Pyosan’s son, and his grandmother was the surviving Guangdong Chen child rescued by Ju Gongsan during the Great Faction War.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 543
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord.

## Korean source

```text
＃544화



주화란이 떠났다.

창밖 너머, 그림자처럼 뒤따르는 송일섬과 함께 멀어지는 그녀의 뒷모습은 가녀리면서도 당당했다.

“멋있네요, 주 소저.”

등 뒤에서 들려오는 혁무진의 목소리에, 나는 조용히 고개를 끄덕였다.

‘그때도 그랬지.’

문득 처음 주화란을 만났던 그 날이 생각난다.

수백여 명의 적들에게 포위된 절망적인 상황 속에서도 물러나지 않던 모습, 그 눈빛이.

어쩌면 그녀는 내가 아는 것보다 훨씬 더 무인(武人)에 가까운 사람일지도 모르겠다.

“안타깝기도 하고요.”

“그래, 어깨에 진 짐이 많아. 아직 거동이 불편한 아버지도 계시고…….”

“그거 말고요.”

“응?”

고개를 돌리자 딱하다는 표정을 짓고 있는 혁무진의 얼굴이 눈에 들어온다.

“공을 세울 목적이었다면 다른 선택지도 많죠. 굳이 여기까지 찾아온 이유가 뭐겠습니까?”

이유라. 곰곰이 생각하던 나는 헛숨을 삼켰다.

“헛. 설마?”

“예, 바로 그 설마입니다.”

“더욱 큰 공을 세울 수 있을 것 같아서?”

“……됐습니다. 드러워서 못해 먹겠네, 진짜.”

한 대 쥐어박아야 하나, 말아야 하나 고민하고 있을 때 혁무진을 구원하는 목소리가 들려왔다.

“아따, 시원하다.”

측간에 간 지 한 식경 만에 적천강이 나타났다.

순산의 기쁨이 상당한지, 싱글벙글 웃으며 술병부터 집어 든 그가 혁무진의 표정을 보고 멈칫했다.

“네놈은 왜 그렇게 똥 씹은 얼굴을 하고 있느냐?”

“적 대협. 그게…….”

기다렸다는 듯이 설명을 시작한 혁무진의 이야기를 잠자코 듣고 있던 적천강이 눈을 크게 떴다

“표왕의 손녀가 왔었다고?”

“예.”

“허어, 한창 힘주고 있을 때 범상치 않은 기세가 둘 정도 지나갔었는데, 그중 하나였던 모양이군.”

적천강이 검붉은 수염을 쓰다듬으며 말을 이었다.

“노부가 사경을 헤맬 때 그런 일이 있었다는 이야기는 들었지만, 이리 이어진 것을 보니 제법 질긴 연이다.”

“그런데 다른 선택지를 놔두고 조장님을 찾아온 이유가 뭐라고 생각하십니까?”

적천강의 입가가 씰룩거렸다.

“그걸 굳이 노부의 입으로 말해야겠느냐?”

“그렇죠? 역시 적 대협이십니다.”

혁무진의 얼굴이 LED 전구처럼 환하게 밝아진 그때, 의미심장한 미소를 띤 적천강이 말을 이었다.

“엄청 큰 공을 세울 수 있어서겠지.”

“…….”

어, 전구 꺼졌네.

순식간에 한밤중처럼 안색이 어둑해진 혁무진으로부터 착 가라앉은 목소리가 흘러나왔다.

“진심이십니까.”

적천강이 자신감 넘치는 표정으로 고개를 끄덕였다.

“종남파로부터 상당한 재물을 보상받았다고는 하나, 향후 표국을 지키며 이끌기 위해서는 무림에서의 명성과 실력이 필요하지. 노부가 보아하니, 표왕의 손녀가 제법 세상 돌아가는 이치를 아는구나.”

“저기, 적 대협.”

“왜?”

“외람되지만, 혹시 지금까지 정인(情人)을 사귀신 적이 있으십니까?”

혁무진의 물음에 곰곰이 생각하던 적천강이 대답했다.

“물론 있다.”

“언제쯤인데요?”

“그때가 열 살 무렵이었으니까. 백 년도 더 되었지, 아마.”

“…….”

“왜 그러느냐?”

“그, 아닙니다. 제가 면벽 수련을 하고 있었던 모양입니다.”

“……?”

“진짜 벽이다. 벽. 통곡의 벽.”

해탈한 고승처럼 중얼거리는 혁무진에게서 시선을 뗀 적천강이 나를 향해 고개를 돌렸다.

“그나저나, 네놈은 어쩔 생각이냐?”

“음.”

“표정을 보아하니 이미 마음의 결정을 내린 것 같아 묻는 게다.”

나는 어깨를 으쓱하며 대꾸했다.

“귀신이시네요. 아직 말씀드리지도 않았는데.”

“들어 보니 과히 나쁘지 않다. 네놈이 턱도 없는 괴물이라 그렇지, 그 연배에 절정의 경지라면 뛰어난 성취고 어릴 적부터 표국 일에 관여했다면 경험도 적지 않을 테니.”

“저도 비슷한 생각입니다. 송일섬이라는 호위는 실력만으로도 큰 전력이 될 거고요.”

당시에 사경을 헤매고 있던 적천강은 두 사람을 직접 겪어 본 적이 없지만, 깨어난 후 그간 있었던 이야기를 모두 들은 터라 이해하는 데에는 별다른 무리가 없었다.

“광동진가의 마지막 핏줄이라. 노부가 측간에서 느낀 바로는 상당한 경지였지.”

“……약간 더럽긴 한데, 저도 동의합니다.”

적천강은 반로환동의 경지에 이른 초절정 고수. 그가 상당하다고 평할 정도니 송일섬의 무위에는 그 누구도 이견을 달 수 없는 수준이다.

‘세상에 드러나지 않은 또 한 명의 천재.’

일찍이 혈육을 여의고 홀로 세상에 버려졌다. 낭인의 검동(劍童) 노릇을 하며 전장을 떠돌았고, 마침내 스스로 검을 뽑았다.

송일섬은 온실 속 화초가 아닌, 모진 풍파를 견디며 살아온 잡초였다.

그의 또 다른 이름인 추혼객(追魂客)은 낭인들 사이에서도 전설로 남은 이름이다.

‘청풍과 문경만큼은 아니겠지만, 충분한 전력감이지.’

아쉽긴 해도 불만은 없다. 그동안의 라인업이 너무 화려했던 것도 사실이니까.

사실 지금부터라도 변화하는 것이 당연하다.

초절정 고수는 불리한 전황을 단번에 뒤집을 수 있는 존재. 사방으로 번지는 전화(戰火)의 불길을 막기 위해서는 당연한 선택이었다.

‘매종학도 그런 의미에서 나와 청풍을 따로 나누었을 것이고.’

불길은 여러 개인데 소방차가 한 곳에만 집중될 수는 없는 법이다.

암천과의 전쟁에서 승리하기 위해서, 또한 더욱 큰 희생을 막기 위해서는 이것이 자연스러운 흐름이다.

그리고…… 나는 함께 이 불길을 진압하기 위한 팀원을 꾸려야 한다.

이제는 냉철한 판단과 이성으로 결정을 내릴 시간이다.

‘어쩔 수 없나.’

아무리 생각해 봐도 이것이 최선이다. 아니, 최선이 아니라 해도 차선(次善)의 선택이라는 것은 부정할 수 없다.

생각을 정리한 나는 나직한 목소리로 한 사람의 이름을 불렀다.

“혁무진.”

혁무진은 늘 둔한 것 같으면서도 눈치가 빨랐다.

적어도 내가 성과 이름을 함께 붙여 부를 때만큼은, 평소와 다른 분위기라는 것을 알고 있었다.

“네, 조장님.”

“단도직입적으로 물어보자.”

선택은 내게만 허락된 것이 아니다. 각자의 선택이 모여 하나의 뜻이 된다.

하지만 내가 미처 말을 잇기도 전에, 혁무진이 재빨리 대답했다.

“함께 가겠습니다.”

“뭐?”

“조장님을 따르겠다고요. 그거 물어보려고 하신 것 아닙니까?”

“……맞아.”

“그럼 됐습니다. 물어보실 필요도 없어요. 바늘이 가는 곳에 실이 따라가는 건 당연한 거죠. 아, 물론 궁 소협 같은 배신자는 예외. 이래서 다른 방파에 속한 외인(外人)은 안 된다니까요. 뭐 그리 사정이 많은지.”

장난스럽게 웃어 보이는 혁무진을 말없이 응시하던 나는 입꼬리를 끌어 올렸다.

“너, 후회 안 해?”

“후회요?”

“그래. 후회.”

“조장님. 그거 아십니까?”

혁무진이 진지한 눈빛으로 말을 이었다.

“조장님을 만난 이후로 제 인생이 후회였습니다.”

“개새끼야.”

“그런데, 후회 몇 번 더 하는 것도 나쁘지 않겠더라고요.”

어깨를 으쓱한 혁무진이 천천히 말을 이었다. 텅 빈 허공을 바라보는 시선은 과거 어딘가를 더듬는 듯했다.

“몇 년 전만 해도 사람들은 저를 혁가 포목점 아들내미라고 불렀습니다. 그런데 어느 순간부터는 쾌풍검(快風劍)이라고 하더라고요. 열화신룡의 오른팔이라고도 하고. 저는 그게 참 마음에 듭니다.”

“무진이, 너…….”

“헤헤. 감동받으셨어요?”

“아니, 그거 말고. 넌 오른팔이 아니라 새끼발가락이야.”

“와, 조장님도 어지간하시네. 제가 여태껏 그 고생을 했는데도 아직 새끼발가락입니까?”

억울해하는 녀석의 표정을 보자 피식 실소가 흘러나온다. 이제 좀 승급을 시켜 줘야 하나.

“그럼 새끼손가락.”

“……왼손 새끼손가락?”

“오른손.”

“오른손이라.”

잠시 생각하던 혁무진이 조심스럽게 협상안을 제시했다.

“그럼 오른손 받고, 엄지 어때요.”

“다음 생에 노려 봐라.”

“이럴 줄 알았습니다. 그럼 엄지 말고 검지.”

“턱도 없지.”

“젠장. 오른팔 되려면 일평생을 바쳐야겠네. 이게 말이 됩니까?”

“그래, 평생 걸릴 테니까 그때까지 옆에 있어라. 죽지 말고.”

“……!”

괜한 말을 한 건가.

목욕한 지 얼마 되지도 않았는데, 왠지 모르게 몸이 간질간질하다. 괜히 애꿎은 턱만 긁적인 나는 손을 내밀었다.

“조, 조장님.”

촉촉한 눈동자로 나를 바라보던 혁무진이 내가 내민 손을 굳게 맞잡았다.

덥석.

“조장님의 오른쪽 새끼손가락 혁무진. 충심을 다하여…….”

“너 뭐 하냐.”

“예?”

“누가 손을 달래? 아까 받은 거 가져와.”

“……아.”

그럼 그렇지, 하는 표정으로 혀를 찬 혁무진이 아까 내게 넘겨받은 죽간 두 개를 품에서 꺼냈다.

죽간을 묶은 끈에는 작은 글씨로 두 사람의 이름이 적혀 있었다.

은비화(隱匕花) 주화란.

추혼객(追魂客) 송일섬.

하지만 내가 받아야 하는 죽간은 이것이 전부가 아니다.

아직도 내민 손을 거두지 않는 내 모습에, 무언가를 짐작한 듯 혁무진의 안색이 떨떠름해졌다.

“조장님. 진심이십니까?”

“그래.”

“후우. 이게 옳은 결정인지 모르겠습니다.”

한숨과 함께 두 개의 죽간이 더해진다.

나는 끈에 적힌 이름과 별호를 가만히 내려다보았다.

흑룡도(黑龍刀) 사마표.

호거아(虎巨兒) 태산.

이것이 옳은 결정인지 모르겠다는 혁무진의 말이 귓전에 어른거린다.

그 이유는 간단하다. 이 선택이 최선인지에 대해서는 나 역시 의문이 남으니까.

하지만 다음 순간 들려온 적천강의 목소리는 망설이는 내게 마지막 확신을 심어 주었다.

“무엇을 망설이느냐. 그저 나아가면 그만인 것을.”

복잡하던 머릿속이 맑아진다.

작게 심호흡한 나는 마음속 깊숙한 어딘가를 향해 속삭였다.

‘주화란, 송일섬, 사마표, 태산…….’

그리고 마지막. 혁무진.

단번에 다섯 사람의 이름을 흘려보낸 뒤 명령어를 입력한다.

‘이룡각(二龍閣) 가입 승인.’

누구에게도 들리지 않는 한 마디에, 대답하는 목소리가 있었다.

띠링.



- 가입 승인 절차를 진행합니다.

- 확인되었습니다. [은비화 주화란]. [추혼객 송일섬]. [흑룡도 사마표]. [호거아 태산]. [쾌풍검 혁무진].

- 위 다섯 명을 이룡각의 일원으로 받아들이시겠습니까?



대답은 정해져 있다.

내가 승낙의 뜻을 담아 작게 고개를 끄덕이자, 경쾌한 알림과 함께 허공에 둥둥 떠 있던 반투명한 홀로그램 창이 책장을 넘기는 것처럼 바뀌었다.

띠링.



- 퀘스트, [너, 내 동료가 돼라!]의 조건 중 하나가 완료되었습니다.

- 최소 5명 이상의 동료 확보 (완료)

- 최소한의 인원을 모두 선별하였습니다!

- 정식 각주가 되기 위한 마지막 절차가 남았습니다. 당신이 맡게 된 각(閣)의 새로운 이름을 정해 주십시오!



‘이름이라.’

새롭게 구성된 조직에 어떤 이름을 부여할까에 대해서는 생각해 보지 않았다.

하지만 아무리 고민해도, 지금 막 뇌리를 스친 이것보다는 못할 것이다.

‘화룡각(火龍閣).’

띠링. 띠링. 띠링.

축포처럼 터져 나오는 맑은 종소리와 함께, 힘찬 시스템 알림이 귓가를 파고들었다.
```

## Final English reading copy

```markdown
# Chapter 544

Ju Hwaran had left.

Beyond the window, her slender yet dignified back grew more distant, with Song Ilseom following behind her like a shadow.

“She’s impressive, Young Lady Ju.”

At Hyuk Mujin’s voice from behind me, I quietly nodded.

*She was like that back then, too.*

I suddenly remembered the day I first met Ju Hwaran.

Even in that desperate situation, surrounded by several hundred enemies, she had refused to retreat. That look in her eyes—

*Perhaps she’s far more of a martial artist than I realized.*

“It’s a shame, too.”

“Yes. She has a lot weighing on her shoulders. Her father still has trouble moving, and…”

“That’s not what I meant.”

“Hm?”

I turned around and saw Hyuk Mujin looking at me with a pitying expression.

“If her goal was to earn merit, she had plenty of other options. Why do you think she came all the way here?”

*The reason, huh?*

After thinking it over, I sucked in a startled breath.

“Wait. No way?”

“Yes. Exactly that no way.”

“Because she thought she could earn even greater merit?”

“……That’s enough. This is too damn filthy to work with.”

As I wondered whether to smack him or not, a voice came to Hyuk Mujin’s rescue.

“Ahh, what a relief.”

Jeok Cheongang appeared after spending half an hour in the latrine.

Apparently celebrating a smooth delivery, he was grinning from ear to ear as he reached for the liquor bottle first. Then he saw Hyuk Mujin’s expression and paused.

“Why do you look like you’ve been chewing shit?”

“Great Hero Jeok. The thing is…”

As though he had been waiting for this, Hyuk Mujin began explaining. Jeok Cheongang listened silently, then his eyes widened.

“The Escort King’s granddaughter came here?”

“Yes.”

“Hm. Two unusual auras passed by while this old man was straining himself. I suppose she was one of them.”

Jeok Cheongang stroked his dark-red beard and continued.

“I heard that something like this happened while I was hovering between life and death, but seeing how it has led to this, it seems to be quite a persistent connection.”

“Then why do you think she came to Captain instead of choosing one of the other options?”

The corner of Jeok Cheongang’s mouth twitched.

“Do you really need this old man to say it aloud?”

“Right? I knew you’d understand, Great Hero Jeok.”

Just as Hyuk Mujin’s face lit up like an LED bulb, Jeok Cheongang continued with a meaningful smile.

“Because she can earn a tremendous amount of merit.”

“……”

*Oh. The bulb went out.*

Hyuk Mujin’s complexion darkened as though night had fallen in an instant, and his voice sank low.

“Are you serious?”

Jeok Cheongang nodded with a confident expression.

“Although she received a considerable fortune from the Zhongnan Sect as compensation, she will need fame and skill in the Murim to protect and lead her Escort Bureau in the future. From what this old man saw, the Escort King’s granddaughter understands how the world works.”

“Great Hero Jeok.”

“What?”

“Forgive me for asking, but have you ever had a sweetheart?”

Jeok Cheongang thought carefully before answering.

“Of course.”

“When was that?”

“I was around ten at the time. That was more than a hundred years ago, I think.”

“……”

“Why are you looking at me like that?”

“N-No, it’s nothing. It seems I was practicing wall-facing meditation.”

“……?”

“A real wall. A wall. The Wailing Wall.”

Jeok Cheongang took his eyes off Hyuk Mujin, who was muttering like an enlightened monk, and turned toward me.

“Anyway, what do you intend to do?”

“Hmm.”

“Judging by your expression, you’ve already made up your mind. That is why I ask.”

I shrugged.

“You’re psychic. I haven’t even told you yet.”

“I heard the details, and it is not a bad choice. You are an absurd monster, of course, but reaching the Peak realm at her age is an impressive accomplishment. And if she has been involved in the Escort Bureau’s affairs since childhood, she should have plenty of experience as well.”

“I was thinking along the same lines. An escort captain named Song Ilseom would be a major asset based on his skill alone.”

Jeok Cheongang had been hovering between life and death at the time, so he had never met either of them in person. But after waking up, he had heard everything that had happened, so he had no trouble following the discussion.

“The last bloodline of the Guangdong Chen Family. From what I sensed in the latrine, he had reached a considerable realm.”

“……That’s a little gross, but I agree.”

Jeok Cheongang was a Supreme Peak master who had reached the Returned to Youth realm. If he considered Song Ilseom’s skill considerable, then no one could dispute the man’s martial prowess.

*Another genius the world has yet to discover.*

He had lost his family at an early age and been cast alone into the world. He had wandered the battlefields as a sword boy for wandering martial artists, and eventually drawn a sword of his own.

Song Ilseom was not a greenhouse flower. He was a weed that had survived harsh storms.

His other name, Soul-Chasing Guest, was legendary even among wandering martial artists.

*He may not be on Cheongpung or Mungyeong’s level, but he’s more than enough to be a useful force.*

It was a shame, but I had no complaints. It was a fact that our lineup had been too spectacular until now.

In truth, it was only natural for things to change from this point onward.

A Supreme Peak master could reverse a losing battle in an instant. With the flames of war spreading in every direction, deploying them where they were needed was only natural.

*Mae Jonghak must have separated Cheongpung and me for the same reason.*

There were fires burning in several places. We could not keep sending the same fire truck to one location.

To win the war against Dark Heaven and prevent even greater sacrifices, this was the natural course of things.

And…

I needed to assemble a team to put out these flames with me.

It was time to make a decision with a cool head and reason.

*I suppose it can’t be helped.*

No matter how I thought about it, this was the best option. No—even if it was not the best, there was no denying that it was the second-best choice.

After organizing my thoughts, I called out one person’s name in a low voice.

“Hyuk Mujin.”

Hyuk Mujin always seemed slow, but he was surprisingly perceptive.

At least whenever I called him by both his given name and family name, he knew that the atmosphere was different from usual.

“Yes, Captain.”

“Let me ask you directly.”

The choice was not mine alone to make. Each person’s choice would come together to form a single will.

But before I could continue, Hyuk Mujin quickly answered.

“I’ll go with you.”

“What?”

“I said I’ll follow you, Captain. That was what you were going to ask, wasn’t it?”

“……Yes.”

“Then that settles it. There’s no need to ask. Naturally, the thread follows wherever the needle goes. Of course, traitors like Young Hero Gung are an exception. This is why outsiders from other sects won’t do. They always have so many complications.”

I stared silently at Hyuk Mujin, who gave me a playful smile, then lifted the corners of my mouth.

“You won’t regret this?”

“Regret?”

“Yes. Regret.”

“Captain. Do you know something?”

Hyuk Mujin continued with a serious look in his eyes.

“Ever since I met you, my life has been one long regret.”

“You son of a bitch.”

“But I decided that a few more regrets wouldn’t be so bad.”

Hyuk Mujin shrugged and continued slowly. His gaze, fixed on the empty air, seemed to be feeling its way through some distant place in the past.

“A few years ago, people called me the son of the Hyuk Family Textile Shop. But at some point, they started calling me the Swift Wind Sword. They even started calling me the Blazing Flame Divine Dragon’s right-hand man. I really like that.”

“Mujin, you…”

“Hehe. Are you touched?”

“No, not that. You’re not my right-hand man. You’re my little toe.”

“Wow, Captain. You really are something else. After all the suffering I’ve endured, I’m still just a little toe?”

At his aggrieved expression, a quiet laugh escaped me. Maybe it was time to promote him a little.

“Then you’re my little finger.”

“……My left little finger?”

“Right hand.”

“Right hand…”

Hyuk Mujin thought for a moment, then cautiously presented a counteroffer.

“Then I’ll take the right hand. How about the thumb?”

“Try again in your next life.”

“I knew you’d say that. Then instead of the thumb, how about the index finger?”

“Not a chance.”

“Damn it. I’ll have to devote my entire life to becoming your right-hand man. Does that make any sense?”

“Yes. It’ll take your whole life, so stay by my side until then. Don’t die.”

“……!”

*Did I say something I shouldn’t have?*

I had not even been out of the bath long, yet for some reason my skin felt itchy. I scratched my innocent chin for no reason, then held out my hand.

“C-Captain.”

Hyuk Mujin looked at me with moist eyes, then firmly clasped the hand I had extended.

*Clasp.*

“Hyuk Mujin, your Captain’s right little finger. I will devote my loyalty to—”

“What are you doing?”

“Huh?”

“Who asked for your hand? Bring me what you received earlier.”

“……Oh.”

Hyuk Mujin clicked his tongue with an expression that said *of course*, then pulled the two bamboo slips I had handed him earlier from inside his robe.

The names of two people were written in tiny letters on the cords binding the slips.

Dagger Hidden Flower Ju Hwaran.

Soul-Chasing Guest Song Ilseom.

But these were not the only bamboo slips I needed to receive.

When I still did not withdraw my outstretched hand, Hyuk Mujin’s complexion turned sour, as though he had guessed what I was thinking.

“Captain. Are you serious?”

“Yes.”

“Hoo. I don’t know if this is the right decision.”

With a sigh, two more bamboo slips were added.

I quietly looked down at the names and epithets written on the cords.

Black Dragon Saber Sama Pyo.

Tiger Giant Child Taishan.

Hyuk Mujin’s words—*I don’t know if this is the right decision*—continued to echo in my ears.

The reason was simple. I also had doubts about whether this was the best choice.

But the voice I heard next gave my hesitation one final push.

“What are you hesitating for? All you have to do is move forward.”

Jeok Cheongang’s words cleared my muddled thoughts.

After taking a small, deep breath, I whispered toward some place deep within my heart.

*Ju Hwaran, Song Ilseom, Sama Pyo, Taishan…*

And last of all, Hyuk Mujin.

After letting the names of all five people pass through my mind at once, I entered the command.

*Approve Two Dragons Pavilion membership.*

A voice answered the words no one else could hear.

*Ding.*

> **System**
>
> - Membership approval procedure initiated.
>
> - Confirmed: **Dagger Hidden Flower Ju Hwaran**, **Soul-Chasing Guest Song Ilseom**, **Black Dragon Saber Sama Pyo**, **Tiger Giant Child Taishan**, and **Swift Wind Sword Hyuk Mujin**.
>
> - Will you accept the five people above as members of the Two Dragons Pavilion?

The answer had already been decided.

I gave a small nod to signify my acceptance, and the translucent holographic window floating in the air changed with a cheerful chime, as though it were turning a page.

*Ding.*

> **System**
>
> - One condition of Quest, **Become My Companion!**, has been completed.
>
> - Secure at least five companions (Complete)
>
> - You have selected the minimum number of members!
>
> - One final procedure remains to become an official Pavilion Master. Choose a new name for the Pavilion assigned to you!

*A name, huh?*

I had never thought about what name to give the newly formed organization.

But no matter how much I thought about it, nothing could possibly be better than the name that had just flashed through my mind.

*Fire Dragon Pavilion.*

*Ding. Ding. Ding.*

Along with the clear bell tones bursting out like celebratory fireworks, powerful System alerts rang in my ears.
```

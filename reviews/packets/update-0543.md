<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0543.txt",
      "sha256": "508fef093bea0f913942d12a29525009f841b87b4e7745047c77cfc9a5d5de23",
      "bytes": 13429
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "220ab58272569ee85ff2dc042887660ef53d41b56356c5e01574b7e10497a36f",
      "bytes": 4449
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "2b4834e3feb0e1467bcbadd60bded3e92bb83558ac504b0b7a0313576d6bf68d",
      "bytes": 171827
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "8a2cdaa361b6fc75491e5b041529a03c0e4a6174b4653dae4925b9f9446a28f3",
      "bytes": 1370
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "19ccdba69cd08264b47a2c6b5f5058f7693e1b854fb7f62cae3840cd7295fa64",
      "bytes": 553
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "d5f0f399572addc9d2e649cdab423c6a49e86ebeab5f184bb25089b177d5fc4a",
      "bytes": 1108
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "fc36fdb461b7f311915b4fcc9963035eb011990189cb120cb26f3a94d618453a",
      "bytes": 1630
    },
    {
      "path": "characters/Ju Hwaran.md",
      "sha256": "cfd35c81cbcc4277133e9c83f3519af45f705c67b96669be00e0075e79c92746",
      "bytes": 971
    },
    {
      "path": "characters/Mae Jonghak.md",
      "sha256": "dcd45971bf56fe460e3758b20019fbdbce7b965542cbd4d437e9144b6491adf4",
      "bytes": 985
    },
    {
      "path": "characters/Old Man Ilyang.md",
      "sha256": "20985ca2e23036714224ab52b319a95526c2096d3020781c2bdd7426282471c7",
      "bytes": 793
    },
    {
      "path": "characters/Sama Pyo.md",
      "sha256": "a615df74e964e97b0b9c8d76ad1bf37f2a1f16f1dd1775e4cb759c7158aaab74",
      "bytes": 810
    },
    {
      "path": "characters/Sima Gong.md",
      "sha256": "a8fc38b4ce531c76f251773891385930feb6aac770ae946616ded468221e9f1c",
      "bytes": 641
    },
    {
      "path": "characters/Song Il.md",
      "sha256": "5a0c5f6d994e84e44f3f0800a94c739099000a15f712f7341d1d1fe31371b205",
      "bytes": 964
    },
    {
      "path": "characters/Song Ilseom.md",
      "sha256": "fe75e630d01b8b19ccd27551bbb03c60f234f76e95bc9a14f90c8f848fc1488f",
      "bytes": 889
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "34218de0fa63d55deae44accbe1aae86b3171150e2fa4e5b76706d46b3fe831d",
      "bytes": 487
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "c8e8dbdcb812d46a4a7e74c59c5f59c827a169b6ebf9860c809c8e5188e33644",
      "bytes": 164439
    }
  ],
  "estimated_tokens": 13967
}
-->

# Durable State Update — Chapter 543

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 543. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 543. Profile updates may replace only one
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
  "chapter": 543,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 543,
    "continuity_sources": [543],
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
    "The Black Dragon Demon Gate remains a major unorthodox power descended from the Demonic Cult's Twelve Branches; Sama Pyo is its Young Sect Leader and Black Dragon Saber, Taishan is his giant subordinate, and Sama Pyo has applied to join the Two Dragons Pavilion.",
    "Jin Taekyung remains a Supreme Peak master with Three Flowers Gather at the Crown, advanced qi perception, exceptional resistance to monster Fear, and public S-rank-level recognition despite retaining an A-rank license.",
    "The System has assigned Taekyung's first Two Dragons Pavilion Quest: recruit at least five companions and name the organization, or receive the Title Loner; recruitment interviews have drawn a huge crowd, Jeok Cheongang's attack on Old Man Ilyang drove many applicants away, and Sama Pyo is now under consideration."
  ],
  "continuity_sources": [
    542,
    541
  ],
  "open_questions": [
    "What is the Lord of Heaven's identity, how is he connected to the dangerous force Taekyung associates with his original world, and how can Dark Heaven open Gates?",
    "Where is the Southern Heaven Demon Empress ultimately headed, and what does she intend to do in Yunnan?",
    "What is the outcome of the duel between Jeok Cheongang and Nangong Cheon, the Azure Sky Sword King?",
    "Why did Ju Hwaran and Sama Pyo's political engagement end?",
    "Which additional companions will join the Two Dragons Pavilion, including whether Sama Pyo will be accepted, what name it will receive, and whether Taekyung can complete the System Quest?"
  ],
  "safe_through": 542,
  "temporary_decisions": [
    "Render 고월루 as Gowolru, 곤륜운룡 as Kunlun Cloud Dragon, 학우 as Hak Woo, 이룡각 as Two Dragons Pavilion, 협 as chivalry, 인의 as humanity, 협객 as knight-errant, 홍학루 as Honghakru, 홍매 as Hongmae, and 호거아 as Tiger Giant Child; render 전 정혼자 contextually as former fiancé or former fiancée.",
    "Render 탈진 as the capitalized system status Exhaustion; retain Ten Dragons and Phoenixes, Blazing Flame Divine Dragon, Dark Heaven, Murim Alliance, and Old Master.",
    "Render 황보세가 as Hwangbo Family, 소가주 as Lesser Family Head, 은비화 as Dagger Hidden Flower, and 전음 as Sound Transmission.",
    "Preserve the chapter's blunt profanity, financial-therapy humor, monster-comparison humor, and Mae Jonghak's carefree 'That can happen' refrain; render 고잉무림호 as Going Murim ship, 대종사 as Grandmaster, and 왕희지 as Wang Xizhi.",
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
| 사마공    | **Sima Gong**      |
| 은비화    | **Dagger Hidden Flower**      | Ju Hwaran      |
| 하오문    | **Lower District Sect**          |
| 종남파    | **Zhongnan Sect**                |
| 무림맹    | **Murim Alliance**               |
| 용봉표국   | **Yongbong Escort Bureau**       |
| 십봉룡    | **Ten Dragons and Phoenixes**    |
| 절정     | **Peak**          |
| 무인     | **martial artist**                               | Default term                                          |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 주화입마   | **qi deviation**                                 |                                                       |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 마교     | **Demonic Cult**                                 |                                                       |
| 강호     | **martial world**                                | Prefer “Murim” where the setting itself is meant      |
| 문주     | **Sect Leader**                              |
| 표국     | **Escort Bureau**                            |
| 소국주    | **Young Bureau Head**                        |
| 하남     | **Henan**              |
| 정마대전   | **Great Faction War**         |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 소저      | **Young Lady**                                                  |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 일양노 | **Old Man Ilyang** | Sobriquet of the eighty-five-year-old Supreme Peak master Won Cheol. |
| 사마표 | **Sama Pyo** | Young Sect Leader of the Black Dragon Demon Gate. |
| 송일섬 | **Song Ilseom** | Young escort captain of the Yongbong Escort Bureau; distinct from Song Il of Zhongnan. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 문주님 | **Sect Leader** | Honorific title Lee Seowol orders the senior figures to use. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 야왕 | **Night King** | Rumored epithet for Jin Taekyung in Taiyuan's red-light district. |
| 개방 | **Beggars' Sect** | Murim organization counted among the Nine Sects and One Gang. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 무재 | **martial talent** | Innate aptitude for learning martial arts. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 마공 | **demonic martial arts** | Martial arts that appear to defy common principles. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 화란 | **Hwaran** | Familiar short form of Ju Hwaran. |
| 표왕 | **Escort King** | Epithet of Ju Gongsan. |
| 이룡 | **Two Dragons** | Collective ranking beneath the Ten Kings in Murim gossip. |
| 흑룡마문 | **Black Dragon Demon Gate** | Unorthodox faction from Gansu. |
| 흑룡도 | **Black Dragon Saber** | Sama Pyo's sobriquet. |
| 맹주부 | **Alliance Leader's Office** | Office directly serving the Alliance Leader. |
| 식경 | **half an hour** | Time limit given for the requested reports. |
| 이룡각 | **Two Dragons Pavilion** | Named pavilion whose masters are identified as Taekyung and Cheongpung at the chapter's close. |
| 흑야왕 | **Black Night King** | Epithet of Sima Gong, Sama Pyo's father and the Sect Leader who built the modern Black Dragon Demon Gate. |

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
| 상인 | 적천강 | merchant_to_legendary_martial_master | Great Hero Jeok | deferential and flattering | Praises Jeok Cheongang while presenting the Poison-Averting Ring and requesting help. |
| 적천강 | 상인 | legendary_guest_to_merchant | you | blunt and transactional | Cuts off the merchant’s praise, asks his identity and origin, and accepts the gift without committing to the requested favor. |
| 송일섬 | 주화란 | escort_captain_to_young_bureau_head | Hwaran | urgent and familiar | Calls out 화란아 while urgently warning Ju Hwaran before stepping into the confrontation. |
| 주화란 | 혁무진 | rescued_survivor_to_benefactor | Benefactor | formal-deferential | Hwaran includes Mujin among the Benefactors when greeting Taekyung's companions. |
| 주화란 | 청풍 | rescued_survivor_to_benefactor | Benefactor | formal-deferential | Hwaran includes Cheongpung among the Benefactors when greeting Taekyung's companions. |
| 주화란 | 송일섬 | bureau_head_to_escort_captain | Captain Song | formal and prosecutorial | Uses his office title, then his personal name, while exposing and confronting him. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 매종학 | 적천강 | long-standing martial rival and friend | Great Hero Jeok | casual and familiar | Mae addresses Jeok as 적 대협 while discussing the Alliance Leader position. |
| 적천강 | 매종학 | long-standing martial rival and friend | you | blunt and familiar | Jeok addresses Mae as 당신 while recalling their meeting at Mount Jiuhua. |
| 주화란 | 사마표 | former_fiancés | Young Sect Leader | formal and guarded | Hwaran formally greets her former fiancé. |
| 사마표 | 태산 | Young Sect Leader to subordinate | Taishan | informal and patronizing | Sama Pyo calls Taishan by name while ordering him to leave. |
| 태산 | 사마표 | subordinate to Young Sect Leader | Lord | crude and deferential | Taishan uses 주군 while obeying Sama Pyo. |
| 청풍 | 매종학 | grandson to grandfather | Grandpa | casual-familiar | Repeatedly calls Mae Jonghak 할아버지 while mistaking the Alliance Leader's summons as a family visit. |
| 일양노 | 혁무진 | prospective recruit to interviewer | you | courteous and controlled | Ilyang tells Mujin to report that he wishes to meet Taekyung. |
| 적천강 | 일양노 | Fire Gate Sect Leader to hostile prospective recruit | bastard | blunt and violently contemptuous | Jeok recognizes Ilyang's intent and attacks him after calling him a backstabbing bastard. |
| 사마표 | 적천강 | Young Sect Leader to legendary elder | Great Hero Jeok | formal-deferential | Sama Pyo formally pays his respects to Jeok Cheongang as the Fire King. |
| 태산 | 적천강 | subordinate of a Young Sect Leader to legendary elder | Fire King | clipped, childlike, and deferential | Taishan gives his awkward greeting and expresses admiration for Jeok's strength. |
| 적천강 | 사마표 | legendary elder to unorthodox Young Sect Leader | you / young brat | blunt, suspicious, and contemptuous | Jeok addresses Sama Pyo with 네놈 and 어린놈 while probing his lineage and motives. |
| 적천강 | 태산 | legendary elder to giant subordinate | you / strange fellow | blunt, startled, and grudgingly tolerant | Jeok addresses Taishan as 네놈 while reacting to his greeting and appetite. |

## Listed compact profiles

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 542
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, the grandson and Disciple of Sword Saint Mae Jonghak, a Supreme Peak martial master known as the Huashan Divine Dragon, the creator of the snake-inspired Mimi Step footwork technique, and now one of the two pavilion masters of the Alliance Leader's direct Two Dragons Pavilion.
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, a deep love of martial arts, competitive pride, unusual resistance to monster-induced Fear, and discomfort when someone copies his martial arts.
- **Voice:** Dreamy and hazy, with innocent, polite phrasing; he has begun imitating Taekyung's profanity.
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions while Taekyung is his only true martial rival; Tang Sadok has temporarily entrusted Mimi, now a large horned snake, to him, Mungyeong recently examined her condition, and Mungyeong accepted Cheongpung's offer to accompany him after Cheongpung pledged to learn by observation rather than formal instruction.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 542
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 542
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers and Vice Squad Leader of the Jin Dragon Squad.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 542
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, and Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Ju Hwaran.md

# Ju Hwaran (주화란)

- **Safe through:** Chapter 534
- **Aliases:** Hwaran
- **Role:** Level 88 Young Bureau Head and leader of the Yongbong Escort Bureau, responsible for its personnel and contracts after Heo Jun’s betrayal and now investigating at least two escort captains suspected of aiding his scheme.
- **Personality:** Intelligent, capable, responsible, filial, composed under pressure, and burdened by intense guilt over the escort journey's deaths.
- **Voice:** Clear, polite, restrained, and determined.
- **Relationships:** Escort King Ju Gongsan was her paternal grandfather and rescued the Guangdong Chen Family’s surviving child, who became Song Ilseom’s grandmother; Ju Hogun is her father, Heo Jun was her uncle, Sama Pyo was her former fiancé in a political engagement she accepted for her father's sake, Song Ilseom is her direct escort, and Jin Taekyung is a trusted ally.

### Mae Jonghak.md

# Mae Jonghak (매종학)

- **Safe through:** Chapter 540
- **Aliases:** Sword Saint
- **Role:** Sword Saint and Cheongpung's grandfather who now serves as the New Murim Alliance's Alliance Leader.
- **Personality:** Playful, easygoing, and teasing, but capable of handling heavy administrative responsibilities efficiently.
- **Voice:** Friendly, casually familiar, and cheerfully teasing, including when greeting old acquaintances and discussing leadership.
- **Relationships:** Cheongpung's grandfather and martial instructor; taught him the Taeeul Miri Palm; secretly entered Huashan while its Sect Leader slept, left a dagger and handwritten note, and then went into hiding, prompting Huashan's search; fought Jeok Cheongang at Mount Jiuhua more than forty years ago and left after their draw; his old friend Hong Dao left him a letter identifying Jin Taekyung as the Morning Star who would drive away darkness.

### Old Man Ilyang.md

# Old Man Ilyang (일양노)

- **Safe through:** Chapter 542
- **Aliases:** Won Cheol
- **Role:** An eighty-five-year-old Supreme Peak master between the orthodox and unorthodox paths who seeks access to the Fire Gate Clan's once-per-generation divine technique.
- **Personality:** Ambitious, calculating, covetous, and willing to exploit the Two Dragons Pavilion and its young master for personal advancement.
- **Voice:** Jovial and courteous in public, with restrained menace beneath his gentle words.
- **Relationships:** He presents himself as a prospective Two Dragons Pavilion recruit but secretly targets Jin Taekyung's Fire Gate inheritance; Jeok Cheongang recognizes him as a threat and has beaten him unconscious.

### Sama Pyo.md

# Sama Pyo (사마표)

- **Safe through:** Chapter 542
- **Aliases:** Black Dragon Saber
- **Role:** Young Sect Leader of the Black Dragon Demon Gate and a Morning Star reputed to be no less than the Ten Dragons and Phoenixes.
- **Personality:** Outwardly courteous and smiling, inwardly calculating, but genuinely protective of Taishan and willing to redirect blame onto his subordinate.
- **Voice:** Polite and ingratiating in public, with sardonic humor and controlled evasiveness.
- **Relationships:** Sama Pyo commands the absolutely loyal Taishan, is Sima Gong's son, was Ju Hwaran's former fiancé in a political engagement, and has applied to join the Two Dragons Pavilion while openly intending to use Jin Taekyung as a useful card.

### Sima Gong.md

# Sima Gong (사마공)

- **Safe through:** Chapter 542
- **Aliases:** Black Night King
- **Role:** Sima Gong is the Sect Leader who built the Black Dragon Demon Gate into a major unorthodox power and the father of its Young Sect Leader, Sama Pyo.
- **Personality:** Sly, cunning, and inscrutable, with a ruthless reputation for valuing talent above family ties.
- **Voice:** Not established.
- **Relationships:** Sama Pyo is his youngest son among seven older brothers and nine older sisters, and he is the father of the current Black Dragon Demon Gate Young Sect Leader.

### Song Il.md

# Song Il (송일)

- **Safe through:** Chapter 534
- **Aliases:** Roaring Fury Swordsman
- **Role:** Elder of the Zhongnan Sect and the Roaring Fury Swordsman; senior brother of Sect Leader Gong Iljung; came to the Jin Family of Taiyuan to demand redress for Gong Ilhyuk's injury and the alleged insult to Zhongnan; attacked Jin Taekyung with the Heavenly River Thirty-Six Swords, was stopped by Jeok Cheongang, and was publicly humiliated by him.
- **Personality:** Arrogant, domineering, punitive, and confident in his martial power and seniority.
- **Voice:** Gruff, cutting, condescending, and threatening, with formal authority used to pressure those beneath him.
- **Relationships:** Gong Iljung is his junior Sect Leader and martial younger brother; Gong Ilhyuk is a junior Disciple of his sect; he recognizes Baek Museong and Cheongpung through their Huashan and Sword Saint connections.

### Song Ilseom.md

# Song Ilseom (송일섬)

- **Safe through:** Chapter 534
- **Aliases:** Escort Captain Song
- **Role:** Level 110 young escort captain of the Yongbong Escort Bureau and one of its Dragon-Phoenix Three Escorts who developed his martial ability on battlefields, was known as the Soul-Chasing Guest ten years ago, and plans to remain one more month to help Ju Hwaran purge traitors before seeking an elixir for Ju Hogun in Xianyang.
- **Personality:** Blunt, decisive, survival-hardened, and dryly self-aware, with little patience for insults or disorder.
- **Voice:** Forceful and urgent in command, with a rough and confrontational edge.
- **Relationships:** He serves under Ju Hwaran, is Song Pyosan’s son, and his grandmother was the surviving Guangdong Chen child rescued by Ju Gongsan during the Great Faction War.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 542
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord.

## Korean source

```text
＃543화



쿵. 쿵.

지축을 울리는 발걸음에 길을 지나가던 사람들이 좌우로 길을 텄다.

그리고 그들의 경계 어린 눈빛이 자신의 옆에 있는 태산의 존재 때문이 아님을, 흑룡도 사마표는 알고 있었다.

‘우리에 관한 소문이 꽤 퍼진 모양이로군.’

하긴, 알려지지 않는 것이 이상한 일이다.

옆 골목 담벼락에 기대어 꾸벅꾸벅 졸고 있는 거지의 허리춤에는 누렇게 찌든 매듭이 삐죽 튀어나와 있고, 날아드는 파리를 쫓는 좌판 상인의 손바닥에는 희미한 굳은살이 박여 있었다.

‘개방, 하오문.’

당장 눈에 보이는 것만 해도 이 정도다.

하남 어디를 가도 수많은 이목이 지켜보는 상황이니 아마 오늘 자신의 행보도 반나절이 채 지나기도 전에 여러 인물에게 알려질 것이 분명했다.

‘숨길 생각도 없었지만.’

감추고자 하면 더욱 큰 의심을 살 뿐이다. 사마표는 어쭙잖은 조심성으로 일을 망칠 생각은 추호도 없었다.

- 저기, 주군.

조심스러운 태산의 전음이 귓가를 파고든다. 사마표는 내색하지 않으며 한구석에 자리한 소면 가게를 가리켰다.

“오늘따라 소면이 당기는구나. 어찌, 한 그릇 하고 가겠느냐?”

“으응?”

“배가 부른 녀석이로군. 싫으면 말거라.”

“아니다! 태산이, 소면 좋다!”

“진작 그럴 것이지. 이보시오. 소면 열 그릇…… 아니, 스무 개만 말아 주시오.”

주인인 중년 아낙이 귀를 의심하는 표정으로 되물었다.

“……몇 그릇이라고 하셨습니까?”

사마표가 굳이 소면 가게를 택한 이유는 간단했다.

목이 좋지 않아서인지 손님도 없었고, 다른 사람의 이목을 등진 채 전음을 나눌 수 있기 때문이었다.

물론 주인장이 무림과는 아무 연관도 없어 보이는, 평범한 양민이라는 점도 한몫했다.

“스무 그릇이라고 했소. 보시다시피 아귀(餓鬼) 같은 놈이 하나 있어서.”

“아, 아, 예!”

그에게는 때아닌 횡재였을 것이다. 눈을 번쩍 뜬 주인장이 바쁘게 손을 놀리는 동안 사마표는 입술을 달싹였다.

- 할 말이 있던 것 같은데.

육중한 무게를 지탱하고 있는 작은 의자가 삐걱거린다. 위태롭게 자세를 잡은 태산이 답했다.

- 주군. 태산이. 불안하다.

- 무엇이?

- 무, 문주님의 명을 따르지 않았다. 태산이. 주군 걱정된다.

순간 사마표의 입가에 고소가 맺혔다.

- 설마 했는데, 역시 그분 때문이었느냐.

- 불복하면 좋지 않다. 문주님 화낸다. 주군 위태롭다.

- 그래, 능히 그러고도 남으실 분이지.

사마표는 탁자 위에 가지런히 놓인 젓가락을 내려다보았다.

문득 자신의 아버지인 흑야왕 사마공이 생각난다. 자식을 향한 부정(父情) 따위는 없는 분.

아마도 그의 아비는 자식을 이 젓가락처럼 생각하고 있을 것이다.

‘땅에 떨어지면 바꾸고, 마음에 안 들면 치우고.’

일곱 명의 형과 아홉 명의 누이 역시 그렇게 버려졌다. 사마표는 흑룡마문의 문주가 택한 마지막이자, 가장 잘 만들어진 젓가락이었다.

‘그마저도 언제 바뀔지 모르지.’

이미 팔순을 훌쩍 넘긴 노인이지만 식욕도, 성욕도 왕성한 아버지다.

삼처사첩(三妻四妾)으로도 모자라 열 명이 넘는 첩을 두었으니 위로도, 밑으로도 피가 이어진 혈육이 수두룩했다.

하지만.

- 걱정 말거라.

- 으응?

사마표는 주인장이 내놓은 미지근한 물을 한 모금 삼켰다.

- 비정하신 분이지만, 그렇기에 나를 쉽게 내치지 못할 테니.

흑야왕 사마공은 분명 비정한 사람이다. 그러니 부모의 정 따위는 내다 버린 채 현실을 냉정히 바라볼 수 있었다.

소싯적의 자신을 뛰어넘는 무재(武才)와 깊은 심계(審計)를 지닌 사마표를 대체할 후계자는 없다는 것 역시 같은 맥락이었다.

그리고…….

- 아무런 문책도 없을 게다. 길이 달라졌을 뿐, 이것 역시 아버지가 원하는 곳을 향하고 있으니까.

- 주군. 이해 안 된다. 태산이 머리 나쁘다.

자신이 한 말을 이해하지 못해 고개만 갸웃거리는 태산을 향해, 사마표는 빙긋 웃어 보였다.

- 굳이 이해할 필요 없으니, 내 옆에만 있거라. 알겠느냐?

- 태산이. 주군 말 듣는다. 착하다.

태산이 힘차게 고개를 끄덕인 그때, 주인장이 소면이 가득 담긴 그릇들을 탁자에 올려놓기 시작했다.

“뜨거우니 천천히…….”

“우와! 태산이! 잘 먹겠습니다!”

“에그머니나!”

깜짝 놀라는 주인장과 김이 펄펄 나는 소면을 그릇 채 들고 삼키는 태산.

그 모습을 바라보며 피식 웃던 사마표의 얼굴이, 순간 딱딱하게 굳었다.

“음.”

정신없이 젓가락을 놀리던 태산이 고개를 쳐들었다.

“주군. 왜 그러나?”

“…….”

“주군?”

태산의 물음에도 말없이 어딘가를 응시하던 사마표가 작게 중얼거렸다.

“아니다. 아무것도. 잘못 본 모양이야.”

하지만 사마표는 알고 있었다. 스치듯 지나쳐 간 한 사람의 모습은 결코 잘못 본 것이 아니라는 것을.

그리고 그것이 무엇을 의미하는지를.

“……그냥 고분고분하게 명을 따를 걸 그랬나.”

“응? 주군. 뭐라고 했나?”

사마표는 대답 대신 한숨을 내쉬었다. 어느새 태산의 손에는 마지막 그릇이 들려 있었다.

“염치도 없는 녀석 같으니. 마저 처먹어라.”

“와! 태산이! 주군을 위해 목숨을 바친다!”



* * *



“자, 여기요.”

영창 피아노보다 맑고 고운 목소리. 이쪽을 향해 불쑥 내민 손에는 두 개의 죽간이 들려 있다.

‘이게 무슨 상황이지.’

흑룡마문의 두 불청객이 떠나고, 적천강이 측간에 간 지 불과 한 식경도 되지 않은 상황.

또다시 찾아온 뜻밖의 손님은 갑작스러운 것을 넘어 당황스럽기까지 하다.

말없이 눈만 깜빡이던 나는 간신히 목소리를 끄집어냈다.

“이……게 뭡니까?”

“지원서죠.”

당연한 걸 왜 묻느냐는 표정으로 대답한 주화란이 덧붙였다.

“저와 여기 있는 송 호위의 것까지 두 개예요.”

뒤에 서 있던 송일섬이 작게 중얼거렸다.

“난 동의한 적 없는데.”

“제가 고용했잖아요. 호위라면 당연히 따라와야죠.”

“이런 상황은 항목에 없었잖소. 계약 위반이오. 무림맹에 속하게 되면 위험 수당이…….”

“두 배 더 드릴게요.”

“그럼 이야기가 달라지지.”

종남파한테 뜯어 낸 돈이 많아서 그런가, 영 앤 리치의 시원시원한 플렉스를 보여 주는 주화란이다.

물론 지켜보는 나로서는 한여름 온실에 들어온 것처럼 갑갑했지만.

“그럼. 정말로?”

“네. 정말로.”

내 물음에 망설임 없이 고개를 끄덕인 주화란이 투명한 눈동자로 나를 응시했다.

“이룡각에 들어가고 싶어요.”

“……!”

짐작은 했지만, 막상 주화란에게서 직접 듣자 입 안이 까끌거렸다. 잠시 생각하던 나는 입을 열었다.

“인연이 있다고 해서 받아 줄 생각은 없습니다.”

“처음부터 그럴 생각이었다면 지원서도 없이 왔겠죠?”

싱긋 웃으며 대답하는 주화란의 모습에 내심 한숨이 흘러나왔다.

“위험할 겁니다. 그것도 매우.”

“이미 알고 왔어요. 맹주부 직속에, 다른 각주들과는 달리 휘하에 단과 대도 거느리지 못하는 이룡각. 아마 별동대의 성격이 강하겠죠.”

정답이다.

매종학은 무림맹 내부에서도 상당한 전력인 나와 청풍을 소규모 별동대로 운용하길 바랐고, 그것은 대다수의 수뇌부가 고개를 끄덕이게 만든 이유이기도 했다.

“주 소저, 그걸 알면서도 왜…….”

“진 대협.”

내가 말을 끝맺기도 전에, 주화란이 불쑥 입을 열었다.

“다른 지원자들에게도 그렇게 말씀하셨나요?”

“네?”

“위험하다. 알면서도 왜 지원하느냐.”

나직한 목소리가 이어졌다.

“이상하네요. 사람이 필요해서 방을 붙이셨을 텐데, 이렇게 만류하시니.”

“그건…….”

망설이는 나를 보며 주화란이 피식 웃었다.

“할 말 없으시죠?”

정곡이다. 뒤통수를 긁적인 나는 어쩔 수 없이 고개를 끄덕였다.

“솔직히, 예. 그러네요.”

“저는 이곳에 한 사람의 무인으로 왔으니, 진 대협께서도 있는 그대로를 봐 주셨으면 좋겠네요.”

“있는 그대로라…….”

“진 대협 눈에는 턱없이 부족할지 모르겠지만, 저 역시 절정의 경지에 오른 검객이에요.”

“기왕 솔직한 거, 터놓고 말씀드리면 많이 부족하긴 합니다. 송일섬. 저 녀석이라면 모를까.”

쿡.

숨죽인 채 상황을 지켜보던 혁무진이 슬쩍 옆구리를 찔렀다.

하지만 그건 녀석의 과한 우려에 불과하다. 그 증거로, 내 직설적인 말에도 주화란의 눈빛은 흔들리지 않았다.

“다른 지원자들에 비해서도 그런가요?”

“글쎄요. 장담할 수는 없지만 아마 그럴 겁니다.”

“경험은요?”

“경험?”

“저는 열두 살 때부터 아버지를 따라 표행(鏢行)을 나갔어요. 연륜과 천하의 지리에 관해서는 여느 노강호와 비교해도 떨어지지 않는다고 생각해요.”

맞다. 주화란은 한때 천하에서도 손꼽히던 용봉표국의 후계자였다.

근 몇 년 동안은 주화입마로 쓰러진 아버지 대신 직접 표국을 이끌기도 했다.

‘그를 통해 얻은 경험은…… 확실히 무시 못 하지.’

표국은 천하 곳곳을 방랑하는 집단이다. 의뢰를 기간에 맞춰 완수하기 위해 수단과 방법을 가리지 않는 그들은 천하 곳곳의 길과 정보를 알고 있다.

하물며 주화란의 조부인 표왕(鏢王)은 과거 정마대전 당시, 마교의 수많은 이목을 피해 만리행(萬里行)을 성공시키기도 했었다.

“진 대협.”

힘 있는 목소리가 귓가를 파고들었다.

“짐이 될 생각은 추호도 없어요. 다만 진 대협께서도 냉정하게 생각해 주세요. 지금까지 있었던 모든 인연을 떠나, 저와 여기 있는 송 호위가 정말 이룡각에 필요 없는 존재인지.”

“……!”

“각오는 충분히 했어요. 떨어트리신다고 해도 감수할게요.”

나는 지그시 눈을 감았다.

주화란의 말이 맞다. 이건 냉정하게 생각해야 할 문제다.

지금 내 대답을 기다리고 있는 사람은 어느 날 밤, 이제 막 꽃을 피우기 시작한 정원에서 함께 걷던 여인이 아니었다.

‘은비화(隱匕花) 주화란.’

십봉룡으로 인정받을 만큼 상당한 무위를 지닌 한 사람의 무인이고, 용봉표국의 소국주다.

게다가 사실상 별동대나 다름없는 이룡각의 향후 임무 수행에 필요한 여러 가지 능력을 갖추기도 했다.

‘그런데 왜일까.’

그 사실을 인정하기 싫은 이유는. 억지를 부려서라도 만류하고 싶은 이 기분은.

“저어, 조장님.”

귓가를 파고드는 목소리에, 나는 감았던 눈을 떴다. 눈치를 살피던 혁무진이 우물쭈물 말을 이었다.

“그, 한 가지 잊으신 모양인데요.”

“뭐?”

“지금 다른 지원자들 싹 다 도망가고 없습니다. 아마 내일도, 모레도 마찬가지일걸요.”

“나도 알아, 인마. 일양노가 반신불수가 돼서 실려 나갔으니까. 그래서?”

“아니, 뭐. 그렇다는 거죠. 제가 드리고 싶은 말씀은 여기까집니다.”

움찔한 혁무진이 슬쩍 고개를 돌린다.

하지만 녀석이 한 말의 의미는 충분히 전해지고도 남았다.

“후.”

한숨을 내쉰 나는 주화란을 똑바로 응시했다.

“제가 대답하기 전에, 주 소저께서 한 가지 아셔야 할 부분이 있는데요.”

이 말을 어떻게 꺼내야 하나. 머뭇거리는 내게 주화란이 싱긋 웃어 보였다.

“상관없어요.”

“네?”

“오는 길에 봤거든요. 그 정도 덩치와 함께 있는데 눈에 안 띄는 게 이상하죠. 어디에 다녀오는 길인지는, 사람들이 수군거리는 말을 들어 보니 대충 알겠더라고요.”

주화란이 차분한 목소리로 말을 이었다.

“그런데, 그게 무슨 문제가 되나요?”

“……!”

“생각할 시간은 충분히 드린 것 같은데. 이제 대답을 들을 수 있을까요?”

나는 주화란을 물끄러미 응시했다. 복잡하던 머릿속이 깔끔하게 정리된 기분이다.

아니, 어쩌면 아직은 정리가 덜 끝났을 수도 있겠지.

하지만 적어도 지금만큼은, 내가 해야 할 대답을 알고 있었다.

“네. 좋습니다.”

주화란의 얼굴 위로, 환한 웃음이 번졌다.
```

## Final English reading copy

```markdown
# Chapter 543

Thud. Thud.

At the thunderous footsteps that shook the earth beneath them, pedestrians moved aside and cleared a path.

And Black Dragon Saber Sama Pyo knew that the wary looks they were receiving were not because of Taishan walking beside him.

*It seems the rumors about us have spread quite a bit.*

That was only natural. It would have been stranger if they had not spread.

A yellowed, grimy knot protruded from the waist of a beggar dozing against a wall in the alley beside them. The palm of a stallkeeper swatting at flies bore faint calluses.

*The Beggars’ Sect. The Lower District Sect.*

That was only what he could see at a glance.

No matter where they went in Henan, countless eyes were watching them. There was no doubt that today’s movements would be reported to various people before even half a day had passed.

*Not that I intended to hide them.*

Trying to conceal himself would only raise greater suspicion. Sama Pyo had no intention of ruining things through half-baked caution.

*—My lord.*

Taishan’s cautious Sound Transmission pierced his ears. Without revealing anything, Sama Pyo pointed toward a small noodle shop tucked away in one corner.

“Thin noodles sound good today. How about a bowl before we go?”

“Hm?”

“You must have a full belly. If you don’t want any, say so.”

“No! Taishan likes noodles!”

“You should have said so from the beginning. Excuse me. Ten bowls of thin noodles—no, make that twenty.”

The middle-aged woman running the shop looked as though she doubted her ears.

“……How many bowls did you say?”

Sama Pyo had chosen the noodle shop for a simple reason.

Perhaps because it was in an inconvenient location, there were no other customers, allowing them to exchange Sound Transmissions with their backs turned to everyone else.

It also helped that the owner appeared to be an ordinary commoner with no connection to the Murim.

“Twenty bowls. As you can see, I have a hungry ghost with me.”

“Y-Yes!”

It must have been an unexpected windfall for her. While the woman’s eyes lit up and her hands moved busily, Sama Pyo’s lips barely moved.

*—You seemed to have something to say.*

The small chair creaked beneath the massive weight it supported. Taishan, precariously balanced on it, answered.

*—My lord. Taishan. Worried.*

*—About what?*

*—Did not obey Sect Leader’s orders. Taishan. Worried about my lord.*

A bitter smile formed at the corners of Sama Pyo’s mouth.

*—I wondered if that might be the reason. So it was because of that person after all.*

*—Disobeying bad. Sect Leader angry. My lord in danger.*

*—Yes. He is more than capable of that.*

Sama Pyo looked down at the chopsticks neatly arranged on the table.

His father, Black Night King Sima Gong, came to mind. He was a man utterly devoid of paternal affection.

*He probably thinks of his children the way he thinks of these chopsticks.*

*Replace them when they fall to the ground. Set them aside when they no longer please him.*

His seven older brothers and nine older sisters had all been discarded in the same way. Sama Pyo was the final—and best-crafted—chopstick the Sect Leader of the Black Dragon Demon Gate had chosen.

*Though I have no idea when even I might be replaced.*

His father was already well past eighty, yet he still possessed a vigorous appetite and an equally vigorous libido.

Three wives and four concubines had not been enough for him. He had taken more than ten concubines, leaving Sama Pyo with countless blood relatives both older and younger than himself.

And yet—

*—Don’t worry.*

*—Hm?*

Sama Pyo swallowed a mouthful of the lukewarm water the owner had brought him.

*—He is heartless. That is precisely why he cannot easily cast me aside.*

Black Night King Sima Gong was certainly a cruel man. That was why he could discard any notion of parental love and look at reality with such cold clarity.

By the same logic, there was no other successor who could replace Sama Pyo, whose martial talent surpassed even Sima Gong’s in his younger days and whose calculating mind ran deep.

And—

*—There will be no punishment. The route has merely changed; this still leads toward the destination my father wants.*

*—My lord. Taishan does not understand. Taishan is stupid.*

Sama Pyo smiled faintly at Taishan, who only tilted his head in confusion.

*—You don’t need to understand. Just stay by my side. Do you understand?*

*—Taishan listens to my lord. Taishan is good.*

Just then, Taishan nodded vigorously, and the owner began setting bowls piled high with thin noodles on the table.

“Careful, they’re hot. Take it slow—”

“Wow! Taishan! Thank you for the food!”

“Oh my goodness!”

The owner stared in shock as Taishan lifted an entire bowl of steaming noodles and gulped them down.

Sama Pyo let out a quiet laugh at the sight.

Then his face suddenly stiffened.

“Hmm.”

Taishan, who had been working his chopsticks without pause, raised his head.

“My lord. What is it?”

“……”

“My lord?”

Sama Pyo continued staring at something in silence before murmuring under his breath.

“No. It’s nothing. I must have seen wrong.”

But Sama Pyo knew that the person who had passed by in a fleeting glimpse was not a mistake.

And he knew what that meant.

“……Perhaps I should have just obeyed the orders without complaint.”

“Hm? My lord. What did you say?”

Sama Pyo answered with a sigh instead. By then, Taishan was holding the final bowl.

“You shameless glutton. Finish stuffing your face.”

“Wow! Taishan will give his life for my lord!”

* * *

“Here you go.”

The voice was clear and lovely, more beautiful than a Young Chang piano.[^1] Two bamboo slips were held out toward me.

*What is going on?*

Less than half an hour had passed since the two uninvited guests from the Black Dragon Demon Gate had left and Jeok Cheongang had gone to the latrine.

The unexpected guest who had arrived was not merely sudden. She was downright disconcerting.

I blinked at her wordlessly, then barely managed to squeeze out a voice.

“W-What are these?”

“Applications.”

Ju Hwaran answered with an expression that seemed to ask why I was questioning the obvious, then added,

“One for me and one for Captain Song.”

Song Ilseom, standing behind her, muttered under his breath.

“I never agreed to this.”

“I hired you, didn’t I? If you’re my escort, of course you have to come with me.”

“That sort of situation wasn’t included in the contract. It’s a breach of contract. If I join the Murim Alliance, I’ll need hazard pay……”

“I’ll pay you double.”

“Then that’s a different story.”

Perhaps it was because she had wrung so much money out of the Zhongnan Sect, but Ju Hwaran was putting on a brisk young-and-rich flex.

Of course, watching her made me feel as stifled as if I had stepped into a greenhouse in midsummer.

“So. Really?”

“Yes. Really.”

Ju Hwaran nodded without hesitation and stared at me with clear eyes.

“I want to join the Two Dragons Pavilion.”

“……!”

I had more or less expected it, but hearing it directly from Ju Hwaran still left a gritty taste in my mouth. After thinking for a moment, I opened my lips.

“I have no intention of accepting you simply because we have a connection.”

“If I’d planned to rely on our connection from the start, I would’ve come without an application, wouldn’t I?”

A faint smile crossed Ju Hwaran’s face, and I sighed inwardly.

“It will be dangerous. Very dangerous.”

“I know. The Two Dragons Pavilion is directly under the Alliance Leader’s Office, and unlike the other pavilions, it cannot even command its own squads or battalions. It will probably function more like a special operations detachment.”

That was exactly right.

Mae Jonghak wanted to use Cheongpung and me, both considerable assets even within the Murim Alliance, as a small special operations detachment. That was also why most of the Alliance’s leadership had nodded along with the idea.

“Young Lady Ju, if you know that, then why—”

“Great Hero Jin.”

Before I could finish, Ju Hwaran cut in.

“Did you say that to the other applicants as well?”

“What?”

“‘It’s dangerous. Why apply when you know that?’”

Her quiet voice continued.

“That’s strange. You put up a notice because you needed people, yet you’re discouraging them like this.”

“That’s……”

As I hesitated, Ju Hwaran let out a quiet laugh.

“You have nothing to say, do you?”

She had hit the nail on the head. I scratched the back of my head, then nodded reluctantly.

“To be honest, yes. I suppose I don’t.”

“I came here as a martial artist in my own right, so I hope you will look at me as I am.”

“As you are……”

“You may think I’m far from enough for you, Great Hero Jin, but I am also a swordswoman who has reached the Peak realm.”

“Since we’re being honest, if we’re laying it all out, you are indeed lacking. Song Ilseom might be a different story.”

Hyuk Mujin, who had been watching the situation with bated breath, gave me a subtle poke in the ribs.

But that was only unnecessary worry on his part. As proof, Ju Hwaran’s gaze did not waver even at my blunt words.

“Even compared with the other applicants?”

“I can’t guarantee it, but you probably are.”

“What about experience?”

“Experience?”

“I began going out on escort runs with my father when I was twelve. I don’t think I fall short of any old hand in the martial world when it comes to experience or knowledge of the land.”

That was true. Ju Hwaran had once been the successor to the Yongbong Escort Bureau, one of the most renowned escort bureaus in the world.

For the past several years, she had even led the bureau herself in place of her father, who had collapsed from qi deviation.

*The experience she gained from that can’t be dismissed.*

Escort bureaus were groups that roamed every corner of the land. To complete their contracts within the appointed time, they used every means and method available to them. As a result, they possessed knowledge of the roads and information found throughout the world.

Moreover, during the Great Faction War, Ju Hwaran’s grandfather, the Escort King, had successfully completed a journey of ten thousand li while evading the Demonic Cult’s countless eyes.

“Great Hero Jin.”

Her powerful voice pierced my ears.

“I have no intention of becoming a burden. But please think about this coldly as well. Setting aside every connection we’ve had until now, are Captain Song and I truly people the Two Dragons Pavilion has no need for?”

“……!”

“I’m fully prepared for what this entails. Even if you reject me, I’ll accept it.”

I slowly closed my eyes.

Ju Hwaran was right. This was something I had to consider coldly.

The person waiting for my answer was not the woman I had once walked beside at night through a garden where the flowers had only just begun to bloom.

*Dagger Hidden Flower Ju Hwaran.*

She was a martial artist whose abilities were enough to earn recognition as one of the Ten Dragons and Phoenixes, as well as the Young Bureau Head of the Yongbong Escort Bureau.

On top of that, she possessed various abilities that would be needed for the Two Dragons Pavilion’s future missions, which were effectively bound to be those of a special operations detachment.

*So why?*

Why did I hate admitting that fact?

Why did I feel like insisting on stopping her, even if I had to be unreasonable?

“Um, Captain.”

At the voice piercing my ears, I opened my eyes. Hyuk Mujin watched my reaction nervously before continuing.

“I think you’ve forgotten one thing.”

“What?”

“All the other applicants have run away. Every last one of them. It’ll probably be the same tomorrow and the day after.”

“I know, you punk. Old Man Ilyang was carried away half-paralyzed. So what?”

“No, I mean, that’s all I wanted to say.”

Hyuk Mujin flinched and subtly turned his head away.

But the meaning behind his words had come through loud and clear.

“Whew.”

I sighed and looked straight at Ju Hwaran.

“Before I answer, there’s one thing you should know, Young Lady Ju.”

How was I supposed to bring this up? As I hesitated, Ju Hwaran gave me a faint smile.

“It doesn’t matter.”

“What?”

“I saw it on my way here. With someone that large beside you, it would be strange if you didn’t attract attention. From the things people were whispering, I was able to roughly figure out where you were coming from.”

Ju Hwaran continued in a calm voice.

“But why would that be a problem?”

“……!”

“I think I’ve given you plenty of time to think. May I hear your answer now?”

I stared at Ju Hwaran. It felt as though the tangled mess in my head had been neatly sorted out.

No. Perhaps it was not completely sorted out yet.

But at least for now, I knew what answer I had to give.

“Yes. That’s fine.”

A radiant smile spread across Ju Hwaran’s face.

[^1]: Young Chang is a Korean piano manufacturer.
```

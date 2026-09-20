<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0542.txt",
      "sha256": "e46358bd7eac983c14685e301da68f2888ea38b9634e9928df61c6c09973a721",
      "bytes": 13439
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "6412986700ba83db5787866e2fd3242fc68bcf1aeddc3af637a47357af444bb0",
      "bytes": 4260
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "d1c4060ac7daf3df93b5111e95cfe8de7e90ee158ed41150a99b08c056fe5ab6",
      "bytes": 171553
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "1b38a5e37967f78d54ab87cdb84f2f07d790743eb2c98cc74597ec19e1b7abbb",
      "bytes": 1370
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "8ccf990b439b20e5a2f6edc0e0ea7782f3bfce6276667a98339db7ab1e968550",
      "bytes": 553
    },
    {
      "path": "characters/Gung Gibang.md",
      "sha256": "cf3e0becf8178f2a4a4276bbab86c06197ff4e6d841d114adb27e7c5fd112405",
      "bytes": 686
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "af512404c51f8ff077b5881d87bb828b857f9d87ec3666cf58417ab37d26e3f4",
      "bytes": 1108
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "081ae5762a71d086bdc61577504e2be8d361dafa6a9a88ea78cddf69d439c270",
      "bytes": 1630
    },
    {
      "path": "characters/Old Man Ilyang.md",
      "sha256": "4334556169875ff82b098afdbb1f8892a77811f17b9833fdf97680dec85631e2",
      "bytes": 793
    },
    {
      "path": "characters/Sama Pyo.md",
      "sha256": "d9ebe864e2969e5c71cc36d4a3b8963da1d0faf8861f8d1f76cbfd2c52be294c",
      "bytes": 768
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "3dbcd4c86dc77ea7a3871352f5fd02818d765c00f7d1d2116110c83dd67f469f",
      "bytes": 487
    },
    {
      "path": "characters/Unnamed.md",
      "sha256": "fff29cf5e9eeda97b57cd5686322f664dea55e837f40e53a7384522fa49c7681",
      "bytes": 750
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "c09d1fcd0c786f2a096c5530f00dab471342d206a6cd158c8f16764da92bdae4",
      "bytes": 163205
    }
  ],
  "estimated_tokens": 12435
}
-->

# Durable State Update — Chapter 542

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 542. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 542. Profile updates may replace only one
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
  "chapter": 542,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 542,
    "continuity_sources": [542],
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
    "Mae Jonghak formally appointed Jin Taekyung and Cheongpung as the two pavilion masters of the Alliance Leader's direct Two Dragons Pavilion, and their appointments are now public throughout Henan.",
    "Tang Sadok and the Sichuan Tang Clan publicly support Jin Taekyung and Cheongpung and acknowledge an unrepayable debt to them.",
    "Taekyung believes the Zhongnan Sect resents him, the Jin Family of Taiyuan, and Jeok Cheongang after its repeated humiliations and will obstruct them.",
    "Cheongpung created Mimi Step from Mimi's movements; it is a snake-like footwork technique fast enough that Taekyung could barely track it with his naked eyes, and Mungyeong recognizes Cheongpung as having the makings of a Grandmaster.",
    "Mimi is now a large horned snake under Cheongpung's care, eats dumplings, sweets, and Blood Fish, and has recently had her condition examined by Mungyeong.",
    "Mungyeong ended Taekyung's direct training and assigned him a final task of incorporating martial principles into his learned martial arts.",
    "Zhuge Feng's Demon-Sealing Formation still blocks all mana from the exposed Gate, while Jang Taebo is summoning artisans to process the Water God Dragon's remains.",
    "The Southern Heaven Demon Empress is traveling toward Yunnan and expects to cause further deaths.",
    "The Black Dragon Demon Gate remains a major unorthodox power descended from the Demonic Cult's Twelve Branches; Sama Pyo is its Young Sect Leader and Black Dragon Saber, and Taishan is his giant subordinate.",
    "Jin Taekyung remains a Supreme Peak master with Three Flowers Gather at the Crown, advanced qi perception, exceptional resistance to monster Fear, and public S-rank-level recognition despite retaining an A-rank license.",
    "The System has assigned Taekyung's first Two Dragons Pavilion Quest: recruit at least five companions and name the organization, or receive the Title Loner. Mungyeong has accepted Cheongpung's offer, and the recruitment interviews have drawn a huge crowd; Jeok Cheongang's attack on Old Man Ilyang has driven many applicants away."
  ],
  "continuity_sources": [
    541,
    540
  ],
  "open_questions": [
    "What is the Lord of Heaven's identity, how is he connected to the dangerous force Taekyung associates with his original world, and how can Dark Heaven open Gates?",
    "Where is the Southern Heaven Demon Empress ultimately headed, and what does she intend to do in Yunnan?",
    "What is the outcome of the duel between Jeok Cheongang and Nangong Cheon, the Azure Sky Sword King?",
    "Why did Ju Hwaran and Sama Pyo's political engagement end?",
    "Which additional companions will join the Two Dragons Pavilion, what name will it receive, and can Taekyung complete the System Quest after the recruitment disruption?"
  ],
  "safe_through": 541,
  "temporary_decisions": [
    "Render 고월루 as Gowolru, 곤륜운룡 as Kunlun Cloud Dragon, 학우 as Hak Woo, 이룡각 as Two Dragons Pavilion, 협 as chivalry, 인의 as humanity, 협객 as knight-errant, 홍학루 as Honghakru, 홍매 as Hongmae, and 호거아 as Tiger Giant Child; render 전 정혼자 contextually as former fiancé or former fiancée.",
    "Render 탈진 as the capitalized system status Exhaustion; retain Ten Dragons and Phoenixes, Blazing Flame Divine Dragon, Dark Heaven, Murim Alliance, and Old Master.",
    "Render 황보세가 as Hwangbo Family, 소가주 as Lesser Family Head, 은비화 as Dagger Hidden Flower, and 전음 as Sound Transmission.",
    "Preserve the chapter's blunt profanity, financial-therapy humor, monster-comparison humor, and Mae Jonghak's carefree 'That can happen' refrain; render 고잉무림호 as Going Murim ship, 대종사 as Grandmaster, and 왕희지 as Wang Xizhi.",
    "Render 일기천룡 as One-Ride Heavenly Dragon and Taishan's speech as clipped, childlike, and literal; render 일양노 and 열양노 as Old Man Ilyang, 원철 as Won Cheol, 흑혈도 as Black Blood Saber, 노귀산 as No Guisan, and 원썬 as One Sun."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 청풍     | **Cheongpung**     |
| 사마공    | **Sima Gong**      |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 십왕     | **Ten Kings**       |
| 무림맹    | **Murim Alliance**               |
| 암천     | **Dark Heaven**                  |
| 용봉표국   | **Yongbong Escort Bureau**       |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 정파     | **orthodox faction**                             |                                                       |
| 사파     | **unorthodox faction**                           |                                                       |
| 문주     | **Sect Leader**                              |
| 소문주    | **Young Sect Leader**                        |
| 표국     | **Escort Bureau**                            |
| 노부      | **this old man / I**                                            |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 궁기방 | **Gung Gibang** | Beggars' Sect Successor Beggar and finalist. |
| 일양노 | **Old Man Ilyang** | Sobriquet of the eighty-five-year-old Supreme Peak master Won Cheol. |
| 사마표 | **Sama Pyo** | Young Sect Leader of the Black Dragon Demon Gate. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 무명 | **Unnamed** | Dharma name given by Hong Dao; literally means having no name. |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 녹림맹주 | **Green Forest Alliance Leader** | Leader title for the Green Forest Alliance. |
| 사마외도 | **demonic, heterodox arts** | Suspected martial-arts origin of Pung Yang's insidious forms. |
| 야왕 | **Night King** | Rumored epithet for Jin Taekyung in Taiyuan's red-light district. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 녹림맹 | **Green Forest Alliance** | Bandit alliance receiving Black Mountain Stronghold’s tribute. |
| 정력도왕 | **Virility Saber King** | Jeok Cheongang's insulting replacement title for the Thunderbolt Saber King. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 마공 | **demonic martial arts** | Martial arts that appear to defy common principles. |
| 염라 | **Yama** | Buddhist lord of the underworld invoked as the one awaiting the dead. |
| 노야 | **Old Master** | Taekyung's private address for Jeok Cheongang. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 표왕 | **Escort King** | Epithet of Ju Gongsan. |
| 살수 | **assassin** | Professional killer considered as a possible suspect. |
| 염라대왕 | **Yama** | Expanded source form of the established underworld ruler term 염라. |
| 이룡 | **Two Dragons** | Collective ranking beneath the Ten Kings in Murim gossip. |
| 흑룡마문 | **Black Dragon Demon Gate** | Unorthodox faction from Gansu. |
| 흑룡도 | **Black Dragon Saber** | Sama Pyo's sobriquet. |
| 황하 | **Yellow River** | River along which civilization began. |
| 이룡각 | **Two Dragons Pavilion** | Named pavilion whose masters are identified as Taekyung and Cheongpung at the chapter's close. |
| 호거아 | **Tiger Giant Child** | Epithet for Taishan. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 청풍 | 혁무진 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung includes Mujin among his 은인들 after receiving the skewers. |
| 혁무진 | 청풍 | martial artist to young master | Young Master | formal-deferential | Mujin uses 공자께서는 when asking why Cheongpung descended from the mountain. |
| 적천강 | 청풍 | overwhelming_elder_to_young_martial_artist | you / little punk | blunt, amused, and threatening | Jeok Cheongang uses 네, 이놈, and related blunt forms while testing Cheongpung. |
| 청풍 | 적천강 | young_martial_artist_to_overwhelming_elder | Grandpa Jeok | casual-familiar despite deference | Cheongpung uses 적 할아버지 while asking Jeok Cheongang to confirm Taekyung's condition; this is a familial form of address, not literal kinship. |
| 혁무진 | 적천강 | subordinate_to_overwhelming_elder | Great Hero Jeok | deferential and fearful | Mujin uses 적 대협 while reporting Jeok’s orders and Taekyung’s awakening. |
| 적천강 | 혁무진 | overwhelming_elder_to_junior_martial_artist | you stupid fool | blunt and mocking | Jeok calls Mujin a 멍청한 놈 after knocking him down during the attempted escape. |
| 무명 | 적천강 | junior_monk_to_legendary_martial_master | Great Hero Jeok Cheongang | formal-deferential | Identifies Jeok by the title Fire King and the honorific 대협. |
| 혁무진 | 궁기방 | squad_companion_to_Beggars_Sect_successor | Young Hero Gung | formal-polite, then pointed | Uses 궁 소협 while asking about the culprit and challenging Gung’s insults. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 궁기방 | 혁무진 | squad_companions | you; that lunatic | insulting-casual | Gung Gibang mocks Hyuk Mujin's injuries and calls him a lunatic for attacking the Third Fiend. |
| 궁기방 | 청풍 | martial_companions | Young Hero Cheongpung | formal-polite | Gung Gibang uses 청 소협 while asking why Cheongpung is at the temporary clinic. |
| 적천강 | 궁기방 | overwhelming_elder_to_younger_martial_artist | you | blunt and threatening | Jeok Cheongang rebukes Gung Gibang for speaking informally and orders him to lie down. |
| 사마표 | 태산 | Young Sect Leader to subordinate | Taishan | informal and patronizing | Sama Pyo calls Taishan by name while ordering him to leave. |
| 태산 | 사마표 | subordinate to Young Sect Leader | Lord | crude and deferential | Taishan uses 주군 while obeying Sama Pyo. |
| 일양노 | 혁무진 | prospective recruit to interviewer | you | courteous and controlled | Ilyang tells Mujin to report that he wishes to meet Taekyung. |
| 적천강 | 일양노 | Fire Gate Sect Leader to hostile prospective recruit | bastard | blunt and violently contemptuous | Jeok recognizes Ilyang's intent and attacks him after calling him a backstabbing bastard. |

## Listed compact profiles

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 540
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, the grandson and Disciple of Sword Saint Mae Jonghak, a Supreme Peak martial master known as the Huashan Divine Dragon, the creator of the snake-inspired Mimi Step footwork technique, and now one of the two pavilion masters of the Alliance Leader's direct Two Dragons Pavilion.
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, a deep love of martial arts, competitive pride, unusual resistance to monster-induced Fear, and discomfort when someone copies his martial arts.
- **Voice:** Dreamy and hazy, with innocent, polite phrasing; he has begun imitating Taekyung's profanity.
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions while Taekyung is his only true martial rival; Tang Sadok has temporarily entrusted Mimi, now a large horned snake, to him, Mungyeong recently examined her condition, and Mungyeong accepted Cheongpung's offer to accompany him after Cheongpung pledged to learn by observation rather than formal instruction.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 541
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Gung Gibang.md

# Gung Gibang (궁기방)

- **Safe through:** Chapter 535
- **Aliases:** Successor Beggar, Beggar Prince, pure-blooded beggar, ultimate beggar
- **Role:** Gung Gibang is the Beggars' Sect Successor Beggar and a unique eight-knot disciple.
- **Personality:** Vulgar, aggressive, and quick-tempered.
- **Voice:** Blunt, profane, and vividly threatening.
- **Relationships:** Gung Gibang is a rival finalist alongside Baek Woo and Zhuge Gyun who trades insults with Taekyung, uses Beggars’ Sect intelligence to investigate Tang Taesang’s murder and Dark Heaven’s Hubei forces, and has now found a trace of Honglan.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 541
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers and Vice Squad Leader of the Jin Dragon Squad.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 541
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, and Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Old Man Ilyang.md

# Old Man Ilyang (일양노)

- **Safe through:** Chapter 541
- **Aliases:** Won Cheol
- **Role:** An eighty-five-year-old Supreme Peak master between the orthodox and unorthodox paths who seeks access to the Fire Gate Clan's once-per-generation divine technique.
- **Personality:** Ambitious, calculating, covetous, and willing to exploit the Two Dragons Pavilion and its young master for personal advancement.
- **Voice:** Jovial and courteous in public, with restrained menace beneath his gentle words.
- **Relationships:** He presents himself as a prospective Two Dragons Pavilion recruit but secretly targets Jin Taekyung's Fire Gate inheritance; Jeok Cheongang recognizes him as a threat and has beaten him unconscious.

### Sama Pyo.md

# Sama Pyo (사마표)

- **Safe through:** Chapter 534
- **Aliases:** Black Dragon Saber
- **Role:** Young Sect Leader of the Black Dragon Demon Gate and a Morning Star reputed to be no less than the Ten Dragons and Phoenixes.
- **Personality:** Outwardly courteous and smiling, inwardly calculating, but genuinely protective of Taishan and willing to redirect blame onto his subordinate.
- **Voice:** Polite and ingratiating in public, with sardonic humor and controlled evasiveness.
- **Relationships:** Sama Pyo commands the absolutely loyal Taishan, Ju Hwaran was his former fiancée in a political engagement she accepted for her father's sake, and his father previously told him about Jung Ho.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 540
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord.

### Unnamed.md

# Unnamed (무명)

- **Safe through:** Chapter 540
- **Aliases:** None
- **Role:** Unnamed is a young Shaolin monk and practical Disciple of the late Hong Dao who achieved enlightenment after three months of treatment and training in Repentance Cave, becoming a Supreme Peak master and Jung Ho's young Martial Uncle.
- **Personality:** Naturally timid and introverted, but unable to control himself once angered.
- **Voice:** His current voice is rough, formal, and polite, punctuated by Buddhist invocations.
- **Relationships:** Hong Dao was his Master; Jung Ho is his Martial Nephew; he carries Hong Dao's will and recognizes the Morning Star whom Hong Dao intended him to find.

## Korean source

```text
＃542화



걸음걸이는 그 사람의 성향을 알 수 있는 중요한 지표 중 하나다.

특히 무림인의 경우에는 생각 이상으로 많은 정보가 걸음걸이에 담겨 있다.

우악스러운 힘을 바탕으로 무공을 펼치는 이의 걸음을 무겁고 거칠다.

반면 유려한 무공을 익혔거나, 살수와 같은 특정한 경우에는 발소리도 잘 들리지 않을 만큼 은밀하고 가볍다.

그런 의미에서 지금 계단을 올라오고 있는 누군가의 걸음걸이는, 자신의 존재를 알리다 못해 소리를 지르고 있다 해도 과언이 아니었다.

쿵, 쿵, 쿵.

‘사운드 보소.’

평범한 사람이라면 듣는 것만으로도 심장이 내려앉을 만큼 육중한 소음.

보보(步步)마다 제법 단단하게 설계되어 있는 계단이 삐걱거리고 미세한 진동이 전해진다.

어느새 옆구리에 찬 호리병을 꺼내 술을 홀짝이고 있던 적천강이 심각한 표정으로 입을 열었다.

“암천. 그놈들이 하다 하다 이제는 사람으로 괴물까지 만드는군. 도대체 무슨 술수를 쓴 거지?”

“예?”

순간 뭔 소린가 했네.

곧장 적천강의 말을 이해한 내가 손을 내저었다.

“그, 말씀하시는 중에 죄송한데 지금 올라오는 놈은 암천 아닌데요.”

“음. 그래도 걱정할 만한 수준의 상대는 아니니, 문을 열고 들어오는 즉시 네 녀석이 때려눕히거라. 무림맹에 던져 주면 뭐라도 나오겠지.”

“……아니, 암천 아니라니까요. 그리고 문은 노야께서 이미 박살 내셨으면서 뭘.”

“뭣이?”

눈이 화등잔만 해진 적천강이 침까지 튀겨가며 말했다.

“그럼 지금 올라오고 있는 저놈이 순수한 인간이란 말이냐?”

“놀랍게도, 자연산입니다.”

“허어, 인생 오래 살고 봐야 할 일이로고. 그런데 느껴지는 기파가 그리 정순하지는 않던데.”

응급환자를 내려보내고 돌아온 혁무진이 일양노의 피가 흥건하게 묻은 손바닥을 바짓단에 문지르며 대답했다.

“이야, 역시 적 대협이십니다. 사마외도를 단번에 알아보시는군요.”

“사마외도?”

“예. 흑룡마문(黑龍魔門)의 소문주와 그 수하지요.”

커다란 소음에 가려져 있어 잘 들리지 않았을 뿐, 처음부터 인기척은 하나가 아니라 둘이었다.

그리고 마침내 두 사람이 적천강의 난입으로 뻥 뚫려 버린 문 너머로 모습을 드러냈다.

“무림말학 사마표가 화왕 적천강 대협을 뵙습니다.”

훤칠한 키에 잘생긴 얼굴의 사내. 그를 마주하자마자 입안이 모래를 씹은 것처럼 까끌거린다.

문득 머릿속을 스쳐 지나가는 세 글자 때문이다.

‘정혼자.’

내 생각을 아는지 모르는지, 적천강을 향해 포권을 취한 사마표가 옆에 멀뚱멀뚱 서 있는 덩어리를 툭 쳤다.

“뭐 하느냐. 어서 인사 올리지 않고.”

별호와 이름이 찰떡처럼 어울리는 호거아(虎巨兒) 태산이 꾸벅 허리를 굽혔다.

“반갑다. 태산이. 화왕 봤다.”

“…….”

신박한 인사법일세.

슬쩍 적천강의 표정을 보니 화왕이 아니라 염라대왕을 보여 주고 싶은 기색이 역력하다.

그런 낌새를 눈치챈 듯 사마표가 신속하게 부연설명을 덧붙였다.

“적 대협께서도 짐작하셨겠지만, 어휘력이 부족해서 이게 최선입니다.”

“……그렇다면 어쩔 수 없긴 한데.”

적천강이 떨떠름한 얼굴로 중얼거렸다.

“별 해괴한 놈을 다 보겠군. 그래, 노부도 네놈 봤느니라.”

“헤헤.”

순진하게 웃은 태산이 대뜸 쌍따봉을 날렸다.

“화왕. 강하다. 태산이. 강자 좋다. 반갑다.”

“오, 오냐. 노부도 반갑다.”

“그런데 태산이. 배고프다.”

“뭐, 뭐라?”

“저거 먹고 싶다. 화왕 허락해 주면 고맙다.”

식탐이 가득한 눈빛은 어느새 우리의 어깨너머를 향하고 있었다.

탁자 위에 놓인 다과의 존재를 깨달은 적천강이 엉겁결에 고개를 끄덕였다.

“그, 그래라.”

“와! 다과! 태산이, 잘 먹겠습니다!”

쿵! 콰직!

객잔 주인이 피눈물을 흘리겠구만.

평범한 사람이라고는 볼 수 없는 엄청난 덩치가 그나마 남아 있던 문짝의 잔해를 박살 내며 돌격한다.

기다렸다는 듯 탁자 위의 모든 것을 쓸어 담는 태산의 모습을 멍하니 바라보던 적천강이 중얼거렸다.

“노부가 너무 오래 살았나.”

아무리 적천강이라고 해도 당황하지 않을 수 없는 모양이다.

하긴, 지금까지 화왕이라는 두 글자만 대면 설설 기는 사람들만 상대해 왔으니 그럴 만도 했다.

아마 청풍을 제외하고는 처음으로 등장하는 강적의 등장이 아닐까.

‘뭐, 그건 그렇다 치고.’

뒤통수를 긁적인 나는 사마표를 위아래로 훑었다.

“그래서. 여기에는 무슨 일로?”

“중요한 용무가 있어서. 괜찮다면 안으로 들어가서 이야기하면 좋겠는데.”

“아니, 별로 괜찮지 않아서 그래.”

사마표가 어깨를 으쓱해 보였다.

“예의상 물어본 건데, 역시 평범하진 않군. 자네도 사마외도에 악감정이 있었나?”

“악감정이라기보다는…….”

제기랄. 막상 이렇게 나오니 뭐라 할 말이 없다.

녀석과는 겨우 한 번 만난 것이 고작이지만 첫인상이 그리 나쁘지도 않았고, 내가 틈만 나면 사마외도 척결과 정파 짱짱맨을 외치는 골수주의자도 아니니까.

그리고 그건 적천강도 크게 다르지 않았다.

“거기 서서 뭔 짓거리들이냐? 정분났어?”

적천강까지 저리 말하니 딱히 거절할 이유가 없다. 고민을 끝마친 나는 사마표를 향해 턱짓했다.

“젠장, 들어오든가.”

“고맙군. 감사합니다, 적 대협.”

정중한 인사와 함께 안으로 들어오는 사마표의 모습에 적천강이 고개를 끄덕였다.

“어린놈이 제법 싸가지는 있구나. 아니면 음흉한 핏줄을 이어받은 건가?”

순간 멈칫한 사마표가 빙긋 웃었다.

“아마 후자일 겁니다. 그나저나 제 아버님을 기억하고 계시는군요.”

“네놈의 얼굴을 보기 전까지는 잊고 있었지. 흑야왕(黑夜王), 그놈의 소싯적 모습을 쏙 빼다 박았군.”

흑야왕 사마공.

사마표의 아버지이자, 지금의 흑룡마문을 만든 입지전적인 인물이다.

별호만 보면 십왕(十王) 중 한 사람이라고 생각하기 쉽지만. 궁기방을 통해 알게 된 정보에 따르면 십왕과는 아무런 연관도 없었다.

‘녹림맹주인 녹림투왕(綠林鬪王)과 용봉표국의 표왕(鏢王)처럼.’

그들 역시 범접할 수 없는 무위를 지닌 초절정 고수였지만, 십왕이라는 전설의 한 자락으로 인정받기에는 무리였다.

사파 무림에서 손꼽히는 고수이자 흑룡마문의 문주인 흑야왕 사마공 역시 같은 맥락으로 그러한 별호를 얻었다고 했다.

“그나저나……”

사마표를 지그시 바라보던 적천강이 문득 미간을 찌푸렸다.

“흑야왕에게 이렇게 젊은 아들놈이 있을 줄은 몰랐는데.”

“위로 형님 일곱과 누이 아홉이 있습니다. 제가 막내지요.”

“허, 정력도왕이 들으면 울고 가겠군. 그럼 네 녀석이 소문주렸다.”

사마표의 눈동자가 살짝 커졌다.

“그렇습니다만, 그건 어찌…….”

“뻔하지 않느냐.”

코웃음 친 적천강이 말을 이었다.

“흑야왕, 그놈 성격이라면 능히 그러고도 남지. 자질이 뒷받침된다면 다른 자식들은 순장(殉葬)해도 신경 쓰지 않을 놈이니까.”

“…….”

“기억하는 모습과 크게 달라지지 않은 모양이군. 도무지 속내를 알 수 없는 놈이었지. 여우처럼 약삭빠르고, 독사처럼 교활했어.”

면전에 대고 패드립 박는 클라스 봐라. 가슴이 웅장해진다.

사마표의 자질을 인정한다는 속뜻이 있긴 하지만 결국 패드립은 패드립. 나는 아빠 욕에 발끈한 효자 아들이 일을 벌이기 전에 불쑥 입을 열었다.

“그래서, 무슨 일이야?”

“……흠. 글쎄.”

생각을 알 수 없는 오묘한 표정을 짓고 있던 사마표가 품에서 무언가를 꺼내 들었다.

무림에서는 제법 비싼 취급을 받는 종이. 그리고 종이의 최상단에 적힌 문구가 단번에 눈에 띈다.



★무명 소졸이었던 내가, 이룡각에서는 무림 영웅?!★



탁자 위에 놓인 종이를 빤히 내려다보던 나는 턱을 문질렀다.

“제법 눈에 익은데.”

사마표가 피식 웃었다.

“눈에 익을 수밖에.”

“누가 생각했는지는 모르겠지만, 천재적이야.”

“파격적이기도 하고.”

툭.

사마표의 길쭉한 손가락이 종이의 한 부분을 짚었다.

혁무진이 악필로 휘갈겨 쓴 모집요건(募集要件).

바로 그 아래에 존재하는 여러 항목 중에서도 손가락은 정확히 한 곳을 가리키고 있었다.



＃성별 및 출신 문파 안 따지고



부드러운 목소리가 이어졌다.

“특히 이 부분이 마음에 들더군.”

“그래서?”

“지원하겠네. 이룡각에.”

내심 짐작은 하고 있었지만, 이렇게 직접 들으니 기분이 복잡미묘하다.

잠시 고민하던 나는 입맛을 다셨다.

“이유는?”

“노래를 듣는 순간 느낌이 오더군. 딱 내가 원하던 곳이지 뭔가.”

“응. 헛소리.”

웃기지도 않는 이야기다.

성공 시대가 시작되고, 찾는 문파가 많아지고, 인생이 달라질 거라는 노래 가사는 사마표에게 해당하지 않는 이야기니까.

흑룡마문은 사파 무림에서도 세 손가락 안에 드는 힘을 지닌 문파.

설령 사마표가 소문주가 아니었다 해도 흑야왕의 핏줄로 태어난 이상 어느 정도의 부귀영화는 보장된 것이나 다름없었다.

‘그런 놈이 이룡각에 들어오길 청한다?’

아무리 정파 골수분자들이 피켓 들고 시위를 벌여도 사마표는 무림맹에서 한 자리를 차지할 수 있는 놈이다.

나는 팔짱을 낀 채로 사마표를 지그시 응시했다.

“농담이라면 재미없는데.”

“다행이군. 전부 진담이거든.”

“헛소리 집어치우고. 진짜 이유가 뭐야?”

“이유를 대야 한다는 건 방에 적혀 있던 내용에 없었네만.”

“가라. 멀리 안 나간다.”

사마표가 어쩔 수 없다는 듯이 어깨를 으쓱해 보였다.

“이룡각에 들어간다면, 사마외도라는 꼬리표를 뗄 수 있지 않을까 싶어서.”

“딱히 떼고 싶어 하는 것 같지는 않던데.”

“정말 그렇게 보이나?”

“믿음이 안 가는 게 사실이지.”

“그렇다면 어쩔 수 없군. 그럼 이참에 허심탄회하게 털어놓겠네.”

“털어놔. 개 털리기 싫으면.”

피식 웃은 사마표가 문득 얼굴을 굳혔다.

거스러미 하나 없는 입술 사이로 흘러나온, 나직한 목소리가 귓가를 파고든다.

“날 위해 자네를 이용할 생각일세. 때에 따라서 어떤 방식으로든 유용한 패가 되겠지.”

순간, 무거운 침묵이 흘렀다.

쉴 새 없이 쩝쩝거리며 음식을 씹던 태산도 움직임을 멈췄고, 혁무진은 화등잔만 하게 커진 눈으로 나와 사마표를 번갈아 바라보았다.

그리고 이내 침묵을 깨트리는 목소리가 있었다.

“재미있는 놈일세, 그려.”

목소리의 주인은 적천강이었다.

웃는 건지 화를 내는 건지, 도무지 알 수 없는 표정으로 사마표를 응시하던 그가 나를 향해 불쑥 질문을 던졌다.

“네놈은 어찌 생각하느냐?”

잠시 고민하던 나는 천천히 입술을 뗐다.

“아주 강렬한데요. 면접 한두 번 본 놈이 아닌 것 같습니다.”

“받겠느냐?”

“글쎄요.”

흑룡도 사마표. 저놈이 했던 말 중 어디까지가 농담이고 어디까지가 진심인지 판단하기가 힘들다.

하지만 한 가지는 확실했다.

‘재미있는 놈이네.’

툭툭.

침묵 속에서 탁자를 두드리는 소리만 울려 퍼진다.

짧은 시간 동안 생각을 정리한 나는 사마표를 똑바로 응시했다.

“우선 하나만 확실하게 하고 가자.”

“얼마든지.”

“만약 허튼수작을 부리면…….”

내 말이 끝나기도 전에, 사마표가 대답했다.

“즉결 처분. 그래, 명심하지.”

“허. 시원시원하시네.”

“당연한 일이니까. 그럼 이제 끝난 건가?”

“아직 합격 아니야. 우선 염두에 두는 거지. 우선 오늘은 이만 가라.”

“그러도록 하지.”

도대체 이놈의 목적은 뭘까.

커져만 가는 궁금증 속에서, 떠나려는 사마표와 태산을 바라보던 나는 잊고 있던 한 가지 중요한 사실을 깨달았다.

“그리고 하나 더.”

“……?”

“저놈 식비는 네가 부담해.”

“……!”
```

## Final English reading copy

```markdown
# Chapter 542

A person’s walk was one of the important indicators of their personality.

For martial artists in particular, their footsteps revealed far more than most people would expect.

Someone who relied on crude strength when using martial arts would have a heavy, rough gait.

On the other hand, those who had learned graceful martial arts—or specialized in certain fields, such as assassination—could move so stealthily and lightly that their footsteps were barely audible.

In that sense, it would not have been an exaggeration to say that the footsteps of whoever was coming up the stairs were not merely announcing his presence. They were practically screaming it.

Thud. Thud. Thud.

*Now that’s some sound.*

It was the kind of heavy noise that would make an ordinary person’s heart sink just from hearing it.

With every step, the solidly built staircase creaked, and faint vibrations traveled through the floor.

Jeok Cheongang, who had somehow already taken out the gourd hanging at his side and was sipping from it, spoke with a grave expression.

“Dark Heaven. After everything else they’ve done, they’re now turning people into monsters. What kind of trick did they use?”

“Huh?”

For a moment, I had no idea what he was talking about.

Then I understood and waved my hand.

“Sorry to interrupt, but the guy coming up isn’t from Dark Heaven.”

“Hm. Even so, he is not an opponent worth worrying about. Open the door, and the moment he enters, knock him flat. If we throw him to the Murim Alliance, something useful will come out of him.”

“……He’s not from Dark Heaven. And you already smashed the door, Old Master. What door are you talking about?”

“What?”

Jeok Cheongang’s eyes widened like lanterns as he splattered spit while speaking.

“You mean to say that the fellow coming up is a pure-blooded human?”

“Amazingly, he’s all-natural.”

“Hah. Some things really do have to be seen after living a long life. But the aura I sense from him doesn’t seem particularly pure.”

Hyuk Mujin returned after sending the emergency patient downstairs. He wiped his palm, still drenched in Old Man Ilyang’s blood, against his trouser leg before answering.

“Wow, as expected of Great Hero Jeok. You recognized a practitioner of demonic, heterodox arts at a glance.”

“Demonic, heterodox arts?”

“Yes. He’s the Young Sect Leader of the Black Dragon Demon Gate, along with his subordinate.”

The loud footsteps had drowned it out, but there had been two presences from the beginning.

At last, two people appeared beyond the doorway that Jeok Cheongang had blown wide open.

“This junior of Murim, Sama Pyo, pays his respects to Great Hero Jeok Cheongang, the Fire King.”

He was a tall, handsome man. The moment I saw him, my mouth felt gritty, as though I were chewing sand.

That was because three words suddenly flashed through my mind.

*Former fiancé.*

Whether he knew what I was thinking or not, Sama Pyo clasped his hands toward Jeok Cheongang, then poked the lump standing blankly beside him.

“What are you doing? Hurry up and pay your respects.”

Tiger Giant Child Taishan, whose epithet and name suited each other perfectly, bent deeply at the waist.

“Nice to meet. Taishan saw Fire King.”

“……”

What a novel greeting.

I took a quick look at Jeok Cheongang’s expression. He looked like he wanted to show Taishan Yama rather than the Fire King.

Perhaps noticing the mood, Sama Pyo quickly added an explanation.

“As you may have guessed, his vocabulary is limited. This is the best he can do.”

“……In that case, I suppose it can’t be helped.”

Jeok Cheongang muttered with a displeased expression.

“I’ve seen all sorts of strange fellows in my life. Fine. This old man has seen you, too.”

“Heh heh.”

Taishan smiled innocently, then abruptly raised both thumbs.

“Fire King. Strong. Taishan. Likes strong people. Nice to meet you.”

“W-Well, yes. This old man is pleased to meet you as well.”

“But Taishan. Hungry.”

“W-What?”

“Want to eat that. If Fire King allows, Taishan grateful.”

His eyes were already fixed over our shoulders, filled with gluttonous anticipation.

Jeok Cheongang realized there were refreshments laid out on the table and nodded without thinking.

“Th-Then go ahead.”

“Hooray! Refreshments! Taishan will eat well!”

Crash! Crunch!

The innkeeper was going to cry tears of blood.

A massive body that could not possibly belong to an ordinary person charged forward, smashing through what remained of the door.

Taishan swept everything on the table into his arms as though he had been waiting for permission. Jeok Cheongang stared blankly at him and muttered.

“Have I lived too long?”

Even Jeok Cheongang seemed incapable of avoiding surprise.

Then again, until now he had only dealt with people who trembled and groveled whenever they heard the words *Fire King*. His reaction was understandable.

Aside from Cheongpung, this might have been the first genuinely formidable opponent to appear.

*Well, putting that aside.*

I scratched the back of my head and looked Sama Pyo up and down.

“So. What brings you here?”

“I have important business. If possible, I would like to go inside and discuss it.”

“No, that’s exactly why it isn’t possible.”

Sama Pyo shrugged.

“I asked out of courtesy, but you really aren’t ordinary. Do you also harbor ill feelings toward the demonic, heterodox path?”

“Rather than ill feelings……”

Damn it. Now that he had put it that way, I had no answer.

I had only met him once, but my first impression of him had not been particularly bad. Nor was I some hardcore zealot who shouted about eradicating the heterodox path and glorifying the orthodox faction whenever I got the chance.

The same was largely true of Jeok Cheongang.

“What are you two standing there doing? Did you fall for each other?”

With even Jeok Cheongang putting it that way, there was no particular reason to refuse. After finishing my deliberation, I jerked my chin toward Sama Pyo.

“Damn it. Come in, then.”

“Thank you. Thank you, Great Hero Jeok.”

As Sama Pyo entered with a polite greeting, Jeok Cheongang nodded.

“That young brat has decent manners. Or did he inherit that sly bloodline?”

Sama Pyo paused for a moment, then smiled faintly.

“Probably the latter. By the way, you remember my father.”

“I had forgotten him until I saw your face. You look exactly like the Black Night King did in his youth.”

Black Night King Sima Gong.

He was Sama Pyo’s father, a self-made man who had built the Black Dragon Demon Gate into what it was today.

Judging from his epithet, it would have been easy to assume that he was one of the Ten Kings. But according to the information I had learned through Gung Gibang, he had no connection to the Ten Kings whatsoever.

*Just like the Green Forest Battle King, the Green Forest Alliance Leader, and the Escort King of the Yongbong Escort Bureau.*

They, too, were Supreme Peak masters with martial prowess beyond ordinary reach. But it would have been a stretch to recognize them as part of the legend of the Ten Kings.

Black Night King Sima Gong, one of the greatest masters in the unorthodox martial world and the Sect Leader of the Black Dragon Demon Gate, had apparently received the title in much the same way.

“But still……”

Jeok Cheongang stared intently at Sama Pyo, then suddenly furrowed his brow.

“I had no idea the Black Night King had such a young son.”

“I have seven older brothers and nine older sisters. I am the youngest.”

“Hah. The Virility Saber King would cry himself to sleep if he heard that. So you’re the Young Sect Leader.”

Sama Pyo’s eyes widened slightly.

“That is correct, but how did you—”

“Isn’t it obvious?”

Jeok Cheongang snorted and continued.

“Given the Black Night King’s personality, that is exactly what he would do. If your talent was sufficient, he wouldn’t care even if it meant burying all his other children alive as sacrifices.”

“……”

“He doesn’t seem to have changed much from the man I remember. I could never tell what was going on inside his head. He was as sly as a fox and as cunning as a viper.”

*Look at him, casually throwing a parent insult right to his face. My heart almost swelled with awe.*

There was an underlying meaning that acknowledged Sama Pyo’s talent, but a parent insult was still a parent insult. Before the dutiful son could start something over the insult to his father, I cut in.

“So what brings you here?”

“……Hm. Well.”

Sama Pyo’s expression became impossible to read. He reached inside his robe and pulled out something.

It was paper, an expensive commodity in Murim. And the words written at the very top immediately caught my eye.

> ★**I Was a Nameless Foot Soldier, but in the Two Dragons Pavilion, I’m a Murim Hero?!**★

I stared down at the paper on the table and rubbed my chin.

“This looks awfully familiar.”

Sama Pyo gave a quiet laugh.

“It couldn’t be otherwise.”

“I don’t know who came up with it, but it’s genius.”

“And groundbreaking.”

Tap.

Sama Pyo’s long finger pointed to one part of the paper.

It was the recruitment requirements Hyuk Mujin had scribbled down in terrible handwriting.

Among the various items written below, his finger accurately indicated one specific line.

> \# Gender and sect affiliation don’t matter \#

His gentle voice continued.

“I particularly like this part.”

“So?”

“I wish to apply. To the Two Dragons Pavilion.”

I had more or less expected it, but hearing him say it directly still left me with complicated feelings.

After a moment’s thought, I clicked my tongue.

“Why?”

“The moment I heard the song, I had a feeling. This is exactly the place I’ve been looking for.”

“Yeah. Bullshit.”

It was not even funny.

The lyrics about the era of success beginning, more sects seeking you out, and your life changing simply did not apply to Sama Pyo.

The Black Dragon Demon Gate was one of the three strongest sects in the unorthodox martial world.

Even if Sama Pyo had not been the Young Sect Leader, being born into the Black Night King’s family practically guaranteed him a certain level of wealth and prosperity.

*And someone like that wants to join the Two Dragons Pavilion?*

Even if the orthodox faction’s diehards held up picket signs and protested, Sama Pyo was more than capable of securing a position within the Murim Alliance.

I folded my arms and stared at him.

“If you’re joking, it isn’t funny.”

“Fortunately, I’m being entirely serious.”

“Enough bullshit. What’s the real reason?”

“You say I need to provide a reason, but that was not written on the notice.”

“Get lost. I won’t walk you out.”

Sama Pyo shrugged as though he had no choice.

“I thought that if I joined the Two Dragons Pavilion, I might be able to shed the label of belonging to the demonic, heterodox path.”

“You don’t exactly seem eager to shed it.”

“Do I really seem that way?”

“It’s a fact that I don’t trust you.”

“Then I suppose it can’t be helped. In that case, I’ll take this opportunity to speak frankly.”

“Go ahead. Unless you want to get the shit beaten out of you.”

Sama Pyo let out a quiet laugh, then his expression abruptly hardened.

A low voice slipped from between his perfectly smooth lips and pierced my ears.

“I intend to use you for my own benefit. Depending on the circumstances, you will become a useful card to me in one way or another.”

A heavy silence descended.

Even Taishan, who had been chewing noisily without pause, stopped moving. Hyuk Mujin stared back and forth between Sama Pyo and me with eyes as wide as lanterns.

Then a voice broke the silence.

“What an interesting fellow.”

The speaker was Jeok Cheongang.

He stared at Sama Pyo with an expression that made it impossible to tell whether he was laughing or angry, then abruptly asked me a question.

“What do you think?”

I considered it for a moment before slowly parting my lips.

“He’s certainly intense. He doesn’t seem like someone who’s only been through one or two interviews.”

“Will you accept him?”

“Hard to say.”

Sama Pyo, the Black Dragon Saber. It was difficult to judge which of his words were jokes and which were sincere.

But one thing was certain.

*He’s an interesting fellow.*

Tap. Tap.

The only sound echoing through the silence was the tapping of fingers against the table.

After organizing my thoughts for a short while, I looked straight at Sama Pyo.

“Let’s establish one thing before we go any further.”

“By all means.”

“If you try anything funny……”

Before I could finish, Sama Pyo answered.

“Summary execution. Yes, I’ll bear that in mind.”

“Huh. You don’t mince words.”

“It is only natural. Then are we finished here?”

“You haven’t been accepted yet. I’m only keeping you under consideration for now. For today, go.”

“Very well.”

What in the world was this man after?

As my curiosity continued to grow, I watched Sama Pyo and Taishan preparing to leave. Then I realized one important thing I had forgotten.

“And one more thing.”

“……?”

“You’re paying for that guy’s food.”

“……!”
```

<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0517.txt",
      "sha256": "dc13631d03a7459927fe19bea802c506b5994033a41ecaad1b705f71909f1fe8",
      "bytes": 12736
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "2f43a3acd5736d4631b44319a6bcebb8ec1203c700d1453e66505b41010c4a97",
      "bytes": 4097
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "6b7e5ff385d053ceedc0ed91fd188826f5d35ff2c3bcd2ffd0636127d26aa5f1",
      "bytes": 164827
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "d8766fbb6bcac82c6e868a8ddf8c4cf34306380f056bb8f1b5e31160409e6e17",
      "bytes": 1006
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "e23297b6dca8cfae86cd7673fabc4ca3d9f824b1de4da1e47e2b44c84c1507dd",
      "bytes": 553
    },
    {
      "path": "characters/Gung Gibang.md",
      "sha256": "66545fe94e99341b2d32994651a0e73214d59f0f3bfaa3539b3469a3bdce08c1",
      "bytes": 686
    },
    {
      "path": "characters/Hong Dao.md",
      "sha256": "11f1ccec07e6e2ca172aa1bcfd76c802aed516b017a5f91280cb55e49e89b1a2",
      "bytes": 1001
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "7670f1e046e1ad8b823c6373ed2fcd742de12e2dd031875e58e47bcd8f26d3a3",
      "bytes": 1108
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "4ec45e8c63d01fe39f57c588976eb022bade0d00ecc8509d2c0998845c0a504a",
      "bytes": 1630
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "97e98ec613c1419c1b4464e2cebcf91431589fb0361d45bc89c0643620cc3495",
      "bytes": 1777
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "65186faf041a4acc0bf08d35108a3e798e7ce11dd17fbb29f95ba0def98b8bb3",
      "bytes": 622
    },
    {
      "path": "characters/Jung Ho.md",
      "sha256": "ff75dd67923acb9049b2364bb57ea39c0ef696792053875008a7ae1a4e898f7c",
      "bytes": 699
    },
    {
      "path": "characters/Unnamed.md",
      "sha256": "ea62d4424074dfed5e5d12fe111ede3f329e3f7f54a3ea7cdb7123d64fa60129",
      "bytes": 727
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "f0eeea838827542b68db72ad422e6d5879396f37918c6c0a7e2a686c6c414560",
      "bytes": 156461
    }
  ],
  "estimated_tokens": 13455
}
-->

# Durable State Update — Chapter 517

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 517. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 517. Profile updates may replace only one
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
  "chapter": 517,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 517,
    "continuity_sources": [517],
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
    "Mungyeong is the Slaughter Saint and former Divine Physician, a Returned to Youth Supreme Peak master and the greatest assassin in history; Mu Song and five Water Dragon Stronghold subordinates know he is exceptionally powerful but not that he is the Slaughter Saint.",
    "Mungyeong is training Taekyung to refine the stability and precision of the violent internal energy produced by the Fire Gate Divine Technique through Rising on Duckweed, Crossing Water.",
    "Zhuge Feng's Demon-Sealing Formation blocks all mana from the exposed Gate by drawing in natural qi, but whether it is permanent and repeatable remains unresolved.",
    "Jang Taebo is the Jin Family of Taiyuan's Master of Ironcraft Hall and is summoning renowned artisans to process the Water God Dragon's remains.",
    "The New Murim Alliance has been publicly announced from Mount Song; major orthodox factions are moving toward Henan, while the Yangtze River Channel League, Green Forest Alliance, North Sea Ice Palace, and Nanman Beast Palace remain uncertain in their positions.",
    "The Southern Heaven Demon Empress is traveling toward Yunnan and expects to cause further deaths.",
    "Jin Mukyung remains secluded in the training hall after losing to Cheongpung, refusing to emerge until he achieves a great accomplishment.",
    "Unnamed, Hong Dao's practical Disciple, has endured three months in Repentance Cave, achieved enlightenment, emerged as Jung Ho's young Martial Uncle, and now appears scarred with a rougher voice.",
    "The Black Dragon Demon Gate is an ancient unorthodox faction that once belonged to the Demonic Cult's Twelve Branches and now ranks among the Central Plains' strongest unorthodox powers.",
    "Jin Taekyung completed Stage 2 of Fake Murim Practitioner, achieved Single Reed Crossing the River, improved his internal-energy control and attributes, gained 50 bonus points and substantial EXP, and leveled up.",
    "Taekyung experienced a nightmare involving a familiar-feeling red gaze, oppressive fear, and a gigantic snake in a swamp; its source and significance are unknown."
  ],
  "continuity_sources": [
    516,
    515
  ],
  "open_questions": [
    "Will the Demon-Sealing Formation remain effective permanently, and can equivalent formations be installed repeatedly if more Gates appear?",
    "What is the Lord of Heaven's identity, and how is he connected to the dangerous force Taekyung associates with his original world?",
    "Where is the Southern Heaven Demon Empress ultimately headed, and what does she intend to do in Yunnan?",
    "Will the Nanman Beast Palace, North Sea Ice Palace, Yangtze River Channel League, and Green Forest Alliance support, ignore, or oppose the New Murim Alliance?",
    "What is the source of the familiar red gaze and oppressive presence Taekyung encountered in his nightmare?"
  ],
  "safe_through": 516,
  "temporary_decisions": [
    "Render 새외무림 as Outer Murim, 새외 as Outer Lands, 북해빙궁 as North Sea Ice Palace, 야수묘왕 as Beast Miao King, and retain Nanman Beast Palace for 남만야수궁.",
    "Render 소뢰음사 as Small Thunderclap Temple, 광풍사 as Mad Wind Society, 포달랍궁 as Potala Palace, 오독문 as Five Poisons Sect, 독곡 as Poison Valley, 천축 as India, and 갠지스강 as Ganges River.",
    "Render 파사국 as Persia, 회교도 as Muslims, 영웅건 as hero headband, 대막 as great desert, 귀염권 as Ghost Flame Fist, and 장성 as Great Wall.",
    "Retain sa-eo for 사어, shark for 상어, Old Master for 노야, this old man/I for 노부, Shark Water-Ski Team for 수상스키단, and swift ship for 쾌조선.",
    "Render 정호 as Jung Ho, 사마표 as Sama Pyo, 흑룡도 as Black Dragon Saber, 대초자곤 as two-section staff, 시주 as Benefactor, 계율원주 as Discipline Hall Master, and 십이지파 as Twelve Branches of the Demonic Cult."
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
| 굉도     | **Hong Dao**       |
| 법왕     | **Dharma King**               | Hong Dao       |
| 태원진가   | **Jin Family of Taiyuan**        |
| 소림     | **Shaolin**                      |
| 무림맹    | **Murim Alliance**               |
| 암천     | **Dark Heaven**                  |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 영약     | **elixir**                                       |                                                       |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 폐관수련   | **closed-door training**                         |                                                       |
| 후기지수   | **young prodigy** / **rising martial artist**    | Contextual, not a title                               |
| 정파     | **orthodox faction**                             |                                                       |
| 사파     | **unorthodox faction**                           |                                                       |
| 중원     | **Central Plains**                               |                                                       |
| 제자     | **Disciple**                                 |
| 사형     | **Senior Brother**                           |
| 생도     | **cadet**                                    |
| 헌터      | **Hunter**            |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 하남     | **Henan**              |
| 사천     | **Sichuan**            |
| 대사      | **Master** for a senior Buddhist monk                           |
| 방장      | **Abbot**                                                       |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 궁기방 | **Gung Gibang** | Beggars' Sect Successor Beggar and finalist. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 정호 | **Jung Ho** | Middle-aged Shaolin martial monk leading the traveling group. |
| 무명 | **Unnamed** | Dharma name given by Hong Dao; literally means having no name. |
| 화시 | **fire arrow** | Flaming arrow Lee Seowol fires to signal Cheol Mubaek. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 오대세가 | **Five Great Families** | Major Murim grouping. |
| 하북 | **Hebei** | Province where Hyuk Family Textile Shop has a branch. |
| 무재 | **martial talent** | Innate aptitude for learning martial arts. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 소림사 | **Shaolin Temple** | Temple invoked in Chulwoo’s comparison of Baek Museong’s conduct. |
| 성라대연 | **Star-Array Grand Banquet** | Major martial gathering held in Henan every two or three years. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 아미타불 | **Amitabha** | Buddhist invocation spoken by the unidentified arriving group. |
| 숭산 | **Mount Song** | Mountain where Shaolin Temple is located. |
| 녹옥불장 | **Green Jade Buddha Staff** | Ancient Shaolin sacred treasure carried by Hong Dao. |
| 천기 | **heavenly patterns** | Celestial patterns Hong Dao studies to perceive major changes and omens. |
| 참회동 | **Repentance Cave** | Zhongnan Sect place of penance. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 불장 | **Buddhist Staff** | Generic term in Hong Dao's final words; the specific treasure is 녹옥불장. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 한강 | **Han River** | River associated with the bridge-collapse incident Lee Jungryong recalls. |
| 미국 | **United States** | Country associated with the talk show and CNM. |
| 아미 | **Emei** | Short form for Emei Sect. |
| 소림혈사 | **Shaolin Bloodshed** | Past incident cited by Hwangbo Eom. |
| 성도 | **Chengdu** | Sichuan destination of Taekyung's party. |
| 음한지기 | **Yin-Cold Qi** | Cold-aligned energy required in the treatment elixir. |
| 오대 | **Five Squads** | Named Tang Clan organizational group in Tang Sadok's mobilization order. |
| 소하 | **Xiao He** | Historical civil official invoked in the same exchange. |

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
| 무명 | 진태경 | newly_met_monk_to_benefactor | Benefactor | formal-polite | Uses 시주 while asking Taekyung's name. |
| 무명 | 적천강 | junior_monk_to_legendary_martial_master | Great Hero Jeok Cheongang | formal-deferential | Identifies Jeok by the title Fire King and the honorific 대협. |
| 무명 | 굉도 | disciple_to_master | Master | deferential | Refers to Hong Dao as 스승님 while explaining his Dharma name and training. |
| 적천강 | 굉도 | old_friends | Hong Dao | familiar and teasing | Uses Hong Dao's personal name in their casual reunion. |
| 굉도 | 적천강 | old_friends | Fire Gate Sect Leader | familiar and teasing | Teases Jeok as the carefree Fire Gate Sect Leader. |
| 굉도 | 무명 | master_to_disciple | Disciple | affectionate and familiar | Hong Dao addresses Unnamed as 제자야 while discussing his residence. |
| 굉도 | 진태경 | senior_monk_to_guest_benefactor | Benefactor | formal-polite and probing | Hong Dao repeatedly addresses Taekyung as 시주 while identifying him as the Master of Morning Star. |
| 궁기방 | 진태경 | rival_finalists | you bastard | insulting-casual | Gung Gibang answers Taekyung's collective insult with a profane threat. |
| 진태경 | 궁기방 | rival_finalists | you three idiots | insulting-casual | Taekyung addresses Gung Gibang as part of the trio and threatens them before a duel. |
| 혁무진 | 궁기방 | squad_companion_to_Beggars_Sect_successor | Young Hero Gung | formal-polite, then pointed | Uses 궁 소협 while asking about the culprit and challenging Gung’s insults. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 궁기방 | 혁무진 | squad_companions | you; that lunatic | insulting-casual | Gung Gibang mocks Hyuk Mujin's injuries and calls him a lunatic for attacking the Third Fiend. |
| 궁기방 | 청풍 | martial_companions | Young Hero Cheongpung | formal-polite | Gung Gibang uses 청 소협 while asking why Cheongpung is at the temporary clinic. |
| 적천강 | 궁기방 | overwhelming_elder_to_younger_martial_artist | you | blunt and threatening | Jeok Cheongang rebukes Gung Gibang for speaking informally and orders him to lie down. |
| 정호 | 무명 | Martial Nephew addressing his young Martial Uncle | Martial Uncle | formal-deferential | Jung Ho repeatedly addresses Unnamed as 사숙 after Unnamed emerges from Repentance Cave. |
| 무명 | 정호 | young Martial Uncle addressing his Martial Nephew | Martial Nephew Jung Ho | formal-polite and reassuring | Unnamed addresses Jung Ho as 정호 사질 while consoling him and discussing Hong Dao's will. |
| 정호 | 진태경 | Shaolin Discipline Hall Master to patient and Benefactor | Benefactor Jin | formal-polite | Jung Ho repeatedly uses 진 시주 and 시주. |
| 진태경 | 정호 | patient to Shaolin Discipline Hall Master | Monk | polite and familiar | Taekyung addresses Jung Ho as 스님. |

## Listed compact profiles

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 516
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, the grandson and Disciple of Sword Saint Mae Jonghak, and a Supreme Peak martial master known as the Huashan Divine Dragon.
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, a deep love of martial arts, competitive pride, unusual resistance to monster-induced Fear, and discomfort when someone copies his martial arts.
- **Voice:** Dreamy and hazy, with innocent, polite phrasing; he has begun imitating Taekyung's profanity.
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions while Taekyung is his only true martial rival; Tang Sadok has temporarily entrusted Mimi to him.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 516
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Gung Gibang.md

# Gung Gibang (궁기방)

- **Safe through:** Chapter 516
- **Aliases:** Successor Beggar, Beggar Prince, pure-blooded beggar, ultimate beggar
- **Role:** Gung Gibang is the Beggars' Sect Successor Beggar and a unique eight-knot disciple.
- **Personality:** Vulgar, aggressive, and quick-tempered.
- **Voice:** Blunt, profane, and vividly threatening.
- **Relationships:** Gung Gibang is a rival finalist alongside Baek Woo and Zhuge Gyun who trades insults with Taekyung, uses Beggars’ Sect intelligence to investigate Tang Taesang’s murder and Dark Heaven’s Hubei forces, and has now found a trace of Honglan.

### Hong Dao.md

# Hong Dao (굉도)

- **Safe through:** Chapter 515
- **Aliases:** Dharma King
- **Role:** Abbot of Shaolin and the Murim's Dharma King; master of Unnamed and the only friend to whom Jeok Cheongang had opened his heart; after leaving the Star-Array Grand Banquet, he was found in a massive pit with both legs severed and catastrophic internal injuries, whispered final words to Jeok Cheongang, and died.
- **Personality:** Calm, responsible, quietly playful, and still regarded by Jeok as lazy for sleeping whenever possible.
- **Voice:** Quiet, deep, weighty, and resonant, with casual familiarity when speaking to Jeok Cheongang.
- **Relationships:** Old friend of Jeok Cheongang; master of Unnamed; before his death, entrusted the Green Jade Buddha Staff to Unnamed and used his final words to warn Jeok about Jongni Chu, Dark Heaven, Unnamed, and the Buddhist Staff; sends Unnamed to bring the Master of Morning Star to Shaolin.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 516
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers and Vice Squad Leader of the Jin Dragon Squad.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 516
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, and Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 515
- **Aliases:** Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, a Supreme Peak master who possesses the Heavenly Martial Physique and superhuman physical strength, has manifested Force, opened his Middle Dantian, crossed the wall into true mastery, can perceive the texture of qi well enough to sever layered magic, can resist high-level monster Fear through exceptional mental strength, is publicly recognized as an S-rank-level Hunter while formally retaining an A-rank license pending testing, and can command coordinated raids against powerful monsters.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate, student, and trusted manager of media and official arrangements, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, and Xiao Shen regards him as an older brother after Jin saved him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 515
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Jung Ho.md

# Jung Ho (정호)

- **Safe through:** Chapter 516
- **Aliases:** None
- **Role:** Middle-aged Shaolin martial monk and Master of Shaolin's Discipline Hall who leads the traveling group and wields a Zen staff hung with prayer beads.
- **Personality:** Humble, observant, principled, and concerned with the safety of commoners.
- **Voice:** Formal, restrained, and admonitory, with Buddhist phrasing.
- **Relationships:** Unnamed is his young Martial Uncle; he leads the Shaolin monks traveling with him, addresses Sama Pyo as a Benefactor, and is recognized by Jin Taekyung as Park Jung Ho, a former Garam Middle School classmate.

### Unnamed.md

# Unnamed (무명)

- **Safe through:** Chapter 516
- **Aliases:** None
- **Role:** Young Shaolin monk and practical Disciple of the late Hong Dao; a Peak master who has achieved enlightenment after three months of treatment and training in Repentance Cave and is Jung Ho's young Martial Uncle.
- **Personality:** Naturally timid and introverted, but unable to control himself once angered.
- **Voice:** His current voice is rough, formal, and polite, punctuated by Buddhist invocations.
- **Relationships:** Hong Dao was his Master; Jung Ho is his Martial Nephew; he carries Hong Dao's will and recognizes the Morning Star whom Hong Dao intended him to find.

## Korean source

```text
＃517화



“잘 지내셨습니까, 시주.”

하마터면 못 알아볼 뻔했다. 그만큼 일 년 전 만났던 무명과 지금의 무명은 달라져 있었다. 얼굴, 말투, 분위기 할 것 없이, 그를 둘러싼 모든 것이 생소하고 낯설었다.

그리고 그가 변한 이유는 아마도…….

‘석 달 전, 그날 있었던 일 때문이겠지.’

무슨 말을 해야 할까. 입맛이 쓰다. 내가 입을 연 것은 정호와 혁무진이 다른 이들을 데리고 방을 빠져나간 직후였다.

“나도 그렇게 잘 지내지는 못했습니다. 생각보다 많은 일이 있었거든요.”

무명이 흐릿하게 웃었다.

“그런 것 같더군요. 사실 소승도 이틀 전에서야 겨우 시주에 관한 이야기를 들을 수 있었습니다.”

지난 석 달 동안 벌어졌던 일련의 사건들은 무림인이라면 모를 수 없었을 것이다. 그런데 소림에서도 중요한 위치에 있는 무명이 고작 이틀 전에야 전해 들었다면, 나로서는 한 가지 이유밖에 떠오르지 않았다.

“폐관수련(閉關修鍊)을 하셨군요.”

“아미타불. 참회동(慙悔洞)에 머무르고 있었습니다.”

“참회동이라면 혹시…….”

“알고 계신 바가 맞습니다. 스스로 청한 일이니 신경 쓰지 않으셔도 됩니다.”

부끄러울 참. 뉘우칠 회. 참회동은 죄인을 가두는 곳이다.

무엇이 그리 부끄럽고, 무엇을 뉘우쳐야 했을까. 그건 아마도 스승의 열반을 막지 못한 후회가 아니었을까. 무명은 스승이 떠나기 전 맡기고 간 소림의 신물, 녹옥불장(綠玉佛杖)마저 지켜 내지 못한 죄인을 자처하며 그곳에서 석 달이라는 시간을 보낸 것이다.

“한 치 앞도 보이지 않는 어둠 속에서 그런 생각을 했습니다.”

무명은 굳은살 박인 손가락으로 제 뺨을 쓰다듬었다. 크고 작은 흉터로 가득한 얼굴의 상당 부분이 검푸른 색으로 변색되어 있었다.

지금으로부터 석 달 전, 목숨을 걸고 막아섰던 적의 음한지기(陰寒地氣)가 남기고 간 흔적이다. 영영 벗겨지지 않을 멍에이기도 했다.

“조금만 더 강했더라면 스승님을 지킬 수 있었을 텐데, 그분의 마지막 당부를 잘 수행할 수 있었을 텐데, 하는 생각 말입니다.”

그러나 후회는 언제나 늦기 마련이다. 만인에게 존경받던 고승(高僧)은 예기치 못한 열반에 들었고, 누군가는 절친한 벗을 잃었으며, 또 다른 누군가는 스승의 마지막 유언조차 지키지 못했다는 죄책감에 휩싸여 참회동에 들어갔다.

‘다른 누구라고 한들 다르지 않았겠지.’

나 역시 마찬가지다. 만약 적천강을 치료하지 못하고 그대로 떠나보내야 했다면 어떤 심정이었을지 생각조차 하기 싫다. 아마 F급 헌터 진태경이었던 그 시절로 돌아가 깊은 후회와 절망을 반복했을지도 모르겠다.

하지만 고통은 사람을 변화시킨다. 좋은 쪽으로든, 나쁜 쪽으로든. 그리고 내 앞에 있는 무명의 경우에는 전자였다. 마음은 망가졌을지 모르나, 적어도 무공의 증진이라는 측면에서는 그랬다.

“개인적인 생각이지만, 참회동에서 생각만 하신 것 같진 않네요.”

“아미타불. 모든 것이 부처와 소림의 은덕 덕분이지요.”

햇살이 비치는 창밖을 향해 합장한 무명은 잔잔한 눈동자로 나를 응시했다. 정순한 힘이 서린 눈빛이다. 일 년 전만 하더라도 옹골찬 근육으로 이루어졌던 육신은 이제 오래된 고목(古木)처럼 말라 버렸다. 하지만 전신에서 흘러나오는 은은한 기세는 과거에 비할 바가 아니다.

‘이 사람, 벽을 넘었어.’

무림인이라면 누구나 꿈꾸는 지고한 경지. 무명 또한 마침내 그 영역에 발을 디딘 것이 틀림없었다.

내 탄성 어린 눈빛에 무명이 작게 고개를 끄덕였다.

“중태에 빠진 몸을 치료하고 높은 경지로 나아가기 위해서는 깨달음 외에도 많은 것이 필요했지요. 대환단(大還丹)도 그중 하나였습니다.”

“아.”

소림의 대환단이라면 천하의 온갖 영약 중에서도 단연 첫손에 꼽을 만큼 대단한 효능을 지닌 영약이다.

‘그래, 대환단이라면 충분히 가능했을지도.’

대환단의 효능도 효능이지만, 무명은 천기(天氣)를 읽는 법왕 굉도가 직접 데려와 심혈을 기울여 키운 제자다. 청풍만큼은 아니더라도 엄청난 무재를 타고난 천재. 대환단에 어울리는 인재임이 틀림없었다.

아직 한창때라고 할 수 있는 서른 줄에 초절정의 경지에 올랐으니, 스승의 안목은 물론 스스로의 재능까지도 입증해 낸 셈이다.

“축하드립니다. 대환단은 소림에서도 매우 귀한 물건이라 들었는데.”

“하여 소승도 극구 거절했습니다. 하지만 방장 사형께서 아무것도 묻지 말라 하시며 내어 주시더군요. 알고 보니 몇 년 전 스승님께서 그에 관련된 언질을 주셨던 모양입니다. 어쩌면…… 이리될 것을 알고 계셨는지도 모르지요.”

무명의 입가에 희미한 미소가 맺혔다. 잠시 스승을 떠올리듯 허공을 바라보던 그는 말을 이었다.

“아, 방장 사형께서도 진 시주를 뵙고 싶어 하십니다.”

“방장 사형이시라면……?”

법왕 굉도의 뒤를 이은 차기 방장에 관해서는 들어 본 바가 없다. 궁기방의 말로는 법왕의 직계 제자 중 한 사람이 될 거라고 했는데, 워낙 스펙타클한 사건들이 이어지는 통에 거기까지 신경 쓸 틈이 없었다.

“두 분이 직접 마주친 적은 없을 겁니다. 소승에게는 항렬상으로 대사형이 되시는 분인데, 방장직에 오르신 것도 불과 한 달이 채 되지 않았으니 진 시주께서 모르실 법도 합니다.”

“아, 그렇군요.”

“방장 사형께서 말씀하시길, 일전에는 워낙 경황이 없어 작별 인사도 못 하고 떠나보냈다며 죄송하다 하시더군요.”

“딱히 죄송하실 필요는 없죠. 그때는 저도 워낙 정신이 없었던 때라서.”

성라대연 도중 벌어진 소림혈사(少林血史)는 초유의 사건이었지만, 나는 불과 하루 이틀 만에 하남을 떠나 사천으로 향해야 했다. 중태에 빠진 적천강을 살리기 위해서는 한시라도 빨리 신의를 찾아야 했으니까.

“아미타불. 적 시주께서 완치되셨다는 소식을 뒤늦게 듣고 진심으로 기뻤습니다. 어딘가에서 소승을 지켜보고 계실 스승님께서도 건강해진 친우분의 모습에 안도하셨겠지요.”

“아, 그러고 보니 노……. 아니, 제 스승님과는 이미 만나셨겠네요.”

“시주께서 깨어나시기 전까지 대화를 나누고 있었습니다. 처음에는 못 알아볼 뻔했지 뭡니까.”

“아무래도 좀, 어…… 변하긴 하셨죠.”

“예. 소승만큼이나 변하셨더군요.”

“……어.”

이러면 뭐라 대답해야 하는 거냐.

난데없이 튀어나온 자학 개그에 머뭇거리는 나를 향해, 무명이 공손히 합장했다.

“아미타불. 농입니다.”

“아, 아아. 그러셨구나.”

“재미없으셨던 모양이군요. 자제하겠습니다.”

제발 그렇게 해 달라는 말이 목끝까지 솟구쳤다.

고생도 정도껏 한 사람이 저런 드립을 쳐야 웃긴 거지, 무명이 이런 말을 하면 단번에 분위기가 숙연해질 수밖에 없다. 하지만 내게는 고개를 끄덕일 용기가 없었다.

“……아닙니다. 재미있었어요.”

“아미타불. 그럼 계속하겠습니다.”

“…….”

“여기까지가 농이었습니다.”

확 그냥, 진짜 목탁으로 대가리를 깨 버릴까.

어이가 없어서 무명을 바라보던 나는 이내 피식 웃었다. 그래도 이런 어설픈 농담을 던지는 것을 보면 생각했던 것보단 훨씬 잘 이겨 낸 것 같다.

옆에서 위로는 해 주지 못하더라도 수위가 아슬아슬한 절간 드립 들어 주는 것 정도는 충분히 가능하지.

그나저나…….

“여긴 어딥니까? 소림사는 아닌 것 같은데.”

창밖에 해가 떠 있는 걸로 봐서는 꼬박 하루 정도는 잔 것 같은데, 이곳이 정확히 어디인지는 모르겠다. 다시 한번 주위를 둘러보는 내게 무명이 설명했다.

“숭산 인근의 객잔입니다. 무림맹의 이름으로 빌린 것이니 푹 쉬시며 머무르십시오.”

“무림맹이라.”

뭔가 멀게 느껴지던 단어였는데, 하남에서 무명의 입으로 직접 듣게 되니 체감이 남다르다. 침상에서 몸을 일으킨 나는 창가로 다가가 바깥 풍경을 감상했다.

저 멀리 하늘을 찌를 듯이 높게 솟은 숭산의 산봉우리가 가장 먼저 눈에 들어왔다. 그 외에도 산자락 밑으로 빼곡하게 운집한 건물들, 그리고 각양각색의 사람들이 시야에 담겼다.

협봉검을 찬 무림인, 커다란 대도(大刀)를 검갑도 없이 등에 짊어진 무림인, 창과 쌍부를 든 무림인…….

“…….”

아니, 각양각색은 맞는데 뭔가 이상해. 무서워.

눈길 닿는 곳 어디에나 있는 무림인들을 구경하는 내 모습에, 무명이 낮은 웃음소리를 흘렸다.

“아미타불. 천하 각지에서 소식을 듣고 모인 시주들입니다.”

“대충 훑어봐도 성라대연 때보다 많은 것 같네요.”

“성라대연이 후기지수를 위한 축제의 장이었다면, 무림맹 창설은 모든 이들에게 해당하는 일입니다. 정, 사에 속한 이들은 물론이고, 잘 알려지지 않은 기인이사(奇人異士)들 역시 상당수 은거를 깨고 나왔더군요.”

하긴 무게감부터가 다르니 그만큼 많은 사람이 모이는 건 당연한 일이다. 성라대연이 한강 불꽃 축제라면, 무림맹 창설은 진돗개 하나다. 그래서인지 성라대연 때와는 달리 양민들이 거의 보이지 않았다.

‘그들도 느끼고 있겠지. 지금 이곳에서 무슨 일이 벌어지고 있는지.’

속으로 중얼거리던 그때, 대로변을 가로지르는 한 무리의 무림인이 문득 눈에 걸렸다. 흔한 무림인 중 일부라고 생각하기에는 범상치 않은 기운. 필시 명문 대파에 소속된 이들이 분명했다.

‘복장도 이상한데. 누구지?’

굳이 무명에게 물어볼 필요도 없었다. 따뜻한 봄날과는 어울리지 않는 모피를 두르고, 평범한 무림인들과 달리 가죽 갑옷까지 걸친 그들의 등장에 곳곳에서 수군거리는 목소리가 흘러나왔으니까.

“저들은 혹시…….”

“맞네. 모용세가(慕容世家)야.”

“허어, 요녕(遼寧)에서 하남까지는 천릿길이 족히 넘거늘. 발 빠르게 도착했군.”

“괜히 기마민족의 피를 이었다고 하겠나. 그나저나 횡재했군. 살면서 모용세가의 인물들을 볼 줄이야.”

모용세가는 나도 처음 본다. 태원진가가 위치한 산서성도 변방에 속하지만, 요녕은 하북을 넘어 북동쪽으로 한참을 가야 있는 곳이라 옆 동네 마실 가듯 갈 수 없는 곳이기 때문이다.

하도 멀다 보니 모용세가의 인물들도 중원에 나오는 일이 드물다고 했다.

‘바로 그 모용세가란 말이지.’

오대세가에서도 강성한 축에 드는 모용세가인 만큼, 그 위명은 귀에 못이 박이도록 들었다. 듣기로는 여타의 문파와 달리 기마대도 운용한다고 들었는데…… 그래서인지는 몰라도 죄다 말 근육이다.

‘구파일방과 오대세가를 위시한 정파 무림. 들어 보니 사파 무림도 끼어든 것 같고, 거기에 더해 어디에도 속하지 않는 무림인들까지 하면…….’

흔히들 미국을 인종의 용광로라고 부른다. 내 눈에는 지금의 하남이 딱 그랬다. 물론 인종이야 같거나 비슷하지만, 어쨌든 쉽게 볼 수 없는 온갖 무림인들이 집결해 있으니까.

‘앞으로 사흘.’

사흘 뒤, 수많은 무림인들은 하나의 깃발 아래 모일 것이다. 무림맹이라는 이름 아래 하나 되어 병장기를 들고 암천에 맞서겠지.

창밖으로 보이는 이들을 바라보며 그런 생각을 떠올린 순간.

쾅!

어디선가, 거대한 굉음이 울려 퍼졌다.
```

## Final English reading copy

```markdown
# Chapter 517

“Have you been well, Benefactor?”

I almost failed to recognize him. That was how different Unnamed was from the person I had met a year ago. His face, speech, and atmosphere had all changed. Everything surrounding him felt unfamiliar and strange.

And the reason he had changed was probably…

*It must be because of what happened that day, three months ago.*

What was I supposed to say? My mouth felt bitter. I only spoke after Jung Ho and Hyuk Mujin left the room with the others.

“I haven’t been doing all that well, either. A lot more happened than I expected.”

Unnamed smiled faintly.

“It seems so. In fact, this humble monk only managed to hear about you two days ago.”

No martial artist could have remained unaware of the events that had unfolded over the past three months. But if Unnamed, who held an important position within Shaolin, had only heard about them two days ago, there was only one reason I could think of.

“You underwent closed-door training.”

“Amitabha. I was staying in Repentance Cave.”

“Repentance Cave? Could it be…”

“You are correct. It was something I requested myself, so there is no need for you to worry.”

The first character meant shame; the second, remorse. Repentance Cave was where criminals were confined.

What had he been so ashamed of? What did he need to repent for? Perhaps he regretted failing to prevent his Master from entering Nirvana. Unnamed had spent three months there, considering himself a sinner because he had failed to protect even the Green Jade Buddha Staff, the sacred treasure of Shaolin that his Master had entrusted to him before passing away.

“I had many thoughts in that darkness, where I could not see even an inch ahead.”

Unnamed stroked his cheek with a callused finger. A large portion of his face, covered in scars both large and small, had turned dark bluish-black.

Three months ago, the Yin-Cold Qi left behind by the enemy he had risked his life to stop had left that mark. It was also a yoke he would never be free of.

“I kept thinking that if only I had been a little stronger, I could have protected my Master. I could have properly carried out his final request.”

But regret was always late. A venerable monk respected by everyone had entered Nirvana unexpectedly. Someone had lost a close friend. And someone else had been consumed by guilt over failing to fulfill even his Master’s final words, so he had entered Repentance Cave.

*Anyone else would have been the same.*

I would have been no different. I did not even want to imagine how I would have felt if I had failed to treat Jeok Cheongang and had been forced to watch him leave this world. I might have returned to the days when I was F-rank Hunter Jin Taekyung and repeated the same cycle of deep regret and despair.

But pain changes people. For better or worse. In Unnamed’s case, it had been for the better. His heart might have been broken, but at least in terms of advancing his martial arts, the pain had helped him.

“This is only my personal opinion, but I doubt you spent all your time thinking in Repentance Cave.”

“Amitabha. Everything was thanks to the Buddha’s and Shaolin’s benevolence.”

Unnamed pressed his palms together toward the window, where sunlight streamed in, then gazed at me with calm eyes. There was a pure power in that gaze. A year ago, his body had been built from sturdy muscle. Now it had withered like an old tree. But the quiet aura flowing from his entire body was incomparable to what it had been before.

*He crossed the wall.*

The supreme realm every martial artist in Murim dreamed of reaching. There was no doubt that Unnamed had finally stepped into it.

At the awed look in my eyes, Unnamed gave a small nod.

“To heal a body that had fallen into critical condition and advance to a higher realm, I needed more than enlightenment. The Great Restoration Pill was one of those things.”

“Ah.”

If it was Shaolin’s Great Restoration Pill, it was an elixir whose effects ranked among the very best in the world.

*Yes. If it was the Great Restoration Pill, it might have been possible.*

The pill’s effects were one thing, but Unnamed was the Disciple whom Dharma King Hong Dao, a man capable of reading heavenly patterns, had personally brought in and raised with all his heart. He was a genius born with tremendous martial talent—not quite on Cheongpung’s level, perhaps, but still extraordinary. There was no doubt that he was worthy of the Great Restoration Pill.

He had reached the Supreme Peak realm while still in his thirties, proving not only his Master’s discerning eye, but also his own talent.

“Congratulations. I heard the Great Restoration Pill is an extremely precious item even within Shaolin.”

“That is why this humble monk vehemently refused it. But my Senior Brother Abbot gave it to me, telling me not to ask any questions. As it turned out, my Master seems to have said something about it several years ago. Perhaps… he knew this would happen.”

A faint smile touched Unnamed’s lips. He gazed into empty space for a moment, as though remembering his Master, then continued.

“Oh, my Senior Brother Abbot would also like to meet Benefactor Jin.”

“Your Senior Brother Abbot?”

I had never heard anything about the next Abbot after Dharma King Hong Dao. According to Gung Gibang, it was supposed to be one of the Dharma King’s direct Disciples, but spectacular events had kept occurring one after another, and I had never found the time to think about it.

“The two of you have probably never met face-to-face. In our lineage, he is my eldest Senior Brother, but he has been Abbot for less than a month, so it is only natural that you would not know him.”

“Ah, I see.”

“He said that he was sorry he had been too distracted to even say goodbye before sending you away last time.”

“He doesn’t need to apologize. I was in such a daze back then that I could hardly think straight, either.”

The Shaolin Bloodshed that had occurred during the Star-Array Grand Banquet had been an unprecedented incident, but I had left Henan for Sichuan within a day or two. To save Jeok Cheongang, who was in critical condition, I had needed to find the Divine Physician as quickly as possible.

“Amitabha. This humble monk was truly delighted when he belatedly heard that Benefactor Jeok had made a full recovery. My Master, who must be watching over me from somewhere, would have been relieved to see his friend in good health.”

“Ah, now that you mention it, you must have already met Old— No, my Master.”

“Until you woke up, we had been speaking together. At first, I almost failed to recognize him.”

“Well, he, uh… did change a little.”

“Yes. He changed as much as this humble monk did.”

“…Uh.”

What was I supposed to say to that?

As I hesitated in response to the sudden self-deprecating joke, Unnamed politely pressed his palms together.

“Amitabha. It was a joke.”

“Oh. Ah. I see.”

“You do not seem to have found it amusing. This humble monk will refrain from doing so again.”

The words *Please do* rose all the way to my throat.

A joke like that was only funny when it came from someone who hadn’t suffered quite so much. When Unnamed said it, the mood could only turn solemn in an instant. But I did not have the courage to nod.

“…No. It was funny.”

“Amitabha. Then this humble monk will continue.”

“…”

“That was the end of the joke.”

*Should I just crack his head open with a wooden fish?*

I stared at Unnamed in disbelief, then let out a quiet laugh. Still, the fact that he was making such clumsy jokes meant he had weathered everything much better than I had expected.

Even if I could not offer him any comfort, I could at least listen to his borderline temple jokes.

*That aside…*

“Where are we? This doesn’t look like Shaolin Temple.”

The sun was shining outside the window, so I seemed to have slept for a full day. But I had no idea where we actually were. As I looked around the room once more, Unnamed explained.

“We are at an inn near Mount Song. It was rented in the name of the Murim Alliance, so please stay here and get plenty of rest.”

“The Murim Alliance.”

It had been a distant-sounding term, but hearing it directly from Unnamed in Henan made it feel much more real. I got out of bed and approached the window to look at the scenery outside.

The first thing that caught my eye was the peak of Mount Song, rising in the distance so high it seemed to pierce the sky. Beneath it, buildings were packed densely along the mountain’s lower slopes, and people of every kind filled my view.

A Murim practitioner with a narrow-bladed sword at his waist. Another carrying a massive saber on his back without even a scabbard. Others carrying spears and twin axes…

“…”

Yes, they were all different, but something felt wrong.

*They’re scary.*

At the sight of me watching the Murim practitioners everywhere I looked, Unnamed let out a low laugh.

“Amitabha. They are Benefactors who heard the news and gathered from every corner of the world.”

“Even a quick glance makes it seem like there are more of them than there were at the Star-Array Grand Banquet.”

“If the Star-Array Grand Banquet was a festival for young prodigies, the founding of the Murim Alliance concerns everyone. Members of the orthodox and unorthodox factions have gathered, along with a considerable number of eccentric experts who were previously little known and had been living in seclusion.”

That made sense. The scale alone was entirely different, so it was only natural that so many people had gathered. If the Star-Array Grand Banquet had been the Han River fireworks festival, the founding of the Murim Alliance was Jindotgae One.[^1] Perhaps for that reason, there were almost no commoners to be seen, unlike during the Star-Array Grand Banquet.

*They can feel it too. They must know what is happening here.*

As I thought that to myself, a group of Murim practitioners crossing the main road suddenly caught my eye. Their aura was unusual enough that they could not be mistaken for ordinary martial artists. They clearly belonged to one of the great prestigious factions.

*Their clothes are strange, too. Who are they?*

I did not even need to ask Unnamed. Their arrival—wrapped in furs that did not suit the warm spring weather and wearing leather armor unlike ordinary Murim practitioners—had already caused whispers to spread in every direction.

“Could they be…”

“That’s right. They’re the Murong Family.”

“My word. It’s well over a thousand li from Liaoning to Henan. They arrived quickly.”

“Do you think people call them descendants of horse-riding nomads for nothing? What luck. I never expected to see people from the Murong Family in my lifetime.”

It was my first time seeing the Murong Family, too. Shanxi Province, where the Jin Family of Taiyuan was located, was also considered a frontier region, but Liaoning lay far to the northeast beyond Hebei. It was not somewhere one could visit as casually as the neighborhood next door.

They were so far away that I had heard even members of the Murong Family rarely ventured into the Central Plains.

*So this is that Murong Family.*

As one of the stronger families among the Five Great Families, the Murong Family’s reputation had reached my ears so often that I was sick of hearing it. I had heard that, unlike other factions, they even operated a cavalry unit.

*Maybe that’s why they all have muscles like horses.*

*The orthodox Murim, led by the Nine Sects and One Gang and the Five Great Families. It sounds like the unorthodox Murim has joined in, too. And on top of that, all the martial artists who belong nowhere at all…*

People often called the United States a melting pot of races. To me, Henan looked exactly like that right now. Of course, the people here were all the same or similar in terms of race, but regardless, every kind of Murim practitioner one could rarely see had gathered in one place.

*Three days.*

Three days from now, countless martial artists would gather beneath a single banner. United under the name of the Murim Alliance, they would raise their weapons and stand against Dark Heaven.

The moment that thought occurred to me as I looked at the people outside—

Boom!

A tremendous roar echoed from somewhere.

[^1]: Jindotgae One is South Korea’s highest military alert level, used when an enemy attack is considered imminent.
```

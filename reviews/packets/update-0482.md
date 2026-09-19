<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0482.txt",
      "sha256": "42153e95206c13c83fd579eb79e185ca560e166ea830da49aacb635c47711f9b",
      "bytes": 12726
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "fb2fdc23bb8b608076cbc3e3d6709badde0c5c3098d3fc367f685e38a5bf9b0d",
      "bytes": 3260
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "da374da9b85e81643994caacb4bf017ebcce78f853b2f92940526aec3a82cb33",
      "bytes": 154110
    },
    {
      "path": "characters/Blood Lord.md",
      "sha256": "cc4eea4ee07252b3d0fa35c85a6f0ac3128ddd69329fbd84def8425bc4af4a1e",
      "bytes": 803
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "63fb609a4f6c93ee1b334ce8d88f05e2ac4340f6846d844e85681e9729c3d7a9",
      "bytes": 1006
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "7b00621c3efb79f2ba1f015b03867454bbdb0b2faebd46b866d90d305dc958ac",
      "bytes": 553
    },
    {
      "path": "characters/Dongting Fisherman.md",
      "sha256": "adf67d0182de7c3ab0b5cb11d1519c70106e1396d076a9d6e85c3fd2d0736621",
      "bytes": 918
    },
    {
      "path": "characters/Gung Gibang.md",
      "sha256": "8af962b79dddc3531bb203029e919f03321d1b09ed6af3a9158308a80375b9b6",
      "bytes": 686
    },
    {
      "path": "characters/Honglan.md",
      "sha256": "0ff6bcfac4456eaa755de4326f0aacf0449926c639ab022d9b9ebfe329b2c42b",
      "bytes": 918
    },
    {
      "path": "characters/Human Butcher.md",
      "sha256": "1ab5eac5a1a0e8681cbf45d0e50171c771cde9f10707d2497df84bfcb69e3d75",
      "bytes": 667
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "c2ba2022f57d1191f4893b2f8c27fddc0d56b9ef4e4552771cfc3c9d25c50a4d",
      "bytes": 1108
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "baef68f0c2638349369e406779e7f65357efbd5efa78644a3c24acfbe8b164d3",
      "bytes": 1542
    },
    {
      "path": "characters/Jin Wikyung.md",
      "sha256": "e47a6ca8635a9f62097c6583b0a04531a27e77fd030ba3b7f52e59b3d30a2c55",
      "bytes": 1239
    },
    {
      "path": "characters/Ju Wongong.md",
      "sha256": "baf38cbc5bf28dd2f0bad32c64490b1e3530488b5e14d75a391072fd3d67c5e8",
      "bytes": 681
    },
    {
      "path": "characters/Mungyeong.md",
      "sha256": "dd8e5a091de57556b312c21b58ee298183ac0df17cd1d703cb6285bbc865b5d1",
      "bytes": 786
    },
    {
      "path": "characters/Song Ho.md",
      "sha256": "608de435e3aec04d4311cb741ca1388db8945fc0534537346da81cf33751a302",
      "bytes": 1866
    },
    {
      "path": "characters/Western Heaven Demon Lord.md",
      "sha256": "41505b9a0fda6d988dc272d47378d268320bccb0e9be41b5a14e752e3add1f36",
      "bytes": 888
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "54d2a68ec061c96217f142361f5de4d95f434d090b2a0d54aaabfc0533fdbf30",
      "bytes": 149353
    }
  ],
  "estimated_tokens": 14181
}
-->

# Durable State Update — Chapter 482

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 482. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 482. Profile updates may replace only one
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
  "chapter": 482,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 482,
    "continuity_sources": [482],
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
    "The Water God Dragon died after regaining its reason and giving Taekyung its purified Origin Essence, which humans call an inner core.",
    "The dragon's Memory Fragment showed its five-hundred-year history, including its benevolent rule of Dongting Lake and its sacrifice to contain the Gate's demonic qi.",
    "Taekyung identifies Honglan as the person who corrupted the benevolent Dongting Lake imugi and used it to kill many people.",
    "Honglan's silver hairpin carries a faint scent and was found in Taekyung's hair after the Memory Fragment ended.",
    "Honglan can enthrall people by seizing their emotions and souls; Officer Song is under her control and obeying her command to change the ship's destination.",
    "The Gate or rift that corrupted the Water God Dragon remains connected to unresolved questions involving demonic qi and Dark Heaven.",
    "Honglan's motives, her exact relationship to Dark Heaven, and the full extent of her role in the Hubei incidents remain unresolved.",
    "Gwak Bongchul is an elderly boatman from the Wuhan and Dongting Lake area who survived the Dongting Lake spirit's rampage, remembers the resulting deaths and bloodshed, and awakened after two days in Mungyeong's clinic.",
    "Mungyeong instructed Gwak to erase the incident from his memory and adopt a false account; Gwak has now regained consciousness without unusual symptoms and understands everything clearly, while Mungyeong has arranged his protection and compensation.",
    "The Dongting Fisherman is alive but severely injured, with crushed limbs, substantial Internal Injury, and serious Fear exposure after encountering the Water God Dragon at Donghu Stronghold.",
    "Gung Gibang has found a trace of Honglan after her whereabouts remained unknown."
  ],
  "continuity_sources": [
    481
  ],
  "open_questions": [
    "What is the Dongting Fisherman's exact role within Dark Heaven, and how was he connected to the earlier destruction inside the secret refuge?",
    "What are the origin and purpose of the symbols shared by the Arch Lich's magic circle and Dark Heaven's formations?",
    "Did the Mutated Water Dragon destroy Donghu Stronghold and the related Yangtze River Channel League strongholds, and why was no Moving Formation trace left?",
    "Who created or controlled the Gate or rift that corrupted the Water God Dragon, and how is that power related to Dark Heaven?",
    "Where does Gung Gibang's trace of Honglan lead, and why did Honglan corrupt the Water God Dragon?"
  ],
  "safe_through": 481,
  "temporary_decisions": [
    "Render 광폭화 as Berserk and preserve the System Status distinction.",
    "Render 장수 돌침대 as Jangsu stone bed and 효자손 as hyojason, each with an explanatory footnote when used.",
    "Retain established jang and geun measurements, established renderings of live-fish sashimi and bone-in sashimi, and gukbap with an explanatory footnote.",
    "Continue rendering 수염 as whiskers; distinguish Force, Sword Energy, Hellfire, and Water Breath.",
    "Render 원정 as Origin Essence, 내단 as inner core, 꽃뱀 as flower snake, 산재처리 as workers’ compensation, and 거열형 as tearing apart by chariots."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진위경    | **Jin Wikyung**    |
| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 청풍     | **Cheongpung**     |
| 하오문    | **Lower District Sect**          |
| 무당파    | **Wudang**                       |
| 암천     | **Dark Heaven**                  |
| 제갈세가   | **Zhuge Clan**                   |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 마교     | **Demonic Cult**                                 |                                                       |
| 지부장    | **Branch Leader**                            |
| 제자     | **Disciple**                                 |
| 상태               | **Status**                     |
| 노부      | **this old man / I**                                            |
| 귀가      | **your family**                                                 |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 공자      | **Young Master**                                                |
| 혈주 | **Blood Lord** | Title of the unidentified young man encountered by Han Su. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 동정어옹 | **Dongting Fisherman** | Publicly condemned the Yangtze River Channel League and disappeared three days before this chapter. |
| 궁기방 | **Gung Gibang** | Beggars' Sect Successor Beggar and finalist. |
| 홍란 | **Honglan** | Stage name of Ju Wongong's Lower District Sect singing courtesan; her real name is concealed. |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 주원공 | **Ju Wongong** | Qingxia Hall leader who claims distant kinship with the Emperor. |
| 문경 | **Mungyeong** | Young medical apprentice and newly introduced passenger. |
| 송호 | **Song Ho** | Elderly martial artist known as the Thousand-Faced Fox. |
| 서천마군 | **Western Heaven Demon Lord** | Title of the middle-aged antagonist who commands the summoned black-robed hunters. |
| 평화 | **Peace Guild** | Guild name. |
| 전서구 | **messenger pigeon** | Pigeon delivering the Lower District Sect's Jeongyang Branch report. |
| 성주 | **City Lord** | Official who sends the invitation for a gathering with young prodigies. |
| 개방 | **Beggars' Sect** | Murim organization counted among the Nine Sects and One Gang. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 호북 | **Hubei** | Province on Ju Gongsan's route from Guangdong to Henan. |
| 성도 | **Chengdu** | Sichuan destination of Taekyung's party. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 이무기 | **imugi** | Legendary serpent mentioned as the only comparable creature to a Thousand-Year Poison Horned Snake. |
| 이동진 | **Moving Formation** | Dark Heaven's inactive long-distance transportation formation. |
| 괴공절학 | **monstrous martial arts and supreme techniques** | Bizarre arts associated with the Demonic Cult. |
| 중단전 | **Middle Dantian** | Martial energy center opened by Jin during the battle. |
| 적벽 | **Red Cliffs** | Site where the Sea Serpent Society's leaders and core members were killed. |
| 호북성 | **Hubei Province** | Province where the chapter’s Dark Heaven incidents occurred. |
| 수신룡 | **Water God Dragon** | Legendary name for the true master of Dongting Lake; distinct from the modern Sea Serpent. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혁무진 | 진위경 | Jin Family subordinate to Lesser Family Head | Lesser Family Head | deferential | Uses 소가주님 while confessing that he accepted Taekyung's invitation. |
| 진위경 | 혁무진 | Lesser Family Head to direct family subordinate | you | formal-but-familiar | Uses 자네 while recognizing Mujin and instructing him to keep helping Taekyung. |
| 청풍 | 혁무진 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung includes Mujin among his 은인들 after receiving the skewers. |
| 혁무진 | 청풍 | martial artist to young master | Young Master | formal-deferential | Mujin uses 공자께서는 when asking why Cheongpung descended from the mountain. |
| 적천강 | 청풍 | overwhelming_elder_to_young_martial_artist | you / little punk | blunt, amused, and threatening | Jeok Cheongang uses 네, 이놈, and related blunt forms while testing Cheongpung. |
| 청풍 | 적천강 | young_martial_artist_to_overwhelming_elder | Grandpa Jeok | casual-familiar despite deference | Cheongpung uses 적 할아버지 while asking Jeok Cheongang to confirm Taekyung's condition; this is a familial form of address, not literal kinship. |
| 혁무진 | 적천강 | subordinate_to_overwhelming_elder | Great Hero Jeok | deferential and fearful | Mujin uses 적 대협 while reporting Jeok’s orders and Taekyung’s awakening. |
| 적천강 | 혁무진 | overwhelming_elder_to_junior_martial_artist | you stupid fool | blunt and mocking | Jeok calls Mujin a 멍청한 놈 after knocking him down during the attempted escape. |
| 진위경 | 적천강 | host_to_legendary_guest | Great Hero Jeok | formal-deferential | Introduces himself and pays respects to Jeok Cheongang as the Fire King. |
| 적천강 | 진위경 | elder_to_younger_family_head | you | gruff and teasing | Uses 자네 while mistaking Wikyung for Taekyung’s father and questioning his age. |
| 상인 | 적천강 | merchant_to_legendary_martial_master | Great Hero Jeok | deferential and flattering | Praises Jeok Cheongang while presenting the Poison-Averting Ring and requesting help. |
| 적천강 | 상인 | legendary_guest_to_merchant | you | blunt and transactional | Cuts off the merchant’s praise, asks his identity and origin, and accepts the gift without committing to the requested favor. |
| 상인 | 청년 | stranger_to_stranger | Young Brother | formal-polite | A merchant uses 소형제 after noticing the young man's sword, and the young man approves of the address. |
| 청년 | 상인 | stranger_to_stranger | friend | casual and shameless | The young man declares that they should be friends after drinking their Yeoahong. |
| 송호 | 청년 | elderly_martial_artist_to_younger_martial_artist | Young Hero | formal-polite | Song Ho calls out to the young man as 소협 at the chapter's end. |
| 혈주 | 적천강 | claimed enemy to enemy | your enemy | calm and threatening | The Blood Lord identifies himself as Jeok's enemy and claims to have killed Jeok's most precious friend. |
| 혈주 | 청풍 | hostile_opponent_to_newly_revealed_identity | Huashan's Invincible Divine Sword; Sword Saint's Disciple or grandson | mocking and taunting | Recognizes Cheongpung's public identity and needles him with his Sword Saint lineage while dismissing the added threat. |
| 청풍 | 문경 | martial_companion_to_medical_apprentice | Medical Apprentice | cheerful-polite | Cheongpung addresses Mungyeong as 의생님 while asking him to greet the Tang Clan. |
| 혁무진 | 궁기방 | squad_companion_to_Beggars_Sect_successor | Young Hero Gung | formal-polite, then pointed | Uses 궁 소협 while asking about the culprit and challenging Gung’s insults. |
| 서천마군 | 청풍 | commander_to_young_opponent | you | gentle and taunting | Uses 자네 while identifying Cheongpung and discussing the Blood Lord. |
| 서천마군 | 신의 | hostile_invader_to_physician | Divine Physician | calm and mocking | Uses 신의 and 그대 while taunting the physician and dismissing his objections. |
| 신의 | 서천마군 | physician_to_invading_fiend | fiend | defiant and formal | Calls the Western Heaven Demon Lord an 악귀 and orders him to leave. |
| 서천마군 | 적천강 | hostile_invader_to_unconscious_patient | you | calm and predatory | Says someone wants to see Jeok Cheongang and attempts to move him with Seizing an Object Through Empty Space. |
| 적천강 | 서천마군 | hostile_opponents | you bastard | blunt and threatening | Jeok addresses the Western Heaven Demon Lord with 네놈 while defending Taekyung and ordering him not to touch his Disciple. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 문경 | 적천강 | old_acquaintances | Fire King | familiar and grave | The figure bearing Mungyeong’s name greets Jeok Cheongang by his established epithet. |
| 궁기방 | 혁무진 | squad_companions | you; that lunatic | insulting-casual | Gung Gibang mocks Hyuk Mujin's injuries and calls him a lunatic for attacking the Third Fiend. |
| 궁기방 | 청풍 | martial_companions | Young Hero Cheongpung | formal-polite | Gung Gibang uses 청 소협 while asking why Cheongpung is at the temporary clinic. |
| 적천강 | 문경 | overwhelming elder to old acquaintance | you / little punk | mocking and threatening | Mocks Mungyeong's expression and threatens to poke out his eyes. |
| 주원공 | 청풍 | Qingxia Hall young master to Huashan Divine Dragon | you | formal and guarded | Uses 그대 while tentatively offering Cheongpung an invitation to Dongting Lake. |
| 주원공 | 홍란 | employer to kept singing courtesan | Honglan | commanding | Orders Honglan to greet Taekyung and presents her as the singing courtesan he keeps at his side. |
| 궁기방 | 군관 | martial_artist_to_military_officer | Officer | insulting-casual | Gung Gibang uses 군관 나리 while mocking the officer's ignorance of Dark Heaven. |
| 군관 | 대협 | military_officer_to_martial_hero | Great Hero | formal-deferential | The officer addresses Taekyung as 대협 while asking whether he knows the culprit. |
| 적천강 | 수신룡 | legendary_martial_master_to_dying_spirit_beast | you | wary and trembling | Jeok asks what the Water God Dragon is after witnessing its mental communication. |
| 문경 | 수신룡 | physician_to_dying_spirit_beast | you | guarded and curious | Mungyeong asks whether the Water God Dragon knows him. |

## Listed compact profiles

### Blood Lord.md

# Blood Lord (혈주)

- **Safe through:** Chapter 476
- **Aliases:** None
- **Role:** Young-seeming high-ranking Dark Heaven figure who seeks Jin Taekyung, Cheongpung, and Jeok Cheongang after escaping the confrontation at Mount Song.
- **Personality:** Calm, confident, theatrically frivolous, casually cruel, and ruthlessly destructive; treats allies as disposable tools and enjoys provoking stronger opponents.
- **Voice:** Light, cheerful, and joking even while threatening or killing; turns cold and contemptuous when challenged.
- **Relationships:** He and the Western Heaven Demon Lord serve the same master; he now seeks to personally kill Cheongpung, Jeok Cheongang, and Jin Taekyung, while his former contact Han Su is dead.

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 479
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, the grandson and Disciple of Sword Saint Mae Jonghak, and a Supreme Peak martial master known as the Huashan Divine Dragon.
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, a deep love of martial arts, competitive pride, unusual resistance to monster-induced Fear, and discomfort when someone copies his martial arts.
- **Voice:** Dreamy and hazy, with innocent, polite phrasing; he has begun imitating Taekyung's profanity.
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions while Taekyung is his only true martial rival; Tang Sadok has temporarily entrusted Mimi to him.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 480
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Dongting Fisherman.md

# Dongting Fisherman (동정어옹)

- **Safe through:** Chapter 481
- **Aliases:** None
- **Role:** The Dongting Fisherman is a previous-generation Supreme Peak master whose water arts rival the Seafaring King; he joined Dark Heaven, committed the Dongting Lake massacre, was captured alive, and is now severely injured with crushed limbs, substantial Internal Injury, and serious Fear exposure after encountering the Water God Dragon at Donghu Stronghold.
- **Personality:** The Dongting Fisherman appears eerily emotionless and savage, eating live fish raw and reacting violently when provoked.
- **Voice:** Not established.
- **Relationships:** The Dongting Fisherman opposed the Yangtze River Channel League and was monitored by the Lower District Sect for several years after friction with it, while current records place him in Hubei Province.

### Gung Gibang.md

# Gung Gibang (궁기방)

- **Safe through:** Chapter 481
- **Aliases:** Successor Beggar, Beggar Prince, pure-blooded beggar, ultimate beggar
- **Role:** Gung Gibang is the Beggars' Sect Successor Beggar and a unique eight-knot disciple.
- **Personality:** Vulgar, aggressive, and quick-tempered.
- **Voice:** Blunt, profane, and vividly threatening.
- **Relationships:** Gung Gibang is a rival finalist alongside Baek Woo and Zhuge Gyun who trades insults with Taekyung, uses Beggars’ Sect intelligence to investigate Tang Taesang’s murder and Dark Heaven’s Hubei forces, and has now found a trace of Honglan.

### Honglan.md

# Honglan (홍란)

- **Safe through:** Chapter 481
- **Aliases:** None
- **Role:** Honglan is a Lower District Sect courtesan who uses a stage name while serving as Ju Wongong's singing courtesan.
- **Personality:** Discreet about her real identity and professionally alluring.
- **Voice:** Clear, pure, and alluring, with humble formal speech toward honored guests.
- **Relationships:** Honglan is kept at Ju Wongong's side as a singing courtesan, belongs to the Lower District Sect, lost her clan and parents overnight as a child, can respond to Taekyung through Sound Transmission, is the sole surviving eyewitness to the Dongting Lake attack who knows several possible locations of the Dongting Fisherman's hidden refuges, corrupted the benevolent imugi in Dongting Lake and used it to kill many people, and can enthrall people and command them.

### Human Butcher.md

# Human Butcher (인도)

- **Safe through:** Chapter 467
- **Aliases:** None
- **Role:** Former mysterious Han Chinese mounted-bandit power in Northern Gaoyuan commanding fifty subordinates; a Peak master killed by an unnamed old man in a single move
- **Personality:** Cold, intimidating, and murderous; he kills people as though slaughtering livestock
- **Voice:** Cold, curt, and quietly threatening
- **Relationships:** He is one of four powerful participants at the Northern Gaoyuan gathering, intimidates Temur, and has claimed Ghost Sword Wipeng as his personal target in the proposed attack

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 470
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers and Vice Squad Leader of the Jin Dragon Squad.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 481
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin and Furnace Fire Pure Blue, and Jin Taekyung's Master.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, and pathologically afraid of water. His meeting with Taekyung rekindled his will to live, making him determined to extend his life despite his illness.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Jin Wikyung.md

# Jin Wikyung (진위경)

- **Safe through:** Chapter 450
- **Aliases:** Junzi Sword
- **Role:** Jin Wikyung is the thirty-six-year-old Lesser Family Head and future Family Head of the Jin Family of Taiyuan, the Alliance Leader who unified Shanxi Murim and Shanxi Province's foremost landowner and magnate.
- **Personality:** Calm, authoritative, and politically capable in public; protective and affectionate toward Taekyung beneath a stern mask. Takes responsibility for his people, acts decisively under pressure, and prioritizes family survival.
- **Voice:** Restrained, formal, and commanding with subordinates; openly affectionate, proud, and occasionally exuberant with Taekyung.
- **Relationships:** Taekyung's eldest brother and future Family Head; Taekyung trusts him as a martial-arts mentor and family protector. Member and acting leader of the Jin Family of Taiyuan. Commands Wipeng and the family's forces. Has worked with Jeok Cheongang, who trained Taekyung under Wikyung's arrangement. Jin Mukyung is his younger brother and a potential successor alongside Taekyung.

### Ju Wongong.md

# Ju Wongong (주원공)

- **Safe through:** Chapter 479
- **Aliases:** Qingxia Hall young master
- **Role:** Ju Wongong is an exiled Qingxia Hall young master and a distant imperial relative of the Zhu ruling house who was punished for embezzling wealth while abusing his imperial authority.
- **Personality:** Entitled, status-conscious, theatrical, and amused by violence until his own protection is overcome.
- **Voice:** Pompous and imperious, with formal declarations of rank and authority.
- **Relationships:** His Qingxia Hall entourage and four Peak guards obey him; he asserts kinship with the Emperor.

### Mungyeong.md

# Mungyeong (문경)

- **Safe through:** Chapter 481
- **Aliases:** None
- **Role:** Mungyeong is the legendary physician known as the former Divine Physician and Slaughter Saint, a former assassin who passed the Divine Physician title to his Disciple, and he has reached the Returned to Youth realm.
- **Personality:** Compassionate, resolute, resourceful, and calm under extreme pressure.
- **Voice:** His Mungyeong persona is timid, deferential, and cheerful, while his Slaughter Saint voice is dry, impassive, and blunt.
- **Relationships:** Dong Feng is his Disciple; Jeok Cheongang is an old acquaintance, and Jeok Cheongang, Jin Taekyung, Cheongpung, and the two Sect Leaders know his Slaughter Saint identity.

### Song Ho.md

# Song Ho (송호)

- **Safe through:** Chapter 267
- **Aliases:** Thousand-Faced Fox
- **Role:** Elderly Peak master known as the Thousand-Faced Fox; he has a wooden prosthetic leg and overwhelming physical strength, was formerly the head of the Murim Alliance's Hidden Shadow Pavilion, and, after Hong Dao sought him out over Dark Heaven, recalled his former subordinates and helped restore the Hidden Shadow Pavilion; he is an intelligence operative and master of disguise who can identify people through their faces, habits, and bone structure; he lost his leg during the final battle against the Demonic Cult decades ago and suffers recurring pain from the old injury; he suspects he previously encountered Jongni Chu and is now investigating him; he attends the Star-Array Grand Banquet's main-event duels every day before leaving during the third day; he now recognizes that Jongni Chu is closely connected to the day his leg was severed and that the connection is not mere coincidence; after receiving a report that Shadow Killer had been found, he sent agents to secure the dueling platform and went there himself when he sensed the clash between Supreme Peak masters; after arriving at Mount Song with hundreds of martial artists, he recognized Jongni Chu as Sword Saint Mae Jonghak and confirmed that Mae had saved his life in the past.
- **Personality:** Outwardly genial and relaxed, but observant, forceful, and intimidating when pursuing information.
- **Voice:** Lightly genial and conversational, turning quietly coercive during interrogation.
- **Relationships:** Takes the Geumwa Merchant Group's merchants away to question them about the young martial artist who drank their Yeoahong; recognizes Jin Taekyung as Jeok Cheongang's Disciple and praises his preliminary performance.

### Western Heaven Demon Lord.md

# Western Heaven Demon Lord (서천마군)

- **Safe through:** Chapter 467
- **Aliases:** None
- **Role:** Former Protector of the Divine Cult who commands Dark Heaven's assault on the Sichuan Tang Clan, lost the Myriad-Poison Ring to Jin Taekyung, suffered a crushed ankle and a torn wrist, and was temporarily possessed by the Lord of Heaven before the borrowed body was destroyed.
- **Personality:** Cold, detached, patient, and utterly ruthless toward those he interrogates or hunts.
- **Voice:** Controlled and dispassionate, with concise statements delivered in a quiet, threatening tone.
- **Relationships:** Tang Taesang and the Heaven-Shaking Venerable Nun were his latest victims, he lost one arm taking their lives, and the Qilian Three Fiends now submit to him alongside his hundreds of black-robed hunters.

## Korean source

```text
＃482화



홍란의 흔적을 찾았다.

궁기방의 한마디에 격동한 것은 나뿐만이 아니었다. 수신룡과의 전투가 끝난 직후, 홍란의 정체에 대해 들어 알고 있는 적천강과 문경 역시 즉각적으로 반응했다.

“그 개 같은 년을 찾았다고?”

“어찌 된 것입니까?”

적천강의 돌직구와 여전히 신분을 숨긴 문경의 가증스러운 질문에 이어, 내가 굳은 얼굴로 입을 열었다.

“흔적?”

중요한 건 결과다.

홍란을 찾았다는 것이 아니다. 궁기방은 분명 ‘홍란의 흔적’을 찾았다고 했고, 이것이 의미하는 바는 명백했다.

“찾지 못했군.”

이제야 호흡을 가다듬은 궁기방이 고개를 끄덕였다.

“아직까지는. 하지만 본 방의 제자들은 물론이고 무당, 제갈세가와 관군에도 전서구를 띄웠으니 곧…….”

“아니. 못 찾을 거야.”

단호하게 대답한 내가 말을 이었다.

“그 정도로 쉽게 잡힐 거였다면 진작 꼬리가 밟혔겠지.”

관군은 머릿수만 많은 머저리고, 그나마 개방과 무당파, 제갈세가가 믿을 만하지만 그들이 홍란을 찾는다는 건…… 글쎄. 아무리 생각해도 확률이 희박하다.

이렇게 쉽게 잡힐 리 없다는 심리적인 측면을 제외하고서라도, 근처에 숨겨 둔 이동진이라도 있다면 전부 닭 쫓던 개 신세니까.

“그런데 정확히 무슨 흔적을, 어디에서 찾은 거지? 자세히 말해 봐.”

“적벽(赤壁)에서 군선 한 척이 발견되었다.”

“혹시 네가 말하는 군선이…….”

“그래. 마지막으로 홍란의 모습이 목격되었던 바로 그 군선이다. 이미 관부 측에서 확인도 끝마쳤어.”

이틀 전, 우리가 동정어옹을 찾기 위해 떠난 직후 관군들은 홍란을 호북성부로 옮기고자 했다.

황족인 주원공과 함께 살아남은 유일한 생존자이자, 표면적으로는 나와 함께 주원공을 구출한 일등 공신이니 관부로서는 당연한 선택이었다.

‘그게 마지막 모습이었지만.’

이후 홍란이 몸을 실었던 군선은 유령처럼 증발했다. 배에 타고 있던 백여 명의 관군과 수부들도 함께.

그런데 지금, 궁기방이 바로 그 군선을 찾았다는 소식을 가져온 것이다.

“……그래서. 어떻게 됐지?”

사실 질문을 하기도 전에 답은 이미 나와 있는 것이나 다름없었다.

‘아마, 모두 죽었겠지.’

이미 들어서 알고 있었다. 홍란과 함께 군선에 승선해 있던 이들이 암천과는 아무런 연관도 없는 평범한 이들이라는 사실을.

그런 이들에게 홍란이 수고비 몇 푼 던져 주고 평화롭게 손을 흔들며 헤어졌을 리는 만무하다.

일그러진 궁기방의 표정 역시 그런 짐작을 뒷받침하는 증거였다.

다만.

“모두 합하여 아흔넷. 하나같이 스스로 목을 찔러 자결했다.”

“뭐?”

이것까지는 미처 예상치 못했다.

말없이 눈을 깜빡이던 나는 가까스로 목소리를 끄집어 냈다.

“그 많은 사람들이…… 집단으로 자결했다고?”

“틀림없다. 관군이라면 기본적으로 소지하고 있던 단검으로 자신의 목을 찔렀어. 시신들을 확인해 보니 웃고 있는 채로 숨이 끊겨 있었다더군. 물론 홍란의 모습은 어디에도 보이지 않았고.”

“이런 미친.”

차라리 홍란의 손에 죽었다면 이렇게까지 놀라지 않았을 거다.

하지만 이건 예상을 훌쩍 벗어나는 종류의 죽음이었다.

대규모 집단 자살, 게다가 웃고 있었다니.

순간 말을 잇지 못하던 그때, 문경과 적천강이 거의 동시에 입술을 뗐다.

“이건.”

“그래, 섭혼술(攝魂術)이 틀림없다. 그것도 아주 강력한.”

섭혼술. 말 그대로 상대의 넋을 홀려 조종하는 괴공절학(怪功絶學)이다.

과거 읽었던 무협 소설에서 자주 언급되었기에 뭔지는 알고 있었지만, 지금껏 무림에서 지내며 섭혼술이 등장한 건 이번이 처음이었다.

“아니, 그게 진짜 있는 거였어요?”

내 물음에 적천강이 어처구니없다는 듯이 되물었다.

“그게 오백 년 묵은 이무기를 잡은 놈이 할 소리냐?”

“……어. 그렇게 따지면 할 말 없긴 한데.”

“아득한 세월 동안 내려온 천년마도(千年魔道)의 총본산이 바로 마교다. 암천은 바로 그 마교의 후신. 섭혼술을 사용하는 연놈들이 날뛰어도 이상하지 않지.”

“하지만 전에 말씀하셨을 때는 섭혼술이 별것 아니라고 하셨잖아요.”

“그거야 노부한테나 그렇지. 홍란, 그 빌어먹을 요녀가 네게 진작 섭혼술을 사용하지 않은 이유도 비슷한 맥락일 게다.”

“제가 초절정 고수라서?”

“벽을 넘었다는 것은 그자의 심신이 지고한 경지에 도달했다는 것을 의미하지. 하물며 중단전(中丹田)을 깨운 네 녀석에게는 오죽할까.”

거기까지 말한 적천강은 문득 눈살을 찌푸리며 한마디를 보탰다.

“아니, 어쩌면 그년이 원하던 것이 이무기와 일전을 벌이는 것이었을 수도 있었겠군.”

“어찌 되었건 간에, 흉수가 섭혼술의 고수이며, 유령처럼 사라졌다는 것이 중요하지요.”

그때, 조용히 끼어든 문경의 말에 궁기방이 고개를 저었다.

“한 가지 더 있어.”

“……무슨?”

“조사 결과 군선에 탑승했던 인원은 총 아흔여섯이었다. 홍란을 제외해도 한 명이 남지.”

“잠깐. 그렇다는 건…….”

“생존자가 한 명 있다. 군선의 책임자이자 호북성부에 속한 군관이지.”

“……!”

생존자라니.

나를 포함한 모두가 눈을 크게 뜬 그 순간, 마른침을 삼킨 궁기방이 말을 이었다.

“지금 이곳으로 오고 있다.”

잠깐의 침묵이 흐른 뒤, 적천강이 딱딱하게 굳은 얼굴로 입을 열었다.

“한데, 요즘 어린 것들 사이에서 노부에게 말 놓는 것이 유행이냐?”

“……저, 저는 적 대협께 드린 말씀이 아닌데.”

“복날 개처럼 처맞아야 정신을 차리지. 엎드려.”



* * *



“이름은 송호. 호북성에서 이름난 상인 집안의 자제로, 아비가 힘써 준 덕분에 호북성주의 부름을 받았습니다. 성주로부터 흉수를 데려오라는 명령을 받아 이틀 전 파견되었지요.”

젊었을 적 여자깨나 울렸을 법한 외모의 중년인은 초조한 목소리로 말을 이었다.

“평소 색을 밝히고, 여러 가지 추문이 있긴 했지만 어릴 적부터 문무에 재능이 있었던 것은 맞습니다. 호북성주가 곁에 둔 것도 아비의 후광 때문만이 아니라, 일 처리가 확실하고 영특했기 때문이지요.”

글쎄. 전에는 어땠을지 몰라도, 지금은 아닌 것 같은데.

나는 중년인, 하오문 호북 지부장의 말을 흘려들으며 포승줄에 묶인 채 앉아 있는 청년을 응시했다.

푸석푸석한 피부. 눈은 귀신에라도 홀린 듯이 풀려 있었고 벌어진 입가에서는 투명한 침이 흐르는 중이었다.

툭. 투둑.

멍하니 침만 흘리는 젊은 군관의 모습을 지켜보던 적천강이 미간을 좁혔다.

“섭혼술에 제대로 걸려들었군. 이미 제정신이 아니야.”

적천강의 말에 십분 동의한다.

눈앞의 청년에게서는 더 이상 이성이 느껴지지 않았다. 장래가 촉망되던 군관 대신, 영혼이 빠져나간 인형이 이 자리에 있었다.

“상태는 어떻습, 어때?”

급하게 말을 고친 내 물음에 문경이 천천히 고개를 저었다.

“틀렸습니다. 장기간 지켜본다면 모르겠습니다만…… 당장으로서는 일말의 가망조차 없어 보입니다.”

“가망이 없다면 어느 정도지?”

“넋이 빠져나갔다는 것은 죽은 것과 다름없는 것. 이 상태라면 스스로 말하거나 행동할 수도 없을 겁니다.”

생각보다 훨씬 심각한 상태다.

유일한 생존자가 호송되었다는 소식을 듣고 급하게 달려온 진위경이 입을 열었다.

“다른 명의에게 보인다면 생각이 다를 수도 있지 않겠나?”

“누가 보아도 같을 겁니다. 저와 의견이 다르다면 아마 그자는 돌팔이일 겁니다.”

“허어, 설령 신의(神醫)께서 살피신다고 해도 말인가?”

“……예.”

형님. 쟤가 걘데요.

나는 차오르는 말을 꿀꺽 삼켰고, 홍란의 정체를 오인함으로써 잠시나마 암천의 주구 취급을 받았던 하오문 호북 지부장은 굽실거리며 물러났다.

그리고, 좌중이 잠깐 침묵에 잠겨 있던 바로 그 순간이었다.

“아, 으, 어.”

“……!”

서늘한 한기가 등골을 타고 솟구친다.

나는 물론이고 주위에 있던 모두가 눈을 부릅뜬 채 젊은 군관을 바라보았다.

몽롱하게 풀어진 두 눈동자, 하지만 그와는 반대로 헤벌어져 있던 입이 조금씩 움찔거리며 목소리가 새어 나오고 있었다.

“어으, 아.”

“……이럴 리가.”

문경이 믿을 수 없다는 표정으로 중얼거렸다.

지금껏 수많은 환자를 보살피고 치료했던 그다. 신의라 불릴 만한 의술과 함께 고강한 무위를 지닌 초절정 고수인 만큼, 문경이 확신에 차서 내린 진단은 절대적인 법칙이나 다름없었다.

아니, 적어도 몇 초 전까지는 그랬다.

“이 무슨!”

드물게도 큰 소리를 낸 문경이 신속하게 군관의 맥을 짚었다.

그의 표정이 수신룡을 바라볼 때 만큼이나 복잡미묘해지는 것이 보였다.

“분명 그대로인데, 어째서?”

그리고 다음 순간, 나를 포함한 이 자리의 모두는 들을 수 있었다.

군관의 입술 사이로 흘러나온 목소리를.

“절대적인 것도, 변하지 않는 것도 없지. 이쯤 되면 알 법도 한데. 안 그래?”

“……!”

군관의 것임에 분명한 사내의 목소리.

그러나 그 목소리에 담긴 누군가의 흔적을 읽은 나와 궁기방은 동시에 눈을 마주쳤고, 동시에 한 사람의 이름을 외쳤다.

“홍란!”

한 줄기 번개가 정수리를 관통한 기분.

혁무진과 청풍이 이 자리에 있었다면 그 두 사람 역시 같은 반응이었을 것이다.

나는 가라앉은 눈빛으로 젊은 군관, 아니 머나먼 어딘가에서 군관의 몸을 빌려 마주한 홍란을 바라보며 입을 열었다.

“어디냐. 이 시벌 년아.”

“어머, 우리 어린 공자님께서 생각보다 입이 험하시네. 여인한테 욕하는 사내는 인기 없는데.”

“좆 까. 난 원래 인기 없으니까.”

“그런 대답은 예상 못 했는데. 역시 걸작이야.”

“개소리 집어치우고 어디 있는지나 말해라. 걸레짝으로 만들어 줄 테니까.”

“들었던 것보다 귀여운 성격이네. 재미도 있고.”

귀에 익은 맑은 웃음소리가 군관의 입술 사이로 비집고 흘러나온다.

입꼬리는 여전한데 목소리만 흘러나오는 광경에 소름이 끼칠 지경이다.

그러나 나는 이런 와중에도 중요한 한마디를 놓치지 않았다.

“……들었던 것보다?”

“이미 알고 있지 않니? 우리에게는 눈과 귀가 많다는 걸. 그중에서도 혈주(血主)가 가장 많이 떠들긴 했지.”

“암천(暗天). 그래, 그럴 줄 알았지.”

99.9%의 가능성도 결국 마지막 0.1%가 없다면 짐작에 불과하다.

아무런 거리낌 없이 스스로 정체를 밝힌 홍란은 산뜻한 목소리로 말을 이었다.

“혈주에게 들었던 것보다 훨씬 강해져 있어서 놀랐어. 하긴, 아직까지도 겨우 그 정도였다면 이무기에게 당하기 전에 서천마군(西天魔君)의 손에 죽었겠지.”

어째서일까. 분노는 도무지 사그라들 기미가 보이지 않는데, 오히려 마음과 목소리는 차분하게 가라앉는다.

나는 처음과 달리 놀랄 만큼 담담한 목소리로 물었다.

“넌 누구지?”

그저 순수한 의문.

물어보면서도 순순히 답해 줄 거라는 생각은 하지 않았다.

그러나 홍란은 단 한 마디로 내 예상을 간단히 깨트렸다.

“남천마후(南天魔后).”

“남천……마후?”

이 개새끼들이 아주, 동서남북으로 지랄을 하는구나.
```

## Final English reading copy

```markdown
# Chapter 482

“We found a trace of Honglan.”

Gung Gibang’s announcement did not agitate only me. Immediately after the battle with the Water God Dragon ended, Jeok Cheongang and Mungyeong—both of whom already knew what we had learned about Honglan’s identity—reacted as well.

“You found that goddamned bitch?”

“What happened?”

After Jeok Cheongang’s blunt question and Mungyeong’s infuriating inquiry, still made while concealing his identity, I spoke with a hardened expression.

“A trace?”

The result was what mattered.

Gung Gibang had not said they found Honglan. He had clearly said they found *a trace of Honglan*, and the meaning was obvious.

“You didn’t find her.”

Gung Gibang, who had only just caught his breath, nodded.

“Not yet. But I’ve sent messenger pigeons to not only the disciples of our sect but also Wudang, the Zhuge Clan, and the government troops, so soon—”

“No. You won’t find her.”

I answered firmly and continued.

“If she were easy enough to catch, we would have picked up her trail long ago.”

The government troops were idiots with nothing but numbers. The Beggars’ Sect, Wudang, and the Zhuge Clan were at least reliable, but the idea of them finding Honglan…

Well. No matter how I looked at it, the odds were slim.

Even setting aside my gut feeling that there was no way she would be caught this easily, if she had a Moving Formation hidden nearby, we would all be left like dogs staring helplessly at the roof after the chicken got away.

“But what exactly did you find a trace of, and where? Tell me everything.”

“A military vessel was found at Red Cliffs.”

“Could the military vessel you’re talking about be…”

“That’s right. It’s the very vessel where Honglan was last seen. The authorities have already confirmed it.”

Two days ago, shortly after we left to find the Dongting Fisherman, the government troops had tried to move Honglan to the Hubei provincial government.

She was the only survivor who had lived through the incident alongside the imperial relative Ju Wongong. On the surface, she was also the chief contributor who had rescued Ju Wongong alongside me. From the authorities’ perspective, it was the obvious choice.

*Though that was the last time anyone saw her.*

After that, the military vessel Honglan had boarded vanished like a ghost.

So did the roughly one hundred government troops and sailors aboard it.

And now Gung Gibang had brought us news that the very same vessel had been found.

“…And? What happened?”

In truth, I already knew the answer before I asked.

*They’re probably all dead.*

I had already heard that the people who boarded the vessel with Honglan were ordinary men with no connection to Dark Heaven.

There was no way Honglan had tossed them a few coins for their trouble, waved goodbye peacefully, and gone on her way.

The grim expression on Gung Gibang’s face only supported my guess.

Except—

“Ninety-four in total. Every one of them committed suicide by stabbing themselves in the throat.”

“What?”

I had not expected that.

I blinked silently, then somehow managed to force out my voice.

“All those people… committed suicide together?”

“Without a doubt. They used the daggers that government troops carried as standard equipment and stabbed themselves in the throat. When the bodies were examined, they were said to have died with smiles on their faces. Of course, Honglan was nowhere to be found.”

“What the hell?”

I would not have been this shocked if Honglan had simply killed them herself.

But this was a kind of death far beyond anything I had expected.

A mass suicide.

And they had been smiling?

For a moment, I could not continue. Then Mungyeong and Jeok Cheongang both spoke almost simultaneously.

“This is…”

“Yeah. It has to be the Soul-Seizing Technique. And a very powerful one.”

The Soul-Seizing Technique.

As the name suggested, it was one of the monstrous martial arts and supreme techniques that bewitched and controlled an opponent’s soul.

I knew what it was because it had often appeared in the wuxia novels I had read in the past, but this was the first time I had encountered it in the Murim.

“Wait. That actually exists?”

Jeok Cheongang stared at me as though I had said something absurd.

“Is that something the man who took down a five-hundred-year-old imugi should be saying?”

“…Well, when you put it that way, I don’t really have anything to say.”

“For ages, the Demonic Cult has been the central seat of the Thousand-Year Demonic Path. Dark Heaven is the successor of that very Demonic Cult. It would hardly be strange for people who use the Soul-Seizing Technique to be running wild.”

“But you said before that the Soul-Seizing Technique was nothing special.”

“That’s only true against this old man. The reason that wretched witch Honglan didn’t use it on you from the beginning is probably similar.”

“Because I’m a Supreme Peak master?”

“Breaking through a wall means that one’s body and mind have reached a supreme realm. And how much more so for you, with your Middle Dantian awakened?”

Jeok Cheongang paused there, then suddenly frowned and added,

“No. Perhaps what that bitch wanted was for you to fight the imugi.”

“Either way, what matters is that the culprit is a master of the Soul-Seizing Technique and that she vanished like a ghost.”

Mungyeong quietly joined the conversation. Gung Gibang shook his head.

“There’s one more thing.”

“…What?”

“The investigation found that there were ninety-six people aboard the military vessel in total. Even excluding Honglan, that leaves one person.”

“Wait. If that’s the case…”

“There’s one survivor. The officer in charge of the military vessel, and a military officer attached to the Hubei provincial government.”

“……!”

A survivor?

Everyone, myself included, stared wide-eyed at Gung Gibang. After swallowing hard, he continued.

“He’s on his way here now.”

A brief silence followed.

Then Jeok Cheongang spoke with a stiff expression.

“By the way, is speaking informally to this old man a trend among young people these days?”

“…I wasn’t speaking to Great Hero Jeok.”

“You won’t come to your senses until you’ve been beaten like a dog on slaughter day. Get down.”

* * *

“His name is Song Ho. He is the son of a prominent merchant family in Hubei Province, and his father pulled strings to secure him a post under the City Lord of Hubei Province. Two days ago, the City Lord dispatched him with orders to bring in the culprit.”

The middle-aged man, whose looks must have broken plenty of women’s hearts in his youth, continued in an anxious voice.

“He was a womanizer and had been involved in several scandals, but it’s true that he showed talent in both literary and martial pursuits from a young age. The City Lord kept him close not merely because of his father’s influence, but because he was sharp and dependable when it came to handling matters.”

I didn’t know what he had been like before, but he certainly didn’t seem that way now.

I ignored the middle-aged man—the Hubei Branch Leader of the Lower District Sect—and watched the young man sitting there bound in ropes.

His skin was dry and rough. His eyes were unfocused, as though he had been possessed by a ghost, and clear saliva dripped from the corner of his open mouth.

*Drip. Drip.*

Jeok Cheongang watched the young officer mindlessly drooling and narrowed his brow.

“He’s been thoroughly caught by the Soul-Seizing Technique. He isn’t in his right mind anymore.”

I agreed with Jeok Cheongang completely.

There was no trace of reason left in the young man before us. Instead of a promising military officer, a doll with its soul pulled out was sitting there.

“How is his condi—how is he?”

At my hurried correction, Mungyeong slowly shook his head.

“It’s hopeless. I cannot say what prolonged observation might reveal, but at present, he does not appear to have even the slightest chance.”

“If there’s no hope, how bad is he?”

“When one’s soul has left the body, it is no different from death. In this state, he will not be able to speak or act on his own.”

His condition was far worse than I had expected.

Jin Wikyung, who had hurried over after hearing that the sole survivor had been escorted here, spoke up.

“Would another renowned physician have a different opinion?”

“No matter who examines him, they will reach the same conclusion. If their opinion differs from mine, they are probably a quack.”

“Good heavens. Even if the Divine Physician examined him?”

“…Yes.”

*Hyung. That’s the guy.*

I swallowed the words rising in my throat. The Hubei Branch Leader of the Lower District Sect—who had briefly been treated as an agent of Dark Heaven after mistaking Honglan’s identity—bowed repeatedly and withdrew.

And it was at that exact moment, while the room was briefly silent, that—

“Ah… uh… oh.”

“……!”

A cold chill rose up my spine.

Everyone around me, myself included, stared at the young officer with our eyes wide open.

His two eyes were still hazy and unfocused. But his slack mouth began to twitch little by little, and a voice seeped out.

“Uh… ah.”

“…That’s impossible.”

Mungyeong muttered with an expression of disbelief.

He had cared for and treated countless patients. With medical skill worthy of the title Divine Physician and the martial prowess of a Supreme Peak master, Mungyeong’s confident diagnoses were practically absolute laws.

Or at least they had been until a few seconds ago.

“What is this?”

Mungyeong rarely raised his voice, but now he did as he swiftly took the officer’s pulse.

His expression grew as complex and subtle as it had been when he looked at the Water God Dragon.

“It’s definitely unchanged. So why?”

And then everyone present, myself included, heard it.

The voice that flowed between the officer’s lips.

“Nothing is absolute, and nothing remains unchanged forever. You’d think you would have learned that by now. Don’t you agree?”

“……!”

It was unmistakably a man’s voice, and unquestionably the officer’s.

But Gung Gibang and I both recognized the trace of someone else in it. We looked at each other and shouted the same name at the same time.

“Honglan!”

It felt as though a bolt of lightning had pierced the crown of my head.

If Hyuk Mujin and Cheongpung had been here, they would have reacted the same way.

I looked at the young officer—or rather, at Honglan, confronting me from some distant place through the officer’s body—with a sunken gaze and spoke.

“Where are you, you fucking bitch?”

“Oh my. Our Young Master has a rougher mouth than I expected. Men who swear at women aren’t very popular, you know.”

“Fuck that. I’ve never been popular anyway.”

“I didn’t expect that answer. You really are a masterpiece.”

“Cut the bullshit and tell me where you are. I’ll turn you into a rag.”

“You’re cuter than I’d heard. And you’re funny, too.”

Her familiar, clear laughter slipped out through the officer’s lips.

The corners of his mouth remained the same while only her voice came out of them. The sight was enough to raise goose bumps.

Even so, I did not miss one important phrase.

“…Than you’d heard?”

“You already know, don’t you? We have many eyes and ears. Blood Lord did most of the talking.”

“Dark Heaven. Yeah, figures.”

Even a 99.9 percent possibility was nothing more than a guess if it lacked the final 0.1 percent.

Honglan had revealed her affiliation without the slightest hesitation and continued in a bright voice.

“I was surprised. You’ve become much stronger than Blood Lord said you were. Still, if you were only that strong even now, the Western Heaven Demon Lord would have killed you before the imugi got to you.”

Why was this happening?

My anger showed no sign of fading, yet my mind and voice were growing calmer instead.

Unlike before, I asked in a surprisingly composed voice,

“Who are you?”

It was nothing more than a genuine question.

Even as I asked, I did not expect her to answer willingly.

But Honglan shattered my expectations with a single word.

“The Southern Heaven Demon Empress.”

“The Southern… Heaven Demon Empress?”

*These fucking bastards are really screwing around in every direction—east, west, south, and north.*
```

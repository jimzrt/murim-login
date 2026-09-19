<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0483.txt",
      "sha256": "3de668ecfabf9911ef88c26e33b0155064ddab6647ec60dd9755d587029a2bfb",
      "bytes": 13423
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "ccdec66db01cf39a672b1390e522d011284006ae09c193c31f39f0ba567b2cc4",
      "bytes": 2816
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "99219305c1dfc00361fcf3ad3b419fea1ff69529859391400fb603e562083363",
      "bytes": 154620
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "c1a6362a4c185d2acb55bfbc7e4088a955081cc76f94b50e4bcc8ddd6a64a269",
      "bytes": 1006
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "6974d0907a0d17ef014e5654d0964e7e923a8dc86e4136064f4bb407ef3885e2",
      "bytes": 553
    },
    {
      "path": "characters/Gung Gibang.md",
      "sha256": "1e8f31317eaaeb9d8710991ca06921e77a7c8242426152b2d07b44617a41c9cc",
      "bytes": 686
    },
    {
      "path": "characters/Honglan.md",
      "sha256": "d78e8133431be0512ed1116c8009284fe4b74626625748accd77c7341604d7f5",
      "bytes": 973
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "bc87d5b6fb54e63df2f213c6ab5167b8221a2d0f0353e116afea610e9ae96063",
      "bytes": 1542
    },
    {
      "path": "characters/Jin Wikyung.md",
      "sha256": "4405437591fdc97a34d589ca76def4575924c724f07ee237e2a0ea216fe593d4",
      "bytes": 1239
    },
    {
      "path": "characters/Mungyeong.md",
      "sha256": "9550bee18990c763728459d652d81b32060fadc27e6369bda7223ef9ebee44a9",
      "bytes": 786
    },
    {
      "path": "characters/Western Heaven Demon Lord.md",
      "sha256": "e5b250d25308eb4294d92cc6b56e126e197a9f016c39aa1ac3caa62180a9b8a1",
      "bytes": 888
    },
    {
      "path": "characters/Zhuge Feng.md",
      "sha256": "4a2bdb2ab03cacdc81841414c266008b7b56f69bcfce340cc1b51167a0e22c48",
      "bytes": 626
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "2b984b636ad5092e24806b4400f52eca0b4845b31788a4f76fff88ba97648586",
      "bytes": 149734
    }
  ],
  "estimated_tokens": 12832
}
-->

# Durable State Update — Chapter 483

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 483. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 483. Profile updates may replace only one
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
  "chapter": 483,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 483,
    "continuity_sources": [483],
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
    "Honglan corrupted the benevolent Dongting Lake imugi and used it to kill many people.",
    "Honglan can enthrall people by seizing their emotions and souls, and she can now speak remotely through a controlled person's body.",
    "Honglan escaped from the military vessel last associated with her at Red Cliffs; ninety-four passengers and crew members died by mass suicide, while the surviving officer Song Ho remains incapacitated.",
    "Honglan identifies herself as the Southern Heaven Demon Empress and confirms that Dark Heaven has many eyes and ears, including Blood Lord's reports.",
    "Honglan's exact location, motives, and full relationship to Dark Heaven remain unresolved.",
    "The Gate or rift that corrupted the Water God Dragon remains connected to unresolved questions involving demonic qi and Dark Heaven.",
    "The Dongting Fisherman is alive but severely injured, with crushed limbs, substantial Internal Injury, and serious Fear exposure after encountering the Water God Dragon at Donghu Stronghold.",
    "Gung Gibang has traced the vessel connected to Honglan to Red Cliffs."
  ],
  "continuity_sources": [
    481,
    482
  ],
  "open_questions": [
    "Where is Honglan, and what does she intend to do as the Southern Heaven Demon Empress?",
    "What is the Dongting Fisherman's exact role within Dark Heaven, and how was he connected to the earlier destruction inside the secret refuge?",
    "What are the origin and purpose of the symbols shared by the Arch Lich's magic circle and Dark Heaven's formations?",
    "Did the Mutated Water Dragon destroy Donghu Stronghold and the related Yangtze River Channel League strongholds, and why was no Moving Formation trace left?",
    "Who created or controlled the Gate or rift that corrupted the Water God Dragon, and how is that power related to Dark Heaven?"
  ],
  "safe_through": 482,
  "temporary_decisions": [
    "Render 광폭화 as Berserk and preserve the System Status distinction.",
    "Render 장수 돌침대 as Jangsu stone bed and 효자손 as hyojason, each with an explanatory footnote when used.",
    "Retain established jang and geun measurements, established renderings of live-fish sashimi and bone-in sashimi, and gukbap with an explanatory footnote.",
    "Continue rendering 수염 as whiskers; distinguish Force, Sword Energy, Hellfire, and Water Breath.",
    "Render 원정 as Origin Essence, 내단 as inner core, 꽃뱀 as flower snake, 산재처리 as workers’ compensation, 거열형 as tearing apart by chariots, 섭혼술 as Soul-Seizing Technique, and 남천마후 as Southern Heaven Demon Empress."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진위경    | **Jin Wikyung**    |
| 적천강    | **Jeok Cheongang** |
| 청풍     | **Cheongpung**     |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 살성     | **Slaughter Saint**           | —              |
| 태원진가   | **Jin Family of Taiyuan**        |
| 열화문    | **Fire Gate Clan**               |
| 암천     | **Dark Heaven**                  |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 표국     | **Escort Bureau**                            |
| 표사     | **escort**                                   |
| 소국주    | **Young Bureau Head**                        |
| 제자     | **Disciple**                                 |
| 은인     | **Benefactor**                               |
| 게이트     | **Gate**              |
| 태원     | **Taiyuan**            |
| 화산     | **Huashan**            |
| 구화산    | **Mount Jiuhua**       |
| 노부      | **this old man / I**                                            |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 궁기방 | **Gung Gibang** | Beggars' Sect Successor Beggar and finalist. |
| 홍란 | **Honglan** | Stage name of Ju Wongong's Lower District Sect singing courtesan; her real name is concealed. |
| 문경 | **Mungyeong** | Young medical apprentice and newly introduced passenger. |
| 서천마군 | **Western Heaven Demon Lord** | Title of the middle-aged antagonist who commands the summoned black-robed hunters. |
| 제갈풍 | **Zhuge Feng** | Current Family Head of the Zhuge Clan. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 마기 | **demonic qi** | Demonic energy discussed as a possible effect of the pill. |
| 주신 | **God of Drinking** | Wipeng's drinking epithet. |
| 개방 | **Beggars' Sect** | Murim organization counted among the Nine Sects and One Gang. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 점혈 | **Pressure-Point Strike** | System-named technique used by Jeok Cheongang on Taekyung. |
| 운남 | **Yunnan** | Region from which Jongni Chu comes. |
| 멸염신권 | **Flame-Extinguishing Divine Fist** | Named fist technique Taekyung announces at the chapter's end. |
| 후개 | **Successor Beggar** | Title of the Beggars' Sect successor competing in the preliminaries. |
| 천주 | **Lord of Heaven** | Authority invoked by the masked attackers. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 미미 | **Mimi** | Worker at Honghwaru referenced in Taekyung's joke. |
| 개방도 | **Beggars' Sect disciple** | Member of the Beggars' Sect. |
| 의생 | **medical apprentice** | Mungyeong's occupation. |
| 살수 | **assassin** | Professional killer considered as a possible suspect. |
| 미미쨩 | **Mimi-chan** | Affectionate form used for Tang Mimi. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 이무기 | **imugi** | Legendary serpent mentioned as the only comparable creature to a Thousand-Year Poison Horned Snake. |
| 와룡객 | **Crouching Dragon Guest** | Epithet of Zhuge Feng. |
| 수신룡 | **Water God Dragon** | Legendary name for the true master of Dongting Lake; distinct from the modern Sea Serpent. |
| 남천마후 | **Southern Heaven Demon Empress** | Title Honglan uses when revealing her identity. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 적천강 | 청풍 | overwhelming_elder_to_young_martial_artist | you / little punk | blunt, amused, and threatening | Jeok Cheongang uses 네, 이놈, and related blunt forms while testing Cheongpung. |
| 청풍 | 적천강 | young_martial_artist_to_overwhelming_elder | Grandpa Jeok | casual-familiar despite deference | Cheongpung uses 적 할아버지 while asking Jeok Cheongang to confirm Taekyung's condition; this is a familial form of address, not literal kinship. |
| 무인 | 진위경 | vassal_martial_artist_to_lesser_family_head | Lesser Family Head | formal-deferential | The Mount Heng martial artists greet Jin Wikyung as 소가주님 while pledging loyalty. |
| 진위경 | 적천강 | host_to_legendary_guest | Great Hero Jeok | formal-deferential | Introduces himself and pays respects to Jeok Cheongang as the Fire King. |
| 적천강 | 진위경 | elder_to_younger_family_head | you | gruff and teasing | Uses 자네 while mistaking Wikyung for Taekyung’s father and questioning his age. |
| 청풍 | 문경 | martial_companion_to_medical_apprentice | Medical Apprentice | cheerful-polite | Cheongpung addresses Mungyeong as 의생님 while asking him to greet the Tang Clan. |
| 서천마군 | 청풍 | commander_to_young_opponent | you | gentle and taunting | Uses 자네 while identifying Cheongpung and discussing the Blood Lord. |
| 서천마군 | 신의 | hostile_invader_to_physician | Divine Physician | calm and mocking | Uses 신의 and 그대 while taunting the physician and dismissing his objections. |
| 신의 | 서천마군 | physician_to_invading_fiend | fiend | defiant and formal | Calls the Western Heaven Demon Lord an 악귀 and orders him to leave. |
| 서천마군 | 적천강 | hostile_invader_to_unconscious_patient | you | calm and predatory | Says someone wants to see Jeok Cheongang and attempts to move him with Seizing an Object Through Empty Space. |
| 적천강 | 서천마군 | hostile_opponents | you bastard | blunt and threatening | Jeok addresses the Western Heaven Demon Lord with 네놈 while defending Taekyung and ordering him not to touch his Disciple. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 문경 | 적천강 | old_acquaintances | Fire King | familiar and grave | The figure bearing Mungyeong’s name greets Jeok Cheongang by his established epithet. |
| 궁기방 | 청풍 | martial_companions | Young Hero Cheongpung | formal-polite | Gung Gibang uses 청 소협 while asking why Cheongpung is at the temporary clinic. |
| 청풍 | 미미 | handler_to_companion_snake | Mimi | cheerful-commanding | Cheongpung repeatedly calls and commands the Thousand-Year Poison Horned Snake. |
| 진위경 | 막내 | older brother to younger brother | my youngest | intimate and informal | Jin Wikyung uses 막내야 affectionately for Jin Taekyung. |
| 적천강 | 문경 | overwhelming elder to old acquaintance | you / little punk | mocking and threatening | Mocks Mungyeong's expression and threatens to poke out his eyes. |
| 적천강 | 제갈풍 | senior_martial_artist_to_old_acquaintance | you / ill-mannered brat | blunt, familiar, and teasing | Jeok treats Zhuge Feng as the younger acquaintance he remembers from childhood. |
| 제갈풍 | 적천강 | younger_old_acquaintance_to_legendary_senior | Senior | respectful but relaxed | Zhuge Feng recalls Jeok's earlier visit and addresses him as an old senior. |
| 제갈풍 | 궁기방 | family_head_to_beggars_sect_successor | Successor Beggar | calm and conversational | Uses 후개 when confirming Gung Gibang's guess about the broken weapon. |
| 홍란 | 은인 | rescued_survivor_to_rescuer | Benefactor | humble-formal | Honglan addresses Taekyung as Benefactor after he rescued her. |
| 궁기방 | 군관 | martial_artist_to_military_officer | Officer | insulting-casual | Gung Gibang uses 군관 나리 while mocking the officer's ignorance of Dark Heaven. |
| 군관 | 대협 | military_officer_to_martial_hero | Great Hero | formal-deferential | The officer addresses Taekyung as 대협 while asking whether he knows the culprit. |
| 제갈풍 | 문경 | old acquaintance to revealed legendary assassin | Slaughter Saint | excited and respectful | Zhuge Feng identifies Mungyeong by his established sobriquet after recognizing his identity. |
| 문경 | 제갈풍 | legendary_senior_to_younger_family_head | you; burden | blunt, insulting, and commanding | Mungyeong orders Zhuge Feng onto his back and dismisses his objections. |
| 청풍 | 제갈풍 | young_martial_artist_to_family_head | Great Hero Zhuge Feng | cheerful and polite | Cheongpung addresses Zhuge Feng as 제갈풍 대협, but deliberately mispronounces the name once as 제갈퐁 for comic effect. |
| 제갈풍 | 청풍 | family_head_to_younger_martial_artist | you | familiar and polite | Zhuge Feng uses 자네 while instructing Cheongpung and responding to his advice. |
| 적천강 | 수신룡 | legendary_martial_master_to_dying_spirit_beast | you | wary and trembling | Jeok asks what the Water God Dragon is after witnessing its mental communication. |
| 문경 | 수신룡 | physician_to_dying_spirit_beast | you | guarded and curious | Mungyeong asks whether the Water God Dragon knows him. |
| 적천강 | 궁기방 | overwhelming_elder_to_younger_martial_artist | you | blunt and threatening | Jeok Cheongang rebukes Gung Gibang for speaking informally and orders him to lie down. |

## Listed compact profiles

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 482
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, the grandson and Disciple of Sword Saint Mae Jonghak, and a Supreme Peak martial master known as the Huashan Divine Dragon.
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, a deep love of martial arts, competitive pride, unusual resistance to monster-induced Fear, and discomfort when someone copies his martial arts.
- **Voice:** Dreamy and hazy, with innocent, polite phrasing; he has begun imitating Taekyung's profanity.
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions while Taekyung is his only true martial rival; Tang Sadok has temporarily entrusted Mimi to him.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 482
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Gung Gibang.md

# Gung Gibang (궁기방)

- **Safe through:** Chapter 482
- **Aliases:** Successor Beggar, Beggar Prince, pure-blooded beggar, ultimate beggar
- **Role:** Gung Gibang is the Beggars' Sect Successor Beggar and a unique eight-knot disciple.
- **Personality:** Vulgar, aggressive, and quick-tempered.
- **Voice:** Blunt, profane, and vividly threatening.
- **Relationships:** Gung Gibang is a rival finalist alongside Baek Woo and Zhuge Gyun who trades insults with Taekyung, uses Beggars’ Sect intelligence to investigate Tang Taesang’s murder and Dark Heaven’s Hubei forces, and has now found a trace of Honglan.

### Honglan.md

# Honglan (홍란)

- **Safe through:** Chapter 482
- **Aliases:** None
- **Role:** Honglan is a Lower District Sect courtesan who uses a stage name, served as Ju Wongong's singing courtesan, and identifies herself as the Southern Heaven Demon Empress.
- **Personality:** Discreet about her real identity and professionally alluring.
- **Voice:** Clear, pure, and alluring, with humble formal speech toward honored guests.
- **Relationships:** Honglan is kept at Ju Wongong's side as a singing courtesan, belongs to the Lower District Sect, lost her clan and parents overnight as a child, can respond to Taekyung through Sound Transmission, is the sole surviving eyewitness to the Dongting Lake attack who knows several possible locations of the Dongting Fisherman's hidden refuges, corrupted the benevolent imugi in Dongting Lake and used it to kill many people, and can enthrall people and command them.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 482
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin and Furnace Fire Pure Blue, and Jin Taekyung's Master.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, and pathologically afraid of water. His meeting with Taekyung rekindled his will to live, making him determined to extend his life despite his illness.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Jin Wikyung.md

# Jin Wikyung (진위경)

- **Safe through:** Chapter 482
- **Aliases:** Junzi Sword
- **Role:** Jin Wikyung is the thirty-six-year-old Lesser Family Head and future Family Head of the Jin Family of Taiyuan, the Alliance Leader who unified Shanxi Murim and Shanxi Province's foremost landowner and magnate.
- **Personality:** Calm, authoritative, and politically capable in public; protective and affectionate toward Taekyung beneath a stern mask. Takes responsibility for his people, acts decisively under pressure, and prioritizes family survival.
- **Voice:** Restrained, formal, and commanding with subordinates; openly affectionate, proud, and occasionally exuberant with Taekyung.
- **Relationships:** Taekyung's eldest brother and future Family Head; Taekyung trusts him as a martial-arts mentor and family protector. Member and acting leader of the Jin Family of Taiyuan. Commands Wipeng and the family's forces. Has worked with Jeok Cheongang, who trained Taekyung under Wikyung's arrangement. Jin Mukyung is his younger brother and a potential successor alongside Taekyung.

### Mungyeong.md

# Mungyeong (문경)

- **Safe through:** Chapter 482
- **Aliases:** None
- **Role:** Mungyeong is the legendary physician known as the former Divine Physician and Slaughter Saint, a former assassin who passed the Divine Physician title to his Disciple, and he has reached the Returned to Youth realm.
- **Personality:** Compassionate, resolute, resourceful, and calm under extreme pressure.
- **Voice:** His Mungyeong persona is timid, deferential, and cheerful, while his Slaughter Saint voice is dry, impassive, and blunt.
- **Relationships:** Dong Feng is his Disciple; Jeok Cheongang is an old acquaintance, and Jeok Cheongang, Jin Taekyung, Cheongpung, and the two Sect Leaders know his Slaughter Saint identity.

### Western Heaven Demon Lord.md

# Western Heaven Demon Lord (서천마군)

- **Safe through:** Chapter 482
- **Aliases:** None
- **Role:** Former Protector of the Divine Cult who commands Dark Heaven's assault on the Sichuan Tang Clan, lost the Myriad-Poison Ring to Jin Taekyung, suffered a crushed ankle and a torn wrist, and was temporarily possessed by the Lord of Heaven before the borrowed body was destroyed.
- **Personality:** Cold, detached, patient, and utterly ruthless toward those he interrogates or hunts.
- **Voice:** Controlled and dispassionate, with concise statements delivered in a quiet, threatening tone.
- **Relationships:** Tang Taesang and the Heaven-Shaking Venerable Nun were his latest victims, he lost one arm taking their lives, and the Qilian Three Fiends now submit to him alongside his hundreds of black-robed hunters.

### Zhuge Feng.md

# Zhuge Feng (제갈풍)

- **Safe through:** Chapter 472
- **Aliases:** Crouching Dragon Guest
- **Role:** Zhuge Feng is the current Family Head of the Zhuge Clan and father of its Lesser Family Head, Zhuge Gyun.
- **Personality:** Analytical and disarmingly casual, he treats comfort and time as principles while delivering grave intelligence with unsettling directness.
- **Voice:** Clear, calm, polished, and conversational, with understated humor and pointed questioning.
- **Relationships:** Zhuge Gyun is his son, and Zhuge Gonghu was his grandfather.

## Korean source

```text
＃483화



“남천……마후?”

젊은 군관의 몸을 빌린 홍란, 아니 남천마후(南天魔后)가 경쾌한 어조로 말했다.

“그 별호, 다른 사람의 입으로 들으니 낯부끄럽네.”

“낯부끄럽기는 시발. 동서남북으로 개지랄을 하고 자빠졌네. 그래서 동쪽은 동정모쏠이고 북쪽은 북괴김씨냐?”

“별호는 달라도 얼추 비슷하게 맞췄어. 생각했던 것보다는 똑똑한데?”

“……젠장.”

서천마군, 그리고 남천마후.

이 정도면 각각 동서남북을 염두에 두고 지은 별호라는 건 미미쨩도 알겠다.

서천마군도 죽을 고비를 몇 번이나 넘긴 끝에 겨우 잡은 괴물인데, 그런 연놈들이 최소 셋이나 더 있다니.

하지만 그보다 더 중요한 의문이 남았다.

나는 넋 나간 표정의 군관을 응시하며 입을 열었다.

“어떻게 한 거지?”

“어머, 우리 어린 대협께서 뭐가 그리 궁금하실까.”

“알잖아. 뭘 말하는지.”

맥없이 풀려 있는 군관의 눈동자에 문득 기광(奇光)이 스쳤다.

다른 이의 시선을 통해 나를 물끄러미 바라보던 남천마후가 한 마디를 툭, 하고 내뱉었다.

“너, 봤구나?”

“……!”

“고작 이틀 만에 찾아냈을 리는 없을 테고, 역시 영물은 영물이라 이건가. 하긴, 오백 년 묵은 이무기라면 확실히 신령스러운 존재긴 하지.”

단숨에 모든 것을 파악한 남천마후가 매끄럽게 한마디를 덧붙인다.

“그럼 알고 있을 텐데. 내가 대답하지 않으리라는 것도.”

아직도 생생하다. 기억의 파편을 통해 엿보았던 게이트(Gate)의 흔적. 그리고 그곳으로부터 흘러나온 마기에 물드는 수신룡의 모습이.

그것은…… 있을 수도 없고 있어서도 안 되는 일이었다.

적어도 이곳, 무림에서만큼은 나타날 수 없는 불가해(不可解)의 현상.

그러나 남천마후는, 암천은 불가능을 현실로 끌어 올렸다. 차라리 거짓말이라고 믿고 싶을 지경이다.

“도대체, 너희들의 목적이 뭐지?”

“목적?”

다음 순간, 군관의 입술 사이로 맑은 웃음소리가 흘러나왔다. 꾸며내지 않은 즐거움이 담긴 웃음소리.

한바탕 소리 내어 웃던 남천마후가 말을 이었다.

“아이야. 나 역시 명에 따라 움직이는 하찮은 종일뿐. 그 누구라 해도 그분의 뜻을 짐작할 수는 없단다.”

그분. 이 두 글자가 누굴 가리키는 것인지, 이 자리에 있는 모두는 알고 있다.

적천강이 용암처럼 끓어오르는 듯한 목소리로 중얼거렸다.

“천주(天主).”

으드득.

뼈 어긋나는 소리와 함께, 삐걱거리는 목각 인형처럼 돌아간 고개가 적천강을 향했다.

“구화산에 미친 노괴(老怪)가 산다는 말은 들었지. 화왕 적천강, 그대의 말이 맞아. 바로 그분이시지. 누구보다 위대하고 고귀하신…….”

“산 채로 태워 죽여도 시원찮을 개호로 새끼겠지. 감히 뉘 앞에서 함부로 요설(妖舌)을 놀리느냐.”

차가운 불길이 담긴 적천강의 말에 짧은 침묵이 내려앉았다.

이내 굳게 닫혀 있던 군관의 입술이 스르륵 열리며, 착 가라앉은 목소리가 흘러나왔다.

“말을 가려서 하는 게 좋을 텐데? 당신의 질긴 명줄을 좀 더 오래 붙들고 싶다면.”

“내 명줄?”

적천강이 코웃음 치며 내게 물었다.

“네 녀석이 말해 보거라. 노부 명줄 끊겠다고 달려든 놈들이 어찌 되었는지.”

“뒈졌죠. 한 놈도 빠짐없이.”

“하면 지금껏 노부가 써 내려간 살생부에 놈이 아니라 년을 포함시킬까 하는데, 어찌 생각하느냐?”

두말할 것도 없이 찬성이다. 나는 엄지를 번쩍 치켜세웠다.

“이 시대의 진정한 페미니스트십니다.”

“패미비수타? 그게 뭐냐?”

“공정하신 분이라는 뜻입니다. 남녀노소 관계없이 평등하게 조지시는.”

“요새 젊은 놈들이 쓰는 말인가? 어찌 되었건 의미는 마음에 드는구나.”

만족스럽게 고개를 끄덕인 적천강이 군관의 몸에 깃든 남천마후를 노려보며 말을 이었다.

“들었느냐? 패미비수타인 노부가 네년과 천주인지 뭐시긴지 하는 놈을 치죄할 터이니, 그때까지 목닦고 기다리거라.”

어. 멸염신권이 페미권이 되기 전에 지금이라도 말려야 되나.

하지만 덕분에 속은 뻥 뚫렸다. 복잡하던 머릿속도 깨끗하게 정리된 기분이다.

‘그래, 시벌. 죄다 족치면 그만이지.’

어차피 열화문의 모토가 그거 아닌가. 적이라고 생각하는 놈들은 닥치는 대로 깨고, 부수고, 태워 버리는 거.

어차피 남천마후는 내 의문에 대한 답을 해 주지 않을 것이다. 그렇다면 암천이 무슨 짓을 벌이든, 철저하게 깨부수며 나아가면 그만이다.

‘어차피 선택권은 없으니까.’

기호지세(騎虎之勢). 애당초 난폭한 호랑이의 등에 올라탄 이상 남은 길은 두 가지뿐이었다.

그리고 나는 등에서 나가떨어지는 대신, 호랑이의 골통을 박살 내서라도 이 미친 몸부림을 끝낼 거다.

아니, 반드시 그래야만 한다.

“후우…….”

참았던 숨을 내뱉은 나는 군관을 향해 바짝 고개를 들이밀었다. 영혼이 빠져나간 눈동자 너머, 머나먼 어딘가를 직시하며 입을 열었다.

“다음에 만나면…… 넌 반드시 죽어.”

군관의 입술이 달싹였다.

“그래, 나도 그날이 기다려지는구나. 그리고 그때가 오면 이 자리의 누구도 살아남지 못하겠지.”

천천히 돌아가는 고개. 초점이 잡히지 않는 희뿌연 눈동자가 방 안의 모두를 차례차례 응시한다.

그러나 누구도 그 소름 끼치는 시선을 피하지 않았다. 문경 역시 그중 한 사람이었다.

“덧없는 살생(殺生)을 멈추는 게 좋을 겁니다. 칼날은 결국 자신에게 돌아오는 법이니.”

다른 이의 시선을 의식한 예의 바른 어조와 목소리. 하지만 그 안에는 극소수의 사람만이 알아차릴 수 있는 칼날이 숨어 있다.

그것이 오직 피로 물든 길을 걸어온 고금제일의 살수. 살성(殺星)이라는 지고한 무인이 지닌 진면목이었다.

“……묘한 아이로구나. 신의라는 자가 궁금해질 만큼.”

그러나 다른 이의 몸을 빌린 남천마후는 문경의 정확한 정체를 파악하지 못한 것 같았다.

신의의 제자라는 표면적인 신분은 알고 있을지는 몰라도, 자그마치 사십 년 전 사라진 살성과 어린 의생을 연결하기에는 그 고리가 너무나도 희미했으니까.

그리고 문경에 대한 남천마후의 의심이 깊어지기도 전에, 진위경이 무거운 목소리로 입을 열었다.

“태원진가의 이름을 걸고 맹세컨대, 당신은 우리 막내를 털끝 하나 건드릴 수 없을 거요.”

“태원진가라. 그 알량한 가문과 하찮은 무공으로 저 아이를 지킬 수 있을까?”

“시궁창 쥐도 제 새끼를 위해서라면 호랑이와도 맞서 싸우는 법. 궁금하다면 오시구려. 직접 보여 드리는 수밖에.”

상식을 아득히 벗어난 기이한 현상에도 진위경은 평정심을 잃지 않았다.

그가 담담하고도 결연하게 말을 끝맺기가 무섭게, 궁기방이 떡 진 머리를 긁적였다.

“진 대협, 본 방을 빼놓으시면 섭섭합니다.”

“개방을 깜빡했군. 함께하겠나?”

“제 스승님이 그러셨습니다. 개 몽둥이 하나로는 동네 똥개밖에 못 잡지만, 백 개가 모이면 호랑이도 때려잡는다고. 하물며 십만의 거지들이 모인다면 어떻겠습니까?”

개방의 진정한 힘은 바로 압도적인 머릿수에서 나온다.

뭉뚱그려 십만 개방도라 칭해도 이의를 제기할 수 없을 만큼 엄청난 물량.

그들의 정점으로부터 한 걸음을 남겨둔 후개(後丐), 궁기방이 누런 이빨을 드러내며 씩 웃어 보였다.

“참 아리따운 처자였는데 이렇게 되어 안타깝구려. 하지만 어쩌겠소. 내가 몽둥이로 그 고운 얼굴을 후려갈겨도 너무 원망 마시오.”

“원망?”

군관의 입꼬리가 슬며시 위로 솟구쳤다.

피부가 찢어질 듯 기괴한 웃음을 짓는 그의 입을 빌린 남천마후가 모두를 향해 말했다.

“지금처럼 안달할 필요는 없을 거야. 그리 오래 걸리지는 않을 테니…….”

서서히 꺼져 가는 모닥불처럼 사그라지는 목소리.

어느새 군관의 입술 사이로 흘러나오는 검붉은 핏물에, 나는 망설임 없이 그의 완맥을 움켜쥐었다.

후우웅.

순식간에 단전으로부터 솟구친 공력이 그의 몸 안으로 흘러 들어갔지만, 이미 시작된 죽음은 돌이킬 수 없었다.

쓸모없어진 물건은 버려지는 법.

어쩌면 남천마후가 군관을 살려 둔 이유는 바로 이 때문이었을 것이다.

‘잠시 몸을 빌릴 꼭두각시.’

울컥. 주르륵.

입뿐만이 아니다.

눈, 코, 귀…… 이른바 칠공(七空)이라 불리는 인체의 구멍으로부터 검붉은 핏물이 펑펑 쏟아졌다.

수 갑자의 공력이나 점혈로도 막을 수 없는 죽음이 군관의 눈앞에 드리워져 있었다.

“늦었습니다.”

문경의 목소리가 귓가에 울려 퍼진 그 순간.

천천히 벌어지는 입술 사이로 흥건한 핏물과 함께 마지막 한 마디가 흘러나왔다.

“모든 것은, 그분의 뜻대로.”

스륵. 툭.

그것으로 끝이었다.

모든 생명력을 소진한 군관의 고개가 축 늘어지며 숨이 멎었다.

한 사람의 죽음과 함께 침묵이 내려앉은 그때, 장원을 향해 다가오던 기척이 문 앞에서 멈췄다.

“저어, 들어가도 될까요?”

귀에 익은 목소리.

이윽고 조심스럽게 열리는 문 틈새로 빼꼼 고개를 내민 한 청년이 입을 열었다.

“은인, 제갈퐁 대협께서 찾으시는데요.”

“제갈퐁이 아니라 제갈풍.”

“네. 제갈퐁 대협이요.”

“……말을 말아야지.”

한숨을 내쉰 나는 자리에서 일어났다.

지금 와룡객 제갈풍이 어디 있으며 어디로 가야 하는지, 나를 왜 찾는 건지 이유조차 묻지 않았다.

처음부터 그들에게 ‘그 장소’를 알려 준 사람은 다름 아닌 나였으니까.

“그래서, 찾았어?”

“네.”

청풍이 눈을 빛내며 말을 이었다.

“은인께서 말씀하신 바로 그곳이 맞아요.”

그곳이란 수신룡의 기억 속에 있던 바로 그 장소.

그래, 빌어먹을 게이트(Gate)다.



* * *



홍란, 아니 남천마후는 감았던 눈을 떴다.

잘게 흔들리는 사두마차의 비단을 걷어 올리자, 격자 창문 밖으로 울창한 풀숲이 보였다. 습하고 무더운 남방의 날씨에 땀을 흘리는 표국의 인원들도.

“흐음.”

턱을 괸 채 창밖을 바라보는 남천마후의 모습은 그 자체로 한 폭의 그림이나 다름없었다.

그리고 그때, 홀린 듯이 힐끔거리는 표국 사내들의 머리 위로 한 줄기 불호령이 떨어졌다.

“모두 한눈팔지 말고 운송에 집중해라! 며칠 후에 만나게 될 묘족(苗族)들에게 뒈지기 싫으면!”

걸쭉한 말과는 달리 목소리의 주인은 눈부신 미모를 자랑하는 여인이었다.

햇빛을 피하고자 푹 눌러쓴 죽립 아래로 쭉 뻗은 콧날은 칼날 같았고, 적당히 그을린 피부는 보기 좋았다.

‘여 표사? 흔치 않은데.’

거친 사내들을 한참이나 윽박지르던 여 표사가 남천마후의 시선을 알아차리기까지는 그리 오랜 시간이 필요하지 않았다.

말고삐를 늦추고 마차 옆에 붙은 그녀가 창문 너머를 향해 말을 걸었다.

“혹시 문제가 있으신가요?”

“문제는요. 고생해 주신 덕분에 편히 가고 있는걸요.”

“그럼 어찌하여 저를 그리…….”

“그냥요.”

“네?”

남천마후가 싱긋 웃으며 덧붙였다.

“참 어리고 예뻐서. 그래서 보고 있었어요.”

“아, 감사합니다.”

중소 표국의 소국주인 여 표사는 당황했지만, 애써 그런 기색을 숨겼다.

칭찬해 주는 상대가 여자도 반할 만큼의 미녀인 건 둘째 치고서라도, 상당한 재물을 지불한 승객이기에 당연한 일이었다.

하지만 다음 순간 이어진 한마디에는, 여 표사도 당황한 기색을 감출 수 없었다.

“탐이 나네요. 제 얼굴에 가져다 붙이고 싶을 만큼.”

“……!”

“농담이에요. 농담.”

까르르 울려 퍼지는 웃음소리. 얼어붙은 여 표사를 향해, 남천마후가 웃음기 섞인 목소리로 말을 이었다.

“그래서, 운남(雲南)까지는 얼마나 남았나요?”

지금 이 순간, 남천마후는 즐거워 견딜 수 없었다. 머지않아 또 다른 장소에서 들려올 비명과 죽음에.

그리고 새로운 얼굴을 만났다는 기쁨에.
```

## Final English reading copy

```markdown
# Chapter 483

“Southern Heaven… Demon Empress?”

Honglan—or rather, the Southern Heaven Demon Empress, inhabiting the body of a young military officer—spoke in a lighthearted tone.

“It’s embarrassing to hear that sobriquet from someone else’s mouth.”

“Embarrassing my ass. You bastards are raising hell in every direction—east, west, south, and north. So is the eastern one the East Virgin Forever-Alone, and the northern one North Korea’s Kim?”

“You got them roughly right, despite the different sobriquets. You’re smarter than I expected.”

“…Damn it.”

Western Heaven Demon Lord and Southern Heaven Demon Empress.

Even Mimi-chan could tell that those sobriquets had been created with the four directions in mind.

The Western Heaven Demon Lord was already a monster I had barely managed to take down after several brushes with death. And there were at least three more like him?

But an even more important question remained.

I stared at the military officer’s vacant expression and opened my mouth.

“How did you do it?”

“Oh my. What could possibly have our Young Great Hero so curious?”

“You know what I’m talking about.”

A strange light suddenly flashed in the officer’s slack eyes.

The Southern Heaven Demon Empress, gazing at me through someone else’s eyes, casually tossed out a single sentence.

“You saw it, didn’t you?”

“……!”

“There’s no way you found it in only two days. So I suppose a spirit creature really is a spirit creature. Then again, a five-hundred-year-old imugi would certainly qualify as a mystical being.”

The Southern Heaven Demon Empress grasped everything in an instant and smoothly added,

“Then you must know that I won’t answer you.”

The fragments of memory still felt vivid. The traces of the Gate I had glimpsed through the dragon’s memories. The Water God Dragon becoming stained by the demonic qi that had flowed from it.

That was something that could not—and should not—have happened.

At least not here, in the Murim. It was an incomprehensible phenomenon that should never have appeared.

Yet the Southern Heaven Demon Empress and Dark Heaven had dragged the impossible into reality. It was enough to make me wish it were a lie.

“What the hell are you people after?”

“After?”

The next moment, a clear laugh flowed between the officer’s lips. It was filled with genuine amusement, not something she had forced.

After laughing aloud for a while, the Southern Heaven Demon Empress continued.

“Child. I am merely a lowly servant who acts according to orders. No one—not anyone—can presume to know that person’s will.”

That person.

Everyone present knew whom those two syllables referred to.

Jeok Cheongang muttered in a voice that seemed to boil like lava.

“Lord of Heaven.”

Crack.

With the sound of bones shifting, the officer’s head turned toward Jeok Cheongang like a creaking wooden puppet.

“I’ve heard that an old monster who went mad lives on Mount Jiuhua. Fire King Jeok Cheongang, you’re right. It is indeed that person. The greatest and noblest of all…”

“You’re talking about a fucking bastard who wouldn’t be worth the satisfaction of burning alive. How dare you wag that wicked tongue before this old man?”

A brief silence descended at Jeok Cheongang’s words, which carried cold flames.

Then the officer’s tightly closed lips slowly opened, and a low voice flowed out.

“You should choose your words more carefully if you want to hold on to your stubborn life a little longer.”

“My life?”

Jeok Cheongang snorted and asked me,

“You tell her. What happened to the people who came running to cut this old man’s lifeline?”

“They died. Every last one of them.”

“Then how about this old man adds a bitch instead of a bastard to his kill list? What do you think?”

There was no question about it. I gave him a vigorous thumbs-up.

“You’re a true feminist of this era.”

“Femibista? What’s that?”

“It means you’re a fair person. You beat the shit out of everyone equally, regardless of sex or age.”

“Is that some word young people use these days? Whatever the case, I like the meaning.”

Jeok Cheongang nodded with satisfaction, then glared at the Southern Heaven Demon Empress inhabiting the officer’s body.

“You heard that? This femibista intends to punish you and that Lord of Heaven fellow, or whatever his name is. So wash your neck and wait.”

*Uh. Should I stop him now before the Flame-Extinguishing Divine Fist turns into the Feminist Fist?*

Still, I felt much better. The confusion in my head had been neatly sorted out.

*Yeah, fuck it. We just need to beat the shit out of all of them.*

Wasn’t that the Fire Gate Clan’s motto, anyway? Smash, break, and burn anyone we decided was an enemy.

The Southern Heaven Demon Empress was never going to answer my questions. If that was the case, then all I had to do was keep moving forward and smash through whatever Dark Heaven did.

*I don’t have a choice anyway.*

Once you climbed onto the back of a tiger, there were only two paths left.

And rather than be thrown from its back, I would end this insane struggle even if I had to smash the tiger’s skull to do it.

No. I had to.

“Phew…”

I exhaled the breath I had been holding, then leaned close to the military officer. Looking through the soul-less eyes at some distant place, I spoke.

“When we meet again… you will die.”

The officer’s lips twitched.

“Yes. I, too, look forward to that day. And when it comes, no one here will survive.”

The head slowly turned. Its unfocused, milky eyes looked over everyone in the room one by one.

But no one avoided that chilling gaze. Mungyeong was no exception.

“You should stop this futile killing. Blades eventually turn back on the person wielding them.”

His tone and voice were polite, clearly conscious of the eyes around him. But hidden within them was a blade only a handful of people could detect.

That was the true nature of the greatest assassin in history—a supreme martial artist known as the Slaughter Saint, who had walked nothing but blood-soaked paths.

“…What an unusual child. Unusual enough to make me curious about this person called the Divine Physician.”

But the Southern Heaven Demon Empress, borrowing someone else’s body, did not seem to have grasped Mungyeong’s true identity.

She might have known his superficial identity as the Divine Physician’s Disciple, but the connection between the Slaughter Saint who had vanished forty years ago and a young medical apprentice was far too faint.

And before the Southern Heaven Demon Empress’s suspicions about Mungyeong could deepen, Jin Wikyung spoke in a heavy voice.

“I swear on the name of the Jin Family of Taiyuan that you will never lay so much as a fingertip on our youngest.”

“The Jin Family of Taiyuan. Can that paltry family and its feeble martial arts really protect that child?”

“Even a sewer rat will fight a tiger for the sake of its young. If you’re curious, come and see for yourself. I’ll have no choice but to show you.”

Even in the face of a bizarre phenomenon far beyond the bounds of common sense, Jin Wikyung did not lose his composure.

The moment he finished speaking, calm yet resolute, Gung Gibang scratched his matted hair.

“Great Hero Jin, it would hurt my feelings if you left our Sect out.”

“I forgot the Beggars’ Sect. Will you join us?”

“My Master used to say that a single dog-beating stick can only catch a neighborhood cur, but when a hundred of them gather, they can beat even a tiger to death. What do you think would happen if a hundred thousand Beggars’ Sect disciples gathered?”

The true strength of the Beggars’ Sect came from its overwhelming numbers.

Their forces were so vast that no one could object even if they were broadly called the hundred-thousand-strong Beggars’ Sect.

Gung Gibang, the Successor Beggar who stood one step short of reaching the summit of the Beggars’ Sect, flashed his yellow teeth in a grin.

“You were such a lovely young lady. It’s a shame to see you like this. But what can we do? Don’t resent me too much when I smash that pretty face of yours with my club.”

“Resent you?”

The corner of the officer’s mouth slowly rose.

Borrowing his mouth to form a grotesque smile that seemed to split the skin, the Southern Heaven Demon Empress addressed everyone.

“There’s no need to be so impatient. It won’t take much longer…”

Her voice faded like a campfire slowly dying out.

By then, dark red blood was already flowing from between the officer’s lips. Without hesitation, I seized his wrist and felt for his pulse.

Whoosh.

Internal energy surged from my dantian in an instant and flowed into his body, but the death that had already begun could not be reversed.

Things that had outlived their usefulness were discarded.

Perhaps that was the reason the Southern Heaven Demon Empress had kept the officer alive.

*A puppet whose body she could borrow for a while.*

Blood gushed from his mouth, then spilled in a stream.

It wasn’t only his mouth.

Dark red blood poured from his eyes, nose, ears—in other words, from the seven openings of the human body.

A death that could not be stopped by several jiazi of internal energy or even a Pressure-Point Strike loomed before the officer’s eyes.

“It’s too late.”

At that exact moment, Mungyeong’s voice rang in my ears.

Along with a flood of blood, one final sentence slipped from the officer’s slowly opening lips.

“Everything is according to that person’s will.”

Swish. Thud.

That was the end.

The officer’s head drooped as all his vitality was exhausted, and his breath stopped.

As silence descended with one man’s death, the presence approaching the estate stopped outside the door.

“Um… may I come in?”

The voice was familiar.

A young man cautiously poked his head through the slowly opening door and spoke.

“Benefactor, Great Hero Zhuge Pong is looking for you.”

“Not Zhuge Pong. Zhuge Feng.”

“Yes. Great Hero Zhuge Pong.”

“…I should just stop talking.”

I sighed and stood up.

I didn’t ask where Crouching Dragon Guest Zhuge Feng was now, where I needed to go, or why he was looking for me.

I was the one who had told them about *that place* in the first place.

“So, did you find it?”

“Yes.”

Cheongpung’s eyes lit up as he continued.

“It’s exactly the place you described, Benefactor.”

That place was the very location from the Water God Dragon’s memories.

Yeah. The damn Gate.

* * *

Honglan—or rather, the Southern Heaven Demon Empress—opened her closed eyes.

She lifted the silk curtain of the gently swaying four-horse carriage. Outside the lattice window was dense undergrowth, along with the Escort Bureau’s men sweating in the hot, humid weather of the southern regions.

“Hm.”

With her chin resting in her hand as she gazed out the window, the Southern Heaven Demon Empress looked like a painting all by herself.

Then, over the heads of the Escort Bureau men sneaking glances at her as if entranced, a thunderous shout rang out.

“Stop gawking and focus on the delivery! Unless you want to get yourselves killed by the Miao people we’ll meet in a few days!”

Despite the rough words, the speaker was a woman of dazzling beauty.

Beneath the bamboo hat pulled low to block the sunlight, her long, straight nose was sharp as a blade, and her lightly tanned skin was pleasing to the eye.

*A female escort? You don’t see that every day.*

It did not take long for the female escort, who had been loudly berating the rough men, to notice the Southern Heaven Demon Empress’s gaze.

She loosened the reins, drew alongside the carriage, and spoke toward the window.

“Is there a problem?”

“No problem. Thanks to your hard work, I’m traveling very comfortably.”

“Then why have you been looking at me like…?”

“Just because.”

“Pardon?”

The Southern Heaven Demon Empress smiled sweetly and added,

“Because you’re so young and pretty. That’s why I was looking.”

“Ah, thank you.”

The female escort, the Young Bureau Head of a small-to-medium Escort Bureau, was flustered but did her best to hide it.

The fact that the woman complimenting her was beautiful enough to make even other women fall for her was one thing. More importantly, she was a passenger who had paid a considerable sum, so the Young Bureau Head’s reaction was only natural.

But at the next words, she could no longer conceal her bewilderment.

“You’re making me want it. Enough to want to stick it onto my own face.”

“……!”

“I’m joking. Just joking.”

Her laughter rang out brightly. Facing the frozen female escort, the Southern Heaven Demon Empress continued in an amused voice.

“So, how much longer until we reach Yunnan?”

At that moment, the Southern Heaven Demon Empress was almost unable to contain her delight.

Delight at the screams and deaths that would soon be heard in another place.

And delight at having met a new face.
```

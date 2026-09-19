<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0491.txt",
      "sha256": "3ff82114f8f4d0cab9a2b9996e381b208819725e00d7a5fe5763740880508bb1",
      "bytes": 14039
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "f834935989b70118d09b6c7c435158a714c48f6145e6e5778ce3be46c0b7da23",
      "bytes": 4141
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "70a59ae47dfd30ce73b77fae576e363a8de3ebd2668af368027cc27475cd2cf7",
      "bytes": 156344
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "3ded9a33d12cea6c3088048a7209035e738913dfa8e441e656f70b6d7585e79d",
      "bytes": 1006
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "d2fb24b42eae9a9ad334840f44447198411b70cad70ca352f713540aa5c2ecc2",
      "bytes": 553
    },
    {
      "path": "characters/Gung Gibang.md",
      "sha256": "55ac69169f5a35829e5c0fe9ed68868db4308ba8650e7cf4fddb6c6855a53a33",
      "bytes": 686
    },
    {
      "path": "characters/Hyeongong.md",
      "sha256": "c4d5de1cc859fa5c154648cb13dac0c3fc1a9981e39779d125655231afe0d05e",
      "bytes": 735
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "b636a8ece071ea5e4007dbe20703c6b3b07b2957ed2da0fc3d9c8beee42924aa",
      "bytes": 1108
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "38a117053fcdce7a4b24f735a9d5713d9ef8042bdef3d12d0a95d07b4b3d89e8",
      "bytes": 1547
    },
    {
      "path": "characters/Mungyeong.md",
      "sha256": "04808e30f1684052d9d2b4041c098ecdd00ae086ed77ad801821d8ccbac8f6ba",
      "bytes": 885
    },
    {
      "path": "characters/Pill Physician.md",
      "sha256": "20959259defeab639c1f7472123d8858a87822292ea3712ca470c82390eb46fe",
      "bytes": 554
    },
    {
      "path": "characters/Zhuge Feng.md",
      "sha256": "9a959b4dc9af5190f1dd84835840d0fefb1c5ff67c234e577a4d8f62e85416c1",
      "bytes": 649
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "0d6cef49b0e30a240b8b7d8a8f091792176d3591c1c9e5c7e0fc265ebea7d898",
      "bytes": 152065
    }
  ],
  "estimated_tokens": 13094
}
-->

# Durable State Update — Chapter 491

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 491. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 491. Profile updates may replace only one
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
  "chapter": 491,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 491,
    "continuity_sources": [491],
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
    "The functionally crippled Gate continues leaking faint mana; its residual mana is mutating local life, and the Water God Dragon has absorbed all of that mana.",
    "Around one hundred Level 5 Mutated Minnows, locally called Blood Fish, have been captured in the Gate's entrance waterways; the remaining population is unknown, and the fish fight and kill one another.",
    "Taekyung suspects Dark Heaven's regeneration, teleportation, and Moving Formation are manifestations of Magic connected to the Gate.",
    "Taekyung told Jeok that he came from another world, that an evil force from it is linked to Dark Heaven, that the corrupted imugi was their work, and that a fully opened Gate could release monsters.",
    "Jeok trusts Taekyung more deeply than anyone else, despite interpreting Taekyung's attempted explanation of his origin as a drawn-out declaration that he wanted to die.",
    "Honglan corrupted the benevolent Dongting Lake imugi and used it to kill many people; the severely injured Dongting Fisherman may be connected to Dark Heaven and the earlier destruction inside the secret refuge.",
    "The Southern Heaven Demon Empress is traveling toward Yunnan and expects to cause further deaths.",
    "Jin Wikyung and Gung Gibang pledged the Jin Family of Taiyuan and the Beggars' Sect to Taekyung's defense.",
    "Jeok's innate qi is damaged and steadily diminishing despite the Thousand-Year Snow Ginseng and the Divine Physician's treatment.",
    "Mungyeong is the Slaughter Saint, a Returned to Youth Supreme Peak master and the greatest assassin in history; before becoming the Slaughter Saint, he was called Killing Ghost, and he saved countless people as the Divine Physician.",
    "Mungyeong has agreed to teach Taekyung his secret martial arts without forming a formal Master-Disciple relationship and has begun testing him through an unannounced poison trap.",
    "Jeok's current whereabouts are unknown after he apparently hid from Taekyung at the camp; Taekyung neutralized the first poison with the Myriad-Poison Ring and Scorching Yang Qi, but a second poison has just affected him."
  ],
  "continuity_sources": [
    490,
    489
  ],
  "open_questions": [
    "What lies beyond the exposed Gate, why has it lost most of its functions, and how far has its residual mana's mutation spread?",
    "What is the Lord of Heaven's identity, and how is he connected to the dangerous force Taekyung associates with his original world?",
    "Where is the Southern Heaven Demon Empress ultimately headed, and what does she intend to do in Yunnan?",
    "What is the Dongting Fisherman's exact role within Dark Heaven, and how was he connected to the earlier destruction inside the secret refuge?",
    "How will Taekyung survive Mungyeong's poison-based first test, and what secret martial arts will Mungyeong teach him?"
  ],
  "safe_through": 490,
  "temporary_decisions": [
    "Render 독문 무공 as secret martial arts, 사승 as Master-Disciple relationship, 살귀 as Killing Ghost, and 가짜 무림인 as Fake Murim Martial Artist; preserve 악 as Agh in the Quest interface.",
    "Render 기억의 파편 as Memory Fragment, 게이트 공략 as Gate Conquest, 텔레포트 as Teleport, 마법 as Magic, 혈어 as Blood Fish, and 변이된 송사리 as Mutated Minnow; render 강력한 마비산 as Potent Paralysis Powder, 강력한 미혼산 as Potent Soul-Bewitching Powder, 전신 마비 as Full-Body Paralysis, 독성 흡수 as Poison Absorption, and 해독 as Detoxification.",
    "Render 시산혈해 as sea of corpses and blood and retain Old Master for 노야 with the established rough, profane Taekyung-Jeok banter; render 해시 as hour of the Pig and 한 식경 as half an hour.",
    "Render 선천지기 as innate qi, 진원진기 as true-origin qi, and 천기 as heavenly patterns.",
    "Render 심마 as Heart Demon, 비급 as martial arts manual, 송문고검 as Pine-Pattern Ancient Sword, 반로환동 as Returned to Youth, 강강수월래 as Ganggangsullae, 생사부 as Book of Life and Death, and 기막 as qi curtain."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 청풍     | **Cheongpung**     |
| 살성     | **Slaughter Saint**           | —              |
| 무당파    | **Wudang**                       |
| 제갈세가   | **Zhuge Clan**                   |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 가주     | **Family Head**                              |
| 장문인    | **Sect Leader**                              |
| 제자     | **Disciple**                                 |
| 사제     | **Junior Brother**                           |
| 선배     | **Senior**                                   |
| 은인     | **Benefactor**                               |
| 시스템              | **System**                     |
| 레이드     | **raid**              |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 공자      | **Young Master**                                                |
| 도사      | **Daoist**                                                      |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 궁기방 | **Gung Gibang** | Beggars' Sect Successor Beggar and finalist. |
| 현공진인 | **Perfected Being Hyeongong** | Veteran Wudang Daoist master and the current Sect Leader's Junior Brother. |
| 문경 | **Mungyeong** | Young medical apprentice and newly introduced passenger. |
| 환의 | **Pill Physician** | Title of the current Family Head of the Seongsu Jang Family. |
| 제갈풍 | **Zhuge Feng** | Current Family Head of the Zhuge Clan. |
| 검강 | **Sword Force** | Higher manifestation than Sword Energy; Pung Yang's is explicitly imperfect because of insufficient enlightenment. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 은자 | **silver nyang** | Silver currency unit. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 중독 | **Poisoned** | System status abnormality caused by the poisons. |
| 송문고검 | **Pine-Pattern Ancient Sword** | Willow-Cloud Divine Dragon’s sword. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 장강 | **Yangtze** | The river controlled by the Yangtze River Channel League. |
| 의생 | **medical apprentice** | Mungyeong's occupation. |
| 살수 | **assassin** | Professional killer considered as a possible suspect. |
| 만독지환 | **Myriad-Poison Ring** | Quest title concerning a legendary treasure said to detoxify any poison. |
| 열화신룡 | **Blazing Flame Divine Dragon** | New sobriquet bestowed on Jin Taekyung. |
| 이무기 | **imugi** | Legendary serpent mentioned as the only comparable creature to a Thousand-Year Poison Horned Snake. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 동정채 | **Donghu Stronghold** | Stronghold where Mu Song's Uncle Hwang is based. |
| 동정호 | **Dongting Lake** | Lake under which Dangyang and Honghu Strongholds operated. |
| 쾌조선 | **swift ship** | Fast vessel operated by the Yangtze River Channel League. |
| 수신룡 | **Water God Dragon** | Legendary name for the true master of Dongting Lake; distinct from the modern Sea Serpent. |
| 제갈 | **Zhuge** | Surname used for Sir Zhuge. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 청풍 | 혁무진 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung includes Mujin among his 은인들 after receiving the skewers. |
| 혁무진 | 청풍 | martial artist to young master | Young Master | formal-deferential | Mujin uses 공자께서는 when asking why Cheongpung descended from the mountain. |
| 적천강 | 청풍 | overwhelming_elder_to_young_martial_artist | you / little punk | blunt, amused, and threatening | Jeok Cheongang uses 네, 이놈, and related blunt forms while testing Cheongpung. |
| 청풍 | 적천강 | young_martial_artist_to_overwhelming_elder | Grandpa Jeok | casual-familiar despite deference | Cheongpung uses 적 할아버지 while asking Jeok Cheongang to confirm Taekyung's condition; this is a familial form of address, not literal kinship. |
| 혁무진 | 적천강 | subordinate_to_overwhelming_elder | Great Hero Jeok | deferential and fearful | Mujin uses 적 대협 while reporting Jeok’s orders and Taekyung’s awakening. |
| 적천강 | 혁무진 | overwhelming_elder_to_junior_martial_artist | you stupid fool | blunt and mocking | Jeok calls Mujin a 멍청한 놈 after knocking him down during the attempted escape. |
| 청풍 | 문경 | martial_companion_to_medical_apprentice | Medical Apprentice | cheerful-polite | Cheongpung addresses Mungyeong as 의생님 while asking him to greet the Tang Clan. |
| 혁무진 | 궁기방 | squad_companion_to_Beggars_Sect_successor | Young Hero Gung | formal-polite, then pointed | Uses 궁 소협 while asking about the culprit and challenging Gung’s insults. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 문경 | 적천강 | old_acquaintances | Fire King | familiar and grave | The figure bearing Mungyeong’s name greets Jeok Cheongang by his established epithet. |
| 궁기방 | 혁무진 | squad_companions | you; that lunatic | insulting-casual | Gung Gibang mocks Hyuk Mujin's injuries and calls him a lunatic for attacking the Third Fiend. |
| 궁기방 | 청풍 | martial_companions | Young Hero Cheongpung | formal-polite | Gung Gibang uses 청 소협 while asking why Cheongpung is at the temporary clinic. |
| 적천강 | 문경 | overwhelming elder to old acquaintance | you / little punk | mocking and threatening | Mocks Mungyeong's expression and threatens to poke out his eyes. |
| 적천강 | 제갈풍 | senior_martial_artist_to_old_acquaintance | you / ill-mannered brat | blunt, familiar, and teasing | Jeok treats Zhuge Feng as the younger acquaintance he remembers from childhood. |
| 제갈풍 | 적천강 | younger_old_acquaintance_to_legendary_senior | Senior | respectful but relaxed | Zhuge Feng recalls Jeok's earlier visit and addresses him as an old senior. |
| 제갈풍 | 궁기방 | family_head_to_beggars_sect_successor | Successor Beggar | calm and conversational | Uses 후개 when confirming Gung Gibang's guess about the broken weapon. |
| 현공진인 | 제갈풍 | senior Wudang master to Zhuge Clan Family Head | Family Head Zhuge | formal-respectful | Uses 제갈가주 while discussing the fast ship and the route. |
| 제갈풍 | 현공진인 | Zhuge Clan Family Head to senior Wudang master | Perfected Being Hyeongong | formal-deferential | Addresses Hyeongong with marked respect and calls his presence a great reinforcement. |
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

- **Safe through:** Chapter 487
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, the grandson and Disciple of Sword Saint Mae Jonghak, and a Supreme Peak martial master known as the Huashan Divine Dragon.
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, a deep love of martial arts, competitive pride, unusual resistance to monster-induced Fear, and discomfort when someone copies his martial arts.
- **Voice:** Dreamy and hazy, with innocent, polite phrasing; he has begun imitating Taekyung's profanity.
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions while Taekyung is his only true martial rival; Tang Sadok has temporarily entrusted Mimi to him.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 490
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Gung Gibang.md

# Gung Gibang (궁기방)

- **Safe through:** Chapter 490
- **Aliases:** Successor Beggar, Beggar Prince, pure-blooded beggar, ultimate beggar
- **Role:** Gung Gibang is the Beggars' Sect Successor Beggar and a unique eight-knot disciple.
- **Personality:** Vulgar, aggressive, and quick-tempered.
- **Voice:** Blunt, profane, and vividly threatening.
- **Relationships:** Gung Gibang is a rival finalist alongside Baek Woo and Zhuge Gyun who trades insults with Taekyung, uses Beggars’ Sect intelligence to investigate Tang Taesang’s murder and Dark Heaven’s Hubei forces, and has now found a trace of Honglan.

### Hyeongong.md

# Perfected Being Hyeongong (현공진인)

- **Safe through:** Chapter 484
- **Aliases:** None
- **Role:** Perfected Being Hyeongong is a veteran Wudang Daoist master of the previous generation, the current Sect Leader's Junior Brother, and a Supreme Peak swordsman who reached the ultimate stage of the Taiji Wisdom Sword.
- **Personality:** Hyeongong is humble and self-deprecating about his limited worldly knowledge while carrying the authority of an experienced senior master.
- **Voice:** Measured, respectful, and lightly self-deprecating.
- **Relationships:** Hyeongong is the current Wudang Sect Leader's Junior Brother and a respected senior to Zhuge Feng.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 488
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers and Vice Squad Leader of the Jin Dragon Squad.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 490
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin and Furnace Fire Pure Blue, and Jin Taekyung's Master.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Mungyeong.md

# Mungyeong (문경)

- **Safe through:** Chapter 490
- **Aliases:** Killing Ghost
- **Role:** Mungyeong is the legendary physician known as the former Divine Physician and Slaughter Saint, a Returned to Youth Supreme Peak master and the greatest assassin in history who passed the Divine Physician title to his Disciple.
- **Personality:** Compassionate, resolute, resourceful, and calm under extreme pressure.
- **Voice:** His Mungyeong persona is timid, deferential, and cheerful, while his Slaughter Saint voice is dry, impassive, and blunt.
- **Relationships:** Dong Feng is his Disciple, Jeok Cheongang is an old acquaintance who asked him to look after and instruct Jin Taekyung, and Mungyeong is currently testing Taekyung before teaching him secret martial arts without a formal Master-Disciple relationship.

### Pill Physician.md

# Pill Physician (환의)

- **Safe through:** Chapter 486
- **Aliases:** None
- **Role:** Current Family Head of the Seongsu Jang Family in Shandong, who personally placed and signed the Thousand-Year Snow Ginseng in the casket entrusted to the Yongbong Escort Bureau.
- **Personality:** No personality traits are established.
- **Voice:** No voice traits are established.
- **Relationships:** The Pill Physician heads the Seongsu Jang Family, a prestigious medical family in Shandong.

### Zhuge Feng.md

# Zhuge Feng (제갈풍)

- **Safe through:** Chapter 487
- **Aliases:** Crouching Dragon Guest
- **Role:** Zhuge Feng is the current Family Head of the Zhuge Clan and father of its Lesser Family Head, Zhuge Gyun.
- **Personality:** Analytical, disarmingly casual, eccentric, and inventive; he treats comfort and time as principles while delivering grave intelligence with unsettling directness.
- **Voice:** Clear, calm, polished, and conversational, with understated humor and pointed questioning.
- **Relationships:** Zhuge Gyun is his son, and Zhuge Gonghu was his grandfather.

## Korean source

```text
＃491화



“어, 조장님. 안 주무셨……?”

어스름한 새벽, 내가 머무르는 임시 막사로 들어온 혁무진이 귀신이라도 본 듯한 표정으로 입을 다물었다.

“왜.”

“어, 그게…….”

“말해.”

“아닙니다. 그냥 오늘따라 왠지 피곤해 보이셔서요.”

“……후.”

피곤이라, 피곤. 이걸 고작 피곤하다고 해야 하나.

나는 세숫물이 담긴 청동 그릇을 노려봤다. 헝클어진 머리카락과 충혈된 눈동자. 고개를 들어 주위를 둘러보니 온통 난장판이다.

뒤늦게 그 사실을 알아챈 혁무진의 눈동자에도 동공 지진이 일어났다.

“이게 무슨, 도대체 무슨 일이 있었던 겁니까?”

“어. 무슨 일이 있긴 했지.”

입술 사이로 흘러나오는 목소리가 남의 것처럼 낯설다. 나는 푸석푸석한 얼굴을 쓸어내리며 중얼거렸다.

“개 같은 살수 새끼…….”

작은 중얼거림이었지만 아주 안 들릴 정도는 아니다. 살수라는 단어에 혁무진이 화들짝 놀랐다.

“예? 살수요?”

“뭐.”

“아니, 방금 분명히 살수라고 하셨잖습니까.”

“잘못 들었어.”

“똑똑히 들었는데요? 제 귀로.”

“아니라니까.”

물론 사실이 맞다.

웬 악독한 살수 새끼가 막사 내부에 십여 개의 암기를 설치했고, 나는 하나도 빠짐없이 걸려드는 100퍼센트의 성공 확률을 보여 주며 걸레짝이 됐다.

하지만 누구에게도 그 사실을 말할 수 없다는 게 통탄할 노릇이다.

“조, 조장님…….”

“아, 잘못 들은 거라니까!”

“그게 아니라요. 엉덩이에서 피나요.”

“……!”

시벌. 어쩐지 아까부터 엉덩이가 따뜻하더라.

내심 쌍욕을 퍼부으며 엉덩이의 상처를 지혈하는 내 모습에, 혁무진이 떨떠름한 표정을 지었다.

“아무래도 살수 맞는 것 같은데요.”

“수련하느라 다친 거야.”

“정말요?”

나는 힘없이 고개를 끄덕였다.

이것도 수련은 수련이다. 밤새 한숨도 못 자고 해독만 하는 게 어느 나라의 무슨 수련 법인지는 모르겠지만, 아무튼 그렇다.

“진짜 수련이야. 네 불알 두 쪽 걸고 맹세한다.”

“누차 말씀드리는 거지만 제 불알은 걸지 마시고요. 혹시 지금도 살수에게 협박당하고 계신 거라면 눈을 두 번 깜빡이십시오.”

“……무진아. 그런 거 시키려면 최소한 전음으로 물어봐야 하는 거 아니냐?”

“저 아직 전음 못 쓰는데요.”

“그럼 필담(筆談)으로 하면 되잖아.”

“어, 그러네요.”

“미친놈인가.”

하긴, 상대가 혁무진인데 뭘 더 바라냐.

한숨을 푹 내쉰 나는 녀석을 위아래로 훑었다. 이른 새벽에 깔끔하게 무복까지 갖춰 입고 찾아온 걸 보니 용무가 있는 게 확실하다.

“그런데 무슨 일이야?”

“아, 제갈 대협께서 찾으십니다. 지금 다들 모여 있어요.”

“다들? 왜?”

“그, 아시잖습니까.”

괜히 주위를 살핀 혁무진이 입을 뻐끔거렸다. 이내 오직 나만 들을 수 있을 만큼 숨죽인 목소리가 들려왔다.

“이무기요. 죽은 이무기.”

“아.”

“극소수만 은밀히 가기로 했습니다. 무당파의 현공진인(玄空眞人)께서도 기다리고 계세요.”

“현공진인까지? 아, 당연히 그럴 만도 하지.”

현공진인은 이번 사건에 참여한 초절정 고수 중 유일하게 동정채에 남아 있던 사람이다.

게다가 무당파 장문인의 사제이자 무림의 원로이기까지 하니, 무당파의 대표로 참석할 자격이라면 차고 넘친다.

아무리 수신룡의 존재가 극비라고는 해도 무당파에까지 비밀로 할 수는 없는 법이니까.

‘그런데 이 정도 사안이라면 장문인이 올 법도 한데, 왜 굳이 현공진인을?’

문득 그런 의문이 들었지만, 이내 떠오른 한 사람에 관한 생각으로 씻은 듯이 지워져 버렸다.

“야, 혹시 같이 가는 사람 중에…….”

설마 하는 마음으로 말을 이으려던 그때, 막사 밖에서 조용한 목소리가 들려왔다.

“진 공자님. 모두들 기다리고 계십니다.”

“……!”

“준비 끝나셨으면 어서 나오시지요.”

말이 끝나기가 무섭게 멀어지는 기척, 돌처럼 굳어 버린 나를 본 혁무진이 고개를 갸웃거렸다.

“왜 그러세요?”

“……쟤는, 쟤는 왜 같이 가?”

“누구, 아. 문경이요? 아무래도 신의의 제자씩이나 되는 녀석이니 이무기의 신체 구조나 그런 부분에서 많은 도움이 될 것 같아서…… 그런데 왜 그러세요?”

왜 그러긴. 저 미친놈이 무슨 짓을 할지 몰라서 그렇지.

나는 목구멍까지 차오른 말을 꿀꺽 삼키고 걸음을 옮겼다. 아니, 옮기려다가 멈칫한 뒤 혁무진을 향해 고개를 돌렸다.

“무진아.”

“예?”

“앞장서라. 난 네 뒤만 따라갈게.”

“예에?”

시스템 알림 소리가 귓가에 울리는 듯한 기분이다.

띠링. [고기 방패]를 획득하셨습니다!



* * *



준비되어 있던 작은 선박에 올라타자 익숙한 면면들이 보인다.

누덕누덕 기운 도포에 낡은 송문고검(松紋古劍)을 허리에 찬 현공진인이 부드럽게 웃으며 인사를 건넸다.

“젊은 도우가 오셨군. 다시 만나게 되어 반갑네.”

“현공진인을 뵙습니다.”

이제는 제법 무림인답게 포권을 취하자, 옆에 있던 제갈풍이 쥘부채를 흔들며 끼어들었다.

“그런데 자네 표정이…….”

“아무 일도 없었습니다.”

“그런 것치고는 영 좋지 않아 보이는데. 그렇지 않습니까. 진인?”

“제갈 가주의 말에 동의하오. 꼭 밤새 살수에게 시달린 듯한 얼굴이구려.”

“살수라니, 진인께서는 농담도 잘하십니다. 하하.”

“허허허.”

“…….”

웃지 마. 이빨도 보이지 마.

만독지환이 없었으면 지금쯤 제대로 서 있기나 했을지 의문이다.

얼마나 독에 절여졌으면 별호를 열화신룡이 아니라 독 장아찌, 뭐 그런 것으로 바꿔야 하나 고민했을 정도다.

‘이 와중에 뻔뻔하게 앉아 있는 것 보소.’

나는 어느새 쾌조선의 한 자리를 차지한 문경을 지그시 노려보았다.

찌를 듯한 눈빛을 알아챈 소년의 고개가 스르륵 돌아간다.

- 눈 깔아라.

“…….”

깔라면 깔아야지.

슬그머니 시선을 돌리자 문경이 흘려보낸 전음이 연이어 들려왔다.

- 꼴을 보아하니 첫날부터 죄다 걸려든 모양이군. 한심하긴, 만독지환과 열양지기가 아니었다면 네놈은 간밤에 이미 죽고도 남았다.

- ……죽었을지 살았을지, 그걸 어떻게 압니까?

- 알려 줄까?

- 제가 실언을 했네요.

이게 영 틀린 말은 아닌 것이, 문경이 설치해 놓은 암기에는 하나같이 강력한 독이 발라져 있었다.

언젠가 의술과 독은 일맥상통한다는 말을 들은 적이 있는데 누가 한 말인지는 몰라도 백번 옳다. 무슨 수를 썼는지 당하는 독마다 ‘강력한’이라는 미사여구가 꼭 붙어 있더라.

그나마 만독지환의 사기적인 성능과, 독에 상극이라 할 수 있는 열양지기를 익혔기에 자상(刺傷) 몇 군데 입은 정도로 끝날 수 있었던 거다.

만약 그 두 가지가 없었다면…… 생각만으로도 간담이 서늘해진다.

‘의생 같은 소리하고 있네. 저게 신의냐, 독의지.’

- 방금 내 욕 한 거 다 안다.

“흡.”

나도 모르게 헛숨을 삼키자, 마음씨 좋은 현공진인이 걱정스러운 얼굴로 나를 바라보았다.

“왜 그러나, 진 도우?”

“아, 아닙니다. 그냥 습관이에요.”

“그렇다면 다행이군. 빈도는 또 정말 살수에게 겁박이라도 당하는 줄 알고 놀랐지 뭔가. 안 그렇소, 제갈 가주?”

“으허허! 제 배꼽 빠집니다, 진인!”

“허허허.”

“…….”

확 그냥, 배꼽을 쥐어 뜯어 버릴라.

내가 제갈풍의 배꼽을 노려보고 있는 사이, 손님들을 태운 선박은 잔잔한 물살을 가르며 부드럽게 나아갔다.

너무나도 당연한 출발에 한 박자 늦게 그 사실을 알아차린 내가 다급히 입을 열었다.

“잠깐만요. 노, 아니 스승님께서 안 오셨는데요.”

갑작스러운 이의 제기에 제갈풍의 얼굴 위로 물음표가 떠올랐다.

“응? 듣지 못했나?”

“네? 뭘요?”

“적 노 선배께서는 불참하시기로 했네. 뿐만 아니라 모든 일이 마무리되기 전까지는 당분간 찾지 말라고 하시더군.”

“……그렇습니까?”

“몰랐나? 어쩐지, 제자를 통해서 말씀하시지 않더라니.”

나로서는 처음 듣는 이야기다.

그리고 그 이유가 뭐건 간에 내게 직접 말 한마디 해 주지 않았다는 사실이 조금은 섭섭하고, 지금 그가 어떤 심정인지 알 것 같기도 했다.

‘착잡하시겠지.’

제자를 키워 본 적은 없지만, 훗날 같은 상황에 처한다면 나 역시 비슷할 거라는 생각이 든다.

사랑과 정성으로 보살핀 가족 같은 반려동물을 다른 사람에게 맡기는 기분이 아닐까.

“…….”

아니, 정정한다. 그렇게 되면 내가 적천강의 애완견이나 마찬가지잖아.

‘자식. 그래, 자식이라고 하자.’

스스로 합의점을 찾고 있던 그때, 해맑은 표정으로 다가온 청풍이 손에 든 것을 불쑥 내밀었다.

“뭐야, 이건.”

“당과예요, 은인.”

“……당과인 건 아는데, 이런 건 도대체 어디서 끊임없이 솟아 나오는 거야?”

둘 중 하나가 틀림없다.

청풍이 시스템 이용자여서 인벤토리에 당과 10톤을 쌓아 놨거나, 근처에 당과가 열리는 나무가 있거나.

“어쨌든 잘 먹을게.”

평소였다면 거들떠보지도 않았겠지만, 머릿속이 복잡한 지금 당과는 훌륭한 당분 보충 수단이다.

나는 건네받은 당과를 깨물며 청풍에게 물었다.

“그런데 이 와중에 당과를 구해 오다니, 재주도 좋네. 아, 지난번에 제갈세가로 왔을 때 사 둔 거야?”

“아뇨. 그건 벌써 다 먹었는데요.”

“음? 그럼 이건?”

“살, 아니 문경이 줬어요. 이건 특별히 은인께 드리래요. 참 좋은 사람이에요!”

“……누구?”

대답은 다른 곳에서 들려왔다.

삐빅.



- [강력한 산공독]에 중독되었습니다!

- [산공독]은 일시적으로 공력을 사용하지 못하게 만드는 효능을 지니고 있습니다.

- [공력]이 서서히 흩어지고 있습니다! 빠른 조치가 필요합니다!



“…….”

시벌, 어쩐지 당과가 유난히 달더라.

나는 조용히 만독지환을 꺼냈다.



* * *



사람은 죽어서 이름을 남기고, 짐승은 죽어서 가죽을 남긴다고 했다.

그리고 이는 장장 오백 년간 동정호와 장강을 지배했던 신령스러운 존재에게도 적용되는 말이었다.

비록 수신룡의 넋은 이미 육신을 떠났지만, 그의 육신은 마지막으로 몸을 뉘었던 그 자리에 남아 있었다. 생전의 위용과 아름다움을 고스란히 간직한 채.

“……허어.”

깊은 현기와 깨달음을 지닌 노도사, 현공진인조차 할 말을 잃고 외마디 탄성을 토해 냈다.

그만큼 수신룡의 육신이 주는 위압감은 대단한 것이었다.

이미 수신룡을 목격한 바 있는 궁기방조차 입을 쩍 벌린 채 감탄사를 연발했다.

“다시 봐도 어마어마하군. 그렇지 않나?”

나는 정중한 목소리로 대답했다.

“어마어마하지. 네 입 냄새도 그렇고. 그런 의미에서 부탁하는 건데 꺼져 주면 안 될까. 산공독보다 더 센 것 같아.”

“음. 어렵지 않은 일이군. 단, 조건이 있다.”

“뭔데.”

“어제 주기로 했던 은자 열 냥 중에 다섯 냥을 아직 못 받았다. 네놈이 막 나가는 건 알고 있었지만, 하다 하다 거지 등쳐 먹는 놈일 줄이야.”

“줄 테니까 말 좀 짧게 해라. 눈앞에 막 환상이 보이려고 하네.”

저게 입인지, 하수구인지 도무지 분간이 가지 않을 지경이다.

기어코 은자 다섯 냥을 추가로 받아 낸 궁기방이 툴툴거렸다.

“엄살은. 그리고 환상이라면 나도 지긋지긋하게 봤다. 근 며칠 동안 이상한 꿈도 꿨어.”

“꿈?”

“그래. 꿈.”

궁기방이 피식 웃으며 문경을 가리켰다.

“꿈속에서 문경이 저 이무기와 싸우더군. 검강도 슁슁 날리고, 유령처럼 휙 사라졌다가 나타나길 반복하는데…… 그 모습이 고금제일의 살수인 살성이라고 해도 믿겠더군.”

“…….”

걔 살성 맞아.

나는 계속해서 떠드는 궁기방을 애써 무시한 채 수신룡의 사체를 바라보았다.

머리부터 꼬리까지. 장장 백여 장에 이르는 거대한 육신.

한때 검게 물들었던 비늘은 눈부신 은빛을 흩뿌리고 있고, 몸뚱어리 곳곳에는 수많은 상처가 아로새겨져 있었다.

나는 쩍 벌어진 상흔을 쓰다듬으며 내심 중얼거렸다.

‘미안합니다.’

물론 알고 있다. 수신룡과의 전투는 불가피한 것이었고, 미안해할 필요도 없다는 것을.

오히려 그는 이렇게라도 자신을 멈춰 준 우리에게 고마워했다.

다만 내가 이렇게 사과하는 이유는, 그의 육신을 이대로 묻어 주지 못하기 때문이다.

‘사체.’

레이드가 끝났으니, 사체를 처리해야 할 시간이다.
```

## Final English reading copy

```markdown
# Chapter 491

“Hey, Captain. You haven’t slept—?”

Hyuk Mujin entered the temporary tent where I was staying at the dim hour before dawn, then clamped his mouth shut with an expression as if he had seen a ghost.

“Why?”

“Uh, well…”

“Say it.”

“No, sir. You just look unusually tired today.”

“…Hoo.”

Tired? Tired. Was that all I could call this?

I glared at the bronze basin filled with wash water. My hair was a mess, and my eyes were bloodshot. When I lifted my head and looked around, the entire tent was a disaster.

Hyuk Mujin belatedly noticed the same thing, and his pupils began quaking.

“What in the world… What on earth happened here?”

“Yeah. Something did happen.”

The voice coming from between my lips sounded unfamiliar, as if it belonged to someone else. I rubbed my haggard face and muttered,

“That fucking assassin bastard…”

It was a quiet mutter, but not quiet enough to be completely inaudible. The word *assassin* made Hyuk Mujin jump.

“Pardon? An assassin?”

“What?”

“No, you definitely just said ‘assassin.’”

“You heard wrong.”

“I heard it perfectly. With my own ears.”

“I said you didn’t.”

Of course, it was true.

Some vicious assassin bastard had installed a dozen or so hidden weapons inside the tent, and I had managed to trigger every single one of them. With a one-hundred-percent success rate, I had been reduced to a bloody rag.

The maddening part was that I couldn’t tell anyone about it.

“C-Captain…”

“Ah, I said you heard wrong!”

“That’s not it. You’re bleeding from your butt.”

“……!”

Fuck. No wonder my ass had felt warm for a while.

As I silently cursed and staunched the wound, Hyuk Mujin gave me an unimpressed look.

“I think it really was an assassin.”

“I was injured during training.”

“Really?”

I weakly nodded.

It was training. I had no idea what country’s training method involved staying awake all night and doing nothing but detoxifying poison, but it was training all the same.

“It really was training. I swear on both your balls.”

“As I’ve told you repeatedly, please don’t swear on my balls. And if an assassin is threatening you right now, blink twice.”

“…Mujin. If you’re going to make me do something like that, shouldn’t you at least ask through Sound Transmission?”

“I still can’t use Sound Transmission.”

“Then you could use written communication.”

“Oh, right.”

“Are you insane?”

Well, what more could I expect from Hyuk Mujin?

I let out a long sigh and looked him up and down. He had even dressed neatly in his martial artist’s uniform this early in the morning, so he clearly had business with me.

“Anyway, what’s going on?”

“Ah, Sir Zhuge is looking for you. Everyone is gathered right now.”

“Everyone? Why?”

“You know.”

Hyuk Mujin glanced around unnecessarily, then opened and closed his mouth a few times. Soon, his voice came in a whisper quiet enough for only me to hear.

“The imugi. The dead imugi.”

“Ah.”

“Only a very small number of people will be going in secret. Perfected Being Hyeongong of the Wudang Sect is waiting as well.”

“Even Perfected Being Hyeongong? Ah, of course he would be.”

Perfected Being Hyeongong was the only Supreme Peak master involved in this incident who had remained in Donghu Stronghold.

On top of that, he was the Wudang Sect Leader’s Junior Brother and a senior figure in the Murim. He had more than enough qualifications to attend as Wudang’s representative.

No matter how strictly confidential the Water God Dragon’s existence was, it wasn’t something we could keep secret from even the Wudang Sect.

*But if this matter is important enough, the Sect Leader himself could have come. Why send Perfected Being Hyeongong?*

The question occurred to me, but it vanished as soon as I thought of one particular person.

“Hey, is anyone going with us—”

I was about to continue, half hoping I was wrong, when a quiet voice came from outside the tent.

“Young Master Jin. Everyone is waiting.”

“……!”

“If you’re ready, please come out.”

The presence outside began moving away as soon as the words ended. Hyuk Mujin tilted his head when he saw me standing rigidly.

“Why are you doing that?”

“Why is he going with us?”

“Who? Oh, Mungyeong? Since he’s actually a disciple of the Divine Physician, he should be able to help a great deal with the imugi’s physical structure and such. But why?”

Why? Because I had no idea what that lunatic might do.

I swallowed the words rising to my throat and started walking. Then I stopped, turned around, and looked at Hyuk Mujin.

“Mujin.”

“Yes?”

“Go first. I’ll follow right behind you.”

“Pardon?”

It felt as if I could hear the System notification ringing in my ears.

*Ding.*



> **System**
>
> - You have acquired **Meat Shield**!

* * *

When I climbed aboard the small vessel prepared for us, I saw several familiar faces.

Perfected Being Hyeongong, dressed in a heavily patched robe with an old Pine-Pattern Ancient Sword at his waist, greeted me with a gentle smile.

“A young fellow Daoist has arrived. It is good to see you again.”

“Greetings, Perfected Being Hyeongong.”

I now made a fairly convincing martial artist’s fist-and-palm salute. Zhuge Feng, sitting beside him, waved his folded fan and cut in.

“But your expression…”

“Nothing happened.”

“You don’t look particularly well for someone to whom nothing happened. Don’t you agree, Perfected Being?”

“I agree with Family Head Zhuge. You look exactly as if you had been tormented by an assassin all night.”

“An assassin? Perfected Being, you do make jokes. Ha ha.”

“Ho ho ho.”

“……”

Don’t laugh. And don’t show me your teeth.

Without the Myriad-Poison Ring, I doubted I would have been able to stand upright by now.

I had been soaked in so much poison that I had seriously considered whether I should change my sobriquet from the Blazing Flame Divine Dragon to something like Poisoned Pickle.

*Look at him, sitting there shamelessly.*

I glared at Mungyeong, who had already claimed a seat on the swift ship.

The boy noticed my piercing gaze and slowly turned his head.

—Lower your eyes.

“……”

If he told me to lower them, I had no choice.

I stealthily turned my gaze away, and Mungyeong’s Sound Transmission continued.

—Judging by your condition, you must have fallen for every trap from the first day. How pathetic. If you hadn’t had the Myriad-Poison Ring and Scorching Yang Qi, you would have been dead by now.

—…How do you know whether I would have died or survived?

—Want me to tell you?

—I misspoke.

He wasn’t entirely wrong. Every hidden weapon Mungyeong had installed was coated with potent poison.

I had once heard that medicine and poison shared the same source. I didn’t know who had said it, but they had been completely right. Somehow, every poison I suffered came with the adjective *potent* attached to it.

Thanks to the Myriad-Poison Ring’s absurd performance and the Scorching Yang Qi I had learned, which was practically the natural opposite of poison, I had gotten away with only a few stab wounds.

If I hadn’t possessed those two things… Just thinking about it made my blood run cold.

*Medical apprentice, my ass. That’s no Divine Physician. He’s a Poison Physician.*

—I know you just insulted me.

“Ghk.”

I accidentally sucked in a startled breath. The kind-hearted Perfected Being Hyeongong looked at me with concern.

“Is something wrong, young friend?”

“Ah, no. It’s just a habit.”

“If so, that is a relief. I was startled, thinking you were actually being threatened by an assassin. Am I wrong, Family Head Zhuge?”

“Ha ha ha! I’m going to split my sides, Perfected Being!”

“Ho ho ho.”

“……”

I should just rip Zhuge Feng’s navel out.

While I glared at his stomach, the vessel carrying its passengers cut smoothly through the calm water.

It was such an obvious departure that I realized it a moment too late and hurriedly opened my mouth.

“Wait. The Old Master—no, my Master isn’t here.”

A question mark seemed to appear over Zhuge Feng’s face at my sudden objection.

“Hm? Didn’t you hear?”

“Hear what?”

“Senior Jeok decided not to attend. He also asked everyone not to look for him for the time being, until everything is finished.”

“…Is that so?”

“You didn’t know? That explains why he didn’t pass the message along through his Disciple.”

This was the first I had heard of it.

Whatever his reason, the fact that he hadn’t told me himself left me a little disappointed. At the same time, I thought I could understand how he felt.

*He must be troubled.*

I had never raised a Disciple, but if I found myself in the same situation someday, I felt I would react similarly.

Wasn’t it like entrusting a beloved pet—one cared for with love and devotion, almost like family—to someone else?

“……”

No, I take that back. If that were the case, I’d basically be Jeok Cheongang’s pet dog.

*His son. Right, let’s call it his son.*

I was still trying to reach that compromise with myself when Cheongpung approached with a bright expression and abruptly held something out to me.

“What’s this?”

“It’s candy, Benefactor.”

“……I know it’s candy, but where does this stuff keep coming from?”

There were only two possibilities.

Either Cheongpung was a System user with ten tons of candy stored in his inventory, or there was a tree nearby that grew candy.

“Either way, thanks.”

I normally wouldn’t have looked twice at it, but with my mind so complicated, candy was an excellent source of sugar.

I bit into the candy he had given me and asked,

“You’re pretty talented to have found candy at a time like this. Ah, did you buy it when you came to the Zhuge Clan last time?”

“No. I already ate all of that.”

“Hm? Then where did this come from?”

“Slaugh—no, Mungyeong gave it to me. He told me to give this one specially to you, Benefactor. He’s a really good person!”

“…Who?”

The answer came from somewhere else.

*Beep.*



> **System**
>
> - You have been poisoned by **Potent Energy-Dispersing Poison**!
>
> - **Energy-Dispersing Poison** temporarily prevents the use of internal energy.
>
> - Your **internal energy** is slowly dissipating! Immediate action is required!



“……”

Fuck. No wonder the candy had tasted unusually sweet.

I quietly took out the Myriad-Poison Ring.

* * *

They say that people leave their names behind when they die, while beasts leave their hides.

The same was true of the spirit creature that had ruled Dongting Lake and the Yangtze for five hundred years.

Although the Water God Dragon’s spirit had already left its body, its body remained where it had last lain down, retaining all the majesty and beauty it had possessed in life.

“…Hoo.”

Even Perfected Being Hyeongong, an old Daoist with profound insight and enlightenment, was speechless. Only a single exclamation escaped his lips.

That was how overwhelming the Water God Dragon’s body was.

Even Gung Gibang, who had already seen the Water God Dragon once, stood with his mouth hanging open, repeatedly exclaiming in awe.

“It’s incredible even the second time around. Don’t you think?”

I answered in a perfectly polite voice.

“It is incredible. So is your breath. Could you get lost? It seems even stronger than the Energy-Dispersing Poison.”

“Hm. That shouldn’t be difficult. However, I have a condition.”

“What?”

“Of the ten silver nyang you promised me yesterday, I still haven’t received five. I knew you were shameless, but I never thought you’d go so far as to prey on a beggar.”

“I’ll pay you, so keep it short. I’m starting to see things in front of me.”

At this point, it was impossible to tell whether his mouth was a mouth or a sewer.

After finally extracting another five silver nyang from me, Gung Gibang grumbled,

“Stop exaggerating. And if you mean hallucinations, I’ve had more than enough of those myself. I’ve been having strange dreams for the past few days.”

“Dreams?”

“Yes. Dreams.”

Gung Gibang gave a quiet laugh and pointed at Mungyeong.

“In the dream, Mungyeong was fighting that imugi. He was sending Sword Force flying through the air and disappearing and reappearing like a ghost. If someone told me he was the Slaughter Saint, the greatest assassin in history, I would have believed them.”

“……”

*He is the Slaughter Saint.*

I continued staring at the Water God Dragon’s body, doing my best to ignore Gung Gibang’s endless chatter.

From head to tail, its enormous body stretched for more than a hundred zhang.[^1]

Its scales, once stained black, now scattered dazzling silver light, while countless wounds were carved across its body.

I stroked one of the gaping scars and apologized silently.

*I’m sorry.*

Of course, I knew. The battle with the Water God Dragon had been unavoidable, and there was no reason for me to feel sorry.

If anything, it had been grateful to us for stopping it, even if we had needed to do so this way.

But I was apologizing because I couldn’t bury its body as it was.

*The corpse.*

The raid was over. It was time to dispose of the corpse.

[^1]: A zhang is a traditional East Asian unit of length, roughly 3.3 meters.
```

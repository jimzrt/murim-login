<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0535.txt",
      "sha256": "c32323f009d6a2721e84805f2cff6776e2fa6413092ff55dc04099e48fc19524",
      "bytes": 12676
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "7b8b741cf0a9bd92bd19c61fe6c0f770226d332e68555a8a52824138eb7d4c7d",
      "bytes": 3518
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "d8c18ae743bf916cb374fcf6cb39850d751272c899ce393c99b2de175371a016",
      "bytes": 170129
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "e5a0d715909fd6b5a8ca63d95d4a5910df7d1d94daa97e8f7b72b127e8945f9e",
      "bytes": 1070
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "e797d2a209a813f1cab7c5bade1313be437b6f0f7b056e02ee9d3d52a9a92825",
      "bytes": 553
    },
    {
      "path": "characters/Gung Gibang.md",
      "sha256": "d1d71412069661d543cbfbbf0beef4f17737797934b7398026c4a12e8aaa3e92",
      "bytes": 686
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "06296b5e521b031aa9f1e1224234644967a71209f47813ab913622afdf3a8648",
      "bytes": 1108
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "d25a7a40b4509337361dc3707b6649f44783c389bf562424e7956326d45b9967",
      "bytes": 1630
    },
    {
      "path": "characters/Jin Wikyung.md",
      "sha256": "9c24d22b9a11e97f30f576d8722b54b0f83581630aa2e7f53d95cf76fe2f6d9c",
      "bytes": 1210
    },
    {
      "path": "characters/Jung Ho.md",
      "sha256": "06b1286a1064c2a31f293bb93988b72572ca68899ff778fffcc2e225c121cadb",
      "bytes": 699
    },
    {
      "path": "characters/Mae Jonghak.md",
      "sha256": "afb67072a170869af0a67baf51eeab12a700f7e82c82fdb9bec33939d5382b35",
      "bytes": 985
    },
    {
      "path": "characters/Mungyeong.md",
      "sha256": "bd703170aa5b5190c655947a6247cf58712137cad7bee4a9e0a8fd4ab3e4ac70",
      "bytes": 1168
    },
    {
      "path": "characters/Peng Cheolhu.md",
      "sha256": "d6bb98df0c6469d43357fc08679a77a8cd2965c7125a449d275c545d386bc6cf",
      "bytes": 680
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "f988869c7dc358c9c520950efdf6099e024bccda202597f813ec9fd47a8a0706",
      "bytes": 160904
    }
  ],
  "estimated_tokens": 13364
}
-->

# Durable State Update — Chapter 535

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 535. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 535. Profile updates may replace only one
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
  "chapter": 535,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 535,
    "continuity_sources": [535],
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
    "Jin Taekyung and Cheongpung's prominent role in raising the Murim Alliance flag made them objects of intense attention among Murim factions.",
    "Taekyung believes the Zhongnan Sect resents him, the Jin Family of Taiyuan, and Jeok Cheongang after its repeated humiliations and will obstruct them.",
    "Cheongpung created Mimi Step from Mimi's movements; it is a snake-like footwork technique fast enough that Taekyung could barely track it with his naked eyes, and Cheongpung has recently lost his appetite while refining it.",
    "Mungyeong ended Taekyung's direct training and assigned him a final task of incorporating martial principles into his learned martial arts.",
    "Zhuge Feng's Demon-Sealing Formation still blocks all mana from the exposed Gate, while Jang Taebo is summoning artisans to process the Water God Dragon's remains.",
    "The Southern Heaven Demon Empress is traveling toward Yunnan and expects to cause further deaths.",
    "Unnamed, Hong Dao's practical Disciple, is a scarred Supreme Peak master and Jung Ho's young Martial Uncle after enduring Repentance Cave and receiving Shaolin's Great Restoration Pill.",
    "The Black Dragon Demon Gate remains a major unorthodox power descended from the Demonic Cult's Twelve Branches; Sama Pyo is its Young Sect Leader and Black Dragon Saber, and Taishan is his giant subordinate.",
    "Jin Taekyung remains a Supreme Peak master with Three Flowers Gather at the Crown, advanced qi perception, exceptional resistance to monster Fear, and public S-rank-level recognition despite retaining an A-rank license.",
    "Ju Hwaran is with Taekyung at Gowolru, Song Ilseom remains her direct escort, and her former political engagement to Sama Pyo was accepted for her father's sake.",
    "Sama Pyo and Taishan have left Gowolru under scrutiny; Taishan is absolutely loyal to Sama Pyo but regards Taekyung as strong and kind, and the Alliance Leader is seeking Taekyung."
  ],
  "continuity_sources": [
    534,
    533
  ],
  "open_questions": [
    "What is the Lord of Heaven's identity, how is he connected to the dangerous force Taekyung associates with his original world, and how can Dark Heaven open Gates?",
    "Where is the Southern Heaven Demon Empress ultimately headed, and what does she intend to do in Yunnan?",
    "What is the outcome of the duel between Jeok Cheongang and Nangong Cheon, the Azure Sky Sword King?",
    "Why did Ju Hwaran and Sama Pyo's political engagement end?",
    "Why is the Alliance Leader seeking Jin Taekyung?"
  ],
  "safe_through": 534,
  "temporary_decisions": [
    "Render 고월루 as Gowolru, 곤륜운룡 as Kunlun Cloud Dragon, and 학우 as Hak Woo; render 전 정혼자 contextually as former fiancé or former fiancée.",
    "Render 탈진 as the capitalized system status Exhaustion; retain Ten Dragons and Phoenixes, Blazing Flame Divine Dragon, Dark Heaven, Murim Alliance, and Old Master.",
    "Render 황보세가 as Hwangbo Family, 소가주 as Lesser Family Head, 은비화 as Dagger Hidden Flower, and 전음 as Sound Transmission.",
    "Preserve the chapter's blunt profanity, financial-therapy humor, and monster-comparison humor.",
    "Render 일기천룡 as One-Ride Heavenly Dragon and Taishan's speech as clipped, childlike, and literal."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진위경    | **Jin Wikyung**    |
| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 매종학    | **Mae Jonghak**    |
| 청풍     | **Cheongpung**     |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 검성     | **Sword Saint**               | Mae Jonghak    |
| 무신     | **Martial God**               | —              |
| 벽력도왕   | **Thunderbolt Saber King**    | Peng Cheolhu   |
| 일신     | **One God**         |
| 삼성     | **Three Saints**    |
| 십왕     | **Ten Kings**       |
| 무림맹    | **Murim Alliance**               |
| 절정     | **Peak**          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 검기     | **Sword Energy**                                 | When functioning as projected weapon qi               |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 중원     | **Central Plains**                               |                                                       |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 장문인    | **Sect Leader**                              |
| 전각     | **pavilion**                                 | Use “hall” only when established for a specific named building |
| 은인     | **Benefactor**                               |
| 상태               | **Status**                     |
| 노부      | **this old man / I**                                            |
| 본문      | **our sect / this sect**                                        |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 소협      | **Young Hero**                                                  |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 궁기방 | **Gung Gibang** | Beggars' Sect Successor Beggar and finalist. |
| 정호 | **Jung Ho** | Middle-aged Shaolin martial monk leading the traveling group. |
| 문경 | **Mungyeong** | Young medical apprentice and newly introduced passenger. |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 구주 | **Nine Provinces** | Traditional geographic expression used in a threat. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 오대세가 | **Five Great Families** | Major Murim grouping. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 창천검왕 | **Azure Sky Sword King** | One of the Ten Kings and the Grand Family Head of the Nangong Family. |
| 성라대연 | **Star-Array Grand Banquet** | Major martial gathering held in Henan every two or three years. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 숭산 | **Mount Song** | Mountain where Shaolin Temple is located. |
| 창천 | **azure heaven** | The cloudless sky seen by Namgung Ryong. |
| 검왕 | **Sword King** | Short form for the Azure Sky Sword King, Nangong Cheon. |
| 노야 | **Old Master** | Taekyung's private address for Jeok Cheongang. |
| 미미 | **Mimi** | Worker at Honghwaru referenced in Taekyung's joke. |
| 오대 | **Five Squads** | Named Tang Clan organizational group in Tang Sadok's mobilization order. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 동정호 | **Dongting Lake** | Lake under which Dangyang and Honghu Strongholds operated. |
| 혈어 | **Blood Fish** | Local name for the aggressive mutated fish in the Gate's waterways. |
| 이룡 | **Two Dragons** | Collective ranking beneath the Ten Kings in Murim gossip. |
| 검기상인 | **the level of injuring others with Sword Energy** | Realm description used for Moon Beauty Saber. |
| 맹주전 | **Alliance Leader's Hall** | Hall directly associated with the Murim Alliance Leader. |
| 숭산결의 | **Mount Song Resolution** | The event marking the formal gathering of the Murim Alliance at Mount Song. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혁무진 | 진위경 | Jin Family subordinate to Lesser Family Head | Lesser Family Head | deferential | Uses 소가주님 while confessing that he accepted Taekyung's invitation. |
| 진위경 | 혁무진 | Lesser Family Head to direct family subordinate | you | formal-but-familiar | Uses 자네 while recognizing Mujin and instructing him to keep helping Taekyung. |
| 청풍 | 혁무진 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung includes Mujin among his 은인들 after receiving the skewers. |
| 혁무진 | 청풍 | martial artist to young master | Young Master | formal-deferential | Mujin uses 공자께서는 when asking why Cheongpung descended from the mountain. |
| 매종학 | 청풍 | grandfather_to_grandson | Pung | affectionate-instructional | Mae Jonghak calls young Cheongpung 풍아 while teaching him the Crouching Tiger Fist. |
| 적천강 | 청풍 | overwhelming_elder_to_young_martial_artist | you / little punk | blunt, amused, and threatening | Jeok Cheongang uses 네, 이놈, and related blunt forms while testing Cheongpung. |
| 청풍 | 적천강 | young_martial_artist_to_overwhelming_elder | Grandpa Jeok | casual-familiar despite deference | Cheongpung uses 적 할아버지 while asking Jeok Cheongang to confirm Taekyung's condition; this is a familial form of address, not literal kinship. |
| 혁무진 | 적천강 | subordinate_to_overwhelming_elder | Great Hero Jeok | deferential and fearful | Mujin uses 적 대협 while reporting Jeok’s orders and Taekyung’s awakening. |
| 적천강 | 혁무진 | overwhelming_elder_to_junior_martial_artist | you stupid fool | blunt and mocking | Jeok calls Mujin a 멍청한 놈 after knocking him down during the attempted escape. |
| 진위경 | 적천강 | host_to_legendary_guest | Great Hero Jeok | formal-deferential | Introduces himself and pays respects to Jeok Cheongang as the Fire King. |
| 적천강 | 진위경 | elder_to_younger_family_head | you | gruff and teasing | Uses 자네 while mistaking Wikyung for Taekyung’s father and questioning his age. |
| 상인 | 적천강 | merchant_to_legendary_martial_master | Great Hero Jeok | deferential and flattering | Praises Jeok Cheongang while presenting the Poison-Averting Ring and requesting help. |
| 적천강 | 상인 | legendary_guest_to_merchant | you | blunt and transactional | Cuts off the merchant’s praise, asks his identity and origin, and accepts the gift without committing to the requested favor. |
| 적천강 | 벽력도왕 | rival_martial_master_to_rival_martial_master | Virility Saber King | insulting and taunting | Jeok coins 정력도왕 as a taunting replacement for the established title. |
| 벽력도왕 | 적천강 | rival_martial_master_to_rival_martial_master | Jeok Cheongang | boisterous and hostile-teasing | The Thunderbolt Saber King calls Jeok by name before their argument escalates. |
| 청풍 | 문경 | martial_companion_to_medical_apprentice | Medical Apprentice | cheerful-polite | Cheongpung addresses Mungyeong as 의생님 while asking him to greet the Tang Clan. |
| 혁무진 | 궁기방 | squad_companion_to_Beggars_Sect_successor | Young Hero Gung | formal-polite, then pointed | Uses 궁 소협 while asking about the culprit and challenging Gung’s insults. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 문경 | 적천강 | old_acquaintances | Fire King | familiar and grave | The figure bearing Mungyeong’s name greets Jeok Cheongang by his established epithet. |
| 궁기방 | 혁무진 | squad_companions | you; that lunatic | insulting-casual | Gung Gibang mocks Hyuk Mujin's injuries and calls him a lunatic for attacking the Third Fiend. |
| 궁기방 | 청풍 | martial_companions | Young Hero Cheongpung | formal-polite | Gung Gibang uses 청 소협 while asking why Cheongpung is at the temporary clinic. |
| 청풍 | 미미 | handler_to_companion_snake | Mimi | cheerful-commanding | Cheongpung repeatedly calls and commands the Thousand-Year Poison Horned Snake. |
| 진위경 | 막내 | older brother to younger brother | my youngest | intimate and informal | Jin Wikyung uses 막내야 affectionately for Jin Taekyung. |
| 적천강 | 문경 | overwhelming elder to old acquaintance | you / little punk | mocking and threatening | Mocks Mungyeong's expression and threatens to poke out his eyes. |
| 적천강 | 궁기방 | overwhelming_elder_to_younger_martial_artist | you | blunt and threatening | Jeok Cheongang rebukes Gung Gibang for speaking informally and orders him to lie down. |
| 궁기방 | 진위경 | martial_companion_to_family_head | Great Hero Jin | familiar and polite | Asks Jin Wikyung not to exclude the Beggars' Sect from the defense. |
| 문경 | 혁무진 | traveling_companion_to_traveling_companion | Martial Warrior Hyuk | formal-polite | Mungyeong asks Mujin to deliver water to Taekyung and lets Mujin receive the credit. |
| 혁무진 | 문경 | traveling_companion_to_traveling_companion | Mungyeong | casual-familiar | Mujin recognizes Mungyeong while reacting to Taekyung's dismantling work. |
| 진위경 | 문경 | Jin Family Lesser Family Head to medical apprentice | you | formal-polite | Asks whether Jin Taekyung will arrive soon. |
| 적천강 | 창천검왕 | long-standing martial rival and duel partner | Azure Sky Sword King | blunt and familiar | Explicitly names him while coming to fulfill their long-delayed duel promise. |
| 창천검왕 | 적천강 | long-standing martial rival and duel partner | Fire King | formal and familiar | Addresses Jeok Cheongang by title while welcoming the promised duel. |
| 창천검왕 | 벽력도왕 | Ten Kings peers | Sir Peng | formal but familiar | Tells Peng to calm himself after Peng's argument with Taekyung. |
| 벽력도왕 | 창천검왕 | Ten Kings peers | Great Hero Nangong | respectful and familiar | Addresses Nangong Cheon while crediting him with preventing a catastrophe. |
| 매종학 | 적천강 | long-standing martial rival and friend | Great Hero Jeok | casual and familiar | Mae addresses Jeok as 적 대협 while discussing the Alliance Leader position. |
| 적천강 | 매종학 | long-standing martial rival and friend | you | blunt and familiar | Jeok addresses Mae as 당신 while recalling their meeting at Mount Jiuhua. |
| 벽력도왕 | 매종학 | Ten Kings peer to Ten Kings peer | Sword Saint | familiar and blunt | Asks Mae what was discussed in the sealed meeting. |
| 매종학 | 벽력도왕 | Ten Kings peer to Ten Kings peer | Peng | casual and admonitory | Calls him 팽가야 and tells him to remain quiet. |

## Listed compact profiles

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 532
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, the grandson and Disciple of Sword Saint Mae Jonghak, a Supreme Peak martial master known as the Huashan Divine Dragon, and the creator of the snake-inspired Mimi Step footwork technique.
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, a deep love of martial arts, competitive pride, unusual resistance to monster-induced Fear, and discomfort when someone copies his martial arts.
- **Voice:** Dreamy and hazy, with innocent, polite phrasing; he has begun imitating Taekyung's profanity.
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions while Taekyung is his only true martial rival; Tang Sadok has temporarily entrusted Mimi to him.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 533
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Gung Gibang.md

# Gung Gibang (궁기방)

- **Safe through:** Chapter 534
- **Aliases:** Successor Beggar, Beggar Prince, pure-blooded beggar, ultimate beggar
- **Role:** Gung Gibang is the Beggars' Sect Successor Beggar and a unique eight-knot disciple.
- **Personality:** Vulgar, aggressive, and quick-tempered.
- **Voice:** Blunt, profane, and vividly threatening.
- **Relationships:** Gung Gibang is a rival finalist alongside Baek Woo and Zhuge Gyun who trades insults with Taekyung, uses Beggars’ Sect intelligence to investigate Tang Taesang’s murder and Dark Heaven’s Hubei forces, and has now found a trace of Honglan.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 534
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers and Vice Squad Leader of the Jin Dragon Squad.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 532
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, and Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Jin Wikyung.md

# Jin Wikyung (진위경)

- **Safe through:** Chapter 534
- **Aliases:** Junzi Sword
- **Role:** Jin Wikyung is the thirty-six-year-old Lesser Family Head and future Family Head of the Jin Family of Taiyuan, the Alliance Leader who unified Shanxi Murim and Shanxi Province's foremost landowner and magnate.
- **Personality:** Calm, authoritative, and politically capable in public; protective and affectionate toward Taekyung beneath a stern mask. Takes responsibility for his people, acts decisively under pressure, and prioritizes family survival.
- **Voice:** Restrained, formal, and commanding with subordinates; openly affectionate, proud, and occasionally exuberant with Taekyung.
- **Relationships:** Jin Wikyung is Taekyung's eldest brother and future Family Head who protects and mentors him, commands Wipeng and the Jin Family's forces, has worked with Jeok Cheongang, and maintains a political connection with Hongcheon, Prince Shangshan's hidden loyal retainer; Jin Mukyung is his younger brother and a potential successor alongside Taekyung.

### Jung Ho.md

# Jung Ho (정호)

- **Safe through:** Chapter 522
- **Aliases:** None
- **Role:** Middle-aged Shaolin martial monk and Master of Shaolin's Discipline Hall who leads the traveling group and wields a Zen staff hung with prayer beads.
- **Personality:** Humble, observant, principled, and concerned with the safety of commoners.
- **Voice:** Formal, restrained, and admonitory, with Buddhist phrasing.
- **Relationships:** Unnamed is his young Martial Uncle; he leads the Shaolin monks traveling with him, addresses Sama Pyo as a Benefactor, and is recognized by Jin Taekyung as Park Jung Ho, a former Garam Middle School classmate.

### Mae Jonghak.md

# Mae Jonghak (매종학)

- **Safe through:** Chapter 527
- **Aliases:** Sword Saint
- **Role:** Sword Saint and Cheongpung's grandfather who now serves as the New Murim Alliance's Alliance Leader.
- **Personality:** Playful, easygoing, and teasing, but capable of handling heavy administrative responsibilities efficiently.
- **Voice:** Friendly, casually familiar, and cheerfully teasing, including when greeting old acquaintances and discussing leadership.
- **Relationships:** Cheongpung's grandfather and martial instructor; taught him the Taeeul Miri Palm; secretly entered Huashan while its Sect Leader slept, left a dagger and handwritten note, and then went into hiding, prompting Huashan's search; fought Jeok Cheongang at Mount Jiuhua more than forty years ago and left after their draw; his old friend Hong Dao left him a letter identifying Jin Taekyung as the Morning Star who would drive away darkness.

### Mungyeong.md

# Mungyeong (문경)

- **Safe through:** Chapter 526
- **Aliases:** Killing Ghost
- **Role:** Mungyeong is the legendary physician known as the former Divine Physician and Slaughter Saint, a Returned to Youth Supreme Peak master and the greatest assassin in history; he was the sole survivor of an assassin training cohort that began with three hundred candidates and passed the Divine Physician title to his Disciple.
- **Personality:** Compassionate, resolute, resourceful, and calm under extreme pressure.
- **Voice:** His Mungyeong persona is timid, deferential, and cheerful, while his Slaughter Saint voice is dry, impassive, and blunt.
- **Relationships:** Dong Feng is his Disciple, Jeok Cheongang is an old acquaintance whom Mungyeong helped break free of his Heart Demon, Mungyeong was asked to look after and instruct Jin Taekyung and has now ended that direct training after teaching him martial principles and giving him a custom fire-qi pill, and Mu Song plus five Water Dragon Stronghold subordinates know he is an exceptionally powerful master but not that he is the Slaughter Saint.

### Peng Cheolhu.md

# Peng Cheolhu (벽력도왕)

- **Safe through:** Chapter 522
- **Aliases:** Thunderbolt Saber King
- **Role:** Peng Cheolhu is the Thunderbolt Saber King, a Ten Kings master and Great Hero of the Hebei Peng Family.
- **Personality:** Boisterous, hot-tempered, argumentative, and protective toward those connected to his close friend Hong Dao.
- **Voice:** Loud, blunt, confrontational, and prone to disguising embarrassment or retreat as serious martial instruction.
- **Relationships:** Long-standing rival and friend of Jeok Cheongang; close friend of Hong Dao; protective toward Hong Dao's Disciple Unnamed.

## Korean source

```text
＃535화



“매 대협. 아니 맹주께서 찾으신다.”

갑작스러운 진위경의 말에 순간 멈칫한 내가 되물었다.

“저를 말입니까?”

“그래. 그리고 청 소협도 함께.”

나에 이어 청풍까지?

진위경에게 그 이유를 물어보려던 찰나, 전각에 나 있는 창에서 익숙한 얼굴이 불쑥 튀어나왔다.

“할아버지! 지금 할아버지 만나러 가요?”

기대가 잔뜩 담긴 청풍의 외침에, 희미하게 웃은 진위경이 작게 고개를 저었다.

“자네의 조부님이 아니라, 맹주께서 찾으시는 거라네.”

“네. 그러니까 할아버지요!”

“같지만 다르지. 여하튼 청 소협도 조속히 채비해서 내려오게.”

“잠시만요! 만두 좀 챙기고요!”

“그래, 골고루 챙기게. 당과도.”

짬밥 좀 먹었나. 눈 하나 깜빡하지 않는 것 보소.

진위경도 청풍을 한두 번 본 것이 아니라 그런지, 이제는 대처가 물 흐르듯 자연스럽다.

청풍이 우당탕탕 소리를 내며 사라지자 진위경의 시선이 나를 향했다.

“이유를 묻지 않는구나.”

“……물어볼 틈이 없었다는 게 정확한 것 같은데요.”

“그것도 그렇군.”

“어차피 이렇게 된 거, 가서 직접 듣겠습니다. 사실 벌써 느낌이 살짝 오긴 했거든요.”

“무슨 느낌?”

“음, 손주 얼굴이나 보려고 부르진 않았을 것 같다는 느낌이죠.”

나와 청풍을 찾는다.

검성 매종학이, 아니. 무림맹의 맹주가.

같은 사람이지만 어떤 이름이냐에 따라 의미가 다르다. 앞서 진위경이 청풍의 호칭을 정정했던 것은 그런 뜻이 내포되어 있을 것이다.

‘무림맹주.’

그 이름은 무겁다. 그리고 구주(九州)를 종횡하는 수많은 무림인과 천하 무림을 양쪽 어깨에 짊어진 거인이 나를 보고자 한다는 건…….

‘아무리 생각해도 쎄한데.’

그새 또 다른 사건이 터진 걸까.

내심 그렇게 생각하고 있던 바로 그때였다.

쉬이이익!

바람 부는 소리와 함께 청풍이 모습을 드러냈다. 손에는 빵빵하게 부풀어 오른 비단 보자기가 들려 있었고, 상반신에는 번쩍거리는 은빛 갑옷을 걸친 채였다.

잠깐. 갑옷?

취릭.

“이제 왔. 뭐여, 시벌.”

“미미요. 쑥쑥 커 버려서 이제 품 안에 못 넣고 다녀요.”

“……그럼 두고 가는 건 어때.”

청풍이 고개를 갸웃거렸다.

“왜요?”

“지금 진심으로 몰라서 묻는 거야?”

“네!”

“오…… 대답 한 치의 망설임도 없는 것 봐. 환장하겠네.”

뱀이다. 그냥 뱀도 아닌 뿔 달린 뱀.

이제 미미라는 이름이 잘못되었다고 느껴질 만큼 떡대도 상당하다.

결론만 말하자면, 무림맹에 뱀 애호가가 몇 명이나 있을지는 몰라도 딱히 환영받을 만한 반려 뱀은 아니라는 거지.

“……도대체 얘한테 뭘 먹인 거야?”

“헤헤. 엄청 많이 컸죠. 은인이 맞춰 보세요.”

나는 망설임 없이 대답했다.

“스테로이드.”

“주로 만두랑 당과 먹였는데요. 아, 혈어(血魚)를 먹인 이후로 확실히 엄청 커진 것 같긴 해요.”

도대체 뱀한테 만두랑 당과를 왜 먹이냐고 따지려던 나는 멈칫했다.

“혈어?”

“네.”

혈어는 동정호를 통해 마력에 오염된 물고기들이다.

그럼 한마디로 단단히 상한 음식을 먹었다는 건데…….

“안 되겠다. 미미는 두고 가.”

“괜찮은데요.”

“다른 사람이 안 괜찮아. 물 수도 있잖아.”

“아니에요. 미미는 물라고 해도 안 물어요. 보실래요?”

다급한 표정을 지은 청풍이 미미를 향해 손을 뻗었다.

“미미, 물어!”

쐐액, 딱!

그야말로 순식간이었다.

아가리를 쩍 벌린 미미가 번개처럼 쇄도하고, 그보다 빠른 속도로 청풍의 손이 사라졌다.

텅 빈 허공을 향해 이빨을 딱 부딪친 미미가 아쉽다는 듯 혀를 날름거렸다.

취릭.

“보세요. 안 물죠?”

“…….”

“…….”

미친놈인가.

‘아니, 이건 그냥 못 문 거잖아.’

나를 포함한 모두가 할 말을 잃은 그때, 청풍이 울상이 된 얼굴로 중얼거렸다.

“살, 아니 문경이가 괜찮다고 했는데…….”

“문경이가?”

“네. 요새 자주 보거든요. 그때 미미 상태도 살펴봤어요.”

그러고 보니 요새 통 청풍과 문경이 눈에 잘 띄지 않았다. 내가 바쁜 탓도 있었겠지만, 자주 본다는 청풍의 말을 들어보니 그것 때문만은 아닌 것 같다.

‘다른 사람한테는 관심도 안 주던 인간이. 갑자기 무슨 바람이 불어서?’

가늘어지는 내 눈초리를 본 청풍이 헛숨을 삼켰다.

“헙.”

“왜?”

“아니에요. 아무것도.”

이렇게 나오니까 더 수상쩍은데.

하지만 나는 어깨를 으쓱하는 것으로 상황을 마무리했다. 진위경이 슬슬 초조해지기 시작하는 것이 눈에 보였기 때문이다.

“막내야, 그.”

“아, 죄송해요. 많이 급합니까?”

“솔직히 늦어서 좋을 건 없겠지. 다른 분들도 함께 기다리고 계실 테니.”

다른 분들?

이거 생각보다 판이 제법 큰 모양이다.

나는 껄끄러운 마음을 숨기며 청풍을 향해 턱짓했다.

“가자, 청 소협.”

“네, 은인!”

궁기방과 혁무진이 굳은 얼굴로 고개를 끄덕였다.

“그래, 가 보자고.”

“제가 모시겠습니다, 조장님. 그리고 소가주님.”

“너희 둘은 개소리하지 말고 남아서 때랑 똥이나 닦아.”

“…….”

“…….”



* * *



하나의 작은 도시를 연상케 하는 무림맹.

그중에서도 중심에 우뚝 선 맹주전(盟主殿)에 들어선 우리는 커다란 문 앞에 섰다.

“오셨군요.”

경직된 눈빛과 표정. 그리고 잘 갈무리된 기세.

의심의 여지 없이 검기상인(劒氣傷人)의 경지에 오른 절정 고수지만, 이 이름 모를 사내의 역할은 문지기에 불과하다.

이미 진위경과는 일면식이 있는지, 나지막한 인사를 건넨 그가 문을 열었다.

드르륵. 드르륵. 드르륵.

차례차례 울리는 마찰음. 그렇게 자그마치 다섯 개의 문이 열리고 나서야 보이는 광경에, 나는 내심 중얼거렸다.

‘그놈들 놔두고 오길 잘했네.’

궁기방과 혁무진은 나한테 감사해야 한다.

따라왔다면 아마 이 자리에서 악취와 똥 냄새를 풍기며 입 벙긋 못한 채 식은땀만 줄줄 흘렸을 테니까.

그만큼 거대한 탁자를 두고 자리한 이들의 면면과 기세는 대단했다.

“와아.”

옆에서 자그마한 탄성이 흘러나온다. 눈을 동그랗게 뜬 채 주위를 둘러보는 청풍의 옆구리를 쿡 찌른 진위경이 전음을 흘려보냈다.

- 난 여기까지다.

무슨 뜻인지 알아듣기에는 충분하다.

고개를 끄덕인 나는 문턱을 넘어 걸음을 내디뎠다.

저벅.

고요한 적막 속에서 울려 퍼지는 발걸음.

그와 동시에 날카롭고, 덤덤하며, 한편으로는 경탄과 호기심이 어린 시선들이 나와 청풍을 향해 쏟아진다.

“허어. 바로 저 아이들이 말로만 듣던…….”

“다시 봐도 대단합니다.”

“흠. 제법이긴 하군.”

“무슨 소리. 실로 대단한 일이오. 무림 전체의 홍복이 아닐 수 없소.”

좌우로 흘러나오는 늙수그레한 목소리의 주인들.

지고한 경지의 무공에 도달하여 노화를 더디게 만들었음에도 하나 같이 새하얗게 흰 터럭은 그들이 흘려보낸 시간을 짐작게 하기에 충분했다.

‘구파일방. 그리고 오대세가의 장문인과 가주들.’

천하 무림을 떠받치는 열다섯 개의 기둥.

무림의 전국구 이벤트라고 부를 수 있는 성라대연 때도 그들 모두가 모인 적은 없었다.

심지어 무림맹이 선포되던 숭산결의 때조차 그랬다. 워낙 거리가 먼 탓에 일정에 맞춰 도착하지 못한 이들이 있었기 때문이었다.

하지만 드디어…….

‘모두가 한자리에 모였다.’

성라대연이 이제 막 떠오르기 시작한 별들의 잔치였다면, 이 자리는 유구한 무림 사에 자신만의 이름과 족적을 아로새긴 거인(巨人)들의 연회다.

그리고 이 연회에서도 단연 거대한 존재감을 뿜어내는 몇 사람이 있었다.

더 이상 일가(一家)의 가주가 아님에도 그 이상의 영향력을 발휘하는 그들을, 천하의 무림인들은 경의를 담아 이렇게 불렀다.

일신(一神), 삼성(三星), 십왕(十王).

과거, 붉게 물든 서쪽 하늘을 등지고 중원을 향하여 쏘아진 십만의 마군(魔軍)이 있었고, 그에 맞선 영웅들이 있었다.

그들은 적을 가르는 검과 창이었고, 중원을 수호하는 방패였으며, 마침내는 거대하고도 빛나는 신화가 되었다.

무신이라는 하늘이 사라지자 하늘을 빛내던 세 개의 별들이 하나둘씩 자취를 감추었고, 스스로 왕좌에서 내려온 열 명의 왕들은 서서히 죽거나 늙었지만 그중 일부는 이 자리로 돌아왔다.

‘창천검왕, 벽력도왕. 그리고…….’

낯익은 얼굴도, 낯선 얼굴도 있다.

그리고 그중에서도 가장 눈에 띄는 한 사람이 나를 보며 눈썹을 들썩였다.

- 부른 지가 언젠데 이제야 오다니. 네놈이 죽고 싶어서 환장했구나.

화왕 적천강.

퉁명스럽지만 따뜻함이 담긴 그의 전음에, 나도 모르게 소리 없는 웃음이 흘러나온다.

- 이놈 보게. 지금 웃음이 나오느냐?

그럼 나오는 걸 어떡합니까.

- 하여간 그놈 참. 방금까지는 잔뜩 굳어 있더니. 구파일방이나 오대세가나. 어차피 별거 없다. 전부 거기서 거기야. 본문이 최고지.

그 누가 이렇게 거침없이 말할 수 있을까.

당당하면서도 광오한 한마디에 이어, 짧은 망설임이 담긴 전음이 귓가에 닿았다.

- 그러니까 어깨 펴고 눈 부릅떠라. 네놈은…… 노부의 자긍심이다.

자긍심.

생각지도 못한 말이다.

비록 소리내어 말하지는 않았지만, 적천강이 내게 이런 말을 할 것이라고는 예상치 못했다.

나는 참지 못하고 입술을 달싹였다.

- 노야.

슬쩍 시선을 회피하고 있던 적천강의 신형이 움찔했다.

- 크흠.

- 노야.

- 왜, 왜 부르느냐.

- 약 드실 시간 같아서요.

- 이런 개호로…….

- 그리고 감사합니다.

- ……!

적천강의 붉은 눈썹이 파르르 떨렸다.

그에게서 시선을 뗀 나는 허리를 꼿꼿하게 폈다.

어느새 긴장으로 굳어 있던 전신의 근육이 부드럽게 이완되고 눈앞이 시원해진다.

‘난 누군가의 자긍심이다.’

아직 이 자리가 무엇을 위해 마련된 것인지 모르겠다.

하지만 적어도 한 가지 사실만큼은 안다.

잠시 잃어버렸다가 되찾은 지금의 당당함이, 나를 이 자리로 이끌었다는 것.

저벅.

나와 청풍의 걸음이 동시에 멈췄다.

멀고 길게 느껴졌던 복도가 끝났으니 더 이상 앞으로 나아갈 길이 없다.

우리를 보며 작게 대화를 주고받던 거인들의 목소리도 마치 이때만을 기다렸다는 듯이 뚝 끊겼다.

적막.

오직 한 사람을 기다리는, 그리고 한 사람을 위해 마련된 적막이다.

이십여 명의 거인들이 자리한 이곳에서 상석(上席)을 차지한 자.

새하얗게 흰 터럭 대신 검게 물든 머리카락과 투명한 눈동자를 지닌 그가 자리에서 일어났다.

드르륵.

광활한 천하 위에 펼쳐진 하늘을 수놓았던 세 개의 별.

그중에서도 가장 빛나는 동시에 유일한 별이 되어 버린 검성(劍星) 매종학이 입을 열었다.

아니.

‘무림맹주 매종학.’

이 자리에 서 있는 것은 바로 그다.

그리고 그것은 나 혼자만이 깨달은 부분이 아니었다.

청풍의 입술 사이로 나만 알아들을 수 있을 만큼 희미한 목소리가 흘러나왔다.

“할아버지…….”

청풍과 나를 바라보는 매종학의 입가에 따뜻한 미소가 스쳤다.

동시에 그의 입술 사이로 힘이 담긴 음성이 흘러나왔다.

“이룡각(二龍閣)의 주인들이 왔구나.”
```

## Final English reading copy

```markdown
# Chapter 535

“Great Hero Mae. No—the Alliance Leader is looking for you.”

Jin Wikyung’s sudden words made me pause.

“Me?”

“Yes. And Young Hero Cheongpung as well.”

Cheongpung too?

I was about to ask Jin Wikyung why when a familiar face suddenly popped out through the window of the pavilion.

“Grandpa! Are we going to see Grandpa now?”

At Cheongpung’s excited shout, Jin Wikyung smiled faintly and gave a small shake of his head.

“Not your grandfather. The Alliance Leader is looking for you.”

“Yes. So, Grandpa!”

“It’s the same person, but not the same. Regardless, Young Hero Cheongpung, prepare yourself and come down as soon as you can.”

“Wait! I need to pack some dumplings!”

“All right. Pack a variety. And some sweets, too.”

*He’s gotten some experience with this. Look at him not even blinking.*

Jin Wikyung must have seen Cheongpung more than once or twice by now, because he handled him as naturally as flowing water.

When Cheongpung disappeared with a great clatter, Jin Wikyung turned his gaze toward me.

“You aren’t asking why.”

“……I’d say it’s more accurate to say I haven’t had a chance to ask.”

“That’s true.”

“Since it’s come to this, I’ll go and hear it directly. Actually, I already have a bit of a feeling about this.”

“What sort of feeling?”

“Well, I don’t think he called us here just to see his grandson’s face.”

They were looking for Cheongpung and me.

Sword Saint Mae Jonghak—or rather, the Alliance Leader of the Murim Alliance.

They were the same person, but the meaning changed depending on which name one used. That was probably why Jin Wikyung had corrected Cheongpung’s form of address.

*The Alliance Leader.*

That name carried weight. And the fact that a giant who carried the countless martial artists crisscrossing the Nine Provinces, as well as the entire Murim beneath heaven, on both shoulders wanted to see me…

*No matter how I think about it, this feels ominous.*

Had another incident broken out already?

I was thinking that when—

Whoosh!

Along with the sound of rushing wind, Cheongpung appeared. He was carrying a bulging silk bundle in one hand, and his upper body was clad in gleaming silver armor.

Wait.

Armor?

Hiss.

“I’m here now. What the hell.”

“It’s Mimi. She’s gotten so big that I can’t carry her in my arms anymore.”

“……Then how about leaving her behind?”

Cheongpung tilted his head.

“Why?”

“Are you seriously asking because you don’t know?”

“Yes!”

“Oh… Not even a moment’s hesitation. This is driving me insane.”

She was a snake. Not just any snake, but a snake with horns.

She had grown so bulky that Mimi no longer even felt like the right name for her.

Bottom line, I had no idea how many snake enthusiasts there were in the Murim Alliance, but she wasn’t exactly the kind of pet snake they would welcome.

“……What the hell have you been feeding her?”

“Hehe. She’s gotten really big, hasn’t she? Take a guess, Benefactor.”

I answered without hesitation.

“Steroids.”

“Mostly dumplings and sweets. Oh, she definitely seems to have gotten a lot bigger after eating the Blood Fish.”

I stopped just as I was about to demand why he had been feeding a snake dumplings and sweets.

“Blood Fish?”

“Yes.”

The Blood Fish were fish from Dongting Lake that had been contaminated by mana.

In other words, she had eaten something seriously spoiled…

“This won’t do. Mimi stays here.”

“She’s fine.”

“Other people might not be. She could bite them.”

“No, Mimi won’t bite even if someone tells her to. Would you like to see?”

Cheongpung reached toward Mimi with an urgent expression.

“Mimi, bite!”

Swish. Clack!

It happened in the blink of an eye.

Mimi opened her jaws wide and lunged like lightning. Cheongpung’s hand vanished even faster.

Mimi’s teeth snapped together in empty air, and she flicked her tongue as though disappointed.

Hiss.

“See? She didn’t bite.”

“……”

“……”

*Is he insane?*

*No, she simply failed to bite him.*

Just as everyone—including me—lost the ability to speak, Cheongpung muttered with a crestfallen expression.

“The Sl—no, Mungyeong said she was fine…”

“Mungyeong?”

“Yes. I see him often these days. He checked Mimi’s condition then, too.”

Come to think of it, I hadn’t seen Cheongpung and Mungyeong around much lately. I had been busy, but judging by Cheongpung’s words, that wasn’t the only reason.

*The guy who never showed interest in anyone else. What suddenly got into him?*

Cheongpung swallowed a startled breath when he saw my narrowing eyes.

“Gasp.”

“Why?”

“It’s nothing.”

That made him even more suspicious.

Still, I ended the matter with a shrug. Jin Wikyung was visibly beginning to grow anxious.

“My youngest, that…”

“Oh, sorry. Is it urgent?”

“To be honest, there’s no benefit to being late. The others are waiting as well.”

*The others?*

This seemed to be a much bigger affair than I had expected.

Hiding my unease, I jerked my chin toward Cheongpung.

“Let’s go, Young Hero Cheongpung.”

“Yes, Benefactor!”

Gung Gibang and Hyuk Mujin nodded with grim expressions.

“Right. Let’s go.”

“I’ll escort you, Captain. And you as well, Lesser Family Head.”

“You two shut up and stay here to clean up the grime and shit.”

“……”

“……”

* * *

The Murim Alliance resembled a small city.

At its center stood the Alliance Leader’s Hall, and we entered it before stopping in front of a massive door.

“You’ve arrived.”

The guard had a rigid gaze and expression, along with a carefully contained aura.

There was no doubt that he was a Peak master who had reached the level of injuring others with Sword Energy. But the role of this nameless man was nothing more than guarding the door.

He seemed to know Jin Wikyung already. After offering a quiet greeting, he opened the door.

Rattle. Rattle. Rattle.

Scraping sounds rang out one after another. It took five doors opening in succession before the view beyond finally came into sight.

*Good thing I left those idiots behind.*

Gung Gibang and Hyuk Mujin ought to thank me.

If they had followed me, they would probably have been drenched in cold sweat here, unable to open their mouths while filling the room with the stench of dirt and shit.

That was how impressive the people seated around the enormous table were—their faces and auras alike.

“Wow.”

A small gasp escaped from beside me. Jin Wikyung poked Cheongpung in the side as he looked around with wide eyes, then sent a Sound Transmission.

*—This is as far as I go.*

It was easy enough to understand what he meant.

I nodded and stepped over the threshold.

Step.

My footsteps rang out through the quiet.

At the same time, sharp yet impassive gazes filled with awe and curiosity poured toward Cheongpung and me.

“Oh my. So those are the children we’ve heard so much about…”

“Even seeing them again, they’re extraordinary.”

“Hm. They’re not bad.”

“What are you talking about? This is a truly remarkable achievement. It is a blessing for the entire Murim.”

The voices came from both sides, all belonging to elderly men.

Although they had reached supreme realms of martial arts and slowed the aging process, every last hair on their heads was as white as snow. It was enough to give me an idea of how much time they had lived through.

*The leaders of the Nine Sects and One Gang, and the Family Heads of the Five Great Families.*

Fifteen pillars supporting the Murim beneath heaven.

Even during the Star-Array Grand Banquet, which could be called a nationwide Murim event, all of them had never gathered in one place.

The same had been true during the Mount Song Resolution, when the Murim Alliance was declared. Some of them had been unable to arrive in time because of the vast distances involved.

But now, at last…

*They’re all gathered in one place.*

If the Star-Array Grand Banquet had been a celebration of stars that had only just begun to rise, this place was a banquet of giants who had carved their names and footprints into the long history of the Murim.

And even among these giants, several figures radiated an especially immense presence.

Although they were no longer Family Heads, their influence surpassed that of any ordinary family leader. The martial artists of the world called them by names filled with reverence.

One God, Three Saints, and Ten Kings.

Long ago, a hundred-thousand-strong demonic army had surged toward the Central Plains with the blood-red western sky at its back, and heroes had risen to oppose it.

Those heroes had been the swords and spears that cleaved through the enemy, the shields that protected the Central Plains, and, in the end, a vast and radiant legend.

When the sky known as the Martial God disappeared, the three stars that had illuminated it vanished one after another. The ten kings who had stepped down from their thrones gradually died or grew old, but some of them had returned to this place.

*The Azure Sky Sword King, the Thunderbolt Saber King. And…*

There were familiar faces and unfamiliar ones.

But one person among them stood out above all the rest. When he saw me, he raised an eyebrow.

*—How long ago did I call you? And you’re only showing up now? You must be desperate to die.*

Fire King Jeok Cheongang.

His Sound Transmission was gruff, but warmth lay beneath it. A silent laugh escaped me before I could stop it.

*—Look at this bastard. You can laugh at a time like this?*

*What am I supposed to do if it comes out?*

*—Honestly. You were all stiff just now. The Nine Sects and One Gang, the Five Great Families—it doesn’t matter. None of them are anything special. They’re all the same. Our sect is the best.*

Who else could speak so fearlessly?

After that bold and arrogant declaration, another Sound Transmission reached my ears. This one contained a brief hesitation.

*—So straighten your shoulders and open your eyes wide. You… are this old man’s pride.*

Pride.

It was something I had never expected to hear.

Although he hadn’t said it aloud, I had never imagined Jeok Cheongang would say something like that to me.

Unable to hold back, I moved my lips.

*—Old Master.*

Jeok Cheongang, who had been subtly avoiding my gaze, flinched.

*—Ahem.*

*—Old Master.*

*—Wh-Why are you calling me?*

*—It seems like it’s time for you to take your medicine.*

*—You little fucking bastard…*

*—And thank you.*

*—……!*

Jeok Cheongang’s red eyebrows trembled.

I looked away from him and straightened my back.

The muscles throughout my body, which had stiffened from tension, gradually relaxed. My vision cleared.

*I am someone’s pride.*

I still didn’t know what this gathering had been arranged for.

But I knew at least one thing.

The confidence I had briefly lost and then regained had led me to this place.

Step.

Cheongpung and I stopped walking at the same time.

The corridor that had seemed so long and distant had ended. There was nowhere left to go.

The voices of the giants, who had been quietly speaking among themselves while watching us, abruptly fell silent as though they had been waiting for this exact moment.

Silence.

A silence waiting for one person, prepared for one person.

The man seated in the place of honor among the more than twenty giants rose to his feet.

Unlike the others, whose hair had turned completely white, his hair was black, and his eyes were clear.

Rattle.

Three stars had once embroidered the sky spread across the vast world.

Of those three, the Sword Saint Mae Jonghak had become both the brightest and the only remaining star.

He opened his mouth.

No.

*The Murim Alliance’s Alliance Leader, Mae Jonghak.*

That was who stood before us.

And I wasn’t the only one who realized it.

A voice so faint that only I could hear it slipped between Cheongpung’s lips.

“Grandpa…”

A warm smile crossed Mae Jonghak’s lips as he looked at Cheongpung and me.

At the same time, a powerful voice flowed from his mouth.

“The masters of the Two Dragons Pavilion have arrived.”
```

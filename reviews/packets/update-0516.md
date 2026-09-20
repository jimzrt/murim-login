<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0516.txt",
      "sha256": "fd5af22bc53e67422db2d6350309868ea64552012e836944159846d25518f958",
      "bytes": 14151
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "196c7b32a6061fa76aa9ac83ae1856a7925d03023dc57ab44f8d2b306c1c4b67",
      "bytes": 3866
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "2b5f1560e8b7774d35bce2e31040d739fb6b047347a38626eab821dc0540c25b",
      "bytes": 164518
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "89e12785388512028f5cb12bc150cd8490e7e28f8c3834570f33d437064205ac",
      "bytes": 1006
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "670e773c25439d81f067e70d64cb3c282930aa885b8b7893d7574c7042404ce7",
      "bytes": 553
    },
    {
      "path": "characters/Gung Gibang.md",
      "sha256": "0a11a904b81bd91896ed44764a21ea1939148b37b9ee8bae74372752d01799b0",
      "bytes": 686
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "4877a4ffc7b9737470e03110ac3e495e0d9deb820a10f76ee337458b95d726d6",
      "bytes": 1108
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "940723926f34de1b8017be7338d0ad1cf5f6ff31d5c7fcf9f32b08d69cdb1019",
      "bytes": 1630
    },
    {
      "path": "characters/Jin Wikyung.md",
      "sha256": "7903742aee9b1799c4e5a34eab85581d1427675263a1501b5ef910e690dd242f",
      "bytes": 1210
    },
    {
      "path": "characters/Jung Ho.md",
      "sha256": "eeabd4d13cd39d5cfb27765cb1f1b1a78797dec368635f11f7566bf655360d5e",
      "bytes": 642
    },
    {
      "path": "characters/Mungyeong.md",
      "sha256": "a4e4e5bfc6dd2491ae8a307fd64023084e8d8baecc6ada70a5e74fb6ee51375b",
      "bytes": 985
    },
    {
      "path": "characters/Unnamed.md",
      "sha256": "66cf762ef6980aa87453c8744fe9c15ca7b45a21a3908cf643bd74377065f85c",
      "bytes": 711
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "d6796ada79c98b888df1cf396c77ddf6aeac4561af151902440fd8d03149b2e5",
      "bytes": 156161
    }
  ],
  "estimated_tokens": 12888
}
-->

# Durable State Update — Chapter 516

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 516. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 516. Profile updates may replace only one
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
  "chapter": 516,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 516,
    "continuity_sources": [516],
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
    "The New Murim Alliance has been publicly announced from Mount Song, and major orthodox factions are moving to join it while heroes gather toward Henan.",
    "The Southern Heaven Demon Empress is traveling toward Yunnan and expects to cause further deaths.",
    "Jin Mukyung remains secluded in the training hall after losing to Cheongpung, refusing to emerge until he achieves a great accomplishment.",
    "The Yangtze River Channel League and Green Forest Alliance may become rear threats to the New Murim Alliance, while the North Sea Ice Palace remains isolationist and the Nanman Beast Palace may support orthodox Murim.",
    "Unnamed, Hong Dao's practical Disciple, has endured three months in Repentance Cave, achieved enlightenment, and emerged as Jung Ho's young Martial Uncle.",
    "Unnamed carries Hong Dao's will and recognizes the arriving Morning Star connected to Hong Dao's final instruction.",
    "The Black Dragon Demon Gate is an ancient unorthodox faction that once belonged to the Demonic Cult's Twelve Branches and now ranks among the Central Plains' strongest unorthodox powers."
  ],
  "continuity_sources": [
    515,
    514
  ],
  "open_questions": [
    "Will the Demon-Sealing Formation remain effective permanently, and can equivalent formations be installed repeatedly if more Gates appear?",
    "What is the Lord of Heaven's identity, and how is he connected to the dangerous force Taekyung associates with his original world?",
    "Where is the Southern Heaven Demon Empress ultimately headed, and what does she intend to do in Yunnan?",
    "Will the Nanman Beast Palace, North Sea Ice Palace, Yangtze River Channel League, and Green Forest Alliance support, ignore, or oppose the New Murim Alliance?",
    "Who is the rightful owner of the sword Sama Pyo was ordered to return?"
  ],
  "safe_through": 515,
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
| 진위경    | **Jin Wikyung**    |
| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 청풍     | **Cheongpung**     |
| 법왕     | **Dharma King**               | Hong Dao       |
| 소림     | **Shaolin**                      |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 사숙     | **Martial Uncle**                            |
| 은인     | **Benefactor**                               |
| 시스템              | **System**                     |
| 레벨               | **Level**                      |
| 경험치              | **EXP**                        |
| 보상               | **Reward**                     |
| 하남     | **Henan**              |
| 노부      | **this old man / I**                                            |
| 소협      | **Young Hero**                                                  |
| 대사      | **Master** for a senior Buddhist monk                           |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 궁기방 | **Gung Gibang** | Beggars' Sect Successor Beggar and finalist. |
| 정호 | **Jung Ho** | Middle-aged Shaolin martial monk leading the traveling group. |
| 문경 | **Mungyeong** | Young medical apprentice and newly introduced passenger. |
| 무명 | **Unnamed** | Dharma name given by Hong Dao; literally means having no name. |
| 화염신장 | **Flame Divine Palm** | Jopil's deadly palm technique, noted when Taekyung compares Jopil with Mukyung. |
| 가람중 | **Garam Middle School** | Middle school attended by Taekyung and Jihoon. |
| 소림사 | **Shaolin Temple** | Temple invoked in Chulwoo’s comparison of Baek Museong’s conduct. |
| 신성 | **Morning Star** | Term in the summons referring to the Master of Morning Star. |
| 계율원 | **Discipline Hall** | Shaolin disciplinary office that urges Hong Dao to return to a formal residence. |
| 천년독각사 | **Thousand-Year Poison Horned Snake** | Extremely venomous horned snake used to make Hong Dao's thirty-year-old liquor. |
| 계인 | **Buddhist precept seals** | Seals carved into the foreheads of Shaolin martial monks. |
| 노야 | **Old Master** | Taekyung's private address for Jeok Cheongang. |
| 미미 | **Mimi** | Worker at Honghwaru referenced in Taekyung's joke. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 일위도강 | **Single Reed Crossing the River** | A legendary river-crossing technique associated with Bodhidharma. |
| 진맥 | **take one's pulse** | Mungyeong's prior medical examination of Jeok. |
| 계율원주 | **Discipline Hall Master** | Shaolin office held by Jung Ho. |

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
| 무명 | 적천강 | junior_monk_to_legendary_martial_master | Great Hero Jeok Cheongang | formal-deferential | Identifies Jeok by the title Fire King and the honorific 대협. |
| 청풍 | 문경 | martial_companion_to_medical_apprentice | Medical Apprentice | cheerful-polite | Cheongpung addresses Mungyeong as 의생님 while asking him to greet the Tang Clan. |
| 혁무진 | 궁기방 | squad_companion_to_Beggars_Sect_successor | Young Hero Gung | formal-polite, then pointed | Uses 궁 소협 while asking about the culprit and challenging Gung’s insults. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 문경 | 적천강 | old_acquaintances | Fire King | familiar and grave | The figure bearing Mungyeong’s name greets Jeok Cheongang by his established epithet. |
| 궁기방 | 혁무진 | squad_companions | you; that lunatic | insulting-casual | Gung Gibang mocks Hyuk Mujin's injuries and calls him a lunatic for attacking the Third Fiend. |
| 궁기방 | 청풍 | martial_companions | Young Hero Cheongpung | formal-polite | Gung Gibang uses 청 소협 while asking why Cheongpung is at the temporary clinic. |
| 청풍 | 미미 | handler_to_companion_snake | Mimi | cheerful-commanding | Cheongpung repeatedly calls and commands the Thousand-Year Poison Horned Snake. |
| 적천강 | 문경 | overwhelming elder to old acquaintance | you / little punk | mocking and threatening | Mocks Mungyeong's expression and threatens to poke out his eyes. |
| 적천강 | 궁기방 | overwhelming_elder_to_younger_martial_artist | you | blunt and threatening | Jeok Cheongang rebukes Gung Gibang for speaking informally and orders him to lie down. |
| 궁기방 | 진위경 | martial_companion_to_family_head | Great Hero Jin | familiar and polite | Asks Jin Wikyung not to exclude the Beggars' Sect from the defense. |
| 문경 | 혁무진 | traveling_companion_to_traveling_companion | Martial Warrior Hyuk | formal-polite | Mungyeong asks Mujin to deliver water to Taekyung and lets Mujin receive the credit. |
| 혁무진 | 문경 | traveling_companion_to_traveling_companion | Mungyeong | casual-familiar | Mujin recognizes Mungyeong while reacting to Taekyung's dismantling work. |
| 진위경 | 문경 | Jin Family Lesser Family Head to medical apprentice | you | formal-polite | Asks whether Jin Taekyung will arrive soon. |
| 정호 | 무명 | Martial Nephew addressing his young Martial Uncle | Martial Uncle | formal-deferential | Jung Ho repeatedly addresses Unnamed as 사숙 after Unnamed emerges from Repentance Cave. |
| 무명 | 정호 | young Martial Uncle addressing his Martial Nephew | Martial Nephew Jung Ho | formal-polite and reassuring | Unnamed addresses Jung Ho as 정호 사질 while consoling him and discussing Hong Dao's will. |

## Listed compact profiles

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 515
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, the grandson and Disciple of Sword Saint Mae Jonghak, and a Supreme Peak martial master known as the Huashan Divine Dragon.
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, a deep love of martial arts, competitive pride, unusual resistance to monster-induced Fear, and discomfort when someone copies his martial arts.
- **Voice:** Dreamy and hazy, with innocent, polite phrasing; he has begun imitating Taekyung's profanity.
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions while Taekyung is his only true martial rival; Tang Sadok has temporarily entrusted Mimi to him.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 515
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Gung Gibang.md

# Gung Gibang (궁기방)

- **Safe through:** Chapter 510
- **Aliases:** Successor Beggar, Beggar Prince, pure-blooded beggar, ultimate beggar
- **Role:** Gung Gibang is the Beggars' Sect Successor Beggar and a unique eight-knot disciple.
- **Personality:** Vulgar, aggressive, and quick-tempered.
- **Voice:** Blunt, profane, and vividly threatening.
- **Relationships:** Gung Gibang is a rival finalist alongside Baek Woo and Zhuge Gyun who trades insults with Taekyung, uses Beggars’ Sect intelligence to investigate Tang Taesang’s murder and Dark Heaven’s Hubei forces, and has now found a trace of Honglan.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 508
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers and Vice Squad Leader of the Jin Dragon Squad.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 515
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, and Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Jin Wikyung.md

# Jin Wikyung (진위경)

- **Safe through:** Chapter 505
- **Aliases:** Junzi Sword
- **Role:** Jin Wikyung is the thirty-six-year-old Lesser Family Head and future Family Head of the Jin Family of Taiyuan, the Alliance Leader who unified Shanxi Murim and Shanxi Province's foremost landowner and magnate.
- **Personality:** Calm, authoritative, and politically capable in public; protective and affectionate toward Taekyung beneath a stern mask. Takes responsibility for his people, acts decisively under pressure, and prioritizes family survival.
- **Voice:** Restrained, formal, and commanding with subordinates; openly affectionate, proud, and occasionally exuberant with Taekyung.
- **Relationships:** Jin Wikyung is Taekyung's eldest brother and future Family Head who protects and mentors him, commands Wipeng and the Jin Family's forces, has worked with Jeok Cheongang, and maintains a political connection with Hongcheon, Prince Shangshan's hidden loyal retainer; Jin Mukyung is his younger brother and a potential successor alongside Taekyung.

### Jung Ho.md

# Jung Ho (정호)

- **Safe through:** Chapter 515
- **Aliases:** None
- **Role:** Middle-aged Shaolin martial monk and Master of Shaolin's Discipline Hall who leads the traveling group and wields a Zen staff hung with prayer beads.
- **Personality:** Humble, observant, principled, and concerned with the safety of commoners.
- **Voice:** Formal, restrained, and admonitory, with Buddhist phrasing.
- **Relationships:** Unnamed is his young Martial Uncle; he leads the Shaolin monks traveling with him and addresses Sama Pyo as a Benefactor while demanding accountability.

### Mungyeong.md

# Mungyeong (문경)

- **Safe through:** Chapter 510
- **Aliases:** Killing Ghost
- **Role:** Mungyeong is the legendary physician known as the former Divine Physician and Slaughter Saint, a Returned to Youth Supreme Peak master and the greatest assassin in history who passed the Divine Physician title to his Disciple.
- **Personality:** Compassionate, resolute, resourceful, and calm under extreme pressure.
- **Voice:** His Mungyeong persona is timid, deferential, and cheerful, while his Slaughter Saint voice is dry, impassive, and blunt.
- **Relationships:** Dong Feng is his Disciple, Jeok Cheongang is an old acquaintance whom Mungyeong helped break free of his Heart Demon, Mungyeong was asked to look after and instruct Jin Taekyung after testing his basics, and Mu Song plus five Water Dragon Stronghold subordinates now know he is an exceptionally powerful master but not that he is the Slaughter Saint.

### Unnamed.md

# Unnamed (무명)

- **Safe through:** Chapter 515
- **Aliases:** None
- **Role:** Young Shaolin monk and practical Disciple of the late Hong Dao; a Peak master who has achieved enlightenment after three months of treatment and training in Repentance Cave and is Jung Ho's young Martial Uncle.
- **Personality:** Naturally timid and introverted, but unable to control himself once angered.
- **Voice:** Timid, deferential, and polite, punctuated by Buddhist invocations.
- **Relationships:** Hong Dao was his Master; Jung Ho is his Martial Nephew; he carries Hong Dao's will and recognizes the Morning Star whom Hong Dao intended him to find.

## Korean source

```text
＃516화



목적지가 가까워질수록 몇 배로 힘들어지는 것은 인간의 본능이고, 열흘 밤낮 동안 혹사한 몸뚱어리는 더 이상 쥐어 짜낼 힘조차 남아 있지 않았다.

‘아부지, 지금 갑니다.’

간만의 부자 상봉을 이렇게 하게 되나. 발버둥 치던 팔다리에 힘이 빠져나가던 그 순간이었다.

덥석!

서서히 흐려지던 눈앞이 또렷해졌다.

내 손목을 굳게 틀어쥔 누군가의 손. 물이 하도 들어가는 바람에 먹먹해진 귓가로 한 사람의 목소리가 파고들었다.

“노부보다 먼저 갈 생각을 하다니. 이런 고얀 놈을 보았나.”

도대체 언제 여기까지 온 걸까. 나루터로부터 거리를 순식간에 좁혀 다가온 적천강이 나를 내려다보며 웃고 있었다.

비로소 그의 얼굴을 마주하자 전신의 긴장이 탁 풀렸다.

“……어흐.”

참았던 숨을 토해 내는 내 모습에 적천강의 웃음이 짙어졌다.

“그래도 숨은 붙어 있구나.”

“신기하네요. 저 아직 살아 있습니까?”

“이놈 보게. 오냐, 살아 있다.”

“그럼 보지만 말고 올려 주십쇼. 진짜 골로 갈 것 같은데.”

“엄살하고는. 아직 백 년은 이르다.”

촤아아악. 투둑.

강한 힘이 내 손목을 붙잡고 그대로 들어 올렸다.

퉁퉁 불어 있던 몸뚱어리에 달라붙어 있던 수초(水草)가 강물과 함께 쏟아져 내린다.

“보이느냐?”

“누구요, 하느님?”

“너를 기다리는 사람들 말이다.”

나는 기진맥진한 채 눈을 깜빡였다. 저 멀리 나루터에 구름처럼 모여든 군중과, 몇몇 익숙한 얼굴들이 빠르게 가까워지고 있었다.

두 팔을 붕붕 휘두르고 있는 청풍, 눈을 동그랗게 뜬 궁기방과 혁무진. 거의 통곡하는 중인 진위경.

그리고…… 조용히 이쪽을 바라보고 있는 문경.

- 하남(下南)에 온 것을 환영한다.

짤막한 전음을 마지막으로, 나를 끌어안은 적천강의 발이 지면에 닿았다.

동시에 귓가를 파고드는 맑은 종소리가 있었다.

띠링. 띠링. 띠링.



- [가짜 무림인 2단계]를 성공적으로 완료했습니다!

- 희귀한 업적, [일위도강一葦渡江]을 달성하셨습니다!

- 놀라운 끈기와 노력을 보여 준 대가로, 그에 합당한 보상이 주어질 것입니다!

- [공력]의 수발이 한층 자유로워집니다! 무공의 위력과 효율이 상승합니다!

- 모든 능력치가 소폭 상승합니다!

- 보너스 포인트 50을 획득했습니다!

- 막대한 경험치를 획득했습니다!

- 레벨 업!



연이어 울리는 시스템 알림. 그리고 허공을 가득 메운 홀로그램 창.

나는 레벨 업 메시지와 함께 가벼워지는 몸을 느꼈다. 동시에 파도처럼 밀려드는 졸음도.

“……노야.”

“응?”

“저, 깨우지 마세요.”

그 한마디를 마지막으로, 무거워진 눈꺼풀과 함께 찾아온 수마(睡魔)가 나를 덮쳤다.



* * *



여기가 어디지?

눈을 뜨자마자 처음으로 든 생각이다.

나는 천천히 눈을 깜빡이며 주위를 둘러보았다. 칠흑 같은 어둠에 잠겨 있는 사방.

점차 어둠에 익숙해지자 비로소 이곳이 어디인지 알 수 있었다.

‘늪.’

그래, 이곳은 늪이다.

인간의 것인지, 짐승의 것인지 모를 백골이 곳곳에 널려 있었고 헛구역질이 날 만큼 끔찍한 악취가 풍겼다.

더욱 지랄 맞은 사실은, 이런 와중에도 내 몸이 제멋대로 움직이고 있다는 거다.

철벅.

신발조차 신지 않은 맨발이 끈적한 진흙을 밟았다. 멈추기 위해 안간힘을 써 보지만 내 몸은 이미 통제를 벗어났다.

한 걸음, 또 한 걸음.

몸이 서서히 늪 깊숙이 가라앉던 그때였다.

솨아아아아.

어디선가 불어온 바람에, 늪지대에 숲을 이루고 있던 앙상한 나무들이 몸을 떨었다.

그리고 짙은 어둠 너머에서 정체를 알 수 없는 붉은빛이 솟구쳤다.

‘……저건.’

불꽃이 아니다. 그것은 차라리 누군가의 눈동자에 가까웠다.

한 줌의 온기조차 느껴지지 않는 소름 끼치는 안광(眼光)이 나를 응시하고 있었다. 마치 올 수 있으면 와 보라는 듯이.

흔한 영화나 소설 속 주인공이라면 안간힘을 쓰며 기어가겠지만…….

‘니가 와, 새꺄.’

클리셰 좆 까.

이미 사이즈 파악을 끝낸 후다.

척 보아하니 요즘 고생을 하도 해서 악몽을 꾸고 있는 모양인데, 굳이 장단 맞춰 줄 필요는 없지.

평범한 사람이었다면 저 붉은 안광을 마주한 순간 오줌이 마려웠겠지만, 나는 화염신장이 마려운 사람이다.

단지 아주 약간, 사소한 문제가 있다면……

철벅. 철벅.

‘아, 시벌.’

내 의지와는 상관없이 몸은 계속해서 나아가고 있다는 점이다.

늪 깊숙이 가라앉은 하반신으로 자맥질하듯 천천히. 그리고 꾸준하게.

하지만 나는 알고 있었다. 계속해서 나아간다 해도 영영 닿을 수 없다는 것을.

저 안광의 주인을 만나기도 전에 내 몸이 늪 깊숙한 곳으로 가라앉을 것이라는 사실을.

‘그래, 빨리 끝내자.’

그렇게 반쯤 체념한 그 순간이었다.

콰득!

‘흡!’

목을 조여 오는 정체불명의 무언가.

부릅뜬 눈동자에 매끄러운 비늘로 뒤덮인 거대한 몸뚱어리가 보인다. 낮게 쉭쉭거리는 울음소리가 귓가를 파고들었다.

‘뱀?’

아니, 뱀이라고 하기에는 너무 크니 구렁이라고 해야 맞겠다.

굵은 몸뚱어리가 내 목을 시작으로 두 팔까지 칭칭 묶어 버렸다.

‘흐읍.’

젠장. 요즘은 꿈도 그래픽 패치를 하나. 왜 이렇게 생생해?

썩은 진흙은 이미 목까지 차올랐고, 콧속을 파고드는 악취에 헛구역질이 절로 나온다.

옴짝달싹하지 못하고 늪으로 가라앉던 나는 붉은 안광과 눈이 마주쳤다.

‘……!’

등골을 타고 솟구치는 서늘한 기운.

순간 정신이 번쩍 들 만큼 선명한 두려움이 엄습한다. 이게, 이런 게 단순한 악몽일 리 없다.

동시에 소름 끼치는 위화감이 나를 감쌌다.

‘이 느낌…… 왠지 모르게 익숙해.’

그렇다면 도대체 언제, 어디에서였을까. 기억해 내기 싫은 기억을 헤집던 내가 전신을 부르르 떤 그 순간.

파앗!

어디선가, 눈부시도록 환한 빛이 폭발했다.

불길하리만치 음습한 기운을 흩뿌리던 붉은 안광이, 사방을 집어삼켰던 어둠마저 깨져 나가고 서늘한 한기가 사라진다.

전신을 감싸는 따사로운 온기를 느끼며, 나는 눈앞까지 다가온 빛무리를 향해 손을 뻗었다.

덥석!

……응?

온갖 생각이 뇌리를 스쳤다.

빛이 왜 덥석 잡혀. 그리고 왜 이렇게 촉감이 좋아. 분명히 꿈에서 깼는데 왜 아직도 만져져.

문질문질.

진짜 뭐지, 이거.

잠시 고민하던 나는 슬쩍 감았던 눈을 떴다.

환한 빛, 아니 반질반질한 누군가의 머리가 그곳에 있었다.

이마에는 승려들이 찍는 계인(契印)이 보였다.

“크리링?”

크리링, 아니 난생처음 보는 승려가 떨떠름한 표정으로 입을 열었다.

“드디어 깨어나셨군요, 진 시주.”

“실례지만 누구……?”

“빈승은 정호라고 합니다.”

정호가 누구야.

잠깐 고민하던 나는 잔뜩 잠긴 목소리로 더듬더듬 물었다.

“혹시 가람중학교 3학년 6반 박정호……?”

“예?”

“너 언제 스님 됐냐.”

“족히 사십 년 정도…… 아니, 잠깐 제 말을 들어 주시겠습니까. 시주.”

“어, 그러고 보니까 이 새끼. 신부 할 거라고 하더니 언제 갈아탔대. 배교자네, 배교자. 순복음교회 십자군한테 얻어맞았나 얼굴 폭삭 늙은 것 봐라. 어디 절에 취직했어?”

간만에 만난 동창 녀석이 반쯤 체념한 표정으로 대답했다.

“……소림에서 계율원주를 맡고 있지요.”

“소림?”

“예, 소림. 소림사를 말씀드린 겁니다.”

“잠깐 있어 봐, 소림사면.”

엇. 시벌. 뭐야 이거.

그제야 정신이 확 든다. 황급히 고개를 흔들어 잠을 털어낸 나는 조심스럽게 입을 열었다.

“아, 죄송합니다. 순간 잠이 덜 깨서.”

“이해합니다.”

전혀 이해가 안 된다는 표정으로 대답한 중년의 승려, 정호가 말을 이었다.

“이제 그만 빈승의 머리에서 손을 좀 떼 주시겠습니까. 아까부터 계속 만지고 계시는데…….”

“어이쿠. 죄송합니다.”

“괜찮습니다.”

이 양반, 표정이랑 말이 전혀 매치가 안 된다.

마음 같아선 한소리 하고 싶은데, 그래도 받은 도움이 있어서 참는다는 기색이 역력했다.

‘그런데 왜 눈 뜨자마자 소림사 계율원주가 옆에 있지.’

그제야 이상함을 느낀 나는 주위를 둘러보며 상황을 파악했다.

한 번에 열 명도 묵을 수 있을 만큼 큰 방. 반쯤 열린 창밖으로 스며들어온 햇빛이 정호의 이마를 받아 번쩍거리고, 익숙한 얼굴들은…… 바로 내 주위에 널려 있다.

‘꿈은 꿈인데, 절반은 현실이었구만.’

어쩐지 꿈이라고 하기에는 너무 생생하다고 했다.

한숨을 푹 내쉰 나는 가장 먼저 발치에 웅크린 채 잠들어 있는 덩어리를 걷어찼다.

퍽!

“핫. 오늘 점심은 고기만두!”

“…….”

아니, 저 기상 구호 뭔데.

갑작스러운 충격으로 벌떡 일어난 청풍이 졸린 눈으로 입을 열었다.

“아, 은인. 안녕히 주무셨어요?”

“주무시긴 했는데, 안녕하진 못했어.”

“왜요? 그럼 더 주무세요.”

“……장난해? 헛소리 그만하고 이놈이나 얼른 떼어 내.”

“앗, 미미야! 이리 와!”

뒤늦게 내 목을 휘감고 있는 애완 뱀을 발견한 청풍이 외치자, 두꺼운 몸통이 스르륵 가슴을 타고 내려간다.

아니, 잠깐. 두꺼운 몸통?

나는 흡사 구렁이가 되어있는 천년독각사의 모습에 입을 딱 벌렸다.

“청 소협. 그놈 원래 그렇게 컸었어?”

“아뇨. 요즘 부쩍 자랐어요. 한창 클 때잖아요.”

“몇 살인데.”

“당씨 할아버지 말씀으로는 아직 백 살도 안 됐대요.”

“……어, 그래.”

“이러다가 저보다 커질지도 몰라요. 아, 나도 빨리 더 커야 하는데.”

“이미 다 컸어. 기다려 봤자 더 안 자라.”

“아니에요. 미미도 나이 먹을수록 더 커지는걸요. 저도 계속 자랄 거예요.”

“……?”

그럼 시바, 적천강이나 문경은 키가 최소 삼 장은 넘어야 하는 거 아니냐.

착잡하게 청풍을 바라보던 나는 설득을 포기했다. 대신 바로 옆에서 끔찍한 악취를 풍기고 있는 주둥이를 후려쳤다.

빡!

“어억!”

“내가 이 닦고 자랬지. 이 거지 새끼는 아가리가 아주 그냥 늪이야, 늪.”

“흐어. 흐어어.”

강제 기상한 궁기방이 촉촉하게 젖은 눈동자로 나를 노려봤다.

“왜 맨날 나만 갖고 그러나!”

“너만 갖고 그러진 않지. 이놈도 똑같이 처리할 거니까.”

사람은 평등해야 하는 법.

잠시 후, 내 한쪽 다리를 부여잡은 채 쿨쿨 잠들어 있던 혁무진에게도 비슷한 운명이 찾아왔다.

빠악!

“악! 왜 저만 갖고 그러십니까!”

“너희 대사 정해 놨냐? 아니면 어릴 적 헤어진 형제, 뭐 그런 거 아냐?”

“저만 때리지 말고 궁 소협도, 어. 깼네.”

“……후, 웬수 같은 놈들.”

나는 작게 투덜거리는 혁무진을 뻥 걷어차 침상 아래로 떨어트렸다.

이놈들 때문에 평소에는 잘 꾸지도 않는 꿈까지 꿨다. 그것도 찝찝하기 짝이 없는 악몽을.

‘그 안광.’

다시 떠올려 봐도 섬뜩한 붉은 빛.

꿈속에서 느꼈던 정체 모를 위화감을 다시금 되짚어 보려던 그때. 소란을 틈타 잠시 자리를 비웠던 정호가 문을 열고 들어왔다.

“진 시주. 잠시 시간을 내어 주실 수 있겠습니까?”

“아, 예.”

정호의 말에 나는 자세를 고쳐 앉았다.

남의 머리를 볼링공이라도 되는 것처럼 문질러 댔으니 없는 시간이라도 만들어야 한다.

“말씀하십시오. 스님.”

“다름이 아니라, 빈승의 사숙께서 시주를 뵙고 싶어 하십니다.”

“사숙이요? 혹시 지금 밖에서 기다리고 계신 분입니까?”

“예. 그렇습니다. 오랜만에 대화를 나누고 싶으시다고…….”

어쩐지. 느껴지는 기척이 왜 두 개인가 했다.

그나저나 정호의 사숙이라면 소림의 고승(高僧)인 건 확실한데, 오랜만에 대화를 나누고 싶다니.

‘누구지? 저렇게 말하는 것 보면 틀림없이 구면일 텐데.’

소림에 나와 그 정도 인연을 쌓은 사람이 법왕 말고 또 있던가.

의아함도 잠시, 나는 흔쾌히 고개를 끄덕였다.

“그러시죠.”

그리고 내 말이 떨어지기가 무섭게, 문을 열고 들어오는 한 사람의 모습을 확인한 나는 미간을 좁혔다.

“실례지만 누구…….”

호리호리한 체구에, 드러난 피부 위로는 흉터가 빼곡하다. 난생처음 보는 인상파 승려의 입술 사이로 거친 목소리가 흘러나왔다.

“다행입니다. 비록 하늘을 흐려졌으나, 북쪽에서 떠오른 신성(新聲)은 더욱 밝아진 듯하군요.”

“……!”

“잘 지내셨습니까. 시주.”

그제야 깨달았다. 눈앞의 승려가 누구인지.

나는 너무나도 달라진 분위기와 겉모습에 쉽게 떠올리지 못했던 그의 이름을 불렀다.

“무명(無名).”
```

## Final English reading copy

```markdown
# Chapter 516

It was human nature for things to feel several times harder the closer one got to one's destination. After ten days and nights of pushing my body to its limits, I had not even a shred of strength left to squeeze out.

*Dad, I'm coming.*

Was this really how a father and son were going to reunite after so long? That was the moment the strength drained from my flailing limbs.

Grab!

My vision, which had been slowly fading, snapped back into focus.

Someone's hand had a firm grip on my wrist. Through my waterlogged ears, a voice forced its way in.

“Trying to get there before this old man? What a rotten little punk.”

When had he gotten here? Jeok Cheongang had closed the distance from the ferry landing in an instant. He was looking down at me with a grin.

The moment I finally saw his face, all the tension left my body.

“…Hrk.”

As I exhaled the breath I had been holding, Jeok Cheongang's grin deepened.

“You're still breathing, at least.”

“That's amazing. Am I still alive?”

“Listen to this fool. Yes, you're alive.”

“Then don't just stand there and look at me. Pull me up. I think I'm actually about to die.”

“Such an exaggeration. You're still a hundred years too young to die.”

Whoosh! Drip.

A powerful hand gripped my wrist and hauled me straight up.

River water and the plants clinging to my bloated body came pouring off me.

“Can you see?”

“Who? God?”

“The people waiting for you.”

Exhausted, I blinked. The crowd gathered like a bank of clouds at the distant ferry landing was rapidly drawing closer, and I could make out several familiar faces among them.

Cheongpung, waving both arms frantically. Gung Gibang and Hyuk Mujin, their eyes opened wide. Jin Wikyung, who was practically bawling his eyes out.

And… Mungyeong, quietly watching us.

—Welcome to Henan.

After sending that brief Sound Transmission, Jeok Cheongang's feet touched the ground while he held me in his arms.

At the same time, a clear ringing sound pierced my ears.

Ding. Ding. Ding.

> **System**
>
> **Fake Murim Practitioner, Stage 2** completed successfully!
>
> You have achieved the rare achievement **Single Reed Crossing the River**!
>
> As a reward for demonstrating remarkable persistence and effort, you will receive a fitting reward!
>
> Your control over **internal energy** has become freer! The power and efficiency of your martial arts have increased!
>
> All attributes have increased slightly!
>
> You have acquired 50 bonus points!
>
> You have acquired a massive amount of EXP!
>
> **Level Up!**

System notifications rang out one after another. Holographic windows filled the air.

Along with the Level Up message, I felt my body becoming lighter. At the same time, a wave of sleepiness came crashing over me.

“…Old Master.”

“Hm?”

“Don't wake me.”

That was the last thing I said before the heavy lids of my eyes closed and the demon of sleep swallowed me whole.



* * *



Where am I?

That was my first thought when I opened my eyes.

I slowly blinked and looked around. Every direction was drowned in pitch-black darkness.

As my eyes gradually adjusted, I finally realized where I was.

*A swamp.*

Yes, this was a swamp.

White bones of uncertain origin—human or beast—were scattered everywhere, and a horrific stench filled the air, strong enough to make me gag.

Even worse was the fact that my body was moving on its own.

Splosh.

My bare foot, without even a shoe on it, stepped into the sticky mud. I struggled with all my might to stop, but my body had already escaped my control.

One step. Then another.

That was when my body began to slowly sink deeper into the swamp.

Whoooosh.

A wind blew in from somewhere, making the skeletal trees that formed a forest throughout the swamp shudder.

Then, beyond the thick darkness, an unidentified red light surged upward.

*…What is that?*

It wasn't a flame. It looked more like the glow of someone's eyes.

A chilling gaze, devoid of even the slightest warmth, stared at me. As though it were saying, *If you can come, then come.*

If this were an ordinary protagonist from a movie or novel, he would struggle and crawl toward it…

*You come here, asshole.*

*Fuck the cliché.*

I had already figured out what I was dealing with.

Judging by appearances, I was having a nightmare after suffering through too much lately. There was no reason to play along.

An ordinary person would have felt the urge to piss himself the moment he saw those red eyes, but I was the kind of person who felt the urge to use Flame Divine Palm.

There was only one small, insignificant problem…

Splosh. Splosh.

*Ah, fuck.*

My body kept moving forward regardless of my will.

Slowly, as though swimming with the lower half of my body already sunk deep into the swamp. And steadily.

But I knew. No matter how long I continued forward, I would never reach it.

I would sink into the depths of the swamp before I ever met the owner of that gaze.

*Fine. Let's get this over with.*

That was when I had almost resigned myself to my fate.

Crack!

*Gasp!*

Something unidentified tightened around my neck.

My eyes flew open, revealing a gigantic body covered in smooth scales. A low, hissing growl pierced my ears.

*A snake?*

No, it was far too large to be called a snake. A python would be more accurate.

Its thick body wrapped tightly around my neck, then bound both my arms.

*Hngh.*

Damn it. Had dreams gotten a graphics patch lately? Why was this so vivid?

Rotten mud had already risen to my neck, and the stench forcing its way into my nostrils made me gag uncontrollably.

Unable to move as I sank into the swamp, I met the red gaze.

*…!*

A cold sensation surged up my spine.

A vivid fear, sharp enough to jolt my mind fully awake, swept over me. This couldn't be an ordinary nightmare. It couldn't be.

At the same time, a horrifying sense of incongruity enveloped me.

*This feeling… Why does it seem familiar?*

If so, when and where had I felt it? I dug through memories I did not want to recall, and that was when my whole body began to tremble.

Flash!

From somewhere, a blindingly bright light exploded.

The red gaze that had been spreading an ominously oppressive energy disappeared. Even the darkness that had swallowed everything around me shattered, and the chilly cold vanished.

Feeling a warm radiance envelop my entire body, I reached toward the mass of light that had come right up to my face.

Grab!

…Huh?

All kinds of thoughts raced through my mind.

Why could I grab the light? Why did it feel so good? I had definitely woken up from the dream, so why could I still feel it?

Rub, rub.

What the hell was this?

After thinking for a moment, I opened my eyes, which I had closed slightly.

There was a bright light—or rather, someone's shiny, smooth head.

A Buddhist precept seal was visible on his forehead.

“Krillin?”

The monk, whom I had never seen before—not Krillin—opened his mouth with an awkward expression.

“You have finally awakened, Benefactor Jin.”

“Excuse me, but who…?”

“This humble monk is Jung Ho.”

Who was Jung Ho?

After thinking briefly, I asked in a hoarse, halting voice.

“Were you perhaps Park Jung Ho from Class 6, Grade 3 at Garam Middle School…?”

“Pardon?”

“When did you become a monk?”

“A good forty years, at least… No, wait. Could you please listen to me, Benefactor?”

“Oh, now that I think about it, you bastard. Didn't you say you were going to become a priest? When did you switch? Apostate. Apostate. Did the Full Gospel Church Crusaders beat you up? Look how old your face has gotten. What temple hired you?”

My old classmate answered with an expression of half resignation.

“…I am Shaolin's Discipline Hall Master.”

“Shaolin?”

“Yes, Shaolin. I mean Shaolin Temple.”

“Wait a second. If it's Shaolin Temple, then…”

Oh, shit. What was this?

Only then did my mind fully clear. I hurriedly shook my head to dispel the sleep and cautiously opened my mouth.

“Ah, I'm sorry. I hadn't fully woken up yet.”

“I understand.”

Jung Ho, the middle-aged monk, replied with an expression that showed he did not understand at all, then continued.

“Could you please remove your hand from this humble monk's head now? You have been touching it for a while…”

“Whoops. Sorry.”

“It is all right.”

This man's expression and words did not match at all.

He clearly wanted to give me a piece of his mind, but was holding back because he owed me for the help he'd received.

*But why was Shaolin's Discipline Hall Master beside me the moment I opened my eyes?*

Only then did I sense that something was strange. I looked around and tried to understand the situation.

It was a large room, big enough for ten people to stay in at once. Sunlight streamed in through the half-open window and gleamed off Jung Ho's forehead, while familiar faces…

They were scattered all around me.

*So it was a dream, but half of it was reality.*

No wonder it had seemed too vivid to be a dream.

I let out a deep sigh, then first kicked the lump curled up asleep at my feet.

Thump!

“Ah! Meat dumplings for lunch today!”

“…”

What the hell was that wake-up call?

Cheongpung sprang awake from the sudden impact and opened his sleepy eyes.

“Ah, Benefactor. Did you sleep well?”

“I slept, but not well.”

“Why not? Then sleep some more.”

“…Are you kidding me? Stop babbling and get this thing off me.”

“Oh! Mimi! Come here!”

Only then did Cheongpung notice the pet snake coiled around my neck. At his shout, the thick body slowly slid down across my chest.

Wait a second. A thick body?

I stared open-mouthed at the Thousand-Year Poison Horned Snake, which looked practically like a python now.

“Young Hero Cheongpung. Was it always that big?”

“No. It has grown a lot lately. It's right in the middle of its growth period.”

“How old is it?”

“Grandpa Tang says it isn't even a hundred years old yet.”

“…Oh. I see.”

“It might end up bigger than me. Ah, I need to grow more quickly too.”

“You're already fully grown. Waiting won't make you any taller.”

“No, I haven't. Mimi will keep getting bigger as she gets older. I'll keep growing too.”

“…?”

Then damn it, shouldn't Jeok Cheongang and Mungyeong be at least three zhang tall?

I gave up trying to reason with Cheongpung and looked at him with a troubled expression. Instead, I smacked the mouth right beside me, which was giving off a horrific stench.

Smack!

“Urgh!”

“I told you to brush your teeth before bed. You damn beggar, your mouth is a swamp. A goddamn swamp.”

“Guh. Guhhh.”

Gung Gibang, forcibly awakened, glared at me with his moist eyes.

“Why do you always pick on me!”

“I don't only pick on you. I'm going to deal with this guy the exact same way.”

People had to be treated equally.

A little while later, Hyuk Mujin, who had been sleeping soundly while clutching one of my legs, met a similar fate.

Whack!

“Argh! Why do you always pick on me!”

“Did you two rehearse those lines? Or are you long-lost brothers or something?”

“Don't just hit me. Young Hero Gung too—oh, he's awake.”

“…Hah. You hateful bastards.”

I kicked Hyuk Mujin hard enough to send him tumbling beneath the bed while he muttered under his breath.

Because of these idiots, I'd even had a dream when I hardly ever dreamed at all—and an incredibly unsettling nightmare at that.

*That gaze.*

Even thinking back on it, that red light sent chills through me.

I was just about to retrace the strange sense of incongruity I had felt in the dream when Jung Ho, who had slipped away amid the commotion, opened the door and entered.

“Benefactor Jin. Could you spare me a moment?”

“Ah, yes.”

At Jung Ho's words, I straightened my posture.

I had rubbed his head as though it were a bowling ball, so I had to make time even if I did not have any.

“Please, speak, Monk.”

“The Martial Uncle of this humble monk wishes to see you, Benefactor.”

“Your Martial Uncle? Is he the person waiting outside right now?”

“Yes. He wishes to speak with you after such a long time…”

That explained it. I'd been wondering why I could sense two presences.

In any case, if Jung Ho's Martial Uncle was a senior monk of Shaolin, that much was certain. But he wanted to speak with me after such a long time?

*Who could it be? Judging by the way he put it, it has to be someone I already know.*

Besides the Dharma King, was there anyone at Shaolin with whom I had formed that kind of connection?

My puzzlement lasted only a moment before I readily nodded.

“Of course.”

And no sooner had the words left my mouth than I saw someone entering through the door and narrowed my eyes.

“Excuse me, but who…?”

He had a slender build, and every inch of exposed skin was covered in scars. A rough voice came from the lips of the fierce-looking monk I had never seen before.

“I am glad. Though the heavens have grown dim, the Morning Star that rose in the north seems to shine even brighter.”

“…!”

“How have you been, Benefactor?”

Only then did I realize who the monk before me was.

His atmosphere and appearance had changed so completely that I could not bring his name to mind right away. Then I called it out.

“Unnamed.”
```

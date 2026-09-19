<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0508.txt",
      "sha256": "bdc52ad3ede19ac63c44fd1abb38beaaf1a6bd62cbe6f794195bab50189e00c2",
      "bytes": 12958
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "5469bc3b663dcff9c445e461e88c3ab67d2393dd07110f28cbed988fcc1c62e1",
      "bytes": 4146
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "a3bc45fbe25041a4749fe476101066b0fa1f0cd543fe5eecf64860d2707f464c",
      "bytes": 162560
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "2067cf645909b89f21c787b1fd9120b291c12f1230fbb9fa501c63f3ee4caae0",
      "bytes": 1006
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "655e5331f688593dcb706b2dc411cd3ddf85d43c7223de2e87f530d8cf5f84ad",
      "bytes": 553
    },
    {
      "path": "characters/Human Butcher.md",
      "sha256": "24fd865a5635777f890a64c955e1a0cdcd89813cfe1120eea8f19af1b5370057",
      "bytes": 667
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "3314dce9e082f801a44101f48a677ffd8137d16fa22c9009b5f5737bff1047e5",
      "bytes": 1108
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "d21cc88a1acf1b6f4103872a16dd265f2085ae6a9a42880d3314fd947a4b2c47",
      "bytes": 1630
    },
    {
      "path": "characters/Mu Song.md",
      "sha256": "719a85b56d6b32bd4b31c7b3c80c6f17732ac6e9e9041c604fc506f265fde4f8",
      "bytes": 985
    },
    {
      "path": "characters/Mungyeong.md",
      "sha256": "edf2ea45ff66e17f815ffeb7d31423d4f040cca2d6ec25bd304cf512ab180bec",
      "bytes": 842
    },
    {
      "path": "characters/Pill Physician.md",
      "sha256": "a4d42abf78d3cba971f7a209e3822235af58f816ca9a062dff13710bbfb7c745",
      "bytes": 554
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "d55e1b559aab842913d6859ee4f86aff71a3a23ad89553d949f27b82a0965ae8",
      "bytes": 154523
    }
  ],
  "estimated_tokens": 12171
}
-->

# Durable State Update — Chapter 508

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 508. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 508. Profile updates may replace only one
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
  "chapter": 508,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 508,
    "continuity_sources": [508],
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
    "Mungyeong is the Slaughter Saint and former Divine Physician, a Returned to Youth Supreme Peak master whose assassin instincts remain formidable despite decades spent living as a medical apprentice.",
    "Zhuge Feng's Demon-Sealing Formation blocks all mana from the exposed Gate by drawing in natural qi, but whether it is permanent and repeatable remains unresolved.",
    "Jang Taebo is the Jin Family of Taiyuan's Master of Ironcraft Hall and is summoning renowned artisans to process the Water God Dragon's remains.",
    "War has begun and the New Murim Alliance is being formed at Mount Song; Taekyung believes Dark Heaven planned the Gate incident, while Jin Wikyung's Hubei arrangement was designed to create an opening among rival unorthodox factions.",
    "Around one hundred Level 5 Mutated Minnows, locally called Blood Fish, were captured in the Gate's entrance waterways; the remaining population is unknown, and the fish kill one another.",
    "The Southern Heaven Demon Empress is traveling toward Yunnan and expects to cause further deaths.",
    "Jin Mukyung remains secluded in the training hall after losing to Cheongpung, refusing to emerge until he achieves a great accomplishment.",
    "Jin Taekyung's party is traveling by ship along the Yangtze toward Xixia in southwestern Henan and will continue overland after leaving the river.",
    "Mu Song wants to aid the Murim Alliance, but the Seafaring King alone decides the Yangtze River Channel League's major matters; the League and Green Forest Alliance may become rear threats.",
    "The North Sea Ice Palace remains isolationist, while Jeok Cheongang believes the Nanman Beast Palace will probably support orthodox Murim because of its historical goodwill toward the Fire Gate Clan.",
    "The Wudang pursuit party has brought back remains attributed to the Killing Ghost, but their nature is neither beast nor human."
  ],
  "continuity_sources": [
    507,
    506
  ],
  "open_questions": [
    "Will the Demon-Sealing Formation remain effective permanently, and can equivalent formations be installed repeatedly if more Gates appear?",
    "What is the Lord of Heaven's identity, and how is he connected to the dangerous force Taekyung associates with his original world?",
    "Where is the Southern Heaven Demon Empress ultimately headed, and what does she intend to do in Yunnan?",
    "Will the Nanman Beast Palace, North Sea Ice Palace, Yangtze River Channel League, and Green Forest Alliance support, ignore, or oppose the New Murim Alliance?",
    "What is Mungyeong's true identity and what does he intend to do now that Mu Song may recognize him?"
  ],
  "safe_through": 507,
  "temporary_decisions": [
    "Render 새외무림 as Outer Murim, 새외 as Outer Lands, 북해빙궁 as North Sea Ice Palace, 야수묘왕 as Beast Miao King, and retain Nanman Beast Palace for 남만야수궁.",
    "Render 소뢰음사 as Small Thunderclap Temple, 광풍사 as Mad Wind Society, 포달랍궁 as Potala Palace, 오독문 as Five Poisons Sect, 독곡 as Poison Valley, 천축 as India, and 갠지스강 as Ganges River.",
    "Render 파사국 as Persia, 회교도 as Muslims, 영웅건 as hero headband, 대막 as great desert, 귀염권 as Ghost Flame Fist, and 장성 as Great Wall.",
    "Retain Energy-Dispersing Poison, Seven-Step Soul-Chasing Powder, Blindness Powder, Potent Paralysis Powder, Potent Soul-Bewitching Powder, Full-Body Paralysis, Poison Absorption, Detoxification, Poison Physician, Memory Fragment, Gate Conquest, Teleport, Magic, Black Wind Corps, Blood Fish, Mutated Minnow, Wa Kingdom, ninja, Zhejiang, sea of corpses and blood, and Old Master as established renderings.",
    "Retain innate qi, true-origin qi, heavenly patterns, acquired qi, Heart Demon, Returned to Youth, Demon-Sealing Formation, New Murim Alliance, Fire Gate Cavern, Martial Extremity Grand Unity Sword, and the other established glossary renderings."
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
| 해상왕    | **Seafaring King**            | Pa Ryun        |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 심법     | **cultivation technique**                        | Especially internal cultivation                       |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 운기조식   | **circulate one's qi**                           | Usually better as a verb than a proper-name technique |
| 생사결    | **life-and-death duel**                          | Explicitly lethal                                     |
| 가주     | **Family Head**                              |
| 제자     | **Disciple**                                 |
| 선배     | **Senior**                                   |
| 상태               | **Status**                     |
| 퀘스트              | **Quest**                      |
| 하남     | **Henan**              |
| 사천     | **Sichuan**            |
| 노부      | **this old man / I**                                            |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 무송 | **Mu Song** | Lord of Water Dragon Stronghold and disciple of the Seafaring King. |
| 문경 | **Mungyeong** | Young medical apprentice and newly introduced passenger. |
| 환의 | **Pill Physician** | Title of the current Family Head of the Seongsu Jang Family. |
| 송이 | **Song-i** | Short form used for Song Song; Taekyung's love interest. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 반박귀진 | **Returning to Simplicity** | Supreme Peak technique or phenomenon used by Jeok Cheongang. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 노환 | **infirmities of old age** | Jeok Cheongang's age-related illness. |
| 반로환동 | **Returned to Youth** | Possible explanation for an apparently young Supreme Peak master. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 수룡채 | **Water Dragon Stronghold** | Major river stronghold belonging to the Yangtze River Channel League. |
| 장강 | **Yangtze** | The river controlled by the Yangtze River Channel League. |
| 의생 | **medical apprentice** | Mungyeong's occupation. |
| 등평도수 | **Rising on Duckweed, Crossing Water** | Comparable movement feat for walking across water. |
| 이무기 | **imugi** | Legendary serpent mentioned as the only comparable creature to a Thousand-Year Poison Horned Snake. |
| 동정호 | **Dongting Lake** | Lake under which Dangyang and Honghu Strongholds operated. |
| 사천혈사 | **Sichuan Blood Tragedy** | Earlier incident in which Taekyung witnessed the strange formation. |
| 쾌조선 | **swift ship** | Fast vessel operated by the Yangtze River Channel League. |
| 제갈 | **Zhuge** | Surname used for Sir Zhuge. |
| 호법 | **stand guard** | Mungyeong offers to protect Jeok during cultivation. |
| 촌각 | **moments** | Short intervals disappearing from Jeok's day. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 청풍 | 혁무진 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung includes Mujin among his 은인들 after receiving the skewers. |
| 혁무진 | 청풍 | martial artist to young master | Young Master | formal-deferential | Mujin uses 공자께서는 when asking why Cheongpung descended from the mountain. |
| 적천강 | 청풍 | overwhelming_elder_to_young_martial_artist | you / little punk | blunt, amused, and threatening | Jeok Cheongang uses 네, 이놈, and related blunt forms while testing Cheongpung. |
| 청풍 | 적천강 | young_martial_artist_to_overwhelming_elder | Grandpa Jeok | casual-familiar despite deference | Cheongpung uses 적 할아버지 while asking Jeok Cheongang to confirm Taekyung's condition; this is a familial form of address, not literal kinship. |
| 혁무진 | 적천강 | subordinate_to_overwhelming_elder | Great Hero Jeok | deferential and fearful | Mujin uses 적 대협 while reporting Jeok’s orders and Taekyung’s awakening. |
| 적천강 | 혁무진 | overwhelming_elder_to_junior_martial_artist | you stupid fool | blunt and mocking | Jeok calls Mujin a 멍청한 놈 after knocking him down during the attempted escape. |
| 문경 | 무송 | survivor_to_savior_and_authority | Great Hero Mu Song | formal-deferential | Mungyeong credits Mu Song with saving him and asks him to spare Hwang Tae-gu. |
| 무송 | 문경 | stronghold_lord_to_young_passenger | you | gruff-but-considerate | Mu Song offers Mungyeong the right to decide Hwang Tae-gu's fate. |
| 청풍 | 문경 | martial_companion_to_medical_apprentice | Medical Apprentice | cheerful-polite | Cheongpung addresses Mungyeong as 의생님 while asking him to greet the Tang Clan. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 문경 | 적천강 | old_acquaintances | Fire King | familiar and grave | The figure bearing Mungyeong’s name greets Jeok Cheongang by his established epithet. |
| 무송 | 적천강 | junior_martial_artist_to_legendary_martial_master | Great Hero Jeok | formal-deferential | Mu Song respectfully refers to Jeok Cheongang as 적 대협 while worrying that Jeok dislikes him. |
| 적천강 | 문경 | overwhelming elder to old acquaintance | you / little punk | mocking and threatening | Mocks Mungyeong's expression and threatens to poke out his eyes. |
| 적천강 | 무송 | legendary martial master to stronghold lord | you | gruff, coercive, and dismissive | Uses 자네 while ordering Mu Song to take the group only as far as Sichuan and leave the fast ship. |
| 청풍 | 무송 | young martial companion to stronghold lord | you | cheerful and familiar | Offers Mu Song his last dumpling and then induces him to buy more in Guang'an. |
| 문경 | 혁무진 | traveling_companion_to_traveling_companion | Martial Warrior Hyuk | formal-polite | Mungyeong asks Mujin to deliver water to Taekyung and lets Mujin receive the credit. |
| 혁무진 | 문경 | traveling_companion_to_traveling_companion | Mungyeong | casual-familiar | Mujin recognizes Mungyeong while reacting to Taekyung's dismantling work. |

## Listed compact profiles

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 505
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, the grandson and Disciple of Sword Saint Mae Jonghak, and a Supreme Peak martial master known as the Huashan Divine Dragon.
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, a deep love of martial arts, competitive pride, unusual resistance to monster-induced Fear, and discomfort when someone copies his martial arts.
- **Voice:** Dreamy and hazy, with innocent, polite phrasing; he has begun imitating Taekyung's profanity.
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions while Taekyung is his only true martial rival; Tang Sadok has temporarily entrusted Mimi to him.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 507
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Human Butcher.md

# Human Butcher (인도)

- **Safe through:** Chapter 505
- **Aliases:** None
- **Role:** Former mysterious Han Chinese mounted-bandit power in Northern Gaoyuan commanding fifty subordinates; a Peak master killed by an unnamed old man in a single move
- **Personality:** Cold, intimidating, and murderous; he kills people as though slaughtering livestock
- **Voice:** Cold, curt, and quietly threatening
- **Relationships:** He is one of four powerful participants at the Northern Gaoyuan gathering, intimidates Temur, and has claimed Ghost Sword Wipeng as his personal target in the proposed attack

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 507
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers and Vice Squad Leader of the Jin Dragon Squad.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 507
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, and Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Mu Song.md

# Mu Song (무송)

- **Safe through:** Chapter 507
- **Aliases:** Ship-Fire Boy
- **Role:** Lord of Water Dragon Stronghold, a Peak master and the Seafaring King's second martial Disciple who controls major Yangtze river traffic in Sichuan, belongs to the Yangtze River Channel League's moderate faction, and is an exceptionally skilled ship captain.
- **Personality:** Ambitious, domineering, impatient with interruptions, and capable of pragmatic cooperation when circumstances demand it.
- **Voice:** Deep and low in private, shifting to dry authority or boisterous command when addressing subordinates and rivals.
- **Relationships:** Mu Song belongs to the Yangtze River Channel League's moderate faction, regards Hwang Chung, his senior and Uncle Hwang, as family, and must now weigh whether the League will support the New Murim Alliance while the Seafaring King retains authority over major League decisions.

### Mungyeong.md

# Mungyeong (문경)

- **Safe through:** Chapter 507
- **Aliases:** Killing Ghost
- **Role:** Mungyeong is the legendary physician known as the former Divine Physician and Slaughter Saint, a Returned to Youth Supreme Peak master and the greatest assassin in history who passed the Divine Physician title to his Disciple.
- **Personality:** Compassionate, resolute, resourceful, and calm under extreme pressure.
- **Voice:** His Mungyeong persona is timid, deferential, and cheerful, while his Slaughter Saint voice is dry, impassive, and blunt.
- **Relationships:** Dong Feng is his Disciple, Jeok Cheongang is an old acquaintance whom Mungyeong helped break free of his Heart Demon, and Mungyeong was asked to look after and instruct Jin Taekyung after testing his basics.

### Pill Physician.md

# Pill Physician (환의)

- **Safe through:** Chapter 491
- **Aliases:** None
- **Role:** Current Family Head of the Seongsu Jang Family in Shandong, who personally placed and signed the Thousand-Year Snow Ginseng in the casket entrusted to the Yongbong Escort Bureau.
- **Personality:** No personality traits are established.
- **Voice:** No voice traits are established.
- **Relationships:** The Pill Physician heads the Seongsu Jang Family, a prestigious medical family in Shandong.

## Korean source

```text
＃508화



“너, 내가 누군지 알지?”

“……!”

“……!”

순간, 주위의 공기가 얼어붙었다. 나는 귀를 의심했고, 무송의 동공은 파르르 떨렸다.

오줌을 지릴 것 같은 표정으로 문경을 바라보던 그가 잔뜩 쉰 목소리를 쥐어짜 냈다.

“저, 전 아무것도 모릅니다.”

“그렇습니까.”

문경이 건조한 눈빛으로 무송을 응시했다.

“한데 왜 제게 존댓말을 쓰십니까. 무송 대협.”

“……!”

“겁이 없는 놈이로군. 감히 내 앞에서 거짓을 고하다니.”

“헙!”

제대로 걸려들었다. 아니, 그런데 무송 저 인간이 어떻게 문경의 정체를 알아차린 거지?

‘안 그래도 왜 자꾸 똥 마려운 개처럼 움찔거리나 싶더라니.’

행동을 보아하니 이미 전부터 문경의 정체를 알고 있었던 소리인데…… 그건 지금까지 내가 파악한 무송의 무공 수위로는 불가능에 가까운 일이다.

현재의 문경은 이미 반박귀진(返璞歸眞)의 경지와 더불어 반로환동(返老還童)에 도달한 상태.

이를 꿰뚫어 보기 위해서는 비슷한 경지의 고수이거나, 최소한 초절정 초입을 벗어나야 약간의 이질감이라도 느낄 수 있을 정도다.

‘그걸 무송이 알아차렸다?’

말도 안 되는 소리다. 차라리 혁무진이 청풍을 원 펀치 쓰리 강냉이로 쓰러트렸다는 걸 믿고 말지.

내가 그런 의문을 떠올리고 있던 찰나. 적천강이 심드렁한 어조로 입을 열었다.

“적당히 해 둬. 저놈도 입 다물고 있던 걸 봐서는 나름대로 모른 척 넘어가려고 했던 모양인데, 늙은이가 어린애 겁박하는 것도 보기 안 좋아.”

“늙은이? 겁박?”

문경이 코웃음을 흘렸다.

“어제까지만 해도 오늘내일하며 청승 떨던 늙은이가 조금 회춘했다고 입부터 살았군. 제삼자는 빠져라.”

“……뭐라?”

반로환동으로 주름 하나 없이 매끈해졌던 이마에 깊은 고랑이 파였다.

나는 황급히 적천강과 문경 사이로 끼어들며 만류했다.

“잠깐, 두 분 다 진정하세요. 진정.”

“네 녀석은 빠지거라.”

“빠져.”

“옙.”

한 치의 망설임도 없이 잽싸게 빠져나온 내게, 샌드위치 사이 양상추처럼 두 괴수 사이에 끼어 버린 무송이 구원의 눈빛을 보냈다.

대충 살려 줘, 뭐 그런 뜻인 것 같은데 고래 싸움에 오장육부 터질 일 있나.

‘나부터 살고 봐야지. 당장 두 사람이 생사결 벌일 것 같지도 않고.’

그리고 내 판단은 정확했다. 가만히 서로를 노려보던 적천강과 문경은 약속이라도 한 것처럼 동시에 기세를 가라앉혔다.

“흥. 그래도 도와줬으니 봐준다.”

“은혜도 모르는 늙은이 같으니.”

새침한 양로원 할아버지들처럼 한 마디씩을 주고받은 두 사람의 시선이 곧장 향한 곳은, 석상처럼 딱딱하게 굳어 있는 무송이었다.

“그러고 보니 신통한 놈일세. 네놈은 도대체 어찌 알았느냐?”

사실 나도 그게 가장 궁금하다.

무송의 대답을 기다리며 입만 빤히 바라보고 있는데, 의문에 대한 답은 문경의 입술 사이로 흘러나왔다.

“그자들이군. 이무기를 쫓아 이동했을 때 함께했던 수부들. 아니, 수룡채의 수적들이라고 해야겠지. 맞느냐?”

무송이 마른 침을 꿀꺽 삼켰다.

“그, 그렇습니다. 문경이라는 어린 의생의 정체가 고강한 무위를 지닌 초절정 고수인데다 제갈 가주도 막 다룰 정도로 배분이 높은 것 같다고…….”

나도 모르는 사이에 그런 일이 있었나?

하긴, 생각해 보면 당연한 일이다. 그 넓은 동정호를 등평도수로 뛰어다니며 나를 찾아냈을 리는 없을 테니까.

‘그나저나 이런 식으로 정체가 탄로나네.’

수십 년 동안 진정한 신분을 꽁꽁 숨겨 왔던 문경이다.

사천혈사가 벌어진 이후에도 그의 정체를 아는 이들은 제자인 신의를 제외하면 나와 적천강을 포함해서 한 손에 꼽을 정도.

아직 살성이라는 것까지 유추해 낸 것 같진 않지만, 비밀을 아는 사람이 늘어난다는 건 문경의 입장에서 결코 유쾌한 일이 아니었다.

물론 적천강은 그딴 거 상관없고 당장 팝콘이라도 뜯을 기세지만.

“멍청한 늙은이. 역용(易用)이라도 했어야지, 껄껄.”

“그럴 겨를 없었다. 네놈 제자 구하러 가느라 촌각이 아쉬웠으니까.”

“……크흠. 그 부분은 고맙군.”

껄껄 웃던 적천강이 웃음을 뚝 그치자, 문경이 작게 혀를 차며 무송을 응시했다.

“분명 전음(傳音)으로 경고했는데, 생각보다 충성스러운 수하를 둔 모양이군.”

“헉!”

문경의 서늘한 목소리에 무송이 눈을 부릅떴다.

그리고 다음 순간, 공력으로 이루어진 기막(氣幕)이 주위를 감싸고 있지 않았더라면 모두가 돌아봤을 만큼 큰 외침이 터져 나왔다.

“아, 안 됩니다!”

“뭐가 안 된단 말이냐?”

“제 수하들은 아무 잘못도 없으니, 차라리 제 목을 치십시오!”

“……내가 왜 네놈을 죽인단 말이냐.”

그 순간, 무송은 물론이고 나와 적천강까지 동시에 눈을 동그랗게 떴다.

“예? 아, 아닙니까?”

“안 죽여요?”

“저 늙은이가 미쳤, 아니 잠깐. 원래 노환이 옮기도 하나?”

노환의 전염성 여부에 대해 잠시 고민하던 적천강이 득의양양한 표정으로 외쳤다.

“그렇군. 노부는 감 잡았다! 죽이는 대신 단전을 폐하거나 사지 한 군데 정도 자를 생각이야!”

“……!”

파르르 떨리는 눈동자로 우리를 바라보던 문경이 회한에 목소리로 중얼거렸다.

“살심이 절로 드는군.”

무송이 두려움과 결의가 뒤섞인 표정으로 입을 열었다.

“수하들은 죄가 없습니다. 부디 저 하나로 만족…….”

“제발 주둥이 좀 닥쳐라. 찢어 버리기 전에.”

“흡. 예.”

무송을 기가 막힌 표정으로 내려다보던 문경이 한숨을 내쉬었다.

“네놈까지 합하여 여섯. 맞느냐?”

“마, 맞습니다. 노선배님. 모두 저와 오랜 세월을 함께한 사이고 입 또한 무겁습니다.”

“나는 네놈 같은 후배를 둔 적도 없고, 더 이상 무림인도 아니다. 하지만 입단속을 하지 않는다면 흔적도 남기지 않고 없애 버릴 수는 있지.”

“……!”

“편안히 천수를 누리다가 죽고 싶다면, 그 입을 영원히 봉하는 것이 좋을 거다. 해상왕은 물론 그 누구에게도 발설하지 마라. 알겠느냐?”

입을 꾹 다문 무송이 작게 고개를 끄덕이자, 문경이 등 뒤를 향해 턱짓했다.

“가라. 그리고 네 수하들에게 하남에 도착하기 전까지 배의 후미에는 얼씬도 하지 말라 일러두고.”

“예?”

“왜. 더 물어볼 것이 있나?”

“아, 아닙니다. 필요한 게 있으시다면 언제든지 불러 주십시오.”

고개를 꾸벅 숙인 무송이 후다닥 사라졌다. 이제 남아 있는 것은 나와 적천강, 마지막으로 문경을 포함한 세 사람이었다.

아쉬움 가득한 얼굴로 입맛을 다신 적천강이 내 옆구리를 쿡 찔렀다.

“저놈이 동네방네 떠들고 다녀야 재미있어질 텐데. 그렇게 생각하지 않느냐?”

“인…… 콜록.”

나는 인정이라는 두 글자를 황급히 기침으로 묻어 버렸다.

문경이 전혀 재미없다는 표정으로 이쪽을 노려보고 있었다. 방금 들은 말이 너무 재미없어서 만만한 놈 하나 잡아 족치고 싶은 기세다.

“전 아무 말도 안 했습니다.”

“나도 마찬가지인데, 찔리는 구석이 있나 보지?”

“그게 아니라, 그냥 미리 말씀드린 겁니다.”

“그래서 나도 네놈을 미리 손봐 줄까, 생각하고 있었다.”

“진짜 아닌데요.”

“들었다. 인. 그다음이 뭐냐?”

이럴 때일수록 당황하면 안 된다. 나는 침착하게 입을 열었다.

“인의(人意)가 있는데 어찌 그러겠냐는 뜻이었습니다.”

“아니었던 것 같은데.”

“사실인데요.”

“아니라니까.”

“맞다니까요. 왜 궁예질을 하세요.”

궁예가 뭔지는 몰라도 안 좋은 뜻이라는 걸 알아차린 것이 분명했다.

나는 서늘해진 문경의 시선을 애써 무시하며 황급히 화제를 돌렸다.

“그런데 왜 후미에 얼씬도 하지 말라고 하신 겁니까?”

“말 돌리지 마라.”

“…….”

말문이 턱 막히네.

할 말이 없어 떨떠름하게 입을 다문 내 모습에 문경이 혀를 찼다.

“이런 놈을 지금까지 잘도 제자랍시고 키웠군.”

팔짱을 낀 채 강 건너 불구경하고 있던 적천강이 피식 웃었다.

“그런 놈이라서 지금까지 키운 게지.”

“예의라고는 밥 말아 먹은 저놈을?”

“그런가? 노부는 허물이 없다고 생각했는데. 우리는 서로 생각이 다른 모양이야. 아니면 누군가가 애써 그런 생각을 무시하고 있거나.”

말없이 나와 적천강을 번갈아 바라보던 문경이 뇌까렸다.

“……청산유수로군. 반로환동 하더니 입만 살았어.”

도대체 이게 무슨 대화인지 모르겠다.

대화의 흐름을 파악하지 못한 내가 어리둥절해 하던 그때, 적천강이 쾌조선의 목제 난간에 기대고 있던 등을 뗐다.

“선실에 들어가 있어야겠군. 염병할 강물을 보고 있자니 지긋지긋해.”

“와, 그거 아주 좋은 생각이십니다. 혹시 성이 적씨가 아니라 제갈씨 아닙니까?”

이거야말로 듣던 중 반가운 소식이다.

하지만 냉큼 뒤를 따르려던 나는 첫걸음을 떼자마자 적천강의 손에 의해 가로막혔다.

툭.

“어?”

“어? 는 무슨. 왜 따라오는 게냐?”

“선실 가신다면서요?”

“그래서?”

“저도 마침 선실 가려던 참인데요.”

“좁아터진 선실에 무슨 사내가 둘씩이나 있는단 말이냐.”

“애초에 오 인실인데, 대체 양심 어디…….”

“운기조식이나 하며 근래에 얻은 깨달음을 정리하러 가는 것이니, 따라올 필요 없다.”

“아아, 운기조식하시러 가는구나. 그럼 제가 호법(護法)을…….”

“필요 없으니 여기 있거라.”

“예?”

내가 되묻자 적천강이 버럭 외쳤다.

“아, 여기 있으라고!”

“깜짝아. 왜 소리를 지르고 그러세요?”

“시끄럽다. 따라왔다가는 아주 경을 칠 줄 알아라!”

“……?”

어안이 벙벙한 채로 멀어지는 적천강을 바라보던 나는 따가운 시선에 슬쩍 고개를 돌렸다.

그리고 스핑크스의 앞발 근처 모래보다 건조한 문경의 시선과 마주쳤다.

‘시벌, 그냥 따라갈걸.’

적천강이 경을 치든 종을 치든 뭔 상관이냐.

내 목을 칠 수도 있는 인간과 단둘이 남아 있을 바에는 차라리 저 드넓은 장강으로 뛰어드는 게 훨씬 낫…….

“오늘따라 강물이 맑군. 들어가고 싶지 않으냐?”

“예?”

아니, 관심법 뭔데. 혹시 진짜 궁예인가.

문득 뇌리를 스치는 의심. 나도 모르게 철퇴를 든 금위장을 찾아 주위를 둘러본 바로 그 순간.

후웅-!

철퇴가 휘둘려졌다.

아니, 그것은 은밀하고도 쾌속한 한 줄기의 장력(掌力)이었다.

나는 귓가를 파고드는 파공성에 황급히 양팔을 교차시켜 막았지만, 살성이라는 희대의 고수가 쏘아 보낸 장력은 그리 쉽게 막아 낼 수 있는 것이 아니었다.

퍼엉!

시벌, 이건 진짜 철퇴 같네.

나는 뻐근한 가슴 통증을 느끼며 쾌조선 밖으로 튕겨 나갔다.

그리고 물살에 처박히기 직전, 신형을 뒤집으며 하단전의 공력을 다리로 흘려보내며 수면을 밟았다.

철벅!

마치 물웅덩이에 발을 담근 것처럼, 잔잔하던 수면이 거칠게 튀었다.

등평도수(登萍渡水)의 수법으로 우뚝 선 나는 어이없는 눈빛으로 문경을 노려보았다.

“갑자기 뭐 하자는 겁니까?”

“잔잔하던 강물이 흐트러지는군.”

“이게 지금 도대체…… 예?”

“네놈의 거친 움직임에 풍랑이라도 일 것 같다는 말이다.”

뭐라 할 새도 없었다. 나를 바라보며 작게 혀를 찬 문경이 말을 이었다.

“그럼…… 시작해야겠군.”

띠링.



- 연계 퀘스트, [가짜 무림인-2단계]가 시작되었습니다!
```

## Final English reading copy

```markdown
# Chapter 508

“You know who I am, don’t you?”

“……!”

“……!”

The air around us froze. I doubted my ears, while Mu Song’s pupils trembled.

He had been staring at Mungyeong with an expression like he was about to wet himself. Now he squeezed out a hoarse voice.

“I-I don’t know anything.”

“Is that so?”

Mungyeong stared at Mu Song with a dry gaze.

“Then why are you speaking formally to me, Great Hero Mu Song?”

“……!”

“What a fearless bastard. How dare you lie to me right to my face?”

“Gasp!”

He had fallen for it hook, line, and sinker.

But how had Mu Song figured out Mungyeong’s identity?

*No wonder he kept flinching like a dog that needed to shit.*

Judging by his behavior, Mu Song had known Mungyeong’s identity for some time. But based on the level of martial arts I had seen from him so far, that should have been nearly impossible.

Mungyeong had already reached the realm of Returning to Simplicity and achieved Returned to Youth.

To see through it, someone had to be a master in a similar realm. At the very least, they had to have surpassed the early stages of Supreme Peak before they could sense even the slightest hint of anything unusual.

*Mu Song had noticed that?*

That was absurd. I would sooner believe Hyuk Mujin had taken Cheongpung down with a one-punch, three-teeth combo.

Just as I was pondering the matter, Jeok Cheongang opened his mouth in a bored tone.

“That’s enough. From the fact that the fool kept his mouth shut, it seems he was trying to pretend he didn’t know and let the matter pass. It’s not a good look for an old man to threaten a child.”

“Old man? Threaten?”

Mungyeong let out a derisive snort.

“The old man who was moping around as though he could die any day until yesterday has gotten a little younger and suddenly found his tongue. Outsiders, stay out of this.”

“……What did you say?”

A deep furrow appeared on the forehead that Returned to Youth had made smooth and free of wrinkles.

I hurriedly stepped between Jeok Cheongang and Mungyeong to stop them.

“Wait. Both of you, calm down. Calm down.”

“You, get out of here.”

“Get out.”

“Yes, sir.”

I slipped away without a moment’s hesitation. Mu Song, who had been wedged between the two monsters like a piece of lettuce between sandwich slices, sent me a pleading look.

It seemed to mean, *Save me.*

But was I supposed to let my guts burst in a fight between two whales?

*I need to save myself first. It doesn’t look like they’re about to have a life-and-death duel.*

My judgment was correct. Jeok Cheongang and Mungyeong glared at each other in silence, then lowered their auras simultaneously, as if they had planned it.

“Hmph. I’ll let it pass since you helped me.”

“What an ungrateful old man.”

The two of them exchanged a word each like a pair of prim old men in a nursing home. Then their gazes turned toward Mu Song, who had gone stiff as a stone statue.

“Come to think of it, you’re quite a remarkable fellow. How on earth did you know?”

That was what I was most curious about, too.

I waited for Mu Song’s answer, staring at his lips. But the answer came from Mungyeong instead.

“So it was them. The waterway men who were with you when you moved after the imugi. Or rather, the river bandits of Water Dragon Stronghold, I suppose. Am I right?”

Mu Song swallowed dryly.

“Y-yes, sir. They said the young medical apprentice named Mungyeong was actually a Supreme Peak master with formidable martial arts, and that his standing seemed high enough for him to order even the Zhuge Family Head around…”

*Did that happen without me knowing?*

Actually, when I thought about it, it made perfect sense. There was no way he could have found me by running across the surface of the vast Dongting Lake with Rising on Duckweed, Crossing Water.

*So this is how his identity gets exposed.*

Mungyeong had kept his true identity hidden for decades.

Even after the Sichuan Blood Tragedy, the people who knew his identity could be counted on one hand, including Jeok Cheongang and me, apart from his Disciple, the Divine Physician.

Mu Song did not seem to have inferred that Mungyeong was the Slaughter Saint yet, but from Mungyeong’s perspective, having more people learn his secret could hardly be pleasant.

Jeok Cheongang, of course, did not care about any of that. He looked ready to start eating popcorn right then and there.

“You stupid old man. You should have used a disguise, at least. Ha ha ha.”

“I had no time. Every moment counted while I was going to save your Disciple.”

“……Ahem. I do appreciate that.”

Jeok Cheongang stopped laughing abruptly. Mungyeong clicked his tongue softly and stared at Mu Song.

“I clearly warned you through Sound Transmission, but it seems you have more loyal subordinates than I expected.”

“Gasp!”

At Mungyeong’s chilly voice, Mu Song’s eyes flew wide.

The next moment, a shout so loud that everyone nearby would have turned to look burst out—if a screen of internal energy had not been enclosing the area.

“N-no, you can’t!”

“What can’t I do?”

“My subordinates haven’t done anything wrong! Take my head instead!”

“……Why would I kill you?”

At that moment, Mu Song, Jeok Cheongang, and I all stared at him with our eyes wide.

“What? Ah, you’re not?”

“You’re not going to kill me?”

“That old man’s gone mad—wait. Are age-related infirmities contagious?”

After briefly considering whether infirmities of old age were contagious, Jeok Cheongang shouted with a triumphant expression,

“I see now! This old man has figured it out! Instead of killing him, you’re planning to cripple his dantian or cut off one of his limbs!”

“……!”

Mungyeong looked at us with trembling eyes and muttered in a voice filled with regret,

“I can feel the urge to kill rising on its own.”

Mu Song spoke with an expression that mixed fear and resolve.

“My subordinates are innocent. Please, be satisfied with taking only me…”

“Please shut your mouth before I tear it apart.”

“Gasp. Yes, sir.”

Mungyeong looked down at Mu Song with an utterly incredulous expression, then sighed.

“Six, including you. Correct?”

“Y-yes, Senior. We have all been together for many years, and they know how to keep their mouths shut.”

“I have never had a junior like you, and I am no longer a martial artist. But if you fail to keep them quiet, I can make all six of you disappear without leaving a trace.”

“……!”

“If you want to live out your natural span in peace, you would do well to seal those mouths forever. Do not tell the Seafaring King—or anyone else. Understood?”

Mu Song pressed his lips together and gave a small nod. Mungyeong jerked his chin toward the rear of the ship.

“Go. And tell your subordinates not to come anywhere near the stern until we reach Henan.”

“What?”

“Why? Is there something else you want to ask?”

“N-no, sir. If you need anything, please call for me at any time.”

Mu Song bowed deeply and hurried away.

That left three of us: me, Jeok Cheongang, and Mungyeong.

Jeok Cheongang smacked his lips, his face full of disappointment, and poked me in the side.

“It would be more fun if that fool went around blabbing to everyone. Don’t you agree?”

“I adm—cough.”

I hurriedly buried the word *admit* in a cough.

Mungyeong was glaring at us with an expression that said he was having absolutely no fun at all. He looked ready to grab the nearest person and beat him senseless just because what he had overheard was so irritating.

“I didn’t say anything.”

“Neither did I. Unless you have something to feel guilty about?”

“That’s not it. I was just giving you a little advance notice.”

“That’s why I was wondering whether to give you a little advance beating.”

“I really didn’t mean anything.”

“I heard you say ‘admi.’ What came after that?”

At times like this, panicking was the worst thing I could do. I calmly opened my mouth.

“I meant, ‘Admittedly, I have a conscience. How could I do such a thing?’”

“That doesn’t sound like what you said.”

“But it’s true.”

“No, it isn’t.”

“It is. Why are you playing Gung Ye?[^1]”

Mungyeong clearly did not know what Gung Ye was, but he had realized that it was not a compliment.

I deliberately ignored his suddenly chilling gaze and hurriedly changed the subject.

“By the way, why did you tell him not to go anywhere near the stern?”

“Don’t change the subject.”

“……”

I was completely speechless.

When I awkwardly shut my mouth, Mungyeong clicked his tongue.

“You’ve done well raising a man like this as your Disciple.”

Jeok Cheongang, who had been watching with his arms folded as though none of this concerned him, let out a quiet laugh.

“That’s exactly why I raised him.”

“You raised that utterly ill-mannered man?”

“Is that so? I thought we were close enough not to stand on ceremony. It seems we see things differently. Or perhaps someone is deliberately ignoring that thought.”

Mungyeong silently looked back and forth between Jeok Cheongang and me, then muttered,

“……You’re as smooth as flowing water. Returned to Youth, and now only your mouth has gotten lively.”

I had no idea what kind of conversation this was supposed to be.

Just as I was staring blankly, unable to follow its flow, Jeok Cheongang pushed himself away from the wooden railing of the swift ship.

“I should go into the cabin. Looking at this goddamn river is getting tiresome.”

“Wow, that’s excellent news. Are you sure your surname isn’t Zhuge instead of Jeok?”

That was the best thing I had heard all day.

But the moment I took my first step to follow him, Jeok Cheongang blocked my way with his hand.

Thud.

“Huh?”

“‘Huh?’ What do you mean, ‘huh’? Why are you following me?”

“You said you were going to the cabin.”

“So?”

“I was just about to go there myself.”

“How can two men fit inside that cramped cabin?”

“It’s a five-person cabin in the first place. Where did your conscience—”

“I’m going there to circulate my qi and organize the enlightenment I’ve gained recently. There’s no need for you to follow me.”

“Oh, you’re going to circulate your qi. Then I’ll stand guard—”

“Not necessary. Stay here.”

“What?”

When I asked again, Jeok Cheongang suddenly shouted.

“I said stay here!”

“Whoa, you startled me. Why are you shouting?”

“Shut up. If you follow me, you’ll be in for it!”

“……?”

I stared blankly at Jeok Cheongang as he walked away. Then I slowly turned my head at the prickling sensation of someone’s gaze.

I met Mungyeong’s stare. It was drier than the sand near a Sphinx’s forepaws.

*Fuck. I should have followed him.*

What did it matter whether Jeok Cheongang caught hell or rang a bell?

Rather than remain alone with a man who might cut off my head, I would have been better off jumping into the vast Yangtze—

“The river looks unusually clear today. Don’t you want to go in?”

“What?”

What the hell was this mind-reading? Was he actually Gung Ye?

A suspicion suddenly flashed through my mind. Without thinking, I looked around for a palace guard carrying a mace.

That was when—

Whoom!

A mace came swinging at me.

No. It was a single, swift, and stealthy wave of palm force.

I hastily crossed both arms to block it when the sound of splitting air pierced my ears, but the palm force fired by a once-in-an-age master known as the Slaughter Saint was not something I could block so easily.

Boom!

*Fuck, that really is like getting hit with a mace.*

I felt a dull pain in my chest as I was blasted off the swift ship.

Just before I plunged into the water, I twisted my body around, sent the internal energy in my lower dantian into my legs, and stepped onto the surface of the river.

Splash!

The calm surface exploded violently, as though I had stepped into a puddle.

I stood upright using Rising on Duckweed, Crossing Water, then glared at Mungyeong with an incredulous expression.

“What are you trying to do all of a sudden?”

“The calm river has been disturbed.”

“What does that even—what?”

“I mean your rough movements look as though they might cause a storm.”

I had no time to say anything else. Mungyeong looked at me and clicked his tongue softly before continuing.

“Then… we should begin.”

> **System**
> 
> - Linked Quest **Fake Murim Martial Artist—Stage 2** has begun!

[^1]: Gung Ye was a Korean ruler traditionally portrayed as claiming to read people’s minds.
```

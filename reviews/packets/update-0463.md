<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0463.txt",
      "sha256": "a58683bf8345afca988f9ed260e839577de76432d41c1888bbdd83a87cfc424f",
      "bytes": 13497
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "1baf5dfc33b12e3bb39ee8594d8ab5411c68e01d611c5f887af5a30edd2b5d25",
      "bytes": 3937
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "862df6cb65a5d58ddaca1039c8edb3289f7c6f72c9015f740ff83eb847dc35d9",
      "bytes": 150883
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "e058c0c604854bb09c140b1510bfabc86e66825f682cdb27c92e2f532d883758",
      "bytes": 990
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "39835117983c4ab6fb7bf7f512ab0f2061087d53edc88d40d10cfe11832cefe3",
      "bytes": 553
    },
    {
      "path": "characters/Dongting Fisherman.md",
      "sha256": "53ed8dd94679f27f9d27ae9be1b1f2ecb78671628dd2e9bc9a4488a95e0bfb23",
      "bytes": 703
    },
    {
      "path": "characters/Gung Gibang.md",
      "sha256": "228890d105b5509466b9fb42c258dbe2f23159590c49a0b192e4f8cc610d7c3f",
      "bytes": 662
    },
    {
      "path": "characters/Heavenly Power Demon.md",
      "sha256": "66c6120e5c6a36a154ddfa7954514bc1d9ada686cc343f491482afb16ca3a01a",
      "bytes": 1018
    },
    {
      "path": "characters/Hong Dao.md",
      "sha256": "2f63f3d5c78393c5ac66ba7c926dee574f0448cba24e4016b7fcd6ae8e6891d6",
      "bytes": 1001
    },
    {
      "path": "characters/Hyeongong.md",
      "sha256": "0ed34a69317e98af7b7fc9e7c232a617f1e5a4d35231089f785d67cddde7e8f4",
      "bytes": 735
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "e04043a18f9558be52f39853fb75fa0a6ae2e98ab16a9fa3cc109c650be1d593",
      "bytes": 1108
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "0d90df2772ff200c17dd3d4bf3d7f3e1c8a74791308933424e458717221e4b19",
      "bytes": 1470
    },
    {
      "path": "characters/Mungyeong.md",
      "sha256": "f804d382daa65d907f5f9a635bdcd8756b595cfd8a4c7346795f858f5eb7625d",
      "bytes": 686
    },
    {
      "path": "characters/Zhuge Feng.md",
      "sha256": "4ae6e0842c8e99e532c28fd9765a08413c0a0cafd2d28fed133b6afa3b7b43e9",
      "bytes": 626
    },
    {
      "path": "characters/Zhuge Gonghu.md",
      "sha256": "42b441b996eb3f9706792daa0e907f2662ba1883e6ee29fd76020fd14d77ee76",
      "bytes": 561
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "8b90c2f29d6d3601f105e825dbd8f23e08fa842fa25760e2441538acfe65522f",
      "bytes": 145865
    }
  ],
  "estimated_tokens": 13338
}
-->

# Durable State Update — Chapter 463

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 463. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 463. Profile updates may replace only one
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
  "chapter": 463,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 463,
    "continuity_sources": [463],
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
    "Taekyung completed the unavoidable Peak-grade Quest The Tragedy of Dongting Lake, rescued the only two survivors found, and earned the Water Rescue Worker Title.",
    "Honglan survived the Dongting Lake disaster and is recovering; Ju Wongong remains unconscious under guard after passing the most dangerous stage of his injuries.",
    "Jin Wikyung is acting as an inspector for the new Murim Alliance and is cooperating with Taekyung's investigation.",
    "The shared symbols between the Arch Lich's magic circle and Dark Heaven's formations remain unexplained.",
    "The Sea Serpent Society and three Yangtze River Channel League strongholds, including Donghu Stronghold, were destroyed with more than a thousand casualties, while the perpetrators' wider plans remain unknown.",
    "The Dongting Fisherman is a previous-generation Supreme Peak water-arts master suspected of Dark Heaven involvement and the Dongting Lake attack; the Hidden Shadow Ghost is the local name for an unseen killer of boatmen who may be connected to him.",
    "Four of five suspected Dongting Fisherman refuges have been searched without results; Taekyung's group is proceeding to the final, deepest site despite worsening weather, intending to capture him alive.",
    "Zhuge Clan and Wudang are searching Donghu Stronghold for Dark Heaven traces; Mungyeong found no land evidence or Moving Formation remnants and has entered the river to search the remaining area.",
    "Wudang is responding to an unidentified killer demon responsible for more than thirty deaths, including twenty pilgrims on Mount Wudang.",
    "The Skeleton King's undead identity remains concealed, and Taekyung has ordered him to join Peace Guild under a prepared contract.",
    "Go Jun is expected to succeed Lee Jungryong as Ares Guild's captain and is searching China for Lee's holographic recorder.",
    "The captured Three Fiends is a former-generation great fiend and Supreme Peak Dark Heaven subordinate whom Taekyung is transporting alive to investigate possible codes or markings."
  ],
  "continuity_sources": [
    462,
    461
  ],
  "open_questions": [
    "What are the origin and purpose of the symbols shared by the Arch Lich's magic circle and Dark Heaven's formations?",
    "Who destroyed Donghu Stronghold and the related Yangtze River Channel League strongholds, why was no Moving Formation trace left, and was the destruction a diversion?",
    "What is the Dongting Fisherman's exact role in Dark Heaven, is he the Hidden Shadow Ghost, and does the final suspected site contain his refuge?",
    "Is the killer demon attacking Wudang connected to Dark Heaven?",
    "What evidence is contained in Lee Jungryong's holographic recorder, and what are the terms of the Peace Guild–Wizard Guild agreement?"
  ],
  "safe_through": 462,
  "temporary_decisions": [
    "Render 익양루 as Yiyang Tower.",
    "Render 황철 as Hwang Cheol, 도립군 as Do Ripgun, 광수도귀 as Mad Water Saber Demon, 파랑호 as Wave Fox, 동정호 as Dongting Lake, and 사천혈사 as Sichuan Blood Tragedy.",
    "Render 살귀 as killer demon, 은영귀 as Hidden Shadow Ghost, 일급 낭인 as First Rate wandering martial artist, 삼괴 as Three Fiends, 대마두 as great fiend, and 마군 as Demon Lord.",
    "Render 시부럴 as “sibu-leol,” 시벌좌 as “Lord Fuck,” and 시부럴좌 as “Lord Sibu-leol.”",
    "Preserve the Skeleton King's grandiose, mock-offended voice and Taekyung's dry, profane humor; render 주원공 as Ju Wongong, 대죽산표국 as Daejuksan Escort Bureau, 형문검가 as Hyungmun Sword Family, 응성상회 as Eungseong Merchant Association, 천룡인 as Celestial Dragon, 사인교 as four-person sedan chair, 홍란 as Honglan, 가기 as singing courtesan, 구족 as the nine branches of kin, 수상 구조대원 as Water Rescue Worker, and 수공 as water arts."
  ],
  "version": 1
}
```

## Exact glossary matches

| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 청풍     | **Cheongpung**     |
| 굉도     | **Hong Dao**       |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 법왕     | **Dharma King**               | Hong Dao       |
| 살성     | **Slaughter Saint**           | —              |
| 무당파    | **Wudang**                       |
| 암천     | **Dark Heaven**                  |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 혈도     | **acupoint** / **vital point**                   | Context dependent                                     |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 정파     | **orthodox faction**                             |                                                       |
| 마교     | **Demonic Cult**                                 |                                                       |
| 제자     | **Disciple**                                 |
| 선배     | **Senior**                                   |
| 시스템              | **System**                     |
| 칭호               | **Title**                      |
| 하남     | **Henan**              |
| 사천     | **Sichuan**            |
| 정마대전   | **Great Faction War**         |
| 노부      | **this old man / I**                                            |
| 소협      | **Young Hero**                                                  |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 동정어옹 | **Dongting Fisherman** | Publicly condemned the Yangtze River Channel League and disappeared three days before this chapter. |
| 궁기방 | **Gung Gibang** | Beggars' Sect Successor Beggar and finalist. |
| 천력마 | **Heavenly Power Demon** | Formerly imprisoned Tang Clan criminal; distinct from 천력부, Heavenly Axe. |
| 현공진인 | **Perfected Being Hyeongong** | Veteran Wudang Daoist master and the current Sect Leader's Junior Brother. |
| 문경 | **Mungyeong** | Young medical apprentice and newly introduced passenger. |
| 제갈풍 | **Zhuge Feng** | Current Family Head of the Zhuge Clan. |
| 제갈공후 | **Zhuge Gonghu** | Former Murim Alliance Chief Strategist and deceased member of the Ten Kings. |
| 만년한철 | **Ten-Thousand-Year Cold Iron** | Material that destroys Pung Yang's Body-Protecting Qi when the Unnamed Sword satisfies a specific condition. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 사천당문 | **Sichuan Tang Clan** | Martial clan cited for its poison-based cleansing method. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 천기 | **heavenly patterns** | Celestial patterns Hong Dao studies to perceive major changes and omens. |
| 노환 | **infirmities of old age** | Jeok Cheongang's age-related illness. |
| 오기조원 | **Five Qi Returning to Origin** | High martial realm displayed by Jeok Cheongang. |
| 기관진식 | **mechanisms and formations** | Fifth preliminary assessment category. |
| 천마신교 | **Heavenly Demon Divine Cult** | The Demonic Cult's self-styled formal name. |
| 반로환동 | **Returned to Youth** | Possible explanation for an apparently young Supreme Peak master. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 당문 | **Tang Clan** | Short form for the Sichuan Tang Clan. |
| 장강 | **Yangtze** | The river controlled by the Yangtze River Channel League. |
| 의생 | **medical apprentice** | Mungyeong's occupation. |
| 살수 | **assassin** | Professional killer considered as a possible suspect. |
| 신교 | **Divine Cult** | Short form used by the Divine Cult's members for the Heavenly Demon Divine Cult. |
| 뇌옥 | **underground prison** | The Tang Clan's subterranean prison. |
| 마두 | **fiend** | Demonic martial masters from the Great Faction War era. |
| 와룡객 | **Crouching Dragon Guest** | Epithet of Zhuge Feng. |
| 천령폭 | **Tianling Falls** | Dangerous waterway leading to Donghu Stronghold. |
| 동정호 | **Dongting Lake** | Lake under which Dangyang and Honghu Strongholds operated. |
| 수공 | **water arts** | Water-based martial arts; the Dongting Fisherman's specialty. |
| 나룻배 | **ferryboat** | Small ferry used to reach the suspected refuge site. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 청풍 | 혁무진 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung includes Mujin among his 은인들 after receiving the skewers. |
| 혁무진 | 청풍 | martial artist to young master | Young Master | formal-deferential | Mujin uses 공자께서는 when asking why Cheongpung descended from the mountain. |
| 적천강 | 청풍 | overwhelming_elder_to_young_martial_artist | you / little punk | blunt, amused, and threatening | Jeok Cheongang uses 네, 이놈, and related blunt forms while testing Cheongpung. |
| 청풍 | 적천강 | young_martial_artist_to_overwhelming_elder | Grandpa Jeok | casual-familiar despite deference | Cheongpung uses 적 할아버지 while asking Jeok Cheongang to confirm Taekyung's condition; this is a familial form of address, not literal kinship. |
| 혁무진 | 적천강 | subordinate_to_overwhelming_elder | Great Hero Jeok | deferential and fearful | Mujin uses 적 대협 while reporting Jeok’s orders and Taekyung’s awakening. |
| 적천강 | 혁무진 | overwhelming_elder_to_junior_martial_artist | you stupid fool | blunt and mocking | Jeok calls Mujin a 멍청한 놈 after knocking him down during the attempted escape. |
| 적천강 | 굉도 | old_friends | Hong Dao | familiar and teasing | Uses Hong Dao's personal name in their casual reunion. |
| 굉도 | 적천강 | old_friends | Fire Gate Sect Leader | familiar and teasing | Teases Jeok as the carefree Fire Gate Sect Leader. |
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

## Listed compact profiles

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 462
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, the grandson and Disciple of Sword Saint Mae Jonghak, and a Supreme Peak martial master known as the Huashan Divine Dragon.
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, a deep love of martial arts, and a martial artist's competitive pride; he becomes unsettled when someone copies his martial arts
- **Voice:** Dreamy and hazy, with innocent, polite phrasing; he has begun imitating Taekyung's profanity.
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions while Taekyung is his only true martial rival; Tang Sadok has temporarily entrusted Mimi to him.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 462
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Dongting Fisherman.md

# Dongting Fisherman (동정어옹)

- **Safe through:** Chapter 462
- **Aliases:** None
- **Role:** The Dongting Fisherman is a previous-generation Supreme Peak master whose water arts rival the Seafaring King; he is identified as Dark Heaven's tail and suspected perpetrator of the Dongting Lake attack, with hidden refuges throughout the lake.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** The Dongting Fisherman opposed the Yangtze River Channel League and was monitored by the Lower District Sect for several years after friction with it, while current records place him in Hubei Province.

### Gung Gibang.md

# Gung Gibang (궁기방)

- **Safe through:** Chapter 462
- **Aliases:** Successor Beggar, Beggar Prince, pure-blooded beggar, ultimate beggar
- **Role:** Gung Gibang is the Beggars' Sect Successor Beggar and a unique eight-knot disciple.
- **Personality:** Vulgar, aggressive, and quick-tempered.
- **Voice:** Blunt, profane, and vividly threatening.
- **Relationships:** Gung Gibang is a rival finalist alongside Baek Woo and Zhuge Gyun who trades insults with Taekyung and uses Beggars’ Sect intelligence to investigate Tang Taesang’s murder and search for Dark Heaven’s Hubei forces.

### Heavenly Power Demon.md

# Heavenly Power Demon (천력마)

- **Safe through:** Chapter 399
- **Aliases:** None
- **Role:** Deceased former Elder of the Great Heavenly Demon Divine Cult who led the subjugation of Qinghai and opened the first front of its holy war before transferring three jiazi of internal energy to Jin Taekyung and asking him to kill the Western Heaven Demon Lord.
- **Personality:** Quiet and self-possessed despite his severe imprisonment, he is reflective about the moral ambiguity of the Great Faction War and disillusioned with the Divine Cult's corruption.
- **Voice:** Gruff and dry, with formal self-reference as 노부.
- **Relationships:** He was once an Elder and commander under the Great Heavenly Demon Divine Cult's Cult Leader, has spent more than forty years imprisoned by the Sichuan Tang Clan, and identifies the Western Heaven Demon Lord as one of the Divine Cult's four Protectors who served closest to and led astray the Cult Leader.

### Hong Dao.md

# Hong Dao (굉도)

- **Safe through:** Chapter 459
- **Aliases:** Dharma King
- **Role:** Abbot of Shaolin and the Murim's Dharma King; master of Unnamed and the only friend to whom Jeok Cheongang had opened his heart; after leaving the Star-Array Grand Banquet, he was found in a massive pit with both legs severed and catastrophic internal injuries, whispered final words to Jeok Cheongang, and died.
- **Personality:** Calm, responsible, quietly playful, and still regarded by Jeok as lazy for sleeping whenever possible.
- **Voice:** Quiet, deep, weighty, and resonant, with casual familiarity when speaking to Jeok Cheongang.
- **Relationships:** Old friend of Jeok Cheongang; master of Unnamed; before his death, entrusted the Green Jade Buddha Staff to Unnamed and used his final words to warn Jeok about Jongni Chu, Dark Heaven, Unnamed, and the Buddhist Staff; sends Unnamed to bring the Master of Morning Star to Shaolin.

### Hyeongong.md

# Perfected Being Hyeongong (현공진인)

- **Safe through:** Chapter 462
- **Aliases:** None
- **Role:** Perfected Being Hyeongong is a veteran Wudang Daoist master of the previous generation, the current Sect Leader's Junior Brother, and a Supreme Peak swordsman who reached the ultimate stage of the Taiji Wisdom Sword.
- **Personality:** Hyeongong is humble and self-deprecating about his limited worldly knowledge while carrying the authority of an experienced senior master.
- **Voice:** Measured, respectful, and lightly self-deprecating.
- **Relationships:** Hyeongong is the current Wudang Sect Leader's Junior Brother and a respected senior to Zhuge Feng.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 462
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers and Vice Squad Leader of the Jin Dragon Squad.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 461
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master, and Jin Taekyung's Master.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, and pathologically afraid of water. His meeting with Taekyung rekindled his will to live, making him determined to extend his life despite his illness.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Mungyeong.md

# Mungyeong (문경)

- **Safe through:** Chapter 462
- **Aliases:** None
- **Role:** Mungyeong is the legendary physician known as the former Divine Physician and Slaughter Saint, having passed the Divine Physician title to his Disciple.
- **Personality:** Compassionate, resolute, resourceful, and calm under extreme pressure.
- **Voice:** His Mungyeong persona is timid, deferential, and cheerful, while his Slaughter Saint voice is dry, impassive, and blunt.
- **Relationships:** Dong Feng is his Disciple, while Jeok Cheongang, Jin Taekyung, Cheongpung, and the two Sect Leaders know his Slaughter Saint identity.

### Zhuge Feng.md

# Zhuge Feng (제갈풍)

- **Safe through:** Chapter 455
- **Aliases:** Crouching Dragon Guest
- **Role:** Zhuge Feng is the current Family Head of the Zhuge Clan and father of its Lesser Family Head, Zhuge Gyun.
- **Personality:** Analytical and disarmingly casual, he treats comfort and time as principles while delivering grave intelligence with unsettling directness.
- **Voice:** Clear, calm, polished, and conversational, with understated humor and pointed questioning.
- **Relationships:** Zhuge Gyun is his son, and Zhuge Gonghu was his grandfather.

### Zhuge Gonghu.md

# Zhuge Gonghu (제갈공후)

- **Safe through:** Chapter 455
- **Aliases:** None
- **Role:** Former Chief Strategist of the Murim Alliance; a Supreme Peak martial artist known for immortal arts and outstanding formation techniques, one of the Ten Kings and a member of the Three Saints; deceased for more than ten years
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** Former Murim Alliance Chief Strategist and member of the Three Saints and Ten Kings.

## Korean source

```text
＃463화



희미한 빛이 스며드는 깊고 어두운 동굴 안. 자그마한 체구의 노인은 가부좌를 튼 채 자신을 관조하고 있었다.

태양과도 같은 기운이 수백 개의 혈도를 지나 기경팔맥(奇經八脈)으로 치닫자, 유형의 기운이 일어나 노인의 전신을 감싸 안았다.

그리고 이내 변화가 시작되었다.

솨아아아.

하얗게 센 노인의 머리 위로 세 개의 꽃봉오리가 피어오르고, 이내 사라졌다.

꽃봉오리를 이룸과 동시에 흩어진 기운은 새로운 형상을 만들어냈다. 오색찬란한 빛을 띤 다섯 개의 원.

초절정 고수 중에서도 선택받은 소수만이 이룩한 경지. 바로 오기조원(五氣朝元)에 다다른 자만이 보일 수 있는 현상이었다.

하지만 노인을 둘러싼 변화는 그것으로 끝나지 않았다.

화륵. 츠츠츠츠!

오기조원을 상징하는 다섯 개의 원이 붉게 물들었다. 극강의 열양지기를 머금은 공력의 고리로부터 뿜어져 나온 엄청난 화기가 노인을 휘감고, 이내 푸른 빛을 띠었다.

노화순청(爐火純靑).

화로의 불이 뜨거워지면 푸른색으로 변하는 법. 노인이 이룩한 무공의 경지 역시 마찬가지였다.

장장 백 년이 넘는 세월 동안 쌓이고 쌓인 공력과 깨달음은 이미 극의(極意)에 달했다고 해도 과언이 아니었다.

그러나…….

‘여기까지인가.’

노인, 화왕(火王) 적천강은 공력을 거둬들였다. 가부좌를 튼 채 허공에 떠올라 있던 신형이 지면에 닿는 순간, 그를 둘러싼 기이한 현상도 씻은 듯이 사라졌다.

고요한 공간에 남은 것은 적천강의 실소뿐이었다.

“허허.”

어찌하여 눈앞의 벽을 넘어 더 나아갈 수 없는가.

그 사실을 누구보다 잘 알고 있기에 고개를 끄덕이면서도, 미동도 하지 않는 벽이 아쉽고 애석했다. 하늘이 원망스럽기도 했다.

그러나 적천강은 미간을 찌푸리는 대신 웃음으로 씁쓸한 마음을 달랬다.

‘무얼 원망할까. 노부가 자초한 일인 것을.’

무공은 끊임없는 단련으로 강해지고, 깨달음은 마음을 비웠을 때 비로소 찾아온다.

그러나 적천강은 지난 수십 년간 마음에 쌓인 찌꺼기를 비워 내지 못했다.

이렇게 쌓이고 고인 것은 언젠가 썩는 법. 썩은 마음에 번뇌가 가득하니 심마(心魔)가 찾아왔고, 심마가 찾아오니 노환을 막을 수 없었다.

“그나마 녀석을 만나지 않았다면…… 아마 지금쯤 벽에 똥칠하고 있었겠지. 허허.”

적천강은 너털웃음을 지었다.

한 번. 단 한 번의 작은 깨달음을 얻는다면 반로환동(返老還童)의 경지에 도달할 수 있을 것이다.

하지만 그는 알고 있었다. 이 또한 욕심이라는 것을. 완전히 비우지 못한 마음이라는 것을.

문득 고개를 들자 자그마한 구멍 사이로 하늘이 비친다. 적천강은 저 너머, 보이지 않는 누군가에게 물었다.

“이것으로 만족하라는 뜻이구려. 맞소?”

대답은 돌아오지 않았다. 아니, 어쩌면 이미 대답을 들었는지도 몰랐다.

타고난 살귀(殺鬼)를 제자로 거두어 죄 없는 이들을 죽게 했으나, 두 번째 제자 덕분에 정신이라도 온전히 보전할 수 있게 되었으니 더 이상 어떤 미련도 갖지 말라는 대답.

대답하는 존재는 없었지만, 적천강은 자신의 마음에서 들려오는 대답을 들었다.

“참으로 지랄 같군. 노부가 지금껏 처리해 준 마두(魔頭)가 몇 놈인데 이런 푸대접이라니.”

푸념 섞인 한숨을 내쉰 적천강이 고개를 내리며 말을 이었다.

“그렇게 생각하지 않느냐?”

적천강의 시선 끝에 선 한 사람, 와룡객(臥龍客) 제갈풍이 쥘부채를 흔들며 대답했다.

“언젠가 조부께서 아홉 살이 된 저를 곁에 앉혀 두고 그런 말씀을 하셨지요. 저 위에 어떤 놈이 있는지는 몰라도, 참으로 지랄 같은 성미를 지닌 것이 분명하다. 지금 노 선배께서도 같은 말씀을 하시는군요.”

적천강이 고개를 끄덕였다.

“제갈공후, 그놈이 그래도 가끔가다 한 번씩 맞는 말을 하긴 했지.”

“현명하신 분이었습니다.”

“물론 네놈보다 똑똑하기도 했다. 적어도 조부뻘 되는 사람 앞에서 버르장머리 없게 부채질하진 않았으니. 그 부채 부숴 버리기 전에 당장 접어라.”

“쉽게 부서질 만한 물건이 아닙니다. 만년한철을 두 냥이나 넣었거든요.”

“네놈 골통도 만년한철이냐?”

“아, 그렇군요. 가르침 감사합니다.”

냉큼 부채를 접은 제갈풍이 동굴을 둘러보며 입을 열었다.

“한데 이곳에는 어인 일로 오셨습니까? 이미 수색도 끝나 아무도 찾지 않는 곳인데.”

“그러니 온 것이다. 노부야 기관진식에는 문외한이니, 나름대로 준비를 해야지.”

준비라는 말에 제갈풍의 눈썹이 슬쩍 올라갔다.

“전투가 벌어질 거라 생각하시는군요.”

“항상 싸움을 대비하는 것이 무인의 자세. 더군다나 암천이라는 놈들은 잔학무도하고 집요하다. 이 정도로는 끝나지 않아.”

적천강의 목소리는 무거웠다.

암천에 의해 법왕 굉도라는 절친했던 벗을 잃은 그다.

하남과 사천의 혈사가 낳은 수많은 죽음은 과거 일어났던 정마대전을 떠올리기에 충분했다.

“사천당문의 지하 뇌옥에 천력마(天力魔)가 갇혀 있었다는 이야기는 알고 있으리라 생각한다.”

“물론입니다. 그가 진 소협을 통해 암천을 마교의 후신(後身)이라 칭하고 죽음을 맞이했다는 것 역시.”

천하의 패권을 두고 벌어진 정마대전은 정파의 승리로 막을 내렸지만, 그것은 대승이 아니라 상처뿐인 승리였다.

만약 당시의 정파에 충분한 여력이 남았다면 퇴각하는 마교의 군세를 추격하여 모든 뿌리를 뽑았을 것이다.

하지만 천마신교와 정파. 두 용과 호랑이는 종전과 동시에 대부분의 힘을 잃었고, 오십여 년이라는 긴 공백의 시간은 도망친 패자가 다시 일어나기에 충분한 시간이었다.

암천(暗天)이라는 새로운 이름으로.

“어느덧 세월이 이렇게 흘렀구나. 돌고 돌아 또다시 난세가 찾아오고 말았어.”

적천강의 나직한 목소리에 제갈풍은 문득 고개를 들었다.

천장의 틈 사이로 보이는 하늘은 어둡고 혼란했다. 당장 내일 저 먹구름이 사라지고 하늘이 푸르게 걷힌다 해도, 흐트러진 천기는 천하의 그 어떤 복자(卜者)도 읽어 낼 수 없을 것이다.

‘난세.’

바야흐로 돌고 돌아 찾아온 난세였고, 환란의 시대는 눈앞까지 들이닥쳤다.

피가 강을 이루고 시체가 산처럼 쌓일 것이다.

죽음과 파괴가 곳곳에서 자행되니 부모 잃은 고아가 천하를 떠돌 것이며, 썩어 가는 시신을 처리하지 못해 역병이 창궐하고 기근이 들 것이다.

‘지금 벌어지는 일은 그 일부분에 불과하다.’

그 사실을 다시 한번 깨달은 제갈풍은 오싹 소름이 돋았다. 하지만 그것은 비단 암천의 존재 때문만은 아니었다.

“선객이 있었군.”

귓가를 파고드는 누군가의 목소리. 제갈풍은 창졸간에 얼음물을 뒤집어쓴 사람처럼 우뚝 굳어 버렸다.

‘어떻게?’

비록 초절정의 경지에 이르지는 못했으나 제갈풍 역시 절정의 끝자락에 다다른 고수.

그런 그가 어떤 기척도 느끼지 못했다. 소리도 들을 수 없었다.

언제나 그림자처럼 따라다니는 호위 셋을 동굴 앞에 세워 두고 왔음에도 아무런 징조를 느끼지 못했다는 것은, 목소리의 주인이 최소 초절정의 고수라는 뜻이다.

‘그 정도의 고수라면…….’

마주 보고 있는 적천강을 제외하면 무당파의 현공진인 뿐.

하지만 들려오는 목소리는 턱없이 젊고 맑았다. 마치 소년의 그것처럼.

‘아.’

제갈풍은 섬전 같은 깨달음과 함께 돌아섰다.

몇 번인가 스치듯이 마주했던 소년 의생을 마주한 순간, 머릿속에 가득했던 안개가 흩어지고 한 사람의 별호가 입술 사이로 흘러나왔다.

“살성(殺星).”

소년 의생, 문경의 눈썹이 꿈틀거렸다.

“이미 알고 있었나?”

“몰랐습니다. 방금까지는.”

제갈풍은 흥분한 목소리로 말을 이었다.

“하지만 고금제일의 살수가 사라진 이유에 대해서는 늘 의문이 남았지요. 어찌하여 신의라는 걸출한 의생이 정마대전이 끝난 후에야 등장했는가에 대해서도.”

“제법이군.”

“유심히 지켜본 적도 있었습니다만, 설마하니 반로환동의 경지에 드셨을 줄은 몰랐습니다.”

살성은 알려진 바가 거의 없는 미지의 인물.

번쩍이는 눈동자로 문경을 바라보던 제갈풍이 문득 멈칫했다.

“한데 어째서 굳이 제게…… 혹시?”

“눈치도 빠르고. 제갈가의 핏줄다워.”

“아무래도 피는 못 속이는 법이지. 약간 이상한 것 같긴 해도 똘똘한 놈이야. 제갈공후가 손주 놈을 잘 키운 게야. 자, 그건 그렇고…….”

어깨를 으쓱한 적천강이 문경을 응시하며 말을 이었다.

“무슨 일인가? 어울리지도 않게 어린애 흉내나 내던 늙은이가 이리 다급하게 찾아온 연유가.”

“짧게 말하지. 지금 당장 이곳을 떠나야 한다.”

“뭐라?”

문경이 말했듯이, 그의 말은 너무나도 짧았다.

그리고 그것은 적천강에게 있어 저 빌어먹을 천령폭을 넘을만한 이유가 되기에는 턱없이 부족했다.

“그게 무슨 개소리…….”

“더 짧게 말해 줄 필요가 있겠군.”

문경이 깊게 가라앉은 목소리로 말을 이었다.

“네 제자가 위험하다. 아니, 어쩌면 모두가.”

“……!”

그 말을 들은 순간, 적천강은 더 이상의 어떤 이유도 필요하지 않음을 깨달았다.

고개를 돌려 제갈풍을 바라보는 그의 노회한 눈동자에는, 어느새 푸른 불꽃이 깃들어 있었다.

“배를 띄워라. 지금 당장.”



* * *



마지막 장소에 도착했을 무렵, 동정호의 강물은 자줏빛으로 물들어 있었다.

절벽과 기암괴석(奇巖怪石)의 틈새로 비추는 석양을 바라본 내가 입을 열었다.

“지금부터 함부로 움직이지 마. 나룻배는 안전한 곳에 묶어 두고, 땅으로 이동해서 만약의 사태를 대비해.”

동정호는 호수지만 그 크기는 호수라고 부를 수 없을 만큼 광활하다.

사방에 물만 있는 것이 아니라 작은 섬, 혹은 장강의 지류에서 흘러들어온 흙과 모래가 쌓여 축적된 평평한 지면도 어렵지 않게 볼 수 있었다.

‘만약 전투가 시작된다면, 육지 위에서 싸우는 것이 훨씬 유리하다.’

이중 수공을 익힌 사람은 아무도 없다.

그나마 내가 [수상 구조대원]의 칭호 효과로 수중에서도 자유롭게 이동할 수 있긴 하지만, 무공의 위력이 20%나 감소하는 디버프를 피할 수는 없었다.

‘만약 상황이 안 좋게 흘러간다면…… 최소한 육지에서 대응할 수 있어야 해.’

이런 내 생각을 모를 리 없는 녀석들이다.

궁기방이 결연한 표정으로 입을 열었다.

“함께 가지.”

“헤엄칠 줄 아냐?”

“개헤엄 조금 한다.”

“개처럼 맞기 전에 육지로 가라.”

“음. 그게 나을 것 같군.”

궁기방이 뒤로 물러나자 이번에는 혁무진이 나섰다.

“조장님.”

“넌 육지에서도 몸 사리고 숨어 있어. 괜히 나서 봤자 별 도움 안 된다.”

“저도 압니다. 그냥 힘내시라고 불러 봤습니다.”

“…….”

저런 시부럴 놈. 그나마 있던 힘도 쭉 빠질 지경이다.

작게 한숨을 내쉰 나는 마지막으로 청풍을 향해 신신당부했다.

“저 안에 동정어옹이 없을 수도 있고, 있을 수도 있어. 하지만 만약 내가 놈을 발견해서 밖으로 끌어낸다면…….”

청풍이 고개를 끄덕였다.

“기회를 놓치지 않을게요.”

“그래. 그거면 돼.”

동정어옹이 얼마나 대단한 고수인지는 몰라도, 청풍의 도움이 있다면 일이 훨씬 수월해진다.

‘물론 이곳에도 없을 수 있겠지만.’

하지만 뭐랄까. 이번에는 뭔가 다르다. 이건 이성이 아니라 본능의 영역이다. 사람들을 차례차례 바라본 나는, 망설임 없이 자줏빛 강물을 향해 뛰어들었다.

촤악!

익숙한 느낌과 동시에 시스템 알림이 울렸다. 칭호 효과에 따라 평범하던 손과 발에 투명한 물갈퀴가 생성되고, 호흡이 편안해진다.

‘더, 깊숙이.’

나는 멈추지 않고 계속해서 나아갔다. 차가운 강물과 수많은 물고기를 지나쳐 빠르게 헤엄치던 그때였다.

‘저건…….’

저 멀리, 시커먼 동혈(洞穴)이 모습을 드러냈다.
```

## Final English reading copy

```markdown
# Chapter 463

Deep within a dark cave where a faint light seeped in, a small old man sat cross-legged, contemplating himself.

An energy like the sun raced through hundreds of acupoints and into the Eight Extraordinary Meridians. Tangible energy rose and enveloped the old man’s entire body.

Then, the changes began.

*Whoooooosh.*

Three flower buds bloomed above the old man’s snow-white hair before soon disappearing.

As the buds formed, the scattered energy created a new shape: five rings radiating a dazzling spectrum of colors.

It was a phenomenon that could only be displayed by one of the chosen few among Supreme Peak masters who had reached the realm of Five Qi Returning to Origin.

But the changes surrounding the old man did not end there.

*Fwoosh. Hissssss!*

The five rings symbolizing Five Qi Returning to Origin turned red. Tremendous flames erupted from the rings of internal energy filled with Scorching Yang Qi, wrapping around the old man before soon taking on a blue hue.

Furnace Fire Pure Blue.

When the fire in a furnace grew hot enough, it turned blue. The realm of martial arts the old man had achieved was the same.

It would not have been an exaggeration to say that the internal energy and insight he had accumulated over more than a hundred years had already reached the ultimate.

And yet…

*Is this as far as I go?*

The old man, Fire King Jeok Cheongang, withdrew his internal energy. The figure that had been floating cross-legged in the air descended until his body touched the ground, and the strange phenomenon surrounding him vanished as though it had been washed away.

The only thing left in the quiet space was Jeok Cheongang’s hollow chuckle.

“Heh heh.”

Why could he not break through the wall before him and advance any farther?

Because he knew that fact better than anyone, Jeok Cheongang nodded, yet the unmoving wall still seemed bitterly unfortunate. At times, he even resented the heavens.

But instead of furrowing his brow, Jeok Cheongang soothed his bitterness with a laugh.

*What is there to resent? This old man brought it upon himself.*

Martial arts grew stronger through ceaseless training, while insight only came when one emptied the heart.

But Jeok Cheongang had been unable to clear away the filth that had accumulated in his heart over the past several decades.

Anything that piled up and stagnated would eventually rot. With his rotting heart filled with afflictions, an inner demon had come for him, and once the inner demon arrived, he could no longer prevent the infirmities of old age.

“If I hadn’t met that brat… I’d probably be smearing shit all over the walls by now. Heh heh.”

Jeok Cheongang let out a hearty laugh.

With one realization—just one small realization—he might be able to reach the realm of Returned to Youth.

But he knew that this, too, was greed. It was proof that he had not completely emptied his heart.

When he suddenly looked up, he saw the sky through a small opening. Jeok Cheongang spoke to someone invisible beyond it.

“Does this mean I should be satisfied with this? Is that right?”

No answer came back.

No… Perhaps he had already received his answer.

He had taken a killer demon by nature as his disciple and allowed innocents to die. But thanks to his second disciple, he had at least been able to preserve his sanity. The answer was that he should no longer cling to anything.

There was no one to give him that answer, yet Jeok Cheongang heard it coming from within his own heart.

“What a fucking joke. After all the fiends this old man has dealt with, this is the shabby treatment I get?”

Jeok Cheongang sighed in complaint and lowered his head before continuing.

“Don’t you think so?”

One person stood at the end of Jeok Cheongang’s gaze. Crouching Dragon Guest Zhuge Feng answered while waving his folding fan.

“Once, when I was nine, my grandfather sat me beside him and said something similar. ‘I don’t know what kind of bastard is up there, but he must have a truly god-awful temper.’ Senior, you’re saying the same thing now.”

Jeok Cheongang nodded.

“Zhuge Gonghu did occasionally say something right.”

“He was a wise man.”

“He was smarter than you, of course. At least he didn’t wave his fan insolently in front of someone old enough to be his grandfather. Fold that thing before I break it.”

“It is not an object that breaks easily. I put two nyang of Ten-Thousand-Year Cold Iron into it.”

“Is your skull made of Ten-Thousand-Year Cold Iron too?”

“Ah, I see. Thank you for the instruction.”

Zhuge Feng promptly folded his fan, then looked around the cave and spoke.

“But what brings you here? The search has already ended, and no one comes here anymore.”

“That is precisely why I came. I’m no expert when it comes to mechanisms and formations, so I need to make preparations in my own way.”

At the word *preparations*, Zhuge Feng’s brow rose slightly.

“You think a battle will break out.”

“A martial artist should always prepare for a fight. Besides, those bastards from Dark Heaven are cruel, lawless, and persistent. This will not end here.”

Jeok Cheongang’s voice was heavy.

Dark Heaven had taken the life of his close friend, Dharma King Hong Dao.

The countless deaths caused by the bloodshed in Henan and Sichuan were more than enough to remind him of the Great Faction War.

“I assume you know that the Heavenly Power Demon was imprisoned in the underground prison beneath the Sichuan Tang Clan.”

“Of course. I also know that, through Young Hero Jin, he called Dark Heaven the successor of the Demonic Cult before meeting his death.”

The Great Faction War, fought over supremacy in the world, had ended with victory for the orthodox factions. But it had not been a sweeping victory. It had been a victory marked only by wounds.

If the orthodox factions of that era had retained enough strength, they would have pursued the retreating armies of the Demonic Cult and torn out every last one of its roots.

But the Heavenly Demon Divine Cult and the orthodox factions—the two great powers, like a dragon and a tiger—had lost most of their strength as soon as the war ended. And the long gap of more than fifty years had been enough time for the defeated side that escaped to rise again.

Under a new name.

Dark Heaven.

“Time has passed like this before we even realized it. The wheel has turned, and troubled times have come again.”

At Jeok Cheongang’s quiet voice, Zhuge Feng suddenly looked up.

The sky visible through the gaps in the cave ceiling was dark and chaotic. Even if the black clouds vanished tomorrow and the sky cleared to blue, the heavenly patterns had already been thrown into such disorder that no diviner in the world would be able to read them.

*Troubled times.*

The age of turmoil had finally returned after completing its long circle, and the era of calamity had already reached their doorstep.

Blood would form rivers, and corpses would pile up like mountains.

Death and destruction would be carried out everywhere. Orphans who had lost their parents would wander the world, while epidemics and famine would spread because there would be no one to dispose of the rotting corpses.

*What is happening now is only a small part of it.*

Zhuge Feng realized that fact once more and felt a chill run over his skin.

But Dark Heaven’s existence was not the only reason.

“I see you already had a guest.”

A voice pierced his ears.

Zhuge Feng froze on the spot as though someone had poured ice water over him.

*How?*

Although he had not reached the Supreme Peak realm, Zhuge Feng was still a master at the very edge of Peak.

Yet he had sensed no presence. He had heard no sound.

Even though he had left three guards who followed him like shadows at the entrance to the cave, he had noticed no sign of anything.

That meant the owner of the voice was at least a Supreme Peak master.

*If he is that kind of master…*

Aside from Jeok Cheongang, the only possibility was Perfected Being Hyeongong of Wudang.

But the voice he heard was far too young and clear.

It sounded almost like a boy’s voice.

*Ah.*

With a flash of insight, Zhuge Feng turned around.

The instant he saw the young medical apprentice he had encountered several times in passing, the fog filling his mind scattered, and a sobriquet slipped from between his lips.

“The Slaughter Saint.”

The young medical apprentice, Mungyeong, twitched an eyebrow.

“You already knew?”

“I did not. Not until just now.”

Zhuge Feng continued in an excited voice.

“But I have always wondered why the greatest assassin in history disappeared. I also wondered why the exceptional physician known as the Divine Physician only appeared after the Great Faction War ended.”

“Not bad.”

“I once watched you closely, but I never imagined that you had reached the realm of Returned to Youth.”

The Slaughter Saint was an unknown figure about whom almost nothing was known.

Zhuge Feng stared at Mungyeong with gleaming eyes before suddenly hesitating.

“But why would you deliberately reveal yourself to me… Unless?”

“You’re quick to notice things. You really are a member of the Zhuge Clan.”

“You can’t fool blood, after all. He may be a little strange, but he’s a clever boy. Zhuge Gonghu raised his grandson well. Now, putting that aside…”

Jeok Cheongang shrugged and continued while staring at Mungyeong.

“What brings you here? Why has an old man who had been pretending to be a child, despite it not suiting him at all, come here in such a hurry?”

“I’ll keep it short. You must leave this place immediately.”

“What?”

As Mungyeong had said, his words were extremely brief.

And to Jeok Cheongang, they were nowhere near enough reason to cross that godforsaken Tianling Falls.

“What kind of bullshit is—”

“I should make it even shorter.”

Mungyeong continued in a deeply sunken voice.

“Your disciple is in danger. No. Perhaps everyone is.”

“……!”

The moment he heard those words, Jeok Cheongang realized that he needed no further reason.

He turned his head toward Zhuge Feng. Blue flames had already kindled in his aged eyes.

“Launch the boat. Right now.”

* * *

By the time we reached the final location, the waters of Dongting Lake had turned purple.

I looked at the sunset shining through the gaps between the cliffs and strange, jagged rocks before speaking.

“Don’t move recklessly from now on. Tie the ferryboat somewhere safe, then move overland and prepare for anything.”

Dongting Lake was a lake, but it was so vast that calling it a lake hardly seemed adequate.

It wasn’t all water in every direction; small islands and flat stretches of ground formed from mud and sand carried in by tributaries of the Yangtze were easy enough to find.

*If a battle starts, it will be much more advantageous to fight on land.*

Not one of us had mastered water arts.

I could at least move freely underwater thanks to the Water Rescue Worker Title’s effect, but I could not avoid the debuff that reduced my martial arts’ power by twenty percent.

*If the situation turns bad… I need to be able to respond from land, at the very least.*

The others understood my thinking perfectly well.

Gung Gibang spoke with a determined expression.

“I’ll go with you.”

“Can you swim?”

“I can dog-paddle a little.”

“Go to land before you get beaten like a dog.”

“Hmm. That probably is better.”

Gung Gibang stepped back, and Hyuk Mujin came forward.

“Captain.”

“You stay on land too. Hide and keep out of trouble. You won’t be any help if you charge in for no reason.”

“I know. I only called out to encourage you.”

“……”

What a sibu-leol bastard. I felt like even the little strength I had left was draining away.

I let out a small sigh, then gave Cheongpung one last earnest warning.

“The Dongting Fisherman may or may not be inside. But if I find him and drag him outside…”

Cheongpung nodded.

“I won’t miss the opportunity.”

“Good. That’s all I need.”

I did not know how formidable the Dongting Fisherman was, but with Cheongpung’s help, things would be much easier.

*Of course, he might not be here either.*

But how should I put it? This time felt different.

It was not a matter of reason. It was instinct.

I looked at each person in turn, then leaped without hesitation into the purple water.

*Splash!*

Along with the familiar sensation, a System notification rang out.

In accordance with the Title’s effect, transparent webbing formed between my ordinary fingers and toes, and breathing became effortless.

*Deeper. Further in.*

I continued forward without stopping.

I swam rapidly through the cold water and past countless fish.

Then, just as I was moving through the depths, something appeared in the distance.

*What’s that…?*

Far ahead, a pitch-black cave came into view.
```

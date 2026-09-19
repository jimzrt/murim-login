<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0448.txt",
      "sha256": "349350243ec6b378023e460e43d9d8278bfc81bde1d1490f5c7c90c707771936",
      "bytes": 13894
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "a1af74e30c7f1e9ec96451583f9d3b303543f2a86e2e738a513c2d5ad32b9502",
      "bytes": 3549
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "dd2d41b94e4eccce70e6817541718c7e2265bf9961d5735641bfcc6c7a54fe1b",
      "bytes": 146879
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "3310cef5c46d6230e2eba0bcaef19519ad2bf9422aeec2d994cc110fc80d385b",
      "bytes": 944
    },
    {
      "path": "characters/Gung Gibang.md",
      "sha256": "25a3948b0ac60751451872b75ceb5bd929a132a38ee9085d4e1abd584985f364",
      "bytes": 609
    },
    {
      "path": "characters/Human Butcher.md",
      "sha256": "a54c86c8f8306f3b78d4c522636d8904c6975e0676d5bc03e16f7b54b74acca4",
      "bytes": 667
    },
    {
      "path": "characters/Hwang Chung.md",
      "sha256": "a9d7e04efaedb7b4e3d3261f945cceead5783dc1479140d0c7ccca0478c04864",
      "bytes": 609
    },
    {
      "path": "characters/Hyeongong.md",
      "sha256": "1a82811f60bcbe309680ce9564415fdb96843dbdbe8bc0e1f51c4cbc29fcb122",
      "bytes": 735
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "cab35c84f78aba6ee15d49cd5af5c2c9c6ba450c3077386dbf703f0e452c9b60",
      "bytes": 1108
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "27c031435106d878226384f03f2217e673b9b18957330bfdb50db84657dd8941",
      "bytes": 1422
    },
    {
      "path": "characters/Jin Wikyung.md",
      "sha256": "718f96a8663fa9c6965d6b87e0cb9b6def562b6108d451bc5dbe5deda941ea26",
      "bytes": 1239
    },
    {
      "path": "characters/Mu Song.md",
      "sha256": "4a6289795ed8322936b36e4cf31a5f953a17bf8e1fedcd839beb3a6cee25d2fa",
      "bytes": 870
    },
    {
      "path": "characters/Mungyeong.md",
      "sha256": "591e86732d43b4887025992d5546b3f9e9450545d57241f3b954b11086268051",
      "bytes": 686
    },
    {
      "path": "characters/Zhuge Feng.md",
      "sha256": "8c93c06c6b0e5bf27c81d64de93c2c326866176ed1b0a47aa18d95e2e97fda5f",
      "bytes": 626
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "d58dfc7ac3f231bf414a16269e60d467bebfb8fab1836710ebfb69735a2cf41c",
      "bytes": 142093
    }
  ],
  "estimated_tokens": 13804
}
-->

# Durable State Update — Chapter 448

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 448. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 448. Profile updates may replace only one
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
  "chapter": 448,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 448,
    "continuity_sources": [448],
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
    "Taekyung accepted the Quest Another Chaos to uncover the truth behind the Hubei incidents and find the culprit.",
    "Jin Wikyung is acting as an inspector for the new Murim Alliance, and Taekyung is cooperating with his investigation.",
    "The shared symbols between the Arch Lich's magic circle and Dark Heaven's formations remain unexplained and may relate to black magic.",
    "The Sea Serpent Society was destroyed at Red Cliffs, the Dongting Fisherman disappeared after condemning the Yangtze River Channel League, and the League is implicated only by circumstantial evidence.",
    "Dangyang Stronghold and Honghu Stronghold vanished after taking control of Sea Serpent Society territory, while Donghu Stronghold remains inaccessible beyond Tianling Falls.",
    "Hwang Chung, the Yangtze One Saber, is the Seafaring King's sworn brother, a moderate-faction elder, and Lord of Donghu Stronghold; his involvement remains unproven.",
    "The Dongting Fisherman's broken Black Bamboo Fishing Rod was found, and Zhuge Feng ordered Mu Song to guide the group to Donghu Stronghold.",
    "Mungyeong remains with Taekyung's group while concealing his former Divine Physician and Slaughter Saint identity from most companions.",
    "The Skeleton King's undead identity remains concealed from the public, and Taekyung has ordered him to join Peace Guild under a prepared contract.",
    "Go Jun is expected to succeed Lee Jungryong as Ares Guild's captain and is searching China for Lee's holographic recorder.",
    "Taekyung's group is traveling toward Donghu Stronghold aboard four Water Dragon Stronghold fast ships with elite Zhuge Clan and Wudang disciples.",
    "The group has reached Tianling Falls, where the fast ship has been struck by the deadly whirlpool guarding Donghu Stronghold's route."
  ],
  "continuity_sources": [
    447,
    446
  ],
  "open_questions": [
    "What are the origin and purpose of the symbols shared by the Arch Lich's magic circle and Dark Heaven's formations, and are they connected to black magic?",
    "Why does Mungyeong continue accompanying Taekyung's group despite being unable to explain the impulse?",
    "What confidential matter is Jin Wikyung withholding?",
    "What are the terms of the Peace Guild–Wizard Guild agreement, and what evidence is contained in Lee Jungryong's holographic recorder?",
    "Who destroyed the Sea Serpent Society, caused the disappearances of the Yangtze River Channel League strongholds and Dongting Fisherman, and what happened inside Donghu Stronghold?"
  ],
  "safe_through": 447,
  "temporary_decisions": [
    "Render 황충 as Hwang Chung, 장강일도 as Yangtze One Saber, 천령폭 as Tianling Falls, and 흑죽조간 as Black Bamboo Fishing Rod.",
    "Render 시부럴 as “sibu-leol,” 시벌좌 as “Lord Fuck,” and 시부럴좌 as “Lord Sibu-leol.”",
    "Preserve the Skeleton King's grandiose, mock-offended voice and Taekyung's dry, profane humor.",
    "Render 최 팀장님 as “Team Leader Choi,” 진태경 씨 as “Mr. Jin Taekyung,” 막내야 as “my youngest,” 노야 as “Old Master,” and 노 선배님 as “Senior.”",
    "Keep Peace Guild, guild house, Inventory, Magic Johnson, established martial-arts terminology, black magic, poison human, World Hunter Association, Wizard Guild, Sea Serpent Society, Red Cliffs, and Dongting Fisherman unchanged; render 현공진인 as “Perfected Being Hyeongong” and 화왕질리언 as “Fire King Zilean.”"
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
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 해상왕    | **Seafaring King**            | Pa Ryun        |
| 열화문    | **Fire Gate Clan**               |
| 화산파    | **Huashan**                      |
| 무당파    | **Wudang**                       |
| 제갈세가   | **Zhuge Clan**                   |
| 장강수로맹  | **Yangtze River Channel League** |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무인     | **martial artist**                               | Default term                                          |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 장문인    | **Sect Leader**                              |
| 제자     | **Disciple**                                 |
| 생도     | **cadet**                                    |
| 선배     | **Senior**                                   |
| 은인     | **Benefactor**                               |
| 화산     | **Huashan**            |
| 노부      | **this old man / I**                                            |
| 본가      | **our family / this family**                                    |
| 본문      | **our sect / this sect**                                        |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 궁기방 | **Gung Gibang** | Beggars' Sect Successor Beggar and finalist. |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 황충 | **Hwang Chung** | Lord of Donghu Stronghold, the Seafaring King's sworn brother, and the Yangtze One Saber. |
| 현공진인 | **Perfected Being Hyeongong** | Veteran Wudang Daoist master and the current Sect Leader's Junior Brother. |
| 무송 | **Mu Song** | Lord of Water Dragon Stronghold and disciple of the Seafaring King. |
| 문경 | **Mungyeong** | Young medical apprentice and newly introduced passenger. |
| 제갈풍 | **Zhuge Feng** | Current Family Head of the Zhuge Clan. |
| 화염신장 | **Flame Divine Palm** | Jopil's deadly palm technique, noted when Taekyung compares Jopil with Mukyung. |
| 대한민국 | **Korea** | Country reference. |
| 송이 | **Song-i** | Short form used for Song Song; Taekyung's love interest. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 오대세가 | **Five Great Families** | Major Murim grouping. |
| 태을미리장 | **Taeeul Miri Palm** | Palm technique taught to Cheongpung by Mae Jonghak. |
| 기해 | **qi sea** | Name for the dantian, the place where internal energy begins and gathers. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 도도 | **Dodo** | Term for the Star-Array Grand Banquet's major gambling matches. |
| 태극혜검 | **Taiji Wisdom Sword** | Wudang’s supreme sword technique. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 허공답보 | **Stepping on Empty Air** | Technique that allows Jongni Chu to move through empty air as if climbing invisible stairs. |
| 노야 | **Old Master** | Taekyung's private address for Jeok Cheongang. |
| 한강 | **Han River** | River associated with the bridge-collapse incident Lee Jungryong recalls. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 전광석화 | **Quick Attack** | Warlordmon’s rapid-movement command; used as a Pokémon-style gag. |
| 전광 | **Quick Attack** | Shortened form of Warlordmon’s rapid-movement command. |
| 수룡채 | **Water Dragon Stronghold** | Major river stronghold belonging to the Yangtze River Channel League. |
| 채주 | **Stronghold Lord** | Title used for the lord of a water stronghold. |
| 장강 | **Yangtze** | The river controlled by the Yangtze River Channel League. |
| 의생 | **medical apprentice** | Mungyeong's occupation. |
| 등평도수 | **Rising on Duckweed, Crossing Water** | Comparable movement feat for walking across water. |
| 오대 | **Five Squads** | Named Tang Clan organizational group in Tang Sadok's mobilization order. |
| 동정채 | **Donghu Stronghold** | Stronghold where Mu Song's Uncle Hwang is based. |
| 와룡객 | **Crouching Dragon Guest** | Epithet of Zhuge Feng. |
| 장강일도 | **Yangtze One Saber** | Hwang Chung's sobriquet. |
| 천령폭 | **Tianling Falls** | Dangerous waterway leading to Donghu Stronghold. |

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
| 무인 | 진위경 | vassal_martial_artist_to_lesser_family_head | Lesser Family Head | formal-deferential | The Mount Heng martial artists greet Jin Wikyung as 소가주님 while pledging loyalty. |
| 진위경 | 적천강 | host_to_legendary_guest | Great Hero Jeok | formal-deferential | Introduces himself and pays respects to Jeok Cheongang as the Fire King. |
| 적천강 | 진위경 | elder_to_younger_family_head | you | gruff and teasing | Uses 자네 while mistaking Wikyung for Taekyung’s father and questioning his age. |
| 수하 | 채주 | subordinate_to_stronghold_lord | Stronghold Lord | deferential | The subordinate calls Mu Song 채주 while reporting the nearby vessel. |
| 문경 | 무송 | survivor_to_savior_and_authority | Great Hero Mu Song | formal-deferential | Mungyeong credits Mu Song with saving him and asks him to spare Hwang Tae-gu. |
| 무송 | 문경 | stronghold_lord_to_young_passenger | you | gruff-but-considerate | Mu Song offers Mungyeong the right to decide Hwang Tae-gu's fate. |
| 청풍 | 문경 | martial_companion_to_medical_apprentice | Medical Apprentice | cheerful-polite | Cheongpung addresses Mungyeong as 의생님 while asking him to greet the Tang Clan. |
| 혁무진 | 궁기방 | squad_companion_to_Beggars_Sect_successor | Young Hero Gung | formal-polite, then pointed | Uses 궁 소협 while asking about the culprit and challenging Gung’s insults. |
| 문경 | 적천강 | old_acquaintances | Fire King | familiar and grave | The figure bearing Mungyeong’s name greets Jeok Cheongang by his established epithet. |
| 궁기방 | 혁무진 | squad_companions | you; that lunatic | insulting-casual | Gung Gibang mocks Hyuk Mujin's injuries and calls him a lunatic for attacking the Third Fiend. |
| 궁기방 | 청풍 | martial_companions | Young Hero Cheongpung | formal-polite | Gung Gibang uses 청 소협 while asking why Cheongpung is at the temporary clinic. |
| 무송 | 적천강 | junior_martial_artist_to_legendary_martial_master | Great Hero Jeok | formal-deferential | Mu Song respectfully refers to Jeok Cheongang as 적 대협 while worrying that Jeok dislikes him. |
| 적천강 | 문경 | overwhelming elder to old acquaintance | you / little punk | mocking and threatening | Mocks Mungyeong's expression and threatens to poke out his eyes. |
| 적천강 | 무송 | legendary martial master to stronghold lord | you | gruff, coercive, and dismissive | Uses 자네 while ordering Mu Song to take the group only as far as Sichuan and leave the fast ship. |
| 청풍 | 무송 | young martial companion to stronghold lord | you | cheerful and familiar | Offers Mu Song his last dumpling and then induces him to buy more in Guang'an. |
| 적천강 | 제갈풍 | senior_martial_artist_to_old_acquaintance | you / ill-mannered brat | blunt, familiar, and teasing | Jeok treats Zhuge Feng as the younger acquaintance he remembers from childhood. |
| 제갈풍 | 적천강 | younger_old_acquaintance_to_legendary_senior | Senior | respectful but relaxed | Zhuge Feng recalls Jeok's earlier visit and addresses him as an old senior. |
| 제갈풍 | 무송 | family_head_to_stronghold_lord | Ship-Fire Boy Mu Song | calm, formal, and pointed | Zhuge Feng stops Mu Song from leaving by saying the coming information concerns him. |
| 무송 | 제갈풍 | stronghold_lord_to_orthodox_family_head | Great Hero Zhuge | formal and concerned | Mu Song addresses Zhuge Feng after realizing why he was asked to remain. |
| 제갈풍 | 궁기방 | family_head_to_beggars_sect_successor | Successor Beggar | calm and conversational | Uses 후개 when confirming Gung Gibang's guess about the broken weapon. |
| 현공진인 | 제갈풍 | senior Wudang master to Zhuge Clan Family Head | Family Head Zhuge | formal-respectful | Uses 제갈가주 while discussing the fast ship and the route. |
| 제갈풍 | 현공진인 | Zhuge Clan Family Head to senior Wudang master | Perfected Being Hyeongong | formal-deferential | Addresses Hyeongong with marked respect and calls his presence a great reinforcement. |
| 궁기방 | 무송 | martial companion to Stronghold Lord | Senior Mu Song | pleading-deferential | Begins pleading for Mu Song to save them from Tianling Falls. |

## Listed compact profiles

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 447
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, the grandson and Disciple of Sword Saint Mae Jonghak, and a Supreme Peak martial master known as the Huashan Divine Dragon.
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, a deep love of martial arts, and a martial artist's competitive pride; he becomes unsettled when someone copies his martial arts
- **Voice:** Dreamy and hazy, with innocent, polite phrasing
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions while Taekyung is his only true martial rival; Tang Sadok has temporarily entrusted Mimi to him.

### Gung Gibang.md

# Gung Gibang (궁기방)

- **Safe through:** Chapter 447
- **Aliases:** Successor Beggar, Beggar Prince, pure-blooded beggar, ultimate beggar
- **Role:** Gung Gibang is the Beggars' Sect Successor Beggar and a unique eight-knot disciple.
- **Personality:** Vulgar, aggressive, and quick-tempered.
- **Voice:** Blunt, profane, and vividly threatening.
- **Relationships:** Rival finalist alongside Baek Woo and Zhuge Gyun; trades insults with Taekyung and is helping investigate Tang Taesang’s murder through Beggars’ Sect intelligence.

### Human Butcher.md

# Human Butcher (인도)

- **Safe through:** Chapter 435
- **Aliases:** None
- **Role:** Former mysterious Han Chinese mounted-bandit power in Northern Gaoyuan commanding fifty subordinates; a Peak master killed by an unnamed old man in a single move
- **Personality:** Cold, intimidating, and murderous; he kills people as though slaughtering livestock
- **Voice:** Cold, curt, and quietly threatening
- **Relationships:** He is one of four powerful participants at the Northern Gaoyuan gathering, intimidates Temur, and has claimed Ghost Sword Wipeng as his personal target in the proposed attack

### Hwang Chung.md

# Hwang Chung (황충)

- **Safe through:** Chapter 446
- **Aliases:** Yangtze One Saber
- **Role:** Hwang Chung is the Lord of Donghu Stronghold, a moderate-faction elder of the Yangtze River Channel League, and the Seafaring King's sworn brother.
- **Personality:** Calm, clever, and supportive of the orthodox faction during the Great Faction War.
- **Voice:** Not established.
- **Relationships:** Hwang Chung helped the Seafaring King establish the Yangtze River Channel League and is regarded by Mu Song as an uncle and trusted senior.

### Hyeongong.md

# Perfected Being Hyeongong (현공진인)

- **Safe through:** Chapter 447
- **Aliases:** None
- **Role:** Perfected Being Hyeongong is a veteran Wudang Daoist master of the previous generation, the current Sect Leader's Junior Brother, and a Supreme Peak swordsman who reached the ultimate stage of the Taiji Wisdom Sword.
- **Personality:** Hyeongong is humble and self-deprecating about his limited worldly knowledge while carrying the authority of an experienced senior master.
- **Voice:** Measured, respectful, and lightly self-deprecating.
- **Relationships:** Hyeongong is the current Wudang Sect Leader's Junior Brother and a respected senior to Zhuge Feng.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 447
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers and Vice Squad Leader of the Jin Dragon Squad.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 447
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is a legendary wandering martial master and Jin Taekyung's Master.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, and pathologically afraid of water. His meeting with Taekyung rekindled his will to live, making him determined to extend his life despite his illness.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Jin Wikyung.md

# Jin Wikyung (진위경)

- **Safe through:** Chapter 447
- **Aliases:** Junzi Sword
- **Role:** Jin Wikyung is the thirty-six-year-old Lesser Family Head and future Family Head of the Jin Family of Taiyuan, the Alliance Leader who unified Shanxi Murim and Shanxi Province's foremost landowner and magnate.
- **Personality:** Calm, authoritative, and politically capable in public; protective and affectionate toward Taekyung beneath a stern mask. Takes responsibility for his people, acts decisively under pressure, and prioritizes family survival.
- **Voice:** Restrained, formal, and commanding with subordinates; openly affectionate, proud, and occasionally exuberant with Taekyung.
- **Relationships:** Taekyung's eldest brother and future Family Head; Taekyung trusts him as a martial-arts mentor and family protector. Member and acting leader of the Jin Family of Taiyuan. Commands Wipeng and the family's forces. Has worked with Jeok Cheongang, who trained Taekyung under Wikyung's arrangement. Jin Mukyung is his younger brother and a potential successor alongside Taekyung.

### Mu Song.md

# Mu Song (무송)

- **Safe through:** Chapter 447
- **Aliases:** Ship-Fire Boy
- **Role:** Lord of Water Dragon Stronghold, a Peak master and the Seafaring King's second martial Disciple who controls major Yangtze river traffic in Sichuan and belongs to the Yangtze River Channel League's moderate faction.
- **Personality:** Ambitious, domineering, impatient with interruptions, and capable of pragmatic cooperation when circumstances demand it.
- **Voice:** Deep and low in private, shifting to dry authority or boisterous command when addressing subordinates and rivals.
- **Relationships:** Mu Song is a member of the Yangtze River Channel League's moderate faction; Hwang Chung, his senior and Uncle Hwang, is the League elder and Donghu Stronghold Lord whom Mu Song firmly believes is innocent.

### Mungyeong.md

# Mungyeong (문경)

- **Safe through:** Chapter 447
- **Aliases:** None
- **Role:** Mungyeong is the legendary physician known as the former Divine Physician and Slaughter Saint, having passed the Divine Physician title to his Disciple.
- **Personality:** Compassionate, resolute, resourceful, and calm under extreme pressure.
- **Voice:** His Mungyeong persona is timid, deferential, and cheerful, while his Slaughter Saint voice is dry, impassive, and blunt.
- **Relationships:** Dong Feng is his Disciple, while Jeok Cheongang, Jin Taekyung, Cheongpung, and the two Sect Leaders know his Slaughter Saint identity.

### Zhuge Feng.md

# Zhuge Feng (제갈풍)

- **Safe through:** Chapter 447
- **Aliases:** Crouching Dragon Guest
- **Role:** Zhuge Feng is the current Family Head of the Zhuge Clan and father of its Lesser Family Head, Zhuge Gyun.
- **Personality:** Analytical and disarmingly casual, he treats comfort and time as principles while delivering grave intelligence with unsettling directness.
- **Voice:** Clear, calm, polished, and conversational, with understated humor and pointed questioning.
- **Relationships:** Zhuge Gyun is his son, and Zhuge Gonghu was his grandfather.

## Korean source

```text
＃448화



단 한 걸음으로 수 장의 거리를 지우고, 텅 빈 허공을 밟고 뛰어오르며, 일권으로 절벽을 무너트린다.

옛날 전래동화에서나 나올 법한 이적(異蹟)을 가능케 하는 존재가 바로 초절정 고수다. 하지만…….

“꽉 잡, 으아아아아!”

콰아아앙!

이곳은 육지가 아닌 망망대해와도 같은 장강의 한복판.

반경 수백 장에 달하는 거대한 와류 앞에서, 내가 몸을 실은 쾌조선은 작은 나뭇잎에 불과했다.

쿠웅!

“어어어어어어!”

“으아아아아악!”

엄청난 수압이 쾌조선의 옆구리를 후려치자 거칠고 빠르게 나아가던 선체가 붕 뜨며 허공에서 기울어진다.

천천히 뒤집히는 세상 속, 내 상반신을 구명조끼라도 되는 양 힘껏 움켜쥔 진위경이 비명을 내질렀다.

“어머니! 지금 갑니다아아악!”

“가긴 어딜 가! 손 떼!”

“아버지! 보고 있다면 해답을 알려 줘어어억!”

해답은 시벌, 답도 안 나오네.

하지만 더욱 큰 문제는 진위경뿐 아니라 궁기방과 혁무진, 거기에 더해 제갈세가와 무당파의 제자들까지 반쯤 정신이 나갔다는 것이다.

그나마 아직 평정심을 유지하고 있는 것은 나를 비롯한 초절정 고수들뿐.

“으허! 으허어어어어! 물! 무울!”

“…….”

정정. 한 사람은 제외다.

나는 눈을 꽉 감은 채 고래고래 소리를 지르는 적천강을 붙잡고, 남은 한 손을 있는 힘껏 허공으로 내뻗었다.

‘화염신장(火焰神掌)!’

퍼엉!

강력한 공력의 파동에 압축된 공기가 터져 나간다.

칼날처럼 휘몰아치던 와류의 일부가 흩어지며, 수면을 향해 거꾸로 곤두박질치던 선체가 가까스로 중심을 잡았다.

하지만 안도하기에는 한참 일렀다.

낙하하는 쾌조선을 향해 제이, 제삼의 와류가 다가오고 있었으니까.

‘나 혼자로는 부족해. 이럴 때는…….’

번개처럼 머릿속을 스치는 생각과 함께, 나는 큰 목소리로 한 사람의 이름을 외쳤다.

“청풍!”

“네!”

다 안다는 듯이 고개를 끄덕인 청풍이 두 팔을 번쩍 들었다.

“끼얏호우!”

“아니, 끼얏호우 말고 이 미친놈아! 내가 했던 대로 하라고!”

“아아. 네, 은인!”

혼자서 월미도 디스코 팡팡을 즐기고 있던 청풍이 양 소매를 떨쳤다.

화산파가 자랑하는 절기, 태을미리장(太乙迷離掌)이 수십 개의 꽃잎으로 화해 허공을 후려쳤다.

퍼버벙!

파괴력으로는 화염신장을 따라올 수 없지만, 지금 같은 상황이라면 타격 범위가 훨씬 넓은 태을미리장이 적격이다.

칼날처럼 휘몰아치던 천령폭이 주춤하는 모습에 제갈세가와 무당파의 제자들도 잠시 출타했던 정신이 돌아온 모양이었다.

“으하하하! 호랑이가 날뛰는구나! 본가의 제자들은 대천성신장(大天星神掌)을 펼쳐라!”

명령을 내린 와룡객 제갈풍이 손에 쥐고 있던 학우선을 흔들었다.

비록 아직 벽을 넘지는 못했으나, 선법(煽法)에 있어서만큼은 초절정 고수와 어깨를 나란히 한다는 그다.

콰아아아!

학우선의 부챗살을 따라 시작된 산들바람이 강력한 바람으로 화해 와류를 막아섰다.

그리고 마치 쾌조선을 집어삼킬 듯, 삼각파도처럼 높게 솟구친 물살이 바람에 가로막혀 나아가지 못하던 그 순간.

쉭!

현공진인의 허리춤에서 솟구친 한 줄기 섬광이 허공을 스쳤다.

태극혜검(太極慧劍).

모든 것을 지나쳐 간 섬광이 공간을 가르고 바람을 베자 천령폭이 일으킨 물의 장벽이 일순 끊어지는가 싶더니, 이내 산산이 무너졌다.

촤아아아악!

사방으로 비산하는 물보라.

엄청난 양의 찬물을 뒤집어쓴 적천강이 잠에서 깨어난 사람처럼 눈을 번쩍 떴다.

그리고 화염이 줄기줄기 쏟아지는 눈동자로 와류를 노려보며 일갈했다.

“이 축축하고, 냄새나고, 더러운 것들!”

“…….”

아니, 아주 틀린 말은 아닌데 왜 이렇게 없어 보이지?

그러나 내 생각과는 달리, 적천강의 양 소매를 타고 터져 나온 공력은 강대하기 이를 데 없었다.

“모조리 꺼져라!”

화륵, 콰아아아!

수 갑자에 달하는 열양지기가 일거에 뿜어져 나온다.

주위에 가득하던 수분이 증발하고, 엄청난 반발력과 함께 쾌조선이 화살처럼 쏘아졌다.

“끼얏호우!”

“청풍, 이 미친놈아!”

“앗. 죄송해요, 은인!”

퍼버버벙!

배를 사수하기 위해 쉴 새 없이 터져 나오는 장력과 허락받지 않은 불청객들을 침몰시키려는 천령폭.

피가 배어 나올 만큼 이를 악문 무송이 목에 핏대를 세웠다.

“좌현으로, 동시에 꺾어!”

“으아아아아!”

파앙!

이 혼란스러운 상황 속, 사람들 사이에서 눈치껏 비명을 내지르던 소년 의생이 아무도 모르게 장력을 쏘아 보낸 것은 나와 적천강, 그리고 청풍만이 아는 비밀이다.

“하나, 둘!”

“지금이다! 젖 먹던 힘까지 다해 노를 저어라!”

촤아아아악!

노력은 결과를 배신하지 않는 법.

그렇게 수백 명의 승객을 실은 네 척의 쾌조선은 와류를 헤치며 앞으로, 앞으로 나아가고 있었다.



* * *



천령폭을 통과하기 무섭게, 진이 빠진 사람들은 체면도 가리지 않고 선체 곳곳에 널브러졌다.

하지만 어느 곳에나 예외는 있는 법.

붉어진 눈가로 거짓말처럼 평온해진 장강의 강물을 바라보던 적천강이 불쑥 입을 열었다.

“열화문의 당대 장문인으로서 말하건대, 명일 이 시간부로 본문의 공적(公敵)은 제갈세가다.”

“…….”

“제갈 성을 쓰는 놈들은 모조리 붙잡아 저 빌어먹을 천령폭에 처넣어야겠다. 이의 있느냐?”

“있으면요?”

“네 녀석도 같이 처넣을 것이다.”

“어, 그럼 없는 것으로 하겠습니다.”

“좋다. 당장 저 쌍노무 새끼를 잡아 노부 앞에 대령하도록 해라.”

적천강의 이글거리는 시선 끝에, 수십 장 뒤에서 따라오는 한 척의 쾌조선과 뱃머리에 앉아 학우선을 흔드는 제갈풍이 있었다.

“하하, 노선배님! 부디 노여움을 푸시지요!”

“……웃어?”

내가 봐도 죽이고 싶긴 하다.

차라리 절벽을 무너트리는 게 쉽지, 피할 곳도 없는 드넓은 장강 한복판에서 와류에 빨려 들어간다고 생각해 봐라.

말이 쉬워서 허공답보(虛空踏步)니 등평도수(登萍渡水)니 떠들어 대지만, 공력 소모도 극심하거니와 수백 명이나 되는 사람들을 구출하는 건 꿈도 꿀 수 없다.

‘아니, 무슨 바다도 아니고 강물에 저딴 게 다 있어.’

괜히 천령폭이라는 이름이 붙은 것이 아니었다.

하긴, 조금 거센 물살 정도였다면 제갈세가와 무당파가 진즉 동정채에 들이닥치고도 남았겠지.

그리고 이 사이에도 적천강의 분노는 끝을 향해 치닫고 있었다.

“당장 배 돌려라. 제갈풍인지 와룡객인지, 노부가 오늘 저놈의 다리 몽둥이를 분질러서 평생 누워 있게 해 줄 것인즉!”

“진정하세요, 진정.”

“노부가 지금 진정하게 생겼느냐! 가뜩이나 물 싫어하는데 별 거지 같은 곳에 오는 바람에 이런 고초를 겪고! 몇 번 와 봤다는 놈은 물길 하나 못 잡아서 끙끙거리고 있고! 이 정도면 수적이 아니라 저승길 뱃사공 아니냐!”

길길이 날뛰는 적천강의 모습에, 대자로 뻗어 있던 무송이 흠칫 놀라며 몸을 일으켰다.

“고, 고정하십시오, 대협. 저도 천령폭이 이 정도인 줄은 꿈에도 몰랐습니다.”

“이미 몇 번이나 와 봤다는 놈이 몰라? 모르면 수적 생활 끝나냐? 네놈 인생도 여기에서 끝내 줘?”

“그, 그게 아니라 천령폭의 물살이 전과 비교하여 이상할 만큼 강해진 탓에…….”

“강해지다니, 그건 또 무슨 개소리냐? 금년에는 비가 얼마 내리지도 않았거늘, 감히 금방 들통날 감언이설로 노부를 속이려고 들어?”

“저, 정말입니다! 제가 어찌 화왕께 거짓을 고하겠습니까!”

음. 이건 무송의 말에 일리가 있다. 어느 누가 감히 화왕 적천강을 상대로 거짓말을 치겠는가.

구라 치다가 걸리는 날에는 손모가지 날아가는 정도로는 안 끝난다. 전신이 미디엄 레어로 구워지기 딱 좋다.

‘그나저나 강수량이 적었는데 물살이 저 정도로 강해질 수가 있나?’

됐다. 내가 기상 학자나 생태계 연구원도 아닌데 생각해 봤자 답도 안 나온다.

작게 혀를 찬 나는, 쉬지 않고 무송을 갈구고 있는 적천강을 향해 입을 열었다.

“노야.”

“돌아갈 때 잘해라. 노부가 조금 전과 같은 일을 다시 한번 겪게 만든다면, 그때는 장강수로맹 총단에 쳐들어가서 모든 배를 불 싸지르고 해상왕 그놈을 제갈세가 놈들과 함께 천령폭에 처넣어…… 뭐냐? 나중에 얘기해라.”

“그게 아니라, 다 도착한 것 같은데요.”

“뭣이!”

타다다닥!

그야말로 전광석화와 같은 속도.

무송을 내팽개치고 한걸음에 쾌조선의 선체를 가로지른 적천강이 부릅뜬 눈으로 전방을 주시했다.

그리고 이내 감격에 찬 탄성이 그의 입술 사이로 흘러나왔다.

“오오, 오오오!”

누가 보면 보물섬이라도 발견한 줄 알겠지만, 자욱하게 낀 안개 너머로 모습을 드러낸 그것은 하나의 섬이었다.

대한민국의 한강에 드문드문 늘어선 섬처럼 작지도 않았고, 사람의 흔적이 보이지 않는 무인도도 아니었다.

“저기 보이는 저거, 혹시…….”

눈을 가늘게 뜬 혁무진의 중얼거림에 옆에 있던 궁기방이 고개를 끄덕였다.

“나루터로군. 제대로 찾아온 모양이야.”

배를 정박시킬 수 있는 나루터가 있다는 건, 다시 말해 사람이 살고 있거나 혹은 경유지로 자주 오가는 섬이라는 뜻이다.

그리고 저 미친 천령폭을 넘어야만 올 수 있는 이곳에 거처를 마련한 자들의 정체는 이미 이 자리의 모두가 알고 있다.

“와아, 동정채!”

청풍의 외침이 장강의 적막함을 깨트리고 멀리 퍼져 나가자, 진위경이 딱딱하게 굳은 얼굴로 입을 열었다.

“이쯤 되면 동정채에서도 우리가 왔다는 사실을 알았을 터. 혹여 모를 만일의 사태를 대비하는 것이 좋겠구려.”

“……!”

만일의 사태가 무엇을 뜻하는지 모르는 사람은 없었다.

만약 지금까지 드러난 정황대로 동정채가 지난 보름 동안 일어났던 두 사건의 흉수라면…… 그때는 무림의 법칙을 따라 무력 충돌이 일어날 수도 있다.

“채주. 우리는 피를 보기 위해 이 자리에 온 것이 아니오. 본인의 말이 무슨 뜻인지 이해하셨을 거라 믿소.”

입을 다문 채 침묵을 지키던 무송이 진위경을 응시하며 대답했다.

“저와 수하들이 앞장서서 이곳에 온 이유는, 본 맹의 형제들이 무고하다는 사실을 밝히기 위해섭니다. 만약 전후 사정을 들어 보지도 않고 무작정 우리를 핍박한다면…….”

“단언컨대 그런 일은 없을 거요. 이는 이미 무당과 제갈세가가 보증했으며, 나를 포함한 이 자리의 모두가 증인이 될 거요.”

망설이던 무송이 작게 고개를 끄덕였다.

“……믿겠소.”

어쩌면 이 중에서도 유혈 사태를 가장 막고 싶어 하는 사람은 그일지도 모른다.

동정채가 아무리 뛰어난 수적들로 이루어져 있고, 그들을 이끄는 장강일도(長江一刀) 황충이 초절정 고수라 할지라도 현재 우리의 전력을 감당할 수는 없을 테니까.

만약 아주 엄청난, 정말 만에 하나라고 부를 만큼 이해할 수 없는 이변이 일어나 이 자리의 모두가 장강에 가라앉는다고 해도, 그때는 천하 무림 전체를 상대해야 한다. 구파일방과 오대세가가 힘을 합치면 장강수로맹은 흔적도 없이 사라질 것이다.

“깃발을 높이 올리고, 우리가 왔음을 알려라.”

수룡채의 수적들은 채주의 명령을 즉시 이행했다.

곧 장강수로맹의 깃발이 네 척의 쾌조선 위로 펄럭이고, 일곱 번의 낮은 북소리가 안개 너머로 울려 퍼졌다.

그리고…… 아무 일도 벌어지지 않았다.

장강도, 안개도, 조용히 흐르는 강물도 여전했다.

바뀐 것은 진위경의 의문과 무송의 흔들리는 눈동자뿐이었다.

“채주. 무슨 일이오?”

“저도 잘 모르겠습니다. 분명 신호를 보냈으니 답이 돌아와야 하는데…….”

바로 그 순간.

“아무래도, 그건 힘들 것 같군요.”

갑자기 들려온 누군가의 목소리에 사람들이 고개를 돌렸다.

수많은 시선이 향하는 곳, 지금껏 아무도 신경 쓰지 않았던 소년 의생이 맑고 침착한 목소리로 말을 이었다.

“변고가 생긴 듯합니다.”

“그게 무슨……!”

무송의 외침은 이어지지 못했다.

소년 의생, 문경이 손가락을 들어 가리키는 그곳에는 안개와 해조물에 가려 보이지 않던 무언가가 떠올라 있었다.

그건, 누군가의 시체였다.
```

## Final English reading copy

```markdown
# Chapter 448

A Supreme Peak master was a being capable of feats straight out of an old folktale—erasing several zhang of distance in a single step, leaping through the air as though stepping on empty space, and bringing down a cliff with one punch.

But…

“Hold on tight—aaahhh!”

KRA-KOOOOM!

This place was the middle of the Yangtze, vast as an endless ocean rather than solid land.

In front of a massive whirlpool hundreds of zhang across, the fast ship carrying me was no more than a tiny leaf.

Boom!

“Whoa, whoa, whoaaaa!”

“Aaaaargh!”

When the tremendous pressure of the water slammed into the side of the fast ship, the hull that had been moving swiftly and roughly lifted into the air and tilted sideways.

As the world slowly turned upside down, Jin Wikyung clung tightly to my upper body as if I were a life jacket and screamed.

“Mother! I’m coming!”

“Where do you think you’re going? Let go!”

“Father! If you’re watching, tell me the answer!”

*Fuck, there isn’t even an answer.*

But the bigger problem was that it wasn’t just Jin Wikyung. Gung Gibang, Hyuk Mujin, and even the disciples of the Zhuge Clan and Wudang had all been driven half out of their minds.

The only ones who had managed to keep their composure were the Supreme Peak masters, myself included.

“Uhh! Uhhhhh! Water! Wateeer!”

“…”

Correction. There was one exception.

I grabbed Jeok Cheongang, who was screaming at the top of his lungs with his eyes squeezed shut, and thrust my free hand into the air with all my strength.

*Flame Divine Palm!*

Boom!

Compressed air burst outward in a wave of powerful internal energy.

Part of the whirlpool that had been raging like a blade dispersed, and the hull that had been plunging upside down toward the surface barely managed to regain its balance.

But it was far too soon to feel relieved.

A second and then a third whirlpool were approaching the falling fast ship.

*I’m not enough on my own. In a situation like this…*

With a thought flashing through my mind like lightning, I shouted one person’s name.

“Cheongpung!”

“Yes!”

Cheongpung nodded as if he understood everything and raised both arms.

“Kiya-hoo!”

“No, not ‘kiya-hoo,’ you lunatic! Do what I did!”

“Ah. Yes, Benefactor!”

Cheongpung had been enjoying the Wolmido Disco Pang Pang[^1] all by himself, but now he shook both sleeves.

The Taeeul Miri Palm, one of Huashan’s proudest techniques, transformed into dozens of flower petals that lashed out through the air.

Boom-boom-boom!

It could not match the destructive power of the Flame Divine Palm, but in a situation like this, the Taeeul Miri Palm was perfect, thanks to its much wider range.

When Tianling Falls, which had been raging like a blade, faltered, it seemed that the disciples of the Zhuge Clan and Wudang also regained the senses that had briefly departed them.

“Ha-ha-ha! The tiger is rampaging! Disciples of our family, unleash the Great Heavenly Star Divine Palm!”

Crouching Dragon Guest Zhuge Feng, who had issued the order, waved the feather fan in his hand.

Although he had not yet crossed the wall, he was said to stand shoulder to shoulder with Supreme Peak masters when it came to fan techniques alone.

Whoooosh!

The breeze that began along the fan’s ribs transformed into a powerful wind and blocked the whirlpool.

And at the moment when a wall of water rose high like a triangular wave, seemingly ready to swallow the fast ship, only to be stopped by the wind—

Whoosh!

A streak of light shot up from the waist of Perfected Being Hyeongong and swept through the air.

Taiji Wisdom Sword.

The streak of light passed through everything in its path, cleaving space and slicing through the wind. The wall of water raised by Tianling Falls seemed to be severed in an instant before collapsing into pieces.

SPLAAASH!

Spray scattered in every direction.

Jeok Cheongang, who had been drenched by an enormous amount of cold water, opened his eyes wide like a man waking from sleep.

Then he glared at the whirlpool with eyes that poured flames and shouted.

“You wet, smelly, filthy things!”

“…”

It wasn’t entirely wrong, but why did he sound so pathetic?

Contrary to my thoughts, however, the internal energy erupting from Jeok Cheongang’s sleeves was anything but pathetic.

“Get the hell out of here!”

Fwoosh—KRA-KOOOOM!

Several jiazi’s worth of Scorching Yang Qi burst out all at once.

The moisture filling the air evaporated, and the fast ship shot forward like an arrow under the tremendous recoil.

“Kiya-hoo!”

“Cheongpung, you lunatic!”

“Oh. Sorry, Benefactor!”

Boom-boom-boom!

Palm forces erupted without pause to protect the ship, while Tianling Falls tried to sink the unwelcome guests who had entered its territory without permission.

Mu Song gritted his teeth so hard that blood began to seep from his gums, the veins standing out on his neck.

“Hard to port! Turn at the same time!”

“Aaaaargh!”

Bang!

In the middle of this chaotic situation, only three people knew the secret of how the young medical apprentice had quietly fired a palm force while screaming strategically among the others: Jeok Cheongang, Cheongpung, and me.

“One, two!”

“Now! Row with every bit of strength you have!”

SPLAAASH!

Hard work never betrayed its results.

And so, the four fast ships carrying hundreds of passengers pushed onward through the whirlpool, farther and farther ahead.

* * *

The moment they passed through Tianling Falls, the exhausted passengers collapsed wherever they stood, no longer bothering with appearances.

But there was an exception to everything.

Jeok Cheongang gazed at the Yangtze, which had become unbelievably calm, his eyes red around the edges. Then he suddenly opened his mouth.

“As the current Sect Leader of the Fire Gate Clan, I hereby declare that, as of this time tomorrow, the Zhuge Clan shall be our public enemy.”

“…”

“Every bastard bearing the Zhuge name should be seized and thrown into that godforsaken Tianling Falls. Any objections?”

“What if there are?”

“I’ll throw you in with them.”

“Then I’ll have no objection.”

“Good. Seize that goddamn bastard and bring him before me at once.”

At the end of Jeok Cheongang’s burning gaze was a fast ship following several dozen zhang behind us, with Zhuge Feng sitting at its bow and waving his feather fan.

“Ha-ha, Senior! Please set aside your anger!”

“…”

“Are you laughing?”

Even I wanted to kill him.

It was easier to bring down a cliff than to escape after being sucked into a whirlpool in the middle of the vast Yangtze, where there was nowhere to run.

People tossed around names like Stepping on Empty Air and Rising on Duckweed, Crossing Water as if they were simple tricks, but those techniques consumed tremendous amounts of internal energy. Rescuing several hundred people was beyond the realm of possibility.

*What the hell is something like that doing in a river, not even the sea?*

There was a reason it had been given the name Tianling Falls.

Then again, if it were merely a somewhat fierce current, the Zhuge Clan and Wudang would have stormed into Donghu Stronghold long ago.

And while I was thinking about this, Jeok Cheongang’s anger continued racing toward its conclusion.

“Turn the ship around at once. Whether he calls himself Zhuge Feng or Crouching Dragon Guest, this old man will break that bastard’s legs and make him lie down for the rest of his life!”

“Please calm down. Calm down.”

“Do I look like I can calm down right now? I already hate water, and now I’ve suffered through this because we came to some godforsaken place! And the man who claims to have crossed it several times is groaning because he can’t even find the correct waterway! At this point, are you a river bandit or a ferryman on the road to the underworld?”

At the sight of Jeok Cheongang raging like a madman, Mu Song, who had been lying spread-eagled on the deck, flinched and forced himself upright.

“P-please calm yourself, Great Hero. I never dreamed Tianling Falls would be this bad, either.”

“You’ve been here several times and didn’t know? If you don’t know, does your life as a river bandit end here? Should I end your life here, too?”

“That’s not it. The current at Tianling Falls has grown abnormally strong compared to before…”

“Grown stronger? What kind of bullshit is that? It barely rained this year, and you’re trying to deceive this old man with sweet talk that’ll be exposed immediately?”

“I-I’m telling the truth! How could I dare lie to the Fire King?”

*Hmm.*

Mu Song had a point. Who would dare lie to Fire King Jeok Cheongang?

The day you were caught lying to him, losing a hand would be the least of your worries. Your entire body would be roasted medium-rare.

*By the way, can the current really become that strong when there hasn’t been much rain?*

Never mind. I wasn’t a meteorologist or an ecosystem researcher. Thinking about it wouldn’t produce an answer.

I clicked my tongue softly and spoke to Jeok Cheongang, who had not stopped berating Mu Song.

“Old Master.”

“When we return, do your job properly. If you make this old man suffer through what we just experienced one more time, I’ll storm the headquarters of the Yangtze River Channel League, set every ship on fire, and throw that Seafaring King bastard into Tianling Falls along with the Zhuge Clan bastards…”

“What is it? Tell me later.”

“That’s not it. I think we’ve arrived.”

“What!”

Tap-tap-tap-tap!

He moved with the speed of lightning itself.

Jeok Cheongang tossed Mu Song aside and crossed the fast ship in a single step, then stared ahead with his eyes wide open.

Soon, an emotional exclamation spilled from his lips.

“Oh. Ohhh!”

Anyone watching him might have thought he had discovered a treasure island, but what appeared beyond the thick fog was simply an island.

It was not small like the islands scattered along Korea’s Han River, nor was it an uninhabited island with no sign of human presence.

“That thing over there… Could it be…”

At Hyuk Mujin’s mutter, Gung Gibang, standing beside him, nodded.

“It’s a ferry landing. Looks like we came to the right place.”

The existence of a ferry landing where ships could dock meant, in other words, that people lived there—or that the island was frequently used as a stopover.

And everyone present already knew the identity of those who had established a settlement in a place that could only be reached after crossing that insane Tianling Falls.

“Whoa, Donghu Stronghold!”

Cheongpung’s shout shattered the silence of the Yangtze and spread into the distance.

Jin Wikyung opened his mouth, his face stiff.

“By now, Donghu Stronghold must know that we have arrived. It would be wise to prepare for any unforeseen situation.”

“…”

No one needed to ask what that unforeseen situation meant.

If Donghu Stronghold really was responsible for the two incidents that had occurred over the past fifteen days, just as the circumstances revealed so far suggested… then a clash of martial force might take place, in accordance with the laws of Murim.

“Stronghold Lord. We did not come here to spill blood. I trust you understand what I mean.”

Mu Song, who had remained silent with his mouth shut, stared at Jin Wikyung as he answered.

“The reason my subordinates and I came here at the head of the group was to prove that the brothers of our League are innocent. If you persecute us without even hearing the full circumstances…”

“I can state categorically that such a thing will not happen. Wudang and the Zhuge Clan have already vouched for this, and everyone present, myself included, will serve as witnesses.”

Mu Song hesitated before giving a small nod.

“…I’ll believe you.”

Perhaps Mu Song was the person here who most wanted to prevent bloodshed.

No matter how outstanding the river bandits of Donghu Stronghold were, and no matter how powerful Yangtze One Saber Hwang Chung—the man who led them—might be as a Supreme Peak master, they could not withstand our current strength.

Even if some utterly incomprehensible disaster—a true one-in-ten-thousand chance—caused everyone here to sink into the Yangtze, the Yangtze River Channel League would then have to face all of Murim.

If the Nine Sects and One Gang joined forces with the Five Great Families, the Yangtze River Channel League would disappear without a trace.

“Raise the flag high and let them know we are here.”

The river bandits of Water Dragon Stronghold immediately carried out their lord’s order.

Soon, the Yangtze River Channel League’s flag fluttered above the four fast ships, and seven low drumbeats echoed beyond the fog.

And then…

Nothing happened.

The Yangtze, the fog, and the quietly flowing river remained unchanged.

The only things that changed were the puzzled expression on Jin Wikyung’s face and Mu Song’s wavering eyes.

“Stronghold Lord. What is happening?”

“I’m not sure, either. We definitely sent the signal, so a reply should have come…”

At that very moment—

“I’m afraid that will be difficult.”

At the sudden voice, everyone turned their heads.

Countless gazes fell on the young medical apprentice whom no one had paid attention to until now.

In a clear, composed voice, he continued.

“It seems something has happened.”

“What do you mean…!”

Mu Song’s shout never finished.

The young medical apprentice, Mungyeong, raised a finger and pointed.

There, something previously hidden by the fog and aquatic plants had floated into view.

It was someone’s corpse.

[^1]: Wolmido Disco Pang Pang is a Korean amusement-park ride in which riders sit on a rotating platform while the operator jolts and spins it.
```

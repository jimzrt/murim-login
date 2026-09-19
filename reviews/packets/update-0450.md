<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0450.txt",
      "sha256": "19c5ed4a09db058050693323e796945892b241c9f617aede20ade4c04e9e00a6",
      "bytes": 13140
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "7a7477d7fae224c1e96b9b304ac66667096d444810aaaf658a2415a374d52235",
      "bytes": 3543
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "ffac39c8708cedbde5225046db2a2d63c5a2a3c8d3372fd2dc78c3a9a8e637f1",
      "bytes": 147306
    },
    {
      "path": "characters/Bingbing.md",
      "sha256": "8759cbf44d7eabd80a38b097855b60e8210c8421c34ead104cd6869aa5a0a61f",
      "bytes": 422
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "c0d0d0cc52c89d471e7720965a00bc00df81f02a136120507e65a616028e712c",
      "bytes": 944
    },
    {
      "path": "characters/Gung Gibang.md",
      "sha256": "798d0a476222276d8527fb36cd3bf98e590dce1e7f47f15ec678462a7ed3f61b",
      "bytes": 609
    },
    {
      "path": "characters/Hong Dao.md",
      "sha256": "2d46c43c5b86788b95f31fafd0c446bd02ebcec3e2ec8bec5b40cb8561b3aa83",
      "bytes": 1001
    },
    {
      "path": "characters/Hwang Chung.md",
      "sha256": "eb21eff344e1b871b55e7a739bb75abfa4f9d107ea5479ee27cc23ce2932d0df",
      "bytes": 663
    },
    {
      "path": "characters/Hyeongong.md",
      "sha256": "e576aa1466b580eb846bd27fd1f8ce98f11489cd5d03da571362654d91407dd7",
      "bytes": 735
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "37ab65d295fceb3fe860af8cf8a599cba8de864670d6b6b9fdcb852d4330ea41",
      "bytes": 1108
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "702f3483cddcc68bf95645f53fefded7df8fbe1717f7551499d5a6884a1117d9",
      "bytes": 1470
    },
    {
      "path": "characters/Jin Wikyung.md",
      "sha256": "3a73612dfd35c5e4211d0f046e76832b362a2c9aa50cf41b9e71148fcaec467d",
      "bytes": 1239
    },
    {
      "path": "characters/Mu Song.md",
      "sha256": "2434aa4755b524cd458ebd47f55c61918cae915af5e2b861b209a8743d7b3350",
      "bytes": 864
    },
    {
      "path": "characters/Mungyeong.md",
      "sha256": "2aa0c83c4341a31ac7693f6004e3ef6a203627d583f440de23f9b58b25e78cee",
      "bytes": 686
    },
    {
      "path": "characters/Zhuge Feng.md",
      "sha256": "ac4d737addf42c12b2198276a366197670be8c765943d1fbb098d9cfbfe63932",
      "bytes": 626
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "e461e36fdfca1b36145d5e3c2c1ab27e0d867d36d7f0c4d6478c5994b61b21fa",
      "bytes": 142508
    }
  ],
  "estimated_tokens": 13637
}
-->

# Durable State Update — Chapter 450

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 450. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 450. Profile updates may replace only one
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
  "chapter": 450,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 450,
    "continuity_sources": [450],
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
    "Dangyang Stronghold and Honghu Stronghold vanished after taking control of Sea Serpent Society territory.",
    "Hwang Chung, the Yangtze One Saber, was Mu Song's mentor-like senior and Donghu Stronghold's Lord; he was found dead after the stronghold's destruction.",
    "The Dongting Fisherman's broken Black Bamboo Fishing Rod was found, and Zhuge Feng ordered Mu Song to guide the group to Donghu Stronghold.",
    "Mungyeong remains with Taekyung's group while concealing his former Divine Physician and Slaughter Saint identity from most companions.",
    "The Skeleton King's undead identity remains concealed from the public, and Taekyung has ordered him to join Peace Guild under a prepared contract.",
    "Go Jun is expected to succeed Lee Jungryong as Ares Guild's captain and is searching China for Lee's holographic recorder.",
    "Taekyung's group survived the unusually violent Tianling Falls aboard four fast ships and reached Donghu Stronghold.",
    "Donghu Stronghold was destroyed along with its civilian population; Wang Pil and Hwang Chung were found dead, and Dark Heaven's possible use of a Moving Formation remains only a suspicion."
  ],
  "continuity_sources": [
    449,
    448
  ],
  "open_questions": [
    "What are the origin and purpose of the symbols shared by the Arch Lich's magic circle and Dark Heaven's formations, and are they connected to black magic?",
    "Why does Mungyeong continue accompanying Taekyung's group despite being unable to explain the impulse?",
    "What confidential matter is Jin Wikyung withholding?",
    "What are the terms of the Peace Guild–Wizard Guild agreement, and what evidence is contained in Lee Jungryong's holographic recorder?",
    "Who destroyed Donghu Stronghold and caused the related disappearances, whether Dark Heaven used a Moving Formation, and why the Yangtze River Channel League was targeted?"
  ],
  "safe_through": 449,
  "temporary_decisions": [
    "Render 황충 as Hwang Chung, 장강일도 as Yangtze One Saber, 천령폭 as Tianling Falls, 흑죽조간 as Black Bamboo Fishing Rod, 소조귀 as Little Tide Demon, and 황 숙부 as Uncle Hwang.",
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
| 굉도     | **Hong Dao**       |
| 법왕     | **Dharma King**               | Hong Dao       |
| 살성     | **Slaughter Saint**           | —              |
| 해상왕    | **Seafaring King**            | Pa Ryun        |
| 무당파    | **Wudang**                       |
| 암천     | **Dark Heaven**                  |
| 제갈세가   | **Zhuge Clan**                   |
| 장강수로맹  | **Yangtze River Channel League** |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 낭인     | **wandering martial artist**                     |                                                       |
| 가주     | **Family Head**                              |
| 장로     | **Elder**                                    |
| 대장로    | **Head Elder**                               |
| 사부     | **Master**                                   |
| 제자     | **Disciple**                                 |
| 은인     | **Benefactor**                               |
| 상태               | **Status**                     |
| 하남     | **Henan**              |
| 사천     | **Sichuan**            |
| 무당산    | **Mount Wudang**       |
| 정마대전   | **Great Faction War**         |
| 노부      | **this old man / I**                                            |
| 본가      | **our family / this family**                                    |
| 귀가      | **your family**                                                 |
| 도사      | **Daoist**                                                      |
| 빙빙 | **Bingbing** | Name or nickname of the child in the Monster Wave footage. |
| 궁기방 | **Gung Gibang** | Beggars' Sect Successor Beggar and finalist. |
| 황충 | **Hwang Chung** | Lord of Donghu Stronghold, the Seafaring King's sworn brother, and the Yangtze One Saber. |
| 현공진인 | **Perfected Being Hyeongong** | Veteran Wudang Daoist master and the current Sect Leader's Junior Brother. |
| 무송 | **Mu Song** | Lord of Water Dragon Stronghold and disciple of the Seafaring King. |
| 문경 | **Mungyeong** | Young medical apprentice and newly introduced passenger. |
| 제갈풍 | **Zhuge Feng** | Current Family Head of the Zhuge Clan. |
| 광수 | **Gwangsu** | First attacker at the Phoenix Inn; identified by the others after Taekyung punches him. |
| 송이 | **Song-i** | Short form used for Song Song; Taekyung's love interest. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 숙부 | **Uncle** | Lee Seowol's shortened address for Cheol Mubaek. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 쫄보 | **Coward** | Song associated with Won Myunghoon. |
| 백주 | **baijiu** | Strong distilled liquor ordered at the inn. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 호북 | **Hubei** | Province on Ju Gongsan's route from Guangdong to Henan. |
| 채주 | **Stronghold Lord** | Title used for the lord of a water stronghold. |
| 장강 | **Yangtze** | The river controlled by the Yangtze River Channel League. |
| 성도 | **Chengdu** | Sichuan destination of Taekyung's party. |
| 의생 | **medical apprentice** | Mungyeong's occupation. |
| 이동진 | **Moving Formation** | Dark Heaven's inactive long-distance transportation formation. |
| 당양채 | **Dangyang Stronghold** | Yangtze River Channel League stronghold whose lack of contact concerns Mu Song. |
| 홍호채 | **Honghu Stronghold** | Yangtze River Channel League stronghold whose lack of contact concerns Mu Song. |
| 동정채 | **Donghu Stronghold** | Stronghold where Mu Song's Uncle Hwang is based. |
| 와룡객 | **Crouching Dragon Guest** | Epithet of Zhuge Feng. |
| 해사방 | **Sea Serpent Society** | Hubei association formed by fishermen and boatmen; it was annihilated at Red Cliffs. |
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
| 적천강 | 굉도 | old_friends | Hong Dao | familiar and teasing | Uses Hong Dao's personal name in their casual reunion. |
| 굉도 | 적천강 | old_friends | Fire Gate Sect Leader | familiar and teasing | Teases Jeok as the carefree Fire Gate Sect Leader. |
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
| 진위경 | 무송 | Alliance inspector to Stronghold Lord | Stronghold Lord | formal and cautionary | Uses 채주 while warning Mu Song that the group did not come to spill blood. |
| 무송 | 황충 | junior_martial_artist_to_mentor_like_uncle | Uncle Hwang | familiar-respectful | Mu Song privately addresses Hwang Chung as 황 숙부 and cries out for him after discovering Donghu Stronghold's destruction. |

## Listed compact profiles

### Bingbing.md

# Bingbing (빙빙)

- **Safe through:** Chapter 304
- **Aliases:** None
- **Role:** Child fleeing the Monster Wave with her mother in the reconnaissance footage.
- **Personality:** Frightened after witnessing her mother's death.
- **Voice:** Childlike and panicked; cries out for Mommy.
- **Relationships:** Daughter of the woman killed by an Orc spear.

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 449
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, the grandson and Disciple of Sword Saint Mae Jonghak, and a Supreme Peak martial master known as the Huashan Divine Dragon.
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, a deep love of martial arts, and a martial artist's competitive pride; he becomes unsettled when someone copies his martial arts
- **Voice:** Dreamy and hazy, with innocent, polite phrasing
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions while Taekyung is his only true martial rival; Tang Sadok has temporarily entrusted Mimi to him.

### Gung Gibang.md

# Gung Gibang (궁기방)

- **Safe through:** Chapter 449
- **Aliases:** Successor Beggar, Beggar Prince, pure-blooded beggar, ultimate beggar
- **Role:** Gung Gibang is the Beggars' Sect Successor Beggar and a unique eight-knot disciple.
- **Personality:** Vulgar, aggressive, and quick-tempered.
- **Voice:** Blunt, profane, and vividly threatening.
- **Relationships:** Rival finalist alongside Baek Woo and Zhuge Gyun; trades insults with Taekyung and is helping investigate Tang Taesang’s murder through Beggars’ Sect intelligence.

### Hong Dao.md

# Hong Dao (굉도)

- **Safe through:** Chapter 340
- **Aliases:** Dharma King
- **Role:** Abbot of Shaolin and the Murim's Dharma King; master of Unnamed and the only friend to whom Jeok Cheongang had opened his heart; after leaving the Star-Array Grand Banquet, he was found in a massive pit with both legs severed and catastrophic internal injuries, whispered final words to Jeok Cheongang, and died.
- **Personality:** Calm, responsible, quietly playful, and still regarded by Jeok as lazy for sleeping whenever possible.
- **Voice:** Quiet, deep, weighty, and resonant, with casual familiarity when speaking to Jeok Cheongang.
- **Relationships:** Old friend of Jeok Cheongang; master of Unnamed; before his death, entrusted the Green Jade Buddha Staff to Unnamed and used his final words to warn Jeok about Jongni Chu, Dark Heaven, Unnamed, and the Buddhist Staff; sends Unnamed to bring the Master of Morning Star to Shaolin.

### Hwang Chung.md

# Hwang Chung (황충)

- **Safe through:** Chapter 449
- **Aliases:** Yangtze One Saber
- **Role:** Hwang Chung was the Lord of Donghu Stronghold, a moderate-faction elder of the Yangtze River Channel League, and the Seafaring King's sworn brother before he was killed in the stronghold's destruction.
- **Personality:** Calm, clever, and supportive of the orthodox faction during the Great Faction War.
- **Voice:** Not established.
- **Relationships:** Hwang Chung helped the Seafaring King establish the Yangtze River Channel League and is regarded by Mu Song as an uncle and trusted senior.

### Hyeongong.md

# Perfected Being Hyeongong (현공진인)

- **Safe through:** Chapter 448
- **Aliases:** None
- **Role:** Perfected Being Hyeongong is a veteran Wudang Daoist master of the previous generation, the current Sect Leader's Junior Brother, and a Supreme Peak swordsman who reached the ultimate stage of the Taiji Wisdom Sword.
- **Personality:** Hyeongong is humble and self-deprecating about his limited worldly knowledge while carrying the authority of an experienced senior master.
- **Voice:** Measured, respectful, and lightly self-deprecating.
- **Relationships:** Hyeongong is the current Wudang Sect Leader's Junior Brother and a respected senior to Zhuge Feng.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 449
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers and Vice Squad Leader of the Jin Dragon Squad.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 449
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master, and Jin Taekyung's Master.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, and pathologically afraid of water. His meeting with Taekyung rekindled his will to live, making him determined to extend his life despite his illness.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Jin Wikyung.md

# Jin Wikyung (진위경)

- **Safe through:** Chapter 449
- **Aliases:** Junzi Sword
- **Role:** Jin Wikyung is the thirty-six-year-old Lesser Family Head and future Family Head of the Jin Family of Taiyuan, the Alliance Leader who unified Shanxi Murim and Shanxi Province's foremost landowner and magnate.
- **Personality:** Calm, authoritative, and politically capable in public; protective and affectionate toward Taekyung beneath a stern mask. Takes responsibility for his people, acts decisively under pressure, and prioritizes family survival.
- **Voice:** Restrained, formal, and commanding with subordinates; openly affectionate, proud, and occasionally exuberant with Taekyung.
- **Relationships:** Taekyung's eldest brother and future Family Head; Taekyung trusts him as a martial-arts mentor and family protector. Member and acting leader of the Jin Family of Taiyuan. Commands Wipeng and the family's forces. Has worked with Jeok Cheongang, who trained Taekyung under Wikyung's arrangement. Jin Mukyung is his younger brother and a potential successor alongside Taekyung.

### Mu Song.md

# Mu Song (무송)

- **Safe through:** Chapter 449
- **Aliases:** Ship-Fire Boy
- **Role:** Lord of Water Dragon Stronghold, a Peak master and the Seafaring King's second martial Disciple who controls major Yangtze river traffic in Sichuan and belongs to the Yangtze River Channel League's moderate faction.
- **Personality:** Ambitious, domineering, impatient with interruptions, and capable of pragmatic cooperation when circumstances demand it.
- **Voice:** Deep and low in private, shifting to dry authority or boisterous command when addressing subordinates and rivals.
- **Relationships:** Mu Song is a member of the Yangtze River Channel League's moderate faction; Hwang Chung, his senior and Uncle Hwang, was the League elder and Donghu Stronghold Lord who was killed in its destruction.

### Mungyeong.md

# Mungyeong (문경)

- **Safe through:** Chapter 449
- **Aliases:** None
- **Role:** Mungyeong is the legendary physician known as the former Divine Physician and Slaughter Saint, having passed the Divine Physician title to his Disciple.
- **Personality:** Compassionate, resolute, resourceful, and calm under extreme pressure.
- **Voice:** His Mungyeong persona is timid, deferential, and cheerful, while his Slaughter Saint voice is dry, impassive, and blunt.
- **Relationships:** Dong Feng is his Disciple, while Jeok Cheongang, Jin Taekyung, Cheongpung, and the two Sect Leaders know his Slaughter Saint identity.

### Zhuge Feng.md

# Zhuge Feng (제갈풍)

- **Safe through:** Chapter 448
- **Aliases:** Crouching Dragon Guest
- **Role:** Zhuge Feng is the current Family Head of the Zhuge Clan and father of its Lesser Family Head, Zhuge Gyun.
- **Personality:** Analytical and disarmingly casual, he treats comfort and time as principles while delivering grave intelligence with unsettling directness.
- **Voice:** Clear, calm, polished, and conversational, with understated humor and pointed questioning.
- **Relationships:** Zhuge Gyun is his son, and Zhuge Gonghu was his grandfather.

## Korean source

```text
＃450화



섬의 끝자락, 모래밭 근처에는 수십여 명의 사람들이 모여 있었다.

우리의 등장에 주위를 둘러싸고 있던 무인들이 길을 트자, 비로소 익숙한 얼굴들을 발견할 수 있었다.

“황 숙부, 소질을 두고 어찌 이리 가십니까! 어찌!”

쉰 목소리로 통곡하는 무송. 그런 그의 모습을 안타까운 표정으로 지켜보는 무당파의 현공진인과 속을 알 수 없는 심유한 눈빛을 한 와룡객 제갈풍.

그리고…….

‘문경.’

언제나 있는 듯 없는 듯, 사람들 사이에서 존재감을 드러내지 않던 문경은 동정채에 변고가 생겼다는 걸 알아차린 그 순간부터 누구보다 기민하게 움직였다.

살성이 아닌 의생으로서, 단 한 사람이라도 살리기 위해 동분서주한 것이다.

하지만 그런 문경의 노력을 비웃기라도 하듯 살아남은 생존자는 아무도 없었다.

무송이 하염없이 눈물을 흘리며 끌어안고 있는 시신 역시, 비극이 낳은 수많은 희생자 중 한 사람이었다.

“오셨습니까.”

말을 건네는 제갈풍을 고깝게 흘겨본 적천강이 입을 열었다.

“저것이 장강일도 황충이냐?”

“알아보시기 힘드시겠지만, 저희가 파악한 바로는 확실합니다.”

저것.

고인을 가리키는 단어로는 부적절하게 들릴지 모른다.

하지만 장강일도 황충의 시신을 직접 본 사람이라면 딱히 이의를 제기하지 못할 것이다. 나 역시 마찬가지였다.

‘도대체 어떤 미친놈이.’

시신은 한때 살아 있는 사람이었다는 것이 믿기지 않을 만큼 심각하게 훼손되어 있었다.

바위로 내리찍은 것처럼 짓이겨진 얼굴과 가슴팍 아래로는 존재하지 않는 몸뚱어리.

부패한 살과 내장이 풍기는 악취가 코를 찌른다.

“읍, 우욱!”

헛구역질과 함께 뒷걸음질 치는 혁무진을 탓할 수 없었다.

지금껏 헤아릴 수 없을 만큼 참혹한 광경과 많은 시신을 목격했던 나조차도 속이 울렁거릴 정도니까.

해상왕의 의형제이자 고강한 무공으로 드넓은 장강을 호령했던 초절정 고수.

장강일도 황충은 시신보다는 고깃덩어리에 가까운 모습이었다.

“은인, 이건…….”

“끔찍하군. 어떤 천인공노할 놈이 이런 짓을.”

안색이 창백하게 질린 청풍과 궁기방이 중얼거렸다.

딱딱하게 굳은 얼굴로 시신을 응시하던 나는, 문득 이상함을 느끼며 입을 열었다.

“저 시신들은 뭡니까?”

섬에 가득한 것이 시체들이니 몇 구가 더 있다고 해서 놀랍지는 않다.

하지만 내 시선이 닿은 두 구의 시체는 장강일도 황충의 옆에 나란히 눕혀져 있었다.

‘그만큼 중요한 인물들이라는 뜻이겠지.’

내 손끝을 따라 시선을 옮긴 제갈풍이 대답했다.

“광수도귀(狂水刀鬼) 황철. 그리고 파랑호(波浪狐) 도립군일세.”

“광수도귀, 파랑호…….”

몇 번인가 들어 본 이름이다. 그것도 비교적 최근에.

짧은 생각 끝에 기억을 떠올린 내가 고개를 번쩍 쳐들었다.

“혹시?”

“맞네. 동정호의 휘하에 있는 당양채와 홍호채의 채주들이지.”

“해사방의 영역을 장악한 뒤에 흔적도 없이 사라졌다고 하지 않았습니까?”

“그래, 분명 그랬지.”

제갈풍이 심유한 눈빛으로 두 채주의 시신을 응시하며 말을 이었다.

“광수도귀는 성정이 폭급했고, 파랑호는 교활했네. 그렇기에 달포 전 해사방의 사건이 터졌을 때, 모두가 그들을 의심할 수밖에 없었어.”

궁기방이 불쑥 입을 열었다.

“사부님께서 언젠가 그런 말씀을 하셨습니다. 장강수로맹 내에서 광수도귀와 파랑호를 통제할 수 있는 것은 두 사람밖에 없다고.”

“맞는 말일세. 성정과는 별개로 그만한 무공을 갖춘 이들이니까. 제어하는 목줄이 없다면 제멋대로 날뛰었을 맹견들이지.”

그런 의미에 보자면 장강일도 황충은 맹견을 제어하는 목줄로는 제격이었을 것이다.

장강수로맹에서 해상왕 다음가는 고수인 데다 사람을 다루는 능력도 출중했을 테니까.

하지만 튼튼했던 목줄은 끊어졌고, 두 마리 맹견도 죽은 채 발견되었다.

오랜 기간 해사방과 팽팽한 이권 다툼을 벌였던 호북성의 장강수로맹마저 초토화된 상황.

그리고 어떤 이유도, 명분도 없이 이와 같은 짓을 벌일 수 있는 집단은 단 한 곳뿐이다.

“암천(暗天). 또다시 그들인가?”

현공진인의 탄식에 숨길 수 없는 분노와 안타까움이 묻어 나왔다.

하남에 이어 사천. 마침내 호북성에까지 암천의 그림자가 드리워진 것이다.

아니, 어쩌면 아주 오래전부터 암천은 천하를 딛고 서 있었을지도 모른다.

다만 그때는 빛 한 점 없는 밤이었기에 그림자를 느끼지 못했을 뿐.

‘오래전 대장로가 암천과 손을 잡았던 것처럼.’

이것은 하루 이틀 만에 시작된 일이 아니라, 자그마치 정마대전 무렵부터 태동한 흉계다.

“난세(亂世). 바야흐로 난세로군.”

낮게 뇌까린 와룡객 제갈풍이 고개를 들어 주위를 둘러보았다.

알 수 없는 빛으로 번뜩이는 한 쌍의 눈동자가 사방에 자욱한 안개를 응시한다.

마치 그 너머에 웅크린 무언가를 꿰뚫어 보듯이.



* * *



나와 일행들을 포함한 모두는 바쁘게 움직였다.

그러나 한 사람의 생존자, 혹은 목격자를 찾기 위해 섬을 포함한 주위 절벽을 샅샅이 수색했음에도 아무런 소득도 얻지 못했다.

오히려 의문과 답답함만이 더욱 커졌을 뿐이었다.

‘생존자가 한 사람도 없다는 건 그렇다 치고, 진법의 흔적까지 찾을 수 없다니.’

만약 암천이 천령폭을 거치지 않고 이동진을 통해 이곳으로 들어왔다면, 이곳 어딘가에는 반드시 사천에서 발견했던 것과 같은 흔적이 남아 있어야 했다.

하지만 진법과 기관으로 이름 높은 제갈세가의 가솔들이 나섰음에도 이렇다 할 성과가 나오지 않았다.

오죽했으면 제갈풍이 찾아와 물어볼 정도였다.

“정말 그런 진법이 있는 것이 확실한가?”

“그렇다니까요. 일이 마무리된 후 바로 떠났던 바람에 하남에서는 찾지 못했지만, 사천혈사(四川血史) 때는 두 눈으로 똑똑히 봤습니다.”

“나 역시 서찰을 통해 알고는 있었지만, 그런 기이한 진법은 본가의 기록에도 존재하지 않는 것일세.”

“그럼 이번 기회에 새로 적으세요.”

“…….”

“찾아보면 분명히 있습니다. 반드시 찾아야 해요.”

“동의하네. 하지만 지금 이곳에 모인 인원들로는 역부족이야.”

동정채가 본거지로 삼은 섬의 면적도 면적이지만, 더욱 큰 문제는 그 주위 환경이다.

육로로도 진입할 수 없는 수백 장 길이의 절벽이 사방을 둘러싸고 있고 그보다 더한 넓이의 강물이 존재한다.

쾌조선 네 척과 삼백여 명 남짓한 인원으로는 한계가 있을 수밖에 없었다.

“무예에 뛰어난 이들을 가려 뽑은 것이 실수일세. 진법에 조예가 깊은 식솔들을 데려와야 했어.”

후회해도 어쩌겠나.

제갈풍 뿐만이 아니라 나를 포함한 이 자리의 모두는 장강수로맹과의 유혈사태를 우려했지, 이런 상황이 기다리고 있을 거라고는 꿈에도 생각하지 못했다.

“그럼 저희가 제갈세가로 가서 필요한 인재들을 데려오겠습니다.”

“가주인 내가 직접 가는 것이 좋겠지만, 아무래도 현재로서는 그것이 최선일 듯하네. 본가의 가솔 몇을 붙여 줄 테니 함께 가도록 하게.”

조용히 이야기를 듣고 있던 적천강이 나를 향해 불쑥 입을 열었다.

“설마 네 녀석이 말한 저희에 노부도 포함되어 있느냐?”

“당연한 거 아닙니까. 그 속담 모르세요? 바늘 가는 데 실 간다.”

“그렇구나. 하면 이런 속담은 들어봤느냐?”

“……?”

“헛소리하면 뒈진다.”

“……!”

순간 움찔하는 내게, 적천강이 주먹을 말아쥐며 으름장을 놓았다.

“노부는 안 간다. 다녀오려면 너나 다녀오거라.”

“아니, 여기서 평생 사실 겁니까? 영원히 안 나가실 거예요?”

“누가 평생 산다고 하더냐? 굳이 우르르 몰려갈 필요는 없으니, 노부 한 사람이라도 더 남아 진법을 찾는 것을 도와야 흉수가 밝혀지고 호북성이 평안해질 것 아니냐?”

친우였던 법왕 굉도가 암천에 의해 죽임을 당한 이후, 적천강은 암천의 암자만 나와도 이를 갈긴 했지만 이번 반응은 뭔가 석연찮다.

잠시 생각하던 내가 손뼉을 쳤다.

“아. 이제 알겠다. 천령폭 때문에 그러시는구나.”

“……!”

“괜히 빙빙 돌리지 마시고 진작 말을 하시지. 저도 신경 쓰는 걸 깜빡했네요.”

“누, 누가 그깟 물 따위를 신경 쓴다고! 노부가 누군지 잊은 것이냐!”

“음. 쫄보?”

“노옴!”

빡! 빡! 빠악!

뒤통수를 일곱 대쯤 맞고 도망쳐 나온 나는 다음 목적지를 향해 발걸음을 옮겼다.

한데 모여 있던 익숙한 얼굴들이 이쪽을 향해 고개를 돌린다.

“조장님. 앞으로 어떻게 하는 겁니까?”

나는 혁무진의 엉덩이를 툭 걷어차며 대답했다.

“막 얘기하고 왔다. 당장 떠나야 하니까 준비해.”

“떠나다니, 어디로요?”

“제갈세가. 진법과 기관에 능통한 사람들을 데려와야 할 것 같다. 여차하면 무당파 쪽에서도 충원하고. 그쪽에도 진법 쪽에 조예가 깊은 도사들이 몇 있다던데?”

“글쎄, 아마 무당파는 힘들지도 모른다.”

불쑥 끼어든 궁기방의 말에 내가 눈살을 찌푸렸다.

“그게 뭔 개소리야?”

“내가 아니라 현공진인께서 말씀하신 거다.”

“음. 다시 생각해 보니까 그럴 만한 이유가 있는 말일 것 같다.”

“…….”

“됐고, 자세히 설명해 봐. 무슨 소린지.”

“무당파 쪽에서도 문제가 생긴 모양이다. 해사방의 일이 있기 전부터 웬 미친 살귀(殺鬼) 한 놈이 호북성 곳곳에서 사람을 죽이고 있다는데…… 이게 일이 커진 모양이야. 벌써 놈의 손에 죽은 이들만 서른을 넘겼으니 그럴 만도 하지.”

“살귀? 그놈 무림인이야?”

“상당한 경지의 무인인 것은 확실해 보인다. 비록 희생자 대부분이 양민이긴 하지만, 제법 이름 있는 일급 낭인이 관부의 의뢰를 받아 놈을 쫓다가 사체로 발견되었다더군.”

일급 낭인이라면 어딜 가도 일류 고수 소리를 듣는다.

만약 소문의 그 살귀가 정말로 손쉽게 일급 낭인을 처리하고 도망쳤다면 절정 고수일 가능성도 충분했다.

‘하지만 겨우 그놈 하나 잡자고 무당파 전체가 들고일어날 리는 없는데.’

순간 들었던 의문은 곧장 이어진 궁기방의 말에 깨끗이 사라졌다.

“사흘 전인가? 무당산을 오르던 참배객 스무 명이 떼 몰살을 당하는 일이 있었다더군. 그중에 무당파의 속가제자로 입문하려는 고관대작의 자제들이 포함되어 있었다.”

“아.”

다른 곳도 아니고 무당산에서 벌어진 참극이다.

참배객들이 본산 앞마당에서 몰살을 당한 것으로도 모자라 고관대작의 자제들을 건드렸으니 무당파의 분노는 당연했다.

‘단단히 미친놈이네. 대담하기도 하고.’

문득 암천이라는 두 글자가 뇌리를 스쳤지만, 이내 고개를 저었다.

이곳은 무림이다. 현대의 연쇄살인마는 명함도 내밀 수 없는 정신 나간 놈들이 수두룩하다.

해가 중천에 뜬 백주 대낮에 대로변에서 살인이 일어나도 그리 놀라운 일은 아니다.

‘만약 암천의 짓이었다면 비교도 안 될 만큼 큰 사건이 터졌겠지.’

어쨌든 무당파의 상황이 그렇다고 하니, 우선은 제갈세가에 도착한 후 다시 생각해 볼 문제다.

“뭐, 일단 알았으니까 다들 짐 챙겨. 밖에서도 우리 데려가려고 준비 중이니까.”

진위경은 이미 제갈풍을 만나러 가기도 전에 남기로 한 상태고, 나는 이 자리에 있는 녀석들만 데려가면 된다.

하지만 한 놈, 아니 한 분은 생각이 다른 모양이었다.

“전 남겠습니다.”

“어떤 새끼가…… 아. 문경이구나.”

“혹시 제가 따라가야 할 이유라도?”

“없지. 남아, 남아.”

제발 남아 줘라.
```

## Final English reading copy

```markdown
# Chapter 450

At the edge of the island, near the sandy shore, several dozen people had gathered.

When the martial artists surrounding us opened a path, I finally spotted some familiar faces.

“Uncle Hwang! How could you leave without your nephew? How could you!”

Mu Song wailed in a hoarse voice. Perfected Being Hyeongong of Wudang watched him with a sorrowful expression, while Crouching Dragon Guest Zhuge Feng watched with a profound, unreadable gaze.

And then…

*Mungyeong.*

Usually, Mungyeong had a presence that was there and yet not there, never drawing attention to himself among the others. But from the instant he realized something had happened at Donghu Stronghold, he had moved more quickly than anyone.

As a medical apprentice rather than a Slaughter Saint, he had rushed from place to place in an effort to save even a single person.

But as though mocking all his efforts, not a single survivor remained.

The corpse Mu Song clutched as he wept endlessly belonged to one of the countless victims claimed by the tragedy.

“You’ve arrived.”

Jeok Cheongang gave Zhuge Feng a displeased glance before speaking.

“Is that Yangtze One Saber Hwang Chung?”

“It may be difficult to recognize him, but according to what we have determined, there is no doubt.”

*That.*

It might sound inappropriate to use such a word when referring to the dead.

But anyone who had seen the corpse of Yangtze One Saber Hwang Chung in person would have been unable to object. I was no different.

*What kind of lunatic did this?*

The corpse had been so badly mutilated that it was difficult to believe it had once been a living person.

The face had been crushed as if it had been smashed with a rock, and below the chest, there was simply no body left.

The stench of rotting flesh and viscera stabbed at my nose.

“Urgh—ugh!”

I could not blame Hyuk Mujin for staggering backward with a retch.

Even I, who had witnessed more gruesome scenes and corpses than I could count, felt my stomach churn.

The sworn brother of the Seafaring King, a Supreme Peak master who had ruled the vast Yangtze with his formidable martial arts…

Yangtze One Saber Hwang Chung looked more like a lump of meat than a corpse.

“Benefactor, this is…”

“It’s horrifying. What kind of fiend would commit such an atrocity?”

Cheongpung and Gung Gibang murmured, their faces pale.

I stared at the corpse with my face stiff as stone, then suddenly felt something strange and opened my mouth.

“What are those corpses?”

There were corpses covering the island, so it was not surprising that there were a few more.

But the two corpses I had noticed had been laid out side by side next to Yangtze One Saber Hwang Chung.

*That must mean they were important figures as well.*

Zhuge Feng followed my gaze and answered.

“Mad Water Saber Demon Hwang Cheol. And Wave Fox Do Ripgun.”

“Mad Water Saber Demon, Wave Fox…”

I had heard those names a few times before. Fairly recently, too.

After a brief moment of thought, I suddenly lifted my head.

“Could they be…?”

“That’s right. They were the Stronghold Lords of Dangyang Stronghold and Honghu Stronghold, which were under Dongting Lake.”

“Weren’t they said to have vanished without a trace after taking control of the Sea Serpent Society’s territory?”

“Yes. That was certainly the case.”

Zhuge Feng continued, his deep eyes fixed on the corpses of the two Stronghold Lords.

“The Mad Water Saber Demon was hot-tempered, while the Wave Fox was cunning. That was why, when the Sea Serpent Society incident occurred a month ago, everyone had no choice but to suspect them.”

Gung Gibang suddenly spoke up.

“My Master once said that only two people in the Yangtze River Channel League were capable of controlling the Mad Water Saber Demon and the Wave Fox.”

“That is correct. Regardless of their personalities, both possessed formidable martial arts. Without a leash to control them, they would have run wild like vicious hounds.”

In that sense, Yangtze One Saber Hwang Chung would have been the perfect leash for those vicious hounds.

He was the second most powerful master in the Yangtze River Channel League after the Seafaring King, and he must also have been exceptionally skilled at handling people.

But the sturdy leash had snapped, and the two vicious hounds had also been found dead.

Even the Yangtze River Channel League in Hubei Province, which had been locked in a fierce struggle over interests with the Sea Serpent Society for a long time, had been laid to waste.

And there was only one group capable of doing something like this without reason or justification.

“Dark Heaven. Is it them again?”

Perfected Being Hyeongong’s sigh carried unmistakable anger and sorrow.

After Henan and Sichuan, Dark Heaven’s shadow had finally fallen over Hubei Province.

No—perhaps Dark Heaven had been standing atop the world for a very long time.

Perhaps we simply had not felt its shadow because it had been night, with not a single ray of light.

*Just as the Head Elder joined hands with Dark Heaven long ago.*

This was not some scheme that had begun yesterday or today. It was a sinister plot that had been taking shape since the time of the Great Faction War.

“An age of chaos. This is truly an age of chaos.”

Crouching Dragon Guest Zhuge Feng muttered the words under his breath, then raised his head and looked around.

A pair of eyes gleaming with an unknowable light stared into the thick fog surrounding us.

It was as though he could see through it, straight to something crouching beyond.

* * *

Everyone, myself and my companions included, moved busily.

But even after searching every corner of the island and the surrounding cliffs in the hope of finding a single survivor or witness, we gained nothing.

If anything, our questions and frustration only grew.

*I can accept that there isn’t a single survivor. But how can there be no trace of a formation, either?*

If Dark Heaven had entered this place through a Moving Formation without passing through Tianling Falls, there had to be traces somewhere resembling those we had found in Sichuan.

Yet even after the retainers of the Zhuge Clan, famed for their knowledge of formations and mechanisms, joined the search, we had nothing to show for it.

The situation was so strange that Zhuge Feng eventually came to ask me about it.

“Are you certain such a formation really exists?”

“I told you, it does. We left Henan immediately after everything was over, so we couldn’t search for it there. But during the Sichuan Blood Tragedy, I saw it clearly with my own two eyes.”

“I knew about it through the letters I received, but even our family’s records contain no trace of such a strange formation.”

“Then add it to the records this time.”

“…”

“If we keep looking, we’ll find it. We have to.”

“I agree. But the people gathered here are insufficient.”

The island Donghu Stronghold had made its headquarters was large enough, but the surrounding environment was an even greater problem.

Cliffs hundreds of zhang long surrounded it on every side, making entry by land impossible, and an even wider expanse of river stretched beyond them.

Four fast ships and roughly three hundred people could only accomplish so much.

“It was a mistake to select people skilled in martial arts. We should have brought retainers with a deep understanding of formations.”

There was no point regretting it now.

Not only Zhuge Feng but everyone present, myself included, had been worried about a bloody conflict with the Yangtze River Channel League. None of us had dreamed that a situation like this would be waiting for us.

“Then we’ll go to the Zhuge Clan and bring back the people we need.”

“It would be best for me, as Family Head, to go myself, but under the circumstances, that seems to be our best option. I’ll have several retainers from our family accompany you. Take them with you.”

Jeok Cheongang, who had been listening quietly, suddenly spoke to me.

“Does that ‘we’ you mentioned include this old man?”

“Of course. Don’t you know the saying? Wherever a needle goes, the thread follows.”

“I see. Then have you heard this saying?”

“…?”

“Talk bullshit and you die.”

“...!”

When I flinched, Jeok Cheongang clenched his fist and threatened me.

“This old man isn’t going. If you want to go, go by yourself.”

“What, are you planning to stay here for the rest of your life? Never leave?”

“Who said this old man was staying forever? There’s no need for everyone to swarm off. If even one extra person stays behind to help find the formation, we can uncover the culprit and restore peace to Hubei, can’t we?”

Ever since his friend, the Dharma King Hong Dao, had been killed by Dark Heaven, Jeok Cheongang had ground his teeth at so much as the first syllable of its name. But there was something suspicious about his reaction this time.

After thinking for a moment, I clapped my hands.

“Ah. Now I understand. This is because of Tianling Falls.”

“...!”

“You should have just said so instead of beating around the bush. I forgot to take that into account, too.”

“W-who says I care about a little water? Have you forgotten who this old man is?”

“Hmm. A Coward?”

“You little—!”

Bam! Bam! Baaam!

After taking about seven blows to the back of the head, I ran away and headed toward our next destination.

The familiar faces gathered in one place turned toward me.

“Captain. What do we do now?”

I answered while giving Hyuk Mujin a light kick to the butt.

“I just talked it over with them. We have to leave immediately, so get ready.”

“Leave? Where are we going?”

“The Zhuge Clan. It seems we need to bring back people skilled in formations and mechanisms. If necessary, we’ll also bring in reinforcements from Wudang. I heard they have several Daoists who are well versed in formations.”

“I’m afraid Wudang may be difficult.”

I frowned at Gung Gibang’s sudden interruption.

“What kind of bullshit is that?”

“I’m not the one who said it. Perfected Being Hyeongong did.”

“Hmm. Now that I think about it, there must be a good reason for him to say that.”

“…”

“Whatever. Explain it properly. What do you mean?”

“It seems there’s been trouble on Wudang’s side as well. Even before the Sea Serpent Society incident, some mad killer demon had been murdering people throughout Hubei Province… It appears the situation has grown serious. More than thirty people have already been killed by his hand, so I suppose it would.”

“A killer demon? Is he a martial artist?”

“He certainly seems to be a martial artist of considerable skill. Most of the victims were commoners, but an accomplished First Rate wandering martial artist with a respectable name was reportedly found dead after accepting a government assignment to hunt him down.”

A first-class wandering martial artist would be considered a First Rate master wherever he went.

If the killer demon from the rumors had really disposed of a First Rate wandering martial artist with ease and escaped, there was a good chance he was a Peak master.

*But Wudang wouldn’t mobilize the entire sect just to catch one man.*

The question that had arisen in my mind vanished at Gung Gibang’s next words.

“Was it three days ago? Twenty pilgrims climbing Mount Wudang were slaughtered to a person. Among them were the sons and daughters of high officials and nobles who were seeking admission as lay disciples of Wudang.”

“Ah.”

It was not merely a massacre that had taken place somewhere else. It had happened on Mount Wudang itself.

As if pilgrims being massacred right in Wudang’s own front yard weren’t enough, the victims included children of high officials and nobles. Wudang’s fury was only natural.

*He’s completely insane. And bold, too.*

For a moment, the two words *Dark Heaven* crossed my mind, but I soon shook my head.

This was Murim. There were lunatics everywhere who made modern serial killers look like amateurs.

Even if someone were murdered in broad daylight on a main road, it would not be all that surprising.

*If Dark Heaven had done this, an incident incomparably larger would have erupted.*

In any case, that was the situation in Wudang. For now, we would have to think about it again after reaching the Zhuge Clan.

“Well, now that I know, everyone pack your things. They’re already preparing outside to take us back.”

Jin Wikyung had already decided to remain behind even before we went to meet Zhuge Feng, so I only needed to take the people here with me.

But one person—or rather, one gentleman—seemed to have a different idea.

“I’ll stay.”

“Which bastard— Oh. It’s Mungyeong.”

“Is there any reason I should go with you?”

“Nope. Stay. Stay.”

*Please stay.*
```

<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0468.txt",
      "sha256": "0fefe64df5de36ba26b1b431be38a19d84e33ce3a02d89850de6c0013777e203",
      "bytes": 13146
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "b458493b995d4f3639fc292893b12c7b9b114c3585780fb6eda789e9f18365b6",
      "bytes": 3570
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "32cc812342789c1f894a4d7beba9341103cf6475e4f84a91f281bd0758fba611",
      "bytes": 151535
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "0aad19120527a52042ec7f58dba695abcb46b9b4be56b88486db61482aaff05b",
      "bytes": 553
    },
    {
      "path": "characters/Hyeongong.md",
      "sha256": "dbc555ecf55a9e66127fe9949484f2131f2a9c970ad4b239ec19870cf887a4b7",
      "bytes": 735
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "eb98d8e433d0e8c4cd3c002877afe3a1ce6e739a19d955aca14d495245d946e8",
      "bytes": 1542
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "da154c52704dc8fb96b2f074b7f031fddcf03b125e5ae676f355456ce8537ae6",
      "bytes": 1574
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "8b2a98426a5afa4fc979ff18051d302c1dc0f4367225b5a5ab5f300a5d67a749",
      "bytes": 622
    },
    {
      "path": "characters/Mu Song.md",
      "sha256": "e3e7c8386c96fd4cd2ee145d2fac6a81dd15aed38efea9b70de3bec8fc2156d9",
      "bytes": 864
    },
    {
      "path": "characters/Mungyeong.md",
      "sha256": "cd825b0b1875bf50f7eab77b65ba8378493bc7e2b2a362ca2f5549fa72b26c98",
      "bytes": 734
    },
    {
      "path": "characters/Zhuge Feng.md",
      "sha256": "f6c883008e1367c98f0aff736f714611749075a32362ecede1865e99e3a5087d",
      "bytes": 626
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "8de819461c480c12e8750d37657d2b4d292aec5597a36b6117702983e151eb39",
      "bytes": 146658
    }
  ],
  "estimated_tokens": 12869
}
-->

# Durable State Update — Chapter 468

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 468. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 468. Profile updates may replace only one
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
  "chapter": 468,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 468,
    "continuity_sources": [468],
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
    "Taekyung defeated the Dongting Fisherman with Flame-Extinguishing Divine Fist and brought him out alive for interrogation; the fisherman is now severely injured and immobilized by Paralysis, Mute, and Sleep Acupoints.",
    "The Dongting Fisherman accepted Dark Heaven’s hand and is implicated in slaughtering innocent commoners and children; Taekyung intends to extract Dark Heaven information before allowing him to die.",
    "Taekyung suffered only a minor internal injury from the Dongting Fisherman’s Inner-Family Heavy Hand and remains capable of fighting.",
    "Hyuk Mujin and Gung Gibang disregarded Taekyung’s order to wait because they sensed he was in danger, while Cheongpung remained confident that Taekyung would return.",
    "Honglan survived the Dongting Lake disaster and is recovering; Ju Wongong remains unconscious under guard after passing the most dangerous stage of his injuries.",
    "Jin Wikyung is acting as an inspector for the new Murim Alliance and is cooperating with Taekyung’s investigation.",
    "The shared symbols between the Arch Lich’s magic circle and Dark Heaven’s formations remain unexplained.",
    "The Sea Serpent Society and three Yangtze River Channel League strongholds, including Donghu Stronghold, were destroyed with more than a thousand casualties, while the perpetrators’ wider plans remain unknown.",
    "The captured Three Fiends is a former-generation great fiend and Supreme Peak Dark Heaven subordinate whom Taekyung is transporting alive to investigate possible codes or markings.",
    "A severe storm has made the ferryboat’s return across Dongting Lake unsafe, forcing the group to wait near the refuge until conditions improve.",
    "Despite remaining under Taekyung’s pressure-point seals, the Dongting Fisherman’s body moved independently of his will; he awoke terrified, warned Taekyung to run, and an unexplained enormous roar followed."
  ],
  "continuity_sources": [
    467,
    466
  ],
  "open_questions": [
    "What is the Dongting Fisherman’s exact role within Dark Heaven, and what information will he reveal under interrogation?",
    "What caused the earlier deliberate destruction inside the refuge, and how was it connected to the Dongting Fisherman or another intruder?",
    "What are the origin and purpose of the symbols shared by the Arch Lich’s magic circle and Dark Heaven’s formations?",
    "Who destroyed Donghu Stronghold and the related Yangtze River Channel League strongholds, why was no Moving Formation trace left, and was the destruction a diversion?",
    "What caused the Dongting Fisherman’s involuntary movement and terrified warning, and what produced the enormous roar behind Taekyung?"
  ],
  "safe_through": 467,
  "temporary_decisions": [
    "Render 천잠사 as Heavenly Silkworm Thread, 운철 as meteorite iron, 초인 as superhuman, and 극쾌 as extreme swiftness.",
    "Render 노괴 as old monster, 신병이기 as divine weapon, 수상 구조대원의 물갈퀴 as Water Rescue Worker’s Webbed Feet, and 수상 구조대원의 아가미 as Water Rescue Worker’s Gills.",
    "Preserve Taekyung’s dry contemporary humor and blunt profanity; render 씨부럴 as sibu-leol in direct abuse.",
    "Preserve the Dongting Fisherman’s emotionless, inhuman presentation and violent combat voice.",
    "Continue rendering 오기조원 as Five Qi Returning to Origin, 노화순청 as Furnace Fire Pure Blue, 반로환동 as Returned to Youth, and 복자 as diviner."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 해상왕    | **Seafaring King**            | Pa Ryun        |
| 소림     | **Shaolin**                      |
| 무당파    | **Wudang**                       |
| 암천     | **Dark Heaven**                  |
| 제갈세가   | **Zhuge Clan**                   |
| 장강수로맹  | **Yangtze River Channel League** |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 신법     | **movement technique**                           |                                                       |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 가주     | **Family Head**                              |
| 장문인    | **Sect Leader**                              |
| 제자     | **Disciple**                                 |
| 사형     | **Senior Brother**                           |
| 사제     | **Junior Brother**                           |
| 선배     | **Senior**                                   |
| 시스템              | **System**                     |
| 사천     | **Sichuan**            |
| 노부      | **this old man / I**                                            |
| 소협      | **Young Hero**                                                  |
| 대사      | **Master** for a senior Buddhist monk                           |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 현공진인 | **Perfected Being Hyeongong** | Veteran Wudang Daoist master and the current Sect Leader's Junior Brother. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 무송 | **Mu Song** | Lord of Water Dragon Stronghold and disciple of the Seafaring King. |
| 문경 | **Mungyeong** | Young medical apprentice and newly introduced passenger. |
| 제갈풍 | **Zhuge Feng** | Current Family Head of the Zhuge Clan. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 오대세가 | **Five Great Families** | Major Murim grouping. |
| 무재 | **martial talent** | Innate aptitude for learning martial arts. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 허공섭물 | **Seizing an Object Through Empty Space** | Technique Jeok Cheongang uses to lift Jang Taebo remotely. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 멸염신권 | **Flame-Extinguishing Divine Fist** | Named fist technique Taekyung announces at the chapter's end. |
| 도도 | **Dodo** | Term for the Star-Array Grand Banquet's major gambling matches. |
| 반로환동 | **Returned to Youth** | Possible explanation for an apparently young Supreme Peak master. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 선장 | **Zen staffs** | Staff weapons carried by the Hundred and Eight Arhats. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 호북 | **Hubei** | Province on Ju Gongsan's route from Guangdong to Henan. |
| 겁화 | **hellfire** | Destructive fire energy used by Taekyung. |
| 수룡채 | **Water Dragon Stronghold** | Major river stronghold belonging to the Yangtze River Channel League. |
| 선화아 | **Ship-Fire Boy** | Mu Song's sobriquet; literally a child who lights fires aboard a ship. |
| 장강 | **Yangtze** | The river controlled by the Yangtze River Channel League. |
| 의생 | **medical apprentice** | Mungyeong's occupation. |
| 동봉 | **Dong Feng** | Personal name of the Divine Physician and Mungyeong's Master. |
| 등평도수 | **Rising on Duckweed, Crossing Water** | Comparable movement feat for walking across water. |
| 오대 | **Five Squads** | Named Tang Clan organizational group in Tang Sadok's mobilization order. |
| 마두 | **fiend** | Demonic martial masters from the Great Faction War era. |
| 유령환살보 | **Ghost Illusory Slaughter Step** | Movement technique used by the Slaughter Saint. |
| 달마대사 | **Bodhidharma** | Famous Shaolin figure cited alongside Lü Dongbin and Jang Samfeng. |
| 와룡객 | **Crouching Dragon Guest** | Epithet of Zhuge Feng. |
| 장강일도 | **Yangtze One Saber** | Hwang Chung's sobriquet. |
| 천령폭 | **Tianling Falls** | Dangerous waterway leading to Donghu Stronghold. |
| 동정호 | **Dongting Lake** | Lake under which Dangyang and Honghu Strongholds operated. |
| 쾌조선 | **swift ship** | Fast vessel operated by the Yangtze River Channel League. |
| 호북성 | **Hubei Province** | Province where the chapter’s Dark Heaven incidents occurred. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 진태경 | 선배님들 | junior_to_senior_team_members | Seniors | polite-but-threatening | Taekyung addresses the Myeongdong Guild Team 1 Hunters while ordering them to clear a path. |
| 진태경 | 무송 | junior_martial_artist_to_senior_martial_artist | Senior | formal-polite | Taekyung uses 선배님 after recognizing Mu Song as a senior martial artist and disciple of the Seafaring King. |
| 문경 | 무송 | survivor_to_savior_and_authority | Great Hero Mu Song | formal-deferential | Mungyeong credits Mu Song with saving him and asks him to spare Hwang Tae-gu. |
| 무송 | 문경 | stronghold_lord_to_young_passenger | you | gruff-but-considerate | Mu Song offers Mungyeong the right to decide Hwang Tae-gu's fate. |
| 진태경 | 문경 | young_martial_artist_to_medical_apprentice | Young Hero | formal-polite | Taekyung addresses the non-martial Mungyeong as 소협 while praising his actions. |
| 문경 | 진태경 | young_passenger_to_younger_martial_artist | Young Hero | deferential | Mungyeong uses 소협 while asking Taekyung for help boarding the ship. |
| 무송 | 진태경 | senior_martial_artist_to_junior_martial_artist | Junior | familiar-teasing | Mu Song calls Taekyung 후배 and jokes about his supposed taste for men. |
| 진태경 | 동봉 | visitor_to_divine_physician | Old Man Dong | formal-polite and deferential | Adopts Dong Feng's requested address after learning his personal name. |
| 문경 | 동봉 | disciple_to_master | Master | deferential and apologetic | Reveals Dong Feng's identity and apologizes for bringing the party without permission. |
| 동봉 | 진태경 | physician_to_visiting_young_martial_artist | Young Master Jin | formal-polite and gentle | Uses 진 공자 while welcoming and speaking with Taekyung. |
| 동봉 | 문경 | master_to_disciple | Gyeong | familiar-commanding | Dong Feng tells Mungyeong to remain at the clinic and care for the patients. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 문경 | 적천강 | old_acquaintances | Fire King | familiar and grave | The figure bearing Mungyeong’s name greets Jeok Cheongang by his established epithet. |
| 무송 | 적천강 | junior_martial_artist_to_legendary_martial_master | Great Hero Jeok | formal-deferential | Mu Song respectfully refers to Jeok Cheongang as 적 대협 while worrying that Jeok dislikes him. |
| 중년인 | 진태경 | veteran civilian Hunter to celebrated allied Hunter | Mr. Jin | formal-polite and awed | The casualty clerk addresses Jin as 진 선생님 after Jin asks him to list Lei Fei among the dead. |
| 진태경 | 중년인 | celebrated Hunter to older fellow Hunter | sir | casual and teasing | Jin addresses the older Hunter as 아저씨 while joking with him and giving him instructions. |
| 적천강 | 문경 | overwhelming elder to old acquaintance | you / little punk | mocking and threatening | Mocks Mungyeong's expression and threatens to poke out his eyes. |
| 적천강 | 무송 | legendary martial master to stronghold lord | you | gruff, coercive, and dismissive | Uses 자네 while ordering Mu Song to take the group only as far as Sichuan and leave the fast ship. |
| 적천강 | 제갈풍 | senior_martial_artist_to_old_acquaintance | you / ill-mannered brat | blunt, familiar, and teasing | Jeok treats Zhuge Feng as the younger acquaintance he remembers from childhood. |
| 제갈풍 | 적천강 | younger_old_acquaintance_to_legendary_senior | Senior | respectful but relaxed | Zhuge Feng recalls Jeok's earlier visit and addresses him as an old senior. |
| 제갈풍 | 무송 | family_head_to_stronghold_lord | Ship-Fire Boy Mu Song | calm, formal, and pointed | Zhuge Feng stops Mu Song from leaving by saying the coming information concerns him. |
| 무송 | 제갈풍 | stronghold_lord_to_orthodox_family_head | Great Hero Zhuge | formal and concerned | Mu Song addresses Zhuge Feng after realizing why he was asked to remain. |
| 제갈풍 | 진태경 | senior strategist_to_younger_martial_artist | you | calm and familiar | Uses 자네 while inviting Taekyung to continue questioning the Hubei incident. |
| 현공진인 | 제갈풍 | senior Wudang master to Zhuge Clan Family Head | Family Head Zhuge | formal-respectful | Uses 제갈가주 while discussing the fast ship and the route. |
| 제갈풍 | 현공진인 | Zhuge Clan Family Head to senior Wudang master | Perfected Being Hyeongong | formal-deferential | Addresses Hyeongong with marked respect and calls his presence a great reinforcement. |
| 제갈풍 | 문경 | old acquaintance to revealed legendary assassin | Slaughter Saint | excited and respectful | Zhuge Feng identifies Mungyeong by his established sobriquet after recognizing his identity. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 467
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Hyeongong.md

# Perfected Being Hyeongong (현공진인)

- **Safe through:** Chapter 463
- **Aliases:** None
- **Role:** Perfected Being Hyeongong is a veteran Wudang Daoist master of the previous generation, the current Sect Leader's Junior Brother, and a Supreme Peak swordsman who reached the ultimate stage of the Taiji Wisdom Sword.
- **Personality:** Hyeongong is humble and self-deprecating about his limited worldly knowledge while carrying the authority of an experienced senior master.
- **Voice:** Measured, respectful, and lightly self-deprecating.
- **Relationships:** Hyeongong is the current Wudang Sect Leader's Junior Brother and a respected senior to Zhuge Feng.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 463
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin and Furnace Fire Pure Blue, and Jin Taekyung's Master.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, and pathologically afraid of water. His meeting with Taekyung rekindled his will to live, making him determined to extend his life despite his illness.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 466
- **Aliases:** Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, a Supreme Peak master who has manifested Force, opened his Middle Dantian, crossed the wall into true mastery, can perceive the texture of qi well enough to sever layered magic, and is publicly recognized as an S-rank-level Hunter while formally retaining an A-rank license pending testing.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate, student, and trusted manager of media and official arrangements, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, and Xiao Shen regards him as an older brother after Jin saved him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 466
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Mu Song.md

# Mu Song (무송)

- **Safe through:** Chapter 456
- **Aliases:** Ship-Fire Boy
- **Role:** Lord of Water Dragon Stronghold, a Peak master and the Seafaring King's second martial Disciple who controls major Yangtze river traffic in Sichuan and belongs to the Yangtze River Channel League's moderate faction.
- **Personality:** Ambitious, domineering, impatient with interruptions, and capable of pragmatic cooperation when circumstances demand it.
- **Voice:** Deep and low in private, shifting to dry authority or boisterous command when addressing subordinates and rivals.
- **Relationships:** Mu Song is a member of the Yangtze River Channel League's moderate faction; Hwang Chung, his senior and Uncle Hwang, was the League elder and Donghu Stronghold Lord who was killed in its destruction.

### Mungyeong.md

# Mungyeong (문경)

- **Safe through:** Chapter 467
- **Aliases:** None
- **Role:** Mungyeong is the legendary physician known as the former Divine Physician and Slaughter Saint, having passed the Divine Physician title to his Disciple, and he has reached the Returned to Youth realm.
- **Personality:** Compassionate, resolute, resourceful, and calm under extreme pressure.
- **Voice:** His Mungyeong persona is timid, deferential, and cheerful, while his Slaughter Saint voice is dry, impassive, and blunt.
- **Relationships:** Dong Feng is his Disciple, while Jeok Cheongang, Jin Taekyung, Cheongpung, and the two Sect Leaders know his Slaughter Saint identity.

### Zhuge Feng.md

# Zhuge Feng (제갈풍)

- **Safe through:** Chapter 463
- **Aliases:** Crouching Dragon Guest
- **Role:** Zhuge Feng is the current Family Head of the Zhuge Clan and father of its Lesser Family Head, Zhuge Gyun.
- **Personality:** Analytical and disarmingly casual, he treats comfort and time as principles while delivering grave intelligence with unsettling directness.
- **Voice:** Clear, calm, polished, and conversational, with understated humor and pointed questioning.
- **Relationships:** Zhuge Gyun is his son, and Zhuge Gonghu was his grandfather.

## Korean source

```text
＃468화



쿠구구궁, 콰아아아!

그건 지금껏 누구도 경험해 본 적 없는 폭풍우였다.

뇌성벽력과 함께 천둥이 울려 퍼질 때마다 빗줄기는 거세어졌고, 강물은 난폭하게 용틀임했다.

그리고 그 모든 것들을 거슬러 올라가려는 한 척의 배가 있었다.

“좌현으로!”

격랑 앞의 버들잎처럼 흔들리는 배의 선미에서 터져 나온 선화아(船火兒) 무송의 고함에, 수룡채의 수적들이 이를 악물었다.

“이이이익!”

“계속 저어! 궁둥짝에 힘 빡 주고 저으란 말이다!”

“지금부터 퍼지는 놈은 나중에 각오해라! 그 뭐냐, 그래! 찍먹형에 처하겠다!”

“으아아아!”

이들 역시 하나같이 잔뼈가 굵은 뛰어난 수부(水夫)들.

하지만 무송의 노련한 지휘와 젖 먹던 힘까지 끌어올린 수적들의 노력에도, 지금껏 겪은 적 없는 최악의 날씨는 더 이상 배의 진입을 허락하지 않았다.

콰아아아아! 쿵!

찢어질 듯이 팽창한 돛이 바람의 힘을 이기지 못하고 밀려나고, 사방에서 날아온 크고 작은 돌무더기가 갑판 위를 강타한다.

이 믿기지 않는 광경에 무송의 눈동자에는 경악이 스쳤다.

‘이 무슨!’

그가 스승인 해상왕에게서 배운 것은 무공뿐만이 아니었다.

아니, 오히려 무공보다 갖가지 선박에 대한 조종술과 기상을 예측하고 물길을 읽는 것을 가장 먼저 배웠다.

무송은 무림인이기 이전에 뱃사람이었고, 능력 없는 선장을 따르는 수적은 존재하지 않으니까.

그렇게 장강을 동경하던 꼬마는 늙은 뱃사람들도 인정할 만큼 뛰어난 선장이 되었다. 사제 간의 정이라고는 눈곱만큼도 없는, 삭막한 스승조차 이렇게 말할 정도였다.



‘아쉽구나. 네놈의 독심과 무재(武才)가 배 다루는 솜씨의 절반만 되었더라면 네 사형을 대신할 수 있었을 터인데.’



장강수로맹의 주인은 두 사람이 될 수 없다.

자신의 장제자를 후계로 낙점한 해상왕은 무송을 사천으로 보냈고, 수룡채를 세운 무송은 얼마 지나지 않아 두각을 드러내며 젊은 나이에 사천의 장강을 휘어잡았다.

하지만 그런 무송에게조차 지금과 같은 광경은 난생처음 보는 것이었다.

아마 스승인 해상왕, 일평생을 뱃사람으로 살다가 은퇴한 늙은 수적들 역시 마찬가지였을 것이다.

‘분명 장강의 지류를 벗어날 때만 해도 이렇지는 않았다. 한데 어찌……!’

이유는 간단했다.

급격하다 못해 경악할 정도의 기상 변화.

현재 그들이 위치한 곳은 다름 아닌 동정호였다.

갑작스러운 제갈풍의 호출을 받은 무송은 가장 솜씨 좋은 수하들을 추려 천령폭을 넘었고, 곧장 진태경의 행방을 수소문하여 동정호로 나아갔다.

그리고 얼마 지나지 않아, 바다 한복판에서나 볼 법한 폭풍우와 맞닥트린 것이다.

‘이게 가능한 일인가? 그것도 동정호에서?’

호북성의 기후는 대체로 따뜻한 편에 속한다. 매해 강수량도 고른 편이며, 간혹 장강이 범람하긴 하지만 그 정도가 심하지 않고 오히려 비옥한 곡창지대를 이룰 수 있는 원동력이 된다.

동정호? 분명 천하에서 세 손가락 안에 드는 크기지만 그래 봤자 호수다.

아무리 악천후라고 한들 장강의 물살보다는 못하며, 종잡을 수 없는 바다의 소용돌이에 비하면 우습다.

분명 그렇게 생각했었다. 적어도 두 시진 전까지는.

‘처음 배를 띄울 때만 해도 이 정도는 아니었거늘.’

그다지 큰 걱정은 없었다. 장강과 해상로가 이어지지 않은 동정호에 쾌조선을 옮길 수는 없는 법이라, 자그마한 상선(商船) 한 척을 빌려 진태경 일행이 향했다는 곳으로 나아갔다.

아니, 나아가려 했다.

그러나 처음과 달리 목적지에 가까워질수록 날씨는 최악을 향해 치달았다.

마치 보이지 않는 어떤 선을 넘은 것처럼, 호수에서 볼 수 없는 괴이한 현상들이 곳곳에서 일어나고 있었다.

휘오오오오.

소름 끼치는 바람 소리와 함께 솟아오르는 용오름.

까마득한 높이의 그것이 좁은 폭을 틀어막은 채 상선을 향해 다가오자, 무송의 악문 잇새 사이로 신음이 흘러나왔다.

“이런 개 같은 일이…….”

저것에 휘말리면 끝장이다. 저 용오름을 넘어간다 해도 내구성이 보잘것없는 상선으로는 오래 버티지 못하리라.

수하들의 안위와 장강일도를 죽인 암천을 향한 복수심 사이에서 갈등하던 그가 마침내 입술을 달싹였다.

“송구합니다만, 아무래도 여기까지인 것 같습니다.”

늙수그레한 목소리가 대답했다.

“충분하다.”

그리고 다음 순간.

팟!

무송의 뒤, 한 치의 흔들림 없이 중심을 잡고 있던 자그마한 신형이 돛대를 밟으며 솟구쳤다.

휘몰아치는 비바람을 뚫고 용오름을 향해 쇄도한 그가 주먹을 그러쥐었다.

고오오오옹.

한 줄기의 바람이 검버섯 핀 주먹을 감쌌다. 공기가 움직임을 멈추고, 한 방울의 비바람도 감히 범접하지 못했다.

그리고 그 주먹의 끝에, 모든 것을 태워 버릴 겁화가 깃들었다.

“썩 꺼져라.”

용암이 끓어오르는 듯한 목소리와 함께, 화왕(火王) 적천강은 일권을 내질렀다.

멸염신권(滅炎神拳).

콰우우우우!

다음 순간, 무송과 수적들은 똑똑히 볼 수 있었다.

주먹에서 피어오른 불꽃이 화룡으로 화하여 용오름의 허리를 물어뜯는 광경을.

극강의 열양지기에 회오리치던 물살이 단숨에 허물어지고 모든 수분이 증발했다. 만근에 달하는 힘을 간직한 채 상선을 향해 다가오던 용오름이 자욱한 수증기가 되어 안개처럼 주위를 뒤덮는다.

바로 그때.

파앙!

묵직한 파공성과 함께 수증기가 흩어졌다.

허공을 밟은 채 우뚝 선 적천강이 상선을 굽어보았다. 평소와는 다른, 깊게 가라앉은 목소리가 그의 입술 사이로 흘러나왔다.

“뭐 하나, 어서 따라오지 않고.”

그건 무송과 휘하의 수적들에게 한 말이 아니었다. 그들의 역할은 처음부터 정해져 있었고, 충분히 제 몫을 해냈다.

곧 펼쳐질 전장은…… 진정한 강자들에게만 허락된 곳이다.

그리고 모두의 시선을 받으며, 한 사람이 앞으로 나섰다.

“일위도강(一葦渡江). 소림의 달마대사도 강을 건너기 위해서 갈대잎을 사용했지. 지금부터 괜히 공력 낭비하지 말고 내려오는 게 좋을 거다.”

도무지 감정이라고는 찾아볼 수 없는 무미건조한 목소리.

얼마 전까지만 하더라도 밝고 따뜻하게 병자를 돌보던 소년 의생의 모습은 어디에도 찾아볼 수 없다.

무송과 수적들이 움찔거리며 길을 비키자 문경이 내심 혀를 찼다.

‘동봉. 이 불민한 제자 녀석 같으니. 결국 네가 원하던 대로 되었구나.’

장장 사십여 년을 의생으로 살았다.

일천이 넘는 목숨을 앗아 갔던 손으로 아픈 병자들을 치료하고 보살폈다.

마두(魔頭) 대신 역병이라는 놈을 잡았고, 신의라는 허명을 얻었지만 단 한 번도 재물을 취하거나 공명심을 탐하지 않았다.

그것은 그저 속죄였고, 다짐이었다.

하지만 지금, 의생으로 살아오며 수십 년간 쌓아 올린 마음 깊숙한 곳의 석탑이 무너져 내렸다.

아니, 어쩌면 석탑이 무너진 것은 사천을 떠나는 쾌조선에 몸을 실었던 그날이었을지도 모르겠다.

‘이 또한 노부가 선택한 길. 어찌 남을 탓할까.’

실소를 흘리며 앞으로 나서는 그의 등 뒤로, 헝클어진 문사 복장의 중년인이 모습을 드러냈다.

“이 후배도 노선배님들과 함께 가겠습니다.”

제갈세가의 당대가주, 와룡객(臥龍客) 제갈풍의 말에 문경이 건조한 목소리로 대답했다.

“당연히 그래야지. 아니라면 왜 너 같은 짐덩어리를 데려왔겠느냐?”

“사람을 무안하게 만드는 재주가 있으십니다그려.”

문경은 짐짓 눈살을 찌푸렸다. 자신에 비하면 핏덩어리나 다름없는 제갈풍의 주절거림을 들어줄 생각 따윈 없었다.

“헛소리 집어치우고 업혀라.”

“이 후배를 얕보시는군요. 제 깨달음이 오대세가의 다른 가주들 만큼은 아니어도 공력 하나만큼은…….”

“널 이곳까지 데려온 이유는 그만한 이유가 있기 때문이다. 무공을 우선시했다면 차라리 무당파의 현공(玄空), 그 아이를 데려왔겠지. 하지만 누구 하나는 그곳에 남아 있어야 하지 않겠느냐?”

“……!”

현공진인은 구파일방의 장문인들과 어깨를 나란히 하는 배분의 고수.

무림에서도 존경받는 원로인 현공진인을 아이라 부르는 문경의 언행에, 반로환동(返老還童)의 고수라는 것 외에는 그의 정체를 정확히 파악하지 못한 무송과 휘하의 수적들은 화들짝 놀랐다.

“헙!”

“저, 저분은 대관절 누구시길래…….”

그러나 문경은 답해 줄 생각도, 시간도 없었다.

그가 손을 쭉 뻗자 제갈풍의 신형이 주르륵 끌려왔다.

다른 누구도 아닌 제갈세가의 당대 가주를 허공섭물(虛空攝物)로 움켜쥔 문경이 가볍게 갑판을 딛고 새처럼 솟구쳤다.

팟!

은밀하면서도 더할 나위 없이 표횰한 신법.

극성에 달한 유령환살보(幽靈幻殺步)를 알아볼 수 있는 사람은 배에 남겨진 이들 중 단 한 사람도 없었다.

입을 딱 벌리는 그들을 뒤로한 문경의 신형이 공간을 접으며 쏘아졌다.

“이 방향이 맞느냐?”

촤악!

쾌속하게 강물 위를 밟으며 나아가는 두 개. 아니, 세 개의 신형.

적천강의 질문에 문경의 손에 의해 대롱대롱 매달려 있는 제갈풍이 대답했다.

“선화아가 알려 준 대로라면, 이대로 곧장 앞으로만 이동하면 합니다.”

“확실한 것이냐?”

“물론입니다. 다만…….”

“다만?”

잠시 망설이던 제갈풍이 말을 이었다.

“그곳에 진 소협이 있을지는 아직 미지수입니다.”

“있다, 분명히.”

적천강이 즉각 고개를 저었다. 확신에 가까운 어조였다.

“지금과 같은 날씨…… 결코 우연이 아니다. 알 수 없는 무엇인가가 이곳에 왔고, 태경이 그 아이를 노리고 있음이 분명해.”

“속단하기에는 이르다. 그것의 정체부터 파악하는 것이 우선이니.”

이어진 문경의 말에 적천강은 자신도 모르게 품 안을 더듬었다.

검날처럼 날카롭고, 갑옷처럼 단단한 무엇인가가 손에 잡혔다.

문경이 이것을 처음 가져와 그 두 사람 앞에 보여 주었을 때, 적천강과 제갈풍 모두 이것의 정체를 믿지 못했다.

‘무엇이냐. 대관절 무슨 일이 벌어지고 있단 말이냐.’

늙은 가슴 안에서 빠르게 크기를 부풀리는 불안감만큼, 등평도수(登萍渡水)의 수법으로 강을 가로지르는 속도도 빨라지던 바로 그때였다.

콰과과과과광!

휘몰아치는 거센 비바람과 자욱한 안개 너머 들려온 엄청난 굉음에 그들 세 사람은 눈을 크게 떴다.

“이건…….”

하늘에서 울려 퍼진 뇌성벽력이 아니었다.

그들의 머리 위로 펼쳐진 검은 하늘은 잠잠했고, 조금 전의 엄청난 굉음은 분명 수백 장 앞의 전방으로부터 들려온 것이었다.

“이놈들-!”

쩌렁쩌렁한 노호성을 내지른 적천강의 신형이 가장 먼저 쏘아졌고, 제갈풍을 단단히 붙잡은 문경이 그 뒤를 따르자 양옆으로 물살이 갈라졌다.

하지만 불과 촌각이 지나기도 전에 그들 세 사람은 동시에 멈춰 설 수밖에 없었다.

“……!”

누구 하나 입을 열 수 없을 만큼 거대한 충격.

굳이 정체를 확인하기 위해 가까이 다가갈 필요조차 없었다.

마침내 저 멀리 모습을 드러낸 ‘그것’의 정체에, 세 사람은 할 말을 잃은 채 우뚝 굳어 버렸다.



* * *



쿠구구구궁!

굉음과 함께 절벽이 무너져 내린다.

수백 년간 그 일부였음이 분명한 만근거석이 소나기처럼 쏟아져 내리고, 엄청난 물보라가 솟구쳤다.

하지만 그런 것 따위는 아무래도 상관없었다.

나는 떨리는 눈빛으로 그 모든 것들 사이로 몸을 일으키는 ‘그것’을 바라보았다.

정확히는 그것의 머리 위에 떠오른 시스템 창을.



[Lv.??? 변이된 수신룡(水神龍)]
```

## Final English reading copy

```markdown
# Chapter 468

*Rumble-rumble-rumble, crash!*

It was a storm unlike anything anyone had ever experienced.

Every time thunder boomed alongside the lightning, the rain grew heavier, and the river thrashed like a violent dragon.

And one ship was trying to make its way against it all.

“Hard to port!”

At Ship-Fire Boy Mu Song’s shout from the stern of the ship, which rocked like a willow leaf before the raging waves, the river bandits of Water Dragon Stronghold gritted their teeth.

“Grrrrgh!”

“Keep rowing! Put your asses into it and row!”

“Anyone who slacks off from this moment on had better watch out! What was it called again? Right! I’ll sentence you to the dip-and-taste punishment!”

“Aaaaaah!”

Every one of them was an experienced, highly skilled sailor.

But despite Mu Song’s seasoned commands and the river bandits’ efforts to summon every last ounce of strength they possessed, the worst weather they had ever encountered refused to let the ship advance any farther.

*Crash! Boom!*

The sail, stretched to the point of tearing, gave way beneath the force of the wind. Rocks of every size came flying from all directions and slammed into the deck.

Mu Song’s eyes flashed with disbelief at the impossible sight.

*What in the world is this?*

What he had learned from his Master, the Seafaring King, was not limited to martial arts.

If anything, he had first learned how to steer all sorts of ships, predict the weather, and read the currents—before he had learned martial arts.

Mu Song had been a sailor before he was a Murim martial artist, and no river bandit would follow a captain without the ability to lead.

The little boy who had yearned for the Yangtze had grown into a captain so skilled that even old sailors acknowledged him. Even his bleak Master, who possessed not a trace of affection for his Disciple, had once said:

> “It’s a shame. If your grit and martial talent had been even half as good as your skill with ships, you might have taken your Senior Brother’s place.”

There could not be two masters of the Yangtze River Channel League.

The Seafaring King, who had chosen his Senior Disciple as his successor, sent Mu Song to Sichuan. After founding Water Dragon Stronghold, Mu Song soon distinguished himself and seized control of Sichuan’s Yangtze at a young age.

Yet even Mu Song had never seen anything like this.

His Master, the Seafaring King, and the old river bandits who had spent their entire lives as sailors before retiring had probably never seen it either.

*It wasn’t like this when we left the Yangtze tributary. So how…?*

The reason was simple.

A sudden change in the weather—so drastic that it was shocking.

Their current location was none other than Dongting Lake.

After receiving Zhuge Feng’s sudden summons, Mu Song had selected his most capable subordinates, crossed Tianling Falls, and immediately set out for Dongting Lake after asking around for Jin Taekyung’s whereabouts.

Not long afterward, they had run into a storm more suited to the middle of the sea.

*Is this even possible? On Dongting Lake?*

Hubei Province’s climate was generally warm. Its annual rainfall was fairly consistent, and although the Yangtze occasionally flooded, the flooding was rarely severe. In fact, it was one of the reasons the region had become such a fertile breadbasket.

Dongting Lake? It was certainly one of the three largest lakes under heaven, but it was still only a lake.

No matter how bad the weather became, it should not have been worse than the Yangtze’s current. Compared to the unpredictable whirlpools of the sea, it should have been laughable.

That was what he had believed.

At least until two shichen ago.

*It wasn’t this bad when we first launched the ship.*

He had not been particularly worried. Since Dongting Lake was not connected to the Yangtze or the sea routes, there was no way to bring a swift ship here. They had borrowed a small merchant vessel instead and headed for the place where Jin Taekyung’s group was said to have gone.

Or rather, they had tried to.

Unlike at the beginning, the weather had worsened the closer they came to their destination.

It was as though they had crossed some invisible line. Strange phenomena that should not have been possible on a lake were appearing everywhere.

*Whoooooosh.*

A waterspout rose with a chilling howl of wind.

It towered to a dizzying height, blocking the narrow waterway as it advanced toward the merchant vessel, a groan slipped between Mu Song’s clenched teeth.

“What the fucking hell is this…?”

If they were caught in that, it was over. Even if they managed to get past the waterspout, the merchant vessel’s poor durability would not let it survive for long.

Torn between concern for the safety of his subordinates and his desire for revenge against Dark Heaven, which had killed Yangtze One Saber, Mu Song finally moved his lips.

“I’m sorry, but I’m afraid this is as far as we can go.”

An old voice answered him.

“That’s enough.”

And then—

*Snap!*

Behind Mu Song, a small figure that had remained perfectly balanced leaped from the mast.

The figure shot toward the waterspout through the driving rain and wind, then clenched a fist.

*Hooooong.*

A single stream of wind wrapped around the fist mottled with age spots. The air stopped moving, and not a single drop of rain dared approach.

At the tip of that fist, hellfire capable of burning everything took shape.

“Get the hell out of my way.”

Alongside a voice like boiling lava, Fire King Jeok Cheongang threw a punch.

*Flame-Extinguishing Divine Fist.*

*Whoooooosh!*

The next moment, Mu Song and the river bandits saw it clearly.

The flames rising from the fist transformed into a fire dragon and bit into the waist of the waterspout.

The churning water collapsed in an instant beneath the overwhelming Scorching Yang Qi, and all its moisture evaporated. The waterspout, which had been approaching the merchant vessel with the power of ten thousand *geun*, became a dense cloud of steam that spread like fog around them.

Then—

*Boom!*

The heavy sound of something splitting the air scattered the steam.

Jeok Cheongang stood tall in midair, looking down at the merchant vessel. His voice, more deeply subdued than usual, drifted from his lips.

“What are you waiting for? Hurry up and follow me.”

He was not speaking to Mu Song or the river bandits under his command. Their roles had been decided from the beginning, and they had more than fulfilled them.

The battlefield that was about to unfold was a place permitted only to true masters.

And as everyone watched, one person stepped forward.

“Single Reed Crossing the River. Even Master Bodhidharma of Shaolin used a reed leaf to cross a river. From now on, you’d better come down instead of wasting your internal energy for no reason.”

There was not even a trace of emotion in the dry, monotonous voice.

The bright, warm boy who had been caring for the sick as a medical apprentice only a short while ago was nowhere to be found.

As Mu Song and the river bandits flinched and stepped aside, Mungyeong clicked his tongue inwardly.

*Dong Feng. You foolish Disciple. In the end, things turned out exactly as you wanted.*

He had lived as a medical apprentice for more than forty years.

With hands that had taken more than a thousand lives, he had treated and cared for sick patients.

Instead of fiends, he had fought the bastard called plague. He had gained the undeserved reputation of being a Divine Physician, but he had never once taken wealth or chased fame.

It had merely been atonement.

And a vow.

But now, the stone pagoda he had built deep within his heart over decades of living as a medical apprentice had come crashing down.

No—perhaps the stone pagoda had collapsed on the day he boarded the swift ship leaving Sichuan.

*This is also the path this old man chose. How could I blame anyone else?*

With a dry chuckle, he stepped forward. Behind him, a middle-aged man in disheveled scholar’s robes appeared.

“This junior will go with you, Seniors.”

At the words of Zhuge Feng, the current Family Head of the Zhuge Clan and the Crouching Dragon Guest, Mungyeong answered in a dry voice.

“Of course you should. Why else would I bring a burden like you?”

“You certainly have a talent for embarrassing people.”

Mungyeong made a show of frowning. He had no intention of listening to Zhuge Feng’s rambling, especially when the man was no more than a babe compared to him.

“Enough nonsense. Get on my back.”

“You underestimate this junior. My enlightenment may not match that of the other Family Heads of the Five Great Families, but when it comes to internal energy alone…”

“There’s a reason I brought you here. If I had prioritized martial arts, I would have brought that youngster Hyeongong of Wudang instead. But shouldn’t someone remain back there?”

“……”

Perfected Being Hyeongong was a master senior enough to stand shoulder to shoulder with the Sect Leaders of the Nine Sects and One Gang.

Mu Song and the river bandits had been unable to determine Mungyeong’s identity beyond knowing that he was a Returned to Youth master. They were shocked by the way he referred to the respected elder, Perfected Being Hyeongong, as a child.

“Gasp!”

“Who in the world is that man…?”

But Mungyeong had neither the time nor the inclination to answer.

He stretched out his hand, and Zhuge Feng’s body came sliding toward him.

After seizing none other than the current Family Head of the Zhuge Clan with Seizing an Object Through Empty Space, Mungyeong lightly stepped off the deck and leaped like a bird.

*Snap!*

A movement technique both stealthy and impossibly elusive.

Not a single person left aboard the ship could recognize the Ghost Illusory Slaughter Step, perfected to its ultimate stage.

Leaving the stunned men behind, Mungyeong’s body shot forward as though folding space.

“Is this the right direction?”

*Splash!*

Two—no, three figures moved swiftly across the surface of the river.

Zhuge Feng, dangling from Mungyeong’s hand, answered Jeok Cheongang.

“According to what Ship-Fire Boy told us, we only need to move straight ahead from here.”

“Are you certain?”

“Of course. However…”

“However?”

After hesitating for a moment, Zhuge Feng continued.

“We still don’t know whether Young Hero Jin is there.”

“He is. Without a doubt.”

Jeok Cheongang immediately shook his head. His tone was nearly one of certainty.

“This weather… It isn’t a coincidence. Something unknown came here, and Taekyung is clearly after it.”

“It’s too early to jump to conclusions. Identifying what it is must come first.”

At Mungyeong’s words, Jeok Cheongang unconsciously reached inside his robes.

His hand closed around something as sharp as a sword blade and as hard as armor.

When Mungyeong had first brought it and shown it to the two of them, neither Jeok Cheongang nor Zhuge Feng had been able to believe what it was.

*What is this? What in the world is happening?*

Just then, as the unease rapidly swelling in the old man’s chest grew, so did the speed at which he crossed the river with Rising on Duckweed, Crossing Water.

*Rumble-rumble-rumble!*

A tremendous roar rang out from beyond the violent rain and dense fog.

The three men opened their eyes wide.

“This is…”

It was not thunder and lightning rumbling across the sky.

The black sky above their heads was quiet. The enormous sound from a moment earlier had clearly come from somewhere several hundred *jang* ahead of them.

“You bastards—!”

Jeok Cheongang’s furious roar rang out, and his body shot forward first. Mungyeong followed with Zhuge Feng held firmly in his grasp, splitting the water on either side.

But before even an instant had passed, the three men were forced to stop simultaneously.

“……”

The impact was so immense that none of them could open their mouths.

They did not even need to move closer to confirm what had caused it.

At last, the identity of “it” appeared in the distance.

The three men stood frozen, speechless.

* * *

*Rumble-rumble-rumble!*

The cliff collapsed with a deafening roar.

Massive boulders that had clearly been part of it for centuries came pouring down like a rain shower, and an enormous spray of water surged upward.

But none of that mattered.

I stared with trembling eyes at “it” rising from among the destruction.

More precisely, I stared at the System window floating above its head.

> **System**
>
> Lv. ??? Mutated Water God Dragon
```

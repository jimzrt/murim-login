<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0471.txt",
      "sha256": "e42fdbef29adee7339763b95923f99b47a11d86534a10d9a75588818a5295085",
      "bytes": 13233
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "b672fe658ee1e37649404b733036e52ba2d5c6701611e0b551079cb58a7bfc63",
      "bytes": 3196
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "3575ec4ba3b2dca85b94e75e9c1082dbf9e777903603af1582891a8a1835db6d",
      "bytes": 152552
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "c815b7d84a7265512d3e67c186d8a99e87419d301799b5a669408072f2c00687",
      "bytes": 1006
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "8388a228b7d578722c395bcb439f4d258d8294854ff0f42b2f3bd7e6b132c581",
      "bytes": 553
    },
    {
      "path": "characters/Dongting Fisherman.md",
      "sha256": "f2da98db2d3423eab036fad5472a668058624f0906a1ba8bb54f8c058443b77d",
      "bytes": 778
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "f16e88fec0971b499b11e8503ab456724f6cf6e953f0e41d857f92732347e815",
      "bytes": 1542
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "d24a17760792881714cfc9c66eda95762808cca1012e1ca0a9cbe9f99e01c4f9",
      "bytes": 1646
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "bb231f08e6acc9e2ea48a924ec86b5d676c89fe1f1644227ba85703f0c13bae5",
      "bytes": 622
    },
    {
      "path": "characters/Mungyeong.md",
      "sha256": "004712645b0325b15465f267ebd0c75848490d0f1f733abb7c22f3f4a0874553",
      "bytes": 734
    },
    {
      "path": "characters/Zhuge Feng.md",
      "sha256": "785c7949ab8b762214f228f7919131c18360c6e75ee450c1bc768fbecd82bd4a",
      "bytes": 626
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "02c75e82577b427aa72f777610f13623d2bfa8352fe24570f94fb4b00282bace",
      "bytes": 147215
    }
  ],
  "estimated_tokens": 12862
}
-->

# Durable State Update — Chapter 471

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 471. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 471. Profile updates may replace only one
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
  "chapter": 471,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 471,
    "continuity_sources": [471],
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
    "A forced System Quest, Corrupted Spirit Beast, is active for Taekyung; Logout is disabled until it ends.",
    "The Quest requires Taekyung to defeat the Mutated Water God Dragon; its Grade is Supreme Peak and failure means death or an equivalent penalty.",
    "The Mutated Water God Dragon was once a noble spirit beast that waited to ascend in deep river water before an unknown power corrupted it into an evil beast.",
    "Taekyung cut dozens of the dragon's whiskers but suffered a shoulder injury and was then struck by its tail; Cheongpung caught him before he hit the cliff.",
    "Cheongpung is unaffected by the dragon's Fear and is protecting the unconscious Dongting Fisherman and old boatman.",
    "Gung Gibang and Hyuk Mujin were brought out of Fear by Taekyung's slaps but remain shaken by the dragon's ordinary terror.",
    "The ferryboat was destroyed by the dragon's falling boulders; the Dongting Fisherman and old boatman remain alive but unconscious.",
    "The Dongting Fisherman remains severely injured, immobilized by Taekyung's seals, and held alive for interrogation about Dark Heaven.",
    "Taekyung believes the Dongting Fisherman encountered the Mutated Water God Dragon before the group and that its Fear caused his earlier mental disturbance.",
    "Honglan is recovering, while Ju Wongong remains unconscious under guard after passing the most dangerous stage of his injuries.",
    "Jin Wikyung is acting as an inspector for the new Murim Alliance and is cooperating with Taekyung's investigation.",
    "Jeok Cheongang, Mungyeong, and Zhuge Feng are moving toward Taekyung's location, while Hyeongong remains behind."
  ],
  "continuity_sources": [
    470,
    469
  ],
  "open_questions": [
    "What is the Dongting Fisherman's exact role within Dark Heaven, what information will he reveal, and what caused his involuntary movement and terrified warning?",
    "What caused the earlier deliberate destruction inside the refuge, and how was it connected to the Dongting Fisherman or another intruder?",
    "What are the origin and purpose of the symbols shared by the Arch Lich's magic circle and Dark Heaven's formations?",
    "Who destroyed Donghu Stronghold and the related Yangtze River Channel League strongholds, why was no Moving Formation trace left, and was the destruction a diversion?",
    "What unknown power corrupted the Water God Dragon, what are its true origin and purpose, and what is the sharp armor-hard object carried by Jeok Cheongang?"
  ],
  "safe_through": 470,
  "temporary_decisions": [
    "Render 타락한 영물 as Corrupted Spirit Beast and 악물 as evil beast.",
    "Render 기암괴석 as bizarre boulder and preserve jang and geun measurements.",
    "Preserve Taekyung's dry contemporary humor, blunt profanity, and game-like System terminology; retain Cheongpung's dreamy, innocent, increasingly profane voice.",
    "Continue rendering 화룡일미 as Fire Dragon's Single Tail, 강기 as Force, 백염 as White Flame, and 피어 as Fear.",
    "Render the dragon's 수염 as whiskers and its attack descriptions with direct, fast-moving physical imagery."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 청풍     | **Cheongpung**     |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 살성     | **Slaughter Saint**           | —              |
| 열화문    | **Fire Gate Clan**               |
| 화산파    | **Huashan**                      |
| 소림     | **Shaolin**                      |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 경맥     | **meridians**                                    |                                                       |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 살기     | **killing intent**                               |                                                       |
| 검기     | **Sword Energy**                                 | When functioning as projected weapon qi               |
| 정파     | **orthodox faction**                             |                                                       |
| 장문인    | **Sect Leader**                              |
| 제자     | **Disciple**                                 |
| 은인     | **Benefactor**                               |
| 일격     | **One Strike**                         |
| 시스템              | **System**                     |
| 퀘스트              | **Quest**                      |
| 습득               | **Acquired**                   |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 몬스터     | **monster**           |
| 화산     | **Huashan**            |
| 정마대전   | **Great Faction War**         |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 동정어옹 | **Dongting Fisherman** | Publicly condemned the Yangtze River Channel League and disappeared three days before this chapter. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 문경 | **Mungyeong** | Young medical apprentice and newly introduced passenger. |
| 제갈풍 | **Zhuge Feng** | Current Family Head of the Zhuge Clan. |
| 사마외도 | **demonic, heterodox arts** | Suspected martial-arts origin of Pung Yang's insidious forms. |
| 내상 | **Internal Injury** | System condition label for internal injury. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 천자 | **Son of Heaven** | Honorific title for the Emperor. |
| 자하신공 | **Zaha Divine Technique** | Huashan internal-energy technique used by Cheongpung. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 소림사 | **Shaolin Temple** | Temple invoked in Chulwoo’s comparison of Baek Museong’s conduct. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 근골 | **Muscles and Bones** | System attribute increased by 2 during the climb. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 제갈무후 | **Zhuge Wuhou** | Honorific title for Zhuge Liang in the Three Visits allusion. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 태산북두 | **Mount Tai and Northern Dipper of the Murim** | Honorific description of Shaolin's standing in the Murim. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 의생 | **medical apprentice** | Mungyeong's occupation. |
| 살수 | **assassin** | Professional killer considered as a possible suspect. |
| 신교 | **Divine Cult** | Short form used by the Divine Cult's members for the Heavenly Demon Divine Cult. |
| 유령환살보 | **Ghost Illusory Slaughter Step** | Movement technique used by the Slaughter Saint. |
| 화룡갑 | **Fire Dragon Armor** | Jin Taekyung's renamed bound armor, formerly the Black Dragon Armor. |
| 와룡객 | **Crouching Dragon Guest** | Epithet of Zhuge Feng. |
| 흑목조간 | **black-wood fishing rod** | The Dongting Fisherman's distinctive weapon; the broken rod is his only known trace. |
| 비처 | **secret refuge** | Hidden retreat of the Dongting Fisherman. |
| 기경팔맥 | **Eight Extraordinary Meridians** | The eight extraordinary meridians of wuxia physiology. |
| 수신룡 | **Water God Dragon** | Legendary name for the true master of Dongting Lake; distinct from the modern Sea Serpent. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 청풍 | 진태경 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung repeatedly addresses Taekyung as 은인 after receiving food. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 진태경 | 청풍 | companion_to_young_martial_artist | Young Master Cheongpung | formal-polite | Taekyung uses 청 공자 while correcting Cheongpung's royal-etiquette mistake. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 적천강 | 청풍 | overwhelming_elder_to_young_martial_artist | you / little punk | blunt, amused, and threatening | Jeok Cheongang uses 네, 이놈, and related blunt forms while testing Cheongpung. |
| 청풍 | 적천강 | young_martial_artist_to_overwhelming_elder | Grandpa Jeok | casual-familiar despite deference | Cheongpung uses 적 할아버지 while asking Jeok Cheongang to confirm Taekyung's condition; this is a familial form of address, not literal kinship. |
| 진태경 | 문경 | young_martial_artist_to_medical_apprentice | Young Hero | formal-polite | Taekyung addresses the non-martial Mungyeong as 소협 while praising his actions. |
| 문경 | 진태경 | young_passenger_to_younger_martial_artist | Young Hero | deferential | Mungyeong uses 소협 while asking Taekyung for help boarding the ship. |
| 청풍 | 문경 | martial_companion_to_medical_apprentice | Medical Apprentice | cheerful-polite | Cheongpung addresses Mungyeong as 의생님 while asking him to greet the Tang Clan. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 문경 | 적천강 | old_acquaintances | Fire King | familiar and grave | The figure bearing Mungyeong’s name greets Jeok Cheongang by his established epithet. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 적천강 | 문경 | overwhelming elder to old acquaintance | you / little punk | mocking and threatening | Mocks Mungyeong's expression and threatens to poke out his eyes. |
| 적천강 | 제갈풍 | senior_martial_artist_to_old_acquaintance | you / ill-mannered brat | blunt, familiar, and teasing | Jeok treats Zhuge Feng as the younger acquaintance he remembers from childhood. |
| 제갈풍 | 적천강 | younger_old_acquaintance_to_legendary_senior | Senior | respectful but relaxed | Zhuge Feng recalls Jeok's earlier visit and addresses him as an old senior. |
| 제갈풍 | 진태경 | senior strategist_to_younger_martial_artist | you | calm and familiar | Uses 자네 while inviting Taekyung to continue questioning the Hubei incident. |
| 제갈풍 | 문경 | old acquaintance to revealed legendary assassin | Slaughter Saint | excited and respectful | Zhuge Feng identifies Mungyeong by his established sobriquet after recognizing his identity. |
| 진태경 | 동정어옹 | hostile interrogator confronting a suspected perpetrator | you | blunt informal and abusive | Taekyung addresses the Dongting Fisherman without honorifics and calls him a sibu-leol bastard. |
| 문경 | 제갈풍 | legendary_senior_to_younger_family_head | you; burden | blunt, insulting, and commanding | Mungyeong orders Zhuge Feng onto his back and dismisses his objections. |
| 진태경 | 수신룡 | hostile martial artist to monster | you, sibu-leol eel bastard | blunt, insulting, and fearless | Taekyung directly insults the emerged Water God Dragon before attacking it. |

## Listed compact profiles

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 470
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, the grandson and Disciple of Sword Saint Mae Jonghak, and a Supreme Peak martial master known as the Huashan Divine Dragon.
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, a deep love of martial arts, competitive pride, unusual resistance to monster-induced Fear, and discomfort when someone copies his martial arts.
- **Voice:** Dreamy and hazy, with innocent, polite phrasing; he has begun imitating Taekyung's profanity.
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions while Taekyung is his only true martial rival; Tang Sadok has temporarily entrusted Mimi to him.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 470
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Dongting Fisherman.md

# Dongting Fisherman (동정어옹)

- **Safe through:** Chapter 470
- **Aliases:** None
- **Role:** The Dongting Fisherman is a previous-generation Supreme Peak master whose water arts rival the Seafaring King; he joined Dark Heaven, committed the Dongting Lake massacre, and is now captured alive for interrogation.
- **Personality:** The Dongting Fisherman appears eerily emotionless and savage, eating live fish raw and reacting violently when provoked.
- **Voice:** Not established.
- **Relationships:** The Dongting Fisherman opposed the Yangtze River Channel League and was monitored by the Lower District Sect for several years after friction with it, while current records place him in Hubei Province.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 468
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin and Furnace Fire Pure Blue, and Jin Taekyung's Master.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, and pathologically afraid of water. His meeting with Taekyung rekindled his will to live, making him determined to extend his life despite his illness.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 470
- **Aliases:** Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, a Supreme Peak master who has manifested Force, opened his Middle Dantian, crossed the wall into true mastery, can perceive the texture of qi well enough to sever layered magic, can resist high-level monster Fear through exceptional mental strength, and is publicly recognized as an S-rank-level Hunter while formally retaining an A-rank license pending testing.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate, student, and trusted manager of media and official arrangements, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, and Xiao Shen regards him as an older brother after Jin saved him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 470
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Mungyeong.md

# Mungyeong (문경)

- **Safe through:** Chapter 468
- **Aliases:** None
- **Role:** Mungyeong is the legendary physician known as the former Divine Physician and Slaughter Saint, having passed the Divine Physician title to his Disciple, and he has reached the Returned to Youth realm.
- **Personality:** Compassionate, resolute, resourceful, and calm under extreme pressure.
- **Voice:** His Mungyeong persona is timid, deferential, and cheerful, while his Slaughter Saint voice is dry, impassive, and blunt.
- **Relationships:** Dong Feng is his Disciple, while Jeok Cheongang, Jin Taekyung, Cheongpung, and the two Sect Leaders know his Slaughter Saint identity.

### Zhuge Feng.md

# Zhuge Feng (제갈풍)

- **Safe through:** Chapter 469
- **Aliases:** Crouching Dragon Guest
- **Role:** Zhuge Feng is the current Family Head of the Zhuge Clan and father of its Lesser Family Head, Zhuge Gyun.
- **Personality:** Analytical and disarmingly casual, he treats comfort and time as principles while delivering grave intelligence with unsettling directness.
- **Voice:** Clear, calm, polished, and conversational, with understated humor and pointed questioning.
- **Relationships:** Zhuge Gyun is his son, and Zhuge Gonghu was his grandfather.

## Korean source

```text
＃471화



화왕 적천강은 장장 일백 년이 넘는 세월을 살았다.

유리걸식하던 소년은 어느 날 스승을 만나 열화문(烈火門)의 십팔 대 계승자가 되었고, 시간이 흘러 스승이 흙으로 돌아가자 유일한 문도이자 장문인이 되었다.

소년이 청년으로, 청년이 중년으로, 마침내 노인이 되기까지는 실로 장구한 세월이 걸렸다.

그사이 천하의 향방을 가를 거대한 전란(戰亂)이 일어나고 새로운 나라와 천자의 성씨가 바뀌었다.

다섯 번의 홍수와 지진이 일어나자 역병이 창궐했고, 홍건(紅巾)을 두른 도적 떼가 도처에서 일어나 약탈을 일삼았다.

이렇듯 지금껏 그가 목격한 모든 일에는 인간이 불러온 재앙도, 하늘이 내린 천벌도 있었다.

하지만 적천강의 일생을 통틀어 가장 깊고 큰 흔적을 남긴 사건은 따로 있었다.

정마대전(正魔大戰).

시체가 산을 이루고 피가 강이 되어 흐르던 시대.

적천강은 그 전란의 소용돌이에서 지금껏 겪어 본 적 없는 광활한 사마외도(邪魔外道)의 세계를 엿보았다.

정파 무림의 태산북두인 소림사와 비견되는 천마 신교의 마도 무학은 깊고 넓었으며, 사이하면서도 기괴했다.

그러나 지금, 적천강은 깨달았다.

일평생 보고 겪은 모든 것을 합한다 해도 지금 눈앞에 벌어지는 광경에 비하면 조족지혈에 불과하다는 것을.

쿠구구구궁!

‘이게 도대체……!’

그리고 마침내 모습으로 드러낸 그 거대한 존재를 목격한 순간, 적천강은 온몸의 피가 얼어붙는 것 같았다.

‘저것이 대관절 무엇이란 말이냐!’

그는 백수(白壽)를 훌쩍 넘긴 전전대의 고수.

살아온 세월과 위치가 있는 만큼 평범한 무림인이라면 일평생 한 번도 보지 못했을 영물, 혹은 악물이라 불리는 것들을 적지 않게 봐 왔다.

하지만 저 존재는…… 다르다. 화왕 적천강이 지닌 모든 경험과 지식을 뛰어넘었다.

지금 괴물에 의해 무너지고 있는 것은 절벽뿐만이 아니다.

그가 굳게 믿고 있던 이 세상의 법도와 규칙이 기암괴석과 함께 무너지고 있었다. 송두리째 파괴되고 흩어졌다.

그리고 그것은 적천강 한 사람만이 느끼는 충격이 아니었다.

“허.”

“아, 아아!”

살성(殺星)이라 불리는 고금제일의 살수는 탄식을 금치 못했고, 지식과 천재성 하나만큼은 과거의 제갈무후와 비견된다는 와룡객 제갈풍은 할 말을 잃었다.

그러나 그들이 느낀 충격은 그것으로 끝이 아니었다.

- 크롸아아아아!

거대한 괴물이 토해 낸 포효가 빗물을 밀어 내고 바람을 터트린다.

동시에 괴물을 중심으로 퍼져 나간 오싹한 기운이 백여 장 밖에 있던 세 사람의 전신을 덮쳤다.

쏴아아아아악!

“……!”

“……!”

“……!”

세 사람의 신형이 약속이라도 한 듯이 덜컥 굳었다. 자신들도 모르게 부릅뜬 세 쌍의 눈동자에는 숨길 수 없는 경악이 떠올라 있었다.

‘이럴 수가!’

물먹은 솜처럼 무거워진 육신과 저절로 힘이 들어가는 손아귀.

아직까지 절정에 머무르고 있는 제갈풍은 엄청난 오한과 함께 옅은 신음을 흘렸고, 그에 비해 까마득한 경지에 올라있는 적천강과 문경마저 순간 헛숨을 삼켰다.

‘이, 이런!’

‘말도 안 되는 일이.’

화왕과 살성이라 불리는 두 희대의 무인은 곧장 자신들에게 찾아온 이질감의 정체를 깨달았다.

그것은 그들이 아주 오랫동안 잊고 있었던 감정. 감히 누구도 범접할 수 없는 강자가 된 이후 느낄 수 없었던 케케묵은 감정이었다.

두려움.

이는 그만큼 변이된 수신룡이 발산한 피어(Fear)가 강력한 탓도 있었지만, 그보다는 적천강과 문경의 무지에서 기인한 것이 가장 컸다.

그들의 무공은 분명 현대의 S급 헌터들보다 몇 수 위에 있었으나, 난생처음 마주한 거대한 괴물의 등장은 오랜 세월 자신만의 영역과 상식을 구축한 두 사람의 굳건한 정신을 뒤흔들기에 충분했다.

- 콰우우우우!

괴물은 그 틈을 놓치지 않고 마음껏 날뛰었다.

흑색 비늘로 뒤덮인 몸통이 절벽을 후려칠 때마다 거대한 기암괴석이 하늘을 가득 메우며 떨어져 내렸다.

콰과과과광!

지형에 가려져 보이지 않는 저 어딘가를 향해 쉴 새 없이 쏘아지는 기암괴석의 소나기.

그 광경을 바라보는 적천강의 눈동자에서 화염이 줄기줄기 쏟아졌다.

‘노옴!’

저 알 수 없는 괴물이 무엇을 향해 저리 공격을 퍼붓는지, 적천강은 이미 알고 있었다.

열화문의 유일한 계승자이자 자신의 제자. 아니, 임시 제자인 진태경이 분명했다.

그 사실을 되새기자 피어의 영향으로 순간 굳어 있던 전신에서 용암과도 같은 기운이 터져 나왔다.

콰아아아!

십이경맥과 기경팔맥을 타고 솟구친 수 갑자의 열양지기가 미지의 존재로부터 내뿜어진 기운을 밀어 낸다.

비록 찰나에 불과하지만 잠시 굳어있던 몸에 초고온의 열기가 깃들고, 이내 뇌성벽력과도 같은 기합성을 토해 냈다.

“갈(喝)-!”

파앙!

기합에 실린 공력이 얼마나 강대했는지, 세 사람의 주위를 가득 메우고 있던 빗방울과 공기가 터져나갔다.

비록 아직까지 피어의 영향에서 완전히 벗어난 것은 아니지만, 난생처음 피어에 노출되었음에도 누구의 도움도 없이 스스로 빠져나온 것이다.

만약 현대의 헌터들이 봤다면 두 눈을 의심했을 만한 광경.

그러나 이처럼 놀라운 일을 해낸 것은 비단 적천강 한 사람뿐만이 아니었다.

적천강이 분노로서 피어의 일부를 해소했다면, 문경은 냉철한 이성과 반 계단 위의 깨달음으로 피어의 압제를 이겨 냈다.

‘동서고금을 통틀어 듣도 보도 못한 악물(惡物). 반드시 이 자리에서 쓰러트려야 한다.’

늘 따뜻하게 병자들을 보살피던 소년 의생은 이 자리에 없다.

천하인이 두려워하는 고금제일의 살수가 가라앉은 눈빛과 함께 걸음을 내딛자, 그의 호리호리한 신형이 허깨비처럼 흩어졌다.

툭, 쉬이이이익!

살성의 독문 무공. 극에 다다른 유령환살보(幽靈幻殺步)가 물살을 누르고 빗방울을 밟으며 쏘아졌다.

희끄무레한 잔상만을 남긴 채 빛살처럼 나아가는 신형. 그 아래로는 주위의 모든 수분을 증발시키며 내달리는 한 줄기 불꽃이 있었다.

콰아아아아!

적천강의 입술 사이로 분노 가득한 노호성이 터져 나왔다.

“이런 천인공노할 뱀장어 새끼를 보았나! 당장 그 녀석에게서 떨어지지 못할까!”



* * *



우르르릉, 꽝!

쉴새 없이 내리치는 뇌성벽력을 뚫고 들려오는 카랑카랑한 외침. 그리고 거대한 수신룡을 향해 섬전 과도 같은 속도로 달려드는 두 사람의 신형.

이제야 비로소 납득이 간다. 왜 이 퀘스트의 난이도가 초절정인지.

‘혼자라면 힘들지 몰라도, 이렇게 되면 이야기가 다르지.’

무공의 응용이나 습득력에서는 시스템을 사용하는 나조차 따라갈 수 없는 천재이자 당당한 초절정 고수인 청풍이 있고, 아무런 미사여구가 필요 없는 두 존재가 있다.

화왕과 살성. 살성과 화왕.

평균 수명이 비약적으로 상승한 현대를 기준으로 잡아도 실버타운에서 게이트볼을 쳐야 할 나이지만, 저 두 사람은 손가락 하나로 절정 고수 머리통을 쳐서 날릴 수 있는 괴수들이다.

‘움직임이 뭔가 전에 비해 무거워 보이기는 하는데…….’

혹시 저 두 사람도 약간이지만 피어의 영향을 받았나?

어찌 되었건 이로써 초대형 괴물에 맞설 인간형 괴수 둘이 추가되었다.

처음의 격돌로 약간의 손해를 보긴 했지만, 동정어옹을 상대하며 입은 약간의 내상과 어깨에 입은 자상을 제외하면 멀쩡한 셈이다.

‘미친 근골과 화룡갑이 없었다면 사지가 부러졌을지도.’

거대한 덩치에 안 맞게 쾌속한 움직임과 수염을 이용한 공격.

확실히 [몬스터 대백과]에서 읽었던 시 서펜트와는 비슷하면서도 다른 구석이 있다고 생각하던 그때였다.

- 크르르르……!

찰나의 순간, 드디어 상황이 이상하게 돌아가는 것을 눈치챈 수신룡의 눈동자가 번뜩였다.

그리고 나는 그 짧은 틈을 놓치지 않았다.

“청풍!”

“네, 은인!”

간혹 짧은 말 한마디, 서로의 눈빛을 교환하는 것만으로도 뜻이 통하는 경우가 있다.

외침과 동시에 수신룡을 향해 쇄도한 나와 청풍이 바로 그랬다.

쐐애애애액!

쉬쉬쉬쉬슁!

꼬리에 맞아 튕겨 나갔을 때보다 두 배는 빠른 속도.

각각 창날과 검신을 타고 솟구친 푸르고 붉은 강기가 자신을 향하자, 수신룡의 수염이 거세게 요동쳤다.

쉬리리리릭!

저 수염이 제일 거지 같았다. 하나하나에 실린 기운이 초절정 고수의 강기만큼은 아니더라도, 일반적인 검기를 뛰어넘는 파괴력과 예리함을 지니고 있기에 결코 무시할 수 없기 때문이다.

거기에 더해 한 가닥의 길이만 해도 얼추 삼 장. 마치 동정어옹이 흑목조간을 이용해 무공을 펼치는 것처럼 투로도 기괴막측하다.

첫 공격을 허용한 것도 놈이 수백 가닥의 수염을 저런 식으로 활용할 줄 몰랐기 때문이었다.

하지만…….

‘다시 한번 들어와 봐, 개자식아.’

수신룡의 기운을 머금은 채 사방에서 쏟아져 내리는 빛줄기. 나는 전방을 향해 비스듬히 창날을 내리그었다.

후우우웅! 서걱!

청백색의 불꽃이 그리는 궤적에 걸려든 빛줄기가 힘을 잃고 잘려 나간다.

그러나 수신룡 역시 호락호락한 놈은 아니었다. 조금 전의 일격으로 베어 버린 것만큼이나 많은 빛줄기가 어느새 내 후방을 노리고 있었다.

쐐액!

처음부터 느꼈지만, 확실히 영리한 놈이다. 본능적으로 화룡갑의 강도를 눈치챈 것인지 갑옷에 가려지지 않는 맨살을 향해 파고든다.

빠르게 날아드는 살기를 느낀 등허리가 서늘했다. 하지만 그보다 반 박자 앞서 날아드는 강력한 기운이 있었다.

쉭, 서걱!

휘황찬란한 자줏빛 강기가 어둠을 몰아내고 빛을 밝힌다. 화산파의 적전제자에게만 전수된다는 비전 절기, 자하신공(紫霞神功).

‘청풍.’

나는 등을 향해 쏘아지던 살기가 사라졌음을 느꼈다.

고개를 돌려 확인하지 않아도 알 수 있었다. 청풍은 제 역할을 확실히 해냈고, 이제는 내가 전력을 발휘해야 할 차례다.

아니, 정정한다. 내가 아니라 ‘우리’다.

- 크르르르륵!

변이된 수신룡이 황급히 고개를 쳐들었지만 이미 엎질러진 물이었다.

나와 청풍을 신속하게 저지하지 못한 것. 그것이 바로 놈의 가장 큰 패착이었고, 이미 거대한 동체 뒤에는 인간형 괴수 둘이 들이닥치고 있었다.

쉭!

조용하고 은밀하게. 동시에 어떤 것보다 쾌속한 움직임으로 허공으로부터 내리꽂히는 한 줄기의 벼락.

그리고 다음 순간 울려 퍼지는 절삭음.

서걱!

은빛 강기와 맞닿은 수신룡의 검은 뿔 중 하나가 절반으로 잘려 나감과 동시에, 놈의 아가리에서 고통인지 분노인지 모를 괴성이 터져 나왔다.

- 그아아아아!

“흡!”

수신룡의 비늘 사이로 어디서 나왔는지 모를 소검(小劍)을 밀어 넣으려던 문경의 신형이 흔들린다.

‘내 예상이 맞았어.’

몬스터의 피어에 익숙한 나나, 원체 미친놈인 청풍과 달리 다른 이들은 차이는 있을지언정 아직 피어의 영향에서 완전히 벗어나지 못했다.

하지만 그렇다고 해서, 이미 쏘아진 적천강의 일권이 멈추는 것은 아니다.

“이 개호로 썅노무-!”

마법 주문과 같은 욕설을 토해 낸 적천강의 일권(一拳)이 수신룡의 허리 부분에 격중한 순간.

화륵, 꽈아앙!

- 크라라라라라!

엄청난 양의 화염과 수증기가 터져 나옴과 동시에, 수신룡의 거대한 동체가 지상을 향해 기울었다.

그리고 놈의 아가리가 쓰러지는 방향의 끝에, 전력을 다해 쇄도하는 내가 있었다.

쉬이이익!

- 크륵!

세로로 쭉 찢어진 거대한 핏빛 동공에, 푸른 화염을 머금은 백염을 내지르는 내 모습이 비쳤다.

“내가 눈 그따위로 뜨지 말랬지. 이 시벌놈아.”

푸욱!
```

## Final English reading copy

```markdown
# Chapter 471

Fire King Jeok Cheongang had lived for well over a hundred years.

The boy who had wandered from place to place, begging for food, met a master one day and became the eighteenth successor of the Fire Gate Clan. When time passed and his master returned to the earth, he became both the clan’s sole Disciple and its Sect Leader.

It had taken a truly long time for the boy to become a young man, the young man to become middle-aged, and finally the middle-aged man to become old.

During that time, a great war erupted—one that would determine the fate of the world—and a new nation was founded under a new imperial surname.

Five floods and earthquakes struck. Plagues spread, and bands of bandits wearing red turbans rose everywhere, pillaging as they pleased.

In every event Jeok Cheongang had witnessed, there had been disasters brought about by humans and divine punishments sent down by the heavens.

But one event had left the deepest and greatest mark on his life.

The Great Faction War.

An age when corpses formed mountains and blood flowed like rivers.

Amid that war’s vortex, Jeok Cheongang glimpsed a vast world of demonic, heterodox arts unlike anything he had ever experienced.

The martial arts of the Heavenly Demon Divine Cult, which could be compared to those of Shaolin Temple, the Mount Tai and Northern Dipper of the Murim’s orthodox faction, were deep and broad—devious, yet bizarre.

But now, Jeok Cheongang understood.

Even if he combined everything he had seen and experienced throughout his life, it would amount to nothing more than a drop in the bucket compared to the scene unfolding before his eyes.

*Rumble-rumble-rumble!*

*What in the world…?*

And when he finally saw the enormous being reveal itself, Jeok Cheongang felt as though every drop of blood in his body had frozen.

*What on earth is that thing?*

He was a master from two generations past, well beyond his ninety-ninth year.

Given the years he had lived and the position he held, he had seen no small number of beings that ordinary martial artists might never encounter even once in their entire lives—beings known as spirit beasts or evil beasts.

But that being…

It was different. It surpassed every bit of Fire King Jeok Cheongang’s experience and knowledge.

The thing being destroyed by the monster was not merely the cliff.

The laws and rules of the world he had firmly believed in were collapsing along with the bizarre boulders. They were being destroyed and scattered completely.

And Jeok Cheongang was not the only one feeling that shock.

“Ha.”

“Ah, ahhh!”

The greatest assassin of all time, known as the Slaughter Saint, could not suppress his groan of disbelief. Crouching Dragon Guest Zhuge Feng, whose knowledge and genius alone were said to rival those of Zhuge Wuhou of the past, was left speechless.

But the shock they felt did not end there.

—Kraaaaaaaaaah!

The enormous monster’s roar drove back the rain and burst the wind apart.

At the same time, a chilling aura spreading outward from the monster engulfed the entire bodies of the three people standing more than a hundred *jang* away.

*Whooooooosh!*

“……”

“……”

“……”

The three figures stiffened at once, as if they had made an agreement to do so. In their three pairs of eyes, widened without their consent, unmistakable shock appeared.

*This can’t be!*

Their bodies had grown heavy as wet cotton, and their clenched hands were tightening on their own.

Zhuge Feng, who still remained at the Peak realm, let out a faint groan amid an overpowering chill. Jeok Cheongang and Mungyeong, whose realms were unimaginably higher, swallowed a startled breath in spite of themselves.

*Th-This is…!*

*Impossible.*

The two extraordinary martial artists known as the Fire King and the Slaughter Saint immediately realized the identity of the unfamiliar sensation that had come over them.

It was an emotion they had forgotten long ago. A stale, ancient emotion they had been unable to feel since becoming beings so powerful that no one dared approach them.

Fear.

The sheer strength of the Fear radiating from the Mutated Water God Dragon was certainly partly responsible. But the greater cause was the ignorance of Jeok Cheongang and Mungyeong.

Their martial arts were unquestionably several levels above those of modern S-rank Hunters. Even so, the appearance of a gigantic monster they had never encountered before was more than enough to shake the firm minds of two people who had spent decades building their own domains and common sense.

—Kraaaaaaow!

The monster did not miss the opening and began rampaging with all its might.

Each time its body, covered in black scales, lashed against the cliff, enormous bizarre boulders filled the sky before crashing down.

*Kwagwagwagwang!*

A rain of bizarre boulders shot without pause toward somewhere hidden from view by the terrain.

Flames poured from Jeok Cheongang’s eyes as he watched the sight.

*You bastard!*

Jeok Cheongang already knew what the unknown monster was attacking so relentlessly.

His sole successor to the Fire Gate Clan and his Disciple. No—his temporary Disciple, Jin Taekyung.

As he recalled that fact, lava-like energy burst from his entire body, which had been momentarily frozen by Fear.

*Whoom!*

Several jiazi’s worth of Scorching Yang Qi surged along his Twelve Regular Meridians and Eight Extraordinary Meridians, pushing away the power radiating from the unknown being.

Though only for an instant, superheated energy filled his body, which had been briefly immobilized. Then he released a battle cry like a thunderclap.

“Ha!”

*Bang!*

The internal energy contained in that shout was so powerful that the raindrops and air filling the area around the three men burst apart.

Jeok Cheongang had not yet completely escaped Fear’s influence. But even though he had been exposed to Fear for the first time in his life, he had broken free of it on his own, without anyone’s help.

If modern Hunters had witnessed the scene, they would have doubted their own eyes.

But Jeok Cheongang was not the only one to accomplish something so astonishing.

If Jeok Cheongang dispelled part of Fear through his rage, Mungyeong overcame its oppression through cool reason and enlightenment half a step above Jeok Cheongang’s.

*An evil beast unheard of throughout history. It must be brought down here and now.*

The young medical apprentice who had always cared warmly for the sick was no longer present.

As the greatest assassin of all time—the one feared by everyone in the world—took a step forward with calm eyes, his slender figure scattered like an illusion.

*Tap. Whoooooosh!*

The Slaughter Saint’s signature martial art, the Ghost Illusory Slaughter Step, shot forward after pressing down on the current and stepping across the raindrops.

His figure advanced like a streak of light, leaving behind only a pale afterimage. Beneath him, a single trail of flame raced forward, evaporating every trace of moisture around it.

*Whoom!*

A furious roar erupted from between Jeok Cheongang’s lips.

“You unholy eel bastard! Get away from that boy this instant!”

* * *

*Rumble, crash!*

A clear, ringing shout pierced through the ceaseless thunder. At the same time, two figures charged toward the gigantic Water God Dragon at the speed of lightning.

Only now did I finally understand why the Quest’s Grade was Supreme Peak.

*It might have been difficult alone, but things are different now.*

There was Cheongpung—a proud Supreme Peak master and a genius whose application and acquisition of martial arts even I, despite using the System, couldn’t keep up with.

And then there were two existences who needed no embellishment whatsoever.

The Fire King and the Slaughter Saint. The Slaughter Saint and the Fire King.

Even by the standards of the modern world, where average life expectancy had risen dramatically, those two were old enough to be playing gateball in a retirement community.

Yet they were both monsters capable of knocking a Peak master’s head clean off with a single finger.

*Their movements do look a little heavier than before…*

Had those two also been affected by Fear, even if only slightly?

In any case, two more human-shaped monsters had joined the fight against the supermassive monster.

I had taken a little damage in the initial clash, but aside from the minor Internal Injury I had suffered while fighting the Dongting Fisherman and the cut on my shoulder, I was perfectly fine.

*If I hadn’t had those insane Muscles and Bones and the Fire Dragon Armor, I might have broken all four limbs.*

The monster moved far faster than its massive body suggested, and it used its whiskers to attack.

Just as I was thinking that it resembled the Sea Serpent I had read about in the *Monster Encyclopedia* while still being different in certain ways—

—Grrrrrrr…!

In that split second, the Water God Dragon’s eyes flashed as it finally realized the situation was taking an unusual turn.

And I did not miss that brief opening.

“Cheongpung!”

“Yes, Benefactor!”

Sometimes, a single short word or the exchange of a glance was enough for two people to understand each other.

Cheongpung and I were exactly like that as we rushed toward the Water God Dragon at the same time as my shout.

*Whoooooosh!*

*Shh-shh-shh-shing!*

We were moving twice as fast as when the dragon’s tail had sent us flying.

As blue and red Force surged along the spearhead and sword blade and rose toward it, the Water God Dragon’s whiskers thrashed violently.

*Shri-ri-ri-rik!*

Those whiskers were the absolute worst.

The energy contained in each one was not quite as powerful as the Force of a Supreme Peak master, but their destructive power and sharpness surpassed ordinary Sword Energy. They could not be ignored.

On top of that, each strand was roughly three *jang* long. Their trajectories were bizarre and impossible to predict, much like the Dongting Fisherman’s martial arts when he used his black-wood fishing rod.

The only reason I had allowed the first attack to land was that I hadn’t known the bastard could use hundreds of whiskers like that.

But…

*Come at me again, you son of a bitch.*

Streaks of light carrying the Water God Dragon’s power poured down from every direction. I slashed the spearhead diagonally downward in front of me.

*Whoooooom! Schk!*

The streaks of light caught in the path drawn by the blue-white flames lost their strength and were sliced apart.

But the Water God Dragon was no pushover, either. Just as many streaks of light as I had cut through a moment ago were already targeting my back.

*Whoosh!*

I had sensed it from the beginning, but the bastard was definitely intelligent. Perhaps it had instinctively recognized the strength of the Fire Dragon Armor and was targeting the bare flesh not protected by the armor.

My back grew cold as I felt the killing intent flying toward me.

But an instant ahead of it, a powerful force came rushing in.

*Shik. Schk!*

Brilliant violet Force drove away the darkness and illuminated the world.

The Zaha Divine Technique, a secret ultimate art taught only to the direct Disciples of Huashan.

*Cheongpung.*

I felt the killing intent shooting toward my back vanish.

I knew without turning around to check. Cheongpung had carried out his role perfectly.

Now it was my turn to use all my strength.

No. Correction.

It was our turn.

—Grrrrrrrrk!

The Mutated Water God Dragon hurriedly raised its head, but it was already too late.

Its failure to stop Cheongpung and me in time was its greatest mistake. Two human-shaped monsters were already closing in behind its enormous body.

*Shik!*

Quietly and stealthily. At the same time, with a swiftness greater than anything else, a streak of lightning plunged down from the air.

Then, a moment later, the sound of something being sliced apart rang out.

*Schk!*

One of the Water God Dragon’s black horns was cut in half when it met the silver Force. A cry that might have been pain or rage burst from the monster’s maw.

—Graaaargh!

“Gasp!”

Mungyeong’s figure shook as he tried to thrust a small sword between the Water God Dragon’s scales.

*My guess was right.*

Unlike me, who was accustomed to the Fear of monsters, and Cheongpung, who was simply insane to begin with, the others had not yet completely escaped Fear’s influence, though the degree varied from person to person.

But that did not mean the fist Jeok Cheongang had already launched stopped.

“You godforsaken son of a bitch—!”

Jeok Cheongang spewed the curse like a magic incantation, and his fist slammed into the Water God Dragon’s waist.

*Fwoosh! Boom!*

—Kra-ra-ra-ra-ra!

An enormous amount of flame and steam exploded outward, and the Water God Dragon’s gigantic body tilted toward the ground.

At the end of the direction in which its maw was falling, I was already charging forward with all my strength.

*Whoooooosh!*

—Krrk!

My figure, thrusting White Flame wreathed in blue fire, was reflected in the enormous blood-red pupil split vertically down the middle.

“I told you not to open those eyes like that, you sibu-leol bastard.”

*Shnk!*
```

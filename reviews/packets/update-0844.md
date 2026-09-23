<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0844.txt",
      "sha256": "b41a53a20eb4c1a98f1836946f44b17acc7523772717dd9b93553a3a8dc71557",
      "bytes": 12494
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "415b801a8ac6c21d17e30cea350b22a7061a1d12147ffaee752fc86cbd3ee994",
      "bytes": 2675
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "2ac235886e36b4a9cfac67990c4e303d5cbbbaacdc20104970ce04b7ba9ca08c",
      "bytes": 227427
    },
    {
      "path": "characters/Blood Lord.md",
      "sha256": "ad23d23bac80e99436ff944833536ac53485861f3e9b54100aaf2022183429c5",
      "bytes": 830
    },
    {
      "path": "characters/Blood Monk.md",
      "sha256": "cc108d888e4abb92d50afdc00dcc1c31d6087511b0e2db8e3a7363e677614da2",
      "bytes": 853
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "7e0e4a8302dc8e5e22f6e91a4793acb1c7c3e4f0c503f4d5fe08c81a31debd60",
      "bytes": 1325
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "cdeef8b540645b3980eb421f89cc6f0c7c7fd29bc8ee626202b33c9dac93dc07",
      "bytes": 723
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "497652f5f38dd738869ec96095b5e4f31af9d70f42de4b45e75662bad569b85a",
      "bytes": 1573
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "6118f49fe0d169e6a180ae640a69988783a99a800d1d5ec65f69d660914ecba2",
      "bytes": 1782
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "3976b2c3138c36c40ab828955d86ce71de4389db8db9769d175c8ad7a5bb0446",
      "bytes": 622
    },
    {
      "path": "characters/Mae Jonghak.md",
      "sha256": "6ac6a61f838e088fde8df3ec5580bf8bcb95443b3bc86ba96f10780cd19586f6",
      "bytes": 1061
    },
    {
      "path": "characters/Southern Heaven Demon Empress.md",
      "sha256": "9a5f907d1c537a52f0163f474bb477004e7d5b7fbde68a5441458ce2c871259f",
      "bytes": 715
    },
    {
      "path": "characters/Western Heaven Demon Lord.md",
      "sha256": "1c7786b4924e0a641909b7a3bef726ce39c249ea375324cb5852e53d18ea5de4",
      "bytes": 888
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "fd4790bf594f3f982af466f12b95b581c707ae942c0105f2f4d7be2cafb615a6",
      "bytes": 252065
    }
  ],
  "estimated_tokens": 12965
}
-->

# Durable State Update — Chapter 844

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

For each matched character, check whether this chapter adds clear, durable
evidence that improves Role, Personality, Voice, or Relationships. Update a
field when it corrects or meaningfully sharpens the existing profile; otherwise
leave it unchanged. Voice guidance should capture observable register, cadence,
word choice, or address habits that help distinguish the character in English.
Do not infer a stable voice from one situational line or generic personality
adjectives. Keep “Not established” only when this chapter provides no reliable
voice evidence; never replace it with unsupported specificity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 844. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 844. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history. For a new profile, describe voice only when the chapter supports
a useful, stable distinction; otherwise say “Not established”.
`names` contains only newly required Korean-to-English rows that are absent from
Exact glossary matches; Korean keys must occur in the source. Do not repeat
glossary matches. The controller drops rows already in the names ledger.
`address_pairs` contains only newly required speaker→addressee rows that
are absent from Matched address pairs. Speaker and addressee must be Hangul source
spellings such as 진태경 or 혁무진, never English names. Arabic digits are
allowed in titles such as 1팀장. At least one endpoint must occur in the source.
Before returning JSON, verify every `speaker` and `addressee` value contains at
least one Hangul character; use the Korean source spelling even when the same
person's English name appears in the reading copy. If no valid new pair exists,
return `"address_pairs": []`.
The controller drops pairs already in the address ledger. Do not invent
risk-register rows. Beat plot paragraphs are plain strings; continuity and
translation decisions are concise list items.
Return this exact shape:

{
  "chapter": 844,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 844,
    "continuity_sources": [844],
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
    "Jin Taekyung is the World Hunter Federation’s Alliance Leader.",
    "The supernatural Rift began at 10%; its progress increases the distribution and concentration of magical power.",
    "The System’s Status Window is inaccessible; Jin suspects an update may be responsible.",
    "Jin’s vision of a black-haired man killing Ahomed after the ritual remains unexplained; Jin believes the man was not Asmodeus.",
    "Jin’s [Broken Body] injury around his lower dantian remains unresolved; leveling up did not heal it.",
    "Jin is at the Sichuan Tang Clan after returning from another world; he and Jeok Cheongang have been talking for two days.",
    "The Divine Physician is preparing a pill for Jin’s recovery.",
    "The Sichuan Tang Clan and Sichuan Murim are rebuilding after Dark Heaven’s attack; allied martial artists remain to treat patients and guard against another attack.",
    "Jeok Cheongang and Jin Taekyung trust each other deeply; their Master-Disciple bond remains unformalized.",
    "Jin concludes that Dark Heaven links the modern world and Murim; magical power and Dark Heaven’s anomalous abilities have appeared in Murim.",
    "Jin believes Dark Heaven first appeared in Murim during or shortly after the Great Faction War."
  ],
  "continuity_sources": [
    843
  ],
  "open_questions": [
    "Why did the Main Quest fail despite the Doppelganger’s erasure, and who or what was summoned?",
    "Was Jin’s vision of the summoned being real, System-delivered, or prophetic?",
    "What will happen as the Rift progresses and more beings enter the world?",
    "Who or what chose Jin, what is the Ark, and how did Dark Heaven reach Murim?",
    "What is the Lord of Heaven’s true identity, and how does the Doppelganger’s prophecy about a great king relate to it?"
  ],
  "safe_through": 843,
  "temporary_decisions": [
    "Keep magical power distinct from mana; keep Blink distinct from Teleport and Warp. Extended-range Blink causes severe strain.",
    "Keep Fire Storm and Aqua Storm as distinct named spells.",
    "Render [영웅의 검] as “Hero’s Sword,” 에어 슬래시 as “Air Slash,” and 실드 마법 as “Shield magic.”",
    "Render 선택받은 자 as “the Chosen One,” 방주의 주인 as “the Master of the Ark,” [격변] as [Cataclysm], [어데 도씹니꺼] as “Where’s Your Do Clan From?,” and [종족 학살자] as “Species Slayer.”",
    "Render 균열 as a social fracture or division, not the supernatural Rift; render 醜王 as “Disgrace King” when used as Jin’s mocking imagined epithet for Jeok Cheongang."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 매종학    | **Mae Jonghak**    |
| 청풍     | **Cheongpung**     |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 검성     | **Sword Saint**               | Mae Jonghak    |
| 태원진가   | **Jin Family of Taiyuan**        |
| 암천     | **Dark Heaven**                  |
| 삼류     | **Third Rate**    |
| 절정     | **Peak**          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 정파     | **orthodox faction**                             |                                                       |
| 사파     | **unorthodox faction**                           |                                                       |
| 중원     | **Central Plains**                               |                                                       |
| 기루     | **pleasure house**                               |                                                       |
| 장로     | **Elder**                                    |
| 대장로    | **Head Elder**                               |
| 제자     | **Disciple**                                 |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 하남     | **Henan**              |
| 혈주 | **Blood Lord** | Title of the unidentified young man encountered by Han Su. |
| 혈승 | **Blood Monk** | Sobriquet of the unidentified bald martial artist active in Guizhou. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 남천마후 | **Southern Heaven Demon Empress** | Title Honglan uses when revealing her identity. |
| 서천마군 | **Western Heaven Demon Lord** | Title of the middle-aged antagonist who commands the summoned black-robed hunters. |
| 섬서 | **Shaanxi** | Province bordering Shanxi. |
| 사마외도 | **demonic, heterodox arts** | Suspected martial-arts origin of Pung Yang's insidious forms. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 고원 | **Gaoyuan** | Plateau region in northern Shanxi. |
| 무재 | **martial talent** | Innate aptitude for learning martial arts. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 천룡 | **Heavenly Dragon** | The ideal form Jeok Cheongang wishes Taekyung to become. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 천주 | **Lord of Heaven** | Authority invoked by the masked attackers. |
| 광동 | **Guangdong** | Province under Demonic Cult control during the war. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 괴력난신 | **supernatural powers** | Term for extraordinary and unnatural powers. |
| 이무기 | **imugi** | Legendary serpent mentioned as the only comparable creature to a Thousand-Year Poison Horned Snake. |
| 광서 | **Guangxi** | Region bordering Nanman. |
| 서천 | **Western Heaven** | Short form used by the Lord of Heaven for the Western Heaven Demon Lord. |
| 남천 | **South Heaven** | Dark Heaven power that the Lord of Heaven orders the servants to contact. |
| 전서 | **missive** | A written message exchanged or delivered in secret. |
| 마후 | **Demon Empress** | Title used for the Southern Heaven Demon Empress. |
| 심해 | **deep sea** | Unexplored ocean depths where the ancient monster awakens. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 청풍 | 진태경 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung repeatedly addresses Taekyung as 은인 after receiving food. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 진태경 | 청풍 | companion_to_young_martial_artist | Young Master Cheongpung | formal-polite | Taekyung uses 청 공자 while correcting Cheongpung's royal-etiquette mistake. |
| 매종학 | 청풍 | grandfather_to_grandson | Pung | affectionate-instructional | Mae Jonghak calls young Cheongpung 풍아 while teaching him the Crouching Tiger Fist. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 적천강 | 청풍 | overwhelming_elder_to_young_martial_artist | you / little punk | blunt, amused, and threatening | Jeok Cheongang uses 네, 이놈, and related blunt forms while testing Cheongpung. |
| 청풍 | 적천강 | young_martial_artist_to_overwhelming_elder | Grandpa Jeok | casual-familiar despite deference | Cheongpung uses 적 할아버지 while asking Jeok Cheongang to confirm Taekyung's condition; this is a familial form of address, not literal kinship. |
| 혈주 | 적천강 | claimed enemy to enemy | your enemy | calm and threatening | The Blood Lord identifies himself as Jeok's enemy and claims to have killed Jeok's most precious friend. |
| 혈주 | 진태경 | hostile_opponent_to_hostile_opponent | Sleeping Dragon of Shanxi | casual, amused, and taunting | Addresses Taekyung by his established epithet while asking whether he agrees with the Blood Lord's judgment of Han Su. |
| 혈주 | 청풍 | hostile_opponent_to_newly_revealed_identity | Huashan's Invincible Divine Sword; Sword Saint's Disciple or grandson | mocking and taunting | Recognizes Cheongpung's public identity and needles him with his Sword Saint lineage while dismissing the added threat. |
| 매종학 | 혈주 | legendary_martial_master_to_enemy | you | cold and judgmental | After revealing himself, Mae Jonghak condemns the Blood Lord's accumulated sins and orders him to pay the price. |
| 혈주 | 매종학 | enemy_to_revealed_legendary_master | you | shocked and hostile | The Blood Lord addresses Mae Jonghak with 당신 immediately after recognizing him as the Sword Saint. |
| 매종학 | 진태경 | older_ally_to_younger_friend | friend | casual-familiar | Mae Jonghak uses 친구 when arriving at Taekyung's window and asking to talk. |
| 서천마군 | 청풍 | commander_to_young_opponent | you | gentle and taunting | Uses 자네 while identifying Cheongpung and discussing the Blood Lord. |
| 서천마군 | 진태경 | hostile_opponents | you | calm and taunting | Uses 자네 while questioning Taekyung and offering to take him alive. |
| 진태경 | 서천마군 | hostile_opponents | Western Heaven Demon Lord | casual and defiant | Identifies the Demon Lord by title and answers his surrender demand with sarcasm. |
| 서천마군 | 신의 | hostile_invader_to_physician | Divine Physician | calm and mocking | Uses 신의 and 그대 while taunting the physician and dismissing his objections. |
| 신의 | 서천마군 | physician_to_invading_fiend | fiend | defiant and formal | Calls the Western Heaven Demon Lord an 악귀 and orders him to leave. |
| 서천마군 | 적천강 | hostile_invader_to_unconscious_patient | you | calm and predatory | Says someone wants to see Jeok Cheongang and attempts to move him with Seizing an Object Through Empty Space. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 서천마군 | hostile_opponents | you bastard | blunt and threatening | Jeok addresses the Western Heaven Demon Lord with 네놈 while defending Taekyung and ordering him not to touch his Disciple. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 남천마후 | 진태경 | hostile_supernatural_opponent_to_young_martial_artist | Young Great Hero / Child | lighthearted and taunting | Addresses Taekyung while refusing to explain the Gate. |
| 진태경 | 남천마후 | young_martial_artist_to_hostile_demon_empress | you | hostile and determined | Promises that the Southern Heaven Demon Empress will die when they meet again. |
| 적천강 | 남천마후 | legendary_martial_master_to_hostile_demon_empress | you bitch | blunt and threatening | Threatens to punish her and Lord of Heaven. |
| 남천마후 | 적천강 | hostile_demon_empress_to_legendary_martial_master | Fire King Jeok / you | flattering and mocking | Addresses Jeok Cheongang as the Fire King while praising Lord of Heaven. |
| 매종학 | 적천강 | long-standing martial rival and friend | Great Hero Jeok | casual and familiar | Mae addresses Jeok as 적 대협 while discussing the Alliance Leader position. |
| 적천강 | 매종학 | long-standing martial rival and friend | you | blunt and familiar | Jeok addresses Mae as 당신 while recalling their meeting at Mount Jiuhua. |
| 청풍 | 매종학 | grandson to grandfather | Grandpa | casual-familiar | Repeatedly calls Mae Jonghak 할아버지 while mistaking the Alliance Leader's summons as a family visit. |
| 진태경 | 매종학 | younger ally to newly installed Alliance Leader | Alliance Leader | formal and deferential | Uses 맹주님 while formally greeting Mae Jonghak as the Alliance Leader. |
| 혈주 | 천주 | servant_to_absolute_master | Lord of Heaven | worshipful and deferential | Blood Lord repeatedly addresses the Lord of Heaven while apologizing and receiving power. |
| 천주 | 혈주 | absolute_master_to_servant | Blood Lord | commanding and reproachful | The Lord of Heaven directly rebukes Blood Lord and then empowers him. |
| 남천마후 | 천주 | devoted_servant_to_revered_master | Lord of Heaven | reverent and prayerful | The Southern Heaven Demon Empress prays that the Lord of Heaven will remember her loyalty and love. |

## Listed compact profiles

### Blood Lord.md

# Blood Lord (혈주)

- **Safe through:** Chapter 725
- **Aliases:** None
- **Role:** Young-seeming high-ranking Dark Heaven figure who seeks Jin Taekyung, Cheongpung, and Jeok Cheongang after escaping the confrontation at Mount Song.
- **Personality:** Calm, confident, theatrically frivolous, casually cruel, and ruthlessly destructive; treats allies as disposable tools and enjoys provoking stronger opponents.
- **Voice:** Light, cheerful, and joking even while threatening or killing; turns cold and contemptuous when challenged.
- **Relationships:** He serves the Lord of Heaven alongside the Western Heaven Demon Lord, has received the Lord of Heaven's power for the coming Great War, and still seeks to kill Cheongpung, Jeok Cheongang, and Jin Taekyung.

### Blood Monk.md

# Blood Monk (혈승)

- **Safe through:** Chapter 835
- **Aliases:** Jeok Cheongang; Fire King
- **Role:** The Blood Monk is Jeok Cheongang, the Fire King, who disguised himself as a monk to evade Dark Heaven and uses a steel Zen staff and the Flame Divine Palm.
- **Personality:** As Jeok Cheongang, the Blood Monk is gruff, blunt, protective of his Disciple, and prone to profane mockery, but acts decisively to protect others.
- **Voice:** He speaks roughly and informally, often curses or teases with insults, and calls himself 'this old man' while addressing Jin as a brat.
- **Relationships:** Jeok Cheongang is Jin Taekyung's master and protective ally; he opposes Dark Heaven and is recognized by the Nanman as the Fire King.

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 835
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, the grandson and Disciple of Sword Saint Mae Jonghak, a Supreme Peak martial master known as the Huashan Divine Dragon, the creator of the snake-inspired Mimi Step footwork technique, and the master of the Azure Dragon Pavilion within the Alliance Leader's Two Dragons Pavilion.
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, a deep love of martial arts, competitive pride, unusual resistance to monster-induced Fear, and discomfort when someone copies his martial arts.
- **Voice:** Dreamy and hazy, with innocent, polite phrasing; he has begun imitating Taekyung's profanity.
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions while Taekyung is his only true martial rival; Tang Sadok has temporarily entrusted Mimi, now a large horned snake, to him, and Cheongpung is accompanying Mungyeong while learning his martial arts through observation to become stronger and adapt to this world.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 843
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 843
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm, the occupant of the chief seat of the Murim Alliance's Five Kings Hall, and a trusted confidant who accepts Jin as himself despite knowing that he travels between Murim and another world resembling the realm of immortals.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; they trust each other deeply but have never formalized their bond. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to the late Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and is a long-standing rival of Peng Cheolhu.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 843
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader.
- **Personality:** Hungry, self-aware, dryly observant, and pragmatic under pressure; accepts extreme personal risk when duty and the lives of others demand it.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; they trust each other deeply, though their bond remains unformalized. Cheongpung is his trusted companion and only true martial rival; Choi Minwoo is his subordinate and trusted manager of media and official arrangements as well as the Peace Guild's Guild Master; Ju Hwaran is a trusted Fire Dragon Pavilion member; Magic Johnson and Chuck Hagel are allied to him; his mother and sister Hayeon are among those he protects; the Skeleton King is his friend and ally; Xiao Shen regards him as an older brother; Jin-ho is his older friend and trusted confidant; he once saved Ju Wongong’s life.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 843
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Mae Jonghak.md

# Mae Jonghak (매종학)

- **Safe through:** Chapter 835
- **Aliases:** Sword Saint
- **Role:** Sword Saint and Cheongpung's grandfather who now serves as the New Murim Alliance's Alliance Leader and has ordered Jin Taekyung's first Fire Dragon Pavilion mission to Nanman.
- **Personality:** Playful, easygoing, and teasing, but capable of handling heavy administrative responsibilities efficiently.
- **Voice:** Friendly, casually familiar, and cheerfully teasing, including when greeting old acquaintances and discussing leadership.
- **Relationships:** Cheongpung's grandfather and martial instructor; taught him the Taeeul Miri Palm; secretly entered Huashan while its Sect Leader slept, left a dagger and handwritten note, and then went into hiding, prompting Huashan's search; fought Jeok Cheongang at Mount Jiuhua more than forty years ago and left after their draw; his old friend Hong Dao left him a letter identifying Jin Taekyung as the Morning Star who would drive away darkness.

### Southern Heaven Demon Empress.md

# Southern Heaven Demon Empress (남천마후)

- **Safe through:** Chapter 840
- **Aliases:** None
- **Role:** The Southern Heaven Demon Empress was Honglan, the creator of the rift behind the Inner Palace, and was killed after the rift closed.
- **Personality:** Playful, cruel, confident, and casually dismissive of mass death and the suffering of others.
- **Voice:** Light, taunting, amused, and delighted even when discussing murder or imminent catastrophe.
- **Relationships:** She commands and advises Baeksang, treats Jin Taekyung and Yayul Cheok as expendable to the grand plan, and keeps a masked hunting dog whom she trained carefully.

### Western Heaven Demon Lord.md

# Western Heaven Demon Lord (서천마군)

- **Safe through:** Chapter 841
- **Aliases:** None
- **Role:** Former Protector of the Divine Cult who commands Dark Heaven's assault on the Sichuan Tang Clan, lost the Myriad-Poison Ring to Jin Taekyung, suffered a crushed ankle and a torn wrist, and was temporarily possessed by the Lord of Heaven before the borrowed body was destroyed.
- **Personality:** Cold, detached, patient, and utterly ruthless toward those he interrogates or hunts.
- **Voice:** Controlled and dispassionate, with concise statements delivered in a quiet, threatening tone.
- **Relationships:** Tang Taesang and the Heaven-Shaking Venerable Nun were his latest victims, he lost one arm taking their lives, and the Qilian Three Fiends now submit to him alongside his hundreds of black-robed hunters.

## Korean source

```text
＃844화



“이게 끝이야?”

입을 연 사내는 기껏해야 삼십 언저리로 보였다. 저잣거리를 걷다 보면 하루에도 몇 번은 볼 수 있는 평범한 외모.

그러나 그 누구도 감히 사내를 보며 평범하다고 생각하지 못했다.

지금 그는 저잣거리가 아닌, 검붉은 피 웅덩이에 서 있었으니까.

“확실히 나아지긴 했지만, 예상했던 것보다는 한참 부족한데…….”

으직.

피 웅덩이에 반쯤 잠겨 있는 팔을 짓밟은 사내가 말을 이었다.

“고작 이런 거나 보여 주려고 날 불렀나?”

이 팔의 주인? 모른다. 사내로서는 알 필요도 없었다.

어차피 수많은 실험체 중 하나였고, 오늘 이 자리에서 그의 손에 죽음을 맞이한 수십여 명 중 하나였을 뿐이다.

다만 문제는, 사내가 이 실험의 결과를 썩 마음에 들어하지 않는다는 것에 있었다.

“누구든 입이 있으면 말을 해 보지, 응?”

이미 차갑게 얼어붙은 분위기 속, 사내의 앞에 늘어선 흑의인들은 조용히 마른침을 삼켰다.

눈앞의 사내에 대해서는 이미 익히 알고 있는 그들이다.

간혹 그의 심기가 뒤틀릴 때마다 꼭 피바람이 불었고, 그중에는 흑의인들의 동료도 있었다.

그런 광경을 수없이 보았으니 누가 감히 입을 열 수 있을까.

반복된 학습의 결과가 바로 지금의 침묵이다. 하지만 사내 역시 광포(狂暴)할지언정, 멍청한 인물은 아니었다.

“허, 이것들 봐라. 꼴에 술사(術師)라고 불러 주며 사람 취급해 줬더니…….”

피식 실소를 흘린 사내의 신형이 흐릿해진 그 순간.

퍽.

살점과 뇌수가 사방으로 튀었다. 머리통이 산산이 으스러진 흑의인, 아니 술사 중 하나가 썩은 고목 나무처럼 허물어졌다.

쿵.

마치 천둥처럼 울려 퍼지는 소리를 듣자, 술사들은 자신들이 곧장 해야 할 행동을 깨달았다.

털썩.

망설임 없이 꿇리는 무릎들.

반복된 학습을 통해 배운 것은 침묵뿐만이 아니다.

술사들은 이미 알고 있었다. 아무리 사내가 잔인무도한 인물이라 해도, 최소한 자신들에 한해서는 굳이 많은 피를 보려 하지 않는다는 것을.

“부, 부디 노기를 가라앉혀 주십시오.”

“혈주(血主)시여……!”

사내, 혈주는 은은한 혈광(血光)이 서린 눈으로 돌바닥에 머리를 찧으며 부르짖는 술사들을 굽어보았다.

‘벌레 같은 놈들.’

마음 같아서는 지금 당장이라도 저들의 사지를 찢어발기고 싶었지만, 혈주는 자꾸만 솟구치려는 살심을 애써 억눌렀다.

‘서천(西天)에 이어 남천(南天)도 죽었다. 대업을 이루기 위해서는 조금이라도 전력을 보존해야 할 터.’

하물며 술사는 귀한 존재다. 괴력난신(怪力亂神)의 힘을 다루는 이들은 암천 내에서도 그리 많지 않았고, 제법 오랜 세월 동안 진행해 온 연구들도 상당한 결실을 보고 있었다.

다만 오늘은 그 결과가 혈주의 마음에 들지 않았을 뿐.

머지않아 어느 정도 완성된 결과물이 나온다면, 그 파급력은 천하를 집어삼키고도 남을 것이 틀림없었다.

“부족해. 아직 부족하단 말이다.”

혼잣말처럼 불쑥 내뱉은 혈주의 말에, 술사들은 더욱 깊숙이 고개를 조아렸다.

부족하다면 어떻게든 채워야 한다. 앞서 죽은 동료와 같은 꼴이 되기는 싫었다.

“혈주시여. 혹여 어느 부분이 미흡하다고 느끼셨는지…….”

“하나부터 열까지. 전부.”

천천히 뒤돌아선 혈주가 사방에 널브러진 시신들을 가리키며 말을 이었다.

“하나같이 약해 빠졌더군. 게다가 지속 시간도 여전히 제자리걸음이고.”

“저희 역시 개선책을 찾고는 있습니다만, 두 가지 약효를 동시에 상승시키기에는 턱없이 부족합니다. 절정 고수의 수급도 마찬가지고요.”

변명 같은 대답에 혈주는 눈살을 찌푸렸지만, 이번만큼은 납득할 수밖에 없었다.

절정 고수는 하루아침에 만들어지는 것이 아니다.

뛰어난 인재만을 받아들이는 중원의 명문대파(名門大波)에서도 십 년 이상의 혹독한 수련을 거쳐야 도달할 수 있는 것이 절정의 경지였다.

타고난 재능과 노력의 여하에 따라 그 기간이 차이가 날 뿐. 정파의 것보다 훨씬 숙련 속도가 빠른 사마외도(邪魔外道)의 무공도 예외는 아니었다.

모든 것을 쉽게 얻을 수는 없는 법.

무공의 정순함과 깊이가 떨어지는 만큼, 절정의 벽 앞에서 좌절하는 이들의 숫자는 셀 수도 없이 많았다.

‘그 두 놈이 예외일 뿐이지.’

차마 소리 내어 말하지 못한 혈주가 입술을 깨물었다.

그리 오래되지 않은 과거를 떠올린 그의 두 눈동자에는 어느덧 핏빛 광망이 일렁이고 있었다.

‘진태경. 청풍.’

처음에는 지렁이라고 생각했다. 그저 힘주어 밟으면 툭, 하고 터져 버리는 지렁이.

하지만 그 두 마리의 지룡(地龍)은 어느 순간 천룡(天龍)이 되어 있었다. 오물로 가득한 진흙탕에서 빠져나와 푸른 하늘을 훨훨 날아다니는 천룡.

‘아니, 적어도 한 놈만큼은 처음부터 지렁이가 아니었지.’

혈주도 내심으로는 인정했다. 자신이 청풍을 지렁이에 빗댄 것은 너무 박한 평가일지도 모른다고.

검성 매종학이 말년에 받아들인 막내 제자.

그야말로 하늘이 내린 무재(武才).

청풍은 무림 역사상 그 전례를 찾기 힘든 천재였고, 태생부터 용의 운명을 타고난 이였다.

하지만…….

‘진태경, 그놈은 도대체 뭐지?’

태원진가의 대장로, 진양백의 배후에 있던 혈주는 오래전에 진태경에 대한 보고를 들었던 그 날을 똑똑히 기억했다.

모든 보고를 끝마친 수하에게, 자신이 처음으로 던졌던 한마디도.



‘다시 조사해라.’

‘예?’

‘어떻게 이런 병신 같은 놈이 있을 수 있단 말이냐. 뭔가 감춰져 있음이 분명하다.’



그럴 수밖에 없었다.

무공은 삼류 왈패보다도 못한 수준에 계획표까지 짜 놓고 온갖 기루를 싸돌아다닌다.

무너져 가는 집안 한번 일으켜 세워 보겠다고 애쓰는 첫째와 밤낮없이 무공을 갈고 닦는 둘째가 태원진가의 대들보라면, 진태경은 남아 있는 기둥을 뿌리부터 갉아 먹고 있었다.

그야말로 지렁이.

아니, 버러지.

하지만 그랬던 진태경이 어느 날부터 달라졌다.

청풍과는 달리 태생부터 버러지였던 놈이 지렁이가 되더니 이내 독을 품은 지네에서 이무기, 마침내는 용이 되었다.

그리고 그 모든 과정을 파악한 혈주는 경악을 금치 못했다.

‘놈은 이미 상식을 벗어났다. 그것도 아득하게.’

청풍은 처음부터 용의 운명을 타고난 자. 그렇기에 지금에 이르러 용으로 불린다 한들 조금도 이상할 것이 없다.

그러나 진태경은 청풍과 달리 하늘로부터 용의 운명을 부여받지 못했다.

놈은 그저 한낱 버러지, 지렁이에 지나지 않았다. 밟으면 꿈틀거리는 것만이 진태경이 할 수 있는 전부였다.

분명, 그것이 전부여야 했다.

욱신.

혈주는 불현듯 찾아온 통증을 느끼며 이를 악물었다.

시선을 내리니 멀쩡히 붙어 있는 두 팔이 보인다. 한때 누군가의 자줏빛 강기(罡氣)에 잘려 나갔던, 하지만 이제는 더욱 강력하게 거듭난 그것은 어느새 잘게 떨리고 있었다.

두려움 때문에? 아니다, 이건 분노다.

그와 동시에 영혼에 각인된 고통과 치욕이기도 했다.

‘진태경, 그놈이 훼방만 놓지 않았어도…….’

으득, 이를 악문 혈주는 그날의 기억을 떠올렸다.

피투성이가 되어서도 자신의 발목을 붙잡고 놓지 않았던 진태경의 모습과 자신의 팔을 가로지르던 검성 매종학의 강기를.

그러나 고통보다 참기 어려웠던 것은 다른 이들의 비웃음이었다.

물론 그중 두 사람은 이미 고혼(孤魂)이 되어 버렸지만.

‘서천, 그리고 남천. 그곳에서 똑똑히 지켜보아라. 너희 두 연놈이 이루지 못한 일을 내가 해내고 말 테니까.’

서천마군과 남천마후는 자존심 강한 혈주조차 무시할 수 없었던 강자들.

그런 그들의 죽음은 암천에게 있어 막대한 손실이었지만, 혈주에게 두 가지 교훈을 남겼다.

첫째. 진태경을 상대할 때는 결코 방심해서는 안 된다는 것.

둘째. 천주를 도와 대업(大業)을 이루기 위해서는, 지금보다 더욱 강대한 전력과 노력이 필요하다는 것.

“뿌려라.”

“예?”

불쑥 입을 연 혈주는 본능적으로 반문한 술사들을 응시했다.

조금 전만 하더라도 은은한 핏빛 안광이 비치던 그의 눈은 차갑게 가라앉아 있었다.

“대전(大戰)이 시작된 이상, 지금은 조금이라도 더 많은 전력을 끌어모아야 한다. 언제까지 이런 실험에 절정 고수들을 소모할 수는 없지.”

“그 말씀은…….”

“이미 중원 곳곳에 씨앗을 뿌려 놓은 것으로 안다. 내 말이 틀렸느냐?”

술사들의 수장이 길게 읍했다.

“아닙니다. 씨앗 중 일부는 이미 꽃을 피웠습니다.”

그 대답은 사실이었다.

암천은 막대한 재물과 긴 시간의 연구를 통해 ‘씨앗’을 만들었고, 이미 오래전에 그중 일부를 천하 곳곳에 흩뿌려 놓았다.

어떤 것은 정파 무림의 중심이라 할 수 있는 하남과 섬서로, 또 어떤 것은 변방에 속한 광서나 광동으로.

혹은…… 산서성과 인접한 북부 고원으로.

그것은 중원 무림의 혼란을 야기하는 동시에 일종의 실험이었고, 불과 한 달 전에는 한 성(城)을 뒤흔들었던 적도 있었다.

아니, 정확히는 뒤흔들 ‘뻔’했었다.

“광서성에서는 보기 좋게 실패했더군.”

“그건…….”

“안다. 화왕(火王), 그 늙은이가 때마침 땡중 행세까지 내며 나타나지 않았다면 성과를 냈을 수도 있었겠지.”

광서성에서 일어난 사파의 준동은 결코 우연이 아니다.

‘씨앗’을 가진 자가 세력을 끌어모았고, 광서 땅의 절반을 장악하기도 했었다.

적어도 혈승(血僧)이라는 별호로 정체를 숨긴 적천강에게 머리가 박살 나기 전까지는 그랬다.

“하오나 그것들도 약효가 개선되기 전에 만들어진 실패작입니다. 만약 현재 저희가 가진 것들이 잘못된 경로로 흘러 들어간다면…….”

“상관없다.”

칼날이 되돌아올 것을 염려하는 술사의 말을 단호하게 잘라 낸 혈주가 말을 이었다.

“씨앗이 될 만한 놈들을 선별해 내고, 깊숙이 파묻어라. 때가 되면 언제든지 퍼트릴 수 있게.”

그런 혈주의 모습에, 술사들은 더 이상의 변명은 불가능하다는 것을 깨달았다.

이제 그들 앞에 놓인 길은 두 개뿐이다.

하나는 순응. 또 하나는 죽음.

혈주의 주장이 틀린 것도 아니었으니, 술사들은 전자(前者)를 택할 수밖에 없었다.

“존명(尊命).”

깊숙이 허리 굽힌 술사들을 내려다보는 혈주의 눈동자가 번뜩였다.

그의 뇌리에는 불과 열흘 전, 예고도 없이 긴 잠에서 깨어난 천주와의 대화가 선명하게 각인되어 있었다.



‘때가 되었구나.’

‘천주시여, 그 말씀은.’

‘천하가 뒤틀리고 있다. 이제…… 하늘을 무너트려라.’



혈주는 길게 심호흡했다.

천주는 한 가지 명령을 끝으로 다시 잠에 빠졌고, 당신의 충실한 종에게 믿을 수 없는 기회를 주었다. 천주의 이름으로, 활시위를 당길 기회를.

그리고 지금 이 순간, 혈주는 본능적으로 직감했다.

지금이 바로 그 시위를 놓을 때라는 것을.

“전서를 띄워라.”

그날. 검은 깃털을 지닌 수십여 마리의 매가 하늘을 날았다.
```

## Final English reading copy

```markdown
# Chapter 844

“Is that it?”

The man who spoke looked to be around thirty at most. An ordinary face, the kind you might see several times in a day while walking through a marketplace.

And yet no one would dare look at him and think he was ordinary.

Because he was standing not in a marketplace, but in a pool of dark-red blood.

“It’s certainly improved, but it’s still nowhere near what I expected…”

Crunch.

The man stepped on an arm half-submerged in the pool of blood and continued.

“Did you call me here just to show me this?”

The owner of the arm? He didn’t know. He had no need to know.

It was just one of countless test subjects, one of the dozens who had met their deaths at his hands here today.

The problem was simply that the man wasn’t particularly pleased with the results of the experiment.

“Anyone with a mouth can speak up, can’t they? Hm?”

In the already icy atmosphere, the black-robed men lined up before him swallowed dryly in silence.

They knew the man before them all too well.

Whenever his temper turned sour, a storm of blood always followed—and some of the black-robed men’s own comrades had been caught in it.

They had witnessed that scene countless times. Who would dare open their mouth?

The silence now was the result of repeated lessons. But the man, for all his rage, wasn’t stupid.

“Hah. Look at you lot. I called you sorcerers and treated you like people, and this is what I get…”

The instant the man let out a quiet laugh, his figure blurred.

Thud.

Flesh and brain matter flew in every direction. One of the black-robed men—or rather, sorcerers—crumpled like a rotten tree, his head smashed to pieces.

Boom.

At the thunderous sound, the sorcerers realized what they had to do at once.

Thump.

They dropped to their knees without hesitation.

Silence wasn’t the only thing they’d learned through repeated lessons.

The sorcerers already knew that no matter how cruel the man was, he didn’t care to spill much blood when it came to them.

“P-please, calm your anger.”

“Blood Lord…!”

The man—the Blood Lord—looked down at the sorcerers crying out as they pounded their heads against the stone floor, his eyes faintly glowing red.

*Vermin.*

He wanted to tear their limbs off right then and there, but the Blood Lord forced down the urge to kill that kept welling up inside him.

*The Western Heaven Demon Lord is dead, and now the Southern Heaven Demon Empress is dead, too. We have to preserve whatever strength we can if we’re to accomplish our great cause.*

Sorcerers were precious, after all. There weren’t many in Dark Heaven who could wield the power of the supernatural, and the research they’d been conducting for many years was finally bearing considerable fruit.

It was just that today’s results hadn’t pleased the Blood Lord.

Once they produced something close to a finished result, its impact would be enough to swallow the whole world.

“Not enough. I said it’s still not enough.”

At the Blood Lord’s abrupt words, spoken as if to himself, the sorcerers bowed their heads even lower.

If it wasn’t enough, they would have to make up the difference somehow. They didn’t want to end up like their comrades who had died before them.

“Blood Lord. If you could tell us which parts you found lacking…”

“Everything. From beginning to end.”

The Blood Lord slowly turned and gestured toward the bodies scattered all around.

“They were all far too weak. And the duration still hasn’t improved at all.”

“We’re also searching for ways to improve it, but our resources are nowhere near enough to increase the potency of both effects at once. The same goes for obtaining the heads of Peak masters.”

The Blood Lord frowned at the excuse-like answer, but this time he had no choice but to accept it.

Peak masters couldn’t be made in a day.

Even in the Central Plains’ great sects, which accepted only the most gifted, it took more than ten years of grueling training to reach the Peak realm.

The time varied according to talent and effort, but that was all. Even demonic, heterodox martial arts, which could be mastered far faster than orthodox techniques, were no exception.

Nothing came easily.

With martial arts that lacked purity and depth, countless people faltered before the wall of the Peak realm.

*Those two were the exceptions.*

The Blood Lord bit his lip, unable to say it aloud.

As he recalled the not-so-distant past, a bloody gleam began to flicker in his eyes.

*Jin Taekyung. Cheongpung.*

At first, he’d thought they were earthworms. Earthworms that would pop if you stepped on them with a little force.

But at some point, those two earth dragons had become heavenly dragons. They’d escaped the mud pit filled with filth and soared freely through the blue sky.

*No. At least one of them was never an earthworm to begin with.*

Even the Blood Lord had to admit it to himself. Comparing Cheongpung to an earthworm might have been too harsh.

The youngest Disciple accepted by Sword Saint Mae Jonghak in his later years.

A martial talent bestowed by the heavens.

Cheongpung was a genius whose equal was hard to find in all of Murim’s history, a man born with the destiny of a dragon.

But…

*What the hell is Jin Taekyung?*

The Blood Lord, who had been behind Jin Yangbaek, Head Elder of the Jin Family of Taiyuan, remembered all too clearly the day he first heard a report about Jin Taekyung, long ago.

He also remembered the first words he’d said to the subordinate who had finished giving the report.

*“Investigate him again.”*

*“Pardon?”*

*“How can a piece of shit like that exist? He must be hiding something.”*

It was only natural.

His martial arts were worse than those of a Third Rate street thug, and he even had a schedule laid out for wandering around every pleasure house in sight.

If the eldest son, who struggled to raise the crumbling family back up, and the second son, who trained day and night, were the pillars of the Jin Family of Taiyuan, then Jin Taekyung was gnawing away at the remaining pillars from the roots up.

An earthworm, plain and simple.

No—a bug.

But one day, Jin Taekyung changed.

Unlike Cheongpung, Jin Taekyung had been born a bug. Then he became an earthworm, then a venomous centipede, then an imugi, and finally a dragon.

And when the Blood Lord understood the whole process, he couldn’t hide his astonishment.

*That bastard has already gone beyond common sense. By a mile.*

Cheongpung was born with the destiny of a dragon. So there was nothing strange about him being called one now.

But unlike Cheongpung, Jin Taekyung had not been granted the destiny of a dragon by the heavens.

He had been nothing but a bug, an earthworm. The only thing he could do was writhe when stepped on.

That should have been all he could do.

Throb.

The Blood Lord clenched his teeth as a sudden pain struck him.

He looked down and saw both arms, still attached and whole. Once severed by someone’s purplish Force, they had since grown back even stronger—but now they were trembling slightly.

Was it fear? No. This was anger.

And, at the same time, pain and humiliation etched into his soul.

*If Jin Taekyung hadn’t gotten in my way…*

Grinding his teeth, the Blood Lord remembered that day.

Jin Taekyung, drenched in blood, clinging to his ankle and refusing to let go—and the Sword Saint Mae Jonghak’s Force sweeping across his arm.

But what had been harder to bear than the pain was the ridicule of others.

Though two of them had already become lonely spirits.

*Western Heaven. Southern Heaven. Watch closely from wherever you are. I’ll accomplish what you two failed to do.*

The Western Heaven Demon Lord and the Southern Heaven Demon Empress had been powerful figures whom even the prideful Blood Lord couldn’t dismiss.

Their deaths were an enormous loss to Dark Heaven, but they had left him with two lessons.

First: never let his guard down when facing Jin Taekyung.

Second: to help the Lord of Heaven accomplish the great cause, he needed even greater strength and effort than before.

“Spread them.”

“What?”

The Blood Lord looked at the sorcerers, who had instinctively questioned him.

The faint red light in his eyes had gone cold.

“Now that the Great War has begun, we need to gather as much strength as we can. We can’t keep using Peak masters on experiments like these forever.”

“You mean…”

“I understand that you’ve already planted seeds throughout the Central Plains. Am I wrong?”

The head of the sorcerers bowed deeply.

“No. Some of the seeds have already blossomed.”

That was true.

Dark Heaven had created the “seeds” through vast sums of money and years of research, then scattered some of them throughout the land long ago.

Some had gone to Henan and Shaanxi, the heart of orthodox Murim; others to the border regions of Guangxi and Guangdong.

Or… to the northern plateau bordering Shanxi Province.

They were both experiments and a way to cause chaos in Central Plains Murim. Just a month ago, one had even shaken an entire city.

No—more precisely, it had *almost* shaken one.

“You failed spectacularly in Guangxi Province.”

“That was…”

“I know. If the Fire King—that old man—hadn’t happened to show up pretending to be a bald monk, it might have worked.”

The unorthodox faction’s uprising in Guangxi Province had been no coincidence.

The one who possessed a “seed” had gathered forces and even taken control of half of Guangxi.

At least, until his head was smashed by Jeok Cheongang, who had concealed his identity under the sobriquet Blood Monk.

“However, those were failures made before we improved their potency. If the ones we have now were to fall into the wrong hands…”

“It doesn’t matter.”

The Blood Lord cut off the sorcerer, who feared the blade might turn against them, and continued.

“Choose those fit to become seeds and bury them deep. Make sure they can be spread whenever the time comes.”

At the Blood Lord’s words, the sorcerers realized there was no room for further excuses.

Only two paths lay before them now.

Submission. Or death.

The Blood Lord wasn’t wrong, so they had no choice but to choose the former.

“We obey.”

The Blood Lord’s eyes flashed as he looked down at the sorcerers bowing deeply.

His conversation with the Lord of Heaven, who had awakened without warning from a long slumber just ten days ago, was etched clearly in his mind.

*“The time has come.”*

*“Lord of Heaven, what do you mean?”*

*“The world is twisting. Now… bring down the heavens.”*

The Blood Lord took a deep breath.

The Lord of Heaven had fallen asleep again after giving a single command, and had given his faithful servant an unbelievable opportunity. A chance, in the name of the Lord of Heaven, to draw the bowstring.

And at this very moment, the Blood Lord instinctively knew.

Now was the time to let the arrow fly.

“Send out missives.”

That day, dozens of hawks with black feathers took to the sky.
```

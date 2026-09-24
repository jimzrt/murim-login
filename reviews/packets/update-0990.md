<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0990.txt",
      "sha256": "c48b47d28afb1d71242aaae8327631fd2e3418429116fb75c08d5f8eb0fc3e59",
      "bytes": 16441
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "bc034b6f4bba3adb9d8c701191902106ad54b7ae4574464860349bbca849976e",
      "bytes": 982
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "d13308fe31a2c64daebd8b79b1737ef2a4f6a2f6e86338670363f6d7acf5174f",
      "bytes": 236719
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "34ab0d0e2f870c6bc8f3006ff2f131324eeddbc0720a928dc3aec92dee421b8f",
      "bytes": 1325
    },
    {
      "path": "characters/Hong Dao.md",
      "sha256": "e456f5c488e43079eba02d343aebacbea1898c3e164043b6f58635b78a1701ed",
      "bytes": 1000
    },
    {
      "path": "characters/Jang Sam.md",
      "sha256": "c9f4eeef1254f91db8c232463e1fad25107cc51968688a6af876231032ff7454",
      "bytes": 508
    },
    {
      "path": "characters/Jang-pal.md",
      "sha256": "f55ea4471d86a687007c78d1ac6aa610391a7d41eb92134c4317f09a6de93ef3",
      "bytes": 515
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "b464a3a2f32ba67b3f92eeb6ba9f407255da39eaf5fc323c9dc15c3a79662deb",
      "bytes": 1391
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "10b6d00e1682e9ec3eb5c019ed95ea99610ba534ec1c250e3b92e3cc8eabcd3b",
      "bytes": 1574
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "b4daab3a4e799c33f250cb7d7275476d15ea10b9c6e570dc860c6f06f4744a55",
      "bytes": 622
    },
    {
      "path": "characters/Peng Cheolhu.md",
      "sha256": "c2f1ca01a97e18b134940a2fef23e7839c6b6e9297f8b485d3cbd78a7ab1f36a",
      "bytes": 1001
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "db77d07af0d2996497db9ec79e415c53e423929110911bda4199b926946a5a04",
      "bytes": 685
    },
    {
      "path": "characters/Tang Taesang.md",
      "sha256": "8878f7f17f69aa9780ca8f4264a3102e585dec8711db597ba1dc02e6ceccc7a6",
      "bytes": 725
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "01eb505153b8bfb0f997a4ee2d2fc22bb3665499082f01713db4cac514f330d1",
      "bytes": 273291
    }
  ],
  "estimated_tokens": 14128
}
-->

# Durable State Update — Chapter 990

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
1 and safe_through 990. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 990. Profile updates may replace only one
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
  "chapter": 990,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 990,
    "continuity_sources": [990],
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
    "Peng Cheolhu died after successfully passing everything he had to Jin Taekyung through Transmitting Internal Energy Across the Body.",
    "Jin Taekyung underwent Bone Transformation after the transfer.",
    "Mae Jonghak regards the age as anomalous, with Dark Heaven, supernatural forces, grotesque monsters, and the Lord of Heaven at the center of growing danger.",
    "Unprecedented snowfall and rapidly changing heavenly patterns are occurring across the world.",
    "Song Ho ordered the Inner Hall officers summoned, the Outer Hall placed on alert, and messenger eagles dispatched."
  ],
  "continuity_sources": [
    989
  ],
  "open_questions": [
    "What is behind the worldwide weather and heavenly-pattern changes?",
    "Is the upheaval a scheme laid by some unknown power, as Mae Jonghak suspects?",
    "What are Dark Heaven and the Lord of Heaven planning?"
  ],
  "safe_through": 989,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 청풍     | **Cheongpung**     |
| 굉도     | **Hong Dao**       |
| 팽철후    | **Peng Cheolhu**   |
| 장삼 | **Jang Sam** | Bandit; personal name |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 검성     | **Sword Saint**               | Mae Jonghak    |
| 법왕     | **Dharma King**               | Hong Dao       |
| 살성     | **Slaughter Saint**           | —              |
| 벽력도왕   | **Thunderbolt Saber King**    | Peng Cheolhu   |
| 독왕     | **Poison King**               | Tang Taesang   |
| 십왕     | **Ten Kings**       |
| 태원진가   | **Jin Family of Taiyuan**        |
| 곤륜파    | **Kunlun Sect**                  |
| 무림맹    | **Murim Alliance**               |
| 암천     | **Dark Heaven**                  |
| 하북팽가   | **Hebei Peng Family**            |
| 정파     | **orthodox faction**                             |                                                       |
| 사파     | **unorthodox faction**                           |                                                       |
| 마교     | **Demonic Cult**                                 |                                                       |
| 강호     | **martial world**                                | Prefer “Murim” where the setting itself is meant      |
| 가주     | **Family Head**                              |
| 문주     | **Sect Leader**                              |
| 표국     | **Escort Bureau**                            |
| 제자     | **Disciple**                                 |
| 은인     | **Benefactor**                               |
| 명성               | **Fame**                       |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 청해     | **Qinghai**            |
| 곤륜     | **Kunlun**             |
| 정마대전   | **Great Faction War**         |
| 노부      | **this old man / I**                                            |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 소협      | **Young Hero**                                                  |
| 장팔 | **Jang-pal** | Woodcutter who meets and helps the unnamed old man. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 당사문 | **Tang Taesang** | Former Family Head of the Sichuan Tang Clan and Poison King; Tang Sadok’s father. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 구주 | **Nine Provinces** | Traditional geographic expression used in a threat. |
| 천자 | **Son of Heaven** | Honorific title for the Emperor. |
| 빙당호로 | **candied hawthorn skewers** | Traditional fruit skewers coated in hardened sugar; explained in a footnote. |
| 하북 | **Hebei** | Province where Hyuk Family Textile Shop has a branch. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 장씨 | **Jang** | Unspaced source variant of 장 씨; surname form for Jang-pal. |
| 태상가주 | **Grand Family Head** | Title held by the Azure Sky Sword King as head of the Nangong Family. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 도도 | **Dodo** | Term for the Star-Array Grand Banquet's major gambling matches. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 오씨 | **Oh** | Surname form used in the clue identifying the Luoyang Strange Physician. |
| 악귀 | **Fiend** | Descriptive epithet applied to the First Fiend. |
| 청해성 | **Qinghai** | Source form specifying Qinghai as a province. |
| 열화신룡 | **Blazing Flame Divine Dragon** | New sobriquet bestowed on Jin Taekyung. |
| 시리 | **City** | Second word in one of the necromantic chants. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 흑룡마문 | **Black Dragon Demon Gate** | Unorthodox faction from Gansu. |
| 모용세가 | **Murong Family** | One of the Five Great Families, based in Liaoning. |
| 화신 | **Fire God** | A local deity worshiped by one Nanman believer. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 청풍 | 진태경 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung repeatedly addresses Taekyung as 은인 after receiving food. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 관리 | 진태경 | official_to_young_martial_artist | Young Master | formal-polite | The official addresses Taekyung as 공자 while explaining the consequences of Prince Shangshan's displeasure. |
| 진태경 | 청풍 | companion_to_young_martial_artist | Young Master Cheongpung | formal-polite | Taekyung uses 청 공자 while correcting Cheongpung's royal-etiquette mistake. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 적천강 | 청풍 | overwhelming_elder_to_young_martial_artist | you / little punk | blunt, amused, and threatening | Jeok Cheongang uses 네, 이놈, and related blunt forms while testing Cheongpung. |
| 청풍 | 적천강 | young_martial_artist_to_overwhelming_elder | Grandpa Jeok | casual-familiar despite deference | Cheongpung uses 적 할아버지 while asking Jeok Cheongang to confirm Taekyung's condition; this is a familial form of address, not literal kinship. |
| 적천강 | 굉도 | old_friends | Hong Dao | familiar and teasing | Uses Hong Dao's personal name in their casual reunion. |
| 굉도 | 적천강 | old_friends | Fire Gate Sect Leader | familiar and teasing | Teases Jeok as the carefree Fire Gate Sect Leader. |
| 굉도 | 진태경 | senior_monk_to_guest_benefactor | Benefactor | formal-polite and probing | Hong Dao repeatedly addresses Taekyung as 시주 while identifying him as the Master of Morning Star. |
| 적천강 | 벽력도왕 | rival_martial_master_to_rival_martial_master | Virility Saber King | insulting and taunting | Jeok coins 정력도왕 as a taunting replacement for the established title. |
| 벽력도왕 | 적천강 | rival_martial_master_to_rival_martial_master | Jeok Cheongang | boisterous and hostile-teasing | The Thunderbolt Saber King calls Jeok by name before their argument escalates. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 관리 | 적천강 | government official to legendary martial master | you | formal, then alarmed and deferential | The official questions Jeok Cheongang, insults him as an old man, and later learns that he is the Fire King. |
| 적천강 | 관리 | legendary martial master to government official | you | blunt and mocking | Jeok Cheongang repeatedly echoes the official's formal phrasing while challenging his authority. |
| 벽력도왕 | 진태경 | elder martial master to younger rival | you | boisterous and confrontational | Peng addresses Taekyung as 네놈 while discussing Peng Dojin. |
| 태산 | 진태경 | subordinate_to_respected_outsider | Jin Taekyung | clipped and familiar | Taishan says he likes Jin Taekyung but will fight him without hesitation if Sama Pyo commands it. |
| 태산 | 적천강 | subordinate of a Young Sect Leader to legendary elder | Fire King | clipped, childlike, and deferential | Taishan gives his awkward greeting and expresses admiration for Jeok's strength. |
| 적천강 | 태산 | legendary elder to giant subordinate | you / strange fellow | blunt, startled, and grudgingly tolerant | Jeok addresses Taishan as 네놈 while reacting to his greeting and appetite. |
| 진태경 | 태산 | pavilion_master_to_pavilion_member | Taishan | forceful and commanding | Taekyung orders Taishan to stop eating the bear. |
| 적천강 | 법왕 | close deceased friend and peer | you | familiar and reflective | Jeok addresses the Dharma King in private thought while wishing he were present to clarify Jeok's confusion. |
| 진태경 | 벽력도왕 | younger martial artist to senior martial master | Great Hero Peng | formal and deferential | Taekyung offers a respectful salute and addresses Peng as 팽 대협. |
| 적천강 | 팽철후 | longtime friends and rivals adopting brotherly terms | Jeok hyung | informal and familiar | Peng accepts Jeok as his older brother; Jeok offers to call him younger brother, though they reserve that address for a future reunion. |
| 팽철후 | 적천강 | longtime friends and rivals adopting brotherly terms | Jeok hyung | informal and familiar | Peng addresses Jeok as hyung in their final conversation. |

## Listed compact profiles

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 989
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, the grandson and Disciple of Sword Saint Mae Jonghak, a Supreme Peak martial master known as the Huashan Divine Dragon, the creator of the snake-inspired Mimi Step footwork technique, and the master of the Azure Dragon Pavilion within the Alliance Leader's Two Dragons Pavilion.
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, a deep love of martial arts, competitive pride, unusual resistance to monster-induced Fear, and discomfort when someone copies his martial arts.
- **Voice:** Dreamy and hazy, with innocent, polite phrasing; he has begun imitating Taekyung's profanity.
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions while Taekyung is his only true martial rival; Tang Sadok has temporarily entrusted Mimi, now a large horned snake, to him, and Cheongpung is accompanying Mungyeong while learning his martial arts through observation to become stronger and adapt to this world.

### Hong Dao.md

# Hong Dao (굉도)

- **Safe through:** Chapter 989
- **Aliases:** Dharma King
- **Role:** Abbot of Shaolin and the Murim's Dharma King; master of Unnamed and the only friend to whom Jeok Cheongang had opened his heart; after leaving the Star-Array Grand Banquet, he was found in a massive pit with both legs severed and catastrophic internal injuries, whispered final words to Jeok Cheongang, and died.
- **Personality:** Calm, responsible, quietly playful, and still regarded by Jeok as lazy for sleeping whenever possible.
- **Voice:** Quiet, deep, weighty, and resonant, with casual familiarity when speaking to Jeok Cheongang.
- **Relationships:** Old friend of Jeok Cheongang and close friend of Peng Cheolhu; master of Unnamed; before his death, entrusted the Green Jade Buddha Staff to Unnamed, warned Jeok about Jongni Chu, Dark Heaven, Unnamed, and the Buddhist Staff, and sent Unnamed to find the Master of Morning Star.

### Jang Sam.md

# Jang Sam (장삼)

- **Safe through:** Chapter 945
- **Aliases:** Killing Ghost
- **Role:** Jang Sam is a bandit chief who abruptly rose from Level 40 to Level 60 and attacked Taekyung while apparently irrational; he is currently unconscious and being taken to the Nangong Family.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** No relationships established.

### Jang-pal.md

# Jang-pal (장팔)

- **Safe through:** Chapter 452
- **Aliases:** None
- **Role:** Woodcutter from Jang Family Village who encounters and helps the unnamed old man.
- **Personality:** Simple, kind, polite, and guileless.
- **Voice:** Plain, respectful, and good-natured.
- **Relationships:** Husband whose wife prepares his rice ball; lives in Jang Family Village and helps the unnamed old man by sharing food and carrying him down the mountain.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 989
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; believes there is no absolute justice and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, and insists on protecting Taekyung while urging him not to risk his life; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 989
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor has appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure, willing to risk himself for others, and unwilling to excuse cruelty as the inevitable price of survival.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; Peng Cheolhu regarded Taekyung as a worthy successor, inheriting all that Peng had to pass on; So Gyo says he is the chosen one spoken of by the Martial God, while the Bow Saint sought him for decades and relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 989
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Peng Cheolhu.md

# Peng Cheolhu (벽력도왕)

- **Safe through:** Chapter 989
- **Aliases:** Thunderbolt Saber King
- **Role:** Peng Cheolhu was the Thunderbolt Saber King, a Ten Kings master and Great Hero of the Hebei Peng Family who died as his accumulated internal energy and remaining life force melted into the flames of Taekyung’s advancement.
- **Personality:** Boisterous and teasing with old friends, yet calm and accepting in the face of death; willing to give everything he has left to protect the world.
- **Voice:** Loud, blunt, confrontational, and prone to disguising embarrassment or retreat as serious martial instruction.
- **Relationships:** He was Jeok Cheongang’s long-standing rival and friend, Hong Dao’s close friend, protective toward Hong Dao’s Disciple Unnamed, father of Peng Cheolyeong, and longtime friend and former youthful rival of Murong Baek; Jeok and Peng parted reconciled as brothers in all but blood.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 983
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo; becomes explosively violent when his meat is threatened.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord, trusts Jin Taekyung as Pavilion Master, and has grown attached to the Fire Dragon Pavilion members.

### Tang Taesang.md

# Tang Taesang (당사문)

- **Safe through:** Chapter 525
- **Aliases:** Poison King
- **Role:** Former Family Head of the Sichuan Tang Clan and Supreme Peak master, he was renowned as the world's leading authority on poison and hidden weapons; after retiring to Meishan, he was tortured and killed by the Western Heaven Demon Lord.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** His only child, Tang Sadok, succeeded him as Family Head; Taesang gave him the Thousand-Year Poison Horned Snake as his first and last gift, and Sadok pursued his father's killer.

## Korean source

```text
＃990화



벽력도왕 팽철후.

하북팽가의 태상가주이자, 정마대전이 낳은 또 한 명의 거인이 쓰러졌다는 소식은 그야말로 성난 들불처럼 퍼져 나갔다.

“그분만큼은 굳건히 버티시리라 믿었건만……. 기어코 이리되는군.”

“아무리 그래도 그렇지. 설마하니 도왕(刀王)께서 이처럼 덧없이 떠나실 줄이야.”

“덧없이? 그런 헛소리는 내 앞에서 두 번 다시 꺼내지 말게. 팽 대협께서는 마지막까지 의기(義氣)를 잃지 않으셨어.”

“그만하게. 저 친구도 몰라서 한 소리겠나. 그저 안타까워서 하는 소리지.”

“알고 있네. 빌어먹을. 나도 알고 있다고.”

생각지도 못한 비보(悲報)를 접한 무림인들은 하나같이 애통함을 감추지 못했다.

그들에게 있어 십왕(十王)이라는 별호에 깃든 의미는 그만큼 남달랐으니까.

그러나 모든 이의 존경을 한 몸에 받았던 법왕 굉도도.

수많은 마교도들을 공포로 몰아넣었던 독왕 당사문도.

마지막으로 화왕 적천강이라는 압도적인 존재를 제외한다면, 십왕의 실질적인 수좌(隨坐)나 다름없던 벽력도왕마저 죽음을 맞이했다.

그리고 그들의 사인은 노화로 인한 자연사도, 병사도 아니었다.

“모두 잊지 말게. 그분들은 협의를 위해 싸우다 명예롭게 전사(戰死)하셨고, 그에 대한 복수는 곧 우리의 몫이라는 것을.”

정파 무림의 상징이자, 의기의 표상이었던 노강호들의 잇따른 죽음.

무림인들은 그렇게 애통함이라는 감정 위에 분노를 덧칠했다.

떠나간 이들의 복수를 위해.

마교 이후 처음으로 나타난, 그 어느 때보다 위협적인 힘을 드러낸 새로운 적을 쓰러트리기 위해.

“암천(暗天)과 맞서 싸울 자, 누구인가!”

“검을 들고 일어나라! 구주천하를 위해, 정의와 협의를 위해 저 천인공노할 악귀들과 맞서 싸우라!”

거리 곳곳에서 터져 나오는 힘찬 외침들은 이제 예삿일이었다.

모용세가의 일례를 반면교사 삼은 일파(一派)의 문주와 가주들은 잦은 회동 속에서 묵은 감정을 털어 냈고, 혈기로 들끓는 젊은이들은 피 한 방울 묻혀 보지 못한 병장기를 손바닥이 찢어지도록 휘둘렀다.

돌멩이가 움직여도 자국이 남는 법인데, 그것이 태산(太山)이라면 오죽할까.

비좁은 협곡을 사이에 두고 벌어진 산서성에서의 혈전.

이른바 팔천혈겁(八天血劫)이라 불리게 된 사건과 벽력도왕의 죽음은 마지막 기폭제나 다름없었다.

아직 정확한 전력이 드러나지 않았음에도 천하 곳곳에서 숱한 피바람을 불러일으키는 암천의 행보에 두려움을 품고 있던 이들도, 일찍이 암천과 맞서는 것에 대해 비교적 미온한 반응을 보이던 정사지간의 무림인들도 이제는 확실히 알게 되었다.

암천의 손에 들린 저 예리하기 그지없는 칼날이, 정파 무림뿐만이 아니라 천하 전체를 노리고 있다는 것을.

그리고 그로 인한 파장은, 이제 무림이라는 울타리를 아득히 넘어선 지 오래였다.

“그래, 어디에서 온 누구인가?”

“정가촌에서 온 장팔입니다.”

“장팔? 정가촌에서 왔다면서 왜 장씨야?”

“예?”

“왜 장팔이냐고.”

“아, 그것이…….”

“그것이, 뭐?”

“아버지가 외지인입니다.”

“외지인이라. 그럼 데릴사위라 이거로군. 정가촌에 정착한.”

“예, 예. 그렇지요.”

“나이는?”

“올해로 약관이 되었습니다.”

모병관으로 임명된 하급 관리는 눈앞의 청년. 아니, 소년이라 불려야 마땅할 지원자를 위아래로 훑었다.

“약관?”

“예. 그렇습니다!”

“그렇군. 그럼 모친의 존함은 어찌 되시나?”

“예?”

“이야기를 죽 들어보니 얼굴도 왠지 낯이 익기도 하고, 내가 아는 사람 같기도 해서 말이야. 혹시 아나? 좋은 게 좋은 거라고, 만약 맞다면 전공(戰功)을 쌓기에 괜찮은 곳으로 보내 주지.”

하급 관리의 은근한 목소리에, 소년의 눈동자가 반짝였다.

“저, 정말이십니까?”

“그렇다니까. 그래서 모친 존함은?”

소년은 잠시 망설였지만, 갈등은 그리 길지 않았다.

비록 집안의 허락은 받지 못했으나, 마음에 품은 의기와 풍운(風雲)의 꿈은 그 어느 때보다 크게 부풀어 올라 있었다.

만약 눈앞의 하급 관리와 부모님이 친분이 있다면, 좋은 전장에 배치되어 눈부신 공적을 쌓아 소년 장수가 될 수도 있는 절호의 기회 아닌가.

‘나도. 나도 반드시 그분처럼.’

마음의 결정은 이미 내렸다.

단 한 번도 본 적 없는 우상을 떠올리며 용기를 얻은 소년은, 어설프게나마 제 손으로 직접 깎아 만든 죽창(竹槍)을 힘껏 말아쥐며 입을 열었다.

“그, 감나무 집 오씨댁 둘째 딸이라고 하면 인근에서는 어느 정도 알 거라고 하셨…….”

“가라.”

“예?”

“아버지는 정씨고, 어머니는 오씨인데 왜 정가촌에 살아?”

“……!”

“왜, 할 말이 남았나?”

이미 다 안다는 듯, 날카로운 눈매로 자신을 노려보는 하급 관리의 모습에 경직되어 있던 소년은 가까스로 목소리를 끄집어냈다.

“사실 저희 집안 전체가 외지인 출신이라…….”

“뭐 하나. 이놈 당장 끌어내!”

“헉, 나리! 안 됩니다! 진짜 안 됩니다! 저를 내치시면 진짜 후회하실 겁니다!”

소년은 강렬한 의지를 담아 눈을 부릅떴고, 이와 같은 모습에 깊은 감명을 받은 하급 관리는 소년의 양팔을 붙든 관병에게 지시했다.

“궁둥이 세 대만 두들겨서 쫓아내게. 약관? 약관은 개뿔이. 어린 놈의 새끼가 어딜 거짓부렁으로도 모자라서 어른한테 눈을 부릅뜨고 있어.”

“나리이!”

애타게 부르짖었음에도 반전은 없었다.

황실의 포고문이 온 천하 곳곳에 퍼진 이후, 입신양명(立身揚名)의 꿈과 끓어오르는 혈기를 참지 못한 이들로 각 성의 관청은 늘 문전성시를 이루고 있었다.

그로 인해 암천은커녕 과로로 죽게 생긴 하급 관리는 나이까지 속여 입대하려는 소년들에게 학을 뗀 상황이었으니.

“두 대 더 때려!”

“안 돼애!”

“돼!”

결국 관병에 의해 호되게 엉덩이를 걷어차인 소년은 초라하게 쫓겨났고, 관청 밖까지 꼬리에 꼬리를 물고 있던 지원자들은 그 광경을 보며 숙덕였다.

“내 동생보다 어려 보이는데.”

“그래도 어린놈이 의기가 제법이오. 대가리가 영 빡통인 게 문제지만.”

“한데, 저 아이가 어디에서 온 누구라고 했소?”

“알아봤자 소용없소. 어차피 지어낸 말이 뻔한데 뭘.”

“아니, 그래도 꼭 알아야겠소.”

“왜 굳이 그렇게까지 집착하는 거요?”

“나도 지어냈으니까.”

“…….”

“괜히 출신지 지명이 겹치면 안 되잖소. 들키면 나도 저 꼴 날 텐데.”

“……혹시 나이가 어찌 되시오?”

“열여섯.”

“지랄 마시오. 얼굴은 이미 백전노장인데.”

“고맙습니다, 형님. 저는 무사히 통과하겠네요. 그리고 이 사실은 비밀로 해 주세요.”

“……아니, 농담이 아니었다고?”

모두가 충격의 구렁텅이에 빠진 그때, 늙수그레한 용모를 한 지원자가 비틀비틀 일어나는 소년을 향해 말했다.

“너, 몇 살이냐?”

넋 놓은 눈빛으로 관청을 바라보던 소년이 대답했다.

“열여섯입니다.”

“나랑 동갑이네. 이것도 인연인데 말 편하게 해.”

“지나가는 개새끼도 안 믿을 소리 하지 마십시오. 가뜩이나 기분 더러우니까.”

“진짠데.”

“안 속아……요.”

“그보다 너, 그 창 어디서 났어?”

우물쭈물하던 소년이 대답했다.

“직접 깎아서……요.”

“우리 또래는 보통 검을 쓰지 않나? 나처럼.”

그 순간, 복잡하던 소년의 표정이 삽시간에 일그러졌다.

“누가 그딴 소리를 해? 창이야말로 만병지왕인데.”

“이제야 말을 놓네. 그리고 난 검이 최고라고 한 적은 없어. 그냥 보통은 그렇다는 거지.”

“아.”

“병장기 문제로 괜히 발끈하는 거 보니까 하나는 알겠네. 너, ‘그 사람’처럼 되고 싶어서 온 거지?”

다 안다는 듯이 건넨 물음에, 잠시 머뭇거리던 소년이 훨씬 누그러진 목소리로 대답했다.

“그분이야.”

“뭐?”

“그분. 그 사람이 아니라, 그분이라고.”

풀 죽어 있던 모습은 이제 온 데 간 데 찾을 수 없었다.

언제 그랬냐는 듯, 소년은 지금 막 관청에서 쫓겨 났다는 사실도 잊은 채 생기 넘치는 눈빛으로 말을 이었다.

“열화신룡 진태경. 난 그분처럼 될 거야. 반드시!”

누구나 각자가 원하는 목표가 있는 법.

소년에게는 진태경이라는 존재가 바로 그런 목표였다.

온 천하가 주시하는 강호의 젊은 협객이자, 하늘 같은 천자께서 친히 임명하신 고귀한 열후(列侯).

선망했고, 존경했다.

당당한 걸음으로 이곳에 올 때까지만 해도, 머지않아 그분과 어깨를 나란히 할 것이라는 포부에 들떠 있었다.

물론 현실은 엉덩이를 걷어차여 쫓겨 났지만.

“젠장.”

소년이 침울하게 고개를 떨군 그때였다.

어디선가 낯선 목소리가 불쑥 들려온 것은.

“우와! 너무 멋져요!”

고개를 들어 목소리의 주인을 확인한 소년은 눈을 깜빡였다. 아니, 관청 밖에서 대기하던 지원자들 모두가 마찬가지였다.

‘뭐야, 이 사람은?’

‘언제 나타났지? 조금 전에는 없었던 것 같은데.’

‘어. 아닌가? 있었나?’

‘다시 생각해 보니까 처음부터 여기 있었던 것 같기도 하고…….’

얼떨떨하게 주고받는 눈빛과 그 안에 담겨 있는 의문들.

하지만 그들이 제대로 된 갈피를 잡기도 전에, 갑작스럽게 모두의 앞에 나타난 청년은 환하게 웃으며 소년을 바라보고 있었다.

“제가 할아. 아니, 누구한테 들었는데. 이루고자 하는 목표가 있는 건 좋은 거랬어요!”

“예, 예?”

소년은 당황 어린 눈빛으로 청년을 바라보았다.

먼지로 뒤범벅이 된 장삼(長衫) 때문인지 평범을 넘어 후줄근해 보이는 외모.

아마도 그 때문일까.

갑작스러운 등장과 안면 트기에 당황스러운 것도 잠시, 경계심보다는 알 수 없는 친근함이 소년을 비롯한 모두를 휘감고 있었다.

이건 마치. 마치…….

그래.

‘동네에 꼭 한 명쯤 있는, 모자란 형.’

지금 이 순간만큼은 모두의 생각이 일치했고, 그렇게 믿을 수밖에 없었다.

티 하나 없는 저 순백의 웃음을 보라.

악의라고는 눈곱만큼도 느껴지지 않는 눈동자는 냇가의 물보다 맑았고, 곧이어 소년의 손을 움켜쥔 째 연신 흔들어 대는 모습은 어린아이의 그것을 연상케 했다.

“멋있어요! 반드시 열화신룡처럼 되겠다니. 정말로 대단해요!”

그나마 양손이 구속된 채 눈을 동그랗게 뜨고 있던 소년이 의식의 끈을 되찾을 수 있던 것은, 뻐근해진 어깻죽지 덕분이었다.

“저, 저기 손을 좀.”

“아, 미안해요. 기분이 좋아서 그만. 많이 아팠어요?”

웃는 얼굴에 침 못 뱉는다고, 진심으로 걱정하는 듯한 저 표정을 보니 뭐라 할 수도 없었다.

“……아뇨, 괜찮습니다. 그런데 대관절 어디의 뉘신지.”

“그냥 지나가는 협객이에요. 소협처럼 천하를 구하고자 하는!”

가슴을 쭉 편 채 토해 내는 당당한 외침에, 소년을 비롯한 모두는 확신했다.

‘모자란 놈 맞구나.’

그리고 그 확신을 증명하듯, 청년은 이상해진 분위기를 알아차리지 못한 채 계속해서 하고싶은 말들을 떠벌렸다.

“그런데 소협. 열화신룡처럼 되고 싶다면서 관청에는 왜 왔어요? 차라리 태원진가로 직접 찾아가는 것도 좋은 방법일텐데.”

“아, 그게 워낙 거리가 멀어서요. 살아생전 백 리 밖으로도 나가본 적이 없는 제가 어찌…….”

“멀긴 하지만, 그 정도로 멀진 않던데?”

“멀지 않다고요? 이곳, 청해(靑海)에서 산서까지가?”

“생각보다 금방 가요. 포기하지 않고 열심히 달리기만 하면.”

곳곳에서 실소가 터져 나왔다.

청해성에서 산서성까지는 과장 조금 보태서 만 리에 달하는 거리.

봇짐 몇 개를 짊어 매고 천하를 종횡하는 늙은 보부상들과, 어지간한 대형 표국조차 이 정도의 장거리 의뢰는 가급적 받지 않는다.

그만큼 고되고 미치도록 지겨운 여정이니까.

이동을 업으로 삼는 그들조차 이럴진대, 하물며 서쪽 끄트머리의 변방에 속한 청해성의 사람들은 어떻겠나.

그야말로 모자란 놈이나 할 수 있는 헛소리였다.

물론, 남들의 비웃음을 받을 만큼 허무맹랑한 꿈을 품은 소년의 귀에는 조금 다르게 들렸지만.

“포기하지 않고, 열심히만 하면 된다고요?”

“네. 그럼요! 설령 먼 곳에 있는 태원진가가 아니더라도 다른 선택지는 있는걸요? 예를 들면…….”

“혹시 곤륜파(崑崙派)를 말씀하시려는 겁니까?”

“어, 알아요?”

“네. 이곳 사람이니 당연하게도 잘 압니다. 곤륜에 입문하기에는 제 나이가 너무 많다는 것도요.”

한숨을 푹 내쉰 소년이 말을 이었다.

“그렇다고 흑룡마문(黑龍魔門)에 들어가고 싶지는 않아요. 무림맹에 속해 있다는 건 알지만, 그래도 뿌리는 사파잖아요. 여전히 영 좋지 않은 소문도 있는 것 같고.”

“으음. 그럼 다른 문파들은…….”

“조금씩만 다를 뿐, 결국 상황은 비슷해요. 그럴 바에야 차라리 군문에 들어 병법을 익히고, 언젠가 일군을 이끄는 장군이 되는 것이 그분의 명성에 조금이라도 가까워지는 길이겠죠.”

한바탕 말을 쏟아 낸 소년은 문득 자조 섞인 웃음을 지었다.

생면부지의, 그것도 한참 모자라 보이는 청년에게 이런 말을 해서 무엇 하나 싶은 마음이 들었기 때문이었다.

“이만 가 보겠습니다. 기회가 되면 다음에 또 뵙죠.”

“어어, 잠깐만요.”

청년의 부름에도 소년은 멈추지 않고 털레털레 자리를 떠났다.

그리고 그 뒷모습을 시무룩한 얼굴로 바라보는 청년의 옆으로, 동그란 얼굴이 불쑥 솟아올랐다.

“형, 여기서 뭐하고 있어? 한참 찾았잖아.”

똘망똘망한 눈망울을 한 아이의 모습에, 모자란 형을 찾으러 왔다고 생각한 사람들은 피식피식 웃으며 관심을 껐다.

지금 이 순간, 저 귀여운 아이가 아무에게도 들리지 않는 음산한 목소리를 청년의 귓가에 쑤셔 박고 있다는 사실은 꿈에도 모른 채.

- 말했지. 한 번만 더 말없이 사라지면 검성의 제자고 나발이고 죽여 버린다고.

청년, 청풍이 천진난만하게 대답했다.

- 죄송해요. 금방 다녀오려고 했는데.

- 노부와 전생에 원수라도 졌느냐? 도대체 이러는 이유가 뭐지?

- 이유가 있었어요.

- 말해 봐라.

- 빙당호로가 떨어졌어요.

- 이런 호로새끼를 봤나……!

살성(殺星)의 깊은 탄식을 들으며, 청풍은 멀어지는 소년의 뒷모습을 바라보았다.

그리고 문득 한 사람을 떠올리며, 슬그머니 웃었다.

- 헤헤. 혹시 제가 말한 적 있었나요? 은인이 저 처음 봤을 때 빙당호로를…….

- 닥쳐라. 제발.

청해성에서, 살성은 고통받고 있었다.
```

## Final English reading copy

```markdown
# Chapter 990

The Thunderbolt Saber King, Peng Cheolhu.

The news that yet another giant born of the Great Faction War—the Grand Family Head of the Hebei Peng Family—had fallen spread like a raging wildfire.

“I believed he of all people would hold firm… And yet it’s come to this.”

“Even so, who could’ve imagined the Saber King would meet such a pointless end?”

“Pointless? Don’t ever say that in front of me again. Great Hero Peng held fast to his chivalrous spirit until the very end.”

“Enough. You think he said that because he didn’t know? He’s just heartbroken.”

“I know. Damn it. I know that, too.”

The martial artists who received the unexpected and tragic news could not hide their grief.

To them, the title of one of the Ten Kings carried a meaning unlike any other.

But even Hong Dao, the Dharma King who had earned everyone’s respect.

Even Tang Taesang, the Poison King who had driven countless members of the Demonic Cult to terror.

At last, even the Thunderbolt Saber King—the man who had been the de facto leader of the Ten Kings, apart from the overwhelming presence of the Fire King, Jeok Cheongang—had met his death.

And their deaths had not been from old age or illness.

“Don’t forget. They died honorably, fighting for justice and chivalry to the very end. It’s our duty to avenge them.”

The successive deaths of old masters who had been symbols of the orthodox Murim and paragons of justice.

The martial artists of Murim layered anger over their grief.

To avenge those who had left them.

To defeat the new enemy, which had emerged for the first time since the Demonic Cult and revealed a power more threatening than ever.

“Who will stand against Dark Heaven!”

“Take up your swords! For the Nine Provinces, for justice and chivalry—rise up and fight those fiends!”

The rousing shouts that rang out from streets everywhere had become an everyday occurrence.

Learning from the Murong Family’s example, Sect Leaders and Family Heads of various factions met often and put old grudges behind them. Young people, their blood burning with fervor, swung weapons they had never so much as bloodied until their palms split.

Even a stone leaves a mark when it moves. Imagine how much more so a mountain.

The bloody battle in Shanxi Province, fought across a narrow gorge.

The incident that came to be known as the Eight Heavens Blood Calamity, and the death of the Thunderbolt Saber King, had been the final sparks that set everything ablaze.

Even those who had feared Dark Heaven’s actions—stirring up bloodshed all over the world despite its full strength still being unknown—and martial artists caught between the orthodox and unorthodox factions, who had once been lukewarm about opposing it, now understood.

The razor-sharp blade in Dark Heaven’s hands was aimed not only at the orthodox Murim, but at the entire world.

And the consequences had long since spread far beyond the confines of Murim.

“So, who are you, and where did you come from?”

“I’m Jang-pal, from Jeong Family Village.”

“Jang-pal? You say you’re from Jeong Family Village, so why is your surname Jang?”

“Pardon?”

“Why are you called Jang-pal?”

“Oh, well…”

“Well, what?”

“My father’s from somewhere else.”

“Somewhere else, huh? So he married into the family and settled in Jeong Family Village.”

“Yes, yes. That’s right.”

“How old are you?”

“I’ve come of age this year.”

The low-ranking official assigned to recruit soldiers looked the young man—or rather, the applicant who ought to have been called a boy—up and down.

“Come of age?”

“Yes, sir!”

“I see. Then what is your mother’s full name?”

“What?”

“Listening to you, your face looks kind of familiar. I feel like you might be someone I know. You never know—it could work out well for both of us. If you’re right, I can send you somewhere you’ll have a good chance to earn military merit.”

At the official’s coaxing tone, the boy’s eyes lit up.

“Y-you really mean it?”

“Of course. So, what’s your mother’s name?”

The boy hesitated for a moment, but not for long.

He might not have his family’s permission, but the sense of justice in his heart and his dreams of making his mark on the world had never burned brighter.

If his parents were acquainted with the official in front of him, this was the perfect chance to be posted to a good battlefield, earn brilliant merit, and become a young general.

*Me, too. I’ll definitely become like him.*

He had already made up his mind.

Thinking of the idol he had never once seen in person, the boy found his courage. He gripped the bamboo spear he had clumsily whittled himself and opened his mouth.

“Th-the second daughter of the Oh family from the house by the persimmon tree. She said people nearby would know her…”

“Go home.”

“What?”

“Your father’s a Jeong, your mother’s an Oh, so why do you live in Jeong Family Village?”

“……!”

“What, still got something to say?”

The low-ranking official glared at him with sharp eyes, as if he already knew everything. The boy stiffened, then barely managed to force out a reply.

“Actually, my entire family came from somewhere else…”

“What are you waiting for? Drag this punk out!”

“Gah, sir! No! You can’t! You’ll really regret turning me away!”

The boy’s eyes widened with fierce determination. Deeply moved by the sight, the low-ranking official gave an order to the guards holding the boy by both arms.

“Give him three swats on the rear and toss him out. Come of age, my ass. You little brat—first you lie, and now you’re glaring at your elders?”

“Siiir!”

His desperate cries changed nothing.

Ever since the Emperor’s proclamation had spread throughout the land, government offices in every province had been packed with people who couldn’t resist their dreams of rising in the world and the fire in their veins.

The low-ranking official, who was in danger of dying from overwork before Dark Heaven ever got to him, had reached the end of his rope with boys trying to enlist by lying about their age.

“Give him two more!”

“Nooo!”

“Yes!”

In the end, the guards gave the boy a sound kick to the rear and drove him out. The applicants, whose line stretched all the way outside the government office, watched him go and murmured among themselves.

“He looks younger than my little brother.”

“Still, the kid’s got a decent sense of justice. Shame his head’s a complete rock.”

“But where did he say he was from again?”

“Doesn’t matter. It was obviously made up.”

“No, I still need to know.”

“Why are you so hung up on it?”

“I made mine up, too.”

“……”

“I can’t have the place name overlapping by accident. They’ll catch me, and I’ll end up like him.”

“…How old are you, by the way?”

“Sixteen.”

“Cut the crap. You’ve got the face of a grizzled veteran.”

“Thank you, sir. Looks like I’ll get through safely. And please keep this a secret.”

“……Wait, you weren’t joking?”

Just as everyone was falling into a pit of shock, an applicant with an old-looking face spoke to the boy as he staggered to his feet.

“How old are you?”

The boy, staring blankly at the government office, answered.

“Sixteen.”

“Same age as me. Since we’ve met, let’s drop the formalities.”

“Not even a stray dog would believe that. I’m in a lousy enough mood already.”

“I’m serious.”

“I’m not falling for… that, sir.”

“By the way, where’d you get that spear?”

The boy fidgeted before answering.

“I whittled it myself…”

“People our age usually use swords, don’t they? Like me.”

In an instant, the boy’s complicated expression twisted.

“Who the hell says that? The spear is the king of all weapons.”

“You’re finally talking casually. And I never said swords were the best. I just said they’re what people usually use.”

“Oh.”

“Seeing you get worked up over weapons tells me one thing. You came here because you want to be like ‘that person,’ didn’t you?”

At the knowing question, the boy hesitated for a moment, then answered in a much softer voice.

“Show him some respect.”

“What?”

“Don’t call him ‘that person.’ Speak of him with respect.”

The boy’s dejected look was nowhere to be seen now.

As if nothing had happened, he seemed to have forgotten he’d just been thrown out of the government office. His eyes brightened as he continued.

“Blazing Flame Divine Dragon Jin Taekyung. I’m going to be like him. I mean it!”

Everyone had a goal they wanted to reach.

For the boy, Jin Taekyung was that goal.

A young hero of the martial world, watched by the entire land, and a noble marquis personally appointed by the Son of Heaven.

He admired him. He respected him.

When he’d come here with a proud stride, he’d been full of confidence that before long he’d stand shoulder to shoulder with him.

Of course, reality had kicked him in the rear and thrown him out.

“Damn it.”

The boy lowered his head gloomily.

Then a strange voice suddenly rang out from somewhere.

“Wow! That’s so cool!”

The boy looked up and blinked at the speaker. Everyone waiting outside the government office did the same.

*Who’s that?*

*When did he show up? I don’t think he was here a moment ago.*

*Huh. Or was he?*

*Now that I think about it, maybe he was here the whole time…*

Their exchanged glances were full of bewilderment and questions.

But before anyone could make sense of it, the young man who had suddenly appeared in front of them was smiling brightly at the boy.

“I heard from my grandfa— No, from someone else. They said it’s good to have a goal you want to achieve!”

“Y-yes?”

The boy stared at the young man, bewildered.

Maybe it was the long robe caked in dust. His appearance seemed not just ordinary, but downright shabby.

Perhaps that was why the shock of his sudden appearance and his attempts to strike up a conversation soon gave way to an inexplicable sense of familiarity—not only in the boy, but in everyone else, too.

It was like… like…

Right.

*That one not-quite-right older guy every neighborhood seems to have.*

Everyone thought the same thing at that moment, and couldn’t help but believe it.

Just look at that completely spotless, pure-white smile.

There wasn’t a speck of malice in his eyes. They were clearer than a stream, and then he grabbed the boy’s hand and shook it over and over—the way a little kid might.

“That’s so cool! You want to become the Blazing Flame Divine Dragon! That’s amazing!”

The boy, eyes wide and both arms trapped in the man’s grip, managed to pull himself back to reality thanks to the ache spreading through his shoulders.

“P-please let go.”

“Oh, sorry. I got excited. Did I hurt you?”

They said you couldn’t spit in a smiling face. Looking at that genuinely worried expression, the boy couldn’t bring himself to complain.

“…No, I’m fine. But who exactly are you?”

“I’m just a passing hero. Someone who wants to save the world, like you, Young Hero!”

With his chest puffed out, he proclaimed this proudly. The boy and everyone else reached the same conclusion.

*Yep. Definitely not quite right.*

And, proving their suspicions, the young man kept babbling about whatever came to mind, oblivious to the strange atmosphere.

“But, Young Hero, if you want to become like the Blazing Flame Divine Dragon, why come to the government office? Wouldn’t it be better to go straight to the Jin Family of Taiyuan?”

“Oh, it’s just so far away. I’ve never been more than a hundred li from home in my life. How could I…”

“It’s far, but it’s not that far.”

“It’s not that far? From here in Qinghai to Shanxi?”

“It goes by faster than you’d think. As long as you keep running hard and don’t give up.”

Snickers broke out here and there.

From Qinghai Province to Shanxi Province was nearly ten thousand li, give or take a little exaggeration.

Even old peddlers who roamed the land with a few packs on their backs, and even the major Escort Bureaus, avoided taking on journeys that long whenever possible.

They were that grueling and mind-numbingly dull.

If even people who made their living on the road felt that way, what about the people of Qinghai Province, on the far western edge of the realm?

It was the sort of nonsense only a fool would say.

Of course, to the boy who dreamed so wildly that others laughed at him, it sounded a little different.

“As long as you don’t give up and keep at it?”

“Yep. That’s right! And even if the Jin Family of Taiyuan is too far away, there are other options. For example…”

“Do you mean the Kunlun Sect?”

“Oh, you know about it?”

“Yes. I’m from around here, of course I do. And I know I’m too old to join the Kunlun Sect.”

The boy let out a deep sigh and continued.

“But I don’t want to join the Black Dragon Demon Gate. I know it’s part of the Murim Alliance, but it’s still an unorthodox faction. And it seems like there are still some pretty bad rumors about them.”

“Hmm. Then what about the other sects…”

“They’re all more or less the same, in the end. I might as well join the military, learn strategy, and someday become a general leading an army. That would bring me at least a little closer to his fame.”

After pouring all that out, the boy suddenly let out a self-deprecating laugh.

He wondered what good it did to tell all this to a complete stranger who looked so dim-witted.

“I should get going. Maybe I’ll see you again sometime.”

“Hey, wait a second.”

The boy kept trudging off despite the young man calling after him.

The young man watched him leave with a dejected expression. Then a round face popped up beside him.

“Hyung, what are you doing here? I’ve been looking all over for you.”

People assumed the child with bright, alert eyes had come looking for the not-quite-right older guy. They chuckled and lost interest.

Little did they know that, at that very moment, the adorable child was jamming a sinister voice into the young man’s ear—one nobody else could hear.

—Didn’t I tell you? Disappear without a word one more time and I’ll kill you. I don’t give a damn if you’re the Sword Saint’s Disciple.

Cheongpung answered innocently.

—Sorry. I was only going to be gone for a little while.

—Did you hold a grudge against this old man in a past life or something? Why do you keep doing this?

—I had a reason.

—Then tell me.

—I ran out of candied hawthorn skewers[^1].

—You little shit…!

As he listened to the Slaughter Saint’s deep sigh, Cheongpung watched the boy’s retreating back.

Then he thought of someone and smiled to himself.

—Hehe. Did I ever tell you? When my Benefactor first saw me, the candied hawthorn skewers—

—Shut up. Please.

In Qinghai Province, the Slaughter Saint was suffering.

[^1]: *Bingtanghulu* are fruit skewers coated in hardened sugar, traditionally made with hawthorn berries.
```

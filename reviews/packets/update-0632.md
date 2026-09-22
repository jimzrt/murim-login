<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0632.txt",
      "sha256": "4770f8a5ad476dcb2be284bb3ebaac4a0626849bae53fdec21868ead1b34a5df",
      "bytes": 13567
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "7a1c4a58e00164be87d0ea96648144dc2523c246fa2e5fda9ad18478ab7fcc1c",
      "bytes": 2484
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "8eb26a059c0bb5001f85f9ee69b9f24da92aa67945afca685b34379725ba08b4",
      "bytes": 194286
    },
    {
      "path": "characters/Baeksang.md",
      "sha256": "7d26bcfc2ce29039ba301b1abc493ec0ffd9cc687468a05c33a76d34063ccc36",
      "bytes": 808
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "0e7f819a599ea69516d020c66be98a4504709dbfcc3cd34dc06dfbec50cd6ebd",
      "bytes": 553
    },
    {
      "path": "characters/Heugung.md",
      "sha256": "6d8c16ba773a2a011d3ccabf7dcb1678a1f83e55cab8a06e028573e2dc7a6827",
      "bytes": 623
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "d535be8dba014c914ffa0837e4f0f39c7ccf3e6cc60e35f2028ea15189f65d9d",
      "bytes": 1936
    },
    {
      "path": "characters/Jin Wikyung.md",
      "sha256": "5560d9da56f754bbbb0376e1c3730e0e685a755a843833f4b474b85e823289c9",
      "bytes": 1289
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "80b4f431c5b3200dbb47ea224f0a58fe33d062d01726ace89a30863f40372bef",
      "bytes": 622
    },
    {
      "path": "characters/Namho.md",
      "sha256": "90524d9fdc619df45193773cd9302717ebab530c8a87c5340266422ab639b410",
      "bytes": 843
    },
    {
      "path": "characters/Yayul Cheok.md",
      "sha256": "a8ceaf572141dd6fd5e085cd00a64680e45060091f493879742bea7b5d2239a6",
      "bytes": 912
    },
    {
      "path": "characters/Yayul Mok.md",
      "sha256": "0f95c43ecabcdfdbcfa20c0b5a3584918adcab7bb28a1169523422a9ffba7ef7",
      "bytes": 871
    },
    {
      "path": "characters/Yohi.md",
      "sha256": "5b2228b87806759a3c2049dad97ca4851d23f34b95593387c8eaf197f76ec21d",
      "bytes": 542
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "f3d69e7c0f99c7ed849df9684d1f970bbe205e464d58054504df0c7eff0927f9",
      "bytes": 200627
    }
  ],
  "estimated_tokens": 13181
}
-->

# Durable State Update — Chapter 632

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 632. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 632. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history.
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
  "chapter": 632,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 632,
    "continuity_sources": [632],
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
    "The Fire Dragon Pavilion remains in temporary lodging within the Nanman Beast Palace after being welcomed by Yayul Cheok.",
    "Nanman's first tribal council opposed joining the Murim Alliance; the second council, involving all thirty-two tribes, is tomorrow.",
    "Jin Taekyung is in Nanman to contain a spreading crisis and assess whether Nanman can be persuaded to join the Murim Alliance.",
    "Jin's tiger mask has been privately identified by Yohi and recognized by Baeksang.",
    "Baeksang is the great chieftain of the Bai people and Yayul Cheok's sworn younger brother; he opposes Nanman joining the Murim Alliance and considers the Palace Lord's judgment wrong.",
    "Baeksang bears a burn scar from Jeok Cheongang, whom he encountered while accompanying Yayul Cheok decades ago.",
    "The Miao, Bai, Yi, and Yao peoples are Nanman's four great tribes.",
    "Yohi is the female great chieftain of the Yao people and is pursuing Yao dominance over the four great tribes.",
    "Heugung is the great chieftain of the Yi people and is easily manipulated by Yohi and Baeksang.",
    "Jin has confirmed through Qi Sense that Yohi is fundamentally different from the Southern Heaven Demon Empress.",
    "The Fire Dragon Pavilion has spent two days investigating the Nanman Beast Palace and its surroundings without finding a trace of Dark Heaven.",
    "The Inner Palace has summoned Jin Taekyung on the day before the tribal council."
  ],
  "continuity_sources": [
    631,
    630
  ],
  "open_questions": [
    "What promise did Yohi and Baeksang make, and what does Yohi intend to gain from it?",
    "Why does Baeksang believe Yayul Cheok's judgment was wrong, and can Jin change his position on the alliance?",
    "Is Baeksang's rage at Jin's mention of someone's son connected to Jin Baekyang?",
    "Why has the Inner Palace summoned Jin Taekyung?",
    "Will Nanman's tribal council agree to join the Murim Alliance, and are Dark Heaven's traces absent or merely undiscovered?"
  ],
  "safe_through": 631,
  "temporary_decisions": [
    "Use Baeksang for 백상 and do not treat White Elephant as a separate alias.",
    "Use sworn younger brother for 불알 동생 in the relationship between Yayul Cheok and Baeksang.",
    "Render 화왕손파이 as Fire King hand pie.",
    "Render 풍둔 주둥아리룡 as Wind Style: Mouth Dragon.",
    "Render 초절정 초입 as the early stage of Supreme Peak."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 진위경    | **Jin Wikyung**    |
| 진백양    | **Jin Baekyang**   |
| 화양검    | **Blade of Flowers**          | Jin Baekyang   |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 소림     | **Shaolin**                      |
| 무림맹    | **Murim Alliance**               |
| 암천     | **Dark Heaven**                  |
| 마교     | **Demonic Cult**                                 |                                                       |
| 중원     | **Central Plains**                               |                                                       |
| 장로     | **Elder**                                    |
| 대장로    | **Head Elder**                               |
| 제자     | **Disciple**                                 |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 사천     | **Sichuan**            |
| 항산     | **Mount Heng**         |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 대사      | **Master** for a senior Buddhist monk                           |
| 백상 | **Baeksang** | Great chieftain of the Bai people and Yayul Cheok's sworn younger brother. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 흑웅 | **Heugung** | Great chieftain of the Yi people; his name literally means Black Bear. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 남호 | **Namho** | Hidden Shadow Pavilion code name; literally associated with amber from the south. |
| 야율척 | **Yayul Cheok** | Beast Miao King and lord of the Nanman Beast Palace. |
| 야율목 | **Yayul Mok** | Young Palace Lord of the Nanman Beast Palace. |
| 요희 | **Yohi** | Female great chieftain of the Yao people. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 한족 | **Han Chinese** | Ethnic designation used by the steppe chieftains. |
| 소림사 | **Shaolin Temple** | Temple invoked in Chulwoo’s comparison of Baek Museong’s conduct. |
| 청성파 | **Qingcheng Sect** | Sect named in Baek Museong's comparison about disciplinary rules. |
| 사천당문 | **Sichuan Tang Clan** | Martial clan cited for its poison-based cleansing method. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 북한 | **North Korea** | Country referenced in Taekyung's comparison. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 은영각 | **Hidden Shadow Pavilion** | Former Murim Alliance intelligence organization. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 당문 | **Tang Clan** | Short form for the Sichuan Tang Clan. |
| 아미 | **Emei** | Short form for Emei Sect. |
| 아미파 | **Emei Sect** | Murim sect in Sichuan. |
| 청성 | **Qingcheng** | Short form for Qingcheng Sect. |
| 소림혈사 | **Shaolin Bloodshed** | Past incident cited by Hwangbo Eom. |
| 골골 | **Golgoli** | Jin's nickname for the Skeleton King. |
| 사천혈사 | **Sichuan Blood Tragedy** | Earlier incident in which Taekyung witnessed the strange formation. |
| 남천마후 | **Southern Heaven Demon Empress** | Title Honglan uses when revealing her identity. |
| 야수묘왕 | **Beast Miao King** | Leader of the Miao people and master of the Nanman Beast Palace. |
| 화룡각 | **Fire Dragon Pavilion** | New name chosen for Taekyung's pavilion. |
| 남천 | **South Heaven** | Dark Heaven power that the Lord of Heaven orders the servants to contact. |
| 백족 | **Bai people** | Ethnic group encountered in Yeongin. |
| 백호 | **White Tiger** | Yayul Mok's tiger companion. |
| 내궁 | **Inner Palace** | The inner compound of the Nanman Beast Palace. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진위경 | younger_to_eldest_brother | brother | familiar-but-respectful | Self-corrects from the personal name to kinship: “Jin Wikyung—I mean, my brother?”; 큰형 is eldest brother. |
| 진위경 | 진태경 | eldest_to_youngest_brother | youngest | affectionate-protective | Uses youngest-brother address; openly affectionate beneath a public mask. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 진태경 | 골골 | captor_to_subordinate_undead | Bones | mocking-casual | Jin uses the mocking nickname while treating the Skeleton Warlord like a pet. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 남천마후 | 진태경 | hostile_supernatural_opponent_to_young_martial_artist | Young Great Hero / Child | lighthearted and taunting | Addresses Taekyung while refusing to explain the Gate. |
| 진태경 | 남천마후 | young_martial_artist_to_hostile_demon_empress | you | hostile and determined | Promises that the Southern Heaven Demon Empress will die when they meet again. |
| 진위경 | 남천마후 | family_head_to_hostile_demon_empress | you | formal and defiant | Swears that she cannot touch Taekyung. |
| 골골 | 진태경 | subordinate_undead_to_captor_and_master | human | mocking, reluctant, and familiar | Calls Jin 인간 and 간악한 인간 while complaining about being deceived into searching Area A. |
| 남호 | 진태경 | Hidden_Shadow_Pavilion_agent_to_mission_leader | Jin Taekyung / you | guarded and familiar | Namho addresses Taekyung as 자네 while explaining the contact and offering guidance. |
| 진태경 | 남호 | mission_leader_to_hidden_shadow_agent | you / Namho | probing and respectful | Taekyung questions Namho’s affiliation and later discusses Dark Heaven’s threat to Nanman. |
| 야율목 | 진태경 | Nanman_Beast_Palace_Young_Palace_Lord_to_Han_intruder_and_Murim_Alliance_Pavilion_Master | you | formal but hostile | Asks Jin's identity and orders him to follow after learning he belongs to the Murim Alliance. |
| 진태경 | 야율목 | Fire_Dragon_Pavilion_Pavilion_Master_to_Nanman_Beast_Palace_Young_Palace_Lord | Mok | casual, teasing, and insulting | Calls him rude and later addresses him as 목아 while jokingly claiming they are friends. |
| 야율목 | 야율척 | Young_Palace_Lord_to_Palace_Lord | Palace Lord | ceremonial and deferential | Yayul Mok kneels with his guards and formally greets Yayul Cheok upon his arrival. |
| 야율척 | 야율목 | Palace_Lord_to_Young_Palace_Lord | Mok | authoritative and familiar | Yayul Cheok questions Mok's unannounced departure and later addresses him as 목아 while discussing Nanman's tribes. |
| 야율척 | 진태경 | Nanman_Beast_Palace_Palace_Lord_to_Jeok_Cheongang's_Disciple | you / Disciple of Old Master Jeok / Jin Taekyung | rough, testing, and later welcoming | Yayul Cheok questions Taekyung as a suspected culprit, strikes him as a test, and then welcomes him after recognizing Jeok's Disciple. |
| 진태경 | 야율척 | Fire_Dragon_Pavilion_Pavilion_Master_to_Nanman_Beast_Palace_Palace_Lord | Great Hero Yayul Cheok | formal and deferential | Taekyung gives Yayul Cheok a formal greeting as the nineteenth successor of the Fire Gate Clan. |
| 야율척 | 남호 | Palace_Lord_to_Hidden_Shadow_Pavilion_agent_and_guest | old man | blunt and inquisitive | Yayul Cheok calls on the old man beside Taishan to identify him. |
| 야율목 | 백상 | nephew_to_father's_sworn_younger_brother | Uncle Baeksang | ceremonial and deferential | Yayul Mok formally greets Baeksang as he arrives at the stone door. |
| 백상 | 야율목 | father's_sworn_brother_to_nephew | you | cold and formal | Baeksang questions Yayul Mok about his return, the pasture fire, and the Palace Lord's whereabouts. |
| 야수묘왕 | 백상 | sworn_older_brother_to_sworn_younger_brother | Baeksang | familiar and bittersweet | Yayul Cheok offers Baeksang his preferred fruit wine and asks why he came. |
| 요희 | 흑웅 | Yao great chieftain to Yi great chieftain | big brother | seductive and falsely affectionate | Uses 오라버니 to flatter and manipulate Heugung. |
| 흑웅 | 요희 | Yi great chieftain to Yao great chieftain | my dear | adoring and deferential | Responds to Yohi's manipulation with open infatuation. |
| 요희 | 진태경 | Yao great chieftain to Murim Alliance pavilion master | Jin Taekyung | casual and probing | Identifies him by his full name while allowing him to keep the mask on. |
| 진태경 | 요희 | Fire Dragon Pavilion pavilion master to Yao great chieftain | you | guarded and blunt | Answers Yohi's probing questions directly while warning her about Ju Hwaran. |
| 백상 | 요희 | Bai great chieftain to Yao great chieftain | Yohi | cold and formal | Calls to Yohi from outside the tent at the chapter's end. |
| 백상 | 진태경 | Nanman great chieftain to Murim Alliance Pavilion Head | you bastard | cold, hostile, and contemptuous | Baeksang calls Jin a Han Chinese man, rejects his status, and orders him to leave. |
| 진태경 | 백상 | Murim Alliance Pavilion Head to Nanman great chieftain | you | polite but deliberately provocative | Jin tells Baeksang that Nanman's blood was shed for the world rather than merely for the Central Plains. |

## Listed compact profiles

### Baeksang.md

# Baeksang (백상)

- **Safe through:** Chapter 631
- **Aliases:** None
- **Role:** Baeksang is the middle-aged great chieftain of the Bai people, one of Nanman's four most powerful great tribes.
- **Personality:** Cold, rigid, meticulous, and politically resolute, with a deep but guarded attachment to his sworn elder brother.
- **Voice:** Rigid, formal, restrained, and emotionally distant.
- **Relationships:** Baeksang is Yayul Cheok's sworn younger brother and childhood companion and Yayul Mok's sworn uncle; he lost a beloved son in the Great Faction War, bears a burn scar from Jeok Cheongang after calling him a crazy old man, opposes the Nanman Beast Palace joining the Murim Alliance, and helps Yohi keep Heugung under control.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 631
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Heugung.md

# Heugung (흑웅)

- **Safe through:** Chapter 631
- **Aliases:** None
- **Role:** Heugung is the middle-aged great chieftain of the Yi people, one of Nanman's four great tribes.
- **Personality:** Heugung is foolish, easily flattered, and politically dependent on stronger personalities despite leading a powerful tribe.
- **Voice:** Heugung speaks with warm enthusiasm and exaggerated devotion toward Yohi.
- **Relationships:** Yohi and Baeksang keep Heugung under their control, while Heugung responds to Yohi's manipulation with apparent infatuation.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 630
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple, the Fire Gate Clan's nineteenth successor, and the Pavilion Master of the Fire Dragon Pavilion within the Murim Alliance; he is a Supreme Peak master with the Heavenly Martial Physique and Force, publicly recognized as an S-rank-level Hunter while formally retaining an A-rank license, and he has completed an unnamed cultivation technique designed for even the lowest-rank Hunter to learn without making it easily abusable.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jin Wikyung.md

# Jin Wikyung (진위경)

- **Safe through:** Chapter 548
- **Aliases:** Junzi Sword
- **Role:** Jin Wikyung is the thirty-six-year-old Lesser Family Head and future Family Head of the Jin Family of Taiyuan, the Alliance Leader who unified Shanxi Murim and Shanxi Province's foremost landowner and magnate.
- **Personality:** Calm, authoritative, and politically capable in public; protective and affectionate toward Taekyung beneath a stern mask. Takes responsibility for his people, acts decisively under pressure, and prioritizes family survival.
- **Voice:** Restrained, formal, and commanding with subordinates; openly affectionate, proud, and occasionally exuberant with Taekyung.
- **Relationships:** Jin Wikyung is Taekyung's eldest brother and future Family Head who protects and mentors him, commands Wipeng and the Jin Family's forces, has worked with Jeok Cheongang, maintains a political connection with Hongcheon, Prince Shangshan's hidden loyal retainer, and wants Taekyung to tell him his untold stories when the current crisis is over; Jin Mukyung is his younger brother and a potential successor alongside Taekyung.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 630
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Namho.md

# Namho (남호)

- **Safe through:** Chapter 629
- **Aliases:** Elder Chao
- **Role:** Namho is an eighty-year-old non-Han Hidden Shadow Pavilion agent who spent more than fifty years operating under the cover of the Poison Flower Pavilion in Nanman and now serves as the Fire Dragon Pavilion’s guide.
- **Personality:** Duty-bound, pragmatic, observant, and willing to use theatrical violence and crude insults to protect an intelligence operation.
- **Voice:** Measured and serious in private, but loudly abusive and convincing when maintaining his local cover.
- **Relationships:** Namho is a Hidden Shadow Pavilion contact for Jin Taekyung and the Fire Dragon Pavilion, receives intelligence from the Pavilion Master, and knows the code used by the Thousand-Faced Fox.

### Yayul Cheok.md

# Yayul Cheok (야율척)

- **Safe through:** Chapter 628
- **Aliases:** Beast Miao King
- **Role:** Yayul Cheok is the over-eighty Beast Miao King, lord of the Nanman Beast Palace, a Supreme Peak master among the Ten Kings, and great chieftain representing the Miao people.
- **Personality:** Boisterous, warmhearted, forthright, playful, and politically conscious of the tribal coalition he leads.
- **Voice:** Rough, loud, convivial, and teasing, becoming authoritative when discussing Nanman's laws or political decisions.
- **Relationships:** Jeok Cheongang is an old acquaintance whom he respects; Baeksang is his sworn younger brother and childhood companion, and they fought together during the Great Faction War; Yayul Mok serves as his Young Palace Lord; Jin Taekyung is Jeok's Disciple whom he welcomes into the Nanman Beast Palace.

### Yayul Mok.md

# Yayul Mok (야율목)

- **Safe through:** Chapter 631
- **Aliases:** None
- **Role:** Yayul Mok is the non-Han Young Palace Lord of the Nanman Beast Palace, a spear-wielding warrior who rides a white tiger, and a halting but capable speaker of Han Chinese.
- **Personality:** Protective of Nanman Beast Palace livestock, quick-tempered toward trespassers, and capable of restraint once he recognizes legitimate authority.
- **Voice:** Blunt, commanding, and formal-polite toward strangers, becoming openly insulting when provoked.
- **Relationships:** Yayul Cheok is the Beast Miao King and Yayul Mok's father; Yayul Mok is his only surviving son after three older siblings died in the Great Faction War, Baeksang is his father's sworn younger brother, and his white tiger is a long-bonded companion.

### Yohi.md

# Yohi (요희)

- **Safe through:** Chapter 631
- **Aliases:** None
- **Role:** Yohi is the female great chieftain of the Yao people, one of Nanman's four great tribes.
- **Personality:** Yohi's public presence is charismatic and captivating, drawing widespread admiration and affection.
- **Voice:** Not established.
- **Relationships:** Yohi leads the Yao people, seeks to unite Nanman's four great tribes under Yao leadership, and manipulates Heugung alongside Baeksang.

## Korean source

```text
＃632화



내궁(內宮).

현재 머무르고 있는 처소도 내궁에 속한 곳이지만, 야율목이 말하고자 하는 뜻이 그게 아니라는 것쯤은 곧장 알아차릴 수 있었다.

“야율 대협이 우리를?”

“그래. 정확히는 너와 그 노인만 데려오라 이르셨다.”

좋은 소식이다. 그간 묵묵부답으로 일관하던 야수묘왕이 마침내 내 독대 요청에 응했다는 거니까.

하지만 화룡각 전체도 아니고 나와 남호, 단 두 사람만 콕 집어 부르다니.

그 순간 의문과 함께 뇌리를 스쳐 지나가는 어떤 생각에, 나는 문득 입을 열었다.

“다른 사람의 이목을 피해야 하나?”

의외라는 표정으로 나를 빤히 바라보던 야율목이 작게 고개를 끄덕인다.

“생각보다 눈치가 빠르군. 가급적이면 눈에 띄지 않게 움직여야 한다.”

“바로 내일이 부족 대회의니까?”

“아니, 대부분의 부족장들이 너희를 싫어하니까.”

“…….”

“사실이다.”

혹시 전생에 기요틴이었나. 뒤에 나올 말까지 싹둑 잘라 내는 것 보소.

그래도 부정할 수 없는 사실이라 나는 씁쓸하게 입맛을 다셨다.

“대충 사정은 알겠네. 야율 대협도 이곳저곳에서 압박을 받고 있는 모양이지?”

뭐라 말할 것처럼 입술을 달싹이던 야율목이 이내 굳은 얼굴로 입을 다문다.

내가 앞서 들었던 말을 부정하지 못했듯이, 녀석도 마찬가지였다.

하지만 인정할 건 인정해야 하는 법.

남만은 중원인들의 편견처럼 야만스러운 땅이 아니며, 야수묘왕은 왕이 아니라 그들을 대표하는 대족장 중 한 사람일 뿐이었다.

‘나도 아는 사실을, 이 녀석이 모를 리는 없지.’

야율목은 나름대로 괜찮은 녀석이지만 아직 치기(稚氣)를 완전히 벗지 못한 청년이기도 하다.

그리고 그때, 자존심이 상한 표정으로 입을 꾹 다물고 있던 야율목이 작게 중얼거렸다.

“네놈의 말이 맞다. 제아무리 아버님이라 해도, 홀로 그들을 감당하시는 건 무리야.”

“……?”

“뭐냐, 그 표정은?”

“아니, 그냥 의외라서. 이렇게 솔직하게 말할 줄은 몰랐지. 그새 철 좀 들었구나?”

이틀 전 나누었던 대화로 뭔가 깨달은 게 있나?

그러고 보면 여전히 사춘기 중학생처럼 틱틱거리긴 해도 꼬박꼬박 멧돼지도 직접 잡아다 주는 등, 야율목은 처음보다는 훨씬 호의적인 태도를 보였다.

‘그렇다면 좋은 일이지. 이 넓은 땅덩어리에 우리 편이 좁쌀만큼이라는 게 문제지만.’

나는 발끈한 얼굴을 한 야율목보다 한발 빨리 입을 열었다.

“시간과 장소는?”

“인시(寅時). 그때 데리러 오지.”

“좋아. 아, 그리고 기왕 오는 김에…….”

“오는 김에. 뭐?”

“사슴이나 노루 좀 잡아 와. 멧돼지 말고.”

“……!”



* * *



무림에서의 하루는 열두 시진으로 나뉘고, 한 시진은 두 시간을 뜻하며 인시는 새벽 세 시부터 다섯 시까지의 시각을 의미한다.

그리고 야율목은 약속을 지켰다. 모두가 깊은 잠에 빠진 새벽, 전신이 새하얀 털로 뒤덮인 백호 한 마리가 어둠을 가르고 처소 앞에 내려앉았다.

쿵.

낯익은 모습으로 죽어 있는 한 마리의 짐승도 함께.

“시벌, 또 멧돼지네. 너 일부러 이러지?”

“오다 주웠다.”

“자꾸 줍긴 뭘 주워. 혹시 멧돼지 밭이라도 있냐? 물만 주면서 쑥쑥 키우다가 서리해 와?”

남호가 어리둥절한 표정으로 물었다.

“서리가 뭔가? 난생처음 들어보는데.”

“그런 게 있어요. 남 노인한테는 난생처음이 아니라, 어차피 이번 생에는 두 번 다시 못 들어볼 겁니다.”

“역시 한족 놈이라 그런지 말하는 꼬락서니가…….”

“한족 혐오를 멈춰 주세요.”

언짢은 목소리로 투덜거리는 남호에게 정중한 중단 요청을 넣은 내게, 야율목이 자신의 뒷자리를 턱짓했다.

“타라.”

“이 호랑이를?”

“……그럼 내가 목말이라도 태워 줘야 하나?”

“성깔 있어 보이는데.”

“편견이다. 새끼 때부터 함께한 녀석이라 순하기 그지없지. 정 못 믿겠으면 시험해 보든가.”

“오. 그래?”

나는 백호의 턱을 쓰다듬기 위해 손을 뻗었……다가 번개처럼 뒤로 뺐다.

딱!

크고 날카로운 이빨이 허공을 갈랐다. 떨떠름한 얼굴로 대답을 요구하는 내 눈빛에, 야율목이 작게 입맛을 다셨다.

“아쉽군.”

“시벌놈이.”

“못 믿겠으면 시험해 보라고 했지. 안 문다는 말은 안 했다.”

개도 안 믿을 헛소리를 지껄인 야율목이 백호의 미간을 살살 긁었다.

“야호. 야호야. 성내지 말거라.”

갑자기 저러길래 처음에는 북한산 등산객 코스프레인 줄 알았는데, 문득 머릿속에 떠오르는 생각이 있었다.

“그거 설마 저 녀석 이름이냐?”

야율목이 당당하게 고개를 끄덕였다.

“무야호(武野虎). 굳센 벌판의 호랑이라는 뜻이다.”

“…….”

“참으로 멋있는 이름이지. 그렇지 않나?”

그릉. 그르릉.

꼴에 자기도 고양이과라고, 골골송을 부르는 백호를 귀여워 죽겠다는 눈빛으로 바라본 야율목이 자랑스럽게 말을 이었다.

“그만큼 기분이 좋다는 거다. 이제 올라타도 좋아.”

“……아, 으응.”

“표정이 왜 그러지? 무슨 문제라도 있나?”

있지. 나만 알고 있는 약간의 문제가. 근데 여기서는 말 못 하지.

목구멍까지 차오른 말을 삼킨 나는 잠자코 백호의 등에 올라탔고, 이어 약간 상기된 얼굴을 한 남호가 그 뒤를 이었다.

“내가 이 나이에 전사들에게만 허락된다는 호랑이를 타 볼 줄이야. 그것도 신령스러운 백호를!”

원래 이 세상에 내 새끼 칭찬만큼 기쁜 게 없다. 야호맘 야율목이 뿌듯한 표정으로 고개를 끄덕였다.

“역시 노인장께서 뭘 아시는군. 백호를 좋아하시오?”

“아, 그럼. 내가 평소에도 많이 좋아하지.”

“…….”

아냐, 그만해. 거기까지 하는 건 무리수야.

기대 반, 우려 반으로 뒤이어 나올 대사를 기다리던 그때.

사람 셋을 태우고도 아무렇지 않게 기지개를 쭉 켠 백호가 지면을 박차고 달려나갔다.

파파팟!

그렇게 밝은 달빛 아래. 어두운 밀림을 빛살처럼 가로지르던 삼인일호(三人一虎)의 걸음이 멈춘 곳은 무너져 가는 낡은 사당이었다.



* * *



사당 안의 공기는 습식 사우나 안처럼 후텁지근했다.

먼지가 쌓인 바닥과 벌레가 좀 먹은 기둥, 금방이라도 꺼질 것처럼 휘청이는 호롱불은 내부를 흐릿하게 밝히고 있었다.

그리고 그 모든 것의 중심에, 우리를 기다리고 있던 한 사람이 있었다.

“오랜만에 와 보니 엉망이더군. 하긴, 그때도 영 좋은 상태는 아니었지.”

처음 만났을 때와 달리, 낮은 뇌까림과 함께 돌아선 야수묘왕 야율척의 표정은 호롱불의 불빛처럼 흐릿했고, 그 안에는 숨길 수 없는 피로가 엿보였다.

그런 이유에서였을까. 나를 포함한 그 누구도 묻지 않았다. 왜 내궁의 대전(大殿)이 아닌 낡은 사당에서 우리를 만나는지에 대해서.

그 대신 나는, 두서없는 그의 말을 받아 주는 것을 택했다.

“언제를 말씀하시는 겁니까?”

“젊었을 때지. 아니, 젊다 못해 어렸던 시절이었어. 도저히 수습할 수 없는 대형 사고를 친 날이면, 우리는 늘 어른들을 피해 이곳에 숨어 있었다.”

“우리라면…….”

“너도 이미 만난 적 있는 자다. 이미 짐작하고 있겠지만.”

“백상(白象)이군요. 백족의 대족장.”

야수묘왕이 고개를 끄덕였다.

“맞다. 바로 그다.”

“오랜 시간을 함께했다는 건 알고 있습니다.”

“오랜 시간이라는 표현으로도 부족하다. 그야말로 일평생을 함께 했으니. 목초지에서, 늪에서, 산과 들. 그리고 전장에서까지도 우리는 함께였다.”

잠시 그때를 생각하는 듯, 흔들리는 호롱불을 말없이 응시하던 야수묘왕이 작게 고개를 끄덕였다.

“그래. 그렇고말고.”

“두 분이고 떼 놓을 수 없는 죽마고우이자 의형제라고 들었습니다.”

불쑥 내뱉은 말에 야수묘왕의 시선이 내게 옮겨 간다. 나는 그의 눈을 똑바로 바라보며 말을 이었다.

“그런데, 지금도 그렇습니까?”

“음.”

“……진태경. 입조심해라.”

크르릉.

웅크리고 있던 백호가 낮은 울음소리를 토해 낸다.

나직한 경고와 함께 앞으로 나선 자신의 아들을 향해, 작게 손을 내저어 보인 야수묘왕이 나를 물끄러미 응시했다.

“아니라고 생각하느냐?”

“그냥 문득 그런 생각이 들었습니다. 백상 대족장의 생각은 궁주님과 다를 것 같다는 생각이.”

“…….”

“얼마나 자세히 아시는지는 모르겠지만, 지금 중원에서는 별의별 일이 다 일어나고 있습니다. 그중에서도 첫 시작은 저희 태원진가가 있는 산서성이었고요.”

지금까지도 생생한 기억이다.

소림혈사, 사천혈사 등의 굵직한 사건에 의해 가려져 있지만, 암천이라는 이름이 처음 중원에 모습을 등장한 것은 바로 산서성에서였다.

항산검문과 대장로를 조종하여 전쟁을 벌였고, 자그마치 일천에 달하는 사람들이 목숨을 잃어야만 했다.

‘은영각에서 정보를 전달받았다면, 모를 수가 없겠지.’

그리고 내 생각을 읽은 것처럼 야수묘왕은 고개를 끄덕였다.

“이미 들어서 알고 있다. 화양검 진백양과는 일면식도 나눈 사이였고.”

“그 누구도 예상치 못했습니다. 가문에 속하지 않은 외인(外人)이라면 모를까. 대장로는 피로 이어진 혈육이자 태원진가의 큰 어른이었으니까요.”

그건 진위경이 대장로를 경계하면서도 끝까지 믿었던 이유이기도 했고, 야수묘왕은 내 말의 의미를 알아차리지 못할 만큼 둔감한 사내가 아니었다.

“백상은…… 아니다. 그럴 리 없다. 그는 화양검과 달라.”

“그건 누구도 모릅니다.”

단호한 내 대답에 이어, 묵묵히 상황을 지켜보던 남호가 불쑥 입을 열었다.

“오래전 혈육처럼 아끼던 수하가 있었소. 그는 몰락한 무가(武家)의 유일한 후손이었고, 부모는 마교에 의해 살해당했지. 훗날 서쪽에서 십만 마도라는 들불이 일어나자 그는 무림맹에 투신했소. 늘 죽음을 두려워하지 않고 작전에 임했기에 그가 가져온 정보들로 십여 차례의 작은 승리를 가져올 수 있었지.”

나조차도 들은 적 없던, 세상에 알려지지 않은 어느 은영각 요원의 이야기다.

그러나 남호의 어두운 표정처럼, 곧이어 이어진 말들도 그러했다.

“일이 벌어진 후에도 믿을 수 없었소. 그가 배신자라는 것을. 어느 날 그가 팔 하나와 바꿔 가져온 정보가, 오천여 명의 맹원(盟員)을 사지로 내몰리라는 것을.”

“……!”

“모든 게 밝혀지자 그는 도주했소. 그리고 나는 며칠 뒤 척살조가 가져온 한 사람의 목을 볼 수 있었지. 뭐가 그리 기뻤는지 한껏 웃고 있더군.”

목소리가 흩어진 자리에 고요함이 찾아왔다. 남호가 깊은 한숨과 함께 재차 입을 열었다.

“이 늙은이의 말은 백족의 대족장이 암천의 주구라는 뜻이 아니외다. 하지만 이토록 한 치 앞도 알 수 없는 곳이 무림이오. 백상. 요희. 흑웅. 혹은 내일 한자리에 모일 서른두 명의 부족장 중 한 사람이 배신자로 밝혀져도 놀랍지 않지.”

야수묘왕은 대답하지 않았다. 아주 오랫동안.

휘청이고 바로 서기를 반복하는 호롱불만 말없이 응시하던 그가 문득 나를 향해 고개를 돌렸다.

“확신하느냐?”

내가 대답했다.

“적어도 한 가지만큼은 확신합니다.”

“그것이 무엇이냐.”

“남천마후(南天魔后). 그 썅년이 남만을 곱게 놔두지 않을 거라는 겁니다.”

작게 침음성을 흘린 야수묘왕이 입을 열었다.

“남만은 결코 녹록치 않다.”

“그럼 사천당문과 소림사, 아미파와 청성파는 존나 녹록한 좆밥이라서 당한 겁니까?”

“……!”

“어, 죄송합니다. 말이 심했네요.”

내 급발진에 헛웃음을 흘린 야수묘왕이 대답했다.

“역시 적 노의 제자답군.”

“들으면 기분 나빠하실 겁니다.”

“내심 좋아하실 거다.”

“……오.”

적잘알 인정.

내가 야수묘왕을 향해 내심 엄지를 치켜세우던 그때.

후우웅, 쉭!

사당 밖에서 거친 인기척과 함께, 한껏 숨죽인 목소리가 들려왔다.

“구. 궁주님!”

동시에 머릿속의 붉은 경고등이 켜졌다.

시스템 알림과 함께.

띠링.
```

## Final English reading copy

```markdown
# Chapter 632

The Inner Palace.

Our current quarters were also part of the Inner Palace, but it didn’t take me long to realize that wasn’t what Yayul Mok meant.

“Great Hero Yayul is summoning us?”

“That’s right. More precisely, he ordered me to bring only you and that old man.”

That was good news. It meant the Beast Miao King, who had remained silent all this time, had finally agreed to my request for a private audience.

But why summon only Namho and me instead of the entire Fire Dragon Pavilion?

A thought flashed through my mind along with the question, and I suddenly opened my mouth.

“Do we need to avoid other people’s eyes?”

Yayul Mok stared at me with an expression of surprise, then gave a small nod.

“You’re quicker on the uptake than I expected. We should move without attracting attention if possible.”

“Because the tribal council is tomorrow?”

“No. Because most of the tribal chiefs hate all of you.”

“……”

“It’s a fact.”

*Was he a guillotine in his previous life? Look at him chopping off even the words that were about to come next.*

Still, it was an undeniable fact, so I clicked my tongue bitterly.

“I more or less understand the situation. Great Hero Yayul is under pressure from all sides too, isn’t he?”

Yayul Mok’s lips parted as though he was about to say something, but he soon closed his mouth with a hardened expression.

Just as I couldn’t deny what I had heard earlier, neither could he.

But there were some things one had to acknowledge.

Nanman was not the barbaric land the people of the Central Plains imagined it to be, and the Beast Miao King was not their king, but merely one of the great chieftains representing them.

*There’s no way this guy doesn’t know something I already do.*

Yayul Mok was a decent enough young man in his own way, but he was still a youth who hadn’t completely shed his immaturity.

And then, with his lips tightly pressed together in a wounded expression of pride, Yayul Mok muttered,

“You’re right. No matter how capable my father is, it’s impossible for him to handle all of them alone.”

“……?”

“What’s with that look?”

“Nothing. I’m just surprised. I didn’t expect you to admit it so honestly. You’ve matured a little in the meantime, huh?”

*Had he realized something after our conversation two days ago?*

Come to think of it, even though he still snapped at me like a middle-schooler going through puberty, Yayul Mok had become much friendlier than he was at first. He even brought us wild boar himself on a regular basis.

*That’s a good thing. The problem is that in this enormous land, our side is no bigger than a grain of millet.*

I opened my mouth a moment before Yayul Mok could glare at me.

“When and where?”

“Insi. I’ll come to get you then.”

“Good. Oh, and while you’re coming…”

“While I’m coming? What?”

“Bring us some venison or roe deer. Anything but wild boar.”

“……!”

* * *

A day in the Murim was divided into twelve shichen, and each shichen meant two hours. Insi referred to the period from three to five in the morning.

And Yayul Mok kept his promise.

In the dead of night, while everyone was deep asleep, a White Tiger covered from head to toe in pure white fur tore through the darkness and landed in front of our quarters.

*Thump.*

A familiar-looking beast lay dead beside him.

“Fuck, it’s another wild boar. Are you doing this on purpose?”

“I found it on the way here.”

“You keep finding them. What, do you have a wild-boar farm somewhere? Do you water them, let them grow nice and big, then sneak over and steal them?”

Namho asked with a bewildered expression.

“What is *seori*? I’ve never heard that word before.”

“It’s a thing. And for you, Old Man Namho, this will be the first and last time you ever hear it in this lifetime.”

“So that’s how you Han Chinese talk…”

“Please stop hating the Han Chinese.”

After politely requesting that Namho stop grumbling in displeasure, I received a gesture from Yayul Mok toward the space behind him.

“Get on.”

“On this tiger?”

“……Do I need to carry you on my shoulders, then?”

“He looks like he has a nasty temper.”

“That’s prejudice. I’ve been with him since he was a cub, so he’s as gentle as can be. If you don’t believe me, test him.”

“Oh. Really?”

I reached out to stroke the White Tiger’s chin, then yanked my hand back like lightning.

*Clack!*

Its large, sharp teeth snapped shut through empty air.

At the demanding look in my eyes, Yayul Mok clicked his tongue softly.

“What a shame.”

“You bastard.”

“I told you to test him if you didn’t believe me. I never said he wouldn’t bite.”

After spouting nonsense that even a dog wouldn’t believe, Yayul Mok gently scratched the White Tiger between the eyes.

“Yaho. Yaho, my boy. Don’t be angry.”

At first, I thought he was cosplaying a North Korean mountain hiker. But then, a thought suddenly occurred to me.

“Don’t tell me that’s his name.”

Yayul Mok proudly nodded.

“Muyaho (武野虎).[^1] It means ‘tiger of the mighty wilds.’”

[^1]: “Muyaho” echoes a Korean meme catchphrase and also resembles *yaho*, a shout traditionally made in the mountains.

“……”

“It’s a truly magnificent name, isn’t it?”

*Grrrrr. Prrrrr.*

The White Tiger purred as though it, too, was proud to be part of the feline family. Yayul Mok looked ready to die of cuteness and continued proudly.

“That means he’s in a very good mood. You may get on now.”

“……Ah. Yeah.”

“Why do you look like that? Is something wrong?”

*There is. A small problem that only I know about. But I can’t say anything here.*

I swallowed the words that had risen to my throat, silently climbed onto the White Tiger’s back, and Namho followed with a slightly flushed face.

“To think I’d ride a tiger at my age, an animal supposedly reserved for warriors. And a sacred White Tiger at that!”

Nothing in this world makes you happier than hearing someone praise your child. Yaho-mom Yayul Mok nodded proudly.

“You know what you’re talking about, old man. Do you like White Tigers?”

“Of course. I’ve always been very fond of them.”[^2]

[^2]: In Korean slang, “White Tiger” can also refer to a woman with little or no pubic hair, giving Namho’s answer an unintended sexual double meaning.

“……”

*No. Stop. Don’t take it any further. That would be a terrible move.*

Just as I waited for the next line with equal parts anticipation and dread, the White Tiger stretched leisurely, seemingly unaffected by carrying three people, then kicked off the ground and raced away.

*Papat!*

Beneath the bright moonlight, the three people riding one tiger crossed the dark jungle like a streak of light.

They stopped in front of an old shrine that was slowly collapsing.

* * *

The air inside the shrine was as hot and humid as a steam sauna.

Dust covered the floor, insects had eaten through the pillars, and an oil lamp swayed as though it might go out at any moment, casting a faint light over the interior.

And at the center of it all stood one person waiting for us.

“When I came back after all this time, the place was a complete mess. Then again, it wasn’t in particularly good shape back then either.”

Unlike when I had first met him, the expression on the Beast Miao King Yayul Cheok’s face as he turned around with a low mutter was as indistinct as the oil lamp’s light. In it, I could see unmistakable fatigue.

Perhaps for that reason, no one, myself included, asked why he had chosen to meet us in this old shrine instead of the Inner Palace’s main hall.

Instead, I chose to respond to his disjointed words.

“When are you talking about?”

“When I was young. No, I was even younger than that. Whenever we caused some huge disaster we couldn’t possibly clean up, we would hide here to avoid the adults.”

“When you say ‘we’…”

“You’ve already met him. Though I’m sure you’ve already guessed.”

“Baeksang. The great chieftain of the Bai people.”

The Beast Miao King nodded.

“That’s right. Exactly him.”

“I know the two of you have been together for a long time.”

“Even ‘a long time’ isn’t enough to describe it. We spent our entire lives together. In the grasslands, the swamps, the mountains and fields, and even on the battlefield—we were always together.”

As though remembering those days, the Beast Miao King silently stared at the swaying oil lamp for a moment, then gave a small nod.

“Yes. That’s right.”

“I heard the two of you were inseparable childhood friends and sworn brothers.”

At my sudden words, the Beast Miao King’s gaze shifted to me. I met his eyes directly and continued.

“But are you still like that now?”

“Hmm.”

“……Jin Taekyung. Watch your mouth.”

“Grrrr.”

The White Tiger, which had been crouching nearby, let out a low growl.

The Beast Miao King made a small waving gesture toward his son, who had stepped forward with a quiet warning, then stared at me.

“Do you think we aren’t?”

“I just had a thought. I thought Great Chieftain Baeksang might have a different opinion from you, Palace Lord.”

“……”

“I don’t know how much detail you’ve heard, but all sorts of things are happening in the Central Plains right now. And the first of them began in Shanxi Province, where my Jin Family of Taiyuan is located.”

I still remembered it vividly.

The Shaolin Bloodshed and the Sichuan Blood Tragedy had overshadowed it, but the first time the name Dark Heaven appeared in the Central Plains was in Shanxi Province.

They manipulated the Mount Heng Sword Sect and its Head Elder into starting a war, and no fewer than a thousand people had to lose their lives.

*If he received information from the Hidden Shadow Pavilion, there’s no way he wouldn’t know.*

As though he had read my thoughts, the Beast Miao King nodded.

“I’ve already heard about it. I had even met Blade of Flowers Jin Baekyang before.”

“No one could have predicted it. If he had been an outsider with no ties to the family, perhaps. But the Head Elder was blood kin and the senior elder of the Jin Family of Taiyuan.”

That was why Jin Wikyung had continued to trust the Head Elder to the end even while remaining wary of him, and the Beast Miao King was not dull enough to miss the meaning behind my words.

“Baeksang… No. It can’t be. He’s different from the Blade of Flowers.”

“No one can know that.”

After my firm answer, Namho, who had been silently watching the situation, suddenly spoke.

“I once had a subordinate I cherished like blood kin. He was the sole descendant of a fallen martial family, and his parents had been killed by the Demonic Cult. Later, when the hundred-thousand-strong Demonic Path rose like wildfire in the west, he joined the Murim Alliance. He never feared death when carrying out missions, and the information he brought us led to more than ten minor victories.”

It was the story of a Hidden Shadow Pavilion agent unknown to the world—someone whose existence even I had never heard about.

But just like Namho’s dark expression, the words that followed were no brighter.

“Even after it happened, I couldn’t believe it. I couldn’t believe he was a traitor. One day, the information he brought back at the cost of one arm drove more than five thousand Alliance members to their deaths.”

“……!”

“When everything was revealed, he fled. And several days later, I saw the head of a man brought back by the assassination squad. He was grinning from ear to ear, as though something had made him terribly happy.”

Silence settled over the place where his voice had faded. Namho let out a deep sigh, then spoke again.

“I am not saying that the great chieftain of the Bai people is a minion of Dark Heaven. But this is the Murim, a place where you cannot see even an inch ahead. Baeksang, Yohi, Heugung—or even one of the thirty-two tribal chiefs gathering here tomorrow—none of it would surprise me if one of them turned out to be a traitor.”

The Beast Miao King did not answer.

For a very long time.

He merely stared at the oil lamp as it swayed and righted itself again and again, then suddenly turned his head toward me.

“Are you certain?”

I answered.

“At least one thing.”

“What is that?”

“The Southern Heaven Demon Empress. That fucking bitch won’t leave Nanman alone.”

The Beast Miao King let out a low groan before opening his mouth.

“Nanman is not an easy target.”

“Then were the Sichuan Tang Clan, Shaolin Temple, Emei Sect, and Qingcheng Sect attacked because they were easy fucking pushovers?”

“……!”

“Oh, sorry. I went too far.”

The Beast Miao King let out a hollow laugh at my sudden outburst before answering.

“You really are Old Master Jeok’s Disciple.”

“He’d be offended if he heard that.”

“He’d secretly love it.”

“……Oh.”

*Okay, he really knows Old Man Jeok.*

Just as I was silently giving the Beast Miao King a thumbs-up, a rough disturbance came from outside the shrine.

*Whoosh, hiss!*

Then a voice, held as low as possible, reached us.

“P-Palace Lord!”

At the same time, a red warning light flashed in my mind.

Along with a System alert.

> **System**
>
> *Ding.*
```

<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1180.txt",
      "sha256": "45fcd3ff40e68a2e0ad6ab62e4c716ccc4ba13f9eef1009aff9ff8edcf5ca1b0",
      "bytes": 12801
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "d3c81be599795ec256dc9a687b9cb81da09c9da8be197ad881cd25bfcf4bf5c4",
      "bytes": 1994
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "6bd67da46d2a4fea774ad7ef64f30f16a650b1c6d85bd1a995fc818ad294b01a",
      "bytes": 248538
    },
    {
      "path": "characters/Cang Gong.md",
      "sha256": "fd60b79eabcd570d62aad1bb247a2e762bed40ee1463332ca9d1a0658f054528",
      "bytes": 779
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "d0807ba61214f1605eb879919eb4650339f700dfbf610076b3cca7585056b0e7",
      "bytes": 1230
    },
    {
      "path": "characters/Jin Mukyung.md",
      "sha256": "6e1680c933d512508e0c2aec2567a90b980200157e9ac3dfe684b11c0a1994ae",
      "bytes": 1665
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "ffa08779b029b86bc6ade279a7a2f9ebd9b553e79fc5b1f5f54f90cfe3d22426",
      "bytes": 1550
    },
    {
      "path": "characters/Jin Wikyung.md",
      "sha256": "923c364ccc79eb656ebd0eaa590cc4b240e1e30cdc098474dccc69bb94443aa0",
      "bytes": 1179
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "f0e3c41506f8ed30ef7fd30a7956fcbe07f978265589133ade29ef7805219f58",
      "bytes": 623
    },
    {
      "path": "characters/Mae Jonghak.md",
      "sha256": "2a4924c43dc8f0e10b4986cfe815a07fbbce136ea9d6ca019f942c8e87161668",
      "bytes": 1084
    },
    {
      "path": "characters/Murong Yeonghwi.md",
      "sha256": "2818a4833e7c3eb9356bf7bb524a1af0798ac4b45129d6cc6eba49750b1cc103",
      "bytes": 527
    },
    {
      "path": "characters/Song Ho.md",
      "sha256": "d7007c4825134fd76488a4382e2914ea094a396509255778d0f1ef97bd56d664",
      "bytes": 768
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "603e3c49f5d38d12148c65f30dba06292ea6e50bd93d8155390005ac0494757a",
      "bytes": 295700
    }
  ],
  "estimated_tokens": 12777
}
-->

# Durable State Update — Chapter 1180

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
1 and safe_through 1180. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1180. Profile updates may replace only one
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
  "chapter": 1180,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1180,
    "continuity_sources": [1180],
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
    "Taekyung and his group are crossing the Taklamakan Desert in Xinjiang, where the land appears to contain no living things.",
    "Jeok Cheongang, the Slaughter Saint, Hyuk Mujin, Cheongpung, and Ju Hwaran know Taekyung comes from the realm of immortals; he has said he is human and around twenty-eight.",
    "Great Sir has not been told Taekyung’s secret; Jeok leaves that decision to Taekyung.",
    "Bow Saint knows Taekyung’s secret and questions whether the Martial God’s letter is truly right.",
    "The Lord of Heaven has awakened and regained greater strength; the process is not complete, but the Lord of Heaven says it will be.",
    "The Grand Mage serves the Lord of Heaven and awaits a command; none has been given.",
    "The Main Quest “Rift and Collapse” failed; “The Foreordained Collapse” warns that player choices can cause irreversible consequences.",
    "Cheon Taemin remains unconscious in a secret facility beneath the Pentagon; Jin knows he is the Martial God and a former Player.",
    "An alert reported that Alpha had awakened; what Alpha is and what its awakening means remain unknown.",
    "Bow Saint misses and grieves for someone she respected and admired; she denies that the person is Taekyung.",
    "Jeok sent Great Sir to fetch Bow Saint; Taekyung was also looking for her after waking from a month-long sleep.",
    "Great Sir still remembers neither his identity nor his past, but showed insight into Bow Saint’s grief."
  ],
  "continuity_sources": [
    1179,
    1178
  ],
  "open_questions": [
    "What command will the Lord of Heaven give the Grand Mage?",
    "What remains to be completed, and what will happen when it is completed?",
    "What is Alpha, and what does its awakening mean?",
    "Why does the land around Taekyung’s group in Xinjiang contain no living things?",
    "Who is the person Bow Saint misses?"
  ],
  "safe_through": 1179,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 진위경    | **Jin Wikyung**    |
| 진무경    | **Jin Mukyung**    |
| 매종학    | **Mae Jonghak**    |
| 청풍     | **Cheongpung**     |
| 진천검    | **Heaven Shaking Sword**      | Jin Mukyung    |
| 검성     | **Sword Saint**               | Mae Jonghak    |
| 태원진가   | **Jin Family of Taiyuan**        |
| 무림맹    | **Murim Alliance**               |
| 암천     | **Dark Heaven**                  |
| 십봉룡    | **Ten Dragons and Phoenixes**    |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 후기지수   | **young prodigy** / **rising martial artist**    | Contextual, not a title                               |
| 강호     | **martial world**                                | Prefer “Murim” where the setting itself is meant      |
| 마적     | **mounted bandits**                              |                                                       |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 대주     | **Squad Leader** / **Commander**             |
| 태원     | **Taiyuan**            |
| 감숙     | **Gansu**              |
| 청해     | **Qinghai**            |
| 팔천협    | **Eight Spring Gorge** |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 소협      | **Young Hero**                                                  |
| 공자      | **Young Master**                                                |
| 창공 | **Cang Gong** | The bedridden East Depot leader for whom Ma Sanbao acts. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 모용영휘 | **Murong Yeonghwi** | A blood relative of the Murong Family regarded as an overwhelmingly powerful young prodigy. |
| 송호 | **Song Ho** | Elderly martial artist known as the Thousand-Faced Fox. |
| 이공자 | **Second Young Master** | Title used for Jin Mukyung. |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 고원 | **Gaoyuan** | Plateau region in northern Shanxi. |
| 개방 | **Beggars' Sect** | Murim organization counted among the Nine Sects and One Gang. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 대초원 | **Great Steppe** | The steppe region from which Temur and Chinggen come. |
| 천룡 | **Heavenly Dragon** | The ideal form Jeok Cheongang wishes Taekyung to become. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 일각 | **fifteen minutes** | Quarter of a shichen; used for the remaining completion time. |
| 천면호리 | **Thousand-Faced Fox** | Epithet of Song Ho. |
| 은영각 | **Hidden Shadow Pavilion** | Former Murim Alliance intelligence organization. |
| 은영각주 | **Chief of the Hidden Shadow Pavilion** | Office formerly held by Song Ho. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 심력 | **mental strength** | Inner mental capacity injured by Jongni Chu's feint. |
| 천산 | **Tianshan** | Mountain region identified as the Demonic Cult's headquarters. |
| 천산산맥 | **Tianshan Mountains** | Mountain range associated with the Demonic Cult. |
| 미미 | **Mimi** | Worker at Honghwaru referenced in Taekyung's joke. |
| 마두 | **fiend** | Demonic martial masters from the Great Faction War era. |
| 복마전 | **demon-slaying battleground** | A possible description for Sichuan if Dark Heaven attacks it. |
| 일기천룡 | **One-Ride Heavenly Dragon** | Sama Pyo's title for Murong Yeonghwi. |
| 신강 | **Xinjiang** | Region beyond Qinghai described as the domain of the Demonic Path. |
| 심해 | **deep sea** | Unexplored ocean depths where the ancient monster awakens. |
| 검귀 | **Sword Demon** | Title used for the kind of swordsman Mukyung is said to resemble. |
| 혈혼비마 | **Blood Soul Fat Demon** | The Demon Bird’s former sobriquet, which he resents. |
| 대인 | **Great Sir** | Name used for the mysterious figure in Ningxia. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진무경 | younger_to_older_brother | hyung | casual-but-junior | Retain hyung for 형 in Taekyung's greeting; Mukyung then punishes the casual speech. |
| 진무경 | 진태경 | older_to_younger_brother | youngest | blunt-senior | 막내 / youngest; may taunt that lasting a quarter-hour would make Taekyung the older brother. |
| 진태경 | 진위경 | younger_to_eldest_brother | brother | familiar-but-respectful | Self-corrects from the personal name to kinship: “Jin Wikyung—I mean, my brother?”; 큰형 is eldest brother. |
| 진위경 | 진태경 | eldest_to_youngest_brother | youngest | affectionate-protective | Uses youngest-brother address; openly affectionate beneath a public mask. |
| 진무경 | 진위경 | younger_to_older_brother | older brother | formal-but-blunt | Mukyung refers to Wikyung as 형 while remaining emotionally restrained. |
| 진위경 | 진무경 | older_to_younger_brother | little brother | affectionate-casual | Wikyung uses 아우야 and 무경아 with openly affectionate familiarity. |
| 청풍 | 진태경 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung repeatedly addresses Taekyung as 은인 after receiving food. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 관리 | 진태경 | official_to_young_martial_artist | Young Master | formal-polite | The official addresses Taekyung as 공자 while explaining the consequences of Prince Shangshan's displeasure. |
| 진태경 | 청풍 | companion_to_young_martial_artist | Young Master Cheongpung | formal-polite | Taekyung uses 청 공자 while correcting Cheongpung's royal-etiquette mistake. |
| 청풍 | 진무경 | young_martial_artist_to_renowned_senior_martial_artist | Young Hero Jin Mukyung | deferential and excited | Cheongpung calls him 진천검 진무경 소협 and later 진 소협 while seeking his duel. |
| 진무경 | 청풍 | senior_martial_artist_to_newly_met_young_martial_artist | Young Hero | deferential and expectant | Mukyung addresses Cheongpung as 소협 while asking whether Great Hero Mae descended from Huashan. |
| 매종학 | 청풍 | grandfather_to_grandson | Pung | affectionate-instructional | Mae Jonghak calls young Cheongpung 풍아 while teaching him the Crouching Tiger Fist. |
| 송호 | 청년 | elderly_martial_artist_to_younger_martial_artist | Young Hero | formal-polite | Song Ho calls out to the young man as 소협 at the chapter's end. |
| 송호 | 진태경 | senior_martial_artist_to_junior_martial_artist | you | familiar-polite | Uses 자네 while recognizing Taekyung and discussing his preliminary performance. |
| 매종학 | 송호 | savior_to_survivor | you | casual-familiar | Mae uses 자네 while speaking to Song Ho after his identity is recognized. |
| 송호 | 매종학 | rescued_survivor_to_savior | Great Hero; you | formal-deferential and familiar | Song Ho credits Mae with saving his life and addresses him as 대협. |
| 매종학 | 진태경 | older_ally_to_younger_friend | friend | casual-familiar | Mae Jonghak uses 친구 when arriving at Taekyung's window and asking to talk. |
| 청풍 | 미미 | handler_to_companion_snake | Mimi | cheerful-commanding | Cheongpung repeatedly calls and commands the Thousand-Year Poison Horned Snake. |
| 진위경 | 막내 | older brother to younger brother | my youngest | intimate and informal | Jin Wikyung uses 막내야 affectionately for Jin Taekyung. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 관리 | 진위경 | government official to influential martial artist | you | formal, then deferential | The official asks Jin Wikyung's identity before bowing and apologizing after learning of his connection to Yi Hongcheon. |
| 진위경 | 관리 | influential martial artist to government official | you | formal, controlled, and quietly authoritative | Jin Wikyung identifies the official's rank, demands that he withdraw his troops, and directs him to apologize. |
| 가솔 | 진태경 | Zhuge Clan retainer to Great Hero | Great Hero Jin | polite and pleading | Uses 진 대협 while urging Taekyung to stop provoking Ju Wongong. |
| 진태경 | 미미 | rescuer to companion snake | Mimi or Mimi-chan | informal, pleading | Taekyung calls to Mimi while asking the snake to carry him and the survivors. |
| 천면호리 | 매종학 | intelligence_chief_to_alliance_leader | Alliance Leader | formal and deferential | Requests that Mae move elsewhere with the others before he reports further. |
| 진위경 | 청풍 | Jin Family Lesser Family Head to young martial companion | Young Hero Cheongpung | formal-polite | Uses 청 소협 while summoning Cheongpung to the Alliance Leader's Hall. |
| 청풍 | 매종학 | grandson to grandfather | Grandpa | casual-familiar | Repeatedly calls Mae Jonghak 할아버지 while mistaking the Alliance Leader's summons as a family visit. |
| 진태경 | 매종학 | younger ally to newly installed Alliance Leader | Alliance Leader | formal and deferential | Uses 맹주님 while formally greeting Mae Jonghak as the Alliance Leader. |
| 매종학 | 천면호리 | Alliance Leader to Hidden Shadow Pavilion Chief | Chief of the Hidden Shadow Pavilion | casual-but-commanding | Asks Song Ho's view of Taekyung's suspected target. |
| 진태경 | 대인 | young martial artist to benefactor | you | casual and blunt | Taekyung asks who Great Sir is, addressing him as 당신. |
| 대인 | 진태경 | older benefactor to young martial artist | you | familiar conversational | Great Sir addresses Taekyung as 자네. |
| 청풍 | 대인 | younger companion addressing an older benefactor | Uncle Great Sir | polite and familiar | Cheongpung repeatedly calls him 대인 아저씨. |
| 대인 | 청풍 | older benefactor addressing a younger companion | you | familiar and teasing | Great Sir addresses Cheongpung as 자네. |
| 노인 | 진태경 | older opponent to younger opponent; no family relation established | you | calm, familiar speech | The old man addresses Taekyung as 자네 while testing him. |

## Listed compact profiles

### Cang Gong.md

# Cang Gong (창공)

- **Safe through:** Chapter 1169
- **Aliases:** None
- **Role:** Cang Gong is the Eastern Heaven Demon Lord’s assumed identity, through which he became the East Depot’s Brush-Holding Eunuch and a power second only to the Emperor.
- **Personality:** Calculating and self-assured, he is driven by vengeance and believes the rulers and the world betrayed him first.
- **Voice:** Dry and sardonic, he delivers taunts and judgments in measured statements.
- **Relationships:** He was raised by a master and fellow disciples in the Maoshan Sect, whose members died resisting the forced relocation of the capital; Ma Sanbao is his disciple, and he regards Jin Taekyung as a potential recruit.

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 1178
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, Sword Saint Mae Jonghak’s grandson and Disciple, a Supreme Peak master known as the Huashan Divine Dragon, creator of Mimi Step, and master of the Azure Dragon Pavilion; he has mastered the Slaughter Saint’s Ghost Illusory Slaughter Step and blended it with his Dark Fragrance Drift.
- **Personality:** Affable, dreamy, and childlike, with innocent curiosity, a deep love of martial arts, and compassion; guided by his grandfather’s righteousness and Taekyung’s chivalry, he meets danger with resolve and trusts Taekyung without wavering.
- **Voice:** Dreamy and hazy, with innocent, polite phrasing; he has begun imitating Taekyung's profanity.
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions; Taekyung is his true martial rival and the person whose way of life he admires, and the Slaughter Saint is his mentor in concealment and Ghost Illusory Slaughter Step.

### Jin Mukyung.md

# Jin Mukyung (진무경)

- **Safe through:** Chapter 997
- **Aliases:** Heaven Shaking Sword; Jin Family Second Young Master
- **Role:** Jin Mukyung is the second son of the Jin Family of Taiyuan, a Supreme Peak swordsman known as the Heaven Shaking Sword, and Commander of the Heaven Shaking Squad.
- **Personality:** Reserved and disciplined, Jin Mukyung is devoted to swordsmanship and guided by a strong sense of chivalry and responsibility; losses deepen his self-reproach and resolve to grow strong enough to protect others.
- **Voice:** Quiet and resonant, clipped and blunt, with dry sarcasm in familiar exchanges.
- **Relationships:** Jin Wikyung is his older brother and the Lesser Family Head who formed the Heaven Shaking Squad in his honor; Jin Taekyung is his younger brother, who shares his own grief and encourages him to keep trying; Cheol Mubaek died protecting Mukyung and left him the Shura Annihilating Fist manual; their father—the Jin Family Head—once apologized to Mukyung for his mother’s death in childbirth.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1179
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and eleventh member of the Ten Kings, a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; he serves as Thousand Captain of the Embroidered Uniform Guard, is enfeoffed as Prince Shangshan, and is widely regarded as a new-age savior.
- **Personality:** Hungry, self-aware, and dryly observant, he is pragmatic and fiercely defiant; he protects those he cherishes and meets mounting responsibility with hope and a determination to endure.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother and Jeok Cheongang his Master and trusted confidant; he shares deep loyalty with Hyuk Mujin, whom he values as family, and considers the revived Undead King, formerly the Skeleton King, a friend.

### Jin Wikyung.md

# Jin Wikyung (진위경)

- **Safe through:** Chapter 1140
- **Aliases:** Junzi Sword
- **Role:** Jin Wikyung is the thirty-six-year-old Lesser Family Head and future Family Head of the Jin Family of Taiyuan, the Alliance Leader who unified Shanxi Murim and Shanxi Province's foremost landowner and magnate.
- **Personality:** Calm and politically capable, Jin Wikyung takes responsibility for his people and prioritizes their lives; he uses calculated leverage to keep dangerous allies in line and commits firmly to his principles, even when doing so means remaining in a losing battle.
- **Voice:** Restrained, formal, and commanding with subordinates; openly affectionate, proud, and occasionally exuberant with Taekyung.
- **Relationships:** Jin Wikyung is Taekyung’s eldest brother and future Family Head, protects and mentors him, and commands the Jin Family’s forces; Jin Mukyung is his younger brother, and he considers the Jin Family indebted to the Dongting Fisherman and the other fallen defenders of Shanxi.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1179
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Mae Jonghak.md

# Mae Jonghak (매종학)

- **Safe through:** Chapter 1144
- **Aliases:** Sword Saint
- **Role:** Sword Saint and Cheongpung's grandfather who now serves as the New Murim Alliance's Alliance Leader and has ordered Jin Taekyung's first Fire Dragon Pavilion mission to Nanman.
- **Personality:** Playful and easygoing in ordinary company, yet guided by a principled commitment to chivalry that can outweigh strategic caution.
- **Voice:** Friendly, casually familiar, and cheerfully teasing, including when greeting old acquaintances and discussing leadership.
- **Relationships:** Cheongpung's grandfather and martial instructor; taught him the Taeeul Miri Palm; secretly entered Huashan while its Sect Leader slept, left a dagger and handwritten note, and then went into hiding, prompting Huashan's search; fought Jeok Cheongang at Mount Jiuhua more than forty years ago and left after their draw; his old friend Hong Dao left him a letter identifying Jin Taekyung as the Morning Star who would drive away darkness.

### Murong Yeonghwi.md

# Murong Yeonghwi (모용영휘)

- **Safe through:** Chapter 982
- **Aliases:** One-Ride Heavenly Dragon
- **Role:** Murong Yeonghwi is a blood relative of the Murong Family and an overwhelmingly powerful young prodigy who escaped the family’s annihilation with several dozen others and is now being pursued toward Liaoning.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** He is a blood relative of the Murong Family.

### Song Ho.md

# Song Ho (송호)

- **Safe through:** Chapter 1086
- **Aliases:** Thousand-Faced Fox
- **Role:** Elderly Peak master known as the Thousand-Faced Fox, a martial artist with a prosthetic leg, and current Chief of the Hidden Shadow Pavilion, overseeing a vetted intelligence network that includes highly trained assassins.
- **Personality:** Outwardly genial and relaxed, but observant, forceful, and intimidating when pursuing information.
- **Voice:** Lightly genial and conversational, turning quietly coercive during interrogation.
- **Relationships:** He serves under Mae Jonghak's New Murim Alliance, commands the Hidden Shadow Pavilion, and recognizes Jin Taekyung as Jeok Cheongang's Disciple.

## Korean source

```text
＃1180화



사막과 어둠만이 들었던 대인의 마지막 뇌까림은 반은 맞고, 반은 틀렸다.

어스름한 새벽안개가 물러가고 여명이 번지기 시작할 즈음, 하늘은 이때만을 기다려왔다는 듯 온 힘을 다해 폭우를 쏟아 내기 시작했다.

메마른 사막이 아닌, 서쪽의 고원(高原)을 향해.

콰아아아아.

장대비가 쏟아졌다. 맹렬하게 휘몰아치는 비바람 앞에 사람들은 옷깃을 여미며 도롱이를 깊게 눌러썼고, 그들을 태운 짐승들은 힘겨운 울음소리를 흘렸다.

“미친 듯이 퍼붓는군. 이래서야 사람은 둘째치고 말들이 버티지 못하겠는걸.”

기름먹인 죽립(竹笠) 아래로 흘러나온 묵직한 음성에, 그의 오른편에서 천천히 말을 몰고 있던 청년이 입을 열었다.

“지금까지 버텨 준 것만으로도 천운입니다. 반나절 뒤면 이 지긋지긋한 고원도 벗어날 수 있을 테니, 조금 더 힘을 내는 수밖에요.”

지긋지긋한.

죽립인은 청년의 그 표현에 공감하지 않을 수 없었다.

아니, 비단 자신뿐만이 아니라 지금 이 순간에도 무거운 발걸음을 옮기고 있는 수만 명의 무림인 역시 같은 생각이리라 확신했다.

“그래, 정말 쉽지 않았지.”

혼잣말처럼 중얼거린 죽립인은 이곳까지 오며 보았던 광경을 떠올렸다.

메마른 강과 죽어 있는 숲.

사람이 머물렀다는 증거인 동시에, 과연 정말 누군가가 머물렀을까 싶을 만큼 황폐해진 마을과 도시까지.

모든 우물은 썩어 있었고, 주위를 샅샅이 수색해 보아도 사람은커녕 그 흔한 날벌레의 사체조차 보이지 않았다.

마치, 처음부터 존재하지 않았던 것처럼.

‘도대체 이곳에서 무슨 일이 벌어진 거지?’

죽립인은 줄곧 해소되지 않았던 의문을 떠올렸지만, 이 문제에 대해 아무리 깊게 고민해 보았자 소용없는 심력 낭비라는 것쯤은 이미 알고 있었다.

그가 홀로 깨달을 정도의 일이었다면, 어느샌가 다가와 눈인사를 건네는 저 백발의 노인이 모를 리 없었을 테니까.

“송 대협.”

죽립인의 정중한 포권지례에, 천면호리(千面狐狸) 송호가 빙긋 웃었다.

“진 가주께서 이토록 예의를 갖추어 주시니 이 늙은이가 민망하여 몸 둘 바를 모르겠구려. 그저 각주라 불러 주시면 족합니다.”

죽립인, 아니 진위경이 멋쩍게 고개를 저었다.

“대협께 비하면 아직 까마득한 후배에 불과합니다. 게다가 저는 단지 가주 대행을 맡은 소가주일 뿐입니다.”

“그야 당연히 알고 있습니다만, 이럴 때일수록 가문의 결속력이 중요한 법이지요. 게다가 태원진가의 가주께서는…….”

“부재중이시죠. 여전히.”

불쑥 끼어든 청년의 말에, 진위경이 입맛을 다셨다.

“둘째야.”

태원진가의 이공자, 진천검(振天劍) 진무경이 반문했다.

“둘째가 누굽니까?”

“……그래, 정정하지. 진천대주.”

“하명하십시오.”

“인원을 선별하여 인근을 수색하거라. 아니, 하게. 나는 여기 계신 송 대협과 긴히 나눌 이야기가 있으니.”

“진천대주 진무경, 가주의 명을 받듭니다.”

“너……!”

“그럼 이만.”

진위경이 뭐라 할 틈도 주지 않은 채, 천연덕스럽게 대답한 진무경은 장포 자락을 휘날리며 빗줄기 너머로 사라졌다.

“후우, 저 녀석이.”

한숨을 내쉬는 진위경의 모습에, 천면호리가 나직한 웃음소리를 흘렸다.

“너무 질책하지 마십시오. 오히려 듣던 대로 형제간의 우애가 두터운 것 같아 보기 좋습니다.”

“아닙니다. 제 아우는 한번 혼쭐이 나야 합니다. 아주 기본이 안 되어 있어요. 웃어른께서 말씀하시는데 끼어들기나 하고.”

“개의치 마십시오. 저는 괜찮습니…….”

“게다가 우산도 안 챙겨갔잖습니까.”

“예?”

“비가 이렇게 많이 오는데! 쓰라고 몇 번을 말해도 들은 척도 안 하고! 하다못해 죽립도 안 쓰고!”

“…….”

“머리털이야 지금 당장 빠지는 게 아니니까 괜찮다지만! 이러다가 고뿔이라도 걸리면 어떡해요, 예? 안 그렇습니까?”

갑자기 열변을 토하는 진위경의 모습에, 잠시 침묵하던 천면호리가 입을 열었다.

“정말…… 우애가 두터우시군요. 듣던 것 이상으로.”

“제 아우들이 어릴 때는 몸이 허약했습니다. 태경이 녀석도 지금쯤 고생이 이만저만이 아닐 텐데, 몸은 잘 돌보고 있는지 걱정이 되는군요.”

이쯤 되니 천면호리도 걱정하는 마음이 들었다.

진위경의 정신에 문제가 있는 것이 아닌가, 하는 걱정이.

진천검 진무경이 누구인가.

어릴 적부터 특출난 재능 하나만으로 무림 최고의 후기지수 중 한 명으로 손꼽혔고, 일기천룡(一騎天龍) 모용영휘가 가문의 몰락과 함께 사라진 직후부터는 그가 십봉룡의 수좌임을 누구도 부정하지 않는다.

정확히는, 이제 후기지수라 불릴 수준도 아득히 넘어섰다. 

북방 전역의 운명을 결정지은 지난 팔천협 전투에서, 저 태원진가의 젊은 검귀는 전대의 대마두였던 혈혼비마(血魂肥魔)를 쓰러트리며 새로운 초절정 고수의 탄생을 만천하에 알렸으니까.

그런데 그런 진무경이 고뿔이라니.

심지어 괴물 중의 괴물인 진태경의 이름이 나왔을 때는 어이가 없어서 할 말을 잃을 뻔했다.

‘지금 농담하는 건가?’

천면호리는 웃어 줘야 하는 건지 잠시 고민했지만, 이내 은영각주다운 노련한 솜씨로 표정을 관리했다.

“진 소협은 잘 지내고 있을 겁니다. 설령 약간의 문제가 생겼더라도 별일 없겠지요.”

“그 부분은 저도 충분히 안심하고 있습니다.”

두 아우, 그중에서도 오랫동안 아픈 손가락이었던 막내를 끔찍이 생각하는 진위경도 이번만큼은 진심 어린 동의를 표했다.

사막이라는 지형의 특성과 속도를 고려한 탓에 인원 자체는 극소수에 불과하지만, 초절정 고수가 무려 여섯이나 포진된 최정예.

심지어 그중 셋은 현 무림맹주인 검성 매종학과 비교해도 크게 부족함이 없는 고수들이니, 만에 하나 큰 위협이 닥치더라도 각자의 몸을 지키기에는 부족함이 없을 터였다.

다만 약간의 우려가 있다면, 그건 단 한 사람의 존재였다.

‘대인, 이라고 했던가.’

소문은 익히 들었다.

새로운 초절정 고수의 출현은 언제나 세간의 이목을 집중시키기 마련이고, 그것은 암천의 흉계가 온 천하를 뒤흔드는 상황에서도 마찬가지였으니까.

아니, 오히려 더했다.

지금처럼 어려운 상황에 등장한, 봉두난발에 반쯤 정신이 출타한 듯한 신비의 고수?

심지어 십여 년 전 감숙성에 난립하던 마적들을 단숨에 진압했던 협객?

더 말이 필요 없다.

강호의 호사가들은 ‘이건 못 참지’를 외치며 입술이 마르도록 대인에 대해 떠들어 댔고, 대인에 관한 소문은 온 천하에 퍼졌다.

‘하지만, 소문이란 결국 믿을 게 못 되지.’

일가(一家)를 이끄는 만큼 진위경은 매사에 신중하고, 특히 아우들의 안위에 관해서만큼은 안전불감증 환자다.

그런 그가 막내아우의 일행에 합류하게 된 이 수상쩍은 괴인을 직접 만나고자 마음먹은 것은 당연한 일이었다.

비록, 결과적으로는 실패하고 말았지만.

‘조금 더 시간이 있었다면 좋았을 텐데.’

대인은 대초원의 바람 같은 사람이었다.

처음 성벽 위에서 진태경의 곁에 서 있던 모습만 잠시 보았을 뿐, 그는 늘 어디론가 사라졌다가 어디에선가 불쑥 나타났다.

잠시라도 대인의 행적이 묘연해졌다면 첩자임을 깊게 의심해 보았겠지만, 나름대로 면밀히 조사해 본 결과 그것도 아니었다.

대인은 항상 쩌렁쩌렁한 목청으로 외치는 헛소리와 고약한 악취로 그 존재감을 만천하에 발산했다.

출전을 앞두고 눈코 뜰 새 없이 바빴던 진위경이 간신히 짬을 내어 처소로 찾아갔을 때 그는 다른 곳에서 개방 방주와 술잔을 기울이며 입방(入幇) 제의를 받고 있었고, 그조차도 여의치 않아 진무경이나 다른 가솔들을 보냈을 때는 청풍과 함께 군량 창고에 숨어 군것질거리를 찾는 중이었다.

그리고 그런 대인을, 대부분의 사람들은 좋아했다.

혈육으로서 아끼는 마음과는 별개로, 그 스승만큼이나 매우 까탈스러운 성격을 지녔다고 생각하는 막내아우조차도.



‘대인? 글쎄, 잘은 모르겠지만 지켜본 바로는 좋은 사람 같던데요.’

‘어허, 막내야! 내가 누누이 말하지 않았느냐. 모르는 사람은 조심 하-’

‘저야 감숙성에서부터 지켜본 것도 있고 뭐, 이리저리 생각해 보긴 했는데 느낌이 좋아요. 마치 형님처럼.’

‘……나처럼?’

‘아니, 그런 표정 좀 짓지 마세요. 나야 당연히 형님이 더 좋지. 비교가 되나.’

‘아, 그렇지?’

‘당연하죠. 근데 형님. 당과 좀 드실래요? 청풍이 놓고 갔던데.’

‘어? 응. 그래!’



그게 마지막이었다.

일각이 여삼추일 만큼 시간은 촉박했고, 진위경은 더욱 바빠졌으며, 대인은 여전히 바람처럼 온 사방을 쏘다녔다.

그리고 머지않아, 대륙 역사상 유례없던 관무연합군(官武聯合軍)은 청해와 신강의 경계에서 세 갈래로 갈라졌다.

두 개의 거대한 파도와 하나의 송곳 같은 형태로.

“……당과, 맛있었지.”

자신도 모르게 중얼거린 진위경은 문득 볼에 닿는 뜨거운 시선을 느끼고 정색했다.

“아, 실례했습니다. 지금쯤 황군(皇軍)이 어디쯤 도착했을지 하는 깊은 생각에 잠기는 바람에 그만.”

그 놀라울 만큼 뻔뻔한 대답에 천면호리 송호는 잠시 입을 다물었다.

그는 늙고 심지어 다리도 하나 없지만, 귀는 여전히 두 개였으며 청각 또한 생생했으니까.

대관절 무슨 당과를 그리 맛있게 처먹었는지 묻고 싶긴 했으나, 천면호리는 다시 한번 연륜을 발휘하여 최대한 담담하게 대답했다.

“계획에 차질이 없다면, 이미 보름 전 나포박호(羅布泊湖)를 넘어 지금쯤 화정(和靜)에 이르렀겠지요.”

“그렇다면.”

“예. 이제 천산이 지척입니다. 하루 정도의 미미한 차이는 있을 수 있겠으나, 아마도 모레 해가 지기 전 천산 산맥의 끝자락에서 합류할 수 있을 것입니다.”

“……!”

천산산맥.

그 네 글자를 듣는 순간, 진위경은 말고삐를 쥔 손에 힘이 들어가는 것을 느꼈다.

천산, 하늘과 가장 가까이 닿아 있는 거대한 흙의 거인.

천년에 달하는 아득한 시간 동안 무수한 악을 쏟아 냈음에도, 도무지 그 끝을 짐작할 수 없는 어둠이 웅크린 천하의 복마전.

‘그러나 드디어.’

그들이 왔다. 

이 기나긴 여정의 끝에, ‘그’가 기다리고 있다.

하지만 진위경이 그 사실에서 비롯된 전율과 두려움을 가라앉히기도 전에, 저 멀리서 익숙한 목소리가 울려 퍼졌다.

“형님-!”

진무경. 바로 그였다.

지금껏 한 몸처럼 여기던 말은 어디에 둔 것인지, 홀로 경공을 발휘하여 화살처럼 쏘아져 오는 아우의 모습에 진위경이 눈을 크게 떴다.

그리고 보았다.

가까워지는 진무경의 어깨 뒤로 펼쳐진 낯선 풍경을.

‘산맥?’

짙은 어둠으로도 가릴 수 없는 자연의 형체.

세찬 빗줄기 너머로 드러난 그것은 실로 거대했으며, 또한 광대했다.

‘천산, 저것이 말로만 듣던 그 천산인가.’

그러나 어째서일까.

가슴은 어찌 이리도 가파르게 뛰고, 진무경의 외침은 왜 이리도 급박한 것일까.

다음 순간, 진위경은 그 이유를 깨달았다.

아니, 알려주었다.

아득한 창공을 베어가르며 내리꽂힌, 한 줄기의 거대한 벼락이.

쿠르르릉!

굉음과 함께 번뜩인 찰나의 빛 속에서, 무수한 괴물들의 포효가 울려퍼졌다.
```

## Final English reading copy

```markdown
# Chapter 1180

Great Sir’s final mutterings, heard only by the desert and the darkness, had been half right and half wrong.

As the dusky dawn mist receded and the first light began to spread, the sky unleashed a downpour with all its might, as if it had been waiting for this moment.

Not over the parched desert, but toward the western plateau.

*Whoooosh!*

Torrential rain poured down. Before the fierce wind and rain, people pulled their collars tight and lowered their rain capes over their heads. The beasts carrying them let out weary cries.

“It’s coming down like crazy. At this rate, forget the people—the horses won’t hold out.”

At the deep voice from beneath an oil-treated bamboo hat, the young man riding slowly at his right spoke up.

“We’re lucky they’ve held out this long. We’ll be clear of this wretched plateau in half a day, so we have no choice but to hang on a little longer.”

Wretched.

The man in the bamboo hat couldn’t help agreeing with the young man’s choice of words.

In fact, he was certain that not only he, but tens of thousands of martial artists trudging forward at that very moment, felt the same way.

“Yes. It’s been a hard road.”

The man in the bamboo hat muttered to himself and remembered what he’d seen on the way here.

Dry riverbeds and dead forests.

Villages and cities—proof that people had once lived there, yet so desolate it was hard to believe anyone ever had.

Every well was foul. They’d searched the surroundings thoroughly, but found no people—not even the carcass of a common gnat.

As if nothing had ever lived there at all.

*What on earth happened here?*

The man in the bamboo hat thought again of the question that had long gone unanswered. But he already knew that no matter how deeply he pondered it, he’d only be wasting his mental strength.

If he could have figured it out on his own, then the white-haired old man approaching now with a nod of greeting would surely have done so as well.

“Great Hero Song.”

At the man’s respectful salute, Song Ho, the Thousand-Faced Fox, smiled.

“Family Head Jin, you’re being so formal that this old man hardly knows where to put himself. Just call me Chief.”

The man in the bamboo hat—no, Jin Wikyung—shook his head awkwardly.

“Compared to you, I’m still a junior by a long way. Besides, I’m only the Lesser Family Head acting in the Family Head’s place.”

“I know that, of course. But these are precisely the times when a family’s unity matters most. And the Family Head of the Jin Family of Taiyuan…”

“He’s away. Still.”

At the young man’s abrupt interruption, Jin Wikyung clicked his tongue.

“Little brother.”

The second young master of the Jin Family of Taiyuan, the Heaven Shaking Sword, Jin Mukyung, replied, “Who’s your little brother?”

“…Fine. Commander of the Heaven Shaking Squad.”

“Give your order.”

“Pick some men and search the surrounding area. No—Commander, please see to it. I need to speak privately with Great Hero Song.”

“Commander Jin Mukyung acknowledges the Family Head’s orders.”

“You…”

“Then I’ll be off.”

Without giving Jin Wikyung a chance to say another word, Jin Mukyung answered as casually as could be and disappeared into the rain, his long robe whipping behind him.

“Whew. That boy…”

At Jin Wikyung’s sigh, the Thousand-Faced Fox let out a quiet chuckle.

“Don’t be too hard on him. From what I’ve heard, it’s good to see that the brothers are so close.”

“No, my younger brother needs a good scolding. He has no manners at all. Interrupting an elder while he’s speaking.”

“Don’t mind me. I’m quite all rig—”

“And he didn’t even bring an umbrella.”

“Pardon?”

“It’s pouring like this! I told him several times to use one, and he didn’t even listen! He didn’t even wear a bamboo hat!”

“…”

“I know he’s not going to lose his hair right this instant, but what if he catches a cold? What then, hm? Am I wrong?”

At Jin Wikyung’s sudden outburst, the Thousand-Faced Fox fell silent for a moment before replying.

“You really are… close. Closer than I’d heard.”

“When my younger brothers were little, they were frail. Taekyung must be having a hard time now, too. I worry whether he’s taking good care of himself.”

By this point, even the Thousand-Faced Fox was beginning to worry.

He was starting to wonder whether there was something wrong with Jin Wikyung’s mind.

Who was the Heaven Shaking Sword, Jin Mukyung?

Since childhood, he’d been counted among the finest rising martial artists in Murim on the strength of his extraordinary talent alone. And after One-Ride Heavenly Dragon Murong Yeonghwi vanished with the downfall of his family, no one had denied Mukyung his place at the head of the Ten Dragons and Phoenixes.

To be precise, he’d long since surpassed the level of a rising martial artist.

In the recent Battle of Eight Spring Gorge, which decided the fate of the entire northern region, that young Sword Demon of the Jin Family of Taiyuan had defeated the Blood Soul Fat Demon, a great fiend of the previous generation, announcing the birth of a new Supreme Peak master to the world.

And yet Jin Wikyung was worried he’d catch a cold.

When he’d even brought up the monster among monsters, Jin Taekyung, the Thousand-Faced Fox had nearly been too dumbfounded to speak.

*Is he joking right now?*

The Thousand-Faced Fox briefly wondered whether he ought to laugh. Then, with the practiced skill of the Chief of the Hidden Shadow Pavilion, he kept his expression in check.

“Young Hero Jin is doing well. Even if he’s run into a little trouble, I’m sure it’s nothing serious.”

“That part doesn’t worry me at all.”

Jin Wikyung, who doted on his two younger brothers—and especially his youngest, who’d long been his sore spot—agreed with heartfelt sincerity for once.

The force they’d sent was tiny, given the terrain and the need for speed. But it included no fewer than six Supreme Peak masters, an elite force by any measure.

Three of them were hardly inferior to Mae Jonghak, the current Alliance Leader of Murim. Even if a major threat arose, each of them should be more than capable of protecting himself.

If Jin Wikyung had one concern, it was a single person.

*The Big Man, was it?*

He’d heard the rumors.

The appearance of a new Supreme Peak master always drew the world’s attention, and that was no different even as Dark Heaven’s schemes shook the land.

If anything, the interest was greater.

A mysterious master who’d appeared in such troubled times, with wild hair and half his mind seemingly somewhere else?

A chivalrous hero who’d single-handedly crushed the mounted bandits running rampant in Gansu more than a decade ago?

That was all it took.

The martial world’s gossips couldn’t resist. They talked about the Big Man until their mouths were dry, and rumors about him spread across the land.

*But rumors aren’t worth much in the end.*

As the man responsible for leading a family, Jin Wikyung was cautious in all things—and when it came to his younger brothers’ safety, he was practically allergic to risk.

So of course he’d decided to meet the suspicious eccentric who’d joined his youngest brother’s group himself.

Though, in the end, he’d failed.

*I wish I’d had a little more time.*

The Big Man was like a wind blowing across the Great Steppe.

Jin Wikyung had seen him only briefly, standing beside Jin Taekyung atop the city wall. After that, he was always vanishing somewhere, then suddenly turning up somewhere else.

If the Big Man had ever gone missing for a while, Jin Wikyung might have seriously suspected he was a spy. But after conducting a fairly thorough investigation, he’d found that wasn’t the case.

The Big Man made his presence known to the whole world with his booming shouts of nonsense and his foul stench.

Just before the army set out, Jin Wikyung had been so busy he could barely find a moment to visit his quarters. The Big Man had been elsewhere, drinking with the Beggars’ Sect Leader and being invited to join the sect. When even that hadn’t worked out, he’d sent Jin Mukyung and other family members in his place, only to find the Big Man hiding with Cheongpung in the military supply warehouse, looking for snacks.

And most people liked the Big Man.

Even his youngest brother, whom Jin Wikyung thought just as finicky as his master, liked him.

“The Big Man? I don’t know him that well, but from what I’ve seen, he seems like a good person.”

“Come now, youngest! How many times have I told you to be careful around people you don’t know—”

“I’ve been watching him since Gansu, and, well, I’ve thought it over from every angle. I’ve got a good feeling about him. Like I do about you, hyung.”

“…Like me?”

“Don’t make that face. Of course I like you more, hyung. There’s no comparison.”

“Oh, right.”

“Of course. But, hyung, would you like some candy? Cheongpung left it behind.”

“Hm? Sure!”

That was the last time.

Time was pressing; a quarter hour felt like three autumns. Jin Wikyung grew busier still, while the Big Man continued darting all over the place like the wind.

And before long, the unprecedented combined army of the government and Murim split into three forces at the border between Qinghai and Xinjiang.

Two like enormous waves, and one like a sharp awl.

“…The candy was good.”

Jin Wikyung found himself murmuring aloud. Then he noticed someone’s hot gaze on his cheek and straightened his expression.

“Ah, pardon me. I was deep in thought about where the Imperial Army might be by now.”

At that remarkably shameless answer, Song Ho fell silent for a moment.

He was old, and even missing a leg, but he still had both ears, and his hearing was as sharp as ever.

He wanted to ask what candy Jin Wikyung had been enjoying so much, but the Thousand-Faced Fox once again put his years of experience to work and answered as calmly as he could.

“If all has gone according to plan, they crossed Lop Nur fifteen days ago and should be reaching Hejing about now.”

“Then…”

“Yes. The Tianshan Mountains are close. There may be a slight difference of a day or so, but they should be able to meet us at the foot of the range before sunset the day after tomorrow.”

“…”

Tianshan Mountains.

The moment he heard the name, Jin Wikyung felt his hand tighten around the reins.

Tianshan, a giant of earth reaching closer to the heavens than any other.

The lair of darkness, an unfathomable demon-slaying battleground that had poured forth countless evils over a thousand years, yet whose depths remained impossible to gauge.

*But at last.*

They had arrived. At the end of this long journey, *he* was waiting.

But before Jin Wikyung could calm the shiver of awe and fear that thought sent through him, a familiar voice rang out in the distance.

“Hyung!”

Jin Mukyung. It was him.

Jin Wikyung’s eyes widened as his younger brother came hurtling toward him like an arrow, using his lightness skill. Where had he left the horse he’d treated like an extension of himself until now?

And then Jin Wikyung saw it.

A strange landscape spread behind Jin Mukyung’s approaching shoulder.

*A mountain range?*

A natural formation that even the deep darkness couldn’t hide.

It loomed vast and immense beyond the driving rain.

*Is that Tianshan? The one I’ve heard so much about?*

But why?

Why was his heart pounding so hard? Why did Jin Mukyung’s voice sound so urgent?

The next moment, Jin Wikyung understood.

Or rather, a single enormous bolt of lightning, slashing down through the distant sky, showed him.

*Rumble!*

As the thunder boomed and a flash of light flared for an instant, the roars of countless monsters rang out.
```

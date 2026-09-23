<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0922.txt",
      "sha256": "5781585b69c373bb1a78ccf1521de58e178cf94733a42468195eaff67879b332",
      "bytes": 12779
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "8c976be956752b42ae44ec590488ed7e84fdb7641f586a0dbd5d7a8031b9769b",
      "bytes": 1292
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "e4f261a256443b1a8267b983fdbd4ae7aa3530803a007681e483b189b757b921",
      "bytes": 231635
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "7a8244c7e78494a61127fecf323bf4e6dd7d5aca5bc2582457b29d3f31f98862",
      "bytes": 759
    },
    {
      "path": "characters/Eastern Heaven Demon Lord.md",
      "sha256": "75f16a93d831a3ec8f20a493608dca9e031d1cd9c4552bcef20abff90fc6bc39",
      "bytes": 807
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "f30c3c1594eaffc16300abb7146d4b7a6a69ef3988fc6c6bdf20060be61800d5",
      "bytes": 1445
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "9db43ddfcbd8333f621c0ba85779118665797ccef0e954aab9da5f8ea20d193a",
      "bytes": 1244
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "86c66a11f39c3bc637131d6a08ca19c425fe58d20fda47173c1f9d7aa0145293",
      "bytes": 1290
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "880a93c0787a85ab019662da0e75325914691819fdd07eb1e10f96417e32824f",
      "bytes": 622
    },
    {
      "path": "characters/Ju Hwaran.md",
      "sha256": "7aebe4ffbcf60e214550f4ff4ffa1c3fa10178d7d2d2d813bcbea1f55b3e6a76",
      "bytes": 973
    },
    {
      "path": "characters/Martial God.md",
      "sha256": "98ee004f0ffffb4f71c85cdbd77be2c02fafe66a43d918793917fd8a36128084",
      "bytes": 752
    },
    {
      "path": "characters/Sama Pyo.md",
      "sha256": "ddfca8f0d995d0ae2707b54ca7e1ce2cd65022d8c47daa737336692e8a8ed41e",
      "bytes": 936
    },
    {
      "path": "characters/So Gyo.md",
      "sha256": "4c2e1a5d436f41ebc934f8b6422be0e94a72f4309e1f6c4518d9ea2cabd0e226",
      "bytes": 767
    },
    {
      "path": "characters/Song Il.md",
      "sha256": "f7b535d9359b6d2570494de4c23f985c10bf7d016c9f8c29a955d601ad24571f",
      "bytes": 964
    },
    {
      "path": "characters/Song Ilseom.md",
      "sha256": "aa5f966fe04122e90055b27a8e0e7ad0bdb513c3c130bb03cc930f017ef10dcf",
      "bytes": 1074
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "c7a36227d6b66db47d531c8eb040aff8beb26a02cb39b8b5c3d571a8a72b687e",
      "bytes": 685
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "21fe7ebbf3c46e6a6c651cab2cf39578c984d9cc64cf538e5662e8d6ad657b81",
      "bytes": 265353
    }
  ],
  "estimated_tokens": 13752
}
-->

# Durable State Update — Chapter 922

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
1 and safe_through 922. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 922. Profile updates may replace only one
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
  "chapter": 922,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 922,
    "continuity_sources": [922],
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
    "So Gyo is the Bow Saint; her two curved swords can join into the bow’s original form.",
    "So Gyo says Jin Taekyung is the chosen one the Martial God spoke of; her allegiance remains unknown.",
    "The Eastern Heaven Demon Lord remains at the scene, neither dead nor alive.",
    "The rebel battle at the grand banquet hall has ended; the apparent ringleaders are being kept alive for questioning.",
    "Ma Sanbao is missing.",
    "The Salcheonmun vowed to pursue Mungyeong regardless of cost or delay and may pursue Jin Taekyung if it learns he killed Gye Yabu."
  ],
  "continuity_sources": [
    920,
    921
  ],
  "open_questions": [
    "What enabled Jin Taekyung to return from his seemingly fatal injuries?",
    "What is the Eastern Heaven Demon Lord’s current condition, and what information does he hold about Dark Heaven and the Lord of Heaven?",
    "Where is Ma Sanbao, and what is his current status?",
    "What does the Martial God’s reference to a chosen one mean for Jin Taekyung?",
    "Will the Salcheonmun pursue Mungyeong or discover that Jin Taekyung killed Gye Yabu?"
  ],
  "safe_through": 921,
  "temporary_decisions": [
    "Keep “Force” for 강기 distinct from “death energy” for 사기."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 송일     | **Song Il**        |
| 주화란    | **Ju Hwaran**      |
| 무신     | **Martial God**               | —              |
| 궁성     | **Bow Saint**                 | —              |
| 암천     | **Dark Heaven**                  |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 중원     | **Central Plains**                               |                                                       |
| 화산     | **Huashan**            |
| 노부      | **this old man / I**                                            |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 동천마군 | **Eastern Heaven Demon Lord** | Title of the absurd masked antagonist in Jin's nightmare. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 사마표 | **Sama Pyo** | Young Sect Leader of the Black Dragon Demon Gate. |
| 소교 | **So Gyo** | The palace attendant leading the group assigned to serve Prince Shangshan. |
| 송일섬 | **Song Ilseom** | Young escort captain of the Yongbong Escort Bureau; distinct from Song Il of Zhongnan. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 은영각 | **Hidden Shadow Pavilion** | Former Murim Alliance intelligence organization. |
| 화란 | **Hwaran** | Familiar short form of Ju Hwaran. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 무한 | **Wuhan** | Capital of Hubei Province near Dongting Lake. |
| 수마 | **sleep demon** | Metaphor for the force keeping Jin unconscious. |
| 지옥도 | **hellscape** | Metaphorical description of the devastated battlefield. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 혁무진 | 적천강 | subordinate_to_overwhelming_elder | Great Hero Jeok | deferential and fearful | Mujin uses 적 대협 while reporting Jeok’s orders and Taekyung’s awakening. |
| 적천강 | 혁무진 | overwhelming_elder_to_junior_martial_artist | you stupid fool | blunt and mocking | Jeok calls Mujin a 멍청한 놈 after knocking him down during the attempted escape. |
| 송일 | 진태경 | hostile Zhongnan Elder to accused outsider | you / Jin Taekyung | hostile and threatening | Song Il questions Taekyung's identity and later threatens him over Gong Ilhyuk's injury. |
| 송일 | 적천강 | former rescued junior to former rescuer | Great Hero Jeok | formal, fearful, and defensive | Uses 적 대협 while insisting that Jeok has no business interfering in the dispute. |
| 적천강 | 송일 | former rescuer to former rescued junior | Zhongnan brat; you; insolent bastard | blunt, mocking, and humiliating | Jeok recalls Song's youthful arrogance and addresses him with contempt while publicly disciplining him. |
| 송일섬 | 주화란 | escort_captain_to_young_bureau_head | Hwaran | urgent and familiar | Calls out 화란아 while urgently warning Ju Hwaran before stepping into the confrontation. |
| 주화란 | 진태경 | escort_bureau_leader_to_famous_younger_martial_artist | Young Hero Jin | formal-deferential | Hwaran introduces herself as the Young Bureau Head and formally greets Taekyung as 진 소협. |
| 진태경 | 주화란 | visitor_to_young_bureau_head | Young Lady Ju | formal-polite | Taekyung uses 주 소저 while announcing that his party must leave. |
| 주화란 | 혁무진 | rescued_survivor_to_benefactor | Benefactor | formal-deferential | Hwaran includes Mujin among the Benefactors when greeting Taekyung's companions. |
| 주화란 | 송일섬 | bureau_head_to_escort_captain | Captain Song | formal and prosecutorial | Uses his office title, then his personal name, while exposing and confronting him. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 진태경 | 엄마 | son_to_mother | Mom | casual and startled | Jin cries out to his mother as she charges at him during the hospital visit. |
| 엄마 | 진태경 | mother_to_son | my son | warm and affectionate | Taekyung's mother praises him during the public welcome. |
| 주화란 | 사마표 | former_fiancés | Young Sect Leader | formal and guarded | Hwaran formally greets her former fiancé. |
| 사마표 | 태산 | Young Sect Leader to subordinate | Taishan | informal and patronizing | Sama Pyo calls Taishan by name while ordering him to leave. |
| 태산 | 사마표 | subordinate to Young Sect Leader | Lord | crude and deferential | Taishan uses 주군 while obeying Sama Pyo. |
| 태산 | 진태경 | subordinate_to_respected_outsider | Jin Taekyung | clipped and familiar | Taishan says he likes Jin Taekyung but will fight him without hesitation if Sama Pyo commands it. |
| 사마표 | 적천강 | Young Sect Leader to legendary elder | Great Hero Jeok | formal-deferential | Sama Pyo formally pays his respects to Jeok Cheongang as the Fire King. |
| 태산 | 적천강 | subordinate of a Young Sect Leader to legendary elder | Fire King | clipped, childlike, and deferential | Taishan gives his awkward greeting and expresses admiration for Jeok's strength. |
| 적천강 | 사마표 | legendary elder to unorthodox Young Sect Leader | you / young brat | blunt, suspicious, and contemptuous | Jeok addresses Sama Pyo with 네놈 and 어린놈 while probing his lineage and motives. |
| 적천강 | 태산 | legendary elder to giant subordinate | you / strange fellow | blunt, startled, and grudgingly tolerant | Jeok addresses Taishan as 네놈 while reacting to his greeting and appetite. |
| 사마표 | 진태경 | prospective recruit to pavilion master | you | polite, controlled, and candid | Sama Pyo uses 자네 while asking about Taekyung's attitude and admitting his intention to use him. |
| 진태경 | 사마표 | pavilion master to prospective recruit | you / that guy | blunt, informal, and distrustful | Taekyung speaks to and about Sama Pyo with casual forms such as 녀석 and 저놈. |
| 진태경 | 송일섬 | pavilion master to prospective member | Song Ilseom | direct and evaluative | Taekyung directly names Song Ilseom while comparing his qualifications with Hwaran's. |
| 혁무진 | 송일섬 | pavilion_member_to_escort_captain | Great Hero Song | formal and deferential | Mujin addresses Song Ilseom while commenting on his broad experience. |
| 송일섬 | 사마표 | fellow_pavilion_member_to_hostile_fellow_member | you | hostile and casual | Song Ilseom discusses fighting Sama Pyo and answers him while preparing to move away. |
| 사마표 | 송일섬 | fellow_pavilion_member_to_hostile_fellow_member | you | controlled and antagonistic | Sama Pyo responds to Song Ilseom's accusations and proposes moving aside to fight. |
| 혁무진 | 태산 | pavilion_member_to_pavilion_member | you / hey | casual and coaxing | Hyuk Mujin calls after Taishan and offers jerky to persuade him to travel together. |
| 태산 | 혁무진 | pavilion_member_to_pavilion_member | you | clipped and dismissive | Taishan tells Hyuk Mujin not to follow, then accepts him as a friend after hearing about the jerky. |
| 진태경 | 태산 | pavilion_master_to_pavilion_member | Taishan | forceful and commanding | Taekyung orders Taishan to stop eating the bear. |
| 태산 | 주화란 | Pavilion member to Pavilion member | Young Lady Ju | clipped, childlike, and deferential | Agrees with Ju Hwaran after she mentions the evening banquet. |
| 주화란 | 태산 | pavilion_member_to_pavilion_member | Young Hero Taishan | formal but stern | Ju Hwaran reprimands Taishan for speaking ominously about Jin and warns that she will muzzle him. |
| 혁무진 | 주화란 | Fire Dragon Pavilion member to fellow member | Young Lady Ju | polite and deferential | Mujin addresses Hwaran as 주 소저 while asking her to call a physician. |
| 주화란 | 적천강 | younger ally to legendary martial master | Great Hero Jeok | formal and deferential | Ju Hwaran addresses Jeok as 적 대협 while asking whether he is all right. |
| 진태경 | 황제 | guest of the Emperor’s younger brother addressing the Emperor | Your Majesty | formal and deferential in address, despite blunt challenges | Taekyung repeatedly addresses the Emperor as 폐하. |
| 소교 | 진태경 | palace attendant addressing a martial artist and guest under escort | Young Master Jin | formal and respectful, but firm | Addresses him as 진 공자 while escorting him and warning him not to investigate. |
| 진태경 | 소교 | palace attendant and martial artist under imperial scrutiny | you | formal-polite, controlled and challenging | Taekyung addresses So Gyo as 당신 while questioning her presence and demanding an explanation. |
| 신의 | 주화란 | senior physician to younger ally | Young Lady Ju | warm and teasing | The Divine Physician lightly teases Hwaran about being more worried for Jin than he is. |
| 황제 | 진태경 | Emperor addressing a subject and Prince Shangshan’s guest | Jin Taekyung | formal and authoritative | The Emperor addresses Taekyung by his family and personal name before asking what to do with the two officials. |
| 황제 | 소교 | Emperor questioning a political ally | you | quiet and direct | The Emperor questions So Gyo through Sound Transmission about why she is only watching. |
| 소교 | 황제 | political ally answering the Emperor | Your Majesty | calm and direct | So Gyo answers the Emperor through Sound Transmission without wavering. |
| 신의 | 태산 | senior physician to younger ally | Young Hero Taishan | urgent and respectful | The Divine Physician uses this address while pleading with Taishan to keep moving. |
| 적천강 | 동천마군 | enemies | you | blunt and informal | Jeok Cheongang addresses the Eastern Heaven Demon Lord with hostile familiarity. |
| 동천마군 | 적천강 | enemies | you | informal | The Eastern Heaven Demon Lord speaks to Jeok Cheongang during their duel. |
| 황제 | 동천마군 | former ruler addressing a former subject, now an enemy | you | measured and formal | The Emperor asks why the Demon Lord betrayed his father, the late Emperor. |
| 동천마군 | 황제 | former subject addressing the Emperor, now an enemy | you; you bastards | hostile and contemptuous | He denies ever being loyal to the imperial family and accuses the rulers of betrayal. |
| 동천마군 | 소교 | enemies | you; you woman | hostile and demanding | He demands that So Gyo reveal her identity. |
| 소교 | 동천마군 | enemies | you | casual, taunting, and threatening | She warns him to stop and taunts him about whether suicide would still kill him. |
| 진태경 | 동천마군 | young martial artist confronting an enemy | ugly-ass big bro | casual, profane, and taunting | Jin calls out to the Demon Lord after returning to the hall. |
| 동천마군 | 진태경 | enemy recognizing the spear wielder | Jin Taekyung | shouted, informal | The Demon Lord cries Taekyung's name after identifying him as the spear's owner. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 921
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Eastern Heaven Demon Lord.md

# Eastern Heaven Demon Lord (동천마군)

- **Safe through:** Chapter 921
- **Aliases:** None
- **Role:** The Eastern Heaven Demon Lord is a former Maoshan Sect disciple who commands the dead with a bell and has spent half a century infiltrating the imperial court while building a far-reaching rebellion.
- **Personality:** His hatred of rulers is rooted in the loss of his family to the violence of the age of chaos and the destruction of the Maoshan Sect, where he had found happiness.
- **Voice:** He speaks in measured, almost lyrical phrasing, recounting the past before turning to pointed accusations.
- **Relationships:** Ma Sanbao is his Disciple; he holds the Emperor responsible for Taizu’s actions against the Maoshan Sect.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 912
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and an active member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented; despite being naturally fearful, he faces danger and remains loyal to the person he serves, with irreverent self-deprecation and a taste for glory. He is suspicious of Taekyung, bluntly critical of the family's disgraced third son, and an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; with Taekyung, blunt and occasionally incredulous, while using breezy, irreverent banter to defuse tense situations.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad; he regards Taekyung as the person who has repeatedly saved him and now believes he may be able to save Taekyung in turn. As a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Fire Dragon Pavilion members accompanying Taekyung. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 921
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; believes there is no absolute justice and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He deeply trusts Jin Taekyung, his publicly acknowledged second Disciple and intended heir; warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, remains Peng Cheolhu's rival, and is the target of an attack by the assassin Heaven's Slaughter.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 921
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader.
- **Personality:** Hungry, self-aware, dryly observant, and pragmatic under pressure; accepts extreme personal risk when duty and the lives of others demand it.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; So Gyo says he is the chosen one spoken of by the Martial God, while her allegiance remains unknown.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 921
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Ju Hwaran.md

# Ju Hwaran (주화란)

- **Safe through:** Chapter 912
- **Aliases:** Hwaran
- **Role:** Ju Hwaran is a Level 88 Young Bureau Head, leader of the Yongbong Escort Bureau, an experienced Nanman guide, and an active member of the Fire Dragon Pavilion.
- **Personality:** Intelligent, capable, responsible, and filial; remains controlled under pressure but has grown more assertive and openly impatient after the hardships she has endured.
- **Voice:** Clear, polite, restrained, and determined.
- **Relationships:** Escort King Ju Gongsan was her paternal grandfather, Ju Hogun is her father, Heo Jun was her uncle, Sama Pyo was her former fiancé in a political engagement she accepted for her father's sake, Song Ilseom is her direct escort who accompanied her previous journey to Yeongin, and Jin Taekyung is a trusted ally; the Yongbong Escort Bureau has longstanding ties with Yeongin’s inhabitants.

### Martial God.md

# Martial God (무신)

- **Safe through:** Chapter 921
- **Aliases:** None
- **Role:** An unidentified legendary martial artist regarded as a pinnacle above the Ten Kings; more than fifty years ago, he defeated five Supreme Peak fiends and five hundred Blood Ghost Squad members alone.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** He met the Beast Miao King twice more than fifty years ago, appearing first as a white-bearded elder and later as a young boy; Mae Jonghak received several teachings from him, while his identity, whereabouts, and possible connection to Cheon Taemin remain unknown.

### Sama Pyo.md

# Sama Pyo (사마표)

- **Safe through:** Chapter 909
- **Aliases:** Black Dragon Saber
- **Role:** Young Sect Leader of the Black Dragon Demon Gate, a Morning Star reputed to be no less than the Ten Dragons and Phoenixes, and a member of the Fire Dragon Pavilion.
- **Personality:** Outwardly courteous and smiling, inwardly calculating, but genuinely protective of Taishan; in combat he is ruthlessly pragmatic, survival-focused, and unafraid to stake his life.
- **Voice:** Polite and ingratiating in public, with sardonic humor and controlled evasiveness.
- **Relationships:** Sama Pyo commands the absolutely loyal Taishan, is Sima Gong's son, was Ju Hwaran's former fiancé in a political engagement, and has joined the Fire Dragon Pavilion while openly intending to use Jin Taekyung as a useful card; he is now openly hostile toward fellow member Song Ilseom.

### So Gyo.md

# So Gyo (소교)

- **Safe through:** Chapter 921
- **Aliases:** None
- **Role:** So Gyo is the Bow Saint, a Supreme Peak master and palace attendant assigned to Prince Shangshan, whose two curved swords can join into their original bow form.
- **Personality:** Calm, calculating, and self-possessed; she conceals her strength and identity and can be openly taunting.
- **Voice:** Measured and composed, shifting from deferential formality to casual, pointed taunts and threats.
- **Relationships:** So Gyo recognizes Jin Taekyung as the chosen one spoken of by the Martial God; she says only she and the Emperor know a secret she withheld from Baek Yeon, while her true allegiance remains unknown.

### Song Il.md

# Song Il (송일)

- **Safe through:** Chapter 909
- **Aliases:** Roaring Fury Swordsman
- **Role:** Elder of the Zhongnan Sect and the Roaring Fury Swordsman; senior brother of Sect Leader Gong Iljung; came to the Jin Family of Taiyuan to demand redress for Gong Ilhyuk's injury and the alleged insult to Zhongnan; attacked Jin Taekyung with the Heavenly River Thirty-Six Swords, was stopped by Jeok Cheongang, and was publicly humiliated by him.
- **Personality:** Arrogant, domineering, punitive, and confident in his martial power and seniority.
- **Voice:** Gruff, cutting, condescending, and threatening, with formal authority used to pressure those beneath him.
- **Relationships:** Gong Iljung is his junior Sect Leader and martial younger brother; Gong Ilhyuk is a junior Disciple of his sect; he recognizes Baek Museong and Cheongpung through their Huashan and Sword Saint connections.

### Song Ilseom.md

# Song Ilseom (송일섬)

- **Safe through:** Chapter 909
- **Aliases:** Escort Captain Song
- **Role:** Level 110 young escort captain of the Yongbong Escort Bureau, one of its Dragon-Phoenix Three Escorts, and a newly accepted member of Jin Taekyung and Cheongpung’s Fire Dragon Pavilion; he is currently bound and unconscious under the reconnaissance squad's guard after being struck at a Sleep Acupoint.
- **Personality:** Blunt, decisive, survival-hardened, and dryly self-aware, with little patience for insults or disorder and practical survival skills such as making disguise masks.
- **Voice:** Forceful and urgent in command, with a rough and confrontational edge.
- **Relationships:** He serves under Ju Hwaran and has expressed concern that she not be hurt or die needlessly; he is Song Pyosan’s son, his grandmother was the surviving Guangdong Chen child rescued by Ju Gongsan during the Great Faction War, and he remains openly hostile toward fellow Fire Dragon Pavilion member Sama Pyo.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 913
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo; becomes explosively violent when his meat is threatened.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord, trusts Jin Taekyung as Pavilion Master, and has grown attached to the Fire Dragon Pavilion members.

## Korean source

```text
＃922화



수많은 생명체가 가득한 세상 속에서 인간이 유독 특별한 존재로 보이는 이유는, 깊고 넓은 사고(思考)가 가능하기 때문이다.

인간이라면 누구나 그렇다.

현재 처한 상황을 눈과 귀로 파악하고, 눈앞의 상대에게 어떤 행동을 해야 하는지, 어떤 말을 내뱉어야 하는지 머릿속에서 생각하고 적절한 단어를 조합한다.

동시에 지금의 이 언행으로 일어날 일들을 예측한다.

그러나 이러한 예측이 언제나 맞아떨어지는 것은 아니다.

주위 상황이 예상치 못한 방향으로 흘러갈 때, 대화하는 상대의 반응이 완전히 엇나갈 때 인간은 당황한다.

팽팽 돌아가던 머릿속이 멈추고, 할 말을 잃어버리고 만다.

바로 지금의 나처럼.

“그래, 너였구나.”

소교, 아니 궁성(弓星)이 나를 물끄러미 바라보았다. 달싹이는 그녀의 입술 사이로 오직 나만이 들을 수 있는 목소리가 흘러나왔다.

- 무신(武神)께서 말씀하셨던, 선택받은 자가.

……뭐?

소교의 정체가 궁성이라 불리는 거인이었다는 것에서 받은 충격은 이제 어디에서도 찾아볼 수 없다.

마치 쇠망치처럼 뒤통수를 후려치는 듯한 그 짤막한 전음(傳音)에, 나는 멍하니 눈을 깜빡였다.

변명이라도 할 줄 알았다.

분노를 숨기지 않고 드러내는 내게 이렇게 될 줄 몰랐다며, 피치 못할 사정이 있었다며 이야기를 꺼낼 줄 알았다.

하지만 아니었다.

무신.

그리고 선택받은 자.

조금도 예측하지 못한 그 단어의 조합과 알 수 없는 의미에 석상처럼 굳어 있던 그때, 궁성의 전음이 이어졌다.

- 그래, 혼란스럽겠지. 오래전의 나 또한 그랬으니까.

오래전이라니. 도대체 언제를 말하는 것일까.

이미 아득한 과거 속에 종적를 감춘 무신은, 과연 그녀에게 어떤 말을 전한 것일까.

그러나 순간 머릿속을 스친 그 의문을, 나는 시작과 동시에 접어야만 했다.

- 홀로 간직해 왔던 긴 이야기다. 다만 지금 이 자리에서 대화를 나누는 건 그리 현명한 선택이 아니겠지.

당장이라도 캐묻고 싶은 마음이 굴뚝 같았지만, 궁성의 전음은 내가 잠시나마 잊고 있던 현재의 상황을 일깨워 주기에 충분했다.

맞다.

오늘 이 자리에서 벌어진 거대한 혈투는 끝났지만, 아직 모든 것이 끝난 건 아니다.

공연의 막이 내려도 커튼콜(Curtain call)이 남아 있듯이.

이 핏물에 잠긴 무대에 오른 배우들에게는 각자의 역할이 남아 있었다.

‘대답을 듣는 건 그다음이겠지.’

나는 고개를 끄덕였고, 그 행동에 담긴 의미를 알아들은 궁성은 조용히 돌아섰다.

줄곧 옆에서 이 모든 상황을 말없이 지켜보던 한 사람을 향해 스치듯이 힐끗 시선을 던지며.

“어째 저 할망구는 여전하군. 아니, 오히려 회춘하더니 눈빛이 더 기분 나빠졌어.”

혼잣말처럼 작게 중얼거린 적천강이 덧붙였다.

“감히 노부의 면전에서 어느 핏덩이 같은 놈에게 전음으로 장난질이나 치고 말이야.”

“…….”

“왜, 모를 줄 알았더냐?”

나는 뺨에 말라붙은 피딱지를 뜯어내며 대답했다.

“알고 계실 것 같긴 했습니다. 만에 하나 모르셨더라도 제가 먼저 말씀드렸을 거고요.”

“말은 청산유수로군.”

“그래서, 전부 엿들으신 겁니까?”

“궁성이라는 별호가 옆집 개똥이로 보이느냐?”

“그럼 말씀드리겠습니다. 토씨 하나 안 빼놓고 전부 다.”

물끄러미 나를 바라보던 적천강이 문득 혀를 찼다.

“됐다. 서두를 것도 없고, 필시 그럴 만한 이유가 있었겠지. 그보다…….”

툭툭.

단단한 손바닥이 내 어깨를 두드린다. 휙 고개를 돌린 적천강의 옆모습에서 퉁명스러운 목소리가 흘러나왔다.

“거, 뭐야, 흠.”

“예?”

“아니, 그러니까. 노부가 하고 싶은 말은…… 어어, 이놈 보게, 웃어?”

어느샌가 나도 모르게 실소가 흘러나온 모양이다.

하지만 예전처럼 황급히 입가에 맺힌 웃음을 지우진 않았다.

적천강이 어떤 마음인지 아니까. 이 웃음에 담긴 내 마음 역시 고스란히 그에게 전해질 테니까.



‘고맙다. 이렇게 돌아와 주어서.’



불과 조금 전 내가 사경을 헤맬 때, 마침내 죽음을 딛고 회복하여 돌아왔을 때 적천강이 해 주었던 말이다.

더불어 이제는 내가 그에게 돌려주어야 말이기도 하다.

“감사합니다. 언제나 제 옆에 계셔 주셔서.”

들릴 듯 말 듯 한 목소리로 작게 중얼거린 나는 짐짓 허공을 바라보며 딴청을 피웠다.

조금은 낯간지럽기도 하고, 한편으로는 적천강의 반응을 볼 자신도 없었다.

하지만…… 글쎄, 때로는 이런 말을 하고 싶을 때가 있다.

더 이상 구구절절한 말이 필요 없는 사이라 해도, 순수하게 진심을 전하고 싶을 때가.

그리고 적어도 그런 부분에 있어서만큼은, 적천강은 그 강대한 무위에 비해 한참이나 서투른 사람이었다.

“크흠. 큼. 털 숭숭 난 놈이 무슨 그런 흉측한…….”

괜한 헛기침과 함께 머뭇거리던 적천강이 문득 피식 웃었다. 그의 손가락이 향하는 방향 끝에, 빠르게 가까워지는 일단의 무리가 있었다.

“노부야 당연한 거고, 감사 인사는 저 녀석들한테나 해라. 네놈 하나 구하겠다고 사지(死地)에 뛰어들었으니 그 정도 공치사는 받아야 하지 않겠느냐?”

고개를 돌린 내 시야에, 머리부터 발끝까지 핏물을 흠뻑 뒤집어쓴 채 허겁지겁 달려오는 익숙한 얼굴들이 담겼다.

하나, 둘, 셋…… 여섯.

모두 살아남았다. 한 사람도 빠지지 않고 무사히.

그것으로 됐다. 더할 나위 없이 충분했다.

‘아.’

무한한 안도감 때문일까. 아니면 잊었던 피로감 때문일까.

찰나의 순간 전신의 맥이 탁 풀린 나는 그대로 비틀거리며 쓰러졌다.

아니, 쓰러질 뻔했다.

만약 사방에서 뻗어 나온 다급한 손길이 나를 붙들지 않았다면, 분명 그랬을 것이다.

덥석.

적천강이, 혁무진이, 주화란과 송일섬, 사마표와 태산, 그리고 신의가 내 팔과 다리를 붙잡는다. 금방이라도 기울어질 듯한 몸뚱어리를 지탱한다.

무거운 짐이 아니라, 견고한 기둥이 되어.

조금이라도 도움이 되기를 바라며 이 사지로 돌아왔을 그들 한 사람 한 사람은, 내게 이 참혹한 전투에서 승리해야만 하는 가장 큰 이유가 되어 주었다.

“빌어먹을. 이 멋있는 순간에 한 손 보태야 하는데, 이놈 키가 너무 커서 도무지 손이 안 닿는군.”

태산의 어깨에 올라탄 늙은 은영각 요원의 서글픈 한 마디에, 모두가 너나 할 것 없이 실소를 흘렸다.

당장이라도 쏟아지는 수마(睡魔)에 눈을 감을 뻔했던 나조차도.

‘안 되지. 아직은 안 돼.’

나는 이를 악물며 허물어지려던 전신에 힘을 불어넣었다. 그리고 모두의 걱정 어린 눈빛을 뒤로한 채 걸음을 옮겼다.

이 지옥 같았던 밤을 끝내기 위해.

그 어떤 화공도 그릴 수 없는 끔찍한 지옥도(地獄道)를 만들어 낸 괴물을 끝장내기 위해.

저벅. 저벅.

걷고, 또 걸었다.

굵은 쇠사슬에 꽁꽁 묶여 발버둥 치는 망자들과 반란군들을 지나.

높게 솟아오른 수십여 개의 깃발을 바라보며.

마침내 어떤 저항이나 비명도 들리지 않는 이 광활한 공간 속, 궁성의 발치에서 홀로 몸부림치는 괴물의 모습이 보일 때까지.

“동천마군(東天魔君).”

내 부름에, 괴물의 움직임이 우뚝 멈췄다.



* * *



진태경의 나직한 목소리가 귓가에 닿은 그 순간, 동천마군은 전신의 모든 힘이 풀리는 것을 느꼈다.

이유?

자신도 몰랐다.

어쩌면 그 상대가 바로 진태경이기에, 흐름을 바꿀 수 있는 매 순간의 전환점에서 그를 가로막은 장본인이기에 그랬을 수도 있었다.

혹은 줄곧 말없이 지켜만 보던 궁성이 아닌 다른 누군가가, 자신을 멈춰 주기를 기다렸는지도 몰랐다.

이 의미 없는 몸부림을.

더는 목적을 이룰 수 없게 된 이 허탈감과 분노를.

“그래, 자네로군.”

한바탕 용암을 토해 낸 화산은 머지않아 차갑게 식는다. 바로 지금의 동천마군이 그랬다.

“늦었어. 사람을 이리 오랫동안 기다리게 하는 건 예의가 아니지.”

담담한 그의 모습을 말없이 내려다보던 진태경이 입을 열었다.

“글쎄, 너처럼 죽지도 않는 괴물은 해당 사항이 없을 텐데.”

“괴물이라, 역시 그런가?”

“그렇지. 그리고 정확히 짚고 넘어가자면, 나는 사람한테도 딱히 예의를 지키는 편이 아니야.”

“아, 태생부터 예의가 없었군.”

“지금 그 말, 우리 엄마 앞에서 했으면 맞아 죽었을걸.”

“조금 전에 노부더러 죽지도 않는 괴물이라고 하지 않았나?”

“엄마신장은 영혼을 때리는 거야. 몸이 아니라.”

동천마군은 자신도 모르게 너털웃음을 터트렸다.

“무슨 이야기인지 알 것 같군. 일리가 있어.”

한때는 그에게도 어머니라는 존재가 있었다.

평소에는 다정다감하다가도, 잘못을 저지르면 호된 질책과 함께 등을 얻어맞고는 했다.

오랜 세월이 흐른 지금에서조차, 그때의 아픔은 아스라이 남아 있었다.

“그래, 기억나는군. 분명 내게도 그럴 때가 있었지. 스승님도 평소에는 온화하신 분이었지만 종종 회초리를 드시곤 했어.”

그러나 즐거운 옛 기억을 떠올릴수록, 동천마군의 입가에 걸려 있던 미소가 서서히 흐릿해졌다.

“그런데…… 이제는 기억이 안 나.”

한때는 그 모든 것이 현재였다.

오늘이었고, 어제였다.

하지만 이제 그의 기억 속에 남아 있는 그들의 모습은, 고통으로 끔찍하게 일그러진 얼굴들뿐이다. 죽거나 혹은 죽어 가는 광경뿐이다.



‘이놈들! 이 천벌을 받을 놈들!’

‘가거라, 어서!’



참으로 알 수 없는 일이었다.

유일하게 남은 자식을 지키기 위해 저항하다 병사들에게 유린당한 어머니의 찢어지는 비명은, 스승님의 마지막 당부는 이토록 생생한데 어찌 그들의 웃는 얼굴은 이토록 흐릿한 것인지.

온통 안개에 휩싸인 것처럼 희뿌연 것인지.

까드득.

동천마군이 어찌나 강하게 이를 악물었는지, 그의 어금니가 산산이 부서졌다.

그러나 당연하게도, 응당 찾아와야 할 고통은 없었다.

그저 부서졌다는 결과만이 있을 뿐이었다.

비명에 죽어 간 그의 주위 사람들이 그러했듯이.

그가 스스로의 선택으로 인간에서 괴물이 되었듯이.

“그거 알고 있나?”

피에 젖은 입술이 달싹인다. 진태경과 궁성을 비롯하여 어느덧 주위를 둘러싼 수많은 이들을 바라보는 동천마군의 두 눈동자는, 차가운 불꽃으로 일렁이고 있었다.

“이건 시작에 불과하다.”

그는 씹어 뱉었다.

한 음절, 한 음절에 분노를 담아.

세상에 대한 원망과 더는 행복해질 수 없는 자신에 대한 슬픔을 삼키며.

“황도(皇都)를 지켰다 해도, 천하 곳곳으로 번지는 불길은 어쩌지 못할 것이다.”

반세기가 넘는 세월을 황실에 몸담았다. 그의 넓은 그늘에 잠시 몸을 의탁하지 않은 자가 없고, 암천의 손이 닿지 않은 자가 없다.

그렇게 황도라는 거대한 우물을 벗어난 개구리들은, 저마다의 관직을 받아 천하 각지로 퍼졌다. 새로운 뿌리를 내리고 가지와 열매를 틔웠다.

그렇기에 동천마군은 웃을 수 있었다.

머지않아 거대한 내전과 화마에 휩싸일 대국을 생각하며. 그 불길을 앞세워 중원으로 향할 암천의 군세(軍勢)를 떠올리며.

“그날, 대국은 멸망하리라.”

동천마군은 앙천대소(仰天大笑)를 터트렸다.

어느새 자신의 앞에 선 한 사람을 바라보며. 아무것도 할 수 없는 무력함을 느낄 황제를 비웃으며.
```

## Final English reading copy

```markdown
# Chapter 922

What made humans seem so special in a world teeming with countless living things was their ability to think deeply and broadly.

That was true of every human being.

They took in their current situation through their eyes and ears, thought about what to do or say to the person in front of them, and put together the right words.

At the same time, they predicted what would happen because of their words and actions.

But those predictions didn’t always come true.

When the situation around them took an unexpected turn, or the person they were talking to reacted in a way they hadn’t anticipated, humans were thrown off.

Their minds, spinning at full speed, came to a halt. They lost all sense of what to say.

Just like I was right now.

“So it was you.”

So Gyo—no, the Bow Saint—stared at me. Her lips moved, and a voice only I could hear slipped between them.

*—The one the Martial God spoke of. The chosen one.*

…What?

The shock of learning that So Gyo was the giant known as the Bow Saint had completely disappeared.

Those few words, transmitted like a hammer blow to the back of my head, left me blinking blankly.

I’d expected an excuse, at least.

I thought she’d explain that she hadn’t expected things to turn out this way, that she’d had no choice—especially since I wasn’t hiding my anger.

But she didn’t.

The Martial God.

And the chosen one.

As I froze like a statue at that utterly unexpected combination of words and their incomprehensible meaning, the Bow Saint’s Sound Transmission continued.

*—Yes, you must be confused. I was, too, a long time ago.*

A long time ago? Just when was she talking about?

What had the Martial God, who had vanished into the distant past, told her?

But the question that flashed through my mind was cut short before it could even take shape.

*—It’s a long story I’ve kept to myself. But this isn’t the best place to talk.*

I desperately wanted to press her for answers, but the Bow Saint’s Sound Transmission was enough to remind me of the situation I’d momentarily forgotten.

Right.

The massive bloodbath that had unfolded here today was over, but that didn’t mean everything was finished.

Just as a curtain call still follows when the curtain falls on a performance.

The actors on this blood-soaked stage still had parts to play.

*I’ll get my answers after that.*

I nodded. The Bow Saint understood what I meant and quietly turned away.

Her gaze flicked toward the one person who’d stood beside us all along, watching everything in silence.

“That old hag’s still the same. No, she’s even more irritating now that she’s gotten younger. Her eyes are worse than before.”

Jeok Cheongang muttered it under his breath, then added, “And playing games with some young punk through Sound Transmission right in front of me, too.”

“……”

“What? You think I wouldn’t notice?”

I peeled a crust of dried blood off my cheek and answered, “I figured you’d know. And even if you didn’t, I would’ve told you myself.”

“You sure know how to talk.”

“So, did you hear everything?”

“Do you take the title Bow Saint for the name of the dog next door?”

“Then I’ll tell you. Every last word. I won’t leave out a single syllable.”

Jeok Cheongang stared at me for a moment, then clicked his tongue.

“Forget it. There’s no rush. She must have had her reasons. Anyway…”

*Pat. Pat.*

His sturdy palm tapped my shoulder. Jeok Cheongang quickly turned his head away, and his gruff voice came from his profile.

“Uh, well. What I’m trying to say is… hmm.”

“Yes?”

“No, I mean. What this old man wants to say is… Hey, look at you. Are you laughing?”

At some point, a laugh must have slipped out of me.

But I didn’t hurriedly wipe the smile from my lips like I used to.

I knew how he felt. And he’d understand what I was feeling, too.

*Thank you. For coming back to me.*

That was what Jeok Cheongang had said just a little while ago, when I’d been hovering between life and death, after I finally clawed my way back from death and recovered.

And now it was my turn to say it back to him.

“Thank you. For always staying by my side.”

I murmured so quietly he could barely hear, then pretended to be distracted by something in the air.

It was a little embarrassing. And I wasn’t sure I could handle seeing his reaction.

But… well. Sometimes you just want to say something like that.

Even when you’re close enough that you don’t need long explanations, there are times when you simply want to speak from the heart.

And in that regard, at least, Jeok Cheongang was far clumsier than his immense martial prowess would suggest.

“Ahem. Ahem. What’s with that creepy stuff coming from a hairy bastard like you…”

He hesitated, clearing his throat for no good reason, then suddenly gave a quiet laugh. At the end of the direction his finger pointed, a group of people was rushing closer.

“This old man’s a given. Save your thanks for those guys. They threw themselves into a deathtrap just to save you. They deserve at least that much praise, don’t they?”

I turned my head. Familiar faces came into view, hurrying toward me with blood covering them from head to toe.

One, two, three… six.

Every one of them had survived. Not a single person was missing.

That was enough. More than enough.

*Ah.*

Was it the overwhelming relief? Or the exhaustion I’d forgotten about?

In an instant, all strength left my body. I staggered and began to fall.

No—I nearly fell.

If a flurry of hands hadn’t reached out from every side to catch me, I certainly would have.

*Grab.*

Jeok Cheongang, Hyuk Mujin, Ju Hwaran, Song Ilseom, Sama Pyo, Taishan, and the Divine Physician caught my arms and legs. They held up my body as it threatened to tip over.

Not like a heavy burden, but like sturdy pillars.

Every one of them had come back to this deathtrap, hoping they could help even a little. Each of them had become the greatest reason I had to win this horrific battle.

“Damn it. I should be lending a hand in this awesome moment, but this guy’s so tall I can’t even reach him.”

At the mournful remark from the old Hidden Shadow Pavilion agent perched on Taishan’s shoulder, everyone let out a quiet laugh.

Even I, who’d nearly closed my eyes against the sleep demon washing over me.

*No. Not yet.*

I clenched my teeth and forced strength back into my crumbling body. Then, ignoring the worried looks around me, I started walking.

To bring this hellish night to an end.

To finish off the monster who had created a hellscape no painter could ever depict.

*Clop. Clop.*

I walked, and kept walking.

Past the dead and the rebels, bound tight in thick iron chains and struggling to break free.

Looking toward the dozens of flags rising high into the air.

Until, at last, in that vast space where not a single protest or scream could be heard, I saw the monster writhing alone at the Bow Saint’s feet.

“Eastern Heaven Demon Lord.”

At my call, the monster’s movements stopped abruptly.

* * *

The moment Jin Taekyung’s low voice reached his ears, the Eastern Heaven Demon Lord felt all the strength leave his body.

Why?

He didn’t know.

Maybe it was because the man before him was Jin Taekyung—the one who had stood in his way at every turning point, every moment when the course of events might have changed.

Or maybe he’d been waiting for someone other than the Bow Saint, who had watched in silence all this time, to stop him.

To stop this meaningless struggle.

This hollow sense of defeat and fury, now that he could no longer achieve his goal.

“Yes, it’s you.”

A volcano that had spewed lava soon cooled. The Eastern Heaven Demon Lord was the same now.

“You’re late. It’s rude to keep someone waiting this long.”

Jin Taekyung looked down at him in silence, then spoke.

“Well, I don’t think that applies to an immortal monster like you.”

“A monster, is it? So that’s how it is?”

“Right. And to be precise, I’m not exactly big on manners even with people.”

“Ah. So you were born rude.”

“If you’d said that in front of my mom, she would’ve beaten you to death.”

“Didn’t you just call me a monster who wouldn’t die?”

“Mom’s Divine Palm hits your soul. Not your body.”

The Eastern Heaven Demon Lord let out a hearty laugh before he could stop himself.

“I think I know what you mean. That makes sense.”

Once, he’d had a mother, too.

She was gentle most of the time, but when he did something wrong, she’d scold him harshly and smack him on the back.

Even after all these long years, the pain of it still lingered faintly.

“Yes, I remember. I had times like that, too. My Master was usually gentle, too, but sometimes the switch would come out.”

But the more he recalled those happy memories from long ago, the fainter the smile on the Eastern Heaven Demon Lord’s lips became.

“But… now I can’t remember.”

Once, all of that had been the present.

It had been today, and yesterday.

But now, the only faces left in his memory were twisted hideously with pain. Only the sight of them dying, or already dead.

*“You bastards! You’ll be cursed for this!”*

*“Go! Hurry!”*

It was strange.

His mother’s piercing scream as the soldiers brutalized her while she fought to protect her only surviving child, and his Master’s final words—those memories were so vivid. So why were their smiling faces so faint?

Why were they all blurred, as if hidden in fog?

*Crack.*

The Eastern Heaven Demon Lord clenched his teeth so hard that his molars shattered.

But, naturally, the pain that should have followed never came.

Only the result remained: they were broken.

Just as the people around him had died screaming.

Just as he had chosen to become a monster instead of a human being.

“Do you know something?”

His lips, wet with blood, moved. His eyes, fixed on Jin Taekyung, the Bow Saint, and the countless people who had gathered around him, flickered with cold flames.

“This is only the beginning.”

He spat out the words.

Each syllable was filled with anger.

He swallowed his resentment toward the world—and his grief at knowing he could never be happy again.

“Even if you’ve protected the imperial capital, you can’t stop the fires spreading throughout the land.”

He had served the imperial family for more than half a century. There wasn’t a single person who hadn’t taken shelter beneath his vast shadow, and not one of them was beyond Dark Heaven’s reach.

The frogs who had escaped the vast well of the imperial capital had each received an official post and spread throughout the land. They’d put down new roots, growing branches and bearing fruit.

That was why the Eastern Heaven Demon Lord could smile.

Thinking of the Great Nation, soon to be swept up in a massive civil war and firestorm. Thinking of the Dark Heaven forces that would use those flames to march into the Central Plains.

“That day, the Great Nation will fall.”

The Eastern Heaven Demon Lord threw his head back and laughed.

He looked at the man standing before him, mocking the Emperor, who would feel helpless to do anything.
```

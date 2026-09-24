<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0996.txt",
      "sha256": "fc26c5a1e4ae85236cfe49b4c041c5382dd353c6dc13f707dbc446db0e43f4e3",
      "bytes": 13178
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "9b8eef6fb2d583b5fc47540815c164843cf993be7a420f4a44b592a7f4557fc3",
      "bytes": 1571
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "d13308fe31a2c64daebd8b79b1737ef2a4f6a2f6e86338670363f6d7acf5174f",
      "bytes": 236719
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "cb1d2d3d5df678e1ee49e85f0f8efbb22cfe2e3d4f40e5b234aa32ca2f8d3a8d",
      "bytes": 759
    },
    {
      "path": "characters/Heavenly Power Demon.md",
      "sha256": "e78c307596b173a2bddf1a084919abfc5496b85252ab2edc2fb9eb92a68a3ff8",
      "bytes": 993
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "9ac984bb68185d6a06cdabbe2fa8eca0afae178a541bc19ca2e2fbb164829f12",
      "bytes": 1374
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "fbdce9ab8ed4ed4d3abc3c4abf703d6444c868840fac3e5c1b5425dab51fc206",
      "bytes": 1613
    },
    {
      "path": "characters/Jin Wikyung.md",
      "sha256": "e2ebd06d8c67817efd87cc481b00a02195b8596567bc65148d93326bd68031c4",
      "bytes": 1178
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "f39e9cfbee5931db943ab94ac0dae5cde4feb6528b81bc6d1e6a8e5fd45653bc",
      "bytes": 622
    },
    {
      "path": "characters/Namho.md",
      "sha256": "e3c17332961418fdcde0a9bf51a78cf3b58a70b8a8885aef013ce764e66a7c2c",
      "bytes": 1091
    },
    {
      "path": "characters/Peng Cheolhu.md",
      "sha256": "a7a756b55455adac312d7d20ee41bf4af132d7bcb1ed08ecbb3603eac7932fbf",
      "bytes": 1001
    },
    {
      "path": "characters/Sama Pyo.md",
      "sha256": "8844f266a773bb1833462d622a084a636cfcdd29c8f4d6e969ea2b9cab5959db",
      "bytes": 936
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "4a967fd58039333e55493d03c66a6f37ddf0dd845d4678dace10bc013b135740",
      "bytes": 685
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "bd5753e5df794eedf5b2ea27975a392475eb9bba5427ebd9beecb42050b7771b",
      "bytes": 273611
    }
  ],
  "estimated_tokens": 13146
}
-->

# Durable State Update — Chapter 996

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
1 and safe_through 996. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 996. Profile updates may replace only one
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
  "chapter": 996,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 996,
    "continuity_sources": [996],
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
    "Taekyung has fully opened his Middle Dantian, reached the Supreme Peak realm, completed Bone Transformation, and absorbed internal energy passed on by the Heavenly Power Demon and Peng Cheolhu.",
    "Taekyung is resolved to help bring about the peace the dead wanted and aspires to reach the upper dantian.",
    "Taekyung suspects the Martial God may have been a System user and may be connected to the unknown voice; these remain unconfirmed.",
    "Logout remains disabled following a System error. Taekyung wonders whether the restriction is connected to Xinjiang, without confirmation.",
    "Dark Heaven’s stronghold in Xinjiang is showing unprecedented activity. More than thirty Hidden Shadow Pavilion agents are reported dead, contact has been lost, and the enemy may number more than a hundred thousand.",
    "Taekyung and the Fire Dragon Pavilion have decided to head west. Their decision triggers a new Quest alert; its objective is unknown."
  ],
  "continuity_sources": [
    995
  ],
  "open_questions": [
    "Who was the unknown voice, and will Taekyung meet its owner?",
    "Was the Martial God a System user, and is he connected to Cheon Taemin?",
    "What did the Doppelganger mean by its final words, and what was it trying to accomplish?",
    "What is Dark Heaven planning in Xinjiang, and how strong and numerous are its forces?",
    "What is the objective of the newly triggered Quest, and is it connected to Logout being disabled?"
  ],
  "safe_through": 995,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 진위경    | **Jin Wikyung**    |
| 혁무진    | **Hyuk Mujin**     |
| 벽력도왕   | **Thunderbolt Saber King**    | Peng Cheolhu   |
| 태원진가   | **Jin Family of Taiyuan**        |
| 곤륜파    | **Kunlun Sect**                  |
| 무림맹    | **Murim Alliance**               |
| 암천     | **Dark Heaven**                  |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 혈도     | **acupoint** / **vital point**                   | Context dependent                                     |
| 운기조식   | **circulate one's qi**                           | Usually better as a verb than a proper-name technique |
| 마교     | **Demonic Cult**                                 |                                                       |
| 중원     | **Central Plains**                               |                                                       |
| 강호     | **martial world**                                | Prefer “Murim” where the setting itself is meant      |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 경험치              | **EXP**                        |
| 명성               | **Fame**                       |
| 퀘스트              | **Quest**                      |
| 보상               | **Reward**                     |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 감숙     | **Gansu**              |
| 청해     | **Qinghai**            |
| 곤륜     | **Kunlun**             |
| 정마대전   | **Great Faction War**         |
| 귀가      | **your family**                                                 |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 천력마 | **Heavenly Power Demon** | Formerly imprisoned Tang Clan criminal; distinct from 천력부, Heavenly Axe. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 남호 | **Namho** | Hidden Shadow Pavilion code name; literally associated with amber from the south. |
| 사마표 | **Sama Pyo** | Young Sect Leader of the Black Dragon Demon Gate. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 송이 | **Song-i** | Short form used for Song Song; Taekyung's love interest. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 오대세가 | **Five Great Families** | Major Murim grouping. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 일각 | **fifteen minutes** | Quarter of a shichen; used for the remaining completion time. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 은영각 | **Hidden Shadow Pavilion** | Former Murim Alliance intelligence organization. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 천주 | **Lord of Heaven** | Authority invoked by the masked attackers. |
| 겁화 | **hellfire** | Destructive fire energy used by Taekyung. |
| 신력 | **divine strength** | Superhuman strength attributed to Taekyung. |
| 오대 | **Five Squads** | Named Tang Clan organizational group in Tang Sadok's mobilization order. |
| 청해성 | **Qinghai** | Source form specifying Qinghai as a province. |
| 격체전공 | **Transmitting Internal Energy Across the Body** | Technique for transferring internal energy between bodies. |
| 서장 | **Tibet** | Region considered by the Third Fiend as a possible escape route. |
| 기경팔맥 | **Eight Extraordinary Meridians** | The eight extraordinary meridians of wuxia physiology. |
| 새외 | **Outer Lands** | Lands outside the Central Plains and its Murim. |
| 흑룡마문 | **Black Dragon Demon Gate** | Unorthodox faction from Gansu. |
| 공동파 | **Kongtong Sect** | Sect belonging to the Nine Sects and One Gang. |
| 황하 | **Yellow River** | River along which civilization began. |
| 화룡각 | **Fire Dragon Pavilion** | New name chosen for Taekyung's pavilion. |
| 가기 | **singing courtesan** | The favored entertainer identity Honglan used in Hubei. |
| 신강 | **Xinjiang** | Region beyond Qinghai described as the domain of the Demonic Path. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진위경 | younger_to_eldest_brother | brother | familiar-but-respectful | Self-corrects from the personal name to kinship: “Jin Wikyung—I mean, my brother?”; 큰형 is eldest brother. |
| 진위경 | 진태경 | eldest_to_youngest_brother | youngest | affectionate-protective | Uses youngest-brother address; openly affectionate beneath a public mask. |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
| 혁무진 | 진위경 | Jin Family subordinate to Lesser Family Head | Lesser Family Head | deferential | Uses 소가주님 while confessing that he accepted Taekyung's invitation. |
| 진위경 | 혁무진 | Lesser Family Head to direct family subordinate | you | formal-but-familiar | Uses 자네 while recognizing Mujin and instructing him to keep helping Taekyung. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 무인 | 진위경 | vassal_martial_artist_to_lesser_family_head | Lesser Family Head | formal-deferential | The Mount Heng martial artists greet Jin Wikyung as 소가주님 while pledging loyalty. |
| 진태경 | 천력마 | prisoner_feeder_to_prisoner | you | casual and mocking | Taekyung questions the Heavenly Power Demon and mocks him as the Kunlun Sect's public-pissing criminal. |
| 천력마 | 진태경 | prisoner_to_prisoner_feeder | you | gruff and self-possessed | The Heavenly Power Demon speaks of himself as 노부 while questioning Taekyung. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 벽력도왕 | 진태경 | elder martial master to younger rival | you | boisterous and confrontational | Peng addresses Taekyung as 네놈 while discussing Peng Dojin. |
| 사마표 | 태산 | Young Sect Leader to subordinate | Taishan | informal and patronizing | Sama Pyo calls Taishan by name while ordering him to leave. |
| 태산 | 사마표 | subordinate to Young Sect Leader | Lord | crude and deferential | Taishan uses 주군 while obeying Sama Pyo. |
| 태산 | 진태경 | subordinate_to_respected_outsider | Jin Taekyung | clipped and familiar | Taishan says he likes Jin Taekyung but will fight him without hesitation if Sama Pyo commands it. |
| 사마표 | 진태경 | prospective recruit to pavilion master | you | polite, controlled, and candid | Sama Pyo uses 자네 while asking about Taekyung's attitude and admitting his intention to use him. |
| 진태경 | 사마표 | pavilion master to prospective recruit | you / that guy | blunt, informal, and distrustful | Taekyung speaks to and about Sama Pyo with casual forms such as 녀석 and 저놈. |
| 혁무진 | 태산 | pavilion_member_to_pavilion_member | you / hey | casual and coaxing | Hyuk Mujin calls after Taishan and offers jerky to persuade him to travel together. |
| 태산 | 혁무진 | pavilion_member_to_pavilion_member | you | clipped and dismissive | Taishan tells Hyuk Mujin not to follow, then accepts him as a friend after hearing about the jerky. |
| 남호 | 진태경 | Hidden_Shadow_Pavilion_agent_to_mission_leader | Jin Taekyung / you | guarded and familiar | Namho addresses Taekyung as 자네 while explaining the contact and offering guidance. |
| 진태경 | 남호 | mission_leader_to_hidden_shadow_agent | you / Namho | probing and respectful | Taekyung questions Namho’s affiliation and later discusses Dark Heaven’s threat to Nanman. |
| 남호 | 혁무진 | hidden_shadow_agent_to_pavilion_member | you there / Han bastard | performatively hostile and abusive | Namho attacks Mujin and insults him to make the meeting appear to be a genuine expulsion. |
| 혁무진 | 남호 | pavilion_member_to_hidden_shadow_agent | old man | indignant and insulting | Mujin protests Namho’s staged attack and objects to the insult about his parents. |
| 남호 | 태산 | guide_to_pavilion_member | Taishan | blunt and exasperated | Namho directly rebukes Taishan for eating the poisonous blood-feeding fungus. |
| 남호 | 사마표 | guide_to_young_sect_leader | Young Sect Leader | blunt and admonishing | Namho warns Sama Pyo that all grass and animals in the territory belong to the Nanman Beast Palace. |
| 사마표 | 남호 | young_sect_leader_to_guide | Elder Namho | formal and apologetic | Sama Pyo apologizes after Taishan attempts to seize the calf. |
| 진태경 | 태산 | pavilion_master_to_pavilion_member | Taishan | forceful and commanding | Taekyung orders Taishan to stop eating the bear. |
| 태산 | 남호 | Fire Dragon Pavilion member to guide | Namho | clipped, childlike, and informal | Taishan directly addresses Namho while asking what Dark Heaven is. |
| 신의 | 태산 | senior physician to younger ally | Young Hero Taishan | urgent and respectful | The Divine Physician uses this address while pleading with Taishan to keep moving. |
| 진태경 | 벽력도왕 | younger martial artist to senior martial master | Great Hero Peng | formal and deferential | Taekyung offers a respectful salute and addresses Peng as 팽 대협. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 994
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Heavenly Power Demon.md

# Heavenly Power Demon (천력마)

- **Safe through:** Chapter 993
- **Aliases:** None
- **Role:** The Heavenly Power Demon was a former Elder of the Great Heavenly Demon Divine Cult who led the subjugation of Qinghai and opened the first front of its holy war before dying after passing his remaining internal energy to Jin Taekyung.
- **Personality:** Quiet and self-possessed despite his severe imprisonment, he is reflective about the moral ambiguity of the Great Faction War and disillusioned with the Divine Cult's corruption.
- **Voice:** Gruff and dry, with formal self-reference as 노부.
- **Relationships:** He was once an Elder and commander under the Great Heavenly Demon Divine Cult's Cult Leader, has spent more than forty years imprisoned by the Sichuan Tang Clan, and identifies the Western Heaven Demon Lord as one of the Divine Cult's four Protectors who served closest to and led astray the Cult Leader.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 995
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and an active member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented; despite being naturally fearful, he faces danger and remains loyal to the person he serves, with irreverent self-deprecation and a taste for glory. He is suspicious of Taekyung, bluntly critical of the family's disgraced third son, and an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; with Taekyung, blunt and occasionally incredulous, while using breezy, irreverent banter to defuse tense situations.
- **Relationships:** He is loyal to Taekyung, who trusts him to act independently, especially in his home region of Shanxi and at the Jin Family of Taiyuan. As a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Fire Dragon Pavilion members accompanying Taekyung. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 994
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan and the original owner of his current body, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure, willing to risk himself for others, and unwilling to excuse cruelty as the inevitable price of survival.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; Peng Cheolhu regarded Taekyung as a worthy successor, inheriting all that Peng had to pass on; So Gyo says he is the chosen one spoken of by the Martial God, while the Bow Saint sought him for decades and relayed the Martial God’s message to him.

### Jin Wikyung.md

# Jin Wikyung (진위경)

- **Safe through:** Chapter 995
- **Aliases:** Junzi Sword
- **Role:** Jin Wikyung is the thirty-six-year-old Lesser Family Head and future Family Head of the Jin Family of Taiyuan, the Alliance Leader who unified Shanxi Murim and Shanxi Province's foremost landowner and magnate.
- **Personality:** Calm and politically capable, Jin Wikyung takes responsibility for his people and prioritizes their lives; he uses calculated leverage to keep dangerous allies in line and commits firmly to his principles, even when doing so means remaining in a losing battle.
- **Voice:** Restrained, formal, and commanding with subordinates; openly affectionate, proud, and occasionally exuberant with Taekyung.
- **Relationships:** Jin Wikyung is Taekyung’s eldest brother and future Family Head, protects and mentors him, and commands the Jin Family’s forces; Jin Mukyung is his younger brother, and he considers the Jin Family indebted to the Dongting Fisherman and the other fallen defenders of Shanxi.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 994
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Namho.md

# Namho (남호)

- **Safe through:** Chapter 995
- **Aliases:** Elder Chao
- **Role:** Namho is an eighty-year-old non-Han Hidden Shadow Pavilion agent who spent more than fifty years undercover in Nanman and maintained contact with Central Plains intelligence through the Pavilion’s Hidden Thread; he guides the Fire Dragon Pavilion and represents Jin Taekyung and the Murim Alliance in negotiating the survivors’ chance to rebuild the Murong household.
- **Personality:** Duty-bound, pragmatic, and observant; uses theatrical violence to protect intelligence work and takes a veteran’s concern for the younger generation’s resolve.
- **Voice:** Measured and reflective when advising the younger generation, loudly abusive when maintaining his local cover, and capable of theatrical boasts and dry humor.
- **Relationships:** Namho is a Hidden Shadow Pavilion contact for Jin Taekyung and the Fire Dragon Pavilion, receives intelligence from the Pavilion Master, and knows the code used by the Thousand-Faced Fox.

### Peng Cheolhu.md

# Peng Cheolhu (벽력도왕)

- **Safe through:** Chapter 994
- **Aliases:** Thunderbolt Saber King
- **Role:** Peng Cheolhu was the Thunderbolt Saber King, a Ten Kings master and Great Hero of the Hebei Peng Family who died as his accumulated internal energy and remaining life force melted into the flames of Taekyung’s advancement.
- **Personality:** Boisterous and teasing with old friends, yet calm and accepting in the face of death; willing to give everything he has left to protect the world.
- **Voice:** Loud, blunt, confrontational, and prone to disguising embarrassment or retreat as serious martial instruction.
- **Relationships:** He was Jeok Cheongang’s long-standing rival and friend, Hong Dao’s close friend, protective toward Hong Dao’s Disciple Unnamed, father of Peng Cheolyeong, and longtime friend and former youthful rival of Murong Baek; Jeok and Peng parted reconciled as brothers in all but blood.

### Sama Pyo.md

# Sama Pyo (사마표)

- **Safe through:** Chapter 995
- **Aliases:** Black Dragon Saber
- **Role:** Young Sect Leader of the Black Dragon Demon Gate, a Morning Star reputed to be no less than the Ten Dragons and Phoenixes, and a member of the Fire Dragon Pavilion.
- **Personality:** Outwardly courteous and smiling, inwardly calculating, but genuinely protective of Taishan; in combat he is ruthlessly pragmatic, survival-focused, and unafraid to stake his life.
- **Voice:** Polite and ingratiating in public, with sardonic humor and controlled evasiveness.
- **Relationships:** Sama Pyo commands the absolutely loyal Taishan, is Sima Gong's son, was Ju Hwaran's former fiancé in a political engagement, and has joined the Fire Dragon Pavilion while openly intending to use Jin Taekyung as a useful card; he is now openly hostile toward fellow member Song Ilseom.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 995
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo; becomes explosively violent when his meat is threatened.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord, trusts Jin Taekyung as Pavilion Master, and has grown attached to the Fire Dragon Pavilion members.

## Korean source

```text
＃996화



간혹, 그런 생각을 한다.

어쩌면 운기조식의 진정한 장점은, 축기(畜氣)를 통해 강해지는 것이 아니라 마음을 가라앉히는 것에 있지 않을까 하는.

콰아아아.

어느 정도의 시간이 지났는지는 몰랐다.

다만 더없이 쾌속하면서도 거센 흐름에 몸을 맡길 뿐.

그리고 마침내 기경팔맥(奇經八脈)을 포함한 수백여 개의 혈도를 순식간에 휩쓸고 지나간 공력의 파도를 갈무리한 순간, 나는 숨 막히는 고요함 속에서 눈을 떴다.

띠링.

때맞춰 울리는 맑은 종소리.

성공적으로 운기조식을 끝마쳤다는 알림을 들으며, 나는 차분하게 몸 안의 기운을 관조했다.

‘최상(最上).’

망설임 없이 뇌리에 떠오른 단어였고, 이러한 내 확신에는 손톱만큼의 과장도 없었다.

그래.

지금의 나는 그 어느 때보다도 강인하다.

제법 오랜 시간 동안 완전히 흡수되지 않은 상태로 체내에 공존하고 있던 천력마(天力魔)의 것은 물론, 벽력도왕의 기운까지 녹여 냈으니.

‘사 갑자(甲子)라.’

실로 어마어마한 공력이다. 지금의 내 나이와 무공을 익히기 시작한 시간을 생각하면 더더욱.

얼뜨기 무림 초출이라면 두 노강호에게 격체전공을 받고도 왜 고작 일 갑자만 늘어났는지 의문을 표하겠지만, 경지에 오른 무인들은 안다.

무공이란 단순한 일 더하기 일이 아니라는 것을.

제아무리 많은 공력을 보유해도 그 본질이 탁하다면 가진 것의 절반도 끌어낼 수 없고, 공력 또한 제대로 통제할 수 없는 법.

그리고 그런 의미에서 완전한 결합을 통해 재탄생한 사 갑자의 공력은, 내가 완전한 지배력을 행사할 수 있는 순수한 힘이었다.

‘만약 격체전공 당시 천력마와 벽력도왕의 상황이 평소와 같았다면 이보다 더 강해질 수 있었겠지만…….’

이 이상을 바라는 것은 욕심이다.

시스템이라는 불가사의한 신력(神力)을 가진 나조차도 두 번의 격체전공을 겪으며 목숨을 걸어야 했으니까.

하지만 그럼에도 불구하고 조금이나마 아쉬운 마음이 드는 이유는, 운기조식을 끝마침과 동시에 마주하게 된 현실 때문이다.



퀘스트



[사막의 아지랑이]



당신의 서쪽의 끝, 신강(新疆)에서 벌어지고 있는 심상치 않은 조짐을 알게 되었습니다.

오랜 세월 중원과 분리되어 있던 저주받은 땅.

뜨거운 모래와 이글거리는 태양 빛만이 존재하는 열사의 사막을 넘어 천하의 중심으로 향하는 무리가 존재하나, 짙은 아지랑이에 가려진 그들의 정확한 실체는 아직 드러나지 않았습니다.

부디 기억하십시오. 명심하십시오.

천하가, 하늘이 변화하고 있습니다.

정해진 것은 그 무엇도 없습니다.

지금 이 순간에도 저 멀리에서부터 다가오는 무수한 적들이 단지 찰나의 불꽃이 될지.

혹은 세상을 파멸로 몰아세울 겁화(劫火)가 될지.



등급 : 초절정

제한 : 진태경

임무 : 서쪽으로 향하기 (미완료)

보상 : 대량의 경험치와 명성

 선택에 따른 연계 퀘스트

실패 : ???





곧 시작될 험난한 여정에 앞서, 화룡각 대원들을 돌려보낸 직후 이미 수십 번에 걸쳐 반복해 읽은 퀘스트창.

허공 한구석을 메운 그것을 손짓으로 지워 낸 나는, 문득 한 시진 전 진위경과 나누었던 대화를 떠올렸다.



‘만약 은영각에서 입수한 정보대로 암천이 신강을 넘어 사막을 가로지른다면 어디를 가장 집중적으로 노리겠습니까?’

‘무림맹에서는 당장 세 곳을 동시에 염두에 두고 있다. 새외(塞外)라 할 수 있는 서장을 통해 진출할 수도 있고, 공동파와 흑룡마문이 버티고 있는 감숙성을 노릴 수도 있겠지. 하지만 가장 위험한 곳은 아마도…….’

‘청해(靑海). 바로 곤륜파겠군요.’

‘그래, 맞다. 곤륜산은 그 자체로도 천혜의 요새나 다름없지만, 중원을 노리는 암천의 입장에서는 반드시 넘어야 하는 첫 번째 관문이기도 하지. 놈들은 결코 청해를 곱게 놔두지 않을 것이다.’



산서성 역시 촌구석 변방에 속하지만, 서쪽 끄트머리에 위치한 청해성에 비할 수준은 아니다.

게다가 험준하다 못해 험악한 산지를 포함한 고지대(高地帶)에서는 풍부한 물자 생산을 기대하기 어렵고, 오랜 세월 사막을 지배해 온 마교의 영향으로 상공업 역시 그리 발달하지 못했다.

이문을 위해서라면 목숨도 거는 이들이 상인이라지만, 예정된 것이나 다름없는 죽음을 각오하고 사막을 횡단할 수는 없는 법이니까.

그러나 그 모든 것을 떠나 군사적인 측면에서 생각한다면 청해성은 없어서는 안 될 전략적 요충지였다.

누군가에게는 반드시 지켜야 하고, 또 다른 누군가에게는 반드시 짓밟고 넘어서야 하는.

‘암천의 전력이라면 충분해. 더군다나 청해성은 이미 한 번 짓밟힌 전력이 있다.’

오십여 년 전, 천마가 이끄는 십만의 마병(魔兵)은 곤륜을 패퇴시키며 청해성을 손에 넣었고 이것이 곧 정마대전의 시작이었다.

그리고 바로 지금.

그 잔혹했던 피의 역사가, 기나긴 세월을 거슬러 다시 한번 반복되려 하고 있었다.

‘청해. 청해성이라…….’

나는 깊게 가라앉은 눈빛으로 창밖을 바라보았다.

격자무늬 창틀 너머, 어느샌가 내려앉은 어둠 속에서 수백여 개에 달하는 수많은 횃불들이 이리저리 흔들리고 있었다.

해가 지고 밤이 찾아왔음에도, 태원진가의 모두는 깨어 있었다.

아니, 비단 태원진가뿐이 아닐 것이다.

구파일방과 오대세가를 포함한 중원 무림 전체가 숯불 위의 가마솥처럼 끓어오르고 있을 모습이 눈앞에 선했다.

‘다가오고 있다. 피할 수 없는 전면전이.’

전쟁을 알리는 전고(戰鼓)의 북소리는 이미 오래전부터 천하를 울리고 있었지만, 지금도 사막을 가로지르며 서쪽 어딘가를 향해 나아가고 있을 무수한 적들의 존재는 그 어느 때보다 무겁게 가슴을 옥죄였다.

지키려는 자와 빼앗으려는 자.

저마다의 명운을 건, 지금까지와는 비교도 할 수 없는 거대한 전투가 서쪽에서 모두를 기다리고 있었다.

‘곧 벌어질 단 한 번의 전투로, 이 세상의 운명이 결정될 수도 있겠지.’

어쩌면 그 때문일지도 모른다.

갑작스러운 시스템 오류도.

어떤 상황 속에서도 정해진 길을 벗어난 적 없던 이 절대적인 법칙이 흔들리기 시작한 것도.

그렇다면 잠시, 아주 잠시 동안만 이곳을 떠나 있으려던 내 발목을 잡아챈 것은 무엇일까.

시스템? 아니면…….

‘암천. 아니, 정확히는 천주(天主).’

지금 당장은 확신할 수 없지만, 적어도 한 가지 사실만큼은 짐작할 수 있었다.

서쪽 저 멀리.

캄캄한 어둠 속에 가려져 보이지 않는 저곳 어딘가에, 이 의문에 대한 답이 기다리고 있으리라는 것을.

혹은, 죽음이거나.

‘제기랄.’

역시, 뭐하나 쉽게 풀리는 게 없다.

혼자 씁쓸하게 웃어 보인 나는, 굳게 닫힌 문밖에서 대기하고 있던 누군가를 향해 입을 열었다.

“출발한다. 정확히 일각 뒤에.”

“존명.”

평소와 달리 힘이 팍 들어간 대답과 함께 멀어지는 혁무진의 인기척을 느끼며 자리에서 일어난 나는, 문득 이상함을 느끼고 고개를 돌렸다.

툭. 투두둑.

바람을 타고 방 안으로 흘러들어온 축축하고 새하얀 무언가.

정해진 때보다 몇 달이나 앞서 찾아온 불청객, 아니 조금씩 쌓여가는 눈송이들을 바라보던 나는 퀘스트창에 적혀 있던 문구 한 줄을 떠올렸다.



천하가, 하늘이 뒤바뀌고 있습니다.



저 말만큼은 오류가 아니길 마음속으로 빌었다.

지금 이 순간 내가 느끼는 천하는, 새하얀 눈송이를 쏟아내는 저 하늘은 모든 변화를 끝마친 것만 같아서.



* * *



방 안의 불빛은 흐릿했다.

밖은 이미 어두컴컴했고, 문 틈새로 흘러들어온 바람은 촛불을 위태롭게 흔들었다.

하지만 이런 악조건 속에서도, 손에 쥔 서신을 읽어 내려가던 누군가는 눈썹 하나 깜짝하지 않았다.

어릴 적부터 뼈와 살을 깎는 수련을 통해 단련된 안력(眼力)은, 당장이라도 꺼질 것 같은 희미한 불빛 속에서도 서신에 적힌 깨알 같은 글씨를 명확하게 구별해 냈으니까.

그리고 이미 몇 번이나 본 서신을 뚫어져라 응시하는 그의 눈동자에는, 휘청이는 촛불에 비친 글자 일부가 비치고 있었다.



즉각 귀환할 것.



칼날처럼 날카롭고 뾰족한 필체와 그 옆에 찍힌 익숙한 직인(職印).

이를 통해 서신을 보낸 자의 정체를 짐작한 그가 작게 뇌까렸다.

“여전하시군요, 당신은.”

공허하게 울려 퍼진 목소리는 낮게 가라앉아 있었다.

서신에 적힌 내용은 요청이나 부탁이 아니다. 명령이다.

언제나 당연했고, 모두가 당연하게 생각해 왔지만 그로서는 도무지 익숙해지지 않는 일이기도 했다.

마치 주인이 하인에게 명령을 내리듯, 무미건조한 내용으로 가득한 서신을 작성한 이는 다름 아닌 같은 피를 공유한 혈육이었으니까.

아니, 정확히는 바로 그 자신에게 피를 물려준 이였으니까.

“……아버지.”

잠깐의 머뭇거림 끝에 흘러나온 세 글자.

낯설게만 느껴지는 그 호칭을 조용히 읊조린 그는 문득 옛 기억을 떠올렸다.

딱딱하고 차가웠던, 꿈 대신 목적만이 존재했던 어린 시절과 그런 그를 냉엄하게 지켜보던 한 쌍의 눈동자를.

소름 끼치게도, 눈동자는 여전히 그의 모든 것을 지켜보고 있는 듯했다.

어쩌면 그래서였을지도 모른다.

문밖에서 다가오는 인기척을 느끼지 못한 것은.

쿵.

“억!”

갑작스럽게 들려 온 소음과 함께 겹친 비명. 뒤이어 울려 퍼진 카랑카랑한 외침이 침묵을 깨트렸다.

“이 멍청한 녀석 같으니! 높이! 높이를 생각하란 말이다!”

“태산이. 멍청하지 않다. 멍청한 건 남호다. 보면서도 못 피하나?”

“네놈, 설마 당과 안 줬다고 이러는 게냐?”

귓가를 파고드는 익숙한 목소리들.

불청객들의 정체를 짐작한 그는 손에 쥐고 있던 서신을 등잔에 던져넣었다.

화륵, 타다닥.

손바닥의 절반도 되지 않는 작은 크기에, 젖는 것을 방지하기 위해 기름까지 먹인 종이는 순식간에 활활 타올랐다.

그리고 그 순간, 굳게 닫혀 있던 문이 활짝 열렸다.

정확히는 박살이 났다고 해야 옳겠지만.

“주군! 준비 끝났나!”

꽈앙!

우렁찬 외침과 함께 산산이 부서진 문의 잔해가 사방으로 흩어졌지만 그, 아니 사마표는 조금도 당황하지 않고 옆에 놓인 행낭을 집어 들며 일어났다.

“물론이지. 태산이 너는?”

“태산이, 준비 끝났다! 완벽하다!”

태산의 어깨에 올라타 있던 남호가 나무 파편을 퉤퉤 뱉으며 덧붙였다.

“당연히 완벽하겠지. 저놈이 챙긴 육포만 되살려도 소 다섯 마리는 나올 테니까.”

“그만하면 과하지 않게 적당히 챙긴 듯합니다만.”

“……흑룡마문이 파산하지 않은 게 용하군. 아귀가 따로 없어.”

사마표는 피식 웃었다. 처음에는 그리 탐탁지 않게 느껴졌던 늙은 은영각 요원이, 제법 잔정이 많고 따뜻한 성품이라는 것은 이미 알고 있었다.

“그보다, 혼자서 뭐하고 있었나?”

“잠시 들렀습니다. 가기 전에 챙길 것이 있어서.”

“그래?”

남호가 사마표의 어깨너머를 흘끗 바라보았지만, 기름을 잔뜩 머금은 서신은 이미 흔적도 없이 타들어 간 후였다.

“그럼 저 불이나 끄고 나오게. 가뜩이나 날씨도 지랄 같은데, 남의 집 초가삼간 태울 작정 아니라면.”

“이런, 깜빡할 뻔했군요.”

부드럽게 대답한 사마표는 손을 내저어 촛불을 껐다. 그리고 마치 아무 일도 없던 것처럼, 문밖을 향해 걸음을 옮겼다.

“가시죠. 모두 기다리고 있을 텐데.”

그런 사마표의 뒷모습을 남호는 묘한 눈빛으로 응시했다.

그마저도 아주 잠깐뿐이었지만.

쿵.

“어억!”

또 다시 처마에 이마를 부딪친 남호가 비명을 지르며 태산의 머리카락을 잡아당겼다.
```

## Final English reading copy

```markdown
# Chapter 996

Sometimes, I wonder.

Maybe the real benefit of circulating your qi isn’t getting stronger by storing up internal energy, but calming your mind.

Kwoooosh.

I had no idea how much time had passed.

I could only surrender myself to the swift, powerful current.

At last, the wave of internal energy swept through hundreds of acupoints—including the Eight Extraordinary Meridians—and I gathered it all in. I opened my eyes amid a breathless silence.

Ding.

A clear chime rang out right on cue.

As the alert confirmed that I’d successfully finished circulating my qi, I calmly surveyed the energy within me.

*The peak.*

The word came to mind without hesitation, and there wasn’t a shred of exaggeration in that conviction.

That’s right.

I’m stronger now than I’ve ever been.

I’d fully absorbed not only the energy of the Heavenly Power Demon, which had coexisted inside me for quite some time without being completely assimilated, but also the energy of the Thunderbolt Saber King.

*Four jiazi.*

That was an incredible amount of internal energy. Even more so when you considered my age and how long I’d been practicing martial arts.

A greenhorn who’d just entered Murim might wonder why I’d gained only one jiazi after receiving Transmitting Internal Energy Across the Body from two old masters. But martial artists who’d reached a certain realm knew better.

Martial arts weren’t as simple as one plus one.

No matter how much internal energy you possessed, if its essence was impure, you couldn’t draw out even half of it. And you couldn’t properly control it, either.

In that sense, the four jiazi of internal energy, reborn through their complete fusion, was pure power I could wield with absolute control.

*If the Heavenly Power Demon and the Thunderbolt Saber King had been in their usual condition when they transferred their energy, I might’ve grown even stronger, but…*

Wanting more would be greedy.

Even I, with the mysterious divine strength known as the System, had risked my life twice while undergoing Transmitting Internal Energy Across the Body.

And yet, I still felt a little disappointed. The reason was the reality I’d faced the moment I finished circulating my qi.

> **System**
>
> **Quest**
>
> Desert Mirage
>
> You have learned of strange developments taking place in Xinjiang, the far western edge of your world.
>
> A cursed land, long separated from the Central Plains.
>
> A group is crossing the scorching desert, where nothing exists but hot sand and the blazing sun, and heading toward the center of the world. But their true nature remains hidden behind a dense mirage.
>
> Please remember. Never forget.
>
> The world—and the heavens—are changing.
>
> Nothing is set in stone.
>
> The countless enemies drawing near from far away, even now, may be no more than a brief spark.
>
> Or they may become a hellfire that brings the world to ruin.
>
> **Grade:** Supreme Peak
>
> **Restriction:** Jin Taekyung
>
> **Mission:** Head west (Incomplete)
>
> **Reward:** A large amount of EXP and Fame
>
> Follow-up Quests depending on your choice
>
> **Failure:** ???

It was the Quest window I’d already read dozens of times, after sending the Fire Dragon Pavilion members away in preparation for the perilous journey ahead.

I gestured, and it vanished from the corner of my vision. Then, suddenly, I remembered the conversation I’d had with Jin Wikyung two hours earlier.

“If Dark Heaven crosses Xinjiang and cuts through the desert, as the information from the Hidden Shadow Pavilion suggests, where would it focus its attack?”

“The Murim Alliance is considering three possibilities at once. They might advance through Tibet, which could be considered part of the Outer Lands. They might target Gansu Province, where the Kongtong Sect and Black Dragon Demon Gate are holding their ground. But the most dangerous place is probably…”

“Qinghai. The Kunlun Sect, then.”

“That’s right. Kunlun Mountain is a natural fortress in its own right, but for Dark Heaven, which is targeting the Central Plains, it’s also the first obstacle they’ll have to overcome. They’ll never leave Qinghai alone.”

Shanxi Province was a remote backwater, but it was nothing compared to Qinghai, at the westernmost edge of the Central Plains.

And in a high-altitude region full of terrain so rugged it was downright brutal, producing abundant supplies was difficult. Commerce and industry hadn’t developed much, either, thanks to the Demonic Cult’s influence over the desert for so many years.

Merchants would risk their lives for profit, but no one could cross a desert expecting certain death.

But even setting all that aside, Qinghai was an indispensable strategic stronghold from a military standpoint.

A place one side absolutely had to defend—and the other had to trample underfoot to get past.

*Dark Heaven has enough strength to do it. Besides, Qinghai has already been trampled once before.*

Over fifty years ago, the hundred thousand demonic soldiers led by the Heavenly Demon defeated the Kunlun Sect and took control of Qinghai. That was the beginning of the Great Faction War.

And now—

That brutal history of bloodshed was about to repeat itself after all these long years.

*Qinghai. Qinghai Province…*

I gazed out the window, my eyes sinking into shadow.

Beyond the latticed window, hundreds of torches swayed in the darkness that had settled without my noticing.

The sun had set and night had come, but everyone in the Jin Family of Taiyuan was still awake.

No, it wouldn’t be just the Jin Family.

I could picture the whole of Murim in the Central Plains—including the Nine Sects and One Gang and the Five Great Families—boiling like a cauldron over hot coals.

*It’s coming. The all-out war we can’t avoid.*

The drums of war had been pounding across the land for a long time. But the countless enemies even now crossing the desert toward somewhere in the west weighed on my heart more heavily than ever.

Those who wanted to defend—and those who wanted to take.

A colossal battle, one that would make everything we’d faced until now seem insignificant, awaited everyone in the west. Each side would stake its fate on it.

*The fate of this world might be decided by a single battle, soon to come.*

Maybe that was why.

Why the System had suddenly malfunctioned.

Why this absolute law, which had never strayed from its set path no matter the circumstances, was beginning to waver.

Then what had seized my ankle as I tried to leave this place for a little while—just a little while?

The System? Or…

*Dark Heaven. No—more precisely, the Lord of Heaven.*

I couldn’t be sure yet, but there was at least one thing I could guess.

Far away in the west.

Somewhere in that place hidden by the pitch-black darkness, the answer to this mystery was waiting.

Or perhaps death.

*Damn it.*

Nothing ever goes smoothly.

I gave a bitter smile to myself, then spoke to someone waiting beyond the firmly shut door.

“We leave in exactly fifteen minutes.”

“As you command.”

I heard Hyuk Mujin’s footsteps receding after his unusually forceful reply. As I stood, I suddenly sensed something strange and turned around.

Tap. Tap-tap.

Something damp and white drifted into the room on the wind.

I looked at the unwelcome visitor that had arrived months ahead of schedule—the snowflakes slowly piling up—and remembered a line from the Quest window.

*The world—and the heavens—are being turned upside down.*

I prayed silently that, at least, those words weren’t a malfunction.

The world I could feel at this very moment—the sky pouring down those pure white snowflakes—seemed to have finished changing already.



* * *



The light in the room was dim.

It was already pitch-black outside, and the wind seeping through the crack in the door made the candle flame flicker precariously.

Yet even under such poor conditions, the person reading the letter in their hand didn’t so much as twitch an eyebrow.

Years of grueling training since childhood had honed his eyesight. Even in the faint light, which looked ready to go out at any moment, he could clearly make out the tiny writing on the letter.

And as he stared at a letter he’d already read several times, some of the words reflected in his eyes, lit by the wavering flame.

**Return immediately.**

The handwriting was sharp and pointed as a blade, and beside it was a familiar official seal.

Guessing who had sent the letter, he muttered softly.

“You haven’t changed, have you?”

His voice echoed hollowly, low and subdued.

The letter wasn’t a request or a favor. It was an order.

It had always been that way, and everyone took it for granted. But he could never quite get used to it.

After all, the person who’d written the dry, lifeless letter as though a master were ordering a servant was his own flesh and blood.

No—more precisely, it was the person who’d given him his blood.

“…Father.”

The word came after a brief hesitation.

Quietly repeating the unfamiliar title, he was suddenly reminded of the past.

Of a childhood that had been rigid and cold, where there’d been no dreams, only purpose—and of the pair of eyes that had watched over him sternly.

Creepy as it was, those eyes still seemed to be watching everything he did.

Perhaps that was why he didn’t notice the presence approaching outside the door.

Thump.

“Ugh!”

A sudden noise overlapped with a cry of pain. Then a sharp shout rang out, breaking the silence.

“You idiot! Higher! I said you need to think about height!”

“Taishan not stupid. Namho stupid. How can’t he dodge when he sees it?”

“You little punk! Is this because I didn’t give you taffy?”

Familiar voices pierced his ears.

Guessing the intruders’ identities, he tossed the letter in his hand into the lamp.

Fwoosh. Crackle.

The small piece of paper, less than half the size of his palm and soaked in oil to keep it from getting wet, blazed up in an instant.

And at that moment, the firmly shut door flew wide open.

It would be more accurate to say it had been smashed to pieces.

“My lord! Are you ready?”

*Bam!*

As his booming shout rang out, splinters of the shattered door flew in every direction. But he—or rather, Sama Pyo—didn’t look the least bit startled. He grabbed the travel bag beside him and stood.

“Of course. What about you, Taishan?”

“Taishan ready! Perfect!”

Namho, who’d been perched on Taishan’s shoulders, spat out pieces of wood and added, “Of course it’s perfect. The jerky that guy packed would be enough to bring five cows back to life.”

“That sounds like a reasonable amount for him to pack. Not too much.”

“…It’s a wonder the Black Dragon Demon Gate hasn’t gone bankrupt. He’s a gluttonous demon through and through.”

Sama Pyo gave a short laugh. He already knew that the old Hidden Shadow Pavilion agent, who hadn’t seemed all that pleasant at first, had a warm heart and a fair amount of affection for others.

“More importantly, what were you doing here alone?”

“I stopped by for a moment. There was something I needed to take care of before we left.”

“Is that so?”

Namho glanced over Sama Pyo’s shoulder, but the letter, soaked through with oil, had already burned away without a trace.

“Then put that fire out before you come out. The weather’s already fucking awful. Unless you’re planning to burn down someone else’s little house.”

“Oh, I almost forgot.”

Sama Pyo answered gently, waved a hand, and snuffed out the candle. Then, as though nothing had happened, he headed for the door.

“Let’s go. Everyone must be waiting.”

Namho watched Sama Pyo’s back with a curious look.

But only for a moment.

Thump.

“Ugh!”

Namho let out a cry after hitting his forehead on the eaves again, then grabbed Taishan by the hair and yanked.
```

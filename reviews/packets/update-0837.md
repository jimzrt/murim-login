<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0837.txt",
      "sha256": "7a4f67f184ffa04609b5d686386c2d4c1d1aa826057b3c10fe28aefde51a45b4",
      "bytes": 13203
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "b0ee9f463e64dcc8801c062842bf597e8a261bc406622caeb71f74711d886621",
      "bytes": 2233
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "168a1e4b47c3e85f7be4ba071a6e419c026e875736c119ce00e57de5bcd19260",
      "bytes": 227203
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "c6aeb536951e9733c6ebc4a8ab240ce73f4fcc6295b7f061793fc00f551e17c8",
      "bytes": 723
    },
    {
      "path": "characters/Human Butcher.md",
      "sha256": "1e126feaf5bb78c51216e47a82aa7b41943cc6cdc412d2c9661a1d8919021a12",
      "bytes": 667
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "21b53cd64d89d63c16842e32ea25452cf1b252fae96d7afd22e9f727d95b578c",
      "bytes": 1853
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "eae58d51591a2cd5eb635918a148052b2995fed3647091f1a387fd991b170d0f",
      "bytes": 622
    },
    {
      "path": "characters/Ju Hwaran.md",
      "sha256": "a0cbc547f5b148d91d21ddf38eac9840db84061564760ce7dc99149479264f87",
      "bytes": 937
    },
    {
      "path": "characters/Ju Wongong.md",
      "sha256": "dac61f28ba7a6571fa42eae948b85b177cc0bf46aacdfbbc7bcf3594145870b8",
      "bytes": 681
    },
    {
      "path": "characters/Namho.md",
      "sha256": "6a97aff51f7c2763786fab665aeead2429c4e02fcce41fd3d3cbd96671888354",
      "bytes": 936
    },
    {
      "path": "characters/Sama Pyo.md",
      "sha256": "62e7eb6946fb386b61b0fae87a5fbee267aec56ec8ed764afb02fc456c2beb20",
      "bytes": 936
    },
    {
      "path": "characters/Song Il.md",
      "sha256": "9bee6a03051f8dd6c63f7dcdc54a464446f24b88f9e75fa1b1620b8707201730",
      "bytes": 964
    },
    {
      "path": "characters/Song Ilseom.md",
      "sha256": "1bca22fb10c65bc257a61400d4c687ac1ea2e37232d2bd0e72de64af42a6fc64",
      "bytes": 1074
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "17c7e3af1972082b3286748e30b8ca2e61cbda7467ae03d6f4c2183b65681a12",
      "bytes": 787
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "2d3ba6654cdbcc372510ec72e3979b0d7dd3413b49d0a44c281c59171f618c6d",
      "bytes": 251874
    }
  ],
  "estimated_tokens": 13357
}
-->

# Durable State Update — Chapter 837

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
1 and safe_through 837. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 837. Profile updates may replace only one
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
  "chapter": 837,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 837,
    "continuity_sources": [837],
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
    "Jin erased the Doppelganger, but Main Quest [Cataclysm] and its “Stop the Summoning” mission failed.",
    "The Rift began at 10%; its progress increases the distribution and concentration of magical power.",
    "Jin was transferred to Murim while unconscious and awakened in Nanman after several days.",
    "The System’s Status Window is inaccessible; Jin suspects an update may be responsible.",
    "Jin saw a vision of a black-haired man killing Ahomed after the ritual; whether it was real remains unknown, and Jin believes the man was not Asmodeus.",
    "Jin’s [Broken Body] injury around his lower dantian remains unresolved; leveling up did not heal it.",
    "Jeok Cheongang went to Sichuan to bring the Divine Physician, his former Disciple, to treat Jin.",
    "The swift ship carrying Jin’s party has traveled for five days from Yunnan toward Sichuan.",
    "Military vessels fired roughly a hundred cannons at the swift ship near the landing; the attack’s outcome is unknown."
  ],
  "continuity_sources": [
    835,
    836
  ],
  "open_questions": [
    "Why did the Main Quest fail despite the Doppelganger’s erasure, and who or what was summoned?",
    "Was Jin’s vision of the summoned being real, System-delivered, or prophetic?",
    "What will happen as the Rift progresses and more beings enter the world?",
    "Who or what chose Jin, and what is the Ark?",
    "What changed in the System update, and when will its functions return?"
  ],
  "safe_through": 836,
  "temporary_decisions": [
    "Keep magical power distinct from mana.",
    "Keep Blink distinct from Teleport and Warp; extended-range Blink causes severe strain.",
    "Keep Fire Storm and Aqua Storm as distinct named spells.",
    "Render [영웅의 검] as “Hero’s Sword,” 에어 슬래시 as “Air Slash,” and 실드 마법 as “Shield magic.”",
    "Render 선택받은 자 as “the Chosen One,” 방주의 주인 as “the Master of the Ark,” [격변] as [Cataclysm], [어데 도씹니꺼] as “Where’s Your Do Clan From?,” and [종족 학살자] as “Species Slayer.”"
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 송일     | **Song Il**        |
| 주화란    | **Ju Hwaran**      |
| 장강수로맹  | **Yangtze River Channel League** |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 강호     | **martial world**                                | Prefer “Murim” where the setting itself is meant      |
| 기녀     | **courtesan**                                    |                                                       |
| 헌터      | **Hunter**            |
| 대격변     | **Great Cataclysm**   |
| 사천     | **Sichuan**            |
| 공자      | **Young Master**                                                |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 주원공 | **Ju Wongong** | Qingxia Hall leader who claims distant kinship with the Emperor. |
| 남호 | **Namho** | Hidden Shadow Pavilion code name; literally associated with amber from the south. |
| 사마표 | **Sama Pyo** | Young Sect Leader of the Black Dragon Demon Gate. |
| 송일섬 | **Song Ilseom** | Young escort captain of the Yongbong Escort Bureau; distinct from Song Il of Zhongnan. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 평화 | **Peace Guild** | Guild name. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 나비 | **Nabi** | Name used for the black kitten Familiar. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 천자 | **Son of Heaven** | Honorific title for the Emperor. |
| 황상 | **Emperor** | Address or reference to the reigning Emperor. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 오향장육 | **five-spice pork** | Dish Cheongpung packed for the journey. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 일각 | **fifteen minutes** | Quarter of a shichen; used for the remaining completion time. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 선장 | **Zen staffs** | Staff weapons carried by the Hundred and Eight Arhats. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 준이 | **Jun** | Family nickname used in the form Jun's dad. |
| 화란 | **Hwaran** | Familiar short form of Ju Hwaran. |
| 수룡채 | **Water Dragon Stronghold** | Major river stronghold belonging to the Yangtze River Channel League. |
| 채주 | **Stronghold Lord** | Title used for the lord of a water stronghold. |
| 장강 | **Yangtze** | The river controlled by the Yangtze River Channel League. |
| 쾌조선 | **swift ship** | Fast vessel operated by the Yangtze River Channel League. |
| 비처 | **secret refuge** | Hidden retreat of the Dongting Fisherman. |
| 군선 | **military vessel** | Vessel carrying the Hubei government troops and sailors. |
| 황족 | **Huang tribe** | Nanman tribe involved in a recently settled dispute. |
| 가기 | **singing courtesan** | The favored entertainer identity Honglan used in Hubei. |
| 변이 | **mutation** | The transformation threatening the humans and beasts in the Inner Palace. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 송일 | 진태경 | hostile Zhongnan Elder to accused outsider | you / Jin Taekyung | hostile and threatening | Song Il questions Taekyung's identity and later threatens him over Gong Ilhyuk's injury. |
| 상인 | 청년 | stranger_to_stranger | Young Brother | formal-polite | A merchant uses 소형제 after noticing the young man's sword, and the young man approves of the address. |
| 청년 | 상인 | stranger_to_stranger | friend | casual and shameless | The young man declares that they should be friends after drinking their Yeoahong. |
| 송일섬 | 주화란 | escort_captain_to_young_bureau_head | Hwaran | urgent and familiar | Calls out 화란아 while urgently warning Ju Hwaran before stepping into the confrontation. |
| 주화란 | 진태경 | escort_bureau_leader_to_famous_younger_martial_artist | Young Hero Jin | formal-deferential | Hwaran introduces herself as the Young Bureau Head and formally greets Taekyung as 진 소협. |
| 진태경 | 주화란 | visitor_to_young_bureau_head | Young Lady Ju | formal-polite | Taekyung uses 주 소저 while announcing that his party must leave. |
| 주화란 | 송일섬 | bureau_head_to_escort_captain | Captain Song | formal and prosecutorial | Uses his office title, then his personal name, while exposing and confronting him. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 중년인 | 진태경 | veteran civilian Hunter to celebrated allied Hunter | Mr. Jin | formal-polite and awed | The casualty clerk addresses Jin as 진 선생님 after Jin asks him to list Lei Fei among the dead. |
| 진태경 | 중년인 | celebrated Hunter to older fellow Hunter | sir | casual and teasing | Jin addresses the older Hunter as 아저씨 while joking with him and giving him instructions. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 진태경 | 주원공 | opponent to exiled imperial relative | you | casual and mocking | Uses 네놈 and the 주인공/주원공 wordplay while ordering Ju Wongong down. |
| 주원공 | 진태경 | Qingxia Hall young master to Great Hero | Great Hero Jin | imperious, then deferential | Initially uses 네놈 and 역적놈아 while asserting imperial authority, then switches to 진 대협 and respectful forms after seeing Prince Shangshan's token. |
| 주화란 | 사마표 | former_fiancés | Young Sect Leader | formal and guarded | Hwaran formally greets her former fiancé. |
| 사마표 | 태산 | Young Sect Leader to subordinate | Taishan | informal and patronizing | Sama Pyo calls Taishan by name while ordering him to leave. |
| 태산 | 사마표 | subordinate to Young Sect Leader | Lord | crude and deferential | Taishan uses 주군 while obeying Sama Pyo. |
| 태산 | 진태경 | subordinate_to_respected_outsider | Jin Taekyung | clipped and familiar | Taishan says he likes Jin Taekyung but will fight him without hesitation if Sama Pyo commands it. |
| 사마표 | 진태경 | prospective recruit to pavilion master | you | polite, controlled, and candid | Sama Pyo uses 자네 while asking about Taekyung's attitude and admitting his intention to use him. |
| 진태경 | 사마표 | pavilion master to prospective recruit | you / that guy | blunt, informal, and distrustful | Taekyung speaks to and about Sama Pyo with casual forms such as 녀석 and 저놈. |
| 진태경 | 송일섬 | pavilion master to prospective member | Song Ilseom | direct and evaluative | Taekyung directly names Song Ilseom while comparing his qualifications with Hwaran's. |
| 송일섬 | 사마표 | fellow_pavilion_member_to_hostile_fellow_member | you | hostile and casual | Song Ilseom discusses fighting Sama Pyo and answers him while preparing to move away. |
| 사마표 | 송일섬 | fellow_pavilion_member_to_hostile_fellow_member | you | controlled and antagonistic | Sama Pyo responds to Song Ilseom's accusations and proposes moving aside to fight. |
| 부채주 | 진태경 | Water Dragon Stronghold deputy to honored ally | Great Hero Jin | deferential | The Deputy Stronghold Lord reports Mu Song's orders and addresses Taekyung upon arrival. |
| 진태경 | 부채주 | Fire Dragon Pavilion Master to Water Dragon Stronghold deputy | Deputy Stronghold Lord | casual and commanding | Taekyung orders him to set off and later summons him with Jang Pil. |
| 남호 | 진태경 | Hidden_Shadow_Pavilion_agent_to_mission_leader | Jin Taekyung / you | guarded and familiar | Namho addresses Taekyung as 자네 while explaining the contact and offering guidance. |
| 진태경 | 남호 | mission_leader_to_hidden_shadow_agent | you / Namho | probing and respectful | Taekyung questions Namho’s affiliation and later discusses Dark Heaven’s threat to Nanman. |
| 주화란 | 남호 | pavilion_member_to_hidden_shadow_agent | you / Elder Namho | formal and appreciative | Hwaran respectfully praises the effort Namho invested in mapping Nanman. |
| 남호 | 태산 | guide_to_pavilion_member | Taishan | blunt and exasperated | Namho directly rebukes Taishan for eating the poisonous blood-feeding fungus. |
| 남호 | 사마표 | guide_to_young_sect_leader | Young Sect Leader | blunt and admonishing | Namho warns Sama Pyo that all grass and animals in the territory belong to the Nanman Beast Palace. |
| 남호 | 주화란 | guide_to_escort_bureau_head | Escort King's granddaughter | approving and familiar | Namho praises Hwaran for recalling Ju Gongsan's records about Nanman. |
| 사마표 | 남호 | young_sect_leader_to_guide | Elder Namho | formal and apologetic | Sama Pyo apologizes after Taishan attempts to seize the calf. |
| 진태경 | 태산 | pavilion_master_to_pavilion_member | Taishan | forceful and commanding | Taekyung orders Taishan to stop eating the bear. |
| 태산 | 주화란 | Pavilion member to Pavilion member | Young Lady Ju | clipped, childlike, and deferential | Agrees with Ju Hwaran after she mentions the evening banquet. |
| 태산 | 남호 | Fire Dragon Pavilion member to guide | Namho | clipped, childlike, and informal | Taishan directly addresses Namho while asking what Dark Heaven is. |
| 주화란 | 태산 | pavilion_member_to_pavilion_member | Young Hero Taishan | formal but stern | Ju Hwaran reprimands Taishan for speaking ominously about Jin and warns that she will muzzle him. |
| 진태경 | 헌터 | field commander to allied Hunters | you; Hunters | blunt and commanding | Orders the human forces to stop asking questions and kill the fleeing Minotaurs. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 834
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Human Butcher.md

# Human Butcher (인도)

- **Safe through:** Chapter 836
- **Aliases:** None
- **Role:** Former mysterious Han Chinese mounted-bandit power in Northern Gaoyuan commanding fifty subordinates; a Peak master killed by an unnamed old man in a single move
- **Personality:** Cold, intimidating, and murderous; he kills people as though slaughtering livestock
- **Voice:** Cold, curt, and quietly threatening
- **Relationships:** He is one of four powerful participants at the Northern Gaoyuan gathering, intimidates Temur, and has claimed Ghost Sword Wipeng as his personal target in the proposed attack

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 836
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader.
- **Personality:** Hungry, self-aware, dryly observant, and pragmatic under pressure; accepts extreme personal risk when duty and the lives of others demand it.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements as well as the Peace Guild's Guild Master, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Magic Johnson is an allied Grand Mage who supplies him with intelligence, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 836
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Ju Hwaran.md

# Ju Hwaran (주화란)

- **Safe through:** Chapter 836
- **Aliases:** Hwaran
- **Role:** Ju Hwaran is a Level 88 Young Bureau Head, leader of the Yongbong Escort Bureau, an experienced Nanman guide, and an active member of the Fire Dragon Pavilion.
- **Personality:** Intelligent, capable, responsible, filial, composed under pressure, and burdened by intense guilt over the escort journey's deaths.
- **Voice:** Clear, polite, restrained, and determined.
- **Relationships:** Escort King Ju Gongsan was her paternal grandfather, Ju Hogun is her father, Heo Jun was her uncle, Sama Pyo was her former fiancé in a political engagement she accepted for her father's sake, Song Ilseom is her direct escort who accompanied her previous journey to Yeongin, and Jin Taekyung is a trusted ally; the Yongbong Escort Bureau has longstanding ties with Yeongin’s inhabitants.

### Ju Wongong.md

# Ju Wongong (주원공)

- **Safe through:** Chapter 482
- **Aliases:** Qingxia Hall young master
- **Role:** Ju Wongong is an exiled Qingxia Hall young master and a distant imperial relative of the Zhu ruling house who was punished for embezzling wealth while abusing his imperial authority.
- **Personality:** Entitled, status-conscious, theatrical, and amused by violence until his own protection is overcome.
- **Voice:** Pompous and imperious, with formal declarations of rank and authority.
- **Relationships:** His Qingxia Hall entourage and four Peak guards obey him; he asserts kinship with the Emperor.

### Namho.md

# Namho (남호)

- **Safe through:** Chapter 836
- **Aliases:** Elder Chao
- **Role:** Namho is an eighty-year-old non-Han Hidden Shadow Pavilion agent who spent more than fifty years operating under the cover of the Poison Flower Pavilion in Nanman and now serves as the Fire Dragon Pavilion’s guide.
- **Personality:** Duty-bound, pragmatic, and observant; uses theatrical violence to protect intelligence work and takes a veteran’s concern for the younger generation’s resolve.
- **Voice:** Measured and reflective when advising the younger generation, loudly abusive when maintaining his local cover, and capable of theatrical boasts and dry humor.
- **Relationships:** Namho is a Hidden Shadow Pavilion contact for Jin Taekyung and the Fire Dragon Pavilion, receives intelligence from the Pavilion Master, and knows the code used by the Thousand-Faced Fox.

### Sama Pyo.md

# Sama Pyo (사마표)

- **Safe through:** Chapter 836
- **Aliases:** Black Dragon Saber
- **Role:** Young Sect Leader of the Black Dragon Demon Gate, a Morning Star reputed to be no less than the Ten Dragons and Phoenixes, and a member of the Fire Dragon Pavilion.
- **Personality:** Outwardly courteous and smiling, inwardly calculating, but genuinely protective of Taishan; in combat he is ruthlessly pragmatic, survival-focused, and unafraid to stake his life.
- **Voice:** Polite and ingratiating in public, with sardonic humor and controlled evasiveness.
- **Relationships:** Sama Pyo commands the absolutely loyal Taishan, is Sima Gong's son, was Ju Hwaran's former fiancé in a political engagement, and has joined the Fire Dragon Pavilion while openly intending to use Jin Taekyung as a useful card; he is now openly hostile toward fellow member Song Ilseom.

### Song Il.md

# Song Il (송일)

- **Safe through:** Chapter 835
- **Aliases:** Roaring Fury Swordsman
- **Role:** Elder of the Zhongnan Sect and the Roaring Fury Swordsman; senior brother of Sect Leader Gong Iljung; came to the Jin Family of Taiyuan to demand redress for Gong Ilhyuk's injury and the alleged insult to Zhongnan; attacked Jin Taekyung with the Heavenly River Thirty-Six Swords, was stopped by Jeok Cheongang, and was publicly humiliated by him.
- **Personality:** Arrogant, domineering, punitive, and confident in his martial power and seniority.
- **Voice:** Gruff, cutting, condescending, and threatening, with formal authority used to pressure those beneath him.
- **Relationships:** Gong Iljung is his junior Sect Leader and martial younger brother; Gong Ilhyuk is a junior Disciple of his sect; he recognizes Baek Museong and Cheongpung through their Huashan and Sword Saint connections.

### Song Ilseom.md

# Song Ilseom (송일섬)

- **Safe through:** Chapter 835
- **Aliases:** Escort Captain Song
- **Role:** Level 110 young escort captain of the Yongbong Escort Bureau, one of its Dragon-Phoenix Three Escorts, and a newly accepted member of Jin Taekyung and Cheongpung’s Fire Dragon Pavilion; he is currently bound and unconscious under the reconnaissance squad's guard after being struck at a Sleep Acupoint.
- **Personality:** Blunt, decisive, survival-hardened, and dryly self-aware, with little patience for insults or disorder and practical survival skills such as making disguise masks.
- **Voice:** Forceful and urgent in command, with a rough and confrontational edge.
- **Relationships:** He serves under Ju Hwaran and has expressed concern that she not be hurt or die needlessly; he is Song Pyosan’s son, his grandmother was the surviving Guangdong Chen child rescued by Ju Gongsan during the Great Faction War, and he remains openly hostile toward fellow Fire Dragon Pavilion member Sama Pyo.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 836
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion; he helped Jin escape the underground prison by blocking the stairs and overpowering the Bai warriors.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo; becomes explosively violent when his meat is threatened.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord, trusts Jin Taekyung as Pavilion Master, and has grown attached to the Fire Dragon Pavilion members.

## Korean source

```text
＃837화



퍼버버버벙!

화염과 함께 피어오르는 새하얀 연기.

동시에 이백여 장의 거리를 격하고 쇄도한 쇳덩이들이 쾌조선을 부수고 그 위의 사람들을 잘 다진 어육(魚肉)처럼 짓뭉개……는 일은 당연히 일어나지 않았다.

이 세상이 21세기의 현대보다 월등하다고 할 수 있는 유일한 것은 무공이지, 과학이 아니니까.

퍼엉, 촤아아악!

쾌조선이 아닌 수면을 후려친 쇳덩이에, 힘을 이기지 못한 물줄기가 파도처럼 솟아오른다.

그 여파에 휘말려 재수 없게 갑판까지 날아온 생선을 허공에서 잡아챈 태산이 울상을 지었다.

“태산이. 슬프다. 이거 오향장육 아니다.”

“…….”

오향장육 원산지가 언제부터 장강이었나.

짜게 식은 눈빛으로 태산을 노려보던 나는, 어느새 다른 수적들처럼 새우처럼 몸을 웅크리고 주저앉아 있는 수룡채 부채주의 뒤통수를 툭 쳤다.

“일어나요. 수적이라는 양반이 뭘 그렇게 바짝 쫄아 있어.”

“헉. 저 살아 있습니까?”

“그럼 다 같이 죽었겠냐?”

“아니, 분명히 쏘는 걸 똑똑히 봤는데…….”

“쏘기야 쐈지. 조준은 엉망이었고.”

적어도 하루에 한두 번씩은 꼭 싸는 오줌도 간혹가다 조준이 빗나가는 마당에 구식 대포 쏘는 게 그렇게 쉽겠나.

백여 발의 쇳덩이 중 제대로 발사된 건 절반 정도고, 그중에서도 절반 이상은 근처에도 오지 못했다.

그나마 기적적으로 쾌조선 가까이 도달한 것들은 파도풀 체험을 위한 제물로 쓰였을 뿐이다.

‘하긴 뭐, 가끔 훈련할 때나 몇 번 쏴 봤을 테니까.’

어찌 보면 당연한 일이었다.

온갖 군벌이 들불처럼 일어나 천하의 패권을 다투던 군웅할거(群雄割據)의 시대는 이미 막을 내린 지 오래.

대격변이라는 거대한 사건을 겪은 현대의 인류도 불과 삼십여 년 만에 평화에 젖고, 헌터라는 두 글자는 사명이 아닌 직업으로 받아들여지는 상황이니 천자(天子)가 다스리는 이 통일 왕조의 군사들이 느슨해지는 건 당연했다.

단 한 가지, 이해가 안 되는 부분은 왜 갑자기 우리를 향해 대포를 쏴 대냐는 건데…….

“물어보면 알겠지.”

“예?”

“그냥 혼잣말이었으니까 신경 쓰지 말고. 배나 몰아요.”

“예?”

“전진하시라고. 여기서 날 샐래?”

“예?”

이 정도로 말귀 못 알아듣는 것도 능력이라면 능력이다.

얼빠진 얼굴로 되묻기만 하는 수룡채 부채주의 모습에 혀를 찬 나는 가까이에 있는 수적 하나를 불렀다.

“거기 아저씨.”

“저, 저 말입니까?”

“그래. 당신이 지금부터 임시 선장이니까 배 몰아요. 아, 혹시 모르니까 백기도 잘 보이게 걸어 두고.”

잠시 남만으로 넘어가 있던 사이 사천에 무슨 일이 벌어졌는지는 모르겠지만, 근처에 대포알 몇 개 떨어졌다고 관군을 공격할 생각은 없다.

제아무리 관과 무림이 불가침의 관계라지만, 무림인도 결국 이 땅의 백성. 자칫하면 반역(反逆)이라는 거창한 죄목이 붙을 수도 있으니까.

‘최근에 인근 수적 놈들이 사고라도 쳤나.’

그런 생각을 하고 있을 때, 잠시 움직임을 멈췄던 쾌조선이 선착장을 향해 나아감과 동시에 수적 중 하나가 외쳤다.

“놈들이 재장전을 하고 있습니다!”

그리 반갑지 않은 소식이지만, 그렇다고 딱히 걱정되는 소식도 아니다.

굳이 내가 나서지 않더라도 구식 대포쯤은 손쉽게 막아 낼 인간 방패들이 함께 있으니까.

“밥값 좀 하자.”

그 한 마디를 툭 던진 순간.

퍼어엉!

두 번째 발포를 알리는 굉음과 함께, 내 등 뒤에서 미세한 파공성이 울려 퍼졌다.

쐐애애액!

사마표, 태산, 송일섬. 그리고 마지막으로 주화란까지.

눈 깜짝할 사이에 갑판을 가로지른 그들이 불러낸 휘황한 빛이, 쾌조선을 향해 들이닥친 쇳덩이와 맞닿았다.

서걱! 콰아앙!



* * *



둥. 둥. 둥.

퍼버버벙!

다급함이 느껴지는 북소리와 함께 쉴 새 없이 울려 퍼지는 폭음.

수십 척의 놀잇배 중에서도 가장 크고 화려한 배에서 가기(歌妓)의 춤사위를 감상하던 청년이 피식 웃었다.

“어느 잡놈들인지는 몰라도, 운 한번 더럽게 없구나.”

거나하게 취한 목소리와 한껏 풀린 눈꼬리. 평소 청년의 성정을 아는 탓에 눈치만 살피고 있던 이들이 그제야 따라 웃었다.

“하하, 못 배운 것들이 다 그렇지요.”

“지금이라도 공자님이 이곳에 계신 걸 알게 된다면, 배도 버리고 천 리 밖으로 도망칠 게 뻔합니다.”

“한데…… 저 깃발이 좀 마음에 걸립니다.”

누군가의 말에 청년이 반응했다.

“깃발? 깃발이 왜?”

“혹 장강수로맹이라고 들어보셨습니까?”

“장강수로맹이라.”

술잔을 든 채 잠시 기억을 더듬던 청년이 문득 탄성을 흘렸다.

“아, 그 수적 놈들 말인가? 알지. 내가 일전에 머무르던 곳에서도 장강수로맹이라는 단체가 있었네.”

“예, 맞습니다. 강호에서도 상당히 유명한 무뢰배 집단이지요. 한데 지금 우리 수군이 공격하는 저 배가 바로 그 장강수로맹의 깃발을 달고 있습니다.”

“그래서?”

“대저 관과 무림은 불가침이 아닙니까. 더군다나 장강수로맹의 수괴는 그 성정이 흉포하고 간악하기로 유명한데. 혹여 이 일로 문제가 생기지는 않을지…….”

막힘 없이 이어지던 목소리가 서서히 흐려졌다.

어느새 조용해진 놀잇배 위, 조금 전까지만 해도 청년의 입가에 맺혀 있던 미소가 흐릿해졌다.

탁.

거칠게 잔을 내려놓는 손길에, 담겨 있던 술이 어지럽게 튀었다.

“문제라.”

하나같이 윤기가 흐르는 비단옷에 귀티 어린 얼굴들.

그중에는 청년 또래의 젊어 보이는 이들도, 족히 아버지뻘은 되어 보이는 중년인들도 있었지만 모두 청년의 일거수일투족을 숨죽인 채 지켜보았다.

“진심으로 궁금해서 묻는 것인데…… 그대는 무슨 문제를 걱정하는 거지?”

“그, 그것은.”

가장 처음 말을 꺼낸 상인이 말을 더듬었다.

사천에서 제법 규모 있는 상단을 운영하는 그는 이미 괜한 말을 한 것을 뼈저리게 후회하고 있었다.

청년의 눈에 들기 위해 뇌물까지 써 가며 참석한 자리다.

상단을 운영하다 보니 보고 들은 것이 있어 별생각 없이 말을 꺼낸 것인데, 이제는 눈에 드는 것이 아니라 눈 밖에 나게 생겼다.

“소, 송구합니다. 공자님.”

뒤늦게 건넨 사과. 그러나 한 번 뒤틀린 청년의 심기를 가라앉히기에는 역부족이다.

술에 취해 흐느적거리던 그의 눈매는 평소처럼 간교하게 위로 솟구쳐 있었다.

‘천한 상인 놈 따위가 감히…….’

청년은 고개 숙인 상인의 뒤통수를 노려보았다.

평소에도 권위와 위엄을 가장 중시하는 그였다. 그런데 그런 자신의 앞에서, 그것도 강호의 무뢰배 집단 따위가 걱정된다는 헛소리를 지껄이다니.

장강수로맹?

이름만 거창하지, 결국 냄새나고 못 배운 수적들이 모여 만든 곳 아닌가.

제아무리 관과 무림이 불가침이라지만, 청년에게는 보는 즉시 때려잡아야 할 도적놈들에 불과했다.

특히나 몇 달 전 ‘그 일’을 겪고 난 후에는 더더욱 그런 생각이 굳혀진 청년이었다.

“저 강호의 무뢰배들도 엄연히 대국(大國)의 백성에 불과한데, 그대들은 무엇이 걱정된단 말인가.”

차갑게 식어 버린 청년의 목소리에, 눈치만 살피던 이들도 넙죽 고개를 숙였다.

“그, 그 말씀이 백번 옳습니다!”

“소인은 아무런 걱정도 없습니다. 관군의 기세는 칼 같고, 이리 영명하신 공자께서 계시온데 어찌 강호인들 따위를 두려워하겠습니까!”

풍악(風樂)은 이미 화포의 폭음에 가려진 지 오래요, 나비처럼 하늘거리던 가기의 옷자락도 주위의 분위기와 함께 가라앉은 상황.

홀로 자리에서 일어난 청년은 오만한 눈빛으로 고개 숙인 이들을 굽어보았다.

‘한심한 것들. 그깟 강호인들이 뭐라고.’

일각 전만 하더라도 기분 좋게 느껴졌던 취기는 오히려 불쾌했고, 하늘에서 내려온 것 같던 기녀들의 자태도 전만 못했다.

그리 오래되지 않은 끔찍한 기억들 때문일까. 좀처럼 분이 풀리지 않은 청년은 손을 들어 장강을 가리켰다.

“모두 고개를 들어 저 수적 놈들을 보아라! 대국의 힘 앞에 산산이 부서지는 놈들의 최후를!”

그리고 외침과 함께 고개를 돌린 순간. 자신도 모르게 눈을 깜빡였다.

“어?”

내가 술을 너무 많이 마셨나?

그것이 가장 처음 청년의 머릿속을 스친 생각이었다.

하지만 옷소매로 눈을 뽀득뽀득 문지르고 다시 보아도, 눈앞의 광경은 여전했다.

아니, 변화가 있긴 했다.

이미 진작 침몰했어야 할 놀잇배가 엄청난 속도로 가까워지고 있었으니까.

“어?”

“어머?”

“뭐여, 저게.”

고용주의 눈치만 살피던 기녀들도, 청년의 명령에 마지못해 고개를 든 이들도 눈을 깜빡이며 그 믿을 수 없는 광경을 지켜보았다.

‘어떻게 저렇게 멀쩡하지?’

‘대포 안 쐈나?’

‘아닌데, 쐈는데?’

‘그러고 보니까 아까부터 계속 쐈던 것 같은데?’

‘어? 지금도 쏘고 있는데?’

누군가의 생각처럼, 십여 척의 군선은 지금도 바쁘게 포탄을 쏘아 보내고 있었다. 처음보다 훨씬 다급하고, 정신없게.

“이, 이놈들이 미쳤나. 똑바로 쏴라!”

“똑바로 쏘고 있습니다!”

“그런데 왜 안 맞아!”

“아닙니다! 분명히 맞았습니다! 소리도 났습니다!”

“그럼 왜 멀쩡해!”

“아니, 싯팔 저희가 그걸 어떻게 압니까!”

병졸의 욕설에는 진심이 담겨 있었다.

쏘고, 쏘고, 또 쐈다. 지금까지 모든 군선에서 퍼부은 대포알만 족히 수백 발은 된다.

하지만 평소 훈련량이 부족했고, 조준을 아무리 병신같이 했어도 이쯤 되면 한 발 정도는 적중해야 예의고 상식 아닌가.

그런데…… 멀쩡하다.

어둠 너머에서 새카만 물살을 가르며 다가오는 저 날렵한 선박의 모습이, 마치 유령처럼 보였다.

‘도대체 왜!’

모두의 머릿속에 떠오른 생각과 함께 슬그머니 고개를 드는 두려움.

뱃사람이라면 한 번쯤은 들어 봤다. 포탄으로도 침몰하지 않고, 죽여도 죽지 않는다는 망자들의 배를.

‘지, 진짜 유령선인가?’

‘아니, 여긴 바다가 아니라 장강인데.’

‘그럼 장강이 바다였나?’

병졸들의 말도 안 되는 생각들이 꼬리에 꼬리를 물고 이어지던 그때. 어느새 놀잇배의 뱃머리에 바짝 붙은 청년은 바로 오늘 선물 받은 천리경(千里鏡)이라는 귀물의 쓰임새를 몸소 확인하고 있었다.

그리고 경악했다.

“이런 미친…….”

자신도 모르게 상스러운 말을 중얼거린 청년이 멍하니 입을 벌렸다.

천리경을 통해 확인한, 믿을 수 없는 광경 때문이었다.

쾅! 쾅! 콰아앙!

굉음과 함께 튕겨 나가는 대포알들.

아니, 정확히는 선박을 향해 짓 쳐드는 대포알을 튕겨 내는 사람들.

“고, 공자님. 지금 무슨 일이 벌어지고 있는 겁니까?”

문득 귓가에 닿은 누군가의 목소리에 잠깐 청년은 고민했다.

지금 본 이 광경을 어떻게 설명해야 하는지. 혹시 미친놈이라고 오해받지는 않을지.

하지만 청년의 그 고민조차 얼마 가지 못하고 사라졌다.

천리경을 통해, 도저히 잊으려야 잊을 수 없는 한 사람의 얼굴을 보았기 때문이었다.

“어, 어어, 어어어!”

말하는 법을 까먹은 사람처럼 이상한 소리를 흘린 청년, 주원공이 군선을 향해 외쳤다.

“공격 중지! 중지잇! 이건 황명, 아니 황상 폐하의 팔촌 되는 몸으로서 내리는 황족명이다!”

그리고 저 멀리서 주원공을 알아본 진태경은, 그 외침을 듣고 중얼거렸다.

“황명은 들었는데, 황족명은 또 뭐야?”

박학다식한 남호가 대답했다.

“황족명은 무슨. 그냥 족 까는 소리지. 그런데 혹시 아는 놈이냐?”

“예. 그냥 뭐…….”

진태경이 뒤통수를 긁적이며 덧붙였다.

“오다가다 목숨 한번 구해 줬어요.”
```

## Final English reading copy

```markdown
# Chapter 837

*Boom! Boom! Boom!*

White smoke billowed up with the flames.

The iron balls came hurtling across more than six hundred yards, smashing the swift ship and crushing the people aboard into finely minced fish…

Naturally, that didn’t happen.

The only thing this world could be said to do far better than the modern twenty-first century was martial arts—not science.

*Boom! Splash!*

The iron balls struck the water instead of the swift ship, sending up waves as the water failed to withstand their force.

Taishan snatched a fish out of the air as the blast sent it flying toward the deck. He looked dejected.

“Taishan sad. This not five-spice pork.”

“……”

Since when did five-spice pork come from the Yangtze?

I gave Taishan a frosty look, then tapped the back of the Water Dragon Stronghold Deputy Stronghold Lord’s head. He was crouched on the deck like a shrimp, just like the other river pirates.

“Get up. You’re a river pirate. Why are you so scared?”

“Gasp! Am I alive?”

“Did you think we’d all died?”

“But I saw them fire with my own eyes…”

“They did fire. Their aim was just terrible.”

Even people who pissed at least once or twice a day sometimes missed the target. Was it really so easy to shoot an old-fashioned cannon?

Only about half of the hundred or so iron balls had been fired properly, and more than half of those hadn’t come anywhere near us.

The ones that had miraculously reached the swift ship had merely served as sacrifices to the river’s wave pool.

*Well, I suppose they’ve only fired a few shots now and then during training.*

When you looked at it that way, it made sense.

The age of competing warlords, when countless factions rose like wildfires to fight for supremacy, had ended long ago.

Even modern humanity, after going through the Great Cataclysm, had settled into peace in just over thirty years. The word Hunter had come to be understood as a profession, not a calling. It was only natural that the soldiers of this unified dynasty, ruled by the Son of Heaven, would grow lax.

There was just one thing I didn’t understand: why were they suddenly firing cannons at us?

“I’ll ask them.”

“Pardon?”

“I was talking to myself. Don’t worry about it. Just steer the ship.”

“Pardon?”

“Get moving. Do you want to spend the night here?”

“Pardon?”

If failing to understand this much counted as a talent, then he had a real talent.

I clicked my tongue at the Deputy Stronghold Lord, who just kept staring blankly and asking me to repeat myself, then called over one of the nearby river pirates.

“Hey, you there.”

“M-me?”

“Yeah. You’re the acting captain now, so steer the ship. Oh, and hang the white flag somewhere it’s easy to see, just in case.”

I didn’t know what had happened in Sichuan while we’d been in Nanman, but I had no intention of attacking the government troops just because a few cannonballs had landed nearby.

No matter how inviolable the boundary between the government and Murim was, martial artists were still subjects of this land. We could end up charged with something as serious as treason.

*Did some local river pirates cause trouble recently?*

As I thought it over, the swift ship—which had paused for a moment—started toward the landing. One of the river pirates shouted:

“They’re reloading!”

Not great news, but not something I was particularly worried about, either.

Even if I didn’t step in, we had human shields who could easily stop a few old-fashioned cannonballs.

“Earn your keep.”

The moment I tossed out that one line—

*Boom!*

The second volley thundered, and a faint whistle came from behind me.

*Whoosh!*

Sama Pyo, Taishan, Song Ilseom—and finally, Ju Hwaran.

In the blink of an eye, they raced across the deck. The brilliant light they summoned met the iron balls flying toward the swift ship.

*Slice! Crash!*

* * *

*Thump. Thump. Thump.*

*Boom! Boom! Boom!*

The cannons kept roaring alongside the urgent beat of drums.

A young man, who’d been watching a singing courtesan dance aboard the largest and most splendid pleasure boat among dozens of them, gave a quiet laugh.

“I don’t know what kind of idiots they are, but they’re having a hell of a bad day.”

His voice was thick with drink, his eyes relaxed. The others had been watching him warily, knowing his usual temperament, but now they finally laughed along.

“Ha ha. That’s what happens to the uneducated.”

“If they realized Young Master was here, they’d abandon their boats and run a thousand li away.”

“But… that flag concerns me.”

The young man reacted to the comment.

“The flag? What about it?”

“Have you ever heard of the Yangtze River Channel League?”

“The Yangtze River Channel League…”

The young man, holding a cup of wine, searched his memory for a moment, then suddenly exclaimed.

“Oh, those river pirates? Of course. There was a group called the Yangtze River Channel League where I used to stay.”

“Yes, exactly. They’re a notorious bunch of scoundrels, even in the martial world. But the boat our navy is attacking is flying the Yangtze River Channel League’s flag.”

“And?”

“Generally speaking, the government and Murim are not supposed to interfere with one another. Besides, the head of the Yangtze River Channel League is famous for being savage and devious. I’m worried this might cause trouble…”

His words, which had been flowing smoothly, gradually faded.

The pleasure boat had fallen quiet. The smile that had been on the young man’s lips a moment ago had dimmed.

*Clack.*

He set his cup down roughly, splashing the wine inside.

“Trouble?”

Every one of them wore glossy silk and had a face that spoke of wealth and status.

Some looked young enough to be the man’s peers; others were middle-aged, old enough to be his father. But all of them held their breath and watched his every move.

“I’m asking because I genuinely want to know… What kind of trouble are you worried about?”

“Th-that is…”

The merchant who’d first spoken stammered.

He ran a sizable trading company in Sichuan, and was already regretting his careless words with every fiber of his being.

He’d even paid a bribe to attend this gathering, hoping to win the young man’s favor. As a merchant, he’d heard and seen a lot, so he’d spoken without giving it much thought. Now, instead of catching the young man’s eye, he was about to fall out of favor.

“I-I’m sorry, Young Master.”

The apology came too late. It wasn’t enough to calm the young man’s temper, which had already turned sour.

His eyes, drooping drunkenly a moment ago, had once again slanted upward with their usual cunning.

*How dare a lowly merchant…*

The young man glared at the back of the bowed merchant’s head.

He valued authority and dignity above all else. And now, right in front of him, this man had spouted nonsense about worrying over a bunch of martial-world ruffians.

The Yangtze River Channel League?

A grand name, but in the end, it was just a collection of stinking, uneducated river pirates.

No matter how inviolable the boundary between the government and Murim was, to the young man they were nothing but bandits who ought to be beaten down on sight.

His belief had only grown stronger since what had happened a few months ago.

“Those ruffians of the martial world are nothing more than subjects of the Great Nation. What is it you’re all worried about?”

At the chill in the young man’s voice, the others, who’d been watching him warily, bowed their heads in a hurry.

“Y-you are absolutely right!”

“I have nothing to worry about. The government troops are as sharp as blades, and with such a wise Young Master here, why would we fear a few martial artists?”

The cannons had long since drowned out the music. The courtesans’ fluttering sleeves, which had danced like butterflies, had settled along with the mood.

The young man stood alone and looked down at the bowed figures with arrogant eyes.

*Pathetic. What are a few martial artists, anyway?*

The drunken haze that had felt pleasant just a quarter of an hour ago now irritated him, and the courtesans, who had seemed to have descended from heaven, had lost their charm.

Perhaps it was because of the dreadful memories he’d had not long ago. The young man still couldn’t let go of his anger. He raised his hand and pointed toward the Yangtze.

“Everyone, raise your heads and look at those river pirates! Look at their end as they’re crushed beneath the might of the Great Nation!”

But as he turned at the same time he shouted, he blinked without meaning to.

“Huh?”

*Did I drink too much?*

That was the first thought to cross his mind.

But even after rubbing his eyes hard with his sleeve and looking again, the scene before him remained unchanged.

Well, not quite unchanged.

The pleasure boat that should have sunk long ago was speeding closer.

“Huh?”

“Oh?”

“What the hell is that?”

The courtesans, who’d been watching their employer for cues, and those who’d reluctantly raised their heads at the young man’s order, all blinked as they watched the unbelievable sight.

*How is it still in one piece?*

*Didn’t they fire the cannons?*

*They did, though.*

*Now that I think about it, they’ve been firing this whole time, haven’t they?*

*Huh? They’re firing right now, too.*

Just as someone had thought, more than ten military vessels were still busy sending cannonballs flying. They were firing more urgently and chaotically than before.

“Y-you idiots! Aim properly!”

“We are aiming properly!”

“Then why aren’t you hitting it?!”

“We are! We definitely hit it! We heard the sound!”

“Then why is it still in one piece?!”

“Hell if we know!”

There was nothing but sincerity in the soldier’s curse.

They’d fired, and fired, and fired again. Together, the military vessels had fired hundreds of cannonballs by now.

They might not have trained enough, and they might have aimed like a bunch of goddamn idiots, but by now, common courtesy—and common sense—said at least one shot should’ve hit.

And yet… it was still in one piece.

The sleek vessel cutting through the black current as it approached from beyond the darkness looked like a ghost.

*Why?!*

Fear slowly rose in everyone’s minds along with that one question.

Every sailor had heard the stories at least once: ships belonging to the dead, said to be impossible to sink with cannonballs and impossible to kill.

*I-is it really a ghost ship?*

*But this is the Yangtze, not the sea.*

*Then was the Yangtze the sea?*

While the soldiers’ absurd thoughts chased one another around, the young man had come right up to the bow of the pleasure boat. He was putting to the test the strange gift he’d received just that day: an instrument called a thousand-li lens.

And he was horrified.

“This is insane…”

The young man muttered an uncharacteristically vulgar phrase under his breath and gaped.

He couldn’t believe what he was seeing through the thousand-li lens.

*Boom! Boom! Craaash!*

Cannonballs bounced away amid the thunderous blasts.

Or, more precisely, people were batting away the cannonballs as they came hurtling toward the ship.

“Y-Young Master. What’s happening?”

At the sudden voice in his ear, the young man hesitated for a moment.

How was he supposed to explain what he’d just seen? Would they think he was crazy?

But the young man’s concern didn’t last long.

Through the thousand-li lens, he saw the face of someone he could never forget, no matter how hard he tried.

“Uh, uh, uhhhh!”

The young man made strange noises as if he’d forgotten how to speak. Then Ju Wongong shouted toward the military vessels.

“Cease fire! Cease! This is an imperial command—no, an imperial-family command, issued by me as His Majesty the Emperor’s eighth-degree relative!”

From far away, Jin Taekyung recognized Ju Wongong and muttered when he heard the shout.

“I heard of an imperial order, but what’s an imperial relative’s order?”

Namho, who knew a thing or two, answered.

“There’s no such thing as an imperial relative’s order. He’s just talking shit. But do you know that guy?”

“Yeah. I, uh…”

Jin Taekyung scratched the back of his head and added:

“I saved his life once, along the way.”
```

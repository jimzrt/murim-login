<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0836.txt",
      "sha256": "0feb61d1e0914d961ae99abc58906235a1661b033af951ad5319e1e0a73be783",
      "bytes": 13739
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "63a0d6f627f280b6d4877d44b92e7eb9c86b3b3bad43fe98e4104bde7dee2449",
      "bytes": 2238
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "168a1e4b47c3e85f7be4ba071a6e419c026e875736c119ce00e57de5bcd19260",
      "bytes": 227203
    },
    {
      "path": "characters/Human Butcher.md",
      "sha256": "f4709eeb72302d1e004164042ebf743e8e572595c4bfff19bd7a1f6c1e67216f",
      "bytes": 667
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "f884c30fd781fa347c5dde19ad58dc7b286c5cd18ed73699a37264f08d754af2",
      "bytes": 1355
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "9a0e45642b13e8c7836d4a534a04a16d67b9b663b18280bef84939cf22fd8da0",
      "bytes": 1853
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "01822cfc3837aec2461c3e1a79c36017db1590a2b58cbf6e18deb7f4f02ac88d",
      "bytes": 622
    },
    {
      "path": "characters/Ju Hwaran.md",
      "sha256": "5ba4bf0ad6f6f93d10e9ef6b5fba56a7f2b7eb825ea9eb04477057e4da70f60f",
      "bytes": 937
    },
    {
      "path": "characters/Mu Song.md",
      "sha256": "304ebe3a28a53c2f3a904c36fdff8d6808c6674a1d4dbf6b6682595569d1e25d",
      "bytes": 1131
    },
    {
      "path": "characters/Namho.md",
      "sha256": "9508e4644b6b60d2edded62408d481531157edaa8463a0e8bd59724d22303077",
      "bytes": 881
    },
    {
      "path": "characters/Sama Pyo.md",
      "sha256": "db084933f5c441a824ccb32e09411359f1aab6b7232b393f44efa100ebd489f0",
      "bytes": 936
    },
    {
      "path": "characters/Sudal.md",
      "sha256": "41bd26f1907570c250ae9bdd526abc4208d87fc00c8e6601b54731c84db95b03",
      "bytes": 618
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "7291473023e7a8730ace0c13c5aea91e05562ed38a9e05fa3da79f9502815e73",
      "bytes": 787
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "2d3ba6654cdbcc372510ec72e3979b0d7dd3413b49d0a44c281c59171f618c6d",
      "bytes": 251874
    }
  ],
  "estimated_tokens": 13637
}
-->

# Durable State Update — Chapter 836

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
1 and safe_through 836. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 836. Profile updates may replace only one
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
  "chapter": 836,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 836,
    "continuity_sources": [836],
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
    "Jin saw a vision of a black-haired man killing Ahomed after the ritual; whether the vision was real remains unknown, and Jin believes the man was not Asmodeus.",
    "Jin’s [Broken Body] injury around his lower dantian remains unresolved; leveling up did not heal it.",
    "Jeok Cheongang went to Sichuan to bring the Divine Physician, his former Disciple, to treat Jin.",
    "Taishan returned with a giant beehive as a supposed cure for Jin.",
    "Jin rested for five days aboard the swift ship and felt better when he emerged.",
    "The swift ship reached Sichuan; Sudal decided to retire."
  ],
  "continuity_sources": [
    834,
    835
  ],
  "open_questions": [
    "Why did the Main Quest fail despite the Doppelganger’s erasure, and who or what was summoned?",
    "Was Jin’s vision of the summoned being real, System-delivered, or prophetic?",
    "What will happen as the Rift progresses and more beings enter the world?",
    "Who or what chose Jin, and what is the Ark?",
    "What changed in the System update, and when will its functions return?"
  ],
  "safe_through": 835,
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
| 혁무진    | **Hyuk Mujin**     |
| 주화란    | **Ju Hwaran**      |
| 태원진가   | **Jin Family of Taiyuan**        |
| 무림맹    | **Murim Alliance**               |
| 장강수로맹  | **Yangtze River Channel League** |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 주화입마   | **qi deviation**                                 |                                                       |
| 중원     | **Central Plains**                               |                                                       |
| 강호     | **martial world**                                | Prefer “Murim” where the setting itself is meant      |
| 선배     | **Senior**                                   |
| 상태               | **Status**                     |
| 헌터      | **Hunter**            |
| 태원     | **Taiyuan**            |
| 사천     | **Sichuan**            |
| 정마대전   | **Great Faction War**         |
| 노부      | **this old man / I**                                            |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 무송 | **Mu Song** | Lord of Water Dragon Stronghold and disciple of the Seafaring King. |
| 남호 | **Namho** | Hidden Shadow Pavilion code name; literally associated with amber from the south. |
| 사마표 | **Sama Pyo** | Young Sect Leader of the Black Dragon Demon Gate. |
| 수달 | **Sudal** | Deputy Stronghold Lord of the Water Dragon Stronghold and river pirate. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 대동 | **Datong** | Shanxi location containing the Mount Heng Sword Sect branch destroyed by the Red Wind Band. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 기해 | **qi sea** | Name for the dantian, the place where internal energy begins and gathers. |
| 오향장육 | **five-spice pork** | Dish Cheongpung packed for the journey. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 운남 | **Yunnan** | Region from which Jongni Chu comes. |
| 은영각 | **Hidden Shadow Pavilion** | Former Murim Alliance intelligence organization. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 화란 | **Hwaran** | Familiar short form of Ju Hwaran. |
| 장강 | **Yangtze** | The river controlled by the Yangtze River Channel League. |
| 열화신룡 | **Blazing Flame Divine Dragon** | New sobriquet bestowed on Jin Taekyung. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 쾌조선 | **swift ship** | Fast vessel operated by the Yangtze River Channel League. |
| 찍먹형 | **dip-and-taste punishment** | Mu Song's joking threat against sailors who slack off. |
| 군선 | **military vessel** | Vessel carrying the Hubei government troops and sailors. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 한나절 | **half a day** | Elapsed duration in Jeok's first time-loss episode. |
| 화룡각 | **Fire Dragon Pavilion** | New name chosen for Taekyung's pavilion. |
| 화신 | **Fire God** | A local deity worshiped by one Nanman believer. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 상인 | 청년 | stranger_to_stranger | Young Brother | formal-polite | A merchant uses 소형제 after noticing the young man's sword, and the young man approves of the address. |
| 청년 | 상인 | stranger_to_stranger | friend | casual and shameless | The young man declares that they should be friends after drinking their Yeoahong. |
| 주화란 | 진태경 | escort_bureau_leader_to_famous_younger_martial_artist | Young Hero Jin | formal-deferential | Hwaran introduces herself as the Young Bureau Head and formally greets Taekyung as 진 소협. |
| 진태경 | 주화란 | visitor_to_young_bureau_head | Young Lady Ju | formal-polite | Taekyung uses 주 소저 while announcing that his party must leave. |
| 주화란 | 혁무진 | rescued_survivor_to_benefactor | Benefactor | formal-deferential | Hwaran includes Mujin among the Benefactors when greeting Taekyung's companions. |
| 진태경 | 무송 | junior_martial_artist_to_senior_martial_artist | Senior | formal-polite | Taekyung uses 선배님 after recognizing Mu Song as a senior martial artist and disciple of the Seafaring King. |
| 무송 | 진태경 | senior_martial_artist_to_junior_martial_artist | Junior | familiar-teasing | Mu Song calls Taekyung 후배 and jokes about his supposed taste for men. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 주화란 | 사마표 | former_fiancés | Young Sect Leader | formal and guarded | Hwaran formally greets her former fiancé. |
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
| 주화란 | 남호 | pavilion_member_to_hidden_shadow_agent | you / Elder Namho | formal and appreciative | Hwaran respectfully praises the effort Namho invested in mapping Nanman. |
| 남호 | 태산 | guide_to_pavilion_member | Taishan | blunt and exasperated | Namho directly rebukes Taishan for eating the poisonous blood-feeding fungus. |
| 혁무진 | 조장님 | pavilion_member_to_squad_leader | Captain | deferential and dubious | Mujin questions whether the pasture should be called the Nanman Ranch instead of the Nanman Beast Palace. |
| 남호 | 사마표 | guide_to_young_sect_leader | Young Sect Leader | blunt and admonishing | Namho warns Sama Pyo that all grass and animals in the territory belong to the Nanman Beast Palace. |
| 남호 | 주화란 | guide_to_escort_bureau_head | Escort King's granddaughter | approving and familiar | Namho praises Hwaran for recalling Ju Gongsan's records about Nanman. |
| 사마표 | 남호 | young_sect_leader_to_guide | Elder Namho | formal and apologetic | Sama Pyo apologizes after Taishan attempts to seize the calf. |
| 진태경 | 태산 | pavilion_master_to_pavilion_member | Taishan | forceful and commanding | Taekyung orders Taishan to stop eating the bear. |
| 주화란 | 조장님 | pavilion member to squad leader | Captain | familiar and deferential | Hwaran asks Captain where he is going before he confronts the mistreatment. |
| 태산 | 주화란 | Pavilion member to Pavilion member | Young Lady Ju | clipped, childlike, and deferential | Agrees with Ju Hwaran after she mentions the evening banquet. |
| 태산 | 남호 | Fire Dragon Pavilion member to guide | Namho | clipped, childlike, and informal | Taishan directly addresses Namho while asking what Dark Heaven is. |
| 수하 | 수달 | subordinate_to_deputy_stronghold_lord | Deputy Stronghold Lord | deferential but alarmed | Sudal's subordinates challenge his plan to raid Guizhou. |
| 수달 | 수하 | deputy_stronghold_lord_to_subordinates | boys | casual and commanding | Sudal orders his subordinates to raid Guizhou. |
| 주화란 | 태산 | pavilion_member_to_pavilion_member | Young Hero Taishan | formal but stern | Ju Hwaran reprimands Taishan for speaking ominously about Jin and warns that she will muzzle him. |
| 진태경 | 헌터 | field commander to allied Hunters | you; Hunters | blunt and commanding | Orders the human forces to stop asking questions and kill the fleeing Minotaurs. |
| 수달 | 남호 | junior_martial_artist_to_older_stranger | Senior No | respectful | Sudal calls Namho 노 선배님 while mistaking him for a martial master. |
| 남호 | 수달 | older_stranger_to_junior | you | blunt and familiar | Namho addresses Sudal as 네놈 while teasing him about his age and health. |
| 진태경 | 수달 | traveler_to_river_pirate | mister | casual | Jin calls Sudal 아저씨 when asking how far they have traveled. |

## Listed compact profiles

### Human Butcher.md

# Human Butcher (인도)

- **Safe through:** Chapter 833
- **Aliases:** None
- **Role:** Former mysterious Han Chinese mounted-bandit power in Northern Gaoyuan commanding fifty subordinates; a Peak master killed by an unnamed old man in a single move
- **Personality:** Cold, intimidating, and murderous; he kills people as though slaughtering livestock
- **Voice:** Cold, curt, and quietly threatening
- **Relationships:** He is one of four powerful participants at the Northern Gaoyuan gathering, intimidates Temur, and has claimed Ghost Sword Wipeng as his personal target in the proposed attack

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 835
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and an active member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son; he uses quiet practices such as fishing to empty his mind. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad; as a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Fire Dragon Pavilion members accompanying Taekyung. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 835
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader.
- **Personality:** Hungry, self-aware, dryly observant, and pragmatic under pressure; accepts extreme personal risk when duty and the lives of others demand it.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements as well as the Peace Guild's Guild Master, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Magic Johnson is an allied Grand Mage who supplies him with intelligence, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 835
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Ju Hwaran.md

# Ju Hwaran (주화란)

- **Safe through:** Chapter 835
- **Aliases:** Hwaran
- **Role:** Ju Hwaran is a Level 88 Young Bureau Head, leader of the Yongbong Escort Bureau, an experienced Nanman guide, and an active member of the Fire Dragon Pavilion.
- **Personality:** Intelligent, capable, responsible, filial, composed under pressure, and burdened by intense guilt over the escort journey's deaths.
- **Voice:** Clear, polite, restrained, and determined.
- **Relationships:** Escort King Ju Gongsan was her paternal grandfather, Ju Hogun is her father, Heo Jun was her uncle, Sama Pyo was her former fiancé in a political engagement she accepted for her father's sake, Song Ilseom is her direct escort who accompanied her previous journey to Yeongin, and Jin Taekyung is a trusted ally; the Yongbong Escort Bureau has longstanding ties with Yeongin’s inhabitants.

### Mu Song.md

# Mu Song (무송)

- **Safe through:** Chapter 835
- **Aliases:** Ship-Fire Boy
- **Role:** Lord of Water Dragon Stronghold, a Peak master and the Seafaring King's second martial Disciple who controls major Yangtze river traffic in Sichuan, belongs to the Yangtze River Channel League's moderate faction, and is an exceptionally skilled ship captain.
- **Personality:** Ambitious, domineering, impatient with interruptions, strongly attached to life on the water, and capable of pragmatic cooperation when circumstances demand it.
- **Voice:** Deep and low in private, shifting to dry authority or boisterous command when addressing subordinates and rivals.
- **Relationships:** Mu Song belongs to the Yangtze River Channel League's moderate faction, regards Hwang Chung, his senior and Uncle Hwang, as family, must weigh whether the League will support the New Murim Alliance while the Seafaring King retains authority over major League decisions, and has instructed his subordinates to aid Jin Taekyung and the Jin Family of Taiyuan in repayment for past help.

### Namho.md

# Namho (남호)

- **Safe through:** Chapter 835
- **Aliases:** Elder Chao
- **Role:** Namho is an eighty-year-old non-Han Hidden Shadow Pavilion agent who spent more than fifty years operating under the cover of the Poison Flower Pavilion in Nanman and now serves as the Fire Dragon Pavilion’s guide.
- **Personality:** Duty-bound, pragmatic, observant, and willing to use theatrical violence and crude insults to protect an intelligence operation.
- **Voice:** Measured and serious in private, loudly abusive when maintaining his local cover, and capable of theatrically boasting about his exploits.
- **Relationships:** Namho is a Hidden Shadow Pavilion contact for Jin Taekyung and the Fire Dragon Pavilion, receives intelligence from the Pavilion Master, and knows the code used by the Thousand-Faced Fox.

### Sama Pyo.md

# Sama Pyo (사마표)

- **Safe through:** Chapter 835
- **Aliases:** Black Dragon Saber
- **Role:** Young Sect Leader of the Black Dragon Demon Gate, a Morning Star reputed to be no less than the Ten Dragons and Phoenixes, and a member of the Fire Dragon Pavilion.
- **Personality:** Outwardly courteous and smiling, inwardly calculating, but genuinely protective of Taishan; in combat he is ruthlessly pragmatic, survival-focused, and unafraid to stake his life.
- **Voice:** Polite and ingratiating in public, with sardonic humor and controlled evasiveness.
- **Relationships:** Sama Pyo commands the absolutely loyal Taishan, is Sima Gong's son, was Ju Hwaran's former fiancé in a political engagement, and has joined the Fire Dragon Pavilion while openly intending to use Jin Taekyung as a useful card; he is now openly hostile toward fellow member Song Ilseom.

### Sudal.md

# Sudal (수달)

- **Safe through:** Chapter 835
- **Aliases:** None
- **Role:** Sudal is the Deputy Stronghold Lord of the Water Dragon Stronghold and a river pirate who decides to retire upon reaching Sichuan.
- **Personality:** Adventurous, opportunistic, irreverent, and willing to bully his subordinates to pursue a scheme.
- **Voice:** Blunt, profane, boastful, and theatrically commanding.
- **Relationships:** He serves the Water Dragon Stronghold's Stronghold Lord, commands its subordinates, and is currently leading a raid toward Guizhou.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 835
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion; he helped Jin escape the underground prison by blocking the stairs and overpowering the Bai warriors.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo; becomes explosively violent when his meat is threatened.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord, trusts Jin Taekyung as Pavilion Master, and has grown attached to the Fire Dragon Pavilion members.

## Korean source

```text
＃836화



닷새. 짧다면 짧고, 길다면 긴 시간.

저 둘 중 무엇에 더 가까운지는 나도 모르겠다.

하지만 단 한 가지 확신할 수 있는 것은, 장강수로맹이 자랑하는 쾌조선이 장강의 지류(支流)를 따라 운남에서 사천으로 이동하기에는 충분한 시간이라는 사실이다.

‘오랜만이네, 여기도.’

내심 중얼거린 나는 눈 앞에 펼쳐진 광경을 바라보았다.

마치 바다처럼 드넓은 장강의 한 자락.

저문 해와 함께 새카맣게 물들어 버린 강물은 여러 색의 불빛으로 뒤섞여 있었다.

“저건…….”

옆에 있던 남호가 눈을 가늘게 뜨자, 혁무진이 저 멀리 보이는 무수한 불빛의 정체를 알려 주었다.

“놀잇배네요.”

“누가 몰라서 물어본 줄 아느냐?”

“어, 남 노인도 아십니까? 남만에는 저런 거 없어서 처음 보시는 줄 알았는데.”

“허!”

코가 아니라 엉덩이로 뀐 것이 아닐까, 하는 의심이 갈 만큼 강하게 콧방귀를 뀐 남호가 헛웃음을 흘렸다.

“이런 멍청한 놈을 보았나. 그새 노부가 어떤 사람인지 잊은 모양이로구나.”

맞다. 남호는 그저 평범한 이민족 노인이 아니다.

그의 혈관에는 남만인의 피가 흐르지만, 소싯적에 청경채 좀 씹었다는 노강호보다 중원의 지리와 문물에 빠삭한 인물인 건 틀림없었다.

이제는 낡아 버린 과거의 일이라고는 해도, 남호는 한때 은영각(隱影閣)이 보유한 최고의 요원 중 하나였으니까.

“아, 맞네. 너무 가까이에서 보다 보니까 자꾸 깜빡해서.”

멋쩍게 뒷머리를 긁적이는 혁무진을 향해, 남호가 근엄한 표정으로 고개를 끄덕였다.

“노부가 워낙 사교성이 좋고 친근한 인상이라 그런 것이니 이해해 주마.”

“확실히 친근하긴 합니다. 남 노인을 보고 있으면 어릴 적 옆집에 살던 홍씨 할아버지가 떠오르거든요.”

“홍씨라, 누구인지는 몰라도 날 떠올릴 정도면 틀림없이 좋은 분이었겠군.”

“고리채(高利債)로 큰 부를 쌓은 사람이었죠. 그래서인지 저잣거리에 나갈 때마다 꼭 호위를 대동하고는 했었는데…… 뭐, 원한 살 만한 짓을 하도 많이 해서 결국 죽긴 했습니다.”

“…….”

“그런데 놀잇배는 왜 그렇게 신기하게 쳐다보신 겁니까? 이미 다 알고 계셨으면서.”

이 새끼가 지금 나랑 한번 해보자는 건가.

딱 그런 눈빛으로 혁무진을 노려보던 남호가 한숨을 푹 내쉬었다.

“신기해서 쳐다본 게 아니라, 허탈해서 그랬다.”

“허탈이요?”

“그래, 중원은 참 변한 게 없구나, 하는 생각이 들어서.”

저 멀리 환한 빛과 함께 장강을 유영하는 선박들을 응시하며, 남호가 천천히 말을 이었다.

“이 세상 누군가는 무너지는 천하를 바로 세우기 위해 목숨을 걸고 싸우지만, 또 다른 누군가는 놀잇배를 띄워 향락에 흠뻑 취한다. 그러니 어찌 우습고 허탈하지 않겠느냐.”

“아.”

“아직 한없이 젊은 네 녀석을 탓하는 것이 아니다. 저들을 향해 분노하라 강요하는 것 또한 아니다. 다만 한 가지만큼은 부탁하고 싶구나.”

어느덧 입을 다문 혁무진과 다른 이들의 모습을 하나하나 눈에 담은 남호가 씁쓸한 목소리로 덧붙였다.

“어떤 모습을 보더라도 부디 실망하지 말아라. 의지만 있다면 몇 번이고 쓰러져도 다시 일어날 수 있지만, 의지가 꺾인다면 그 무엇도 이룰 수 없다.”

평소의 남호가 아니다.

이건 정마대전이라는 거센 파도를 겪은 선배로서, 한 사람의 노인으로서 건네는 충고.

그리고 지금 이 순간 남호의 시선이 유독 내게 오래 머무른다고 느낀 것은, 결코 단순한 착각이 아닐 것이다.

‘걱정되겠지. 지금의 나는, 열화신룡 진태경은 제대로 된 전란(戰亂)을 겪어 보지 못한 어린애니까.’

현대에서도 젊은 나이에 속하는 나지만, 무림에서는 특히 우려의 시선이 있을 수밖에 없다.

본격적으로 이름을 알리기 시작한 지 불과 이 년도 되지 않은 무림 초출. 거기에 더해 약관을 갓 넘긴 나이.

나이 지긋한 노강호가 바라보기에, 태원진가의 진태경은 정신적인 성숙함을 기대하기에는 너무나도 앳된 청년이었으니.

물론…….

‘헌터 진태경은 다르지.’

누군가가 내게 어른이 되었냐고 물어본다면, 글쎄. 아마도 아니라고 대답할 것이다.

나는 지금도 종종, 혹은 꽤 자주 애처럼 굴고 감정적으로 행동하는 경우가 많으니까.

하지만 적어도 주위에서 걱정할 만큼 쉽게 흔들리지는 않는다.

아니, 그러기에는 이미 너무 많은 일을 겪었다.

같은 편이라고 믿었던. 심지어 한때 선망의 대상이었던 사람에게도 뒤통수를 얻어맞았고 그 과정에서 가까운 지인을 잃기도 했다.

목숨을 걸고 어떻게든 사람들을 구하기 위해 몸부림치는 와중에도 언론은 나를 물어뜯었으며, 두 편으로 갈라진 네티즌들은 또 다른 전쟁을 벌였다.

한 나라의 수도가 무너지고 십만 명의 사상자가 발생한다 해도, 방관자는 어디에나 존재한다.

무감각하게 뉴스를 클릭한 뒤, 인터넷 기사를 절반도 보지 않고 닫아 버리는 이들처럼.

그러는 이유?

‘뻔하지.’

새로운 게임이 잡혔거나, 클럽에 갈 시간이 되었거나.

혹은 옆 동네가 아닌 지구 반대편에서 벌어지는 일이라면 수만 명이 죽어도 신경 쓰지 않는 유형의 인간이거나.

한때는 그 모든 것 하나하나가 고통이었다.

하지만 얼굴도 모르는 수많은 누군가에 의해 할퀴어진 내 마음은 시간이 흐르자 굳은살이 배겨 단단해졌고, 폐부를 찌르는 것 같던 고통도 어느 순간 익숙해졌다.

그래, 그럼 된 거다.

그런 것 하나하나에 상처받고 괴로워하기에는, 내가 짊어진 짐이 너무나도 많다.

“잘들 노네요.”

생각을 끝마친 내가 피식 웃으며 내뱉은 한 마디에, 남호의 눈이 크게 뜨였다. 그리고 이내 그 역시 쓴웃음을 머금었다.

“그래, 그렇구나.”

이 정도로 남호가 안심했을지는 모르겠다. 그러나 어느 정도의 시간이 흐른 뒤에는 그도 저절로 깨닫게 될 것이다.

열화신룡 진태경이 단순히 힘과 재능만 넘치는 어린놈이 아니라는 것을.

“갑시다. 선착장에 도착하는 즉시 지체하지 않고 움직일 테니, 다들 늦장 부릴 생각하지 말고.”

내 지시에 태산이 번쩍 손을 치켜들었다.

“태산이. 오향장육이 먹고 싶다.”

“오향장육?”

“응. 태산이가 제일 좋아한다.”

“오향장육, 좋지. 맛있고.”

“조장. 좋다. 태산이랑 통한다.”

“그런데 괜찮냐. 객잔 갈 때쯤에는 강물을 하도 처먹어서 위장에 오향장육이 들어갈 자리가 없을 텐데.”

깊이를 알 수 없을 만큼 시커멓게 물든 강물과 장강찍먹형을 위한 만반의 준비를 끝마친 나를 번갈아 바라보던 태산이 슬그머니 손을 내렸다.

“아니다. 태산이 다시 생각해 보니 오향장육 싫다.”

“확실해?”

“으응. 확실하다…….”

축 늘어진 목소리로 대답하는 태산을 사마표는 측은하게 바라보았고, 또 다른 의미로 안타까운 표정을 짓고 있던 남호는 수적들의 우두머리를 향해 손짓했다.

“어이, 해달. 이리와 보게.”

“수달입니다요.”

“그러니까 해달.”

“수달…….”

“해달.”

“…….”

사람 이름 갖고 장난을 치다니.

남호의 막무가내 어깃장에 말대꾸할 힘조차 잃어버린 수적의 얼굴을 보고 있자니 내가 다 마음이 아프다.

나는 안쓰러운 마음을 담아 그의 어깨를 두드려 주었다.

“자, 이제 다 도착했어요. 조금만 더 기운 차립시다.”

“가, 감사합니다. 진 대협.”

“우리가 그동안 여러모로 심했던 거 알아요. 나중에 무송 선배 만나면, 헤임달 아저씨가 고생 많이 했다고 말씀드릴게.”

“죄송한데 헤임달은 또 누구…….”

“아니, 지금 당신 이름이 중요한 게 아니라 우선 선착장까지 가자고. 아저씨 우리랑 떨어지는 게 아쉬워? 그러면 한 칠 주야 정도 바람 쐬면서 장강 한 바퀴 돌아?”

초점이 흐릿하던 해달, 수달, 헤임달의 눈동자가 번뜩인다. 분노인지 광기인지 모를 감정을 내비친 그가 수하들을 향해 목이 터져라 외쳤다.

“이 게을러터진 놈들아! 속력을 더 높여라!”

“…….”

반응을 보아하니 정말 어지간히 힘들었던 모양이다.

하긴, 하나같이 통제 불가능한 화룡각 대원들의 면면을 보자면 힘든 것이 당연하다.

그나마 우리 일행의 홍일점이자 유일한 정상인이었던 주화란조차 이상 징후를 보이고 있었으니까.

“아, 꼭 이 정도로 시끄럽게 소리 질러야 하나? 가뜩이나 조장님 힘드신데. 주화입마라도 걸리면 어쩌려고 저러는 거지?”

“…….”

솔직히 이쯤 되니 듣는 나도 무섭다.

쉴새 없이 입술을 달싹거리며 뭐라 중얼거리는데, 딕션은 무림맹 공채 아나운서 수준에 발성은 성악가라 한 마디 한 마디가 대못처럼 귀에 때려 박힌다.

선실 밖으로 나선 지 한나절쯤 된 나도 이 정도니, 꼬박 닷새를 시달린 수적들은 이미 얼굴이 새파랗게 질려 있는 상태.

‘주화입마는 나 대신 쟤들이 걸린 것 같은데…….’

내가 심각하게 수적들의 상태를 고민하고 있던 그때, 쾌조선을 진두지휘하며 마지막 불꽃을 불태우고 있던 우두머리가 황급히 다가왔다.

“지, 진 대협. 문제가 생겼습니다.”

그렇지 않아도 흉신 악살이나 다름없는 얼굴이 딱딱하게 굳어 있다.

그나마 여기가 장강이라 다행이지, 위대한 항로였으면 지금 저 얼굴만으로도 현상금이 치솟고 정부의 표적이 되었을 거다.

나는 진심 어린 걱정을 담아 물었다.

“내 이럴 줄 알았다. 혹시 기혈이 엉켰어요?”

“예? 아닙니다. 저는 완전 멀쩡한…….”

“손 닿는 데까지 힘쓸 테니까 그냥 참지 말고 속 시원하게 얘기해요. 안색이 너무 거무죽죽한데. 지금 시선도 완전히 다른 곳을 향하고 있어요. 맛탱이가 갔어.”

“얼굴은 처음 태어났을 때부터 그랬습니다. 눈은 열다섯 살 때 아버지한테 얻어맞은 이후로 쭉 이렇고요.”

“예?”

“오해는 마십시오. 단지 너무 놀라셨을 뿐이에요. 잘 주무시다가 불현듯 잠에서 깨어나셨는데, 눈을 뜨자마자 제 얼굴을 보셨거든요. 아마 저라도 주먹이 나갔을 겁니다.”

“아, 춘부장께서…….”

평범한 사람이라면 여기서 당황했을 것이다. 뭐라 이어 가야 할지 몰라 말도 버벅거리고, 상대방의 눈치를 보다가 하지 않느니만 못한 사과를 했겠지.

하지만 초절정 고수다운 침착성을 발휘한 나는, 어느덧 허공을 수놓고 있는 폭죽을 자연스럽게 가리켰다.

“와, 저기 봐요. 폭죽 터진다. 불꽃 축제하나?”

“폭죽은 맞는데, 불꽃 축제인지 뭔지는 아닙니다. 그래서 더욱 문제인 거고요.”

“문제라니, 폭죽 좀 쏘는데 뭐가?”

“자세히 보십시오. 하늘 말고 배를요.”

배? 배가 왜?

나는 의문과 함께 반사적으로 시선을 내렸다.

그리고 어느새 훌쩍 가까워진 놀잇배들을 보며, 마침내 수달, 해달, 헤임달이 황급히 다가온 이유를 깨달았다.

“저건…….”

“전부 놀잇배가 아닙니다. 어쩐지 보이는 불빛이 평소보다도 너무 많았어요.”

말 그대로였다.

멀리서만 봤을 때는 그저 수많은 불빛 중 하나로 느껴졌던 그 선박들은, 내가 아는 놀잇배보다 열 배는 거대하고 단단해 보였다.

그러니까 마치…….

“허, 꼭 군선(軍船) 같네.”

“군선 맞습니다.”

“아.”

맞다는 말에 잠시 멈칫했지만, 별 상관은 없었다.

군선이고 나발이고 무슨 걱정이란 말인가.

지금 내가 탄 쾌조선에는 장강수로맹의 깃발이 휘날리고 있고 이 거대한 수적 집단이 관(官)에 뇌물을 퍼부어 친목질을 다져 놓은 지 오래라는 사실쯤은 익히 알고 있다.

아니, 적어도 내가 아는 바로는 그랬다.

펑. 펑. 퍼엉!

연달아 터지는 폭죽과 함께 비스듬히 옆면으로 회전하는 군선들. 그리고 그 단단한 나무 틈새로 거무스름한 무언가가 보이기 전까지는.

“해달, 저게 뭐야.”

“대포 같은데요.”

“나도 알아. 헤임달 이 새끼가 사람을 놀리나. 그런데 왜 저걸 우리한테 겨누냐고.”

이제는 완전히 이름을 잃어버린 수적 우두머리가 완전히 포기한 얼굴로 허허 웃었다.

“방금 쏜 폭죽이 공격 신호였으니까요.”

“뭐?”

내가 멍하니 되물은 그 순간.

퍼버버버벙!

백여 개의 포신(砲身)이 동시에 화염을 내뿜었다.
```

## Final English reading copy

```markdown
# Chapter 836

Five days. A short time, if you looked at it one way; a long time, if you looked at it another.

I didn’t know which one it was closer to.

But one thing I could say for certain: it was enough time for the swift ship the Yangtze River Channel League was so proud of to travel from Yunnan to Sichuan along a tributary of the Yangtze.

*It’s been a while since I was here.*

I murmured to myself and looked at the scene spread out before me.

A stretch of the Yangtze so vast it looked like the sea.

The river, turned pitch-black with the setting sun, was streaked with lights of every color.

“What are those…?”

Namho narrowed his eyes. Hyuk Mujin explained what the countless lights in the distance were.

“Pleasure boats.”

“Do you think I asked because I didn’t know?”

“Oh, you know about those too, Old Man Nam? I thought you were seeing them for the first time, since there’s nothing like that in Nanman.”

“Hah!”

Namho snorted so hard I wondered if he’d done it through his ass instead of his nose, then gave a hollow laugh.

“Have you ever seen such a fool? You’ve already forgotten what kind of man this old man is.”

That was right. Namho wasn’t just some ordinary old man from another people.

Nanman blood ran through his veins, but there was no doubt he knew the Central Plains’ geography and customs better than some old martial-world veteran who’d chewed his fair share of bok choy in his youth.

Even if it was all in the past now, Namho had once been one of the finest agents in the Hidden Shadow Pavilion.

“Oh, right. I keep forgetting because you’re always right there.”

Hyuk Mujin scratched the back of his head sheepishly. Namho nodded at him with a solemn expression.

“I’ll forgive you. It’s only natural—you find this old man so sociable and approachable.”

“You are approachable, all right. Looking at you reminds me of Grandpa Hong, who lived next door when I was a kid.”

“Grandpa Hong? Whoever he was, he must have been a good man if he reminded you of me.”

“He made a fortune lending money at exorbitant interest. He always had bodyguards with him whenever he went out to the market, probably because he did so many things to make enemies. Anyway, he ended up getting killed.”

“……”

“Then why were you looking at the pleasure boats like they were so fascinating, if you already knew what they were?”

Was this bastard trying to start something with me?

Namho glared at Hyuk Mujin with exactly that look, then let out a deep sigh.

“I wasn’t looking because I found them fascinating. I felt empty.”

“Empty?”

“Yes. It made me think about how little the Central Plains have changed.”

Namho gazed at the ships gliding along the Yangtze, their lights bright in the distance, and continued slowly.

“Some people in this world risk their lives fighting to set a collapsing realm back on its feet, while others float pleasure boats and lose themselves in indulgence. How could that not seem ridiculous? How could it not leave me feeling empty?”

“Ah.”

“I’m not blaming you, young as you are. Nor am I telling you to be angry with them. But there’s just one thing I’d like to ask of you.”

Hyuk Mujin had fallen silent. Namho took in the faces of him and the others one by one, then added in a bitter voice:

“No matter what you see, please don’t lose heart. If you have the will, you can get back up no matter how many times you fall. But if your will is broken, you won’t accomplish a thing.”

This wasn’t the Namho we usually saw.

This was advice from a veteran who’d weathered the storm of the Great Faction War—and from an old man.

And the feeling that Namho’s gaze lingered on me in particular at that moment wasn’t just my imagination.

*He must be worried. The Jin Taekyung I am now—the Blazing Flame Divine Dragon—has never been through a proper war. I’m just a kid.*

I was young even by modern standards, but in Murim there was all the more reason for people to look at me with concern.

I’d only started making a name for myself in Murim less than two years ago. And on top of that, I’d barely passed twenty.

To an old martial-world veteran, Jin Taekyung of the Jin Family of Taiyuan was far too young to be expected to have matured mentally.

Of course…

*Hunter Jin Taekyung is different.*

If someone asked whether I’d grown up, I’d say… probably not. I still acted like a kid now and then—or pretty often, honestly—and I had a bad habit of letting my emotions get the better of me.

But at least I wasn’t so easily shaken that the people around me needed to worry.

No. I’d already been through too much for that.

I’d been stabbed in the back by someone I’d thought was on my side—someone I’d once even looked up to. And in the process, I’d lost someone close to me.

While I struggled to save people, risking my life to do it, the media tore into me, and people online split into two camps and waged another war.

Even when a country’s capital falls and a hundred thousand people are killed or injured, there are bystanders everywhere.

People who click the news without a hint of feeling, then close the article before they’ve even read half of it.

Why?

*It’s obvious.*

They’ve got a new game to play, or it’s time to head to the club.

Or they’re the type who don’t care if tens of thousands die, as long as it’s on the other side of the world and not in the neighborhood next door.

Once, every one of those things hurt.

But as time passed, my heart—scratched raw by countless strangers whose faces I’d never seen—grew calloused and hard. The pain that used to pierce deep into me eventually became familiar.

Yeah. That was that.

I had too much on my shoulders to let every little thing wound me and make me suffer.

“They’re having a good time.”

I finished thinking, gave a quiet laugh, and said it aloud. Namho’s eyes widened at my words. Then he, too, gave a bitter smile.

“Yes. They are.”

I didn’t know how much that had reassured him. But after some time passed, he’d understand on his own.

That the Blazing Flame Divine Dragon Jin Taekyung wasn’t just some kid overflowing with strength and talent.

“Let’s go. The moment we reach the landing, we move out without delay. Don’t anyone think about dawdling.”

At my order, Taishan shot his hand up.

“Taishan wants five-spice pork.”

“Five-spice pork?”

“Yes. Taishan’s favorite.”

“Five-spice pork, sure. It’s delicious.”

“Captain. Good. Taishan and Captain agree.”

“But are you sure? By the time we get to an inn, you’ll have swallowed so much river water there won’t be room in your stomach for five-spice pork.”

Taishan looked back and forth between the river, black enough to hide its depth, and me, who’d made thorough preparations for the Yangtze dip-and-taste punishment. Then he slowly lowered his hand.

“No. Taishan thought again. Taishan doesn’t want five-spice pork.”

“You sure?”

“Mm-hm. Sure…”

Taishan answered in a drooping voice. Sama Pyo looked at him with sympathy, while Namho—wearing a look of regret for a different reason—beckoned to the head of the river pirates.

“Hey, sea otter. Come here.”

“It’s Sudal.”

“That’s what I said. Sea otter.”

“Sudal…”

“Sea otter.”

“……”

Watching the river pirate’s face as Namho stubbornly mangled his name until he didn’t even have the energy to argue, I felt sorry for him.

I patted his shoulder sympathetically.

“Come on, we’re almost there. Just hang in there a little longer.”

“Th-thank you, Great Hero Jin.”

“I know we’ve been pretty hard on you. When we see Senior Mu Song later, I’ll tell him Uncle Heimdall had a rough time.”

“Sorry, but who’s Heimdall…?”

“Your name isn’t important right now. Let’s just get to the landing first. Mister, are you sad to leave us? If you are, how about we take a trip around the Yangtze for about a week?”

Sudal, Sea Otter, Heimdall—whatever his name was—his unfocused eyes suddenly flashed. His expression gave away some emotion I couldn’t quite place, somewhere between anger and madness. He bellowed at his subordinates until his voice nearly gave out.

“You lazy bastards! Pick up the speed!”

“……”

Judging by his reaction, they really must have had a rough time.

Then again, with the Fire Dragon Pavilion members—each one more impossible to control than the last—it was only natural.

Even Ju Hwaran, the only woman in our party and the only sane person, was showing signs of something being wrong.

“Ah, does he have to shout so loudly? The Captain’s already exhausted. What if all that noise gives him qi deviation? What’s he thinking?”

“……”

At this point, even hearing it scared me.

She kept moving her lips and muttering under her breath. Her diction was at the level of a Murim Alliance announcer, and her projection was like an opera singer. Every word hammered into my ears like a nail.

I’d only been outside the cabin for half a day, and I was already like this. The river pirates, who’d endured it for five whole days, had gone pale.

*They look more like the ones about to suffer qi deviation than me…*

As I seriously considered the river pirates’ condition, their leader—who’d been directing the swift ship and burning through the last of his energy—hurried over.

“G-Great Hero Jin. There’s a problem.”

His face, already no less terrifying than a demon’s, had gone stiff.

At least we were on the Yangtze. If we’d been on the Grand Line, his face alone would’ve sent his bounty soaring and made the government mark him as a target.

I asked with sincere concern.

“I knew this would happen. Are your qi and blood all tangled up?”

“What? No. I’m perfectly fine—”

“I’ll do whatever I can. Don’t hold it in—tell me what’s going on. Your complexion’s awfully dark. And you’re looking off in a completely different direction. You’re a wreck.”

“My face has looked like this since I was born. And my eyes have been like this ever since my father beat me when I was fifteen.”

“Pardon?”

“Please don’t misunderstand. My father was just startled. He’d been sleeping soundly, then suddenly woke up and saw my face the moment he opened his eyes. If it were me, I’d probably have thrown a punch too.”

“Ah. Your father…”

A normal person would’ve been flustered here. They’d stammer, unsure what to say next, then watch the other person’s face and apologize in a way that was worse than not apologizing at all.

But, using the composure befitting a Supreme Peak master, I naturally pointed up at the fireworks that were now filling the sky.

“Whoa, look over there. Fireworks. Are they having a festival?”

“They are fireworks, but it’s not a festival. That’s what makes it a problem.”

“A problem? What’s wrong with setting off a few fireworks?”

“Look closely. At the ships, not the sky.”

The ships? What about them?

I lowered my eyes without thinking.

And when I saw how close the pleasure boats had gotten, I finally understood why Sudal had hurried over.

“Those are…”

“They’re not all pleasure boats. No wonder there were so many more lights than usual.”

He was right.

From far away, those ships had looked like just a few more lights among the many. But now that they were closer, they looked ten times bigger and sturdier than any pleasure boat I knew.

They were more like…

“Huh. They look like military vessels.”

“They are military vessels.”

“Oh.”

I paused for a moment when he confirmed it, but it didn’t really matter.

Military vessels, my ass. What was there to worry about?

The Yangtze River Channel League’s flag was flying from the swift ship I was on, and I knew perfectly well that this huge band of river pirates had long ago greased the officials’ palms and made friends in the right places.

Or at least, that was what I thought I knew.

*Bang. Bang. Baaang!*

Fireworks burst one after another as the military vessels angled around to present their broadsides. Then, through the gaps in the sturdy wooden hulls, something dark came into view.

“Sudal, what’s that?”

“Looks like a cannon.”

“I know that. Are you messing with me, Heimdall? Why are they pointing it at us?”

The river pirate leader, who’d by now completely lost his name, gave a hollow laugh.

“Because the fireworks they just set off were the signal to attack.”

“What?”

The moment I asked again, dumbfounded—

*BOOOOM!*

About a hundred cannon barrels belched fire at once.
```

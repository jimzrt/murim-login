<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0715.txt",
      "sha256": "862726f56a465e9a5ac1f80e95547bd94790be45fb81c43634ddcad68a95aa7c",
      "bytes": 13637
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "72254a1fd1f792fa159a77fc6f633cae4ff5724f2cbd5c353c3c57f11f5740db",
      "bytes": 1561
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "a9ca28e549ccb6140f955aaef16e16b815c5d9199162a46409a090b831bc65ee",
      "bytes": 208075
    },
    {
      "path": "characters/Blood Monk.md",
      "sha256": "70005810f8cf58bd164441c8f38c666614745bda7c5eee2e55c419fd92a7d6c7",
      "bytes": 542
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "856dcb1261097aaa0cdc54be3f729e5c844cb1555beeccfd52ffc98d16268aae",
      "bytes": 1464
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "682cab3aa20b01be08ac87bf43f8341e49b42028e72c2375a5e896f52a15e60f",
      "bytes": 1702
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "80912159a966813481c763cbe49b5a1e335e0504687dcb61e1aa662dc122c629",
      "bytes": 1787
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "d81539b5ef418881ab04a6eebaf39ae1412847a23515960650408bbb51469357",
      "bytes": 622
    },
    {
      "path": "characters/Ju Hwaran.md",
      "sha256": "89e13b3608b1dc54431880fd82bfc859a21aae60d6ec815260a43afe769e9f25",
      "bytes": 1196
    },
    {
      "path": "characters/Namho.md",
      "sha256": "853a8d86fa52540c9ac597f4afef0d7be1f990778bf78e383d81be972954a443",
      "bytes": 843
    },
    {
      "path": "characters/Sama Pyo.md",
      "sha256": "0a5aaa7f53a95c277ec01f325665fbf0a1857482cfbbca7e1bf5af923e96cc9b",
      "bytes": 936
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "cf9da5e4938fc38d7b828a145c3c59bb2a12147c3259835db164855e8a0f5145",
      "bytes": 787
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "04e05b397803c14da83d4095d0d350b37c1f097208d8c3b5761113c8a8df99c4",
      "bytes": 218560
    }
  ],
  "estimated_tokens": 13251
}
-->

# Durable State Update — Chapter 715

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 715. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 715. Profile updates may replace only one
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
  "chapter": 715,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 715,
    "continuity_sources": [715],
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
    "The rift has closed, demonic qi has disappeared, and the sacred stone is purifying the corrupted energy.",
    "The mutated guardian spirit was killed by Jin Taekyung and Jeok Cheongang after sacrificing itself and requesting death.",
    "The Southern Heaven Demon Empress is dead.",
    "Baeksang knowingly served Dark Heaven's plan and sacrificed Nanman's forces to advance it.",
    "Baeksang is dead, having been killed by the Beast Miao King at his own request.",
    "Dark Heaven has kept Baekhwi alive in a deep sleep, and Baeksang accepted the Southern Heaven Demon Empress's bargain to recover him.",
    "Baeksang created the Baekcheon Unit as a contingency to stop the catastrophe.",
    "Jin Taekyung was unconscious for seven days after Baeksang's death and has now awakened.",
    "Baeksang's final public warning claimed that Dark Heaven will eventually devour Nanman."
  ],
  "continuity_sources": [
    714
  ],
  "open_questions": [
    "What is Baekhwi's condition, and can he be recovered from his deep sleep?"
  ],
  "safe_through": 714,
  "temporary_decisions": [
    "Continue rendering the guardian spirit's 의념 as Will.",
    "Render the sacred stone's cleansing effect as purification.",
    "Retain Old Master as Jin Taekyung's address to Jeok Cheongang.",
    "Retain established renderings of Blazing Flame Divine Palm and Sacrifice and Rest.",
    "Render 백천 as Baekcheon and the new directional titles as Eastern Heaven Demon Lord and East-West Heaven Demon Empress."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 주화란    | **Ju Hwaran**      |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 중원     | **Central Plains**                               |                                                       |
| 전각     | **pavilion**                                 | Use “hall” only when established for a specific named building |
| 화신귀무   | **Dance of the Fire God and Demon** |
| 스킬               | **Skill**                      |
| 하남     | **Henan**              |
| 정마대전   | **Great Faction War**         |
| 노부      | **this old man / I**                                            |
| 혈승 | **Blood Monk** | Sobriquet of the unidentified bald martial artist active in Guizhou. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 남호 | **Namho** | Hidden Shadow Pavilion code name; literally associated with amber from the south. |
| 사마표 | **Sama Pyo** | Young Sect Leader of the Black Dragon Demon Gate. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 화염신장 | **Flame Divine Palm** | Jopil's deadly palm technique, noted when Taekyung compares Jopil with Mukyung. |
| 만년한철 | **Ten-Thousand-Year Cold Iron** | Material that destroys Pung Yang's Body-Protecting Qi when the Unnamed Sword satisfies a specific condition. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 태양권 | **Solar Fist** | Martial art mentioned in Taekyung's joke about Unnamed's forehead strike. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 멸염신권 | **Flame-Extinguishing Divine Fist** | Named fist technique Taekyung announces at the chapter's end. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 노야 | **Old Master** | Taekyung's private address for Jeok Cheongang. |
| 화란 | **Hwaran** | Familiar short form of Ju Hwaran. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 촌각 | **moments** | Short intervals disappearing from Jeok's day. |
| 화기 | **fire qi** | The fire nature imparted to internal energy by the Fire Gate Divine Technique. |
| 화룡각 | **Fire Dragon Pavilion** | New name chosen for Taekyung's pavilion. |
| 내궁 | **Inner Palace** | The inner compound of the Nanman Beast Palace. |

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
| 주화란 | 진태경 | escort_bureau_leader_to_famous_younger_martial_artist | Young Hero Jin | formal-deferential | Hwaran introduces herself as the Young Bureau Head and formally greets Taekyung as 진 소협. |
| 진태경 | 주화란 | visitor_to_young_bureau_head | Young Lady Ju | formal-polite | Taekyung uses 주 소저 while announcing that his party must leave. |
| 주화란 | 혁무진 | rescued_survivor_to_benefactor | Benefactor | formal-deferential | Hwaran includes Mujin among the Benefactors when greeting Taekyung's companions. |
| 중년인 | 진태경 | veteran civilian Hunter to celebrated allied Hunter | Mr. Jin | formal-polite and awed | The casualty clerk addresses Jin as 진 선생님 after Jin asks him to list Lei Fei among the dead. |
| 진태경 | 중년인 | celebrated Hunter to older fellow Hunter | sir | casual and teasing | Jin addresses the older Hunter as 아저씨 while joking with him and giving him instructions. |
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
| 남호 | 각주 | guide to pavilion master | Pavilion Master | blunt, hostile, and abusive | Namho addresses Jin as 각주 while accusing him of causing the disturbance. |
| 사마표 | 각주 | Fire Dragon Pavilion member to pavilion master | Pavilion Master | formal but sardonic | Sama Pyo addresses Jin as 각주 while questioning his account of the incident. |
| 태산 | 각주 | Fire Dragon Pavilion member to pavilion master | Pavilion Master | clipped, childlike, and informal | Taishan directly asks Jin whether his Lord Sama Pyo is safe. |
| 적천강 | 의원 | interrogator_to_physician | you; quack | blunt and threatening | Jeok shakes the physician and demands an explanation for Jin's seven-day sleep before ordering him to summon the Beast Miao King. |

## Listed compact profiles

### Blood Monk.md

# Blood Monk (혈승)

- **Safe through:** Chapter 711
- **Aliases:** Jeok Cheongang; Fire King
- **Role:** The Blood Monk is Jeok Cheongang, the Fire King and legendary martial master who uses a steel Zen staff and the Flame Divine Palm.
- **Personality:** As Jeok Cheongang, the Blood Monk is gruff, blunt, protective toward his Disciple, and prone to profane mockery.
- **Voice:** Not established.
- **Relationships:** His connection to Dark Heaven and Nanman is unknown.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 674
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and a member of the Fire Dragon Pavilion; he is currently bound and unconscious under the reconnaissance squad's guard after being struck at a Sleep Acupoint.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son; he uses quiet practices such as fishing to empty his mind. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad; as a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Fire Dragon Pavilion members accompanying Taekyung. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 714
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm, and the occupant of the chief seat of the Murim Alliance's Five Kings Hall.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 714
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple, the Fire Gate Clan's nineteenth successor, and the Pavilion Master of the Fire Dragon Pavilion within the Murim Alliance, a Supreme Peak master with the Heavenly Martial Physique and Force, and a publicly recognized S-rank-level Hunter who formally retains an A-rank license.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 714
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Ju Hwaran.md

# Ju Hwaran (주화란)

- **Safe through:** Chapter 665
- **Aliases:** Hwaran
- **Role:** Ju Hwaran is a Level 88 Young Bureau Head, leader of the Yongbong Escort Bureau, a member of the Fire Dragon Pavilion, an experienced Nanman escort guide with route knowledge from the Escort King's records, someone who can understand the Miao and Bai languages, and a volunteer accepted for the scouting mission to investigate the Blood Monk in Guizhou; she is currently alive but subdued with a Pressure-Point Strike.
- **Personality:** Intelligent, capable, responsible, filial, composed under pressure, and burdened by intense guilt over the escort journey's deaths.
- **Voice:** Clear, polite, restrained, and determined.
- **Relationships:** Escort King Ju Gongsan was her paternal grandfather, Ju Hogun is her father, Heo Jun was her uncle, Sama Pyo was her former fiancé in a political engagement she accepted for her father's sake, Song Ilseom is her direct escort who accompanied her previous journey to Yeongin, and Jin Taekyung is a trusted ally; the Yongbong Escort Bureau has longstanding ties with Yeongin’s inhabitants.

### Namho.md

# Namho (남호)

- **Safe through:** Chapter 679
- **Aliases:** Elder Chao
- **Role:** Namho is an eighty-year-old non-Han Hidden Shadow Pavilion agent who spent more than fifty years operating under the cover of the Poison Flower Pavilion in Nanman and now serves as the Fire Dragon Pavilion’s guide.
- **Personality:** Duty-bound, pragmatic, observant, and willing to use theatrical violence and crude insults to protect an intelligence operation.
- **Voice:** Measured and serious in private, but loudly abusive and convincing when maintaining his local cover.
- **Relationships:** Namho is a Hidden Shadow Pavilion contact for Jin Taekyung and the Fire Dragon Pavilion, receives intelligence from the Pavilion Master, and knows the code used by the Thousand-Faced Fox.

### Sama Pyo.md

# Sama Pyo (사마표)

- **Safe through:** Chapter 679
- **Aliases:** Black Dragon Saber
- **Role:** Young Sect Leader of the Black Dragon Demon Gate, a Morning Star reputed to be no less than the Ten Dragons and Phoenixes, and a member of the Fire Dragon Pavilion.
- **Personality:** Outwardly courteous and smiling, inwardly calculating, but genuinely protective of Taishan; in combat he is ruthlessly pragmatic, survival-focused, and unafraid to stake his life.
- **Voice:** Polite and ingratiating in public, with sardonic humor and controlled evasiveness.
- **Relationships:** Sama Pyo commands the absolutely loyal Taishan, is Sima Gong's son, was Ju Hwaran's former fiancé in a political engagement, and has joined the Fire Dragon Pavilion while openly intending to use Jin Taekyung as a useful card; he is now openly hostile toward fellow member Song Ilseom.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 714
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion; he helped Jin escape the underground prison by blocking the stairs and overpowering the Bai warriors.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo; becomes explosively violent when his meat is threatened.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord, trusts Jin Taekyung as Pavilion Master, and has grown attached to the Fire Dragon Pavilion members.

## Korean source

```text
＃715화



약재 냄새가 가득한 방 안. 그리고 손에 대침을 든 채 바들바들 떨고 있는 한 중년인과 그의 멱살을 붙잡고 있는 적천강.

‘각 나온다. 각 나와.’

이제 겨우 잠에서 깨어났음에도 일련의 상황을 파악하는 건 간단했고, 의원으로 짐작되는 중년인은 적천강의 어깨너머로 눈을 껌뻑거리는 나를 발견하고 외쳤다.

“어어! 어어어! 깨어났다! 깨어났습니다아아!”

“…….”

우리 엄마가 이 자리에 있었어도 저것보단 덜 기뻐했겠는데.

장담하는데, 저건 환자가 깨어나서 기쁜 게 아니라 연쇄살인마 앞에서 경찰을 발견한 피해자의 환호다.

그리고 그런 의원의 멱살을 순순히 놔준 적천강은 고개를 돌려 나를 바라보았다.

그저 말없이, 의원이 허겁지겁 빠져나간 후에도 한참이나.

그러더니 불쑥 입을 열었다.

“늦게도 일어났구나.”

퉁명스러운 목소리에 나는 어깨를 으쓱해 보였다.

사실 지랄 같은 악몽을 꿨는데 노야가 제 목을 물어뜯었습니다, 라고 말할 수는 없는 것 아닌가.

“푹 잤느냐?”

“뭐, 그럭저럭요.”

“몸은?”

“가뿐합니다. 머리도 맑고요.”

한 치의 과장도 없는 사실이다. 몸은 깃털처럼 가벼웠고, 긴 잠으로 피로를 날려 버린 머릿속은 어느 때보다 또렷했다.

‘칠 주야 동안 의식을 잃었다고 했었나.’

그간의 피로가 어지간히 컸던 모양이었다.

내 입으로 말하긴 뭐하지만, 나 정도 경지에 이른 초절정 고수가 일주일이나 정신을 차리지 못하는 건 드문 경우니까.

그러던 중 문득, 나도 모르게 한마디가 툭 튀어나왔다.

“다행이네요.”

“뭐가 말이냐?”

“이게 꿈이 아니라서.”

“…….”

“정말 다행이에요.”

나는 감회에 젖은 눈빛으로 주위를 둘러보았다.

반쯤 열린 창문 사이로 햇빛이 스며들고, 새들이 지저귀는 울음소리가 귓가를 간지럽힌다. 저 멀리에서 두런두런 대화를 나누며 지나가는 사람들의 인기척이 느껴졌다.

‘나, 살아 있구나.’

아이러니한 일이다.

입과 코로 숨을 쉬면서도, 감각으로 현실을 인지했음에도 내가 살아 있다는 사실이 쉽게 믿기지 않는다는 것은.

동시에 텅 빈 공허함이 나를 사로잡았다.

순간 창가에 내려앉은 햇빛 위로 내궁을 휘감았던 짙은 어둠이, 피 웅덩이에 머리를 박고 쓰러진 무수한 시체들의 모습이 스쳐 지나가는 듯했다.

‘정말…… 그 모든 게 꿈이 아니었어.’

살아남았다는 기쁨과 안도가 흩어지고, 죄책감과 씁쓸함이 빈자리를 채운다.

나는 그저 멍하니 창가를 바라보았다. 한 줄기의 나직한 목소리가 귓가를 파고들기 전까지.

“결국 누군가는 살아남고, 누군가는 죽는다.”

툭.

어깨에 닿은 손에서 온기가 느껴진다. 적천강이 먼 곳을 바라보며 말을 이었다.

“그것이야말로 거스를 수 없는 순리이며, 무림(武林)이니라.”

“…….”

“살아남았다는 것에 감사하고, 죽어 간 이들을 추모해라. 지금은 그것만으로 충분하다.”

걸음을 옮겨 창가로 다가간 적천강이 창문을 열어젖혔다. 왈칵 쏟아지는 햇빛을 받으며 서 있는 그의 모습을, 나는 말 없이 바라보았다.

뇌리를 스치는 많은 생각과 함께 입술이 열렸다.

“노야.”

내 부름에 적천강이 푸근한 미소를 지으며 고개를 저었다.

“됐다. 지금은 아무 말도 하지 말거라.”

“아, 그게 아니고요.”

“어허. 그만 되었대도. 네게 묻고 싶은 것도 많지만 지금은 우선 마음을 정리…….”

“아니, 그. 눈부셔서 그럽니다.”

“응?”

나는 조심스럽게 적천강의 머리를 가리켰다. 햇빛을 받아 번쩍거리는 그의 대머리는 태양권을 패시브 스킬로 쓰고 있었다.

“창문을 닫든지, 머리를 좀 치워 주세요.”

“……!”

“그나저나 강기 사용하셨어요? 머리 진짜 말끔하게 미셨네. 변장도 좋지만 그래도 숱은 좀 남겨 두시지. 나중에 안 자라면 어쩌시려고.”

그 순간, 적천강의 입가에 맺혀 있던 푸근한 미소가 사라졌다.

순식간에 마음씨 좋은 옆집 할아버지에서 혈승(血僧)으로 돌변한 적천강이 짜게 식은 눈빛으로 날 바라보았다.

“이런 개호로…….”

“아니, 그냥 부탁드린 건데 왜 욕을 하세요. 이제 막 깨어난 환자한테.”

“다시 잠들고 싶으냐? 앞으로 석 달 보름 동안 푹 재워 줘?”

우득.

야무지게 말아쥔 주먹에서 뼈 어긋나는 소리가 들린다. 무언가 잘못되었음을 직감한 내가 빠르게 입을 열었다.

“이미 충분히 잤는데요.”

“노부의 판단에 따르면 더 자고 싶어 하는 것 같은데.”

“진짜 괜찮습니다. 이쪽 일도 거의 끝났으니까 얼른 중원으로 가야…….”

“괜찮다. 이번에 자고 일어나면 최소 하남일 테니까.”

나는 침을 꿀꺽 삼켰다.

“그건 좀. 많이 별로 같은데요.”

“어째서? 어차피 가는 길이라고 해 봤자 따분하기만 할 것 아니냐.”

“하나도 안 따분해요. 저 자연 경관 감상하는 거 좋아합니다.”

“아예 자연으로 돌아가는 건?”

“……농담이시죠?”

“농담처럼 들리느냐?”

“아뇨.”

“방금 했던 말은 농담이다. 하남에서 깨어나는 건 진담이고.”

화륵.

나는 적천강의 주먹을 휘감으며 타오르는 불꽃을 발견하고 본능적으로 주위를 둘러보았지만, 당연하게도 소화기는 보이지 않았다.

좆 됐네. 시바.

체념한 나는 정중하게 부탁했다.

“살살 부탁드립니다.”

“고분고분하게 받아들인다면 어렵지 않은 부탁이지. 화염신장과 멸염신권, 둘 중 무엇으로 하겠느냐?”

“……그게 살살 맞는다고 안 아플까요?”

“그럼 세게?”

“……화염신장이나 멸염신권 말고 다른 선택지는 없습니까.”

“있지.”

“오, 뭔데요.”

“화신귀무.”

나는 진심으로 담아 물었다.

“진짜 노망나셨어요?”

빡!

눈앞이 번쩍한다.

이마를 타고 전해지는 격통에 입을 딱 벌리고 몸부림치던 그때, 퉁명스럽기 그지없는 적천강의 목소리가 귓가를 파고들었다.

“슬슬 일어날 때가 되었다 싶어 간만에 들렀더니 아주 멀쩡하구먼. 헛소리 지껄이지 말고 몸이나 추스러라. 노부는 이만 간다.”

탁.

눈을 뜸과 동시에 굳게 닫히는 문. 눈물을 찔끔 흘리며 이마를 문지른 나는 적천강의 빈자리를 보며 중얼거렸다.

“좀 더 있다 가시지…….”

그리고 그 희미한 목소리가 허공으로 흩어지기도 전에, 나는 전각을 휩쓰는 진동을 느낄 수 있었다.

쿵. 쿵. 드드득!

새삼 놀랍게도 그건 누군가의 발걸음이었고, 흡사 코끼리가 달려오는 듯한 그 진동 너머에서는 표홀하게 움직이는 여러 개의 인기척도 함께 가까워지고 있었다.

조금 전 적천강이 나갔던, 굳게 닫힌 문을 향해.

“야, 잠깐 멈……!”

하지만 내 다급한 외침은 끝까지 이어지지 못했다.

콰앙!

폭발하듯 터져 나가는 목제 문과 함께 뿌옇게 솟아오른 먼지구름.

순식간에 폐허가 되어 버린 처소에서 멍하니 굳어 있던 나는, 먼지구름 너머로 보이는 낯익은 얼굴들을 발견하고 풀썩 웃어 버렸다.

그래. 뭐, 이것도 나쁘지 않지.

“다들 잘 지냈어?”

그 말을 신호탄으로, 여러 개의 신형이 동시에 나를 덮쳤다.

아니, 천장에 닿을 정도로 높게 솟구친 거대한 인영이 나를 비롯한 모두를 덮쳤다.

후우우웅!

“태산이! 각주 보고 싶었다!”

“……아.”

너는 내 계산에 없었는데.



* * *



쾅!

등 뒤에서 울려 퍼진 굉음을 들은 적천강이 피식 실소를 흘렸다.

“거, 아주 난리도 아니구먼.”

태산인지 거산인지 하는 그 덩치 큰 놈의 소행이 분명하다.

먼저 처소를 빠져나갔던 의원이 이미 소식을 전했는지, 그 누구보다 빠르게 달려온 화룡각 대원들이 적천강을 보는 둥 마는 둥 하면서 전각으로 향한 것이 불과 촌각도 전의 일이었으니까.

‘젊은것들이 어울리겠다는데, 이 늙은이는 빠져 줘야지.’

그런 것 치고는 웬 늙은이 하나가 끼어 있긴 했지만, 이미 오래전 백수(白壽)를 넘긴 적천강의 입장에서는 이팔청춘이다.

아직 팔순 이하라면 만년한철도 씹어먹는다는 게 그의 지론이었다.

‘……그건 좀 아닌가.’

내심 작게 중얼거린 적천강은 천천히 걷기 시작했다.

언제 그랬냐는 듯이 맑아진 하늘도 올려다보고, 진태경의 소식을 듣고 삼삼오오 모여들기 시작하는 남만인들도 보았다.

그리고 선선한 바람을 맞으며 생각했다.

아니, 이 자리에 없는 한 사람에게 전해지지 못할 물음을 던졌다.

‘진정 그리 생각하느냐?’

칠 주야 만에 의식을 되찾은 진태경은 말했다. 이 모든 게 꿈이 아니라서 다행이라고. 정말 다행이라고.

하지만 그렇게 말하는 진태경의 목소리와 눈빛은, 적천강의 눈에 비친 그의 모습은 그렇지 않았다.

‘탓하는 게지. 살아남은 자신을, 그들을 구하지 못한 스스로를.’

죽은 이들이 어찌 되었는지는 그 누구도 모른다.

그러나 적천강은 지옥에서 살아남은 이들을 수없이 지켜보았고, 그들이 후회와 죄책감이라는 감정을 짊어진 채 살아간다는 것을 알고 있었다.

정마대전(正魔大戰).

피와 죽음으로 점철된 그 억겁과도 같은 시간 속에는, 적천강 역시 있었으니.

‘허나, 그것을 이겨 냈을 때 더욱 강해진다.’

그렇기에 최대한 말을 아꼈다. 의식을 잃은 와중에도 고통스럽게 신음하고, 몸부림치던 진태경의 모습도 애써 모른 척하며 물어야 했다.



‘푹 잤느냐?’

‘뭐, 그럭저럭요.’



필시 끔찍한 악몽이었으리라. 하지만 진태경은 입술에 침도 안 바르고 천연덕스럽게 거짓말을 늘어놓았다.

‘고얀 놈 같으니.’

화는 나지 않았다.

어떻게든 견뎌 내려는 그 모습이 대견했고, 한편으로는 씁쓸했다.

그저…… 그뿐이다.

그런데 왜 지금도 가슴 한구석이 저리는 걸까. 세상 곳곳을 보고 있음에도 녀석의 모습이 눈앞에 어른거리는 걸까.

‘염병할. 노부도 늙긴 늙었구먼.’

한데 어째서인지 이런 자신이 썩 싫지 않다.

두 눈으로 직접 목격한 그 불가사의한 회복도, 다른 무엇도 아닌 진태경만이 그의 마음을 채우고 있었다.

‘뭐, 이것도 나쁘지는 않디.’

희미하게 웃은 적천강은 인적 드문 곳으로 발걸음을 옮겼다. 나뭇잎 사이로 비친 햇빛이 그의 텅 빈 대머리를 비추고 있었다.



* * *



“조장님.”

“왜.”

“조장니임.”

“아, 왜.”

“조장니이이임!”

“그만 불러, 이 자식아. 나 아직 안 죽었어.”

내 윽박지름에도 불구하고 혁무진은 울먹거림을 멈추지 않았다.

그 대신 두 손으로 내 옷소매를 꽉 붙든 채 촉촉하게 젖은 눈으로 이렇게 물었다.

“그럼 언제 돌아가시는데요?”

“……미친 새낀가. 이 정도면 죽으라고 염불을 외는 수준 같은데.”

“꼬박 칠 주야 동안 정신을 잃으셨잖아요. 진짜 돌아가시는 줄 알았다고요.”

내 특명에 따라, 바닥에 엎드려 열심히 걸레질하고 있던 태산이 냉큼 고개를 끄덕였다.

“맞다. 태산이도 각주가 영영 못 일어나는 줄 알고 기대했다.”

살짝 감동하려던 나는, 뭔가 이상함을 눈치채고 눈을 깜빡였다.

“기대? 기대를 왜 해.”

나이를 핑계로 하나밖에 없는 의자를 차지한 남호가 중얼거렸다.

“뭘 물어봐, 상갓집 잔치 기대한 거지. 저 썅노무 새끼.”

“아, 아니다! 태산이 각주 생각만 하면 걱정이 돼서 침을 흘렸다!”

“…….”

“…….”

저 새끼 저거, 진짜 어지간히 기대했나 본데.

나와 눈이 마주친 태산 맘, 사마표가 힘없이 고개를 떨구었다.

“못 들은 것으로 해라. 입이 열 개라도 할 말이 없군.”

“입이 열 개? 태산이는 입이 열 개면……!”

“열 배를 더 처먹겠지. 제발 부탁인데 누가 저놈 주둥이에 재갈 좀 물리면 안 되나?”

남만당에 소속된 남호 의원이 태산 입마개 법안을 정식으로 발의한 그때, 어디선가 바람을 가르는 파공성이 울려 퍼졌다.

쉬익, 쾅!

개판이 난 처소에서 그나마 형체를 유지하고 있던 탁자가 단번에 으스러진다.

동시에 한 사람의 입술 사이로 차가운 목소리가 흘러나왔다.

“지금…… 환자 앞에서 무슨 짓들인가요?”

환자 앞에서 가구를 박살 낸 주화란의 한 마디에, 모두가 입을 굳게 다물었다.
```

## Final English reading copy

```markdown
# Chapter 715

A room filled with the smell of medicinal herbs.

A middle-aged man stood there, trembling as he held a long acupuncture needle in his hand, while Jeok Cheongang had him by the collar.

*This is going to be good. This is going to be good.*

Even though I had only just woken up, it was easy to understand what was happening. The middle-aged man I assumed was a physician spotted me blinking over Jeok Cheongang’s shoulder and shouted.

“Ah! Ahhh! He’s awake! He’s awake!”

“……”

Even my mother would have been less happy than that if she’d been here.

I guarantee it. That wasn’t the cheer of someone happy that a patient had woken up. It was the cheer of a victim who had spotted the police in front of a serial killer.

Jeok Cheongang let go of the physician’s collar without protest, then turned to look at me.

He said nothing for a long while, even after the physician hurriedly escaped.

Then he suddenly opened his mouth.

“You took your time waking up.”

His voice was gruff, so I shrugged.

I couldn’t exactly tell him that I’d had a fucking nightmare where Old Master had bitten my throat out.

“Did you sleep well?”

“More or less.”

“How do you feel?”

“Light. My head feels clear, too.”

That was the unvarnished truth. My body felt as light as a feather, and the long sleep had washed away the fatigue in my head, leaving me clearer than ever.

*They said I was unconscious for seven days and nights, didn’t they?*

I must have been more exhausted than I realized.

Not to brag, but it was rare for a master who had reached the Supreme Peak realm like me to remain unconscious for an entire week.

Then, without meaning to, I blurted out a single sentence.

“That’s a relief.”

“What is?”

“That this isn’t a dream.”

“……”

“It really is a relief.”

With eyes clouded by emotion, I looked around.

Sunlight streamed through the half-open window, while the chirping of birds tickled my ears. Far off, I could sense people passing by, chatting quietly among themselves.

*I’m alive.*

It was ironic.

Even while breathing through my mouth and nose, even while perceiving reality through my senses, I found it difficult to believe that I was alive.

At the same time, a hollow emptiness seized me.

For an instant, the darkness that had wrapped around the Inner Palace seemed to pass over the sunlight settling on the window. So did the sight of countless corpses collapsed with their faces buried in pools of blood.

*So… it really wasn’t a dream.*

The joy and relief of surviving scattered, replaced by guilt and bitterness.

I stared blankly at the window until a low voice pierced my ears.

“In the end, some survive, and some die.”

Tap.

I felt warmth from the hand resting on my shoulder. Jeok Cheongang continued while gazing into the distance.

“That is the irresistible order of things. That is the Murim.”

“……”

“Be grateful that you survived, and mourn those who died. For now, that is enough.”

Jeok Cheongang walked over to the window and threw it open. Bathed in the sunlight pouring inside, he stood there while I watched him in silence.

Along with the many thoughts flashing through my mind, my lips parted.

“Old Master.”

At my call, Jeok Cheongang gave me a warm smile and shook his head.

“Enough. Say nothing for now.”

“Ah, that’s not what I meant.”

“Enough, I said. There are many things I wish to ask you, but for now, you should first settle your mind—”

“No, it’s just that you’re dazzling me.”

“Hm?”

I cautiously pointed at Jeok Cheongang’s head. His bald head, gleaming in the sunlight, was using Solar Fist as a passive Skill.

“Either close the window or move your head a little.”

“……!”

“By the way, did you use Force? You shaved your head really cleanly. I understand the disguise, but you should’ve left some hair. What if it doesn’t grow back later?”

At that moment, the warm smile around Jeok Cheongang’s mouth vanished.

In an instant, Jeok Cheongang transformed from the kind old man next door into the Blood Monk. He stared at me with a look gone completely cold.

“You goddamn—”

“I was only asking you to do something. Why are you swearing at me? I just woke up.”

“Do you want to go back to sleep? Shall I let you sleep for the next three and a half months?”

Crack.

The bones in his tightly clenched fist shifted with an ominous sound. Realizing that something had gone terribly wrong, I hurriedly opened my mouth.

“I’ve already slept enough.”

“According to this old man’s judgment, you seem to want more.”

“I’m really fine. The work here is almost finished, so we should hurry back to the Central Plains—”

“It’s fine. Once you sleep and wake up this time, you’ll be in Henan at the very least.”

I swallowed hard.

“That sounds… really bad.”

“Why? The journey there will be boring anyway, won’t it?”

“It won’t be boring at all. I like admiring natural scenery.”

“What about returning to nature entirely?”

“……You’re joking, right?”

“Does it sound like a joke?”

“No.”

“What I just said was a joke. Waking up in Henan was not.”

Whoosh.

I saw flames winding around Jeok Cheongang’s fist and instinctively looked around, but naturally, there was no fire extinguisher in sight.

*I’m fucked. Shit.*

Having resigned myself to my fate, I made a polite request.

“Please go easy on me.”

“If you accept it obediently, that won’t be difficult. Which will you take—Flame Divine Palm or Flame-Extinguishing Divine Fist?”

“……Would either of those not hurt if you used them gently?”

“Then shall I hit you hard?”

“……Is there really no option besides Flame Divine Palm and Flame-Extinguishing Divine Fist?”

“There is.”

“Oh? What is it?”

“Dance of the Fire God and Demon.”

I asked in complete sincerity.

“Have you really gone senile?”

Whack!

My vision flashed white.

As I writhed with my mouth hanging open from the blinding pain racing across my forehead, Jeok Cheongang’s thoroughly gruff voice pierced my ears.

“I thought it was about time you woke up, so I stopped by for the first time in a while. And you’re perfectly fine. Stop spouting nonsense and take care of yourself. This old man is leaving.”

Click.

The door slammed shut just as I opened my eyes. Shedding a few tears as I rubbed my forehead, I looked at the empty space Jeok Cheongang had left behind and muttered.

“You could’ve stayed a little longer…”

Before that faint voice could even disperse into the air, I felt a tremor sweeping through the pavilion.

Boom. Boom. Rumble!

Surprisingly, it was someone’s footsteps. Beyond the tremor, which sounded like an elephant charging toward me, several other presences were also drawing closer, moving with uncanny lightness.

They were headed toward the firmly closed door Jeok Cheongang had just passed through.

“Hey, wait—!”

But my desperate shout never reached the end.

Crash!

The wooden door exploded outward, sending a cloud of dust billowing into the air.

As I stood there blankly frozen in the quarters that had become a ruin in an instant, I saw several familiar faces through the dust cloud and let out a helpless laugh.

*Yeah. Well, this isn’t so bad either.*

“How has everyone been?”

That sentence served as the signal. Several figures leaped toward me at once.

No—one enormous figure shot up high enough to reach the ceiling and crashed down on all of us, myself included.

Whoooosh!

“Taishan wanted to see the Pavilion Master!”

“……Ah.”

*You weren’t part of my calculations.*

* * *

Bang!

Hearing the tremendous crash behind him, Jeok Cheongang let out a quiet laugh.

“Well, what a commotion.”

It was obviously the work of that big fellow called Taishan—or was it Geosan?

The physician who had left the quarters first must already have spread the news. The members of the Fire Dragon Pavilion had rushed over faster than anyone else, barely sparing Jeok Cheongang a glance as they headed toward the pavilion. That had happened only moments ago.

*The youngsters want to spend time together, so this old man should step aside.*

There was one old man among them, but from Jeok Cheongang’s perspective, someone who had not yet reached eighty was still in the prime of youth. After all, Jeok Cheongang himself had passed ninety-nine long ago.

It was his firm belief that anyone eighty or younger could chew Ten-Thousand-Year Cold Iron.

*…That may be taking it a little far.*

After muttering inwardly, Jeok Cheongang began to walk slowly.

He looked up at the sky, which had cleared as though nothing had happened, and watched the Nanman people begin gathering in groups of three or five after hearing the news of Jin Taekyung.

Then, as he felt the cool breeze against his skin, he thought.

No. He silently posed a question to someone who was not there to hear it.

*Do you really think so?*

Jin Taekyung had regained consciousness after seven days and nights. He had said he was relieved that none of this was a dream. That it really was a relief.

But the voice and eyes of the person saying those words—and the Jin Taekyung Jeok Cheongang saw—did not seem that way at all.

*He was blaming himself. The self who survived. The self who failed to save them.*

No one knew what had become of the dead.

But Jeok Cheongang had watched countless people survive hell, and he knew that they continued living while carrying the weight of regret and guilt.

The Great Faction War.

Jeok Cheongang had also been there during that eternity of blood and death.

*But once you overcome it, you grow stronger.*

That was why he had chosen his words as sparingly as possible. Even while pretending not to notice Jin Taekyung groaning and thrashing in pain while unconscious, he had forced himself to ask.

*Did you sleep well?*

*More or less.*

It had surely been a terrible nightmare. But Jin Taekyung had lied through his teeth with a perfectly straight face.

*What a cheeky brat.*

Jeok Cheongang was not angry.

He was proud of the way Jin Taekyung was trying to endure it somehow, but at the same time, he felt bitter.

That was all. Nothing more.

So why did something in his chest still ache? Why did Jin Taekyung’s figure keep wavering before his eyes even as he looked at the world around him?

*Damn it. This old man really is getting old.*

And yet, for some reason, he did not dislike himself like this.

He had witnessed that mysterious recovery with his own eyes, but it was Jin Taekyung—not anything else—who filled his heart.

*Well, this isn’t bad either.*

Jeok Cheongang gave a faint laugh and walked toward a quiet place. Sunlight filtering through the leaves shone on his bare, gleaming head.

* * *

“Captain.”

“What?”

“Captain.”

“Ah, what?”

“Captaiiin!”

“Stop calling me, you bastard. I’m not dead yet.”

Despite my shouting, Hyuk Mujin continued to sound as though he was about to cry.

Instead, he clutched my sleeve tightly with both hands and asked with his wet, glistening eyes,

“Then when are you going to pass away?”

“……Are you insane? At this point, you’re practically chanting for me to die.”

“You were unconscious for seven whole days and nights. I really thought you were going to pass away.”

Taishan, who was diligently scrubbing the floor under my direct orders, promptly nodded.

“That’s right. Taishan thought the Pavilion Master would never wake up and was looking forward to it.”

I was just beginning to feel touched when I noticed that something was wrong and blinked.

“Looking forward to it? Why would you look forward to that?”

Namho, who had claimed the only chair under the pretext of his age, muttered,

“Why ask? That son of a bitch was looking forward to the funeral feast.”

“No! Taishan worried whenever he thought about the Pavilion Master, so he drooled!”

“……”

“……”

That bastard really must have been looking forward to it.

Sama Pyo, who was practically Taishan’s mother, met my eyes and lowered his head weakly.

“Pretend you didn’t hear that. I have nothing to say for myself, even if I had ten mouths.”

“Ten mouths? If Taishan had ten mouths, then—!”

“He’d eat ten times more. Please, can someone put a muzzle on that bastard?”

At that moment, Assemblyman Namho of the Nanman Party formally introduced the Taishan Muzzle Bill, and the sound of something cutting through the air came from somewhere.

Whoosh—crash!

The table that had somehow managed to keep its shape in the ruined quarters was crushed in a single blow.

At the same time, a cold voice slipped between someone’s lips.

“What… are you all doing in front of a patient?”

Everyone clamped their mouths shut at Ju Hwaran’s remark, delivered after she had smashed the furniture in front of the patient.
```

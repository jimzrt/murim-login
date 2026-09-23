<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0840.txt",
      "sha256": "9f31a4e174f04f783ad4eac3687bd23bf28254e6e6b1d52406d7d3d95369f9a9",
      "bytes": 13342
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "61970fabcc867599c38a9eeae672943d2b59c3e98be7f592f019f8c0064a9e61",
      "bytes": 2332
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "2ac235886e36b4a9cfac67990c4e303d5cbbbaacdc20104970ce04b7ba9ca08c",
      "bytes": 227427
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "dbc77fe8ce5a2184208fd9642e3fd5ae4aebe48b57c083777e8a3a795c3ad115",
      "bytes": 723
    },
    {
      "path": "characters/Human Butcher.md",
      "sha256": "e5cd20ee979af797ddef41325790e8c6cd62d706af4220a7c953a946b5b62857",
      "bytes": 667
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "ba22ce3f415853274ae0252df11acbcc95dba299aa4fe9aa46e61dbcf1085559",
      "bytes": 1355
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "c53dd419ab4a78cec6f282a0c32385c7ce41bf8ab3c53bda96fc6ef4f432d93f",
      "bytes": 1848
    },
    {
      "path": "characters/Ju Hwaran.md",
      "sha256": "38132d6aba8990bc992d133108d251596c630b363e0ffc80fb2d995a08656fad",
      "bytes": 937
    },
    {
      "path": "characters/Namho.md",
      "sha256": "4917215fc9d5b65fdb4cdf81f01cfd45abd4723717a0d2d98ad922cf91850fc7",
      "bytes": 936
    },
    {
      "path": "characters/Sama Pyo.md",
      "sha256": "7bd29612b9b1b770352031e709d2949170b5609b049b3c9d85de3db38aa4fc99",
      "bytes": 936
    },
    {
      "path": "characters/Song Il.md",
      "sha256": "39da6333bf28e2ec516b59a9b52e671919806d1458613dc36618f988ffafa426",
      "bytes": 964
    },
    {
      "path": "characters/Song Ilseom.md",
      "sha256": "e73bb7cd97195a2224e49f9e356df183ccc7db3448b3c8ccef692f85b6bae55c",
      "bytes": 1074
    },
    {
      "path": "characters/Southern Heaven Demon Empress.md",
      "sha256": "be7edc1c6f334537b18b262813347749cbca96d6fdebda2777b5cecbf27925b9",
      "bytes": 715
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "2c376254581e57b0093d3a0fa4d0f6edc9d42228f48040a2d9753e1c4024a6b7",
      "bytes": 787
    },
    {
      "path": "characters/Tang Sadok.md",
      "sha256": "4a693755d6b03f2ab8ddc7ac5e42478c9d0222151ed5f412d815f9d2d6fa48e4",
      "bytes": 806
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "2d3ba6654cdbcc372510ec72e3979b0d7dd3413b49d0a44c281c59171f618c6d",
      "bytes": 251874
    }
  ],
  "estimated_tokens": 13802
}
-->

# Durable State Update — Chapter 840

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
1 and safe_through 840. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 840. Profile updates may replace only one
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
  "chapter": 840,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 840,
    "continuity_sources": [840],
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
    "The supernatural Rift began at 10%; its progress increases the distribution and concentration of magical power.",
    "The System’s Status Window is inaccessible; Jin suspects an update may be responsible.",
    "Jin saw a vision of a black-haired man killing Ahomed after the ritual. Whether it was real is unknown; Jin believes the man was not Asmodeus.",
    "Jin’s [Broken Body] injury around his lower dantian remains unresolved; leveling up did not heal it.",
    "Jeok Cheongang went to Sichuan to bring the Divine Physician, his former Disciple, to treat Jin.",
    "Ju Wongong remains temporarily appointed acting City Lord of Sichuan Province by imperial order while under exile.",
    "The Sichuan Tang Clan and Sichuan Murim are rebuilding and reuniting after Dark Heaven’s attack.",
    "Tang Sadok welcomed Jin as the Tang Clan’s benefactor and is taking him to the Old Master."
  ],
  "continuity_sources": [
    838,
    839
  ],
  "open_questions": [
    "Why did the Main Quest fail despite the Doppelganger’s erasure, and who or what was summoned?",
    "Was Jin’s vision of the summoned being real, System-delivered, or prophetic?",
    "What will happen as the Rift progresses and more beings enter the world?",
    "Who or what chose Jin, and what is the Ark?",
    "What changed in the System update, and when will its functions return?"
  ],
  "safe_through": 839,
  "temporary_decisions": [
    "Keep magical power distinct from mana; keep Blink distinct from Teleport and Warp. Extended-range Blink causes severe strain.",
    "Keep Fire Storm and Aqua Storm as distinct named spells.",
    "Render [영웅의 검] as “Hero’s Sword,” 에어 슬래시 as “Air Slash,” and 실드 마법 as “Shield magic.”",
    "Render 선택받은 자 as “the Chosen One,” 방주의 주인 as “the Master of the Ark,” [격변] as [Cataclysm], [어데 도씹니꺼] as “Where’s Your Do Clan From?,” and [종족 학살자] as “Species Slayer.”",
    "In chapter 839, render 균열 as a social fracture or division, not the supernatural Rift."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 송일     | **Song Il**        |
| 주화란    | **Ju Hwaran**      |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 살성     | **Slaughter Saint**           | —              |
| 암천     | **Dark Heaven**                  |
| 사천당가   | **Sichuan Tang Clan**            |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 주화입마   | **qi deviation**                                 |                                                       |
| 중원     | **Central Plains**                               |                                                       |
| 가주     | **Family Head**                              |
| 제자     | **Disciple**                                 |
| 은인     | **Benefactor**                               |
| 상태               | **Status**                     |
| 매력               | **Charm**                      |
| 사천     | **Sichuan**            |
| 노부      | **this old man / I**                                            |
| 본가      | **our family / this family**                                    |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 남호 | **Namho** | Hidden Shadow Pavilion code name; literally associated with amber from the south. |
| 사마표 | **Sama Pyo** | Young Sect Leader of the Black Dragon Demon Gate. |
| 송일섬 | **Song Ilseom** | Young escort captain of the Yongbong Escort Bureau; distinct from Song Il of Zhongnan. |
| 남천마후 | **Southern Heaven Demon Empress** | Title Honglan uses when revealing her identity. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 당사독 | **Tang Sadok** | Current Family Head of the Sichuan Tang Clan; also called the Myriad-Poison Asura. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 여름이 | **Yeoreum** | Name Hayeon gives to the Level 2 kitten. |
| 사마외도 | **demonic, heterodox arts** | Suspected martial-arts origin of Pung Yang's insidious forms. |
| 개방 | **Beggars' Sect** | Murim organization counted among the Nine Sects and One Gang. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 점혈 | **Pressure-Point Strike** | System-named technique used by Jeok Cheongang on Taekyung. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 아미 | **Emei** | Short form for Emei Sect. |
| 청성 | **Qingcheng** | Short form for Qingcheng Sect. |
| 화란 | **Hwaran** | Familiar short form of Ju Hwaran. |
| 표왕 | **Escort King** | Epithet of Ju Gongsan. |
| 당가 | **Tang Family** | Short form for the Sichuan Tang Clan when distinguished from 사천당문. |
| 만독수라 | **Myriad-Poison Asura** | Epithet of Tang Sadok. |
| 일원 | **One Origin** | Named Tang Clan organizational unit in Tang Sadok's mobilization order. |
| 독의 | **Poison Physician** | Taekyung's mocking description of Mungyeong after learning how aggressively he uses poison. |
| 소하 | **Xiao He** | Historical civil official invoked in the same exchange. |
| 화룡각 | **Fire Dragon Pavilion** | New name chosen for Taekyung's pavilion. |
| 고든 | **Gordon** | Pentagon employee tasked with repairing smashed warning lights. |
| 남천 | **South Heaven** | Dark Heaven power that the Lord of Heaven orders the servants to contact. |
| 마후 | **Demon Empress** | Title used for the Southern Heaven Demon Empress. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혁무진 | 적천강 | subordinate_to_overwhelming_elder | Great Hero Jeok | deferential and fearful | Mujin uses 적 대협 while reporting Jeok’s orders and Taekyung’s awakening. |
| 적천강 | 혁무진 | overwhelming_elder_to_junior_martial_artist | you stupid fool | blunt and mocking | Jeok calls Mujin a 멍청한 놈 after knocking him down during the attempted escape. |
| 송일 | 적천강 | former rescued junior to former rescuer | Great Hero Jeok | formal, fearful, and defensive | Uses 적 대협 while insisting that Jeok has no business interfering in the dispute. |
| 적천강 | 송일 | former rescuer to former rescued junior | Zhongnan brat; you; insolent bastard | blunt, mocking, and humiliating | Jeok recalls Song's youthful arrogance and addresses him with contempt while publicly disciplining him. |
| 송일섬 | 주화란 | escort_captain_to_young_bureau_head | Hwaran | urgent and familiar | Calls out 화란아 while urgently warning Ju Hwaran before stepping into the confrontation. |
| 주화란 | 혁무진 | rescued_survivor_to_benefactor | Benefactor | formal-deferential | Hwaran includes Mujin among the Benefactors when greeting Taekyung's companions. |
| 주화란 | 송일섬 | bureau_head_to_escort_captain | Captain Song | formal and prosecutorial | Uses his office title, then his personal name, while exposing and confronting him. |
| 호위 | 당사독 | guard_to_Family_Head | Family Head | formal-deferential | Uses 가주님 while reporting Jin Taekyung's request. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 적천강 | 남천마후 | legendary_martial_master_to_hostile_demon_empress | you bitch | blunt and threatening | Threatens to punish her and Lord of Heaven. |
| 남천마후 | 적천강 | hostile_demon_empress_to_legendary_martial_master | Fire King Jeok / you | flattering and mocking | Addresses Jeok Cheongang as the Fire King while praising Lord of Heaven. |
| 주화란 | 사마표 | former_fiancés | Young Sect Leader | formal and guarded | Hwaran formally greets her former fiancé. |
| 사마표 | 태산 | Young Sect Leader to subordinate | Taishan | informal and patronizing | Sama Pyo calls Taishan by name while ordering him to leave. |
| 태산 | 사마표 | subordinate to Young Sect Leader | Lord | crude and deferential | Taishan uses 주군 while obeying Sama Pyo. |
| 사마표 | 적천강 | Young Sect Leader to legendary elder | Great Hero Jeok | formal-deferential | Sama Pyo formally pays his respects to Jeok Cheongang as the Fire King. |
| 태산 | 적천강 | subordinate of a Young Sect Leader to legendary elder | Fire King | clipped, childlike, and deferential | Taishan gives his awkward greeting and expresses admiration for Jeok's strength. |
| 적천강 | 사마표 | legendary elder to unorthodox Young Sect Leader | you / young brat | blunt, suspicious, and contemptuous | Jeok addresses Sama Pyo with 네놈 and 어린놈 while probing his lineage and motives. |
| 적천강 | 태산 | legendary elder to giant subordinate | you / strange fellow | blunt, startled, and grudgingly tolerant | Jeok addresses Taishan as 네놈 while reacting to his greeting and appetite. |
| 혁무진 | 송일섬 | pavilion_member_to_escort_captain | Great Hero Song | formal and deferential | Mujin addresses Song Ilseom while commenting on his broad experience. |
| 송일섬 | 사마표 | fellow_pavilion_member_to_hostile_fellow_member | you | hostile and casual | Song Ilseom discusses fighting Sama Pyo and answers him while preparing to move away. |
| 사마표 | 송일섬 | fellow_pavilion_member_to_hostile_fellow_member | you | controlled and antagonistic | Sama Pyo responds to Song Ilseom's accusations and proposes moving aside to fight. |
| 혁무진 | 태산 | pavilion_member_to_pavilion_member | you / hey | casual and coaxing | Hyuk Mujin calls after Taishan and offers jerky to persuade him to travel together. |
| 태산 | 혁무진 | pavilion_member_to_pavilion_member | you | clipped and dismissive | Taishan tells Hyuk Mujin not to follow, then accepts him as a friend after hearing about the jerky. |
| 남호 | 혁무진 | hidden_shadow_agent_to_pavilion_member | you there / Han bastard | performatively hostile and abusive | Namho attacks Mujin and insults him to make the meeting appear to be a genuine expulsion. |
| 혁무진 | 남호 | pavilion_member_to_hidden_shadow_agent | old man | indignant and insulting | Mujin protests Namho’s staged attack and objects to the insult about his parents. |
| 주화란 | 남호 | pavilion_member_to_hidden_shadow_agent | you / Elder Namho | formal and appreciative | Hwaran respectfully praises the effort Namho invested in mapping Nanman. |
| 남호 | 태산 | guide_to_pavilion_member | Taishan | blunt and exasperated | Namho directly rebukes Taishan for eating the poisonous blood-feeding fungus. |
| 남호 | 사마표 | guide_to_young_sect_leader | Young Sect Leader | blunt and admonishing | Namho warns Sama Pyo that all grass and animals in the territory belong to the Nanman Beast Palace. |
| 남호 | 주화란 | guide_to_escort_bureau_head | Escort King's granddaughter | approving and familiar | Namho praises Hwaran for recalling Ju Gongsan's records about Nanman. |
| 사마표 | 남호 | young_sect_leader_to_guide | Elder Namho | formal and apologetic | Sama Pyo apologizes after Taishan attempts to seize the calf. |
| 태산 | 주화란 | Pavilion member to Pavilion member | Young Lady Ju | clipped, childlike, and deferential | Agrees with Ju Hwaran after she mentions the evening banquet. |
| 태산 | 남호 | Fire Dragon Pavilion member to guide | Namho | clipped, childlike, and informal | Taishan directly addresses Namho while asking what Dark Heaven is. |
| 남호 | 각주 | guide to pavilion master | Pavilion Master | blunt, hostile, and abusive | Namho addresses Jin as 각주 while accusing him of causing the disturbance. |
| 사마표 | 각주 | Fire Dragon Pavilion member to pavilion master | Pavilion Master | formal but sardonic | Sama Pyo addresses Jin as 각주 while questioning his account of the incident. |
| 태산 | 각주 | Fire Dragon Pavilion member to pavilion master | Pavilion Master | clipped, childlike, and informal | Taishan directly asks Jin whether his Lord Sama Pyo is safe. |
| 적천강 | 의원 | interrogator_to_physician | you; quack | blunt and threatening | Jeok shakes the physician and demands an explanation for Jin's seven-day sleep before ordering him to summon the Beast Miao King. |
| 주화란 | 태산 | pavilion_member_to_pavilion_member | Young Hero Taishan | formal but stern | Ju Hwaran reprimands Taishan for speaking ominously about Jin and warns that she will muzzle him. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 837
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Human Butcher.md

# Human Butcher (인도)

- **Safe through:** Chapter 837
- **Aliases:** None
- **Role:** Former mysterious Han Chinese mounted-bandit power in Northern Gaoyuan commanding fifty subordinates; a Peak master killed by an unnamed old man in a single move
- **Personality:** Cold, intimidating, and murderous; he kills people as though slaughtering livestock
- **Voice:** Cold, curt, and quietly threatening
- **Relationships:** He is one of four powerful participants at the Northern Gaoyuan gathering, intimidates Temur, and has claimed Ghost Sword Wipeng as his personal target in the proposed attack

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 838
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and an active member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son; he uses quiet practices such as fishing to empty his mind. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad; as a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Fire Dragon Pavilion members accompanying Taekyung. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 835
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm, the occupant of the chief seat of the Murim Alliance's Five Kings Hall, and a trusted confidant who accepts Jin as himself despite knowing that he travels between Murim and another world resembling the realm of immortals.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Ju Hwaran.md

# Ju Hwaran (주화란)

- **Safe through:** Chapter 839
- **Aliases:** Hwaran
- **Role:** Ju Hwaran is a Level 88 Young Bureau Head, leader of the Yongbong Escort Bureau, an experienced Nanman guide, and an active member of the Fire Dragon Pavilion.
- **Personality:** Intelligent, capable, responsible, filial, composed under pressure, and burdened by intense guilt over the escort journey's deaths.
- **Voice:** Clear, polite, restrained, and determined.
- **Relationships:** Escort King Ju Gongsan was her paternal grandfather, Ju Hogun is her father, Heo Jun was her uncle, Sama Pyo was her former fiancé in a political engagement she accepted for her father's sake, Song Ilseom is her direct escort who accompanied her previous journey to Yeongin, and Jin Taekyung is a trusted ally; the Yongbong Escort Bureau has longstanding ties with Yeongin’s inhabitants.

### Namho.md

# Namho (남호)

- **Safe through:** Chapter 839
- **Aliases:** Elder Chao
- **Role:** Namho is an eighty-year-old non-Han Hidden Shadow Pavilion agent who spent more than fifty years operating under the cover of the Poison Flower Pavilion in Nanman and now serves as the Fire Dragon Pavilion’s guide.
- **Personality:** Duty-bound, pragmatic, and observant; uses theatrical violence to protect intelligence work and takes a veteran’s concern for the younger generation’s resolve.
- **Voice:** Measured and reflective when advising the younger generation, loudly abusive when maintaining his local cover, and capable of theatrical boasts and dry humor.
- **Relationships:** Namho is a Hidden Shadow Pavilion contact for Jin Taekyung and the Fire Dragon Pavilion, receives intelligence from the Pavilion Master, and knows the code used by the Thousand-Faced Fox.

### Sama Pyo.md

# Sama Pyo (사마표)

- **Safe through:** Chapter 837
- **Aliases:** Black Dragon Saber
- **Role:** Young Sect Leader of the Black Dragon Demon Gate, a Morning Star reputed to be no less than the Ten Dragons and Phoenixes, and a member of the Fire Dragon Pavilion.
- **Personality:** Outwardly courteous and smiling, inwardly calculating, but genuinely protective of Taishan; in combat he is ruthlessly pragmatic, survival-focused, and unafraid to stake his life.
- **Voice:** Polite and ingratiating in public, with sardonic humor and controlled evasiveness.
- **Relationships:** Sama Pyo commands the absolutely loyal Taishan, is Sima Gong's son, was Ju Hwaran's former fiancé in a political engagement, and has joined the Fire Dragon Pavilion while openly intending to use Jin Taekyung as a useful card; he is now openly hostile toward fellow member Song Ilseom.

### Song Il.md

# Song Il (송일)

- **Safe through:** Chapter 837
- **Aliases:** Roaring Fury Swordsman
- **Role:** Elder of the Zhongnan Sect and the Roaring Fury Swordsman; senior brother of Sect Leader Gong Iljung; came to the Jin Family of Taiyuan to demand redress for Gong Ilhyuk's injury and the alleged insult to Zhongnan; attacked Jin Taekyung with the Heavenly River Thirty-Six Swords, was stopped by Jeok Cheongang, and was publicly humiliated by him.
- **Personality:** Arrogant, domineering, punitive, and confident in his martial power and seniority.
- **Voice:** Gruff, cutting, condescending, and threatening, with formal authority used to pressure those beneath him.
- **Relationships:** Gong Iljung is his junior Sect Leader and martial younger brother; Gong Ilhyuk is a junior Disciple of his sect; he recognizes Baek Museong and Cheongpung through their Huashan and Sword Saint connections.

### Song Ilseom.md

# Song Ilseom (송일섬)

- **Safe through:** Chapter 837
- **Aliases:** Escort Captain Song
- **Role:** Level 110 young escort captain of the Yongbong Escort Bureau, one of its Dragon-Phoenix Three Escorts, and a newly accepted member of Jin Taekyung and Cheongpung’s Fire Dragon Pavilion; he is currently bound and unconscious under the reconnaissance squad's guard after being struck at a Sleep Acupoint.
- **Personality:** Blunt, decisive, survival-hardened, and dryly self-aware, with little patience for insults or disorder and practical survival skills such as making disguise masks.
- **Voice:** Forceful and urgent in command, with a rough and confrontational edge.
- **Relationships:** He serves under Ju Hwaran and has expressed concern that she not be hurt or die needlessly; he is Song Pyosan’s son, his grandmother was the surviving Guangdong Chen child rescued by Ju Gongsan during the Great Faction War, and he remains openly hostile toward fellow Fire Dragon Pavilion member Sama Pyo.

### Southern Heaven Demon Empress.md

# Southern Heaven Demon Empress (남천마후)

- **Safe through:** Chapter 781
- **Aliases:** None
- **Role:** The Southern Heaven Demon Empress was Honglan, the creator of the rift behind the Inner Palace, and was killed after the rift closed.
- **Personality:** Playful, cruel, confident, and casually dismissive of mass death and the suffering of others.
- **Voice:** Light, taunting, amused, and delighted even when discussing murder or imminent catastrophe.
- **Relationships:** She commands and advises Baeksang, treats Jin Taekyung and Yayul Cheok as expendable to the grand plan, and keeps a masked hunting dog whom she trained carefully.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 839
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion; he helped Jin escape the underground prison by blocking the stairs and overpowering the Bai warriors.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo; becomes explosively violent when his meat is threatened.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord, trusts Jin Taekyung as Pavilion Master, and has grown attached to the Fire Dragon Pavilion members.

### Tang Sadok.md

# Tang Sadok (당사독)

- **Safe through:** Chapter 839
- **Aliases:** Myriad-Poison Asura
- **Role:** Current Family Head of the Sichuan Tang Clan, gravely wounded in the Three-Gate Bloodbath and recovering under medical care.
- **Personality:** Grim, cold, blunt, suspicious, and unsentimental, with fierce concern for the Tang Clan’s affairs.
- **Voice:** Hissing, curt, authoritative, and threatening.
- **Relationships:** Tang Taesang was his father and predecessor, his unnamed nephew serves as Master of the Gatekeeper Pavilion, Mimi is his cherished old friend and companion temporarily entrusted to Cheongpung, and he regards Jin Taekyung and Cheongpung as benefactors, openly welcoming Jin with a warmth he usually conceals.

## Korean source

```text
＃840화



혈족 중심으로 이루어진 사천당가에서 가주의 권위는 그야말로 절대적이었다. 아니, 설령 당사독이 가주가 아니었더라도 그 사실은 크게 달라지지 않았을 것이다.

만독수라(萬毒修羅)라는 별호는 경외와 두려움의 대상이었으니까.

“본가의 은인이 먼 길을 오느라 지친 모양이군.”

당사독의 그 한 마디에, 내 주위를 둘러싸고 있던 수많은 인파가 자연스럽게 흩어졌다.

사천당가의 무인들은 물론이고 아미와 청성, 개방에 소속된 외부인들도 당사독과 나를 향해 포권을 취한 뒤 본래의 위치로 향했다.

자신들의 문파에도 꼭 들리라는 신신당부도 잊지 않고.

“그래, 자네들이 말로만 듣던 바로 그 화룡각의 동량(棟梁)들이로군.”

내가 잠시 다른 이들과 인사를 주고받는 사이, 화룡각의 일원들을 찬찬히 훑어보던 당사독이 문득 멈칫했다.

“내가 아는 바에 의하면 화룡각에 속한 이들은 하나같이 모두 젊은이라 들었는데, 혹시 극독에라도 당했나?”

지목당한 늙은 청년, 남호가 똥 씹은 얼굴로 대꾸했다.

“그런 일 없소.”

“독이 아니면, 주화입마?”

“지금 나랑 해보자는 거요?”

“아, 공력이 안 느껴져서 물어본 걸세. 그렇다면 혹시 나이가…….”

“일흔다섯. 이놈들과는 사정이 있어서 잠시 동행하고 있소.”

“이런. 결례를 저질렀구려.”

“이해하오. 같이 늙어 가는 처지에 그럴 수도 있지 뭘.”

당사독은 무공을 익히지 않았음에도 당당한 태도를 보이는 남호를 흥미롭게 바라보았고, 표왕의 핏줄인 주화란과 젊은 나이에 뛰어난 경지에 다다른 송일섬에게 호의를 내비쳤으며, 엄밀히 따지면 사마외도(邪魔外道)에 속한 사마표와 태산에게는 말없이 고개만 끄덕여 보였다.

그리고…….

“저 친구는 왜 저러나?”

“어, 그게. 오는 길에 일이 좀 있었습니다.”

“아주 엄청난 일이었던 모양이군. 얼굴이 저 정도로 부풀어 오를 수 있다니. 혹시 암천의 짓인가?”

“아뇨. 사실 제가 몇 대 때렸는데요.”

잠시 내려앉은 침묵.

태산의 어깨에 짐짝처럼 얹혀 있는 혁무진과 나를 번갈아 바라보던 당사독이 한숨을 내쉬었다.

“자네 수하들에게는 사람을 붙여 줄 테니, 우선 짐을 풀고 외원에 있는 약당을 찾아가 보게. 잘 치료해 줄 거야.”

당사독의 손짓에 근처에서 대기하고 있던 호위가 다가온 그때, 태산이 무뚝뚝한 목소리로 입을 열었다.

“태산이. 그리고 우리. 움직이지 않는다. 아니, 않습니다. 각주의 명령이 있기 전까지는.”

“아, 물론 식사도 준비되어 있을 걸세.”

“잘 다녀오겠다. 각주. 나중에 보자.”

“…….”

아무래도 미친 새끼가 확실하다.

아니, 이럴 거면 처음부터 말이라도 하지 말든가.

나는 태산의 머리통을 후려치려 하는 주화란을 눈짓으로 만류한 뒤, 당사독을 따라 내원(內院)으로 걸음을 옮겼다.

“자네는 어딜 가나 사람들의 신뢰를 얻는군. 이곳 사천에서도, 그리고 함께한 지 얼마 되지 않은 수하들에게서도.”

피식 웃는 것으로 대답을 대신한 나는, 지금 이 순간에도 서서히 멀어져 가는 사람들을 바라보며 입을 열었다.

“그건 당 대협도 마찬가지신 것 같은데요. 저분들이 아직까지 사천당가에 남아 있을 줄은 몰랐거든요.”

“참으로 고마운 일이지. 염치가 없어 몇 번이나 돌아가도 좋다고 했지만…… 그럼에도 끝까지 본가에 남아 있네. 아직 회복되지 않은 병자들을 치료하고, 가문의 재건도 계속해서 돕고 있어.”

“제가 본 게 전부는 아니겠지만, 외원(外院)은 이미 충분히 예전의 모습을 되찾은 것 같습니다만.”

“재건은 단순한 핑계일 뿐. 혹시 모를 암천의 재침공을 우려하여 본가에 주둔 중인 것일세. 노부도 그 사정을 알기에 더는 돌아가라 말하지 못하겠더군.”

“예?”

“인정할 건 해야지. 만약 저들이 없는 상황에서 지난번과 같은 일이 또다시 발생한다면…… 나는 가주로서 둘 중 하나를 선택해야 하네. 본가가 대대로 일궈 온 터전을 버리고 도망치든지, 아니면 마지막 의기를 보이고 멸문(滅門)당하든지.”

예상 밖의 대답에 나도 모르게 눈이 크게 뜨였다.

중원에서 손꼽히는 명문대파(名門大波). 그중에서도 자존심 강하기로 모르는 이가 없는 사천당가의 가주가 이런 말을 할 줄은 예상치 못했기 때문이었다.

특히 당사독이 어떤 사람인지 익히 알고 있던 나로서는 그 놀라움이 더할 수밖에 없었다.

“왜, 너무 솔직한 대답이라 놀랐나?”

“음. 아무래도 그렇죠.”

“충분히 이해하네. 더군다나 자네는 그 일이 있기 전에 이미 나를 알고 있었으니까.”

“그럼요. 그때만 해도 진짜…… 한 성격 하셨었는데.”

“허허, 그랬지.”

이제는 너털웃음까지 터트리는 당사독의 모습에, 나는 입을 딱 벌렸다.

“이 정도면 어디 아프신 거 아니에요?”

“아무 문제 없네. 그저 변하기로 마음먹었을 뿐이야.”

“그래도 모르니까 조심하세요. 사람이 너무 갑작스럽게 변하면 죽을 때가 된 거라던데.”

“허허허. 자넨 여전히 과할 정도로 솔직하군. 물론 그게 가장 큰 매력이긴 하지만.”

“그, 죄송한데 저도 취향이란 게 있습니다.”

“그래, 그런 식의 농담도 나쁘지 않고.”

“진담인데요.”

“……방금 했던 말은 취소하지. 자넨 가끔 사람을 열 받게 만드는 재주가 있어.”

나는 고개를 절레절레 내젓는 당사독과 함께 나란히 걸음을 옮겼다.

외원을 넘어 내원으로, 그리고 내원을 넘어 후원으로 진입하자 어느 순간 보이지 않는 곳에서 은밀히 뒤따라 오던 기척들이 완전히 사라졌다.

“노, 아니 스승님께서 후원에 머무르고 계십니까?”

“맞네, 이틀 전에 도착하셨지.”

이틀이라면 시기상으로 얼추 맞아 떨어진다.

내가 잠시 깨어났다가 다시 잠들어 있던 기간이 사흘.

사태를 파악한 적천강은 조금도 지체하지 않고 사천으로 향했고, 깊은 잠에 빠진 나를 지키며 후미에 남은 일행의 속도는 그보다 느릴 수밖에 없었다.

“그래도 아직 당가에 머무르고 계시다니 다행입니다. 내심 무슨 일이 생기진 않았을까 걱정했거든요.”

“걱정? 자네 스승께서 어떤 분인지 잊었나?”

“별호가 살벌해서 그렇지, 막상 알고 보면 은근히 허점투성이에요. 의외로 말랑말랑한 구석도 있고.”

“허.”

내 말을 들은 당사독이 헛웃음을 흘렸다.

“천하의 화왕(火王)을 두고 그런 식으로 말할 수 있는 건 자네가 유일할 거야. 하긴, 그만큼 제자를 아끼시니 이런 상황에서도 별다른 사단이 안 난 거겠지만.”

“이런 상황이요? 무슨 일이 있었습니까?”

“그러니까…… 아닐세. 직접 확인하는 게 빠르겠군.”

도대체 뭐지?

사실 나로서도 마음에 걸리는 점이 몇 가지 있긴 했다.

이를테면 한참이나 먼저 앞질러 간 적천강이 아직도 사천당가에 머무르고 있다거나, 당사독이 의도적으로 화룡각 대원들을 제외하려 했다는 느낌이 그랬다.

‘설마.’

여러 안 좋은 상상들이 머릿속을 스쳐 지나간다.

적천강이 홀로 움직이다가 암천의 습격을 받은 것은 아닐까.

혹은 완쾌된 줄 알았던 몸 상태가 남천마후와의 전투로 인해 악화된 것일까.

‘그게 아니면 또…….’

온갖 생각이 꼬리에 꼬리를 물고 늘어지던 그 순간이었다.

사천당가에서도 가장 깊숙한 곳에 자리 잡은 후원. 각양각색의 초목이 어우러진 그곳에 들어선 자그마한 모옥(茅屋)이 눈에 들어온 것은.

그리고 백여 장도 넘게 떨어져 있음에도, 천둥처럼 울려 퍼지는 목소리가 귓가를 파고든 것은.

“냉큼 자리에서 일어나지 못할까!”

“안 일어납니다! 못 일어납니다!”

“그 아이가 위험하단 말이다!”

“여기에도 아직 치료를 받아야 할 환자들이 남아 있습니다!”

“노부의 제자다!”

“제 환자들입니다!”

“지금 네놈이 안 가면 그 녀석의 목숨이 위태롭다고 노부가 수십 번을 말하지 않았느냐!”

“그랬으면 제가 아직 여기 남아 있겠습니까? 우선 상태 들어 보고 괜찮을 것 같다는 확신이 있으니 여기서 기다려 보자고 한 것 아닙니까! 지금까지 수백 번은 말했습니다!”

“아니, 그래도 이놈이! 노부가 판단하기에는 그게 아니라니까!”

“판단은 의원이 하는 것이고, 제가 바로 그 의원입니다!”

“무인의 상태는 같은 무인이 잘 아는 법. 노부가 바로 화왕 적천강이니라!”

“제 스승님은 신의인 동시에 살성이십니다! 그런 분의 가르침을 고스란히 이어받은 제가 어르신보다는 더 잘 압니다!”

“어어, 지금 그 인간 뒷배를 믿고 노부에게 깝치는 것이냐?”

“어어, 지금 제 면전에서 스승님 욕보이시는 겁니까?”

“이노옴!”

“아, 몰라. 배 째십시오! 점혈을 하든, 납치를 하든 상관없습니다! 단, 절 강제로 데려간다면 치료를 거부하겠습니다!”

“이런 돌팔이 같은 놈을 봤나! 오냐, 지금부터 셋을 세겠다! 그때까지 그 염병할 행낭을 들고 일어나지 않으면 각오하는 것이 좋을 것이다! 자, 하나!”

“둘, 셋! 됐습니까!”

“이, 이놈이 감히……!”

“이제 어르신 마음대로 하십시오! 저는 이만 약초나 채집하러 가야겠습니다!”

쾅!

마지막 외침과 동시에 거칠게 열리는 모옥의 문.

말 그대로 문을 박차고 뛰쳐나온 노인이 잔뜩 헝클어진 백발을 가다듬으며 씩씩거렸다.

“가뜩이나 할 일도 많은데 한두 번도 아니고. 내가 더러워서 진짜 이 짓도 때려치우든가 해야지.”

제아무리 공력의 도움이 있었다지만, 제법 먼 거리에서도 들릴 정도의 목소리 크기.

방 안에서 고래고래 소리를 지르던 누군가의 발작 버튼이 눌리는 건 당연했다.

“마! 거기 안 서! 칠순밖에 안 된 핏덩이 주제에 감히! 네 스승이 그따위로 가르치……!”

그 순간, 천둥 같던 외침이 뚝 끊겼다.

방 안에서 뛰쳐나오자마자 나와 시선이 마주친 중년인이 제자리에서 굳었다.

어디선가 불어온 바람이, 마치 불길처럼 타오르는 것 같은 중년인의 붉은 머리카락을 흔들었다.

스스스슥.

무겁게 가라앉은 공기. 중년인에게 뭐라 대꾸하려던 노인도 이상함을 눈치채고 고개를 돌렸다.

그리고 나와 당사독을 말없이 응시하던 그가 무거운 침묵을 깨트렸다.

“어서 오십시오, 두 분 모두.”

언제 그랬냐는 듯, 마치 신선(神仙)처럼 온화한 목소리와 미소. 하지만 이미 모든 상황을 똑똑히 보고 들은 나는 속지 않았다.

그리고 동시에 깨달았다.

앞서 당사독에게 들었던 말에 담긴 의미를.

거기에 더해 왜 화룡각 대원들과 호위까지 떼어 놓고 왔었어야 했는지를.

‘추하다……!’

말 그대로다. 이건 추해도 너무 추했다.

칠순 먹은 신의와 백 살도 넘은 화왕의 치열한 말싸움은, 듣고만 있어도 가슴이 옹졸해지게 만드는 무언가가 있었다.

만약 무림의 누군가가 이 광경을 보았더라면, 적천강이 화왕 대신 또 다른 별호를 얻게 되리라는 것에 혁무진의 불알 두 쪽을 걸 용의도 있었다.

‘추왕(醜王) 적천강……!’

오랜만에 봤으니 분명 반가워야 하는데, 나를 위해 여기까지 와서 신의를 땅콩처럼 달달 볶고 있는 모습에 감동해야 하는데 그게 참 쉽지가 않다.

“아, 날씨 한번 좋다.”

이런 상황을 예상했다는 듯, 이미 먼 산을 쳐다보는 당사독의 뇌까림이 공허하게 느껴지는 것은 왜일까.

깊게 가라앉은 눈빛으로 나를 바라보던 붉은 머리카락의 중년인, 적천강이 무거운 목소리로 입을 열었다.

“몸은……?”

“괜찮습니다…….”

“어디까지…… 들었느냐?”

나는 슬픈 목소리로 대답했다.

“아무것도…… 못 들었습니다.”

적천강이 맑은 하늘을 우러러보며 탄식했다.

“이런 씨부랄. 다 들었네…….”

오랜만에 조우한 스승과 제자는 그렇게 한동안 서로의 얼굴을 바라보지 못했다.

여름이었다.
```

## Final English reading copy

```markdown
# Chapter 840

In the Sichuan Tang Clan, a family built around its bloodline, the Family Head’s authority was absolute. No—in truth, even if Tang Sadok hadn’t been the Family Head, that fact wouldn’t have changed much.

The title Myriad-Poison Asura was enough to inspire both awe and fear.

“Our Benefactor looks tired from the long journey.”

At Tang Sadok’s words, the throng surrounding me naturally began to disperse.

The Sichuan Tang Clan’s martial artists, along with outsiders from Emei, Qingcheng, and the Beggars’ Sect, clasped their hands toward Tang Sadok and me before heading back to their posts.

They didn’t forget to urge us to visit their sects, either.

“So you’re the very pillars of the Fire Dragon Pavilion I’ve heard so much about.”

Tang Sadok had been taking a good look at the members of the Fire Dragon Pavilion while I exchanged greetings with the others. Then he suddenly paused.

“As I understand it, every member of the Fire Dragon Pavilion is young. Have you been struck by some deadly poison?”

Namho, the old young man singled out, answered with a face like he’d bitten into something foul.

“Nothing like that.”

“If not poison, then qi deviation?”

“You trying to start something with me?”

“Ah, I only asked because I couldn’t sense any internal energy. In that case, perhaps your age is…”

“Seventy-five. I’m traveling with these fellows for a while, for certain reasons.”

“I see. I spoke out of turn.”

“I understand. We’re both getting old, after all. It happens.”

Though Namho practiced no martial arts, Tang Sadok regarded his confidence with interest. He showed kindness to Ju Hwaran, granddaughter of the Escort King, and to Song Ilseom, who’d reached an impressive realm at a young age. As for Sama Pyo and Taishan, who strictly speaking belonged to the demonic, heterodox arts, he simply gave them a silent nod.

And then…

“What happened to that fellow?”

“Uh, well. Something came up on the way here.”

“It must have been quite something. I’ve never seen a face swell up that much. Was it Dark Heaven?”

“No. I actually hit him a few times.”

Silence fell for a moment.

Tang Sadok looked back and forth between me and Hyuk Mujin, who was slung over Taishan’s shoulder like a sack of luggage, then sighed.

“I’ll have someone look after your subordinates. For now, unpack and visit the Medical Hall in the Outer Court. They’ll treat him well.”

As one of the guards waiting nearby approached at Tang Sadok’s gesture, Taishan spoke in his usual flat voice.

“Taishan. And us. Not moving. No—we are not moving. Until Pavilion Master orders us.”

“Ah, of course. There should be food ready for you, too.”

“I’ll go, then, Pavilion Master. See you later.”

“……”

He really was a lunatic.

I mean, if he was going to do that, why say anything in the first place?

I stopped Ju Hwaran with a glance as she started to smack Taishan upside the head, then followed Tang Sadok toward the Inner Court.

“You seem to earn people’s trust wherever you go. Here in Sichuan, and even among subordinates who haven’t been with you long.”

I answered with a quiet laugh, then spoke as I watched the people slowly disappearing from sight.

“Seems like the same goes for you, Great Hero Tang. I didn’t expect those people to still be with the Sichuan Tang Clan.”

“It’s something I’m truly grateful for. I felt ashamed to keep relying on them, so I told them more than once that they were free to go… Yet they’ve stayed with our family all this time. They’re treating the sick who haven’t yet recovered and continuing to help rebuild the clan.”

“What I’ve seen may not be everything, but the Outer Court already looks much as it did before.”

“Rebuilding is only an excuse. They’re stationed at the family home in case Dark Heaven attacks again. I know the circumstances, so I can’t bring myself to tell them to leave.”

“What?”

“We have to face the truth. If something like last time happens again while they’re gone…I’ll have to choose one of two things as Family Head. Either abandon the home our family has built over generations and run, or make one last stand and be wiped out.”

My eyes widened before I could stop them. I hadn’t expected the Family Head of the Sichuan Tang Clan—one of the Central Plains’ most renowned great clans, known for its pride—to say something like that.

And knowing what Tang Sadok was like, the surprise hit all the harder.

“Are you surprised because I was too honest?”

“Mm. I suppose I am.”

“I understand. Especially since you knew what I was like before all this happened.”

“Of course. Back then, you really…had quite a temper.”

“Hah. I was.”

Tang Sadok let out a hearty laugh, and I gaped at him.

“Are you sure you’re feeling all right?”

“I’m perfectly fine. I’ve simply decided to change.”

“Still, be careful. They say when a person changes too suddenly, it means they’re about to die.”

“Hahaha. You’re still honest to a fault. Though that is your greatest charm.”

“Um, sorry, but I have my own preferences.”

“Yes, that sort of joke isn’t bad either.”

“I’m serious.”

“……I take back what I said just now. You do have a talent for getting under people’s skin.”

I shook my head as I walked beside Tang Sadok.

We crossed the Outer Court, then the Inner Court, and entered the Rear Court. At some point, the unseen presences that had been secretly following us from a distance disappeared completely.

“Is the old—no, is my Master staying in the Rear Court?”

“He is. He arrived two days ago.”

That timing seemed about right.

I’d woken briefly, then fallen asleep again. Three days had passed.

After assessing the situation, Jeok Cheongang had headed for Sichuan without the slightest delay. The rest of the party, who’d stayed behind to look after me while I was deep in sleep, couldn’t have traveled as fast as he did.

“I’m glad he’s still at the Tang Clan. I’d been worried something might have happened to him.”

“Worried? Have you forgotten what kind of person your Master is?”

“His title sounds terrifying, but once you get to know him, he’s full of holes. He’s softer than you’d expect, too.”

“Huh.”

Tang Sadok let out a disbelieving chuckle.

“You’re probably the only person in the world who could talk about the Fire King that way. Then again, he cares for you that much. That must be why nothing serious has happened, even under these circumstances.”

“These circumstances? Did something happen?”

“I mean…never mind. It’ll be quicker if you see for yourself.”

What on earth was going on?

There were a few things that had been bothering me, too.

For instance, Jeok Cheongang had arrived long before us, yet was still at the Sichuan Tang Clan. And Tang Sadok had seemed to deliberately leave out the Fire Dragon Pavilion members.

*No way…*

All sorts of unpleasant possibilities flashed through my mind.

Had Jeok Cheongang been attacked by Dark Heaven while traveling alone?

Or had his condition, which I thought had fully recovered, worsened after his fight with the Southern Heaven Demon Empress?

*Or maybe…*

My thoughts chased one another around in circles. That was when I spotted a small thatched cottage nestled among the varied plants in the deepest part of the Sichuan Tang Clan’s Rear Court.

And though I was more than three hundred yards away, a voice boomed like thunder and pierced my ears.

“Get up this instant!”

“I’m not getting up! I can’t get up!”

“That boy is in danger!”

“There are still patients here who need treatment!”

“He’s my Disciple!”

“They’re my patients!”

“How many times have I told you that boy’s life is in danger if you don’t go now?”

“If it were that bad, would I still be here? I heard about his condition, and I was sure he’d be all right, so I told you we should wait here! I’ve said that hundreds of times by now!”

“No, but you—! I’m telling you, I don’t think that’s what’s going on!”

“The physician decides that, and I’m the physician!”

“One martial artist knows another’s condition best. And I am Jeok Cheongang, the Fire King!”

“My Master is both the Divine Physician and the Slaughter Saint! I inherited his teachings in full, so I know better than you do, Elder!”

“Hey, are you talking back to this old man because you’re counting on that man’s backing?”

“Hey, are you insulting my Master right in front of me?”

“You insolent brat!”

“Oh, I don’t care. Go ahead and do your worst! Strike my pressure points, kidnap me—I don’t care! But if you take me by force, I refuse to treat him!”

“Would you look at this quack! Fine! I’ll count to three! If you don’t get up with that damned travel bag by then, you’d better be ready! One!”

“Two, three! There, happy?”

“You insolent little—!”

“Do whatever you want now! I’m going to gather herbs!”

Bang!

The cottage door flew open with one last shout.

An old man came bursting out as if he’d kicked it down. He smoothed his wildly mussed white hair and grumbled furiously.

“I’ve got enough work as it is, and this is more than once or twice now. I’m so sick of this I ought to just quit!”

Even with internal energy lending it force, his voice had carried a considerable distance.

It was only natural that someone inside, who’d been shouting at the top of his lungs, would be set off.

“Hey! You’re not going anywhere! You’re nothing but a baby who’s only seventy! How dare you! Is that how your Master taught—”

At that moment, the thunderous shout cut off.

A middle-aged man had rushed out of the cottage, then frozen in place when his gaze met mine.

A breeze blew in from somewhere, ruffling the man’s red hair as if it were burning like flames.

*Rustle.*

The air grew heavy. The old man, who’d been about to snap back at him, sensed something was off and turned around.

After silently staring at Tang Sadok and me, he broke the heavy silence.

“Welcome, both of you.”

His voice and smile were gentle, as if he were a Daoist immortal, as though nothing had happened. But having seen and heard everything with my own eyes and ears, I wasn’t fooled.

And at the same time, I understood what Tang Sadok had meant earlier.

I also understood why he’d left the Fire Dragon Pavilion members and the guards behind.

*Pathetic…!*

That was exactly what it was. This was just too pathetic.

The fierce argument between a seventy-year-old Divine Physician and a Fire King over a hundred had a way of making your heart shrink just listening to it.

If anyone in Murim had witnessed that scene, I would’ve been willing to bet both of Hyuk Mujin’s balls that Jeok Cheongang would earn himself another title to go with Fire King.

*The Disgrace King, Jeok Cheongang…!*

I should’ve been happy to see him again after so long. I should’ve been moved that he’d come all this way for me and was roasting the Divine Physician like a peanut over a fire. But it wasn’t easy.

But it wasn’t easy.

“Ah, what a lovely day.”

Tang Sadok’s mutter, as he gazed at a distant mountain as though he’d expected this, sounded strangely hollow.

The red-haired middle-aged man—Jeok Cheongang—looked at me with eyes heavy with emotion and spoke in a solemn voice.

“Your body…?”

“I’m fine…”

“How much…did you hear?”

I answered in a sad voice.

“Nothing… I didn’t hear anything.”

Jeok Cheongang looked up at the clear sky and sighed.

“Fuck. You heard everything…”

The Master and Disciple, reunited after so long, couldn’t look each other in the face for a while.

It was summer.
```

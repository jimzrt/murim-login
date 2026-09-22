<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0627.txt",
      "sha256": "558643fbef594f4b4155dbbe852f4283eb8e52e8fabb3ad3c550ec5e81c2358e",
      "bytes": 13004
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "ed22503d1bedcf718b5701da039bdc1f6e6d8fb117fc2d3a9b6b9027f6f68ad8",
      "bytes": 1972
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "af611c85091068c4bb5b2c4a240ddb26d9f731678005f55d36327e25c866fac4",
      "bytes": 193474
    },
    {
      "path": "characters/Baeksang.md",
      "sha256": "7708cbc36f32237487e3f0b960fabcb7aa4063565a9304edb32e7b90e08d8a90",
      "bytes": 701
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "85db17105b92908e677a5bf4f938451fa26e5cb1ed0b98151a4e6e40aedaaf7a",
      "bytes": 1206
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "2fe4c28099e0c51731991bca8234daf9b7108e40697d2de545d98ba391e53710",
      "bytes": 1702
    },
    {
      "path": "characters/Ju Hwaran.md",
      "sha256": "28aff3e9d03d322d029f1d77f736d28b94c3c9bb9e0ebbccd53cbfbb2c2baca2",
      "bytes": 1043
    },
    {
      "path": "characters/Namho.md",
      "sha256": "9e2280ea81863904b2cdd12f2d2549cdc654a83b74802a52de9b19209f8eb621",
      "bytes": 843
    },
    {
      "path": "characters/Sama Pyo.md",
      "sha256": "0eef40c7d16a36be6cad5623c40b2de32634b2d669c5277e9685aef587d16478",
      "bytes": 899
    },
    {
      "path": "characters/Song Il.md",
      "sha256": "7f44b92582c64ac33cd6b7e31587f2d755d177d2de7d7bd71df1c597b3d91774",
      "bytes": 964
    },
    {
      "path": "characters/Song Ilseom.md",
      "sha256": "324b48a37e5e5670a4801e778ff200f20f335ceb9adacb73c11edd4ed94fba09",
      "bytes": 957
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "f3cd9f8aef2a9afa759d0af4b0c279e40b84e2eaeccbc0fff70fdf9a304201a7",
      "bytes": 528
    },
    {
      "path": "characters/Yayul Mok.md",
      "sha256": "f72d4d52375498828c60b706d98870119c7c4e781af2134ada4808d6692f99dd",
      "bytes": 946
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "2c497e8bc7482da5eee722176f752fe7418978ea6d90e36eb31fefba6a9c86ea",
      "bytes": 199152
    }
  ],
  "estimated_tokens": 12500
}
-->

# Durable State Update — Chapter 627

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 627. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 627. Profile updates may replace only one
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
  "chapter": 627,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 627,
    "continuity_sources": [627],
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
    "The Fire Dragon Pavilion has been sent to its lodging after meeting Yayul Cheok, with further discussions pending.",
    "Yayul Cheok personally welcomes Jin Taekyung as Jeok Cheongang's Disciple and receives the Fire Dragon Pavilion as Murim Alliance representatives.",
    "Yayul Mok is Yayul Cheok's only son for three generations and serves as Young Palace Lord of the Nanman Beast Palace.",
    "Baeksang is the great chieftain of the Bai people, one of Nanman's four most powerful great tribes.",
    "Baeksang is Yayul Cheok's sworn younger brother and childhood companion; they fought together during the Great Faction War.",
    "Baeksang and Yayul Cheok are now estranged, with Baeksang refusing Yayul Cheok's fruit wine for decades.",
    "Baeksang declares that the Nanman Beast Palace will never join the Murim Alliance, following the previous tribal council's result.",
    "Baeksang watches Jin Taekyung with cold scrutiny, but the reason for his interest is unknown."
  ],
  "continuity_sources": [
    626,
    625
  ],
  "open_questions": [
    "Why does Baeksang oppose joining the Murim Alliance despite his lifelong bond with Yayul Cheok and their shared service in the Great Faction War?",
    "What is the meaning of Baeksang's cold scrutiny of Jin Taekyung?",
    "Will Yayul Cheok be able to overcome the previous tribal council's opposition and bring the Nanman Beast Palace into the Murim Alliance?",
    "Are the Bai people and other tribes aligned behind Baeksang's opposition?",
    "Was the timing of the Heavenly Demon Escort Bureau massacre connected to Dark Heaven's scheme?"
  ],
  "safe_through": 626,
  "temporary_decisions": [
    "Use Baeksang for 백상 and do not treat White Elephant as a separate alias.",
    "Use sworn younger brother for 불알 동생 in the relationship between Yayul Cheok and Baeksang.",
    "Use Jiang Taigong for 강태공 and Jindro for 진드로."
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
| 남만야수궁  | **Nanman Beast Palace**          |
| 중원     | **Central Plains**                               |                                                       |
| 표국     | **Escort Bureau**                            |
| 전각     | **pavilion**                                 | Use “hall” only when established for a specific named building |
| 보상               | **Reward**                     |
| 정마대전   | **Great Faction War**         |
| 귀가      | **your family**                                                 |
| 백상 | **Baeksang** | Great chieftain of the Bai people and Yayul Cheok's sworn younger brother. |
| 남호 | **Namho** | Hidden Shadow Pavilion code name; literally associated with amber from the south. |
| 사마표 | **Sama Pyo** | Young Sect Leader of the Black Dragon Demon Gate. |
| 송일섬 | **Song Ilseom** | Young escort captain of the Yongbong Escort Bureau; distinct from Song Il of Zhongnan. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 야율목 | **Yayul Mok** | Young Palace Lord of the Nanman Beast Palace. |
| 논산 | **Nonsan** | Location of Korea's Hunter training center. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 숙부 | **Uncle** | Lee Seowol's shortened address for Cheol Mubaek. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 한족 | **Han Chinese** | Ethnic designation used by the steppe chieftains. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 준이 | **Jun** | Family nickname used in the form Jun's dad. |
| 화란 | **Hwaran** | Familiar short form of Ju Hwaran. |
| 푸린 | **Furin** | Russian president mentioned in a forum headline. |
| 새외 | **Outer Lands** | Lands outside the Central Plains and its Murim. |
| 야수묘왕 | **Beast Miao King** | Leader of the Miao people and master of the Nanman Beast Palace. |
| 화룡각 | **Fire Dragon Pavilion** | New name chosen for Taekyung's pavilion. |
| 천마표국 | **Heavenly Demon Escort Bureau** | A Sichuan group whose arrival preceded the Yeongin massacre; all members were later found dead from venom. |

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
| 관리 | 적천강 | government official to legendary martial master | you | formal, then alarmed and deferential | The official questions Jeok Cheongang, insults him as an old man, and later learns that he is the Fire King. |
| 적천강 | 관리 | legendary martial master to government official | you | blunt and mocking | Jeok Cheongang repeatedly echoes the official's formal phrasing while challenging his authority. |
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
| 혁무진 | 조장님 | pavilion_member_to_squad_leader | Captain | deferential and dubious | Mujin questions whether the pasture should be called the Nanman Ranch instead of the Nanman Beast Palace. |
| 남호 | 사마표 | guide_to_young_sect_leader | Young Sect Leader | blunt and admonishing | Namho warns Sama Pyo that all grass and animals in the territory belong to the Nanman Beast Palace. |
| 남호 | 주화란 | guide_to_escort_bureau_head | Escort King's granddaughter | approving and familiar | Namho praises Hwaran for recalling Ju Gongsan's records about Nanman. |
| 사마표 | 남호 | young_sect_leader_to_guide | Elder Namho | formal and apologetic | Sama Pyo apologizes after Taishan attempts to seize the calf. |
| 야율목 | 백상 | nephew_to_father's_sworn_younger_brother | Uncle Baeksang | ceremonial and deferential | Yayul Mok formally greets Baeksang as he arrives at the stone door. |
| 백상 | 야율목 | father's_sworn_brother_to_nephew | you | cold and formal | Baeksang questions Yayul Mok about his return, the pasture fire, and the Palace Lord's whereabouts. |
| 야수묘왕 | 백상 | sworn_older_brother_to_sworn_younger_brother | Baeksang | familiar and bittersweet | Yayul Cheok offers Baeksang his preferred fruit wine and asks why he came. |

## Listed compact profiles

### Baeksang.md

# Baeksang (백상)

- **Safe through:** Chapter 626
- **Aliases:** None
- **Role:** Baeksang is the middle-aged great chieftain of the Bai people, one of Nanman's four most powerful great tribes.
- **Personality:** Cold, rigid, meticulous, and politically resolute, with a deep but guarded attachment to his sworn elder brother.
- **Voice:** Rigid, formal, restrained, and emotionally distant.
- **Relationships:** Baeksang is Yayul Cheok's sworn younger brother and childhood companion; they fought together during the Great Faction War. He is Yayul Mok's sworn uncle and opposes the Nanman Beast Palace joining the Murim Alliance.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 626
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and a member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son; he uses quiet practices such as fishing to empty his mind. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 625
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm, and the occupant of the chief seat of the Murim Alliance's Five Kings Hall.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Ju Hwaran.md

# Ju Hwaran (주화란)

- **Safe through:** Chapter 626
- **Aliases:** Hwaran
- **Role:** Ju Hwaran is a Level 88 Young Bureau Head, leader of the Yongbong Escort Bureau, a member of the Fire Dragon Pavilion, an experienced Nanman escort guide with route knowledge from the Escort King's records, and someone who can understand the Miao and Bai languages.
- **Personality:** Intelligent, capable, responsible, filial, composed under pressure, and burdened by intense guilt over the escort journey's deaths.
- **Voice:** Clear, polite, restrained, and determined.
- **Relationships:** Escort King Ju Gongsan was her paternal grandfather, Ju Hogun is her father, Heo Jun was her uncle, Sama Pyo was her former fiancé in a political engagement she accepted for her father's sake, Song Ilseom is her direct escort who accompanied her previous journey to Yeongin, and Jin Taekyung is a trusted ally; the Yongbong Escort Bureau has longstanding ties with Yeongin’s inhabitants.

### Namho.md

# Namho (남호)

- **Safe through:** Chapter 626
- **Aliases:** Elder Chao
- **Role:** Namho is an eighty-year-old non-Han Hidden Shadow Pavilion agent who spent more than fifty years operating under the cover of the Poison Flower Pavilion in Nanman and now serves as the Fire Dragon Pavilion’s guide.
- **Personality:** Duty-bound, pragmatic, observant, and willing to use theatrical violence and crude insults to protect an intelligence operation.
- **Voice:** Measured and serious in private, but loudly abusive and convincing when maintaining his local cover.
- **Relationships:** Namho is a Hidden Shadow Pavilion contact for Jin Taekyung and the Fire Dragon Pavilion, receives intelligence from the Pavilion Master, and knows the code used by the Thousand-Faced Fox.

### Sama Pyo.md

# Sama Pyo (사마표)

- **Safe through:** Chapter 626
- **Aliases:** Black Dragon Saber
- **Role:** Young Sect Leader of the Black Dragon Demon Gate, a Morning Star reputed to be no less than the Ten Dragons and Phoenixes, and a member of the Fire Dragon Pavilion.
- **Personality:** Outwardly courteous and smiling, inwardly calculating, but genuinely protective of Taishan and willing to redirect blame onto his subordinate.
- **Voice:** Polite and ingratiating in public, with sardonic humor and controlled evasiveness.
- **Relationships:** Sama Pyo commands the absolutely loyal Taishan, is Sima Gong's son, was Ju Hwaran's former fiancé in a political engagement, and has joined the Fire Dragon Pavilion while openly intending to use Jin Taekyung as a useful card; he is now openly hostile toward fellow member Song Ilseom.

### Song Il.md

# Song Il (송일)

- **Safe through:** Chapter 626
- **Aliases:** Roaring Fury Swordsman
- **Role:** Elder of the Zhongnan Sect and the Roaring Fury Swordsman; senior brother of Sect Leader Gong Iljung; came to the Jin Family of Taiyuan to demand redress for Gong Ilhyuk's injury and the alleged insult to Zhongnan; attacked Jin Taekyung with the Heavenly River Thirty-Six Swords, was stopped by Jeok Cheongang, and was publicly humiliated by him.
- **Personality:** Arrogant, domineering, punitive, and confident in his martial power and seniority.
- **Voice:** Gruff, cutting, condescending, and threatening, with formal authority used to pressure those beneath him.
- **Relationships:** Gong Iljung is his junior Sect Leader and martial younger brother; Gong Ilhyuk is a junior Disciple of his sect; he recognizes Baek Museong and Cheongpung through their Huashan and Sword Saint connections.

### Song Ilseom.md

# Song Ilseom (송일섬)

- **Safe through:** Chapter 626
- **Aliases:** Escort Captain Song
- **Role:** Level 110 young escort captain of the Yongbong Escort Bureau, one of its Dragon-Phoenix Three Escorts, and a newly accepted member of Jin Taekyung and Cheongpung’s Fire Dragon Pavilion.
- **Personality:** Blunt, decisive, survival-hardened, and dryly self-aware, with little patience for insults or disorder and practical survival skills such as making disguise masks.
- **Voice:** Forceful and urgent in command, with a rough and confrontational edge.
- **Relationships:** He serves under Ju Hwaran and has expressed concern that she not be hurt or die needlessly; he is Song Pyosan’s son, his grandmother was the surviving Guangdong Chen child rescued by Ju Gongsan during the Great Faction War, and he remains openly hostile toward fellow Fire Dragon Pavilion member Sama Pyo.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 626
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord.

### Yayul Mok.md

# Yayul Mok (야율목)

- **Safe through:** Chapter 626
- **Aliases:** None
- **Role:** Yayul Mok is the non-Han Young Palace Lord of the Nanman Beast Palace, a spear-wielding warrior who rides a white tiger, and a halting but capable speaker of Han Chinese.
- **Personality:** Protective of Nanman Beast Palace livestock, quick-tempered toward trespassers, and capable of restraint once he recognizes legitimate authority.
- **Voice:** Blunt, commanding, and formal-polite toward strangers, becoming openly insulting when provoked.
- **Relationships:** Yayul Cheok is the Beast Miao King, lord of the Nanman Beast Palace, and Yayul Mok's father; Yayul Mok is his only son for three generations; Baeksang is his father's sworn younger brother; his white tiger is a long-bonded companion; he orders Jin Taekyung and the Fire Dragon Pavilion to follow him after the pasture fire.

## Korean source

```text
＃627화



임시로 배정받은 처소는 그럭저럭 괜찮았다. 비록 중원만큼 화려하고 고급스럽지는 않았지만, 정갈하면서도 나와 화룡각 대원들이 당분간 머무르기에 부족함이 없었다.

물론 그렇다고 해서, 무조건적인 환대를 받았다는 뜻은 아니다.

“음. 지금 내 젓가락에 끼워져 있는 게 뭔지 아는 사람?”

식사 도중 내가 출제한 깜짝 퀴즈에, 혁무진이 번쩍 손을 치켜들었다.

“어, 그래. 무진이. 대답해 봐.”

“정답! 벌레입니다!”

“맞아, 정확히는 지네지. 그런데 왜 이딴 게 음식 속에 있을까?”

“음. 남만 이민족들의 풍습이 아닐까요?”

80년 차 경력의 남만 이민족인 남호가 송충이 비슷한 것을 골라내며 중얼거렸다.

“난생처음 듣는 풍습인데……?”

차라리 메뚜기 구워 먹는 정도면 어느 정도 이해를 하겠는데, 이건 살아 있는 벌레를 쏟아부은 수준이라 실드도 못 친다.

이 와중에도 열심히 접시에 코박죽을 시도하는 태산의 모습을 지그시 바라보던 사마표가 한숨을 내쉬었다.

“역시 환영받지 못하는 모양이군.”

이래서야 식사가 될 리 없다. 젓가락을 내려놓은 송일섬이 담담하게 말을 받았다.

“아무래도 천마표국 일 때문이겠지.”

동감이다. 하지만 그렇다고 해서 야율목이 직접 이런 일을 지시했다고도 생각하지 않았다.

소궁주씩이나 되는 녀석이 이렇게 치졸한 방법을 사용하지는 않을 테니까.

‘결국 남만야수궁 내부의 다른 이민족들의 짓이다, 이건데.’

남만에 들어선 후부터 지금까지 꾸준히 미움을 받다니. 미운 오리 새끼도 이 정도는 아닐 거라 생각하던 그때, 식사 전에 씻으러 간다며 이 층으로 올라갔던 주화란이 슬그머니 나타났다.

“어? 벌써 다 씻으셨어요?”

아니, 올라간 지 얼마나 됐다고 벌써? 논산 훈련소 54번 훈련병도 이 정도로 빨리 씻지는 못한다.

의문이 담긴 내 물음에 주화란이 애매한 웃음을 지으며 대답했다.

“아, 네.”

“……?”

어째 안 좋은 느낌이 딱 온다. 내가 말없이 바라보자 잠시 망설이던 주화란이 입을 열었다.

“사실 그게…….”

전후사정을 모두 들으니 실소가 흘러나왔다.

“이 날씨에 펄펄 끓는 물을 줬다고요? 그것도 오물 비슷한 걸 섞어서?”

주화란이 곤란한 얼굴로 고개를 끄덕였다.

“사실 말씀 안 드리려고 했어요. 단순한 착오일 수도 있는데 혹시 이 일로 문제가 생길까 봐…….”

“단순한 착오 아닙니다. 그리고 신경 쓰지 마세요. 어차피 그거 아니어도 다른 문제가 있으니까.”

그제야 식사 상황을 알아챈 주화란이 짧은 감상평을 남겼다.

“으.”

“혹시나 해서 여쭤보는 건데, 드실 건 아니죠?”

“네. 당연히.”

주화란이 이렇게 단호하게 대답하는 건 처음 본다. 작게 혀를 찬 나는 자리에서 일어났다.

“조장님. 어디 가세요?”

“깽판 치러.”

가만히 있으면 가마니로 알고, 보자 보자 하면 보자기로 아는 게 세상 이치다.

아무래도 남만야수궁을 설득하러 온 입장이니 어느 정도의 선은 지키겠지만, 한 번 정도는 지랄을 떨어 줘야 두 번 다시 이런 짓을 안 하지.

곧장 문을 열어젖히려던 나는, 문득 잊었던 말을 떠올리고 걸음을 멈췄다.

“아. 그리고.”

“예?”

“쟤 좀 그만 먹게 해라.”

내가 말한 ‘쟤’가 누구인지 되묻는 사람은 아무도 없었다.

이 중에서 형형색색의 벌레 볶음밥을 세 그릇째 처먹고 있는 건 한 명밖에 없었으니까. 사마표가 슬픈 눈으로 태산을 바라보았다.

“태산. 멈춰……!”

그래, 제발 좀 멈춰.



* * *



그건 지금껏 내가 본 것 중 가장 거대한 나무였다.

수십 명의 장정이 양팔을 펼친 채 감싸 안아야 할 것 같은 엄청난 둘레와 최소 수십 장에 달하는 까마득한 높이.

보자마자 내심 탄성이 흘러나왔지만, 내가 이곳을 찾은 목적은 나무를 구경하기 위해서가 아니라 한 사람을 만나기 위해서다.

“마. 내려와.”

푸스슥.

울창한 잎사귀가 흔들린다. 곧이어 나직한 맹수의 울음소리와 함께 야율목의 떨떠름한 목소리가 귓가를 파고들었다.

“또 네놈이군. 여긴 어떻게 알고 왔지?”

“물어보니까 알려 주던데. 너 여기 자주 온다고.”

“누구한테?”

“전각 관리하는 놈.”

“황개가?”

“황개인지 똥개인지. 뭐 그런 이름이었던 것 같기도 하고.”

“한족에게 그런 걸 알려 줄 자가 아닌데.”

“한족한테는 몰라도, 주먹한테는 잘 알려 주던데?”

“…….”

“내려와라. 목 아프다.”

아무리 생각해도 내가 목 아프다고 내려올 것 같지는 않아서, 친절하게 한 마디를 덧붙였다.

“나무 꺾어 버리기 전에.”

“이건 선조의 선조들께서 심은 나무다. 자그마치 천 년 전에 이 땅에 뿌리내렸단 말이다.”

“그럼 먼 훗날에 네 후손들이 그러겠지. 얘야, 여기에는 천 년 된 나무가 있었는데 어떤 한족 새끼가 와서 뿌리째 뽑아 버렸단다. 왜요, 엄마? 왜냐하면 우리 선조님이 좋은 말로 할 때 나무에서 안 내려왔거든.”

“…….”

“그러니까 내려와. 환경 파괴하기 전에.”

이번에도 거절하면 정말 뽑아야 하나, 생각했지만 야율목은 내가 생각했던 것 이상으로 자연을 사랑하는 녀석이었다.

스슥. 탁.

크르릉. 나뭇가지를 연달아 밟으며 부드럽게 착지한 백호(白虎)가 나를 향해 낮은 울음소리를 흘린다.

그런 백호의 목덜미를 가볍게 쓸어 준 야율목이 나를 노려보았다.

“미친놈.”

“아이, 새삼스럽게 뭘.”

쑥스럽게 뒤통수를 긁적이는 내 모습에, 분노로 얼굴이 벌겋게 달아오른 야율목이 맹수처럼 으르렁거렸다.

“황개는 어찌 되었지?”

“아, 그 인간. 사지는 멀쩡해. 약간 겁먹긴 했지만.”

“제정신이 아니군. 도움을 청하러 와서 남만인을 핍박하다니.”

“오해가 있는 모양인데, 정말 털끝 하나 안 건드렸어. 그 대신 멱살은 좀 잡았지만.”

내가 무슨 동네 양아치도 아니고, 중원에서도 그렇게 막 나간 적은 없었다.

항상 처음에는 부드럽게 말로 하다가 안 되니까 주먹을 쓴 거지. 그리고 이번에는 그럴 만한 사유도 충분했다.

“벌레 볶음밥. 목욕용 똥물.”

“뭐?”

“전통 풍습이 아니라면 남만야수궁의 손님 대접이 말이 아니네. 안 그래?”

미간을 찌푸린 채 잠시 뭔가를 생각하던 야율목이 한숨처럼 중얼거렸다.

“대충 어떻게 된 일인지 알 것 같군.”

“대충 알 것 같았으면 언질이라도 좀 해 놨어야지.”

“설마 그렇게 노골적으로 적의를 보일 줄은 예상 못 했…….”

뭐라 말을 이으려던 야율목이 문득 입을 다물더니, 나를 향해 이내 고개를 까딱 숙여 보였다.

“미안하다. 내 진심으로 사과하지.”

“……오.”

“뭐냐, 그 반응은?”

“별거 아냐.”

사실 조금 놀랐다. 비록 만난 지는 얼마 되지 않았지만, 자존심 강하고 거칠어 보이는 야율목이 이렇게 고분고분하게 고개를 숙일 줄은 몰랐기 때문이다.

‘잘못한 건 바로 인정하고, 뒤끝도 없는 뭐 그런 타입인가?’

잘못을 저지르는 건 쉽지만, 그 잘못을 인정하고 진심을 다해 사과하는 건 어려운 일이다.

그리고 그런 의미에서 보자면 남만야수궁의 젊은 소궁주는 생각보다 괜찮은 성격의 소유자였다.

“돌아가는 대로 사람을 바꿔 주지. 황개는 물론이고 연관된 자들 모두. 앞으로 이번 같은 일은 일절 없을 거다.”

“뭐, 그렇게 해 준다면야.”

“내 실수였다. 다시 한번 사과할 테니 아버지의 귀에 들어가는 일은 없었으면 한다.”

“왜. 가끔 잘못하면 맞기도 하고 그러냐?”

야율목이 울컥한 표정으로 대답했다.

“무슨 말도 안 되는 소리를!”

“아니면 말고. 그냥 굳이 부탁까지 하는 걸 보면 사흘 밤낮 동안 처맞나 싶었지.”

“아버지께서는 단 한 번도 내게 손 대신 적이 없다.”

사실 아버지가 야수묘왕이라면 손 안 대도 잘 자랄 것 같긴 하다.

저 덩치에 저 무위라면 아들은 물론이고 손자. 어쩌면 증손자까지 사춘기 프리 패스지.

내가 그런 생각을 하고 있을 때, 잠시 머뭇거리던 야율목이 작은 목소리로 덧붙였다.

“나는 괜찮겠지만 다른 이들은 예외지. 아버지께서 이 사실을 아신다면 불호령이 떨어질 거다.”

“아.”

“아버지께서 환영하신 손님에게 푸대접을 했으니 너희 한족들이 항의하는 건 당연하다. 하지만 그렇다고 해서 황개를 비롯한 다른 이들을 벌할 생각도 없어.”

“그 썅놈의 좆마표국 때문에 열 받았을 테니까?”

“……이름이 좀 틀린 것 같지만, 그것 역시 이유 중 하나지.”

“이유 중 하나라. 다른 이유도 있다는 말로 들리는데.”

한동안 말없이 나를 응시하던 야율목이 어느덧 얌전해진 백호의 턱을 쓰다듬으며 입을 열었다.

“정마대전(正魔大戰).”

“음?”

“우리는 중원에서 너무 많은 피를 흘렸다. 아버지의 주도하에 남만의 모든 부족이 힘을 모았고, 자그마치 일만에 달하는 전사가 전장으로 향했지만…… 살아서 고향으로 돌아온 이들의 숫자는 그중 반의 반도 되지 않았지.”

그르릉.

조용히 자신을 쓰다듬는 손길을 받아들이던 백호가, 걱정스러운 눈빛으로 주인을 바라본다.

복잡한 감정이 스며 있는 야율목의 목소리가 이어졌다.

“누군가의 부모. 누군가의 자식. 어릴 때부터 함께 자란 친구와 친인척들. 웃으며 전장으로 향한 그들 대부분이 돌아오지 못했다. 한참 후에 태어난 나조차도 마찬가지였다.”

“너도?”

“원래대로라면 난 소궁주가 될 수 없었겠지. 이게 아까 네가 했던 질문에 대한 진짜 대답이다.”

야수묘왕과 헤어진 직후 야율목과 나누었던 대화를 떠올린 나는 문득 깨달았다.

“위로 형제가 있었군.”

“셋. 그중 한 명은 누이였지. 비록 어렸고 여인의 몸이었지만 여느 전사 못지않게 용맹했다고 들었다. 만약 정마대전에 참전하지 않았더라면 누이는 사랑하는 사람과 혼례를 치렀을 거다. 아버지와 백상 숙부는 의형제인 동시에 사돈이 되었을 테고.”

“잠깐. 그렇다면…….”

“네가 지금 생각하는 것이 맞다. 정마대전이라 이름 붙인 한족들 간의 전쟁에서 아버지는 두 아들과 딸 하나를 잃었고, 백상 숙부는 목숨처럼 아끼던 아들을 먼저 떠나보내야 했지.”

야율목이 씁쓸하게 웃으며 한 마디를 덧붙였다.

“황개를 너무 탓하지 마라. 그는 부모와 일가친척 모두를 잃었으니까.”

나는 뭐라 할 말이 없어 그저 입을 다물었다.

사실 지금까지 이곳저곳에서 정마대전에 관한 이야기를 귀에 못이 박이도록 들었지만, 남만이 이 정도까지 큰 피해를 입었는지에 대해서는 몰랐다.

아니, 더 솔직히 말하자면 딱히 알 필요가 없다고 생각했던 것 같다.

남만은 중원에서 수만 리나 떨어진 새외였고, 무림과는 동떨어진 완전한 별개의 땅이라고 생각했으니까.

그리고 그것은 지금까지도 정마대전에 관하여 이야기하는 다른 이들도 마찬가지일 것이다.

그나마 남만이 큰 피해를 입었다고 알려 주기라도 한 것은 적천강을 비롯한 극소수에 불과했다.

‘그러니 다들 묵은 감정이 있었겠지. 얼마 전 있었던 천마표국의 일은 그 발화점이었을 테고.’

종전 직후 무슨 보상을 받았건 간에, 그들에게는 아직까지도 남아 있는 아픈 상처다. 그런데 그 상처가 조금씩 아물고 겨우 딱지가 생길 무렵에 이런 일이 생긴 것이다.

“불과 수십 년 전 우리는 하나가 되어 한족들을 위해 목숨을 바쳐 싸웠는데, 이제는 우리 중 일부를 죽였지.”

차갑게 끓어오른 야율목의 목소리가 귓가를 파고들었다.
```

## Final English reading copy

```markdown
# Chapter 627

The temporary lodging we’d been assigned was decent enough. It wasn’t as lavish or high-class as anything in the Central Plains, but it was clean and more than adequate for me and the Fire Dragon Pavilion members to stay in for the time being.

Of course, that didn’t mean we’d received an unconditional welcome.

“Hmm. Does anyone know what’s stuck to my chopsticks right now?”

At the surprise quiz I posed during the meal, Hyuk Mujin shot his hand into the air.

“Oh, right. Mujin. Answer it.”

“The correct answer is… a bug!”

“Correct. More precisely, it’s a centipede. But why would something like this be in our food?”

“Hmm. Perhaps it’s a custom of the non-Han people of Nanman?”

Namho, an eighty-year veteran of being one of Nanman’s non-Han people, muttered as he picked out something resembling a pine caterpillar.

“This is the first I’ve ever heard of such a custom…”

I could have understood it to some extent if they’d simply roasted locusts and served them to us. But this was on the level of dumping live insects into the food. There was no way even I could defend it.

Sama Pyo let out a sigh as he stared pointedly at Taishan, who was still trying his hardest to bury his face in his plate.

“So it seems we really aren’t welcome.”

There was no way this could be called a meal. Song Ilseom set down his chopsticks and replied calmly.

“It’s probably because of the Heavenly Demon Escort Bureau incident.”

I agreed. But that didn’t mean I thought Yayul Mok had personally ordered this.

Someone important enough to be the Young Palace Lord wouldn’t use such petty methods.

*So this was the work of other non-Han people within the Nanman Beast Palace.*

We’d been hated consistently from the moment we entered Nanman until now. I was just thinking that even the ugly duckling hadn’t been treated this badly when Ju Hwaran quietly appeared.

She had gone upstairs before the meal, saying she was going to wash up.

“Huh? You’re already done?”

How long had it been since she went upstairs? Not even Recruit Number 54 at the Nonsan training center could wash that quickly.

At my questioning tone, Ju Hwaran answered with an ambiguous smile.

“Ah, yes.”

“……”

I had a distinctly bad feeling about this. When I continued staring at her without saying anything, Ju Hwaran hesitated for a moment before speaking.

“Actually, the thing is…”

After hearing the whole story, I couldn’t help letting out a dry laugh.

“They gave you water hot enough to boil in this weather? And they mixed something resembling filth into it?”

Ju Hwaran nodded awkwardly.

“I wasn’t going to tell you. It could have been a simple mistake, but I was worried this might cause trouble…”

“It wasn’t a simple mistake. And don’t worry about it. Even without that, we already have another problem.”

Only then did Ju Hwaran realize what was happening with the meal and gave her brief assessment.

“Ugh.”

“I’m only asking to be sure, but you’re not going to eat that, are you?”

“No. Of course not.”

I had never seen Ju Hwaran answer so decisively before. Clicking my tongue softly, I rose from my seat.

“Captain, where are you going?”

“To make a scene.”

The way of the world was simple: stay still, and people took you for a mat; keep letting them get away with things, and they took you for something to wrap up.

Since we had come here to persuade the Nanman Beast Palace, I would maintain a certain degree of restraint. But I needed to make a proper fuss at least once if I wanted to ensure they never tried this again.

I was about to fling open the door when I suddenly remembered something I’d forgotten and stopped.

“Oh. And one more thing.”

“Yes?”

“Make him stop eating.”

No one asked who I meant by “him.”

There was only one person among us wolfing down his third bowl of colorful insect fried rice. Sama Pyo gazed at Taishan with sorrowful eyes.

“Taishan. Stop…”

Yes. Please stop.

* * *

It was the largest tree I had ever seen.

Its trunk was so massive that dozens of strong men would have needed to stretch out their arms to encircle it, and its lofty height reached at least several dozen jang.

I couldn’t help letting out an inward exclamation when I saw it, but I hadn’t come here to admire the tree. I had come to meet someone.

“Hey. Get down.”

*Rustle.*

The dense leaves shook. Soon, accompanied by the low growl of a beast, Yayul Mok’s displeased voice reached my ears.

“It’s you again. How did you find out about this place?”

“I asked, and someone told me. They said you come here often.”

“Who?”

“The guy who manages the pavilion.”

“Hwang Gae?”

“Maybe it was Hwang Gae or Ddong Gae. Something like that.”

“He isn’t the sort of person who would tell a Han Chinese that.”

“Maybe not a Han Chinese, but he was pretty forthcoming with my fist.”

“……”

“Come down. My neck hurts.”

I didn’t think he would come down simply because I said my neck hurt, so I kindly added one more thing.

“Before I break the tree.”

“This tree was planted by my ancestors’ ancestors. It took root in this land a full thousand years ago.”

“Then, sometime far in the future, your descendants will say, ‘There used to be a thousand-year-old tree here, but some Han Chinese bastard came and ripped it out by the roots.’ And when the child asks, ‘Why, Mom?’ she’ll say, ‘Because our ancestor wouldn’t come down from the tree when asked nicely.’”

“……”

“So get down before I damage the environment.”

I wondered whether I would really have to pull the tree out if he refused again, but Yayul Mok loved nature even more than I’d expected.

*Swish. Tap.*

*Grrrr.*

A white tiger landed smoothly after stepping on branch after branch. It let out a low growl in my direction.

Yayul Mok lightly stroked the white tiger’s neck, then glared at me.

“You’re insane.”

“Come on. Why are you acting surprised?”

I scratched the back of my head bashfully. Yayul Mok’s face flushed red with anger, and he snarled like a wild beast.

“What happened to Hwang Gae?”

“Ah, that guy? All four limbs are intact. He was a little frightened, though.”

“You’re out of your mind. You came here asking for help, yet you’re oppressing the people of Nanman.”

“You seem to have misunderstood. I really didn’t lay a finger on him. I did grab him by the collar, though.”

I wasn’t some neighborhood thug. I had never gone that far even in the Central Plains.

I always started by speaking gently and only used my fists when that failed. And this time, I had more than enough reason.

“Insect fried rice. Bathwater mixed with filth.”

“What?”

“If that isn’t a traditional custom, then the Nanman Beast Palace’s treatment of its guests is pretty terrible. Don’t you think?”

Yayul Mok furrowed his brow and thought for a moment before muttering as if sighing.

“I think I have a general idea of what happened.”

“If you had a general idea, you should have warned them beforehand.”

“I never expected them to show such blatant hostility…”

Yayul Mok was about to continue when he suddenly closed his mouth. Then he dipped his head toward me.

“I’m sorry. I sincerely apologize.”

“……”

“Oh.”

“What’s with that reaction?”

“It’s nothing.”

I was honestly a little surprised. We hadn’t known each other long, but I hadn’t expected someone as proud and rough as Yayul Mok to bow his head so obediently.

*Is he the type who admits his mistakes immediately and doesn’t hold grudges?*

Making a mistake was easy. Admitting it and offering a sincere apology was much harder.

In that sense, the young Young Palace Lord of the Nanman Beast Palace had a better personality than I’d expected.

“I’ll replace the people responsible as soon as I return. Hwang Gae, of course, as well as everyone else involved. Nothing like this will happen again.”

“Well, if you’ll do that…”

“It was my mistake. I apologize once again, so I hope this doesn’t reach my father’s ears.”

“Why? Does he beat you when you make mistakes?”

Yayul Mok answered with an indignant expression.

“What kind of nonsense are you talking about?”

“If not, never mind. You went so far as to ask me not to tell him, so I thought you might get beaten for three days and three nights.”

“My father has never laid a hand on me even once.”

If his father was the Beast Miao King, I supposed it was possible to raise a son without ever touching him.

With that size and that level of martial power, he could probably give not only his son but also his grandson—and perhaps even his great-grandson—a free pass through puberty.

While I was thinking this, Yayul Mok hesitated, then added in a small voice,

“I may be fine, but the others are a different matter. If my father finds out about this, he’ll come down on them like thunder.”

“Ah.”

“He welcomed you as guests. It’s only natural for you Han Chinese to protest after being treated so poorly. But even so, I have no intention of punishing Hwang Gae or the others.”

“Because they were pissed off over that fucking Dick Demon Escort Bureau?”

“……”

“The name seems a little off, but that is one of the reasons.”

“One of the reasons? That makes it sound like there are others.”

Yayul Mok stared at me silently for a while. Then, as he stroked the chin of the now-quiet white tiger, he opened his mouth.

“The Great Faction War.”

“Hmm?”

“We shed far too much blood in the Central Plains. Under my father’s leadership, all of Nanman’s tribes joined forces, and as many as ten thousand warriors went to the battlefield. But the number of those who returned home alive was less than a quarter of that.”

*Grrr.*

The white tiger quietly accepted the hand stroking it, then looked at its master with worried eyes.

Yayul Mok’s voice continued, heavy with complicated emotions.

“Someone’s parents. Someone’s children. Friends and relatives who had grown up together since childhood. Most of them left for the battlefield with smiles on their faces and never returned. Even I, who was born long afterward, wasn’t exempt.”

“You, too?”

“If things had gone as they should have, I wouldn’t have been able to become the Young Palace Lord. That is the real answer to the question you asked earlier.”

Recalling the conversation I’d had with Yayul Mok immediately after he parted from the Beast Miao King, I suddenly realized.

“You had older siblings.”

“Three. One of them was my elder sister. She was young, and she was a woman, but I heard she was as brave as any warrior. If she hadn’t participated in the Great Faction War, she would have married the man she loved. My father and Uncle Baeksang would have become in-laws as well as sworn brothers.”

“Wait. Then…”

“You’re thinking correctly. In the war between the Han Chinese that they named the Great Faction War, my father lost two sons and a daughter, while Uncle Baeksang had to send off a son he cherished like his own life.”

Yayul Mok gave a bitter smile and added,

“Don’t blame Hwang Gae too much. He lost his parents and every last one of his relatives.”

I had nothing to say, so I simply closed my mouth.

I had heard so much about the Great Faction War from one place and another that my ears were practically ringing with it. But I hadn’t known Nanman had suffered losses on this scale.

No. To be more honest, I hadn’t thought I particularly needed to know.

Nanman lay in the Outer Lands, tens of thousands of li from the Central Plains, and I had thought it was a completely separate land with nothing to do with Murim.

The others who talked about the Great Faction War even now were probably the same.

The only people who had even told me that Nanman had suffered heavy losses were Jeok Cheongang and a tiny handful of others.

*So they must have all been carrying old resentment. The Heavenly Demon Escort Bureau incident from recently must have been the flashpoint.*

Whatever compensation they had received right after the war ended, the wound was still there. And just as that wound was beginning to heal and had barely formed a scab, this had happened.

“Only a few decades ago, we united and risked our lives fighting for the Han Chinese. And now, you killed some of us.”

Yayul Mok’s voice, coldly boiling over, pierced my ears.
```

<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0652.txt",
      "sha256": "0ac38c7c3658d3062069bec87aa01b74c068b4892961ccbef1e8ce54323dd8db",
      "bytes": 13279
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "42e2d1df02f8f30d1472db310b78e43cc7fab8e48383bec7e5e0390c86134538",
      "bytes": 1888
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "2816675828363f5aa2eda7b704c7c1f5c45a36cf153542b6fcb89ef04a3628c4",
      "bytes": 199864
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "49d75c79c87f024ab414be52d6a3ec5a376933316e3b1b72aadc2b05a57fd0f9",
      "bytes": 553
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "8013103b43821626f67eb4961c7c2b8dd3d271e5287ced02bd9c84d105c3bd4e",
      "bytes": 1347
    },
    {
      "path": "characters/Jang Sam.md",
      "sha256": "7ed5457f4ae8352154dd584895f21f6e3563c33909938f812df865d106818c47",
      "bytes": 408
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "daaba64e0f9c64bd9ad4fdf747411b0778d623ef80f2d409b909da2c4bc8f59c",
      "bytes": 1936
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "bff47b4aba42d4b5477871cd411e00fd15b00445f1658994e417f8b454ce31ed",
      "bytes": 622
    },
    {
      "path": "characters/Ju Hwaran.md",
      "sha256": "86bc9eae155fa0b2eca10e8030eed1dca2c6bf16d4502a4875af5af31a4a7d0e",
      "bytes": 1131
    },
    {
      "path": "characters/Namho.md",
      "sha256": "92b67678c8247325e1a00943015217cbd90d4faea1aa541084f99af779799251",
      "bytes": 843
    },
    {
      "path": "characters/Sama Pyo.md",
      "sha256": "84d453fbff2c66b65d9b94077cd9e0c12dd9f2730ba87e38666920e63c4e2303",
      "bytes": 899
    },
    {
      "path": "characters/Song Il.md",
      "sha256": "562a0a4fa355ef805543a4027893a1fdbd4998103a20edff050ecc25d99d8876",
      "bytes": 964
    },
    {
      "path": "characters/Song Ilseom.md",
      "sha256": "e07c41d6c276e48c7ee2036a55473c99f03d128ff321a87725fe6603fe1bce5d",
      "bytes": 957
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "930d82eb2618eaac925b6519dd304ef5abe8c526a572f512a6d1637cf27a1b91",
      "bytes": 528
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "88019c0cfd61c3aeb2dd467971aea7a4324db023c59e4689c59c3828ae2f0565",
      "bytes": 205898
    }
  ],
  "estimated_tokens": 13053
}
-->

# Durable State Update — Chapter 652

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 652. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 652. Profile updates may replace only one
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
  "chapter": 652,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 652,
    "continuity_sources": [652],
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
    "Jin remains in the Nanman Beast Palace's Inner Palace as the Third Young Master of the Jin Family of Taiyuan and head of the Fire Dragon Pavilion.",
    "Heugung alleges that Baeksang colluded with Dark Heaven but has no concrete proof.",
    "Heugung has secretly evaded Baeksang's surveillance for more than twenty years, including by learning the Bone-Shrinking Technique.",
    "Heugung claims Baeksang exchanges unexplained monthly missives and disappears alone, monthly since last year.",
    "Heugung's loyal retainers investigated Baeksang's secret refuge twenty years ago, but the refuge was destroyed and the retainers died or vanished.",
    "Heugung genuinely loves Yohi and says she chose wrongly while trying to revive the Yao people.",
    "Heugung offers to testify at the next day's Tribal Grand Council if his and Yohi's safety is guaranteed.",
    "Heugung has staked his life on the truth of his allegations.",
    "Jin has not yet informed the Beast Miao King and intends to consult the Fire Dragon Pavilion first.",
    "Sama Pyo is training outside the quarters when the surrounding grass moves."
  ],
  "continuity_sources": [
    651
  ],
  "open_questions": [
    "Is Baeksang truly colluding with Dark Heaven, and what evidence can Heugung provide?",
    "What happened at Baeksang's secret refuge, and who destroyed it?",
    "Will the Beast Miao King accept Heugung as a witness and guarantee Heugung's and Yohi's safety?",
    "How knowingly did Yohi align herself with Baeksang's side?",
    "Who or what is moving in the grass around Sama Pyo?"
  ],
  "safe_through": 651,
  "temporary_decisions": [
    "Use Insi for 인시.",
    "Use the hour of the Rabbit for 묘시.",
    "Use Bone-Shrinking Technique for 축골공.",
    "Use Tribal Grand Council for 대회의.",
    "Use missive for 전서."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 혁무진    | **Hyuk Mujin**     |
| 송일     | **Song Il**        |
| 주화란    | **Ju Hwaran**      |
| 장삼 | **Jang Sam** | Bandit; personal name |
| 암천     | **Dark Heaven**                  |
| 남만야수궁  | **Nanman Beast Palace**          |
| 삼류     | **Third Rate**    |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 살기     | **killing intent**                               |                                                       |
| 검기     | **Sword Energy**                                 | When functioning as projected weapon qi               |
| 후기지수   | **young prodigy** / **rising martial artist**    | Contextual, not a title                               |
| 정파     | **orthodox faction**                             |                                                       |
| 중원     | **Central Plains**                               |                                                       |
| 전각     | **pavilion**                                 | Use “hall” only when established for a specific named building |
| 상태               | **Status**                     |
| 하남     | **Henan**              |
| 정마대전   | **Great Faction War**         |
| 귀가      | **your family**                                                 |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 남호 | **Namho** | Hidden Shadow Pavilion code name; literally associated with amber from the south. |
| 사마표 | **Sama Pyo** | Young Sect Leader of the Black Dragon Demon Gate. |
| 송일섬 | **Song Ilseom** | Young escort captain of the Yongbong Escort Bureau; distinct from Song Il of Zhongnan. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 순이 | **Sooni** | Former owner of Sooni's Super. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 사마외도 | **demonic, heterodox arts** | Suspected martial-arts origin of Pung Yang's insidious forms. |
| 송이 | **Song-i** | Short form used for Song Song; Taekyung's love interest. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 천면호리 | **Thousand-Faced Fox** | Epithet of Song Ho. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 은영각 | **Hidden Shadow Pavilion** | Former Murim Alliance intelligence organization. |
| 화란 | **Hwaran** | Familiar short form of Ju Hwaran. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 비도 | **throwing blade** | Mungyeong throws one past Taekyung's neck. |
| 암기 | **hidden weapon** | Term used in Mungyeong's promise not to throw one. |
| 흑룡도 | **Black Dragon Saber** | Sama Pyo's sobriquet. |
| 내궁 | **Inner Palace** | The inner compound of the Nanman Beast Palace. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 송일 | 진태경 | hostile Zhongnan Elder to accused outsider | you / Jin Taekyung | hostile and threatening | Song Il questions Taekyung's identity and later threatens him over Gong Ilhyuk's injury. |
| 송일섬 | 주화란 | escort_captain_to_young_bureau_head | Hwaran | urgent and familiar | Calls out 화란아 while urgently warning Ju Hwaran before stepping into the confrontation. |
| 주화란 | 진태경 | escort_bureau_leader_to_famous_younger_martial_artist | Young Hero Jin | formal-deferential | Hwaran introduces herself as the Young Bureau Head and formally greets Taekyung as 진 소협. |
| 진태경 | 주화란 | visitor_to_young_bureau_head | Young Lady Ju | formal-polite | Taekyung uses 주 소저 while announcing that his party must leave. |
| 주화란 | 혁무진 | rescued_survivor_to_benefactor | Benefactor | formal-deferential | Hwaran includes Mujin among the Benefactors when greeting Taekyung's companions. |
| 주화란 | 송일섬 | bureau_head_to_escort_captain | Captain Song | formal and prosecutorial | Uses his office title, then his personal name, while exposing and confronting him. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 주화란 | 사마표 | former_fiancés | Young Sect Leader | formal and guarded | Hwaran formally greets her former fiancé. |
| 사마표 | 태산 | Young Sect Leader to subordinate | Taishan | informal and patronizing | Sama Pyo calls Taishan by name while ordering him to leave. |
| 태산 | 사마표 | subordinate to Young Sect Leader | Lord | crude and deferential | Taishan uses 주군 while obeying Sama Pyo. |
| 태산 | 진태경 | subordinate_to_respected_outsider | Jin Taekyung | clipped and familiar | Taishan says he likes Jin Taekyung but will fight him without hesitation if Sama Pyo commands it. |
| 사마표 | 진태경 | prospective recruit to pavilion master | you | polite, controlled, and candid | Sama Pyo uses 자네 while asking about Taekyung's attitude and admitting his intention to use him. |
| 진태경 | 사마표 | pavilion master to prospective recruit | you / that guy | blunt, informal, and distrustful | Taekyung speaks to and about Sama Pyo with casual forms such as 녀석 and 저놈. |
| 진태경 | 송일섬 | pavilion master to prospective member | Song Ilseom | direct and evaluative | Taekyung directly names Song Ilseom while comparing his qualifications with Hwaran's. |
| 혁무진 | 송일섬 | pavilion_member_to_escort_captain | Great Hero Song | formal and deferential | Mujin addresses Song Ilseom while commenting on his broad experience. |
| 송일섬 | 사마표 | fellow_pavilion_member_to_hostile_fellow_member | you | hostile and casual | Song Ilseom discusses fighting Sama Pyo and answers him while preparing to move away. |
| 사마표 | 송일섬 | fellow_pavilion_member_to_hostile_fellow_member | you | controlled and antagonistic | Sama Pyo responds to Song Ilseom's accusations and proposes moving aside to fight. |
| 혁무진 | 태산 | pavilion_member_to_pavilion_member | you / hey | casual and coaxing | Hyuk Mujin calls after Taishan and offers jerky to persuade him to travel together. |
| 태산 | 혁무진 | pavilion_member_to_pavilion_member | you | clipped and dismissive | Taishan tells Hyuk Mujin not to follow, then accepts him as a friend after hearing about the jerky. |
| 남호 | 진태경 | Hidden_Shadow_Pavilion_agent_to_mission_leader | Jin Taekyung / you | guarded and familiar | Namho addresses Taekyung as 자네 while explaining the contact and offering guidance. |
| 진태경 | 남호 | mission_leader_to_hidden_shadow_agent | you / Namho | probing and respectful | Taekyung questions Namho’s affiliation and later discusses Dark Heaven’s threat to Nanman. |
| 남호 | 혁무진 | hidden_shadow_agent_to_pavilion_member | you there / Han bastard | performatively hostile and abusive | Namho attacks Mujin and insults him to make the meeting appear to be a genuine expulsion. |
| 혁무진 | 남호 | pavilion_member_to_hidden_shadow_agent | old man | indignant and insulting | Mujin protests Namho’s staged attack and objects to the insult about his parents. |
| 주화란 | 남호 | pavilion_member_to_hidden_shadow_agent | you / Elder Namho | formal and appreciative | Hwaran respectfully praises the effort Namho invested in mapping Nanman. |
| 남호 | 태산 | guide_to_pavilion_member | Taishan | blunt and exasperated | Namho directly rebukes Taishan for eating the poisonous blood-feeding fungus. |
| 남호 | 사마표 | guide_to_young_sect_leader | Young Sect Leader | blunt and admonishing | Namho warns Sama Pyo that all grass and animals in the territory belong to the Nanman Beast Palace. |
| 남호 | 주화란 | guide_to_escort_bureau_head | Escort King's granddaughter | approving and familiar | Namho praises Hwaran for recalling Ju Gongsan's records about Nanman. |
| 사마표 | 남호 | young_sect_leader_to_guide | Elder Namho | formal and apologetic | Sama Pyo apologizes after Taishan attempts to seize the calf. |
| 진태경 | 태산 | pavilion_master_to_pavilion_member | Taishan | forceful and commanding | Taekyung orders Taishan to stop eating the bear. |
| 태산 | 주화란 | Pavilion member to Pavilion member | Young Lady Ju | clipped, childlike, and deferential | Agrees with Ju Hwaran after she mentions the evening banquet. |
| 태산 | 남호 | Fire Dragon Pavilion member to guide | Namho | clipped, childlike, and informal | Taishan directly addresses Namho while asking what Dark Heaven is. |
| 남호 | 각주 | guide to pavilion master | Pavilion Master | blunt, hostile, and abusive | Namho addresses Jin as 각주 while accusing him of causing the disturbance. |
| 사마표 | 각주 | Fire Dragon Pavilion member to pavilion master | Pavilion Master | formal but sardonic | Sama Pyo addresses Jin as 각주 while questioning his account of the incident. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 651
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 647
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and a member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son; he uses quiet practices such as fishing to empty his mind. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad; as a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Fire Dragon Pavilion members accompanying Taekyung. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jang Sam.md

# Jang Sam (장삼)

- **Safe through:** Chapter 641
- **Aliases:** Killing Ghost
- **Role:** Jang Sam was a Hubei fisherman who disappeared for a month and reappeared as a grotesque mutant monster known as a Killing Ghost.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** No relationships established.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 647
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple, the Fire Gate Clan's nineteenth successor, and the Pavilion Master of the Fire Dragon Pavilion within the Murim Alliance; he is a Supreme Peak master with the Heavenly Martial Physique and Force, publicly recognized as an S-rank-level Hunter while formally retaining an A-rank license, and he has completed an unnamed cultivation technique designed for even the lowest-rank Hunter to learn without making it easily abusable.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 647
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Ju Hwaran.md

# Ju Hwaran (주화란)

- **Safe through:** Chapter 649
- **Aliases:** Hwaran
- **Role:** Ju Hwaran is a Level 88 Young Bureau Head, leader of the Yongbong Escort Bureau, a member of the Fire Dragon Pavilion, an experienced Nanman escort guide with route knowledge from the Escort King's records, someone who can understand the Miao and Bai languages, and a volunteer accepted for the scouting mission to investigate the Blood Monk in Guizhou.
- **Personality:** Intelligent, capable, responsible, filial, composed under pressure, and burdened by intense guilt over the escort journey's deaths.
- **Voice:** Clear, polite, restrained, and determined.
- **Relationships:** Escort King Ju Gongsan was her paternal grandfather, Ju Hogun is her father, Heo Jun was her uncle, Sama Pyo was her former fiancé in a political engagement she accepted for her father's sake, Song Ilseom is her direct escort who accompanied her previous journey to Yeongin, and Jin Taekyung is a trusted ally; the Yongbong Escort Bureau has longstanding ties with Yeongin’s inhabitants.

### Namho.md

# Namho (남호)

- **Safe through:** Chapter 650
- **Aliases:** Elder Chao
- **Role:** Namho is an eighty-year-old non-Han Hidden Shadow Pavilion agent who spent more than fifty years operating under the cover of the Poison Flower Pavilion in Nanman and now serves as the Fire Dragon Pavilion’s guide.
- **Personality:** Duty-bound, pragmatic, observant, and willing to use theatrical violence and crude insults to protect an intelligence operation.
- **Voice:** Measured and serious in private, but loudly abusive and convincing when maintaining his local cover.
- **Relationships:** Namho is a Hidden Shadow Pavilion contact for Jin Taekyung and the Fire Dragon Pavilion, receives intelligence from the Pavilion Master, and knows the code used by the Thousand-Faced Fox.

### Sama Pyo.md

# Sama Pyo (사마표)

- **Safe through:** Chapter 651
- **Aliases:** Black Dragon Saber
- **Role:** Young Sect Leader of the Black Dragon Demon Gate, a Morning Star reputed to be no less than the Ten Dragons and Phoenixes, and a member of the Fire Dragon Pavilion.
- **Personality:** Outwardly courteous and smiling, inwardly calculating, but genuinely protective of Taishan and willing to redirect blame onto his subordinate.
- **Voice:** Polite and ingratiating in public, with sardonic humor and controlled evasiveness.
- **Relationships:** Sama Pyo commands the absolutely loyal Taishan, is Sima Gong's son, was Ju Hwaran's former fiancé in a political engagement, and has joined the Fire Dragon Pavilion while openly intending to use Jin Taekyung as a useful card; he is now openly hostile toward fellow member Song Ilseom.

### Song Il.md

# Song Il (송일)

- **Safe through:** Chapter 647
- **Aliases:** Roaring Fury Swordsman
- **Role:** Elder of the Zhongnan Sect and the Roaring Fury Swordsman; senior brother of Sect Leader Gong Iljung; came to the Jin Family of Taiyuan to demand redress for Gong Ilhyuk's injury and the alleged insult to Zhongnan; attacked Jin Taekyung with the Heavenly River Thirty-Six Swords, was stopped by Jeok Cheongang, and was publicly humiliated by him.
- **Personality:** Arrogant, domineering, punitive, and confident in his martial power and seniority.
- **Voice:** Gruff, cutting, condescending, and threatening, with formal authority used to pressure those beneath him.
- **Relationships:** Gong Iljung is his junior Sect Leader and martial younger brother; Gong Ilhyuk is a junior Disciple of his sect; he recognizes Baek Museong and Cheongpung through their Huashan and Sword Saint connections.

### Song Ilseom.md

# Song Ilseom (송일섬)

- **Safe through:** Chapter 647
- **Aliases:** Escort Captain Song
- **Role:** Level 110 young escort captain of the Yongbong Escort Bureau, one of its Dragon-Phoenix Three Escorts, and a newly accepted member of Jin Taekyung and Cheongpung’s Fire Dragon Pavilion.
- **Personality:** Blunt, decisive, survival-hardened, and dryly self-aware, with little patience for insults or disorder and practical survival skills such as making disguise masks.
- **Voice:** Forceful and urgent in command, with a rough and confrontational edge.
- **Relationships:** He serves under Ju Hwaran and has expressed concern that she not be hurt or die needlessly; he is Song Pyosan’s son, his grandmother was the surviving Guangdong Chen child rescued by Ju Gongsan during the Great Faction War, and he remains openly hostile toward fellow Fire Dragon Pavilion member Sama Pyo.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 650
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord.

## Korean source

```text
＃652화



파스슥.

사마표는 알고 있었다. 지금 저 무성한 풀숲을 뒤흔드는 것은 그저 스쳐 지나가는 바람이 아니라는 것을.

족히 수십에 달하는 적들의 살기(殺氣)가 보이지 않는 칼날처럼 그를 향하고 있었다.

“청하지도 않았는데 찾아오고. 묻는데 대답도 안 하고…….”

불청객도 이런 불청객이 없다.

작게 혀를 찬 사마표는 자신의 독문병기인 흑룡도(黑龍刀)를 늘어트리며 입을 열었다.

“나와라. 얼굴이나 마주 보고 얘기하지.”

그리고 대답 대신 돌아온 것은 십여 자루의 비도였다.

쐐애액! 캉!

번개처럼 흑룡도를 휘둘러 비도를 쳐낸 사마표가 부드럽게 신형을 회전시킨다.

동시에 묵빛 도신을 휘감은 도기(刀氣)가 광풍이 되어 풀숲을 가르고 베었다.

쉬쉬쉬쉭! 서걱!

수백 개의 잎사귀가 조각조각으로 나뉘어 흩날렸고, 커다란 아름드리나무의 몸통에 희미한 실선이 그어졌다.

스륵, 쿠웅!

미끄러지듯 쓰러지는 거목. 사마표는 쓰러진 나무를 넘으며 공터로 다가오는 인영들을 응시했다.

동서남북. 전각을 중심으로 사방을 포위하듯 서서히 움직이는 삼십여 명의 적들은, 하나같이 검은 복면으로 얼굴을 가리고 있었다.

“얼굴 한번 보는 것도 힘들군. 허락도 안 받고 찾아왔으면 복면이라도 걷고 사과하는 게 예의이긴 한데…… 아무래도 그럴 것 같지는 않고.”

사마표는 침착하게 상황을 받아들였다.

야심한 시각에 복면을 쓰고 온 불청객들. 비도로 인사를 대신하는 것을 보면 놈들의 목적은 터무니없을 정도로 명확하다.

더군다나…….

‘하필이면 그가 없을 때 이런 일이 벌어지다니.’

삼류 왈패처럼 입이 지저분하고, 틈만 나면 누군가를 쥐어박아야 하는 손버릇을 가진 각주 놈이 문득 떠오른다.

‘진태경.’

도무지 종잡을 수 없어 사고만 치고 다니는 종자지만, 그래도 이런 상황에서는 누구보다 믿을 수 있는 인간이기도 했다.

고작 스물두 살의 나이로 천하 무림에 족적을 남긴 괴물이었으니까.

하지만 우연인지 필연인지. 지금 진태경은 자리를 비운 상태였고, 만약 남아 있었다면 큰 힘이 되었을 송일섬과 주화란. 비록 그들에게는 못 미쳐도 최소 일 인분 정도는 하는 혁무진도 없었다.

현재 남아 있는 것은 자신과 일찌감치 잠들어 버린 태산. 그리고 전력으로 칠 수도 없는 평범한 늙은이인 남호뿐.

반면 적들의 머릿수는 서른에 육박한다.

‘아니, 숫자가 문제가 아니지.’

내심 중얼거린 사마표는 빠르게 주위를 훑었다. 그물망처럼 서서히 옥죄어 오는 적들이 내뿜는 살기는, 어설픈 무림인의 그것이 아니었다.

‘중원으로 치자면 하나하나가 초일류에서 절정. 도대체 남만 어디에서 이런 놈들이 나타난 거지?’

중원 무림은 실로 광대하나, 백사장의 모래알처럼 수많은 무림인들 중에서도 절정 고수는 그리 흔히 찾아볼 수 있는 존재가 아니었다.

그런데 중원에 비할 수 없는 남만에서, 그것도 이 정도 수준의 전사들을 서른이나 동원해서 습격을 해 오다니.

다행히 그리 높은 수준은 아니었지만, 사마표가 적잖이 놀라는 것도 이상한 일은 아니었다.

더군다나 이곳은 한참 떨어진 외곽이라고는 해도 분명 남만야수궁의 내궁(內宮)에 속한 영역이었으니까.

“누구냐, 너희는.”

쐐애애액! 콰득!

물음에 대한 답 대신, 아슬아슬하게 목을 스쳐 지나간 단창(短槍)이 전각의 문을 박살 냈다.

그리고 그것이 전투의 시작을 알리는 신호탄이었다.

파파팟!

희미한 달빛을 가리며 날아드는 암기와 화살. 그리고 빛살처럼 쇄도하는 그림자들.

동시에 사마표의 손에 들린 흑룡도가 바람을 가르며 움직였다.

쉬이이잉! 서걱!

강맹한 도기가 허공을 격하고 암기와 화살을 휩쓸었다. 단숨에 화망(火網)을 파훼한 사마표를 향해 좌우로 칼날이 짓쳐 들었다.

쉬익!

급소를 노림에 있어 한 치의 망설임도 없는 손속. 절묘하게 맞아떨어지는 합격술(合擊術).

아마 사마표가 별다를 것 없는 절정 고수였다면 이 공격으로 큰 상처를 입었거나, 혹은 목숨을 잃었을 것이다.

하지만 사마표는 달랐다.

그는 실전 경험이 부족한 애송이 후기지수가 아니었고, 정파의 절정 고수처럼 고리타분하지도 않았다.

사마외도(邪魔外道)의 가장 큰 가치는, 바로 생존이다.

달칵, 퍼걱!

둔탁한 소음과 함께, 사마표의 좌우를 노리고 달려들던 두 명의 절정 고수가 썩은 고목처럼 허물어졌다.

복면 위로 드러난 눈은 크게 뜨여 있었고, 미간 사이에는 한 뼘 길이의 작은 화살이 깊숙이 틀어박혀 있었다.

‘성공이군.’

사마표가 이 무더운 날씨에도 단출한 무복 대신 얇은 장삼을 걸친 이유는 간단했다. 풍성한 소매 안에 암기를 숨길 수 있으니까.

정해진 각도로 손목을 비틀면 장전된 화살이 발사되는 이 기관장치의 원리는 간단했지만, 예상치 못한 상황에서는 어떤 것보다 치명적이었다.

“병신들.”

씹어뱉듯 중얼거린 사마표는 쓰러지려는 두 시신을 끌어당겨 앞뒤로 세웠다.

푸푸푹!

부지불식 간에 날아온 암기가 조금 전만 하더라도 아군이었던 시신을 벌집으로 만들었고, 사마표는 방패로 삼은 시신의 옆구리 사이로 소매를 겨누었다.

달칵, 푸푹!

하지만 이제는 적들도 상황을 인지하고 있었다.

애당초 노렸던 미간 대신 팔뚝에 박힌 화살. 이미 두 번이나 보여 주었으니 다음부터는 통하지 않을 것이다.

‘그렇다면.’

투둑.

사마표의 판단은 신속했다.

소매에 숨겨 둔 기관장치를 해제한 그는 기합과 같은 외침을 내지르며 적들을 향해 쇄도했다.

“태산!”

쉬쉬쉭!

스물일곱으로 줄어든 복면인들이 이리처럼 사마표를 에워쌌다.



* * *



쾅!

한참을 뒤척이다가 겨우 잠에 들었던 남호는 눈을 뜨자마자 생각했다.

‘어떤 호로 새끼일까.’

늙어서 안 좋은 점은 헤아릴 수 없이 많지만, 그중에서도 특히 서러운 것은 밤잠이 줄어든다는 거다.

그런데 감히 팔순 노인의 단잠을 방해하다니. 관절이 삐걱거리는 몸을 일으키며 남호는 굳게 다짐했다.

‘만약에 태산, 그 아귀 같은 놈이 야식을 처먹느라 내 잠을 깨웠다면…… 내 이번에는 절대 쉽게 넘어가지 않으리라.’

이래 보여도 은영각 짬밥만 오십 년이다.

정마대전 때 몸과 마음을 갈아 가며 헌신했으니, 하남에 서신을 보내서 태산을 무림 공적으로 만들어도 천면호리가 한 번쯤은 눈감아 줄 것 같았다.

‘놈이 암천의 끄나풀이라고 하면 믿어 줄까?’

하지만 남호의 그런 고민은 얼마 지나지 않아 물거품처럼 사라졌다. 창밖에서 들려오는 요란한 소리 때문이었다.

“태산!”

쉬쉬쉭! 캉!

차차차창!

창가에서 멍하니 공터를 내려다보던 남호는, 잠시 헛것을 보나 싶어 눈을 비볐다.

하지만 눈앞에서 벌어지는 일은 꿈이 아니라 틀림없는 현실이었고, 사마표가 피해 낸 누군가의 검기는 남호가 서 있는 창가를 훑고 지나갔다.

서걱! 쿠궁!

그리고 남호는 마침내 상황을 깨달았다.

‘습격!’

그것도 철저히 계획된 습격이다. 그 미친놈, 아니 진태경이 자리를 비웠을 때 쳐들어온 것만 해도 알 수 있었다.

‘이런 개 같은 상황을 봤나. 도대체 누가……!’

이제 잠에서 깼다는 불쾌함은 남호에게 있어 아무런 문제도 되지 못했다. 잠시 후면 잠이 아니라 목이 달아날 판국이니까.

사마표가 생각하는 것 이상으로 잘 싸우고 있었지만, 이대로라면 중과부적(衆寡不敵)으로 쓰러질 것이 분명했다.

게다가.

파파팟!

사마표를 놔둔 채 전각으로 접근하는 일부 복면인들을 확인하자 더 이상 망설일 틈조차 없었다.

“으헉!”

질겁한 남호는 팔순이라는 나이가 무색할 만큼 빠른 속도로 방을 벗어났다.

그리고 곧장 보이는 복도 끝을 가로질러 굳게 닫힌 문을 열어젖혔다.

벌컥!

“기습! 기습이다! 지금 밖에 네 주군이……!”

그리고 방의 주인, 태산이 우렁차게 대답했다.

“커어어어억. 쿠우우우우!”

“야, 이 개호로 같은 놈아!”

“쿠허어어어억!”

남호는 도저히 믿을 수 없었다.

‘이런 상황에서도 잠을 잘 수 있다니. 이놈이 진정 사람 새끼란 말인가!’

전각 곳곳이 부서지고, 병장기가 부딪치는 소리가 하남까지 들릴 지경이다.

그런데 정작 전각 안에서 코까지 골면서 잘 수 있다는 것이 믿어지지 않았다.

“노옴! 어서 일어나지 못하겠느냐!”

퍽! 퍽퍽!

영혼을 쥐어 짜내는 외침과 함께 흐르는 세월에 힘을 잃은 주먹이 태산의 턱주가리를 후려쳤다.

그리고 그런 남호의 정성에 하늘이 감동한 듯, 태산이 마침내 몸을 뒤척이며 반응했다.

“으응. 태산이.”

“그래! 어서 일어나거라! 어서!”

“으으응. 모기 싫다. 저리 가라…….”

“이 개애새끼야!”

흡사 통곡과도 같은 외침.

이제 남호가 눈물마저 글썽이고 있던 그때, 활짝 열린 창으로 흘러든 달빛에 누군가의 검은 그림자가 드리워졌다.

“……!”

남호의 몸이 덜컥 굳었다. 천천히 고개를 돌리자, 어느새 전각으로 침투한 복면인 셋이 그의 회색빛 눈동자에 비쳤다.

‘저, 저놈들은.’

흡사 유령 같은 움직임.

동시에 복면인들의 손에 들린 병장기가 달빛을 받아 새하얗게 빛난 그 순간, 장장 팔십여 년에 달하는 방대한 분량의 주마등을 겪은 남호는 태산을 깨울 수 있는 유일한 방법을 깨달았다.

“태산! 네 이놈!”

스윽.

외침과 함께 복면인들의 병장기가 들어 올려졌다. 죽음을 떠올린 남호가 질끈 눈을 감으며 외침을 이었다.

“이놈들이 네 고기 다 뺏어 먹는다!”

그리고 다음 순간.

“안 돼! 태산이 고기!”

마법처럼 눈을 부릅뜬 태산이 복면인들을 향해 일권(一拳)을 뻗었다.

뻐억! 콰과과광!



* * *



후우욱. 훅.

사마표는 거친 호흡을 가다듬었다. 상반신이 피에 흠뻑 젖은 그를 주시하는 복면인들의 시선은 처음과 달리 은은한 두려움이 배어 있었다.

그만큼 사마표의 분전은 그들이 생각했던 것 이상으로 거칠고, 치열했으며 잔혹했다.

전신에 숨겨 둔 온갖 암기와 독, 게다가 오직 살생을 위한 실전성을 기반으로 한 무공까지.

하지만 더욱 무서운 것은 죽음을 두려워하지 않는 그의 태도였다.

“누구든 와라. 맹세컨대 내 전부를 걸고 죽여 주마.”

거친 호흡을 내뱉으면서 피칠갑을 한 채 덤벼드는 사마표의 손에 복면인들은 하나둘씩 쓰러졌다.

어느덧 스물에 달하는 시신이 땅바닥에 널브러져 있었고, 그들 중 일곱은 중원 어디에서도 인정받을 수 있는 절정 고수였다.

‘이런 괴물 같은 놈.’

그리고 복면인들이 동시에 같은 생각을 떠올린 그 순간.

“안 돼! 태산이 고기!”

우지직! 콰과과광!

무너지는 전각 속에서 진짜 괴물이 나타났다. 팔 척에 달하는 미친 신장과 엄청난 떡대. 그리고…….

“태산이 고기! 고기 어디 있나!”

이 세상의 것이 아닌 것 같은 광기.

꿀꺽.

저놈은 또 뭐지?

복면인들이 마른침을 삼키던 그때, 괴물의 등 뒤에서 자그마한 노인이 고개를 쏙 내밀더니 손가락으로 그들을 가리켰다.

“저놈들 보이지?”

“태산이! 보인다!”

“내가 아까 다 봤는데, 저놈들이 네놈 고기를 다 훔쳐 먹었다.”

“태산이이이이! 용서할 수 없다!!”

도대체 고기는 뭐고, 훔쳐 먹은 건 뭐란 말인가.

당황한 복면인들이 주춤거리는 모습에 사마표가 피에 젖은 이빨을 드러내며 웃었다.

하지만 그가 바라보는 곳은 태산이 아닌, 공터를 훤히 내려다볼 수 있는 언덕 위였다.

아니, 정확히는 언덕을 털레털레 내려오는 누군가였다.

“잠깐 자리를 비우면서도 혹시나 했는데.”

저벅저벅.

느긋하게 걸어온 청년, 진태경이 사마표에게 물었다.

“혹시 네 친구들이냐?”

사마표는 크게 웃으며 고개를 저었다.
```

## Final English reading copy

```markdown
# Chapter 652

Rustle.

Sama Pyo knew that what was shaking the dense grass was not merely a passing breeze.

The killing intent of dozens of enemies was aimed at him like invisible blades.

“They come without being invited. And when I ask them something, they don’t even answer…”

There were no more unwelcome guests than these.

Clicking his tongue softly, Sama Pyo lowered his Black Dragon Saber, his personal weapon, and spoke.

“Come out. Let’s talk face-to-face.”

The answer that came instead was a volley of a dozen or so throwing blades.

Whoosh! Clang!

Sama Pyo swung the Black Dragon Saber like lightning and knocked the blades aside, smoothly twisting his body.

At the same time, the saber energy coiling around the dark blade became a gale that tore through the grass.

Sh-sh-sh-shk! Slash!

Hundreds of leaves were sliced into pieces and scattered through the air, while a faint line was carved across the trunk of a massive tree.

Sss, crash!

The giant tree slid to the ground. Sama Pyo vaulted over it and stared at the figures approaching the clearing.

East, west, north, and south. The roughly thirty enemies slowly moved into position, surrounding the pavilion from every direction.

Every one of them concealed their face behind a black mask.

“Getting a look at your faces is difficult. If you came here without permission, common courtesy would dictate that you at least remove your masks and apologize… but I suppose that’s not going to happen.”

Sama Pyo calmly accepted the situation.

Unwelcome guests arriving in masks at this late hour. The fact that they had greeted him with throwing blades made their purpose absurdly clear.

Moreover…

*Of all times, this had to happen while he was away.*

He suddenly thought of that Pavilion Master bastard, whose mouth was filthy as a Third Rate thug and whose hands itched to punch someone whenever he got the chance.

*Jin Taekyung.*

He was impossible to predict and constantly caused trouble, but in a situation like this, he was also more reliable than anyone.

After all, he was a monster who had left his mark on the Murim at the age of only twenty-two.

But whether by coincidence or fate, Jin Taekyung was currently away. Song Ilseom and Ju Hwaran, who would have been a great help if they had remained, were absent as well. Hyuk Mujin was gone, too—although he might not have been able to match them, he was at least worth one person.

Those who remained were Sama Pyo himself, Taishan, who had gone to sleep early, and Namho, an ordinary old man who could not even be counted as fighting strength.

Meanwhile, the enemies numbered nearly thirty.

*No, the numbers aren’t the problem.*

Sama Pyo muttered inwardly and quickly swept his gaze across the surroundings. The killing intent radiating from the enemies slowly tightening around him like a net was not that of some clumsy martial artists.

*By Central Plains standards, every one of them is between upper First Rate and Peak. Where in Nanman did these people come from?*

The Central Plains Murim was truly vast, but even among the countless martial artists scattered across it like grains of sand on a beach, Peak masters were not common.

Yet in Nanman, which could not compare to the Central Plains in size or population, someone had mobilized thirty warriors of this caliber to launch an attack.

Fortunately, they were not at an especially high level, but it was hardly strange that Sama Pyo found their appearance surprising.

Especially since this area, despite being far from the center, still clearly belonged to the Inner Palace of the Nanman Beast Palace.

“Who are you?”

Whoosh! Crack!

Instead of an answer, a short spear skimmed dangerously past his neck and smashed through the pavilion door.

That was the signal that began the battle.

Papapat!

Hidden weapons and arrows flew through the air, blocking out the faint moonlight. Shadows rushed forward like rays of light.

At the same time, the Black Dragon Saber in Sama Pyo’s hand moved, cleaving through the wind.

Whiiiiing! Slash!

Powerful saber energy split the air and swept away the hidden weapons and arrows. The instant Sama Pyo broke through the net of projectiles, blades came slashing in from both sides.

Whoosh!

The attackers’ hands showed not the slightest hesitation as they aimed for his vitals. Their coordinated attack was exquisitely timed.

If Sama Pyo had been an ordinary Peak master, this attack would have inflicted a serious wound—or taken his life.

But Sama Pyo was different.

He was not a young prodigy lacking real combat experience, nor was he as rigid as a Peak master from an orthodox faction.

The greatest value of demonic, heterodox arts was survival.

Click, crunch!

With a dull sound, the two Peak masters who had charged in from either side collapsed like rotten trees.

Their eyes were wide behind their masks, and a small arrow a span long was buried deep between their brows.

*It worked.*

There was a simple reason Sama Pyo had worn a thin robe instead of the lighter martial uniform suited to such hot weather.

It allowed him to hide hidden weapons inside its voluminous sleeves.

The principle behind the mechanical device was simple. A loaded arrow was fired when he twisted his wrist at a predetermined angle. But in an unexpected situation, it was more lethal than anything else.

“Idiots.”

Sama Pyo spat the word out, then pulled the two collapsing bodies toward him and propped one in front of himself and the other behind him.

Thud-thud-thud!

The hidden weapons that flew from nowhere turned the bodies of men who had been allies only moments earlier into pincushions. Using them as shields, Sama Pyo aimed his sleeve through the gap beside one corpse’s ribs.

Click, thud!

But the enemies had recognized what was happening by then.

Instead of striking the space between the brows he had originally targeted, the arrow embedded itself in a forearm. He had already shown the trick twice. It would not work again.

*In that case…*

Snap.

Sama Pyo made his decision swiftly.

He disengaged the mechanical device hidden in his sleeve, let out a shout like a battle cry, and charged toward the enemies.

“Taishan!”

Sh-sh-sh-shk!

The masked men, reduced to twenty-seven, surrounded Sama Pyo like wolves.

* * *

Bang!

Namho had tossed and turned for a long time before finally falling asleep. The instant he opened his eyes, he thought:

*What fucking bastard is this?*

There were countless disadvantages to growing old, but the most miserable of them was that one’s sleep became shorter.

And yet someone had dared to disturb the sound sleep of an eighty-year-old man. As Namho pushed himself upright, his joints creaking, he made a firm resolve.

*If that gluttonous bastard Taishan woke me up because he was eating a midnight snack… this time, I absolutely will not let it slide.*

Even if it did not look that way, he had fifty years of experience in the Hidden Shadow Pavilion.

He had devoted himself body and soul during the Great Faction War. Even if he sent a letter to Henan and had Taishan declared an enemy of the Murim, he thought the Thousand-Faced Fox might overlook it just this once.

*Would he believe me if I said the bastard was a Dark Heaven spy?*

But Namho’s worries soon vanished like a bubble. The reason was the uproar coming from outside the window.

“Taishan!”

Sh-sh-sh-shk! Clang!

Cha-cha-cha-chang!

Namho had been staring blankly down at the clearing from the window when he rubbed his eyes, wondering for a moment if he was seeing things.

But what was happening before him was not a dream. It was unmistakably real, and the Sword Energy of someone whose attack Sama Pyo had evaded swept past the window where Namho stood.

Slash! Crash!

Namho finally understood the situation.

*An ambush!*

And not just any ambush. This was a thoroughly planned attack. The fact that they had struck while that madman—no, while Jin Taekyung—was away made that obvious.

*What the hell is this? Who in the world…!*

The unpleasantness of being woken up was no longer a problem for Namho. Soon, it would not be his sleep but his head that was in danger of being lost.

Sama Pyo was fighting better than Namho had expected, but if this continued, it was obvious that he would eventually fall beneath the overwhelming numbers.

And then—

Papapat!

When Namho spotted several masked men approaching the pavilion while leaving Sama Pyo behind, he no longer had even a moment to hesitate.

“Gah!”

Terrified, Namho dashed from the room with a speed that belied his eighty years.

He raced across the corridor at the end of the room and threw open the tightly shut door.

Bang!

“Ambush! It’s an ambush! Your master is outside right now—!”

The owner of the room, Taishan, answered in a booming voice.

“Grrrrrrrk. Hooooooonk!”

“You damn piece of shit!”

“Guh-hoooooonk!”

Namho could not believe it.

*He can sleep through even this? Is this thing really human?*

Parts of the pavilion were collapsing, and the noise of clashing weapons was loud enough to be heard all the way to Henan.

And yet Taishan was actually sleeping inside the pavilion, snoring loudly.

“Wake up, you bastard! Get up at once!”

Thud! Thud-thud!

With a soul-rending cry, Namho’s fist—its strength diminished by the passing years—slammed into Taishan’s jaw.

As if the heavens had been moved by Namho’s devotion, Taishan finally tossed and turned.

“Umm. Taishan.”

“Yes! Now get up! Quickly!”

“Mmmm. Taishan doesn’t like mosquitoes. Go away…”

“You son of a bitch!”

The cry that came from Namho was almost a wail.

Just as tears were beginning to glimmer in his eyes, the moonlight streaming through the wide-open window cast a black shadow across the floor.

“…”

Namho’s body went rigid.

He slowly turned his head. Three masked men who had already infiltrated the pavilion appeared in his gray eyes.

*Those, those bastards…*

Their movements were almost ghostlike.

At that moment, the weapons in the masked men’s hands caught the moonlight and gleamed white. Namho, who experienced a sweeping panorama of his eighty-odd years, realized the only way to wake Taishan.

“Taishan! You bastard!”

Sss.

The masked men raised their weapons as Namho shouted. Thinking of death, Namho squeezed his eyes shut and continued yelling.

“They’re going to eat all your meat!”

And in the next moment—

“No! Taishan’s meat!”

Taishan’s eyes flew open as if by magic, and he thrust one fist toward the masked men.

Wham! Krrrra-boom!

* * *

Hoo. Hah.

Sama Pyo steadied his ragged breathing.

His upper body was drenched in blood, and the gazes of the masked men watching him now contained a faint trace of fear.

Sama Pyo’s desperate struggle had been harsher, fiercer, and more brutal than they had imagined.

Hidden weapons and poison concealed throughout his body, along with martial arts built entirely around practical combat for the purpose of killing.

But even more frightening was that he showed no fear of death.

“Come, whoever you are. I swear I’ll stake everything I have and kill you.”

As Sama Pyo charged at them, panting heavily and drenched in blood, the masked men fell one after another beneath his hands.

By then, twenty bodies lay scattered across the ground. Seven of them had been Peak masters recognized anywhere in the Central Plains.

*What kind of monster is this?*

At the moment the masked men all reached the same conclusion—

“No! Taishan’s meat!”

Crack! Krrrra-boom!

A true monster emerged from the collapsing pavilion.

A madly enormous body standing nearly eight feet tall. An immense frame. And…

“Taishan’s meat! Where’s the meat!”

A madness that seemed not of this world.

Gulp.

*What the hell is that?*

Just as the masked men swallowed nervously, a tiny old man poked his head out from behind the monster and pointed at them.

“You see those guys?”

“Taishan! Sees them!”

“I saw everything earlier, and those bastards ate all your meat.”

“Taishaaaaaan! Cannot forgive them!”

What did meat have to do with anything, and what did they mean by stealing and eating it?

As the flustered masked men cautiously stepped back, Sama Pyo revealed bloodstained teeth and smiled.

But he was not looking at Taishan.

His gaze was fixed on a hill overlooking the clearing.

More precisely, he was looking at someone trudging down the hill.

“I had a feeling this might happen even while I was away for a little while.”

Step. Step.

The young man approached at a leisurely pace and asked Sama Pyo:

“Are those your friends?”

Sama Pyo burst into laughter and shook his head.
```

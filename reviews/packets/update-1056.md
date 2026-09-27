<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1056.txt",
      "sha256": "5d6457d02e8e1fa4052aa45f50729f9f3c8ae01274b6b9427039695b5249cd75",
      "bytes": 14553
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "04846b248200523aae016ecaea8ca94456d247725b5b796384392efa84c3d1f9",
      "bytes": 1443
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "5928ba5f9f942187d5c6e9149eb7593670dc2db24724f7fc8e9018bc095627ca",
      "bytes": 240988
    },
    {
      "path": "characters/Blood-Sword Demon Lord.md",
      "sha256": "6aae7431fbf2bd7319b09836945f5d03d77fc380e702f38fe4d3958056117ae6",
      "bytes": 920
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "0e664f8850fc8ab53b157cf516aa0b567f9a9d760721b4670becf7a7a21a3e7a",
      "bytes": 1325
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "13e9032117e09d3d27beb83628c8611363b62e175ce87060b036bee922387481",
      "bytes": 760
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "d13a8329fe96405163249afe63bd34ae5a08d8d3b3b1741625da63416900eeec",
      "bytes": 1375
    },
    {
      "path": "characters/Ju Hwaran.md",
      "sha256": "a50fa6b2d75be929a676a1ca3e37cd9bdbc07082e211d9abff5de30afc4a5ba5",
      "bytes": 974
    },
    {
      "path": "characters/Ma Junggeol.md",
      "sha256": "bdbb590b676127f78145edb12a774b3bfe8a2a2d5d097df687c8d62749c71aef",
      "bytes": 673
    },
    {
      "path": "characters/Namho.md",
      "sha256": "2475d09f2e67753d9d4abeebf3b1ccf87ab26d275a9d4c7d50da452fbb355aae",
      "bytes": 1092
    },
    {
      "path": "characters/Sama Pyo.md",
      "sha256": "5c960ce82e93e4a61094ffb0a49afaf60adb3e9ab467347ca4f43d0257641a6d",
      "bytes": 967
    },
    {
      "path": "characters/Sima Gong.md",
      "sha256": "69a3193c47b561f904be81c65fd64d89ce4abd8876b35316320a7ab8e8730338",
      "bytes": 854
    },
    {
      "path": "characters/Song Il.md",
      "sha256": "d7db98aa15ef5aa4ac96ded8eb279bd280de72186ee8532149b50f2fcacbfd1c",
      "bytes": 774
    },
    {
      "path": "characters/Song Ilseom.md",
      "sha256": "92eb2eeda0823d5e60045214b79248d7d5019beed587ec43765eae13b5494863",
      "bytes": 980
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "5464cdab3077766dfd0f8bd101d5ca381bcc449f303e140c160d41dc495b12a3",
      "bytes": 686
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "378d7aefdd54ea7c974a9b9e4024a94e31cc9cf3b9d4e85ce7257e2497dfa904",
      "bytes": 282320
    }
  ],
  "estimated_tokens": 14088
}
-->

# Durable State Update — Chapter 1056

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
1 and safe_through 1056. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1056. Profile updates may replace only one
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
  "chapter": 1056,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1056,
    "continuity_sources": [1056],
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
    "The allied forces have effectively won the battle; the Blood-Sword Demon Lord and the mages are dead, the Grand Mage has disappeared, and the Black Ghosts are gone.",
    "Sima Gong confessed to betraying the Gansu sects and Kongtong Sect at Dunhuang; Sama Pyo proposes sacrificing the Black Dragon Demon Gate’s leaders and offering compensation to contain the reprisals.",
    "Sima Gong accepted Sama Pyo as his heir and told him to strike; the outcome is not shown.",
    "The Grand Mage departed for Qinghai on a new mission; the identity of the other servant is unknown.",
    "The Lord of Heaven’s identity and connection to Asmodeus remain unknown; a mysterious green light remains in the dispersing darkness.",
    "Some Kongtong Sect survivors vanished to an unknown location."
  ],
  "continuity_sources": [
    1054,
    1055
  ],
  "open_questions": [
    "What happens after Sama Pyo raises the Black Dragon Saber to strike Sima Gong?",
    "What are the identity and purpose of the Lord of Heaven, and is he connected to Asmodeus?",
    "Where did the missing Kongtong Sect survivors go?",
    "What is the new mission in Qinghai, and who is the other servant there?",
    "What is the mysterious green light?"
  ],
  "safe_through": 1055,
  "temporary_decisions": [
    "Render 풍운아 as “bold hero of changing fortunes” in Sama Pyo’s ironic self-description."
  ],
  "version": 1
}
```

## Exact glossary matches

| 혁무진    | **Hyuk Mujin**     |
| 청풍     | **Cheongpung**     |
| 송일     | **Song Il**        |
| 주화란    | **Ju Hwaran**      |
| 사마공    | **Sima Gong**      |
| 암천     | **Dark Heaven**                  |
| 절정     | **Peak**          |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 검기     | **Sword Energy**                                 | When functioning as projected weapon qi               |
| 사파     | **unorthodox faction**                           |                                                       |
| 마적     | **mounted bandits**                              |                                                       |
| 문주     | **Sect Leader**                              |
| 은인     | **Benefactor**                               |
| 레벨               | **Level**                      |
| 감숙     | **Gansu**              |
| 공자      | **Young Master**                                                |
| 혈검마군 | **Blood-Sword Demon Lord** | Antagonist commanding the army advancing on the Great Snow Mountain. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 마중걸 | **Ma Junggeol** |
| 남호 | **Namho** | Hidden Shadow Pavilion code name; literally associated with amber from the south. |
| 사마표 | **Sama Pyo** | Young Sect Leader of the Black Dragon Demon Gate. |
| 송일섬 | **Song Ilseom** | Young escort captain of the Yongbong Escort Bureau; distinct from Song Il of Zhongnan. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 야왕 | **Night King** | Rumored epithet for Jin Taekyung in Taiyuan's red-light district. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 마공 | **demonic martial arts** | Martial arts that appear to defy common principles. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 몸통박치기 | **Body Slam** | Comic attack command Taekyung gives Warlordmon. |
| 화란 | **Hwaran** | Familiar short form of Ju Hwaran. |
| 신력 | **divine strength** | Superhuman strength attributed to Taekyung. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 흑룡마문 | **Black Dragon Demon Gate** | Unorthodox faction from Gansu. |
| 흑룡도 | **Black Dragon Saber** | Sama Pyo's sobriquet. |
| 대초자곤 | **two-section staff** | Weapon carried by Sama Pyo's giant subordinate. |
| 공동파 | **Kongtong Sect** | Sect belonging to the Nine Sects and One Gang. |
| 흑야왕 | **Black Night King** | Epithet of Sima Gong, Sama Pyo's father and the Sect Leader who built the modern Black Dragon Demon Gate. |
| 화룡각 | **Fire Dragon Pavilion** | New name chosen for Taekyung's pavilion. |
| 사냥개 | **hunting dog** | Jin's demeaning metaphor for Ares personnel who obey Go Jun. |
| 검마 | **Sword Demon** | A Demonic Cult swordsman whose final technique is compared with One Annihilation. |
| 신인 | **divine man** | Descriptive term for a human who became something beyond humanity. |
| 백마칠종 | **Seven Masters of Baekma Bang** | Collective title for Ma Junggeol and his six associates. |
| 흑귀 | **Black Ghost** | The Blood-Sword Demon Lord’s name for the Death Knights. |
| 대술사 | **Grand Mage** | Title of the veiled woman leading the white-robed mages. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 청풍 | 혁무진 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung includes Mujin among his 은인들 after receiving the skewers. |
| 혁무진 | 청풍 | martial artist to young master | Young Master | formal-deferential | Mujin uses 공자께서는 when asking why Cheongpung descended from the mountain. |
| 송일 | 청풍 | hostile Zhongnan Elder to younger martial artist | Sword Saint's heir / you | hostile and threatening | Song Il identifies Cheongpung as the Sword Saint's heir and demands that he face the consequences of injuring Gong Ilhyuk. |
| 송일섬 | 주화란 | escort_captain_to_young_bureau_head | Hwaran | urgent and familiar | Calls out 화란아 while urgently warning Ju Hwaran before stepping into the confrontation. |
| 주화란 | 혁무진 | rescued_survivor_to_benefactor | Benefactor | formal-deferential | Hwaran includes Mujin among the Benefactors when greeting Taekyung's companions. |
| 주화란 | 청풍 | rescued_survivor_to_benefactor | Benefactor | formal-deferential | Hwaran includes Cheongpung among the Benefactors when greeting Taekyung's companions. |
| 주화란 | 송일섬 | bureau_head_to_escort_captain | Captain Song | formal and prosecutorial | Uses his office title, then his personal name, while exposing and confronting him. |
| 주화란 | 사마표 | former_fiancés | Young Sect Leader | formal and guarded | Hwaran formally greets her former fiancé. |
| 사마표 | 태산 | Young Sect Leader to subordinate | Taishan | informal and patronizing | Sama Pyo calls Taishan by name while ordering him to leave. |
| 태산 | 사마표 | subordinate to Young Sect Leader | Lord | crude and deferential | Taishan uses 주군 while obeying Sama Pyo. |
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
| 주화란 | 조장님 | pavilion member to squad leader | Captain | familiar and deferential | Hwaran asks Captain where he is going before he confronts the mistreatment. |
| 태산 | 주화란 | Pavilion member to Pavilion member | Young Lady Ju | clipped, childlike, and deferential | Agrees with Ju Hwaran after she mentions the evening banquet. |
| 태산 | 남호 | Fire Dragon Pavilion member to guide | Namho | clipped, childlike, and informal | Taishan directly addresses Namho while asking what Dark Heaven is. |
| 남호 | 각주 | guide to pavilion master | Pavilion Master | blunt, hostile, and abusive | Namho addresses Jin as 각주 while accusing him of causing the disturbance. |
| 사마표 | 각주 | Fire Dragon Pavilion member to pavilion master | Pavilion Master | formal but sardonic | Sama Pyo addresses Jin as 각주 while questioning his account of the incident. |
| 태산 | 각주 | Fire Dragon Pavilion member to pavilion master | Pavilion Master | clipped, childlike, and informal | Taishan directly asks Jin whether his Lord Sama Pyo is safe. |
| 주화란 | 태산 | pavilion_member_to_pavilion_member | Young Hero Taishan | formal but stern | Ju Hwaran reprimands Taishan for speaking ominously about Jin and warns that she will muzzle him. |
| 혁무진 | 주화란 | Fire Dragon Pavilion member to fellow member | Young Lady Ju | polite and deferential | Mujin addresses Hwaran as 주 소저 while asking her to call a physician. |
| 신의 | 주화란 | senior physician to younger ally | Young Lady Ju | warm and teasing | The Divine Physician lightly teases Hwaran about being more worried for Jin than he is. |
| 신의 | 태산 | senior physician to younger ally | Young Hero Taishan | urgent and respectful | The Divine Physician uses this address while pleading with Taishan to keep moving. |
| 송일섬 | 혁무진 | Older fellow Pavilion member and martial senior | you | casual and informal | Song insists that his age and martial experience entitle him to speak casually to Mujin. |
| 마중걸 | 사마공 | visiting group leader to sect leader | Sect Leader Sima | polite and respectful | Addresses him as 사마 문주 while explaining Ningxia and Baekma Bang. |
| 사마공 | 마중걸 | sect leader to visiting group leader | you | formal and probing | Uses 자네 while questioning Ma Junggeol about following Dark Heaven. |
| 사마공 | 사마표 | father to son | Pyo | intimate and familiar | Sima Gong calls him 표야 and 내 아들아. |
| 사마표 | 사마공 | son to father | you; Father | familiar and confrontational | Sama Pyo challenges his father during their battlefield confrontation. |
| 마중걸 | 주화란 | fellow combatant addressing the young bureau head | Young Lady | polite and hesitant | Addresses her as 소저 while trying to speak up about his injuries. |
| 혈검마군 | 사마공 | former bargaining allies turned enemies | you; you traitor | blunt and hostile | Uses direct, contemptuous forms while accusing Sima Gong of betraying him. |
| 사마공 | 혈검마군 | former bargaining allies turned enemies | you; you Demonic Cult bastard | calm and contemptuous | Uses 당신 before ending with the insult 마교 잡놈아. |
| 대술사 | 혈검마군 | subordinate_to_commander | Demon Lord | respectful and formal | Addresses him as 마군 while acknowledging his injuries. |
| 혈검마군 | 대술사 | commander_to_subordinate | Grand Mage | blunt and commanding | Orders her to heal him immediately. |

## Listed compact profiles

### Blood-Sword Demon Lord.md

# Blood-Sword Demon Lord (혈검마군)

- **Safe through:** Chapter 1055
- **Aliases:** None
- **Role:** The Blood-Sword Demon Lord is a formidable martial master who commands the force advancing on the Great Snow Mountain and now serves the Lord of Heaven.
- **Personality:** Devoted to his master and proud of his abilities, he is deeply wounded by perceived distrust and resolves to prove his worth.
- **Voice:** Casually familiar and self-amused, addressing Jeok Cheongang respectfully as Senior while trading blunt insults; his easy laughter can turn to a low, cold intensity.
- **Relationships:** He serves the Lord of Heaven with deep devotion, but the Grand Mage says the Lord ordered his disposal; he has been ordered not to kill Jin Taekyung, admires Jeok Cheongang, and once shared the Demonic Cult with the fiends who became Black Ghosts.

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 990
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, the grandson and Disciple of Sword Saint Mae Jonghak, a Supreme Peak martial master known as the Huashan Divine Dragon, the creator of the snake-inspired Mimi Step footwork technique, and the master of the Azure Dragon Pavilion within the Alliance Leader's Two Dragons Pavilion.
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, a deep love of martial arts, competitive pride, unusual resistance to monster-induced Fear, and discomfort when someone copies his martial arts.
- **Voice:** Dreamy and hazy, with innocent, polite phrasing; he has begun imitating Taekyung's profanity.
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions while Taekyung is his only true martial rival; Tang Sadok has temporarily entrusted Mimi, now a large horned snake, to him, and Cheongpung is accompanying Mungyeong while learning his martial arts through observation to become stronger and adapt to this world.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1055
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 1046
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and an active member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented; despite being naturally fearful, he faces danger and remains loyal to the person he serves, with irreverent self-deprecation and a taste for glory. He is suspicious of Taekyung, bluntly critical of the family's disgraced third son, and an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; with Taekyung, blunt and occasionally incredulous, while using breezy, irreverent banter to defuse tense situations.
- **Relationships:** He is loyal to Taekyung, who trusts him to act independently, especially in his home region of Shanxi and at the Jin Family of Taiyuan. As a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Fire Dragon Pavilion members accompanying Taekyung. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business.

### Ju Hwaran.md

# Ju Hwaran (주화란)

- **Safe through:** Chapter 1046
- **Aliases:** Hwaran
- **Role:** Ju Hwaran is a Level 88 Young Bureau Head, leader of the Yongbong Escort Bureau, an experienced Nanman guide, and an active member of the Fire Dragon Pavilion.
- **Personality:** Intelligent, capable, responsible, and filial; remains controlled under pressure but has grown more assertive and openly impatient after the hardships she has endured.
- **Voice:** Clear, polite, restrained, and determined.
- **Relationships:** Escort King Ju Gongsan was her paternal grandfather, Ju Hogun is her father, Heo Jun was her uncle, Sama Pyo was her former fiancé in a political engagement she accepted for her father's sake, Song Ilseom is her direct escort who accompanied her previous journey to Yeongin, and Jin Taekyung is a trusted ally; the Yongbong Escort Bureau has longstanding ties with Yeongin’s inhabitants.

### Ma Junggeol.md

# Ma Junggeol (마중걸)

- **Safe through:** Chapter 1046
- **Aliases:** Chief of Baekma Bang
- **Role:** Ma Junggeol is the chief of Baekma Bang, a horse-caravan group founded by reformed Ningxia mounted-bandit leaders.
- **Personality:** Though timid by nature, he is earnest and protective of his sworn brothers, loyal to the benefactor who helped them reform, and willing to bear personal risk for their mission.
- **Voice:** Not established
- **Relationships:** He leads six sworn brothers who, with him, are known as the Seven Masters of Baekma Bang, and trusts the benefactor they call the Lord.

### Namho.md

# Namho (남호)

- **Safe through:** Chapter 1046
- **Aliases:** Elder Chao
- **Role:** Namho is an eighty-year-old non-Han Hidden Shadow Pavilion agent who spent more than fifty years undercover in Nanman and maintained contact with Central Plains intelligence through the Pavilion’s Hidden Thread; he guides the Fire Dragon Pavilion and represents Jin Taekyung and the Murim Alliance in negotiating the survivors’ chance to rebuild the Murong household.
- **Personality:** Duty-bound, pragmatic, and observant; uses theatrical violence to protect intelligence work and takes a veteran’s concern for the younger generation’s resolve.
- **Voice:** Measured and reflective when advising the younger generation, loudly abusive when maintaining his local cover, and capable of theatrical boasts and dry humor.
- **Relationships:** Namho is a Hidden Shadow Pavilion contact for Jin Taekyung and the Fire Dragon Pavilion, receives intelligence from the Pavilion Master, and knows the code used by the Thousand-Faced Fox.

### Sama Pyo.md

# Sama Pyo (사마표)

- **Safe through:** Chapter 1055
- **Aliases:** Black Dragon Saber
- **Role:** Young Sect Leader and heir of the Black Dragon Demon Gate, a Morning Star reputed to be no less than the Ten Dragons and Phoenixes.
- **Personality:** Courteous and calculating, he is willing to sacrifice himself and the Gate’s leaders to protect its people and contain the consequences of his father’s betrayal.
- **Voice:** Polite and ingratiating in public, with sardonic humor and controlled evasiveness.
- **Relationships:** Sama Pyo is Sima Gong’s son and chosen heir; his father approved his resolve to take responsibility for the Gate’s betrayal and told him to strike, though the outcome is unknown. He commands the absolutely loyal Taishan, admires Jin Taekyung, was Ju Hwaran’s former fiancé in a political engagement, and is openly hostile toward fellow member Song Ilseom.

### Sima Gong.md

# Sima Gong (사마공)

- **Safe through:** Chapter 1055
- **Aliases:** Black Night King
- **Role:** Sima Gong is the Sect Leader who built the Black Dragon Demon Gate into a major unorthodox power and the father of its Young Sect Leader, Sama Pyo.
- **Personality:** Sly and calculating yet capable of risking himself for a moment of conscience, he values his heir’s future and repaying a debt to Jeok Cheongang.
- **Voice:** Polished and persuasive, with smooth rhetorical turns and a composed, gently teasing manner.
- **Relationships:** Sama Pyo is his youngest son among seven older brothers and nine older sisters; Sima Gong chose him as heir and told him to strike after approving his plan to answer the Gate’s betrayal. Sima Gong aided Jeok Cheongang despite their history.

### Song Il.md

# Song Il (송일)

- **Safe through:** Chapter 1054
- **Aliases:** Roaring Fury Swordsman
- **Role:** Elder of the Zhongnan Sect, known as the Roaring Fury Swordsman and one of Sect Leader Gong Iljung’s two Senior Brothers.
- **Personality:** Arrogant and domineering, but capable of remorse over choices that harmed his sect and those he failed to protect.
- **Voice:** Gruff, cutting, condescending, and threatening, with formal authority used to pressure those beneath him.
- **Relationships:** Gong Iljung is his junior Sect Leader and martial younger brother; Gong Ilhyuk is a junior Disciple of his sect; he recognizes Baek Museong and Cheongpung through their Huashan and Sword Saint connections.

### Song Ilseom.md

# Song Ilseom (송일섬)

- **Safe through:** Chapter 1046
- **Aliases:** Escort Captain Song
- **Role:** Song Ilseom is a Level 110 escort captain of the Yongbong Escort Bureau, one of its Dragon-Phoenix Three Escorts, and a member of Jin Taekyung and Cheongpung’s Fire Dragon Pavilion.
- **Personality:** Blunt, decisive, survival-hardened, and dryly self-aware, with little patience for insults or disorder and practical survival skills such as making disguise masks.
- **Voice:** Direct and rough, with dry, matter-of-fact teasing among allies and forceful urgency in command.
- **Relationships:** He serves under Ju Hwaran and has expressed concern that she not be hurt or die needlessly; he is Song Pyosan’s son, his grandmother was the surviving Guangdong Chen child rescued by Ju Gongsan during the Great Faction War, and he remains openly hostile toward fellow Fire Dragon Pavilion member Sama Pyo.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 1052
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo; becomes explosively violent when his meat is threatened.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord, trusts Jin Taekyung as Pavilion Master, and has grown attached to the Fire Dragon Pavilion members.

## Korean source

```text
＃1056화



슈확!

바람을 찢은 섬광은 실로 예리하면서도 정확했다.

흑룡도(黑龍刀).

고작 십 대에 불과했던, 그러나 어린 나이를 무색하게 만들 만큼 일찍이 두각을 드러냈던 한 소년이 아버지에게 처음이자 마지막으로 선물 받았던 보도(寶刀)는, 주인의 손을 따라 눈앞의 목표를 정확히 베어 갈랐다.

서걱!

서늘한 절삭음과 함께 핏물이 튀었고, 이 모든 것을 직시하고 있던 한 쌍의 눈동자가 깊게 가라앉았다.

“무슨 짓이냐.”

많은 것이 담긴 물음이었지만, 되돌아온 대답은 간단명료했다.

“제가 원하는 길이 아니기 때문입니다.”

사마표는 차갑게 식은 칼자루에서 손을 뗐다.

흑룡마문의 후계자에게만 허락된 그 예리한 날붙이는, 사마공의 콧날을 스쳐 지나가 피 웅덩이를 가른 후였다.

진정한 사파인으로 성장한 아들의 모습에 기뻐하며, 기꺼이 죽음을 받아들였던 아버지를 비웃듯이.

“이게 제 선택입니다. 당신의 뒤를 이어 흑룡마문의 문주가 될, 이 사마표가 택한 길입니다.”

“어째서……!”

핏물이 끓어오르는 목소리로 외치는 사마공을, 사마표는 담담한 눈빛으로 응시했다.

“옳지 않기 때문입니다.”

“뭐라?”

“최선(最先)이나, 최선(最善)이 아니기 때문입니다.”

사마표에게 있어, 이것은 무엇이 먼저냐의 문제가 아니었다.

무엇이 옳은가, 더욱 선한가의 문제였다.

“일평생 잊고 있었습니다. 아니, 익숙해져 있었기에 계속해서 모른 척해 왔습니다. 하지만 이제는 아닙니다.”

감숙에서의 지난 삶은, 그야말로 투쟁의 연속이었다.

앞서 태어난 피붙이들이 그러했듯, 사마가(家)의 막내 역시 버림받지 않기 위해 발버둥 쳐야 했다.

그들은 같은 핏줄을 지닌 가족인 동시에, 오직 하나뿐인 후계자 자리를 다퉈야 하는 경쟁자였으며, 이러한 핏줄을 물려준 한 사람에게 복종하는 군인이나 다름없었다.

때로는 죽음조차 불사해야 하는, 그런 존재.



‘아버지, 둘째 형님께서……!’

‘이미 전령을 통해 들었다. 장례는 놈들을 모조리 쓸어 버린 후에 치를 것이니, 그리 알고 있거라.’



사마공은 냉철한 정복자였고, 사파를 일통하기 위해서는 그만한 피와 희생이 필요했다.

흑룡마문이 천하의 모든 사파를 아우르고 공동파와 어깨를 나란히 하는 과정에서, 다섯이 넘는 형제와 누이가 죽음을 맞이했다는 사실은 공공연한 비밀이었다.

불과 십 대의 나이임에도 후계자로 낙점된 흑룡마문의 막내 공자가, 보이는 것만큼 냉정하지 않다는 사실은 누구도 몰랐지만.



‘어찌 그리 서럽게 울고 있느냐?’

‘아버지, 흑룡마문 도왔다. 그런데 죽었다. 슬프다.’

‘……!’

‘시신, 찾아야 한다. 아버지 묻어 줘야 한다. 그런데, 그런데 저 사람들이 모른다고 했다. 태산이 슬프다.’

‘……태산이라고 했지, 따라오거라.’



사마표는 산만 한 덩치로 울고 있는 소년의 아버지를 찾아 주었다. 흑룡마문의 무복을 입은 채, 까마귀 떼에 둘러싸여 있던 그를 정성 들여 묻었다.

그리고 생전 처음으로 친구를 얻었다.

가족보다 소중한, 아버지보다 자신을 아껴 주는 유일한 친구를.

하지만 그로부터 십여 년의 세월이 흐른 후, 또 다른 친구들이 생길 것이라고는 생각하지 못했다.

“그들과 함께 지내며 알게 되었습니다. 모든 것은 결국 제 선택에 따라 달라진다는 것을.”

화룡각.

그 거창한 이름과는 달리, 고작 열 명도 되지 않는 그들의 틈바구니에서 사마표는 자신이 몰랐던 새로운 길을 발견할 수 있었다.

그곳에서는 어떤 족쇄나 꼬리표도 존재하지 않았다.

언제나 서로를 믿고 싸웠고, 그렇게 위기를 헤쳐 나갔다.

아마도 그래서였을 것이다.

사마표가 자신의 지난 삶을 몇 번이나 되돌아보게 된 이유도.

어느 순간부터, 피도 눈물도 없는 아버지에 대해 낯선 감정이 들기 시작한 이유도.

“문득 그런 생각이 들었습니다. 알고 보면 당신도, 퍽 불쌍한 사람이라는 생각이.”

“……!”

“처음부터 그러지는 않았겠지요. 서서히 야망에 사로잡히고, 어느 날부터인가 수단과 방법을 가리지 않게 되었겠지요.”

한때, 아버지의 냉엄한 시선을 차마 마주칠 수 없었던 아들은 이제 없다.

지금 이 순간, 사마표는 담담하면서도 슬픔이 담긴 눈빛으로 죽음을 코앞에 둔 아버지를 바라보고 있었다.

“우연이 아니었습니다.”

“그게…… 무슨.”

“우연히 돌아온 것이 아닙니다. 그저, 당신의 마지막을 지키기 위해 온 겁니다. 흑야왕의 후계자가 아니라, 사마공의 피를 이어받은 아들로서.”

철벅.

“알고 계십니까?”

사마표는 피 웅덩이에 앉아 자신의 아버지와 시선을 맞추었다. 떨리는 그의 눈동자를 바라보며 천천히 말을 이었다.

“아버지를 죽일 수 있는 아들은, 이 세상에 없습니다.”

“……!”

“제 입으로 직접 저들에게 모든 사실을 밝힐 겁니다. 아버지의 배신을 애써 모른 척해 왔던 못난 아들에 관한 이야기도 털어놓겠습니다.”

“너.”

“용서받고자 하는 것이 아닙니다. 감내하려는 것입니다.”

모든 것을 받아들인 평온한 그 대답에, 사마공은 아무 말도 할 수 없었다.

그저 오랫동안 잊고 있던, 오늘 이 자리에서야 문득 떠올린 어떤 감정을 억누르기 위해 안간힘을 쓸 뿐이었다.

서서히 어두워지는 시야 속. 마지막을 암시하듯 가빠지는 숨결을 느끼며.

“왜 그랬냐고, 물었었지. 일평생 생존과 실리만을 좇던 내가 왜 그런 멍청한 선택을 했느냐고…….”

자신의 모든 것을 물려줄 후계자를 구하기 위해서?

아니다. 아니었다.

적어도 그때 그 순간만큼은, 또 다른 이유였음을 사마공은 알고 있었다.

다만, 이를 고백하기에는 너무 늦었을 뿐.

“나는, 이 아비는.”

아버지의 최후를 지키기 위해 돌아온 아들을 향해, 사마공은 남아 있는 온 힘을 다해 목소리를 쥐어 짜냈다.

그것이 자신의 마지막 숨결이라는 사실조차 인식하지 못한 채.

스륵.

불현듯 꺾이는 고개.

살아생전의 업보처럼, 처참한 모습으로 죽음을 맞이한 아버지를 향해 아들은 나직이 속삭였다.

“들었습니다. 분명히.”

이내 들썩이는 어깨를 따라, 두 부자(父子)를 적신 피웅덩이가 잘게 떨리고 있었다.



* * *



극도로 훈련된 사냥개들은 언제나 주인의 명령을 따라 움직인다.

주인이 가리킨 사냥감을 직시하고, 이빨을 드러내며 으르렁대다가, 마침내 목줄이 풀림과 동시에 온 힘을 다해 달려나가 물어뜯는 것이다.

사냥감의 숨통이 끊어질 때까지.

혹은 사냥을 그만하고 되돌아오라는 주인의 명령이 떨어지기 전까지.

바로 지금처럼.

쐐애액!

측면으로부터 시작된, 강렬한 파공성과 함께 번뜩이는 섬광.

그러나 속도란 늘 상대적인 것이다.

새하얀 검신을 타고 솟구친 검기(劍氣)가 정수리를 향해 떨어져 내리는 그 일련의 과정은 절정 고수의 솜씨답게 쾌속했지만, 내게는 아니었다.

서걱!

일순간 갈라지는 공간.

반 박자 늦은 절삭음과 함께, 은백색의 창날이 스쳐 지나간 궤적 안의 모든 것이 베어졌다.

어느새 바람 앞의 촛불처럼 꺼져버린 검기.

그 강력한 기운을 담고 있던 검신.

마지막으로 이 덧없는 공격을 감행한 누군가의 몸뚱어리까지.

푸확!

군더더기 없이 깔끔하게 분리된 몸뚱어리에서 엄청난 양의 피 분수가 뿜어져 나왔지만, 그 처참한 광경에도 나는 눈 하나 깜짝하지 않았다.

지금 이 순간에도 사방에서 달려드는, 또 다른 사냥개들 역시 마찬가지였다.

푹, 콰득! 퍼걱!

가장 먼저 전방에서 달려드는 놈의 가슴에 창날을 박아넣고, 곧이어 사각에서 들이닥친 적의 얼굴을 일권(一拳)으로 짓뭉개는 동시에 박혀있던 창날을 뽑아 휘둘렀다.

“꺼흑, 끅.”

털썩.

유언을 대신한 단말마(斷末摩)와 동시에 쓰러지는 세 명의 절정 고수.

아니, 세 구의 시체.

하지만 피로 물든 설원을 휘감은 전투의 광기는, 조금도 사그라질 기미가 보이지 않았다.

쉬쉬쉬쉭!

찰나의 공백조차 허락하지 않고 빈 자리를 메우며 달려드는 암천의 교도들.

그리고 한 줌의 감정조차 깃들어있지 않은 그 무감각한 표정과 눈동자들을 보며, 나는 전신을 짓누르는 극심한 피로를 느꼈다.

‘도대체 몇 명째지?’

모르겠다.

내 손에 죽음을 맞이한 적들의 숫자를 일일이 헤아릴 여유도, 그럴 이유도 없었으니까.

그저 싸울 뿐이다. 끊임없이 쓰러트릴 뿐이다.

영혼이 없는 저 목각 인형들을.

자신들의 목줄을 쥔 주인이 사라졌음에도 불구하고, 마지막으로 내려진 명령을 따라 맹목적으로 임무를 수행하고 있는 저 사냥개이자 부나방들을.

물론 나 역시 알고 있다.

이건 일방적인 학살이고, 살육이다.

그러나 반드시 해내야 했다.

그것만이 피로 얼룩진 이 혈투를 끝내는 유일한 방법이자, 한 사람이라도 더 많은 아군을 구할 수 있는 길이니까.

그렇기에 나는 당장이라도 끊어질 것 같은 이 의식의 끈을, 온 힘을 다해 붙잡을 수밖에 없었다.

‘와라.’

나는 마음속으로 뇌까리며 적들을 향해 쇄도했다.

정확히는, 쇄도하려 했다.

바로 그 순간, 아득해지는 시야를 느끼기 전까지는.

“……!”

머릿속에서 붉은색 경종이 울렸다.

한참 전부터 한계에 달해있던 정신력이 참지 못하고 전달한 위험신호.

하지만 내가 애써 이를 악물며 눈을 부릅떴을 때는, 이미 모든 것이 늦어 있었다.

슈확!

어느샌가 비스듬히 기울어진 시야 속, 나도 모르는 사이에 휘청이고 만 몸뚱어리를 향해 십여 자루의 날붙이가 쏟아지고 있었다.

흐릿하면서도, 느리게.

문제는 극도로 예리한 안력(眼力)과는 달리, 빠르게 명령을 내려 몸을 움직여야 할 두뇌가 석상처럼 굳어있다는 것이었다.

‘빌어먹을.’

느려진 세상 속, 나는 내심 욕설을 내뱉었다.

저들은 혈검마군도, 대술사도, 흑귀들과 비견될 만한 무위를 지니지도 않았다.

아니, 턱없이 부족하다.

평상시의 나였다면 코웃음을 쳤을 정도의 격차.

그럼에도 저들의 공격을 온전히 피할 수 없으리라는 직감이 들었다.

몸이 움직이지 않는 이 와중에도 문득 뇌리를 스치는 어이없는 생각과 함께.

‘레벨 업 이거, 혹시 사지가 잘려나가도 회복시켜주나?’

그러나 다행히도, 청풍 같은 인간이나 좋아할 법한 불쾌한 첫 경험을 걱정할만한 상황은 벌어지지 않았다.

다음 순간 어디선가 울려 퍼진 엄청난 파공성이, 내가 품고 있던 우려를 한 번에 날려버렸으니까.

후우우웅!

그건 말 그대로 눈 깜짝할 사이에 벌어진 일이었다.

나를 향해 쇄도하던 적들의 어깨너머로 불쑥 솟구친 거대한 그림자와 함께, 그 명칭처럼 크고 아름다운 대초자곤(大梢子棍)이 벼락처럼 공간을 갈랐다.

콰드드득!

단 한 번의 빠따질로 머리통 다섯 개를 날려 보내는 광경을 보았느냐고 누군가가 묻는다면, 나는 망설임 없이 고개를 끄덕일 것이다.

이제는 각성자들의 놀이터가 되어버린 현대식 메이저리그를 폭격할 저 특급 유망주의 이름도 알려줄 수 있다.

물론, 저 미친 떡대는 누가 말해주기도 전에 스스로 본인을 소개하겠지만.

바로 지금처럼.

“태산이! 왔다! 봤다! 때렸다!”

“잘했다! 자, 이어서 몸통박치기!”

그리고 카이사르 시저도 울고 갈 명언을 내뱉은 태산의 어깨에 걸터앉은 남호를 시작으로, 낯익은 얼굴들이 빛살처럼 튀어나왔다.

“공자님, 아니 은인! 아니 각주님!”

서걱!

트랜스포머도 한 수 접어줄 삼단 변화 호칭을 토해내며 적의 뒤통수를 쪼개는 주화란.

“갈! 네놈들이 감히 조장님을 해하려 하다니! 용기는 가상하나 그러기 위해서는 바로 이 몸, 조장님의 오른팔이자 심장! 바로 나 혁무……어어 시발!”

캉!

한껏 분위기를 잡으며 달려들다가, 예상외로 한 수 위인 적의 반격에 허겁지겁 물러나는 혁무진.

“그, 혹시 저 친구는 아가리를 여물고 싸우는 법을 모르나?”

“당신부터 여무시오.”

푸푹!

그런 혁무진을 구하며, 단숨에 남아 있는 적들을 베어내는 송일섬과…… 잠깐, 저 새카만 털북숭이 아저씨가 누구였더라.

“흑마칠종(黑馬七宗)?”

불현듯 입술을 비집고 흘러나온 네 글자에, 전직 마적 출신인 중년인이 가뜩이나 흉악한 얼굴을 일그러트렸다.

“흑마가 아니고 백마! 백마칠종의 맏형 마중걸이오! 내가 누구 때문에 이 개고생을 했는데 그걸 까먹……!”

“목소리 낮추세요. 좋게 말할 때.”

주화란의 스산한 경고에 입을 꾹 다무는 마중걸의 모습을 보자, 나도 모르게 실소가 흘러나왔다.

그냥, 보기 좋아서.

누구 하나 잃지 않았다는 사실을 알게 되어서.

그리고…….

이대로 영영 헤어질 줄 알았던, 마지막 한 사람을 볼 수 있어서.

“왔냐?”

내가 불쑥 던진 물음에, 언제 나타났는지 모를 사마표가 어깨를 으쓱해 보였다.

“많이 늦은 건가?”

아니.

그럴 리가.
```

## Final English reading copy

```markdown
# Chapter 1056

*Shwaa!*

The flash that tore through the wind was razor-sharp and perfectly aimed.

The Black Dragon Saber.

The treasured blade had been a gift from his father—the first and last he had ever received from him. Its owner had been only a boy in his teens, yet he had distinguished himself so early that his youth hardly mattered. Now the blade followed its master’s hand and cut cleanly through the target before him.

*Shhk!*

Blood sprayed with a cold, slicing sound. A pair of eyes that had watched the whole thing sank deeply.

“What have you done?”

The question held a great many things, but the answer was simple.

“Because this isn’t the path I want.”

Sama Pyo let go of the hilt, already cold beneath his hand.

The keen blade, a weapon permitted only to the heir of the Black Dragon Demon Gate, had passed just beside Sima Gong’s nose and cut through the pool of blood.

As if mocking the father who had been glad to see his son become a true man of the unorthodox faction—and had willingly accepted death.

“This is my choice. The path I, Sama Pyo, have chosen—the man who will succeed you as Sect Leader of the Black Dragon Demon Gate.”

“Why…!”

Sama Pyo calmly met Sima Gong’s gaze as he shouted, his voice boiling with blood.

“Because it isn’t right.”

“What?”

“Because it isn’t what comes first, or what is best.”

For Sama Pyo, this wasn’t a question of what came first.

It was a question of what was right—and what was better.

“I’d forgotten for my whole life. No—I’d grown so used to it that I kept pretending not to know. But not anymore.”

His life in Gansu had been one long struggle.

Like the siblings born before him, the youngest of the Sama family had fought desperately to avoid being cast aside.

They were family, bound by the same blood, and rivals competing for the one and only position of heir. They were little more than soldiers, obeying the one man who had given them that blood.

The kind of people who sometimes had to face even death without hesitation.

*“Father, Second Brother…”*

*“I’ve already heard from the messenger. We’ll hold the funeral after we’ve wiped them all out. Understand?”*

Sima Gong had been a cold conqueror. Unifying the unorthodox faction demanded blood and sacrifice.

It was an open secret that more than five of Sama Pyo’s brothers and sisters had died as the Black Dragon Demon Gate brought every unorthodox faction in the land under its banner and rose to stand alongside the Kongtong Sect.

No one knew that the Black Dragon Demon Gate’s youngest young lord, chosen as heir while still in his teens, wasn’t as cold as he seemed.

*“Why are you crying so bitterly?”*

*“Father helped Black Dragon Demon Gate. But he died. Taishan sad.”*

*“……!”*

*“Need to find body. Taishan needs to bury father. But, but those people said they don’t know. Taishan sad.”*

*“……You said your name was Taishan. Come with me.”*

Sama Pyo had found the father of the huge boy who was crying, then carefully buried him. He had been wearing the Black Dragon Demon Gate’s uniform, surrounded by a flock of crows.

And Sama Pyo had made his first friend.

A friend more precious than family—the only one who cared for him more than his own father did.

But he hadn’t imagined that he would make other friends more than a decade later.

“Living with them taught me that in the end, everything changes according to the choices I make.”

The Fire Dragon Pavilion.

Despite its grand name, it had fewer than ten members. Among them, Sama Pyo had found a new path he’d never known existed.

There were no shackles or labels there.

They always trusted one another and fought together, and that was how they overcame each crisis.

Perhaps that was why.

Why Sama Pyo had looked back on his past again and again.

Why, at some point, he had begun to feel something unfamiliar toward his father, a man of ice and stone.

“Then, out of nowhere, I thought: when you look at it closely, you’re a rather pitiable man.”

“……!”

“You probably weren’t like this from the start. Little by little, ambition took hold of you. And one day, you began using any means necessary.”

The son who once couldn’t bear to meet his father’s cold gaze was gone.

Now, in this moment, Sama Pyo looked at his father, who stood on the brink of death, his eyes calm but full of sorrow.

“It wasn’t an accident.”

“What… do you mean?”

“I didn’t happen to come back. I came to see you through your final moments. Not as the heir of the Black Night King, but as the son who carries Sima Gong’s blood.”

*Splash.*

“Do you know?”

Sama Pyo sat in the pool of blood and met his father’s eyes. Watching his trembling pupils, he continued slowly.

“No son in this world can kill his father.”

“……!”

“I’ll tell them everything myself. I’ll also confess what a pathetic son I’ve been—turning a blind eye to your betrayal even though I knew the truth.”

“You…”

“I’m not asking to be forgiven. I’m choosing to bear it.”

At that peaceful answer, as if he had accepted everything, Sima Gong could say nothing.

He could only struggle to hold back a feeling he’d forgotten for so long, one that had suddenly come back to him here, today.

As his vision slowly dimmed, his breath grew short, hinting at the end.

“You asked why I did it. Why I, who’d spent my whole life chasing survival and practical gain, made such a foolish choice…”

To save the heir who would inherit everything he had?

No. That wasn’t it.

At least in that moment, Sima Gong knew there had been another reason.

He was simply too late to confess it.

“I, your father…”

Facing the son who had returned to see his father’s last moments, Sima Gong squeezed out his remaining strength to speak.

He didn’t even realize that this was his final breath.

*Slump.*

His head suddenly drooped.

The son looked toward his father, who had met death in a wretched state, as if paying for the sins of his life. Then he whispered quietly.

“I heard you. Clearly.”

The pool of blood soaking father and son trembled faintly as Sama Pyo’s shoulders began to shake.



* * *



Highly trained hunting dogs always obeyed their master’s commands.

They fixed their eyes on the prey their master pointed out, bared their teeth and growled, then, the moment their leash was released, charged forward with all their strength and tore into it.

Until their prey stopped breathing.

Or until their master ordered them to stop hunting and return.

Just like now.

*Shwaa!*

A fierce, piercing whistle and a flash of light came from the side.

But speed was always relative.

The Sword Energy that surged along the white blade and fell toward my crown moved with the lightning-fast speed of a Peak master. But to me, it didn’t.

*Shhk!*

Space split in an instant.

A fraction of a beat later, the slicing sound rang out. Everything within the path of the silver-white spearhead had been cut apart.

The Sword Energy went out like a candle before the wind.

The sword that held that mighty energy.

And finally, the body of the person who had launched this futile attack.

*Fwoosh!*

A tremendous fountain of blood burst from the body, split cleanly without a single ragged edge. But I didn’t even blink at the gruesome sight.

Neither did the other hunting dogs charging from every direction, even now.

*Thud, crunch! Whump!*

I drove my spearhead into the chest of the first enemy charging straight at me, then crushed the face of another who came at me from the blind spot with one punch. At the same time, I yanked out the embedded spearhead and swung it.

“Ghk—kgh.”

*Thump.*

Three Peak masters fell as their dying cries served as their last words.

No—not three masters.

Three corpses.

But the battle frenzy sweeping across the blood-soaked snowfield showed no sign of easing.

*Shh-shh-shh-shhk!*

The Dark Heaven cultists charged in without allowing even the briefest gap, rushing to fill the space left behind.

Looking at their blank expressions and emotionless eyes, I felt the crushing exhaustion weighing down my whole body.

*How many is that now?*

I had no idea.

I had neither the time nor the reason to count every enemy who had died by my hand.

I just had to fight. Keep knocking them down.

Those soulless wooden puppets.

Those hunting dogs, those moths to the flame, blindly carrying out their final orders even though the master who held their leash was gone.

Of course, I knew what this was.

A one-sided massacre. Slaughter.

But I had to do it.

It was the only way to end this blood-soaked battle, and the only way to save as many allies as possible.

So I had no choice but to cling with all my strength to the thread of consciousness that felt ready to snap at any moment.

*Come on.*

I muttered the words to myself and charged toward the enemy.

Or tried to.

That was when my vision began to fade.

“……!”

A red alarm bell rang in my head.

My mental strength had reached its limit long ago. Now, unable to endure any longer, it was sending me a warning.

But by the time I gritted my teeth and forced my eyes open, it was already too late.

*Shwaa!*

From my slanted, blurry view, a dozen blades came raining down on my body as it staggered without my realizing it.

Faintly. Slowly.

The problem was that, as keen as my eyes were, the brain that needed to send quick commands to move my body had frozen like stone.

*Damn it.*

In the slowed-down world, I cursed under my breath.

These men weren’t the Blood-Sword Demon Lord, the Grand Mage, or even close to the Black Ghosts.

No—they were far weaker.

The gap was so wide that under normal circumstances, I would’ve scoffed at them.

Even so, I had a gut feeling I wouldn’t be able to dodge all their attacks.

And, even as my body refused to move, one ridiculous thought crossed my mind.

*If I level up, does that maybe heal me even if my limbs get cut off?*

Fortunately, nothing happened that forced me to worry about the unpleasant first-time experience only someone like Cheongpung might look forward to.

The next moment, an enormous whistle rang out from somewhere and swept all my worries away.

*Whoooosh!*

It happened in the blink of an eye.

Over the shoulders of the enemies charging toward me, a huge shadow suddenly surged upward. Along with it, the two-section staff—big and beautiful, just like its name—sliced through the air like a bolt of lightning.

*Craaaack!*

If someone asked whether I’d ever seen five heads blown away with a single whack of a bat, I’d nod without hesitation.

I could even tell them the name of the top prospect who’d be bombing today’s modern Major League, now turned into a playground for Awakened Ones.

Of course, that lunatic hulk would introduce himself before anyone else could tell you.

Just like now.

“Taishan! Came! Saw! Hit!”

“Well done! Now, Body Slam!”

Starting with Namho, perched on the shoulder of Taishan—who had just delivered a line to rival even Julius Caesar—familiar faces burst out like streaks of light.

“Young Master! No, Benefactor! No, Captain!”

*Shhk!*

Ju Hwaran split an enemy’s skull while blurting out a three-step change of address that even Transformers would’ve had trouble keeping up with.

“Fools! How dare you try to harm the Captain! Your courage is admirable, but to do that, you’ll have to get through me—the Captain’s right arm and heart! I, Hyuk Mu—whoa, shit!”

*Clang!*

Hyuk Mujin had charged in with a grand entrance, only to stumble back in a panic when an unexpectedly stronger enemy counterattacked.

“Uh, does that guy know how to fight without running his mouth?”

“You should start by keeping yours shut.”

*Thrust!*

Song Ilseom and… wait, who was that black, shaggy old guy? Together, they saved Hyuk Mujin and cut down the remaining enemies in a flash.

“The Seven Masters of the Black Horse?”

The four syllables suddenly slipped out of my mouth. The middle-aged man, a former mounted bandit, twisted his already fearsome face.

“Not Black Horse—White Horse! I’m Ma Junggeol, eldest of the Seven Masters of Baekma Bang! Who do you think I went through all this shit for? And you forgot me…!”

“Lower your voice. While I’m asking nicely.”

At Ju Hwaran’s chilling warning, Ma Junggeol clamped his mouth shut. A laugh escaped me before I knew it.

Just because it was nice to see.

Because I knew we hadn’t lost anyone.

And…

Because I could see the one last person I’d thought I’d never meet again.

“You made it?”

At my abrupt question, Sama Pyo, who I hadn’t even seen arrive, shrugged.

“Am I late?”

No.

Not at all.
```

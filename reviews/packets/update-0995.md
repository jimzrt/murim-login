<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0995.txt",
      "sha256": "19f50e900c74aee615f104ce2e04bac712b9205464927a97573838671b856258",
      "bytes": 12743
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "1621369f74e74f66494747af39bfa454d3b6d2b21fb188f1e25a78fbf89e75fe",
      "bytes": 1406
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "d13308fe31a2c64daebd8b79b1737ef2a4f6a2f6e86338670363f6d7acf5174f",
      "bytes": 236719
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "4fb64bc751859f44d851dbc0009bf1965ff9e9af98fe9c5add5738ac009aaa2c",
      "bytes": 1374
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "69e0a6a68bc9bc2c1f55ef5db26f04928f3def99adbda937bed6f85461b91b0b",
      "bytes": 1391
    },
    {
      "path": "characters/Jin Wikyung.md",
      "sha256": "06d8748733f62fe02c681db02d2b9869ca2b13476fed45b481b637ca37dc2ded",
      "bytes": 1178
    },
    {
      "path": "characters/Ju Hwaran.md",
      "sha256": "396d4d829f4f43a3414199ea44d856ce6de929f663f93920dfb11c0af5e3a56b",
      "bytes": 973
    },
    {
      "path": "characters/Namho.md",
      "sha256": "d59db922d21060075966294fe9811ea199ce8bac4177cfb21f402aa4308205a8",
      "bytes": 1091
    },
    {
      "path": "characters/Pill Physician.md",
      "sha256": "a3a51ab8763ee521684a3a62f04f2ab0ed4b61edb5995457d6eb7b32ea7427e4",
      "bytes": 554
    },
    {
      "path": "characters/Sama Pyo.md",
      "sha256": "fbead472caacc06518db9bfe54879ee5bbc0d5547ec908a8309e4e87150b9b43",
      "bytes": 936
    },
    {
      "path": "characters/Song Il.md",
      "sha256": "f2fb0a061291f6ca20cdcfadb0f5ce52093439644622065d2d8a1a38c7a1ec7b",
      "bytes": 964
    },
    {
      "path": "characters/Song Ilseom.md",
      "sha256": "863330174c41e402dd96ff283b383a8a502d826af6334cd04df8d12ddbd94d5b",
      "bytes": 1074
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "3b3b5ab38754c929a4c4408a71d43d7827e26bc1a832c703c40945f31cb2b237",
      "bytes": 685
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "bd5753e5df794eedf5b2ea27975a392475eb9bba5427ebd9beecb42050b7771b",
      "bytes": 273611
    }
  ],
  "estimated_tokens": 13030
}
-->

# Durable State Update — Chapter 995

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
1 and safe_through 995. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 995. Profile updates may replace only one
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
  "chapter": 995,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 995,
    "continuity_sources": [995],
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
    "Taekyung is resolved to repay the dead by helping bring about the peace they wanted; he aspires to reach the upper dantian.",
    "The System has forced Taekyung to proceed with the Unknown Voice Quest, whose objective is to continue surviving.",
    "Taekyung suspects the Martial God may have been a System user, or Player, and may be the unknown voice's owner; these are unconfirmed hypotheses.",
    "Logout has been temporarily disabled following a System error, preventing Taekyung from returning to the modern world as planned.",
    "Taekyung intends to investigate Cheon Taemin and the Doppelganger's final words when he can return to the modern world."
  ],
  "continuity_sources": [
    993,
    994
  ],
  "open_questions": [
    "Who was the unknown voice, and will Taekyung meet its owner?",
    "Was the Martial God a System user, and is he connected to Cheon Taemin?",
    "What did the Doppelganger mean by its final words, and what was it trying to accomplish?",
    "What are Dark Heaven and the Lord of Heaven planning?",
    "What does the Bow Saint know about the chosen one?"
  ],
  "safe_through": 994,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진위경    | **Jin Wikyung**    |
| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 송일     | **Song Il**        |
| 주화란    | **Ju Hwaran**      |
| 소림     | **Shaolin**                      |
| 무림맹    | **Murim Alliance**               |
| 암천     | **Dark Heaven**                  |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 마교     | **Demonic Cult**                                 |                                                       |
| 중원     | **Central Plains**                               |                                                       |
| 강호     | **martial world**                                | Prefer “Murim” where the setting itself is meant      |
| 생도     | **cadet**                                    |
| 은인     | **Benefactor**                               |
| 상태               | **Status**                     |
| 퀘스트              | **Quest**                      |
| 로그아웃             | **Logout**                     |
| 산서     | **Shanxi**             |
| 하남     | **Henan**              |
| 화산     | **Huashan**            |
| 구화산    | **Mount Jiuhua**       |
| 정마대전   | **Great Faction War**         |
| 본문      | **our sect / this sect**                                        |
| 공자      | **Young Master**                                                |
| 소저      | **Young Lady**                                                  |
| 남호 | **Namho** | Hidden Shadow Pavilion code name; literally associated with amber from the south. |
| 환의 | **Pill Physician** | Title of the current Family Head of the Seongsu Jang Family. |
| 사마표 | **Sama Pyo** | Young Sect Leader of the Black Dragon Demon Gate. |
| 송일섬 | **Song Ilseom** | Young escort captain of the Yongbong Escort Bureau; distinct from Song Il of Zhongnan. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 전서응 | **messenger eagle** | Emergency courier used by the Lower District Sect. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 환골탈태 | **Bone Transformation** | Advanced transformation described as optional in martial-arts novels. |
| 소림사 | **Shaolin Temple** | Temple invoked in Chulwoo’s comparison of Baek Museong’s conduct. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 일각 | **fifteen minutes** | Quarter of a shichen; used for the remaining completion time. |
| 노환 | **infirmities of old age** | Jeok Cheongang's age-related illness. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 천마신교 | **Heavenly Demon Divine Cult** | The Demonic Cult's self-styled formal name. |
| 은영각 | **Hidden Shadow Pavilion** | Former Murim Alliance intelligence organization. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 러시아 | **Russia** | Country associated with Sorkovache and the imperial-style sofa. |
| 화란 | **Hwaran** | Familiar short form of Ju Hwaran. |
| 유엽도 | **willow-leaf saber** | Saber wielded by Song Ilseom. |
| 신교 | **Divine Cult** | Short form used by the Divine Cult's members for the Heavenly Demon Divine Cult. |
| 악귀 | **Fiend** | Descriptive epithet applied to the First Fiend. |
| 교주 | **Cult Leader** | Leader of the Divine Cult. |
| 도산검림 | **a mountain of sabers and a forest of swords** | Idiom describing the lethal life of martial artists. |
| 신인 | **divine man** | Descriptive term for a human who became something beyond humanity. |
| 전서 | **missive** | A written message exchanged or delivered in secret. |
| 신강 | **Xinjiang** | Region beyond Qinghai described as the domain of the Demonic Path. |
| 상산후 | **Marquis of Shangshan** | Title bestowed on Jin Taekyung by the Emperor. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혁무진 | 진위경 | Jin Family subordinate to Lesser Family Head | Lesser Family Head | deferential | Uses 소가주님 while confessing that he accepted Taekyung's invitation. |
| 진위경 | 혁무진 | Lesser Family Head to direct family subordinate | you | formal-but-familiar | Uses 자네 while recognizing Mujin and instructing him to keep helping Taekyung. |
| 혁무진 | 적천강 | subordinate_to_overwhelming_elder | Great Hero Jeok | deferential and fearful | Mujin uses 적 대협 while reporting Jeok’s orders and Taekyung’s awakening. |
| 적천강 | 혁무진 | overwhelming_elder_to_junior_martial_artist | you stupid fool | blunt and mocking | Jeok calls Mujin a 멍청한 놈 after knocking him down during the attempted escape. |
| 진위경 | 송일 | Jin Family host to visiting Zhongnan Elder | Senior | formal and guarded | Jin Wikyung respectfully asks Song Il's name before the dispute escalates. |
| 송일 | 적천강 | former rescued junior to former rescuer | Great Hero Jeok | formal, fearful, and defensive | Uses 적 대협 while insisting that Jeok has no business interfering in the dispute. |
| 적천강 | 송일 | former rescuer to former rescued junior | Zhongnan brat; you; insolent bastard | blunt, mocking, and humiliating | Jeok recalls Song's youthful arrogance and addresses him with contempt while publicly disciplining him. |
| 진위경 | 적천강 | host_to_legendary_guest | Great Hero Jeok | formal-deferential | Introduces himself and pays respects to Jeok Cheongang as the Fire King. |
| 적천강 | 진위경 | elder_to_younger_family_head | you | gruff and teasing | Uses 자네 while mistaking Wikyung for Taekyung’s father and questioning his age. |
| 송일섬 | 주화란 | escort_captain_to_young_bureau_head | Hwaran | urgent and familiar | Calls out 화란아 while urgently warning Ju Hwaran before stepping into the confrontation. |
| 주화란 | 혁무진 | rescued_survivor_to_benefactor | Benefactor | formal-deferential | Hwaran includes Mujin among the Benefactors when greeting Taekyung's companions. |
| 주화란 | 송일섬 | bureau_head_to_escort_captain | Captain Song | formal and prosecutorial | Uses his office title, then his personal name, while exposing and confronting him. |
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
| 주화란 | 태산 | pavilion_member_to_pavilion_member | Young Hero Taishan | formal but stern | Ju Hwaran reprimands Taishan for speaking ominously about Jin and warns that she will muzzle him. |
| 혁무진 | 주화란 | Fire Dragon Pavilion member to fellow member | Young Lady Ju | polite and deferential | Mujin addresses Hwaran as 주 소저 while asking her to call a physician. |
| 주화란 | 적천강 | younger ally to legendary martial master | Great Hero Jeok | formal and deferential | Ju Hwaran addresses Jeok as 적 대협 while asking whether he is all right. |
| 남호 | 적천강 | junior_to_senior | Senior | respectful and formal | Namho refers to Jeok as 노선배님 while agreeing with him. |

## Listed compact profiles

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 994
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and an active member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented; despite being naturally fearful, he faces danger and remains loyal to the person he serves, with irreverent self-deprecation and a taste for glory. He is suspicious of Taekyung, bluntly critical of the family's disgraced third son, and an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; with Taekyung, blunt and occasionally incredulous, while using breezy, irreverent banter to defuse tense situations.
- **Relationships:** He is loyal to Taekyung, who trusts him to act independently, especially in his home region of Shanxi and at the Jin Family of Taiyuan. As a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Fire Dragon Pavilion members accompanying Taekyung. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 994
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; believes there is no absolute justice and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, and insists on protecting Taekyung while urging him not to risk his life; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy.

### Jin Wikyung.md

# Jin Wikyung (진위경)

- **Safe through:** Chapter 994
- **Aliases:** Junzi Sword
- **Role:** Jin Wikyung is the thirty-six-year-old Lesser Family Head and future Family Head of the Jin Family of Taiyuan, the Alliance Leader who unified Shanxi Murim and Shanxi Province's foremost landowner and magnate.
- **Personality:** Calm and politically capable, Jin Wikyung takes responsibility for his people and prioritizes their lives; he uses calculated leverage to keep dangerous allies in line and commits firmly to his principles, even when doing so means remaining in a losing battle.
- **Voice:** Restrained, formal, and commanding with subordinates; openly affectionate, proud, and occasionally exuberant with Taekyung.
- **Relationships:** Jin Wikyung is Taekyung’s eldest brother and future Family Head, protects and mentors him, and commands the Jin Family’s forces; Jin Mukyung is his younger brother, and he considers the Jin Family indebted to the Dongting Fisherman and the other fallen defenders of Shanxi.

### Ju Hwaran.md

# Ju Hwaran (주화란)

- **Safe through:** Chapter 943
- **Aliases:** Hwaran
- **Role:** Ju Hwaran is a Level 88 Young Bureau Head, leader of the Yongbong Escort Bureau, an experienced Nanman guide, and an active member of the Fire Dragon Pavilion.
- **Personality:** Intelligent, capable, responsible, and filial; remains controlled under pressure but has grown more assertive and openly impatient after the hardships she has endured.
- **Voice:** Clear, polite, restrained, and determined.
- **Relationships:** Escort King Ju Gongsan was her paternal grandfather, Ju Hogun is her father, Heo Jun was her uncle, Sama Pyo was her former fiancé in a political engagement she accepted for her father's sake, Song Ilseom is her direct escort who accompanied her previous journey to Yeongin, and Jin Taekyung is a trusted ally; the Yongbong Escort Bureau has longstanding ties with Yeongin’s inhabitants.

### Namho.md

# Namho (남호)

- **Safe through:** Chapter 983
- **Aliases:** Elder Chao
- **Role:** Namho is an eighty-year-old non-Han Hidden Shadow Pavilion agent who spent more than fifty years undercover in Nanman and maintained contact with Central Plains intelligence through the Pavilion’s Hidden Thread; he guides the Fire Dragon Pavilion and represents Jin Taekyung and the Murim Alliance in negotiating the survivors’ chance to rebuild the Murong household.
- **Personality:** Duty-bound, pragmatic, and observant; uses theatrical violence to protect intelligence work and takes a veteran’s concern for the younger generation’s resolve.
- **Voice:** Measured and reflective when advising the younger generation, loudly abusive when maintaining his local cover, and capable of theatrical boasts and dry humor.
- **Relationships:** Namho is a Hidden Shadow Pavilion contact for Jin Taekyung and the Fire Dragon Pavilion, receives intelligence from the Pavilion Master, and knows the code used by the Thousand-Faced Fox.

### Pill Physician.md

# Pill Physician (환의)

- **Safe through:** Chapter 936
- **Aliases:** None
- **Role:** Current Family Head of the Seongsu Jang Family in Shandong, who personally placed and signed the Thousand-Year Snow Ginseng in the casket entrusted to the Yongbong Escort Bureau.
- **Personality:** No personality traits are established.
- **Voice:** No voice traits are established.
- **Relationships:** The Pill Physician heads the Seongsu Jang Family, a prestigious medical family in Shandong.

### Sama Pyo.md

# Sama Pyo (사마표)

- **Safe through:** Chapter 943
- **Aliases:** Black Dragon Saber
- **Role:** Young Sect Leader of the Black Dragon Demon Gate, a Morning Star reputed to be no less than the Ten Dragons and Phoenixes, and a member of the Fire Dragon Pavilion.
- **Personality:** Outwardly courteous and smiling, inwardly calculating, but genuinely protective of Taishan; in combat he is ruthlessly pragmatic, survival-focused, and unafraid to stake his life.
- **Voice:** Polite and ingratiating in public, with sardonic humor and controlled evasiveness.
- **Relationships:** Sama Pyo commands the absolutely loyal Taishan, is Sima Gong's son, was Ju Hwaran's former fiancé in a political engagement, and has joined the Fire Dragon Pavilion while openly intending to use Jin Taekyung as a useful card; he is now openly hostile toward fellow member Song Ilseom.

### Song Il.md

# Song Il (송일)

- **Safe through:** Chapter 943
- **Aliases:** Roaring Fury Swordsman
- **Role:** Elder of the Zhongnan Sect and the Roaring Fury Swordsman; senior brother of Sect Leader Gong Iljung; came to the Jin Family of Taiyuan to demand redress for Gong Ilhyuk's injury and the alleged insult to Zhongnan; attacked Jin Taekyung with the Heavenly River Thirty-Six Swords, was stopped by Jeok Cheongang, and was publicly humiliated by him.
- **Personality:** Arrogant, domineering, punitive, and confident in his martial power and seniority.
- **Voice:** Gruff, cutting, condescending, and threatening, with formal authority used to pressure those beneath him.
- **Relationships:** Gong Iljung is his junior Sect Leader and martial younger brother; Gong Ilhyuk is a junior Disciple of his sect; he recognizes Baek Museong and Cheongpung through their Huashan and Sword Saint connections.

### Song Ilseom.md

# Song Ilseom (송일섬)

- **Safe through:** Chapter 943
- **Aliases:** Escort Captain Song
- **Role:** Level 110 young escort captain of the Yongbong Escort Bureau, one of its Dragon-Phoenix Three Escorts, and a newly accepted member of Jin Taekyung and Cheongpung’s Fire Dragon Pavilion; he is currently bound and unconscious under the reconnaissance squad's guard after being struck at a Sleep Acupoint.
- **Personality:** Blunt, decisive, survival-hardened, and dryly self-aware, with little patience for insults or disorder and practical survival skills such as making disguise masks.
- **Voice:** Forceful and urgent in command, with a rough and confrontational edge.
- **Relationships:** He serves under Ju Hwaran and has expressed concern that she not be hurt or die needlessly; he is Song Pyosan’s son, his grandmother was the surviving Guangdong Chen child rescued by Ju Gongsan during the Great Faction War, and he remains openly hostile toward fellow Fire Dragon Pavilion member Sama Pyo.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 990
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo; becomes explosively violent when his meat is threatened.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord, trusts Jin Taekyung as Pavilion Master, and has grown attached to the Fire Dragon Pavilion members.

## Korean source

```text
＃995화



어떤 종류의 대화에는 굳이 많은 말이 필요하지 않다.

시급을 다투는 일일수록 더더욱.

오늘의 내게는 갑작스럽게 침소를 찾아온 진위경과의 대화가 그랬다.

일각도 되지 않는 짧은 시간 동안 이어진 대화.

그러나 그 안에 담겨 있던 내용은 만근 거석처럼 무거웠고, 나는 진위경이 떠난 즉시 사람들을 불러모았다.

이 대화에 실린 막중한 무게를 나와 함께 감당할 수 있는 이들을.

드르륵.

“거 참, 오래 살고 볼 일이군. 우리 같은 강호의 무뢰배들이 상산후(上山后)의 존안을 뵙는 날이 오다니.”

문이 열리자마자 실없는 농담을 던지는 남호를 보자, 나도 모르게 헛웃음이 흘러나왔다.

이유는 두 가지였다.

첫 번째는 오랜만에 마주하는 듯한 남호, 아니 그들 모두의 모습이 반갑고 편안해서.

두 번째는 당연하다는 듯이 태산의 어깨에 목말을 타고 앉아있는 남호의 모습이 우스꽝스러워서.

“아니, 지금 뭐 하세요?”

“뭐하긴. 보면 모르나? 앉아 있지.”

“그건 알겠는데, 왜 하필 거기에 앉아 있는지 여쭤보는 겁니다.”

“그 질문에는 아주 간단하게 대답할 수 있지. 엄청나게 편하거든. 이놈 아주 물건이야, 물건.”

세상을 뒤바꿀 뭔가를 발견한 세기의 발명가처럼 흐뭇하게 웃어 보인 남호가 태산의 정수리를 탁탁 두드렸다.

“뭣 하느냐. 어서 들어가지 않고.”

열린 문 앞에서 멀뚱멀뚱 서 있던 태산이 슬쩍 먼 산을 쳐다보며 대답했다.

“태산이. 발이 안 움직인다. 아무래도 배고파서 그런 것 같다.”

“뭔 개소리냐. 고작 일각 전에 네놈 주둥이로 들어간 육포만 따져도 송아지 한 마린데.”

“…….”

요금제 운행이었던 모양이다.

그것도 연비가 엄청나게 구린.

“기억 안 난다. 배고프다.”

“이런 천하의 아귀 같은 놈을 봤나…….”

한숨을 푹 내쉰 남호가 소매춤에서 당과 하나를 꺼내서 태산의 눈앞에 흔들었다.

“자, 이제 됐느냐?”

그 순간, 태산의 눈꼬리가 더할 나위 없이 날카로워졌다.

“겨우 하나?”

“빌어먹을, 돌아가는 대로 하나 더 주마.”

“세 개.”

“날강도 같은 놈. 어림도 없다. 두 개. 마지막 제안이니 잘 생각해 보고 결정하거라.”

태산의 눈동자가 흔들리던 그 순간, 녀석의 거대한 몸뚱어리 뒤로 잠깐의 갈등을 끝내 줄 누군가의 목소리가 들려왔다.

“당장 썩 비켜요. 그렇지 않으면 제 손으로 직접 칼침 두 방씩 놔 드릴 테니까.”

“……!”

“……!”

“왜, 칼침 두 방으로도 부족해요? 세 방씩 놔 드려요?”

나직하면서도 침착한 음성.

그래서인지 몰라도 더 위험하게 느껴지는 경고에, 마른침을 꿀꺽 삼킨 태산이 후다닥 방 안으로 들어왔다.

남호가 눈앞에 대고 흔들어 대던 당과도 잊지 않고 낚아채는 철두철미함까지 보이며.

그리고 그제야 훤히 드러난 입구를 통해, 이 러시아워를 단번에 마무리 지은 주화란이 빠른 걸음으로 다가왔다.

언제 그랬냐는 듯 먹먹해진 목소리로 나를 부르며.

“진 공자님! 아니, 은인! 아니, 각주님!”

“…….”

하나만 정해서 하자고 몇 번이나 부탁했던 것 같은데.

이 상황이 웃기기도 하고, 한편으로는 난데없는 주화란의 태세 전환에 당황한 내가 우왕좌왕하는 사이 그녀는 눈물까지 글썽였다.

“지난번 전투에서 너무 늦게 도착해서 죄송해요. 많이 힘드셨죠?”

주화란의 어깨너머, 투명 인간처럼 서 있던 사마표가 혼잣말처럼 중얼거렸다.

“모르긴 몰라도 아마 적들이 더 힘들었을 것 같은데.”

언제나처럼 유엽도(柳葉刀)를 품에 안은 채 팔짱을 끼고 있던 송일섬도 고개를 끄덕였다.

“싸운 흔적을 보니 괴물이 따로 없더군. 전부 뼈도 못 추렸어.”

이를 악문 채 등 뒤에서 들려 오는 목소리들을 무시한 주화란이 계속해서 말을 이었다.

“다치신 곳은요? 이제 괜찮나요?”

사마표와 송일섬은 그나마 눈치가 있는 편이었다.

적어도 다음 순간, 혁무진처럼 눈치 없이 끼어들지 않고 적절한 시기에 빠졌으니까.

“아니, 주 소저. 엊그제 환골탈태한 사람한테 무슨 몸 상태를 물어보…….”

그 순간, 싸늘한 공기가 사방에 내려앉았다.

천천히 고개를 돌린 주화란이 무슨 표정을 짓고 있었는지는 모르겠지만, 흐려지는 말꼬리와 함께 공포로 물드는 혁무진의 얼굴을 본 나는 앞으로도 영원히 모른 채 살리라 다짐하며 입을 열었다.

“무진이, 방정맞은 주둥이 다물고. 주 소저, 저는 괜찮습니다. 아주 멀쩡하니까 걱정하실 필요 없어요. 그리고 태산이. 지금부터 중요한 이야기를 해야 하니까 입안에 든 당과부터 얼른 삼키…… 아, 벌써 다 먹었구나. 혹시 씹은 게 아니라 마셨니?”

당과 액체설을 의심케 하는 태산의 깜짝 마술쇼를 끝으로 교통정리를 끝마친 내게, 남호가 떨떠름한 눈빛을 보냈다.

“중요한 얘기라, 어째서인지 벌써부터 굉장히 불길하게 느껴지는데…… 내 단순한 노파심인가?”

“단지 그뿐이라면 얼마나 좋을까.”

내가 한 말이 아니다.

이 자리의 마지막 손님. 적천강이 방 안으로 성큼 들어서며 나를 향해 고개를 까딱였다.

“모두에게 알려 주어라. 지금 산서성 밖에서 무슨 일이 벌어지고 있는지.”

착 가라앉은 눈빛은 그 역시 나와 같은 소식을 들었다는 증거.

어느덧 침소를 가득 채운 사람들을 말없이 차례차례 응시하던 나는, 마침내 굳게 닫혀 있던 입술을 뗐다.

“서쪽에서, 심상치 않은 일들이 벌어지고 있습니다.”

“서쪽? 서쪽이라면 정확히 어디…….”

운을 떼자마자 가장 먼저 반응한 사람은 예상대로 남호였다.

미간을 찡그린 채 말을 이어 가던 그의 가느다란 눈매가, 문득 크게 부풀어 올랐다.

“서, 설마?”

“네. 지금 생각하시는 그곳이 맞습니다.”

나는 고개를 끄덕였다. 그리고 무거운 목소리로 내뱉었다.

서쪽의 끝자락, 중원에서는 마교(魔敎)라 불리는 천마신교의 발원지이자 이제는 암천의 본거지가 된 그 저주받은 땅을.

“신강(新疆).”

“……!”

“……!”

거대한 충격이, 보이지 않는 파도가 되어 좌중을 휩쓸었다.



* * *



무림(武林)이라 불리는 천하 속의 또 다른 세상은, 그리고 그 안에서 살아가는 무림인이란 존재는 언제 탄생한 것일까.

그 정확한 시기는 아무도 모른다.

다만 입과 입을 통해서 전해져 내려오는 구전(口傳)과 몇 줄 남지 않은 아득한 과거의 기록을 살펴보았을 때, 하남의 소림사가 이 기나긴 무림사의 첫 단추를 끼웠다고 주장하는 이들이 많았고 그것이 곧 정설로 굳혀졌다.

물론, 구화산에서 한창 뼈와 살을 깎는 고된 수련을 거듭할 무렵 적천강이 해 주었던 말은 달랐지만.



‘역사라는 것은 결국 다듬어지고 짜 맞춰지기 마련이다. 저마다 믿고 싶은 대로 믿는 게지. 자기들 입맛에 맞는 것으로.’



당시만 하더라도 노환을 앓고 있던 적천강은 과거를 회상하는 일들이 많아졌다. 아니, 사실 반쯤은 내 간곡한 권유였다.

틈날 때마다 남아 있는 기억을 떠올리고 되짚을수록, 노환의 진행이 더뎌진다는 토막 상식을 어디선가 본 것 같았기 때문이다.

그리고 적천강의 방대한 지식 속에는, 세상에 널리 알려지지 않은 무림의 비사(祕史) 또한 포함되어 있었다.



‘빛과 어둠은 떼놓을 수 없는 단짝이다. 부처가 되겠다는 놈들이 득실거리는 소림에서 무공이 탄생했다는 것부터가 우습기 짝이 없지만, 그 강대한 힘을 좋지 않은 방향으로 이용하려는 것들이 없었겠느냐?’

‘그럼 지금 하시는 말씀이 혹시…….’

‘그래, 본문의 사조들께서 남기신 기록에 의하면 마교(魔敎) 역시 그렇게 탄생했다. 정확한 시기는 몰라도 아마 소림사와 비슷한 시기였겠지.’



무림이라는 도산검림의 세계가 형성된 것은 그만큼 혼란스러운 난세였기 때문에 가능했던 일.

소림사의 무승들은 지키기 위한 수단으로 무공을 익혔으나, 이 놀라운 힘을 접한 누군가는 천하를 제패하는 수단으로 무공을 익혔다.



‘사방 각지에서 온갖 인간군상들이 구름처럼 모여들었겠지. 무공을 이용해 도무지 인간 같지도 않은 신묘한 힘을 발휘하니, 그들이 느꼈을 놀라움이 오죽했겠느냐.’



분명 처음에는 수십여 명에 불과했을 것이다.

해가 떠 있어도 어두컴컴하기 그지없는 현실 속, 거대한 빛과도 같은 힘을 접한 그들은 이내 추종자가 되어 사방으로 퍼져나갔을 것이다.

두 눈으로 똑똑히 목격한 그 놀라운 광경을 입을 통해 전하고, 아무리 말해도 믿지 못하는 이들의 소맷자락을 붙잡고 이끌었다.

믿을 수 없는 힘을 지닌 그에게. 이 지긋지긋한 난세에서 자신들을 지켜 줄 우두머리에게.

그렇게 모여든 추종자들이 수백이 되고, 이내 수천을 넘어서고, 마침내 십만에 달하자 우두머리는 스스로를 교주이자 하늘이 내린 신인(神人)으로 칭했다.



‘그것이 천마(天魔)의, 마교의 시작이었다.’



더불어 적천강은 말했다.

처음부터 천마요, 마교를 칭하진 않았을 것이라고.

다만 중요한 것은 최초의 천마가 끝끝내 천하를 제패하지 못한 채, 자신을 따르는 추종자들과 함께 서쪽 변방의 사막에 자리 잡았다는 것이었다.

그 후 천년에 가까운 세월이 흐를 때까지 그들은 때때로 서로를 향해 칼날을 휘둘렀고, 몇 번의 분열을 거쳐 통합되자 정마대전이라는 대환란을 일으키기도 했다.

그리고 그 기나긴 세월 동안 악귀들의 절대적인 지배하에 놓인 열사(熱砂) 사막은, 중원 무림조차 넘볼 수 없는 멸지(滅地)가 되었다.

암천이라 불리는, 새로운 그림자가 사막에 드리워진 지금까지도.

그런데…….

“바로 그 신강에서, 지금껏 없었던 움직임이 보이고 있다?”

짧은 이야기가 끝난 후 길게 이어지던 침묵.

그 고요함을 깨트린 남호의 물음에 나는 고개를 끄덕였다.

“들으신 대롭니다.”

“정보의 출처는?”

“어디겠습니까.”

손가락을 들어 위를 가리키자, 남호가 탄식하듯 중얼거렸다.

“무림맹…… 아니, 은영각(隱影閣)이로군.”

“삼십여 명의 정예 요원이 희생됐다고 하더군요. 그마저도 처음이자 마지막 전서응을 끝으로 연락이 끊겼고.”

“빌어먹을. 그렇다면 더는 의심의 여지가 없겠군. 적들의 추정 숫자는?”

“그건.”

이번만큼은 나도 쉽사리 말을 잇지 못했고, 남호는 그런 내 모습에 신음했다.

“그렇군. 십만마도(十萬魔徒)의 재림인가.”

“어쩌면 그보다 많을 수도 있습니다. 적어도 제게 전해진 정보에 의하면.”

그리고 더 중요한 것은, 놈들이 오십여 년 전의 마교도들보다도 훨씬 더 강하고 끔찍한 존재들일 거라는 사실이었다.

사막의 주인은 더 이상 마교가 아니다. 암천이다.

단순히 이름만 바꾼 마교의 후신(後身) 따위가 아니라, 그보다 비교할 수 없이 강력하고 위험한 존재가 지배하는 새로운 추종자들.

‘갑자기 로그아웃이 막힌 것도, 설마 이것 때문일까.’

문득 그런 의문이 뇌리를 스쳤지만, 나는 이내 고개를 저었다.

아니다. 틀렸다.

퀘스트는 아직 발생도 하지 않았다. 왜냐하면 내가 아직 선택하지 않았기 때문에.

그리고 지금이 바로 결정을 내릴 순간이다.

“지금 이 순간부터, 우리는 서쪽으로 향합니다.”

띠링.

새로운 퀘스트를 알리는 알림이 울려 퍼졌다.
```

## Final English reading copy

```markdown
# Chapter 995

Some conversations don’t need many words.

The more urgent the matter, the less they need.

That was certainly true of my conversation today with Jin Wikyung, who’d suddenly come to my room.

It had lasted less than fifteen minutes.

But what we’d discussed had been as heavy as a massive stone, and as soon as Jin Wikyung left, I called everyone together.

The people who could help me bear the immense weight of that conversation.

Creak.

“Well, I’ll be damned. You live long enough, and you see everything. Who’d have thought a bunch of martial-world lowlifes like us would live to see the face of the Marquis of Shangshan?”

Namho tossed out a silly joke the moment the door opened, and I couldn’t help but chuckle.

For two reasons.

First, because seeing Namho again—or rather, seeing all of them again—felt like a relief. It was almost as if I hadn’t seen them in ages.

Second, because Namho was sitting astride Taishan’s shoulders as though that were the most natural thing in the world. It was ridiculous.

“What are you doing?”

“What does it look like? I’m sitting.”

“I can see that. I’m asking why you’re sitting there of all places.”

“That’s easy to answer. It’s incredibly comfortable. This guy’s a real find.”

Namho smiled with the satisfaction of a great inventor who’d discovered something that could change the world, then patted Taishan on the crown of his head.

“What are you waiting for? Get inside.”

Taishan stood blankly in the open doorway, then glanced off into the distance before answering.

“Taishan. Feet won’t move. Must be hungry.”

“What the hell are you talking about? The jerky you stuffed into your mouth barely fifteen minutes ago amounted to a whole calf.”

“……”

Apparently, he ran on a pay-as-you-go plan.

And one with terrible mileage, at that.

“Don’t remember. Hungry.”

“Good grief. You’re a gluttonous demon if I ever saw one…”

With a deep sigh, Namho pulled a piece of taffy from his sleeve and waved it in front of Taishan’s eyes.

“There. Happy now?”

In that instant, Taishan’s eyes narrowed to razor-sharp slits.

“Just one?”

“Damn it. I’ll give you another as soon as we get back.”

“Three.”

“You little bandit. No way. Two. That’s my final offer, so think carefully before you decide.”

Just as Taishan’s eyes began to waver, a voice sounded from behind his huge body, putting an end to his hesitation.

“Move. Right now. Otherwise, I’ll personally stab each of you twice.”

“……!”

“……!”

“What, two knives each still isn’t enough? Should I make it three?”

Her voice was quiet and composed.

Maybe that was why the warning felt even more dangerous. Taishan swallowed hard, then hurried into the room.

He even snatched the taffy Namho had been waving in front of him, displaying a thoroughness I could only admire.

Only then was the entrance clear. Ju Hwaran, who’d brought the rush-hour traffic to an abrupt stop, strode toward me.

Her voice had grown thick with emotion, as if nothing had happened.

“Young Master Jin! No, Benefactor! No, Pavilion Master!”

“……”

I was pretty sure I’d asked her several times to pick just one.

The situation was funny, but Ju Hwaran’s sudden change in attitude also caught me off guard. While I floundered, she even teared up.

“I’m sorry I arrived so late during the last battle. You must’ve had such a hard time.”

Over Ju Hwaran’s shoulder, Sama Pyo stood like an invisible man and muttered to himself.

“I’d guess the enemies had a harder time.”

Song Ilseom, arms crossed and his willow-leaf saber tucked against his chest as always, nodded.

“From the signs of the fight, he was a monster. None of them stood a chance.”

Jaw clenched, Ju Hwaran ignored the voices behind her and continued.

“Were you hurt? Are you all right now?”

Sama Pyo and Song Ilseom at least had some sense.

They both slipped away at the right moment instead of butting in without a clue like Hyuk Mujin was about to.

“No, Young Lady Ju. Why are you asking about the condition of someone who went through Bone Transformation just the other day—”

A chill settled over the room.

I didn’t know what expression Ju Hwaran had on her face as she slowly turned around, but I saw terror spread across Hyuk Mujin’s face as his voice trailed off. I decided I’d go on living without ever finding out.

“Mujin, shut your blabbering mouth. Young Lady Ju, I’m fine. Completely fine, so there’s no need to worry. And Taishan, I need to talk about something important, so hurry up and swallow the taffy in your mouth—oh, you already finished it. Did you chew it, or did you drink it?”

After Taishan’s startling magic trick, which made me wonder if taffy came in liquid form, I finished sorting out the traffic. Namho gave me a dubious look.

“Something important, huh? For some reason, I already have a very bad feeling about this… Am I just being an old worrywart?”

“If that were all, how nice that would be.”

I wasn’t the one who said it.

The last guest in the room stepped inside. Jeok Cheongang gave me a nod.

“Tell everyone what’s happening beyond Shanxi Province.”

His sunken gaze told me he’d heard the same news I had.

By now, the room was full. I silently looked around at everyone, one by one, then finally parted my tightly shut lips.

“Something’s happening in the west.”

“The west? Where exactly in the west…?”

As expected, Namho was the first to react. He furrowed his brow as he began to ask, then his narrow eyes suddenly widened.

“D-Don’t tell me…”

“Yes. It’s where you’re thinking.”

I nodded, then spoke in a heavy voice.

The far western edge, the birthplace of the Heavenly Demon Divine Cult—called the Demonic Cult in the Central Plains—and now the home base of Dark Heaven. That accursed land.

“Xinjiang.”

“……!”

“……!”

A massive shock swept through the room like an invisible wave.



* * *



When did the other world within the world—known as Murim—and the martial artists who lived in it first come into being?

No one knew for sure.

But according to oral traditions passed down from one person to another, and the few lines left in records from the distant past, many claimed that Shaolin Temple in Henan had set this long history of Murim in motion. Before long, that claim had become accepted as fact.

Of course, what Jeok Cheongang had told me while I was undergoing grueling training on Mount Jiuhua had been different.

*“History is always shaped and pieced together in the end. People believe whatever they want to believe—whatever suits their taste.”*

Back then, Jeok Cheongang had been suffering from the infirmities of old age, and he’d begun reminiscing about the past more often. Or, to be more accurate, I’d half-begged him to.

I thought I’d once read somewhere that bringing up and revisiting old memories whenever you had the time could slow the progression of age-related illness.

And Jeok Cheongang’s vast knowledge included hidden histories of Murim that weren’t widely known.

*“Light and darkness are inseparable companions. It’s absurd enough to claim martial arts were born in Shaolin, where people who want to become Buddhas are packed together. But do you really think no one tried to use that great power for evil?”*

*“Then what you’re saying is…”*

*“That’s right. According to records left by the founders of our sect, the Demonic Cult came into being the same way. We don’t know the exact date, but it was probably around the same time as Shaolin Temple.”*

The world of Murim, a mountain of sabers and a forest of swords, had formed in an age of such chaos that it could hardly have happened any other way.

The Shaolin monks learned martial arts as a means of protecting others. But when someone else encountered that astonishing power, they learned martial arts as a means of conquering the world.

*“People of every stripe must’ve gathered from all directions, in droves. They used martial arts to wield such mysterious power that they hardly seemed human. Just imagine how astonished everyone must’ve been.”*

There must’ve been only a few dozen at first.

In a world that remained dark even beneath the sun, they’d encountered a power like a great light. Before long, they became followers and spread in every direction.

They told others of the astonishing sight they’d witnessed with their own eyes, then grabbed the sleeves of those who refused to believe them and led them there.

To the man with that unbelievable power. To the leader who would protect them in this wretched age of chaos.

The followers who gathered around him grew from hundreds to thousands, then finally to a hundred thousand. At last, their leader declared himself the Cult Leader and a divine man sent by Heaven.

*“That was the beginning of the Heavenly Demon and the Demonic Cult.”*

Jeok Cheongang had also said that they probably hadn’t called themselves the Heavenly Demon or the Demonic Cult from the very beginning.

What mattered was that the first Heavenly Demon had never managed to conquer the world. Instead, he and his followers had settled in the desert on the western frontier.

For nearly a thousand years after that, they sometimes turned their blades against one another. After several splits and reunifications, they eventually brought about the Great Faction War, a calamity on an enormous scale.

Throughout those long years, the scorching sands ruled absolutely by Fiends became a wasteland that even Murim of the Central Plains couldn’t hope to challenge.

And they remained so even now, with a new shadow called Dark Heaven cast across the desert.

“And now something unprecedented is happening in Xinjiang?”

After the short account came a long silence.

Namho’s question broke the quiet. I nodded.

“That’s what I heard.”

“Where did the information come from?”

“Where do you think?”

I pointed upward with a finger, and Namho murmured as if letting out a sigh.

“The Murim Alliance… No, the Hidden Shadow Pavilion.”

“I heard thirty-odd elite agents were killed. Their contact was cut off after the first and last messenger eagle they sent.”

“Damn it. Then there’s no room left for doubt. What’s the estimated number of enemies?”

“That…”

For once, I couldn’t bring myself to continue easily. Namho groaned at the sight of me.

“I see. The return of the Hundred Thousand Demonic Disciples.”

“There may be even more. At least, that’s what the information I received suggests.”

And what mattered more was that they were far stronger and more horrifying than the Demonic Cult’s followers had been fifty years ago.

The desert no longer belonged to the Demonic Cult. It belonged to Dark Heaven.

They weren’t merely the successors of the Demonic Cult under a different name. They were a new group of followers, ruled by a power incomparably stronger and more dangerous.

*Could this be why Logout was suddenly blocked?*

The thought crossed my mind, but I soon shook my head.

No. That was wrong.

The Quest hadn’t appeared yet. Because I hadn’t chosen yet.

And now was the moment to make that choice.

“From this moment on, we’re heading west.”

Ding.

An alert rang out, announcing a new Quest.
```

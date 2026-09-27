<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1071.txt",
      "sha256": "05b2e4d443b49813417ecd8a580863a08d9fbcdab5b411ebf2ef6c59ff88c61a",
      "bytes": 13904
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "0d62d57427757a73efcfb2a204b6dad35b253c8442dc9da5d500d991abdc039c",
      "bytes": 1591
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "5be93eb6bd068e9f3140c82d613f582e8e72d687cb3b90fa54d2c393096f3e5c",
      "bytes": 242356
    },
    {
      "path": "characters/Blood Lord.md",
      "sha256": "befcac62f82747ee0154c726361e0388960ec9dd64ff225a848fa2b055e9402e",
      "bytes": 928
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "ec51abd3a20b322f88b4ffef49189ccf2dd344c044a8543828a9094cc1f8caa0",
      "bytes": 760
    },
    {
      "path": "characters/Hyeoncheon.md",
      "sha256": "c720d7bda0d0069d3e210df1abbc111d241c884c772a15ebf65fa92a983a8c2a",
      "bytes": 651
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "feee2f286efda5c4168da395787028ad8eb25fed966be10b74d3f257ee3cd4e4",
      "bytes": 1375
    },
    {
      "path": "characters/Hyuk Sopyung.md",
      "sha256": "2aacf1a888b1efadd98e12a79d6948ba31c928767a8e7160be8ca8517b7d22d8",
      "bytes": 619
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "16e3a1e43f1b35387ff3a58d33359084829335e53a5dc05c41e22db37903a665",
      "bytes": 1502
    },
    {
      "path": "characters/Jeong Hogun.md",
      "sha256": "b85cd7c4c1bf6fedc4f6de1e06591f4af50e7f6a4dd6feb8b85441b5da5b54e6",
      "bytes": 700
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "303819469762f6683233825723743710b591b728a1dd7753d1c0cfb82b98461c",
      "bytes": 1828
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "d04ffa3db460750957120c038efc7db1e92a46cfc0c9c1a4a31e67dc0bac7ba8",
      "bytes": 623
    },
    {
      "path": "characters/Jung Ho.md",
      "sha256": "e51b14db0653819a99c0e38231d69fab1fbf339d3e9b8206c4061499ab34bd89",
      "bytes": 700
    },
    {
      "path": "characters/Sama Pyo.md",
      "sha256": "964bb4ae952b8879bd712e162838df72b7dfa2c9f5b91198990944f5d67a0a28",
      "bytes": 850
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "7df8b2357d0faa08e63a571debd66c331206f8c9af0b11d116826f4c7dad2ad4",
      "bytes": 284375
    }
  ],
  "estimated_tokens": 13701
}
-->

# Durable State Update — Chapter 1071

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
1 and safe_through 1071. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1071. Profile updates may replace only one
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
  "chapter": 1071,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1071,
    "continuity_sources": [1071],
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
    "Jin’s allied force is retreating toward Qinghai Lake, estimated to be two days away at full effort.",
    "Jin’s force of roughly three thousand is now surrounded by coordinated enemies approaching from every direction and must break through to continue east.",
    "A giant monster’s Fear effect froze the force; Jin killed it with Fire Dragon’s Single Tail and hellfire.",
    "Faint bell sounds came from all around the encirclement.",
    "Jeong Hogun agreed to remove the Embroidered Uniform Guard’s armor, but Jin told him to keep his helmet on when the new threat approached.",
    "Ma Sanbao serves the Blood Lord and covertly watched Jin’s force; Great Sir first detected the surveillance in Ningxia.",
    "The East Depot’s network had shared its view with Dark Heaven through the Eastern Heaven Demon Lord.",
    "The Grand Mage suspects Hyeoncheon and the Kongtong survivors went to Great Sir."
  ],
  "continuity_sources": [
    1069,
    1070
  ],
  "open_questions": [
    "Who is Great Sir, and what is his connection to Hyeoncheon and the surviving Kongtong Disciples?",
    "Did Jin’s sword strike kill or otherwise affect the watching crow?",
    "Are Dark Heaven’s forces broadly composed of reanimated corpses, and has Ma Sanbao spread the Corpse Art to others?",
    "What is the Lord of Heaven seeking through Jin, and when will he appear?",
    "Who created the giant monster, and who directs the coordinated encirclement signaled by bells?"
  ],
  "safe_through": 1070,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 혁소평    | **Hyuk Sopyung**   |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 궁성     | **Bow Saint**                 | —              |
| 종남파    | **Zhongnan Sect**                |
| 남만야수궁  | **Nanman Beast Palace**          |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 강호     | **martial world**                                | Prefer “Murim” where the setting itself is meant      |
| 장문인    | **Sect Leader**                              |
| 제자     | **Disciple**                                 |
| 몬스터     | **monster**           |
| 대격변     | **Great Cataclysm**   |
| 감숙     | **Gansu**              |
| 정마대전   | **Great Faction War**         |
| 본문      | **our sect / this sect**                                        |
| 혈주 | **Blood Lord** | Title of the unidentified young man encountered by Han Su. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 현천진인 | **Perfected Being Hyeoncheon** | Current Sect Leader of Wudang and Hyeongong's Senior Brother. |
| 정호군 | **Jeong Hogun** | Commander of the Embroidered Uniform Guard force confronting Jin. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 정호 | **Jung Ho** | Middle-aged Shaolin martial monk leading the traveling group. |
| 사마표 | **Sama Pyo** | Young Sect Leader of the Black Dragon Demon Gate. |
| 중상 | **Severe Injury** | System condition label causing a major drop in all stats. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 풍운검군 | **Wind-and-Cloud Sword Lord** | Epithet of Gong Iljung, the Zhongnan Sect's Sect Leader. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 오우거 | **ogre** | B-rank monster species emerging from the Gate. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 트롤 | **Troll** | Monster species with extraordinary regenerative ability. |
| 일각 | **fifteen minutes** | Quarter of a shichen; used for the remaining completion time. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 천주 | **Lord of Heaven** | Authority invoked by the masked attackers. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 종남일룡 | **Zhongnan One Dragon** | Epithet of Hyuk Sopyung. |
| 호북 | **Hubei** | Province on Ju Gongsan's route from Guangdong to Henan. |
| 성도 | **Chengdu** | Sichuan destination of Taekyung's party. |
| 열화신룡 | **Blazing Flame Divine Dragon** | New sobriquet bestowed on Jin Taekyung. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 소평 | **So Pyeong** | Alliance office worker assigned to prepare a report. |
| 공동파 | **Kongtong Sect** | Sect belonging to the Nine Sects and One Gang. |
| 화룡각 | **Fire Dragon Pavilion** | New name chosen for Taekyung's pavilion. |
| 변이체 | **mutant** | Taekyung's classification for the monster. |
| 대설산 | **Great Snow Mountain** | Mountain where Baeksang's wartime account reaches its next episode. |
| 균열 | **rift** | The dark rift opening in the cliff behind the Inner Palace. |
| 변이 | **mutation** | The transformation threatening the humans and beasts in the Inner Palace. |
| 화신 | **Fire God** | A local deity worshiped by one Nanman believer. |
| 파리 | **Paris** | The city containing Ares Guild's branch attacked at the chapter's end. |
| 심해 | **deep sea** | Unexplored ocean depths where the ancient monster awakens. |
| 종남 | **Zhongnan Sect** | Orthodox faction that fought in the historic battle. |
| 진인 | **Perfected One** | Honorific for the two Kongtong Elders killed at Dunhuang. |
| 대인 | **Great Sir** | Name used for the mysterious figure in Ningxia. |

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
| 혈주 | 적천강 | claimed enemy to enemy | your enemy | calm and threatening | The Blood Lord identifies himself as Jeok's enemy and claims to have killed Jeok's most precious friend. |
| 혈주 | 진태경 | hostile_opponent_to_hostile_opponent | Sleeping Dragon of Shanxi | casual, amused, and taunting | Addresses Taekyung by his established epithet while asking whether he agrees with the Blood Lord's judgment of Han Su. |
| 혁소평 | 진태경 | hostile_opponents | you; bastard | hostile and contemptuous | Hyuk insults Taekyung as a beggar and attacks him after Taekyung refuses to defer to his status. |
| 진태경 | 혁소평 | hostile_opponents | you; bastard | insulting and taunting | Taekyung mocks Hyuk’s appearance, cultivation, and failed attack while forcing him to agree to end the dispute. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 사마표 | 정호 | Black Dragon Demon Gate Young Sect Leader addressing a Shaolin Master | Master Jung Ho | Polite and ingratiating | Uses 정호대사 and 대사 while flattering Jung Ho and negotiating responsibility for the killing. |
| 정호 | 사마표 | Shaolin martial monk addressing the Black Dragon Demon Gate Young Sect Leader | Benefactor | Formal and admonitory | Uses 시주 while questioning Sama Pyo and demanding accountability. |
| 정호 | 진태경 | Shaolin Discipline Hall Master to patient and Benefactor | Benefactor Jin | formal-polite | Jung Ho repeatedly uses 진 시주 and 시주. |
| 진태경 | 정호 | patient to Shaolin Discipline Hall Master | Monk | polite and familiar | Taekyung addresses Jung Ho as 스님. |
| 사마표 | 적천강 | Young Sect Leader to legendary elder | Great Hero Jeok | formal-deferential | Sama Pyo formally pays his respects to Jeok Cheongang as the Fire King. |
| 적천강 | 사마표 | legendary elder to unorthodox Young Sect Leader | you / young brat | blunt, suspicious, and contemptuous | Jeok addresses Sama Pyo with 네놈 and 어린놈 while probing his lineage and motives. |
| 사마표 | 진태경 | prospective recruit to pavilion master | you | polite, controlled, and candid | Sama Pyo uses 자네 while asking about Taekyung's attitude and admitting his intention to use him. |
| 진태경 | 사마표 | pavilion master to prospective recruit | you / that guy | blunt, informal, and distrustful | Taekyung speaks to and about Sama Pyo with casual forms such as 녀석 and 저놈. |
| 혈주 | 천주 | servant_to_absolute_master | Lord of Heaven | worshipful and deferential | Blood Lord repeatedly addresses the Lord of Heaven while apologizing and receiving power. |
| 천주 | 혈주 | absolute_master_to_servant | Blood Lord | commanding and reproachful | The Lord of Heaven directly rebukes Blood Lord and then empowers him. |
| 혁무진 | 조장님 | pavilion_member_to_squad_leader | Captain | deferential and dubious | Mujin questions whether the pasture should be called the Nanman Ranch instead of the Nanman Beast Palace. |
| 진태경 | 정호군 | young martial artist to senior imperial officer | Commander Jeong | casual and teasing, then conciliatory | Jin addresses him by rank while trying to defuse the standoff. |
| 궁성 | 진태경 | elder who spent decades searching for the chosen one | you | casual and teasing | Uses 너/널 while testing and praising Taekyung. |
| 진태경 | 궁성 | chosen one addressing the elder who sought him | you | polite, shifting to familiar-casual under stress | Begins with formal-polite phrasing, then speaks more casually as the conversation intensifies. |
| 적천강 | 궁성 | old acquaintance and fellow martial master | you; nasty old hag | blunt and familiar | Uses a contemptuous insult while expressing concern for his Disciple. |
| 궁성 | 적천강 | old acquaintance and fellow martial master | you | familiar and lightly teasing | Speaks with dry familiarity about his unchanged, impulsive nature. |
| 정호군 | 진태경 | imperial officer responding to the Marquis of Shangshan | Marquis of Shangshan | formal and deferential | Accepts the command with a formal acknowledgment of Taekyung’s title. |
| 적천강 | 풍운검군 | legendary_elder_to_Zhongnan_sect_leader | Wind-and-Cloud Sword Lord | familiar and commanding | Jeok Cheongang tells him to get the Zhongnan disciples moving. |
| 풍운검군 | 적천강 | Zhongnan Sect Leader to legendary martial master | Senior Jeok | respectful | Refers to Jeok as 적 대협. |
| 풍운검군 | 진태경 | martial artist to fellow martial artist | Daoist Friend Jin | respectful and familiar | Thinks of Jin as 진 도우 when recognizing him as a possible turning point in the battle. |
| 현천진인 | 사마표 | Kongtong Sect Leader confronting the son of a man he believes betrayed the survivors | Sama family boy | formal, then cold and severe | Initially addresses him as 도우, then shifts to 사마가의 아해야 before demanding that he bring his father. |
| 진태경 | 대인 | young martial artist to benefactor | you | casual and blunt | Taekyung asks who Great Sir is, addressing him as 당신. |
| 대인 | 진태경 | older benefactor to young martial artist | you | familiar conversational | Great Sir addresses Taekyung as 자네. |
| 진태경 | 현천진인 | young martial artist addressing a senior Daoist Sect Leader | Perfected Being | polite | Jin responds respectfully to Hyeoncheon's assessment of the retreat. |
| 현천진인 | 진태경 | Kongtong Sect Leader addressing an allied martial artist | Daoist Friend Jin | respectful and measured | Refers to Jin as 진 도우 while discussing the Zhongnan Disciples’ future. |

## Listed compact profiles

### Blood Lord.md

# Blood Lord (혈주)

- **Safe through:** Chapter 1068
- **Aliases:** None
- **Role:** Young-seeming high-ranking Dark Heaven figure who directs its sorcerers’ seed experiments and prepares their deployment for the Lord of Heaven’s great cause.
- **Personality:** Confident, cruel, and controlling; readily kills subordinates who disappoint him, but restrains his violence when preserving valuable sorcerers serves Dark Heaven’s goals.
- **Voice:** Light, cheerful, and joking even while threatening or killing; turns cold and contemptuous when challenged.
- **Relationships:** He serves the Lord of Heaven and seeks to advance the Lord’s great cause; he regards the deceased Western Heaven Demon Lord and Southern Heaven Demon Empress as powerful allies whose deaths cost Dark Heaven, and considers Jin Taekyung and Cheongpung formidable adversaries.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1070
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Hyeoncheon.md

# Perfected Being Hyeoncheon (현천진인)

- **Safe through:** Chapter 1068
- **Aliases:** None
- **Role:** Perfected Being Hyeoncheon is the current Sect Leader of the Kongtong Sect, a veteran Daoist master, and a Supreme Peak martial artist.
- **Personality:** Grave and reflective, he bears the losses of the Great Faction War yet rejects punishing the innocent for their relatives’ crimes.
- **Voice:** Measured, solemn, and calm with the authority of a Sect Leader.
- **Relationships:** Hyeongong is his Junior Brother, and both studied under the same master from childhood.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 1066
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and an active member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented; despite being naturally fearful, he faces danger and remains loyal to the person he serves, with irreverent self-deprecation and a taste for glory. He is suspicious of Taekyung, bluntly critical of the family's disgraced third son, and an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; with Taekyung, blunt and occasionally incredulous, while using breezy, irreverent banter to defuse tense situations.
- **Relationships:** He is loyal to Taekyung, who trusts him to act independently, especially in his home region of Shanxi and at the Jin Family of Taiyuan. As a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Fire Dragon Pavilion members accompanying Taekyung. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business.

### Hyuk Sopyung.md

# Hyuk Sopyung (혁소평)

- **Safe through:** Chapter 1065
- **Aliases:** Zhongnan One Dragon
- **Role:** Peak master of the Zhongnan Sect known as the Zhongnan One Dragon and a senior disciple who can command the Taeeul Sword Unit in Hwangbo Eom's presence.
- **Personality:** Proud, volatile, entitled, and quick to anger, especially when drunk.
- **Voice:** Loud, confrontational, insulting, and imperious.
- **Relationships:** Baek Museong knows him from several prior encounters; Baek says their elders' connection has been passed down to them.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 1070
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; he distrusts process-first excuses when outcomes fail and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, and insists on protecting Taekyung while urging him not to risk his life; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy, and personally killed his former ally the Junzi Saber after that man joined the Demonic Cult.

### Jeong Hogun.md

# Jeong Hogun (정호군)

- **Safe through:** Chapter 1070
- **Aliases:** None
- **Role:** Jeong Hogun is a Thousand Captain of the Embroidered Uniform Guard and a highly skilled martial artist whose force includes dozens of Peak masters.
- **Personality:** Disciplined and resolute, he follows imperial orders without hesitation and reads the political consequences of events with care.
- **Voice:** Formal and rigid, emphasizing duty to imperial authority.
- **Relationships:** Jeong Hogun serves under Baek Yeon’s command in the Embroidered Uniform Guard and honors Jin Taekyung as a comrade-in-arms after their shared battle.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1070
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan and the original owner of his current body, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master who has reached the realm of the Ten Kings as its eleventh member and can detect and eavesdrop on nearby Sound Transmissions subject to the participants’ relative levels, and a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure, willing to risk himself for others, and fiercely defiant when others try to dictate his choices or survival.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; Hyuk Mujin trusts Taekyung to fight beside him; Taekyung trusts Sama Pyo as a friend despite suspecting his betrayal, and values him beyond his unorthodox affiliation; Peng Cheolhu regarded Taekyung as a worthy successor, and the Bow Saint relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1070
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Jung Ho.md

# Jung Ho (정호)

- **Safe through:** Chapter 1070
- **Aliases:** None
- **Role:** Middle-aged Shaolin martial monk and Master of Shaolin's Discipline Hall who leads the traveling group and wields a Zen staff hung with prayer beads.
- **Personality:** Humble, observant, principled, and concerned with the safety of commoners.
- **Voice:** Formal, restrained, and admonitory, with Buddhist phrasing.
- **Relationships:** Unnamed is his young Martial Uncle; he leads the Shaolin monks traveling with him, addresses Sama Pyo as a Benefactor, and is recognized by Jin Taekyung as Park Jung Ho, a former Garam Middle School classmate.

### Sama Pyo.md

# Sama Pyo (사마표)

- **Safe through:** Chapter 1066
- **Aliases:** Black Dragon Saber
- **Role:** Young Sect Leader and heir of the Black Dragon Demon Gate, a Morning Star reputed to be no less than the Ten Dragons and Phoenixes.
- **Personality:** Courteous and calculating, he chooses what he believes is right over expedience and accepts responsibility for his choices, even when they expose him to blame.
- **Voice:** Polite and ingratiating in public, with sardonic humor and controlled evasiveness.
- **Relationships:** Sama Pyo is Sima Gong’s son and chosen heir, commands Taishan, and is Jin Taekyung’s friend; he deliberately let Namho suspect his father’s actions to protect their companions, was Ju Hwaran’s former fiancé, and is hostile toward Song Ilseom.

## Korean source

```text
1071화




나는 신속하고 주위의 상황을 읽고 판단했다.

그리고 그중에서도 최우선으로 둔 것은, 사방에서 몰려오는 먼지구름의 크기와 지면으로부터 전해지는 진동의 세기를 통하여 적들의 숫자를 가늠하는 것이었다.

‘최소 일만. 절대 그 이하는 아니야.’

당연하게도 상황은 좋지 않았다.

어림짐작하기에도 무려 아군의 세 배가 넘는 머릿수.

더불어 지금 이 순간에도 시시각각 가까워지는 적들은 지치지도, 쉽게 죽지도 않는 괴물들이니까.

‘심지어 그중에는 저놈 같은 또 다른 변이체도 있겠지.’

나는 고개를 돌려 바라보았다.

머리가 절반으로 쪼개진 채, 완전한 죽음을 맞이한 거인의 시체를.

장담컨대 저 거대한 체구를 지닌 괴물의 정체는 트롤도, 오우거도 아니다.

21세기 현대를 혼돈의 구렁텅이로 빠트린 대격변 이후, 지금까지 나타난 모든 종류의 괴물이 기록된 몬스터 백과사전에도 저런 괴물은 없다.

앞서 내가 마음속으로 읊조렸던 것처럼, 그야말로 변이체(變異體)라는 표현이 어울리는 존재였다.

어느 순간부터 무림에서 모습을 드러냈던, 또 다른 괴물들처럼.

‘그래, 그때와 같은 흐름이다.’

변이체의 등장은 이번이 처음이 아니다.

호북에서도, 남만야수궁에서도 이와 비슷한 일들이 벌어졌었다.

그리고 언제나 그 모든 것의 중심에는, 천주(天主)를 따르는 추종자들과 그들이 불러온 ‘균열’이 있었음을 나는 똑똑히 기억하고 있다.

‘그렇다는 건, 설마…….’

문득 뇌리를 스치는 한 줄기의 불길한 생각.

그러나 나는 이내 고개를 내저어 상념을 끊어 냈다.

설령 조금 전 떠오른 생각이 전부 사실이라 해도, 지금은 당장 눈앞의 적들을 쓰러트리는 것이 우선이었으니까.

“사마표, 정호군.”

불쑥 입을 연 나는 두 사람을 똑바로 응시하며 말을 이었다.

“지금부터 각각 좌, 우를 맡는다.”

말없이 고개를 숙인 사마표와 정호군이 즉각 움직였다.

각각 일천의 수하를 거느린 저들은 지금부터 아군의 양 날개가 되어 줄 것이다.

이 긴박한 상황에서 시간을 지체시킨 웬수 덩어리인 동시에, 한편으로는 기가 막힌 우연의 일치로 적들을 맞이할 준비 시간을 벌어 주었던 어느 초절정 고수와 함께.

“대인.”

“응? 나? 나는 빠지면 안 되나? 저들과는 별 악감정도 없는데.”

“시발 대인아.”

“……어디로 가면 되겠나?”

“좌우측. 번갈아 가면서 위급한 쪽을 도와주십시오.”

“끄응. 알겠네.”

이로써 아군의 양 날개는 더욱더 날카롭고 튼튼해질 것이다.

정신이 오락가락하긴 해도, 초절정 고수가 버티고 있는 한 결코 쉽게 허물어질 수 없을 테니까.

“빈도는 어찌하면 되겠는가?”

공동파의 장문인, 현천진인의 물음에 나는 즉각 답했다.

“장문인께서는 공동파의 제자들과 함께 후미를 맡아 주십시오.”

“종남파에게 선봉을 빼앗긴 것은 아쉽지만, 지금 같은 상황에서는 본문이 가장 중요한 역할을 맡아야겠지. 도우의 뜻은 잘 알겠네.”

적들에 의한 포위망이 어느 정도 갖추어진 상황에서는 선봉보다도 후미가 중요한 법.

그런 의미에서 보자면 현천진인은 평범한 무림인과는 달리 전술에 대한 이해도가 있는 사람이었다.

정마대전이라는 거대한 전란을 온몸으로 헤쳐나온 노강호였고, 그렇기에 내 의도를 어렵지 않게 알아차린 것이다.

물론, 그런 현천진인조차도 모든 것을 꿰뚫어 본 것은 아니었지만.

“선봉은 종남이 아닙니다.”

“그게 무슨.”

순간 의아해하는 현천진인을 뒤로한 채, 나는 긴장된 얼굴로 검을 쥐고 있던 한 사람을 불렀다.

“혁소평. 너와 종남파 또한 공동파를 도와 후미를 맡는다.”

종남일룡(終南一龍) 혁소평.

대설산에서의 전투로 중상을 입은 탓에 감숙에 남을 수밖에 없었던 풍운검군 대신, 살아남은 종남파의 제자들을 이끌고 있던 그가 눈을 동그랗게 떴다.

아니, 비단 혁소평 한 사람뿐만이 아니라 내 한 마디 한 마디에 촉각을 곤두세우고 있던 주변인들 모두가 동시에 보인 반응이기도 했다.

“그렇다면 선봉은…….”

혁소평이 말꼬리를 흐린 그때, 누군가의 걸걸한 목소리가 모두의 귓가를 파고들었다.

“뭐 하고 자빠졌느냐. 냉큼 후미로 빠지지 않고.”

화왕(火王) 적천강.

바로 그였다.

그리고 이 드넓은 무림에 자신의 발자국을 난폭하게 박아 넣은 거인의 옆자리에는, 왕을 넘어 별이라 불리게 된 한 여인이 있었다.

철컥.

말없이 두 자루의 곡도를 연결하여 거대한 활을 완성시키는 궁성(弓星)의 모습에 모두가 입을 다물었다.

저들이 누구인가.

화왕과 궁성이다.

가장 난폭한 화염을 간직한 왕중왕(王中王)이자, 한 자루의 활로 숱한 전장을 지배한 천하 무림의 별이며, 살아 있는 무림의 전설들이다.

또한.

저벅.

나 역시 그들과 함께할 자격을 얻었다.

지금 이 순간 화왕과 궁성을 향해 걸어갈 수 있는 하나의 상징이 되었다.

비록 그들보다 조금 작고, 아직은 보다 나약할지언정.

나는, 열화신룡(烈火神龍) 진태경은 이 엿 같은 전쟁 속에서 일어난 또 한 명의 거인이었다.

구구구구궁!

땅이 떨린다. 아니, 몸부림친다.

등 뒤의 야트막한 언덕 하나를 제외하면 사방이 탁 트여 있던 이 갈대숲은, 어느덧 자욱한 먼지구름에 둘러싸여 있었다.

아니, 어디에서 왔는지 무엇인지도 모르는 괴물들에게 포위되어 있다.

하지만.

“아직도 저런 잡것들한테 겁먹은 놈들이 있나?”

나는 놈들이 두렵지 않다.

두려운 것이 있다면 오직, 내 잘못으로 인해 죽음을 맞이할 누군가의 불행뿐이다.

“만약 두렵다면, 피하고 싶다면 지금이라도 전열에서 물러나라. 결코 비난하지 않을 테니.”

내 모든 말들은 진심이었다.

누구에게나 가족이, 지켜야 할 것이 있다.

생존에 있어 비겁함이란 없다.

그렇게라도 살아서 돌아가고자 하는 이가 있다면, 나는 그를 기꺼이 보호할 것이다.

몇 년 전, 어둡고 악취 나던 그 동굴에서 누군가가 나를 위해 그러했듯이.

그리고 지금 내 곁에는, 목숨을 걸고 지킬 가치가 있는 이들이 있었다.

“씨바 거, 인생 뭐 있습니까? 조장님 뒤꽁무니만 쫓다 보니까 이제는 천마 할애비가 나타나도 안 쫄립니다.”

혁무진이 불쑥 내뱉은 한마디에 곳곳에서 실소가 터져 나온 그때, 녀석이 나직이 덧붙였다.

“따르겠습니다. 지옥 끝까지라도.”

“……!”

“……!”

일순간, 주위의 공기가 찌르르 울렸다.

지금 이 순간만큼은 사방을 뒤덮은 거대한 울림들도, 그 너머에서 울려 퍼지는 괴물들의 괴성도 이 세상에서 지워진 듯했다.

동시에, 그 모든 것을 몰아내는 강철의 파도가 일어났다.

차차차차창!

모두가 손에 쥔 병장기를 곧추세우며 함성을 내질렀다.

육신의 피로도, 본 적 없는 괴물들에 의한 공포도 잊은 그들은 맹수처럼 포효하며 일렁이는 어둠 속을 노려보았다.

자신들이 이곳에 있어야 하는 이유를 떠올리며, 놈들에 의해 죽어 간 그리운 얼굴들을 떠올리며.

그리고 그런 그들의 선두에는, 바로 내가 있다.

“오직 두 가지만 명심해라.”

나는 선봉을 향해 걸음을 옮기며 말을 이었다.

“첫째. 어떤 상황에서도 현재의 진형을 유지할 것.”

처처척!

나아가는 걸음을 따라 갈라지는 인(人)의 파도.

더불어 그 너머로 모습을 드러내는 빈자리.

각각 일천의 병력이 결집한 다른 곳과 달리, 텅 비어 있는 그곳은 당장이라도 허물어트릴 수 있는 거대한 구멍처럼 보였지만 이제는 아니었다.

“둘째.”

사박.

갈대를 밟으며 제자리에 멈춰 섰다.

좌측에는 궁성이, 우측에는 적천강이.

그리고 우리 세 사람의 등 뒤에는, 당연하다는 듯이 나를 따라온 화룡각의 대원들이.

머릿수로 치자면 한 줌도 되지 않지만, 그것만으로도 비어 있던 선두의 공간이 빈틈없이 메워지며 하나의 진이 완성되었다.

“어떻게 해서라도, 반드시 살아남을 것.”

마지막 한 마디를 내뱉은 그때.

그그그긍!

하늘이 갈라지는 듯한 굉음과 함께, 무수한 그림자들이 온 사방을 뒤덮으며 쏟아졌다.

삼천여 명의 정예로 이루어진 원형진(元型陳)을 향해.

아니, 강철로 무장한 이 거대한 수레바퀴를 향해.

쉬이이잉, 콰앙!

궁성의 손가락 끝을 떠난 빛줄기가 어둠을 찢어발기며 폭발한 그 순간.

콰드드득!

강철의, 죽음의 수레바퀴가 마침내 이 세상의 것이 아닌 괴물들과 맞닿았다.

딸랑.

음산하고도 사이한 방울 소리가, 휘몰아치는 피 보라 너머로 울려 퍼지고 있었다.



* * *



그들은 짙은 어둠 속에 존재하고 있었다.

아니, 어쩌면 적어도 지금 이 순간만큼은 그들이 어둠 그 자체일지도 몰랐다.

그들은 단순히 어둠 속에 숨어 있는 것이 아닌, 어둠을 장막으로 삼아 몸을 가리고 있었으니까.

설령 한 사람 한 사람이 흑의(黑衣)로 전신을 빈틈없이 둘러싸지 않았더라도, 그들을 둘러싼 장막을 간파해 내고 안을 엿볼 수 있는 이는 극히 드물었다.

그리고 그런 위협을 줄 수 있는 이들은, 수백여 장이나 떨어진 곳에서 무수한 괴물들과 맞서 싸우는 와중이었다.

정확히는, 그들의 조종에 따라 움직이는 수하들이었지만.

딸랑.

흑의인은 손에 쥔 요령(妖鈴)을 흔들었다.

낡고 거무튀튀한 그것으로부터 흘러나온 방울 소리는 탁했으나, 한편으로는 선명하게 뻗어 나가 또 다른 명령과 정보를 전달하고 있었다.

사방에 일정한 거리를 두고 숨어 있는, 흑의인의 또 다른 동료들이 그러하듯이.

“마침내 시작됐군.”

콰아앙!

저 멀리, 굉음과 함께 번뜩이는 섬광을 확인한 흑의인은 작게 중얼거렸다.

괴물들이 쉴 새 없이 내지르는 괴성으로 인해 소리만으로는 정확한 판단이 불가능했지만, 궁성의 것임이 분명한 저 빛줄기는 전투가 시작되었다는 증거였다.

“목표로 했던 위치는 아니지만…… 그래도 포위망은 제대로 갖추었으니 그나마 다행인가.”

흑의인은 못내 아쉬웠다.

일각.

단 일각만 더 놈들이 빠르게 움직여 갈대숲을 빠져나갔다면, 자신과 동료들은 훨씬 더 유리한 위치를 점한 채 전투를 시작할 수 있었을 것이다.

“하지만 기왕 벌어진 것. 별수 없지.”

전투는 이미 시작되었고, 흑의인을 포함한 서른 명의 술사(術士)에게 주어진 역할은 명확했다.

“놈들의 머릿수를 최대한 줄이고, 가능하다면 진태경을 생포할 것.”

불과 반나절 전, 혈주에게서 전달받은 명령을 조용히 읊조린 흑의인은 짐짓 눈살을 찌푸렸다.

“죽이는 것도 아닌 생포라니.”

명령에 앞서 적들에 대한 정보를 입수한바 있는 흑의인으로서는 말도 안 되는 소리로 들렸다.

저들 중에는 초절정 고수가 무려 여섯이나 포함되어 있고, 심지어 그중 두 사람은 화왕과 궁성이다.

진태경 한 사람에게만 집중하여 모든 전력을 퍼붓는다면 죽일 가능성은 충분할지 몰라도,

생포는 매우 어려운 임무였다.

“빌어먹을.”

혈주를 향해 무심코 욕설을 내뱉은 흑의인은 본능적으로 헛숨을 삼키며 주위를 둘러보았다.

하지만 언제나 그렇듯, 그곳에는 끔찍한 악취를 풍기며 멍하니 서 있는 괴물들만이 존재할 뿐이었다.

“……엿 같군.”

흑의인은 짜증 섞인 목소리와 눈빛으로 수하들을 바라보았다.

한참이나 멀리 떨어져 있는 혈주가 무서워 벌벌 떠는 자신의 모습이, 이지를 상실한 채 악취만 뿜어내는 저 괴물들이 오늘따라 유독 꼴 보기 싫었다.

“멍청한 것들 같으니.”

딸랑.

흑의인이 파리를 쫓는 듯한 손짓으로 요령을 흔들자, 호위를 위해 주인의 곁을 둘러싸고 있던 일백 마리의 괴물이 망설임 없이 뒷걸음질 쳤다.

정확히는, 흑의인이 아는 바로는 그러해야 했다.

저벅.

“……?”

흑의인은 눈을 깜빡였다.

구십구 마리의 괴물이 뒷걸음질 치는 가운데, 혼자서 앞으로 걸음을 내디딘 단 한 마리의 괴물을 바라보며.

“아니, 이게 무슨.”

흑의인이 할 말을 찾지 못하는 사이, 그제야 뒤늦게 자신이 처한 상황을 깨달은 괴물은 엉덩이를 움찔거리며 우왕좌왕하다 이렇게 말했다.

“와, 와아아. 신기하다. 이런 괴물 처음 보죠?”

“……!”

“저, 저도 처음, 에이 씨.”

떨리는 목소리로 말을 이어가던 괴물, 아니 사람인 것이 분명한 누군가가 울상을 지으며 한숨을 내쉬었다.
```

## Final English reading copy

```markdown
# Chapter 1071

I quickly read the situation around me and assessed it.

Above all, I focused on estimating the enemy’s numbers from the size of the dust clouds rolling in from every direction and the strength of the vibrations coming through the ground.

*At least ten thousand. It can’t be any less.*

Naturally, things didn’t look good.

Even a rough estimate put them at more than three times our numbers.

And the enemies drawing closer by the second were monsters that neither tired nor died easily.

*There might even be another mutant like that one among them.*

I turned to look at the giant’s corpse, its head split in half and its life well and truly ended.

I could say with certainty that the identity of that huge monster wasn’t a Troll or an ogre.

Not even the monster encyclopedia—which recorded every kind of monster to appear since the Great Cataclysm plunged the modern twenty-first century into chaos—contained anything like it.

Just as I’d thought to myself earlier, *mutant* was the only word that fit.

Like the other monsters that had begun appearing in Murim some time ago.

*Right. The same pattern as back then.*

This wasn’t the first time a mutant had appeared.

Similar things had happened in Hubei and at the Nanman Beast Palace.

And I clearly remembered that at the center of all of it had always been the followers of the Lord of Heaven—and the *rifts* they brought with them.

*If that’s true, then could it be…?*

A single ominous thought suddenly flashed through my mind.

But I shook my head and cut it off.

Even if the thought that had just occurred to me was entirely true, taking down the enemies right in front of us had to come first.

“Sama Pyo. Jeong Hogun.”

I spoke abruptly, looking the two of them straight in the eye.

“From now on, you each take one side. Left and right.”

Sama Pyo and Jeong Hogun bowed without a word and moved immediately.

Each commanded a thousand men. From this moment on, they would form our left and right wings.

Along with one Supreme Peak master who’d delayed us in this urgent situation—but, by an absurd coincidence, had also bought us time to prepare for the enemy.

“Great Sir.”

“Hm? Me? Can’t I sit this one out? I don’t have any particular grudge against them.”

“Fuck, Great Sir.”

“…Where should I go?”

“Left and right. Go back and forth, and help whichever side is in trouble.”

“Ugh. Fine.”

With that, our two wings would grow sharper and stronger.

His mind might wander, but as long as a Supreme Peak master stood with us, they wouldn’t break easily.

“And what should I do?”

I answered at once when Perfected Being Hyeoncheon, the Sect Leader of the Kongtong Sect, asked.

“Please take the rear with the Kongtong Disciples, Sect Leader.”

“It’s unfortunate that the Zhongnan Sect has taken the vanguard from us, but in this situation, our sect must play the most important role. I understand your intentions, Daoist Friend.”

When the enemy had nearly completed their encirclement, the rear mattered more than the vanguard.

In that regard, Perfected Being Hyeoncheon understood tactics better than the average martial artist.

He was a veteran who’d weathered the great turmoil of the Great Faction War with his own body. It wasn’t hard for him to see what I intended.

Of course, even Perfected Being Hyeoncheon hadn’t seen everything.

“The Zhongnan Sect won’t take the vanguard.”

“What do you mean?”

Leaving Hyeoncheon staring at me in confusion, I called to the man gripping his sword with a tense expression.

“Hyuk Sopyung. You and the Zhongnan Sect will help the Kongtong Sect take the rear.”

Hyuk Sopyung, the Zhongnan One Dragon.

He was leading the surviving Zhongnan Disciples in place of the Wind-and-Cloud Sword Lord, who’d been severely injured in the battle at Great Snow Mountain and had to remain in Gansu. His eyes widened.

It wasn’t just Hyuk Sopyung. Everyone around us, listening closely to my every word, reacted the same way.

“Then the vanguard will be…”

As Hyuk Sopyung trailed off, a rough voice rang in everyone’s ears.

“What are you standing around for? Get your asses to the rear.”

It was the Fire King, Jeok Cheongang.

And beside the giant who’d violently stamped his mark on this vast martial world stood a woman called a star, not a king.

*Click.*

Everyone fell silent as Bow Saint joined her two curved swords together, forming a massive bow.

Who were they?

The Fire King and the Bow Saint.

The King of Kings, holding the most savage flames. A star of the martial world who’d dominated countless battlefields with a single bow. Living legends of Murim.

And—

*Step.*

I, too, had earned the right to stand beside them.

In this moment, I’d become a symbol of someone who could walk toward the Fire King and the Bow Saint.

Even if I was a little smaller than they were, and still a little weaker.

I, Jin Taekyung—the Blazing Flame Divine Dragon—was another giant who’d risen in this goddamn war.

*Rumble, rumble!*

The ground trembled. No—it writhed.

Apart from the low hill behind us, the reed bed had once been open in every direction. Now it was surrounded by dense clouds of dust.

No. We were surrounded by monsters whose origins and identities we didn’t even know.

But—

“Anyone still scared of those worthless bastards?”

I wasn’t afraid of them.

If there was anything I feared, it was the misfortune of someone dying because of my mistake.

“If you’re afraid, if you want to run, leave the formation now. I won’t blame you.”

I meant every word.

Everyone had a family, someone or something they needed to protect.

There was no such thing as cowardice when it came to survival.

If anyone wanted to fall back so they could make it home alive, I’d gladly protect them.

Just as someone had done for me, years ago, in that dark, reeking cave.

And now I had people beside me worth risking my life to protect.

“Fuck it, what’s life anyway? I’ve spent all this time following your ass around, Captain. Now I wouldn’t even flinch if the Heavenly Demon’s granddad showed up.”

Hyuk Mujin’s sudden remark drew quiet laughter from around us. Then he added, softly:

“I’ll follow you. Even to the edge of hell.”

“……!”

“……!”

For an instant, the air around us rang like a struck string.

In that moment, it was as if the great rumbling all around us, and the monsters’ roars beyond it, had vanished from the world.

At the same time, a wave of steel swept it all away.

*Clang, clang, clang, clang!*

Everyone raised their weapons and let out a shout.

Forgetting their physical exhaustion and their fear of monsters they’d never seen before, they roared like beasts and glared into the wavering darkness.

Remembering why they had to be here. Remembering the faces of those they missed, killed by the monsters.

And at the head of them all stood me.

“Remember only two things.”

I started toward the vanguard and continued.

“First. Hold the current formation no matter what.”

*Clack, clack, clack!*

The human tide parted as I advanced.

Beyond it, an empty space came into view.

Unlike the other sections, where a thousand men had gathered in each, this vacant spot looked like a massive hole that could collapse at any moment. But it wasn’t one anymore.

“Second.”

*Step.*

I stopped among the reeds.

Bow Saint to my left. Jeok Cheongang to my right.

And behind the three of us stood the members of the Fire Dragon Pavilion, who’d followed me without hesitation.

There weren’t many of us, but we filled the empty space at the front completely, finishing the formation.

“Survive, no matter what it takes.”

Just as I spoke those final words—

*Rrrrmmm!*

With a deafening roar that sounded as if the sky had split apart, countless shadows came pouring in from every direction.

They surged toward the circular formation of roughly three thousand elite fighters.

No—the enormous wheel of steel.

*Whoooosh—BOOM!*

A streak of light shot from Bow Saint’s fingertips, tearing through the darkness and exploding.

*Craaaack!*

The steel wheel—the wheel of death—finally collided with the monsters that didn’t belong in this world.

*Jingle.*

The eerie, sinister sound of a bell rang out beyond the swirling spray of blood.



* * *



They existed in deep darkness.

No, perhaps at least in that moment, they were the darkness itself.

They weren’t simply hiding in the dark. They used it as a curtain to conceal themselves.

Even without every last inch of their bodies covered by black robes, few could see through the curtain that surrounded them and glimpse what lay within.

The people capable of seeing through their concealment were hundreds of yards away, fighting countless monsters.

Those monsters were the concealed figures’ subordinates, moving under their control.

*Jingle.*

The black-robed man shook the evil bell in his hand.

Its sound was dull, issuing from the old, dark object, but it carried clearly into the distance, relaying further commands and information.

Just like the black-robed man’s other comrades, hidden at regular intervals in every direction.

“So it’s finally begun.”

*BOOM!*

The black-robed man quietly murmured as he spotted a flash of light far away, accompanied by a deafening boom.

The monsters’ ceaseless roars made it impossible to judge precisely from sound alone, but that streak of light was unmistakably Bow Saint’s. It was proof the battle had begun.

“It’s not where we wanted them, but… at least we’ve completed the encirclement.”

The black-robed man couldn’t help feeling disappointed.

Another fifteen minutes.

If they’d moved just that much faster and gotten out of the reed bed, he and his comrades could have started the battle from a far more advantageous position.

“But it’s already begun. Nothing to do about it now.”

The battle was underway, and the role assigned to the thirty sorcerers, including the black-robed man, was clear.

“Cut down their numbers as much as possible. If you can, capture Jin Taekyung alive.”

The black-robed man quietly repeated the order he’d received from the Blood Lord just half a day earlier, then furrowed his brow.

“Capture him alive instead of killing him?”

The black-robed man had received information about the enemy before the order came. It sounded absurd.

Among them were no fewer than six Supreme Peak masters, and two of those were the Fire King and the Bow Saint.

If they concentrated all their strength on Jin Taekyung alone, they might have a good chance of killing him.

Capturing him alive, though, would be an extremely difficult task.

“Damn it.”

The black-robed man instinctively sucked in a breath and glanced around, having cursed the Blood Lord without thinking.

But, as always, all he saw were monsters standing vacantly around him, giving off a horrible stench.

“…This is bullshit.”

The black-robed man looked at his subordinates with irritation in his eyes and voice.

He hated that he was trembling in fear of the Blood Lord, who was nowhere near him. And today, he found himself especially disgusted by the monsters that had lost their reason and only gave off a foul stench.

“Stupid bastards.”

*Jingle.*

The black-robed man shook the evil bell with a shooing motion. The hundred monsters surrounding their master to guard him immediately took a step back without hesitation.

At least, that was what the black-robed man knew was supposed to happen.

*Step.*

“…?”

The black-robed man blinked.

Ninety-nine monsters stepped back. He stared at the one that had stepped forward alone.

“What the hell is this?”

Before the black-robed man could find the words, the monster finally seemed to realize its situation. Its backside twitched as it fidgeted, then it said:

“W-Wow. Amazing. You’ve never seen a monster like this before, right?”

“……!”

“I-I haven’t either. Damn it.”

The monster—or, clearly, someone who was a person—continued in a trembling voice, then wore a miserable expression and sighed.
```

<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1066.txt",
      "sha256": "4805f215ead2d0d763c805f508a28e297c58493492f1081b8d75649a478bd441",
      "bytes": 12899
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "3fde65e41c52cc47647a72e63af289917908cfddf396c81d7ba733e4540b39c7",
      "bytes": 926
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "30eaa2be30abc53c7f0555f378868db0fa2a48f03969e97280dbb9724020e47a",
      "bytes": 242084
    },
    {
      "path": "characters/Blood Lord.md",
      "sha256": "592f242e624290f64105ac344cd9cea344611a8813b895df44e4c7cbdeb55cc4",
      "bytes": 928
    },
    {
      "path": "characters/Blood-Sword Demon Lord.md",
      "sha256": "157672694d9c1dac7ce2874f28d5a2af0ae825943ae87de13b65e2e01acd1e39",
      "bytes": 920
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "d9b009aeae240da5f1068bc1f297c272b1cacf30b1341043c24905bc1a74b302",
      "bytes": 760
    },
    {
      "path": "characters/Hyeoncheon.md",
      "sha256": "e1c61b20626c9db0e47e65e3743331b9c68fb345bff7497e72736760fa24c96a",
      "bytes": 651
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "b3237b1117483773168bd49c3ccd0159146811c37f791d1add1f12a7c6eb69d2",
      "bytes": 1375
    },
    {
      "path": "characters/Jang Sam.md",
      "sha256": "364447f6f86da009f096229f7b348cf8aebd9c6d553ce957279f675d7e0b07fb",
      "bytes": 509
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "1255fb4bd9387d53ab83b24a8000650b21d3ecdaddb8d7e0123919f88ae4fb5d",
      "bytes": 1502
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "7cb0753ce3e2130e6587760dc20f12e665dcad828f7f53d8e4961f30af44c1a7",
      "bytes": 1828
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "9490a86d407489c0e0e162bea8ae2252fc832381f684572c917ed105b7bfc219",
      "bytes": 623
    },
    {
      "path": "characters/Ma Sanbao.md",
      "sha256": "f72425cd5cd1c6fcf30b13204dc396765aeae3f409b380f81aaef72af323bd49",
      "bytes": 850
    },
    {
      "path": "characters/Sama Pyo.md",
      "sha256": "8bb0546774ab2ae1a93206e466eb93ec8ffa385fe95b2c3a0ead084865612efc",
      "bytes": 850
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "3187f1a2d77b9ba4e276ef4ce8ab41c3fb3fa577b62db4b4a5c2fa391601eceb",
      "bytes": 283802
    }
  ],
  "estimated_tokens": 12951
}
-->

# Durable State Update — Chapter 1066

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
1 and safe_through 1066. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1066. Profile updates may replace only one
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
  "chapter": 1066,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1066,
    "continuity_sources": [1066],
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
    "The Emperor has called for the government and Murim to unite against Dark Heaven.",
    "Dark Heaven occupies Kunlun; the Kunlun Sect and allies retreated to Qinghai Lake, suffering about a thousand killed or wounded.",
    "Jin Taekyung’s group entered Qinghai Province after leaving Gansu with nearly two thousand allied fighters.",
    "The allied force includes the Kongtong Sect, Zhongnan Sect, Black Dragon Demon Gate, and Embroidered Uniform Guard.",
    "Sama Pyo exposed and dealt with traitors among Gansu’s faction leaders before the departure.",
    "Jin Taekyung cannot log out while the linked Quest “To Qinghai” is incomplete."
  ],
  "continuity_sources": [
    1064,
    1065
  ],
  "open_questions": [
    "Why does the System prevent Jin from logging out beyond the incomplete linked Quest?"
  ],
  "safe_through": 1065,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 장삼 | **Jang Sam** | Bandit; personal name |
| 궁성     | **Bow Saint**                 | —              |
| 종남파    | **Zhongnan Sect**                |
| 곤륜파    | **Kunlun Sect**                  |
| 암천     | **Dark Heaven**                  |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 중원     | **Central Plains**                               |                                                       |
| 장문인    | **Sect Leader**                              |
| 제자     | **Disciple**                                 |
| 사형     | **Senior Brother**                           |
| 시스템              | **System**                     |
| 체력               | **Stamina**                    |
| 헌터      | **Hunter**            |
| 길드      | **Guild**             |
| 감숙     | **Gansu**              |
| 청해     | **Qinghai**            |
| 곤륜     | **Kunlun**             |
| 도사      | **Daoist**                                                      |
| 혈주 | **Blood Lord** | Title of the unidentified young man encountered by Han Su. |
| 혈검마군 | **Blood-Sword Demon Lord** | Antagonist commanding the army advancing on the Great Snow Mountain. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 현천진인 | **Perfected Being Hyeoncheon** | Current Sect Leader of Wudang and Hyeongong's Senior Brother. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 마삼보 | **Ma Sanbao** | The East Depot’s Brush-Holding Eunuch and second-in-command. |
| 사마표 | **Sama Pyo** | Young Sect Leader of the Black Dragon Demon Gate. |
| 은원 | **gratitude and grudges** | Moral debts that must be repaid. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 개방 | **Beggars' Sect** | Murim organization counted among the Nine Sects and One Gang. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 신성 | **Morning Star** | Term in the summons referring to the Master of Morning Star. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 천산 | **Tianshan** | Mountain region identified as the Demonic Cult's headquarters. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 청해성 | **Qinghai** | Source form specifying Qinghai as a province. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 살귀 | **Killing Ghost** | Mungyeong's earlier sobriquet before he became the Slaughter Saint. |
| 흑룡마문 | **Black Dragon Demon Gate** | Unorthodox faction from Gansu. |
| 공동파 | **Kongtong Sect** | Sect belonging to the Nine Sects and One Gang. |
| 화룡각 | **Fire Dragon Pavilion** | New name chosen for Taekyung's pavilion. |
| 만족 | **Man people** | An ethnic group mentioned by the Poison Flower Pavilion owner. |
| 검마 | **Sword Demon** | A Demonic Cult swordsman whose final technique is compared with One Annihilation. |
| 마후 | **Demon Empress** | Title used for the Southern Heaven Demon Empress. |
| 금의위 | **Embroidered Uniform Guard** | Imperial guard force mentioned by Hong Jin. |
| 동창 | **East Depot** | Imperial agency named by Hong Jin. |
| 종남 | **Zhongnan Sect** | Orthodox faction that fought in the historic battle. |
| 십만마도 | **Hundred Thousand Demonic Disciples** | The earlier force used as a comparison for Dark Heaven’s army. |
| 진인 | **Perfected One** | Honorific for the two Kongtong Elders killed at Dunhuang. |
| 대술사 | **Grand Mage** | Title of the veiled woman leading the white-robed mages. |
| 미친놈 | **Madman** | Insult Great Sir adopts as a name; also appears in the System display. |

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
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 사마표 | 적천강 | Young Sect Leader to legendary elder | Great Hero Jeok | formal-deferential | Sama Pyo formally pays his respects to Jeok Cheongang as the Fire King. |
| 적천강 | 사마표 | legendary elder to unorthodox Young Sect Leader | you / young brat | blunt, suspicious, and contemptuous | Jeok addresses Sama Pyo with 네놈 and 어린놈 while probing his lineage and motives. |
| 사마표 | 진태경 | prospective recruit to pavilion master | you | polite, controlled, and candid | Sama Pyo uses 자네 while asking about Taekyung's attitude and admitting his intention to use him. |
| 진태경 | 사마표 | pavilion master to prospective recruit | you / that guy | blunt, informal, and distrustful | Taekyung speaks to and about Sama Pyo with casual forms such as 녀석 and 저놈. |
| 진태경 | 헌터 | field commander to allied Hunters | you; Hunters | blunt and commanding | Orders the human forces to stop asking questions and kill the fleeing Minotaurs. |
| 마삼보 | 진태경 | political ally recruiting a young martial artist | you; my friend | courteous and familiar | Ma uses 자네 and 이보게 while explaining his choice of Jin and inviting him to join the restoration army. |
| 진태경 | 마삼보 | young martial artist addressing the East Depot’s Brush-Holding Eunuch and prospective ally | you; Brush-Holding Eunuch | polite and direct | Jin asks Ma why he withheld information and presses him for a clear answer; he refers to him as 태감. |
| 궁성 | 진태경 | elder who spent decades searching for the chosen one | you | casual and teasing | Uses 너/널 while testing and praising Taekyung. |
| 진태경 | 궁성 | chosen one addressing the elder who sought him | you | polite, shifting to familiar-casual under stress | Begins with formal-polite phrasing, then speaks more casually as the conversation intensifies. |
| 적천강 | 궁성 | old acquaintance and fellow martial master | you; nasty old hag | blunt and familiar | Uses a contemptuous insult while expressing concern for his Disciple. |
| 궁성 | 적천강 | old acquaintance and fellow martial master | you | familiar and lightly teasing | Speaks with dry familiarity about his unchanged, impulsive nature. |
| 혈검마군 | 적천강 | former opposing martial masters | Senior Jeok | respectful and familiar | Addresses Jeok as 선배 while teasing him. |
| 적천강 | 혈검마군 | former opposing martial masters | you; you bastard | blunt and hostile | Uses 너 and 네놈 while confronting him. |
| 혈검마군 | 진태경 | enemy addressing a younger martial artist | you | familiar and measured | Uses 자네 while praising and assessing Taekyung. |
| 진태경 | 혈검마군 | young martial artist confronting an enemy | you | casual and challenging | Questions when the Blood-Sword Demon Lord and the Lord of Heaven appeared. |
| 대술사 | 혈검마군 | subordinate_to_commander | Demon Lord | respectful and formal | Addresses him as 마군 while acknowledging his injuries. |
| 혈검마군 | 대술사 | commander_to_subordinate | Grand Mage | blunt and commanding | Orders her to heal him immediately. |
| 현천진인 | 사마표 | Kongtong Sect Leader confronting the son of a man he believes betrayed the survivors | Sama family boy | formal, then cold and severe | Initially addresses him as 도우, then shifts to 사마가의 아해야 before demanding that he bring his father. |
| 진태경 | 대인 | young martial artist to benefactor | you | casual and blunt | Taekyung asks who Great Sir is, addressing him as 당신. |
| 대인 | 진태경 | older benefactor to young martial artist | you | familiar conversational | Great Sir addresses Taekyung as 자네. |
| 혈주 | 대술사 | fellow servant of the same person | you; you bitch | insulting-casual | Blood Lord taunts the Grand Mage and uses a crude insult. |
| 대술사 | 혈주 | fellow servant of the same person | you | contemptuous-casual | The Grand Mage addresses the Blood Lord while rebuking him. |
| 진태경 | 현천진인 | young martial artist addressing a senior Daoist Sect Leader | Perfected Being | polite | Jin responds respectfully to Hyeoncheon's assessment of the retreat. |
| 현천진인 | 진태경 | Kongtong Sect Leader addressing an allied martial artist | Daoist Friend Jin | respectful and measured | Refers to Jin as 진 도우 while discussing the Zhongnan Disciples’ future. |

## Listed compact profiles

### Blood Lord.md

# Blood Lord (혈주)

- **Safe through:** Chapter 1062
- **Aliases:** None
- **Role:** Young-seeming high-ranking Dark Heaven figure who directs its sorcerers’ seed experiments and prepares their deployment for the Lord of Heaven’s great cause.
- **Personality:** Confident, cruel, and controlling; readily kills subordinates who disappoint him, but restrains his violence when preserving valuable sorcerers serves Dark Heaven’s goals.
- **Voice:** Light, cheerful, and joking even while threatening or killing; turns cold and contemptuous when challenged.
- **Relationships:** He serves the Lord of Heaven and seeks to advance the Lord’s great cause; he regards the deceased Western Heaven Demon Lord and Southern Heaven Demon Empress as powerful allies whose deaths cost Dark Heaven, and considers Jin Taekyung and Cheongpung formidable adversaries.

### Blood-Sword Demon Lord.md

# Blood-Sword Demon Lord (혈검마군)

- **Safe through:** Chapter 1058
- **Aliases:** None
- **Role:** The Blood-Sword Demon Lord is a formidable martial master who commands the force advancing on the Great Snow Mountain and now serves the Lord of Heaven.
- **Personality:** Devoted to his master and proud of his abilities, he is deeply wounded by perceived distrust and resolves to prove his worth.
- **Voice:** Casually familiar and self-amused, addressing Jeok Cheongang respectfully as Senior while trading blunt insults; his easy laughter can turn to a low, cold intensity.
- **Relationships:** He serves the Lord of Heaven with deep devotion, but the Grand Mage says the Lord ordered his disposal; he has been ordered not to kill Jin Taekyung, admires Jeok Cheongang, and once shared the Demonic Cult with the fiends who became Black Ghosts.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1065
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Hyeoncheon.md

# Perfected Being Hyeoncheon (현천진인)

- **Safe through:** Chapter 1065
- **Aliases:** None
- **Role:** Perfected Being Hyeoncheon is the current Sect Leader of the Kongtong Sect, a veteran Daoist master, and a Supreme Peak martial artist.
- **Personality:** Grave and reflective, he bears the losses of the Great Faction War yet rejects punishing the innocent for their relatives’ crimes.
- **Voice:** Measured, solemn, and calm with the authority of a Sect Leader.
- **Relationships:** Hyeongong is his Junior Brother, and both studied under the same master from childhood.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 1063
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and an active member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented; despite being naturally fearful, he faces danger and remains loyal to the person he serves, with irreverent self-deprecation and a taste for glory. He is suspicious of Taekyung, bluntly critical of the family's disgraced third son, and an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; with Taekyung, blunt and occasionally incredulous, while using breezy, irreverent banter to defuse tense situations.
- **Relationships:** He is loyal to Taekyung, who trusts him to act independently, especially in his home region of Shanxi and at the Jin Family of Taiyuan. As a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Fire Dragon Pavilion members accompanying Taekyung. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business.

### Jang Sam.md

# Jang Sam (장삼)

- **Safe through:** Chapter 1065
- **Aliases:** Killing Ghost
- **Role:** Jang Sam is a bandit chief who abruptly rose from Level 40 to Level 60 and attacked Taekyung while apparently irrational; he is currently unconscious and being taken to the Nangong Family.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** No relationships established.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 1064
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; he distrusts process-first excuses when outcomes fail and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, and insists on protecting Taekyung while urging him not to risk his life; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy, and personally killed his former ally the Junzi Saber after that man joined the Demonic Cult.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1065
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan and the original owner of his current body, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master who has reached the realm of the Ten Kings as its eleventh member and can detect and eavesdrop on nearby Sound Transmissions subject to the participants’ relative levels, and a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure, willing to risk himself for others, and fiercely defiant when others try to dictate his choices or survival.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; Hyuk Mujin trusts Taekyung to fight beside him; Taekyung trusts Sama Pyo as a friend despite suspecting his betrayal, and values him beyond his unorthodox affiliation; Peng Cheolhu regarded Taekyung as a worthy successor, and the Bow Saint relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1065
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Ma Sanbao.md

# Ma Sanbao (마삼보)

- **Safe through:** Chapter 931
- **Aliases:** None
- **Role:** Ma Sanbao is the East Depot’s Brush-Holding Eunuch and a Supreme Peak martial artist who secretly led a restoration effort for Prince Shangshan as a disciple of the Eastern Heaven Demon Lord.
- **Personality:** He is vigilant and patient, concealing his loyalties while awaiting the moment to act for the late Emperor.
- **Voice:** He speaks in measured, courteous language and uses calm repetition, feigned agreement, and procedural reminders to steer conversations while keeping sensitive details guarded.
- **Relationships:** Ma Sanbao was a longtime friend and former East Depot cohort of Hong Jin, served the Eastern Heaven Demon Lord, and led a restoration effort for Prince Shangshan.

### Sama Pyo.md

# Sama Pyo (사마표)

- **Safe through:** Chapter 1065
- **Aliases:** Black Dragon Saber
- **Role:** Young Sect Leader and heir of the Black Dragon Demon Gate, a Morning Star reputed to be no less than the Ten Dragons and Phoenixes.
- **Personality:** Courteous and calculating, he chooses what he believes is right over expedience and accepts responsibility for his choices, even when they expose him to blame.
- **Voice:** Polite and ingratiating in public, with sardonic humor and controlled evasiveness.
- **Relationships:** Sama Pyo is Sima Gong’s son and chosen heir, commands Taishan, and is Jin Taekyung’s friend; he deliberately let Namho suspect his father’s actions to protect their companions, was Ju Hwaran’s former fiancé, and is hostile toward Song Ilseom.

## Korean source

```text
1066화




띠링.



- [청해성]에 진입했습니다.



때맞춰 울려 퍼진 시스템 알림에, 주먹을 불끈 쥔 채 대인을 향해 걸어가던 나는 불현듯 걸음을 멈췄다.

“생각 잘 생각하셨습니다. 가뜩이나 성치 않은 사람 때려 봤자 좋을 게 하나도 없…… 제 말 듣고 계세요?”

“쉿.”

내가 생각을 고쳐먹었다고 생각한 건지, 안도의 한숨을 내쉬던 혁무진을 향해 입 다물라는 신호를 보내고 주위를 둘러보았다.

어둠이 내려앉은 울창한 삼림(森林)과 곳곳에서 들려오는 풀벌레 소리.

주위의 풍경은 조금도 달라진 것이 없었지만, 나를 포함한 모두는 지금 이 순간 보이지 않는 경계를 지난 것이 확실했다.

시스템은 언제나 정확하고, 거짓말을 하지 않으니까.

그리고 용케도 자신에게 주어진 소임을 완수한 대인은, 그의 머리 위에 떠올랐던 물음표들과 같은 얼굴을 하고 내게 물었다.

“왜 그러나? 장삼이.”

“……장삼이 아니고 진태경이라니까요.”

사실 끝까지 반신반의했었다.

본인 이름도 기억 못 하는 사람을 따라 이동하는 건 누가 봐도 결코 현명한 판단이 아니었으니.

심지어 이동하는 와중에도 이리저리 방향을 틀어 대는 통에, 평생을 감숙성에서 나고 자란 사마표와 같은 이들도 몇 번이나 의문을 표했을 정도였다.

하지만, 뭐.

‘결과는 좋네.’

처음에 예상했던 것보다 최소 이틀 이상을 단축했고, 비록 험난한 산세를 타고 이동했으나 그만큼 체력을 비축할 시간을 얻었다.

‘문제는 이 인간이 어떻게 이런 길을 알고 있냐는 건데.’

다시 한번 당연한 의문이 고개를 들었지만, 입이 찢어져라 하품하는 대인의 모습을 본 순간 나도 모르게 고개가 저어졌다.

여기서 더 의심을 품어 봤자 어쩌겠나.

이미 한참 전부터 오락가락했던 사람이고, 시스템이 미친놈이라고 인증마크까지 박아 준 이상 의심의 여지도 없다.

중요한 것은 대인이 적어도 아군이라는 범주에 포함되는 사람이며, 그의 도움으로 우리 모두가 지금 이 순간 청해성에 도달했다는 것이다.

정확히는, 청해성의 북서부 인근에.

‘그리고 이곳은…….’

그래.

이제는 암천의 지배하에 놓인, 수많은 위험으로 가득한 적지(敵地)다.



* * *



삼천여 명.

결코 적지 않은 머릿수다.

현대에서 이 정도의 헌터를 보유하고 있다면 충분히 대형 길드로 취급받을 정도고, 개방을 제외한 다른 구파일방이라 할지라도 본산에 속하지 않은 속가제자(俗家弟子)들까지 끌어모아야 가능한 숫자다.

하지만 결국 모든 것은 상대적인 법.

현재 청해성을 침략한 암천의 군세가 과거의 십만마도(十萬魔道)과 버금가는 대군이라는 것을 생각한다면, 삼천이라는 병력은 태양 앞의 잔딧불이나 다름없었다.

‘시급을 다투는 상황이라고는 해도, 지금처럼 피로가 쌓인 채로 곧장 움직였다간 되레 당하고 말아.’

그렇기에 나는 잠시 이동이 멈춘 산맥에서 하루 동안의 휴식을 제안했고, 누구도 이에 반박하지 않았다.

나로서는 가장 어려운 상대라 할 수 있는 현천진인마저 예외는 아니었다.

아니, 그는 오히려 필요 이상의 예의까지 갖추어 나를 당혹스럽게 했다.

“실로 타당한 판단이로군. 좋네. 휴식 이후의 분부는 어찌 되나?”

“예? 분부요?”

“왜, 뭔가 잘못된 거라도 있나? 분부가 아니라 명령이라고 해도 별 상관은 없네만.”

“……차라리 욕을 하세요. 저한테 왜 이러십니까.”

명절날 할아버지뻘 되는 분한테 큰절 받는 종갓집 종손이 이런 기분일까.

심히 당황스러워하는 내 반응에 현천진인은 피식 웃더니 생각지도 못한 한마디를 던졌다.

“가끔은 한 번씩 주위를 둘러보는 것이 어떤가?”

“그게 무슨…….”

“도우의 주위에 얼마나 많은 사람이 있는지, 그토록 많은 이들이 도우를 어떤 눈빛으로 바라보는지 확인해 보게. 그것이 현재 자신의 위치니까.”

“……!”

그제야 뒤늦게 깨달을 수 있었다.

지금 이 순간에도 나를 향해 집중된 수많은 시선.

그들의 눈동자에 담긴 짙은 선망과 호의는 손을 뻗어 만질 수 있을 것처럼 선명했고, 입가에 맺힌 은은한 미소에는 숨길 수 없는 고마움이 담겨 있었다.

뒤이어 귓가에 흘러들어오는 현천진인의 따스한 목소리처럼.

“부탁이건, 분부건, 명령이건. 그 무엇이어도 상관없네. 우리 모두는 도우에게 큰 빚을 졌으니까.”

“빚…….”

“은원(恩怨)은 반드시 갚는 것이 무림의 법도. 허나 빈도는 원한을 용서했고, 이제 은혜를 갚고자 하네. 아마도 저들 역시 같은 마음이겠지.”

문득 생각했다.

오랜 세월 동고동락한 동료, 피붙이, 혹은 사형제를 잃은 저들의 마음을.

전장에서 느낀 그 막대한 공포와 슬픔을 채 추스르기도 전에, 스스로의 의지로 나를 따라 새로운 사지(死地)로 걸어 들어온 그 심정을.

그건 빚을 갚기 위함인 동시에 이 땅에 어둠을 가져올 복수심이었고.

그 자체로 어둠을 밝힐 빛이었다.

“아.”

도무지 익숙해질 수 없는, 실로 이상한 기분이다.

뭐라 대답해야 할지 모를 정도로.

그리고 자신이 살아온 긴 세월만큼의 현명함을 지닌 노도사는 구태여 내 답을 요구하지 않았다.

툭툭.

그는 말없이 어깨를 두드려 준 뒤 자리를 떠났고, 남아 있는 사람들의 이목은 내게 집중되었다.

공동파와 종남파의 제자들.

금의위와 흑룡마문의 무인들.

심지어는 화룡각 대원들 틈에 섞여 있던 적천강과 궁성마저도 조용히 고개를 끄덕여 보였을 뿐이었다.

마치, 설령 내가 지옥으로 향하더라도 끝까지 따르겠다는 듯한 표정과 눈빛으로.

“저는. 아니, 나는…….”

무려 삼천여 명에 달하는 모두의 시선 속에서, 나는 천천히 입술을 뗐다.

그리고 그와 동시에 숨 막히는 적막이 깨져 나간 순간, 불현듯 한 가지 생각을 떠올렸다.

‘도대체 어떻게…… 이 정도까지 고요할 수 있지?’

그제야 깨달았다.

울창한 숲속 곳곳에 숨어 있던 풀벌레들의 힘찬 울음소리가 어느샌가부터 들리지 않는다는 것을.

높게 솟은 나뭇가지에 앉아 있던 날짐승들도 이미 어디론가 사라져 버렸다는 사실을.

“……!”

서늘한 한기가 등골을 타고 흘러내린 그 순간.

드득, 드드득.

저 멀리에서부터 뒤늦게 전해진 미세한 진동과 함께, 알 수 없는 무언가의 괴성이 스산한 바람을 타고 귓가로 흘러들어왔다.

크르륵.

“……빌어먹을.”

반사적으로 내뱉어진 욕설.

나는 백염의 창대를 힘주어 부여잡았다.

그리고 때아닌 불청객들을 맞이하기 위해 이른 마중을 나온 어둠 너머의 적들을 응시하며, 청해성에서의 첫 명령을 내렸다.

“전투 준비.”

차차차창!

동시에 몸을 일으킨 무수한 강철의 파도가, 서늘한 빛이 되어 어둠을 밝혔다.

그것을 장막 삼아 다가오던 적들의 모습 역시도.

“……아, 아아.”

누군가의 입술 사이로 흘러나온 나직한 신음에, 가장 앞장서서 산등성이를 기어오르던 적이 고개를 갸웃거렸다.

투두둑.

이미 절반 가까이 사라진 머리에서 점점이 떨어지는 그것은, 그의 피부만큼이나 희멀건 뇌수(腦髓)였다.



* * *



기록조차 되지 않은 아득한 과거부터, 세인들은 머나먼 서쪽 끝자락에 위치한 어느 광활한 산맥을 가리켜 이렇게 칭했다.

“하늘과 가장 가까운 땅, 구름과 맞닿은 최고봉(最高峰)…….”

혼잣말처럼 뇌까린 혈주(血主)는 주위를 둘러보며 고개를 끄덕였다.

겹겹이, 그리고 끝없이 굽이굽이 이어진 산맥과 곳곳에 솟아 있는 수많은 산봉우리는 누가 보아도 탄성을 터트릴 만큼 장엄하면서도 아름다웠다.

“과연 볼만하군. 중원인들이 왜 그렇게 이곳을 신성시하는지 조금은 이해가 돼. 곤륜파(崑崙波)의 도사 나부랭이들이 어찌하여 그토록 악착같이 지키려 했는지도. 안 그래?”

혈주가 불쑥 던진 물음에, 커다란 바위에 앉아 알 수 없는 손짓을 하고 있던 대술사가 대꾸했다.

“이곳 경치가 썩 마음에 드는 모양이네, 당신은.”

“뭐, 다른 건 몰라도 천산(天山)이 삭막한 건 사실이니까.”

“그럼 이참에 곤륜파에 정식으로 입문을 청해 보는 건 어때. 혹시 알아? 언젠가 장문인이 될 수 있을지도.”

노골적인 조롱이 담긴 말이었지만, 그런 대술사의 의도와는 달리 혈주는 별다른 반응을 보이지 않았다.

다만, 알 수 없는 묘한 눈빛으로 그녀를 빤히 바라보다 이내 어깨를 으쓱해 보일 뿐이었다.

“그다지 구미가 당기는 제안은 아니군. 좀 더 그럴싸한 건 없나?”

아무렇지 않게 되받아치는 혈주의 대답에, 대술사는 자신도 모르게 미간을 찌푸렸다.

“도대체 뭐야?”

“뭐냐니, 그게 무슨 뜻이지?”

“당신, 애초에 이런 성격이 아니었잖아.”

“글쎄, 그랬던가.”

마지막 기억 속에 남아 있는 모습과는 다른 능청스러운 대꾸.

그런 혈주를 바라보는 대술사의 마음속에 짙은 불쾌감이 몽글몽글 피어올랐다.

‘정신 나간 괴물 주제에 괜히 여유로운 척은.’

혈검마군(血劍魔君)도 피에 굶주린 살귀였지만, 그보다도 마음에 들지 않는 것이 바로 혈주였다.

멍청하고, 잔인무도하며, 최소한의 수치심조차 모르는 자.

이 세 가지 문제점만으로도 싫어할 만한 이유로는 차고 넘칠 지경이었으나, 더욱 중요한 것은 따로 있었다.

‘그분께서는 왜 이런 놈을 가까이에 두시는 거지?’

도무지 이해할 수 없었다.

대술사가 보아 온 혈주라는 인물은 앞서 죽음을 맞이한 네 명의 마군과 마후보다 딱히 무공이 뛰어나지도, 심계가 깊은 것도 아니었으니까.

하지만 한낱 장기판 위의 말이었던 혈검마군과는 달리 혈주가 주인의 신뢰를 받는다는 것은 부정할 수 없는 사실이었고, 그가 자신과 동등한 위치에 있다는 점은 그녀를 더욱 불편하게 만들었다.

그리고 불과 수 장 밖에서, 시종일관 끔찍한 악취를 풍기고 있는 누군가의 존재 역시도.

쩔그럭. 쩔그럭.

대술사는 인상을 찡그린 채, 가부좌를 튼 채 쉴 새 없이 뭔가를 중얼거리는 흑의인을 바라보았다.

바람을 통해 전해지는 악취도 악취였지만, 흔들릴 때마다 둔탁하고 거슬리는 소음을 내는 방울 소리는 들을수록 거슬렸다.

마치, 송곳처럼 귓가를 후비고 마음속을 어지럽히는 것처럼.

“저자는 누구지?”

대술사의 물음에 혈주가 선선히 대답했다.

“내 수하.”

“당신이 부리는 수하 중에 저런 자가 있었나? 뭔가 풍기는 분위기가 묘하게 익숙하면서도 기분 나쁜데.”

“아무래도 그렇겠지. 술사니까.”

“뭐?”

“아, 오해하지는 마. 어떤 앙칼진 년과는 다른 종류의 술사니까. 사실 내 밑에 들어온 지도 얼마 되지 않았지.”

순간, 혈주의 뒷말에 담긴 뜻을 짐작한 대술사가 눈을 크게 떴다.

“그렇다는 건.”

“맞아. 불과 몇 달 전까지는 다른 마군(魔君)의 수하였던 놈이지. 뭐, 정확히는…….”

혈주가 입꼬리를 말아 올리며 덧붙였다.

“수하라기보다는, 제자였다고 해야겠지만.”

바로 그 순간.

떨그럭.

다시 한번, 동시에 유독 깊고 크게 울려 퍼진 둔탁한 방울 소리와 함께 흑의인이 고개를 들었다.

창백한 피부와 푸른 기운이 감도는 눈동자.

그리고 감정이 느껴지지 않는, 건조한 목소리.

“찾았습니다.”

지금으로부터 그리 오래되지 않은 과거.

한때 동창 병필태감(秉筆太監)으로서 황실을 주름잡았던 마삼보의 보고에 혈주가 만족스럽게 웃었다.

“그거 아주 반가운 소식이군 그래.”
```

## Final English reading copy

```markdown
# Chapter 1066

*Ding!*

> **System**
>
> Entered **Qinghai Province**.

At the timely chime of the System notification, I stopped in my tracks. I’d been clenching my fist and walking toward the Great Sir.

“You made the right call. There’s nothing to gain by hitting someone who’s already in rough shape… Are you listening to me?”

“Shh.”

Hyuk Mujin had let out a sigh of relief, thinking I’d changed my mind. I gestured for him to be quiet and looked around.

Dense forest lay under the cover of darkness, and insects chirped here and there.

The landscape around us hadn’t changed in the slightest, but there was no doubt that all of us—including me—had just crossed an invisible boundary.

The System was always accurate. It never lied.

And the Great Sir, who had somehow managed to fulfill the task assigned to him, wore the same baffled expression as the question marks that had floated above his head. He asked me,

“What is it, Jang Sam?”

“…I’m Jin Taekyung, not Jang Sam.”

To be honest, I’d doubted him right up to the end.

Following someone who couldn’t even remember his own name was, by anyone’s standards, a terrible idea.

What’s more, he kept changing direction along the way. Even people like Sama Pyo, who’d been born and raised in Gansu Province, had questioned him several times.

Still.

*The results speak for themselves.*

We’d cut at least two days off our journey compared to what I’d expected. And though we’d traveled through rough mountain country, we’d gained time to rest and recover our Stamina.

*The question is, how does this guy know a route like this?*

The obvious question surfaced again. But when I saw the Great Sir yawn so wide his jaw might split, my head shook before I knew it.

What good would it do to keep wondering?

He’d been out of his mind for ages, and now the System had officially certified him a Madman. There was no room left for doubt.

What mattered was that the Great Sir was, at the very least, on our side—and thanks to his help, we’d all reached Qinghai Province.

More precisely, the area near Qinghai Province’s northwest border.

*And this place is…*

Right.

Enemy territory, now under Dark Heaven’s control and filled with countless dangers.



* * *



Three thousand men.

Not a small number by any means.

In the modern world, a force of that many Hunters would be considered a major Guild. Even the other Nine Sects and One Gang, with the exception of the Beggars’ Sect, would have to call in even their lay Disciples outside the main sect to reach those numbers.

But everything was relative.

Considering that the Dark Heaven forces invading Qinghai were a great army comparable to the Hundred Thousand Demonic Disciples of old, three thousand men were no more than fireflies before the sun.

*This is urgent, but if we rush straight in with everyone this exhausted, we’ll be the ones getting slaughtered.*

So I proposed a day of rest in the mountain range where we’d paused our march. No one objected.

Not even Perfected Being Hyeoncheon, who could be considered my toughest opponent.

If anything, he went out of his way to show me more respect than necessary, which only left me flustered.

“A truly sound decision. Very well. What are your orders after we rest?”

“Sorry? My orders?”

“Is something wrong? I don’t mind if you call them commands instead.”

“…Just curse me out instead. Why are you doing this to me?”

Was this how a family heir felt when his grandfather’s generation bowed deeply to him during a holiday gathering?

At my thoroughly disconcerted reaction, Perfected Being Hyeoncheon gave a quiet laugh and said something I hadn’t expected.

“Why not take a look around you now and then?”

“What do you mean…?”

“Look at how many people are around you, and how they look at you. That is where you stand now.”

“……!”

Only then did I finally understand.

All those eyes fixed on me in that moment.

The deep admiration and goodwill in their gazes were so vivid I could almost reach out and touch them. Their faint smiles held a gratitude they couldn’t hide.

Then Perfected Being Hyeoncheon’s warm voice drifted into my ears.

“Whether it’s a request, an order, or a command, it makes no difference. We all owe you a great debt.”

“A debt…”

“Gratitude and grudges must always be repaid. That is the way of Murim. I forgave my grudge, and now I intend to repay the kindness. I imagine they feel the same.”

I thought for a moment about how they must feel.

They’d lost comrades they’d shared years of hardship with, family, Senior and Junior Brothers. Before they’d even begun to recover from the fear and sorrow they’d felt on the battlefield, they’d chosen of their own accord to follow me into another deadly place.

They had come to repay a debt, but they were also driven by a desire for revenge that would bring darkness to this land.

And that desire was, in itself, a light that would illuminate the darkness.

“Ah.”

It was a strange feeling, one I could never get used to.

I didn’t even know what to say.

But the old Daoist, whose wisdom matched his long life, didn’t demand a reply. He simply patted my shoulder a few times and walked away.

The attention of those who remained was fixed on me.

The Disciples of the Kongtong and Zhongnan Sects.

The martial artists of the Embroidered Uniform Guard and the Black Dragon Demon Gate.

Even Jeok Cheongang and Bow Saint, who stood among the Fire Dragon Pavilion members, silently nodded at me.

As though they’d follow me to the end, even if I were headed straight for hell.

“I… No, I…”

Under the gaze of all three thousand men, I slowly parted my lips.

And at the very moment the suffocating silence broke, a thought suddenly struck me.

*How can it possibly be this quiet?*

Only then did I realize that the loud chirping of insects hidden throughout the thick forest had stopped at some point.

The birds that had perched on the high branches were gone, too.

“……!”

A chill ran down my spine.

*Rumble. Rumble.*

A faint tremor finally reached us from far away. With it came the eerie cry of something unknown, carried to my ears on the desolate wind.

*Grrrk.*

“…Shit.”

The curse slipped out on reflex.

I tightened my grip on the shaft of White Flame.

I stared into the darkness at the enemies who had come out early to greet their unexpected visitors, then gave my first command in Qinghai.

“Prepare for battle.”

*Shing! Shing! Shing!*

Countless waves of steel rose all at once, their cold gleam lighting up the darkness.

And the enemies who had been approaching under its cover.

“……A-ah…”

At the low groan that slipped from someone’s lips, the enemy crawling up the ridge at the very front tilted his head.

*Plop. Plop.*

The drops falling from the head that had already lost nearly half its mass were as pale as his skin.

Brain matter.



* * *



From time immemorial, long before anything had been committed to the written record, people had called a vast mountain range at the far western edge of the world:

“The land closest to the heavens, the highest peaks touching the clouds…”

The Blood Lord murmured as if to himself, then looked around and nodded.

The mountain range stretched on in endless, overlapping ridges, its many peaks rising here and there. It was majestic and beautiful enough to make anyone gasp.

“Quite a sight. I can see why people of the Central Plains consider this place sacred. And why those worthless Daoists of the Kunlun Sect fought so stubbornly to protect it. Don’t you agree?”

At the Blood Lord’s sudden question, the Grand Mage, seated on a large rock and making strange gestures with her hands, answered,

“Seems like you’re quite taken with the scenery.”

“Well, whatever else you can say about Tianshan, it’s bleak.”

“Then why not formally apply to join the Kunlun Sect? Who knows? You might become its Sect Leader someday.”

Her words were openly mocking, but the Blood Lord showed little reaction to her intent.

He only stared at her with a strange, inscrutable look, then shrugged.

“That offer doesn’t tempt me much. Got anything better?”

The Blood Lord’s casual retort made the Grand Mage furrow her brow before she knew it.

“What’s gotten into you?”

“What do you mean?”

“You weren’t like this before.”

“Wasn’t I?”

His smooth reply was nothing like the man in her last memory of him.

As she watched the Blood Lord, a strong sense of displeasure gradually welled up inside her.

*Putting on airs, like he’s got all the time in the world. And he’s a deranged monster.*

The Blood-Sword Demon Lord had been a bloodthirsty killer, but the Blood Lord was even more unbearable.

Stupid, vicious, and without the slightest sense of shame.

Those three failings alone were more than enough reason to dislike him, but there was something else more important.

*Why does that person keep someone like this so close?*

She couldn’t understand it.

The Blood Lord she’d known wasn’t particularly skilled in martial arts, nor was he a deep thinker—unlike the four Demon Lords and the Demon Empress who had died before him.

But there was no denying that, unlike the Blood-Sword Demon Lord, a mere piece on the board, the Blood Lord had his master’s trust. And the fact that he stood on equal footing with her only made her more uncomfortable.

There was also the person sitting just a few *jang* away, who gave off a horrific stench without pause.

*Jingle. Jangle.*

The Grand Mage frowned as she looked at the man in black, sitting cross-legged and muttering something incessantly.

The foul odor drifting over on the wind was bad enough, but the dull, grating jingling of his bells every time he moved was even worse. The more she heard it, the more it grated on her.

As if an awl were scraping at her ears and stirring up her mind.

“Who’s that?”

At the Grand Mage’s question, the Blood Lord answered readily.

“My subordinate.”

“Did you have someone like him working for you? There’s something about him that feels oddly familiar, and unpleasant.”

“Probably because he’s a sorcerer.”

“What?”

“Oh, don’t get the wrong idea. He’s a different kind of sorcerer from a certain sharp-tongued bitch. He only joined my ranks recently, actually.”

For a moment, the Grand Mage’s eyes widened as she guessed what he meant.

“Then…”

“That’s right. Until a few months ago, he served another Demon Lord. Well, more precisely…”

The Blood Lord curled his lips into a smile and added,

“I should say he was his Disciple, rather than his subordinate.”

At that very moment—

*Clatter.*

Along with another dull bell sound, deeper and louder than before, the man in black raised his head.

Pale skin. Eyes tinged blue.

And a dry voice, without a hint of emotion.

“I found it.”

Not long ago.

At Ma Sanbao’s report—once the East Depot’s Brush-Holding Eunuch, and a man who’d held the imperial court in his grasp—the Blood Lord smiled with satisfaction.

“That’s very good news.”
```

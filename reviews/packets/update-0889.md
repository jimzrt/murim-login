<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0889.txt",
      "sha256": "2765a86332ef0e7843d5ad92416317a02f62961dac8a7b90ffed55fd613fb34b",
      "bytes": 12962
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "28239abb46e29cbecd528bf085ced10f46c5ee7bdb117aae2d96a3a4e003c8b2",
      "bytes": 2288
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "320ce751be3fb3e0a87bf53762efb7d7d993d82fdb6aaaeacad1a601ce4c4d7c",
      "bytes": 230284
    },
    {
      "path": "characters/Baek Yeon.md",
      "sha256": "d9afc2fcc5a7a7ec71c79a8a3bcbeb298af400f6bddd2a1b0121f0e8c026df2d",
      "bytes": 983
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "61d04c585979effe7746d0cc2fd585ae80044e1fbfd8f9a7d4d40bb148030035",
      "bytes": 1325
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "934188024481d5ca0645d0b5fa34207d9545fd414cbaeaf3042ad165c75bfa37",
      "bytes": 759
    },
    {
      "path": "characters/Hong Jin.md",
      "sha256": "23e7c62affb295e1a9abe5381c5f9c452f4c53773898630f7d0ea11bef927adf",
      "bytes": 837
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "1b1c73ee750a389c9deeb9a4a3bf85fbd8e823b0a1fd4721864aafa4f91210dd",
      "bytes": 1432
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "82066412f86bf61b9c6ffce093dbdf466d9dbbb35a4def1f8a50baf33392cc3d",
      "bytes": 1511
    },
    {
      "path": "characters/Jeong Hogun.md",
      "sha256": "7c18d3435652c7aa03efcdce0e91786f0657e5c0185659d7979ec670d949aaa4",
      "bytes": 628
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "3be08c8d5659669320011dc8a3ac793e2837cb214a56125cdd53ff812ae09bae",
      "bytes": 1782
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "b388317ffc9ef87e3ef9c10fa0dc7d2c3f27bce802c221a3f8a3048fa3a21e4a",
      "bytes": 622
    },
    {
      "path": "characters/Jung Ho.md",
      "sha256": "26dd3217c55c97f117a7b0f5fb9e39c58d497c7bbef32a29c9268375101e2063",
      "bytes": 699
    },
    {
      "path": "characters/Prince Shangshan.md",
      "sha256": "b61840a50b1d6bdaabdb96e29be27b274a319edb30742b36e36c1853e81d1494",
      "bytes": 952
    },
    {
      "path": "characters/So Gyo.md",
      "sha256": "379ff1c1409de731cbf1303fc0d9e5f3bbe1f4345d1e82559512af0718232a71",
      "bytes": 782
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "a9e4813b1ffcf8dcaf9b4070b00697ce7a532a563020b724ebc07a5d1bfc282a",
      "bytes": 259474
    }
  ],
  "estimated_tokens": 13607
}
-->

# Durable State Update — Chapter 889

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
1 and safe_through 889. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 889. Profile updates may replace only one
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
  "chapter": 889,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 889,
    "continuity_sources": [889],
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
    "The Emperor has confined Prince Shangshan Zhu Bao in Qianqing Palace; the prince’s safety prevents Taekyung from fighting So Gyo and Baek Yeon.",
    "The imperial grand banquet is approaching and is expected to become the decisive confrontation.",
    "So Gyo says her mission requires Taekyung to remain alive; Taekyung infers that the Lord of Heaven wants him alive, but the reason is unknown.",
    "So Gyo’s identity and allegiance remain unconfirmed; she is a Supreme Peak master and Taekyung’s opponent.",
    "Ma Sanbao leads a covert faction seeking to enthrone Prince Shangshan; assassins brought into the palace by Ma Sanbao remain present.",
    "Taekyung suspects the Emperor is connected to Dark Heaven, but this is unconfirmed.",
    "The late Emperor died after mental confusion while confined; Taekyung suspects Blood Soul Gu may have been involved. Blood Soul Gu was found in the City Lord of Sichuan Province’s corpse after he showed strange symptoms.",
    "Baek Yeon is the Commander of the Embroidered Uniform Guard and carries the weapon Golden Dragon, made of Ten-Thousand-Year Cold Iron."
  ],
  "continuity_sources": [
    888
  ],
  "open_questions": [
    "Who is So Gyo, and whom does she serve?",
    "Why does the Lord of Heaven want Taekyung alive, and what mission was So Gyo given?",
    "What does the Emperor intend at the banquet, and will it become a confrontation?",
    "Did the Emperor or Dark Heaven use Blood Soul Gu against the late Emperor and the City Lord of Sichuan Province?",
    "What preparations has Ma Sanbao’s faction made, and who is the person his allies asked about?"
  ],
  "safe_through": 888,
  "temporary_decisions": [
    "Render 기관진식 as “mechanisms and formations”; retain “Third Shadow,” “First Shadow,” “No Shadow,” and “Marquis Within the Passes.”",
    "Use “imugi,” not “dragon,” for the creature Taekyung killed at Dongting Lake.",
    "Render 연판장 as “a pact bearing their signatures”; retain “Hongmen Banquet” for 홍문연.",
    "Treat 거산 as Taishan’s uncertain name variant, not a confirmed separate person; render 열화단 as “Blazing Flame Troupe” and 마희단 as “circus troupe.”"
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 청풍     | **Cheongpung**     |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 후기지수   | **young prodigy** / **rising martial artist**    | Contextual, not a title                               |
| 마교     | **Demonic Cult**                                 |                                                       |
| 전각     | **pavilion**                                 | Use “hall” only when established for a specific named building |
| 화산     | **Huashan**            |
| 정마대전   | **Great Faction War**         |
| 공자      | **Young Master**                                                |
| 백연 | **Baek Yeon** | Commander of the Embroidered Uniform Guard. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 홍진 | **Hong Jin** | Level 22 man at the City Lord's luncheon; delicate in appearance and voice. |
| 정호군 | **Jeong Hogun** | Commander of the Embroidered Uniform Guard force confronting Jin. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 정호 | **Jung Ho** | Middle-aged Shaolin martial monk leading the traveling group. |
| 상산왕 | **Prince Shangshan** | The City Lord and a member of the imperial family who orders the luncheon. |
| 소교 | **So Gyo** | The palace attendant leading the group assigned to serve Prince Shangshan. |
| 황상 | **Emperor** | Address or reference to the reigning Emperor. |
| 선황 | **the late Emperor** | The former Emperor whom Hong Jin served. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 노야 | **Old Master** | Taekyung's private address for Jeok Cheongang. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 화산신룡 | **Huashan Divine Dragon** | Title given to Cheongpung after the Star-Array Grand Banquet. |
| 성도 | **Chengdu** | Sichuan destination of Taekyung's party. |
| 살수 | **assassin** | Professional killer considered as a possible suspect. |
| 유령환살보 | **Ghost Illusory Slaughter Step** | Movement technique used by the Slaughter Saint. |
| 열화신룡 | **Blazing Flame Divine Dragon** | New sobriquet bestowed on Jin Taekyung. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 이전 | **Two Halls** | Top-level Murim Alliance organizational grouping. |
| 인시 | **Insi** | The traditional time period from three to five in the morning. |
| 화원 | **Fire Courtyard** | Courtyard associated with Jin Taekyung and Ju Hwaran's final walk before leaving Sichuan. |
| 외궁 | **Outer Palace** | The outer compound of the Nanman Beast Palace. |
| 궁인 | **palace attendant** | Former Inner Palace attendant expelled by Baeksang. |
| 화신 | **Fire God** | A local deity worshiped by one Nanman believer. |
| 금의위 | **Embroidered Uniform Guard** | Imperial guard force mentioned by Hong Jin. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
| 청풍 | 진태경 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung repeatedly addresses Taekyung as 은인 after receiving food. |
| 청풍 | 혁무진 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung includes Mujin among his 은인들 after receiving the skewers. |
| 혁무진 | 청풍 | martial artist to young master | Young Master | formal-deferential | Mujin uses 공자께서는 when asking why Cheongpung descended from the mountain. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 진태경 | 청풍 | companion_to_young_martial_artist | Young Master Cheongpung | formal-polite | Taekyung uses 청 공자 while correcting Cheongpung's royal-etiquette mistake. |
| 홍진 | 진태경 | political_host_to_young_martial_artist | Young Hero Jin; Young Master Jin; Sleeping Dragon of Shanxi | polite, coaxing, and probing | Uses respectful forms while steering Taekyung toward relaying the Escort Bureau proposal and teasing him with the Seongun Escort Bureau. |
| 진태경 | 홍진 | young_martial_artist_to_political_official | Comrade Chairman—no, Deputy Military Commissioner | casual and teasing, then formally corrective | Deliberately jokes with an inappropriate title before correcting himself to Hong Jin's official office. |
| 홍진 | 청풍 | political_official_to_young_martial_artist | Young Master | formal and curious | Uses 공자께서는 while asking whether Cheongpung has always lived on Huashan. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 적천강 | 청풍 | overwhelming_elder_to_young_martial_artist | you / little punk | blunt, amused, and threatening | Jeok Cheongang uses 네, 이놈, and related blunt forms while testing Cheongpung. |
| 청풍 | 적천강 | young_martial_artist_to_overwhelming_elder | Grandpa Jeok | casual-familiar despite deference | Cheongpung uses 적 할아버지 while asking Jeok Cheongang to confirm Taekyung's condition; this is a familial form of address, not literal kinship. |
| 혁무진 | 적천강 | subordinate_to_overwhelming_elder | Great Hero Jeok | deferential and fearful | Mujin uses 적 대협 while reporting Jeok’s orders and Taekyung’s awakening. |
| 적천강 | 혁무진 | overwhelming_elder_to_junior_martial_artist | you stupid fool | blunt and mocking | Jeok calls Mujin a 멍청한 놈 after knocking him down during the attempted escape. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 정호 | 진태경 | Shaolin Discipline Hall Master to patient and Benefactor | Benefactor Jin | formal-polite | Jung Ho repeatedly uses 진 시주 and 시주. |
| 진태경 | 정호 | patient to Shaolin Discipline Hall Master | Monk | polite and familiar | Taekyung addresses Jung Ho as 스님. |
| 진태경 | 정호군 | young martial artist to senior imperial officer | Commander Jeong | casual and teasing, then conciliatory | Jin addresses him by rank while trying to defuse the standoff. |
| 홍진 | 혁무진 | imperial aide addressing a martial artist accompanying the prince | Martial artist Hyuk | polite and conversational | Uses 혁 무인 when asking whether Mujin knows of an exception. |
| 백연 | 정호군 | commander to subordinate | you | direct and commanding | Uses 네 while testing Jeong Hogun’s obedience. |
| 홍진 | 백연 | imperial aide confronting a senior military officer | you | angry and confrontational | Uses 당신 in an indignant outburst. |
| 진태경 | 백연 | young martial artist confronting an imperial military commander | you | casual and insulting | Refers to Baek as 이 양반 while challenging his conduct. |
| 진태경 | 상산왕 | protector addressing a young prince | His Highness | respectful royal address | Taekyung refers to the prince as 상산왕 전하 when ordering Mujin to bring him. |
| 정호군 | 상산왕 | imperial guard officer escorting the prince | His Highness | formal and deferential | Hogun formally reports that he has come to escort the prince. |
| 정호군 | 홍진 | Embroided Uniform Guard officer addressing a senior imperial official | Deputy Military Commissioner | formal and admonishing | Hogun tells Hong Jin to mind his words. |
| 진태경 | 황제 | guest of the Emperor’s younger brother addressing the Emperor | Your Majesty | formal and deferential in address, despite blunt challenges | Taekyung repeatedly addresses the Emperor as 폐하. |
| 상산왕 | 황제 | younger brother addressing the Emperor | Your Majesty | deferential royal address | Shangshan addresses the Emperor as 폐하 while pleading for Taekyung. |
| 소교 | 진태경 | palace attendant addressing a martial artist and guest under escort | Young Master Jin | formal and respectful, but firm | Addresses him as 진 공자 while escorting him and warning him not to investigate. |
| 혁무진 | 홍진 | martial artist addressing a senior official and political ally | Comrade Hong | casual and coaxing | Hyuk Mujin addresses Hong Jin as 홍 동지님 while trying to calm him and de-escalate the confrontation. |
| 홍진 | 정호군 | Embroided Uniform Guard officers of equal rank | Thousand Captain Jeong | polite and direct | Hong Jin addresses Jeong Hogun by rank and surname. |
| 진태경 | 소교 | palace attendant and martial artist under imperial scrutiny | you | formal-polite, controlled and challenging | Taekyung addresses So Gyo as 당신 while questioning her presence and demanding an explanation. |
| 백연 | 진태경 | imperial commander confronting a young martial artist | Jin Taekyung | measured and familiar, using 자네 | Baek Yeon cautions Taekyung about his words and asks whether he must cause a scene. |

## Listed compact profiles

### Baek Yeon.md

# Baek Yeon (백연)

- **Safe through:** Chapter 888
- **Aliases:** Blood Envoy
- **Role:** Baek Yeon is the Commander of the Embroidered Uniform Guard, a former martial arts instructor to the Crown Prince, and the Blood Envoy who helped the fourth prince seize the throne and led the purge.
- **Personality:** Politically assured and controlled, he enforces authority with ruthless decisiveness but speaks with striking defiance to the Emperor in private when their shared undertaking is at stake.
- **Voice:** Not established
- **Relationships:** He commands the Embroidered Uniform Guard and serves the Emperor; they share an old promise tied to a great undertaking, and Baek urges the Emperor to restore matters before their adversaries' moves unravel it. He orders Jeong Hogun to surveil Prince Shangshan’s party while leaving openings for an approach, and treats Taekyung as a dangerous potential obstacle.

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 886
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, the grandson and Disciple of Sword Saint Mae Jonghak, a Supreme Peak martial master known as the Huashan Divine Dragon, the creator of the snake-inspired Mimi Step footwork technique, and the master of the Azure Dragon Pavilion within the Alliance Leader's Two Dragons Pavilion.
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, a deep love of martial arts, competitive pride, unusual resistance to monster-induced Fear, and discomfort when someone copies his martial arts.
- **Voice:** Dreamy and hazy, with innocent, polite phrasing; he has begun imitating Taekyung's profanity.
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions while Taekyung is his only true martial rival; Tang Sadok has temporarily entrusted Mimi, now a large horned snake, to him, and Cheongpung is accompanying Mungyeong while learning his martial arts through observation to become stronger and adapt to this world.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 888
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Hong Jin.md

# Hong Jin (홍진)

- **Safe through:** Chapter 884
- **Aliases:** None
- **Role:** Hong Jin is a Level 22 Deputy Military Commissioner of Shanxi Province, a eunuch and trusted aide to Prince Shangshan, and a former member of the East Depot.
- **Personality:** Composed, socially deft, and ambitious, Hong Jin became a eunuch to escape poverty and save his family, then used his abilities to pursue a broader life.
- **Voice:** Delicate and deferential, using formal, self-effacing language with Prince Shangshan.
- **Relationships:** Hong Jin is devoted to Prince Shangshan, whom the late Emperor entrusted to his care; the Fourth Prince spared him because of their old ties, and his longtime friend and former East Depot cohort Ma Sanbao stayed behind in the palace.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 880
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and an active member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented; loyal even when left behind, irreverently self-deprecating, and willing to face danger rather than abandon the person he serves. He is proud, glory-seeking, suspicious of Taekyung, bluntly critical of the family's disgraced third son, and an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; with Taekyung, blunt and occasionally incredulous, while using breezy, irreverent banter to defuse tense situations.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad; as a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Fire Dragon Pavilion members accompanying Taekyung. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 888
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm, the occupant of the chief seat of the Murim Alliance's Five Kings Hall, and a trusted confidant who accepts Jin as himself despite knowing that he travels between Murim and another world resembling the realm of immortals.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He deeply trusts his publicly acknowledged Disciple and intended heir Jin Taekyung, warmly regards Ju Hwaran and hopes she and Jin grow closer, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and remains Peng Cheolhu's rival.

### Jeong Hogun.md

# Jeong Hogun (정호군)

- **Safe through:** Chapter 884
- **Aliases:** None
- **Role:** Jeong Hogun is a Thousand Captain of the Embroidered Uniform Guard and a highly skilled martial artist whose force includes dozens of Peak masters.
- **Personality:** Disciplined and resolute, he follows imperial orders without hesitation and reads the political consequences of events with care.
- **Voice:** Formal and rigid, emphasizing duty to imperial authority.
- **Relationships:** Jeong Hogun serves under Baek Yeon’s command in the Embroidered Uniform Guard.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 888
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader.
- **Personality:** Hungry, self-aware, dryly observant, and pragmatic under pressure; accepts extreme personal risk when duty and the lives of others demand it.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; they trust each other deeply, though their bond remains unformalized. Cheongpung is his trusted companion and only true martial rival; Choi Minwoo is his subordinate and trusted manager of media and official arrangements as well as the Peace Guild's Guild Master; Ju Hwaran is a trusted Fire Dragon Pavilion member; Magic Johnson and Chuck Hagel are allied to him; his mother and sister Hayeon are among those he protects; the Skeleton King is his friend and ally; Xiao Shen regards him as an older brother; Jin-ho is his older friend and trusted confidant; he once saved Ju Wongong’s life.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 888
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Jung Ho.md

# Jung Ho (정호)

- **Safe through:** Chapter 884
- **Aliases:** None
- **Role:** Middle-aged Shaolin martial monk and Master of Shaolin's Discipline Hall who leads the traveling group and wields a Zen staff hung with prayer beads.
- **Personality:** Humble, observant, principled, and concerned with the safety of commoners.
- **Voice:** Formal, restrained, and admonitory, with Buddhist phrasing.
- **Relationships:** Unnamed is his young Martial Uncle; he leads the Shaolin monks traveling with him, addresses Sama Pyo as a Benefactor, and is recognized by Jin Taekyung as Park Jung Ho, a former Garam Middle School classmate.

### Prince Shangshan.md

# Prince Shangshan (상산왕)

- **Safe through:** Chapter 888
- **Aliases:** None
- **Role:** Prince Shangshan, whose personal name is Zhu Bao, is the Emperor’s twelve-year-old youngest younger brother and an exceptionally skilled young swordsman.
- **Personality:** Earnest and compassionate, he takes responsibility for his loyal subjects’ hardship, admires Jin Taekyung, seeks candid counsel, and shows composure beyond his years in the face of death and political danger.
- **Voice:** Archaic and formal in the manner of a historical drama, with openly eager and childlike reactions beneath his royal diction.
- **Relationships:** Prince Shangshan Zhu Bao is the Emperor’s youngest younger brother; the late Emperor entrusted Hong Jin with his care. Zhu Bao admires Jin Taekyung, seeks to emulate him, and calls him a friend; the Emperor says he will take care of Zhu Bao.

### So Gyo.md

# So Gyo (소교)

- **Safe through:** Chapter 888
- **Aliases:** None
- **Role:** A palace attendant assigned to Prince Shangshan who is a Supreme Peak master and has a mission to keep Jin Taekyung alive; her identity and allegiance remain unconfirmed.
- **Personality:** Calm, calculating, and self-possessed; she conceals her strength and identity and can be openly taunting.
- **Voice:** Measured and composed, shifting from deferential formality to casual, pointed taunts and threats.
- **Relationships:** She poses as the leader of the palace attendants assigned to Prince Shangshan and is Jin Taekyung’s opponent; she says her mission requires him to stay alive, while her true allegiance remains unknown.

## Korean source

```text
＃889화



떠날 사람은 떠나고, 남을 사람은 남는다.

어느덧 저 멀리 사라져 버린 진태경의 뒷모습을 응시하던 소교는, 조금 전 바람 섞여 들려오던 희미한 목소리를 곱씹었다.



‘아직 어린애라고. 미친 새끼들아.’



소교는 문득 궁금해졌다.

그때의 진태경이 무슨 표정을 짓고 있었을지. 분노와 씁쓸함이 묻어 나던 그의 뒷모습에는 얼마만큼의 진심이 담겨 있었는지.

그러나 그녀로서는 알 방법이 없었다.

‘열 길 물속은 알아도 한 길 사람 속은 모르는 법이니까.’

소교가 마음속으로 뇌까리던 그때, 백연이 불쑥 입을 열었다.

“어디까지 의도했던 거요?”

“의도?”

“진태경이 이곳까지 온 것이, 그대가 의도했던 게 아니었소?”

소교가 작게 고개를 저었다.

“딱히. 조금 전의 상황은 그저 우연이었을 뿐이야.”

“우연이라, 그럼 황상께 저자의 운신을 자유롭게 해 달라 요청했던 이유는…….”

“나로서는 그를 더 자세히 지켜봐야 할 필요가 있었으니까. 당신도 이미 알고 있지 않나? 내가 황궁에 머물렀던 몇 가지 이유를.”

“그렇다면 혹시?”

문득 눈을 크게 뜬 백연을 향해, 소교가 담담한 목소리로 대답했다.

“아직 확신할 수는 없지만…… 아마도 그가 맞을 거야. 내가 찾던 사람. 그리고 그분께서 예견하셨던 인물이.”

삼십 대의 미부(美婦)가 반백의 노장에게 건네는 말에는 조금의 격식도 없었으나, 백연은 그런 것 따위에 신경 쓰지 않았다.

소교라는 이름을 쓰는 저 여인은 그럴 만한 자격과 힘을 갖춘 인물이었고, 조금 전의 대답은 생각했던 것 이상으로 놀라운 것이었으니까.

“그래서, 그래서 그를 황궁에 머무르게끔 했던 거요?”

“직접 확인해 봐야 했으니까. 열화신룡 진태경을 둘러싼 소문이 진실인지, 정말 그분께서 말씀하신 자가 맞는지. 또…….”

소교가 고개를 움직였다. 이제는 보이지 않는 누군가가 머물렀던 자리를 훑던 그녀의 시선이 한순간 날카롭게 빛났다.

“그가 어떤 사람인지.”

다행히 이 우연한 만남의 결과는 훌륭했다. 분노를 머금고 떠난 진태경에게는 아니었겠지만, 소교는 나름대로의 확신을 얻어 생각을 정리할 수 있었으니까.

‘화산신룡 청풍. 열화신룡 진태경.’

소교는 언젠가부터 주시하고 있던 두 후기지수의 이름을 마음속 저울추에 올려 두었다.

그리고 처음 그들에 관한 정보를 접했을 때와 달리, 한 사람을 향해 기울어져 있는 저울추를 확인할 수 있었다.

‘열화신룡 진태경.’

백연에게 했던 대답대로 아직은 섣불리 확신할 수 없었지만, 지난 행적과 직접 보고 느낀 바에 의하면 진태경이 그녀가 찾는 사람일 가능성은 충분했다.

‘그러니 그분께서도 내게 이 일을 맡긴 거겠지.’

내심 뇌까린 소교는 천천히 화원을 가로질렀다.

앞서 벌어진 잠깐의 격돌로 인해 폭풍이라도 휩쓸고 간 것처럼 엉망이 된 그곳의 중심에는, 꽃과 풀에 가려져 보이지 않던 무언가가 흙 사이로 고개를 내밀고 있었다.

“오랜만이구나.”

얼마나 깊숙이, 또 오랫동안 이곳에 파묻혀 있던 것일까.

익숙한 모습을 한 그것을 향해 혼잣말처럼 인사를 건넨 소교는 손을 뻗었다.

우우웅, 텅!

보이지 않는 거대한 기운이 공기를 뒤흔듦과 동시에, 땅 깊숙이 박혀 있던 두 개의 물체가 솟구치듯 소교의 양손에 잡혔다.

마치 자로 잰 듯, 조금의 오차도 없이 동일한 길쭉한 길이와 폭. 거기에 더해 끝으로 갈수록 부드럽게 휘어진 곡선까지.

흡사 곡도(曲刀)를 연상시키는 그것들을 각각 양 허리에 찬 소교는 자신을 바라보고 있던 백연을 향해 입을 열었다.

“치열한 전투가 될 거야. 어쩌면 십여 년 전보다도 더.”

백연이 고개를 끄덕였다.

“이미 각오했소.”

“목숨을 걸 만큼?”

“그거 아시오?”

되물음과 동시에 백연이 담담한 얼굴로 말을 이었다.

“나는 항상 원하는 바를 이루기 위해 목숨을 걸었소. 그랬기에 여기까지 올 수 있었고.”

“이번에도 그러길 바라지.”

“그래야 하오. 반드시.”

백연의 눈빛이 목소리만큼이나 무겁게 가라앉았다.

“한 가지만 물어봐도 되겠소?”

소교가 고개를 끄덕였다.

“뭐든지. 내가 대답할 수 있는 선에서라면.”

“열화신룡 진태경. 그자를 이대로 내버려 두는 이유가 뭐요?”

“이유?”

“그렇소.”

“당신도 이미 짐작하고 있을 텐데?”

“물론이오. 그러나 놈들을 한자리에서 일망타진(一網打盡)하는 것보다 먼저 지금 당장 진태경부터…….”

“불가(不可).”

이어지려는 백연의 말을 단호하게 끊어 낸 소교가 입을 열었다.

“아직 확인할 것이 더 남았어. 그때까지는 상황이 이대로 흘러가도록 놔두는 것이 나아.”

“만약 그가 대업(大業)에 방해가 된다면?”

“방해라. 이를테면?”

“그대도 알다시피 진태경의 스승은 화왕(火王) 적천강이오. 그리고 황도에 이르러 공교롭게도 종적이 묘연해졌지. 진태경을 따르는 다른 무림인들이야 대세에 별 지장을 줄 수 없겠지만…… 놈들이 화왕마저 끌어들인다면 일이 복잡해질 수 있소.”

백연은 진심으로 우려하고 있었다.

화왕 적천강.

관과 무림이 불가침이라고는 하나, 장장 일백 년이 넘는 세월을 살아온 그의 위명은 천하에서 모르는 이가 없다.

그리고 선황 시절부터 금의위의 수장이었던 백연은, 화왕 적천강을 둘러싼 무수한 소문들의 진위여부를 누구보다 잘 알고 있는 사람 중 하나였다.

정마대전이 낳은 영웅. 마교가 깨운 악마.

감히 왕이라 칭해지는 강자들 중에서도 단연 압도적인 무위.

인간의 몸으로 태어나 신이라 불리게 된 누군가에게는 닿을 수 없으나, 세 개의 별과는 어깨를 나란히 한다는 그가 반대편에 선다면 엄청난 피해를 각오해야 할 것이 틀림없었다.

설령 아군에 소교가, 자신이, 그리고 황제를 비롯한 여러 초절정 고수가 있다고 하여도.

“저들의 전력은 이미 충분히 막강하오. 지금껏 파악한 것만으로도 그 정도일진대, 이대로 진태경에 이어 화왕까지 놈들과 손을 잡는다면…….”

“화왕이라, 나쁘지 않네.”

순간, 백연은 자신의 귀를 의심했다.

그리고 입가에 희미한 미소를 띤 채 말을 잇는 소교의 모습에, 조금 전 들었던 대답이 사실이었다는 것을 깨달았다.

“아니, 오히려 그편이 좋겠는걸.”

“……!”

도무지 이해할 수 없는 말에 석상처럼 굳어 버린 백연을 뒤로한 채, 소교는 피식 웃으며 돌아섰다.

말해 주지 않은 뒷말을 마음속으로 흘려보내며.

‘기다려. 당신도 곧 알게 될 테니.’

백연은 모든 것을 알고 있다고 생각했겠지만, 틀렸다.

지금 말해 주지 않은 이야기는 소교와 황제만이 알고 있는 것이었고, 비밀은 알려지지 않을수록 좋은 법이었다.

아군과 적군. 모두가 기다려 마지않는 연회가 열리기 전까지는.

“그날까지, 이제 겨우 사흘인가.”

소교는 어느새 어두컴컴해진 하늘을 바라보며 중얼거렸다. 이미 시작된 폭풍전야(暴風前夜)를 직감하듯, 차가운 빗방울이 떨어져 내리기 시작했다.



* * *



솨아아아.

거센 빗줄기가 사방을 두드렸다.

대나무를 엮어 만든 죽립과 우의(雨衣) 따위를 걸친 궁인들이 곳곳을 뛰어다니며 큰소리로 외치는 것조차 집어삼킬 만큼.

무림에서 제법 긴 시간을 보낸 나조차도 처음 겪을 정도로 유례없는 폭우(暴雨)였고, 예상치 못한 이 빗줄기와 천둥은 감시자들의 시야를 가리기에 충분했다.

“정말 가시게요?”

긴장한 얼굴로 묻는 혁무진에게 내가 대답했다.

“가야지.”

“그러다가 발각되기라도 하면…….”

“그럴 일 없어. 그럴 상황도 아니고. 너도 옆에서 들었으니까 알잖아.”

“알죠. 급한 상황인 거. 하지만 아무리 그래도.”

“괜찮을 거예요. 진 공자라면.”

불쑥 입을 연 홍진이 가라앉은 목소리로 말을 이었다.

“설령 발각된다고 하더라도, 모른 척할 가능성도 높고요.”

“예? 그게 무슨.”

“진 공자가 알려 준 것이 사실이라면 저들이 원하는 건 일망타진이에요. 이 기회에 단번에 뿌리를 뽑겠다는 건데…… 우리로서는 선택의 여지가 없어요.”

나는 말없이 고개를 끄덕였다.

소교와 백연이 아무런 생각도 없이 나를 놔줬을까?

이 이야기가 자신의 적들에게 흘러갈 것을 뻔히 알면서도?

‘그럴 리가.’

이건 경고인 동시에 통보다. 건곤일척(乾坤一擲)의 승부를 피하지 말라는 통보. 그리고 우리는 그 통보를 거부할 수 없다.

‘상산왕이 놈들의 손아귀에 넘어간 이상, 무슨 수를 써도 피할 수 없어.’

적들이 이런 상황을 유도했다는 것은 승리에 대한 확신이 있다는 뜻. 하지만 얼마나 철저한 준비와 함정이 있다 하더라도 아군으로서도 뒷걸음질 칠 수는 없었다.

‘싸워야 한다. 지금은 승패(勝敗)를 걱정하기 이전에 우선 결단해야 할 때야.’

이미 무대도, 배우도 마련되었다.

적들이 무대를 꾸민 이상 자신들을 주연으로 한 무대겠지만, 때로는 모두의 예상을 뒤엎고 조연이 주연보다도 빛날 때가 있다.

바로 그것이 내가 해야 할 일이다.

곧 시작될 무대의 주연을, 이 시나리오의 결말을 바꾸는 것.

그리고 다행히도 현재 황궁에는 적들이 모르는 중요한 카메오가 한 사람 있었다.

‘노야.’

나는 장대비가 쏟아져 내리는 창밖을 응시했다.

빗줄기에 가려진 시야와 이미 캄캄하게 물든 하늘. 전각 아래에는 돌아가며 번을 서고 있는 금의위들이 있다.

숫자는 대략 이십여 명에, 하나같이 절정의 고수들.

그러나 그들이 설령 초절정 고수라 해도, 갑작스럽게 내리치는 낙뢰(落雷)마저 예측할 수는 없다.

번쩍. 쿠구궁!

‘지금.’

새하얀 빛과 동시에 굉음이 울려 퍼진 그 순간. 나는 부드럽게 난간을 박차고 솟아올랐다.

쉭!

고금제일의 살수가 창안한 독문무공, 유령환살보(幽靈幻殺步)가 발끝에서 펼쳐졌다.

정식으로 사사한 것이 아니라 그저 가미한 것이 고작이지만, 잠깐의 혼란을 틈타 감시의 시선을 벗어나기에는 그것으로도 충분했다.

툭. 쉬릭!

궁인들의 숙소로 쓰인다는 이름 모를 전각 위로 착지한 나는 은밀하게, 그러나 쾌속하게 신형을 쏘았다.

이미 머릿속 깊이 각인시켜 둔 황궁 내부의 구조를 떠올린 내 발걸음에는 일말의 망설임도 없었다.

‘여기서 동서쪽.’

넓다 못해 광활한 공간과 그 사이사이 늘어선 전각들.

전신에 두른 흑의(黑衣)는 어둠에 잘 녹아들 수 있게 해 주었고, 곳곳에 배치된 경계병들은 내 움직임을 포착할 수 없었다.

“빌어먹을. 지독하게 쏟아붓는군.”

“대연회가 코앞인데, 날씨가 이래서야 원…….”

처마 밑에서 하늘을 바라보며 투덜거리던 금위군들은 꿈에도 몰랐을 것이다.

바로 두 걸음 뒤에서 허락받지 않은 불청객이 지금 막 자신들을 지나쳐 외궁(外弓)에 들어왔다는 것을.

하지만 모든 것이 순탄하게 흘러가는 것만은 아니었다.

“여기서 무엇을 하고 있나.”

“추, 충(忠)!”

“본관이 아는 규정대로라면, 정해진 근무 위치가 처마 밑은 아닐 텐데.”

바위처럼 딱딱한 누군가의 목소리에 놀란 것은 금위군뿐만이 아니었다. 막 자리를 옮기려던 나는 갑작스럽게 등장한 익숙한 얼굴을 보며 침음성을 삼켰다.

‘시벌, 저 새끼가 여기에서 왜 나와.’

정호군.

금의위에서 천호라는 고위직을 맡고 있는 그가, 금위군을 향해 다가오고 있었다.

아니, 그와 동시에 그리 멀지 않은 어둠 속에 숨어 있던 내게.
```

## Final English reading copy

```markdown
# Chapter 889

Those who were going to leave left. Those who were going to stay stayed.

So Gyo watched Jin Taekyung’s back until it vanished in the distance, turning over the faint words she’d heard moments ago, carried to her on the wind.

*“He’s still a kid, you crazy bastards.”*

So Gyo suddenly wondered what expression Jin Taekyung had worn when he said it. How much sincerity had been in the back of him as he left, with anger and bitterness hanging over him?

But there was no way for her to know.

*You can plumb ten fathoms of water, but never one fathom of a person’s heart.*

As So Gyo repeated the saying to herself, Baek Yeon abruptly spoke.

“How much of this did you intend?”

“Intend?”

“Jin Taekyung coming here. Was that what you intended?”

So Gyo shook her head slightly.

“Not particularly. What happened just now was only a coincidence.”

“A coincidence. Then the reason you asked His Majesty to let him move about freely…”

“I needed to keep a closer eye on him. You already know some of the reasons I’ve been staying in the imperial palace, don’t you?”

“Could it be…?”

So Gyo answered Baek Yeon, whose eyes had suddenly widened, in an even voice.

“I can’t be certain yet…but I think he’s the one. The person I’ve been looking for. And the person that person foretold.”

There was not a trace of formality in the words the beautiful woman in her thirties spoke to the half-white-haired veteran, but Baek Yeon paid it no mind.

The woman calling herself So Gyo had the standing and the strength to speak that way. And her answer just now was more astonishing than he’d expected.

“So that’s why you made him stay in the imperial palace?”

“I had to see for myself. Whether the rumors surrounding the Blazing Flame Divine Dragon, Jin Taekyung, were true. Whether he really was the one that person spoke of. And…”

So Gyo turned her head. Her gaze swept over the place where someone had been moments ago, though that person was already gone. For an instant, her eyes gleamed sharply.

“What kind of person he is.”

Fortunately, the outcome of this chance encounter had been excellent. Perhaps not for Jin Taekyung, who had left with anger in his heart, but So Gyo had gained a measure of certainty and sorted out her thoughts.

*The Huashan Divine Dragon, Cheongpung. The Blazing Flame Divine Dragon, Jin Taekyung.*

So Gyo placed the names of the two rising martial artists she had been watching for some time on the scales in her mind.

And unlike when she’d first heard of them, she could see the scales tipping toward one of them.

*The Blazing Flame Divine Dragon, Jin Taekyung.*

As she’d told Baek Yeon, it was too soon to be certain. But given Jin Taekyung’s past actions and what she’d seen and sensed herself, there was every chance he was the person she was looking for.

*That must be why that person entrusted this task to me.*

Thinking this to herself, So Gyo slowly crossed the flower garden.

The place had been left in shambles by their brief clash, as if a storm had swept through it. At its center, something hidden beneath the flowers and grass poked up through the dirt.

“It’s been a long time.”

How deep beneath the ground had it been buried, and for how long?

So Gyo greeted the familiar-looking object as if speaking to herself, then reached out.

Whoooom—THUNK!

As an enormous, unseen surge of qi shook the air, two objects buried deep in the ground shot up into So Gyo’s hands.

They were exactly alike in length and width, as if measured with a ruler. Each also curved gently toward its tip.

They looked much like curved sabers. So Gyo hung one at each hip, then spoke to Baek Yeon, who had been watching her.

“It’ll be a fierce battle. Maybe fiercer than the one over a decade ago.”

Baek Yeon nodded.

“I’m prepared.”

“To the point of staking your life?”

“Do you know something?”

Baek Yeon followed the question with a calm reply.

“I’ve always staked my life to get what I wanted. That’s how I made it this far.”

“I hope you do the same this time.”

“I must. I will.”

Baek Yeon’s eyes sank as heavily as his voice.

“May I ask you one thing?”

So Gyo nodded.

“Anything, within what I can answer.”

“Why are you leaving the Blazing Flame Divine Dragon, Jin Taekyung, alone?”

“Why?”

“That’s right.”

“You must have guessed already.”

“Of course I have. But before we wipe them all out in one place, we should go after Jin Taekyung right now—”

“Impossible.”

So Gyo cut Baek Yeon off firmly, then spoke.

“There are still things we need to confirm. Until then, it’s better to let things proceed as they are.”

“What if he becomes an obstacle to the great undertaking?”

“An obstacle. For example?”

“As you know, Jin Taekyung’s master is the Fire King, Jeok Cheongang. And, by coincidence, he vanished without a trace after reaching the imperial capital. The other Murim martial artists following Jin Taekyung won’t make much difference to the larger situation, but…if they draw the Fire King in as well, things could become complicated.”

Baek Yeon was genuinely worried.

The Fire King, Jeok Cheongang.

Though the government and Murim were meant to stay out of each other’s affairs, there wasn’t a soul in the land who hadn’t heard of the man’s fame after more than a hundred years of life.

And Baek Yeon, who had led the Embroidered Uniform Guard since the late Emperor’s reign, was among those who knew better than anyone whether the countless rumors surrounding the Fire King were true.

A hero born of the Great Faction War. A demon awakened by the Demonic Cult.

A martial prowess that towered above even those powerful enough to be called kings.

He could not reach someone born in a human body and called a god, but he stood shoulder to shoulder with the Three Stars. If he took the other side, they would have to be prepared for tremendous losses.

Even with So Gyo, himself, the Emperor, and several other Supreme Peak masters on their side.

“Their forces are already formidable enough. And that’s only what we’ve managed to learn so far. If the Fire King joins them after Jin Taekyung…”

“The Fire King? That wouldn’t be bad.”

For a moment, Baek Yeon doubted his ears.

Then, seeing So Gyo continue with a faint smile on her lips, he realized she’d meant what she said.

“No, actually, that might be better.”

“……!”

Leaving Baek Yeon frozen like a statue, unable to understand her at all, So Gyo turned away with a quiet laugh.

The words she hadn’t told him drifted through her mind.

*Wait. You’ll know soon enough.*

Baek Yeon thought he knew everything, but he was wrong.

The story So Gyo had kept from him was something only she and the Emperor knew. Secrets were better off unknown.

At least until the banquet that both allies and enemies were eagerly awaiting.

“Only three days left until then.”

So Gyo looked up at the sky, now dark with night, and murmured. As if sensing the calm before the storm that had already begun, cold raindrops started to fall.

* * *

Shaaah.

The heavy rain hammered everything around us.

It was so loud that it swallowed even the shouts of the palace attendants running here and there in bamboo rain hats and rain cloaks.

Even after spending a good while in Murim, this was the fiercest downpour I’d ever experienced. The unexpected rain and thunder were more than enough to block the watchers’ view.

“You’re really going?”

Hyuk Mujin asked, his face tense. I answered,

“I have to.”

“What if they catch you…”

“They won’t. Not in this situation. You were there and heard it too, so you know.”

“I do. I know it’s urgent. But even so…”

“It’ll be all right. If it’s Young Master Jin.”

Hong Jin suddenly spoke, his voice subdued.

“Even if they catch him, there’s a good chance they’ll pretend they didn’t see him.”

“Huh? What do you mean?”

“If what Young Master Jin told us is true, what they want is to wipe us all out at once. They intend to uproot us in one fell swoop. We have no choice.”

I nodded silently.

Would So Gyo and Baek Yeon have let me go without a thought?

Even knowing full well that this story would reach their enemies?

*No way.*

This was a warning, and a declaration. A declaration that we weren’t to avoid this all-or-nothing battle. And we couldn’t refuse it.

*With Prince Shangshan in their grasp, there’s no way to avoid it, no matter what we do.*

The fact that our enemies had engineered the situation meant they were confident of victory. But no matter how thorough their preparations or how many traps they’d set, we couldn’t back down.

*We have to fight. Right now, before we worry about winning or losing, we have to make a decision.*

The stage was set. So were the actors.

The enemy had arranged the stage, and they intended to star in it. But sometimes, against everyone’s expectations, the supporting actor outshines the lead.

That was my job.

To change the lead of the coming performance—and the ending of this story.

And fortunately, there was one important surprise in the imperial palace that the enemy didn’t know about.

*Old Master.*

I stared out the window at the sheets of rain.

The downpour obscured my view, and the sky was already pitch-black. Below the pavilion, Embroidered Uniform Guard soldiers stood watch in shifts.

There were about twenty of them, all Peak masters.

But even if they were Supreme Peak masters, they couldn’t predict a sudden lightning strike.

FLASH! KABOOM!

*Now.*

At the instant white light flashed and a thunderous boom rang out, I pushed off the railing and sprang into the air.

Whoosh!

The Ghost Illusory Slaughter Step, a signature martial art created by the greatest assassin of all time, unfolded from my feet.

I hadn’t formally learned it; I’d only managed to work a little of it in. But that was enough to slip past the watchers during the brief confusion.

Tap. Swish!

I landed on the roof of a pavilion I didn’t know by name, said to house the palace attendants, and shot forward—quietly, but swiftly.

With the layout of the imperial palace already etched deep in my mind, I didn’t hesitate for even a moment.

*From here, along the east-west axis.*

The grounds were vast—vast enough to be boundless—with pavilions lined up here and there between them.

The black clothes I wore blended into the darkness, and the guards posted throughout the grounds failed to catch my movements.

“Damn, it’s really coming down.”

“The grand banquet’s right around the corner, and now the weather’s like this…”

The imperial guards grumbled as they gazed up at the sky from beneath the eaves. They had no idea that an uninvited guest had just passed within two steps behind them and entered the Outer Palace.

But not everything went smoothly.

“What are you doing here?”

“Y-Yes, sir!”

“If I remember the regulations correctly, your assigned post isn’t beneath the eaves.”

The only ones startled by that rock-hard voice weren’t the soldiers. I was just about to move on when I saw the familiar face that had suddenly appeared and swallowed a groan.

*Fuck, what’s that bastard doing here?*

Jeong Hogun.

A high-ranking Thousand Captain in the Embroidered Uniform Guard, he was walking toward the soldiers.

And at the same time, he was heading toward me, concealed not far away in the darkness.
```

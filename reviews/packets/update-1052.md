<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1052.txt",
      "sha256": "19c1d5b4a924e001735d1413b3ff358a9468c80486c80eaa107e1e26f5e6d913",
      "bytes": 12743
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "e572d7bf7eabb7611bae9767aa04fa2170dfa29c5b3e9487c7872fb9f28015c9",
      "bytes": 1663
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "91edff1ea0e7f2d1bdf20f77998a86f250b89f1bc3f043cd106289bea1e118b4",
      "bytes": 240895
    },
    {
      "path": "characters/Blood-Sword Demon Lord.md",
      "sha256": "7a29e07daae86314b21b5ec9f259d6170aaddeeb348bdf2d6d38ba16963967bf",
      "bytes": 920
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "a3611d4f7470da0f7bb97957cecaca2649fcb026e32bd0b39fef941b7de4c3ed",
      "bytes": 760
    },
    {
      "path": "characters/Grand Mage.md",
      "sha256": "05a2c022bb1e3ededb108fef5426b39f005eb377c46683ecba893138a415fcf6",
      "bytes": 753
    },
    {
      "path": "characters/Hwangbo Eom.md",
      "sha256": "16477a5e4b8037e25a18a73466dc710c8e9b0681945db97e9b0b11cc033a9236",
      "bytes": 674
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "f68254c3029d9d2b070d48248399e03ab8166bcf20db99127a83ae04c31143a1",
      "bytes": 1502
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "48da46732730e15265a5c228eba3bd025cd98925a2163b0756cc24f4ca23f9f5",
      "bytes": 1827
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "72bfdd6fda70069cf0dca4000e5afb06865bff5de047ea51d3bfaf45fca9eb69",
      "bytes": 623
    },
    {
      "path": "characters/Sama Pyo.md",
      "sha256": "a1c7c2f1eb793b90491cb841af7b7361740ef9e457792d85f53a9c7b139e8097",
      "bytes": 1056
    },
    {
      "path": "characters/Sima Gong.md",
      "sha256": "269192636e0d2caf53b88f1867e3fbd78d6df88cebb904af7ae20f4d25798bbe",
      "bytes": 800
    },
    {
      "path": "characters/So Gyo.md",
      "sha256": "08b6ef3d86567219f1f6891838b28d7a7c23dc6fe120a17ceca02fb615efc5ee",
      "bytes": 768
    },
    {
      "path": "characters/Song Il.md",
      "sha256": "6077f38f0414b7e4b6771b8b9c3305397491582b97ef82f5aacbc35b8f120b06",
      "bytes": 774
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "82da979917673ecf9336c9a75297fb511fdb57983eb6bca6932c7d82fe10c0c4",
      "bytes": 686
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "e476e49cdcddf6de4980fb9437ae78bed54ffc02a595fe7c61e28608999f8e34",
      "bytes": 281989
    }
  ],
  "estimated_tokens": 13457
}
-->

# Durable State Update — Chapter 1052

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
1 and safe_through 1052. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1052. Profile updates may replace only one
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
  "chapter": 1052,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1052,
    "continuity_sources": [1052],
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
    "The Grand Mage says the Lord of Heaven ordered her faction to watch Jin Taekyung and wants him to survive and grow stronger; the reason is unknown.",
    "The Grand Mage identifies Jin as the Chosen One, matching the title the Bow Saint used based on the Martial God’s letter.",
    "The Grand Mage says she lacks authority to kill Jin and acts to save him because her master has waited a long time for him.",
    "Jin severed his heart meridians while bound by the Grand Mage’s plant magic, then survived after her healing power took effect; his injuries and listed status effects were removed.",
    "Jin broke free of the vines and attacked the Grand Mage; she evaded with Blink, and Jin closed in on her. The fight continues."
  ],
  "continuity_sources": [
    1050,
    1051
  ],
  "open_questions": [
    "What are the identity and purpose of the Lord of Heaven?",
    "Why does the Lord of Heaven want Jin to survive and grow stronger?",
    "How did the Martial God foresee the Chosen One, and what connects his letter to the Lord of Heaven’s plans?",
    "Who are the white-robed mages, and what is their purpose?",
    "What is the Grand Mage’s master’s identity and connection to the Chosen One?"
  ],
  "safe_through": 1051,
  "temporary_decisions": [
    "Render 대마도사 and 대술사 as Grand Mage.",
    "Use Fire Ball, Stone Wall, and Magic Arrow for the named spells.",
    "Render 헬 파이어 as Hell Fire; use hellfire for descriptive 겁화.",
    "Render 쇄월검진 as Moon-Shattering Sword Formation.",
    "Render the achievement 배 째 as “Go Ahead, Gut Me!”"
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 송일     | **Song Il**        |
| 사마공    | **Sima Gong**      |
| 궁성     | **Bow Saint**                 | —              |
| 암천     | **Dark Heaven**                  |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 살기     | **killing intent**                               |                                                       |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 사형     | **Senior Brother**                           |
| 사제     | **Junior Brother**                           |
| 도사      | **Daoist**                                                      |
| 혈검마군 | **Blood-Sword Demon Lord** | Antagonist commanding the army advancing on the Great Snow Mountain. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 대마도사 | **Grand Mage** | Title used for Magic Johnson. |
| 황보엄 | **Hwangbo Eom** | Personal name of the Taeeul Merciless Sword. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 사마표 | **Sama Pyo** | Young Sect Leader of the Black Dragon Demon Gate. |
| 소교 | **So Gyo** | The palace attendant leading the group assigned to serve Prince Shangshan. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 전세 | **jeonse lease** | Korean lump-sum deposit lease used in the family's redevelopment-era housing history. |
| 야왕 | **Night King** | Rumored epithet for Jin Taekyung in Taiyuan's red-light district. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 노호검객 | **Roaring Fury Swordsman** | Fiery-tempered elder and top-five master of the Zhongnan Sect. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 마공 | **demonic martial arts** | Martial arts that appear to defy common principles. |
| 천주 | **Lord of Heaven** | Authority invoked by the masked attackers. |
| 절체절명 | **Life-or-Death Crisis** | Sudden System Quest forcibly accepted during the confrontation at Mount Song. |
| 노야 | **Old Master** | Taekyung's private address for Jeok Cheongang. |
| 태을무정검 | **Taeeul Merciless Sword** | Title of the Zhongnan Sect’s Second Martial Uncle, who is in Xi’an. |
| 황보 | **Hwangbo** | Surname form used when addressing Hwangbo Eom. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 신력 | **divine strength** | Superhuman strength attributed to Taekyung. |
| 성도 | **Chengdu** | Sichuan destination of Taekyung's party. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 마두 | **fiend** | Demonic martial masters from the Great Faction War era. |
| 시리 | **City** | Second word in one of the necromantic chants. |
| 텔레포트 | **Teleport** | Taekyung's label for the Blood Lord's unexplained disappearance. |
| 흑야왕 | **Black Night King** | Epithet of Sima Gong, Sama Pyo's father and the Sect Leader who built the modern Black Dragon Demon Gate. |
| 사냥개 | **hunting dog** | Jin's demeaning metaphor for Ares personnel who obey Go Jun. |
| 고든 | **Gordon** | Pentagon employee tasked with repairing smashed warning lights. |
| 검마 | **Sword Demon** | A Demonic Cult swordsman whose final technique is compared with One Annihilation. |
| 대설산 | **Great Snow Mountain** | Mountain where Baeksang's wartime account reaches its next episode. |
| 가기 | **singing courtesan** | The favored entertainer identity Honglan used in Hubei. |
| 대술사 | **Grand Mage** | Title of the veiled woman leading the white-robed mages. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 송일 | 진태경 | hostile Zhongnan Elder to accused outsider | you / Jin Taekyung | hostile and threatening | Song Il questions Taekyung's identity and later threatens him over Gong Ilhyuk's injury. |
| 송일 | 적천강 | former rescued junior to former rescuer | Great Hero Jeok | formal, fearful, and defensive | Uses 적 대협 while insisting that Jeok has no business interfering in the dispute. |
| 적천강 | 송일 | former rescuer to former rescued junior | Zhongnan brat; you; insolent bastard | blunt, mocking, and humiliating | Jeok recalls Song's youthful arrogance and addresses him with contempt while publicly disciplining him. |
| 진태경 | 황보엄 | junior_martial_artist_to_Zhongnan_senior | Great Hero Hwangbo | casual-polite and teasing | Taekyung uses 황보 대협 after deliberately pretending not to recognize Hwangbo. |
| 황보엄 | 진태경 | Zhongnan_senior_to_younger_martial_artist | insolent brat | blunt, amused, and probing | Hwangbo describes Taekyung as a 건방진 아해 and later treats him as a youngster. |
| 황보엄 | 적천강 | rival_martial_masters | Fire King Jeok Cheongang | cold and taunting | Reveals that he knows Jeok's illness and threatens to settle his bad blood with the Fire Gate Clan. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 사마표 | 태산 | Young Sect Leader to subordinate | Taishan | informal and patronizing | Sama Pyo calls Taishan by name while ordering him to leave. |
| 태산 | 사마표 | subordinate to Young Sect Leader | Lord | crude and deferential | Taishan uses 주군 while obeying Sama Pyo. |
| 태산 | 진태경 | subordinate_to_respected_outsider | Jin Taekyung | clipped and familiar | Taishan says he likes Jin Taekyung but will fight him without hesitation if Sama Pyo commands it. |
| 사마표 | 적천강 | Young Sect Leader to legendary elder | Great Hero Jeok | formal-deferential | Sama Pyo formally pays his respects to Jeok Cheongang as the Fire King. |
| 태산 | 적천강 | subordinate of a Young Sect Leader to legendary elder | Fire King | clipped, childlike, and deferential | Taishan gives his awkward greeting and expresses admiration for Jeok's strength. |
| 적천강 | 사마표 | legendary elder to unorthodox Young Sect Leader | you / young brat | blunt, suspicious, and contemptuous | Jeok addresses Sama Pyo with 네놈 and 어린놈 while probing his lineage and motives. |
| 적천강 | 태산 | legendary elder to giant subordinate | you / strange fellow | blunt, startled, and grudgingly tolerant | Jeok addresses Taishan as 네놈 while reacting to his greeting and appetite. |
| 사마표 | 진태경 | prospective recruit to pavilion master | you | polite, controlled, and candid | Sama Pyo uses 자네 while asking about Taekyung's attitude and admitting his intention to use him. |
| 진태경 | 사마표 | pavilion master to prospective recruit | you / that guy | blunt, informal, and distrustful | Taekyung speaks to and about Sama Pyo with casual forms such as 녀석 and 저놈. |
| 진태경 | 태산 | pavilion_master_to_pavilion_member | Taishan | forceful and commanding | Taekyung orders Taishan to stop eating the bear. |
| 소교 | 진태경 | palace attendant addressing a martial artist and guest under escort | Young Master Jin | formal and respectful, but firm | Addresses him as 진 공자 while escorting him and warning him not to investigate. |
| 진태경 | 소교 | palace attendant and martial artist under imperial scrutiny | you | formal-polite, controlled and challenging | Taekyung addresses So Gyo as 당신 while questioning her presence and demanding an explanation. |
| 신의 | 태산 | senior physician to younger ally | Young Hero Taishan | urgent and respectful | The Divine Physician uses this address while pleading with Taishan to keep moving. |
| 궁성 | 진태경 | elder who spent decades searching for the chosen one | you | casual and teasing | Uses 너/널 while testing and praising Taekyung. |
| 진태경 | 궁성 | chosen one addressing the elder who sought him | you | polite, shifting to familiar-casual under stress | Begins with formal-polite phrasing, then speaks more casually as the conversation intensifies. |
| 적천강 | 궁성 | old acquaintance and fellow martial master | you; nasty old hag | blunt and familiar | Uses a contemptuous insult while expressing concern for his Disciple. |
| 궁성 | 적천강 | old acquaintance and fellow martial master | you | familiar and lightly teasing | Speaks with dry familiarity about his unchanged, impulsive nature. |
| 노호검객 | 적천강 | senior_martial_artist_to_legendary_elder | Senior Jeok | deferential and cautious | Addresses Jeok as 노 선배 while explaining his actions. |
| 사마공 | 적천강 | unorthodox sect leader to senior martial master | Senior | formal and deferential | Greets Jeok Cheongang as 노선배. |
| 적천강 | 사마공 | senior martial master to longtime martial acquaintance | you | blunt and familiar | Uses direct, contemptuous language while teasing Sima Gong. |
| 진태경 | 사마공 | allied young martial artist to unorthodox sect leader | Great Hero Sima | polite and deferential | Addresses him as 사마 대협. |
| 사마공 | 진태경 | unorthodox sect leader to celebrated young martial artist | you | polite and familiar | Uses 자네 while speaking to Taekyung. |
| 사마공 | 사마표 | father to son | Pyo | intimate and familiar | Sima Gong calls him 표야 and 내 아들아. |
| 혈검마군 | 적천강 | former opposing martial masters | Senior Jeok | respectful and familiar | Addresses Jeok as 선배 while teasing him. |
| 적천강 | 혈검마군 | former opposing martial masters | you; you bastard | blunt and hostile | Uses 너 and 네놈 while confronting him. |
| 혈검마군 | 진태경 | enemy addressing a younger martial artist | you | familiar and measured | Uses 자네 while praising and assessing Taekyung. |
| 진태경 | 혈검마군 | young martial artist confronting an enemy | you | casual and challenging | Questions when the Blood-Sword Demon Lord and the Lord of Heaven appeared. |
| 혈검마군 | 천주 | servant_to_master | Lord of Heaven | deferential | In his inner monologue, he addresses his absent master as 당신 and refers to himself as 속하. |
| 사마표 | 사마공 | son to father | you; Father | familiar and confrontational | Sama Pyo challenges his father during their battlefield confrontation. |
| 대마도사 | 진태경 | adversary_to_adversary | you | polite, teasing | She uses polite phrasing while taunting him and warning him not to overexert himself. |
| 진태경 | 대마도사 | adversary_to_adversary | you bitch | insulting-casual | He curses at her while refusing to give up. |
| 송일 | 황보엄 | Senior Brother to Junior Brother | Junior Brother | familiar and heated | Song Il calls Hwangbo Eom 사제. |
| 황보엄 | 송일 | Junior Brother to Senior Brother | Senior Brother | familiar and dryly teasing | Hwangbo Eom calls Song Il 대사형. |
| 대마도사 | 궁성 | Adversaries | Bow Saint | Not established | She identifies him by title when recognizing the archer who struck the Hell Fire sphere. |
| 혈검마군 | 사마공 | former bargaining allies turned enemies | you; you traitor | blunt and hostile | Uses direct, contemptuous forms while accusing Sima Gong of betraying him. |
| 사마공 | 혈검마군 | former bargaining allies turned enemies | you; you Demonic Cult bastard | calm and contemptuous | Uses 당신 before ending with the insult 마교 잡놈아. |
| 대술사 | 혈검마군 | subordinate_to_commander | Demon Lord | respectful and formal | Addresses him as 마군 while acknowledging his injuries. |
| 혈검마군 | 대술사 | commander_to_subordinate | Grand Mage | blunt and commanding | Orders her to heal him immediately. |

## Listed compact profiles

### Blood-Sword Demon Lord.md

# Blood-Sword Demon Lord (혈검마군)

- **Safe through:** Chapter 1050
- **Aliases:** None
- **Role:** The Blood-Sword Demon Lord is a formidable martial master who commands the force advancing on the Great Snow Mountain and now serves the Lord of Heaven.
- **Personality:** Devoted to his master and proud of his abilities, he is deeply wounded by perceived distrust and resolves to prove his worth.
- **Voice:** Casually familiar and self-amused, addressing Jeok Cheongang respectfully as Senior while trading blunt insults; his easy laughter can turn to a low, cold intensity.
- **Relationships:** He serves the Lord of Heaven with deep devotion, but the Grand Mage says the Lord ordered his disposal; he has been ordered not to kill Jin Taekyung, admires Jeok Cheongang, and once shared the Demonic Cult with the fiends who became Black Ghosts.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1051
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Grand Mage.md

# Grand Mage (대마도사)

- **Safe through:** Chapter 1051
- **Aliases:** None
- **Role:** The Grand Mage leads the white-robed mages and is a formidable mage who has reached the edge of truth.
- **Personality:** Fanatically devoted to the Lord of Heaven, she stays composed while coercing her enemies and treats their resistance with contempt.
- **Voice:** Calm and formally polite while taunting, but drops the courtesy for blunt, scornful challenges when addressing an enemy.
- **Relationships:** She commands the white-robed mages, serves a master who has long awaited Jin Taekyung, and acts to keep Jin alive despite being unable to kill him without her master’s permission.

### Hwangbo Eom.md

# Hwangbo Eom (황보엄)

- **Safe through:** Chapter 1044
- **Aliases:** Taeeul Merciless Sword
- **Role:** Supreme Peak master of the Zhongnan Sect and its Second Martial Uncle, known as the Taeeul Merciless Sword.
- **Personality:** Ruthless, severe, proud, and deeply invested in restoring Zhongnan's standing.
- **Voice:** Calmly courteous when offering tea, then cold, commanding, and cutting when reprimanding others.
- **Relationships:** Song Il and Hwangbo Eom are Gong Iljung’s two Senior Brothers; the three served the same Master for over fifty years, and Hyuk Sopyung is Hwangbo’s junior.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 1051
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; he distrusts process-first excuses when outcomes fail and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, and insists on protecting Taekyung while urging him not to risk his life; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy, and personally killed his former ally the Junzi Saber after that man joined the Demonic Cult.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1051
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan and the original owner of his current body, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master who has reached the realm of the Ten Kings as its eleventh member and can detect and eavesdrop on nearby Sound Transmissions subject to the participants’ relative levels, and a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure, willing to risk himself for others, and fiercely defiant when others try to dictate his choices or survival.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; Hyuk Mujin trusts Taekyung to fight beside him and feels no fear when Taekyung is with him; Taekyung trusts Sama Pyo and values him beyond his unorthodox affiliation; Peng Cheolhu regarded Taekyung as a worthy successor, and the Bow Saint relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1051
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Sama Pyo.md

# Sama Pyo (사마표)

- **Safe through:** Chapter 1037
- **Aliases:** Black Dragon Saber
- **Role:** Young Sect Leader and heir of the Black Dragon Demon Gate, a Morning Star reputed to be no less than the Ten Dragons and Phoenixes.
- **Personality:** Outwardly courteous and calculating, he protects those beside him even at personal risk and has begun rejecting his father's survival-at-any-cost worldview.
- **Voice:** Polite and ingratiating in public, with sardonic humor and controlled evasiveness.
- **Relationships:** Sama Pyo commands the absolutely loyal Taishan and is Sima Gong's son and heir, but now openly challenges his father and chooses a different path. He joined the Fire Dragon Pavilion intending to use Jin Taekyung, who rejects defining him by his unorthodox affiliation and whom Sama Pyo admires; Sima Gong ordered him to spy on Taekyung's group. He was Ju Hwaran's former fiancé in a political engagement and is openly hostile toward fellow member Song Ilseom.

### Sima Gong.md

# Sima Gong (사마공)

- **Safe through:** Chapter 1048
- **Aliases:** Black Night King
- **Role:** Sima Gong is the Sect Leader who built the Black Dragon Demon Gate into a major unorthodox power and the father of its Young Sect Leader, Sama Pyo.
- **Personality:** Sly and calculating yet capable of risking himself for a moment of conscience, he values his heir’s future and repaying a debt to Jeok Cheongang.
- **Voice:** Polished and persuasive, with smooth rhetorical turns and a composed, gently teasing manner.
- **Relationships:** Sama Pyo is his youngest son among seven older brothers and nine older sisters; he aided Jeok Cheongang despite their history, and hopes his heir will carry on the Black Dragon Demon Gate.

### So Gyo.md

# So Gyo (소교)

- **Safe through:** Chapter 1048
- **Aliases:** None
- **Role:** So Gyo is the Bow Saint, a Supreme Peak master and palace attendant assigned to Prince Shangshan, whose two curved swords can join into their original bow form.
- **Personality:** Calm, calculating, and self-possessed; she conceals her strength and identity and can be openly taunting.
- **Voice:** Measured and composed, shifting from deferential formality to casual, pointed taunts and threats.
- **Relationships:** So Gyo recognizes Jin Taekyung as the chosen one spoken of by the Martial God; she says only she and the Emperor know a secret she withheld from Baek Yeon, while her true allegiance remains unknown.

### Song Il.md

# Song Il (송일)

- **Safe through:** Chapter 1046
- **Aliases:** Roaring Fury Swordsman
- **Role:** Elder of the Zhongnan Sect, known as the Roaring Fury Swordsman and one of Sect Leader Gong Iljung’s two Senior Brothers.
- **Personality:** Arrogant and domineering, but capable of remorse over choices that harmed his sect and those he failed to protect.
- **Voice:** Gruff, cutting, condescending, and threatening, with formal authority used to pressure those beneath him.
- **Relationships:** Gong Iljung is his junior Sect Leader and martial younger brother; Gong Ilhyuk is a junior Disciple of his sect; he recognizes Baek Museong and Cheongpung through their Huashan and Sword Saint connections.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 1051
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo; becomes explosively violent when his meat is threatened.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord, trusts Jin Taekyung as Pavilion Master, and has grown attached to the Fire Dragon Pavilion members.

## Korean source

```text
＃1052화



“또 보네?”

나직한 음성과 함께 어느덧 코앞까지 들이닥친 진태경의 모습에, 대술사는 전신의 피가 차갑게 식는 것을 느꼈다.

‘도대체 어떻게?’

단순히 빠르다는 표현으로는 설명할 수 없는, 예상을 아득하게 벗어난 속도.

그리고 이미 알고 있었다는 듯이, 그녀의 몸뚱어리를 향해 내리그어지는 은빛 창날.

쐐애액!

바람이 갈라진다. 아니, 부서진다.

창날을 휘감은 강기를 따라 공간이 일그러지는 그 무시무시한 광경 앞에, 대술사는 그 어느 때보다 거대한 공포를 느끼며 마음속으로 부르짖었다.

‘강대한 보호의 힘이여!’

우우웅.

느려진 세상 속, 심장을 중심으로 뭉쳐 있던 기운이 들끓었다.

그와 동시에 겹겹이 솟아오른 반투명한 보호막이 시전자의 육신을 감싸며 창날을 막아섰다.

콰앙! 콰드드득!

굉음과 함께 지진이라도 난 것처럼 뒤흔들리는 지면.

그러나 지금 이 순간, 대술사의 모든 감각은 오직 눈앞의 시야에만 집중되어 있었다.

수십여 겹이나 중첩된 보호막 중 대부분을 파괴한 후에야 아슬아슬하게 멈춰선 창날에.

‘막았다.’

등골을 타고 솟구치는 전율 속, 대술사는 그제야 참았던 숨을 토해냈다.

그리고 그 안도감을 온전히 느끼기도 전, 회심의 공격이 실패로 돌아갔음에도 흐릿하게 웃고 있는 진태경의 모습을 보며 불현듯 한 가지 사실을 깨달았다.

자신이 무언가를 잊고 있었음을.

그것도 아주 중요하면서도, 위험한 존재들을.

하지만 모두에게 그렇듯이, 전장에서의 깨달음은 늘 한발 늦게 찾아오는 법이었다.

쉬이이잉!

공간을 가로지르며 날아든 거대한 섬광.

시야를 아득하게 물들이는 그 휘황한 빛무리 너머로 보이는 두 사람의 인영(人影)에, 대술사는 소리없는 비명을 터트렸다.

‘궁성(弓星)……!’

콰아아앙!

거대한 폭발음에 이어 크게 부풀어 오른 섬광이, 언덕 전체를 집어삼켰다.



* * *



마지막 순간, 그 모든 일은 거의 동시에 벌어졌다.

엄청난 충돌의 여파를 예측한 내가 거리를 벌린 것.

저 멀리, 활시위를 떠나 맹렬하게 들이닥친 강기의 화살이 마침내 보호막과 맞닿은 것.

그리고.

화아악!

모두의 시야를 가리며 부풀어 오르는 아득한 섬광이, 힘없이 부서지는 보호막 뒤에 가려져 있던 대술사의 신형을 집어삼킨 것.

구구구구궁!

지축이 뒤흔들린다. 일순간 터져 나온 빛이 어둠을 찢고 모든 것을 집어삼킨다.

그저 엄청나다고밖에 할 수 없는 힘의 파동.

‘흡……!’

숨을 삼키며 한껏 몸을 웅크렸다. 마치 칼날처럼 휘몰아치는 광풍이 전신을 스치고 허공을 난도질했다.

그렇게 찰나에 불과하지만 마치 영원처럼 느껴졌던 시간이 끝났을 때.

나는 비로소 들을 수 있었다.

먹먹해진 귓가로 흘러 들어오는 누군가의 익숙한 음성을.

“괜찮으냐?”

참았던 숨을 토해 내며, 나는 고개를 들었다.

서서히 사그라지는 섬광 너머, 갈기갈기 찢어진 새하얀 의복과 사방에 흩뿌려진 핏물. 그리고 몸뚱어리에서 떨어져 나온 누군가의 팔다리가 보였다.

여인의 것이 분명한, 하얗고 가느다란 그것들이.

“끝났다. 전부.”

“……아.”

대마도사의 죽음.

비로소 그 사실을 인지한 순간, 나도 모르게 전신의 맥이 탁 풀렸다.

이미 한참 전에 한계에 다다라 있던 정신력, 그로 인한 숨길 수 없는 피로가 밀려와 눈앞을 흐릿하게 만들었다.

덥석.

휘청이는 몸뚱어리를 붙잡는 억센 손아귀.

힘있게 나를 일으켜 세우는 적천강의 모습에, 문득 실소가 흘러나왔다.

“죄송합니다, 노야.”

“뭐가 말이냐?”

“반 각. 한참 전에 지났잖아요.”

적천강이 나를 따라 웃었다.

“아직 백 년은 이르지. 저 염병할 놈이 여기까지 도망쳐 온 것을 보면 모르겠느냐?”

말과는 달리 피투성이가 된 몰골.

그러나 적천강은 천연덕스럽게 대꾸하며 한 곳을 가리켰고, 그의 손가락 끝에는 바퀴벌레처럼 끈질기게 살아남은 늙은 대마두가 있었다.

물론 당연하게도, 이 엄청난 후폭풍 속에서 혈검마군이 살아남을 수 있었던 이유는 따로 있었지만.

“잠시 자리를 비운 사이에 참 멀리도 떠났더구나. 터무니없이 무모하게도.”

소교, 아니 궁성이 평소와 다름없는 침착한 눈빛으로 나를 응시하며 입을 열었다.

쉴 틈 없이 천하의 절반을 가로질렀음이 분명한데도, 그녀의 모습에서는 여전히 칼날 같은 기세가 느껴졌다.

그리고 막중한 피로를 느끼고 있을 궁성이 이와 같은 태도를 유지하고 있는 가장 큰 이유를, 나는 누구보다 잘 알고 있었다.

그녀가 굳이 혈검마군을 보호한 이유 역시도.

“하지만 남은 이야기는 뒤로 미루어야겠지. 아직 남아 있는 문제가 있으니.”

궁성의 말은 틀림없는 사실이었다.

대마도사가 죽었지만, 지금 이 순간에도 언덕 아래의 혈전은 계속되고 있었으니.

그러나 궁성이 말하는 문제는, 비단 그뿐만이 아니었다.

“결국, 이렇게 되었나.”

서늘한 살기(殺氣)가 묻어 나오는 궁성의 한 마디에, 그녀의 발치에 쓰러져 거친 숨을 내뱉고 있던 혈검마군이 힘겹게 입을 열었다.

“좋다. 무엇이든…… 무엇이든 말해 주마.”

무엇이든, 이라.

나는 마음속으로 조용히 그 말을 곱씹었다. 동시에 비틀거리는 발걸음으로 그를 향해 다가가며 백염을 들어 올렸다.

스릉.

대답 대신 겨누어진 창날.

그 시리도록 빛나는 섬광 앞에서, 애써 담담하던 혈검마군의 음성이 한층 커졌다.

“배신자, 너희 중에 배신자가 있었다!”

무시무시한 기파를 뿜어내던 대마두의 모습은 이제 어디에서도 찾아볼 수 없다.

지금 내 앞에 쓰러져 있는 혈검마군은, 패악으로 물든 일평생의 끝자락에서 모든 것을 잃고 몰락해 버린 걸인(乞人)이나 다름없다.

주인에게 버려지고, 아군에게 배신당하고, 이제는 자신이 죽이려 했던 적에게까지 정보를 팔아 목숨을 구걸하려는.

“두려워?”

“……뭐?”

“너 같은 것들도, 두려움을 느끼냐고.”

부릅떠진 놈의 눈동자를 내려다보며, 나는 나직한 목소리로 말을 이었다.

“거래는 없다.”

혈검마군은 이미 버림받은 개다.

어쩌면 아주 오래전부터, 놈의 운명은 토사구팽으로 정해졌을 것이다.

그 이유는 자세히 알 수 없으나, 그것이야말로 천주가 의도했던 결과였고 언젠가 가차 없이 내쳐 버릴 사냥개에게 정성을 쏟을 주인은 없다.

그렇기에 나 역시 그 사냥개의 말을 귀담아들을 필요도, 이유도 없었다.

설령 그것이, 오늘 이 자리에서 윤곽을 드러낸 배신자들에 관한 정보라면 더더욱.

“흑야왕(黑夜王) 사마공. 노호검객(怒號劍客) 송일. 그리고 태을무정검(太乙無情劍) 황보엄.”

“……!”

돌아오는 대답은 없었으나, 세차게 흔들리는 혈검마군의 눈동자가 대답을 대신한다.

단지 확신에 가까웠던 짐작을, 비로소 확신이라는 두 글자로 완성시킨다.

“이미…… 알고 있었다고?”

간신히 쥐어 짜낸 듯한 음성.

나는 넋 나간 얼굴을 하고 있는 혈검마군을 향해 고개를 끄덕였다.

“어느 정도는.”

“하, 하지만. 그렇다면 어째서?”

“이유를 묻는다면, 글쎄.”

나는 참을 수 없는 피로를 느끼며 창날을 들어 올렸다.

동시에 문득 떠올렸다.

배신자들의 존재를 짐작하고 있었음에도 여기까지 올 수 있었던 이유를.

이 불합리한 상황 속에서도 목숨을 건 혈투를 치르고, 끝까지 포기하지 않았던 이유를.

그리고 그건 아마도.

“조금 더. 믿고 싶었나 보지.”

“……!”

“그렇게 믿지 않고서는 승리할 수 없으니까. 그래서, 그래서 이렇게 병신처럼 여기까지 왔던 거겠지.”

그래.

그것이 승리할 수 있는 이유였다.

암천과 우리의 차이.

천주와 나의 차이.

그리고 나는 이미 그 실낱같은 믿음과 기대에 대한 결과를 두 눈으로 똑똑히 확인했다.

정확히는, 한 사람으로부터 비롯된 믿음을.

‘사마표.’

과묵하고, 어두컴컴하지만 단 한 번도 기대를 배신하지 않았던 녀석.

그 어떤 절체절명의 순간에서도 먼저 뒷걸음질 치지 않고, 늘 함께 등을 맞대고 싸웠으며, 서로의 피를 뒤집어쓴 채 웃었던 전우.

아니, 친구.

‘녀석이 아니었다면, 이런 작은 믿음조차 품지 못했겠지.’

그리 오래되지 않은 과거에, 적천강이 내게 물었었다.

만약 사마표와 태산이 배신한 것이 사실로 밝혀진다면, 너는 어찌하겠느냐고.

나는 대답하지 않았다.

사마표와 함께 대설산의 산맥을 내려가던 그 순간에도 마음속으로 되뇌었지만, 도저히 대답할 수 없었다.

나는 녀석들을 죽이지 못할 테니까.

다만 믿었을 뿐이다. 누구보다 간절하게.

그리고 배신자들을 향해 믿음을 보낸 이는, 나뿐만이 아니었을 것이다.

‘사제는 두 사형을. 아들은 아버지를.’

결국 그들의 믿음은 보답받았다.

배신자들의 마음을 움직이고, 끝끝내 전세를 뒤바꾸었다.

나는 보았다.

태을무정검과 노호검객이 헬파이어를 향해 몸을 내던지는 광경을, 적천강을 대신하여 혈검마군과 맞서는 사마공의 모습을.

물론 그들이 지은 죄는 용서받지 못할 것이다.

적어도 그들을 용서할 권리는 내게 없다.

적천강도, 궁성도 마찬가지다.

하지만 적어도 마지막 순간 최소한의 도리(道理)를 지킨 배신자들의 모습을, 나는 기억할 것이다.

곧 주인의 기억 속에서 까맣게 잊혀질, 버림받은 사냥개와는 다르게.

“그래서 다른 거야. 너희랑 우리는.”

작지만 또렷한 목소리로 속삭이는 나를, 혈검마군은 실핏줄이 터져나간 붉은 눈동자로 바라보았다.

“진태경-!”

그리고 피를 토하는 듯한 외침이 터져 나온 그 순간.

푹.

두부를 가르듯 부드럽게 가슴을 파고든 창날이, 혈검마군의 뒷말을 집어삼켰다.

아니, 놈에게 남아 있던 실낱같은 생명력을.

띠링.

귓가를 울리는 맑은 종소리.

동시에 계곡물처럼 시원한 기운이 전신을 휩쓸고, 다시 한번 내 육신에 새로운 강인함을 불어넣었다.

은백색 창날에 꿰뚫려 처참한 죽음을 맞이한 누군가와는 달리.

그리고 그보다 한발 앞서, 몸뚱어리조차 제대로 건사하지 못할 만큼 처참한 죽음을 맞이한 누군가의 뜻대로.

‘여기에서 쓰러져서는 안 된다고? 지금보다 더 강해지라고?’

전신을 짓누르는 극심한 정신적 피로를 느끼며, 나는 문득 고개를 돌려 바라보았다.

강기의 화살이 휩쓸고 지나간 그 자리에 남아 있는 대마도사의 마지막 흔적을 향해, 이제는 그녀가 듣지 못할 한 마디를 마음속으로 뇌까렸다.

‘걱정하지 마. 반드시 그렇게 해 줄 테니까.’

천주가 무엇을 원하는지, 나는 모른다.

그러나 한 가지는 분명하다.

나는 나아가야 한다. 끊임없이 앞으로 나아가기 위해 더욱 강해져야 한다.

천주의 예상을 아득히 벗어날 만큼, 언젠가 놈이 이 선택을 후회하게 될 만큼.

‘무엇이 앞길을 가로막더라도, 부수고 허물어트리면 그만이다.’

지금껏 그렇게 살았고, 앞으로도 그렇게 살 것이다.

마음속 뇌까림과 함께, 나는 비틀거리는 신형을 돌려세웠다.

정확히는 돌려세우려 했다.

피 웅덩이 위에 잠겨 있는, 각각 하나씩 몸뚱어리에서 떨어져 나온 가냘픈 팔과 다리에 새겨진 예리한 단면(斷面)을 보기 전까지는.

아니.

“……!”

텔레포트(Teleport)의 흔적을 발견하기 전까지는.
```

## Final English reading copy

```markdown
# Chapter 1052

“Fancy seeing you again.”

At the sound of his low voice, Jin Taekyung was suddenly right in front of her. The Grand Mage felt the blood in her body turn cold.

*How?*

His speed couldn’t be explained by simply calling him fast. It was far beyond anything she’d expected.

And as if he’d known exactly where she’d be, the silver spearhead came slashing down toward her body.

*Whoosh!*

The air split. No—it shattered.

As space warped around the Force coiling around the spearhead, the Grand Mage felt greater fear than ever before and cried out in her heart.

*O mighty power of protection!*

*Vwoom.*

In the slowed world, the energy gathered around her heart began to boil.

At the same time, layers of translucent shields rose up, surrounding her body and blocking the spearhead.

*Boom! Crash!*

The ground shook as if an earthquake had struck.

But in that moment, all the Grand Mage’s senses were focused on what lay before her eyes.

The spearhead had smashed through most of the dozens of layered shields, but at last it stopped—just barely.

*I blocked it.*

A shiver ran up her spine. Only then did the Grand Mage let out the breath she’d been holding.

Before she could fully feel the relief, she saw Jin Taekyung smiling faintly despite his sure-kill attack having failed. And suddenly, she realized something.

She’d forgotten something.

Or rather, some very important—and very dangerous—people.

But as with everyone, the realization came a moment too late on the battlefield.

*Whooosh!*

A vast flash of light flew across the space between them.

Beyond the dazzling light that filled her vision, she saw two figures—and the Grand Mage let out a silent scream.

*The Bow Saint…!*

*Boom!*

The enormous blast was followed by a swelling flash of light that swallowed the entire hill.

* * *

In the final moment, everything happened almost at once.

I’d backed away, anticipating the shock of the tremendous collision.

Far away, the Force arrow had left the bowstring and come hurtling toward us. At last, it struck the shield.

And then—

*Fwoom!*

The distant flash of light swelled, blocking everyone’s view and swallowing the Grand Mage’s figure, which had been hidden behind the crumbling shield.

*Rumble…!*

The earth shook. Light burst forth in an instant, tearing through the darkness and devouring everything.

The force of the blast was beyond words.

*Hngh…!*

I sucked in a breath and curled up as tightly as I could. A gale whipped past me like a blade, slashing through the air.

When that instant—which felt like an eternity—finally ended, I could hear again.

A familiar voice reached my muffled ears.

“Are you all right?”

I let out the breath I’d been holding and raised my head.

Beyond the slowly fading flash of light, I saw a white robe ripped to shreds, blood scattered everywhere, and someone’s limbs torn from their body.

They were slender and white—the limbs clearly belonged to a woman.

“It’s over. All of it.”

“…Ah.”

The Grand Mage was dead.

The moment I finally understood that, I felt all the strength drain from my body.

My mental strength had been at its limit for a long time. Exhaustion washed over me, and my vision blurred.

*Grab.*

A strong hand caught my swaying body.

Jeok Cheongang pulled me firmly to my feet, and a laugh escaped me.

“Sorry, Old Master.”

“For what?”

“Seven and a half minutes. That ran out ages ago.”

Jeok Cheongang laughed along with me.

“Still a hundred years too soon. Can’t you tell, seeing that damned bastard run all the way over here?”

His words said one thing, but he was covered in blood.

Jeok Cheongang answered nonchalantly and pointed toward a spot where an old fiend had somehow survived, like a cockroach.

Of course, there was a reason the Blood-Sword Demon Lord had survived the tremendous blast.

“You went a long way while I was gone. Recklessly far, too.”

So Gyo—or rather, the Bow Saint—looked at me with her usual calm gaze and spoke.

She must have crossed half the land without a moment’s rest, yet her presence still felt as sharp as a blade.

I knew better than anyone why the Bow Saint, despite the crushing fatigue she must have felt, was keeping up this front.

And why she’d gone out of her way to protect the Blood-Sword Demon Lord.

“But the rest will have to wait. There’s still a problem to deal with.”

The Bow Saint was right. The battle below the hill continued even now, despite the Grand Mage’s death.

But that wasn’t the only problem she meant.

“So this is how it ended.”

Her words were edged with cold killing intent. The Blood-Sword Demon Lord lay at her feet, breathing hard. He struggled to speak.

“Fine. Anything… I’ll tell you anything.”

*Anything,* huh?

I quietly rolled the word around in my mind. At the same time, I staggered toward him and raised White Flame.

*Shing.*

I pointed the spearhead at him instead of answering.

Faced with that icy gleam, the Blood-Sword Demon Lord’s voice grew louder, though he’d been trying to sound calm.

“There was a traitor among you!”

The fiend who’d once radiated such terrifying power was nowhere to be seen.

The Blood-Sword Demon Lord sprawled before me now was little more than a beggar, ruined at the end of a lifetime steeped in brutality.

Abandoned by his master. Betrayed by his allies. Now begging for his life by selling information to the very enemy he’d tried to kill.

“Are you afraid?”

“…What?”

“Can things like you feel fear?”

I looked down at his wide, bloodshot eyes and spoke softly.

“There’s no deal.”

The Blood-Sword Demon Lord was already a discarded dog.

Perhaps he’d been doomed to be cast aside after he’d outlived his usefulness long ago.

I didn’t know the exact reason, but this was the outcome the Lord of Heaven had intended. No master would lavish care on a hunting dog he planned to discard without mercy.

So I had no reason to listen to the dog’s words.

Especially if those words were about the traitors whose identities had finally come to light here today.

“Black Night King Sima Gong. The Roaring Fury Swordsman Song Il. And the Taeeul Merciless Sword, Hwangbo Eom.”

“……!”

The Blood-Sword Demon Lord didn’t answer, but his eyes shook violently in response.

That was enough to turn a suspicion close to certainty into certainty itself.

“You already… knew?”

His voice sounded like he’d barely managed to force it out.

I nodded at the Blood-Sword Demon Lord’s dazed face.

“To a certain extent.”

“B-But then why?”

“If you’re asking why… I don’t know.”

I raised my spearhead, feeling an unbearable exhaustion.

At the same time, something came to mind.

Why I’d been able to make it this far, even though I’d suspected there were traitors among them.

Why I’d fought for my life in this unfair situation and refused to give up until the end.

And maybe…

“I wanted to believe a little longer.”

“……!”

“You can’t win without believing in them. That’s why I came all this way like a fucking idiot.”

Yeah.

That was what made victory possible.

The difference between Dark Heaven and us.

The difference between the Lord of Heaven and me.

And I’d already seen the result of that slender thread of faith and hope with my own eyes.

Or, more precisely, the faith that began with one person.

*Sama Pyo.*

Quiet and gloomy, but someone who’d never once betrayed my trust.

A comrade who’d never stepped back first, no matter how dire the situation. We’d fought back to back, then laughed together, covered in each other’s blood.

No—he was my friend.

*If it weren’t for him, I wouldn’t have been able to place even this little faith in them.*

Not long ago, Jeok Cheongang had asked me what I’d do if it turned out Sama Pyo and Taishan had betrayed us.

I hadn’t answered.

Even as I walked down the Great Snow Mountain with Sama Pyo, I’d asked myself the same question. But I couldn’t bring myself to answer it.

I couldn’t kill them.

All I could do was believe. More desperately than anyone.

And I wasn’t the only one who’d put their faith in the traitors.

*A Junior Brother in his two Senior Brothers. A son in his father.*

In the end, their faith had been rewarded.

It had moved the traitors’ hearts and finally turned the tide of battle.

I’d seen it.

The Taeeul Merciless Sword and the Roaring Fury Swordsman throwing themselves at the Hell Fire. Sima Gong taking on the Blood-Sword Demon Lord in Jeok Cheongang’s place.

Of course, they wouldn’t be forgiven for their crimes.

At least, I had no right to forgive them.

Neither did Jeok Cheongang or the Bow Saint.

But I would remember that, in their final moments, the traitors had upheld at least the smallest measure of honor.

Unlike the discarded hunting dog, who would soon be forgotten by its master.

“That’s why we’re different. You and us.”

The Blood-Sword Demon Lord looked at me as I whispered in a small but clear voice. His eyes were red, their blood vessels burst.

“Jin Taekyung!”

Then, just as his cry erupted like a mouthful of blood—

*Thrust.*

The spearhead slid smoothly into his chest, as if cutting through tofu, swallowing the rest of his words.

No—swallowing the last faint traces of life left in him.

*Ding.*

A clear chime rang in my ears.

At the same time, a refreshing energy swept through my body like a mountain stream, once again filling me with new strength.

Unlike the person who’d met a gruesome death, pierced by a silver-white spearhead.

And just as someone who’d died a little earlier—so horribly she couldn’t even keep her body in one piece—had wanted.

*I mustn’t fall here? I have to get stronger than I am now?*

Feeling the crushing mental exhaustion weighing on my body, I turned to look toward the last trace of the Grand Mage, left behind where the Force arrow had swept through.

I murmured a word in my heart, one she could no longer hear.

*Don’t worry. I’ll do it. I promise.*

I didn’t know what the Lord of Heaven wanted.

But one thing was clear.

I had to keep going. To keep moving forward, I had to grow stronger.

Strong enough to far exceed the Lord of Heaven’s expectations—strong enough to make him regret this choice someday.

*Whatever gets in my way, I’ll just smash it to pieces.*

That was how I’d lived until now, and that was how I’d live from here on.

With that thought, I turned my unsteady body around.

Or at least, I tried to.

Until I saw the sharp, clean cuts on the slender arms and legs, one each, lying in a pool of blood, severed from a body.

No.

“……!”

Not until I spotted the traces of Teleport.
```

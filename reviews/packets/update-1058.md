<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1058.txt",
      "sha256": "85515a505e8a94f7f0b9cbb5b68992f2d14fb513d8282ebcdde70bc30bcc3671",
      "bytes": 14014
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "cac24437ff3d95eb89e65a699a5d512b66310f0563c12d0ce436a178c38dbb26",
      "bytes": 1394
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "5928ba5f9f942187d5c6e9149eb7593670dc2db24724f7fc8e9018bc095627ca",
      "bytes": 240988
    },
    {
      "path": "characters/Blood-Sword Demon Lord.md",
      "sha256": "da4bb4956059fdadde8be9ca90dbe2cfd485d09751686c100f4931777c0e87a2",
      "bytes": 920
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "4435ef8c620689c8d57e849e02a64577f78358f09b9955e5eb9b27dac3f38fc6",
      "bytes": 760
    },
    {
      "path": "characters/Human Butcher.md",
      "sha256": "2806a7121b83d1e1adc5b95f7f6a3db712145530098ad6030978a9727918c3e8",
      "bytes": 668
    },
    {
      "path": "characters/Hwangbo Eom.md",
      "sha256": "8be5c3d7a7a06ff6e1eec5ff725a44f246b129dc03b83670c32dcb0cf718dcb0",
      "bytes": 674
    },
    {
      "path": "characters/Hwangso.md",
      "sha256": "4a1cf1659c81205ce8d453a01d76d609b914ac0d35b6a7ba28d55f5dd4657b24",
      "bytes": 698
    },
    {
      "path": "characters/Hyeoncheon.md",
      "sha256": "656619e1d36a28f44a9294a9f84f79b44ab62e2bbea15b44e78a78ddc8a451f5",
      "bytes": 627
    },
    {
      "path": "characters/Namho.md",
      "sha256": "a9c35a0a3fd835006c484cf46fb7cfd54dbbc9d90a7df097d57561aa15ae687f",
      "bytes": 1092
    },
    {
      "path": "characters/Sama Pyo.md",
      "sha256": "c86c6aed3ffea14db961c0b438b07ee20c38908da2b531282ef32d67841900bb",
      "bytes": 850
    },
    {
      "path": "characters/Sima Gong.md",
      "sha256": "3ac77edcb8eb41f88d3bacf01c9ba5916cfb1dfe599147edb472dc738a1f5f13",
      "bytes": 877
    },
    {
      "path": "characters/Song Il.md",
      "sha256": "1c767c168b35ccd352c7c1c451186af9056515e5eed59cd0f9aa9fc7487fcba3",
      "bytes": 774
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "6fef6c79dbdbe76eed3e75d1f256cefb44dfad93530b85f6902416f4a8e64bd4",
      "bytes": 686
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "378d7aefdd54ea7c974a9b9e4024a94e31cc9cf3b9d4e85ce7257e2497dfa904",
      "bytes": 282320
    }
  ],
  "estimated_tokens": 12349
}
-->

# Durable State Update — Chapter 1058

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
1 and safe_through 1058. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1058. Profile updates may replace only one
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
  "chapter": 1058,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1058,
    "continuity_sources": [1058],
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
    "The allied forces have defeated Dark Heaven’s army and are searching the battlefield for survivors.",
    "Sama Pyo deliberately left Namho clues about his father’s covert actions to protect their companions without openly accusing his father.",
    "Sama Pyo intends to leave the Fire Dragon Pavilion and face what lies ahead alone; Jin Taekyung calls him a friend and orders him not to die.",
    "Sama Pyo has approached the Kongtong Sect Leader, who bears down on him with overwhelming killing intent.",
    "Sima Gong is dead; the Lord of Heaven’s identity and connection to Asmodeus remain unknown.",
    "Some Kongtong Sect survivors vanished to an unknown location.",
    "The Grand Mage departed for Qinghai on a new mission; the identity of the other servant remains unknown.",
    "A mysterious green light remains in the dispersing darkness."
  ],
  "continuity_sources": [
    1056,
    1057
  ],
  "open_questions": [
    "What are the identity and purpose of the Lord of Heaven, and is he connected to Asmodeus?",
    "Where did the missing Kongtong Sect survivors go?",
    "What is the new mission in Qinghai, and who is the other servant there?",
    "What is the mysterious green light?",
    "What will happen when Sama Pyo confronts the Kongtong Sect Leader?"
  ],
  "safe_through": 1057,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 송일     | **Song Il**        |
| 사마공    | **Sima Gong**      |
| 십왕     | **Ten Kings**       |
| 종남파    | **Zhongnan Sect**                |
| 암천     | **Dark Heaven**                  |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무인     | **martial artist**                               | Default term                                          |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 신법     | **movement technique**                           |                                                       |
| 살기     | **killing intent**                               |                                                       |
| 장문인    | **Sect Leader**                              |
| 장로     | **Elder**                                    |
| 제자     | **Disciple**                                 |
| 사형     | **Senior Brother**                           |
| 감숙     | **Gansu**              |
| 정마대전   | **Great Faction War**         |
| 도사      | **Daoist**                                                      |
| 혈검마군 | **Blood-Sword Demon Lord** | Antagonist commanding the army advancing on the Great Snow Mountain. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 황보엄 | **Hwangbo Eom** | Personal name of the Taeeul Merciless Sword. |
| 황소 | **Hwangso** | First-generation disciple of the Gongdao Sect and a reluctant search-party member. |
| 현천진인 | **Perfected Being Hyeoncheon** | Current Sect Leader of Wudang and Hyeongong's Senior Brother. |
| 남호 | **Namho** | Hidden Shadow Pavilion code name; literally associated with amber from the south. |
| 사마표 | **Sama Pyo** | Young Sect Leader of the Black Dragon Demon Gate. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 야왕 | **Night King** | Rumored epithet for Jin Taekyung in Taiyuan's red-light district. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 노호검객 | **Roaring Fury Swordsman** | Fiery-tempered elder and top-five master of the Zhongnan Sect. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 천산 | **Tianshan** | Mountain region identified as the Demonic Cult's headquarters. |
| 마공 | **demonic martial arts** | Martial arts that appear to defy common principles. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 태을무정검 | **Taeeul Merciless Sword** | Title of the Zhongnan Sect’s Second Martial Uncle, who is in Xi’an. |
| 황보 | **Hwangbo** | Surname form used when addressing Hwangbo Eom. |
| 삼노 | **Three Old Men** | Mocking designation used by the Western Heaven Demon Lord for the aged Qilian Three Fiends. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 흑룡마문 | **Black Dragon Demon Gate** | Unorthodox faction from Gansu. |
| 대초자곤 | **two-section staff** | Weapon carried by Sama Pyo's giant subordinate. |
| 공동파 | **Kongtong Sect** | Sect belonging to the Nine Sects and One Gang. |
| 흑야왕 | **Black Night King** | Epithet of Sima Gong, Sama Pyo's father and the Sect Leader who built the modern Black Dragon Demon Gate. |
| 화룡각 | **Fire Dragon Pavilion** | New name chosen for Taekyung's pavilion. |
| 검마 | **Sword Demon** | A Demonic Cult swordsman whose final technique is compared with One Annihilation. |
| 종남 | **Zhongnan Sect** | Orthodox faction that fought in the historic battle. |
| 돈황 | **Dunhuang** | City identified as the foremost defensive line in Gansu. |
| 진인 | **Perfected One** | Honorific for the two Kongtong Elders killed at Dunhuang. |
| 천산삼노 | **Three Elders of Tianshan** | The three former Demonic Cult fiends serving the Blood-Sword Demon Lord. |
| 대술사 | **Grand Mage** | Title of the veiled woman leading the white-robed mages. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 사형 | 황소 | senior_disciple_to_junior_disciple | you; brat | blunt-commanding | The unnamed Senior Brother sharply scolds Hwangso and orders him to search. |
| 황소 | 사형 | junior_disciple_to_senior_disciple | Senior Brother | casual-but-junior | Hwangso addresses his supervising senior with a familiar but deferential tone while complaining about the mission. |
| 사마표 | 태산 | Young Sect Leader to subordinate | Taishan | informal and patronizing | Sama Pyo calls Taishan by name while ordering him to leave. |
| 태산 | 사마표 | subordinate to Young Sect Leader | Lord | crude and deferential | Taishan uses 주군 while obeying Sama Pyo. |
| 남호 | 태산 | guide_to_pavilion_member | Taishan | blunt and exasperated | Namho directly rebukes Taishan for eating the poisonous blood-feeding fungus. |
| 남호 | 사마표 | guide_to_young_sect_leader | Young Sect Leader | blunt and admonishing | Namho warns Sama Pyo that all grass and animals in the territory belong to the Nanman Beast Palace. |
| 사마표 | 남호 | young_sect_leader_to_guide | Elder Namho | formal and apologetic | Sama Pyo apologizes after Taishan attempts to seize the calf. |
| 태산 | 남호 | Fire Dragon Pavilion member to guide | Namho | clipped, childlike, and informal | Taishan directly addresses Namho while asking what Dark Heaven is. |
| 남호 | 각주 | guide to pavilion master | Pavilion Master | blunt, hostile, and abusive | Namho addresses Jin as 각주 while accusing him of causing the disturbance. |
| 사마표 | 각주 | Fire Dragon Pavilion member to pavilion master | Pavilion Master | formal but sardonic | Sama Pyo addresses Jin as 각주 while questioning his account of the incident. |
| 태산 | 각주 | Fire Dragon Pavilion member to pavilion master | Pavilion Master | clipped, childlike, and informal | Taishan directly asks Jin whether his Lord Sama Pyo is safe. |
| 신의 | 태산 | senior physician to younger ally | Young Hero Taishan | urgent and respectful | The Divine Physician uses this address while pleading with Taishan to keep moving. |
| 사마공 | 사마표 | father to son | Pyo | intimate and familiar | Sima Gong calls him 표야 and 내 아들아. |
| 혈검마군 | 삼노 | former Demonic Cult fiend to subordinate | Elder Three | familiar and contemptuous | Addresses the wounded elder as 삼노 while asking how he compares to the Fire King. |
| 사마표 | 삼노 | enemy addressing an elder of the Three Elders of Tianshan | you | casual and taunting | Sama Pyo answers the Third Elder’s accusation and taunts him while attacking. |
| 사마표 | 사마공 | son to father | you; Father | familiar and confrontational | Sama Pyo challenges his father during their battlefield confrontation. |
| 송일 | 황보엄 | Senior Brother to Junior Brother | Junior Brother | familiar and heated | Song Il calls Hwangbo Eom 사제. |
| 황보엄 | 송일 | Junior Brother to Senior Brother | Senior Brother | familiar and dryly teasing | Hwangbo Eom calls Song Il 대사형. |
| 혈검마군 | 사마공 | former bargaining allies turned enemies | you; you traitor | blunt and hostile | Uses direct, contemptuous forms while accusing Sima Gong of betraying him. |
| 사마공 | 혈검마군 | former bargaining allies turned enemies | you; you Demonic Cult bastard | calm and contemptuous | Uses 당신 before ending with the insult 마교 잡놈아. |
| 대술사 | 혈검마군 | subordinate_to_commander | Demon Lord | respectful and formal | Addresses him as 마군 while acknowledging his injuries. |
| 혈검마군 | 대술사 | commander_to_subordinate | Grand Mage | blunt and commanding | Orders her to heal him immediately. |

## Listed compact profiles

### Blood-Sword Demon Lord.md

# Blood-Sword Demon Lord (혈검마군)

- **Safe through:** Chapter 1056
- **Aliases:** None
- **Role:** The Blood-Sword Demon Lord is a formidable martial master who commands the force advancing on the Great Snow Mountain and now serves the Lord of Heaven.
- **Personality:** Devoted to his master and proud of his abilities, he is deeply wounded by perceived distrust and resolves to prove his worth.
- **Voice:** Casually familiar and self-amused, addressing Jeok Cheongang respectfully as Senior while trading blunt insults; his easy laughter can turn to a low, cold intensity.
- **Relationships:** He serves the Lord of Heaven with deep devotion, but the Grand Mage says the Lord ordered his disposal; he has been ordered not to kill Jin Taekyung, admires Jeok Cheongang, and once shared the Demonic Cult with the fiends who became Black Ghosts.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1057
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Human Butcher.md

# Human Butcher (인도)

- **Safe through:** Chapter 1042
- **Aliases:** None
- **Role:** Former mysterious Han Chinese mounted-bandit power in Northern Gaoyuan commanding fifty subordinates; a Peak master killed by an unnamed old man in a single move
- **Personality:** Cold, intimidating, and murderous; he kills people as though slaughtering livestock
- **Voice:** Cold, curt, and quietly threatening
- **Relationships:** He is one of four powerful participants at the Northern Gaoyuan gathering, intimidates Temur, and has claimed Ghost Sword Wipeng as his personal target in the proposed attack

### Hwangbo Eom.md

# Hwangbo Eom (황보엄)

- **Safe through:** Chapter 1054
- **Aliases:** Taeeul Merciless Sword
- **Role:** Supreme Peak master of the Zhongnan Sect and its Second Martial Uncle, known as the Taeeul Merciless Sword.
- **Personality:** Ruthless, severe, proud, and deeply invested in restoring Zhongnan's standing.
- **Voice:** Calmly courteous when offering tea, then cold, commanding, and cutting when reprimanding others.
- **Relationships:** Song Il and Hwangbo Eom are Gong Iljung’s two Senior Brothers; the three served the same Master for over fifty years, and Hyuk Sopyung is Hwangbo’s junior.

### Hwangso.md

# Hwangso (황소)

- **Safe through:** Chapter 915
- **Aliases:** None
- **Role:** First-generation disciple of the Gongdao Sect in Sichuan, deployed with roughly thirty second- and third-generation disciples to search for the surviving Third Fiend.
- **Personality:** Privileged, impatient, pleasure-seeking, inattentive, and dismissive of the danger surrounding the mission.
- **Voice:** Complaining and casual, with irreverent sarcasm toward his Senior Brother and the search.
- **Relationships:** His Senior Brother supervises him, and his prosperous merchant father forced him into the Murim to establish family connections.

### Hyeoncheon.md

# Perfected Being Hyeoncheon (현천진인)

- **Safe through:** Chapter 505
- **Aliases:** None
- **Role:** Perfected Being Hyeoncheon is the current Sect Leader of Wudang, a veteran Daoist master, and a Supreme Peak martial artist who succeeded his master as Sect Leader.
- **Personality:** Grave, dignified, reflective, and burdened by memories of the Great Faction War.
- **Voice:** Measured, solemn, and calm with the authority of a Sect Leader.
- **Relationships:** Hyeongong is his Junior Brother, and both studied under the same master from childhood.

### Namho.md

# Namho (남호)

- **Safe through:** Chapter 1057
- **Aliases:** Elder Chao
- **Role:** Namho is an eighty-year-old non-Han Hidden Shadow Pavilion agent who spent more than fifty years undercover in Nanman and maintained contact with Central Plains intelligence through the Pavilion’s Hidden Thread; he guides the Fire Dragon Pavilion and represents Jin Taekyung and the Murim Alliance in negotiating the survivors’ chance to rebuild the Murong household.
- **Personality:** Duty-bound, pragmatic, and observant; uses theatrical violence to protect intelligence work and takes a veteran’s concern for the younger generation’s resolve.
- **Voice:** Measured and reflective when advising the younger generation, loudly abusive when maintaining his local cover, and capable of theatrical boasts and dry humor.
- **Relationships:** Namho is a Hidden Shadow Pavilion contact for Jin Taekyung and the Fire Dragon Pavilion, receives intelligence from the Pavilion Master, and knows the code used by the Thousand-Faced Fox.

### Sama Pyo.md

# Sama Pyo (사마표)

- **Safe through:** Chapter 1057
- **Aliases:** Black Dragon Saber
- **Role:** Young Sect Leader and heir of the Black Dragon Demon Gate, a Morning Star reputed to be no less than the Ten Dragons and Phoenixes.
- **Personality:** Courteous and calculating, he chooses what he believes is right over expedience and accepts responsibility for his choices, even when they expose him to blame.
- **Voice:** Polite and ingratiating in public, with sardonic humor and controlled evasiveness.
- **Relationships:** Sama Pyo is Sima Gong’s son and chosen heir, commands Taishan, and is Jin Taekyung’s friend; he deliberately let Namho suspect his father’s actions to protect their companions, was Ju Hwaran’s former fiancé, and is hostile toward Song Ilseom.

### Sima Gong.md

# Sima Gong (사마공)

- **Safe through:** Chapter 1057
- **Aliases:** Black Night King
- **Role:** Sima Gong is the Sect Leader who built the Black Dragon Demon Gate into a major unorthodox power and the father of its Young Sect Leader, Sama Pyo.
- **Personality:** Sly and calculating yet capable of risking himself for a moment of conscience, he values his heir’s future and repaying a debt to Jeok Cheongang.
- **Voice:** Polished and persuasive, with smooth rhetorical turns and a composed, gently teasing manner.
- **Relationships:** Sama Pyo is his youngest son among seven older brothers and nine older sisters; Sima Gong chose him as heir and approved his plan to answer the Gate’s betrayal. Sama Pyo returned to remain with him as he died. Sima Gong aided Jeok Cheongang despite their history.

### Song Il.md

# Song Il (송일)

- **Safe through:** Chapter 1056
- **Aliases:** Roaring Fury Swordsman
- **Role:** Elder of the Zhongnan Sect, known as the Roaring Fury Swordsman and one of Sect Leader Gong Iljung’s two Senior Brothers.
- **Personality:** Arrogant and domineering, but capable of remorse over choices that harmed his sect and those he failed to protect.
- **Voice:** Gruff, cutting, condescending, and threatening, with formal authority used to pressure those beneath him.
- **Relationships:** Gong Iljung is his junior Sect Leader and martial younger brother; Gong Ilhyuk is a junior Disciple of his sect; he recognizes Baek Museong and Cheongpung through their Huashan and Sword Saint connections.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 1057
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo; becomes explosively violent when his meat is threatened.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord, trusts Jin Taekyung as Pavilion Master, and has grown attached to the Fire Dragon Pavilion members.

## Korean source

```text
1058화




그야말로 한순간이었다.

전신에 피를 흠뻑 뒤집어쓴 채 적들을 도살하던 혈의인(血衣人)들이 사마표를 포위하며 무시무시한 살기를 쏘아 보낸 것은.

스아아아.

그 머릿수가 약 일백.

그들이 발산하는 기파가 얼마나 강렬했는지, 아직 완전히 가시지 않은 전장의 열기가 삽시간에 얼어붙었고 단숨에 일변한 공기의 흐름이 또렷하게 느껴졌다.

십여 장 밖에서 걸음을 멈춘 채 지켜보고 있던 내게도.

그리고 그보다도 먼 곳에서, 영문도 모른 채 명령을 따라 대기하고 있던 화룡각 대원들에게도.

“주군! 위험하다!”

거리를 무색하게 만들 정도로 짙은 살기다.

본능적으로 사마표의 위험을 직감한 태산은 다급한 외침과 함께 신형을 날렸고, 이내 곧장 가로막혔다.

다른 누구도 아닌, 바로 내게.

“이게 무슨 짓인가, 각주!”

으르렁거리는 듯이 토해 내는 외침과 맹렬하게 발산되는 투기(鬪氣).

처음 본다.

녀석의 이런 모습은.

하지만 나로서도 물러설 수 없다.

지금의 이 상황은, 염병할 운명이나 불운 따위가 아니라 사마표 스스로의 선택이기에.

“가지 마. 아직은.”

“태산이, 이런 말도 안 되는 명령은 따르지 않는다!”

“명령 내린 적 없어. 부탁한 거지. 사마표가 내게 나서지 말아 달라고 했던 것처럼.”

“……!”

태산의 퉁방울만 한 눈동자가 흔들린다.

그리고 때맞춰 뒤쫓아온 화룡각 대원들이 뭐라 말하기도 전에, 남호가 평소답지 않은 침잠한 음성으로 불쑥 입을 열었다.

물론, 목말을 타고 있어서 그런지 딱히 권위가 있어 보이지는 않았지만.

“네 녀석이 지금 어떤 마음인지는 알겠다만, 지금은 적절한 때가 아니다.”

“남호, 하지만.”

“어허, 이 성난 황소 같은 놈을 보았나!”

찰싹!

야무지다 못해 앙칼진 손짓으로 태산의 이마를 후려친 남호가 준엄하게 일갈했다.

“정에 눈이 먼 것으로도 부족해서 이제는 귀까지 먹었누. 앞서 각주가 했던 말도 제대로 듣지 않았단 말이냐?”

맞다.

남호의 말처럼, 나는 태산에게 분명히 말했다.

아직은…… 가지 말라고.

‘그래, 아직은 아니지.’

마음속으로 작게 뇌까린 나는, 갈등 끝에 힘없이 대초자곤(大相子根)을 내려놓는 태산의 어깨를 두드려 주었다.

동시에 고개를 돌려 한 곳을 바라보았다.

선명한 살기를 내뿜고 있는 일백의 혈의인…… 아니, 공동파의 제자들을.

그런 그들의 중심에서 깊게 가라앉은 눈동자로 사마표를 응시하는 노인을.

‘현천진인(玄天眞人).’

그것이 노인의 정체였다.

명실상부한 구파일방의 일익인 공동파의 장문인이자, 감숙성 제일의 무인.

그리고…….

아군이라 믿었던 이들에게 배신당하고 수많은 제자를 잃어야만 했던, 또 한 명의 복수귀(復讎鬼).

화아아악.

웅혼한 공력에 소매가 부풀어 오른다.

지금 이 순간, 도무지 깊이를 알 수 없는 그 무감정한 먹빛 눈동자 위에 비친 것은 사마표가 아니었다.

단숨에 찢어 죽여도 시원치 않을, 원수의 핏줄이었다.



* * *



우우웅.

반경 수 장의 공기가 부르르 떨리고, 숨이 막힌다.

마치 보이지 않는 거인의 손처럼 서서히 사방을 조여 오는 막강한 기파에 사마표가 굳어 버린 그 순간, 현천진인이 불현듯 입을 열었다.

“근래 들어 계속해서 떠오르더군. 정마대전의 한복판에서 도우(道友)의 춘부장을 처음으로 만났을 때가.”

젖먹이 시절부터 지금까지, 일평생을 도가(道家)에 몸담은 이 노도사는 특유의 온화한 성품으로 신망이 높았다.

비록 십왕(十王)의 반열에는 들지 못했을지언정, 그는 공동파라는 걸출한 명문대파의 장문인임에도 늘 겸손했고 항상 스스로를 낮추었다.

그러나 제아무리 큰 그릇이라 하더라도, 담을 수 있는 것에는 한계가 존재하는 법이었다.

“동시에 후회했네. 차라리 그때 죽여 버렸더라면 어땠을까, 하고.”

깊은 탄식이 묻어나는 그 음성에, 사마표는 대답하지 않았다.

아니, 대답할 수 없었다.

그가 아직 진실을 이야기하지 않았음에도, 눈앞의 노도사는 이미 그 일부를 들여다보고 있었으니까.

그리고 현천진인이 이와 같은 사실을 처음으로 알게 된 것은, 다름 아닌 어느 한 여인의 입을 통해서였다.

“처음에는 믿고 싶지 않았네. 돈황에서 살아남은 생존자들을 흔들어 내분(內紛)을 일으키려는 수작이라고, 더욱 큰 흉계를 위해 우리를 발판으로 삼았다 생각하려 애썼지.”

현천진인은 풀숲 속에서 조용히 숨죽인 채 들었던 정보들을 머릿속에서 떨쳐 내고자 했으나, 날이 갈수록 의심은 깊어졌다.

흑야왕(黑夜王) 사마공이라는 한 인간에 대한 불신.

돈황으로 출진하기 전 느꼈던, 심상치 않은 징조까지 포함해 모든 것이 하나의 톱니바퀴처럼 정교하게 맞물리고 있었다.

“돌이켜 볼수록 희한하더군. 흑룡마문으로부터 전해 받은 정보는 모조리 어긋났고, 피를 흘린 것은 우리뿐이었으니.”

예로부터 공동파의 근거지인 공동산(崆峒山)이 감숙성의 동남면 끝자락에 위치했다면, 흑룡마문의 권역은 돈황 일대를 아우르는 서북면.

그렇기에 공동파와 그를 따르는 여러 문파는 흑룡마문이 제공하는 정보를 토대로 움직였고, 끔찍할 정도의 대패(大敗)를 당했다.

“수천이 죽었지. 그날 하루 동안에만.”

조금씩 떨려 오는 현천진인의 음성에, 사방을 에워싼 일백의 제자들은 이를 악물었다.

어찌 잊을까. 벼락처럼 시작된 그 참혹했던 전투를.

아니, 일방적인 학살을.

“수성(守城) 따위는 아무런 의미도 없었네. 홀연히 나타난 그 엄청난 대군과 마주한 우린 그 무엇도 할 수 없었어.”

천산삼노.

수십여 년의 세월을 거슬러 돌아온 천산의 세 늙은이가 선봉에 섰고, 두려움이라는 감정을 느끼지 못하는 수만 명의 교도가 그 뒤를 따랐다.

쉼 없이 쏘아 보낸 화살도, 단단한 암석 위에 황토를 발라 세운 성벽도 그들을 막을 수는 없었다.

칠흑과도 같았던 그 거대한 인(人)의 파도는 단숨에 높은 성벽을 무너트리고 모든 것을 휩쓸었다.

오랫동안 동고동락한 누군가의 사형제, 벗, 혹은 혈육들의 생명을 집어삼키며.

“차라리 그곳에서 함께 싸우다가 죽고 싶었지. 숨이 끊기는 그 순간까지 장렬하게.”

이는 비단 현천진인만의 생각이 아니었다. 붉게 물든, 동시에 어느덧 습기가 맺힌 백여 쌍의 눈동자가 그것을 증명했다.

하지만 그들은 끝끝내 살아남았다.

살아남아야 했다.

비명에 죽어 간 이들의 복수를 위해서라도.

“그렇게 우리는 비겁하게 도망쳤네. 도중에 뜻하지 않은 도움을 받아 손쉽게 놈들의 추격을 뿌리칠 수 있었지만, 다른 이들은 아니었겠지.”

행운은 모두에게 공평하게 돌아오지 않았다.

돈황에서만 수천이 죽었고, 피눈물을 흘리며 도주한 생존자들도 사냥감 신세를 면치 못했다.

그들은 살기 위해 뿔뿔이 흩어졌고, 철저하게 사냥당하는 과정에서 다시 수천이 죽거나 다쳤다.

그러나 암천의 포위망을 벗어난 후에도, 현천진인을 비롯한 공동파의 제자들은 후방으로 복귀하지 않았다.

정확히는 모두가 크고 작은 부상을 입었기에 당장은 복귀할 수 없었다.

하지만 대술사가 그들의 마음 깊이 심어 놓은 의심은 이미 싹을 틔웠고, 앞서 벌어진 암천과의 전투에서 극심한 부상을 입은 현천진인은 고통에 신음하던 와중에 불현듯 깨달았다.

복수를 다짐하며 생사를 오가던 그 순간, 자신의 눈앞을 스쳐 지나가는 기억 속 낯익은 면면들이 누구의 것인지.

그것은 은백색 면사로 얼굴을 가린 정체 모를 여인도 아니요, 두 장로와 수백의 제자들을 잡아 죽인 천산삼노나 혈검마군도 아니었다.

다름 아닌, 자신들의 등 뒤를 든든히 지켜 줄 것이라 믿었던 아군들이었다.

“참으로 이상한 일이지 않나, 도우.”

낮게 깔린 목소리.

사흘간 죽음의 고비를 견딘 끝에 가까스로 부상에서 회복한 현천진인은 생각했더랬다.

어째서일까.

곰의 쓸개를 씹듯이 복수를 다짐하던 그 순간에 왜 하필 그들이 떠올랐을까.

흑야왕 사마공. 노호검객 송일. 태을무정검 황보엄.

더불어 흑룡마문의 수족이나 다름없는 감숙의 여러 영수(領袖)들.

은백색의 면사 아래로 흘러나온 그들 한 사람 한 사람의 얼굴과 이름을 떠올릴 때마다, 왜 가슴 깊은 곳에서 불길이 솟구치는 것일까.

결국, 현천진인은 이 의문에 대한 답을 찾아냈다.

자신의 두 눈으로 직접 그 답을 확인하기 위해, 살아남은 제자들과 함께 이곳으로 왔다.

그리고 지금 이 순간, 복수를 시작하기에 앞서 스스로 찾아온 한 청년을 마주하고 있다.

“사마가(家)의 아해야.”

어느덧 뒤바뀐 말투.

쇳소리가 섞인 목소리는 담담했으나, 노도사의 눈동자에는 차갑게 이글거리는 불꽃이 담겨 있었다.

“네 아비를 데려오거라. 검을 뽑기 전, 반드시 확인해야 하는 것이 있으니.”

드드득.

잘게 떨리는 지면.

고여 있던 피 웅덩이 위로 일어나는 파문을 말없이 내려다보던 사마표는, 그때까지도 깊게 숙였던 고개를 들며 입을 열었다.

“이미 떠났습니다. 두 번 다시 돌아올 수 없는 먼 곳으로.”

“……!”

현천진인의 눈이 부릅떠졌다.

사마표를 둘러싼 채 숨 막히는 살기를 뿜어내던 모든 공동파의 제자들 역시 마찬가지였다.

그들은 조금 전 들었던 말에 담긴 의미를 본능적으로 깨닫고 있었다.

죽었다.

흑야왕 사마공이.

자신들의 손으로 직접 죽음을 내려야 마땅한, 천인공노할 원수가.

그리고 이와 같은 운명을 맞이한 배신자는, 비단 사마공뿐만이 아니었다.

“장문인!”

어디선가 들려오는 통렬한 외침.

화살 같은 속도로 수십여 장의 거리를 단숨에 좁힌 공동파의 제자가, 슬픔과 분노로 얼룩진 얼굴로 현천진인의 앞에 엎드렸다.

“놈들이, 그자들이……!”

통곡과도 같은 그 부르짖음이 끝나기도 전, 불현듯 고개를 돌린 현천진인은 똑똑히 볼 수 있었다.

저 멀리 비스듬히 솟아 있는 종남파의 깃발을.

아니, 정확히는 그 깃대에 묶인 채 힘없이 흩날리고 있는 두 개의 새하얀 천 조각을.

“조기(弔旗)……!”

누군가의 악물린 입술 사이로 흘러나온 탄식에, 주위를 에워싸고 있던 기파가 거세게 출렁였다.

누군가의 죽음을 의미하는 흰색 천. 그리고 지금 막 되돌아온 제자의 반응.

이 상황이 의미하는 바는 명백했다.

노호검객 송일과 태을무정검 황보엄.

사마공에 이어 반드시 처단해야 할, 종남파의 두 배신자마저 떠난 것이다.

그 어떤 경신법으로도 잡을 수 없는 머나먼 그곳, 저승으로.

“죽어? 죽었단 말이냐? 이렇게, 고작 이런 식으로!”

으득.

현천진인은 입술을 깨물었다. 

살이 찢어지고 피가 튀었으나 이 정도 고통 따위, 당장이라도 터져 버릴 듯한 가슴에 비하면 아무것도 아니었다.

“어떻게, 어떻게 감히……!”

현천진인은 격노했다.

아직 성치 않은 몸임에도 불구하고 그에게서 뿜어져 나오는 거대한 기운이 사방을 짓누르자, 주위에 있던 공동파의 제자들마저 숨을 삼켜야 했다.

그러나 단 한 사람, 사마표만큼은 예외였다.

“제가 대신하겠습니다.”

초절정 고수의 기파를 온몸으로 견뎌 내며 가까스로 쥐어 짜낸 음성에, 현천진인의 눈빛이 깊게 가라앉았다.

“지금, 무어라 했느냐?”

“제가 대신한다 하였습니다. 죄 많은 아비의 잘못을, 그로 인해 치러야 할 마땅한 죗값을 받겠습니다.”

순간 내려앉은 침묵 사이에서, 사마표는 현천진인을 포함한 모두를 향해 고개를 숙이며 말을 이었다.

“실로 건방진 언행이라는 것을 압니다. 별것 아닌 제 목숨으로, 떠난 이들의 원한을 대신할 수 없다는 것 또한 압니다.”

맞다.

사람의 마음은 언제든지 채워 넣을 수 있는 종류의 것이 아니다.

한번 뚫린 구멍은 무엇으로도 메울 수 없다.

그저 잊기 위해 무언가를 계속해서 채워 넣거나, 채워도 채워도 메워지지 않는 그 구멍을 바라보며 기억할 뿐이다.

한순간의 실수로 사라진 것을. 잃어버린 것에 대한 후회를.

바로 그런 이유에서였다.

사마표가 지금 이 자리에 있는 이유는, 아버지와는 다른 길을 가고자 하는 것은.

“눈에는 눈. 이에는 이. 죽음에는 죽음.”

무림인 간의 혈채(血債)는, 오직 피로만 갚을 수 있다.

“베십시오. 원망하지 않겠습니다.”

그리고 그 순간.

스릉.

현천진인의 허리춤에서, 눈부신 섬광이 뿜어져 나왔다.
```

## Final English reading copy

```markdown
# Chapter 1058

It happened in an instant.

The Blood-Clad Men, drenched head to toe in blood as they slaughtered their enemies, surrounded Sama Pyo and unleashed a terrifying wave of killing intent.

*Shhhhhh.*

There were about a hundred of them.

Their qi was so fierce that the lingering heat of the battlefield froze in a flash. The flow of the air changed all at once, and I could feel it clearly.

Even from some thirty-odd yards away, where I’d stopped to watch.

And even farther off, where the Fire Dragon Pavilion members stood waiting as ordered, with no idea what was happening.

“My Lord! It’s dangerous!”

The killing intent was so dense it seemed to erase the distance between them.

Taishan instinctively sensed Sama Pyo was in danger. With an urgent shout, he launched himself forward—only to be stopped immediately.

By no one other than me.

“What do you think you’re doing, Pavilion Master!”

He roared the words, his fighting spirit pouring out fiercely.

I’d never seen him like this before.

But I couldn’t back down either.

This wasn’t some damn fate or bad luck. This was Sama Pyo’s own choice.

“Don’t go. Not yet.”

“Taishan will not obey such an unreasonable order!”

“I’m not ordering you. I’m asking. Just like Sama Pyo asked me not to interfere.”

“……!”

Taishan’s enormous eyes wavered.

The Fire Dragon Pavilion members caught up, but before any of them could say a word, Namho suddenly spoke in an unusually subdued voice.

Though riding on someone’s shoulders didn’t exactly make him look authoritative.

“I understand how you feel right now, but this isn’t the right time.”

“Namho, but—”

“Honestly, look at this angry bull of a man!”

*Smack!*

Namho struck Taishan’s forehead with a sharp, emphatic slap, then rebuked him sternly.

“You weren’t satisfied with letting sentiment cloud your eyes, so now you’ve gone deaf too? You didn’t even hear what the Pavilion Master just said?”

He was right.

As Namho said, I’d told Taishan clearly.

*Not yet… Don’t go yet.*

*That’s right. Not yet.*

I murmured to myself, then patted Taishan on the shoulder as he lowered his two-section staff, his strength seeming to leave him after his inner struggle.

At the same time, I turned to look toward the hundred figures radiating such vivid killing intent.

The Blood-Clad Men—or rather, the Kongtong Sect Disciples.

And at their center, an old man stared at Sama Pyo with deeply sunken eyes.

*Perfected Being Hyeoncheon.*

That was who he was.

The Sect Leader of the Kongtong Sect, one of the Nine Sects and One Gang, and the greatest martial artist in Gansu.

And…

Another avenger, betrayed by those he had trusted as allies and forced to lose countless Disciples.

*Whoooosh.*

His sleeves swelled with the force of his formidable internal energy.

At that moment, the emotionless, ink-black eyes—so deep their depths were impossible to discern—didn’t reflect Sama Pyo.

They reflected the bloodline of his enemy: a man Hyeoncheon would gladly tear to pieces.

* * *

*Rumble.*

The air trembled within a radius of several yards. It was hard to breathe.

In the moment the overwhelming qi began slowly tightening around him from every direction, like the hand of an invisible giant, Sama Pyo froze. Then Perfected Being Hyeoncheon suddenly spoke.

“Lately, I keep remembering when I first met your esteemed father, my friend, in the middle of the Great Faction War.”

From infancy to old age, the elderly Daoist had devoted his entire life to the Dao. His character was gentle, and he had earned the respect of many.

Though he had never joined the ranks of the Ten Kings, he had always been humble, even as Sect Leader of the great Kongtong Sect.

But even the largest vessel has its limits.

“At the same time, I regretted it. I wondered if I should have killed him then and there.”

Sama Pyo said nothing in response to the deep sigh in Hyeoncheon’s voice.

No—he couldn’t answer.

The old Daoist before him had already glimpsed part of the truth, even though Sama Pyo hadn’t told him yet.

And the first time Hyeoncheon learned anything of the sort had been through a woman.

“At first, I didn’t want to believe it. I tried to convince myself it was a ploy to stir up internal strife among the survivors from Dunhuang—that we were being used as stepping-stones for an even greater scheme.”

Hyeoncheon had tried to shake the information he’d heard while holding his breath in the undergrowth from his mind. But with every passing day, his suspicions had deepened.

His distrust of one man: Sima Gong, the Black Night King.

Everything—including the ominous signs he had sensed before setting out for Dunhuang—had fitted together like the precise teeth of a single gear.

“The more I thought about it, the stranger it seemed. Every scrap of information we received from the Black Dragon Demon Gate was wrong, and we were the only ones who bled.”

Kongtong Mountain, the Kongtong Sect’s home since ancient times, stood at the southeastern edge of Gansu. The Black Dragon Demon Gate’s territory, by contrast, covered the Dunhuang region in the northwest.

So the Kongtong Sect and the many sects that followed it had acted on information provided by the Black Dragon Demon Gate—and suffered a crushing defeat.

“Thousands died. In that single day.”

At the slight tremor in Hyeoncheon’s voice, the hundred Disciples surrounding them clenched their teeth.

How could they forget that horrific battle, which had begun like a bolt of lightning?

No—it had been a one-sided slaughter.

“Defending the city meant nothing. When that enormous army appeared out of nowhere, we couldn’t do a thing.”

The Three Elders of Tianshan.

The three old fiends from Tianshan, returned after decades away, had led the charge. Behind them came tens of thousands of cultists who knew no fear.

Neither the arrows they fired without pause nor the city walls—built of sturdy stone coated in yellow earth—could stop them.

That immense human tide, black as night, had brought down the high walls in an instant and swept away everything in its path.

The lives of brothers, friends, and family members who had stood by them through so many years.

“I would rather have fought there with them and died. Heroically, with my last breath.”

Hyeoncheon wasn’t the only one who felt that way. A hundred pairs of eyes, reddened and now glistening with tears, bore witness to it.

But they had survived in the end.

They had to survive.

If only to avenge those who had died screaming.

“So we ran away like cowards. We received unexpected help on the way and easily shook off their pursuit, but the others weren’t so lucky.”

Luck didn’t come equally to everyone.

Thousands had died in Dunhuang alone, and even those who had fled in tears had remained prey.

They scattered to survive, and thousands more were killed or wounded as they were hunted down one by one.

But even after escaping Dark Heaven’s encirclement, Hyeoncheon and the Kongtong Sect Disciples hadn’t returned to the rear.

More precisely, they couldn’t return yet. Every one of them had suffered some injury, large or small.

But the suspicion the Grand Mage had planted deep in their hearts had already taken root. And while Hyeoncheon was groaning in pain from the severe injuries he’d sustained in the battle against Dark Heaven, he suddenly realized whose familiar faces had flashed through his memories.

Back then, as he hovered between life and death and swore revenge.

They weren’t the mysterious woman whose face had been hidden behind a silver-white veil. They weren’t the Three Elders of Tianshan or the Blood-Sword Demon Lord, who had captured and killed two Elders and hundreds of Disciples.

They were the allies he had believed would protect their rear.

“It’s strange, isn’t it, my friend?”

His voice was low.

After three days at death’s door, Hyeoncheon had barely recovered from his injuries. He’d thought then:

*Why?*

Why had their faces come to mind as he vowed revenge, as if chewing bear gall?

The Black Night King, Sima Gong. The Roaring Fury Swordsman, Song Il. The Taeeul Merciless Sword, Hwangbo Eom.

And the many leaders of Gansu, no different from the Black Dragon Demon Gate’s servants.

Why did fire surge from deep in his chest whenever he recalled each face and name the woman had spoken of from behind her silver-white veil?

In the end, Hyeoncheon had found the answer.

To see it with his own eyes, he had come here with the Disciples who had survived.

And at this very moment, before beginning his revenge, he faced a young man who had come to him of his own accord.

“Boy of the Sama family.”

His way of speaking had changed.

His voice was steady, edged with iron, but cold flames burned in the old Daoist’s eyes.

“Bring me your father. There’s something I must confirm before I draw my sword.”

*Rumble.*

The ground trembled faintly.

Sama Pyo silently watched the ripples spreading across the pools of blood. Then, at last, he raised his head, which had been bowed all this time, and spoke.

“He’s already gone. To a distant place from which he can never return.”

“……!”

Perfected Being Hyeoncheon’s eyes flew open.

So did those of every Kongtong Sect Disciple around Sama Pyo, still radiating suffocating killing intent.

By instinct, they understood what his words meant.

*He was dead.*

*The Black Night King, Sima Gong.*

The enemy they ought to have put to death with their own hands—the heinous traitor who deserved no less.

And Sima Gong wasn’t the only traitor who had met this fate.

“Sect Leader!”

A heartrending cry came from somewhere.

A Kongtong Sect Disciple closed a distance of well over a hundred yards in an instant, moving like an arrow. His face was streaked with grief and fury as he threw himself down before Hyeoncheon.

“They—they…!”

Before his sobbing shout could even end, Hyeoncheon suddenly turned his head.

He saw it clearly in the distance: the flag of the Zhongnan Sect, rising at an angle.

Or rather, he saw the two white cloths tied to its pole, fluttering weakly.

“A mourning flag…!”

At the anguished whisper that slipped through someone’s clenched teeth, the qi surrounding them surged violently.

The white cloth signaled someone’s death. Then there was the reaction of the Disciple who had just returned.

The meaning was clear.

The Roaring Fury Swordsman, Song Il, and the Taeeul Merciless Sword, Hwangbo Eom.

The two Zhongnan Sect traitors, whom they’d meant to punish after Sima Gong, were gone too.

To the far-off place no movement technique could reach: the afterlife.

“Dead? You mean they’re dead? Just like that? Is that all they get?”

*Grrk.*

Hyeoncheon bit his lip.

The flesh split and blood flew, but that pain was nothing beside the agony in his chest, which felt ready to burst.

“How—how dare they…!”

Hyeoncheon was enraged.

Despite his still-healing body, his immense qi pressed down all around him. Even the Kongtong Sect Disciples nearby had to hold their breath.

Only one person was an exception: Sama Pyo.

“I’ll take his place.”

His voice was barely squeezed out as he endured the Supreme Peak master’s qi with his whole body. Hyeoncheon’s eyes sank deeply.

“What did you just say?”

“I said I’ll take his place. I’ll accept the just punishment for my sinful father’s wrongs.”

In the silence that fell, Sama Pyo bowed his head to everyone, Hyeoncheon included, and continued.

“I know how presumptuous that sounds. I know my insignificant life can’t make up for the grudge of those who are gone.”

He was right.

A person’s heart wasn’t something that could simply be filled again whenever it was empty.

Nothing could fill a hole once it had been torn open.

All you could do was keep filling it with things in an attempt to forget, or remember as you stared at the hole that remained no matter how much you put inside.

Remember the things lost in a single moment of carelessness. Regret what you’d lost.

That was why Sama Pyo was here now.

Why he wanted to take a different path from his father.

“An eye for an eye. A tooth for a tooth. Death for death.”

In the Murim, a blood debt between martial artists could only be repaid with blood.

“Strike me down. I won’t hold it against you.”

And at that moment—

*Shing.*

A dazzling flash burst from the sword at Perfected Being Hyeoncheon’s waist.
```

<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1065.txt",
      "sha256": "e1e15165b30d2c3e9c119d9e0d29b42fc00bb6363d2bdca3e32b406e4398b477",
      "bytes": 16788
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "e4c22725f8c15858a884d32800b6b26f18448262e281ad1e6f2e9b1820346b81",
      "bytes": 868
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "e6e90c56c4fb5b6e5840445ba07954691ab7080fd172ad4077862271c2c42052",
      "bytes": 241772
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "6e69c8cd972a77c30b85bc1b0351523b730ae3f0fec9c9a95745ad280c63b850",
      "bytes": 760
    },
    {
      "path": "characters/Hwangbo Eom.md",
      "sha256": "a49c96bf92832c50cfe27c074a086a5c15b2eeb166c94c7e9b17980b7cb9e2a1",
      "bytes": 674
    },
    {
      "path": "characters/Hyeoncheon.md",
      "sha256": "00d462552e67370b327b6c37462c9b4acfeaffa7e8c699f87bda6cbe48d9a2cb",
      "bytes": 651
    },
    {
      "path": "characters/Hyuk Sopyung.md",
      "sha256": "c4d92cf6cc84c7cbc629a17fd879d61a6d3290090bb39ab269d1dea9aac0890f",
      "bytes": 619
    },
    {
      "path": "characters/Jang Sam.md",
      "sha256": "52871a0bd0798177fabaaa629d065ea8fc5725c5189d55e609d5d6c0f191271e",
      "bytes": 508
    },
    {
      "path": "characters/Jeong Hogun.md",
      "sha256": "dfcb591ef2161101c245b3b182dfafd007462d044b6ee455251c9378867d353e",
      "bytes": 700
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "6aab015b19b833b034c92da49e376771f639df0c31dac402c73d3f8440142570",
      "bytes": 1828
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "92cc7be2553dd821ff4cdc2e8f3eb6c04e7541b2b4879ea402a577013a9d3917",
      "bytes": 623
    },
    {
      "path": "characters/Jung Ho.md",
      "sha256": "3747757c39bc3f76c6abbdddffaf228ab800327c285c6ece419fb539d5c16fb8",
      "bytes": 700
    },
    {
      "path": "characters/Ma Junggeol.md",
      "sha256": "4b05dd105c74875c6f879b5ffbc721f7e82e8acfaf8141895e346a70211efbd5",
      "bytes": 673
    },
    {
      "path": "characters/Sama Pyo.md",
      "sha256": "da9b0e2aa665ec6fe17d80101213d3d198683554bb9068053e212e4d4a318adf",
      "bytes": 850
    },
    {
      "path": "characters/Sima Gong.md",
      "sha256": "07fedf0ec0c0c5e80447443741d5f5a694f5c0557f127d4f9d24bfb504246ac3",
      "bytes": 877
    },
    {
      "path": "characters/Song Il.md",
      "sha256": "0cbbff1d06b1a71b19a1de8917cf532377e1bf27b031be9fe83d13a4c9f2572e",
      "bytes": 774
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "5c57876010e2ee43d63e40e88054487436bd19e82b96872d5c4928add2546923",
      "bytes": 686
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "28f788fb31d8efdb4fd177462216606b8fa95eb0fd92e09c8c2b8af3b3d112f9",
      "bytes": 283587
    }
  ],
  "estimated_tokens": 15927
}
-->

# Durable State Update — Chapter 1065

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
1 and safe_through 1065. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1065. Profile updates may replace only one
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
  "chapter": 1065,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1065,
    "continuity_sources": [1065],
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
    "Dark Heaven has occupied Kunlun; the Kunlun Sect and allied forces retreated to Qinghai Lake, with about a thousand killed or wounded.",
    "The messenger report describes Dark Heaven's force as countless, evoking the Hundred Thousand Demonic Disciples.",
    "Qinghai and Gansu remain vulnerable to Dark Heaven.",
    "Jin Taekyung cannot log out while the linked Quest “To Qinghai” is incomplete.",
    "Jin and his companions are entering Qinghai from the Qilian Mountains, guided by Great Sir."
  ],
  "continuity_sources": [
    1063,
    1064
  ],
  "open_questions": [
    "Why does the System prevent Jin from logging out beyond the incomplete linked Quest?"
  ],
  "safe_through": 1064,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 혁소평    | **Hyuk Sopyung**   |
| 송일     | **Song Il**        |
| 사마공    | **Sima Gong**      |
| 장삼 | **Jang Sam** | Bandit; personal name |
| 궁성     | **Bow Saint**                 | —              |
| 태원진가   | **Jin Family of Taiyuan**        |
| 종남파    | **Zhongnan Sect**                |
| 암천     | **Dark Heaven**                  |
| 하북팽가   | **Hebei Peng Family**            |
| 용봉표국   | **Yongbong Escort Bureau**       |
| 십봉룡    | **Ten Dragons and Phoenixes**    |
| 살기     | **killing intent**                               |                                                       |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 후기지수   | **young prodigy** / **rising martial artist**    | Contextual, not a title                               |
| 가주     | **Family Head**                              |
| 문주     | **Sect Leader**                              |
| 소문주    | **Young Sect Leader**                        |
| 장문인    | **Sect Leader**                              |
| 표국     | **Escort Bureau**                            |
| 제자     | **Disciple**                                 |
| 사매     | **Junior Sister**                            |
| 사질     | **Martial Nephew**                           |
| 전각     | **pavilion**                                 | Use “hall” only when established for a specific named building |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 퀘스트              | **Quest**                      |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 감숙     | **Gansu**              |
| 청해     | **Qinghai**            |
| 귀가      | **your family**                                                 |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 도사      | **Daoist**                                                      |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 황보엄 | **Hwangbo Eom** | Personal name of the Taeeul Merciless Sword. |
| 현천진인 | **Perfected Being Hyeoncheon** | Current Sect Leader of Wudang and Hyeongong's Senior Brother. |
| 정호군 | **Jeong Hogun** | Commander of the Embroidered Uniform Guard force confronting Jin. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 정호 | **Jung Ho** | Middle-aged Shaolin martial monk leading the traveling group. |
| 마중걸 | **Ma Junggeol** |
| 사마표 | **Sama Pyo** | Young Sect Leader of the Black Dragon Demon Gate. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 원시천존 | **Primordial Heavenly Venerable** | Daoist deity invoked alongside the Jade Emperor. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 숙부 | **Uncle** | Lee Seowol's shortened address for Cheol Mubaek. |
| 야왕 | **Night King** | Rumored epithet for Jin Taekyung in Taiyuan's red-light district. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 하북 | **Hebei** | Province where Hyuk Family Textile Shop has a branch. |
| 풍운검군 | **Wind-and-Cloud Sword Lord** | Epithet of Gong Iljung, the Zhongnan Sect's Sect Leader. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 노호검객 | **Roaring Fury Swordsman** | Fiery-tempered elder and top-five master of the Zhongnan Sect. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 일각 | **fifteen minutes** | Quarter of a shichen; used for the remaining completion time. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 마공 | **demonic martial arts** | Martial arts that appear to defy common principles. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 천주 | **Lord of Heaven** | Authority invoked by the masked attackers. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 종남일룡 | **Zhongnan One Dragon** | Epithet of Hyuk Sopyung. |
| 태을무정검 | **Taeeul Merciless Sword** | Title of the Zhongnan Sect’s Second Martial Uncle, who is in Xi’an. |
| 황보 | **Hwangbo** | Surname form used when addressing Hwangbo Eom. |
| 청해성 | **Qinghai** | Source form specifying Qinghai as a province. |
| 창룡 | **Azure Dragon** | Divine dragon form invoked in Hyeongong's blessing. |
| 장성 | **Great Wall** | Wall used in the discussion of the Outer Lands. |
| 흑룡마문 | **Black Dragon Demon Gate** | Unorthodox faction from Gansu. |
| 대초자곤 | **two-section staff** | Weapon carried by Sama Pyo's giant subordinate. |
| 소평 | **So Pyeong** | Alliance office worker assigned to prepare a report. |
| 공동파 | **Kongtong Sect** | Sect belonging to the Nine Sects and One Gang. |
| 호거아 | **Tiger Giant Child** | Epithet for Taishan. |
| 흑야왕 | **Black Night King** | Epithet of Sima Gong, Sama Pyo's father and the Sect Leader who built the modern Black Dragon Demon Gate. |
| 화룡각 | **Fire Dragon Pavilion** | New name chosen for Taekyung's pavilion. |
| 화룡각주 | **Fire Dragon Pavilion Master** | Unique Title awarded to Jin Taekyung. |
| 대설산 | **Great Snow Mountain** | Mountain where Baeksang's wartime account reaches its next episode. |
| 금의위 | **Embroidered Uniform Guard** | Imperial guard force mentioned by Hong Jin. |
| 종남 | **Zhongnan Sect** | Orthodox faction that fought in the historic battle. |
| 상산후 | **Marquis of Shangshan** | Title bestowed on Jin Taekyung by the Emperor. |
| 진중 | **Jinzhong** | County included in Taekyung’s fief. |
| 천호 | **Thousand Captain** | Rank held by Jeong Hogun in the Embroidered Uniform Guard. |
| 난주 | **Lanzhou** | Capital of Gansu. |
| 진인 | **Perfected One** | Honorific for the two Kongtong Elders killed at Dunhuang. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 송일 | 진태경 | hostile Zhongnan Elder to accused outsider | you / Jin Taekyung | hostile and threatening | Song Il questions Taekyung's identity and later threatens him over Gong Ilhyuk's injury. |
| 혁소평 | 진태경 | hostile_opponents | you; bastard | hostile and contemptuous | Hyuk insults Taekyung as a beggar and attacks him after Taekyung refuses to defer to his status. |
| 진태경 | 혁소평 | hostile_opponents | you; bastard | insulting and taunting | Taekyung mocks Hyuk’s appearance, cultivation, and failed attack while forcing him to agree to end the dispute. |
| 혁소평 | 황보엄 | junior_disciple_to_senior_martial_uncle | Senior Martial Uncle | formal-deferential but strained | Hyuk Sopyung repeatedly addresses Hwangbo Eom as 사백 while resisting his criticism. |
| 황보엄 | 혁소평 | senior_martial_uncle_to_junior_martial_artist | you; nobody like you | cold and contemptuous | Hwangbo Eom uses 네 녀석 and 네까짓 놈 while reprimanding Hyuk Sopyung. |
| 진태경 | 황보엄 | junior_martial_artist_to_Zhongnan_senior | Great Hero Hwangbo | casual-polite and teasing | Taekyung uses 황보 대협 after deliberately pretending not to recognize Hwangbo. |
| 황보엄 | 진태경 | Zhongnan_senior_to_younger_martial_artist | insolent brat | blunt, amused, and probing | Hwangbo describes Taekyung as a 건방진 아해 and later treats him as a youngster. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 가솔 | 진태경 | Zhuge Clan retainer to Great Hero | Great Hero Jin | polite and pleading | Uses 진 대협 while urging Taekyung to stop provoking Ju Wongong. |
| 사마표 | 정호 | Black Dragon Demon Gate Young Sect Leader addressing a Shaolin Master | Master Jung Ho | Polite and ingratiating | Uses 정호대사 and 대사 while flattering Jung Ho and negotiating responsibility for the killing. |
| 정호 | 사마표 | Shaolin martial monk addressing the Black Dragon Demon Gate Young Sect Leader | Benefactor | Formal and admonitory | Uses 시주 while questioning Sama Pyo and demanding accountability. |
| 거한 | 사마표 | Subordinate addressing the Black Dragon Demon Gate Young Sect Leader | Young Sect Leader | Crude and deferential | Uses 소문주 in short, childlike replies. |
| 사마표 | 거한 | Young Sect Leader addressing his giant subordinate | This fellow | Informal and patronizing | Refers to him as 이 녀석 while assigning him responsibility for Do Sangho's death. |
| 정호 | 진태경 | Shaolin Discipline Hall Master to patient and Benefactor | Benefactor Jin | formal-polite | Jung Ho repeatedly uses 진 시주 and 시주. |
| 진태경 | 정호 | patient to Shaolin Discipline Hall Master | Monk | polite and familiar | Taekyung addresses Jung Ho as 스님. |
| 사마표 | 태산 | Young Sect Leader to subordinate | Taishan | informal and patronizing | Sama Pyo calls Taishan by name while ordering him to leave. |
| 태산 | 사마표 | subordinate to Young Sect Leader | Lord | crude and deferential | Taishan uses 주군 while obeying Sama Pyo. |
| 태산 | 진태경 | subordinate_to_respected_outsider | Jin Taekyung | clipped and familiar | Taishan says he likes Jin Taekyung but will fight him without hesitation if Sama Pyo commands it. |
| 사마표 | 진태경 | prospective recruit to pavilion master | you | polite, controlled, and candid | Sama Pyo uses 자네 while asking about Taekyung's attitude and admitting his intention to use him. |
| 진태경 | 사마표 | pavilion master to prospective recruit | you / that guy | blunt, informal, and distrustful | Taekyung speaks to and about Sama Pyo with casual forms such as 녀석 and 저놈. |
| 아빠 | 진태경 | father to son | Taekyung | affectionate informal | Addresses his young son warmly as Taekyung. |
| 진태경 | 아빠 | son to father | Dad | childlike informal | Taekyung addresses his father as Dad in the childhood flashback. |
| 진태경 | 태산 | pavilion_master_to_pavilion_member | Taishan | forceful and commanding | Taekyung orders Taishan to stop eating the bear. |
| 사마표 | 각주 | Fire Dragon Pavilion member to pavilion master | Pavilion Master | formal but sardonic | Sama Pyo addresses Jin as 각주 while questioning his account of the incident. |
| 태산 | 각주 | Fire Dragon Pavilion member to pavilion master | Pavilion Master | clipped, childlike, and informal | Taishan directly asks Jin whether his Lord Sama Pyo is safe. |
| 진태경 | 정호군 | young martial artist to senior imperial officer | Commander Jeong | casual and teasing, then conciliatory | Jin addresses him by rank while trying to defuse the standoff. |
| 정호군 | 태산 | guard officer questioning a performer | you | blunt and direct | He calls Taishan forward and asks whether he belongs to the circus troupe. |
| 신의 | 태산 | senior physician to younger ally | Young Hero Taishan | urgent and respectful | The Divine Physician uses this address while pleading with Taishan to keep moving. |
| 궁성 | 진태경 | elder who spent decades searching for the chosen one | you | casual and teasing | Uses 너/널 while testing and praising Taekyung. |
| 진태경 | 궁성 | chosen one addressing the elder who sought him | you | polite, shifting to familiar-casual under stress | Begins with formal-polite phrasing, then speaks more casually as the conversation intensifies. |
| 정호군 | 진태경 | imperial officer responding to the Marquis of Shangshan | Marquis of Shangshan | formal and deferential | Accepts the command with a formal acknowledgment of Taekyung’s title. |
| 진태경 | 사마공 | allied young martial artist to unorthodox sect leader | Great Hero Sima | polite and deferential | Addresses him as 사마 대협. |
| 사마공 | 진태경 | unorthodox sect leader to celebrated young martial artist | you | polite and familiar | Uses 자네 while speaking to Taekyung. |
| 진태경 | 마중걸 | Murim Alliance member to visiting horse-caravan chief | Junggeol | casual | Initially addresses him familiarly, then apologizes and shifts to polite speech. |
| 마중걸 | 진태경 | visiting horse-caravan chief to young Murim Alliance member | young man | polite and deferential | Initially calls him a pretty little gigolo as an insult, then uses a respectful address. |
| 마중걸 | 사마공 | visiting group leader to sect leader | Sect Leader Sima | polite and respectful | Addresses him as 사마 문주 while explaining Ningxia and Baekma Bang. |
| 사마공 | 마중걸 | sect leader to visiting group leader | you | formal and probing | Uses 자네 while questioning Ma Junggeol about following Dark Heaven. |
| 사마공 | 사마표 | father to son | Pyo | intimate and familiar | Sima Gong calls him 표야 and 내 아들아. |
| 풍운검군 | 노호검객 | Zhongnan Sect Leader to Senior Brother | Senior Brother | respectful and strained | Addresses him as 사형 while protesting the decision. |
| 풍운검군 | 태을무정검 | Zhongnan Sect Leader to Senior Brother | Senior Brother | respectful and strained | Addresses him as 사형 while protesting the decision. |
| 풍운검군 | 진태경 | martial artist to fellow martial artist | Daoist Friend Jin | respectful and familiar | Thinks of Jin as 진 도우 when recognizing him as a possible turning point in the battle. |
| 사마표 | 사마공 | son to father | you; Father | familiar and confrontational | Sama Pyo challenges his father during their battlefield confrontation. |
| 노호검객 | 풍운검군 | Senior Brother to Zhongnan Sect Leader and Junior Brother | Junior Brother, Sect Leader | blunt and commanding | Uses 장문 사제 while ordering him to give the retreat command. |
| 태을무정검 | 풍운검군 | Senior Brother to Zhongnan Sect Leader and Junior Brother | Junior Brother, Sect Leader | serious and restrained | Uses 장문 사제 while telling him the sect’s losses will worsen if the battle continues. |
| 송일 | 황보엄 | Senior Brother to Junior Brother | Junior Brother | familiar and heated | Song Il calls Hwangbo Eom 사제. |
| 황보엄 | 송일 | Junior Brother to Senior Brother | Senior Brother | familiar and dryly teasing | Hwangbo Eom calls Song Il 대사형. |
| 현천진인 | 사마표 | Kongtong Sect Leader confronting the son of a man he believes betrayed the survivors | Sama family boy | formal, then cold and severe | Initially addresses him as 도우, then shifts to 사마가의 아해야 before demanding that he bring his father. |
| 진태경 | 대인 | young martial artist to benefactor | you | casual and blunt | Taekyung asks who Great Sir is, addressing him as 당신. |
| 대인 | 진태경 | older benefactor to young martial artist | you | familiar conversational | Great Sir addresses Taekyung as 자네. |
| 진태경 | 현천진인 | young martial artist addressing a senior Daoist Sect Leader | Perfected Being | polite | Jin responds respectfully to Hyeoncheon's assessment of the retreat. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1063
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Hwangbo Eom.md

# Hwangbo Eom (황보엄)

- **Safe through:** Chapter 1058
- **Aliases:** Taeeul Merciless Sword
- **Role:** Supreme Peak master of the Zhongnan Sect and its Second Martial Uncle, known as the Taeeul Merciless Sword.
- **Personality:** Ruthless, severe, proud, and deeply invested in restoring Zhongnan's standing.
- **Voice:** Calmly courteous when offering tea, then cold, commanding, and cutting when reprimanding others.
- **Relationships:** Song Il and Hwangbo Eom are Gong Iljung’s two Senior Brothers; the three served the same Master for over fifty years, and Hyuk Sopyung is Hwangbo’s junior.

### Hyeoncheon.md

# Perfected Being Hyeoncheon (현천진인)

- **Safe through:** Chapter 1064
- **Aliases:** None
- **Role:** Perfected Being Hyeoncheon is the current Sect Leader of the Kongtong Sect, a veteran Daoist master, and a Supreme Peak martial artist.
- **Personality:** Grave and reflective, he bears the losses of the Great Faction War yet rejects punishing the innocent for their relatives’ crimes.
- **Voice:** Measured, solemn, and calm with the authority of a Sect Leader.
- **Relationships:** Hyeongong is his Junior Brother, and both studied under the same master from childhood.

### Hyuk Sopyung.md

# Hyuk Sopyung (혁소평)

- **Safe through:** Chapter 1046
- **Aliases:** Zhongnan One Dragon
- **Role:** Peak master of the Zhongnan Sect known as the Zhongnan One Dragon and a senior disciple who can command the Taeeul Sword Unit in Hwangbo Eom's presence.
- **Personality:** Proud, volatile, entitled, and quick to anger, especially when drunk.
- **Voice:** Loud, confrontational, insulting, and imperious.
- **Relationships:** Baek Museong knows him from several prior encounters; Baek says their elders' connection has been passed down to them.

### Jang Sam.md

# Jang Sam (장삼)

- **Safe through:** Chapter 990
- **Aliases:** Killing Ghost
- **Role:** Jang Sam is a bandit chief who abruptly rose from Level 40 to Level 60 and attacked Taekyung while apparently irrational; he is currently unconscious and being taken to the Nangong Family.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** No relationships established.

### Jeong Hogun.md

# Jeong Hogun (정호군)

- **Safe through:** Chapter 1046
- **Aliases:** None
- **Role:** Jeong Hogun is a Thousand Captain of the Embroidered Uniform Guard and a highly skilled martial artist whose force includes dozens of Peak masters.
- **Personality:** Disciplined and resolute, he follows imperial orders without hesitation and reads the political consequences of events with care.
- **Voice:** Formal and rigid, emphasizing duty to imperial authority.
- **Relationships:** Jeong Hogun serves under Baek Yeon’s command in the Embroidered Uniform Guard and honors Jin Taekyung as a comrade-in-arms after their shared battle.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1064
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan and the original owner of his current body, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master who has reached the realm of the Ten Kings as its eleventh member and can detect and eavesdrop on nearby Sound Transmissions subject to the participants’ relative levels, and a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure, willing to risk himself for others, and fiercely defiant when others try to dictate his choices or survival.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; Hyuk Mujin trusts Taekyung to fight beside him; Taekyung trusts Sama Pyo as a friend despite suspecting his betrayal, and values him beyond his unorthodox affiliation; Peng Cheolhu regarded Taekyung as a worthy successor, and the Bow Saint relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1064
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Jung Ho.md

# Jung Ho (정호)

- **Safe through:** Chapter 1046
- **Aliases:** None
- **Role:** Middle-aged Shaolin martial monk and Master of Shaolin's Discipline Hall who leads the traveling group and wields a Zen staff hung with prayer beads.
- **Personality:** Humble, observant, principled, and concerned with the safety of commoners.
- **Voice:** Formal, restrained, and admonitory, with Buddhist phrasing.
- **Relationships:** Unnamed is his young Martial Uncle; he leads the Shaolin monks traveling with him, addresses Sama Pyo as a Benefactor, and is recognized by Jin Taekyung as Park Jung Ho, a former Garam Middle School classmate.

### Ma Junggeol.md

# Ma Junggeol (마중걸)

- **Safe through:** Chapter 1061
- **Aliases:** Chief of Baekma Bang
- **Role:** Ma Junggeol is the chief of Baekma Bang, a horse-caravan group founded by reformed Ningxia mounted-bandit leaders.
- **Personality:** Though timid by nature, he is earnest and protective of his sworn brothers, loyal to the benefactor who helped them reform, and willing to bear personal risk for their mission.
- **Voice:** Not established
- **Relationships:** He leads six sworn brothers who, with him, are known as the Seven Masters of Baekma Bang, and trusts the benefactor they call the Lord.

### Sama Pyo.md

# Sama Pyo (사마표)

- **Safe through:** Chapter 1059
- **Aliases:** Black Dragon Saber
- **Role:** Young Sect Leader and heir of the Black Dragon Demon Gate, a Morning Star reputed to be no less than the Ten Dragons and Phoenixes.
- **Personality:** Courteous and calculating, he chooses what he believes is right over expedience and accepts responsibility for his choices, even when they expose him to blame.
- **Voice:** Polite and ingratiating in public, with sardonic humor and controlled evasiveness.
- **Relationships:** Sama Pyo is Sima Gong’s son and chosen heir, commands Taishan, and is Jin Taekyung’s friend; he deliberately let Namho suspect his father’s actions to protect their companions, was Ju Hwaran’s former fiancé, and is hostile toward Song Ilseom.

### Sima Gong.md

# Sima Gong (사마공)

- **Safe through:** Chapter 1058
- **Aliases:** Black Night King
- **Role:** Sima Gong is the Sect Leader who built the Black Dragon Demon Gate into a major unorthodox power and the father of its Young Sect Leader, Sama Pyo.
- **Personality:** Sly and calculating yet capable of risking himself for a moment of conscience, he values his heir’s future and repaying a debt to Jeok Cheongang.
- **Voice:** Polished and persuasive, with smooth rhetorical turns and a composed, gently teasing manner.
- **Relationships:** Sama Pyo is his youngest son among seven older brothers and nine older sisters; Sima Gong chose him as heir and approved his plan to answer the Gate’s betrayal. Sama Pyo returned to remain with him as he died. Sima Gong aided Jeok Cheongang despite their history.

### Song Il.md

# Song Il (송일)

- **Safe through:** Chapter 1058
- **Aliases:** Roaring Fury Swordsman
- **Role:** Elder of the Zhongnan Sect, known as the Roaring Fury Swordsman and one of Sect Leader Gong Iljung’s two Senior Brothers.
- **Personality:** Arrogant and domineering, but capable of remorse over choices that harmed his sect and those he failed to protect.
- **Voice:** Gruff, cutting, condescending, and threatening, with formal authority used to pressure those beneath him.
- **Relationships:** Gong Iljung is his junior Sect Leader and martial younger brother; Gong Ilhyuk is a junior Disciple of his sect; he recognizes Baek Museong and Cheongpung through their Huashan and Sword Saint connections.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 1059
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo; becomes explosively violent when his meat is threatened.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord, trusts Jin Taekyung as Pavilion Master, and has grown attached to the Fire Dragon Pavilion members.

## Korean source

```text
1065화




전투에서의 패배는 곧 끝장을 의미한다.

수만 명이 정면으로 맞붙어 싸우는 대규모 회전(會戰)의 경우에는 특히나 그렇다.

가까스로 살아남은 패자들의 앞에 놓인 운명은 단 두 가지다.

포로가 되거나, 세상 끝까지 도망치거나.

이는 선택할 수도, 거부할 수도 없다.

하지만 승자는 다르다.

그렇기에 지금으로부터 사흘 전, 대설산(大雪山)을 둘러싼 혈전이 아군의 대승으로 막을 내린 직후 우리에게는 새로운 선택지가 주어졌다.

전투의 여파를 수습한 뒤 계속해서 감숙성을 지킬 것인가.

아니면 또 다른 어딘가에서 밀려들고 있을 암천의 군세를 막기 위해 이동할 것인가.

그리고 우리의 선택은 후자(後者)였다.

아니, 내 의사를 모두가 존중해 주었다는 것이 더 정확한 표현이었다.

‘저는 이만 떠나겠습니다. 해야 할 일이 있어요.’

설원(雪原)이 불길과 연기로 뒤덮인 날이었다.

수만여 구의 시신을 집어삼킨 화염은 영원히 꺼지지 않을 것처럼 타오르는 중이었고, 내가 불현듯 던진 한마디는 그 광경을 지켜보며 하염없이 눈물을 흘리던 이들에게 너무나도 가혹하게 느껴졌을 것이다.

하지만 온전히 슬픔에 잠길 시간조차 빼앗겼음에도, 그들은 나를 비난하지 않았다.

단 한 사람도.

다만 공동파의 장문인인 현천진인만이 앞으로 나서 짧은 물음을 던졌을 뿐이었다.

‘어디로 갈 생각인가?’

내 대답은 처음부터 정해져 있었다.

시스템은 이미 퀘스트라는 나침반으로 다음 행선지를 명확하게 가리키고 있었으니까.

‘청해(靑海). 청해입니다.’

‘그렇다는 건.’

‘예. 놈들이 오고 있습니다.’

이해할 수 없을 정도의 확신이 담긴 내 음성에도, 현천진인은 이유를 묻지 않았다.

다만 무거운 얼굴로 고개를 끄덕였을 뿐이었다.

‘다시 한번 세상이 피로 물들겠군.’

‘그럴 겁니다. 분명히.’

‘그곳에서도 놈들을 상대로 대승을 거둔다면, 이 저주받은 전쟁을 종식시킬 수 있으리라 생각하나?’

‘한 걸음 더 가까워질 겁니다. 그리고 이번에 내디딜 걸음은, 그 어느 때보다 크고 깊겠죠.’

‘천주(天主)에게 닿을 만큼?’

‘그러리라 믿습니다.’

‘그렇다면 우리 공동파 또한 자네와 함께하겠네.’

‘……!’

‘끝에 다다르기 전까지는 결코 멈추지 않겠네. 지금쯤 저 구름 위에서 원시천존(號出天等)의 보살핌을 받고 있을 넋들을 위해서라도.’

만약 현천진인이 살아남은 암천의 교도들을 도살할 때와 같은 살기를 흘리고 있었다면, 나는 그의 합류를 거절했을 것이다.

하지만 이미 많은 것을 잃어버린 노도사(老道士)의 눈동자는 더없이 맑았으며, 이는 한바탕 분노와 슬픔을 쏟아낸 공동파의 제자들 또한 마찬가지였다.

‘좋습니다.’

그렇게 현천진인을 비롯한 일백여 명의 공동파 제자들이 합류하게 되었지만, 이는 단지 시작에 불과했다.

‘무림말학 혁소평. 감히 이 자리를 빌어 사문의 죄를 청하고자 합니다.’

종남일룡(終南一龍) 혁소평.

더불어 혈전 속에서 가까스로 목숨을 부지한 삼백여 명의 종남파 제자들은 병장기를 내려놓고 무릎을 꿇었다.

노호검객 송일과 태을무정검 황보엄.

이제는 죽고 없는 사문의 두 어른이 지은 죄를 알게 된 그들의 낯빛은 부끄러움과 슬픔으로 가득했고, 온 힘을 다해 악문 잇새 사이로는 핏줄기가 흘렀다.

만일 종남파의 장문인인 풍운검군(風雲劍君)이 극심한 부상으로 의식불명의 상태에 빠지지만 않았더라면, 그 또한 제자들과 함께 무릎을 꿇고 죄를 청했을 것이다.

그리고 그런 종남파의 제자들을 한참이나 말없이 응시하던 현천진인은 이렇게 말했다.

‘아비의 죄가 자식의 것이 아니듯, 스승의 죄 역시 제자의 몫이 아닌 법. 한데 종남의 제자들은 어찌하여 빈도에게 죗값을 청하는가.’

‘……!’

‘그럼에도 죗값을 달게 받고자 한다면, 좋다. 여기 있는 진 도우(道友)를 따라 올곧고 밝은 방향으로 나아가거라. 그것이 종남파의 새로운 길이 될 것이니.’

현명하고 자애로운 노도사의 말에, 혁소평과 종남파의 제자들은 크게 절을 올린 뒤 내게 지극한 예를 갖추어 포권지례를 취했다.

‘한 치의 어긋남도 없는 정도(正道)를 걷고자 하는바, 진 대협께 합류를 청합니다.’

용봉표국의 사건 이후 처음으로 맞대면하게 된 혁소평이었다.

종남파 제일의 후기지수로서 십봉룡(十鳳龍)의 한 자리를 차지하고 있던 녀석과 나 사이에 놓인 간극은 그때보다도 아득하게 벌어져 있었다.

따라서 종남파와 여러 날을 함께 하며 감숙에서 시간을 보내는 와중에도 멀리서만 스쳐 지나갈 수밖에 없었다.

아마도 그래서였을 것이다.

혁소평의 기세와 눈빛이, 마지막에 보았던 것과는 비교도 할 수 없을 만큼 진중하고 깊어졌다는 사실을 그제야 깨달은 것은.

‘그 제안, 기꺼이 받아들이겠습니다.’

나는 모처럼 예의를 갖추어 종남파의 합류를 승낙했고, 두 문파의 합류로 순식간에 오백여 명까지 불어난 상황을 지켜보던 한 사람이 다가왔다.

‘이 정도로도 부족할 텐데. 안 그런가?’

‘글쎄. 어중이떠중이들로 머릿수를 채우는 것보단 훨씬 낫겠지.’

‘어째서인지 귀가 간지러운데. 기분 탓이겠지?’

‘아닐 수도 있고.’

짐짓 딴청을 피우는 내 모습에 실소를 흘린 흑룡마문(黑龍魔門)의 신임 문주는, 오와 열을 맞춰 도열한 자신의 새로운 수하들을 가리켰다.

‘오백. 시간이 촉박했지만 자원한 이들 중에서도 철저하게 가려 뽑았네. 비록 구파일방의 제자들에게는 미치지 못하더라도 충성심과 투지만큼은 보장하지.’

‘그래서, 내게 맡기겠다?’

‘아니. 데려가도록 허락해 주면 고맙겠군.’

‘뭐?’

‘흑룡마문주 사마표 이하 오백 인. 화룡각주(火龍閣主)께 합류를 청합니다. 부디 지난날의 과오를 조금이나마 씻고 천하를 위해 싸우도록 허락해 주십시오.’

‘……!’

순간, 나는 잠시 말문이 막혔다.

만약 그때 자그마한 노인을 목에 대롱대롱 매단 거한이 이렇게 외치지 않았다면, 울컥하는 마음을 쉽게 억누르지 못했을 정도로.

‘태산이! 태산이도 간다! 각주랑 끝까지 간다!’

‘이런 염병할! 살살 좀 뛰라고! 제발!’

모두가 약속이라도 한 것처럼 동시에 웃음을 터트렸다.

나와 사마표, 화룡각 대원들과 구파일방의 생존자들.

그리고 기쁠 때나 슬플 때나 늘 무미건조한 표정을 짓고 있던 금의위 천호 정호군까지도.

‘제법 재미있는 족속들이군. 그대와 같은 무림인들은.’

‘그래? 기왕 말 나온 김에 더 재미있는 얘기 해 줄까?’

‘더 재미있는 얘기?’

‘응. 하늘 같은 열후한테 반말 찍찍해 대다가 강제 전역당할 위기에 처한 어느 금의위 천호에 대한 이야긴데. 놀랍게도 얘랑 너랑 성씨가 같네. 신기한 우연이지?’

‘……이렇게 나올 건가?’

‘그러니까 잘해 봐. 이렇게 나오지 않도록.’

정호군은 못 당하겠다는 듯이 고개를 절레절레 내저었고, 이내 철탑 같은 자세로 내게 군례(軍禮)를 취했다.

‘그렇다면 부디 명령을.’

‘청해. 청해성으로 간다. 전속력을 다해서.’

‘신, 금의위 천호 정호군. 지엄하신 상산후의 명을 받듭니다.’

그리하여 지금으로부터 이틀 전.

마지막 한 조각이었던 금의위까지 합류하며 이천여 명에 가까워진 병력은, 짧은 휴식을 뒤로한 채 곧장 청해성으로 향했다.

물론 그 과정에서 몇몇 이들은 암천이 다시 한번 감숙성을 노릴지도 모른다는 신중론을 제기하기도 했지만, 궁성은 짤막한 한 마디로 모든 우려를 종식시켰다.

‘북부가 움직이고 있다.’

당연하게도 이는 단순히 감숙성 북부를 말하는 것이 아니었다.

장성으로 구분된 천하 전체에서의 북부. 아울러 그 드넓은 땅을 지배하는 두 패자(霸者)를 뜻함이었다.

하북의 맹호, 하북팽가.

더불어 푸르른 초원의 하늘마저 손에 넣게 된 산서성의 창룡(蒼龍), 태원진가.

‘화살마다 쏘아지는 속도는 다를지라도, 방향만 흔들리지 않으면 결국은 표적에 닿는 법이지.’

예컨대 궁성과 금의위는 먼저 쏘아진 화살이었다.

실로 궁성다운 비유였고, 그 후로는 누구도 감히 반박하지 못했다.

비단 그 말을 한 이가 궁성이기 때문만은 아니었다.

북부의 창룡과 맹호가 날개를 펴고, 발톱을 드러낸 이상 감숙성의 안전은 어느 정도 보장된 것이라는 사실을 모두가 알고 있었으니까.

그리고 감숙성을 떠나기 직전 벌어진 짧은 숙청(肅淸)의 시간은, 혹시 모를 후환을 송두리째 제거하기에 충분했다.

‘마지막으로 남길 말이 있나? 변명은 됐고, 유언이라면 들어주지.’

‘나, 나는 암천과 결탁하지 않았소. 뭔가 오해가 있었던 것이 분명하오!’

‘소문주, 아니 문주! 도대체 왜 이러는 거요. 작고하신 선친(先親)과 내가 의형제나 다름없는 각별한 사이라는 걸 알지 않소!’

‘그래, 알지. 배신도 함께할 정도였으니까. 어찌나 각별한 사이였는지 아버지께서 전부 세세하게 기록도 해 두셨던데…… 알고 있었나?’

‘……!’

감숙 무림의 미래를 결정짓는 중차대한 회의에서, 배신자들을 추궁하는 재판장으로 변해 버린 공간이 삽시간에 얼어붙었다.

부릅뜬 눈. 파르르 떨리는 입꼬리.

그런 그들의 모습에 작게 한숨을 내쉰 사마표가 품에서 낡은 서책 한 권을 꺼내 탁자에 올려 두었다.

‘역시 몰랐던 모양이군. 의심 정도는 해 볼 법도 했을 텐데.’

그 철두철미한 흑야왕 사마공이 이토록 확실한 증거를 남겼다는 것에 대해 나조차도 뜻밖이라고 생각했으니, 수십여 년간 생전의 그를 알아 왔던 저들이야 오죽했을까.

하지만 사마표는 아랑곳하지 않고 말을 이어 갔다.

아버지에 대한 일말의 씁쓸함이 담긴 음성과 벌레들을 바라보는 듯한 눈빛으로.

‘그래서, 유언은?’

그것이 결정타였다.

‘이, 이런 대가리에 피도 안 마른 애새끼 따위가! 이놈! 의숙부나 다름없는 나를 죽일 셈이냐!’

‘허. 허허. 결국, 결국 이리 되었는가.’

궁지에 몰린 쥐새끼가 선택할 수 있는 길은 두 가지뿐이었다.

그 앙증맞은 앞니라도 무기 삼아 달려들거나. 혹은 모든 것을 체념하고 운명을 받아들이거나.

그리고 어리석게도 전자를 택한 이들을 기다리고 있던 것은.

‘이야기 끝났다. 태산아.’

‘흐아암. 태산이. 듣다가 깜빡 잠들 뻔했다.’

커리어 통산 타율 9할 9푼 9리에 빛나는, 감숙성 블랙 드래곤즈의 지명타자 호거아(虎巨兒) 태산이었다.

뻑!　뻐어억!

혹시 모를 상황을 대비하여 함께 자리하고 있던 내가 나설 필요조차 없었다.

태산의 대초자곤이 신명 나게 불을, 아니 피를 뿜었으니까.

앞서 사마표를 향해 대가리에 피도 안 마른 애새끼라고 외치며 달려들었던 흑룡마문의 중진은 피를 담을 머리통 자체가 사라졌고, 온 힘을 다해 도주를 감행한 여러 문주와 가주들은 전각을 나서자마자 포위당했다.

새로운 주군에게 충성을 맹세한 흑룡마문의 무사들.

그리고 다름 아닌 자신의 수하와 제자들에게.

‘가, 강평! 네놈이 어찌 내게 이럴 수 있느냐!’

‘그러는 장문인께서는 어찌 그러실 수 있습니까?’

‘길을 지켜라! 어서! 아니, 아니지. 장문령이다! 지금 당장 저놈들을 막…….’

‘그 더러운 아가리 닥쳐.’

‘뭐라?’

‘네놈 때문에 내 스승님이, 사매가, 사질이 죽었다! 이는 곧 기사멸조(欺師滅祖)의 대죄이니, 고랑검문의 제자들은 지엄한 문규에 따라 장문인을 즉결 처단하라!’

‘난주혁가(蘭州奕家)의 가솔들은 무엇하는가!’

‘부디 원망하지 마시오. 가주. 먼저 배신한 것은 우리가 아닌 당신이니.’

‘이, 이놈들이 감히……!’

서걱, 푸푸푹!

사방에서 쏟아지는 수많은 창칼에, 십여 명에 달하는 문주와 가주들은 제대로 된 유언조차 남기지 못한 채 부릅뜬 눈으로 죽음을 맞이했다.

그들 개개인이 감숙 무림을 이끄는 영수(領袖)들이자, 상당한 숫자의 문도들을 거느린 일파의 주인이라는 사실을 생각한다면 너무나도 비참한 최후.

그러나 흑룡마문의 젊은 문주는 도합 스물에 달하는 명숙들을 쳐 죽이거나 사로잡는 와중에도 눈 하나 깜짝하지 않았다.

다만 그 모든 광경을 침착하고 냉정한 눈빛으로 지켜보다, 어느새 차갑게 식은 찻잔을 어루만지며 불쑥 입을 열었다.

‘새로 내오라고 할까?’

‘아니. 맛없어. 시간도 없고. 게다가 곧 정신없는 인간도 합류할 테니까 속만 쓰려.’

‘대인, 그자가 정말 청해성으로 가는 가장 빠른 길을 알고 있다던가?’

‘정확히는 마중걸이 알려 줬지. 소싯적에 뭐 하는 인간이었는지는 몰라도 지리에 아주 빠삭하다던데.’

‘그렇군. 그럼 볼일도 끝마쳤으니 나도 각주와 함께 가도록 하지.’

고개를 끄덕인 사마표는 자리에서 일어났다. 

일각 전만 하더라도 스무 명이 넘는 얼굴들로 채워져 있던 탁자는 이제 텅 비어 있었고, 그 위에는 이리저리 엎어진 찻잔들과 낡은 서책 한 권만이 덩그러니 놓여 있었다.

‘안 가져가?’

‘이제는 필요 없는 물건이니까.’

그 한 마디를 남긴 채 사마표는 자리를 떠났고, 잠시 고민하던 나는 서책을 챙겼다.

비록 쓸모를 다하고 버려진 물건이지만, 그래도 이 낡아빠진 서책 역시 녀석의 죽은 아버지가 남긴 흔적 중 하나일 테니까.

그리고 씁쓸하게 입맛을 다시며 별생각 없이 서책의 첫 장을 넘긴 순간, 앞서 사마표가 했던 말의 진정한 의미를 깨달을 수 있었다.

‘……허.’

실소를 흘린 나는 서책을 내려놓았다.

아니.

글자 하나조차 적히지 않은 채, 제 쓰임새를 다하지 못하고 오랜 세월 동안 어딘가에 처박혀 있었던 것이 분명한 싯누런 종이 묶음을.

‘피는 못 속이네. 좋은 의미로.’

작게 중얼거린 나는 배신자들의 몸뚱어리에서 흘러나오는 피비린내를 맡으며 걸음을 옮겼다.

그리고 그날로부터 이틀이 지나고, 욕이 나올 만큼 험한 산자락을 타고 이동하며 또다시 사흘이 흘렀을 때.

“거기. 젊은 친구. 자네 이름이 뭔가?”

“진태경이요. 스물네 번째 말씀드리는 건 아시죠?”

“아, 그래. 장삼이.”

“도대체 진태경이 왜 장삼…… 후, 됐습니다. 그런데 왜요?”

“아니, 사실 뭐 크게 중요한 얘기는 아닌데.”

“그래도 말씀해 보세요. 지금처럼 존댓말 써 드릴 때.”

“별건 아니고, 당최 여기가 어딘가?”

“예? 뭐요?”

“여기가 어디냐고.”

“이런 씹.”

미친 소리를 태연하게 지껄이는 저 미친 길잡이 놈을 죽이고 싶다는 충동에 사로잡혔다.

이성의 끈이 버티지 못할 만큼 아주 강렬하고도 진한 충동에.

저벅.

그러나 도저히 참지 못하고 육체의 대화를 시도하기 위해 대인에게 다가간 그 순간.

띠링.



- [청해성]에 진입했습니다.



잠시 끊어졌던 이성의 끈을 접착시켜주는, 맑은 종소리가 귓가에 울려 퍼졌다.
```

## Final English reading copy

```markdown
# Chapter 1065

Losing a battle meant the end.

That was especially true in a large-scale engagement, where tens of thousands of men clashed head-on.

The defeated survivors had only two possible fates:

Become prisoners, or run to the ends of the earth.

They had no say in which fate awaited them, and no way to refuse it.

But the victors were different.

So, three days ago, just after the bloody battle around the Great Snow Mountain ended in a crushing victory for our side, we were given a new choice.

Would we stay to protect Gansu Province after dealing with the aftermath of the battle?

Or would we move out to stop the Dark Heaven forces advancing somewhere else?

We chose the latter.

No—more accurately, everyone respected my wishes.

“I’ll be leaving now. There’s something I have to do.”

The snowfield was covered in flames and smoke that day.

The fire, consuming tens of thousands of corpses, burned as if it would never go out. And my sudden announcement must have felt unbearably cruel to those watching the scene, their tears falling without end.

Even though they’d been robbed of any chance to grieve in peace, they didn’t blame me.

Not a single person.

Only Perfected Being Hyeoncheon, the Sect Leader of the Kongtong Sect, stepped forward to ask a brief question.

“Where do you intend to go?”

I’d known my answer from the start.

The System had already pointed the way to our next destination with a Quest as clear as a compass.

“Qinghai. Qinghai.”

“Which means…”

“Yes. They’re coming.”

Even though I spoke with a certainty that made no sense, Perfected Being Hyeoncheon didn’t ask why.

He only nodded, his face heavy.

“The world will be stained with blood once more.”

“It will. Without a doubt.”

“If we win a great victory against them there as well, do you think we can bring this accursed war to an end?”

“We’ll be one step closer. And the step we take this time will be bigger and deeper than any before it.”

“Big enough to reach the Lord of Heaven?”

“I believe so.”

“Then the Kongtong Sect will stand with you.”

“……!”

“We won’t stop until we reach the end. If only for the sake of the souls who, by now, must be under the care of the Primordial Heavenly Venerable beyond those clouds.”

If Perfected Being Hyeoncheon had been leaking the same killing intent he’d shown while slaughtering the Dark Heaven followers who’d survived, I would have refused his offer.

But the eyes of the old Daoist, who had already lost so much, were clear. The same was true of the Kongtong Disciples, who had let out all their anger and grief.

“Good.”

And so, Perfected Being Hyeoncheon and about a hundred Kongtong Disciples joined us. But that was only the beginning.

“I, Hyuk Sopyung, an unworthy martial artist, humbly ask to answer for my sect’s sins.”

Hyuk Sopyung, the Zhongnan One Dragon.

Along with him, more than three hundred Zhongnan Sect Disciples who had barely survived the bloody battle set down their weapons and knelt.

The Roaring Fury Swordsman, Song Il, and the Taeeul Merciless Sword, Hwangbo Eom.

The faces of those Disciples who had learned of the sins committed by the two elders of their sect—now both dead—were full of shame and grief. Blood trickled between their clenched teeth.

If the Wind-and-Cloud Sword Lord, the Zhongnan Sect Leader, hadn’t been unconscious with severe injuries, he would have knelt with his Disciples and asked to answer for their sins, too.

Perfected Being Hyeoncheon watched the Zhongnan Disciples in silence for a long while, then spoke.

“A father’s sins do not belong to his children. A master’s sins do not belong to his Disciples. So why do Zhongnan’s Disciples ask me to punish them?”

“……!”

“Still, if you wish to accept your punishment, so be it. Follow Great Hero Jin here and walk a straight and righteous path. That will be the new way of the Zhongnan Sect.”

At the wise, kind old Daoist’s words, Hyuk Sopyung and the Zhongnan Disciples bowed deeply, then saluted me with the utmost respect.

“We wish to walk the righteous path without the slightest deviation. We ask to join you, Great Hero Jin.”

This was the first time I’d come face-to-face with Hyuk Sopyung since the incident at the Yongbong Escort Bureau.

He had once been the Zhongnan Sect’s most promising young prodigy, one of the Ten Dragons and Phoenixes. The gap between us had grown even wider than before.

So, while I spent several days with the Zhongnan Sect in Gansu, I could only pass him at a distance.

Maybe that was why I only then realized how much more serious and profound his aura and gaze had become compared with the last time I’d seen him.

“I gladly accept your offer.”

I accepted the Zhongnan Sect’s offer with a rare show of courtesy. As I watched our numbers swell to more than five hundred with the two sects’ arrival, someone came over.

“This still won’t be enough. Don’t you think?”

“Who knows? It’s a lot better than padding the numbers with any old riffraff.”

“Why do my ears itch? Must be my imagination.”

“Maybe not.”

The new Sect Leader of the Black Dragon Demon Gate chuckled at my deliberate air of innocence, then pointed to his new followers, lined up in perfect ranks.

“Five hundred. We were short on time, but I thoroughly vetted the volunteers. They may not measure up to the Nine Sects and One Gang’s Disciples, but I can guarantee their loyalty and fighting spirit.”

“So you’re putting them under my command?”

“No. I’d be grateful if you’d let them come with you.”

“What?”

“I, Sama Pyo, Sect Leader of the Black Dragon Demon Gate, and five hundred men ask to join the Fire Dragon Pavilion Master. Please let us fight for the world and make up, even a little, for the mistakes of our past.”

“……!”

For a moment, I was at a loss for words.

If a big guy hadn’t then shouted while dangling a small old man from his neck, I might not have been able to hold back the emotion welling up inside me.

“Taishan’s going! Taishan’s going, too! Taishan will go with the Pavilion Master to the end!”

“Goddamn it! Stop bouncing around so hard! Please!”

Everyone burst out laughing at once, as if they’d planned it.

Me, Sama Pyo, the Fire Dragon Pavilion members, and the survivors of the Nine Sects and One Gang.

Even Jeong Hogun, Thousand Captain of the Embroidered Uniform Guard, whose expression had always been utterly dry, whether he was happy or sad.

“What an amusing bunch you martial artists are.”

“Really? Since we’re on the subject, want to hear something even more amusing?”

“Something even more amusing?”

“Yeah. It’s about a certain Thousand Captain of the Embroidered Uniform Guard who kept talking back to a Marquis like he was his equal and is now on the verge of being forcibly discharged. The funny thing is, he has the same surname as you. What a coincidence, huh?”

“……Is that the way you’re going to play it?”

“Then do your best. So I don’t have to.”

As if he couldn’t win against me, Jeong Hogun shook his head, then stood as straight as an iron tower and saluted me.

“Then, please give your orders.”

“Qinghai. We’re going to Qinghai. At full speed.”

“I, Jeong Hogun, Thousand Captain of the Embroidered Uniform Guard, accept the solemn order of the Most Honorable Marquis of Shangshan.”

And so, two days ago, the final piece of our force—the Embroidered Uniform Guard—joined us. Our numbers had grown to nearly two thousand. After a brief rest, we headed straight for Qinghai Province.

A few people did argue that Dark Heaven might target Gansu again, but the Bow Saint ended all their concerns with a brief remark.

“The North is on the move.”

Of course, he didn’t mean northern Gansu.

He meant the North of the entire world, divided by the Great Wall—and the two powers that ruled that vast land.

The fierce tiger of Hebei, the Hebei Peng Family.

And the Azure Dragon of Shanxi Province, the Jin Family of Taiyuan, who had now claimed even the skies of the green grasslands.

“Each arrow may fly at a different speed, but as long as it doesn’t stray from its course, it will reach its target in the end.”

The Bow Saint and the Embroidered Uniform Guard were the first arrows shot, for example.

It was a metaphor worthy of the Bow Saint. After that, no one dared argue.

Not merely because the Bow Saint had said it.

Everyone knew that with the Azure Dragon and the fierce tiger of the North spreading their wings and baring their claws, Gansu’s safety was more or less guaranteed.

And the brief purge just before we left Gansu was enough to wipe out any possible future threat.

“Anything you want to say before you die? Spare me the excuses. I’ll hear your last words.”

“I—I never colluded with Dark Heaven. There must have been some misunderstanding!”

“Young Sect Leader—no, Sect Leader! Why are you doing this? You know your late father and I were practically sworn brothers!”

“Yeah, I know. Close enough to betray us together. You were so close that my father wrote it all down in detail… Did you know that?”

“……!”

The critical meeting that would decide the future of Gansu’s Murim had turned into a trial, with traitors being called to account. The room froze in an instant.

Wide eyes. Trembling lips.

Sama Pyo gave a small sigh at the sight of them and pulled a battered old book from inside his robe, setting it on the table.

“Looks like you really didn’t know. You might at least have suspected.”

Even I found it surprising that the meticulous Black Night King, Sima Gong, had left such clear evidence behind. So imagine how those men must have felt, having known him in life for decades.

But Sama Pyo went on without a second thought.

His voice held a trace of bitterness toward his father, and his eyes looked at them as though they were insects.

“So, any last words?”

That was the finishing blow.

“You—you little brat, with the blood barely dry on your head! You dare kill me, your uncle in all but name?!”

“Heh. Heh heh. So this is how it ends.”

A cornered rat had only two choices.

Charge with its adorable little front teeth as its only weapon—or give up on everything and accept its fate.

And the fools who chose the first option were met by…

“Story’s over, Taishan.”

“Yaaawn. Taishan almost fell asleep listening.”

The designated hitter for the Gansu Province Black Dragon Dragons, boasting a career batting average of .999: Tiger Giant Child Taishan.

*Wham! Wham!*

I’d been there in case anything happened, but there was no need for me to step in.

Taishan’s two-section staff was enthusiastically spewing fire—no, blood.

One of the Black Dragon Demon Gate’s senior members had shouted that Sama Pyo was a little brat with the blood barely dry on his head, then charged at him. His head was gone before he could spill any blood into it. Several Sect Leaders and Family Heads tried to flee with all their might, but they were surrounded the moment they left the pavilion.

By the warriors of the Black Dragon Demon Gate, who had pledged their loyalty to their new lord.

And by their own followers and Disciples.

“G-Gangpyeong! How could you do this to me?!”

“And how could you do this, Sect Leader?”

“Guard the way! Quickly! No, wait. I’m the Sect Leader! Stop those men right—”

“Shut your filthy mouth.”

“What?”

“Because of you, my Master, my Junior Sister, and my Martial Nephew died! That makes you guilty of deceiving your master and betraying your ancestors. Disciples of the Gorang Sword Sect, execute the Sect Leader on the spot, as the sect rules demand!”

“What are the members of the Lanzhou Hyuk Family doing?!”

“Please don’t hold it against us, Family Head. You were the one who betrayed us first.”

“Y-you bastards…!”

*Slice! Thud-thud-thud!*

Under the storm of spears and blades from every direction, around a dozen Sect Leaders and Family Heads died with their eyes wide open, unable even to leave proper last words.

It was a pitiful end for men who had led Gansu’s Murim, each the head of a faction with a substantial number of followers.

But the young Sect Leader of the Black Dragon Demon Gate didn’t so much as blink as he killed or captured twenty renowned masters in all.

He watched the whole scene with calm, cool eyes, then idly touched his teacup, which had gone cold, and suddenly spoke.

“Should I have them bring us fresh tea?”

“No. It tastes bad. We don’t have time, either. Besides, that scatterbrained guy will be joining us soon, so it’ll only upset my stomach.”

“Benefactor, does he really know the fastest route to Qinghai Province?”

“More precisely, Ma Junggeol told me. I don’t know what the guy used to do in his youth, but he knows geography inside out.”

“I see. Then, since we’ve finished our business here, I’ll come with the Pavilion Master.”

Sama Pyo nodded and stood.

The table had been filled with more than twenty faces only fifteen minutes earlier. Now it was empty, with nothing but toppled teacups and a battered old book left on it.

“Aren’t you taking it?”

“It’s useless to me now.”

With that, Sama Pyo left. I hesitated for a moment, then picked up the book.

It might have outlived its purpose and been thrown away, but this battered old book was still one of the traces left behind by his dead father.

And the moment I turned its first page without thinking, absently tasting the bitterness in my mouth, I understood the real meaning of what Sama Pyo had said.

“…Huh.”

I let out a laugh and set the book down.

No.

It was a bundle of yellowed pages, not a single character written on them, clearly left to gather dust somewhere for years without ever serving its purpose.

“Guess blood really does tell. In a good way.”

Muttering under my breath, I walked on, breathing in the stench of blood flowing from the traitors’ bodies.

Two days passed. Then, as we traveled across mountain slopes so rough they made me want to curse, another three days went by.

“Hey, young man. What’s your name?”

“Jin Taekyung. You know this is the twenty-fourth time you’ve asked, right?”

“Ah, yes. Jang Sam.”

“Why the hell would Jin Taekyung be Jang Sam… Hah. Never mind. What is it?”

“Well, it’s not all that important, really.”

“Then tell me anyway. While I’m still using polite speech with you.”

“It’s nothing much. I was just wondering where we are.”

“Pardon? What?”

“I asked where we are.”

“Son of a bitch.”

A powerful urge to kill that lunatic guide, who kept spouting insane nonsense with a straight face, took hold of me.

It was a fierce, deep-seated urge, strong enough to snap my last thread of self-control.

*Step.*

But just as I approached the Great Sir, unable to hold back any longer and ready to let our bodies do the talking—

*Ding!*

The clear chime that momentarily glued my fraying self-control back together rang in my ears.

> **System**
>
> Entered **Qinghai Province**.
```

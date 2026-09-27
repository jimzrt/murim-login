<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1026.txt",
      "sha256": "e1eb12d764e270d0f4e5ce6130d537e2c762ede8581598d704d0e4472bf6b973",
      "bytes": 15919
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "0d8cbe9041f88acb5f15506f446468f0f0a11a8e5b7af2d330ce59eb7d9964c9",
      "bytes": 1877
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "046f3071032d8c15b2687fbc02349b692cc95bf08c9f42b52911e659d45a859e",
      "bytes": 239514
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "c95b4ca4bf7e950bb5b119c41e709bf74ee0bdd6d2d998cf0d785ccf55df0338",
      "bytes": 1502
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "6ef5ad89c11dc5bce98035c61f8381713f0c14cf68a21f7b9e81baeb294ac1db",
      "bytes": 1682
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "1ed20074fe7f56911da4eedccb022c152d0b3149c5817036a1d6b1553cacd516",
      "bytes": 623
    },
    {
      "path": "characters/Sama Pyo.md",
      "sha256": "5ca6ed248fdf42e3e71422191f45bff6245103a2e12928e2e7dccc33c5100636",
      "bytes": 1069
    },
    {
      "path": "characters/Sima Gong.md",
      "sha256": "4cc75c02f5c1d3b0357f9a4d12f7dec6bb9344b595602ecc9ef27e148193323d",
      "bytes": 778
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "fcf67bc6cfbc70c2a257c30ba7ba70cada7f28488513fed7350a8eac519e333f",
      "bytes": 278187
    }
  ],
  "estimated_tokens": 12525
}
-->

# Durable State Update — Chapter 1026

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
1 and safe_through 1026. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1026. Profile updates may replace only one
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
  "chapter": 1026,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1026,
    "continuity_sources": [1026],
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
    "Dark Heaven captured Dunhuang after breaching the Jade Gate Pass, inflicting catastrophic losses on the defenders.",
    "The Blood-Sword Demon Lord serves the Lord of Heaven, has been ordered not to kill Jin Taekyung, and wants to meet him before battle; the Lord’s reason remains unknown.",
    "An unidentified killer slew all one hundred Great Snow Mountain scouts with identical single-sword strikes; Jeok Cheongang recognizes the wounds but cannot identify the technique.",
    "The Three Elders of Tianshan arrived beneath a white banner as Dark Heaven’s envoys; their leader says a new Demon Lord wishes to meet the defenders.",
    "Dark Heaven’s pursuit after Dunhuang killed Kongtong Sect leaders, including the Kongtong Sword Dragon and two Elders; the Kongtong Sect Leader appears to have escaped, but his whereabouts are unknown.",
    "Dark Heaven holds another thousand captives and offers to return some if the defenders accept the new Demon Lord’s offer; the terms and the captives’ fate remain unresolved.",
    "An army of tens of thousands has reached the Great Snow Mountain, where a battle is imminent.",
    "Sima Gong ordered Sama Pyo to watch Taekyung’s group; the secret letter Sama Pyo received remains unexplained."
  ],
  "continuity_sources": [
    1025
  ],
  "open_questions": [
    "Who is the new Demon Lord, and what does the offer require?",
    "Will the defenders accept the offer, and what will happen to the thousand captives?",
    "Where is the escaped Kongtong Sect Leader?",
    "Who killed the Great Snow Mountain scouts, and what is the origin of the sword technique?",
    "Who sent Sama Pyo the secret letter, what did it say, and are Sima Gong’s orders involving Pyo and Taishan connected to Dark Heaven?"
  ],
  "safe_through": 1025,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 사마공    | **Sima Gong**      |
| 종남파    | **Zhongnan Sect**                |
| 암천     | **Dark Heaven**                  |
| 가주     | **Family Head**                              |
| 문주     | **Sect Leader**                              |
| 소문주    | **Young Sect Leader**                        |
| 장문인    | **Sect Leader**                              |
| 제자     | **Disciple**                                 |
| 사형     | **Senior Brother**                           |
| 선배     | **Senior**                                   |
| 산서     | **Shanxi**             |
| 감숙     | **Gansu**              |
| 청해     | **Qinghai**            |
| 노부      | **this old man / I**                                            |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 사마표 | **Sama Pyo** | Young Sect Leader of the Black Dragon Demon Gate. |
| 산서괴협 | **Strange Hero of Shanxi** | Epithet referenced for the absent martial artist. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 야왕 | **Night King** | Rumored epithet for Jin Taekyung in Taiyuan's red-light district. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 풍운검군 | **Wind-and-Cloud Sword Lord** | Epithet of Gong Iljung, the Zhongnan Sect's Sect Leader. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 노호검객 | **Roaring Fury Swordsman** | Fiery-tempered elder and top-five master of the Zhongnan Sect. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 인내 | **Endurance** | System attribute replacing Toughness. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 천산 | **Tianshan** | Mountain region identified as the Demonic Cult's headquarters. |
| 마공 | **demonic martial arts** | Martial arts that appear to defy common principles. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 노야 | **Old Master** | Taekyung's private address for Jeok Cheongang. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 태을무정검 | **Taeeul Merciless Sword** | Title of the Zhongnan Sect’s Second Martial Uncle, who is in Xi’an. |
| 삼노 | **Three Old Men** | Mocking designation used by the Western Heaven Demon Lord for the aged Qilian Three Fiends. |
| 일원 | **One Origin** | Named Tang Clan organizational unit in Tang Sadok's mobilization order. |
| 열화신룡 | **Blazing Flame Divine Dragon** | New sobriquet bestowed on Jin Taekyung. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 촌각 | **moments** | Short intervals disappearing from Jeok's day. |
| 장성 | **Great Wall** | Wall used in the discussion of the Outer Lands. |
| 흑룡마문 | **Black Dragon Demon Gate** | Unorthodox faction from Gansu. |
| 식경 | **half an hour** | Time limit given for the requested reports. |
| 흑야왕 | **Black Night King** | Epithet of Sima Gong, Sama Pyo's father and the Sect Leader who built the modern Black Dragon Demon Gate. |
| 화룡각 | **Fire Dragon Pavilion** | New name chosen for Taekyung's pavilion. |
| 대설산 | **Great Snow Mountain** | Mountain where Baeksang's wartime account reaches its next episode. |
| 대마불사 | **a large group doesn't die easily** | Go proverb explaining why a large formation of stones is difficult to kill. |
| 화신 | **Fire God** | A local deity worshiped by one Nanman believer. |
| 종남 | **Zhongnan Sect** | Orthodox faction that fought in the historic battle. |
| 돈황 | **Dunhuang** | City identified as the foremost defensive line in Gansu. |
| 천산삼노 | **Three Elders of Tianshan** | The three former Demonic Cult fiends serving the Blood-Sword Demon Lord. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 진태경 | 엄마 | son_to_mother | Mom | casual and startled | Jin cries out to his mother as she charges at him during the hospital visit. |
| 엄마 | 진태경 | mother_to_son | my son | warm and affectionate | Taekyung's mother praises him during the public welcome. |
| 사마표 | 적천강 | Young Sect Leader to legendary elder | Great Hero Jeok | formal-deferential | Sama Pyo formally pays his respects to Jeok Cheongang as the Fire King. |
| 적천강 | 사마표 | legendary elder to unorthodox Young Sect Leader | you / young brat | blunt, suspicious, and contemptuous | Jeok addresses Sama Pyo with 네놈 and 어린놈 while probing his lineage and motives. |
| 사마표 | 진태경 | prospective recruit to pavilion master | you | polite, controlled, and candid | Sama Pyo uses 자네 while asking about Taekyung's attitude and admitting his intention to use him. |
| 진태경 | 사마표 | pavilion master to prospective recruit | you / that guy | blunt, informal, and distrustful | Taekyung speaks to and about Sama Pyo with casual forms such as 녀석 and 저놈. |
| 아빠 | 진태경 | father to son | Taekyung | affectionate informal | Addresses his young son warmly as Taekyung. |
| 진태경 | 아빠 | son to father | Dad | childlike informal | Taekyung addresses his father as Dad in the childhood flashback. |
| 사마표 | 각주 | Fire Dragon Pavilion member to pavilion master | Pavilion Master | formal but sardonic | Sama Pyo addresses Jin as 각주 while questioning his account of the incident. |
| 적천강 | 풍운검군 | legendary_elder_to_Zhongnan_sect_leader | Wind-and-Cloud Sword Lord | familiar and commanding | Jeok Cheongang tells him to get the Zhongnan disciples moving. |
| 노호검객 | 적천강 | senior_martial_artist_to_legendary_elder | Senior Jeok | deferential and cautious | Addresses Jeok as 노 선배 while explaining his actions. |
| 사마공 | 적천강 | unorthodox sect leader to senior martial master | Senior | formal and deferential | Greets Jeok Cheongang as 노선배. |
| 적천강 | 사마공 | senior martial master to longtime martial acquaintance | you | blunt and familiar | Uses direct, contemptuous language while teasing Sima Gong. |
| 진태경 | 사마공 | allied young martial artist to unorthodox sect leader | Great Hero Sima | polite and deferential | Addresses him as 사마 대협. |
| 사마공 | 진태경 | unorthodox sect leader to celebrated young martial artist | you | polite and familiar | Uses 자네 while speaking to Taekyung. |
| 풍운검군 | 적천강 | Zhongnan Sect Leader to legendary martial master | Senior Jeok | respectful | Refers to Jeok as 적 대협. |
| 사마공 | 사마표 | father to son | Pyo | intimate and familiar | Sima Gong calls him 표야 and 내 아들아. |
| 풍운검군 | 노호검객 | Zhongnan Sect Leader to Senior Brother | Senior Brother | respectful and strained | Addresses him as 사형 while protesting the decision. |
| 풍운검군 | 태을무정검 | Zhongnan Sect Leader to Senior Brother | Senior Brother | respectful and strained | Addresses him as 사형 while protesting the decision. |

## Listed compact profiles

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 1025
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; he distrusts process-first excuses when outcomes fail and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, and insists on protecting Taekyung while urging him not to risk his life; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy, and personally killed his former ally the Junzi Saber after that man joined the Demonic Cult.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1025
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan and the original owner of his current body, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master who can detect and eavesdrop on nearby Sound Transmissions subject to the participants’ relative levels, and a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure, willing to risk himself for others, and unwilling to excuse cruelty as the inevitable price of survival.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; Hyuk Mujin trusts Taekyung to fight beside him and feels no fear when Taekyung is with him; Peng Cheolhu regarded Taekyung as a worthy successor, and the Bow Saint relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1025
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Sama Pyo.md

# Sama Pyo (사마표)

- **Safe through:** Chapter 1024
- **Aliases:** Black Dragon Saber
- **Role:** Young Sect Leader and heir of the Black Dragon Demon Gate, a Morning Star reputed to be no less than the Ten Dragons and Phoenixes.
- **Personality:** Outwardly courteous and calculating, he is protective of Taishan and pragmatic in combat; he recognizes that his father's ruthless, survival-driven worldview shaped him, even as its influence weighs on him.
- **Voice:** Polite and ingratiating in public, with sardonic humor and controlled evasiveness.
- **Relationships:** Sama Pyo commands the absolutely loyal Taishan and is Sima Gong's son and heir; his father's ruthless treatment of family shaped his rise and remains a source of inner constraint. He joined the Fire Dragon Pavilion intending to use Jin Taekyung, and Sima Gong has now ordered him to spy on Taekyung's group. He was Ju Hwaran's former fiancé in a political engagement and is openly hostile toward fellow member Song Ilseom.

### Sima Gong.md

# Sima Gong (사마공)

- **Safe through:** Chapter 1025
- **Aliases:** Black Night King
- **Role:** Sima Gong is the Sect Leader who built the Black Dragon Demon Gate into a major unorthodox power and the father of its Young Sect Leader, Sama Pyo.
- **Personality:** Sly and calculating yet outwardly gentle; he calmly accepts sacrificing the rear population as the cost of a strategy he believes offers the best odds of victory.
- **Voice:** Polished and persuasive, with smooth rhetorical turns and a composed, gently teasing manner.
- **Relationships:** Sama Pyo is his youngest son among seven older brothers and nine older sisters; he is personally familiar with Jeok Cheongang, who openly dislikes him.

## Korean source

```text
＃1026화



놈들의 제안은 이랬다.

첫째. 지금으로부터 한 식경 후, 무장을 해제한 채 중간 지점에서 만날 것.

둘째. 참석 인원은 세 명으로 제한할 것.

그리고 마지막 셋째.

‘그 세 명 중, 반드시 열화신룡 진태경을 포함할 것.’

내가 조금 전 들었던 요구 조건을 떠올리며, 말을 몰아 멀어져 가는 천산삼노의 뒷모습을 바라보던 그때였다.

“네 녀석은 빠지거라.”

단호한 음성과 함께, 적천강이 굳은 얼굴로 나를 바라보며 말을 이었다.

“이번만큼은 안 된다.”

나는 어깨를 으쓱해 보였다.

“조금 다르긴 한데, 통했네요.”

“무엇이 말이냐.”

“저도 그 말씀 드리려고 했거든요. 이번만큼은 가야 할 것 같다고.”

“……!”

그럴 수밖에 없다.

무려 천 명.

놈들은 일천의 목숨을 망설임 없이 이 도박판에 밀어 넣었고, 이건 결코 우리를 대설산 밑으로 끌어내리기 위한 허장성세가 아니었다.

지금 이 순간, 저 멀리 낭패한 몰골을 한 포로들이 줄줄이 묶여 언덕 위로 모습을 드러내고 있었으니까.

아마도 돈황에서 사로잡혔거나, 패주하여 추격당한 이들일 것이 분명했다.

“보이시죠?”

내 물음에 적천강은 대답하지 않았고, 나는 천천히 말을 이었다.

“열 명도, 백 명도 아니고 천 명입니다. 선택의 여지가 없어요.”

일평생을 무법자로 살아온 세 마리의 개새끼들은, 떠나기 전 자신들이 재판장의 판사라도 되는 것처럼 엄중하게 경고했다.

만약 요구 조건을 하나라도 어긴다면, 저들을 모조리 죽이겠다고.

그리고 나는 저들에게 죽음이 선고되길 바라지 않는다.

“솔직히 저도 좀 후달리긴 하는데, 뭐 어쩌겠습니까. 얼마나 더 살지는 모르겠지만…… 남은 일평생 동안 잠 설치지 않으려면 가 봐야죠.”

반은 농담이고, 반은 진담이다.

도대체 언제쯤 악몽을 꾸지 않게 될까.

불현듯 드는 생각을 뒤로한 채 짐짓 웃으며 말을 건네자, 한참 동안 말이 없던 적천강이 문득 한숨을 내쉬었다.

“멍청한 놈 같으니.”

“에헤이, 갑자기 왜 이러셔. 저 말고 저 새끼들을 욕하셔야죠. 양심 없는 새끼들, 크게 이겨 놓고 추격까지 열심히 했네.”

“괜히 밝은 척하지 마라. 하나도 안 어울린다.”

“티 나요?”

“천하의 그 누구보다 뻔뻔한 주제에, 거짓말에는 도통 재주가 없는 것이 네놈 아니더냐.”

“……그런가.”

“만약 사로잡힌 포로가 만 명, 천 명이 아니라 열 명뿐이었어도 갔겠지. 노부가 알고 있는 너라면.”

과연 그럴까.

모르겠다.

벌어지지도 않은 상황에 대해 확신하는 건 어려운 일이니까.

하지만…… 그래. 아마도 그랬을 것 같다.

그리고 나는, 적천강 역시 그런 부류의 사람이라고 생각하고 있다.

“가실 거죠? 제가 말려도.”

“말릴 생각이었느냐?”

“아뇨.”

내가 정색하며 덧붙였다.

“까딱하면 훅 갈 수도 있는데, 노야라도 옆에 있어 주셔야죠.”

그제야 적천강이 피식 실소를 흘렸다.

“그러니까, 죽어도 같이 죽자?”

“무슨 그런 살벌한 말씀을 살아도 같이 살자는 얘깁니다.”

“그게 그거 아니냐.”

“다르죠. 아 다르고 어 다른 건데. 말씀을 그렇게 하시면 어떡합니까. 계속 그러시면 저 섭섭해요. 노야를 향한 믿음, 소망, 사랑. 뭐 그런 거 안 느껴지세요?”

“하여간 혓바닥 놀릴 때만큼은 아주 청산유수가 따로 없구나. 한데…….”

어이없다는 듯이 웃음소리를 흘린 적천강이, 일순간 착 가라앉은 목소리로 말을 이었다.

“네 녀석이 말하는 그 믿음이, 저놈들에게도 있을 거라 생각하느냐?”

나는 대답 대신 적천강이 바라보는 방향을 따라 고개를 돌렸다.

우리로부터 멀찍이 떨어진 그곳에는 논의를 끝마치고 다가오는 ‘저놈들’, 아니 수뇌부가 있었다.

철벅. 철벅.

눈과 비에 젖어 진창이 된 지면 위를 뒤덮는 수십여 개의 발자국.

그 선두이자 중심에, 한 사람이 있었다.

흑야왕 사마공.

“마음의 결정은, 이미 내렸나?”

아주 잠시, 나는 곧장 본론부터 꺼내 드는 사마공을 물끄러미 바라보았다.

그리고 대답했다.

“저는 이미 결정한 지 오랩니다. 여기 계신 노, 아니 스승님도 마찬가지고요.”

“매우 위험한 자리가 될 수 있다는 사실은 알고 있겠지?”

“물론입니다.”

“조심하게. 고작 일천 명의 포로로 대마(大馬)를 끌어들일 수 있다면, 놈들에게는 더할 나위 없는 결과일 테니.”

구구절절 옳은 말이다.

내 입으로 말하긴 뭣하지만, 적천강과 나는 암천으로서는 반드시 제거해야 하는 일 순위 경계 대상이니까.

지금까지 우리 두 사람이 놈들에게 준 타격을 생각한다면, 씹어 죽여도 시원치 않을 원수나 다름없었다.

하지만…….

‘고작, 고작 일천 명이라.’

아무리 그렇다 하더라도.

그 많은 숫자와 생명에 담긴 어마어마한 무게를, 당신은 어떻게 이리 가볍게 말할 수 있는 것일까.

그리고 암천이 바라는 그 결과와 당신이 그리는 그림은 얼마나 서로를 닮아 있으며, 조심하라는 경고에는 어느 정도의 진심이 들어가 있을까.

혀끝에서 맴도는 말을 삼킨 나는, 문득 기억 속에서 떠오른 네 글자를 불쑥 내뱉었다.

“대마불사(大馬不死).”

“대마는 쉽게 죽지 않는다…… 그렇군. 자네와 노 선배라면 설령 함정이더라도 무사히 돌아올 수 있겠지.”

오래된 바둑 격언을 혼잣말처럼 작게 중얼거린 사마공이 고개를 끄덕였다.

“자네와 노 선배의 뜻은 잘 알겠네.”

우리의 뜻을 전했으니, 이제 저들의 뜻을 전해 들을 차례다.

“그럼 다른 한 분은 누구십니까?”

참석할 수 있는 인원은 총 셋.

나와 적천강은 결정되었지만 다른 한 명이 빈다.

그리고 뒤이어 벌어진 상황은, 내가 내심 예상하고 있던 범주를 크게 벗어나지 않았다.

“나일세. 흑룡마문의 문주로서 기꺼이…….”

“아니오. 빈도가 가겠소.”

거의 동시에 튀어나온 두 줄기의 목소리.

마치 술집에서 자기가 계산하겠답시고 아웅다웅하는 아저씨들처럼, 사마공과 풍운검군은 서로를 만류했다.

“어떤 위험이 기다리고 있을지 모르오. 장문인께서는 이곳에 남아 계시지요.”

“그렇다면 더더욱 가야겠구려. 그런 측면에서 판단하자면 사마 문주보다는 빈도가 더 적임자일 테니.”

풍운검군의 반박처럼, 그가 마지막 자리를 차지하는 것은 상식적으로는 옳은 판단이었다.

사마공은 단순히 일문의 문주가 아니니까.

그는 흑룡마문의 시작과 끝이며, 감숙 무림의 중심이자 핵이다.

만약 불상사가 일어나 사마공의 신변에 문제가 생긴다면 흑룡마문이, 아니 현재 아군 병력 중 과반수를 차지한 감숙 무림 전체가 흔들린다.

그에 반해 풍운검군은 종남파의 장문인이지만, 그의 빈자리를 채울 두 사형이 있다.

노호검객과 태을무정검은 사람 됨됨이를 떠나, 종남파 내에서 지닌 영향력은 충분한 이들.

그러니 이는 자리의 중요성과 위험함에 있어, 최소한의 리스크를 계산해서 내린 선택이라고 할 수 있었다.

물론…….

‘남아 있는 사람이 완전히 믿을 수 있는 아군이라는 확신이 있을 때의 이야기지만.’

이것이 어디까지나 상식적으로 옳은 판단이라고 해도, 상식이 지배하는 세상이라면 우리가 왜 여기에 있겠나.

세상은 종종 극소수의 미친놈들에 의해 변화한다.

그것이 좋은 의미로든, 나쁜 의미로든.

‘그리고 어떤 미친놈은 나와 적천강, 풍운검군이 자리를 비운 사이에 후방을 장악할 수도 있을 테고.’

하지만 지금은 확신할 수 없는 불안감에 기대어 반박할 여지도, 그럴만한 여유도 없었다.

‘시간이 없어.’

약속했던 한 식경의 중, 이미 절반이 훌쩍 넘는 시간이 흘러간 상황.

적천강과 조용히 시선을 마주친 나는, 우리가 같은 마음을 품고 있음을 알 수 있었다.

‘이럴 거라면 차라리…….’

이대로 둘이 가는 게 낫다. 사마공은 어디에 있더라도 완전히 신뢰할 수 없는 인물이고, 그렇기에 풍운검군은 더더욱 남아 있어야 했으니까.

그래서 나는 이 의견을 모두에게 말했다.

아니, 정확히는 그러려고 했다.

바로 그때, 누구도 예상치 못했던 한 사람이 불현듯 입을 열기 전까지는.

저벅.

“외람되지만, 감히 제가 두 분께 양보를 청해도 되겠습니까?”

“……!”

그 순간, 나는 똑똑히 보았다.

유난히도 크게 울려 퍼지는 발걸음 소리와 함께 앞으로 나선 아들의 모습에, 깊게 가라앉는 아버지의 눈빛을.

“마지막 한 자리는, 제게 기회를 주시지요.”

또렷한 음성으로, 사마표가 모두를 향해 재차 되뇌었다.

“가겠습니다. 제가.”



* * *



왜일까.

어째서일까.

정확한 이유는 모르겠다.

다만, 지금 이 순간 내가 적천강과 사마표의 사이에서 나란히 걷고 있다는 것이 중요할 뿐이다.

하지만 치밀어 오르는 의문을 참아 내기에는, 내 인내심이 아주 조금 모자랐다.

“왜 그랬냐.”

고개는 일부러 돌리지 않았다.

정면을 주시하며 툭 내뱉은 한 마디에, 얼마 지나지 않아 나지막한 대답이 돌아왔다.

“무슨 말인지 모르겠군.”

“갑자기 왜 자원했냐고. 이미 어느 정도는 다 정해진 마당에.”

“정해지지 않았던 상황이었으니 내가 이 자리에 있는 거겠지. 그렇지 않나?”

나는 미간을 찌푸렸다.

“그건…….”

“어떤 함정이 기다리고 있을지 모르는 사지(死地)에 제 발로 가고 싶은 사람은 없지. 그것이 설령 의기로 드높은 구파일방의 장문인이라 하더라도.”

사마표가 담담한 어조로 덧붙였다.

“장문인을 사지로 보내야 하는 제자들은 어떻게 해서라도 그런 상황을 막고 싶었을 테고. 그렇지 않나, 각주?”

나는 반박할 수 없었다.

이건 단순한 가정이나 짐작이 아니라, 불과 촌각 전의 상황을 그대로 말로 풀어놓았을 뿐이니까.

사마표가 때맞춰 나서자 종남파 제자들은 반색하며 자신들의 장문인을 극구 만류했고, 감숙 무림의 영수들도 이때다 싶었는지 사마공의 소맷자락을 붙들었다.

이대로 다 가 버리면 유사시에 지휘는 누가 하냐고.

무슨 일이라도 생기면 이 많은 사람은 어쩔 거냐고.

게다가 사마표는 흑룡마문의 소문주 겸, 화룡각의 일원.

만류하는 명분도, 나설 만한 자격도 충분했고 그래서인지 다들 젊은 놈의 돌발행동을 고분고분하게 받아들였다.

현대식으로 쉽게 말하자면, 상황이 제법 괜찮게 와꾸가 짜여진 거다.

어느 쪽 대가리가 남아 있는 총대를 메느냐로 눈치 싸움을 하던 와중에, 사마표가 나섬으로써 그들의 간지러운 곳을 시원하게 긁어 주었으니까.

‘우리 쪽 사람들이야 뭐, 애초에 말려 봤자 씨알도 안 먹힌다는 걸 알고 있었고.’

뒤에 남게 된 다른 화룡각 대원들은 별다른 만류조차 하지 않았다. 그저 무사히 돌아오라는 말만 인사로 건넸을 뿐이다.

아무튼.

그렇게 모두가 원하는 결과가 나왔다.

아니, 단 한 사람만큼은 예외일지도 모른다.

‘사마공.’

갑작스럽게 나선 아들을 보며 그는 과연 무슨 생각을 하고 있었을까.

그 순간 깊게 가라앉았던 눈빛은 처음부터 계산된 것이었을까, 아니면 당황으로 인한 것이었을까.

그리고…….

‘이 녀석은 도대체 무슨 생각으로 나선 걸까.’

왜 그랬냐는 내 물음에, 사마표는 지금까지도 제대로 된 대답을 내놓지 않았다.

그 대신 지금 이 상황과는 전혀 상관없는 불쑥 내뱉고 있었다.

“그나저나, 바둑에도 조예가 있는 줄은 몰랐군.”

“뭐?”

“조금 전에 각주가 말하지 않았나. 대마불사라고.”

말을 돌리는 건가. 아니면 뭔가를 말하고 싶은 건가.

쉽게 예측이 되지 않았지만, 나는 이내 담담하게 대답했다.

“조예는 무슨. 나는 바둑 같은 거 잘 몰라. 그냥 어릴 때부터 어깨너머로 보고 들은 게 전부지.”

“어릴 때부터라면…….”

“아버지. 바둑 좋아하셨거든.”

“그렇군. 가주이신 산서괴협(山西怪俠)에 관한 이야기는 얼핏 들어 알고 있지.”

“못 뵌 지 한참 됐는데, 아직도 기억이 생생해.”

사마공은 까맣게 모를 것이다.

지금 내가 말하는 아버지가 누구인지.

나는 이 두 번째 세상에서 피가 이어지지 않은 형들을 얻고, 새로운 동료와 친구들. 또 스승을 만났지만 아버지만큼은 늘 한 분뿐이었다.

인터넷 바둑에서 매번 패배할 때마다 짱깨 새끼들이 치팅 프로그램을 썼다며 정신 승리를 얻어내고, 국내의 모 대기업 전자 종목에 주식을 몰빵하며 대마불사를 외치셨던.

그런 분이었다.



‘아빠, 컴퓨터 화면이 왜 다 파래?’

‘아들아, 하늘은 무슨 색이지?’

‘빨간색.’

‘아니야. 지금은 노을 때문에 그래. 하늘은 원래 파란색이야. 아빠의 주식도 잠깐 그런 것뿐이란다.’

‘구래? 그럼 곧 빨개져?’

‘물론이지. 이 종목은 그러니까, 대마거든.’

‘대마? 그거 안 좋은 거자나. 기분 좋아지는 거.’

‘너 도대체 유치원에서 뭘 하고 다니…… 아니다. 여하튼 이건 그 대마가 아니야. 엄청 큰, 쎄고 뭐 그런 거야. 그리고 이렇게 쎄고 큰 건 쉽게 죽지 않는단다. 바둑에서는 대마불사라고 하지.’

‘아하.’

‘아마 조만간 그때가 되면, 여기 있는 선이 위로 쑥쑥 솟구칠 거야. 하늘 높이, 노을 진 것처럼 빨갛게.’

‘우음. 그렇구나. 근데 아빠.’

‘응?’

‘지금 엄마 얼굴 봐, 엄청 빨개!’

‘……여보, 언제 왔어?’



피식.

불현듯 터져 나온 실소에 사마표가 눈을 크게 떴다.

이런 상황에서 웃으면 안 되는데, 알고 있는데도 자꾸만 입가에 번지는 미소를 감추지 못하며 내가 입을 열었다.

“별거 아냐. 그냥, 그냥…… 예전에 좋았던 기억이 생각나서.”

“아버지와의 좋았던 기억이라.”

혼잣말처럼 중얼거린 사마표가 나를 따라 웃었다.

“그렇군.”

먹구름 낀 하늘처럼 흐릿하고, 씁쓸한 미소.

그런 녀석의 모습에 알 수 없는 기시감을 느낀 그때, 어느 새인가부터 묵묵히 앞장서서 걷던 적천강이 입을 열었다.

“둘 다 실컷 웃고 떠들었으면, 이제 불청객을 맞이해야겠지?”

그 순간.

다그닥. 다그닥.

느릿하게 울려 퍼지는 말발굽 소리와 함께, 마침내 놈들이 모습을 드러냈다.

아니, ‘놈’이.
```

## Final English reading copy

```markdown
# Chapter 1026

Their offer was as follows.

First: They would meet at a midpoint in half an hour, unarmed.

Second: No more than three people could attend.

And third…

*One of those three must be the Blazing Flame Divine Dragon, Jin Taekyung.*

I was recalling the terms I’d just heard, watching the Three Elders of Tianshan ride away, when Jeok Cheongang spoke.

“You’re staying behind.”

His voice was firm. He looked at me, his face set, and continued.

“Not this time.”

I shrugged.

“Well, that was a little different, but it worked.”

“What was?”

“I was about to say the same thing to you. That I think I have to go this time.”

“……!”

There was no other choice.

A thousand people.

They’d wagered a thousand lives without hesitation. This wasn’t some empty bluff to lure us down from the Great Snow Mountain.

Even now, a long line of prisoners, looking battered and miserable, was appearing on the distant hillside, bound together.

They had to be people captured at Dunhuang, or people who’d fled and been run down.

“You see them, right?”

Jeok Cheongang didn’t answer. I continued slowly.

“Not ten. Not a hundred. A thousand. We don’t have a choice.”

Before leaving, those three bastard dogs who’d spent their entire lives as outlaws had issued a stern warning, as if they were judges in a courtroom.

If we broke even one of their conditions, they’d kill every last prisoner.

And I didn’t want those people condemned to die.

“Honestly, I’m pretty damn scared too, but what can you do? I don’t know how much longer I’ll live, but… I don’t want to spend the rest of it losing sleep. So I have to go.”

Half joke, half serious.

When would I stop having nightmares?

I pushed the sudden thought aside, put on a smile, and spoke. Jeok Cheongang had been quiet for a long while. At last, he let out a sigh.

“You foolish brat.”

“Hey, what’s with that all of a sudden? You should be cursing those bastards, not me. Shameless bastards. They won big, and then they even worked hard at chasing everyone down.”

“Don’t pretend to be cheerful. It doesn’t suit you at all.”

“Is it that obvious?”

“You’re more shameless than anyone under heaven, but you’ve never been any good at lying.”

“……I guess not.”

“Even if there were only ten prisoners instead of ten thousand or a thousand, you’d still go. That’s the kind of person you are, as far as this old man knows.”

Would I really?

I didn’t know.

It was hard to be certain about a situation that hadn’t happened.

But… yeah. I probably would have.

And I thought Jeok Cheongang was that kind of person, too.

“You’re going, right? Even if I try to stop you?”

“Were you planning to?”

“No.”

I added, dead serious,

“If things go badly, we could be dead in a flash. You’d better stay by my side, Old Master.”

Only then did Jeok Cheongang let out a quiet laugh.

“So we die together, then?”

“What kind of grim talk is that? I mean we live together.”

“Same thing.”

“It’s not. One word can make all the difference. How can you say that? Keep it up and you’ll hurt my feelings. Don’t you feel my trust, hope, and love for you?”

“Your tongue is a river of eloquence whenever you start running it. But…”

Jeok Cheongang’s laughter faded. His voice dropped low.

“Do you think those men have the same trust you’re talking about?”

Instead of answering, I turned to look where Jeok Cheongang was looking.

A short distance away, the people we’d been discussing—no, the leaders—were approaching after finishing their deliberations.

Squish. Squish.

Dozens of footsteps pressed into the ground, turned to mud by snow and rain.

At their head, at the center of them all, was one man.

The Black Night King, Sima Gong.

“Have you made up your mind?”

For a moment, I stared at Sima Gong as he got straight to the point.

Then I answered.

“I made up my mind a long time ago. And so did the… no, my Master here.”

“You understand how dangerous this could be?”

“Of course.”

“Be careful. If they can draw in a major piece with just a thousand prisoners, it will be the best possible outcome for them.”

Every word was true.

As much as I hated to say it, Jeok Cheongang and I were Dark Heaven’s highest-priority targets for elimination.

After all the damage we’d done, we were enemies they’d like nothing more than to chew up and spit out.

But…

*Just a thousand, huh.*

No matter how you looked at it…

How could you talk so lightly about the immense weight of so many lives?

And how much did the outcome Dark Heaven wanted resemble the picture you were trying to paint? How sincere was that warning to be careful?

I swallowed the words circling the tip of my tongue. Then four characters suddenly came to mind, and I blurted them out.

“A large group is hard to kill.”[^1]

“Right… A large group doesn’t die easily. If you and Senior Jeok are going, you should be able to return safely even if it’s a trap.”

Sima Gong murmured the old Go proverb to himself, then nodded.

“I understand what you and Senior Jeok have decided.”

We’d made our intentions clear. Now it was time to hear theirs.

“Then who will the third person be?”

Three people could attend in all.

Jeok Cheongang and I were settled, but there was still one place open.

What happened next wasn’t far outside the range of what I’d been expecting.

“I’ll go. As Sect Leader of the Black Dragon Demon Gate, I’m willing to…”

“No. I’ll go.”

Two voices rang out almost at once.

Like a couple of middle-aged men arguing over who was going to pay at a bar, Sima Gong and the Wind-and-Cloud Sword Lord tried to stop each other.

“We don’t know what dangers lie ahead. Sect Leader, you should remain here.”

“Then all the more reason I must go. By that logic, I’m more suited to the task than Sect Leader Sima.”

As the Wind-and-Cloud Sword Lord argued, choosing him for the last spot made sense.

Sima Gong wasn’t merely the leader of one sect.

He was the beginning and end of the Black Dragon Demon Gate, and the heart and center of the Gansu Murim world.

If something went wrong and Sima Gong were harmed, the Black Dragon Demon Gate—or rather, the entire Gansu Murim force, which made up more than half of our current army—would be thrown into disarray.

The Wind-and-Cloud Sword Lord, on the other hand, was the Sect Leader of the Zhongnan Sect, but two of his Senior Brothers could fill his place.

The Roaring Fury Swordsman and the Taeeul Merciless Sword were both influential enough within the Zhongnan Sect, regardless of what kind of people they were.

So, in terms of the importance of the position and the danger involved, this was the choice that minimized the risk.

Of course…

*That only applies if you can be certain the people left behind are allies you can trust completely.*

Even if that was the sensible choice, why were we here if the world were governed by common sense?

The world sometimes changed because of a tiny handful of lunatics.

For better or worse.

*And one of those lunatics could take control of the rear while Jeok Cheongang, the Wind-and-Cloud Sword Lord, and I were away.*

But there was no time to argue based on an unease I couldn’t prove. We didn’t have that kind of time to spare.

*There’s no time.*

More than half of the promised half hour had already passed.

I met Jeok Cheongang’s eyes. I could tell we were thinking the same thing.

*If it comes to this, then…*

It would be better for just the two of us to go. Sima Gong wasn’t someone we could fully trust, wherever he was, and that was all the more reason the Wind-and-Cloud Sword Lord needed to stay behind.

I was about to tell everyone that.

No, I was about to.

Until someone no one expected suddenly spoke up.

Step.

“Forgive me for speaking out of turn, but may I respectfully ask you two to let me take the place?”

“……!”

In that moment, I saw it clearly.

As his son stepped forward, his footsteps ringing unusually loud, his father’s eyes sank into a deep, dark gaze.

“Please give me the last place.”

In a clear voice, Sama Pyo repeated himself to everyone.

“I’ll go.”

[^1]: The Korean word for a large group of stones in Go is also the word for cannabis, which sets up the wordplay in the childhood memory that follows.

* * *

Why?

Why had it turned out this way?

I didn’t know the exact reason.

All that mattered was that, at this moment, I was walking alongside Jeok Cheongang and Sama Pyo.

But my patience was just a little too thin to keep the questions building inside me to myself.

“Why’d you do it?”

I deliberately kept my gaze forward. Not long after I tossed out the question, a quiet answer came back.

“I don’t know what you mean.”

“Why’d you suddenly volunteer? Most of it was already decided.”

“If it had been decided, I wouldn’t be here. Would I?”

I furrowed my brow.

“Well…”

“No one wants to walk willingly into a deadly trap when they have no idea what might be waiting for them. Not even the Sect Leader of one of the Nine Sects and One Gang, whose reputation is built on honor.”

Sama Pyo added in a calm voice,

“His disciples would have wanted to prevent that at all costs. They wouldn’t want to send their Sect Leader to his death. Isn’t that right, Pavilion Master?”

I couldn’t argue.

He wasn’t making a guess or a supposition. He was just describing what had happened a few moments ago.

When Sama Pyo stepped forward at just the right time, the Zhongnan disciples had looked relieved and done everything they could to dissuade their Sect Leader. The leaders of the Gansu Murim forces had taken their chance, too, grabbing at Sima Gong’s sleeves.

If everyone left, who would be in command if something happened?

What would happen to all these people?

On top of that, Sama Pyo was both the Young Sect Leader of the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion.

There were plenty of grounds for trying to stop him, but he was also qualified to step forward. Perhaps that was why everyone accepted the young man’s sudden move without much fuss.

Put simply, the situation had been arranged pretty neatly.

While everyone had been trying to read each other’s faces, waiting to see which leader would be left holding the bag, Sama Pyo had scratched exactly the itch they all had.

*Our people, of course, already knew that trying to stop us would be a waste of breath.*

The other Fire Dragon Pavilion members who were staying behind hadn’t tried to dissuade us either. They’d simply told us to come back safely.

Anyway.

Everyone had gotten what they wanted.

Well, almost everyone.

*Sima Gong.*

What was he thinking as he watched his son step forward so suddenly?

Had his eyes grown dark because he’d planned this from the start, or because he’d been caught off guard?

And…

*What the hell was this guy thinking when he volunteered?*

Even now, Sama Pyo hadn’t given me a proper answer to my question.

Instead, he suddenly brought up something that had nothing to do with the situation.

“By the way, I didn’t know you knew anything about Go.”

“What?”

“You said it earlier, Pavilion Master. That a large group is hard to kill.”

Was he changing the subject? Or trying to tell me something?

I couldn’t tell. So I answered calmly.

“I’m no expert. I don’t know much about Go. I just watched and listened from the sidelines when I was a kid.”

“Since you were a kid…”

“My dad liked Go.”

“I see. I’ve heard a little about the Strange Hero of Shanxi, your Family Head.”

“It’s been a long time since I saw him, but I still remember him vividly.”

Sima Gong had no idea.

He had no idea who I was talking about.

In this second life, I’d found brothers who weren’t related to me by blood, new companions and friends, and a Master. But I’d only ever had one father.

The kind of man who, whenever he lost at online Go, convinced himself that those Chinese bastards were using cheat programs, and who went all in on some major Korean electronics company’s stock while insisting it was a daema—a large group, hard to kill.

That was the kind of man he was.

*“Dad, why is the whole computer screen blue?”*

*“Son, what color is the sky?”*

*“Red.”*

*“No, that’s because of the sunset. The sky is blue. My stock’s only blue for a little while, too.”*

*“Really? So it’ll turn red soon?”*

*“Of course. This stock is a daema, you see.”*

*“Daema? Isn’t that bad? The stuff that makes you feel good?”*

*“What on earth are you doing at kindergarten… No, anyway, this isn’t that kind of daema. It means something really big and strong. And something this big and strong doesn’t die easily. In Go, we call it ‘a large group is hard to kill.’”*

*“Oh.”*

*“Once it happens, those lines on the screen will shoot way up. High into the sky, red like the sunset.”*

*“Hmm. I see. But, Dad.”*

*“Yeah?”*

*“Look at Mom’s face. It’s really red!”*

*“……Honey, when did you get here?”*

A quiet laugh escaped me.

Sama Pyo’s eyes widened.

I knew I shouldn’t laugh at a time like this, but I couldn’t hide the smile creeping onto my lips.

“It’s nothing. Just… just remembered something nice from a long time ago.”

“A nice memory with your father.”

Sama Pyo murmured as if to himself, then smiled along with me.

“I see.”

His smile was hazy and bitter, like the cloudy sky.

I felt a strange sense of déjà vu at the sight of him. That was when Jeok Cheongang, who had been silently leading the way, spoke.

“If you two are done laughing and chatting, we should greet our unwelcome guest.”

At that moment—

Clip-clop. Clip-clop.

With the slow sound of approaching hooves, they finally appeared.

No—*he* did.
```

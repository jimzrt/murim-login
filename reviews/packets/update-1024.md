<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1024.txt",
      "sha256": "9ff73f6cabd0aee0f318ad73387613fe10144665d5f3bb7f327911271a12afcb",
      "bytes": 13334
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "7682c1cc1e08499d8cf200a07a636584eae8fbae47c60bb17dfdcfaa39d4f296",
      "bytes": 1789
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "50510c5c666f259e0286c9c5f0498e0c9610e51f87349dfe70db991ed606b4e8",
      "bytes": 239169
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "b78e802e928721870502becbb39e059a1bdf21f22d9cbd7e6f5d7b5dda773125",
      "bytes": 760
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "63320c50e3d9dc5e689623ae0186bf72295ad9bf1b8baf65f6a1dc65cff1879b",
      "bytes": 1375
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "7bcfaca953c72174c9baede5aeb4853b0965f0806c6a9e15b71c3cdd3c57dd40",
      "bytes": 1502
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "d98d86897150d1c4d049de87b8c18430c4a989c9c6461f7b1662030b56089746",
      "bytes": 1682
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "562a6bd1a934ce6ba3b4d36c8e99ee2d818b73ede03dbc83cbff0e5eaca2e026",
      "bytes": 623
    },
    {
      "path": "characters/Ma Junggeol.md",
      "sha256": "13bdadf4c0360bd8b586356a7d4c4fa7b72cb73f00c532f430e3ddf510e4476b",
      "bytes": 673
    },
    {
      "path": "characters/Sama Pyo.md",
      "sha256": "3e66d06523a8564ae7ba5cd024fa489880c0977a0108b819e21be1651bdd0c02",
      "bytes": 1069
    },
    {
      "path": "characters/Sima Gong.md",
      "sha256": "d64af3366516da2b799d3166f1e97de43501ce7a28c3073014cb84b3fb0b698a",
      "bytes": 778
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "09989f9e6ebbc933bcef7c9c3fac34bff01693d4d450595ef0198c38e31daca8",
      "bytes": 277989
    }
  ],
  "estimated_tokens": 12707
}
-->

# Durable State Update — Chapter 1024

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
1 and safe_through 1024. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1024. Profile updates may replace only one
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
  "chapter": 1024,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1024,
    "continuity_sources": [1024],
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
    "Taekyung’s thirty-thousand-strong force is advancing up the Great Snow Mountain; more than half are from unorthodox factions, and Taekyung doubts its strength.",
    "Allied signals have confirmed that the Great Snow Mountain is occupied by Taekyung’s side.",
    "Dark Heaven captured Dunhuang after breaching the Jade Gate Pass, inflicting catastrophic losses on the defenders.",
    "A middle-aged Dark Heaven killer slaughtered more than a hundred Kongtong Sect members, including the Kongtong Sword Dragon; his identity and strength are unknown.",
    "Taekyung suspects Dark Heaven has at least three Supreme Peak masters or one overwhelmingly powerful superhuman; he wonders whether the Lord of Heaven is involved.",
    "Sima Gong ordered Sama Pyo to watch Taekyung’s group; the secret letter Sama Pyo received remains unexplained.",
    "The Kongtong Sect Leader escaped Dunhuang, but his whereabouts remain unknown.",
    "Hong Pyo is a Deputy Thousand Captain of the Gansu Regional Military Commission who strictly enforces identity checks at a checkpoint on the mountain.",
    "Urgent war drums sound from beyond the ridge; their source is unknown."
  ],
  "continuity_sources": [
    1023
  ],
  "open_questions": [
    "Who sent Sama Pyo the secret letter, what did it say, and are Sima Gong’s orders involving Pyo and Taishan connected to Dark Heaven?",
    "Where is the Kongtong Sect Leader?",
    "Who is the middle-aged killer, and what is the extent of his strength?",
    "What hidden strength gave Dark Heaven confidence to invade Gansu, and is the Lord of Heaven involved?",
    "What is happening beyond the ridge, and what prompted the war drums?"
  ],
  "safe_through": 1023,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 사마공    | **Sima Gong**      |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 십왕     | **Ten Kings**       |
| 종남파    | **Zhongnan Sect**                |
| 암천     | **Dark Heaven**                  |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무인     | **martial artist**                               | Default term                                          |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 살기     | **killing intent**                               |                                                       |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 정파     | **orthodox faction**                             |                                                       |
| 마교     | **Demonic Cult**                                 |                                                       |
| 중원     | **Central Plains**                               |                                                       |
| 제자     | **Disciple**                                 |
| 사매     | **Junior Sister**                            |
| 상태               | **Status**                     |
| 칭호               | **Title**                      |
| 화산     | **Huashan**            |
| 구화산    | **Mount Jiuhua**       |
| 노부      | **this old man / I**                                            |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 마중걸 | **Ma Junggeol** |
| 사마표 | **Sama Pyo** | Young Sect Leader of the Black Dragon Demon Gate. |
| 내상 | **Internal Injury** | System condition label for internal injury. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 군림 | **The Reign** | Opening fragment of an incomplete wuxia novel title that Taekyung read through volume thirty-four. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 천산 | **Tianshan** | Mountain region identified as the Demonic Cult's headquarters. |
| 마공 | **demonic martial arts** | Martial arts that appear to defy common principles. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 천주 | **Lord of Heaven** | Authority invoked by the masked attackers. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 살수 | **assassin** | Professional killer considered as a possible suspect. |
| 삼노 | **Three Old Men** | Mocking designation used by the Western Heaven Demon Lord for the aged Qilian Three Fiends. |
| 악귀 | **Fiend** | Descriptive epithet applied to the First Fiend. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 교주 | **Cult Leader** | Leader of the Divine Cult. |
| 마두 | **fiend** | Demonic martial masters from the Great Faction War era. |
| 열화신룡 | **Blazing Flame Divine Dragon** | New sobriquet bestowed on Jin Taekyung. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 흑룡마문 | **Black Dragon Demon Gate** | Unorthodox faction from Gansu. |
| 화룡각 | **Fire Dragon Pavilion** | New name chosen for Taekyung's pavilion. |
| 서리 | **seori** | Colloquial term for stealing crops or produce from a field. |
| 검마 | **Sword Demon** | A Demonic Cult swordsman whose final technique is compared with One Annihilation. |
| 대설산 | **Great Snow Mountain** | Mountain where Baeksang's wartime account reaches its next episode. |
| 화신 | **Fire God** | A local deity worshiped by one Nanman believer. |
| 종남 | **Zhongnan Sect** | Orthodox faction that fought in the historic battle. |
| 십만마도 | **Hundred Thousand Demonic Disciples** | The earlier force used as a comparison for Dark Heaven’s army. |
| 백마칠종 | **Seven Masters of Baekma Bang** | Collective title for Ma Junggeol and his six associates. |
| 돈황 | **Dunhuang** | City identified as the foremost defensive line in Gansu. |
| 옥문관 | **Jade Gate Pass** | Strategic pass breached before Dunhuang fell. |

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
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 중년인 | 진태경 | veteran civilian Hunter to celebrated allied Hunter | Mr. Jin | formal-polite and awed | The casualty clerk addresses Jin as 진 선생님 after Jin asks him to list Lei Fei among the dead. |
| 진태경 | 중년인 | celebrated Hunter to older fellow Hunter | sir | casual and teasing | Jin addresses the older Hunter as 아저씨 while joking with him and giving him instructions. |
| 사마표 | 적천강 | Young Sect Leader to legendary elder | Great Hero Jeok | formal-deferential | Sama Pyo formally pays his respects to Jeok Cheongang as the Fire King. |
| 적천강 | 사마표 | legendary elder to unorthodox Young Sect Leader | you / young brat | blunt, suspicious, and contemptuous | Jeok addresses Sama Pyo with 네놈 and 어린놈 while probing his lineage and motives. |
| 사마표 | 진태경 | prospective recruit to pavilion master | you | polite, controlled, and candid | Sama Pyo uses 자네 while asking about Taekyung's attitude and admitting his intention to use him. |
| 진태경 | 사마표 | pavilion master to prospective recruit | you / that guy | blunt, informal, and distrustful | Taekyung speaks to and about Sama Pyo with casual forms such as 녀석 and 저놈. |
| 혁무진 | 조장님 | pavilion_member_to_squad_leader | Captain | deferential and dubious | Mujin questions whether the pasture should be called the Nanman Ranch instead of the Nanman Beast Palace. |
| 사마공 | 적천강 | unorthodox sect leader to senior martial master | Senior | formal and deferential | Greets Jeok Cheongang as 노선배. |
| 적천강 | 사마공 | senior martial master to longtime martial acquaintance | you | blunt and familiar | Uses direct, contemptuous language while teasing Sima Gong. |
| 진태경 | 사마공 | allied young martial artist to unorthodox sect leader | Great Hero Sima | polite and deferential | Addresses him as 사마 대협. |
| 사마공 | 진태경 | unorthodox sect leader to celebrated young martial artist | you | polite and familiar | Uses 자네 while speaking to Taekyung. |
| 진태경 | 마중걸 | Murim Alliance member to visiting horse-caravan chief | Junggeol | casual | Initially addresses him familiarly, then apologizes and shifts to polite speech. |
| 마중걸 | 진태경 | visiting horse-caravan chief to young Murim Alliance member | young man | polite and deferential | Initially calls him a pretty little gigolo as an insult, then uses a respectful address. |
| 마중걸 | 적천강 | visiting horse-caravan chief to legendary martial master | Great Hero Jeok Cheongang | polite and deferential | Recognizes Jeok as the Fire King. |
| 마중걸 | 사마공 | visiting group leader to sect leader | Sect Leader Sima | polite and respectful | Addresses him as 사마 문주 while explaining Ningxia and Baekma Bang. |
| 사마공 | 마중걸 | sect leader to visiting group leader | you | formal and probing | Uses 자네 while questioning Ma Junggeol about following Dark Heaven. |
| 사마공 | 사마표 | father to son | Pyo | intimate and familiar | Sima Gong calls him 표야 and 내 아들아. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1022
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 1023
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and an active member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented; despite being naturally fearful, he faces danger and remains loyal to the person he serves, with irreverent self-deprecation and a taste for glory. He is suspicious of Taekyung, bluntly critical of the family's disgraced third son, and an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; with Taekyung, blunt and occasionally incredulous, while using breezy, irreverent banter to defuse tense situations.
- **Relationships:** He is loyal to Taekyung, who trusts him to act independently, especially in his home region of Shanxi and at the Jin Family of Taiyuan. As a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Fire Dragon Pavilion members accompanying Taekyung. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 1023
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; he distrusts process-first excuses when outcomes fail and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, and insists on protecting Taekyung while urging him not to risk his life; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy, and personally killed his former ally the Junzi Saber after that man joined the Demonic Cult.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1021
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan and the original owner of his current body, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master who can detect and eavesdrop on nearby Sound Transmissions subject to the participants’ relative levels, and a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure, willing to risk himself for others, and unwilling to excuse cruelty as the inevitable price of survival.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; Hyuk Mujin trusts Taekyung to fight beside him and feels no fear when Taekyung is with him; Peng Cheolhu regarded Taekyung as a worthy successor, and the Bow Saint relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1021
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Ma Junggeol.md

# Ma Junggeol (마중걸)

- **Safe through:** Chapter 1022
- **Aliases:** Chief of Baekma Bang
- **Role:** Ma Junggeol is the chief of Baekma Bang, a horse-caravan group founded by reformed Ningxia mounted-bandit leaders.
- **Personality:** Though timid by nature, he is earnest and protective of his sworn brothers, loyal to the benefactor who helped them reform, and willing to bear personal risk for their mission.
- **Voice:** Not established
- **Relationships:** He leads six sworn brothers who, with him, are known as the Seven Masters of Baekma Bang, and trusts the benefactor they call the Lord.

### Sama Pyo.md

# Sama Pyo (사마표)

- **Safe through:** Chapter 1023
- **Aliases:** Black Dragon Saber
- **Role:** Young Sect Leader and heir of the Black Dragon Demon Gate, a Morning Star reputed to be no less than the Ten Dragons and Phoenixes.
- **Personality:** Outwardly courteous and calculating, he is protective of Taishan and pragmatic in combat; he recognizes that his father's ruthless, survival-driven worldview shaped him, even as its influence weighs on him.
- **Voice:** Polite and ingratiating in public, with sardonic humor and controlled evasiveness.
- **Relationships:** Sama Pyo commands the absolutely loyal Taishan and is Sima Gong's son and heir; his father's ruthless treatment of family shaped his rise and remains a source of inner constraint. He joined the Fire Dragon Pavilion intending to use Jin Taekyung, and Sima Gong has now ordered him to spy on Taekyung's group. He was Ju Hwaran's former fiancé in a political engagement and is openly hostile toward fellow member Song Ilseom.

### Sima Gong.md

# Sima Gong (사마공)

- **Safe through:** Chapter 1023
- **Aliases:** Black Night King
- **Role:** Sima Gong is the Sect Leader who built the Black Dragon Demon Gate into a major unorthodox power and the father of its Young Sect Leader, Sama Pyo.
- **Personality:** Sly and calculating yet outwardly gentle; he calmly accepts sacrificing the rear population as the cost of a strategy he believes offers the best odds of victory.
- **Voice:** Polished and persuasive, with smooth rhetorical turns and a composed, gently teasing manner.
- **Relationships:** Sama Pyo is his youngest son among seven older brothers and nine older sisters; he is personally familiar with Jeok Cheongang, who openly dislikes him.

## Korean source

```text
＃1024화



언제나 죽음의 위기를 넘나드는 무림인에게 청각(聽覺)은 더할 나위 없이 중요한 감각이다.

소리에는 그만큼 많은 의미가 담겨 있다.

적과 마주한 상태에서 옷깃 스치는 소리가 나면 그건 상대가 암습을 펼치고 있다는 뜻이나 진배없고, 목소리의 높낮이와 떨림을 통해 심리 또한 읽어 낼 수 있다.

즉 무림인에게 있어 소리란 곧 정보였다.

그리고 바로 지금 이 순간, 저 멀리서 울려 퍼지는 북소리도 결코 그 범주를 벗어날 수 없었다.

둥, 두둥, 두우웅!

제대로 된 박자도 지키지 않고, 울림의 크기도 다르다.

눈 덮인 산맥 어딘가에서 반쯤 혼백이 빠져나간 얼굴로 그저 온 힘을 다해 북을 치고 있을 고수(鼓手)의 모습을 떠올린 중년인은 뒷덜미를 긁적였다.

“이거, 시작부터 너무 인사가 과했나?”

그의 말에 곳곳에서 낮은 웃음소리가 흘러나왔다.

한 시진 전, 인근에서 맞닥트린 대설산의 척후조 일백이 싸늘한 주검이 되었다는 것은 이제 그들만이 아는 비밀이 아니었다.

“그럴 만도 하지요. 한솥밥 먹던 자들이 하루아침에 시체가 되어 돌아왔으니.”

“수급을 주렁주렁 매단 말들이 돌아오니 벌써 잔뜩 겁을 집어먹은 모양입니다. 이제 겨우 시작이라는 것도 모르고.”

“하지만 저희로서도 경계를 늦춰서는 안 됩니다. 화왕, 그 노괴(老怪)의 무위가 정확히 어느 정도인지는…….”

퍼엉!

거대한 파공성이 이어지려던 목소리를 집어삼킨다.

말을 끝맺기도 전, 가슴을 후려치는 막강한 힘을 느낀 노인은 일순간 포탄처럼 튕겨 나가는 신형을 바로잡으며 지면에 착지했다.

아니, 착지하려 했다.

“우읍, 쿠에에엑!”

촤아아악.

입술 사이로 쏟아지는 핏물과 함께 균형을 잃고 비틀거리는 몸뚱어리.

끝끝내 내상을 감당하지 못하고 한쪽 무릎을 꿇은 노인의 모습에, 조금 전만 하더라도 웃으며 맞장구치던 나머지 두 노인이 경직된 얼굴로 중년인을 응시했다.

단 일 수(一手)만에 초절정 고수 하나를 거꾸러트린 그는, 천연덕스러운 표정으로 자신의 손과 쓰러진 노인을 번갈아 바라보고 있었다.

“이런, 힘이 너무 들어갔군. 이보게 삼노(三老), 괜찮나?”

무릎을 꿇은 채 핏물을 토해 내던 노인, 삼노가 숨을 헐떡이며 대답했다.

“괜찮, 괜찮습니다.”

“이거 참, 이럴 생각까지는 아니었는데…… 그보다, 어때?”

“그것이 무슨, 말씀이신지.”

반문하는 삼노를 향해, 중년인이 빙긋 웃어 보였다.

“화왕, 그 늙은이에 비하면 어떤가 물어본 걸세.”

“……!”

“왜, 영 아닐 것 같은가? 하기사 자네들도 화왕에 대해 잘 모르니 쉽게 답할 수 없겠군. 오래전 먼발치에서 한번 본 것이 전부였다고 했지 아마?”

세 명의 노인을 차례대로 훑어본 중년인이 입맛을 다시며 중얼거렸다.

“괜한 것을 물었군. 쥐새끼처럼 도망쳤으니 알 도리가 없겠지.”

피와 살 대신, 자존심과 자부심으로 이루어졌다는 무림인에게 이처럼 모욕적인 언사가 또 있을까.

그러나 세 노인, 천산삼노(天山三老)는 말없이 신형을 떨고 있을 뿐이었다.

치밀어오르는 분노를 삭이기 위해서?

틀렸다.

존재하지도 않는 것을 어찌 삭일 수 있단 말인가.

그들의 늙은 육신과 마음에, 중년인을 향한 분노는 없었다.

지금 이 순간 세 노인을 쇠사슬처럼 옭아매고 있는 감정은 바로 두려움이었다.

심기를 거스르는 말 한마디에 망설임 없이 살수(殺手)를 내뻗고, 마치 당장이라도 짓밟아 죽일 수 있는 개미를 대하는 듯한 표정과 말투.

눈앞의 중년인에게는 그럴 만한 힘과 자격이 있었다.

“부디 용서하여 주십시오!”

“소, 속하들이 부족한 탓입니다.”

“이 멍청한 늙은이가 그만 실언을 했습니다. 어찌 감히 화왕 따위가 마군(魔君)의 상대가 될 수 있겠습니까.”

한때 마교의 깃발 아래서 중원을 피로 물들였던 천산의 세 악귀는 앞다투어 부복할 수밖에 없었다.

이렇게라도 하지 않는다면 중년인, 혈검마군(血劍魔君)의 손에 당장이라도 죽임을 당할 것만 같았으니까.

그리고 그런 그들을 내려다보는 혈검마군의 눈동자에는, 명백한 조소가 서려 있었다.

‘한심한 것들 같으니. 고작 이런 놈들로 천하를 도모하려 했단 말인가.’

혈검마군의 비웃음은 비단 천산삼노에 국한된 것이 아니었다.

한때 그가 따랐던, 그의 전부나 다름없었던 한 사람을 향한 조소이기도 했다.

‘당신은 실패할 수밖에 없었소, 교주(敎主). 한낱 인간에 불과한 자가 스스로를 하늘에 빗대었으니.’

천마(天魔).

대대로 내려오는 그 칭호를 물려받아, 십만마도의 하늘이자 왕으로 군림했던 그를 떠올리며 혈검마군은 실소를 흘렸다.

이제와서 다시 생각해 보면, 실로 우스운 일이 아닐 수 없었다.

고작 그 정도의 인물을 믿고 충성을 바쳤다는 것이.

천 년에 달하는 기나긴 세월 동안 그 어떤 천마도 이루지 못했던 마도 천하를 꿈꾸었다는 것이.

하지만 이제는 다르다.

그는 실패를 통해 깨달음을 얻었고, 새로운 하늘을 받아들였다.

천주(天主)라 불리는 새로운 하늘을.

진정한 주인을.

그리고 지금 이 순간에도 서서히 가까워지고 있는 저 대설산의 적들도, 머지않아 자신과 함께 천주를 섬기게 되리라고 혈검마군은 굳게 믿고 있었다.

설령 저들이 격렬히 거부하고, 저항하고, 끝끝내 죽음을 택하더라도 이 결말은 달라지지 않을 것이다.

‘결국, 그분의 그늘에 몸을 의탁하게 될 터.’

잔잔한 웃음을 흘린 혈검마군은 문득 고개를 돌려 등 뒤를 바라보았다.

드득. 드드득.

서리 낀 초목(草木)을 짓밟으며 대설산을 향해 진군하는 수만의 대군.

그들의 선두에는 칠흑처럼 새카만 흑의를 걸친 일곱 명의 괴인과, 그에 상반되는 수십여 명의 백의인들이 있었다.

“자네들의 우려가 큰 듯하니, 내 한 가지 알려 주지.”

불현듯 입을 연 혈검마군은 천산삼노를 향해 천천히 말을 이었다.

“고작 화왕 따위로는, 결코 우리를 막을 수는 없어.”

이것은 자신감이 아니다. 확신이다.

옥문관을 넘을 때도, 종남파가 지키던 돈황을 단숨에 즈려밟았을 때조차도 내보이지 않았던 숨겨진 전력에 대한 확신.

물론 천산삼노 역시 그에 대해서는 어렴풋이 짐작하고 있었다.

과거 일세를 풍미했던 대마두인 그들조차 불길함을 느끼게 만드는 저들의 정체가, 결코 범상치 않으리라는 것 정도는.

하지만…….

‘도대체 뭐지?’

‘저들의 이름도, 별호도 알려 주지 않았다. 한데 어찌 저렇게 확신할 수 있단 말인가.’

‘어쩔 수 없다. 그저 따르는 수밖에.’

그저 조용히 의문을 삼킬 뿐.

감히 눈조차 마주치지 못하고 고개를 숙인 천산삼노의 모습에 작게 혀를 찬 혈검마군은, 이내 대설산에서의 첫 번째 명령을 내렸다.

“놈들에게 사자(使者)를 보내라.”

“사자라고 하신다면.”

“앞서 인사치레는 해 두었으니, 투항을 권유하는 자비 정도는 괜찮겠지. 그리고…….”

천산삼노는 이어질 말을 기다렸지만, 조용히 뒷말을 삼킨 혈검마군은 이내 빙긋 웃으며 내심 중얼거렸다.

‘꼭 보고 싶은 얼굴도 있고.’

과거의 적이자, 각기 다른 전장에서 각자의 목표를 위해 싸웠던 화왕 적천강을 뜻하는 것이 아니었다.

본격적인 전투가 벌어지기 전, 혈검마군이 마주하고 싶은 것은 구화산의 노괴가 아니라 그의 제자였다.

열화신룡(烈火神龍) 진태경.

도대체 무슨 이유에서인지, 자신의 주인에게 뜻 모를 관심을 받고있는 정파 무림의 젊은 거인.

만약 마주치게 되더라도 결코 죽여서는 안 된다는, 필요 이상의 명령을 받은 그 순간부터 혈검마군의 신경은 온통 그를 향해 쏠려 있었다.

‘어디 한번 볼까, 그만한 자격이 있는지.’

혈검마군의 두 눈동자가 형형하게 빛났다.



* * *



일백.

대설산의 척후조 일백 명 중, 단 한 사람의 예외도 없었다.

두 시진 전, 적들의 동태를 파악하기 위해 떠났다는 그들은 한 몸이 되어 돌아왔다.

말안장에 주렁주렁 매달린 수급(首級)으로.

“사, 사매.”

“안 돼. 안 돼!”

곳곳에서 비명과도 같은 외침이 울려 퍼진다.

척후조에 포함되어 있던 가까운 이들을 잃은 사람들은 슬픔과 분노를 토해 냈고, 잔인한 광경에 익숙해져 있던 화룡각 대원들조차 이를 악물었다.

“이건…….”

미처 말을 잇지 못한 채 파르르 떨리는 입술.

하지만 이런 상황일수록 냉정을 유지해야 하는 사람도 있다.

착 가라앉은 눈으로 수급을 살피던 나는 적천강과 시선을 교환했다.

“보셨어요?”

“그래, 모두 일검(一劍)에 베였다. 게다가 상흔이 전부 일정해.”

“그렇다는 건…….”

“한 사람이 소행이라는 뜻이지. 노부도 지금껏 몇 번 본 적 없는, 실로 무시무시한 검공(劍功)이다.”

죽음에는 흔적이 남는다. 그리고 척후조들의 수급에 난 단면은, 마치 자로 잰 것처럼 일정하면서도 예리했다.

적천강조차 저리 평가할 정도라면, 최소 십왕(十王)에 비견되거나 그 이상의 고수가 저들을 몰살시켰음이 틀림없었다.

“게다가 이건.”

문득 말을 멈춘 적천강이 눈살을 찌푸렸다.

“빌어먹을, 모르겠군. 분명 이와 비슷한 상흔을 어디서 본 것 같은데…….”

적천강은 고심을 거듭하며 기억을 더듬는 듯했지만, 나는 조용히 고개를 내저었다.

지금 중요한 것은 적의 정체가 아니다.

저 멀리에서 거대한 먼지구름을 피워올리며 다가오고 있는, 끔찍하리만치 많은 적들이었다.

아직 정확히 파악할 수는 없지만, 당장 언덕을 쏟아져 내려오는 숫자만 헤아려보아도 물경 이만.

족히 수백여 장이 떨어져 있었음에도 그 어마어마한 군세가 일제히 내뿜는 기세와 살기에, 척박한 대설산에서 살아가던 날짐승들조차 황급히 날갯짓을 하며 날아오를 정도였다.

“제기랄. 진짜였어. 내가 본 게 진짜였다고. 저 악귀들이 여기까지 오다니.”

반 인질이 되어 여기까지 끌려온 백마칠종(白馬七宗) 대형, 마중걸이 입술을 잘근잘근 씹으며 중얼거렸다.

벌벌 떨고 있는 그의 손에는 망원경, 아니 무림에서는 십리경(十里鏡)이라 불리는 물건이 들려 있었다.

“미친. 말로만 듣던 십만마도(十萬魔道)라니. 끝장이야. 이제 전부 다 끝장…….”

“주둥이 닥치쇼. 그쪽부터 끝장나기 싫으면.”

한 마디로 마중걸의 입을 다물게 만든 혁무진이, 그가 들고 있던 십리경을 빼앗으며 내게 속삭였다.

“조장님. 이제 어떻게 하실 생각이십니까?”

나는 담담한 목소리로 대답했다.

“알잖아. 어떻게 해야 하는지.”

놈들이 목전까지 치달은 이상, 남아 있는 선택지는 하나뿐이다.

전투.

아니, 혈투(血鬪).

한번 솟구친 불길은 온 들판을 다 불태우고 나서야 끝난다. 사막으로부터 시작된 암천이라는 불길은 대설산에 다다랐고, 우리는 그것에 맞서 맞불을 놓을 것이다.

‘그렇게 온 사방이 피로 물든 후에야 끝이 나겠지.’

물어본 혁무진도, 그 물음에 대답한 나도, 그리고 목숨을 건 대전투를 준비하는 대설산의 모두도 알고 있다.

또 다른 공통점은, 아무도 이 전투의 결말을 모른다는 것이다.

‘물론, 누군가는 이미 짐작할 수도 있겠지만.’

나는 저 멀리서 흑룡마문의 무인들을 진두지휘하는 사마공을 힐끗 바라보았다.

늘 침착하게 가라앉아 있던 평소와는 달리, 딱딱하게 굳은 얼굴로 산맥 아래를 응시하고 있는 사마표 역시도.

그리고 다음 순간 알게 되었다.

사마표의 얼굴이 굳어 있던 이유가, 전투의 긴장감 혹은 녀석이 감추고 있는 어떠한 비밀 때문이 아니었다는 사실을.

“온다.”

나직한 그 한마디에 고개를 돌린 나는 볼 수 있었다.

어느덧 언덕을 넘어 산밑을 새카맣게 물든 수만의 대군세를 가로질러 다가오고 있는, 새하얀 백기를 치켜세운 일단의 무리를.
```

## Final English reading copy

```markdown
# Chapter 1024

For martial artists who were always brushing up against death, hearing was an invaluable sense.

Sound could carry a great deal of information.

When you were facing an enemy, the whisper of a sleeve brushing past could only mean they were launching a sneak attack. And you could read someone’s state of mind from the pitch and tremor of their voice.

In other words, to a martial artist, sound was information.

And the drumbeats rolling in from far away at that very moment were no exception.

Thump. Thump-thump. Thuuump!

The rhythm was all over the place, and each beat rang out at a different volume.

An image came to the middle-aged man’s mind: somewhere in the snow-covered mountains, a drummer was pounding away with all his might, looking as if half his soul had already left his body. He scratched the back of his neck.

“Did we come on a little too strong with the welcome?”

Low laughter rippled through the group at his words.

By now, they weren’t the only ones who knew that the hundred scouts from the Great Snow Mountain they had encountered nearby two hours earlier were dead.

“Can you blame them? Their comrades, the people they shared meals with, came back as corpses overnight.”

“Looks like those horses came back with heads dangling all over them, and scared the daylights out of everyone. They don’t even know this is only the beginning.”

“Still, we mustn’t let our guard down either. We don’t know exactly how powerful the Fire King, that old monster, is…”

*Boom!*

A tremendous crash swallowed the rest of his words.

Before he could finish speaking, the old man felt an immense force slam into his chest. His body shot backward like a cannonball, but he righted himself in midair and landed on the ground.

Or tried to.

“Ugh, bleurgh!”

A spray of blood poured from his lips as he staggered, his balance gone.

At last, unable to withstand his internal injuries, the old man dropped to one knee. The other two elders, who had been laughing along with him just moments ago, stared at the middle-aged man with stiff faces.

The man who had felled a Supreme Peak master with a single move glanced back and forth between his hand and the fallen elder, his expression perfectly calm.

“Well, I put too much into that. Elder Three, are you all right?”

The old man—Elder Three—coughed up blood as he knelt and gasped for breath.

“I’m… I’m fine.”

“Good. I didn’t mean for it to come to that… Anyway, what do you think?”

“What… do you mean?”

The middle-aged man smiled faintly at Elder Three’s question.

“I’m asking how I compare to the Fire King, that old man.”

“……!”

“What, you think I don’t stand a chance? Well, you don’t know much about the Fire King either, so I suppose it’s hard to answer. You said you’d only seen him once, from a distance, a long time ago. Wasn’t that right?”

The middle-aged man looked over the three elders in turn, smacked his lips, and muttered.

“Shouldn’t have asked. You ran off like rats, so how would you know?”

Could there be a more humiliating thing to say to martial artists, who were said to be made of pride and confidence instead of flesh and blood?

And yet the three old men—the Three Elders of Tianshan—could only tremble in silence.

Were they trying to suppress the rage welling up inside them?

No.

How could you suppress something that didn’t exist?

In the old men’s bodies and hearts, there was no anger toward the middle-aged man.

The emotion binding them like chains at that very moment was fear.

He’d lashed out with a killing blow without hesitation over a single word that displeased him. His expression and tone made it seem as though he were looking at ants he could crush underfoot at any moment.

The middle-aged man before them had both the strength and the right to act that way.

“Please forgive us!”

“I-It’s because we’re lacking.”

“This foolish old man misspoke. How could someone like the Fire King ever be a match for the Demon Lord?”

The three fiends of Tianshan, who had once drenched the Central Plains in blood beneath the Demonic Cult’s banner, scrambled to prostrate themselves before him.

If they didn’t, they felt the middle-aged man—the Blood-Sword Demon Lord—might kill them on the spot.

Looking down at them, the Blood-Sword Demon Lord wore an unmistakable sneer.

*Pathetic fools. Had they really tried to conquer the world with the likes of these men?*

His scorn wasn’t limited to the Three Elders of Tianshan.

It was also directed at the one man he’d once followed, the man who had been everything to him.

*You were doomed to fail, Cult Leader. A mere human compared himself to Heaven.*

The Heavenly Demon.

Remembering the man who had inherited that title through the generations and ruled as the king and Heaven of the Hundred Thousand Demonic Disciples, the Blood-Sword Demon Lord let out a hollow laugh.

Thinking back on it now, it was truly ridiculous.

That he had pledged his loyalty to someone so ordinary.

That he had dreamed of a Demonic Path ruling the world—a feat no Heavenly Demon had achieved in a thousand years.

But things were different now.

He had gained insight through failure and accepted a new Heaven.

A new Heaven called the Lord of Heaven.

His true master.

And the Blood-Sword Demon Lord firmly believed that his enemies at the Great Snow Mountain, drawing nearer even now, would soon serve the Lord of Heaven alongside him.

Even if they refused fiercely, resisted, and chose death in the end, the outcome would be the same.

*In the end, they’ll seek shelter in that person’s shadow.*

With a quiet laugh, the Blood-Sword Demon Lord suddenly turned to look behind him.

*Crunch. Crunch.*

Tens of thousands of troops were marching toward the Great Snow Mountain, crushing the frost-covered plants underfoot.

At their head were seven strange figures clad in robes as black as night, and several dozen men in white, their appearance a stark contrast.

“Your concerns seem to be weighing on you, so I’ll tell you something.”

The Blood-Sword Demon Lord spoke without warning, then continued slowly, addressing the Three Elders of Tianshan.

“Someone like the Fire King could never stop us.”

This wasn’t confidence. It was certainty.

Certainty in the hidden strength they hadn’t revealed when crossing the Jade Gate Pass—not even when they trampled Dunhuang, defended by the Zhongnan Sect, in an instant.

Of course, the Three Elders of Tianshan had an inkling of it too.

Even they, fiends who had once dominated their age, could sense that there was nothing ordinary about the people whose identities filled them with dread.

But…

*What are they?*

*He hasn’t told us their names or titles. How can he be so certain?*

*There’s nothing we can do. We’ll just have to follow him.*

They could only quietly swallow their questions.

The Blood-Sword Demon Lord clicked his tongue softly at the sight of the Three Elders bowing their heads, unable even to meet his eyes. Then he issued his first command on the Great Snow Mountain.

“Send them a messenger.”

“A messenger, you say?”

“We’ve already given them a greeting. It’s only fair to show them the mercy of offering them a chance to surrender. And…”

The Three Elders waited for him to continue, but the Blood-Sword Demon Lord silently swallowed the rest of his words. Then he smiled faintly and thought to himself,

*There’s someone I’d very much like to see, too.*

He didn’t mean the Fire King, Jeok Cheongang, his former enemy, who had fought for his own goals on battlefields far from his.

Before the fighting truly began, the person the Blood-Sword Demon Lord wanted to meet wasn’t the old monster from Mount Jiuhua, but his Disciple.

The Blazing Flame Divine Dragon, Jin Taekyung.

For some reason, the young colossus of the orthodox Murim had drawn the attention of his master—the Lord of Heaven—in a way the Demon Lord couldn’t understand.

From the moment he’d received an order that went further than necessary, telling him not to kill Taekyung even if they met, the Blood-Sword Demon Lord’s thoughts had been fixed on him.

*Let’s see if he’s really worthy of all that.*

The Blood-Sword Demon Lord’s eyes shone brightly.

* * *

A hundred.

Not one person out of the Great Snow Mountain’s hundred-man scouting party had been spared.

They had left four hours earlier to check on the enemy’s movements. Now they’d returned as one.

Their heads hung from the saddles.

“J-Junior Sister…”

“No. No!”

Cries like screams rang out from all around us.

Those who had lost people close to them in the scouting party poured out their grief and rage. Even the Fire Dragon Pavilion members, who were used to gruesome sights, clenched their teeth.

“This…”

The speaker’s lips trembled, unable to finish the thought.

But in a situation like this, someone had to keep a cool head.

I studied the severed heads with a steady gaze, then exchanged a look with Jeok Cheongang.

“You saw it?”

“Yes. Every one was cut by a single sword strike. And the wounds are all identical.”

“So that means…”

“One person did it. A truly fearsome sword technique. I’ve only seen anything like it a few times in all my life.”

Death left its mark. The cuts on the scouts’ heads were so even and sharp they could have been measured with a ruler.

If even Jeok Cheongang judged it that way, then it had to be a master at least comparable to one of the Ten Kings—or someone even stronger—who had slaughtered them all.

“And this…”

Jeok Cheongang stopped mid-sentence and frowned.

“Damn it, I can’t place it. I’m sure I’ve seen a wound like this somewhere before…”

He seemed to be racking his brain, digging through his memories, but I quietly shook my head.

The enemy’s identity wasn’t what mattered right now.

It was the horrifying number of enemies approaching in the distance, raising a vast cloud of dust.

I couldn’t make out their exact numbers yet, but even just counting those pouring down the hill toward us, there were a staggering twenty thousand.

Though they were still several hundred *jang* away, the aura and killing intent pouring from that enormous army made even the wild birds living in the harsh Great Snow Mountain take frenzied flight.

“Damn it. It was real. What I saw was real. Those fiends made it all the way here.”

Ma Junggeol, chief of the Seven Masters of Baekma Bang, had been dragged here as something of a hostage. He chewed his lip and muttered to himself.

In his trembling hand was a telescope—no, in Murim, it was called a *siptiryeong*.

“Madness. The Hundred Thousand Demonic Disciples, just like I’d heard. We’re finished. It’s all over now…”

“Shut your mouth, unless you want to be the first one finished.”

Hyuk Mujin cut Ma Junggeol off with a single sentence, snatched the telescope from his hand, and whispered to me,

“Captain. What do you plan to do now?”

I answered evenly.

“You know what we have to do.”

With the enemy almost upon us, only one choice remained.

Battle.

No—a bloodbath.

Once a fire had taken hold, it didn’t end until it had burned the whole field. The fire called Dark Heaven had started in the desert and reached the Great Snow Mountain. We would meet it with a fire of our own.

*Once everything around us is drenched in blood, it’ll finally be over.*

Hyuk Mujin, who’d asked the question; me, who’d answered it; and everyone on the Great Snow Mountain preparing for a battle to the death—we all knew it.

There was one thing we didn’t know: how the battle would end.

*Of course, someone might already have a guess.*

I glanced at Sima Gong, directing the martial artists of the Black Dragon Demon Gate far away.

And Sama Pyo, too, who stood watching the mountainside with a rigid expression, unlike his usual calm.

The next moment, I understood.

The reason Sama Pyo’s face was so tense had nothing to do with the pressure of battle or some secret he was hiding.

“They’re coming.”

I turned at his quiet words and saw them.

A group was approaching, carrying a pure white banner raised high as it crossed the tens of thousands of troops who had crested the hill and blackened the foot of the mountain.
```

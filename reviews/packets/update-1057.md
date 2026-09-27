<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1057.txt",
      "sha256": "9b71ebf4cefe5df75a919325d4b8a0ede65a632e47d35df82f0b047f9a2badfd",
      "bytes": 13347
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "ef940d403faf1058543999870135f6d3efb80690c2df0973525b8977991d5394",
      "bytes": 1027
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "5928ba5f9f942187d5c6e9149eb7593670dc2db24724f7fc8e9018bc095627ca",
      "bytes": 240988
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "4491bca1ca6da3ab3a8ea9297ec92b3f9e5d42d8a5b01df3d600d7cf05b3b411",
      "bytes": 760
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "ba5c1363280e8115177c1b62ddfbe30c29e3878970719f9f0a256c5a9aa3af47",
      "bytes": 1828
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "27c637c1a52266106fc538ddc9b9dbe66e2374f538e9d5224e7b41b2cd5d2f8a",
      "bytes": 623
    },
    {
      "path": "characters/Namho.md",
      "sha256": "afa96e4a51abbf82fcaca5c884713c20c5699679f0a90bf1cbd88234287ff2da",
      "bytes": 1092
    },
    {
      "path": "characters/Sama Pyo.md",
      "sha256": "f47dfc83569ebcaa57246c00dab6d25bdfbad2321497441ebc10b9ef65aaa082",
      "bytes": 986
    },
    {
      "path": "characters/Sima Gong.md",
      "sha256": "b731b37472e1799ccd202938ade582522856db14884bc6f198ba0dbd7e0dfb06",
      "bytes": 877
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "08b6cfb5e3ddecd8eb9f37691e6b1de110c70b0ffbeca8249feb2cddf5774d9e",
      "bytes": 686
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "378d7aefdd54ea7c974a9b9e4024a94e31cc9cf3b9d4e85ce7257e2497dfa904",
      "bytes": 282320
    }
  ],
  "estimated_tokens": 11257
}
-->

# Durable State Update — Chapter 1057

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
1 and safe_through 1057. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1057. Profile updates may replace only one
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
  "chapter": 1057,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1057,
    "continuity_sources": [1057],
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
    "Sima Gong is dead; Sama Pyo intends to disclose his father’s betrayal and accept responsibility for having concealed it.",
    "Taekyung was near collapse while fighting the remaining Dark Heaven cultists when his allies and Sama Pyo arrived to help.",
    "The Lord of Heaven’s identity and connection to Asmodeus remain unknown; a mysterious green light remains in the dispersing darkness.",
    "Some Kongtong Sect survivors vanished to an unknown location.",
    "The Grand Mage departed for Qinghai on a new mission; the identity of the other servant remains unknown."
  ],
  "continuity_sources": [
    1056
  ],
  "open_questions": [
    "What are the identity and purpose of the Lord of Heaven, and is he connected to Asmodeus?",
    "Where did the missing Kongtong Sect survivors go?",
    "What is the new mission in Qinghai, and who is the other servant there?",
    "What is the mysterious green light?"
  ],
  "safe_through": 1056,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 사마공    | **Sima Gong**      |
| 태원진가   | **Jin Family of Taiyuan**        |
| 암천     | **Dark Heaven**                  |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 살기     | **killing intent**                               |                                                       |
| 문주     | **Sect Leader**                              |
| 소문주    | **Young Sect Leader**                        |
| 장문인    | **Sect Leader**                              |
| 제자     | **Disciple**                                 |
| 장비               | **Equipment**                  |
| 태원     | **Taiyuan**            |
| 감숙     | **Gansu**              |
| 도사      | **Daoist**                                                      |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 남호 | **Namho** | Hidden Shadow Pavilion code name; literally associated with amber from the south. |
| 사마표 | **Sama Pyo** | Young Sect Leader of the Black Dragon Demon Gate. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 야왕 | **Night King** | Rumored epithet for Jin Taekyung in Taiyuan's red-light district. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 기해 | **qi sea** | Name for the dantian, the place where internal energy begins and gathers. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 은영각 | **Hidden Shadow Pavilion** | Former Murim Alliance intelligence organization. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 마공 | **demonic martial arts** | Martial arts that appear to defy common principles. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 흑룡마문 | **Black Dragon Demon Gate** | Unorthodox faction from Gansu. |
| 공동파 | **Kongtong Sect** | Sect belonging to the Nine Sects and One Gang. |
| 흑야왕 | **Black Night King** | Epithet of Sima Gong, Sama Pyo's father and the Sect Leader who built the modern Black Dragon Demon Gate. |
| 화룡각 | **Fire Dragon Pavilion** | New name chosen for Taekyung's pavilion. |
| 고든 | **Gordon** | Pentagon employee tasked with repairing smashed warning lights. |
| 변이 | **mutation** | The transformation threatening the humans and beasts in the Inner Palace. |
| 금의위 | **Embroidered Uniform Guard** | Imperial guard force mentioned by Hong Jin. |
| 종남 | **Zhongnan Sect** | Orthodox faction that fought in the historic battle. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 거한 | 사마표 | Subordinate addressing the Black Dragon Demon Gate Young Sect Leader | Young Sect Leader | Crude and deferential | Uses 소문주 in short, childlike replies. |
| 사마표 | 거한 | Young Sect Leader addressing his giant subordinate | This fellow | Informal and patronizing | Refers to him as 이 녀석 while assigning him responsibility for Do Sangho's death. |
| 사마표 | 태산 | Young Sect Leader to subordinate | Taishan | informal and patronizing | Sama Pyo calls Taishan by name while ordering him to leave. |
| 태산 | 사마표 | subordinate to Young Sect Leader | Lord | crude and deferential | Taishan uses 주군 while obeying Sama Pyo. |
| 태산 | 진태경 | subordinate_to_respected_outsider | Jin Taekyung | clipped and familiar | Taishan says he likes Jin Taekyung but will fight him without hesitation if Sama Pyo commands it. |
| 사마표 | 진태경 | prospective recruit to pavilion master | you | polite, controlled, and candid | Sama Pyo uses 자네 while asking about Taekyung's attitude and admitting his intention to use him. |
| 진태경 | 사마표 | pavilion master to prospective recruit | you / that guy | blunt, informal, and distrustful | Taekyung speaks to and about Sama Pyo with casual forms such as 녀석 and 저놈. |
| 남호 | 진태경 | Hidden_Shadow_Pavilion_agent_to_mission_leader | Jin Taekyung / you | guarded and familiar | Namho addresses Taekyung as 자네 while explaining the contact and offering guidance. |
| 진태경 | 남호 | mission_leader_to_hidden_shadow_agent | you / Namho | probing and respectful | Taekyung questions Namho’s affiliation and later discusses Dark Heaven’s threat to Nanman. |
| 남호 | 태산 | guide_to_pavilion_member | Taishan | blunt and exasperated | Namho directly rebukes Taishan for eating the poisonous blood-feeding fungus. |
| 남호 | 사마표 | guide_to_young_sect_leader | Young Sect Leader | blunt and admonishing | Namho warns Sama Pyo that all grass and animals in the territory belong to the Nanman Beast Palace. |
| 사마표 | 남호 | young_sect_leader_to_guide | Elder Namho | formal and apologetic | Sama Pyo apologizes after Taishan attempts to seize the calf. |
| 진태경 | 태산 | pavilion_master_to_pavilion_member | Taishan | forceful and commanding | Taekyung orders Taishan to stop eating the bear. |
| 태산 | 남호 | Fire Dragon Pavilion member to guide | Namho | clipped, childlike, and informal | Taishan directly addresses Namho while asking what Dark Heaven is. |
| 남호 | 각주 | guide to pavilion master | Pavilion Master | blunt, hostile, and abusive | Namho addresses Jin as 각주 while accusing him of causing the disturbance. |
| 사마표 | 각주 | Fire Dragon Pavilion member to pavilion master | Pavilion Master | formal but sardonic | Sama Pyo addresses Jin as 각주 while questioning his account of the incident. |
| 태산 | 각주 | Fire Dragon Pavilion member to pavilion master | Pavilion Master | clipped, childlike, and informal | Taishan directly asks Jin whether his Lord Sama Pyo is safe. |
| 신의 | 태산 | senior physician to younger ally | Young Hero Taishan | urgent and respectful | The Divine Physician uses this address while pleading with Taishan to keep moving. |
| 진태경 | 사마공 | allied young martial artist to unorthodox sect leader | Great Hero Sima | polite and deferential | Addresses him as 사마 대협. |
| 사마공 | 진태경 | unorthodox sect leader to celebrated young martial artist | you | polite and familiar | Uses 자네 while speaking to Taekyung. |
| 사마공 | 사마표 | father to son | Pyo | intimate and familiar | Sima Gong calls him 표야 and 내 아들아. |
| 사마표 | 사마공 | son to father | you; Father | familiar and confrontational | Sama Pyo challenges his father during their battlefield confrontation. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1056
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1055
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan and the original owner of his current body, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master who has reached the realm of the Ten Kings as its eleventh member and can detect and eavesdrop on nearby Sound Transmissions subject to the participants’ relative levels, and a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure, willing to risk himself for others, and fiercely defiant when others try to dictate his choices or survival.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; Hyuk Mujin trusts Taekyung to fight beside him; Taekyung trusts Sama Pyo as a friend despite suspecting his betrayal, and values him beyond his unorthodox affiliation; Peng Cheolhu regarded Taekyung as a worthy successor, and the Bow Saint relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1055
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Namho.md

# Namho (남호)

- **Safe through:** Chapter 1056
- **Aliases:** Elder Chao
- **Role:** Namho is an eighty-year-old non-Han Hidden Shadow Pavilion agent who spent more than fifty years undercover in Nanman and maintained contact with Central Plains intelligence through the Pavilion’s Hidden Thread; he guides the Fire Dragon Pavilion and represents Jin Taekyung and the Murim Alliance in negotiating the survivors’ chance to rebuild the Murong household.
- **Personality:** Duty-bound, pragmatic, and observant; uses theatrical violence to protect intelligence work and takes a veteran’s concern for the younger generation’s resolve.
- **Voice:** Measured and reflective when advising the younger generation, loudly abusive when maintaining his local cover, and capable of theatrical boasts and dry humor.
- **Relationships:** Namho is a Hidden Shadow Pavilion contact for Jin Taekyung and the Fire Dragon Pavilion, receives intelligence from the Pavilion Master, and knows the code used by the Thousand-Faced Fox.

### Sama Pyo.md

# Sama Pyo (사마표)

- **Safe through:** Chapter 1056
- **Aliases:** Black Dragon Saber
- **Role:** Young Sect Leader and heir of the Black Dragon Demon Gate, a Morning Star reputed to be no less than the Ten Dragons and Phoenixes.
- **Personality:** Courteous and calculating, he chooses what he believes is right over expedience and accepts responsibility for his choices, even when they expose him to blame.
- **Voice:** Polite and ingratiating in public, with sardonic humor and controlled evasiveness.
- **Relationships:** Sama Pyo is Sima Gong’s son and chosen heir; he returned to stay with his dying father rather than kill him, and intends to disclose his father’s betrayal and bear responsibility for having concealed it. He commands the absolutely loyal Taishan, admires Jin Taekyung, was Ju Hwaran’s former fiancé in a political engagement, and is openly hostile toward fellow member Song Ilseom.

### Sima Gong.md

# Sima Gong (사마공)

- **Safe through:** Chapter 1056
- **Aliases:** Black Night King
- **Role:** Sima Gong is the Sect Leader who built the Black Dragon Demon Gate into a major unorthodox power and the father of its Young Sect Leader, Sama Pyo.
- **Personality:** Sly and calculating yet capable of risking himself for a moment of conscience, he values his heir’s future and repaying a debt to Jeok Cheongang.
- **Voice:** Polished and persuasive, with smooth rhetorical turns and a composed, gently teasing manner.
- **Relationships:** Sama Pyo is his youngest son among seven older brothers and nine older sisters; Sima Gong chose him as heir and approved his plan to answer the Gate’s betrayal. Sama Pyo returned to remain with him as he died. Sima Gong aided Jeok Cheongang despite their history.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 1056
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo; becomes explosively violent when his meat is threatened.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord, trusts Jin Taekyung as Pavilion Master, and has grown attached to the Fire Dragon Pavilion members.

## Korean source

```text
1057화




광활한 설원을 둘러싼 그날의 대혈투에서, 더 이상의 이변(異變)은 일어나지 않았다.

불과 몇 시진 전까지만 하더라도 압도적인 위용을 뽐내던 암천의 군세는 바람 앞의 촛불이나 다름없었고, 초절정 고수들과 잇따른 지원군을 앞세운 연합군은 거대한 폭풍과도 같았다.

모든 것을 찢어발기며 나아가는, 살의와 강철로 이루어진 폭풍.

콰드드득!

푸푸푹! 서걱!

사방에서 터져 나오는 피 분수.

자욱한 피 안개를 망토처럼 두른 채, 닥치는 대로 눈앞의 적을 찌르고 베며 돌격하는 연합군의 손속에는 조금의 망설임도 깃들어 있지 않았다.

눈에는 눈.

이에는 이.

그리고 죽음에는 죽음으로 되갚는 것이야말로 이 세상의, 무림(武林)의 법칙이자 전쟁의 본질이었으니까.

“천상천하, 만마…….”

퍼걱!

관병이 내지른 창날이 팔을 찌르고, 어디선가 날아온 화살이며 검이 얼굴과 가슴을 난도질한다.

여덟 글자의 교언(敎言)을 끝맺기도 전에 피를 흩뿌리며 쓰러지는 적들의 시신들을 짓밟으며, 연합군은 이 거대한 도살장의 울타리를 좁혀 갔다.

빠르고, 격렬하게.

이지를 상실한 암천의 교도들을 상대로 회유나 생포라는 단어는 사치였고, 오늘 이 자리에서 연합군이 치러야 했던 막대한 희생은 자비를 잊게 만들었다.

가장 마지막에 합류했으나, 가장 앞장서서 적진을 휩쓸고 있는 일단의 무리에게는 더더욱.

쉬쉬쉬쉭!

피에 젖은 도포 자락이 흩날린다.

마치 목숨을 도외시한 듯이 단숨에 적진의 중심으로 파고드는 그들의 움직임은 바람처럼 표홀했고, 무리의 선두에 선 노인의 검을 타고 솟구친 검광(劍光)은 잔인하리만치 눈부셨다.

콰아앙!

거대한 폭음이 대지를 떨쳐 울린다.

본래의 형태를 잃어버린 살점과 핏물이 사방으로 튀었다.

강기(罡氣)가 스쳐 지나간 그 자리에는 아무것도 남아 있지 않았다.

있다면 오직 피와 죽음.

더불어, 흐트러진 적들의 전열(戰列)을 완전히 짓뭉개며 들이닥친 연합군의 거대한 함성만이 있을 뿐.

“와아아아아!”

“돌격! 돌격하라!”

“한 놈도 살려 두지 마라!”

지금 이 순간, 연합군은 제각각 다른 색을 지닌 하나의 파도나 다름없었다.

극심한 혼전 속에서도 냉철함을 잃지 않고 오와 열을 맞춰 돌격하는 금의위.

마지막 힘을 쥐어 짜내어 그들의 뒤를 따르는 감숙의 관군과 무림인들.

그리고 처음과 달리 수가 확연히 줄어든 종남의 제자들과, 어느 순간 불현듯 나타나 연합군에 합류한 정체불명의 기마인(騎馬人)들까지도.

두두두두!

마치 지진이라도 난 것처럼 뒤흔들리는 지축.

귀를 먹먹하게 만드는 함성은 끝없이 울려 퍼졌고, 온 사방을 빽빽하게 메운 강철의 숲은 침략자들을 뒤덮으며 무수한 꽃과 가지를 피워 올렸다.

피와 뼈로 이루어진 붉은 꽃과 새하얀 가지를.

그것이 이 길고도 잔혹했던 대전투의 끝이었다.

반나절의 시간이 더 흘렀을 때, 물경 삼만을 아우르던 암천의 교도 중 자신의 의지로 전장에 서 있는 자는 아무도 없었다.

단 한 사람도.



* * *



현대의 군사 용어에서 전멸이란 곧 전투 역량의 상실을 뜻한다.

병력, 장비, 보급, 사기 등.

통상 삼 할 이상의 전투원이 죽거나 다친 상황에서 살아남은 전투 병력의 의지가 흔들린다면, 전투를 계속 이어 갈 수 없다는 판단하에 곧 전멸로 간주하는 것이다.

하지만 이곳 무림에서는, 지금 이 순간 진태경의 눈앞에 펼쳐진 광경은 달랐다.

전멸(全滅).

단어에 담긴 뜻 그대로다.

아니, 어쩌면 전멸이라는 두 글자로도 모든 것을 표현할 수 없을지 모른다.

살육, 학살.

혹은.

‘……도살(屠殺).’

차마 토해 내지 못한 그 단어가 혀끝에서 맴돈다. 진태경은 깊게 가라앉은 눈빛으로 주위를 둘러보았다.

붉다. 시야에 들어온 모든 것이 붉게 물들어 있다.

새하얗던 눈밭도, 눈을 부릅뜬 채 피 웅덩이에 잠겨 있는 시신들의 얼굴도.

그리고 강이 되어 흐르는 핏물과 시체의 산을 헤집으며, 기적처럼 살아남은 적들을 찾고 있는 핏발 선 눈동자들도.

푸욱!

거칠게 떨어져 내린 검신이 수많은 시체의 틈바구니에서 꿈틀거리던 적의 가슴을 파고든다.

기적은 두 번 일어나지 않았고, 한번 살아남은 것은 오히려 불행이나 다름없었다.

만약 진즉 숨이 끊어졌다면, 훨씬 더 빠르고 평온한 죽음을 맞이할 수 있었을 테니.

콰드득.

몸속 깊숙이 파고든 날붙이가 천천히 비틀린다.

뼈와 살이 짓이겨지는 그 끔찍한 소리에, 더불어 그보다도 더욱 선명하게 느껴지는 살의(殺意)에 진태경의 곁에 있던 화룡각 대원들의 얼굴이 딱딱하게 굳었다.

“조장님.”

“아무리 그래도 이건…….”

진태경은 손을 들어 이어지려는 뒷말을 막아 세웠다.

안다. 이들이 무슨 말을 하고자 하는지.

이건 살인이 아니다. 가축을 처리하는 것과 같은 도살이다.

그러나 동시에, 저항할 힘조차 없는 적에게 저토록 잔인한 최후를 내리는 이들의 심정 또한 충분히 이해할 수 있었다.

“이곳에서 대기해.”

화룡각 대원들에게 그 한마디를 툭 던진 진태경은 천천히 발걸음을 옮겼다.

한 걸음. 또 한 걸음을 내디딜 때마다 견딜 수 없는 피로가 밀려왔지만, 어디에선가 불쑥 뻗어 나온 누군가의 손길이 비틀거리는 신형을 부축했다.

“분명히 대기하라고 했던 것 같은데.”

혼잣말처럼 흘러나온 진태경의 뇌까림에, 사마표가 어깨를 으쓱해 보였다.

“글쎄, 그런 말은 듣지 못해서.”

“지금이라도 들었으니까 뒤로 물러나.”

“그럴 수는 없지.”

“명령이야.”

“명령이라, 결국 그렇게 나오겠다는 건가?”

“그래.”

진태경의 음성은 그 어느 때보다 단호했고, 그것은 뒤이어 울려 퍼진 사마표의 대답 역시 마찬가지였다.

“좋아, 그렇다면 나는 지금 이 시간부로 화룡각을 떠나겠네.”

“……!”

일순간 눈을 크게 뜬 진태경을 향해, 사마표는 흐릿하게 웃어 보였다.

“왜, 이건 예상치 못했나 보지?”

“……너.”

“그동안 즐거웠네, 각주. 하지만 우리가 함께하는 것도 여기까지야.”

사마표는 담담한 시선으로 진태경을 응시하며 덧붙였다.

“더 이상 자네나 다른 이들에게 누를 끼칠 수는 없어. 어떤 결과가 기다리고 있건 간에, 그건 오직 나 홀로 감내해야 하는 일이겠지.”

그는 알고 있었다.

오래전부터 한계에 다다라 있던 진태경이 왜 지금까지도 의식의 끈을 부여잡고 있는지.

그리고 지금부터 자신이 홀로 걸어가야 하는 이 길 끝에, 얼마나 큰 위험이 도사리고 있는지.

그럼에도 지금처럼 침착한 모습을 보일 수 있는 이유는, 이미 마음의 결정을 내렸기 때문이었다.

“설령 그 어떤 상황이 벌어지더라도 나서지 말게. 그리고 만에 하나 내게 문제가 생긴다면…….”

흐려지는 말꼬리와 함께, 사마표의 시선이 문득 태산을 향한 바로 그 순간이었다.

그런 그를 물끄러미 지켜보던 진태경이 한마디를 툭 내던진 것은.

“싫은데?”

“뭐?”

“싫다고, 새꺄. 네 사람은 네가 챙겨. 가뜩이나 고생하는 사람한테 짬 때릴 생각 하지 말고.”

잠시 말문이 막혀 있던 사마표는, 이내 진태경의 말에 담긴 의미를 깨닫고 피식 실소를 흘렸다.

“맞는 말이야. 저 녀석만큼은 내가 끝까지 책임져야지. 반드시.”

그럴 수 있다면, 네 말대로 살아남을 수만 있다면.

끝끝내 내뱉지 못한 뒷말을 조용히 삼키며, 사마표는 홀로 걸음을 내디뎠다.

그리고 그런 사마표의 뒷모습을 말없이 바라보던 진태경은 불현듯 입을 열었다.

“갑자기 궁금해진 건데…… 우리가 태원진가를 떠나던 날, 혹시 기억나냐?”

당연했다.

몇 년이나 몇 달도 아닌, 불과 달포 남짓밖에 되지 않은 최근의 일이었으니까.

더불어 충분히 짐작할 수 있었다.

진태경이 왜, 무슨 이유로 이런 이야기를 꺼냈는지.

“물론. 서쪽으로 출발하기 직전, 남 노인과 태산이 직접 나를 찾으러 왔었지.”

그날 밤, 사마표는 감숙에서 보내온 밀서(密書)를 읽고 있었다.

이미 보고, 또 보았음에도 몇 번이나 반복해서.

두 사람의 인기척이 문 앞까지 다가올 때까지도.

“평소에는 칼같이 시간을 지키더니, 그날따라 늑장을 부렸더라. 꼭 누가 찾아오기를 기다리는 사람처럼.”

혼잣말처럼 뇌까리는 진태경의 음성에, 사마표는 문득 걸음을 멈추었다.

“그냥, 그날따라 생각할 게 많더군.”

“남 노인은 늙었지만 훌륭한 요원이야. 나이에 비해 후각도 예민하고.”

“그래, 그에 반해 귀는 어두워서, 목청도 크지.”

걷기만 해도 땅이 울리는 구척장신의 거한과 말 많고 목청 좋은 노인의 조합.

어디에서나 눈에 띄고, 잘 들릴 수밖에 없다.

그리고 그것은 그날 밤, 처소에 홀로 남아 밀서를 읽고 있던 사마표에게도 마찬가지였다.

“의도했던 거지? 처음부터.”

“아니. 전혀.”

거짓말이었다. 새빨간.

사마표는 그곳에서 기다리고 있었다.

누구보다 먼저 자신을 찾으러 올 가장 오래된 친구를.

아니, 그런 태산과 단짝처럼 붙어 다니는 은영각의 늙은 요원을.

동시에, 내심 바라고 있었다.

자신의 입으로는 말할 수 없는 비밀을, 남호가 조금이라도 알아차려 주기를.

이로 말미암아 경계해 주기를.

“왜, 어째서 그렇게까지?”

등 뒤에서 들려오는 진태경의 나직한 물음에, 사마표는 잠시 멈추었던 발걸음을 내디뎠다.

“그래도…… 내 아버지니까.”

어떻게 해서든 마지막까지 믿고 싶었다.

그러나 이 믿음이 배반당했을 때, 곁에 있는 이들을 위험에 빠트리기 싫었다.

하여 일부러 경고의 의미로 단서를 남겼다.

아들이 아버지의 수상한 움직임을 밀고하기 전에, 그들이 자연스럽게 의심을 품을 수 있도록.

설령 사마표 자신 또한 그 의심의 대상이 될지라도, 모두의 신변이 안전해질 수 있다면 상관없었다.

의심당하고, 미움받는 것에는 익숙해져 있었으니까.

흑야왕 사마공의 혈육으로, 흑룡마문의 소문주로 산다는 것은 그런 의미였으니까.

하지만 참으로 이상한 일이었다.

언젠가부터 그를 바라보는 남호의 시선이 날카롭고 깊어진 이후에도, 진태경은 일언반구조차 없었다.

지금 이 순간까지도.

“그러는 자네는, 왜 끝까지 내게 아무것도 묻지 않았나?”

줄곧 뇌리에 맴돌던 의문을 입밖으로 꺼낸 바로 다음 순간.

한 치의 망설임도 없이 등 뒤에서 울려 퍼진 짧은 대답에, 사마표의 가슴 한구석이 찌르르 울렸다.

“그래도, 친구니까.”

“……!”

“시벌, 모르겠다. 분명히 겉모습만 보면 칙칙하고 시커먼 놈인데…… 계속 믿고 싶더라고. 점점 개판이 되어 가는 상황에서도 그러고 싶더라고, 내가.”

사마표는 아무 말도 하지 못했다.

그저 뜨거워지는 눈시울을 억누르기 위해 이를 악물고, 흔들리는 발걸음을 재차 옮길 뿐이었다.

어느샌가 퍽 멀어져 버린, 진태경의 마지막 음성을 들으며.

“죽지 마라. 이건 명령이야.”

그 어느 때보다 부드러운 명령에, 사마표는 대답하지 않았다.

그리고 지금 이 순간에도 처참한 전장을 돌아다니며, 살아남은 적들을 도살하는 일단의 무리를 향해 계속해서 걸음을 옮겼다.

아니, 정확히는 그들의 중심에 서 있는 한 노인을 향해.

철벅.

마침내 우뚝 선 발걸음과 함께 출렁이는 피 웅덩이.

사마표는 크게 심호흡했다. 헛구역질이 치밀어 오를 정도의 악취와 피비린내가 콧속 깊숙이 스며들었지만, 그의 마음은 되레 차분하고 잔잔했다.

속을 읽을 수 없을 만큼 깊게 가라앉은 눈빛으로, 눈앞에 멈춰 선 원수의 자식을 바라보는 어느 노인의 표정처럼.

“무림말학 사마표, 대 공동파(崆峒波)의 장문인을 뵙습니다.”

그 순간.

스아아아.

끔찍하리만치 거대한 살기(殺氣)가, 온 사방에서 솟아올라 사마표의 전신을 짓눌렀다.
```

## Final English reading copy

```markdown
# Chapter 1057

No further surprises occurred in the great battle that day across the vast snowfield.

Just a few hours earlier, the forces of Dark Heaven had flaunted their overwhelming might. Now they were no more than candles before the wind, while the allied forces—led by Supreme Peak masters and wave after wave of reinforcements—were like a tremendous storm.

A storm made of steel and killing intent, tearing through everything in its path.

*Crraack!*

*Thud! Shhk!*

Fountains of blood erupted all around them.

With thick blood mist draped over them like cloaks, the allied soldiers charged, stabbing and cutting down every enemy in their path without the slightest hesitation.

An eye for an eye.

A tooth for a tooth.

And death repaid with death. That was the law of this world—the Murim—and the very essence of war.

“Heaven above and earth below, all demons—”

*Thwack!*

A guard’s spear pierced his arm. Arrows and swords flying from somewhere slashed through his face and chest.

Before they could finish their eight-character doctrine, the enemies fell, spraying blood. The allied forces trampled over their bodies and closed in around the enormous slaughterhouse.

Quickly. Ferociously.

Against Dark Heaven’s cultists, who had lost their reason, words like *persuasion* and *capture alive* were luxuries. The immense sacrifices the allied forces had made here today had left them with no mercy to spare.

Least of all the band of fighters who had joined last, yet were now sweeping through the enemy ranks at the very front.

*Shh-shh-shhk!*

Blood-soaked robes fluttered in the wind.

They plunged straight into the heart of the enemy lines as if they didn’t care whether they lived or died. Their movements were as elusive as the wind, and the sword light that surged along the blade of the old man at their head was cruelly dazzling.

*Boom!*

A thunderous blast shook the earth.

Chunks of flesh, no longer recognizable as such, and blood flew in every direction.

Where the Force had passed, nothing remained.

Nothing but blood and death.

And the tremendous roar of the allied forces as they crashed into the enemies’ broken formation and crushed it completely.

“Waaah!”

“Charge! Keep charging!”

“Don’t leave a single one alive!”

In that moment, the allied forces were one wave, though each part had a different color.

The Embroidered Uniform Guard charged in ranks, keeping their composure amid the chaos.

The soldiers and martial artists of Gansu followed behind them, squeezing out their last strength.

Then there were the Zhongnan Sect Disciples, whose numbers had dwindled drastically since the start—and even the mysterious mounted fighters who had suddenly appeared and joined the allied forces.

*Thud-thud-thud-thud!*

The ground trembled as if an earthquake had struck.

Their deafening shouts echoed without end. The forest of steel packed across the land engulfed the invaders, blooming with countless flowers and branches.

Red flowers made of blood and bone, white branches made of bone.

That was the end of the long, brutal battle.

Another half day passed. Of the fully thirty thousand Dark Heaven cultists, not one still stood on the battlefield of his own will.

Not one.



* * *



In modern military terminology, annihilation means the loss of combat effectiveness.

Troops, equipment, supplies, morale, and so on.

Generally, when at least thirty percent of a fighting force has been killed or wounded and the surviving troops’ will falters, they’re judged incapable of continuing to fight—and are considered annihilated.

But here in the Murim, what lay before Jin Taekyung at this very moment was different.

*Annihilation.*

The word meant exactly what it said.

No, perhaps those two characters still couldn’t express the whole thing.

Killing. Massacre.

Or…

*…Slaughter.*

The word I couldn’t bring myself to say lingered on the tip of my tongue. I looked around, my gaze heavy.

Red. Everything in sight was stained red.

The once-white snowfield. The faces of the corpses submerged in pools of blood, eyes wide open.

And the bloodshot eyes searching for enemies who might have survived, probing through rivers of blood and mountains of corpses.

*Shhk!*

The sword that came down hard pierced the chest of an enemy writhing among the countless corpses.

A miracle wouldn’t happen twice. If you survived once, it was practically a misfortune.

Had his life ended sooner, he could have met a much quicker, more peaceful death.

*Craack.*

The blade buried deep inside him slowly twisted.

At the dreadful sound of bone and flesh being crushed—and the killing intent, even more vivid than the sound—the faces of the Fire Dragon Pavilion members beside me stiffened.

“Captain.”

“Even so, this is…”

I raised a hand to stop them before they could finish.

I knew what they wanted to say.

This wasn’t murder. It was slaughter, like butchering livestock.

At the same time, Taekyung understood the feelings of those giving such a cruel end to enemies who no longer had the strength to resist.

“Wait here.”

I tossed the words to the Fire Dragon Pavilion members and slowly started walking.

One step. Then another. With each step, unbearable fatigue washed over me. But someone’s hand reached out from somewhere and steadied my swaying body.

“I believe I told you to wait.”

At my mutter, which came out almost as if I were talking to myself, Sama Pyo shrugged.

“Did you? I don’t remember hearing that.”

“You’ve heard it now. Step back.”

“I can’t do that.”

“That’s an order.”

“An order? So that’s how you’re going to play it?”

“Yeah.”

My voice was firmer than ever. Sama Pyo’s reply, which rang out a moment later, was just as firm.

“Fine. Then as of this moment, I’m leaving the Fire Dragon Pavilion.”

“……!”

I stared at him, eyes widening. Sama Pyo gave me a faint smile.

“What? Didn’t see that coming?”

“You…”

“I’ve enjoyed our time together, Pavilion Master. But this is where we part ways.”

He met my gaze calmly and added, “I can’t keep dragging you or anyone else into this. Whatever comes, I have to face it alone.”

He knew.

He knew why I was still clinging to consciousness when I’d been on the verge of collapse for a long time.

And he knew how great the danger waiting at the end of the road he now had to walk alone might be.

Even so, he could remain so calm because he had already made up his mind.

“Whatever happens, don’t get involved. And if something should happen to me…”

His voice trailed off as his gaze shifted to Taishan.

Taekyung, who had been watching him, cut in.

“Nope.”

“What?”

“I said no, asshole. Look after your own man. Don’t dump him on someone who’s already got enough on his plate.”

Sama Pyo fell silent for a moment. Then he understood what Taekyung meant and gave a short laugh.

“You’re right. I have to look after him to the very end. No matter what.”

*If I can. If I can survive, like you said.*

Swallowing the words he could not bring himself to say, Sama Pyo set off alone.

Taekyung watched him go, then suddenly spoke.

“Something just occurred to me… Do you remember the day we left the Jin Family of Taiyuan?”

Of course he did.

It had been recent—not years or months ago, but barely more than a month.

And he could guess well enough why I’d brought it up.

“Of course. Right before we left for the west, Elder Namho and Taishan came looking for me themselves.”

That night, Sama Pyo had been reading a secret letter from Gansu.

He had already read it, then read it again—over and over.

Even as the two men’s footsteps approached his door.

“You’re usually punctual to the second, but that day you dragged your feet. Like someone waiting for a visitor.”

At my mutter, Sama Pyo abruptly stopped walking.

“I had a lot on my mind that day.”

“Elder Namho’s old, but he’s a fine agent. His nose is pretty sharp for his age, too.”

“True. Though his hearing’s bad, so he talks loudly.”

A giant nearly nine feet tall who made the ground shake just by walking, and an old man who talked a lot and had a booming voice.

They stood out wherever they went, and you couldn’t help hearing them.

That had been true for Sama Pyo, too, alone in his quarters that night, reading the secret letter.

“You planned it, didn’t you? From the start.”

“No. Not at all.”

A blatant lie.

Sama Pyo had been waiting there.

Waiting for the oldest friend who would come looking for him before anyone else.

No—or for the old Hidden Shadow Pavilion agent who was always stuck to Taishan’s side.

And, deep down, he had hoped Namho would figure out at least a little of the secret he couldn’t bring himself to say aloud.

He had hoped Namho would be on his guard because of it.

“Why? Why go that far?”

At my quiet question from behind him, Sama Pyo resumed his halted steps.

“Even so… he’s my father.”

He’d wanted to believe in him until the very end, no matter what.

But when that trust was betrayed, he didn’t want the people beside him put in danger.

So he had deliberately left a clue as a warning, so they would naturally grow suspicious before Sama Pyo himself could report his father’s suspicious actions.

Even if that meant they might suspect him, too, he didn’t care, as long as everyone else would be safe.

He was used to being suspected and hated.

That was what it meant to live as the blood relative of Sima Gong, the Black Night King, and the Young Sect Leader of the Black Dragon Demon Gate.

And yet it was strange.

Even after Namho’s gaze toward him had grown sharper and more searching, I hadn’t said a word.

Not once.

Not even now.

“Then why didn’t you ask me anything? Not once, all this time?”

The moment he voiced the question that had been circling in his mind, a short answer came from behind him without a hint of hesitation.

“Even so, we’re friends.”

“……!”

“Shit, I don’t know. You look dark and gloomy on the outside, but… I kept wanting to trust you. Even as everything kept turning into a shitshow, I still wanted to.”

Sama Pyo couldn’t say anything.

He just clenched his teeth to hold back the heat in his eyes, then continued forward with unsteady steps.

Somewhere behind him, my voice had already grown faint with distance.

“Don’t die. That’s an order.”

At my gentler-than-ever command, Sama Pyo didn’t answer.

He kept walking, through the ruined battlefield where the band of fighters were still hunting down and slaughtering the surviving enemies.

Or, to be exact, toward the old man standing at their center.

*Splash.*

He came to a stop at last. A pool of blood rippled beneath his feet.

Sama Pyo took a deep breath. The stench and reek of blood were foul enough to make him gag, but his heart was strangely calm and still.

His heart was as calm and still as the expression of the old man before him, who gazed at his enemy’s son with eyes too deep to read.

“Your junior, Sama Pyo, pays his respects to the Sect Leader of the great Kongtong Sect.”

At that moment—

*Shwaaah.*

Killing intent, so immense it was terrifying, surged up all around him and pressed down on Sama Pyo’s entire body.
```

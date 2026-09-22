<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0678.txt",
      "sha256": "dda51815f8fa0aec6eb5bbc03089bc23ced5006227477ee1f637162775afa90d",
      "bytes": 13068
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "163b2ff5bfcdf8d11381d89208e77bf96fe97dd87ea05d25440dffb34992d701",
      "bytes": 1881
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "a6659a37801d357b220249781d32112754534f4a2d02e2e90dc670e93300bacd",
      "bytes": 203075
    },
    {
      "path": "characters/Baeksang.md",
      "sha256": "bb6603596dfa25c2b799ca3f78e7f17ab5b16145ffbe5df7e2ef505a984c3b55",
      "bytes": 980
    },
    {
      "path": "characters/Black Hand.md",
      "sha256": "861867c4796fd74f68f563cc837dc6361865928a2cbec9421f6760260fb4507f",
      "bytes": 700
    },
    {
      "path": "characters/Heugung.md",
      "sha256": "9aaeb5f4e63fb18454cb4dc984936c7d03b6bf9f359d42b40ad80364f3f15e0a",
      "bytes": 695
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "ba1732bb66150e75be7b0f193ec48ea98f01094d9be5e02e473ac1cdaa1d1160",
      "bytes": 1858
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "95e4df3fef3799e491de85475376dc5cf0bdb167cc9c7512e1a78a45b074f2e4",
      "bytes": 622
    },
    {
      "path": "characters/Muyaho.md",
      "sha256": "ab4d79157b3a2b11bfb081ecb2fdabd74037266a85ea979c5d88d4f8fe7f64ff",
      "bytes": 648
    },
    {
      "path": "characters/Namho.md",
      "sha256": "6b84eb8f7ce492bf28428fc15efccdd37968b237c33dcacb128b4a53a68185e1",
      "bytes": 843
    },
    {
      "path": "characters/Yohi.md",
      "sha256": "0bfd26a5a9a177aec53df99bc9b67bb2dbfe7b523d0b7fd74be32269def05342",
      "bytes": 671
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "71b4c4fbfbc3e90e33d09d8c64b70a318df12882aa5e3c4be64e35d7c8477736",
      "bytes": 209835
    }
  ],
  "estimated_tokens": 11999
}
-->

# Durable State Update — Chapter 678

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 678. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 678. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history.
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
  "chapter": 678,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 678,
    "continuity_sources": [678],
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
    "Jin Taekyung is rampaging through the Poisonblood Grounds to expose the enemy and has been confronted by two Supreme Peak masters.",
    "Black Hand is a sadistic Dark Heaven agent who captured Yohi and Heugung and severely injured Heugung before being ordered not to kill them.",
    "Heugung is bound and unconscious with his internal energy sealed; Yohi remains captive with her internal energy sealed.",
    "A cold, senior old man commands Black Hand and refers to a great undertaking ordered by the Southern Heaven Demon Empress.",
    "Yohi received gold and influence from Baeksang for more than ten years, supported his decisions, and deliberately suppressed her suspicions about his Dark Heaven ties.",
    "Black Hand claims that Dark Heaven arranged the deaths of the previous Yao Great Chieftain and his three sons, enabling Yohi's succession.",
    "Black Hand knows that Yohi prepared a tracking scent, destroying her last hope of secretly guiding rescuers to her.",
    "The Southern Heaven Demon Empress has expressed interest in Yohi and remains connected to the operation in the Poisonblood Grounds."
  ],
  "continuity_sources": [
    677
  ],
  "open_questions": [
    "Who is the cold old man who commands Black Hand?",
    "What is the great undertaking ordered by the Southern Heaven Demon Empress?",
    "Can Jin Taekyung survive or defeat the two Supreme Peak masters?",
    "How directly did Baeksang participate in the deaths that enabled Yohi's succession?",
    "Can Jin rescue Yohi and Heugung before Dark Heaven carries out its plans?"
  ],
  "safe_through": 677,
  "temporary_decisions": [
    "Use Black Hand for 흑수.",
    "Render 마후 as the Demon Empress when used without the full Southern Heaven title.",
    "Preserve Black Hand's archaic first-person voice and predatory insults."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 일신     | **One God**         |
| 열화문    | **Fire Gate Clan**               |
| 무림맹    | **Murim Alliance**               |
| 남만야수궁  | **Nanman Beast Palace**          |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 초식     | **form**                                         | Numbered technique movement                           |
| 살기     | **killing intent**                               |                                                       |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 생사결    | **life-and-death duel**                          | Explicitly lethal                                     |
| 정파     | **orthodox faction**                             |                                                       |
| 강호     | **martial world**                                | Prefer “Murim” where the setting itself is meant      |
| 제자     | **Disciple**                                 |
| 선배     | **Senior**                                   |
| 상태               | **Status**                     |
| 화산     | **Huashan**            |
| 정마대전   | **Great Faction War**         |
| 노부      | **this old man / I**                                            |
| 백상 | **Baeksang** | Great chieftain of the Bai people and Yayul Cheok's sworn younger brother. |
| 흑수 | **Black Hand** | Sadistic Dark Heaven agent and Supreme Peak master. |
| 흑웅 | **Heugung** | Great chieftain of the Yi people; his name literally means Black Bear. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 무야호 | **Muyaho** | Yayul Mok's White Tiger's name; it means tiger of the mighty wilds. |
| 남호 | **Namho** | Hidden Shadow Pavilion code name; literally associated with amber from the south. |
| 요희 | **Yohi** | Female great chieftain of the Yao people. |
| 도발 | **Taunt** | System effect that the Matador’s Shield can activate against bovine-type monsters. |
| 사마외도 | **demonic, heterodox arts** | Suspected martial-arts origin of Pung Yang's insidious forms. |
| 전서구 | **messenger pigeon** | Pigeon delivering the Lower District Sect's Jeongyang Branch report. |
| 만년한철 | **Ten-Thousand-Year Cold Iron** | Material that destroys Pung Yang's Body-Protecting Qi when the Unnamed Sword satisfies a specific condition. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 권강 | **Fist Force** | Qi force projected through the Western Heaven Demon Lord's fist. |
| 열화신룡 | **Blazing Flame Divine Dragon** | New sobriquet bestowed on Jin Taekyung. |
| 남천마후 | **Southern Heaven Demon Empress** | Title Honglan uses when revealing her identity. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 남천 | **South Heaven** | Dark Heaven power that the Lord of Heaven orders the servants to contact. |
| 백호 | **White Tiger** | Yayul Mok's tiger companion. |
| 전서 | **missive** | A written message exchanged or delivered in secret. |
| 요서부 | **Western Yao Estate** | Estate inherited by Yohi when she became a Great Chieftain. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 진태경 | 선배님들 | junior_to_senior_team_members | Seniors | polite-but-threatening | Taekyung addresses the Myeongdong Guild Team 1 Hunters while ordering them to clear a path. |
| 남천마후 | 진태경 | hostile_supernatural_opponent_to_young_martial_artist | Young Great Hero / Child | lighthearted and taunting | Addresses Taekyung while refusing to explain the Gate. |
| 진태경 | 남천마후 | young_martial_artist_to_hostile_demon_empress | you | hostile and determined | Promises that the Southern Heaven Demon Empress will die when they meet again. |
| 남호 | 진태경 | Hidden_Shadow_Pavilion_agent_to_mission_leader | Jin Taekyung / you | guarded and familiar | Namho addresses Taekyung as 자네 while explaining the contact and offering guidance. |
| 진태경 | 남호 | mission_leader_to_hidden_shadow_agent | you / Namho | probing and respectful | Taekyung questions Namho’s affiliation and later discusses Dark Heaven’s threat to Nanman. |
| 요희 | 흑웅 | Yao great chieftain to Yi great chieftain | big brother | seductive and falsely affectionate | Uses 오라버니 to flatter and manipulate Heugung. |
| 흑웅 | 요희 | Yi great chieftain to Yao great chieftain | my dear | adoring and deferential | Responds to Yohi's manipulation with open infatuation. |
| 요희 | 진태경 | Yao great chieftain to Murim Alliance pavilion master | Jin Taekyung | casual and probing | Identifies him by his full name while allowing him to keep the mask on. |
| 진태경 | 요희 | Fire Dragon Pavilion pavilion master to Yao great chieftain | you | guarded and blunt | Answers Yohi's probing questions directly while warning her about Ju Hwaran. |
| 백상 | 요희 | Bai great chieftain to Yao great chieftain | Yohi | cold and formal | Calls to Yohi from outside the tent at the chapter's end. |
| 백상 | 진태경 | Nanman great chieftain to Murim Alliance Pavilion Head | you bastard | cold, hostile, and contemptuous | Baeksang calls Jin a Han Chinese man, rejects his status, and orders him to leave. |
| 진태경 | 백상 | Murim Alliance Pavilion Head to Nanman great chieftain | you | polite but deliberately provocative | Jin tells Baeksang that Nanman's blood was shed for the world rather than merely for the Central Plains. |
| 진태경 | 백호 | human ally to intelligent spiritual beast | you | casual and familiar | Converses with White Tiger after interpreting its warning. |
| 흑웅 | 백상 | younger_great_chieftain_to_senior_great_chieftain | Uncle Baek | deferential and nervous | Heugung addresses Baeksang as 백 숙부 after being confronted by his icy stare. |
| 남호 | 각주 | guide to pavilion master | Pavilion Master | blunt, hostile, and abusive | Namho addresses Jin as 각주 while accusing him of causing the disturbance. |
| 흑웅 | 진태경 | Nanman great chieftain to Central Plains ally and covert contact | you | cautious and informal | Heugung uses 자네 in private Sound Transmission while explaining the missive and Baeksang's alleged collusion. |
| 진태경 | 흑웅 | Central Plains investigator to covert informant and prospective witness | Heugung | blunt and confrontational | Jin questions Heugung's reliability, challenges his claims, and demands proof. |
| 백상 | 남천마후 | Nanman Great Chieftain to hostile demon empress | Southern Heaven Demon Empress | formal and shocked | Baeksang directly identifies the woman who appears before him. |
| 남천마후 | 백상 | Dark Heaven controller to coerced Nanman leader | Great Chieftain Baeksang / Palace Lord | playful, taunting, and threatening | She repeatedly addresses Baeksang while mocking his grief, acknowledging his effort, and issuing her order. |
| 흑수 | 요희 | hostile captor to captive | little bitch / little girl | cruel, mocking, and predatory | Black Hand taunts Yohi, threatens her life, and says the Demon Empress covets her. |
| 요희 | 흑수 | captured tribal chieftain to torturer | you | terrified and pleading | Yohi recognizes Black Hand as the Fiend who attacked her warriors and maimed Heugung. |

## Listed compact profiles

### Baeksang.md

# Baeksang (백상)

- **Safe through:** Chapter 677
- **Aliases:** None
- **Role:** Baeksang is the temporary Palace Lord of the Nanman Beast Palace, an over-seventy Great Chieftain of the Bai people, and the leader of Nanman's general mobilization, with nearly ten thousand troops stationed in the Inner Palace.
- **Personality:** Cold, rigid, meticulous, politically resolute, and strategically manipulative, with enduring grief over Hwi's death and a guarded but still powerful bond with his sworn elder brother that now leaves him visibly conflicted.
- **Voice:** Rigid, formal, restrained, and emotionally distant.
- **Relationships:** Baeksang is Yayul Cheok's sworn younger brother and childhood companion, Yayul Mok's sworn uncle, and the father of deceased Baekhwi, whom the Great Snow Fiend killed; he cultivated Yohi with gold and influence and used her support to advance Dark Heaven's preparations.

### Black Hand.md

# Black Hand (흑수)

- **Safe through:** Chapter 677
- **Aliases:** None
- **Role:** Black Hand is a sadistic Dark Heaven agent and Supreme Peak master acting under orders associated with the Southern Heaven Demon Empress.
- **Personality:** Black Hand is cruel, gleeful, predatory, and fascinated by the despair of his victims.
- **Voice:** Black Hand speaks in archaic first person with drunken mockery, humiliating insults, and casual threats.
- **Relationships:** Black Hand is the captor and torturer of Yohi and Heugung and an enemy of Jin Taekyung; a colder senior figure can command him to obey the Demon Empress's orders.

### Heugung.md

# Heugung (흑웅)

- **Safe through:** Chapter 677
- **Aliases:** None
- **Role:** Heugung is the middle-aged great chieftain of the Yi people, one of Nanman's four great tribes.
- **Personality:** Heugung presents as foolish and easily flattered in public but is capable of concealed planning, disguise, and covert contact.
- **Voice:** Heugung speaks with warm enthusiasm and genuine, openly devoted affection toward Yohi.
- **Relationships:** Heugung genuinely loves Yohi and had promised to cooperate with Jin Taekyung; Black Hand captured him and Yohi, and he is now bound and unconscious with his internal energy sealed.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 677
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple, the Fire Gate Clan's nineteenth successor, and the Pavilion Master of the Fire Dragon Pavilion within the Murim Alliance, a Supreme Peak master with the Heavenly Martial Physique and Force, a publicly recognized S-rank-level Hunter who formally retains an A-rank license, and an escaped prisoner still facing public execution at noon in two days.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 677
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Muyaho.md

# Muyaho (무야호)

- **Safe through:** Chapter 676
- **Aliases:** White Tiger
- **Role:** Muyaho is Yayul Mok's enormous white tiger companion and a renowned Nanman spiritual creature currently accompanying Jin Taekyung through the Poisonblood Grounds.
- **Personality:** Muyaho is intelligent enough to understand speech, wary of threats, and strongly food-motivated.
- **Voice:** Muyaho communicates through growls, roars, and gestures rather than human speech.
- **Relationships:** Muyaho is Yayul Mok's cherished companion and currently carries Jin while aiding his escape.

### Namho.md

# Namho (남호)

- **Safe through:** Chapter 671
- **Aliases:** Elder Chao
- **Role:** Namho is an eighty-year-old non-Han Hidden Shadow Pavilion agent who spent more than fifty years operating under the cover of the Poison Flower Pavilion in Nanman and now serves as the Fire Dragon Pavilion’s guide.
- **Personality:** Duty-bound, pragmatic, observant, and willing to use theatrical violence and crude insults to protect an intelligence operation.
- **Voice:** Measured and serious in private, but loudly abusive and convincing when maintaining his local cover.
- **Relationships:** Namho is a Hidden Shadow Pavilion contact for Jin Taekyung and the Fire Dragon Pavilion, receives intelligence from the Pavilion Master, and knows the code used by the Thousand-Faced Fox.

### Yohi.md

# Yohi (요희)

- **Safe through:** Chapter 677
- **Aliases:** None
- **Role:** Yohi is the female great chieftain of the Yao people, one of Nanman's four great tribes.
- **Personality:** Yohi's public presence is charismatic and captivating, drawing widespread admiration and affection.
- **Voice:** Not established.
- **Relationships:** Yohi leads the Yao people and seeks to unite Nanman's four great tribes under Yao leadership; she manipulated Heugung while following Baeksang, deliberately suppressed suspicions about his Dark Heaven ties, and is now held captive with her internal energy sealed.

## Korean source

```text
＃678화



당장 남천마후가 보이지 않는 건 다행이지만, 초절정 고수가 둘이라.

젠장, 모르겠다.

지금 이 상황을 다행이라고 해야 할지. 아니면 불행이라고 해야 할지.

쉬이잉, 콰광!

빛살처럼 쇄도한 흑색 권강(拳罡)을 한 끗 차이로 피해 낸 나는, 신형을 바로 세우며 탄식했다.

“아아, 강호의 도리가 땅에 떨어졌구나. 후배를 위해 삼 초식(招式)을 양보하던 무림의 미덕은 어디로 사라졌단 말인가.”

“뭐?”

두 노인 중, 땅딸막한 산발의 늙은이가 눈을 끔뻑거리며 나를 바라봤다.

방금 들었던 말이 어지간히 황당했는지, 선제공격에 이어 연이어 출수(出手)하려던 주먹도 얌전히 내려간 상태다.

“강호의 도리? 후배를 위해 삼 초식을 양보해?”

나는 목소리를 내리깔며 대답했다.

“그렇소.”

“갑자기 웬 하오체에 헛소리냐. 심지어 조금 전에는 차례대로 상대할 테니 한 놈은 빠져 있으라고 했으면서.”

“놈? 놈이요? 제가 그랬습니까?”

“이젠 또 존댓말이군. 차라리 처음처럼 반말을 하든가, 아니면 하오체로 통일해라. 정신없으니까.”

“용서하십시오. 까마득한 후배가 노선배님들을 몰라뵙고 결례를 저질렀습니다.”

칼 같은 자세로 포권까지 취하자 산발 노인의 눈동자에 혼란이 깃들었다.

“이 정도면 슬슬 헷갈리기까지 하는데. 네놈, 혹시 화왕의 후인인 열화신룡 진태경이 아니더냐?”

“맞습니다.”

“그럼 결국 정파 나부랭이라는 소린데, 후배 운운하는 걸 듣고 있자니 기도 안 차는군.”

“무슨 섭섭한 말씀을. 강호에 있다면 모두 같은 무림 동도이자, 한 가족 아니겠습니까? 그리고 열화문은 본래 정사지간의 문파라 정사마 그런 거 편식 안 하고 모두 사이좋게 지냅니다.”

“그런 놈이 무림맹 각주 노릇을 하고 있느냐?”

눈빛은 이미 맛탱이가 갔는데, 그나마 아직 뇌는 최소한의 기능을 하는 모양이다.

그러나 진정한 고수는 어떤 상황에서도 평정심을 유지하는 법.

나는 산발 노인의 날카로운 질문에도, 표정 하나 바꾸지 않고 대답했다.

“사실 이중 첩자입니다.”

“이중 첩자?”

“예.”

“개소리.”

“왈.”

“환장하겠군.”

“어떤 마음이실지 이해합니다. 하지만 하늘을 우러러 맹세코, 한 치의 거짓도 없는 진실입니다.”

“네 녀석…….”

“부르셨습니까. 노선배.”

정중한 내 모습을 물끄러미 바라보던 산발 노인이, 감탄한 표정으로 입을 열었다.

“아주 한 땀 한 땀 정성을 다해 헛소리를 지껄이는구나. 노부가 지금껏 살면서 너 같은 정파 놈은 처음 봤다.”

나는 쑥스럽게 뒤통수를 긁적였다.

“시벌 새끼. 그럼 정성을 봐서라도 속아 주지.”

“이 정신 나간 아해야. 속을 만해야 속지 않겠느냐.”

“안 그래도 쪽팔리니까 그만해, 병신아.”

“……혀가 짧아도 너무 짧군. 분명 조금 전까진 노선배였던 것 같은데.”

“늙은이가 노망이 났나. 정마대전 때 진작 뒤졌어야 할 사마외도 찌끄레기 새끼가 어딜 선배 소리를 들으려고.”

시원하게 쏟아지는 욕설에, 잠깐 멍한 표정을 짓던 산발 노인이 낄낄거렸다.

“이거 완전히 미친놈이었군. 실로 화왕의 제자다워.”

“이상하게 만나는 놈들마다 꼭 저 소리 하더라. 실제로는 화왕이 누구인지 얼굴 한번 본 적 없으면서.”

잠깐 멈칫한 산발 노인이 피식, 실소를 흘렸다.

“우습구나. 참으로 우스워. 이제 고작 약관을 갓 넘은 핏덩이에 불과한 네놈이 감히 그 시절을 논하다니.”

“글쎄. 굳이 안 살아 봤어도 알 것 같은데.”

나는 어깨를 으쓱하며 말을 이었다.

“너 같은 새끼가 그분을 만났으면, 이미 뒈지고 없을 거거든. 한 마디로 화왕을 피해 살아남은 운 좋은 새끼라는 거지.”

“……!”

“근데, 아마 그 운도 오늘이 마지막일 것 같다.”

스윽.

손에 쥔 백염을 들어 놈을, 아니 놈들을 겨누었다. 열양지기를 머금은 새하얀 창날로부터 아지랑이가 피어올랐다.

“요서부. 너희 짓이냐?”

우득.

어느새 얼굴에 웃음기가 사라진 산발 노인이 주먹을 말아쥐며 앞으로 나섰다.

“그래, 노부가 했다.”

“하긴. 왠지 느낌이 그럴 것 같긴 했어. 정신 나간 놈이나 그런 식으로 사람을 죽이니까. 흑웅과 요희는?”

“우선은 곱게 모셔 두었지. 마후(魔后)께서 돌아오시면 그 연놈들의 질긴 명줄도 끝장이겠지만.”

나는 적이 직접 확인해 준 두 가지 사실에 안도했다.

“개꿀 정보 고맙다. 일단 남천마후, 그 썅년은 여기에 없다는 소리네. 두 사람도 멀쩡하고.”

그제야 굳이 하지 않아도 될 말을 했다는 것을 깨달은 산발 노인의 얼굴이 딱딱하게 굳었다.

“……그렇다고 달라지는 건 없다. 설령 마후께서 안 계시다 한들 네놈은 노부의 손에 죽을 테니.”

“근데 왜 둘이 손잡고 왔니. 어린놈한테 줘 터질까 봐 쫄려서 형 데려온 거야?”

“이런 빌어먹을 애새끼가…….”

저벅.

분노를 참지 못해 앞으로 튀어나온 한 걸음. 남들이 보기에는 별것 아니지만, 그 한 걸음이 지금의 내게는 꼭 필요했다.

‘지금.’

하지만 다음 순간, 나는 전력을 다해 휘두르려던 창을 멈출 수밖에 없었다.

턱.

막 걸음을 뗀 산발 노인의 어깨를, 나뭇가지처럼 길고 말라비틀어진 손이 붙잡았기 때문이었다.

“격장지계(激將之計)다. 놈의 세 치 혓바닥에 놀아나지 마라.”

드디어 나섰군.

냉막한 목소리와 표정. 백상도 쌀쌀맞기로는 둘째가라면 서러울 정도지만, 시종일관 한마디도 하지 않던 호리호리한 노인은 그 이상이었다. 아니, 성질은 같을지라도 깊이부터가 달랐다.

빙하처럼 단단하고 차가운 냉정함도, 일신에 깃든 무위도.

‘틈이 안 보여.’

이러한 직감이 의미하는 사실은 명백하다.

최소한 나와 동수이거나, 혹은 그 이상.

그렇기에 직접 말을 주고받은 건 산발 노인이었지만, 내 신경은 처음부터 줄곧 저자에게 쏠려 있었다.

그리고 그것은 상대도 마찬가지인 듯했다.

“제법이구나. 아니, 제법이라는 말로는 턱없이 부족해.”

감정을 느끼기 어려운 탄성과 함께 호리호리한 노인이 앞으로 나섰다.

“말 몇 마디로 상대의 마음을 어지럽히고, 틈을 노려 이득을 취한다……. 왜 마후께서 너를 경계하라 하셨는지 이제야 알겠다. 나이를 무색케 하는 무위에 심계(心計)마저 갖추었으니, 향후 큰 걸림돌이 될 테지.”

“단순한 칭찬을 내가 너무 부정적으로 생각하는 건가? 어떻게든 날 죽이겠다는 소리로 들리는데.”

“하면 제대로 알아들은 것이 맞다. 칭찬도, 죽이겠다는 뜻도.”

“그럼 기왕 칭찬한 김에 그냥 조용히 지나가지. 굳이 돌을 빼낼 필요가 있을까.”

“길 한 가운데에 박힌 돌을 뽑아야, 앞으로 갈 길이 평탄해지지 않겠느냐.”

“둘 다 그럴 만한 실력은 되고?”

“노옴! 주둥이 닥치지 못할까!”

툭 던진 도발에 얼굴을 일그러트린 산발 노인과 달리, 호리호리한 노인은 냉막한 목소리로 대답했다.

“최선을 다해야겠지.”

빌어먹을.

문득 매우 어려운 싸움이 될 거라는 짐작, 아니 확신이 들었다.

미친개가 날뛴다면 몽둥이로 때려잡으면 그만이다.

하지만 어떤 상황에서도 냉정함을 유지하고, 상대를 경원시하지 않는 적이라면…… 까다로울 수밖에 없다.

더군다나 그 적이 나와 비교해도 결코 떨어지지 않는 무위의 소유자라면 더더욱.

‘저자와 일대일로 생사결을 벌인다면 승률은 반반. 하지만 그런 상황은 일어나지 않겠지.’

한 끗 차이로 생사가 오가는 혈투에는 고양이 손이라도 보탬이 된다. 하물며 내가 파악한 산발 노인의 실력은 백상보다도 윗줄.

‘할 수 있을까. 내가.’

본능이 불러온 한 줄기 의문이 뇌리를 스친 그때.

- 크르릉…….

무야호가 이빨을 드러내며 경계 어린 울음소리를 토해 냈다.

그러나 언제든지 달려들 수 있도록 잔뜩 수그린 자세에서는, 한 치의 물러섬도 보이지 않았다.

그래, 시발. 말 못 하는 짐승도 싸우겠다는데 사람인 내가 물러설 수야 있나.

다만 한 가지 걸리는 점이 있다면, 이번만큼은 녀석을 보호해 주지 못할 수도 있다는 직감 때문이다.

‘미안하다.’

- 크릉.

모르겠다. 저 영민한 백호가 내 눈빛에 담긴 뜻을 읽었는지, 차라리 녀석만은 멀리 도망치기를 바라는 내 마음을 아는지.

하지만 이것 하나만큼은 확실하다.

이 자리에서 죽거나, 혹은 죽이거나.

결말과 상관없이, 나는 물러서지 않을 거다.

저벅.

“어차피 네놈들 이름은 들어 본 적도 없으니까 더 이상 서지도 않는 좆이나 까 잡수시고, 각자 별호나 씨부려 봐.”

백염을 늘어트린 나를 향해, 산발 노인이 살기 어린 미소를 지으며 입을 열었다.

“흑수권마(黑手拳魔).”

“그래, 우리 흑손이. 별호가 낯선 걸 보니 역시 듣보잡이었구나.”

“나름의 사정이 있었지. 하지만 이제 온 천하가 알게 될 거다. 열화신룡을 죽인 자의 별호니까.”

“글쎄. 굳이 그 방법이 아니어도 다들 알게 될 거야. 내 손에 죽은 놈들은 죄다 유명해지거든.”

담담하게 대답한 나는, 벌컥 성을 내려는 흑수권마를 무시한 채 시선을 돌렸다.

하지만 내 바람과는 달리, 나와 눈이 마주친 호리호리한 노인은 작게 고개를 저어 보였다.

“별호가 알려진 상대만큼 파악하기 쉬운 적도 없지. 그렇지 않으냐? 열화신룡 진태경.”

“……!”

“노부는 너를 알고, 너는 노부를 모른다. 허나 우리 중 하나는 이곳에서 쓰러지겠지. 각오가 끝났다면 오너라.”

빌어먹을. 역시 쉽지 않다.

하지만 이미 주사위는 던져졌고, 이제는 주사위의 눈을 확인해야 할 시간.

나는 하단전에 웅크린 화룡(火龍)을 깨웠다.

구구구궁-!

화산이 폭발하듯 전신으로부터 터져 나온 기파가 사방을 뒤흔들고, 만년한철로 이루어진 투명한 창날 위로 청백색의 화염이 겹겹이 덧씌워지며 창을 온전하게 감싸 안는다.

화륵. 츠츠츠!

독을 태우고 수분을 증발시키는 끔찍한 열기.

내가 뿜어내는 기세에 술에 취한 사람처럼 흐릿하던 흑수권마의 초점이 또렷해지고, 만년설처럼 얼어붙어 있던 노인의 눈동자에는 기광(奇光)이 스쳤다.

“과연……!”

스윽.

그리고 짧은 탄성과 함께 헐렁한 소매 아래로 모습을 드러낸 날붙이가 시퍼런 빛을 흘린 그 순간.

슈화아아악!

노인의 손을 떠난 두 자루의 쌍륜(雙輪)이, 공간을 찢어발기며 날아들었다.



* * *



쉬쉬쉬쉭!

그들은 쉼 없이 달렸다.

세 마리였던 호랑이가 둘로, 다섯 사람이 넷으로 줄어도 그 사실은 변하지 않았다.

아니, 그렇기에 더더욱 빠르게 나아가야 했다.

지나온 길을 돌아가기에는 너무 멀리 와 버렸으니. 이곳에서 돌아간다면 ‘그’의 선택과 희생이 물거품이 되어 버릴 테니.

그리고 그, 아니, 진태경의 노력 덕분인지 그들의 앞길을 막아서는 방해물은 없었다.

네 사람을 등에 실은 호랑이들은 남만야수궁에서 날아오른 전서구가 도착하기도 전에 북으로, 또 북으로 내달렸고 각 부족의 전사들은 진태경을 쫓기에 바빴으니까.

쉬쉬쉬쉭!

그들은 들판을 가로지르고, 산을 넘고, 늪지대와 강을 건넜다.

그리고 마침내…… 이 짧지만 긴박했던 여정의 첫 번째 목표가 보이기 시작했다.

“저곳!”

남호의 외침은 언덕 아래를 향하고 있었다.

저 멀리, 꼬리를 물고 북쪽 경계선을 향해 나아가는 수백여 명의 남만 전사들.

마침내 척후대를 따라잡은 그들은 맥이 풀림과 동시에 한 사람의 얼굴을 떠올렸다.

‘진태경.’

지금쯤 어디에서 무엇을 하고 있을지 모르는 자신들의 각주를.
```

## Final English reading copy

```markdown
# Chapter 678

It was fortunate that the Southern Heaven Demon Empress was nowhere to be seen for the moment, but there were two Supreme Peak masters here.

*Damn it. I don’t know.*

Should I call this situation fortunate? Or unfortunate?

*Whoosh—KWA-BOOM!*

I narrowly dodged a black Fist Force that came rushing at me like a beam of light, straightened my body, and let out a sigh.

“Ah, the ways of the martial world have fallen to the ground. Where has the martial virtue of yielding three forms for the sake of a junior disappeared to?”

“What?”

The squat old man with disheveled hair blinked at me.

Apparently, what I had just said was so absurd that the fist he had been about to send out after his opening attack slowly lowered.

“The ways of the martial world? Yielding three forms for a junior?”

I lowered my voice and answered.

“That is correct.”

“Why are you suddenly talking like some old-fashioned gentleman and spouting nonsense? A moment ago, you said you’d face us one at a time and told one bastard to stay out of it.”

“‘Bastard’? Did I say that?”

“Now you’re being polite again. Either speak casually like you did at first, or stick to the formal register. You’re giving me whiplash.”

“Forgive me. This distant junior failed to recognize his Seniors and committed a grave discourtesy.”

I adopted a posture as straight as a sword and even performed a clasped-fist salute. Confusion filled the disheveled old man’s eyes.

“This is getting confusing. You’re not Blazing Flame Divine Dragon Jin Taekyung, the Fire King’s heir, are you?”

“I am.”

“Then that means you’re one of those orthodox-faction types. Hearing you go on about juniors is enough to make me sick.”

“What a hurtful thing to say. Aren’t all those who dwell in the martial world fellow martial artists and members of one family? Besides, the Fire Gate Clan has always been a faction between the orthodox and unorthodox sides. We don’t discriminate between the orthodox, demonic, or anything else. We all get along.”

“And yet you’re serving as a pavilion master in the Murim Alliance?”

His eyes had already gone completely off the rails, but at least his brain still seemed to possess a minimum level of function.

However, a true master maintained his composure in any situation.

So I answered his sharp question without changing my expression.

“I’m actually a double agent.”

“A double agent?”

“Yes.”

“Bullshit.”

“Woof.”

“This is driving me insane.”

“I understand how you feel. But I swear to heaven, there isn’t a shred of falsehood in what I’ve said.”

“You little…”

“Did you call for me, Senior?”

The disheveled old man stared blankly at my polite demeanor before opening his mouth with a look of admiration.

“You put your whole heart into spouting nonsense, one stitch at a time. In all my years, I’ve never seen an orthodox-faction brat like you.”

I scratched the back of my head sheepishly.

“You fucking bastard. Then at least pretend to fall for it out of respect for the effort.”

“You deranged child. Shouldn’t the lie be believable before anyone can be fooled?”

“I’m already embarrassed, so shut up, you idiot.”

“……That tongue of yours got awfully rude, awfully fast. I could’ve sworn I was ‘Senior’ just a moment ago.”

“Did senility finally get you, old man? You’re a piece of demonic, heterodox trash who should’ve died back during the Great Faction War. Who the hell do you think you are, demanding to be called Senior?”

At the stream of abuse, the disheveled old man stared blankly for a moment before bursting into laughter.

“You really are a completely insane bastard. You’re truly worthy of being the Fire King’s Disciple.”

“Funny how everyone I meet says that when none of them have ever even seen the Fire King’s face.”

The disheveled old man hesitated for a moment before letting out a quiet laugh.

“How amusing. Truly amusing. You’re nothing but a bloody whelp who has barely passed the age of twenty, yet you dare speak of those days.”

“Well, I feel like I can figure it out without having lived through them.”

I shrugged and continued.

“If a bastard like you had met him, you’d already be dead. In short, you’re a lucky bastard who survived by avoiding the Fire King.”

“……!”

“But I have a feeling that luck will run out today.”

*Swish.*

I raised White Flame and pointed it at him—or rather, at them. A haze rose from the pure-white spearhead filled with Scorching Yang Qi.

“The Western Yao Estate. Was that your doing?”

*Crack.*

The smile vanished from the disheveled old man’s face as he clenched his fist and stepped forward.

“Yes. This old man did it.”

“I thought so. Only someone out of his mind would kill people that way. What about Heugung and Yohi?”

“For now, we have those two tucked away nice and comfortably. But once Her Majesty the Demon Empress returns, those bastards’ stubborn hold on life will end.”

I felt relieved by the two facts the enemy had confirmed himself.

“Thanks for the fucking useful intel. So the Southern Heaven Demon Empress—that fucking bitch—isn’t here. And those two are still in one piece.”

Only then did the disheveled old man realize that he had said more than he needed to. His face hardened.

“……That changes nothing. Even if Her Majesty the Demon Empress is absent, you will die by this old man’s hand.”

“Then why did you two come together? Were you scared a kid would kick your ass, so you brought your hyung?”

“You fucking brat…”

*Step.*

The disheveled old man took a step forward, unable to contain his anger. It was nothing special to an observer, but that single step was exactly what I needed.

*Now.*

But in the next moment, I had no choice but to stop the spear I had been about to swing with all my strength.

*Thud.*

A long, withered hand as thin as a tree branch had seized the shoulder of the disheveled old man just as he stepped forward.

“It’s a provocation tactic. Don’t let that bastard’s three-inch tongue fool you.”

*So he finally stepped in.*

A cold voice. A cold expression.

Baeksang was second to none when it came to being chilly, but the slender old man, who had not said a word from beginning to end, was on another level. No—their temperaments might have been similar, but there was a difference in depth.

The ice-hard, glacier-cold composure.

And the martial prowess contained within his body.

*There’s no opening.*

The meaning of that instinct was clear.

He was at least my equal—or perhaps even stronger.

That was why, although the disheveled old man had been the one speaking with me directly, my nerves had been focused on the slender old man from the very beginning.

And it seemed my opponent felt the same way.

“You’re quite something. No, ‘quite something’ doesn’t come close.”

With an exclamation that betrayed little emotion, the slender old man stepped forward.

“You unsettled your opponent with a few words and exploited the opening you created… Now I understand why Her Majesty the Demon Empress warned us to be wary of you. You possess martial prowess that belies your age, as well as a calculating mind. You will become a major obstacle in the future.”

“Am I being too negative about a simple compliment? It sounds like you’re saying you intend to kill me somehow.”

“Then you understood correctly. Both the compliment and the intention to kill you.”

“Since you went to the trouble of complimenting me, why don’t you just let me pass quietly? Is there really any need to pull out a stone?”

“If you remove the stone embedded in the middle of the road, the path ahead will become smooth.”

“And are the two of you really skilled enough to do that?”

“You bastard! Shut your mouth!”

Unlike the disheveled old man, whose face twisted at my casually tossed taunt, the slender old man answered in his cold voice.

“We will have to do our best.”

*Damn it.*

I suddenly had a feeling—no, the certainty—that this would be an extremely difficult fight.

If a mad dog runs wild, all you have to do is beat it down with a club.

But an enemy who maintained his composure in every situation and never underestimated his opponent was bound to be troublesome.

Even more so if that enemy possessed martial prowess that was in no way inferior to my own.

*If I fought that man one-on-one in a life-and-death duel, my odds would be fifty-fifty. But that situation won’t happen.*

In a bloody struggle where life and death could be decided by the slightest difference, even a cat’s paw was useful. And the disheveled old man’s skill, as far as I could tell, was even greater than Baeksang’s.

*Can I do this? Can I?*

Just as a single doubt summoned by instinct flashed through my mind—

“Grrrr…”

Muyaho bared his fangs and let out a wary growl.

Yet in his crouched posture, ready to spring at any moment, there was not the slightest sign of retreat.

*Yeah, fuck. Even an animal that can’t speak is willing to fight. How can I, a human being, back down?*

There was only one thing that bothered me.

I had a feeling I might not be able to protect him this time.

*I’m sorry.*

“Grrr.”

I didn’t know.

Perhaps the clever White Tiger had read the meaning in my eyes. Perhaps he understood that I wished, if nothing else, for him to run far away.

But one thing was certain.

Either I would die here, or I would kill them.

Regardless of the outcome, I would not retreat.

*Step.*

“Since I’ve never even heard your names anyway, go peel and eat those limp cocks of yours, then spit out your sobriquets.”

The disheveled old man smiled with killing intent as he spoke to me, White Flame hanging loosely in my hand.

“Black Hand Fist Demon.”

“Yeah, there you are, Black Hand. I’ve never heard that sobriquet before, so I guess you really are some nobody.”

“There were reasons for that. But now the whole world will know it. It will be the sobriquet of the one who killed the Blazing Flame Divine Dragon.”

“Maybe. But everyone will learn who I am even without that. Everyone who dies by my hand becomes famous.”

I answered calmly, ignoring the Black Hand Fist Demon as he began to flare up, and turned my gaze away.

But contrary to my wishes, the slender old man met my eyes and gave a small shake of his head.

“There is no enemy easier to assess than one whose sobriquet is known. Isn’t that right, Blazing Flame Divine Dragon Jin Taekyung?”

“……!”

“This old man knows you, while you do not know me. But one of us will fall here. If you have finished preparing yourself, come.”

*Damn it. This really won’t be easy.*

But the die had already been cast. Now it was time to see how it landed.

I awakened the fire dragon curled within my lower dantian.

*Rumble-rumble-rumble—!*

An aura erupted from my entire body like a volcano exploding, shaking the area in every direction. Blue-white flames layered themselves over the transparent spearhead made of Ten-Thousand-Year Cold Iron, completely enveloping the spear.

*Fwoosh. Sizzle-sizzle-sizzle!*

The terrible heat burned poison and evaporated moisture.

The Black Hand Fist Demon’s focus, which had been hazy like that of a drunken man, sharpened at the aura I released. A strange light flashed through the old man’s eyes, frozen like eternal snow.

“Indeed…!”

*Swish.*

At that moment, with a brief exclamation, an edged weapon emerged from beneath his loose sleeve and gleamed with a cold blue light.

*SHWAAAAAAK!*

The twin wheels flew from the old man’s hand, tearing through the air.

* * *

*Whoosh-whoosh-whoosh!*

They ran without stopping.

Even when three tigers became two and five people became four, that fact did not change.

No—in that situation, they had to move even faster.

They had come too far to turn back. If they returned now, *his* choice and sacrifice would become meaningless.

And perhaps thanks to his—no, Jin Taekyung’s—efforts, nothing blocked their path.

The tigers carrying four people on their backs ran north, then farther north, before the messenger pigeon sent from the Nanman Beast Palace could even arrive. The warriors of each tribe were too busy chasing Jin Taekyung to interfere.

*Whoosh-whoosh-whoosh!*

They crossed the plains, climbed over mountains, and passed through swamps and rivers.

And at last, the first goal of this short yet urgent journey began to appear.

“There!”

Namho’s shout was directed below the hill.

In the distance, several hundred Nanman warriors advanced toward the northern border in a long, snaking line.

At last, having caught up with the reconnaissance squad, they felt the tension leave their bodies as a single person’s face came to mind.

*Jin Taekyung.*

Their Pavilion Master, though they had no idea where he was or what he might be doing now.
```

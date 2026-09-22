<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0619.txt",
      "sha256": "c56a254c7ae4b2d25e5fbd4c0ebc41d7c03f56faf51cb5db8fc61522e9ea5968",
      "bytes": 13538
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "96f140b31b23e2882866623d5fd98fa18527d27d4f2ef1df53319b80f2defef5",
      "bytes": 1751
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "7906913bb59587a85c3226e6498488e0e70f62c4105df4f75854fbb133ecd719",
      "bytes": 192084
    },
    {
      "path": "characters/Honglan.md",
      "sha256": "b558eef103c7d83ad8e11302b57afe6b186d885936d6fb20f3dd23eedcaa874b",
      "bytes": 973
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "b6fd00e1b2fa26c1e9f08c788e6f1e3a9f851ae05f482fbb905b2638c7b3d0c7",
      "bytes": 1206
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "c060d85462ff6e5c3130dea25f75c8a7642caf017c199a37e0e1b7d63ff3919c",
      "bytes": 1775
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "a6b490183e75ca4b2e8273e9292d6ddd5b7d7182f5c7a8f895e118c4116f3115",
      "bytes": 622
    },
    {
      "path": "characters/Ju Hwaran.md",
      "sha256": "048761f5e4ad3cc0bd18ce80a35e732f233f2cbc833039eb37715f7dffdc3332",
      "bytes": 988
    },
    {
      "path": "characters/Sama Pyo.md",
      "sha256": "ff200f7b06b9291945a54cb0f9a6b0887dbd8c5ce2377e90c212091439075f82",
      "bytes": 899
    },
    {
      "path": "characters/Song Il.md",
      "sha256": "7d82d3631b4841cf6a513f504416f21e551b9b3dd2f705b8e829d7f31ecd4e48",
      "bytes": 964
    },
    {
      "path": "characters/Song Ilseom.md",
      "sha256": "b2381e19b99016727ff19e21db74ef71bc909b13f54b0ca8a536e7ab1a483bd4",
      "bytes": 957
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "915a56f242b7383195979441f705804eacb3f86a908119d192db7325acb9a4be",
      "bytes": 528
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "692b720c4e0a64c9d34e66cdb655ddef2821d6f6435171e988fa2f5721d9fad9",
      "bytes": 194503
    }
  ],
  "estimated_tokens": 12592
}
-->

# Durable State Update — Chapter 619

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 619. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 619. Profile updates may replace only one
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
  "chapter": 619,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 619,
    "continuity_sources": [619],
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
    "The Fire Dragon Pavilion has entered Nanman and is traveling approximately two hundred li to Yeongin.",
    "The Nanman Beast Palace remains the Fire Dragon Pavilion's primary mission objective.",
    "The Peak-grade Chain Quest Seeds Planted in Nanman requires Taekyung and the Fire Dragon Pavilion to contact a Hidden Shadow Pavilion agent planted by the Murim Alliance; failure causes a stats decrease.",
    "Poison Flower Pavilion is the Hidden Shadow Pavilion contact location in Yeongin.",
    "The Deputy Stronghold Lord has promised to keep one or two Water Dragon Stronghold ships anchored nearby until the party returns.",
    "Yeongin is an underdeveloped county seat where several ethnic groups live together and its inhabitants are hostile toward Han Chinese outsiders.",
    "Ju Hwaran visited Yeongin three years earlier during an escort journey, accompanied by Song Ilseom, and knows the local area and its people.",
    "The local inhabitants have alerted their chief to the Fire Dragon Pavilion's arrival and are watching the party suspiciously."
  ],
  "continuity_sources": [
    618
  ],
  "open_questions": [
    "Who is the Hidden Shadow Pavilion agent at Poison Flower Pavilion, and what information or assistance can they provide?",
    "What dangers and plans await the Fire Dragon Pavilion at the Nanman Beast Palace?",
    "How will the party handle the local hostility toward Han Chinese outsiders?"
  ],
  "safe_through": 618,
  "temporary_decisions": [
    "Render 永仁 as Yeongin.",
    "Render 독화루 as Poison Flower Pavilion.",
    "Use Bai people for 白族.",
    "Continue using Chain Quest for 연계 퀘스트 and Peak for the system's 절정 Grade."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 혁무진    | **Hyuk Mujin**     |
| 송일     | **Song Il**        |
| 주화란    | **Ju Hwaran**      |
| 무림맹    | **Murim Alliance**               |
| 암천     | **Dark Heaven**                  |
| 용봉표국   | **Yongbong Escort Bureau**       |
| 일류     | **First Rate**    |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 중원     | **Central Plains**                               |                                                       |
| 기루     | **pleasure house**                               |                                                       |
| 표국     | **Escort Bureau**                            |
| 스킬               | **Skill**                      |
| 퀘스트              | **Quest**                      |
| 사천     | **Sichuan**            |
| 귀가      | **your family**                                                 |
| 홍란 | **Honglan** | Stage name of Ju Wongong's Lower District Sect singing courtesan; her real name is concealed. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 사마표 | **Sama Pyo** | Young Sect Leader of the Black Dragon Demon Gate. |
| 송일섬 | **Song Ilseom** | Young escort captain of the Yongbong Escort Bureau; distinct from Song Il of Zhongnan. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 은자 | **silver nyang** | Silver currency unit. |
| 인피면구 | **human-skin mask** | Disguise made from peeled human facial skin. |
| 한족 | **Han Chinese** | Ethnic designation used by the steppe chieftains. |
| 오향장육 | **five-spice pork** | Dish Cheongpung packed for the journey. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 중독 | **Poisoned** | System status abnormality caused by the poisons. |
| 화주 | **strong liquor** | Liquor stored and consumed by the dark-path swordsmen. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 천면호리 | **Thousand-Faced Fox** | Epithet of Song Ho. |
| 은영각 | **Hidden Shadow Pavilion** | Former Murim Alliance intelligence organization. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 화란 | **Hwaran** | Familiar short form of Ju Hwaran. |
| 역용술 | **disguise technique** | Technique used by the Third Fiend to conceal his identity. |
| 열화신룡 | **Blazing Flame Divine Dragon** | New sobriquet bestowed on Jin Taekyung. |
| 남천마후 | **Southern Heaven Demon Empress** | Title Honglan uses when revealing her identity. |
| 묘족 | **Miao people** | Ethnic group the Escort Bureau expects to encounter near Yunnan. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 화룡각 | **Fire Dragon Pavilion** | New name chosen for Taekyung's pavilion. |
| 독물 | **venomous beasts** | Venomous creatures associated with the Nanman Beast Palace. |
| 남천 | **South Heaven** | Dark Heaven power that the Lord of Heaven orders the servants to contact. |
| 영인 | **Yeongin** | Remote county seat in Yunnan and the party's immediate destination. |
| 백족 | **Bai people** | Ethnic group encountered in Yeongin. |
| 독화루 | **Poison Flower Pavilion** | Derelict wooden building serving as the Hidden Shadow Pavilion contact location. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 송일 | 진태경 | hostile Zhongnan Elder to accused outsider | you / Jin Taekyung | hostile and threatening | Song Il questions Taekyung's identity and later threatens him over Gong Ilhyuk's injury. |
| 송일섬 | 주화란 | escort_captain_to_young_bureau_head | Hwaran | urgent and familiar | Calls out 화란아 while urgently warning Ju Hwaran before stepping into the confrontation. |
| 주화란 | 진태경 | escort_bureau_leader_to_famous_younger_martial_artist | Young Hero Jin | formal-deferential | Hwaran introduces herself as the Young Bureau Head and formally greets Taekyung as 진 소협. |
| 진태경 | 주화란 | visitor_to_young_bureau_head | Young Lady Ju | formal-polite | Taekyung uses 주 소저 while announcing that his party must leave. |
| 주화란 | 혁무진 | rescued_survivor_to_benefactor | Benefactor | formal-deferential | Hwaran includes Mujin among the Benefactors when greeting Taekyung's companions. |
| 주화란 | 송일섬 | bureau_head_to_escort_captain | Captain Song | formal and prosecutorial | Uses his office title, then his personal name, while exposing and confronting him. |
| 홍란 | 진태경 | Lower District Sect courtesan to honored guest | honored guest | humble and formal | Introduces herself with 소녀 and addresses Taekyung as 귀인. |
| 진태경 | 홍란 | pursuer_to_hostile_opponent | you fucking bitch | profane and threatening | Taekyung demands Honglan's location and threatens her while she speaks through Song Ho. |
| 남천마후 | 진태경 | hostile_supernatural_opponent_to_young_martial_artist | Young Great Hero / Child | lighthearted and taunting | Addresses Taekyung while refusing to explain the Gate. |
| 진태경 | 남천마후 | young_martial_artist_to_hostile_demon_empress | you | hostile and determined | Promises that the Southern Heaven Demon Empress will die when they meet again. |
| 주화란 | 사마표 | former_fiancés | Young Sect Leader | formal and guarded | Hwaran formally greets her former fiancé. |
| 사마표 | 태산 | Young Sect Leader to subordinate | Taishan | informal and patronizing | Sama Pyo calls Taishan by name while ordering him to leave. |
| 태산 | 사마표 | subordinate to Young Sect Leader | Lord | crude and deferential | Taishan uses 주군 while obeying Sama Pyo. |
| 태산 | 진태경 | subordinate_to_respected_outsider | Jin Taekyung | clipped and familiar | Taishan says he likes Jin Taekyung but will fight him without hesitation if Sama Pyo commands it. |
| 사마표 | 진태경 | prospective recruit to pavilion master | you | polite, controlled, and candid | Sama Pyo uses 자네 while asking about Taekyung's attitude and admitting his intention to use him. |
| 진태경 | 사마표 | pavilion master to prospective recruit | you / that guy | blunt, informal, and distrustful | Taekyung speaks to and about Sama Pyo with casual forms such as 녀석 and 저놈. |
| 진태경 | 송일섬 | pavilion master to prospective member | Song Ilseom | direct and evaluative | Taekyung directly names Song Ilseom while comparing his qualifications with Hwaran's. |
| 아빠 | 진태경 | father to son | Taekyung | affectionate informal | Addresses his young son warmly as Taekyung. |
| 진태경 | 아빠 | son to father | Dad | childlike informal | Taekyung addresses his father as Dad in the childhood flashback. |
| 혁무진 | 송일섬 | pavilion_member_to_escort_captain | Great Hero Song | formal and deferential | Mujin addresses Song Ilseom while commenting on his broad experience. |
| 송일섬 | 사마표 | fellow_pavilion_member_to_hostile_fellow_member | you | hostile and casual | Song Ilseom discusses fighting Sama Pyo and answers him while preparing to move away. |
| 사마표 | 송일섬 | fellow_pavilion_member_to_hostile_fellow_member | you | controlled and antagonistic | Sama Pyo responds to Song Ilseom's accusations and proposes moving aside to fight. |
| 혁무진 | 태산 | pavilion_member_to_pavilion_member | you / hey | casual and coaxing | Hyuk Mujin calls after Taishan and offers jerky to persuade him to travel together. |
| 태산 | 혁무진 | pavilion_member_to_pavilion_member | you | clipped and dismissive | Taishan tells Hyuk Mujin not to follow, then accepts him as a friend after hearing about the jerky. |

## Listed compact profiles

### Honglan.md

# Honglan (홍란)

- **Safe through:** Chapter 549
- **Aliases:** None
- **Role:** Honglan is a Lower District Sect courtesan who uses a stage name, served as Ju Wongong's singing courtesan, and identifies herself as the Southern Heaven Demon Empress.
- **Personality:** Discreet about her real identity and professionally alluring.
- **Voice:** Clear, pure, and alluring, with humble formal speech toward honored guests.
- **Relationships:** Honglan is kept at Ju Wongong's side as a singing courtesan, belongs to the Lower District Sect, lost her clan and parents overnight as a child, can respond to Taekyung through Sound Transmission, is the sole surviving eyewitness to the Dongting Lake attack who knows several possible locations of the Dongting Fisherman's hidden refuges, corrupted the benevolent imugi in Dongting Lake and used it to kill many people, and can enthrall people and command them.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 618
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and a member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son; he uses quiet practices such as fishing to empty his mind. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 618
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, a Supreme Peak master with the Heavenly Martial Physique and Force, publicly recognized as an S-rank-level Hunter while formally retaining an A-rank license, and he has completed an unnamed cultivation technique designed for even the lowest-rank Hunter to learn without making it easily abusable.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 618
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Ju Hwaran.md

# Ju Hwaran (주화란)

- **Safe through:** Chapter 618
- **Aliases:** Hwaran
- **Role:** Ju Hwaran is a Level 88 Young Bureau Head, leader of the Yongbong Escort Bureau, a member of the Fire Dragon Pavilion, and an experienced Nanman escort guide with route knowledge from the Escort King's records.
- **Personality:** Intelligent, capable, responsible, filial, composed under pressure, and burdened by intense guilt over the escort journey's deaths.
- **Voice:** Clear, polite, restrained, and determined.
- **Relationships:** Escort King Ju Gongsan was her paternal grandfather, Ju Hogun is her father, Heo Jun was her uncle, Sama Pyo was her former fiancé in a political engagement she accepted for her father's sake, Song Ilseom is her direct escort who accompanied her previous journey to Yeongin, and Jin Taekyung is a trusted ally; the Yongbong Escort Bureau has longstanding ties with Yeongin’s inhabitants.

### Sama Pyo.md

# Sama Pyo (사마표)

- **Safe through:** Chapter 617
- **Aliases:** Black Dragon Saber
- **Role:** Young Sect Leader of the Black Dragon Demon Gate, a Morning Star reputed to be no less than the Ten Dragons and Phoenixes, and a member of the Fire Dragon Pavilion.
- **Personality:** Outwardly courteous and smiling, inwardly calculating, but genuinely protective of Taishan and willing to redirect blame onto his subordinate.
- **Voice:** Polite and ingratiating in public, with sardonic humor and controlled evasiveness.
- **Relationships:** Sama Pyo commands the absolutely loyal Taishan, is Sima Gong's son, was Ju Hwaran's former fiancé in a political engagement, and has joined the Fire Dragon Pavilion while openly intending to use Jin Taekyung as a useful card; he is now openly hostile toward fellow member Song Ilseom.

### Song Il.md

# Song Il (송일)

- **Safe through:** Chapter 618
- **Aliases:** Roaring Fury Swordsman
- **Role:** Elder of the Zhongnan Sect and the Roaring Fury Swordsman; senior brother of Sect Leader Gong Iljung; came to the Jin Family of Taiyuan to demand redress for Gong Ilhyuk's injury and the alleged insult to Zhongnan; attacked Jin Taekyung with the Heavenly River Thirty-Six Swords, was stopped by Jeok Cheongang, and was publicly humiliated by him.
- **Personality:** Arrogant, domineering, punitive, and confident in his martial power and seniority.
- **Voice:** Gruff, cutting, condescending, and threatening, with formal authority used to pressure those beneath him.
- **Relationships:** Gong Iljung is his junior Sect Leader and martial younger brother; Gong Ilhyuk is a junior Disciple of his sect; he recognizes Baek Museong and Cheongpung through their Huashan and Sword Saint connections.

### Song Ilseom.md

# Song Ilseom (송일섬)

- **Safe through:** Chapter 618
- **Aliases:** Escort Captain Song
- **Role:** Level 110 young escort captain of the Yongbong Escort Bureau, one of its Dragon-Phoenix Three Escorts, and a newly accepted member of Jin Taekyung and Cheongpung’s Fire Dragon Pavilion.
- **Personality:** Blunt, decisive, survival-hardened, and dryly self-aware, with little patience for insults or disorder and practical survival skills such as making disguise masks.
- **Voice:** Forceful and urgent in command, with a rough and confrontational edge.
- **Relationships:** He serves under Ju Hwaran and has expressed concern that she not be hurt or die needlessly; he is Song Pyosan’s son, his grandmother was the surviving Guangdong Chen child rescued by Ju Gongsan during the Great Faction War, and he remains openly hostile toward fellow Fire Dragon Pavilion member Sama Pyo.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 618
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord.

## Korean source

```text
＃619화



독화루(毒華樓)라…….

온갖 독물이 득실거리는 남만에 잘 어울리는 이름이다. 다만 객잔이나 기루보다는 와르르 맨션에 가깝다는 점이 함정이지만.

‘천면호리가 알려 준 대로라면 여기가 맞긴 할 텐데.’

미심쩍은 눈빛으로 낡아 부스러지기 직전의 목제 건물을 바라보던 그때, 이방인들을 둘러싼 주위의 분위기는 시시각각 흉흉해지고 있었다.

“빌어먹을 한족 놈들!”

“네놈들 땅으로 돌아가라!”

쉬익! 딱!

뒤통수로 날아드는 짱돌을 피해 낸 사마표가 한숨처럼 중얼거렸다.

“각주, 그냥 들어가는 게 낫겠는데. 당장 저들과 싸울 게 아니라면.”

“그건 곤란하지.”

적어도 이번만큼은 녀석의 말이 백번 옳았다.

남만에 도착하자마자 토착민 전체를 적으로 돌릴 수는 없으니까.

나는 살벌한 기세를 뿜어내는 이민족 무리를 힐끗 바라본 뒤 독화루의 문을 열었다.

끼이이익.

낡아빠진 목제 문이 힘없는 마찰음을 토해 낸다.

흐릿한 불빛과 음울한 분위기에 잠긴 객잔 내부. 잡초처럼 듬성듬성 자리 잡은 조잡한 탁자를 사이에 두고 앉아 있던 선객들이 이쪽을 향해 고개를 돌렸다.

“못 보던 얼굴인…… 한족?”

“카악, 퉤.”

히드라인가.

이 동네 사람들은 가래를 아주 패시브 스킬처럼 쓰는구만.

먼지 쌓인 바닥에 침을 탁 뱉은 이민족 손님들은 불콰하게 달아오른 얼굴로 자리에서 일어났다.

“여기가 어디라고 감히 한족 놈들이. 죽고 싶어서 환장을 한 건가?”

“술맛도 떨어졌으니 이만 나가세. 저놈들이랑 함께 있어 봤자 좋을 게 없어.”

쾅!

큰소리와 함께 문이 닫히자 주화란이 복잡한 표정으로 입을 열었다.

“뭔가 단단히 틀어진 모양이에요. 지난번에 왔을 때만 해도 분명 이 정도는 아니었는데.”

송일섬도 고개를 끄덕이며 동조했다.

“내 생각도 같다. 남만의 이민족들이 경계심이 심한 건 사실이지만, 적어도 중원과 가장 가깝게 맞닿아 있는 영인(永仁)만큼은 달랐어.”

“맞아요. 그래서 비록 흔한 일은 아니었지만, 중원의 상단이나 표국이 오가던 곳이기도 했고요. 그런데 왜…….”

주화란이 말꼬리를 흐리던 그때. 어디선가 늙수그레한 목소리가 불쑥 끼어들었다.

“왜긴. 바로 그 표국 때문이지. 자네들과 같은 한족 놈들 말이야.”

독화루에 남아 있던 사람은 우리뿐만이 아니었다.

조금 전까지만 하더라도 술에 떡이 된 채 자고 있던 노인은, 굽은 허리를 두드리며 말을 이었다.

“재수 옴 붙은 게지. 이런 상황에 멋모르고 남만까지 기어들어 온 자네들도. 그런 겁 없는 한족 놈들 때문에 장사 공치게 생긴 어떤 늙은이도.”

노인의 정체를 알아차린 내가 물었다.

“여기 주인장 되십니까?”

입술 사이로 흘러나오는 유창한 이민족의 언어에, 노인이 뜻밖이라는 눈빛으로 나를 바라보았다.

“이곳 말을 할 줄 아는군. 혹시 묘족(苗族) 출신인가?”

“아뇨.”

“그렇다고 백족이나 만족 같지는 않고. 상판을 보아하니 한족이 틀림없는데…… 말이 놀라울 만큼 능숙하군. 여기서 나고 자란 사람이라고 해도 믿을 정도야.”

역시 [통합언어팩]. 성능 하나는 확실하지.

내 유창한 발음에 주화란도 놀란 표정을 지을 정도다.

“이민족들의 언어는 언제 익히셨어요?”

“음, 그거야 뭐.”

미주알고주알 설명할 수도 없는 문제라, 말꼬리를 흐린 나는 천연덕스럽게 대답했다.

“그냥 어쩌다가 보니 익히게 된 잡기예요.”

옆자리에 앉은 혁무진이 작은 목소리로 중얼거렸다.

“조장님이 할 줄 아는 건 주색잡기밖에 없었는데…….”

“시벌놈이.”

빡!

“어억!”

명치를 붙잡고 쓰러지는 혁무진의 모습에 노인이 혀를 찼다.

“맞을 말만 골라서 하는 놈이로군.”

“원래 저런 놈이니까 신경 쓰지 마시고…… 잠깐. 한어를 할 줄 아십니까?”

“어느 정도는. 젊었을 적에는 한족들과의 통역도 여러 번 맡았었지.”

대수롭지 않다는 듯이 대답한 노인이 뼈마디밖에 남지 않은 손가락으로 송일섬을 가리켰다.

“저 컴컴하게 생긴 자는 제법 익숙한 얼굴인데, 혹시 삼 년 전쯤 이곳에 온 적이 있지 않나?”

따지고 보면 가장 눈에 띄는 것은 주화란이었을 텐데, 인피면구를 착용해서인지 송일섬을 가장 먼저 알아본다.

송일섬이 묵묵히 고개를 끄덕이자, 노인이 무릎을 탁 쳤다.

“그럴 줄 알았지. 거기 이름이 아마 용왕…….”

“용봉표국이오. 용왕이 아니라.”

“그래. 용봉표국. 중원의 다른 상단이나 표국과는 달리 일 년에 두어 번씩 오던 한족들이라 똑똑히 기억하고 있지.”

똑똑히 기억한 것치고는 이름부터 틀렸는데요.

근질거리는 입을 참은 나는, 아까부터 노인에게 묻고 싶었던 질문을 던졌다.

“그런데 조금 전에 하신 말씀은 뭡니까?”

“응? 뭐가?”

“표국 때문에 이렇게 됐다고 하셨잖습니까. 하신 말씀을 그대로 옮기자면, 우리 같은 한족 놈들 때문에요.”

노인이 뚱한 표정으로 되물었다.

“내가? 언제?”

“예? 분명히 그러셨…….”

“도통 기억이 안 나는데.”

기억이 안 나긴 개뿔이. 노인의 태도에서 뭔가를 깨달은 내가 한숨처럼 입을 열었다.

“식사. 지금 바로 준비됩니까?”

“아, 당연히 되지. 돈만 주면 뭐든 해 줄 테니 걱정 말라고.”

식사라는 두 글자에, 죽어 가는 표정으로 탁자에 엎드려 있던 태산이 벌떡 일어나며 부르짖었다.

“태산이! 오향장육 먹고 싶다!”

“무식할 만큼 기운찬 놈이 하나 있었군. 그럼 닭고기를 준비해 주지.”

“왜째서 닭고기! 태산이 싫다! 오향장육!”

오향장육을 해 달라는데 왜 닭고기로 변경되었는지는 모르겠지만, 지금은 최대한 노인의 비위를 맞춰야 한다.

나는 곧장 지랄 발광을 떨어 대는 태산을 막을 한 사람의 이름을 불렀다.

“마표야. 뭐하냐.”

“사마표다.”

“그래, 사표야.”

“……태산. 그만하고 자리에 앉아라.”

기분 나쁜 표정으로 나를 노려본 사마표가 태산을 진정시키는 사이, 노인은 천연덕스럽게 손을 내밀고 있었다.

“뭡니까?”

“선결제일세.”

“아.”

“어디 보자. 일인일계(一人一鷄)는 기본이니 닭 다섯 마리가 필요하겠군. 게다가 마리 당 은자 한 냥으로 쳐서…… 도합 은자 열 냥일세.”

“……은자 열 냥이요? 심지어 마리당 한 냥이면 은자 다섯 냥인데?”

“그런가? 그럼 마리 당 두 냥으로 하세나.”

“예?”

노인이 당당하게 대답했다.

“아. 마리당 두 냥으로 하자고.”

“…….”

“싫으면 침 뱉고 나가든가. 참고로 인근 백 리 안에 다른 마을은 없네.”

미친 배짱 장사 보소. 한 오십 년 전쯤 용산에서 태어났다면 건물주가 되었을 양반이다.

‘웬일로 오는 길에 산적을 안 만나나 했는데, 산이 아니라 객잔에 있었네.’

날강도나 다름없는 가격이었지만 지금은 돈 아낄 때가 아니다.

나는 무림맹에서 활동비로 받아 온 두둑한 전낭에서 은자 열 개를 꺼내어 노인에게 건넸다.

“자. 은자 열 냥입니다.”

“한족치고는 제법 말귀가 통하는군.”

촤르륵.

번쩍이는 은자를 쓸어 담은 노인이 씩 웃었다.

“그건 그렇고. 술은?”

“술은 괜찮습니다.”

“마셔.”

“…….”

“마시라고.”

이제는 뭐라 대꾸할 기력도 없다.

나는 침울한 표정으로 다시 전낭을 열었다.



* * *



남만에서의 첫 식사는 다른 의미로 대단했다.

영양실조에 걸려 비쩍 마른 닭 요리. 그리고 누군가 먹다 남긴 것이 분명해 보이는 키핑 화주(火酒).

이딴 걸로 은자 수십 냥씩이나 받아먹는 것도 놀라웠지만, 그중 상당수가 노인의 입에 들어갔다는 사실만큼은 아니었다.

“꺼윽. 잘 먹었다.”

“…….”

아니, 왜 우리가 아니라 당신이 잘 먹은 건데.

그런 의문이 목구멍 끝까지 차올랐지만 간신히 참았다. 돈과 식사를 바치는 대가로 정보를 얻었으니까.

“천마표국이요?”

“그래. 기억하기로는 분명 사천(四川)에서 왔다고 했어. 여인 하나에 다른 사내들까지 합치면 거진 삼십여 명이었지.”

고개를 끄덕인 노인이 얼큰하게 취한 낯빛으로 말을 이었다.

“처음에는 다들 그러려니 했네. 이 영인 땅에 한족이 왔던 적이 한두 번도 아니었고, 규모도 그리 크지 않았으니까.”

하지만 그건 오판이었다. 노인은 불그스름하게 달아오른 눈빛으로 그날의 기억을 천천히 회상했다.

“누구도 예상치 못했던 일이 벌어졌지. 인근의 마을 사람들이 잔치를 열어 놈들을 대접했는데, 하룻밤 사이 모조리 도륙이 난 거야.”

“……!”

“우리 마을은 다행히 화를 피했지만, 나중에 확인해 보니 그날 밤에만 자그마치 이백여 명이 죽었더군. 사내는 물론이거니와 여인과 아이. 노인까지. 단 한 사람도 살아남지 못했네. 말할 것도 없이 그 한족 놈들의 소행이었지.”

“허.”

놀랍고도 처참한 이야기다. 이제야 우리를 향해 쏟아졌던 흉흉한 눈빛들과 분위기를 충분히 이해할 수 있었다.

더불어 두 개의 단어가 뇌리를 스쳤다.

‘암천(暗天). 그리고 남천마후(南天魔后).’

천마표국에 포함되었던 한 여인이 마음에 걸리는 건 결코 과민반응이 아니다.

심각한 표정으로 이야기를 듣고 있던 화룡각 대원들과 눈빛을 주고받은 나는 인벤토리에 넣어 두었던 종이 한 장을 꺼내 들었다.

“말씀 중에 죄송한데, 이것 좀 봐 주시겠습니까?”

“이게 뭔가?”

내가 꺼낸 종이는 그림이었다.

보다 정확히 말하자면 나를 포함한 여러 사람의 증언과 기억을 토대로 만들어진 홍란, 아니 남천마후의 용모파기다.

혹시나 하는 마음에 보여 준 것인데, 그림을 확인한 노인의 반응은 미적지근했다.

“화공의 솜씨가 대단하군. 한데 이 여인은 누구지?”

“음, 아닙니다. 혹시 알고 계신 얼굴인가 해서요.”

“그림 속 여인은 본 적 없네. 이토록 아름답다면 어떻게든 기억에 남아 있었겠지. 나 역시 아무리 늙었어도 사내니까.”

기대했던 반응은 아니었지만, 크게 실망하는 마음이 들지는 않았다.

심성이야 어찌 되었건 남천마후는 화려한 외모의 소유자. 주화란이 송일섬이 만들어 준 인피면구를 통해 얼굴을 숨겼듯, 방법은 얼마든지 있었다.

‘남천마후라면 대단한 수준의 역용술(逆用術)을 익혔어도 전혀 이상하지 않지.’

내심 중얼거린 나는 재차 노인을 향해 물었다.

“천마표국에서 왔다는 그 중원인들은 지금 어디에 있습니까?”

은영각의 요원과 접선하는 것이 퀘스트 임무지만, 놈들이 아직 근처에 있다면 이야기가 달라진다.

그런 내 마음을 읽은 것처럼 노인이 되물었다.

“왜. 지금이라도 쫓아볼 생각인가?”

“할 수만 있다면요.”

“글쎄, 뜻은 가상하지만 어려울걸세. 이미 보름도 넘게 지난 일이야.”

“그래도 놈들이 향한 방향이나, 짐작하고 계신 목적지가 있다면 시도해 볼 만할 겁니다.”

나는 말할 것도 없고, 이 자리에 있는 화룡각 대원들은 전부 상당한 실력자들이다.

가장 실력이 떨어지는 혁무진조차도 수많은 실전과 죽음의 고비를 겪은 초일류 고수였다.

그러나 그런 내 태도에도 노인은 피식 웃을 뿐이었다.

“무리일세.”

“어르신. 아직 이해하지 못하신 것 같은데…….”

“이해하지 못한 건 내가 아니라 자네지. 그 중원인들은 모두 죽었거든.”

순간 멈칫한 내가 되물었다.

“예?”

“말 그대로일세. 횡액을 입은 이들 중에는 부족의 전사들도 수두룩했는데 그런 이들이 눈 뜨고 당했겠나? 중원인들 역시 전부 죽었어. 극독에 중독되어 얼마 가지 못하고 쓰러진 시신들을 발견했지.”

“……!”

“자네들이 아무리 날고 기는 재주가 있다 한들, 저승까지 쫓아갈 방도는 없다네. 그리고 그건…….”

흐려지는 말꼬리. 다음 순간 노인이 한숨처럼 말을 이었다.

“이미 늙을 대로 늙은 은영각 요원도 마찬가지지.”

벌컥. 벌컥.

독한 화주를 끝까지 들이킨 노인이 나를 향해 빙긋 웃어 보였다.

“반갑네, 열화신룡 진태경.”
```

## Final English reading copy

```markdown
# Chapter 619

Poison Flower Pavilion…

It was a name that suited Nanman, a land crawling with all kinds of venomous beasts. The catch was that it looked more like a crumbling mansion than an inn or pleasure house.

*If the Thousand-Faced Fox’s directions were right, this should be the place.*

As I stared suspiciously at the wooden building that looked old enough to crumble at any moment, the atmosphere surrounding the outsiders grew more hostile by the second.

“You fucking Han bastards!”

“Go back to your own land!”

Whoosh! Crack!

Sama Pyo dodged the rock flying toward the back of his head and muttered with a sigh,

“Pavilion Master, we’d better just go inside. Unless we plan to fight them right now.”

“Fighting them is out of the question.”

At least this time, he was completely right.

We couldn’t turn every native in Nanman into an enemy the moment we arrived.

I glanced at the group of non-Han locals radiating a murderous aura, then opened the door to the Poison Flower Pavilion.

Creeeeak.

The ancient wooden door let out a weak scraping sound.

Inside the inn, everything was steeped in dim light and a gloomy atmosphere. The patrons sitting at crude tables scattered around the room like weeds turned their heads toward us.

“Faces I’ve never seen before… Han Chinese?”

“Caw, spit.”

Is this a Hydra?

The people around here used phlegm like a passive Skill.

The ethnic patrons spat onto the dusty floor and rose from their seats, their faces flushed red.

“Those Han bastards dare come here of all places. Are they desperate to die?”

“I’ve lost my appetite for liquor. Let’s leave. Nothing good can come from staying here with those bastards.”

Bang!

When the door slammed shut behind them, Ju Hwaran spoke with a troubled expression.

“Something must have gone badly wrong. It definitely wasn’t this bad the last time I came here.”

Song Ilseom nodded in agreement.

“I think so too. It’s true that the ethnic groups of Nanman are wary, but Yeongin, which is closest to the Central Plains, was different.”

“That’s right. It wasn’t common, but merchants and Escort Bureaus from the Central Plains used to travel through here. But why…”

Ju Hwaran let her voice trail off when an elderly voice suddenly interrupted from somewhere.

“Why? Because of that Escort Bureau. Those Han bastards just like you.”

We weren’t the only ones left in the Poison Flower Pavilion.

The old man, who had been sleeping off his liquor until a moment ago, continued while rubbing his bent back.

“You’ve all been cursed with bad luck. You lot, for crawling all the way into Nanman without knowing what you were getting into. And some old man whose business is about to be ruined because of fearless Han bastards like those.”

I realized who the old man was and asked,

“Are you the owner?”

The old man looked at me in surprise when he heard the fluent language of the locals flowing from my lips.

“You can speak our language. Are you perhaps one of the Miao people?”

“No.”

“Then you don’t look like the Bai or Man people either. Judging by your face, you’re definitely Han Chinese… but you speak remarkably well. I’d believe you were born and raised here.”

As expected of the *Integrated Language Pack*. It certainly did its job.

Even Ju Hwaran looked surprised by my fluent pronunciation.

“When did you learn the language of the ethnic groups?”

“Hmm. Well, that…”

Since I couldn’t exactly explain everything, I let my voice trail off and answered casually.

“I just happened to pick up the skill. It’s nothing more than a miscellaneous trick.”

Hyuk Mujin, sitting beside me, muttered under his breath,

“The only things our Captain used to know were drinking, women, and gambling…”

“You little shit.”

Bam!

“Urgh!”

The old man clicked his tongue as Hyuk Mujin collapsed, clutching his solar plexus.

“That one sure picks only things worth getting hit for.”

“He’s always like that, so don’t worry about him… Wait. Can you speak Chinese?”

“To a degree. When I was young, I served as an interpreter for the Han Chinese several times.”

The old man answered as though it were nothing important, then pointed at Song Ilseom with a finger reduced to little more than bone.

“That dark-looking fellow seems familiar. Did you perhaps come here around three years ago?”

Strictly speaking, Ju Hwaran should have been the most eye-catching person there. But perhaps because she was wearing a human-skin mask, the old man recognized Song Ilseom first.

Song Ilseom silently nodded, and the old man slapped his knee.

“I knew it. Your name was probably Dragon King…”

“It was the Yongbong Escort Bureau. Not Dragon King.”

“Right. The Yongbong Escort Bureau. Unlike the other merchant groups and Escort Bureaus from the Central Plains, you Han Chinese came here two or three times a year, so I remember you clearly.”

For someone who remembered it so clearly, he got the name wrong right from the start.

I held back the words itching to leave my mouth and asked the question I had wanted to pose to the old man for a while.

“But what did you mean earlier?”

“Hm? What about?”

“You said things had become like this because of an Escort Bureau. To quote you exactly, you said it was because of Han bastards like us.”

The old man asked back with a blank expression.

“I did? When?”

“What? You clearly said…”

“I don’t remember a thing.”

As if hell he didn’t. Realizing something from the old man’s attitude, I spoke with a sigh.

“Food. Can you prepare it right now?”

“Ah, of course I can. I can make anything as long as you pay, so don’t worry.”

At the mention of food, Taishan sprang up from where he had been lying facedown on the table with a dying expression.

“Taishan wants five-spice pork!”

“So there’s one fellow here who’s absurdly full of energy. Then I’ll prepare chicken.”

“Why chicken? Taishan hates chicken! Five-spice pork!”

I had no idea why his request for five-spice pork had somehow been changed to chicken, but for now, we needed to keep the old man in as good a mood as possible.

I immediately called out the name of the one person who could stop Taishan from throwing a fit.

“Ma Pyo. What are you doing?”

“It’s Sama Pyo.”

“Right, Sa-pyo.”

“…”

Sama Pyo glared at me with an unpleasant expression, then turned to Taishan.

“Taishan. Enough. Sit down.”

While he calmed Taishan, the old man casually held out his hand.

“What is it?”

“Payment in advance.”

“Ah.”

“Let’s see. One chicken per person is the minimum, so we’ll need five chickens. And at one silver nyang per chicken… That comes to ten silver nyang.”

“…Ten silver nyang? Even if it’s one nyang per chicken, that should be five silver nyang.”

“Is that so? Then let’s make it two nyang per chicken.”

“What?”

The old man answered boldly,

“Ah. I said let’s make it two nyang per chicken.”

“…”

“If you don’t like it, spit on the floor and leave. For your information, there isn’t another village within a hundred li.”

Talk about shameless price gouging. If he’d been born in Yongsan[^1] some fifty years ago, he would have become a landlord.

[^1]: A central Seoul district where decades of development drove real-estate values sharply upward.

*I wondered why we hadn’t run into bandits on the way here. Turns out they were in the inn, not the mountains.*

The price was no different from highway robbery, but this wasn’t the time to save money.

I took ten silver nyang from the well-filled pouch of expenses I had received from the Murim Alliance and handed them to the old man.

“Here. Ten silver nyang.”

“For a Han, you’re surprisingly reasonable.”

Rustle.

The old man swept up the gleaming silver with a grin.

“That aside. What about liquor?”

“No, thank you.”

“Drink.”

“…”

“I said drink.”

I no longer had the strength to answer.

With a gloomy expression, I opened my pouch again.

* * *

Our first meal in Nanman was impressive in an entirely different sense.

There was a chicken dish so thin and scrawny it looked malnourished. And there was strong liquor that clearly looked like someone had already drunk from it and left the rest behind.

It was astonishing that the old man charged us dozens of silver nyang for this, but even that paled beside the fact that a considerable portion of it had gone into his mouth.

“Burp. That hit the spot.”

“…”

Why were you the one who ate well instead of us?

The question rose all the way to the back of my throat, but I barely managed to swallow it down. We had obtained information in exchange for offering him money and a meal.

“The Heavenly Demon Escort Bureau?”

“That’s right. As I recall, they definitely said they came from Sichuan. There was one woman, and with the other men, there were nearly thirty of them.”

The old man nodded and continued with his face flushed from the liquor.

“At first, everyone thought nothing of it. Han Chinese had come to Yeongin more than once or twice, and their group wasn’t particularly large.”

But that had been a miscalculation.

His eyes red from drink, the old man slowly recalled what had happened that day.

“Something no one could have expected happened. The people from a nearby village held a feast for them and treated them as guests, but every last one of them was slaughtered overnight.”

“…”

“Fortunately, our village avoided the disaster. But when we checked later, we found that some two hundred people had died that very night. Men, women, children, even the elderly. Not a single person survived. Needless to say, those Han bastards were responsible.”

“Damn.”

It was a shocking and horrific story. Only now did I fully understand the hostile looks and oppressive atmosphere that had been directed at us.

Two words came to mind.

*Dark Heaven. And the Southern Heaven Demon Empress.*

It was hardly an overreaction to be troubled by one woman who had been part of the Heavenly Demon Escort Bureau.

I exchanged glances with the Fire Dragon Pavilion members, who had been listening with grim expressions, then took a sheet of paper from my inventory.

“Sorry to interrupt, but could you take a look at this?”

“What is it?”

The paper I had taken out contained a drawing.

More precisely, it was a likeness of Honglan—or rather, the Southern Heaven Demon Empress—created from the testimony and memories of several people, including me.

I showed it to him just in case, but the old man’s reaction was lukewarm.

“That artist is remarkably skilled. But who is this woman?”

“Hmm, no. I was just wondering if you recognized her.”

“I’ve never seen the woman in that drawing. If a woman were this beautiful, I would have remembered her somehow. I may be old, but I’m still a man.”

It wasn’t the response I had been hoping for, but I wasn’t terribly disappointed.

Whatever her character might have been, the Southern Heaven Demon Empress possessed a striking appearance. Just as Ju Hwaran had hidden her face with the human-skin mask Song Ilseom made for her, she could have used any number of methods.

*It wouldn’t be strange at all for the Southern Heaven Demon Empress to have mastered an extraordinary disguise technique.*

I muttered inwardly, then asked the old man again,

“Where are the Central Plains people who claimed to have come from the Heavenly Demon Escort Bureau now?”

The Quest required us to make contact with an agent of the Hidden Shadow Pavilion, but if those people were still nearby, that changed things.

As if he had read my thoughts, the old man asked,

“Why? Are you thinking of chasing after them even now?”

“If we can.”

“Well, it’s an admirable thought, but it’ll be difficult. More than fifteen days have already passed.”

“Even so, if you know which direction they went or have a destination in mind, it should be worth trying.”

Every Fire Dragon Pavilion member present was highly skilled, myself included.

Even Hyuk Mujin, the least skilled among us, was a First Rate master who had endured countless real battles and brushes with death.

Yet despite my attitude, the old man merely let out a short laugh.

“It’s impossible.”

“Old man. I don’t think you understand yet…”

“I’m not the one who fails to understand. You are. Every one of those Central Plains people is dead.”

I paused for a moment, then asked,

“What?”

“I mean exactly what I said. There were countless tribal warriors among those who suffered that calamity. Do you think people like that would have stood by and let themselves be slaughtered? The Central Plains people all died too. We found their bodies after they were poisoned with deadly venom and collapsed before they could get very far.”

“…”

“No matter how skilled you are, there’s no way to chase them into the afterlife. And the same goes for…”

His voice trailed off. A moment later, the old man continued with a sigh.

“The Hidden Shadow Pavilion agent, who’s already old as dirt.”

Gulp. Gulp.

The old man drained the strong liquor to the last drop, then smiled at me.

“Good to meet you, Blazing Flame Divine Dragon Jin Taekyung.”
```

<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0628.txt",
      "sha256": "3b19002d81dd71589c98b5e25e0e00095c9905e3267cd341cd308c87ab5d0f7c",
      "bytes": 12831
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "b373e21cf403e110b64be02d9096f60cff58a8f03565c35b9bb8281ee9d9d03e",
      "bytes": 2341
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "527fe15f8aa215b5254b70898f96e6339f8ec8fba9191e68decb2a6d0fc445b6",
      "bytes": 193641
    },
    {
      "path": "characters/Baeksang.md",
      "sha256": "108176e50b3f781c862860ca0ed8fe9e41c051a5f872292ce4610f71c43c73a3",
      "bytes": 695
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "23d779b6d8e5ae1152f53f1816321affdf368e5280573a3c86dd8048eb31d994",
      "bytes": 553
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "386b9de9228262c3ce401f869974f256fd452dd79651ebc31e9c65fce2ceb153",
      "bytes": 1857
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "e52c5129741c3ac0c1b2a1b8250a4ccb21cee241822a6080fe1febf8ef8b6262",
      "bytes": 622
    },
    {
      "path": "characters/Yayul Cheok.md",
      "sha256": "ef4355a28e31e7b9be968d606813f1b0b8bba3ca8c9b23546b95a4502f64d678",
      "bytes": 912
    },
    {
      "path": "characters/Yayul Mok.md",
      "sha256": "0f1dfc5bd157323d27b554b71f28dbe8712e31b75200205daece336f822a375a",
      "bytes": 871
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "125f5eb0209cf9b4c3184ed15eda2fcee1dd1b93d46e304ec7f1a7ac2915ff71",
      "bytes": 199327
    }
  ],
  "estimated_tokens": 10732
}
-->

# Durable State Update — Chapter 628

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 628. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 628. Profile updates may replace only one
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
  "chapter": 628,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 628,
    "continuity_sources": [628],
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
    "The Fire Dragon Pavilion is staying in temporary lodging within the Nanman Beast Palace after being welcomed by Yayul Cheok.",
    "The Nanman Beast Palace's hostile treatment of the Fire Dragon Pavilion was driven by resentment over the Heavenly Demon Escort Bureau incident and the Great Faction War.",
    "Yayul Mok has apologized for the mistreatment and promised to replace the responsible staff and prevent a recurrence.",
    "Nanman sent approximately ten thousand warriors to the Great Faction War, and fewer than a quarter returned alive.",
    "Yayul Cheok lost two sons and a daughter in the Great Faction War.",
    "Baeksang lost a beloved son in the Great Faction War.",
    "Yayul Mok's three older siblings died in the Great Faction War, leaving him Yayul Cheok's only surviving son and Young Palace Lord.",
    "Yayul Mok is Yayul Cheok's only son for three generations and serves as Young Palace Lord of the Nanman Beast Palace.",
    "Baeksang is the great chieftain of the Bai people, one of Nanman's four most powerful great tribes.",
    "Baeksang is Yayul Cheok's sworn younger brother and childhood companion, but they are now estranged over the Murim Alliance issue.",
    "Baeksang watches Jin Taekyung with cold scrutiny, but the reason for his interest remains unknown."
  ],
  "continuity_sources": [
    627,
    626
  ],
  "open_questions": [
    "Why does Baeksang oppose joining the Murim Alliance despite his lifelong bond with Yayul Cheok and their shared service in the Great Faction War?",
    "What is the meaning of Baeksang's cold scrutiny of Jin Taekyung?",
    "Will Yayul Cheok overcome the previous tribal council's opposition and bring the Nanman Beast Palace into the Murim Alliance?",
    "Are the Bai people and the other tribes aligned behind Baeksang's opposition?",
    "Was the timing of the Heavenly Demon Escort Bureau massacre connected to Dark Heaven's scheme?"
  ],
  "safe_through": 627,
  "temporary_decisions": [
    "Use Baeksang for 백상 and do not treat White Elephant as a separate alias.",
    "Use sworn younger brother for 불알 동생 in the relationship between Yayul Cheok and Baeksang.",
    "Use Jiang Taigong for 강태공 and Jindro for 진드로.",
    "Render 황개 as Hwang Gae and 똥개 as Ddong Gae."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 무신     | **Martial God**               | —              |
| 열화문    | **Fire Gate Clan**               |
| 무림맹    | **Murim Alliance**               |
| 남만야수궁  | **Nanman Beast Palace**          |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 후기지수   | **young prodigy** / **rising martial artist**    | Contextual, not a title                               |
| 중원     | **Central Plains**                               |                                                       |
| 표국     | **Escort Bureau**                            |
| 청해     | **Qinghai**            |
| 정마대전   | **Great Faction War**         |
| 백상 | **Baeksang** | Great chieftain of the Bai people and Yayul Cheok's sworn younger brother. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 야율척 | **Yayul Cheok** | Beast Miao King and lord of the Nanman Beast Palace. |
| 야율목 | **Yayul Mok** | Young Palace Lord of the Nanman Beast Palace. |
| 교관 | **Instructor** | Kim Hwajong's former Hunter Training Center role and address. |
| 숙부 | **Uncle** | Lee Seowol's shortened address for Cheol Mubaek. |
| 한족 | **Han Chinese** | Ethnic designation used by the steppe chieftains. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 일원 | **One Origin** | Named Tang Clan organizational unit in Tang Sadok's mobilization order. |
| 묘족 | **Miao people** | Ethnic group the Escort Bureau expects to encounter near Yunnan. |
| 야수묘왕 | **Beast Miao King** | Leader of the Miao people and master of the Nanman Beast Palace. |
| 소평 | **So Pyeong** | Alliance office worker assigned to prepare a report. |
| 백족 | **Bai people** | Ethnic group encountered in Yeongin. |
| 천마표국 | **Heavenly Demon Escort Bureau** | A Sichuan group whose arrival preceded the Yeongin massacre; all members were later found dead from venom. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 야율목 | 진태경 | Nanman_Beast_Palace_Young_Palace_Lord_to_Han_intruder_and_Murim_Alliance_Pavilion_Master | you | formal but hostile | Asks Jin's identity and orders him to follow after learning he belongs to the Murim Alliance. |
| 진태경 | 야율목 | Fire_Dragon_Pavilion_Pavilion_Master_to_Nanman_Beast_Palace_Young_Palace_Lord | Mok | casual, teasing, and insulting | Calls him rude and later addresses him as 목아 while jokingly claiming they are friends. |
| 야율목 | 야율척 | Young_Palace_Lord_to_Palace_Lord | Palace Lord | ceremonial and deferential | Yayul Mok kneels with his guards and formally greets Yayul Cheok upon his arrival. |
| 야율척 | 야율목 | Palace_Lord_to_Young_Palace_Lord | Mok | authoritative and familiar | Yayul Cheok questions Mok's unannounced departure and later addresses him as 목아 while discussing Nanman's tribes. |
| 야율척 | 진태경 | Nanman_Beast_Palace_Palace_Lord_to_Jeok_Cheongang's_Disciple | you / Disciple of Old Master Jeok / Jin Taekyung | rough, testing, and later welcoming | Yayul Cheok questions Taekyung as a suspected culprit, strikes him as a test, and then welcomes him after recognizing Jeok's Disciple. |
| 진태경 | 야율척 | Fire_Dragon_Pavilion_Pavilion_Master_to_Nanman_Beast_Palace_Palace_Lord | Great Hero Yayul Cheok | formal and deferential | Taekyung gives Yayul Cheok a formal greeting as the nineteenth successor of the Fire Gate Clan. |
| 야율목 | 백상 | nephew_to_father's_sworn_younger_brother | Uncle Baeksang | ceremonial and deferential | Yayul Mok formally greets Baeksang as he arrives at the stone door. |
| 백상 | 야율목 | father's_sworn_brother_to_nephew | you | cold and formal | Baeksang questions Yayul Mok about his return, the pasture fire, and the Palace Lord's whereabouts. |
| 야수묘왕 | 백상 | sworn_older_brother_to_sworn_younger_brother | Baeksang | familiar and bittersweet | Yayul Cheok offers Baeksang his preferred fruit wine and asks why he came. |

## Listed compact profiles

### Baeksang.md

# Baeksang (백상)

- **Safe through:** Chapter 627
- **Aliases:** None
- **Role:** Baeksang is the middle-aged great chieftain of the Bai people, one of Nanman's four most powerful great tribes.
- **Personality:** Cold, rigid, meticulous, and politically resolute, with a deep but guarded attachment to his sworn elder brother.
- **Voice:** Rigid, formal, restrained, and emotionally distant.
- **Relationships:** Baeksang is Yayul Cheok's sworn younger brother and childhood companion and Yayul Mok's sworn uncle; he lost a beloved son in the Great Faction War and opposes the Nanman Beast Palace joining the Murim Alliance.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 626
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 625
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple, the Fire Gate Clan's nineteenth successor, and the Pavilion Master of the Fire Dragon Pavilion within the Murim Alliance; he is a Supreme Peak master with the Heavenly Martial Physique and Force, publicly recognized as an S-rank-level Hunter while formally retaining an A-rank license, and he has completed an unnamed cultivation technique designed for even the lowest-rank Hunter to learn without making it easily abusable.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 625
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Yayul Cheok.md

# Yayul Cheok (야율척)

- **Safe through:** Chapter 626
- **Aliases:** Beast Miao King
- **Role:** Yayul Cheok is the over-eighty Beast Miao King, lord of the Nanman Beast Palace, a Supreme Peak master among the Ten Kings, and great chieftain representing the Miao people.
- **Personality:** Boisterous, warmhearted, forthright, playful, and politically conscious of the tribal coalition he leads.
- **Voice:** Rough, loud, convivial, and teasing, becoming authoritative when discussing Nanman's laws or political decisions.
- **Relationships:** Jeok Cheongang is an old acquaintance whom he respects; Baeksang is his sworn younger brother and childhood companion, and they fought together during the Great Faction War; Yayul Mok serves as his Young Palace Lord; Jin Taekyung is Jeok's Disciple whom he welcomes into the Nanman Beast Palace.

### Yayul Mok.md

# Yayul Mok (야율목)

- **Safe through:** Chapter 627
- **Aliases:** None
- **Role:** Yayul Mok is the non-Han Young Palace Lord of the Nanman Beast Palace, a spear-wielding warrior who rides a white tiger, and a halting but capable speaker of Han Chinese.
- **Personality:** Protective of Nanman Beast Palace livestock, quick-tempered toward trespassers, and capable of restraint once he recognizes legitimate authority.
- **Voice:** Blunt, commanding, and formal-polite toward strangers, becoming openly insulting when provoked.
- **Relationships:** Yayul Cheok is the Beast Miao King and Yayul Mok's father; Yayul Mok is his only surviving son after three older siblings died in the Great Faction War, Baeksang is his father's sworn younger brother, and his white tiger is a long-bonded companion.

## Korean source

```text
＃628화



“불과 수십 년 전, 우리는 하나가 되어 한족들을 위해 목숨을 바쳐 싸웠다. 하지만 오늘에 이르러 너희는 우리에게 칼을 겨누었지.”

지금 이 순간, 야율목은 진심으로 분노하고 있었다.

이번 참사 속에서 몰살당한 이들의 숫자가 자그마치 이백여 명. 희생당한 이들의 대부분은 힘없는 노인과 여인, 그리고 아이들이었다.

게다가 그들은 야율목이 속한 묘족(苗族)의 일원이기도 했다. 한데 그런 짓을 벌이고도 감히 도움을 청하다니.

“우리는 이미 많은 피를 흘렸다. 우리를 위해서가 아닌, 너희 한족들을 위해서.”

야율목은 끓어오르는 목소리로 말을 이었다.

“남만은 두 번 다시 헛된 피를 흘리지 않을 것이다. 그러니 더 이상 분란을 일으키지 말고 돌아가라.”

칼날처럼 예리하면서도 단호한 한마디. 참고 있던 말을 모두 쏟아낸 야율목은 후련한 마음으로 눈앞의 한족을 바라보았다.

‘진태경이라고 했지.’

야율목은 반나절 전까지만 하더라도 그에 대해서 잘 몰랐다. 중원에서 이름난 대단한 후기지수라고 얼핏 들었던 것을 빼고는.

하지만 초절정 고수라는 허무맹랑한 소문이 사실이라면 당장 자신이 나고 자란 남만에서도 세 손가락 안에 들만한 전사일지도 모른다.

‘다른 누구도 아닌 아버님의 일권을 막았으니, 그 소문이 사실일지도.’

야율목은 자신의 아버지, 야율척이 얼마나 대단한 사람인지 누구보다 잘 알고 있었다.

불혹이 채 되기도 전에 남만 제일의 전사가 되었고, 묘족을 가장 강성한 부족으로 만들었으며 모두에게 인정받아 남만야수궁의 주인이 되었다.

그뿐인가, 그 대단한 무위로 남만인들을 오랑캐 취급하는 중원의 한족들마저 탄복하게 만들었다.

야수묘왕(野獸苗王)이라는 별호 또한 그때 얻었다고 들었다.

‘아버님과 수를 교환할 만한 상대는 백상 숙부밖에 없다고 생각했는데.’

두 눈으로 직접 목격한 바에 의하면, 기껏해야 자신의 또래인 진태경의 무공은 놀라웠다.

자신은 제대로 볼 수도, 막을 수도 없는 아버지의 일권을 그리 어렵지 않게 막아 냈으니까.

물론 힘을 이겨 내지 못해 일장에 가까운 거리를 물러서긴 했지만, 그것이 진태경을 과소평가할 이유는 되지 않는다.

‘게다가…….’

체격도 크다. 평범한 장정보다 머리 한두 개는 큰 키와 딱 벌어진 어깨. 그리고 옷으로도 감출 수 없는 근육질의 체형.

이렇게 발걸음을 멈춘 채로 눈앞에서 마주하고 있으니, 마치 두 발로 일어선 한 마리의 맹수를 보는 것 같았다.

그래서일까, 아니면 늘 실실 웃고 있던 눈과 입꼬리가 지금은 굳어 있는 탓일까. 야율목은 자신도 모르게 마른침을 꿀꺽 삼켰다.

그때였다.

“야.”

“……!”

“뭘 그렇게 놀라. 그냥 부른 건데.”

불쑥 튀어나온 낮은 목소리에 흠칫 놀란 야율목이 대답했다.

“……왜, 왜 불렀냐.”

“말은 또 왜 더듬어?”

그야 네놈이 정색하고 있으니까 그렇지.

지금까지의 모습은 항상 새 깃털보다 가벼워 보이던 놈이었는데, 얼굴에 웃음기를 지우니 숫제 만근거석(萬斤巨石)을 두고 있는 것 같다.

- 크으으응…….

이런 주인의 마음은 함께 있던 백호에게까지 전해졌다.

야율목은 애써 침착한 척, 덩달아 위축된 애호(愛虎)의 목덜미를 쓰다듬으며 대답했다.

“더, 더듬은 적 없다.”

“…….”

“그런데 왜 부른 거냐. 불렀으면 말을 해라.”

“음. 뭐 별건 아니고.”

묘한 눈빛으로 야율목을 바라보던 진태경이 뒤통수를 긁적이며 말을 이었다.

“말해 줘서 고맙다.”

“어?”

“솔직하게 다 말해 줘서 고맙다고. 나도 아직 잘 모르는 부분이 있었는데, 뭐 덕분에 여러 가지를 알게 됐네. 이쪽 동네 사정도 어느 정도 이해가 되고.”

이게 무슨 소리지?

예상했던 것과는 전혀 다른 반응이다. 말없이 진태경을 빤히 쳐다보던 야율목이 불쑥 입을 열었다.

“그러니까 지금 네가 하는 말이…… 그냥 돌아가겠다는 뜻이냐?”

“음?”

진태경이 고개를 갸웃거렸다.

“그게 그렇게 되나?”

“아니, 이해했다면서?”

“어. 당연히 이해는 했지. 내가 무슨 공감 능력 장애가 있는 것도 아닌데.”

“그런데?”

“그거랑 이거는 별개지.”

“뭐?”

“말하자면 길어져서 입 아프니까. 툭 까 놓고 하나만 묻자.”

자연스럽게 나무에 등을 기댄 진태경이 나직한 목소리로 말을 이었다.

“넌 진심으로 정마대전이 한족들만을 위한 전쟁이었다고 생각하냐?”

“……!”

“내친김에 하나 더. 그 전쟁에서 희생된 남만인들이 아무 목적 없이 개죽음을 당했다고 생각해?”

“그건…….”

“그건, 뭐?”

야율목은 문득 말문이 막혔다. 어째서인지 쉽게 대답이 나오지 않았다.

그리고 그가 어지러운 머릿속에서 대답할 말을 찾는 사이, 나직한 목소리가 귓가를 파고들었다.

“쉽게 대답하지 못하는 이유는 두 가지겠지. 첫째. 마음속으로는 내 말이 사실인 걸 알지만 인정하기 싫어서. 그리고 둘째.”

두 개의 손가락을 곧게 편 진태경이 툭 내뱉었다.

“네가 아직 생각 머리 없는 애새끼라서.”

“그게 무슨…….”

“나한테 묻지 말고 스스로 곰곰이 생각해 봐라. 남만야수궁이 왜 그 많은 전사를 데리고 수만 리나 떨어져 있는 중원을 도왔는지. 단순히 아주 오래전에 열화문의 선조가 혼란스럽던 남만을 정리해 줘서? 그게 사실이면 니 옆에 있는 백호가 웃겠다.”

“……!”

“뭐, 너희 남만인 중 대부분은 첫 번째 이유 때문에 입맹(入盟)을 반대하고 있겠지. 애꿎은 피만 흘렸다고 생각하니까. 그 역사를 다시 한번 반복하기 싫으니까.”

진태경이 한숨처럼 말을 이었다.

“따지고 보면 아주 틀린 말도 아냐. 누가 시발, 전쟁하고 싶어 하냐. 개같이 싸워서 땅이랑 금은보화를 얻으면 뭐 해. 사방에서 사람이 개미처럼 죽어 나가는데. 물론 그 개미 중의 일부는 내 친구, 가족. 연인이지. 아니면 나나 너 자신일 수도 있고. 근데 너 여자친구 있냐?”

불쑥 튀어나온 질문에, 야율목은 엉겁결에 고개를 가로저었다.

“전여친은?”

“지금 네가 말하는 그 여친이라는게 정확히 뭐지?”

“연인. 혹은 애인. 남자와는 다른 신체적 구조를 지녔으며 너와 애틋한 마음으로 교제하는 존재.”

“어, 없다.”

“아. 있었는데?”

“없다.”

“그러니까. 있었는데?”

“……단 한 번도 없었다.”

“지금 나이가?”

“스물여섯.”

“녀석. 동자공 유망주였네. 이대로 오십 년만 버티면 무신도 되겠다. 그럼 연인은 희생자 명단에서 빼자.”

어째서인지 흐뭇하게 웃는 진태경의 모습에 기분이 나빠진 야율목은 맥이 탁 풀렸다.

상대는 도무지 종잡을 수 없는 놈이었고, 종잡을 수 없는 대화를 하고 있었다.

“도대체 하고 싶은 말이 뭐냐? 거기에서 왜 연인 이야기로 빠져?”

“글쎄. 나도 잘은 모르겠는데 한 가지는 확실하지.”

희미하게 어려있던 웃음기를 지운 진태경이 담담하게 말을 이었다.

“오래전 고향을 떠나 중원에서 스러져 간 남만인들의 희생이, 목적 없는 개죽음이 아니라는 것. 그리고 같은 일이 벌어진다면 이번에도 마찬가지일 거라는 것.”

“…….”

“천마표국 일은 진심으로 유감이다. 하지만 그런 미친놈들이 있었다면…… 내 손으로 직접 죽였을 거야.”

“너와 같은 한족인데도?”

“그게 무슨 상관인데?”

기분 탓인지. 오늘따라 여러 번 말문이 막히는 것 같다.

입을 꾹 다문 채 진태경을 응시하던 야율목이 한마디를 툭 내뱉었다.

“아무리 듣기 좋은 말을 한다 해도 남만은 중원을 돕지 않아.”

“어려울 것 같긴 한데, 설득은 해 봐야지.”

“헛수고야.”

“뭐?”

“이미 결정된 사안이나 다름없다. 보름 전 열린 일 차 부족 회의에서 결론이 났어.”

“그 말은 이 차도 있다는 소리로 들리는데.”

“남만은 넓고, 서른두 개의 부족이 한자리에 모이려면 상당한 시간이 소요된다. 그렇기에 아버님을 비롯한 네 명의 대족장들이 먼저 사안을 검토하지.”

“그 결과가 입맹 반대다? 계속해 봐.”

“사흘 뒤, 이 땅의 모든 부족이 한자리에 모여 회의를 열 것이다. 하지만 아버님을 제외한 대족장들은 이미 마음을 굳혔으니, 크게 달라지는 것은 없을 거다.”

야율목의 말은 사실이었다. 남만야수궁은 화합의 상징이었지만, 그렇다고 해서 부족 간의 평등을 의미하는 것은 아니었다.

백족의 대족장인 백상을 필두로 세 명의 대족장이 뜻을 모았다면, 제아무리 남만 제일의 전사이자 궁주인 야수묘왕이라 할지라도 제멋대로 입맹을 결정할 수 없었다.

‘그것이 이곳의 규칙이니까.’

마음속으로 뇌까린 야율목은 신중한 눈빛으로 진태경을 주시했다.

저 젊고 강한 중원의 한족 놈은 어떻게 반응할까.

남만의 합류가 사실상 불가능해진 지금, 놈이 보여 줄 반응이 궁금했다.

아무래도 실망하겠지? 그게 아니라면 어떻게든 설득해 보겠다고 용을 쓸 것이 틀림 없…….

“우선 손 닿는 데까지는 해 보고, 안 되면 어쩔 수 없지.”

“어?”

야율목은 자신도 모르게 당황했다. 진태경의 반응이 예상외로 너무나도 담담했고, 태평스러웠기 때문이었다.

“그. 어차피 결과는 정해져 있다니까?”

“응. 근데 아직 끝난 건 아니라면서?”

“그건 사실이긴 한데…….”

뭐지, 이거.

야율목은 곤혹스러운 마음으로 물었다.

“어떻게든 우리를 설득해야 하지 않나?”

“그러니까 우선은 해 본다고. 안 되면 그때는 돌아가야지. 물론 그전에 더 중요한 것부터 처리하고.”

“더 중요한 거라면…….”

“뭘 오해하고 있나 본데.”

진태경이 턱을 긁적이며 말을 이었다.

“난 이곳에 외교관 자격으로 온 게 아냐. 굳이 따지자면 소방관으로서 온 거지.”

“소방관? 그게 뭐지?”

“음. 불 끄는 사람.”

“오자마자 목초지에 불 지르지 않았나?”

진심이 담긴 야율목의 물음에 잠깐 침묵하던 진태경이 대답했다.

“뭐, 그건 단순한 비유가 그렇다는 거지. 막말로 내가 누구를 설득하는 데에 재주가 특출난 사람은 아니니까.”

“그 말은 맞는 것 같다.”

“……시벌놈. 괜히 열 받네. 아무튼 남만이 합류하지 않는다면 아쉽지만, 노력해도 안 되면 어쩔 수 없지.”

“하지만 네놈은 한족이고, 게다가 무림맹 소속이지 않나.”

“그래서?”

“자세한 사정은 정확히 모르지만, 중원이 위기에 처했다는 것 정도는 익히 알고 있다. 그런데 어떻게든 도움을 청해도 모자랄 판에, 우리를 도우러 왔다고?”

희한한 생물을 바라보는 듯한 야율목의 눈빛에, 진태경이 피식 웃었다.

“지난번처럼 목초지에 불나면 어쩔래?”

“당장 꺼야지.”

“왜?”

“꺼트리지 않으면 불길이 사방으로 번질 테니까.”

“좋아. 답 나왔네.”

“……!”

“복잡하게 생각하지 마라. 불이 났으니까 끄려고 하는 것뿐이야. 수십 년 전 고향을 떠나 중원으로 향한 이 땅의 남만인들처럼.”

잠시 침묵하던 야율목이 복잡한 표정으로 입을 열었다.

“그럼 아무런 대가 없이…… 단순히 우리를 돕기 위해 왔단 말이냐?”

“그렇다면?”

“믿을 수 없다.”

“뭐 좋을 대로 생각해라. 아, 물론 그 전에…….”

자연스럽게 돌아서서 걸음을 옮기던 진태경이 정색하며 말을 이었다.

“밥이나 제대로 줘. 개새끼야.”
```

## Final English reading copy

```markdown
# Chapter 628

“Only a few decades ago, we united and risked our lives fighting for the Han Chinese. But now, you’ve turned your swords on us.”

At that moment, Yayul Mok was genuinely furious.

More than two hundred people had been massacred in the recent tragedy. Most of the victims had been powerless old men, women, and children.

They had also been members of the Miao people—the same group Yayul Mok belonged to. And after doing something like that, they still had the nerve to ask for help.

“We’ve already shed enough blood. Not for ourselves, but for you Han Chinese.”

Yayul Mok continued in a voice that boiled with anger.

“Nanman will never shed blood in vain again. So stop causing trouble and go back.”

His words were as sharp and decisive as a blade. After finally saying everything he had been holding back, Yayul Mok looked at the Han Chinese man before him with a lighter heart.

*He said his name was Jin Taekyung.*

Until half a day ago, Yayul Mok hadn’t known much about him. Aside from hearing in passing that he was a renowned young prodigy from the Central Plains, he had known nothing.

But if the absurd rumor that Jin Taekyung was a Supreme Peak master was true, he might be one of the three greatest warriors in Nanman—the land where Yayul Mok had been born and raised.

*He blocked Father’s punch, of all things. Maybe the rumor is true.*

Yayul Mok knew better than anyone how formidable his father, Yayul Cheok, was.

Before he had even reached forty, Yayul Cheok had become the greatest warrior in Nanman. He had made the Miao people the strongest tribe, and after earning everyone’s recognition, he had become the lord of the Nanman Beast Palace.

And that wasn’t all. Through his astonishing martial power, he had even made the Han Chinese of the Central Plains—who treated the people of Nanman as barbarians—admire him.

Yayul Mok had heard that his father had earned the sobriquet Beast Miao King around that time.

*I thought Uncle Baeksang was the only person capable of exchanging blows with Father.*

But according to what he had witnessed with his own eyes, Jin Taekyung’s martial arts were astonishing, despite him being at most around Yayul Mok’s age.

He had blocked Yayul Cheok’s punch without much difficulty—a punch Yayul Mok himself couldn’t properly see, much less stop.

Of course, Jin Taekyung had been unable to withstand its force and had retreated nearly one jang, but that was no reason to underestimate him.

*And besides…*

He was big.

He was a head or two taller than an ordinary grown man, with broad shoulders and a muscular build that even his clothes couldn’t conceal.

Standing still and facing him from such a short distance, Yayul Mok felt as if he were looking at a beast that had risen onto two legs.

Perhaps that was why. Or perhaps it was because the eyes and the corners of his mouth—which had always seemed to be smiling foolishly—were now completely rigid.

Without realizing it, Yayul Mok swallowed dryly.

That was when it happened.

“Hey.”

“……!”

“Why are you so startled? I just called you.”

Yayul Mok flinched at the low voice that suddenly cut in, then answered.

“……Wh-why did you call me?”

“Why are you stuttering?”

*Because you’re standing there with that terrifying look on your face, you bastard.*

Until now, Jin Taekyung had always seemed lighter than a feather. But with the smile wiped from his face, it was as if a massive boulder weighing ten thousand jin stood before Yayul Mok.

—Grrr…

The owner’s feelings had even reached the white tiger beside him.

Yayul Mok pretended to remain calm as he stroked the neck of his beloved tiger, which had shrunk back along with him.

“I-I wasn’t stuttering.”

“……”

“Why did you call me, then? If you called me, say what you want.”

“Hmm. It’s nothing important.”

Jin Taekyung looked at Yayul Mok with an odd expression, scratched the back of his head, and continued.

“Thanks for telling me.”

“Huh?”

“I mean, thanks for telling me everything honestly. There were still some things I didn’t know, but thanks to you, I learned quite a few things. I understand the situation around here a little better now, too.”

*What was he talking about?*

This was a completely different reaction from what Yayul Mok had expected.

After staring at Jin Taekyung in silence, he suddenly opened his mouth.

“So what you’re saying is… you’re just going to go back?”

“Hm?”

Jin Taekyung tilted his head.

“Does it work that way?”

“No, but you said you understood.”

“Yeah. Of course I understand. It’s not as if I have some kind of empathy disorder.”

“Then?”

“That’s separate from this.”

“What?”

“This’ll take too long if I explain everything, and my mouth hurts. So let’s cut to the chase and ask one thing.”

Jin Taekyung naturally leaned his back against a tree and continued in a low voice.

“Do you sincerely believe the Great Faction War was a war fought only for the Han Chinese?”

“……!”

“And since we’re on the subject, do you think the Nanman people who died in that war died like dogs for no reason?”

“That’s…”

“That’s what?”

Yayul Mok suddenly found himself unable to speak.

For some reason, no easy answer came to mind.

As he searched through his confused thoughts for something to say, Jin Taekyung’s quiet voice pierced his ears.

“There are two reasons you can’t answer easily, right? First, you know in your heart that what I’m saying is true, but you don’t want to admit it. And second…”

Jin Taekyung held up two straight fingers and tossed out the words.

“Because you’re still a brainless brat.”

“What the hell does that—”

“Don’t ask me. Think it over carefully yourself. Why did the Nanman Beast Palace bring so many warriors and travel tens of thousands of li to help the Central Plains? Was it simply because the ancestor of the Fire Gate Clan put Nanman, which was in chaos, in order a long time ago? If that were true, the white tiger next to you would laugh.”

“……!”

“Most of you Nanman people probably oppose joining the alliance for the first reason. Because you think you only shed blood for nothing. Because you don’t want to repeat that history.”

Jin Taekyung continued with a sigh.

“If you look at it that way, it isn’t entirely wrong. Who the fuck wants war? So what if you fight like hell and gain land, gold, and silver treasures? People are dying like ants in every direction. And some of those ants might be my friends, my family, or my lover. They could even be me—or you. By the way, do you have a girlfriend?”

At the unexpected question, Yayul Mok shook his head without thinking.

“An ex-girlfriend?”

“What exactly is this ‘girlfriend’ you’re talking about?”

“A lover. Or a romantic partner. A being with a physical structure different from a man’s who dates you while harboring tender feelings for you.”

“Uh, no.”

“Oh. You did have one?”

“No.”

“So you did have one?”

“……I’ve never had one. Not even once.”

“How old are you?”

“Twenty-six.”

“What a guy. A promising candidate for the virgin-boy technique. If you hold out like this for fifty years, you might even become a Martial God. Fine, let’s take lovers off the list of victims.”

For some reason, Jin Taekyung smiled with satisfaction.

Yayul Mok’s mood soured, and all the strength drained from him.

The man was impossible to understand, and he was having an impossible-to-understand conversation.

“What the hell are you trying to say? Why did you suddenly go off on a tangent about lovers?”

“Who knows? I’m not entirely sure myself, but one thing is certain.”

Jin Taekyung’s faint smile disappeared as he continued calmly.

“The sacrifice of the Nanman people who left their homeland long ago and fell in the Central Plains wasn’t a pointless death. And if the same thing happens again, it won’t be pointless this time, either.”

“……”

“I’m sincerely sorry about what happened with the Heavenly Demon Escort Bureau. But if there were people crazy enough to do something like that… I would have killed them myself.”

“Even though they were Han Chinese like you?”

“What does that have to do with anything?”

Perhaps it was his imagination. But for some reason, Yayul Mok felt as if he had been unable to respond several times today.

With his mouth pressed tightly shut, he stared at Jin Taekyung and tossed out one final remark.

“No matter how pleasant your words sound, Nanman will not help the Central Plains.”

“It’ll probably be difficult, but we still have to try persuading you.”

“It’s pointless.”

“What?”

“The matter is as good as decided. The conclusion was reached at the first tribal council held fifteen days ago.”

“That makes it sound as if there’s going to be a second one.”

“Nanman is vast, and it takes considerable time for thirty-two tribes to gather in one place. That is why the four great chieftains, including my father, review matters first.”

“And the result was opposition to joining the alliance? Go on.”

“In three days, all the tribes of this land will gather in one place for a council. But the great chieftains other than my father have already made up their minds, so little will change.”

Yayul Mok’s words were true.

The Nanman Beast Palace was a symbol of harmony, but that did not mean the tribes were equal.

If three great chieftains, led by Baeksang, the great chieftain of the Bai people, united their opinions, then even the Beast Miao King—the greatest warrior in Nanman and lord of the palace—could not decide to join the alliance as he pleased.

*Because those were the rules here.*

Yayul Mok muttered the words inwardly as he watched Jin Taekyung carefully.

How would that young and powerful Han Chinese from the Central Plains react?

Now that Nanman’s joining the alliance was practically impossible, he was curious about what Jin Taekyung would do.

*He’ll probably be disappointed. If not, he’ll surely exhaust himself trying to persuade us somehow…*

“First, I’ll do whatever I can. If it doesn’t work, then it can’t be helped.”

“Huh?”

Yayul Mok was confused without realizing it.

Jin Taekyung’s reaction was so calm and unconcerned that it was completely outside his expectations.

“B-but the result is already decided, isn’t it?”

“Yeah. But you said it isn’t over yet.”

“That’s true, but…”

*What is this?*

Yayul Mok asked in bewilderment.

“Shouldn’t you try to persuade us no matter what?”

“That’s why I said I’d try first. If it doesn’t work, then I’ll go back. Of course, I’ll take care of something more important first.”

“Something more important?”

“You seem to be misunderstanding something.”

Jin Taekyung scratched his chin and continued.

“I didn’t come here as a diplomat. If I had to put it another way, I came here as a firefighter.”

“A firefighter? What is that?”

“Someone who puts out fires.”

“Didn’t you set fire to the pasture as soon as you arrived?”

At Yayul Mok’s genuinely curious question, Jin Taekyung was silent for a moment before answering.

“Well, that was just a metaphor. To put it bluntly, I’m not particularly talented at persuading people.”

“That much seems to be true.”

“…You fucking bastard. Now I’m getting annoyed for no reason. Anyway, it’d be a shame if Nanman didn’t join us, but if trying doesn’t work, there’s nothing we can do.”

“But you’re Han Chinese. And aren’t you also a member of the Murim Alliance?”

“So?”

“I don’t know the exact circumstances, but I know well enough that the Central Plains is in danger. At a time like this, when you should be begging us for help no matter what, you came to help us?”

At Yayul Mok’s gaze, which seemed to be examining some strange creature, Jin Taekyung let out a quiet laugh.

“What are you going to do if the pasture catches fire again like last time?”

“Put it out immediately.”

“Why?”

“If we don’t put it out, the flames will spread in every direction.”

“Good. There’s your answer.”

“……!”

“Don’t overthink it. There’s a fire, so I’m trying to put it out. Just like the Nanman people of this land who left their homeland and headed for the Central Plains decades ago.”

After a brief silence, Yayul Mok spoke with a complicated expression.

“Then are you saying you came here simply to help us… without asking for anything in return?”

“What if I did?”

“I don’t believe you.”

“Believe whatever you want. Ah, but before that…”

Jin Taekyung naturally turned around and began walking. Then he continued with a suddenly hardened expression.

“At least feed me properly, asshole.”
```

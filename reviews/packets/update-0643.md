<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0643.txt",
      "sha256": "a94e9c860a0b52aad9b5e0f32be306ca810963df38e387728571dbba855b73ba",
      "bytes": 13058
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "39d6d7f999505e79725de84247003bf90c6c62b0e25f1e16ec25e72488291e12",
      "bytes": 2154
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "2226d0b4624acff466125247c292c22b0c41eb77b94dba2391c37b56660112c7",
      "bytes": 197800
    },
    {
      "path": "characters/Baeksang.md",
      "sha256": "ef75d0228bd92f9eab54a8c3ae9b41fd33a7c5a796c9b7fc80ae363a1ce790fa",
      "bytes": 808
    },
    {
      "path": "characters/Beast Miao King.md",
      "sha256": "cb4526b3508a529ac3e7a7c319fb0d4e920d417623ebaba116b50e75e96206be",
      "bytes": 560
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "1b3c91fc2d5e4f12d62b1d3afce682adbe8dedb3e7c02c645f201e7cc549f813",
      "bytes": 553
    },
    {
      "path": "characters/Human Butcher.md",
      "sha256": "113f09d4dc40dcd83d2ef63cdb594ab5fca1bcad73b8ce2534ccf5105b40784f",
      "bytes": 667
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "50c0aa38a772fbd2baa46a1041552f4df23e4a53c50ddbac7b03cd4d3c982381",
      "bytes": 1936
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "59544cfc405539060e6dd3399f80fc548c3b36094bdc535760775179d85c4b39",
      "bytes": 622
    },
    {
      "path": "characters/Yayul Cheok.md",
      "sha256": "4b2f3bb2154afc25352bd56bfe5763db890b55fceac48772a531a5570c3dcc76",
      "bytes": 901
    },
    {
      "path": "characters/Yayul Mok.md",
      "sha256": "3d5aff707e20dbe8290e96768775ad0883ceee7e9e06821a1fb360055f1d4468",
      "bytes": 871
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "d8a8f583fa8b4e48f863198396771ec4efbe5cb6302603de77f6c5e661cfcaab",
      "bytes": 203166
    }
  ],
  "estimated_tokens": 11516
}
-->

# Durable State Update — Chapter 643

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 643. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 643. Profile updates may replace only one
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
  "chapter": 643,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 643,
    "continuity_sources": [643],
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
    "Muyaho, Yayul Mok's White Tiger, returns and uses its roar to summon the Nanman Beast Palace party.",
    "The hundred elite warriors who went to Ailao Mountain return to the Nanman Beast Palace by dawn with Baeksang and Yayul Mok.",
    "Jin Taekyung completes the Quest [My Love, Don't Cross That Swamp] and receives five Top-Grade Poison-Warding Pearls, the Achievement [How'd You Get Back?], and the Title [Poisonblood Grounds Pioneer].",
    "Nanman's tribal chieftains recognize that Jin's contribution to resolving the Ailao Mountain incident was substantial.",
    "The tribal grand council has thirty-two seats; thirty-one are occupied before two unidentified figures approach through the reopened stone gate.",
    "Approximately two hundred elite warriors of Ailao Mountain remain alive inside the Thousand-Year Spider webs and await evacuation.",
    "The Thousand-Year Spider webs appear to shield their victims from the Poison Mist, so the survivors remain wrapped until they can be transported.",
    "The missing ferocious beasts have not been found in the Poisonblood Grounds.",
    "Dark Heaven's involvement in the Thousand-Year Spider attack remains suspected but unconfirmed.",
    "The purpose of Ailao Mountain's Wraith remains unknown.",
    "The nature of the pure-white eggs in the Poisonblood Grounds remains unknown."
  ],
  "continuity_sources": [
    642
  ],
  "open_questions": [
    "Who are the two figures approaching the tribal grand council, and why are two seats vacant?",
    "Where did the missing ferocious beasts go?",
    "Did Dark Heaven influence the Thousand-Year Spider attack, and why did it occur on the final day of the tribal competition?",
    "What does Ailao Mountain's Wraith intend to do?",
    "What are the pure-white eggs in the swamp, and what will emerge from them?"
  ],
  "safe_through": 642,
  "temporary_decisions": [
    "Use Sword Demon for 검마.",
    "Use two-headed horn snake for 쌍두각사.",
    "Use black frog for 흑와.",
    "Use golden bee for 금봉.",
    "Use Poisonblood Grounds Pioneer for 독혈지 개척자."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 열화문    | **Fire Gate Clan**               |
| 무림맹    | **Murim Alliance**               |
| 남만야수궁  | **Nanman Beast Palace**          |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 중원     | **Central Plains**                               |                                                       |
| 문주     | **Sect Leader**                              |
| 퀘스트              | **Quest**                      |
| 정마대전   | **Great Faction War**         |
| 귀가      | **your family**                                                 |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 백상 | **Baeksang** | Great chieftain of the Bai people and Yayul Cheok's sworn younger brother. |
| 야수묘왕 | **Beast Miao King** | Leader of the Miao people and master of the Nanman Beast Palace. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 야율척 | **Yayul Cheok** | Beast Miao King and lord of the Nanman Beast Palace. |
| 야율목 | **Yayul Mok** | Young Palace Lord of the Nanman Beast Palace. |
| 한족 | **Han Chinese** | Ethnic designation used by the steppe chieftains. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 열화신룡 | **Blazing Flame Divine Dragon** | New sobriquet bestowed on Jin Taekyung. |
| 묘족 | **Miao people** | Ethnic group the Escort Bureau expects to encounter near Yunnan. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 오독문 | **Five Poisons Sect** | Formerly dominant Nanman faction destroyed by the Fire Gate Clan. |
| 화룡각 | **Fire Dragon Pavilion** | New name chosen for Taekyung's pavilion. |
| 화룡각주 | **Fire Dragon Pavilion Master** | Unique Title awarded to Jin Taekyung. |
| 성하 | **Seongha** | Hunter named during the cave battle. |
| 백족 | **Bai people** | Ethnic group encountered in Yeongin. |
| 만족 | **Man people** | An ethnic group mentioned by the Poison Flower Pavilion owner. |
| 애뇌산 | **Ailao Mountain** | Mountain crossed by the party on the route to the Nanman Beast Palace. |
| 이족 | **Yi people** | One of Nanman's four great tribes. |
| 내궁 | **Inner Palace** | The inner compound of the Nanman Beast Palace. |
| 독혈지 | **Poisonblood Grounds** | Hidden poisonous region created by the Five Poisons Sect inside Ailao Mountain. |
| 야율 | **Yayul** | Name used in Taekyung's colloquial address to the Beast Miao King. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 중년인 | 진태경 | veteran civilian Hunter to celebrated allied Hunter | Mr. Jin | formal-polite and awed | The casualty clerk addresses Jin as 진 선생님 after Jin asks him to list Lei Fei among the dead. |
| 진태경 | 중년인 | celebrated Hunter to older fellow Hunter | sir | casual and teasing | Jin addresses the older Hunter as 아저씨 while joking with him and giving him instructions. |
| 야율목 | 진태경 | Nanman_Beast_Palace_Young_Palace_Lord_to_Han_intruder_and_Murim_Alliance_Pavilion_Master | you | formal but hostile | Asks Jin's identity and orders him to follow after learning he belongs to the Murim Alliance. |
| 진태경 | 야율목 | Fire_Dragon_Pavilion_Pavilion_Master_to_Nanman_Beast_Palace_Young_Palace_Lord | Mok | casual, teasing, and insulting | Calls him rude and later addresses him as 목아 while jokingly claiming they are friends. |
| 야율목 | 야율척 | Young_Palace_Lord_to_Palace_Lord | Palace Lord | ceremonial and deferential | Yayul Mok kneels with his guards and formally greets Yayul Cheok upon his arrival. |
| 야율척 | 야율목 | Palace_Lord_to_Young_Palace_Lord | Mok | authoritative and familiar | Yayul Cheok questions Mok's unannounced departure and later addresses him as 목아 while discussing Nanman's tribes. |
| 야율척 | 진태경 | Nanman_Beast_Palace_Palace_Lord_to_Jeok_Cheongang's_Disciple | you / Disciple of Old Master Jeok / Jin Taekyung | rough, testing, and later welcoming | Yayul Cheok questions Taekyung as a suspected culprit, strikes him as a test, and then welcomes him after recognizing Jeok's Disciple. |
| 진태경 | 야율척 | Fire_Dragon_Pavilion_Pavilion_Master_to_Nanman_Beast_Palace_Palace_Lord | Great Hero Yayul Cheok | formal and deferential | Taekyung gives Yayul Cheok a formal greeting as the nineteenth successor of the Fire Gate Clan. |
| 야율목 | 백상 | nephew_to_father's_sworn_younger_brother | Uncle Baeksang | ceremonial and deferential | Yayul Mok formally greets Baeksang as he arrives at the stone door. |
| 백상 | 야율목 | father's_sworn_brother_to_nephew | you | cold and formal | Baeksang questions Yayul Mok about his return, the pasture fire, and the Palace Lord's whereabouts. |
| 야수묘왕 | 백상 | sworn_older_brother_to_sworn_younger_brother | Baeksang | familiar and bittersweet | Yayul Cheok offers Baeksang his preferred fruit wine and asks why he came. |
| 백상 | 진태경 | Nanman great chieftain to Murim Alliance Pavilion Head | you bastard | cold, hostile, and contemptuous | Baeksang calls Jin a Han Chinese man, rejects his status, and orders him to leave. |
| 진태경 | 백상 | Murim Alliance Pavilion Head to Nanman great chieftain | you | polite but deliberately provocative | Jin tells Baeksang that Nanman's blood was shed for the world rather than merely for the Central Plains. |
| 진태경 | 야수묘왕 | younger allied master to Ten Kings elder | Great Hero Yayul | urgent and respectful | Uses 야율 대협 while warning the Beast Miao King not to enter the valley. |
| 야수묘왕 | 진태경 | senior allied master to younger allied master | you | informal and cautionary | Warns Taekyung not to lower his guard and to be careful while crossing the swamp. |
| 야율목 | 야수묘왕 | son_to_father | Father | formal and deferential | Yayul Mok calls out to the Beast Miao King after the rescue party arrives. |

## Listed compact profiles

### Baeksang.md

# Baeksang (백상)

- **Safe through:** Chapter 642
- **Aliases:** None
- **Role:** Baeksang is the middle-aged great chieftain of the Bai people, one of Nanman's four most powerful great tribes.
- **Personality:** Cold, rigid, meticulous, and politically resolute, with a deep but guarded attachment to his sworn elder brother.
- **Voice:** Rigid, formal, restrained, and emotionally distant.
- **Relationships:** Baeksang is Yayul Cheok's sworn younger brother and childhood companion and Yayul Mok's sworn uncle; he lost a beloved son in the Great Faction War, bears a burn scar from Jeok Cheongang after calling him a crazy old man, opposes the Nanman Beast Palace joining the Murim Alliance, and helps Yohi keep Heugung under control.

### Beast Miao King.md

# Beast Miao King (야수묘왕)

- **Safe through:** Chapter 642
- **Aliases:** None
- **Role:** The Beast Miao King is the Palace Lord of the Nanman Beast Palace, the great chieftain of the Miao people, and a master among the Ten Kings.
- **Personality:** Fierce and vigilant when confronting threats to the Nanman Beast Palace.
- **Voice:** Low, growling, and forceful.
- **Relationships:** He commands the Nanman Beast Palace and is responsible for the forces stationed at Ailao Mountain.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 640
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Human Butcher.md

# Human Butcher (인도)

- **Safe through:** Chapter 626
- **Aliases:** None
- **Role:** Former mysterious Han Chinese mounted-bandit power in Northern Gaoyuan commanding fifty subordinates; a Peak master killed by an unnamed old man in a single move
- **Personality:** Cold, intimidating, and murderous; he kills people as though slaughtering livestock
- **Voice:** Cold, curt, and quietly threatening
- **Relationships:** He is one of four powerful participants at the Northern Gaoyuan gathering, intimidates Temur, and has claimed Ghost Sword Wipeng as his personal target in the proposed attack

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 642
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple, the Fire Gate Clan's nineteenth successor, and the Pavilion Master of the Fire Dragon Pavilion within the Murim Alliance; he is a Supreme Peak master with the Heavenly Martial Physique and Force, publicly recognized as an S-rank-level Hunter while formally retaining an A-rank license, and he has completed an unnamed cultivation technique designed for even the lowest-rank Hunter to learn without making it easily abusable.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 642
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Yayul Cheok.md

# Yayul Cheok (야율척)

- **Safe through:** Chapter 639
- **Aliases:** Beast Miao King
- **Role:** Yayul Cheok is the over-eighty Beast Miao King, lord of the Nanman Beast Palace, a Supreme Peak master among the Ten Kings, and great chieftain of the Bai people.
- **Personality:** Boisterous, warmhearted, forthright, playful, and politically conscious of the tribal coalition he leads.
- **Voice:** Rough, loud, convivial, and teasing, becoming authoritative when discussing Nanman's laws or political decisions.
- **Relationships:** Jeok Cheongang is an old acquaintance whom he respects; Baeksang is his sworn younger brother and childhood companion, and they fought together during the Great Faction War; Yayul Mok serves as his Young Palace Lord; Jin Taekyung is Jeok's Disciple whom he welcomes into the Nanman Beast Palace.

### Yayul Mok.md

# Yayul Mok (야율목)

- **Safe through:** Chapter 642
- **Aliases:** None
- **Role:** Yayul Mok is the non-Han Young Palace Lord of the Nanman Beast Palace, a spear-wielding warrior who rides a white tiger, and a halting but capable speaker of Han Chinese.
- **Personality:** Protective of Nanman Beast Palace livestock, quick-tempered toward trespassers, and capable of restraint once he recognizes legitimate authority.
- **Voice:** Blunt, commanding, and formal-polite toward strangers, becoming openly insulting when provoked.
- **Relationships:** Yayul Cheok is the Beast Miao King and Yayul Mok's father; Yayul Mok is his only surviving son after three older siblings died in the Great Faction War, Baeksang is his father's sworn younger brother, and his white tiger is a long-bonded companion.

## Korean source

```text
＃643화



구구궁!

등 뒤에서 석문이 묵직한 소음과 함께 내려앉는다.

은은한 불빛이 번지는 넓은 대전 내부. 그 누구도 입을 열지 않는 침묵 속에서 서른한 쌍의 시선이 화살처럼 날아와 내 얼굴에 꽂힌다.

네가 왜 거기서 나와?

딱 그런 눈빛들이다. 하지만 그 안에 스며 있는 감정은 한족에 대한 적의(敵意)보다는 순수한 놀라움에 가까웠고, 몇몇 부족장들의 시선에는 호의마저 담겨 있었다.

물론 한 사람만큼은 절대적으로 예외였지만.

“둘 중 하나겠군. 내 눈이 잘못되었든지, 그도 아니면 나를 포함한 그 누구도 모르는 사이에 부족 대회의의 규율이 바뀌었든지.”

침묵을 깨트리고 입을 연 중년인, 백족의 대족장인 백상(白象)이 차가운 목소리로 말을 이었다.

“설명해 보아라. 왜 부족장도, 그렇다고 남만인도 아닌 일개 한족을 이곳에 들였는지.”

백상이 설명을 요구하는 상대는 현재 이 자리에 없는 야수묘왕도, 그렇다고 나도 아니었다.

내 오른편에 서 있던 야율목이 침착한 어조로 대답했다.

“그는 그럴 만한 자격이 있기 때문입니다.”

“자격이라.”

작게 뇌까린 백상이 말을 이었다.

“이립(而立)도 채 되지 않은 어린놈의 섣부른 판단이라는 소리로 들리는구나.”

“아직 도착하지 않으신 다른 분의 판단이기도 합니다.”

“……!”

“아버님. 아니, 궁주님께서 말씀하셨습니다. 그는 부족 대회의에 참석할 자격이 있다고.”

백상의 눈빛이 깊숙이 가라앉는다. 잠시 침묵하던 그가 불쑥 입을 열었다.

“궁주께서는 왜 오시지 않았느냐?”

“곧 오실 겁니다. 그리고 그때쯤이면 남은 자리는 오직 하나뿐이겠지요.”

“불가(不可).”

백상이 못 박힌 손가락으로 탁자를 두드렸다.

“부족 대회의는 남만 전체를 대표하는 부족장들이 한자리에 모여 뜻을 교환하는 중대한 자리. 부족장이 아니라면 소궁주를 제외한 그 누구도 자리할 수 없다. 저자에게 자격이 있다는 것은 궁주 한 사람의 뜻일 뿐. 우리는 허락하지 않겠다.”

상황을 지켜보던 내가 문득 중얼거렸다.

“듣다 보니까 이상하네. 그것도 결국 본인 혼자만의 뜻 아닌가?”

명백한 혼잣말이었지만, 이 자리에 모인 수십여 명의 부족장 중 내 목소리를 듣지 못할 만큼 무공이 일천한 사람은 아무도 없었다.

그중에서도 특히 무공이 뛰어난 백상은 말할 것도 없다.

나를 향해 시선을 옮긴 그가 서늘한 목소리로 입을 열었다.

“지금 뭐라 했지?”

“아, 혹시 들으셨어요?”

“듣지 못할 거라 생각했느냐?”

“아뇨. 사실 들으라고 한 이야기는 맞습니다. 잘 들으셨네요.”

“……!”

나는 굳어 있는 백상의 표정을 바라보며 어깨를 으쓱해 보였다.

“기왕 이야기가 나왔으니 하는 말인데. 사실 말이 좋아서 우리지, 이것도 결국 그쪽 혼자만의 생각 아닙니까? 다른 부족장님들 의견은 물어보지도 않아 놓고 허락하지 않겠다고 하면 뭐 어쩌란 건지.”

물 흐르듯 이어지는 내 말에, 자리에 앉은 부족장들 사이로 보이지 않는 동요가 퍼져 나가는 것이 느껴진다.

백상은 묘족 다음으로 강성한 백족의 대족장인 동시에 야수묘왕과 함께 남만을 대표하는 초절정 고수.

아마 지금까지 그 누구도 감히 그에게 이렇게 노골적으로 말하지 못했을 거다.

단 한 사람, 나를 제외하면.

“야율 대협이 저를 먼저 보내시면서 그런 말씀을 하셨습니다. 묘족의 대족장 야율척은 네 자격을 인정하지만, 남만야수궁주 야율척은 독단으로 결정을 내릴 수 없다. 그러니 다른 부족장들의 동의를 얻어라, 라고.”

남만은 외지인이 숨 쉬는 것도 빡빡한 동네고, 일 년에 단 한 번 열리는 부족 대회의는 바늘 들어갈 틈도 없을 만큼 퍽퍽한 의식이다.

‘만약 야수묘왕이 호의를 베풀지 않았다면, 이 자리에 들어오기도 전에 제지당했겠지.’

덕분에 이 퍽퍽한 규율을 비집고 들어왔으니, 반드시 한 자리를 차지할 생각이었다. 물론 다른 부족장들의 지지를 얻어서.

“자, 그래서 여쭤보는 건데.”

나는 한 사람, 한 사람과 차례대로 시선을 맞추며 말을 이었다.

“다른 분들은 어떤 생각이십니까?”

화아아악.

어디선가 불어온 미풍(微風)에 대전을 밝히던 횃불이 흔들린다.

불그스름한 불빛에 비춰진 얼굴들은 불편함으로 일그러져 있기도 했고, 곤혹스러워하기도 했으며, 생각했던 것 이상으로 긍정적인 표정을 짓고 있기도 했다.

지금 막 입술을 뗀, 어느 중년 부족장처럼.

“우리 장족을 포함한 이 자리의 모두는 지난밤, 애뇌산에서 벌어진 사건을 알고 있소.”

남만에서 보고 들은 바에 의하면 장족은 남만 사대 부족만큼은 아니더라도, 마땅히 그 뒷줄에 설 만한 세력을 지닌 부족이다.

그런 장족의 우두머리로 짐작되는 중년 부족장은 천천히 말을 이었다.

“우리는 뜻하지 않은 불행으로 많은 피를 흘렸지만, 신속한 대처로 더 큰 희생을 막을 수 있었지. 그 모든 것이 현명한 궁주이신 야율 대족장과, 그분을 도왔던 어느 한족 젊은이 덕분이었소.”

힘 있는 목소리가 대전 내부를 울린다. 시시각각 변하는 족장들의 표정을 지켜본 그가 나를 보며 희미하게 웃었다.

“비록 늦었지만 이 자리에서나마 감사를 표하오. 그대의 도움 덕분에 우리 장족은 용맹하고도 훌륭한 스물두 명의 전사를 살릴 수 있었소. 그중에는 본인의 혈육 역시 포함되어 있었지.”

“아.”

독혈지에 끌려갔던 전사들의 숫자는 이백여 명에 달했고, 나는 그들의 이름과 신분을 일일이 듣지 못했다.

미처 몰랐고, 알 수도 없었던 사실이었지만 지난 밤의 일이 지금 이 순간 호의와 감사가 되어 돌아오고 있었다.

“장족(藏族)을 대표하여, 열화신룡 진태경의 부족 대회의 참석을 환영하오.”

말을 끝마친 그가 나를 향해 정중하게 예를 갖추었다. 지금껏 나고 자라온 이 땅의 예법이 아닌, 중원의 포권으로.

그리고 그것이 시작이었다.

드르륵. 드륵.

하나둘씩 자리에서 일어난 낯선 얼굴의 부족장들. 생김새와 복장도 다른 그들은 호의가 담긴 표정으로 입을 열었다.

“은혜를 입고도 모른 척할 수는 없지. 우리 회족(回族)도 찬성이오.”

“만족(蠻族)도 이의 없소. 그저 내 못난 아들놈을 살려 줘서 감사하다는 말을 드리고 싶을 뿐이오.”

각기 크고 작은 부족을 다스리는 부족장들.

그러나 이들은 부족장인 동시에 한 집안의 가장이고, 사랑하는 자식을 둔 아버지이자 어머니였다.

그들은 어색하기 짝이 없는 포권지례와 함께 차례대로 내게 감사 인사를 건넸다.

내가 지난밤 독혈지에서 구출한 전사들은 모두 그들의 백성이었고, 가족이었으니까.

그러나 꼭 지난 밤의 일로 내 대회의 참석을 찬성하는 부족장들만 있는 것은 아니었다.

“부이족도 찬성하겠습니다. 그는 충분한 자격이 있어요.”

중년 여족장의 말에. 아직도 자리에서 일어나지 않았던 족장 중 한 하나가 눈살을 찌푸렸다.

“잠깐. 부이족은 도대체 이유가 뭐요? 애뇌산에 주둔하고 있던 전사 중 부이족은 포함되어 있지 않았을 텐데?”

“제 고향은 남만이니까요.”

“그게 무슨…….”

“말하지 못하는 짐승들도 은혜를 입으면 보답하는 법입니다. 열화신룡 진태경은 지난 밤 제 고향을 위해 목숨을 걸고 싸웠고요. 그것 하나만으로도 이 자리에 참석할 자격은 충분하지 않나요?”

“……크흠.”

질문을 던졌던 부족장은 불편한 헛기침과 함께 입을 다물었고, 다른 이들의 얼굴에는 호의 어린 미소가 감돌았다.

그리고 이처럼 며칠 전과는 확연히 다른 분위기 속에서, 나는 가슴 한구석이 간질거렸다.

‘상대의 도움에 보답한다. 생각해 보면 당연한 건데.’

이 세상에는 때때로 그 당연한 것이, 당연하지 않게 될 때가 있다.

나 역시 그들의 보답을 바라며 독혈지와 향한 것이 아니었지만, 지금 이 순간 상당수의 부족장들은 내게 감사와 신뢰로 보답하고 있었다.

지난밤에 자신들이 받은 도움 때문에. 혹은 까마득한 과거의 일 때문에.

“선대 부족장이셨던 선친께서는 정마대전에서 귀환하신 직후, 종종 이런 말씀을 하셨지. 화왕이 아니었다면 당신께서는 남만이 아니라 구천(九泉)에 갔을 거라고. 돌아가신 이후 까마득히 잊고 있던 말씀이 이제야 생각이 나는구려.”

“내 선조께서는 과거 당대의 열화문주와 함께 오독문을 멸문시켰소. 그분이 아니었다면 우리 부족도 지금까지 명맥을 이어 오지 못했겠지. 나 역시 찬성이오.”

멈춰 있던 물이 흐르기 시작한다.

자리에 앉아 침묵을 지키던 부족장들 역시 흐르는 물살처럼 차례대로 자리에서 일어나 입을 열었고, 어느새 서 있는 이들의 숫자는 앉아 있는 이들의 숫자를 넘어섰다.

그리고 이 뜻하지 않은 상황 속, 종지부를 찍을 마지막 한 사람이 마침내 모습을 드러냈다.

구구구궁, 쿵!

천근의 무게를 지닌 석문을 한 손으로 들어 올린 팔 척 장신의 거한.

대전에 길고 거대한 그림자를 드리운 야수묘왕이 낮은 목소리로 입을 열었다.

“결론이 나온 모양이군.”

야수묘왕의 시선이 향하는 방향의 끝. 천천히 자리에서 일어난 백상이 냉담한 표정으로 예를 취했다.

“궁주를 뵙습니다.”

“내 눈과 귀가 잘못된 것이 아니라면, 그에게는 자격이 충분한 것 같네. 그렇게 생각하지 않나, 아우?”

“잘못된 선택입니다. 유서 깊은 전통을 지닌 부족 대회의의 규율을 무너트리시다니.”

“이미 과반수 이상의 부족장들이 그의 참석을 인정했네. 그리고 중원의 유생들은 이걸 합의라고 부르더군.”

백상은 대답 대신 눈을 감았고, 야수묘왕은 더 이상 그의 대답을 기다리지 않았다.

“묘족의 대족장이자, 남만야수궁의 궁주인 나. 야율척은 무림맹 화룡각주이며 열화문의 후인인 진태경의 대회의 참석을 허(許)한다.”

그리고 그와 동시에, 맑은 종소리가 내 귓가를 파고들었다.

띠링.



- 퀘스트, [부족 대회의]가 생성되었습니다!



* * *



축축하고 무더운 어느 공간.

칠흑과 심연. 그 어딘가 쯤에 위치한 어둠 속에서, 들리지 않는 목소리가 흘러나오고 있었다.

- 내궁에서 대회의가 시작되었습니다.

- 그는?

- 그 역시 대회의에 참석했습니다. 한데…….

- 계속해. 머뭇거리지 말고.

- 그, 그것이.

잠깐의 망설임.

그것이 자신의 숨통을 끊을 줄은, 아마 전음(傳音)을 흘려보내던 사내조차 예상치 못했을 것이다.

쉭, 서걱.

희미한 소음과 함께 어둠 속에 묻혀 있던 신형이 힘없이 허물어졌다.

뺨에 묻은 핏물을 닦아 낸 하얀 손가락이 움직이자, 생기가 빠져나간 시신이 어둠 너머로 날아가 사라졌다.

- 그래서. 어떻게 됐다고?

순식간에 한 생명이 사라졌지만, 빈자리는 금세 새로운 누군가로 채워졌다. 바짝 긴장한 전음이 뒤를 이어 울려 퍼졌다.

- 진태경. 진태경이 대회의에 참석했습니다.

- 누구? 진태경?

- 옛! 야수묘왕과 다른 부족장들의 지지를 얻어 허락을 받아 냈다고 합니다.

잠깐의 침묵이 흐른 뒤, 어둠 속 누군가가 작게 혀를 찼다.

- 하여간 야만족 새끼들…… 그런데 넌? 그걸 손 놓고 보고만 있었어?

- 예, 예?

- 하긴. 너 같은 버러지가 무슨 잘못일까. 쓸모없는 버러지를 수하로 둔 내 잘못이지.

- ……!

어둠 속의 존재에게 보고하던 누군가는 즉각 위험을 알아차렸지만, 그 역시 죽음을 피해 갈 수는 없었다.

쉭, 푸푹!

또다시 스쳐 지나간 죽음. 어둠에 파묻힌 시체를 빤히 내려다보던 존재가 나직하게 뇌까렸다.

“진태경. 오랜만이네?”
```

## Final English reading copy

```markdown
# Chapter 643

*Rumble!*

The stone gate behind me descended with a heavy noise.

Inside the spacious main hall, illuminated by spreading lamplight, thirty-one pairs of eyes flew toward my face like arrows and lodged there amid a silence in which no one spoke.

*Why are you coming out of there?*

That was the look in their eyes. But the emotion permeating them was closer to pure surprise than hostility toward a Han Chinese man, and several of the chieftains even regarded me with goodwill.

Of course, there was one absolute exception.

“One of two things must be true. Either my eyes are deceiving me, or the rules of the tribal grand council have changed without anyone, myself included, knowing.”

The middle-aged man who broke the silence was Baeksang, the great chieftain of the Bai people. He continued in a cold voice.

“Explain yourself. Why have you allowed an ordinary Han Chinese man—who is neither a chieftain nor even a Nanman—to enter this place?”

The person Baeksang demanded an explanation from was neither the Beast Miao King, who was not currently present, nor me.

Yayul Mok, standing to my right, answered calmly.

“Because he is qualified to do so.”

“Qualified.”

Baeksang muttered the word under his breath before continuing.

“It sounds like the rash judgment of an immature brat who has not even reached thirty.”

“It is also the judgment of another person who has yet to arrive.”

“……!”

“My father. No, the Palace Lord said that he is qualified to attend the tribal grand council.”

Baeksang’s gaze sank deeper. After a brief silence, he abruptly spoke.

“Why has the Palace Lord not come?”

“He will be here soon. And by then, I expect only one seat will remain.”

“Impossible.”

Baeksang tapped the table with a callused finger.

“The tribal grand council is a solemn gathering where the chieftains representing all of Nanman come together to exchange their views. If one is not a chieftain, no one may take a seat here except the Young Palace Lord. This man’s qualification is merely the will of the Palace Lord alone. We will not permit it.”

Watching the situation unfold, I muttered,

“That sounds strange. Isn’t that ultimately just your personal opinion too?”

It was clearly an aside, but not one of the several dozen chieftains gathered here possessed martial arts so weak that they could not hear my voice.

That went without saying for Baeksang, whose martial arts were particularly formidable.

He turned his gaze toward me and spoke in a chilly voice.

“What did you just say?”

“Oh, did you hear me?”

“Did you think I wouldn’t?”

“No. Actually, I did mean for you to hear it. Glad you caught that.”

“……!”

I shrugged as I looked at Baeksang’s stiff expression.

“Since the subject has come up, let me say this. We may call ourselves ‘we,’ but isn’t this ultimately just your personal opinion as well? You haven’t even asked what the other chieftains think, yet you say you won’t permit it. What exactly are we supposed to do with that?”

As my words continued to flow smoothly, I could feel an invisible stir spreading among the seated chieftains.

Baeksang was the great chieftain of the Bai people, the most powerful tribe in Nanman after the Miao people, as well as a Supreme Peak master who represented Nanman alongside the Beast Miao King.

No one had probably ever dared to speak to him so bluntly.

Except for me.

“Great Hero Yayul told me this when he sent me ahead. ‘Yayul Cheok, the great chieftain of the Miao people, recognizes your qualification, but Yayul Cheok, the Palace Lord of the Nanman Beast Palace, cannot make this decision unilaterally. So obtain the consent of the other chieftains.’ That is what he said.”

Nanman was a place where even breathing was difficult for outsiders, and the tribal grand council held only once a year was a rigid ceremony with not even enough room for a needle to pass through.

*If the Beast Miao King hadn’t shown me favor, I would have been stopped before I even made it inside.*

Thanks to that favor, I had forced my way through those rigid rules. I intended to claim a seat here.

Of course, I would do so by earning the support of the other chieftains.

“So, that is why I’m asking.”

I looked each chieftain in the eye in turn and continued.

“What do the rest of you think?”

*Fwoosh.*

A breeze blew in from somewhere, making the torches illuminating the hall flicker.

The faces revealed by their reddish light were twisted with discomfort, filled with confusion, or wearing expressions far more positive than I had expected.

Like the middle-aged chieftain who had just begun to speak.

“Everyone here, including the Zang people, knows about the incident that occurred at Ailao Mountain last night.”

From what I had heard and seen in Nanman, the Zang people possessed enough power to stand directly behind Nanman’s four great tribes, even if they did not belong among them.

The middle-aged chieftain, who appeared to be the leader of such a tribe, slowly continued.

“We shed much blood because of an unforeseen disaster, but through a swift response, we were able to prevent an even greater loss of life. We owe it all to Great Chieftain Yayul, our wise Palace Lord, and to a young Han Chinese man who aided him.”

His powerful voice rang throughout the hall. After watching the chieftains’ expressions change from moment to moment, he looked at me and smiled faintly.

“Though late, I would like to express our gratitude here. Thanks to your help, our Zang people were able to save twenty-two brave and excellent warriors. One of them was even a member of my own family.”

“Ah.”

Around two hundred warriors had been dragged into the Poisonblood Grounds, and I had not heard every one of their names and identities.

It was a fact I had not known—and could not have known—but the events of last night were returning to me now in the form of goodwill and gratitude.

“On behalf of the Zang people, I welcome Blazing Flame Divine Dragon Jin Taekyung’s attendance at the tribal grand council.”

When he finished speaking, he offered me a respectful salute. Not with the etiquette of the land where I had been born and raised, but with a Central Plains cupped-fist salute.

And that was only the beginning.

*Scrape. Scrape.*

One by one, unfamiliar chieftains rose from their seats. Different in appearance and clothing, they spoke with expressions of goodwill.

“We cannot pretend not to notice after receiving such a kindness. The Hui people also support him.”

“The Man people have no objection either. I merely wish to thank him for saving my worthless son.”

These chieftains ruled tribes large and small.

But they were not only chieftains. They were also heads of households, fathers and mothers with beloved children.

With painfully awkward cupped-fist salutes, they each offered me their thanks in turn.

The warriors I had rescued from the Poisonblood Grounds the previous night had all been their people and their families.

But the chieftains supporting my attendance at the grand council were not all doing so because of last night’s events.

“The Bouyei people also support him. He is more than qualified.”

At the words of the middle-aged female chieftain, one of the chieftains who still had not risen from his seat frowned.

“Wait. What reason do the Bouyei people have? There weren’t any Bouyei among the warriors stationed at Ailao Mountain, were there?”

“Because Nanman is my homeland.”

“What does that—”

“Even beasts that cannot speak know how to repay a kindness. Blazing Flame Divine Dragon Jin Taekyung risked his life and fought for my homeland last night. Isn’t that alone enough to qualify him to attend this gathering?”

“……Ahem.”

The chieftain who had asked the question shut his mouth with an uncomfortable cough, while goodwill-filled smiles spread across the faces of the others.

And amid this atmosphere, so clearly different from the one only a few days ago, I felt a tickle in one corner of my chest.

*Repaying someone for the help they gave you. When you think about it, it’s only natural.*

In this world, however, there were times when something so natural ceased to be natural.

I had not gone to the Poisonblood Grounds expecting repayment from them, but at this very moment, quite a few chieftains were repaying me with gratitude and trust.

Because of the help they had received last night.

Or because of something that had happened in the distant past.

“My late father, who was once a great chieftain, often said things like this after returning from the Great Faction War. ‘If it hadn’t been for the Fire King, I would have gone to the Nine Springs instead of returning to Nanman.’ I had completely forgotten those words after his death, but they have finally come back to me.”

“My ancestor destroyed the Five Poisons Sect alongside the Sect Leader of the Fire Gate Clan at the time. If it hadn’t been for him, our tribe would not have survived to this day. I support him as well.”

The water that had been still began to flow.

The chieftains who had remained seated in silence rose one after another like the current of flowing water and began to speak. Before long, the number of people standing had surpassed the number still seated.

And amid this unexpected situation, the final person who would bring it to an end finally appeared.

*Rumble, rumble—boom!*

A giant nearly eight feet tall lifted the stone gate, which weighed a thousand geun, with one hand.

Casting a long, enormous shadow across the hall, the Beast Miao King spoke in a low voice.

“Looks like a conclusion has been reached.”

At the far end of the Beast Miao King’s gaze, Baeksang slowly rose from his seat and offered a cold salute.

“I greet you, Palace Lord.”

“Unless my eyes and ears deceive me, he seems more than qualified. Don’t you agree, little brother?”

“It is the wrong choice. You are destroying the rules of a tribal grand council with a venerable tradition.”

“More than half of the chieftains have already recognized his right to attend. And the scholars of the Central Plains call this a consensus.”

Baeksang closed his eyes instead of answering, and the Beast Miao King did not wait any longer.

“I, Yayul Cheok, great chieftain of the Miao people and Palace Lord of the Nanman Beast Palace, hereby permit Jin Taekyung—the Fire Dragon Pavilion Master of the Murim Alliance and successor to the Fire Gate Clan—to attend the tribal grand council.”

At that exact moment, a clear bell tone pierced my ears.

*Ding.*

> **System**
>
> - **Quest: Tribal Grand Council** has been created!

* * *

A damp, sweltering space.

Somewhere in the darkness between pitch-blackness and the abyss, a voice that could not be heard drifted through the air.

—The grand council has begun in the Inner Palace.

—And him?

—He attended the grand council as well. But……

—Continue. Don’t hesitate.

—Th-that is……

There was a brief hesitation.

Even the man sending the Sound Transmission could not have expected that it would cost him his life.

*Swish. Slice.*

With a faint noise, the figure concealed in the darkness crumpled helplessly.

When the white fingers that had wiped the blood from their cheek moved, the lifeless corpse flew beyond the darkness and vanished.

—So? What happened?

A life had vanished in an instant, but the empty space was quickly filled by someone new. A tense Sound Transmission rang out in succession.

—Jin Taekyung. Jin Taekyung attended the grand council.

—Who? Jin Taekyung?

—Yes! Apparently he gained permission with the support of the Beast Miao King and the other chieftains.

After a brief silence, someone in the darkness clicked their tongue.

—Those barbarian bastards…… But what about you? You just stood by and watched it happen?

—W-what?

—Then again, how could a worm like you be at fault? It was my mistake for keeping a useless worm under my command.

—……!

The person reporting to the entity in the darkness immediately realized the danger, but he could not escape death either.

*Swish. Thrust!*

Death passed by once again. The entity gazed down at the corpse buried in the darkness and muttered quietly.

“Jin Taekyung. It’s been a while.”
```

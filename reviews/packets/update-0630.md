<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0630.txt",
      "sha256": "f22d256f431066b677304f079331b9cc5d761b9d07b6a5f3b2a779d36f00b6d1",
      "bytes": 13495
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "8a392c26539b38412dba7680fe8b871485deb0c307c9509458ff0849221e6e86",
      "bytes": 2443
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "05a94885844819251e91dc6bf2ea1baee7fbb2e74e2126440e2ea967d5a27310",
      "bytes": 193849
    },
    {
      "path": "characters/Baeksang.md",
      "sha256": "9af47b7e2b9068f02cd7c21f768388942f4cdafc172ffc5399519a47c30156d0",
      "bytes": 695
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "d9a2fb3639025388a8ce41eccdd7d400982b14e38f87d6701e1336f08546859c",
      "bytes": 553
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "18b16f5aea7b937676e4139a9d0810e1ea2899bfc5fd28dfa74685617b5eaf2d",
      "bytes": 1857
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "3927de8296d07fadc3bd4ce7a63f87bb59be18594fb48ba59460c9d52924fcc1",
      "bytes": 622
    },
    {
      "path": "characters/Ju Hwaran.md",
      "sha256": "638e323502b2378b82216bf90083cd9c48bb6fc58f64d676af43d29928fa8bf0",
      "bytes": 1043
    },
    {
      "path": "characters/Yayul Mok.md",
      "sha256": "700c82e35b915851b41edc40f9141cc62802e2d0f119fdc613ea747c05570eeb",
      "bytes": 871
    },
    {
      "path": "characters/Yohi.md",
      "sha256": "1ee0733e39ab7a29122859a4b4b4a0e13ed9b18e2643298e1f17c6dc2e4f5593",
      "bytes": 504
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "125f5eb0209cf9b4c3184ed15eda2fcee1dd1b93d46e304ec7f1a7ac2915ff71",
      "bytes": 199327
    }
  ],
  "estimated_tokens": 11182
}
-->

# Durable State Update — Chapter 630

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 630. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 630. Profile updates may replace only one
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
  "chapter": 630,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 630,
    "continuity_sources": [630],
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
    "Nanman's first tribal council opposed joining the Murim Alliance; all thirty-two tribes will meet in three days for a second council.",
    "Baeksang is the great chieftain of the Bai people and Yayul Cheok's sworn younger brother, but he opposes Nanman joining the Murim Alliance.",
    "Jin Taekyung came to Nanman to contain a spreading crisis rather than as a diplomat, but he will attempt to persuade Nanman if possible.",
    "Jin Taekyung is currently in the Nanman Beast Palace's Outer Hall after getting lost on the way back to the Fire Dragon Pavilion's lodging.",
    "Jin Taekyung is concealing his identity with a crudely made tiger mask while moving through the crowded Outer Hall market.",
    "The Miao, Bai, Yi, and Yao peoples are Nanman's four great tribes; the Miao are strongest, followed by the Bai.",
    "The Yi and Yao great chieftains returned with roughly five hundred warriors after a campaign against man-eating beasts, and the Yi achieved no notable result according to local reports.",
    "Yohi is the female great chieftain of the Yao people, renowned for her intelligence and extraordinary beauty.",
    "Yohi has noticed Jin Taekyung in the crowd and her eyes lit up when she recognized him."
  ],
  "continuity_sources": [
    629,
    628
  ],
  "open_questions": [
    "Why does Baeksang oppose joining the Murim Alliance despite his lifelong bond with Yayul Cheok and their shared service in the Great Faction War?",
    "What is the meaning of Baeksang's cold scrutiny of Jin Taekyung?",
    "Will Yayul Cheok overcome the other great chieftains' opposition and bring the Nanman Beast Palace into the Murim Alliance?",
    "Will the remaining tribes follow Baeksang and the other opposing great chieftains at the council in three days?",
    "Why did Yohi react so strongly after noticing Jin Taekyung?"
  ],
  "safe_through": 629,
  "temporary_decisions": [
    "Use Baeksang for 백상 and do not treat White Elephant as a separate alias.",
    "Use sworn younger brother for 불알 동생 in the relationship between Yayul Cheok and Baeksang.",
    "Use Jiang Taigong for 강태공 and Jindro for 진드로.",
    "Render 황개 as Hwang Gae and 똥개 as Ddong Gae.",
    "Render 입맹 as joining the alliance."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 주화란    | **Ju Hwaran**      |
| 십왕     | **Ten Kings**       |
| 태원진가   | **Jin Family of Taiyuan**        |
| 무림맹    | **Murim Alliance**               |
| 암천     | **Dark Heaven**                  |
| 남만야수궁  | **Nanman Beast Palace**          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 중원     | **Central Plains**                               |                                                       |
| 매력               | **Charm**                      |
| 태원     | **Taiyuan**            |
| 대사      | **Master** for a senior Buddhist monk                           |
| 백상 | **Baeksang** | Great chieftain of the Bai people and Yayul Cheok's sworn younger brother. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 야율목 | **Yayul Mok** | Young Palace Lord of the Nanman Beast Palace. |
| 요희 | **Yohi** | Female great chieftain of the Yao people. |
| 기감 | **Qi Sense** | Taekyung's sensory technique; its range reaches seventy meters in this chapter. |
| 교관 | **Instructor** | Kim Hwajong's former Hunter Training Center role and address. |
| 한족 | **Han Chinese** | Ethnic designation used by the steppe chieftains. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 천주 | **Lord of Heaven** | Authority invoked by the masked attackers. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 화란 | **Hwaran** | Familiar short form of Ju Hwaran. |
| 호북 | **Hubei** | Province on Ju Gongsan's route from Guangdong to Henan. |
| 푸린 | **Furin** | Russian president mentioned in a forum headline. |
| 호북성 | **Hubei Province** | Province where the chapter’s Dark Heaven incidents occurred. |
| 남천마후 | **Southern Heaven Demon Empress** | Title Honglan uses when revealing her identity. |
| 묘족 | **Miao people** | Ethnic group the Escort Bureau expects to encounter near Yunnan. |
| 야수묘왕 | **Beast Miao King** | Leader of the Miao people and master of the Nanman Beast Palace. |
| 화룡각 | **Fire Dragon Pavilion** | New name chosen for Taekyung's pavilion. |
| 남천 | **South Heaven** | Dark Heaven power that the Lord of Heaven orders the servants to contact. |
| 이족 | **Yi people** | One of Nanman's four great tribes. |
| 요족 | **Yao people** | One of Nanman's four great tribes, led by Yohi. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 주화란 | 진태경 | escort_bureau_leader_to_famous_younger_martial_artist | Young Hero Jin | formal-deferential | Hwaran introduces herself as the Young Bureau Head and formally greets Taekyung as 진 소협. |
| 진태경 | 주화란 | visitor_to_young_bureau_head | Young Lady Ju | formal-polite | Taekyung uses 주 소저 while announcing that his party must leave. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 중년인 | 진태경 | veteran civilian Hunter to celebrated allied Hunter | Mr. Jin | formal-polite and awed | The casualty clerk addresses Jin as 진 선생님 after Jin asks him to list Lei Fei among the dead. |
| 진태경 | 중년인 | celebrated Hunter to older fellow Hunter | sir | casual and teasing | Jin addresses the older Hunter as 아저씨 while joking with him and giving him instructions. |
| 남천마후 | 진태경 | hostile_supernatural_opponent_to_young_martial_artist | Young Great Hero / Child | lighthearted and taunting | Addresses Taekyung while refusing to explain the Gate. |
| 진태경 | 남천마후 | young_martial_artist_to_hostile_demon_empress | you | hostile and determined | Promises that the Southern Heaven Demon Empress will die when they meet again. |
| 야율목 | 진태경 | Nanman_Beast_Palace_Young_Palace_Lord_to_Han_intruder_and_Murim_Alliance_Pavilion_Master | you | formal but hostile | Asks Jin's identity and orders him to follow after learning he belongs to the Murim Alliance. |
| 진태경 | 야율목 | Fire_Dragon_Pavilion_Pavilion_Master_to_Nanman_Beast_Palace_Young_Palace_Lord | Mok | casual, teasing, and insulting | Calls him rude and later addresses him as 목아 while jokingly claiming they are friends. |
| 야율목 | 백상 | nephew_to_father's_sworn_younger_brother | Uncle Baeksang | ceremonial and deferential | Yayul Mok formally greets Baeksang as he arrives at the stone door. |
| 백상 | 야율목 | father's_sworn_brother_to_nephew | you | cold and formal | Baeksang questions Yayul Mok about his return, the pasture fire, and the Palace Lord's whereabouts. |
| 야수묘왕 | 백상 | sworn_older_brother_to_sworn_younger_brother | Baeksang | familiar and bittersweet | Yayul Cheok offers Baeksang his preferred fruit wine and asks why he came. |

## Listed compact profiles

### Baeksang.md

# Baeksang (백상)

- **Safe through:** Chapter 629
- **Aliases:** None
- **Role:** Baeksang is the middle-aged great chieftain of the Bai people, one of Nanman's four most powerful great tribes.
- **Personality:** Cold, rigid, meticulous, and politically resolute, with a deep but guarded attachment to his sworn elder brother.
- **Voice:** Rigid, formal, restrained, and emotionally distant.
- **Relationships:** Baeksang is Yayul Cheok's sworn younger brother and childhood companion and Yayul Mok's sworn uncle; he lost a beloved son in the Great Faction War and opposes the Nanman Beast Palace joining the Murim Alliance.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 629
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 628
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple, the Fire Gate Clan's nineteenth successor, and the Pavilion Master of the Fire Dragon Pavilion within the Murim Alliance; he is a Supreme Peak master with the Heavenly Martial Physique and Force, publicly recognized as an S-rank-level Hunter while formally retaining an A-rank license, and he has completed an unnamed cultivation technique designed for even the lowest-rank Hunter to learn without making it easily abusable.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 628
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Ju Hwaran.md

# Ju Hwaran (주화란)

- **Safe through:** Chapter 627
- **Aliases:** Hwaran
- **Role:** Ju Hwaran is a Level 88 Young Bureau Head, leader of the Yongbong Escort Bureau, a member of the Fire Dragon Pavilion, an experienced Nanman escort guide with route knowledge from the Escort King's records, and someone who can understand the Miao and Bai languages.
- **Personality:** Intelligent, capable, responsible, filial, composed under pressure, and burdened by intense guilt over the escort journey's deaths.
- **Voice:** Clear, polite, restrained, and determined.
- **Relationships:** Escort King Ju Gongsan was her paternal grandfather, Ju Hogun is her father, Heo Jun was her uncle, Sama Pyo was her former fiancé in a political engagement she accepted for her father's sake, Song Ilseom is her direct escort who accompanied her previous journey to Yeongin, and Jin Taekyung is a trusted ally; the Yongbong Escort Bureau has longstanding ties with Yeongin’s inhabitants.

### Yayul Mok.md

# Yayul Mok (야율목)

- **Safe through:** Chapter 629
- **Aliases:** None
- **Role:** Yayul Mok is the non-Han Young Palace Lord of the Nanman Beast Palace, a spear-wielding warrior who rides a white tiger, and a halting but capable speaker of Han Chinese.
- **Personality:** Protective of Nanman Beast Palace livestock, quick-tempered toward trespassers, and capable of restraint once he recognizes legitimate authority.
- **Voice:** Blunt, commanding, and formal-polite toward strangers, becoming openly insulting when provoked.
- **Relationships:** Yayul Cheok is the Beast Miao King and Yayul Mok's father; Yayul Mok is his only surviving son after three older siblings died in the Great Faction War, Baeksang is his father's sworn younger brother, and his white tiger is a long-bonded companion.

### Yohi.md

# Yohi (요희)

- **Safe through:** Chapter 629
- **Aliases:** None
- **Role:** Yohi is the female great chieftain of the Yao people, one of Nanman's four great tribes.
- **Personality:** Yohi's public presence is charismatic and captivating, drawing widespread admiration and affection.
- **Voice:** Not established.
- **Relationships:** Yohi leads the Yao people and is one of the great chieftains representing Nanman's major tribes.

## Korean source

```text
＃630화



가면으로 얼굴을 가린 직후부터 안심하고 있던 것이 화근이었다.

나도 다른 사람들처럼 발을 동동 구르면서 박수라도 쳐야 했었나.

이제야 문득 그런 생각이 들었지만 이미 엎질러진 물이다. 지금 이 순간조차도 요희의 시선은 정확히 나를 응시하고 있었으니까.

그래도 문제 될 건 없을 거다. 눈에 띄는 점이라고는 호응 하나 없이 어정쩡하게 서 있던 것밖에는 없었으니까.

이 화려한 개선식의 주인공이라 할 수 있는 요족의 대족장이 내게 이 이상의 관심을 보일 가능성은 제로에 가깝다.

“거기, 당신.”

“…….”

제로에 가깝다고 했지, 제로라고는 하지 않았다.

염병. 그나저나 이걸 부르네.

나는 정확히 이쪽을 바라보는 요희의 모습에, 혹시나 하는 마음으로 슬쩍 뒤를 돌아봤다.

“그래. 방금 돌아본 당신.”

다행히도 지금 막 고개를 돌린 사람은 나 한 사람뿐만이 아니었다.

갑작스러운 요희의 돌발 행동에 시전에 모여 있던 사람들이 웅성거리며 미어캣처럼 사방으로 고개를 돌리고 있었으니까.

“호랑이 가면 쓴 사람.”

잽싸게 주위를 훑었다. 간지나는 호랑이 가면을 착용한 사람은 나를 포함해서 열댓 명 정도. 이 정도면 든든한 확률이다.

호랑이 가면을 사길 잘했다. 물론 돈을 준 건 아니지만.

“지금 나와 눈이 마주친, 호랑이 가면을 쓴 칠척장신의 사내. 이쯤하고 앞으로 나오지?”

갑작스러운 성별과 신장 옵션 추가로 인해 호랑이 가면 코인이 떡락했다. 당첨 확률이 급상승하자 이마에 땀이 맺히는 것 같다.

요희의 시선을 피해 황급히 고개를 숙인 나는 신속하고도 은밀하게 하체를 꼬았다.

그리고 내 블랙 아나콘다를 다리 사이로 완벽하게 숨기고 고개를 든 순간, 짜게 식은 요희의 눈빛과 시선이 마주쳤다.

“…….”

“…….”

환호 속에서 이어지던 행렬은 이미 멈춘 지 오래.

시전에 내려앉은 숨 막히는 침묵과 요희를 비롯한 숱한 사람들의 시선 속에서, 나는 한껏 오므렸던 다리를 펴며 준엄한 목소리로 입을 열었다.

“음, 날 불렀소?”

“…….”

“…….”

가면에 덮인 내 얼굴과 하체만 번갈아 볼 뿐, 그 누구도 대답하지 않았다.

……씨바. 그냥 처음 불렀을 때 나갈걸.



* * *



한 단체를 이끄는 지도자가 갖춰야 할 덕목은 여러 가지다. 그중에는 훌륭한 안목(眼目)도 빠질 수 없다.

“당신을 보는 순간 묘한 느낌을 받았지.”

맹수 토벌을 축하하는 행렬이 끝난 뒤, 수행원을 시켜 나를 따로 불러낸 요희가 나른한 목소리로 말을 이었다.

“뭐랄까. 그 많은 사람 속에서 홀로 이질적이었어.”

옆에서 쉴 새 없이 과일을 집어 먹던 이족의 대족장이 헤실헤실 웃으며 그녀의 말에 맞장구쳤다.

“그대의 말이 맞소. 혼자서 목석처럼 서 있는 게, 딱 눈에 띄더라니까.”

전사와는 어울리지 않는 통통한 몸매를 지닌 중년의 그는, 과즙으로 축축하게 젖은 손을 흔들며 인사했다.

“아직도 가면을 벗지 않은 무례한 친구. 나는 아직 자네가 누구인지 모르지만, 자네는 이미 나를 알고 있겠지. 이족을 이끌고 있는 흑웅(黑熊)이라고 하네.”

흑웅. 검은 곰이라는 뜻이다.

어쩐지 행렬 때 웬 곰을 타고 있나 했더니, 이 동네는 본인 이름을 딴 애완 맹수를 데리고 다니는 게 기본인 모양이었다.

‘그나저나 뭐라고 대답해야 하나.’

사실은 기왕 이렇게 된 거, 가면을 벗고 정체를 밝힐 생각이었다. 미리 자리를 피하지 않았던 것도 그런 이유에서였고.

하지만 요희는 내 생각보다 훨씬 더 눈치가 빠른 여인이었다.

“가면은 그대로 쓰고 있어도 좋아. 태원진가의 진태경.”

“음?”

“어?”

약간 놀랐다. 이제 막 도착한 요희가 내 신분을 정확히 알고 있던 것에 한 번, 그리고 같은 대족장인 흑웅이 나보다 더 크게 놀라는 것에 또 한 번.

순간 멈칫한 나와 흑웅의 모습에 요희가 피식 웃었다.

“뭘 그렇게 놀라? 궁주께서 무림맹에서 보낸 한족 무리를 내궁(內宮)으로 들였다는 소식은 이미 들었어.”

흑웅이 어리둥절한 표정으로 고개를 갸웃거렸다.

“무림맹에서 온 한족? 정말이오? 난 못 들었는데.”

“그거야 당신이 미련한 곰 같아서지요. 물론 그런 모습이 매력적이지만.”

뒤에 덧붙인 말이 단순한 립 서비스라는 건 스켈레톤 킹도 알아챌 정도였지만, 흑웅은 헤죽 웃으며 좋아했다.

“그 말, 진심이오?”

“당연하지요. 제가 늘 연모하고 있다는 사실을 잊지 마세요.”

고혹적인 목소리와 눈빛. 남만인이라는 게 믿어지지 않을 만큼 희고 잡티 없는 손가락이 곰보 자국으로 가득한 볼을 쓰다듬자, 흑웅의 얼굴에 황홀감이 감돌았다.

“아아. 그대여.”

누군가가 이 광경을 세 글자로 표현할 수 있냐 묻는다면, 나는 주저 없이 이렇게 답할 것이다.

‘우욱. 씹…….’

뱃살 불룩한 50대 중년인이 20대 미녀의 손길에 버터처럼 녹아내리는 모습.

제아무리 사랑에는 나이도 국경도 없다지만, 이 정도면 없어도 새로 만들어야 한다.

‘어차피 진짜 사랑도 아니겠지만.’

보아하니 왜 이족의 힘이 상장 폐지 예정의 주식처럼 나날이 떡락 하는지 알겠다. 더불어 요족이 성장할 수 있었던 이유도 함께.

그나저나…….

‘확실히, 다르긴 해도 비슷한 면이 있네.’

한 사람을 떠올리며 내심 중얼거리던 그때, 나를 힐끗 바라본 요희가 흑웅의 어깨를 쓰다듬었다.

“그런데 오라버니.”

“오, 오라버니?”

어머니가 즐겨 보시던 일일 드라마에서 몇 번 들었던 대사다.

딱딱하게 부장님 말고, 오빠라고 불러.

요희는 진상 중년 남성이라면 환장하고도 남을 니즈를 정확히 찔렀다. 좋아 죽으려고 하는 흑웅을 향해 부드러운 목소리가 이어졌다.

“잠시 자리를 비켜 주시겠어요? 이 한족에게 긴히 묻고 싶은 게 있어서요.”

“으응? 그럼. 그래야지. 그대가 원한다면 뭐든 해야지!”

“고마워요. 오라버니. 그럼 이따 봐요.”

“오오. 오오오!”

상기된 얼굴로 콧김을 내뿜은 흑웅이 천막을 벗어나자, 피식 웃은 요희가 비단 금침에 몸을 기대며 중얼거렸다.

“병신.”

어느 정도는 대충 예상은 했는데, 이건 생각 이상이다. 턱을 긁적이는 내 모습에 요희가 입꼬리를 끌어올렸다.

“왜, 너무 노골적이어서?”

상대가 이렇게 나오면 오히려 편하다. 잠시 고민하던 나는 솔직하게 대답했다.

“뭐. 그런 면이 없지 않아 있지.”

“딱히 놀라진 않는 걸 보니 대충은 알아채고 있던 모양이네? 무공만 강한 줄 알았는데, 생각했던 것보다 눈치가 빨라.”

“드물긴 해도 아주 없는 성격은 아니니까. 무림에 겉과 속이 다른 인간군상이 한둘도 아니고.”

“그래? 확실히 중원이 넓긴 한가 보구나. 남만에서는 나 같은 년이 그리 흔치 않은데. 아, 혹시 함께 왔다는 그 계집애도 같은 부류인가? 이름이 아마…… 주화란이라고 들었던 것 같은데.”

나는 대답 대신 요희를 응시했다. 그녀의 입꼬리에 맺혀 있던 미소가 한층 짙어진다.

“좋아. 취소. 당신 표정을 보아하니 내가 말실수를 한 모양이네.”

순간 내가 무슨 표정을 지었는지는, 나 자신도 모른다. 하지만 아마도 그리 상냥한 얼굴을 하고 있지는 않았을 것 같았다.

그냥, 느낌이 그랬다.

나는 이상한 기분을 느끼며 애써 담담하게 입을 열었다.

“다음부터는 말조심해. 날 믿고 남만까지 따라와 준 화룡각 대원이다.”

“아하. 단지 아끼는 수하다?”

“딱히 상관이나 수하의 구별은 없지만…… 좋을 대로 생각하든지.”

“그렇게 말해 주면 고맙고. 내가 상상력이 제법 풍부한 편이거든.”

무슨 상상을 하는지, 오묘한 웃음을 흘린 요희가 말을 이었다.

“아까는 날 그렇게 빤히 쳐다보길래 오해했었어. 혹시 첫눈에 반하기라도 했나 싶었지.”

“그럴 리가. 나도 아무나 막 좋아하고 그런 놈은 아니라서.”

“그럼 왜 그렇게 본 거지? 흑웅, 그 병신이 한심해 보였나?”

“아니. 전에 봤던 누군가가 생각났거든.”

요희의 눈빛에 흥미로움이 깃들었다.

“누구? 여자?”

“여자는 여자지. 누구인지는 당장 말해 봤자 모르겠지만.”

사실은 여자보다 괴물에 가깝다. 내가 요희를 보며 떠올렸던 건 남천마후(南天魔侯)니까.

암천에 속한 이들은 남녀의 구분이 무의미한 괴물들이고, 천주(天主)라는 하늘을 섬기는 광신도들이었다.

“흠. 여인이라……. 나랑 그렇게 닮았나?”

“조금은. 하지만 근본적으로 다르지.”

“어떻게 그렇게 확신하지? 내가 그 여인일 수도 있잖아?”

짓궂은 표정을 짓는 요희였지만, 이미 혹시나 하는 마음에 [기감]으로 확인까지 끝낸 나로서는 헷갈릴 여지조차 없었다.

‘앞서 했던 말처럼 본질적으로 다르기도 하고.’

요희의 분위기와 용모가 요사스럽다면, 남천마후는 그 자체로 사람을 현혹하는 마력(魔力)을 지녔다.

그리고 이건 비단 용모만을 뜻하는 것이 아니었다.

‘분위기.’

아름다우면서도 자연스러운, 그렇기에 미처 의심할 수 없는 특유의 분위기가 남천마후에게는 있었다.

나조차도 그 아름다움과 분위기가 위험하게 느껴진 것은 호북성에서 감쪽같이 속아 넘어간 이후였다.

“어쨌든 달라.”

“흠, 재미없네. 누군지는 몰라도 중요한 사람인가 보지?”

“중요하지. 그 이상으로 위험하고.”

“암천. 암천이구나?”

역시 요희는 눈치가 빨랐다. 그리고 이미 내가 왜 중원에서 수만 리나 떨어진 남만에 왔는지, 무엇을 위해 이곳에 왔는지 아는 사람이기도 했다.

“당신한테는 미안한 말이지만, 사대부족의 대족장 중 입맹(入盟)을 원하는 사람은 아무도 없어. 단 한 사람, 궁주를 제외한다면 말이지.”

“당신은?”

“나? 나는 아무래도 상관없어. 남만야수궁이 어떤 피해를 입어도, 우리 요족이 사대부족을 아우르기를 바라지.”

“그건 당신 생각일 뿐이고. 다른 부족장들은…….”

“물론 아닌 족장들도 있겠지. 하지만 이거 하나만큼은 확실해. 자신의 부족이 강성해지길 바라는 마음은 대부분이 같다는 것. 그리고 중원에서 애꿎은 피를 흘린다면, 자연스럽게 남만에서의 힘이 줄어들 거야.”

문득 앞서 내궁에서 야수묘왕에게 들었던 대답이 생각난다.

자신은 남만야수궁의 궁주고, 중원에서도 인정받은 십왕(十王)의 한 사람이지만 결국은 묘족의 대족장이라는 것.

남만의 크고 작은 부분을 차지하는 족장들이 요희와 같은 생각이라면, 야율목의 말처럼 남만야수궁이 무림맹에 입맹 하는 것은 사실상 불가능하다고 봐야 한다.

‘아니, 협상 난이도 진짜 줫 같네.’

비록 내가 외교관 자격으로 남만에 온 건 아니지만, 이건 시작하기도 전에 실패한 것이나 다름 없는 상황이다.

황당해하는 내 모습에 요희가 재미있다는 표정을 지었다.

“당신한테는 미안하지만 그게 현실인걸. 아, 물론 한 사람만큼은 설득할 가능성이 아주 없진 않아. 그는 사대부족에 꼽힐 만큼 큰 부족을 이끌고 있고, 그 사실이 믿어지지 않을 만큼 멍청하니까.”

여기까지만 들어도 누굴 말하는지는 알겠다. 나는 한숨처럼 입을 열었다.

“흑웅?”

깔깔거리며 소리 내어 웃은 요희가 대답했다.

“그래, 그 병신. 어차피 나나 백상(白象), 그 늙은이한테 꽉 잡혀서 아무것도 못 하는 놈이지만.”

“…….”

그래도 나름대로 남만에서 곰 좀 키우는 거대 부족의 대족장인데 취급 실화냐. 흑웅을 떠올리는 것만으로도 가슴이 조촐해진다.

‘그리고 정말 내가 흑웅을 설득할 가능성이 있었다면, 이렇게 친절하게 알려 줄 이유도 없겠지.’

흑웅은 결국 허수아비에 불과하다. 백상과 요희의 손아귀에 잡혀서 조종당하는지도 모르고 헤벌레 웃고 있는.

‘놀리는 것도 아니고.’

내가 미간을 찌푸린 채 요희를 바라보던 그때. 천막 밖이 분주해지더니 누군가의 목소리가 들려왔다.

“요희. 안에 있나?”

차갑고 메마른 목소리. 백상이었다.
```

## Final English reading copy

```markdown
# Chapter 630

The moment I covered my face with the mask, I let my guard down. That was my mistake.

Should I have stamped my feet and clapped like everyone else?

The thought only occurred to me now, but it was already too late. Even at this very moment, Yohi’s gaze was fixed directly on me.

Still, it shouldn’t become a problem. The only thing that made me stand out was the fact that I had been standing there awkwardly without joining in.

The chances of the Yao people’s great chieftain—the star of this splendid victory parade—showing any further interest in me were close to zero.

“You there.”

“……”

I said close to zero. I never said zero.

*Damn it. So she really is calling me.*

Yohi was looking straight at me, so I cautiously turned around, just in case.

“Yes. You who just turned around.”

Fortunately, I wasn’t the only person who had just looked back.

At Yohi’s sudden and unexpected action, the people gathered in the marketplace began murmuring and turning their heads in every direction like meerkats.

“The person wearing the tiger mask.”

I swiftly scanned my surroundings. There were about a dozen people wearing cool-looking tiger masks, including me. Those were reassuring odds.

Buying a tiger mask had been the right choice. Of course, I hadn’t paid for it.

“The seven-foot-tall man wearing a tiger mask who just made eye contact with me. That’s enough. Come forward.”

The tiger-mask lottery’s value plummeted with the sudden addition of gender and height requirements. Now that my odds of being the winner had shot up, I could almost feel sweat beading on my forehead.

I hurriedly lowered my head to avoid Yohi’s gaze, then discreetly crossed my legs.

After hiding my Black Anaconda perfectly between my legs, I raised my head—and met Yohi’s gaze, which had gone completely cold.

“……”

“……”

The procession, which had continued amid the cheers, had come to a stop some time ago.

Under the suffocating silence that had settled over the marketplace and the gazes of Yohi and countless others, I uncrossed my tightly clenched legs and opened my mouth in a solemn voice.

“Um, did you call for me?”

“……”

“……”

They only looked back and forth between my masked face and my lower body. No one answered.

*Shit. I should’ve just stepped forward when she first called me.*

* * *

A leader needed many virtues. Among them, a keen eye was essential.

“I had a strange feeling the moment I saw you.”

After the celebratory procession for the subjugation of the man-eating beasts ended, Yohi had sent an attendant to summon me privately. Now she continued in her languid voice.

“Somehow, you were the only one who seemed out of place among all those people.”

Beside her, the great chieftain of the Yi people, who had been popping fruit into his mouth nonstop, grinned broadly and chimed in.

“She’s right. You were standing there like a block of wood all by yourself. You really stood out.”

The middle-aged man had a plump build that didn’t suit a warrior. He waved his hand, still damp with fruit juice, in greeting.

“You’re quite a rude fellow, keeping your mask on even now. I don’t know who you are yet, but you already know who I am, don’t you? I’m Heugung, and I lead the Yi people.”

Heugung. The name meant Black Bear.

So that was why he had been riding a bear during the procession. Apparently, people around here routinely kept fierce animals named after themselves as pets.

*What am I supposed to say to that?*

In truth, now that things had turned out this way, I had been planning to take off my mask and reveal my identity. That was why I hadn’t slipped away beforehand.

But Yohi was far more perceptive than I had expected.

“You can leave the mask on. Jin Taekyung of the Jin Family of Taiyuan.”

“Hmm?”

“Oh?”

I was a little surprised. First, because Yohi had only just arrived, yet already knew my identity. And second, because Heugung—the other great chieftain—was even more shocked than I was.

At the sight of Heugung and me both freezing for a moment, Yohi let out a quiet laugh.

“Why are you so surprised? I already heard that the Palace Lord brought the Han Chinese group sent by the Murim Alliance into the Inner Palace.”

Heugung tilted his head with a bewildered expression.

“Han Chinese from the Murim Alliance? Really? I hadn’t heard anything about that.”

“That’s because you’re as slow as a foolish bear. Though that side of you is charming.”

Even the Skeleton King would have realized that her added compliment was nothing more than lip service, but Heugung only grinned happily.

“Are you being sincere?”

“Of course. Don’t forget that I’ve always been in love with you.”

Her voice and gaze were alluring. When her pale, flawless fingers—so white and unblemished that it was hard to believe she was from Nanman—stroked his pockmarked cheek, rapture spread across Heugung’s face.

“Ahh. My dear.”

If someone asked me to describe this scene in three words, I would have answered without hesitation.

*Ugh. Fucking hell…*

A middle-aged man in his fifties with a bulging belly was melting like butter beneath the touch of a woman in her twenties.

People said that love knew no age or borders, but at this point, they would have to invent new ones.

*Not that it was real love anyway.*

Now I understood why the Yi people’s power had been dropping day by day like a stock awaiting delisting. I also understood why the Yao people had been able to grow so strong.

*Still… different as they are, there are some similarities.*

Just as I was thinking of someone else, Yohi glanced at me and stroked Heugung’s shoulder.

“But, big brother.”

“B-big brother?”

It was a line I had heard a few times in the daily dramas my mother liked to watch.

*Don’t call me Manager. Call me Oppa.*[^1]

Yohi had struck precisely the sort of nerve that could drive a pathetic middle-aged man insane. Her gentle voice continued as Heugung looked ready to die from happiness.

“Would you mind stepping outside for a moment? There’s something important I want to ask this Han Chinese man.”

“Hmm? Of course. I should. If that’s what you want, I’ll do anything!”

“Thank you, big brother. See you later.”

“Ooh. Oooooh!”

Heugung left the tent with an excited face, forcefully exhaling through his nose. Yohi let out a quiet laugh, leaned against the silk bedding, and muttered.

“Fucking moron.”

I had roughly expected something like this, but it was worse than I’d imagined. As I scratched my chin, Yohi raised the corners of her mouth.

“What? Was I too obvious?”

When someone came at you this directly, it was actually easier.

I thought for a moment, then answered honestly.

“Well, you’re not wrong.”

“You weren’t particularly surprised, so I suppose you had already figured it out. I thought you were only good at martial arts, but you’re more perceptive than I expected.”

“It’s not a personality that’s completely unheard of. The Central Plains has more than a few people who are different on the inside from what they show on the outside.”

“Really? I suppose the Central Plains must be very large. A bitch like me is rare in Nanman. Oh, is that girl who came with you the same sort? I think I heard her name was… Ju Hwaran?”

I stared at Yohi instead of answering. The smile at the corners of her mouth grew even broader.

“Fine. I take it back. Judging by your expression, I must have said something I shouldn’t have.”

I didn’t know what expression I had made at that moment. But it probably wasn’t a particularly kind one.

That was just how it felt.

With a strange feeling in my chest, I forced myself to speak calmly.

“Watch what you say next time. She’s a member of the Fire Dragon Pavilion who trusted me enough to follow me all the way to Nanman.”

“Oh? Just a subordinate you care about?”

“I don’t really distinguish between people based on whether they’re superiors or subordinates… but think whatever you want.”

“I appreciate you putting it that way. I happen to have quite a vivid imagination.”

Yohi let out an enigmatic laugh, apparently imagining something, then continued.

“You were staring at me so intently earlier that I got the wrong idea. I wondered if you had fallen in love at first sight.”

“As if. I’m not the kind of guy who just likes anyone.”

“Then why were you looking at me like that? Did Heugung, that fucking moron, look pathetic to you?”

“No. You reminded me of someone I’d seen before.”

Interest appeared in Yohi’s eyes.

“Who? A woman?”

“A woman, yes. You wouldn’t know who she was even if I told you now.”

In truth, she was closer to a monster than a woman. The person Yohi had reminded me of was the Southern Heaven Demon Empress.

The people belonging to Dark Heaven were monsters to whom distinctions between men and women meant nothing. They were fanatics who worshipped the Lord of Heaven.

“Hmm. A woman… Does she resemble me that much?”

“A little. But fundamentally, you’re different.”

“How can you be so sure? I could be that woman, you know?”

Yohi made a mischievous face, but I had already checked with Qi Sense just in case. There wasn’t even room for confusion.

*Like I said, the two of them were fundamentally different.*

If Yohi’s appearance and air were bewitching, the Southern Heaven Demon Empress possessed a magic all her own that could ensnare people.

And that wasn’t limited to her looks.

*Her atmosphere.*

The Southern Heaven Demon Empress had a distinctive air that was both beautiful and natural—and because it was so natural, impossible to suspect.

Even I had only realized how dangerous her beauty and atmosphere were after she completely deceived me in Hubei Province.

“Either way, you’re different.”

“Hmm. How boring. Whoever she is, she must be important, then?”

“She is. More than that, she’s dangerous.”

“Dark Heaven. It’s Dark Heaven, isn’t it?”

Yohi was perceptive indeed. She already knew why I had come to Nanman, tens of thousands of li away from the Central Plains, and what I had come here to do.

“I’m sorry to tell you this, but none of the great chieftains of the four great tribes want to join the alliance. Not a single one—except the Palace Lord.”

“What about you?”

“Me? I don’t particularly care either way. No matter what losses the Nanman Beast Palace suffers, I want our Yao people to unite the four great tribes under us.”

“That’s just your opinion. The other tribal chiefs…”

“Of course, there are chiefs who don’t think that way. But one thing is certain. Most of them share the desire for their tribes to grow stronger. And if they shed blood for nothing in the Central Plains, their power within Nanman will naturally diminish.”

I suddenly remembered what the Beast Miao King had told me earlier in the Inner Palace.

He was the lord of the Nanman Beast Palace and one of the Ten Kings recognized even in the Central Plains, but ultimately, he was still the great chieftain of the Miao people.

If the chiefs who controlled every large and small part of Nanman thought the same way as Yohi, then, just as Yayul Mok had said, it was effectively impossible for the Nanman Beast Palace to join the Murim Alliance.

*God, the negotiation difficulty here is fucking ridiculous.*

I hadn’t come to Nanman as a diplomat, but this situation was still as good as a failure before it had even begun.

Yohi looked amused by my bewilderment.

“I’m sorry, but that’s reality. Ah, of course, there’s at least one person you might have a chance of persuading. He leads a tribe large enough to rank among the four great tribes, and he’s so stupid that it’s hard to believe.”

I already knew who she meant from that description alone. I spoke with a sigh.

“Heugung?”

Yohi burst into loud laughter.

“Yes, that fucking moron. He can’t do a thing with me and that old man Baeksang keeping him firmly under our thumbs anyway.”

“……”

Even so, he was the great chieftain of a huge tribe that raised quite a few bears in Nanman. Was this treatment for real?

Just thinking about Heugung made my heart shrink.

*And if I really had any chance of persuading Heugung, she wouldn’t have kindly told me about it.*

Heugung was nothing more than a puppet, grinning idiotically without even realizing that he was being manipulated by Baeksang and Yohi.

*Was she messing with me or what?*

Just as I was frowning at Yohi, the area outside the tent suddenly grew busy, and a voice reached us.

“Yohi. Are you in there?”

It was a cold, dry voice.

Baeksang.

[^1]: *Oppa* is a Korean form of address used by a woman for an older brother or older man, often with romantic overtones.
```

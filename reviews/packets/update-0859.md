<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0859.txt",
      "sha256": "a1a1b93cee9c0b44b2b485f0c2f3654818e1b896c3ff6dc171da56e649c9f69b",
      "bytes": 13200
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "216cebebd9a5038961c4b06fb76049e30e6c7999583a9e6c82b515828feb8769",
      "bytes": 2021
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "9390505d674fb676ba71d497b7c076a11d913316c6d7748dc8dcaf650196fd7e",
      "bytes": 228651
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "facb5c385b3bd35b79bf0d7f5fd85e5c914207d36070ad0002f724a8482bff52",
      "bytes": 1325
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "ae412e5f13c6c137595e947bea6920dbfafeb7b0e922507f0d7993961504a002",
      "bytes": 759
    },
    {
      "path": "characters/Hong Jin.md",
      "sha256": "6a8bf669d7de3aede0d0c1d1ec2b86976682063f2ac1df22d850e5b31b7467e8",
      "bytes": 797
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "3d2ab9d20a8a3d419b50a4a93dc8a187d0f5a41211e1ea30e933ae0ed947ab56",
      "bytes": 1378
    },
    {
      "path": "characters/Jeong Hogun.md",
      "sha256": "077f21c4518920f5e14701c9e095fa7b39c048bf588bd05c9c92a725ef5ff1be",
      "bytes": 627
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "5543669cddb8684c7adbabb43c7932f15baccc02b361e63fa3e532e5f167de46",
      "bytes": 1782
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "d6ad2ebe60f26dd8acac0ba2778f0367cf799ca34984960f26e39b229fa2c15c",
      "bytes": 622
    },
    {
      "path": "characters/Ju Hogun.md",
      "sha256": "a044994158b66c8addee5983a0ad4861aeb742ec3b8d44650340209b914310a7",
      "bytes": 832
    },
    {
      "path": "characters/Jung Ho.md",
      "sha256": "531311d87ec772333b473ef01d53ae599aa8cafaf9aec9fca95c4ef7e9583bec",
      "bytes": 699
    },
    {
      "path": "characters/Prince Shangshan.md",
      "sha256": "365778bd8748a53089d4cfd1f071dd9b981af9048233ce412f4aafaba360098c",
      "bytes": 883
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "7d5589ecb1e0d436b2f0bfc393a6ea88afdb27fd2a300931984bfcfd7857ec4c",
      "bytes": 254014
    }
  ],
  "estimated_tokens": 12248
}
-->

# Durable State Update — Chapter 859

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
1 and safe_through 859. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 859. Profile updates may replace only one
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
  "chapter": 859,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 859,
    "continuity_sources": [859],
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
    "The Divine Physician secured the Blood Soul Gu found in the deceased City Lord of Sichuan Province; it weakens hosts, causes madness, and eventually kills them.",
    "Jin suspects Dark Heaven's covert killing of the City Lord may be part of a scheme targeting the Great Nation, possibly its imperial family.",
    "Prince Shangshan Zhu Bao is traveling toward the imperial capital with Hong Jin and fifty Embroidered Uniform Guard members; the late Emperor entrusted Hong Jin with Zhu Bao's care, while Zhu Bao trusts his elder brother.",
    "Jin's party reached its destination ahead of the Embroidered Uniform Guard after an arduous journey; Jin was severely sleep-deprived and briefly rested in a tree while Mujin kept watch.",
    "Mujin held his ground against the Guard until Jin awoke; Jin praised his resolve but told him to withdraw and reconsider when outmatched.",
    "Commander Jeong is Jeong Hogun, a highly skilled general leading dozens of Peak-level Embroidered Uniform Guard martial artists who claim loyalty to the Emperor's command.",
    "Zhu Bao reunited with Jin, gave him a secret letter, and asked for his autograph."
  ],
  "continuity_sources": [
    857,
    858
  ],
  "open_questions": [
    "Why did Dark Heaven secretly kill the City Lord of Sichuan Province, and is it targeting the Emperor or imperial family?",
    "What does the Emperor intend for Prince Shangshan, and what prompted the imperial decree against Hong Jin?",
    "What does the secret letter Zhu Bao handed Jin contain?",
    "Who trained the Embroidered Uniform Guard force of highly skilled martial artists, and for what purpose?"
  ],
  "safe_through": 858,
  "temporary_decisions": [
    "Render 혈혼고 as “Blood Soul Gu.”",
    "Render 대국 as “Great Nation.”",
    "Render 금의위 as “Embroidered Uniform Guard.”",
    "Render 강소 as “Jiangsu.”",
    "Render 정호군 as “Jeong Hogun” and 정 천호 as “Commander Jeong.”"
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 혁무진    | **Hyuk Mujin**     |
| 청풍     | **Cheongpung**     |
| 태원진가   | **Jin Family of Taiyuan**        |
| 열화문    | **Fire Gate Clan**               |
| 암천     | **Dark Heaven**                  |
| 절정     | **Peak**          |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 강호     | **martial world**                                | Prefer “Murim” where the setting itself is meant      |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 사천     | **Sichuan**            |
| 화산     | **Huashan**            |
| 도사      | **Daoist**                                                      |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 홍진 | **Hong Jin** | Level 22 man at the City Lord's luncheon; delicate in appearance and voice. |
| 정호군 | **Jeong Hogun** | Commander of the Embroidered Uniform Guard force confronting Jin. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 주호군 | **Ju Hogun** | Ju Hwaran's father and former leader of the Yongbong Escort Bureau. |
| 정호 | **Jung Ho** | Middle-aged Shaolin martial monk leading the traveling group. |
| 상산왕 | **Prince Shangshan** | The City Lord and a member of the imperial family who orders the luncheon. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 주신 | **God of Drinking** | Wipeng's drinking epithet. |
| 천자 | **Son of Heaven** | Honorific title for the Emperor. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 주표 | **Zhu Bao** | Personal name of Prince Shangshan. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 절강성 | **Zhejiang Province** | Province where the Geumwa Merchant Group ranks among the top three merchant groups. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 화산신룡 | **Huashan Divine Dragon** | Title given to Cheongpung after the Star-Array Grand Banquet. |
| 열화신룡 | **Blazing Flame Divine Dragon** | New sobriquet bestowed on Jin Taekyung. |
| 이룡 | **Two Dragons** | Collective ranking beneath the Ten Kings in Murim gossip. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 절강 | **Zhejiang** | Region from which the boat travels east. |
| 황족 | **Huang tribe** | Nanman tribe involved in a recently settled dispute. |
| 화신 | **Fire God** | A local deity worshiped by one Nanman believer. |
| 금의위 | **Embroidered Uniform Guard** | Imperial guard force mentioned by Hong Jin. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
| 청풍 | 진태경 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung repeatedly addresses Taekyung as 은인 after receiving food. |
| 청풍 | 혁무진 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung includes Mujin among his 은인들 after receiving the skewers. |
| 혁무진 | 청풍 | martial artist to young master | Young Master | formal-deferential | Mujin uses 공자께서는 when asking why Cheongpung descended from the mountain. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 진태경 | 청풍 | companion_to_young_martial_artist | Young Master Cheongpung | formal-polite | Taekyung uses 청 공자 while correcting Cheongpung's royal-etiquette mistake. |
| 홍진 | 주표 | servant and political aide to prince | His Highness | formal-deferential | Uses the elongated royal call 전하 while summoning Zhu Bao. |
| 진태경 | 주표 | visitor to prince | His Highness, Prince Shangshan | formal-deferential | Addresses Zhu Bao as 상산왕 전하 after kneeling to meet his gaze. |
| 주표 | 진태경 | prince to visiting young hero | Jin Taekyung | formal and inquisitive | Uses the formal second-person address before asking Taekyung's name and requesting an autograph. |
| 홍진 | 진태경 | political_host_to_young_martial_artist | Young Hero Jin; Young Master Jin; Sleeping Dragon of Shanxi | polite, coaxing, and probing | Uses respectful forms while steering Taekyung toward relaying the Escort Bureau proposal and teasing him with the Seongun Escort Bureau. |
| 진태경 | 홍진 | young_martial_artist_to_political_official | Comrade Chairman—no, Deputy Military Commissioner | casual and teasing, then formally corrective | Deliberately jokes with an inappropriate title before correcting himself to Hong Jin's official office. |
| 주표 | 청풍 | prince_to_young_martial_artist | you | formal and gatekeeping | Refuses Cheongpung's autograph until he acquires a martial title. |
| 홍진 | 청풍 | political_official_to_young_martial_artist | Young Master | formal and curious | Uses 공자께서는 while asking whether Cheongpung has always lived on Huashan. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 정호 | 진태경 | Shaolin Discipline Hall Master to patient and Benefactor | Benefactor Jin | formal-polite | Jung Ho repeatedly uses 진 시주 and 시주. |
| 진태경 | 정호 | patient to Shaolin Discipline Hall Master | Monk | polite and familiar | Taekyung addresses Jung Ho as 스님. |
| 혁무진 | 조장님 | pavilion_member_to_squad_leader | Captain | deferential and dubious | Mujin questions whether the pasture should be called the Nanman Ranch instead of the Nanman Beast Palace. |
| 주표 | 홍진 | prince to loyal subject | you | formal and reassuring | Zhu Bao refers to Hong Jin as 그대 while apologizing for the hardship he has endured. |
| 진태경 | 정호군 | young martial artist to senior imperial officer | Commander Jeong | casual and teasing, then conciliatory | Jin addresses him by rank while trying to defuse the standoff. |

## Listed compact profiles

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 852
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, the grandson and Disciple of Sword Saint Mae Jonghak, a Supreme Peak martial master known as the Huashan Divine Dragon, the creator of the snake-inspired Mimi Step footwork technique, and the master of the Azure Dragon Pavilion within the Alliance Leader's Two Dragons Pavilion.
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, a deep love of martial arts, competitive pride, unusual resistance to monster-induced Fear, and discomfort when someone copies his martial arts.
- **Voice:** Dreamy and hazy, with innocent, polite phrasing; he has begun imitating Taekyung's profanity.
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions while Taekyung is his only true martial rival; Tang Sadok has temporarily entrusted Mimi, now a large horned snake, to him, and Cheongpung is accompanying Mungyeong while learning his martial arts through observation to become stronger and adapt to this world.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 858
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Hong Jin.md

# Hong Jin (홍진)

- **Safe through:** Chapter 856
- **Aliases:** None
- **Role:** Hong Jin is a Level 22 Deputy Military Commissioner of Shanxi Province, a eunuch who served the late Emperor and has been entrusted with Prince Shangshan’s protection since the prince’s infancy.
- **Personality:** Composed and socially deft, Hong Jin is considerate toward those beneath him and dislikes excessive deference, which recalls his impoverished past.
- **Voice:** Delicate and deferential, using formal, self-effacing language with Prince Shangshan.
- **Relationships:** Hong Jin is devoted to Prince Shangshan, whom the late Emperor entrusted to his care, and trusts Jin Taekyung as the person best able to keep the prince safe.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 858
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and an active member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented; loyal even when left behind, irreverently self-deprecating, and willing to face danger rather than abandon the person he serves. He is proud, glory-seeking, suspicious of Taekyung, bluntly critical of the family's disgraced third son, and an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad; as a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Fire Dragon Pavilion members accompanying Taekyung. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jeong Hogun.md

# Jeong Hogun (정호군)

- **Safe through:** Chapter 858
- **Aliases:** None
- **Role:** Jeong Hogun is a commander of the Embroidered Uniform Guard and a highly skilled martial artist whose force includes dozens of Peak masters.
- **Personality:** Disciplined and resolute, he presents loyalty to the Emperor's command as the foundation of his force's actions.
- **Voice:** Formal and rigid, emphasizing duty to imperial authority.
- **Relationships:** Commands the Embroidered Uniform Guard force confronting Jin Taekyung and serves the Emperor's command.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 858
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader.
- **Personality:** Hungry, self-aware, dryly observant, and pragmatic under pressure; accepts extreme personal risk when duty and the lives of others demand it.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; they trust each other deeply, though their bond remains unformalized. Cheongpung is his trusted companion and only true martial rival; Choi Minwoo is his subordinate and trusted manager of media and official arrangements as well as the Peace Guild's Guild Master; Ju Hwaran is a trusted Fire Dragon Pavilion member; Magic Johnson and Chuck Hagel are allied to him; his mother and sister Hayeon are among those he protects; the Skeleton King is his friend and ally; Xiao Shen regards him as an older brother; Jin-ho is his older friend and trusted confidant; he once saved Ju Wongong’s life.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 858
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Ju Hogun.md

# Ju Hogun (주호군)

- **Safe through:** Chapter 330
- **Aliases:** None
- **Role:** Ju Hwaran's father and the only blood child of Escort King Ju Gongsan; he inherited leadership of the Yongbong Escort Bureau, but his chivalrous generosity and inability to pursue profit caused it to shrink substantially over thirty years before he fell into qi deviation during cultivation two years earlier and was left between life and death, now awaiting the elixir Song Ilseom plans to bring from Xianyang.
- **Personality:** Loving, proudly doting, and deeply confident in his daughter's ability.
- **Voice:** Warm, affectionate, and praising toward his daughter.
- **Relationships:** Ju Hwaran is his only daughter and the sole person he expects to carry on his legacy.

### Jung Ho.md

# Jung Ho (정호)

- **Safe through:** Chapter 858
- **Aliases:** None
- **Role:** Middle-aged Shaolin martial monk and Master of Shaolin's Discipline Hall who leads the traveling group and wields a Zen staff hung with prayer beads.
- **Personality:** Humble, observant, principled, and concerned with the safety of commoners.
- **Voice:** Formal, restrained, and admonitory, with Buddhist phrasing.
- **Relationships:** Unnamed is his young Martial Uncle; he leads the Shaolin monks traveling with him, addresses Sama Pyo as a Benefactor, and is recognized by Jin Taekyung as Park Jung Ho, a former Garam Middle School classmate.

### Prince Shangshan.md

# Prince Shangshan (상산왕)

- **Safe through:** Chapter 858
- **Aliases:** None
- **Role:** Prince Shangshan, whose personal name is Zhu Bao, is an early-adolescent member of the imperial family and an exceptionally skilled young swordsman who has trained daily for three years.
- **Personality:** Earnest, compassionate, and eager to emulate Jin Taekyung; he takes responsibility for his loyal subjects’ hardship, though his trust in his elder brother shows his youth.
- **Voice:** Archaic and formal in the manner of a historical drama, with openly eager and childlike reactions beneath his royal diction.
- **Relationships:** Prince Shangshan Zhu Bao is the Emperor’s only younger full brother; the late Emperor entrusted Hong Jin with his care, and Zhu Bao admires Jin Taekyung and seeks to emulate him.

## Korean source

```text
＃859화



“외람되지만, 제가 한 말씀 드려도 되겠습니까?”

말머리를 나란히 한 채 나아가던 수하의 말에, 정호군은 담담하게 대답했다.

“스스로 외람되는 말이라고 생각한다면, 처음부터 꺼내지 말거라.”

“천호(千戶)!”

깊게 가라앉은 눈빛과 딱딱하게 굳은 표정.

벌써 십 년이 넘는 세월 동안 동고동락한 수하다. 정호군은 이미 듣지 않고도 그가 할 말을 알고 있었다.

“네 마음은 충분히 짐작하고 있다. 지금 이 상황이 못마땅한 거겠지.”

“못마땅한 정도가 아닙니다. 천호께서는 저 무뢰배들을 이대로 지켜만 보실 겁니까?”

등 뒤를 힐끗 노려보는 수하의 시선 끝에는, 천천히 이동 중인 마차 한 대가 있었다.

미세하게 열린 창문 틈새로 끊임없이 흘러나오는 웃음과 대화 소리에, 수하는 물론이고 주위의 금의위들 또한 표정이 굳어졌다.

“지금이라도 늦지 않았습니다. 명령만 내려 주신다면…….”

수하는 말꼬리를 흐렸지만, 그 안에 담긴 뜻을 알아채지 못할 정호군이 아니었다.

“한바탕 혈전이라도 벌일 셈이더냐.”

“천호께서 우려하시는 바는 저도 압니다. 하지만 하늘 같은 황명(皇命)에 반하는 역도의 무리를 이대로 놔둘 수는 없지 않습니까.”

“가만히 놔두지 못한다면. 그자를 쓰러트릴 자신은 있고?”

“그건…….”

수하는 문득 말문이 막혔다.

비록 군문(軍門)에 속한 몸이지만 그 역시 무공을 수련한 한 사람의 무인.

지금쯤 마차 안에서 웃고 떠들고 있을 ‘그자’를 떠올리니 쉽게 말문이 열리지 않았다.

태원진가의 진태경.

아니, 열화신룡(烈火神龍) 진태경.

‘아직 젊다고 말은 들었지만, 저 정도일 줄이야.’

금의위에는 천하 각지의 온갖 정보가 들어온다.

그러나 열화신룡에 관한 온갖 이야기들은, 곳곳에 심어 놓은 세작(細作)들을 통하지 않더라도 익히 들어 보았을 만큼 유명했다.

몰락한 무가의 후손.

오직 일인전승(一人傳承)으로 장장 삼백여 년간이나 이어져 내려온 열화문의 후계자.

산서 땅에서 모르는 사람이 없던 망나니는 불과 이 년 남짓한 짧은 시간 만에 신룡이라 불리게 되었고, 현재 무림을 뒤흔들고 있는 격랑의 중심에 서 있었다.

그러나 진태경이 이토록 특별해질 수 있었던 가장 큰 이유는, 누가 뭐라 해도 단 한 가지뿐이었다.

‘그 무위(武威).’

모든 것에는 한계가 있고, 무공이라 한들 예외는 아니다.

하지만 진태경은 이미 그 한계를 아득히 뛰어넘었다. 그런 그가 화산신룡 청풍과 함께 이룡(二龍)이라 불리며 천고의 재능이라 칭해지는 것은 결코 이상한 일이 아니었다.

정호군의 수하가 긴 침묵 끝에 이런 대답을 내놓은 것 역시도.

“분하지만…… 현재의 상황으로는 대적하기 어렵습니다.”

“알고 있다면 되었다.”

정호군은 담담하게 대꾸했다. 지엄한 황제의 명을 받드는 금의위로서는 치욕스러운 결론이었지만, 군인으로서는 옳은 대답이다.

승패(勝敗)에 대해서는 언제나 냉정해야 한다.

일말의 자존심으로 그릇된 판단을 내린다면, 그 전투는 결코 승리할 수 없다.

다만 어느 경우에서도 금의위가 잃지 말아야 할 태도는, 어떠한 강자 앞에서도 굴복하거나 물러서지 않는 것이다.

“너의, 아니 너희 모두의 마음을 안다.”

정호군은 나직이 말을 이었다.

“그러나 우리가 받은 황명은 상산왕 전하를 황도까지 모셔오라는 것이었다. 최대한 은밀하게, 아무런 잡음도 없이.”

“…….”

“만약 상산왕 전하께서 검을 내려놓으라 명하시지 않았다면, 나 역시 맞서 싸웠을 것이다.”

하지만 상산왕 주표의 행동은 금의위 모두를 대경하게 만들었다.

황실의 고귀한 피를 이어받은 이 어린 왕은, 강호의 무뢰배를 손수 일으켜 세우는 것으로도 모자라 소지하고 있던 은패(銀牌)에 친필 서명까지 받길 원했으니까.

“이미 엎질러진 물이다. 이 사안에 관한 결정은 우리의 몫이 아니니, 이에 대하여 더는 논하지 말라.”

조금의 반박조차 허락하지 않는 단호한 목소리에, 수하는 굳게 입을 다물었다.

주호군의 말이 맞다. 그들에게 주어진 임무는 상산왕을 황도까지 데려오는 것뿐이다. 천자를 향한 충심(忠心)과 권한은 다른 의미다.

그리고 애써 불만을 억누르는 수하를 향해, 주호군은 재차 말을 이어 갔다.

이번에는 오직 한 사람만이 들을 수 있는 전음(傳音)으로.

- 해 주어야 할 일이 있다.

크게 뜨여진 눈으로 주호군을 바라보던 수하가 이내 입술을 달싹였다.

- 하명하십시오.

- 황도에 계신 지휘사(指揮使)께 가거라. 네가 직접.

- 지휘사께 말입니까?

지휘사는 곧 금의위의 수장.

온갖 거물들이 득실거리는 황도의 고관대작(高官大爵) 중에서도 손꼽히는 영향력과 실권을 지닌 것이 바로 금의위 지휘사였고, 그가 지닌 강대한 권력은 오직 한 사람으로부터 비롯된 것이었다.

- 그 말씀은…….

수하는 말을 끝맺지 않았으나, 뒤에 이어질 말이 뜻하는 누군가의 신분은 두 사람 모두가 알고 있었다.

천자(天子).

이 광활한 대륙의 주인.

옥좌에 앉아 수많은 신하와 백성을 굽어보는 거인.

그리고 그들 금의위가 존재하는 이유이자, 절대적인 충성을 바치는 대상.

그렇기에 지휘사에게 소식을 전하라는 정호군의 말은, 곧 천자에게 보고를 올리라는 뜻이나 다름없었다.

- 천호께서는…… 제가 어찌하길 원하십니까.

- 지금 즉시 떠나라. 그리고 곧장 지휘사를 찾아뵙고 이렇게 말씀드려라.

정호군은 천천히 전음을 이어 갔다.

- 당신께서 예측하신 대로, 불청객들이 끼어들었다고.

- ……!

- 가거라. 멀리 나가지는 않겠다.

도저히 믿을 수 없다는 듯, 눈을 부릅뜬 채 정호군을 바라보던 수하의 입가에 문득 희미한 미소가 스쳐 지나갔다.

예측. 분명 예측이라고 했다.

그 두 글자면 충분하다. 어째서인지 평소와는 다른 모습이었던 상관에 대한 불만도, 구겨진 금의위의 자존심도 완벽하게 회복되었다.

- 충(忠)!

차마 소리 내어 외칠 수 없는 힘찬 군례(軍禮)와 함께, 말과 한 몸이 되어 바람처럼 사라지는 수하의 뒷모습을 바라보던 정호군은 내심 중얼거렸다.

모든 것은 금의위의, 아니 지엄하신 천자(天子)의 손바닥 위에 있었다.

언제나 그랬듯이.



* * *



감각이란 곧 시야와 같다.

눈앞의 것만 본다고 해서 주위의 풍경이 완전히 지워지지 않는 것처럼, 나는 대화를 나누면서도 예리한 감각을 통해 사방에서 전해지는 모든 정보를 받아들였다.

울창한 풀숲 사이를 총총 뛰어다니는 날짐승들의 기척.

마차를 호위하듯, 아니 포위하듯 감싼 금의위들의 주위로 감도는 냉랭한 공기.

그리고…….

빠르게 멀어지는 말발굽 소리 역시도.

“그대에 관한 소식은 계속해서 전해 듣고 있었다. 그 믿을 수 없는 무용담(武勇談)을 들을 때마다 과인의 가슴이 벅찰 지경이었지.”

“과호흡 증상이면 좀 걱정인데. 마침 제가 잘 아는 의원 하나 있으니까, 전하도 이번 기회에 진찰 한 번 받아 보세요.”

“이렇게 과인을 걱정해 주니 참으로 기쁘구나. 허나 누구인지도 모르는 의원에게 몸을 맡기는 것은 황실의 예법에도 어긋나는 일. 황도에 도착하면 어의(御醫)가 있으니…….”

“그럼 어쩔 수 없네요. 하긴, 신의(神醫) 어르신께서도 지쳐 있으니 그게 낫겠어요.”

“잠깐. 지금 누구라 했는가?”

“신의요.”

“받겠다! 꼭!”

“황실의 예법은요?”

“법은 어기라고 있는 것이다.”

제아무리 고귀한 황족이라 해도 결국은 어린아이.

나는 발갛게 상기된 얼굴로 조잘조잘 떠들어 대는 상산왕 주표에게 적당히 맞장구쳐 주며, 그의 어깨너머로 보이는 홍진을 향해 전음을 흘려보냈다.

- 놈들이 어딘가로 사람을 보냈습니다. 그런데 제 생각에는 아무리 봐도 척후는 아닌 것 같네요.

무공을 익히긴 했으나, 절정의 경지까지 이르진 못한 홍진은 전음 대신 조용히 고개를 끄덕였다.

마차 주위를 둘러싼 금의위들을 다분히 의식하는 행동이었다.

- 소식을 전하러 간 것이 분명한데, 어디로 간 것 같습니까?

어디서 꺼무위키라도 봤는지, 주표가 신의에 대해 줄줄이 읊어 대는 사이 홍진은 손가락을 붓 삼아 허공에 글자를 써 내려갔다.

황도(皇都).

좋지 않은 소식이지만, 어느 정도는 예상했던 바다.

애초에 금의위는 대국의 황제가 수족으로 부리기 위해 창설한 집단.

특히나 상산왕 주표에 관련된 모든 사안은 황제의 귀로 흘러 들어갈 것이 틀림없었다.

‘황도라…….’

좋아한다. 복숭아는.

하지만 무림에서의 황도란 그야말로 천하의 중심을 뜻했다.

아니, 황제라는 지위가 가지는 의미가 바로 그러했다.

광활한 천하를 다스리는 만백성의 주인. 천자가 머무르는 곳이 바로 천하의 중심이며 용의 둥지다.

‘물론 지금 같은 경우에는 호랑이굴이지만.’

황도에 직접 가 본 적은 없지만, 풍문은 꽤 자주 들었다.

하늘을 찌를 듯이 높게 솟은 거대한 건물들. 보는 이로 하여금 절로 탄성을 자아내는 아름다운 명승고적(名勝古跡)과 운하를 통해 넘쳐흐르는 재물들.

비옥한 토지와 풍부한 물자까지 더해지니, 그야말로 천하에서 둘째가라면 서러운 지상낙원이 따로 없다.

단 한 가지만 빼면.

‘천자와 황도를 수호하는, 백만의 금위군(禁衛軍).’

만 명도, 십만 명도 아니다.

무려 백만이다.

대륙 놈들 특유의 허풍이 들어갔다는 사실을 감안해서 그 절반이라고 쳐도, 황도인 절강성의 인근에만 약 50만이 넘는 대군이 도사리고 있는 셈이다.

‘그 정도면…… 시벌, 감도 안 잡히네.’

나도 모르게 바짝 마른 입술을 핥았다.

개인적으로도 도저히 이러고 싶지는 않지만, 사천에서부터 줄곧 뇌리를 떠나지 않던 불길한 예감은 어쩔 수 없었다.

‘만약 황제와 암천이 모종의 관계를 맺었다는 짐작이 사실이라면?’

그에 대한 답은 고민해 볼 필요도 없었다.

좆 되는 거지. 뭘.

백만에 달하는 금위군이 겹겹이 에워싼 황도로 진입하는 순간 모든 것이 끝장이다.

살아 있는 신이나 다름없는 천자가 명령만 내린다면, 사방에서 무수한 칼날이 날아들 것은 불 보듯 뻔했다.

천자로서는 그리 길게 말할 필요도 없다. 손가락으로 우리를 가리키며 딱 한 마디만 하면 된다.

해로운 역적이다.

“…….”

상상만으로도 오금이 저리는 상황.

내가 말없이 입을 다물자, 마차 한구석에 쭈그러져 있던 혁무진이 조심스럽게 물었다.

“왜 그렇게 똥 씹은 얼굴을 하고 계세요?”

“……무진아.”

“예. 조장님.”

“넌 매번 말하는 태도는 조심스러운데, 그 안에 담긴 내용은 왜 이렇게 대담하냐.”

“제가 또 상남자 중의 상남자 아니겠습니까. 상남자 열 명분의 몫을 하는 십상남자(十上男子) 혁무진! 그게 바로 접니다.”

“…….”

진짜 미친 새낀가.

말 대신 눈으로 혁무진을 향해 쌍욕을 퍼붓던 그때, 어느새 말을 멈추고 우리의 대화에 귀 기울이고 있던 상산왕 주표가 나직이 탄성을 흘렸다.

“십상남자라, 역시 그대의 수하답게 범상치 않은 별호로군.”

“……?”

“……?”

“이렇게 만난 것도 인연일 터. 십상남자 혁무진이라 하였더냐?”

눈을 깜빡이던 혁무진이 황급히 고개를 조아렸다.

“예, 예. 상산왕 전하. 하온데 외람되게도 소인의 별호는 십상남자가 아니라…….”

“자, 여기에 서명하거라.”

“예?”

“사양할 필요 없다. 십상남자 혁무진. 이는 네 가문 대대로 이어질 영광이니라.”

“…….”

“…….”

혁무진은 주표에게서 건네받은 동패에 자신의 새로운 별호를 새겨 넣었고, 나는 그 광경을 바라보며 생각했다.

지랄 났다. 진짜.
```

## Final English reading copy

```markdown
# Chapter 859

“Pardon me, but may I say something?”

Jeong Hogun answered calmly as one of his subordinates rode beside him.

“If you think what you have to say is out of line, then don’t say it in the first place.”

“Commander!”

The subordinate’s gaze was deeply troubled, his expression stiff.

He’d shared hardship with Jeong Hogun for more than ten years. The commander already knew what he was going to say without hearing it.

“I can guess well enough how you feel. You’re unhappy with this situation.”

“Unhappy doesn’t begin to cover it. Are you really going to let those rogues carry on like this, Commander?”

The subordinate glared over his shoulder at the slowly moving carriage.

Laughter and conversation poured incessantly through a window left slightly ajar. The subordinate’s expression hardened, as did those of the Embroidered Uniform Guard around him.

“It’s not too late. If you’ll just give the order…”

The subordinate let his voice trail off, but Jeong Hogun understood exactly what he meant.

“You’re thinking of starting a bloodbath?”

“I understand your concerns, Commander. But we can’t just let a band of traitors who defy the Emperor’s supreme command go free.”

“If we can’t let them go free, are you confident you can bring that man down?”

“Well…”

The subordinate was suddenly at a loss for words.

Though he belonged to the military, he was still a martial artist who had trained in martial arts.

The thought of the man laughing and chatting inside the carriage right now made it hard to answer.

Jin Taekyung of the Jin Family of Taiyuan.

No—Jin Taekyung, the Blazing Flame Divine Dragon.

*I’d heard he was still young, but I never imagined he’d be that strong.*

The Embroidered Uniform Guard received all kinds of reports from across the land.

But the stories about the Blazing Flame Divine Dragon were so famous that he’d heard them countless times, even without relying on the spies they had planted far and wide.

A descendant of a fallen martial family.

The heir to the Fire Gate Clan, passed down through a single successor for more than three hundred years.

The troublemaker nobody in Shanxi had failed to hear of had become a Divine Dragon in barely two years. Now he stood at the heart of the turbulent currents shaking Murim.

But there was only one reason Jin Taekyung had become so exceptional.

*His martial might.*

Everything had its limits, and martial arts were no exception.

But Jin Taekyung had already soared far beyond those limits. It was no wonder he was called one of the Two Dragons alongside Cheongpung, the Huashan Divine Dragon, and hailed as a talent unseen in a thousand years.

Nor was it surprising that, after a long silence, Jeong Hogun’s subordinate answered:

“Much as I hate to admit it… in our current situation, we’d have a hard time facing him.”

“If you know that, then that’s enough.”

Jeong Hogun replied evenly. For the Embroidered Uniform Guard, who served the Emperor’s solemn command, it was a humiliating conclusion. But as a soldier, it was the right one.

You had to be clear-eyed about victory and defeat.

If pride led you to make the wrong call, you could never win that battle.

But there was one attitude the Embroidered Uniform Guard could never abandon: never submit or back down before any opponent, no matter how powerful.

“I know how you feel. All of you.”

Jeong Hogun continued in a low voice.

“But the Emperor’s command was to escort His Highness Prince Shangshan to the imperial capital. As discreetly as possible, without causing the slightest disturbance.”

“……”

“If His Highness Prince Shangshan hadn’t ordered us to lower our swords, I would have fought them myself.”

But Prince Shangshan Zhu Bao’s actions had left every member of the Embroidered Uniform Guard stunned.

This young prince, born of the imperial family’s noble blood, had personally helped a rogue of the martial world to his feet—and then asked him to sign the silver token he carried.

“What’s done is done. This matter isn’t ours to decide. Don’t speak of it again.”

At the firm voice, which allowed not even the slightest objection, the subordinate pressed his lips together.

Commander Jeong was right. Their only duty was to escort Prince Shangshan to the imperial capital. Loyalty to the Son of Heaven and authority were two different things.

Then, turning to the subordinate who was struggling to contain his displeasure, Jeong Hogun continued.

This time, he used Sound Transmission, so only one person could hear him.

—I have something for you to do.

The subordinate stared at Jeong Hogun with wide eyes, then moved his lips.

—Give me your orders.

—Go to the Commander-in-Chief in the imperial capital. You, personally.

—To the Commander-in-Chief?

The Commander-in-Chief was the head of the Embroidered Uniform Guard.

Among the high-ranking officials packed into the imperial capital, where all manner of powerful figures gathered, the Commander-in-Chief of the Embroidered Uniform Guard held exceptional influence and authority. And his immense power came from one person alone.

—You mean…

The subordinate didn’t finish his sentence, but both men knew whose rank his words implied.

The Son of Heaven.

Ruler of this vast continent.

A giant who sat upon the throne and looked down over countless officials and subjects.

The very reason the Embroidered Uniform Guard existed—and the one to whom they gave their absolute loyalty.

So Jeong Hogun’s order to inform the Commander-in-Chief was no different from telling him to report directly to the Son of Heaven.

—Commander, what would you have me do?

—Leave at once. Go straight to the Commander-in-Chief and tell him this.

Jeong Hogun continued his Sound Transmission slowly.

—Just as you predicted, uninvited guests have interfered.

—…!

—Go. I won’t be going far.

The subordinate stared at Jeong Hogun, eyes wide with disbelief. Then a faint smile crossed his lips.

A prediction. He’d definitely called it a prediction.

Those two words were enough. His displeasure with his superior, who had seemed so unlike himself, and the Embroidered Uniform Guard’s wounded pride both vanished completely.

—Loyalty!

Unable to shout it aloud, the subordinate gave a vigorous military salute, then rode off like the wind, moving as one with his horse.

Jeong Hogun watched him disappear and thought to himself:

Everything was in the palm of the Embroidered Uniform Guard—or, more precisely, of His Imperial Majesty, the Son of Heaven.

Just as it always had been.

* * *

Senses were like vision.

Just as looking at what was in front of you didn’t erase the scenery around you, I took in every bit of information from all directions with my keen senses, even as I talked.

The small movements of birds bounding through the thick undergrowth.

The cold air swirling around the Embroidered Uniform Guard surrounding the carriage—as if to escort it, or maybe to hem it in.

And…

The sound of a horse’s hooves rapidly fading into the distance.

“I’ve continued to hear news of you. Every time I hear one of those unbelievable tales of your exploits, I can hardly contain my excitement.”

“If you’re hyperventilating, that’s a little concerning. I happen to know a good physician, so why don’t you get a checkup while you’re at it, Your Highness?”

“I’m glad you’re concerned for me. But entrusting my health to a physician I don’t even know would go against imperial etiquette. Once we reach the imperial capital, there will be an Imperial Physician, so…”

“Then I guess there’s no choice. The Divine Physician is exhausted, too, so that’s probably for the best.”

“Wait. Who did you say?”

“The Divine Physician.”

“I’ll see him! I absolutely will!”

“What about imperial etiquette?”

“Rules are there to be broken.”

No matter how noble a member of the imperial family he was, he was still a child.

I humored Prince Shangshan Zhu Bao as he chattered away, his face flushed, and sent a Sound Transmission to Hong Jin, visible over his shoulder.

—They’ve sent someone somewhere. But I really don’t think he’s a scout.

Hong Jin had learned martial arts, but hadn’t reached the Peak realm. Instead of answering with Sound Transmission, he nodded quietly.

He was clearly mindful of the Embroidered Uniform Guard surrounding the carriage.

—He must’ve gone to deliver a message. Any idea where?

Maybe he’d been reading fan wikis or something; while Zhu Bao rambled on about the Divine Physician, Hong Jin used a finger as a brush and wrote in the air.

The imperial capital.

It wasn’t good news, but I’d expected as much.

The Embroidered Uniform Guard had been created by the Great Nation’s Emperor to serve as his own hands and feet. Anything concerning Prince Shangshan Zhu Bao was certain to reach the Emperor’s ears.

*The imperial capital, huh…*

I liked peaches.

But in Murim, “the imperial capital” meant the very center of the world.

Or rather, that was what the Emperor’s position meant.

The ruler of all the people across this vast land. Wherever the Son of Heaven resided was the center of the world, the dragon’s den.

*Though in this case, it’s a tiger’s den.*

I’d never been to the imperial capital, but I’d heard about it often enough.

Enormous buildings that rose so high they seemed to pierce the sky. Beautiful historic sites that made visitors gasp in awe, and wealth pouring through its canals.

With fertile land and abundant supplies, it was practically a paradise on earth—second to none in the world.

Except for one thing.

*The million Imperial Guards protecting the Son of Heaven and the imperial capital.*

Not ten thousand. Not a hundred thousand.

A million.

Even if I allowed for the usual exaggeration from the people of this continent and cut that figure in half, there’d still be an army of over five hundred thousand stationed around Zhejiang Province, where the imperial capital stood.

*That many… Fuck, I can’t even picture it.*

I unconsciously licked my parched lips.

I really didn’t want to be acting like this, but I couldn’t shake the ominous feeling that had haunted me ever since Sichuan.

*What if my suspicion is right, and the Emperor has some sort of relationship with Dark Heaven?*

I didn’t need to think about the answer.

We’d be fucked. Simple as that.

The moment we entered the imperial capital, surrounded by layers upon layers of a million Imperial Guards, it would all be over.

If the Son of Heaven, who was as good as a living god, gave the order, countless blades would come flying at us from every direction. He wouldn’t even have to say much. He’d just point at us and say one thing:

“They’re dangerous traitors.”

“……”

Just imagining it made my legs go weak.

I’d gone quiet, and Hyuk Mujin, huddled in a corner of the carriage, asked cautiously,

“Why do you look like you’ve got a mouthful of shit?”

“……Mujin.”

“Yes, Captain.”

“You’re always so careful with your tone. Why is the content of what you say so damn bold?”

“Because I’m the manliest of men. Hyuk Mujin, the Tenfold Man—with enough manliness for ten men! That’s me.”

“……”

Is this guy actually insane?

I was silently hurling every insult I could think of at Hyuk Mujin with my eyes when Prince Shangshan Zhu Bao, who had stopped to listen to us, let out a quiet gasp.

“The Tenfold Man? That is an extraordinary title. Just what I’d expect from your subordinate.”

“……?”

“……?”

“It’s fate that we’ve met like this. You said your name is Hyuk Mujin, the Tenfold Man?”

Hyuk Mujin blinked, then hurriedly bowed his head.

“Y-Yes, Your Highness Prince Shangshan. But I’m sorry to say my title isn’t the Tenfold Man…”

“Come here and sign this.”

“Pardon?”

“No need to refuse. Hyuk Mujin, the Tenfold Man. This shall be an honor passed down through your family for generations.”

“……”

“……”

Hyuk Mujin took the bronze token Prince Zhu Bao handed him and inscribed his new title on it.

Watching him, I thought:

What a fucking mess. Seriously.
```

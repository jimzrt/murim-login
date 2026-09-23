<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0876.txt",
      "sha256": "4704b5f706f7674225838b5a7fe8d8565cf5137ca967bc86a989ce53b65a908a",
      "bytes": 13488
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "f02a86b0de6d83c955def2c10abb1ccaf7f1f0e1ffe377c08cbd5800e0f05275",
      "bytes": 1350
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "77f7f9625d663fdeec408b3696199ba3f21d98f335ae9eae4e9465caec345d0f",
      "bytes": 230213
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "88c2bf07afea1daa7fe2d65f57824fb22fbdac06150d14c878aab935de204981",
      "bytes": 759
    },
    {
      "path": "characters/Hong Jin.md",
      "sha256": "da144102c90a2dd6ba96ad063f64cdd54173aec0a216f3216584dcd5c90a69b2",
      "bytes": 854
    },
    {
      "path": "characters/Human Butcher.md",
      "sha256": "14fc32431d96d6b1ed4eb363294bd5219f03be5959167c0b19157564dcc9a20c",
      "bytes": 667
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "58504cac08bec20f09b9d566dce7277ac18fa93a87b05d9f9228050cee5a8727",
      "bytes": 1378
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "38b04805b9ccf8ef2d8129b91a6cd375fb090c66896d2239bc24b4176557665f",
      "bytes": 1782
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "bfce1b2d5b0f6921ab2390db49ca9e3bca5b8c126462e7c8894aaea7a3f47b66",
      "bytes": 622
    },
    {
      "path": "characters/Jung Ho.md",
      "sha256": "8acbaaa063b67722996819bc96603efd69a7c8fecf37d1eb2c3b97c928f3fff4",
      "bytes": 699
    },
    {
      "path": "characters/Li Feng.md",
      "sha256": "97678c81a072f65fd3b58d3e10cc50f97b88b8fa8347d8303f6ce9b8de5bbd6f",
      "bytes": 888
    },
    {
      "path": "characters/Ma Sanbao.md",
      "sha256": "567b909a02f84a5b30fd5b1c8440e011aff3d5cb508348d2edbde6ea1518f97d",
      "bytes": 765
    },
    {
      "path": "characters/Prince Shangshan.md",
      "sha256": "446b44ffb2939d3a763bc28b9c858d85cb156de64e72fb042abf42421ebdbac3",
      "bytes": 952
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "bfc2115961643976e5e046d021bf671cc7a5855e001e3b3fce5d53858818df23",
      "bytes": 258239
    }
  ],
  "estimated_tokens": 12376
}
-->

# Durable State Update — Chapter 876

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
1 and safe_through 876. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 876. Profile updates may replace only one
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
  "chapter": 876,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 876,
    "continuity_sources": [876],
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
    "Prince Shangshan remains in the imperial capital under the care of palace attendants led by So Gyo; Taekyung gave him the Myriad-Poison Ring for protection against poisoning.",
    "The palace attendants assigned to Shangshan are First Rate martial artists who carry flexible swords.",
    "The Emperor has a concealed Supreme Peak assassin, No Shadow.",
    "Taekyung suspects the Emperor is connected to Dark Heaven, but this is unconfirmed.",
    "Qianqing Palace is defended by mechanisms and formations, at least three Supreme Peak masters, and more than a hundred elite assassins.",
    "Taekyung heard Aehyang’s voice in a restricted part of Qianqing Palace and recognized her as the concubine the City Lord of Sichuan Province lost to the Emperor."
  ],
  "continuity_sources": [
    875
  ],
  "open_questions": [
    "What does the Emperor intend for Shangshan, and what are the palace attendants’ true orders?",
    "What is Aehyang’s situation in the restricted part of Qianqing Palace?",
    "What is the nature of the Emperor’s connection to Dark Heaven?"
  ],
  "safe_through": 875,
  "temporary_decisions": [
    "Render 기관진식 as “mechanisms and formations”; retain “Third Shadow,” “First Shadow,” “No Shadow,” and “Marquis Within the Passes.”"
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 혁무진    | **Hyuk Mujin**     |
| 태원진가   | **Jin Family of Taiyuan**        |
| 화산파    | **Huashan**                      |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 제자     | **Disciple**                                 |
| 전각     | **pavilion**                                 | Use “hall” only when established for a specific named building |
| 시스템              | **System**                     |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 사천     | **Sichuan**            |
| 화산     | **Huashan**            |
| 공자      | **Young Master**                                                |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 홍진 | **Hong Jin** | Level 22 man at the City Lord's luncheon; delicate in appearance and voice. |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 정호 | **Jung Ho** | Middle-aged Shaolin martial monk leading the traveling group. |
| 이풍 | **Li Feng** | Shanxi Province's Assistant Military Commissioner; former Huashan lay disciple |
| 마삼보 | **Ma Sanbao** | The East Depot’s Brush-Holding Eunuch and second-in-command. |
| 상산왕 | **Prince Shangshan** | The City Lord and a member of the imperial family who orders the luncheon. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 성주 | **City Lord** | Official who sends the invitation for a gathering with young prodigies. |
| 도지휘첨사 | **Assistant Military Commissioner** | Military office held by the unnamed official responsible for training soldiers. |
| 도지휘동지 | **Deputy Military Commissioner** | Second-rank military office held by Eunuch Hong |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 선황 | **the late Emperor** | The former Emperor whom Hong Jin served. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 인내 | **Endurance** | System attribute replacing Toughness. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 염라 | **Yama** | Buddhist lord of the underworld invoked as the one awaiting the dead. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 사천성 | **Sichuan Province** | Province form used in the title of its chief official. |
| 사천성주 | **City Lord of Sichuan Province** | Title held by Won Gyun. |
| 염라대왕 | **Yama** | Expanded source form of the established underworld ruler term 염라. |
| 열화신룡 | **Blazing Flame Divine Dragon** | New sobriquet bestowed on Jin Taekyung. |
| 이무기 | **imugi** | Legendary serpent mentioned as the only comparable creature to a Thousand-Year Poison Horned Snake. |
| 동정호 | **Dongting Lake** | Lake under which Dangyang and Honghu Strongholds operated. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 상호 | **Sangho** | Go Se-won's young son. |
| 사냥개 | **hunting dog** | Jin's demeaning metaphor for Ares personnel who obey Go Jun. |
| 화신 | **Fire God** | A local deity worshiped by one Nanman believer. |
| 금의위 | **Embroidered Uniform Guard** | Imperial guard force mentioned by Hong Jin. |
| 동창 | **East Depot** | Imperial agency named by Hong Jin. |
| 건청궁 | **Qianqing Palace** | The Emperor's palace, where Baek Yeon meets him. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 이풍 | 진태경 | senior_official_to_respected_young_martial_artist | Young Hero Jin | formal and respectful | Addresses Taekyung as 진 소협 after praising his reputation. |
| 홍진 | 진태경 | political_host_to_young_martial_artist | Young Hero Jin; Young Master Jin; Sleeping Dragon of Shanxi | polite, coaxing, and probing | Uses respectful forms while steering Taekyung toward relaying the Escort Bureau proposal and teasing him with the Seongun Escort Bureau. |
| 진태경 | 홍진 | young_martial_artist_to_political_official | Comrade Chairman—no, Deputy Military Commissioner | casual and teasing, then formally corrective | Deliberately jokes with an inappropriate title before correcting himself to Hong Jin's official office. |
| 진태경 | 이풍 | junior_to_respected_official_and_martial_ally | Great Hero Li | polite and respectful | Agrees with Li Feng's proposal that Zhu Bao visit the Jin Family's banquet. |
| 사천성주 | 진태경 | official_to_imperial_messenger | Messenger of His Highness Prince Shangshan | formal-deferential | The City Lord addresses Taekyung deferentially after seeing Prince Shangshan's Token. |
| 진태경 | 사천성주 | visitor_to_city_lord | City Lord | sarcastic-polite | Taekyung jokingly praises him as our City Lord after making him fund the reward. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 정호 | 진태경 | Shaolin Discipline Hall Master to patient and Benefactor | Benefactor Jin | formal-polite | Jung Ho repeatedly uses 진 시주 and 시주. |
| 진태경 | 정호 | patient to Shaolin Discipline Hall Master | Monk | polite and familiar | Taekyung addresses Jung Ho as 스님. |
| 혁무진 | 조장님 | pavilion_member_to_squad_leader | Captain | deferential and dubious | Mujin questions whether the pasture should be called the Nanman Ranch instead of the Nanman Beast Palace. |
| 홍진 | 혁무진 | imperial aide addressing a martial artist accompanying the prince | Martial artist Hyuk | polite and conversational | Uses 혁 무인 when asking whether Mujin knows of an exception. |
| 홍진 | 마삼보 | Longtime friend and former East Depot cohort | Ma Constable; Eunuch Ma | Familiar and respectful | Hong uses both forms while acknowledging Ma’s former and current standing. |
| 마삼보 | 홍진 | Longtime friend and former East Depot cohort | Hong Constable | Familiar and respectful | Ma addresses Hong by his former East Depot title. |
| 진태경 | 상산왕 | protector addressing a young prince | His Highness | respectful royal address | Taekyung refers to the prince as 상산왕 전하 when ordering Mujin to bring him. |
| 진태경 | 황제 | guest of the Emperor’s younger brother addressing the Emperor | Your Majesty | formal and deferential in address, despite blunt challenges | Taekyung repeatedly addresses the Emperor as 폐하. |
| 상산왕 | 황제 | younger brother addressing the Emperor | Your Majesty | deferential royal address | Shangshan addresses the Emperor as 폐하 while pleading for Taekyung. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 875
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Hong Jin.md

# Hong Jin (홍진)

- **Safe through:** Chapter 874
- **Aliases:** None
- **Role:** Hong Jin is a Level 22 Deputy Military Commissioner of Shanxi Province, a eunuch and trusted aide to Prince Shangshan, and a former member of the East Depot.
- **Personality:** Composed, socially deft, and ambitious, Hong Jin became a eunuch to escape poverty and save his family, then used his abilities to pursue a broader life.
- **Voice:** Delicate and deferential, using formal, self-effacing language with Prince Shangshan.
- **Relationships:** Hong Jin is devoted to Prince Shangshan, whom the late Emperor entrusted to his care, and trusts Jin Taekyung to help protect him; he left the palace to serve the prince, while his longtime friend and former East Depot cohort Ma Sanbao stayed behind.

### Human Butcher.md

# Human Butcher (인도)

- **Safe through:** Chapter 875
- **Aliases:** None
- **Role:** Former mysterious Han Chinese mounted-bandit power in Northern Gaoyuan commanding fifty subordinates; a Peak master killed by an unnamed old man in a single move
- **Personality:** Cold, intimidating, and murderous; he kills people as though slaughtering livestock
- **Voice:** Cold, curt, and quietly threatening
- **Relationships:** He is one of four powerful participants at the Northern Gaoyuan gathering, intimidates Temur, and has claimed Ghost Sword Wipeng as his personal target in the proposed attack

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 870
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and an active member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented; loyal even when left behind, irreverently self-deprecating, and willing to face danger rather than abandon the person he serves. He is proud, glory-seeking, suspicious of Taekyung, bluntly critical of the family's disgraced third son, and an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad; as a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Fire Dragon Pavilion members accompanying Taekyung. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 873
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader.
- **Personality:** Hungry, self-aware, dryly observant, and pragmatic under pressure; accepts extreme personal risk when duty and the lives of others demand it.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; they trust each other deeply, though their bond remains unformalized. Cheongpung is his trusted companion and only true martial rival; Choi Minwoo is his subordinate and trusted manager of media and official arrangements as well as the Peace Guild's Guild Master; Ju Hwaran is a trusted Fire Dragon Pavilion member; Magic Johnson and Chuck Hagel are allied to him; his mother and sister Hayeon are among those he protects; the Skeleton King is his friend and ally; Xiao Shen regards him as an older brother; Jin-ho is his older friend and trusted confidant; he once saved Ju Wongong’s life.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 873
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Jung Ho.md

# Jung Ho (정호)

- **Safe through:** Chapter 871
- **Aliases:** None
- **Role:** Middle-aged Shaolin martial monk and Master of Shaolin's Discipline Hall who leads the traveling group and wields a Zen staff hung with prayer beads.
- **Personality:** Humble, observant, principled, and concerned with the safety of commoners.
- **Voice:** Formal, restrained, and admonitory, with Buddhist phrasing.
- **Relationships:** Unnamed is his young Martial Uncle; he leads the Shaolin monks traveling with him, addresses Sama Pyo as a Benefactor, and is recognized by Jin Taekyung as Park Jung Ho, a former Garam Middle School classmate.

### Li Feng.md

# Li Feng (이풍)

- **Safe through:** Chapter 858
- **Aliases:** None
- **Role:** Assistant Military Commissioner of Shanxi Province; former Huashan lay disciple who left the sect nearly ten years ago
- **Personality:** Resolute, proud, blunt, and hostile toward political and martial rivals
- **Voice:** Formal and restrained in official settings; dry and cutting with opponents
- **Relationships:** Former lay disciple of Huashan; visited the hidden residence of his Grandmaster Mae Jonghak and saw ten-year-old Cheongpung there; recognizes Cheongpung as his Martial Uncle; direct subordinate and political rival of Hong Jin, the Deputy Military Commissioner; agrees to act as Hong Jin's intermediary with Huashan and send a messenger pigeon to his Master; bears a humiliating martial grievance involving Gong Ilhyuk

### Ma Sanbao.md

# Ma Sanbao (마삼보)

- **Safe through:** Chapter 874
- **Aliases:** None
- **Role:** Ma Sanbao is the East Depot’s Brush-Holding Eunuch and second-in-command, a Supreme Peak martial artist who has secretly remained in the imperial palace.
- **Personality:** He is vigilant and patient, concealing his loyalties while awaiting the moment to act for the late Emperor.
- **Voice:** He speaks casually and directly with longtime companions, while remaining alert and controlled with new acquaintances.
- **Relationships:** Ma Sanbao is a longtime friend and former East Depot cohort of Hong Jin; he stayed behind to await Prince Shangshan's return and is leading a group seeking to enthrone him.

### Prince Shangshan.md

# Prince Shangshan (상산왕)

- **Safe through:** Chapter 875
- **Aliases:** None
- **Role:** Prince Shangshan, whose personal name is Zhu Bao, is the Emperor’s twelve-year-old youngest younger brother and an exceptionally skilled young swordsman.
- **Personality:** Earnest and compassionate, he takes responsibility for his loyal subjects’ hardship, admires Jin Taekyung, seeks candid counsel, and shows composure beyond his years in the face of death and political danger.
- **Voice:** Archaic and formal in the manner of a historical drama, with openly eager and childlike reactions beneath his royal diction.
- **Relationships:** Prince Shangshan Zhu Bao is the Emperor’s youngest younger brother; the late Emperor entrusted Hong Jin with his care. Zhu Bao admires Jin Taekyung, seeks to emulate him, and calls him a friend; the Emperor says he will take care of Zhu Bao.

## Korean source

```text
＃876화



홍진은 앞을 가로막은 황금빛 갑옷들을 지그시 노려보았다.

언제나 여인의 그것처럼 높고 나긋나긋하던 목소리는 전에 들어본 적 없을 만큼 낮게 가라앉아 있었다.

“비켜라.”

“불가(不可). 그대는 이곳에서 한 걸음도 벗어날 수 없소.”

“비키라고 했다.”

“이보시오! 도지휘동지!”

“정말 나를 막을 수 있으리라 생각하느냐? 네놈들 따위가 감히?”

“……!”

수십여 명의 금의위가 얼굴을 굳힌 채 서로를 바라보았다.

그들도 이미 알고 있었다. 눈앞의 환관이 결코 호락호락한 인물이 아니라는 것쯤은.

아무리 높은 권세라도 십 년을 가지 못하고, 열흘 붉은 꽃이 없다지만 과거 선황의 총애를 듬뿍 받았던 동창 첩형(貼刑)이라면 이야기가 달라진다.

게다가 조정에는 아직 적지 않은 수의 노신(老臣)들이 남아 있었고, 홍진은 그들과 묵은 인연이 있을 것이 분명했다.

그것이 함께 선황을 모셨던 신하로서의 우정인지, 동창을 쥐락펴락하던 실력자로서 잡아챈 약점인지는 모르겠으나 적어도 한 가지만큼은 확실했다.

그가 지닌 영향력을 쉽게 볼 수 없다는 것.

“황궁을 떠난 지 십 년이 넘었어도, 말단 금의위 위사쯤은 서신 몇 통이면 변방에 처박아 버릴 수 있다. 그러니 썩 꺼져. 앞으로도 그 번쩍이는 갑옷을 걸치고 싶다면.”

홍진의 두 눈동자에 차가운 불꽃이 일렁였다.

어린 주군이 황제를 알현하기 위해 떠난 지 어언 두 시진.

동창 내에서도 냉철하기로 이름 높았던 환관의 인내심은 벌써 밑바닥을 드러내고 있었다.

‘이렇게 될 줄 알았다면, 무슨 수를 써서라도 동행했어야 했는데.’

무슨 일이 생긴 것이 분명하다.

자꾸만 고개를 드는 불안감을 애써 억눌러 보지만, 그조차도 더 이상은 쉽지 않은 상황.

홍진이 자신도 모르게 입술을 질끈 깨문 그때였다.

“다들 진정하십쇼, 진정.”

불쑥 들려온 넉살 좋은 목소리. 자연스럽게 홍진의 앞을 가로막은 혁무진이 금의위들을 향해 손사래를 쳤다.

“넓은 아량으로 이해하시오. 너무 늦어지니까 걱정이 돼서 그래.”

“이보세요. 혁 무인!”

“아이고, 홍 동지님도 고정하세요. 저 사람들이 무슨 죕니까? 우리 같은 아랫것들이야 까라면 까고, 짖으라면 짖는 것뿐인데. 안 그래요?”

편을 들어 주는 건지, 면전에 대고 개새끼라고 하는 건지 당최 헷갈리게 만드는 말에 금의위들이 눈살을 찌푸리던 그때. 혁무진은 생각할 틈도 주지 않고 빠르게 말을 이었다.

“그래도 상황이 어떻게 돌아가는지 정도는 확인 좀 해 줘요. 가뜩이나 피곤한 마당에 빡빡하게 굴면 피차 재미없잖아. 안 그래?”

“잠깐. 그건…….”

“아, 확인해 준다고? 이야! 역시 금의위! 대국의 자존심! 황실의 수호자들! 거 존나게 고맙소! 나중에 시간 나면 황도 중심가에 있는 혁가 포목점에 한 번 들러요. 내 이름 대면 좀 싸게 살 수 있을 거야.”

뭐라 대꾸할 틈도 없었다. 금의위들의 대답을 기다리지도 않고 후다닥 돌아선 혁무진은 홍진을 붙잡고 물러났다.

한껏 숨죽인 속삭임과 함께.

“지금 쟤들 건드려 봐야 좋을 것 없습니다. 알 만큼 아는 분이 왜 그러십니까? 평정심을 좀 되찾으세요.”

그 한마디로 마음속 불안감이 완전히 사라지지는 않았지만, 홍진이 잠시 잊고 있던 현실을 깨닫게 하기에는 충분했다.

혁무진의 말은 사실이었다.

아직 조정에 남아 있는 자신의 영향력을 이용해서 몇몇 권력자들을 움직여 봤자, 기껏해야 사냥개 몇 마리 내치는 것뿐.

몸통이나 머리는 건드려 보지도 못할 테고, 사냥개들의 목줄을 쥔 주인까지는 언감생심 꿈도 꿀 수 없다.

지금은 발톱을 숨기고, 이빨을 감춰야 할 때였다.

물론 차갑게 식은 머리와 달리 가슴은 여전히 거세게 요동치고 있었지만.

“혁 무인은 걱정도 안 되나요?”

불현듯 흘러나온 홍진의 물음에, 혁무진이 고개를 갸웃거렸다.

“예? 뭘 말입니까?”

“당신이 상산왕 전하께 별다른 충성심이 없다는 것쯤은 알아요. 무림인의 생리가 그러하니 그것에 대해 비난할 생각도 없고요. 하지만…….”

“아, 함께 가신 조장님이 어찌 되셨는지 걱정도 안 되냐. 뭐 그런 말씀이십니까?”

홍진이 힘없이 고개를 끄덕이자 혁무진이 즉각 대답했다.

“걱정이야 당연히 하죠. 합니다.”

“그런데 어떻게 그리 태평해요?”

“이게 최선이니까요.”

“네?”

“제가 지금까지 조장님 뒤꽁무니 따라다니면서 별의별 일들을 다 겪었는데…… 조장님께서 직접 움직여서 해결 안 된 일은 없습니다.”

“……!”

“일이 얼마나 더럽게 꼬이든 간에, 마지막 결과만 보면 결국 조장님이 싹 다 쓸어 버렸어요. 앞에서 고수입네, 내가 흑막입네, 하고 깐죽거리던 새끼들은 싹 다 염라대왕이랑 면접 보러 갔고요.”

눈을 부릅뜬 홍진을 바라보며, 혁무진은 태연한 목소리로 말을 이었다.

“딱 까놓고 말해서, 저는 지금까지 조장님만큼 강한 사람을 본 적이 없습니다. 정말 미치도록 강해요.”

“혁 무인, 미안하지만 이것만큼은 냉정하게 말할게요. 황궁은 그야말로 살아 있는 괴물이나 다름없어요. 진 공자가 제아무리 초절정 고수라고 해도…….”

“전 무공만을 말한 게 아닌데요.”

“……?”

“무공이 아니라 사람. 그냥 사람 자체가 강합니다. 조장님은 그런 사람이에요.”

“……!”

“설령 황궁에 한 수, 두 수 위의 고수들이 득실거려도 조장님은 못 당합니다. 이게 도저히 말이 안 되는 거긴 한데, 제가 아는 조장님은 지금까지 늘 그랬어요.”

“……그게 말이 되나요?”

“원래는 안 되는데, 되더라고요. 그러니까 홍 동지께서도 우리 조장님께 상산왕 전하를 부탁한 거 아닙니까?”

순간 말문이 막혀 버린 홍진은 불현듯 깨달았다.

처음 마삼보에게서 금의위가 움직였다는 밀서를 받았을 때. 어째서 진태경이라는 이름이 가장 먼저 떠올랐는지.

서로 간의 신뢰?

물론 중요하다. 하지만 단순히 신뢰만을 따졌더라면 화산파의 속가제자이자 산서성 도지휘첨사인 이풍을 데려왔을 것이다.

홍진 자신과는 잠시나마 대립각을 세우긴 했어도, 벌써 수년이 넘는 시간 동안 끈 떨어진 연이나 다름없는 상산왕을 향해 변함없는 충성심을 바쳐 온 그였으니.

그런 이풍에 비하면 진태경과의 관계는…… 상호 간의 신뢰라 칭하기에는 조금 민망한 감이 있다.

그의 가문인 태원진가와 제법 끈끈한 사업적 관계를 맺고 있는 것은 사실이었지만.

그런데 왜?

왜 자신은 진태경을 청했을까. 이미 입증된 충신, 혹은 또 다른 무림의 고수를 초빙할 수 있었음에도.

그 의문에 대한 답을, 홍진은 이미 알고 있었다.

“혁 무인 말이 맞아요. 내가 멍청하게도 잠시 잊고 있었어. 감정적으로 흐트러진 탓이겠지.”

언제 그랬냐는 듯 침착함을 되찾은 홍진의 모습에, 혁무진이 씩 웃어 보였다.

“충분히 이해합니다. 그럴 수 있죠.”

“진 공자는…… 그래, 확실히 불가사의한 사람이야. 내가 전해 들은 이야기만 해도 믿을 수 없는 것들이 대부분이었지. 물론 그중에서도 힘들게 입수한 어떤 정보들은 헛소문이 분명하겠지만.”

“헛소문이요? 그 정보가 어떤 겁니까?”

“아, 그거?”

홍진이 피식 웃기까지 하며 대답했다.

“들으면 혁 무인도 배꼽을 잡고 웃을걸. 글쎄 진 공자가 동정호에서 용을 잡았다는 헛소리를 늘어놓더라고.”

“확실히 헛소문이네요. 용이라기보단 이무기였는데.”

“역시 그렇지? 천금(千金)이나 주고 구한 정보였는데, 어디서 그따위 말도 안 되는…….”

웃으며 말을 잇던 홍진이 문득 입을 다물었다.

그리고 숨 막히는 침묵 끝에 간신히 목소리를 쥐어 짜냈다.

“지금, 뭐라고?”

“예? 뭐가 말입니까?”

“아니 방금, 방금 전에 용이 아니라…….”

“아. 이무기요. 그거 맞습니다. 저도 그 자리에 있었거든요. 처음엔 단순히 꿈을 꾸나 했는데 시간이 지나고 보니까 아니더라고요. 뭐 그래도 하늘을 날아다니지는 않았으니 용이 아니라 이무기였던 건 확실합니다.”

“……?”

“그런데 그 정보, 어떤 호로새끼가 넘긴 겁니까? 정말 극비리에 조용히 처리된 일일 텐데.”

“……!”

마치 시간이 정지한 듯한 충격 속에서, 홍진은 깨달았다.

앞서 혁무진이 했던 모든 말들은, 정말 한 치의 거짓도 없는 진실이었다는 것을.

진태경을 선택한 것은 정말이지 신의 한 수였다는 사실을.

‘이무기? 이무기를 잡아? 사람이 이무기를? 아니, 이무기가 실제로 있었단 말인가?’

충격이 얼마나 컸던지, 이 순간만큼은 잠시나마 어린 왕에 대한 걱정마저 잊어버릴 정도였다.

그리고 멍하니 입을 벌린 채 굳어 버린 홍진에게, 한참 동안 호사가를 욕하던 혁무진이 조심스럽게 입을 연 그때였다.

“저기, 혹시 천금 한 번 더 쓰실 용의 있으십니까? 다름이 아니라 제가 이번에 남만에 갔다가 말하는 호랑이를 봤는데…….”

“비켜!”

공력이 실린, 더없이 익숙한 목소리로 터져 나온 외침.

번개처럼 고개를 돌려 그 목소리의 주인을 확인한 홍진의 눈은 화등잔만 하게 커졌고, 은밀한 거래를 시도하던 혁무진은 반사적으로 외쳤다.

“죄송합니다! 살려 주십시오! 저는 아무 말도 안 했습니다! 조장님이 보우하사, 태원진가 만세!”

“저 왔습니다. 드릴 말씀이 있으니 어서 안으로…… 혁무진 이 새끼 뭐야. 얘 도대체 왜 이래요?”

말하는 호랑이에 대해 알려 주려던 홍진은 가슴이 덜컥 내려앉는 것을 느꼈다.

‘전하께서는 어디에…….’

아무리 고개를 돌려도 보이지 않는다.

자신의 어린 왕. 대국의 마지막 희망이.

몇 번이나 소매로 눈을 문질러도 이곳을 향해 돌아오는 이는 단 한 사람뿐이었다.

열화신룡 진태경.

‘기어이.’

일이 생긴 것이 틀림없다. 저 잔혹한 황제의 마수(魔手)가 마침내 자신의 주군에게까지 닿았다.

그러나 홍진은 눈앞이 희뿌옇게 물드는 것을 애써 참아냈다.

아직 끝나지 않았다. 분명 저 젊은 무림인은 무언가 방법을 찾아냈을 것이다.

그리고 그런 홍진의 바람에 답하듯, 철탑처럼 버티고 선 금의위들을 어깨빵으로 반쯤 날려 버리다시피 한 진태경이 입술을 달싹였다.

- 전각으로 들어가세요. 지금 당장!

물론 그 짧은 틈을 타, 하나뿐인 충복의 뒤통수를 후려갈기는 것도 잊지 않았다.

“무사히 다녀오셨…….”

빡!

“억!”

“그래, 잘 다녀왔다. 이 새끼야.”



* * *



전각으로 복귀한 나는 공력으로 든든하게 방음 시스템을 갖춘 뒤, 빠르게 말을 쏟아냈다.

최대한 간략하게, 핵심만 담아서.

첫째. 황제가 상산왕을 보호한다는 명목하에 건청궁에 가둠.

둘째. 황제 새끼 노양심. 별주부전 토끼가 간 빼놓고 다녔던 것처럼 양심이라는 걸 다른 곳에 숨겨 놓고 사는 것 같음. 아, 초절정 고수고 엄청 겉늙었음.

셋째. 몇 달 전 황제가 사천성주에게 빼앗은 애첩이 건청궁에 있는 것 같음.

그렇게 눈깔과 마우스 스크롤을 장식쯤으로 여기는 21세기 요약충들도 합격을 외칠 만한 성공적인 썰풀기가 끝난 직후. 시시각각 표정이 뒤바뀌던 홍진의 얼굴에는 숨길 수 없는 경악만이 남아 있었다.

“사천성주의 애첩이…… 건청궁에 머무르고 있단 말입니까?”

“예. 거의 확실합니다. 그런데 제 나름대로 결론을 내리기 전에 꼭 여쭤볼 것이 있어서요.”

크게 심호흡한 내가 재차 입을 열었다.

“보통 황후나 후궁들이, 건청궁에 머무르는 게 일반적입니까?”

“전혀 아닙니다.”

“황제가 아끼는 후궁이라고 해도?”

“전혀요. 황실의 법도는 지엄합니다.”

“그렇다면…….”

“맞아요. 그것뿐이네요.”

나와 홍진의 시선이 허공에서 맞닥트렸다. 그리고 다음 순간, 동시에 입술이 열렸다.

“임신.”

“회임(懷妊).”

시발.

아무래도 황제는, 상산왕을 대신할 대국의 새로운 후계자를 찾은 모양이다.
```

## Final English reading copy

```markdown
# Chapter 876

Hong Jin fixed a cold stare on the golden armor blocking his way.

His voice, usually high and gentle as a woman’s, had sunk lower than anyone had ever heard it.

“Move.”

“Impossible. You cannot take a single step beyond this place.”

“I said move.”

“Sir! Deputy Military Commissioner!”

“Do you really think you can stop me? You lot dare?”

“……!”

The dozens of Embroidered Uniform Guards looked at one another, their faces stiff.

They already knew the eunuch standing before them was no pushover.

They said no matter how high you climbed, power never lasted ten years, and no flower stayed red for ten days. But things were different when you were talking about the East Depot’s former Investigating Eunuch, who had once enjoyed the late Emperor’s favor.

Besides, plenty of old officials still remained at court, and Hong Jin had surely built up ties with them over the years.

Whether those ties were friendships forged as fellow servants of the late Emperor or secrets he’d seized as a power broker who’d once controlled the East Depot, no one could say. But one thing was certain.

His influence was not to be underestimated.

“Even after more than ten years away from the palace, a few letters are enough to send a low-ranking Embroidered Uniform Guard stationed here to the borderlands. So get the hell out of my way, if you want to keep wearing that shiny armor.”

A cold flame flickered in Hong Jin’s eyes.

Around four hours had passed since his young lord left to meet the Emperor.

The eunuch, renowned even within the East Depot for his cool head, was already at the end of his patience.

*If I’d known it would come to this, I should’ve done whatever it took to go with him.*

Something had clearly happened.

He tried to suppress the unease that kept rising inside him, but he was finding it harder and harder to do so.

Just as Hong Jin bit down hard on his lip without realizing it—

“Everyone, calm down. Take it easy.”

A breezy voice cut in out of nowhere. Hyuk Mujin stepped in front of Hong Jin and waved the Embroidered Uniform Guards down.

“Try to be understanding. It’s taking a while, so he’s worried.”

“Martial artist Hyuk!”

“Come now, Comrade Hong, you should calm down too. What did these people do wrong? We underlings do what we’re told, whether they say ‘get down’ or ‘bark.’ Right?”

The Embroidered Uniform Guards frowned, unsure whether he was taking their side or calling them sons of bitches to their faces. Hyuk Mujin didn’t give them time to think it over before continuing.

“Still, could you at least find out what’s going on? We’re all exhausted as it is. If you make this difficult, nobody’s going to have a good time. Right?”

“Wait. That’s…”

“Oh, you’ll check? Wow! The Embroidered Uniform Guard! The pride of the Great Nation! The guardians of the imperial family! Thanks a fucking lot! If you get the time, drop by the Hyuk Family Textile Shop in the center of the imperial capital. Give them my name and you can get a discount.”

There was no chance to reply. Without waiting for the guards’ answer, Hyuk Mujin quickly turned around, grabbed Hong Jin, and backed away.

He spoke in a low whisper.

“There’s nothing to gain by provoking them right now. You know better than most, so why are you doing this? Get a grip.”

Those words didn’t make the unease in Hong Jin’s heart disappear, but they were enough to make him remember something he’d briefly forgotten.

Hyuk Mujin was right.

If he used his remaining influence at court to move a few powerful figures, all he’d manage to do was get rid of a few hunting dogs.

He wouldn’t touch the body, let alone the head. And reaching the owner holding the hunting dogs’ leashes was out of the question.

Now was the time to hide his claws and sheath his fangs.

Of course, while his head had cooled, his heart was still pounding wildly.

“Aren’t you worried, Martial artist Hyuk?”

At Hong Jin’s sudden question, Hyuk Mujin tilted his head.

“Sorry? About what?”

“You don’t feel any particular loyalty toward His Highness Prince Shangshan. I know that. It’s the nature of martial artists, so I have no intention of criticizing you for it. But…”

“Oh, you mean I’m not worried about what happened to the Captain who went with him?”

Hong Jin nodded weakly, and Hyuk Mujin answered at once.

“Of course I’m worried. I am.”

“Then how can you be so calm?”

“This is the best I can do.”

“What?”

“I’ve been following the Captain around and going through all kinds of things with him. There’s never been a problem he couldn’t solve by getting involved himself.”

“……!”

“No matter how badly things got twisted, in the end, the Captain swept everything away. All those bastards who strutted around bragging about being masters or the masterminds behind it all went off to interview with Yama.”

Hyuk Mujin looked at Hong Jin’s wide eyes and continued in an unruffled voice.

“To be perfectly honest, I’ve never met anyone as strong as the Captain. He’s insanely strong.”

“Martial artist Hyuk, I’m sorry, but I’ll be blunt about this. The imperial palace is practically a living monster. No matter how skilled a Supreme Peak master Young Master Jin is…”

“I wasn’t just talking about martial arts.”

“……?”

“Not his martial arts. The man himself. He’s just a strong person, period. That’s the kind of person the Captain is.”

“……!”

“Even if the palace is crawling with masters a level or two above him, they still won’t be able to handle the Captain. It makes no sense at all, but that’s how the Captain I know has always been.”

“Does that make any sense?”

“It shouldn’t, but somehow it does. Isn’t that why you asked our Captain to look after His Highness Prince Shangshan?”

Hong Jin was struck speechless. Then he suddenly understood.

When he’d first received a secret letter from Ma Sanbao saying the Embroidered Uniform Guard was on the move, why had Jin Taekyung been the first person to come to mind?

Trust between them?

Of course that mattered. But if trust alone had been the deciding factor, he would have brought Li Feng, a lay disciple of Huashan and the Assistant Military Commissioner of Shanxi Province.

Even though Li Feng and Hong Jin had briefly been at odds, Li Feng had spent years offering unwavering loyalty to Prince Shangshan, who’d long been left with no support.

Compared to that, Hong Jin’s relationship with Jin Taekyung… calling it mutual trust was a little embarrassing.

It was true that he had a fairly close business relationship with the Jin Family of Taiyuan.

But why?

Why had he asked for Jin Taekyung, when he could have brought along a proven loyalist or another master from the martial world?

Hong Jin already knew the answer.

“You’re right, Martial artist Hyuk. I’d foolishly forgotten for a moment. I must have let my emotions get the better of me.”

Seeing Hong Jin regain his composure as if nothing had happened, Hyuk Mujin grinned.

“I understand. It happens.”

“Young Master Jin… yes, he really is an unfathomable person. Most of what I’ve heard about him is hard to believe. Of course, some of the information I went to great trouble to obtain must be nonsense.”

“Nonsense? What information?”

“Oh, that?”

Hong Jin answered with a little laugh.

“You’d laugh your head off if you heard it, too, Martial artist Hyuk. Apparently, Young Master Jin caught a dragon in Dongting Lake.”

“That’s definitely a rumor. It was more of an imugi than a dragon.”

“Thought so. I paid a thousand gold pieces for that information, and this is the kind of ridiculous…”

Hong Jin stopped mid-sentence.

After a breathless silence, he finally managed to squeeze out a few words.

“What did you just say?”

“Huh? What do you mean?”

“No, just now. You said it wasn’t a dragon…”

“Oh. An imugi. That’s right. I was there, too. At first I thought I was dreaming, but after a while I realized it wasn’t a dream. Well, it didn’t fly through the sky, so it definitely wasn’t a dragon—it was an imugi.”

“……?”

“By the way, what piece of shit leaked that information? That was supposed to have been handled quietly, under the strictest secrecy.”

“……!”

Still reeling as if time had stopped, Hong Jin realized that everything Hyuk Mujin had said earlier had been true—every last word.

Choosing Jin Taekyung really had been a stroke of genius.

*An imugi? He caught an imugi? A person caught an imugi? Wait, those things actually exist?*

The shock was so great that, for a moment, he even forgot to worry about the young prince.

Just as Hong Jin stood frozen with his mouth hanging open, Hyuk Mujin, who’d been cursing the rumor-monger for some time, cautiously spoke up.

“Um, would you be willing to spend another thousand gold pieces? I saw a talking tiger when I went to Nanman recently…”

“Move!”

A shout rang out, carried on internal energy. It was a voice Hong Jin knew all too well.

Hong Jin whipped his head around. His eyes widened like saucers when he saw who it was, while Hyuk Mujin, who’d been trying to strike a quiet deal, cried out on instinct.

“I’m sorry! Please spare me! I didn’t say anything! May the Captain protect me—long live the Jin Family of Taiyuan!”

“I’m back. I have something to tell you, so let’s get inside… Hyuk Mujin, you little shit, what’s wrong with you? Why is he acting like that?”

Hong Jin had been about to tell him about the talking tiger, but his heart sank.

*Where is His Highness…?*

No matter how many times he looked around, he couldn’t see him.

His young lord. The Great Nation’s last hope.

Hong Jin rubbed his eyes with his sleeve again and again, but only one person came back toward him.

Jin Taekyung, the Blazing Flame Divine Dragon.

*So it’s come to this.*

Something had definitely happened. That cruel Emperor’s hand had finally reached his lord.

But Hong Jin forced himself to hold back the haze gathering before his eyes.

It wasn’t over yet. Surely that young martial artist had found some way out.

And as if to answer Hong Jin’s hopes, Jin Taekyung—who’d nearly knocked the Embroidered Uniform Guards, standing firm as iron towers, flying with a shoulder-check—moved his lips.

“Get inside the pavilion. Right now!”

Of course, he didn’t forget to smack his one loyal subordinate on the back of the head as he passed.

“Glad you returned safely…”

Whack!

“Ow!”

“Yeah, I’m back safe and sound, you little shit.”

* * *

After returning to the pavilion, I used my internal energy to soundproof the place, then quickly laid out what had happened.

As briefly as possible, just the essentials.

First. The Emperor had locked Prince Shangshan inside Qianqing Palace under the pretext of protecting him.

Second. That Emperor was shameless as hell. Like the rabbit in the old folktale who left his liver behind, he seemed to keep his conscience hidden somewhere else. Oh, and he was a Supreme Peak master who looked way older than he was.

Third. It seemed like the beloved concubine the Emperor had taken from the City Lord of Sichuan Province a few months ago was in Qianqing Palace.

My summary was over—successful enough that even a twenty-first-century summary junkie, who treated their eyes and the scroll wheel as mere decorations, would’ve given it a passing grade. Hong Jin’s expression had changed with every sentence; now all that remained was unconcealable shock.

“The City Lord of Sichuan Province’s concubine… is staying in Qianqing Palace?”

“Yes. Almost certainly. But before I draw my own conclusions, there’s something I need to ask you.”

I took a deep breath and asked again.

“Is it normal for the Empress or the imperial consorts to stay in Qianqing Palace?”

“Not at all.”

“Even a consort the Emperor favors?”

“Not at all. The rules of the imperial family are strict.”

“Then…”

“That’s right. There’s only one explanation.”

Hong Jin and I met eyes. The next moment, we spoke at the same time.

“Pregnant.”

“With child.”

Fuck.

The Emperor seemed to have found a new heir for the Great Nation to replace Prince Shangshan.
```

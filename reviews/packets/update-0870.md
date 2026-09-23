<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0870.txt",
      "sha256": "4419e6176ed9a24ee58beb73574afedfb035b0923bdeee022f2ef71b9fdf55d4",
      "bytes": 13252
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "5011d4c2a68ef026d571c78e5c8c3f184f32a920669102e337d520e0afb57615",
      "bytes": 2106
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "c6aa7ac66627729312c888562b57669d8c199736b3a54a323fd416b739461b8d",
      "bytes": 229550
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "137f4bc0ae1a526b04830c96c77483c2cf386b8f707d3ec933891ec3db10a27a",
      "bytes": 759
    },
    {
      "path": "characters/Hong Jin.md",
      "sha256": "71e1277d1b24b64fa97a80cc8a21e941bc06efb7674bba0692df10dd5a5a7f2c",
      "bytes": 854
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "d1c31d5cf33fcf795752cebbb71f3220cc096bf577d992312419e834cf2ed045",
      "bytes": 1378
    },
    {
      "path": "characters/Jeong Hogun.md",
      "sha256": "032fbfe8e71f8fa39043dd0f27c37a2a099704eea7ac73083bd9c3130545776c",
      "bytes": 771
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "c7318092527235df685c3b9e0739fa0b4ae22d0091f3b35ceb42bffb0820e9ae",
      "bytes": 1782
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "234f63287b0daa789542e6acbe0d76acb97a7e978f58d8e6f29f2f597872469f",
      "bytes": 622
    },
    {
      "path": "characters/Jung Ho.md",
      "sha256": "b9f4c09de1205a28c7ff3b726211ec52e84bfb2e7a1879cdac2668c4ca718131",
      "bytes": 699
    },
    {
      "path": "characters/Ma Sanbao.md",
      "sha256": "d20faddb209e6952879f6ec53d9bb9481e4f1d1ef8361f35a9a7d7a7f05079ec",
      "bytes": 765
    },
    {
      "path": "characters/Prince Shangshan.md",
      "sha256": "02facd106eb0e97d8cef8fad26b05c4554553c74a990f606c56d3d217e8e4daf",
      "bytes": 920
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "78f2a30d7157188be2aadbb18e2e9d210a30a8f5d3d7b635d5d58939f6cbf55e",
      "bytes": 256919
    }
  ],
  "estimated_tokens": 12223
}
-->

# Durable State Update — Chapter 870

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
1 and safe_through 870. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 870. Profile updates may replace only one
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
  "chapter": 870,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 870,
    "continuity_sources": [870],
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
    "The Emperor has summoned Prince Shangshan and Jin Taekyung for an audience; Hong Jin is not permitted to accompany them.",
    "Jeong Hogun says three red lanterns lit from the hour of the Ox to the hour of the Tiger match an East Depot secret signal. Taekyung recognizes the timing of Ma Sanbao’s visit, suspects a trap, and denies knowledge of the East Depot.",
    "Prince Shangshan’s party remains under Embroidered Uniform Guard surveillance; Baek Yeon previously promised Taekyung that the guards would cause them no harm.",
    "Ma Sanbao secretly remained in the palace, loyal to the late Emperor and leading a group that seeks to enthrone Prince Shangshan; Hong Jin left the East Depot to serve the prince, while Ma stayed behind.",
    "Ma Sanbao says he knows much about Dark Heaven and offers a reward for helping enthrone Shangshan; Taekyung suspects the reward may be imperial support for the Murim Alliance against Dark Heaven.",
    "Taekyung has not decided whether to join Ma Sanbao’s plan and fears the consequences of failure.",
    "The Emperor is the fourth prince who seized the throne in a bloody coup and purge; Ma Sanbao says tens of thousands died, including many uninvolved in the struggle.",
    "The Emperor relies on opium, which he calls medicine, and broke his pipe to clear his mind."
  ],
  "continuity_sources": [
    868,
    869
  ],
  "open_questions": [
    "Will Taekyung agree to help enthrone Prince Shangshan, and what would the plan require?",
    "What does Ma Sanbao know about Dark Heaven, and what reward is he offering?",
    "What does the Emperor intend for Prince Shangshan and Taekyung?",
    "Who sent the assassin to Qianqing Palace, and what was the intended target?",
    "What happened between Hong Jin and the former East Depot Director?"
  ],
  "safe_through": 869,
  "temporary_decisions": [
    "Render 밀마 as “secret signal” in this chapter’s context.",
    "Render 창공 as “Director” for the East Depot’s head.",
    "Render 연판장 as “blood-signed pact.”"
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 혁무진    | **Hyuk Mujin**     |
| 태원진가   | **Jin Family of Taiyuan**        |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 강호     | **martial world**                                | Prefer “Murim” where the setting itself is meant      |
| 전각     | **pavilion**                                 | Use “hall” only when established for a specific named building |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 레벨               | **Level**                      |
| 경험치              | **EXP**                        |
| 로그아웃             | **Logout**                     |
| 태원     | **Taiyuan**            |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 홍진 | **Hong Jin** | Level 22 man at the City Lord's luncheon; delicate in appearance and voice. |
| 정호군 | **Jeong Hogun** | Commander of the Embroidered Uniform Guard force confronting Jin. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 정호 | **Jung Ho** | Middle-aged Shaolin martial monk leading the traveling group. |
| 마삼보 | **Ma Sanbao** | The East Depot’s Brush-Holding Eunuch and second-in-command. |
| 상산왕 | **Prince Shangshan** | The City Lord and a member of the imperial family who orders the luncheon. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 천자 | **Son of Heaven** | Honorific title for the Emperor. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 주표 | **Zhu Bao** | Personal name of Prince Shangshan. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 화룡갑 | **Fire Dragon Armor** | Jin Taekyung's renamed bound armor, formerly the Black Dragon Armor. |
| 단환 | **pill** | A martial elixir in pill form; Mungyeong gives Taekyung a custom-made one. |
| 복마전 | **demon-slaying battleground** | A possible description for Sichuan if Dark Heaven attacks it. |
| 성하 | **Seongha** | Hunter named during the cave battle. |
| 제니 | **Jenny** | East Asian news anchor interviewing Jacob. |
| 인벤토리 | **Inventory** | System storage summoned by Jin. |
| 황족 | **Huang tribe** | Nanman tribe involved in a recently settled dispute. |
| 궁인 | **palace attendant** | Former Inner Palace attendant expelled by Baeksang. |
| 신병이기 | **divine weapon** | Jin's description of White Flame. |
| 자금성 | **Forbidden City** | Chinese landmark engulfed in flames. |
| 금의위 | **Embroidered Uniform Guard** | Imperial guard force mentioned by Hong Jin. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 관리 | 진태경 | official_to_young_martial_artist | Young Master | formal-polite | The official addresses Taekyung as 공자 while explaining the consequences of Prince Shangshan's displeasure. |
| 홍진 | 주표 | servant and political aide to prince | His Highness | formal-deferential | Uses the elongated royal call 전하 while summoning Zhu Bao. |
| 진태경 | 주표 | visitor to prince | His Highness, Prince Shangshan | formal-deferential | Addresses Zhu Bao as 상산왕 전하 after kneeling to meet his gaze. |
| 주표 | 진태경 | prince to visiting young hero | Jin Taekyung | formal and inquisitive | Uses the formal second-person address before asking Taekyung's name and requesting an autograph. |
| 홍진 | 진태경 | political_host_to_young_martial_artist | Young Hero Jin; Young Master Jin; Sleeping Dragon of Shanxi | polite, coaxing, and probing | Uses respectful forms while steering Taekyung toward relaying the Escort Bureau proposal and teasing him with the Seongun Escort Bureau. |
| 진태경 | 홍진 | young_martial_artist_to_political_official | Comrade Chairman—no, Deputy Military Commissioner | casual and teasing, then formally corrective | Deliberately jokes with an inappropriate title before correcting himself to Hong Jin's official office. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 중년인 | 진태경 | veteran civilian Hunter to celebrated allied Hunter | Mr. Jin | formal-polite and awed | The casualty clerk addresses Jin as 진 선생님 after Jin asks him to list Lei Fei among the dead. |
| 진태경 | 중년인 | celebrated Hunter to older fellow Hunter | sir | casual and teasing | Jin addresses the older Hunter as 아저씨 while joking with him and giving him instructions. |
| 정호 | 진태경 | Shaolin Discipline Hall Master to patient and Benefactor | Benefactor Jin | formal-polite | Jung Ho repeatedly uses 진 시주 and 시주. |
| 진태경 | 정호 | patient to Shaolin Discipline Hall Master | Monk | polite and familiar | Taekyung addresses Jung Ho as 스님. |
| 주표 | 홍진 | prince to loyal subject | you | formal and reassuring | Zhu Bao refers to Hong Jin as 그대 while apologizing for the hardship he has endured. |
| 진태경 | 정호군 | young martial artist to senior imperial officer | Commander Jeong | casual and teasing, then conciliatory | Jin addresses him by rank while trying to defuse the standoff. |
| 주표 | 혁무진 | prince_to_subordinate_of_his_companion | Tenfold Man Hyuk Mujin | formal and playful | Zhu Bao takes Mujin’s boast literally and grants him the title. |
| 홍진 | 혁무진 | imperial aide addressing a martial artist accompanying the prince | Martial artist Hyuk | polite and conversational | Uses 혁 무인 when asking whether Mujin knows of an exception. |
| 홍진 | 마삼보 | Longtime friend and former East Depot cohort | Ma Constable; Eunuch Ma | Familiar and respectful | Hong uses both forms while acknowledging Ma’s former and current standing. |
| 마삼보 | 홍진 | Longtime friend and former East Depot cohort | Hong Constable | Familiar and respectful | Ma addresses Hong by his former East Depot title. |
| 진태경 | 상산왕 | protector addressing a young prince | His Highness | respectful royal address | Taekyung refers to the prince as 상산왕 전하 when ordering Mujin to bring him. |
| 정호군 | 상산왕 | imperial guard officer escorting the prince | His Highness | formal and deferential | Hogun formally reports that he has come to escort the prince. |
| 정호군 | 홍진 | Embroided Uniform Guard officer addressing a senior imperial official | Deputy Military Commissioner | formal and admonishing | Hogun tells Hong Jin to mind his words. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 869
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Hong Jin.md

# Hong Jin (홍진)

- **Safe through:** Chapter 869
- **Aliases:** None
- **Role:** Hong Jin is a Level 22 Deputy Military Commissioner of Shanxi Province, a eunuch and trusted aide to Prince Shangshan, and a former member of the East Depot.
- **Personality:** Composed, socially deft, and ambitious, Hong Jin became a eunuch to escape poverty and save his family, then used his abilities to pursue a broader life.
- **Voice:** Delicate and deferential, using formal, self-effacing language with Prince Shangshan.
- **Relationships:** Hong Jin is devoted to Prince Shangshan, whom the late Emperor entrusted to his care, and trusts Jin Taekyung to help protect him; he left the palace to serve the prince, while his longtime friend and former East Depot cohort Ma Sanbao stayed behind.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 869
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and an active member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented; loyal even when left behind, irreverently self-deprecating, and willing to face danger rather than abandon the person he serves. He is proud, glory-seeking, suspicious of Taekyung, bluntly critical of the family's disgraced third son, and an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad; as a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Fire Dragon Pavilion members accompanying Taekyung. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jeong Hogun.md

# Jeong Hogun (정호군)

- **Safe through:** Chapter 869
- **Aliases:** None
- **Role:** Jeong Hogun is a Thousand Captain of the Embroidered Uniform Guard and a highly skilled martial artist whose force includes dozens of Peak masters.
- **Personality:** Disciplined and resolute, he presents loyalty to the Emperor's command as the foundation of his force's actions.
- **Voice:** Formal and rigid, emphasizing duty to imperial authority.
- **Relationships:** A Thousand Captain in the Embroidered Uniform Guard under Baek Yeon’s command, he is ordered to surveil Prince Shangshan’s party while leaving openings for someone to approach; he says he would give his life to obey an imperial command.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 869
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader.
- **Personality:** Hungry, self-aware, dryly observant, and pragmatic under pressure; accepts extreme personal risk when duty and the lives of others demand it.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; they trust each other deeply, though their bond remains unformalized. Cheongpung is his trusted companion and only true martial rival; Choi Minwoo is his subordinate and trusted manager of media and official arrangements as well as the Peace Guild's Guild Master; Ju Hwaran is a trusted Fire Dragon Pavilion member; Magic Johnson and Chuck Hagel are allied to him; his mother and sister Hayeon are among those he protects; the Skeleton King is his friend and ally; Xiao Shen regards him as an older brother; Jin-ho is his older friend and trusted confidant; he once saved Ju Wongong’s life.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 869
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Jung Ho.md

# Jung Ho (정호)

- **Safe through:** Chapter 869
- **Aliases:** None
- **Role:** Middle-aged Shaolin martial monk and Master of Shaolin's Discipline Hall who leads the traveling group and wields a Zen staff hung with prayer beads.
- **Personality:** Humble, observant, principled, and concerned with the safety of commoners.
- **Voice:** Formal, restrained, and admonitory, with Buddhist phrasing.
- **Relationships:** Unnamed is his young Martial Uncle; he leads the Shaolin monks traveling with him, addresses Sama Pyo as a Benefactor, and is recognized by Jin Taekyung as Park Jung Ho, a former Garam Middle School classmate.

### Ma Sanbao.md

# Ma Sanbao (마삼보)

- **Safe through:** Chapter 869
- **Aliases:** None
- **Role:** Ma Sanbao is the East Depot’s Brush-Holding Eunuch and second-in-command, a Supreme Peak martial artist who has secretly remained in the imperial palace.
- **Personality:** He is vigilant and patient, concealing his loyalties while awaiting the moment to act for the late Emperor.
- **Voice:** He speaks casually and directly with longtime companions, while remaining alert and controlled with new acquaintances.
- **Relationships:** Ma Sanbao is a longtime friend and former East Depot cohort of Hong Jin; he stayed behind to await Prince Shangshan's return and is leading a group seeking to enthrone him.

### Prince Shangshan.md

# Prince Shangshan (상산왕)

- **Safe through:** Chapter 869
- **Aliases:** None
- **Role:** Prince Shangshan, whose personal name is Zhu Bao, is an early-adolescent member of the imperial family and an exceptionally skilled young swordsman who has trained daily for three years.
- **Personality:** Earnest and compassionate, he takes responsibility for his loyal subjects’ hardship, admires Jin Taekyung, seeks candid counsel, and shows composure beyond his years in the face of death and political danger.
- **Voice:** Archaic and formal in the manner of a historical drama, with openly eager and childlike reactions beneath his royal diction.
- **Relationships:** Prince Shangshan Zhu Bao is the Emperor’s only younger full brother; the late Emperor entrusted Hong Jin with his care, and Zhu Bao admires Jin Taekyung and seeks to emulate him.

## Korean source

```text
＃870화



순간 나는 내 귀를 의심했다.

‘내가 지금 무슨 말을 들은 거지.’

솔직히 말하자면, 황궁에 도착한 이후에도 천자와 대면할 수 있을 거라는 생각은 딱히 하지 못했으니까.

당연한 일이다.

상대는 이 광활한 대륙을 지배하는 만인지상(萬人之上)의 존재.

그에 비하면 나는 호패조차 없는 강호의 무뢰배요, 태원진가라는 변변찮은 무가의 자제에 불과하다.

내가 무림에서 어떤 위치인지, 그동안 태원진가가 얼마나 성장했는지는 천자라는 두 글자 앞에서 무의미해진다.

이곳은 황궁이고, 그는 문무백관과 수많은 백성을 거느린 황제니까.

그런데 용의 핏줄로 태어나 반역으로 천하를 움켜쥔 황제가, 홍진도 허락받지 않은 자리에 나를 부르다니.

‘혹시 개노잼 몰래카메라인가.’

마른침을 꿀꺽 삼킨 나는 우선 몸 상태를 점검했다.

새끼손가락으로 귀를 후비고, 손바닥으로 힘주어 뺨을 두세 번 두드린 다음 호흡을 가다듬은 뒤에야 다시 입을 열었다.

“방금 했던 말, 다시 해 봐.”

“뭐?”

“다시 해 보라고. 토씨 하나 빼놓지 말고.”

나를 말 없이 바라보던 정호군이 순순히 대답했다.

“황제 폐하의 부름을 받은 것은 상산왕 전하와 태원진가의 진태경. 이 두 사람뿐이라고 했다.”

저 무뚝뚝한 표정을 보아하니 몰래카메라는 아닌 것이 확실하다. 이 예상치 못한 현실에 잠시 침묵하던 내가 재차 물었다.

“이거 혹시 꿈인가?”

정호군이 담담하게 대꾸했다.

“조금 전에 뺨을 치던데. 그것도 꽤 세게.”

“그랬지.”

“아프지 않았나?”

“아팠지.”

“그럼 꿈이 아니겠지.”

“그렇군.”

두 번째 침묵은 조금 더 길었고, 그 무거운 공기 속에서 가장 먼저 입을 연 것은 내가 아닌 홍진이었다.

“어째서죠?”

“모르오.”

짤막하게 대답한 정호군이 덧붙였다.

“우리 금의위는 그저 황제 폐하의 명을 따를 뿐이오. 어떤 이유나 의문도 필요 없지.”

물론 그건 어디까지나 공무원인 금의위들 입장이었고, 내가 처한 상황은 생각보다 훨씬 복잡했다.

‘왜 갑자기 날 부르는 거지?’

아무래도 느낌이 좋지 않다. 아니, 벌써부터 뒷골이 싸하다.

간밤의 일을 어느 정도 짐작하는 듯하던 정호군의 태도와 역모를 논하던 마삼보의 얼굴이 떠오르는 것을 왜일까.

나는 등줄기를 타고 흐르는 서늘한 기운을 느끼며 입술을 뗐다.

“만약에…… 내가 그 제안을 거절한다면?”

그리고 내가 예상했던 것과 달리, 정호군은 대수롭지 않은 어투로 대답했다.

“그럴 만한 이유라도 있나?”

“요새 몸이 좀 안 좋아서. 게다가 이미 말했다시피 어제 잠을 제대로 못 잤거든.”

“병환이라, 그렇다면 어쩔 수 없지.”

“오. 진짜?”

“물론이다. 이참에 처소도 바꾸는 게 좋겠군.”

“아니, 마음은 고맙지만 괜찮아. 그럴 필요까지는 없…….”

“여봐라. 지금 즉시 형부(刑部)에 연통을 넣어라. 가장 넓은 곳으로 준비하라고.”

“응?”

나는 정호군을 바라보며 눈을 깜빡였다.

그리고 잠시 생각했다.

저 형부가 처제 형부 할 때 그 형부일까. 그렇다면 정호군이 대륙 최초의 트렌스젠더 금위군인가. 그것도 아니라면…….

“저기. 그 형부가 혹시.”

“별것 아니다. 그저 금의위가 관리하는 형집행 기관일 뿐이니 신경 쓰지 말아라.”

“…….”

존나 별거네. 시벌.

눈썹 하나 까딱하지 않는 정호군을 노려보던 나는, 상산왕 주표를 향해 손을 내밀었다.

“가시죠, 전하. 제가 모시겠습니다.”

그리고 금의위들을 따라 전각을 나서는 내 귓가에, 혁무진의 안도 섞인 중얼거림이 닿았다.

“휴, 내가 아니라 다행이다. 진짜 잡혀가는 줄.”

개새끼야.



* * *



황궁은 생각했던 것보다도 훨씬 거대했다.

학창시절 VR 기기로 체험 학습을 했던 자금성보다도 몇 배나 더.

그나마 다행인 점은 금의위가 양심껏 가마를 준비했다는 것이었다.

“오르시지요, 전하.”

“어? 내 건?”

“형부에 다시 연락해야겠군.”

“…….”

물론 나를 위한 가마는 없었고, 황족인 상산왕 주표만이 네 명의 금의위가 들쳐 맨 사인교(四人轎)에 앉아 이동하는 호사를 누렸다.

“이동한다.”

쉬쉬쉬쉭!

정호군의 명령이 떨어지기 무섭게, 쾌속한 속도로 나아가는 황금빛 물결.

혹시 모를 상황을 대비해 상산왕의 사인교 옆에 바짝 붙어선 나는 황궁 곳곳을 빠짐없이 시야에 담았다.

‘알고 있어서 나쁠 건 없으니까.’

최악의 상황을 생각하는 것 역시 내 오랜 습관 중 하나다.

어느 곳에는 어떤 건물이 있고, 그곳을 지키는 군사들의 숫자는 몇이며 수준은 어느 정도인지.

만약 나를 기다리고 있는 것이 천자가 아닌 수많은 창칼이라면, 가장 빠르고 효율적인 도주로를 파악해 두는 것이 우선이었다.

나 혼자가 아닌 다른 누군가와 함께라면 더더욱.

- 전하.

은밀히 흘려보낸 전음(傳音)에 상산왕의 몸이 작게 움찔거린다.

하지만 그건 아주 짧은 순간에 불과했고, 나는 순식간에 평정심을 회복한 어린 왕을 향해 재차 전음을 날렸다.

- 그럴 리는 없겠지만…… 만약 최악의 상황이 닥친다면 제게 모든 걸 맡기셔야 합니다. 아시겠습니까?

상산왕이 작게 고개를 끄덕이려던 그 순간, 나는 행렬의 선두에서 앞만 응시하며 달려가던 정호군의 상반신이 돌아서려는 것을 눈치채고 한발 앞서 입을 열었다.

“저들은 뭐지?”

다행히 상황과 타이밍은 완벽했다.

반 박자 늦게 상산왕을 힐끗 바라본 정호군은, 내 손끝이 향하는 방향을 따라 고개를 돌렸다.

철벅. 철벅.

보보(步步)마다 아직 마르지 않은 빗물과 피가 뒤섞인다.

또 다른 금의위들에게 둘러싸인 채, 피투성이가 되어 어딘가로 끌려가는 수십여 명의 사내를 확인한 정호군이 대답했다.

“보면 알 텐데. 죄인들이다.”

“그건 누구나 알지. 무슨 죄를 지었냐고 물어본 거야.”

“흠천감(欽天監)에 속한 이들이다. 아니, 한때 속해 있었다고 해야 옳겠군.”

“흠천감?”

“천문(天文)을 읽고 분석하는 기관이 바로 흠천감이다. 그리고 저들은 어젯밤의 낙뢰와 폭우를 예측하지 못한 죄로 처벌받겠지.”

“……!”

“괜한 것에 신경 쓰느라 더 이상 시간을 지체하지 마라. 폐하께서 기다리고 계시니.”

나는 말 없이 고개를 끄덕이는 것으로 대답을 대신했지만, 금세 멀어져 버린 죄인들의 뒷모습은 쉽게 눈앞에서 사라지지 않았다.

‘이거…… 제대로 미친놈들이네.’

날씨 한 번 예측 못 했다고 사람을 반 시체 꼴로 만들어 놓다니.

단지 시대상의 분위기라 어쩔 수 없다고 하기에는, 필요 이상으로 훨씬 가혹하게 느껴졌다.

‘아니, 아무리 그런 시대라고 해도 확실히 정상은 아니야.’

생각을 바꾸면 더 많은 것이 보이기 마련.

나는 금의위를 따라 빠르게 이동하는 와중에도 지금껏 눈여겨 보이지 않았던 궁인(宮人)들의 표정을 살폈다.

목각인형처럼 딱딱한 얼굴과 움직임. 사방 어디에나 깔린 군사들을 힐끗거리는 시선에는 미처 숨기지 못한 떨림이 묻어 나오고 있었다.

‘모두가 두려워하고 있다.’

황제의 뜻으로, 혹은 단순히 내뱉은 한 마디로 누군가가 고문당하거나 죽어 나간다.

아무리 담 큰 자라고 한들 감히 거부할 수도, 불만을 내비칠 수도 없을 것이다.

이곳은 한 치의 실수도 용납되어서는 안 되는 황궁이고, 수많은 고관대작은 물론 피붙이마저 살해하며 옥좌에 오른 황제의 권력은 절대적일 테니까.

지금 이 순간에도 피부에 와닿는 싸늘하고 무거운 공기는, 단지 전제군주(專制君主)의 시대관만으로 설명할 수 없는 그 이상의 무언가였다.

‘공포 정치.’

어질고 현명한 현군(賢君)은 하해와 같은 인덕으로 사람을 포용한다.

그러나 폭군(暴君)은 창칼과 공포로 사람들을 자신이 만든 가시 울타리 안으로 밀어 넣는다.

숱한 이야기만 들어봤을 뿐 직접 겪어 본 바는 없지만, 작금의 천자가 어떤 사람인지는 충분히 짐작하고도 남았다.

그리고 가장 큰 문제는…….

‘지금 내가, 그 폭군을 만나기 위해 제 발로 찾아가고 있다는 거지.’

습관처럼 품 안을 더듬자 곧바로 이물감이 느껴진다. 신의(神醫)가 제조한 단환이 들어 있는 작은 꾸러미다.

그 단환에서 풍겨 오는 끔찍할 만큼 고약한 냄새를 떠올리자, 우습게도 약간 마음이 편안해지는 듯했다.

‘만약, 만약 내가 이곳에서 일전을 치른다면 어떻게 될까.’

이걸 다행이라고 불러야 하는지는 모르겠지만, 지금껏 확인한 바로는 황궁에 주둔하고 있는 금의위의 숫자는 수천에서 많게는 일만 남짓.

물론 그것만으로도 대군이라 부르기에는 부족함이 없으나, 황도 전체와 그 인근의 병력을 모두 합친 숫자에 비하면 선녀나 다름없다.

‘중요한 건 황제에게 충성하는 초절정 고수들의 존재. 그리고 업데이트로 인한 시스템의 부재(不在).’

시스템을 사용할 수 없다는 건 엄청난 패널티다.

시스템이 멈췄다는 것은 경험치 획득은 물론이고, 레벨 업을 통한 회복도 불가능하다는 뜻.

거기에 더해 예측하지 못한 공격 방식으로 언제나 쏠쏠하게 재미를 봤던 인벤토리마저 지금은 굳게 닫혀 있었다.

‘이럴 줄 알았다면 무림에서 마지막으로 로그아웃했을 때 백염(白炎)이라도 꺼내 놨었어야 했는데. 아니, 하다못해 화룡갑(火龍鉀)이라도.’

지금까지 해 왔던 과감한 전투 방식은 레벨 업이 있었기에 가능했고, 나보다 높은 경지의 고수들을 꺾을 수 있었던 것은 인벤토리의 성능과 신병이기의 도움이 컸다.

하지만…… 지금의 내게는 아무것도 없다.

위험한 순간마다 내 목숨을 구해 주었던 시스템도, 신병이기도.

유일하게 갖고 있는 것이라고는 옆집 누렁이도 먹다 뱉을 단환 한 꾸러미와 그 썩은 내 풍기는 단환이라도 꾸역꾸역 처먹어야 악화되지 않는 몸뚱어리뿐이다.

아, 물론 그 외에도 몇 개 더 있긴 하다.

어떻게든 지켜야 하는 어린 왕과 환관. 그리고 코골이가 심한 어느 시벌 놈.

‘끝내주는군.’

이쯤 되면 차라리 상산왕에게 천자 암살을 부탁해야 하나 싶을 정도다. 나는 혹시나 하는 마음으로 묵묵히 앞서가는 정호군을 불러세웠다.

“뭐 좀 물어볼 게 있는데. 혹시 촉법소년이라고 아나?”

“촉법, 뭐?”

“촉법소년.”

“그게 뭐지? 처음 들어보는데.”

“……아냐. 됐다.”

생각해보니 연좌죄로 줄줄이 엮여 죽어 나가는 마당에 촉법소년은 개뿔이.

나는 이루어질 수 없는 달콤한 상상을 떠올렸다.

피투성이가 되어 쓰러진 황제. 비명을 듣고 사방에서 몰려온 금의위. 그리고 단검을 든 채 의기양양하게 웃고 있는 상산왕의 모습까지.

- 폐하! 폐하!

- 응. 형님 폐하 내가 죽였쥬?

- 상산왕 전하! 이게 무슨 짓입니까!

- 금의위 아무고토 못 하쥬? 이제 내가 황제쥬?

- 폐하께서 시해되셨다! 지금 당장 역적 주표를 추포하라!

- 응. 나 아직 촉법소년~

“…….”

달콤하면서도 아쉬운 상상이긴 한데, 생각해 보니 이건 이것대로 심각할 것 같기도 하다.

촉법소년이라서 황제가 되다니.

만약 여기가 서구권 세계관이라면 잼민 1세 정도로 불리지 않았을까.

“진태경. 그대는 왜 그런 눈빛으로 나를 보는가?”

“아, 아닙니다.”

내가 의문을 표하는 상산왕에게 차마 속마음을 털어놓지 못하고 둘러댄 그때였다.

우우우웅.

거칠게 떨리는 공기.

만근과도 같은 중압감과 함께 등장한, 서로를 쏙 빼닮은 두 중년인이 행렬을 막아섰다.

“멈춰라.”

“멈춰라.”

같은 얼굴, 같은 체격을 한 쌍둥이가 동시에 한 목소리로 말하는 광경은 언뜻 보면 퍽 우스웠으나 나는 웃지 않았다.

‘초절정 고수.’

확실하다. 이곳은 복마전(伏魔殿)이다.
```

## Final English reading copy

```markdown
# Chapter 870

For a moment, I doubted my own ears.

*What did I just hear?*

To be honest, even after arriving at the imperial palace, I hadn’t really thought I’d get to meet the Son of Heaven.

It was only natural.

He was the exalted ruler of this vast continent, above all others.

Compared to him, I was a lawless thug from the martial world without so much as an identification plaque, and no more than a son of the unimpressive Jin Family of Taiyuan.

Whatever standing I held in Murim, however much the Jin Family of Taiyuan had grown, none of it meant anything in the face of those two words: Son of Heaven.

This was the imperial palace, and he was the Emperor, with civil and military officials and countless subjects under his command.

And yet the Emperor, born of the dragon’s blood and having seized the realm through rebellion, had summoned me to an audience even Hong Jin wasn’t allowed to attend.

*Could this be the world’s lamest hidden-camera prank?*

I swallowed hard, then checked that I was still in working order.

I picked at my ear with my pinky, slapped my cheek two or three times with my palm, and steadied my breathing before I finally spoke again.

“Say that again.”

“What?”

“Say it again. Every last word.”

Jeong Hogun looked at me in silence, then answered without complaint.

“I said that only His Highness Prince Shangshan and Jin Taekyung of the Jin Family of Taiyuan had been summoned by His Majesty the Emperor.”

Judging by his unflappable expression, this definitely wasn’t a hidden-camera prank. I fell silent for a moment, faced with this unexpected reality, then asked again.

“Is this a dream or something?”

Jeong Hogun replied calmly.

“You slapped yourself just now. Pretty hard, too.”

“I did.”

“Did it hurt?”

“It did.”

“Then it wasn’t a dream.”

“I see.”

The second silence lasted a little longer. The first to break it wasn’t me, but Hong Jin.

“Why?”

“I don’t know.”

Jeong Hogun gave a brief answer, then added, “We, the Embroidered Uniform Guard, merely follow His Majesty the Emperor’s orders. We need no reason or explanation.”

Of course, that was the perspective of the Embroidered Uniform Guard, as government officials. My own situation was far more complicated than that.

*Why is he summoning me all of a sudden?*

I had a bad feeling about this. No—I already felt the back of my neck prickling.

Why was I thinking of Jeong Hogun’s manner, which suggested he had some idea what had happened last night, and Ma Sanbao’s face as he spoke of rebellion?

I felt a chill run down my spine and parted my lips.

“What if…I refused the invitation?”

Contrary to what I expected, Jeong Hogun answered in a casual tone.

“Do you have a reason to?”

“I haven’t been feeling well lately. Besides, like I said, I didn’t get much sleep last night.”

“If you’re ill, then there’s no helping it.”

“Oh. Really?”

“Of course. It would be best to move you to a different residence while we’re at it.”

“No, I appreciate the thought, but I’m fine. There’s no need to go that far…”

“Guards. Contact the Ministry of Punishments at once. Tell them to prepare the most spacious accommodations.”

“Huh?”

I blinked at Jeong Hogun.

Then I thought about it for a moment.

Was this the same “brother-in-law” as the one who’d married your wife’s older sister? If so, was Jeong Hogun the continent’s first transgender Imperial Guard? Or was it…

“Um. That Ministry of Punishments…”

“It’s nothing to worry about. It’s simply the institution that administers punishments under the Embroidered Uniform Guard.”

“……”

So it was a big deal. Shit.

I glared at Jeong Hogun, who didn’t so much as twitch an eyebrow, then held out my hand toward Prince Shangshan Zhu Bao.

“Shall we go, Your Highness? I’ll escort you.”

Then, as I followed the Embroidered Uniform Guard out of the pavilion, I heard Hyuk Mujin mutter with relief.

“Phew. Glad it wasn’t me. I really thought I was getting hauled off.”

You little shit.

* * *

The imperial palace was far bigger than I’d imagined.

Several times larger than the Forbidden City I’d toured on a school field trip with a VR headset.

The one saving grace was that the Embroidered Uniform Guard had the decency to prepare a palanquin.

“Please get in, Your Highness.”

“Huh? What about mine?”

“I’ll have to contact the Ministry of Punishments again.”

“……”

Of course, there was no palanquin for me. Only Prince Shangshan, a member of the imperial family, got to enjoy the luxury of riding in a four-man sedan chair carried by four Embroidered Uniform Guards.

“We’re moving.”

*Whoosh, whoosh, whoosh!*

At Jeong Hogun’s order, a golden current surged forward at tremendous speed.

I stayed close beside Prince Shangshan’s sedan chair, ready for anything, and took in every corner of the imperial palace.

*Couldn’t hurt to know the layout.*

Thinking about the worst-case scenario was one of my old habits.

Where each building stood, how many soldiers guarded it, and how strong they were.

If what awaited me wasn’t the Son of Heaven but a forest of spears and blades, I needed to find the fastest, most efficient escape route.

Especially if I had someone else with me.

—Your Highness.

At the Sound Transmission I sent discreetly, Prince Shangshan’s body gave a small jerk.

But it lasted only an instant. I sent another Sound Transmission to the young prince, who had quickly regained his composure.

—It’s unlikely, but…if the worst should happen, you must leave everything to me. Do you understand?

Prince Shangshan was just about to give a small nod when I noticed Jeong Hogun, riding at the head of the procession with his eyes fixed ahead, starting to turn his upper body.

I spoke a beat before he could.

“What are those people?”

Fortunately, my timing was perfect.

Half a beat later, Jeong Hogun glanced toward Prince Shangshan, then followed the direction of my finger.

*Splash. Splash.*

With every step, still-wet rainwater mixed with blood.

Surrounded by another group of Embroidered Uniform Guards, dozens of men were being dragged somewhere, covered in blood. Jeong Hogun saw them and answered.

“You can see for yourself. Prisoners.”

“Anyone can see that. I asked what they did.”

“Those men belong to the Imperial Astronomical Bureau. Or rather, they used to.”

“The Imperial Astronomical Bureau?”

“It’s the institution that observes and analyzes the heavens. And they’ll be punished for failing to predict last night’s lightning and torrential rain.”

“……”

“Don’t waste any more time on something so irrelevant. His Majesty is waiting.”

I answered with a silent nod, but the sight of the prisoners’ backs, already receding into the distance, wouldn’t leave my mind.

*These people are seriously insane.*

They’d beaten men half to death just because they hadn’t predicted the weather.

It felt far more brutal than something you could write off as the way things were in this era.

*No. Even for this era, that’s not normal.*

A change in perspective often revealed more.

Even as I hurried along behind the Embroidered Uniform Guard, I studied the expressions of the palace attendants, whose faces I hadn’t paid much attention to before.

Their faces and movements were stiff as wooden dolls. Whenever their eyes flicked toward the soldiers stationed all around them, I could see a tremor they hadn’t managed to hide.

*Everyone is afraid.*

By the Emperor’s will—or even by a single careless word—someone could be tortured or killed.

No matter how brave you were, you couldn’t refuse or voice your displeasure.

This was the imperial palace, where not even the smallest mistake was tolerated. The Emperor’s power must have been absolute, given that he’d climbed onto the throne after killing countless high officials and even his own blood relatives.

The cold, oppressive atmosphere pressing against my skin even now was something more than the mere nature of an era ruled by an absolute monarch.

*Terror rule.*

A wise and benevolent ruler embraced people with kindness as vast as the sea.

A tyrant, on the other hand, drove them into a thorny enclosure of his own making with spears and fear.

I’d heard plenty of stories, but never experienced it for myself. Even so, I could guess what kind of person the current Son of Heaven was.

And the biggest problem was…

*I’m walking right into his presence of my own accord.*

Out of habit, I reached into my chest. My hand met a small bundle containing pills made by the Divine Physician.

Remembering the unbelievably foul stench coming from them somehow made me feel a little better.

*If—I mean, if—I got into a fight here, what would happen?*

Whether I should call it reassuring or not, based on what I’d seen so far, the Embroidered Uniform Guard stationed in the imperial palace numbered in the thousands, perhaps as many as ten thousand.

That alone was enough to make a great army. Still, compared to the combined forces in the imperial capital and its surrounding areas, they were as lovely as fairies.

*The real issue is the Supreme Peak masters loyal to the Emperor. And the System is unavailable because of the update.*

Not being able to use the System was an enormous penalty.

With the System down, I couldn’t gain EXP, let alone recover by leveling up.

On top of that, my Inventory—the handy trick that had gotten me out of trouble with attacks my enemies never saw coming—was firmly shut.

*If I’d known this would happen, I should’ve taken White Flame out of my Inventory the last time I logged out in Murim. Or at least the Fire Dragon Armor.*

The reckless way I’d fought until now had been possible because I could level up. And I’d been able to beat masters in higher realms than mine thanks in large part to my Inventory and divine weapons.

But…right now, I had nothing.

No System to save my life in a dangerous moment. No divine weapons.

All I had was a bundle of pills that even the neighborhood mongrel would spit out, and a body that would get worse unless I forced myself to swallow the rotten-smelling things.

Oh, and I had a few other things, too.

A young prince and an eunuch I had to protect. And some damn idiot with a bad snoring problem.

*Perfect.*

At this point, I was almost tempted to ask Prince Shangshan to assassinate the Son of Heaven. I called out to Jeong Hogun, who was walking silently ahead of us, just in case.

“Hey, can I ask you something? Ever heard of *chokbeop sonyeon*[^1]?”

“Chokbeop what?”

“*Chokbeop sonyeon*.”

“What’s that? Never heard of it.”

“…Never mind.”

[^1]: A Korean legal term for a child too young to be criminally prosecuted.

Now that I thought about it, people were being strung up and killed through collective punishment. What good was the age of criminal responsibility here?

I pictured a sweet little fantasy that could never come true.

The Emperor, collapsed in a pool of blood. Embroidered Uniform Guards rushing in from every direction at the sound of a scream. And Prince Shangshan, grinning triumphantly with a dagger in his hand.

—Your Majesty! Your Majesty!

—Yeah. I killed my imperial brother, didn’t I?

—His Highness Prince Shangshan! What are you doing?

—The Embroidered Uniform Guard can’t do a thing, can you? Now I’m the Emperor, right?

—His Majesty has been assassinated! Apprehend the traitor Zhu Bao at once!

—Yep. I’m still too young to be prosecuted!

“……”

It was a sweet fantasy, but now that I thought about it, it seemed pretty serious in its own way.

Becoming Emperor because he was too young to be prosecuted.

If this were a Western fantasy setting, wouldn’t they call him Brat the First?

“Jin Taekyung. Why are you looking at me like that?”

“Ah, it’s nothing.”

I was trying to dodge Prince Shangshan’s question without revealing what I’d been thinking when it happened.

*Vrrrrmm.*

The air shook violently.

With an oppressive weight like ten thousand *geun*, two middle-aged men who looked exactly alike appeared and blocked our procession.

“Stop.”

“Stop.”

The twins, identical in face and build, spoke in unison. It looked a little ridiculous—but I didn’t laugh.

*Supreme Peak masters.*

No doubt about it. This place was a demon-slaying battleground.
```

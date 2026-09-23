<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0869.txt",
      "sha256": "0e0a3e0a820aa3d19dd05c3775ffe73f4d07b6629dcaf8104aaf2cb3b1780b57",
      "bytes": 13819
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "5a6d539f78e09e08fd5745a07f1509a5bf46356ac79c9eacc2514dde1b7c3d7f",
      "bytes": 2276
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "c6aa7ac66627729312c888562b57669d8c199736b3a54a323fd416b739461b8d",
      "bytes": 229550
    },
    {
      "path": "characters/Baek Yeon.md",
      "sha256": "33f5117883ab99ee40d14224e6f25055f783cd9b9c2e13e1ddd29ae953db8e79",
      "bytes": 983
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "8e69b28ef0c269b04ef2b86bcfc165fb66b9d9bdfc874e443fd9e0d38efce215",
      "bytes": 759
    },
    {
      "path": "characters/Hong Jin.md",
      "sha256": "76a588420239b02411318099725cf7c59315081cc494d348304abe6883e90a11",
      "bytes": 854
    },
    {
      "path": "characters/Human Butcher.md",
      "sha256": "2ef1e1b16a4e0f628119d7110716838047c17ce180f916aca08d1398d21c85f6",
      "bytes": 667
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "8f7601fd02245d7b6e568cc48f61f3969648fcf76e7ea146937d9fb13699a247",
      "bytes": 1378
    },
    {
      "path": "characters/Jeong Hogun.md",
      "sha256": "6ea17d031e48fd89678663124dff9ee9f94ca2913d210d5692becff9408d9bfd",
      "bytes": 771
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "2cdea5fd2d79b04e6b086784da33429f83a1c4ac6abdf35202f81cd3d3e8fac7",
      "bytes": 1782
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "fc3008578f4fa5d9d46f4dd205ead555b5bd792e61f5ca13934a9eb588f1f2f1",
      "bytes": 622
    },
    {
      "path": "characters/Jung Ho.md",
      "sha256": "28315a80bbda8b6b9f01ebca580cc12331ba741519eceac9a9e671fa14fca260",
      "bytes": 699
    },
    {
      "path": "characters/Ma Sanbao.md",
      "sha256": "ffc97f34239080632202dffb4495aacb7b784d8c38da80d3d1a0ed03c1a202e9",
      "bytes": 765
    },
    {
      "path": "characters/Prince Shangshan.md",
      "sha256": "c024e31ebccb7edfa9a19db2dae4562262843a3e81c43c65faa55b689f03bed1",
      "bytes": 920
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "46e199341ebb22f33e48871aa25b23bb91705400a33866ed280bc03152de17c3",
      "bytes": 256550
    }
  ],
  "estimated_tokens": 12660
}
-->

# Durable State Update — Chapter 869

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
1 and safe_through 869. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 869. Profile updates may replace only one
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
  "chapter": 869,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 869,
    "continuity_sources": [869],
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
    "Prince Shangshan and his party remain inside the imperial palace under surveillance; the Embroidered Uniform Guard arrives at the pavilion, and Taekyung sends Mujin to bring the prince.",
    "The Emperor is the fourth prince who seized the throne in a bloody coup and purge; Ma Sanbao says tens of thousands died and that many victims had no connection to the struggle.",
    "Ma Sanbao secretly remained in the palace, loyal to the late Emperor and ready to help enthrone Prince Shangshan; he says the East Depot Director fell ill five years ago and Ma then began leading their group.",
    "Ma Sanbao says he knows much more about Dark Heaven than Taekyung suspects and offers an appropriate reward for helping enthrone Shangshan; Taekyung suspects the reward is imperial support for the Murim Alliance against Dark Heaven.",
    "Hong Jin left the palace to serve Prince Shangshan, while Ma Sanbao stayed behind to await the prince's return; they are longtime friends and allies.",
    "Taekyung has not decided whether to join Ma Sanbao's plan; he fears that failure would make him and those around him traitors in the Emperor's eyes.",
    "The Emperor relies on opium, which he calls medicine, and breaks his pipe to clear his mind."
  ],
  "continuity_sources": [
    867,
    868
  ],
  "open_questions": [
    "Will Taekyung agree to help enthrone Prince Shangshan, and what action would the plan require?",
    "What does Ma Sanbao know about Dark Heaven, and what is his promised reward?",
    "Who sent the assassin to Qianqing Palace, and what was the intended target?",
    "What does the Emperor intend for Prince Shangshan?",
    "What happened between Hong Jin and the old East Depot Director, and why did Hong leave the East Depot?"
  ],
  "safe_through": 868,
  "temporary_decisions": [
    "Render 동창 병필태감 as “Brush-Holding Eunuch of the East Depot.”",
    "Render 첩형 as “Constable” and 태감 as “Eunuch” in forms of address.",
    "Render 앵속 as “opium” and 곰방대 as “long-stemmed tobacco pipe.”",
    "Render 건청궁 as “Qianqing Palace.”",
    "Render 창공 as “Director” for the East Depot’s head and 연판장 as “blood-signed pact.”"
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 혁무진    | **Hyuk Mujin**     |
| 태원진가   | **Jin Family of Taiyuan**        |
| 살기     | **killing intent**                               |                                                       |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 강호     | **martial world**                                | Prefer “Murim” where the setting itself is meant      |
| 전각     | **pavilion**                                 | Use “hall” only when established for a specific named building |
| 일격     | **One Strike**                         |
| 상태               | **Status**                     |
| 태원     | **Taiyuan**            |
| 백연 | **Baek Yeon** | Commander of the Embroidered Uniform Guard. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 홍진 | **Hong Jin** | Level 22 man at the City Lord's luncheon; delicate in appearance and voice. |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 정호군 | **Jeong Hogun** | Commander of the Embroidered Uniform Guard force confronting Jin. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 정호 | **Jung Ho** | Middle-aged Shaolin martial monk leading the traveling group. |
| 마삼보 | **Ma Sanbao** | The East Depot’s Brush-Holding Eunuch and second-in-command. |
| 상산왕 | **Prince Shangshan** | The City Lord and a member of the imperial family who orders the luncheon. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 천자 | **Son of Heaven** | Honorific title for the Emperor. |
| 도지휘동지 | **Deputy Military Commissioner** | Second-rank military office held by Eunuch Hong |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 기해 | **qi sea** | Name for the dantian, the place where internal energy begins and gathers. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 인내 | **Endurance** | System attribute replacing Toughness. |
| 계도 | **precept blades** | Blades carried by the Hundred and Eight Arhats. |
| 골렘 | **Golem** | Magical rock-based monster classification. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 무한 | **Wuhan** | Capital of Hubei Province near Dongting Lake. |
| 초인 | **superhuman** | A being who has surpassed ordinary human limits. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 만족 | **Man people** | An ethnic group mentioned by the Poison Flower Pavilion owner. |
| 인시 | **Insi** | The traditional time period from three to five in the morning. |
| 신인 | **divine man** | Descriptive term for a human who became something beyond humanity. |
| 묘시 | **the hour of the Rabbit** | Traditional time period following Insi. |
| 가기 | **singing courtesan** | The favored entertainer identity Honglan used in Hubei. |
| 금의위 | **Embroidered Uniform Guard** | Imperial guard force mentioned by Hong Jin. |
| 동창 | **East Depot** | Imperial agency named by Hong Jin. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 홍진 | 진태경 | political_host_to_young_martial_artist | Young Hero Jin; Young Master Jin; Sleeping Dragon of Shanxi | polite, coaxing, and probing | Uses respectful forms while steering Taekyung toward relaying the Escort Bureau proposal and teasing him with the Seongun Escort Bureau. |
| 진태경 | 홍진 | young_martial_artist_to_political_official | Comrade Chairman—no, Deputy Military Commissioner | casual and teasing, then formally corrective | Deliberately jokes with an inappropriate title before correcting himself to Hong Jin's official office. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 정호 | 진태경 | Shaolin Discipline Hall Master to patient and Benefactor | Benefactor Jin | formal-polite | Jung Ho repeatedly uses 진 시주 and 시주. |
| 진태경 | 정호 | patient to Shaolin Discipline Hall Master | Monk | polite and familiar | Taekyung addresses Jung Ho as 스님. |
| 진태경 | 정호군 | young martial artist to senior imperial officer | Commander Jeong | casual and teasing, then conciliatory | Jin addresses him by rank while trying to defuse the standoff. |
| 홍진 | 혁무진 | imperial aide addressing a martial artist accompanying the prince | Martial artist Hyuk | polite and conversational | Uses 혁 무인 when asking whether Mujin knows of an exception. |
| 백연 | 정호군 | commander to subordinate | you | direct and commanding | Uses 네 while testing Jeong Hogun’s obedience. |
| 홍진 | 백연 | imperial aide confronting a senior military officer | you | angry and confrontational | Uses 당신 in an indignant outburst. |
| 진태경 | 백연 | young martial artist confronting an imperial military commander | you | casual and insulting | Refers to Baek as 이 양반 while challenging his conduct. |
| 홍진 | 마삼보 | Longtime friend and former East Depot cohort | Ma Constable; Eunuch Ma | Familiar and respectful | Hong uses both forms while acknowledging Ma’s former and current standing. |
| 마삼보 | 홍진 | Longtime friend and former East Depot cohort | Hong Constable | Familiar and respectful | Ma addresses Hong by his former East Depot title. |
| 백연 | 천자 | imperial officer addressing the Emperor | Your Majesty | formal, deferential in address but openly defiant in private counsel | Baek uses formal honorifics while sharply confronting the Emperor over their shared undertaking. |
| 천자 | 백연 | Emperor addressing his military commander | Baek Yeon | familiar and authoritative | The Emperor addresses Baek by name and gives him a direct warning. |
| 진태경 | 상산왕 | protector addressing a young prince | His Highness | respectful royal address | Taekyung refers to the prince as 상산왕 전하 when ordering Mujin to bring him. |

## Listed compact profiles

### Baek Yeon.md

# Baek Yeon (백연)

- **Safe through:** Chapter 867
- **Aliases:** Blood Envoy
- **Role:** Baek Yeon is the Commander of the Embroidered Uniform Guard, a former martial arts instructor to the Crown Prince, and the Blood Envoy who helped the fourth prince seize the throne and led the purge.
- **Personality:** Politically assured and controlled, he enforces authority with ruthless decisiveness but speaks with striking defiance to the Emperor in private when their shared undertaking is at stake.
- **Voice:** Not established
- **Relationships:** He commands the Embroidered Uniform Guard and serves the Emperor; they share an old promise tied to a great undertaking, and Baek urges the Emperor to restore matters before their adversaries' moves unravel it. He orders Jeong Hogun to surveil Prince Shangshan’s party while leaving openings for an approach, and treats Taekyung as a dangerous potential obstacle.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 867
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Hong Jin.md

# Hong Jin (홍진)

- **Safe through:** Chapter 868
- **Aliases:** None
- **Role:** Hong Jin is a Level 22 Deputy Military Commissioner of Shanxi Province, a eunuch and trusted aide to Prince Shangshan, and a former member of the East Depot.
- **Personality:** Composed, socially deft, and ambitious, Hong Jin became a eunuch to escape poverty and save his family, then used his abilities to pursue a broader life.
- **Voice:** Delicate and deferential, using formal, self-effacing language with Prince Shangshan.
- **Relationships:** Hong Jin is devoted to Prince Shangshan, whom the late Emperor entrusted to his care, and trusts Jin Taekyung to help protect him; he left the palace to serve the prince, while his longtime friend and former East Depot cohort Ma Sanbao stayed behind.

### Human Butcher.md

# Human Butcher (인도)

- **Safe through:** Chapter 850
- **Aliases:** None
- **Role:** Former mysterious Han Chinese mounted-bandit power in Northern Gaoyuan commanding fifty subordinates; a Peak master killed by an unnamed old man in a single move
- **Personality:** Cold, intimidating, and murderous; he kills people as though slaughtering livestock
- **Voice:** Cold, curt, and quietly threatening
- **Relationships:** He is one of four powerful participants at the Northern Gaoyuan gathering, intimidates Temur, and has claimed Ghost Sword Wipeng as his personal target in the proposed attack

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 868
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and an active member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented; loyal even when left behind, irreverently self-deprecating, and willing to face danger rather than abandon the person he serves. He is proud, glory-seeking, suspicious of Taekyung, bluntly critical of the family's disgraced third son, and an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad; as a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Fire Dragon Pavilion members accompanying Taekyung. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jeong Hogun.md

# Jeong Hogun (정호군)

- **Safe through:** Chapter 865
- **Aliases:** None
- **Role:** Jeong Hogun is a Thousand Captain of the Embroidered Uniform Guard and a highly skilled martial artist whose force includes dozens of Peak masters.
- **Personality:** Disciplined and resolute, he presents loyalty to the Emperor's command as the foundation of his force's actions.
- **Voice:** Formal and rigid, emphasizing duty to imperial authority.
- **Relationships:** A Thousand Captain in the Embroidered Uniform Guard under Baek Yeon’s command, he is ordered to surveil Prince Shangshan’s party while leaving openings for someone to approach; he says he would give his life to obey an imperial command.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 868
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader.
- **Personality:** Hungry, self-aware, dryly observant, and pragmatic under pressure; accepts extreme personal risk when duty and the lives of others demand it.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; they trust each other deeply, though their bond remains unformalized. Cheongpung is his trusted companion and only true martial rival; Choi Minwoo is his subordinate and trusted manager of media and official arrangements as well as the Peace Guild's Guild Master; Ju Hwaran is a trusted Fire Dragon Pavilion member; Magic Johnson and Chuck Hagel are allied to him; his mother and sister Hayeon are among those he protects; the Skeleton King is his friend and ally; Xiao Shen regards him as an older brother; Jin-ho is his older friend and trusted confidant; he once saved Ju Wongong’s life.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 868
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Jung Ho.md

# Jung Ho (정호)

- **Safe through:** Chapter 865
- **Aliases:** None
- **Role:** Middle-aged Shaolin martial monk and Master of Shaolin's Discipline Hall who leads the traveling group and wields a Zen staff hung with prayer beads.
- **Personality:** Humble, observant, principled, and concerned with the safety of commoners.
- **Voice:** Formal, restrained, and admonitory, with Buddhist phrasing.
- **Relationships:** Unnamed is his young Martial Uncle; he leads the Shaolin monks traveling with him, addresses Sama Pyo as a Benefactor, and is recognized by Jin Taekyung as Park Jung Ho, a former Garam Middle School classmate.

### Ma Sanbao.md

# Ma Sanbao (마삼보)

- **Safe through:** Chapter 868
- **Aliases:** None
- **Role:** Ma Sanbao is the East Depot’s Brush-Holding Eunuch and second-in-command, a Supreme Peak martial artist who has secretly remained in the imperial palace.
- **Personality:** He is vigilant and patient, concealing his loyalties while awaiting the moment to act for the late Emperor.
- **Voice:** He speaks casually and directly with longtime companions, while remaining alert and controlled with new acquaintances.
- **Relationships:** Ma Sanbao is a longtime friend and former East Depot cohort of Hong Jin; he stayed behind to await Prince Shangshan's return and is leading a group seeking to enthrone him.

### Prince Shangshan.md

# Prince Shangshan (상산왕)

- **Safe through:** Chapter 868
- **Aliases:** None
- **Role:** Prince Shangshan, whose personal name is Zhu Bao, is an early-adolescent member of the imperial family and an exceptionally skilled young swordsman who has trained daily for three years.
- **Personality:** Earnest and compassionate, he takes responsibility for his loyal subjects’ hardship, admires Jin Taekyung, seeks candid counsel, and shows composure beyond his years in the face of death and political danger.
- **Voice:** Archaic and formal in the manner of a historical drama, with openly eager and childlike reactions beneath his royal diction.
- **Relationships:** Prince Shangshan Zhu Bao is the Emperor’s only younger full brother; the late Emperor entrusted Hong Jin with his care, and Zhu Bao admires Jin Taekyung and seeks to emulate him.

## Korean source

```text
＃869화



혁무진을 서둘러 위층으로 올려보낸 뒤, 나는 동이 트기 무섭게 전각을 찾은 금의위들의 앞을 가로막았다.

그리고 가장 먼저 눈에 띄는 익숙한 얼굴을 향해 활짝 웃어 주었다.

“오, 또 보네?”

웃는 얼굴에 침 못 뱉는다는 옛말은 다 거짓이다.

정겹게 손까지 흔들어 주었음에도 눈썹 하나 까딱하지 않은 정호군이 입을 열었다.

“상산왕 전하께서는?”

나는 어깨를 으쓱하며 대답했다.

“조금 전까지만 해도 주무시고 계셨지. 어느 예의범절 없는 놈들이 아침 댓바람부터 들이닥치기 전까지는.”

“이미 묘시(卯時)다. 이는 황궁에서 결코 이른 시각이 아니지.”

묘시라면 오전 다섯 시에서 일곱 시.

저 스톤 골렘 같은 인간에게 아동 인권에 관해 설명하고 싶은 마음이 굴뚝 같았지만, 로마에 온 이상 로마법에 따르는 것이 도리다.

물론 이른 시간부터 금의위를 움직이게 한 것은, 대국의 모든 법 위에 있는 천자의 뜻이겠지만.

“찾아온 용건은?”

“말해 줄 의무는 없다.”

“그럼 내가 맞춰 보지 뭐. 드디어 형제 상봉인가?”

그제야 정호군이 반응을 보였다. 놈은 선명하게 보일 정도로 눈썹을 꿈틀거리며 대답했다.

“상산왕 전하께서 황제 폐하를 알현(謁見)하는 것이다.”

“그래. 그걸 네 글자로 줄이면 형제 상봉이잖아.”

“강호의 무뢰배라 그런지 도무지 이해를 못 하는군. 이건 단순한 형제간의 상봉이 아니라…….”

“아, 이해했다.”

진지한 얼굴로 고개를 끄덕인 내가 말을 이었다.

“다소 복잡한 형제 상봉. 맞지?”

“…….”

“이것도 좀 아닌 것 같아? 너무 길면 우당탕탕 형제 상봉으로 바꿀까? 한 글자가 줄긴 했어도 의미는 비슷해.”

심신의 안정을 되찾으려는 듯, 깊게 심호흡한 정호군이 이내 딱딱한 음성으로 입을 열었다.

“……그 발칙한 주둥이를 조심하는 것이 좋겠군. 감당하지 못할 화를 자초하기 전에.”

“어어? 지금 나한테 경고하는 거야? 어제 느그 지휘사가 우리 전하한테 그런 일 절대 없을 거라고 약속한 거 못 들었어?”

“그건…….”

“표정 보니까 이제야 기억났나 보네. 알겠으면 지금부터라도 잘하자고. 괜히 문제 만들지 말고. 응?”

내가 빙긋 웃으며 정호군의 갑옷을 툭툭 두드리자, 놈의 등 뒤로 철탑처럼 서 있던 금의위들 사이에서 아지랑이 같은 살기가 피어올랐다.

스아아아.

음. 분위기 한 번 끝내주는구만.

필요 이상으로 너무 속을 긁었나 싶기도 한데, 지금껏 겪어 본 바에 의하면 저런 부류의 인간들은 이렇게라도 해야 조금이라도 속내를 드러내기 마련이다.

바로 지금처럼.

“문제를 일으킬 생각이 없는 건 그대도 마찬가지일 텐데. 특히 지금처럼 피곤한 상태에서는 더더욱. 안 그런가? 태원진가의 진태경.”

“뭐?”

“제법 피로해 보이기에 하는 말이다. 마치 간밤에 잠도 제대로 못 잔 사람처럼.”

바보가 아닌 이상, 정호군이 불쑥 던진 저 한 마디가 순수한 의도에서 비롯된 것이 아니라는 것쯤은 눈치챌 수 있을 것이다.

나는 담담하게 가라앉은 놈의 눈동자에 숨어 있는 칼날을 바라보며 내심 중얼거렸다.

‘이놈 봐라…….’

시작부터 무언가 알고 있다는 느낌이 강하게 풍겨 온다.

그러나 생각이 깊어지면 침묵이 길어지고, 이는 곧 상대에게 더욱 큰 의심을 심어 주게 되는 법이다.

그 사실을 알고 있는 나는 짐짓 눈살을 찌푸리며 대답했다.

“잠자리가 편안해야 잠이 오지. 당신 같으면 시커먼 사내놈들이 사방을 포위하고 있는 상황에서 숙면을 취할 수 있겠어?”

“포위가 아니라 호위다. 상산왕 전하를 지키기 위한.”

“혹시 황궁에서는 주로 호위라고 쓰고 포위라고 읽나?”

“대답할 가치도 없는 말이로군.”

“그럼 대답하지 마. 아, 그리고 말 나온 김에 뭐 하나 더 물어보자면…….”

나는 뒤통수를 긁적이며 말을 이었다.

“지엄하신 황제 폐하께서 다스리시는 이 황궁에서, 도대체 무엇으로부터 상산왕 전하를 지키는 거지?”

“……!”

“아니, 생각하면 할수록 좀 희한하더라고. 호위라고 하면 어차피 사방에 깔린 게 군사들인데 금의위까지 나서서 이 정도로 철통 경계할 필요가 있나 싶고. 포위면 또 그것대로 이해가 안 가.”

외통수다. 그것도 완벽한.

이건 둘 중 어느 하나를 선택해도 궁색해질 수밖에 없다.

호위라면 내 말마따나 하등 그럴 이유가 없고, 포위라면 금의위가 천자의 명을 받들어 상산왕을 감시하고 있다는 증언이나 다름 없으니까.

그리고 어느 방향으로 가도 길을 잃어버릴 이 서술형 문제에서 정호군이 선택한 것은, 대답이 아닌 침묵이었다.

이렇게 할 말을 잃어버린 상대를 갈구는 건 내 특기 중의 특기고.

“기껏 물어봤는데, 말이 없네.”

“…….”

“백연. 그 양반이었으면 속 시원하게 무슨 대답이라도 해 줬을 것 같은데. 아직 직급이 딸려서 말을 아끼는 건가?”

“…….”

“이래서 사람은 성공하고 봐야 한다니까. 승진 언제 해. 연차나 병가는 있어? 혹시 내가 말썽이라도 피우면 당신 인사고과에 문제라도 생기나?”

“…….”

“솔직히 어제 느그 지휘사가 갑자기 수하 죽였을 때 놀랐지? 그 인간 평소에도 그렇게 막 나가? 아무한테도 말 안 할 테니까 나한테만 살짝 얘기해 봐. 내가 귓불이 예민해서 귓속말은 좀 그렇고, 전음으로 딱 한 번만.”

짜릿해. 늘 새로워. 갈구는 게 최고야.

올해 발롱도르 수상자가 누구인지는 모르겠지만, 아갈도르는 놓칠 수 없다.

나는 조금이라도 더 많은 정보를 캐내기 위해 종횡무진 혓바닥을 놀리며 정호군을 박박 긁어 댔다.

상관인 백연의 뒷담화부터 시작해서 직장인의 두통 원인인 승진 문제. 금의위의 평균 연봉과 초과 근무 수당에 이어 어떤 똥군기 문화가 있는지까지.

말 그대로 황제 빼고 다 건드렸다.

그리고 생각했던 것 이상으로 오래 참아내던 정호군이 마침내 입을 연 것은, 내가 금의위 짬밥이 만족스럽냐는 질문 이후 가족 관계도에 대해 캐묻기 시작했을 때였다.

“이제 좀…… 적당히 하지.”

중간에 들어간 들숨 한번에서 정호군의 초인적인 인내심이 느껴진다. 약간의 존경심을 담아 고개를 끄덕여 준 내가 대답했다.

“그래서, 아직 노총각이라는 거지?”

“……!”

“오해하지 마. 그 나이에 혼례도 안 올린다고 뭐라고 하는 거 아니다. 막말로 내가 그쪽 부모님도 아닌데 뭘. 그리고 괜히 누구 신세 망칠 일 없으니까 미혼도 나쁘지 않은 것 같아. 이런 일로 기죽을 필요 없으니까 고추, 아니 어깨 쭉 펴고…….”

“이, 이 개새끼가!”

딱 잘라 말하자면, 지금 들려온 이 외침은 정호군의 것이 아니다.

아까 전부터 일곱 빛깔 무지개처럼 알록달록한 안색을 뽐내던 휘하의 금의위들 중 하나가 마침내 화를 참지 못하고 내게 달려든 것이었다.

정확히는, 한 걸음 나서자마자 가로막혔다고 해야 옳겠지만.

턱.

“그만. 두 번 말하지 않겠다.”

깊게 가라앉은 음성과 함께, 굳은살로 가득한 손바닥이 황금빛 갑옷을 가로막는다.

그 손의 주인이 조금 전 모욕당한 상관이라는 것을 확인한 금의위 무사가 끓어오르는 목소리로 부르짖었다.

“천호(千戶)! 어찌 저런 놈을…….”

퍽!

무거우나 느리지 않고, 동시에 가장 효율적인 움직임으로 간결하게 끊어친 일권(一拳).

정호군의 일격에 정확히 턱을 얻어맞은 금의위 무사가 신음도 못 내고 기절하는 모습을 지켜본 나는 나직한 탄성을 흘렸다.

정호군의 보여 준 훌륭한 움직임과는 별개의, 또 다른 이유로.

“이야, 진짜 두 번 안 말하네.”

“상명하복(上命下服). 그것이 대국을 지탱하는 군문의 법도요, 금의위의 규칙이다.”

직접 쓰러트린 수하를 다른 금의위들에게 넘겨준 정호군이 손에 묻은 피를 닦아 내며 말을 이었다.

“지휘사께서 어떠한 해도 입히지 않겠다 약조하셨으니, 이번만큼은 나 역시 그 명을 따를 것이다.”

“이번만큼은?”

“어떠한 명령이라도 상황에 따라 철회되기 마련이지. 예외는 없어.”

목소리는 여느 때처럼 무뚝뚝하지만, 나를 바라보는 정호군의 눈빛은 간밤에 휘몰아친 비바람처럼 스산하고 거칠었다.

황도로 오는 길에도, 도착한 후에도 볼 수 없었던 분위기.

이는 마음이 흐트러졌다는 증거였고, 내 예상은 적중했다.

“글쎄. 아직 상황이 변하지 않았으니 그 명령도 철회되지 않을 것 같은데.”

“그렇게 생각하나?”

“물론.”

내 천연덕스러운 대답에, 거리를 좁혀 바짝 다가온 정호군이 낮게 속삭였다.

“진심으로 경고하건대…… 황제 폐하께서 기거하시는 이 황궁에서 헛된 수작을 부렸다가는 결코 화를 피하지 못할 것이다.”

“누가 들으면 꼭 이미 수작질을 벌인 줄 알겠네.”

“축시(丑時)에서 인시(寅時)까지. 세 개의 붉은 등이 켜져 있더군.”

“뭐?”

“내가 들은 풍월에 의하면 동창의 밀마(密嗎)도 이런 식이었지. 아마.”

순간 심장이 크게 뛰었다.

축시에서 인시. 마삼보가 찾아왔던 시간과 정확히 겹친다.

‘게다가 붉은 등을 이용한 신호까지.’

정호군이 내 귓가에 속삭이느라 시선을 마주하지 않은 것이 다행이다.

그렇지 않았다면 조금, 아주 조금의 미동이라도 보이고 말았을 테니까.

그러나 지금껏 많은 일을 겪으며 감정을 억누르는 방법을 알게 된 나다.

그 누구도 눈치챌 수 없을 만큼 조용히, 그리고 순식간에 호흡과 맥박을 가라앉힌 나는 피식 웃었다.

“홍진. 그 양반이 붉은색이라면 환장을 하더라고. 입술도 맨날 그 색으로 칠하고 다니는 거 보면 감 오지?”

“그래, 감이 와. 그 역시 한때 동창에 소속되어 있던 몸. 그런 구닥다리 밀마를 사용해서라도 힘이 되어 줄 자를 불러야 했을 테니까.”

이건 의심인가, 확신인가.

무수한 생각들이 섬광처럼 뇌리를 스쳐 지나간 끝에 내가 내놓은 결론은 하나였다.

‘함정.’

홍진도, 마삼보도 그리 허술한 사람들이 아니다.

아니, 오히려 지금껏 내가 만난 모든 사람을 통틀어도 철저하기로는 능히 다섯 손가락 안에 들고도 남을 것이다.

황궁은, 동창은 그런 사람들만 살아남을 수 있는 곳이니까.

게다가 정호군이 알아차릴 정도로 뻔한 밀마라면, 그런 위험을 감수하고 접선했을 리는 더더욱 없었다.

‘걸려들어선 안 된다.’

모든 판단은 찰나라고 부를 만큼 순식간에 이루어졌다.

곧장 이어진 내 움직임도.

툭.

바짝 붙어 있는 정호군의 몸을 밀쳐 낸 나는 최대한 자연스럽게 입꼬리를 말아 올렸다.

“아주 시발, 소설을 써라. 소설을.”

“…….”

“동창이고 나발이고, 난 몰라. 어쩌다가 복잡한 일에 얽혀서 머리 좀 싸매고 생각에 잠기긴 했지. 정 못 믿겠으면 뭐, 누명이라도 씌워 보든가.”

물증도, 증인도 없다.

이건 함정이다.

조금의 흔들림도 없는 내 눈빛을 빤히 바라보던 정호군이 할 대답은, 이미 정해져 있는 것이나 다름없었다.

“간밤에는 유난히 소란스러웠지. 거친 비바람과 뇌성벽력이 쉬지 않고 울려 퍼졌어.”

“그래서?”

“별다른 뜻은 없다. 그뿐이야.”

저 새카만 눈동자에 담긴 것은 아직 놓지 못한 의심의 끈일까.

아니면 단순한 떠보기가 실패했을 때 나오는 아쉬움일까.

이번만큼은 나도 확실한 판단을 내릴 수 없었고, 그럴 만한 시간도 주어지지 않았다.

“오래 기다렸나요?”

저벅. 저벅.

특유의 중성적인 목소리와 함께 계단을 걸어 내려오는 세 사람의 발걸음.

즉각 자세를 바로 한 정호군과 휘하의 금의위들이 막 모습을 드러낸 어린 왕을 향해 군례를 올렸다.

“신, 금의위 천호 정호군. 상산왕 전하를 모셔 가기 위해 왔나이다.”

긴장된 낯빛을 한 상산왕의 뒤에 서 있던 홍진이 쓴웃음을 지었다.

“여전히 성미가 급하시군요. 아니, 하루씩이나 참았으니 생각보다 오래 기다리셨다고 해야 하나.”

“말씀을 삼가시오, 도지휘동지.”

“무섭기도 해라. 그럼 나는…….”

“그대는 함께 갈 수 없소.”

서늘하게 홍진의 말을 잘라 낸 정호군이, 생각지도 못한 뒷말을 이었다.

“황제 폐하의 부름을 받은 것은 상산왕 전하와 태원진가의 진태경. 이 두 사람뿐이니까.”

뭐?
```

## Final English reading copy

```markdown
# Chapter 869

After hurrying Hyuk Mujin upstairs, I blocked the Embroidered Uniform Guards who had come to the pavilion at the crack of dawn.

Then I flashed a broad smile at the familiar face that caught my eye first.

“Oh, fancy seeing you again.”

So much for the old saying that nobody spits in a smiling face. It was a complete lie.

Jeong Hogun didn’t so much as twitch an eyebrow, even when I waved at him like an old friend.

“Where is His Highness Prince Shangshan?”

I shrugged. “He was asleep until just now. Before a bunch of rude bastards barged in at the crack of dawn.”

“It is already the hour of the Rabbit. That is by no means early in the imperial palace.”

The hour of the Rabbit meant five to seven in the morning.

I was itching to explain children’s rights to this man, who was built like a Stone Golem, but when in Rome, you did as the Romans did.

Though, of course, it was the Son of Heaven’s will—above every law in the Great Nation—that had set the Embroidered Uniform Guard in motion so early.

“What brings you here?”

“I have no obligation to tell you.”

“Then let me guess. Is it finally time for a family reunion?”

At that, Jeong Hogun reacted. His eyebrow twitched so sharply I could see it from where I stood.

“His Highness Prince Shangshan is to have an audience with His Majesty the Emperor.”

“Right. Four characters: brothers reunited.”

“You’re a lawless thug from the martial world, so it seems you can’t understand. This is not merely a reunion between brothers. It’s…”

“Oh, I get it.”

I nodded with a solemn expression.

“A somewhat complicated reunion of brothers. Right?”

“……”

“Not quite? Too long? How about a chaotic reunion of brothers? One word shorter, but pretty much the same thing.”

Jeong Hogun took a deep breath, as if trying to calm himself, then spoke in a stiff voice.

“……You’d be wise to watch that insolent mouth of yours before you bring down trouble you can’t handle.”

“Whoa, are you warning me? Didn’t you hear your commander promise our prince yesterday that nothing like that would happen?”

“That was…”

“Judging by your face, you just remembered. If you understand, then let’s do better from now on. Don’t go making trouble for no reason. Okay?”

I smiled and patted Jeong Hogun’s armor. Behind him, the killing intent of the Embroidered Uniform Guards standing like iron towers began to rise in waves.

*Whoosh.*

Now, that was some atmosphere.

Maybe I’d gotten under their skin more than I needed to. But in my experience, people like him only showed even a hint of what they were thinking when you provoked them like this.

Just like now.

“You don’t want to cause trouble either, do you? Especially when you’re this tired. Isn’t that right, Jin Taekyung of the Jin Family of Taiyuan?”

“What?”

“You look rather exhausted. As if you didn’t get much sleep last night.”

Anyone with half a brain could tell that Jeong Hogun hadn’t tossed out that remark on a whim.

I looked into his calmly lowered eyes and the blade hidden in them, thinking to myself:

*Well, look at this guy…*

From the very start, he’d given off the strong impression that he knew something.

But the deeper you thought, the longer you stayed silent—and that only gave your opponent more reason to suspect you.

Knowing that, I furrowed my brow and answered,

“You need to feel comfortable to get any sleep. Could you sleep soundly with a bunch of menacing men surrounding you on every side?”

“They are not surrounding you. They are guarding His Highness Prince Shangshan.”

“Does the imperial palace write ‘guard’ but pronounce it ‘surround’?”

“That isn’t worth answering.”

“Then don’t answer. Oh, while we’re on the subject, let me ask you something else…”

I scratched the back of my head and went on.

“In this imperial palace ruled by His August Majesty the Emperor, what exactly are you guarding His Highness from?”

“……!”

“No, the more I think about it, the stranger it gets. If you’re guarding him, there are already soldiers everywhere. I don’t see why the Embroidered Uniform Guard needs to be on this kind of high alert. And if you’re surrounding him, that makes even less sense.”

Checkmate. A perfect one, too.

Either answer would leave him in an awkward position.

If he said they were guarding the prince, then as I’d said, there was no reason for all this. If he said they were surrounding him, that would be as good as admitting that the Embroidered Uniform Guard was monitoring Prince Shangshan on the Son of Heaven’s orders.

And in this essay question where either answer would lead to a dead end, Jeong Hogun chose silence.

Getting under the skin of someone who’d run out of things to say was my specialty.

“I asked you something, but you’ve gone quiet.”

“……”

“If it were Baek Yeon, I bet he’d give me a straight answer. Are you keeping your mouth shut because you haven’t made the rank yet?”

“……”

“People really have to get ahead in life. When’s your next promotion? Do you get annual leave or sick days? If I cause trouble, does that mess up your performance review?”

“……”

“Honestly, you were surprised when your commander suddenly killed one of his subordinates yesterday, weren’t you? Is he always that reckless? I won’t tell anyone, so just whisper it to me. My earlobes are sensitive, so whispering’s a little awkward. Just use Sound Transmission once.”

Thrilling. Always fresh. Getting under someone’s skin was the best.

I had no idea who’d won this year’s Ballon d’Or, but I wasn’t about to miss out on the Mouth d’Or.

I let my tongue run wild, trying to pry out as much information as I could, and needled Jeong Hogun relentlessly.

I started with gossip about his superior, Baek Yeon, then moved on to promotion woes, a working person’s headache. I asked about the Embroidered Uniform Guard’s average salary and overtime pay, then about what kind of hazing culture they had.

In short, I went after everyone but the Emperor.

And Jeong Hogun held out far longer than I’d expected. He finally opened his mouth after I asked whether the Embroidered Uniform Guard’s chow was any good—and then started digging into his family tree.

“That’s enough… Give it a rest.”

I could feel his superhuman patience in the one breath he took between words. I nodded with a touch of respect, then replied,

“So you’re still an unmarried bachelor, then?”

“……!”

“Don’t get me wrong. I’m not criticizing you for being unmarried at your age. I mean, I’m not your parents. And staying single isn’t so bad—you won’t ruin someone else’s life by accident. So don’t let it get you down. Keep your package—no, your shoulders—up…”

“You son of a bitch!”

To be precise, the shout I heard just then didn’t come from Jeong Hogun.

One of the Embroidered Uniform Guards under him, whose face had been changing colors like a seven-hued rainbow for a while now, had finally lost his temper and charged at me.

Or, more accurately, he took one step forward before someone stopped him.

*Thud.*

“Enough. I won’t say it twice.”

With a voice low and heavy, a calloused palm stopped the guard’s golden armor in its tracks. The guard who recognized the hand as belonging to the very superior I’d just insulted shouted in a voice bubbling with rage.

“Thousand Captain! How can you let that bastard—”

*Whack!*

One punch, delivered with a heavy yet swift movement—brief, precise, and ruthlessly efficient.

Jeong Hogun’s fist caught the Embroidered Uniform Guard squarely on the jaw. The man crumpled without even a groan, and I watched him fall with a quiet sound of admiration.

For another reason entirely than the impressive way Jeong Hogun had moved.

“Wow. You really didn’t say it twice.”

“Obeying those above you—that is the law of the military that sustains the Great Nation, and the rule of the Embroidered Uniform Guard.”

Jeong Hogun handed the subordinate he’d knocked out to the other guards, wiped the blood from his hand, and continued.

“The Commander promised no harm would come to you. For this once, I will follow that order as well.”

“For this once?”

“Any order can be withdrawn depending on the circumstances. There are no exceptions.”

His voice was as blunt as ever, but the gaze he fixed on me was bleak and wild, like the storm that had raged through the night.

It was a side of him I hadn’t seen on the way to the imperial capital or after we’d arrived.

A sign that his composure had slipped—and my guess had been right.

“Well, the situation hasn’t changed yet, so I don’t think that order’s been withdrawn.”

“Is that what you think?”

“Of course.”

At my casual reply, Jeong Hogun closed the distance and leaned in to whisper.

“I’m warning you in all seriousness… If you try anything foolish in this imperial palace, where His Majesty the Emperor resides, you will not escape the consequences.”

“Anyone listening would think I’d already pulled something.”

“From the hour of the Ox to the hour of the Tiger. Three red lanterns were lit.”

“What?”

“From what I’ve heard, that was how the East Depot’s secret signals worked. Probably.”

My heart gave a hard thump.

From the hour of the Ox to the hour of the Tiger. Exactly when Ma Sanbao had come to see me.

*And the signal used red lanterns, too.*

It was lucky that Jeong Hogun wasn’t looking me in the eye while whispering in my ear.

Otherwise, he might have noticed the tiniest flicker of a reaction.

But I’d been through a lot by now. I’d learned how to keep my emotions in check.

I quietly and instantly steadied my breathing and pulse, so no one could notice, then gave a short laugh.

“Hong Jin’s crazy about the color red. You can tell by how he paints his lips that color every day, right?”

“Yeah, I can tell. He used to belong to the East Depot, after all. He must have needed to call in someone who could help, even if it meant using such an outdated secret signal.”

Was it suspicion, or certainty?

After countless thoughts flashed through my mind like streaks of lightning, I reached a single conclusion.

*A trap.*

Neither Hong Jin nor Ma Sanbao was careless.

No—in terms of thoroughness, they were easily in the top five of everyone I’d ever met.

The imperial palace, the East Depot—only people like that could survive in places like these.

And if the secret signal was obvious enough for Jeong Hogun to figure out, there was no way they’d risk meeting while using it.

*I can’t take the bait.*

All those judgments came in an instant—so fast it barely seemed like time had passed.

My next move followed just as quickly.

*Tap.*

I pushed Jeong Hogun away from where he stood right up against me, then curled my lips into a smile as naturally as I could.

“Fuck, you’re writing a whole damn novel.”

“……”

“To hell with the East Depot. I don’t know anything about that. I got tangled up in something complicated and spent a while thinking it over. If you really don’t believe me, go ahead and try to frame me.”

No physical evidence. No witnesses.

It was a trap.

Jeong Hogun stared at my eyes, which didn’t waver in the slightest. His answer was practically decided already.

“The night was unusually noisy. A fierce storm and thunder kept roaring without letup.”

“So?”

“It means nothing. That’s all.”

Was the thing in those black eyes a suspicion he still couldn’t let go of?

Or disappointment because his attempt to sound me out had failed?

For once, I couldn’t tell for sure, and I wasn’t given time to try.

“Have you been waiting long?”

*Step. Step.*

Three people came down the stairs, their footsteps accompanied by a familiar, androgynous voice.

Jeong Hogun and the Embroidered Uniform Guards immediately straightened and saluted the young prince, who had just appeared.

“I, Jeong Hogun, Thousand Captain of the Embroidered Uniform Guard, have come to escort His Highness Prince Shangshan.”

Hong Jin, standing behind Prince Shangshan, who wore a tense expression, gave a wry smile.

“You’re still as impatient as ever. No, perhaps I should say you’ve waited longer than expected, since you did manage to hold out for an entire day.”

“Mind your words, Deputy Military Commissioner.”

“How frightening. Then I’ll…”

“You cannot come with us.”

Jeong Hogun cut Hong Jin off coldly, then added something neither of us had expected.

“His Majesty the Emperor summoned only His Highness Prince Shangshan and Jin Taekyung of the Jin Family of Taiyuan. Those two alone.”

What?
```
